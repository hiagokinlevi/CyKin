# Human Factors and Cyber Policy: Technical Course

- Language: English (`en`); course 052, Technical course (18 months).
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; nine offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical trainees who configure, verify, troubleshoot and document reporting and verification controls in a small organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs count unlocked minutes, summarise a CSV, model reporting losses, count survey barriers, tally verification results, compare reporting times and feedback effects and summarise driver reports, all on synthetic data; no real staff, customers, emails or accounts are involved. Contained laboratories use test accounts and volunteers who know the purpose. No simulated phishing is sent; the documented rules require approval by managers and staff representatives, ban lures about pay, health or job security and keep results aggregate and out of HR processes. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. Chapters 1–5 cover systems, networks, identities, scripting and scope through one logistics placement; chapters 6–15 configure, verify, troubleshoot, automate and integrate reporting and verification, with a contained laboratory; chapters 16–18 cover documentation and safety, a second contained laboratory and the supervised project. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Priya Raman** | Technical trainee | Invented |
| **Tom Hallett** | Instructor | Invented |
| **Eastvale Technical College** | Fictional college | Invented |
| **Kestrel Logistics** | Fictional logistics company, 300 staff, three depots | Invented |

### Core sources

Whitten and Tygar (1999), USENIX Security; Reason (1990), [doi:10.1017/CBO9781139062367](https://doi.org/10.1017/CBO9781139062367); Hansche et al. (2024), NIST SP 800-50r1; Adams and Sasse (1999), [doi:10.1145/322796.322806](https://doi.org/10.1145/322796.322806). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe the systems used at a logistics depot; (2) identify where staff interact with security during shifts; (3) record a baseline of security tasks.

### 1.1 Depot systems

Priya Raman, a technical trainee at the fictional Eastvale Technical College, joins the IT support team at the fictional Kestrel Logistics, a company with 300 staff across three depots. Her instructor, Tom Hallett, asks her to list the systems staff use. Warehouse workers use handheld scanners and shared terminals to log deliveries. Office staff use laptops, email and a dispatch system that holds customer addresses. Drivers use a mobile app for routes. Priya draws a simple diagram showing which group uses which system, and how the systems connect to the cloud services that run dispatch.

### 1.2 Security in shifts

Priya follows a warehouse shift and an office shift to see where security appears. Warehouse workers log into shared terminals with a single team password written on the wall, because each login takes time and shifts are busy. Office staff receive many emails from customers and carriers, some with attachments and links. Drivers sometimes receive texts claiming to be from the company about route changes. Priya notes each point and the pressure staff face there, such as loading deadlines or angry customers on the phone.

### 1.3 Baseline record

Priya records a baseline: number of systems, logins per shift, shared passwords in use, and how staff currently report anything suspicious. She finds there is no clear reporting route; most people tell their supervisor, who may or may not tell IT. She writes the baseline as a one-page summary for Tom and the IT lead. A baseline lets the team measure later whether changes improved things, and it shows where effort is most needed before any tool or policy is changed.

### Worked example

Priya maps depot systems, observes security points during shifts and records a baseline including a shared wall password and no reporting route.

> **Synthetic case.** Kestrel Logistics is synthetic.

### Errors and limits

Two shifts may not be typical. Observations should not record names.

### Exercises

- **EX001 — Wall password.** Why is the team password written on the wall? *Rubric:* 3 = individual logins take time during busy shifts;; 2 = time;; 1 = carelessness;; 0 = none.
- **EX002 — Driver texts.** What do drivers sometimes receive? *Rubric:* 3 = texts claiming route changes from the company;; 2 = fake texts;; 1 = vague;; 0 = none.
- **EX003 — Current reporting.** How do staff currently report suspicious messages? *Rubric:* 3 = tell their supervisor, who may tell IT;; 2 = supervisor;; 1 = a button;; 0 = none.
- **EX004 — Baseline purpose.** Why record a baseline? *Rubric:* 3 = to measure later whether changes helped;; 2 = comparison;; 1 = vague;; 0 = none.

### Synthesis

A baseline of systems and shift pressures shows where human-centred security is needed.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) explain how emails and texts reach staff; (2) describe why sender details can be faked; (3) configure simple warnings.

### 2.1 How messages arrive

Emails reach Kestrel through its cloud mail service, which passes them through a filter before delivering them. Texts reach drivers' phones through mobile networks. Priya learns that the sender shown on an email or text is easy to fake, because the basic protocols were designed to deliver messages, not to prove who sent them. Email authentication checks can detect some forgeries of Kestrel's own domain, but they cannot stop attackers who register similar-looking domains or send texts using a company name as the sender label.

### 2.2 Why fakes work

Priya studies a synthetic example: an email from a domain that differs from Kestrel's by one letter, asking office staff to update a customer's delivery address and to send an invoice copy. It passes authentication because the attacker owns that lookalike domain. Staff under time pressure read the familiar name and act. Whitten and Tygar (1999) showed that security tools leave users confused when the interface does not guide them, and Priya sees that staff need clear cues rather than technical knowledge.

### 2.3 Configuring warnings

With the IT lead, Priya configures an external tag on emails from outside Kestrel and a warning when a sender's display name matches a staff member but the address is external. She tests both with synthetic messages in a test mailbox before enabling them. She also drafts a short message for drivers stating that route changes always come through the route app, never by text. Each cue gives staff a simple signal at the moment of decision without requiring them to understand protocols.

### Worked example

Priya explains message delivery and forgery, analyses a lookalike domain example and configures external tags, name warnings and a driver message.

> **Synthetic case.** Examples are synthetic; Whitten and Tygar (1999) is real.

### Errors and limits

Tags lose effect if overused. Drivers may not read messages.

### Exercises

- **EX005 — Lookalike pass.** Why does the lookalike email pass authentication? *Rubric:* 3 = the attacker owns the lookalike domain;; 2 = ownership;; 1 = vague;; 0 = none.
- **EX006 — Whitten and Tygar.** What did Whitten and Tygar (1999) show? *Rubric:* 3 = unguided security interfaces confuse users;; 2 = usability;; 1 = vague;; 0 = none.
- **EX007 — Testing warnings.** Where were the warnings tested first? *Rubric:* 3 = a test mailbox with synthetic messages;; 2 = test mailbox;; 1 = live inboxes;; 0 = none.
- **EX008 — Driver rule.** What rule did Priya draft for drivers? *Rubric:* 3 = route changes only come through the route app;; 2 = app only;; 1 = vague;; 0 = none.

### Synthesis

Protocol limits leave staff to judge messages, so simple cues must guide them.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) replace a shared terminal password with usable individual logins; (2) configure screen locks for warehouse work; (3) manage accounts for seasonal staff.

### 3.1 Individual logins

Priya proposes replacing the wall password with badge logins on warehouse terminals. Each worker taps a badge to log in and taps again to log out, taking about two seconds. Individual logins let IT see who made each change, which helps investigate errors and misuse. She tests the badge readers on one terminal for a week. Workers find the tap quicker than typing the shared password. Making the secure option faster than the insecure one is the key to adoption. Supervisors support the trial.

