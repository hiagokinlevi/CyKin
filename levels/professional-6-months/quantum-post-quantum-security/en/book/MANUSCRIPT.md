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

Ask data owners which records fall under each clock before ranking anything.

### 1.4 Hybrid key exchange

During the transition, systems combine a post-quantum method with a traditional one so an attacker would need to break both. This *hybrid* approach (terminology in [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) is now available in common web software as the TLS group X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)). Hybrid key exchange protects the confidentiality of sessions; it does not by itself make certificates or signatures post-quantum.

For MTI this means the broker portal's recorded sessions are protected once hybrid is negotiated, but the portal's RSA-2048 certificate still needs its own plan.

### 1.5 Worked example

A draft status report says: "Our website is now quantum-proof because we enabled Kyber." Corrected: "The broker portal now uses hybrid post-quantum key exchange (X25519MLKEM768, based on ML-KEM from NIST FIPS 203) for connections from up-to-date browsers. This protects recorded portal traffic against future decryption. The portal's certificate still uses a classical signature; certificate migration is planned separately."

Note what the correction does. It names the service, the algorithm and its standard, says which clients benefit, states what is protected, and says plainly what is not yet done. It also drops "Kyber", the pre-standard name, in favour of ML-KEM. Use the same pattern whenever a team reports progress to you.

### 1.6 Practice task

Rewrite three sentences from a vendor brochure or news article about quantum security so that they are accurate, sourced and appropriately cautious.

For each sentence, record the original, your rewrite and the source you used to check it. Look for three typical faults: claims of permanence such as "quantum-proof", draft dates presented as rules, and hybrid key exchange described as if it also covered certificates. Where a claim cannot be checked, say so instead of guessing. Keep the rewrites; they become your accurate explainer for the portfolio.

### 1.7 Common errors and limits

- "Quantum-proof" or "unbreakable" claims.
- Treating IR 8547's draft dates as final.
- Saying hybrid key exchange makes the whole system post-quantum.

Each error costs credibility later. An MTI report that called the portal "quantum-proof" would be contradicted by the first auditor who looked at its classical certificate. A plan built on IR 8547's proposed 2030 and 2035 dates as fixed law would need rewriting if the final text changes. Check every status report against these three before it leaves your desk. Ask a colleague to read it too.

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

Where sources disagree, take the longer lifetime and record the disagreement. For example, a reinsurance contract may require claims data to be kept longer than the internal schedule says. A lifetime with no source is a guess and should be graded as one.

### 2.2 Mosca's rule

Mosca (2018): if data must stay secure for *x* years, migration takes *y* years, and a capable quantum computer may arrive in *z* years, then data is already at risk when *x* + *y* > *z*. Since nobody knows *z*, try several values.

For MTI the archive's x of 40 years exceeds any plausible z on its own, so the decision does not depend on the forecast. Quote requests, with x close to zero, are never at risk however short z is. The interesting cases lie in between, such as claims records, where the answer changes with z.

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

Change the inputs to see how sensitive the list is. If migration of claims records took five years instead of three, claims would be at risk at z = 15 as well. Record such sensitivities next to the table: they tell the sponsor which estimates deserve better evidence.

### 2.4 Stakeholders

Data owners (underwriting, claims) set lifetimes; system owners (IT teams) make changes; suppliers control products; procurement writes contracts; legal and compliance track obligations; executives approve budgets and accept risk; auditors check evidence. List what each needs from the workflow and what you need from them.

At MTI, underwriting owns the life-policy lifetime and claims owns the 10-year claims lifetime; the infrastructure team owns the reinsurer SFTP servers. Write each name into the stakeholder map with a contact, so requests reach a person rather than a department.

### 2.5 Worked example

MTI's first priority list: 1) transfers of life-policy records between offices and the archive; 2) reinsurer SFTP exchanges carrying claims data; 3) broker portal; 4) internal CA planning (forge-later, long validity). Quote requests are deprioritised. The list is explained to the executive sponsor as "protect what must stay secret longest, first".

Each place on the list has a reason that can be traced to Lab M or to exposure class. The internal CA appears despite carrying no secrets because its long validity makes it a forge-later concern. Keep the reasons with the list so it can be defended.

### 2.6 Practice task

Build a five-row table of MTI services with data, lifetime, source of lifetime and owner; run Lab M with your own values.

Source each lifetime from a retention schedule, contract or owner statement, and write which. Then compare your Lab M output with the book's: if a service moves in or out of the at-risk list, explain why in one sentence. Ask a peer to check that each owner named actually controls the service, not just uses it. Keep the table in your portfolio.

### 2.7 Common errors and limits

- Lifetimes guessed instead of sourced.
- A single assumed quantum date.
- Forgetting procurement and legal as stakeholders.

Each error weakens the priority list in a different way. A guessed lifetime cannot be defended to an auditor. A single quantum date makes the list look like a forecast and invites argument about the date rather than the data. Leaving out procurement and legal means contract clauses and obligations surface late, after suppliers have already set their roadmaps. Check your own table for each of them.

### 2.8 Revisiting the list

Priorities change when facts change: a new contract extends a retention period, a supplier ships hybrid support, a service is retired. Review the priority list each quarter with data owners and system owners, record what changed and why, and keep the old versions. Auditors and executives trust a list that visibly evolves with evidence more than one that never changes.

At MTI a typical trigger would be the archive vendor publishing dates for ML-DSA support, which would change how the forge-later item is planned.

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

