# Security Operations and Blue Team: Master's Course

- Language: English (`en`); course 176, Master's course (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: master's students who will design, run and defend an applied study of security-operations practice.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one dissertation on allow-list tuning of noisy detection rules from research question to defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Tariq Haddad** | Master's student and part-time SOC analyst | Invented |
| **Dr. Ingrid Solberg** | Supervisor | Invented |
| **Marcus Bell** | SOC lead | Invented |
| **Ashworth Institute of Technology** | Fictional university | Invented |
| **Pelham Water Utility** | Fictional host organisation | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn a practical SOC problem into a researchable question; (2) run a structured literature search; (3) appraise sources by type and strength; (4) keep a reproducible search log.

### 1.1 From problem to question

**Tariq Haddad**, a master's student at the fictional **Ashworth Institute of Technology**, works part-time in the corporate SOC of the fictional **Pelham Water Utility**. Analysts complain of "too many alerts". That is a problem, not a question. With supervisor **Dr. Ingrid Solberg**, Tariq narrows it: "Does adding reviewed allow-lists to the ten noisiest detection rules reduce weekly alert volume without suppressing true attacks, compared with untuned rules over the same weeks?"

Section one point one develops research question and literature method with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

### 1.2 Parts of a good question

The question names an intervention (allow-lists), a population (ten rules, one SOC), a comparison (untuned rules), outcomes (volume and suppressed attacks) and a time frame. Each part can be measured.

Section one point two develops research question and literature method with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section one point two, Dr. Ingrid Solberg expects research claims to carry owners and dates.

Section one point two treats from problem to question as testable only when evidence and ticket IDs are recorded.

### 1.3 Searching the literature

Tariq searches digital libraries (ACM, IEEE, USENIX) and grey literature (NIST, MITRE) with recorded terms: "alert fatigue", "false positive" AND "security operations", "detection tuning", "SOC" AND "qualitative". He records dates, databases and hit counts.

Section one point three develops research question and literature method with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section one point three, Dr. Ingrid Solberg expects research claims to carry owners and dates.

Section one point three treats from problem to question as testable only when evidence and ticket IDs are recorded.

### 1.4 Appraising sources

Peer-reviewed empirical studies, such as Alahmadi, Axon and Martinovic (2022) on benign triggers, carry more weight than vendor blogs. Frameworks — NIST SP 800-92 on log management, the SigmaHQ rule format — define practice but are not evidence of effect. Tariq tags each source by type.

Section one point four develops research question and literature method with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section one point four, Dr. Ingrid Solberg expects research claims to carry owners and dates.

Section one point four treats from problem to question as testable only when evidence and ticket IDs are recorded.

### 1.5 What the literature says

Analysts report most alarms are benign triggers (Alahmadi et al., 2022); low base rates make false alarms dominate (Axelsson, 2000); mismatched incentives distort SOC metrics (Kokulu et al., 2019). Little published work measures tuning effects with a comparison group.

Section one point five develops research question and literature method with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section one point five, Dr. Ingrid Solberg expects research claims to carry owners and dates.

Section one point five treats from problem to question as testable only when evidence and ticket IDs are recorded.

### 1.6 The search log

The log lets a reader rerun the search and see why sources were included or excluded.

Section one point six develops research question and literature method with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section one point six, Dr. Ingrid Solberg expects research claims to carry owners and dates.

Section one point six treats from problem to question as testable only when evidence and ticket IDs are recorded.

For section one point six, Ashworth Institute of Technology will not accept research work without a written trail.

### Worked example

Tariq's search log entry: "2026-02-03, ACM DL, ('alert fatigue' OR 'false positive') AND ('security operations' OR SOC), 2010–2026: 214 hits; 31 screened by abstract; 9 included. Exclusions: 12 network-IDS algorithm papers without analyst data; 10 duplicates."

> **Synthetic case.** Ashworth, Pelham Water Utility and all people are invented.

### Errors and limits

Searches miss industry reports behind paywalls; note this as a limitation.

### Exercises

- **EX001 — Problem versus question.** Why is "too many alerts" not yet a research question? *Rubric:* 3 = no intervention, comparison, measurable outcome or time frame; 2 = partial; 1 = it is; 0 = none.
- **EX002 — Question parts.** Name the five parts of Tariq's question. *Rubric:* 3 = intervention, population, comparison, outcomes, time; 2 = three; 1 = one; 0 = none.
- **EX003 — Search record.** What does Tariq record for each search? *Rubric:* 3 = date, database, terms, hits, screening counts; 2 = three; 1 = one; 0 = none.
- **EX004 — Source weight.** Compare the evidential weight of Alahmadi et al. and a vendor blog. *Rubric:* 3 = peer-reviewed empirical vs unreviewed marketing; 2 = partial; 1 = equal; 0 = none.
- **EX005 — Frameworks.** What role do NIST SP 800-92 and Sigma play in the review? *Rubric:* 3 = define practice/format, not evidence of effect; 2 = partial; 1 = evidence; 0 = none.
- **EX006 — Gap.** State the gap Tariq's study addresses. *Rubric:* 3 = few measurements of tuning effects with comparison group; 2 = partial; 1 = none; 0 = none.
- **EX007 — Exclusions.** Why were network-IDS algorithm papers excluded? *Rubric:* 3 = no analyst/operational data relevant to the question; 2 = partial; 1 = random; 0 = none.

### Synthesis

A researchable question has measurable parts; a logged, appraised literature search shows where it fits.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Security operations and blue team: advanced seminar

### Learning outcomes

You will (1) discuss SOC models and functions critically; (2) relate detection engineering to frameworks; (3) debate metrics and their side effects; (4) present a seminar argument with sources.

### 2.1 What a SOC does

