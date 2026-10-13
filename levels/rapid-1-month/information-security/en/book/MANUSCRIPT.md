# Information Security: Rapid Course

- Language: English (`en`); course 002, Rapid course (1 month).
- Editorial state: **published**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; one offline lab uses only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: managers and staff of very small organisations who need to fix the most common security weaknesses in a month.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the lab counts synthetic shared files open to anyone with the link, by folder. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The four chapters follow one practice manager from what the clinic holds, through accounts, devices and sharing, and email fraud and people, to backups, incidents and a monthly routine. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Sofia Lindqvist** | Practice manager and learner | Invented |
| **Mr. Tomasz Nowak** | Trainer | Invented |
| **Eastgate Training Centre** | Fictional training centre | Invented |
| **Hollybank Veterinary Practice** | Fictional clinic, one site, eighteen staff | Invented |

### Core sources

ISO/IEC 27000:2026. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — A month to get the basics right

<!-- cyberabc:lesson-figures:start ch-01 -->
### Lesson map

Lesson 01 published. Map, example, EX001.

```mermaid
flowchart TD
  N0["Learning outcomes"]
  N1["1.1 The learner"]
  N2["1.2 The practice"]
  N3["1.3 What the clinic holds"]
  N4["1.4 What cannot be lost"]
  N5["1.5 Ground rules"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5
  N5 --> EX["Worked example"]
  EX --> Q["Exercise EX001"]
```

### Logical drawing

```mermaid
flowchart LR
  N0["Learning outcomes"]
  N1["1.1 The learner"]
  N2["1.2 The practice"]
  N3["1.3 What the clinic holds"]
  N4["1.4 What cannot be lost"]
  N5["1.5 Ground rules"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> Q["EX001"]
```

```text
[Learning outcomes]
    |
    v
[1.1 The learner]
    |
    v
[1.2 The practice]
    |
    v
[1.3 What the clinic holds]
    |
    v
[1.4 What cannot be lost]
    |
    v
[1.5 Ground rules]
    |
    v
[Worked example] --> [Exercise EX001]
```
<!-- cyberabc:lesson-figures:end ch-01 -->


### Learning outcomes

You will (1) describe what the one-month rapid course covers; (2) meet the running case; (3) list what a small practice holds and what it cannot lose.

### 1.1 The learner

Sofia Lindqvist is the practice manager at a small veterinary clinic. After a neighbouring business lost a week of work to ransomware, the owner asks her to make sure the clinic is not next. Sofia enrols on a one-month rapid course in information security at the fictional Eastgate Training Centre, with four weekly sessions and short tasks in between. Her trainer, Mr. Tomasz Nowak, has spent years helping small businesses recover from incidents. He tells the group that a month is enough to fix the most common weaknesses, though not to become an expert.

### 1.2 The practice

Sofia works at the fictional Hollybank Veterinary Practice, a single site with two vets, four nurses, three receptionists and a small office team, eighteen staff in all. The clinic uses a cloud practice management system for appointments, pet records and payments, a cloud email and file service, and nine computers plus two tablets. Client records hold names, addresses, phone numbers and payment history. An outside technician visits when something breaks. The owner, Dr. Rachel Moss, wants the clinic protected without slowing down the reception desk on busy mornings, when queues already build up.

### 1.3 What the clinic holds

In the first task, Sofia lists the information the clinic holds and where it lives. Pet and client records, appointments and payments are in the practice management system. Staff contracts and rotas are in shared folders. Supplier invoices and bank details arrive by email. Laboratory results come by email from an outside laboratory. Marketing photos for the clinic's social media pages are also in shared folders. Mr. Nowak asks her to mark each item by how much harm a leak, a wrong change or a loss would cause, using high, medium or low.

### 1.4 What cannot be lost

