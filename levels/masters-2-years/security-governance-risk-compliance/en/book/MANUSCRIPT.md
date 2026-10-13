# Security Governance, Risk and Compliance: Master's Course

- Language: English (`en`); course 166, Master's course (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students evaluating whether a governance control change improves a measurable security outcome.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs compute requirement-to-evidence coverage, exact attribute-sampling bounds and a bootstrap difference in excess-access rates on synthetic data; no real accounts, employees or audits are involved. Mappings and audit-style tests here are teaching illustrations, not real attestations or legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one master's student studying whether quarterly access review reduces excess access: the question and literature, the framework seminar, design and ethics, rival explanations, proposal and pilot, data and analysis, writing and limitations, and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lucas Ferreira** | Master's student | Invented |
| **Dr. Ingrid Solberg** | Supervisor | Invented |
| **Marlow Institute of Technology** | Fictional university | Invented |
| **Tessaly Logistics** | Fictional ISO/IEC 27001-certified company with 1,200 staff | Invented |

### Core sources

ISO/IEC 27001:2022 and 27002:2022; NIST [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5); NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); COBIT 2019; Spears and Barki (2010), [doi:10.2307/25750689](https://doi.org/10.2307/25750689); Gordon and Loeb (2002), [doi:10.1145/581271.581274](https://doi.org/10.1145/581271.581274); Wohlin et al. (2012). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn a governance concern into a researchable question; (2) search and screen literature systematically; (3) record sources so others can repeat the search.

### 1.1 From concern to question

Lucas Ferreira, a master's student at the fictional Marlow Institute of Technology, works part time in the security office of Tessaly Logistics, a fictional company with 1,200 staff and an ISO/IEC 27001:2022 certified management system. Auditors keep finding staff with access they no longer need. His manager asks whether reviewing access every quarter instead of every year would help. Lucas turns this into a research question: in Tessaly's business units, is quarterly access review associated with a lower rate of excess access than annual review, and at what cost in reviewer time?

### 1.2 Making it answerable

His supervisor, Dr. Ingrid Solberg, pushes for precision. Excess access must be defined: an account holding a permission that its owner's current role does not require, judged against a written role catalogue. The unit of analysis is the account, not the person. The outcome is measured at one point in time by an independent reviewer. Cost is the hours reviewers log. Lucas also writes down what the study cannot show: it is observational, because units chose their review frequency, so any difference may reflect other unit traits.

### 1.3 Searching systematically

Lucas searches two academic databases and standards bodies' sites with a written search string combining access review, entitlement, recertification and audit findings. He records the date, database, string and number of hits for each search in a log. He screens titles and abstracts against inclusion rules: empirical or standards sources about periodic access review or control effectiveness in organisations. He keeps a list of excluded items with reasons. This log lets Dr. Solberg, or anyone else, repeat the search and see whether Lucas missed relevant work.

### 1.4 Reading standards as sources

Standards are a special kind of literature. ISO/IEC 27002:2022 provides guidance on access rights, including review of rights at planned intervals, but does not prescribe a frequency. NIST SP 800-53 Rev. 5 includes an account management control whose review frequency is set by the organisation. Lucas notes that standards express consensus good practice, not tested effects, so they define the question but cannot answer it. He paraphrases rather than copies them and cites each by edition so readers know exactly which text he means.

### Worked example

Lucas defines excess access against a role catalogue, logs reproducible searches and treats standards as context rather than evidence of effect.

> **Synthetic case.** Tessaly, Marlow and all data are synthetic; ISO/IEC 27002:2022 and SP 800-53 Rev. 5 are real.

### Errors and limits

Observational designs cannot prove cause. Search logs miss grey literature.

### Exercises

- **EX001 — Unit of analysis.** What is the unit of analysis in Lucas's study? *Rubric:* 3 = the account;; 2 = accounts;; 1 = people;; 0 = none.
- **EX002 — Excess definition.** How is excess access defined? *Rubric:* 3 = a permission the owner's current role does not need, per the role catalogue;; 2 = role catalogue;; 1 = none;; 0 = none.
- **EX003 — Cost measure.** How does Lucas measure cost? *Rubric:* 3 = reviewer hours logged;; 2 = hours;; 1 = none;; 0 = none.
- **EX004 — Design limit.** Why can the study not prove cause? *Rubric:* 3 = units chose their review frequency;; 2 = observational;; 1 = none;; 0 = none.
- **EX005 — Search log fields.** What does Lucas record for each search? *Rubric:* 3 = date, database, string and hit count;; 2 = log;; 1 = none;; 0 = none.
- **EX006 — Frequency guidance.** Does ISO/IEC 27002:2022 prescribe a review frequency? *Rubric:* 3 = no, it asks for planned intervals;; 2 = no;; 1 = yes;; 0 = none.
- **EX007 — Standards role.** What can standards do for this question? *Rubric:* 3 = define it but not answer it;; 2 = context;; 1 = evidence of effect;; 0 = none.

### Synthesis

A precise, answerable question and a reproducible search come before any data.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Security governance, risk and compliance: advanced seminar

### Learning outcomes

You will (1) compare major governance and control frameworks; (2) analyse requirement-to-control-to-evidence coverage; (3) present a critical seminar argument.

### 2.1 Framework landscape

In the seminar, Lucas compares frameworks. ISO/IEC 27001:2022 specifies requirements for an information security management system and lists reference controls in Annex A drawn from ISO/IEC 27002:2022. NIST CSF 2.0 organises outcomes under six functions, including the new Govern function. COBIT 2019 addresses governance of enterprise information and technology, separating governance from management. NIST SP 800-53 Rev. 5 offers a detailed control catalogue. He notes that these frameworks overlap heavily but differ in purpose, granularity and whether they can be certified. He keeps a table of these differences for later chapters.

### 2.2 Coverage analysis

Compliance often asks whether every requirement has a control and evidence that the control works. Lucas builds a small synthetic example for Tessaly: ten policy requirements, eight controls and a record of whether each control has current evidence. The lab finds eight requirements mapped to at least one control but only six with evidence; two requirements are unmapped and two are mapped to controls with no evidence. Coverage is therefore 80% on paper but only 60% in demonstrable terms, a gap auditors are likely to find.

### Lab — Requirement, control and evidence coverage

```python
"""Requirement-to-control-to-evidence coverage on synthetic data (stdlib only)."""
reqs = {"R1": ["C1"], "R2": ["C2", "C3"], "R3": [], "R4": ["C4"], "R5": ["C5"],
        "R6": ["C6"], "R7": ["C2"], "R8": [], "R9": ["C7"], "R10": ["C8"]}
evidence = {"C1": True, "C2": True, "C3": False, "C4": True, "C5": False,
            "C6": True, "C7": True, "C8": False}
mapped = [r for r, c in reqs.items() if c]
evidenced = [r for r in mapped if any(evidence[c] for c in reqs[r])]
print(f"requirements {len(reqs)}; mapped {len(mapped)}; evidenced {len(evidenced)}")
print("unmapped:", ", ".join(r for r, c in reqs.items() if not c))
print("mapped but no evidence:", ", ".join(r for r in mapped if r not in evidenced))
print(f"coverage mapped {len(mapped)/len(reqs):.0%}; evidenced {len(evidenced)/len(reqs):.0%}")
```

Run with `python3 lab_map.py`. Verified output:

```text
requirements 10; mapped 8; evidenced 6
unmapped: R3, R8
mapped but no evidence: R5, R10
coverage mapped 80%; evidenced 60%
```

### 2.3 Critique of mapping

Lucas argues in his seminar paper that mapping can create an illusion of assurance. A requirement mapped to a control looks covered, but the control may be badly designed, poorly operated or evidenced by a document no one checks. Spears and Barki (2010) found that involving business users in security risk management improved alignment with business processes, which suggests coverage depends on people as well as tables. He recommends that mappings record evidence quality and date, not just a link, so that gaps stay visible.

### 2.4 Seminar discussion

Classmates challenge him. One argues that mapping is still valuable because it reveals unmapped requirements, such as R3 and R8 in the lab, which would otherwise be forgotten. Another notes that evidence checks cost time, so organisations sample instead of checking everything. Lucas accepts both points and refines his claim: mapping is a necessary first step, but assurance requires tested evidence, and the depth of testing should follow risk. This refinement links his seminar to his thesis question about access reviews.

### Worked example

Lucas compares four frameworks, finds 80% mapped but 60% evidenced coverage and argues that assurance needs tested evidence.

> **Synthetic case.** The coverage data are synthetic; the frameworks are real.

### Errors and limits

Coverage percentages hide control quality. Frameworks change editions.

### Exercises

- **EX008 — Certifiable standard.** Which of the frameworks discussed specifies certifiable ISMS requirements? *Rubric:* 3 = ISO/IEC 27001:2022;; 2 = 27001;; 1 = CSF;; 0 = none.
- **EX009 — COBIT separation.** What does COBIT 2019 separate? *Rubric:* 3 = governance from management;; 2 = governance;; 1 = none;; 0 = none.
- **EX010 — Mapped count.** How many requirements did the lab find mapped? *Rubric:* 3 = eight of ten;; 2 = 8;; 1 = 10;; 0 = none.
- **EX011 — Evidenced coverage.** What share of requirements had evidence? *Rubric:* 3 = 60%;; 2 = six;; 1 = 80%;; 0 = none.
- **EX012 — Unmapped items.** Which requirements were unmapped? *Rubric:* 3 = R3 and R8;; 2 = two;; 1 = none;; 0 = none.
- **EX013 — Illusion of assurance.** Why can mapping create an illusion of assurance? *Rubric:* 3 = mapped controls may be badly designed, operated or evidenced;; 2 = quality hidden;; 1 = none;; 0 = none.
- **EX014 — Refined claim.** How did Lucas refine his claim after discussion? *Rubric:* 3 = mapping is necessary, assurance needs risk-based tested evidence;; 2 = refined;; 1 = none;; 0 = none.

### Synthesis

Frameworks overlap; demonstrable coverage requires evidence, not just mappings.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design an observational comparison with confounders in mind; (2) obtain ethical and organisational approval; (3) plan reproducible analysis.

### 3.1 Choosing the design

Tessaly has ten business units: five review access quarterly and five annually. Lucas cannot randomise frequency, so he designs a cross-sectional comparison. An independent reviewer samples 300 accounts from each group and judges each against the role catalogue. To address confounding, he records unit size, staff turnover and system count, because high turnover could raise excess access regardless of review frequency. He plans to compare rates and then check whether the difference holds within units of similar turnover. He also records the number of accounts in each unit.

### 3.2 Ethics and approval

Although no one is experimented on, the study handles data about employees' access. Lucas obtains approval from Marlow's ethics committee and Tessaly's data protection officer. Reviewers see account identifiers only, not names, and results are reported by group, never by person or by named unit. Findings will not be used to discipline anyone. Lucas also agrees with Tessaly that any serious excess access found, such as administrator rights for a departed contractor, will be reported to the security team immediately as an operational issue.

### 3.3 Reproducible plan

Lucas writes an analysis plan before seeing the data: the outcome, the comparison, a bootstrap interval for the difference in rates, the turnover check and how missing judgements will be handled. He fixes random seeds in scripts and stores the plan with a date. He notes that pre-specifying analyses protects against choosing the most flattering result after the fact, a problem Wohlin and colleagues (2012) discuss for software engineering experiments that applies equally to governance studies. All scripts and the plan live in one versioned folder for review.

### 3.4 Pilot of the reviewer

Before the main study, Lucas tests whether excess access can be judged consistently. Two reviewers independently judge 40 accounts. They agree on 36, and discussion reveals that most disagreements concerned shared mailboxes, which the role catalogue did not cover. Lucas adds a rule for shared resources. This pilot shows that the outcome is measurable but depends on catalogue quality, a limit he will report. It also suggests a practical benefit for Tessaly: a better catalogue makes every future review easier. He records the rule in the codebook.

### Worked example

Lucas designs a 300-plus-300 account comparison, records turnover as a confounder, secures approval and pre-registers his analysis.

> **Synthetic case.** All units, accounts and agreement figures are synthetic.

### Errors and limits

Measured confounders do not remove unmeasured ones. Catalogue quality limits validity.

### Exercises

- **EX015 — Group sizes.** How many accounts are sampled per group? *Rubric:* 3 = 300;; 2 = three hundred;; 1 = none;; 0 = none.
- **EX016 — Key confounder.** Which confounder could raise excess access regardless of frequency? *Rubric:* 3 = staff turnover;; 2 = turnover;; 1 = none;; 0 = none.
- **EX017 — Approvals needed.** Whose approval did Lucas obtain? *Rubric:* 3 = Marlow's ethics committee and Tessaly's data protection officer;; 2 = both;; 1 = none;; 0 = none.
- **EX018 — Serious finding rule.** What happens if serious excess access is found? *Rubric:* 3 = reported immediately to security as an operational issue;; 2 = report;; 1 = ignore;; 0 = none.
- **EX019 — Pilot agreement.** How many of 40 pilot accounts did reviewers agree on? *Rubric:* 3 = 36;; 2 = 90%;; 1 = none;; 0 = none.
- **EX020 — Catalogue fix.** What rule did Lucas add after the pilot? *Rubric:* 3 = a rule for shared resources such as mailboxes;; 2 = shared mailboxes;; 1 = none;; 0 = none.

### Synthesis

Observational designs need recorded confounders, approvals and a pre-registered plan.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Security governance, risk and compliance: competing explanations

### Learning outcomes

You will (1) list rival explanations for an observed difference; (2) design checks that can distinguish them; (3) judge which explanations remain plausible.

### 4.1 Rival explanations

Before collecting data, Lucas lists explanations that could produce lower excess access in quarterly units even if frequency itself made no difference. Quarterly units might have lower turnover. They might have fewer systems, making access simpler. Their managers might be more diligent in general, and diligence rather than frequency could drive results. Reviews might also be rubber-stamped, in which case frequency would add cost without benefit. Writing these down early forces him to plan checks rather than explain results away later.

### 4.2 Designing checks

For each rival, Lucas plans a check. He compares turnover and system counts between groups. To probe diligence, he records whether units completed other controls on time, such as security training. To detect rubber-stamping, he measures how many access removals each review produced and how long reviewers spent per account. If quarterly reviews remove almost nothing and take seconds per account, their apparent benefit is suspect. These checks cannot prove cause but can make some explanations much less plausible. Each check is written into the plan.

### 4.3 Literature on control effectiveness

Lucas connects his checks to the literature. Herley and van Oorschot (2017) argue that security research often lacks falsifiable claims, and he uses their point to insist that his hypothesis could fail. Gordon and Loeb (2002) remind him that more control is not always worth its cost, so he will compare benefit with reviewer hours. The COBIT 2019 emphasis on performance management supports measuring whether a process achieves its goal, not merely whether it occurs. Together these sources shape what he measures, how he frames costs and what counts as a fair test of his idea.

### 4.4 Judging plausibility

Lucas plans to report each rival with its check result and a judgement: ruled less likely, still plausible or untested. He will avoid claiming that quarterly review causes lower excess access unless the main rivals are weakened. Dr. Solberg approves this structure, noting that examiners value candour about what remains uncertain. She also asks him to state in advance what result would count against his hypothesis: no meaningful difference, or a difference that disappears among units with similar turnover. Lucas adds this to his plan.

### Worked example

Lucas lists four rival explanations, plans checks for each and states in advance what result would count against his hypothesis.

> **Synthetic case.** Planned checks are synthetic; cited works are real.

### Errors and limits

Some rivals cannot be tested. Diligence measures are crude.

### Exercises

- **EX021 — Rubber-stamp test.** How will Lucas detect rubber-stamping? *Rubric:* 3 = removals per review and time per account;; 2 = removals;; 1 = none;; 0 = none.
- **EX022 — Diligence proxy.** What proxy does Lucas use for general diligence? *Rubric:* 3 = on-time completion of other controls such as training;; 2 = training;; 1 = none;; 0 = none.
- **EX023 — Cost lens.** Which source reminds Lucas that more control is not always worth its cost? *Rubric:* 3 = Gordon and Loeb (2002);; 2 = Gordon-Loeb;; 1 = none;; 0 = none.
- **EX024 — Falsifiability.** Why does Lucas cite Herley and van Oorschot? *Rubric:* 3 = to insist his hypothesis could fail;; 2 = falsifiable;; 1 = none;; 0 = none.
- **EX025 — Judgement categories.** Which three judgements will each rival receive? *Rubric:* 3 = ruled less likely, still plausible or untested;; 2 = three;; 1 = none;; 0 = none.
- **EX026 — Disconfirming result.** What result would count against the hypothesis? *Rubric:* 3 = no meaningful difference, or one that disappears at similar turnover;; 2 = stated;; 1 = none;; 0 = none.

### Synthesis

Listing and checking rival explanations is the core of honest observational research.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a concise research proposal; (2) pilot evidence testing with attribute sampling; (3) interpret upper bounds on deviation rates.

### 5.1 The proposal

Lucas writes a twelve-page proposal: the question, a short review of standards and studies, the cross-sectional design, the outcome definition, the confounders, the rival explanations with planned checks, the ethics arrangements and a timeline of nine months. He includes the analysis plan as an appendix and a one-page summary for Tessaly's chief information security officer. The proposal states clearly that results describe Tessaly's units in one year and may not generalise to other companies, other systems or other kinds of review.

### 5.2 Why sample review records

Besides excess access, Lucas wants to know whether reviews actually happen as recorded. Checking every review record is too slow, so he borrows the auditor's tool of attribute sampling: draw a random sample of records, count deviations such as a missing sign-off, and compute an upper bound on the true deviation rate. If that bound is below a tolerable rate set in advance, the control is judged to operate effectively. He sets the tolerable rate at 5%, a common choice that he records with its rationale in the plan.

### 5.3 Piloting the sample

In the pilot, Lucas computes exact upper 95% bounds for several sample outcomes. With 60 records and no deviations, the bound is 0.049, just below the 5% tolerable rate. One deviation in 60 raises the bound to 0.077, and three deviations to 0.124. A sample of 25 with one deviation gives 0.176. Only the clean sample of 60 supports a conclusion of effective operation. The lab makes clear that small samples cannot support strong assurance, even when deviations are rare. He records each bound in his notes so that the choice of sample size can be checked later by his supervisor and by examiners.

### Lab — Exact upper bounds for attribute samples

```python
"""Attribute sampling: exact upper 95% bound on control deviation rate (stdlib only)."""
from math import comb
def cdf(k, n, p): return sum(comb(n, i)*p**i*(1-p)**(n-i) for i in range(k+1))
def upper(k, n):
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo+hi)/2
        if cdf(k, n, mid) > 0.05: lo = mid
        else: hi = mid
    return hi
for n, k in [(60, 0), (60, 1), (60, 3), (25, 1)]:
    print(f"sample {n}, deviations {k}: upper 95% bound {upper(k, n):.3f}")
print("tolerable rate 0.05 met:", [f"{n}/{k}" for n, k in [(60,0),(60,1),(60,3),(25,1)] if upper(k,n) <= 0.05])
```

Run with `python3 lab_sample.py`. Verified output:

```text
sample 60, deviations 0: upper 95% bound 0.049
sample 60, deviations 1: upper 95% bound 0.077
sample 60, deviations 3: upper 95% bound 0.124
sample 25, deviations 1: upper 95% bound 0.176
tolerable rate 0.05 met: ['60/0']
```

### 5.4 Pilot lessons

The pilot changes the plan. Lucas decides to sample 60 review records per group rather than 25, because smaller samples cannot meet the tolerable rate even with a single deviation. He also clarifies what counts as a deviation: a review with no sign-off, a sign-off after the deadline, or a sign-off by someone not responsible for the unit. Dr. Solberg notes that this evidence test complements the excess-access measure: one shows whether reviews happened, the other whether access ended up correct. He updates the plan.

### Worked example

Lucas pilots attribute sampling and finds only a clean sample of 60 gives a bound below 5%, so he sets n=60 per group.

> **Synthetic case.** Sample outcomes are synthetic; the method is standard statistics.

### Errors and limits

Sampling cannot detect rare systematic failures. Tolerable rates are judgement calls.

### Exercises

- **EX027 — Proposal length.** How long is Lucas's proposal and its timeline? *Rubric:* 3 = twelve pages, nine months;; 2 = 12 pages;; 1 = none;; 0 = none.
- **EX028 — Tolerable rate.** Which tolerable deviation rate did Lucas set? *Rubric:* 3 = 5%;; 2 = 0.05;; 1 = none;; 0 = none.
- **EX029 — Clean sample bound.** With 60 records and no deviations, what is the upper bound? *Rubric:* 3 = 0.049;; 2 = under 5%;; 1 = none;; 0 = none.
- **EX030 — One deviation bound.** How high is the bound with one deviation in 60? *Rubric:* 3 = 0.077;; 2 = above 5%;; 1 = none;; 0 = none.
- **EX031 — Small sample.** Can a sample of 25 with one deviation support effective operation? *Rubric:* 3 = no, the bound is 0.176;; 2 = no;; 1 = yes;; 0 = none.
- **EX032 — Deviation types.** List the three deviation types Lucas defined. *Rubric:* 3 = no sign-off, late sign-off, wrong signer;; 2 = three;; 1 = none;; 0 = none.

### Synthesis

Pilots set realistic sample sizes and sharpen definitions before the main study.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) collect governance data under a pre-registered plan; (2) estimate a difference with a bootstrap interval; (3) run the planned rival-explanation checks.

