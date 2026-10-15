# Information Security: Professional Course

- Language: English (`en`); course 025, Professional course (6 months).
- Editorial state: **published**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working professionals taking on information security alongside another role in a small or mid-sized firm.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs measure multi-factor sign-in coverage by account type in a synthetic directory and rank a synthetic risk register by likelihood times impact. Standards are cited by edition and paraphrased; legal points are general and need professional advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one office manager from understanding the firm and its risks through accounts, devices, payment fraud, suppliers and people to incidents, continuity, policy and reporting to leadership. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Daniel Reyes** | Office manager and learner | Invented |
| **Ms. Helen Ashby** | Tutor | Invented |
| **Kingsmere Professional Institute** | Fictional institute | Invented |
| **Corbridge Accountancy Partners** | Fictional firm, eight partners, about sixty staff, two thousand clients | Invented |

### Core sources

ISO/IEC 27000:2026; ISO/IEC 27001:2022; ISO/IEC 27002:2022; NIST SP 800-30 Rev. 1. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — A working professional returns to study

### Learning outcomes

You will (1) describe what the six-month professional course covers; (2) meet the running case; (3) agree the ground rules for working with a real employer.

### 1.1 The learner

Daniel Reyes is an office manager who has been asked to take on information security at his employer alongside his existing job. He enrols on a six-month professional course at the fictional Kingsmere Professional Institute, studying two evenings a week. His tutor, Ms. Helen Ashby, spent fifteen years running security for mid-sized firms before teaching. She tells the group that most of them will be the only person in their organisation with security in their title, so the course focuses on judgement, priorities and clear communication rather than deep technical skill.

### 1.2 The employer

Daniel works at the fictional Corbridge Accountancy Partners, a firm of eight partners and about sixty staff in two offices. The firm holds tax returns, payroll files, bank statements and identity documents for around two thousand clients. Email, files and accounting software all run in cloud services, with a small file server kept in the main office for older records. An outside support company handles devices. Daniel reports to the managing partner, Mrs. Joanna Pike, who wants a plain answer to one question: are we doing the right things, and what should we do next?

### 1.3 How the course runs

The twelve chapters move from understanding the firm and its risks, through accounts, devices, email, suppliers and people, to incidents, continuity, policy, measurement and reporting to leadership. Each chapter ends with a task Daniel applies at Corbridge, and Ms. Ashby reviews the results in a short weekly call. Two labs use small Python scripts on synthetic data: one measures multi-factor sign-in coverage and one ranks a risk register. Daniel has never written code, so Ms. Ashby explains that he only needs to read and run the scripts, not write them from scratch.

### 1.4 Ground rules

Ms. Ashby sets three rules. First, get written agreement from Mrs. Pike before checking any system, even one Daniel already uses daily. Second, never copy real client data into coursework; describe it or use synthetic examples. Third, record every finding with the date, evidence and the person told, so a colleague could follow the trail later. Daniel writes a one-page scope note listing what he may look at, and Mrs. Pike signs it. Ms. Ashby explains that the note protects Daniel if anyone later asks why he was looking at settings outside his usual job.

### Worked example

Daniel joins the professional course, meets Corbridge's sixty staff and two thousand clients, and gets a signed scope note before checking anything.

> **Synthetic case.** Kingsmere, Corbridge and all people are synthetic.

### Errors and limits

Checking systems without written agreement can damage trust even when the intention is good.

### Exercises

- **EX001 — Course length.** How long is Daniel's course? *Rubric:* 3 = six months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX002 — Client records.** Roughly how many clients does Corbridge hold records for? *Rubric:* 3 = about two thousand;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX003 — Leadership question.** What does Mrs. Pike want answered? *Rubric:* 3 = are we doing the right things, what next;; 2 = both parts;; 1 = one part;; 0 = none.
- **EX004 — Scope note.** Why does Daniel get a signed scope note? *Rubric:* 3 = written agreement before checking;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX005 — Coding needed.** Does Daniel need to write the lab scripts? *Rubric:* 3 = no, read and run them;; 2 = partly correct;; 1 = wrong;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue studying — lesson 01 (chapter 01 of 12)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Understanding the firm

### Learning outcomes

You will (1) map the information a professional firm holds; (2) identify who depends on it; (3) state what the firm cannot afford to lose.

### 2.1 Information inventory

Daniel spends his first week listing what Corbridge holds. Client identity documents and bank statements arrive by email and upload portal. Tax returns and payroll calculations live in the accounting software. Engagement letters and working papers sit in shared cloud folders. Staff records live in a payroll service. Older client files, some over ten years old, remain on the office file server. He records each type with its location, owner and rough volume in a spreadsheet, and he notes where the same information is copied into more than one place, because each copy needs protecting.

### 2.2 Who depends on it

Daniel asks each partner which information they could not work without for a week. The answers cluster around three things: the accounting software during tax season, the email system for client communication, and the client portal for document collection. He also asks reception and the payroll team, who add the phone system and the payroll service. Ms. Ashby explains that dependency is as important as sensitivity. A system holding little personal data can still stop the business if it fails, and that kind of risk is often missed by people who think only about secrecy.

### 2.3 Security goals