At MTI the SEC-118 ticket is the model: it names the servers, the read-only method, the dates, the repository and a contact. Keep a copy of every authorization with the evidence it produced, and stop work when the window closes, even if the task is unfinished.

### 3.2 Minimum necessary evidence

Collect what answers the question: algorithm names, versions, certificate details, dates. Do not collect message contents or customer data. Prefer configuration exports and summaries over raw captures.

For the reinsurer SFTP servers, this means an export of OpenSSH version and key-exchange settings, not samples of transferred files. If a team offers more than you need, decline politely and record that you did. Less evidence is easier to protect and simpler to delete when the programme ends. Write down what you chose not to collect.

### 3.3 Storage and labelling

Store evidence in the agreed repository with labels: source, date, collector, system, classification. Restrict access; inventories of weaknesses are sensitive. Keep a log of who accessed what.

Use the same label fields for every item so that searches work across sources: an export, a questionnaire and a log summary should all show who collected them and when. Review the access log monthly, and remove people who no longer need access. Evidence that cannot be traced to a source and date should be graded U until it can.

### 3.4 Sensitive findings

If you find something serious — an exposed private key, an unpatched system with a known vulnerability — report it immediately through the security process; do not investigate further on your own.

Record what you saw, when and where, and pass it to the incident contact named in your authorization. Do not copy a discovered key or test whether it works; that would be outside your authorization and could damage evidence. Afterwards, note in the tracker that the item is waiting on the security process.

### 3.5 Supplier information

Suppliers may share roadmaps under confidentiality. Record them as supplier statements, respect the agreement, and do not forward them outside the people who need them.

Store them with restricted access, as MTI did with the NDA roadmap, and grade the claims they contain as D until observed. When summarising for executives, refer to a roadmap by its date and status without quoting confidential details. If a supplier asks for its roadmap to be deleted, follow the agreement and note the deletion in the evidence log.

### 3.6 Worked example

MTI's coordinator requests configuration exports for the reinsurer SFTP servers (inventory name `insurer-sftp`). The authorization (ticket SEC-118) covers read-only export, 1–15 October, results stored in the security evidence repository, contact the infrastructure lead. The export shows OpenSSH version and key-exchange settings; no file contents are touched. A supplier's roadmap received under NDA is stored with restricted access and labelled "supplier statement, confidential".

Note what made this work: the scope was narrow, the method was read-only, the window had an end date, and the contact was named in advance. The roadmap was useful but stayed confidential. Both items can be traced later through their labels.

### 3.7 Practice task

Write an authorization request and an evidence label for one inventory activity.

Choose a real kind of activity, such as a certificate export from MTI's internal CA. The request should name systems, method, time window, storage, data handling and a contact, like SEC-118. The label should give source, date, collector, system and classification. Ask a peer whether a system owner could approve your request without asking a single follow-up question. Then revise the request once and keep both versions to show what you improved.

### 3.8 Common errors and limits

- Collecting more data than needed.
- Evidence without labels.
- Sharing supplier roadmaps widely.

Each error has a cost. Excess data enlarges what must be protected and later deleted. Unlabelled evidence cannot support a grade or be traced in an audit, so the work must be repeated. A roadmap shared beyond the agreement can breach an NDA and damage the supplier relationship on which several MTI tracker items depend. Check each piece of evidence against all three before filing it. Correct them before filing.

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

At MTI the broker portal's key exchange was seen in passive observation, its certificate came from configuration, and the claims app's signing algorithm was known only from code. No single source covered all six assets. Record which source supplied each line of the CBOM, because the source sets the evidence grade. Note where two sources disagree and ask the owner which is current.

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

The script counts assets, flags quantum-vulnerable uses and lists where hybrid key exchange is already present. Notice that billing's AES-256-GCM is not flagged, because symmetric encryption at that size remains adequate, and that the call recorder is counted as unknown rather than safe. The 17 % unknown share is the first headline measure: one asset in six cannot yet be assessed. Run it with an extra record of your own and check that the counts change as you expect.

### 4.3 Evidence grades

A simple grade: A observed in operation; B authoritative configuration; C inferred from documentation or code; D supplier claim; U unknown. Priorities based on D or U evidence need verification before money is spent.

Grades also tell you how to improve evidence: a D can be raised by asking technical staff to observe the product in operation, and a C by obtaining the configuration. Write the grade next to each record, not just each asset, since one asset can have different grades for different functions.

### 4.4 Exposure classes

Record-now (HNDL): classical key exchange carrying long-lived data. Forge-later: classical signatures trusted for long periods or hard to replace. Adequate: symmetric encryption and hashes at good sizes. Unknown.

In the Lab I extract, policy-db's RSA key exchange is record-now if it carries long-lived data, the broker portal's RSA-2048 signature is forge-later, billing's AES-256-GCM is adequate and the call recorder is unknown. Classify each use of cryptography separately, since one asset can fall in two classes. The class decides which controls apply.

### 4.5 Unknowns as work

Every unknown becomes a task with owner and due date: ask the supplier, request a configuration export, ask technical staff to observe. Track the unknown share as a headline measure.

At MTI the call recorder's U became a questionnaire task for its vendor with a named owner and a due date. The share of unknowns is a better measure of inventory progress than the number of assets listed, because it cannot be improved by counting easy assets twice. Close each task with evidence.

### 4.6 Worked example

