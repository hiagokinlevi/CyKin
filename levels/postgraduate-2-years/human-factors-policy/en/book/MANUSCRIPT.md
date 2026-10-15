# Human Factors and Cyber Policy: Postgraduate Course

- Language: English (`en`); course 144, Postgraduate course (2 years).
- Editorial state: **published**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; six offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working security practitioners leading a human-centred security programme in a mid-sized organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs compare expected loss, compute risk differences, test weight sensitivity, analyse a stepped rollout with a permutation test and summarise assurance and help desk data, all synthetic; no real staff, emails or accounts are involved. Any phishing simulation described is announced, approved by a panel including staff representatives and HR, avoids lures exploiting personal distress such as pay, bonuses or health, is reported only in aggregate and is never used in performance reviews. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one practitioner-student redesigning an insurer's programme: decision framing, current practice, specialist evidence, risk and ethics, design alternatives, controlled evaluation, integration, difficult cases, leadership and assurance, research critique, an applied project and final review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Daniel Osei** | Security manager and postgraduate student | Invented |
| **Dr Ingrid Holm** | Course leader | Invented |
| **Westbrook School of Professional Studies** | Fictional school | Invented |
| **Calloway Insurance** | Fictional insurer, 900 staff | Invented |

### Core sources

Hansche et al. (2024), NIST SP 800-50r1; Beautement, Sasse and Wonham (2008), [doi:10.1145/1595676.1595684](https://doi.org/10.1145/1595676.1595684); Lain, Kostiainen and Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766); Bada, Sasse and Nurse (2019), arXiv:1901.02672; Herley (2009), [doi:10.1145/1719030.1719050](https://doi.org/10.1145/1719030.1719050). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame human-centred security decisions under uncertainty; (2) use expected loss alongside staff burden; (3) document decision rationale for leaders.

### 1.1 Framing the decision

Daniel Osei, a security manager studying part-time at the fictional Westbrook School of Professional Studies, faces a decision at the fictional Calloway Insurance, a firm of 900 staff. The board wants to know whether to buy an expanded simulation service or invest in faster reporting and verification controls. His course leader, Dr Ingrid Holm, asks him to frame the decision explicitly: the options, the outcomes that matter, the uncertainties and the people affected. A clear frame prevents the choice from being made on vendor enthusiasm or habit alone.

### 1.2 Expected loss and burden

Daniel estimates expected annual loss from payment fraud and credential theft under each option, using ranges rather than single numbers because evidence is uncertain. He adds staff burden, estimated in hours per year, because Herley (2009) showed that security advice imposes real costs on users that organisations often ignore. The lab compares options by expected loss reduction and by staff hours, showing that the verification option reduces more loss while costing staff fewer hours, though the ranges overlap enough to require judgement.

### Lab — Expected loss reduction and staff hours for two options

```python
# Expected loss reduction (thousands) and staff hours for two options (synthetic, triangular estimates).
opts = {"verification and reporting": ((180, 300, 450), 1800), "expanded simulations": ((60, 130, 230), 4500)}
for name, ((lo, mode, hi), hrs) in opts.items():
    mean = (lo + mode + hi) / 3
    print(f"{name}: expected loss reduction {mean:.0f}k (range {lo}-{hi}k), staff hours {hrs}")
```

Run with `python3 lab_decide.py`. Verified output:

```text
verification and reporting: expected loss reduction 310k (range 180-450k), staff hours 1800
expanded simulations: expected loss reduction 140k (range 60-230k), staff hours 4500
```

### 1.3 Documenting rationale

Daniel writes a two-page decision note for the board stating the options, estimates, assumptions and his recommendation for the verification and reporting option. He records what would change his mind, such as evidence that simulation results predict real fraud losses. The note uses plain language and shows ranges. Documenting the rationale lets the board challenge the reasoning, and it creates a record that future reviewers can compare with actual outcomes, which supports learning across decisions rather than only within one. The board reads it before the meeting.

### Worked example

Daniel frames a programme choice at Calloway Insurance, compares expected loss and staff hours and documents a recommendation with conditions for change.

> **Synthetic case.** Calloway and all figures are synthetic; Herley (2009) is real.

### Errors and limits

Loss estimates are uncertain. Hours estimates may omit hidden effort.

### Exercises

- **EX001 — Decision frame.** What elements make up Daniel's decision frame? *Rubric:* 3 = options, outcomes, uncertainties and people affected;; 2 = frame;; 1 = vague;; 0 = none.
- **EX002 — Herley cost.** Why include staff hours following Herley (2009)? *Rubric:* 3 = security advice imposes real user costs;; 2 = burden;; 1 = vague;; 0 = none.
- **EX003 — Lab comparison.** How did the two options compare on loss reduction and hours? *Rubric:* 3 = verification 310k and 1,800 h; simulations 140k and 4,500 h;; 2 = verification better;; 1 = vague;; 0 = none.
- **EX004 — Mind-changer.** What evidence would change Daniel's mind? *Rubric:* 3 = simulation results predicting real fraud losses;; 2 = prediction;; 1 = vague;; 0 = none.
- **EX005 — Note purpose.** Why document the rationale? *Rubric:* 3 = so it can be challenged and compared with outcomes later;; 2 = record;; 1 = vague;; 0 = none.

### Synthesis

Advanced decisions frame options, weigh loss and burden and record rationale openly.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Human factors and cyber policy: current practice

### Learning outcomes

You will (1) describe current practice in security awareness programmes; (2) relate practice to guidance such as NIST SP 800-50r1; (3) identify gaps between practice and evidence.

### 2.1 Current practice

Daniel surveys current practice through industry reports and conversations with peers. Many organisations run annual online courses, monthly simulated phishing and dashboards of click rates by department. Fewer measure reporting speed or invest in verification procedures for high-risk tasks. The Verizon DBIR continues to report a large human element in breaches, which organisations often cite to justify training. Daniel notes that practice is shaped as much by what is easy to buy and report as by what evidence shows works. He records each source.

### 2.2 Guidance

NIST SP 800-50r1 (Hansche et al., 2024) describes building a cybersecurity and privacy learning programme, including assessing needs, designing role-based content, implementing, and evaluating. The older SP 800-16 (Wilson et al., 1998) set out the distinction between awareness, training and education. The ENISA cybersecurity culture guidelines stress understanding and shaping culture rather than delivering messages alone. Daniel maps Calloway's programme against these documents and finds that needs assessment and evaluation are weakest, while content delivery is strongest. He shares the mapping with the risk committee so that members can see where effort is concentrated and where the programme needs to grow next.

### 2.3 Gaps

Comparing practice with evidence, Daniel finds gaps. Lain, Kostiainen and Čapkun (2022) found that embedded training after simulated clicks did not reduce later clicks, yet Calloway uses exactly that. Bada, Sasse and Nurse (2019) found fear-based messages often backfire, yet Calloway's posters use alarming images. Reporting, which Lain and colleagues found valuable at scale, is hard at Calloway because the report address is buried. Identifying these gaps gives Daniel a starting agenda grounded in published evidence rather than personal preference. He lists each gap with its source.

### Worked example

Daniel reviews common practice, maps Calloway against SP 800-50r1, SP 800-16 and ENISA guidance and identifies three gaps against evidence.

> **Synthetic case.** Calloway is synthetic; the cited guidance and studies are real.

### Errors and limits

Peer conversations are anecdotal. Guidance is not evidence of effect.

### Exercises

- **EX006 — Common practice.** Which measure dominates common practice? *Rubric:* 3 = click rates by department;; 2 = clicks;; 1 = reporting speed;; 0 = none.
- **EX007 — Weakest stages.** Which programme stages were weakest at Calloway? *Rubric:* 3 = needs assessment and evaluation;; 2 = two;; 1 = delivery;; 0 = none.
- **EX008 — Embedded training gap.** What evidence conflicts with Calloway's embedded training? *Rubric:* 3 = Lain et al. found it did not reduce clicks;; 2 = Lain;; 1 = vague;; 0 = none.
- **EX009 — Poster gap.** Which practice conflicts with Bada et al. (2019)? *Rubric:* 3 = alarming fear-based posters;; 2 = fear;; 1 = vague;; 0 = none.
- **EX010 — Reporting gap.** Why is reporting weak at Calloway? *Rubric:* 3 = the report address is buried;; 2 = access;; 1 = vague;; 0 = none.

### Synthesis

Current practice often lags evidence, and guidance helps map the gaps.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Human factors and cyber policy: specialist evidence

### Learning outcomes

You will (1) appraise specialist studies of security behaviour; (2) interpret effect sizes and uncertainty; (3) judge transferability to an organisation.

### 3.1 Appraising studies

Daniel appraises key studies in detail. For each he asks what was studied, with whom, how outcomes were measured, whether there was a comparison and what limits the authors state. Lain and colleagues studied thousands of employees in one company over fifteen months with randomised conditions, giving strong internal validity. Adams and Sasse (1999) used questionnaires and interviews to explain password behaviour, offering depth rather than measurement of effects. Appraisal helps him use each study for what it can support. He keeps notes on each one.

### 3.2 Effect sizes

Daniel learns to read effect sizes, not just significance. A difference may be statistically significant yet small in practice, or large but uncertain. The lab computes a risk difference and its confidence interval for a synthetic comparison of reporting rates between two training formats. The interval is wide, so although one format looks better, the data are consistent with a small or even zero benefit. He notes that decisions should consider the plausible range, not only the point estimate. He reports both numbers.

### Lab — Risk difference and interval for two formats

```python
# Risk difference with Wald 95% interval for two training formats (synthetic).
from math import sqrt
a, n1, b, n2 = 37, 100, 31, 100
p1, p2 = a / n1, b / n2; d = p1 - p2; se = sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
print(f"format A {p1:.0%}, format B {p2:.0%}, difference {100 * d:.1f} points, 95% CI {100 * (d - 1.96 * se):.1f} to {100 * (d + 1.96 * se):.1f}")
```

Run with `python3 lab_effect.py`. Verified output:

```text
format A 37%, format B 31%, difference 6.0 points, 95% CI -7.1 to 19.1
```

### 3.3 Transferability

A finding from one organisation may not hold in another. Daniel compares Calloway with the organisations in key studies: size, sector, culture and attack exposure. Calloway resembles the large company in Lain's study in its email-heavy work, so the reporting finding likely transfers; it differs from the university settings in some password studies. He records his transferability judgements explicitly, so that others can see why he relies more on some studies than others when designing Calloway's programme. Dr Holm reviews these judgements.

### Worked example

Daniel appraises studies by design, reads an effect size with its interval and judges transferability to Calloway.

> **Synthetic case.** Lab data are synthetic; cited studies are real.

### Errors and limits

Transferability is a judgement. Published studies favour positive results.

### Exercises

- **EX011 — Lain design strength.** What gives Lain et al. strong internal validity? *Rubric:* 3 = randomised conditions over fifteen months;; 2 = randomisation;; 1 = vague;; 0 = none.
- **EX012 — Adams and Sasse method.** What did Adams and Sasse (1999) offer? *Rubric:* 3 = depth from questionnaires and interviews;; 2 = depth;; 1 = effect size;; 0 = none.
- **EX013 — Lab difference.** What risk difference did the lab compute? *Rubric:* 3 = 6.0 points, interval -7.1 to 19.1;; 2 = wide;; 1 = vague;; 0 = none.
- **EX014 — Interval meaning.** What does the wide interval mean? *Rubric:* 3 = benefit could be small or zero;; 2 = uncertain;; 1 = vague;; 0 = none.
- **EX015 — Transfer judgement.** Why does Lain's reporting finding likely transfer? *Rubric:* 3 = Calloway resembles the large email-heavy company;; 2 = similarity;; 1 = vague;; 0 = none.

### Synthesis

Specialist evidence is appraised by design, read with uncertainty and transferred with explicit judgement.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) assess human-centred risks using SP 800-30r1 concepts; (2) analyse ethical issues in workplace security programmes; (3) set governance for ethical practice.

