# Privacy and Data Protection: Postgraduate Course

- Language: English (`en`); course 142, Postgraduate course (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: postgraduate practitioners leading a privacy programme in a regulated, cross-border business.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs simulate fraud detection with different location detail, analyse a consent-banner A/B test and compare privacy risk indicators with board thresholds, all on synthetic data. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one privacy manager through a postgraduate course: decision-making, current practice, evidence on necessity, risk and ethics, consent design alternatives, a controlled A/B evaluation, organisational integration, difficult cases, board indicators and assurance, research critique, an applied retention project and final review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Priscila Andrade** | Postgraduate student and privacy manager | Invented |
| **Dr. Helen Ward** | Tutor | Invented |
| **Ashgrove School of Management** | Fictional school | Invented |
| **Corvina Pay** | Fictional payments company, 900 staff, Brazil and Portugal | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR); Lei 13.709/2018 (LGPD); Directive 2002/58/EC (ePrivacy) Article 5(3); EDPB Guidelines 05/2020, 07/2020 and 9/2022; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 27701:2025; Acquisti et al. (2015), [doi:10.1126/science.aaa1465](https://doi.org/10.1126/science.aaa1465); Sweeney (2002); Narayanan and Shmatikov (2008); Dwork and Roth (2014); Solove (2006); Nissenbaum (2004). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame privacy decisions as choices under uncertainty; (2) separate legal constraints from risk trade-offs; (3) document decisions for accountability.

### 1.1 The practitioner and the firm

Priscila Andrade is the privacy manager at the fictional Corvina Pay, a payments company with 900 staff serving customers in Brazil and Portugal. She enrols in a two-year postgraduate course at the fictional Ashgrove School of Management, tutored by Dr. Helen Ward. Corvina must comply with the LGPD in Brazil and the GDPR in Portugal. Priscila's daily work involves decisions about fraud models, marketing consent, vendors and data requests, often made quickly and with incomplete information about risks and benefits. Most arrive as urgent product requests.

### 1.2 Decisions under uncertainty

Dr. Ward asks Priscila to describe a recent decision. The fraud team wanted precise GPS location for every card payment. Priscila did not know how much GPS would improve detection, how customers would react or how regulators would view it. She learns to frame such decisions with options, outcomes, probabilities and values, even if estimates are rough. Writing down the uncertainty makes it possible to reduce it, for instance by testing whether coarser data perform as well before collecting precise location from everyone.

### 1.3 Constraints versus trade-offs

Priscila separates constraints from trade-offs. Constraints are requirements that cannot be traded away, such as having a lawful basis under GDPR Article 6 or LGPD Article 7, and respecting necessity. Trade-offs are choices among lawful options, such as how much data to collect for fraud prevention. She notes that managers often treat legal requirements as costs to be weighed, which is a category error. Clarifying the difference early prevents wasted debate and focuses discussion on the genuine choices that remain. The 72-hour breach deadline is a constraint; how much location detail to keep is a trade-off.

### 1.4 Recording decisions

Priscila introduces a decision record at Corvina: the question, options considered, evidence, legal constraints, chosen option, residual risk and owner. She uses it for the GPS decision. Accountability under GDPR Article 5(2) and LGPD Article 6(X) requires demonstrating compliance, and decision records are strong evidence. Dr. Ward notes that records also improve future decisions, because the organisation can look back at what it expected and what actually happened, and learn from the difference. Her template has five fields: the question, options considered, evidence used, decision and owner, plus a date for checking the expected outcome.

### Worked example

Priscila frames the GPS request as a decision under uncertainty, separates lawful-basis constraints from collection trade-offs and introduces a decision record.

> **Synthetic case.** Corvina, Ashgrove and all people are synthetic; GDPR Articles 5(2) and 6 and LGPD Articles 6 and 7 are real.

### Errors and limits

Rough probabilities can create false precision; show ranges.

### Exercises

- **EX001 — Constraint or trade-off.** Is having a lawful basis a trade-off or a constraint? *Rubric:* 3 = a constraint that cannot be traded away;; 2 = constraint without reason;; 1 = trade-off;; 0 = none.
- **EX002 — Reducing uncertainty.** How could Corvina reduce uncertainty about GPS value? *Rubric:* 3 = test whether coarser data perform as well before collecting precise location;; 2 = mentions testing;; 1 = collect anyway;; 0 = none.
- **EX003 — Decision record fields.** List the fields of Priscila's decision record. *Rubric:* 3 = question, options, evidence, constraints, choice, residual risk, owner;; 2 = most;; 1 = few;; 0 = none.
- **EX004 — Learning from records.** How do decision records improve future decisions? *Rubric:* 3 = comparing expectations with outcomes teaches the organisation;; 2 = mentions learning;; 1 = compliance only;; 0 = none.
- **EX005 — Two laws.** Which laws govern Corvina's processing and where? *Rubric:* 3 = LGPD in Brazil, GDPR in Portugal;; 2 = one;; 1 = wrong;; 0 = none.

### Synthesis

Chapter 1 frames decisions. Chapter 2 surveys current practice.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Privacy and data protection: current practice

### Learning outcomes

You will (1) map current privacy practice in a payments company; (2) compare GDPR and LGPD obligations; (3) identify gaps against good practice.

### 2.1 Mapping practice

Priscila maps Corvina's privacy programme: a data protection officer (called encarregado under the LGPD), a record of processing, a DPIA process, a rights request team, vendor contracts and training. She interviews team leads to see how each works in practice. She finds that the record of processing exists but has not been updated for a year, and that DPIAs are done only for new products, not for changes to existing ones like the fraud model. She also finds two vendors missing from the record of processing.

### 2.2 Comparing laws

Priscila builds a comparison of obligations under the GDPR and LGPD. Both require lawful bases, transparency, security and rights handling. The LGPD lists ten legal bases in Article 7, including credit protection, which is relevant to Corvina. The GDPR uses six bases in Article 6. Breach notification under the GDPR has a 72-hour target; the LGPD requires communication within a reasonable time, as defined by the national authority. She designs processes that meet the stricter requirement in each area. Where rules diverge, the stricter one becomes the group standard.

### 2.3 Frameworks

Priscila compares Corvina's programme with the NIST Privacy Framework 1.0 and ISO/IEC 27701:2025. The NIST framework's functions help her see that Corvina is strong on Protect-P but weaker on Identify-P, because the inventory is stale. ISO/IEC 27701 expects documented management system processes, which Corvina partly has. She uses the frameworks as a structured checklist rather than as certification targets, at least for now. The NIST Privacy Framework helps her describe target outcomes for the board, while ISO/IEC 27701 control lists help her check whether supplier management and training are covered in practice.

### 2.4 Gaps

Priscila lists gaps: a stale record of processing, DPIAs not triggered by changes, vendor contracts without clear deletion terms, and training that is generic. She ranks them by risk. The stale inventory is first because other processes depend on it. She presents the gap list to Corvina's executive committee with a twelve-month plan. Dr. Ward comments that a credible gap list is specific, ranked and owned, rather than a long list of everything that could be better. Her top gap is unreviewed product changes, owned by the product director.

### Worked example

Priscila maps Corvina's programme, compares GDPR and LGPD obligations, uses NIST Privacy Framework and ISO/IEC 27701 as checklists and ranks four gaps with a twelve-month plan.

> **Synthetic case.** Corvina's programme is synthetic; GDPR Article 6, LGPD Article 7, the NIST Privacy Framework 1.0 and ISO/IEC 27701:2025 are real.

### Errors and limits

Comparisons of laws simplify; national authority regulations add detail.

### Exercises

- **EX006 — DPIA trigger gap.** What gap did Priscila find in DPIA practice? *Rubric:* 3 = DPIAs only for new products, not changes;; 2 = mentions changes;; 1 = none;; 0 = none.
- **EX007 — LGPD bases.** How many legal bases does LGPD Article 7 list, and which suits payments? *Rubric:* 3 = ten; credit protection is relevant;; 2 = number only;; 1 = wrong;; 0 = none.
- **EX008 — Stricter requirement.** How does Priscila handle differences between the laws? *Rubric:* 3 = designs processes meeting the stricter requirement;; 2 = mentions stricter;; 1 = picks one;; 0 = none.
- **EX009 — Framework role.** How does Priscila use the frameworks? *Rubric:* 3 = as structured checklists, not certification targets;; 2 = mentions checklist;; 1 = certify;; 0 = none.
- **EX010 — First gap.** Why is the stale inventory ranked first? *Rubric:* 3 = other processes depend on it;; 2 = mentions dependency;; 1 = random;; 0 = none.

### Synthesis

Chapter 2 maps practice. Chapter 3 gathers specialist evidence.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Privacy and data protection: specialist evidence

### Learning outcomes

You will (1) test whether data are necessary with evidence; (2) compare model performance with less data; (3) apply evidence to a minimisation decision.

### 3.1 The necessity question

Data minimisation requires that data be adequate, relevant and limited to what is necessary, under GDPR Article 5(1)(c) and the necessity principle in LGPD Article 6(III). The fraud team argues that precise GPS is necessary. Priscila asks for evidence. Together with a data scientist she designs a simulation on 20,000 synthetic transactions comparing three rules: full GPS with device novelty, city-level location with device novelty, and device novelty alone. The aim is to measure what precise location adds. All three rules run on the same synthetic transaction history so the comparison is fair.

### 3.2 Results

The lab shows that full GPS with device and city-level location with device detect the same 43.1% of fraud with the same 90 false alarms. In this synthetic setting GPS adds nothing beyond knowing that a payment comes from an unusual city. Using device novelty alone detects more fraud, 56.4%, but produces 1,572 false alarms, which would block many legitimate customers. City-level location therefore provides the useful signal without precise tracking. Device novelty alone catches more fraud only by flagging huge numbers of customers. The lab output shows that keeping exact coordinates adds no detection over city-level location, so precise tracking cannot be called necessary.

### 3.3 Interpreting evidence

Priscila is careful. The simulation is synthetic and built on assumptions the fraud team agreed. It shows that GPS may be unnecessary, not that it never helps. She proposes a controlled pilot with real but pseudonymised data in the fraud team's secure environment, comparing city-level and GPS rules for three months. Until results are available, Corvina uses city-level location. She records this as a decision taken under the necessity principle, with the evidence and the plan. The plan includes a review after six months.

### 3.4 Evidence culture

Dr. Ward points out that Priscila changed the conversation from opinion to evidence. The fraud team, initially resistant, accepts the pilot because it might prove them right. Priscila notes that necessity arguments are stronger when backed by data, and that privacy teams gain credibility when they help test claims rather than simply reject them. She plans to use the same approach for other data-hungry requests. The fraud team now proposes its own tests before asking for new data, and the next request, for contact-list access, is withdrawn after a small trial shows no benefit.

### Lab — Fraud detection with full GPS, city-level location or device only

```python
# Does a fraud rule need precise location? Compare detection with full GPS, city-level and no location (synthetic).
import random
r = random.Random(21)
tx = []
for _ in range(20000):
    fraud = r.random() < 0.01
    far = r.random() < (0.70 if fraud else 0.05)          # far from usual city
    newdev = r.random() < (0.60 if fraud else 0.08)       # new device
    odd_gps = far and r.random() < 0.5                    # GPS adds detail only within 'far' cases
    tx.append((fraud, far, newdev, odd_gps))
def score(rule):
    flagged = [t for t in tx if rule(t)]; tp = sum(t[0] for t in flagged); fr = sum(t[0] for t in tx)
    return tp / fr, len(flagged) - tp
for name, rule in [("full GPS + device", lambda t: (t[1] and t[2]) or t[3] and t[2]),
                   ("city-level + device", lambda t: t[1] and t[2]),
                   ("device only", lambda t: t[2])]:
    rec, fp = score(rule); print(f"{name:20s} detects {rec:5.1%} of fraud; false alarms {fp:5d}")
```

Run with `python3 lab_fraud.py`. Verified output:

```text
full GPS + device    detects 43.1% of fraud; false alarms    90
city-level + device  detects 43.1% of fraud; false alarms    90
device only          detects 56.4% of fraud; false alarms  1572
```

### Worked example

Priscila shows that GPS and city-level rules both detect 43.1% of synthetic fraud with 90 false alarms, while device-only detection raises false alarms to 1,572, and adopts city-level location pending a pilot.

> **Synthetic case.** Transactions are synthetic; GDPR Article 5(1)(c) and LGPD Article 6 are real.

### Errors and limits

Synthetic data reflect assumptions; real pilots may show different results.

### Exercises

- **EX011 — GPS value.** What did precise GPS add in the simulation? *Rubric:* 3 = nothing beyond city-level: same 43.1% detection and 90 false alarms;; 2 = mentions no gain;; 1 = improved;; 0 = none.
- **EX012 — Device-only cost.** Why not use device novelty alone? *Rubric:* 3 = 1,572 false alarms would block many legitimate customers;; 2 = mentions false alarms;; 1 = best;; 0 = none.
- **EX013 — Interim decision.** What does Corvina use until the pilot ends? *Rubric:* 3 = city-level location;; 2 = mentions city;; 1 = GPS;; 0 = none.
- **EX014 — Necessity principle.** Which principles require limiting data to what is necessary? *Rubric:* 3 = GDPR Article 5(1)(c) and LGPD Article 6(III);; 2 = one;; 1 = none;; 0 = none.
- **EX015 — Resistant team.** Why did the fraud team accept the pilot? *Rubric:* 3 = it could prove them right;; 2 = mentions fairness;; 1 = forced;; 0 = none.

### Synthesis

Chapter 3 tests necessity. Chapter 4 addresses risk and ethics.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) assess privacy risk for individuals, not only the company; (2) apply ethical analysis to profiling; (3) handle conflicts of interest.

