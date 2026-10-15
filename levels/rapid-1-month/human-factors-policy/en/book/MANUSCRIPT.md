# Human Factors and Cyber Policy: Rapid Course

- Language: English (`en`); course 006, Rapid course (1 month).
- Editorial state: **published**. Chapters 1–20 have hand-written teaching text; exercises EX001–EX066 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. The rapid planning minimum is 20 lessons and there is no maximum. These twenty lessons meet that minimum. Independent review remains open. Page count is not the writing target. This is not a finished qualification.
- Audience: staff and volunteers in small charities and community organisations who need a fast, practical start in human-centred security.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs count systems each role can reach and summarise reporting times in a guided test, both on synthetic data; no real staff, volunteers, donors, emails or accounts are involved. The guided test uses a test email account and volunteers who know the purpose. The course recommends no simulated phishing; if ever used, it must be announced, agreed with staff and volunteer representatives, avoid lures about money, food or hardship, give kind feedback and report only totals. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

<!-- open-cyber-academy:chapter-lessons -->

## How to use this book

Read the chapters in order. This English edition publishes twenty lessons, and each numbered chapter is that lesson. Five chapters in a row can be one study week; the grouping does not make a second copy of the text. Ruth Adeyemi's first four lessons cover the early decisions, the permitted scope, the systems people depend on, and the reporting lab with the adopted month plan. Lessons 5–20 each take one later Riverbend question and leave the laboratory prints where the file already has them. Meeting twenty lessons meets the planning minimum. It does not close review, and it does not award a qualification. Run each lab where the chapter shows it, try the exercise before the worked result, and score the rubric yourself.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Ruth Adeyemi** | Operations coordinator and rapid-course learner | Invented |
| **Callum Shaw** | Facilitator | Invented |
| **Oakmere Adult Learning Centre** | Fictional training provider | Invented |
| **Riverbend Food Bank** | Fictional charity, 12 staff and 60 volunteers | Invented |

### Core sources

