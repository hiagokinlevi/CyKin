# Privacy and Data Protection: Technologist Course

- Language: English (`en`); course 073, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; five offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students learning to check how real systems handle personal data.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs inspect synthetic app SDK flows, test the completeness of an access request export, scan synthetic files for personal data patterns, check CCTV retention and automate inactive account deletion, all on synthetic data. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one technologist student through computing foundations, then privacy orientation, assets, flows, risk, methods, tooling, controls, monitoring, troubleshooting, integration, automation, evaluation, research, team work, handoff, deployment, field practice and a capstone. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Aisha Bello** | Technologist student | Invented |
| **Mr. Tom Reilly** | Supervisor | Invented |
| **Lindon Technical Institute** | Fictional institute | Invented |
| **Quayside Fitness** | Fictional gym chain, 40 clubs, about 60,000 members, app and wearables | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR) Articles 5, 9, 15, 28, 30, 32, 33 and 35; Lei 13.709/2018 (LGPD); EDPB Guidelines 3/2019 (video devices), 05/2020 (consent) and 01/2022 (access); WP248 rev.01; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 27701:2025; Nissenbaum (2004). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes

You will (1) describe the systems that handle member data in a fitness business; (2) distinguish servers, cloud services, apps and devices; (3) start a system inventory.

### 1.1 The course and the case

Aisha Bello begins a three-year technologist course at the fictional Lindon Technical Institute, supervised by Mr. Tom Reilly. Her work placement is with the fictional Quayside Fitness, a chain of forty gyms with about 60,000 members, a mobile app and wearable heart-rate straps used in classes. Quayside holds names, contact details, payment data, workout histories, heart-rate readings and CCTV footage. Mr. Reilly explains that privacy and data protection will be her specialism, and that each technical course will be applied to Quayside's systems.

### 1.2 Kinds of systems

Aisha lists Quayside's systems. A membership system in the cloud stores contracts and payments. The app stores profiles and workout history. Club computers run door access and class booking. Wearable straps send heart-rate data to class screens and to the app. CCTV recorders sit in each club. She notes that some systems are run by Quayside and some by vendors, and that member data move between them. Understanding the kinds of systems helps her see where data are stored and who controls them.

### 1.3 Starting an inventory

Mr. Reilly asks Aisha to start an inventory. For each system she records its purpose, the data it holds, where it runs, who owns it and which vendor supports it. The inventory reveals that nobody owns the CCTV recorders centrally; each club manager manages their own. She notes this as a governance gap. She learns that Article 30 of the GDPR requires a record of processing activities, and that her technical inventory will feed that record. The record must list purposes, categories of data and recipients, so her columns use the same headings.

### 1.4 Why systems matter for privacy

Aisha reflects that privacy depends on systems behaving correctly. A policy may say heart-rate data are deleted after a year, but if the app keeps them forever, the policy is false. She concludes that technologists have a key role: they know how systems actually behave and can check that practice matches policy. Mr. Reilly agrees and adds that technologists often discover privacy problems first, because they see the data every day. Her first example is the app's export button, which the written policy never mentions but which lets any manager download every member in seconds.

### Worked example

Aisha lists Quayside's membership, app, club, wearable and CCTV systems, starts an inventory that reveals no central CCTV owner and links it to Article 30.

> **Synthetic case.** Lindon, Quayside and all people are synthetic; GDPR Article 30 is real.

### Errors and limits

A first inventory is incomplete; plan to revisit it.

### Exercises

- **EX001 — Systems list.** Name four systems holding Quayside member data. *Rubric:* 3 = membership, app, club door/booking, wearables, CCTV;; 2 = three;; 1 = one;; 0 = none.
- **EX002 — CCTV gap.** What governance gap did the inventory show? *Rubric:* 3 = no central owner for CCTV recorders;; 2 = mentions CCTV;; 1 = none;; 0 = none.
- **EX003 — Practice versus policy.** Why do technologists matter for privacy? *Rubric:* 3 = they see how systems behave and can check practice against policy;; 2 = mentions systems;; 1 = none;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) trace member data across networks; (2) identify third-party services in apps and websites; (3) protect data in transit.

### 2.1 Club networks

Each club has a network for staff computers, door access, CCTV and guest Wi-Fi. Aisha finds that CCTV recorders and guest Wi-Fi share one network in two clubs, so a guest could reach the recorders. She recommends separating them. She explains that network separation protects personal data such as footage from people who should not access it, and that it also reduces the chance that a compromised device spreads to other systems. At Quayside the fix is a separate virtual network for cameras, with a rule that only the recorder management server may connect to them.

### 2.2 Internet services

Quayside's website and app use many internet services: hosting, payments, analytics, maps and social login. Aisha uses browser developer tools on the website with a test account to see which domains receive requests. She lists eleven third-party domains. Some receive only technical data; others receive member identifiers. She learns that each third party may be a processor needing a contract under GDPR Article 28, or a separate controller, and that many services are added without privacy review. Her list shows a map service receiving club searches with member IDs attached.

### 2.3 Encryption in transit

Aisha checks that the website and app use encrypted connections. All public endpoints do, but the club booking screens send member names to a local server without encryption. She raises it with the IT team, who enable encryption. She explains that encryption in transit is a basic security measure under Article 32 and that internal networks are not automatically safe. On the booking screens, anyone plugged into the club switch could have read names and class times in plain text. After the change she repeats the capture with a test booking and sees only encrypted traffic, which she records as evidence for the IT ticket.

### 2.4 Guest Wi-Fi

Guest Wi-Fi asks members to log in with their membership number. Aisha finds that login records with device identifiers are kept indefinitely. She recommends keeping them only as long as needed for security and abuse handling, such as thirty days, and telling members in the privacy notice. She notes that networks create personal data as a side effect, which needs the same care as data collected deliberately. Device identifiers can follow a member across visits, so thirty days limits how much movement history builds up.

### Worked example

Aisha separates CCTV from guest Wi-Fi, lists eleven third-party domains on the website, gets booking screens encrypted and limits guest Wi-Fi logs to thirty days.

> **Synthetic case.** Networks are synthetic; GDPR Articles 28 and 32 are real.

### Errors and limits

Browser tools show web requests only; apps need separate testing.

### Exercises

- **EX004 — Shared network risk.** Why separate CCTV from guest Wi-Fi? *Rubric:* 3 = guests could reach recorders holding footage;; 2 = mentions access;; 1 = fine;; 0 = none.
- **EX005 — Third parties.** How did Aisha find third-party services? *Rubric:* 3 = browser developer tools with a test account;; 2 = mentions tools;; 1 = guessed;; 0 = none.
- **EX006 — Wi-Fi logs.** What retention did Aisha recommend for Wi-Fi login records? *Rubric:* 3 = about thirty days with transparency;; 2 = mentions limit;; 1 = indefinite;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write scripts that handle member data safely; (2) avoid printing or logging personal data; (3) use test data.

### 3.1 Safe scripts

Aisha writes Python scripts to count class attendance. Mr. Reilly requires synthetic member data for all exercises. Her script reads a file of bookings, counts attendance per class and prints totals. She avoids printing member names, which are not needed for totals. She learns that scripts are often copied and reused, so habits formed in simple scripts spread into production systems. Her script therefore groups bookings by class code and date, and the only output is a table such as Spin Tuesday 18:00 with twenty-two attendees.

### 3.2 Logging

Aisha adds logging to her script to help debugging. Her first version logs each booking with the member name. She changes it to log only booking references and counts. She explains that logs are often kept longer and accessed by more people than the data they describe, so personal data in logs create unnecessary exposure. In her script, a log line now reads booking B-10422 counted for class SPN-18, which still lets her trace an error back to the source file without revealing who attended the class.

### 3.3 Input validation

Aisha's script reads files exported from the booking system. She adds checks that the file has only expected columns and stops if it includes unexpected ones such as health notes. She explains that validation supports data minimisation, since a script should not process data it does not need, and that stopping loudly is better than silently processing sensitive information. Her check compares the header row with an allowed list of five columns and exits with a message naming any extra column, such as medical_notes.

### 3.4 Test data generation

Aisha writes a generator for synthetic members with names, ages, membership types and bookings. She includes edge cases, such as members with long names or no bookings. She shares the generator with classmates. Mr. Reilly notes that good test data make development safer and faster, and that using real member data for testing is a common cause of breaches. Her generator uses a fixed random seed, so classmates who run it get identical members and can compare their results line by line.

### Worked example

Aisha writes an attendance script that prints totals without names, logs references only, rejects unexpected columns and generates synthetic members with edge cases.

> **Synthetic case.** Scripts and members are synthetic.

### Errors and limits

Synthetic data may miss real-world quirks; add them deliberately.

### Exercises

- **EX007 — No names in totals.** Why does Aisha's script not print names? *Rubric:* 3 = totals do not need them;; 2 = mentions minimisation;; 1 = prints;; 0 = none.
- **EX008 — Log content.** What does Aisha log instead of names? *Rubric:* 3 = booking references and counts;; 2 = mentions references;; 1 = names;; 0 = none.
- **EX009 — Real test data.** Why avoid real member data in testing? *Rubric:* 3 = it is a common cause of breaches;; 2 = mentions risk;; 1 = fine;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) design data models that separate sensitive data; (2) define retention in the model; (3) model consent.

### 4.1 Separating sensitive data

Aisha designs a data model for Quayside's app. Member identity (name, email, phone) sits in one table; workout and heart-rate data sit in another linked by an internal identifier; marketing preferences sit in a third. She explains that separation lets each service access only what it needs. Heart-rate data may be data concerning health under GDPR Article 4(15) when used to assess fitness or health, which requires extra care under Article 9. In practice, the class screen service can read heart-rate zones and first names but cannot query emails or payment status.

### 4.2 Retention fields

Aisha adds a created date and a category to each record, so that retention rules can be applied. Heart-rate readings are kept for twelve months unless the member chooses to keep longer; workout summaries are kept while the account is active. She notes that designing retention into the model from the start is much easier than adding it later, when data have accumulated without dates or categories. Her retention job reads the category, compares the created date with the rule and deletes the expired rows.

### 4.3 Modelling consent

Quayside uses consent for marketing emails and for sharing heart-rate data with class screens. Aisha models consent as a table with member, purpose, wording version, date and status. Withdrawals change the status and the date. She explains that EDPB Guidelines 05/2020 require consent to be specific and demonstrable, which the model supports by recording what was agreed and when. A wording version matters because Quayside will change its consent text; without it, nobody can prove which text a member saw in 2025 compared with 2027.

### 4.4 Reviewing the model

Mr. Reilly reviews Aisha's model and asks why date of birth is stored when age bands would do. Aisha replaces it with an age band for classes and keeps the full date only in the membership system, where it is needed for contracts. He notes that each field in a data model should have a reason, and that reviewing models for unnecessary fields is an effective privacy practice. After the review she also removes gender from the app, since no feature uses it.

### Worked example

Aisha separates identity, workout and marketing data, adds retention fields, models consent with wording versions and replaces date of birth with age bands in the app.

> **Synthetic case.** The model is synthetic; GDPR Articles 4(15) and 9 and EDPB Guidelines 05/2020 are real.

### Errors and limits

