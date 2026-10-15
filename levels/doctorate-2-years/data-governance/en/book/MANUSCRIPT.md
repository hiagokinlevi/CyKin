# Data Governance: Doctoral Research Track

- Language: English (`en`); course 187, Doctoral research track (2 years).
- Editorial state: **published**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: doctoral candidates studying how decision rights over data quality rules and record linkage shape official statistics.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs score quality dimensions on a synthetic business register, compute Fellegi-Sunter match weights on synthetic record pairs and score synthetic dataset metadata against a FAIR checklist. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one doctoral candidate from integrity rules and the research frontier through a proposal, a replicated linkage baseline, a main simulation with independent validation, peer critique, a reproducibility archive and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Nadia Rahman** | Doctoral candidate | Invented |
| **Prof. Lars Eriksen** | Supervisor | Invented |
| **Halvorsen University** | Fictional university | Invented |
| **Westmark Statistics Office** | Fictional statistics office linking a business register with employment records | Invented |

### Core sources

DAMA-DMBOK2 (2017); ISO/IEC 38505-1:2017; ISO 8000-8:2015; Khatri and Brown (2010), [doi:10.1145/1629175.1629210](https://doi.org/10.1145/1629175.1629210); Wang and Strong (1996); Batini et al. (2009); Fellegi and Sunter (1969); NIST SP 800-188; Wilkinson et al. (2016), [doi:10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes

You will (1) frame a doctoral question about data governance; (2) set integrity rules for working with linked administrative data; (3) plan methods that others can reproduce.

### 1.1 The candidate and the question

Nadia Rahman begins a two-year doctoral research track at the fictional Halvorsen University, supervised by Prof. Lars Eriksen. Her partner organisation is the fictional Westmark Statistics Office, which links a business register with employment records to publish statistics on regional jobs. Her question is how governance decisions, such as who sets data quality rules and who chooses record linkage thresholds, change the statistics that ministers and the public read. Khatri and Brown describe governance as deciding who holds decision rights over data, and Nadia wants to measure the consequences of those rights.

### 1.2 Integrity rules

Prof. Eriksen asks Nadia to write integrity rules before touching any data. All analysis uses a synthetic replica of Westmark's register built from published distributions, never confidential records. Every result is produced by a script kept under version control, and every figure in the thesis must be traceable to a script run. She will record decisions that change results, such as dropping a field, in a decision log with dates and reasons. Nadia notes that integrity in governance research matters doubly, because the research itself makes claims about the integrity of other people's data.

### 1.3 Methods others can repeat

Nadia chooses mixed methods. Quantitative work measures data quality dimensions and linkage error on the synthetic replica. Qualitative work uses interviews with Westmark staff about who decides quality rules and thresholds, conducted with informed consent and anonymised transcripts. She pre-registers her main hypotheses with her supervisor: that unclear decision rights lead to inconsistent thresholds across releases, and that inconsistent thresholds produce measurable shifts in regional employment counts. Pre-registration protects her against reshaping hypotheses after seeing the results. Interview guides are piloted with two retired staff.

### 1.4 Sources and standards

Nadia builds her reading list around established sources. DAMA-DMBOK2 describes data governance as the exercise of authority and control over data assets and lists its relationship to other data management functions. ISO/IEC 38505-1 applies the ISO/IEC 38500 governance model to data, placing accountability with the governing body. Wang and Strong offer a consumer-oriented framework of data quality dimensions. She records which claims each source supports, so that her thesis cites sources for definitions and evidence rather than for authority alone. Definitions come first.

### Worked example

Nadia frames a question about decision rights and published statistics, writes integrity rules for a synthetic replica, pre-registers hypotheses and maps sources to the claims they support.

> **Synthetic case.** Halvorsen, Westmark and all people are synthetic; DAMA-DMBOK2, ISO/IEC 38505-1, Khatri and Brown (2010) and Wang and Strong (1996) are real.

### Errors and limits

A synthetic replica cannot reproduce every quirk of real records; state this limit early.

### Exercises

- **EX001 — Research question.** What is Nadia's doctoral question? *Rubric:* 3 = how governance decisions change published statistics;; 2 = mentions decisions;; 1 = vague;; 0 = none.
- **EX002 — Decision rights.** How do Khatri and Brown frame governance? *Rubric:* 3 = deciding who holds decision rights over data;; 2 = mentions rights;; 1 = vague;; 0 = none.
- **EX003 — Replica rule.** What data may Nadia analyse? *Rubric:* 3 = a synthetic replica from published distributions;; 2 = partly correct;; 1 = real;; 0 = none.
- **EX004 — Traceability.** How must every figure be traceable? *Rubric:* 3 = to a script run under version control;; 2 = mentions scripts;; 1 = vague;; 0 = none.
- **EX005 — Pre-registration.** Why pre-register hypotheses? *Rubric:* 3 = to avoid reshaping them after results;; 2 = mentions bias;; 1 = vague;; 0 = none.
- **EX006 — Two hypotheses.** State one pre-registered hypothesis. *Rubric:* 3 = unclear rights cause inconsistent thresholds; thresholds shift counts;; 2 = one;; 1 = vague;; 0 = none.
- **EX007 — ISO model.** Where does ISO/IEC 38505-1 place accountability? *Rubric:* 3 = with the governing body;; 2 = partly correct;; 1 = managers;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue studying — lesson 01 (chapter 01 of 08)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Data governance: research frontier

### Learning outcomes

You will (1) review current debates in data governance research; (2) measure data quality dimensions on a synthetic register; (3) identify a gap for original work.

### 2.1 The state of the field

Nadia reviews the literature. Early work treated data quality as accuracy alone; Wang and Strong showed that data consumers also care about timeliness, relevance, accessibility and interpretability. Batini and colleagues compared assessment methodologies and found that most define dimensions, measure them and propose improvements, but differ in which dimensions they choose and how they weigh them. ISO 8000-8 sets out concepts and prerequisites for measuring information and data quality. Nadia notes that measurement methods are well developed, while research on who decides quality rules is thinner.

### 2.2 Measuring a register

To ground her review, Nadia measures three dimensions on a synthetic register of 5,000 businesses. The lab reports completeness of 0.798, validity of 0.937 and uniqueness of 0.966. Completeness is lowest because many records lack a sector code or postcode. Validity failures come from postcodes with letters and an unknown sector code. Uniqueness falls below one because some registration numbers appear twice. Each figure depends on a rule someone chose, such as whether a blank sector counts as missing or as a legitimate value. Rules matter as much.

### 2.3 Rules are decisions

Nadia shows Prof. Eriksen how the completeness score changes if blank sectors are allowed for newly registered firms. The number rises, although no record has changed. She argues that quality scores are partly governance outputs: they reflect decisions about rules, thresholds and exceptions. DAMA-DMBOK2 places data quality management within a governance framework for this reason. Nadia's literature map shows few empirical studies that trace how such rule decisions are made and how they shift published figures, which is the gap she will address.

### 2.4 Positioning the contribution

Nadia writes a positioning statement: existing research measures quality and proposes governance structures, but rarely links the two quantitatively in an official statistics setting. Her contribution will be a method that records decision rights, applies alternative rules on a synthetic replica and measures the effect on outputs. Prof. Eriksen challenges her to show why this matters beyond Westmark. She answers that any organisation publishing indicators from administrative data faces the same question of who decides what counts as good enough data. Westmark is the test case.

### Lab — Quality dimensions of a synthetic business register

```python
"""Score completeness, validity and uniqueness of a synthetic business register (stdlib only)."""
import random, re
random.seed(3)
rows = []
for i in range(5000):
    reg = f"BR{i:06d}"
    if random.random() < 0.03: reg = f"BR{random.randint(0, i):06d}"      # duplicate ids
    post = f"{random.randint(1000, 9999)}" if random.random() > 0.08 else ""
    if random.random() < 0.04: post = "ABCD"                                # invalid
    sector = random.choice(["A", "C", "F", "G", "J", "M", ""]) if random.random() > 0.02 else "Z9"
    rows.append((reg, post, sector))
n = len(rows)
complete = sum(1 for r in rows if r[1] and r[2]) / n
valid = sum(1 for r in rows if re.fullmatch(r"\d{4}", r[1] or "0000") and r[2] in {"A","C","F","G","J","M",""}) / n
unique = len({r[0] for r in rows}) / n
print(f"records {n}")
print(f"completeness {complete:.3f}  validity {valid:.3f}  uniqueness {unique:.3f}")
```

Run with `python3 lab_quality.py`. Verified output:

```text
records 5000
completeness 0.798  validity 0.937  uniqueness 0.966
```

### Worked example

Nadia reviews quality literature, measures completeness 0.798, validity 0.937 and uniqueness 0.966 on 5,000 synthetic records, shows that rule choices move scores and positions her contribution.

> **Synthetic case.** The register is synthetic; Wang and Strong (1996), Batini et al. (2009), ISO 8000-8:2015 and DAMA-DMBOK2 are real.

### Errors and limits

Dimension scores depend on rule definitions; publish the rules with the scores.

### Exercises

- **EX008 — Beyond accuracy.** What did Wang and Strong add to accuracy? *Rubric:* 3 = timeliness, relevance, accessibility, interpretability;; 2 = two;; 1 = one;; 0 = none.
- **EX009 — Completeness.** What completeness score did the lab report? *Rubric:* 3 = 0.798;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX010 — Lowest cause.** Why is completeness lowest? *Rubric:* 3 = missing sector codes or postcodes;; 2 = mentions missing;; 1 = vague;; 0 = none.
- **EX011 — Uniqueness cause.** Why is uniqueness below one? *Rubric:* 3 = duplicated registration numbers;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX012 — Score change.** Why did completeness rise without any record changing? *Rubric:* 3 = the rule for blank sectors changed;; 2 = mentions rule;; 1 = vague;; 0 = none.
- **EX013 — ISO 8000 role.** What does ISO 8000-8 provide? *Rubric:* 3 = concepts and prerequisites for measuring data quality;; 2 = mentions measuring;; 1 = vague;; 0 = none.
- **EX014 — Research gap.** What gap does Nadia address? *Rubric:* 3 = how rule decisions are made and shift published figures;; 2 = mentions decisions;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue studying — lesson 02 (chapter 02 of 08)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes

You will (1) write a doctoral proposal with testable claims; (2) define measures and decision-rights variables; (3) plan ethics and access.

### 3.1 The proposal

Nadia's proposal has three claims. First, Westmark's decision rights over quality rules and linkage thresholds can be described with a matrix of roles and decisions, following Khatri and Brown's domains. Second, alternative decisions within plausible ranges change regional employment counts by amounts that matter to users. Third, a documented decision process reduces unexplained variation between releases. Each claim names its evidence: the matrix from interviews and documents, the effect sizes from simulation on the synthetic replica, and the variation from comparing releases before and after documentation.

### 3.2 Measures

For outputs, Nadia measures regional employment counts and their change between releases. For linkage, she measures precision and recall, defined as the share of linked pairs that are true matches and the share of true matches that are linked. For quality, she uses the dimensions from Chapter 2. For governance, she codes each decision by who made it, whether it was documented and whether it was reviewed. Prof. Eriksen asks her to define every measure before running anything, so measures cannot drift toward convenient results.

### 3.3 Ethics and access

Interviews involve Westmark staff, who might fear criticism of their decisions. Nadia's ethics application promises anonymity, the right to withdraw, review of quotations and storage of recordings on encrypted university systems, deleted after transcription. Access to Westmark's documents is governed by a written agreement that excludes confidential microdata and allows publication of aggregate findings after a review for accuracy, not for content. She notes that a review for content would compromise independence, so the agreement limits Westmark's review to factual errors. Westmark signs it.

### 3.4 Feasibility

Nadia plans the work across two years: six months for the replica, the decision matrix and the baseline; six months for the main simulation and interviews; six months for validation and the release comparison; and six months for writing and defence. She identifies risks such as delayed interviews and plans fallback analyses that rely on documents alone. Prof. Eriksen approves the proposal after asking her to narrow the release comparison to two indicators, which makes the validation stage achievable within the time available.

### Worked example

Nadia proposes three testable claims, defines output, linkage, quality and governance measures, secures ethics with anonymity and a factual-only review clause and plans a feasible two-year schedule.

> **Synthetic case.** The proposal is synthetic; Khatri and Brown (2010) are real.

### Errors and limits

Proposals that promise too much fail at validation; narrow scope early.

### Exercises

- **EX015 — Three claims.** State one of Nadia's claims. *Rubric:* 3 = decision rights matrix; decisions change counts; documentation reduces variation;; 2 = one;; 1 = vague;; 0 = none.
- **EX016 — Precision.** Define precision in linkage. *Rubric:* 3 = share of linked pairs that are true matches;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX017 — Recall.** Define recall in linkage. *Rubric:* 3 = share of true matches that are linked;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX018 — Coding decisions.** How is each governance decision coded? *Rubric:* 3 = who made it, documented, reviewed;; 2 = most;; 1 = one;; 0 = none.
- **EX019 — Review clause.** What may Westmark review before publication? *Rubric:* 3 = factual accuracy only;; 2 = partly correct;; 1 = content;; 0 = none.
- **EX020 — Narrowing.** How did Prof. Eriksen narrow the plan? *Rubric:* 3 = release comparison limited to two indicators;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue studying — lesson 03 (chapter 03 of 08)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes

You will (1) replicate a record linkage baseline; (2) compute match weights and thresholds; (3) report the trade-off between precision and recall.

### 4.1 Why replicate first

Before testing her own ideas, Nadia replicates Westmark's published linkage method on the synthetic replica. Westmark uses a Fellegi and Sunter approach: each field contributes a weight based on m, the probability that a true match agrees on the field, and u, the probability that a non-match agrees by chance. Agreement adds the logarithm of m over u; disagreement adds the logarithm of one minus m over one minus u. Replicating the baseline proves that her tools reproduce the method before she varies the decisions within it.

### 4.2 The pilot lab

The pilot uses 4,000 synthetic record pairs, 400 of them true matches, with name, postcode and sector fields. At a threshold of 0, it links 505 pairs with precision 0.776 and recall 0.980. At a threshold of 4, it links 386 pairs with precision 0.953 and recall 0.920. At a threshold of 8, it links 338 pairs with precision 0.991 and recall 0.838. Raising the threshold removes false matches but loses true ones, so no threshold is free of error. Between thresholds 0 and 4, precision gains far more than recall loses, which suggests the lowest threshold links too many false pairs. Beyond 4, each gain in precision costs noticeably more recall.

### 4.3 Who chooses the threshold

Nadia asks Westmark staff who chose the current threshold. The answer is unclear: a methodologist set it years ago, and later releases reused it without review. Interviews suggest that the production team believes the methods team owns it, while the methods team believes production can adjust it. This is exactly the decision-rights gap her proposal anticipated. She records the finding in her decision matrix and notes that the threshold affects every regional employment count Westmark publishes. Neither team had a written mandate covering the decision.

### 4.4 Pilot lessons

The pilot shows that the replica and scripts work, that the precision and recall trade-off is substantial and that ownership of the threshold is unclear. It also reveals that m and u values were estimated once and never updated, although the register has changed. Prof. Eriksen asks Nadia to treat the m and u estimates as another governance decision in the main study. She updates her pre-registration log to note the addition before running the main study, keeping the change transparent. Transparency comes first.

### Lab — Match weights, thresholds, precision and recall

```python
"""Fellegi-Sunter style match weights on synthetic record pairs; precision and recall by threshold (stdlib only)."""
import random, math
random.seed(9)
fields = {"name": (0.95, 0.01), "postcode": (0.90, 0.05), "sector": (0.85, 0.20)}  # (m, u)
pairs = []
for i in range(4000):
    match = i < 400
    agree = {f: (random.random() < (m if match else u)) for f, (m, u) in fields.items()}
    w = sum(math.log2(m / u) if agree[f] else math.log2((1 - m) / (1 - u)) for f, (m, u) in fields.items())
    pairs.append((w, match))
for t in (0, 4, 8):
    pred = [p for p in pairs if p[0] >= t]; tp = sum(1 for p in pred if p[1])
    print(f"threshold {t:2d}: linked {len(pred):4d}  precision {tp/len(pred):.3f}  recall {tp/400:.3f}")
```

Run with `python3 lab_linkage.py`. Verified output:

```text
threshold  0: linked  505  precision 0.776  recall 0.980
threshold  4: linked  386  precision 0.953  recall 0.920
threshold  8: linked  338  precision 0.991  recall 0.838
```

### Worked example

Nadia replicates Fellegi-Sunter weights on 4,000 synthetic pairs, reports precision from 0.776 to 0.991 and recall from 0.980 to 0.838 across thresholds and finds unclear ownership of the threshold.

> **Synthetic case.** Pairs are synthetic; Fellegi and Sunter (1969) is real.

### Errors and limits

Assuming field independence, as this pilot does, can distort weights; test it later.

### Exercises

- **EX021 — Weight formula.** What does agreement on a field add to the weight? *Rubric:* 3 = log of m over u;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX022 — Threshold 4.** What precision and recall occur at threshold 4? *Rubric:* 3 = 0.953 and 0.920;; 2 = both;; 1 = one;; 0 = none.
- **EX023 — Higher threshold.** What happens when the threshold rises to 8? *Rubric:* 3 = fewer false matches, more missed true ones;; 2 = mentions trade-off;; 1 = vague;; 0 = none.
- **EX024 — Unclear owner.** Who owns the threshold at Westmark? *Rubric:* 3 = unclear; teams point to each other;; 2 = mentions unclear;; 1 = names one;; 0 = none.
- **EX025 — Stale estimates.** What else had never been updated? *Rubric:* 3 = m and u estimates;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX026 — Log update.** What did Nadia do before adding the new variable? *Rubric:* 3 = updated her pre-registration log;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue studying — lesson 04 (chapter 04 of 08)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes

You will (1) run the main simulation of governance decisions; (2) measure effects on published counts; (3) validate results independently.

### 5.1 Designing the main study

The main study varies three decisions within ranges that Westmark staff described as plausible: the linkage threshold from 0 to 8, whether m and u are re-estimated each year, and whether blank sector codes are imputed or left blank. Each combination produces a synthetic set of regional employment counts. Nadia runs every combination with fixed random seeds and stores outputs with the script version. She compares each result with a reference produced by the true synthetic links, which are known because she generated the data herself.

### 5.2 Effects on counts

The results show that the threshold has the largest effect. At low thresholds, false links inflate employment in regions with many similarly named firms. At high thresholds, missed links deflate counts in regions where postcodes change often. Re-estimating m and u reduces both errors. Imputing sector codes shifts employment between sectors but barely changes regional totals. Nadia expresses each effect as the difference from the reference, so readers can see which decisions matter most and for which regions. Small regions show the largest relative errors.

### 5.3 Independent validation

To validate, Prof. Eriksen arranges for a researcher at another university, who has not seen Nadia's code, to implement the method from her written description and run it on a fresh synthetic replica generated with a different seed. The independent results agree in direction and approximate size for all three decisions. One discrepancy arises because Nadia's description omitted how ties at the threshold were treated. She corrects the description, showing how validation improves documentation as well as confidence in the results. Both runs are archived.

### 5.4 Interpreting the findings

Nadia relates the findings to governance. The decision with the largest effect, the threshold, is also the one with the least clear ownership. The decision with the smallest effect on regional totals, sector imputation, has the most documentation, because it appears in a published manual. She argues that governance attention at Westmark has followed visibility rather than impact. Prof. Eriksen warns her to avoid generalising from one organisation, and she frames the claim as a hypothesis for other statistics offices to test.

### Worked example

Nadia varies threshold, re-estimation and imputation, finds the threshold has the largest effect on regional counts, has an independent researcher reproduce the direction and size of effects and links impact to unclear ownership.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Plausible ranges come from interviews; other organisations may use wider ranges.

### Exercises

- **EX027 — Three decisions.** Name the three decisions varied. *Rubric:* 3 = threshold, m and u re-estimation, sector imputation;; 2 = all;; 1 = one;; 0 = none.
- **EX028 — Largest effect.** Which decision had the largest effect? *Rubric:* 3 = the linkage threshold;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX029 — Low threshold.** What happens to counts at low thresholds? *Rubric:* 3 = false links inflate counts;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX030 — Validation method.** How was validation independent? *Rubric:* 3 = another researcher reimplemented from the description with a new seed;; 2 = mentions reimplementation;; 1 = vague;; 0 = none.
- **EX031 — Discrepancy.** What caused the validation discrepancy? *Rubric:* 3 = undocumented tie handling at the threshold;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX032 — Attention.** What has governance attention followed at Westmark? *Rubric:* 3 = visibility rather than impact;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 08)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes

You will (1) respond to peer critique of governance research; (2) revise analyses transparently; (3) strengthen limitations.

### 6.1 The critique

Nadia presents her results at a doctoral workshop. Peers raise three critiques. First, the synthetic replica may understate real-world name variation, which would change linkage error. Second, interviews with Westmark staff may reflect blame avoidance, since nobody wants to admit owning a poorly chosen threshold. Third, the claim that documentation reduces variation rests on only two releases. Prof. Eriksen tells her that good critique is a gift, because it identifies weaknesses before examiners or users find them. She writes each critique down verbatim.

### 6.2 Responding to name variation

Nadia adds a sensitivity analysis in which name agreement is less reliable, lowering m for names from 0.95 to 0.85. Linkage error rises at every threshold, but the ranking of decisions by effect remains the same. She reports both versions and explains that the size of effects is uncertain while the ranking is robust. She also notes that NIST SP 800-188 discusses how synthetic data may preserve some properties and not others, so analysts must state which properties they relied on. Both analyses are archived together.

### 6.3 Responding to interview bias

To address possible blame avoidance, Nadia compares interview answers with documents such as release notes, meeting minutes and change requests. Documents confirm that no record exists of a threshold review since the original choice. They also show that the methods team proposed a review two years ago that was never scheduled. Triangulation strengthens the finding that ownership was unclear, while softening any suggestion that individuals ignored the issue. She revises her wording to describe a structural gap rather than personal failure. Documents settle it.

