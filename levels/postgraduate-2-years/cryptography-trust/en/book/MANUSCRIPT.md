# Cryptography and Trust Services: Postgraduate Course

- Language: English (`en`); course 146, Postgraduate course (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: experienced practitioners leading organisation-scale cryptographic decisions.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: labs summarise inventories, scores, sizes and evaluation data; they implement no cryptography. Production systems use vetted libraries, HSMs and supplier products; never roll your own cryptography. All people, organisations and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one security architect leading a two-year cryptographic modernisation programme at a logistics company: decision framing, current practice and inventory, post-quantum evidence, risk and ethics, key-management alternatives, a controlled evaluation, organisational integration, difficult cases, leadership and assurance, research critique, an applied legacy-retirement project and final transfer. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leila Moradi** | Security architect and postgraduate student | Invented |
| **Prof. Anika Rao** | Programme director | Invented |
| **Westbrook School of Security** | Fictional school | Invented |
| **Corvane Logistics** | Fictional shipping and freight company | Invented |

### Core sources

Katz and Lindell (3rd ed.); Boneh and Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); NIST [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5), [SP 800-131A](https://doi.org/10.6028/NIST.SP.800-131Ar2), [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205); [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame an organisation-scale cryptographic decision; (2) separate facts, assumptions and values in a decision record; (3) choose decision rules that survive scrutiny by executives and auditors.

### 1.1 The case

Leila Moradi is a security architect at the fictional Corvane Logistics, a shipping and freight company with port terminals, a truck fleet, a finance division and an ageing electronic data interchange platform. She studies part-time in the postgraduate programme at the fictional Westbrook School of Security under Prof. Anika Rao. Corvane's board has asked for a plan to modernise cryptography across the company within two years: retire legacy TLS, consolidate key management and prepare for post-quantum migration. Every system, figure and person in this book is synthetic. The decision is not which cipher is strongest but how to spend limited money and engineering time across many systems.

### 1.2 Facts, assumptions and values

Prof. Rao asks students to split every decision into three columns. Facts are verifiable, such as the number of endpoints still accepting TLS 1.0 or the date a supplier contract ends. Assumptions are beliefs that could be wrong, such as how quickly large quantum computers will arrive or how long a migration will take. Values are preferences the organisation must own, such as how much outage risk it tolerates during a change. Leila finds that her first draft mixed all three, presenting an assumption about quantum timelines as if it were fact. Separating them lets executives debate values openly and lets engineers test assumptions.

### 1.3 Decision rules

Leila compares decision rules. Minimising the worst case suits catastrophic, irreversible risks such as losing the firmware root key. Maximising expected value suits frequent, measurable risks such as certificate expiry. Satisficing, accepting the first option that meets every requirement, suits decisions where analysis costs more than small improvements. She chooses rules per decision, documents why and records what new evidence would change the choice. Katz and Lindell's emphasis on explicit threat models carries over to management: a decision without stated assumptions cannot be evaluated later, and auditors will ask what Corvane believed when it chose.

### 1.4 Writing the decision record

Leila drafts the programme's first decision record, adopting a company-wide TLS baseline. It states the decision, the facts (inventory counts), the assumptions (that most clients support TLS 1.2), the values (acceptable disruption for legacy partners), alternatives considered, the rule used (satisficing against a published baseline) and review triggers. She links each claim to its source, including RFC 8446 for TLS 1.3 behaviour and NIST SP 800-52 Rev. 2, the TLS guideline referenced in Corvane's policy. Prof. Rao marks the record strong because a newcomer could reconstruct the reasoning in five minutes without asking Leila.

### Worked example

Leila separates facts, assumptions and values for the modernisation programme, picks satisficing for the TLS baseline and minimax for root keys, and writes a decision record with review triggers.

> **Synthetic case.** Corvane, Westbrook and all figures are invented; RFC 8446 is real.

### Errors and limits

Decision frameworks cannot replace judgement; they make judgement visible. Assumptions presented as facts are the most common flaw in security business cases.

### Exercises

- **EX001 — Programme scope.** What three goals did Corvane's board set for the programme? *Rubric:* 3 = retire legacy TLS, consolidate key management, prepare post-quantum migration;; 2 = two;; 1 = one;; 0 = none.
- **EX002 — Three columns.** Distinguish a fact, an assumption and a value with Corvane examples. *Rubric:* 3 = fact: endpoints on TLS 1.0; assumption: quantum timeline; value: tolerated outage risk;; 2 = two correct;; 1 = confused;; 0 = none.
- **EX003 — Matching rules.** Which decision rule suits root-key loss and which suits certificate expiry? *Rubric:* 3 = minimax for catastrophic root loss; expected value for frequent expiry;; 2 = one;; 1 = reversed;; 0 = none.
- **EX004 — Draft flaw.** What flaw did Leila find in her first draft? *Rubric:* 3 = an assumption about quantum timelines presented as fact;; 2 = mixing;; 1 = none;; 0 = none.
- **EX005 — Record test.** Why did Prof. Rao rate the record strong? *Rubric:* 3 = a newcomer could reconstruct the reasoning in five minutes;; 2 = clarity;; 1 = length;; 0 = none.

### Synthesis

Organisation-scale cryptographic decisions improve when facts, assumptions and values are separated and each decision uses an explicit, recorded rule.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Cryptography and trust services: current practice

### Learning outcomes

You will (1) survey current cryptographic practice from standards; (2) build an endpoint inventory and read it; (3) identify where an organisation lags current practice.

### 2.1 What current practice means

Current practice is set by standards and widely deployed defaults, not by vendor marketing. For transport security it is TLS 1.3 from RFC 8446, with TLS 1.2 still acceptable when configured carefully, and older versions retired. For key exchange it is ephemeral elliptic-curve Diffie-Hellman such as X25519 from RFC 7748; for signatures, ECDSA or EdDSA under FIPS 186-5; for symmetric encryption, AES-GCM under SP 800-38D. Key management follows SP 800-57 Part 1, and algorithm transitions follow SP 800-131A. Leila writes a one-page summary of these references for Corvane's engineers so that later debates start from shared ground.

### Lab — Endpoint inventory

```python
"""Summarise a synthetic TLS endpoint inventory for an organisation-scale decision."""
from collections import Counter
# (business unit, highest TLS version offered, accepts legacy <=1.1?, cert key type)
EP = ([("ports", "1.3", False, "ecdsa")] * 46 + [("ports", "1.2", True, "rsa2048")] * 9 +
      [("fleet", "1.3", False, "ecdsa")] * 38 + [("fleet", "1.2", False, "rsa2048")] * 21 +
      [("finance", "1.3", False, "rsa3072")] * 30 + [("finance", "1.2", True, "rsa2048")] * 4 +
      [("legacy-edi", "1.2", True, "rsa2048")] * 12)

def main():
    n = len(EP)
    print(f"endpoints {n}")
    for v, c in sorted(Counter(e[1] for e in EP).items()):
        print(f"  max TLS {v}: {c} ({100 * c / n:.1f}%)")
    leg = Counter(e[0] for e in EP if e[2])
    print("legacy-accepting by unit:", dict(leg), "total", sum(leg.values()))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_inventory.py`. Verified output:

```text
endpoints 160
  max TLS 1.2: 46 (28.8%)
  max TLS 1.3: 114 (71.2%)
legacy-accepting by unit: {'ports': 9, 'finance': 4, 'legacy-edi': 12} total 25
```

### 2.2 Reading the inventory

Corvane's synthetic inventory lists 160 TLS endpoints. Of these, 114 (71.2 percent) offer TLS 1.3 and 46 (28.8 percent) top out at TLS 1.2. Twenty-five endpoints still accept TLS 1.1 or older: nine in ports, four in finance and all twelve on the legacy EDI platform. Leila notes that the fleet unit has many TLS 1.2-only endpoints but none accepting legacy versions, so it is behind but not dangerous, whereas legacy EDI is both behind and exposed. The inventory changes the conversation from "Corvane is insecure" to a specific list of units, counts and owners.

### 2.3 Key types and certificates

The inventory also shows certificate key types: ECDSA on modern endpoints, RSA 3072 in finance and RSA 2048 on older services. RSA 2048 remains acceptable under current NIST guidance for now, but Leila records it as a migration candidate because certificates and keys with long lifetimes will need to move to stronger or post-quantum alternatives. She checks certificate lifetimes and finds that the EDI platform uses certificates valid for two years, renewed by hand, while most other units use automated ninety-day certificates through ACME, RFC 8555. Lifetimes are a proxy for automation maturity.

### 2.4 Where Corvane lags

Leila summarises gaps against current practice: legacy protocol acceptance in three units; manual certificate management on EDI; no central record of which applications use which keys; and no post-quantum readiness assessment. She ranks them by exposure and effort. Legacy acceptance on internet-facing EDI endpoints ranks first because partners connect over the internet. She avoids overstating: none of the gaps implies a known breach, and several have compensating controls such as network restrictions. Presenting gaps with context keeps executives focused rather than alarmed.

### Worked example

Leila reads a 160-endpoint inventory, finds 25 legacy-accepting endpoints concentrated in EDI, ports and finance, and ranks four gaps with context.

> **Synthetic case.** The inventory is invented; the cited standards are real.

### Errors and limits

Inventories from scanning miss internal-only services and client-side settings. RSA 2048 is acceptable today but is not a long-term choice.

### Exercises

- **EX006 — Current baselines.** Name the standards Leila cites for TLS, key exchange and AEAD. *Rubric:* 3 = RFC 8446, RFC 7748, SP 800-38D;; 2 = two;; 1 = one;; 0 = none.
- **EX007 — Inventory split.** What share of endpoints offer TLS 1.3? *Rubric:* 3 = 114 of 160, 71.2 percent;; 2 = count;; 1 = wrong;; 0 = none.
- **EX008 — Legacy by unit.** How are the 25 legacy-accepting endpoints distributed? *Rubric:* 3 = ports 9, finance 4, legacy-edi 12;; 2 = two units;; 1 = total only;; 0 = none.
- **EX009 — Lifetime proxy.** Why does Leila treat certificate lifetime as a proxy? *Rubric:* 3 = short lifetimes indicate automated management; EDI two-year manual certificates show low maturity;; 2 = automation;; 1 = none;; 0 = none.
- **EX010 — Top gap.** Which gap ranks first and why? *Rubric:* 3 = legacy protocol acceptance on internet-facing EDI, since partners connect over the internet;; 2 = gap;; 1 = other;; 0 = none.

### Synthesis

Current practice is defined by standards; an inventory translates it into specific, owned gaps ranked by exposure.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Cryptography and trust services: specialist evidence

### Learning outcomes

You will (1) gather specialist evidence on post-quantum readiness; (2) read standards for sizes and performance implications; (3) judge evidence quality for decisions.

### 3.1 Specialist questions

Post-quantum migration raises questions general staff cannot answer: which algorithms are standardised, how large their keys and signatures are, and what that means for protocols and devices. NIST published FIPS 203 (ML-KEM) for key establishment, FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) for signatures. Leila gathers evidence directly from these documents rather than from summaries, and records which parameter sets Corvane would likely use. She also notes that protocol integration, such as hybrid key exchange in TLS, is defined in IETF work that is still maturing, so dates and details must be rechecked.

