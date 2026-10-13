# Privacy and Data Protection: Technical Course

- Language: English (`en`); course 050, Technical course (18 months).
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical students who configure, check and document the systems that hold personal data in a small healthcare business.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs find personal data in synthetic log lines, check which cookies a synthetic site sets before consent, flag record views outside a staff member's clinic in a synthetic audit log and apply a retention rule to synthetic reminder records. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one technical student through eighteen months centred on a dental group: services, networks, identities and scripting, scope and evidence, the processing model, telemetry, failure modes, methods, configuration, verification, two contained labs, troubleshooting, automation, integration, documentation and a supervised project. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leila Haddad** | Technical student | Invented |
| **Mr. Daniel Okafor** | Instructor | Invented |
| **Riverside Technical College** | Fictional college | Invented |
| **Marlow Dental Group** | Fictional dental group, 8 clinics, about 45,000 patients, online booking and SMS reminders | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR) Articles 4(15), 5, 9(2)(h), 15, 17, 28, 30, 32 and 33; Directive 2002/58/EC (ePrivacy) Article 5(3); EDPB Guidelines 05/2020 (consent); Lei 13.709/2018 (LGPD); NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 27701:2025. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe the services a small healthcare business runs; (2) identify where patient data are stored and processed; (3) draw a simple service map.

### 1.1 The course and the case

Leila Haddad starts an eighteen-month technical course at the fictional Riverside Technical College. Her instructor, Mr. Daniel Okafor, pairs every topic with a placement at the fictional Marlow Dental Group, which runs eight clinics, treats about 45,000 patients and offers online booking with text-message reminders. Dental records include treatment notes, X-ray images and medical histories, which are data concerning health under Article 4(15) of the GDPR. Leila's role is technical: configuring, checking and documenting the systems that hold this information, always under supervision and using synthetic test data.

### 1.2 Services and components

Marlow's main services are a cloud practice-management system holding patient records, an imaging server in each clinic for X-rays, a booking website, an SMS gateway for reminders, email, and a payroll service for staff. Leila learns to separate a service, which is what users experience, from the components that deliver it: servers, databases, network links and vendor platforms. The booking service, for example, depends on the website, the practice-management system's interface and the SMS gateway, so a privacy problem in any one of them affects patients who book online.

### 1.3 Where data live

For each service, Leila asks three questions: what patient data does it store, where is it physically or logically hosted, and who can reach it. She finds X-ray images on local servers in every clinic, copies of referral letters in a shared mailbox and appointment lists exported to a spreadsheet by one receptionist. These locations matter because protection, retention and access requests must cover every copy, not just the main system. A record that exists in four places has four chances to be lost, kept too long or overlooked.

### 1.4 A first service map

Leila draws a service map with boxes for services, cylinders for data stores and arrows for flows, labelling each arrow with the data it carries. Mr. Okafor asks her to mark vendors in a different colour, because Marlow does not control their systems directly. The map shows that the SMS gateway receives patient names, phone numbers and appointment times, which reveals that a person is a dental patient. The map becomes the reference for later chapters, and Leila dates it so that changes can be tracked.

### Worked example

Leila lists Marlow's services, separates services from components, finds patient data in local imaging servers, a shared mailbox and an exported spreadsheet, and draws a dated service map with vendors marked.

> **Synthetic case.** Riverside, Marlow and all people are synthetic; GDPR Article 4(15) is real.

### Errors and limits

A first map misses informal copies; interview staff as well as reading system lists.

### Exercises

- **EX001 — Health data.** Why are dental treatment notes data concerning health? *Rubric:* 3 = they reveal information about a person's health status;; 2 = mentions health;; 1 = vague;; 0 = none.
- **EX002 — Service and component.** What is the difference between a service and a component? *Rubric:* 3 = a service is what users experience; components deliver it;; 2 = both;; 1 = one;; 0 = none.
- **EX003 — Copies matter.** Why does every copy of a record matter? *Rubric:* 3 = protection, retention and access requests must cover all copies;; 2 = mentions copies;; 1 = vague;; 0 = none.
- **EX004 — SMS content.** What does the SMS gateway learn about patients? *Rubric:* 3 = names, phone numbers, appointment times and that they are dental patients;; 2 = most;; 1 = one;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) trace patient data across clinic networks; (2) check protocols for encryption; (3) recommend network separation.

### 2.1 Clinic networks

Each Marlow clinic has a small network connecting reception computers, dental chairs with intraoral cameras, the imaging server, a printer and a guest Wi-Fi access point. Leila maps the network with the clinic's IT contractor and discovers that guest Wi-Fi and the imaging server share one flat network in three clinics. A patient in the waiting room could therefore reach the server's file shares. She explains that separating networks into zones is a basic measure under Article 32, because it limits who can even attempt to access sensitive systems.

### 2.2 Protocols in use

Leila lists the protocols that carry patient data: HTTPS between browsers and the practice-management system, DICOM for X-ray images between cameras and the imaging server, SMB file shares for scanned letters, and SMTP for email. She learns that DICOM traffic inside the clinic is unencrypted by default, which is common in medical imaging. She records this as a risk rather than a failure, because changing imaging protocols needs vendor support and testing, and she proposes protecting it through network separation first. Each protocol is listed with its port.

### 2.3 Checking encryption

Using a test workstation and synthetic records, Leila checks which connections are encrypted. The booking website and practice-management system use TLS. The SMS gateway's interface also uses TLS. However, the clinic printer receives referral letters over plain text, and the scanning station saves files to an unencrypted share. She documents each finding with the protocol, the data carried and the recommended change, so that the IT contractor can plan the work and Mr. Okafor can check her reasoning before anything is altered.

### 2.4 Recommending separation

Leila proposes three zones per clinic: a clinical zone for chairs, cameras and the imaging server; an office zone for reception and printers; and a guest zone with internet access only. Traffic between zones is limited to what each workflow needs, such as reception viewing images through the practice-management system rather than browsing the imaging server directly. The contractor implements the design in one clinic first. Leila tests from the guest Wi-Fi with a laptop and confirms that the imaging server is no longer reachable.

### Worked example

Leila maps clinic networks, finds guest Wi-Fi sharing a network with the imaging server, lists protocols including unencrypted DICOM and printing, and recommends three zones that are tested in one clinic.

> **Synthetic case.** Networks are synthetic; GDPR Article 32 is real.

### Errors and limits

Separation can break workflows; test with clinic staff before rolling out.

### Exercises

- **EX005 — Guest risk.** Why was the shared guest network a problem? *Rubric:* 3 = patients could reach the imaging server;; 2 = mentions server;; 1 = vague;; 0 = none.
- **EX006 — DICOM.** How did Leila treat unencrypted DICOM traffic? *Rubric:* 3 = as a risk managed by separation first;; 2 = mentions separation;; 1 = vague;; 0 = none.
- **EX007 — Three zones.** Name the three zones Leila proposed. *Rubric:* 3 = clinical, office and guest;; 2 = all;; 1 = two;; 0 = none.
- **EX008 — Confirming the change.** How did Leila confirm the separation worked? *Rubric:* 3 = tested from guest Wi-Fi that the server was unreachable;; 2 = mentions test;; 1 = vague;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) configure accounts on clinic computers; (2) apply least privilege; (3) manage shared and departing accounts.

### 3.1 Accounts on clinic computers

Reception computers at Marlow were set up years ago with one shared login per clinic. Leila explains to the practice managers that shared accounts make it impossible to tell who opened a patient record, which undermines both security and accountability under Article 5(2). With the IT contractor, she plans individual accounts for each staff member, linked to the central directory, with automatic screen locking after five minutes. She tests the change with synthetic patients at one clinic before the contractor rolls it out elsewhere.