Ms. Ashby introduces the three goals that ISO/IEC 27000:2026 uses to describe information security: confidentiality, integrity and availability. For Corbridge, confidentiality matters most for identity documents and bank statements. Integrity matters most for tax calculations and client bank details used for refunds, because a changed figure or account number causes direct financial harm. Availability matters most in the weeks before filing deadlines, when an outage of even a day causes missed submissions. Daniel adds a column to his inventory marking which goal matters most for each information type, with one sentence explaining why.

### 2.4 What cannot be lost

Daniel drafts a short statement for Mrs. Pike: the firm cannot afford a leak of client identity documents, a change to client refund bank details, or loss of the accounting software in January. She agrees and adds a fourth item from her own experience: the firm's reputation for discretion, which brings most new clients through referrals. Ms. Ashby tells Daniel that this statement will guide every priority decision for the rest of the course, and that a short list agreed by leadership is worth more than a long list written alone.

### Worked example

Daniel inventories Corbridge's information, finds what partners depend on, ties each type to a security goal and agrees four things the firm cannot lose.

> **Synthetic case.** Information types and volumes are synthetic.

### Errors and limits

Listing only sensitive data misses systems the business depends on to operate.

### Exercises

- **EX006 — Three goals.** Which three goals does ISO/IEC 27000:2026 use? *Rubric:* 3 = confidentiality, integrity, availability;; 2 = all three;; 1 = two;; 0 = none.
- **EX007 — Integrity example.** Give an integrity example at Corbridge. *Rubric:* 3 = client refund bank details;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX008 — Peak availability.** When does availability matter most? *Rubric:* 3 = weeks before filing deadlines;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX009 — Fourth item.** What did Mrs. Pike add to the list? *Rubric:* 3 = the firm's reputation for discretion;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX010 — Dependency lesson.** Why ask about dependency as well as sensitivity? *Rubric:* 3 = low-sensitivity systems can still stop the business;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue studying — lesson 02 (chapter 02 of 12)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Risk in plain terms

### Learning outcomes

You will (1) describe risk as likelihood and impact; (2) build a small risk register; (3) rank risks with a simple script.

### 3.1 What risk means

Ms. Ashby defines a risk as something that could go wrong, described by how likely it is and how much harm it would cause. NIST SP 800-30 Revision 1, the guide to conducting risk assessments, uses the same two ideas, though in more detail. She asks the group to write each risk as a short sentence naming the cause and the result, such as phishing leads to mailbox takeover. Vague entries like cyber attack cannot be acted on, because nobody knows which control would help or who should own the work.

### 3.2 Building the register

Daniel lists eight risks for Corbridge after talking with partners and the support company. He scores each from one to five for likelihood and impact, using simple descriptions: a likelihood of four means it has happened to similar firms several times recently; an impact of five means client harm, regulatory reporting and lost clients. Ms. Ashby reminds him that the scores are judgements, not measurements, and that their value lies in forcing a conversation about which risks matter most. He records who gave each score and why.

### Lab — Ranking a synthetic risk register by likelihood times impact

```python
"""Score a synthetic risk register by likelihood x impact and rank it (stdlib only)."""
risks = [
    ("R1 phishing leads to mailbox takeover", 4, 4),
    ("R2 laptop lost with client files", 3, 4),
    ("R3 ransomware on file server", 2, 5),
    ("R4 payment diversion by fake invoice", 3, 5),
    ("R5 leaver keeps cloud access", 3, 3),
    ("R6 backup fails silently", 2, 4),
    ("R7 website defaced", 2, 2),
    ("R8 tax software vendor breach", 1, 4),
]
scored = sorted(((l * i, name, l, i) for name, l, i in risks), reverse=True)
for s, name, l, i in scored:
    band = "high" if s >= 15 else "medium" if s >= 8 else "low"
    print(f"{s:>2} {band:<6} {name} (L{l} x I{i})")
print("high:", sum(1 for s, *_ in scored if s >= 15), "medium:", sum(1 for s, *_ in scored if 8 <= s < 15), "low:", sum(1 for s, *_ in scored if s < 8))
```

Run with `python3 lab_risk.py`. Verified output:

```text
16 high   R1 phishing leads to mailbox takeover (L4 x I4)
15 high   R4 payment diversion by fake invoice (L3 x I5)
12 medium R2 laptop lost with client files (L3 x I4)
10 medium R3 ransomware on file server (L2 x I5)
 9 medium R5 leaver keeps cloud access (L3 x I3)
 8 medium R6 backup fails silently (L2 x I4)
 4 low    R8 tax software vendor breach (L1 x I4)
 4 low    R7 website defaced (L2 x I2)
high: 2 medium: 4 low: 2
```

### 3.3 Reading the ranking

The script multiplies likelihood by impact and sorts the register. Two risks score fifteen or more and are marked high: phishing leading to mailbox takeover at sixteen, and payment diversion by a fake invoice at fifteen. Four are medium, from lost laptops at twelve down to silent backup failure at eight. Two are low at four each: a breach at the tax software vendor and website defacement. Daniel notices that both high risks start with an email, which tells him where to focus first and gives him a simple message for the partners.

### 3.4 Limits of scoring

Ms. Ashby warns against treating the numbers as precise. A vendor breach scored low because Daniel judged it unlikely, but its impact could reach every client at once. She suggests keeping a short note beside any low-scoring risk with a severe worst case, so leadership sees it rather than having it hidden at the bottom of a list. Daniel adds such a note to the vendor risk and plans to ask the vendor about its own security in the supplier chapter. He also sets a date to review all scores in three months.