Knerler, Parker and Zimmerman (2022) describe SOC functions from monitoring and analysis to incident response, threat intelligence and expanded services such as hunting. Their first strategy, "know what you are protecting and why", anchors tuning decisions: a rule matters according to the assets it guards.

Section two point one develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section two point one, Dr. Ingrid Solberg expects security claims to carry owners and dates.

### 2.2 Detection engineering

Detections are written, tested, deployed and maintained like software. MITRE ATT&CK (Strom et al., 2018) gives a shared vocabulary of adversary behaviour so coverage can be mapped; Sigma gives a portable rule format. D3FEND (Kaloroumakis and Smith, 2021) maps defensive techniques, helping teams see which countermeasure a detection belongs to.

Section two point two develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section two point two, Dr. Ingrid Solberg expects security claims to carry owners and dates.

### 2.3 Continuous monitoring

NIST SP 800-137 frames monitoring as an ongoing programme tied to risk, with defined frequencies and metrics, not a set of tools.

Section two point three develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section two point three, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section two point three treats what soc does detection as testable only when evidence and ticket IDs are recorded.

For section two point three, Ashworth Institute of Technology will not accept security work without a written trail.

### 2.4 Metrics and side effects

Counting closed alerts rewards speed over depth; mean time to resolve can push analysts to close uncertain cases. Kokulu et al. (2019) found such metric mismatches a frequent issue. Tariq's seminar argues that tuning studies must measure suppressed attacks alongside volume, or they reward silence.

Section two point four develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section two point four, Dr. Ingrid Solberg expects security claims to carry owners and dates.

### 2.5 Maturity models

The SOC-CMM (van Os, 2016) assesses business, people, process, technology and services domains. It helps place tuning within process maturity rather than treating it as a one-off clean-up.

Section two point five develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section two point five, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section two point five treats what soc does detection as testable only when evidence and ticket IDs are recorded.

### 2.6 Seminar format

Each student presents a claim, evidence, counter-evidence and a question for discussion.

Section two point six develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section two point six, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section two point six treats what soc does detection as testable only when evidence and ticket IDs are recorded.

For section two point six, Ashworth Institute of Technology will not accept security work without a written trail.

### Worked example

Tariq's seminar claim: "Alert-volume reduction is a misleading success metric on its own." Evidence: Axelsson's base-rate argument and Kokulu et al. on metrics. Counter-evidence: Alahmadi et al. report that volume itself drives burnout, so reduction has value. Question: "What suppressed-attack rate would you accept for a 30% volume cut?"

> **Synthetic case.** The seminar is invented.

### Errors and limits

Frameworks change versions; cite the version used.

### Exercises

- **EX008 — Strategy one.** How does "know what you are protecting and why" guide tuning? *Rubric:* 3 = rule value depends on assets guarded; 2 = partial; 1 = vague; 0 = none.
- **EX009 — ATT&CK use.** What does ATT&CK provide to detection engineering? *Rubric:* 3 = shared behaviour vocabulary for mapping coverage; 2 = partial; 1 = exploits; 0 = none.
- **EX010 — D3FEND use.** What does D3FEND add? *Rubric:* 3 = map of defensive techniques/countermeasures; 2 = partial; 1 = same as ATT&CK; 0 = none.
- **EX011 — Monitoring programme.** How does SP 800-137 frame monitoring? *Rubric:* 3 = ongoing risk-tied programme with frequencies and metrics; 2 = partial; 1 = tools; 0 = none.
- **EX012 — Metric side effect.** Give one metric side effect. *Rubric:* 3 = e.g. closed-count rewards speed over depth; 2 = partial; 1 = none; 0 = none.
- **EX013 — Counter-evidence.** What counter-evidence did Tariq present? *Rubric:* 3 = Alahmadi et al.: volume drives burnout, so reduction has value; 2 = partial; 1 = none; 0 = none.
- **EX014 — Maturity framing.** How does SOC-CMM change the view of tuning? *Rubric:* 3 = part of process maturity, not one-off clean-up; 2 = partial; 1 = none; 0 = none.

### Synthesis

Advanced SOC practice links detections to frameworks, assets and maturity, and judges metrics by their side effects.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) choose a design suited to an operational intervention; (2) plan ethics and data protection; (3) make the study reproducible; (4) define ground truth for "suppressed attack".

### 3.1 Design choice

Random assignment of rules to tuning is possible but the SOC wants its noisiest rules fixed first. Tariq uses a controlled before-after design: ten tuned rules and ten comparable untuned rules, four weeks before and four after. Comparing changes in both groups removes effects common to all rules.

Section three point one develops study design ethics and reproducibility with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section three point one, Dr. Ingrid Solberg expects study claims to carry owners and dates.

### 3.2 Ground truth for attacks

Real attacks are rare and unknown in advance. With the CISO's approval, the utility's authorised purple-team exercises inject benign simulated behaviour matching rule logic during the study, logged with exact times. A "suppressed attack" is an injected event that matched a rule but was removed by an allow-list.

Section three point two develops study design ethics and reproducibility with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section three point two, Dr. Ingrid Solberg expects study claims to carry owners and dates.

### 3.3 Ethics

Alerts contain user names. Tariq's data is pseudonymised before leaving the SOC; only the SOC sees real names. Ethics approval covers analyst interviews. The purple-team scope is signed by the CISO and excludes operational technology networks entirely.

Section three point three develops study design ethics and reproducibility with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section three point three, Dr. Ingrid Solberg expects study claims to carry owners and dates.

Section three point three treats design choice ground truth as testable only when evidence and ticket IDs are recorded.

### 3.4 Reproducibility

Allow-list entries are version-controlled with reasons; analysis scripts and counts are archived; the rule set is stored in Sigma format with tuning diffs.

Section three point four develops study design ethics and reproducibility with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section three point four, Dr. Ingrid Solberg expects study claims to carry owners and dates.