### 6.1 Collecting the data

Over six weeks, an independent reviewer judges 300 sampled accounts in the quarterly group and 300 in the annual group, using the role catalogue with its new shared-resource rule. Lucas samples 60 review records per group for the evidence test. He logs every step: sample draws with their seeds, judgements with dates and any accounts that could not be judged. Only four accounts lacked enough information, and he records them as missing rather than guessing, as the plan requires. The reviewer works without knowing which group each account came from.

### 6.2 The main estimate

The reviewer finds 18 excess accounts of 300 in the quarterly group and 39 of 300 in the annual group: rates of 0.060 and 0.130. The difference is 0.070, about seven percentage points. A bootstrap with 2,000 resamples gives a 95% interval from 0.023 to 0.117. The interval excludes zero, so the data are consistent with a real difference in these units, though its size is uncertain: it could be as small as two points or as large as twelve. Lucas reports the interval alongside the point estimate in every table and figure, so that readers never see the difference without its uncertainty.

### Lab — Bootstrap interval for the difference in excess-access rates

```python
"""Bootstrap difference in excess-access rate, quarterly vs annual review units (synthetic)."""
import random
random.seed(7)
q = [1]*18 + [0]*282   # quarterly units: 300 accounts, 18 excess
a = [1]*39 + [0]*261   # annual units: 300 accounts, 39 excess
diff = sum(a)/len(a) - sum(q)/len(q)
boots = []
for _ in range(2000):
    bq = [random.choice(q) for _ in q]; ba = [random.choice(a) for _ in a]
    boots.append(sum(ba)/len(ba) - sum(bq)/len(bq))
boots.sort()
print(f"excess rate annual {sum(a)/len(a):.3f}; quarterly {sum(q)/len(q):.3f}; difference {diff:.3f}")
print(f"95% bootstrap interval {boots[49]:.3f} to {boots[1949]:.3f}")
```