MTI's first CBOM extract matches Lab I: six assets, five quantum-vulnerable uses, one unknown (the call recorder). Grades: broker portal A for key exchange (observed) and B for its signature (configuration), claims app A for key exchange and C for signing (code only), policy DB B, call recorder U, office VPN B. Tasks: supplier questionnaire to the call-recorder vendor; confirm claims-app signing algorithm with its owner.

The grades decide what happens next. Items with A or B can be prioritised with confidence; the call recorder cannot be prioritised at all until its vendor answers, and the claims app's signing entry needs owner confirmation because code alone may not reflect what is deployed.

### 4.7 Practice task

Grade and classify each Lab I record and write tasks for the unknowns.

Give each record a grade from A to U and an exposure class, with one line explaining each choice. For the call recorder, write a task with an owner, a due date and the question to ask. Then compare with the worked example and explain any difference. A peer should be able to reproduce your grades from the source column alone. Note which records you could not grade and why.

### 4.8 Common errors and limits

- One source only.
- Treating supplier claims as observations.
- Unknowns without owners.

A single source leaves blind spots: configuration alone misses what is negotiated, and observation alone misses encrypted certificates. A supplier claim treated as an observation can push money toward an asset that is already protected, or away from one that is not. An unknown without an owner simply stays unknown, quarter after quarter, while the headline measure stalls. Check the MTI extract for each of these before relying on it, and fix any you find.

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

At MTI the configuration audit in Lab T showed what the claims portal offered; only log summaries could show what it negotiated. Keep the type of each output beside your finding so readers know whether it describes intent or operation.

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

The script checks two things for each service: whether a hybrid group is offered at all, and whether it is first in the server's preference order. The quote API passes both checks. The SFTP server and the HR intranet fail the first. Note that the script works on configurations only; it cannot show what clients actually negotiate.

### 5.3 Blind spots

A passive sensor in TLS 1.3 sees the negotiated group but not the certificate, which is encrypted. An active scanner with an old library reports everything as classical. A configuration export may be stale. A questionnaire may describe a product version MTI does not run. Write the blind spot next to each result.

For MTI's broker portal, a passive sensor can show X25519MLKEM768 but not the RSA-2048 certificate, which came from configuration. Always pair a result with the source that covers its blind spot before reporting it.

### 5.4 Interpreting questionnaires

Good answers name algorithms and parameter sets (ML-KEM-768 per FIPS 203), protocols (TLS 1.3 hybrid group per RFC 10024; IKEv2 per RFC 9370), product versions and dates, and offer test access. Weak answers say "PQC-ready" or "roadmap under review". Score answers consistently, for example 0 = no answer, 1 = undated claim, 2 = dated roadmap naming algorithms and protocols, 3 = shipped and verifiable.

Apply the same scale to every supplier and keep the answer text with the score, so a reviewer can check it. A score of 2 is still a D grade until the product is observed. Where a supplier offers test access, ask MTI's technical staff to use it and raise the grade with what they find.

### 5.5 From output to finding

A finding states observation, source, date, impact, recommendation and owner. "Claims portal: hybrid group offered but X25519 preferred (configuration audit, 6 October). Impact: claims sessions remain HNDL-exposed. Recommendation: reorder groups to prefer X25519MLKEM768; verify with logs. Owner: Web Platform."

Each element has a purpose: the source and date let a reader judge freshness, the impact links the result to exposure, and the owner makes someone responsible. A finding missing any of them tends to be argued about instead of fixed. Write findings so the owner can act without asking you what you meant.

### 5.6 Worked example

The audit flags insurer-sftp as classical-only. The infrastructure team confirms the OpenSSH version predates hybrid support. Finding raised: upgrade and enable `mlkem768x25519-sha256`; coordinate with reinsurers whose clients may be old; owner Infrastructure; due in one quarter.

Note that the finding was raised only after the infrastructure team confirmed the version; the audit alone could have been stale. The reinsurer coordination is part of the finding because an upgrade on MTI's side protects only partners whose clients also support the hybrid method.

### 5.7 Practice task

Turn each Lab T line into a finding or an "as expected" note.

For each line, write observation, source, date, impact, recommendation and owner, or a one-line note explaining why no action is needed. The quote API should be an "as expected" note; the claims portal and both classical services need findings. Ask whether the HR intranet carries long-lived data before deciding its priority. Keep each finding to a few lines and name the owner. Ask a peer to review them.

### 5.8 Asking the right follow-up

When tool output surprises you, ask technical staff three questions before raising a finding: is the tool current enough to see post-quantum algorithms; is the data fresh; and does the result match another source? Many apparent findings disappear — or become more serious — after these checks.

At MTI, asking these questions about the insurer-sftp result led to the infrastructure team's version check, which turned a tool result into a confirmed finding. Record the answers to the three questions with the finding, so a reviewer can see what was checked and when.

### 5.9 Common errors and limits

- Presence counted as success.
- Ignoring blind spots.
- Scoring questionnaire answers inconsistently.

Each error leads to a wrong report. Counting presence would have marked MTI's claims portal as done while most sessions stayed classical. Ignoring blind spots can hide a classical certificate behind a hybrid result. Inconsistent questionnaire scores make suppliers impossible to compare and invite complaints from those scored harshly. Check every tool-based finding against these three errors before it goes into the tracker. Correct any you find before reporting.

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

Each step produces an input for the next: authorization for inventory, graded evidence for prioritisation, a plan for implementation. At MTI the cycle runs quarterly, so a slipped step shows up in the next report rather than at the end of the programme.

