# Security Governance, Risk and Compliance: Professional Course

- Language: English (`en`); course 028, Professional course (6 months).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working professionals moving into GRC roles who need practical methods for risk, findings, control testing and supplier assurance.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs compare self-assessment with independent review, compute zero-deviation sample sizes and age open findings on synthetic data. The SOC 2 report reviewed is fictional and not an attestation; standards are cited by edition and paraphrased, and nothing here is legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one compliance professional through a six-month course centred on a credit union: foundations, stakeholders, authorised practice, risk methods, self-assessment, findings workflow, control testing, a supplier case, reporting and ethics, process quality, a supervised assurance review and the portfolio. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lena Hoffmann** | Compliance professional moving into GRC | Invented |
| **Mr. Victor Reyes** | Mentor | Invented |
| **Ashby Professional Academy** | Fictional academy | Invented |
| **Marston Credit Union** | Fictional cooperative, 400 staff | Invented |

### Core sources

ISO 31000:2018; ISO/IEC 27005:2022 and 27001:2022; PCI DSS v4.0; AICPA trust services criteria. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) explain core security concepts in business terms; (2) relate them to a credit union's services; (3) recognise where governance adds value.

### 1.1 Core concepts

Lena Hoffmann has worked for six years in compliance at Marston Credit Union, a fictional member-owned financial cooperative with four hundred staff, savings and loan products, a mobile banking app and card services. She joins the six-month professional course at the fictional Ashby Professional Academy, mentored by Mr. Victor Reyes. Her first module revisits core ideas: confidentiality, integrity and availability, threats exploiting vulnerabilities to cause impact, and controls that prevent, detect or correct. She learns to explain each using Marston's services rather than abstract definitions.

### 1.2 Applying to Marston

For members' account data, confidentiality and integrity matter most: leaks or wrong balances damage trust and may breach law. For the mobile app, availability matters too, since members expect access at any time. Lena lists threats that matter most: account takeover through stolen passwords, fraud through social engineering of call centre staff, ransomware affecting core banking and errors by suppliers. She learns that understanding the business first lets her judge which controls are proportionate. Account takeover through stolen passwords, for instance, points to stronger authentication on the app rather than more call centre training.

### 1.3 Where governance helps

Lena's compliance background helps her see where governance adds value. Many controls exist, but nobody checks whether they work. Risk decisions are made informally by IT without involving business owners. The board receives long reports with little analysis. She sees her new role as connecting these pieces: clear ownership, risk decisions documented with business input, controls tested and board reports that enable decisions. Mr. Reyes notes that her compliance discipline is a strong foundation for this broader work. Mr. Reyes adds that the informal IT risk decisions are the first gap to close, because every later step depends on business owners taking part.

### Worked example

Lena relates security concepts to Marston's services, lists key threats and identifies where governance would add value.

> **Synthetic case.** Ashby, Marston and all details are synthetic.

### Errors and limits

Business framing can oversimplify technology. Threat lists change.

### Exercises

- **EX001 — Member data priorities.** Which security objectives matter most for member account data? *Rubric:* 3 = confidentiality and integrity;; 2 = C and I;; 1 = availability only;; 0 = none.
- **EX002 — App availability.** Why does availability matter for the mobile app? *Rubric:* 3 = members expect access at any time;; 2 = access;; 1 = vague;; 0 = none.
- **EX003 — Social engineering target.** Which staff are targeted by social engineering fraud? *Rubric:* 3 = call centre staff;; 2 = call centre;; 1 = vague;; 0 = none.
- **EX004 — Governance gaps.** Name two governance gaps Lena identified. *Rubric:* 3 = untested controls and informal risk decisions;; 2 = gaps;; 1 = vague;; 0 = none.
- **EX005 — Compliance strength.** Why is Lena's compliance background useful? *Rubric:* 3 = its discipline is a strong foundation;; 2 = discipline;; 1 = vague;; 0 = none.

### Synthesis

Security foundations framed in business terms show where governance adds value.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Security governance, risk and compliance: service and stakeholder context

### Learning outcomes

You will (1) identify stakeholders in a credit union's security; (2) map their expectations; (3) define the GRC programme's purpose.

### 2.1 Stakeholders

Lena maps stakeholders: members who trust Marston with savings, the board elected by members, the financial regulator, the deposit insurer, card schemes through PCI DSS v4.0 obligations, auditors and suppliers such as the core banking provider. Each has expectations about security. Members expect their money and data to be safe. The regulator expects sound risk management and timely incident reporting. Card schemes expect cardholder data protection. She learns that GRC serves many audiences at once. The deposit insurer and the card schemes, for example, will ask for different evidence about the same controls.

### 2.2 Expectations

Lena lists each stakeholder's expectations, how they are expressed and how Marston shows it meets them. The regulator's expectations come through rules and supervisory visits; Marston shows compliance through policies, risk reports and audit results. The board's expectations come through risk appetite; Marston shows performance through reports. She learns that mapping expectations to evidence reveals where Marston has no clear way to show it meets an expectation. For member expectations, for instance, Marston has no report at all showing that their data are safe, which becomes an early gap to close.

### 2.3 Programme purpose