### 4.1 Risk to whom

Corporate risk registers measure risk to the company: fines, reputation, costs. Priscila notes that data protection law focuses on risks to people's rights and freedoms. A data breach exposing transaction histories could reveal health purchases, religious donations or gambling, causing harm to customers even if Corvina's losses are small. She adds a separate column to the risk register for harm to individuals, so that decisions consider both perspectives explicitly rather than letting company risk dominate. For the profiling proposal, company risk is moderate but harm to customers is high.

### 4.2 Profiling ethics

Corvina's marketing team proposes using transaction data to infer life events, such as pregnancy or job loss, to offer financial products. Priscila analyses it with contextual integrity: customers share transaction data to make payments, not to have intimate life events inferred. Solove's taxonomy names this as secondary use and aggregation. She also notes GDPR Article 21's right to object to direct marketing and the transparency duties. She recommends against inferring sensitive events and proposes opt-in offers instead. Opt-in offers respect customer choice.

### 4.3 Conflicts of interest

The data protection officer reports to the chief operating officer, who is also responsible for marketing revenue. Priscila notes the risk of a conflict, since GDPR Article 38(6) requires that other tasks of the DPO do not result in a conflict of interests. She recommends that the DPO report to the board's risk committee for privacy matters. The executive committee agrees after discussion. Dr. Ward notes that governance structures shape outcomes as much as individual decisions do. The privacy lead now reports directly to the audit committee.

