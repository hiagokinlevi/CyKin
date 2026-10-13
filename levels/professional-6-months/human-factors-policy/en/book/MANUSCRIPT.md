# Human Factors and Cyber Policy: Professional Course

- Language: English (`en`); course 029, Professional course (6 months).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; five offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working practitioners moving into security coordinator roles who support staff reporting, verification procedures and honest reporting to leaders.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs count survey barriers, compute verdict times, tally near-miss factors, chart monthly reports and compare two verdict versions, all on synthetic data; no real staff, tenants, emails or accounts are involved. Procedures are practised by announced role-play and tested with volunteers who know the purpose. The book recommends no simulated phishing in the first year; any later simulation must be announced, agreed with staff representatives, avoid lures about pay, housing or health, give kind feedback, stay aggregate and stay out of performance processes. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one practitioner through a six-month course while becoming security coordinator at a housing association: foundations, context, authorised practice, methods, tools, workflow, controls, case analysis, communication and ethics, quality, a supervised laboratory and a portfolio review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Grace Mwangi** | Security coordinator and course participant | Invented |
| **Alan Pryce** | Mentor | Invented |
| **Harlow Professional Academy** | Fictional training provider | Invented |
| **Ferngate Housing Association** | Fictional housing association, 180 staff | Invented |

### Core sources

Adams and Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff and Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Cialdini (2021); Bada, Sasse and Nurse (2019), arXiv:1901.02672; Lain, Kostiainen and Čapkun (2022), [doi:10.1109/SP46214.2022.9833766](https://doi.org/10.1109/SP46214.2022.9833766). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) explain core security ideas in human terms; (2) describe the practitioner's role in human-centred security; (3) set personal learning goals.

### 1.1 Core ideas

Grace Mwangi, an office manager moving into a security coordinator role, enrols in a six-month professional course at the fictional Harlow Professional Academy. Her mentor, Alan Pryce, starts with core ideas: confidentiality, integrity and availability; threats and vulnerabilities; and controls that reduce risk. He explains each through examples from her employer, the fictional Ferngate Housing Association, which has 180 staff and holds tenant records and rent payments. A fake email that changes a contractor's bank details threatens integrity and money; a lost laptop threatens confidentiality.

### 1.2 The practitioner's role

Alan explains that Grace's new role sits between staff, managers and the IT supplier. She will help staff report suspicious messages, run short learning sessions, check that verification procedures are followed and report to managers. Adams and Sasse (1999) showed that users are not the enemy, and Sasse, Brostoff and Weirich (2001) argued that the weakest-link view should be transformed by design. Grace's role is to make secure behaviour easy and welcome, not to police colleagues, which suits her background in supporting people.

### 1.3 Learning goals

Grace sets learning goals: understand common attacks on housing associations, learn simple measurement, write clear procedures and handle ethical questions such as simulations. Alan suggests she keep a portfolio of work, including procedures she writes, data she analyses and reflections on cases. The portfolio will be reviewed in the final chapter. Setting goals early helps her focus during a short course and gives her a way to judge her own progress against concrete outcomes rather than vague impressions. Alan agrees to the goals.

### Worked example

Grace learns core security ideas through Ferngate examples, defines her coordinator role as enabling rather than policing and sets learning goals with a portfolio.

> **Synthetic case.** Ferngate is synthetic; Adams and Sasse (1999) and Sasse et al. (2001) are real.

### Errors and limits

Roles can drift into enforcement. Goals need revisiting.

### Exercises

- **EX001 — Integrity example.** Which Ferngate example threatens integrity? *Rubric:* 3 = a fake email changing a contractor's bank details;; 2 = bank change;; 1 = lost laptop;; 0 = none.
- **EX002 — Role position.** Between whom does Grace's role sit? *Rubric:* 3 = staff, managers and the IT supplier;; 2 = three groups;; 1 = none;; 0 = none.
- **EX003 — Role purpose.** What is the purpose of Grace's role? *Rubric:* 3 = make secure behaviour easy and welcome;; 2 = enabling;; 1 = policing;; 0 = none.
- **EX004 — Weakest link.** What did Sasse, Brostoff and Weirich (2001) argue? *Rubric:* 3 = the weakest-link view should be transformed by design;; 2 = design;; 1 = blame;; 0 = none.
- **EX005 — Portfolio.** What will Grace's portfolio contain? *Rubric:* 3 = procedures, analyses and reflections;; 2 = portfolio;; 1 = none;; 0 = none.

### Synthesis

Practitioners translate security ideas into human terms and enable rather than police.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Human factors and cyber policy: service and stakeholder context

### Learning outcomes

You will (1) map Ferngate's services and stakeholders; (2) identify where people face security decisions; (3) understand stakeholder concerns.

### 2.1 Services and people

Grace maps Ferngate's services: tenancy management, repairs, rent collection and community support. Stakeholders include tenants, staff, repair contractors, the IT supplier, the board and the housing regulator. Staff often work remotely, visiting tenants with tablets, and use email and a housing management system. Tenants contact Ferngate by phone, email and an online portal. Each relationship creates opportunities for impersonation, such as fake contractors asking for payment or callers pretending to be tenants to obtain information about a neighbour. She draws the map on one page.

### 2.2 Decision points

Grace lists points where staff face security decisions: answering phone requests for tenant information, approving contractor invoices, opening attachments from tenants and logging into the system on shared tablets. She talks to five colleagues about recent difficult moments. A housing officer describes a caller claiming to be a tenant's son asking for her new address. A finance assistant describes an urgent invoice from a contractor's lookalike address. These conversations ground her work in real pressures rather than abstract threats. She writes each story without names.

### 2.3 Stakeholder concerns

Grace interviews stakeholders about their concerns. Managers worry about fraud and regulator scrutiny. Staff worry about being blamed for mistakes and about extra work. Tenants, through a tenants' panel, worry about privacy and want to be sure Ferngate will not ask for bank details by email. The IT supplier worries about unclear requests from staff. She records concerns in a simple table. Understanding concerns helps her design changes that answer them, making support more likely across groups. Managers review the table.

### Worked example

Grace maps services and stakeholders, records decision points from colleagues' stories and tabulates stakeholder concerns.

> **Synthetic case.** All details are synthetic.

### Errors and limits

Interviews reflect few voices. Concerns change.

### Exercises

- **EX006 — Remote work.** How do housing officers often work? *Rubric:* 3 = remotely with tablets visiting tenants;; 2 = mobile;; 1 = none;; 0 = none.
- **EX007 — Caller example.** What did the fake son caller want? *Rubric:* 3 = a tenant's new address;; 2 = address;; 1 = none;; 0 = none.
- **EX008 — Staff concern.** What do staff worry about? *Rubric:* 3 = blame and extra work;; 2 = two;; 1 = fraud;; 0 = none.
- **EX009 — Tenant concern.** What do tenants want assurance about? *Rubric:* 3 = Ferngate never asks for bank details by email;; 2 = email;; 1 = none;; 0 = none.
- **EX010 — Concerns table.** Why record stakeholder concerns? *Rubric:* 3 = to design changes that answer them;; 2 = design input;; 1 = none;; 0 = none.

### Synthesis

Service and stakeholder context shows where people decide and what they worry about.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) work within written authorisation; (2) handle evidence from reports safely; (3) protect privacy in security work.