### 3.2 Screen locks

Shared terminals stayed logged in for whole shifts. With badge logins, Priya configures the terminals to lock after two minutes of inactivity, since unlocking now takes a tap. Office laptops lock after five minutes and unlock with a fingerprint or PIN. She counts how often terminals were left unlocked before and after over a test week. The short lock time is accepted because the unlocking cost is small, which shows how usability and security can reinforce each other. The supervisors agree to the settings.

### Lab — Unlocked terminal minutes before and after badges

```python
# Unlocked terminal minutes per test week before and after badge logins (synthetic, 4 terminals).
before = [480, 500, 460, 480]; after = [20, 25, 18, 22]
print("before:", sum(before), "after:", sum(after))
```

Run with `python3 lab_unlocked.py`. Verified output:

```text
before: 1920 after: 85
```

### 3.3 Seasonal staff

Kestrel hires fifty seasonal workers each winter. Previously they shared accounts. Priya sets up a process: HR sends a list before each season, IT creates accounts with an end date, badges are issued at induction and accounts expire automatically at the end date. She writes a checklist for HR and IT. Seasonal staff receive a two-minute induction on reporting and badges. Automatic expiry removes the risk of old accounts remaining active, which no one would otherwise remember to remove. HR agrees to the checklist.

### Worked example

Priya replaces a shared password with badge logins, shortens screen locks and sets up expiring accounts for seasonal workers.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Badges can be lost or shared. End dates may need extension.

### Exercises

- **EX009 — Badge time.** How long does a badge login take? *Rubric:* 3 = about two seconds;; 2 = 2 seconds;; 1 = vague;; 0 = none.
- **EX010 — Lab unlocked minutes.** How did unlocked minutes change in the lab? *Rubric:* 3 = from 1,920 to 85 per week;; 2 = fall;; 1 = vague;; 0 = none.
- **EX011 — Lock acceptance.** Why is a two-minute lock accepted? *Rubric:* 3 = unlocking only needs a tap;; 2 = low cost;; 1 = vague;; 0 = none.
- **EX012 — Seasonal expiry.** How do seasonal accounts end? *Rubric:* 3 = they expire automatically at an end date;; 2 = expiry;; 1 = manual removal;; 0 = none.

### Synthesis

Usable identities make the secure option the quickest one.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) write a script to summarise reports from a CSV file; (2) use JSON for configuration; (3) avoid storing personal data unnecessarily.

### 4.1 Summarising reports

Once a reporting mailbox exists, Priya writes a Python script that reads a weekly CSV export with date, depot, category and verdict, and prints counts by depot and category. She uses Python's csv module so commas inside fields are handled correctly. She tests the script on a small file whose totals she knows. The summary replaces a manual count that took the IT lead an hour each week and often contained mistakes, freeing time for replying to reporters. The IT lead checks the first output.

### Lab — Weekly report summary from CSV

```python
# Weekly report summary from CSV (synthetic).
import csv, io, json
cfg = json.loads('{"depots": ["North", "South", "East"]}')
data = "date,depot,category,verdict\n" + "".join(f"2026-10-0{1 + i % 5},{d},{c},{v}\n" for i, (d, c, v) in enumerate(
    [("North", "fake carrier", "malicious")] * 7 + [("North", "newsletter", "harmless")] * 5 +
    [("South", "fake invoice", "malicious")] * 4 + [("South", "other", "harmless")] * 3 + [("East", "fake carrier", "malicious")] * 5))
counts = {d: 0 for d in cfg["depots"]}
for row in csv.DictReader(io.StringIO(data)): counts[row["depot"]] += 1
print(counts, "total", sum(counts.values()))
```

Run with `python3 lab_weekly.py`. Verified output:

```text
{'North': 12, 'South': 7, 'East': 5} total 24
```

### 4.2 JSON configuration

Priya stores settings, such as depot names and category labels, in a JSON file rather than inside the script. JSON is a simple text format of names and values that both people and programs can read. When a new depot opens, the IT lead updates the JSON file without changing code. Separating configuration from code makes scripts easier to maintain and reduces the chance of errors when someone less familiar with programming needs to make a change. She adds a short example file.

### 4.3 Avoiding personal data

The first export Priya receives includes reporter email addresses. She asks for them to be removed, because the summary needs only depot-level counts, and names could make staff feel monitored. The export now includes a random code instead. She stores files in a restricted folder and deletes them after four weeks. Good scripting practice includes thinking about what data the script handles and whether it needs them at all. The IT lead agrees with the change and records it in the data processing notes, and Tom praises her for raising the question early.

### Worked example

Priya writes a CSV summary script, moves settings to JSON and removes reporter addresses from the export.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Exports can change format. Random codes can sometimes be linked.

### Exercises

- **EX013 — CSV module reason.** Why use Python's csv module? *Rubric:* 3 = it handles commas inside fields;; 2 = parsing;; 1 = split;; 0 = none.
- **EX014 — Lab top depot.** Which depot had most reports in the lab? *Rubric:* 3 = North with 12;; 2 = North;; 1 = vague;; 0 = none.
- **EX015 — JSON benefit.** Why store settings in JSON? *Rubric:* 3 = changes need no code edits;; 2 = maintainability;; 1 = vague;; 0 = none.
- **EX016 — Removed field.** Which field was removed from the export? *Rubric:* 3 = reporter email addresses;; 2 = addresses;; 1 = vague;; 0 = none.

### Synthesis

Scripts should be tested, configurable and careful with personal data.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) define the scope of a technical human factors task; (2) agree permission and boundaries; (3) collect evidence that supports decisions.

### 5.1 Defining scope

Tom asks Priya to define the scope of her work: improving how staff report suspicious messages and verify unusual requests at Kestrel. In scope are the reporting mailbox, warning settings, verification procedures and short guidance. Out of scope are disciplinary matters, monitoring individual staff and any test that deceives staff without agreement. Writing scope down protects staff, the company and Priya, because everyone knows what she will and will not do during her placement. Tom and the IT lead sign the scope document.

### 5.2 Permission and boundaries

Priya obtains written permission from the IT lead and the operations manager for each activity, such as installing badge readers or running usability tests with volunteers. Staff representatives are informed. She agrees boundaries: tests use test mailboxes and synthetic messages; no simulated phishing is sent during her placement; and all data are reported in aggregate. NIST SP 800-50r1 (Hansche et al., 2024) emphasises planning and governance in learning programmes, and permission is the first step of that governance. Each permission is filed.

### 5.3 Collecting evidence

Priya collects evidence to support decisions: counts from the reporting export, timing tests of procedures, short surveys and observation notes without names. She records the source and date of each item. When she recommends a change, she points to the evidence behind it. Evidence-based recommendations are easier for managers to accept and to review later. She also records evidence that contradicts her expectations, such as staff preferring email reminders, because hiding it would mislead. She keeps all items in one dated folder.

