# Security Governance, Risk and Compliance: Postgraduate Course

- Language: English (`en`); course 143, Postgraduate course (2 years).
- Editorial state: **published**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: postgraduate practitioners improving how an organisation quantifies cyber risk, oversees suppliers and informs its board.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs run a FAIR-style Monte Carlo loss model, a permutation test on review durations and an appetite comparison on synthetic data. Risk figures are illustrations, standards are cited by edition and paraphrased, and nothing here is a real audit, attestation or legal advice; SOC 2 reports described are fictional. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one risk manager through a postgraduate course: decision-making, current practice, quantified evidence, ethics, design alternatives for supplier oversight, a controlled evaluation, integration, difficult cases, appetite and board assurance, research critique, the applied project and final review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Daniel Mensah** | Postgraduate student and operational risk manager | Invented |
| **Dr. Elena Varga** | Tutor | Invented |
| **Wexford School of Management** | Fictional school | Invented |
| **Halbrook Mutual** | Fictional insurer, 2,000 staff, 300 suppliers | Invented |

### Core sources

Freund and Jones (2015), [doi:10.1016/C2013-0-09966-5](https://doi.org/10.1016/C2013-0-09966-5); Hubbard and Seiersen (2016), [doi:10.1002/9781119162315](https://doi.org/10.1002/9781119162315); Gordon and Loeb (2002); Cox (2008); Spears and Barki (2010); ISO 31000:2018; ISO/IEC 27001:2022; NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); COBIT 2019; AICPA trust services criteria. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame security decisions as choices under uncertainty; (2) separate decision quality from outcome quality; (3) identify biases in risk decisions.

### 1.1 Decisions under uncertainty

Daniel Mensah is a postgraduate student at the fictional Wexford School of Management and an operational risk manager at Halbrook Mutual, a fictional insurer with two thousand staff and a large network of brokers and claims suppliers. His tutor, Dr. Elena Varga, opens the course by asking what a good security decision is. Daniel learns to describe decisions as choices among options with uncertain consequences, judged by whether the choice made sense given the information, values and time available. At Halbrook this matters because the risk committee reviews decisions months later, when only the record of what was known at the time can show whether the choice was reasonable.

### 1.2 Decision versus outcome

A good decision can have a bad outcome, and a poor decision can be lucky. Halbrook once skipped a supplier review to meet a deadline, and nothing went wrong; managers praised the speed. Daniel learns to judge that decision on its reasoning, not its outcome. Did anyone estimate the risk? Was the appetite respected? Was the decision recorded and revisited? Separating the two protects organisations from learning the wrong lesson from luck and from punishing sound decisions that turned out badly. Daniel suggests that Halbrook's post-decision reviews ask what was known on the day of the skipped supplier review, not merely whether a breach followed.

### 1.3 Biases

Daniel studies biases that affect risk decisions: availability, where recent headlines inflate some risks; overconfidence, where experts give ranges that are too narrow; anchoring, where a first number shapes later estimates; and optimism about one's own controls. Hubbard and Seiersen (2016) describe calibration training to reduce overconfidence in security estimates. He learns that structured methods, such as recording assumptions and asking for ranges, are practical defences against bias in governance committees. For Halbrook's committee he proposes that every estimate be given as a range with its source, so that anchoring on the first number spoken becomes visible.

### Worked example

Daniel frames risk choices as decisions under uncertainty, judges a skipped supplier review on reasoning rather than outcome and lists four biases.

> **Synthetic case.** Wexford, Halbrook and all figures are synthetic; Hubbard and Seiersen (2016) is real.

### Errors and limits

Bias labels can be used to dismiss views. Records of reasoning may be incomplete.

### Exercises

- **EX001 — Good decision.** How should a good security decision be judged? *Rubric:* 3 = by whether the choice made sense given information, values and time;; 2 = reasoning;; 1 = outcome;; 0 = none.
- **EX002 — Lucky skip.** Why was praising the skipped supplier review a mistake? *Rubric:* 3 = it rewarded luck, not reasoning;; 2 = luck;; 1 = vague;; 0 = none.
- **EX003 — Overconfidence.** What does overconfidence do to expert ranges? *Rubric:* 3 = makes them too narrow;; 2 = narrow;; 1 = wide;; 0 = none.
- **EX004 — Calibration source.** Which source describes calibration training for security estimates? *Rubric:* 3 = Hubbard and Seiersen (2016);; 2 = Hubbard;; 1 = Cox;; 0 = none.
- **EX005 — Bias defence.** Name one practical defence against bias. *Rubric:* 3 = recording assumptions and asking for ranges;; 2 = structure;; 1 = vague;; 0 = none.

### Synthesis

Good security decisions are judged by reasoning under uncertainty and protected by structured methods against bias.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Security governance, risk and compliance: current practice

### Learning outcomes

You will (1) survey current GRC frameworks and their uses; (2) assess Halbrook's practice against them; (3) identify trends shaping the field.

### 2.1 Frameworks in use

Daniel maps the frameworks used at Halbrook. The security programme follows ISO/IEC 27001:2022 and holds certification. The board receives reports structured by NIST CSF 2.0 functions. Enterprise risk management follows ISO 31000:2018 principles. Internal audit uses COBIT 2019 for IT governance reviews. Suppliers provide SOC 2 reports or ISO certificates. He notes that each framework answers a different question and that mature organisations combine them rather than choosing one. For example, ISO 31000 tells Halbrook how to manage risk, while a supplier's SOC 2 report tells it how far it can rely on that supplier's controls.

### 2.2 Halbrook's practice

Daniel assesses Halbrook's practice candidly. Policies and certification are mature. Risk assessment uses a five-by-five matrix that the board finds hard to compare with financial risks. Supplier oversight relies on questionnaires that take weeks and are rarely read in depth. Board reporting is long and mostly lists activities. He concludes that Halbrook's weaknesses lie less in controls than in how risk is expressed, how suppliers are overseen and how the board is informed. These three weaknesses become the threads of his later work: loss exceedance reporting, supplier tiering and quantified appetite for the board.

### 2.3 Trends

Daniel identifies trends: growing interest in quantifying cyber risk in financial terms; regulators expecting boards to oversee cyber risk directly, reflected in the Govern function of NIST CSF 2.0; supply chain risk management becoming central; and continuous control monitoring replacing annual snapshots. He learns that trends should be weighed against the organisation's maturity, and that adopting a fashionable method without the data or skills to support it can make governance worse rather than better. Halbrook, with mature certification but sparse loss data, can adopt quantification only if it starts with a few scenarios and honest ranges.

### Worked example

Daniel maps five frameworks in use at Halbrook, finds weaknesses in risk expression, supplier oversight and board reporting and identifies four trends.

> **Synthetic case.** Halbrook's practice is synthetic; frameworks cited are real.

### Errors and limits

Trend lists date quickly. Self-assessment can be generous.

### Exercises

- **EX006 — Board structure.** Which framework structures Halbrook's board reports? *Rubric:* 3 = NIST CSF 2.0;; 2 = CSF;; 1 = COBIT;; 0 = none.
- **EX007 — Matrix problem.** Why does the board struggle with the five-by-five matrix? *Rubric:* 3 = it is hard to compare with financial risks;; 2 = comparability;; 1 = vague;; 0 = none.
- **EX008 — Supplier weakness.** What is weak about supplier oversight? *Rubric:* 3 = slow questionnaires rarely read in depth;; 2 = questionnaires;; 1 = vague;; 0 = none.
- **EX009 — Trend caution.** Why should trends be weighed against maturity? *Rubric:* 3 = methods without data or skills can make governance worse;; 2 = maturity;; 1 = vague;; 0 = none.
- **EX010 — Combining frameworks.** Why do mature organisations combine frameworks? *Rubric:* 3 = each answers a different question;; 2 = complementary;; 1 = vague;; 0 = none.

### Synthesis

Current practice combines frameworks; Halbrook's gaps lie in expressing risk, overseeing suppliers and informing the board.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Security governance, risk and compliance: specialist evidence

### Learning outcomes

You will (1) build a FAIR-style quantitative risk estimate; (2) interpret a loss distribution; (3) explain specialist evidence to non-specialists.

### 3.1 FAIR structure

Daniel studies the FAIR model described by Freund and Jones (2015), which decomposes risk into loss event frequency and loss magnitude, each estimated as a range. For a claims supplier data breach scenario, he works with claims, legal and IT staff to estimate frequency between one event in ten years and nearly one a year, most likely about one in three years, and a loss magnitude with a median near three hundred thousand and a long tail from regulatory fines and remediation. These ranges, not single points, become the inputs to the simulation in the next section.

### 3.2 The simulation

The lab simulates twenty thousand years. Mean annual loss is about one hundred and seventy thousand. In sixty-eight percent of years there is no loss at all, so the median year costs nothing. The ninetieth percentile is about five hundred and fifty-five thousand and the ninety-ninth about one point nine million. The chance of losing more than a million in a year is about four percent. Daniel notes that the mean alone would hide both the many quiet years and the severe tail. A median of zero also explains why managers who have never seen a loss may doubt the scenario is real.

### Lab — Monte Carlo loss distribution for a supplier breach scenario

```python
"""FAIR-style Monte Carlo: loss event frequency x loss magnitude (synthetic, stdlib)."""
import random
random.seed(11)
N = 20000
def year():
    n = 0; t = random.expovariate(random.triangular(0.1, 0.8, 0.3))
    while t < 1: n += 1; t += random.expovariate(random.triangular(0.1, 0.8, 0.3))
    return sum(random.lognormvariate(12.6, 0.9) for _ in range(n))
L = sorted(year() for _ in range(N))
print(f"mean annual loss {sum(L)/N/1000:,.0f}k")
print(f"P(no loss) {sum(x == 0 for x in L)/N:.2f}")
for q in (0.5, 0.9, 0.99): print(f"{int(q*100)}th percentile {L[int(q*N)]/1000:,.0f}k")
print(f"P(loss > 1,000k) {sum(x > 1e6 for x in L)/N:.3f}")
```

Run with `python3 lab_fair.py`. Verified output:

```text
mean annual loss 170k
P(no loss) 0.68
50th percentile 0k
90th percentile 555k
99th percentile 1,930k
P(loss > 1,000k) 0.041
```

### 3.3 Explaining it

Daniel presents the result to the risk committee as a loss exceedance statement: in about one year in twenty-five, losses from this scenario could exceed a million. He explains that the figures depend on estimated ranges, shows the assumptions and invites challenge. Committee members compare it with insurance and credit risks they already manage. He learns that specialist evidence persuades when it is translated into familiar terms and when its uncertainty is visible rather than hidden. Linking the cyber figure to how the committee already reads insurance exposures makes the one-in-twenty-five statement usable in the same discussion.

### Worked example

Daniel builds a FAIR-style simulation with mean 170k, 68% loss-free years, 99th percentile 1,930k and a 4% chance of exceeding a million.

> **Synthetic case.** Ranges and results are synthetic; Freund and Jones (2015) is real.

### Errors and limits

Estimates depend on expert ranges. Models omit correlated events.

### Exercises

- **EX011 — FAIR decomposition.** Into which two factors does FAIR decompose risk? *Rubric:* 3 = loss event frequency and loss magnitude;; 2 = two;; 1 = vague;; 0 = none.
- **EX012 — Mean loss.** What mean annual loss did the lab report? *Rubric:* 3 = about 170k;; 2 = 170;; 1 = vague;; 0 = none.
- **EX013 — Quiet years.** In what share of years was there no loss? *Rubric:* 3 = 68%;; 2 = 0.68;; 1 = vague;; 0 = none.
- **EX014 — Tail chance.** What is the chance of exceeding a million in a year? *Rubric:* 3 = about 4%;; 2 = 0.041;; 1 = vague;; 0 = none.
- **EX015 — Persuasion.** What makes specialist evidence persuasive to committees? *Rubric:* 3 = translation into familiar terms and visible uncertainty;; 2 = translation;; 1 = vague;; 0 = none.

### Synthesis

Quantitative risk estimates show both quiet years and severe tails when explained in familiar terms.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) identify ethical issues in risk quantification and assurance; (2) handle conflicts of interest; (3) protect people affected by risk decisions.

