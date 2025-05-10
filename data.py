control_procedures = [
    {
        "id": "CP-10341",
        "name": "Smartcard Authentication for Privileged Accounts",
        "description": "All privileged accounts must use PIV/CAC-based smartcard authentication for workstation and server logins. This enhances non-repudiation and prevents password-based compromise. Enforcement is applied via group policy and PKI validation mechanisms.",
        "eval_metadata": {
            "expected_co_match": "CO-203"
        },  # Identity and Privilege Management
    },
    {
        "id": "CP-10342",
        "name": "Mandatory Endpoint Detection & Response",
        "description": "All endpoints must have an approved EDR solution installed and configured with real-time protection. Agents must be registered in the enterprise console with policy compliance enforced at all times.",
        "eval_metadata": {"expected_co_match": "CO-204"},  # Endpoint Protection
    },
    {
        "id": "CP-10343",
        "name": "Automated Patch Deployment for Critical Servers",
        "description": "Servers must auto-install security patches within 7 days of release for Critical or High vulnerabilities. Compliance is tracked via vulnerability scanning and SCCM/WSUS reporting. Manual patching is only permitted under documented exceptions.",
        "eval_metadata": {
            "expected_co_match": "CO-205"
        },  # Vulnerability and Patch Management
    },
    {
        "id": "CP-10344",
        "name": "Controlled Change Deployment Pipeline",
        "description": "Production changes must go through formal change management and an automated deployment pipeline. Change records must include risk impact and rollback steps. Unauthorized changes are flagged and reported to IT compliance.",
        "eval_metadata": {"expected_co_match": "CO-206"},  # Change Management
    },
    {
        "id": "CP-10345",
        "name": "Restricted Removable Media Use",
        "description": "All removable media ports are disabled by default across endpoints. Exceptions must be requested, reviewed monthly, and centrally logged. Unauthorized usage triggers alerts.",
        "eval_metadata": {"expected_co_match": "CO-207"},  # Data Loss Prevention
    },
    {
        "id": "CP-10346",
        "name": "Block Unauthorized Sync Clients",
        "description": "File sharing and cloud sync clients such as Dropbox and Google Drive are blocked on corporate laptops unless connected through secure VPN. DLP policies enforce this restriction at network and endpoint level.",
        "eval_metadata": {"expected_co_match": "CO-207"},  # Data Loss Prevention
    },
    {
        "id": "CP-10347",
        "name": "Security Events Audit Logging",
        "description": "Appropriate audit logging for security-related events are to be enabled to provide telemetry to the Security Operations Center.",
        "eval_metadata": {
            "expected_co_match": "CO-209"
        },  # Security Monitoring and Logging
    },
    {
        "id": "CP-10348",
        "name": "Encryption Backups for Critical Assets",
        "description": "Weekly encrypted backups of critical assets must be stored in segregated backup domains. Backup success and restore testing are logged and reviewed quarterly.",
        "eval_metadata": {
            "expected_co_match": "CO-208"
        },  # Encryption and Data Protection (alternative: CO-212: CO-212: Backup & Recovery)
    },
    {
        "id": "CP-10349",
        "name": "Developer Secure Coding Training",
        "description": "Developers must complete secure coding training annually. Pull requests for production must include evidence of OWASP Top 10 risk evaluation. Secure coding checklists are enforced during code review.",
        "eval_metadata": {"expected_co_match": "CO-213"},  # Secure Software Development
    },
    {
        "id": "CP-10350",
        "name": "Time-Bound Vendor Access",
        "description": "Vendors accessing internal systems must be granted time-bound credentials. Sessions are monitored in real-time and subject to endpoint controls. Vendor access must be reviewed weekly by asset owners.",
        "eval_metadata": {"expected_co_match": "CO-214"},  # Third-Party Risk Management
    },
    # Invalid CP
    {
        "id": "CP-00000",
        "name": "Expected To be Have No Match",
        "description": "lorem ipsum brown fox over the wall flying tomatoes fencing cats",
        "eval_metadata": {"expected_co_match": None},  # No match expected
    },
    # Ultra vague
    {
        "id": "CP-11111",
        "name": "IT Security",
        "description": "Computers must be protected and secure.",
        "eval_metadata": {"expected_co_match": None},  # No match expected
    },
]

control_objectives = [
    {
        "id": "CO-203",
        "name": "Identity and Privilege Management",
        "description": "Ensure strong identity governance and privileged account management. Enforce secure authentication and minimize standing access.",
    },
    {
        "id": "CO-204",
        "name": "Endpoint Protection",
        "description": "Maintain endpoint visibility and defense using centrally managed protection agents. This may include anti malware solution or software to provide endpoint machine security telemtry.",
    },
    {
        "id": "CO-205",
        "name": "Vulnerability and Patch Management",
        "description": "Ensure timely remediation of software vulnerabilities. Establish automated patching processes for critical systems.",
    },
    {
        "id": "CO-206",
        "name": "Change Management",
        "description": "Control infrastructure and application changes via structured workflows to reduce operational risk.",
    },
    {
        "id": "CO-207",
        "name": "Data Loss Prevention",
        "description": "Prevent unauthorized data exfiltration through technical and administrative safeguards.",
    },
    {
        "id": "CO-208",
        "name": "Encryption and Data Protection",
        "description": "Ensure encryption of data in transit and at rest using approved algorithms.",
    },
    {
        "id": "CO-209",
        "name": "Security Monitoring and Logging",
        "description": "Implement centralized logging and monitoring to detect and respond to anomalies.",
    },
    {
        "id": "CO-210",
        "name": "Threat Detection and Response",
        "description": "Identify and respond to threats through real-time alerts and correlation rules.",
    },
    {
        "id": "CO-211",
        "name": "Configuration Management",
        "description": "Standardize and harden system configurations to reduce attack surface.",
    },
    {
        "id": "CO-212",
        "name": "Backup and Recovery",
        "description": "Ensure that business-critical systems can be recovered in the event of data loss or corruption.",
    },
    {
        "id": "CO-213",
        "name": "Secure Software Development",
        "description": "Promote secure development lifecycle practices to minimize vulnerabilities in code.",
    },
    {
        "id": "CO-214",
        "name": "Third-Party Risk Management",
        "description": "Monitor and control third-party access to systems and data.",
    },
    {
        "id": "CO-215",
        "name": "Incident Response",
        "description": "Enable timely investigation and containment of security incidents.",
    },
    {
        "id": "CO-216",
        "name": "Regulatory Compliance",
        "description": "Maintain compliance with legal and regulatory cybersecurity obligations.",
    },
    {
        "id": "CO-217",
        "name": "Change Control Governance",
        "description": "Ensure traceability and auditability for all changes to critical infrastructure.",
    },
]