### Lab — Post-quantum sizes

```python
"""Public-key and signature/ciphertext sizes in bytes, from RFC 7748/8032 and FIPS 203/204/205."""
ROWS = [("X25519 (RFC 7748)", "key share", 32, 32), ("ML-KEM-768 (FIPS 203)", "encaps key / ciphertext", 1184, 1088),
        ("Ed25519 (RFC 8032)", "public key / signature", 32, 64), ("ML-DSA-65 (FIPS 204)", "public key / signature", 1952, 3309),
        ("SLH-DSA-SHA2-128s (FIPS 205)", "public key / signature", 32, 7856)]

def main():
    for name, what, a, b in ROWS:
        print(f"{name:<29} {what:<24} {a:>5} / {b:>5}")
    print(f"ML-DSA-65 signature is {3309 / 64:.0f}x an Ed25519 signature")
    print(f"hybrid X25519+ML-KEM-768 client share: {32 + 1184} bytes")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_sizes.py`. Verified output:

```text
X25519 (RFC 7748)             key share                   32 /    32
ML-KEM-768 (FIPS 203)         encaps key / ciphertext   1184 /  1088
Ed25519 (RFC 8032)            public key / signature      32 /    64
ML-DSA-65 (FIPS 204)          public key / signature    1952 /  3309
SLH-DSA-SHA2-128s (FIPS 205)  public key / signature      32 /  7856
ML-DSA-65 signature is 52x an Ed25519 signature
hybrid X25519+ML-KEM-768 client share: 1216 bytes
```

### 3.2 Reading the sizes

The lab tabulates sizes from the standards. An X25519 key share is 32 bytes; an ML-KEM-768 encapsulation key is 1,184 bytes and its ciphertext 1,088. An Ed25519 signature is 64 bytes; an ML-DSA-65 signature is 3,309 bytes, about 52 times larger, and its public key 1,952 bytes. SLH-DSA-SHA2-128s keeps a 32-byte public key but produces 7,856-byte signatures. A hybrid TLS client share combining X25519 and ML-KEM-768 is 1,216 bytes. Leila concludes that bandwidth on modern networks is rarely the problem; constrained devices, certificate chains and protocols with fixed message limits are.

### 3.3 Where sizes matter at Corvane

Leila maps sizes onto Corvane's systems. Office and cloud traffic can absorb larger handshakes. Truck telematics units send small messages over expensive cellular links and verify firmware signatures with limited memory, so ML-DSA signatures and certificate chains need testing. Port terminal controllers run vendor firmware with long replacement cycles. The EDI platform's protocol has message-size limits that may break with large signatures. She classifies systems as ready, needing testing or blocked by vendors, and asks vendors for written migration plans rather than verbal reassurance.

### 3.4 Judging evidence quality

Leila grades evidence. Standards are authoritative on algorithms and sizes but say nothing about Corvane's vendors. Vendor statements are relevant but self-interested. Laboratory measurements on Corvane's own devices are strongest for local decisions but expensive. Public benchmarks may use different hardware. She records grades in her evidence table and uses the lowest-grade link in any argument to describe its overall strength. Prof. Rao notes that executives often treat vendor slides as facts, and that a postgraduate practitioner's value lies in showing where evidence is thin.

### Worked example

Leila reads FIPS 203/204/205 sizes, finds ML-DSA-65 signatures 52 times larger than Ed25519, and classifies Corvane systems as ready, needing tests or vendor-blocked.

> **Synthetic case.** Corvane's systems are invented; sizes come from RFC 7748, RFC 8032 and FIPS 203–205.

### Errors and limits