### 6.4 Limiting the documentation claim

With only two releases, Nadia cannot show that documentation causes reduced variation. She rewrites the third claim as an observation consistent with the hypothesis and proposes a follow-up design in which Westmark documents decisions for four releases while a comparison series continues without documentation. Prof. Eriksen approves the revision. Nadia records every change in her decision log, including the original wording, so that examiners can see how the thesis responded to critique rather than quietly shifting its claims. Examiners value this honesty highly.

### Worked example

Nadia answers critiques with a sensitivity analysis on name agreement, triangulates interviews with documents and reframes the documentation claim as consistent but not causal.

> **Synthetic case.** The workshop is synthetic; NIST SP 800-188 is real.

### Errors and limits

Sensitivity analyses test chosen alternatives only; others may matter.

### Exercises

- **EX033 — Name critique.** What critique concerned names? *Rubric:* 3 = replica may understate name variation;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX034 — Sensitivity change.** How did Nadia test name variation? *Rubric:* 3 = lowered m for names from 0.95 to 0.85;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX035 — Robust result.** What stayed the same in the sensitivity analysis? *Rubric:* 3 = the ranking of decisions by effect;; 2 = partly correct;; 1 = sizes;; 0 = none.
- **EX036 — Triangulation.** What did documents show about threshold reviews? *Rubric:* 3 = none since the original choice; a proposal never scheduled;; 2 = both;; 1 = one;; 0 = no answer.
- **EX037 — Structural wording.** How did Nadia revise her wording on ownership? *Rubric:* 3 = a structural gap, not personal failure;; 2 = partly correct;; 1 = blame;; 0 = none.
- **EX038 — Follow-up design.** What follow-up did Nadia propose? *Rubric:* 3 = four documented releases against a comparison series;; 2 = mentions comparison;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 08)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes

You will (1) synthesise findings into a coherent thesis; (2) build a reproducibility archive; (3) assess the archive against FAIR principles.

### 7.1 The thesis argument

Nadia's thesis argues that, in the setting studied, governance decisions about linkage and quality rules shape official statistics as much as data collection does, and that the most influential decisions received the least governance attention. Each chapter supports one step: the decision matrix, the baseline replication, the main simulation, the validation and the critique response. She writes the argument on one page before revising chapters, so that every section contributes to the claim and nothing is included simply because it was work she did.

### 7.2 The reproducibility archive

Nadia builds an archive containing the replica generator, analysis scripts, fixed seeds, expected outputs, the decision log, interview protocol and anonymised coding frame. Confidential material, including any Westmark internal documents, is excluded and described instead. Wilkinson and colleagues' FAIR principles state that data and metadata should be findable, accessible, interoperable and reusable, with persistent identifiers, rich metadata, standard vocabularies, clear licences and provenance. She treats the principles as design goals for the archive rather than as a certificate it either has or lacks.

### 7.3 Checking FAIR properties

To test her archive against those goals, Nadia scores four synthetic dataset records using an eight-item checklist. The lab reports that the business register record meets 8 of 8 items, the linked employment record 4 of 8, the trade survey 4 of 8 and the pilot extract 1 of 8, a mean score of 0.53. The linked employment record lacks a persistent identifier, search index entry, standard vocabulary and licence, which would make reuse difficult even for colleagues inside Westmark. The pilot extract meets only the open protocol item, which is typical of files produced quickly for a test and never described afterwards. Such files are the first to become unusable.