### 4.4 Ethical reasoning

Priscila writes an ethics note for Corvina: consider harm to individuals, respect contexts in which data were shared, prefer transparency and choice, and avoid inferences that customers would find intrusive. She tests the note on three past decisions and finds that one, a marketing segmentation by spending category, would have been designed differently. She revises it with the marketing team to use coarser categories and opt-in personalisation. For example, a category such as pharmacy spending becomes general retail, so the model no longer hints at health conditions while still allowing useful segmentation for offers.

### Worked example

Priscila adds individual harm to the risk register, advises against inferring life events from transactions, moves the DPO's reporting line to avoid a conflict and writes an ethics note applied to past decisions.

> **Synthetic case.** Proposals are synthetic; Solove (2006), Nissenbaum (2004) and GDPR Articles 21 and 38(6) are real.

### Errors and limits

Ethics notes need examples to be usable; abstract principles are easily ignored.

### Exercises

- **EX016 — Two risk views.** Why add a column for harm to individuals? *Rubric:* 3 = law focuses on people's rights, not only company losses;; 2 = mentions people;; 1 = company only;; 0 = none.
- **EX017 — Life-event inference.** Why advise against inferring life events from transactions? *Rubric:* 3 = breaks contextual norms and amounts to secondary use;; 2 = mentions intrusion;; 1 = support;; 0 = none.
- **EX018 — DPO conflict.** What conflict did Priscila identify for the DPO? *Rubric:* 3 = reporting to an executive responsible for marketing revenue;; 2 = mentions reporting;; 1 = none;; 0 = none.
- **EX019 — Article 38(6).** What does GDPR Article 38(6) require? *Rubric:* 3 = DPO's other tasks must not cause a conflict of interests;; 2 = close;; 1 = wrong;; 0 = none.
- **EX020 — Revised segmentation.** How was the past segmentation decision revised? *Rubric:* 3 = coarser categories and opt-in personalisation;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Chapter 4 broadens risk and ethics. Chapter 5 compares design alternatives.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Privacy and data protection: design alternatives

### Learning outcomes

You will (1) generate alternatives for a consent interface; (2) evaluate alternatives against law and user behaviour; (3) choose an alternative for testing.

### 5.1 The consent problem

Corvina's app asks customers to accept marketing cookies and personalised offers. The current banner shows a large Accept button and a small link to settings. Article 5(3) of the ePrivacy Directive requires consent for non-essential cookies, and EDPB Guidelines 05/2020 say consent must be freely given and as easy to refuse as to give. Priscila suspects the design nudges customers. She sets out to design alternatives and test them properly. Design A shows a large Accept button and hides refusal behind a settings link, which EDPB Guidelines 05/2020 treat as a warning sign.

### 5.2 Alternatives

Priscila's team designs three alternatives: A, the current banner; B, a banner with Accept all and Reject all buttons of equal size and colour, plus settings; C, a layered choice with separate toggles for analytics and marketing, all off by default. She evaluates each against legal criteria and expected user experience. A likely fails the equal-ease criterion. B and C both appear compliant. C gives more granular choice but takes longer. She records each design's screenshots and criteria in the test plan so reviewers can see exactly what customers saw.

### 5.3 Behavioural insight

Acquisti, Brandimarte and Loewenstein (2015) describe how defaults and framing influence privacy choices. Priscila expects acceptance to fall under B and C, because the design no longer pushes acceptance. She notes that a fall in acceptance is not a failure: it means choices reflect customers' preferences more accurately. The marketing team worries about fewer consents. She argues that consents obtained by nudging are fragile, both legally and in customer trust. A consent that customers regret leads to withdrawals, complaints and possibly regulatory scrutiny, so a lower acceptance rate may be the more valuable result.

### 5.4 Choosing what to test

Priscila chooses to test A against B, because B is the minimal change likely to achieve compliance and is easy to implement. C will be considered later if B performs well. She defines outcomes: acceptance rate and withdrawals within ninety days as a measure of regret. She writes a test plan with sample sizes and an analysis method, so that the decision will rest on evidence rather than opinion. She chooses A against B because B is the simplest compliant design and C needs more engineering work.

### Worked example

Priscila designs three consent banners, judges the current one non-compliant on equal ease of refusal, explains why lower acceptance is acceptable and chooses an A/B test of the current banner against equal buttons.

> **Synthetic case.** Banners are synthetic; ePrivacy Directive Article 5(3), EDPB Guidelines 05/2020 and Acquisti et al. (2015) are real.

### Errors and limits