### 3.1 Authorisation

Alan explains that security coordinators must act within written authorisation. Grace obtains a short mandate from Ferngate's chief executive describing what she may do: manage the reporting mailbox, review reported messages with the IT supplier, run learning sessions and review verification logs. It states what she may not do: read staff mailboxes, monitor individuals or run deceptive tests without approval from managers and staff representatives. Authorisation protects Grace, colleagues and Ferngate by making boundaries clear before any problem arises. She keeps a signed copy.

### 3.2 Handling evidence

Reported messages are evidence of attacks. Grace learns to handle them safely: never click links or open attachments from reports on her normal computer; forward suspicious items to the IT supplier using the agreed method; record the date, type and outcome without copying personal details; and keep records in a restricted folder. If a report suggests a serious incident, such as a tenant data leak, she follows the incident plan and preserves information as the IT supplier advises, rather than investigating alone.

### 3.3 Protecting privacy

Reports sometimes contain tenant details or personal messages. Grace removes personal details from summaries and keeps original reports only as long as needed. She does not record who reported what in any summary shared with managers. She explains to managers that this protects tenants' privacy and encourages staff to report without fear of being judged. Privacy protection is part of authorised practice, because security work must not create new harms while trying to prevent others. Managers agree with this approach. Alan agrees.

### Worked example

Grace obtains a mandate with clear limits, handles reported messages safely and removes personal details from summaries.

> **Synthetic case.** The mandate is synthetic.

### Errors and limits

Mandates need updating. Evidence handling needs supplier support.

### Exercises

- **EX011 — Mandate limit.** Name one thing Grace may not do. *Rubric:* 3 = read staff mailboxes;; 2 = monitoring;; 1 = review reports;; 0 = none.
- **EX012 — Safe handling.** What must Grace never do with reported items? *Rubric:* 3 = click links or open attachments on her computer;; 2 = no clicking;; 1 = none;; 0 = none.
- **EX013 — Serious incident.** What does Grace do if a report suggests a serious incident? *Rubric:* 3 = follow the incident plan and supplier advice;; 2 = plan;; 1 = investigate alone;; 0 = none.
- **EX014 — Summary rule.** What is excluded from summaries for managers? *Rubric:* 3 = who reported what;; 2 = reporter identity;; 1 = none;; 0 = none.
- **EX015 — Privacy reason.** Why does privacy encourage reporting? *Rubric:* 3 = staff do not fear being judged;; 2 = trust;; 1 = none;; 0 = none.

### Synthesis

Authorised practice sets boundaries, handles evidence safely and protects privacy.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Human factors and cyber policy: core methods

### Learning outcomes

You will (1) run a short anonymous survey; (2) hold structured conversations; (3) turn findings into priorities.