### 7.4 Improving the archive

Nadia applies the lessons to her own archive. She obtains a persistent identifier through the university repository, writes metadata describing variables with standard codes, chooses an open licence for code and synthetic data and documents provenance from generator to figure. Access conditions state that confidential microdata are not included and how researchers can apply to Westmark separately. Prof. Eriksen tests the archive by asking a new student to regenerate two figures; the student succeeds without help in an afternoon. No step required her help.

### Lab — FAIR checklist scores for dataset records

```python
"""Score synthetic dataset metadata records against a simple FAIR checklist (stdlib only)."""
checks = ["persistent_id", "rich_metadata", "searchable_index", "open_protocol", "access_conditions",
          "standard_vocabulary", "licence", "provenance"]
sets = {
    "business_register_2025": {"persistent_id", "rich_metadata", "searchable_index", "open_protocol", "licence", "provenance", "standard_vocabulary", "access_conditions"},
    "linked_employment_2024": {"rich_metadata", "open_protocol", "access_conditions", "provenance"},
    "trade_survey_2023":      {"persistent_id", "searchable_index", "open_protocol", "licence"},
    "pilot_linkage_extract":  {"open_protocol"},
}
for name, have in sets.items():
    miss = [c for c in checks if c not in have]
    print(f"{name:24s} {len(have)}/{len(checks)}  missing: {', '.join(miss) if miss else '-'}")
avg = sum(len(h) for h in sets.values()) / (len(sets) * len(checks))
print(f"mean checklist score {avg:.2f}")
```