### Worked example

Priya writes scope, obtains permission with boundaries and collects dated evidence including contradicting findings.

> **Synthetic case.** The scope is synthetic; SP 800-50r1 is real.

### Errors and limits

Scope creep. Evidence collection takes time.

### Exercises

- **EX017 — Out of scope.** Name an item out of scope. *Rubric:* 3 = monitoring individual staff;; 2 = monitoring;; 1 = reporting mailbox;; 0 = none.
- **EX018 — Simulation boundary.** What boundary applies to simulated phishing? *Rubric:* 3 = none sent during the placement;; 2 = none;; 1 = monthly;; 0 = no answer.
- **EX019 — Evidence record.** What does Priya record with each item of evidence? *Rubric:* 3 = source and date;; 2 = provenance;; 1 = vague;; 0 = none.
- **EX020 — Contradicting evidence.** Why record contradicting evidence? *Rubric:* 3 = hiding it would mislead;; 2 = honesty;; 1 = vague;; 0 = none.

### Synthesis

Clear scope, permission and evidence protect people and support sound decisions.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Human factors and cyber policy: system model

### Learning outcomes

You will (1) model the reporting process from message arrival to feedback; (2) identify steps where reports are lost; (3) choose improvements by step.

### 6.1 The process

Priya models reporting at Kestrel as a series of steps: a suspicious message arrives; the person notices; they decide to report; they find how to report; they send it; IT reviews; IT replies. If any step fails, the warning never reaches IT or the reporter never learns whether they were right. She draws the process with arrows and adds where each step happens, such as on a warehouse terminal, an office laptop or a driver's phone. Tom reviews the drawing. He suggests labels.

### 6.2 Where reports are lost

Using survey answers and the reporting export, Priya estimates how many potential reports survive each step. Many staff notice suspicious messages, but fewer decide to report because they are unsure whether IT wants them. Some cannot find how to report on phones. The lab multiplies the step rates to estimate how many of every hundred suspicious messages become reports with replies. The biggest loss is at the decision step, which tells her where improvement matters most. She shares the result with the IT lead.

### Lab — Reporting process losses by step

```python
# Reporting process losses by step for 100 suspicious messages (synthetic).
steps = [("notice", 0.75), ("decide", 0.40), ("find how", 0.80), ("send", 0.98), ("IT review", 0.95), ("reply", 0.95)]
n = 100.0
for s, r in steps: n2 = n * r; print(f"{s}: {n:.0f} -> {n2:.0f}"); n = n2
print(f"replied reports: {n:.0f}")
```

Run with `python3 lab_steps.py`. Verified output:

```text
notice: 100 -> 75
decide: 75 -> 30
find how: 30 -> 24
send: 24 -> 24
IT review: 24 -> 22
reply: 22 -> 21
replied reports: 21
```

### 6.3 Improvements by step

Priya chooses improvements by step. For the decision step, a clear message from managers that unsure reports are welcome. For finding how to report, a report button in email and a short phone number for drivers. For feedback, replies within a working day. She estimates that fixing the decision step would add more reports than the other two combined. Modelling the process turns vague concern about staff awareness into specific, targeted changes. The operations manager approves all three changes. Work starts the following week.

### Worked example

Priya models reporting as seven steps, finds the decision step loses most and targets improvements by step.

> **Synthetic case.** Rates are synthetic.

### Errors and limits

Step rates are estimates. Steps interact.

### Exercises

- **EX021 — Step count.** How many steps does Priya's model have? *Rubric:* 3 = seven;; 2 = 7;; 1 = three;; 0 = none.
- **EX022 — Lab survivors.** How many of 100 suspicious messages become replied reports in the lab? *Rubric:* 3 = 21;; 2 = 21, without explanation;; 1 = vague;; 0 = none.
- **EX023 — Biggest loss.** Which step loses the most? *Rubric:* 3 = the decision to report;; 2 = decision;; 1 = noticing;; 0 = none.
- **EX024 — Decision fix.** What fixes the decision step? *Rubric:* 3 = managers saying unsure reports are welcome;; 2 = message;; 1 = vague;; 0 = none.

### Synthesis

A step model shows where reports are lost and which fix matters most.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Human factors and cyber policy: data and telemetry

### Learning outcomes

You will (1) identify data sources for reporting and verification; (2) define what telemetry to collect; (3) respect privacy in telemetry.

### 7.1 Data sources

Priya lists data sources for monitoring the human side of security at Kestrel: the reporting mailbox export, the mail filter's logs of blocked and delivered malicious messages, the accounting system's log of held payment changes, help desk tickets and short quarterly surveys. Each source answers different questions. Together they show how many attacks reach staff, how many are reported, how quickly IT responds and whether verification controls are being used as intended. She lists each source in a short table. None needs new software.

### 7.2 Choosing telemetry

Telemetry means data collected automatically from systems. Priya defines a small set: time each malicious message was delivered; time of first report; time of verdict; number of held payment changes and their outcome; and count of badge logins per terminal per shift. She avoids collecting anything not linked to a decision. Collecting too much data adds storage, cost and privacy risk without improving decisions, and it can make staff feel watched. The IT lead agrees with the list. Each item has a stated purpose.

### 7.3 Privacy in telemetry

Badge login data could show when each person worked, which could be misused to monitor productivity. Priya proposes that badge data be used only for security investigations and aggregated counts, with access limited to IT and a clear statement in the staff privacy notice. Reporting data contain no names. The operations manager agrees in writing. Respecting privacy in telemetry keeps the trust that the reporting programme depends on, and it prevents security data drifting into uses staff never agreed to. Staff are told.

### Worked example

Priya lists data sources, defines minimal telemetry and limits badge data use with a written agreement.

> **Synthetic case.** Data uses are synthetic.

### Errors and limits

Agreements can be forgotten. Logs may be incomplete.

### Exercises

- **EX025 — Telemetry definition.** What is telemetry? *Rubric:* 3 = data collected automatically from systems;; 2 = automatic;; 1 = surveys;; 0 = none.
- **EX026 — Collection rule.** What rule guides telemetry collection? *Rubric:* 3 = collect only what links to a decision;; 2 = minimal;; 1 = everything;; 0 = none.
- **EX027 — Badge data risk.** What misuse could badge data allow? *Rubric:* 3 = monitoring productivity;; 2 = surveillance;; 1 = vague;; 0 = none.
- **EX028 — Badge data limit.** What is badge data limited to? *Rubric:* 3 = security investigations and aggregated counts;; 2 = limited use;; 1 = vague;; 0 = none.

### Synthesis

Minimal telemetry, used only for agreed purposes, supports monitoring without eroding trust.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Human factors and cyber policy: failure modes

### Learning outcomes

You will (1) identify human-related failure modes; (2) distinguish slips, lapses and mistakes; (3) match defences to failure types.

### 8.1 Failure modes