### 4.1 Human-centred risk

Daniel assesses risks where human behaviour plays a part, following the concepts in NIST SP 800-30r1: threat sources, events, vulnerabilities, likelihood and impact. For payment fraud, the threat source is criminal groups, the event a fake supplier change request, the vulnerability the absence of independent verification and the impact direct financial loss. He notes that the vulnerability lies in the process, not in staff character. Framing risk this way points to process controls rather than to more warnings for staff. The risk owner agrees.

### 4.2 Ethical issues

Daniel analyses ethical issues in Calloway's programme. Simulations use deception without specific consent. Department click rankings shame teams publicly. Staff who click repeatedly are sent to mandatory training described as remedial. Some templates mimic bonus announcements. He judges each against principles of respect, proportionality and harm. The bonus template exploits financial hopes and the rankings undermine trust; both could discourage reporting. He also notes that monitoring data about individuals could be misused in performance reviews if not controlled. He discusses each with HR.

### 4.3 Governance

Daniel proposes governance for ethical practice: a charter stating the purpose of the programme; a review panel including staff representatives and HR to approve simulation templates; a ban on lures exploiting personal distress such as pay, bonuses or health; aggregate reporting only; no use of simulation results in performance reviews; and an annual ethics review. Governance turns good intentions into rules that persist when people change, and it gives staff a voice in a programme that affects them directly. The board adopts it.