### 4.1 Ethics of numbers

Daniel considers ethical issues in quantification. Numbers can be used to justify cutting controls by choosing optimistic inputs, or to frighten boards into spending with pessimistic ones. He learns that ethical practice means documenting sources for each estimate, inviting independent challenge and reporting ranges honestly. He also notes that people affected by risks, such as policyholders whose data could be exposed, rarely appear in loss models, so their interests need explicit attention. In the supplier breach scenario, he therefore adds a short narrative of the harm to policyholders beside the loss figures.

### 4.2 Conflicts of interest

Daniel's role creates potential conflicts. He estimates risks for controls his own team runs, and his bonus depends partly on meeting budget targets. Dr. Varga asks how he will manage this. He proposes that internal audit review his key estimates, that he declare the conflict to the risk committee and that budget decisions be made by people other than the estimator. He learns that conflicts are normal in practice and become harmful mainly when they are hidden. He also records the declaration in the committee minutes so that later reviewers can see the conflict was known when estimates were accepted.

### 4.3 Protecting people

Halbrook considers reducing breach notification costs by narrowing what counts as a notifiable incident. Daniel points out that notification obligations come from law and that narrowing them would harm policyholders who need to protect themselves. He recommends instead investing in faster detection so incidents are smaller. He learns that GRC professionals sometimes need to defend people outside the organisation, and that compliance with law is a minimum, not the full measure of ethical conduct. Faster detection also reduces the number of policyholders affected, which the notification approach would only have hidden.

