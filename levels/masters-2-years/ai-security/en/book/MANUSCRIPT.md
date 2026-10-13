# AI and Machine-Learning Security: A Master's Research Book

- Language: English (`en`); master's programme, two years; approximately 1,600 hours of planned study.
- Editorial state: **draft**. Chapters 1–8 of 8 have authored teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; offline labs use the Python 3 standard library and their printed outputs were produced by real runs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: beginning researchers who will design, run and defend a supervised dissertation in AI and machine-learning security.
- Relation to neighbouring books: the [postgraduate book](../../../../postgraduate-2-years/ai-security/en/book/MANUSCRIPT.md) is practice-led; the [doctoral book](../../../../doctorate-2-years/ai-security/en/book/MANUSCRIPT.md) asks for an original contribution tested independently. **This book teaches the full research cycle once, under supervision**: question, literature, design, competing explanations, pilot, analysis, writing and defence.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not a qualification and no authority to test real systems. All organizations, people, datasets and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Each chapter has learning outcomes, teaching text, a worked example, practice activities, errors and limits, exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs are deterministic, run offline with `python3 file.py`, and print the results shown under *Expected output*. They are toy models chosen to make a concept measurable, not evidence about production systems.

### The running example (synthetic): a privacy dissertation at Harbourline

> **Synthetic case — fiction.** *Leo Brandt* is a master's student placed with **Harbourline Mutual**, an invented insurer that fine-tunes a text classifier to triage claim notes. Leo's dissertation asks whether *deduplicating training records* reduces membership-inference leakage from the fine-tuned model at an acceptable accuracy cost. All records are synthetic; no real claimant data is used; experiments run on an isolated copy. Every number about Harbourline is invented.

### Source policy