### 3.2 Least privilege

Leila reviews roles in the practice-management system. Receptionists need appointments, contact details and payment status, but not treatment notes. Dental nurses need notes for the patients they assist. Dentists need full clinical records for their patients. Managers need reports. She finds that all receptionists currently have clinical access because a default role was copied years ago. She proposes narrower roles, and the practice manager approves them after Leila shows that reception tasks still work with synthetic records. Nurses keep access only to their own clinic's patients.

### 3.3 Administrator rights

On clinic computers, staff accounts had local administrator rights so that they could install printer drivers. Leila explains that administrator rights let malware spread and let users install unapproved software that might send data elsewhere. She removes the rights in the pilot clinic and creates a short procedure for printer installation by the contractor. The change reduces the number of administrator accounts from twenty-three to four, and she records each remaining account with its owner and justification. The contractor now installs drivers remotely.

### 3.4 Joiners and leavers

Dental clinics use locum staff for short periods. Leila finds accounts for locums who left months ago still active. She links account creation and removal to the rota system, so each locum account has an end date and is disabled automatically. For permanent staff, removal is triggered by the HR leaver form. She runs a monthly report comparing active accounts with current staff and sends differences to practice managers, keeping the reports as evidence that the control operates. The first report finds six expired locum accounts.

### Worked example

Leila replaces shared logins with individual accounts, narrows reception roles away from clinical notes, removes local administrator rights and links locum accounts to rota end dates.

> **Synthetic case.** Accounts and roles are synthetic; GDPR Article 5(2) is real.

### Errors and limits

Narrow roles can block urgent tasks; define a recorded emergency access route.

### Exercises

- **EX009 — Shared login problem.** Why are shared logins a privacy problem? *Rubric:* 3 = nobody can tell who opened a record;; 2 = mentions accountability;; 1 = vague;; 0 = none.
- **EX010 — Reception access.** What does reception need in the practice system? *Rubric:* 3 = appointments, contact details, payment status;; 2 = most;; 1 = notes;; 0 = none.
- **EX011 — Admin count.** How many administrator accounts remained? *Rubric:* 3 = four of twenty-three;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX012 — Locum control.** How are locum accounts controlled now? *Rubric:* 3 = end dates linked to the rota;; 2 = mentions end date;; 1 = vague;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) read CSV and JSON exports safely; (2) write scripts that minimise output; (3) validate data before processing.

### 4.1 Common formats

Marlow's systems export data as CSV files for spreadsheets and JSON for system interfaces. Leila practises reading both with Python's standard csv and json modules, using synthetic patient records. She notes that CSV files are easily opened in spreadsheets and emailed, so they spread quickly, while JSON exports often contain more fields than anyone looks at. In one synthetic JSON export, she finds a medical history field nested inside the appointment object, even though the booking report needs only times and clinic codes.

### 4.2 Minimal output

Leila writes a script that counts appointments per clinic per day for capacity planning. Her first version prints the full appointment rows while debugging. She rewrites it to output only counts and to write debugging details to a temporary file that is deleted at the end. Mr. Okafor explains that outputs from scripts often end up in tickets, chat messages and email, so a script that prints patient names can create a disclosure even when nobody intended to share anything. Only aggregate counts leave the script.

### 4.3 Validating input

Before processing an export, Leila's script checks that the file has the expected columns and rejects files with unexpected ones such as medical_history or date_of_birth. It also checks that dates parse correctly and that clinic codes are between one and eight. When validation fails, the script stops with a clear message instead of guessing. She explains that validation enforces minimisation at the point where data enter a tool, and it also catches export mistakes before they produce misleading reports.

### 4.4 Handling files

Leila's scripts read exports from a restricted folder and never copy them to desktops or personal drives. Temporary files use Python's tempfile module and are removed when the script ends. She adds a note at the top of each script explaining what data it reads, why and what it outputs. Mr. Okafor reviews the scripts and asks her to remove an unused import of a third-party plotting library, keeping the tools dependent on the standard library only, which simplifies review and maintenance.

### Worked example

Leila reads CSV and JSON exports, finds an unnecessary nested medical history field, writes a count-only capacity script, validates columns and values, and handles files only in a restricted folder.

> **Synthetic case.** Exports are synthetic.

### Errors and limits

Validation rules need updating when systems change their export formats.

### Exercises

- **EX013 — Nested field.** What unnecessary field did Leila find in the JSON export? *Rubric:* 3 = medical history inside appointments;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX014 — Script output.** Why should scripts avoid printing names? *Rubric:* 3 = outputs end up in tickets and chats;; 2 = mentions spread;; 1 = vague;; 0 = none.
- **EX015 — Validation action.** What does the script do when validation fails? *Rubric:* 3 = stops with a clear message;; 2 = partly correct;; 1 = guesses;; 0 = none.
- **EX016 — Temporary files.** How are temporary files handled? *Rubric:* 3 = tempfile module, removed at the end;; 2 = mentions removal;; 1 = kept;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) define the scope of a technical check; (2) obtain authorisation; (3) collect and store evidence properly.

### 5.1 Defining scope

Before Leila checks any Marlow system, Mr. Okafor requires a written scope: which systems, which clinics, which dates, what methods and what is excluded. For her first check, the scope covers account settings and network zones in the pilot clinic, using synthetic patient records in a test copy of the practice-management system. Live patient records and the vendor's cloud infrastructure are excluded. He explains that clear scope protects patients, Marlow and Leila herself, because work outside scope can cause harm or break contracts.

### 5.2 Authorisation

The scope is signed by Marlow's operations director and the data protection officer. The practice-management vendor is informed because its terms forbid testing without notice. Leila keeps the signed scope with her notes and carries a copy during clinic visits. When a practice manager asks her to look at a live record to explain a problem, she declines and asks for the issue to be reproduced with synthetic data, recording the request and her answer in her log. Her log also records who approved each step.

### 5.3 Evidence collection

Leila records each finding with the date, time, system, method, what she observed and a screenshot or command output taken from the test environment. She avoids capturing real patient data in screenshots by using synthetic records and cropping irrelevant parts. Evidence is stored in a restricted folder with access for her, Mr. Okafor and the data protection officer. She explains that evidence must allow someone else to repeat the check and reach the same result. File names follow a fixed pattern of date, clinic and check name, so evidence can be found quickly.

### 5.4 Integrity of evidence

To show that evidence has not been changed, Leila calculates a SHA-256 hash of each evidence file using Python's hashlib and records the hashes in a log. When the data protection officer later reviews the findings, she recalculates two hashes and they match. Mr. Okafor notes that hashing does not protect confidentiality, only integrity, and that evidence containing personal data must still be protected and deleted when no longer needed, following the same retention rules as other records. The hash log is itself stored read-only.

### Worked example

Leila writes a signed scope excluding live records, informs the vendor, declines an out-of-scope request, records findings with method and time, and hashes evidence files.

> **Synthetic case.** Scope and evidence are synthetic.

### Errors and limits

Scope creep happens gradually; recheck the scope before each new task.

### Exercises

- **EX017 — Scope exclusion.** What did Leila's first scope exclude? *Rubric:* 3 = live patient records and vendor infrastructure;; 2 = both;; 1 = one;; 0 = none.
- **EX018 — Declined request.** Why did Leila decline to view a live record? *Rubric:* 3 = outside scope; reproduce with synthetic data;; 2 = mentions scope;; 1 = vague;; 0 = none.
- **EX019 — Evidence fields.** What does each finding record include? *Rubric:* 3 = date, time, system, method, observation, screenshot;; 2 = most;; 1 = few;; 0 = none.
- **EX020 — Hash purpose.** What does hashing evidence prove? *Rubric:* 3 = integrity, not confidentiality;; 2 = partly correct;; 1 = confidentiality;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Privacy and data protection: system model