### Worked example

Daniel frames payment fraud risk in SP 800-30r1 terms, identifies ethical problems in rankings and bonus lures and proposes governance with a review panel.

> **Synthetic case.** Calloway's programme is synthetic; SP 800-30r1 is real.

### Errors and limits

Panels can approve borderline content. Ethics reviews may become routine.

### Exercises

- **EX016 — Fraud vulnerability.** Where does the payment fraud vulnerability lie? *Rubric:* 3 = in the absence of independent verification;; 2 = process;; 1 = staff character;; 0 = none.
- **EX017 — Bonus template.** Why is the bonus template unethical? *Rubric:* 3 = it exploits financial hopes;; 2 = distress;; 1 = vague;; 0 = none.
- **EX018 — Ranking harm.** What harm do department rankings cause? *Rubric:* 3 = public shaming that undermines trust;; 2 = trust;; 1 = vague;; 0 = none.
- **EX019 — Panel members.** Who sits on the template review panel? *Rubric:* 3 = staff representatives and HR;; 2 = representatives;; 1 = vague;; 0 = none.
- **EX020 — Performance rule.** What rule applies to simulation results and performance reviews? *Rubric:* 3 = they are never used;; 2 = prohibition;; 1 = vague;; 0 = none.

### Synthesis

Human-centred risk points to process controls, and governance makes ethical practice durable.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Human factors and cyber policy: design alternatives

### Learning outcomes

You will (1) generate alternative programme designs; (2) evaluate them against multiple criteria; (3) select and justify a design.

### 5.1 Alternatives

Daniel generates three designs for Calloway. Design A refines the current model with better simulations and shorter training. Design B centres on reporting: a prominent button, fast feedback, a no-blame policy and simulations reduced to quarterly under the new governance. Design C centres on engineering: phishing-resistant authentication for all staff, payment verification controls and strong filtering, with minimal training. He describes each in a page, including what staff would experience day to day, so stakeholders can picture the change. Stakeholders read all three.

### 5.2 Evaluating

Daniel scores the designs with stakeholders on risk reduction, staff burden, cost, trust and regulatory evidence. Weights are agreed before scoring. The lab computes weighted scores and tests whether the ranking changes when each weight is varied by half in either direction. Design C scores highest for risk reduction but lowest for regulatory evidence; Design B balances well. A combination of B and C emerges as the strongest option across most weight settings, which gives the board confidence that the result is not fragile.

### Lab — Weighted scores and sensitivity for three designs

```python
# Weighted scores and sensitivity for three designs plus a combination (synthetic 1-5 scores).
crit = ["risk", "burden", "cost", "trust", "evidence"]
w0 = dict(risk=0.30, burden=0.20, cost=0.15, trust=0.20, evidence=0.15)
S = {"A": [2, 2, 4, 2, 5], "B": [4, 4, 4, 5, 3], "C": [5, 4, 2, 3, 2], "B+C": [5, 4, 3, 5, 4]}
def score(w): return {k: sum(w[c] * v for c, v in zip(crit, vals)) / sum(w.values()) for k, vals in S.items()}
print("base:", {k: round(v, 2) for k, v in score(w0).items()})
wins = 0
for c in crit:
    for f in (0.5, 1.5):
        s = score(dict(w0, **{c: w0[c] * f})); wins += max(s, key=s.get) == "B+C"
print("B+C ranked first in", wins, "of 10 variations")
```

Run with `python3 lab_weights.py`. Verified output:

```text
base: {'A': 2.75, 'B': 4.05, 'C': 3.5, 'B+C': 4.35}
B+C ranked first in 10 of 10 variations
```

### 5.3 Selecting

Daniel recommends a combined design: the engineering controls of C with the reporting culture of B, retaining brief role-based training to satisfy regulators. He explains the trade-off: higher first-year cost for lasting reductions in risk and burden. He notes risks of the combination, such as project overload, and proposes phasing over eighteen months. The board accepts, asking for a progress review at six months. Selection based on explicit criteria makes the decision easier to defend and to revisit. The phasing plan is agreed.

### Worked example

Daniel designs three alternatives, scores them with stakeholder weights, tests sensitivity and recommends a phased combination.

> **Synthetic case.** Designs and scores are synthetic.

### Errors and limits

Scores are subjective. Combined designs may overload teams.

### Exercises

- **EX021 — Design C weakness.** Where does Design C score lowest? *Rubric:* 3 = regulatory evidence;; 2 = evidence;; 1 = risk;; 0 = none.
- **EX022 — Weight timing.** When were weights agreed? *Rubric:* 3 = before scoring;; 2 = before;; 1 = after;; 0 = none.
- **EX023 — Lab sensitivity.** How robust was the combined design in the lab? *Rubric:* 3 = first in 10 of 10 weight variations;; 2 = robust;; 1 = vague;; 0 = none.
- **EX024 — Phasing.** Over what period is the combined design phased? *Rubric:* 3 = eighteen months;; 2 = 18;; 1 = vague;; 0 = none.
- **EX025 — Combined risk.** What risk does the combination carry? *Rubric:* 3 = project overload;; 2 = overload;; 1 = vague;; 0 = none.

### Synthesis

Alternatives evaluated on agreed weights, with sensitivity tests, support robust selection.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Human factors and cyber policy: controlled evaluation

### Learning outcomes

You will (1) design a controlled evaluation of a programme change; (2) analyse results with appropriate tests; (3) address ethical constraints in evaluation.

### 6.1 Designing the evaluation

Daniel plans to evaluate the new feedback messages that tell reporters within an hour whether their report was malicious. He uses a stepped rollout: six offices start in month one, six in month two and six in month three, with order chosen randomly. Every office eventually receives the change, which addresses fairness concerns. The outcome is the share of real malicious emails reported by at least one person in each office per month, using data that the reporting system already collects without extra burden.

### 6.2 Within-month analysis

The lab compares office-months with and without feedback, adjusting for month by comparing within each month. Offices with feedback show a higher share of malicious emails reported. Daniel computes the average within-month difference and checks it with a permutation test that shuffles which offices had feedback. The observed difference is larger than almost all shuffled differences. He reports the estimate, the permutation result and the limits, including that office sizes differ and that the period is short. The difference is about 14 points.

### Lab — Stepped rollout analysis with permutation test

```python
# Stepped rollout: 18 offices, start months 1-3 (6 each), 4 months of data (synthetic).
import random
r = random.Random(3)
start = [1] * 6 + [2] * 6 + [3] * 6; r.shuffle(start)
base = [r.uniform(0.45, 0.65) for _ in range(18)]
y = {(o, m): min(1, base[o] + 0.03 * m + (0.16 if m >= start[o] else 0) + r.gauss(0, 0.05)) for o in range(18) for m in range(4)}
def effect(st):
    diffs = []
    for m in range(1, 4):
        t = [y[o, m] for o in range(18) if m >= st[o]]; c = [y[o, m] for o in range(18) if m < st[o]]
        if t and c: diffs.append(sum(t) / len(t) - sum(c) / len(c))
    return sum(diffs) / len(diffs)
obs = effect(start)
cnt = 0; N = 2000
for _ in range(N):
    s = start[:]; r.shuffle(s); cnt += effect(s) >= obs
print(f"within-month difference {100 * obs:.1f} points; permutation share {cnt / N:.3f}")
```

Run with `python3 lab_stepped.py`. Verified output:

```text
within-month difference 14.4 points; permutation share 0.001
```

### 6.3 Ethical constraints

The evaluation uses existing data in aggregate, so individual consent is not needed for each staff member, but Daniel informs staff through the charter and newsletters that the feedback change is being evaluated by office. The governance panel approves the plan. No simulations are part of the evaluation. He notes that an evaluation that withheld useful feedback indefinitely from some offices would be unfair; the stepped design limits delay to two months, which the panel considers acceptable for the knowledge gained.

### Worked example

Daniel evaluates feedback messages with a randomised stepped rollout across eighteen offices, finds a positive within-month difference and documents ethical approval.

> **Synthetic case.** Offices and data are synthetic.

### Errors and limits

Short evaluations miss long-term effects. Offices differ in exposure.

### Exercises

- **EX026 — Rollout order.** How was the rollout order chosen? *Rubric:* 3 = randomly;; 2 = random;; 1 = by size;; 0 = none.
- **EX027 — Outcome measure.** What outcome was used? *Rubric:* 3 = share of malicious emails reported per office per month;; 2 = reported share;; 1 = clicks;; 0 = none.
- **EX028 — Lab estimate.** What within-month difference did the lab find? *Rubric:* 3 = about 14.4 points, permutation share 0.001;; 2 = positive;; 1 = vague;; 0 = none.
- **EX029 — No simulations.** Were simulations part of the evaluation? *Rubric:* 3 = no; it used real reported emails only;; 2 = no, without saying what was used;; 1 = yes;; 0 = no answer.
- **EX030 — Maximum delay.** What was the maximum delay for any office? *Rubric:* 3 = two months;; 2 = 2;; 1 = vague;; 0 = none.

### Synthesis

Controlled evaluations can be fair, ethical and informative when rollout is staged and randomised.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Human factors and cyber policy: organizational integration