### 6.2 Roles

Coordinator (you): runs the cycle, keeps the tracker, writes reports. System owners: implement changes. Data owners: confirm lifetimes. Procurement: supplier clauses. Security architecture: standards. Executive sponsor: decisions and risk acceptance. Internal audit: independent checks.

At MTI the infrastructure team is the system owner for the reinsurer SFTP servers, underwriting confirms the archive lifetime, and the sponsor approves exceptions. Write the roles into the tracker so each item names a person, and agree with each one what they will provide and by when.

### 6.3 Tracker states

Use simple states: *Unknown* → *Assessed* → *Planned* → *In progress* → *Implemented* → *Verified* → *Closed* (or *Exception*). An item moves to Verified only with evidence of negotiation, not just a change ticket.

Each state needs its own evidence: an inventory record for Assessed, an owner and date for Planned, a change ticket for Implemented and negotiation logs for Verified. Record the date of each state change so the tracker shows how long items take. A move back to an earlier state is also recorded, with a reason, as happened with the broker portal (Chapter 10).

### 6.4 Dependencies

Many items wait on suppliers or partners. Record the dependency, the request sent, the answer and the follow-up date. Escalate unanswered requests through procurement or account management.

At MTI the reinsurer SFTP item depended on partners upgrading their clients, and the archive item depended on the vendor's signature roadmap. Each had a request date and a follow-up date in the tracker. When a dependency is resolved, record the answer as evidence and update the item's grade and state together. Keep this short.

### 6.5 Outcome measures

Report: share of tier-1 items Verified; share Unknown; number of open exceptions and how many are past expiry; supplier answers received. Avoid activity counts such as "meetings held".

Each measure answers a question an executive can act on: how much is protected, how much is still unknown, how much risk is accepted and whether suppliers are engaging. Define each measure once, in writing, and keep the definition unchanged between quarters, or note any change in the report. Show each measure next to last quarter's.

### 6.6 Worked example

MTI's tracker after one quarter (synthetic): 64 tier-1 items — 6 Verified, 9 Implemented, 14 In progress, 18 Planned, 11 Assessed, 6 Unknown; 3 exceptions. Report headline: "9 % of tier-1 items verified, 9 % unknown; reinsurer SFTP and archive transfers in progress; 3 exceptions, none past expiry."

The headline reports outcomes rather than effort. It also makes the gap visible: 9 Implemented items are not yet counted as Verified, because no negotiation evidence exists for them. The figures will look modest; that is accurate. The sponsor can see which items need a push and which need evidence collection rather than more changes.

### 6.7 Practice task

Set up a tracker for ten MTI items and move three through the states with evidence.

Give each item a source, an owner and a current state. For the three you move, attach the evidence that justifies each transition: an inventory record, an owner and date, a change ticket, then negotiation logs before Verified. Ask a peer to check that no item jumps a state without evidence, and that dependencies carry follow-up dates. Keep a record of what evidence you used for each move.

### 6.8 Cadence

A monthly working meeting with system owners keeps items moving; a quarterly report goes to the sponsor; an annual review revisits the standard, priorities and lifetimes. Keep each meeting short and driven by the tracker: blocked items first, then items due, then new unknowns.

At MTI the monthly meeting is where the reinsurer SFTP dependency was chased, and the quarterly report carried the result to the sponsor. Cancel a meeting rather than hold one with nothing on the tracker to discuss, and send a short note of decisions and new due dates after each.

### 6.9 Common errors and limits

- Marking items done on a change ticket alone.
- Dependencies without follow-up dates.
- Activity metrics in reports.

Each error inflates progress or hides delay. A change ticket shows intent, but MTI's broker portal regression showed that configuration can revert. A dependency without a follow-up date can sit unanswered for quarters. Activity metrics such as meetings held tell an executive nothing about protection and crowd out the measures that do. Check the tracker and report for all three before each quarterly report.

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

Not every control applies to every item, and several are often combined, as in MTI's archive case. Record which controls each item uses.

### 7.2 Matching controls

HNDL exposure → hybrid key exchange and minimization first. Forge-later exposure → signature plans, procurement and archive renewal. Unknown → investigation. Supplier-controlled → contract clauses and roadmap tracking.

At MTI the archive transfers are HNDL-exposed, so hybrid key exchange and fewer transfers came first; the archive's document signatures are forge-later, so a vendor deadline and timestamp renewal were planned; and the call recorder, still unknown, went to investigation. Record the reason for each match in the tracker, so later reviewers can see why a control was chosen and change it if the exposure changes.

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

Ask system owners at MTI whether the algorithm is named in configuration or hard-coded. Where an algorithm is hard-coded, migration needs a code change and a release, which takes longer and should be planned earlier. Record the answer in the tracker as a factor in the item's migration time.

### 7.4 Verification

Verification means evidence that the control works in operation: negotiation logs showing hybrid on the intended service, certificate inventory showing new algorithms, questionnaire answers confirmed by observation, minimization confirmed by data-flow review. A change ticket is evidence of intent, not of effect.

At MTI the reinsurer SFTP item was marked Verified only when sshd logs showed partners negotiating the hybrid method. Without that evidence, the item stays Implemented, however confident the owner is. Ask for evidence that covers a normal working period, so occasional clients are included, and record its date.

### 7.5 Residual risk

For each verified item, record what remains: usually classical authentication, partners on old clients, or devices awaiting replacement. Give each residual risk an owner and review date.