Priya lists ways the human side of security can fail at Kestrel: a dispatcher clicks a link in a fake carrier email; a driver follows a fake text to a fake login page; an accounts clerk changes a customer's bank details after a convincing email; a supervisor forgets to tell IT about a suspicious call. Each failure has different causes. Listing failures before they happen lets the team design defences in advance rather than reacting after damage. Supervisors add two more.

### 8.2 Slips, lapses, mistakes

Reason (1990) distinguished slips, where an action goes wrong despite a correct plan, such as clicking the wrong button; lapses, where something is forgotten, such as not passing on a report; and mistakes, where the plan itself is wrong, such as believing a fake email is genuine. Priya classifies each failure mode. The supervisor's forgotten report is a lapse; the bank detail change is a mistake caused by deception. The classification guides the choice of defence. She explains the terms to supervisors.

### 8.3 Matching defences

Slips are reduced by design, such as confirmation steps for risky actions. Lapses are reduced by removing memory demands, such as a report button that sends directly to IT instead of through supervisors. Mistakes caused by deception are reduced by verification procedures that do not depend on judging appearance, such as calling the customer on a known number. Priya presents a table matching each failure to a defence type, which shows managers that more training is not the answer to every failure.

### Worked example

Priya lists four failure modes, classifies them using Reason's slips, lapses and mistakes and matches each to a defence type.

> **Synthetic case.** Failures are synthetic; Reason (1990) is real.

### Errors and limits

Classifications overlap. Defences have side effects.

### Exercises

- **EX029 — Lapse example.** Which failure is a lapse? *Rubric:* 3 = the supervisor forgetting to tell IT;; 2 = forgetting;; 1 = the bank change;; 0 = none.
- **EX030 — Mistake definition.** What is a mistake in Reason's terms? *Rubric:* 3 = the plan itself is wrong;; 2 = wrong plan;; 1 = wrong action;; 0 = none.
- **EX031 — Lapse defence.** How are lapses reduced? *Rubric:* 3 = by removing memory demands;; 2 = memory;; 1 = training;; 0 = none.
- **EX032 — Deception defence.** What reduces mistakes caused by deception? *Rubric:* 3 = verification not based on appearance;; 2 = callbacks;; 1 = vague;; 0 = none.

### Synthesis

Classifying human failures points to defences that fit, beyond more training.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Human factors and cyber policy: tools and methods

### Learning outcomes

You will (1) use a short survey and observation to study reporting; (2) run a simple usability test; (3) combine methods into findings.

### 9.1 Survey and observation

Priya runs a five-question anonymous survey for all staff and observes how reporting happens in each depot, with permission and without recording names. She receives 210 responses from 300 staff. The most common barrier is not knowing how to report from a terminal or phone. Observation shows that warehouse terminals have no email client, so workers have no way to report a suspicious message they see on a shared screen, such as a pop-up claiming to be from IT. She writes up her notes the same day.

### Lab — Survey barriers among 210 responses

```python
# Barriers among 210 synthetic survey responses (multiple choice).
b = {"don't know how from terminal or phone": 88, "unsure IT wants it": 71, "too busy": 52, "never heard back": 30}
for k, v in sorted(b.items(), key=lambda x: -x[1]): print(f"{k}: {v}/210 = {v / 210:.0%}")
```

Run with `python3 lab_survey.py`. Verified output:

```text
don't know how from terminal or phone: 88/210 = 42%
unsure IT wants it: 71/210 = 34%
too busy: 52/210 = 25%
never heard back: 30/210 = 14%
```

### 9.2 Usability test

Priya tests a proposed report method for warehouse terminals: a desktop shortcut that opens a short form. Six volunteer workers try it with synthetic pop-ups on a test terminal, knowing they are testing the form. Five complete the report in under twenty seconds; one is confused by the word incident. She changes the label to Report something odd. Small usability tests catch wording problems that designers miss because they already know what they meant. All six then succeed. The test takes an hour.

### 9.3 Combining methods

Priya combines survey, observation and testing into findings: staff want to report but lack a route on terminals and phones; the word incident is off-putting; and many are unsure whether IT wants reports. She proposes the terminal form, a driver text number and a clear welcome message from managers. Each finding cites its evidence. Combining methods gives a fuller picture than any one method, because surveys count, observation reveals context and tests check solutions. The operations manager approves the proposals. Work begins soon.

### Worked example

Priya surveys 210 staff, observes depots, tests a terminal form with six volunteers and combines methods into findings.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Self-report bias. Small tests.

### Exercises

- **EX033 — Response rate.** What was the survey response rate? *Rubric:* 3 = 70%;; 2 = 210 of 300;; 1 = 210%;; 0 = none.
- **EX034 — Lab top barrier.** What was the top barrier in the lab? *Rubric:* 3 = not knowing how to report from terminals or phones, 88 of 210;; 2 = how;; 1 = vague;; 0 = none.
- **EX035 — Terminal gap.** Why could warehouse workers not report? *Rubric:* 3 = terminals have no email client;; 2 = no route;; 1 = vague;; 0 = none.
- **EX036 — Label change.** What label replaced incident? *Rubric:* 3 = Report something odd;; 2 = plain words;; 1 = vague;; 0 = none.

### Synthesis

Combined methods reveal barriers and test fixes before rollout.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Human factors and cyber policy: control configuration

### Learning outcomes

You will (1) configure reporting routes for email, terminals and phones; (2) set up verification controls for payment and address changes; (3) document configurations clearly.

### 10.1 Reporting routes

Priya configures three reporting routes. In email, a report button sends the message to the shared IT mailbox and shows a thank-you note at once. On warehouse terminals, the desktop shortcut opens the form labelled Report something odd, which asks for a short description and the terminal number, with no name required. For drivers, a short company number accepts forwarded texts. She tests each route end to end with synthetic messages and confirms that all three arrive in the same triage queue for the IT team.

### 10.2 Verification controls

Fake requests to change customer delivery addresses or bank details are a major risk at Kestrel. Priya works with the accounts team to configure the accounting system so that any change to bank details is held until a second person confirms it by calling the customer on the number already on file. In the dispatch system, address changes requested by email are flagged for a quick call before the next delivery. These controls move the decision away from judging an email's appearance to a simple check.

### 10.3 Documentation

Priya documents each configuration on one page: what it does, why it exists, how to test it and who owns it. She includes screenshots and the date of the last test. The IT lead stores the pages in the shared support folder. Clear documentation lets anyone on the team check or repair a control, and it records the reasons for each setting, which prevents someone from removing a control later because they do not understand what it was for. Tom reviews the pages.

### Worked example

Priya configures email, terminal and phone reporting routes, sets payment and address verification holds and documents each on one page.

> **Synthetic case.** Configurations are synthetic.

### Errors and limits

Holds can delay genuine changes. Phone numbers on file may be outdated.

### Exercises

