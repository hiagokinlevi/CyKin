# Quantum and Post-Quantum Security: Specialist Practice for Organization-Scale Decisions

- Language: English (`en`); postgraduate specialist course, two years part-time; approximately 600 hours of planned study.
- Editorial state: **draft**. Chapters 1–12 of 12 have authored teaching text; exercises EX001–EX060 (five per chapter) have matching worked results; offline labs use the Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: experienced security specialists — architects, PKI and network leads, risk and assurance managers — who already know classical cryptography and enterprise operations and must now lead post-quantum migration in a large organization. Entry knowledge: a prior degree or equivalent professional experience in security.
- Relation to neighbouring books: the [bachelor's book](../../../../bachelors-4-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) builds foundations and the [engineering book](../../../../engineering-5-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) designs and builds migrations; the [master's book](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) studies them as research. **This book is about specialist practice: deciding, justifying, integrating and assuring migration at organization scale.** It assumes the mathematics and concentrates on judgment under uncertainty, evidence standards and leadership.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. No authority to test real systems. All organizations, people and numbers in examples are **synthetic** unless a sentence cites a public source. Toy code in the labs is not cryptography for use; production systems must use vetted implementations of [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) and [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208).

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Twelve chapters run in four stages: decision foundations (1–4), design and evaluation (5–6), integration, hard cases and assurance (7–9) and research, project and transfer (10–12). Each chapter has learning outcomes, specialist teaching, a worked case, a practice task, common errors, five exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs run offline with Python 3; the printed output is shown so you can check your run.

### The running case: Northgate Regional Health Trust

**Northgate Regional Health Trust (NRHT)** is a synthetic public healthcare provider with six hospitals, 40 clinics and 22,000 staff. It runs an electronic health record (EHR) replicated between two data centres, a picture archiving system (PACS) with a cloud radiology reader, a genomics service whose data must stay confidential for 50 years, connected medical devices, an internal PKI, site-to-site VPNs and a supplier ecosystem of more than 300 vendors. Its executive board has appointed you to lead the post-quantum programme. Every number about NRHT is invented.

### Source policy