Age bands can still identify people in small classes; combine with other protections.

### Exercises

- **EX010 — Heart-rate status.** When may heart-rate data be health data? *Rubric:* 3 = when used to assess fitness or health, per Article 4(15);; 2 = mentions health;; 1 = never;; 0 = none.
- **EX011 — Consent fields.** What fields does the consent table hold? *Rubric:* 3 = member, purpose, wording version, date and status;; 2 = most;; 1 = few;; 0 = none.
- **EX012 — Date of birth.** Why replace date of birth with an age band in the app? *Rubric:* 3 = the app does not need the full date;; 2 = mentions need;; 1 = keep;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) recognise threats to member data; (2) explain basic protections to club staff; (3) recognise personal data breaches.

### 5.1 Threats

Aisha lists threats to Quayside: phishing emails to club managers, weak passwords on booking screens, lost tablets used at reception, and staff sharing member lists on personal phones. She notes that most incidents in similar businesses involve ordinary mistakes rather than sophisticated attacks. She groups the threats by where they start. Phishing begins in email, weak passwords begin at the screen, lost tablets begin at the front desk and shared photos begin in staff habits. For each group she writes a realistic example from a club day, such as a manager clicking a fake invoice link during a busy Monday evening rush.

### 5.2 Staff guidance

Aisha writes a one-page guide for club staff: use the password manager, lock reception screens, never photograph member lists, report lost devices immediately and check email recipients. She tests it with two club managers and simplifies the wording. The first draft used security vocabulary that confused the managers, who asked what a password manager actually was and why locking a screen mattered when they were standing beside it. Aisha rewrote each rule as a short action with a reason, for example: lock the screen whenever you walk away, because members queue right next to it.

### 5.3 Recognising breaches

Aisha explains that a personal data breach includes accidental loss or disclosure, not only hacking. A lost tablet with member bookings or an email to the wrong member can be a breach. Quayside must assess each and notify the supervisory authority within 72 hours under Article 33 unless the breach is unlikely to result in a risk. She prepares three short examples for training: a reception tablet left on a bus, a class list emailed to the wrong trainer, and a door access log exposed by a misconfigured link. Staff discuss whether each involves personal data and who might be harmed, which shows them that breaches are everyday events, not only cyber attacks.

### 5.4 Reporting

Aisha sets up a simple reporting form for staff. She explains that quick reporting matters because the 72-hour clock starts when Quayside becomes aware. Mr. Reilly adds that staff who fear blame delay reports, so the guide thanks staff for reporting promptly. The form asks only for what happened, when it was noticed, which club and what data might be involved. It does not ask staff to judge severity, because that decision belongs to the data protection officer. In the first month the form receives six reports, four of which are misdirected emails that would previously have gone unrecorded.

### Worked example

Aisha lists everyday threats, writes a one-page staff guide, explains that accidental losses are breaches and sets up a quick reporting form.

> **Synthetic case.** Threats and guidance are synthetic; GDPR Article 33 is real.

### Errors and limits

Guides need refreshing as threats change.

### Exercises

- **EX013 — Lost tablet.** Is a lost reception tablet with bookings a possible breach? *Rubric:* 3 = yes; accidental loss of personal data;; 2 = yes;; 1 = no;; 0 = none.
- **EX014 — Report timing.** Why must staff report quickly? *Rubric:* 3 = the 72-hour clock starts when Quayside becomes aware;; 2 = mentions deadline;; 1 = none;; 0 = none.
- **EX015 — Photographing lists.** Which risky habit does the guide forbid? *Rubric:* 3 = photographing member lists on personal phones;; 2 = mentions phones;; 1 = none;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) secure club computers; (2) understand virtual machines and isolation; (3) manage local data.

### 6.1 Club computers

Club reception computers run booking and door software. Aisha finds shared administrator accounts and saved member exports in download folders. She recommends individual accounts, removal of admin rights for reception staff, and automatic clean-up of downloads. She explains that operating system settings protect personal data even when applications are secure. She also finds that the booking software stores a full member export each night in a temporary folder that nobody empties. The software vendor confirms that the folder can be set to clear automatically. Aisha asks the vendor to make clearing the default for every club, rather than relying on each manager to remember the setting.

### 6.2 Virtual machines

Quayside's head office runs several services on virtual machines in the cloud. Aisha learns that virtual machines isolate workloads but share hosts. She checks that the membership database runs on its own virtual machine with restricted network access. Isolation reduces the spread of compromise and keeps member data separate from less critical services. She reviews the cloud firewall rules and finds one rule that allows any address on the head office network to reach the database port. She narrows it to the two application servers that need it. She explains that isolation only works if network rules match the design, and that rules tend to widen over time when people fix urgent problems.

### 6.3 Local data

Aisha searches club computers for local copies of member data and finds old spreadsheets in three clubs. She works with managers to delete them and to use the central system instead. She notes that local copies escape retention rules and access controls. To understand why the copies existed, she asks the managers. They explain that the central system was slow on Monday evenings, so they kept lists for quick lookups. Aisha reports the performance problem to IT, because deleting copies without fixing the reason would only cause new copies to appear within weeks.

### 6.4 Updates

Aisha checks update status and finds two club computers months behind. She sets up automatic updates. Mr. Reilly notes that unpatched machines are a frequent route for attacks and that patching is a basic measure under Article 32. She lists the software on each club computer and finds an old document viewer with known vulnerabilities. It is removed because nobody uses it. She records the update status in the inventory so that future checks can compare against it, and she asks IT to report monthly on any club computer more than thirty days behind.

### Worked example

Aisha removes shared admin accounts, isolates the membership database VM, deletes old local spreadsheets and enables automatic updates.

> **Synthetic case.** Computers are synthetic; GDPR Article 32 is real.

### Errors and limits

Automatic updates can break club software; test first.

### Exercises

- **EX016 — Downloads clean-up.** Why clean download folders on reception computers? *Rubric:* 3 = saved exports contain member data;; 2 = mentions exports;; 1 = none;; 0 = none.
- **EX017 — VM isolation.** Why give the membership database its own VM? *Rubric:* 3 = isolation limits spread of compromise;; 2 = mentions isolation;; 1 = none;; 0 = none.
- **EX018 — Local copies risk.** Why are local spreadsheets risky? *Rubric:* 3 = they escape retention and access controls;; 2 = mentions control;; 1 = none;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) design roles for club and head office staff; (2) manage leavers; (3) apply multi-factor authentication.

### 7.1 Roles

Aisha designs roles: reception, personal trainer, club manager, head office support, marketing and IT. Trainers see bookings and workout data for their clients; reception sees bookings and membership status; marketing sees preferences but not workout data. She documents why each role needs its access. She meets each group to check the draft. Trainers point out that they sometimes cover classes for colleagues and need temporary access to those clients. Aisha adds a time-limited cover permission that expires after the class instead of giving trainers access to all members, which keeps access narrow while still letting the clubs run smoothly every day.

### 7.2 Leavers

Gyms have high staff turnover. Aisha finds forty active accounts belonging to former staff. She links account removal to the HR leaver process and runs a monthly check. She notes that stale accounts are a common route for misuse. She traces how the forty accounts arose. Club managers create staff accounts directly, but nobody told IT when staff left, and HR used a separate system. Linking the two means a leaver date in HR now disables the account automatically. The monthly check compares active accounts with the HR list and reports any difference to the club manager.

### 7.3 Multi-factor authentication

Aisha recommends multi-factor authentication for head office and manager accounts, which can export member lists. Reception accounts on shared screens use short sessions and badge login. Managers worry that extra login steps will slow busy shifts. Aisha runs a two-week trial in one club using an authenticator app and finds that managers log in only a few times per day, so the delay is small. Export rights are the main reason for the control, because an export can copy thousands of members in seconds.

### 7.4 Reviews

Aisha sets up quarterly access reviews for club managers. The first review corrects twenty-three accounts. She records results as evidence of accountability under Article 5(2). Each manager receives a list of the accounts in their club with roles and last login dates and must confirm or correct each one. The corrections include trainers with reception rights, a cleaner with a booking account and two managers who had transferred to other clubs. Aisha keeps the signed lists with dates as evidence of the review being done.

### Worked example

Aisha defines six roles, removes forty former-staff accounts through HR linkage, adds multi-factor authentication for exporters and runs quarterly reviews.

> **Synthetic case.** Accounts are synthetic; GDPR Article 5(2) is real.

### Errors and limits

Reviews by busy managers can be rubber stamps; sample their answers.

### Exercises

- **EX019 — Trainer access.** What can personal trainers see? *Rubric:* 3 = bookings and workout data for their clients;; 2 = mentions clients;; 1 = all members;; 0 = none.
- **EX020 — Former staff.** How many former-staff accounts were active? *Rubric:* 3 = forty;; 2 = about;; 1 = none;; 0 = none.
- **EX021 — MFA scope.** Which accounts get multi-factor authentication? *Rubric:* 3 = head office and managers who can export lists;; 2 = mentions managers;; 1 = all;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) apply segmentation and least privilege; (2) place controls around sensitive data; (3) document an architecture.

### 8.1 Segments

Aisha draws Quayside's architecture with segments: public app and website, head office services, club networks and CCTV. She places the membership database and heart-rate store in a restricted segment. She explains the reasoning for each boundary to the IT team. Public services face the internet and are attacked most often, so they should not reach member stores directly. Club networks are physically exposed in public buildings. CCTV produces large volumes of footage of identifiable people, and each segment has rules describing exactly which traffic may cross into another.

### 8.2 Controls around data

Access to the heart-rate store passes through an API that checks role and purpose. Exports require approval. Encryption protects data at rest. She explains that layered controls reduce reliance on any single measure. The API records every request with the role and stated purpose, so unusual patterns can be found later, such as a trainer reading hundreds of profiles in an evening. Export approvals go to the data protection officer for large lists. Encryption keys are managed by the cloud key service and access to keys is limited to two administrators.

### 8.3 Vendors in the diagram

Aisha includes vendors: payment processor, chat support, analytics and wearable strap provider. She marks which receive personal data and whether contracts exist. The mapping shows that the wearable strap provider receives raw heart-rate readings, not just zones, and that its contract does not mention retention. Aisha flags the gap for the procurement team. She also discovers that chat support transcripts are stored by the vendor for five years by default, which is far longer than Quayside needs for customer service. Aisha asks for ninety days.

### 8.4 Documentation

Aisha writes a short architecture document with the diagram, data flows and controls. Mr. Reilly notes that documentation helps new staff and auditors understand how member data are protected. She writes the document in plain language with a glossary for terms such as segment, API and encryption at rest. She includes a section listing known weaknesses and planned fixes, so readers do not assume the design is perfect. The document has a version number and an owner in IT who will update it after each major change.

### Worked example

Aisha segments Quayside's architecture, restricts the heart-rate store behind a role-checking API, maps vendors and documents the design.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Diagrams drift from reality; review after changes.

### Exercises

