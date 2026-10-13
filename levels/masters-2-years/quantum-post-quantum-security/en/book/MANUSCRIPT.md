# Quantum and Post-Quantum Security: Master's Research Methods and Dissertation Practice

- Language: English (`en`); master's course, two years; approximately 1,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–8 of 8 have authored teaching text, exercises EX001–EX050 and matching worked results. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open.
- Audience: beginning researchers with strong domain foundations and research-method literacy who will formulate a question, evaluate prior work and produce reproducible findings in quantum and post-quantum security. Entry knowledge: the [postgraduate](../../../../postgraduate-2-years/quantum-post-quantum-security/en/book/PLAN.md) or [engineering](../../../../engineering-5-years/quantum-post-quantum-security/en/book/PLAN.md) content in this area or equivalent: TLS 1.3, public-key cryptography, basic statistics.
- Relationship to the [doctoral course](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md): the doctorate studies discovery of quantum-vulnerable cryptography across an organization. **This book studies one deployment question in depth** — what happens to real connections when a post-quantum/traditional (PQ/T) hybrid key exchange is switched on — and teaches the full cycle of a master's dissertation around it.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights.
- Educational boundary: not an accredited degree; grants no authority to test any network or product. Every organization, log, participant and number in a worked example is **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

The eight chapters follow one dissertation from question to defense. Each chapter has outcomes, teaching sections, a worked example, a practical activity (offline Python 3 standard library where useful), common errors, exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete, scoped and justified) and a **Continue studying** block. Attempt exercises before the [worked results](#worked-results).

### The synthetic dissertation: the Fragment Study

*Larkspur University* (synthetic: 30,000 users, a campus network with two egress paths — a modern direct path and a legacy inspecting proxy used by the research hospital wing) enabled the hybrid TLS 1.3 group X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) in its managed browsers. Help-desk tickets about "sites not loading" rose. The student's question: **how much of the rise in failed TLS handshakes after enabling the hybrid group is attributable to ClientHello messages that no longer fit in one packet, as opposed to competing causes, and on which network paths?** The fictional log corpus is called **LK-HS-1**; a second campus, *Fenwick College*, provides validation data. Coders **C1–C2** and interviewees **I01–I06** are fictional.