Adams and Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806); Sasse, Brostoff and Weirich (2001), [doi:10.1023/A:1011902718709](https://doi.org/10.1023/A:1011902718709); Hadnagy (2018); Cialdini (2021); Bada, Sasse and Nurse (2019), arXiv:1901.02672; Hansche et al. (2024), NIST SP 800-50r1. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Human factors and cyber policy: foundations and decisions

### Learning outcomes

You will (1) explain why people, not only technology, decide security outcomes; (2) recognise common deception tactics; (3) make three early decisions for a small charity.

### 1.1 People and security

Ruth Adeyemi coordinates operations at the fictional Riverbend Food Bank, a charity with twelve staff and sixty volunteers. She joins a one-month rapid course at the fictional Oakmere Adult Learning Centre, guided by facilitator Callum Shaw. Callum begins with a simple idea: most attacks on small charities reach people before they reach systems. A fake supplier invoice, a call pretending to be the bank or an email asking a volunteer to log in somewhere all depend on a person acting. Security therefore depends on helping people act safely under ordinary pressures.

### 1.2 Not the enemy

Callum introduces two classic papers. Adams and Sasse (1999), Users are not the enemy, showed that people break security rules mostly because the rules do not fit their work, not because they are careless. Sasse, Brostoff and Weirich (2001) argued for transforming the so-called weakest link through better design. Ruth recognises this at Riverbend: volunteers share one login for the donations spreadsheet because creating individual accounts was never arranged. The problem is the setup, not the volunteers' attitude, and blaming them would only make them hide mistakes.

### 1.3 Deception tactics

Ruth learns common tactics described by Hadnagy (2018) and explained by Cialdini's principles of influence. Attackers claim authority, such as posing as the bank or a major donor; create urgency, such as a deadline today; and use liking or familiarity, such as copying a known supplier's style. At Riverbend, a typical attack might be an email from a lookalike of the food wholesaler's address asking for payment to new bank details. Knowing these patterns helps Ruth design simple checks that do not rely on spotting every clue.

### 1.4 Knowledge is not enough

Callum warns that telling people about tactics rarely changes behaviour by itself. Bada, Sasse and Nurse (2019) found that awareness campaigns often fail when they rely on fear or assume knowledge leads to action. NIST SP 800-50r1 (Hansche et al., 2024) describes learning programmes that combine awareness with role-based training and evaluation. For a small charity, Ruth concludes, the practical approach is a few easy habits, clear procedures for risky tasks and a friendly way to ask for help, rather than long lectures that people forget.

### 1.5 Three early decisions

Ruth makes three early decisions for Riverbend. First, any change to a supplier's bank details will be checked by phoning the supplier on the number already on file. Second, staff and volunteers will be told clearly that reporting anything odd is welcome and never leads to blame. Third, the shared donations login will be replaced with individual accounts. She writes the decisions in a one-page note for the charity manager, explaining the reason for each in plain language. Callum notes that these decisions target the highest risks with little cost.

### Worked example

Ruth learns why people decide outcomes, recognises authority and urgency tactics and makes three decisions: callbacks for bank changes, a no-blame reporting message and individual accounts.

> **Synthetic case.** Riverbend is synthetic; Adams and Sasse (1999), Sasse et al. (2001), Hadnagy (2018), Cialdini (2021), Bada et al. (2019) and SP 800-50r1 are real.

### Errors and limits

Decisions need follow-through. Small teams change often.

### Exercises

- **EX001 — Charity size.** How many staff and volunteers does Riverbend have? *Rubric:* 3 = twelve staff and sixty volunteers;; 2 = 72;; 1 = vague;; 0 = none.
- **EX002 — Where attacks land.** According to Callum, what do most attacks on small charities reach first? *Rubric:* 3 = people, before they reach systems;; 2 = people, without the contrast with systems;; 1 = systems;; 0 = none.
- **EX003 — Rule breaking cause.** Why do people break security rules according to Adams and Sasse (1999)? *Rubric:* 3 = the rules do not fit their work;; 2 = fit;; 1 = carelessness;; 0 = none.
- **EX004 — Shared login cause.** Why do volunteers share one donations login? *Rubric:* 3 = individual accounts were never arranged;; 2 = setup;; 1 = laziness;; 0 = none.
- **EX005 — Authority example.** Give an example of an authority tactic. *Rubric:* 3 = posing as the bank or a major donor;; 2 = authority;; 1 = vague;; 0 = none.
- **EX006 — Urgency example.** Give an example of an urgency tactic. *Rubric:* 3 = a deadline today;; 2 = deadline;; 1 = vague;; 0 = none.
- **EX007 — Typical attack.** What typical attack might Riverbend face? *Rubric:* 3 = a lookalike wholesaler email with new bank details;; 2 = invoice fraud;; 1 = vague;; 0 = none.
- **EX008 — Campaign weakness.** Why do awareness campaigns often fail according to Bada et al. (2019)? *Rubric:* 3 = fear and assuming knowledge leads to action;; 2 = fear;; 1 = vague;; 0 = none.
- **EX009 — SP 800-50r1 content.** What does SP 800-50r1 combine in learning programmes? *Rubric:* 3 = awareness, role-based training and evaluation;; 2 = three;; 1 = lectures;; 0 = none.
- **EX010 — Practical approach.** What practical approach suits a small charity? *Rubric:* 3 = easy habits, clear procedures and friendly help;; 2 = habits;; 1 = long lectures;; 0 = none.
- **EX011 — First decision.** What is Ruth's first decision? *Rubric:* 3 = phone suppliers on the number on file before bank changes;; 2 = callback;; 1 = vague;; 0 = none.
- **EX012 — Second decision.** What is Ruth's second decision? *Rubric:* 3 = tell everyone reporting is welcome without blame;; 2 = no blame;; 1 = vague;; 0 = none.
- **EX013 — Third decision.** What is Ruth's third decision? *Rubric:* 3 = replace the shared login with individual accounts;; 2 = accounts;; 1 = vague;; 0 = none.

### Synthesis

Security in small organisations starts with people, simple procedures and a welcoming reporting culture.

### Continue studying — lesson 01 (chapter 01 of 20)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) set the scope of security work in a small charity; (2) obtain permission and respect boundaries; (3) practise safely and ethically, including on simulations.

### 2.1 Setting scope

Callum asks Ruth to write down what her security work will cover. In scope are reporting suspicious messages, the bank change procedure, individual accounts and a short welcome guide for volunteers. Out of scope are reading anyone's email, monitoring what volunteers do and any test that tricks people without agreement. Writing scope down helps Ruth explain her role to colleagues and protects her from being asked to do things that would damage trust, such as checking up on particular volunteers. The manager reads it.

### 2.2 Permission

Ruth asks the charity manager and the trustees' chair to approve her one-page scope. They sign it. She tells staff and the volunteer coordinators what she will do and why. Callum explains that permission matters even for small, friendly changes, because security work touches people's accounts, data and sense of being trusted. Asking first also brings useful ideas: the volunteer coordinator suggests including the guide in the induction pack that every new volunteer already receives, which saves Ruth from creating a separate process.

### 2.3 Handling reports safely

Ruth learns safe habits for handling reported messages. She never clicks links or opens attachments in reported emails; she forwards them to the charity's IT volunteer using the agreed method; and she records only the date, type and outcome, not who reported. If a report suggests something serious, such as donor data being sent to the wrong address, she follows the charity's incident steps and asks the IT volunteer for help rather than investigating alone. Safe handling protects both the charity and the person who reported.

### 2.4 Simulations and ethics

The charity manager asks whether Riverbend should send fake phishing emails to test volunteers. Callum explains that deception can damage trust, which a volunteer-based charity depends on. Lain, Kostiainen and Čapkun (2022) found that some common simulation practices did not help. Ruth recommends no simulations for now. If they are ever used, rules must be agreed with staff and volunteer representatives: announce the programme, avoid lures about money, food or personal hardship, give kind feedback immediately, report only totals and never use results against anyone.

### 2.5 Safe practice summary

Ruth writes a short safe practice summary for herself: work within the signed scope; ask before changing anyone's access; handle reports without clicking; keep records free of names; use synthetic examples in training; and practise procedures through announced role-play rather than secret tests. She pins it above her desk. Callum notes that these habits are what separate trustworthy security work from well-meant interference, and that they matter even more in charities, where people give their time freely and can simply leave if they feel mistrusted.

### Worked example

Ruth writes and gets approval for a scope, adopts safe report handling, recommends no simulations with strict future rules and writes a safe practice summary.

> **Synthetic case.** Scope and rules are synthetic; Lain et al. (2022) is real.

### Errors and limits

Scope may need updating. Volunteers may not read guides.

### Exercises

- **EX014 — Out-of-scope item.** Name one item outside Ruth's scope. *Rubric:* 3 = reading anyone's email;; 2 = monitoring;; 1 = reporting;; 0 = none.
- **EX015 — Scope signatories.** Who signed Ruth's scope? *Rubric:* 3 = the charity manager and trustees' chair;; 2 = two;; 1 = vague;; 0 = none.
- **EX016 — Coordinator idea.** What did the volunteer coordinator suggest? *Rubric:* 3 = include the guide in the induction pack;; 2 = induction;; 1 = vague;; 0 = none.
- **EX017 — Reported link rule.** What must Ruth never do with links in reported emails? *Rubric:* 3 = click them;; 2 = no clicking;; 1 = vague;; 0 = none.
- **EX018 — Record fields.** What does Ruth record about reports? *Rubric:* 3 = date, type and outcome only;; 2 = minimal;; 1 = names;; 0 = none.
- **EX019 — Serious report.** What does Ruth do with a serious report? *Rubric:* 3 = follow incident steps with the IT volunteer;; 2 = escalate;; 1 = investigate alone;; 0 = none.
- **EX020 — Simulation risk.** Why are simulations risky for a volunteer charity? *Rubric:* 3 = deception can damage trust;; 2 = trust;; 1 = cost;; 0 = none.
- **EX021 — Simulation recommendation.** What does Ruth recommend about simulations now? *Rubric:* 3 = no simulations for now;; 2 = no simulations, without 'for now';; 1 = monthly;; 0 = no answer.
- **EX022 — Banned lure themes.** Which lure themes are banned if simulations are ever used? *Rubric:* 3 = money, food or personal hardship;; 2 = hardship;; 1 = vague;; 0 = none.
- **EX023 — Results use.** How may simulation results ever be used? *Rubric:* 3 = only as totals, never against anyone;; 2 = aggregate;; 1 = vague;; 0 = none.
- **EX024 — Procedure practice.** How should procedures be practised? *Rubric:* 3 = announced role-play;; 2 = role-play;; 1 = secret tests;; 0 = none.
- **EX025 — Why habits matter more.** Why do safe habits matter even more in charities? *Rubric:* 3 = volunteers can leave if mistrusted;; 2 = volunteers;; 1 = vague;; 0 = none.
- **EX026 — Pinned summary.** Where does Ruth keep her safe practice summary? *Rubric:* 3 = pinned above her desk;; 2 = desk;; 1 = vague;; 0 = none.

### Synthesis

Clear scope, permission and ethical habits make security work trustworthy.

### Continue studying — lesson 02 (chapter 02 of 20)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.

<a id="ch-03"></a>

## Chapter 3 — Human factors and cyber policy: systems, data and dependencies

### Learning outcomes

You will (1) map the systems, data and people a small charity depends on; (2) find points where one person or mistake can cause harm; (3) choose simple fixes.

### 3.1 Mapping systems

Ruth maps Riverbend's systems on one page: shared email accounts, the donations spreadsheet, an online bank account, a volunteer rota app and the charity's social media pages. Beside each she writes who uses it and what data it holds. The donations spreadsheet holds donor names and addresses; the rota app holds volunteer phone numbers; the bank account can make payments. Mapping helps Ruth see where personal data and money sit, which are the things attackers most want and the things whose loss would hurt the charity most.

### 3.2 Data and people

Ruth notes how data move between people. Volunteers copy donor details from paper forms into the spreadsheet. The treasurer approves payments after the coordinator forwards invoices by email. Staff post updates on social media using one shared password. At each handover, a deceptive message or simple error could cause harm. She counts how many systems each person can access and finds that the treasurer, a retired volunteer, can reach almost everything, while some staff who need access to the rota do not have it.

### Lab — Counting systems each role can reach

```python
# Systems each role can reach (synthetic): email, spreadsheet, bank, rota, social media.
access = {"treasurer": {"email", "spreadsheet", "bank", "rota", "social"}, "coordinator": {"email", "spreadsheet", "rota"},
          "warehouse volunteer": {"spreadsheet"}, "staff (rota needed)": {"email"}}
for r, s in access.items(): print(f"{r}: {len(s)} of 5")
```

Run with `python3 lab_access.py`. Verified output:

```text
treasurer: 5 of 5
coordinator: 3 of 5
warehouse volunteer: 1 of 5
staff (rota needed): 1 of 5
```

### 3.3 Single points of failure

Ruth finds two single points of failure. Only the treasurer can approve payments, so if she is away, invoices wait and pressure builds, which attackers can exploit with urgent fake invoices. Only one volunteer knows the social media password, so if that account is taken over, nobody else can recover it quickly. She also notes that the bank account sends alerts only to the treasurer's personal email. Each single point means that one absence, one mistake or one deception could cause lasting harm.

### 3.4 Simple fixes

Ruth chooses simple fixes. A second trustee is authorised to approve payments, always after a callback for any bank change. Social media accounts get individual logins with two-step verification and recovery details held by the charity manager. Bank alerts go to a shared charity mailbox as well as the treasurer. Donor data in the spreadsheet are limited to what is needed for thank-you letters. Each fix costs little and removes a point where one person or mistake could cause serious harm.

### 3.5 Checking the fixes

Ruth checks that each fix works. She asks the second trustee to approve a small test payment with a callback, confirms that a test bank alert reaches the shared mailbox and logs into social media with her own account to confirm two-step verification works. She records each check with the date. Callum reminds her that checking fixes is part of the job, because many security changes are made with good intentions but never confirmed, and they quietly fail when they are needed most.

### Worked example

Ruth maps systems and data, counts access by role, finds payment and social media single points of failure and checks simple fixes.

> **Synthetic case.** Systems and data are synthetic.

### Errors and limits

Maps go out of date. Second approvers need training.

### Exercises

- **EX027 — Data locations.** Where do donor names and addresses sit? *Rubric:* 3 = the donations spreadsheet;; 2 = spreadsheet;; 1 = rota app;; 0 = none.
- **EX028 — Treasurer access.** How many of five systems can the treasurer reach in the lab? *Rubric:* 3 = 5;; 2 = all;; 1 = 2;; 0 = none.
- **EX029 — Payment single point.** Why is the treasurer a single point of failure? *Rubric:* 3 = only she can approve payments;; 2 = approval;; 1 = vague;; 0 = none.
- **EX030 — Pressure link.** How does a waiting invoice help attackers? *Rubric:* 3 = pressure builds that urgent fakes exploit;; 2 = urgency;; 1 = vague;; 0 = none.
- **EX031 — Social media risk.** What is the social media single point? *Rubric:* 3 = only one volunteer knows the password;; 2 = one person;; 1 = vague;; 0 = none.
- **EX032 — Bank alerts.** Where did bank alerts originally go? *Rubric:* 3 = only the treasurer's personal email;; 2 = personal;; 1 = vague;; 0 = none.
- **EX033 — Payment fix.** What fixes the payment single point? *Rubric:* 3 = a second authorised trustee with callbacks;; 2 = second approver;; 1 = vague;; 0 = none.
- **EX034 — Social media fix.** How are social media accounts secured? *Rubric:* 3 = individual logins with two-step verification;; 2 = two-step;; 1 = shared password;; 0 = none.
- **EX035 — Donor data limit.** What limit applies to donor data? *Rubric:* 3 = only what thank-you letters need;; 2 = minimal;; 1 = vague;; 0 = none.
- **EX036 — Fix checks.** How did Ruth check the bank alert fix? *Rubric:* 3 = a test alert reached the shared mailbox;; 2 = test;; 1 = vague;; 0 = none.
- **EX037 — Unchecked fixes.** Why check fixes according to Callum? *Rubric:* 3 = well-meant changes often fail silently;; 2 = silent failure;; 1 = vague;; 0 = none.
- **EX038 — Rota access gap.** What gap did Ruth find for rota access? *Rubric:* 3 = some staff who need it lack it;; 2 = missing access;; 1 = vague;; 0 = none.

### Synthesis

Mapping systems, data and people reveals single points of failure that simple fixes can remove.

### Continue studying — lesson 03 (chapter 03 of 20)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.

<a id="ch-04"></a>

## Chapter 4 — Human factors and cyber policy: guided lab and applied synthesis

### Learning outcomes

You will (1) test a reporting route with volunteers in a safe setting; (2) measure whether it is quick and clear; (3) write a one-month action plan.

### 4.1 Reporting route

Riverbend had no clear way to report suspicious messages; people mentioned them to whoever was nearby, if at all. Ruth sets up a simple route: forward anything odd to a shared report address, or tell the duty coordinator, who forwards it. The IT volunteer checks the address daily and replies to every report with a short verdict and thanks. She writes a two-line instruction and adds it to the volunteer guide and to a poster in the warehouse. The route must be quick, because volunteers have little time on shift.

### 4.2 Guided lab

In the guided lab, Ruth tests the route with eight volunteers using a test email account and synthetic messages. Everyone knows they are testing the route, not being tested. Each volunteer receives three messages, one suspicious, and is asked to report anything odd. Ruth times how long reporting takes and notes confusion. The lab summarises times and success. Seven of eight report the suspicious message correctly; one forwards a genuine message instead, unsure which was odd, which Ruth treats as a useful report rather than a mistake.

### Lab — Reporting times and success in the guided lab

```python
# Reporting times (seconds) and success for eight volunteers in the guided lab (synthetic).
times = [25, 31, 34, 38, 42, 47, 95, 110]; correct = [1, 1, 1, 1, 1, 1, 1, 0]
s = sorted(times)
print(f"correct {sum(correct)}/8; median time {(s[3] + s[4]) / 2:.0f} s; over 60 s: {sum(t > 60 for t in times)}")
```

Run with `python3 lab_route.py`. Verified output:

```text
correct 7/8; median time 40 s; over 60 s: 2
```

### 4.3 Learning from the test

The test shows that forwarding takes most volunteers under a minute, but two struggled to find the report address on their phones. Ruth adds the address as a contact on the shared volunteer phones and asks the IT volunteer to add a quick reply template. Volunteers say they like hearing back, which matches evidence that feedback encourages future reporting. Ruth also notes that one volunteer felt nervous about reporting a genuine message, so she adds a line to the guide: if unsure, report it.

### 4.4 One-month plan

Ruth writes a one-month action plan. Week one: confirm the callback procedure with the treasurer and second trustee, and send the no-blame message. Week two: replace the shared donations login with individual accounts. Week three: launch the reporting route with the guide and poster. Week four: review reports, replies and any problems with the charity manager. Each step has an owner and a check. Callum notes that a short, concrete plan is more likely to be completed than an ambitious strategy.

### 4.5 Synthesis

At the end of the course, Ruth summarises what she learned. Security at Riverbend depends on people: volunteers, staff and trustees acting under real pressures. The most useful measures are simple: callbacks for bank changes, individual accounts, an easy reporting route with friendly replies and no blame for honest mistakes. Deceptive tests are unnecessary and could harm trust. She shares her summary with the trustees, who adopt the plan. Callum reminds her to review it after three months, because good habits need regular attention to last.

### Worked example

Ruth sets up a reporting route, tests it with eight volunteers, fixes phone contact and unsure-report issues and writes a four-week plan adopted by trustees.

> **Synthetic case.** The lab and plan are synthetic.

### Errors and limits

Small test. Plans slip without review.

### Exercises

- **EX039 — Old reporting.** How were suspicious messages reported before? *Rubric:* 3 = mentioned to whoever was nearby;; 2 = informal;; 1 = button;; 0 = none.
- **EX040 — Reply promise.** What does the IT volunteer do for every report? *Rubric:* 3 = replies with a short verdict and thanks;; 2 = feedback;; 1 = vague;; 0 = none.
- **EX041 — Lab success.** How many volunteers reported the suspicious message correctly in the lab? *Rubric:* 3 = 7 of 8;; 2 = seven;; 1 = 8 of 8;; 0 = none.
- **EX042 — Lab median time.** What was the median reporting time in the lab? *Rubric:* 3 = 40 seconds;; 2 = under a minute;; 1 = vague;; 0 = none.
- **EX043 — Genuine forward.** How did Ruth treat the volunteer who forwarded a genuine message? *Rubric:* 3 = as a useful report;; 2 = useful;; 1 = mistake;; 0 = none.
- **EX044 — Phone fix.** What fixed the phone problem? *Rubric:* 3 = adding the report address as a contact;; 2 = contact;; 1 = vague;; 0 = none.
- **EX045 — Unsure line.** What line did Ruth add to the guide? *Rubric:* 3 = if unsure, report it;; 2 = unsure;; 1 = vague;; 0 = none.
- **EX046 — Week two.** What happens in week two of the plan? *Rubric:* 3 = individual accounts replace the shared login;; 2 = accounts;; 1 = vague;; 0 = none.
- **EX047 — Week four.** What happens in week four? *Rubric:* 3 = review reports and problems with the manager;; 2 = review;; 1 = vague;; 0 = none.
- **EX048 — Plan style.** Why prefer a short concrete plan? *Rubric:* 3 = it is more likely to be completed;; 2 = completion;; 1 = vague;; 0 = none.
- **EX049 — Deceptive tests view.** What is Ruth's view on deceptive tests? *Rubric:* 3 = unnecessary and could harm trust;; 2 = unnecessary;; 1 = vague;; 0 = none.
- **EX050 — Review timing.** When should Ruth review the plan? *Rubric:* 3 = after three months;; 2 = three months;; 1 = never;; 0 = none.

### Synthesis

A safe test, a short plan and simple, kind measures give a small charity a strong start.

### Continue studying — lesson 04 (chapter 04 of 20)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.

<a id="ch-05"></a>

## Chapter 5 — An adopted plan is not week two already done

### Learning outcomes

After this chapter, you should be able to:

1. Keep the published access lines as the count already run.
2. Tell an adopted week-two step apart from accounts already issued.
3. Leave the shared-login finding in place until a later listing exists.

### 5.1 The signature starts the month. It does not finish Tuesday's task.

Chapter 4 records that the trustees adopt Ruth's four-week plan. Week two of that plan is the replacement of the shared donations login with individual accounts. A classmate treats the adoption as proof the replacement has happened, and wants the access note rewritten so every role shows a private login. The only listing in the file is the four-line print from `lab_access.py`. That print still describes the treasurer, the coordinator, the warehouse volunteer and the staff who need the rota. It does not describe a completed issuance of accounts. Ruth leaves the script alone. Week two remains a step on the adopted page, not a result she can already quote.

### 5.2 Worked example

| What someone cites | What the file holds | Decision |
|---|---|---|
| The trustees adopt the plan | A decision to follow the four weeks | Keep the adoption |
| "Week two is therefore finished." | No later access listing | Refuse |
| The four published role lines | The first run | Leave them |
| "Add a row for every new account." | The original dictionary | Refuse the edit |

> **Synthetic case.** No new login is issued in this lesson. The four lines stay the verified run.

### Errors and limits

Leaving week two open does not cancel the decision to replace the shared login. It refuses a result the file does not contain.

### Apply

- **EX051 — Which week finished?** The trustees adopt the plan. Week two says the shared donations login will be replaced with individual accounts. The access print is still the four published lines. Has week two happened, and what happens to the script? *Rubric:* 3 = adoption is not completion; the four lines stay; do not edit the script; do not add account rows;; 2 = the plan is adopted and the print stays;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 20)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Seven of eight is not a perfect eight