Section three point four treats design choice ground truth as testable only when evidence and ticket IDs are recorded.

For section three point four, Ashworth Institute of Technology will not accept study work without a written trail.

### 3.5 Threats to validity

Seasonal change, log-source outages, other tuning by colleagues, and analysts' awareness of the study. Each has a planned check.

Section three point five develops study design ethics and reproducibility with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section three point five, Dr. Ingrid Solberg expects study claims to carry owners and dates.

Section three point five treats design choice ground truth as testable only when evidence and ticket IDs are recorded.

For section three point five, Ashworth Institute of Technology will not accept study work without a written trail.

### 3.6 Registration

The design, outcomes and checks are registered with the supervisor before week 1.

Section three point six develops study design ethics and reproducibility with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section three point six, Dr. Ingrid Solberg expects study claims to carry owners and dates.

Section three point six treats design choice ground truth as testable only when evidence and ticket IDs are recorded.

For section three point six, Ashworth Institute of Technology will not accept study work without a written trail.

### Stopping rule

If any injected event is suppressed, the responsible allow-list entry is reviewed within a day; the study continues, but the finding is recorded and the entry may be narrowed.

### Worked example

Tariq's design table: "Groups: T (10 tuned) and C (10 untuned, matched on volume and ATT&CK tactic). Weeks 1–4 baseline, 5–8 tuned. Primary: weekly alerts per group. Safety: injected purple-team events per rule (8 total) and how many were suppressed. Data: pseudonymised at source."

> **Synthetic case.** The design is invented.

### Errors and limits

Injected events test only behaviours that were injected; real attackers may differ.

### Exercises

- **EX015 — Design selection.** Why a controlled before-after design rather than randomisation? *Rubric:* 3 = SOC wants noisiest rules tuned; comparison group removes common effects; 2 = partial; 1 = easier; 0 = none.
- **EX016 — Ground truth.** How is "suppressed attack" defined and measured? *Rubric:* 3 = authorised injected events matching a rule removed by allow-list; logged times; 2 = partial; 1 = real attacks; 0 = none.
- **EX017 — Purple-team limits.** What limits applied to the purple-team scope? *Rubric:* 3 = CISO-signed; excludes OT networks; benign simulations; 2 = two; 1 = one; 0 = none.
- **EX018 — Pseudonymisation.** Where does pseudonymisation happen, and why there? *Rubric:* 3 = at source in SOC; names never leave; 2 = partial; 1 = later; 0 = none.
- **EX019 — Validity threats.** List three threats to validity. *Rubric:* 3 = seasonal change, outages, other tuning, awareness (three); 2 = two; 1 = one; 0 = none.
- **EX020 — Matching.** On what were control rules matched? *Rubric:* 3 = volume and ATT&CK tactic; 2 = one; 1 = random; 0 = none.

### Synthesis

Operational studies need comparison groups, defined ground truth, protected data and registered threats to validity.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Security operations and blue team: competing explanations

### Learning outcomes

You will (1) list competing explanations for an observed change; (2) use a comparison group to remove shared effects; (3) test specific alternatives with data; (4) state what remains uncertain.

### 4.1 The observation

After allow-lists were added in week 5, alerts from the ten tuned rules fell sharply. Tempting conclusion: tuning worked. But other things happened in weeks 5–8: a public holiday, a SIEM upgrade and a firewall log source migration.

Section four point one develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section four point one, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section four point one treats the observation comparison group as testable only when evidence and ticket IDs are recorded.

### 4.2 Comparison group

If the drop were due to the holiday or the SIEM upgrade, untuned rules should fall too. Difference-in-differences subtracts the control group's change from the tuned group's change.

Section four point two develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section four point two, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section four point two treats the observation comparison group as testable only when evidence and ticket IDs are recorded.

### Lab — difference-in-differences

```python
"""Difference-in-differences on synthetic weekly alert counts.
Tuned group: rules given allow-lists in week 5. Control group: untuned rules."""
tuned   = [410, 395, 402, 420, 230, 241, 225, 236]
control = [300, 290, 305, 310, 262, 270, 258, 266]
def mean(x): return sum(x) / len(x)
t_pre, t_post = mean(tuned[:4]), mean(tuned[4:])
c_pre, c_post = mean(control[:4]), mean(control[4:])
print(f"tuned   pre={t_pre:.1f} post={t_post:.1f} change={t_post-t_pre:.1f}")
print(f"control pre={c_pre:.1f} post={c_post:.1f} change={c_post-c_pre:.1f}")
print(f"difference-in-differences = {(t_post-t_pre)-(c_post-c_pre):.1f} alerts/week")
```

Run with `python3 lab_did.py`. Verified output:

```text
tuned   pre=406.8 post=233.0 change=-173.8
control pre=301.2 post=264.0 change=-37.2
difference-in-differences = -136.5 alerts/week
```

### 4.3 Reading the result

Tuned rules fell from 406.8 to 233.0 alerts per week (−173.8). Control rules also fell, from 301.2 to 264.0 (−37.2), showing a shared effect. The net estimate attributable to tuning is −136.5 alerts per week.

Section four point three develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section four point three, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section four point three treats the observation comparison group as testable only when evidence and ticket IDs are recorded.

### 4.4 Testing specific alternatives

**Log-source outage:** ingestion counts per source show no gaps in weeks 5–8. **Firewall migration:** none of the tuned rules use firewall logs. **Colleague tuning:** the change log shows no other edits to the twenty rules. **Holiday:** affects both groups; absorbed by the comparison.

Section four point four develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section four point four, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section four point four treats the observation comparison group as testable only when evidence and ticket IDs are recorded.

### 4.5 Parallel trends

Difference-in-differences assumes both groups would have moved alike without tuning. In weeks 1–4 their trends are similar (both roughly flat), which supports but does not prove the assumption.