Run with `python3 lab_boot.py`. Verified output:

```text
excess rate annual 0.130; quarterly 0.060; difference 0.070
95% bootstrap interval 0.023 to 0.117
```

### 6.3 Rival checks

Lucas runs his planned checks. Turnover is similar in the two groups, and when he compares only the six units with mid-range turnover the difference shrinks but remains. System counts are similar. Quarterly units completed training on time slightly more often, so diligence remains a plausible partial explanation. Quarterly reviews removed an average of nine permissions each, and reviewers spent about forty seconds per account, so rubber-stamping looks unlikely. The evidence tests found no deviations in 60 quarterly records and two in 60 annual records.

### 6.4 Cost

Quarterly review costs more time. Reviewers in quarterly units logged about four times as many hours per year as those in annual units, though each review was shorter because fewer changes accumulated. Lucas presents both benefit and cost without combining them into a single figure, because the value of removing excess access depends on what that access could expose. He suggests that Tessaly might adopt quarterly reviews for high-risk systems and keep annual reviews elsewhere, a risk-based compromise consistent with ISO/IEC 27002:2022 guidance.

### Worked example

Lucas finds excess access of 0.060 versus 0.130, a difference of 0.070 with interval 0.023 to 0.117, and checks rivals and cost.

> **Synthetic case.** All counts and costs are synthetic.