Run with `python3 lab_fair.py`. Verified output:

```text
business_register_2025   8/8  missing: -
linked_employment_2024   4/8  missing: persistent_id, searchable_index, standard_vocabulary, licence
trade_survey_2023        4/8  missing: rich_metadata, access_conditions, standard_vocabulary, provenance
pilot_linkage_extract    1/8  missing: persistent_id, rich_metadata, searchable_index, access_conditions, standard_vocabulary, licence, provenance
mean checklist score 0.53
```

### Worked example

Nadia writes a one-page thesis argument, builds an archive excluding confidential material, scores four synthetic records from 8 of 8 to 1 of 8 (mean 0.53) and improves her archive until a new student regenerates figures unaided.

> **Synthetic case.** Dataset records are synthetic; Wilkinson et al. (2016) is real.

### Errors and limits

A checklist simplifies FAIR principles; some items need judgement, not ticks.

### Exercises

- **EX039 — Thesis claim.** What is the core thesis claim? *Rubric:* 3 = governance decisions shape statistics; influential ones get least attention;; 2 = mentions attention;; 1 = vague;; 0 = none.
- **EX040 — FAIR letters.** What do the FAIR letters stand for? *Rubric:* 3 = findable, accessible, interoperable, reusable;; 2 = all;; 1 = two;; 0 = none.
- **EX041 — Linked record.** What score did the linked employment record get? *Rubric:* 3 = 4 of 8;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX042 — Mean score.** What was the mean checklist score? *Rubric:* 3 = 0.53;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX043 — Excluded content.** What does Nadia exclude from the archive? *Rubric:* 3 = confidential Westmark material;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX044 — Archive test.** How did Prof. Eriksen test the archive? *Rubric:* 3 = a new student regenerated two figures;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 08)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes

You will (1) defend governance research before examiners; (2) plan publication responsibly; (3) transfer findings to practice.

### 8.1 Preparing the defense

Nadia prepares by listing the hardest questions she expects: why a synthetic replica is credible, whether one organisation can support general claims, how interview bias was handled and what Westmark should do differently. For each, she writes a short answer citing her evidence and a limit she accepts. Prof. Eriksen runs a mock defense in which he plays a sceptical examiner and presses her on the precision and recall trade-off until she can explain it without slides. Each answer fits on one card.

### 8.2 The defense

At the defense, the external examiner asks why Westmark should not simply choose the threshold that maximises precision. Nadia explains that maximising precision lowers recall and undercounts regions with unstable postcodes, so the choice depends on which error users can tolerate, which is a governance decision rather than a technical fact. The examiner also asks about the reproducibility archive and regenerates a figure during the session. The examiners pass the thesis with minor corrections to the limitations chapter. The corrections take two weeks.

### 8.3 Publication plan

Nadia plans three papers: a methods paper on simulating governance decisions, an empirical paper on decision rights at a statistics office and a short practice note for official statisticians. Each paper links to the archive. Westmark reviews drafts for factual accuracy as agreed, and requests no content changes. She chooses open-access venues where possible, because her findings concern public statistics and should be readable by the people who rely on them, not only by subscribers. The practice note comes first, because Westmark's next release cycle starts within months.

### 8.4 Transfer to practice

Nadia presents a summary to Westmark's governing board. She recommends naming an owner for the linkage threshold, reviewing m and u estimates each year, documenting each release's decisions and publishing precision and recall estimates alongside regional counts. The board accepts the first three and asks for a pilot of the fourth. Prof. Eriksen notes that the strongest sign of a useful thesis is that its recommendations can be checked: next year's release will show whether they were adopted. Nadia offers to review the pilot.

### Worked example

Nadia rehearses hard questions, defends the threshold choice as a governance decision, plans three papers with an open archive and recommends threshold ownership, annual re-estimation, documentation and published error estimates.

> **Synthetic case.** The defense and board are synthetic.

### Errors and limits

Publication timelines slip; prioritise the paper that most affects practice.

### Exercises

