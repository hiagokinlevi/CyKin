# Security Operations and Blue Team: Doctoral Research Track

- Language: English (`en`); course 199, Doctoral research track (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: doctoral candidates who will produce original, reproducible research on security operations, alert quality and analyst decision-making.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one doctoral project on context-enriched alert triage from research integrity to defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Nadia Ferreira** | Doctoral candidate | Invented |
| **Prof. Elias Grant** | Supervisor | Invented |
| **Calder University** | Fictional university | Invented |
| **Northgate Shared SOC** | Fictional partner SOC | Invented |
| **Ruth Okonkwo** | SOC manager | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes

You will (1) apply research-integrity principles to security-operations research; (2) separate detection quality, triage quality and operational outcome as distinct constructs; (3) design studies that use synthetic or consented operational data; (4) pre-register hypotheses, measures and analysis.

### 1.1 Why integrity matters in SOC research

SOC research shapes how organisations spend scarce analyst time. A study that overstates a triage aid can lead a SOC to switch off useful alerts or trust a tool it should check. Vielberth et al. (2020), in a systematic study of SOC literature, found the field fragmented and short of empirical evaluation; Kokulu et al. (2019) showed through interviews that managers and analysts often disagree about what the SOC's problems even are. A doctoral project should add careful evidence, not more opinion.

### 1.2 Three constructs, kept apart

**Detection quality** asks whether a rule fires on the activity it targets and stays quiet otherwise (precision, recall). **Triage quality** asks whether an analyst, given an alert, reaches the right disposition (accuracy, time, agreement). **Operational outcome** asks whether incidents are contained sooner or with less harm. A study can improve one while harming another; claims must name which construct was measured. Nadia's thesis measures triage quality only. Her synthetic alerts have known labels, so accuracy can be scored exactly, but nothing in the design shows whether Northgate would contain incidents faster. Her conclusion chapter keeps that boundary.

### 1.3 Data for research

Real SOC data contains personal data, business secrets and evidence of live incidents. It is rarely shareable and may not be consented for research. Synthetic alert sets with known ground truth allow exact scoring and open publication. Where operational data is needed, it is used under a data-sharing agreement, minimised and pseudonymised, with ethics approval. Nadia's corpus is synthetic for these reasons: Northgate serves several municipalities, and its real alerts would include residents' and staff data. The only operational data in her study are the analysts' own triage logs, collected with consent and anonymised before analysis, under ethics approval from Calder University.

### 1.4 Pre-registration

Before the main study the candidate registers hypotheses, primary and secondary measures, sample size reasoning, analysis plan and exclusion rules. Later changes are allowed but logged with reasons, so readers can tell planned from exploratory results. Nadia registers accuracy as the primary measure and time-to-disposition as secondary, with the paired analysis and the exclusion rule for incomplete sessions. Her change log, starting with version 1.1 after the pilot, records each later change, so readers can see that moving context fields to the top of the card happened before the main study, not after the results were known.

### 1.5 Interests and tools

Vendors may fund SOC studies or supply tools. Funding, relationships and tool versions are declared. A study that tests a product must not let the vendor approve conclusions. Nadia's study uses no vendor product; the alert cards are her own design, and the rules are written in the open Sigma format. She still records the Python version used to generate alerts and score decisions, and Calder's declaration form states that Northgate receives no payment or product benefit from the study. Her thesis lists these declarations in the front matter, so examiners see them before the results.

### 1.6 Ethics with analysts as participants

When analysts are participants, their performance data could affect careers. Consent is voluntary, managers do not see individual scores, and participants may withdraw. At Northgate, Ruth Okonkwo approved participation in work time but agreed in writing not to see individual accuracy scores. Analysts receive random IDs before the sessions, and results are reported only in aggregate. An analyst who withdraws can have their logs removed up to the point of analysis, and the consent form states that date. Nadia also promised to present results to the analysts first.

### Worked example

**Nadia Ferreira**, a doctoral candidate at the fictional **Calder University** supervised by **Prof. Elias Grant**, drafts the aim "context-enriched alerts make analysts better". Grant asks: better at what, measured how, against what truth, with what uncertainty? Nadia rewrites: "Estimate the difference in triage accuracy and median time-to-disposition between baseline and context-enriched alert cards on 160 synthetic alerts with known labels, reporting 95% intervals."

> **Synthetic case.** Calder University, Nadia, Prof. Grant and all data are invented.

### Errors and limits

Synthetic alerts simplify real operations. Results transfer only as far as the alert set resembles a real SOC's mix; the thesis must say which features were not modelled.

### Exercises

- **EX001 — Three constructs.** Distinguish detection quality, triage quality and operational outcome. *Rubric:* 3 = all three with a measure each; 2 = two; 1 = one; 0 = none.
- **EX002 — The field's gap.** What did Vielberth et al. (2020) report about SOC research? *Rubric:* 3 = fragmented, short of empirical evaluation; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Perspectives differ.** What did Kokulu et al. (2019) find about managers and analysts? *Rubric:* 3 = they often disagree on the SOC's problems; 2 = partial; 1 = vague; 0 = none.
- **EX004 — Rewrite the aim.** Turn "enriched alerts make analysts better" into a testable aim. *Rubric:* 3 = measures, conditions, ground truth, uncertainty; 2 = three; 1 = vague; 0 = none.
- **EX005 — Pre-registration content.** Name five things registered before the main study. *Rubric:* 3 = hypotheses, measures, sample-size reasoning, analysis, exclusions; 2 = three; 1 = one; 0 = none.
- **EX006 — Participant protection.** How are analyst participants protected? *Rubric:* 3 = voluntary consent, no individual scores to managers, withdrawal; 2 = two; 1 = one; 0 = none.
- **EX007 — Synthetic boundary.** State the main limit of synthetic alert sets. *Rubric:* 3 = transfer only as far as the mix resembles reality; say what is missing; 2 = partial; 1 = vague; 0 = none.

### Synthesis

SOC research must name the construct measured, use shareable or properly governed data, pre-register and protect participants.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Security operations and blue team: research frontier

### Learning outcomes

You will (1) map open problems in security operations research; (2) explain the base-rate problem for alerting; (3) relate alert fatigue research to triage design; (4) position a thesis on the frontier.

### 2.1 The base-rate problem

Axelsson (2000) showed that because genuine intrusions are rare among the events a detector sees, even a small false-positive rate produces mostly false alarms. Precision depends on prevalence as well as on the detector. For Nadia's study, the base-rate argument is the motivation: if rules fire mostly on benign activity, the analyst's decision at triage decides whether a SOC is useful. Her experiment therefore measures what happens at that second stage, where the alerts that detection could not filter must be sorted by people.

### Lab — precision under different base rates

```python
"""Base-rate effect on alert precision (Axelsson 2000), synthetic figures."""
def ppv(tpr, fpr, prevalence):
    tp = tpr * prevalence
    fp = fpr * (1 - prevalence)
    return tp / (tp + fp)
for prev in (1e-2, 1e-3, 1e-4):
    for fpr in (1e-2, 1e-3):
        print(f"prevalence={prev:.0e} TPR=0.95 FPR={fpr:.0e} -> precision={ppv(0.95, fpr, prev):.3f}")
```

Run with `python3 lab_baserate.py`. Verified output:

```text
prevalence=1e-02 TPR=0.95 FPR=1e-02 -> precision=0.490
prevalence=1e-02 TPR=0.95 FPR=1e-03 -> precision=0.906
prevalence=1e-03 TPR=0.95 FPR=1e-02 -> precision=0.087
prevalence=1e-03 TPR=0.95 FPR=1e-03 -> precision=0.487
prevalence=1e-04 TPR=0.95 FPR=1e-02 -> precision=0.009
prevalence=1e-04 TPR=0.95 FPR=1e-03 -> precision=0.087
```

### 2.2 Reading the result

With 95% true-positive rate and 1% false-positive rate, precision is 0.490 at a prevalence of one in a hundred, 0.087 at one in a thousand and 0.009 at one in ten thousand. Cutting the false-positive rate to 0.1% lifts the one-in-a-thousand case only to 0.487. Rare-event detection needs very low false-positive rates or a second stage, such as analyst triage, to be useful. Nadia uses the lab to set expectations for her corpus. Because real alert streams are dominated by benign triggers, her corpus includes many of them deliberately, so that triage decisions are tested on the alerts analysts most often see.

### 2.3 Alert fatigue

Alahmadi, Axon and Martinovic (2022) interviewed SOC practitioners and found that many alarms called "false positives" are benign triggers: the rule matched real behaviour that was legitimate in context. They propose that alarms be Reliable, Explainable, Analytical, Contextual and Transferable. Hassan et al. (2019) used provenance graphs to rank alerts and reduce fatigue. The benign-trigger finding is the starting point of Nadia's project: if many alarms are correct matches on legitimate activity, analysts need context to recognise legitimacy quickly. Her enriched cards test the Contextual property directly. Ranking methods like Hassan et al.'s reduce how many alerts reach analysts, which is complementary to her question rather than a competitor.

### 2.4 Machine learning caution

Sommer and Paxson (2010) argued that anomaly detection suits closed worlds poorly: attacks are rare, benign variety is huge, and errors are costly to explain. Their critique still frames how frontier work must be evaluated. Nadia's study avoids anomaly detection altogether; her rules are explicit Sigma conditions. The critique still shapes her design, because it warns that a method evaluated on convenient data can fail in operation. That is why she reports realism as a limitation and plans an operational pilot as the test that could falsify her claim.

### 2.5 Human and organisational factors

Sundaramurthy et al. (2014) embedded researchers in SOCs and found tacit knowledge and tooling friction central. Kokulu et al. (2019) stressed mismatches between management metrics and analyst reality. These studies remind Nadia that triage happens inside an organisation, with habits and tools that a laboratory session removes. Her pilot found exactly such friction: analysts did not see a field placed at the bottom of the card. A senior analyst's later comment that the raw command line was missing came from the same kind of tacit knowledge.

### 2.6 Nadia's position

Nadia's thesis sits between detection and triage: it tests whether adding context to alerts, as the "Contextual" property suggests, improves analysts' decisions on benign triggers without hiding true attacks. The position makes her claim specific. She does not test whether context improves detection, nor whether it shortens incidents; she tests whether analysts who see context reach the right disposition more often. Her worry from the start was the second half of the sentence: that context might also lead analysts to dismiss a true attack, which is why harms are measured alongside accuracy.

### Worked example

Nadia's literature map has three columns — detector-level, alert-level and analyst-level work — and places her study in the alert-level column, citing Alahmadi et al. for motivation and Axelsson for why triage, not detection alone, decides usefulness.

> **Synthetic case.** Figures come from the lab script.

### Errors and limits

Frontier claims age quickly; Nadia dates her review and records search terms so it can be updated.

### Exercises

- **EX008 — Base-rate statement.** State Axelsson's base-rate point in one sentence. *Rubric:* 3 = rare intrusions make even low FPR yield mostly false alarms; 2 = partial; 1 = vague; 0 = none.
- **EX009 — Lab reading.** Give precision at prevalence 1e-3 for FPR 1e-2 and 1e-3. *Rubric:* 3 = 0.087 and 0.487; 2 = one; 1 = wrong; 0 = none.
- **EX010 — Benign triggers.** How do benign triggers differ from false positives? *Rubric:* 3 = rule matched real but legitimate behaviour; 2 = partial; 1 = same; 0 = none.
- **EX011 — REACT properties.** List the five alarm properties proposed by Alahmadi et al. *Rubric:* 3 = Reliable, Explainable, Analytical, Contextual, Transferable; 2 = three; 1 = one; 0 = none.
- **EX012 — Closed-world critique.** Summarise Sommer and Paxson's caution. *Rubric:* 3 = rare attacks, huge benign variety, costly unexplained errors; 2 = two; 1 = one; 0 = none.
- **EX013 — Thesis position.** Where does Nadia's thesis sit, and why? *Rubric:* 3 = alert/triage level; tests Contextual property on benign triggers without hiding attacks; 2 = partial; 1 = detector; 0 = none.
- **EX014 — Updating reviews.** How does Nadia keep her review updatable? *Rubric:* 3 = dates it and records search terms; 2 = one; 1 = vague; 0 = none.

### Synthesis

The frontier is shaped by base rates, alarm quality and human factors; a thesis must place itself precisely among them.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes

You will (1) state an original contribution precisely; (2) separate the contribution from its supporting work; (3) evaluate detection conditions against labelled synthetic events; (4) defend the proposal's novelty and feasibility.

### 3.1 What counts as original

An original contribution adds knowledge others can use and test: a validated method, a measured effect, a reusable dataset. Nadia proposes three items: a labelled synthetic alert corpus with benign triggers; a controlled experiment on context enrichment; and an analysis of where enrichment fails. Each item can be checked separately by others. The corpus can be reused for different experiments; the measured effect can be challenged by repeating the study; and the failure analysis gives designers concrete cases. Nadia's contribution statement names the three items so examiners can judge each one against its evidence.

### 3.2 Supporting work

Detection rules must be good enough that triage, not detection, is the bottleneck in the experiment. Nadia evaluates candidate rules on labelled synthetic events before building alert cards. Rules are written in the Sigma format from SigmaHQ so others can read them in a vendor-neutral way. The rule evaluation is supporting work, not a contribution in itself. Its purpose is to make sure that the alerts in the experiment come from plausible rules, including one that fires on benign activity, so that triage decisions are tested on realistic material.

### Lab — replaying detection conditions

```python
"""Replay a Sigma-style detection condition over synthetic labelled events."""
events = [  # (process, parent, cmdline_has_encoded, label)
    ("powershell.exe", "winword.exe", True, "attack"),
    ("powershell.exe", "explorer.exe", False, "benign"),
    ("powershell.exe", "sccm_agent.exe", True, "benign"),
    ("powershell.exe", "excel.exe", True, "attack"),
    ("cmd.exe", "winword.exe", False, "attack"),
    ("powershell.exe", "explorer.exe", True, "benign"),
    ("powershell.exe", "outlook.exe", True, "attack"),
    ("powershell.exe", "sccm_agent.exe", True, "benign"),
]
office = {"winword.exe", "excel.exe", "outlook.exe"}
def v1(p, par, enc): return p == "powershell.exe" and enc
def v2(p, par, enc): return p in {"powershell.exe", "cmd.exe"} and par in office
for name, rule in (("v1 encoded-only", v1), ("v2 office-parent", v2)):
    tp = sum(rule(p, q, e) and l == "attack" for p, q, e, l in events)
    fp = sum(rule(p, q, e) and l == "benign" for p, q, e, l in events)
    fn = sum((not rule(p, q, e)) and l == "attack" for p, q, e, l in events)
    print(f"{name:17} TP={tp} FP={fp} FN={fn} precision={tp/(tp+fp):.2f} recall={tp/(tp+fn):.2f}")
```

Run with `python3 lab_replay.py`. Verified output:

```text
v1 encoded-only   TP=3 FP=3 FN=1 precision=0.50 recall=0.75
v2 office-parent  TP=4 FP=0 FN=0 precision=1.00 recall=1.00
```

### 3.3 Reading the result

Condition v1 (encoded PowerShell command line) catches 3 of 4 attacks but also fires on 3 benign events — the software-deployment agent and an administrator — giving precision 0.50. Condition v2 (script host whose parent is an Office application) catches all 4 attacks with no false alarms in this small set. The benign triggers of v1 are exactly the kind of alerts context should help analysts dismiss, so Nadia keeps v1's alerts in the corpus as triage material. Both results come from a small labelled set, so Nadia does not claim v2 is a better rule in general; she only checks that each rule behaves as intended on known events. The administrator and deployment-agent alerts give her benign triggers whose context, such as user role or a history of benign closures, is exactly what enriched cards display.

### 3.4 Novelty

Her review shows prior work measured analysts' perceptions (Alahmadi et al., 2022) and automated ranking (Hassan et al., 2019), but few controlled experiments on context in alert cards with known ground truth. The gap is narrow but real: practitioners report that context helps, and ranking systems reduce volume, yet few studies measure whether showing context changes analysts' decisions on alerts with known truth. Nadia's literature map supports this claim, and she keeps the search record so examiners can check it. The search covered security and human-factors venues, because studies of analyst decisions are often published outside security conferences.

### 3.5 Feasibility

Eight analysts from the fictional **Northgate Shared SOC**, which serves several municipalities, agree to participate in work time with manager **Ruth Okonkwo**'s approval; the corpus is synthetic; the study fits in two semesters. Running sessions in work time with the manager's approval avoids asking analysts to give up their own time, but it also means that urgent incidents could interrupt a session. The protocol allows a session to be paused and resumed, with the pause recorded. Two semesters allow for the pilot, the main study and the analysis with some slack.

### 3.6 Risks

Recruitment may fall short; analysts may recognise synthetic patterns. Mitigations: a reserve pool from a second SOC; realism review by two senior analysts. Recognising synthetic patterns could inflate accuracy in both conditions, which would narrow any difference. The realism review checks the corpus before the main study; the second SOC's reserve pool is contacted only if Northgate's volunteers fall below eight. Both mitigations are recorded in the proposal with who is responsible. Nadia reviews the risk list with Prof. Grant each month until the main study ends.

### Worked example

Nadia's contribution statement: "C1: an openly licensed synthetic alert corpus of 320 alerts with labels and benign-trigger annotations. C2: a crossover experiment estimating the effect of context enrichment on triage accuracy and time. C3: a failure analysis of alerts where enrichment misled analysts."

> **Synthetic case.** Events and rules are from the lab script; Northgate is invented.

### Errors and limits

Eight events cannot validate a rule; the lab shows method, not rule quality.

### Exercises

- **EX015 — Contribution list.** State Nadia's three contributions. *Rubric:* 3 = corpus, crossover experiment, failure analysis; 2 = two; 1 = one; 0 = none.
- **EX016 — Why test rules first.** Why must detection be evaluated before the triage experiment? *Rubric:* 3 = triage must be the bottleneck being studied; 2 = partial; 1 = no reason; 0 = none.
- **EX017 — Replay result.** Give precision and recall for v1 and v2. *Rubric:* 3 = v1 0.50/0.75, v2 1.00/1.00; 2 = one rule; 1 = wrong; 0 = none.
- **EX018 — Keeping v1 alerts.** Why keep v1's benign triggers in the corpus? *Rubric:* 3 = they are realistic triage material context should help dismiss; 2 = partial; 1 = mistake; 0 = none.
- **EX019 — Novelty gap.** What gap establishes novelty? *Rubric:* 3 = few controlled experiments on alert context with ground truth; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Small sample.** What does the eight-event replay not show? *Rubric:* 3 = rule validity; it only illustrates the method; 2 = partial; 1 = proves rule; 0 = none.

### Synthesis

State contributions precisely, make supporting work fit for purpose, and show novelty and feasibility with evidence.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes

You will (1) replicate a baseline before testing an intervention; (2) measure inter-rater reliability of ground-truth labels; (3) run a pilot to test procedures; (4) revise the protocol from pilot evidence.

### 4.1 Why replicate a baseline

Before claiming enrichment helps, Nadia must show her setup reproduces known behaviour: analysts in the baseline condition should show accuracy and benign-trigger confusion similar to what practitioners report. If the baseline is odd, the comparison is meaningless. Nadia's check is that baseline analysts confuse benign triggers with attacks at a rate similar to what practitioners describe. If baseline accuracy were near perfect, enrichment would have nothing to improve and the corpus would be too easy. Her pilot and baseline results are compared with the benign-trigger reports in the literature before the main analysis.

### 4.2 Ground-truth labels

The corpus labels are written by Nadia when she generates alerts, but "malicious" versus "benign" can be debatable for borderline cases. Two senior analysts independently label 20 sample alerts to test whether labels are clear. If the two senior analysts disagree often, the ground truth itself is unclear and accuracy cannot be scored fairly. The 20 alerts are drawn to include borderline cases, not only obvious ones, so the test is demanding. The senior analysts do not take part in the main study.

### Lab — agreement on labels

```python
"""Cohen's kappa for two analysts labelling the same 20 synthetic alerts."""
from collections import Counter
a = "MMBBBMBBBBMBBBBBMBBB"   # M = malicious, B = benign (analyst A)
b = "MMBBBBBBBBMBBBMBMBBB"   # analyst B
n = len(a)
po = sum(x == y for x, y in zip(a, b)) / n
ca, cb = Counter(a), Counter(b)
pe = sum(ca[k] * cb[k] for k in "MB") / n**2
kappa = (po - pe) / (1 - pe)
print(f"n={n} observed agreement={po:.2f} chance={pe:.3f} kappa={kappa:.2f}")
```

Run with `python3 lab_kappa.py`. Verified output:

```text
n=20 observed agreement=0.90 chance=0.625 kappa=0.73
```

### 4.3 Reading the result

The two analysts agree on 18 of 20 alerts (0.90). Chance agreement, given how often each says "malicious", is 0.625, so Cohen's kappa is 0.73 — "substantial" on the Landis and Koch (1977) scale. The two disagreements are discussed; one label is corrected and one alert is rewritten to remove ambiguity. Kappa is lower than the raw agreement because both analysts called many alerts malicious, which makes chance agreement high. The corrected label and the rewritten alert are recorded in the change log, including alert 17. With these fixes, Nadia treats the corpus labels as reliable enough to score the main study.

### 4.4 The pilot

Two volunteer analysts not in the main study triage 40 alerts, 20 in each condition. The pilot checks timing, instructions, the alert-card layout and logging. The pilot analysts use the same cards and instructions as the main study, so any problem they meet would also affect the main sessions. They are asked afterwards what confused them, and Nadia watches one session to see where they hesitate. Their logs are kept separately and are not part of any reported effect. Pilot analysts also time each session, which is how the 70-minute run for 40 alerts was found.

### 4.5 What the pilot found

Analysts did not notice the asset criticality field because it sat at the bottom of the card; logging missed disposition changes; 40 alerts took 70 minutes, causing fatigue. Nadia moves context fields near the top, fixes logging, and splits the 40 alerts into two sessions of 20. Each change is listed in the v1.1 change log before the main study begins. The fatigue finding matters for validity: tired analysts make more errors late in a session, which could bias whichever condition comes second. The pilot also confirmed that the logging worked: every disposition and change was recorded with a timestamp, so no fix was needed there.

### 4.6 Pilot data

Pilot results are not used to estimate effects; they test procedure. This is stated in the registration. Using pilot data for estimates would mix procedure testing with outcome measurement, and the pilot cards differed from the final ones after the layout change. Keeping them apart means the main results come only from the registered design. Nadia still reports what the pilot found about procedure, because it explains why the final cards look as they do. The registered plan states that pilot logs are excluded from every reported estimate, so examiners can check this against the archive.

### Worked example

Nadia's protocol change log: "v1.1 — context fields moved above the raw event; disposition-change logging added; sessions split into 2 × 20 alerts with a 15-minute break; alert 17 rewritten after label disagreement."

> **Synthetic case.** Labels come from the lab script.

### Errors and limits

Kappa depends on prevalence; with very unbalanced labels, high agreement can still give low kappa.

### Exercises

- **EX021 — Baseline purpose.** Why replicate baseline behaviour first? *Rubric:* 3 = an odd baseline makes the comparison meaningless; 2 = partial; 1 = habit; 0 = none.
- **EX022 — Kappa result.** Report observed agreement, chance agreement and kappa. *Rubric:* 3 = 0.90, 0.625, 0.73; 2 = two; 1 = one; 0 = none.
- **EX023 — Interpreting kappa.** How is 0.73 described on the Landis and Koch scale? *Rubric:* 3 = substantial (0.61–0.80); 2 = substantial only; 1 = wrong; 0 = none.
- **EX024 — Disagreements.** What happened to the two disagreements? *Rubric:* 3 = discussed; one label corrected, one alert rewritten; 2 = partial; 1 = ignored; 0 = none.
- **EX025 — Pilot findings.** Name three pilot findings and their fixes. *Rubric:* 3 = field placement, logging, fatigue with fixes; 2 = two; 1 = one; 0 = none.
- **EX026 — Kappa caveat.** What caveat applies to kappa? *Rubric:* 3 = prevalence effect; unbalanced labels lower kappa despite agreement; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Replicate the baseline, check label reliability, pilot procedures and revise transparently before the main study.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes

You will (1) run a controlled crossover study; (2) estimate effects with intervals; (3) arrange independent validation of analysis; (4) report effects honestly, including harms.

### 5.1 Design

Eight analysts each triage 40 alerts: 20 baseline cards and 20 enriched cards, in counterbalanced order, with alert sets swapped between halves. Each of the 320 corpus alerts is triaged by exactly one analyst, so the study has 320 decisions, 160 per condition. Enriched cards add asset criticality, user role, and the count of similar alerts closed as benign in the last 30 days. Counterbalancing means half the analysts see baseline cards first and half see enriched cards first, so learning and fatigue affect both conditions equally. Swapping alert sets between halves ensures that differences come from the cards, not from easier alerts in one condition. The three enriched fields were chosen from the Contextual property and from what Northgate's analysts said they look up most often.

### 5.2 Primary measure

Accuracy: the share of dispositions matching ground truth. Pooled across analysts, each condition has 160 alert decisions (8 analysts × 20), and all of them enter the registered interval. Accuracy is scored against the corpus labels confirmed by the senior analysts. Decisions are logged automatically, including any change of disposition before submission, so the final decision is the one scored. Time-to-disposition is recorded in the same log but treated as secondary, as registered. An alert is scored correct only when the disposition matches the label exactly; escalating a benign alert counts as an error, just as closing an attack does, because both cost a SOC time or safety.

### Lab — intervals for accuracy

```python
"""Wilson 95% intervals for triage accuracy in two synthetic conditions."""
import math
def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d
    h = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
for name, k, n in (("baseline", 118, 160), ("enriched", 139, 160)):
    lo, hi = wilson(k, n)
    print(f"{name:9} {k}/{n} = {k/n:.3f}  95% CI [{lo:.3f}, {hi:.3f}]")
```

Run with `python3 lab_wilson.py`. Verified output:

```text
baseline  118/160 = 0.738  95% CI [0.664, 0.800]
enriched  139/160 = 0.869  95% CI [0.808, 0.913]
```

### 5.3 Reading the result

Baseline accuracy is 118/160 = 0.738 (95% CI 0.664–0.800); enriched is 139/160 = 0.869 (0.808–0.913). The intervals barely overlap, and the difference of 13 points is consistent with the hypothesis. Because the same analysts did both conditions, the registered paired analysis is the main test; the Wilson intervals describe each condition. They treat the 160 pooled decisions as independent, although each analyst contributes 20 of them, so they are likely somewhat too narrow if analysts differ in skill; this is why they are descriptive only. Nadia reports the interval for each condition and leaves the main inference to the registered paired test. The two intervals together show readers the scale of the change. Neither interval is used to claim significance on its own, since overlapping or separate intervals are not a formal test.

### 5.4 Harms

Of the 21 additional correct decisions, most were benign triggers correctly closed. But two true attacks were wrongly closed in the enriched condition, both carrying the note "similar alerts closed as benign: 14". History context can lull analysts. This is reported prominently. Nadia reports the two missed attacks in the abstract, not only in the results, because a reader deploying enriched cards needs to know about them. She examines both alerts in detail as part of her failure analysis, and the history field becomes the focus of the follow-up and the critique that followed.

### 5.5 Independent validation

A statistician at another university reruns the analysis from Nadia's raw logs and scripts without seeing her results. Her figures match to three decimals. The statistician received the registered plan and the anonymised logs, not Nadia's tables, so agreement shows that the analysis follows from the plan and the data. Matching to three decimals also checks that the scripts are complete. The validation report is in the archive with her name and university. Prof. Grant arranged the statistician through Calder University, someone with no part in the study or in Nadia's supervision.

### 5.6 Time

Median time-to-disposition fell from 96 to 81 seconds; the time difference is secondary and labelled as such. Because time was registered as secondary, Nadia does not test it as a main hypothesis or build claims on it. She notes that faster decisions on enriched cards are consistent with analysts using context to settle benign triggers quickly, but the same speed could contribute to the two missed attacks. The time data are released with the logs for others to analyse. The time comparison is also reported per analyst, so readers can see whether the drop from 96 to 81 seconds came from a few people.

### Deviations from the plan

One analyst missed a session through illness and completed it a week later. The registration allowed this; the deviation is reported with the date.

### Worked example

Nadia's results paragraph: "Enriched cards raised accuracy from 0.738 to 0.869 (paired difference 0.131, 95% CI per registered analysis). Two true attacks were closed incorrectly in the enriched condition, both shown a high benign-history count; we treat this as a design hazard."

> **Synthetic case.** Figures come from the lab script.

### Errors and limits

Eight analysts from one SOC limit generalisation; analyst effects may dominate.

### Exercises

- **EX027 — Crossover design.** Describe the crossover design. *Rubric:* 3 = each analyst both conditions, counterbalanced order, swapped sets; 2 = partial; 1 = two groups; 0 = none.
- **EX028 — Enrichment fields.** What context did enriched cards add? *Rubric:* 3 = asset criticality, user role, benign-history count; 2 = two; 1 = one; 0 = none.
- **EX029 — Interval results.** Report both accuracies with intervals. *Rubric:* 3 = 0.738 [0.664, 0.800]; 0.869 [0.808, 0.913]; 2 = values only; 1 = wrong; 0 = none.
- **EX030 — Paired analysis.** Why is the paired analysis the main test? *Rubric:* 3 = same analysts in both conditions; 2 = partial; 1 = no reason; 0 = none.
- **EX031 — Harm found.** What harm did enrichment cause? *Rubric:* 3 = two attacks closed with high benign-history count; 2 = partial; 1 = vague; 0 = none.
- **EX032 — Validation method.** How was the analysis independently validated? *Rubric:* 3 = outside statistician reran from raw logs blind to results; matched; 2 = partial; 1 = self-checked; 0 = none.

### Synthesis

Controlled designs, interval estimates, independent reanalysis and honest reporting of harms make a main study credible.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes

You will (1) seek and receive structured critique; (2) classify critiques by severity; (3) revise claims, analyses and text in response; (4) document responses transparently.

### 6.1 Sources of critique

Nadia's committee, an external examiner in training, Northgate's senior analysts and a workshop paper's anonymous reviewers all read the draft. Each sees different weaknesses. Each source looks at the thesis differently: the committee at method, the trainee examiner at structure, the senior analysts at realism and the workshop reviewers at the claim. Nadia logs every comment in one table with its source, so none is lost between drafts. The table also records which draft each change entered and whether the commenter saw the revised text, so Prof. Grant can check that each source had a chance to respond to Nadia's changes.

### 6.2 The main critiques

Reviewer 1: "The corpus is synthetic; benign triggers in real SOCs are messier." Reviewer 2: "The benign-history field may be doing all the work; you cannot separate the three fields." Reviewer 3: "Two missed attacks are a safety issue, not a footnote." A senior analyst: "Your alert cards lack the raw command line that we always look at first." The analyst's comment shows how practice can see what researchers miss: the cards were designed from the Contextual property, but analysts work from the raw event.

### 6.3 Classifying severity

Nadia sorts critiques into: threatens validity (Reviewer 2), changes conclusions (Reviewer 3), limits scope (Reviewer 1), improves realism (analyst). Validity threats are answered first. Answering validity threats first makes sense because they could change what the data mean. Reviewer 2's point led to the exploratory follow-up with single-field cards, while Reviewer 3's point changed how prominently the missed attacks were reported. The analyst's comment led to the raw command line being restored on all cards. Reviewer 1's point became a stated limit on realism, with a plan for an operational pilot.

### 6.4 Responses

To Reviewer 2 she runs an exploratory follow-up with four analysts and single-field cards; history alone gives most of the gain and both missed attacks — evidence that history context is powerful and risky. To Reviewer 3 she moves the harm to the abstract and recommends showing history only alongside a "why it could still be malicious" prompt. To Reviewer 1 she adds a limits section and releases the generator so others can test realism. The analyst's point is accepted for the next study.

### 6.5 The response letter

Each critique is quoted, followed by the change made (with page numbers) or a reasoned disagreement. Nadia's letter answers Reviewer 2 by describing the follow-up and labelling its result exploratory, so the reviewer can see that the confound was addressed without overstating it. Where she disagrees, as with a request to drop the synthetic corpus altogether, she explains why with evidence from the realism review and the ethical limits on real SOC data. Every change carries a page number. Prof. Grant reads the letter before it is sent, checking that each claimed change can be found on the page it cites.

### 6.6 Avoiding defensive revision

Grant reminds her that rebuttal without change rarely persuades; where a reviewer is wrong, show evidence. For Reviewer 3, rebuttal would have meant arguing that two attacks in many decisions were a small number. Nadia instead moved the missed attacks into the abstract and added a design recommendation, which persuaded the reviewer more than any argument could. Grant's reminder applies to her own instincts as much as to the reviewers' tone. The response letter shows the change for each critique that was accepted.

### Worked example

Response excerpt: "R2.1 — We agree the fields are confounded. A follow-up (n = 4 analysts, 40 alerts each) with single-field cards suggests the benign-history field accounts for most of the improvement and for both missed attacks (reported in the critique chapter, labelled exploratory)."

> **Synthetic case.** Critiques and follow-up are invented.

### Errors and limits

A four-analyst follow-up is exploratory; it guides future work but cannot settle attribution.

### Exercises

- **EX033 — Severity classes.** Name the four severity classes used. *Rubric:* 3 = validity, conclusions, scope, realism; 2 = three; 1 = one; 0 = none.
- **EX034 — Confounded fields.** What was Reviewer 2's critique, and how was it answered? *Rubric:* 3 = fields confounded; single-field follow-up, history drives gain and misses; 2 = partial; 1 = ignored; 0 = none.
- **EX035 — Safety framing.** How was the missed-attack critique handled? *Rubric:* 3 = moved to abstract; recommend counter-prompt with history; 2 = partial; 1 = footnote; 0 = none.
- **EX036 — Realism response.** What answered the synthetic-corpus critique? *Rubric:* 3 = limits section; release generator for testing; 2 = one; 1 = vague; 0 = none.
- **EX037 — Letter format.** Describe a good response letter entry. *Rubric:* 3 = quote, change with location or reasoned disagreement; 2 = partial; 1 = rebuttal only; 0 = none.
- **EX038 — Follow-up status.** Why is the follow-up labelled exploratory? *Rubric:* 3 = small, unplanned for confirmation; cannot settle attribution; 2 = partial; 1 = confirmatory; 0 = none.

### Synthesis

Gather critique widely, rank it by threat to validity, revise with evidence and document every response.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes

You will (1) synthesise findings into a coherent thesis argument; (2) build a reproducibility archive; (3) separate confirmatory and exploratory results; (4) state implications for practice and research.

### 7.1 The argument

The thesis argues: (1) benign triggers dominate analyst workload, consistent with Alahmadi et al. (2022); (2) context on alert cards improves triage accuracy; (3) benign-history context carries a specific risk of dismissing true attacks; (4) alert design should pair context with counter-evidence prompts. Each step rests on a different kind of evidence: the first on literature, the second on the registered experiment, the third on the failure analysis and exploratory follow-up, and the fourth on Nadia's judgement from all three. The thesis labels the fourth as a recommendation, not a finding.

### 7.2 Confirmatory versus exploratory

Chapter results are tagged: the accuracy effect is confirmatory (registered); the field attribution and time effect are exploratory. Tables mark each. Tagging tells readers how much weight each result can bear. The confirmatory accuracy effect was tested as registered; the attribution to the benign-history field comes from a small follow-up with four analysts and is a lead, not a conclusion. Nadia's summary table repeats each tag next to the archive file that reproduces the result. The time result carries a secondary tag, matching how it was registered before the main study.

### 7.3 The archive

The archive contains: the alert generator and seed; the 320-alert corpus with labels; Sigma-format rules used; anonymised analyst logs; analysis scripts with pinned versions; the pre-registration and change log; and a README explaining how to rerun every table. The archive lets another researcher regenerate every alert, rule match, card and table from the seed. Anonymised logs replace the raw triage records, as the consent forms promised. The change log and pre-registration show readers which choices were fixed before the data and which came later.

### 7.4 Testing the archive

A fellow student downloads the archive on a clean machine and regenerates all tables. Two figures differ in the fourth decimal because of a rounding call; Nadia fixes the script and notes it. The differences were small, but finding them shows that the test checks the archive itself. Nadia records the fix in the change log and tags a new archive version. A colleague at Calder ran the test on a clean machine, using only the archive's instructions. Her rebuilt tables differed in two rounding places, traced to an unpinned library version. Pinning that version made the outputs match exactly.

### 7.5 Licensing and privacy

Corpus and code are released under an open licence. Analyst logs are anonymised: analyst IDs are random, timestamps shifted, free-text notes removed after review for identifying content. Removing free-text notes after review prevents analysts from being identified by their writing or by details of their workplace. Shifted timestamps keep durations accurate while hiding when sessions occurred. The open licence lets other researchers reuse the corpus for different alert-card experiments, which is the point of the first contribution. The archive README explains each anonymisation step, so reusers know which fields were removed and why.

### 7.6 Implications

For SOCs: test enrichment fields one at a time and monitor missed-attack rates; history fields need guard rails. For research: field-level experiments and realism studies on corpora. The SOC-CMM (van Os, 2016) offers a way for SOCs to place such changes within capability maturity. The implications follow the evidence: the missed attacks support the advice on history fields, while the exploratory attribution supports testing fields one at a time. Each implication in the thesis names the result it rests on, so a reader can follow it back to the evidence and its confirmatory or exploratory tag before applying it at their own SOC.

### 7.7 Mapping to frameworks

Findings are mapped to NIST CSF 2.0's Detect function (adverse event analysis) so practitioners can locate them. Mapping the work to adverse event analysis lets a SOC manager see that the findings concern how alerts are assessed after detection, not how rules are written. Nadia also notes the related Respond activities, since dismissing a true attack at triage delays every later step of incident handling. The mapping appears in the practitioner article as well as the thesis. The thesis cites NIST CSF 2.0 for the mapping, using its Detect and Respond functions by name.

### Worked example

Nadia's thesis summary table lists each claim, evidence chapter, status (confirmatory or exploratory) and archive file that reproduces it.

> **Synthetic case.** The archive and test are invented.

### Errors and limits

Archives decay as software changes; pinned versions and a container description slow but do not stop decay.

### Exercises

- **EX039 — Four claims.** State the thesis's four claims. *Rubric:* 3 = benign triggers dominate; context helps; history risk; pair with counter-prompts; 2 = three; 1 = one; 0 = none.
- **EX040 — Status tags.** Which results are confirmatory and which exploratory? *Rubric:* 3 = accuracy confirmatory; attribution and time exploratory; 2 = partial; 1 = all confirmatory; 0 = none.
- **EX041 — Archive contents.** List six archive items. *Rubric:* 3 = six of generator, corpus, rules, logs, scripts, registration, README; 2 = four; 1 = two; 0 = none.
- **EX042 — Archive test.** What did the clean-machine test reveal? *Rubric:* 3 = fourth-decimal rounding difference; fixed and noted; 2 = partial; 1 = nothing; 0 = none.
- **EX043 — Log anonymisation.** How were analyst logs anonymised? *Rubric:* 3 = random IDs, shifted times, free text removed; 2 = two; 1 = one; 0 = none.
- **EX044 — Practice implication.** Give one implication for SOCs. *Rubric:* 3 = test fields singly, monitor misses, guard history fields; 2 = partial; 1 = vague; 0 = none.

### Synthesis

A thesis earns trust by a clear argument, honest status tags and an archive that others can actually rerun.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes

You will (1) prepare for a doctoral defense; (2) anticipate hard questions; (3) plan publication of papers, corpus and code; (4) plan responsible engagement with practitioners.

### 8.1 The defense

The defense tests whether the candidate can explain, justify and limit the work. Nadia prepares a 40-minute talk: problem, design, results, harm, limits, contributions. Nadia gives the harm finding its own slide immediately after the accuracy result, so examiners see both together. She rehearses with Prof. Grant and with a colleague who plays the external examiner, and keeps backup slides for the follow-up study and the archive test. The talk itself lasts about forty minutes. Nadia ends it with the limits of a synthetic corpus and the planned operational pilot, so the examiners' questions start from what the study cannot show.

### 8.2 Hard questions

Mock examiners ask: "Why should a SOC trust a synthetic corpus?" "Is a 13-point gain worth the two missed attacks?" "Would results hold for analysts with two months' experience?" "What would falsify your claim?" Nadia answers with evidence and admits where she does not know. Her answers draw on the thesis: the realism review for the synthetic corpus, the failure analysis for the missed attacks, and the participant profile for analyst experience, which she admits her sample does not cover. For the falsification question, she names an operational pilot across at least two SOCs.

### 8.3 The trade-off question

On the missed attacks, Nadia avoids a simple yes. She explains that the value depends on the SOC's base rates and costs (Axelsson, 2000): if benign triggers consume most analyst time, the gain frees capacity for deeper investigation, but only if guard rails reduce the history-driven misses. She proposes measuring both in an operational pilot. Her answer keeps the two outcomes in one sentence, as the evidence does, and uses the same reasoning about base rates that motivated the project in the first place.

### 8.4 Publication plan

Paper 1 (experiment and harm) to a security venue; paper 2 (corpus and generator) to a dataset track; a practitioner article for SOC managers. The corpus and code are released with the first paper. Releasing the corpus with the first paper lets reviewers check the experiment's material directly. The dataset paper describes the generator, labels and benign-trigger annotations so others can extend them. The practitioner article leads with the guard-rail recommendation for history fields and states the limits of a synthetic corpus.

### 8.5 Practitioner engagement

Nadia presents results to Northgate's analysts first, as promised in consent forms, and offers a design note on alert cards. She avoids marketing language. Presenting first to Northgate's analysts keeps the promise made when they consented, and lets them hear about the missed attacks before anyone else. Ruth Okonkwo receives the same aggregate results; no analyst's individual performance is shown. The design note proposes context fields with counter-evidence prompts, matching the thesis's recommendation. Analysts can comment on the note before it goes to Ruth.

### 8.6 After the defense

Corrections required by examiners are tracked and completed before final submission; the archive is updated with a version tag. Each correction is listed with the examiner's comment, the change and the page, and any change that affects a figure triggers a rerun from the archive. The final version tag is cited in the thesis and the papers, so all outputs point to the same reproducible state of the work. Prof. Grant signs off each correction after checking it against the examiners' list, and the final thesis is deposited at Calder with the archive link.

### 8.7 Strategy alignment

Her design note references Strategy 8 of Knerler, Parker and Zimmerman (2022), "Leverage tools to support analyst workflow", to connect the research with SOC planning language. The connection lets SOC managers place her recommendation within a plan they may already use, instead of treating it as an isolated research idea. Nadia is careful not to claim that the strategy is validated by her study; she cites it as planning language, while her evidence concerns one design choice within it. The practitioner article cites the same strategy, so SOC managers reading only the article see the same boundary on her claim.

### Worked example

At the mock defense, asked "What would falsify your claim?", Nadia answers: "An operational pilot in which enriched cards with guard rails showed no accuracy gain, or a missed-attack rate higher than baseline, across at least two SOCs."

> **Synthetic case.** The defense and plans are invented.

### Errors and limits

Publication timelines depend on reviewers; plan for revision cycles.

### Exercises

- **EX045 — Talk structure.** Outline the defense talk. *Rubric:* 3 = problem, design, results, harm, limits, contributions; 2 = four; 1 = two; 0 = none.
- **EX046 — Trade-off answer.** How did Nadia answer the gain-versus-misses question? *Rubric:* 3 = depends on base rates and costs; capacity gain only with guard rails; operational pilot; 2 = partial; 1 = yes/no; 0 = none.
- **EX047 — Falsification.** What would falsify the claim? *Rubric:* 3 = operational pilot with no gain or higher misses across two SOCs; 2 = partial; 1 = nothing; 0 = none.
- **EX048 — Publication outputs.** List the planned outputs. *Rubric:* 3 = experiment paper, corpus paper, practitioner article, open release; 2 = three; 1 = one; 0 = none.
- **EX049 — Northgate first.** Why present to Northgate's analysts first? *Rubric:* 3 = promised in consent; respect participants; 2 = partial; 1 = marketing; 0 = none.
- **EX050 — Strategy link.** Which MITRE strategy did the design note cite, and why? *Rubric:* 3 = Strategy 8, tools supporting analyst workflow; connects to planning language; 2 = number or name; 1 = wrong; 0 = none.

### Synthesis

A strong defense explains, justifies and limits the work; publication and engagement plans honour participants and help practice.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Nadia Ferreira, Prof. Elias Grant, Calder University, Northgate Shared SOC, Ruth Okonkwo and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Detection quality is whether a rule fires correctly (precision and recall); triage quality is whether analysts reach correct dispositions (accuracy, time, agreement); operational outcome is whether incidents end sooner or with less harm (for example time to containment).

**EX002.** That SOC research is fragmented and has little empirical evaluation.

**EX003.** Managers and analysts frequently see different problems as the SOC's main issues.

**EX004.** "Estimate the difference in triage accuracy and median time-to-disposition between baseline and enriched alert cards on 160 synthetic alerts with known labels, with 95% intervals."

**EX005.** Hypotheses, primary and secondary measures, the reasoning for sample size, the analysis plan and exclusion rules.

**EX006.** Participation is voluntary, managers never see individual results, and anyone may withdraw.

**EX007.** Findings carry over only as far as the synthetic mix resembles real alert traffic, so the thesis must list the features it left out.

**EX008.** Since real intrusions are rare among events, even a tiny false-positive rate means most alerts are false.

**EX009.** 0.087 with a 1% false-positive rate and 0.487 with 0.1%.

**EX010.** A benign trigger is a correct match on real behaviour that happens to be legitimate in context; a false positive in the strict sense is a match on behaviour the rule did not intend.

**EX011.** Reliable, Explainable, Analytical, Contextual and Transferable.

**EX012.** Attacks are rare, normal behaviour is extremely varied and errors are expensive to explain, so anomaly detection fits poorly without careful evaluation.

**EX013.** At the alert and triage level: it tests whether contextual information helps analysts dismiss benign triggers while still catching real attacks.

**EX014.** She dates the review and keeps the exact search terms so it can be rerun.

**EX015.** An open labelled synthetic alert corpus, a crossover experiment on context enrichment, and a failure analysis of misleading enrichment.

**EX016.** If rules were poor, detection errors would swamp the triage effect the study is designed to measure.

**EX017.** v1 has precision 0.50 and recall 0.75; v2 has precision 1.00 and recall 1.00 on this set.

**EX018.** They are realistic legitimate matches, the very cases enrichment should help analysts close correctly.

**EX019.** Earlier studies measured perceptions or automated ranking, but few ran controlled experiments on alert-card context with known labels.

**EX020.** Whether either rule is valid in general; eight events only demonstrate how replay scoring works.

**EX021.** Unless the baseline behaves like real triage, a difference from enrichment cannot be interpreted.

**EX022.** Observed agreement 0.90, chance agreement 0.625, kappa 0.73.

**EX023.** Substantial agreement, the band from 0.61 to 0.80.

**EX024.** Both were discussed; one label was corrected and the other alert was rewritten to remove ambiguity.

**EX025.** The criticality field was overlooked (moved to the top), logging missed changed dispositions (fixed), and 40-alert sessions caused fatigue (split into two with a break).

**EX026.** When one label is much rarer than the other, chance agreement is high, so kappa can be low even when raters mostly agree.

**EX027.** Every analyst triaged in both conditions, in counterbalanced order, with the alert sets exchanged between halves.

**EX028.** The asset's criticality, the user's role and how many similar alerts had been closed as benign in the past 30 days.

**EX029.** Baseline 0.738 (95% CI 0.664–0.800); enriched 0.869 (0.808–0.913).

**EX030.** Because each analyst contributed to both conditions, a paired comparison removes differences between analysts.

**EX031.** Two genuine attacks were dismissed in the enriched condition, each displaying a large benign-history count.

**EX032.** A statistician at another university repeated the analysis from raw logs and scripts without seeing Nadia's figures, and obtained the same numbers.

**EX033.** Threatens validity, changes conclusions, limits scope, and improves realism.

**EX034.** The three enrichment fields could not be separated; a small single-field follow-up suggested the benign-history field produced most of the gain and both missed attacks.

**EX035.** The harm was moved into the abstract, with a recommendation to pair history with a prompt explaining why the alert could still be malicious.

**EX036.** A limits section was added and the alert generator released so others can test realism.

**EX037.** It quotes the critique, then states the change made with page references, or gives a reasoned and evidenced disagreement.

**EX038.** With four analysts and no confirmatory registration it can suggest, but not establish, which field caused the effect.

**EX039.** Benign triggers dominate workload; alert context improves accuracy; benign-history context risks dismissing true attacks; context should come with prompts for counter-evidence.

**EX040.** The accuracy effect is confirmatory; the attribution to individual fields and the time reduction are exploratory.

**EX041.** The generator with its seed, the labelled corpus, the Sigma rules, anonymised logs, pinned analysis scripts and the pre-registration with change log (and a README).

**EX042.** Two figures differed in the fourth decimal because of rounding; the script was fixed and the fix recorded.

**EX043.** Analysts got random IDs, timestamps were shifted and free-text notes were stripped after checking for identifying content.

**EX044.** Introduce enrichment fields one at a time and watch missed-attack rates, adding guard rails to history fields.

**EX045.** Problem, study design, results, the harm found, limits, and contributions.

**EX046.** She said it depends on prevalence and the cost of each error: the gain frees analyst time only if guard rails cut history-driven misses, which an operational pilot should measure.

**EX047.** An operational pilot across at least two SOCs showing no accuracy gain, or more missed attacks than baseline, with guard rails in place.

**EX048.** A paper on the experiment and harm, a dataset paper on the corpus and generator, a practitioner article, and open release of corpus and code.

**EX049.** The consent forms promised participants would hear results first.

**EX050.** Strategy 8, "Leverage tools to support analyst workflow", because it ties the findings to how SOCs plan their tooling.

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