Sofia agrees three priorities with Dr. Moss. The clinic cannot lose access to the practice management system during opening hours, because appointments and treatment notes depend on it. It cannot let client contact and payment details leak, because clients trust the clinic with them and the law requires them to be protected. And it cannot pay a fraudulent supplier invoice, because margins are thin. Mr. Nowak explains that ISO/IEC 27000:2026 describes information security as protecting confidentiality, integrity and availability, and that Sofia's three priorities map neatly onto those three goals.

### 1.5 Ground rules

Mr. Nowak sets three rules for the month. Get Dr. Moss's written agreement before changing any setting. Never put real client details into coursework or shared examples. Write down each change with the date and the reason, so the technician and Dr. Moss can see what was done. Sofia creates a simple change log in a shared document only she and Dr. Moss can open. Mr. Nowak adds that small businesses are often harmed by well-meant changes that nobody recorded, because problems later cannot be traced back to their cause.

### Worked example

Sofia joins the rapid course, lists what Hollybank's eighteen-person clinic holds, agrees three priorities tied to confidentiality, integrity and availability, and starts a change log.

> **Synthetic case.** Eastgate, Hollybank and all people are synthetic.

### Errors and limits

Unrecorded changes make later problems hard to trace.

### Exercises

- **EX001 — Course length.** How long is Sofia's course? *Rubric:* 3 = one month, four sessions;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX002 — Trigger.** What prompted the owner to act? *Rubric:* 3 = a neighbour's ransomware;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX003 — Staff count.** How many staff does Hollybank have? *Rubric:* 3 = eighteen;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX004 — Core system.** Where are pet records and appointments kept? *Rubric:* 3 = cloud practice management system;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX005 — Device count.** How many computers and tablets does the clinic use? *Rubric:* 3 = nine computers, two tablets;; 2 = both;; 1 = one;; 0 = none.
- **EX006 — Owner's condition.** What did Dr. Moss ask for? *Rubric:* 3 = protection without slowing reception;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX007 — Lab results.** How do laboratory results arrive? *Rubric:* 3 = by email;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX008 — Harm marking.** How does Sofia mark each information item? *Rubric:* 3 = high, medium or low harm;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX009 — Availability priority.** Which priority is about availability? *Rubric:* 3 = practice system during opening hours;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX010 — Integrity priority.** Which priority is about integrity? *Rubric:* 3 = not paying a fraudulent invoice;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX011 — Standard named.** Which standard describes the three goals? *Rubric:* 3 = ISO/IEC 27000:2026;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX012 — Change log access.** Who can open the change log? *Rubric:* 3 = Sofia and Dr. Moss;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX013 — Why log changes.** Why record each change? *Rubric:* 3 = so problems can be traced;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — lesson 01 (chapter 01 of 04)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Accounts, devices and sharing

<!-- cyberabc:lesson-figures:start ch-02 -->
### Lesson map

Lesson 02 published. Map, example, EX014.

```mermaid
flowchart TD
  N0["Learning outcomes"]
  N1["2.1 Own accounts"]
  N2["2.2 Second factor"]
  N3["2.3 Devices"]
  N4["Lab — Shared files open to anyone with the link, by"]
  N5["2.4 Over-shared files"]
  N6["2.5 Closing the gaps"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6
  N6 --> EX["Worked example"]
  EX --> Q["Exercise EX014"]
```

### Logical drawing

```mermaid
flowchart LR
  N0["Learning outcomes"]
  N1["2.1 Own accounts"]
  N2["2.2 Second factor"]
  N3["2.3 Devices"]
  N4["Lab — Shared files open to anyone with the link, by"]
  N5["2.4 Over-shared files"]
  N6["2.5 Closing the gaps"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> N6 --> Q["EX014"]
```

```text
[Learning outcomes]
    |
    v
[2.1 Own accounts]
    |
    v
[2.2 Second factor]
    |
    v
[2.3 Devices]
    |
    v
[Lab — Shared files open to anyone with the link, by]
    |
    v
[2.4 Over-shared files]
    |
    v
[2.5 Closing the gaps]
    |
    v
[Worked example] --> [Exercise EX014]
```
<!-- cyberabc:lesson-figures:end ch-02 -->