### Errors and limits

Diligence remains a partial rival. Cost-benefit depends on asset value.

### Exercises

- **EX033 — Missing judgements.** How did Lucas handle accounts that could not be judged? *Rubric:* 3 = recorded them as missing;; 2 = missing;; 1 = guessed;; 0 = none.
- **EX034 — Group rates.** What excess-access rates did each group show? *Rubric:* 3 = quarterly 0.060, annual 0.130;; 2 = 18 and 39;; 1 = none;; 0 = none.
- **EX035 — Bootstrap interval.** Give the 95% bootstrap interval for the difference. *Rubric:* 3 = 0.023 to 0.117;; 2 = excludes zero;; 1 = none;; 0 = none.
- **EX036 — Turnover check.** What happened to the difference among mid-turnover units? *Rubric:* 3 = it shrank but remained;; 2 = remained;; 1 = vanished;; 0 = none.
- **EX037 — Rubber-stamp evidence.** Why does rubber-stamping look unlikely? *Rubric:* 3 = nine removals per review and forty seconds per account;; 2 = removals;; 1 = none;; 0 = none.
- **EX038 — Risk-based option.** Which compromise does Lucas suggest? *Rubric:* 3 = quarterly for high-risk systems, annual elsewhere;; 2 = risk-based;; 1 = none;; 0 = none.