### Worked example

Daniel scores eight synthetic risks; the script ranks phishing takeover (16) and invoice fraud (15) as high, four medium and two low, and he flags the vendor risk's severe worst case.

> **Synthetic case.** Risks and scores are synthetic.

### Errors and limits

Treating judgement-based scores as precise measurements hides uncertainty from decision makers.

### Exercises

- **EX011 — Top risk.** Which risk ranks highest and with what score? *Rubric:* 3 = phishing mailbox takeover, 16;; 2 = both;; 1 = one;; 0 = none.
- **EX012 — High count.** How many risks are high? *Rubric:* 3 = two;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX013 — Common cause.** What do both high risks start with? *Rubric:* 3 = an email;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX014 — Vendor note.** Why add a note to the vendor risk? *Rubric:* 3 = low score but severe worst case;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX015 — Good risk sentence.** How should a risk be written? *Rubric:* 3 = cause and result in a short sentence;; 2 = both;; 1 = one;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue studying — lesson 03 (chapter 03 of 12)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Accounts and multi-factor sign-in

### Learning outcomes

You will (1) explain why multi-factor sign-in matters; (2) measure coverage by account type; (3) plan fixes for gaps.

### 4.1 Why it matters

Daniel's top risk is mailbox takeover after phishing. Ms. Ashby explains that a stolen password alone is enough to take over an account protected only by a password, but a second factor, such as an app prompt or a security key, stops most such attempts. She notes that attackers increasingly try to trick users into approving prompts, so the method matters too. Daniel decides to measure how many Corbridge accounts already use a second factor before proposing anything, because a recommendation based on numbers is easier for partners to accept.

### 4.2 Account types

Daniel exports a list of accounts from the email and identity service, with permission from Mrs. Pike, and groups them into four types: partners, staff, administrators and service accounts. Service accounts are used by software rather than people, such as the scanner that emails documents into folders. He replaces names with codes before using the list in coursework. Ms. Ashby points out that administrators deserve separate attention because one compromised administrator account can change settings for everyone, so their coverage matters more than the overall total.

### Lab — Multi-factor sign-in coverage by account type in a synthetic directory

```python
"""Measure multi-factor sign-in coverage by account type in a synthetic directory (stdlib only)."""
import random
from collections import Counter
random.seed(25)
accounts = []
for kind, n, p in [("partner", 8, 0.75), ("staff", 52, 0.6), ("admin", 4, 0.5), ("service", 6, 0.0)]:
    for i in range(n):
        accounts.append((kind, random.random() < p))
total = Counter(k for k, _ in accounts)
on = Counter(k for k, m in accounts if m)
for k in total:
    print(f"{k}: {on[k]} of {total[k]} with MFA ({on[k]/total[k]:.1%})")
print(f"all accounts: {sum(on.values())} of {len(accounts)} ({sum(on.values())/len(accounts):.1%})")
```

Run with `python3 lab_mfa.py`. Verified output:

```text
partner: 4 of 8 with MFA (50.0%)
staff: 39 of 52 with MFA (75.0%)
admin: 1 of 4 with MFA (25.0%)
service: 0 of 6 with MFA (0.0%)
all accounts: 44 of 70 (62.9%)
```

### 4.3 Reading the results

The script finds 44 of 70 synthetic accounts using a second factor, 62.9 percent overall. Staff are highest at 39 of 52, or 75 percent. Partners are at 4 of 8, or 50 percent. Administrators are lowest among people, at 1 of 4, or 25 percent. None of the six service accounts use a second factor. Daniel sees that the overall figure hides the most important gaps: the accounts with most power and the partners who approve payments are the least protected, which matches the invoice fraud risk. He shares the table with the support company before the partners see it.

### 4.4 Closing the gaps

Daniel proposes enabling a second factor for all administrators within a week and all partners within a month, with the support company present to help. For service accounts, which often cannot use a second factor, he asks the support company to restrict where each can sign in from and to remove any that are no longer needed. Ms. Ashby advises him to explain the change to partners in terms of the invoice fraud risk they already worry about, rather than as a technical rule. Mrs. Pike agrees to go first, to set an example.

### Worked example

Daniel measures synthetic coverage: 44 of 70 accounts (62.9 percent), administrators 1 of 4, partners 4 of 8, service accounts 0 of 6, and plans fixes starting with administrators.

> **Synthetic case.** Accounts are synthetic and anonymised.

### Errors and limits

An overall coverage figure can hide gaps in the most powerful accounts.

### Exercises

- **EX016 — Overall coverage.** What is overall MFA coverage? *Rubric:* 3 = 44 of 70, 62.9 percent;; 2 = both;; 1 = one;; 0 = none.
- **EX017 — Administrators.** How many administrators use MFA? *Rubric:* 3 = 1 of 4;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX018 — Service accounts.** What does Daniel do about service accounts? *Rubric:* 3 = restrict sign-in locations, remove unused;; 2 = both;; 1 = one;; 0 = none.
- **EX019 — Partner pitch.** How should the change be explained to partners? *Rubric:* 3 = in terms of invoice fraud risk;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX020 — Who first.** Who agrees to enable MFA first? *Rubric:* 3 = Mrs. Pike;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue studying — lesson 04 (chapter 04 of 12)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Devices and data in the office