### Learning outcomes

You will (1) give each person their own account with a second factor; (2) secure the clinic's devices; (3) find and close over-shared files with a short script.

### 2.1 Own accounts

Sofia finds that reception staff share one login to the practice management system, written on a note under the keyboard. Mr. Nowak explains that shared logins hide who did what, and the note means anyone at the desk could sign in. The system supports personal accounts with quick switching between users, so Sofia sets up one account per person and removes the note. Reception staff worry about delays, so she times the switch during a busy morning and shows that it takes a few seconds. Dr. Moss approves the change after seeing the timing.

### 2.2 Second factor

Mr. Nowak explains that most account takeovers start with a stolen or guessed password, and that a second factor, such as an app on a phone, stops most of them. Sofia turns on a second factor for email and the practice system, starting with Dr. Moss and the office team, who handle payments, then everyone else over two weeks. Two nurses do not want work apps on their own phones, so the clinic buys two small security keys for them. Sofia records each person's method in the change log so lost devices can be handled quickly.

### 2.3 Devices

Sofia checks the nine computers and two tablets with the technician. Three computers have updates switched off because an old label printer stopped working after an update last year. The technician installs a newer printer driver and switches updates back on. All devices now lock after five minutes, and staff accounts can no longer install software. The tablets used in consulting rooms get a passcode and remote wipe. Mr. Nowak notes that switching updates off to solve one problem is common, and that the fix is to solve the underlying problem instead of leaving devices exposed.

### Lab — Shared files open to anyone with the link, by folder, in a synthetic file store

```python
"""Find synthetic shared files open to anyone with the link, by folder (stdlib only)."""
import random
from collections import Counter
random.seed(2)
files = []
for folder, n, p in [("clients", 140, 0.04), ("finance", 60, 0.05), ("marketing", 80, 0.30), ("rotas", 20, 0.5)]:
    for i in range(n):
        files.append((folder, random.random() < p))
total = Counter(f for f, _ in files)
open_ = Counter(f for f, o in files if o)
for f in total:
    print(f"{f}: {open_[f]} of {total[f]} open to anyone with the link")
print(f"all files: {sum(open_.values())} of {len(files)}")
```

Run with `python3 lab_sharing.py`. Verified output:

```text
clients: 8 of 140 open to anyone with the link
finance: 4 of 60 open to anyone with the link
marketing: 25 of 80 open to anyone with the link
rotas: 10 of 20 open to anyone with the link
all files: 47 of 300
```

### 2.4 Over-shared files

With Dr. Moss's permission, the technician exports a list of shared files and whether each is open to anyone with the link. Sofia runs the script on a synthetic copy with the same folder structure. It finds 47 of 300 files open to anyone with the link. Most are marketing photos, 25 of 80, and staff rotas, 10 of 20. But 8 of 140 files in the client folder and 4 of 60 in the finance folder are also open. Those twelve matter most, because anyone who obtains a link could read client or bank information.

### 2.5 Closing the gaps

Sofia changes the twelve client and finance files to clinic-only sharing first. She then asks staff why rotas were shared openly and learns that part-time staff check them from home on personal phones. She moves the rota to the practice system, where staff can see it after signing in. Marketing photos can stay public because they are already posted online. Sofia asks the technician to set the default for new shares to clinic-only, and adds a monthly reminder to rerun the check. Mr. Nowak praises her for fixing the reason behind the rota sharing, not just the setting.

### Worked example

Sofia replaces a shared reception login, turns on second factors with security keys for two nurses, re-enables updates on three computers and finds 47 of 300 synthetic files open to anyone, including 12 client and finance files.

> **Synthetic case.** Accounts, devices and files are synthetic.

### Errors and limits

Switching off updates to fix a printer leaves devices exposed long after the printer is forgotten.