### Synthesis

A pre-registered analysis yields an uncertain but real difference, with rivals and cost reported alongside.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a master's dissertation; (2) write a candid limitations section; (3) report results for both academic and practitioner readers.

### 7.1 Structure

Lucas structures his dissertation in seven parts: introduction, literature and standards, method, results, rival explanations, discussion and conclusion, followed by appendices with the analysis plan, codebook and scripts. Each results claim cites a table or figure, and each table states its sample size. He keeps the main text near 20,000 words, as Marlow requires, moving long material to appendices. He writes the method so precisely that another student at another company could repeat the study with their own access data. He follows the template.

### 7.2 Limitations

His limitations section is direct. The design is observational, so frequency may not be the cause. Diligence remains a partial alternative explanation. The study covers one company in one year. Excess access depends on the role catalogue, which was revised during the pilot. The bootstrap interval is wide. The cost estimate relies on self-logged hours, which may be inaccurate. For each limit he states how it could bias results and in which direction, rather than listing limits without consequences, so readers can weigh them.

### 7.3 Two audiences

Lucas writes a four-page practitioner summary for Tessaly alongside the dissertation. It avoids statistical jargon, explains that quarterly units had about half the excess access with a wide margin of uncertainty, and presents the risk-based option with its cost. He is careful not to overstate. He also shows the summary to two unit managers, who point out that a phrase implied their units were careless. He rewrites it, because reports that blame groups can reduce cooperation in future reviews. Both managers approve it.