Sizes alone do not determine performance; computation and memory matter too. IETF integration details change, so recheck before committing.

### Exercises

- **EX011 — Standards map.** Which FIPS standards cover ML-KEM, ML-DSA and SLH-DSA? *Rubric:* 3 = FIPS 203, 204, 205 respectively;; 2 = two;; 1 = wrong;; 0 = none.
- **EX012 — Size ratio.** How much larger is an ML-DSA-65 signature than Ed25519? *Rubric:* 3 = 3,309 vs 64 bytes, about 52 times;; 2 = ratio;; 1 = wrong;; 0 = none.
- **EX013 — Hybrid share.** What is the size of a hybrid X25519 plus ML-KEM-768 client share? *Rubric:* 3 = 1,216 bytes;; 2 = close;; 1 = wrong;; 0 = none.
- **EX014 — Constrained systems.** Which Corvane systems are most affected by size and why? *Rubric:* 3 = telematics (cellular, memory), port controllers (vendor cycles), EDI (message limits);; 2 = two;; 1 = none;; 0 = none.
- **EX015 — Evidence strength.** How does Leila describe an argument's overall strength? *Rubric:* 3 = by its lowest-grade evidence link;; 2 = weakest link;; 1 = average;; 0 = none.

### Synthesis

Specialist evidence from standards and local testing, graded honestly, shows where post-quantum migration will hurt and where it will not.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) assess risk for long-lived confidential data; (2) weigh ethical duties to partners and customers; (3) decide on disclosure of cryptographic weaknesses in supplier products.

### 4.1 Long-lived confidentiality

Some Corvane data must stay confidential for decades: customs records, contracts and customer identities. Leila applies a simple test from post-quantum planning literature: if data must remain secret for x years, migration takes y years and a cryptographically relevant quantum computer might appear in z years, then x plus y greater than z signals risk now, because recorded traffic could be decrypted later. She estimates x at fifteen years for contracts and y at three, but treats z as deeply uncertain, presenting scenarios rather than a single date. The test identifies which data flows deserve hybrid key exchange first.

### 4.2 Risk scenarios

Leila writes three scenarios for the board: slow progress, where large quantum computers remain decades away; moderate, around fifteen years; and fast, under ten. For each she shows exposure of recorded EDI and finance traffic, migration cost and residual risk. Rather than predicting, she asks the board to choose a planning scenario that matches its risk appetite. The board chooses moderate with a review every two years. This turns an unknowable date into a governed assumption, consistent with Chapter 1's separation of assumptions from facts.

### 4.3 Ethical duties

Corvane holds data belonging to customers and partners who cannot see its security choices. Leila argues that this creates duties beyond compliance: to protect data proportionately, to tell partners when shared systems are weak and to avoid shifting risk onto those least able to bear it. One example is the legacy EDI platform, where small partners still use old clients; forcing an abrupt cut-off would harm them, while waiting indefinitely exposes everyone. She proposes a supported transition with free updated client software and a firm, published deadline.

### 4.4 Supplier weakness disclosure

During testing, Leila's team finds that a port terminal vendor's controller accepts firmware signed with a deprecated algorithm. She follows Corvane's coordinated disclosure policy: report privately to the vendor, agree a fix timeline, apply compensating controls such as network isolation, and inform other affected customers through the vendor once a fix exists. She does not publish details or test beyond Corvane's authorised lab. The episode becomes a teaching case on balancing transparency with the risk of helping attackers before fixes ship.

### Worked example

Leila applies the x + y > z test to contracts, presents three quantum scenarios for board choice, proposes a supported EDI transition and handles a vendor firmware weakness through coordinated disclosure.

> **Synthetic case.** Scenarios and the vendor case are invented.

### Errors and limits

Quantum timelines are uncertain; scenarios must be revisited. Disclosure without a fix can endanger other customers.

### Exercises

- **EX016 — Planning inequality.** State the x + y > z test and its meaning. *Rubric:* 3 = secrecy years plus migration years exceeding years to a quantum computer signals risk now;; 2 = partial;; 1 = none;; 0 = none.
- **EX017 — Board choice.** Which planning scenario did the board choose, with what review? *Rubric:* 3 = moderate (about fifteen years), reviewed every two years;; 2 = scenario;; 1 = none;; 0 = none.
- **EX018 — EDI ethics.** What transition did Leila propose for small EDI partners? *Rubric:* 3 = supported transition with free updated clients and a firm published deadline;; 2 = partial;; 1 = abrupt cut-off;; 0 = none.
- **EX019 — Vendor flaw.** What weakness did the team find in the port controller? *Rubric:* 3 = accepts firmware signed with a deprecated algorithm;; 2 = weakness;; 1 = none;; 0 = none.
- **EX020 — Disclosure steps.** List the disclosure steps Leila followed. *Rubric:* 3 = private report, agreed fix timeline, compensating controls, vendor informs others after fix;; 2 = three;; 1 = publish;; 0 = none.

### Synthesis

Advanced risk work governs uncertain assumptions through scenarios and treats ethical duties to partners as part of cryptographic decisions.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Cryptography and trust services: design alternatives

### Learning outcomes

You will (1) compare key-management architectures at organisation scale; (2) apply a weighted decision matrix and test its sensitivity; (3) present alternatives without hiding trade-offs.

### 5.1 Three alternatives

Corvane's keys are scattered across application servers, two old HSMs and several cloud accounts. Leila defines three alternatives for consolidation. On-premises HSMs give Corvane full custody but require specialist staff and hardware refreshes. A cloud key management service offers availability and low operational effort, with custody shared under contract. A hybrid keeps root and high-value signing keys in on-premises HSMs while application data keys live in the cloud service, wrapped under keys Corvane controls. Each alternative is described with its trust assumptions, following SP 800-57's emphasis on who can access keys.

### Lab — Weighted decision matrix

```python
"""Weighted decision matrix for key-management options (synthetic scores 1-5)."""
W = {"custody": 0.30, "availability": 0.20, "ops_effort": 0.20, "cost": 0.15, "pq_path": 0.15}
OPT = {"on-prem HSM": {"custody": 5, "availability": 3, "ops_effort": 2, "cost": 2, "pq_path": 3},
       "cloud KMS": {"custody": 3, "availability": 5, "ops_effort": 4, "cost": 4, "pq_path": 4},
       "hybrid (HSM root + cloud KMS)": {"custody": 4, "availability": 4, "ops_effort": 3, "cost": 3, "pq_path": 4}}

def main():
    for name, s in sorted(OPT.items(), key=lambda kv: -sum(W[k] * kv[1][k] for k in W)):
        print(f"{name:<31} {sum(W[k] * s[k] for k in W):.2f}")
    W2 = dict(W, custody=0.45, cost=0.0)
    best = max(OPT, key=lambda o: sum(W2[k] * OPT[o][k] for k in W2))
    print("if custody weight 0.45 and cost 0:", best)

if __name__ == "__main__":
    main()
```

Run with `python3 lab_matrix.py`. Verified output:

```text
cloud KMS                       3.90
hybrid (HSM root + cloud KMS)   3.65
on-prem HSM                     3.25
if custody weight 0.45 and cost 0: hybrid (HSM root + cloud KMS)
```

### 5.2 Reading the matrix