The question is grounded in public experience: when Chrome began offering a hybrid Kyber key share, Google reported that larger ClientHello messages exposed bugs in some middleboxes and servers ([Chromium Blog, 2023](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)), and the community page [tldr.fail](https://tldr.fail/) documents servers that mishandle a ClientHello split across several TCP packets.

## Contents

1. [Research question and literature method](#ch-01)
2. [Quantum and post-quantum security: advanced seminar](#ch-02)
3. [Study design, ethics and reproducibility](#ch-03)
4. [Quantum and post-quantum security: competing explanations](#ch-04)
5. [Proposal and pilot](#ch-05)
6. [Data collection and analysis](#ch-06)
7. [Dissertation writing and limitations](#ch-07)
8. [Independent review and defense](#ch-08)
- [Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes and connection

You will (1) turn an operational complaint into a researchable question; (2) apply the FINER test (feasible, interesting, novel, ethical, relevant); (3) design a documented literature search across standards, academic and practitioner sources; and (4) build an evidence table. The chapter builds on your entry knowledge and prepares the seminar of Chapter 2.

### 1.1 From complaint to question

"Post-quantum broke the internet for the hospital wing" is a complaint. It mixes an intervention (offering X25519MLKEM768), an outcome (users cannot load sites), a population (hospital-wing users) and an implied cause (post-quantum cryptography). A research question separates them and makes the cause something to test rather than assume. Draft one: *Did failures increase?* — answerable but descriptive. Draft two: *Did failures increase more on the proxy path than the direct path?* — comparative. Draft three, the Fragment Study question above: *how much of the increase is attributable to multi-packet ClientHello handling, and where?* — explanatory and bounded. The third draft is harder but is what a dissertation should attempt, because it can inform a decision (fix the proxy, or roll back the group) and can be wrong.

### 1.2 Why size is plausible

A traditional X25519 key share is 32 bytes. ML-KEM-768's encapsulation key is 1,184 bytes ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), Table 3), so the X25519MLKEM768 client share is 1,216 bytes and the server's reply share — ML-KEM ciphertext of 1,088 bytes plus 32 — is 1,120 bytes (RFC 10024). A ClientHello that previously fitted in one TCP segment now often needs two. TLS 1.3 itself handles this ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html) records can span segments), but software that reads only the first packet to make a routing or inspection decision may fail. The mechanism is specific, which makes it testable.

### 1.3 FINER

Feasible: Larkspur's proxy and browser telemetry already log handshake outcomes (synthetic). Interesting: every organization enabling hybrid groups faces the question. Novel: public reports are mostly vendor or browser-wide; few studies attribute failures within one organization with competing explanations tested. Ethical: logs can be minimized to metadata (Chapter 3). Relevant: the answer decides between rolling back quantum protection and repairing infrastructure.

Write the FINER check into the proposal with one sentence of evidence for each letter, not just a tick. For feasibility, name the log sources and confirm with the network team that they keep handshake outcomes for long enough. For novelty, point to the evidence table, where the gap in within-organization attribution is visible.

### 1.4 A documented search

Search three source families separately. **Standards**: RFC Editor and IETF datatracker for TLS hybrid key exchange, ML-KEM in TLS, and ClientHello size. **Academic**: IACR ePrint, ACM/IEEE/USENIX digital libraries, terms "post-quantum TLS performance", "hybrid key exchange deployment", "middlebox ossification". **Practitioner**: browser and CDN engineering blogs, which hold most deployment evidence but are written by interested parties. Record date, database, string and hit counts for each search so that a reader can rerun it — this is the master's-level equivalent of a lab notebook.

### 1.5 Worked example: the evidence table

| Source | Type | Claim relevant to question | Evidence | Limit |
|---|---|---|---|---|
| RFC 10024 | Standard | Defines sizes of hybrid shares | Specification | Says nothing about failure rates |
| Chromium Blog 2023 | Practitioner | Larger ClientHello exposed middlebox bugs | Deployment observation | Browser-wide; no per-network attribution |
| tldr.fail | Community | Some servers mishandle split ClientHello | Curated list | Not a sample; selection unknown |
| FIPS 203 | Standard | ML-KEM sizes | Specification | — |

The table reveals the gap: mechanisms and anecdotes exist, attribution within an organization does not.

Add a row for each new source as the search proceeds, and keep the limit column honest even for sources that support the question. The P-7 paper discussed in the seminar would enter the table with its 240% claim and a limit noting the missing base rate. A reader should be able to see from the table alone why the study is needed.

### 1.6 Common errors and limits

- Letting the complaint's implied cause become the hypothesis without rivals.
- Searching only academic databases in a field where deployment evidence lives in engineering blogs.
- Treating a curated list (tldr.fail) as a random sample.
- Unrecorded searches that cannot be rerun.

Each error has a guard. Write rivals before choosing a hypothesis, as Chapter 4 does with five of them. Search engineering blogs as a separate family with its own limits. Describe tldr.fail as curated, not sampled. Keep a search log with date, database, string and hit count for every run, so an examiner can repeat it.

### Exercises — chapter 1

- **EX001 — Decompose a complaint.** Split "PQC broke Wi-Fi in the library" into intervention, outcome, population and implied cause. Rubric: 3 = all four plus one rival cause.
- **EX002 — Three drafts.** Write descriptive, comparative and explanatory versions of a question about hybrid groups and VPNs. Rubric: 3 = explanatory version bounded and testable.
- **EX003 — Size arithmetic.** Compute client and server key-share sizes for SecP384r1MLKEM1024 using FIPS 203 ML-KEM-1024 sizes (1,568-byte encapsulation key and ciphertext) and a 97-byte uncompressed P-384 point. Rubric: 3 = both sizes correct with sources.
- **EX004 — FINER.** Apply FINER to your own question. Rubric: 3 = each criterion argued, at least one weakness admitted.
- **EX005 — Search log.** Write a search log with three databases, strings and dates. Rubric: 3 = rerunnable.
- **EX006 — Evidence table.** Add two rows from sources you verify yourself. Rubric: 3 = sources primary or clearly labelled practitioner, limits stated.
- **EX007 — Gap statement.** Write the gap in one sentence. Rubric: 3 = names missing evidence precisely.

### Chapter synthesis

A researchable question separates intervention, outcome, population and cause, rests on a specific mechanism and is supported by a rerunnable search across standards, academic and practitioner sources.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Quantum and post-quantum security: advanced seminar

### Learning outcomes and connection

You will (1) explain why key establishment is migrated before signatures; (2) describe the structure of ML-KEM and of a PQ/T hybrid combiner at the level needed to reason about deployment; (3) compare post-quantum families by size and assumption; and (4) critique a seminar paper. It deepens the background of Chapter 1 and grounds the study design of Chapter 3.

### 2.1 Harvest now, decrypt later

An adversary who records encrypted traffic today can decrypt it later if the key exchange falls to a future cryptographically relevant quantum computer running Shor's algorithm ([Shor 1997](https://doi.org/10.1137/S0097539795293172)). Signatures are different: forging a signature later does not help an attacker against a session that has already ended. That asymmetry is why browsers and CDNs deployed hybrid key exchange first and why the Fragment Study concerns key shares, not certificates. Signature migration matters for long-lived trust anchors and firmware, and brings its own size problems — ML-DSA-65 signatures are 3,309 bytes ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) — but it is a later wave.

### 2.2 ML-KEM in one page

ML-KEM is a key-encapsulation mechanism built on the module learning-with-errors problem, a structured variant of LWE ([Regev 2009](https://doi.org/10.1145/1568318.1568324)). Informally, the public key hides a secret vector behind a matrix product plus small noise; encapsulation produces a ciphertext from which only the secret-key holder can recover a shared 32-byte key, and a Fujisaki–Okamoto-style transform gives security against chosen-ciphertext attacks. ML-KEM-512, -768 and -1024 target NIST security categories 1, 3 and 5. For deployment research the essential facts are the sizes (encapsulation key 800/1,184/1,568 bytes; ciphertext 768/1,088/1,568 bytes), the speed (fast — often faster than X25519 in optimized code) and that decapsulation failure is possible but negligible at the standardized parameters. [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) gives NIST's recommendations for using KEMs.

### 2.3 Hybrid combiners

A PQ/T hybrid ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)) runs a post-quantum and a traditional key exchange and derives the session key from both, so that an attacker must break both. In X25519MLKEM768 the two shared secrets are concatenated — ML-KEM first, then X25519 — and fed into the TLS 1.3 key schedule (RFC 10024). The hybrid hedges two risks at once: a future quantum computer (covered by ML-KEM) and an unexpected weakness in the newer lattice assumption (covered by X25519). The breaks of Rainbow ([Beullens 2022](https://eprint.iacr.org/2022/214)) and SIKE ([Castryck and Decru 2022](https://eprint.iacr.org/2022/975)) are why the second hedge is taken seriously.

### 2.4 Families compared

| Family | Example | Assumption | Public key / ciphertext or signature | Deployment note |
|---|---|---|---|---|
| Lattice KEM | ML-KEM-768 | Module-LWE | 1,184 / 1,088 B | Default for TLS hybrids |
| Code KEM | HQC (selected 2025, [IR 8545](https://doi.org/10.6028/NIST.IR.8545)) | Quasi-cyclic codes | Several kB | Backup with different assumption |
| Code KEM | Classic McEliece | Goppa codes | Public keys of hundreds of kB | Long-term static keys, not handshakes |
| Lattice signature | ML-DSA-65 | Module-LWE/SIS | 1,952 B key / 3,309 B signature | Certificates, code signing |
| Hash signature | SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) | Hash functions | Small keys / 7.8–49.9 kB signatures | Conservative; large |

### 2.5 Worked example: seminar critique

The seminar paper (synthetic study "P-7") reports that "hybrid key exchange increases handshake failure by 240%". Critique: the base rate is not stated (240% of what?); the comparison is across two different weeks with a browser update in between; failures are counted per attempt, but retries inflate attempts; and there is no stratification by path. The defensible version would report absolute rates with intervals, a concurrent control and path-level results — which is the Fragment Study's design.

Write the critique in four short paragraphs, one per flaw, each ending with the design change that would fix it. That turns a list of complaints into a method, and it makes the link to the Fragment Study visible: base rates per 10,000 series, a concurrent control cohort, series rather than attempts, and results by egress path.

### 2.6 Common errors and limits

- Saying hybrid key exchange "makes TLS quantum-safe": certificates and stored data are separate.
- Treating relative increases without base rates as evidence.
- Assuming ML-KEM is slow; size, not computation, is the usual deployment issue.
- Forgetting that HQC and FN-DSA standards were still in development on 12 October 2026.

Each error has a concrete correction in this dissertation. Hybrid key exchange protects key establishment only, and certificates migrate later. Rates are reported per 10,000 series with Wilson intervals. ML-KEM's cost in the Fragment Study is the size of the key share, which pushes the ClientHello across a segment boundary. Standards status is dated, and should be checked again before submission.

### Exercises — chapter 2

- **EX008 — Why KEMs first.** Explain the harvest-now-decrypt-later asymmetry in 150 words. Rubric: 3 = correct asymmetry and one case where signatures are urgent.
- **EX009 — ML-KEM facts.** List the three parameter sets with categories and sizes. Rubric: 3 = all correct with FIPS 203 cited.
- **EX010 — Combiner reasoning.** Explain why concatenating both shared secrets into the key schedule requires an attacker to break both. Rubric: 3 = mentions key derivation and the assumption that the KDF behaves well.
- **EX011 — Family choice.** Choose a KEM for a firmware-update channel with long-lived static keys and justify. Rubric: 3 = size/assumption trade-off explicit.
- **EX012 — Critique P-7.** Write a 200-word critique. Rubric: 3 = base rate, confound and unit issues all named.
- **EX013 — Relative to absolute.** Convert "240% increase" into absolute terms if the base rate was 4.5 per 10,000. Rubric: 3 = correct (to 15.3 per 10,000) and comment on meaning.

### Chapter synthesis

Key establishment migrates first because recorded traffic can be decrypted later. ML-KEM is fast but large; hybrids hedge both quantum and classical surprises; and deployment claims need base rates, concurrent controls and stratification.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes and connection

You will (1) choose between observational, quasi-experimental and testbed designs; (2) define outcome, exposure and unit of analysis; (3) minimize personal data in network logs; (4) estimate rates with honest intervals; and (5) plan a reproducible analysis. It operationalizes the question from Chapters 1–2 and prepares the competing explanations of Chapter 4.

### 3.1 Designs

An **observational before/after** study compares failure rates before and after the change; it is cheap but confounded by anything else that changed. A **quasi-experiment** exploits staggered rollout: if the hybrid group was enabled for half of managed browsers first, the other half is a concurrent control. A **testbed** reproduces handshakes through a copy of the proxy with and without the hybrid share and isolates the size mechanism directly, but cannot tell you how often the mechanism matters in real traffic. The Fragment Study combines a staggered-rollout quasi-experiment on LK-HS-1 with a testbed replication — each covers the other's weakness.

### 3.2 Defining the variables

Unit of analysis: a *connection attempt series* — the first attempt plus automatic retries within 10 seconds to the same host — so that retries do not inflate denominators. Exposure: whether the ClientHello offered X25519MLKEM768. Outcome: series ends without a completed handshake. Stratifiers: egress path (direct or legacy proxy), browser version, destination category. Write these definitions before seeing outcome data.

Store the definitions in the data dictionary with the date they were fixed. The pilot later changed one of them, defining a series by hostname rather than address, and that amendment is recorded alongside the original wording.

### 3.3 Ethics and minimization

Handshake logs contain client IP addresses and destination names, which can reveal health conditions (a hospital wing) or private behaviour. Minimize at collection: replace client addresses with a keyed hash rotated monthly; keep destination names only as category labels plus a salted hash; retain no payload; store raw logs only on university systems; obtain approval from the university's ethics or data-protection office; and consult the network team about what users were told. Interviews with help-desk staff (I01–I06) need informed consent and must avoid naming users.

### 3.4 Rates and intervals

Failure rates are small proportions, where the textbook normal interval misbehaves. The Wilson score interval behaves well near zero and is easy to compute with the standard library.

```python
# Lab 3 (synthetic): Wilson 95% intervals for handshake failure rates before/after enabling hybrid.
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
for label, k, n in [("before (x25519 only)", 18, 40000), ("after (hybrid offered)", 61, 40000)]:
    lo, hi = wilson(k, n)
    print(f"{label:24s} {k:3d}/{n} = {1e4*k/n:5.1f} per 10k  95% CI [{1e4*lo:4.1f}, {1e4*hi:4.1f}]")
```

Expected output:

```text
before (x25519 only)      18/40000 =   4.5 per 10k  95% CI [ 2.8,  7.1]
after (hybrid offered)    61/40000 =  15.2 per 10k  95% CI [11.9, 19.6]
```

The synthetic increase from 4.5 to 15.2 failures per 10,000 series is clear — the intervals do not overlap — but it says nothing yet about *why*. That is Chapter 4.

The lab computes the rates for the whole corpus, before stratification. Because both rates are small, the intervals are asymmetric, which the Wilson method handles correctly. Report counts and denominators with every rate, so a reader can recompute the interval; 18 and 61 failures out of 40,000 series each are the figures that later split by path in Lab 4.

### 3.5 Reproducibility plan

Pin the analysis to versioned code and a data dictionary; generate every number in the dissertation from scripts; store the minimized dataset with a checksum; record the exact browser policy that enabled the group and its date. Lab 3b below also documents the size assumptions behind the mechanism so that a reader can recompute them.

```python
# Lab 3b: key-share sizes in a TLS 1.3 ClientHello (sizes from FIPS 203 and RFC 10024).
# X25519 share = 32 bytes; ML-KEM-768 encapsulation key = 1184 bytes; ciphertext = 1088 bytes.
BASE_HELLO = 520          # synthetic size of the rest of a typical ClientHello (illustrative)
MSS = 1460                # TCP payload per segment on a 1500-byte Ethernet path, no options
shares = {"x25519 only": 32,
          "X25519MLKEM768": 1184 + 32,
          "X25519MLKEM768 + x25519": 1184 + 32 + 32}
for name, size in shares.items():
    hello = BASE_HELLO + size + 4          # 4 bytes: group id + length per share (approx.)
    segs = -(-hello // MSS)
    print(f"{name:26s} ClientHello ~{hello:5d} B -> {segs} TCP segment(s)")
print("server share for X25519MLKEM768:", 1088 + 32, "bytes")
```

Expected output:

```text
x25519 only                ClientHello ~  556 B -> 1 TCP segment(s)
X25519MLKEM768             ClientHello ~ 1740 B -> 2 TCP segment(s)
X25519MLKEM768 + x25519    ClientHello ~ 1772 B -> 2 TCP segment(s)
server share for X25519MLKEM768: 1120 bytes
```

The rest-of-ClientHello size (520 bytes) is an illustrative assumption; real sizes vary with extensions, server name length and padding, which is why the testbed measures them directly.

### 3.6 Common errors and limits

- Counting retries as independent attempts.
- Collecting full destination names "just in case".
- Using normal-approximation intervals for rates near zero.
- Treating a before/after difference as a causal effect.

Each error has a guard already in the design: series instead of attempts as the unit, destination categories plus salted hashes instead of names, Wilson intervals for small rates, and a staggered rollout with a concurrent control to separate the effect of the hybrid group from anything else that changed during the same weeks.

### Exercises — chapter 3

- **EX014 — Design choice.** Compare the three designs for the Fragment Study in a table of strengths and threats. Rubric: 3 = each threat matched to a design that addresses it.
- **EX015 — Unit of analysis.** Explain how retries could inflate the failure denominator and bias the rate. Rubric: 3 = direction of bias stated.
- **EX016 — Minimization plan.** Write the data-minimization section for the ethics application. Rubric: 3 = keyed hashing, categories, retention and access covered.
- **EX017 — Wilson by hand.** Compute the Wilson interval for 9 failures in 20,000 series with Lab 3. Rubric: 3 = correct output and interpretation.
- **EX018 — Size sensitivity.** Change Lab 3b's base size to 300 and 1,300 bytes; when does the x25519-only hello need two segments? Rubric: 3 = correct runs and a conclusion about why the testbed must measure.
- **EX019 — Reproducibility checklist.** List eight items a reader needs to reproduce your numbers. Rubric: 3 = includes policy date and data checksum.

### Chapter synthesis

A staggered-rollout quasi-experiment plus a testbed replication, with pre-defined units and outcomes, minimized logs, Wilson intervals and scripted numbers, gives a design whose results can be both trusted and rerun.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Quantum and post-quantum security: competing explanations

### Learning outcomes and connection

You will (1) list rival explanations for an observed effect; (2) predict what each rival implies in data you can collect; (3) use stratification to discriminate between rivals; and (4) recognize when a pattern reverses on aggregation. It applies the design of Chapter 3 and shapes the proposal of Chapter 5.

### 4.1 Rivals for the failure rise

1. **Size mechanism** — multi-packet ClientHello mishandled by the legacy proxy or by some servers.
2. **Software update** — the managed-browser update shipped the same week changed other behaviour.
3. **Unknown codepoint** — some middlebox rejects an unrecognized supported-group value (0x11EC for X25519MLKEM768 in the [IANA registry](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml)), regardless of size.
4. **Seasonality** — term started; more users, more unusual destinations.
5. **Reporting artefact** — a help-desk campaign encouraged reporting, raising tickets but not failures.

Write each rival down with the data that would weaken it before looking at results.

### 4.2 Predictions

Each rival predicts a different fingerprint. Size predicts failures concentrated on the path containing the inspecting proxy and among destinations reached through it, appearing only when the hello crosses a segment boundary — the testbed can vary padding to cross or not cross it. The update predicts a rise on *both* paths. Unknown codepoint predicts failure even when the hybrid share is small enough to fit one segment (testable by offering the codepoint with padding removed, in the testbed only). Seasonality predicts a rise in the control group too. Reporting artefact predicts tickets rising without logged failures rising. Writing these predictions before analysis prevents post-hoc storytelling.

### 4.3 Practical activity — Lab 4: stratify by path

```python
# Lab 4 (synthetic): competing explanations. Is the failure rise caused by ClientHello size,
# or by the client software update shipped the same week? Stratify by path type.
data = {  # (path, hybrid offered): (failures, attempts)
    ("direct", False): (8, 20000), ("direct", True): (9, 20000),
    ("legacy proxy", False): (10, 20000), ("legacy proxy", True): (52, 20000)}
for path in ("direct", "legacy proxy"):
    r0 = 1e4 * data[(path, False)][0] / data[(path, False)][1]
    r1 = 1e4 * data[(path, True)][0] / data[(path, True)][1]
    print(f"{path:13s} before {r0:4.1f}/10k  after {r1:4.1f}/10k  difference {r1-r0:+5.1f}")
```

Expected output:

```text
direct        before  4.0/10k  after  4.5/10k  difference  +0.5
legacy proxy  before  5.0/10k  after 26.0/10k  difference +21.0
```

The aggregate rise is almost entirely on the legacy-proxy path; the direct path barely moves. A browser update would have affected both paths, so rival 2 is weakened. The pattern fits the size mechanism and the unknown-codepoint mechanism equally — only the testbed can separate those two. This is the central lesson of the chapter: one stratification eliminates some rivals, not all.

The lab's before and after totals match Lab 3: 18 and 61 failures out of 40,000 series. Splitting by path shows where the change happened. The direct path's half-point rise is within noise for these counts, while the proxy path's rise is large. Neither stratum yet distinguishes size from codepoint; that needs the testbed with padding varied.

### 4.4 Aggregation reversals

Stratified and aggregate comparisons can disagree. If the hybrid group were enabled first for users who mostly use the direct path, the aggregate failure rate could fall after enabling it even though, within the proxy path, it rose. This is Simpson's paradox; the defence is to report path-stratified rates alongside the aggregate and to explain any reversal rather than choosing the convenient level.

In the Fragment Study the staggered rollout randomized by device identifier makes this reversal unlikely, because both cohorts should use the two paths in similar proportions. Check that assumption with a balance table of path use by cohort before reporting either level. If the cohorts turn out to be unbalanced, report both levels and explain the difference.

### 4.5 Worked example: interview evidence

Help-desk interviews (I01–I06, synthetic) report that complaints came "mostly from the hospital wing" and that clearing the cache "sometimes fixed it". The first is consistent with the proxy path. The second points to a further rival: some clients retried with a smaller hello after a failure (browsers can fall back), so failures were intermittent. Qualitative evidence suggested a mechanism the logs could then test — the series-level unit of analysis from Chapter 3 shows whether retries succeeded without the hybrid share.

### 4.6 Common errors and limits

- Testing only the favoured explanation.
- Treating consistency with one rival as proof when another predicts the same pattern.
- Reporting only the aggregate (or only the stratum) that tells the preferred story.
- Running codepoint or size experiments against production middleboxes; use the testbed.

Each error has a guard used in this chapter: five rivals listed before analysis, predictions that tell them apart, both aggregate and path-level rates reported, and all size and codepoint experiments run on an isolated copy of the proxy. Interview evidence is used to suggest tests, not to settle them.

### Exercises — chapter 4

- **EX020 — Rival table.** Build a table of the five rivals with their predicted fingerprints. Rubric: 3 = each prediction observable.
- **EX021 — Add a rival.** Propose a sixth rival and its prediction. Rubric: 3 = plausible and discriminable.
- **EX022 — Extend Lab 4.** Add a "Wi-Fi guest" path with 6 and 7 failures per 20,000 before/after. Interpret. Rubric: 3 = correct difference and interpretation.
- **EX023 — Simpson construction.** Construct numbers where the aggregate rate falls while both strata rise. Rubric: 3 = arithmetic correct and mechanism explained.
- **EX024 — Separate size from codepoint.** Design a testbed experiment that separates rivals 1 and 3. Rubric: 3 = varies size and codepoint independently, isolated environment.
- **EX025 — Qualitative to quantitative.** Turn interview statement "clearing the cache fixed it" into a testable log query. Rubric: 3 = query uses series-level outcome.

### Chapter synthesis

An effect has rivals; each rival predicts a fingerprint; stratification and testbed variation eliminate rivals one by one; and aggregate and stratified results must both be reported.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes and connection

You will (1) write a dissertation proposal with aims, hypotheses and an analysis plan; (2) set pilot success criteria; (3) run a small testbed pilot safely; and (4) revise the protocol on the basis of the pilot. It turns the rivals of Chapter 4 into a plan and prepares data collection in Chapter 6.

### 5.1 Proposal structure

A master's proposal fits in eight to twelve pages: background and gap (Chapters 1–2); aims; hypotheses; design and data (Chapter 3); rivals and how each is addressed (Chapter 4); analysis plan; ethics and data management; timeline and risks. The Fragment Study's aims: (A1) estimate the change in failure rate attributable to offering X25519MLKEM768, by path; (A2) determine in a testbed whether the legacy proxy's failures depend on ClientHello size, on the codepoint, or on both; (A3) recommend a remediation that preserves quantum protection.

### 5.2 Hypotheses

- **H1** — On the legacy-proxy path, failures per 10,000 series rise by at least 10 when the hybrid group is offered, relative to the concurrent control cohort; on the direct path the rise is below 2.
- **H2** — In the testbed, proxy failures occur when and only when the ClientHello spans more than one TCP segment, independent of codepoint.
- **H3** — After the proxy's firmware update or a bypass for TLS 1.3 inspection, the proxy-path excess disappears (difference below 2 per 10,000).

H2 is the decisive mechanism test; if failures also occur with a one-segment hello carrying the codepoint, H2 is rejected in favour of rival 3.

### 5.3 Pilot criteria and run

A two-week pilot on 2,000 synthetic series per cohort plus a testbed copy of the proxy (an isolated lab instance, never the production device) tests whether the pipeline works. Criteria: minimization verified on 100 records by a second person; series construction matches manual reconstruction on 50 cases; testbed can produce one-segment and two-segment hellos with the same codepoint by adjusting padding; coders reach κ ≥ 0.75 on 40 failure logs. The synthetic pilot meets all but the series criterion: 6 of 50 cases differed because retries to a different IP address of the same host were treated as new series. The rule is amended to define the series by hostname rather than address.

### 5.4 Worked example: revising after the pilot

The revision memo states the problem (series split by address), its effect (denominators inflated by about 4% on the proxy path), the amendment (hostname-based series with a 10-second window), and a re-check (50 new cases, 50/50 match). It also records a decision *not* to change: the coders asked to add a label for "certificate pinning", but there were only two such cases, so they remain under "cert" with a note. Pilots should produce small, documented changes, not a new study.

Attach the memo to the protocol as a dated amendment.

### 5.5 Common errors and limits

- Hypotheses without a threshold, so that any rise "supports" them.
- Running size or codepoint experiments on the production proxy.
- Treating a pilot as preliminary results to report as findings.
- Amending the protocol silently.

Each error has a guard in the Fragment proposal. H1 and H3 have numeric thresholds per 10,000 series. All size and codepoint experiments use the isolated testbed instance. Pilot data appear only in the methods chapter as checks on the pipeline. Every amendment, such as the hostname-based series rule, is written down with its date and reason.

### Exercises — chapter 5

- **EX026 — Aims to hypotheses.** Write one hypothesis per aim with a threshold. Rubric: 3 = each falsifiable.
- **EX027 — Decisive test.** Explain why H2 is the decisive mechanism test and what result rejects it. Rubric: 3 = links to rival 3.
- **EX028 — Pilot criteria.** Add two pilot criteria of your own. Rubric: 3 = measurable, linked to a risk.
- **EX029 — Revision memo.** Write the memo for a pilot where κ was 0.66. Rubric: 3 = cause, amendment, re-test.
- **EX030 — Risk register.** List five project risks with likelihood, impact and mitigation. Rubric: 3 = includes data access and ethics delay.
- **EX031 — Timeline.** Draft a 24-month Gantt-style list for the dissertation. Rubric: 3 = realistic, includes validation on Fenwick data.

### Chapter synthesis

A proposal turns rivals into falsifiable hypotheses with a decisive mechanism test; a pilot checks the pipeline against stated criteria and produces documented, minimal amendments.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes and connection

You will (1) collect data according to a frozen protocol; (2) code failure logs reliably and measure agreement; (3) estimate a difference-in-differences effect; (4) analyse testbed results; and (5) validate on a second site. It executes the proposal of Chapter 5 and supplies the results Chapter 7 will write up.

### 6.1 Collection

Eight weeks of LK-HS-1 data are collected under the amended protocol: four weeks before and four weeks after the staggered rollout, with half of managed browsers (randomized by device identifier) receiving the hybrid policy first. Freeze the analysis script and record its hash before unblinding the cohort labels.

Keep a collection log noting outages or gaps in the proxy and browser telemetry, with dates, because a missing day in one cohort would bias the comparison. Check before unblinding that the randomization put roughly equal numbers of devices in each cohort and that both used the proxy path in similar proportions.

### 6.2 Coding failures

Each failed series has a log excerpt. Two coders (C1, C2) assign one of four labels — *size* (proxy reset after first segment), *cert* (certificate validation), *timeout*, *other* — using a written codebook, independently.

```python
# Lab 6 (synthetic): agreement between two coders labelling 60 failure logs, then the share of
# failures attributed to "split ClientHello mishandled" after reconciliation.
from collections import Counter
labels = ["size", "cert", "timeout", "other"]
a = ["size"]*30 + ["cert"]*12 + ["timeout"]*10 + ["other"]*8
b = ["size"]*27 + ["timeout"]*3 + ["cert"]*11 + ["other"] + ["timeout"]*9 + ["size"] + ["other"]*8
n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
ca, cb = Counter(a), Counter(b); pe = sum(ca[l]*cb[l] for l in labels) / n**2
print(f"observed agreement {po:.3f}  chance {pe:.3f}  Cohen's kappa {(po-pe)/(1-pe):.3f}")
```

Expected output:

```text
observed agreement 0.917  chance 0.323  Cohen's kappa 0.877
```

A κ of 0.88 indicates strong agreement beyond chance; disagreements (mostly *size* vs *timeout*, because a dropped second segment can look like a timeout) are resolved by discussion and logged.

Keep the codebook with an example log excerpt for each label, especially for the difficult boundary between size and timeout. Coders work from excerpts without cohort labels, so that knowing whether the hybrid group was offered cannot influence the label they choose.

### 6.3 Difference-in-differences

With a concurrent control cohort, the effect is the change in the treated cohort minus the change in the control cohort, estimated separately by path. Synthetic results: proxy path +20.4 per 10,000 (95% CI 15.1–25.8); direct path +0.6 (−1.0 to 2.2). H1 is supported. The control cohort's own small rise (+0.9) captures seasonality, rival 4, which the before/after design alone would have attributed to the hybrid group.

Report the estimate with its interval and the number of series behind each cell, so the calculation can be checked. The direct-path interval includes zero, which supports the second part of H1. The control cohort's rise shows why the concurrent control matters: without it, seasonal change would have been counted as an effect of the hybrid group.

### 6.4 Testbed results

In the isolated testbed copy of the proxy, 200 handshakes per condition: one-segment hello without codepoint 0/200 failures; one-segment hello *with* the hybrid codepoint 0/200; two-segment hello without the codepoint (padding only) 187/200; two-segment hello with codepoint 189/200. Failures track segmentation, not the codepoint: H2 supported, rival 3 rejected for this proxy model. After applying the vendor's firmware update in the testbed, two-segment failures fall to 0/200, which anticipates H3.

The four conditions vary size and codepoint independently, which is what lets the testbed separate the two rivals the logs could not. Report the testbed's firmware versions before and after the update and the padding used for each condition, so another lab can reproduce the result with the same proxy model.

### 6.5 Validation on Fenwick College

Fenwick (synthetic) has a different proxy vendor. Applying the frozen analysis: proxy-path excess +1.2 per 10,000 (−0.8 to 3.2) — no meaningful effect. The mechanism is product-specific; the dissertation must say "the legacy proxy model at Larkspur", not "inspecting proxies". A null result at the second site is a finding about scope, not a failure of the study.

Freeze the analysis script before opening Fenwick data, as for Larkspur, and record its hash. Report Fenwick's interval as well as its estimate: it includes zero and excludes an effect as large as Larkspur's. Recording the proxy vendor and version at Fenwick lets readers see which products the null result covers.

### 6.6 Common errors and limits

- Unblinding cohort labels before freezing the script.
- Treating κ as a pass/fail without examining which categories disagree.
- Generalizing a product-specific defect to a category of products.
- Synthetic numbers here illustrate methods; they are not measurements of any product.

Each error has a guard in this chapter: a script hash recorded before unblinding, a look at which labels disagreed rather than a κ threshold alone, the Fenwick null result used to limit the claim to one proxy model, and a clear statement that the numbers are synthetic.

### Exercises — chapter 6

- **EX032 — Freeze record.** Write the freeze record (what, hash, witness, date). Rubric: 3 = verifiable.
- **EX033 — Kappa interpretation.** Recompute Lab 6 after changing three *size* labels in coder B to *timeout*; interpret. Rubric: 3 = correct κ and comment on which confusion matters.
- **EX034 — DiD by hand.** Treated proxy path 5.0→26.0, control proxy path 5.1→5.7 per 10,000: compute the DiD. Rubric: 3 = 20.4 and explanation.
- **EX035 — Testbed table.** Explain how the four testbed conditions discriminate between rivals 1 and 3. Rubric: 3 = correct logic.
- **EX036 — Scope from validation.** Write the scope sentence implied by the Fenwick null result. Rubric: 3 = product-specific claim, no overgeneralization.
- **EX037 — Threats.** List three threats to the DiD's parallel-trends assumption here. Rubric: 3 = specific to the setting.

### Chapter synthesis

Frozen scripts, double coding with κ, a difference-in-differences estimate by path, a testbed that varies size and codepoint independently, and validation at a second site turn a correlation into a scoped causal account.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes and connection

You will (1) structure a dissertation so that each chapter answers a question; (2) write results that separate estimate, uncertainty and interpretation; (3) write limitations with direction and consequence; and (4) make recommendations proportionate to evidence. It turns Chapter 6's results into a document examined in Chapter 8.

### 7.1 Structure

Introduction (question, why it matters, contribution); background (quantum threat, ML-KEM, hybrids, middlebox ossification); method (design, data, minimization, analysis plan with amendments); results (rates, DiD, coding, testbed, validation); discussion (mechanism, scope, recommendations); limitations; conclusion. Each chapter should open with the question it answers and close with what the next chapter needs.

Draft the results chapter first, then the methods that produced them, and write the introduction last, so it does not promise more than was delivered. Check that each chapter's opening question is answered by its last paragraph. The discussion should connect testbed and log evidence explicitly rather than presenting them separately.

### 7.2 Writing results

Separate three layers in every results paragraph. *Estimate*: "proxy-path failures rose by 20.4 per 10,000 series relative to control." *Uncertainty*: "95% CI 15.1–25.8; coding κ = 0.88." *Interpretation*: "consistent with the size mechanism, which the testbed isolates." Never put interpretation in the estimate sentence. Report the null result at Fenwick in the results chapter, not in a footnote.

Apply the same pattern to the testbed and to Fenwick: estimate, uncertainty, interpretation in separate sentences. Generate the numbers in each sentence from the analysis scripts, so that a revision of the data cannot leave stale figures in the text.

### 7.3 Limitations with direction

- *Only managed browsers were observed* → unmanaged devices on the guest network are excluded; the effect for them is unknown.
- *Testbed proxy is the same model but a lab instance* → configuration differences could make the production effect larger or smaller.
- *Eight weeks* → rare destinations may be under-represented, likely underestimating failures for unusual servers.
- *Synthetic data in this teaching book* → no claim about real products.

Add a column for magnitude where it can be estimated, and update the table if later evidence settles a direction. Unmanaged devices could be studied in a follow-up if the network team agrees, which would turn an unknown into a measured result.

### 7.4 Recommendations

Proportionate recommendation: update the legacy proxy's firmware (validated in testbed) and monitor proxy-path failures; do not roll back the hybrid group for the direct path, where no effect was found; ask the proxy vendor to confirm the fix in release notes. Disproportionate recommendation, to avoid: "inspecting proxies are incompatible with post-quantum cryptography".

Write each recommendation with its owner and the evidence that supports it. The firmware update needs production monitoring after rollout, because the testbed showed the fix only in a lab instance. If proxy-path failures do not fall after the update, the recommendation is revisited.

### 7.5 Worked example: abstract

"Enabling the post-quantum/traditional hybrid TLS group X25519MLKEM768 at a synthetic university increased failed handshakes on a legacy inspecting-proxy path by 20.4 per 10,000 connection series (95% CI 15.1–25.8) relative to a concurrent control, with no meaningful change on the direct path. Testbed experiments showed failures occurred only when the ClientHello spanned two TCP segments, independent of the new codepoint, and stopped after a firmware update. A second site with a different proxy showed no effect. Repairing the specific device preserves quantum protection; rollback is unnecessary."

### 7.6 Common errors and limits

- Interpretation mixed into estimates.
- Limitations listed without direction.
- Recommendations broader than the product and site studied.

Each error has a guard in this dissertation: three-layer results sentences, a limitations list where each item names its direction, and recommendations limited to the legacy proxy model at Larkspur. Read the abstract once more against the results tables before submission.  Ask a peer to mark any sentence that mixes estimate and interpretation, any limitation without a direction, and any recommendation that names a category of products instead of the device studied.

### Exercises — chapter 7

- **EX038 — Three layers.** Rewrite a paragraph that mixes estimate and interpretation. Rubric: 3 = layers separated.
- **EX039 — Limitation directions.** Add two limitations with directions. Rubric: 3 = directions argued.
- **EX040 — Proportionate recommendation.** Write recommendations for a site where the testbed showed codepoint-triggered failures instead. Rubric: 3 = matches mechanism.
- **EX041 — Abstract critique.** Identify any overclaim in the 7.5 abstract. Rubric: 3 = notes synthetic status and single-model scope.
- **EX042 — Chapter openings.** Write the first two sentences of each dissertation chapter. Rubric: 3 = each poses its question.
- **EX043 — Null result paragraph.** Write the Fenwick results paragraph. Rubric: 3 = reports CI and scope implication.

### Chapter synthesis

A dissertation answers its question chapter by chapter, separates estimates from interpretation, gives limitations a direction, reports null results prominently and recommends no more than the evidence supports.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes and connection

You will (1) prepare a reproducibility package an independent reviewer can run; (2) anticipate examiner questions; (3) handle disclosure of a product defect responsibly; and (4) present findings to operators. It closes the dissertation cycle and leads to the worked-answer appendix.

### 8.1 Reproducibility package

Include the minimized dataset (or a synthetic surrogate if the university cannot release it), the frozen scripts with hashes, the codebook and coding sheets, the testbed configuration (without vendor-confidential firmware), and a README explaining how to regenerate every table. Ask a peer to run it cold and log every point where they got stuck.

Test the package on a clean machine with only the README to guide the run.  Record the versions of Python and of each script, and note how long the full run takes, so a reviewer can plan time.

### 8.2 Examiner questions

- *Why should randomization by device identifier be trusted?* Show balance tables for path use and browser version.
- *Could the browser fall back to a classical-only hello after failure and hide the effect?* Yes; the series-level outcome counts a series as failed only if no attempt succeeded, and a secondary analysis reports first-attempt failures.
- *Is the effect about post-quantum cryptography?* Only indirectly: the trigger is message size, which ML-KEM increases; any large ClientHello would do the same, as the padding-only condition shows.
- *What would change your recommendation?* Evidence of codepoint-triggered failures elsewhere, or a vendor fix that fails in production.

### 8.3 Disclosure

The proxy defect was found in an isolated testbed. Before publication, report it to the vendor with reproduction details (padding sizes, segment boundaries, firmware version), give a reasonable window, and inform Larkspur's network team. Publish the class of defect — mishandling of multi-segment ClientHello — rather than steps for evading the proxy's inspection.

Record the date of each step in the disclosure, from first contact with the vendor to publication. If the vendor confirms the fix in its release notes, cite them in the dissertation. Larkspur's network team should hear about the defect before any public presentation of the results.

### 8.4 Operator briefing

For Larkspur's network operations (synthetic): "Turning on quantum-resistant key exchange made some connections through the old inspection proxy fail, because the first message became too large for one packet and the proxy mishandled it. A firmware update fixes this in our lab. Keep the protection on; update the proxy; watch the failure dashboard for the hospital wing."

Test the briefing with one operator who has not seen the study. If they cannot say what to do on Monday, simplify it. Keep the technical detail in an appendix for engineers who ask.

### 8.5 Common errors and limits

- Packages that cannot run without the author.
- Answering "is it PQC's fault?" with yes or no instead of the mechanism.
- Publishing a defect before the vendor and owner are informed.

Each error has a guard: a package tested cold by a peer, an answer to the PQC question that explains message size and the padding-only result, and a disclosure timeline with the vendor and Larkspur's network team agreed before publication. Check each before the defense date.  Rehearse the answers aloud once.

### Exercises — chapter 8

- **EX044 — Package README.** Write the README for the reproducibility package. Rubric: 3 = a stranger could regenerate Table 1.
- **EX045 — Cold run.** List five likely stumbling points for a peer running the package. Rubric: 3 = specific.
- **EX046 — Balance table.** Describe the balance table that answers the randomization question. Rubric: 3 = variables relevant to rivals.
- **EX047 — Fallback question.** Answer the fallback question in 120 words. Rubric: 3 = distinguishes series and first-attempt outcomes.
- **EX048 — Disclosure email.** Draft the vendor disclosure (no exploit steps). Rubric: 3 = reproducible, scoped, window stated.
- **EX049 — Operator brief.** Rewrite 8.4 for the university's executive. Rubric: 3 = decision-focused, no jargon.
- **EX050 — Defense reflection.** Name the weakest part of the Fragment Study and how a future study would fix it. Rubric: 3 = honest and actionable.

### Chapter synthesis

A defense succeeds when an outsider can rerun the work, hard questions are answered with mechanisms rather than slogans, defects are disclosed before publication and operators receive a clear decision.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for self-assessment; any answer meeting the rubric scores equally. Synthetic numbers come from the labs.

**EX001.** Intervention: hybrid group enabled; outcome: Wi-Fi sessions fail; population: library users; implied cause: PQC. Rival: a captive-portal or access-point firmware change the same week.

**EX002.** Descriptive: did VPN connection failures change after enabling hybrid IKEv2 key exchange? Comparative: did they change more for remote than on-campus users? Explanatory: how much of the change is attributable to IKE fragmentation handling, and on which gateways?

**EX003.** Client share 97 + 1,568 = 1,665 bytes; server share 97 + 1,568 = 1,665 bytes (ML-KEM-1024 ciphertext is also 1,568 bytes; FIPS 203; RFC 10024).

**EX004.** A good answer argues each FINER element and admits a weakness, e.g. feasibility depends on log access.

**EX005.** Three databases (RFC Editor, IACR ePrint, ACM DL), exact strings, dates and hit counts.

**EX006.** E.g. RFC 9794 (terminology; standard; no deployment data) and SP 800-227 (KEM usage; standard; not TLS-specific).

**EX007.** "No published study attributes post-hybrid handshake failures within one organization to message size versus competing causes with a concurrent control."

**EX008.** Recorded key exchanges can be decrypted once a CRQC exists, so confidentiality of today's traffic depends on today's key exchange; forged signatures later cannot alter past sessions. Signatures are urgent for long-lived roots of trust and firmware that must be verifiable for decades.

**EX009.** ML-KEM-512 (category 1; 800 B key, 768 B ciphertext), -768 (category 3; 1,184 / 1,088), -1024 (category 5; 1,568 / 1,568). Shared secret 32 B.

**EX010.** Both secrets enter the TLS key schedule; recovering the session key requires both inputs, assuming the KDF (HKDF) behaves as a good extractor, so breaking one component alone yields nothing useful.

**EX011.** For long-lived static keys with infrequent transfers, Classic McEliece's conservative code-based assumption and small ciphertexts can justify its large public key; alternatively ML-KEM with HQC as a later backup. The answer must weigh key size against assumption diversity.

**EX012.** 240% lacks a base rate; weeks differ and a browser update intervenes; retries inflate attempts; no path stratification.

**EX013.** 4.5 × 3.4 = 15.3 per 10,000 — an absolute increase of about 10.8 per 10,000 series, small in aggregate but concentrated by path.

**EX014.** Before/after: cheap, confounded. Quasi-experiment: concurrent control, needs staggered rollout. Testbed: isolates mechanism, lacks prevalence. Combining the latter two covers each other's threats.

**EX015.** Retries add attempts; if failures trigger retries, both numerator and denominator rise and per-attempt rates can mislead in either direction; series-level units remove the dependence.

**EX016.** Keyed hashing of client addresses with monthly rotation, destination categories plus salted hash, no payload, on-premises storage, limited retention, named access, ethics approval.

**EX017.** 9/20,000 → 4.5 per 10,000, Wilson 95% CI about 2.4–8.6 per 10,000.

**EX018.** Base 300: all fit or not as before (x25519 556→336 B, one segment). Base 1,300: x25519-only hello is ~1,336 B, still one segment; it needs two only when the base exceeds about 1,424 B. Real sizes depend on extensions, so measure.

**EX019.** Code version and hash; data dictionary; minimized dataset and checksum; browser policy and date; cohort assignment rule; series definition; codebook; testbed configuration.

**EX020.** Size → proxy path only, segment-boundary dependent; update → both paths; codepoint → failures with one-segment hello; seasonality → control rises too; reporting → tickets rise without logged failures.

**EX021.** E.g. DNS resolver change routing hospital traffic through the proxy more often → path mix shifts; check path share over time.

**EX022.** Guest path 3.0→3.5 per 10,000 (+0.5): no meaningful change, consistent with the size mechanism being proxy-specific.

**EX023.** Stratum A (proxy) 10/1,000 → 30/1,000 with most hybrid-period traffic moving to stratum B (direct) 1/10,000 → 2/10,000; aggregate can fall because the mix shifts toward the low-failure stratum while both rates rise.

**EX024.** 2×2 in the isolated testbed: {one, two segments} × {codepoint present, absent}, using padding to control size.

**EX025.** "Share of failed first attempts to a host followed within 10 s by a successful attempt from the same client without the hybrid share."

**EX026.** As H1–H3 in 5.2, each with a numeric threshold.

**EX027.** It varies size and codepoint independently; failures with a one-segment hello carrying the codepoint would reject H2 in favour of rival 3.

**EX028.** E.g. testbed packet captures confirm segmentation in ≥ 95% of padded trials; pipeline processes one day of logs in under one hour.

**EX029.** Cause (codebook ambiguity size vs timeout), amendment (decision rule: proxy RST after first segment = size), re-test on 40 new logs, proceed if κ ≥ 0.75.

**EX030.** Data access withdrawn; ethics delay; vendor refuses testbed licence; rollout schedule changes; coder unavailability — each with mitigation.

**EX031.** Months 1–4 search and proposal; 5–6 ethics and pilot; 7–12 collection; 13–16 analysis; 17–18 Fenwick validation; 19–22 writing; 23–24 review and defense.

**EX032.** Script file, SHA-256, witness (supervisor), date, location of record.

**EX033.** κ falls to 0.808 (observed agreement 0.867); the size/timeout confusion matters most because it bears on the mechanism.

**EX034.** (26.0 − 5.0) − (5.7 − 5.1) = 21.0 − 0.6 = 20.4 per 10,000.

**EX035.** Failures with two segments regardless of codepoint and none with one segment plus codepoint support size and reject codepoint.

**EX036.** "The effect was observed for one legacy proxy model at Larkspur; a different vendor's proxy at Fenwick showed none."

**EX037.** Hospital-wing traffic growth at term start; proxy rule changes; differential browser update timing between cohorts.

**EX038.** Estimate sentence, uncertainty sentence, interpretation sentence — separated.

**EX039.** Excluding unmanaged devices (unknown direction); short window (likely underestimates rare-destination failures).

**EX040.** Request vendor support for the new codepoint, temporarily bypass inspection for TLS 1.3 to known destinations, and keep the hybrid group on unaffected paths.

**EX041.** It should state that data are synthetic (in this book) and that the effect concerns one proxy model; "rollback is unnecessary" holds only for Larkspur.

**EX042.** One question-posing opening per chapter.

**EX043.** "At Fenwick, the proxy-path excess was +1.2 per 10,000 (95% CI −0.8 to 3.2): no meaningful effect, indicating the Larkspur defect is product-specific."

**EX044.** Steps, environment, data checksum, one command per table.

**EX045.** Missing dependencies, unexplained hashing keys, path labels, testbed licence, undocumented date ranges.

**EX046.** Cohort shares of path, browser version, device type, campus building.

**EX047.** A browser fallback could make a series succeed after failure; the primary outcome counts series failures, and a secondary analysis reports first-attempt failures to expose hidden fallback.

**EX048.** Product, firmware version, observed behaviour, testbed method, 90-day window, contact; no evasion steps.

**EX049.** Decision: approve proxy update; keep protection on; expected outcome and monitoring.

**EX050.** E.g. only managed browsers observed — a future study adds guest-network sampling with consent and minimization.

<a id="references"></a>

## References

Links checked 12 October 2026.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Chromium Blog (2023). Protecting Chrome Traffic with Hybrid Kyber KEM. <https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html>
- Driscoll, F., Parsons, M., and Hale, B. (2025). Terminology for Post-Quantum Traditional Hybrid Schemes. RFC 9794. <https://www.rfc-editor.org/rfc/rfc9794.html>
- IANA. TLS Supported Groups registry. <https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml>
- Kwiatkowski, K., Kampanakis, P., Westerbaan, B., and Stebila, D. (2026). Post-Quantum Traditional (PQ/T) Hybrid Key Agreement Mechanisms for TLS 1.3. RFC 10024. <https://www.rfc-editor.org/rfc/rfc10024.html>
- NIST (2024). FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard. <https://doi.org/10.6028/NIST.FIPS.203>
- NIST (2024). FIPS 204, Module-Lattice-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.204>
- NIST (2024). FIPS 205, Stateless Hash-Based Digital Signature Standard. <https://doi.org/10.6028/NIST.FIPS.205>
- NIST (2025). IR 8545, Status Report on the Fourth Round of the NIST PQC Standardization Process. <https://doi.org/10.6028/NIST.IR.8545>
- NIST (2025). SP 800-227, Recommendations for Key-Encapsulation Mechanisms. <https://doi.org/10.6028/NIST.SP.800-227>
- Regev, O. (2009). On lattices, learning with errors, random linear codes, and cryptography. *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Rescorla, E. (2018). The Transport Layer Security (TLS) Protocol Version 1.3. RFC 8446. <https://www.rfc-editor.org/rfc/rfc8446.html>
- Shor, P. W. (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM J. Computing* 26(5). <https://doi.org/10.1137/S0097539795293172>
- tldr.fail. Community page on servers that mishandle large or split TLS ClientHello messages. <https://tldr.fail/>