- **EX037 — Terminal form.** What does the terminal form ask for? *Rubric:* 3 = a short description and terminal number, no name;; 2 = minimal;; 1 = name;; 0 = none.
- **EX038 — Driver route.** How do drivers report suspicious texts? *Rubric:* 3 = forward them to a short company number;; 2 = forward;; 1 = vague;; 0 = none.
- **EX039 — Bank change control.** How is a bank detail change confirmed? *Rubric:* 3 = a second person calls the number on file;; 2 = callback;; 1 = email reply;; 0 = none.
- **EX040 — Documentation value.** Why record the reason for each setting? *Rubric:* 3 = so nobody removes it without understanding;; 2 = rationale;; 1 = vague;; 0 = none.

### Synthesis

Configured routes and holds make reporting easy and verification routine.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Human factors and cyber policy: verification

### Learning outcomes

You will (1) verify that controls work as configured; (2) check controls from the user's point of view; (3) record verification results.

### 11.1 Technical checks

Priya verifies each control. She reports synthetic messages through each route and confirms they arrive in the triage queue within a minute. She submits a synthetic bank detail change and confirms it is held. She checks that external tags appear and that name-match warnings trigger. She checks that seasonal accounts expire on their end date using a test account. Each check has an expected result written before testing, so that she can say clearly whether the control passed or failed. Each check is timed.

### 11.2 User-side checks

Technical checks do not show what staff experience. Priya asks three volunteers in different roles to use each control while she watches. A driver finds that his phone's messaging app makes forwarding a text awkward, needing five taps. An accounts clerk is unsure what to do when a held change appears. Priya writes a one-line instruction for the clerk and a short guide with pictures for drivers. User-side checks find problems that matter in practice but would not appear in any log.

### Lab — Verification results for seven controls

```python
# Verification results for seven controls (synthetic).
r = [("email button", True), ("terminal form", True), ("driver number", False), ("bank change hold", True),
     ("address flag", False), ("external tag", True), ("seasonal expiry", True)]
print("first pass:", sum(ok for _, ok in r), "of", len(r)); print("needed fixes:", [n for n, ok in r if not ok])
```

Run with `python3 lab_verify.py`. Verified output:

```text
first pass: 5 of 7
needed fixes: ['driver number', 'address flag']
```

### 11.3 Recording results

Priya records each check in a table with date, method, expected result, actual result and any fix. Of seven controls, five pass first time and two need fixes before passing. She shares the table with the IT lead and Tom. The table becomes the baseline for re-verification after future updates. Recording failures as well as passes shows that verification was genuine, and it helps the team notice if the same control fails repeatedly over time. The two fixed controls are the driver number and the address flag.

### Worked example

Priya runs technical and user-side checks on seven controls, fixes two and records results.

> **Synthetic case.** Checks are synthetic.

### Errors and limits

Checks reflect one moment. Volunteers may not represent everyone.

### Exercises

- **EX041 — Expected result.** Why write expected results before testing? *Rubric:* 3 = so pass or fail is clear;; 2 = clarity;; 1 = vague;; 0 = none.
- **EX042 — Driver problem.** What problem did the driver find? *Rubric:* 3 = forwarding a text needed five taps;; 2 = awkward;; 1 = vague;; 0 = none.
- **EX043 — Lab pass rate.** How many controls passed first time in the lab? *Rubric:* 3 = 5 of 7;; 2 = five;; 1 = 7 of 7;; 0 = none.
- **EX044 — Table use.** What does the table become? *Rubric:* 3 = the baseline for re-verification;; 2 = baseline;; 1 = vague;; 0 = none.

### Synthesis

Verification from both technical and user sides, with recorded results, proves controls work.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) test reporting methods in a contained environment; (2) measure task time and success; (3) report limits honestly.

### 12.1 Contained setup

In the first contained laboratory, Priya sets up a test terminal, a test email account and a spare phone, all disconnected from Kestrel's live systems. She prepares synthetic suspicious messages for each. Nine volunteers, three from each staff group, take part. They know they are testing the reporting methods, not being tested on their judgement. Each volunteer reports one message using the old method, telling a supervisor who then emails IT, and one using the new route for their group. Each session takes fifteen minutes.

### 12.2 Measurements

Priya measures time from seeing the message to the report reaching the triage queue. With the old method, reports take several minutes because supervisors are busy; with new routes, they take under half a minute. Two old-method reports never arrive because the supervisor role-player forgot, mirroring the lapse identified in chapter 8. The lab computes average times by method. Volunteers say the new routes feel easier, though drivers still find forwarding fiddly. She notes every hesitation in a short log and shares the log with the app supplier.

### Lab — Old and new reporting times in the contained lab

```python
# Old vs new reporting times in seconds (synthetic, 9 volunteers; None = never arrived).
old = [210, 300, None, 250, 280, None, 240, 270, 270]; new = [18, 25, 20, 22, 30, 19, 21, 24, 19]
o = [x for x in old if x is not None]
print(f"old: mean {sum(o) / len(o):.0f} s, {old.count(None)} never arrived; new: mean {sum(new) / len(new):.0f} s")
```

Run with `python3 lab_contained.py`. Verified output:

```text
old: mean 260 s, 2 never arrived; new: mean 22 s
```

### 12.3 Honest limits

Priya reports results with limits: nine volunteers is a small group; the lab was calmer than a real shift; and the old-method times depend on how busy the supervisor role-player was. She recommends adopting the new routes and measuring real reporting times after launch. She also notes that the driver route needs a simpler forwarding option. Honest limits help managers trust the findings and plan sensible follow-up rather than treating a small test as final proof. Managers accept the recommendation. Tom agrees.

### Worked example

Priya tests old and new reporting in a contained lab with nine volunteers and reports large time savings with honest limits.

> **Synthetic case.** The lab is synthetic.

### Errors and limits

Small sample. Calm conditions.

### Exercises

- **EX045 — Isolation.** Why is the lab disconnected from live systems? *Rubric:* 3 = to keep tests contained and safe;; 2 = containment;; 1 = vague;; 0 = none.
- **EX046 — Lost reports.** What happened to two old-method reports? *Rubric:* 3 = they never arrived because the supervisor forgot;; 2 = lapse;; 1 = vague;; 0 = none.
- **EX047 — Lab times.** What average times did the lab show? *Rubric:* 3 = old 260 seconds, new 22 seconds;; 2 = faster;; 1 = vague;; 0 = none.
- **EX048 — Driver follow-up.** What follow-up is needed for drivers? *Rubric:* 3 = a simpler forwarding option;; 2 = simpler;; 1 = vague;; 0 = none.

### Synthesis

Contained tests show the value of direct reporting routes and need honest limits.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Human factors and cyber policy: troubleshooting

### Learning outcomes

You will (1) diagnose problems in the reporting service; (2) separate technical and human causes; (3) fix causes and prevent recurrence.

### 13.1 The problem