### Exercises

- **EX014 — Shared login.** What did reception use to sign in? *Rubric:* 3 = one shared login on a note;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX015 — Switch time.** How long does switching users take? *Rubric:* 3 = a few seconds;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX016 — First MFA group.** Who got a second factor first? *Rubric:* 3 = Dr. Moss and the office team;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX017 — Security keys.** Why were security keys bought? *Rubric:* 3 = two nurses declined apps on personal phones;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX018 — Updates off.** Why were updates off on three computers? *Rubric:* 3 = an old label printer broke after an update;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX019 — Update fix.** How was the printer problem fixed? *Rubric:* 3 = a newer printer driver;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX020 — Tablet controls.** What did the consulting room tablets get? *Rubric:* 3 = passcode and remote wipe;; 2 = both;; 1 = one;; 0 = none.
- **EX021 — Open total.** How many files were open to anyone with the link? *Rubric:* 3 = 47 of 300;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX022 — Marketing count.** How many marketing files were open? *Rubric:* 3 = 25 of 80;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX023 — Sensitive open.** How many client and finance files were open? *Rubric:* 3 = 12 (8 client, 4 finance);; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX024 — Rota cause.** Why were rotas shared openly? *Rubric:* 3 = part-time staff checked them from home;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX025 — Rota fix.** Where did the rota move? *Rubric:* 3 = into the practice system;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX026 — Default setting.** What default did the technician set? *Rubric:* 3 = clinic-only sharing for new shares;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — lesson 02 (chapter 02 of 04)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Email, fraud and people

<!-- cyberabc:lesson-figures:start ch-03 -->
### Lesson map

Lesson 03 published. Map, example, EX027.

```mermaid
flowchart TD
  N0["Learning outcomes"]
  N1["3.1 Phishing signs"]
  N2["3.2 Invoice fraud"]
  N3["3.3 The rule in action"]
  N4["3.4 Short training"]
  N5["3.5 Reporting without blame"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5
  N5 --> EX["Worked example"]
  EX --> Q["Exercise EX027"]
```

### Logical drawing

```mermaid
flowchart LR
  N0["Learning outcomes"]
  N1["3.1 Phishing signs"]
  N2["3.2 Invoice fraud"]
  N3["3.3 The rule in action"]
  N4["3.4 Short training"]
  N5["3.5 Reporting without blame"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> Q["EX027"]
```

```text
[Learning outcomes]
    |
    v
[3.1 Phishing signs]
    |
    v
[3.2 Invoice fraud]
    |
    v
[3.3 The rule in action]
    |
    v
[3.4 Short training]
    |
    v
[3.5 Reporting without blame]
    |
    v
[Worked example] --> [Exercise EX027]
```
<!-- cyberabc:lesson-figures:end ch-03 -->


### Learning outcomes

You will (1) recognise phishing and invoice fraud; (2) set a payment verification rule; (3) build a short, blame-free reporting habit.

### 3.1 Phishing signs

Mr. Nowak shows the group common signs of phishing: a sender address that does not match the name shown, unexpected urgency, a link whose real destination differs from its text, and requests for passwords or payments. Sofia picks three recent emails from the clinic's inbox that staff had asked about and checks them with the reception team. One claimed to be from a parcel company and linked to a lookalike address. Mr. Nowak stresses that no list catches everything, so the habit of pausing and checking matters more than memorising signs.

### 3.2 Invoice fraud

Small businesses are often targeted with messages that claim a supplier has changed bank details. Hollybank pays a drug wholesaler, a laboratory and several equipment suppliers. Sofia agrees a rule with Dr. Moss: any request to change bank details is checked by phoning the supplier on a number already held, never one in the message, and a second person approves the change. Mr. Nowak explains that this one rule stops most invoice fraud, whatever the email looks like, because the criminal cannot answer the phone at the real supplier's office.

### 3.3 The rule in action