- **EX022 — Restricted segment.** Which stores sit in the restricted segment? *Rubric:* 3 = membership database and heart-rate store;; 2 = one;; 1 = none;; 0 = none.
- **EX023 — Layered controls.** Why use several layers of controls? *Rubric:* 3 = reduces reliance on any single measure;; 2 = mentions layers;; 1 = one enough;; 0 = none.
- **EX024 — Vendor mapping.** What does Aisha mark for each vendor? *Rubric:* 3 = whether it receives personal data and has a contract;; 2 = one;; 1 = none;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) choose privacy metrics; (2) collect evidence reliably; (3) report results.

### 9.1 Metrics

Aisha proposes metrics: accounts of former staff, local copies found, rights requests answered on time and CCTV footage past retention. Each has a definition and data source. She avoids metrics that are easy to count but say little, such as the number of policies published. For each metric she writes how it is calculated, who supplies the data, how often it is measured and what value would be a concern. For example, any former-staff account active for more than two days is a concern.

### 9.2 Evidence

She collects evidence through system reports rather than surveys where possible, because reports are more reliable. She stores evidence with dates. Surveys ask managers whether they removed leavers, but managers may remember incorrectly or answer optimistically. A system report lists the accounts directly. Where only a survey is possible, such as staff awareness, she combines it with a small test, like asking staff to show where the reporting form is, and she records how each piece of evidence was produced. Method notes prevent overclaiming.

### 9.3 Baseline

Aisha records a baseline: forty stale accounts, three clubs with local spreadsheets and an unknown CCTV retention position. She notes unknowns as gaps to measure. She writes down the date and method for each baseline value, because a later change in method could look like an improvement. For CCTV she plans a check at one club first. She also records two values she expects to rise at first, breach reports and access requests, explaining that better awareness can make numbers increase before risks fall.

### 9.4 Reporting

She reports monthly to Quayside's data protection officer. Mr. Reilly notes that measuring from the start allows progress to be shown later. Each monthly report fits on one page: a table of metrics with the current value, the previous value and the baseline, a short comment on each change and a list of actions with owners. The data protection officer forwards it to the operations director. Aisha keeps the reports in a dated folder so trends can be reviewed later. Each report names its data sources.

### Worked example

Aisha defines four metrics, prefers system evidence, records a baseline including unknowns and reports monthly.

> **Synthetic case.** Metrics are synthetic.

### Errors and limits

Metrics can miss what is not measured.

### Exercises

- **EX025 — Evidence source.** Why prefer system reports over surveys? *Rubric:* 3 = more reliable;; 2 = mentions reliability;; 1 = surveys;; 0 = none.
- **EX026 — Unknown CCTV.** How does Aisha treat the unknown CCTV position? *Rubric:* 3 = as a gap to measure;; 2 = mentions gap;; 1 = ignore;; 0 = none.
- **EX027 — Baseline value.** Why record a baseline? *Rubric:* 3 = to show progress later;; 2 = mentions comparison;; 1 = none;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Privacy and data protection: orientation

### Learning outcomes

You will (1) explain core data protection principles; (2) identify lawful bases in a fitness business; (3) recognise special category data.

### 10.1 Principles

Aisha studies GDPR Article 5 principles and LGPD Article 6 principles and applies each to Quayside. Purpose limitation means CCTV footage for security is not used to monitor staff productivity. Minimisation means the app asks only for data needed for workouts. Accuracy means members can correct their details in the app. Storage limitation means footage and inactive accounts are deleted on schedule. Integrity and confidentiality mean member data are protected against loss and misuse. Accountability under Article 5(2) means Quayside must be able to show compliance, not just claim it, which is why Aisha keeps evidence of every check she performs.

### 10.2 Lawful bases

Membership processing relies on contract; payment records on legal obligation; marketing emails on consent; CCTV on legitimate interests. Aisha learns that each purpose needs its own basis. She notes that consent is not appropriate for membership processing, because members cannot refuse the processing and still have a membership; contract fits better. For CCTV, legitimate interests require a balancing test showing that security needs outweigh the intrusion on members and staff. She drafts the balancing test with the data protection officer and records the reasoning.

### 10.3 Special categories

Heart-rate data used to assess health may be health data, needing an Article 9 condition such as explicit consent. Aisha notes that Quayside must decide and document this carefully. She discusses the difference between heart-rate readings shown during a class and a long history used to suggest rest days or detect irregular rhythms. The second clearly reveals information about health. Quayside decides to treat all stored heart-rate data as health data, which is the more protective choice and simplifies explanations to members and staff alike.

### 10.4 Rights

Members have rights to access, rectify, erase, restrict, port and object. Aisha lists how each would be handled in Quayside's systems. Mr. Reilly notes that rights must be practical, not only stated. For access, a checklist covers every system. For rectification, members edit details in the app. For erasure, an account deletion process reaches all systems with documented exceptions such as debt. For objection, members can stop marketing in one tap. She notes that LGPD Article 18 gives similar rights to members in Brazil if Quayside ever operates there.

### Worked example

Aisha maps principles to Quayside, assigns lawful bases by purpose, flags heart-rate data as possible health data and lists rights handling.

> **Synthetic case.** Quayside's choices are synthetic; GDPR Articles 5 and 9 and LGPD Article 6 are real.

### Errors and limits

Lawful basis choices depend on facts; review with counsel.

### Exercises

- **EX028 — CCTV purpose.** Why can CCTV footage not be used for staff productivity? *Rubric:* 3 = purpose limitation;; 2 = mentions purpose;; 1 = allowed;; 0 = none.
- **EX029 — Marketing basis.** What lawful basis does marketing email use? *Rubric:* 3 = consent;; 2 = correct;; 1 = contract;; 0 = none.
- **EX030 — Heart-rate condition.** What condition may heart-rate health data need? *Rubric:* 3 = explicit consent under Article 9;; 2 = mentions consent;; 1 = none;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Privacy and data protection: assets and context

### Learning outcomes

You will (1) classify personal data assets; (2) understand member expectations; (3) relate context to appropriate use.

### 11.1 Asset classes

Aisha classifies assets: identity, payment, workout, heart-rate, CCTV and marketing. She rates sensitivity and volume for each. Identity data include names, emails, phones and photos on membership cards. Payment data include bank details and card tokens. Workout data include classes and exercises. Heart-rate data come from straps. CCTV covers entrances and gym floors. Marketing data include preferences and campaign responses. She rates heart-rate and CCTV as most sensitive, and identity and workout data as the largest by volume. Payment data rank third because card tokens are held by the processor.

### 11.2 Expectations

She surveys twenty volunteers about expectations. Most expect workout data to stay within the app and be deleted when they leave. The volunteers are members who responded to a notice in two clubs. She asks short questions about where data go, who can see them and how long they are kept. Several volunteers are surprised that class screens show heart-rate zones with first names, and two say they stopped wearing straps for that reason. She records their views anonymously. She feeds these views into the risk work.

### 11.3 Context

Using contextual integrity, Aisha notes that heart-rate data shared for training should not flow to advertisers. Members' expectations match this. Contextual integrity asks whether an information flow matches the norms of the context where data were shared. Members share heart-rate data with trainers to train better. A flow to advertisers serves a different purpose and breaks those norms, even if a notice mentions it. Aisha uses this framework to explain to the app team why some legal flows still feel wrong to members.

### 11.4 Priorities

She ranks assets by sensitivity and exposure; heart-rate and CCTV come first. Mr. Reilly notes that context helps decide where protection matters most. She combines sensitivity with how widely data are exposed. Heart-rate data are sensitive and reach vendors and screens. CCTV footage is sensitive and accessed by local managers without logging. Payment data are sensitive but already protected by the payment processor. This ranking guides which data flows she examines first in the next chapter and which controls she proposes later.

### Worked example

Aisha classifies six asset types, surveys expectations, applies contextual integrity to heart-rate data and ranks heart-rate and CCTV highest.

> **Synthetic case.** The survey is synthetic; Nissenbaum (2004) is real.

### Errors and limits

Twenty volunteers are not representative.

### Exercises

- **EX031 — Asset classes.** Name four asset classes. *Rubric:* 3 = identity, payment, workout, heart-rate, CCTV, marketing;; 2 = three;; 1 = none;; 0 = none.
- **EX032 — Member expectation.** What did most volunteers expect about workout data? *Rubric:* 3 = stays in the app and is deleted on leaving;; 2 = one part;; 1 = none;; 0 = none.
- **EX033 — Top priorities.** Which assets rank highest? *Rubric:* 3 = heart-rate and CCTV;; 2 = one;; 1 = wrong;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Privacy and data protection: data flows

### Learning outcomes

You will (1) inspect SDKs embedded in an app; (2) check notice and contract coverage; (3) recommend changes.

### 12.1 SDKs

Quayside's app embeds five software development kits. Aisha lists what each receives using a test build and network inspection with synthetic accounts. SDKs are third-party code that can collect data without the app team noticing. An SDK is a library supplied by another company that the app includes to provide a feature such as crash reports or chat. Aisha builds a test version of the app, signs in with synthetic members and records network traffic while using workouts, classes and chat. She then lists each SDK, the fields it receives and whether the notice and contracts cover it.

### 12.2 Results

The lab shows that the crash reporter, analytics and chat support SDKs are covered by the privacy notice and contracts. The ad network receives an advertising identifier, heart-rate zone and location, and is neither in the notice nor under contract. Social login lacks a contract. Heart-rate data flowing to advertisers is the most serious finding. The heart-rate zone is derived from health data, and sending it with an advertising identifier and location lets an ad network build a profile of a member's fitness and movements. The developers say the SDK came bundled with a promotions feature two years ago and nobody reviewed its data collection. The other gaps are smaller but still need contracts and notices to be fixed.

### 12.3 Recommendations

Aisha recommends removing the ad network SDK, signing a contract with the social login provider and updating the notice. She also recommends a rule that no SDK is added without privacy review. She writes the recommendations with owners and dates. The app team owns removing the SDK, procurement owns the social login contract and the data protection officer owns the notice update. She also asks the app team to keep a list of every SDK with its version and purpose in the repository, so future reviews start from an accurate record rather than memory.

### 12.4 Follow-up

The app team removes the ad SDK in the next release. Aisha tests again and confirms that no heart-rate data leave to advertisers. Mr. Reilly notes that SDK reviews should be repeated for every release. The retest uses the same synthetic accounts and steps, so results can be compared directly. Traffic to the ad network has disappeared, and the social login contract is signed within a month. Aisha adds an SDK review step to the release checklist, with a simple question for developers: does this release add or update any third-party library that sends data off the device?

### Lab — SDK data flows and coverage

```python
# Fitness app: what does each embedded SDK receive, and is it covered by the privacy notice and a contract?
sdks = [("crash reporter", ["device model", "app version"], True, True),
        ("analytics", ["member id", "screen views", "workout type"], True, True),
        ("ad network", ["advertising id", "heart rate zone", "location"], False, False),
        ("chat support", ["member id", "name", "messages"], True, True),
        ("social login", ["email", "name"], True, False)]
for name, data, notice, contract in sdks:
    issues = ([] if notice else ["not in notice"]) + ([] if contract else ["no contract"])
    health = any(d in ("heart rate zone",) for d in data)
    print(f"{name:15s} {', '.join(data):40s} {'OK' if not issues else '; '.join(issues)}{' [HEALTH DATA]' if health else ''}")
```

Run with `python3 lab_flows.py`. Verified output:

```text
crash reporter  device model, app version                OK
analytics       member id, screen views, workout type    OK
ad network      advertising id, heart rate zone, location not in notice; no contract [HEALTH DATA]
chat support    member id, name, messages                OK
social login    email, name                              no contract
```

### Worked example

Aisha finds the ad network receiving heart-rate zone and location without notice or contract and social login without a contract, and the ad SDK is removed.

> **Synthetic case.** SDKs are synthetic.

### Errors and limits

Network inspection may miss data sent later or in batches.

### Exercises

- **EX034 — Worst SDK.** Which SDK is the most serious finding? *Rubric:* 3 = ad network, receiving heart-rate zone and location without notice or contract;; 2 = names it;; 1 = other;; 0 = none.
- **EX035 — Social login gap.** What gap does social login have? *Rubric:* 3 = no contract;; 2 = correct;; 1 = none;; 0 = none.
- **EX036 — SDK rule.** What rule did Aisha recommend? *Rubric:* 3 = no SDK added without privacy review;; 2 = mentions review;; 1 = none;; 0 = none.

<a id="ch-13"></a>

## Chapter 13 — Privacy and data protection: risk scenarios

### Learning outcomes

You will (1) write risk scenarios for member data; (2) rate likelihood and impact; (3) choose treatments.

### 13.1 Scenarios

Aisha writes scenarios: heart-rate data leaked to advertisers; CCTV footage of changing-room corridors accessed by staff; member lists photographed and shared; app account taken over. Each scenario names who acts, what they do, which data are affected and what harm follows. For example, a reception employee curious about a neighbour views CCTV clips of her arrivals and shares them, causing embarrassment and distress. Writing scenarios this way helps managers recognise risks in their own clubs rather than treating privacy as an abstract legal matter.

### 13.2 Ratings

She rates each on likelihood and impact from one to three. Heart-rate leakage and account takeover rate highest. Likelihood considers how often similar events happen and how easy they are. Impact considers harm to members, such as distress, discrimination or financial loss, rather than only harm to Quayside. Heart-rate leakage scores high on impact because health data can affect insurance or employment. Account takeover scores high on likelihood because member passwords are often reused from other services. Both therefore rate three by three.

### 13.3 Treatments

Treatments include SDK review, CCTV access logging, staff guidance and multi-factor login for the app. She chooses treatments that reduce likelihood or impact. SDK review reduces the chance of new leaks. CCTV access logging deters misuse and makes it detectable. Staff guidance reduces photographed lists. Optional multi-factor login protects app accounts. She records the residual risk after each treatment, and accepts that some risk remains, such as members choosing weak passwords despite advice. Residual risk for heart-rate leakage falls from high to medium after SDK review.

### 13.4 Owners

Each treatment gets an owner and date. Mr. Reilly notes that scenarios help non-specialists understand risks. Owners are people with authority to act, not committees. The app lead owns SDK review and login changes; the operations director owns CCTV logging; the training manager owns staff guidance. Dates are realistic and agreed with owners. Aisha reviews the list each month and reports overdue items to the data protection officer, who can escalate them to the leadership team. Each item shows its target date beside it.

### Worked example

Aisha writes four scenarios, rates heart-rate leakage and account takeover highest and assigns treatments with owners.

> **Synthetic case.** Scenarios are synthetic.

### Errors and limits

Ratings are subjective; discuss them with colleagues.

### Exercises

- **EX037 — Highest scenarios.** Which scenarios rate highest? *Rubric:* 3 = heart-rate leakage and account takeover;; 2 = one;; 1 = none;; 0 = none.
- **EX038 — CCTV treatment.** What treatment addresses CCTV misuse? *Rubric:* 3 = access logging;; 2 = mentions logging;; 1 = none;; 0 = none.
- **EX039 — Scenario value.** Why use scenarios? *Rubric:* 3 = they help non-specialists understand risks;; 2 = mentions understanding;; 1 = none;; 0 = none.

<a id="ch-14"></a>

## Chapter 14 — Privacy and data protection: methods I

### Learning outcomes

You will (1) test the completeness of an access request response; (2) find systems missed; (3) improve the process.

### 14.1 The test

Aisha tests Quayside's access request process with a synthetic member. The first export searches membership, app profile and payments. She compares it with all systems holding data for that member. She creates a synthetic member who uses the app, books classes, chats with support, appears in a CCTV index entry and receives marketing. She then submits an access request through the normal channel and waits for the response that a real member would receive, so she can see the process as members experience it rather than as staff describe it.

### 14.2 Results

The lab shows that the export covered 47 of 287 records, 16%, in three of seven systems. Workout history, CCTV index, chat support and marketing were missed. Article 15 requires access to all personal data held. The response team searched the systems they knew best and missed the others because no list told them where member data lived. Workout history, the largest set of records, was missing because it sits in a separate app database. The missing CCTV index and chat transcripts were held by vendors and needed requests to those vendors, which nobody had asked them to provide.

### 14.3 Improvement

Aisha creates a checklist of systems from the inventory and assigns an owner for each search. EDPB Guidelines 01/2022 help define what must be included. The checklist lists each system, the search method, the owner, the expected time and any redaction needs. CCTV footage needs other people blurred, and chat transcripts may mention staff. The response team now records which systems were searched for each request. This record also shows the supervisory authority, if asked, how Quayside meets its obligation under Article 15. It is kept for two years.

### 14.4 Retest

After changes, a second test covers all seven systems. Mr. Reilly notes that end-to-end tests with synthetic members reveal gaps that procedure documents hide. The second synthetic member's response includes all seven systems and arrives within the one-month deadline. The team notes that the vendor searches take the longest, so they now start those on day one. Aisha recommends repeating the test twice a year and after any new system is added, because new systems are the most likely place for gaps to reappear.

### Lab — Completeness of an access request export

```python
# Access request completeness: which systems hold data for a synthetic member, and which did the first export search?
holding = {"membership": 14, "app profile": 9, "workout history": 220, "CCTV index": 3, "chat support": 6, "marketing": 11, "payments": 24}
searched = {"membership", "app profile", "payments"}
found = sum(v for k, v in holding.items() if k in searched); total = sum(holding.values())
for k, v in holding.items(): print(f"{k:16s} records {v:4d} {'searched' if k in searched else 'MISSED'}")
print(f"first export covered {found} of {total} records ({found/total:.0%}) in {len(searched)} of {len(holding)} systems")
```

Run with `python3 lab_sar.py`. Verified output:

```text
membership       records   14 searched
app profile      records    9 searched
workout history  records  220 MISSED
CCTV index       records    3 MISSED
chat support     records    6 MISSED
marketing        records   11 MISSED
payments         records   24 searched
first export covered 47 of 287 records (16%) in 3 of 7 systems
```

### Worked example

Aisha finds the first export covered 47 of 287 records (16%) in three of seven systems, adds an inventory-based checklist and confirms full coverage on retest.

> **Synthetic case.** The member is synthetic; GDPR Article 15 and EDPB Guidelines 01/2022 are real.

### Errors and limits

CCTV footage requires redaction of other people before disclosure.

### Exercises

- **EX040 — Coverage.** What share of records did the first export cover? *Rubric:* 3 = 47 of 287, 16%;; 2 = approximately;; 1 = wrong;; 0 = none.
- **EX041 — Missed systems.** Name two systems missed. *Rubric:* 3 = workout history, CCTV index, chat support, marketing;; 2 = one;; 1 = none;; 0 = none.
- **EX042 — Fix.** What fixed the gap? *Rubric:* 3 = inventory-based checklist with search owners;; 2 = mentions checklist;; 1 = none;; 0 = none.

<a id="ch-15"></a>

## Chapter 15 — Privacy and data protection: guided lab

### Learning outcomes

You will (1) run a guided privacy lab safely; (2) verify retention on CCTV; (3) record results.

### 15.1 Lab plan

Aisha plans a guided lab on CCTV retention at one club using a synthetic index of clips. Quayside's policy keeps footage for thirty days unless flagged for an incident. EDPB Guidelines 3/2019 on video devices discuss retention and transparency. The index lists each clip's camera, date and incident flag but no images, so the lab avoids viewing footage of real people. Aisha agrees the plan with the club manager and the data protection officer, sets a date for the check and writes down what result would show a problem: any unflagged clip older than thirty days.

### 15.2 Results

The lab checks 500 clips. 304 are older than thirty days; twelve are held for incidents; 292 should be deleted. The oldest unflagged clip is 75 days old. Automatic deletion is not working. The result surprises the club manager, who believed deletion was automatic. The incident-flagged clips are expected, since footage linked to incidents is kept until the incident is resolved. Unflagged clips should never exceed thirty days. The age of the oldest clip, seventy-five days, suggests deletion stopped about six weeks before the check. The firmware log confirms the date.

### 15.3 Fix

The club's recorder had automatic deletion switched off after a firmware update. Aisha switches it on and adds a monthly check. The firmware update reset several settings to factory defaults, including automatic deletion. Aisha asks the vendor whether updates at other clubs did the same, and the vendor confirms the problem across one model. She checks the other clubs with that model and finds two more with deletion switched off, which are fixed the same week. She then asks for vendor update notes in advance.

### 15.4 Record

She records the findings and fix. Mr. Reilly notes that guided labs show how a simple check can reveal a silent failure. The record includes the date, method, result, root cause, fix and follow-up checks. She also suggests that the vendor change its update process so that privacy settings survive updates. The monthly check is added to the club manager's routine, and the results feed the monitoring she will build later in the course for all forty clubs. This one club becomes the template for the rest.

### Lab — CCTV footage past retention

```python
# CCTV footage retention: clips older than 30 days must be deleted unless flagged for an incident.
import random
r = random.Random(8)
clips = [(r.randint(0, 75), r.random() < 0.04) for _ in range(500)]
over = [a for a, f in clips if a > 30 and not f]; held = [a for a, f in clips if a > 30 and f]
print(f"clips {len(clips)}; older than 30 days {len(over)+len(held)}; held for incidents {len(held)}; to delete {len(over)}")
print(f"oldest unflagged clip {max(over)} days")
```

Run with `python3 lab_cctv.py`. Verified output:

```text
clips 500; older than 30 days 304; held for incidents 12; to delete 292
oldest unflagged clip 75 days
```

### Worked example

Aisha finds 292 of 500 clips past thirty days (oldest 75 days), traces it to deletion disabled by a firmware update, re-enables it and adds a monthly check.

> **Synthetic case.** Clips are synthetic; EDPB Guidelines 3/2019 are real.

### Errors and limits

One club's result may not represent all forty.

### Exercises

- **EX043 — Clips to delete.** How many clips should be deleted? *Rubric:* 3 = 292;; 2 = close;; 1 = wrong;; 0 = none.
- **EX044 — Root cause.** Why was footage not deleted? *Rubric:* 3 = a firmware update switched off automatic deletion;; 2 = mentions firmware;; 1 = none;; 0 = none.
- **EX045 — Ongoing check.** What ongoing control did Aisha add? *Rubric:* 3 = a monthly retention check;; 2 = mentions monthly;; 1 = none;; 0 = none.

<a id="ch-16"></a>

## Chapter 16 — Privacy and data protection: methods II