### Learning outcomes

You will (1) model processing activities technically; (2) link systems to purposes and lawful bases; (3) identify recipients and transfers.

### 6.1 Purposes and systems

Leila turns her service map into a processing model. Each purpose, such as providing dental care, booking appointments, sending reminders, billing and staff payroll, is linked to the systems that support it. Providing care uses the practice-management system and imaging servers. Reminders use the practice-management system and the SMS gateway. She notes that the GDPR's record of processing under Article 30 is organised by purpose, so a technical model built the same way can feed the record directly. Payroll uses only the external payroll service.

### 6.2 Lawful bases and conditions

With the data protection officer, Leila notes the lawful basis for each purpose. Care relies on the provision of health care, with Article 9(2)(h) as the condition for health data. Billing relies on contract and legal obligation. Reminders rely on legitimate interests, with an easy opt-out. Marketing of whitening offers requires consent. Leila's role is not to decide these, but her model shows which systems process data for each basis, so that a change in one place does not silently alter another.

### 6.3 Recipients

The model lists recipients: the practice-management vendor and SMS gateway as processors, the dental laboratory receiving impressions and prescriptions, specialist referral clinics and the payroll provider. Each processor needs a contract under Article 28. Leila checks that contracts exist and finds none for a small courier company that carries printed lab prescriptions with patient names. She flags this for the operations director, noting that paper flows are part of the system model even though no software is involved. Paper still carries patient names across town.

### 6.4 Transfers

Leila asks each vendor where data are stored. The practice-management system hosts data in the EU. The SMS gateway routes messages through a provider whose support team is in another country outside the EU. She records this as a possible transfer that needs safeguards under Chapter V of the GDPR and passes it to the data protection officer. Mr. Okafor reminds her that technical staff often discover transfers first, because they see network destinations and support arrangements. Her note lists the vendor's support location.

### Worked example

Leila links purposes to systems, records lawful bases with the data protection officer, lists recipients, finds a courier without a contract and flags an SMS support transfer outside the EU.

> **Synthetic case.** The model is synthetic; GDPR Articles 9(2)(h), 28 and 30 and Chapter V are real.

### Errors and limits

Lawful bases are decided by the controller with advice; technical staff document them.

### Exercises

- **EX021 — Model structure.** How is Leila's processing model organised? *Rubric:* 3 = by purpose, like the Article 30 record;; 2 = mentions purpose;; 1 = systems only;; 0 = none.
- **EX022 — Care condition.** Which Article 9 condition supports care? *Rubric:* 3 = Article 9(2)(h);; 2 = partly correct;; 1 = consent;; 0 = none.
- **EX023 — Courier gap.** What gap did Leila find with the courier? *Rubric:* 3 = no processor contract;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX024 — Possible transfer.** What possible transfer did Leila flag? *Rubric:* 3 = SMS provider support outside the EU;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Privacy and data protection: data and telemetry

### Learning outcomes

You will (1) find personal data in logs and telemetry; (2) mask it safely; (3) set log retention.

### 7.1 Telemetry everywhere

Marlow's systems produce logs, error reports and usage statistics. The booking server logs each request, the SMS gateway logs delivery results and the website sends performance data to a monitoring service. Leila learns that telemetry is often designed by developers for debugging, with little thought about privacy. Logs are copied to monitoring tools, shared with vendors during support cases and kept longer than the data they describe. A log line that includes an email address can therefore travel further than the booking record itself.

### 7.2 The log lab

Leila analyses a synthetic sample of booking-server logs. The lab shows that 95 of 400 lines, 23.8%, contain personal data: 75 include patient email addresses and 20 include phone numbers from failed text messages. Each of those lines links a person to a dental appointment. After a masking step that replaces emails with a placeholder and hides phone digits, no lines with personal data remain. The booking reference still allows support staff to trace a problem through the practice-management system when they are authorised to do so.

### 7.3 Fixing at the source

Masking after the fact is useful, but Leila argues that the better fix is to stop logging personal data in the first place. She asks the developer to log booking references instead of emails and to record only the last three digits of phone numbers for failed messages. The developer agrees and changes the logging calls in the next release. Leila reruns the analysis on synthetic traffic from the new version and confirms that no new lines contain email addresses or full phone numbers.

### 7.4 Retention for logs

Logs are kept for ninety days in the monitoring service by default, and old logs in the booking server were never deleted. Leila proposes thirty days for detailed logs, which covers most troubleshooting, and twelve months for aggregated statistics without personal data. She documents the decision with the data protection officer, linking it to storage limitation in Article 5(1)(e). The IT contractor configures automatic deletion, and Leila adds a quarterly check that the oldest log file is younger than the limit. The first check passes.

### Lab — Personal data in booking-server logs

```python
"""Find and mask personal data in synthetic booking-server log lines (stdlib only)."""
import random, re
random.seed(7)
names = ["ana", "ben", "chloe", "dev", "erin", "farid", "gita", "hugo"]
lines = []
for i in range(400):
    kind = random.random()
    if kind < 0.15:
        lines.append(f"INFO booking created for {random.choice(names)}@example.org slot={i}")
    elif kind < 0.22:
        lines.append(f"WARN sms failed to +44 7700 900{random.randint(100,999)} ref={i}")
    else:
        lines.append(f"INFO booking created ref=B{i:05d} clinic={random.randint(1,8)}")
EMAIL = re.compile(r"[\w.]+@[\w.]+"); PHONE = re.compile(r"\+44 \d{4} \d{6}")
hit = [l for l in lines if EMAIL.search(l) or PHONE.search(l)]
masked = [PHONE.sub("+44 **** ******", EMAIL.sub("<email>", l)) for l in lines]
left = sum(1 for l in masked if EMAIL.search(l) or PHONE.search(l))
print(f"log lines {len(lines)}; with personal data {len(hit)} ({100*len(hit)/len(lines):.1f}%)")
print(f"emails {sum(1 for l in lines if EMAIL.search(l))}; phones {sum(1 for l in lines if PHONE.search(l))}; after masking {left}")
```

Run with `python3 lab_logs.py`. Verified output:

```text
log lines 400; with personal data 95 (23.8%)
emails 75; phones 20; after masking 0
```

### Worked example

Leila finds personal data in 95 of 400 synthetic log lines (23.8%), masks them to zero, has the developer stop logging emails and full phone numbers, and sets thirty-day log retention.

> **Synthetic case.** Logs are synthetic; GDPR Article 5(1)(e) is real.

### Errors and limits

Regular expressions miss unusual formats; review samples by hand as well.

### Exercises

- **EX025 — Log share.** What share of log lines held personal data? *Rubric:* 3 = 95 of 400, 23.8%;; 2 = approximate;; 1 = wrong;; 0 = none.
- **EX026 — Source fix.** What did the developer change? *Rubric:* 3 = log booking references, partial phone digits;; 2 = mentions references;; 1 = vague;; 0 = none.
- **EX027 — Why logs travel.** Why do logs spread further than records? *Rubric:* 3 = copied to monitoring tools and shared in support cases;; 2 = mentions copies;; 1 = vague;; 0 = none.
- **EX028 — Log retention.** What retention did Leila propose for detailed logs? *Rubric:* 3 = thirty days;; 2 = partly correct;; 1 = ninety;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Privacy and data protection: failure modes

### Learning outcomes

You will (1) identify how privacy controls fail; (2) classify failures; (3) design detection for each.

### 8.1 Ways controls fail