### 4.1 A short survey

Grace runs a six-question anonymous survey asking staff whether they know how to report, what stops them, whether they have heard back after reporting, how confident they feel about phone requests and how much security effort they spend weekly. The tenants' panel reviews a separate two-question version for tenants. She receives 126 staff responses from 180. The lab counts the barriers staff selected. She shares headline results with all staff within two weeks, explaining what will happen next. The survey is anonymous. Staff representatives approve it.

### Lab — Barriers among 126 staff responses

```python
# Barriers among 126 synthetic staff responses (multiple choice).
b = {"unsure if worth reporting": 51, "never heard back": 38, "don't know how": 33, "too busy": 27, "fear of blame": 15}
for k, v in sorted(b.items(), key=lambda x: -x[1]): print(f"{k}: {v}/126 = {v / 126:.0%}")
```

Run with `python3 lab_barriers.py`. Verified output:

```text
unsure if worth reporting: 51/126 = 40%
never heard back: 38/126 = 30%
don't know how: 33/126 = 26%
too busy: 27/126 = 21%
fear of blame: 15/126 = 12%
```

### 4.2 Structured conversations

Grace holds eight structured conversations of fifteen minutes with staff from different teams, using the same five questions each time and taking notes without names. Housing officers describe uncertainty about phone requests from relatives. Finance staff describe pressure from contractors demanding urgent payment. Several people say they reported a suspicious email once and never heard back. Structured conversations add reasons and stories to the survey numbers, while consistent questions make it easier to compare answers across teams. Notes are checked with each person.

### 4.3 Setting priorities

Grace combines findings into three priorities: make reporting easy with a button and quick replies; provide a clear procedure for phone requests about tenants; and introduce callback verification for contractor bank detail changes. Each priority answers both a common barrier and a stakeholder concern from chapter 2. She presents the priorities to managers with the evidence behind them. Managers approve them and assign a small budget, impressed that the priorities came from staff experience rather than generic advice. Work begins within a month.

### Worked example

Grace surveys 126 staff, holds eight structured conversations and sets three evidence-based priorities.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Self-report bias. Eight conversations are few.

### Exercises

- **EX016 — Response rate.** What was the staff response rate? *Rubric:* 3 = 70%;; 2 = 126 of 180;; 1 = 126%;; 0 = none.
- **EX017 — Lab top barrier.** What was the top barrier in the lab? *Rubric:* 3 = unsure if worth reporting, 51 of 126;; 2 = uncertainty;; 1 = none;; 0 = none.
- **EX018 — Consistent questions.** Why use the same questions in every conversation? *Rubric:* 3 = to compare answers across teams;; 2 = comparability;; 1 = none;; 0 = none.
- **EX019 — Phone priority.** Which priority addresses phone requests? *Rubric:* 3 = a clear procedure for phone requests about tenants;; 2 = procedure;; 1 = none;; 0 = none.
- **EX020 — Results sharing.** When did Grace share headline results with staff? *Rubric:* 3 = within two weeks;; 2 = two weeks;; 1 = never;; 0 = none.

### Synthesis

Simple surveys and structured conversations produce priorities grounded in staff experience.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Human factors and cyber policy: tools and interpretation

### Learning outcomes

You will (1) use simple tools to track reports and verdicts; (2) interpret basic measures correctly; (3) avoid misleading comparisons.

### 5.1 Simple tools

Grace uses a spreadsheet and a short Python script provided by the course to track reports. Each row holds date, team, category, verdict and the time the verdict was sent, with no reporter names. The script computes monthly counts, the share of reports that were malicious and the median time to verdict. She learns to check the script's output against a few rows counted by hand, which builds confidence that the tool is working correctly before she shares figures with managers.

### 5.2 Interpreting measures

Grace learns to interpret measures carefully. A rise in reports may mean more attacks or more willingness to report; she checks the IT supplier's filter logs to see which. A low share of malicious reports may mean staff report too much, but Alan explains that over-reporting is a healthy sign in a new programme, because it shows people feel safe to ask. The lab computes the median time to verdict before and after replies were templated, showing a large improvement. She records both checks.

### Lab — Median time to verdict before and after templates

```python
# Median hours to verdict before and after templated replies (synthetic).
before = [4, 9, 18, 22, 26, 30, 41, 48, 70]; after = [0.5, 1, 1.5, 2, 3, 3.5, 5, 6, 20]
m = lambda x: sorted(x)[len(x) // 2]
print(f"before: median {m(before)} h; after: median {m(after)} h")
```

Run with `python3 lab_verdict.py`. Verified output:

```text
before: median 26 h; after: median 3 h
```

### 5.3 Misleading comparisons

Grace avoids comparisons that mislead. She does not rank teams by report counts, because team sizes and exposure differ, and rankings would shame some groups. She reports figures only for groups of at least twenty staff. She shows changes over time with the number of cases behind each figure. When a manager asks which team is worst, she explains why that question cannot be answered fairly from the data and offers a more useful question: where do people need more support?

### Worked example