For MTI's reinsurer SFTP item, the residual risk was three partners on old clients and classical host keys. Recording it keeps the item honest: verified does not mean finished. When a residual risk is resolved, note the evidence and close it; when it persists past its review date, consider an exception. Keep the list short and specific.

### 7.6 Worked example

Reinsurer SFTP: control — hybrid SSH key exchange after OpenSSH upgrade; verification — sshd logs show 7 of 10 reinsurers negotiating the hybrid; residual — three reinsurers on old clients (notified, deadline in 12 months), host keys classical; owner Infrastructure; review quarterly.

This record is complete because each part points to evidence or a person: the control names the method, verification gives a measured share from logs, the residual risk names what remains, and the owner and review cycle say who follows up and when. Use it as a template.

### 7.7 Practice task

For three MTI items, write control, verification evidence and residual risk.

Choose items in different states: for example the reinsurer SFTP servers, the claims portal and the archive transfers. For each, name the control, say what evidence would show it works in operation, and list what remains afterwards with an owner and review date. Where evidence does not yet exist, write how and when it will be collected. Compare your records with the reinsurer SFTP example and fill any gap you find.

### 7.8 Exceptions

When a control cannot be applied in time, raise an exception: scope, reason, compensating controls, owner, expiry. The sponsor approves; the tracker shows it; expiry triggers review. Exceptions are normal; exceptions without expiry are not.

At MTI the two offices awaiting hardware refresh are the example: interim PSKs as compensating control, expiry at refresh. Each exception names its compensating control, so the sponsor knows what reduces the risk while the main control waits. Review open exceptions at the monthly meeting and report any past expiry in the quarterly report.

### 7.9 Common errors and limits

- Change tickets accepted as verification.
- Residual risk omitted.
- Exceptions without expiry.

Each error makes the tracker overstate protection. A change ticket accepted as verification would have hidden MTI's broker portal regression. Omitting residual risk makes a partly protected item look finished, so classical host keys or old partner clients drop out of view. An exception without an expiry becomes permanent acceptance that nobody decided. Review every Verified item and exception against these three each quarter. Fix any you find. Record what you changed.

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

Notice that the case combines both risks from Chapter 1: classical key exchange on long-lived transfers and classical signatures on long-lived documents. List the facts in a table with their grades before analysing them.

### 8.2 Analysis

Exposure: transfers are HNDL-exposed now (40-year data). Signatures are forge-later exposed (documents must stay verifiable for decades). AES-256 at rest is adequate; RSA key wrapping matters if wrapped keys ever leave the HSM or are backed up off-site.

Grade each fact before using it. Support from firmware version 7.4 is a supplier statement, so it is grade D until tested; the archive vendor's roadmap claim scores 1 on the questionnaire scale, an undated claim. Note also the HSM backup question, which needs an answer from the owner of the HSM.

### 8.3 Options

(A) Upgrade VPN firmware to 7.4 and enable hybrid key exchange; (B) interim RFC 8784 PSKs on the archive tunnels until A; (C) reduce transfers by sending documents once at completion instead of nightly re-sync; (D) archive signature plan: require vendor dates for ML-DSA support and plan timestamp renewal. Criteria: protection, time, cost, operational risk, dependency.

Score each option against every criterion and write a short reason for each score. A protects transfers fully but depends on the supplier's firmware; B is quick but adds key management work; C costs little and reduces exposure immediately; D addresses signatures but depends on the vendor.

### 8.4 Governance gaps

No owner for archive cryptography; no contract clause requiring the archive vendor to support post-quantum signatures; no exception process used for the VPN delay.

Each gap explains part of the risk. Without an owner, nobody chased the archive vendor. Without a clause, MTI has no lever to require dates. Without a registered exception, the VPN delay was accepted by default instead of by decision. Fix the gaps alongside the technical options, or the same problems will recur. Assign each gap an owner.

### 8.5 Recommendation

A within two quarters, with C immediately and B for the two offices whose appliances cannot be upgraded until hardware refresh; D as a procurement action with a deadline; name Records Management as owner of archive cryptography; register an exception for the two offices with expiry at refresh.

Note that the options are combined, not chosen singly: C and B reduce exposure while A is prepared, and D starts the signature work that has the longest lead time. Each part has an owner and a date.

### 8.6 Worked example of presentation

"Recommendation: protect archive transfers within six months by upgrading VPN firmware and enabling hybrid post-quantum key exchange, reduce nightly transfers now, and use interim pre-shared keys at two offices. Cost: CU 40–70k (synthetic). Residual: classical document signatures until the archive vendor delivers ML-DSA; we request a contract amendment with dates."

The presentation states the recommendation first, then what it costs, then what remains. It uses plain words rather than option letters, and it ends with the one request the audience can act on.

### 8.7 Practice task

Analyse the case yourself, score options against criteria, and compare with the recommendation above.

Score each option on protection, time, cost, operational risk and dependency, with a short reason for every score. Grade the facts you rely on, especially the firmware support and the vendor's roadmap claim. Then compare your recommendation with the book's and explain any difference: you may weigh cost or dependency differently, which is acceptable if you say why. Present your scores to a peer and note any changes.

### 8.8 Supervisor review

Present your analysis to your supervisor before sharing it: they will check whether the facts are graded correctly, whether options were considered fairly and whether the recommendation stays within what the evidence supports. Incorporate comments and record what changed.