Leila lists ways that privacy controls can fail at Marlow: an SMS reminder sent to an old phone number now used by someone else, a referral letter emailed to the wrong clinic, an X-ray exported to a USB stick and lost, a former locum's account still active, and an automatic deletion job that stops running. She notes that most failures are not attacks but ordinary errors or silent breakdowns, and that each can expose health information about a patient to someone who should not see it.

### 8.2 Classifying failures

She classifies failures into four types. Wrong recipient failures send data to the wrong person. Over-retention failures keep data too long. Over-access failures let people see more than they need. Silent control failures happen when a protective job or setting stops working without anyone noticing. The classification helps her choose controls: wrong recipient failures need checks before sending, over-retention needs deletion jobs, over-access needs role design and silent failures need monitoring that someone actually reads. Each past incident at Marlow is tagged with one type, and wrong recipient turns out to be the most common.

### 8.3 Detection design

For each failure type, Leila designs a way to notice it. Wrong recipient emails are detected through staff reports and an outbound warning for external addresses. Over-retention is detected by a monthly query of the oldest records. Over-access is detected by reviewing audit logs for views outside a staff member's clinic. Silent failures are detected by jobs that report success daily, so that a missing report triggers an alert. She notes that a control without detection may fail for months before anyone notices.

### 8.4 The reminder case

Leila studies the old phone number case in detail. A patient changed numbers but did not tell the clinic, and the new owner of the number received reminders naming the patient and the clinic. Leila recommends that reminders contain only the clinic name and time, not the patient's full name or treatment type, and that reception confirms phone numbers at each visit. The data protection officer treats the original event as a personal data breach and records it, even though the risk was assessed as low.

### Worked example

Leila lists failures, classifies them as wrong recipient, over-retention, over-access and silent failure, designs detection for each and reduces reminder content after a wrong-number case.

> **Synthetic case.** Failures are synthetic; GDPR Article 33 breach recording is real.

### Errors and limits

Detection depends on people acting on alerts; assign owners.

### Exercises

- **EX029 — Four types.** Name the four failure types. *Rubric:* 3 = wrong recipient, over-retention, over-access, silent failure;; 2 = all;; 1 = two;; 0 = none.
- **EX030 — Silent detection.** How are silent failures detected? *Rubric:* 3 = jobs report success daily; missing report alerts;; 2 = mentions daily;; 1 = vague;; 0 = none.
- **EX031 — Reminder content.** What should reminders contain now? *Rubric:* 3 = only clinic name and time;; 2 = partly correct;; 1 = full details;; 0 = none.
- **EX032 — Breach recording.** Why was the wrong-number case recorded? *Rubric:* 3 = it was a personal data breach even if low risk;; 2 = mentions breach;; 1 = vague;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Privacy and data protection: tools and methods

### Learning outcomes

You will (1) choose tools for privacy checks; (2) use standard-library scripts responsibly; (3) document methods for repeatability.

### 9.1 Choosing tools

Leila needs tools to search exports, analyse logs, check cookies and review audit trails. Mr. Okafor sets a rule for the course: use built-in system features and Python's standard library before adding new software, because every new tool needs approval, updates and a check of what data it sends elsewhere. Some commercial scanners upload files to the vendor's cloud for analysis, which would itself be a disclosure of patient data. Leila adds a question to her tool checklist: where does this tool send the data it reads?

### 9.2 Methods before tools

Leila writes a method for each check before choosing a tool: the question, the data source, the steps, the expected output and how to interpret it. For example, the method for checking log retention asks: what is the oldest log file in each location, and is it within thirty days? The tool is then a short script or a system command that answers that question. She learns that a clear method makes it easier to explain results and to swap tools later without changing the conclusion.

### 9.3 Repeatability

Each method is saved with its script, the synthetic test data and the expected results. Another student can run the same method and compare outputs. Leila uses fixed random seeds in synthetic data generators so results are identical across runs. When a result changes unexpectedly, the saved expected output shows immediately that something in the system or the script has changed. Mr. Okafor explains that repeatable checks turn privacy controls into something that can be tested like any other technical requirement. Expected outputs are kept under version control.

### 9.4 Responsible use

Tools that read personal data are themselves processing. Leila's scripts run only on the restricted analysis computer, read only the exports named in the scope and produce counts or masked outputs. She records each run in a log with the date, method, input file name and result summary. When she finishes a check, she deletes working copies of exports. She explains that privacy tools should be held to the same standards as the systems they examine, otherwise they become a new source of risk.

### Worked example

Leila prefers built-in features and the standard library, asks where each tool sends data, writes methods before choosing tools, saves expected outputs with fixed seeds and logs every run.

> **Synthetic case.** Tools and methods are synthetic.

### Errors and limits

Built-in tools have limits; document what a method cannot detect.

### Exercises

- **EX033 — Tool question.** What question did Leila add to her tool checklist? *Rubric:* 3 = where does the tool send the data it reads;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX034 — Method parts.** What does each method define? *Rubric:* 3 = question, source, steps, expected output, interpretation;; 2 = most;; 1 = few;; 0 = none.
- **EX035 — Fixed seeds.** Why use fixed random seeds? *Rubric:* 3 = identical synthetic data across runs;; 2 = mentions repeatability;; 1 = vague;; 0 = none.
- **EX036 — Tools as processing.** Why are privacy tools themselves a risk? *Rubric:* 3 = they process personal data too;; 2 = mentions processing;; 1 = vague;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Privacy and data protection: control configuration

### Learning outcomes

You will (1) check cookie behaviour on a website; (2) configure consent correctly; (3) verify configuration changes.

### 10.1 Cookies and consent

Marlow's booking website sets cookies and similar technologies. Article 5(3) of the ePrivacy Directive requires consent before storing or reading information on a user's device, unless it is strictly necessary for a service the user requested. EDPB Guidelines 05/2020 explain that consent must be freely given, specific, informed and unambiguous. Leila's task is technical: check which cookies the site actually sets, when they are set and whether the consent banner controls them as the privacy notice claims. Cookies that only remember a visitor's chosen settings may be exempt, but only after the visitor has made that choice.

### 10.2 The cookie lab

Leila loads the site in a clean browser profile, records cookies before interacting with the banner and repeats after accepting. The lab summarises her synthetic results: seven cookies, of which three are set before consent without an exemption. The analytics cookie and an advertising pixel load immediately. A language cookie is also set automatically before the visitor has chosen a language, so it is not clearly necessary for a service the visitor requested. The session and security token cookies are strictly necessary and correctly load immediately.

### 10.3 Fixing the configuration

The website uses a tag manager to load scripts. Leila works with the web developer to set the analytics and advertising tags to fire only after consent is recorded, and to set the language cookie only when a visitor selects a language. The banner is changed so that refusing is as easy as accepting, with buttons of equal size on the first layer. The advertising pixel is removed altogether, because Marlow does not run advertising campaigns that need it and nobody could explain why it was installed.

### 10.4 Verifying the change

Leila repeats the test in a clean profile after the change. Before consent, only the session and security cookies appear. After refusing, no analytics cookies appear, even after browsing several pages. After accepting, analytics loads as expected. She records the results with dates and browser versions. She also adds the test to the release checklist, because website changes and new plugins often reintroduce tags that load before consent, and a quick repeat test catches this before patients are affected. Screenshots show each cookie list.

### Lab — Cookies set before consent

```python
"""Check which cookies a synthetic booking site sets before consent (stdlib only)."""
cookies = [
    ("session_id", "strictly necessary", "before"),
    ("csrf_token", "strictly necessary", "before"),
    ("lang", "functional", "before"),
    ("_ga", "analytics", "before"),
    ("_fbp", "advertising", "before"),
    ("chat_widget", "functional", "after"),
    ("ab_test", "analytics", "after"),
]
bad = [c for c in cookies if c[2] == "before" and c[1] not in ("strictly necessary",)]
for n, cat, when in cookies:
    flag = "PROBLEM" if (n, cat, when) in bad else "ok"
    print(f"{n:12s} {cat:19s} set {when:6s} consent  {flag}")
print(f"cookies set before consent without exemption: {len(bad)} of {len(cookies)}")
```

