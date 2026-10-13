# Human Factors and Cyber Policy: Doctoral Research Track

- Language: English (`en`); course 190, Doctoral research track (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: doctoral candidates testing whether a change in security awareness practice changes real staff behaviour.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs compute coder agreement, a stepped-design effect with a permutation check and archive digests on synthetic data; no real person, mailbox or simulation is involved. Phishing simulations described here follow an ethical protocol: organisational approval, no credential capture, no individual blame and aggregate reporting only. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one doctoral candidate testing whether a reporting-focused awareness programme improves timely reporting of real suspicious emails: integrity and methods, the research frontier, the proposal, baseline replication and pilot, the main study and validation, critique, synthesis and archive, and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Mireille Okonjo** | Doctoral candidate | Invented |
| **Prof. Henrik Aalto** | Supervisor | Invented |
| **Calder University** | Fictional university | Invented |
| **Vantor Municipal Services** | Fictional city council with 4,000 staff | Invented |
| **Brenholt District** | Fictional replication council | Invented |

### Core sources

Adams and Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff and Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Whitten and Tygar (1999); Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050); Lain, Kostiainen and Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766); NIST [SP 800-50 Rev. 1](https://doi.org/10.6028/NIST.SP.800-50r1) and the [NIST Phish Scale](https://doi.org/10.6028/NIST.TN.2276). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes

You will (1) frame a falsifiable question about security behaviour; (2) set integrity and ethics rules for research with employees; (3) measure agreement when coding reported emails.

### 1.1 A falsifiable question

Mireille Okonjo is a doctoral candidate at the fictional Calder University, supervised by Prof. Henrik Aalto. Her partner is the fictional Vantor Municipal Services, a city council with four thousand staff. Vantor's awareness programme is judged by the share of staff who click simulated phishing links. Mireille's question is narrower and testable: does a programme built on easy reporting and immediate, supportive feedback raise the share of real suspicious emails reported within thirty minutes, compared with the existing click-focused programme? She writes down in advance which result would show her idea is wrong.

### 1.2 Why click rates mislead

Mireille reviews the critique of click rates as an outcome. Click rates depend heavily on how hard the lure is, so they change when the simulation changes even if staff behaviour does not. Lain, Kostiainen and Čapkun (2022) studied phishing in a large organisation over a long period and found that some popular training practices did not help as expected, while staff reporting was a valuable signal. Dawkins and Jacobs (2023) describe the NIST Phish Scale for rating lure difficulty. She decides to fix lure difficulty in her study and use reporting as the main outcome.

### 1.3 Integrity and ethics

Research with employees carries risks of deception, embarrassment and power imbalance. Mireille's protocol, approved by Calder's ethics board and Vantor's works council, sets rules: simulations are announced at the organisational level in advance, without dates; no individual results go to managers; nobody is disciplined for clicking; no real credentials are collected, since the landing page records only that a link was opened; and staff who click see a short supportive explanation. She pre-registers hypotheses, outcomes and analysis before collecting data, so she cannot adjust them after seeing results.

### 1.4 Coding reported emails

Her outcome depends on judging whether a reported real email was actually suspicious. Two trained coders independently label a pilot sample of reports as suspicious or benign using a written guide. The lab computes agreement and Cohen's kappa, which corrects for agreement expected by chance; Landis and Koch (1977) offer conventional bands for interpreting it. Agreement is high enough to proceed, and disagreements lead to a clearer rule about newsletters with tracking links. Measured coder agreement is part of the evidence that her outcome means something stable.

### Lab — Coder agreement on reported emails

```python
# Cohen's kappa for two coders labelling 50 pilot reports suspicious (1) or benign (0), synthetic.
a = [1] * 22 + [0] * 3 + [1] * 2 + [0] * 23
b = [1] * 22 + [1] * 3 + [0] * 2 + [0] * 23
n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
pa, pb = sum(a) / n, sum(b) / n
pe = pa * pb + (1 - pa) * (1 - pb)
print(f"reports {n}; agreement {po:.2f}; chance {pe:.3f}; kappa {(po - pe) / (1 - pe):.2f}")
```

Run with `python3 lab_kappa.py`. Verified output:

```text
reports 50; agreement 0.90; chance 0.500; kappa 0.80
```

### Worked example

Mireille frames a falsifiable reporting question, replaces click rate with reporting at fixed lure difficulty, writes ethical rules for simulations and measures coder agreement.

> **Synthetic case.** Calder, Vantor and all people are synthetic; Lain et al. (2022), Dawkins and Jacobs (2023) and Landis and Koch (1977) are real.

### Errors and limits

Pre-registration does not stop all bias. Kappa depends on prevalence in the sample.

### Exercises

- **EX001 — Falsifiable outcome.** What makes Mireille's question falsifiable? *Rubric:* 3 = she states in advance which result would show her idea is wrong;; 2 = prior statement;; 1 = none;; 0 = none.
- **EX002 — Click-rate flaw.** Why are click rates a weak outcome? *Rubric:* 3 = they depend heavily on lure difficulty;; 2 = difficulty;; 1 = none;; 0 = none.
- **EX003 — Lure difficulty tool.** Which published tool helps rate lure difficulty? *Rubric:* 3 = the NIST Phish Scale (Dawkins and Jacobs, 2023);; 2 = Phish Scale;; 1 = none;; 0 = none.
- **EX004 — Landing page rule.** How does the protocol avoid collecting credentials? *Rubric:* 3 = the landing page records only that a link was opened;; 2 = no capture;; 1 = none;; 0 = none.
- **EX005 — Manager reports.** Who receives individual simulation results? *Rubric:* 3 = nobody; only aggregates are reported;; 2 = aggregates;; 1 = managers;; 0 = none.
- **EX006 — Kappa result.** What kappa did the pilot coding reach in the lab? *Rubric:* 3 = 0.80 on 50 reports, agreement 0.90;; 2 = about 0.8;; 1 = none;; 0 = none.
- **EX007 — Coding rule change.** What rule changed after coder disagreements? *Rubric:* 3 = newsletters with tracking links were defined more clearly;; 2 = newsletters;; 1 = none;; 0 = none.

### Synthesis

Doctoral work on security behaviour needs a falsifiable outcome, strict ethics for simulations and measured agreement on how outcomes are coded.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Human factors and cyber policy: research frontier

### Learning outcomes

You will (1) map the research frontier on awareness and behaviour; (2) identify gaps that matter for policy; (3) position a contribution against prior work.

### 2.1 From weakest link to partners

Mireille traces how the field changed. Adams and Sasse (1999) showed that users who broke password rules were often coping with unworkable demands, not acting carelessly. Sasse, Brostoff and Weirich (2001) argued that calling users the weakest link hides design failures, and that usable security should be the goal. Whitten and Tygar (1999) showed that even motivated users could not use encryption software correctly. Together these works moved the frontier from blaming people to designing systems and policies that fit how people actually work.

### 2.2 Rational rejection and budgets

Herley (2009) argued that users often rationally reject security advice because its costs exceed its benefits for them. Beautement, Sasse and Wonham (2008) described a compliance budget: people have limited capacity for security effort, and each new demand competes with work. Bada, Sasse and Nurse (2019) reviewed why awareness campaigns often fail to change behaviour, citing fear messages, information overload and lack of practical support. Mireille notes that these ideas predict her intervention should succeed only if reporting is cheap and feedback is useful to staff.

### 2.3 Policy frameworks

Mireille reviews policy guidance. NIST SP 800-50 Rev. 1 (Hansche et al., 2024) frames awareness and training as a learning programme with roles, needs assessment and evaluation. ISO/IEC 27001:2022 requires organisations to ensure staff awareness and competence. The ENISA cybersecurity culture guidelines (2019) draw on behavioural science and recommend measuring culture, not just completion. She notes that frameworks require evaluation but rarely say what outcome to evaluate, which leaves organisations defaulting to completion counts and click rates because they are easy to measure. This gap is one reason she chose reporting as her main outcome.

### 2.4 The gap

Mireille states the gap: few studies compare reporting-focused programmes with click-focused ones in a public-sector organisation, at fixed lure difficulty, with pre-registered outcomes and an independent replication. Her contribution is a staggered field study with those features and a reusable measurement protocol. Prof. Aalto pushes her to state what the contribution is not: it does not measure whether breaches fall, which would need far more time and data. Positioning a claim precisely against prior work protects it from both overstatement and dismissal.

### Worked example

Mireille traces the move from weakest-link thinking to usable security, reviews budget and rejection arguments, maps policy guidance and states a precise gap.

> **Synthetic case.** The positioning is synthetic; all cited works are real.

### Errors and limits

Literature maps reflect the reader's choices. Policy guidance changes between revisions.

### Exercises

- **EX008 — Adams and Sasse finding.** What did Adams and Sasse (1999) find about rule-breaking users? *Rubric:* 3 = they were coping with unworkable demands, not careless;; 2 = coping;; 1 = careless;; 0 = none.
- **EX009 — Johnny study.** What did Whitten and Tygar (1999) show? *Rubric:* 3 = motivated users could not use encryption software correctly;; 2 = usability;; 1 = none;; 0 = none.
- **EX010 — Rational rejection.** Why might users rationally reject advice, per Herley (2009)? *Rubric:* 3 = its costs exceed its benefits to them;; 2 = cost-benefit;; 1 = ignorance;; 0 = none.
- **EX011 — Compliance budget idea.** What is the compliance budget? *Rubric:* 3 = limited capacity for security effort competing with work;; 2 = limited capacity;; 1 = none;; 0 = none.
- **EX012 — Framework silence.** What do frameworks often leave unspecified? *Rubric:* 3 = what outcome to evaluate;; 2 = outcome;; 1 = none;; 0 = none.
- **EX013 — Not claimed.** What does Mireille's contribution not measure? *Rubric:* 3 = whether breaches fall;; 2 = breaches;; 1 = none;; 0 = none.
- **EX014 — Contribution parts.** Name two features of her planned contribution. *Rubric:* 3 = public sector, fixed lure difficulty, pre-registration, replication, staggered design;; 2 = two;; 1 = none;; 0 = none.

### Synthesis

The frontier has moved from blaming users to designing for them; a precise contribution fills a measurable gap without overstating it.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes

You will (1) write a doctoral proposal with a staggered design; (2) justify sample size; (3) anticipate ethical and practical risks.

### 3.1 The design

Mireille proposes a stepped rollout across Vantor's twelve departments. All departments start on the existing programme. Every two months, three randomly chosen departments switch to the reporting-focused programme: a one-click report button, an automatic thank-you within minutes, a weekly digest showing what reported emails turned out to be, and short monthly simulations at a fixed Phish Scale difficulty. Randomising the order of switching lets her compare departments before and after while controlling for seasonal changes in email threats that affect everyone at once.

### 3.2 Outcomes and sample

The primary outcome is the share of real suspicious emails reported by at least one recipient within thirty minutes, coded as in chapter 1. Secondary outcomes are simulation report rates, simulation click rates and staff-reported burden from a short survey. Because departments, not individuals, are randomised, she accounts for clustering: staff in one department share managers and email patterns. With twelve clusters, she estimates the study can detect a difference of about ten percentage points, and she says plainly that smaller effects may go undetected.

### 3.3 Ethical and practical risks

Mireille lists risks and responses. Staff may feel watched: the works council reviews all messages, and only department-level results are reported. Managers may ask for names of people who click: the data agreement forbids it. A real attack during the study could be mistaken for a simulation: simulated emails carry a hidden marker known to the security team, and any real report is handled normally. The IT team may change the email filter mid-study: changes are logged so the analysis can account for them.

### 3.4 Committee review

Her proposal committee includes a statistician, an organisational psychologist and a practitioner from another council. The statistician asks for a permutation test that respects the stepped design; the psychologist asks how burden will be measured; the practitioner warns that report buttons can overwhelm small security teams. Mireille adds an automated triage step that groups duplicate reports. The committee approves with these changes. Proposals improve most when reviewers from different disciplines can challenge them before data collection begins. The committee's comments and her responses are kept in an appendix to the proposal for later readers.

### Worked example

Mireille proposes a randomised stepped rollout across twelve departments, defines outcomes with clustering, plans ethical safeguards and revises after a multidisciplinary committee.

> **Synthetic case.** The design and departments are synthetic; the Phish Scale is real.

### Errors and limits

Twelve clusters give limited power. Stepped designs can be disrupted by organisational changes.

### Exercises

- **EX015 — Randomised order.** Why randomise the order in which departments switch? *Rubric:* 3 = to control for seasonal threat changes affecting everyone;; 2 = seasonality;; 1 = none;; 0 = none.
- **EX016 — Primary outcome.** What is the study's primary outcome? *Rubric:* 3 = share of real suspicious emails reported within thirty minutes;; 2 = reporting;; 1 = clicks;; 0 = none.
- **EX017 — Clustering reason.** Why account for clustering? *Rubric:* 3 = staff in a department share managers and email patterns;; 2 = shared context;; 1 = none;; 0 = none.
- **EX018 — Real attack confusion.** How does the protocol avoid confusing real attacks with simulations? *Rubric:* 3 = simulated emails carry a hidden marker known to the security team;; 2 = marker;; 1 = none;; 0 = none.
- **EX019 — Practitioner warning.** What did the practitioner warn about? *Rubric:* 3 = report buttons can overwhelm small security teams;; 2 = workload;; 1 = none;; 0 = none.
- **EX020 — Triage response.** How did Mireille respond to the workload concern? *Rubric:* 3 = an automated triage step grouping duplicate reports;; 2 = triage;; 1 = none;; 0 = none.

### Synthesis

A strong proposal randomises what it can, measures what matters, plans for ethical risks and invites challenge before data collection.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes

You will (1) replicate a baseline measurement; (2) run a pilot of the intervention; (3) refine instruments before the main study.

### 4.1 Replicating the baseline

Before changing anything, Mireille replicates Vantor's existing measures for three months. She confirms that monthly simulation click rates vary between eight and nineteen percent, mostly tracking lure difficulty, which supports her decision to fix difficulty. She also measures the baseline for her primary outcome: about one in four real suspicious emails is reported within thirty minutes. Replication shows that her measurement process works in this setting and gives the reference point every later claim depends on. She also records how many simulations were sent each month, so that later comparisons use the same base.

### 4.2 Running a pilot

Two departments not in the main study pilot the reporting-focused programme for six weeks. Mireille watches for practical problems. The report button works in desktop email but is hidden in the mobile app, so staff who read email on phones cannot easily report. The thank-you message arrives after two hours, not minutes, because of a mail rule. Staff find the weekly digest useful but too long. Pilots exist to find such problems cheaply, before they damage the main study. Each problem is logged with the date it was found.

### 4.3 Refining instruments

Mireille fixes the problems. The vendor adds the report button to the mobile app; the mail rule is corrected; the digest is cut to three examples. She also tests the burden survey and finds one question confusing, so she rewrites it. She records every change and its reason in a log that will be published with the thesis. Prof. Aalto notes that transparent records of changes before the main study build trust in the final results. The revised survey is tested again with five volunteers before the main study, and all of them understand every question.

### 4.4 What the pilot does not show

Mireille resists reporting pilot effects as findings. Two departments over six weeks cannot show whether the programme works, and the pilot departments volunteered, so they may be unusually engaged. She reports the pilot only as a feasibility check: the programme can run, the measures work, and the practical problems are fixed. Treating a pilot as evidence of effect is a common mistake that leads to overconfident main studies and disappointing replications. She writes this caution into the pilot report itself, so that nobody at Vantor quotes the early figures as proof that the programme works, and she asks the steering group to wait for the main study.

### Worked example

Mireille replicates baseline click and reporting measures, pilots the programme in two departments, fixes three problems and reports the pilot only as feasibility.

> **Synthetic case.** Figures and departments are synthetic.

### Errors and limits

Volunteer pilots are unrepresentative. Baseline periods may include unusual events.

### Exercises

- **EX021 — Baseline click range.** What range did baseline click rates show? *Rubric:* 3 = eight to nineteen percent, tracking lure difficulty;; 2 = range;; 1 = none;; 0 = none.
- **EX022 — Baseline reporting.** What was baseline reporting of real suspicious emails? *Rubric:* 3 = about one in four within thirty minutes;; 2 = 25%;; 1 = none;; 0 = none.
- **EX023 — Mobile problem.** What problem did the pilot find with mobile email? *Rubric:* 3 = the report button was hidden in the mobile app;; 2 = mobile;; 1 = none;; 0 = none.
- **EX024 — Feedback delay.** Why did thank-you messages arrive late? *Rubric:* 3 = a mail rule delayed them by two hours;; 2 = mail rule;; 1 = none;; 0 = none.
- **EX025 — Change log.** Why log every change before the main study? *Rubric:* 3 = transparency builds trust in final results;; 2 = trust;; 1 = none;; 0 = none.
- **EX026 — Pilot limits.** Why is the pilot not evidence of effect? *Rubric:* 3 = two volunteer departments over six weeks cannot show it;; 2 = feasibility;; 1 = effect;; 0 = none.

### Synthesis

Replication fixes the baseline, and a pilot finds practical problems, but neither should be mistaken for evidence of effect.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes

You will (1) run the stepped main study; (2) estimate the effect with a permutation check; (3) arrange independent validation.

### 5.1 Running the study

The main study runs for fourteen months. Every two months three departments switch, until all twelve use the reporting-focused programme. Mireille monitors fidelity: is the button available, are thank-you messages prompt, are simulations at the agreed difficulty? Two months in, an email filter upgrade reduces the volume of suspicious emails reaching staff. Because it affects all departments at once and is logged, her design absorbs it. She publishes monthly fidelity notes to the steering group without any individual data. Each note is reviewed by the works council before circulation.

### 5.2 Estimating the effect

Mireille compares department-months before and after switching, adjusting for month to absorb organisation-wide changes. The lab runs a simplified version on synthetic data: it estimates the change in thirty-minute reporting after switching and then repeats the estimate many times with the switch order shuffled, to see how often chance alone gives an effect as large. Following her pre-registration, she reports both the estimate and the permutation share rather than a single headline number. She keeps the analysis script frozen from the date of pre-registration, and any later change is recorded with its reason so that reviewers can see exactly what was planned and what was added.

### Lab — Stepped-design effect with a permutation check

```python
# Stepped rollout: 12 departments, 7 periods; switch order randomised. Synthetic 30-minute reporting rates.
import random
random.seed(11)
order = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]   # period each department switches
base = [0.22, 0.25, 0.27, 0.24, 0.21, 0.26, 0.23, 0.28, 0.25, 0.22, 0.24, 0.26]
month = [0.0, 0.01, -0.02, 0.00, 0.01, -0.01, 0.0]
rates = [[base[d] + month[t] + (0.17 if t >= order[d] else 0) + random.gauss(0, 0.02) for t in range(7)] for d in range(12)]
def effect(o):
    # regress on treatment after removing department and month means (two-way demeaning)
    y = [row[:] for row in rates]; x = [[1.0 if t >= o[d] else 0.0 for t in range(7)] for d in range(12)]
    for m in (y, x):
        for _ in range(50):
            for d in range(12):
                a = sum(m[d]) / 7; m[d] = [v - a for v in m[d]]
            for t in range(7):
                a = sum(m[d][t] for d in range(12)) / 12
                for d in range(12): m[d][t] -= a
    num = sum(x[d][t] * y[d][t] for d in range(12) for t in range(7))
    den = sum(x[d][t] ** 2 for d in range(12) for t in range(7))
    return num / den
est = effect(order); rng = random.Random(5); k = 0; N = 2000
for _ in range(N):
    o = order[:]; rng.shuffle(o)
    if abs(effect(o)) >= abs(est): k += 1
print(f"estimated change in 30-min reporting: {est:+.3f}; permutation share {k / N:.3f}")
```

Run with `python3 lab_stepped.py`. Verified output:

```text
estimated change in 30-min reporting: +0.157; permutation share 0.000
```

### 5.3 Reading the result

The lab estimates that reporting rose by about sixteen percentage points (+0.157) after switching, and none of 2,000 shuffled orders produces an effect that large. Simulation click rates fell slightly, but less than reporting rose, and the burden survey showed no increase. Mireille states the finding narrowly: in this council, at fixed lure difficulty, the reporting-focused programme was followed by substantially more timely reporting of real suspicious emails. She does not claim fewer breaches, which the study did not measure. She reports the burden result with the same care as the main effect.

### 5.4 Independent validation

Mireille arranges for a second analyst at another university to receive the anonymised department-month data, the pre-registration and the analysis plan, but not her code. The analyst writes an independent analysis and reaches an estimate within two percentage points of hers. A second council, the fictional Brenholt District, also runs a shorter replication and finds a smaller but positive effect. Independent validation shows that the result does not depend on one analyst's choices or one organisation's peculiarities. Both validation reports are published alongside her own analysis, with differences explained.

### Worked example

Mireille runs a fourteen-month stepped study with fidelity checks, estimates a reporting effect with a permutation check and obtains independent reanalysis and replication.

> **Synthetic case.** Councils, data and results are synthetic.

### Errors and limits

Department-level outcomes hide individual variation. Replications in other councils may differ in culture.

### Exercises

- **EX027 — Fidelity checks.** What did fidelity monitoring check? *Rubric:* 3 = button availability, prompt thank-yous and fixed simulation difficulty;; 2 = three;; 1 = none;; 0 = none.
- **EX028 — Filter upgrade.** Why did the filter upgrade not spoil the study? *Rubric:* 3 = it affected all departments at once and was logged;; 2 = design absorbs;; 1 = none;; 0 = none.
- **EX029 — Lab estimate.** What effect did the lab estimate? *Rubric:* 3 = +0.157 in 30-minute reporting, permutation share 0.000 of 2,000;; 2 = positive;; 1 = none;; 0 = none.
- **EX030 — Narrow claim.** How does Mireille state the finding? *Rubric:* 3 = more timely reporting in this council at fixed difficulty, not fewer breaches;; 2 = narrow;; 1 = breaches fell;; 0 = none.
- **EX031 — Reanalysis setup.** What did the second analyst receive? *Rubric:* 3 = anonymised data, pre-registration and plan, but not the code;; 2 = no code;; 1 = everything;; 0 = none.
- **EX032 — Replication result.** What did the Brenholt replication find? *Rubric:* 3 = a smaller but positive effect;; 2 = smaller;; 1 = none;; 0 = none.

### Synthesis

A stepped study with fidelity checks, permutation inference and independent validation supports a narrow, credible claim.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes

You will (1) respond to peer review of a behaviour study; (2) revise analyses without p-hacking; (3) strengthen ethical reporting.

### 6.1 The critique

Mireille submits a paper and receives three reviews. One reviewer argues that more reporting might simply reflect more false alarms, burdening the security team. Another asks whether the thank-you messages, not the button, caused the effect. A third questions whether works council oversight changed staff behaviour by making them aware of the study. Prof. Aalto advises her to treat each comment as a hypothesis to test where possible, and to concede clearly where her data cannot answer. She writes a response letter that lists every comment with her action.

### 6.2 Testing alternatives

For false alarms, Mireille reports the share of reports coded benign before and after switching: it rose slightly, and the triage step kept handling time stable. For the mechanism question, she cannot separate button from feedback because they were introduced together, and she says so, proposing a factorial study as future work. For awareness of the study, she notes that announcements went to all departments at once, so awareness should not differ by switching time. Each response states what was pre-registered and what is exploratory.

### 6.3 Avoiding p-hacking

Reviewers suggest additional subgroup analyses by age and role. Mireille runs those that are reasonable but labels them exploratory and reports all of them, not just the interesting ones. She does not change her primary outcome or analysis. Herley and van Oorschot (2017) warn that security research often lacks the discipline of falsifiable, pre-specified claims; keeping the distinction between confirmatory and exploratory results is what lets readers trust the main finding. She also publishes a short table comparing the pre-registered plan with what was finally done, line by line, so that any deviation is visible and explained to readers.

### 6.4 Ethical reporting

A reviewer asks for more detail on harm. Mireille adds a section on how simulations were designed to avoid distress: no lures about pay cuts, bereavement or health; no lures impersonating trade unions; and a clear route for staff to complain. She reports two complaints received and how they were resolved. Ethical reporting in simulation research shows readers and organisations how to repeat the work without causing harm, which matters as much as the effect size. She also shares the full complaint procedure in an appendix.

### Worked example

Mireille tests reviewers' alternative explanations, concedes the mechanism question, reports exploratory subgroups transparently and expands ethical reporting.

> **Synthetic case.** Reviews and figures are synthetic; Herley and van Oorschot (2017) is real.

### Errors and limits

Exploratory findings may be noise. Some reviewer concerns cannot be resolved with existing data.

### Exercises

- **EX033 — False-alarm test.** How did Mireille address the false-alarm concern? *Rubric:* 3 = benign share rose slightly; triage kept handling time stable;; 2 = data;; 1 = none;; 0 = none.
- **EX034 — Mechanism limit.** Why can't she separate the button from feedback? *Rubric:* 3 = they were introduced together;; 2 = confounded;; 1 = none;; 0 = none.
- **EX035 — Future design.** What study did she propose for the mechanism question? *Rubric:* 3 = a factorial study;; 2 = factorial;; 1 = none;; 0 = none.
- **EX036 — Subgroup handling.** How were subgroup analyses reported? *Rubric:* 3 = all reported and labelled exploratory;; 2 = exploratory;; 1 = selected;; 0 = none.
- **EX037 — Excluded lure themes.** Which lure themes were excluded to avoid distress? *Rubric:* 3 = pay cuts, bereavement, health and union impersonation;; 2 = two;; 1 = none;; 0 = none.
- **EX038 — Complaints.** How many complaints were reported? *Rubric:* 3 = two, with their resolution;; 2 = two;; 1 = none;; 0 = none.

### Synthesis

Good revision tests alternatives, concedes limits, separates confirmatory from exploratory work and reports ethics openly.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes

You will (1) synthesise findings into a coherent thesis; (2) build a reproducibility archive; (3) protect participants in shared data.

### 7.1 Synthesis

Mireille's thesis connects four parts: the critique of click rates, the measurement protocol, the stepped study and the replication. She frames the overall contribution as evidence that reporting-focused programmes can improve timely reporting when reporting is cheap and feedback is fast, consistent with the compliance budget idea of Beautement, Sasse and Wonham (2008). She also lists what remains unknown: which component matters most, whether effects last beyond fourteen months and whether reporting translates into fewer harmful incidents. Each unknown is linked to a concrete design that could answer it.

### 7.2 The archive

Mireille builds an archive: pre-registration, analysis code, the coding guide, the change log, anonymised department-month data, the simulation templates with difficulty ratings and the ethics approvals. Each file is listed in a manifest with a SHA-256 digest, so anyone can check that files have not changed since publication. The lab builds a manifest for a small synthetic archive, then edits one file and shows that the check reports a mismatch. She tests the archive by asking a colleague to rerun the main analysis from it alone on a fresh computer, which succeeds after one missing file is added.

### Lab — Manifest digests for a reproducibility archive

```python
# Build a SHA-256 manifest for a synthetic archive, then detect an edited file.
import hashlib
files = {"prereg.md": b"H1: reporting rises after switch\n", "dept_month.csv": b"dept,month,rate\nG1,1,0.24\n",
         "coding_guide.md": b"Suspicious if sender spoofed or link mismatched\n"}
manifest = {n: hashlib.sha256(b).hexdigest() for n, b in files.items()}
files["dept_month.csv"] = b"dept,month,rate\nG1,1,0.42\n"
for n, b in files.items():
    print(f"{n}: {'OK' if hashlib.sha256(b).hexdigest() == manifest[n] else 'MISMATCH'} {manifest[n][:12]}")
```

Run with `python3 lab_archive.py`. Verified output:

```text
prereg.md: OK 32460485b7ca
dept_month.csv: MISMATCH 92dd85d36614
coding_guide.md: OK 0b96e40b1bab
```

### 7.3 Protecting participants

Even department-level data could identify people in small departments. Mireille merges departments with fewer than twenty staff into larger groups before release and removes dates finer than a month. Simulation templates are shared without Vantor's branding. She checks that no free-text fields remain. Vantor's data protection officer reviews the archive before release. Reproducibility and privacy can conflict, and she documents each choice so others understand what was withheld and why. The data protection officer signs a short statement confirming the review, which is included in the archive, and Mireille records which variables were removed or coarsened.

### 7.4 What the archive enables

With the archive, another researcher can rerun every analysis, check coding decisions and reuse the protocol in a new organisation. Prof. Aalto notes that this matters especially in behaviour research, where results often fail to replicate and organisations change quickly. Mireille deposits the archive in Calder's repository with a persistent identifier and a licence that permits reuse. She also writes a short practitioner guide so organisations can apply the protocol without reading the full thesis. She plans to update the archive if errors are found.

### Worked example

Mireille synthesises her findings with clear unknowns, builds a digest-checked archive, protects participants through aggregation and deposits it with a practitioner guide.

> **Synthetic case.** Archive contents are synthetic; Beautement, Sasse and Wonham (2008) is real.

### Errors and limits

Digests prove files are unchanged, not that they are correct. Aggregation reduces analytical detail.

### Exercises

- **EX039 — Overall contribution.** How does Mireille frame her overall contribution? *Rubric:* 3 = reporting-focused programmes improve timely reporting when reporting is cheap and feedback fast;; 2 = conditional;; 1 = universal;; 0 = none.
- **EX040 — Open unknowns.** Name one question the thesis leaves open. *Rubric:* 3 = which component matters, whether effects last, whether incidents fall;; 2 = one;; 1 = none;; 0 = none.
- **EX041 — Manifest check.** What did the archive lab report after editing one file? *Rubric:* 3 = MISMATCH for the edited CSV;; 2 = mismatch;; 1 = none;; 0 = none.
- **EX042 — Small departments.** How were small departments protected? *Rubric:* 3 = merged if under twenty staff;; 2 = merged;; 1 = none;; 0 = none.
- **EX043 — Privacy review.** Who reviewed the archive before release? *Rubric:* 3 = Vantor's data protection officer;; 2 = DPO;; 1 = none;; 0 = none.
- **EX044 — Practitioner guide.** Why write a short practitioner guide? *Rubric:* 3 = so organisations can apply the protocol without the full thesis;; 2 = uptake;; 1 = none;; 0 = none.

### Synthesis

A thesis synthesis states contributions and unknowns, and a privacy-aware archive lets others verify and reuse the work.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes

You will (1) defend the thesis against expert questions; (2) plan publications for academic and practitioner audiences; (3) set a post-doctoral research agenda.

### 8.1 The defense

At her defense, examiners ask hard questions. One asks whether reporting could rise because staff fear being caught by simulations. Mireille points to the burden survey and to the policy of no individual consequences, and admits she cannot rule out some anxiety-driven reporting. Another asks why she did not measure breaches; she explains the time and data that would require. Examiners value clear answers that separate what her evidence shows from what it cannot show. She prepares for the defense by rehearsing with two colleagues who play sceptical examiners and question every limitation in turn.

### 8.2 Policy implications

Examiners ask what councils should do. Mireille recommends that organisations evaluate awareness programmes by timely reporting rather than click rates alone, rate simulation difficulty, never punish individuals for clicking, and invest in making reporting easy. She links these to NIST SP 800-50 Rev. 1, which calls for evaluating learning programmes, and to the ENISA culture guidelines. She adds that policy should require ethical review of simulations, since poorly designed ones can damage trust between staff and security teams. Each recommendation is tied to a specific result in the thesis.

### 8.3 Publication plan

Mireille plans three outputs: a journal article on the stepped study, a methods paper on the measurement protocol, and a practitioner briefing for public-sector security teams. Each has a target venue and a draft timeline. The archive's persistent identifier is cited in all three. She plans to share the practitioner briefing through a public-sector network, so that the results reach organisations which rarely read academic journals. She also plans to present the work at a public-sector security conference and to write a plain-language summary for Vantor staff who took part, thanking them and explaining what their participation showed.

### 8.4 Post-doctoral agenda

Mireille's next research question follows from her limits: a factorial study to separate the report button from feedback, and a longer study linking reporting to incident response time. She applies for funding with Vantor and Brenholt as partners. Prof. Aalto's final advice is to keep the discipline that made the thesis credible: pre-registration, ethical simulation design and independent validation. Her defense passes with minor corrections. She also plans to mentor a master's student who will help with the factorial study, and she schedules a meeting with both councils to agree what data each can share under the new project.

### Worked example

Mireille answers examiners with clear limits, draws ethical policy recommendations, plans three publications and sets a factorial follow-up agenda.

> **Synthetic case.** The defense and plans are synthetic; SP 800-50 Rev. 1 and ENISA (2019) are real.

### Errors and limits

Policy recommendations generalise beyond one or two councils. Funding may not follow.

### Exercises

- **EX045 — Fear question.** How did Mireille answer the fear-driven reporting question? *Rubric:* 3 = burden survey and no-consequence policy, admitting some anxiety cannot be ruled out;; 2 = partly;; 1 = denied;; 0 = none.
- **EX046 — Evaluation advice.** What should organisations evaluate instead of click rates alone? *Rubric:* 3 = timely reporting;; 2 = reporting;; 1 = completion;; 0 = none.
- **EX047 — Simulation ethics policy.** Why should policy require ethical review of simulations? *Rubric:* 3 = poorly designed simulations damage trust;; 2 = trust;; 1 = none;; 0 = none.
- **EX048 — Three outputs.** Which three outputs does she plan? *Rubric:* 3 = journal article, methods paper and practitioner briefing;; 2 = two;; 1 = none;; 0 = none.
- **EX049 — Next study.** What is her next research question? *Rubric:* 3 = a factorial study separating button from feedback, and linking reporting to response time;; 2 = factorial;; 1 = none;; 0 = none.
- **EX050 — Defense outcome.** What was the defense outcome? *Rubric:* 3 = passed with minor corrections;; 2 = passed;; 1 = failed;; 0 = none.

### Synthesis

A doctoral defense separates evidence from speculation, turns findings into ethical policy and sets the next research questions.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Mireille Okonjo, Prof. Henrik Aalto, Calder University, Vantor Municipal Services, Brenholt District and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** She writes down beforehand the result that would show reporting-focused training does not help.

**EX002.** Because they change with how hard the lure is, even when behaviour does not change.

**EX003.** The NIST Phish Scale described by Dawkins and Jacobs (2023).

**EX004.** The landing page records only that a link was opened and collects no credentials.

**EX005.** Nobody; managers see only aggregate results.

**EX006.** Kappa 0.80 with raw agreement 0.90 on 50 pilot reports.

**EX007.** A clearer rule for newsletters containing tracking links.

**EX008.** That they were often coping with unworkable password demands rather than being careless.

**EX009.** That even motivated users could not use PGP encryption correctly.

**EX010.** Because the advice costs them more effort than the benefit they receive.

**EX011.** People's limited capacity for security effort, which competes with their main work.

**EX012.** Which outcome to evaluate, so organisations default to completion and click rates.

**EX013.** Whether actual breaches decrease.

**EX014.** A staggered field study at fixed lure difficulty with pre-registered outcomes, plus replication.

**EX015.** So that seasonal changes in email threats can be separated from the programme's effect.

**EX016.** The share of real suspicious emails reported by someone within thirty minutes.

**EX017.** Because staff in one department share managers and email patterns, so they are not independent.

**EX018.** Simulated emails carry a hidden marker, and every real report is handled normally.

**EX019.** That report buttons can overwhelm small security teams.

**EX020.** By adding automated triage that groups duplicate reports.

**EX021.** Between eight and nineteen percent, mostly tracking lure difficulty.

**EX022.** About one in four were reported within thirty minutes.

**EX023.** The report button was missing from the mobile app.

**EX024.** A mail rule delayed them by about two hours.

**EX025.** So readers can see what changed and why, which builds trust in the results.

**EX026.** Because two volunteer departments over six weeks cannot show whether the programme works.

**EX027.** That the button was available, thank-yous were prompt and simulations stayed at the agreed difficulty.

**EX028.** Because it hit all departments at the same time, was logged and was absorbed by month adjustment.

**EX029.** About sixteen percentage points (+0.157) more timely reporting, with no shuffled order out of 2,000 as large.

**EX030.** As more timely reporting in this council at fixed lure difficulty, without claiming fewer breaches.

**EX031.** Anonymised department-month data, the pre-registration and the analysis plan, but not Mireille's code.

**EX032.** A smaller but still positive effect.

**EX033.** She showed benign reports rose only slightly and triage kept handling time stable.

**EX034.** Because the button and the feedback were introduced at the same time.

**EX035.** A factorial study varying the button and feedback separately.

**EX036.** All were reported and clearly labelled exploratory.

**EX037.** Pay cuts, bereavement, health and impersonating trade unions.

**EX038.** Two complaints, reported with how each was resolved.

**EX039.** As evidence that reporting-focused programmes improve timely reporting when reporting is cheap and feedback is fast.

**EX040.** Which component matters most, whether effects last beyond fourteen months, or whether incidents fall.

**EX041.** A MISMATCH for the edited synthetic CSV, while other files stayed OK.

**EX042.** Departments with fewer than twenty staff were merged into larger groups.

**EX043.** Vantor's data protection officer.

**EX044.** So organisations can use the protocol without reading the whole thesis.

**EX045.** By citing the burden survey and no-punishment policy while admitting some anxiety-driven reporting cannot be excluded.

**EX046.** Timely reporting of suspicious emails.

**EX047.** Because poorly designed simulations can damage trust between staff and security teams.

**EX048.** A journal article, a methods paper and a practitioner briefing.

**EX049.** A factorial study separating the button from feedback, plus linking reporting to incident response time.

**EX050.** She passed with minor corrections.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Beautement, A., Sasse, M. A., & Wonham, M. (2008). The compliance budget: Managing security behaviour in organisations. *Proceedings of the 2008 New Security Paradigms Workshop*, 47–58. <https://doi.org/10.1145/1595676.1595684>
- Dawkins, S., & Jacobs, J. (2023). *NIST Phish Scale user guide* (NIST TN 2276). NIST. <https://doi.org/10.6028/NIST.TN.2276>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Whitten, A., & Tygar, J. D. (1999). Why Johnny can't encrypt: A usability evaluation of PGP 5.0. *Proceedings of the 8th USENIX Security Symposium*. USENIX. <https://www.usenix.org/conference/8th-usenix-security-symposium/why-johnny-cant-encrypt-usability-evaluation-pgp-50>