### Learning outcomes

You will (1) set a baseline for laptops; (2) handle the old file server; (3) reduce paper and removable media risks.

### 5.1 Laptop baseline

The support company manages Corbridge's laptops, but nobody has written down what a properly set up laptop looks like. Daniel drafts a short baseline with them: disk encryption on, automatic updates on, screen lock after five minutes, staff use standard accounts, and the device can be wiped remotely if lost. He asks for a monthly report showing how many laptops meet each item. Ms. Ashby explains that a written baseline turns vague trust in a supplier into something that can be checked, and that the monthly report gives Daniel evidence for leadership.

### 5.2 The old file server

The office file server holds client files more than ten years old. Daniel learns that the firm's retention rules say most client records need keeping for a set number of years, after which they should be destroyed. He asks a partner to review a sample and finds many files well past that period. Keeping them adds risk without benefit. With Mrs. Pike's approval he plans a supervised clean-up, starting with a list of folders by age, and asks the support company to confirm that backups of deleted files also expire on schedule.

### 5.3 Paper and media

Corbridge still receives paper documents from some older clients. Daniel finds a tray of scanned originals waiting to be returned, kept on an open shelf near reception. He moves them to a locked cabinet and sets a rule that originals are returned or securely shredded within two weeks of scanning. He also finds two unencrypted memory sticks used to carry files between offices. He replaces them with the cloud folders already available, and asks the support company to block unencrypted removable storage on laptops, with exceptions only by request.

### 5.4 Checking progress

After a month, the support company's report shows 55 of 60 laptops meeting the full baseline. The five exceptions include two laptops that missed updates while staff were on leave and three where encryption was never switched on. Daniel follows each up and records the fix. The file server clean-up removes a large share of out-of-date folders, after partner sign-off on each batch. He records what was deleted and why, so the firm can answer questions later. Ms. Ashby praises the record-keeping as much as the clean-up itself.

### Worked example

Daniel writes a five-item laptop baseline, finds 55 of 60 laptops compliant after a month, cleans up out-of-date server files with partner sign-off, and locks away paper originals.

> **Synthetic case.** Device counts and findings are synthetic.

### Errors and limits

Deleting old records without sign-off and a log can breach retention duties or leave the firm unable to explain what happened.

### Exercises

- **EX021 — Baseline items.** Name three items in the laptop baseline. *Rubric:* 3 = encryption, updates, screen lock, standard accounts, remote wipe;; 2 = three;; 1 = two;; 0 = none.
- **EX022 — Compliance.** How many laptops met the baseline after a month? *Rubric:* 3 = 55 of 60;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX023 — Old files.** Why remove out-of-date server files? *Rubric:* 3 = risk without benefit;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX024 — Paper rule.** What rule did Daniel set for paper originals? *Rubric:* 3 = returned or shredded within two weeks;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX025 — Memory sticks.** What replaced the memory sticks? *Rubric:* 3 = the existing cloud folders;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 12)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Email and payment fraud

### Learning outcomes

You will (1) explain how invoice and payment fraud works; (2) design checks that stop it; (3) prepare staff for it.

### 6.1 How the fraud works

Daniel's second high risk is payment diversion. Ms. Ashby explains the usual pattern: a criminal gains access to a supplier's or client's mailbox, or registers a lookalike address, and sends a convincing message saying bank details have changed. Staff update the details and the next payment goes to the criminal. For an accountancy firm, the same trick can target client tax refunds. The messages often arrive at busy times and refer to real invoices, which is why careful people are still fooled. Daniel realises that technical controls alone cannot stop this pattern.

### 6.2 Verification checks

Daniel proposes a simple rule: no change to any bank details, for suppliers or client refunds, is made on the strength of an email alone. The person receiving the request phones the supplier or client on a number already on file, not one in the email, and records the call. A second person approves the change before the next payment. Mrs. Pike accepts the rule but asks for a way to handle urgent requests. Daniel suggests that urgency itself be treated as a warning sign, and that the managing partner be the only person who can approve a same-day change.

### 6.3 Email protections

Daniel asks the support company to mark emails from outside the firm with a visible banner, and to check that the firm's own domain is set up so that criminals find it harder to send email pretending to be Corbridge. He also asks them to flag messages from newly registered domains that resemble client or supplier names. Ms. Ashby notes these measures reduce the number of fraudulent messages reaching staff but never remove them, so the verification rule remains the main defence. Daniel records each measure in his register against the payment risk.

### 6.4 Preparing staff

Daniel runs a short session for the finance and payroll teams. He shows two synthetic examples of fraudulent change requests and asks the teams to find the warning signs. He then walks through the phone-back rule step by step. The teams ask what to do if a client is annoyed at being called; Daniel suggests explaining that the call protects the client's money. A month later, a payroll assistant phones a supplier after an email requesting new bank details. The supplier knows nothing about it, and the attempt is stopped and reported.

### Worked example

Daniel introduces a phone-back and second-approval rule for bank detail changes, adds email protections, trains finance staff, and the rule stops a synthetic fraud attempt within a month.

> **Synthetic case.** Fraud examples are synthetic.

### Errors and limits

Calling a number provided in the suspicious email only reaches the criminal.

### Exercises

