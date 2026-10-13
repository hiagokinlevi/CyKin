# Privacy and Data Protection: Doctoral Research Track

- Language: English (`en`); course 188, Doctoral research track (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; five offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: doctoral candidates comparing k-anonymised records with differentially private counts for a public-sector data release.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs measure uniqueness, generalise records to k = 5, add Laplace noise to counts, run a linkage attack and check an archive for identifiers, all on a seeded synthetic population. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one doctoral candidate comparing release methods for transit data: integrity and a uniqueness baseline, the research frontier, the proposal, the differential privacy pilot, the main linkage study and validation, peer critique, synthesis and archive, and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Ines Carvalho** | Doctoral candidate | Invented |
| **Prof. Henrik Aaltonen** | Supervisor | Invented |
| **Thornbury University** | Fictional university | Invented |
| **Valemont Regional Transit Authority** | Fictional authority publishing smart-card travel data | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR); Lei 13.709/2018 (LGPD); Sweeney (2002), [doi:10.1142/S0218488502001648](https://doi.org/10.1142/S0218488502001648); Dwork et al. (2006) and Dwork and Roth (2014), [doi:10.1561/0400000042](https://doi.org/10.1561/0400000042); Narayanan and Shmatikov (2008); Solove (2006); Nissenbaum (2004, 2009); NISTIR 8053 and NIST SP 800-188; EDPB Guidelines 4/2019. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes

You will (1) frame a falsifiable question about privacy-preserving data release; (2) set integrity rules for research that touches personal data; (3) measure how quickly ordinary attributes make people unique.

### 1.1 A falsifiable question

Ines Carvalho is a doctoral candidate at the fictional Thornbury University, supervised by Prof. Henrik Aaltonen. Her partner is the fictional Valemont Regional Transit Authority, which collects smart-card journeys and wants to publish travel data for city planners. Ines asks whether releasing differentially private origin-destination counts protects riders better than releasing k-anonymised journey records, at a utility planners still accept. Before collecting anything she writes down which results would prove her wrong: no measurable reduction in linkage risk, or an error so large that planners reject the counts for routine timetable decisions.

### 1.2 Why the question matters

The question matters because transit data looks harmless but describes where people live, work and pray. Under Regulation (EU) 2016/679, the GDPR, data that can single out a person remain personal data, while Recital 26 places truly anonymous information outside the regulation. The Brazilian LGPD, Lei 13.709/2018, draws a similar line in its definition of anonymised data. Whether a release counts as anonymous is therefore a legal as well as a technical question. Ines treats it as an empirical claim to be tested rather than a label that the authority can simply apply to a spreadsheet before publishing it.

### 1.3 Integrity rules

Research on personal data must not create the harm it studies. Ines's protocol, approved by the Thornbury ethics committee and reviewed by Valemont's data protection officer, sets five rules. She works only on a synthetic population generated to match published aggregate statistics; no real card numbers leave the authority; any attack experiment targets the synthetic population, never real riders; the analysis plan is pre-registered before results are seen; and every file leaving the secure environment is checked for direct identifiers. She also declares that she has no commercial interest in any anonymisation product or consultancy.

### 1.4 Uniqueness as a baseline

Before comparing release methods, Ines measures how identifying ordinary attributes are. Sweeney (2002) showed that a few quasi-identifiers such as postcode, birth date and sex can single out most people, which motivated the k-anonymity model. The lab builds 20,000 synthetic riders with a home zone, a work zone, a birth year and a sex, then counts the share who are unique on growing combinations. Home zone alone singles out nobody, and home plus work zone singles out nobody either, but adding birth year makes 83.4% unique, and adding sex raises the figure to 91.5% of the synthetic population.

### Lab — Uniqueness of synthetic riders on quasi-identifiers

```python
# Share of synthetic transit riders who are unique on combinations of quasi-identifiers.
import random
from collections import Counter
r = random.Random(7)
riders = [(r.randrange(40), r.randrange(40), r.randrange(1940, 2008), r.choice("FM")) for _ in range(20000)]
def unique(cols):
    keys = [tuple(x[c] for c in cols) for x in riders]
    c = Counter(keys)
    return sum(1 for k in keys if c[k] == 1) / len(keys)
for name, cols in [("home zone", (0,)), ("home + work zone", (0, 1)),
                   ("home + work + birth year", (0, 1, 2)), ("home + work + birth year + sex", (0, 1, 2, 3))]:
    print(f"{name:32s} unique {unique(cols):6.1%}")
```

Run with `python3 lab_unique.py`. Verified output:

```text
home zone                        unique   0.0%
home + work zone                 unique   0.0%
home + work + birth year         unique  83.4%
home + work + birth year + sex   unique  91.5%
```

### Worked example

Ines frames a falsifiable comparison between k-anonymised records and differentially private counts, sets integrity rules for research on transit data and records a baseline: 83.4% of synthetic riders are unique on home zone, work zone and birth year.

> **Synthetic case.** Thornbury, Valemont and every rider are synthetic; the GDPR, the LGPD and Sweeney (2002) are real.

### Errors and limits

Uniqueness in a synthetic population only approximates uniqueness in the real one. Being unique is not the same as being re-identified; an attacker also needs outside knowledge.

### Exercises

- **EX001 — Falsifiable plan.** What makes Ines's research question falsifiable? *Rubric:* 3 = she lists in advance results that would refute it: no drop in linkage risk or unacceptable error;; 2 = mentions pre-stated outcomes vaguely;; 1 = says it is a good question;; 0 = none.
- **EX002 — Anonymous in law.** Why is "anonymous" a legal as well as a technical question for the authority? *Rubric:* 3 = GDPR Recital 26 and the LGPD place anonymous data outside the law, so the label changes legal duties;; 2 = cites one law only;; 1 = says it is technical;; 0 = none.
- **EX003 — Synthetic population.** Why does Ines work on a synthetic population instead of real cards? *Rubric:* 3 = it lets her run attacks and publish results without exposing or re-identifying real riders;; 2 = says it is easier;; 1 = says real data is unavailable;; 0 = none.
- **EX004 — Uniqueness jump.** Which attribute causes the biggest jump in uniqueness in the lab, and why? *Rubric:* 3 = birth year: from 0% to 83.4%, because it splits each zone pair into many small groups;; 2 = names birth year without numbers;; 1 = names zone;; 0 = none.
- **EX005 — Unique versus identified.** Why is uniqueness not yet re-identification? *Rubric:* 3 = an attacker also needs outside knowledge that links the unique combination to a named person;; 2 = says they differ;; 1 = treats them as equal;; 0 = none.
- **EX006 — Interest declaration.** Why does Ines declare that she has no commercial interest? *Rubric:* 3 = readers can judge bias; a product interest could tilt the method comparison;; 2 = says it is required;; 1 = omits reasons;; 0 = none.
- **EX007 — Pre-registration value.** What does pre-registering the analysis plan protect against? *Rubric:* 3 = choosing metrics or thresholds after seeing results that flatter one method;; 2 = mentions bias generally;; 1 = says it is paperwork;; 0 = none.

### Synthesis

Chapter 1 sets a falsifiable question, integrity rules and a uniqueness baseline. Chapter 2 maps the research frontier from Warren and Brandeis to differential privacy.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Privacy and data protection: research frontier

### Learning outcomes

You will (1) trace how privacy theory developed; (2) contrast syntactic anonymity models with differential privacy; (3) locate the gap Ines's study addresses.

### 2.1 From a right to be let alone

Ines begins her review with Warren and Brandeis (1890), who argued in the Harvard Law Review for a right to privacy against intrusive photography and gossip. Solove (2006) later argued that privacy is not one thing and offered a taxonomy of harmful activities grouped as information collection, information processing, information dissemination and invasion. Nissenbaum (2004, 2009) proposed contextual integrity: a flow of information is appropriate when it respects the norms of the context in which it was shared. For transit data, contextual integrity asks whether riders expect their journeys to reach city planners in any form at all.

### 2.2 Syntactic anonymity models

The first technical family protects records by making them look alike. Sweeney (2002) defined k-anonymity: each combination of quasi-identifiers must be shared by at least k records. Machanavajjhala and colleagues (2007) showed that a k-anonymous group can still reveal a sensitive value if everyone in it shares that value, and proposed l-diversity. Li, Li and Venkatasubramanian (2007) proposed t-closeness, which requires the sensitive distribution in each group to stay close to the overall distribution. Ines notes that each model was proposed after an attack on the previous one, which suggests that syntactic guarantees depend on assumptions about the attacker.

### 2.3 Linkage and de-anonymisation

Narayanan and Shmatikov (2008) showed that a supposedly anonymous dataset of film ratings could be linked to public reviews using only a few known ratings, because sparse records are highly distinctive. Their result generalises to transit journeys, which are also sparse and distinctive. Garfinkel's NIST report on de-identification (NISTIR 8053, 2015) and NIST SP 800-188 (2023) describe the resulting practical position: removing names is not enough, re-identification risk must be estimated, and the choice of method should depend on the release model, whether public, restricted or enclave access, as well as on the intended data users.

### 2.4 Differential privacy

The second family protects the output of an analysis rather than records. Dwork, McSherry, Nissim and Smith (2006) introduced calibrating noise to the sensitivity of a query: if adding or removing one person changes a count by at most one, Laplace noise with scale one over epsilon makes the published count almost equally likely with or without that person. Dwork and Roth (2014) give the formal foundations. The guarantee holds whatever the attacker already knows, which answers the weakness of syntactic models, but it costs accuracy, and the cost is largest for small counts such as quiet stations and rare journeys.

### 2.5 The gap

Ines finds many theoretical comparisons and many single-method case studies, but few studies that compare both families on the same release, measure risk with the same attack and ask real users whether the result remains useful. That is her gap. Her contribution will be empirical and practical: a controlled comparison on one synthetic transit population, with planners' acceptance as an explicit utility criterion. She writes the gap as a single sentence for her committee and checks it against the falsifiable question from Chapter 1, so that the review and the study design point at exactly the same uncertainty.

### Worked example

Ines groups the literature into theory (Warren and Brandeis, Solove, Nissenbaum), syntactic models (Sweeney, l-diversity, t-closeness), attacks (Narayanan and Shmatikov) and differential privacy (Dwork and colleagues), and identifies a gap: same-release comparison with a user utility test.

> **Synthetic case.** Every work named is real and cited in the references; Ines's synthesis is a teaching illustration.

### Errors and limits

A literature map simplifies; differential privacy also has variants and attacks on implementations. Contextual integrity is a normative theory, not a metric.

### Exercises

- **EX008 — Contextual integrity.** How would contextual integrity judge sending journey data to planners? *Rubric:* 3 = asks whether the flow fits the norms riders expected when they tapped their cards;; 2 = mentions norms;; 1 = says it is legal;; 0 = none.
- **EX009 — Solove's groups.** Name Solove's four groups of privacy problems. *Rubric:* 3 = collection, processing, dissemination, invasion;; 2 = names three;; 1 = names one;; 0 = none.
- **EX010 — l-diversity motive.** What weakness of k-anonymity led to l-diversity? *Rubric:* 3 = a k-anonymous group may share one sensitive value, revealing it for all members;; 2 = mentions sensitive values;; 1 = restates k-anonymity;; 0 = none.
- **EX011 — Sparse records.** Why does the Narayanan and Shmatikov result matter for transit data? *Rubric:* 3 = journeys are sparse and distinctive like ratings, so a few known trips can link a record;; 2 = says linkage is possible;; 1 = cites a film case only;; 0 = none.
- **EX012 — Sensitivity meaning.** What is the sensitivity of a count query, and why does it matter? *Rubric:* 3 = the most one person can change it, one; noise scale is sensitivity over epsilon;; 2 = defines sensitivity loosely;; 1 = names epsilon only;; 0 = none.
- **EX013 — Background knowledge.** Which advantage does differential privacy have over syntactic models? *Rubric:* 3 = its guarantee holds regardless of the attacker's background knowledge;; 2 = mentions attackers;; 1 = says it is newer;; 0 = none.
- **EX014 — Gap statement.** State Ines's research gap in one sentence. *Rubric:* 3 = few studies compare both families on one release with one attack and a user utility test;; 2 = mentions comparison;; 1 = says more research is needed;; 0 = none.

### Synthesis

Chapter 2 maps theory, models, attacks and differential privacy to a precise gap. Chapter 3 turns the gap into a proposal with a generalisation baseline.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes

You will (1) write a doctoral proposal with hypotheses and criteria; (2) generalise records to reach k-anonymity; (3) explain the utility cost of generalisation.

### 3.1 Hypotheses

Ines states two hypotheses. H1: a differentially private release of origin-destination counts with epsilon one yields lower measured linkage risk than a k-anonymised journey file with k equal to five. H2: planners will accept the differentially private counts for timetable decisions at that epsilon, defined as at least two of three planners rating them usable. Each hypothesis has a measurable criterion and a stated threshold set before data exist. Prof. Aaltonen asks her to justify both thresholds in writing, which she does by citing the authority's current planning practice and the error tolerance planners already accept in manual surveys.

### 3.2 Generalisation as the baseline

To build a fair baseline, Ines must produce a k-anonymous file that a competent data steward would actually release. She generalises zones into blocks and birth years into bands, and any rider still in a group smaller than five is suppressed. The lab tries four settings on 20,000 synthetic riders. Exact values would suppress every record, two-zone blocks with five-year bands still suppress 51.4%, four-zone blocks with five-year bands suppress only 0.1%, and eight-zone blocks with ten-year bands suppress none. Each step that removes suppression also blurs where people actually travel.

### 3.3 Choosing the baseline setting

Ines chooses four-zone blocks and five-year bands as the baseline, because it suppresses only 24 of 20,000 riders while keeping 1,400 classes. The coarser eight-zone setting suppresses nothing but merges distinct suburbs that planners need to distinguish. She records the choice and its reason in the protocol, because a weak baseline would make differential privacy look better than it is. This follows the advice in NIST SP 800-188 that de-identification choices should be documented and justified for the intended release, so that reviewers can see whether the comparison was fair.

### 3.4 Planners as judges of utility

Utility is often measured only as numerical error, but Ines's hypothesis H2 asks people who use the data. Three Valemont planners will each receive the same set of journey tables, produced by both methods, without labels, and rate whether they could use each for a timetable decision. Ines will also report mean absolute error so that readers can compare her result with other studies. She explains in the proposal that combining a human judgement with a numerical metric makes the study more relevant to the authority's actual decision about what kind of data to publish.

### Lab — Generalisation and suppression for k = 5

```python
# Generalise synthetic rider records until every class has k >= 5; report suppression and information loss.
import random
from collections import Counter
r = random.Random(7)
riders = [(r.randrange(40), r.randrange(40), r.randrange(1940, 2008)) for _ in range(20000)]
def gen(x, zw, yw):
    return (x[0] // zw, x[1] // zw, x[2] // yw)
for zw, yw in [(1, 1), (2, 5), (4, 5), (8, 10)]:
    keys = [gen(x, zw, yw) for x in riders]; c = Counter(keys)
    small = sum(1 for k in keys if c[k] < 5)
    print(f"zones/{zw:<2d} years/{yw:<2d} classes {len(c):6d}  suppressed for k=5 {small:6d} ({small/len(keys):5.1%})")
```

Run with `python3 lab_kanon.py`. Verified output:

```text
zones/1  years/1  classes  18228  suppressed for k=5  20000 (100.0%)
zones/2  years/5  classes   5430  suppressed for k=5  10282 (51.4%)
zones/4  years/5  classes   1400  suppressed for k=5     24 ( 0.1%)
zones/8  years/10 classes    175  suppressed for k=5      0 ( 0.0%)
```

### Worked example

Ines states H1 and H2 with thresholds, generalises synthetic records and chooses four-zone blocks with five-year bands as the k = 5 baseline: 1,400 classes and 24 riders suppressed.

> **Synthetic case.** All figures come from the synthetic population; NIST SP 800-188 and Sweeney (2002) are real.

### Errors and limits

Three planners are a small panel; acceptance is a coarse measure. The baseline is one reasonable choice among several.

### Exercises

- **EX015 — Hypothesis criteria.** What makes H2 testable? *Rubric:* 3 = a defined panel, a defined rating and a threshold of two of three set in advance;; 2 = mentions a threshold;; 1 = restates the hypothesis;; 0 = none.
- **EX016 — Exact values.** Why does releasing exact zones and birth years fail k = 5 entirely? *Rubric:* 3 = almost every combination is unique, so every record sits in a group below five;; 2 = says many are unique;; 1 = says it is too detailed;; 0 = none.
- **EX017 — Baseline choice.** Why does Ines prefer four-zone blocks with five-year bands over eight-zone blocks? *Rubric:* 3 = it suppresses only 24 riders while keeping finer geography planners need;; 2 = mentions suppression only;; 1 = picks eight-zone;; 0 = none.
- **EX018 — Weak baseline danger.** What happens if the k-anonymity baseline is badly chosen? *Rubric:* 3 = the comparison flatters differential privacy and the result misleads;; 2 = says results change;; 1 = ignores fairness;; 0 = none.
- **EX019 — Blind rating.** Why are the planners' tables unlabelled? *Rubric:* 3 = to stop expectations about either method influencing ratings;; 2 = says it is fairer;; 1 = omits the reason;; 0 = none.
- **EX020 — Two utility measures.** Why report both planner acceptance and mean absolute error? *Rubric:* 3 = acceptance shows real usefulness; error allows comparison with other studies;; 2 = names one;; 1 = says more data is better;; 0 = none.

### Synthesis

Chapter 3 fixes hypotheses, a fair k-anonymity baseline and a two-part utility test. Chapter 4 pilots the differentially private release.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes

You will (1) replicate a known result before extending it; (2) implement the Laplace mechanism on counts; (3) read the accuracy cost of epsilon on small cells.

### 4.1 Replicating first

Before trusting her own code, Ines replicates a textbook property described by Dwork and Roth (2014): for Laplace noise with scale one over epsilon, the expected absolute error equals one over epsilon. If her implementation produced a different average, every later result would be suspect. She draws many noise samples for each epsilon and checks the mean absolute error against the theory. The replication is a small step, but Prof. Aaltonen insists that it appears in the thesis, because examiners need evidence that the instrument works before they consider what it measures in the transit setting.

### 4.2 The pilot release

The pilot uses 100 synthetic origin-destination counts between zero and 400 journeys a day. For each epsilon in the grid 0.1, 0.5, 1.0 and 2.0, the lab adds Laplace noise twenty times to every count. The mean absolute error is 9.91 at epsilon 0.1, 1.98 at 0.5, 0.98 at 1.0 and 0.51 at 2.0, matching one over epsilon closely. The replication passes. Ines notes that these absolute errors look tiny next to counts of several hundred journeys, which is exactly why the next step examines small cells separately rather than trusting an average. Small cells get separate checks.

### 4.3 Small cells

Planners care most about quiet routes, where a few journeys decide whether a bus continues to run. The pilot contains five cells with fewer than twenty journeys a day. On those cells the mean relative error is 94.1% at epsilon 0.1, 22.0% at 0.5, 9.3% at 1.0 and 5.0% at 2.0. At epsilon 0.1 the published number is almost noise. Ines therefore expects planners to reject low epsilon values for small routes, and she adds a pre-registered secondary analysis that reports errors separately for small and large cells, so that an average cannot hide the problem.

### 4.4 Budget accounting

Each published table spends part of a privacy budget, because answering several queries about the same riders adds up. Dwork and Roth describe how epsilon values combine under composition. Valemont wants daily tables for a year, so Ines must decide whether epsilon one is per table, per day or per year. She writes this decision into the protocol as an explicit question for the authority's data protection officer, because it changes the strength of the guarantee by orders of magnitude, and she warns that a per-table epsilon repeated daily cannot be described honestly as a strong annual protection.

### Lab — Laplace noise on origin-destination counts

```python
# Laplace mechanism on 100 synthetic origin-destination counts (sensitivity 1); error by epsilon.
import random, math
r = random.Random(3)
true = [r.randint(0, 400) for _ in range(100)]
def lap(b):
    u = r.random() - 0.5
    return -b * math.copysign(1, u) * math.log(1 - 2 * abs(u))
for eps in [0.1, 0.5, 1.0, 2.0]:
    errs = [abs(lap(1 / eps)) for _ in true for _ in range(20)]
    small = [t for t in true if t < 20]
    rel = sum(abs(lap(1 / eps)) / max(t, 1) for t in small for _ in range(20)) / (20 * len(small))
    print(f"epsilon {eps:3.1f}  mean abs error {sum(errs)/len(errs):5.2f}  mean relative error on {len(small)} small cells {rel:6.1%}")
```

Run with `python3 lab_laplace.py`. Verified output:

```text
epsilon 0.1  mean abs error  9.91  mean relative error on 5 small cells  94.1%
epsilon 0.5  mean abs error  1.98  mean relative error on 5 small cells  22.0%
epsilon 1.0  mean abs error  0.98  mean relative error on 5 small cells   9.3%
epsilon 2.0  mean abs error  0.51  mean relative error on 5 small cells   5.0%
```

### Worked example

Ines replicates the one-over-epsilon error of the Laplace mechanism (0.98 at epsilon 1.0), then finds a 94.1% relative error on small cells at epsilon 0.1, and raises budget accounting as a protocol decision.

> **Synthetic case.** Counts are synthetic and seeded; Dwork, McSherry, Nissim and Smith (2006) and Dwork and Roth (2014) are real.

### Errors and limits

Five small cells are too few for precise estimates. Real releases also need post-processing, such as rounding negative counts, which the pilot omits.

### Exercises

- **EX021 — Replication purpose.** Why replicate the one-over-epsilon error before studying transit data? *Rubric:* 3 = it checks the instrument works so later results can be trusted;; 2 = says it is good practice;; 1 = omits;; 0 = none.
- **EX022 — Error at epsilon one.** What mean absolute error did the pilot find at epsilon 1.0, and what did theory predict? *Rubric:* 3 = 0.98 against a predicted 1.0;; 2 = gives one number;; 1 = gives neither;; 0 = none.
- **EX023 — Average hides harm.** Why can mean absolute error hide harm to planning? *Rubric:* 3 = it averages over large counts while small routes suffer large relative error;; 2 = mentions small cells;; 1 = trusts the average;; 0 = none.
- **EX024 — Small-cell error.** What relative error do small cells show at epsilon 0.5? *Rubric:* 3 = 22.0%;; 2 = about one fifth;; 1 = wrong figure;; 0 = none.
- **EX025 — Composition question.** Why must Valemont decide whether epsilon is per table, per day or per year? *Rubric:* 3 = repeated releases compose, so the total guarantee depends on the accounting unit;; 2 = mentions repeated tables;; 1 = ignores composition;; 0 = none.
- **EX026 — Negative counts.** What post-processing issue does the pilot omit? *Rubric:* 3 = noisy counts can be negative or fractional and must be cleaned without breaking the guarantee;; 2 = mentions rounding;; 1 = says none;; 0 = none.

### Synthesis

Chapter 4 replicates the mechanism and exposes small-cell error and budget accounting. Chapter 5 runs the main study with an independent attack.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes

You will (1) run a linkage attack on synthetic releases; (2) compare risk across release methods; (3) validate results with an independent team.

### 5.1 The attack model

Ines defines an attacker who knows the home zone, work zone and birth year of 500 target riders, perhaps from a social network or an employer directory. Against pseudonymised microdata, in which names are replaced but exact values remain, the attacker looks for a row matching each target exactly. Against the k-anonymised file, the attacker finds the matching class and guesses one row at random. Against the differentially private counts there are no rows to link. Defining the attacker precisely matters because NISTIR 8053 warns that re-identification estimates depend on the assumed knowledge, which must be stated openly.

### 5.2 Results

The lab shows that pseudonymisation alone lets the attacker re-identify 415 of the 500 targets with certainty, 83.0%. The k-anonymised file prevents any certain match; random guessing within classes yields about 4.4 expected correct guesses, 0.9% of targets. The differentially private counts give the attacker no record to link at all, and the risk is instead bounded by epsilon. H1 is supported in direction, but the comparison is not like for like: the k-anonymous file leaks little under this attack, and its remaining risk comes from attacks that Ines has not yet tried, such as combining journeys.

### 5.3 Pseudonymisation is not anonymisation

The 83.0% figure makes a legal point concrete. The GDPR defines pseudonymisation in Article 4(5) as processing so that data can no longer be attributed to a person without additional information kept separately, and it treats pseudonymised data as personal data. Valemont's original plan was to replace card numbers with random tokens and call the file anonymous. Ines's result shows why that would be wrong: the tokens hide names, but the remaining attributes identify most riders. She writes this finding as a recommendation the authority can act on immediately, independent of the rest of the thesis.

### 5.4 Independent validation

Ines asks a team from another university to run the attack on her released files without seeing her code. They receive the synthetic population, the releases and the attack description, and report their own re-identification rates. Their results differ from hers by less than one percentage point. She also asks them to try one attack she did not design, combining two days of journeys; they find that the k-anonymous file leaks more under that attack. Ines reports both results, because independent validation is only valuable if it is allowed to find problems in the main study.

### Lab — Linkage attack on three release types

```python
# Linkage attack: an adversary knows home zone, work zone and birth year of 500 targets.
import random
from collections import Counter
r = random.Random(7)
riders = [(r.randrange(40), r.randrange(40), r.randrange(1940, 2008)) for _ in range(20000)]
targets = r.sample(range(20000), 500)
raw = Counter(riders)
hit_raw = sum(1 for t in targets if raw[riders[t]] == 1)
g = lambda x: (x[0] // 8, x[1] // 8, x[2] // 10)
gen = Counter(g(x) for x in riders)
kept = [t for t in targets if gen[g(riders[t])] >= 5]
exp = sum(1 / gen[g(riders[t])] for t in kept)
print(f"pseudonymised microdata: {hit_raw} of 500 targets re-identified with certainty ({hit_raw/5:.1f}%)")
print(f"k-anonymised (k>=5): 0 certain; expected correct guesses {exp:.1f} ({exp/5:.1f}%)")
print("differentially private counts: no record-level rows to link; risk bounded by epsilon instead")
```

Run with `python3 lab_link.py`. Verified output:

```text
pseudonymised microdata: 415 of 500 targets re-identified with certainty (83.0%)
k-anonymised (k>=5): 0 certain; expected correct guesses 4.4 (0.9%)
differentially private counts: no record-level rows to link; risk bounded by epsilon instead
```

### Worked example

Ines finds 83.0% certain re-identification for pseudonymised data, 0.9% expected correct guesses for k = 5, and no linkable rows for differentially private counts; an independent team confirms the figures and finds an extra multi-day weakness.

> **Synthetic case.** The attacker, targets and releases are synthetic; GDPR Article 4(5) and NISTIR 8053 are real.

### Errors and limits

One attacker model cannot represent all attackers. Differential privacy removes linkage but its real protection depends on the epsilon accounting chosen.

### Exercises

- **EX027 — Attacker knowledge.** What does Ines's attacker know, and why state it? *Rubric:* 3 = home zone, work zone, birth year of targets; risk estimates depend on assumed knowledge;; 2 = lists knowledge only;; 1 = omits;; 0 = none.
- **EX028 — Pseudonymised result.** How many targets were re-identified in the pseudonymised file? *Rubric:* 3 = 415 of 500, 83.0%;; 2 = about four in five;; 1 = wrong;; 0 = none.
- **EX029 — Article 4(5).** Why is pseudonymised data still personal data under the GDPR? *Rubric:* 3 = Article 4(5) data can be re-attributed using additional information, so it stays in scope;; 2 = mentions re-attribution;; 1 = says it is anonymous;; 0 = none.
- **EX030 — Like for like.** Why is the H1 comparison "not like for like"? *Rubric:* 3 = different release types face different attacks; k-anonymity's residual risk lies in attacks not yet tried;; 2 = mentions different outputs;; 1 = accepts H1 outright;; 0 = none.
- **EX031 — Blind validation.** Why does the validation team work without Ines's code? *Rubric:* 3 = so errors in her code are not copied and their check is independent;; 2 = mentions independence;; 1 = says it is quicker;; 0 = none.
- **EX032 — Unplanned attack.** Why report the extra multi-day attack that weakened k-anonymity? *Rubric:* 3 = validation must be allowed to find problems; hiding it would bias the thesis;; 2 = mentions honesty;; 1 = omits it;; 0 = none.

### Synthesis

Chapter 5 measures risk under a stated attack and validates it independently. Chapter 6 faces peer critique and revises the claims.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes

You will (1) respond to substantive peer criticism; (2) narrow claims to what evidence supports; (3) distinguish legal, technical and ethical objections.

### 6.1 The critiques

Ines presents her draft at a doctoral workshop. Three critiques stand out. A statistician argues that synthetic populations may be less diverse than real ones, so uniqueness and linkage may be underestimated. A lawyer argues that the thesis treats epsilon as if it settled the legal question of anonymity under GDPR Recital 26, which it cannot do alone. A planner argues that rating tables on paper is not the same as using them in a real timetable meeting. Ines writes each critique down in full before responding, so that she answers what was actually said and not a weaker version.

### 6.2 Responding to the statistician

Ines accepts the point and tests it. She regenerates the synthetic population with a skewed distribution in which most riders live in a few dense zones, which is closer to real cities. Uniqueness falls slightly in dense zones and rises in sparse ones, but the overall conclusions do not change. She adds this sensitivity analysis to the thesis and narrows her claim: results hold for populations with similar structure, and a real-data replication inside the authority's secure environment, under its own legal basis and data protection impact assessment, is recommended as future work rather than assumed.

### 6.3 Responding to the lawyer

Ines agrees that the legal status of a release depends on all the means reasonably likely to be used to identify people, as Recital 26 puts it, including cost, time and available technology. Epsilon is evidence for that assessment, not a substitute for it. She rewrites her conclusion to say that differentially private counts with a documented budget give strong technical evidence that the authority can use in its anonymisation assessment, which its data protection officer and, where necessary, the supervisory authority must still judge. She also cites EDPB guidance on data protection by design as context for documenting such choices.

### 6.4 Responding to the planner

Ines cannot run real timetable meetings during the thesis, so she narrows H2 to "planners judge the tables usable in a structured review", and adds a limitation. She also proposes a follow-up in which one route review uses the released counts and planners record any decision that differs from the one they would make with exact data. The planner agrees that this is a fairer test. Ines notes in her revision log that two of the three critiques changed her claims, and that this is a normal and healthy outcome of peer review rather than a sign that the thesis was weak.

### Worked example

Ines turns three critiques into a sensitivity analysis, a narrower legal conclusion and a narrower utility claim, recording each change in a revision log.

> **Synthetic case.** Workshop participants are synthetic; GDPR Recital 26 and EDPB Guidelines 4/2019 are real.

### Errors and limits

Narrowing claims can go too far and leave nothing useful; Ines keeps the core result and limits only its reach.

### Exercises

- **EX033 — Diversity critique.** How does Ines test the statistician's critique? *Rubric:* 3 = regenerates a skewed population and reruns the analyses as a sensitivity check;; 2 = mentions rerunning;; 1 = dismisses it;; 0 = none.
- **EX034 — Reasonably likely means.** Why can epsilon not settle anonymity under Recital 26 alone? *Rubric:* 3 = Recital 26 asks about all means reasonably likely to identify, a legal judgement that uses technical evidence;; 2 = mentions the law;; 1 = says epsilon is enough;; 0 = none.
- **EX035 — Narrowed H2.** How does Ines narrow H2 after the planner's critique? *Rubric:* 3 = to usability judged in a structured review, with a limitation and a follow-up route test;; 2 = mentions narrowing;; 1 = keeps H2 unchanged;; 0 = none.
- **EX036 — Recording critiques.** Why write critiques down in full before responding? *Rubric:* 3 = to answer the actual argument, not a weaker version;; 2 = mentions accuracy;; 1 = omits;; 0 = none.
- **EX037 — Healthy revision.** Is it a weakness that two critiques changed her claims? *Rubric:* 3 = no; revising claims to match evidence is the purpose of review;; 2 = says it is fine;; 1 = says it is a failure;; 0 = none.
- **EX038 — Real-data replication.** What conditions does Ines attach to a future real-data replication? *Rubric:* 3 = inside the secure environment, with a legal basis and a DPIA;; 2 = names one;; 1 = omits;; 0 = none.

### Synthesis

Chapter 6 shows critique sharpening claims. Chapter 7 assembles the thesis and a reproducibility archive without leaking personal data.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes

You will (1) synthesise findings into defensible claims; (2) build a reproducibility archive; (3) check that no identifier leaves in supplementary files.

### 7.1 The synthesis

Ines writes her central claim carefully. Pseudonymisation alone leaves most synthetic riders re-identifiable. A well-chosen k-anonymised file resists simple linkage but leaks under multi-day attacks. Differentially private counts remove record linkage, with error that is negligible for busy routes and serious for quiet routes at low epsilon. Planners in a structured review accepted counts at epsilon one. The claim is bounded by the synthetic population, three planners and the attacks tested. She checks every sentence of the claim against a table, a figure or a lab output so that nothing in the conclusion floats free of evidence.

### 7.2 What goes in the archive

Thornbury requires a reproducibility archive. Ines includes the pre-registered protocol, the analysis code with its random seeds, the results tables and a short instruction file that explains how to rerun everything. Each file is listed in a manifest with its SHA-256 digest, so that any later change can be detected. She does not include the synthetic population itself, only the generator and its seed, because the population can be rebuilt exactly. This makes the archive small enough to deposit in the university repository while keeping every number in the thesis reproducible by an examiner with ordinary tools.

### 7.3 A leak caught

When Ines runs the archive check, it blocks one file. A sample rows file she had added to illustrate the data format contains a column named rider identifier with a token copied from an early test that used real card formats. Although the token is fictitious, the check is designed to stop exactly this kind of slip. She removes the file and replaces it with a format description. The episode illustrates why data protection by design, as described in Article 25 of the GDPR and the EDPB guidelines, includes the research outputs as well as the main system being studied.

### 7.4 Licensing and access

Ines publishes code under an open licence and states that the generator is synthetic and contains no personal data. She adds a data statement that explains what the archive contains, what it does not, and who to contact at the authority about access to real data under its own procedures. Prof. Aaltonen reminds her that open science and data protection are compatible when the archive is designed for both from the start. She records the statement in the thesis front matter as well as in the archive so that readers who never open the repository still understand its limits.

### Lab — Manifest and identifier check for the thesis archive

```python
# SHA-256 manifest for a synthetic thesis archive; the release check flags any file containing a raw rider id.
import hashlib
files = {"protocol.md": b"pre-registered protocol v3", "analysis.py": b"seed=7; epsilon grid", "results.csv": b"eps,mae\n0.1,10.1\n", "README.md": b"rerun: python3 analysis.py", "sample_rows.csv": b"rider_id,zone\nR-104233,12\n"}
for n, b in files.items():
    flag = "BLOCK (contains rider_id)" if b"rider_id" in b else "ok"
    print(f"{hashlib.sha256(b).hexdigest()[:16]}  {n:16s} {flag}")
```

Run with `python3 lab_archive.py`. Verified output:

```text
a52eebd60ecdcdf6  protocol.md      ok
fec505cc4b189e5f  analysis.py      ok
56ae8db2fd66c425  results.csv      ok
0859d3705f295926  README.md        ok
59ddbf48bee52954  sample_rows.csv  BLOCK (contains rider_id)
```

### Worked example

Ines writes a bounded central claim, builds a five-file manifest with SHA-256 digests and catches a sample file with a rider identifier column, which she replaces before deposit.

> **Synthetic case.** The archive files and the token are synthetic; GDPR Article 25 and EDPB Guidelines 4/2019 are real.

### Errors and limits

A keyword check catches only identifiers it is told to look for; free text can still leak. Digests prove integrity, not correctness.

### Exercises

- **EX039 — Bounded claim.** List the three bounds on Ines's central claim. *Rubric:* 3 = synthetic population, three planners, attacks tested;; 2 = lists two;; 1 = lists none;; 0 = none.
- **EX040 — Generator not data.** Why archive the generator and seed rather than the population? *Rubric:* 3 = it rebuilds the same population exactly and keeps the archive small;; 2 = mentions size;; 1 = archives everything;; 0 = none.
- **EX041 — Blocked file.** Which file did the check block, and why? *Rubric:* 3 = sample_rows.csv, because it contains a rider_id column;; 2 = names the file;; 1 = says none;; 0 = none.
- **EX042 — Digests role.** What does a SHA-256 manifest prove, and what not? *Rubric:* 3 = that files have not changed since listing; not that analyses are correct;; 2 = names one;; 1 = confuses them;; 0 = none.
- **EX043 — Design scope.** Why does data protection by design reach the research archive? *Rubric:* 3 = outputs can leak personal data just as systems can;; 2 = mentions outputs;; 1 = limits it to systems;; 0 = none.
- **EX044 — Data statement.** What should Ines's data statement explain? *Rubric:* 3 = contents, exclusions and how to request real-data access;; 2 = names one;; 1 = omits;; 0 = none.

### Synthesis

Chapter 7 produces a bounded claim and a clean archive. Chapter 8 prepares the defense and publication.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes

You will (1) prepare a doctoral defense around evidence and limits; (2) plan publications for distinct audiences; (3) translate findings into an organisational decision.

### 8.1 Preparing the defense

Ines prepares by listing the hardest questions she expects. Why should a synthetic population be trusted? Is epsilon one per year realistic for daily releases? Would a stronger attacker break the k-anonymous file further? For each she prepares a short answer that points to evidence and a limit. Prof. Aaltonen runs a mock defense in which he plays a hostile examiner, and she learns to answer "I do not know, but here is how I would find out" when the evidence runs out, instead of defending claims her data cannot support in front of the committee.

### 8.2 The defense

At the defense, the external examiner, a privacy engineer, presses on budget accounting. Ines explains that her study used epsilon one per table, and that a year of daily tables under simple composition would give a much larger total, so the authority must choose a yearly budget and accept larger daily error, or publish less often. The examiner accepts the answer and asks that the thesis state this trade-off in the abstract. The committee passes the thesis with minor corrections, one of which adds a sentence on composition to the abstract and another clarifies the multi-day attack.

### 8.3 Publication plan

Ines plans three outputs for three audiences. A journal article reports the controlled comparison and the independent validation for researchers. A short practitioner guide explains, without equations, why pseudonymisation is not anonymisation and how to choose between release methods. A briefing for Valemont's board recommends stopping the token-only release and piloting differentially private counts for busy routes, while keeping restricted access for quiet routes. Each output cites the same archive, so readers in every audience can trace claims to the same evidence and examine the code that produced each number.

### 8.4 The organisational decision

Valemont's board adopts the recommendation. Its data protection officer records the reasoning in the authority's records, with a data protection impact assessment for the new release process, as Article 35 of the GDPR requires where processing is likely to result in a high risk. The board also asks Ines to present the result to other transit authorities. She agrees, but only with the bounded claim and its limits, and she reminds them that their own populations and attackers may differ. Her final reflection is that the thesis changed one real decision because every claim was falsifiable and documented.

### Worked example

Ines prepares hard questions, defends a budget-accounting trade-off, plans a journal article, a practitioner guide and a board briefing, and sees Valemont replace token-only releases with a documented differentially private pilot.

> **Synthetic case.** The defense, board and examiner are synthetic; GDPR Articles 25 and 35 are real.

### Errors and limits

A successful defense is not proof of universal truth; other authorities must validate in their own context.

### Exercises

- **EX045 — Unknown answers.** How should Ines answer when evidence runs out in a defense? *Rubric:* 3 = admit the limit and explain how she would find out;; 2 = admits uncertainty;; 1 = defends anyway;; 0 = none.
- **EX046 — Yearly budget.** What trade-off did the examiner want stated in the abstract? *Rubric:* 3 = a yearly budget forces larger daily error or less frequent publication;; 2 = mentions composition;; 1 = omits;; 0 = none.
- **EX047 — Three audiences.** Name Ines's three outputs and audiences. *Rubric:* 3 = journal article for researchers, guide for practitioners, briefing for the board;; 2 = names two;; 1 = names one;; 0 = none.
- **EX048 — Board recommendation.** What did the board briefing recommend? *Rubric:* 3 = stop token-only release, pilot DP counts for busy routes, restricted access for quiet ones;; 2 = two parts;; 1 = one part;; 0 = none.
- **EX049 — Article 35 role.** Why does the new release process need a DPIA? *Rubric:* 3 = Article 35 requires one where processing is likely to result in high risk;; 2 = mentions risk;; 1 = says optional;; 0 = none.
- **EX050 — Transfer caution.** What caution does Ines give other authorities? *Rubric:* 3 = their populations and attackers may differ, so they must validate locally;; 2 = mentions difference;; 1 = says results transfer;; 0 = none.

### Synthesis

Chapter 8 closes the doctoral track with a defended, bounded result and one changed decision. The worked results follow, then the references.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Ines Carvalho, Prof. Henrik Aaltonen, Thornbury University, Valemont Regional Transit Authority and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Ines states beforehand that no reduction in linkage risk, or error planners reject, would refute her claim, so data can prove her wrong.

**EX002.** Because the GDPR and LGPD exclude truly anonymous data from their scope, calling a release anonymous removes legal duties; the claim must therefore be technically justified.

**EX003.** A synthetic population lets her test attacks and publish without exposing real riders, keeping the research from causing the harm it measures.

**EX004.** Adding birth year moves uniqueness from 0.0% to 83.4%; it divides each home-work pair into dozens of tiny groups.

**EX005.** A unique row only becomes a named person when an attacker holds outside data matching that combination; uniqueness is a precondition, not proof.

**EX006.** Declaring no interest in anonymisation products lets examiners and the authority trust that the comparison is not tilted toward a product she sells.

**EX007.** It prevents her from picking the error metric or epsilon grid after seeing which choice favours her preferred method.

**EX008.** It asks whether that flow matches the norms of the context in which riders shared journeys; if planners' use breaks those norms, the flow is inappropriate.

**EX009.** Information collection, information processing, information dissemination and invasion.

**EX010.** If every member of a k-anonymous group shares the same sensitive value, the attacker learns it without singling anyone out; l-diversity requires variety.

**EX011.** Transit histories, like film ratings, are sparse and distinctive; knowing a few trips can link a pseudonymous history to a person.

**EX012.** For a count, one person changes the answer by at most one; Laplace noise with scale 1/epsilon is calibrated to that bound.

**EX013.** Its guarantee does not depend on what the attacker already knows, while k-anonymity assumes a particular set of quasi-identifiers.

**EX014.** Few studies compare k-anonymised records and differentially private counts on the same release, under the same attack, with users' acceptance as the utility test.

**EX015.** H2 names who judges, how they rate and the pass threshold of two out of three, all fixed before data exist.

**EX016.** With exact values nearly every rider is unique, so every record falls in a class smaller than five and all 20,000 would be suppressed.

**EX017.** It suppresses just 24 of 20,000 while keeping 1,400 classes; eight-zone blocks merge suburbs planners must distinguish.

**EX018.** A weak baseline exaggerates the advantage of differential privacy, so the study would mislead the authority.

**EX019.** Unlabelled tables prevent planners from favouring the method they expect to be better.

**EX020.** Acceptance shows whether the data serve real decisions, while mean absolute error makes the result comparable with the literature.

**EX021.** Matching the theoretical error shows her implementation is correct, so later differences reflect the method, not a bug.

**EX022.** The lab reports 0.98, close to the predicted 1/epsilon = 1.0.

**EX023.** Large counts dominate the average, while quiet routes, which drive service decisions, see relative errors of 22–94% at low epsilon.

**EX024.** 22.0% mean relative error on the five small cells.

**EX025.** Privacy loss adds up across releases; epsilon one per daily table means a much weaker annual guarantee than epsilon one per year.

**EX026.** Noisy counts can be negative; post-processing such as rounding is safe for privacy but changes error, and the pilot ignores it.

**EX027.** The attacker knows three quasi-identifiers for 500 targets; stating this matters because risk depends on what the attacker knows.

**EX028.** 415 of 500 targets (83.0%) were re-identified with certainty.

**EX029.** Article 4(5) defines pseudonymised data as re-attributable with separately kept information; it therefore remains personal data.

**EX030.** Records and counts are attacked differently; the k-anonymous file's remaining risk shows up in other attacks, such as multi-day linkage.

**EX031.** Without her code they cannot repeat her mistakes, so agreement is real evidence.

**EX032.** Reporting the multi-day weakness shows the validation was genuine and gives the authority a complete risk picture.

**EX033.** She builds a skewed population closer to real cities and reruns uniqueness and linkage; conclusions hold, and she narrows the claim.

**EX034.** Recital 26 considers all means reasonably likely to be used, including cost and technology; epsilon informs but does not replace that judgement.

**EX035.** H2 now claims usability in a structured review only, with a stated limitation and a proposed real route review.

**EX036.** Recording each critique exactly prevents answering a straw man.

**EX037.** No; narrowing claims in response to valid critique is what peer review is for.

**EX038.** It must happen inside the authority's secure environment, under its own legal basis and after a data protection impact assessment.

**EX039.** The claim is bounded by the synthetic population, the three-planner panel and the specific attacks tested.

**EX040.** The seeded generator recreates the population exactly, so the archive stays small and reproducible.

**EX041.** sample_rows.csv was blocked because it contained a rider_id column with a card-style token.

**EX042.** It proves integrity since the manifest was made, not that the code or conclusions are correct.

**EX043.** Supplementary files are processing outputs too; designing them to exclude identifiers applies Article 25 thinking to research.

**EX044.** It explains what the archive contains, what it excludes and whom to contact about access to real data.

**EX045.** She says she does not know and explains the study that would answer it.

**EX046.** Daily releases spend budget; a fixed yearly epsilon means larger daily error or fewer releases.

**EX047.** A journal article for researchers, a practitioner guide and a board briefing for Valemont.

**EX048.** Stop pseudonymised token releases, pilot differentially private counts for busy routes and keep restricted access for quiet ones.

**EX049.** Publishing derived travel data is likely high risk, so Article 35 requires a data protection impact assessment.

**EX050.** Results are bounded; other authorities must test their own populations and attackers.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Dwork, C., McSherry, F., Nissim, K., & Smith, A. (2006). Calibrating noise to sensitivity in private data analysis. *Theory of Cryptography (TCC 2006)*, 265–284. <https://doi.org/10.1007/11681878_14>
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. <https://doi.org/10.1561/0400000042>
- European Data Protection Board. (2020). *Guidelines 4/2019 on Article 25 Data Protection by Design and by Default* (Version 2.0, adopted 20 October 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S. L. (2015). *De-identification of personal information* (NISTIR 8053). NIST. <https://doi.org/10.6028/NIST.IR.8053>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). NIST. <https://doi.org/10.6028/NIST.SP.800-188>
- Li, N., Li, T., & Venkatasubramanian, S. (2007). t-Closeness: Privacy beyond k-anonymity and l-diversity. *IEEE 23rd ICDE*, 106–115. <https://doi.org/10.1109/ICDE.2007.367856>
- Machanavajjhala, A., Kifer, D., Gehrke, J., & Venkitasubramaniam, M. (2007). l-Diversity: Privacy beyond k-anonymity. *ACM TKDD, 1*(1), 3. <https://doi.org/10.1145/1217299.1217302>
- Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. <https://doi.org/10.1109/SP.2008.33>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Nissenbaum, H. (2009). *Privacy in context: Technology, policy, and the integrity of social life*. Stanford University Press. <https://doi.org/10.1515/9780804772891>
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
- Warren, S. D., & Brandeis, L. D. (1890). The right to privacy. *Harvard Law Review, 4*(5), 193–220. <https://doi.org/10.2307/1321160>