With weights of 0.30 for custody, 0.20 each for availability and operational effort, and 0.15 each for cost and post-quantum path, the cloud service scores 3.90, the hybrid 3.65 and on-premises HSMs 3.25. A sensitivity test raises custody to 0.45 and removes cost, reflecting a board that values control above price; the hybrid then wins. Leila presents both results. The matrix does not decide; it shows that the choice depends mainly on how much the board values custody, which is a value judgement, not an engineering fact.

### 5.3 Hidden trade-offs

Leila lists trade-offs the matrix cannot show. Cloud custody depends on contract terms, regional data laws and the provider's own staff controls. On-premises HSMs concentrate knowledge in a few engineers, creating key-person risk. The hybrid doubles the number of systems to audit and requires careful key wrapping so cloud services never see root keys. She also notes migration effort: moving keys between systems is itself risky and must be done with vendor-supported mechanisms, never by exporting keys in plain form.

### 5.4 Presenting alternatives

Leila's board paper presents all three options with scores, sensitivity results, trade-offs and her recommendation: the hybrid, because Corvane's regulators and customers expect control over signing roots, while cloud services suit high-volume data keys. She states the condition that would reverse it: if the cloud provider offered customer-controlled HSM-backed keys meeting regulator requirements at lower cost. Presenting the runner-up fairly builds trust with the board and protects the recommendation from accusations of bias. The board asks for a cost breakdown before deciding.

### Worked example

Leila's matrix ranks cloud first at 3.90, but a custody-heavy sensitivity test favours the hybrid, which she recommends with an explicit reversal condition.

> **Synthetic case.** Scores and weights are invented; SP 800-57 is real.

### Errors and limits

Weighted matrices hide judgement in weights; always test sensitivity. Key migration must use vendor mechanisms, never plaintext export.

### Exercises

- **EX021 — Hybrid definition.** Describe the hybrid alternative. *Rubric:* 3 = root and high-value signing keys in on-prem HSMs; data keys in cloud KMS wrapped under Corvane-controlled keys;; 2 = partial;; 1 = cloud only;; 0 = none.
- **EX022 — Base scores.** Give the three base scores. *Rubric:* 3 = cloud 3.90, hybrid 3.65, on-prem 3.25;; 2 = two;; 1 = one;; 0 = none.
- **EX023 — Sensitivity result.** What did the sensitivity test show? *Rubric:* 3 = with custody 0.45 and cost 0 the hybrid wins; choice hinges on custody value;; 2 = winner;; 1 = none;; 0 = none.
- **EX024 — Matrix blind spots.** Name two trade-offs the matrix cannot show. *Rubric:* 3 = two of contract/law dependence, key-person risk, double audit scope, migration risk;; 2 = one;; 1 = none;; 0 = none.
- **EX025 — Reversal condition.** What would reverse the recommendation? *Rubric:* 3 = cloud provider offering customer-controlled HSM-backed keys meeting regulators at lower cost;; 2 = condition;; 1 = none;; 0 = none.

### Synthesis

Comparing key-management alternatives with tested weights and explicit trade-offs exposes the value judgements boards must own.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Cryptography and trust services: controlled evaluation

### Learning outcomes

You will (1) design a controlled evaluation of a cryptographic baseline rollout; (2) analyse paired before-and-after data; (3) report effect, uncertainty and threats.

### 6.1 Designing the evaluation

Before rolling the TLS baseline company-wide, Leila evaluates it at eight sites. Each site counts misconfigured endpoints, those accepting legacy protocols, weak cipher suites or expired certificates, using the same scanner profile before and three months after applying the baseline templates and automated certificate renewal. Paired measurement controls for site differences such as size and age. She registers the plan, the outcome definition and the analysis with Prof. Rao before collecting the after data, so that she cannot adjust the outcome definition to flatter the result.

### Lab — Paired evaluation

```python
"""Before/after evaluation of a TLS baseline rollout across 8 synthetic sites, with a sign-flip test."""
import random
BEFORE = [14, 9, 11, 6, 17, 8, 12, 10]   # misconfigured endpoints per site
AFTER = [5, 4, 6, 3, 9, 5, 4, 6]

def main():
    d = [b - a for b, a in zip(BEFORE, AFTER)]
    obs = sum(d) / len(d)
    rng = random.Random(11); n = 20000
    hits = sum(sum(x if rng.random() < 0.5 else -x for x in d) / len(d) >= obs for _ in range(n))
    print(f"mean reduction {obs:.2f} endpoints per site; every site improved: {all(x > 0 for x in d)}")
    print(f"sign-flip p = {hits / n:.4f} (seed 11, {n} draws)")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_eval.py`. Verified output:

```text
mean reduction 5.62 endpoints per site; every site improved: True
sign-flip p = 0.0036 (seed 11, 20000 draws)
```

### 6.2 Reading the results

Every site improves, and the mean reduction is 5.62 misconfigured endpoints per site. A sign-flip test asks how often a mean reduction this large would occur if each site's change were equally likely to be positive or negative; with seed 11 and 20,000 draws the p-value is 0.0036, close to the minimum possible for eight sites, 1/256. Leila reports the absolute counts before and after per site, not only the mean, because a manager in the largest port wants to see their own site's numbers and because skewed sites could otherwise dominate.

### 6.3 Threats to the conclusion

Leila lists threats. Without a control group, other changes during the three months, such as a separate patching campaign, could explain part of the improvement. The scanner sees only reachable endpoints. Staff knew they were being measured. Eight sites are few, and the pilot sites volunteered, so they may be more capable than others. She recommends a staggered rollout for remaining sites, which creates natural comparison groups, and continued measurement after the initial attention fades. She lists each threat with its likely direction of bias.

### 6.4 From evaluation to decision

The evaluation supports rolling out the baseline, with caveats. Leila updates the decision record from Chapter 1 with the evidence, notes the threats and adds a monitoring requirement: the misconfiguration count per site becomes a quarterly metric. She also reports costs: about two engineer-weeks per site, mostly spent on legacy clients. Including costs lets the board compare this programme with others competing for the same budget, which is the real decision context at organisation scale. The board approves the rollout for the remaining sites.

### Worked example

Leila's eight-site paired evaluation shows a mean reduction of 5.62 misconfigured endpoints (sign-flip p = 0.0036), with threats and costs reported and a staggered rollout recommended.

> **Synthetic case.** Site data are invented.

### Errors and limits

Before-and-after designs without controls are vulnerable to concurrent changes. Volunteer sites may not represent the rest.

### Exercises

- **EX026 — Paired design.** Why measure the same sites before and after? *Rubric:* 3 = pairing controls for site differences such as size and age;; 2 = control;; 1 = none;; 0 = none.
- **EX027 — Evaluation numbers.** Report the mean reduction and p-value. *Rubric:* 3 = 5.62 per site, p = 0.0036;; 2 = one;; 1 = wrong;; 0 = none.
- **EX028 — Minimum p.** Why is 0.0036 close to the minimum possible? *Rubric:* 3 = eight sites allow at most 1/256 ≈ 0.0039 when all improve;; 2 = 1/256;; 1 = none;; 0 = none.
- **EX029 — Concurrent change.** Which threat arises from the lack of a control group? *Rubric:* 3 = other changes such as a patching campaign could explain improvement;; 2 = concurrent;; 1 = none;; 0 = none.
- **EX030 — Cost reporting.** Why include the two engineer-weeks per site cost? *Rubric:* 3 = lets the board compare against other programmes competing for budget;; 2 = budget;; 1 = irrelevant;; 0 = none.

### Synthesis

Pre-registered paired evaluations, with threats and costs, turn a promising baseline into evidence for organisation-wide decisions.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Cryptography and trust services: organizational integration