With this context, Lena drafts a purpose statement for Marston's GRC programme: to keep security risk within the board's appetite, meet legal and contractual obligations and give members, the board and regulators reliable evidence that their trust is justified. Mr. Reyes asks how she would know if the programme succeeded. She adds measurable outcomes, such as top risks within appetite, no overdue high findings and clean regulatory reviews. Each outcome can be checked quarterly, so the purpose statement becomes something the board can hold the programme to.

### Worked example

Lena maps seven stakeholders, links expectations to evidence and drafts a purpose statement with measurable outcomes.

> **Synthetic case.** Marston's context is synthetic; PCI DSS v4.0 is real.

### Errors and limits

Stakeholder views change. Purpose statements can be vague.

### Exercises

- **EX006 — Regulator expectation.** What does the regulator expect? *Rubric:* 3 = sound risk management and timely incident reporting;; 2 = expectations;; 1 = vague;; 0 = none.
- **EX007 — Card scheme duty.** Which obligation comes from card schemes? *Rubric:* 3 = PCI DSS v4.0;; 2 = PCI;; 1 = vague;; 0 = none.
- **EX008 — Mapping benefit.** What does mapping expectations to evidence reveal? *Rubric:* 3 = expectations Marston cannot yet show it meets;; 2 = gaps;; 1 = vague;; 0 = none.
- **EX009 — Programme purpose.** What is the purpose of Marston's GRC programme? *Rubric:* 3 = keep risk within appetite, meet obligations, give reliable evidence;; 2 = purpose;; 1 = vague;; 0 = none.
- **EX010 — Success outcome.** Name one measurable outcome Lena added. *Rubric:* 3 = no overdue high findings;; 2 = outcome;; 1 = vague;; 0 = none.

### Synthesis

Stakeholder context defines what the GRC programme must achieve and evidence.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) work within authority and confidentiality limits; (2) handle evidence securely; (3) avoid conflicts in assurance work.

### 3.1 Authority

In her new role, Lena can request evidence from any department, but she cannot change systems or approve exceptions herself. She learns to confirm her authority before acting, especially when asked to look at member data. Marston's internal policy allows GRC staff to access member data only when needed for a specific review, with approval and logging. She learns that respecting these limits protects members and keeps her work defensible. When a review needs member data, she now files the approval reference with her evidence so the access can be justified afterwards.

### 3.2 Evidence handling

Lena collects evidence such as access review sign-offs, system reports and test results. She stores it in a restricted folder, names files consistently with date and source, and records where each item came from. She removes member details that are not needed. She learns that evidence must be complete enough to support conclusions, protected from alteration and handled according to its sensitivity, especially when it contains personal or financial information. For an access review sign-off, she records the system it came from and the date it was exported, so another reviewer could obtain the same file.

### 3.3 Conflicts

Lena previously wrote Marston's data protection procedures. Now she is asked to assess whether they work. Mr. Reyes points out the conflict: she may be inclined to see her own work favourably. She discloses the conflict and asks a colleague to review that area. She learns that in assurance work, independence matters, and that disclosing and managing conflicts is better than pretending they do not exist. The colleague's review of the data protection procedures is then reported under the colleague's name, not Lena's.

### Worked example

Lena confirms her authority before accessing data, handles evidence securely and discloses a conflict in assessing her own procedures.

> **Synthetic case.** Policies and roles are synthetic.

### Errors and limits

Independence is relative in small teams. Evidence handling takes time.

### Exercises

- **EX011 — Lena's limits.** What can Lena not do in her role? *Rubric:* 3 = change systems or approve exceptions;; 2 = limits;; 1 = vague;; 0 = none.
- **EX012 — Member data access.** When may GRC staff access member data? *Rubric:* 3 = only when needed for a specific review, with approval and logging;; 2 = need;; 1 = always;; 0 = none.
- **EX013 — Evidence protection.** What protections apply to evidence? *Rubric:* 3 = restricted folder, consistent names, source records, minimised data;; 2 = protection;; 1 = vague;; 0 = none.
- **EX014 — Conflict found.** What conflict did Lena have? *Rubric:* 3 = assessing procedures she wrote;; 2 = self-review;; 1 = vague;; 0 = none.
- **EX015 — Conflict response.** How did Lena manage the conflict? *Rubric:* 3 = disclosed it and asked a colleague to review;; 2 = disclose;; 1 = ignore;; 0 = none.

### Synthesis

Authorised, secure and independent practice makes GRC evidence trustworthy.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Security governance, risk and compliance: core methods

### Learning outcomes

You will (1) run a risk assessment using an established process; (2) link risks to appetite; (3) record treatment decisions.

### 4.1 The process

Lena learns the risk process described in ISO 31000:2018 and applied to information security in ISO/IEC 27005:2022: establish context, identify risks, analyse and evaluate them, treat them, and monitor and review. She runs an assessment for Marston's mobile banking app with the product owner, IT security and fraud teams. They identify risks such as account takeover, fraudulent payments to new payees and app outages, each described with causes and consequences. Writing each risk as a cause leading to a consequence, such as stolen passwords leading to fraudulent payments to new payees, makes treatments easier to target.

### 4.2 Appetite