- **EX026 — Fraud pattern.** How does payment diversion usually work? *Rubric:* 3 = message says bank details changed;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX027 — Phone-back number.** Which number should staff call? *Rubric:* 3 = one already on file;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX028 — Urgent changes.** Who can approve a same-day change? *Rubric:* 3 = the managing partner only;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX029 — Main defence.** What remains the main defence against this fraud? *Rubric:* 3 = the verification rule;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX030 — Stopped attempt.** Who stopped the fraud attempt? *Rubric:* 3 = a payroll assistant;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 12)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Suppliers and cloud services

### Learning outcomes

You will (1) list the suppliers that handle firm information; (2) ask proportionate security questions; (3) record what each supplier can reach.

### 7.1 Supplier list

Daniel lists every outside organisation that stores or can reach Corbridge information: the email and file service, the accounting software vendor, the client portal provider, the payroll service, the support company and a shredding firm. He notes what each holds and how it connects. The support company stands out because it has administrator access to every laptop and the email system. Ms. Ashby explains that a supplier with broad access is part of the firm's security whether or not anyone thinks of it that way, so it belongs in the risk register.

### 7.2 Proportionate questions

Ms. Ashby advises against sending long questionnaires that small suppliers cannot answer. Instead, Daniel asks each a few questions matched to what they hold: does staff access require a second factor, how quickly will you tell us about a breach, where is our data stored, and what happens to it when the contract ends. ISO/IEC 27002:2022, the guidance on information security controls, includes supplier relationships among its control topics, and Daniel uses it as a checklist for his questions rather than a rulebook, choosing only the items that matter for each supplier.

### 7.3 The support company

The support company's answers show that its engineers share one administrator account for Corbridge systems. Daniel explains that this makes it impossible to tell who changed what. He asks for named accounts, each with a second factor, and for a monthly list of changes made. The company agrees, after some discussion about cost. Daniel also confirms that the support contract includes a duty to report incidents within one working day. Ms. Ashby notes that clear contract terms give a small firm leverage it would otherwise lack when dealing with a larger provider.

### 7.4 The vendor risk

Daniel returns to the low-scoring vendor breach risk from chapter three. The accounting software vendor publishes a security summary and holds a recognised certification, which Daniel records. He also checks how the firm would learn of a breach and what it would need to do: tell affected clients and possibly the regulator. He drafts a short plan for that case and files it with the incident procedures. Ms. Ashby observes that planning for a risk outside your control is still useful, because the response is within your control.

### Worked example

Daniel lists six suppliers, asks four proportionate questions of each, gets the support company to replace a shared administrator account with named accounts, and plans a response to a vendor breach.

> **Synthetic case.** Suppliers and answers are synthetic.

### Errors and limits

Long generic questionnaires often go unanswered and leave the real gaps unknown.

### Exercises

- **EX031 — Broadest access.** Which supplier has the broadest access? *Rubric:* 3 = the support company;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX032 — Four questions.** Name two of Daniel's supplier questions. *Rubric:* 3 = MFA, breach notice, data location, contract end;; 2 = two;; 1 = one;; 0 = none.
- **EX033 — Shared account.** What problem did the support company have? *Rubric:* 3 = one shared administrator account;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX034 — Reporting duty.** How fast must the support company report incidents? *Rubric:* 3 = within one working day;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX035 — Vendor plan.** Why plan for a vendor breach outside the firm's control? *Rubric:* 3 = the response is within its control;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 12)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — People and awareness

### Learning outcomes

You will (1) design short, relevant awareness activities; (2) handle joiners and leavers reliably; (3) build a culture where reporting is welcomed.

### 8.1 Relevant awareness

Corbridge has previously used a generic annual video that staff watch with the sound off. Daniel replaces it with short sessions tied to the firm's own risks: phishing, payment fraud, handling client documents and what to do with a lost laptop. Each session lasts fifteen minutes during a team meeting and uses synthetic examples that look like the firm's real work. Ms. Ashby explains that people remember examples from their own job far better than general advice, and that short regular sessions beat one long session a year for keeping habits fresh.

### 8.2 Joiners and leavers

Daniel checks how accounts are created and removed. New staff get accounts promptly, but leavers' accounts are sometimes disabled days after they go, because human resources tells the support company by email when someone remembers. He sets up a simple form that human resources completes on a leaver's last day, which goes straight to the support company and copies Daniel. He then compares the account list with the payroll list monthly. The first comparison finds two former seasonal staff with active accounts, which are removed the same day.

### 8.3 A reporting culture

Ms. Ashby stresses that staff who fear blame hide mistakes, and hidden mistakes become incidents. Daniel works with Mrs. Pike to send a short message from her: reporting a suspicious email or a mistake is always the right thing, and nobody will be criticised for reporting. He creates a single email address and phone number for reports. In the next month, staff report nine suspicious messages and one email sent to the wrong client. Daniel thanks each reporter personally, because the thanks encourage the next report as much as any training.

### 8.4 Measuring behaviour

Daniel wants to know whether the sessions change anything. He tracks three simple numbers each month: suspicious emails reported, mistakes self-reported and days taken to disable leavers' accounts. Ms. Ashby advises against judging success by the number of people who click a test phishing email, because results vary with how hard the test is and can make staff resentful. Daniel agrees and decides that rising reports and falling leaver delays are better signs that habits are changing, and he plans to show them to leadership quarterly alongside other measures.

### Worked example