### Learning outcomes

You will (1) embed cryptographic standards into organisational processes; (2) assign ownership across units; (3) integrate with procurement, architecture review and change management.

### 7.1 Standards into processes

A baseline in a document does nothing until processes use it. Leila embeds Corvane's cryptographic standard into four processes: architecture review, where new designs must state algorithms and key ownership; procurement, where suppliers answer a cryptography questionnaire; change management, where TLS and key changes need a rollback plan; and onboarding, where engineers learn the standard and its reasons. She publishes the standard with an approved-algorithms list and retirement dates, following the transition approach of SP 800-131A, and assigns the security architecture team to maintain it.

### 7.2 Ownership across units

Each business unit nominates a cryptography owner responsible for its inventory, renewals and migrations. Leila runs a monthly forum where owners share problems and progress. Ownership resolves a pattern seen in the inventory: certificates and keys with no clear owner were the ones that expired or lingered on deprecated algorithms. She defines a RACI chart: units are responsible for their systems, security architecture is accountable for the standard, operations is consulted on changes and the risk committee is informed quarterly.

### 7.3 Procurement and suppliers

Procurement becomes a lever. New contracts require support for TLS 1.3, documented key management, notification of key compromise within a set time and a post-quantum migration roadmap. Leila provides a scoring guide so procurement staff, who are not cryptographers, can evaluate answers. The first tender using the questionnaire rejects a supplier whose answers revealed hard-coded keys in its product. She notes that procurement cannot fix existing contracts quickly, so renewals become the main opportunity for older suppliers. She also offers procurement staff a short training session on the guide.

### 7.4 Change management

Cryptographic changes can break systems silently, for example a cipher suite removal that disconnects a partner. Leila adds a cryptographic change template: what changes, which clients might fail, how to detect failure, rollback steps and partner notification. Changes to legacy EDI require partner notice weeks in advance. After a change disconnects a small partner unexpectedly, she adds a pre-change client compatibility scan. Integrating cryptography into change management reduces both outages and the temptation to avoid security changes for fear of breaking things.

### Worked example

Leila embeds the standard into architecture review, procurement, change management and onboarding, appoints unit owners with a RACI chart and adds a compatibility scan after a partner disconnection.

> **Synthetic case.** Corvane's processes are invented; SP 800-131A is real.

### Errors and limits

Standards without owners decay. Procurement questionnaires need scoring guidance or answers go unchecked.

### Exercises

- **EX031 — Four processes.** Into which four processes was the standard embedded? *Rubric:* 3 = architecture review, procurement, change management, onboarding;; 2 = three;; 1 = one;; 0 = none.
- **EX032 — Ownership pattern.** What inventory pattern did unit ownership address? *Rubric:* 3 = unowned certificates and keys were those that expired or stayed on deprecated algorithms;; 2 = pattern;; 1 = none;; 0 = none.
- **EX033 — Contract requirements.** List three contract requirements for new suppliers. *Rubric:* 3 = three of TLS 1.3, documented key management, compromise notification, PQ roadmap;; 2 = two;; 1 = one;; 0 = none.
- **EX034 — Tender rejection.** Why was a supplier rejected in the first tender? *Rubric:* 3 = answers revealed hard-coded keys in its product;; 2 = hard-coded keys;; 1 = price;; 0 = none.
- **EX035 — Compatibility scan.** What prompted the pre-change compatibility scan? *Rubric:* 3 = a change unexpectedly disconnected a small partner;; 2 = outage;; 1 = audit;; 0 = none.

### Synthesis

Cryptography becomes organisational practice when standards drive processes, owners exist in every unit and changes are managed for compatibility.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Cryptography and trust services: difficult cases

### Learning outcomes

You will (1) analyse cases where good cryptography conflicts with operations or law; (2) handle lawful-access and inspection requests; (3) resolve conflicts between availability and key protection.

### 8.1 TLS inspection

Corvane's network team wants to decrypt outbound TLS traffic to detect malware, using inspection proxies that re-sign connections with a corporate authority. Leila analyses the trade-off: inspection may catch threats, but it breaks end-to-end guarantees, concentrates a powerful signing key in the proxy and can weaken connections if the proxy's TLS is outdated. She recommends limited inspection for high-risk categories, exemptions for banking, health and partner traffic, strict protection of the proxy key, and regular checks that the proxy itself meets the TLS baseline.

### 8.2 Lawful access requests

A customs authority asks Corvane to provide decrypted shipment records for an investigation. Leila works with legal counsel: the request is valid under applicable law, and Corvane holds the keys for its own data, so it can comply with the specific records requested. She ensures the process follows a documented procedure, with approvals, logging and minimal disclosure. She also notes the contrast with end-to-end encrypted systems, where Corvane would not hold keys, and explains that design choices determine what an organisation can be compelled to provide.

### 8.3 Availability versus protection

A port terminal's HSM fails during a peak period, and operations asks to export signing keys to a standby server without an HSM to restore service quickly. Leila refuses export in plaintext, which would violate the key's protection requirements, and instead activates the documented standby HSM, which takes two hours longer. She records the incident and proposes a second HSM at the site. Difficult cases test whether controls hold under pressure, and decisions made under stress should follow plans agreed in calm.

### 8.4 Learning from difficult cases

Leila writes up each case using the same structure: context, conflicting goals, options, decision, rationale and follow-up. She shares anonymised versions with her postgraduate cohort. Classmates from other industries describe similar conflicts, such as hospitals inspecting traffic or banks handling regulator requests. Prof. Rao emphasises that difficult cases rarely have perfect answers; the professional task is to make trade-offs visible, follow law and policy and leave an auditable record. Several cohort members adopt the same structure in their own organisations, and the shared cases become material for a later seminar on professional judgement.

### Worked example

Leila limits TLS inspection with exemptions, handles a customs request through documented lawful process, and refuses plaintext key export during an HSM failure in favour of the standby HSM.

> **Synthetic case.** The cases are invented; legal requirements vary by jurisdiction.

### Errors and limits

Inspection proxies become high-value targets. Pressure during incidents is when controls most often get bypassed.

### Exercises

- **EX036 — Inspection risks.** Name two risks of TLS inspection. *Rubric:* 3 = two of breaks end-to-end guarantees, concentrates signing key, outdated proxy TLS weakens connections;; 2 = one;; 1 = none;; 0 = none.
- **EX037 — Inspection exemptions.** Which traffic did Leila exempt from inspection? *Rubric:* 3 = banking, health and partner traffic;; 2 = two;; 1 = none;; 0 = none.
- **EX038 — Lawful request.** Why could Corvane comply with the customs request? *Rubric:* 3 = it holds keys for its own data and the request was valid; followed documented procedure;; 2 = holds keys;; 1 = refused;; 0 = none.
- **EX039 — HSM failure.** What did Leila do when operations asked to export signing keys? *Rubric:* 3 = refused plaintext export; activated standby HSM despite two-hour delay;; 2 = refused;; 1 = exported;; 0 = none.
- **EX040 — Case structure.** What structure does Leila use for case write-ups? *Rubric:* 3 = context, conflicting goals, options, decision, rationale, follow-up;; 2 = four;; 1 = none;; 0 = none.

### Synthesis

Difficult cases force trade-offs between security, operations and law; documented procedures and visible reasoning keep decisions defensible.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Cryptography and trust services: leadership and assurance

### Learning outcomes