For the archive case, expect questions such as why option B applies to two offices only and whether the cost range is supported by quotes. Your supervisor may also ask whether the claim about firmware version 7.4 has been tested. Answer with the evidence you have and say what you do not yet know.

### 8.9 Common errors and limits

- Ignoring signatures because key exchange is urgent.
- Options without criteria.
- Missing governance gaps.

Each error leaves part of the risk unmanaged. In MTI's archive case, focusing only on transfers would leave decades-old signed documents with no plan. Options without criteria make the recommendation look like preference. Missing governance gaps means the archive vendor stays unchased and the VPN delay stays unrecorded. Check your analysis for all three before presenting it. Revise your analysis where you find any of them. Note each one you fixed.

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

Write each version from the same tracker so the figures match across audiences. At MTI the executive summary gives the verified share and decisions needed, while the infrastructure team receives the reinsurer SFTP findings with sshd evidence and dates. The archive vendor receives a clear requirement for dated ML-DSA support. Check that each version answers what that audience must decide or do.

### 9.2 Uncertainty

Say what is known (standards published, algorithms in use), what is estimated (migration durations), and what is unknown (when a capable quantum computer will exist). Use ranges and show that recommendations hold across them. Avoid single-date predictions.

At MTI, the priority list rests on Lab M results for z of 10, 15 and 20, and the archive comes first under all three. Saying so lets executives accept the list without having to accept any forecast. Where an estimate drives a decision, give its source and range.

### 9.3 Tone

Fear-based messages ("quantum apocalypse") produce either panic or dismissal. Overconfident messages ("we are quantum-safe") collapse at the first audit. Calm, specific messages work: "we are protecting the data that must stay private longest first; here is progress and what remains."

Read your draft aloud and remove any word that claims certainty you cannot show, or alarm you cannot justify. Check each figure against the tracker before sending. At MTI, the quarterly summary avoided both extremes by stating the verified share and the risks plainly.

### 9.4 Ethics

Reports about weaknesses are sensitive; share them on a need-to-know basis. Do not exaggerate risk to win budget or understate it to avoid work. Credit teams' work accurately. Label synthetic examples in training materials. Report problems you discover, including your own mistakes.

At MTI, a report on the claims portal's weak preference order goes to Web Platform and the sponsor, not to all staff. If you find that a figure you reported was wrong, correct it in the next report and say what changed.

### 9.5 Oral presentation

Lead with the question and answer, show evidence, end with decisions needed. Keep slides simple; prepare for questions about assumptions and status of guidance.

For MTI's quarterly briefing, the question is whether tier-1 data is better protected than last quarter, the answer is the verified share, and the decisions are the contract amendment and the two exceptions. Rehearse with someone who will ask whether IR 8547 is final, and answer that it is a draft with proposed dates. Keep it short.

### 9.6 Worked example

Quarterly executive summary (synthetic): "Position: 9 % of tier-1 items verified, 9 % still unknown (down from 31 %). Highlights: reinsurer SFTP now uses hybrid post-quantum key exchange for 7 of 10 partners. Risks: archive vendor has no dated plan for post-quantum signatures. Decisions needed: approve contract amendment request; approve two exceptions for offices awaiting hardware refresh. Outlook: archive transfers protected by Q2 if firmware upgrades proceed."

The summary follows the order of an executive's questions: where are we, what improved, what is at risk, what do you need from me and what comes next. Each figure can be traced to the tracker. The outlook is conditional, which is honest about the dependency on firmware upgrades.

### 9.7 Practice task

Write the same quarter's message for system owners and for a supplier.

For system owners, lead with their open findings, evidence and deadlines; for the archive vendor, state the requirement for dated ML-DSA support and the contract amendment request, without sharing MTI's internal weakness details. Check that both use the same figures as the executive summary. Ask a peer whether each recipient would know exactly what to do after reading it. Revise both after feedback. Keep both in your portfolio.

### 9.8 Handling pushback

Owners may object to deadlines; executives may question cost. Respond with evidence: the lifetime of the data, the robustness of the priority list across timelines, the cost range and the residual risk of waiting. Offer options rather than ultimatums, and record the decision and who made it.

At MTI an owner who resists reordering the claims portal's groups might be offered a staged rollout with gate results instead of an immediate change. Ask what would make the deadline possible, such as help from a supplier or a different change window, and include that in the options.

### 9.9 Common errors and limits

- One report for all audiences.
- False precision about timelines.
- Sharing weakness details widely.

Each error weakens trust. A single report gives executives detail they will not read and owners too little to act on. False precision about when a quantum computer will exist invites argument and is easily discredited. Sharing weakness details widely creates a map useful to attackers and breaks the need-to-know rule. Review each report against all three before sending it. Rewrite any that fail. Note what you changed and why.

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

Record the result of each sample, including items that passed, so trends become visible. At MTI the broker portal regression was found this way. When a sample fails, fix the item, then ask whether the same failure could affect similar items and check those too. Keep the sampling method the same each month so results can be compared over time.

### 10.2 Workflow failures

*Silent fallback*: an item verified last quarter has reverted to classical after an update. *Stuck items*: dependencies with no follow-up. *Scope creep*: the workflow absorbs unrelated work. *Report drift*: definitions change between quarters without notice.

Each failure has a different remedy: re-verification for silent fallback, escalation for stuck items, a scope review for creep and a definitions log for drift. Check for all four at the monthly meeting. At MTI, the broker portal regression was a silent fallback, caught by sampling. Record each failure found and the remedy applied.

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