### Worked example

Daniel documents estimate sources, declares and mitigates his conflicts and defends policyholders' interests in notification decisions.

> **Synthetic case.** The cases are synthetic.

### Errors and limits

Ethical judgements can be contested. Declared conflicts still influence.

### Exercises

- **EX016 — Misused numbers.** How can numbers be misused in risk quantification? *Rubric:* 3 = optimistic or pessimistic inputs chosen to justify a conclusion;; 2 = manipulation;; 1 = vague;; 0 = none.
- **EX017 — Missing interests.** Whose interests rarely appear in loss models? *Rubric:* 3 = people affected, such as policyholders;; 2 = policyholders;; 1 = vague;; 0 = none.
- **EX018 — Conflict measures.** What did Daniel propose to manage his conflicts? *Rubric:* 3 = audit review, declaration, separate budget decision makers;; 2 = three;; 1 = vague;; 0 = none.
- **EX019 — Notification stance.** Why did Daniel oppose narrowing notifiable incidents? *Rubric:* 3 = it would harm policyholders and conflict with legal duties;; 2 = harm;; 1 = vague;; 0 = none.
- **EX020 — Compliance minimum.** How should compliance with law be viewed ethically? *Rubric:* 3 = as a minimum, not the full measure;; 2 = minimum;; 1 = vague;; 0 = none.

### Synthesis

Ethical GRC practice documents estimates, manages conflicts and protects those affected by risk.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security governance, risk and compliance: design alternatives

### Learning outcomes

You will (1) design alternative approaches to supplier oversight; (2) compare them on effectiveness, cost and burden; (3) select an approach for evaluation.

### 5.1 Three alternatives

Halbrook oversees three hundred suppliers using one long questionnaire for all. Daniel designs alternatives. The first keeps the questionnaire but adds follow-up interviews for key suppliers. The second introduces tiering: suppliers are classified by data access, criticality and connectivity, with deep reviews for high tiers relying on SOC 2 type two reports or ISO/IEC 27001:2022 certificates plus targeted questions, and light reviews for others. The third buys an external rating service. Each alternative must be judged against the same criteria, which the next section sets out.

### 5.2 Comparison

Daniel compares alternatives on criteria agreed with procurement and security: depth of assurance for critical suppliers, review time, burden on suppliers, cost and fit with regulatory expectations for outsourcing. The interview option adds depth but increases time. The rating service is fast but gives outside-in views that miss internal controls. Tiering concentrates effort where it matters and reuses existing assurance reports. He records scores and reasoning in a table that colleagues can challenge. Dr. Varga points out that a written score table also lets procurement see why the interview option lost despite its depth.

### 5.3 Selection

The committee selects tiering for a controlled evaluation before full rollout. Daniel notes that the rating service could complement tiering by flagging changes between reviews, and records it as a possible later addition. He also defines what success would mean: faster reviews without losing depth for critical suppliers. He learns that selecting an approach for evaluation, rather than declaring it the answer, keeps the organisation open to evidence and reduces the cost of being wrong. The success definition is set before the trial so the results cannot be reinterpreted afterwards to favour tiering.

### Worked example

Daniel designs three supplier oversight alternatives, compares them on five criteria and selects tiering for evaluation.

> **Synthetic case.** Alternatives and scores are synthetic; SOC 2 and ISO/IEC 27001:2022 are real.