Banner tests measure behaviour, not understanding; add comprehension checks if possible.

### Exercises

- **EX021 — Banner A problem.** Why does banner A likely fail? *Rubric:* 3 = refusing is harder than accepting;; 2 = mentions ease;; 1 = compliant;; 0 = none.
- **EX022 — Lower acceptance.** Why is a fall in acceptance not a failure? *Rubric:* 3 = choices reflect real preferences; nudged consents are fragile;; 2 = mentions preferences;; 1 = is failure;; 0 = none.
- **EX023 — Why test B.** Why test B rather than C first? *Rubric:* 3 = minimal change likely compliant and easy to implement;; 2 = mentions simplicity;; 1 = random;; 0 = none.
- **EX024 — Regret measure.** What outcome measures regret? *Rubric:* 3 = withdrawals within ninety days;; 2 = mentions withdrawals;; 1 = none;; 0 = none.
- **EX025 — Cookie consent law.** Which provision requires consent for non-essential cookies? *Rubric:* 3 = ePrivacy Directive Article 5(3);; 2 = mentions ePrivacy;; 1 = GDPR only;; 0 = none.

### Synthesis

Chapter 5 designs alternatives. Chapter 6 evaluates them in a controlled test.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Privacy and data protection: controlled evaluation

### Learning outcomes

You will (1) run an A/B test ethically; (2) estimate a difference in proportions; (3) interpret behavioural outcomes for compliance.

### 6.1 Running the test

Corvina randomly shows banner A or B to 8,000 new app users, 4,000 each, over two weeks. Priscila checks that the test itself is lawful: banner A is shown only during the test and both banners record choices correctly. She also limits analysis to aggregate choices. The test is approved by the data protection officer. She notes that testing a less compliant design should be brief and justified by the need to measure the improvement. The test runs for two weeks with random assignment.

### 6.2 Results

The lab computes results. Banner A has an acceptance rate of 79.0%; banner B, 57.0%. The difference is 22.0 percentage points, with a 95% interval from 20.0 to 24.0 points and a z statistic of 21.1. The difference is far beyond chance. Over ninety days, withdrawals per thousand consents are 41 under A and 12 under B. Customers who accepted under A were more than three times as likely to change their minds later. The confidence interval for the acceptance difference, 20.0 to 24.0 points, excludes zero, so the gap is not a chance result of this sample.

### 6.3 Interpretation

Priscila interprets the results. Banner A pushed about a fifth of users into accepting when an equal choice would not have. Higher withdrawals under A suggest that many of those consents did not reflect real preferences. From a compliance view, consents under A are questionable as freely given. From a business view, B produces fewer but more durable consents. She recommends adopting B immediately. The extra consents under A carry a legal and reputational cost that the acceptance rate alone hides from view.

### 6.4 Communicating results

Marketing leaders are disappointed by lower acceptance. Priscila presents the evidence: B is compliant, A probably is not, and B's consents are more stable. She also estimates that marketing reach falls less than acceptance suggests, because fewer people withdraw. Dr. Ward notes that controlled evaluation turns a values debate into an evidence-based decision, which is easier for leaders to accept even when the result is unwelcome. Her one-page summary shows the two acceptance rates, the two withdrawal rates and a single recommendation, with the confidence interval in a footnote for technical readers.

### Lab — Consent banner A/B test

```python
# Consent banner A/B test: A has "Accept" prominent; B gives "Reject all" equal prominence. Two-proportion z-test.
import math
na, ka, nb, kb = 4000, 3160, 4000, 2280
pa, pb = ka / na, kb / nb; p = (ka + kb) / (na + nb)
z = (pa - pb) / math.sqrt(p * (1 - p) * (1 / na + 1 / nb))
se = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
print(f"A accept rate {pa:.1%}; B accept rate {pb:.1%}; difference {pa-pb:.1%} (95% CI {pa-pb-1.96*se:.1%} to {pa-pb+1.96*se:.1%}); z = {z:.1f}")
wa, wb = 130, 27  # synthetic 90-day follow-up: withdrawals among consenting users
print(f"withdrawals within 90 days per 1,000 consents: A {1000*wa/ka:.0f} vs B {1000*wb/kb:.0f}")
```

Run with `python3 lab_ab.py`. Verified output:

```text
A accept rate 79.0%; B accept rate 57.0%; difference 22.0% (95% CI 20.0% to 24.0%); z = 21.1
withdrawals within 90 days per 1,000 consents: A 41 vs B 12
```

### Worked example

Priscila finds acceptance of 79.0% under banner A versus 57.0% under equal buttons (difference 22.0 points, 95% CI 20.0 to 24.0) and withdrawals of 41 versus 12 per 1,000, and recommends banner B.

> **Synthetic case.** Users and choices are synthetic.

### Errors and limits

Two weeks may not capture seasonal behaviour; repeat later.

### Exercises

- **EX026 — Acceptance difference.** What was the difference in acceptance between A and B? *Rubric:* 3 = 22.0 points (95% CI 20.0 to 24.0);; 2 = approximately;; 1 = wrong;; 0 = none.
- **EX027 — Withdrawal ratio.** How did withdrawals compare? *Rubric:* 3 = 41 vs 12 per 1,000, more than three times higher under A;; 2 = numbers only;; 1 = none;; 0 = none.
- **EX028 — Test ethics.** Why must showing banner A during the test be brief? *Rubric:* 3 = it is likely less compliant, justified only to measure improvement;; 2 = mentions compliance;; 1 = unlimited;; 0 = none.
- **EX029 — Durable consent.** What business benefit does banner B offer? *Rubric:* 3 = fewer but more durable consents;; 2 = mentions stability;; 1 = none;; 0 = none.
- **EX030 — Freely given doubt.** Why are consents under A questionable? *Rubric:* 3 = design pushed users, and higher withdrawals suggest choices did not reflect preferences;; 2 = mentions nudging;; 1 = valid;; 0 = none.

### Synthesis

Chapter 6 evaluates a design. Chapter 7 integrates privacy into the organisation.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Privacy and data protection: organizational integration

### Learning outcomes

You will (1) embed privacy in product and procurement processes; (2) align privacy with security and risk functions; (3) build a network of privacy champions.

### 7.1 Product process

Priscila integrates privacy into Corvina's product process. Each product change passes a short screening: does it collect new data, use data for a new purpose, involve a new vendor or affect many customers? A yes triggers a full DPIA. This closes the gap found in Chapter 2, where changes to existing products escaped review. In the first quarter, screening triggers three DPIAs, including one for changes to the fraud model. Screening uses six yes-or-no questions about new data, new purposes, new recipients and automation.