### 7.4 Linking to frameworks

In the discussion, Lucas relates his findings to frameworks. ISO/IEC 27001:2022 requires monitoring and evaluation of the management system, and his method offers one way to evaluate an access control rather than only confirming that reviews took place. NIST CSF 2.0 Govern outcomes include oversight of risk management strategy, and he suggests boards ask for outcome measures like excess-access rates. He frames these as suggestions grounded in one study, not as requirements of the standards, which he paraphrases rather than quotes at length.

### Worked example

Lucas writes a seven-part dissertation, states each limit with its likely bias and produces a non-blaming practitioner summary.

> **Synthetic case.** The dissertation is synthetic; the standards are real.

### Errors and limits

Practitioner summaries can oversimplify. Framework links are interpretations.

### Exercises

- **EX039 — Main text length.** Roughly how long is the main text? *Rubric:* 3 = about 20,000 words;; 2 = 20k;; 1 = none;; 0 = none.
- **EX040 — Limit style.** How does Lucas present each limitation? *Rubric:* 3 = with its likely bias and direction;; 2 = bias;; 1 = list only;; 0 = none.
- **EX041 — Self-logged hours.** Which limitation affects the cost estimate? *Rubric:* 3 = hours were self-logged;; 2 = self-report;; 1 = none;; 0 = none.
- **EX042 — Summary length.** How long is the practitioner summary? *Rubric:* 3 = four pages;; 2 = 4;; 1 = none;; 0 = none.
- **EX043 — Manager feedback.** Why did Lucas rewrite a phrase in the summary? *Rubric:* 3 = it implied units were careless;; 2 = blame;; 1 = none;; 0 = none.
- **EX044 — Board suggestion.** What does Lucas suggest boards ask for? *Rubric:* 3 = outcome measures such as excess-access rates;; 2 = outcomes;; 1 = none;; 0 = none.