Primary sources were checked on 12 October 2026: NIST FIPS 203/204/205 (August 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (initial public draft)](https://doi.org/10.6028/NIST.IR.8547.ipd), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) and [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). FN-DSA (FIPS 206) and the HQC standard were still in development. Re-verify status before relying on it.

## Contents

| Stage | Chapters |
|---|---|
| Decision foundations | [1 Advanced security decision-making](#ch-01) · [2 Current practice](#ch-02) · [3 Specialist evidence](#ch-03) · [4 Advanced risk and ethics](#ch-04) |
| Design and evaluation | [5 Design alternatives](#ch-05) · [6 Controlled evaluation](#ch-06) |
| Integration and assurance | [7 Organizational integration](#ch-07) · [8 Difficult cases](#ch-08) · [9 Leadership and assurance](#ch-09) |
| Research and transfer | [10 Research reading and critique](#ch-10) · [11 Applied project](#ch-11) · [12 Final review and transfer](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame post-quantum migration as decision-making under deep uncertainty; (2) distinguish robust, optimal and regret-minimising choices; (3) make the value judgments inside a prioritisation model explicit; (4) build a decision record that survives audit and turnover; and (5) recognise when to decide now and when to buy information.

### 1.1 Deep uncertainty

Specialists are rarely short of opinions about when a cryptographically relevant quantum computer (CRQC) will exist; they are short of a defensible way to act without knowing. The arrival time *z* in Mosca's inequality (Mosca, 2018) is not a quantity with an agreed probability distribution. Public resource estimates have fallen — Gidney and Ekerå (2021) estimated 20 million noisy qubits for RSA-2048, Gidney (2025) under one million under stated assumptions — but resource estimates are not forecasts. This is *deep uncertainty*: parties cannot agree on the probabilities, and possibly not even on the model. Under deep uncertainty, optimising expected value with a single invented distribution produces false confidence. Prefer *robust* decisions: options that perform acceptably across all plausible scenarios, even if they are optimal in none.

### 1.2 Three decision rules

*Expected-value* choice weights outcomes by scenario probabilities; it is appropriate when probabilities are credible. *Robust* choice discards options that fail badly in any plausible scenario, then picks among the rest by cost. *Minimax regret* compares each option with the best option in hindsight for each scenario and chooses the one whose worst regret is smallest. For quantum migration, robust and regret framings often agree: starting hybrid key exchange on long-lived data flows has small regret if CRQCs arrive late (the cost is modest and builds agility) and avoids large regret if they arrive early (recorded data is protected).

### 1.3 Models encode values

A prioritisation score is not neutral. Multiplying records by harm weight favours volume; treating each person's lifetime privacy as paramount favours long-lived data regardless of volume. Lab D makes the point concrete.

### 1.4 Practical activity — Lab D

```python
# Lab D (ch 1): robust prioritisation - rank synthetic NRHT data flows by expected exposure across timeline scenarios.
flows = {  # name: (confidentiality years x, migration years y, records in transit per year, harm weight) - synthetic
    "genomics transfers": (50, 3, 2e4, 5), "EHR site replication": (25, 2, 3e6, 3),
    "imaging to cloud reader": (10, 2, 8e5, 2), "staff rota sync": (1, 1, 5e5, 1)}
scenarios = {"early z=8": (8, 0.25), "mid z=15": (15, 0.5), "late z=25": (25, 0.25)}  # (z, subjective weight)
score = {}
for name, (x, y, vol, harm) in flows.items():
    s = sum(w * (vol * harm if x + y > z else 0) for z, w in scenarios.values())
    score[name] = s
    print(f"{name:24s} late in: {[k for k, (z, _) in scenarios.items() if x + y > z]}")
print("ranking by weighted exposure:", [n for n, _ in sorted(score.items(), key=lambda kv: -kv[1])])
```

Expected output:

```text
genomics transfers       late in: ['early z=8', 'mid z=15', 'late z=25']
EHR site replication     late in: ['early z=8', 'mid z=15', 'late z=25']
imaging to cloud reader  late in: ['early z=8']
staff rota sync          late in: []
ranking by weighted exposure: ['EHR site replication', 'imaging to cloud reader', 'genomics transfers', 'staff rota sync']
```

The volume-weighted score ranks imaging above genomics even though genomic data is exposed in every scenario and stays sensitive for 50 years. The arithmetic is correct; the question is whether the board accepts its values. A specialist's job is to show both the "late in" column, which is value-light, and the weighted ranking, which is value-laden, and to make the choice of weights an explicit governance decision.

### 1.5 Buying information

Some uncertainty can be reduced cheaply: whether a vendor will ship hybrid IKEv2 next year, how many devices are unknown, what the real retention period of a dataset is. *Value of information* reasoning asks whether resolving an uncertainty could change the decision; if not, do not wait for it. CRQC timing usually cannot be bought; inventory facts usually can.

### 1.6 Worked case

NRHT's board must decide whether to fund an 18-month programme for hybrid key exchange on inter-site links now or wait two years for a planned network refresh. Scenario analysis: if *z* = 8, waiting exposes genomics and EHR replication traffic for two extra years of collection with no remedy; if *z* = 25, acting now costs perhaps 15 % more than folding work into the refresh. The worst regret of waiting (irreversible disclosure of 50-year data) dominates the worst regret of acting (moderate extra cost). Decision: act now on the two long-lived flows; defer the rest to the refresh; buy information on device inventory immediately.

### 1.7 Common errors and limits

- Treating a single CRQC date as the planning basis.
- Hiding value judgments inside scoring weights.
- Waiting for information that cannot change the decision.

### Exercises

- **EX001 — Decision rules.** For NRHT's act-now/wait decision, state which option each of expected value (with *P*(*z* = 8) = 0.1), robust and minimax-regret framings favour, using qualitative reasoning. Rubric: 3 = all three framings applied with stated assumptions.
- **EX002 — Values in the model.** Propose a scoring change to Lab D that would rank genomics first, and state the value it encodes. Rubric: 3 = concrete change and explicit value.
- **EX003 — Value of information.** Name two uncertainties worth resolving before NRHT signs a VPN appliance contract, and one not worth waiting for. Rubric: 3 = justified by decision sensitivity.
- **EX004 — Decision record.** List the fields of a decision record that would let an auditor in 2032 understand the 2026 decision. Rubric: 3 = context, options, scenarios, values/weights, decision, owner, review trigger.
- **EX005 — Robustness test.** Define one scenario that would make "act now on long-lived flows" a poor decision, and say how plausible it is. Rubric: 3 = coherent scenario with honest assessment.

### Synthesis

Quantum migration decisions are made under deep uncertainty. Robust and regret-based framings, explicit value judgments and targeted information-buying produce decisions that can be defended when the future arrives.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Quantum and post-quantum security: current practice

### Learning outcomes

You will (1) summarise the state of standards, guidance and deployment as of the source date; (2) distinguish final, draft and in-development documents; (3) describe how hybrid key exchange reached large-scale deployment; (4) evaluate national and sector guidance for applicability; and (5) maintain a living "state of practice" brief for an organization.

### 2.1 Standards

NIST's final standards are [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) (ML-KEM), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) (ML-DSA) and [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) (SLH-DSA), published in August 2024, together with [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) for the stateful hash-based signatures LMS and XMSS. [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) gives recommendations for KEMs, including their composition. FN-DSA (FIPS 206, derived from Falcon) and a KEM standard based on HQC, selected in 2025 as a code-based backup to ML-KEM, were in development on the source date. Specialists should keep a dated register of each document's status, because procurement and audit language often cites drafts as if they were final.

### 2.2 Transition guidance

NIST's [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) initial public draft (November 2024) proposes deprecating quantum-vulnerable public-key algorithms at 112-bit security after 2030 and disallowing quantum-vulnerable algorithms after 2035. [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) discusses crypto-agility considerations. The NCCoE's [Migration to Post-Quantum Cryptography](https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms) project publishes practice guides developed with industry. National agencies elsewhere publish their own roadmaps; their dates and algorithm preferences differ in detail. A specialist summarises the convergent message — inventory now, prioritise long-lived confidentiality, adopt hybrids during transition, plan signatures and PKI — and flags divergences relevant to the organization's jurisdictions.

### 2.3 Deployment

Hybrid key exchange in TLS moved from experiment to default in a few years. Chrome announced hybrid Kyber in 2023 ([Chromium Blog](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)); the standardised X25519MLKEM768 group ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) followed in major browsers, CDNs and TLS libraries. Post-quantum *authentication* lags: ML-DSA certificates require CA, browser and policy changes, and their size (Chapter 5) is a real engineering cost. IKEv2 supports additional key exchanges via [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html), and vendor support varies. Terminology for hybrids is set by [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html).

### 2.4 Worked case

NRHT's state-of-practice brief, one page, dated: final standards (FIPS 203/204/205, SP 800-208); drafts (IR 8547 dates); in development (FN-DSA, HQC); deployment (hybrid TLS widely available in browsers and CDNs; NRHT's PACS cloud reader already negotiates X25519MLKEM768; VPN appliances: vendor A supports RFC 9370 in current firmware, vendor B "roadmap 2027"); gaps (no public CA issuing ML-DSA certificates for the web PKI at scale; medical-device vendors mostly silent). The brief is reviewed quarterly and every claim has a link.

### 2.5 Practice task

Write your organization's (or NRHT's) state-of-practice brief. Mark each item final, draft, in development or vendor claim.

### 2.6 Common errors and limits

- Citing draft dates as mandates.
- Assuming web deployment status applies to VPNs, devices or PKI.
- Briefs without dates, which age silently.

### Exercises

- **EX006 — Status register.** Classify FIPS 203, IR 8547, FIPS 206, SP 800-227 and RFC 10024 by status on 12 October 2026. Rubric: 3 = five correct with sources.
- **EX007 — Convergent message.** Summarise in four bullets the advice on which major guidance converges. Rubric: 3 = inventory, prioritisation, hybrids, PKI planning.
- **EX008 — Lag analysis.** Explain why post-quantum authentication lags key exchange in TLS deployment. Rubric: 3 = HNDL urgency asymmetry, ecosystem coordination, size.
- **EX009 — Vendor claim.** NRHT's vendor B says "PQC-ready". Write three questions that turn this into checkable claims. Rubric: 3 = algorithm/parameter, protocol/standard, date/version.
- **EX010 — Jurisdiction.** NRHT operates under two national authorities whose roadmaps differ by three years for deprecation. How should the programme set its internal date? Rubric: 3 = earliest binding requirement, documented rationale, review.

### Synthesis

Current practice combines final standards, draft transition guidance and uneven deployment. Specialists maintain dated, sourced briefs that separate what is required, proposed, available and merely claimed.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Quantum and post-quantum security: specialist evidence

### Learning outcomes

You will (1) design an organization-scale cryptographic inventory programme; (2) grade evidence by method and confidence; (3) quantify coverage and the unknown share; (4) handle supplier evidence; and (5) present inventory results as decision evidence rather than as spreadsheets.

### 3.1 Inventory as a programme

At organization scale, a cryptographic bill of materials (CBOM) is not a one-off spreadsheet but a programme with owners, sources, schedules and quality metrics. Sources include passive network sensors, configuration management databases, certificate management systems, code and binary scanners, cloud provider APIs, HSM audit logs and supplier attestations. Each feeds observations — asset, function, algorithm, parameter, implementation, method, date — into a store that can be queried and diffed over time.

### 3.2 Evidence grading

Not all observations are equal. A practical grading: **A** — observed in operation (handshake, HSM log); **B** — read from authoritative configuration; **C** — inferred from code or binary analysis; **D** — supplier statement; **U** — unknown. Decisions about urgent work should rest on A or B evidence where possible; D evidence triggers verification for high-priority assets. Grading also guides investment: if most high-priority assets have only D evidence, the next spend is verification, not migration.

### 3.3 Practical activity — Lab I

```python
# Lab I (ch 3): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("pacs-gateway", "key-exchange", "X25519MLKEM768", "passive"), ("pacs-gateway", "signature", "RSA-2048", "config"),
    ("infusion-hub", "key-exchange", "ECDHE-P256", "passive"), ("infusion-hub", "signature", "ECDSA-P256", "code"),
    ("ehr-core", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("imaging-modality", "unknown", "unknown", "none"), ("site-vpn", "key-exchange", "ECDHE-P384", "config")]
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
quantum-vulnerable uses 5: pacs-gateway/signature, infusion-hub/key-exchange, infusion-hub/signature, ehr-core/key-exchange, site-vpn/key-exchange
hybrid key exchange present on: ['pacs-gateway']
```

Even in this small synthetic set, one asset of six is unknown, and the hybrid that exists covers only key exchange on one gateway. At NRHT scale, a 17 % unknown share across 40,000 assets would be 6,800 assets — a programme in itself.

### 3.4 Supplier evidence

Suppliers control much of the cryptography in a hospital: EHR platforms, PACS, devices, cloud services. Ask for structured inventories (algorithms, libraries, versions), roadmaps with dates and versions, and test access. Contract clauses should require disclosure and notification of cryptographic changes. Treat silence as *unknown*, never as *compliant*.

### 3.5 Presenting evidence

Executives need answers to three questions: what share of priority flows is protected, how confident are we, and what is unknown? Present coverage by evidence grade and priority tier, not raw counts. Show trends over quarters; a falling unknown share is progress even before any algorithm changes.

### 3.6 Worked case

NRHT's first-quarter inventory (synthetic): 41,200 assets; priority tier 1 (long-lived confidentiality or long-lived trust) 1,850 assets. Of tier 1: 22 % grade A/B, 31 % grade C, 29 % grade D, 18 % unknown. The board report leads with "we can confirm the cryptography of only 22 % of our most important assets"; the funded response is sensor coverage on inter-site links and a supplier questionnaire to the 40 suppliers behind 80 % of tier 1.

### 3.7 Common errors and limits

- Treating supplier statements as observations.
- Reporting asset counts without tier and grade.
- Deleting stale observations instead of downgrading them.

### Exercises

- **EX011 — Grade it.** Grade: TLS handshake capture of the EHR replication link; vendor PDF stating "AES-256 and RSA-3072"; binary scan finding OpenSSL 3.x; CMDB field "crypto: standard". Rubric: 3 = A, D, C, B-or-U with justification for the CMDB case.
- **EX012 — Unknown scale.** If NRHT reduces tier-1 unknowns from 18 % to 6 %, how many tier-1 assets moved out of unknown? Rubric: 3 = 0.12 × 1,850 = 222.
- **EX013 — Supplier clause.** Draft a clause requiring notification of cryptographic changes. Rubric: 3 = scope, timing, content, remedy.
- **EX014 — Staleness rule.** Propose a rule for downgrading observations by age, and justify the thresholds. Rubric: 3 = time-based grade decay linked to change rates.
- **EX015 — Board metric.** Design a single chart for the board showing inventory confidence for tier 1. Rubric: 3 = stacked grade shares by quarter, with unknown highlighted.

### Synthesis

Specialist evidence is graded, dated and supplier-aware. Coverage and the unknown share are first-class outcomes, and the board sees confidence, not spreadsheets.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) quantify quantum risk with scenario-based exposure measures; (2) handle risks with long latency and irreversible harm; (3) analyse ethical obligations to data subjects whose harm outlives the organization's horizon; (4) navigate dual-use and disclosure questions at specialist level; and (5) document residual risk acceptance properly.

### 4.1 Latent, irreversible risk

Harvest-now-decrypt-later (HNDL) risk is latent: the loss event (collection) may already have happened, and the harm (decryption) happens later and cannot be undone. Standard risk registers, built for events with immediate detection and recovery, misrepresent it. Represent HNDL as *exposure accumulated per year*: the volume of long-lived data crossing interceptable links under classical key exchange each year, weighted by harm, under each timeline scenario. Each year of delay adds a year's exposure that no later migration removes.

### 4.2 Forge-later and systemic risk

Forge-later risk depends on trust anchors and update channels. A forged code-signing key for a widely deployed medical device could affect patient safety across many hospitals simultaneously; the risk is systemic, not local. Specialists should identify trust anchors whose compromise has correlated effects and prioritise their migration or compensating controls, such as multiple signatures or hardware-bound verification keys that can be rotated.

### 4.3 Obligations to data subjects

A patient's genomic data reveals information about relatives and remains sensitive for generations. The organization's planning horizon (budget cycles, contracts) is shorter than the harm horizon. Ethically, the people bearing the risk — patients — are not party to the decision, which strengthens the duty of care. Specialists should insist that harm horizons, not organizational retention schedules, set *x* for such data, and that minimization (Chapter 5) is considered before cryptographic controls.

### 4.4 Dual use and disclosure

Organization-scale inventories are maps of weakness. Restrict access, publish only aggregates, and treat vulnerability reports from suppliers under coordinated disclosure. Active testing of negotiation, downgrade or fault behaviour belongs in isolated, authorized testbeds; a specialist who directs others is responsible for ensuring those boundaries are written down.

### 4.5 Residual-risk acceptance

When a risk cannot be reduced in time — a legacy imaging modality that cannot be upgraded — the accountable executive accepts it formally: scope, rationale, compensating controls, expiry date and review trigger. Acceptance without expiry becomes permanent by default.

### 4.6 Worked case

NRHT's genomics service sends 20,000 records a year to an external research partner over a TLS link with classical key exchange. Exposure framing: every year adds 20,000 lifetime-sensitive records to what an interceptor could hold. Ethical framing: the harm horizon is ~50 years and includes relatives. Decision: migrate this link to hybrid key exchange within three months, reduce data sent by moving analysis to a trusted research environment, and record that prior years' transfers remain exposed — a residual risk the board formally accepts with a note in the privacy impact assessment.

### 4.7 Common errors and limits

- Scoring HNDL like an ordinary incident with immediate impact.
- Letting retention schedules define harm horizons.
- Risk acceptances without expiry.

### Exercises

- **EX016 — Exposure accumulation.** If migration of the genomics link is delayed by 18 months, how many additional records are exposed? Rubric: 3 = 30,000 with reasoning.
- **EX017 — Systemic anchor.** Identify two NRHT trust anchors with correlated failure effects. Rubric: 3 = two plausible anchors with explanation.
- **EX018 — Acceptance form.** Write a residual-risk acceptance for a legacy MRI scanner with RSA-only firmware verification. Rubric: 3 = scope, rationale, compensating controls, expiry, trigger.
- **EX019 — Ethics argument.** Argue in five sentences why patients' harm horizon should set *x*. Rubric: 3 = non-party bearing risk, irreversibility, duty of care.
- **EX020 — Access control for inventory.** Define who may see the full CBOM and why. Rubric: 3 = least privilege, aggregate reporting, audit.

### Synthesis

Quantum risk is latent, irreversible and sometimes systemic. Specialists express it as accumulated exposure, set horizons by harm to data subjects, guard inventories as sensitive and make residual-risk acceptance explicit and time-limited.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Quantum and post-quantum security: design alternatives

### Learning outcomes

You will (1) enumerate design alternatives for key establishment, authentication and data protection; (2) compare pure post-quantum, hybrid, PSK-augmented and minimization designs; (3) quantify authentication byte costs; (4) choose parameter sets against policy; and (5) document alternatives so reviewers can challenge the choice.

### 5.1 Key-establishment alternatives

*Hybrid PQ/T* (in the sense of [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) combines ML-KEM with ECDH so that the session is secure if either holds; it is the default transition design in TLS (X25519MLKEM768) and IKEv2 (RFC 9370 additional key exchanges). *Pure PQ* uses ML-KEM alone; it reduces complexity and is attractive where policy requires it or where the traditional component adds no value, but it removes the hedge against an unexpected break or implementation flaw. *PSK augmentation* mixes a pre-shared symmetric key into the handshake (as in [RFC 8784](https://www.rfc-editor.org/rfc/rfc8784.html) for IKEv2); it is a quick interim protection against HNDL on a few fixed links but scales poorly. *Minimization and re-architecture* sends less long-lived data — a control independent of algorithms. [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) discusses KEM composition and the requirements on combiners.

### 5.2 Authentication alternatives

Options for certificates: keep classical certificates while monitoring ecosystem readiness (acceptable where forge-later risk is low and certificates are short-lived); issue ML-DSA certificates in closed ecosystems such as internal PKI and device fleets first; use dual or composite certificate approaches during transition where standards and products support them; and use hash-based signatures (SLH-DSA, LMS, XMSS) where conservatism or verification simplicity matters, notably for firmware.

### 5.3 Practical activity — Lab B

```python
# Lab B (ch 5): bytes of authentication in a TLS handshake for different signature choices.
# Sizes in bytes: (public key, signature). ML-DSA from FIPS 204; SLH-DSA-128s from FIPS 205.
algs = {"ECDSA P-256": (65, 72), "RSA-2048": (270, 256), "ML-DSA-44": (1312, 2420),
        "ML-DSA-65": (1952, 3309), "SLH-DSA-SHA2-128s": (32, 7856)}
def chain_bytes(alg, depth=2, scts=2):
    pk, sig = algs[alg]
    certs = depth * (pk + sig + 400)          # leaf + intermediate: key + CA signature + ~400 B fields
    return certs + sig + scts * sig           # + CertificateVerify + embedded SCT signatures
for a in algs:
    print(f"{a:20s} ~{chain_bytes(a):6d} bytes of certificates and signatures")
```

Expected output:

```text
ECDSA P-256          ~  1290 bytes of certificates and signatures
RSA-2048             ~  2620 bytes of certificates and signatures
ML-DSA-44            ~ 15524 bytes of certificates and signatures
ML-DSA-65            ~ 21249 bytes of certificates and signatures
SLH-DSA-SHA2-128s    ~ 40144 bytes of certificates and signatures
```

For an internal service mesh on a data-centre network, 15 kB per handshake is acceptable. For clinic devices on constrained links, or protocols with small message limits, it may not be. The design response is to choose where post-quantum authentication goes first, trim chains, and measure — not to assume.

### 5.4 Parameter policy

Parameter sets map to NIST categories: ML-KEM-512/768/1024 to categories 1/3/5; ML-DSA-44/65/87 to 2/3/5. A specialist sets policy explicitly (for example, category 3 by default, category 5 for national-security-adjacent partners) and records why. Uniform maximum parameters waste bytes and cycles; ad hoc choices make audits painful.

### 5.5 Worked case

NRHT's inter-site EHR replication runs over IPsec. Alternatives: (a) hybrid IKEv2 with ML-KEM-768 on vendor A's appliances (supported now); (b) RFC 8784 PSKs for the two vendor-B sites until 2027; (c) re-architect replication to send only deltas, cutting volume by 70 %; (d) pure ML-KEM — rejected because vendor A's implementation is new and the hedge is valuable. Chosen: (a) + (b) + (c), with (b) expiring when vendor B ships hybrid support. Authentication stays classical for now; the internal PKI plan (Chapter 8) addresses it.

### 5.6 Common errors and limits

- Choosing pure PQ to "be modern" without considering the hedge.
- PSK schemes without rotation and secure distribution.
- Ignoring minimization because it is not cryptography.

### Exercises

- **EX021 — Alternatives table.** Compare hybrid, pure PQ, PSK augmentation and minimization on HNDL protection, complexity, scalability and residual risk. Rubric: 3 = four alternatives × four criteria, defensible.
- **EX022 — Byte budget.** From Lab B, by what factor does ML-DSA-65 exceed ECDSA P-256 in authentication bytes? Rubric: 3 = 21,249/1,290 ≈ 16.5.
- **EX023 — Parameter policy.** Write a two-line parameter policy for NRHT with justification. Rubric: 3 = categories by use, rationale.
- **EX024 — PSK expiry.** Specify conditions under which alternative (b) in 5.5 must end. Rubric: 3 = vendor support verified, migration tested, date bound.
- **EX025 — Pure PQ case.** Describe a context where pure ML-KEM is the better choice. Rubric: 3 = policy requirement or constrained context with argued hedge loss.

### Synthesis

Design alternatives span hybrid, pure, PSK-augmented and minimization approaches for key establishment, and staged, closed-ecosystem-first approaches for authentication. Explicit parameter policy and byte budgets make the choice reviewable.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Quantum and post-quantum security: controlled evaluation

### Learning outcomes

You will (1) design controlled evaluations of migration changes; (2) set decision thresholds before collecting data; (3) use confidence bounds for staged rollout decisions; (4) evaluate interoperability across a heterogeneous estate; and (5) report evaluation results with their validity limits.

### 6.1 Evaluation questions

Specialist evaluation answers decision questions: does enabling a hybrid group on the PACS gateway keep failure rates within budget? Does ML-DSA in the internal PKI break any clinical application? Which VPN firmware versions negotiate the intended methods? Each question needs a population, a measure, a threshold set in advance and a decision rule.

### 6.2 Thresholds before data

Set failure budgets and latency thresholds before the experiment, agreed with service owners. Thresholds set afterwards drift toward whatever the data show. A typical budget: handshake failure rate may rise by at most 0.04 percentage points over baseline, judged by the 95 % upper confidence bound.

### 6.3 Practical activity — Lab K

```python
# Lab K (ch 6): canary gate for enabling a hybrid group - promote only if failures stay within budget.
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

The first stage holds on uncertainty, not on evidence of harm; the proxy site holds on evidence of harm. These are different findings and deserve different actions — extend the first stage; investigate the second.

### 6.4 Interoperability matrices

Hospitals have long tails of clients: old browsers on clinical workstations, embedded browsers in devices, partner systems. An interoperability matrix lists client types × server configurations with observed outcomes. Build it in a lab with representative clients first, then confirm with production telemetry. Gaps in the matrix are unknowns to resolve before broad rollout.

### 6.5 Validity

Lab evaluations have external-validity limits: real inspection proxies, Wi-Fi conditions and device firmware differ. Production canaries have internal-validity limits: concurrent changes and weekly cycles. Report both and prefer conclusions supported by lab and canary evidence together.

### 6.6 Worked case

NRHT evaluates hybrid key exchange on the PACS gateway. Pre-set threshold: upper bound ≤ 0.09 % failures. Lab matrix: 14 client types; two embedded viewers fail with the larger ClientHello. Canary 1 % for two weeks: promote. Canary 10 %: one hospital exceeds the threshold — its legacy inspection proxy. Decision: exclude that hospital, upgrade the proxy, continue elsewhere; the two embedded viewers are routed through a classical-only listener with documented residual risk and a vendor ticket.

### 6.7 Common errors and limits

- Setting thresholds after seeing data.
- Pooling sites, which hides a failing one.
- Lab-only conclusions for production decisions.

### Exercises

- **EX026 — Decision rule.** Write a decision rule for promoting a canary that includes threshold, statistic and minimum duration. Rubric: 3 = all three, justified.
- **EX027 — Interpret holds.** Explain the different actions for Lab K's first and third holds. Rubric: 3 = extend sample vs investigate cause.
- **EX028 — Matrix design.** List six client types NRHT must include in its interoperability matrix. Rubric: 3 = six realistic, distinct types.
- **EX029 — Pooling.** Give a numeric example where pooled results pass but one site fails. Rubric: 3 = correct arithmetic showing masking.
- **EX030 — Validity statement.** Write a validity paragraph for the PACS evaluation. Rubric: 3 = internal and external limits with effects.

### Synthesis

Controlled evaluation fixes thresholds in advance, uses confidence bounds, maps interoperability across real client populations and reports validity limits, so rollout decisions rest on evidence rather than hope.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Quantum and post-quantum security: organizational integration

### Learning outcomes

You will (1) integrate PQC migration into architecture, change, procurement and risk processes; (2) build crypto-agility into platforms through policy; (3) design governance roles and decision rights; (4) align migration with refresh cycles and budgets; and (5) measure programme progress meaningfully.

### 7.1 Not a project, a capability

A migration run as a separate project ends with a report and leaves the organization as rigid as before. Integrated into normal processes, it leaves a capability: architecture reviews ask about algorithms and agility; change management records cryptographic changes; procurement requires inventories and algorithm support; risk management tracks quantum exposure. [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) frames this as crypto-agility at the organizational as well as technical level.

### 7.2 Policy-driven platforms

Platforms that read cryptographic choices from policy let the organization change algorithms by configuration. The algorithm identifier must travel with data and be authenticated, so that a verifier can refuse a retired algorithm.

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
k, m = b"k" * 32, b"discharge summary 42"
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

The same pattern — registry, policy, accepted list, retirement — applies to KEMs and signatures in real platforms.

### 7.4 Governance and decision rights

Define who decides cryptographic policy (a cryptography authority or board), who owns each platform's implementation, who approves exceptions, and who accepts residual risk. Publish a cryptographic standard listing approved algorithms and parameters, transition dates and the exception process.

### 7.5 Refresh cycles and budget

Most hardware is replaced on cycles of five to ten years. Aligning PQC requirements with those cycles avoids premature replacement; it requires procurement clauses now so that equipment bought in 2027 does not need replacing in 2031. Software subscriptions are faster; require roadmaps with dates.

### 7.6 Measuring progress

Count outcomes, not activities: share of tier-1 flows with hybrid key exchange (grade A/B evidence); share of new contracts with PQC clauses; median time to change an algorithm on policy-driven platforms; tier-1 unknown share. Avoid vanity metrics such as "number of meetings held".

### 7.7 Worked case

NRHT establishes a Cryptography Authority chaired by the CISO with architecture, PKI, clinical engineering and procurement members. Its standard (synthetic) sets ML-KEM-768 hybrid as the default for new key establishment, requires algorithm identifiers in new data formats, and adds PQC clauses to all contracts above a threshold. Progress metrics are reviewed quarterly by the audit committee.

### 7.8 Common errors and limits

- Treating migration as a one-off project.
- No exception process, leading to silent non-compliance.
- Activity metrics instead of outcome metrics.

### Exercises

- **EX031 — Process hooks.** Name four existing processes into which PQC requirements should be integrated, with one requirement each. Rubric: 3 = four processes, concrete requirements.
- **EX032 — Decision rights.** Draft a RACI for "approve an exception to hybrid key exchange". Rubric: 3 = responsible, accountable, consulted, informed sensibly assigned.
- **EX033 — Refresh alignment.** A PACS replacement is scheduled for 2029. What must the 2026 tender include? Rubric: 3 = algorithm support, agility, inventory, update commitments.
- **EX034 — Outcome metric.** Convert "PQC awareness sessions delivered" into an outcome metric. Rubric: 3 = measurable behaviour or state change.
- **EX035 — Agility test.** Design a quarterly test showing that a platform can switch algorithms by policy. Rubric: 3 = procedure, evidence, pass criterion.

### Synthesis

Integration turns migration into an organizational capability: policy-driven platforms, clear decision rights, procurement aligned with refresh cycles and outcome metrics.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Quantum and post-quantum security: difficult cases

### Learning outcomes

You will (1) analyse migrations involving medical and embedded devices, internal PKI, long-term archives and third parties; (2) apply compensating controls where migration is impossible; (3) manage stateful hash-based signatures; (4) plan long-term signature validity; and (5) reason about algorithm-break response.

### 8.1 Medical and embedded devices

Devices have regulatory approvals, long lives and vendor-controlled firmware. Changing cryptography may require recertification. Options: vendor firmware with hybrid key exchange where offered; network segmentation and gateways that terminate post-quantum protocols in front of devices; minimised data flows; and procurement requirements for replacements. Patient safety governs change windows.

### 8.2 Internal PKI

The internal PKI anchors VPNs, device identities and service-to-service TLS. A post-quantum PKI plan: stand up an ML-DSA root and intermediates in HSMs that support FIPS 204; distribute the new root to relying parties; issue post-quantum certificates in closed ecosystems first; keep classical hierarchy in parallel; and set end dates for classical issuance aligned with the internal standard.

### 8.3 Stateful hash-based signatures

[SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) approves LMS and XMSS with the requirement that keys and state are managed in hardware modules and not exported. They suit firmware signing. Plan signature capacity, protect state against rollback during HSM failover, and test disaster recovery so that recovery never reuses an index.

### 8.4 Long-term signatures and archives

Signed clinical documents and consent forms must remain verifiable for decades. Archive timestamping and evidence-record renewal can preserve validity across algorithm transitions, provided renewal happens while the older algorithm is still trustworthy. Encrypted archives already exposed in transit cannot be repaired by re-encryption.

### 8.5 Algorithm-break response

Rainbow (Beullens, 2022) and SIKE (Castryck and Decru, 2022) show that candidate schemes can fall quickly; KyberSlash (Bernstein et al., 2024) shows that implementations can leak. A response plan names the decision forum, the configuration paths to disable an algorithm, the systems needing releases or hardware, the fallback (hybrids help), and communications to suppliers and regulators. HQC's selection as a backup KEM gives a future alternative with a different mathematical basis.

### 8.6 Worked case

NRHT's infusion pump fleet (synthetic, 4,000 units) uses RSA-signed firmware verified by a boot ROM and ECDH to a management hub. Vendor offers hybrid key exchange in a 2027 firmware release; boot verification cannot change. Plan: segment pumps into a dedicated VLAN; adopt the 2027 firmware after clinical safety testing; accept forge-later residual risk for firmware until fleet replacement in 2031, with compensating controls (signed-update allow-listing at the hub, anomaly monitoring); require ML-DSA or LMS boot verification in the replacement tender.

### 8.7 Common errors and limits

- Applying IT change windows to clinical devices.
- Building a PQ root without a relying-party distribution plan.
- Software-only LMS signing.

### Exercises

- **EX036 — Compensating controls.** List four compensating controls for devices that cannot migrate. Rubric: 3 = four distinct, effective controls.
- **EX037 — PKI sequence.** Order the PKI plan steps and justify the order. Rubric: 3 = root, distribution, closed ecosystems, broad issuance, classical sunset.
- **EX038 — LMS capacity.** An LMS tree with 2^15 signatures signs 40 firmware images a year. How many years of capacity? Rubric: 3 = 819 years, with comment on multiple trees/HSM failover.
- **EX039 — Archive renewal timing.** When should NRHT renew archive evidence records based on RSA-signed timestamps? Rubric: 3 = well before credible RSA weakness, policy-driven schedule.
- **EX040 — Break drill.** Design a tabletop exercise for "weakness announced in ML-KEM-768". Rubric: 3 = scenario, participants, decisions, success criteria.

### Synthesis

Difficult cases — devices, PKI, stateful signatures, archives and algorithm breaks — need compensating controls, careful sequencing, hardware-held state, timely renewal and rehearsed response.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Quantum and post-quantum security: leadership and assurance

### Learning outcomes

You will (1) lead a multi-year migration programme with clear objectives; (2) design an assurance model with independent verification; (3) prepare evidence for auditors and regulators; (4) communicate with boards, clinicians and suppliers; and (5) sustain the programme through staff turnover and changing guidance.

### 9.1 Programme leadership

A multi-year programme needs a mission ("protect long-lived confidentiality and trust against quantum attack without harming clinical services"), objectives with dates, a roadmap by tier, a budget envelope with ranges, and governance. The leader's job is to keep priorities aligned with evidence as both guidance and technology change, and to protect the programme from being reduced to a compliance checklist.

### 9.2 Three lines of assurance

The first line (platform owners) implements and self-tests; the second line (security and risk) sets standards and monitors; the third line (internal audit) independently tests. For PQC, independent verification means re-observing negotiated algorithms, sampling certificates, reviewing exception registers and testing agility claims, not reading status reports.

### 9.3 Evidence for auditors and regulators

Prepare an evidence pack: cryptographic standard and its approval; inventory with coverage and grades; prioritisation method and decisions; progress metrics with sources; exception and residual-risk register with expiries; test reports; supplier assurance. Each item should be generated by normal operation, so the pack is cheap to refresh.

### 9.4 Communication

Boards need decisions and risk posture; clinicians need assurance that changes will not disrupt care and clear change windows; suppliers need clear requirements and timelines; staff need to know what changes for them. Messages should be calm and specific; avoid both alarm and complacency.

### 9.5 Sustaining

Guidance will change: IR 8547 may be finalised with different dates; FN-DSA and HQC standards will appear. Build review cycles into governance, keep decision records, train successors, and keep the inventory alive. A programme that depends on one expert is fragile.

### 9.6 Worked case

NRHT's year-two assurance review (synthetic): internal audit samples 60 tier-1 flows and re-observes 57 (95 %) with the reported algorithm; three show classical fallback due to a reverted configuration — a finding that leads to configuration-drift monitoring. The exception register has 41 entries; six have passed expiry without review — a finding that leads to automatic escalation. The board receives a one-page posture: tier-1 hybrid coverage 64 % (A/B evidence), unknown 7 %, PKI plan on track, two high residual risks accepted with expiry.

### 9.7 Common errors and limits

- Assurance by status report.
- Evidence packs built specially before audits.
- Programmes dependent on a single expert.

### Exercises

- **EX041 — Objectives.** Write three dated, measurable programme objectives for NRHT. Rubric: 3 = specific, measurable, time-bound, tied to tiers.
- **EX042 — Audit test.** Design an independent test of the claim "all tier-1 inter-site links use hybrid key exchange". Rubric: 3 = sampling, re-observation method, pass criterion.
- **EX043 — Evidence pack.** List seven items in the evidence pack and their sources. Rubric: 3 = seven items with operational sources.
- **EX044 — Clinician message.** Write a 100-word message to clinical leads about a PACS change window. Rubric: 3 = what, when, impact, contact, reassurance.
- **EX045 — Continuity.** Propose three measures that keep the programme alive through leadership change. Rubric: 3 = documentation, governance cycles, distributed expertise.

### Synthesis

Leadership keeps a multi-year programme aligned with evidence; assurance re-observes rather than reads; evidence packs arise from normal operations; and continuity is designed in.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read cryptanalysis, resource-estimate and deployment papers critically; (2) extract assumptions and evaluate their realism; (3) judge preprints and vendor research appropriately; (4) translate research into practice implications; and (5) write a structured critique.

### 10.1 Reading cryptanalysis

Cryptanalysis papers state attack models, complexity and experiments. Ask: does the attack apply to the standardised parameter set or to a variant? Is it classical or quantum? Is complexity asymptotic or concrete? Has it been reproduced? Beullens's Rainbow break (2022) applied to submitted parameters with concrete laptop-scale experiments — decisive. Many claimed lattice attacks improve constants slightly without changing security categories — important but not urgent.

### 10.2 Reading resource estimates

Resource-estimate papers such as Gidney and Ekerå (2021) and Gidney (2025) assume physical error rates, connectivity, code distance, cycle time and algorithmic choices. Extract them into a table. Ask which assumptions current hardware meets and which it does not. A falling estimate under optimistic assumptions is a signal about the direction of travel, not a date.

### 10.3 Reading deployment studies

Deployment papers report negotiated groups, failure rates and performance from measurements. Ask: what population, which vantage point, which period, what biases (for example, scanning only popular websites)? Do results transfer to enterprise or clinical environments?

### 10.4 Preprints and vendor research

Preprints (arXiv, IACR ePrint) are often the first credible source and are routinely cited in this field; weigh them by author track record, reproducibility and subsequent review. Vendor research may be careful but has interests; check whether data and methods are published.

### 10.5 Structured critique

A critique summarises the claim, evaluates evidence and assumptions, identifies what would change the conclusion, and states implications for practice. Keep it to one page for practitioners.

### 10.6 Worked case

Critique of Gidney (2025) for NRHT's board, one page: claim — RSA-2048 could be factored with under one million noisy qubits in under a week; key assumptions — physical error rate around 10^−3, surface-code style error correction, specific connectivity and cycle times; status — preprint by an established author building on peer-reviewed predecessors; implication — the resource gap is narrowing, supporting the board's robust "act now on long-lived flows" decision; it does not give a date and should not be quoted as one.

### 10.7 Common errors and limits

- Treating every new attack paper as urgent.
- Quoting resource estimates as forecasts.
- Dismissing preprints wholesale.

### Exercises

- **EX046 — Assumption table.** Build a five-row assumption table for a resource-estimate paper. Rubric: 3 = error rate, qubit count, runtime, code, connectivity with sources.
- **EX047 — Urgency test.** Give three questions that decide whether a new lattice attack paper changes NRHT's plans. Rubric: 3 = parameter applicability, category impact, reproduction.
- **EX048 — Deployment bias.** Name two biases in internet-wide scanning studies when applied to hospitals. Rubric: 3 = population and vantage biases explained.
- **EX049 — Vendor whitepaper.** List what you would need to trust a vendor's benchmark of hybrid VPN throughput. Rubric: 3 = method, configuration, data availability, independence.
- **EX050 — One-page critique.** Outline the five headings of your critique template. Rubric: 3 = claim, evidence, assumptions, sensitivities, implications.

### Synthesis

Specialists read research for its assumptions and applicability, weigh sources by type and reproducibility, and translate findings into calm, specific implications for practice.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) scope an applied specialist project with an organizational sponsor; (2) produce decision-ready deliverables; (3) apply the evidence, evaluation and governance methods of this book; (4) manage authorization and data protection; and (5) evaluate impact.

### 11.1 Project types

Suitable projects: designing and piloting an inventory programme for one division; producing an internal cryptographic standard with a transition plan; leading an evaluated pilot of hybrid key exchange on one platform; designing a post-quantum PKI roadmap; or building a supplier assurance process. Each produces artefacts the organization will use.

### 11.2 Scoping with a sponsor

Agree with a sponsor: the decision the project supports, scope, deliverables, access, authorization, success criteria, and how results will be used. Written authorization must cover any observation or testing; prefer isolated labs for active tests.

### 11.3 Deliverables

Decision-ready deliverables include a short decision paper, the evidence behind it (inventory extracts, evaluation results, assumption tables), implementation artefacts (policy text, configuration baselines, procurement clauses) and a handover plan.

### 11.4 Data protection

Projects in healthcare touch sensitive systems. Collect metadata, not content; minimise identifiers; store project data securely; and delete it per the agreement.

### 11.5 Impact evaluation

Define impact before starting: for example, "tier-1 unknown share in the radiology division reduced from 25 % to below 10 %" or "supplier questionnaire adopted for all new radiology contracts". Measure after a defined period.

### 11.6 Worked case

Project (synthetic): "Supplier assurance for post-quantum readiness in NRHT radiology." Sponsor: Director of Radiology IT. Deliverables: questionnaire, scoring rubric, contract clauses, results for 18 suppliers, decision paper. Results: 5 suppliers with dated roadmaps and test access; 7 with undated claims; 6 silent. Decision: PQC clauses mandatory in all renewals; silent suppliers escalated to procurement; two suppliers invited to joint lab pilots. Impact after six months: unknown share in radiology fell from 31 % to 12 %.

### 11.7 Common errors and limits

- Projects without a decision to support.
- Deliverables that are reports only, without usable artefacts.
- Impact measures defined after the fact.
### 11.8 Working with resistance

Applied projects meet resistance: service owners worried about outages, suppliers reluctant to disclose, budget holders sceptical of a risk that has not materialised. Treat resistance as information. An owner's fear of outage is a requirement for staged rollout and rollback; a supplier's reluctance is a procurement lever; scepticism is a request for the robust-decision argument of Chapter 1. Record objections and how the project addressed them in the decision paper, because the same objections will return when the work scales beyond the pilot.

### Exercises

- **EX051 — Sponsor agreement.** List eight items for the sponsor agreement. Rubric: 3 = decision, scope, deliverables, access, authorization, success, use, data handling.
- **EX052 — Scoring rubric.** Design a 0–3 rubric for supplier PQC readiness. Rubric: 3 = levels clearly distinguished by evidence.
- **EX053 — Impact.** Compute the reduction in unknown share in 11.6 in percentage points and relative terms. Rubric: 3 = 19 points, ≈ 61 % relative.
- **EX054 — Data protection.** Specify retention and deletion for project data. Rubric: 3 = scope, period, method, verification.
- **EX055 — Handover.** List what the operational owner needs at handover. Rubric: 3 = artefacts, procedures, contacts, open issues.

### Synthesis

Applied projects support real decisions, deliver usable artefacts under proper authorization and data protection, and measure impact against criteria set in advance.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review your portfolio against course outcomes; (2) present and defend organization-scale choices; (3) transfer methods to other domains and future algorithm changes; (4) plan continuing professional development; and (5) leave a maintainable legacy.

### 12.1 Portfolio review

Assemble: the decision records from Chapter 1; state-of-practice brief (2); inventory design and metrics (3); risk and ethics analysis (4); design alternatives (5); evaluation (6); governance model (7); difficult-case plans (8); assurance design (9); research critiques (10); project deliverables (11). For each, note what evidence shows the outcome was met.

### 12.2 Defence

Expect challenges on assumptions (timelines, harm horizons), values (scoring weights), evidence grades, residual-risk acceptance, and status of guidance. Defend with evidence and acknowledge uncertainty.

### 12.3 Transfer

The methods transfer: robust decisions under uncertainty, evidence grading, controlled evaluation, policy-driven agility and assurance by re-observation apply to any future cryptographic transition — a break in a deployed algorithm, a new standard such as FN-DSA, or the eventual retirement of today's hybrids. They also transfer to other long-latency risks.

### 12.4 Continuing development

Track standards (NIST, IETF), sector guidance, cryptanalysis and deployment research. Maintain your state-of-practice brief quarterly. Participate in professional communities and share anonymised lessons.

### 12.5 Legacy

Leave the organization with a living inventory, a cryptographic standard with a review cycle, decision records, an exception register with expiries and trained successors. Success is a programme that continues without you.

### 12.6 Worked case

At NRHT's final review the programme lead presents: tier-1 hybrid coverage 78 % with A/B evidence; unknown 5 %; ML-DSA internal root in place with 40 % of internal service certificates migrated; 12 accepted residual risks, all with expiry; agility test passed on four platforms. An examiner asks what happens if IR 8547 is finalised with earlier dates; the lead shows the decision record for setting internal dates and the governance trigger for review.

### 12.7 Common errors and limits

- Portfolios without evidence of outcomes.
- Defences that overclaim certainty.
- Legacy that depends on the departing lead.
### 12.8 Reflecting on judgment

Close the portfolio with a reflective note on your own judgment: one decision you would make again, one you would change with what you now know, and one assumption you are least sure of. Specialists are trusted not because they are always right but because they show how they reason and update. The note also helps successors understand which parts of the programme rest on firm evidence and which on considered bets.

### Exercises

- **EX056 — Outcome evidence.** For three course outcomes, name the portfolio evidence that demonstrates each. Rubric: 3 = specific artefacts.
- **EX057 — Transfer.** Explain how the programme would handle a new requirement to adopt FN-DSA. Rubric: 3 = policy, inventory, evaluation, rollout via agility.
- **EX058 — Defence answer.** Answer: "Why did you accept residual risk for infusion pumps?" Rubric: 3 = constraints, compensating controls, expiry, safety rationale.
- **EX059 — CPD plan.** Draft a one-year continuing development plan. Rubric: 3 = sources, cadence, outputs.
- **EX060 — Legacy checklist.** List six items that must exist for the programme to continue without you. Rubric: 3 = six concrete items.

### Synthesis

The final review demonstrates outcomes with evidence, defends choices honestly, and transfers methods and capability so that future cryptographic changes find a prepared organization.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Numbers about NRHT are synthetic.

**EX001.** Expected value with *P*(*z* = 8) = 0.1: waiting saves ~15 % programme cost in 90 % of cases but risks irreversible disclosure in 10 %; if harm is valued highly, EV still favours acting, but the result depends on the invented probability. Robust: waiting fails badly in the early scenario, so it is discarded; act now. Minimax regret: worst regret of waiting (irreversible disclosure) exceeds worst regret of acting (moderate cost); act now.

**EX002.** Score by lifetime-weighted records — e.g. multiply by (*x* + *y* − *z*) years of residual exposure, or by harm weight squared for genetic data — or cap volume's influence with log(volume). This encodes the value that lifetime harm to individuals (and relatives) matters more than record counts.

**EX003.** Worth resolving: whether the appliance firmware supports RFC 9370 hybrid IKEv2 now (changes vendor choice); the appliance's planned support life (changes refresh alignment). Not worth waiting for: CRQC arrival date — unresolvable and the decision is robust to it.

**EX004.** Context and question; options considered; scenarios and assumptions (including *z* range and sources); values and weights; evidence and grades; decision and rationale; owner and approver; date; review triggers (guidance change, vendor delivery, new estimate).

**EX005.** A scenario in which a severe implementation flaw in early hybrid appliances causes widespread outages or leaks, or in which ML-KEM is weakened before deployment; plausibility low-to-moderate for implementation flaws (KyberSlash precedent), mitigated by hybrids, vetted firmware and staged rollout.

**EX006.** FIPS 203: final (2024). IR 8547: initial public draft. FIPS 206 (FN-DSA): in development. SP 800-227: final recommendations (2025). RFC 10024: published IETF RFC specifying hybrid TLS groups.

**EX007.** Build and maintain a cryptographic inventory; prioritise data needing long-term confidentiality (HNDL); use PQ/T hybrids during transition; plan PKI and signature migration and crypto-agility.

**EX008.** HNDL makes key exchange urgent while forgery needs a CRQC at attack time; authentication changes need coordinated CA, browser, policy and root-store changes; ML-DSA certificates add many kilobytes, raising performance and compatibility costs.

**EX009.** Which algorithms and parameter sets (e.g. ML-KEM-768 per FIPS 203) in which protocol mechanism (e.g. RFC 9370 for IKEv2)? Which product versions support it now, and on what date for others? Can we test it, and is a cryptographic inventory provided?

**EX010.** Adopt the earliest date that is binding in any jurisdiction for affected systems, or justify a later date with documented risk acceptance; record the rationale and set a governance review when either authority updates guidance.

**EX011.** Handshake capture: A (observed). Vendor PDF: D (supplier statement). Binary scan: C (inferred from code). CMDB "crypto: standard": effectively U — it is configuration-sourced but uninformative, so it cannot support a decision.

**EX012.** (0.18 − 0.06) × 1,850 = 222 assets.

**EX013.** "The supplier shall notify NRHT in writing at least 90 days before any change to cryptographic algorithms, parameters, libraries or protocols in delivered products or services, describing the change, affected versions and interoperability impact. Emergency changes for security fixes shall be notified within 5 working days. Failure to notify is a material breach."

**EX014.** Grade decays one level when observations exceed an age threshold tied to change rate: network observations older than 30 days → B; configuration older than 90 days → C; supplier statements older than 12 months → U. Fast-changing layers decay faster.

**EX015.** A stacked bar per quarter for tier-1 assets showing shares of grades A, B, C, D and U, with U in a contrasting colour and its percentage labelled; target line for U.

**EX016.** 20,000 records/year × 1.5 years = 30,000 additional records.

**EX017.** Internal root CA (anchors VPNs, device identities and internal TLS everywhere); a major device vendor's firmware-signing key (affects all units of a fleet across hospitals simultaneously).

**EX018.** Scope: MRI scanner model X, 6 units, firmware RSA-2048 verification. Rationale: boot ROM immutable; vendor replacement 2030. Compensating controls: isolated VLAN, update allow-listing via vendor portal with out-of-band hash check, monitoring. Expiry: 31 December 2030 or replacement. Trigger: credible CRQC progress, vendor advisory or incident.

**EX019.** Patients bear the harm but do not take part in the decision. Genomic disclosure is irreversible and affects relatives. Harm lasts decades beyond NRHT's retention schedules and budget horizons. Duty of care requires protecting people for the time they can be harmed. Therefore *x* should be the harm horizon.

**EX020.** Full CBOM: Cryptography Authority members and platform owners for their scope, on least-privilege access with audit logging; executives and auditors receive aggregates; suppliers see only their products; never published.

**EX021.** Hybrid: strong HNDL protection, moderate complexity, scales, residual: authentication. Pure PQ: strong if ML-KEM holds, lower complexity, scales, residual: no hedge. PSK: good if PSKs are secret, moderate complexity, scales poorly, residual: key management. Minimization: reduces exposure regardless, variable complexity, scales by design, residual: remaining data.

**EX022.** 21,249 / 1,290 ≈ 16.5 times.

**EX023.** "Default: ML-KEM-768 hybrid key establishment and ML-DSA-65 signatures (category 3), balancing margin and size. Category 5 (ML-KEM-1024/ML-DSA-87) for links where partners or regulation require it."

**EX024.** Vendor B ships hybrid IKEv2 support; NRHT verifies negotiation in lab and canary; migration completed and PSKs revoked; hard end date (e.g. 31 December 2027) with escalation if missed.

**EX025.** A closed system whose policy mandates pure ML-KEM (e.g. a partner requiring CNSA-style pure PQ) or a constrained link where the traditional component's bytes and code matter, accepting the loss of the hedge after mature implementation review.

**EX026.** "Promote when the Wilson 95 % upper bound of handshake failure rate ≤ baseline + 0.04 points, measured over at least 14 days covering two weekly cycles, with no site individually exceeding the bound."

**EX027.** First hold: uncertainty — extend the canary to gather more data. Third hold: evidence of harm at one site — investigate cause (proxy), exclude the site, fix, then retest.

**EX028.** Modern browsers on clinical workstations; legacy browsers on unpatched kiosks; embedded viewers in modalities; mobile apps on staff devices; partner systems (other trusts, labs); inspection proxies/firewalls in the path.

**EX029.** Site A: 10/50,000 failures; site B: 60/10,000. Pooled 70/60,000 = 0.117 %; if the threshold is 0.15 %, the pool passes while site B at 0.6 % fails badly.

**EX030.** Internal: concurrent changes (OS patches) during canaries could confound failures; weekly patterns addressed by two-week durations. External: lab clients may not represent all embedded viewers; one hospital's proxy shows site conditions differ; results apply to configurations tested.

**EX031.** Architecture review: new designs must state algorithms and agility. Change management: record cryptographic changes and rollback. Procurement: PQC clauses and inventory disclosure. Risk management: quantum exposure tracked per tier.

**EX032.** Responsible: platform owner prepares request. Accountable: Cryptography Authority chair. Consulted: security architecture, clinical safety (if clinical), risk. Informed: internal audit, service desk.

**EX033.** Support for FIPS 203/204 algorithms in named protocols by delivery or with dated roadmap; policy-driven algorithm configuration; cryptographic inventory disclosure; update and support commitments over the product's life; test access.

**EX034.** "Share of platform teams whose services pass the quarterly agility test" or "share of tier-1 change requests that record algorithm details".

**EX035.** Quarterly, switch a test service's configured algorithm (e.g. preferred group order or signature algorithm) via policy only; verify negotiation with test clients; restore. Evidence: change ticket, before/after negotiation logs. Pass: change and rollback within one day, no code release.

**EX036.** Segmentation into dedicated VLANs; gateways terminating PQ protocols; minimising data sent by devices; allow-listing and out-of-band verification of updates; enhanced monitoring.

**EX037.** 1) Create ML-DSA root and intermediates in HSMs; 2) distribute root to relying parties; 3) issue PQ certificates in closed ecosystems; 4) broaden issuance; 5) sunset classical issuance. Order follows chain validation dependencies.

**EX038.** 2^15 = 32,768 / 40 ≈ 819 years; capacity is ample, but plan separate trees or reserved index ranges for HSM failover so state is never duplicated.

**EX039.** On a fixed policy schedule well before any credible weakening of RSA — e.g. migrate timestamp renewal to ML-DSA or SLH-DSA as soon as the TSA supports it, and renew existing evidence records immediately thereafter.

**EX040.** Scenario: a credible paper reduces ML-KEM-768 security below category 3. Participants: Cryptography Authority, platform owners, suppliers' contacts, communications. Decisions: move to ML-KEM-1024 or rely on hybrid classical part temporarily; schedule releases. Success: decisions within 48 hours, configuration paths identified for all tier-1 platforms.

**EX041.** "By 31 Dec 2027, 90 % of tier-1 inter-site flows use hybrid key exchange (A/B evidence)." "By 30 Jun 2027, tier-1 unknown share below 5 %." "By 31 Dec 2028, ML-DSA internal root distributed to 100 % of managed relying parties."

**EX042.** Random sample of tier-1 links; independent re-observation from appliance logs or passive sensors of negotiated methods over a week; pass if ≥ 95 % confirm hybrid and every failure has an approved exception.

**EX043.** Cryptographic standard (governance records); inventory with grades (CBOM store); prioritisation method and decisions (decision records); progress metrics (dashboards with sources); exception register (GRC tool); test reports (lab/canary records); supplier assurance (questionnaires and contracts).

**EX044.** "On 14 Nov, 22:00–02:00, we will update how PACS connections set up encryption to protect images long term. Viewing may pause briefly during the window; no change to workflows. Emergency reads continue on the backup viewer. Contact the IT service desk on 4444 with any issue; a radiology IT engineer is on site."

**EX045.** Decision records and runbooks kept current; governance cycles embedded in committees (quarterly reviews); deputies and trained successors with shared responsibilities.

**EX046.** Physical error rate (e.g. 10^−3); number of physical qubits; runtime; error-correcting code and distance; connectivity and cycle time — each with source and whether current hardware meets it.

**EX047.** Does the attack apply to standardised parameter sets? Does it reduce security below the targeted NIST category? Has it been reproduced or peer reviewed?

**EX048.** Population bias: scans cover public websites, not internal clinical systems or devices. Vantage bias: external scanners do not see internal networks, proxies or VPNs.

**EX049.** Test configuration and hardware; algorithms and parameter sets; traffic profile; published data and scripts; independent reproduction or third-party test.

**EX050.** Claim; evidence quality; key assumptions; what would change the conclusion; implications for practice.

**EX051.** Decision supported; scope; deliverables; access; written authorization; success criteria; how results will be used; data handling and deletion.

**EX052.** 0 = no information; 1 = undated claim; 2 = dated roadmap with named algorithms/protocols; 3 = shipped support verified in test plus inventory disclosure.

**EX053.** 31 % − 12 % = 19 points; 19/31 ≈ 61 % relative reduction.

**EX054.** Project data limited to metadata; retained for the project plus 3 months for review; secure deletion with verification log signed by the sponsor; aggregate results retained.

**EX055.** Artefacts (questionnaire, rubric, clauses, results), procedures for running the process, contacts at suppliers and procurement, open issues and dates.

**EX056.** Robust decisions → decision records (Ch 1); evidence standards → inventory grading design (Ch 3); controlled evaluation → canary/evaluation report (Ch 6).

**EX057.** Update the cryptographic standard after FIPS 206 is final; inventory signature uses where FN-DSA's compactness helps; evaluate in lab and canary; roll out via policy-driven platforms with agility tests.

**EX058.** Boot ROM cannot verify PQ signatures; replacement scheduled; compensating controls reduce exposure; acceptance expires at replacement; patient safety requires validated firmware rather than risky interim changes.

**EX059.** Sources: NIST, IETF, sector guidance, IACR ePrint; cadence: monthly reading, quarterly brief update; outputs: updated brief, two critiques per quarter, one talk.

**EX060.** Living CBOM with owners; cryptographic standard with review cycle; decision records; exception register with expiries; runbooks for agility and break response; trained successors.

## Twelve-subject teaching route

This is the **postgraduate specialist** course. It follows the synthetic **Northgate Regional Health Trust (NRHT)** through organization-scale decisions: robust choice, current practice, evidence grading, risk ethics, design alternatives, controlled evaluation, integration, difficult cases, assurance, research critique, applied project and transfer.

## References

Links checked 12 October 2026; standards status changes, so re-verify.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Bernstein, D. J., et al. (2024). KyberSlash. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Chromium Blog (2023). Protecting Chrome Traffic with Hybrid Kyber KEM. <https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html>
- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- Gidney, C., and Ekerå, M. (2021). *Quantum* 5, 433. <https://doi.org/10.22331/q-2021-04-15-433>
- IETF RFCs: 8784 (IKEv2 PSK mixing), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NCCoE. Migration to Post-Quantum Cryptography project. <https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