### Errors and limits

Criteria weights are subjective. Rating services vary in quality.

### Exercises

- **EX021 — Current approach.** How does Halbrook currently oversee suppliers? *Rubric:* 3 = one long questionnaire for all three hundred;; 2 = questionnaire;; 1 = vague;; 0 = none.
- **EX022 — Tiering evidence.** What evidence do deep reviews rely on? *Rubric:* 3 = SOC 2 type two reports or ISO/IEC 27001:2022 certificates plus targeted questions;; 2 = assurance reports;; 1 = vague;; 0 = none.
- **EX023 — Rating limit.** What is the limitation of the rating service? *Rubric:* 3 = outside-in views miss internal controls;; 2 = outside-in;; 1 = vague;; 0 = none.
- **EX024 — Success definition.** How is success defined for tiering? *Rubric:* 3 = faster reviews without losing depth for critical suppliers;; 2 = criteria;; 1 = vague;; 0 = none.
- **EX025 — Evaluate first.** Why evaluate before full rollout? *Rubric:* 3 = keeps the organisation open to evidence and reduces cost of error;; 2 = evidence;; 1 = vague;; 0 = none.

### Synthesis

Designing alternatives and evaluating the chosen one guards against expensive mistakes.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Security governance, risk and compliance: controlled evaluation

### Learning outcomes

You will (1) design a controlled comparison of governance processes; (2) test a difference with a permutation test; (3) check depth as well as speed.

### 6.1 Design

Daniel evaluates tiering on twenty upcoming supplier reviews. With the committee's agreement, ten are randomly assigned to the old questionnaire and ten to the tiered process. Random assignment makes the groups comparable on average, avoiding the risk that easier suppliers end up in one group. The outcome is days from request to completed review. To check depth, an independent reviewer from internal audit scores each completed review for whether it identified the key risks of that supplier. Blinding the auditor to which process produced each review prevents expectations about tiering from colouring the depth scores.

### 6.2 Speed

The lab compares mean days. The old process averaged thirty-nine point three days and the tiered process twenty-six point five, a difference of twelve point eight days. A permutation test reshuffles the twenty results five thousand times to see how often chance alone produces a difference this large. The one-sided p-value is about two in ten thousand, so chance is an unlikely explanation. Daniel reports the difference with the caution that ten reviews per group is a small sample. With only twenty reviews, one unusually slow supplier could move a group mean by several days, so the depth check in the next section matters.

### Lab — Permutation test on review duration

```python
"""Permutation test: days to complete supplier reviews, old vs tiered process (synthetic)."""
import random
random.seed(5)
old = [34, 41, 29, 52, 38, 45, 31, 47, 40, 36]
new = [22, 30, 19, 35, 27, 24, 33, 21, 28, 26]
obs = sum(old)/10 - sum(new)/10
pool = old + new; hits = 0
for _ in range(5000):
    random.shuffle(pool)
    if sum(pool[:10])/10 - sum(pool[10:])/10 >= obs: hits += 1
print(f"mean old {sum(old)/10:.1f} days; tiered {sum(new)/10:.1f} days; difference {obs:.1f}")
print(f"one-sided permutation p = {hits/5000:.4f}")
```

Run with `python3 lab_perm.py`. Verified output:

```text
mean old 39.3 days; tiered 26.5 days; difference 12.8
one-sided permutation p = 0.0002
```

### 6.3 Depth

Speed alone would be misleading if reviews became shallower. The internal auditor, not told which process was used, scores depth. Both groups identified the key risks in most reviews, and the tiered group performed slightly better on high-tier suppliers because reviewers read SOC 2 exceptions rather than skimming questionnaires. Daniel concludes that tiering was faster without loss of depth in this sample. He recommends rollout with continued monitoring of depth scores during the first year. Monitoring depth scores during rollout guards against reviewers drifting into shallow reviews once speed becomes the visible target.

### Worked example

Daniel randomises twenty reviews, finds tiering 12.8 days faster with permutation p of 0.0002 and confirms depth with blinded scoring.

> **Synthetic case.** Review data are synthetic.

### Errors and limits

Small samples. Blinding may be imperfect if reviewers recognise formats.

### Exercises

- **EX026 — Random assignment.** Why were reviews randomly assigned? *Rubric:* 3 = to make groups comparable on average;; 2 = comparability;; 1 = vague;; 0 = none.
- **EX027 — Mean durations.** What were the mean durations? *Rubric:* 3 = old 39.3 days, tiered 26.5 days;; 2 = 12.8 difference;; 1 = vague;; 0 = none.
- **EX028 — Permutation p.** What one-sided p-value did the permutation test give? *Rubric:* 3 = about 0.0002;; 2 = 0.0002;; 1 = 0.05;; 0 = none.
- **EX029 — Blind scoring.** Why was the auditor not told which process was used? *Rubric:* 3 = to avoid bias in depth scores;; 2 = blinding;; 1 = vague;; 0 = none.
- **EX030 — Depth result.** Did tiering lose depth? *Rubric:* 3 = no, slightly better on high-tier suppliers;; 2 = no;; 1 = yes;; 0 = none.

### Synthesis

Controlled evaluation with blinded depth checks shows whether faster processes stay thorough.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Security governance, risk and compliance: organizational integration

### Learning outcomes

You will (1) integrate supplier tiering into procurement and risk; (2) align three lines of responsibility; (3) manage change across departments.

### 7.1 Procurement integration

Daniel works with procurement to embed tiering in the purchasing process. A short intake form now asks about data access, criticality and connectivity before any contract. The answers set the tier automatically, and high-tier suppliers cannot be approved without a completed security review. He learns that integration works when governance steps sit inside existing workflows, at the point where decisions are made, rather than in a separate process that staff must remember to start. Because the tier is set at intake, a high-tier supplier can no longer reach contract signature without the security review having started.