### 7.2 Procurement

Vendors receive personal data. Priscila adds privacy criteria to procurement: data processing agreements meeting GDPR Article 28 and LGPD requirements, deletion terms, sub-processor lists and breach notification times. EDPB Guidelines 07/2020 help her define when a vendor is a processor or a controller. Procurement now cannot sign contracts involving personal data without privacy review, which prevents gaps rather than finding them later. The review takes at most five working days, and a standard questionnaire covers security, subprocessors, transfers, retention and support for rights requests, so procurement staff know exactly what to collect before contacting the privacy team.

### 7.3 Alignment

Priscila meets the security and enterprise risk teams monthly. They share incident data, align risk ratings and coordinate on vendor reviews. The security team adopts her individual-harm column in their breach assessments. She notes that privacy, security and risk functions often duplicate work or leave gaps between them, and that regular coordination makes the organisation's protection more coherent and less burdensome for teams who must answer all three. Priscila, the security lead and the compliance officer now meet monthly and share one register of open actions.

### 7.4 Champions

Priscila builds a network of privacy champions, one in each department, trained to answer basic questions and spot issues. Champions meet quarterly and share examples. She finds that champions catch problems early, such as a customer service team sharing screenshots containing card numbers in internal chat. Dr. Ward notes that a small privacy team can extend its reach through champions, as long as they receive training, time and recognition. Each champion receives two hours of training each quarter. Their names appear on the intranet privacy page.

### Worked example

Priscila adds change screening that triggers three DPIAs in a quarter, embeds privacy in procurement, coordinates monthly with security and risk and builds a champion network that spots screenshot sharing.

> **Synthetic case.** Processes are synthetic; GDPR Article 28, LGPD and EDPB Guidelines 07/2020 are real.

### Errors and limits

Screening questions can be answered carelessly; spot-check answers.

### Exercises

- **EX031 — Screening triggers.** Name two screening questions that trigger a DPIA. *Rubric:* 3 = new data, new purpose, new vendor or many customers affected;; 2 = one;; 1 = none;; 0 = none.
- **EX032 — Procurement criteria.** What privacy criteria were added to procurement? *Rubric:* 3 = Article 28-compliant agreements, deletion terms, sub-processor lists and breach times;; 2 = two;; 1 = none;; 0 = none.
- **EX033 — Champion catch.** What did champions catch early? *Rubric:* 3 = screenshots with card numbers in internal chat;; 2 = mentions screenshots;; 1 = nothing;; 0 = none.
- **EX034 — Coordination value.** Why coordinate privacy, security and risk monthly? *Rubric:* 3 = avoids duplication and gaps, making protection coherent;; 2 = mentions alignment;; 1 = unnecessary;; 0 = none.
- **EX035 — Fraud DPIA.** Which existing product change triggered a DPIA? *Rubric:* 3 = changes to the fraud model;; 2 = mentions fraud;; 1 = none;; 0 = none.

### Synthesis

Chapter 7 integrates privacy. Chapter 8 handles difficult cases.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Privacy and data protection: difficult cases

### Learning outcomes

You will (1) handle conflicting obligations such as anti-money-laundering and erasure; (2) respond to law enforcement requests; (3) manage a complex breach.

### 8.1 AML versus erasure

A customer asks Corvina to erase all their data. Anti-money-laundering rules require Corvina to keep transaction records and identity documents for several years. Priscila explains that GDPR Article 17(3)(b) allows retention where processing is necessary for compliance with a legal obligation, and the LGPD has similar provisions. Corvina erases marketing data and profile preferences, restricts the retained records to compliance use and tells the customer clearly what is kept, why and for how long. Anti-money-laundering law requires keeping records for years. Erasure therefore applies only partly.

### 8.2 Law enforcement requests

Police request transaction records for a customer under investigation. Priscila checks that the request is in proper legal form, specifies the data and comes from an authorised body. Corvina discloses only the transactions in the requested period and records the disclosure. She notes that Corvina may not be able to inform the customer if this would prejudice the investigation. She creates a procedure for such requests to ensure consistency and to protect both customers and staff. Each request is checked for a legal basis.

### 8.3 Complex breach

A vendor providing customer support software reports that an attacker accessed support tickets, some containing partial card numbers and addresses. Priscila leads the response. The breach affects customers in both countries. Under the GDPR, Corvina notifies the Portuguese supervisory authority within 72 hours; under the LGPD, it communicates with the Brazilian authority within the timeframe set by its regulations. EDPB Guidelines 9/2022 help assess risk. Affected customers are informed with advice on phishing. The response log records each notification time, so the team can show that both the Portuguese and Brazilian deadlines were met.

### 8.4 Lessons

Priscila reflects that difficult cases often involve competing obligations, multiple jurisdictions and incomplete information. Clear procedures, documented reasoning and coordination with legal counsel help. She updates the vendor contract to require faster notification and restricts card data in support tickets through automated masking. Dr. Ward notes that difficult cases test whether a privacy programme works under pressure, and that learning from them is as important as handling them. The breach review produces three changes: faster vendor contact, a template for customer letters and a rehearsal every six months.

### Worked example

Priscila balances erasure with AML retention, handles a police request with minimal disclosure, coordinates a cross-border vendor breach and adds automated masking of card data in tickets.

> **Synthetic case.** Cases are synthetic; GDPR Article 17(3)(b) and EDPB Guidelines 9/2022 are real.

### Errors and limits

Jurisdiction-specific timelines change; check current regulations.

### Exercises

- **EX036 — AML erasure.** What does Corvina erase and retain for the erasure request? *Rubric:* 3 = erases marketing and preferences; retains AML records restricted to compliance;; 2 = one part;; 1 = everything;; 0 = none.
- **EX037 — Article 17(3)(b).** Which provision allows retaining data for legal obligations? *Rubric:* 3 = GDPR Article 17(3)(b);; 2 = close;; 1 = wrong;; 0 = none.
- **EX038 — Police disclosure.** What did Corvina disclose to police? *Rubric:* 3 = only transactions in the requested period, with a record;; 2 = mentions limited;; 1 = all;; 0 = none.
- **EX039 — Cross-border breach.** Which authorities were notified for the vendor breach? *Rubric:* 3 = Portuguese supervisory authority under GDPR and Brazilian authority under LGPD;; 2 = one;; 1 = none;; 0 = none.
- **EX040 — Ticket masking.** What preventive fix followed the breach? *Rubric:* 3 = automated masking of card data in support tickets;; 2 = mentions masking;; 1 = none;; 0 = none.

### Synthesis

Chapter 8 handles hard cases. Chapter 9 provides leadership and assurance.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Privacy and data protection: leadership and assurance