### Learning outcomes

You will (1) integrate the programme with HR, finance and incident response; (2) align with governance frameworks; (3) manage change across departments.

### 7.1 Cross-department links

Daniel integrates the programme with other functions at Calloway. HR adds security expectations to induction and agrees that simulation data stay out of performance processes. Finance adopts the payment verification control, with holds on bank detail changes and callbacks using known numbers. Incident response receives reports automatically and credits first reporters in its summaries. Each link turns the programme from a security team project into part of how Calloway works, which makes it more durable and less dependent on a few enthusiasts.

### 7.2 Framework alignment

Daniel maps the programme to the Govern function of NIST CSF 2.0, which covers roles, responsibilities, policy and oversight, and to ISO/IEC 27001:2022 requirements for awareness and competence. He shows the risk committee how each element supplies evidence for audits. He is careful not to let frameworks define success; they describe structures, while outcomes such as faster reporting and fewer frauds show whether the programme works. Alignment reduces duplicated effort when auditors and regulators request evidence. Auditors welcome the mapping. The committee agrees.

### 7.3 Managing change

Daniel uses a simple change plan for each department: explain why, involve local champions, pilot with one team, adjust and then extend. Finance initially resists the verification control because it slows payments at month-end. He works with them to schedule a second officer at month-end and to pre-verify regular suppliers. Resistance often signals a real cost, and addressing that cost wins support more effectively than insisting on compliance. By month nine, all three departments have adopted their parts of the programme.

### Worked example

Daniel links the programme to HR, finance and incident response, maps it to CSF 2.0 Govern and ISO/IEC 27001 and manages finance resistance by addressing month-end costs.

> **Synthetic case.** Integration is synthetic; NIST CSF 2.0 and ISO/IEC 27001:2022 are real.

### Errors and limits

Integration takes time. Framework mapping can become paperwork.

### Exercises

- **EX031 — HR agreement.** What did HR agree about simulation data? *Rubric:* 3 = it stays out of performance processes;; 2 = separation;; 1 = vague;; 0 = none.
- **EX032 — Govern scope.** What does the CSF 2.0 Govern function cover? *Rubric:* 3 = roles, responsibilities, policy and oversight;; 2 = governance;; 1 = detection;; 0 = none.
- **EX033 — Framework role.** What role should frameworks play? *Rubric:* 3 = describe structures, not define success;; 2 = structure;; 1 = outcomes;; 0 = none.
- **EX034 — Finance resistance.** Why did finance resist the verification control? *Rubric:* 3 = it slowed month-end payments;; 2 = month-end;; 1 = vague;; 0 = none.
- **EX035 — Resistance lesson.** What does resistance often signal? *Rubric:* 3 = a real cost;; 2 = cost;; 1 = stubbornness;; 0 = none.

### Synthesis

Integration embeds the programme in other functions and treats resistance as information.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Human factors and cyber policy: difficult cases

### Learning outcomes

You will (1) handle cases involving repeated clickers, executives and whistleblowing; (2) balance accountability with support; (3) apply consistent principles.

### 8.1 Repeated clickers

A small number of Calloway staff click simulated emails repeatedly. The old programme sent them to remedial training. Daniel reviews the cases with HR and finds that most work in roles receiving very high volumes of external email, such as claims handling. He proposes support rather than sanction: workload review, extra filtering for their inboxes and phishing-resistant authentication so that a click causes less harm. He notes that labelling people as repeat offenders is likely to reduce their willingness to report mistakes.

### 8.2 Executives

Senior executives are frequent targets yet often exempt themselves from the programme. Daniel proposes that executives follow the same verification rules, have assistants trained in callback procedures and receive short personal briefings on impersonation of themselves. He explains that attackers impersonate executives precisely because staff hesitate to question them. An executive who publicly welcomes verification calls gives staff permission to check, which strengthens the whole organisation. The CEO agrees to record a short message saying so. Assistants receive the briefing as well.

### 8.3 Whistleblowing and reporting

A staff member reports that a manager has been asking colleagues to share passwords to cover absences. This is a policy breach but also a symptom of understaffing. Daniel ensures the report is handled confidentially through the whistleblowing route, that the reporter is protected and that the underlying workload issue is raised. He applies consistent principles across cases: protect reporters, look for system causes, apply sanctions only for deliberate harmful acts and keep decisions documented and fair. The manager receives support too.

### Worked example

Daniel reframes repeated clicking as a workload and design issue, brings executives under the same rules and handles a password-sharing report through whistleblowing with system fixes.

> **Synthetic case.** Cases are synthetic.

### Errors and limits

Support may be seen as leniency. Executive buy-in may fade.

### Exercises

- **EX036 — Clicker roles.** Where did most repeated clickers work? *Rubric:* 3 = high-volume external email roles such as claims;; 2 = claims;; 1 = vague;; 0 = none.
- **EX037 — Clicker support.** What support did Daniel propose for repeated clickers? *Rubric:* 3 = workload review, extra filtering and phishing-resistant authentication;; 2 = support;; 1 = remedial training;; 0 = none.
- **EX038 — Executive message.** What did the CEO agree to do? *Rubric:* 3 = record a message welcoming verification calls;; 2 = permission;; 1 = vague;; 0 = none.
- **EX039 — Password sharing cause.** What underlying issue did the password-sharing report reveal? *Rubric:* 3 = understaffing;; 2 = workload;; 1 = malice;; 0 = none.
- **EX040 — Sanction rule.** When do sanctions apply under Daniel's principles? *Rubric:* 3 = only for deliberate harmful acts;; 2 = deliberate;; 1 = any mistake;; 0 = none.