Two weeks later, the office receives an email apparently from the equipment supplier, with a correct invoice number and a request to pay into a new account before the end of the day. The office assistant follows the rule and phones the supplier on the number in the clinic's records. The supplier has sent no such message and says its own mailbox may have been compromised. The clinic pays nothing to the new account. Sofia records the attempt, forwards the email to the supplier and thanks the assistant in front of the team.

### 3.4 Short training

Sofia runs a ten-minute session at the weekly staff meeting, using two synthetic examples that look like clinic emails, one about a parcel and one about a pet insurance claim. Staff find the signs together and agree what to do. Mr. Nowak advises against long annual training for a clinic this size; short, regular, relevant sessions are remembered better. Sofia plans one short topic a month, chosen from questions staff have asked, and keeps a list of the topics covered so new staff can catch up during their first week.

### 3.5 Reporting without blame

Sofia sets up one way to report anything suspicious: forward it to her or tell her at the desk. Dr. Moss tells staff that nobody will be criticised for clicking a link or making a mistake, as long as they report it quickly, because early reports make problems smaller. Within a week, a receptionist reports that she typed her password into a page that looked odd. Sofia resets the password the same morning and checks the account, finding no misuse. Mr. Nowak notes that the second factor would also have blocked a sign-in with that password.

### Worked example

Sofia teaches phishing signs, sets a phone-back rule that stops a synthetic invoice fraud attempt, runs ten-minute monthly sessions and gets a quick blame-free report of a typed password.

> **Synthetic case.** Emails and suppliers are synthetic.

### Errors and limits

Calling the number in a suspicious message reaches the criminal, not the supplier.

### Exercises

- **EX027 — Four signs.** Name two phishing signs. *Rubric:* 3 = mismatched sender, urgency, odd link, password or payment request;; 2 = two;; 1 = one;; 0 = none.
- **EX028 — Parcel email.** What did the parcel email link to? *Rubric:* 3 = a lookalike address;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX029 — Key habit.** What matters more than memorising signs? *Rubric:* 3 = pausing and checking;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX030 — Bank rule.** What is the bank detail change rule? *Rubric:* 3 = phone a known number, second approval;; 2 = both;; 1 = one;; 0 = none.
- **EX031 — Why it works.** Why does the phone-back rule stop fraud? *Rubric:* 3 = the criminal cannot answer the real supplier's phone;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX032 — Fake invoice.** Which supplier did the fake email impersonate? *Rubric:* 3 = the equipment supplier;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX033 — Outcome.** How much did the clinic pay to the new account? *Rubric:* 3 = nothing; the request was refused after the call;; 2 = nothing, without saying why;; 1 = wrong;; 0 = no answer.
- **EX034 — Training length.** How long is each staff session? *Rubric:* 3 = ten minutes;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX035 — Topic source.** How are monthly topics chosen? *Rubric:* 3 = from staff questions;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX036 — Report route.** How do staff report something suspicious? *Rubric:* 3 = forward to Sofia or tell her;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX037 — Owner's promise.** What did Dr. Moss promise staff? *Rubric:* 3 = no criticism for quick reports;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX038 — Typed password.** What did Sofia do about the typed password? *Rubric:* 3 = reset it and checked the account;; 2 = both;; 1 = one;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — lesson 03 (chapter 03 of 04)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Backups, incidents and the plan ahead

<!-- cyberabc:lesson-figures:start ch-04 -->
### Lesson map

Lesson 04 published. Map, example, EX039.

```mermaid
flowchart TD
  N0["Learning outcomes"]
  N1["4.1 Backups"]
  N2["4.2 Testing a restore"]
  N3["4.3 An incident card"]
  N4["4.4 A practice drill"]
  N5["4.5 The plan ahead"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5
  N5 --> EX["Worked example"]
  EX --> Q["Exercise EX039"]
```

### Logical drawing