### 7.2 Lines of responsibility

Halbrook uses a model in which business units own and manage risk, a risk and compliance function oversees and challenges, and internal audit provides independent assurance. Daniel clarifies each line's role in supplier risk: procurement and business owners manage, his team sets methods and challenges, and internal audit tests the process annually. He learns that confusion between lines, such as the risk team performing reviews it should challenge, weakens assurance and blurs accountability. Before the change, his team had run some supplier reviews itself, which left no one independent to challenge them.

### 7.3 Managing change

Some business units resist tiering because high-tier reviews delay contracts. Daniel meets them, explains the reasons and offers early engagement so reviews start before contracts are urgent. He also publishes review times so units can plan. Resistance falls. He learns that change succeeds when people see the reasons, receive practical help and have their legitimate concerns, such as deadlines, addressed rather than dismissed as obstruction. Publishing the review times also gives his team a measure that business units can hold it to, which builds trust in the new process.

### Worked example

Daniel embeds tiering in procurement, clarifies three lines of responsibility and reduces resistance through early engagement and published timings.

> **Synthetic case.** Processes are synthetic.

### Errors and limits

Intake forms can be gamed. Lines models vary across organisations.

### Exercises

- **EX031 — Intake gate.** What prevents high-tier suppliers being approved without review? *Rubric:* 3 = the procurement intake sets tier and blocks approval;; 2 = gate;; 1 = vague;; 0 = none.
- **EX032 — First line.** Who manages supplier risk in the first line? *Rubric:* 3 = procurement and business owners;; 2 = owners;; 1 = audit;; 0 = none.
- **EX033 — Line confusion.** What weakens assurance between lines? *Rubric:* 3 = the risk team performing reviews it should challenge;; 2 = confusion;; 1 = vague;; 0 = none.
- **EX034 — Resistance cause.** Why did some units resist tiering? *Rubric:* 3 = high-tier reviews delayed contracts;; 2 = delay;; 1 = vague;; 0 = none.
- **EX035 — Resistance fix.** How was resistance reduced? *Rubric:* 3 = early engagement and published review times;; 2 = engagement;; 1 = vague;; 0 = none.

### Synthesis

Integration places governance steps inside workflows and respects clear lines of responsibility.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security governance, risk and compliance: difficult cases

### Learning outcomes

You will (1) handle conflicts between compliance and risk; (2) decide under incomplete evidence; (3) escalate appropriately.

### 8.1 A critical supplier fails

A high-tier claims supplier's SOC 2 type two report shows exceptions: access reviews were not performed for two quarters. The supplier is critical, and replacing it would take a year. Daniel must recommend what to do. He considers options: accept with compensating controls, require a remediation plan with milestones, increase monitoring or start an exit plan. He recommends a remediation plan, extra monitoring of the supplier's access to Halbrook data and a parallel exit assessment. The parallel exit assessment keeps Halbrook from being trapped if the remediation milestones slip.

### 8.2 Incomplete evidence

A new cloud provider for fraud analytics offers only a recent ISO/IEC 27001:2022 certificate, whose scope does not clearly include the analytics service. Daniel cannot confirm controls directly. He recommends a limited pilot with synthetic data, contractual rights to audit and a request for a scope statement. He learns that difficult cases rarely offer complete evidence, and that good practice is to limit exposure while evidence is gathered rather than choose between blind trust and refusal. The synthetic-data pilot lets fraud analysts test the service while no policyholder data is exposed to unconfirmed controls.

### 8.3 Escalation

A business director wants to proceed with the analytics provider using real policyholder data before the scope statement arrives. Daniel escalates to the chief risk officer with a short memo: the decision needed, the options, the risk and his recommendation. The chief risk officer supports the pilot with synthetic data only. Daniel learns that escalation is a normal governance tool, and that a clear memo makes it a decision process rather than a personal dispute. The memo also leaves a record showing that the director's request and the risk reasoning were both considered.

### Worked example

Daniel handles SOC 2 exceptions at a critical supplier, limits exposure to an uncertain provider and escalates a data decision with a clear memo.

> **Synthetic case.** Suppliers and decisions are synthetic; SOC 2 and ISO/IEC 27001:2022 are real.

### Errors and limits

Compensating controls can mask risk. Escalation can strain relationships.

### Exercises

- **EX036 — SOC 2 exception.** What exception did the supplier's report show? *Rubric:* 3 = access reviews not performed for two quarters;; 2 = access review;; 1 = vague;; 0 = none.
- **EX037 — Critical supplier plan.** What did Daniel recommend for the critical supplier? *Rubric:* 3 = remediation plan, extra monitoring and parallel exit assessment;; 2 = three;; 1 = replace immediately;; 0 = none.
- **EX038 — Scope doubt.** Why was the provider's certificate insufficient? *Rubric:* 3 = its scope did not clearly include the analytics service;; 2 = scope;; 1 = vague;; 0 = none.
- **EX039 — Limited exposure.** How did Daniel limit exposure while gathering evidence? *Rubric:* 3 = pilot with synthetic data and audit rights;; 2 = pilot;; 1 = vague;; 0 = none.
- **EX040 — Escalation memo.** What did Daniel's escalation memo contain? *Rubric:* 3 = decision needed, options, risk and recommendation;; 2 = memo;; 1 = vague;; 0 = none.

### Synthesis

Difficult cases call for limiting exposure, reading assurance carefully and escalating clearly.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Security governance, risk and compliance: leadership and assurance

### Learning outcomes

You will (1) express risk appetite in quantitative terms; (2) compare risk estimates with appetite; (3) lead assurance conversations with the board.

### 9.1 Quantified appetite