Grace tracks reports with a spreadsheet and script, interprets rises and over-reporting correctly and avoids unfair team rankings.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Small numbers vary. Scripts need checking after changes.

### Exercises

- **EX021 — Hand check.** Why check script output by hand? *Rubric:* 3 = to confirm the tool works before sharing;; 2 = verification;; 1 = none;; 0 = none.
- **EX022 — Report rise.** What two things could a rise in reports mean? *Rubric:* 3 = more attacks or more willingness;; 2 = two causes;; 1 = none;; 0 = none.
- **EX023 — Over-reporting.** How does Alan view over-reporting in a new programme? *Rubric:* 3 = as a healthy sign of feeling safe;; 2 = healthy;; 1 = problem;; 0 = none.
- **EX024 — Lab verdict times.** How did median time to verdict change with templates? *Rubric:* 3 = 26 hours before and 3 hours after templates;; 2 = faster;; 1 = none;; 0 = none.
- **EX025 — Better question.** What question did Grace offer instead of which team is worst? *Rubric:* 3 = where people need more support;; 2 = support;; 1 = none;; 0 = none.

### Synthesis

Simple tools give useful measures when interpreted carefully and fairly.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Human factors and cyber policy: operational workflow

### Learning outcomes

You will (1) design the daily reporting workflow; (2) set response times and responsibilities; (3) handle peaks and absences.

### 6.1 Daily workflow

Grace designs the daily workflow. Staff report through a button that sends messages to a shared mailbox and shows a thank-you note. Twice a day, Grace or her backup reviews new reports, groups duplicates, sends clear harmless or spam verdicts using templates and forwards uncertain or malicious items to the IT supplier. The IT supplier confirms verdicts and removes malicious messages from all mailboxes. Grace records outcomes in the spreadsheet. The workflow takes about twenty minutes a day on normal days.

### 6.2 Times and responsibilities

Grace sets targets: a thank-you instantly, a verdict within one working day and removal of confirmed malicious messages within two hours of confirmation. She writes down who does each step: Grace for triage, a named backup when she is away, the IT supplier for analysis and removal, and the finance manager for any payment-related reports. Clear responsibilities stop reports falling between people, which interviews showed had happened before when nobody was sure who should reply. Managers approve the targets. Each owner signs.

### 6.3 Peaks and absences

During attack campaigns, reports can multiply. Grace plans for peaks: when more than twenty reports arrive about one message, she sends a short message to all staff saying the message is known and being removed, which reduces duplicate reports and reassures people. For absences, her backup has a short runbook and access to the mailbox. She tests the backup arrangement by taking a planned day off during a normal week and reviewing what happened afterwards. The test goes smoothly. Nothing is missed.

### Worked example

Grace designs a twice-daily triage workflow with templates, sets response targets and named responsibilities and plans for campaign peaks and absences.

> **Synthetic case.** The workflow is synthetic.

### Errors and limits

Twice-daily review may be slow during campaigns. Backups need practice.

### Exercises

- **EX026 — Daily time.** How long does the workflow take on normal days? *Rubric:* 3 = about twenty minutes;; 2 = 20 minutes;; 1 = none;; 0 = none.
- **EX027 — Verdict target.** What is the verdict target? *Rubric:* 3 = within one working day;; 2 = one day;; 1 = none;; 0 = none.
- **EX028 — Payment reports.** Who handles payment-related reports? *Rubric:* 3 = the finance manager;; 2 = finance;; 1 = Grace alone;; 0 = none.
- **EX029 — Peak message.** What does Grace send during campaigns? *Rubric:* 3 = a message saying the email is known and being removed;; 2 = all-staff notice;; 1 = none;; 0 = none.
- **EX030 — Backup test.** How did Grace test the backup arrangement? *Rubric:* 3 = taking a planned day off and reviewing afterwards;; 2 = planned absence;; 1 = none;; 0 = none.

### Synthesis

A clear workflow with targets, owners and plans for peaks keeps reporting reliable.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Human factors and cyber policy: controls and verification

### Learning outcomes

You will (1) introduce a phone request procedure and contractor callback control; (2) verify that controls work in practice; (3) adjust controls after feedback.

### 7.1 Phone procedure

Grace writes a procedure for phone requests about tenants: staff never share a tenant's address, contact details or circumstances by phone with anyone other than the verified tenant; requests from relatives, agencies or officials are taken in writing and passed to the data protection lead. A short script helps staff decline politely: I cannot share that by phone, but I can pass your request to our data team. The procedure removes the need to judge whether a caller sounds genuine, which attackers exploit.

### 7.2 Callback control

With the finance manager, Grace introduces a callback control. Any request to change a contractor's bank details is held until a second person calls the contractor using the number already in Ferngate's records. The finance system blocks payment to new details until the callback is logged. Contractors receive a letter explaining the rule. Cialdini (2021) describes how authority and urgency pressure people; the control means that no single person has to resist that pressure alone under deadline. Most contractors reply positively. Finance agrees.

### 7.3 Verification and adjustment