### Learning outcomes

You will (1) carry out a data protection impact assessment for a new feature; (2) consult stakeholders; (3) record decisions.

### 16.1 The feature

Quayside plans a feature that uses heart-rate trends to suggest rest days. Aisha recognises that systematic processing of health data may require a data protection impact assessment under GDPR Article 35. WP29 guidance WP248 lists criteria such as sensitive data and data at large scale. The product team sees the feature as a simple convenience, but Aisha points out that it analyses health data from thousands of members over long periods and makes suggestions that could influence behaviour. Two WP248 criteria clearly apply, and the guidance suggests that meeting two criteria usually means an assessment is needed before the feature is built and released.

### 16.2 Assessment

She describes the processing, assesses necessity and proportionality, and lists risks: inaccurate suggestions, inference of illness, and sharing with insurers. Mitigations include on-device processing, no sharing and clear explanations. Necessity asks whether the feature needs full heart-rate histories or only recent trends; Aisha finds that fourteen days of data are enough. Proportionality asks whether the benefit justifies the intrusion. The risk of inferring illness is real, because irregular readings could suggest a heart condition. Processing on the member's phone means raw histories never need to leave the device, which removes several risks at once.

### 16.3 Consultation

Aisha consults trainers, five member volunteers and the data protection officer. Members want an easy off switch, which is added. Trainers worry that members might skip sessions on the app's advice without understanding why. The data protection officer asks how members will learn what the feature does and how to switch it off. Volunteers want clear wording, no surprise notifications and assurance that their insurer will never see the data. Aisha records each concern and the design response in the assessment document.

### 16.4 Decision

The data protection officer signs off with conditions. Mr. Reilly notes that the assessment shaped the design rather than just documenting it. The conditions are that the feature is off by default, explained in plain words, processed on the device, and reviewed after three months of use. The assessment is stored with the product documentation, so future changes trigger a review. Mr. Reilly points out that a good assessment records alternatives considered and rejected, not only the final design choice. Here, cloud processing was the rejected alternative.

### Worked example

Aisha runs an impact assessment for rest-day suggestions, chooses on-device processing, adds an off switch after consultation and records sign-off.

> **Synthetic case.** The feature is synthetic; GDPR Article 35 and WP248 are real.

### Errors and limits

Assessments must be updated if the feature changes.

### Exercises

- **EX046 — DPIA trigger.** Why does the feature need an assessment? *Rubric:* 3 = systematic processing of health data at scale;; 2 = mentions health;; 1 = none;; 0 = none.
- **EX047 — Key mitigation.** Name one mitigation. *Rubric:* 3 = on-device processing, no sharing, clear explanations;; 2 = one;; 1 = none;; 0 = none.
- **EX048 — Consultation result.** What did members ask for? *Rubric:* 3 = an easy off switch;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-17"></a>

## Chapter 17 — Privacy and data protection: tooling

### Learning outcomes

You will (1) use a simple scanner to find personal data in files; (2) interpret its limits; (3) act on results.

### 17.1 The scanner

Aisha writes a stdlib Python scanner using regular expressions for email addresses, phone numbers and card numbers. She runs it on five synthetic files from a shared drive. The scanner reads each file line by line, applies three patterns and counts matches without printing the matched values, so the report itself does not spread personal data. Card numbers are checked with a simple digit pattern; she notes that a production tool would add a checksum test. The files are synthetic copies modelled on real types found on the shared drive.

### 17.2 Results

The lab finds patterns in three of five files: an old member export with two emails and two phone numbers, trainer notes with one phone number and a refunds file with one card number. The trainer notes also mention a knee injury, which the regex does not detect. The old export was created for a promotion three years ago and forgotten. The refunds file was saved by a finance assistant to work offline. The trainer notes were shared to cover classes. Each file has a plausible story, which shows that personal data spread through ordinary work rather than carelessness, and that fixing the work pattern matters as much as deleting files.

### 17.3 Limits

Aisha explains that pattern scanners miss free-text health information and may produce false positives. Human review is needed for files flagged and for notes in general. Regular expressions find structured patterns such as email addresses, but health information appears in ordinary words: knee injury, asthma, pregnant. A keyword list could help but would produce many false alarms in a fitness business, where words like heart and injury appear in class descriptions. Aisha recommends using the scanner to prioritise human review, not to declare files clean.

### 17.4 Actions

The old export is deleted, the refunds file is moved to the payment system and trainer notes are moved into the app with access controls. Mr. Reilly notes that tools help but do not replace judgement. Before deleting the old export, she checks with the data protection officer that no legal hold applies. She asks the finance team why they needed an offline copy and finds that the payment system lacked a refunds report, which IT adds. Trainers get a notes field in the app that only the member's own trainers can read, replacing the shared document.

### Lab — Pattern scan of shared files

```python
# Scan synthetic shared-drive files for personal data patterns (email, phone, card-like numbers).
import re
files = {"class_timetable.csv": "Mon,Spin,Studio 2\nTue,Yoga,Studio 1",
         "member_export_old.csv": "name,email,phone\nAna Lima,ana@example.org,+44 7700 900123\nRui Sousa,rui@example.org,+44 7700 900456",
         "trainer_notes.txt": "Client J. knee injury, avoid squats. Call 07700 900789.",
         "refunds_march.txt": "Refund to card 4111 1111 1111 1111 approved",
         "poster.txt": "Summer challenge! Join at the front desk."}
pat = {"email": r"[\w.]+@[\w.]+", "phone": r"(?:\+44 ?|0)7700 ?\d{6}", "card": r"\b(?:\d{4} ?){3}\d{4}\b"}
hits = 0
for f, t in files.items():
    found = {k: len(re.findall(p, t)) for k, p in pat.items() if re.findall(p, t)}
    hits += bool(found); print(f"{f:22s} {found if found else '-'}")
print(f"files with personal data patterns: {hits} of {len(files)}")
```

Run with `python3 lab_scan.py`. Verified output:

```text
class_timetable.csv    -
member_export_old.csv  {'email': 2, 'phone': 2}
trainer_notes.txt      {'phone': 1}
refunds_march.txt      {'card': 1}
poster.txt             -
files with personal data patterns: 3 of 5
```

### Worked example

Aisha's scanner flags three of five files, misses the knee-injury note, and she deletes, moves and secures the files.

> **Synthetic case.** Files are synthetic.

### Errors and limits

Regex scanners miss context and unusual formats.

### Exercises

- **EX049 — Files flagged.** How many files contained patterns? *Rubric:* 3 = 3 of 5;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX050 — Missed data.** What did the scanner miss? *Rubric:* 3 = the knee-injury health note;; 2 = mentions health;; 1 = none;; 0 = none.
- **EX051 — Card file action.** What happened to the refunds file? *Rubric:* 3 = moved to the payment system;; 2 = mentions moved;; 1 = kept;; 0 = none.

<a id="ch-18"></a>

## Chapter 18 — Privacy and data protection: controls

### Learning outcomes

You will (1) select controls for Quayside's risks; (2) map controls to principles; (3) track implementation.

### 18.1 Selecting controls

Aisha lists controls: SDK review, access request checklist, CCTV deletion check, file scanning, multi-factor authentication and inactive account deletion. She chooses controls that respond to findings in earlier chapters rather than copying a generic list. Each control addresses a real failure: the ad SDK, the incomplete access response, the CCTV firmware reset, the forgotten files, weak manager logins and accounts kept forever. This makes the control set easy to explain, because every item has a story that staff remember. Generic controls with no story are deferred.

### 18.2 Mapping

She maps each to principles: SDK review to lawfulness and transparency, CCTV deletion to storage limitation, MFA to integrity and confidentiality. SDK review also supports purpose limitation, because it stops data flowing to new purposes. The access request checklist supports transparency and the right of access. File scanning supports storage limitation and confidentiality. Inactive account deletion supports storage limitation and minimisation. The map shows that accuracy has no dedicated control, so she adds a yearly reminder asking members to check their details.

### 18.3 Standards

She notes that ISO/IEC 27701 provides privacy controls extending an information security management system, and the NIST Privacy Framework organises privacy outcomes. Quayside uses them as reference. She does not attempt certification; she uses the documents as checklists to find missing areas. The NIST Privacy Framework functions, such as Identify-P and Control-P, help her group activities. ISO/IEC 27701 control lists remind her of training and supplier management. She records which reference items Quayside already meets and which are planned, so progress can be shown to the leadership team.

### 18.4 Tracking

Each control has an owner, status and evidence. Mr. Reilly notes that mapping shows coverage gaps. The tracker is a simple table shared with owners. Status values are planned, in progress, operating and tested. A control counts as tested only when evidence shows it worked, such as a log of deleted clips or a completed access request test. Aisha reviews the tracker monthly and asks owners to update evidence links, not just status words. Owners without evidence stay at in progress. Status alone proves nothing.

### Worked example

Aisha lists six controls, maps them to GDPR principles, references ISO/IEC 27701 and the NIST Privacy Framework, and tracks owners and evidence.

> **Synthetic case.** Controls are synthetic; ISO/IEC 27701 and NIST Privacy Framework are real.

### Errors and limits

A mapped control is not necessarily effective.

### Exercises

- **EX052 — CCTV principle.** Which principle does CCTV deletion support? *Rubric:* 3 = storage limitation;; 2 = correct;; 1 = other;; 0 = none.
- **EX053 — Reference standard.** Name one standard used as reference. *Rubric:* 3 = ISO/IEC 27701 or NIST Privacy Framework;; 2 = one;; 1 = none;; 0 = none.
- **EX054 — Mapping benefit.** Why map controls to principles? *Rubric:* 3 = shows coverage gaps;; 2 = mentions gaps;; 1 = none;; 0 = none.

<a id="ch-19"></a>

## Chapter 19 — Privacy and data protection: monitoring

### Learning outcomes

You will (1) monitor privacy controls; (2) set alerts; (3) review trends.

### 19.1 What to monitor

Aisha monitors CCTV retention at all clubs, SDK changes in each app release, access request deadlines and former-staff accounts. She chooses these because each has already failed once or is likely to drift. CCTV deletion failed after a firmware update, SDKs arrive with releases, request deadlines are legal obligations and staff turnover is high. She avoids monitoring everything, because a small set of meaningful signals is easier to act on than a large dashboard nobody reads. Four signals fit on one page.

### 19.2 Alerts

She sets alerts: footage older than thirty-five days, any new SDK, requests within five days of deadline and accounts not removed within two days of leaving. The thresholds include a small margin so that normal timing variations do not trigger alerts. CCTV alerts go to the club manager and IT; SDK alerts go to the app lead and the data protection officer; deadline alerts go to the response team; account alerts go to HR and IT. Each alert message says what to do, not only what happened.

### 19.3 Trends

After three months, former-staff accounts fall from forty to two, and all clubs meet CCTV retention. Access requests are all answered on time, though vendor searches remain the slowest step. One club's CCTV alert fires once after another firmware update, and the fix takes a day instead of six weeks. Aisha notes that the trend data now show the controls working, which is stronger evidence than a statement that a policy exists. Members' complaints about marketing emails also fall to zero over the same period.

### 19.4 Review