### Learning outcomes

After this chapter, you should be able to:

1. Keep `correct 7/8` as the published success line.
2. Keep the genuine forward as a useful report.
3. Refuse a rewritten list that would print eight of eight.

### 6.1 Useful and correct answer different questions

The guided lab asked eight volunteers to report anything odd. Seven reported the suspicious message. One forwarded a genuine message instead, and Ruth treats that forward as a useful report rather than a scolding. A classmate says the kindness means the print should read eight of eight. The program counts the suspicious message only. The genuine forward is the final 0 in the correct list, which is why the line says 7/8. Calling it useful does not change that 0. Ruth does not edit `lab_route.py`, and she does not name the volunteer.

### 6.2 Worked example

| Claim | Which question it answers | Decision |
|---|---|---|
| Seven reported the suspicious message | The correct list | Keep 7/8 |
| The other forward was a useful report | Ruth's reading of that person | Keep that reading |
| "So the lab was 8/8." | A different tally | Refuse |
| "Change the last 0 to 1." | The published list | Refuse |

> **Synthetic case.** The eighth person stays unnamed. The 0 is the list already run.

### Errors and limits

Protecting the volunteer from blame does not require a prettier fraction. The fraction and the kindness can both stand.

### Apply

- **EX052 — Which number moves?** Seven of eight reported the suspicious message. The other volunteer forwarded a genuine message, and Ruth calls that useful. May the print become 8/8, and what happens to the script? *Rubric:* 3 = 7/8 stays; the genuine forward stays a useful report and is not relabelled as a correct suspicious report; do not edit the script; name no volunteer;; 2 = 7/8 stays and the person is not blamed;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 20)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — One test alert is not every later alert