Section four point five develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section four point five, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section four point five treats the observation comparison group as testable only when evidence and ticket IDs are recorded.

### 4.6 Remaining uncertainty

Eight weeks is short; the estimate's interval is wide because weekly counts vary. Tariq reports the point estimate with a bootstrap interval in the dissertation.

Section four point six develops security operations and blue team with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section four point six, Dr. Ingrid Solberg expects security claims to carry owners and dates.

Section four point six treats the observation comparison group as testable only when evidence and ticket IDs are recorded.

### Worked example

Tariq's alternatives table: each explanation, the evidence that would support it, the check run and the result. Only the tuning explanation survives all checks; the holiday explains the control group's fall.

> **Synthetic case.** Counts come from the lab script.

### Errors and limits

Comparison groups remove shared effects only; something affecting tuned rules alone would still bias the estimate.

### Exercises

- **EX021 — Alternatives list.** Name three competing explanations for the drop. *Rubric:* 3 = holiday, SIEM upgrade, firewall migration (or outage/colleague tuning); 2 = two; 1 = one; 0 = none.
- **EX022 — DiD logic.** Explain difference-in-differences in one sentence. *Rubric:* 3 = subtract control change from treated change to remove shared effects; 2 = partial; 1 = vague; 0 = none.
- **EX023 — Lab estimate.** Give both group changes and the net estimate. *Rubric:* 3 = −173.8, −37.2, −136.5; 2 = two; 1 = one; 0 = none.
- **EX024 — Specific checks.** How was the firewall migration ruled out? *Rubric:* 3 = tuned rules do not use firewall logs; 2 = partial; 1 = assumed; 0 = none.
- **EX025 — Parallel trends.** What assumption does the method need, and what supports it? *Rubric:* 3 = parallel trends; similar flat pre-period; 2 = assumption only; 1 = none; 0 = none.
- **EX026 — Residual bias.** What could still bias the estimate? *Rubric:* 3 = something affecting tuned rules only; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Before crediting an intervention, list rivals, subtract shared effects and test the rest one by one.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a dissertation proposal; (2) plan a labelling sample efficiently; (3) pilot data collection and labelling; (4) adjust the plan from the pilot.

### 5.1 The proposal

Sections: background and gap; question and hypotheses; design; data and ethics; analysis; validity threats; timeline; risks. Dr. Solberg asks for one page per section at most.

Section five point one develops proposal and pilot with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section five point one, Dr. Ingrid Solberg expects proposal claims to carry owners and dates.

Section five point one treats the proposal why label as testable only when evidence and ticket IDs are recorded.

For section five point one, Ashworth Institute of Technology will not accept proposal work without a written trail.

### 5.2 Why label a sample

Volume alone cannot show whether suppressed alerts were benign. Tariq will manually label a sample of alerts as benign trigger, false positive or true positive, to estimate how much of the reduction removed only benign noise. Labelling all 4,000 alerts is impossible; a stratified sample by severity gives precise estimates where it matters.

Section five point two develops proposal and pilot with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section five point two, Dr. Ingrid Solberg expects proposal claims to carry owners and dates.

### Lab — stratified sample

```python
"""Stratified sample of synthetic alerts for manual labelling."""
import random
random.seed(7)
population = {"high": 120, "medium": 900, "low": 2980}
budget = 200
total = sum(population.values())
alloc = {k: max(20, round(budget * v / total)) for k, v in population.items()}
over = sum(alloc.values()) - budget
alloc["low"] -= over
for k, v in population.items():
    ids = random.sample(range(v), alloc[k])
    print(f"{k:6} population={v:5} sampled={alloc[k]:3} first ids={sorted(ids)[:3]}")
print("total sampled", sum(alloc.values()))
```

Run with `python3 lab_strata.py`. Verified output:

```text
high   population=  120 sampled= 20 first ids=[4, 6, 7]
medium population=  900 sampled= 45 first ids=[47, 50, 60]
low    population= 2980 sampled=135 first ids=[16, 49, 92]
total sampled 200
```

### 5.3 Reading the result

With a budget of 200, proportional allocation would give the high-severity stratum only 6 alerts, too few to estimate anything. A minimum of 20 is set, giving high 20, medium 45, low 135. A fixed seed (7) makes the draw reproducible; estimates for the whole population are reweighted by stratum size.

Section five point three develops proposal and pilot with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section five point three, Dr. Ingrid Solberg expects proposal claims to carry owners and dates.

Section five point three treats the proposal why label as testable only when evidence and ticket IDs are recorded.

### 5.4 The pilot

Tariq and a SOC colleague label 30 alerts independently. They disagree on 6, mostly "benign trigger" versus "false positive". The definitions are sharpened: a benign trigger is the intended behaviour occurring legitimately; a false positive is the rule matching behaviour it was not meant to catch.

Section five point four develops proposal and pilot with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section five point four, Dr. Ingrid Solberg expects proposal claims to carry owners and dates.

Section five point four treats the proposal why label as testable only when evidence and ticket IDs are recorded.

### 5.5 Logistics found

Exporting alerts with pseudonymised fields took two hours by hand; Tariq scripts it. The SOC's ticket system truncates notes; he uses the SIEM export instead.

Section five point five develops proposal and pilot with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section five point five, Dr. Ingrid Solberg expects proposal claims to carry owners and dates.

Section five point five treats the proposal why label as testable only when evidence and ticket IDs are recorded.

For section five point five, Ashworth Institute of Technology will not accept proposal work without a written trail.

### 5.6 Proposal approval

Solberg and the SOC lead **Marcus Bell** sign the proposal; the CISO signs the purple-team annex.

Section five point six develops proposal and pilot with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section five point six, Dr. Ingrid Solberg expects proposal claims to carry owners and dates.

Section five point six treats the proposal why label as testable only when evidence and ticket IDs are recorded.

