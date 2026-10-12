# CyberABC — Cybersecurity Academic Books Collection

~~~text
  +------------------------------------------------------------------+
  |        CYBERABC / CYBERSECURITY ACADEMIC BOOKS COLLECTION        |
  +------------------------------------------------------------------+
  |     ________    ________    ________    ________    ________     |
  |    |   IR   |  |  CYBR  |  |  INFO  |  |  DATA  |  |  PRIV  |    |
  |    | 23.1%  |  |  1.6%  |  |  0.0%  |  |  0.0%  |  |  0.0%  |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |     ________    ________    ________    ________    ________     |
  |    |  GRC   |  | HUMAN  |  |  ARCH  |  | CRYPT  |  |  WEB3  |    |
  |    |  0.5%  |  |  0.0%  |  |  0.0%  |  |  0.0%  |  |  0.0%  |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |     ________    ________    ________    ________    ________     |
  |    |  IAM   |  |  NET   |  |  SYS   |  | CLOUD  |  |  APP   |    |
  |    |  0.0%  |  |  0.0%  |  |  0.0%  |  |  0.0%  |  |  0.0%  |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |     ________    ________    ________    ________    ________     |
  |    |  SOC   |  |  DFIR  |  |  CTI   |  |  RED   |  |   AI   |    |
  |    |  0.0%  |  |  0.0%  |  |  0.0%  |  |  0.0%  |  |  0.0%  |    |
  |    |________|  |________|  |________|  |________|  |________|    |
  |==================================================================|
  |                 ________    ________    ________                 |
  |                |  PQC   |  |   OT   |  |  CRIT  |                |
  |                |  0.0%  |  |  0.0%  |  |  8.8%  |                |
  |                |________|  |________|  |________|                |
  |==================================================================|
  |            ENGLISH DRAFT CHAPTERS / 23 ACADEMIC AREAS            |
  +------------------------------------------------------------------+
~~~

**English writing progress:** each percentage is the share of that area's planned English chapters with at least 300 words of authored teaching in a manuscript draft. The bookshelf is refreshed from the manuscripts on each local publication; it does not indicate a finished book or an A4 page count. [Sigil key, exact counts and method](WRITING_PROGRESS.md).

**Incident Response book-length checkpoints:** [Rapid](levels/rapid-1-month/incident-response-resilience/README.md): 128/300 A4 pages (42.7% of page floor) · [Professional](levels/professional-6-months/incident-response-resilience/README.md): 63/300 A4 pages (21.0% of page floor) · [Technical](levels/technical-18-months/incident-response-resilience/README.md): 124/300 A4 pages (41.3% of page floor) · [Doctoral](levels/doctorate-2-years/incident-response-resilience/README.md): 122/300 A4 pages (40.7% of page floor). These are measured lengths of English drafts, not completion percentages; the writing queue runs from rapid to doctoral level.

**A public, free Markdown learning library for cybersecurity, information security, data governance and digital defense.** Its long-term vision is an online university-style curriculum from first practice to advanced research.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned text is dedicated under [CC0 1.0](LICENSE); factual sources are cited and third-party works retain their own rights. Course titles are educational plans, not accredited degrees.

[**Follow the complete 207-course study path**](STUDY_PATH.md) · [**Browse by formation level**](levels/README.md) · [**Start Incident Response**](levels/rapid-1-month/incident-response-resilience/README.md) · [**View all 23 areas**](AREA_MAP.md) · [**Find a skill**](SKILLS.md)