### Learning outcomes

You will (1) report privacy risk to a board with indicators; (2) set appetite thresholds; (3) provide assurance on the privacy programme.

### 9.1 Board reporting

Corvina's board wants to understand privacy risk. Priscila proposes six key risk indicators with thresholds approved by the board as its risk appetite: rights requests answered late, breaches notified late, processors without agreements, records past retention, DPIAs overdue for review and staff training overdue. Each has an amber threshold equal to the appetite and a red threshold at one and a half times the appetite. The indicators summarise complex operations in a form the board can monitor. Four indicators are chosen. Each has a clear source.

### 9.2 The dashboard

The lab compares current values with thresholds. Late rights requests are 4.0% against a 5.0% threshold, green. DPIAs overdue are 2 against 3, green. Training overdue is 10.5% against 10.0%, amber. Breaches notified late are 1 against 0.5, red. Processors without agreements are 6.0% against 2.0%, red. Records past retention are 11.0% against 5.0%, red. Three indicators are red. Priscila presents each red indicator with its cause and a remediation plan. Each red indicator has an owner and a date. The board asks why retention is so high, and Priscila explains that old systems had no deletion rules, which is the problem her applied project in chapter 11 will address directly over the following six months.

### 9.3 Assurance

The board asks whether the indicators can be trusted. Priscila arranges for internal audit to test two indicators each quarter, sampling underlying records. The first audit finds that the processors-without-agreements figure was understated because some vendors were missing from the register. The corrected figure is higher. She reports the correction openly. She notes that assurance must test both controls and the data used to report on them. Internal audit found that one system had been left out of the retention calculation, which made the indicator look better than it was.

### 9.4 Leadership

Priscila reflects on leadership. Board members respond to clear risks, trends and plans, not to technical detail. She learns to tell a short story for each red indicator: what is wrong, why it matters to customers, what will fix it and when. Dr. Ward notes that privacy leaders must earn board attention by being concise and accurate, and that honest corrections increase rather than reduce credibility over time. Her board papers never exceed two pages and always end with the decision she needs.

### Lab — Privacy risk indicators against board appetite

```python
# Privacy key risk indicators against board-approved appetite thresholds (amber at threshold, red at 1.5x).
kris = [("rights requests late (%)", 4.0, 5.0), ("breaches notified late (count/qtr)", 1, 0.5), ("processors without DPA (%)", 6.0, 2.0),
        ("records past retention (%)", 11.0, 5.0), ("DPIAs overdue for review", 2, 3), ("staff training overdue (%)", 10.5, 10.0)]
for name, v, t in kris:
    st = "RED" if v >= 1.5 * t else "AMBER" if v >= t else "GREEN"
    print(f"{name:36s} value {v:5.1f} threshold {t:4.1f} {st}")
```

Run with `python3 lab_kri.py`. Verified output:

```text
rights requests late (%)             value   4.0 threshold  5.0 GREEN
breaches notified late (count/qtr)   value   1.0 threshold  0.5 RED
processors without DPA (%)           value   6.0 threshold  2.0 RED
records past retention (%)           value  11.0 threshold  5.0 RED
DPIAs overdue for review             value   2.0 threshold  3.0 GREEN
staff training overdue (%)           value  10.5 threshold 10.0 AMBER
```

### Worked example

Priscila reports six indicators: three red (late breach notification, processors without agreements, records past retention), one amber (training) and two green, arranges audit testing and corrects an understated figure.

> **Synthetic case.** Indicators and thresholds are synthetic.

### Errors and limits

Indicators can be gamed; audit underlying data.

### Exercises

- **EX041 — Red indicators.** Which indicators are red? *Rubric:* 3 = breaches notified late, processors without DPA, records past retention;; 2 = two;; 1 = wrong;; 0 = none.
- **EX042 — Amber indicator.** Which indicator is amber and why? *Rubric:* 3 = staff training overdue: 10.5% just above 10.0%;; 2 = names it;; 1 = none;; 0 = none.
- **EX043 — Red threshold.** How is the red threshold defined? *Rubric:* 3 = 1.5 times the appetite threshold;; 2 = mentions multiple;; 1 = none;; 0 = none.
- **EX044 — Audit finding.** What did internal audit find? *Rubric:* 3 = processors-without-agreements figure understated due to register gaps;; 2 = mentions understated;; 1 = none;; 0 = none.
- **EX045 — Board story.** What four elements does Priscila use for each red indicator? *Rubric:* 3 = what is wrong, why it matters, what fixes it, when;; 2 = three;; 1 = none;; 0 = none.

### Synthesis

Chapter 9 leads and assures. Chapter 10 reads and critiques research.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) critique research on de-identification and consent; (2) judge relevance to practice; (3) write a critical summary.

### 10.1 Reading de-identification research

Dr. Ward assigns key research. Sweeney (2002) showed that combinations of attributes re-identify people. Narayanan and Shmatikov (2008) showed linkage of sparse behavioural data. Priscila applies these to transaction data, which are highly distinctive: a few purchases with times and places can identify a customer. She concludes that Corvina should never treat transaction-level data as anonymous merely because names are removed, which affects how it shares data with partners. Narayanan and Shmatikov showed that sparse records, such as movie ratings, can be re-identified with little auxiliary information, and transaction histories are similarly sparse.

### 10.2 Reading differential privacy

Priscila reads Dwork and Roth (2014) on differential privacy. She understands the core idea: outputs should change little whether any individual is included. She critiques its practical use at Corvina: aggregate spending statistics for partners could use differential privacy, but fraud detection requires individual data and cannot. She writes that differential privacy is a strong tool for releases but not a general solution, and that choosing parameters requires expertise. Dwork and Roth explain how noise protects individuals, but the privacy budget must be set and spent carefully.

### 10.3 Reading behavioural research

Priscila revisits Acquisti and colleagues (2015). She critiques the relevance: the review covers many contexts, mostly online; payment apps share features such as defaults and framing. Her own A/B test supports the review's claim that design shapes choices. She notes that research often lacks the specific context practitioners face, so practitioners must test locally, as she did, rather than assume results transfer exactly. Acquisti and colleagues review evidence that people's privacy choices are uncertain, context-dependent and malleable, which matches what her consent test showed about design influencing acceptance.

### 10.4 Writing critique

Priscila writes a critical summary for colleagues: what each work claims, its evidence, its limits and its implications for Corvina. She avoids overstating results. Dr. Ward praises the summary for connecting research to decisions and for distinguishing what the research shows from what Corvina must test. Priscila decides to share the summary with the privacy champions as background reading. Her critique template asks four questions of each paper: what was studied, on what data, what was found and what would change if the setting were a Brazilian and Portuguese payments firm. The answers fit on one page per paper.