### Synthesis

Difficult cases call for consistent principles that protect reporters and fix system causes.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Human factors and cyber policy: leadership and assurance

### Learning outcomes

You will (1) lead a human-centred security programme; (2) provide assurance to boards and regulators; (3) communicate uncertainty honestly.

### 9.1 Leading the programme

Daniel leads a small team and a network of thirty champions across departments. He sets a clear purpose: help people make safe choices easily and report quickly. He holds monthly champion meetings to share examples and problems. He models the behaviour he asks for, reporting his own near misses openly. Leadership in this field is less about commanding compliance and more about creating conditions in which people feel able to act safely and speak up when something seems wrong. Champions rotate yearly.

### 9.2 Assurance

The board and the insurance regulator ask for assurance that human risks are managed. Daniel provides a quarterly report with outcome measures: median time to first report, share of malicious emails reported, payment changes held and verified, and staff burden. He includes verification results for controls and the governance panel's decisions. The lab produces a quarter-by-quarter summary from synthetic data. Assurance means showing evidence that controls work and outcomes improve, not just listing activities completed. Each measure has a written definition.

### Lab — Quarterly assurance measures

```python
# Quarterly assurance measures (synthetic).
q = [("Q1", 52, 0.48, 3, 3.1), ("Q2", 31, 0.61, 5, 3.0), ("Q3", 19, 0.72, 4, 2.8), ("Q4", 14, 0.79, 6, 2.7)]
for name, med, share, held, burden in q:
    print(f"{name}: median first report {med} min, reported share {share:.0%}, fake changes held {held}, burden {burden}/5")
```

Run with `python3 lab_assure.py`. Verified output:

```text
Q1: median first report 52 min, reported share 48%, fake changes held 3, burden 3.1/5
Q2: median first report 31 min, reported share 61%, fake changes held 5, burden 3.0/5
Q3: median first report 19 min, reported share 72%, fake changes held 4, burden 2.8/5
Q4: median first report 14 min, reported share 79%, fake changes held 6, burden 2.7/5
```

### 9.3 Communicating uncertainty

Daniel reports uncertainty honestly. He shows intervals for rates, notes when changes are within normal variation and explains when attack volumes have changed. When the board asks whether the programme has made Calloway safe, he answers that it has reduced specific risks measurably but that no programme eliminates deception. The board values this candour. He notes that overclaiming would undermine trust when the next incident occurs, while honest reporting sets realistic expectations. He includes a short glossary of terms so board members can read intervals and variation without needing statistical training.

### Worked example

Daniel leads through purpose and champions, reports outcome-based assurance quarterly and communicates uncertainty honestly.

> **Synthetic case.** Measures are synthetic.

### Errors and limits

Champions vary in commitment. Quarterly data are noisy.

### Exercises

- **EX041 — Programme purpose.** What purpose did Daniel set? *Rubric:* 3 = help people make safe choices easily and report quickly;; 2 = purpose;; 1 = compliance;; 0 = none.
- **EX042 — Modelling behaviour.** How does Daniel model desired behaviour? *Rubric:* 3 = reporting his own near misses openly;; 2 = openness;; 1 = vague;; 0 = none.
- **EX043 — Lab trend.** How did median report time move across the quarters? *Rubric:* 3 = 52, 31, 19 and 14 minutes;; 2 = falling;; 1 = vague;; 0 = none.
- **EX044 — Assurance meaning.** What does assurance mean here? *Rubric:* 3 = evidence that controls work and outcomes improve;; 2 = evidence;; 1 = activity lists;; 0 = none.
- **EX045 — Board answer.** How did Daniel answer whether Calloway is safe? *Rubric:* 3 = specific risks reduced but deception not eliminated;; 2 = candour;; 1 = yes;; 0 = none.

### Synthesis

Leadership creates safe conditions, and assurance reports evidence with honest uncertainty.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read research papers critically; (2) write a structured critique; (3) identify implications for practice.

### 10.1 Critical reading

Daniel reads three papers closely: Sasse, Brostoff and Weirich (2001) on transforming the weakest link, Beautement, Sasse and Wonham (2008) on the compliance budget and Lain, Kostiainen and Čapkun (2022) on phishing in organisations. For each he notes the question, methods, findings and limits, and asks whether the conclusions follow from the evidence. He reads the methods sections carefully, because summaries in other sources often overstate findings or omit limits that the authors themselves stated clearly. He keeps a reading log with one page of notes for each paper and its limits.

### 10.2 Structured critique

Daniel writes a critique of the compliance budget paper. He summarises its argument that staff weigh security effort against business goals and have limited capacity for compliance. He notes strengths: grounded in interviews across organisations, the concept explains many observed behaviours. He notes limits: the budget is hard to measure directly and the paper offers a framework rather than tested predictions. He concludes that the concept is useful for design decisions, provided managers treat it as a lens rather than a precise quantity.

### 10.3 Implications

From his reading, Daniel draws implications for Calloway: design to reduce effort; measure burden alongside outcomes; favour collective reporting over individual perfection; and treat simulations cautiously, as evidence suggests some common practices add little. He writes these into the programme charter with citations. Critique is valuable not for finding fault but for understanding how far each study can support decisions, which protects practice from both blind faith and dismissal of research. The governance panel reviews the charter changes and approves them after a short discussion with HR.

### Worked example

Daniel reads three papers critically, critiques the compliance budget paper and writes four implications into Calloway's charter.

> **Synthetic case.** Cited works are real; Calloway is synthetic.

### Errors and limits

Critique can drift into fault-finding. Implications may stretch evidence.

### Exercises