Grace verifies both controls. She checks the finance log monthly and confirms that every bank detail change has a callback recorded. She asks five housing officers to practise the phone script in announced role-play with a colleague acting as a caller. All use the script correctly after one practice, but two say the script sounds abrupt to elderly tenants' relatives. Grace adjusts it to add a sentence explaining that the rule protects their family member. Verification and feedback improve controls together.

### Worked example

Grace writes a phone request procedure with a script, sets up a contractor callback control and verifies both, adjusting the script after role-play feedback.

> **Synthetic case.** Procedures are synthetic; Cialdini (2021) is real.

### Errors and limits

Scripts can sound cold. Contractor records may be outdated.

### Exercises

- **EX031 — Phone rule.** What may staff not share by phone? *Rubric:* 3 = tenant address, contact details or circumstances;; 2 = tenant data;; 1 = none;; 0 = none.
- **EX032 — Callback number.** Which number is used for callbacks? *Rubric:* 3 = the number in Ferngate's records;; 2 = records;; 1 = request;; 0 = none.
- **EX033 — Pressure principles.** Which pressures does the callback control relieve? *Rubric:* 3 = authority and urgency;; 2 = Cialdini;; 1 = none;; 0 = none.
- **EX034 — Role-play.** How was the phone script tested? *Rubric:* 3 = announced role-play with a colleague as caller;; 2 = role-play;; 1 = secret test;; 0 = none.
- **EX035 — Script change.** Why was the script adjusted? *Rubric:* 3 = it sounded abrupt to relatives;; 2 = tone;; 1 = none;; 0 = none.

### Synthesis

Controls remove hard judgements, and verification with feedback improves them.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Human factors and cyber policy: supervised case analysis

### Learning outcomes

You will (1) analyse a security near miss without blame; (2) identify contributing factors; (3) recommend improvements under supervision.

### 8.1 The near miss

A finance assistant received an invoice from a lookalike of a roofing contractor's email address, with new bank details and a request for payment that day because of a supposed cash flow problem. She started to update the details but the finance system blocked payment pending callback. The callback revealed the request was fake. Grace analyses the near miss with Alan's supervision. The assistant had reported it immediately when the callback failed, and she is thanked publicly by the finance manager.

### 8.2 Contributing factors

Grace identifies factors without blaming the assistant. The lookalike domain passed email checks; the external tag was present but easy to miss on a busy screen; the request used urgency and a plausible story; and month-end workload left little time. The callback control worked as designed. She notes that the assistant behaved reasonably under pressure and that the system caught the fraud, which is exactly how layered defences should work. The lab tallies factors across this and three other near misses that year.

### Lab — Contributing factors across four near misses

```python
# Contributing factors across four near misses (synthetic).
nm = [{"urgency", "lookalike domain", "workload"}, {"urgency", "authority"}, {"urgency", "lookalike domain"}, {"urgency", "workload", "authority"}]
for f in ("urgency", "lookalike domain", "workload", "authority"): print(f, sum(f in s for s in nm), "of 4")
```

Run with `python3 lab_nearmiss.py`. Verified output:

```text
urgency 4 of 4
lookalike domain 2 of 4
workload 2 of 4
authority 2 of 4
```

### 8.3 Recommendations

Grace recommends making the external tag more visible in the finance mailbox, sending contractors a reminder that Ferngate always calls back, and sharing the case anonymously in the next learning session as a success story. Alan reviews the analysis and suggests adding a note on how the callback log helped. Sharing near misses as successes encourages reporting and shows staff that the system is designed to support them. The finance manager approves all recommendations. Work starts the next week. Staff are told.

### Worked example

Grace analyses a fake invoice near miss caught by callback, finds factors without blame and recommends visible tags, reminders and sharing the success.

> **Synthetic case.** The case is synthetic.

### Errors and limits

Near-miss sets are small. Success stories can encourage complacency.

### Exercises

- **EX036 — What stopped payment.** What stopped the fake payment? *Rubric:* 3 = the finance system blocked it pending callback;; 2 = callback;; 1 = the assistant;; 0 = none.
- **EX037 — Story used.** What story did the fake invoice tell? *Rubric:* 3 = a cash flow problem requiring same-day payment;; 2 = urgency;; 1 = none;; 0 = none.
- **EX038 — Lab top factor.** Which factor appeared in all four near misses in the lab? *Rubric:* 3 = urgency;; 2 = urgency;; 1 = workload;; 0 = none.
- **EX039 — Tag issue.** What problem did the external tag have? *Rubric:* 3 = easy to miss on a busy screen;; 2 = visibility;; 1 = none;; 0 = none.
- **EX040 — Sharing approach.** How will the case be shared? *Rubric:* 3 = anonymously as a success story;; 2 = success;; 1 = blame;; 0 = none.

### Synthesis

Blameless analysis shows layered defences working and turns near misses into learning.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) communicate security messages without fear; (2) decide ethically about simulations; (3) report to managers and the board.

### 9.1 Communicating without fear