Daniel replaces a generic video with short firm-specific sessions, fixes leaver delays with a form and monthly check, and gains nine reports in a month after a blame-free message.

> **Synthetic case.** Staff and figures are synthetic.

### Errors and limits

Judging awareness only by test click rates can mislead and discourage staff.

### Exercises

- **EX036 — Session length.** How long is each awareness session? *Rubric:* 3 = fifteen minutes;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX037 — Leaver gap.** Why were leavers' accounts disabled late? *Rubric:* 3 = HR emailed the support company when remembered;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX038 — Monthly check.** What does Daniel compare monthly? *Rubric:* 3 = account list against payroll list;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX039 — Reports gained.** How many suspicious messages were reported next month? *Rubric:* 3 = nine;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX040 — Better measure.** Why avoid judging by test click rates? *Rubric:* 3 = vary with difficulty, cause resentment;; 2 = both;; 1 = one;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 12)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Handling incidents

### Learning outcomes

You will (1) write a short incident procedure; (2) follow it during a synthetic incident; (3) decide when to notify clients or regulators.

### 9.1 A short procedure

Daniel writes a two-page procedure covering the first hours of an incident: who to call, how to contain the problem, what to record and who decides on notifications. It names Daniel as coordinator, the support company as technical responders and Mrs. Pike as decision maker for anything involving clients or regulators. Ms. Ashby reminds him that a procedure nobody can find is useless, so he prints copies for each office and saves one where it can be reached even if email is down, along with all the key phone numbers.

### 9.2 A mailbox takeover

Three weeks later, a partner's assistant reports that clients have received an odd message from her account asking them to open a document. Daniel follows the procedure. The support company resets the password, ends all active sessions, enables a second factor and removes a forwarding rule the attacker had added, which sent copies of all incoming mail to an outside address. Daniel records each step with times. He then asks the support company to check whether the attacker read or downloaded any client documents during the period the account was controlled.

### 9.3 Deciding on notification

The review shows that the attacker's forwarding rule copied about two weeks of incoming mail, including some messages with client identity documents attached. Mrs. Pike, with advice from the firm's data protection adviser, decides that the affected clients must be told and that the regulator must be notified within the legal time limit. Daniel prepares a factual list of affected clients and the type of documents involved. Ms. Ashby notes that the forwarding rule turned a nuisance into a reportable breach, which is why checking for such rules is a standard step.

### 9.4 Learning afterwards

A week later, Daniel holds a short review with the people involved. The cause was a stolen password on an account without a second factor; the assistant had been on the list for the next stage of the rollout. The firm brings forward the rollout for all remaining staff and adds a monthly check for forwarding rules to outside addresses. Daniel writes a one-page summary for the partners, without blaming the assistant, who reported promptly. Ms. Ashby praises the review for focusing on fixing the conditions that allowed the incident rather than on the individual.

### Worked example

Daniel's procedure guides a synthetic mailbox takeover: sessions ended, a forwarding rule removed, clients and the regulator notified, and the second-factor rollout brought forward.

> **Synthetic case.** The incident and clients are synthetic.

### Errors and limits

Resetting a password without removing forwarding rules leaves the attacker still receiving mail.

### Exercises

- **EX041 — Coordinator.** Who coordinates incidents at Corbridge? *Rubric:* 3 = Daniel;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX042 — Hidden rule.** What had the attacker added to the mailbox? *Rubric:* 3 = a forwarding rule to an outside address;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX043 — Notify why.** Why did the incident become reportable? *Rubric:* 3 = forwarded mail held client identity documents;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX044 — Root cause.** What was the root cause? *Rubric:* 3 = stolen password without a second factor;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX045 — New check.** What monthly check was added? *Rubric:* 3 = forwarding rules to outside addresses;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue studying — lesson 09 (chapter 09 of 12)

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Continuity and backups

### Learning outcomes

You will (1) identify what must keep running; (2) check that backups can be restored; (3) rehearse a short continuity exercise.

### 10.1 What must keep running

Using the dependency list from chapter two, Daniel identifies three services that must return quickly: email, the accounting software and the client portal. He asks each provider how they back up data and how fast they could restore it. He learns that the cloud email service keeps deleted items only for a limited period, so a malicious deletion noticed late might not be recoverable. The firm buys a separate backup service for email and files. Ms. Ashby explains that a cloud provider keeping the service running is not the same as backing up your data.

### 10.2 Testing restores

Daniel asks the support company to restore a sample of files and one mailbox from the new backup service into a test area. The files restore correctly, but the mailbox restore takes six hours, longer than expected. Daniel records the time and asks whether it can be improved for urgent cases. He also checks the old file server's backup and finds it has been copying to a disk in the same room, which would be lost in a fire or flood. The support company adds an off-site copy. Ms. Ashby reminds him that an untested backup is only a hope.

### 10.3 A tabletop exercise

Daniel runs a one-hour exercise with Mrs. Pike, two partners and the support company. The scenario: in early January, the accounting software vendor is unavailable for three days. The group discusses what work can continue, how clients would be told and whether filing deadlines could be met. They find that nobody knows how to ask the tax authority for extra time in such a case. One partner agrees to find out and document the steps. Daniel records the decisions and gaps, and schedules the next exercise for six months later.

### 10.4 Writing it down