Marston's board has stated a low appetite for member financial loss from fraud and a moderate appetite for short service outages. Lena compares each risk with appetite. Account takeover leading to member losses is above appetite and must be treated. Short app outages fall within appetite if recovered within four hours. She learns that appetite turns analysis into decisions: it tells the organisation which risks need action and which can be accepted. Because the four-hour recovery is the threshold, Marston must also be able to show that it actually recovers within four hours.

### 4.3 Treatment decisions

For account takeover, the team chooses stronger authentication for new payees and transaction monitoring. The product owner agrees to own the treatment with a target date. For outages, the team accepts the current recovery capability and documents the acceptance. Lena records each decision with its owner, date and reasons. She learns that recorded decisions show regulators and auditors that risks were considered and managed deliberately. Mr. Reyes notes that the documented outage acceptance should name the product owner and be revisited if outages begin to exceed four hours.

### Worked example

Lena runs a mobile app risk assessment, compares risks with appetite and records treatment and acceptance decisions.

> **Synthetic case.** Risks and appetite are synthetic; ISO 31000:2018 and ISO/IEC 27005:2022 are real.

### Errors and limits

Workshops depend on attendees. Appetite statements can be vague.

### Exercises

- **EX016 — Process steps.** Name the main steps of the risk process. *Rubric:* 3 = context, identify, analyse, evaluate, treat, monitor;; 2 = steps;; 1 = vague;; 0 = none.
- **EX017 — Above appetite.** Which risk was above appetite? *Rubric:* 3 = account takeover leading to member losses;; 2 = takeover;; 1 = outages;; 0 = none.
- **EX018 — Outage tolerance.** When are app outages within appetite? *Rubric:* 3 = if recovered within four hours;; 2 = 4 hours;; 1 = vague;; 0 = none.
- **EX019 — Takeover treatment.** What treatments were chosen for account takeover? *Rubric:* 3 = stronger new-payee authentication and transaction monitoring;; 2 = two;; 1 = vague;; 0 = none.
- **EX020 — Decision records.** Why record treatment decisions? *Rubric:* 3 = to show risks were managed deliberately;; 2 = evidence;; 1 = vague;; 0 = none.

### Synthesis

An established process linked to appetite turns risk analysis into recorded decisions.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security governance, risk and compliance: tools and interpretation

### Learning outcomes

You will (1) use control self-assessment results; (2) compare them with independent review; (3) interpret gaps carefully.

### 5.1 Self-assessment

Marston asks control owners to rate their controls each quarter from zero, not in place, to four, fully effective and evidenced. Lena learns that self-assessment is cheap and engages owners, but tends to be optimistic. To test this, she compares owners' ratings with an independent review by internal audit for four control domains: access management, change management, backups and vendor management. Both used the same rating scale and definitions. Using identical definitions means any gap between the two sets of ratings reflects judgement, not different scales.

### 5.2 The comparison

The lab computes average ratings. Access management self-rates at three point two five against two point five from review, a gap of three quarters of a point. Change management self-rates two point six seven against one point six seven, a gap of one. Backups self-rate four against three point five. Vendor management self-rates two point six seven against one point three three, the largest gap at one point three three. Every domain rates itself higher than the review. The pattern is consistent, but the size of each gap is what directs Lena's attention in the next section.

### Lab — Self-assessment versus independent review

```python
"""Control self-assessment: mean rating (0-4) per domain and the gap to independent review."""
self_r = {"access": [3, 3, 4, 3], "change": [3, 2, 3], "backup": [4, 4], "vendor": [3, 3, 2]}
review = {"access": [2, 3, 3, 2], "change": [2, 1, 2], "backup": [4, 3], "vendor": [1, 2, 1]}
for d in self_r:
    s = sum(self_r[d])/len(self_r[d]); r = sum(review[d])/len(review[d])
    print(f"{d}: self {s:.2f} review {r:.2f} gap {s-r:+.2f}")
```

Run with `python3 lab_csa.py`. Verified output:

```text
access: self 3.25 review 2.50 gap +0.75
change: self 2.67 review 1.67 gap +1.00
backup: self 4.00 review 3.50 gap +0.50
vendor: self 2.67 review 1.33 gap +1.33
```

### 5.3 Interpreting

Lena does not conclude that owners are dishonest. She asks why gaps differ. Vendor management owners rated controls as working because contracts include security clauses, while reviewers found that nobody checks supplier compliance. Backups have the smallest gap because restore tests produce clear evidence. She recommends tightening rating definitions to require evidence and focusing independent review on domains with the largest gaps, starting with vendor management. Requiring evidence for a rating of four would, for example, stop vendor management claiming effectiveness from contract clauses alone.

### Worked example

Lena compares self-ratings with independent review, finds all domains overrated with vendor management worst at 1.33 and explains why gaps differ.

> **Synthetic case.** Ratings are synthetic.

### Errors and limits

Small samples of controls. Reviewers can be strict.

### Exercises