- **EX045 — Precision question.** Why not just maximise precision? *Rubric:* 3 = recall falls and some regions are undercounted;; 2 = mentions recall;; 1 = vague;; 0 = none.
- **EX046 — Governance choice.** What kind of decision is choosing tolerable error? *Rubric:* 3 = a governance decision;; 2 = partly correct;; 1 = technical;; 0 = none.
- **EX047 — Defense result.** What was the defense outcome? *Rubric:* 3 = pass with minor corrections;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX048 — Papers.** How many papers does Nadia plan? *Rubric:* 3 = three;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX049 — Board decisions.** Which recommendation did the board pilot rather than adopt? *Rubric:* 3 = publishing precision and recall estimates;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX050 — Checkable advice.** Why are checkable recommendations valuable? *Rubric:* 3 = next release shows adoption;; 2 = mentions verification;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 08)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Nadia Rahman, Prof. Lars Eriksen, Halvorsen University, Westmark Statistics Office and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** How decisions about quality rules and linkage thresholds change the statistics people read.

**EX002.** As deciding who holds decision rights over data.

**EX003.** Only a synthetic replica built from published distributions.

**EX004.** Each figure must trace to a version-controlled script run.

**EX005.** So hypotheses cannot be reshaped after seeing results.

**EX006.** Unclear decision rights lead to inconsistent linkage thresholds across releases.

**EX007.** With the organisation's governing body.

**EX008.** Dimensions such as timeliness and relevance that consumers value.

**EX009.** 0.798.

**EX010.** Many records lack a sector code or postcode.

**EX011.** Some registration numbers appear twice.

**EX012.** Allowing blank sectors for new firms changed the rule, not the data.

**EX013.** Concepts and prerequisites for measuring information and data quality.

**EX014.** Empirical links between quality rule decisions and published outputs.

**EX015.** Alternative linkage decisions change regional employment counts meaningfully.

**EX016.** The share of linked pairs that are true matches.

**EX017.** The share of true matches that are linked.

**EX018.** By who made it, whether documented and whether reviewed.

**EX019.** Only factual accuracy, not content.

**EX020.** He limited the release comparison to two indicators.

**EX021.** The logarithm of m divided by u.

**EX022.** Precision 0.953 and recall 0.920.

**EX023.** Precision rises to 0.991 but recall falls to 0.838.

**EX024.** Nobody clearly; each team believes the other owns it.

**EX025.** The m and u probability estimates.

**EX026.** She updated her pre-registration log first.

**EX027.** Linkage threshold, re-estimation of m and u, and sector imputation.

**EX028.** The linkage threshold.

**EX029.** False links inflate employment in some regions.

**EX030.** A researcher reimplemented the method from her description on a new replica.

**EX031.** Her description omitted how ties at the threshold were handled.

**EX032.** Visibility, not impact.

**EX033.** The replica may understate real name variation.

**EX034.** She lowered the name m value from 0.95 to 0.85.

**EX035.** The ranking of decisions by effect.

**EX036.** No review since the original choice, and a proposed review was never scheduled.

**EX037.** As a structural gap rather than personal failure.

**EX038.** Documenting four releases while a comparison series continues undocumented.

**EX039.** Influential governance decisions shape statistics yet receive the least attention.

**EX040.** Findable, accessible, interoperable and reusable.

**EX041.** Four of eight.

**EX042.** 0.53.

**EX043.** Confidential material such as internal documents.

**EX044.** A new student regenerated two figures unaided.

**EX045.** Higher precision lowers recall and undercounts regions with unstable postcodes.

**EX046.** A governance decision about which error users can accept.

**EX047.** A pass with minor corrections to the limitations chapter.

**EX048.** Three.

**EX049.** Publishing precision and recall estimates alongside counts.

**EX050.** The next release will show whether they were adopted.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and standards were checked against their publisher pages. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009). Methodologies for data quality assessment and improvement. *ACM Computing Surveys, 41*(3), 1–52. https://doi.org/10.1145/1541880.1541883
- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- Fellegi, I. P., & Sunter, A. B. (1969). A theory for record linkage. *Journal of the American Statistical Association, 64*(328), 1183–1210. https://doi.org/10.1080/01621459.1969.10501049
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-188
- ISO. (2015). *ISO 8000-8:2015 Data quality — Part 8: Information and data quality: Concepts and measuring*. International Organization for Standardization. <https://www.iso.org/standard/60805.html>
- ISO/IEC. (2017). *ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data — Part 1: Application of ISO/IEC 38500 to the governance of data*. <https://www.iso.org/standard/56639.html>
- Khatri, V., & Brown, C. V. (2010). Designing data governance. *Communications of the ACM, 53*(1), 148–152. https://doi.org/10.1145/1629175.1629210
- Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. *Journal of Management Information Systems, 12*(4), 5–33. https://doi.org/10.1080/07421222.1996.11518099
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., et al. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. https://doi.org/10.1038/sdata.2016.18