Two months after launch, reports from South depot terminals stop. Priya investigates. The terminal form still exists, but submissions fail silently because a network change blocked the form's server. Workers who tried to report saw no error and assumed it worked, so nobody raised a problem. Meanwhile, the IT lead had noticed the drop but assumed South simply had fewer suspicious messages. Priya checks the mail filter logs and confirms that South received a normal number of malicious messages during the period.

### 13.2 Separating causes

Priya separates causes. The technical cause was the network change, made without a test of dependent services. The design cause was that the form showed no confirmation, so failures were invisible to users. The human cause was that a drop in reports was interpreted as good news without checking. Each cause needs its own fix. Treating only the technical cause would leave the service vulnerable to the next silent failure, whatever its source, and would miss the lesson about interpreting data.

### 13.3 Fixes and prevention

Priya and the IT lead fix all three causes. The network change is corrected and added to a checklist of services to test after changes. The form now shows a confirmation number when a report is received and an error message if it fails. A weekly check compares reports with malicious messages delivered for each depot and flags any depot where reports fall sharply. She records the incident in the troubleshooting log. The weekly check would have caught the South problem within days.

### Worked example

Priya traces a South depot reporting drop to a network change, a missing confirmation and a misread metric, and fixes all three.

> **Synthetic case.** The incident is synthetic.

### Errors and limits

Weekly checks need attention. Checklists can be skipped.

### Exercises

- **EX049 — Silent failure.** Why did workers not notice the failure? *Rubric:* 3 = the form showed no error or confirmation;; 2 = silent;; 1 = vague;; 0 = none.
- **EX050 — Misread drop.** How did the IT lead misread the drop? *Rubric:* 3 = as fewer suspicious messages;; 2 = good news;; 1 = vague;; 0 = none.
- **EX051 — Form fix.** What does the form now show? *Rubric:* 3 = a confirmation number or an error;; 2 = feedback;; 1 = vague;; 0 = none.
- **EX052 — Weekly check.** What does the weekly check compare? *Rubric:* 3 = reports with malicious messages delivered per depot;; 2 = ratio;; 1 = vague;; 0 = none.

### Synthesis

Troubleshooting finds technical, design and human causes, and prevention needs all three fixed.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Human factors and cyber policy: automation

### Learning outcomes

You will (1) automate triage steps for reports; (2) keep human review where needed; (3) monitor automated steps.

### 14.1 Automating triage

Priya automates routine triage. Reports about the same message are grouped. A thank-you note is sent immediately. If a reported message matches one already confirmed as malicious, the reporter receives the standard verdict and the message is removed from other mailboxes automatically. The IT lead reviews only new messages. The lab counts how many reports in a synthetic busy week needed human review after automation, showing how much time is saved for replies and investigation. The rules are simple to read and change.

### Lab — Reports needing human review after automation

```python
# Reports needing human review after automation in a synthetic busy week.
total, dup, known = 80, 51, 17
print(f"total {total}; duplicates {dup}; known verdicts {known}; human review {total - dup - known} ({(total - dup - known) / total:.0%})")
```

Run with `python3 lab_triage.py`. Verified output:

```text
total 80; duplicates 51; known verdicts 17; human review 12 (15%)
```

### 14.2 Human review

Priya considers whether to let a scoring service decide verdicts for all messages. She decides against it, because wrongly labelling a real customer email as malicious could cause a missed delivery or a lost customer, and wrongly labelling a fake as safe could cause fraud. Human review stays for new messages. She notes that automation should handle what is certain and repetitive, while people handle what is uncertain or has serious consequences. The IT lead agrees with this division of work and records it in the triage runbook.

### 14.3 Monitoring automation

Automated steps can fail without anyone noticing, as the South depot incident showed. Priya adds a daily log line for each automated step and a weekly summary that lists failures. She also samples ten automated verdicts each month for the IT lead to check by hand. In the first month, all ten are correct. Monitoring gives the team confidence in automation and catches errors before they harm trust in the reporting service. The summary arrives every Monday morning by email. Results are logged.

### Worked example

Priya automates grouping, thanks and known verdicts, keeps human review for new messages and monitors automation with logs and samples.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Known lists need updates. Samples may miss rare errors.

### Exercises

- **EX053 — Lab review share.** How many of 80 reports needed human review in the lab? *Rubric:* 3 = 12;; 2 = 15%;; 1 = 80;; 0 = none.
- **EX054 — Scoring service.** Why not let a scoring service decide all verdicts? *Rubric:* 3 = mislabelling causes lost customers or fraud;; 2 = consequences;; 1 = cost;; 0 = none.
- **EX055 — Automation rule.** What should automation handle? *Rubric:* 3 = what is certain and repetitive;; 2 = routine;; 1 = judgement;; 0 = none.
- **EX056 — Monthly sample.** What monthly check did Priya add? *Rubric:* 3 = hand-checking ten automated verdicts;; 2 = sample;; 1 = vague;; 0 = none.

### Synthesis

Automation speeds feedback when it handles certainty and leaves judgement to people.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Human factors and cyber policy: integration and dependencies

### Learning outcomes

You will (1) connect reporting to incident response and customer service; (2) identify dependencies on people and suppliers; (3) reduce single points of failure.

### 15.1 Integration

Priya links reporting to incident response: when a malicious message reached many staff, the IT lead removes it, blocks the sender and checks whether anyone entered details. She also links it to customer service. When customers report fake delivery texts using Kestrel's name, customer service forwards them to the same triage queue, and a notice is placed on the website. Integration means one queue sees all reports, so patterns affecting both staff and customers are noticed quickly. Customer service staff receive a short briefing.

### 15.2 Dependencies

Priya lists dependencies: the IT lead does most triage; the mail provider runs the report button; a contractor maintains the terminal form; and the accounts system's hold feature depends on a vendor update schedule. She marks the IT lead as a single point of failure, since triage stops when he is away. She also notes that the driver number depends on one mobile contract. Mapping dependencies shows what the reporting service relies on and where it could break. She shares the list with Tom.

### 15.3 Reducing single points

To reduce dependence on the IT lead, Priya trains a second team member in triage using a short runbook and arranges a rota. She asks the contractor to provide a support contact for the terminal form. She records the mobile contract renewal date in the team calendar. Reducing single points of failure costs little but makes the service reliable during leave, illness and staff changes, which are inevitable in any small team. The rota starts the following month. Both changes are recorded in the runbook.

### Worked example

Priya integrates reporting with response and customer service, maps dependencies and adds a triage backup and supplier contacts.

> **Synthetic case.** Integration is synthetic.

### Errors and limits

Backups lose skill if unused. Contracts change.

### Exercises

- **EX057 — Customer reports.** What happens to customer reports of fake texts? *Rubric:* 3 = forwarded to triage and a website notice posted;; 2 = integration;; 1 = vague;; 0 = none.
- **EX058 — Single point.** Who is the main single point of failure? *Rubric:* 3 = the IT lead;; 2 = one person;; 1 = the contractor;; 0 = none.
- **EX059 — Triage backup.** How is dependence on the IT lead reduced? *Rubric:* 3 = training a second person with a runbook and rota;; 2 = backup;; 1 = vague;; 0 = none.
- **EX060 — Contract risk.** Which supplier risk is tracked in the calendar? *Rubric:* 3 = the mobile contract renewal;; 2 = renewal;; 1 = vague;; 0 = none.