- **EX021 — Self-assessment bias.** What is the typical bias of self-assessment? *Rubric:* 3 = optimism;; 2 = optimistic;; 1 = pessimistic;; 0 = none.
- **EX022 — Largest gap.** Which domain had the largest gap? *Rubric:* 3 = vendor management, +1.33;; 2 = vendor;; 1 = backup;; 0 = none.
- **EX023 — Smallest gap.** Why did backups have the smallest gap? *Rubric:* 3 = restore tests produce clear evidence;; 2 = evidence;; 1 = vague;; 0 = none.
- **EX024 — Vendor cause.** Why did vendor owners overrate their controls? *Rubric:* 3 = contracts had clauses but nobody checked compliance;; 2 = assumption;; 1 = vague;; 0 = none.
- **EX025 — Recommendation.** What did Lena recommend? *Rubric:* 3 = evidence-based rating definitions and review focus on largest gaps;; 2 = two;; 1 = vague;; 0 = none.

### Synthesis

Self-assessment engages owners, but independent review shows where optimism hides weakness.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Security governance, risk and compliance: operational workflow

### Learning outcomes

You will (1) design a GRC workflow for findings; (2) set severity-based targets; (3) report progress to management.

### 6.1 Findings workflow

Lena designs a workflow for audit and review findings. Each finding is logged with a description, severity, owner, agreed action and target date. Owners update progress monthly. When an owner claims completion, Lena checks evidence before closing. Overdue findings escalate to the owner's executive. She learns that a clear workflow makes accountability visible and prevents findings from being forgotten after the audit report is filed. Checking evidence before closure prevents a finding being marked done when only a plan exists.

### 6.2 Severity targets

Lena proposes targets by severity: high findings closed within thirty days, medium within ninety and low within one hundred and eighty. She explains that targets must be realistic; a high finding needing a system replacement may need an agreed interim measure and a longer plan. She learns that target dates without realistic plans encourage false closure, while plans with interim measures keep risk managed while longer fixes proceed. A high finding needing a system replacement could, for example, be held within target by an interim restriction while the replacement is planned.

### 6.3 Reporting

Lena reports to the executive risk committee monthly: open findings by severity, overdue findings with owners and reasons, and findings closed with evidence. She leads with overdue high findings. The committee asks owners of overdue items to explain delays. She learns that reporting works when it is short, consistent and leads to action at the right level, rather than simply informing people that problems exist. Leading with overdue high findings means the committee's limited time goes to the items most likely to need executive help.

### Worked example

Lena designs a findings workflow with evidence-based closure, severity targets and monthly committee reporting.

> **Synthetic case.** The workflow is synthetic.

### Errors and limits

Targets can drive false closure. Committees may not act.

### Exercises

- **EX026 — Closure check.** What happens when an owner claims completion? *Rubric:* 3 = Lena checks evidence before closing;; 2 = evidence;; 1 = vague;; 0 = none.
- **EX027 — High target.** What is the target for high findings? *Rubric:* 3 = thirty days;; 2 = 30;; 1 = vague;; 0 = none.
- **EX028 — Long fixes.** How should a high finding needing a system replacement be handled? *Rubric:* 3 = interim measure and longer agreed plan;; 2 = interim;; 1 = vague;; 0 = none.
- **EX029 — Report lead.** What does Lena's report lead with? *Rubric:* 3 = overdue high findings;; 2 = overdue;; 1 = vague;; 0 = none.
- **EX030 — Escalation path.** Where do overdue findings escalate? *Rubric:* 3 = the owner's executive;; 2 = executive;; 1 = vague;; 0 = none.

### Synthesis

A findings workflow with realistic targets and action-focused reporting keeps remediation moving.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Security governance, risk and compliance: controls and verification

### Learning outcomes

You will (1) choose sample sizes for control testing; (2) test a control's operation; (3) state conclusions with their limits.

### 7.1 Sample sizes

Lena needs to test whether Marston's new-payee authentication works for every payment. Testing all payments is impractical, so she samples. The lab computes the smallest sample with no deviations that supports each tolerable deviation rate with ninety-five percent confidence. For ten percent, twenty-nine items suffice; for five percent, fifty-nine; for three percent, ninety-nine. She learns that tighter conclusions require larger samples, and that the tolerable rate should reflect the control's importance. Fifty-nine is the size she will use for new-payee authentication in the next section.

### Lab — Zero-deviation sample sizes for three tolerable rates

```python
"""Smallest zero-deviation sample whose 95% upper bound meets a tolerable rate: (1-t)^n <= 0.05."""
from math import ceil, log
for t in (0.10, 0.05, 0.03):
    n = ceil(log(0.05)/log(1-t)); print(f"tolerable {t:.0%}: sample {n} with no deviations")
```

Run with `python3 lab_n.py`. Verified output:

```text
tolerable 10%: sample 29 with no deviations
tolerable 5%: sample 59 with no deviations
tolerable 3%: sample 99 with no deviations
```

### 7.2 Testing

Because new-payee authentication protects member funds, Lena chooses a five percent tolerable rate and samples fifty-nine new-payee payments at random from the quarter. For each, she checks the authentication log shows a successful second factor before the payment. All fifty-nine show it. She records the sample method, the selected items, the checks and the results so another person could repeat the test. Mr. Reyes points out that random selection across the whole quarter matters, because a sample from one week could miss a period when the control failed.

### 7.3 Conclusions