Halbrook's board has a qualitative appetite statement: low tolerance for cyber risk. Daniel helps translate it into exceedance limits: the probability of annual cyber losses exceeding given amounts should not exceed agreed thresholds, for example no more than a five percent chance of exceeding one million in a year. He learns that quantified appetite makes risk discussions concrete and lets the board compare cyber risk with its tolerances for other financial risks. The five percent limit at one million becomes the benchmark against which the combined curve is tested in the next section.

### 9.2 Comparing with appetite

Daniel's team estimates a loss exceedance curve for all cyber scenarios combined. The lab compares five points with the appetite. Estimates are within appetite at two hundred and fifty thousand and five hundred thousand, but exceed it at one million, two million and five million: for example, an eight percent chance of exceeding one million against an appetite of five percent. The tail, not the typical year, breaches appetite. He recommends treatments aimed at severe scenarios. Treatments such as backup isolation shrink the tail without changing much in ordinary years.

### Lab — Loss exceedance estimates against board appetite

```python
"""Compare loss exceedance points with board appetite (synthetic, thousands)."""
lec = {250: 0.42, 500: 0.21, 1000: 0.08, 2000: 0.02, 5000: 0.004}
appetite = {250: 0.50, 500: 0.25, 1000: 0.05, 2000: 0.01, 5000: 0.002}
for x in lec:
    s = "within" if lec[x] <= appetite[x] else "EXCEEDS"
    print(f"P(loss > {x}k): estimate {lec[x]:.3f} appetite {appetite[x]:.3f} {s}")
```

Run with `python3 lab_appetite.py`. Verified output:

```text
P(loss > 250k): estimate 0.420 appetite 0.500 within
P(loss > 500k): estimate 0.210 appetite 0.250 within
P(loss > 1000k): estimate 0.080 appetite 0.050 EXCEEDS
P(loss > 2000k): estimate 0.020 appetite 0.010 EXCEEDS
P(loss > 5000k): estimate 0.004 appetite 0.002 EXCEEDS
```

### 9.3 Board assurance

Daniel presents the comparison to the board with the uncertainty behind the curve and the treatments proposed: improved backup isolation and an insurance review. A director asks whether the estimates can be trusted. He explains how the inputs were gathered, that internal audit reviewed the method and that results are ranges. The board approves the treatments and asks for an update in six months. He learns that board assurance depends on transparency about methods as much as on the numbers. Dr. Varga notes that the six-month update gives the board a way to see whether the treatments actually moved the tail.

### Worked example

Daniel translates appetite into exceedance limits, finds the tail exceeding appetite at three points and leads a transparent board discussion.

> **Synthetic case.** Curves and appetite are synthetic.

### Errors and limits

Combined curves depend on correlation assumptions. Appetite thresholds are judgements.

### Exercises

- **EX041 — Appetite example.** Give the example exceedance limit. *Rubric:* 3 = no more than 5% chance of exceeding 1 million;; 2 = 5% at 1m;; 1 = vague;; 0 = none.
- **EX042 — Within appetite.** At which points is the estimate within appetite? *Rubric:* 3 = 250k and 500k;; 2 = two;; 1 = vague;; 0 = none.
- **EX043 — One-million breach.** What is the estimate at one million versus appetite? *Rubric:* 3 = 8% versus 5%;; 2 = exceeds;; 1 = vague;; 0 = none.
- **EX044 — Breach location.** Which part of the curve breaches appetite? *Rubric:* 3 = the tail;; 2 = tail, hedged with another option;; 1 = typical year;; 0 = none.
- **EX045 — Trust answer.** How did Daniel answer whether estimates could be trusted? *Rubric:* 3 = explained inputs, audit review and ranges;; 2 = transparency;; 1 = vague;; 0 = none.

### Synthesis

Quantified appetite lets boards see where severe risks breach tolerance and govern treatments.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read GRC research critically; (2) assess methods and claims; (3) relate findings to practice.

### 10.1 Reading strategy

Daniel reads four sources: Gordon and Loeb (2002) on security investment economics, Cox (2008) on risk matrices, Spears and Barki (2010) on user participation in security risk management and Hubbard and Seiersen (2016) on measurement. For each he records the question, method, data, main claim and limits. He learns that reading research for practice means asking not only whether a claim is true but whether it applies to his organisation's setting. Recording the same five fields for each source makes it easier to compare the analytical, survey and practice-based work that follows.

### 10.2 Assessing methods

Gordon and Loeb offer an analytical model with assumptions about vulnerability and loss functions; its insight that optimal investment is bounded is robust, but exact numbers depend on assumptions. Cox analyses mathematical properties of matrices; his conclusions are logical rather than empirical. Spears and Barki use survey data and interviews with managers; findings depend on context. Hubbard and Seiersen synthesise practice and research to argue for quantification. Daniel notes the different kinds of evidence each provides. A logical argument like Cox's can show that matrices mislead in principle, but it cannot say how often they misled Halbrook's own committee.

### 10.3 Relating to practice

Daniel relates each source to Halbrook. Gordon and Loeb support comparing investments with expected loss reduction. Cox supports moving away from matrices for board reporting. Spears and Barki support involving business owners in supplier risk decisions, which tiering did. Hubbard and Seiersen support calibration training for estimators. He writes a critique noting that none studied an insurer's supplier oversight directly, so his own evaluation adds local evidence. His tiering evaluation of twenty reviews is the local evidence that the published sources could not supply.

### Worked example

Daniel reads four sources, records method and limits, distinguishes analytical from empirical evidence and links each to Halbrook's practice.

> **Synthetic case.** The critique is synthetic; all four sources are real.

### Errors and limits

Summaries simplify sources. Settings differ from Halbrook's.

### Exercises