For section five point six, Ashworth Institute of Technology will not accept proposal work without a written trail.

### Worked example

Proposal timeline: "Weeks 1–4 baseline and labelling of baseline sample; week 5 allow-lists deployed after peer review; weeks 5–8 follow-up; week 9 purple-team summary; weeks 10–14 analysis and writing."

> **Synthetic case.** Sample figures come from the lab script.

### Errors and limits

Minimum stratum sizes improve small-stratum estimates but require reweighting; forgetting this biases totals.

### Exercises

- **EX027 — Proposal sections.** List six proposal sections. *Rubric:* 3 = six of background, question, design, data/ethics, analysis, threats, timeline, risks; 2 = four; 1 = two; 0 = none.
- **EX028 — Why sample.** Why label a sample instead of relying on volume? *Rubric:* 3 = volume cannot show whether removed alerts were benign; all too many; 2 = partial; 1 = no reason; 0 = none.
- **EX029 — Allocation.** Give the stratum allocations and why high gets 20. *Rubric:* 3 = 20/45/135; proportional gives 6, too few; 2 = numbers only; 1 = wrong; 0 = none.
- **EX030 — Reweighting.** Why reweight estimates? *Rubric:* 3 = sample not proportional; reweight by stratum size to avoid bias; 2 = partial; 1 = no need; 0 = none.
- **EX031 — Definitions sharpened.** How were benign trigger and false positive distinguished? *Rubric:* 3 = intended behaviour legitimate vs unintended match; 2 = partial; 1 = same; 0 = none.
- **EX032 — Signatures.** Who signed the proposal and annex? *Rubric:* 3 = Solberg and Bell; CISO for purple-team annex; 2 = partial; 1 = none; 0 = none.

### Synthesis

A proposal sets the plan; a pilot tests definitions and logistics; sampling makes manual labelling feasible and reproducible.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) collect operational data under the approved protocol; (2) evaluate allow-lists against injected ground truth; (3) combine volume, labels and safety outcomes; (4) handle unexpected findings properly.

### 6.1 Collection

Weekly exports from the SIEM give alert counts per rule, pseudonymised at source. The labelling sample is drawn with the registered seed. Purple-team events are logged by the exercise lead with exact times.

Section six point one develops data collection and analysis with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section six point one, Dr. Ingrid Solberg expects data claims to carry owners and dates.

Section six point one treats collection labelling results checking as testable only when evidence and ticket IDs are recorded.

### 6.2 Labelling results

Of the reweighted sample of alerts removed by allow-lists, an estimated 93% were benign triggers, 6% false positives and 1% unresolved. This supports the claim that tuning removed mostly legitimate activity.

Section six point two develops data collection and analysis with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section six point two, Dr. Ingrid Solberg expects data claims to carry owners and dates.

Section six point two treats collection labelling results checking as testable only when evidence and ticket IDs are recorded.

### 6.3 Checking allow-lists against ground truth

Allow-list entries suppress alerts for specific rule, host and account combinations. The concern is that an attacker using an allow-listed account on an allow-listed host would be hidden.

Section six point three develops data collection and analysis with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section six point three, Dr. Ingrid Solberg expects data claims to carry owners and dates.

Section six point three treats collection labelling results checking as testable only when evidence and ticket IDs are recorded.

### Lab — allow-list replay

```python
"""Apply an allow-list to synthetic labelled alerts; check for suppressed attacks."""
alerts = [
    ("ps-encoded", "SCADA-HIST01", "svc_backup", "benign"),
    ("ps-encoded", "SCADA-HIST01", "svc_backup", "benign"),
    ("ps-encoded", "FIN-PC07", "a.moss", "attack"),
    ("new-service", "PATCH-SRV2", "svc_patch", "benign"),
    ("new-service", "PATCH-SRV2", "svc_patch", "attack"),
    ("new-service", "HR-PC03", "j.ward", "benign"),
    ("rdp-logon", "JUMP01", "it.admin", "benign"),
    ("rdp-logon", "JUMP01", "it.admin", "benign"),
]
allow = {("ps-encoded", "SCADA-HIST01", "svc_backup"), ("new-service", "PATCH-SRV2", "svc_patch"), ("rdp-logon", "JUMP01", "it.admin")}
kept = [a for a in alerts if a[:3] not in allow]
suppressed = [a for a in alerts if a[:3] in allow]
print("alerts", len(alerts), "kept", len(kept), "suppressed", len(suppressed))
print("attacks kept", sum(a[3] == "attack" for a in kept), "attacks suppressed", sum(a[3] == "attack" for a in suppressed))
for a in suppressed:
    if a[3] == "attack": print("SUPPRESSED ATTACK:", a[:3])
```

Run with `python3 lab_allow.py`. Verified output:

```text
alerts 8 kept 2 suppressed 6
attacks kept 1 attacks suppressed 1
SUPPRESSED ATTACK: ('new-service', 'PATCH-SRV2', 'svc_patch')
```

### 6.4 Reading the result

Of 8 sample alerts, 6 are suppressed and 2 kept. One kept alert is an attack (FIN-PC07). One suppressed alert is an attack: a new service on PATCH-SRV2 by svc_patch — the purple team's simulated misuse of the patching account. The allow-list "new-service on PATCH-SRV2 by svc_patch" hides exactly this.

Section six point four develops data collection and analysis with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section six point four, Dr. Ingrid Solberg expects data claims to carry owners and dates.

### 6.5 Handling the finding

Per the registered stopping rule, the entry is reviewed within a day. Marcus Bell narrows it: new services by svc_patch on PATCH-SRV2 are allowed only when the service name matches the patch tool's signed naming pattern and occurs in the maintenance window. A re-replay shows the injected event now alerts.

Section six point five develops data collection and analysis with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section six point five, Dr. Ingrid Solberg expects data claims to carry owners and dates.