Run with `python3 lab_cookies.py`. Verified output:

```text
session_id   strictly necessary  set before consent  ok
csrf_token   strictly necessary  set before consent  ok
lang         functional          set before consent  PROBLEM
_ga          analytics           set before consent  PROBLEM
_fbp         advertising         set before consent  PROBLEM
chat_widget  functional          set after  consent  ok
ab_test      analytics           set after  consent  ok
cookies set before consent without exemption: 3 of 7
```

### Worked example

Leila finds three of seven cookies set before consent without exemption, has tags fire only after consent, removes an unused advertising pixel, equalises banner buttons and verifies with a clean profile.

> **Synthetic case.** The website is synthetic; Directive 2002/58/EC Article 5(3) and EDPB Guidelines 05/2020 are real.

### Errors and limits

Cookie names do not prove purpose; check what each script actually does.

### Exercises

- **EX037 — Before consent.** How many cookies were set before consent without exemption? *Rubric:* 3 = 3 of 7;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX038 — Language cookie.** Why was the language cookie a problem? *Rubric:* 3 = set before the visitor chose a language;; 2 = mentions choice;; 1 = vague;; 0 = none.
- **EX039 — Pixel decision.** What happened to the advertising pixel? *Rubric:* 3 = removed; nobody needed it;; 2 = mentions removal;; 1 = delayed;; 0 = none.
- **EX040 — Release check.** Why add the cookie test to the release checklist? *Rubric:* 3 = changes often reintroduce early tags;; 2 = mentions regressions;; 1 = vague;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Privacy and data protection: verification

### Learning outcomes

You will (1) verify that privacy controls work as designed; (2) use sampling; (3) report verification honestly.

### 11.1 What verification means

Leila distinguishes three questions: is the control designed correctly, is it implemented as designed, and does it operate consistently over time? A role design may be correct on paper, implemented with an error and later changed by an administrator. Verification needs evidence for each question. Mr. Okafor gives an example from her own work: the network separation design was correct, the pilot clinic implementation was tested, but nobody has yet checked whether the other clinics were configured the same way. Operation is the hardest to prove.

### 11.2 Sampling accounts

Leila verifies access roles by sampling. She takes twenty staff accounts at random across the eight clinics and compares each account's role with the person's job and current employment. Eighteen match. One receptionist still has clinical access from an old role, and one dental nurse transferred to another clinic still has access to her previous clinic's patients. She reports both and asks the practice managers to correct them, and she notes that a sample estimates the error rate but cannot prove that all other accounts are correct.

### 11.3 Testing operation

For the deletion job that removes old reminder records, Leila checks the job's success log for the past three months and finds two missing days. She asks the IT contractor, who explains that the server was restarted for updates on those days and the job did not run. The next day's run caught up, so no data were kept too long. Leila records this as a minor operational gap and recommends that the job report its run time, so a missed day is visible immediately.

### 11.4 Honest reporting

Leila's verification report lists each control, the evidence, the result and any limits. She marks controls as verified, partly verified or not yet verified, and she avoids describing a sample as a full check. For network separation, she writes: verified in one clinic, not yet verified in seven. The data protection officer appreciates the clarity, because it shows exactly where further work is needed. Mr. Okafor notes that inflated verification reports create false confidence, which is worse than an honest gap. Gaps are listed first.

### Worked example

Leila separates design, implementation and operation, samples twenty accounts and finds two errors, checks deletion job history, and reports verified, partly verified and not yet verified controls.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Samples estimate rates; they do not certify every account.

### Exercises

- **EX041 — Three questions.** What three questions does verification answer? *Rubric:* 3 = designed correctly, implemented as designed, operating over time;; 2 = all;; 1 = one;; 0 = none.
- **EX042 — Sample result.** How many sampled accounts matched? *Rubric:* 3 = 18 of 20;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX043 — Missed runs.** Why did the deletion job miss two days? *Rubric:* 3 = server restarts for updates;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX044 — Separation status.** How did Leila report network separation? *Rubric:* 3 = verified in one clinic, not yet in seven;; 2 = partly correct;; 1 = verified;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) run a contained audit-log analysis; (2) interpret unusual access; (3) handle findings fairly.

### 12.1 The contained lab

Leila's first contained laboratory uses a synthetic copy of the practice-management audit log, prepared by the vendor's test tools and approved under her scope. The log records which staff account viewed which patient record and at which clinic. No real patients or staff appear. Mr. Okafor sets the rules: the lab runs on an isolated computer, results are shared only with the data protection officer and the instructor, and any names in conclusions refer to synthetic accounts only. Results never leave the isolated computer.

### 12.2 Lab results

The lab analyses 5,060 record views and finds 179 views, 3.5%, of patients registered at a clinic other than the staff member's own. Most staff have a handful of such views, which is expected because patients sometimes visit another clinic. One synthetic account, S07, has 53 outside views spread across several clinics, far more than anyone else; the next highest are S13 with 9 and S27 with 7. The pattern is unusual enough to justify a closer look, but it is not proof of misuse. Context decides what follows.

### 12.3 Interpreting the pattern

Leila lists possible explanations for S07: a role that covers several clinics, such as a regional nurse or a manager, a temporary assignment, a shared account, or curiosity about patients without a reason. She checks the synthetic staff list and finds S07 is a receptionist at one clinic. She does not conclude wrongdoing. Instead, she prepares a factual summary for the data protection officer, who in a real case would follow Marlow's investigation procedure, including speaking with the person and their manager.

### 12.4 Fairness and limits

Mr. Okafor emphasises that audit-log analysis affects staff, who also have privacy rights and a right to fair treatment. Staff must be told in their privacy notice that access is logged and reviewed. Thresholds must be applied consistently, and findings must be checked before any action. Leila notes the limits of her lab: the synthetic log has no information about legitimate cross-clinic tasks, so a real review would combine the log with rota and job information before drawing conclusions. Context protects staff from unfair suspicion.

### Lab — Record views outside the staff member's clinic

```python
"""Flag record views outside a staff member's own clinic in a synthetic audit log (stdlib only)."""
import random, collections
random.seed(5)
staff = {f"S{i:02d}": random.randint(1, 8) for i in range(40)}
log = []
for _ in range(5000):
    s = random.choice(list(staff)); home = staff[s]
    clinic = home if random.random() < 0.97 else random.randint(1, 8)
    log.append((s, clinic))
log += [("S07", c) for c in (2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6) * 5]
out = [(s, c) for s, c in log if c != staff[s]]
per = collections.Counter(s for s, _ in out)
print(f"record views {len(log)}; outside own clinic {len(out)} ({100*len(out)/len(log):.1f}%)")
top = per.most_common(3)
print("top staff by outside views:", ", ".join(f"{s} {n}" for s, n in top))
```

Run with `python3 lab_access.py`. Verified output:

```text
record views 5060; outside own clinic 179 (3.5%)
top staff by outside views: S07 53, S13 9, S27 7
```

### Worked example

Leila finds 179 of 5,060 views (3.5%) outside staff members' clinics, identifies S07 with 53 outside views, lists explanations, and prepares a factual summary without concluding misuse.

> **Synthetic case.** The audit log is synthetic.

### Errors and limits

Unusual access is a signal, not proof; follow a fair procedure.

### Exercises