Read the three results carefully. The first canary held because 5,000 connections are too few to show that failures are within budget, so more data is needed. The 10 % canary was promoted. The proxy site held because failures were clearly high, which points to a fault that needs technical diagnosis.

### 10.4 Coordinating troubleshooting

When a rollout causes problems, your role is coordination: make sure the right owners are engaged, the impact is understood, communication goes out, the tracker shows the item as blocked with a reason, and lessons are captured. Leave technical diagnosis to technical staff.

At MTI, when the quote API's hybrid share dropped, the coordinator's job was to engage the platform owner, inform stakeholders and update the tracker, not to diagnose the cause. Keep a short timeline of events and decisions.

### 10.5 Lessons learned

After each quarter and each significant incident, hold a short review: what went well, what didn't, what to change in the workflow. Record changes to definitions and procedures.

Keep the review short and blame-free, and focus on the workflow rather than on individuals. At MTI, the broker portal regression led to a new rule that every Verified item is re-checked monthly. Each lesson should produce a concrete change with an owner, or a recorded decision not to change. Share the review notes with the team.

### 10.6 Worked example

A monthly sample finds that the broker portal, marked Verified in Q1, shows 4 % hybrid in Q2 logs. Cause: a platform update restored a default profile. Actions: item moved back to In progress; owner restores profile; a quality rule is added — every Verified item is re-checked automatically each month. Lessons recorded.

The response follows the workflow: the tracker shows the true state, the owner fixes the cause, and a rule prevents a repeat. Reporting the regression openly protects the credibility of the other Verified figures.

### 10.7 Practice task

Design a monthly quality checklist of eight checks for MTI's tracker.

Include checks for stale evidence, items without owners, unknowns without tasks, Verified items without negotiation evidence and exceptions past expiry. Add checks of your own, such as the monthly re-check of Verified items introduced after the broker portal regression. For each check, say what data it uses, who runs it and what happens when it fails. Keep the checklist to one page so it is used, and review it after each quarter.

### 10.8 Measuring quality

Report a quality measure alongside progress: for example, the share of sampled items whose evidence matched their tracker state. A falling quality score is an early warning that progress figures may be overstated.

At MTI the score would have fallen in the month the broker portal regression was found. Report the score with the sample size, since a sample of ten items gives only a rough figure. If the score falls, look at which kinds of items failed before drawing conclusions, and say in the report how the figures may be affected.

### 10.9 Common errors and limits

- Trusting Verified forever.
- Coordinators doing technical diagnosis.
- Definitions changed silently.

Each error lets the numbers drift from reality. MTI's broker portal showed that Verified items can revert after an update. A coordinator who diagnoses technical faults delays the people who can fix them and may misreport the cause. Definitions changed silently make one quarter's figures incomparable with the next, so trends become meaningless. Add a check for each to your monthly quality checklist. Fix any you find. Record the fixes.

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

Treat the dataset as you would real evidence: request simulated authorization before using it, label it and grade each item. The supervisor checks handling as well as results. Ask questions of the role-players as you would of real owners, and record their answers as evidence.

### 11.2 Tasks

Day 1: scope, authorization (simulated), inventory and grading. Day 2: prioritisation with Mosca's rule and exposure classes. Day 3: plan items, send supplier requests, raise findings. Day 4: a simulated rollout with gate results and one incident (silent fallback). Day 5: quarterly report and presentation.

Keep outputs from each day, since the next day builds on them. At the end of each day, check that the tracker reflects what you learned. The Day 5 report should draw only on outputs from earlier days, so anything missing will show. If you fall behind, tell the supervisor and agree what to drop, as you would with a real sponsor.

### 11.3 The incident

Mid-lab, the "platform owner" reports that the quote API's hybrid share dropped after an update. You coordinate: tracker update, owner engagement, communication to stakeholders, lessons.

Treat it as a real incident. Move the item from Verified to In progress or blocked with a reason, contact the owner, tell stakeholders what changed and when the next update will come, and leave diagnosis to the platform owner. Record a lesson afterwards, as MTI did after the broker portal regression. Keep the timeline.

### 11.4 Assessment

Supervisors assess accuracy of the inventory and priorities, quality of findings and evidence handling, tracker integrity, communication, and handling of the incident.

Each criterion maps to a chapter of the book, so feedback tells you which chapter to revisit. Supervisors look at evidence for every claim you make; an accurate tracker with honest unknowns scores better than a tidy one with unsupported Verified items. Ask for written feedback at the end of each day. Act on it the next day.

### 11.5 Worked example

A participant's Day 2 output: 9 tier-1 assets; priority list headed by archive transfers and reinsurer SFTP; 6 unknowns with tasks; Mosca table across *z* = 10, 15, 20. Supervisor feedback: one supplier claim graded as B should be D; corrected and the priority of that asset reduced pending verification.

The feedback shows why grading matters: the misgraded claim had raised an asset's priority on a supplier's word. Correcting it moved money and attention to items with better evidence. The participant recorded the correction in the daily log.

### 11.6 Practice task

Complete the five-day lab and keep a short daily log.

Each day, write what you produced, what decision you made and why, and what you would do differently. Keep the log factual and short. Note when a role-player's answer changed your plan. The log feeds the reflection and becomes part of your portfolio. Read the log each morning before starting, so yesterday's lessons shape today's work. Share it with your supervisor at the end of the week. At MTI, the log is the first evidence your supervisor reads when signing off the lab.

