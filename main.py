from sentence_transformers import SentenceTransformer, CrossEncoder, util
from data import control_procedures, control_objectives
import csv

# Toggle this flag to control verbosity
VERBOSE = True

# Load models
if VERBOSE:
    print("🔧 Loading models...")

sbert_model = SentenceTransformer("all-mpnet-base-v2")
cross_encoder_rank = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
cross_encoder_nli = CrossEncoder("cross-encoder/nli-deberta-v3-base")

if VERBOSE:
    print("✅ Models loaded.")

# Prepare CO texts and embeddings
co_texts = [f'{co["name"]}: {co["description"]}' for co in control_objectives]
co_embeddings = sbert_model.encode(co_texts, convert_to_tensor=True)

results = []

for cp in control_procedures:
    cp_id = cp["id"]
    cp_name = cp["name"]
    cp_desc = cp["description"]
    cp_text = f"{cp_name}: {cp_desc}"

    if VERBOSE:
        print(f"\n🔍 Evaluating CP {cp_id} - {cp_name}")
        print(f"📝 Description: {cp_desc}")

    # Step 1: SBERT retrieval
    cp_embedding = sbert_model.encode(cp_text, convert_to_tensor=True)
    cosine_scores = util.cos_sim(cp_embedding, co_embeddings)[0]
    top_k = min(5, len(control_objectives))
    top_results = cosine_scores.topk(k=top_k)

    if VERBOSE:
        print(f"\n📌 [Step 1] Top-{top_k} SBERT retrieval candidates:")
    top_candidates = []
    for rank, (score, idx) in enumerate(
        zip(top_results.values, top_results.indices), 1
    ):
        co = control_objectives[idx]
        co_text = f"{co['name']}: {co['description']}"
        if VERBOSE:
            print(f"  {rank}. CO {co['id']} ({score.item():.3f}) → {co['name']}")
        top_candidates.append((co, co_text, score.item()))

    # Step 2: CrossEncoder re-ranking
    rerank_inputs = [(cp_text, co_text) for (_, co_text, _) in top_candidates]
    rerank_scores = cross_encoder_rank.predict(rerank_inputs)

    if VERBOSE:
        print("\n📊 [Step 2] Semantic re-ranking:")
        for i, ((co, _, _), score) in enumerate(zip(top_candidates, rerank_scores), 1):
            print(f"  {i}. CO {co['id']} → {co['name']} (Score: {score:.3f})")

    reranked = sorted(
        zip(top_candidates, rerank_scores), key=lambda x: x[1], reverse=True
    )
    (best_co, best_co_text, sbert_score), rank_score = reranked[0]

    if VERBOSE:
        print(f"\n✅ Best CO by re-ranking: {best_co['id']} → {best_co['name']}")

    # Step 3: NLI entailment check
    nli_logits = cross_encoder_nli.predict(
        [(cp_text, best_co_text)], apply_softmax=True
    )[0]
    entailment_score = nli_logits[2]

    if VERBOSE:
        print("\n🧠 [Step 3] NLI entailment:")
        print(
            f"   Entailment: {entailment_score:.3f}, Neutral: {nli_logits[1]:.3f}, Contradiction: {nli_logits[0]:.3f}"
        )

    # Final decision
    threshold = 0.1  # Original 0.85
    if entailment_score < threshold:
        match_id = "N/A"
        match_name = "No confident match"
        match_desc = "-"
        if VERBOSE:
            print(f"⚠️  Below threshold ({threshold}). No confident match.")
    else:
        match_id = best_co["id"]
        match_name = best_co["name"]
        match_desc = best_co["description"]

    # Always show CP → CO result and scores
    print(f"\n🔐 CP {cp_id}: {cp_name}")
    print(f"→ Matched to CO {match_id}: {match_name}")
    print(
        f"   SBERT: {sbert_score:.3f} | Ranker: {rank_score:.3f} | Entailment: {entailment_score:.3f}"
    )

    # Output: Save result
    # Format SBERT results (full list with bullet points)
    sbert_ranked = sorted(top_candidates, key=lambda x: x[2], reverse=True)
    top_sbert_str = "\n".join(
        f"- {co['id']}: {co['name'][:40]} ({score:.3f}),"
        for (co, _, score) in sbert_ranked
    )

    # Format Ranker results (full list with bullet points)
    top_ranker_str = "\n".join(
        f"- {co['id']}: {co['name'][:40]} ({score:.3f}),"
        for ((co, _, _), score) in reranked
    )

    # Expected match
    expected_co_match = cp.get("eval_metadata", {}).get("expected_co_match", None)
    expected_id = expected_co_match
    expected_name = (
        next(
            (co["name"] for co in control_objectives if co["id"] == expected_id), "None"
        )
        if expected_id
        else "None"
    )
    actual_pair = f"{match_id}: {match_name}"
    expected_pair = f"{expected_id}: {expected_name}"
    evaluation = "✅" if match_id == expected_id else "❌"

    results.append(
        {
            "cp_id": cp_id,
            "cp_name": cp_name,
            "expected_co_match": expected_pair,
            "actual_co_match": actual_pair,
            "evaluation": evaluation,
            "sbert_top_results": top_sbert_str,
            "ranker_top_results": top_ranker_str,
            "entailment_score": round(entailment_score, 3),
        }
    )

# Export CSV
if VERBOSE:
    print("\n💾 Writing results to cp_co_matches.csv")

with open("cp_co_matches.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

if VERBOSE:
    print("✅ Done.")