### 6.6 Overall results

Net reduction 136.5 alerts/week (chapter 4); 93% of removed alerts benign; 1 of 8 injected events suppressed before narrowing, 0 after.

Section six point six develops data collection and analysis with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section six point six, Dr. Ingrid Solberg expects data claims to carry owners and dates.

Section six point six treats collection labelling results checking as testable only when evidence and ticket IDs are recorded.

For section six point six, Ashworth Institute of Technology will not accept data work without a written trail.

### Worked example

Tariq's results table has three rows — volume, label composition, safety — each with estimate, uncertainty and source file, plus a note: "Safety finding led to narrowing of allow-list entry AL-07 in week 6."

> **Synthetic case.** Alerts come from the lab script.

### Errors and limits

Eight injected events are few; zero suppressions after narrowing does not prove no future suppression.

### Exercises

- **EX033 — Label composition.** What share of removed alerts were benign triggers? *Rubric:* 3 = about 93%, reweighted; 2 = number only; 1 = wrong; 0 = none.
- **EX034 — Allow-list risk.** Why can allow-lists hide attacks? *Rubric:* 3 = attacker using allow-listed account/host combination is suppressed; 2 = partial; 1 = cannot; 0 = none.
- **EX035 — Replay output.** Summarise the lab output. *Rubric:* 3 = 8 alerts, 6 suppressed, 2 kept; 1 attack kept, 1 suppressed (PATCH-SRV2 svc_patch); 2 = partial; 1 = wrong; 0 = none.
- **EX036 — Narrowing.** How was entry AL-07 narrowed? *Rubric:* 3 = signed naming pattern plus maintenance window; re-replay alerts; 2 = partial; 1 = deleted rule; 0 = none.
- **EX037 — Three outcomes.** Report the three overall results. *Rubric:* 3 = −136.5/week, 93% benign, 1→0 suppressed injections; 2 = two; 1 = one; 0 = none.
- **EX038 — Zero suppressions.** Why does zero after narrowing not prove safety? *Rubric:* 3 = few injected events; future behaviours may differ; 2 = partial; 1 = proves it; 0 = none.

### Synthesis

Measure volume, composition and safety together; when ground truth exposes a hole, fix it under the protocol and report it.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a master's dissertation; (2) write results without overclaiming; (3) write a strong limitations section; (4) make recommendations proportional to evidence.

### 7.1 Structure

Abstract; introduction; literature review; method; results; discussion; limitations; recommendations; conclusion; references; appendices (protocol, scripts, allow-list change log).

Section seven point one develops dissertation writing and limitations with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section seven point one, Dr. Ingrid Solberg expects dissertation claims to carry owners and dates.

Section seven point one treats structure writing results the as testable only when evidence and ticket IDs are recorded.

For section seven point one, Ashworth Institute of Technology will not accept dissertation work without a written trail.

### 7.2 Writing results

Results report what was measured with uncertainty: "Net reduction of 136.5 alerts per week (bootstrap 95% interval 98–171)." Interpretation belongs in the discussion. Tariq avoids words such as "proves" and "eliminates".

Section seven point two develops dissertation writing and limitations with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section seven point two, Dr. Ingrid Solberg expects dissertation claims to carry owners and dates.

Section seven point two treats structure writing results the as testable only when evidence and ticket IDs are recorded.

### 7.3 The discussion

Tuning removed mostly benign triggers, consistent with Alahmadi et al. (2022). The suppressed injected event shows allow-lists move risk rather than removing it: they trade analyst time against blind spots. Narrow, conditional entries reduce the trade-off.

Section seven point three develops dissertation writing and limitations with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section seven point three, Dr. Ingrid Solberg expects dissertation claims to carry owners and dates.

Section seven point three treats structure writing results the as testable only when evidence and ticket IDs are recorded.

### 7.4 Limitations

One SOC; eight weeks; twenty rules; eight injected events; labelling by two people from the same team; parallel-trends assumption untestable after week 5; purple-team behaviours chosen by people who knew the rules. Each limitation states its likely direction of bias where possible — for example, injected events designed with knowledge of rule logic probably make suppression look rarer than it would be against unknown attackers.

Section seven point four develops dissertation writing and limitations with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

### 7.5 Recommendations

Review allow-list entries with the same rigour as rules; add conditions (time window, signed names) rather than broad host-account pairs; replay entries against purple-team events quarterly; track suppressed-attack tests as a metric beside volume.

Section seven point five develops dissertation writing and limitations with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section seven point five, Dr. Ingrid Solberg expects dissertation claims to carry owners and dates.

Section seven point five treats structure writing results the as testable only when evidence and ticket IDs are recorded.

### 7.6 Proportion

Recommendations are framed for SOCs similar to Pelham's, not "all SOCs".

Section seven point six develops dissertation writing and limitations with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section seven point six, Dr. Ingrid Solberg expects dissertation claims to carry owners and dates.

Section seven point six treats structure writing results the as testable only when evidence and ticket IDs are recorded.

For section seven point six, Ashworth Institute of Technology will not accept dissertation work without a written trail.

### 7.7 Writing process

Tariq writes the method first, results second, discussion last, and sends each chapter to Solberg as it is finished.

Section seven point seven develops dissertation writing and limitations with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section seven point seven, Dr. Ingrid Solberg expects dissertation claims to carry owners and dates.

Section seven point seven treats structure writing results the as testable only when evidence and ticket IDs are recorded.

For section seven point seven, Ashworth Institute of Technology will not accept dissertation work without a written trail.

### Worked example

Tariq's limitation paragraph on labelling: "Both labellers work in the Pelham SOC and may share assumptions about what is normal. Agreement after definition changes was high, but shared bias would not appear as disagreement. An external labeller would strengthen future work."

> **Synthetic case.** The text is invented.

### Errors and limits