```mermaid
flowchart LR
  N0["Learning outcomes"]
  N1["4.1 Backups"]
  N2["4.2 Testing a restore"]
  N3["4.3 An incident card"]
  N4["4.4 A practice drill"]
  N5["4.5 The plan ahead"]
  N0 --> N1 --> N2 --> N3 --> N4 --> N5 --> Q["EX039"]
```

```text
[Learning outcomes]
    |
    v
[4.1 Backups]
    |
    v
[4.2 Testing a restore]
    |
    v
[4.3 An incident card]
    |
    v
[4.4 A practice drill]
    |
    v
[4.5 The plan ahead]
    |
    v
[Worked example] --> [Exercise EX039]
```
<!-- cyberabc:lesson-figures:end ch-04 -->


### Learning outcomes

You will (1) confirm the clinic can restore its data; (2) write a one-page incident card; (3) set a simple plan for the months after the course.

### 4.1 Backups

Sofia asks the practice system provider how its data is backed up and how quickly it could be restored. The provider keeps daily backups for thirty days and can restore within a day. The clinic's email and shared files have no separate backup, so a deletion noticed late would be lost. Dr. Moss approves a low-cost backup service for email and files. Mr. Nowak explains that a provider keeping its service running does not mean your own deleted or encrypted files can be recovered, which surprises several people in the group.

### 4.2 Testing a restore

Sofia asks the technician to restore one folder and one mailbox from the new backup into a test area. The folder restores in minutes. The mailbox restore fails on the first attempt because the backup had not finished its first full copy. On the second attempt a week later it works. Sofia records both results in the change log. Mr. Nowak praises her for testing, because many businesses discover backup problems only when they need the backup, at the worst possible moment, and with clients waiting at the desk.

### 4.3 An incident card

Sofia writes a one-page incident card and pins it in the office. It lists what counts as an incident, such as a lost tablet, a suspicious sign-in alert, a ransom message or client details sent to the wrong person; who to call first, which is Sofia, then Dr. Moss, then the technician; the first steps, such as disconnecting an affected computer from the network; and the phone numbers of the practice system provider and the data protection adviser. She also keeps a paper appointment sheet for the day in case the system is unavailable.

### 4.4 A practice drill

Sofia runs a twenty-minute drill with Dr. Moss and two receptionists. The scenario: on a Monday morning, the practice system is unavailable for four hours. The team uses the paper sheet, phones clients with urgent appointments from a printed list and records treatments on paper for entry later. They discover the printed list is three weeks old and missing new clients. Sofia sets a weekly reminder to print a fresh list and lock it in the office. Mr. Nowak notes that drills find small gaps that are easy to fix beforehand and painful to discover during a real outage.

### 4.5 The plan ahead

At the last session, Sofia lists what changed in the month: personal accounts and second factors for everyone, updates back on, twelve sensitive files no longer open to anyone, a phone-back rule that stopped one fraud attempt, a tested backup and an incident card. She sets a short monthly routine: rerun the sharing check, review leavers' accounts, give one ten-minute session and test one restore. Mr. Nowak recommends the data governance rapid course next, since the clinic's retention of old client records is the next question Dr. Moss wants answered.

### Worked example

Sofia adds a backup for email and files, tests a restore that fails once then succeeds, pins a one-page incident card, finds a stale client list in a drill and sets a four-item monthly routine.

> **Synthetic case.** Providers, times and drills are synthetic.

### Errors and limits

Assuming a cloud provider will recover your deleted or encrypted files can leave the business with no copy.

### Exercises