Grace writes short monthly messages for staff with one recent example, one simple action and thanks for reports. She avoids frightening images and threats of discipline. Bada, Sasse and Nurse (2019) found that fear-based campaigns often fail. She also writes a short notice for tenants on the website and in newsletters: Ferngate will never ask for bank details by email or text, and tenants can call the main number to check. Messages focus on what people can do, which builds confidence. Staff like them.

### 9.2 Simulation decision

Managers ask whether Ferngate should run simulated phishing. Grace considers the evidence, including Lain, Kostiainen and Čapkun (2022), which found that some common simulation practices did not help. She recommends no simulations in the first year while reporting and controls bed in. If simulations are used later, they must follow rules agreed with staff representatives: announced programme, no lures about pay, housing or health, immediate kind feedback, aggregate results and no use in performance processes. Managers accept her recommendation. The decision is recorded in the minutes.

### 9.3 Reporting upwards

Grace reports quarterly to managers and annually to the board. Reports include outcome measures, such as the share of suspicious messages reported and time to verdict, controls verified, near misses and staff burden. She states limits honestly and avoids claiming that Ferngate is fully protected. The board asks good questions about contractor fraud and tenant privacy, which Grace answers using her evidence. Clear reporting builds trust between the coordinator and leaders, which secures support for the programme. The board thanks her.

### Worked example

Grace writes fear-free staff and tenant messages, recommends no simulations in year one with strict rules thereafter and reports outcomes honestly to managers and the board.

> **Synthetic case.** Communications are synthetic; Bada et al. (2019) and Lain et al. (2022) are real.

### Errors and limits

Monthly messages can become routine. Board attention varies.

### Exercises

- **EX041 — Message parts.** What does each monthly message contain? *Rubric:* 3 = an example, an action and thanks;; 2 = three;; 1 = warnings;; 0 = none.
- **EX042 — Tenant notice.** What does the tenant notice promise? *Rubric:* 3 = Ferngate never asks for bank details by email or text;; 2 = never;; 1 = none;; 0 = none.
- **EX043 — Simulation recommendation.** What did Grace recommend for year one? *Rubric:* 3 = no simulations;; 2 = none;; 1 = monthly;; 0 = none.
- **EX044 — Banned lure topics.** Which lure topics are banned if simulations are used later? *Rubric:* 3 = pay, housing or health;; 2 = distress;; 1 = none;; 0 = none.
- **EX045 — Report contents.** What do Grace's reports include? *Rubric:* 3 = outcomes, verified controls, near misses and burden;; 2 = outcomes;; 1 = activities;; 0 = none.

### Synthesis

Communication without fear, careful simulation decisions and honest reporting sustain trust.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Human factors and cyber policy: quality and troubleshooting

### Learning outcomes

You will (1) check the quality of the reporting service; (2) troubleshoot a problem; (3) improve the service continuously.

### 10.1 Quality checks

Grace checks quality monthly: are verdicts sent within one working day; are verdicts correct; are reports from all teams arriving; and are templates clear? She samples ten verdicts each month and asks the IT supplier to confirm them. She also asks two reporters each month, chosen at random, whether the reply was helpful. Quality checks catch slow drift, such as templates becoming outdated or replies becoming curt during busy periods, before staff lose confidence in the service. She logs each result.

### 10.2 Troubleshooting

In month four, reports from housing officers drop sharply. Grace checks the filter logs and finds no fall in suspicious messages. She asks two officers and learns that a tablet update removed the report button from the mail app. They had assumed reporting was no longer wanted. The IT supplier restores the button and adds a check after updates. Grace sends a message explaining the problem and thanking officers. The lab shows reports per month for housing officers, with the drop and the recovery.

### Lab — Housing officer reports by month

```python
# Housing officer reports by month (synthetic).
for m, n in enumerate([11, 14, 16, 2, 15, 17], 1): print(f"month {m}: {n}")
```

Run with `python3 lab_officers.py`. Verified output:

```text
month 1: 11
month 2: 14
month 3: 16
month 4: 2
month 5: 15
month 6: 17
```

### 10.3 Continuous improvement

Grace keeps an improvement log listing problems, causes, fixes and dates. She reviews it quarterly with Alan and the IT supplier, looking for patterns. Two entries involve updates removing settings, so the supplier adds a standard post-update checklist. One involves a confusing template, which she rewrites. Continuous improvement turns individual fixes into lasting changes, which is important in a small organisation where the same problems would otherwise recur whenever systems change or staff move on. Alan reads the log each quarter.

### Worked example

Grace runs monthly quality checks, traces a housing officer reporting drop to a tablet update and keeps an improvement log that leads to a post-update checklist.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Samples may miss problems. Logs need review.

### Exercises