- **EX045 — Outside views.** What share of views were outside the staff member's clinic? *Rubric:* 3 = 179 of 5,060, 3.5%;; 2 = approximate;; 1 = wrong;; 0 = none.
- **EX046 — Outlier.** Which account stood out and with how many outside views? *Rubric:* 3 = S07 with 53;; 2 = both;; 1 = one;; 0 = none.
- **EX047 — Explanations.** Name two possible explanations for S07's pattern. *Rubric:* 3 = regional role, temporary assignment, shared account, curiosity;; 2 = two;; 1 = one;; 0 = none.
- **EX048 — Staff rights.** What must staff be told about audit logs? *Rubric:* 3 = access is logged and reviewed;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-13"></a>

## Chapter 13 — Privacy and data protection: troubleshooting

### Learning outcomes

You will (1) diagnose a privacy fault methodically; (2) find the root cause; (3) prevent recurrence.

### 13.1 The symptom

A patient complains that she received a whitening offer by email although she never agreed to marketing. The data protection officer asks Leila to investigate technically. Leila starts by writing down exactly what is known: the patient's synthetic test equivalent, the date of the email, the campaign name and the patient's current marketing setting, which is off. She resists guessing at causes before collecting facts, because early guesses tend to focus attention on the wrong system and waste time. Facts first, theories later.

### 13.2 Following the data

Leila traces how the campaign list was built. The marketing platform receives a nightly export from the practice-management system of patients with marketing consent. She compares the export from the campaign date with the consent table and finds that the export query used the field for appointment reminders instead of the field for marketing consent. Every patient who accepted reminders, about four times as many people as had agreed to marketing, was included in the campaign list for that night. The affected list is reconstructed.

### 13.3 Root cause

The query had been edited two weeks earlier when the practice-management vendor renamed several fields during an upgrade. The person updating the query chose the wrong field because both had similar names: contact_ok and marketing_ok. There was no test to check that the export contained only consenting patients. Leila identifies three causes: confusing field names, no review of the query change and no automated check. She notes that blaming the individual would leave all three causes in place. The rename was undocumented.

### 13.4 Preventing recurrence

Leila adds an automated check that compares each export with the consent table before it is sent and stops the export if any patient lacks marketing consent. Query changes now require review by a second person. The vendor is asked to document field meanings clearly. Marlow suppresses marketing to all affected patients, sends an apology and records the event as a breach of its own rules, with the data protection officer deciding whether notification is required under Article 33. The check also runs for SMS lists.

### Worked example

Leila traces an unwanted marketing email to an export query that used the reminder field after a vendor renamed fields, adds an automated consent check and second-person review.

> **Synthetic case.** The fault is synthetic; GDPR Article 33 is real.

### Errors and limits

A quick fix to the query alone would not stop the next similar mistake.

### Exercises

- **EX049 — First step.** What did Leila do before guessing causes? *Rubric:* 3 = wrote down known facts;; 2 = mentions facts;; 1 = guessed;; 0 = none.
- **EX050 — Wrong field.** Which field did the export wrongly use? *Rubric:* 3 = the reminder field, contact_ok;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX051 — Three causes.** Name the three causes Leila found. *Rubric:* 3 = confusing names, no review, no automated check;; 2 = all;; 1 = one;; 0 = none.
- **EX052 — Automated check.** What does the new check do? *Rubric:* 3 = stops exports with non-consenting patients;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-14"></a>

## Chapter 14 — Privacy and data protection: automation

### Learning outcomes

You will (1) automate a retention rule; (2) handle exceptions; (3) monitor the automation.

### 14.1 The retention rule

Appointment reminder records, which store a phone number, appointment time and delivery status, are needed for about a year to resolve complaints and check delivery problems. Marlow's retention schedule sets 365 days. Clinical records follow longer professional rules and are not part of this job. Leila writes the rule precisely: delete reminder records whose appointment date is more than 365 days before the run date, except those linked to an open complaint. A precise rule is easier to automate and to explain to auditors.

### 14.2 The retention lab

The lab applies the rule to 1,200 synthetic reminder records. It finds 712, 59.3%, older than 365 days, and the oldest record is 900 days old. The result shows that reminders have never been deleted since the SMS service started, so most stored reminders are already beyond their purpose. Leila points out that every excess record contains a phone number linked to a dental appointment, which would be exposed if the reminder database were breached, so deletion directly reduces risk. Deleting the 712 expired records removes most of the phone numbers the database holds without affecting any current appointment.

### 14.3 Exceptions and safety

Before enabling deletion, Leila adds an exception flag for records linked to open complaints, set by the complaints team. She runs the job first in report-only mode, listing what would be deleted without deleting anything, and the operations director reviews the counts. Only then is deletion switched on. The job writes a summary of counts deleted and held to a log each night, without listing phone numbers. She explains that report-only runs are a simple way to catch mistakes in rules before data are lost.

### 14.4 Monitoring the job

The job sends a daily success message with the counts. If no message arrives, the IT contractor receives an alert. Each quarter, Leila checks that the oldest reminder record is younger than 366 days and that held records have a current complaint reference. This monitoring addresses the silent failure mode from Chapter 8. Mr. Okafor notes that automation enforces storage limitation reliably, but only if somebody notices when the automation stops, which is why the success message matters as much as the job. Both checks take minutes.

### Lab — Reminder records past retention

```python
"""Apply a retention rule to synthetic appointment-reminder records (stdlib only)."""
import random, datetime
random.seed(11)
today = datetime.date(2026, 10, 1)
recs = [(i, today - datetime.timedelta(days=random.randint(0, 900))) for i in range(1200)]
keep_days = 365
expired = [r for r in recs if (today - r[1]).days > keep_days]
oldest = max((today - d).days for _, d in recs)
print(f"reminder records {len(recs)}; older than {keep_days} days {len(expired)} ({100*len(expired)/len(recs):.1f}%)")
print(f"oldest record {oldest} days")
```

Run with `python3 lab_retention.py`. Verified output:

```text
reminder records 1200; older than 365 days 712 (59.3%)
oldest record 900 days
```

### Worked example

Leila finds 712 of 1,200 reminder records (59.3%) older than 365 days, adds a complaint exception, runs report-only first, then enables deletion with daily success messages and quarterly checks.

> **Synthetic case.** Records are synthetic.

### Errors and limits

Backups may still hold deleted records until they expire; document backup retention.

### Exercises

- **EX053 — Past retention.** How many reminder records were past retention? *Rubric:* 3 = 712 of 1,200, 59.3%;; 2 = approximate;; 1 = wrong;; 0 = none.
- **EX054 — Oldest record.** How old was the oldest record? *Rubric:* 3 = 900 days;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX055 — Report-only.** Why run in report-only mode first? *Rubric:* 3 = catch rule mistakes before data are lost;; 2 = mentions mistakes;; 1 = vague;; 0 = none.
- **EX056 — Exception.** Which records are held? *Rubric:* 3 = those linked to open complaints;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-15"></a>

## Chapter 15 — Privacy and data protection: integration and dependencies

### Learning outcomes

You will (1) assess a new integration; (2) map dependencies; (3) limit data shared.

### 15.1 The new integration

Marlow wants to connect its practice-management system to an online review service that emails patients after appointments asking for a rating. Leila assesses the integration technically before anything is connected. She asks what data the service needs, what it stores, where, for how long, who its subprocessors are and how patients can opt out. The vendor's default integration requests names, emails, appointment types and dentist names, and it publishes reviews with first names and appointment types by default. Leila records each answer in writing.

### 15.2 Dependencies