### Worked example

Priscila applies Sweeney and Narayanan and Shmatikov to transaction data, limits differential privacy to releases, relates behavioural research to her A/B test and writes a critical summary for colleagues.

> **Synthetic case.** Corvina's applications are synthetic; the cited works are real.

### Errors and limits

Summaries simplify; link to originals.

### Exercises

- **EX046 — Transaction data.** Why are transaction data not anonymous after removing names? *Rubric:* 3 = few purchases with times and places identify customers;; 2 = mentions distinctiveness;; 1 = anonymous;; 0 = none.
- **EX047 — DP limits.** Where can Corvina not use differential privacy? *Rubric:* 3 = fraud detection, which needs individual data;; 2 = mentions fraud;; 1 = everywhere;; 0 = none.
- **EX048 — Local testing.** Why must practitioners test research claims locally? *Rubric:* 3 = research contexts differ from their own;; 2 = mentions context;; 1 = trust research;; 0 = none.
- **EX049 — Summary elements.** What does each entry in Priscila's summary contain? *Rubric:* 3 = claim, evidence, limits, implications;; 2 = three;; 1 = none;; 0 = none.
- **EX050 — Shared reading.** Who receives the critical summary? *Rubric:* 3 = the privacy champions;; 2 = mentions colleagues;; 1 = board;; 0 = none.

### Synthesis

Chapter 10 critiques research. Chapter 11 delivers the applied project.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) deliver a privacy improvement project; (2) measure its effect; (3) manage stakeholders through change.

### 11.1 Choosing the project

Priscila's applied project addresses the worst red indicator: records past retention at 11.0%. She proposes automated retention enforcement across Corvina's main systems, with exceptions for AML records and legal holds. The project aims to bring the indicator below 5.0% within six months. She defines scope, stakeholders and measures, and secures sponsorship from the chief technology officer. She chooses retention because it is the reddest indicator, affects every system and has a clear measure that the board already tracks. A project with a visible number makes progress easy to report and hard to dispute.

### 11.2 Delivery

The project builds a retention table linking data categories to periods and legal bases, tags records with categories, and runs weekly deletion jobs with review for exceptions. Legal counsel confirms AML periods. The project team tests on synthetic data first, then on one system, then on all. During rollout, a job nearly deletes records under a legal hold because a tag was missing; the review step catches it. The team adds a check that blocks deletion of untagged records. Tagging finishes first.

### 11.3 Effect

After six months, records past retention fall from 11.0% to 3.8%, below the appetite threshold. Storage costs fall. Rights requests become faster because there are fewer old records to search. Priscila reports the result to the board with the near miss and its fix. She notes that the improvement must be sustained by monitoring and that new systems must join the retention process before launch. The indicator falls from 11.0% to 3.8%, below the 5.0% appetite, and turns green on the board dashboard for the first time.

### 11.4 Stakeholders

Some teams resisted deleting data they might use someday. Priscila listened to their needs and found that most could be met with aggregated statistics kept longer. She also explained the risk of keeping data unnecessarily, using the breach in Chapter 8 as an example. Dr. Ward notes that change management is often the hardest part of privacy projects, and that listening and offering alternatives is more effective than enforcing rules alone. Finance agreed to deletion once archived summaries were offered. That compromise unlocked the remaining systems.

### Worked example

Priscila delivers automated retention, catches a legal-hold near miss, reduces records past retention from 11.0% to 3.8% and manages resistance with aggregated alternatives.

> **Synthetic case.** The project and figures are synthetic.

### Errors and limits

Lower retention figures can hide unindexed data stores; keep discovering.

### Exercises

- **EX051 — Project result.** How did records past retention change? *Rubric:* 3 = from 11.0% to 3.8%;; 2 = direction;; 1 = wrong;; 0 = none.
- **EX052 — Near miss.** What near miss occurred and how was it fixed? *Rubric:* 3 = a job nearly deleted legal-hold records; untagged records now blocked;; 2 = one part;; 1 = none;; 0 = none.
- **EX053 — Resistance.** How did Priscila handle teams wanting to keep data? *Rubric:* 3 = offered aggregated statistics kept longer and explained risks;; 2 = one part;; 1 = forced;; 0 = none.
- **EX054 — Side benefits.** Name two side benefits of the project. *Rubric:* 3 = lower storage costs and faster rights requests;; 2 = one;; 1 = none;; 0 = none.
- **EX055 — Sustaining.** What sustains the improvement? *Rubric:* 3 = monitoring and onboarding new systems before launch;; 2 = one;; 1 = nothing;; 0 = none.

### Synthesis

Chapter 11 delivers change. Chapter 12 reviews and transfers learning.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review a two-year programme of change; (2) transfer lessons to other contexts; (3) plan continuing development.

### 12.1 Review

Priscila reviews two years at Corvina. The programme moved from stale records and generic training to change screening, procurement controls, a champion network, board indicators and automated retention. The consent banner test changed design practice. The GPS decision showed how evidence supports necessity. Two red indicators remain: late breach notification and processors without agreements. She presents a plan for each, recognising that improvement is continuous. Breach notification is late because vendors report slowly, so contracts will set a 24-hour vendor reporting duty.

### 12.2 Transfer

Dr. Ward asks what Priscila would transfer to another organisation. She lists principles rather than tools: separate constraints from trade-offs; test necessity with evidence; measure behaviour, not only policy; report honestly to the board; and integrate privacy into existing processes. She notes that tools and thresholds would differ in a hospital or a public agency, but that these principles would still guide good decisions. In a hospital, for example, clinical safety would add constraints and patients would replace customers in the harm column of the register.

### 12.3 Limits

Priscila notes limits of her experience. Corvina is a mid-sized firm with board support; smaller firms may lack resources, and larger ones may face more complexity. Her evidence from tests is local. She avoids presenting her programme as a template. She also notes that laws evolve, such as the 2025 edition of ISO/IEC 27701, so practices must be updated over time. Her results come from one firm in two countries, with synthetic data in the labs and a particular regulatory history. A different culture or regulator could change what works best.

### 12.4 Development

Priscila plans continuing development: deeper knowledge of privacy engineering, especially differential privacy for partner statistics; experience with supervisory authority interactions; and mentoring privacy champions. She also plans to present her A/B test at a practitioner conference. Dr. Ward closes the course by noting that the best privacy leaders combine evidence, ethics and organisational skill, and that Priscila has shown all three. Priscila plans to mentor the privacy champions and to publish an anonymised case study of the consent test for other practitioners in the region.