Lena concludes that, with ninety-five percent confidence, the control failed in no more than five percent of new-payee payments during the quarter. She notes limits: the test covers the app channel only, not branch payments, and checks that authentication happened, not that it was resistant to all attacks. She learns that clear conclusions with stated limits are more valuable than broad claims that the control works. Branch payments would need a separate sample before any statement about all new-payee payments could be made.

### Worked example

Lena computes 29, 59 and 99 as zero-deviation sample sizes, tests 59 payments with no deviations and states a bounded conclusion.

> **Synthetic case.** Payments and results are synthetic.

### Errors and limits

Random sampling misses targeted abuse. Logs may be incomplete.

### Exercises

- **EX031 — Five percent sample.** How many items with no deviations support a 5% tolerable rate? *Rubric:* 3 = fifty-nine;; 2 = 59;; 1 = 29;; 0 = none.
- **EX032 — Three percent sample.** How many are needed for 3%? *Rubric:* 3 = ninety-nine;; 2 = 99;; 1 = vague;; 0 = none.
- **EX033 — Rate choice.** Why choose a 5% tolerable rate here? *Rubric:* 3 = the control protects member funds;; 2 = importance;; 1 = vague;; 0 = none.
- **EX034 — Check performed.** What did Lena check for each payment? *Rubric:* 3 = a successful second factor before payment in the log;; 2 = log check;; 1 = vague;; 0 = none.
- **EX035 — Test limits.** Name one limit of the conclusion. *Rubric:* 3 = covers the app channel only;; 2 = scope;; 1 = vague;; 0 = none.

### Synthesis

Sized samples support bounded, clearly limited conclusions about control operation.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security governance, risk and compliance: supervised case analysis

### Learning outcomes

You will (1) analyse a governance case under supervision; (2) identify control and governance failures; (3) recommend proportionate improvements.

### 8.1 The case

Mr. Reyes gives Lena a synthetic case from a peer credit union. A supplier managing the card platform was breached, exposing some member card data. The credit union had a contract with security clauses and received an annual certificate, but nobody reviewed the supplier's assurance report, which noted exceptions in access management. After the breach, the regulator asked why the exceptions were not followed up. The unread exceptions in access management are exactly the kind of warning that a review of the assurance report would have caught.

### 8.2 Analysis

Lena identifies failures at several levels. At control level, supplier access management had known weaknesses. At process level, assurance reports were received but not read. At governance level, nobody owned supplier risk, and the board never saw supplier risk reported. She notes that this pattern mirrors Marston's own vendor management gap found in self-assessment. She learns that cases are most valuable when they reveal patterns relevant to one's own organisation. Marston's largest self-assessment gap, vendor management at one point three three, therefore becomes the focus of her recommendations.

### 8.3 Recommendations

Lena recommends that Marston assign an owner for supplier risk, review assurance reports for critical suppliers with a checklist that highlights exceptions, track exceptions as findings and report supplier risk to the board twice a year. She keeps the recommendations proportionate to Marston's size. Mr. Reyes asks how she would measure success; she proposes tracking the share of critical suppliers with reviewed reports and the time to follow up exceptions. Both measures can be reported in the twice-yearly supplier risk update to the board.

### Worked example

Lena analyses a peer supplier breach, finds failures at control, process and governance levels and recommends proportionate improvements with measures.

> **Synthetic case.** The case is synthetic.

### Errors and limits

Single cases may not generalise. Hindsight makes failures look obvious.

### Exercises

- **EX036 — Case trigger.** What triggered the regulator's question? *Rubric:* 3 = unreviewed exceptions in the supplier's assurance report;; 2 = exceptions;; 1 = vague;; 0 = none.
- **EX037 — Process failure.** What was the process-level failure? *Rubric:* 3 = assurance reports received but not read;; 2 = unread;; 1 = vague;; 0 = none.
- **EX038 — Governance failure.** What was the governance-level failure? *Rubric:* 3 = nobody owned supplier risk and the board never saw it;; 2 = ownership;; 1 = vague;; 0 = none.
- **EX039 — Exception tracking.** How should supplier exceptions be handled? *Rubric:* 3 = tracked as findings;; 2 = findings;; 1 = ignored;; 0 = none.
- **EX040 — Success measure.** Give one measure of success Lena proposed. *Rubric:* 3 = share of critical suppliers with reviewed reports;; 2 = measure;; 1 = vague;; 0 = none.

### Synthesis

Case analysis reveals multi-level failures and patterns relevant to one's own organisation.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) write governance reports for executives and boards; (2) communicate bad news honestly; (3) handle pressure ethically.

### 9.1 Board reporting

Lena drafts Marston's quarterly security report to the board. It opens with decisions needed, then top risks against appetite, significant findings and their status, incidents and lessons, and supplier risk. It uses plain language and keeps to four pages. Each risk shows a trend and an owner. She learns that board reports should support oversight: directors need to know what is going wrong and what they are being asked to decide. A director who reads only the first page should still know which decisions are being asked of the board.

### 9.2 Bad news