You will (1) lead a cryptographic modernisation programme; (2) provide assurance to boards and regulators; (3) define programme metrics and reporting.

### 9.1 Leading the programme

Leila becomes programme lead. She sets a two-year roadmap in phases: inventory and baseline in the first six months, key-management consolidation in the next nine, and post-quantum readiness pilots in the final nine, with legacy EDI retirement running throughout. Each phase has deliverables, owners and exit criteria. She meets unit owners monthly and the steering committee quarterly. Leading means removing obstacles, such as negotiating time with business units, more than designing cryptography. She keeps a single-page roadmap visible to every unit, so progress and slips are obvious to everyone.

### 9.2 Assurance to the board

The board wants assurance that the programme reduces risk. Leila reports a small set of metrics: legacy-accepting endpoints, share of certificates automated, keys without owners, systems with post-quantum readiness assessments and incidents related to cryptography. Each metric has a baseline, a target and a trend. She pairs metrics with narrative: what changed, what slipped and why. She avoids vanity metrics, such as the number of policies published, which say little about risk. Each quarter's report fits on two pages, so busy directors actually read it.

### 9.3 Independent assurance

Corvane's internal audit team reviews the programme halfway through. Auditors sample evidence: change records, inventory entries and key ceremony minutes. They find the inventory accurate for internet-facing systems but incomplete for internal services, and that two units' owners rarely attend the forum. Leila accepts the findings, adds internal scanning and escalates attendance through unit heads. She values independent assurance because it tests whether the programme works as reported, not only as designed. She shares the audit report with all unit owners.

### 9.4 Regulatory engagement

Corvane's finance division is regulated and must show sound key management. Leila prepares a pack for the regulator: the cryptographic standard, inventory summary, key-management architecture, evidence of controls and the post-quantum plan. She explains assumptions openly, including the planning scenario chosen in Chapter 4. The regulator asks how Corvane would respond to a compromise of a signing root; Leila walks through the rehearsed procedure. Transparent engagement builds credibility that helps when issues arise later. She keeps a log of every regulator question and answer.

### Worked example

Leila leads a phased two-year roadmap, reports five risk metrics with narrative, accepts audit findings on internal inventory and forum attendance, and briefs the regulator on assumptions and compromise response.

> **Synthetic case.** The programme and audit are invented.

### Errors and limits

Metrics reported without narrative invite misreading. Assurance limited to design misses whether controls operate.

### Exercises

- **EX041 — Roadmap phases.** Describe the three roadmap phases. *Rubric:* 3 = inventory and baseline (6 months), key consolidation (9), PQ pilots (9), with EDI retirement throughout;; 2 = partial;; 1 = none;; 0 = none.
- **EX042 — Board metrics.** Name three metrics Leila reports. *Rubric:* 3 = three of legacy endpoints, automated certificate share, unowned keys, PQ assessments, crypto incidents;; 2 = two;; 1 = vanity;; 0 = none.
- **EX043 — Audit findings.** What did internal audit find? *Rubric:* 3 = inventory incomplete for internal services; two units' owners rarely attend;; 2 = one;; 1 = none;; 0 = none.
- **EX044 — Regulator pack.** List three items in the regulator pack. *Rubric:* 3 = three of standard, inventory summary, architecture, control evidence, PQ plan;; 2 = two;; 1 = one;; 0 = none.
- **EX045 — Regulator question.** What did the regulator ask and how did Leila answer? *Rubric:* 3 = response to signing-root compromise; walked through rehearsed procedure;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Leadership turns cryptographic plans into delivered change, and honest metrics with independent assurance give boards and regulators justified confidence.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read cryptographic research critically as a practitioner; (2) evaluate claims about attacks and performance; (3) translate research into organisational relevance.

### 10.1 Reading as a practitioner

Leila's cohort reads research papers and standards on topics affecting Corvane: side-channel attacks on post-quantum implementations, studies of TLS deployment and analyses of certificate ecosystems. Prof. Rao teaches a reading method: identify the claim, the threat model, the evidence and the conditions under which the claim holds. Leila applies it to Boneh and Shoup's chapters on authenticated encryption and to Shoup's paper on sequences of games, published on the IACR ePrint archive, learning how security proofs structure their arguments step by step.

### 10.2 Evaluating attack claims

Many headlines announce that an algorithm is "broken". Leila learns to ask whether the attack is practical, what resources it needs, whether it targets the algorithm or a specific implementation and whether patches exist. A side-channel attack on one implementation, requiring physical access, does not mean the standard is broken. Conversely, a cryptanalytic attack on an algorithm's structure, even if not yet practical, signals the need to plan migration. She writes one-paragraph briefs translating papers into "what this means for Corvane".

### 10.3 Evaluating performance claims

Performance studies of post-quantum algorithms report handshake times and sizes. Leila checks the hardware, software versions and network conditions, comparing them with Corvane's environment. A study on server-grade processors says little about telematics units. She replicates one benchmark on Corvane's own test devices using vendor libraries and finds results close to published figures for servers but slower on telematics units, confirming that local testing is needed for constrained systems. She publishes her measurement method internally so other teams can repeat it on their own devices before planning migrations.

### 10.4 Translating research

Leila maintains a research watch list for the programme: topics, key papers, standards status and relevance ratings. Each quarter she briefs the steering committee on changes, such as a new IETF document on hybrid key exchange or an implementation vulnerability in a library Corvane uses. She avoids flooding executives with papers; she reports only items that change risk or plans. Research reading thus becomes a programme input rather than an academic exercise. Executives say the brief is the most useful page in their pack.

### Worked example

Leila applies a claim-threat-evidence-conditions method, separates implementation attacks from algorithm breaks, replicates a benchmark on telematics units and maintains a quarterly research watch list.

> **Synthetic case.** The watch list and benchmarks are invented; Boneh–Shoup and Shoup (2004) are real.

### Errors and limits

Headlines exaggerate; read the paper. Benchmarks rarely transfer across hardware.

### Exercises

- **EX046 — Reading method.** What four elements does Prof. Rao's method identify? *Rubric:* 3 = claim, threat model, evidence, conditions;; 2 = three;; 1 = one;; 0 = none.
- **EX047 — Broken claims.** What questions does Leila ask of a "broken" headline? *Rubric:* 3 = practicality, resources, algorithm vs implementation, patches;; 2 = three;; 1 = none;; 0 = none.
- **EX048 — Side-channel meaning.** Does a physical side-channel attack on one implementation break the standard? *Rubric:* 3 = no; it targets an implementation needing physical access;; 2 = no;; 1 = yes;; 0 = none.
- **EX049 — Benchmark replication.** What did Leila's replication show? *Rubric:* 3 = close to published figures on servers, slower on telematics units;; 2 = both;; 1 = one;; 0 = none.
- **EX050 — Watch list rule.** What does Leila report to executives from the watch list? *Rubric:* 3 = only items that change risk or plans;; 2 = filter;; 1 = everything;; 0 = none.

### Synthesis

Practitioners read research for claims, threat models and conditions, then translate only what changes organisational risk.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) deliver an applied project retiring legacy EDI cryptography; (2) coordinate partners through a transition; (3) measure outcomes and residual risk.

### 11.1 Project definition

Leila's applied project retires legacy cryptography on the EDI platform: twelve endpoints accepting TLS 1.1 or older, two-year manual certificates and RSA 2048 keys. The aim is that every EDI endpoint meets the baseline, certificates renew automatically, and all active partners migrate without lost shipments. Scope includes 140 partners, ranging from global carriers to small customs brokers. She defines success measures, risks and a communication plan before any technical change. She also secures a budget line for partner support, recognising that most of the effort will be human rather than technical, and agrees it with the finance director.