- **EX046 — Methods focus.** Why does Daniel read methods sections carefully? *Rubric:* 3 = summaries elsewhere often overstate or omit limits;; 2 = accuracy;; 1 = vague;; 0 = none.
- **EX047 — Budget strength.** Name a strength of the compliance budget paper. *Rubric:* 3 = grounded in interviews across organisations;; 2 = grounding;; 1 = vague;; 0 = none.
- **EX048 — Budget limit.** Name a limit of the compliance budget paper. *Rubric:* 3 = the budget is hard to measure directly;; 2 = measurement;; 1 = vague;; 0 = none.
- **EX049 — Lens use.** How should managers treat the compliance budget? *Rubric:* 3 = as a lens, not a precise quantity;; 2 = lens;; 1 = number;; 0 = none.
- **EX050 — Charter implications.** Where did Daniel record his implications? *Rubric:* 3 = the programme charter with citations;; 2 = charter;; 1 = vague;; 0 = none.

### Synthesis

Critical reading weighs what studies can support and translates them carefully into practice.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) carry out an applied project on a human-centred control; (2) evaluate outcomes and burden; (3) report to stakeholders.

### 11.1 The project

Daniel's applied project introduces phishing-resistant security keys for Calloway's claims and finance staff, 240 people who handle payments and sensitive data. He plans the rollout with IT, HR and team leaders: keys are issued in short sessions, each person registers two keys and a simple recovery process is set up. He applies lessons from earlier chapters: involve users early, test with a pilot team and measure burden. The project aims to make credential phishing ineffective for the most targeted roles. The pilot team gives feedback.

### 11.2 Outcomes and burden

After four months, Daniel compares credential phishing outcomes and help desk calls. Before keys, these teams had several account compromises from phishing a year; after, none during the period, though the period is short. Help desk calls rose in the first month as people learned the keys and then fell below the previous level, because password resets declined. The lab summarises monthly help desk calls. A short survey shows most staff find keys easier than codes, though some worry about losing them.

### Lab — Help desk calls before and after keys

```python
# Monthly help desk calls for 240 staff before and after security keys (synthetic).
base = 45; after = [62, 44, 36, 31]
print("baseline per month:", base)
for m, c in enumerate(after, 1): print(f"month {m}: {c} ({c - base:+d})")
```

Run with `python3 lab_keys.py`. Verified output:

```text
baseline per month: 45
month 1: 62 (+17)
month 2: 44 (-1)
month 3: 36 (-9)
month 4: 31 (-14)
```

### 11.3 Reporting

Daniel reports to the board and staff. He states that keys removed the main route for credential theft in the targeted teams and reduced password support calls after a learning period. He notes limits: four months is short and attackers may shift to other methods, such as phone-based fraud, which the verification controls address. He recommends extending keys to all staff over the next year. Staff hear the results first, which reinforces that the programme is done with them rather than to them.

### Worked example

Daniel rolls out security keys to 240 staff, finds no phishing compromises in four months and lower help desk load after a learning month, and reports honestly.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Short periods mislead. Key loss needs good recovery.

### Exercises

- **EX051 — Target group.** Which staff received keys first? *Rubric:* 3 = claims and finance staff, 240 people;; 2 = targeted roles;; 1 = vague;; 0 = none.
- **EX052 — Two keys.** Why does each person register two keys? *Rubric:* 3 = as a backup if one is lost;; 2 = backup;; 1 = vague;; 0 = none.
- **EX053 — Help desk pattern.** What did the lab show for help desk calls? *Rubric:* 3 = rose to 62 in month one, then fell to 31 by month four from a base of 45;; 2 = dip;; 1 = vague;; 0 = none.
- **EX054 — Attacker shift.** What might attackers shift to? *Rubric:* 3 = phone-based fraud;; 2 = phone;; 1 = vague;; 0 = none.
- **EX055 — Audience order.** Who heard the results first? *Rubric:* 3 = staff, reinforcing that the programme is done with them;; 2 = staff, without explanation;; 1 = the board;; 0 = none.

### Synthesis

Applied projects deliver controls with users, measure burden and report limits.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review the programme's development as a whole; (2) transfer lessons to other contexts; (3) plan continuing professional development.

### 12.1 Reviewing the whole

Daniel reviews the two years at Calloway. The programme shifted from simulations and click rankings to reporting, fast feedback, verification controls and security keys, governed by a charter and a panel including staff representatives. Outcome measures improved: faster reporting, more malicious emails reported and fake payment changes caught. Burden fell slightly. He also lists what did not work, such as an early champion scheme that collapsed when champions had no time allocated. A whole review shows how parts interacted over time.

### 12.2 Transfer

Daniel considers how lessons transfer. A small charity would lack a security team, so the core ideas, easy reporting, kind feedback, verification for payments and strong authentication, would need simpler forms. A hospital would face clinical time pressure, making burden even more important. He writes a short transfer guide that separates principles from Calloway-specific details. Transfer requires distinguishing why something worked from how it was done, since the how often depends on local resources and culture. He tests the guide with a peer from a charity.

### 12.3 Continuing development

Daniel plans continuing development: reading new evidence each quarter, including the annual DBIR and new studies; joining a peer group of security managers; and mentoring a junior colleague in human-centred methods. Dr Holm suggests he write a short practitioner article about the stepped evaluation, since practice-based evaluations are rare in the literature. He notes that the field changes quickly as attackers adapt, so his own learning must continue well beyond the course. He also blocks two hours each month in his calendar for reading and reflection.

### Worked example

Daniel reviews the whole programme, writes a transfer guide separating principles from local details and plans continuing development.

> **Synthetic case.** The review is synthetic; the DBIR is real.

### Errors and limits

Reviews can be self-serving. Transfer guides oversimplify.

### Exercises