She reviews alerts monthly to remove noise. Mr. Reilly notes that monitoring keeps fixes from silently failing, as the CCTV firmware issue showed. In the first month, the SDK alert fires for every minor library update, so she changes it to fire only when a library sends data to a new domain. She records every change to alert rules with a reason, so that reviewers can see whether monitoring was weakened for convenience or improved for accuracy. The SDK alert drops from forty a month to two.

### Worked example

Aisha monitors four controls with alerts, sees stale accounts fall from forty to two and all clubs meet CCTV retention.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Too many alerts cause people to ignore them.

### Exercises

- **EX055 — CCTV alert.** What triggers the CCTV alert? *Rubric:* 3 = footage older than thirty-five days;; 2 = correct;; 1 = none;; 0 = none.
- **EX056 — Account trend.** How did former-staff accounts change? *Rubric:* 3 = from forty to two;; 2 = correct;; 1 = none;; 0 = none.
- **EX057 — Monitoring purpose.** Why monitor fixed controls? *Rubric:* 3 = fixes can silently fail;; 2 = mentions failure;; 1 = none;; 0 = none.

<a id="ch-20"></a>

## Chapter 20 — Privacy and data protection: troubleshooting

### Learning outcomes

You will (1) diagnose privacy failures; (2) find root causes; (3) prevent recurrence.

### 20.1 A failure

A member receives a marketing email after withdrawing consent. Aisha investigates. The member complains to reception, and the complaint reaches the data protection officer, who asks Aisha to find out what went wrong. The member had withdrawn consent through the app nine days earlier. A complaint like this can damage trust and, if repeated, could lead to a complaint to the supervisory authority, so it deserves careful investigation. Aisha starts by collecting the app record, the email platform log and the job history for the nine days.

### 20.2 Diagnosis

She finds the withdrawal recorded in the app but not synchronised to the email platform because a nightly job failed for a week. She follows the withdrawal from the app database to the marketing platform. The app recorded the change correctly with a timestamp. The nightly job that copies preference changes to the email platform had logged errors for seven nights. During that week, 214 synthetic-equivalent withdrawals in the test copy were not transferred, so the problem affected many members, not just one.

### 20.3 Root cause

The job failed after a password change and had no failure alert. She adds an alert and a weekly reconciliation. IT had rotated a service password as part of good security practice but did not update the job's stored credential. The job failed quietly because its error messages went to a mailbox nobody checked. The real cause was therefore a missing alert and missing ownership, not the password change itself, which was the right thing to do. Blaming IT would have fixed nothing.

### 20.4 Prevention

She checks other jobs that carry privacy choices and adds alerts. Mr. Reilly notes that withdrawal must be as easy as giving consent, and must actually work. Aisha lists every job that carries privacy choices: marketing preferences, heart-rate sharing settings, account deletions and vendor data deletions. Each now has an owner and an alert on failure. The weekly reconciliation compares withdrawals in the app with suppressions in the email platform and reports any differences. The affected members receive an apology and confirmation of their choice.

### Worked example

Aisha traces an unwanted email to a failed synchronisation job, adds alerts and reconciliation, and checks similar jobs.

> **Synthetic case.** The failure is synthetic; GDPR Article 7(3) is real.

### Errors and limits

Fixing the symptom alone invites recurrence.

### Exercises

- **EX058 — Cause.** Why did the member get an email? *Rubric:* 3 = sync job failed after a password change;; 2 = mentions job;; 1 = none;; 0 = none.
- **EX059 — Fix.** What fixes did Aisha add? *Rubric:* 3 = an alert and weekly reconciliation;; 2 = one;; 1 = none;; 0 = none.
- **EX060 — Principle.** What does Article 7(3) require? *Rubric:* 3 = withdrawal as easy as giving consent;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-21"></a>

## Chapter 21 — Privacy and data protection: service integration

### Learning outcomes

You will (1) integrate a new vendor safely; (2) check contracts and transfers; (3) limit data shared.

### 21.1 The vendor

Quayside wants a new class booking vendor. Aisha reviews its security, contract and data location. The new vendor offers a better booking screen and a waiting-list feature. Aisha sends a short questionnaire covering security certification, data location, subprocessors, retention, breach notification and support for deletion and access requests. She also reads the vendor's public privacy notice and compares it with the answers, because marketing material and contract terms sometimes say different things. Here the notice listed an analytics partner that the questionnaire omitted.

### 21.2 Contract

The contract must meet GDPR Article 28. The vendor stores data outside the EU, so transfer safeguards are needed. The contract must describe processing only on Quayside's instructions, confidentiality, security, use of subprocessors, help with rights requests, deletion at the end of the service and audit rights. For transfers outside the EU, the GDPR requires safeguards such as standard contractual clauses. Aisha flags these points for the legal team, which negotiates the final contract with the vendor. Signing waits for those clauses. Audit rights are kept.

### 21.3 Minimisation

Aisha limits shared data to name, membership number and bookings; no health data. The vendor's default integration requests date of birth, gender, address and heart-rate zones to personalise class suggestions. Aisha removes these fields because bookings work without them. The vendor agrees, and the integration specification lists the exact fields allowed. Any request to add a field later must go through the data protection officer and update the record of processing. The vendor's waiting list works with membership numbers alone. Fewer fields mean fewer risks to manage.

### 21.4 Testing

She tests the integration with synthetic members. Mr. Reilly notes that integration is where unplanned data flows appear. The tests check that only the listed fields leave Quayside, that cancellations and deletions reach the vendor and that an access request can retrieve the vendor's records. One test finds that the vendor keeps cancelled bookings indefinitely, so the contract adds a retention limit of twelve months. Testing with synthetic members means no real data are exposed while problems are found. Each failed test becomes a contract term.

### Worked example

Aisha checks the vendor's contract and transfers, limits shared fields and tests with synthetic members.

> **Synthetic case.** The vendor is synthetic; GDPR Article 28 is real.

### Errors and limits

Vendors change subprocessors; monitor notices.

### Exercises

- **EX061 — Contract article.** Which article governs processor contracts? *Rubric:* 3 = Article 28;; 2 = correct;; 1 = other;; 0 = none.
- **EX062 — Shared fields.** What data are shared? *Rubric:* 3 = name, membership number, bookings;; 2 = most;; 1 = health;; 0 = none.
- **EX063 — Testing data.** What data were used in testing? *Rubric:* 3 = synthetic members;; 2 = correct;; 1 = real;; 0 = none.

<a id="ch-22"></a>

## Chapter 22 — Privacy and data protection: automation

### Learning outcomes

You will (1) automate deletion of inactive accounts; (2) handle exceptions; (3) verify results.

### 22.1 The rule

Quayside deletes accounts inactive for over two years, after a warning email thirty days before. Two years matches Quayside's documented retention schedule, which balances members returning after long breaks against storage limitation. The warning email gives members a chance to keep their account by logging in. Accounts with unresolved debt are held, because Quayside needs records to pursue or settle the debt, which is a documented exception with its own retention period. The thirty-day warning lets members keep accounts by logging in.

### 22.2 Results

The lab processes 3,000 accounts: 73 warning emails this month, 1,116 to delete, and 37 held for outstanding debt. The lab script reads a synthetic list of 3,000 accounts with last activity dates and debt flags. It calculates which accounts reach the warning point this month, which have passed the deletion point and which are held. The script prints only counts, not identities, and writes the list of affected account numbers to a protected file for the operations team. No names appear in console output or logs.

### 22.3 Exceptions

Accounts with debt are held under a documented basis until resolved. Aisha logs every decision. Each held account is reviewed monthly, and once the debt is settled or written off the account enters deletion in the next run. Aisha considers other possible exceptions, such as legal claims, and adds a manual hold flag that only the data protection officer can set. Every hold records who set it, when and why. Unexplained holds are cleared at the monthly review. In the first run, all thirty-seven holds have a recorded debt reference.

### 22.4 Verification

She samples deleted accounts to confirm removal across systems. Mr. Reilly notes that automation enforces storage limitation reliably. For a sample of twenty deleted accounts, she checks the membership system, app database, email platform and booking vendor. In the first run, the booking vendor still holds three accounts because its deletion interface had failed. The fix adds a confirmation step from the vendor. Deletion is now verified, not assumed, which supports the accountability principle in Article 5(2). Twenty samples each month are enough to detect a broken vendor link.

### Lab — Automated inactive account deletion

```python
# Automated deletion of inactive app accounts: inactive > 24 months, warn at 23 months, skip accounts with debt.
import random
r = random.Random(13)
acc = [(r.randint(0, 40), r.random() < 0.03) for _ in range(3000)]  # months inactive, outstanding debt
warn = sum(1 for m, d in acc if m == 23); dele = sum(1 for m, d in acc if m > 24 and not d); hold = sum(1 for m, d in acc if m > 24 and d)
print(f"accounts {len(acc)}; warning emails this month {warn}; delete {dele}; held for outstanding debt {hold}")
```

Run with `python3 lab_inactive.py`. Verified output:

```text
accounts 3000; warning emails this month 73; delete 1116; held for outstanding debt 37
```

### Worked example

Aisha's job sends 73 warnings, deletes 1,116 accounts and holds 37 with debt, and samples deletions.

> **Synthetic case.** Accounts are synthetic.

### Errors and limits

Deletion must reach backups and vendors over time.

### Exercises

- **EX064 — Deletions.** How many accounts are deleted? *Rubric:* 3 = 1,116;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX065 — Held.** Why are 37 held? *Rubric:* 3 = outstanding debt;; 2 = correct;; 1 = none;; 0 = none.
- **EX066 — Verify.** How is deletion verified? *Rubric:* 3 = sampling across systems;; 2 = mentions sampling;; 1 = none;; 0 = none.

<a id="ch-23"></a>

## Chapter 23 — Privacy and data protection: evaluation

### Learning outcomes

You will (1) evaluate the privacy programme; (2) compare against baseline; (3) recommend priorities.

### 23.1 Comparison

Aisha compares current metrics with the baseline: stale accounts down from forty to two, CCTV retention met, access request coverage complete. She presents each metric with its baseline date and method, so the comparison is fair. Some improvements are large and clear. Others, like breach reports rising from almost none to six a month, need explanation: more reports show better awareness, not more breaches. She avoids claiming that the programme caused every change without supporting evidence. Each comparison cites its source. Context prevents misreading.

### 23.2 Remaining gaps

Free-text health notes remain hard to detect, and vendor monitoring is manual. Health information in free text remains a weakness because the scanner cannot reliably find it. Vendor monitoring depends on someone reading emails about subprocessor changes, which is easy to miss. CCTV access is logged at only thirty clubs because ten older recorders lack the feature. Aisha lists these gaps openly so that leaders understand what the programme does not yet cover. Each gap gets a named owner. None are hidden in footnotes or appendices.

### 23.3 Priorities

She recommends training trainers on notes and automating vendor checks. Training trainers to keep health notes inside the protected app field addresses the first gap at low cost. Automated vendor checks could compare vendor subprocessor lists monthly. Replacing the ten old recorders needs budget, so she estimates the cost and the risk reduction. She ranks priorities by risk reduction per unit of effort, which helps leaders choose. Trainer training costs a single afternoon per region and reduces the largest remaining exposure quickly.