### Learning outcomes

After this chapter, you should be able to:

1. Keep the test alert as one confirmed arrival.
2. Leave the treasurer's personal copy in place.
3. Refuse to treat the test as proof of every later alert.

### 7.1 The mailbox was added beside the old address, and then tried once

Bank alerts used to go only to the treasurer's personal email. The fix sends them to a shared charity mailbox as well. Ruth confirmed that one test alert reached that mailbox, and she recorded the check. A classmate crosses the personal address off the page and writes that future alerts are solved. The file says "as well as," not "instead of." One arrival does not describe the next real alert from the bank. Ruth does not remove the treasurer's copy, and this lesson invents no second test.

### 7.2 Worked example

| Sentence | Support in the file | Decision |
|---|---|---|
| A test alert reached the shared mailbox | The check Ruth recorded | May stay |
| The treasurer still receives alerts too | "As well as" | May stay |
| "Every later alert will arrive." | No later test | Refuse |
| "Delete the personal address." | The fix did not say that | Refuse |

> **Synthetic case.** No second alert is composed. The treasurer stays unnamed.

### Errors and limits

Keeping the personal copy does not mean the shared mailbox was unnecessary. It means the file did not replace one destination with the other.

### Apply

- **EX053 — What did the test cover?** One test bank alert reached the shared mailbox. Alerts still go to the treasurer as well. A teammate deletes the personal address and says later alerts are guaranteed. What stays, and what is not guaranteed? *Rubric:* 3 = the one test stands; the personal copy stays; a later alert is not guaranteed; invent no second test;; 2 = one test is not every alert, and the personal copy stays;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 20)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — A test payment is not the wholesaler's new details