- **EX046 — Quality questions.** Name two monthly quality questions. *Rubric:* 3 = verdict speed and correctness;; 2 = two;; 1 = none;; 0 = none.
- **EX047 — Drop cause.** What caused the housing officer drop? *Rubric:* 3 = a tablet update removed the report button;; 2 = update;; 1 = fewer attacks;; 0 = none.
- **EX048 — Lab drop.** How did housing officer reports move across the six months? *Rubric:* 3 = 14 and 16, then 2 in month four, then 15;; 2 = drop and recovery;; 1 = none;; 0 = none.
- **EX049 — Pattern found.** What pattern did the improvement log reveal? *Rubric:* 3 = updates removing settings;; 2 = updates;; 1 = none;; 0 = none.
- **EX050 — Supplier fix.** What did the supplier add? *Rubric:* 3 = a standard post-update checklist;; 2 = checklist;; 1 = none;; 0 = none.

### Synthesis

Quality checks and an improvement log turn fixes into lasting service improvements.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) test a change to verdict messages with volunteers; (2) compare understanding between versions; (3) decide on adoption.

### 11.1 The test

In the supervised laboratory, Grace tests two versions of the verdict message. Version A says only whether the message was malicious. Version B adds one sentence explaining the clue, such as a lookalike address or an unusual payment request. Twenty volunteers, who know the purpose, each read verdicts for five synthetic messages in a test environment, half seeing version A and half version B. Afterwards, each judges three new synthetic messages. Alan supervises, and volunteers can withdraw at any time. Each session lasts twenty minutes.

### 11.2 Comparing results

The lab compares correct judgements on the new messages between the two groups. Volunteers who read version B judge more messages correctly than those who read version A. Grace notes the small sample and that volunteers knew they were being asked to judge messages, which may make them more careful than usual. Still, the result is consistent with the idea that brief explanations help people learn from each report. She records the counts and the difference without overstating them. Alan reviews the analysis.

### Lab — Correct judgements after verdict versions A and B

```python
# Correct judgements of three new messages by ten volunteers per version (synthetic).
a = [2, 1, 2, 2, 1, 2, 3, 2, 1, 2]; b = [3, 2, 3, 3, 2, 3, 2, 3, 2, 2]
print(f"version A: {sum(a)}/30 correct; version B: {sum(b)}/30 correct")
```

Run with `python3 lab_versions.py`. Verified output:

```text
version A: 18/30 correct; version B: 25/30 correct
```

### 11.3 Adoption

Grace recommends adopting version B, since it costs only one sentence per verdict and may help staff learn. She updates templates with common clues and trains her backup to write short explanations. She plans to check after three months whether repeat reporting improves, using real data. Alan notes that she has followed a sound process: a clear question, a small fair test, honest analysis and a cheap change with follow-up, which is how practitioners should improve services. Managers approve the change.

### Worked example

Grace tests two verdict versions with twenty volunteers, finds better judgements after explanations and adopts version B with follow-up.

> **Synthetic case.** The test is synthetic.

### Errors and limits

Small sample. Volunteers knew the task.

### Exercises

- **EX051 — Version B.** What does version B add? *Rubric:* 3 = one sentence explaining the clue;; 2 = explanation;; 1 = none;; 0 = none.
- **EX052 — Lab result.** What did the lab show for correct judgements? *Rubric:* 3 = A 18 of 30, B 25 of 30;; 2 = B better;; 1 = none;; 0 = none.
- **EX053 — Caution.** Why might volunteers be more careful than usual? *Rubric:* 3 = they knew they would judge messages;; 2 = awareness;; 1 = none;; 0 = none.
- **EX054 — Cost.** What does version B cost? *Rubric:* 3 = one sentence per verdict;; 2 = low;; 1 = none;; 0 = none.
- **EX055 — Follow-up.** What follow-up did Grace plan? *Rubric:* 3 = check repeat reporting after three months;; 2 = follow-up;; 1 = none;; 0 = none.

### Synthesis

Small, fair tests support cheap improvements when followed up with real data.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a practice portfolio; (2) present outcomes and limits; (3) plan continuing professional development.

### 12.1 The portfolio

Grace assembles her portfolio: the mandate, stakeholder map, survey and conversation findings, procedures and scripts, workflow and runbook, near-miss analysis, quality log, laboratory report and quarterly reports. Each item has a short note explaining what it shows about her practice. Alan reviews it with her, checking that every item is free of personal details and that claims are supported by evidence. A portfolio shows not only what she did but how she reasoned, which matters for professional assessment. It is stored securely.

### 12.2 Outcomes and limits

Grace presents outcomes after six months: the share of suspicious messages reported rose; median time to verdict fell from about a day to a few hours; one fake invoice was stopped by callback; and staff burden stayed level. She presents limits: six months is short, numbers are small and some improvement may reflect novelty. Managers ask what she would do next; she suggests extending callback rules to tenant refund requests and reviewing the phone procedure with the tenants' panel. Managers agree.

### 12.3 Continuing development

Grace plans her continuing development: join a regional network of security coordinators in housing, read the annual Verizon DBIR and NIST SP 800-50r1 guidance, and complete a short course in data protection. Alan suggests she mentor a colleague as her backup, which also strengthens Ferngate's resilience. Grace reflects that her background in supporting people proved more useful than she expected, because human-centred security depends on trust, clear communication and practical help as much as on technical knowledge. Alan signs off her course.

### Worked example

Grace assembles a portfolio, presents six-month outcomes with limits and plans continuing development and mentoring.