### 23.4 Report

She presents to the data protection officer. Mr. Reilly notes that evaluation turns activity into evidence. The report is short: what was found, what changed, what remains and what she recommends. It includes the evidence for each claim. The data protection officer accepts the first two priorities and asks the finance director about recorder replacement. Mr. Reilly tells Aisha that a balanced evaluation is more credible than one that claims full success. The report runs to two pages in total. Leaders read all of it.

### Worked example

Aisha shows improvement against the baseline, names remaining gaps and recommends priorities.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Improvements may reflect measurement changes.

### Exercises

- **EX067 — Improvement.** Name one improvement. *Rubric:* 3 = stale accounts forty to two; CCTV met; full SAR coverage;; 2 = one;; 1 = none;; 0 = none.
- **EX068 — Remaining gap.** Name one remaining gap. *Rubric:* 3 = free-text health notes; manual vendor monitoring;; 2 = one;; 1 = none;; 0 = none.
- **EX069 — Priority.** What did Aisha recommend? *Rubric:* 3 = trainer training and automated vendor checks;; 2 = one;; 1 = none;; 0 = none.

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) frame a small study; (2) collect data ethically; (3) report limits.

### 24.1 Question

Aisha asks whether members understand the heart-rate sharing settings. Earlier, volunteers mentioned surprise at class screens showing heart-rate zones. Aisha wants to know whether the settings page lets members control this. A clear research question keeps the study small and focused. She writes the question, the method, the participants and the planned analysis before collecting data, so the results cannot shape the question after the fact. She also limits the study to adult members. The question is narrow enough to answer in four weeks with a small group of volunteers.

### 24.2 Method

She runs a short survey with consent and no identifiers, plus five usability sessions. The survey asks members to find and explain each setting and records whether their explanation is correct. The usability sessions ask five members to complete tasks while thinking aloud. Participants receive an information sheet, give consent and can stop at any time. No names are recorded, and session notes use participant numbers that are not linked to accounts. Raw survey files are deleted after analysis. Consent forms are kept separately.

### 24.3 Results

Most participants found the setting but misunderstood class screen sharing. Of the survey participants, most located the heart-rate setting, but fewer than half correctly explained that it controlled sharing to class screens, and several thought it switched off the strap completely. In sessions, two participants searched the class booking page for the setting. These results suggest a wording and placement problem rather than members being uninterested in privacy. Fewer than half explaining the setting correctly is a strong signal that the label, not the members, needs to change.

### 24.4 Limits

The sample is small and self-selected. Mr. Reilly notes that honest limits make results useful. Participants volunteered, so they may care more about privacy than other members. The study took place in two clubs only. The usability sample is small, though small samples can still reveal major problems. Aisha reports these limits beside the results and recommends a follow-up after the redesign to see whether understanding improves, using the same questions. She also notes that participants knew it was a study. Honest limits guide the follow-up.

### Worked example

Aisha studies settings understanding with an anonymous survey and five sessions and reports limits.

> **Synthetic case.** The study is synthetic.

### Errors and limits

Small samples do not generalise.

### Exercises

- **EX070 — Question.** What did the study ask? *Rubric:* 3 = whether members understand heart-rate settings;; 2 = correct;; 1 = none;; 0 = none.
- **EX071 — Ethics.** How was data collected ethically? *Rubric:* 3 = consent and no identifiers;; 2 = one;; 1 = none;; 0 = none.
- **EX072 — Limit.** Name one limit. *Rubric:* 3 = small, self-selected sample;; 2 = one;; 1 = none;; 0 = none.

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) work in a team on a privacy project; (2) divide roles; (3) review peers.

### 25.1 Project

Aisha's team redesigns the app's privacy settings page. The research from the previous chapter showed that members misunderstood the heart-rate sharing setting. The team project turns this finding into a redesign. Aisha works with three classmates from other specialisms: interface design, software development and testing. The team agrees a brief, a timeline of six weeks and a definition of success based on member understanding. Success means most testers explain the setting correctly without help, measured with the same questions as in the earlier study.

### 25.2 Roles

Roles include research, design, development and testing. Aisha leads research and privacy review, a classmate leads interface design, another builds the prototype and a third plans tests. Roles are clear but not rigid; everyone joins two member sessions. The team meets twice a week and keeps a shared log of decisions, which later helps explain why particular wording and layouts were chosen over alternatives. When the designer and developer disagree about placing the setting, the log records the member evidence that settled it.

### 25.3 Review

Peers review each other's work for clarity and accuracy. Reviews follow a simple checklist: is the setting easy to find, is the wording accurate, does the default protect members and does the design work for screen readers. Aisha's wording is criticised for being too long, and she shortens it. Peer review catches an error in the prototype where switching off sharing also stopped workout logging. That bug would have silently removed members' workout history, so the team adds a test checking that sharing and logging are independent settings.

### 25.4 Outcome

The new page explains class screen sharing clearly. Mr. Reilly notes that teamwork brings varied views. In a retest with new volunteers, most participants now explain the setting correctly. The page separates sharing to class screens from the strap connection and uses plain words: show my heart-rate zone on class screens. Sharing is now off by default for new members. The team hands the design to Quayside's app team with the research evidence. Screen sharing now needs a deliberate choice. Existing members are asked once.

### Worked example

The team redesigns the settings page with clear roles and peer review.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Teams can miss member views; test with members.

### Exercises

- **EX073 — Project.** What did the team redesign? *Rubric:* 3 = privacy settings page;; 2 = correct;; 1 = none;; 0 = none.
- **EX074 — Roles.** Name two roles. *Rubric:* 3 = research, design, development, testing;; 2 = two;; 1 = one;; 0 = none.
- **EX075 — Outcome.** What improved? *Rubric:* 3 = explanation of class screen sharing;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-26"></a>

## Chapter 26 — Privacy and data protection: operational handoff

### Learning outcomes

You will (1) hand over controls to operations; (2) write runbooks; (3) confirm ownership.

### 26.1 Runbooks

Aisha writes runbooks for CCTV checks, SDK reviews, access requests and deletions. Each runbook describes the purpose of the task, when to run it, the steps, the expected results, what to do if results are unexpected and who to contact. Aisha writes them for operations staff, not specialists, so she avoids jargon and includes screenshots from the synthetic test environment rather than real systems. The CCTV runbook, for example, lists the recorder menu path, the expected oldest clip age and the number to call when it exceeds thirty-five days.

### 26.2 Ownership

Each runbook names an owner in operations. The CCTV runbook belongs to the operations manager, SDK review to the app lead, access requests to the customer service lead and account deletion to the IT service manager. Each owner has a named deputy for holidays. Ownership is written into job descriptions where possible, so responsibilities survive when people move roles. Without named owners, the CCTV deletion check would depend on whoever happened to remember it, which is exactly how the firmware reset went unnoticed for six weeks.

### 26.3 Training

She trains the owners and watches them run each task. For each runbook, the owner performs the task while Aisha observes and notes where they hesitate or misread steps. The customer service lead struggles with the vendor search for chat transcripts, so Aisha adds clearer steps and a contact name at the vendor. Observation reveals gaps that a document review alone would miss. For the deletion runbook, the IT service manager misreads which vendor confirmation to wait for, so the step now shows an example confirmation message.

### 26.4 Confirmation

Owners sign acceptance. Mr. Reilly notes that handoff keeps controls alive after a project ends. Acceptance means owners agree the runbook is accurate and they can perform it. The data protection officer keeps the signed acceptances. Aisha schedules a follow-up three months later to check that tasks are running, and she leaves her contact details for questions. Handoff is complete when the tasks run without her help. Three months later, all four tasks have run on schedule without her involvement. Her role then ends.

### Worked example

Aisha writes four runbooks, names owners, trains them and gets acceptance.

> **Synthetic case.** Runbooks are synthetic.

### Errors and limits

Runbooks age; review yearly.

### Exercises

- **EX076 — Runbooks.** Name two runbooks. *Rubric:* 3 = CCTV checks, SDK reviews, access requests, deletions;; 2 = two;; 1 = one;; 0 = none.
- **EX077 — Training.** How did Aisha confirm owners could do the tasks? *Rubric:* 3 = watched them run each task;; 2 = correct;; 1 = none;; 0 = none.
- **EX078 — Purpose.** Why hand over? *Rubric:* 3 = keeps controls alive after the project;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) deploy privacy changes; (2) validate them; (3) roll back safely.

### 27.1 Deployment

The new settings page and SDK removal deploy in stages. The new settings page and the app release without the ad SDK go first to five percent of members, then half, then everyone over two weeks. Staged deployment limits the impact of mistakes. The app team monitors crash reports and support contacts at each stage, and Aisha monitors network traffic from test devices for unexpected data flows. At the five percent stage she sees no ad network traffic from any test device.

### 27.2 Validation

Aisha validates with synthetic accounts and network inspection. Validation repeats the earlier flow tests on the new release using the same synthetic accounts and steps, so results can be compared with the earlier findings. She checks every domain contacted by the app and the fields sent. She also checks that the new default for heart-rate sharing is off for newly created accounts. A new test account created on release day confirms that the heart-rate sharing switch starts in the off position. All results match the plan.

### 27.3 Rollback

A rollback plan is ready if errors occur. The rollback plan describes how to return to the previous version if serious problems appear. Aisha points out a privacy issue with rollback: the previous version contained the ad SDK, so rolling back would restart the harmful flow. The team prepares a patched previous version without the SDK to use for any rollback instead. The patched version is tested in advance so that a rollback does not reintroduce the ad network flow under pressure.

### 27.4 Result

Validation confirms no heart-rate data to advertisers. Mr. Reilly notes that validation proves change, not intent. The release reaches all members without serious errors. Network tests show no traffic to the ad network and no heart-rate fields leaving to third parties other than the contracted strap provider. Aisha records the validation results with dates and versions, so the data protection officer can show evidence if a member or regulator asks. The record lists app version, date and test devices. Nothing is left undocumented.

### Worked example

Aisha deploys in stages, validates with synthetic accounts and confirms no advertiser flows.

> **Synthetic case.** The deployment is synthetic.

### Errors and limits

Staged rollouts can mix versions.

### Exercises

- **EX079 — Validation.** How is validation done? *Rubric:* 3 = synthetic accounts and network inspection;; 2 = one;; 1 = none;; 0 = none.
- **EX080 — Rollback.** Why a rollback plan? *Rubric:* 3 = to recover from errors;; 2 = correct;; 1 = none;; 0 = none.
- **EX081 — Result.** What did validation confirm? *Rubric:* 3 = no heart-rate data to advertisers;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) apply skills in clubs; (2) talk with staff; (3) record observations.

### 28.1 Visits

Aisha visits five clubs to check screens, CCTV signs and records. Each visit follows a checklist: reception screens locked when unattended, no member lists visible, CCTV signs present and readable, recorders in locked rooms, guest Wi-Fi separate, and the reporting form known to staff. Aisha chooses clubs of different sizes and ages, including two with older recorders, so that the visits cover a range of conditions. Each visit takes about ninety minutes, and she photographs only signs and room doors, never screens or people.

### 28.2 Staff