### Synthesis

Good dissertations make claims traceable, limits consequential and summaries fair.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) obtain and respond to independent review; (2) defend design choices; (3) plan dissemination and next steps.

### 8.1 Independent review

Before submission, Lucas asks a researcher from another university to rerun his scripts from the archive. She reproduces every table and the bootstrap interval exactly, thanks to fixed seeds. She also questions whether the four missing accounts could change the result. Lucas runs a worst-case check, assuming all four missing accounts belonged to the quarterly group and had excess access; the difference falls slightly but the interval still excludes zero. He adds this sensitivity check to the results chapter and thanks the reviewer in his acknowledgements.

### 8.2 The defense

At the defense, examiners ask why Lucas did not randomise frequency. He explains that Tessaly could not change review schedules for research, and that he addressed this through confounder checks and candour about diligence. Another examiner asks whether excess access is the right outcome. Lucas argues it is closer to risk than counting completed reviews, but admits it does not measure whether excess access was ever misused. A third asks about generalisability; he answers that the method generalises more readily than the specific result.

### 8.3 Outcome and dissemination

The examiners pass the dissertation with minor revisions: clearer labels on two figures and a short discussion of review fatigue. Lucas plans a short paper for a practitioner journal and a talk at a regional security forum. Tessaly decides to pilot quarterly reviews for its warehouse management and finance systems, the highest-risk applications, and to measure excess access again after a year. Lucas offers his scripts and codebook so that the follow-up measurement uses exactly the same method. Both outputs cite the archive.

### 8.4 What comes next

Dr. Solberg suggests that a randomised follow-up would be the natural next study: if several companies agreed to assign review frequency by lottery to comparable units, frequency could be tested directly. Lucas notes the practical and ethical issues, such as ensuring no unit is left with unacceptable risk. He reflects that his master's work taught him to value modest, well-checked findings over striking claims, and that governance research is most useful when it measures outcomes that matter to risk. He records this reflection.

### Worked example

Lucas survives independent reproduction, adds a worst-case missing-data check, defends his design and plans dissemination.

> **Synthetic case.** Review, defense and follow-up are synthetic.

### Errors and limits

Reproduction checks code, not truth. Follow-up results may differ.

### Exercises