### 11.2 Partner transition

Leila segments partners by readiness. Large partners already support TLS 1.3 and move in the first month. Medium partners need configuration help, provided through a support desk. Small brokers using old client software receive free updated clients and step-by-step guides, with a test endpoint where they can check connections before the deadline. Monthly reminders show each partner's status. She negotiates a short extension for three brokers affected by a local internet outage, documenting the exception and its compensating controls. Weekly status dashboards help her focus effort.

### 11.3 Technical changes

The team deploys new EDI gateways configured to the baseline, with certificates from the internal ACME service renewed every ninety days and keys generated on the gateways. Old endpoints run in parallel during migration, monitored for remaining connections. When traffic on an old endpoint drops to zero for two weeks, it is shut down. Leila insists on vendor-supported configuration and no custom cryptographic code, and runs the pre-change compatibility scan from Chapter 7 before each cut-over. Each cut-over has a named engineer on call.

### 11.4 Outcomes and residual risk

After six months, all twelve legacy endpoints are retired; 138 of 140 partners have migrated, and the remaining two, inactive for a year, are formally offboarded. No shipments were lost, though four partners had delays of under a day. Certificates now renew automatically. Residual risks include RSA 2048 keys on some partner sides, outside Corvane's control, and the EDI protocol's message-size limit, which may complicate post-quantum signatures. Leila records both in the risk register with owners. She presents the outcomes to the steering committee.

### Worked example

Leila's project retires all twelve legacy EDI endpoints, migrates 138 of 140 partners with no lost shipments, automates certificates and records residual risks.

> **Synthetic case.** Partner counts and outcomes are invented.

### Errors and limits

Hard deadlines without support harm small partners; exceptions need compensating controls. Parallel running must end, or old endpoints linger.

### Exercises

- **EX051 — Project aim.** State the project's aim. *Rubric:* 3 = every EDI endpoint meets baseline, automatic renewal, all active partners migrate without lost shipments;; 2 = partial;; 1 = vague;; 0 = none.
- **EX052 — Small broker support.** What support did small brokers receive? *Rubric:* 3 = free updated clients, guides, a test endpoint, reminders;; 2 = two;; 1 = none;; 0 = none.
- **EX053 — Shutdown rule.** When is an old endpoint shut down? *Rubric:* 3 = after traffic is zero for two weeks;; 2 = rule;; 1 = immediately;; 0 = none.
- **EX054 — Migration result.** How many partners migrated, and what happened to the rest? *Rubric:* 3 = 138 of 140; two inactive partners offboarded;; 2 = count;; 1 = wrong;; 0 = none.
- **EX055 — Residual EDI risk.** Name one residual risk recorded. *Rubric:* 3 = partner-side RSA 2048 keys or EDI message-size limit for PQ signatures;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Applied projects succeed when technical change is paired with partner support, monitored parallel running and honest residual-risk records.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review the programme's results against its goals; (2) transfer ownership to business-as-usual teams; (3) plan continuing improvement and personal development.

### 12.1 Results against goals

At the end of two years Leila reviews results. Legacy-accepting endpoints fell from twenty-five to zero on internet-facing systems; certificates are automated across all units; keys have owners and live in the hybrid architecture; and post-quantum readiness assessments cover every critical system, with pilots of hybrid key exchange on internal services. Two goals slipped: two port controllers await vendor firmware, and internal service inventory remains ninety percent complete. She reports successes and slips with equal clarity. She attaches the metric trends as an appendix.

### 12.2 Transfer to operations

Programmes end; operations continue. Leila transfers each capability to an owner: the standard to security architecture, inventory and renewals to operations, supplier requirements to procurement and post-quantum planning to a small working group. Each receives documentation, runbooks, metrics and a handover session. She defines what "done" means for transfer: the receiving team runs the process for one quarter without programme help. Two transfers need extra support, which she provides before closing. She keeps a transfer checklist signed by each receiving owner.

### 12.3 Continuing improvement

Leila writes a continuing-improvement plan: annual review of the standard against new NIST and IETF publications; biennial review of the quantum planning scenario chosen in Chapter 4; quarterly metrics to the risk committee; and a lessons-learned session after any cryptography-related incident. She recommends that the next programme focus on post-quantum migration of signatures for long-lived devices, where vendor dependencies make early action essential. Each element has a named owner and a calendar date, so the plan does not depend on Leila remaining in her role. The risk committee formally adopts it at its next meeting.

### 12.4 Personal development

In her final postgraduate reflection Leila notes that her technical knowledge mattered most when translating between engineers, executives, lawyers and partners. She lists skills developed: decision framing, evaluation design, negotiation and regulatory communication. She also notes mistakes: underestimating partner support needs and initially presenting assumptions as facts. Prof. Rao advises her to mentor junior architects, since teaching consolidates learning. Leila plans to present the EDI project at an industry forum, sharing lessons without revealing sensitive details. She also schedules a check-in with Prof. Rao in a year.

### Worked example

Leila reports zero internet-facing legacy endpoints and full certificate automation, two slipped goals, transfers capabilities with a one-quarter "done" test and writes an improvement plan and personal reflection.

> **Synthetic case.** Results are invented.

### Errors and limits

Declaring victory hides slips; report them. Transfers without a test period often fail quietly.

### Exercises

- **EX056 — Slipped goals.** Which two goals slipped? *Rubric:* 3 = two port controllers awaiting vendor firmware; internal inventory 90 percent complete;; 2 = one;; 1 = none;; 0 = none.
- **EX057 — Transfer done.** How is a completed transfer defined? *Rubric:* 3 = receiving team runs the process one quarter without programme help;; 2 = definition;; 1 = handover meeting;; 0 = none.
- **EX058 — Improvement plan.** Name three elements of the continuing-improvement plan. *Rubric:* 3 = three of annual standard review, biennial scenario review, quarterly metrics, post-incident lessons;; 2 = two;; 1 = one;; 0 = none.
- **EX059 — Next focus.** What should the next programme focus on and why? *Rubric:* 3 = PQ migration of signatures for long-lived devices, due to vendor dependencies;; 2 = focus;; 1 = none;; 0 = none.
- **EX060 — Leila's mistakes.** Which mistakes did Leila acknowledge? *Rubric:* 3 = underestimating partner support needs and presenting assumptions as facts;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Closing a programme means honest results, tested transfers, a plan for continuing improvement and reflection that shapes the next leader.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Leila Moradi, Prof. Anika Rao, Westbrook School of Security, Corvane Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Retire legacy TLS, consolidate key management and prepare for post-quantum migration within two years.

**EX002.** A fact is the count of TLS 1.0 endpoints, an assumption is the quantum-computer timeline, and a value is how much outage risk Corvane accepts.

**EX003.** Worst-case minimisation for the catastrophic root-key loss, expected value for frequent, measurable expiries.

**EX004.** She had presented an assumption about quantum timelines as an established fact.

**EX005.** Because someone new could rebuild the reasoning from it in about five minutes without asking Leila.

**EX006.** RFC 8446 for TLS 1.3, RFC 7748 for X25519 and SP 800-38D for AES-GCM.

**EX007.** 114 of 160 endpoints, or 71.2 percent.