### 11.7 Reflection

At the end, write a one-page reflection: what you did well, what you would change, which skill needs more practice, and one improvement to the workflow itself. Share it with your supervisor.

Base the reflection on the daily log and the supervisor's feedback rather than memory. Be specific: "I graded a supplier claim as B" is more useful than "grading needs work". Choose one improvement to the workflow that you could propose at MTI, such as a rule for re-checking Verified items, and explain how you would test whether it helped.

### 11.8 Working with simulated stakeholders

Treat role-players as real: send clear, polite requests with deadlines; record answers; escalate when deadlines pass. The lab assesses whether you can keep a workflow moving through other people, which is the core of the practitioner's job.

If a role-player refuses a deadline, record it and offer options, as you would with a real owner. The supervisor watches whether your requests are clear enough to act on without a follow-up question, whether you record answers as evidence, and whether escalation is timely and polite rather than abrupt.

### 11.9 Common errors and limits

- Treating the lab as a spreadsheet exercise.
- Missing the incident's communication step.
- Skipping the reflection.

Each error misses what the lab tests. Treating it as a spreadsheet exercise ignores the people who must act on your requests. Missing the incident's communication step leaves stakeholders unaware of a regression, which damages trust more than the regression itself. Skipping the reflection loses the lesson that the supervisor's feedback was meant to produce. Check your own lab work for all three. Note what you changed.

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

Choose items that show outcomes as well as documents, such as tracker states backed by evidence. Each item should cite its source and date, and graded items should show their grade. Remove anything you cannot support, and note which outcomes are covered weakly so you can address them before the review.

### 12.2 Presentation

Ten minutes: the workflow, what you produced, one decision you supported, one lesson. Then questions.

For example, you might choose the archive case recommendation as the decision and the broker portal regression as the lesson. Keep the workflow overview to two minutes so most of the time goes to results. Rehearse with a timer, and prepare one slide that shows the tracker before and after your work. Leave time for questions, since the review tests how you reason as much as what you produced. Bring the portfolio so you can point to evidence when asked.

### 12.3 Likely questions

"How do you know an item is verified?" "Why is the archive first?" "Is IR 8547 final?" "What does hybrid key exchange not protect?" "What would you do if a supplier never answers?" Answer with evidence from your portfolio.

For example, "How do you know an item is verified?" is answered with negotiation logs from the portfolio, not with a change ticket. Prepare a one-line answer and a piece of evidence for each. Practise the answers with a peer. Keep the evidence ready to show.

### 12.4 Next steps

Agree with your manager which workflow responsibilities you will take on, which skills to deepen (for example, the technical course for hands-on configuration), and when you will review progress.

Write the agreement down with dates and a named reviewer. Choose responsibilities that use what the portfolio shows you can do, such as running the quarterly cycle for one division, and add one new skill at a time. Review the plan after three months and adjust it with your manager. Keep a copy in the portfolio.

### 12.5 Staying current

Track NIST and IETF publications, sector guidance and supplier announcements. Update your explainer and the workflow's standards section when status changes — for example when FN-DSA or the HQC standard is published, or IR 8547 is finalised.

Set a regular time each month to check these sources and record what changed, if anything. When a status changes, update the accurate explainer from Chapter 1 and tell stakeholders who rely on it. When guidance changes, check whether any MTI decision rested on the old status, and if so raise it at the next monthly meeting rather than waiting for the annual review.

### 12.6 Worked example

A participant presents MTI's Q2 position, the archive case recommendation and the broker-portal regression lesson. Asked "What does hybrid not protect?", they answer: "Authentication — the portal certificate is still classical — plus any hop or partner still on classical key exchange, and data recorded before the change." Asked about IR 8547, they state it is a draft with proposed dates and show how MTI's internal dates were set.

The answers work because each points to evidence and states limits. Neither overclaims, and both refer to MTI's own records.

### 12.7 Practice task

Assemble your portfolio and rehearse the presentation with a peer.

Check that each portfolio item maps to a course outcome and carries evidence, not just a document. Rehearse the ten-minute presentation at least twice with a peer who asks the likely questions, including whether IR 8547 is final and what hybrid does not protect. Time yourself, note the questions you found hard, and prepare evidence for each before the final review. Ask the peer for written notes. Revise once and keep both versions.

### 12.8 Professional habits

The habits this course builds — sourcing every claim, grading evidence, recording decisions, stating residual risk, communicating calmly — apply to any security programme. Practise them deliberately in your next role; they are what make a practitioner trusted to coordinate work across teams.

Choose one habit to practise each month and ask a colleague to tell you when you slip. At MTI these habits showed in small things: a supplier claim graded D rather than B, a regression reported openly and an exception given an expiry. Keep doing them when nobody checks.

### 12.9 Common errors and limits

- Portfolios of documents without evidence of outcomes.
- Overclaiming in answers.
- No plan for staying current.

Each error weakens the final review. A portfolio of documents without outcomes shows activity but not results, such as tracker states without evidence. Overclaiming, for example calling IR 8547 final or hybrid key exchange complete protection, undoes the credibility the portfolio builds. Without a plan for staying current, your explainer will be out of date as soon as FN-DSA or the HQC standard is published. Check for each before submitting.

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

<a id="references"></a>

## References

Links checked 12 October 2026; standards status changes, so re-verify.

- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- IETF RFCs: 8784 (IKEv2 PSK mixing), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