**Start at lesson 01:** [Cybersecurity / rapid / English](levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md#ch-01). At each chapter's end, follow **Continue studying** to the previous chapter, course index or next chapter. The same navigation is present in every book plan. Follow each [course's chapter index](levels/rapid-1-month/cybersecurity/en/SUBJECTS.md) into the next course until the last doctoral chapter. Unwritten chapters are labeled as plans, not lessons.

## How this library is organized

1. **Formation level** — choose one of nine pathways below.
2. **Academic area** — every level has all 23 areas, each represented by one course home.
3. **Language edition** — every course has one planned principal book per language. English is authored and reviewed first.
4. **Subjects and chapters** — each curricular subject is one chapter in that book, with teaching, examples, exercises and a final worked-answer appendix.
5. **One course skill** — a single `SKILL.md` guides AI clients through the whole course and its chapters. Playbooks are supplementary.

~~~text
levels/<level>/<area>/
├── README.md               course home: objectives, all languages and links
├── skill/SKILL.md          one skill for this course
└── <language>/
    ├── README.md           edition and editorial status
    ├── SUBJECTS.md         all subjects and chapter links
    ├── MATERIALS.md        labs, cases, exercises and references
    └── book/
        ├── PLAN.md          chapter summaries and learning sequence
        └── MANUSCRIPT.md    authored draft, only when present
~~~

**Current structure:** 9 levels × 23 areas = **207 courses and course skills**. With 9 language editions, **1,863 books are planned**. The English grades contain **4,186 subject-chapters**. These are plans, not finished books. 7 English manuscripts are public drafts; **zero books have passed the complete-book gate**.

**Progress, measured separately:** the folders and course/book plans cover 100% of the current 23-area catalog. Only 336 of 4,186 English chapter briefs have a manually tailored teaching outline so far; the other summaries are template-based working plans. Authored English chapter drafts: **54 of 4,186 (1.3%)**, with the area-by-area method in the [writing progress table](WRITING_PROGRESS.md) and [percentages for all 207 courses](COURSE_WRITING_PROGRESS.md). Completed book editions: **0 of 1,863 (0%)**. All 1,863 editions still need to pass the publication gate; see the [progress review](STRUCTURE_REVIEW.md).

A finished book must have **at least 300 verified A4 pages** and **50 substantive exercises with worked results**, plus technical, source, rights, language and accessibility review. The [book standard](BOOK_STANDARD.md) explains the gate.

## 1. Choose a formation level

| Level | Planned duration | Subjects / book | Planned exercises | Open all 23 areas |
|---|---:|---:|---:|---|
| Rapid course | 1 month | 4 | 50 | [Open level](levels/rapid-1-month/README.md) |
| Professional course | 6 months | 12 | 60 | [Open level](levels/professional-6-months/README.md) |
| Technical course | 18 months | 18 | 72 | [Open level](levels/technical-18-months/README.md) |
| Technologist course | 3 years | 30 | 90 | [Open level](levels/technologist-3-years/README.md) |
| Bachelor's course | 4 years | 40 | 120 | [Open level](levels/bachelors-4-years/README.md) |
| Engineering course | 5 years | 50 | 150 | [Open level](levels/engineering-5-years/README.md) |
| Postgraduate course | 2 years | 12 | 60 | [Open level](levels/postgraduate-2-years/README.md) |
| Master's course | 2 years | 8 | 50 | [Open level](levels/masters-2-years/README.md) |
| Doctoral research track | 2 years | 8 | 50 | [Open level](levels/doctorate-2-years/README.md) |

## 2. English draft progress for every course

Each linked percentage opens one course page with its nine language editions, one skill, book, chapter index, materials, related project and practice playbooks. The percentage is **authored English chapters with at least 300 words of teaching ÷ planned chapters**. It updates when manuscripts and this README are published from the maintainer's machine. **100% means every chapter has a draft start; it does not mean the book or any translation is complete.** All 207 courses are shown here. See [course counts, manuscript words and A4 measurements](COURSE_WRITING_PROGRESS.md) and the [book completion gate](BOOK_STANDARD.md). The five schools are descriptive groupings; the folder hierarchy begins with formation level.

| School / area | Rapid | Professional | Technical | Technologist | Bachelor's | Engineering | Postgraduate | Master's | Doctorate |
|---|---|---|---|---|---|---|---|---|---|
| **Cybersecurity** (School of Cybersecurity Foundations) | [75.0%](levels/rapid-1-month/cybersecurity/README.md) | [0.0%](levels/professional-6-months/cybersecurity/README.md) | [0.0%](levels/technical-18-months/cybersecurity/README.md) | [0.0%](levels/technologist-3-years/cybersecurity/README.md) | [0.0%](levels/bachelors-4-years/cybersecurity/README.md) | [0.0%](levels/engineering-5-years/cybersecurity/README.md) | [0.0%](levels/postgraduate-2-years/cybersecurity/README.md) | [0.0%](levels/masters-2-years/cybersecurity/README.md) | [0.0%](levels/doctorate-2-years/cybersecurity/README.md) |
| **Information security** (School of Cybersecurity Foundations) | [0.0%](levels/rapid-1-month/information-security/README.md) | [0.0%](levels/professional-6-months/information-security/README.md) | [0.0%](levels/technical-18-months/information-security/README.md) | [0.0%](levels/technologist-3-years/information-security/README.md) | [0.0%](levels/bachelors-4-years/information-security/README.md) | [0.0%](levels/engineering-5-years/information-security/README.md) | [0.0%](levels/postgraduate-2-years/information-security/README.md) | [0.0%](levels/masters-2-years/information-security/README.md) | [0.0%](levels/doctorate-2-years/information-security/README.md) |
| **Data governance** (School of Data and Security Governance) | [0.0%](levels/rapid-1-month/data-governance/README.md) | [0.0%](levels/professional-6-months/data-governance/README.md) | [0.0%](levels/technical-18-months/data-governance/README.md) | [0.0%](levels/technologist-3-years/data-governance/README.md) | [0.0%](levels/bachelors-4-years/data-governance/README.md) | [0.0%](levels/engineering-5-years/data-governance/README.md) | [0.0%](levels/postgraduate-2-years/data-governance/README.md) | [0.0%](levels/masters-2-years/data-governance/README.md) | [0.0%](levels/doctorate-2-years/data-governance/README.md) |
| **Privacy and data protection** (School of Data and Security Governance) | [0.0%](levels/rapid-1-month/privacy-data-protection/README.md) | [0.0%](levels/professional-6-months/privacy-data-protection/README.md) | [0.0%](levels/technical-18-months/privacy-data-protection/README.md) | [0.0%](levels/technologist-3-years/privacy-data-protection/README.md) | [0.0%](levels/bachelors-4-years/privacy-data-protection/README.md) | [0.0%](levels/engineering-5-years/privacy-data-protection/README.md) | [0.0%](levels/postgraduate-2-years/privacy-data-protection/README.md) | [0.0%](levels/masters-2-years/privacy-data-protection/README.md) | [0.0%](levels/doctorate-2-years/privacy-data-protection/README.md) |
| **Security governance, risk and compliance** (School of Data and Security Governance) | [25.0%](levels/rapid-1-month/security-governance-risk-compliance/README.md) | [0.0%](levels/professional-6-months/security-governance-risk-compliance/README.md) | [0.0%](levels/technical-18-months/security-governance-risk-compliance/README.md) | [0.0%](levels/technologist-3-years/security-governance-risk-compliance/README.md) | [0.0%](levels/bachelors-4-years/security-governance-risk-compliance/README.md) | [0.0%](levels/engineering-5-years/security-governance-risk-compliance/README.md) | [0.0%](levels/postgraduate-2-years/security-governance-risk-compliance/README.md) | [0.0%](levels/masters-2-years/security-governance-risk-compliance/README.md) | [0.0%](levels/doctorate-2-years/security-governance-risk-compliance/README.md) |
| **Human factors and cyber policy** (School of Data and Security Governance) | [0.0%](levels/rapid-1-month/human-factors-policy/README.md) | [0.0%](levels/professional-6-months/human-factors-policy/README.md) | [0.0%](levels/technical-18-months/human-factors-policy/README.md) | [0.0%](levels/technologist-3-years/human-factors-policy/README.md) | [0.0%](levels/bachelors-4-years/human-factors-policy/README.md) | [0.0%](levels/engineering-5-years/human-factors-policy/README.md) | [0.0%](levels/postgraduate-2-years/human-factors-policy/README.md) | [0.0%](levels/masters-2-years/human-factors-policy/README.md) | [0.0%](levels/doctorate-2-years/human-factors-policy/README.md) |
| **Security architecture and engineering** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/security-architecture/README.md) | [0.0%](levels/professional-6-months/security-architecture/README.md) | [0.0%](levels/technical-18-months/security-architecture/README.md) | [0.0%](levels/technologist-3-years/security-architecture/README.md) | [0.0%](levels/bachelors-4-years/security-architecture/README.md) | [0.0%](levels/engineering-5-years/security-architecture/README.md) | [0.0%](levels/postgraduate-2-years/security-architecture/README.md) | [0.0%](levels/masters-2-years/security-architecture/README.md) | [0.0%](levels/doctorate-2-years/security-architecture/README.md) |
| **Cryptography and trust services** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/cryptography-trust/README.md) | [0.0%](levels/professional-6-months/cryptography-trust/README.md) | [0.0%](levels/technical-18-months/cryptography-trust/README.md) | [0.0%](levels/technologist-3-years/cryptography-trust/README.md) | [0.0%](levels/bachelors-4-years/cryptography-trust/README.md) | [0.0%](levels/engineering-5-years/cryptography-trust/README.md) | [0.0%](levels/postgraduate-2-years/cryptography-trust/README.md) | [0.0%](levels/masters-2-years/cryptography-trust/README.md) | [0.0%](levels/doctorate-2-years/cryptography-trust/README.md) |
| **Web3, blockchain and cryptoasset security** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/web3-blockchain-security/README.md) | [0.0%](levels/professional-6-months/web3-blockchain-security/README.md) | [0.0%](levels/technical-18-months/web3-blockchain-security/README.md) | [0.0%](levels/technologist-3-years/web3-blockchain-security/README.md) | [0.0%](levels/bachelors-4-years/web3-blockchain-security/README.md) | [0.0%](levels/engineering-5-years/web3-blockchain-security/README.md) | [0.0%](levels/postgraduate-2-years/web3-blockchain-security/README.md) | [0.0%](levels/masters-2-years/web3-blockchain-security/README.md) | [0.0%](levels/doctorate-2-years/web3-blockchain-security/README.md) |
| **Identity and access management** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/identity-access/README.md) | [0.0%](levels/professional-6-months/identity-access/README.md) | [0.0%](levels/technical-18-months/identity-access/README.md) | [0.0%](levels/technologist-3-years/identity-access/README.md) | [0.0%](levels/bachelors-4-years/identity-access/README.md) | [0.0%](levels/engineering-5-years/identity-access/README.md) | [0.0%](levels/postgraduate-2-years/identity-access/README.md) | [0.0%](levels/masters-2-years/identity-access/README.md) | [0.0%](levels/doctorate-2-years/identity-access/README.md) |
| **Network and communications security** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/network-communications/README.md) | [0.0%](levels/professional-6-months/network-communications/README.md) | [0.0%](levels/technical-18-months/network-communications/README.md) | [0.0%](levels/technologist-3-years/network-communications/README.md) | [0.0%](levels/bachelors-4-years/network-communications/README.md) | [0.0%](levels/engineering-5-years/network-communications/README.md) | [0.0%](levels/postgraduate-2-years/network-communications/README.md) | [0.0%](levels/masters-2-years/network-communications/README.md) | [0.0%](levels/doctorate-2-years/network-communications/README.md) |
| **Systems, endpoints and hardware security** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/systems-endpoints-hardware/README.md) | [0.0%](levels/professional-6-months/systems-endpoints-hardware/README.md) | [0.0%](levels/technical-18-months/systems-endpoints-hardware/README.md) | [0.0%](levels/technologist-3-years/systems-endpoints-hardware/README.md) | [0.0%](levels/bachelors-4-years/systems-endpoints-hardware/README.md) | [0.0%](levels/engineering-5-years/systems-endpoints-hardware/README.md) | [0.0%](levels/postgraduate-2-years/systems-endpoints-hardware/README.md) | [0.0%](levels/masters-2-years/systems-endpoints-hardware/README.md) | [0.0%](levels/doctorate-2-years/systems-endpoints-hardware/README.md) |
| **Cloud and container security** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/cloud-containers/README.md) | [0.0%](levels/professional-6-months/cloud-containers/README.md) | [0.0%](levels/technical-18-months/cloud-containers/README.md) | [0.0%](levels/technologist-3-years/cloud-containers/README.md) | [0.0%](levels/bachelors-4-years/cloud-containers/README.md) | [0.0%](levels/engineering-5-years/cloud-containers/README.md) | [0.0%](levels/postgraduate-2-years/cloud-containers/README.md) | [0.0%](levels/masters-2-years/cloud-containers/README.md) | [0.0%](levels/doctorate-2-years/cloud-containers/README.md) |
| **Application and software supply chain security** (School of Secure Engineering) | [0.0%](levels/rapid-1-month/application-supply-chain/README.md) | [0.0%](levels/professional-6-months/application-supply-chain/README.md) | [0.0%](levels/technical-18-months/application-supply-chain/README.md) | [0.0%](levels/technologist-3-years/application-supply-chain/README.md) | [0.0%](levels/bachelors-4-years/application-supply-chain/README.md) | [0.0%](levels/engineering-5-years/application-supply-chain/README.md) | [0.0%](levels/postgraduate-2-years/application-supply-chain/README.md) | [0.0%](levels/masters-2-years/application-supply-chain/README.md) | [0.0%](levels/doctorate-2-years/application-supply-chain/README.md) |
| **Security operations and blue team** (School of Cyber Defense and Operations) | [0.0%](levels/rapid-1-month/security-operations-blue-team/README.md) | [0.0%](levels/professional-6-months/security-operations-blue-team/README.md) | [0.0%](levels/technical-18-months/security-operations-blue-team/README.md) | [0.0%](levels/technologist-3-years/security-operations-blue-team/README.md) | [0.0%](levels/bachelors-4-years/security-operations-blue-team/README.md) | [0.0%](levels/engineering-5-years/security-operations-blue-team/README.md) | [0.0%](levels/postgraduate-2-years/security-operations-blue-team/README.md) | [0.0%](levels/masters-2-years/security-operations-blue-team/README.md) | [0.0%](levels/doctorate-2-years/security-operations-blue-team/README.md) |
| **Incident response and cyber resilience** (School of Cyber Defense and Operations) | [100.0%](levels/rapid-1-month/incident-response-resilience/README.md) | [100.0%](levels/professional-6-months/incident-response-resilience/README.md) | [100.0%](levels/technical-18-months/incident-response-resilience/README.md) | [0.0%](levels/technologist-3-years/incident-response-resilience/README.md) | [0.0%](levels/bachelors-4-years/incident-response-resilience/README.md) | [0.0%](levels/engineering-5-years/incident-response-resilience/README.md) | [0.0%](levels/postgraduate-2-years/incident-response-resilience/README.md) | [0.0%](levels/masters-2-years/incident-response-resilience/README.md) | [100.0%](levels/doctorate-2-years/incident-response-resilience/README.md) |
| **Digital forensics and malware analysis** (School of Cyber Defense and Operations) | [0.0%](levels/rapid-1-month/digital-forensics-malware/README.md) | [0.0%](levels/professional-6-months/digital-forensics-malware/README.md) | [0.0%](levels/technical-18-months/digital-forensics-malware/README.md) | [0.0%](levels/technologist-3-years/digital-forensics-malware/README.md) | [0.0%](levels/bachelors-4-years/digital-forensics-malware/README.md) | [0.0%](levels/engineering-5-years/digital-forensics-malware/README.md) | [0.0%](levels/postgraduate-2-years/digital-forensics-malware/README.md) | [0.0%](levels/masters-2-years/digital-forensics-malware/README.md) | [0.0%](levels/doctorate-2-years/digital-forensics-malware/README.md) |
| **Threat intelligence and OSINT** (School of Cyber Defense and Operations) | [0.0%](levels/rapid-1-month/threat-intelligence-osint/README.md) | [0.0%](levels/professional-6-months/threat-intelligence-osint/README.md) | [0.0%](levels/technical-18-months/threat-intelligence-osint/README.md) | [0.0%](levels/technologist-3-years/threat-intelligence-osint/README.md) | [0.0%](levels/bachelors-4-years/threat-intelligence-osint/README.md) | [0.0%](levels/engineering-5-years/threat-intelligence-osint/README.md) | [0.0%](levels/postgraduate-2-years/threat-intelligence-osint/README.md) | [0.0%](levels/masters-2-years/threat-intelligence-osint/README.md) | [0.0%](levels/doctorate-2-years/threat-intelligence-osint/README.md) |
| **Authorized offensive security and red team** (School of Cyber Defense and Operations) | [0.0%](levels/rapid-1-month/offensive-security-red-team/README.md) | [0.0%](levels/professional-6-months/offensive-security-red-team/README.md) | [0.0%](levels/technical-18-months/offensive-security-red-team/README.md) | [0.0%](levels/technologist-3-years/offensive-security-red-team/README.md) | [0.0%](levels/bachelors-4-years/offensive-security-red-team/README.md) | [0.0%](levels/engineering-5-years/offensive-security-red-team/README.md) | [0.0%](levels/postgraduate-2-years/offensive-security-red-team/README.md) | [0.0%](levels/masters-2-years/offensive-security-red-team/README.md) | [0.0%](levels/doctorate-2-years/offensive-security-red-team/README.md) |
| **AI and machine-learning security** (School of Emerging and Critical Systems) | [0.0%](levels/rapid-1-month/ai-security/README.md) | [0.0%](levels/professional-6-months/ai-security/README.md) | [0.0%](levels/technical-18-months/ai-security/README.md) | [0.0%](levels/technologist-3-years/ai-security/README.md) | [0.0%](levels/bachelors-4-years/ai-security/README.md) | [0.0%](levels/engineering-5-years/ai-security/README.md) | [0.0%](levels/postgraduate-2-years/ai-security/README.md) | [0.0%](levels/masters-2-years/ai-security/README.md) | [0.0%](levels/doctorate-2-years/ai-security/README.md) |
| **Quantum and post-quantum security** (School of Emerging and Critical Systems) | [0.0%](levels/rapid-1-month/quantum-post-quantum-security/README.md) | [0.0%](levels/professional-6-months/quantum-post-quantum-security/README.md) | [0.0%](levels/technical-18-months/quantum-post-quantum-security/README.md) | [0.0%](levels/technologist-3-years/quantum-post-quantum-security/README.md) | [0.0%](levels/bachelors-4-years/quantum-post-quantum-security/README.md) | [0.0%](levels/engineering-5-years/quantum-post-quantum-security/README.md) | [0.0%](levels/postgraduate-2-years/quantum-post-quantum-security/README.md) | [0.0%](levels/masters-2-years/quantum-post-quantum-security/README.md) | [0.0%](levels/doctorate-2-years/quantum-post-quantum-security/README.md) |
| **OT, IoT and cyber-physical security** (School of Emerging and Critical Systems) | [0.0%](levels/rapid-1-month/ot-iot-security/README.md) | [0.0%](levels/professional-6-months/ot-iot-security/README.md) | [0.0%](levels/technical-18-months/ot-iot-security/README.md) | [0.0%](levels/technologist-3-years/ot-iot-security/README.md) | [0.0%](levels/bachelors-4-years/ot-iot-security/README.md) | [0.0%](levels/engineering-5-years/ot-iot-security/README.md) | [0.0%](levels/postgraduate-2-years/ot-iot-security/README.md) | [0.0%](levels/masters-2-years/ot-iot-security/README.md) | [0.0%](levels/doctorate-2-years/ot-iot-security/README.md) |
| **Critical infrastructure and sector security** (School of Emerging and Critical Systems) | [0.0%](levels/rapid-1-month/critical-sector-security/README.md) | [0.0%](levels/professional-6-months/critical-sector-security/README.md) | [0.0%](levels/technical-18-months/critical-sector-security/README.md) | [0.0%](levels/technologist-3-years/critical-sector-security/README.md) | [0.0%](levels/bachelors-4-years/critical-sector-security/README.md) | [0.0%](levels/engineering-5-years/critical-sector-security/README.md) | [0.0%](levels/postgraduate-2-years/critical-sector-security/README.md) | [0.0%](levels/masters-2-years/critical-sector-security/README.md) | [100.0%](levels/doctorate-2-years/critical-sector-security/README.md) |