Sources were checked on 12 October 2026: NIST [AI 100-1](https://doi.org/10.6028/NIST.AI.100-1), [AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) and [AI 100-2 E2025](https://doi.org/10.6028/NIST.AI.100-2e2025); the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); [MITRE ATLAS](https://atlas.mitre.org/); [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj); and [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html). Papers are cited by arXiv identifier, each opened and title-checked.

## Contents

| Stage | Chapter |
|---|---|
| 1 | [1 Research question and literature method](#ch-01) |
| 1 | [2 AI and machine-learning security: advanced seminar](#ch-02) |
| 2 | [3 Study design, ethics and reproducibility](#ch-03) |
| 2 | [4 AI and machine-learning security: competing explanations](#ch-04) |
| 3 | [5 Proposal and pilot](#ch-05) |
| 3 | [6 Data collection and analysis](#ch-06) |
| 4 | [7 Dissertation writing and limitations](#ch-07) |
| 4 | [8 Independent review and defense](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) move from a topic to a researchable question with a clear unit of analysis; (2) run a systematic, documented literature search across security and machine-learning venues and preprint servers; (3) extract evidence into a comparison matrix; (4) judge source quality, including preprints and vendor material; and (5) write a short, honest state-of-the-art section.

### 1.1 From topic to question

"Privacy of AI" is a topic. "Does deduplicating training records reduce membership-inference advantage against a fine-tuned text classifier, and at what accuracy cost?" is a question. A researchable question names a *system* (fine-tuned classifier), an *intervention or factor* (deduplication), an *outcome* (membership-inference advantage; accuracy) and implicitly a *comparison* (with versus without). The acronym PICO from evidence-based medicine (population, intervention, comparison, outcome) is a useful template. Check feasibility early: can you obtain or synthesise data, do you have compute, can the work be done in the time, and is it ethical and authorised?

### 1.2 A documented search

AI-security literature is spread across security conferences (IEEE S&P, USENIX Security, ACM CCS, NDSS), machine-learning conferences (NeurIPS, ICML, ICLR) and arXiv preprints, plus frameworks from NIST, OWASP and MITRE. Write a search protocol: databases (e.g., DBLP, Google Scholar, arXiv, ACM Digital Library), search strings, date range, inclusion and exclusion criteria, and the date you searched. Follow citations forwards and backwards from seed papers — for membership inference, Shokri et al. (arXiv:1610.05820) is the obvious seed. Log counts at each stage (found, screened, included) so a reader could repeat the search. This is a light version of systematic-review practice; it protects you from citing only what you already knew.

### 1.3 Extracting evidence

Build a matrix with one row per paper and columns for: threat model (attacker knowledge and access), model type and size, data, metric, main result, defence tested, adaptive evaluation, code availability and limitations. For privacy work, record whether the paper reports true-positive rate at low false-positive rate or only average accuracy/AUC; the former matters because an attack that confidently identifies a few individuals is a real harm even if its average performance looks modest. The matrix will reveal disagreements and gaps that become your contribution.

### 1.4 Judging sources

Rank evidence by how checkable it is. Peer-reviewed papers with released code are strongest; preprints may be excellent but are unreviewed; vendor blogs and marketing are claims to verify, not evidence. Standards and frameworks (NIST AI 100-1, AI 100-2 E2025, ISO/IEC 42001) define vocabulary and expectations; they are not experimental results. When a preprint later appears in a venue, cite the final version if it differs. Never cite a paper you have not opened, and never invent a DOI: if you cannot find an identifier, cite the title, authors, year and URL you actually used.

### 1.5 Worked example (synthetic Harbourline case)

Leo's protocol searched DBLP, arXiv and Google Scholar on 2 February with strings combining "membership inference", "fine-tuning", "deduplication" and "memorization", 2016–2026, including empirical studies on classifiers or language models and excluding papers without a stated threat model. Of 212 hits, 61 survived title screening, 24 abstract screening and 17 full-text reading. The matrix showed that most studies reported AUC, few reported TPR at 0.1% FPR, and only three tested deduplication directly — all on generative language models, none on fine-tuned classifiers. Leo's state-of-the-art paragraph said so plainly and cited Carlini et al. (arXiv:2012.07805) for verbatim extraction as the motivating harm.

The membership-inference lab shows the core idea Leo will study: when a model effectively memorises its training records (k = 1), membership is detectable; when it generalises (larger k), the signal fades.

```python
"""Lab M: membership inference against an overfit 1-nearest-neighbour 'model'
that returns a confidence score. Synthetic records only; teaching model."""
import random, math
rng = random.Random(5)
def rec(): 
    y = rng.random() < 0.5
    return [rng.gauss(0.6 if y else -0.6, 1.0) for _ in range(4)], int(y)
members = [rec() for _ in range(150)]; nonmembers = [rec() for _ in range(150)]
def confidence(x, y, k):
    # k-NN vote share for the true label, computed over the training set
    d = sorted((sum((a-b)**2 for a, b in zip(x, m)), my) for m, my in members)
    return sum(1 for _, my in d[:k] if my == y)/k
def auc(pos, neg):
    s = sum((p > n) + 0.5*(p == n) for p in pos for n in neg)
    return s/(len(pos)*len(neg))
for k in (1, 5, 25):
    pos = [confidence(x, y, k) for x, y in members]
    neg = [confidence(x, y, k) for x, y in nonmembers]
    best = max(sum(p >= t for p in pos)/len(pos) - sum(n >= t for n in neg)/len(neg)
               for t in sorted(set(pos + neg)))
    print(f"k={k:2d} attack_auc={auc(pos, neg):.3f} best_advantage={best:.3f}")
```

Expected output:

```text
k= 1 attack_auc=0.600 best_advantage=0.200
k= 5 attack_auc=0.521 best_advantage=0.073
k=25 attack_auc=0.520 best_advantage=0.060
```

### 1.6 Practice activities

1. Write your topic, then three candidate questions in PICO form; pick one and justify feasibility. 2. Write a search protocol and run it, logging counts. 3. Build a ten-row evidence matrix.

For the questions, name the system, the intervention or factor, the comparison and the outcome, as Leo's question does. Judge feasibility on data, compute, time and ethics, and drop any question that fails one of them. For the search, record databases, strings, dates and counts at each stage, so someone else could repeat it. For the matrix, include whether each paper reports TPR at low FPR.

### 1.7 Errors and limits

- Questions too broad to answer in a dissertation.
- Searches that stop at the first page of a search engine.
- Treating a vendor blog as evidence.
- Citing papers you have not read, or fabricating identifiers.
- Reporting only averages for privacy attacks.

Each error weakens the dissertation from the start. A broad question cannot be answered in the time. A search that stops early misses work such as the three deduplication studies Leo found. A vendor blog is a claim to verify. Uncited or invented identifiers damage trust in every other citation. Averages hide the few individuals an attack identifies confidently, which is the harm Leo studies.

### Exercises

- **EX001 — PICO.** Write a PICO question about prompt-injection defences. Rubric: 3 = all four elements specific and feasible; 2 = one vague; 1 = two missing; 0 = topic only.
- **EX002 — Search protocol.** List six elements of a documented search protocol. Rubric: 3 = sources, strings, dates, criteria, search date, counts; 2 = four; 1 = two; 0 = none.
- **EX003 — Matrix columns.** Name six matrix columns for an AI-security literature review and why one matters. Rubric: 3 = six relevant plus justification; 2 = six; 1 = three; 0 = none.
- **EX004 — Low-FPR.** Why report TPR at low FPR for membership inference? Rubric: 3 = harm comes from confident identification of some individuals; averages hide it; 2 = partial; 1 = vague; 0 = wrong.
- **EX005 — Source ranking.** Rank: vendor blog, arXiv preprint with code, peer-reviewed paper without code, NIST framework — and explain the framework's role. Rubric: 3 = sensible ranking plus framework as vocabulary not results; 2 = ranking only; 1 = vague; 0 = none.
- **EX006 — Lab reading.** What AUC does the MIA lab report at k = 1 and at k = 5? Rubric: 3 = 0.600 and 0.521 with interpretation; 2 = numbers only; 1 = one number; 0 = wrong.
- **EX007 — Missing identifier.** You cannot find a DOI for a workshop paper. How do you cite it? Rubric: 3 = authors, title, venue/year, URL actually used, no invented DOI; 2 = partial; 1 = vague; 0 = invents one.

### Synthesis

A good dissertation starts with a narrow, feasible question and a search that someone else could repeat. The evidence matrix turns reading into a map of gaps, and honest sourcing keeps the map trustworthy.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — AI and machine-learning security: advanced seminar

### Learning outcomes

You will (1) explain the main attack classes — evasion, poisoning and backdoors, privacy (membership inference, data extraction), model extraction, and prompt injection — with their threat models; (2) explain the defences and their known limits; (3) read and present a paper critically in a seminar; (4) relate results to NIST AI 100-2 E2025, OWASP LLM 2025 and MITRE ATLAS; and (5) identify how each attack class appears in a real deployment such as Harbourline's.

### 2.1 The seminar format

Each week one student presents a paper in fifteen minutes: claim, threat model, method, results, and three critical questions. The group discusses whether the evidence supports the claim. The aim is not to admire papers but to understand exactly what they show.

Leo's presentation of Shokri et al. in the worked example below follows this format, and his third question became part of his own design. Prepare questions that a reader could answer from the paper, and note those it cannot answer, since those are often where research gaps lie.

### 2.2 Evasion

Adversarial examples (Szegedy et al., arXiv:1312.6199) are inputs changed slightly to cause errors. FGSM (Goodfellow et al., arXiv:1412.6572) takes one step along the sign of the loss gradient; PGD (Madry et al., arXiv:1706.06083) iterates and projects back into the allowed perturbation set; adversarial training uses such examples during training. In text, "small" changes are harder to define: synonym swaps or character edits may change meaning. The toy lab shows how accuracy collapses as the budget grows.

```python
"""Lab E: evasion of a toy linear classifier (synthetic data, stdlib only).
Trains logistic regression on two synthetic clusters, then applies a
fast-gradient-sign (FGSM-style) perturbation of size eps to every test point
and reports clean vs adversarial accuracy. Teaching model only."""
import math, random
rng = random.Random(7)
def point(label):
    cx = 1.0 if label else -1.0
    return [rng.gauss(cx, 0.7), rng.gauss(cx, 0.7)], label
train = [point(i % 2) for i in range(400)]
test = [point(i % 2) for i in range(200)]
w, b = [0.0, 0.0], 0.0
sig = lambda z: 1 / (1 + math.exp(-z))
for epoch in range(200):
    gw, gb = [0.0, 0.0], 0.0
    for x, y in train:
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        gw[0] += (p - y)*x[0]; gw[1] += (p - y)*x[1]; gb += p - y
    w = [w[i] - 0.1*gw[i]/len(train) for i in range(2)]; b -= 0.1*gb/len(train)
def acc(data, eps):
    ok = 0
    for x, y in data:
        # gradient of the loss w.r.t. x is (p - y) * w; FGSM steps along its sign
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        xa = [x[i] + eps*math.copysign(1, (p - y)*w[i]) for i in range(2)]
        ok += (sig(w[0]*xa[0] + w[1]*xa[1] + b) >= 0.5) == bool(y)
    return ok / len(data)
print(f"weights w=({w[0]:.3f}, {w[1]:.3f}) b={b:.3f}")
for eps in (0.0, 0.25, 0.5, 0.75, 1.0):
    print(f"eps={eps:.2f} accuracy={acc(test, eps):.3f}")
```

Expected output:

```text
weights w=(1.795, 1.756) b=-0.080
eps=0.00 accuracy=0.985
eps=0.25 accuracy=0.950
eps=0.50 accuracy=0.840
eps=0.75 accuracy=0.660
eps=1.00 accuracy=0.505
```

For Harbourline, evasion would mean wording a claim note so the classifier routes it wrongly.

### 2.3 Poisoning and backdoors

Poisoning attacks control part of the training data. Availability poisoning degrades accuracy broadly; targeted and backdoor poisoning (Gu et al., arXiv:1708.06733) keep clean accuracy while a trigger causes chosen behaviour. For Harbourline, a malicious claims handler who can insert notes into the training set could teach the classifier that a phrase routes claims to fast-track approval. Defences include data provenance, filtering of outliers, and limiting who can contribute training data; none is complete.

Ask, for any dataset, who can add records and whether that is logged.

### 2.4 Privacy attacks

Membership inference (Shokri et al., arXiv:1610.05820) decides whether a record was in training, using differences in model confidence or loss. Training-data extraction (Carlini et al., arXiv:2012.07805) recovers verbatim sequences from generative models. Differential privacy (Abadi et al., arXiv:1607.00133) bounds how much any one record can influence the model, reducing both risks at a utility cost. For an insurer, membership itself can be sensitive ("this person made a claim").

Leo's dissertation studies the first of these: whether deduplication reduces membership leakage. A claimant whose note appears many times is, on this reasoning, more exposed.

### 2.5 Model extraction

Model extraction (Tramèr et al., arXiv:1609.02943) builds a copy of a model from its API outputs. Rich outputs (full probability vectors) make it easier; rounding and returning only labels make it harder but not impossible. Extraction matters for intellectual property and because a stolen copy enables white-box attacks.

```python
"""Lab X: model extraction of a toy linear scoring API by querying it.
The 'API' returns a real-valued score; d+1 well-chosen queries recover the
weights exactly, and rounding the output limits fidelity. Synthetic model."""
import random
rng = random.Random(9)
d = 5
secret_w = [round(rng.uniform(-2, 2), 3) for _ in range(d)]; secret_b = 0.42
def api(x, decimals=None):
    s = sum(a*b for a, b in zip(secret_w, x)) + secret_b
    return round(s, decimals) if decimals is not None else s
for dec in (None, 2, 0):
    b = api([0]*d, dec)
    w = [api([1 if j == i else 0 for j in range(d)], dec) - b for i in range(d)]
    err = max(abs(a-c) for a, c in zip(w, secret_w))
    test = [[rng.uniform(-1, 1) for _ in range(d)] for _ in range(500)]
    agree = sum((sum(a*c for a, c in zip(w, x))+b > 0) == (api(x) > 0) for x in test)/500
    print(f"output_rounding={str(dec):4s} queries={d+1} max_weight_error={err:.3f} label_agreement={agree:.3f}")
```

Expected output:

```text
output_rounding=None queries=6 max_weight_error=0.000 label_agreement=1.000
output_rounding=2    queries=6 max_weight_error=0.004 label_agreement=0.998
output_rounding=0    queries=6 max_weight_error=0.534 label_agreement=0.882
```

The lab shows the effect of output precision: with full probabilities the copy is exact, with two decimals it is nearly exact, and with whole-number rounding the copy agrees on 88% of labels. For Harbourline, returning only the triage label would make extraction harder, not impossible.

### 2.6 Prompt injection and LLM applications

When an LLM processes untrusted text, that text may contain instructions (Greshake et al., arXiv:2302.12173). OWASP LLM 2025 ranks prompt injection first and lists related risks such as sensitive information disclosure, excessive agency and system prompt leakage. Harbourline's future plan — an assistant that reads claim e-mails and drafts responses — would inherit these risks.

For such an assistant, a claimant's e-mail is untrusted text that could steer drafts or leak other claimants' details. That plan is outside Leo's dissertation, but the seminar should map it to the OWASP entries so Harbourline can see which risks it would add.

### 2.7 Worked example (synthetic Harbourline case)

Leo presented Shokri et al. His three critical questions: (1) the shadow-model approach assumes the attacker can sample from a similar data distribution — is that realistic for insurance notes? (2) results were reported mostly as precision/accuracy; what is TPR at low FPR? (3) how much of the leakage is explained by overfitting? The group concluded that question (3) was directly relevant to his dissertation: if deduplication helps mainly by reducing overfitting, the "explanation" is generalisation, not deduplication per se — a competing explanation for Chapter 4.

### 2.8 Practice activities

1. Present one paper using the seminar format. 2. For each attack class, write a one-line threat model for a system you know. 3. Map Harbourline's planned e-mail assistant to three OWASP LLM 2025 entries.

For the presentation, prepare claim, threat model, method, results and three critical questions, as Leo did. For the threat models, name attacker knowledge, access and goal for each class. For the mapping, consider prompt injection, sensitive information disclosure and excessive agency, and say for each what the assistant could do wrong and what control would limit it.

### 2.9 Errors and limits

- Describing attacks without their threat model.
- Assuming image-domain results transfer directly to text.
- Treating rounding or label-only output as a complete defence against extraction.
- Ignoring that membership itself can be sensitive.

Each error leads to a misleading summary. An attack without its threat model cannot be compared with a defence. Image results may not transfer, since small text edits can change meaning. Rounding made extraction harder in the lab but did not stop it. For Harbourline, the mere fact that a person made a claim can be sensitive, so membership inference is a real harm. Check your seminar notes for all four.

### Exercises

- **EX008 — Threat models.** Give a one-line threat model for evasion, backdoor poisoning and membership inference. Rubric: 3 = three with knowledge, capability and goal; 2 = two; 1 = one; 0 = none.
- **EX009 — FGSM vs PGD.** Explain the difference. Rubric: 3 = single step vs iterated projected steps; PGD stronger; 2 = partial; 1 = vague; 0 = wrong.
- **EX010 — Extraction lab.** What happens to weight error and label agreement when outputs are rounded to integers, and what does that imply? Rubric: 3 = error 0.534, agreement 0.882; output precision limits fidelity but a useful copy remains; 2 = numbers only; 1 = vague; 0 = wrong.
- **EX011 — Insurer harm.** Why can membership be sensitive for Harbourline? Rubric: 3 = reveals that a person filed a claim, possibly health or loss details; 2 = partial; 1 = vague; 0 = none.
- **EX012 — Backdoor scenario.** Describe (at design level) a backdoor risk for the claims classifier and two controls. Rubric: 3 = insider-inserted trigger notes; provenance/access control and trigger/outlier testing; 2 = one control; 1 = vague; 0 = harmful detail.
- **EX013 — OWASP mapping.** Map the e-mail assistant to three OWASP LLM 2025 entries. Rubric: 3 = e.g., LLM01, LLM02, LLM06 with reasons; 2 = IDs only; 1 = one; 0 = none.
- **EX014 — Seminar questions.** Write three critical questions for a defence paper of your choice. Rubric: 3 = three about threat model, adaptive attack, metrics/costs; 2 = two; 1 = one; 0 = none.

### Synthesis

The seminar builds fluency in the attack classes and in critical reading. Each class has a threat model, a typical harm and defences with known limits — and the competing explanations you discover in discussion become research questions.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) choose a design (controlled experiment, observational study, case study) that fits the question; (2) define variables, controls, randomisation and sample size; (3) plan data handling and ethics for personal or sensitive data; (4) make the study reproducible from the start; and (5) document the plan so a supervisor can approve it.

### 3.1 Choosing a design

Most master's projects in AI security are **controlled experiments**: you change one factor (deduplication on/off), hold others fixed, and measure outcomes. **Observational** studies analyse existing data without intervening (for example, logs of attempted prompt injections against a deployed assistant) and must worry about confounding. **Case studies** examine one system in depth and are useful when experiments are impossible, but they support weaker generalisation. Pick the strongest design you can run ethically and within time.

Leo's question compares conditions he can control, so a controlled experiment fits.

### 3.2 Variables and controls

For Leo: the *independent variable* is training-set treatment (original, exact-deduplicated, near-deduplicated). *Dependent variables* are membership-inference TPR at 1% FPR, AUC, and classifier macro-F1. *Controlled variables* include model architecture, epochs, learning rate, random seeds and evaluation split. Randomise which records go into training versus held-out sets so that members and non-members come from the same distribution — otherwise an attack may detect distribution shift rather than membership, a known pitfall. Use several seeds and report variability. Estimate sample size from a pilot (Chapter 5).

### 3.3 Ethics and data protection

When data relates to people, apply data-protection principles: lawful basis, purpose limitation, minimisation, storage limitation and security. The GDPR applies in the EU; other jurisdictions have similar laws. Prefer synthetic data that preserves the properties you need; if real data is essential, obtain approval from your institution's ethics board and the data controller, pseudonymise, restrict access, and set deletion dates. Privacy attacks on real data create the very harm you study; run them only on copies under agreement, and never publish recovered records. If your project involves people (annotators, survey participants), you need informed consent.

### 3.4 Reproducible by design

Set up from day one: a version-controlled repository; pinned environment; configuration files rather than hard-coded settings; fixed seeds; a single command to run each experiment; logs written as machine-readable records; and a data card describing provenance and processing (Gebru et al., arXiv:1803.09010). The NeurIPS reproducibility programme (Pineau et al., arXiv:2003.12206) offers a checklist worth adopting. Reproducibility is far cheaper to build in than to retrofit.

Leo's design lists the repository, a lock file and a `run.py --config` interface from the start, which made his later reruns simple.

### 3.5 Worked example (synthetic Harbourline case)

Leo's design document specifies a controlled experiment with three conditions × five seeds. Data: 20,000 synthetic claim notes generated from templates with controlled duplication (8% exact duplicates, 6% near-duplicates), so the ground truth of duplication is known. Members and non-members are drawn by random split from the same pool. The ethics section records that no real claimant data is used, that Harbourline's data-protection officer reviewed the plan, and that the synthetic generator will be released. The reproducibility section lists the repository, environment lock file and a `run.py --config` interface.

The stats lab shows why five seeds are planned: per-seed results vary even when nothing changes but the seed.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Expected output:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

### 3.6 Practice activities

1. Write your design with variables, controls and randomisation. 2. Draft an ethics and data-protection section. 3. Create the repository skeleton with configuration files and a seed policy.

Use Leo's design as a model: name independent, dependent and controlled variables, and say how members and non-members are drawn from the same pool. For the ethics text, say what data is used, who reviewed the plan and what will be released. For the repository, include configuration files, a lock file, a seed policy and a single command per experiment. Ask your supervisor to review all three.

### 3.7 Errors and limits

- Members and non-members drawn from different distributions.
- One seed per condition.
- Using real personal data where synthetic data would do.
- Hard-coded paths and settings that make reruns impossible.

Each error undermines the result. Members and non-members from different distributions let the attack detect shift rather than membership. One seed cannot show variability, which Lab S makes visible. Real personal data creates the harm being studied when synthetic data would serve, as Leo's synthetic notes do. Hard-coded paths make reruns fail for anyone else, including examiners. Check your design for all four.

### Exercises

- **EX015 — Design choice.** For "do deployed assistants receive injection attempts, and of what kinds?", choose a design and justify. Rubric: 3 = observational study of authorised logs with confounding/consent notes; 2 = design only; 1 = poor fit; 0 = none.
- **EX016 — Variables.** List independent, dependent and three controlled variables for an evasion-defence experiment. Rubric: 3 = all correct; 2 = minor gap; 1 = major gap; 0 = none.
- **EX017 — Distribution pitfall.** Explain why members and non-members must come from the same distribution. Rubric: 3 = otherwise the attack detects shift, inflating results; 2 = partial; 1 = vague; 0 = wrong.
- **EX018 — Data protection.** Name four data-protection principles that apply to a privacy-attack study. Rubric: 3 = four correct; 2 = three; 1 = one or two; 0 = none.
- **EX019 — Lab reading.** In the stats lab, what is the spread of per-seed rates and the mean? Rubric: 3 = 0.105–0.145, mean 0.125, sd 0.017; 2 = two of three; 1 = one; 0 = wrong.
- **EX020 — Reproducibility setup.** List five things to set up before the first experiment. Rubric: 3 = five from repo, pinned env, configs, seeds, single command, logs, data card; 2 = four; 1 = two; 0 = none.

### Synthesis

Design determines what you can conclude. Controlled variables, matched member/non-member sampling, multiple seeds, ethical data handling and reproducibility built in from the start are what let a short project produce a credible answer.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — AI and machine-learning security: competing explanations

### Learning outcomes

You will (1) list alternative explanations for an observed security effect; (2) design ablations and controls that separate them; (3) recognise confounders typical of AI-security experiments (overfitting, data leakage, distribution shift, evaluation artefacts, weak attacks); (4) use the poisoning and evasion labs to reason about mechanisms; and (5) state conclusions at the level the evidence supports.

### 4.1 Why competing explanations matter

An observed effect — "deduplication lowered membership-inference advantage" — can have several causes. Deduplication might reduce memorisation of repeated records specifically; it might simply reduce effective training-set size and therefore change overfitting; it might change class balance; or the attack might be weaker on the new model for reasons unrelated to privacy. A dissertation that names and tests these alternatives is far stronger than one that reports the effect alone.

Leo's seminar discussion raised the overfitting explanation before he had any data.

### 4.2 A catalogue of alternatives in AI security

- **Generalisation vs. specific mechanism.** Privacy leakage correlates with the train–test gap. Compare treatments at matched generalisation gaps, or include a control that changes data size without deduplicating.
- **Leakage.** Duplicates across train and test splits inflate accuracy and confuse privacy metrics (Kapoor and Narayanan, arXiv:2207.07048).
- **Distribution shift.** If members and non-members differ in distribution, attacks detect shift, not membership.
- **Weak or mis-tuned attack.** A defence "works" because the attack was not adapted (Athalye et al., arXiv:1802.00420). Use a stronger or calibrated attack as a control.
- **Evaluation artefacts.** Metric choice or thresholds tuned on the test set.
- **Randomness.** A single seed can produce an apparent effect.

### 4.3 Ablations and controls

An *ablation* removes or varies one component to see its contribution. Leo's plan adds a fourth condition: *random removal* of the same number of records that deduplication would remove. If random removal gives the same privacy gain, the explanation is dataset size; if deduplication gives more, the duplicates matter. He also adds a control attack calibrated with reference models, which is known to be stronger at low FPR than a simple confidence threshold.

Write the expected result of each condition before running.

### 4.4 Reasoning about mechanisms with the labs

The poisoning lab gives a clean contrast. Label flipping of up to 40% of one class barely moves a nearest-centroid model (0.965 → 0.945), because centroids average many points; a backdoor using a separate trigger feature reaches 98% attack success with 80 points while clean accuracy stays at 0.968. The *mechanism* — a new, otherwise unused feature direction — explains why clean metrics miss it. A competing explanation ("the model is just inaccurate") is ruled out by the unchanged clean accuracy.

```python
"""Lab P: label-flip poisoning and a backdoor trigger on a toy nearest-centroid
classifier (synthetic data, stdlib only). Teaching model only."""
import random
rng = random.Random(11)
def point(label, trigger=False):
    cx = 1.0 if label else -1.0
    x = [rng.gauss(cx, 0.8), rng.gauss(cx, 0.8), 0.0]
    if trigger: x[2] = 5.0          # third feature is the 'trigger'
    return x, label
clean = [point(i % 2) for i in range(400)]
test = [point(i % 2) for i in range(400)]
def fit(data):
    c = {}
    for lab in (0, 1):
        pts = [x for x, y in data if y == lab]
        c[lab] = [sum(p[i] for p in pts)/len(pts) for i in range(3)]
    return c
def pred(c, x):
    d = {k: sum((x[i]-v[i])**2 for i in range(3)) for k, v in c.items()}
    return min(d, key=d.get)
def accuracy(c, data): return sum(pred(c, x) == y for x, y in data)/len(data)
print("label-flip poisoning (flip a fraction of class-1 labels to 0):")
for frac in (0.0, 0.1, 0.2, 0.3, 0.4):
    data = [(x, y) for x, y in clean]; ones = [i for i, (x, y) in enumerate(data) if y == 1]
    for i in ones[:int(frac*len(ones))]: data[i] = (data[i][0], 0)
    print(f"  flipped={frac:.1f} clean_test_accuracy={accuracy(fit(data), test):.3f}")
print("backdoor: add n triggered class-1 points labelled 0")
trig_test = [point(1, trigger=True) for _ in range(200)]
for n in (0, 10, 40, 80):
    data = clean + [(point(1, trigger=True)[0], 0) for _ in range(n)]
    c = fit(data)
    asr = sum(pred(c, x) == 0 for x, _ in trig_test)/len(trig_test)
    print(f"  poison_points={n:3d} clean_accuracy={accuracy(c, test):.3f} attack_success={asr:.3f}")
```

Expected output:

```text
label-flip poisoning (flip a fraction of class-1 labels to 0):
  flipped=0.0 clean_test_accuracy=0.965
  flipped=0.1 clean_test_accuracy=0.965
  flipped=0.2 clean_test_accuracy=0.953
  flipped=0.3 clean_test_accuracy=0.950
  flipped=0.4 clean_test_accuracy=0.945
backdoor: add n triggered class-1 points labelled 0
  poison_points=  0 clean_accuracy=0.965 attack_success=0.075
  poison_points= 10 clean_accuracy=0.963 attack_success=0.145
  poison_points= 40 clean_accuracy=0.963 attack_success=0.685
  poison_points= 80 clean_accuracy=0.968 attack_success=0.980
```

For Leo, the analogy is that duplicated records may give the model a specific route to memorise them.

### 4.5 Worked example (synthetic Harbourline case)

In pilot data under the calibrated attack, deduplication reduced TPR at 1% FPR from 6.1% to 3.4%. Random removal of the same number of records reduced it to 5.6%. The difference between deduplication and random removal (2.2 points) is the part plausibly attributable to removing duplicates; the remaining 0.5 points is explained by size. The simple confidence-threshold attack sat near its floor in every condition (the pilot in Chapter 5 describes this), so only the calibrated attack could separate them. Leo's conclusion sentence changed from "deduplication protects privacy" to "most of the observed reduction in membership leakage is attributable to removing duplicated records rather than to the smaller training set, under the evaluated attack".

### 4.6 Practice activities

1. List five competing explanations for your expected result. 2. Design one ablation and one control for each of the two most plausible. 3. Rewrite your expected conclusion at the evidence level you will have.

For the list, use the catalogue above and add any explanation specific to your system. For the ablations, change one thing at a time and say what result would support each explanation. For the conclusion, write the sentence you could defend if the main effect appeared, and compare it with Leo's revised sentence, which names the attack and what was ruled out.

### 4.7 Errors and limits

- Reporting an effect without testing alternatives.
- Ablations that change several things at once.
- Using only a weak attack to evaluate a privacy defence.
- Claiming mechanism from correlation alone.

Each error lets a competing explanation survive. An effect without alternatives tested may be size, shift or chance. An ablation that changes several things cannot attribute the effect. A weak attack can make any defence look good, which is why Leo added the calibrated attack. Correlation, such as leakage tracking duplication, does not by itself show mechanism without controls like random removal. Check your plan for all four.

### Exercises

- **EX021 — Alternatives.** List four competing explanations for "a guardrail reduced jailbreak success". Rubric: 3 = four plausible (weaker attack set, refusals over-triggered, distribution change, seed/judge artefact); 2 = three; 1 = one or two; 0 = none.
- **EX022 — Ablation.** Design the random-removal control and explain what each outcome would mean. Rubric: 3 = same count removed at random; equal gain → size, larger gain → duplicates; 2 = design only; 1 = vague; 0 = none.
- **EX023 — Lab mechanism.** Why does label flipping barely change the centroid model while the backdoor succeeds? Rubric: 3 = centroids average many points vs trigger uses a new feature direction unaffected by clean data; 2 = partial; 1 = vague; 0 = wrong.
- **EX024 — Lab numbers.** Report clean accuracy and attack success at 80 poison points. Rubric: 3 = 0.968 and 0.980; 2 = one; 1 = approximate; 0 = wrong.
- **EX025 — Stronger attack.** Why include a calibrated attack as a control? Rubric: 3 = ensures defence effect is not an artefact of a weak attack, especially at low FPR; 2 = partial; 1 = vague; 0 = wrong.
- **EX026 — Conclusion level.** Rewrite "dedup fixes privacy" at the evidence level of 4.5. Rubric: 3 = attributes portion, names attack and conditions; 2 = partial; 1 = still overclaims; 0 = unchanged.

### Synthesis

Effects need explanations, and explanations need tests. Ablations, controls and stronger attacks separate mechanisms from artefacts, and the resulting conclusions are narrower but defensible.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a dissertation proposal with question, background, design, analysis plan, ethics, risks and timeline; (2) run a pilot to test feasibility and estimate variability; (3) compute sample sizes; (4) revise the plan from pilot evidence; and (5) obtain approval with a clear record of decisions.

### 5.1 The proposal

A master's proposal is typically 3,000–6,000 words. Sections: **question and motivation** (one paragraph each); **background** from your evidence matrix; **design** (Chapter 3) including competing explanations and ablations (Chapter 4); **analysis plan** with primary and secondary outcomes and the statistics you will use; **ethics and data protection**; **risks** (technical, data, schedule) with mitigations; **timeline** with milestones; and **expected contribution** stated modestly. The analysis plan is the most neglected part — write it now, before data, so later choices cannot be steered by results.

Leo's proposal followed this outline.

### 5.2 The pilot

A pilot runs the full pipeline at small scale. Goals: confirm the code works end to end, measure run time, measure variability of the primary outcome, check that the attack and metrics behave sensibly (for example, the undefended model is attackable), and find surprises. Pilot results are not hypothesis tests; do not report them as findings, and keep the final test data out of the pilot.

Leo's pilot found a floor effect and a generator flaw. Record both in the decision log.

### 5.3 Sample size and power

For rates, the normal approximation n ≈ z² p(1−p)/h² gives the trials needed for a confidence-interval half-width h. For comparisons between conditions, power analysis asks how many repetitions you need to detect a difference d with probability (power) 0.8 at significance 0.05; for paired designs, the variance of the *differences* matters. With few seeds (typical in ML), report intervals over seeds and over evaluation items rather than relying on a single significance test.

Leo's pilot showed about 0.8 points of variation across seeds, which together with bootstrapping over records made five seeds adequate. Use the variation you actually observe, not a guess.

### 5.4 Revising the plan

Pilots usually change something: an attack too weak to separate conditions, an evaluation that takes too long, a metric with a floor effect (all conditions near zero). Record each change in a decision log with the reason. Supervisors and examiners respond well to a proposal that shows it learned from its pilot.

Leo's log records two changes from his pilot: replacing the floor-limited attack with a calibrated one, and fixing the templates that produced near-identical notes across classes. Each has a date and a reason. Keep the log with the proposal so examiners can trace the plan's evolution.

### 5.5 Worked example (synthetic Harbourline case)

Leo's pilot used 2,000 records and two seeds. It took 40 minutes per run, so the full plan (20,000 records, four conditions, five seeds) is about 130 hours of compute — feasible on the lab cluster. The simple confidence-threshold attack produced TPR at 1% FPR of 1–2% in all conditions: a floor effect. He replaced it with a reference-model-calibrated attack, which separated conditions. Variability across seeds was about 0.8 points, so five seeds plus bootstrap over records were judged adequate. He also found that two templates generated near-identical notes across classes, introducing label noise; he fixed the generator and recorded the change.

The evasion lab provides an example of a pilot sweep: before choosing one perturbation budget for a main study, sweep several to find where the effect is measurable rather than at floor or ceiling.

```python
"""Lab E: evasion of a toy linear classifier (synthetic data, stdlib only).
Trains logistic regression on two synthetic clusters, then applies a
fast-gradient-sign (FGSM-style) perturbation of size eps to every test point
and reports clean vs adversarial accuracy. Teaching model only."""
import math, random
rng = random.Random(7)
def point(label):
    cx = 1.0 if label else -1.0
    return [rng.gauss(cx, 0.7), rng.gauss(cx, 0.7)], label
train = [point(i % 2) for i in range(400)]
test = [point(i % 2) for i in range(200)]
w, b = [0.0, 0.0], 0.0
sig = lambda z: 1 / (1 + math.exp(-z))
for epoch in range(200):
    gw, gb = [0.0, 0.0], 0.0
    for x, y in train:
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        gw[0] += (p - y)*x[0]; gw[1] += (p - y)*x[1]; gb += p - y
    w = [w[i] - 0.1*gw[i]/len(train) for i in range(2)]; b -= 0.1*gb/len(train)
def acc(data, eps):
    ok = 0
    for x, y in data:
        # gradient of the loss w.r.t. x is (p - y) * w; FGSM steps along its sign
        p = sig(w[0]*x[0] + w[1]*x[1] + b)
        xa = [x[i] + eps*math.copysign(1, (p - y)*w[i]) for i in range(2)]
        ok += (sig(w[0]*xa[0] + w[1]*xa[1] + b) >= 0.5) == bool(y)
    return ok / len(data)
print(f"weights w=({w[0]:.3f}, {w[1]:.3f}) b={b:.3f}")
for eps in (0.0, 0.25, 0.5, 0.75, 1.0):
    print(f"eps={eps:.2f} accuracy={acc(test, eps):.3f}")
```

Expected output:

```text
weights w=(1.795, 1.756) b=-0.080
eps=0.00 accuracy=0.985
eps=0.25 accuracy=0.950
eps=0.50 accuracy=0.840
eps=0.75 accuracy=0.660
eps=1.00 accuracy=0.505
```

### 5.6 Practice activities

1. Write your analysis plan with primary and secondary outcomes. 2. Run a pilot and fill a decision log. 3. Compute sample size for your primary outcome.

For the analysis plan, name the primary outcome, such as TPR at 1% FPR, and the secondary ones, with the statistics for each. For the pilot, run the whole pipeline at small scale, and log every change with its reason as Leo did. For the sample size, use the formula above with the variation your pilot observed, and say whether your compute budget allows it.

### 5.7 Errors and limits

- Proposals without an analysis plan.
- Reporting pilot results as findings.
- Using test data in the pilot.
- Ignoring floor or ceiling effects.

Each error weakens the study. Without an analysis plan, later choices can be steered by results. Pilot results are not findings, because the pilot was not designed or sized for testing. Test data used in a pilot is no longer unseen. A floor effect, such as Leo's simple attack at 1–2% in every condition, hides real differences. Check your proposal for all four.

### Exercises

- **EX027 — Proposal sections.** List eight proposal sections. Rubric: 3 = eight correct; 2 = six; 1 = three; 0 = none.
- **EX028 — Pilot goals.** Give four goals of a pilot. Rubric: 3 = pipeline works, timing, variability, metric sanity/surprises; 2 = three; 1 = one or two; 0 = none.
- **EX029 — Sample size.** Compute trials for a rate near 5% with half-width 1 point at 95%. Rubric: 3 = ≈1,825 with formula; 2 = arithmetic slip; 1 = formula only; 0 = none.
- **EX030 — Floor effect.** What is a floor effect and how did Leo fix it? Rubric: 3 = all conditions near minimum so differences invisible; stronger calibrated attack; 2 = definition only; 1 = vague; 0 = wrong.
- **EX031 — Lab sweep.** From the evasion lab, which eps values avoid floor and ceiling for comparing defences? Rubric: 3 = around 0.5–0.75 (0.840, 0.660), reasons; 2 = values only; 1 = vague; 0 = wrong.
- **EX032 — Decision log.** Write two decision-log entries from Leo's pilot. Rubric: 3 = date, change, reason, effect for both; 2 = one; 1 = vague; 0 = none.

### Synthesis

The proposal fixes what you will do and how you will analyse it; the pilot shows whether you can. Revisions recorded with reasons turn surprises into evidence of a careful process.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) run the main experiments exactly as planned and log deviations; (2) check data quality before analysis; (3) compute primary outcomes with uncertainty (Wilson intervals, bootstrap, variation across seeds); (4) analyse paired comparisons and secondary outcomes; and (5) present results in tables and figures that answer the research question.

### 6.1 Running the main study

Freeze code at a tagged commit, lock the configuration files, and run conditions in an interleaved or randomised order so that time-dependent problems (a node slowing down, a library update) do not align with one condition. Each run writes a record: condition, seed, config hash, start and end time, metrics and paths to raw outputs. Keep a deviation log as in the pilot.

Leo's runs were interleaved by condition and seed, and his deviation log recorded the missing seed-4 run and its rerun. Check the log before analysis, not after.

### 6.2 Data-quality checks

Before computing anything, check: are all expected runs present? Do canary checks pass (the undefended model must be attackable; a model trained on shuffled labels should perform at chance)? Are there duplicates across splits? Are metric values within plausible ranges? These checks catch bugs that would otherwise become "findings".

Leo's checks found one missing seed-4 run, which was rerun and logged before analysis. Write the checks as a script so they run the same way each time, and keep their output with the results.

### 6.3 Primary analysis

Compute the primary outcome per condition with intervals. For rates, use Wilson intervals; for metrics averaged over items, bootstrap over items; report variation across seeds separately. For paired comparisons (same records or prompts across conditions), bootstrap the *difference*. Follow the analysis plan; label any extra analysis as exploratory. When several comparisons are made, correct for multiplicity or present them as exploratory.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Expected output:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

The lab demonstrates the three tools. With 3 of 20 successes, the Wilson interval spans 5% to 36%: such a small sample cannot support a precise claim. The per-seed rates show seed-to-seed spread. The paired bootstrap estimates the reduction of a defence on the same prompts with an interval excluding zero.

### 6.4 Secondary outcomes and costs

Every security improvement has costs: accuracy, latency, refusals of legitimate requests, compute, maintainability. Report them on the same items. A privacy defence that halves leakage but drops macro-F1 by 10 points is a different proposition from one that costs 1 point. Plot the trade-off (e.g., TPR at 1% FPR versus macro-F1) for all conditions.

Leo's result is the second kind: near dedup more than halved TPR at 1% FPR, to 4.2%, while macro-F1 fell by less than one point. Report both numbers together, with intervals, so readers can weigh the trade-off themselves. Do it here too.

### 6.5 Worked example (synthetic Harbourline case)

Leo's main results (synthetic, five seeds, 20,000 records): TPR at 1% FPR under the calibrated attack was 9.8% (original), 7.9% (random removal), 5.1% (exact dedup) and 4.2% (near dedup). The paired difference between near dedup and random removal was 3.7 points (bootstrap 95% CI 2.6–4.9). Macro-F1 fell from 0.912 to 0.905 under near dedup. Data-quality checks found one missing seed-4 run, rerun and logged. An exploratory analysis, labelled as such, showed leakage concentrated in records that had appeared three or more times.

The exploratory finding about records seen three or more times is a hypothesis for future work, not a confirmed result.

### 6.6 Practice activities

1. Write a data-quality checklist for your study and run it. 2. Produce the primary table with intervals. 3. Plot the security–utility trade-off.

For the checklist, include all expected runs, canary checks, duplicates across splits and plausible ranges, and run it before any analysis. For the primary table, give each condition's outcome with an interval and the number of seeds. For the plot, put the privacy metric against macro-F1 for every condition, so a reader can see the trade-off at a glance, as Leo's figure does.

### 6.7 Errors and limits

- Running all seeds of one condition before another.
- Analysing before quality checks.
- Mixing exploratory and confirmatory results.
- Reporting security gains without costs.

Each error biases results or hides costs. Running seeds of one condition first lets time-dependent problems align with it. Analysing before quality checks turns bugs into findings, such as a missing seed. Mixing exploratory and confirmatory results overstates certainty. Reporting gains without costs hides trade-offs, such as the drop in macro-F1 that Leo reported. Check your analysis for all four.

### Exercises

- **EX033 — Interleaving.** Why interleave conditions during runs? Rubric: 3 = prevents time-dependent problems confounding conditions; 2 = partial; 1 = vague; 0 = wrong.
- **EX034 — Quality checks.** List four data-quality checks. Rubric: 3 = completeness, canaries, cross-split duplicates, plausible ranges; 2 = three; 1 = one or two; 0 = none.
- **EX035 — Lab reading.** What are the baseline and defended ASR and the reduction interval in the stats lab? Rubric: 3 = 0.350, 0.190, [0.120, 0.203]; 2 = two; 1 = one; 0 = wrong.
- **EX036 — Paired vs unpaired.** Why bootstrap the difference on shared items rather than comparing two separate intervals? Rubric: 3 = item difficulty cancels; tighter, correct inference; 2 = partial; 1 = vague; 0 = wrong.
- **EX037 — Costs.** Name four costs to report for a security defence. Rubric: 3 = accuracy/utility, latency, false refusals, compute/maintenance; 2 = three; 1 = one or two; 0 = none.
- **EX038 — Exploratory.** How should Leo report the "three or more appearances" finding? Rubric: 3 = labelled exploratory, hypothesis for future work, not confirmatory; 2 = partial; 1 = reported as main result; 0 = omitted without reason.

### Synthesis

Analysis is where careful design pays off: interleaved runs, quality checks, intervals and paired comparisons turn raw logs into a defensible answer, and costs make the answer useful.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a dissertation so every chapter serves the research question; (2) write results and discussion that separate findings from interpretation; (3) write a limitations section organised by validity type; (4) handle security-sensitive details responsibly in writing; and (5) produce an artefact appendix that supports reproduction.

### 7.1 Structure

A common structure: introduction (problem, question, contribution summary); background and related work (from your matrix); method (design, data, attacks, metrics, analysis plan); results (primary, secondary, exploratory clearly labelled); discussion (interpretation, competing explanations, implications); limitations; conclusion; references; appendices (artefacts, extra tables). Write the method so a peer could repeat it; write the results so a reader can find the answer to the research question in one table.

Leo's dissertation answers its question in one table of TPR at 1% FPR and macro-F1 for the four conditions.

### 7.2 Findings versus interpretation

Results state what was measured: "near deduplication reduced TPR at 1% FPR from 9.8% to 4.2%". Discussion interprets: "this suggests duplicated records drive much of the leakage, consistent with work on memorisation in language models". Keep them apart. In discussion, return to competing explanations and say which your ablations ruled out.

Leo moved a recommendation that insurers should deduplicate from results to discussion and softened it. Read each results sentence and ask whether it reports a measurement; if it explains or recommends, move it.

### 7.3 Limitations by validity type

- **Internal**: could something other than the treatment explain the effect? (e.g., synthetic generator artefacts.)
- **Construct**: do the metrics measure the property? (e.g., TPR at 1% FPR under one attack family captures only some privacy risk.)
- **External**: does the result transfer? (e.g., one model architecture, synthetic notes, English only.)
- **Conclusion**: are the statistics adequate? (e.g., five seeds.)

For each, say what you did and what remains. Limitations written this way are a strength; examiners distrust dissertations that claim none.

### 7.4 Writing about attacks responsibly

Describe attacks at the level needed for understanding and reproduction in research settings, cite the original papers, and avoid publishing operational detail that targets named live systems. Never include recovered personal data. If you found a vulnerability in a real product, follow coordinated disclosure before the dissertation is published. Label synthetic data and organisations as fiction throughout.

Leo's dissertation describes the calibrated attack by citing its source and his configuration, without any recovered records. Ask your supervisor to read the attack description for operational detail before submission.

### 7.5 Artefact appendix

Include repository URL and commit, environment, commands to reproduce each table, data card for the synthetic generator, model card for any released model (Mitchell et al., arXiv:1810.03993), and hashes of key files. State what is not released and why.

Leo's appendix includes the synthetic generator's data card, the repository commit, commands for each table and file hashes. He states that no model is released and why. Ask a peer to reproduce one table from the appendix alone before submission. Keep it current.

### 7.6 Worked example (synthetic Harbourline case)

Leo's limitations section has four short subsections. External validity: "We studied one transformer classifier fine-tuned on synthetic English notes; results may differ for generative models, other languages and real claims data." Construct validity: "We measured membership inference with two attacks; attribute inference and extraction were not studied." He moved a sentence about "insurers should deduplicate" out of results into discussion and softened it to "deduplication is a low-cost candidate control that insurers could evaluate".

The extraction lab is cited in his background chapter as a simple illustration of why API output precision matters when describing threat models.

```python
"""Lab X: model extraction of a toy linear scoring API by querying it.
The 'API' returns a real-valued score; d+1 well-chosen queries recover the
weights exactly, and rounding the output limits fidelity. Synthetic model."""
import random
rng = random.Random(9)
d = 5
secret_w = [round(rng.uniform(-2, 2), 3) for _ in range(d)]; secret_b = 0.42
def api(x, decimals=None):
    s = sum(a*b for a, b in zip(secret_w, x)) + secret_b
    return round(s, decimals) if decimals is not None else s
for dec in (None, 2, 0):
    b = api([0]*d, dec)
    w = [api([1 if j == i else 0 for j in range(d)], dec) - b for i in range(d)]
    err = max(abs(a-c) for a, c in zip(w, secret_w))
    test = [[rng.uniform(-1, 1) for _ in range(d)] for _ in range(500)]
    agree = sum((sum(a*c for a, c in zip(w, x))+b > 0) == (api(x) > 0) for x in test)/500
    print(f"output_rounding={str(dec):4s} queries={d+1} max_weight_error={err:.3f} label_agreement={agree:.3f}")
```

Expected output:

```text
output_rounding=None queries=6 max_weight_error=0.000 label_agreement=1.000
output_rounding=2    queries=6 max_weight_error=0.004 label_agreement=0.998
output_rounding=0    queries=6 max_weight_error=0.534 label_agreement=0.882
```

### 7.7 Practice activities

1. Write your limitations section by validity type. 2. Mark every sentence in your results chapter as finding or interpretation and move misplaced ones. 3. Draft the artefact appendix.

For the limitations, use the four validity types and say for each what you did and what remains, as Leo did for one classifier and synthetic notes. For the results chapter, mark each sentence and move interpretations to the discussion. For the appendix, list repository, commit, environment, commands, cards and hashes, and state what is not released.

### 7.8 Errors and limits

- Results and discussion mixed.
- Limitations that are generic ("more data needed").
- Operational attack detail against named systems.
- Recommendations stated as findings.

Each error makes claims harder to trust. Mixed results and discussion blur what was measured. Generic limitations tell examiners nothing about this study. Operational detail against named systems helps attackers without helping readers. A recommendation stated as a finding claims more than the data shows, which is why Leo moved and softened his insurer recommendation. Check your draft for all four.

### Exercises

- **EX039 — Finding or interpretation.** Classify: (a) "ASR fell from 31% to 6%"; (b) "the defence works because it removes the attacker's channel". Rubric: 3 = (a) finding, (b) interpretation, with reason; 2 = labels only; 1 = one; 0 = wrong.
- **EX040 — Validity.** Write one limitation for each validity type for your project. Rubric: 3 = four specific; 2 = three; 1 = one or two; 0 = none.
- **EX041 — Responsible detail.** Rewrite a sentence giving an exact working payload against a named chatbot into responsible form. Rubric: 3 = design-level description, citation, no live target or string; 2 = partial; 1 = still operational; 0 = unchanged.
- **EX042 — Artefact appendix.** List six items. Rubric: 3 = six relevant; 2 = four; 1 = two; 0 = none.
- **EX043 — Lab citation.** What does the extraction lab show about output precision, with numbers? Rubric: 3 = exact recovery with full precision (error 0.000), 0.004 at 2 decimals, 0.534 at integers; agreement drops to 0.882; 2 = partial numbers; 1 = vague; 0 = wrong.
- **EX044 — Recommendation.** Rewrite "Insurers must deduplicate" at the evidence level. Rubric: 3 = candidate control to evaluate, with conditions; 2 = partial; 1 = still prescriptive; 0 = unchanged.

### Synthesis

A dissertation is judged by how clearly its claims match its evidence. Separating findings from interpretation, writing specific limitations and handling attack details responsibly make the work credible and safe.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) commission and use independent review of code and text before submission; (2) prepare a defence presentation; (3) answer examiner questions with evidence and limits; (4) respond to required corrections; and (5) plan dissemination, including a short practitioner summary.

### 8.1 Independent review before submission

Ask a peer who did not work on the project to (a) reproduce one main table from your artefact appendix, (b) read the method and say what they could not repeat, and (c) read the abstract and say what they think you claim. Each reveals a different problem: hidden dependencies, missing method detail, and overclaiming. A short code review focusing on metric computation and data splits is worth the time; bugs there change conclusions.

Leo's peer found a silent skip of long records this way.

### 8.2 The defence presentation

Twenty to thirty minutes: problem and question; design and why; results with intervals and costs; competing explanations and what ruled them out; limitations; contribution and next steps. One slide should answer the research question in a sentence with a number and an interval.

Leo's answer slide gave the paired difference with its interval. Put competing explanations before limitations, since examiners will ask about them. Rehearse with a timer and a peer who asks hard questions, and prepare backup slides for the ablation and the quality checks so you can show evidence when asked.

### 8.3 Answering examiners

Expect questions on design choices ("why synthetic data?"), threats to validity ("would this hold on real notes?"), statistics ("are five seeds enough?"), alternative explanations ("isn't this just overfitting?") and practice ("what should Harbourline do?"). Answer in three parts: direct answer, evidence, limit. When you do not know, say so and say how you would find out.

Leo's answers in the worked example below follow this form: the ablation as evidence, the attack as the limit. Prepare written answers to each expected question and rehearse them with a peer who plays a critical examiner.

### 8.4 Corrections and dissemination

Examiners often require corrections. Make each change, list it in a correction table with page references, and return it promptly. Dissemination options include a workshop paper, a public repository with the synthetic generator, and a two-page practitioner summary that states the finding, the conditions and the recommended next step — mapped where relevant to frameworks the organisation uses, such as the NIST AI RMF *Measure* and *Manage* functions or its ISO/IEC 42001 risk-treatment process.

Leo's practitioner summary states deduplication as a low-cost candidate control under the evaluated attack.

### 8.5 Worked example (synthetic Harbourline case)

A peer reproducing Leo's main table found that the evaluation script silently skipped records longer than 512 tokens, about 3% of non-members. Leo fixed it; TPR at 1% FPR moved by 0.2 points and conclusions held, and he recorded the fix. At the defence an examiner asked: "Isn't this just overfitting?" Leo showed the random-removal ablation and the matched-gap analysis: "Part of the effect is size-related — 1.9 points — but the remaining 3.7 points are specific to duplicates, under this attack." Another asked whether Harbourline should adopt differential privacy instead. Leo answered that DP gives formal guarantees (Abadi et al., arXiv:1607.00133) at a utility cost he did not measure; deduplication is complementary and cheap, and a DP comparison is future work.

The membership-inference lab can be used in the defence to show the core concept in thirty seconds.

```python
"""Lab M: membership inference against an overfit 1-nearest-neighbour 'model'
that returns a confidence score. Synthetic records only; teaching model."""
import random, math
rng = random.Random(5)
def rec(): 
    y = rng.random() < 0.5
    return [rng.gauss(0.6 if y else -0.6, 1.0) for _ in range(4)], int(y)
members = [rec() for _ in range(150)]; nonmembers = [rec() for _ in range(150)]
def confidence(x, y, k):
    # k-NN vote share for the true label, computed over the training set
    d = sorted((sum((a-b)**2 for a, b in zip(x, m)), my) for m, my in members)
    return sum(1 for _, my in d[:k] if my == y)/k
def auc(pos, neg):
    s = sum((p > n) + 0.5*(p == n) for p in pos for n in neg)
    return s/(len(pos)*len(neg))
for k in (1, 5, 25):
    pos = [confidence(x, y, k) for x, y in members]
    neg = [confidence(x, y, k) for x, y in nonmembers]
    best = max(sum(p >= t for p in pos)/len(pos) - sum(n >= t for n in neg)/len(neg)
               for t in sorted(set(pos + neg)))
    print(f"k={k:2d} attack_auc={auc(pos, neg):.3f} best_advantage={best:.3f}")
```

Expected output:

```text
k= 1 attack_auc=0.600 best_advantage=0.200
k= 5 attack_auc=0.521 best_advantage=0.073
k=25 attack_auc=0.520 best_advantage=0.060
```

### 8.6 Practice activities

1. Arrange a reproduction and abstract-reading review. 2. Build a defence deck with one answer slide. 3. Write the practitioner summary.

For the review, ask a peer to reproduce one table and read the abstract, and record what they found. For the deck, include one slide that answers the question with a number and an interval, as Leo's did with the 3.7-point difference. For the summary, state the finding, the conditions and the next step, and keep it to two pages. Keep notes of what changed.

### 8.7 Errors and limits

- Submitting without anyone reproducing a result.
- Answering questions defensively without evidence.
- Practitioner summaries that drop the conditions.
- Ignoring required corrections' page references.

Each error weakens the final stage. Without a reproduction, problems such as Leo's skipped long records reach examiners. Defensive answers without evidence lose examiners' confidence. A summary that drops conditions turns a result under one attack into a general rule. Corrections without page references are hard to check and delay the award. Check your submission for all four.

### Exercises

- **EX045 — Reviews.** Name three independent reviews to request and what each finds. Rubric: 3 = reproduction/hidden dependencies, method read/missing detail, abstract read/overclaiming; 2 = two; 1 = one; 0 = none.
- **EX046 — Answer slide.** Write Leo's one-sentence answer slide. Rubric: 3 = finding with number, interval, conditions; 2 = missing interval or conditions; 1 = vague; 0 = none.
- **EX047 — Overfitting question.** Answer "isn't this just overfitting?" for your own project. Rubric: 3 = direct answer, evidence (ablation/control), limit; 2 = two parts; 1 = one; 0 = none.
- **EX048 — Bug impact.** How should Leo report the 512-token bug? Rubric: 3 = describe, fix, quantify change, note conclusions held, in deviation/corrections record; 2 = partial; 1 = hide; 0 = none.
- **EX049 — DP vs dedup.** Contrast differential privacy and deduplication in two sentences. Rubric: 3 = DP formal bound with utility cost; dedup heuristic, cheap, targets repetition; complementary; 2 = partial; 1 = vague; 0 = wrong.
- **EX050 — Practitioner summary.** Write the first three sentences of the practitioner summary. Rubric: 3 = finding, conditions, next step, no overclaiming; 2 = two; 1 = one; 0 = none.

### Synthesis

Independent review catches the errors you cannot see; the defence tests whether you can connect every claim to evidence and its limits. A careful practitioner summary carries the result into practice without losing its conditions.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Harbourline Mutual and all its numbers are synthetic.

**EX001.** "In tool-using LLM agents that read untrusted e-mail (P), does requiring human confirmation for outbound actions (I), compared with no confirmation (C), reduce successful exfiltration in a sandbox benchmark of 500 synthetic tasks (O)?"

**EX002.** Sources/databases; search strings; date range; inclusion and exclusion criteria; date of search; counts at each screening stage (also: citation chasing).

**EX003.** Threat model; model type/size; data; metric; main result; defence; adaptive evaluation; code availability; limitations. *Adaptive evaluation* matters because defences tested only against fixed attacks are often broken later.

**EX004.** Privacy harm comes from confidently identifying particular individuals; an attack with modest AUC can still identify some records with near certainty, which only TPR at low FPR reveals.

**EX005.** Peer-reviewed paper (checked by review) and arXiv preprint with code (checkable) near the top — either order can be argued; vendor blog last. The NIST framework is not an experimental source: it provides vocabulary and expectations to cite for definitions.

**EX006.** k = 1: AUC 0.600; k = 5: AUC 0.521. Memorising (k = 1) leaks membership; averaging over neighbours mostly removes the signal.

**EX007.** Cite authors, title, workshop name and year, and the URL you used (with access date). Never invent a DOI.

**EX008.** Evasion: attacker with query (or white-box) access perturbs test inputs to cause misclassification. Backdoor: attacker who controls some training data inserts triggered examples to cause chosen outputs. Membership inference: attacker with query access to outputs decides whether a record was in training.

**EX009.** FGSM takes one step of size eps along the gradient sign; PGD takes many smaller steps, projecting back into the allowed set each time, and is a stronger attack.

**EX010.** With integer outputs, the maximum weight error is 0.534 and label agreement 0.882 (versus 0.000/1.000 at full precision). Coarse outputs reduce fidelity but still leave a useful approximate copy.

**EX011.** Membership reveals that a person filed a claim, which may imply health problems, accidents or losses — sensitive in itself.

**EX012.** An insider with write access to training notes could insert notes containing a rare phrase labelled "fast-track". Controls: restricted and logged write access with provenance on training data; pre-training audits for rare token–label correlations and post-training trigger testing.

**EX013.** LLM01 Prompt Injection (instructions in e-mails); LLM02 Sensitive Information Disclosure (claim details in replies); LLM06 Excessive Agency (sending replies without review).

**EX014.** E.g.: What adversary knowledge is assumed, and is the defence evaluated against an attacker who knows it? Are results reported at low false-positive rates and with intervals across seeds? What is the utility or latency cost on the same tasks?

**EX015.** Observational study of logs from an assistant the researcher is authorised to study, with consent/privacy safeguards; confounders (user population, feature changes) must be discussed. An experiment is impossible because you cannot control real attackers.

**EX016.** Independent: defence (none vs adversarial training). Dependent: accuracy under PGD at fixed eps; clean accuracy. Controlled: architecture, training epochs, data split, attack steps/eps, seeds.

**EX017.** If non-members differ in distribution (e.g., newer records), the attack can tell them apart by distribution shift, not membership, so measured leakage is inflated.

**EX018.** Lawfulness; purpose limitation; data minimisation; storage limitation; integrity and confidentiality (security); accountability.

**EX019.** Per-seed rates 0.110, 0.130, 0.135, 0.105, 0.145 — a range of 0.105–0.145 — with mean 0.125 and sd 0.017.

**EX020.** Version-controlled repository; pinned environment; configuration files; seed policy; one command per experiment; structured logs; data card.

**EX021.** The evaluation used weaker or different jailbreak prompts; the guardrail over-refuses (including benign prompts); prompt distribution differs between conditions; judge or seed artefacts.

**EX022.** Remove the same number of records at random (multiple draws). If privacy gain equals deduplication's, dataset size explains it; if deduplication gains more, removing duplicates matters.

**EX023.** Centroids average hundreds of points, so a minority of flipped labels shifts them little; the backdoor uses a third feature that is zero for clean data, creating a new direction that clean data cannot counteract.

**EX024.** Clean accuracy 0.968; attack success 0.980.

**EX025.** A weak attack can make any defence look effective; a calibrated, stronger attack (especially at low FPR) shows whether the reduction survives.

**EX026.** "Under a calibrated membership-inference attack, most of the observed reduction in leakage was attributable to removing duplicated records rather than to the smaller training set."

**EX027.** Question/motivation; background; design; competing explanations/ablations; analysis plan; ethics and data protection; risks and mitigations; timeline; expected contribution.

**EX028.** Confirm pipeline works end to end; measure run time; estimate variability; check metrics and attacks behave sensibly; discover surprises.

**EX029.** n ≈ 1.96² × 0.05 × 0.95 / 0.01² ≈ 1,825.

**EX030.** All conditions sit near the metric's minimum, so differences cannot be seen. Leo replaced the confidence-threshold attack with a reference-model-calibrated attack.

**EX031.** eps 0.50 (0.840) and 0.75 (0.660): accuracy is neither near the clean ceiling (0.985) nor at chance (0.505 at 1.00), so defences can be distinguished.

**EX032.** "Pilot day 3: replaced threshold attack with calibrated attack; reason: floor effect (1–2% TPR all conditions); effect: conditions separable." "Pilot day 4: fixed generator templates 12 and 19; reason: near-identical notes across classes; effect: removes label noise."

**EX033.** If conditions run in blocks, a time-dependent change (hardware, library, load) can masquerade as a treatment effect; interleaving spreads such problems across conditions.

**EX034.** All runs present; canaries pass (undefended model attackable, shuffled-label model at chance); no cross-split duplicates; metric values plausible.

**EX035.** Baseline ASR 0.350; defended 0.190; reduction 95% CI [0.120, 0.203].

**EX036.** Items vary in difficulty; pairing cancels that shared variation, giving a tighter, correct interval for the difference. Comparing overlapping separate intervals is conservative and can mislead.

**EX037.** Utility/accuracy; latency; false refusals or false positives; compute and maintenance cost.

**EX038.** As an exploratory result in a labelled subsection, framed as a hypothesis for future confirmatory work.

**EX039.** (a) Finding — a measured quantity. (b) Interpretation — a causal explanation that needs ablation evidence.

**EX040.** Internal: generator artefacts; construct: one attack family; external: one architecture, synthetic English notes; conclusion: five seeds. (Each with action taken.)

**EX041.** "Following Greshake et al. (arXiv:2302.12173), we constructed indirect injections embedded in retrieved documents in our sandbox; payload strings are withheld and available to researchers on request."

**EX042.** Repository and commit; environment; reproduction commands per table; data card; model card; key file hashes; statement of what is withheld and why.

**EX043.** Full precision recovers weights exactly (error 0.000, agreement 1.000); two decimals give error 0.004 (agreement 0.998); integers give error 0.534 (agreement 0.882). Output precision is part of the threat model.

**EX044.** "Deduplication is a low-cost control that insurers fine-tuning classifiers could evaluate for reducing membership leakage."

**EX045.** Reproduction of a table finds hidden dependencies and bugs; a method read finds missing detail; an abstract read finds overclaiming.

**EX046.** "Near deduplication reduced membership-inference TPR at 1% FPR from 9.8% to 4.2%, 3.7 points (95% CI 2.6–4.9) more than random removal, at a 0.007 macro-F1 cost — on synthetic notes, one architecture, calibrated attack."

**EX047.** Answers vary; a full answer gives a direct answer, the ablation or control evidence, and a limit.

**EX048.** Describe the bug, the fix, the 0.2-point change, that conclusions held, and record it in the deviation log and methods.

**EX049.** Differential privacy bounds each record's influence formally, at a measurable utility cost. Deduplication is a cheap heuristic that targets repeated records; they are complementary.

**EX050.** "Removing duplicated claim notes before fine-tuning roughly halved one measure of membership leakage in our synthetic study, at almost no accuracy cost. This held for one model type and synthetic data. We suggest a pilot on a governed copy of real data before adopting it."

## References

Links checked 12 October 2026; frameworks change, so re-verify. arXiv identifiers were opened and titles checked.

- Abadi, M. et al. (2016). Deep Learning with Differential Privacy. arXiv:1607.00133.
- Athalye, A., Carlini, N., Wagner, D. (2018). Obfuscated Gradients Give a False Sense of Security. arXiv:1802.00420.
- Carlini, N. et al. (2020). Extracting Training Data from Large Language Models. arXiv:2012.07805.
- European Union. Regulation (EU) 2024/1689 (Artificial Intelligence Act). <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Gebru, T. et al. (2018). Datasheets for Datasets. arXiv:1803.09010.
- Goodfellow, I., Shlens, J., Szegedy, C. (2014). Explaining and Harnessing Adversarial Examples. arXiv:1412.6572.
- Greshake, K. et al. (2023). Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv:2302.12173.
- Gu, T., Dolan-Gavitt, B., Garg, S. (2017). BadNets. arXiv:1708.06733.
- ISO/IEC 42001:2023 Artificial intelligence — Management system. <https://www.iso.org/standard/81230.html>
- Kapoor, S., Narayanan, A. (2022). Leakage and the Reproducibility Crisis in ML-based Science. arXiv:2207.07048.
- Madry, A. et al. (2017). Towards Deep Learning Models Resistant to Adversarial Attacks. arXiv:1706.06083.
- MITRE ATLAS. <https://atlas.mitre.org/>
- Mitchell, M. et al. (2018). Model Cards for Model Reporting. arXiv:1810.03993.
- NIST AI 100-1 (2023), AI RMF 1.0. <https://doi.org/10.6028/NIST.AI.100-1>
- NIST AI 100-2 E2025 (2025), Adversarial Machine Learning taxonomy. <https://doi.org/10.6028/NIST.AI.100-2e2025>
- NIST AI 600-1 (2024), Generative AI Profile. <https://doi.org/10.6028/NIST.AI.600-1>
- OWASP Top 10 for LLM Applications 2025. <https://genai.owasp.org/llm-top-10/>
- Pineau, J. et al. (2020). Improving Reproducibility in Machine Learning Research. arXiv:2003.12206.
- Shokri, R. et al. (2016). Membership Inference Attacks against Machine Learning Models. arXiv:1610.05820.
- Szegedy, C. et al. (2013). Intriguing properties of neural networks. arXiv:1312.6199.
- Tramèr, F. et al. (2016). Stealing Machine Learning Models via Prediction APIs. arXiv:1609.02943.