### Synthesis

Integration widens what reporting sees, and backups keep it running.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write runbooks for the reporting service; (2) include safety and ethics rules; (3) keep documentation current.

### 16.1 Runbooks

Priya writes runbooks for triage, verification holds, the weekly depot check and seasonal account setup. Each runbook states its purpose, steps, tools, expected results and what to do if something goes wrong. She uses numbered steps and screenshots. She tests each runbook by watching the second team member follow it without help, then fixes steps that caused hesitation. Runbooks let the service continue when the person who built it is absent or has moved on. Each runbook has a version number.

### 16.2 Safety and ethics rules

Priya includes rules in the documentation: never send simulated phishing without approval from the operations manager and staff representatives; never use lures about pay, health or job security; report results only in aggregate; never use reporting or click data in disciplinary or performance processes; and use test accounts and synthetic messages for any testing. She cites NIST SP 800-50r1 and the ENISA culture guidelines as background. Writing these rules down protects staff from well-meant but harmful experiments. The operations manager signs them.

### 16.3 Keeping it current

Documentation decays as systems change. Priya adds a review date to every page and a line at the top saying who owns it. She sets a calendar reminder for quarterly review. When the network change incident happened, she updated three pages within a day. She explains to Tom that outdated documentation can be worse than none, because people trust it, and that ownership and review dates are what keep documents useful over time. The IT lead adopts this practice. Owners confirm reviews.

### Worked example

Priya writes tested runbooks, records ethics rules for any simulation or testing and sets owners and review dates.

> **Synthetic case.** Documentation is synthetic; SP 800-50r1 and the ENISA guidelines are real.

### Errors and limits

Reviews get skipped. Rules need enforcing.

### Exercises

- **EX061 — Runbook test.** How were runbooks tested? *Rubric:* 3 = a colleague followed them unaided;; 2 = walkthrough;; 1 = vague;; 0 = none.
- **EX062 — Banned lures.** Which lures are banned? *Rubric:* 3 = pay, health or job security;; 2 = distress;; 1 = vague;; 0 = none.
- **EX063 — Data rule.** Where must reporting and click data never be used? *Rubric:* 3 = disciplinary or performance processes;; 2 = HR;; 1 = vague;; 0 = none.
- **EX064 — Outdated danger.** Why can outdated documentation be worse than none? *Rubric:* 3 = people trust it;; 2 = misplaced trust;; 1 = vague;; 0 = none.

### Synthesis

Documentation includes steps, ethics rules and ownership so the service stays safe and current.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) test the effect of quick feedback on later reporting in a contained exercise; (2) analyse results simply; (3) recommend practice.

### 17.1 Exercise design

In the second contained laboratory, Priya tests whether quick feedback encourages people to report again. Twelve volunteers, who know the purpose, use test accounts over two sessions a week apart. In session one, each reports synthetic messages; half receive a short verdict within minutes and half receive nothing. In session two, all receive a new batch and Priya counts how many they report. The design is approved by Tom and the operations manager, and volunteers can withdraw at any time. Session times suit shifts.

### 17.2 Results

The lab compares session two reporting between the two groups. Volunteers who received quick feedback report more of the new messages than those who did not. Priya notes that twelve people is a small group and that volunteers knew the purpose, which could affect behaviour. Still, the result is consistent with interviews and with earlier findings that feedback matters. She presents the counts and the difference without claiming more than the small test shows. Feedback reached 87% against 57%. She shares the counts with volunteers.

### Lab — Session two reporting with and without feedback

```python
# Session two: messages reported out of 30 per group (6 volunteers x 5 messages), synthetic.
fb, nofb = 26, 17
print(f"feedback group {fb}/30 = {fb / 30:.0%}; no-feedback group {nofb}/30 = {nofb / 30:.0%}")
```

Run with `python3 lab_feedback.py`. Verified output:

```text
feedback group 26/30 = 87%; no-feedback group 17/30 = 57%
```

### 17.3 Recommendation

Priya recommends that every real report receive a reply within one working day and that automated verdicts be used where possible to speed this up. She suggests that the IT lead track reply times weekly. She also recommends a brief explanation in each verdict of what made the message suspicious, so that staff learn from each case. Her recommendation is cheap and builds on several sources of evidence, which makes managers willing to adopt it. The IT lead adopts it at once.

### Worked example

Priya runs a contained feedback exercise with twelve volunteers, finds more later reporting after quick feedback and recommends replies within a day.

> **Synthetic case.** The exercise is synthetic.

### Errors and limits

Volunteers knew the purpose. Small group.

### Exercises

- **EX065 — Exercise groups.** How were the two groups treated in session one? *Rubric:* 3 = half got quick verdicts, half got nothing;; 2 = feedback;; 1 = vague;; 0 = none.
- **EX066 — Lab result.** What did the lab show for session two reporting? *Rubric:* 3 = 26 of 30 with feedback versus 17 of 30 without;; 2 = higher;; 1 = vague;; 0 = none.
- **EX067 — Verdict content.** What should each verdict briefly include? *Rubric:* 3 = what made the message suspicious;; 2 = explanation;; 1 = vague;; 0 = none.
- **EX068 — Reply target.** What reply target did Priya recommend? *Rubric:* 3 = within one working day;; 2 = one day;; 1 = vague;; 0 = none.

### Synthesis

Contained exercises can support simple, cheap improvements such as fast feedback.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) deliver a complete improvement under supervision; (2) evaluate it after launch; (3) hand it over with documentation.

### 18.1 The project

For her supervised project, Priya delivers a simpler reporting route for drivers. Instead of forwarding texts, drivers tap a Report button in the route app, which captures the suspicious text's sender and content after the driver pastes it, and sends it to triage. She works with the app supplier, tests the feature with five drivers in a test environment and launches it after Tom and the operations manager approve. Drivers receive a one-minute video showing how to use it. Drivers like the video.

### 18.2 Evaluation

After six weeks, Priya compares driver reports before and after the change. Reports of fake texts rose, and the median time from receipt to report fell. Drivers in a short survey say the button is easier than forwarding. The lab summarises the figures. She also checks that triage time did not grow too much and finds that automatic grouping kept it manageable. She notes that six weeks is short and that an attack campaign in week four may have raised reports.

### Lab — Driver reports before and after the app button

```python
# Driver reports of fake texts, six weeks before vs after the app button (synthetic).
before = [120, 95, 60, 150, 80, 40]; after = [5, 8, 12, 15, 20, 9, 10, 14, 12, 18, 11, 25, 7, 13, 16, 30, 6, 12, 22]
m = lambda x: sorted(x)[len(x) // 2]
print(f"before: {len(before)} reports, median {m(before)} min; after: {len(after)} reports, median {m(after)} min")
```