Long limitation lists without direction or impact are less useful than a few analysed ones.

### Exercises

- **EX039 — Dissertation parts.** List the main dissertation sections in order. *Rubric:* 3 = abstract through appendices in order; 2 = minor slips; 1 = jumbled; 0 = none.
- **EX040 — Results wording.** Rewrite "tuning eliminated noise" in results style. *Rubric:* 3 = measured estimate with interval, no overclaim; 2 = partial; 1 = unchanged; 0 = none.
- **EX041 — Risk trade.** What trade-off does the discussion identify? *Rubric:* 3 = analyst time vs blind spots; narrow entries reduce it; 2 = partial; 1 = none; 0 = none.
- **EX042 — Bias direction.** Which way does purple-team design bias the suppression estimate? *Rubric:* 3 = makes suppression look rarer; designers knew rules; 2 = direction only; 1 = wrong; 0 = none.
- **EX043 — Recommendations.** Give three recommendations. *Rubric:* 3 = review entries rigorously, conditional entries, quarterly replay, suppression metric (three); 2 = two; 1 = one; 0 = none.
- **EX044 — Shared bias.** Why would shared labeller bias not show up as disagreement? *Rubric:* 3 = both share the same assumptions so they agree wrongly; 2 = partial; 1 = it would; 0 = none.

### Synthesis

Report measured results plainly, interpret in discussion, analyse limitations with their direction and keep recommendations proportional.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) arrange independent review before submission; (2) prepare an oral defense; (3) respond to examiners' questions; (4) hand results back to the host organisation responsibly.

### 8.1 Independent review

Before submission, a SOC analyst from another organisation reviews the method and recommendations, and a fellow student reruns the analysis scripts from the archive. The analyst's main comment: "Your allow-list review process assumes a mature change process; smaller SOCs may not have one." Tariq adds a paragraph scaling the recommendations.

Section eight point one develops independent review and defense with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section eight point one, Dr. Ingrid Solberg expects independent claims to carry owners and dates.

### 8.2 The defense format

A 20-minute presentation and 40 minutes of questions from two examiners.

Section eight point two develops independent review and defense with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section eight point two, Dr. Ingrid Solberg expects independent claims to carry owners and dates.

Section eight point two treats independent review the defense as testable only when evidence and ticket IDs are recorded.

For section eight point two, Ashworth Institute of Technology will not accept independent work without a written trail.

### 8.3 Likely questions

"Why not randomise?" "How do you know the holiday affected both groups equally?" "Is one suppressed event in eight a lot or a little?" "Would you deploy these allow-lists at another utility?"

Section eight point three develops independent review and defense with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section eight point three, Dr. Ingrid Solberg expects independent claims to carry owners and dates.

Section eight point three treats independent review the defense as testable only when evidence and ticket IDs are recorded.

### 8.4 Answering well

Tariq answers directly, gives the evidence, then the limit. On "one in eight": "In this exercise it was 12.5% of injected behaviours, but the events were few and chosen; the important finding is that a broad entry could hide a realistic misuse, and narrowing it fixed that case."

Section eight point four develops independent review and defense with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section eight point four, Dr. Ingrid Solberg expects independent claims to carry owners and dates.

### 8.5 Returning results

Pelham receives a summary report, the narrowed allow-list policy and the replay script. Tariq briefs analysts before managers, so the people who did the work hear results first.

Section eight point five develops independent review and defense with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section eight point five, Dr. Ingrid Solberg expects independent claims to carry owners and dates.

Section eight point five treats independent review the defense as testable only when evidence and ticket IDs are recorded.

### 8.6 Sharing safely

The public dissertation omits host names, account names and rule logic details that would help an attacker evade Pelham's detections; these remain in a restricted appendix for the examiners.

Section eight point six develops independent review and defense with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section eight point six, Dr. Ingrid Solberg expects independent claims to carry owners and dates.

Section eight point six treats independent review the defense as testable only when evidence and ticket IDs are recorded.

### 8.7 Afterwards

Examiner corrections are tracked and completed; the archive is tagged with the final version.

Section eight point seven develops independent review and defense with a Ashworth Institute of Technology note Tariq Haddad can demo offline.

Under section eight point seven, Dr. Ingrid Solberg expects independent claims to carry owners and dates.

Section eight point seven treats independent review the defense as testable only when evidence and ticket IDs are recorded.

For section eight point seven, Ashworth Institute of Technology will not accept independent work without a written trail.

### Worked example

Asked "Would you deploy these allow-lists elsewhere?", Tariq replies: "Not as they are — they encode Pelham's hosts and accounts. I would deploy the process: conditional entries, peer review and quarterly replay against authorised simulations."

> **Synthetic case.** The review and defense are invented.

### Errors and limits

Restricting details protects the host but limits reproducibility; the archive explains what was withheld and why.

### Exercises

- **EX045 — External comment.** What did the external analyst point out, and what changed? *Rubric:* 3 = assumes mature change process; scaling paragraph added; 2 = partial; 1 = nothing; 0 = none.
- **EX046 — Defense questions.** List three likely examiner questions. *Rubric:* 3 = randomise, holiday equality, one in eight, deploy elsewhere (three); 2 = two; 1 = one; 0 = none.
- **EX047 — One in eight.** How did Tariq frame the one-in-eight result? *Rubric:* 3 = 12.5% of few chosen events; key point broad entry hid realistic misuse; fixed by narrowing; 2 = partial; 1 = percentage only; 0 = none.
- **EX048 — Returning results.** What did Pelham receive, and who heard first? *Rubric:* 3 = report, policy, replay script; analysts before managers; 2 = partial; 1 = nothing; 0 = none.
- **EX049 — Restricted appendix.** What was withheld from the public version, and why? *Rubric:* 3 = host/account names, rule details; would aid evasion; 2 = partial; 1 = nothing; 0 = none.
- **EX050 — Deploy elsewhere.** Why not reuse the allow-lists at another utility? *Rubric:* 3 = encode Pelham-specific hosts/accounts; transfer the process instead; 2 = partial; 1 = would reuse; 0 = none.