[Detailed area map](mapa-areas-ciberseguranca.md) · [All course and book links](COURSE_GUIDE.md) · [English subject counts](CURRICULUM_GRID.md)

## First English book in progress

The [Incident Response rapid-course draft](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md) contains initial teaching for four chapters, 50 exercises and 50 worked results. Chapter 1 includes a testable evidence-readiness contract, a readiness workshop, a claim-falsification ledger and an offline evidence-bound lab with eight verified output lines; six exercises and their worked answers now assess these additional distinctions. Chapter 2 adds a decision-oriented preservation queue, a query-envelope and source/copy/interpretation review, the VQ2 quiet-query lab with seven verified output lines, two earlier evidence-and-time labs plus delayed-arrival, evidence-package and cross-source correlation activities; six exercise-answer pairs were deepened. Chapter 3 adds competing cause hypotheses, a cause-to-fix verification lesson, explicit approval/execution receipts and the eleven-line G3-DG decision-gate lab to its write-pause validation, guided booking reconciliation, read-only CSV comparison and three-candidate recovery replay, each with worked results. Chapter 3 also uses the British Library's cited incident review to distinguish a real recovery lesson from the fictional teaching case. All 50 numbered exercises across four chapters have explicit objectives, inputs, assessment criteria and worked answers; Chapter 4 adds a six-artifact model tabletop, an evidence-linked score-calibration lesson, an after-action report, an approval-route replay and an audience-specific communication replay. The manuscript currently contains 60,157 whitespace-separated words across teaching, exercises, answers and references; that count is not an A4 page result. It remains a **draft**: the chapters need substantial expansion, technical review and a release-quality A4 verification. A dated page-count preflight is recorded in the [progress review](STRUCTURE_REVIEW.md). All 182 Incident Response chapter briefs across nine levels and 154 Cybersecurity briefs have individual teaching plans; the remaining English chapters are on the editorial work queue. The earlier [Cybersecurity](levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md) and [Security Governance](levels/rapid-1-month/security-governance-risk-compliance/en/book/MANUSCRIPT.md) drafts are preserved. The [professional Incident Response draft](levels/professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md) has a teaching draft for all twelve subjects and 60 exercise-answer pairs in one continuous fictional case. [The technical Incident Response draft](levels/technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md) has all eighteen subject drafts and 72 worked exercises. Chapters 1–5 received a further teaching pass on service outcomes, protocol evidence, identifier joins, CSV record coordinates and evidence custody; Chapter 6.1 now adds four route contracts, cache and identity negative tests, seven reproducible offline scenarios, and a deeper EX021 with its worked answer. Chapters 14–18 cover scripted triage, cross-service joins, runbook safety, containment/recovery gates and a staged handoff. The [doctoral Incident Response draft](levels/doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) has eight authored research-method chapters and 50 exercise-answer pairs; its preliminary A4 length is recorded separately. All remain drafts: the 300-page A4 length and independent reviews remain open. Every authored chapter and planned summary ends with previous/index/next navigation. All four Incident Response books remain incomplete.