### Worked example

Priscila reviews the programme, transfers five principles, states limits of her experience and plans development in privacy engineering, regulatory work and mentoring.

> **Synthetic case.** The review is synthetic; ISO/IEC 27701:2025 is real.

### Errors and limits

Self-review is biased; ask colleagues and auditors for their view.

### Exercises

- **EX056 — Remaining red.** Which indicators remain red after two years? *Rubric:* 3 = late breach notification and processors without agreements;; 2 = one;; 1 = none;; 0 = none.
- **EX057 — Transferable principles.** Name three transferable principles. *Rubric:* 3 = e.g. separate constraints from trade-offs; test necessity; report honestly;; 2 = two;; 1 = tools;; 0 = none.
- **EX058 — Not a template.** Why does Priscila avoid presenting her programme as a template? *Rubric:* 3 = contexts and resources differ;; 2 = mentions context;; 1 = universal;; 0 = none.
- **EX059 — Evolving standards.** Give an example of an evolving standard she must track. *Rubric:* 3 = ISO/IEC 27701:2025 edition;; 2 = mentions ISO;; 1 = none;; 0 = none.
- **EX060 — Development areas.** Name two development areas Priscila plans. *Rubric:* 3 = privacy engineering/DP, regulator interactions, mentoring;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Chapter 12 completes the postgraduate route. The worked results follow, then the references.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Priscila Andrade, Dr. Helen Ward, Ashgrove School of Management, Corvina Pay and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A constraint: processing without a lawful basis is not an option to weigh.

**EX002.** By testing whether city-level location detects fraud as well as GPS.

**EX003.** Question, options, evidence, legal constraints, chosen option, residual risk and owner.

**EX004.** They let the organisation compare what it expected with what happened.

**EX005.** The LGPD for Brazilian operations and the GDPR for Portuguese operations.

**EX006.** DPIAs were not triggered by significant changes to existing processing.

**EX007.** Ten, including credit protection, which is relevant to a payments firm.

**EX008.** She designs each process to meet the stricter of the two requirements.

**EX009.** As structured checklists to find gaps.

**EX010.** Because DPIAs, rights handling and vendor management all depend on an accurate inventory.

**EX011.** Nothing; detection and false alarms matched city-level location.

**EX012.** It produces 1,572 false alarms, harming many legitimate customers.

**EX013.** City-level location.

**EX014.** GDPR data minimisation in Article 5(1)(c) and LGPD necessity in Article 6(III).

**EX015.** Because a fair test might confirm their view.

**EX016.** Data protection law assesses risks to individuals, which company-focused registers miss.

**EX017.** Customers share data to pay, not to have intimate events inferred; it is secondary use and aggregation.

**EX018.** The DPO reported to the executive who also owned marketing revenue.

**EX019.** That other tasks and duties of the DPO do not result in a conflict of interests.

**EX020.** Using coarser spending categories and opt-in personalisation.

**EX021.** Rejection is less prominent than acceptance, so consent is not as easy to refuse.

**EX022.** Lower acceptance shows freer choice; nudged consent is legally and reputationally fragile.

**EX023.** B is the smallest change likely to meet the law.

**EX024.** Consent withdrawals within ninety days.

**EX025.** Article 5(3) of the ePrivacy Directive.

**EX026.** 22.0 percentage points, 95% interval 20.0 to 24.0.

**EX027.** 41 per 1,000 under A versus 12 under B, over three times as many.

**EX028.** Because A is probably non-compliant, its use must be limited to the test.

**EX029.** Its consents are fewer but more stable over time.

**EX030.** Because the design nudged acceptance and later withdrawals show many choices were not genuine.

**EX031.** New data collection and new purposes (also new vendors or large impact).

**EX032.** Compliant agreements, deletion terms, sub-processor lists and breach notification times.

**EX033.** Customer service staff sharing screenshots containing card numbers.

**EX034.** It reduces duplication and gaps between functions.

**EX035.** Changes to the fraud model.

**EX036.** It erases marketing data and preferences, keeping AML records restricted to compliance use.

**EX037.** GDPR Article 17(3)(b).

**EX038.** Only the transactions for the requested period, recorded in a log.

**EX039.** The Portuguese supervisory authority and the Brazilian national authority.

**EX040.** Automatic masking of card data in support tickets.

**EX041.** Late breach notification, processors without agreements and records past retention.

**EX042.** Training overdue at 10.5%, just above its 10.0% threshold.

**EX043.** At one and a half times the board's appetite threshold.

**EX044.** That missing vendors in the register understated the processors-without-agreements figure.

**EX045.** What is wrong, why it matters to customers, the fix and the timeline.

**EX046.** A few transactions are distinctive enough to identify individuals.

**EX047.** In fraud detection, which requires individual-level decisions.

**EX048.** Because published studies rarely match a practitioner's specific setting.

**EX049.** The claim, its evidence, its limits and implications for Corvina.

**EX050.** The privacy champion network.

**EX051.** From 11.0% to 3.8%, below the 5.0% threshold.

**EX052.** A missing tag nearly caused deletion of held records; deletion of untagged records is now blocked.

**EX053.** By meeting needs with aggregated statistics and explaining the risks of keeping data.

**EX054.** Reduced storage costs and faster rights request handling.

**EX055.** Ongoing monitoring and requiring new systems to join the retention process.

**EX056.** Late breach notification and processors without agreements.

**EX057.** Separate constraints from trade-offs, test necessity with evidence and report honestly to the board.

**EX058.** Organisations differ in size, sector and resources.

**EX059.** The 2025 edition of ISO/IEC 27701.

**EX060.** Differential privacy for partner statistics and supervisory authority experience.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science, 347*(6221), 509–514. <https://doi.org/10.1126/science.aaa1465>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. <https://doi.org/10.1561/0400000042>
- European Data Protection Board. (2023). *Guidelines 9/2022 on personal data breach notification under GDPR* (Version 2.0, adopted 28 March 2023). <https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. <https://doi.org/10.1109/SP.2008.33>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
- European Data Protection Board. (2021). *Guidelines 07/2020 on the concepts of controller and processor in the GDPR* (Version 2.0 adopted 7 July 2021; Version 2.1, 20 September 2022). <https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Union. (2002). Directive 2002/58/EC of the European Parliament and of the Council of 12 July 2002 concerning the processing of personal data and the protection of privacy in the electronic communications sector (ePrivacy Directive), as amended by Directive 2009/136/EC. *Official Journal of the European Communities, L 201*, 37–47 (CELEX 32002L0058; ELI dir/2002/58/oj, confirmed via the Publications Office record). <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0058>