- **EX046 — Reading fields.** What does Daniel record for each source? *Rubric:* 3 = question, method, data, main claim, limits;; 2 = five;; 1 = vague;; 0 = none.
- **EX047 — Cox evidence.** What kind of evidence does Cox (2008) provide? *Rubric:* 3 = logical analysis of matrix properties;; 2 = analytical;; 1 = empirical;; 0 = none.
- **EX048 — Spears method.** What method do Spears and Barki (2010) use? *Rubric:* 3 = survey data and interviews with managers;; 2 = survey;; 1 = vague;; 0 = none.
- **EX049 — Gordon-Loeb practice.** How does Gordon and Loeb's work apply at Halbrook? *Rubric:* 3 = comparing investments with expected loss reduction;; 2 = investment;; 1 = vague;; 0 = none.
- **EX050 — Research gap.** What gap does Daniel's evaluation fill? *Rubric:* 3 = none studied insurer supplier oversight directly;; 2 = local evidence;; 1 = vague;; 0 = none.

### Synthesis

Critical reading separates kinds of evidence and checks whether findings fit the setting.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) deliver an applied GRC improvement; (2) measure results against objectives; (3) document for handover.

### 11.1 Project scope

Daniel's applied project brings together his work: quantified risk reporting for the board, supplier tiering and appetite in exceedance terms. Over six months he rolls out tiering to all three hundred suppliers, introduces loss exceedance reporting for the top ten cyber scenarios and trains six estimators in calibration. Objectives include halving average review time, completing deep reviews for all high-tier suppliers and presenting scenarios in financial terms at every board meeting. Each objective is measurable, so the results section can report it as met, partly met or missed.

### 11.2 Results

After six months, average review time fell from about thirty-nine to twenty-four days, close to the objective. All forty-two high-tier suppliers have completed deep reviews, revealing three with significant exceptions now under remediation. The board receives quantified scenarios each quarter and has approved two treatments. Calibration tests show estimators' ranges capturing true answers more often after training. Daniel reports one objective, halving review time, as nearly but not fully met. The three suppliers with significant exceptions show that deep reviews found problems the old questionnaires had missed.

### 11.3 Handover

Daniel documents methods, tools, estimator guidance and the tiering rules, and trains a colleague to run the process. He records known limitations: estimates depend on a small group of experts, and loss data are sparse. He recommends collecting internal incident cost data to improve future estimates. He learns that applied projects create lasting value only when others can continue them, and that honest reporting of partly met objectives builds credibility. Recording the reliance on a small expert group warns his successor where the estimates are most fragile.

### Worked example

Daniel rolls out tiering and quantified reporting, nearly halves review time, completes forty-two deep reviews and hands over with documented limits.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Six months is short. Calibration gains can fade.

### Exercises

- **EX051 — Review time result.** How did average review time change? *Rubric:* 3 = from about thirty-nine to twenty-four days;; 2 = nearly halved;; 1 = vague;; 0 = none.
- **EX052 — High-tier reviews.** How many high-tier suppliers completed deep reviews? *Rubric:* 3 = forty-two;; 2 = 42;; 1 = vague;; 0 = none.
- **EX053 — Exceptions found.** How many high-tier suppliers had significant exceptions? *Rubric:* 3 = three;; 2 = 3;; 1 = vague;; 0 = none.
- **EX054 — Partly met.** Which objective was only nearly met? *Rubric:* 3 = halving review time;; 2 = review time;; 1 = vague;; 0 = none.
- **EX055 — Data recommendation.** What data does Daniel recommend collecting? *Rubric:* 3 = internal incident cost data;; 2 = incident costs;; 1 = vague;; 0 = none.

### Synthesis

Applied projects succeed when results are measured honestly and work is handed over.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review your postgraduate learning critically; (2) transfer methods to new contexts; (3) plan continuing development.

### 12.1 Final review

Daniel presents his work to Dr. Varga and an external examiner from another insurer. He summarises the decisions, evidence and results and answers questions. The examiner asks whether quantification will survive his departure. Daniel points to the handover, the trained colleague and internal audit's review of the method. Dr. Varga asks what he would do differently; he answers that he would collect incident cost data from the start and involve brokers earlier. Both answers point to data and stakeholders he could have engaged earlier, not to flaws in the methods themselves.

### 12.2 Transfer

Daniel considers how his methods transfer. Tiering applies to any organisation with many suppliers. Loss exceedance reporting suits organisations with boards used to financial risk, such as banks or pension funds, but may need simplification for smaller charities. Calibration training applies wherever experts estimate uncertain quantities. He learns that methods transfer best when their assumptions are explicit, so new users can check whether those assumptions hold in their setting. For a small charity, for instance, a single tiering rule based on data access may be enough where Halbrook needed three criteria.

### 12.3 Continuing development

Daniel plans continuing development: deeper study of statistics for risk, following updates to NIST CSF and ISO standards and joining a professional community on risk quantification. He also commits to mentoring a junior colleague. Dr. Varga notes that GRC practice changes quickly and that his habits of critical reading, controlled evaluation and transparent reporting will remain useful as specific frameworks change. Dr. Varga also suggests he keep his calibration records, so he can later check whether his own estimates stay well calibrated.

### Worked example

Daniel defends his work, explains how methods transfer with explicit assumptions and plans continuing development.

> **Synthetic case.** The review is synthetic.

### Errors and limits

Self-review can be generous. Transfer needs local testing.

### Exercises