- **EX039 — Provider backups.** How long does the practice system provider keep backups? *Rubric:* 3 = thirty days;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX040 — Missing backup.** What had no separate backup? *Rubric:* 3 = email and shared files;; 2 = both;; 1 = one;; 0 = none.
- **EX041 — First failure.** Why did the first mailbox restore fail? *Rubric:* 3 = first full copy not finished;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX042 — First call.** Who is called first in an incident? *Rubric:* 3 = Sofia;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX043 — First step.** What is a first step for an affected computer? *Rubric:* 3 = disconnect it from the network;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX044 — Paper fallback.** What paper fallback does Sofia keep? *Rubric:* 3 = the day's appointment sheet;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX045 — Drill length.** How long was the drill? *Rubric:* 3 = twenty minutes;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX046 — Drill gap.** What gap did the drill find? *Rubric:* 3 = printed client list was three weeks old;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX047 — Gap fix.** How was the drill gap fixed? *Rubric:* 3 = weekly fresh printout, locked away;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX048 — Sensitive files.** How many sensitive files were closed off? *Rubric:* 3 = twelve;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX049 — Monthly routine.** Name two items in the monthly routine. *Rubric:* 3 = sharing check, leavers, session, restore test;; 2 = two;; 1 = one;; 0 = none.
- **EX050 — Next step.** What course comes next and why? *Rubric:* 3 = data governance rapid, retention of old records;; 2 = both;; 1 = one;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — lesson 04 (chapter 04 of 04)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Sofia Lindqvist, Mr. Tomasz Nowak, Eastgate Training Centre, Hollybank Veterinary Practice and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** One month, with four weekly sessions.

**EX002.** A neighbouring business lost a week of work to ransomware.

**EX003.** Eighteen staff.

**EX004.** In the cloud practice management system.

**EX005.** Nine computers and two tablets.

**EX006.** Protection that does not slow the reception desk.

**EX007.** By email from an outside laboratory.

**EX008.** By the harm a leak, change or loss would cause: high, medium or low.

**EX009.** Keeping the practice management system available during opening hours.

**EX010.** Not paying a fraudulent supplier invoice.

**EX011.** ISO/IEC 27000:2026.

**EX012.** Only Sofia and Dr. Moss.

**EX013.** So later problems can be traced to their cause.

**EX014.** One shared login written on a note under the keyboard.

**EX015.** A few seconds, timed during a busy morning.

**EX016.** Dr. Moss and the office team, who handle payments.

**EX017.** Two nurses did not want work apps on personal phones.

**EX018.** An update had broken an old label printer.

**EX019.** The technician installed a newer printer driver.

**EX020.** A passcode and remote wipe.

**EX021.** 47 of 300 synthetic files.

**EX022.** 25 of 80 marketing files.

**EX023.** Twelve: 8 client files and 4 finance files.

**EX024.** Part-time staff checked them from home on personal phones.

**EX025.** Into the practice system, behind sign-in.

**EX026.** New shares default to clinic-only.

**EX027.** A sender address that does not match and unexpected urgency.

**EX028.** A lookalike address.

**EX029.** The habit of pausing and checking.

**EX030.** Phone the supplier on a held number and get a second approval.

**EX031.** The criminal cannot answer the real supplier's phone.

**EX032.** The equipment supplier.

**EX033.** Nothing; the request was refused after the call.

**EX034.** Ten minutes at the weekly staff meeting.

**EX035.** From questions staff have asked.

**EX036.** Forward it to Sofia or tell her at the desk.

**EX037.** Nobody is criticised for a mistake reported quickly.

**EX038.** Reset the password that morning and checked the account for misuse.

**EX039.** Daily backups kept for thirty days.

**EX040.** The clinic's email and shared files.

**EX041.** The backup had not finished its first full copy.

**EX042.** Sofia, then Dr. Moss, then the technician.

**EX043.** Disconnect it from the network.

**EX044.** A paper appointment sheet for the day.

**EX045.** Twenty minutes.

**EX046.** The printed client list was three weeks old.

**EX047.** A weekly reminder to print a fresh list and lock it away.

**EX048.** Twelve client and finance files.

**EX049.** Rerun the sharing check and test one restore.

**EX050.** The data governance rapid course, to address retention of old client records.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and ISO/IEC editions were checked against iso.org on the same day. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