### Synthesis

Independent review, direct answers with limits, and responsible return and sharing complete a master's project.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Tariq Haddad, Dr. Ingrid Solberg, Marcus Bell, Ashworth Institute of Technology, Pelham Water Utility and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** It names no intervention, comparison, measurable outcome or time frame.

**EX002.** Intervention (allow-lists), population (ten rules in one SOC), comparison (untuned rules), outcomes (volume and suppressed attacks) and time frame (the same weeks).

**EX003.** The date, database, exact terms, number of hits and how many were screened and included.

**EX004.** Alahmadi et al. is a peer-reviewed empirical study; a vendor blog is unreviewed and may serve marketing aims.

**EX005.** They describe practice and formats; they do not show whether tuning works.

**EX006.** Hardly any studies measure the effect of tuning against a comparison group.

**EX007.** They study algorithms without analyst or operational data, so they cannot answer a question about SOC alert handling.

**EX008.** A rule is worth keeping loud in proportion to the importance of the assets it protects.

**EX009.** A common vocabulary of adversary techniques so detection coverage can be mapped and compared.

**EX010.** A structured map of defensive techniques, showing which countermeasure a detection represents.

**EX011.** As a continuing, risk-driven programme with set frequencies and metrics rather than a tool purchase.

**EX012.** Counting closed alerts encourages fast closure over careful investigation.

**EX013.** Alahmadi et al. found high volume itself causes burnout, so reducing it has real value.

**EX014.** Tuning becomes a maturing, repeatable process inside the SOC rather than a single clean-up.

**EX015.** The SOC insisted on tuning its noisiest rules first, so randomisation was impractical; an untuned comparison group still removes changes affecting all rules.

**EX016.** An authorised purple-team event, logged with its time, that matched a rule but was removed by an allow-list entry.

**EX017.** The CISO signed it, it used benign simulated behaviour and it excluded operational technology networks.

**EX018.** Inside the SOC before data leaves, so real names never reach the research copy.

**EX019.** Seasonal variation, log-source outages and colleagues tuning other rules (and analysts knowing about the study).

**EX020.** On weekly alert volume and the ATT&CK tactic they cover.

**EX021.** The public holiday, the SIEM upgrade and the firewall log migration.

**EX022.** It takes the change in the tuned group and subtracts the change in the untuned group, cancelling influences both share.

**EX023.** Tuned −173.8, control −37.2, net −136.5 alerts per week.

**EX024.** None of the tuned rules read firewall logs, so the migration could not change their counts.

**EX025.** That both groups would have followed parallel paths without tuning; their similar, flat weeks 1–4 support this.

**EX026.** Any event that touched only the tuned rules, such as a change in the hosts they monitor.

**EX027.** Background and gap, question and hypotheses, design, data and ethics, analysis, and validity threats (timeline and risks too).

**EX028.** A drop in volume says nothing about whether the removed alerts were harmless, and labelling every alert is not feasible.

**EX029.** High 20, medium 45, low 135; proportional allocation would give high-severity alerts only 6, too few for an estimate.

**EX030.** The sample over-represents the high stratum, so each stratum's results are weighted by its population size to avoid bias.

**EX031.** A benign trigger is the intended behaviour happening legitimately; a false positive is the rule catching behaviour it was never meant to match.

**EX032.** Dr. Solberg and Marcus Bell signed the proposal; the CISO signed the purple-team annex.

**EX033.** Roughly 93%, after reweighting the stratified sample.

**EX034.** Anyone abusing an allow-listed account on an allow-listed host produces activity the entry silently removes.

**EX035.** Eight alerts: six suppressed and two kept; one attack (FIN-PC07) kept, and one attack (new service on PATCH-SRV2 by svc_patch) suppressed.

**EX036.** It now applies only when the service name fits the patch tool's signed pattern and the event falls in the maintenance window; the re-replay then alerted.

**EX037.** A net cut of 136.5 alerts per week, about 93% of removed alerts benign, and suppressed injections falling from one to zero after narrowing.

**EX038.** Only eight events were injected, and attackers may behave in ways none of them covered.

**EX039.** Abstract, introduction, literature review, method, results, discussion, limitations, recommendations, conclusion, references, appendices.

**EX040.** "Weekly alerts from tuned rules fell by a net 136.5 (95% interval 98–171) compared with untuned rules."

**EX041.** Allow-lists save analyst time but create blind spots; conditional entries shrink that cost.

**EX042.** Downward: people who knew the rules designed the injections, so suppression probably appears less common than real attackers would cause.

**EX043.** Review allow-list entries like rules, add conditions such as time windows and signed names, and replay entries quarterly against purple-team events (also track suppression tests as a metric).

**EX044.** If both labellers hold the same mistaken view, they agree with each other, so the error never surfaces as a disagreement.

**EX045.** That the review process presumes a mature change process that small SOCs may lack; Tariq added a paragraph adapting the recommendations by SOC size.

**EX046.** Why not randomise? Did the holiday affect both groups equally? Is one suppressed event in eight a lot?

**EX047.** He said it was 12.5% of a few deliberately chosen events, and that the real lesson was that a broad entry hid a realistic misuse until it was narrowed.

**EX048.** A summary report, the narrowed allow-list policy and the replay script; analysts were briefed before managers.

**EX049.** Host names, account names and detailed rule logic, which could help someone evade Pelham's detections.

**EX050.** They are built around Pelham's own hosts and accounts; what transfers is the method of conditional, reviewed, replay-tested entries.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and telemetry in this book are synthetic unless a sentence cites a public source.


- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