### Learning outcomes

After this chapter, you should be able to:

1. Keep the small test payment as a check of the second trustee's path.
2. Send a later bank-detail request back to the number on file.
3. Refuse to treat the rehearsal as approval of a lookalike invoice.

### 8.1 The callback was practised. It was not spent on a supplier.

Ruth asked the second trustee to approve a small test payment, and that approval used a callback. Separately, the early decision says any change to a supplier's bank details is checked by phoning the number already on file. A classmate receives a lookalike of the food wholesaler asking for payment to new details, and says the test payment means the path is trusted enough to pay. The test had no supplier and no new account. The lookalike is the situation the phone call was written for. Ruth does not pay it, does not invent an amount, and does not invent the wholesaler's real name.

### 8.2 Worked example

| Item | What it is | Decision |
|---|---|---|
| Small test payment with a callback | A check of the second trustee | May stay as that check |
| Lookalike wholesaler, new details | The typical lure | Do not pay |
| "The rehearsal covered this invoice." | A leap | Refuse |
| Phone the number on file | The rule for a real change | Still required |

> **Synthetic case.** No supplier name, account number or sum is added.

### Errors and limits

Refusing the lure does not undo the test payment. The rehearsal and the invoice are different objects.

### Apply

- **EX054 — Which payment was the test?** The second trustee approved a small test payment with a callback. A lookalike wholesaler then asks for new bank details. Does the test approve that request, and what call is still required? *Rubric:* 3 = the test does not approve the lure; phone the number already on file; do not pay; invent no amount and no supplier name;; 2 = the lure is not the test payment;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 20)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — The rota gap is not a copy of the treasurer's row

### Learning outcomes

After this chapter, you should be able to:

1. Read `staff (rota needed): 1 of 5` as email without the rota.
2. Refuse to copy the treasurer's five systems onto that role.
3. Leave the gap open in this lesson.

### 9.1 The role's name says which system is missing

The access listing prints `staff (rota needed): 1 of 5`. The dictionary gives that role email alone. Ruth's note says some staff who need the rota do not have it. A classmate "fixes" the line by giving those staff the treasurer's five systems, including the bank and social media. The gap is the rota. It is not a reason to hand over payments or the public pages. This lesson does not grant the rota either, because no new listing has been run. The published line stays 1 of 5. Ruth does not edit `lab_access.py`.

### 9.2 Worked example

| Proposal | What it changes | Decision |
|---|---|---|
| Leave the staff line at 1 of 5 | Nothing | Accept for this file |
| Give those staff the rota when a real change is made | The missing system | Not done in this lesson |
| Copy the treasurer's five systems | Bank and social as well | Refuse |
| Delete the role so the gap disappears | The evidence | Refuse |

> **Synthetic case.** No staff member is named. The rota is not switched on here.

### Errors and limits

Keeping the gap visible is not a decision to withhold the rota forever. It stops a wider grant from pretending to be the smaller fix.

### Apply

- **EX055 — Which system was missing?** The print says `staff (rota needed): 1 of 5`, and that role has email only. A teammate assigns the treasurer's five systems. What was the gap, and what does the print still say? *Rubric:* 3 = the gap is the rota, not the bank or social media; the line stays 1 of 5; do not copy the treasurer's set; do not edit the script; this lesson does not grant the rota;; 2 = the gap is the rota and the print stays;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue studying — lesson 09 (chapter 09 of 20)

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — One checked login is not a destroyed shared password

### Learning outcomes

After this chapter, you should be able to:

1. Keep Ruth's two-step check as a check of her own login.
2. Leave the old shared password's destruction unstated.
3. Name neither the password nor the volunteer who knew it.

### 10.1 The check had one subject: Ruth's own sign-in

Only one volunteer knew the social media password, and the book never names that person. The fix is individual logins, two-step verification, and recovery details held by the charity manager. Ruth then signs in with her own account and sees two-step verification work. A classmate writes "shared password destroyed" and asks Ruth to store the old password in the note so people can compare. The file shows one successful check. It does not show a destruction, and it does not show every other account. Ruth writes no password and invents no name. The treasurer's row in the access listing is a different fact and is not used to identify the password holder.

### 10.2 Worked example

| Sentence | Evidence | Decision |
|---|---|---|
| Ruth's own login passed two-step verification | The check | May stay |
| Recovery details are held by the manager | The design of the fix | May stay as the design |
| "The shared password is destroyed." | Not in the file | Refuse |
| "Write the old password in the margin." | A secret the note must not hold | Refuse |
| Name the volunteer who knew it | No name was given | Do not invent one |

> **Synthetic case.** No password and no extra account are created.

### Errors and limits

Stopping the note from holding a password does not prove the old password is harmless. It keeps the note inside what was checked.

### Apply

- **EX056 — What did Ruth's sign-in prove?** Two-step verification worked on Ruth's own social login. A teammate writes that the shared password is destroyed and asks for it to be copied into the note. What stands, and what do you not write? *Rubric:* 3 = the check is one account; destruction is not in the file; do not write the password; do not name the volunteer;; 2 = one login is not a destroyed password;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue studying — lesson 10 (chapter 10 of 20)

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — No simulations for now is not a friendly surprise

### Learning outcomes

After this chapter, you should be able to:

1. Keep the recommendation of no simulations for now.
2. Recognise a surprise email as a simulation.
3. Leave practice on announced role-play.

### 11.1 The manager's question was already answered

The charity manager asked whether Riverbend should send fake messages to test volunteers. Ruth's recommendation is no simulations for now, because deception can damage trust that volunteers can walk away from. After the trustees adopt the plan, a colleague proposes one "friendly surprise" about a missed shift, and says it is not really a simulation. A message people do not know is a test is the thing the scope excluded: a test that tricks people without agreement. Missed shifts sit next to the hardship themes that would be barred even if a programme were ever agreed. Ruth does not send it. Announced role-play remains the way to practise a procedure.

### 11.2 Worked example

| Proposal | What it actually is | Decision |
|---|---|---|
| No simulations for now | The recommendation | Keep it |
| Announced role-play of the callback | The allowed practice | May go ahead as practice |
| A surprise email about a missed shift | An unannounced trick | Refuse |
| "We will only keep the totals, so it is fine." | A rule for a programme that is not agreed | Not a reason to start |

> **Synthetic case.** No lure is sent. No volunteer is scored.

### Errors and limits

Refusing the surprise does not forbid talking about tactics in a lesson people know they are attending. The difference is whether the person agreed to be tested.

### Apply

- **EX057 — What is the surprise?** Ruth has recommended no simulations for now. A colleague wants one friendly surprise email about a missed shift, with only totals kept. What do you refuse, and what practice remains allowed? *Rubric:* 3 = refuse the surprise; it is a trick without agreement; no simulations for now still stands; announced role-play remains the practice; do not send the message;; 2 = the surprise is refused;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue studying — lesson 11 (chapter 11 of 20)

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — A name on the report line breaks the record

### Learning outcomes

After this chapter, you should be able to:

1. Keep a report record to date, type and outcome.
2. Refuse a name on that line.
3. Leave investigation of a serious report with the incident steps and the IT volunteer.