Run with `python3 lab_drivers.py`. Verified output:

```text
before: 6 reports, median 95 min; after: 19 reports, median 12 min
```

### 18.3 Handover

Priya writes a runbook for the app route, adds it to the verification table and trains the second triage person. She presents the project to Tom, the IT lead and the operations manager, covering the problem, design, test, results and limits. The operations manager asks to extend the app button to warehouse handheld scanners. Tom notes that Priya's project shows the technical role at its best: practical, tested, respectful of users and documented so others can maintain it. Tom signs off the project.

### Worked example

Priya delivers an in-app report button for drivers, evaluates six weeks of results and hands over with runbook and training.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Six weeks is short. Campaigns can inflate reports.

### Exercises

- **EX069 — Driver route.** What replaced forwarding for drivers? *Rubric:* 3 = a Report button in the route app;; 2 = app button;; 1 = vague;; 0 = none.
- **EX070 — Lab change.** What did the lab show for driver reports? *Rubric:* 3 = 6 to 19 reports and median 95 to 12 minutes;; 2 = rise;; 1 = vague;; 0 = none.
- **EX071 — Confounder.** What may have raised reports besides the button? *Rubric:* 3 = an attack campaign in week four;; 2 = campaign;; 1 = vague;; 0 = none.
- **EX072 — Next request.** What did the operations manager ask for next? *Rubric:* 3 = extend the button to handheld scanners;; 2 = scanners;; 1 = vague;; 0 = none.

### Synthesis

A supervised project delivers, evaluates and hands over a practical improvement.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Priya Raman, Tom Hallett, Eastvale Technical College, Kestrel Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Because each login takes time and shifts are busy.

**EX002.** Texts claiming to be from the company about route changes.

**EX003.** They tell their supervisor, who may or may not tell IT.

**EX004.** So the team can measure later whether changes improved things.

**EX005.** Because the attacker owns the lookalike domain, so its messages authenticate.

**EX006.** That security tools confuse users when interfaces do not guide them.

**EX007.** In a test mailbox using synthetic messages.

**EX008.** That route changes always come through the route app, never by text.

**EX009.** About two seconds.

**EX010.** From 1,920 to 85 unlocked minutes per week.

**EX011.** Because unlocking only requires a badge tap.

**EX012.** They expire automatically at a set end date.

**EX013.** Because it correctly handles quoted fields and commas inside them.

**EX014.** North depot, with 12 reports.

**EX015.** So settings can be updated without changing the code.

**EX016.** Reporter email addresses.

**EX017.** Disciplinary matters, monitoring individual staff or deceptive tests without agreement.

**EX018.** No simulated phishing is sent during her placement.

**EX019.** Its source and date.

**EX020.** Because hiding it would mislead decision-makers.

**EX021.** Seven, from arrival to reply.

**EX022.** About 21 of every 100.

**EX023.** The decision step.

**EX024.** A clear message from managers that unsure reports are welcome.

**EX025.** Data collected automatically from systems.

**EX026.** Collect only data linked to a decision.

**EX027.** Monitoring when each person worked, for productivity purposes.

**EX028.** Security investigations and aggregated counts, accessed only by IT.

**EX029.** The supervisor forgetting to pass on a suspicious call.

**EX030.** A failure where the plan itself is wrong, such as trusting a fake email.

**EX031.** By removing memory demands, such as direct reporting.

**EX032.** Verification procedures that do not depend on judging appearance.

**EX033.** 70%, since 210 of 300 staff responded.

**EX034.** Not knowing how to report from a terminal or phone, chosen by 88 of 210 (42%).

**EX035.** Because warehouse terminals have no email client.

**EX036.** Report something odd.

**EX037.** A short description and the terminal number, without a name.

**EX038.** By forwarding them to a short company number.

**EX039.** A second person calls the customer on the number already on file.

**EX040.** So nobody removes the control later without understanding its purpose.

**EX041.** So she can say clearly whether each control passed or failed.

**EX042.** Forwarding a text needed five taps in his messaging app.

**EX043.** Five of seven passed first time; two passed after fixes.

**EX044.** The baseline for re-verification after future updates.

**EX045.** So that tests cannot affect live systems or real staff.

**EX046.** They never arrived because the supervisor role-player forgot to pass them on.

**EX047.** About 260 seconds with the old method and 22 seconds with new routes.

**EX048.** A simpler way to forward suspicious texts.

**EX049.** Because the form showed no confirmation or error.

**EX050.** As a sign that South had fewer suspicious messages.

**EX051.** A confirmation number on success or an error on failure.

**EX052.** Reports with malicious messages delivered, for each depot.

**EX053.** 12 of 80, or 15%.

**EX054.** Because mislabelling could cause lost customers or fraud.

**EX055.** What is certain and repetitive.

**EX056.** The IT lead hand-checks ten automated verdicts each month.

**EX057.** Customer service forwards them to triage and a notice is posted on the website.

**EX058.** The IT lead, who does most triage.

**EX059.** By training a second team member with a runbook and setting up a rota.

**EX060.** The renewal date of the driver number's mobile contract.

**EX061.** By watching a colleague follow them without help.

**EX062.** Lures about pay, health or job security.

**EX063.** In disciplinary or performance processes.

**EX064.** Because people trust it and follow wrong steps.

**EX065.** Half received quick verdicts and half received no feedback.

**EX066.** 26 of 30 messages reported with feedback versus 17 of 30 without.

**EX067.** A short explanation of what made the message suspicious.

**EX068.** A reply to every report within one working day.

**EX069.** A Report button in the route app.

**EX070.** Reports rose from 6 to 19 and median time to report fell from 95 to 12 minutes.

**EX071.** An attack campaign in week four.

**EX072.** To extend the button to warehouse handheld scanners.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Adams, A., & Sasse, M. A. (1999). Users are not the enemy. *Communications of the ACM*, 42(12), 40–46. <https://doi.org/10.1145/322796.322806>
- European Union Agency for Cybersecurity. (2019). *Cybersecurity culture guidelines: Behavioural aspects of cybersecurity*. ENISA. <https://www.enisa.europa.eu/publications/cybersecurity-culture-guidelines-behavioural-aspects-of-cybersecurity>
- Hansche, S., Ellis, B., Sanchez-Cherry, K., Snyder, J. N., & Walden, D. (2024). *Building a cybersecurity and privacy learning program* (NIST SP 800-50 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-50r1>
- Reason, J. (1990). *Human error*. Cambridge University Press. <https://doi.org/10.1017/CBO9781139062367>
- Whitten, A., & Tygar, J. D. (1999). Why Johnny can't encrypt: A usability evaluation of PGP 5.0. *Proceedings of the 8th USENIX Security Symposium*. USENIX. <https://www.usenix.org/conference/8th-usenix-security-symposium/why-johnny-cant-encrypt-usability-evaluation-pgp-50>