> **Synthetic case.** Outcomes are synthetic; the DBIR and SP 800-50r1 are real.

### Errors and limits

Portfolios can be selective. Six months is short.

### Exercises

- **EX056 — Portfolio check.** What did Alan check in the portfolio? *Rubric:* 3 = no personal details and supported claims;; 2 = quality;; 1 = none;; 0 = none.
- **EX057 — Verdict time outcome.** How did median time to verdict change? *Rubric:* 3 = from about a day to a few hours;; 2 = faster;; 1 = none;; 0 = none.
- **EX058 — Next control.** What next control did Grace suggest? *Rubric:* 3 = callbacks for tenant refund requests;; 2 = refunds;; 1 = none;; 0 = none.
- **EX059 — Mentoring.** Whom will Grace mentor? *Rubric:* 3 = a colleague acting as her backup;; 2 = backup;; 1 = none;; 0 = none.
- **EX060 — Background lesson.** Why did Grace's background prove useful? *Rubric:* 3 = human-centred security depends on trust and communication;; 2 = people skills;; 1 = none;; 0 = none.

### Synthesis

A portfolio shows reasoning and outcomes, and continuing development sustains practice.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Grace Mwangi, Alan Pryce, Harlow Professional Academy, Ferngate Housing Association and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A fake email that changes a contractor's bank details.

**EX002.** Between staff, managers and the IT supplier.

**EX003.** To make secure behaviour easy and welcome, not to police colleagues.

**EX004.** That the weakest-link view should be transformed by designing security around people.

**EX005.** Procedures she writes, data she analyses and reflections on cases.

**EX006.** Remotely, visiting tenants with tablets.

**EX007.** The tenant's new address.

**EX008.** Being blamed for mistakes and extra work.

**EX009.** That Ferngate will never ask for bank details by email.

**EX010.** So that changes can be designed to answer them and gain support.

**EX011.** Read staff mailboxes, monitor individuals or run deceptive tests without approval.

**EX012.** Click links or open attachments from reports on her normal computer.

**EX013.** She follows the incident plan and the IT supplier's advice.

**EX014.** Who reported what, along with personal details.

**EX015.** Because staff report more when they do not fear being judged.

**EX016.** 70%, since 126 of 180 staff responded.

**EX017.** Being unsure whether a message was worth reporting, chosen by 51 of 126 (40%).

**EX018.** To make answers comparable across teams.

**EX019.** A clear procedure for phone requests about tenants.

**EX020.** Within two weeks of the survey.

**EX021.** To confirm the tool is working correctly before sharing figures.

**EX022.** More attacks or more willingness to report.

**EX023.** As a healthy sign that people feel safe to ask.

**EX024.** About 26 hours before templates and 3 hours after.

**EX025.** Where do people need more support?

**EX026.** About twenty minutes a day.

**EX027.** A verdict within one working day.

**EX028.** The finance manager.

**EX029.** A short all-staff message saying the message is known and being removed.

**EX030.** By taking a planned day off and reviewing what happened.

**EX031.** A tenant's address, contact details or circumstances, except with the verified tenant.

**EX032.** The number already in Ferngate's records.

**EX033.** Pressure from authority and urgency, described by Cialdini.

**EX034.** Through announced role-play, with a colleague acting as the caller.

**EX035.** Because it sounded abrupt to relatives, so an explanation was added.

**EX036.** The system blocked payment pending callback, and the callback revealed the fraud.

**EX037.** A supposed cash flow problem requiring payment that day.

**EX038.** Urgency, present in all four.

**EX039.** It was easy to miss on a busy screen.

**EX040.** Anonymously, as a success story in a learning session.

**EX041.** One recent example, one simple action and thanks for reports.

**EX042.** That Ferngate will never ask for bank details by email or text.

**EX043.** No simulations in the first year.

**EX044.** Pay, housing or health.

**EX045.** Outcome measures, verified controls, near misses and staff burden, with limits.

**EX046.** Whether verdicts are timely, correct, arriving from all teams and clearly templated.

**EX047.** A tablet update removed the report button from the mail app.

**EX048.** 14 and 16 in months two and three, 2 in month four and 15 in month five after the fix.

**EX049.** Two problems were caused by updates removing settings.

**EX050.** A standard post-update checklist.

**EX051.** One sentence explaining the clue that revealed the message.

**EX052.** Version A readers judged 18 of 30 correctly and version B readers 25 of 30.

**EX053.** Because they knew they were being asked to judge messages.

**EX054.** Only one extra sentence per verdict.

**EX055.** To check after three months whether repeat reporting improves.

**EX056.** That items were free of personal details and claims were supported by evidence.

**EX057.** From about a day to a few hours.

**EX058.** Extending callback rules to tenant refund requests.

**EX059.** A colleague who acts as her backup.

**EX060.** Because human-centred security depends on trust, communication and practical help.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
- Verizon Business. (2024). *2024 Data breach investigations report*. Verizon. <https://www.verizon.com/business/resources/reports/dbir/>