### 12.1 The welcome does not collect an identity

Ruth records only the date, the type and the outcome of a report, not who sent it. That limit protects the person who spoke up. A classmate adds a name "so the thanks can be personal," and also opens the link to see whether the message is real. Thanks can be given without storing the name in the log. Opening the link is the act the handling rule forbids. If the report looks serious, Ruth follows the incident steps and asks the IT volunteer for help. She does not investigate it alone, and she does not invent a name in order to refuse one.

### 12.2 Worked example

| Addition | Allowed? | Decision |
|---|---|---|
| Date, type, outcome | Yes | Keep those three |
| The reporter's name | No | Leave it off |
| Click the link to check | No | Do not click |
| A serious case investigated by Ruth alone | No | Incident steps, with the IT volunteer |

> **Synthetic case.** No reporter is named and no message body is quoted.

### Errors and limits

Omitting the name does not mean the report is ignored. The outcome is still recorded, and a serious case still moves.

### Apply

- **EX058 — What goes on the line?** A report arrives. A teammate writes the volunteer's name beside the date, type and outcome, and clicks the link. What do you record, and what do you not do? *Rubric:* 3 = record only date, type and outcome; do not record the name; do not click; do not invent a name; a serious report follows incident steps with the IT volunteer;; 2 = no name and no click;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue studying — lesson 12 (chapter 12 of 20)

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — A suggestion for the induction pack is not the pack

### Learning outcomes

After this chapter, you should be able to:

1. Keep the coordinator's idea as a suggestion.
2. Keep week three as a launch that the adoption has not completed.
3. Refuse a claim that every new volunteer has already received the guide.

### 13.1 The pack was the right shelf. Nobody has shown the guide on it.

The volunteer coordinator suggests putting the guide in the induction pack, so Ruth does not build a second process. That sentence is an idea from a colleague. Week three of the adopted plan is the launch of the reporting route with the guide and the poster. A classmate ticks "all new volunteers briefed" because the suggestion was sensible and the trustees adopted the plan. The file does not say the pack was reprinted, and it does not say week three has been carried out. Ruth does not invent a count of people who have read the page.

### 13.2 Worked example

| Statement | Status | Decision |
|---|---|---|
| The coordinator suggested the induction pack | An idea | May stay as an idea |
| Ruth wrote a short instruction | Drafting | May stay |
| Week three launches the route | A plan step | Not shown as finished |
| "Every new volunteer has the guide." | No count | Refuse |

> **Synthetic case.** No new volunteer is named. No pack is described as reprinted.

### Errors and limits

Leaving the insert unfinished does not waste the suggestion. It keeps the launch on the week that was written for it.

### Apply

- **EX059 — Who has the guide?** The coordinator suggested the induction pack. Week three is the launch, and the trustees have adopted the plan. A teammate says every new volunteer already has the guide. What is still only a suggestion or a step, and what count is missing? *Rubric:* 3 = the pack idea is not a completed insert; week three is not shown as finished; do not claim every new volunteer has the guide; invent no count;; 2 = the suggestion is not the launch;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue studying — lesson 13 (chapter 13 of 20)

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — Twelve and sixty are not a census of seventy-two

### Learning outcomes

After this chapter, you should be able to:

1. Keep twelve staff and sixty volunteers as the published size.
2. Refuse 72 as a replacement census.
3. Keep the access print as four roles, not as a headcount.

### 14.1 The size of the charity and the width of a role are different counts

Riverbend has twelve staff and sixty volunteers. The access program does not count those people. It counts systems reachable by four roles, each out of five. A classmate adds twelve and sixty, writes 72, and replaces the role lines with "72 of 5." Addition of the two groups is not a run of the program, and 72 people cannot each be a fraction of five systems. The staff figure and the volunteer figure stay separate. Ruth does not edit `lab_access.py`.

### 14.2 Worked example

| Figure | What it counts | Decision |
|---|---|---|
| Twelve staff | Staff | Keep |
| Sixty volunteers | Volunteers | Keep |
| 72 | Someone's sum | Refuse as the census |
| Four role lines, each of 5 | Systems a role can reach | Keep those lines |

> **Synthetic case.** The sum 72 is the classmate's arithmetic. It is not a new execution.

### Errors and limits

Refusing the sum does not make either group unimportant. It stops one number from erasing the distinction the file actually drew.

### Apply

- **EX060 — What is 72?** Riverbend has twelve staff and sixty volunteers. The access print has four role lines. A teammate writes 72 of 5. What figures stay, and what do you not print? *Rubric:* 3 = twelve and sixty stay separate; 72 is not the census; the four role lines stay; do not edit the script;; 2 = 72 is refused and the role lines stay;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue studying — lesson 14 (chapter 14 of 20)

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — Two slow times stay in the published list

### Learning outcomes

After this chapter, you should be able to:

1. Keep 95 and 110 inside the published time list.
2. Keep the median at 40 seconds for that full list.
3. Place the phone-contact fix after the test, not inside it.

### 15.1 The slow pair is why the phones were changed. It is not a pair to erase.

Two of the eight times are over a minute: 95 seconds and 110 seconds. The print says `over 60 s: 2`, and the median of the full sorted list is 40 seconds. Ruth then adds the report address as a contact on the shared volunteer phones, because people struggled to find it. A classmate deletes 95 and 110, saying the phones are fixed so those times no longer count, and asks for a new median. The contact was added after the eight attempts. Removing the pair would be a different list, and this lesson does not run that list. The published median stays 40 seconds.

### 15.2 Worked example

| Action | Timing | Decision |
|---|---|---|
| Keep 95 and 110 | They are in the published list | Accept |
| Median 40 seconds | The full list | Keep |
| Add the address to the phones | After the test | May stay as a later fix |
| Drop the two slow times and recompute | A new list | Refuse |

> **Synthetic case.** No new median is calculated. The eight times stay the ones in the program.

### Errors and limits

Keeping the slow times does not mean the phone contact was pointless. It means the contact does not rewrite the afternoon that prompted it.

### Apply

- **EX061 — Which times stay?** The published list includes 95 and 110, the median is 40 seconds, and two times are over 60 seconds. Ruth adds the report address to the phones afterwards. A teammate drops the two slow times. What stays, and what do you not recompute? *Rubric:* 3 = 95 and 110 stay; the median stays 40 seconds for the full list; the phone contact is after the test; do not recompute; do not edit the script;; 2 = the slow times stay and the median is not redone;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue studying — lesson 15 (chapter 15 of 20)

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — Adoption is not the three-month review

### Learning outcomes

After this chapter, you should be able to:

1. Keep the three-month review as a future look.
2. Tell it apart from the trustees' adoption.
3. Refuse findings that the later look never produced.

### 16.1 The reminder points forward. The adoption points at the plan.

Callum tells Ruth to review the plan after three months, because habits need attention if they are to last. The trustees adopt the plan at the end of the course. A classmate writes "three-month review: done" on the strength of that adoption, and adds two findings the meeting never recorded. Adoption is the decision to begin. The three-month look has no date in the file and no notes. Week four, a conversation with the charity manager about reports and problems, is a step inside the first month. It is not the later review. Ruth invents no finding and does not mark the three months as elapsed.

### 16.2 Worked example

