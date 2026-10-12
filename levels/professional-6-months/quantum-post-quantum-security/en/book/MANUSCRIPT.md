# Quantum and Post-Quantum Security: A Practitioner's Migration Workflow

- Language: English (`en`); professional course, six months; approximately 360 hours of planned study.
- Editorial state: **draft**. Chapters 1–12 of 12 have authored teaching text; exercises EX001–EX060 (five per chapter) have matching worked results; offline labs use the Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: entry-level practitioners — security analysts, IT risk and compliance staff, project coordinators — who will run a repeatable post-quantum migration workflow and communicate findings to managers, owners and suppliers. Entry knowledge: security basics and the relevant system fundamentals.
- Relation to neighbouring books: the [technical book](../../../../technical-18-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) teaches hands-on configuration and the [postgraduate book](../../../../postgraduate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) organization-scale leadership. **This book is about the management workflow of migration**: scoping, inventory, prioritisation, governance, supplier engagement, tracking, verification and reporting.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. No authority to test real systems. All organizations, people and numbers in examples are **synthetic** unless a sentence cites a public source. Production systems must use vetted implementations of [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) and [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205).

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Twelve chapters follow one workflow over six months: foundations and context (1–3), core methods and tools (4–5), the operational workflow, controls and verification (6–7), a supervised case (8), communication and reporting (9), quality and troubleshooting (10), a supervised laboratory (11) and a portfolio review (12). Each chapter has learning outcomes, teaching, a worked example, a practice task, common errors, five exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs run offline with Python 3; the printed output is shown so you can check your run.

### The running case: Marlow & Tide Insurance

**Marlow & Tide Insurance (MTI)** is a synthetic insurer with 1,800 staff. It sells policies through a broker portal and a quote API, handles claims through a claims application, keeps a life-policy archive that must remain confidential and verifiable for 40 years, exchanges files with reinsurers over SFTP, and runs office VPNs, an internal certificate authority and more than 120 suppliers. You have joined MTI's security team as the coordinator of its post-quantum readiness workflow. Every number about MTI is invented.

### Source policy