She talks with staff about the guide and reporting. Staff are friendly and open about difficulties. Several say the reporting form is easy, but one club had not heard of it because its manager was new. Trainers like the new notes field. Reception staff ask for a quick way to answer members who ask what data Quayside holds, so Aisha drafts a short script. The script tells staff to point members to the access request form in the app rather than reading out data at the desk.

### 28.3 Observations

Two clubs lacked CCTV signs, which EDPB Guidelines 3/2019 expect as a first layer of information. Other observations include a reception screen left unlocked during a busy period and a recorder room used as a store cupboard with the door open. The EDPB guidelines describe a warning sign as the first layer of transparency, telling people about monitoring before they enter the area, with fuller information available elsewhere. Missing signs mean members enter monitored areas without notice. Both clubs had removed old signs during painting and never replaced them.

### 28.4 Follow-up

Signs are installed. Mr. Reilly notes that field visits find what remote checks miss. Signs are installed within two weeks, the store cupboard is cleared and locked, and the new manager receives an introduction to the reporting form. Aisha adds the checklist to the regional managers' routine visits, so field checks continue after her placement. She shares common findings with all clubs without naming individual staff. Regional managers report results quarterly, and repeated findings at the same club trigger a conversation with its manager.

### Worked example

Aisha visits five clubs, finds two missing CCTV signs and gets them installed.

> **Synthetic case.** Visits are synthetic; EDPB Guidelines 3/2019 are real.

### Errors and limits

Visits are snapshots.

### Exercises

- **EX082 — Clubs visited.** How many clubs did Aisha visit? *Rubric:* 3 = five;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX083 — Signs.** What was missing in two clubs? *Rubric:* 3 = CCTV signs;; 2 = correct;; 1 = none;; 0 = none.
- **EX084 — Value.** Why do field visits matter? *Rubric:* 3 = they find what remote checks miss;; 2 = correct;; 1 = none;; 0 = none.

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) build a privacy toolkit; (2) combine labs; (3) document it.

### 29.1 Toolkit

Aisha combines flows, access request, scan, CCTV and inactive account scripts into a toolkit. The scripts come from earlier labs: the SDK flow review, the access request coverage check, the file scanner, the CCTV retention check and the inactive account job. She gives them a common structure, consistent output formats and a shared configuration file for thresholds, so the privacy team can run them the same way each time. Thresholds such as thirty days for footage and two years for inactive accounts live in the configuration file, not in the code.

### 29.2 Documentation

Each script has a purpose, inputs, outputs and limits. For the scanner, the limits section says clearly that free-text health information is not detected. For the CCTV check, it says that the script reads an index, not footage. Documentation also explains how to change thresholds and where outputs are stored. Aisha writes it for people who did not attend her course. Each limits section is written as a direct warning, for example: a clean scan result does not mean a file contains no health information. A worked example with synthetic files shows the expected output for each script.

### 29.3 Testing

She tests all with synthetic data. Each script has a set of synthetic input files with known correct results, so anyone can confirm that the script still works after changes. The tests include edge cases such as empty files, missing dates and accounts with both debt and inactivity. All tests pass before handover, and the results are saved with the toolkit. One test feeds the deletion job an account that is both inactive and in debt and confirms that the hold wins over deletion.

### 29.4 Handover

The toolkit is handed to Quayside's privacy team. Mr. Reilly notes that tools must be maintained. The privacy team names an owner for the toolkit and agrees to review it each year. Aisha explains that scripts written for one version of a system may break when systems change. She also reminds the team that the toolkit uses only standard Python libraries, which keeps maintenance simple and avoids extra dependencies. The privacy team runs every script once with Aisha watching. The first annual review date is set.

### Worked example

Aisha builds and documents a five-script toolkit tested on synthetic data.

> **Synthetic case.** The toolkit is synthetic.

### Errors and limits

Tools need owners.

### Exercises

- **EX085 — Scripts.** How many scripts are combined? *Rubric:* 3 = five;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX086 — Docs.** What does each script's documentation include? *Rubric:* 3 = purpose, inputs, outputs, limits;; 2 = most;; 1 = one;; 0 = none.
- **EX087 — Data.** What data are used for testing? *Rubric:* 3 = synthetic;; 2 = correct;; 1 = real;; 0 = none.

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) present your capstone; (2) answer questions; (3) reflect.

### 30.1 Presentation

Aisha presents her work at Quayside to Mr. Reilly and the data protection officer. Her presentation follows the course: inventory, flows, rights, retention, monitoring and handoff. For each area she shows a finding, the fix and the evidence. She keeps the slides simple and uses numbers from her labs, such as 47 of 287 records in the first access response and 292 clips past retention at one club. She ends with the remaining gaps: free-text health notes, ten old recorders and manual vendor monitoring. Assessors note the honesty.

### 30.2 Questions

Assessors ask about limits, such as free-text health notes. The data protection officer asks how Quayside would detect a new free-text health risk, and Aisha explains the training and sampling approach. Mr. Reilly asks what she would do differently. She answers that she would have started monitoring earlier, because several problems had been present for months before anyone looked at them. She adds that she would have tested the access request process in her first month, since the 16% coverage result changed how the team viewed every other control.

### 30.3 Reflection

Aisha reflects that technical checks reveal real gaps. She reflects that many problems came from ordinary work: slow systems, firmware updates, forgotten files and bundled SDKs. Technical checks found them because they compared what systems actually did with what policies said. She also learned that fixes need owners and monitoring, or they quietly fail again, as the CCTV deletion showed twice. Her strongest lesson is that a synthetic member who walks through a whole process, from sign-up to deletion, reveals more than any checklist.

### 30.4 Next steps

She plans to study governance next. Mr. Reilly notes that privacy work continues after the course. After the course, Quayside offers Aisha a junior privacy technologist role. She plans to study governance, risk and compliance to understand how her technical checks fit into wider management systems. Mr. Reilly closes by noting that the questions she learned to ask will remain useful whatever technologies Quayside adopts in future years. Her first task in the new role is running the access request test again.

### Worked example

Aisha presents, answers questions about limits and reflects on technical checks.

> **Synthetic case.** The assessment is synthetic.

### Errors and limits

Reflection should be honest about failures.

### Exercises

- **EX088 — Audience.** Who assessed? *Rubric:* 3 = Mr. Reilly and the data protection officer;; 2 = both;; 1 = one;; 0 = none.
- **EX089 — Limit asked.** What limit was asked about? *Rubric:* 3 = free-text health notes;; 2 = correct;; 1 = none;; 0 = none.
- **EX090 — Next.** What does Aisha plan next? *Rubric:* 3 = governance study;; 2 = correct;; 1 = none;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Aisha Bello, Mr. Tom Reilly, Lindon Technical Institute, Quayside Fitness and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Membership system, app, wearables and CCTV (club door and booking systems too).

**EX002.** Each club manages its own CCTV with no central owner.

**EX003.** They know whether systems actually follow the policies written about them.

**EX004.** Guests on the same network could access CCTV recorders.

**EX005.** She watched requests with browser developer tools using a test account.

**EX006.** Around thirty days, explained in the privacy notice.

**EX007.** Names are unnecessary for attendance totals.

**EX008.** Booking references and counts.

**EX009.** Test environments are less protected, so real data there often leak.

**EX010.** When they reveal information about health, such as when used to assess fitness.

**EX011.** Member, purpose, wording version, date and status.

**EX012.** Classes need only an age band; the full date stays where contracts need it.

**EX013.** Yes, accidental loss of personal data can be a breach.

**EX014.** Notification deadlines run from when the company becomes aware.

**EX015.** Taking photos of member lists with personal phones.

**EX016.** They held member exports outside central controls.

**EX017.** To isolate it from less critical services.

**EX018.** They avoid central retention rules and access controls.

**EX019.** Bookings and workout data for their own clients.

**EX020.** Forty.

**EX021.** Head office and manager accounts with export rights.

**EX022.** The membership database and the heart-rate store.

**EX023.** So that one failure does not expose data.

**EX024.** Whether it receives personal data and whether a contract exists.

**EX025.** System reports are more reliable than self-reported answers.

**EX026.** As a measurement gap to close.

**EX027.** So later improvements can be demonstrated.

**EX028.** Footage collected for security must not be reused for an incompatible purpose.

**EX029.** Consent.

**EX030.** An Article 9 condition such as explicit consent.

**EX031.** Identity, payment, heart-rate and CCTV (workout and marketing too).

**EX032.** That it stays in the app and is deleted when they leave.

**EX033.** Heart-rate data and CCTV footage.

**EX034.** The ad network.

**EX035.** It lacks a contract.

**EX036.** Every new SDK requires privacy review.

**EX037.** Heart-rate data leakage and app account takeover.

**EX038.** Logging and reviewing access to footage.

**EX039.** They make risks concrete for non-specialists.

**EX040.** 47 of 287 (16%).

**EX041.** Workout history and chat support (also CCTV index and marketing).

**EX042.** A checklist from the inventory with an owner per system.

**EX043.** 292.

**EX044.** Automatic deletion was disabled by a firmware update.

**EX045.** A monthly check of CCTV retention.

**EX046.** It processes health data systematically at scale.

**EX047.** On-device processing.

**EX048.** An easy way to switch the feature off.

**EX049.** Three of five.

**EX050.** Free-text health information about a knee injury.

**EX051.** It was moved into the payment system.

**EX052.** Storage limitation.

**EX053.** ISO/IEC 27701.

**EX054.** It reveals principles without controls.

**EX055.** Footage older than thirty-five days.

**EX056.** From forty to two.

**EX057.** Fixes can fail silently, like the CCTV deletion.

**EX058.** The nightly sync job failed after a password change.

**EX059.** A failure alert and weekly reconciliation.

**EX060.** Withdrawing consent must be as easy as giving it.

**EX061.** Article 28.

**EX062.** Name, membership number and bookings.

**EX063.** Synthetic members.

**EX064.** 1,116.

**EX065.** They have outstanding debt.

**EX066.** By sampling deleted accounts across systems.

**EX067.** Stale accounts fell from forty to two.

**EX068.** Free-text health notes.

**EX069.** Training trainers on notes.

**EX070.** Whether members understand heart-rate sharing settings.

**EX071.** With consent and no identifiers.

**EX072.** Small sample.

**EX073.** The privacy settings page.

**EX074.** Research and design.

**EX075.** Class screen sharing was explained clearly.

**EX076.** CCTV checks and SDK reviews.

**EX077.** She watched them perform each task.

**EX078.** So controls continue after the project.

**EX079.** With synthetic accounts and network inspection.

**EX080.** To recover quickly from errors.

**EX081.** No heart-rate data reach advertisers.

**EX082.** She visited five clubs.

**EX083.** CCTV signs.

**EX084.** They reveal issues remote checks miss.

**EX085.** Five scripts were combined.

**EX086.** Purpose, inputs, outputs and limits.

**EX087.** Synthetic data.

**EX088.** Mr. Reilly and the data protection officer.

**EX089.** Detecting free-text health notes the scanner misses.

**EX090.** Studying governance.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Data Protection Board. (2020). *Guidelines 3/2019 on processing of personal data through video devices* (Version 2.0, adopted 29 January 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-32019-on-processing-of-personal-data-through-video-devices_en>