| Event | What it is | Decision |
|---|---|---|
| Trustees adopt the plan | The start | May stay |
| Review after three months | A reminder | Keep it in the future |
| Week four with the manager | A step inside the plan | Not the three-month review |
| Two findings from that later review | Nothing was written | Do not invent them |

> **Synthetic case.** No calendar date is supplied for the later review.

### Errors and limits

Leaving the review in the future does not weaken Callum's reminder. It refuses to pretend the reminder has already been kept.

### Apply

- **EX062 — Which meeting was the review?** The trustees adopt the plan. Callum says to review it after three months. A teammate marks that review done and writes two findings. What has happened, and what is missing? *Rubric:* 3 = adoption is not the three-month review; the three months are not dated as elapsed; invent no findings; week four is not that later review;; 2 = adoption is not the later review;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue studying — lesson 16 (chapter 16 of 20)

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — No blame is not a reason to investigate alone

### Learning outcomes

After this chapter, you should be able to:

1. Keep the no-blame welcome.
2. Send a serious report through the incident steps with the IT volunteer.
3. Refuse a solo investigation dressed up as kindness.

### 17.1 The welcome and the escalation are both still in force

Ruth's second decision tells staff and volunteers that reporting anything odd is welcome and does not lead to blame. A classmate hears about donor details sent to the wrong place and says Ruth should "quietly sort it" so nobody feels accused. Quiet sorting by one person is the investigation the handling rule already refused. A serious report follows the charity's incident steps, and Ruth asks the IT volunteer for help. The absence of blame still allows a record of date, type and outcome. It does not require a name, and this lesson does not invent a donor or a volunteer.

### 17.2 Worked example

| Response | Fits the welcome? | Decision |
|---|---|---|
| Thank the report and record date, type, outcome | Yes | Do that |
| Blame the person | No | Do not |
| Ruth investigates the wrong-address case alone | No | Incident steps, with the IT volunteer |
| Hide the case so the welcome stays comfortable | No | The welcome is not concealment |

> **Synthetic case.** The wrong-address case stays the type already used in the book. No one is named.

### Errors and limits

Escalating does not turn the reporter into a suspect. It moves a serious case to the people the steps already named.

### Apply

- **EX063 — Who follows a serious report?** Reporting is welcome and nobody is blamed for an honest mistake. Donor details have gone to the wrong address. A teammate tells Ruth to sort it quietly alone. What still happens, and what does no-blame not allow? *Rubric:* 3 = no blame stands; she does not investigate alone; she follows incident steps with the IT volunteer; the record can still hold date, type and outcome; name no one;; 2 = no solo investigation;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue studying — lesson 17 (chapter 17 of 20)

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — The warehouse row does not inherit the bank

### Learning outcomes

After this chapter, you should be able to:

1. Read the warehouse line as the spreadsheet only.
2. Keep the second trustee as the payment fix.
3. Refuse to put the bank on the warehouse role.

### 18.1 A second approver is a person with a job, not a new set for the warehouse

The warehouse volunteer reaches one system of five: the spreadsheet, which is where donor details from paper forms are typed. The payment single point is fixed by authorising a second trustee, who approves only after a callback when bank details change. A classmate sees that the treasurer can reach the bank and says the warehouse role should reach it too, so the charity is never stuck. Spreading the bank to the people who type donor forms is a wider grant than the fix. The second trustee is not a rename of the warehouse row. The published line stays `warehouse volunteer: 1 of 5`. Ruth does not edit the script.

### 18.2 Worked example

| Proposal | Effect | Decision |
|---|---|---|
| Leave the warehouse line at 1 of 5 | Spreadsheet only | Accept |
| Second trustee approves after a callback | The payment fix | Already the chosen fix |
| Give the warehouse role the bank | A new grant | Refuse |
| "Then they can pay if the treasurer is away." | The pressure problem, solved by the wrong role | Refuse |

> **Synthetic case.** The second trustee stays unnamed. The warehouse line is not rewritten.

### Errors and limits

Keeping the bank off the warehouse role does not leave payments with only one person. The second trustee is already the other person in the design.

### Apply

- **EX064 — Who gains the bank?** The warehouse print is 1 of 5, the spreadsheet. A second trustee is the payment fix. A teammate gives the warehouse role the bank so invoices need not wait. What stays 1 of 5, and who was already the second approver? *Rubric:* 3 = the warehouse line stays 1 of 5 and does not gain the bank; the second trustee remains the payment fix; do not edit the script;; 2 = the warehouse role does not gain the bank;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue studying — lesson 18 (chapter 18 of 20)

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Chapter 19 — A requested reply template is not a reply already sent

### Learning outcomes

After this chapter, you should be able to:

1. Keep the reply promise as a promise.
2. Place the template request after the guided lab.
3. Refuse a claim that eight replies were sent with that template.

### 19.1 The ask came after the clock had already stopped

The design of the route says the IT volunteer checks the report address daily and replies to every report with a short verdict and thanks. After the eight volunteers had been timed, Ruth asks for a quick reply template, because people said they like hearing back. A classmate writes that the template was used on all eight messages and drafts a verdict to paste into the note. The template was requested after those times. The file does not contain eight sent replies, and it does not contain the words of a verdict. Ruth does not invent them. The promise still stands for reports that come later. It is not evidence about the eight.

### 19.2 Worked example

| Item | When it sits | Decision |
|---|---|---|
| A short verdict and thanks for every report | The promise | May stay as a promise |
| A request for a quick template | After the lab | May stay as a request |
| "The template handled the eight." | Before the request existed | Refuse |
| A sample verdict written now | Not in the file | Do not invent the words |

> **Synthetic case.** No reply text is drafted. The eight times stay a timing exercise.

### Errors and limits

Separating the promise from the eight attempts does not cancel the promise. It stops the lab clock from being decorated with a tool that was requested later.

### Apply

- **EX065 — When was the template asked for?** The IT volunteer is to reply to every report with a short verdict and thanks. Ruth asks for a quick reply template after the eight volunteers are timed. A teammate says the template produced eight replies. What is a promise, what is a later request, and what do you not invent? *Rubric:* 3 = the reply rule is a promise; the template was requested after the lab; eight sent replies are not in the file; invent no verdict text;; 2 = the template is not evidence about the eight;; 1 = one of those;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue studying — lesson 19 (chapter 19 of 20)

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Chapter 20 — What the charity note can say

### Learning outcomes

After this chapter, you should be able to:

1. Repeat the laboratory lines and the decisions the file already holds.
2. Reject a note that closes open steps.
3. Point to the next course without calling this edition finished.

### 20.1 A note may quote the file. It may not improve the file.

A leaving note may say what was already written down. Riverbend still has twelve staff and sixty volunteers. The access print still shows the treasurer at 5 of 5, the coordinator at 3 of 5, the warehouse volunteer at 1 of 5 and the staff who need the rota at 1 of 5. The reporting print still says `correct 7/8`, a median of 40 seconds and two times over 60 seconds. The trustees have adopted the four-week plan. Week two, the individual accounts, is not shown as finished. Simulations stay off for now. The three-month review has not been held. Ruth's own social login passed one two-step check, which is not a note that the shared password was destroyed.

### 20.2 Worked example