The report must include the vendor management weakness. An executive suggests describing it as an improvement opportunity rather than a weakness. Lena explains that the board needs an accurate picture, and that softening language could mislead directors who have legal duties of oversight. She agrees to present the issue together with the remediation plan and progress. She learns that honest framing with a plan maintains trust better than euphemism. Presenting the vendor management weakness with its remediation plan lets the board judge progress rather than only learn of a problem.

### 9.3 Ethics

Later, a manager asks Lena to delay logging a finding until after the regulator's visit. She declines, explaining that the finding must be recorded when identified and that delaying it would mislead the regulator. She offers to help the manager prepare a remediation plan to present alongside it. She learns that professional ethics in GRC often means resisting small pressures to shape the record, and that offering help makes refusal easier to accept. Logging the finding when identified also protects the manager, since a later discovery of the delay would damage trust with the regulator.

### Worked example

Lena writes a decision-focused board report, presents a weakness honestly with a plan and declines to delay logging a finding.

> **Synthetic case.** The scenarios are synthetic.

### Errors and limits

Honest reports can strain relationships. Boards vary in engagement.

### Exercises

- **EX041 — Report opening.** What does Lena's board report open with? *Rubric:* 3 = decisions needed;; 2 = decisions;; 1 = risks;; 0 = none.
- **EX042 — Softening risk.** Why not call the weakness an improvement opportunity? *Rubric:* 3 = it could mislead directors with oversight duties;; 2 = honesty;; 1 = vague;; 0 = none.
- **EX043 — Honest framing.** How did Lena present the weakness? *Rubric:* 3 = with the remediation plan and progress;; 2 = plan;; 1 = vague;; 0 = none.
- **EX044 — Delay request.** What did a manager ask Lena to do? *Rubric:* 3 = delay logging a finding until after the regulator's visit;; 2 = delay;; 1 = vague;; 0 = none.
- **EX045 — Refusal help.** What did Lena offer instead? *Rubric:* 3 = help preparing a remediation plan;; 2 = help;; 1 = vague;; 0 = none.

### Synthesis

Honest, decision-focused reporting and resistance to pressure sustain trust in GRC.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Security governance, risk and compliance: quality and troubleshooting

### Learning outcomes

You will (1) measure the quality of the findings process; (2) identify ageing problems; (3) troubleshoot why findings stall.

### 10.1 Ageing

Lena checks how long open findings have been outstanding against their severity targets. The lab examines eight open findings. Of three high findings, two are past the thirty-day target, at forty-eight and ninety-five days. Of three medium findings, one is past ninety days at one hundred and thirty. Of two low findings, one is past one hundred and eighty days at two hundred. Four of eight findings are overdue, half of all open items. Ageing alone does not explain why these four stalled, which is why she turns to the owners next.

### Lab — Ageing of open findings by severity

```python
"""Ageing of open audit findings by severity (synthetic Marston data, days open)."""
f = [("high", 12), ("high", 95), ("medium", 40), ("medium", 130), ("medium", 75), ("low", 200), ("low", 15), ("high", 48)]
lim = {"high": 30, "medium": 90, "low": 180}
for s in ("high", "medium", "low"):
    a = [d for x, d in f if x == s]; over = [d for d in a if d > lim[s]]
    print(f"{s}: open {len(a)}, past {lim[s]}-day target {len(over)} {over}")
print(f"total open {len(f)}; overdue {sum(d > lim[s] for s, d in f)}")
```

Run with `python3 lab_age.py`. Verified output:

```text
high: open 3, past 30-day target 2 [95, 48]
medium: open 3, past 90-day target 1 [130]
low: open 2, past 180-day target 1 [200]
total open 8; overdue 4
```

### 10.2 Why findings stall

Lena interviews owners of the four overdue findings. The ninety-five-day high finding needs a supplier change the supplier has not prioritised. The forty-eight-day high finding has a fix ready but waiting for a change window. The medium finding's owner left Marston and nobody took it over. The low finding was considered unimportant and forgotten. She learns that ageing data show where to look, but conversations reveal causes, which differ for each finding. The orphaned medium finding, for example, needs a process fix, while the supplier issue needs contractual pressure.

### 10.3 Fixes

Lena proposes specific fixes: escalate the supplier issue through contract management, schedule an extra change window for the ready fix, reassign orphaned findings automatically when owners leave and review low findings quarterly so they are either fixed or formally accepted. She also suggests adding the reason for delay to each overdue finding in the committee report. She learns that improving process quality means addressing distinct causes rather than applying one general push. The added delay reasons also let the committee see whether the same cause keeps recurring.

### Worked example

Lena finds four of eight findings overdue, discovers four different causes through interviews and proposes a specific fix for each.

> **Synthetic case.** Findings and causes are synthetic.

### Errors and limits

Small numbers. Interviews may be defensive.

### Exercises

- **EX046 — Overdue count.** How many open findings were overdue? *Rubric:* 3 = four of eight;; 2 = 4/8;; 1 = vague;; 0 = none.
- **EX047 — High overdue.** Which high findings were overdue? *Rubric:* 3 = those at 48 and 95 days;; 2 = two;; 1 = vague;; 0 = none.
- **EX048 — Orphan cause.** Why did the medium finding stall? *Rubric:* 3 = its owner left and nobody took it over;; 2 = orphaned;; 1 = vague;; 0 = none.
- **EX049 — Orphan fix.** How will orphaned findings be prevented? *Rubric:* 3 = automatic reassignment when owners leave;; 2 = reassign;; 1 = vague;; 0 = none.
- **EX050 — Low finding fix.** How should low findings be handled? *Rubric:* 3 = reviewed quarterly to fix or formally accept;; 2 = quarterly;; 1 = vague;; 0 = none.