Primary sources were checked on 12 October 2026: NIST FIPS 203/204/205 (August 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (initial public draft)](https://doi.org/10.6028/NIST.IR.8547.ipd), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) and [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). FN-DSA (FIPS 206) and the HQC standard were still in development. Re-verify status before relying on it.

## Contents

| Stage | Chapters |
|---|---|
| Foundations and context | [1 Security foundations for practitioners](#ch-01) · [2 Service and stakeholder context](#ch-02) · [3 Authorized practice and evidence handling](#ch-03) |
| Methods and workflow | [4 Core methods](#ch-04) · [5 Tools and interpretation](#ch-05) · [6 Operational workflow](#ch-06) · [7 Controls and verification](#ch-07) · [8 Supervised case analysis](#ch-08) |
| Communication and quality | [9 Communication, ethics and reporting](#ch-09) · [10 Quality and troubleshooting](#ch-10) · [11 Supervised laboratory](#ch-11) · [12 Practice portfolio and final review](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) explain what quantum computers threaten in cryptography and what they do not; (2) name the NIST post-quantum standards and their status; (3) distinguish harvest-now-decrypt-later from forge-later risk; (4) explain hybrid key exchange in plain terms; and (5) avoid common misstatements in reports.

### 1.1 What changes and what does not

Today's systems rely on two kinds of cryptography. *Symmetric* cryptography (such as AES) encrypts data with a shared key and *hash functions* (such as SHA-256) fingerprint data; these remain strong against known quantum attacks at current sizes. *Public-key* cryptography (RSA, elliptic curves) lets systems agree keys and sign data without a prior shared secret; a large error-corrected quantum computer running Shor's algorithm (Shor, 1997) would break it. No such computer exists today and nobody knows when one will; public estimates of the resources needed have fallen over time (for example Gidney, 2025), which is why organizations are planning now.

### 1.2 The replacements

In August 2024 NIST published three standards: [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) (ML-KEM) for agreeing keys, [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) (ML-DSA) and [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (SLH-DSA) for signatures. [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) covers stateful hash-based signatures for specialised uses such as firmware. NIST's [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) is an initial public draft proposing that quantum-vulnerable algorithms be deprecated after 2030 and disallowed after 2035 — proposed dates, not yet final rules. FN-DSA and a standard based on HQC were in development.

### 1.3 Two risks with different clocks

*Harvest now, decrypt later*: an adversary records encrypted traffic today and decrypts it once a quantum computer exists. This matters now for data that must stay confidential for many years — for MTI, life-policy records (40 years) and claims records (10 years). *Forge later*: once a quantum computer exists, an adversary could forge signatures, certificates and software updates. This matters most for things trusted for a long time, such as root certificates, signed archives and devices that cannot be updated.

### 1.4 Hybrid key exchange

During the transition, systems combine a post-quantum method with a traditional one so an attacker would need to break both. This *hybrid* approach (terminology in [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) is now available in common web software as the TLS group X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)). Hybrid key exchange protects the confidentiality of sessions; it does not by itself make certificates or signatures post-quantum.

### 1.5 Worked example

A draft status report says: "Our website is now quantum-proof because we enabled Kyber." Corrected: "The broker portal now uses hybrid post-quantum key exchange (X25519MLKEM768, based on ML-KEM from NIST FIPS 203) for connections from up-to-date browsers. This protects recorded portal traffic against future decryption. The portal's certificate still uses a classical signature; certificate migration is planned separately."

### 1.6 Practice task

Rewrite three sentences from a vendor brochure or news article about quantum security so that they are accurate, sourced and appropriately cautious.

### 1.7 Common errors and limits

- "Quantum-proof" or "unbreakable" claims.
- Treating IR 8547's draft dates as final.
- Saying hybrid key exchange makes the whole system post-quantum.

### Exercises

- **EX001 — Keep or replace.** Classify AES-256, RSA-2048, SHA-256 and ECDSA P-256. Rubric: 3 = four correct with reasons.
- **EX002 — Standards.** Name the three 2024 NIST standards and what each is for. Rubric: 3 = FIPS 203 ML-KEM key establishment; FIPS 204 ML-DSA and FIPS 205 SLH-DSA signatures.
- **EX003 — Two clocks.** Give one MTI example each of HNDL and forge-later risk. Rubric: 3 = correct, explained examples.
- **EX004 — Draft status.** Write one accurate sentence about IR 8547's dates. Rubric: 3 = draft, proposal, years.
- **EX005 — Correct the claim.** Correct: "Hybrid TLS makes our certificates quantum-safe." Rubric: 3 = separates key exchange from authentication.

### Synthesis

Quantum computers threaten public-key key agreement and signatures, not symmetric encryption. NIST's 2024 standards provide replacements; hybrid key exchange addresses harvest-now-decrypt-later now, while signatures follow a planned path.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Quantum and post-quantum security: service and stakeholder context

### Learning outcomes

You will (1) map MTI's services to the data they carry and how long it must stay protected; (2) apply Mosca's rule across several timeline assumptions; (3) identify stakeholders and what each needs; (4) set a first priority list; and (5) explain priorities to non-specialists.

### 2.1 Services and data lifetimes

List each service, the data it handles and how long that data must stay confidential or trustworthy. Use contracts, regulations and retention schedules as sources, and ask data owners when unsure. For MTI: life-policy archive 40 years; claims records 10 years; broker portal sessions carry personal data relevant for about 7 years; quote requests are short-lived.

### 2.2 Mosca's rule

Mosca (2018): if data must stay secure for *x* years, migration takes *y* years, and a capable quantum computer may arrive in *z* years, then data is already at risk when *x* + *y* > *z*. Since nobody knows *z*, try several values.

### 2.3 Practical activity — Lab M

```python
# Lab M (ch 2): Mosca's inequality x + y > z for synthetic Marlow & Tide Insurance data, sweeping z.
assets = [  # (name, shelf-life x in years, migration time y in years) - synthetic
    ("life-policy archive", 40, 4), ("claims records", 10, 3), ("quote requests", 0.1, 1), ("broker portal traffic", 7, 2)]
for z in (10, 15, 20):  # years until a cryptographically relevant quantum computer: an assumption, not a forecast
    late = [n for n, x, y in assets if x + y > z]
    print(f"z={z:>2}: at risk now -> {', '.join(late) if late else 'none'}")
```

Expected output:

```text
z=10: at risk now -> life-policy archive, claims records
z=15: at risk now -> life-policy archive
z=20: at risk now -> life-policy archive
```

The life-policy archive is at risk under every assumption; claims records only if *z* is ten years. That pattern is the basis of a priority list that does not depend on predicting the future.

### 2.4 Stakeholders

Data owners (underwriting, claims) set lifetimes; system owners (IT teams) make changes; suppliers control products; procurement writes contracts; legal and compliance track obligations; executives approve budgets and accept risk; auditors check evidence. List what each needs from the workflow and what you need from them.

### 2.5 Worked example

MTI's first priority list: 1) transfers of life-policy records between offices and the archive; 2) reinsurer SFTP exchanges carrying claims data; 3) broker portal; 4) internal CA planning (forge-later, long validity). Quote requests are deprioritised. The list is explained to the executive sponsor as "protect what must stay secret longest, first".

### 2.6 Practice task

Build a five-row table of MTI services with data, lifetime, source of lifetime and owner; run Lab M with your own values.

### 2.7 Common errors and limits

- Lifetimes guessed instead of sourced.
- A single assumed quantum date.
- Forgetting procurement and legal as stakeholders.
### 2.8 Revisiting the list

Priorities change when facts change: a new contract extends a retention period, a supplier ships hybrid support, a service is retired. Review the priority list each quarter with data owners and system owners, record what changed and why, and keep the old versions. Auditors and executives trust a list that visibly evolves with evidence more than one that never changes.

### Exercises

- **EX006 — Mosca.** For claims records (*x* = 10, *y* = 3), state the timelines under which they are at risk. Rubric: 3 = *z* < 13.
- **EX007 — Lifetime source.** Name two sources for data lifetimes at an insurer. Rubric: 3 = contracts/regulation/retention schedule with owner confirmation.
- **EX008 — Stakeholder map.** List five stakeholders and one need each. Rubric: 3 = five relevant pairs.
- **EX009 — Priority.** Why is the life-policy archive first? Rubric: 3 = at risk under all assumptions; longest lifetime.
- **EX010 — Plain explanation.** Explain the priority list to an executive in three sentences. Rubric: 3 = clear, accurate, decision-oriented.

### Synthesis

Service maps with sourced lifetimes, Mosca's rule across several assumptions and a stakeholder map produce a priority list that is robust and explainable.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) obtain and respect written authorization; (2) collect only necessary evidence; (3) store and label evidence properly; (4) handle sensitive findings; and (5) work with suppliers' confidential information.

### 3.1 Authorization

Even "harmless" activities — reading configurations, running an inventory tool, asking for logs — need written authorization from the system owner stating systems, methods, time window, data handling and contacts. Active tests that alter negotiation are done only in isolated labs by technical staff.

### 3.2 Minimum necessary evidence

Collect what answers the question: algorithm names, versions, certificate details, dates. Do not collect message contents or customer data. Prefer configuration exports and summaries over raw captures.

### 3.3 Storage and labelling

Store evidence in the agreed repository with labels: source, date, collector, system, classification. Restrict access; inventories of weaknesses are sensitive. Keep a log of who accessed what.

### 3.4 Sensitive findings

If you find something serious — an exposed private key, an unpatched system with a known vulnerability — report it immediately through the security process; do not investigate further on your own.

### 3.5 Supplier information

Suppliers may share roadmaps under confidentiality. Record them as supplier statements, respect the agreement, and do not forward them outside the people who need them.

### 3.6 Worked example

MTI's coordinator requests configuration exports for the insurer SFTP servers. The authorization (ticket SEC-118) covers read-only export, 1–15 October, results stored in the security evidence repository, contact the infrastructure lead. The export shows OpenSSH version and key-exchange settings; no file contents are touched. A supplier's roadmap received under NDA is stored with restricted access and labelled "supplier statement, confidential".

### 3.7 Practice task

Write an authorization request and an evidence label for one inventory activity.

### 3.8 Common errors and limits

- Collecting more data than needed.
- Evidence without labels.
- Sharing supplier roadmaps widely.
### 3.9 Retention and deletion

Evidence has its own lifetime. Agree how long inventory exports, questionnaires and logs are kept — typically for the duration of the programme plus an audit period — and delete them securely afterwards, keeping only aggregate results and decision records. Record deletions in the evidence log. Keeping raw exports forever increases the damage if the repository is ever compromised, because a complete map of an organization's cryptographic weaknesses is valuable to attackers.

When staff leave the workflow, remove their access to the evidence repository promptly and review what they could see; access reviews are part of evidence handling, not an afterthought.

### Exercises

- **EX011 — Authorization elements.** List five elements of a written authorization. Rubric: 3 = systems, methods, window, data handling, contacts.
- **EX012 — Minimum evidence.** For an SFTP inventory, list three things to collect and two not to. Rubric: 3 = justified lists.
- **EX013 — Label.** Write an evidence label for the SFTP export. Rubric: 3 = source, date, collector, system, classification.
- **EX014 — Serious finding.** What do you do when you find a private key in an export? Rubric: 3 = stop, report, don't use, document.
- **EX015 — NDA roadmap.** How do you record and share a supplier roadmap under NDA? Rubric: 3 = supplier statement label, restricted access, need-to-know.

### Synthesis

Authorized, minimal, well-labelled evidence handling protects the organization, its customers and its suppliers, and keeps the workflow trustworthy.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Quantum and post-quantum security: core methods

### Learning outcomes

You will (1) run an inventory using several sources; (2) build and read a cryptographic bill of materials (CBOM); (3) grade evidence; (4) classify exposure; and (5) track unknowns as work.

### 4.1 Inventory sources

Configuration exports, certificate lists from the CA, network observations by technical teams, application documentation, and supplier questionnaires. Each answers different questions; combine them.

### 4.2 Practical activity — Lab I

```python
# Lab I (ch 4): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("broker-portal", "key-exchange", "X25519MLKEM768", "passive"), ("broker-portal", "signature", "RSA-2048", "config"),
    ("claims-app", "key-exchange", "ECDHE-P256", "passive"), ("claims-app", "signature", "ECDSA-P256", "code"),
    ("policy-db", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("call-recorder", "unknown", "unknown", "none"), ("office-vpn", "key-exchange", "ECDHE-P384", "config")]
VULN = {"RSA-2048", "ECDHE-P256", "ECDSA-P256", "RSA-kex", "ECDHE-P384"}
assets = {r[0] for r in records}
unknown = {r[0] for r in records if r[2] == "unknown"}
vuln = [r for r in records if r[2] in VULN]
print(f"assets {len(assets)}, unknown {len(unknown)} ({100*len(unknown)/len(assets):.0f}%)")
print(f"quantum-vulnerable uses {len(vuln)}:", ", ".join(f"{a}/{f}" for a, f, _, _ in vuln))
print("hybrid key exchange present on:", [r[0] for r in records if "MLKEM" in r[2]])
```

Expected output:

```text
assets 6, unknown 1 (17%)
quantum-vulnerable uses 5: broker-portal/signature, claims-app/key-exchange, claims-app/signature, policy-db/key-exchange, office-vpn/key-exchange
hybrid key exchange present on: ['broker-portal']
```

### 4.3 Evidence grades

A simple grade: A observed in operation; B authoritative configuration; C inferred from documentation or code; D supplier claim; U unknown. Priorities based on D or U evidence need verification before money is spent.

### 4.4 Exposure classes

Record-now (HNDL): classical key exchange carrying long-lived data. Forge-later: classical signatures trusted for long periods or hard to replace. Adequate: symmetric encryption and hashes at good sizes. Unknown.

### 4.5 Unknowns as work

Every unknown becomes a task with owner and due date: ask the supplier, request a configuration export, ask technical staff to observe. Track the unknown share as a headline measure.

### 4.6 Worked example

MTI's first CBOM extract matches Lab I: six assets, five quantum-vulnerable uses, one unknown (the call recorder). Grades: broker portal A (observed), claims app B, policy DB B, call recorder U, office VPN B. Tasks: supplier questionnaire to the call-recorder vendor; confirm claims-app signing algorithm with its owner.

### 4.7 Practice task

Grade and classify each Lab I record and write tasks for the unknowns.

### 4.8 Common errors and limits

- One source only.
- Treating supplier claims as observations.
- Unknowns without owners.
### 4.9 Running the inventory as a cycle

An inventory is not done once. Run it as a cycle: collect (exports, questionnaires, observations), merge into the CBOM, grade, classify, raise tasks for unknowns and gaps, then repeat each quarter. Each cycle should show three numbers to management: how many tier-1 assets have A or B evidence, how many are unknown, and how many are already protected. When a supplier answers a questionnaire, the grade for their products moves from U to D; when a technical team confirms the answer by observation, it moves to A. This movement is real progress even before any algorithm changes, because it turns guesses into facts on which budgets can be based.

Keep the CBOM's access restricted to those who need it and share only summaries more widely.

### Exercises

- **EX016 — Lab I reading.** Which asset already has hybrid key exchange, and what remains classical on it? Rubric: 3 = broker-portal; its signature (RSA-2048).
- **EX017 — Grades.** Assign grades to: observed handshake; supplier email; CA database record; architecture diagram. Rubric: 3 = A, D, B, C.
- **EX018 — Classes.** Classify the five vulnerable uses in Lab I by exposure class. Rubric: 3 = key exchanges HNDL; signatures forge-later.
- **EX019 — Unknown share.** What is Lab I's unknown share, and how would you report it? Rubric: 3 = 17 % of assets, shown beside every figure.
- **EX020 — Task.** Write the task for the call recorder. Rubric: 3 = question, method, owner, due date.

### Synthesis

A multi-source, graded CBOM classifies exposure and turns unknowns into tracked work.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Quantum and post-quantum security: tools and interpretation

### Learning outcomes

You will (1) read the output of configuration audits and inventory tools; (2) distinguish "offered" from "negotiated"; (3) recognise tool blind spots; (4) interpret supplier questionnaire answers; and (5) turn tool output into findings.

### 5.1 What tools show

Configuration audits show what a service offers and in which order. Log summaries from technical teams show what was negotiated. Certificate inventories show signature algorithms and expiry dates. Supplier questionnaires show claims. As a practitioner you will rarely run active tools yourself; you will read and interpret their output.

### 5.2 Practical activity — Lab T

```python
# Lab T (ch 5): audit synthetic TLS server configurations for post-quantum key exchange and preference order.
configs = {  # service: ordered list of offered groups (server preference) - synthetic
    "quote-api": ["X25519MLKEM768", "X25519", "secp256r1"],
    "claims-portal": ["X25519", "X25519MLKEM768", "secp256r1"],
    "insurer-sftp": ["ecdh-sha2-nistp256"],
    "hr-intranet": ["X25519", "secp384r1"]}
HYBRID = {"X25519MLKEM768", "SecP256r1MLKEM768", "SecP384r1MLKEM1024"}
for svc, groups in configs.items():
    offered = [g for g in groups if g in HYBRID]
    if not offered: verdict = "CLASSICAL ONLY"
    elif groups[0] in HYBRID: verdict = "OK (hybrid preferred)"
    else: verdict = "WARN hybrid offered but not preferred"
    print(f"{svc:17s} {verdict}")
```

Expected output:

```text
quote-api         OK (hybrid preferred)
claims-portal     WARN hybrid offered but not preferred
insurer-sftp      CLASSICAL ONLY
hr-intranet       CLASSICAL ONLY
```

The claims portal "offers but does not prefer" hybrid: a configuration audit that only checked presence would report it as done, but most connections will still use classical key exchange. Always ask whether a tool checks preference and actual negotiation.

### 5.3 Blind spots

A passive sensor in TLS 1.3 sees the negotiated group but not the certificate, which is encrypted. An active scanner with an old library reports everything as classical. A configuration export may be stale. A questionnaire may describe a product version MTI does not run. Write the blind spot next to each result.

### 5.4 Interpreting questionnaires

Good answers name algorithms and parameter sets (ML-KEM-768 per FIPS 203), protocols (TLS 1.3 hybrid group per RFC 10024; IKEv2 per RFC 9370), product versions and dates, and offer test access. Weak answers say "PQC-ready" or "roadmap under review". Score answers consistently, for example 0 = no answer, 1 = undated claim, 2 = dated roadmap naming algorithms and protocols, 3 = shipped and verifiable.

### 5.5 From output to finding

A finding states observation, source, date, impact, recommendation and owner. "Claims portal: hybrid group offered but X25519 preferred (configuration audit, 6 October). Impact: claims sessions remain HNDL-exposed. Recommendation: reorder groups to prefer X25519MLKEM768; verify with logs. Owner: Web Platform."

### 5.6 Worked example

The audit flags insurer-sftp as classical-only. The infrastructure team confirms the OpenSSH version predates hybrid support. Finding raised: upgrade and enable `mlkem768x25519-sha256`; coordinate with reinsurers whose clients may be old; owner Infrastructure; due in one quarter.

### 5.7 Practice task

Turn each Lab T line into a finding or an "as expected" note.

### 5.8 Asking the right follow-up

When tool output surprises you, ask technical staff three questions before raising a finding: is the tool current enough to see post-quantum algorithms; is the data fresh; and does the result match another source? Many apparent findings disappear — or become more serious — after these checks.

### 5.9 Common errors and limits

- Presence counted as success.
- Ignoring blind spots.
- Scoring questionnaire answers inconsistently.

### Exercises

- **EX021 — Offered vs negotiated.** Explain the difference using the claims portal. Rubric: 3 = order/preference causes classical negotiation.
- **EX022 — Blind spot.** What can't a passive TLS 1.3 sensor see, and where do you get it instead? Rubric: 3 = certificate; config/certificate inventory.
- **EX023 — Score answers.** Score: "PQC-ready"; "ML-KEM-768 hybrid in TLS 1.3 from v8.2, shipped"; "roadmap 2027 for RFC 9370". Rubric: 3 = 1, 3 (if verifiable) and 2.
- **EX024 — Finding.** Write the finding for hr-intranet. Rubric: 3 = observation, source, date, impact, recommendation, owner.
- **EX025 — Follow-up.** List the three questions to ask before raising a surprising finding. Rubric: 3 = tool currency, freshness, corroboration.

### Synthesis

Practitioners interpret tool and questionnaire output with attention to preference, negotiation and blind spots, and turn it into precise findings.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Quantum and post-quantum security: operational workflow

### Learning outcomes

You will (1) run the migration workflow as a repeatable cycle; (2) define roles, inputs and outputs for each step; (3) use a tracker with clear states; (4) manage dependencies on suppliers and partners; and (5) report progress with outcome measures.

### 6.1 The cycle

1. **Scope** services and confirm authorization. 2. **Inventory** with graded evidence. 3. **Prioritise** by lifetime, exposure and change route. 4. **Plan** each item: control, owner, date, dependencies. 5. **Implement** through the owning team's change process. 6. **Verify** with negotiation evidence. 7. **Record** residual risk and exceptions. 8. **Report** and repeat each quarter.

### 6.2 Roles

Coordinator (you): runs the cycle, keeps the tracker, writes reports. System owners: implement changes. Data owners: confirm lifetimes. Procurement: supplier clauses. Security architecture: standards. Executive sponsor: decisions and risk acceptance. Internal audit: independent checks.

### 6.3 Tracker states

Use simple states: *Unknown* → *Assessed* → *Planned* → *In progress* → *Implemented* → *Verified* → *Closed* (or *Exception*). An item moves to Verified only with evidence of negotiation, not just a change ticket.

### 6.4 Dependencies

Many items wait on suppliers or partners. Record the dependency, the request sent, the answer and the follow-up date. Escalate unanswered requests through procurement or account management.

### 6.5 Outcome measures

Report: share of tier-1 items Verified; share Unknown; number of open exceptions and how many are past expiry; supplier answers received. Avoid activity counts such as "meetings held".

### 6.6 Worked example

MTI's tracker after one quarter (synthetic): 64 tier-1 items — 6 Verified, 9 Implemented, 14 In progress, 18 Planned, 11 Assessed, 6 Unknown; 3 exceptions. Report headline: "9 % of tier-1 items verified, 9 % unknown; reinsurer SFTP and archive transfers in progress; 3 exceptions, none past expiry."

### 6.7 Practice task

Set up a tracker for ten MTI items and move three through the states with evidence.

### 6.8 Cadence

A monthly working meeting with system owners keeps items moving; a quarterly report goes to the sponsor; an annual review revisits the standard, priorities and lifetimes. Keep each meeting short and driven by the tracker: blocked items first, then items due, then new unknowns.

### 6.9 Common errors and limits

- Marking items done on a change ticket alone.
- Dependencies without follow-up dates.
- Activity metrics in reports.

### Exercises

- **EX026 — Order the cycle.** Put the eight steps in order and give one output for each. Rubric: 3 = correct order with outputs.
- **EX027 — Verified.** What evidence moves an item from Implemented to Verified? Rubric: 3 = negotiation logs/tool output, dated.
- **EX028 — Headline.** Compute the Verified and Unknown shares in 6.6. Rubric: 3 = 6/64 ≈ 9 %, 6/64 ≈ 9 %.
- **EX029 — Dependency record.** List the fields for a supplier dependency. Rubric: 3 = request, date, answer, grade, follow-up, escalation.
- **EX030 — Meeting agenda.** Draft a 30-minute monthly agenda. Rubric: 3 = blocked, due, unknowns, decisions.

### Synthesis

A repeatable cycle with clear roles, tracker states, managed dependencies and outcome measures turns migration into routine, reportable work.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Quantum and post-quantum security: controls and verification

### Learning outcomes

You will (1) describe the main controls available for quantum risk; (2) match controls to exposure; (3) understand crypto-agility as a governance goal; (4) define what counts as verification; and (5) record residual risk.

### 7.1 Controls

*Hybrid key exchange* (X25519MLKEM768 in TLS; ML-KEM in IKEv2 via RFC 9370; `mlkem768x25519-sha256` in SSH). *Interim pre-shared keys* mixed into VPNs (RFC 8784) for fixed links. *Data minimization*: send and keep less long-lived data. *Signature migration planning*: post-quantum internal CA, code-signing plans, archive timestamp renewal. *Procurement clauses*: algorithm support, inventories, update commitments. *Exception management*: time-limited acceptance with compensating controls.

### 7.2 Matching controls

HNDL exposure → hybrid key exchange and minimization first. Forge-later exposure → signature plans, procurement and archive renewal. Unknown → investigation. Supplier-controlled → contract clauses and roadmap tracking.

### 7.3 Practical activity — Lab A

```python
# Lab A (ch 7): crypto-agility through a policy-driven registry instead of hard-coded algorithms.
import hashlib, hmac
REGISTRY = {"hmac-sha256": lambda k, m: hmac.new(k, m, hashlib.sha256).digest(),
            "hmac-sha3-256": lambda k, m: hmac.new(k, m, hashlib.sha3_256).digest()}
POLICY = {"tag-algorithm": "hmac-sha256", "accept": ["hmac-sha256", "hmac-sha3-256"]}
def protect(key, msg):
    alg = POLICY["tag-algorithm"]; return alg, REGISTRY[alg](key, msg)
def check(key, msg, alg, tag):
    if alg not in POLICY["accept"]: return False            # algorithm identifier is authenticated by policy
    return hmac.compare_digest(REGISTRY[alg](key, msg), tag)
k, m = b"k" * 32, b"policy schedule 42"
a1, t1 = protect(k, m)
POLICY["tag-algorithm"] = "hmac-sha3-256"                   # migration = one policy change
a2, t2 = protect(k, m)
print("old tag still verifies during transition:", check(k, m, a1, t1))
print("new tag verifies:", check(k, m, a2, t2), "| algorithms:", a1, "->", a2)
POLICY["accept"] = ["hmac-sha3-256"]                        # retire the old algorithm
print("old tag after retirement:", check(k, m, a1, t1))
```

Expected output:

```text
old tag still verifies during transition: True
new tag verifies: True | algorithms: hmac-sha256 -> hmac-sha3-256
old tag after retirement: False
```

When algorithms are chosen by policy and labelled in the data, migration is a configuration change, and an old algorithm can be retired cleanly. Ask system owners and suppliers whether their products work this way; NIST's [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) discusses such crypto-agility considerations.

### 7.4 Verification

Verification means evidence that the control works in operation: negotiation logs showing hybrid on the intended service, certificate inventory showing new algorithms, questionnaire answers confirmed by observation, minimization confirmed by data-flow review. A change ticket is evidence of intent, not of effect.

### 7.5 Residual risk

For each verified item, record what remains: usually classical authentication, partners on old clients, or devices awaiting replacement. Give each residual risk an owner and review date.

### 7.6 Worked example

Reinsurer SFTP: control — hybrid SSH key exchange after OpenSSH upgrade; verification — sshd logs show 7 of 10 reinsurers negotiating the hybrid; residual — three reinsurers on old clients (notified, deadline in 12 months), host keys classical; owner Infrastructure; review quarterly.

### 7.7 Practice task

For three MTI items, write control, verification evidence and residual risk.

### 7.8 Exceptions

When a control cannot be applied in time, raise an exception: scope, reason, compensating controls, owner, expiry. The sponsor approves; the tracker shows it; expiry triggers review. Exceptions are normal; exceptions without expiry are not.

### 7.9 Common errors and limits

- Change tickets accepted as verification.
- Residual risk omitted.
- Exceptions without expiry.

### Exercises

- **EX031 — Match.** Match controls to: archive transfers (HNDL), internal CA (forge-later), call recorder (unknown), CDN (supplier). Rubric: 3 = four sensible matches.
- **EX032 — Verification evidence.** For the broker portal, what verifies hybrid key exchange? Rubric: 3 = negotiation logs/tool output, dated.
- **EX033 — Agility.** Using Lab A, explain why retirement is a one-line policy change. Rubric: 3 = accept list, identifier in data.
- **EX034 — Residual.** Write the residual-risk note for reinsurer SFTP. Rubric: 3 = remaining risks, owner, review, deadline.
- **EX035 — Exception.** Draft an exception for the call recorder pending vendor answer. Rubric: 3 = scope, reason, compensating controls, owner, expiry.

### Synthesis

Controls are matched to exposure, verified by operational evidence, and accompanied by recorded residual risk and time-limited exceptions; agility makes future change cheaper.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Quantum and post-quantum security: supervised case analysis

### Learning outcomes

You will (1) analyse a realistic migration case end to end; (2) apply the workflow under supervision; (3) weigh options with explicit criteria; (4) identify governance gaps; and (5) present a recommendation.

### 8.1 The case

MTI's life-policy archive (synthetic): 40-year confidentiality and verifiability; documents signed with RSA-2048; transferred nightly from regional offices over IPsec VPNs with ECDH; stored encrypted with AES-256, keys wrapped by an HSM using RSA-OAEP; VPN appliances from a supplier whose firmware supports RFC 9370 from version 7.4, with MTI on 7.1; archive software vendor states "PQC signatures on roadmap".

### 8.2 Analysis

Exposure: transfers are HNDL-exposed now (40-year data). Signatures are forge-later exposed (documents must stay verifiable for decades). AES-256 at rest is adequate; RSA key wrapping matters if wrapped keys ever leave the HSM or are backed up off-site.

### 8.3 Options

(A) Upgrade VPN firmware to 7.4 and enable hybrid key exchange; (B) interim RFC 8784 PSKs on the archive tunnels until A; (C) reduce transfers by sending documents once at completion instead of nightly re-sync; (D) archive signature plan: require vendor dates for ML-DSA support and plan timestamp renewal. Criteria: protection, time, cost, operational risk, dependency.

### 8.4 Governance gaps

No owner for archive cryptography; no contract clause requiring the archive vendor to support post-quantum signatures; no exception process used for the VPN delay.

### 8.5 Recommendation

A within two quarters, with C immediately and B for the two offices whose appliances cannot be upgraded until hardware refresh; D as a procurement action with a deadline; name Records Management as owner of archive cryptography; register an exception for the two offices with expiry at refresh.

### 8.6 Worked example of presentation

"Recommendation: protect archive transfers within six months by upgrading VPN firmware and enabling hybrid post-quantum key exchange, reduce nightly transfers now, and use interim pre-shared keys at two offices. Cost: CU 40–70k (synthetic). Residual: classical document signatures until the archive vendor delivers ML-DSA; we request a contract amendment with dates."

### 8.7 Practice task

Analyse the case yourself, score options against criteria, and compare with the recommendation above.

### 8.8 Supervisor review

Present your analysis to your supervisor before sharing it: they will check whether the facts are graded correctly, whether options were considered fairly and whether the recommendation stays within what the evidence supports. Incorporate comments and record what changed.

### 8.9 Common errors and limits

- Ignoring signatures because key exchange is urgent.
- Options without criteria.
- Missing governance gaps.

### Exercises

- **EX036 — Exposure.** List the case's exposures by class. Rubric: 3 = transfers HNDL, signatures forge-later, AES adequate, key wrapping conditional.
- **EX037 — Option scoring.** Score options A–C on protection and time (1–5). Rubric: 3 = defensible scores with reasons.
- **EX038 — Gap.** Propose fixes for the three governance gaps. Rubric: 3 = owner, clause, exception.
- **EX039 — Recommendation.** Rewrite the recommendation for a non-technical board in 60 words. Rubric: 3 = clear, accurate, costs and residual.
- **EX040 — Key wrapping.** When does RSA-OAEP key wrapping become a quantum concern? Rubric: 3 = when wrapped keys are exposed outside the HSM/recorded.

### Synthesis

Supervised case analysis applies the workflow end to end: exposures, options with criteria, governance gaps and a clear, costed recommendation with residual risk.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) write reports for executives, owners, suppliers and auditors; (2) communicate uncertainty honestly; (3) avoid fear-based or overconfident messaging; (4) handle sensitive information ethically; and (5) present findings orally.

### 9.1 Audiences

Executives need decisions, risk posture, costs and residual risk on one page. System owners need specific findings with evidence and deadlines. Suppliers need clear requirements and dates. Auditors need evidence and method. Staff need to know what changes for them.

### 9.2 Uncertainty

Say what is known (standards published, algorithms in use), what is estimated (migration durations), and what is unknown (when a capable quantum computer will exist). Use ranges and show that recommendations hold across them. Avoid single-date predictions.

### 9.3 Tone

Fear-based messages ("quantum apocalypse") produce either panic or dismissal. Overconfident messages ("we are quantum-safe") collapse at the first audit. Calm, specific messages work: "we are protecting the data that must stay private longest first; here is progress and what remains."

### 9.4 Ethics

Reports about weaknesses are sensitive; share them on a need-to-know basis. Do not exaggerate risk to win budget or understate it to avoid work. Credit teams' work accurately. Label synthetic examples in training materials. Report problems you discover, including your own mistakes.

### 9.5 Oral presentation

Lead with the question and answer, show evidence, end with decisions needed. Keep slides simple; prepare for questions about assumptions and status of guidance.

### 9.6 Worked example

Quarterly executive summary (synthetic): "Position: 9 % of tier-1 items verified, 9 % still unknown (down from 31 %). Highlights: reinsurer SFTP now uses hybrid post-quantum key exchange for 7 of 10 partners. Risks: archive vendor has no dated plan for post-quantum signatures. Decisions needed: approve contract amendment request; approve two exceptions for offices awaiting hardware refresh. Outlook: archive transfers protected by Q2 if firmware upgrades proceed."

### 9.7 Practice task

Write the same quarter's message for system owners and for a supplier.

### 9.8 Handling pushback

Owners may object to deadlines; executives may question cost. Respond with evidence: the lifetime of the data, the robustness of the priority list across timelines, the cost range and the residual risk of waiting. Offer options rather than ultimatums, and record the decision and who made it.

### 9.9 Common errors and limits

- One report for all audiences.
- False precision about timelines.
- Sharing weakness details widely.

### Exercises

- **EX041 — Audience.** List what executives and auditors each need. Rubric: 3 = decisions/posture vs evidence/method.
- **EX042 — Uncertainty sentence.** Write one sentence stating quantum timeline uncertainty accurately. Rubric: 3 = no date, range/assumption, robust recommendation.
- **EX043 — Tone fix.** Rewrite: "Hackers with quantum computers will steal everything soon!" Rubric: 3 = calm, specific, accurate.
- **EX044 — Supplier message.** Write a five-sentence requirement message to the archive vendor. Rubric: 3 = requirement, standard, date, test, contact.
- **EX045 — Pushback.** How do you respond to an owner who says "quantum is decades away"? Rubric: 3 = HNDL, lifetime, robustness, options.

### Synthesis

Good communication fits the audience, states uncertainty honestly, keeps a calm tone, handles sensitive information ethically and leads to recorded decisions.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Quantum and post-quantum security: quality and troubleshooting

### Learning outcomes

You will (1) check the quality of the inventory and tracker; (2) detect common workflow failures; (3) interpret rollout gate decisions; (4) coordinate troubleshooting with technical teams; and (5) improve the workflow from lessons learned.

### 10.1 Data quality

Check regularly: stale evidence (older than the agreed age), items without owners, unknowns without tasks, items marked Verified without evidence, exceptions past expiry. Sample ten items each month and check their evidence yourself.

### 10.2 Workflow failures

*Silent fallback*: an item verified last quarter has reverted to classical after an update. *Stuck items*: dependencies with no follow-up. *Scope creep*: the workflow absorbs unrelated work. *Report drift*: definitions change between quarters without notice.

### 10.3 Practical activity — Lab K

```python
# Lab K (ch 10): canary gate for enabling a hybrid group - promote only if failures stay within budget.
import math
def upper95(k, n):                      # Wilson upper bound
    z = 1.96; p = k / n; d = 1 + z*z/n
    return ((p + z*z/(2*n)) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
baseline, budget = 5e-4, 4e-4            # baseline failure rate, allowed increase
for stage, k, n in [("1% canary", 3, 5000), ("10% canary", 28, 50000), ("10% canary (proxy site)", 96, 50000)]:
    ub = upper95(k, n); ok = ub <= baseline + budget
    print(f"{stage:24s} {k}/{n}  upper95={ub:.5f}  {'PROMOTE' if ok else 'HOLD'}")
```

Expected output:

```text
1% canary                3/5000  upper95=0.00176  HOLD
10% canary               28/50000  upper95=0.00081  PROMOTE
10% canary (proxy site)  96/50000  upper95=0.00234  HOLD
```

Technical teams roll out changes in stages and promote only when failure rates stay within budget with confidence. As coordinator, read gate results so you can report status accurately: "held for more data" and "held because of a fault" mean different things for the timeline.

### 10.4 Coordinating troubleshooting

When a rollout causes problems, your role is coordination: make sure the right owners are engaged, the impact is understood, communication goes out, the tracker shows the item as blocked with a reason, and lessons are captured. Leave technical diagnosis to technical staff.

### 10.5 Lessons learned

After each quarter and each significant incident, hold a short review: what went well, what didn't, what to change in the workflow. Record changes to definitions and procedures.

### 10.6 Worked example

A monthly sample finds that the broker portal, marked Verified in Q1, shows 4 % hybrid in Q2 logs. Cause: a platform update restored a default profile. Actions: item moved back to In progress; owner restores profile; a quality rule is added — every Verified item is re-checked automatically each month. Lessons recorded.

### 10.7 Practice task

Design a monthly quality checklist of eight checks for MTI's tracker.

### 10.8 Measuring quality

Report a quality measure alongside progress: for example, the share of sampled items whose evidence matched their tracker state. A falling quality score is an early warning that progress figures may be overstated.

### 10.9 Common errors and limits

- Trusting Verified forever.
- Coordinators doing technical diagnosis.
- Definitions changed silently.

### Exercises

- **EX046 — Quality checks.** List five data-quality checks. Rubric: 3 = stale, ownerless, untasked unknowns, unevidenced Verified, expired exceptions.
- **EX047 — Gate reading.** Report Lab K's three results in plain language for the sponsor. Rubric: 3 = wait for data; proceed; fault at one site under investigation.
- **EX048 — Regression.** What tracker change and rule follow the broker-portal regression? Rubric: 3 = back to In progress; monthly re-check.
- **EX049 — Coordination.** List four coordinator actions during a rollout problem. Rubric: 3 = owners, impact, communication, tracker.
- **EX050 — Quality measure.** Define a quality measure and its calculation. Rubric: 3 = matched/sampled share.

### Synthesis

Quality checks, accurate reading of gate decisions, coordinated troubleshooting and lessons learned keep the workflow's numbers honest.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) run a full workflow cycle on a synthetic dataset; (2) produce tracker, findings and report; (3) work with simulated owners and suppliers; (4) handle a simulated incident; and (5) reflect on performance.

### 11.1 Setup

The lab uses a synthetic MTI dataset: 40 assets with configuration exports, a few log summaries, supplier questionnaire answers and data-lifetime records. Your supervisor and peers play owners, suppliers and the sponsor. No real systems or data are involved.

### 11.2 Tasks

Day 1: scope, authorization (simulated), inventory and grading. Day 2: prioritisation with Mosca's rule and exposure classes. Day 3: plan items, send supplier requests, raise findings. Day 4: a simulated rollout with gate results and one incident (silent fallback). Day 5: quarterly report and presentation.

### 11.3 The incident

Mid-lab, the "platform owner" reports that the quote API's hybrid share dropped after an update. You coordinate: tracker update, owner engagement, communication to stakeholders, lessons.

### 11.4 Assessment

Supervisors assess accuracy of the inventory and priorities, quality of findings and evidence handling, tracker integrity, communication, and handling of the incident.

### 11.5 Worked example

A participant's Day 2 output: 9 tier-1 assets; priority list headed by archive transfers and reinsurer SFTP; 6 unknowns with tasks; Mosca table across *z* = 10, 15, 20. Supervisor feedback: one supplier claim graded as B should be D; corrected and the priority of that asset reduced pending verification.

### 11.6 Practice task

Complete the five-day lab and keep a short daily log.

### 11.7 Reflection

At the end, write a one-page reflection: what you did well, what you would change, which skill needs more practice, and one improvement to the workflow itself. Share it with your supervisor.

### 11.8 Working with simulated stakeholders

Treat role-players as real: send clear, polite requests with deadlines; record answers; escalate when deadlines pass. The lab assesses whether you can keep a workflow moving through other people, which is the core of the practitioner's job.

### 11.9 Common errors and limits

- Treating the lab as a spreadsheet exercise.
- Missing the incident's communication step.
- Skipping the reflection.

### Exercises

- **EX051 — Day plan.** Write the deliverables for each lab day. Rubric: 3 = five days with outputs.
- **EX052 — Grading correction.** Why does regrading a claim from B to D change priority actions? Rubric: 3 = needs verification before spend.
- **EX053 — Incident note.** Write the stakeholder note for the quote-API incident. Rubric: 3 = what, impact, action, next update.
- **EX054 — Assessment criteria.** List five criteria supervisors use. Rubric: 3 = accuracy, findings, evidence, tracker, communication/incident.
- **EX055 — Reflection.** Write a five-sentence reflection template. Rubric: 3 = strengths, changes, skill gap, workflow improvement, next step.

### Synthesis

The supervised lab runs a complete cycle with simulated people and an incident, building confidence in the workflow before real use.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a portfolio showing each course outcome; (2) present your workflow and results; (3) answer questions on method, evidence and status of guidance; (4) plan next steps in practice; and (5) keep your knowledge current.

### 12.1 Portfolio contents

Include: an accurate explainer (Chapter 1); a service and stakeholder map with priorities (2); authorization and evidence labels (3); a graded CBOM extract (4); findings from tool output (5); a tracker with states and dependencies (6); control, verification and residual-risk records (7); the case analysis (8); reports for two audiences (9); a quality checklist and lessons (10); the lab outputs and reflection (11).

### 12.2 Presentation

Ten minutes: the workflow, what you produced, one decision you supported, one lesson. Then questions.

### 12.3 Likely questions

"How do you know an item is verified?" "Why is the archive first?" "Is IR 8547 final?" "What does hybrid key exchange not protect?" "What would you do if a supplier never answers?" Answer with evidence from your portfolio.

### 12.4 Next steps

Agree with your manager which workflow responsibilities you will take on, which skills to deepen (for example, the technical course for hands-on configuration), and when you will review progress.

### 12.5 Staying current

Track NIST and IETF publications, sector guidance and supplier announcements. Update your explainer and the workflow's standards section when status changes — for example when FN-DSA or the HQC standard is published, or IR 8547 is finalised.

### 12.6 Worked example

A participant presents MTI's Q2 position, the archive case recommendation and the broker-portal regression lesson. Asked "What does hybrid not protect?", they answer: "Authentication — the portal certificate is still classical — plus any hop or partner still on classical key exchange, and data recorded before the change." Asked about IR 8547, they state it is a draft with proposed dates and show how MTI's internal dates were set.

### 12.7 Practice task

Assemble your portfolio and rehearse the presentation with a peer.

### 12.8 Professional habits

The habits this course builds — sourcing every claim, grading evidence, recording decisions, stating residual risk, communicating calmly — apply to any security programme. Practise them deliberately in your next role; they are what make a practitioner trusted to coordinate work across teams.

### 12.9 Common errors and limits

- Portfolios of documents without evidence of outcomes.
- Overclaiming in answers.
- No plan for staying current.

### Exercises

- **EX056 — Portfolio map.** Map five course outcomes to portfolio items. Rubric: 3 = specific artefacts.
- **EX057 — Answer.** Answer "How do you know an item is verified?" Rubric: 3 = operational evidence, date, source.
- **EX058 — Supplier silence.** What do you do if a supplier never answers? Rubric: 3 = escalate via procurement, grade U, exception/compensating controls, alternative supplier.
- **EX059 — Currency plan.** Write a three-item plan for staying current. Rubric: 3 = sources, cadence, update actions.
- **EX060 — Next role.** Name two workflow responsibilities you could take on next and why. Rubric: 3 = realistic, linked to evidence of skill.

### Synthesis

The portfolio and final review demonstrate a repeatable, evidence-based workflow and the communication skills to run it, with a plan to stay current.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Numbers about MTI are synthetic.

**EX001.** AES-256: keep (Grover only square-roots search). RSA-2048: replace (Shor). SHA-256: keep (no practical quantum break). ECDSA P-256: replace (Shor).

**EX002.** FIPS 203 ML-KEM: key establishment. FIPS 204 ML-DSA: general-purpose signatures. FIPS 205 SLH-DSA: hash-based signatures.

**EX003.** HNDL: life-policy record transfers over VPNs with classical key exchange. Forge-later: the internal root CA or signed policy documents that must stay verifiable for decades.

**EX004.** "NIST IR 8547, an initial public draft, proposes deprecating quantum-vulnerable algorithms after 2030 and disallowing them after 2035; these dates are not yet final."

**EX005.** "Hybrid TLS protects session key exchange against future decryption; our certificates still use classical signatures and need a separate migration."

**EX006.** At risk when 10 + 3 > *z*, i.e. *z* < 13 years.

**EX007.** Regulatory record-keeping rules and policy/claims contracts, confirmed with data owners; the retention schedule as a cross-check.

**EX008.** Data owners: lifetime questions. System owners: clear findings and dates. Procurement: clause text. Legal/compliance: obligations mapping. Executive sponsor: decisions and risk posture. (Auditors: evidence.)

**EX009.** It is at risk under every assumed timeline in the sweep, because its 40-year lifetime dwarfs any plausible *z*.

**EX010.** "Records that must stay private for decades could be recorded today and decrypted later. We are protecting those transfers first, then claims and portal traffic. This order is right whichever quantum timeline turns out to be true."

**EX011.** Systems; methods; time window; data handling; contacts (and stop conditions).

**EX012.** Collect: OpenSSH version; configured `KexAlgorithms`; host-key types. Do not collect: transferred file contents; user credentials or session data.

**EX013.** "Source: config export (read-only); date 2026-10-06; collector: coordinator; system: insurer-sftp-01/02; classification: confidential – security inventory; ticket SEC-118."

**EX014.** Stop; do not copy or use the key; report via the security process immediately; record what and where; follow instructions on revocation.

**EX015.** Record as "supplier statement (grade D), confidential"; store with restricted access; share only with people who need it for the programme.

**EX016.** broker-portal has hybrid key exchange; its signature remains RSA-2048 (classical).

**EX017.** Observed handshake A; supplier email D; CA database record B; architecture diagram C.

**EX018.** claims-app/key-exchange, policy-db/key-exchange, office-vpn/key-exchange: HNDL (record-now). broker-portal/signature and claims-app/signature: forge-later.

**EX019.** 1 of 6 assets = 17 %; report it next to every coverage figure, e.g. "5 of 6 assets assessed; 1 (17 %) unknown".

**EX020.** "Determine key-exchange and signature algorithms used by the call recorder (model, version). Method: supplier questionnaire and configuration export. Owner: Contact Centre IT. Due: 30 days."

**EX021.** The claims portal offers the hybrid group but lists X25519 first; the server's preference wins, so clients negotiate classical even though hybrid is "present".

**EX022.** The server certificate (encrypted in TLS 1.3); get it from configuration or the certificate inventory.

**EX023.** "PQC-ready": 1. "ML-KEM-768 hybrid in TLS 1.3 from v8.2, shipped": 3 if it can be verified, otherwise 2. "Roadmap 2027 for RFC 9370": 2.

**EX024.** "hr-intranet offers only classical groups (configuration audit, 6 Oct). Impact: HR data sessions HNDL-exposed. Recommendation: enable and prefer X25519MLKEM768 after library check; verify via logs. Owner: Corporate IT."

**EX025.** Is the tool current enough to see PQ algorithms? Is the data fresh? Does another source agree?

**EX026.** Scope (scope statement), inventory (graded CBOM), prioritise (priority list), plan (item plans), implement (change records), verify (negotiation evidence), record (residual/exception register), report (quarterly report).

**EX027.** Dated negotiation evidence — logs or tool output showing the hybrid method on the intended service.

**EX028.** Verified 6/64 ≈ 9 %; Unknown 6/64 ≈ 9 %.

**EX029.** Supplier, product/version, request sent (date), answer (date, content), evidence grade, follow-up date, escalation path.

**EX030.** 5 min blocked items and asks; 10 min items due this month; 5 min new unknowns and owners; 5 min exceptions near expiry; 5 min decisions and actions.

**EX031.** Archive transfers: hybrid key exchange + minimization. Internal CA: signature migration plan. Call recorder: investigation (questionnaire). CDN: contract/roadmap tracking and configuration once supported.

**EX032.** Logs or tool output showing X25519MLKEM768 negotiated on the broker portal, with date and coverage.

**EX033.** The algorithm identifier travels with each tag and the policy's accepted list decides validity; removing the old identifier retires it everywhere without code changes.

**EX034.** "Three reinsurers on old clients remain HNDL-exposed until upgrade (deadline 12 months); host keys classical (forge-later). Owner: Infrastructure. Review: quarterly."

**EX035.** Scope: call recorder (model X). Reason: algorithms unknown, supplier answer pending. Compensating: network segmentation, minimal data export. Owner: Contact Centre IT. Expiry: 90 days or supplier answer.

**EX036.** Transfers: HNDL. Document signatures: forge-later. AES-256 at rest: adequate. RSA-OAEP key wrapping: concern only if wrapped keys are exposed outside the HSM.

**EX037.** A: protection 5, time 3 (two quarters). B: protection 3–4 (depends on PSK management), time 4. C: protection 2–3 (reduces volume), time 5 (immediate).

**EX038.** Name Records Management as owner of archive cryptography; add a contract clause requiring dated PQ signature support; register exceptions for delayed offices with expiry.

**EX039.** "Our 40-year policy archive could be recorded today and decrypted later. Within six months we will upgrade office VPNs to new quantum-resistant protection and reduce nightly transfers now. Cost CU 40–70k. Document signatures remain classical until the archive vendor delivers; we are amending the contract to require dates."

**EX040.** When wrapped keys leave the HSM — in backups, exports or recorded transfers — an adversary with a CRQC could unwrap them later.

**EX041.** Executives: decisions, posture, cost, residual risk. Auditors: evidence, method, definitions, sampling.

**EX042.** "No one can say when a quantum computer able to break today's encryption will exist; our priorities are chosen so they remain correct whether that is ten or twenty-five years away."

**EX043.** "Future quantum computers could decrypt data recorded today. We are protecting the most long-lived data first and tracking progress quarterly."

**EX044.** "MTI requires post-quantum signatures for archived policy documents. Please confirm support for ML-DSA (NIST FIPS 204) and planned release dates. We also need timestamp renewal support for existing documents. Please provide a test environment by 31 March. Contact: security programme coordinator."

**EX045.** Explain HNDL: recorded data with long lifetimes is already exposed; show that priorities hold across timelines; offer phased options with costs; record the decision.

**EX046.** Stale evidence; items without owners; unknowns without tasks; Verified without evidence; exceptions past expiry.

**EX047.** "First stage: waiting for more data before expanding. Second: safe to expand. Third: a fault at one site is being investigated; that site is paused."

**EX048.** Move the item back to In progress; add a monthly automatic re-check of all Verified items.

**EX049.** Engage the right owners; establish impact; send stakeholder communication; mark the item blocked with reason in the tracker (and record lessons).

**EX050.** Share of sampled items whose evidence matches tracker state = matching items / sampled items (e.g. 9/10 = 90 %), reported monthly.

**EX051.** Day 1 scope/authorization, graded inventory; Day 2 priority list and Mosca table; Day 3 item plans, supplier requests, findings; Day 4 rollout tracking and incident handling; Day 5 report and presentation.

**EX052.** A grade D claim is unverified; spending or scheduling on it risks error, so the next action becomes verification rather than migration.

**EX053.** "Today 10:20 the quote API's post-quantum protection was found disabled after an update. No outage; quotes continue. The platform team is restoring the setting now. Next update by 14:00."

**EX054.** Inventory and priority accuracy; finding quality; evidence handling; tracker integrity; communication and incident handling.

**EX055.** "What went well was… I would change… The skill I need to practise is… One workflow improvement is… My next step is…"

**EX056.** Explainer → accurate communication (Ch 1); graded CBOM → inventory method (Ch 4); tracker → workflow (Ch 6); case analysis → recommendation (Ch 8); reports → audience communication (Ch 9).

**EX057.** By dated operational evidence — negotiation logs or tool output — from a named source showing the control in effect, rechecked monthly.

**EX058.** Escalate via procurement/account management; keep grade U; apply compensating controls under a time-limited exception; consider alternative suppliers at renewal.

**EX059.** Sources: NIST CSRC, IETF datatracker, sector guidance; cadence: monthly scan, quarterly explainer update; actions: update standards section and inform the sponsor of status changes.

**EX060.** Running the quarterly report (shown by portfolio reports) and coordinating supplier questionnaires (shown by scored answers and dependency tracking).

## Twelve-subject teaching route

This is the **professional** course for practitioners running the migration workflow at the synthetic **Marlow & Tide Insurance (MTI)**: foundations, context, authorized evidence, inventory, tool interpretation, workflow, controls and verification, case analysis, communication, quality and a supervised lab.

## References

Links checked 12 October 2026; standards status changes, so re-verify.

- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- IETF RFCs: 8784 (IKEv2 PSK mixing), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