| Leaving-note sentence | Why it fails or stands | Decision |
|---|---|---|
| "The access print is the four published role lines." | The first run | May stay |
| "Correct reports were 7 of 8, median 40 seconds." | The reporting run | May stay |
| "The print is now 8/8 and the median was recomputed." | No new run | Reject |
| "Week two finished because the plan was adopted." | Adoption is not that step | Reject |
| "The three-month review has been held." | No such note | Reject |

> **Synthetic case.** The note is a classroom page about Riverbend. It is not a notice to donors.

### Errors and limits

Meeting the planning minimum of 20 lessons leaves independent review open. A new Riverbend question can still earn its own later lesson. These English chapters do not publish another language edition. Human factors stays this course. Security architecture is the learner's following subject. Open steps at Riverbend stay open on that turn. These chapters do not certify the charity, and they do not hand anyone a qualification.

### Apply

- **EX066 — Four claims.** A classmate's leaving note says the reporting print is now 8/8 with a new median, that week two is finished because the trustees adopted the plan, that the shared social password has been destroyed, and that the three-month review has already been held. Which claims do you reject, and what do twenty lessons meet? *Rubric:* 3 = reject all four; the reporting print stays 7/8 with median 40 seconds and two times over 60 seconds; week two is not shown as finished; the shared password's destruction is not in the file; the three-month review has not been held; twenty lessons meet the planning minimum and leave review open;; 2 = reject the four claims and keep the published prints;; 1 = one claim;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue studying — lesson 20 (chapter 20 of 20)

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX066. Ruth Adeyemi, Callum Shaw, Oakmere Adult Learning Centre, Riverbend Food Bank and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Twelve staff and sixty volunteers.

**EX002.** People, before they reach systems.

**EX003.** Mostly because the rules do not fit their work.

**EX004.** Because individual accounts were never arranged.

**EX005.** Posing as the bank or a major donor.

**EX006.** Claiming a deadline today.

**EX007.** An email from a lookalike wholesaler address asking for payment to new bank details.

**EX008.** Because they rely on fear or assume knowledge leads to action.

**EX009.** Awareness, role-based training and evaluation.

**EX010.** A few easy habits, clear procedures and a friendly way to ask for help.

**EX011.** To check bank detail changes by phoning the supplier on the number on file.

**EX012.** To tell staff and volunteers that reporting anything odd is welcome and never leads to blame.

**EX013.** To replace the shared donations login with individual accounts.

**EX014.** Reading anyone's email, monitoring volunteers or tricking people without agreement.

**EX015.** The charity manager and the chair of trustees.

**EX016.** Including the guide in the existing induction pack.

**EX017.** Click them, or open attachments.

**EX018.** Only the date, type and outcome.

**EX019.** She follows the incident steps and asks the IT volunteer for help.

**EX020.** Because deception can damage the trust the charity depends on.

**EX021.** No simulations for now.

**EX022.** Money, food or personal hardship.

**EX023.** Only as totals, never against any individual.

**EX024.** Through announced role-play rather than secret tests.

**EX025.** Because volunteers give their time freely and can leave if they feel mistrusted.

**EX026.** Pinned above her desk.

**EX027.** In the donations spreadsheet.

**EX028.** All five systems.

**EX029.** Because only she can approve payments.

**EX030.** Pressure builds, which attackers can exploit with urgent fake invoices.

**EX031.** Only one volunteer knows the shared password.

**EX032.** Only to the treasurer's personal email.

**EX033.** Authorising a second trustee, with callbacks for bank changes.

**EX034.** With individual logins, two-step verification and recovery details held by the manager.

**EX035.** Only what is needed for thank-you letters.

**EX036.** By confirming a test bank alert reached the shared mailbox.

**EX037.** Because well-meant changes often fail quietly when never confirmed.

**EX038.** Some staff who need rota access do not have it.

**EX039.** People mentioned them to whoever was nearby, if at all.

**EX040.** Replies with a short verdict and thanks.

**EX041.** Seven of eight.

**EX042.** 40 seconds.

**EX043.** As a useful report rather than a mistake.

**EX044.** Adding the report address as a contact on shared volunteer phones.

**EX045.** If unsure, report it.

**EX046.** The shared donations login is replaced with individual accounts.

**EX047.** A review of reports, replies and problems with the charity manager.

**EX048.** Because it is more likely to be completed than an ambitious strategy.

**EX049.** That they are unnecessary and could harm trust.

**EX050.** After three months.

**EX051.** Adoption is not completion. The four lines stay. Do not edit the script. Do not add account rows.

**EX052.** 7/8 stays. The genuine forward stays a useful report and is not relabelled as a correct suspicious report. Do not edit the script. Name no volunteer.

**EX053.** The one test stands. The personal copy stays. A later alert is not guaranteed. Invent no second test.

**EX054.** The test does not approve the lure. Phone the number already on file. Do not pay. Invent no amount and no supplier name.

**EX055.** The gap is the rota, not the bank or social media. The line stays 1 of 5. Do not copy the treasurer's set. Do not edit the script. This lesson does not grant the rota.

**EX056.** The check is one account. Destruction is not in the file. Do not write the password. Do not name the volunteer.

**EX057.** Refuse the surprise. It is a trick without agreement. No simulations for now still stands. Announced role-play remains the practice. Do not send the message.

**EX058.** Record only date, type and outcome. Do not record the name. Do not click. Do not invent a name. A serious report follows incident steps with the IT volunteer.

**EX059.** The pack idea is not a completed insert. Week three is not shown as finished. Do not claim every new volunteer has the guide. Invent no count.

**EX060.** Twelve and sixty stay separate. 72 is not the census. The four role lines stay. Do not edit the script.

**EX061.** 95 and 110 stay. The median stays 40 seconds for the full list. The phone contact is after the test. Do not recompute. Do not edit the script.

**EX062.** Adoption is not the three-month review. The three months are not dated as elapsed. Invent no findings. Week four is not that later review.

**EX063.** No blame stands. She does not investigate alone. She follows incident steps with the IT volunteer. The record can still hold date, type and outcome. Name no one.

**EX064.** The warehouse line stays 1 of 5 and does not gain the bank. The second trustee remains the payment fix. Do not edit the script.

**EX065.** The reply rule is a promise. The template was requested after the lab. Eight sent replies are not in the file. Invent no verdict text.

**EX066.** Reject all four. The reporting print stays 7/8 with median 40 seconds and two times over 60 seconds. Week two is not shown as finished. The shared password's destruction is not in the file. The three-month review has not been held. Twenty lessons meet the planning minimum and leave review open.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- Bada, M., Sasse, M. A., & Nurse, J. R. C. (2019). *Cyber security awareness campaigns: Why do they fail to change behaviour?* arXiv:1901.02672. <https://arxiv.org/abs/1901.02672>
- Cialdini, R. B. (2021). *Influence, new and expanded: The psychology of persuasion*. Harper Business.
- Hadnagy, C. (2018). *Social engineering: The science of human hacking* (2nd ed.). Wiley.
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Lain, D., Kostiainen, K., & Čapkun, S. (2022). Phishing in organizations: Findings from a large-scale and long-term study. *2022 IEEE Symposium on Security and Privacy*, 842–859. <https://doi.org/10.1109/SP46214.2022.9833766>
- Sasse, M. A., Brostoff, S., & Weirich, D. (2001). Transforming the 'weakest link' — a human/computer interaction approach to usable and effective security. *BT Technology Journal*, 19(3), 122–131. <https://doi.org/10.1023/A:1011902718709>