- **EX056 — Programme shift.** What did the programme shift from and to? *Rubric:* 3 = from simulations and rankings to reporting, feedback, verification and keys;; 2 = shift;; 1 = vague;; 0 = none.
- **EX057 — Failed scheme.** What early scheme failed and why? *Rubric:* 3 = champions without allocated time;; 2 = time;; 1 = vague;; 0 = none.
- **EX058 — Hospital difference.** What would matter more in a hospital? *Rubric:* 3 = burden, due to clinical time pressure;; 2 = burden;; 1 = vague;; 0 = none.
- **EX059 — Transfer distinction.** What must transfer distinguish? *Rubric:* 3 = why something worked from how it was done;; 2 = principle;; 1 = vague;; 0 = none.
- **EX060 — Article suggestion.** What article did Dr Holm suggest? *Rubric:* 3 = on the stepped evaluation;; 2 = evaluation;; 1 = vague;; 0 = none.

### Synthesis

Final review connects the parts, separates principles from details and commits to continued learning.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Daniel Osei, Dr Ingrid Holm, Westbrook School of Professional Studies, Calloway Insurance and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The options, the outcomes that matter, the uncertainties and the people affected.

**EX002.** Because security advice imposes real costs on users that are often ignored.

**EX003.** Verification reduced expected loss by about 310 thousand with 1,800 staff hours, simulations by about 140 thousand with 4,500 hours.

**EX004.** Evidence that simulation results predict real fraud losses.

**EX005.** So the board can challenge it and future reviewers can compare it with outcomes.

**EX006.** Click rates by department from simulations.

**EX007.** Needs assessment and evaluation.

**EX008.** Lain, Kostiainen and Čapkun (2022) found embedded training did not reduce later clicks.

**EX009.** Calloway's fear-based posters.

**EX010.** Because the report address is hard to find.

**EX011.** Randomised conditions with thousands of employees over fifteen months.

**EX012.** Depth of explanation from questionnaires and interviews.

**EX013.** A 6.0 point difference with a 95% interval from about -7.1 to 19.1 points.

**EX014.** That the true benefit could be small or even zero.

**EX015.** Because Calloway resembles the large, email-heavy company studied.

**EX016.** In the process, which lacks independent verification.

**EX017.** Because it exploits staff's financial hopes and anxieties.

**EX018.** They shame teams publicly and undermine trust, discouraging reporting.

**EX019.** Staff representatives and HR, alongside security.

**EX020.** Simulation results are never used in performance reviews.

**EX021.** On regulatory evidence.

**EX022.** Before any scoring took place.

**EX023.** It ranked first in all ten weight variations.

**EX024.** Eighteen months.

**EX025.** The risk of overloading project teams.

**EX026.** Randomly.

**EX027.** The share of real malicious emails reported by at least one person, per office per month.

**EX028.** About 14.4 percentage points, with only 0.1% of shuffles as large.

**EX029.** No; it used real reported emails only.

**EX030.** Two months.

**EX031.** That simulation data stay out of performance processes.

**EX032.** Roles, responsibilities, policy and oversight.

**EX033.** They describe structures; outcomes show whether the programme works.

**EX034.** Because it slowed payments at month-end.

**EX035.** A real cost that needs addressing.

**EX036.** In roles with very high external email volume, such as claims handling.

**EX037.** Workload review, extra filtering and phishing-resistant authentication.

**EX038.** Record a message welcoming verification calls.

**EX039.** Understaffing that led to covering absences.

**EX040.** Only for deliberate harmful acts.

**EX041.** To help people make safe choices easily and report quickly.

**EX042.** By reporting his own near misses openly.

**EX043.** It fell from 52 to 31, 19 and then 14 minutes.

**EX044.** Evidence that controls work and outcomes improve, not just activities.

**EX045.** That specific risks were reduced but no programme eliminates deception.

**EX046.** Because other summaries often overstate findings or omit stated limits.

**EX047.** It is grounded in interviews across organisations and explains many behaviours.

**EX048.** The budget is hard to measure directly and the paper offers a framework, not tested predictions.

**EX049.** As a lens for design, not a precise quantity.

**EX050.** In the programme charter, with citations.

**EX051.** Claims and finance staff, 240 people.

**EX052.** So there is a backup if one key is lost.

**EX053.** Calls rose to 62 in the first month and then fell to 31 by month four, below the 45 baseline.

**EX054.** Phone-based fraud, addressed by verification controls.

**EX055.** Staff, reinforcing that the programme is done with them.

**EX056.** From simulations and click rankings to reporting, fast feedback, verification and security keys.

**EX057.** An early champion scheme, because champions had no time allocated.

**EX058.** Burden, because of clinical time pressure.

**EX059.** Why something worked from how it was done locally.

**EX060.** A practitioner article about the stepped evaluation.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Beautement, A., Sasse, M. A., & Wonham, M. (2008). The compliance budget: Managing security behaviour in organisations. *Proceedings of the 2008 New Security Paradigms Workshop*, 47–58. <https://doi.org/10.1145/1595676.1595684>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Herley, C. (2009). So long, and no thanks for the externalities: The rational rejection of security advice by users. *Proceedings of the 2009 New Security Paradigms Workshop*, 133–144. <https://doi.org/10.1145/1719030.1719050>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Verizon Business. (2024). *2024 Data breach investigations report*. Verizon. <https://www.verizon.com/business/resources/reports/dbir/>
- Wilson, M., de Zafra, D. E., Pitcher, S. I., Tressler, J. D., & Ippolito, J. B. (1998). *Information technology security training requirements: A role- and performance-based model* (NIST SP 800-16). NIST. <https://doi.org/10.6028/NIST.SP.800-16>