Daniel turns the decisions into a three-page continuity plan: the three key services, who to contact for each, temporary ways of working and the steps for requesting deadline extensions. He stores printed copies in both offices and one with Mrs. Pike at home. Ms. Ashby notes that the plan's main value came from the conversation that produced it, because the partners now understand the firm's weak points. She suggests reviewing it before each busy season, when staff change and suppliers may have changed their arrangements.

### Worked example

Daniel adds a separate backup service, finds a six-hour mailbox restore and a backup disk in the same room, runs a vendor-outage tabletop exercise and writes a three-page continuity plan.

> **Synthetic case.** Services, times and decisions are synthetic.

### Errors and limits

Assuming a cloud provider backs up your data can leave deleted items unrecoverable.

### Exercises

- **EX046 — Key services.** Which three services must return quickly? *Rubric:* 3 = email, accounting software, client portal;; 2 = all three;; 1 = two;; 0 = none.
- **EX047 — Restore time.** How long did the mailbox restore take? *Rubric:* 3 = six hours;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX048 — Same-room disk.** What was wrong with the file server backup? *Rubric:* 3 = copied to a disk in the same room;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX049 — Exercise gap.** What gap did the tabletop exercise find? *Rubric:* 3 = nobody knew how to request a deadline extension;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX050 — Plan review.** When should the plan be reviewed? *Rubric:* 3 = before each busy season;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue studying — lesson 10 (chapter 10 of 12)

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Policy and obligations

### Learning outcomes

You will (1) write a short, usable security policy; (2) map the firm's legal and professional obligations; (3) decide whether formal certification is worthwhile.

### 11.1 A usable policy

Corbridge's existing security policy is a twenty-page document copied from a template, which nobody has read. Daniel replaces it with a two-page policy covering the rules staff actually need: accounts and second factors, devices, handling client documents, email and payments, reporting and supplier use. Each rule has a one-sentence reason. Detailed procedures, such as the phone-back rule and the incident procedure, sit in separate documents linked from the policy. Mrs. Pike signs the policy, and each member of staff confirms they have read it during a team meeting.

### 11.2 Obligations

Daniel maps what the firm must do by law and by professional rules. Data protection law requires appropriate security for personal data and notification of certain breaches within set time limits. The professional body expects members to protect client confidentiality. Some larger clients require security commitments in their contracts. Daniel lists each obligation with its source and the controls that meet it. Ms. Ashby advises him to confirm legal points with the firm's data protection adviser rather than relying on his own reading, because obligations differ between countries and change over time.

### 11.3 Certification

A large client asks whether Corbridge is certified to ISO/IEC 27001:2022, the international standard for an information security management system. Daniel explains to the partners that certification requires a documented management system, internal audits and an external audit each year, which would take significant time for a firm of sixty. He suggests a middle path: align the firm's work with the standard's main ideas, such as risk assessment, leadership commitment and regular review, and reconsider certification if more clients ask. The partners agree, and Daniel writes a short response for the client.

### 11.4 Keeping it current

Daniel sets a simple calendar for reviewing the policy and related documents: the policy once a year, the risk register every three months, supplier answers yearly and the continuity plan before each busy season. Each review has a named owner. Ms. Ashby explains that a policy left untouched for years drifts away from how people actually work, and staff stop trusting it. She praises the short policy for being readable, and suggests that Daniel ask two staff members each year whether the rules make sense to them in practice.

### Worked example

Daniel replaces a twenty-page template with a two-page signed policy, maps legal and professional obligations, and advises aligning with ISO/IEC 27001:2022 rather than certifying for now.

> **Synthetic case.** The policy, client request and obligations are synthetic and general; real legal duties need professional advice.

### Errors and limits

A long template policy that nobody reads gives a false sense of compliance.

### Exercises

- **EX051 — Policy length.** How long is Daniel's new policy? *Rubric:* 3 = two pages;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX052 — Procedures.** Where do detailed procedures go? *Rubric:* 3 = separate linked documents;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX053 — Certification cost.** What does certification require? *Rubric:* 3 = management system, internal and yearly external audits;; 2 = all;; 1 = some;; 0 = none.
- **EX054 — Middle path.** What did Daniel recommend instead of certifying now? *Rubric:* 3 = align with the standard's main ideas;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX055 — Legal advice.** Who should confirm legal points? *Rubric:* 3 = the data protection adviser;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue studying — lesson 11 (chapter 11 of 12)

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Reporting to leadership and next steps

### Learning outcomes

You will (1) report security status in plain language; (2) review six months of progress; (3) plan the next year and further study.

### 12.1 A one-page report

Daniel prepares a one-page report for the partners each quarter. It shows the top risks and whether each is rising or falling, five measures with their trend, recent incidents in one line each, and up to three decisions needed. The measures are second-factor coverage, laptops meeting the baseline, days to disable leavers, suspicious emails reported and the last successful restore test. Ms. Ashby advises him to put the decisions first, because partners have little time, and to avoid technical terms they would need explained before they could respond.

### 12.2 Six months of progress

Daniel compares the start of the course with today. Second-factor coverage has risen from 62.9 percent to all people accounts, with service accounts restricted instead. Laptops meeting the baseline went from unknown to 55 of 60 and then to all 60. Leavers are now disabled on their last day. One fraud attempt was stopped and one incident was handled and reported within the legal time limit. Mrs. Pike tells the partners that she now has a clear answer to her original question, and that the next steps are known.