### Synthesis

Ageing data point to stalled findings, and conversations reveal distinct causes to fix.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) carry out a supervised assurance review of a synthetic supplier; (2) read an assurance report critically; (3) record findings.

### 11.1 The task

In the supervised laboratory, Lena reviews a synthetic SOC 2 type two report from a fictional card processing supplier. Mr. Reyes asks her to determine whether the report covers the services Marston uses, whether the period is current, what exceptions were noted and which complementary controls Marston must operate itself. She uses a checklist based on the AICPA trust services criteria categories, without treating the synthetic report as a real attestation. Mr. Reyes adds that each of these questions changes how much Marston can rely on the report, so none can be skipped.

### 11.2 Reading critically

Lena finds the report covers the card processing service but excludes the fraud monitoring module Marston also uses. The period ended nine months ago. Two exceptions appear: delayed removal of leavers' access and one missed quarterly vulnerability scan. The report lists complementary user entity controls, including that Marston must review its own users' access to the supplier's portal. She notes that Marston has never done this review. That missing portal review is a complementary user entity control, so the gap sits with Marston rather than with the supplier.

### 11.3 Findings

Lena records findings: the fraud module is outside the report's scope, so separate assurance is needed; the period is ageing, so a bridge letter should be requested; the two exceptions need follow-up with the supplier; and Marston must start reviewing its own portal users. Mr. Reyes confirms her analysis and notes that complementary controls are often missed because organisations assume the supplier handles everything. Each of these four items is then logged in her findings workflow with an owner, a severity and a target date.

### Worked example

Lena reviews a synthetic SOC 2 report, finds a scope gap, an ageing period, two exceptions and an unperformed complementary control.

> **Synthetic case.** The report and supplier are synthetic; AICPA trust services criteria are real; this is not an attestation.

### Errors and limits

Reports have limited scope. Bridge letters give limited assurance.

### Exercises

- **EX051 — Scope gap.** What was outside the report's scope? *Rubric:* 3 = the fraud monitoring module;; 2 = fraud module;; 1 = vague;; 0 = none.
- **EX052 — Ageing period.** Why request a bridge letter? *Rubric:* 3 = the report period ended nine months ago;; 2 = ageing;; 1 = vague;; 0 = none.
- **EX053 — Exceptions.** Which two exceptions did the report note? *Rubric:* 3 = delayed leaver removal and a missed vulnerability scan;; 2 = two;; 1 = vague;; 0 = none.
- **EX054 — Complementary control.** Which complementary control had Marston never performed? *Rubric:* 3 = reviewing its own users' access to the supplier portal;; 2 = portal review;; 1 = vague;; 0 = none.
- **EX055 — Common mistake.** Why are complementary controls often missed? *Rubric:* 3 = organisations assume the supplier handles everything;; 2 = assumption;; 1 = vague;; 0 = none.

### Synthesis

Critical reading of assurance reports finds scope gaps, exceptions and duties left with the customer.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a practice portfolio; (2) reflect on competence gained; (3) plan next steps in GRC practice.

### 12.1 Portfolio

Lena assembles her portfolio: the stakeholder map and purpose statement, the mobile app risk assessment, the self-assessment comparison, the findings workflow and ageing analysis, the sampled control test, the board report and the supplier report review. For each she writes a short note on what she did, what evidence supports it and what she learned. She removes any real member or staff data, keeping only synthetic or anonymised material. Each note links an artefact to the chapter in which it was produced, so assessors can trace her reasoning.

### 12.2 Final review

Mr. Reyes and a second assessor review the portfolio. They ask how she would handle a regulator questioning her sample size; she explains the tolerable rate and confidence and offers to extend the sample if needed. They ask what she found hardest; she says resisting pressure to soften reports while keeping good relationships. They judge her competent and note her strength in linking evidence to conclusions. The sample-size question shows why she recorded the tolerable rate and confidence when she ran the test in chapter 7.

### 12.3 Next steps

Lena plans her next steps: take on supplier risk ownership at Marston, deepen her knowledge of ISO/IEC 27001:2022 to support a possible certification and mentor a junior colleague in evidence handling. She commits to reviewing her methods yearly as standards and threats change. Mr. Reyes reminds her that GRC practice depends on judgement, honesty and steady follow-through as much as on frameworks. Taking on supplier risk ownership also closes the governance gap she identified in the peer credit union case.

### Worked example

Lena assembles a seven-item portfolio, answers assessors on sampling and pressure and plans her next steps.

> **Synthetic case.** The portfolio is synthetic; ISO/IEC 27001:2022 is real.

### Errors and limits

Portfolios show selected work. Plans change with roles.

### Exercises