Leila maps dependencies: the review service depends on an email delivery provider and a cloud hosting company, both subprocessors. The integration depends on the practice-management system's interface, which changes when the vendor upgrades. A failure in any part could send emails to patients who opted out or publish details they did not expect. She notes that each dependency adds a party who may process patient data and a point where configuration can drift, so dependencies belong in the processing model. Both subprocessors are listed in the contract.

### 15.3 Limiting data

Leila recommends sending only first name, email and clinic, not appointment type or dentist, because a review request does not need them and appointment types such as implants or orthodontics reveal health information. Publication of appointment types is switched off. Patients who opted out of non-essential messages are excluded at the source by a filter in the export, not by the review service. The data protection officer asks for a legitimate interests assessment and a processor contract before the integration goes live.

### 15.4 Testing the integration

Leila tests with synthetic patients, including one who opted out and one with an implant appointment. The opted-out patient receives nothing. The implant patient's request contains no appointment type, and a test review is published without treatment details. She also checks that deleting a patient in the practice system leads to deletion in the review service within the agreed thirty days. The integration goes live in one clinic, and Leila schedules a repeat test after the next vendor upgrade. All three tests pass.

### Worked example

Leila assesses a review integration, maps subprocessors and interface dependencies, limits shared fields to first name, email and clinic, filters opt-outs at source and tests with synthetic patients.

> **Synthetic case.** The integration is synthetic; GDPR Article 28 contracts and legitimate interests assessments are real requirements.

### Errors and limits

Vendors change defaults in upgrades; retest after each one.

### Exercises

- **EX057 — Default fields.** What did the vendor's default integration request? *Rubric:* 3 = names, emails, appointment types, dentist names;; 2 = most;; 1 = one;; 0 = none.
- **EX058 — Appointment type.** Why remove appointment type? *Rubric:* 3 = it reveals health information and is unnecessary;; 2 = mentions health;; 1 = vague;; 0 = none.
- **EX059 — Opt-out filter.** Where are opted-out patients filtered? *Rubric:* 3 = at the source export;; 2 = partly correct;; 1 = at vendor;; 0 = none.
- **EX060 — Deletion test.** What deletion behaviour was tested? *Rubric:* 3 = deletion reaches the review service within thirty days;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write clear technical documentation for privacy controls; (2) include safety and rollback; (3) keep documentation current.

### 16.1 Why documentation matters

Marlow's IT contractor changes staff every few years, and practice managers change clinics. Leila finds that several privacy settings, such as the network zones and the reminder deletion job, are understood by only one person. If that person leaves, nobody knows why a setting exists or how to check it. Article 5(2) requires Marlow to demonstrate compliance, which is impossible if nobody can explain the controls. Documentation turns personal knowledge into organisational knowledge that survives staff changes and supports audits. One contractor holds most knowledge today.

### 16.2 Structure of a control document

Leila writes one short document per control with a fixed structure: purpose, the risk it addresses, where it is configured, how to check it works, what normal results look like, what to do when results are abnormal, who owns it and when it was last reviewed. The deletion job document, for example, shows where the job runs, the expected daily message and the quarterly check. She keeps documents under two pages and uses screenshots from the test environment, never from live patient screens.

### 16.3 Safety and rollback

Every change procedure includes safety steps. Before changing network rules, the contractor records the current configuration so it can be restored. Before enabling deletion, the job runs in report-only mode. Before changing roles, a test account confirms that daily tasks still work. Each procedure states how to roll back and when rollback is not possible, such as after data have been deleted. Leila explains that irreversible steps deserve extra checks, because a mistake cannot be undone once patient data are gone. Rollback steps are tested too.

### 16.4 Keeping it current

Documents drift from reality as systems change. Leila adds a review date to each document and links document reviews to change tickets: any ticket that touches a documented control must update the document before closing. Every six months, the data protection officer receives a list of documents past their review date. Mr. Okafor reviews her documents and asks her to remove two paragraphs of background theory, because operational staff need instructions and reasons, not lectures, when something goes wrong at a busy clinic.

### Worked example

Leila writes two-page control documents with purpose, risk, location, checks, normal results, abnormal actions, owner and review date, adds rollback steps and links updates to change tickets.

> **Synthetic case.** Documents are synthetic; GDPR Article 5(2) is real.

### Errors and limits

Documents written once and never reviewed become misleading.

### Exercises

- **EX061 — Single knowledge.** Why was single-person knowledge a risk? *Rubric:* 3 = nobody could explain controls if that person left;; 2 = mentions leaving;; 1 = vague;; 0 = none.
- **EX062 — Document fields.** Name four parts of a control document. *Rubric:* 3 = purpose, risk, location, checks, results, actions, owner, review date;; 2 = four;; 1 = two;; 0 = none.
- **EX063 — Irreversible steps.** Why do irreversible steps need extra checks? *Rubric:* 3 = mistakes cannot be undone after deletion;; 2 = mentions deletion;; 1 = vague;; 0 = none.
- **EX064 — Staying current.** How are documents kept current? *Rubric:* 3 = review dates and change tickets must update them;; 2 = mentions tickets;; 1 = vague;; 0 = none.

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) run an end-to-end test with a synthetic patient; (2) verify rights handling; (3) report gaps.

### 17.1 The synthetic patient

In the second contained laboratory, Leila creates a synthetic patient in Marlow's test environment who books online, receives a reminder, attends an appointment with an X-ray, pays, is referred to a specialist and leaves a review. The patient then exercises two rights: access under Article 15 and erasure of non-clinical data under Article 17 where it applies. The lab follows the patient's data through every system in the processing model, which tests whether the model and the controls hold together in practice. No real patient is involved.

### 17.2 Access request

Leila submits an access request as the synthetic patient. The response includes the practice-management record, the X-ray and the invoice, but misses the reminder history, the review service record and the referral letter in the shared mailbox. Leila notes that the missed items all sit in systems added or changed recently. She adds them to the access request checklist and recommends that any new integration, such as the review service, updates the checklist before going live, so access responses stay complete as systems change.

### 17.3 Erasure

The patient then asks to delete marketing and review data while clinical records are retained under professional rules. Leila checks each system: the marketing platform removes the patient, the review service removes the review after nine days, but the reminder database keeps the phone number until the yearly deletion rule removes it. She recommends that erasure requests trigger reminder deletion immediately. She also confirms that clinical records remain, and that the response letter explains clearly why they are kept. The letter lists each system.

### 17.4 Reporting gaps

Leila's lab report lists each system, the expected result, the observed result and a recommended fix. Three gaps are found: missing access items, slow reminder deletion and no record of the referral letter copy. All are assigned owners. The data protection officer asks for the lab to be repeated yearly. Mr. Okafor observes that a single synthetic patient exercised more of Marlow's privacy controls in one afternoon than months of document reviews, because the test followed real data paths end to end.

### Worked example

Leila follows a synthetic patient through booking, treatment, referral and review, finds access responses missing three sources, finds slow reminder deletion and reports owned fixes.

> **Synthetic case.** The patient is synthetic; GDPR Articles 15 and 17 are real.

### Errors and limits

Erasure does not apply to records Marlow must keep by law; explain this clearly.

### Exercises

- **EX065 — Missing items.** Which items were missing from the access response? *Rubric:* 3 = reminder history, review record, referral letter;; 2 = two;; 1 = one;; 0 = none.
- **EX066 — New systems.** Why were the missed items in recent systems? *Rubric:* 3 = checklist not updated when systems changed;; 2 = mentions checklist;; 1 = vague;; 0 = none.
- **EX067 — Reminder erasure.** What did Leila recommend for reminders on erasure? *Rubric:* 3 = delete immediately on request;; 2 = partly correct;; 1 = yearly;; 0 = none.
- **EX068 — Clinical records.** Why are clinical records kept after erasure requests? *Rubric:* 3 = professional rules require retention;; 2 = mentions rules;; 1 = vague;; 0 = none.

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) plan and deliver a supervised privacy project; (2) measure the result; (3) hand over to operations.