- **EX056 — Survival answer.** How did Daniel show quantification would survive his departure? *Rubric:* 3 = handover, trained colleague and audit review;; 2 = continuity;; 1 = vague;; 0 = none.
- **EX057 — Do differently.** What would Daniel do differently? *Rubric:* 3 = collect incident cost data from the start and involve brokers earlier;; 2 = hindsight;; 1 = vague;; 0 = none.
- **EX058 — Transfer condition.** When do methods transfer best? *Rubric:* 3 = when assumptions are explicit;; 2 = assumptions;; 1 = vague;; 0 = none.
- **EX059 — Smaller charities.** What adjustment might loss exceedance reporting need for small charities? *Rubric:* 3 = simplification;; 2 = simpler;; 1 = vague;; 0 = none.
- **EX060 — Lasting habits.** Which habits will remain useful as frameworks change? *Rubric:* 3 = critical reading, controlled evaluation, transparent reporting;; 2 = habits;; 1 = vague;; 0 = none.

### Synthesis

Final review consolidates learning and prepares methods for transfer to new contexts.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Daniel Mensah, Dr. Elena Varga, Wexford School of Management, Halbrook Mutual and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** By whether the choice made sense given the information, values and time available.

**EX002.** Because nothing going wrong was luck; the decision itself lacked risk estimation and recording.

**EX003.** It makes them too narrow.

**EX004.** Hubbard and Seiersen (2016).

**EX005.** Recording assumptions and asking for ranges instead of single numbers.

**EX006.** NIST CSF 2.0 functions.

**EX007.** Because matrix scores are hard to compare with financial risks.

**EX008.** It relies on questionnaires that take weeks and are rarely read in depth.

**EX009.** Because adopting a method without supporting data or skills can make governance worse.

**EX010.** Because each framework answers a different question.

**EX011.** Loss event frequency and loss magnitude.

**EX012.** About 170 thousand.

**EX013.** 68%.

**EX014.** About 4.1%, roughly one year in twenty-five.

**EX015.** Translating it into familiar terms and showing uncertainty openly.

**EX016.** By choosing optimistic or pessimistic inputs to justify cutting or increasing spending.

**EX017.** People affected by risks, such as policyholders.

**EX018.** Internal audit review of estimates, declaring the conflict and having others make budget decisions.

**EX019.** Because notification duties come from law and narrowing them would harm policyholders.

**EX020.** As a minimum rather than the full measure of ethical conduct.

**EX021.** With one long questionnaire for all three hundred suppliers.

**EX022.** SOC 2 type two reports or ISO/IEC 27001:2022 certificates, plus targeted questions.

**EX023.** It gives outside-in views that miss internal controls.

**EX024.** Faster reviews without losing depth for critical suppliers.

**EX025.** Because it keeps decisions open to evidence and reduces the cost of being wrong.

**EX026.** To make the groups comparable on average, so easier suppliers do not cluster in one group.

**EX027.** 39.3 days for the old process and 26.5 days for tiering.

**EX028.** About 0.0002.

**EX029.** To avoid bias in scoring the depth of each review.

**EX030.** No; it was slightly better on high-tier suppliers in this sample.

**EX031.** The intake form sets the tier and approval is blocked until the security review is complete.

**EX032.** Procurement and business owners.

**EX033.** Confusion such as the risk team performing reviews it should independently challenge.

**EX034.** Because high-tier reviews delayed their contracts.

**EX035.** Through early engagement and publishing review times so units could plan.

**EX036.** Access reviews were not performed for two quarters.

**EX037.** A remediation plan with milestones, extra monitoring and a parallel exit assessment.

**EX038.** Its scope did not clearly include the analytics service.

**EX039.** A limited pilot with synthetic data, audit rights and a request for a scope statement.

**EX040.** The decision needed, the options, the risk and his recommendation.

**EX041.** No more than a 5% chance of annual cyber losses exceeding one million.

**EX042.** At 250 thousand and 500 thousand.

**EX043.** An estimated 8% chance against an appetite of 5%.

**EX044.** The tail, covering severe losses.

**EX045.** By explaining how inputs were gathered, that internal audit reviewed the method and that results are ranges.

**EX046.** The question, method, data, main claim and limits.

**EX047.** Logical, mathematical analysis of risk matrix properties.

**EX048.** Survey data and interviews with managers.

**EX049.** It supports comparing security investments with expected loss reduction.

**EX050.** None of the sources studied an insurer's supplier oversight directly.

**EX051.** From about thirty-nine to twenty-four days.

**EX052.** All forty-two.

**EX053.** Three, now under remediation.

**EX054.** Halving average review time.

**EX055.** Internal incident cost data to improve future estimates.

**EX056.** By pointing to the handover, the trained colleague and internal audit's review of the method.

**EX057.** Collect incident cost data from the start and involve brokers earlier.

**EX058.** When their assumptions are explicit so new users can check them.

**EX059.** Simplification.

**EX060.** Critical reading, controlled evaluation and transparent reporting.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- Cox, L. A., Jr. (2008). What's wrong with risk matrices? *Risk Analysis*, 28(2), 497–512. <https://doi.org/10.1111/j.1539-6924.2008.01030.x>
- Freund, J., & Jones, J. (2015). *Measuring and managing information risk: A FAIR approach*. Butterworth-Heinemann. <https://doi.org/10.1016/C2013-0-09966-5>
- Gordon, L. A., & Loeb, M. P. (2002). The economics of information security investment. *ACM Transactions on Information and System Security*, 5(4), 438–457. <https://doi.org/10.1145/581271.581274>
- Hubbard, D. W., & Seiersen, R. (2016). *How to measure anything in cybersecurity risk*. Wiley. <https://doi.org/10.1002/9781119162315>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- ISACA. (2018). *COBIT 2019 framework: Introduction and methodology*. ISACA. <https://www.isaca.org/resources/cobit>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Spears, J. L., & Barki, H. (2010). User participation in information systems security risk management. *MIS Quarterly*, 34(3), 503–522. <https://doi.org/10.2307/25750689>