- **EX056 — Portfolio note.** What note accompanies each portfolio item? *Rubric:* 3 = what she did, supporting evidence, what she learned;; 2 = note;; 1 = vague;; 0 = none.
- **EX057 — Data in portfolio.** What data did Lena remove from the portfolio? *Rubric:* 3 = real member or staff data;; 2 = real data;; 1 = vague;; 0 = none.
- **EX058 — Sample challenge.** How would Lena answer a regulator questioning her sample size? *Rubric:* 3 = explain tolerable rate and confidence, offer to extend;; 2 = explain;; 1 = vague;; 0 = none.
- **EX059 — Hardest part.** What did Lena find hardest? *Rubric:* 3 = resisting pressure to soften reports while keeping relationships;; 2 = pressure;; 1 = vague;; 0 = none.
- **EX060 — Next role.** Which ownership will Lena take on next? *Rubric:* 3 = supplier risk;; 2 = supplier risk, without explanation;; 1 = vague;; 0 = none.

### Synthesis

A practice portfolio demonstrates competence and sets direction for continuing GRC practice.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Lena Hoffmann, Mr. Victor Reyes, Ashby Professional Academy, Marston Credit Union and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Confidentiality and integrity.

**EX002.** Because members expect to reach their accounts at any time.

**EX003.** Call centre staff.

**EX004.** Controls not checked for effectiveness and risk decisions made informally by IT (also weak board reports).

**EX005.** Because compliance discipline is a strong foundation for broader governance work.

**EX006.** Sound risk management and timely incident reporting.

**EX007.** PCI DSS v4.0 obligations to protect cardholder data.

**EX008.** Where Marston has no clear way to show it meets an expectation.

**EX009.** To keep security risk within appetite, meet obligations and give stakeholders reliable evidence.

**EX010.** For example, no overdue high-severity findings (or top risks within appetite, clean regulatory reviews).

**EX011.** Change systems or approve exceptions herself.

**EX012.** Only when needed for a specific review, with approval and logging.

**EX013.** A restricted folder, consistent naming, recorded sources and removal of unneeded member details.

**EX014.** She was asked to assess procedures she had written herself.

**EX015.** She disclosed it and asked a colleague to review that area.

**EX016.** Establish context, identify, analyse, evaluate, treat, and monitor and review.

**EX017.** Account takeover leading to member financial losses.

**EX018.** When recovered within four hours.

**EX019.** Stronger authentication for new payees and transaction monitoring.

**EX020.** To show regulators and auditors that risks were considered and managed deliberately.

**EX021.** It tends to be optimistic.

**EX022.** Vendor management, with a gap of 1.33.

**EX023.** Because restore tests produce clear evidence.

**EX024.** Because contracts included security clauses, but nobody checked whether suppliers complied.

**EX025.** Tightening rating definitions to require evidence and focusing review on the largest gaps.

**EX026.** Lena checks evidence before closing the finding.

**EX027.** Thirty days.

**EX028.** With an agreed interim measure and a longer realistic plan.

**EX029.** Overdue high-severity findings.

**EX030.** To the owner's executive.

**EX031.** Fifty-nine.

**EX032.** Ninety-nine.

**EX033.** Because new-payee authentication protects member funds, so a tight rate is appropriate.

**EX034.** That the authentication log showed a successful second factor before the payment.

**EX035.** It covers the app channel only (and shows authentication occurred, not resistance to all attacks).

**EX036.** Exceptions in the supplier's assurance report that nobody followed up.

**EX037.** Assurance reports were received but not read.

**EX038.** Nobody owned supplier risk and the board never saw it reported.

**EX039.** Tracked as findings through the workflow.

**EX040.** The share of critical suppliers with reviewed reports (or time to follow up exceptions).

**EX041.** The decisions the board is asked to make.

**EX042.** Because softening language could mislead directors who have legal duties of oversight.

**EX043.** Together with the remediation plan and progress.

**EX044.** Delay logging a finding until after the regulator's visit.

**EX045.** Help preparing a remediation plan to present with the finding.

**EX046.** Four of eight.

**EX047.** Two, at 48 and 95 days.

**EX048.** Its owner left Marston and nobody took it over.

**EX049.** By automatically reassigning findings when owners leave.

**EX050.** Reviewed quarterly so they are either fixed or formally accepted.

**EX051.** The fraud monitoring module Marston also uses.

**EX052.** Because the report period ended nine months earlier.

**EX053.** Delayed removal of leavers' access and one missed quarterly vulnerability scan.

**EX054.** Reviewing its own users' access to the supplier's portal.

**EX055.** Because organisations assume the supplier handles everything.

**EX056.** What she did, the evidence supporting it and what she learned.

**EX057.** Any real member or staff data, keeping only synthetic or anonymised material.

**EX058.** By explaining the tolerable rate and confidence level and offering to extend the sample.

**EX059.** Resisting pressure to soften reports while keeping good relationships.

**EX060.** Supplier risk ownership at Marston.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- International Organization for Standardization. (2018). *ISO 31000:2018 Risk management — Guidelines*. <https://www.iso.org/standard/65694.html>
- International Organization for Standardization. (2022a). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022c). *ISO/IEC 27005:2022 Information security, cybersecurity and privacy protection — Guidance on managing information security risks*. <https://www.iso.org/standard/80585.html>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