- **EX045 — Reproduction result.** Did the independent reviewer reproduce the tables? *Rubric:* 3 = yes, exactly, due to fixed seeds;; 2 = yes;; 1 = no;; 0 = none.
- **EX046 — Worst-case check.** What did the worst-case missing-data check show? *Rubric:* 3 = the difference fell slightly but the interval still excluded zero;; 2 = robust;; 1 = reversed;; 0 = none.
- **EX047 — No randomisation.** Why was frequency not randomised? *Rubric:* 3 = Tessaly could not change schedules for research;; 2 = practical;; 1 = none;; 0 = none.
- **EX048 — Outcome limit.** What does excess access not measure? *Rubric:* 3 = whether access was misused;; 2 = misuse;; 1 = none;; 0 = none.
- **EX049 — Tessaly decision.** Which systems will Tessaly pilot quarterly reviews on? *Rubric:* 3 = warehouse management and finance;; 2 = high-risk;; 1 = all;; 0 = none.
- **EX050 — Next study.** What follow-up does Dr. Solberg suggest? *Rubric:* 3 = a randomised multi-company study;; 2 = randomise;; 1 = none;; 0 = none.

### Synthesis

Independent reproduction, candid defense and planned follow-up complete a master's study.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Lucas Ferreira, Dr. Ingrid Solberg, Marlow Institute of Technology, Tessaly Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The account, not the person.

**EX002.** A permission the account owner's current role does not require, judged against the written role catalogue.

**EX003.** By the hours reviewers log.

**EX004.** Because units chose their own frequency, so differences may reflect other unit traits.

**EX005.** The date, database, search string and number of hits.

**EX006.** No; it calls for review at planned intervals without setting a frequency.

**EX007.** Define the question as consensus practice, but not provide tested evidence of an effect.

**EX008.** ISO/IEC 27001:2022.

**EX009.** Governance from management of enterprise information and technology.

**EX010.** Eight of ten.

**EX011.** 60%, six of ten.

**EX012.** R3 and R8.

**EX013.** Because a mapped control may be badly designed, poorly operated or evidenced by unchecked documents.

**EX014.** Mapping is a necessary first step, but assurance needs tested evidence with depth following risk.

**EX015.** 300 accounts from each group.

**EX016.** Staff turnover.

**EX017.** Marlow's ethics committee and Tessaly's data protection officer.

**EX018.** It is reported to the security team immediately as an operational issue.

**EX019.** 36 of 40.

**EX020.** A rule for shared resources such as shared mailboxes.

**EX021.** By measuring access removals per review and reviewer time per account.

**EX022.** Whether units completed other controls on time, such as security training.

**EX023.** Gordon and Loeb (2002).

**EX024.** To insist that his hypothesis must be falsifiable.

**EX025.** Ruled less likely, still plausible or untested.

**EX026.** No meaningful difference, or a difference that disappears among units with similar turnover.

**EX027.** Twelve pages with a nine-month timeline.

**EX028.** 5%.

**EX029.** 0.049, just below 5%.

**EX030.** 0.077.

**EX031.** No; the upper bound is 0.176.

**EX032.** No sign-off, a sign-off after the deadline and a sign-off by someone not responsible.

**EX033.** He recorded them as missing rather than guessing.

**EX034.** 0.060 quarterly and 0.130 annual.

**EX035.** 0.023 to 0.117.

**EX036.** It shrank but remained.

**EX037.** Reviews removed about nine permissions each and took about forty seconds per account.

**EX038.** Quarterly reviews for high-risk systems and annual reviews elsewhere.

**EX039.** About 20,000 words.

**EX040.** By stating how it could bias results and in which direction.

**EX041.** Reviewer hours were self-logged and may be inaccurate.

**EX042.** Four pages.

**EX043.** Because it implied some units were careless, which could reduce cooperation.

**EX044.** Outcome measures such as excess-access rates, not just confirmation that reviews occurred.

**EX045.** Yes, exactly, because seeds were fixed.

**EX046.** The difference fell slightly but the interval still excluded zero.

**EX047.** Because Tessaly could not change review schedules for research purposes.

**EX048.** Whether excess access was ever actually misused.

**EX049.** Its warehouse management and finance systems.

**EX050.** A randomised study assigning review frequency by lottery across comparable units in several companies.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Gordon, L. A., & Loeb, M. P. (2002). The economics of information security investment. *ACM Transactions on Information and System Security*, 5(4), 438–457. <https://doi.org/10.1145/581271.581274>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022b). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. ISACA. <https://www.isaca.org/resources/cobit>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Spears, J. L., & Barki, H. (2010). User participation in information systems security risk management. *MIS Quarterly*, 34(3), 503–522. <https://doi.org/10.2307/25750689>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