**EX008.** Nine in ports, four in finance and twelve on legacy EDI.

**EX009.** Short, automated lifetimes signal mature management, while EDI's two-year manual certificates reveal low maturity.

**EX010.** Legacy protocol acceptance on EDI, because those endpoints face partners over the internet.

**EX011.** FIPS 203 for ML-KEM, FIPS 204 for ML-DSA and FIPS 205 for SLH-DSA.

**EX012.** It is 3,309 bytes against 64, about fifty-two times larger.

**EX013.** 1,216 bytes.

**EX014.** Truck telematics with costly links and small memory, port controllers on long vendor cycles, and EDI with message-size limits.

**EX015.** By the weakest grade of evidence in its chain.

**EX016.** If years data must stay secret plus years to migrate exceed years until a capable quantum computer, recorded traffic is already at risk.

**EX017.** The moderate scenario, with a review every two years.

**EX018.** A supported migration offering free updated client software and a firm, published deadline.

**EX019.** The controller accepted firmware signed with a deprecated algorithm.

**EX020.** She reported privately, agreed a timeline, isolated the controllers and let the vendor notify other customers once fixed.

**EX021.** Root and high-value signing keys stay in Corvane's HSMs, while application data keys live in the cloud service, wrapped under keys Corvane controls.

**EX022.** Cloud KMS 3.90, hybrid 3.65 and on-premises HSM 3.25.

**EX023.** Raising custody to 0.45 and dropping cost made the hybrid best, showing the choice turns on how much custody matters.

**EX024.** Dependence of cloud custody on contracts and law, and key-person risk with on-premises HSMs.

**EX025.** A cloud offer of customer-controlled, HSM-backed keys that satisfies regulators at lower cost.

**EX026.** Pairing removes differences between sites, such as size and age, from the comparison.

**EX027.** A mean reduction of 5.62 misconfigured endpoints per site with p = 0.0036.

**EX028.** With eight sites all improving, the smallest attainable value is about 1/256, roughly 0.0039.

**EX029.** A simultaneous change, such as a separate patching campaign, might account for some of the improvement.

**EX030.** So the board can weigh this programme against others competing for the same budget.

**EX031.** Architecture review, procurement, change management and onboarding.

**EX032.** Certificates and keys without owners were the ones expiring or lingering on deprecated algorithms.

**EX033.** TLS 1.3 support, documented key management and timely notification of key compromise.

**EX034.** Its answers showed its product contained hard-coded keys.

**EX035.** An unexpected disconnection of a small partner after a cryptographic change.

**EX036.** It breaks end-to-end protection and concentrates a powerful signing key in the proxy.

**EX037.** Banking, health and partner traffic.

**EX038.** Corvane held the keys to its own records and the request was lawful, so it complied through a documented procedure.

**EX039.** She refused plaintext export and brought up the documented standby HSM, accepting a two-hour delay.

**EX040.** Context, conflicting goals, options, decision, rationale and follow-up.

**EX041.** Inventory and baseline first, then key-management consolidation, then post-quantum pilots, with EDI retirement running across all three.

**EX042.** Legacy-accepting endpoints, the share of automated certificates and keys without owners.

**EX043.** The inventory missed internal services, and owners from two units seldom attended the forum.

**EX044.** The cryptographic standard, an inventory summary and the post-quantum plan.

**EX045.** How Corvane would handle a compromised signing root, answered by walking through the rehearsed procedure.

**EX046.** The claim, the threat model, the evidence and the conditions under which it holds.

**EX047.** Whether the attack is practical, what it needs, whether it hits the algorithm or one implementation, and whether fixes exist.

**EX048.** No, it affects that implementation under physical access, not the standard itself.

**EX049.** Results matched published server figures but were slower on telematics units.

**EX050.** Only research or standards changes that alter Corvane's risks or plans.

**EX051.** All EDI endpoints meet the baseline with automated renewal, and every active partner migrates without losing shipments.

**EX052.** Free updated client software, step-by-step guides, a test endpoint and monthly reminders.

**EX053.** Once it has carried no traffic for two weeks.

**EX054.** 138 of 140 migrated, and the two inactive for a year were offboarded.

**EX055.** The EDI protocol's message-size limit, which may hamper post-quantum signatures.

**EX056.** Two port controllers still need vendor firmware, and the internal service inventory is only ninety percent complete.

**EX057.** The receiving team operates the process for a quarter without help from the programme.

**EX058.** An annual standard review, a biennial review of the quantum scenario and quarterly metrics to the risk committee.

**EX059.** Post-quantum migration of signatures on long-lived devices, because vendor dependencies require early action.

**EX060.** Underestimating how much support partners needed and initially stating assumptions as facts.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, keys and data in this book are synthetic unless a sentence cites a public source.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barker, E., & Roginsky, A. (2019). *Transitioning the use of cryptographic algorithms and key lengths* (NIST SP 800-131A Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-131Ar2>
- Barnes, R., Bhargavan, K., Lipp, B., & Wood, C. (2022). *Hybrid public key encryption* (RFC 9180). IETF. <https://www.rfc-editor.org/rfc/rfc9180>
- Barnes, R., Hoffman-Andrews, J., McCarney, D., & Kasten, J. (2019). *Automatic certificate management environment (ACME)* (RFC 8555). IETF. <https://www.rfc-editor.org/rfc/rfc8555>
- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Boneh, D., & Shoup, V. (2023). *A graduate course in applied cryptography* (version 0.6, draft). <https://toc.cryptobook.us/>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Dworkin, M. (2007). *Recommendation for block cipher modes of operation: Galois/Counter Mode (GCM) and GMAC* (NIST SP 800-38D). NIST. <https://doi.org/10.6028/NIST.SP.800-38D>
- Josefsson, S., & Liusvaara, I. (2017). *Edwards-curve digital signature algorithm (EdDSA)* (RFC 8032). IETF. <https://www.rfc-editor.org/rfc/rfc8032>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Krawczyk, H., & Eronen, P. (2010). *HMAC-based extract-and-expand key derivation function (HKDF)* (RFC 5869). IETF. <https://www.rfc-editor.org/rfc/rfc5869>
- Krawczyk, H., Bellare, M., & Canetti, R. (1997). *HMAC: Keyed-hashing for message authentication* (RFC 2104). IETF. <https://www.rfc-editor.org/rfc/rfc2104>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Langley, A., Hamburg, M., & Turner, S. (2016). *Elliptic curves for security* (RFC 7748). IETF. <https://www.rfc-editor.org/rfc/rfc7748>
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate transparency* (RFC 6962). IETF. <https://www.rfc-editor.org/rfc/rfc6962>
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- Moriarty, K., Kaliski, B., Jonsson, J., & Rusch, A. (2016). *PKCS #1: RSA cryptography specifications version 2.2* (RFC 8017). IETF. <https://www.rfc-editor.org/rfc/rfc8017>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2008). *The keyed-hash message authentication code (HMAC)* (FIPS 198-1). <https://doi.org/10.6028/NIST.FIPS.198-1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2023). *Digital signature standard (DSS)* (FIPS 186-5). <https://doi.org/10.6028/NIST.FIPS.186-5>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Nystrom, M. (2005). *Identifiers and test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512* (RFC 4231). IETF. <https://www.rfc-editor.org/rfc/rfc4231>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Shoup, V. (2004). *Sequences of games: A tool for taming complexity in security proofs* (Cryptology ePrint Archive, Paper 2004/332). <https://eprint.iacr.org/2004/332>