### 18.1 Choosing the project

For her final project, Leila chooses to roll out network separation to the seven clinics not yet covered, because her verification report showed it as the largest unverified control and the guest Wi-Fi exposure affected patient images. She writes a project plan with scope, schedule, tests, rollback steps and owners. The operations director approves the plan, and the IT contractor agrees to carry out configuration changes outside clinic hours while Leila prepares tests and documentation for each clinic. Each clinic gets a test sheet.

### 18.2 Delivery

The project proceeds one clinic per week. At each clinic, the contractor records the current configuration, applies the three-zone design and Leila tests from the guest network, the office zone and the clinical zone. At the fourth clinic, the intraoral cameras stop sending images because they used an address outside the clinical zone. The rollback plan restores service within twenty minutes, the camera addresses are corrected, and the change is reapplied the next week with an added test for camera image transfer.

### 18.3 Measuring the result

After eight weeks, all eight clinics have three zones, and guest Wi-Fi cannot reach any imaging server in Leila's tests. The verification report now marks network separation as verified in all clinics. She also measures side effects: no increase in support calls after the first week, and image transfer times unchanged. She presents results with the evidence log and notes the remaining risk that DICOM traffic inside the clinical zone is still unencrypted, which needs a future vendor project. Evidence accompanies each claim.

### 18.4 Handover and reflection

Leila hands the control document, test scripts and evidence to the IT contractor and data protection officer, who agree a yearly re-test. In her reflection, she notes that technical privacy work is mostly careful configuration, testing and documentation rather than dramatic discoveries. Mr. Okafor closes the course by pointing out that each technical change she made, from reminder content to network zones, reduced the chance that a patient's health information would reach someone who should not see it. Leila joins Marlow as a technician.

### Worked example

Leila rolls out network separation to seven more clinics, recovers from a camera failure with rollback, verifies all eight clinics and hands over documents and tests.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Projects that end without handover lose their controls; agree owners before closing.

### Exercises

- **EX069 — Project choice.** Why did Leila choose network separation? *Rubric:* 3 = largest unverified control with patient image exposure;; 2 = mentions exposure;; 1 = vague;; 0 = none.
- **EX070 — Camera failure.** What failed at the fourth clinic? *Rubric:* 3 = intraoral cameras could not send images;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX071 — Remaining risk.** What risk remains after the project? *Rubric:* 3 = unencrypted DICOM inside the clinical zone;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX072 — Handover.** Who receives the handover? *Rubric:* 3 = IT contractor and data protection officer;; 2 = both;; 1 = one;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Leila Haddad, Mr. Daniel Okafor, Riverside Technical College, Marlow Dental Group and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** They reveal information about a patient's health, which Article 4(15) covers.

**EX002.** A service is what users experience; components such as servers and databases deliver it.

**EX003.** Each copy must be protected, deleted on time and included in access requests.

**EX004.** Names, phone numbers and appointment times, which reveal they are dental patients.

**EX005.** Anyone on guest Wi-Fi could reach the imaging server's file shares.

**EX006.** As a risk to reduce through network separation while vendor changes are planned.

**EX007.** Clinical, office and guest zones.

**EX008.** She tested from guest Wi-Fi and found the imaging server unreachable.

**EX009.** They make it impossible to know who accessed which patient record.

**EX010.** Appointments, contact details and payment status, not treatment notes.

**EX011.** Four, down from twenty-three.

**EX012.** Each locum account has an end date from the rota and is disabled automatically.

**EX013.** A medical history field nested inside each appointment object.

**EX014.** Outputs are copied into tickets, chats and emails, creating disclosures.

**EX015.** It stops with a clear message rather than guessing.

**EX016.** Created with tempfile and removed when the script ends.

**EX017.** Live patient records and the vendor's cloud infrastructure.

**EX018.** It was outside her signed scope, so she asked for a synthetic reproduction.

**EX019.** Date, time, system, method, observation and supporting output.

**EX020.** That files have not changed; it does not keep them confidential.

**EX021.** By purpose, matching the Article 30 record of processing.

**EX022.** Article 9(2)(h), the provision of health care.

**EX023.** The courier carrying named prescriptions had no contract.

**EX024.** The SMS provider's support team outside the EU.

**EX025.** 95 of 400 lines (23.8%).

**EX026.** Logs now use booking references and only the last three phone digits.

**EX027.** They are copied to monitoring tools and shared with vendors in support cases.

**EX028.** Thirty days for detailed logs.

**EX029.** Wrong recipient, over-retention, over-access and silent control failure.

**EX030.** Jobs report success daily, and a missing report triggers an alert.

**EX031.** Only the clinic name and appointment time.

**EX032.** It was a personal data breach, which must be documented even when low risk.

**EX033.** Where does this tool send the data it reads?

**EX034.** The question, data source, steps, expected output and interpretation.

**EX035.** So synthetic data, and therefore results, are identical across runs.

**EX036.** They read personal data, so they need the same protections as other systems.

**EX037.** Three of seven.

**EX038.** It was set automatically, before any language was chosen.

**EX039.** It was removed because Marlow had no need for it.

**EX040.** Website changes and plugins often bring back tags that load before consent.

**EX041.** Is it designed correctly, implemented as designed and operating consistently?

**EX042.** Eighteen of twenty.

**EX043.** The server was restarted for updates and the job did not run.

**EX044.** Verified in one clinic, not yet verified in the other seven.

**EX045.** 179 of 5,060 (3.5%).

**EX046.** S07, with 53 outside views.

**EX047.** A temporary assignment or a shared account (also a regional role or curiosity).

**EX048.** That their access to records is logged and reviewed.

**EX049.** She recorded the known facts first.

**EX050.** The reminder field (contact_ok) instead of marketing_ok.

**EX051.** Confusing field names, no review of the change and no automated check.

**EX052.** It stops any export that includes a patient without marketing consent.

**EX053.** 712 of 1,200 (59.3%).

**EX054.** 900 days.

**EX055.** To check what would be deleted before deleting anything.

**EX056.** Records linked to an open complaint.

**EX057.** Names, emails, appointment types and dentist names.

**EX058.** It reveals health information and a review request does not need it.

**EX059.** In Marlow's export, before data reach the vendor.

**EX060.** That deleting a patient removes them from the review service within thirty days.

**EX061.** If that person left, nobody would know why settings exist or how to check them.

**EX062.** Purpose, risk, where configured and owner (plus checks, results, actions and review date).

**EX063.** Once patient data are deleted, a mistake cannot be undone.

**EX064.** Each has a review date, and change tickets must update affected documents.

**EX065.** Reminder history, the review service record and the referral letter.

**EX066.** The checklist had not been updated when systems were added or changed.

**EX067.** Erasure requests should trigger immediate reminder deletion.

**EX068.** Professional rules require Marlow to keep them, which the letter explains.

**EX069.** It was the largest unverified control and exposed patient images to guest Wi-Fi.

**EX070.** Intraoral cameras stopped sending images because of their addresses.

**EX071.** DICOM traffic inside the clinical zone is still unencrypted.

**EX072.** The IT contractor and the data protection officer.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
- European Union. (2002). Directive 2002/58/EC of the European Parliament and of the Council of 12 July 2002 concerning the processing of personal data and the protection of privacy in the electronic communications sector (ePrivacy Directive), as amended by Directive 2009/136/EC. *Official Journal of the European Communities, L 201*, 37–47 (CELEX 32002L0058; ELI dir/2002/58/oj, confirmed via the Publications Office record). <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0058>