### 12.3 The next year

Daniel drafts a plan for the next twelve months: complete the file server clean-up and move remaining records to the cloud, repeat the tabletop exercise with a ransomware scenario, review supplier answers, and run awareness sessions on new fraud patterns. He estimates the time and cost of each and asks the partners to choose. Ms. Ashby suggests he also budget time for his own learning, since threats and services change faster than any course can cover, and that he join a local group of security practitioners for support and fresh ideas.

### 12.4 Further study

Ms. Ashby reviews options with Daniel. He could take a recognised introductory certification to formalise his knowledge, attend short courses on incident handling or cloud security, or move to a longer qualification later. She also recommends the data governance course that follows this one, since much of Daniel's work, such as retention and supplier data handling, overlaps with how organisations manage information as an asset. Daniel decides to start the data governance course next term and to aim for a certification within a year.

### Worked example

Daniel writes a one-page quarterly report with decisions first, shows six months of progress from 62.9 percent second-factor coverage to full people coverage, and plans the next year and further study.

> **Synthetic case.** Progress figures are synthetic.

### Errors and limits

Reports full of technical detail without clear decisions are often ignored by leadership.

### Exercises

- **EX056 — Report order.** What should come first in the partner report? *Rubric:* 3 = decisions needed;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX057 — Five measures.** Name three of the five measures. *Rubric:* 3 = MFA, baseline, leaver days, reports, restore test;; 2 = three;; 1 = two;; 0 = none.
- **EX058 — Coverage change.** How did second-factor coverage change? *Rubric:* 3 = 62.9 percent to all people accounts;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX059 — Next scenario.** What scenario will the next tabletop use? *Rubric:* 3 = ransomware;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX060 — Next course.** Which course does Daniel take next? *Rubric:* 3 = data governance;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue studying — lesson 12 (chapter 12 of 12)

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Daniel Reyes, Ms. Helen Ashby, Kingsmere Professional Institute, Corbridge Accountancy Partners and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Six months, two evenings a week.

**EX002.** Around two thousand clients.

**EX003.** Whether the firm is doing the right things and what to do next.

**EX004.** It records written agreement before he checks any system.

**EX005.** No; he only needs to read and run them.

**EX006.** Confidentiality, integrity and availability.

**EX007.** Client bank details used for tax refunds.

**EX008.** In the weeks before tax filing deadlines.

**EX009.** The firm's reputation for discretion.

**EX010.** A system with little personal data can still halt work if it fails.

**EX011.** Phishing leading to mailbox takeover, scored 16.

**EX012.** Two: mailbox takeover and invoice fraud.

**EX013.** Both start with an email.

**EX014.** Its score is low but its worst case could reach every client.

**EX015.** As a short sentence naming the cause and the result.

**EX016.** 44 of 70 accounts, 62.9 percent.

**EX017.** One of four administrators, 25 percent.

**EX018.** Restrict where each can sign in from and remove unused ones.

**EX019.** In terms of the invoice fraud risk they already worry about.

**EX020.** Mrs. Pike, the managing partner.

**EX021.** Disk encryption, automatic updates and a five-minute screen lock.

**EX022.** 55 of 60 laptops.

**EX023.** Keeping them adds risk without benefit once retention ends.

**EX024.** Return or securely shred them within two weeks of scanning.

**EX025.** The cloud folders the firm already had.

**EX026.** A convincing message says bank details have changed, diverting the next payment.

**EX027.** A number already on file, never one from the email.

**EX028.** Only the managing partner.

**EX029.** The phone-back and second-approval rule.

**EX030.** A payroll assistant who phoned the supplier.

**EX031.** The support company, with administrator access to laptops and email.

**EX032.** Whether staff use a second factor and how quickly they report a breach.

**EX033.** Engineers shared one administrator account.

**EX034.** Within one working day.

**EX035.** Because the firm still controls its own response.

**EX036.** Fifteen minutes during a team meeting.

**EX037.** Human resources emailed the support company only when someone remembered.

**EX038.** The account list against the payroll list.

**EX039.** Nine suspicious messages, plus one misdirected email.

**EX040.** Results vary with test difficulty and can make staff resentful.

**EX041.** Daniel coordinates; Mrs. Pike decides on notifications.

**EX042.** A rule forwarding incoming mail to an outside address.

**EX043.** Forwarded mail included client identity documents.

**EX044.** A stolen password on an account with no second factor.

**EX045.** A monthly check for rules forwarding mail outside the firm.

**EX046.** Email, the accounting software and the client portal.

**EX047.** Six hours, longer than expected.

**EX048.** It copied to a disk in the same room as the server.

**EX049.** Nobody knew how to ask the tax authority for extra time.

**EX050.** Before each busy season.

**EX051.** Two pages, with reasons for each rule.

**EX052.** In separate documents linked from the policy.

**EX053.** A documented management system, internal audits and a yearly external audit.

**EX054.** Align with the standard's main ideas and revisit if more clients ask.

**EX055.** The firm's data protection adviser.

**EX056.** The decisions needed.

**EX057.** Second-factor coverage, laptops meeting baseline and days to disable leavers.

**EX058.** From 62.9 percent to every account used by a person.

**EX059.** A ransomware scenario.

**EX060.** The data governance course, starting next term.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and ISO/IEC editions were checked against iso.org on the same day. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