**A4 length check:** The current hash-checked A4 preflight measures **128 of the 300-page minimum (42.7% of the page floor)**. This measures length only; the book remains a draft until all teaching and review requirements pass. [View the source-specific measurement](STRUCTURE_REVIEW.md#a4-preflight).

## Language sequence

**English → Portuguese → Spanish → Hebrew → French → Russian → German → Chinese → Japanese.** Complete and review the English collection before translating; each later language receives its own technical and linguistic review. Current non-English folders contain working outlines, not completed translations.

## Existing projects

**27 curated active repositories from the [hiagokinlevi account](https://github.com/hiagokinlevi?tab=repositories), checked 11 October 2026.** This inventory includes the current learning platform, 13 original security projects, two research repositories, nine forks, and two profile or website repositories. It is a project index, separate from the **23 CyberABC academic areas**. Each linked repository has its own scope, state, authorship history, and license; inclusion here does not make its contents part of a completed CyberABC course.

### Learning platform · 1

- [CyberABC](https://github.com/hiagokinlevi/CyberABC) — public curriculum, study plans, books, and learner materials.

### Original security software · 13

| Focus | Repositories |
|---|---|
| Detection and response | [honeypot-foundry](https://github.com/hiagokinlevi/honeypot-foundry) · [dfir-attack-lab](https://github.com/hiagokinlevi/dfir-attack-lab) · [ir-playbooks-automation](https://github.com/hiagokinlevi/ir-playbooks-automation) |
| Applications and delivery | [waf-defense-rulepacks](https://github.com/hiagokinlevi/waf-defense-rulepacks) · [secure-pipeline-blueprints](https://github.com/hiagokinlevi/secure-pipeline-blueprints) · [offensive-gvuln](https://github.com/hiagokinlevi/offensive-gvuln) |
| Cloud and infrastructure | [cloud-posture-watch](https://github.com/hiagokinlevi/cloud-posture-watch) · [iam-audit-lab](https://github.com/hiagokinlevi/iam-audit-lab) · [container-defense-stack](https://github.com/hiagokinlevi/container-defense-stack) |
| Secrets and exposure | [secret-leak-sentinel](https://github.com/hiagokinlevi/secret-leak-sentinel) · [phishing-surface-monitor](https://github.com/hiagokinlevi/phishing-surface-monitor) |
| AI and cryptography | [ai-security-guardrails](https://github.com/hiagokinlevi/ai-security-guardrails) · [cryptologik](https://github.com/hiagokinlevi/cryptologik) |

### Study routes from the original projects

Each original project links to a related CyberABC course. The course home links its nine editions, principal book, chapter index, one skill and supplementary playbooks.

| Project | Related course |
|---|---|
| [honeypot-foundry](https://github.com/hiagokinlevi/honeypot-foundry) | [Security operations and blue team](levels/rapid-1-month/security-operations-blue-team/README.md) |
| [dfir-attack-lab](https://github.com/hiagokinlevi/dfir-attack-lab) | [Digital forensics and malware analysis](levels/rapid-1-month/digital-forensics-malware/README.md) |
| [ir-playbooks-automation](https://github.com/hiagokinlevi/ir-playbooks-automation) | [Incident response and cyber resilience](levels/rapid-1-month/incident-response-resilience/README.md) |
| [waf-defense-rulepacks](https://github.com/hiagokinlevi/waf-defense-rulepacks) | [Network and communications security](levels/rapid-1-month/network-communications/README.md) |
| [secure-pipeline-blueprints](https://github.com/hiagokinlevi/secure-pipeline-blueprints) | [Application and software supply chain security](levels/rapid-1-month/application-supply-chain/README.md) |
| [offensive-gvuln](https://github.com/hiagokinlevi/offensive-gvuln) | [Authorized offensive security and red team](levels/rapid-1-month/offensive-security-red-team/README.md) |
| [cloud-posture-watch](https://github.com/hiagokinlevi/cloud-posture-watch) | [Cloud and container security](levels/rapid-1-month/cloud-containers/README.md) |
| [iam-audit-lab](https://github.com/hiagokinlevi/iam-audit-lab) | [Identity and access management](levels/rapid-1-month/identity-access/README.md) |
| [container-defense-stack](https://github.com/hiagokinlevi/container-defense-stack) | [Cloud and container security](levels/rapid-1-month/cloud-containers/README.md) |
| [secret-leak-sentinel](https://github.com/hiagokinlevi/secret-leak-sentinel) | [Information security](levels/rapid-1-month/information-security/README.md) |
| [phishing-surface-monitor](https://github.com/hiagokinlevi/phishing-surface-monitor) | [Threat intelligence and OSINT](levels/rapid-1-month/threat-intelligence-osint/README.md) |
| [ai-security-guardrails](https://github.com/hiagokinlevi/ai-security-guardrails) | [AI and machine-learning security](levels/rapid-1-month/ai-security/README.md) |
| [cryptologik](https://github.com/hiagokinlevi/cryptologik) | [Cryptography and trust services](levels/rapid-1-month/cryptography-trust/README.md) |

### Original research · 2

- [ADAI-Autonomous-Defensive-Artificial-Intelligence](https://github.com/hiagokinlevi/ADAI-Autonomous-Defensive-Artificial-Intelligence) — research on governed autonomous defensive AI.
- [DAI-Decripte-Artificial-Intelligence-LLM](https://github.com/hiagokinlevi/DAI-Decripte-Artificial-Intelligence-LLM) — research on a security-focused language model and verifiable authority.

For related learning, open the [AI and machine-learning security course](levels/rapid-1-month/ai-security/README.md) and choose a formation level from the [complete level index](levels/README.md). The research repositories remain independent sources.

### Forked reference collections · 9

These are **forks of other projects**. Their upstream authorship and license terms remain with their respective sources; check each repository before reuse.

- [AwesomeResponsibleAI](https://github.com/hiagokinlevi/AwesomeResponsibleAI) · [awesome-llm-security-alignment](https://github.com/hiagokinlevi/awesome-llm-security-alignment) · [Awesome-LLM4SecOps](https://github.com/hiagokinlevi/Awesome-LLM4SecOps)
- [LLM-security-and-privacy](https://github.com/hiagokinlevi/LLM-security-and-privacy) · [prompt-injection-defenses](https://github.com/hiagokinlevi/prompt-injection-defenses) · [awesome-agentic-hardening](https://github.com/hiagokinlevi/awesome-agentic-hardening)
- [awesome-ai-agent-governance](https://github.com/hiagokinlevi/awesome-ai-agent-governance) · [awesome-ai-security](https://github.com/hiagokinlevi/awesome-ai-security) · [awesome-llm-security](https://github.com/hiagokinlevi/awesome-llm-security)

### Public profile and website · 2

- [hiagokinlevi](https://github.com/hiagokinlevi/hiagokinlevi) — GitHub profile repository.
- [hiagokinlevi.github.io](https://github.com/hiagokinlevi/hiagokinlevi.github.io) — public portfolio website.

The [project categories](CATEGORIES.md) give context for the original security software. New public repositories can be added to this index without changing the academic taxonomy.

## Rights, progress and navigation

Original maintainer-owned content is public and dedicated to the public domain under [CC0 1.0](LICENSE). Accurate citation of factual sources remains an editorial requirement. Linked repositories and third-party works retain their own licenses.

[Level index](levels/README.md) · [Area map](AREA_MAP.md) · [Book guide](guia-geral-cursos-e-livros.md) · [Course skills](SKILLS.md) · [Playbooks](playbooks/README.md) · [AI navigation](AI_GUIDE.md) · [Writing by area](WRITING_PROGRESS.md) · [Writing by course](COURSE_WRITING_PROGRESS.md) · [Progress](STRUCTURE_REVIEW.md) · [Roadmap](ROADMAP.md) · [Sources](SOURCE_AUDIT.md) · [Rights](RIGHTS.md) · [Project categories](CATEGORIES.md)

Construction scripts, tests, measurements and operational records stay in a separate private editorial workspace. All teaching Markdown, including unfinished chapter drafts, belongs in this public repository and is published directly from the maintainer's machine. Separate chapter drafts are temporary and will be consolidated into the course's single principal book.
