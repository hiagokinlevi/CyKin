# Security Architecture and Engineering: Rapid Course

- Language: English (`en`); course 007, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: staff in small organisations who need a fast, practical start in security architecture.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs count supplier dependencies and check settings against a baseline, both on synthetic data; nothing touches a real system. Production designs use vetted products and standards; never roll your own cryptography. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The four chapters follow one operations coordinator at a small credit union: foundations and decisions; scope, permission and safe practice; systems, data and dependencies; and a guided lab with a closing plan. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leah Brennan** | Operations coordinator and rapid-course learner | Invented |
| **Felix Ortega** | Tutor | Invented |
| **Northgate Learning Centre** | Fictional training provider | Invented |
| **Saltmarsh Community Credit Union** | Fictional credit union with two branches | Invented |

### Core sources

Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Anderson, *Security Engineering* 3e (2020); Shostack, *Threat Modeling* (2014). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security architecture and engineering: foundations and decisions

### Learning outcomes

You will (1) explain security architecture in plain terms; (2) apply five design principles to a small credit union; (3) record one decision properly.

### 1.1 What architecture means

Leah Brennan coordinates operations at the fictional Saltmarsh Community Credit Union, which serves six thousand members from two branches and a website. She joins a one-month rapid course at the fictional Northgate Learning Centre, taught by Felix Ortega. Felix defines security architecture as the overall arrangement of protections across people, processes and technology, designed so they work together. It answers practical questions: who may reach which systems, where identities are checked, where member data lives and how services recover. It is a plan for the whole, not a list of products.

### 1.2 Why it matters to a small organisation

Leah asks whether a small credit union needs architecture at all. Felix explains that small organisations make security decisions constantly, such as buying a new loan system or letting a supplier connect remotely. Without an overall plan, each decision is made alone and they often contradict one another. A short written architecture lets Leah check each new proposal against agreed principles. Anderson (2020) notes that many security failures come from systems that were each reasonable alone but unsafe in combination. Leah agrees to draft one for Saltmarsh.

### 1.3 Five principles

Felix teaches five principles from Saltzer and Schroeder (1975), in plain terms. Least privilege: give each person only the access their job needs. Fail-safe defaults: start from no access and grant what is needed. Complete mediation: check permission on every request, not only at sign-in. Separation of privilege: require two people or two conditions for the most sensitive actions. Psychological acceptability: make controls easy enough that people use them properly. Leah notes that these principles are decades old yet still describe most of the problems she sees at work.

### 1.4 Applying them at Saltmarsh

Leah applies the principles. Tellers can view member accounts but not change interest rates, which is least privilege. New staff accounts start empty and receive roles on approval, which is fail-safe defaults. Large transfers need a second staff member to approve, which is separation of privilege. She finds a gap: the shared branch email account is used by all tellers, so nobody can tell who sent what. She also finds the online banking sign-in already uses an app-based second factor, which members find easy, an example of acceptability.

### 1.5 Recording a decision

Leah's first architecture decision is whether to replace the shared branch email account with individual mailboxes and a shared inbox that each person accesses with their own account. She writes a short decision record: context, options, the choice, reasons, consequences and when to revisit. The choice is individual accounts with shared inbox access. The reason is accountability, since member queries must be traceable to the person who answered. Felix stresses that writing decisions down lets others understand and challenge them later, even after the author has moved on.

### Worked example

Leah defines architecture in plain terms, applies five principles to Saltmarsh, finds a shared email gap and records a decision to replace it.

> **Synthetic case.** Saltmarsh, Northgate and all people are synthetic; Anderson (2020) and Saltzer and Schroeder (1975) are real.

### Errors and limits

Principles can conflict, such as acceptability against separation of privilege. Short courses give foundations, not mastery.

### Exercises

- **EX001 — Plain definition.** How does Felix define security architecture? *Rubric:* 3 = the overall arrangement of protections across people, process and technology;; 2 = overall plan;; 1 = product list;; 0 = none.
- **EX002 — Small organisations.** Why does a small credit union need architecture? *Rubric:* 3 = decisions made alone often contradict each other;; 2 = consistency;; 1 = vague;; 0 = none.
- **EX003 — Least privilege at Saltmarsh.** Give Saltmarsh's example of least privilege. *Rubric:* 3 = tellers view accounts but cannot change interest rates;; 2 = tellers;; 1 = vague;; 0 = none.
- **EX004 — Fail-safe example.** Which practice shows fail-safe defaults? *Rubric:* 3 = new staff accounts start empty and get roles on approval;; 2 = empty start;; 1 = vague;; 0 = none.
- **EX005 — Two-person rule.** Where does Saltmarsh use separation of privilege? *Rubric:* 3 = large transfers need a second approver;; 2 = transfers;; 1 = vague;; 0 = none.
- **EX006 — Shared mailbox gap.** Why is the shared branch email account a gap? *Rubric:* 3 = nobody can tell who sent what;; 2 = accountability;; 1 = vague;; 0 = none.
- **EX007 — Acceptability example.** Which control shows psychological acceptability? *Rubric:* 3 = the app-based second factor members find easy;; 2 = app factor;; 1 = vague;; 0 = none.
- **EX008 — Decision record parts.** List the parts of Leah's decision record. *Rubric:* 3 = context, options, choice, reasons, consequences, revisit date;; 2 = four;; 1 = vague;; 0 = none.
- **EX009 — Chosen option.** Which option did the email decision select? *Rubric:* 3 = individual accounts with shared inbox access;; 2 = individual;; 1 = keep shared;; 0 = none.
- **EX010 — Reason for choice.** Why did accountability drive the email choice? *Rubric:* 3 = member queries must be traceable to who answered;; 2 = traceable;; 1 = cost;; 0 = none.
- **EX011 — Combined failures.** According to Anderson, where do many failures come from? *Rubric:* 3 = systems reasonable alone but unsafe together;; 2 = combination;; 1 = single bugs;; 0 = none.
- **EX012 — Principle conflict.** Name two principles that can conflict. *Rubric:* 3 = acceptability and separation of privilege;; 2 = pair;; 1 = vague;; 0 = none.
- **EX013 — Value of writing.** Why write decisions down, according to Felix? *Rubric:* 3 = so others can understand and challenge them later;; 2 = challenge;; 1 = vague;; 0 = none.

### Synthesis

Security architecture is a written plan grounded in a few durable principles and recorded decisions.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) set the scope of a small security review; (2) obtain written permission; (3) work safely with member data.

### 2.1 Setting scope

Leah's manager asks her to review security around Saltmarsh's new loan application system. Felix teaches her to write a scope first: which systems are included, which are excluded, what she will do and what she will not do. Included are the loan system, the staff PCs that use it and the document upload feature for members. Excluded are the core banking system, run by a service bureau, and the card processor. She will read settings and interview staff; she will not attempt attacks or access member files.

### 2.2 Written permission

Leah obtains written approval from the chief executive and the loan system owner. The approval names her, the systems in scope, the dates and the activities allowed. Felix explains that even staff reviewing their own employer's systems need permission, because reviews can touch sensitive data, disrupt services or breach supplier contracts. The approval also protects Leah if anyone questions her actions. She asks the loan system vendor to confirm that reading configuration screens does not breach the support contract. She files the approval with her notes.

### 2.3 Safe handling of member data

Loan applications include payslips, bank statements and identity documents. Leah's review does not need any of them. Where screens show member data, she uses a test application created by the vendor with fictitious details. When taking screenshots of settings, she checks that no member information appears. Her notes are stored in a restricted folder and will be deleted after the review is accepted. Felix stresses that a security review must never become a new source of data exposure. She confirms this approach with the system owner first.

### 2.4 Stop conditions

Felix asks Leah to define when she will stop and report immediately. She lists three conditions: finding signs that someone else has already broken in, finding member documents exposed to the internet and causing any disruption to the loan service. In each case she will stop, tell the system owner and the chief executive, and not investigate further alone. Clear stop conditions protect members and keep the reviewer from wandering into incident response work that needs different skills and authority.

### 2.5 A finding under scope

During the review, Leah finds that document uploads are stored in a cloud folder whose sharing setting allows anyone with the link to view files. This meets one of her stop conditions. She stops, informs the owner and chief executive, and the vendor changes the setting within the hour. The vendor checks access logs and finds no access by unknown parties. Leah records the event, the response and the evidence. Her scope, permission and stop conditions made the response quick, calm and properly documented.

### Worked example

Leah scopes a loan system review, obtains written permission, uses fictitious test data, defines three stop conditions and handles a link-sharing finding correctly.

> **Synthetic case.** The loan system and events are synthetic.

### Errors and limits

Scopes can exclude where problems lie. Vendor logs may not show all access.

### Exercises

- **EX014 — Excluded systems.** Which systems did the scope exclude? *Rubric:* 3 = core banking run by a service bureau and the card processor;; 2 = both;; 1 = vague;; 0 = none.
- **EX015 — Not allowed.** Which activities were outside Leah's permission? *Rubric:* 3 = attempting attacks or accessing member files;; 2 = attacks;; 1 = interviews;; 0 = none.
- **EX016 — Approvers.** Who approved Leah's review in writing? *Rubric:* 3 = the chief executive and the loan system owner;; 2 = both;; 1 = vague;; 0 = none.
- **EX017 — Vendor check.** What did Leah confirm with the vendor? *Rubric:* 3 = that reading configuration screens does not breach the support contract;; 2 = contract;; 1 = vague;; 0 = none.
- **EX018 — Test application.** How did Leah avoid seeing real member data? *Rubric:* 3 = used a vendor test application with fictitious details;; 2 = test data;; 1 = vague;; 0 = none.
- **EX019 — Screenshot care.** What did Leah check before saving screenshots? *Rubric:* 3 = that no member information appears;; 2 = no data;; 1 = vague;; 0 = none.
- **EX020 — Three stop triggers.** Which three conditions make Leah stop? *Rubric:* 3 = signs of a break-in, member documents exposed online, disruption to the service;; 2 = two;; 1 = vague;; 0 = none.
- **EX021 — Why stop.** Why should a reviewer stop rather than investigate alone? *Rubric:* 3 = incident response needs different skills and authority;; 2 = authority;; 1 = vague;; 0 = none.
- **EX022 — Upload finding.** What exposure did the review find? *Rubric:* 3 = uploads in a cloud folder viewable by anyone with the link;; 2 = link sharing;; 1 = vague;; 0 = none.
- **EX023 — Vendor log result.** What did the vendor's access logs show? *Rubric:* 3 = no access by unknown parties;; 2 = none found;; 1 = breach;; 0 = none.
- **EX024 — Notes retention.** When are Leah's review notes deleted? *Rubric:* 3 = after the review is accepted;; 2 = after acceptance;; 1 = never;; 0 = none.
- **EX025 — Response speed.** How quickly did the vendor fix the sharing setting? *Rubric:* 3 = within the hour;; 2 = hour;; 1 = vague;; 0 = none.
- **EX026 — Review exposure.** What must a security review never become? *Rubric:* 3 = a new source of data exposure;; 2 = exposure;; 1 = vague;; 0 = none.

### Synthesis

Scope, permission, safe data handling and stop conditions make reviews useful and safe.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Security architecture and engineering: systems, data and dependencies

### Learning outcomes

You will (1) map Saltmarsh's systems and data flows; (2) identify suppliers and dependencies; (3) find where one failure would stop many services.

### 3.1 Mapping systems

Leah lists Saltmarsh's main systems with their owners: the core banking system at the service bureau, online banking, the new loan system, email and office tools in the cloud, branch PCs, the card processor and the phone system. For each she records what data it holds and who uses it. Member account balances and transactions sit in core banking; loan documents sit in the loan system; member correspondence sits in email. Knowing where data lives tells her which systems need the strongest protection.

### 3.2 Drawing data flows

Leah draws how a loan application moves: a member uploads documents through the website; the loan system stores them; a loan officer reviews them on a branch PC; approval triggers a payment through core banking; the member receives an email. She labels each flow with the data it carries and marks where it crosses to a supplier. Shostack (2014) recommends close attention to these crossings, because each one relies on someone else's controls and assumptions about what the other side has checked.

### 3.3 Suppliers and dependencies

Saltmarsh depends heavily on suppliers: the service bureau, the loan system vendor, the cloud email provider, the card processor, the identity provider used for staff sign-in and two internet providers. Leah records each supplier's role, the data it holds, the contract owner and what happens if it fails. She notes that the identity provider is used by almost every system, so its failure or compromise would affect nearly everything. Dependencies are part of the architecture even though Saltmarsh does not operate them.

### Lab — Counting services that depend on each supplier

```python
# Count services depending on each supplier (synthetic map).
services = {"online banking": ["identity", "bureau", "internet"], "loan system": ["identity", "loan vendor", "bureau"],
            "email": ["identity", "cloud email"], "branch PCs": ["identity", "internet"],
            "card services": ["card processor", "bureau"], "staff intranet": ["identity", "cloud email"],
            "member payments": ["identity", "bureau"]}
count = {}
for s, deps in services.items():
    for d in deps: count[d] = count.get(d, 0) + 1
for d, n in sorted(count.items(), key=lambda x: (-x[1], x[0])): print(f"{d:14} {n} service(s)")
```

Run with `python3 lab_deps.py`. Verified output:

```text
identity       6 service(s)
bureau         4 service(s)
cloud email    2 service(s)
internet       2 service(s)
card processor 1 service(s)
loan vendor    1 service(s)
```

### 3.4 Single points of failure

The lab counts how many services depend on each supplier. The identity provider supports six services and the service bureau four; most others support one or two. Leah discusses the results with her manager. For the identity provider they agree a break-glass administrator account stored securely offline and a tested procedure for signing in if the provider fails. For the service bureau they rely on its contractual recovery commitments and keep a manual procedure for urgent member withdrawals at branches.

### 3.5 Using the map

Leah stores the system list, data flow diagram and dependency table together as Saltmarsh's first architecture overview. When the board later considers a new budgeting app for members, the overview shows that it would add a new supplier holding transaction data and another dependency on the identity provider. The board asks the vendor security questions before signing. Felix notes that a simple map pays for itself the first time it shapes a decision before money is spent. Leah sets a yearly date to update the overview.

### Worked example

Leah maps systems and loan data flows, lists six suppliers, counts dependencies to find the identity provider as the main single point of failure and uses the map for a board decision.

> **Synthetic case.** Systems, suppliers and counts are synthetic; Shostack (2014) is real.

### Errors and limits

Maps go stale without updates. Supplier failures can cascade through fourth parties.

### Exercises

- **EX027 — Where balances live.** Which system holds account balances and transactions? *Rubric:* 3 = core banking at the service bureau;; 2 = core banking;; 1 = loan system;; 0 = none.
- **EX028 — Loan flow steps.** Describe the loan application flow. *Rubric:* 3 = upload, loan system, officer review, core banking payment, email;; 2 = most steps;; 1 = vague;; 0 = none.
- **EX029 — Crossing attention.** Why do supplier crossings need attention? *Rubric:* 3 = each relies on someone else's controls and assumptions;; 2 = assumptions;; 1 = vague;; 0 = none.
- **EX030 — Supplier record.** What does Leah record for each supplier? *Rubric:* 3 = role, data held, contract owner and failure impact;; 2 = three;; 1 = vague;; 0 = none.
- **EX031 — Identity count.** How many services depend on the identity provider in the lab? *Rubric:* 3 = six;; 2 = 6;; 1 = one;; 0 = none.
- **EX032 — Bureau count.** How many services depend on the service bureau? *Rubric:* 3 = four;; 2 = 4;; 1 = vague;; 0 = none.
- **EX033 — Break-glass.** What fallback was agreed for the identity provider? *Rubric:* 3 = an offline break-glass account and tested sign-in procedure;; 2 = break-glass;; 1 = vague;; 0 = none.
- **EX034 — Bureau fallback.** What fallback exists for the service bureau? *Rubric:* 3 = contractual recovery and a manual branch withdrawal procedure;; 2 = manual;; 1 = vague;; 0 = none.
- **EX035 — Budgeting app.** What did the map reveal about the budgeting app? *Rubric:* 3 = a new supplier with transaction data and more identity dependency;; 2 = new supplier;; 1 = vague;; 0 = none.
- **EX036 — Board action.** How did the board respond to the budgeting app? *Rubric:* 3 = asked the vendor security questions before signing;; 2 = questions;; 1 = signed;; 0 = none.
- **EX037 — Map payoff.** When does a simple map pay for itself? *Rubric:* 3 = the first time it shapes a decision before money is spent;; 2 = first decision;; 1 = never;; 0 = none.
- **EX038 — Stale maps.** What limits the usefulness of the map over time? *Rubric:* 3 = it goes stale without updates;; 2 = staleness;; 1 = vague;; 0 = none.

### Synthesis

Mapping systems, data flows and dependencies shows where protection and fallback plans matter most.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Security architecture and engineering: guided lab and applied synthesis

### Learning outcomes

You will (1) check a system's settings against a baseline in a guided lab; (2) turn results into prioritised actions; (3) synthesise the month's learning into a short plan.

### 4.1 The guided lab

Felix sets a guided lab using synthetic settings exported from a loan system like Saltmarsh's. The lab compares each setting with a short baseline drawn from the month's principles: multi-factor sign-in for staff, sessions that time out, no shared accounts, upload links that expire, audit logging on and administrator rights limited to two people. Leah runs the script and reads the output line by line. The lab runs offline on fictitious data, so nothing touches a real system. Felix walks the class through the first two checks.

### Lab — Checking loan system settings against a baseline

```python
# Check loan system settings against a baseline (synthetic exports before and after fixes).
rules = {"staff_mfa": lambda v: v == "on", "session_timeout_min": lambda v: v <= 30,
         "shared_accounts": lambda v: v == 0, "upload_link_expiry_days": lambda v: v is not None and v <= 14,
         "audit_logging": lambda v: v == "on", "admin_count": lambda v: v <= 2, "public_links": lambda v: v == "off"}
after = {"staff_mfa": "on", "session_timeout_min": 30, "shared_accounts": 0, "upload_link_expiry_days": 14,
         "audit_logging": "on", "admin_count": 2, "public_links": "off"}
before = dict(after, session_timeout_min=480, admin_count=5, upload_link_expiry_days=None)
for label, cfg in (("before", before), ("after", after)):
    fails = [f"{k}={cfg[k]}" for k, ok in rules.items() if not ok(cfg[k])]
    print(f"{label}: {len(rules) - len(fails)}/{len(rules)} settings meet baseline; fails {fails}")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
before: 4/7 settings meet baseline; fails ['session_timeout_min=480', 'upload_link_expiry_days=None', 'admin_count=5']
after: 7/7 settings meet baseline; fails []
```

### 4.2 Reading the results

The lab reports four of seven settings meeting the baseline. Three do not: sessions stay open for eight hours instead of thirty minutes, five people hold administrator rights instead of two, and upload links never expire. Leah notes that the earlier link-sharing fix closed the public access issue but did not set expiry. Reading results carefully matters, because a pass on one setting may hide a related weakness that the baseline describes separately. She writes each gap in her notes with the setting name, the current value and the baseline value, so the vendor can act on it.

### 4.3 Prioritising actions

Leah ranks the three gaps. Administrator rights come first, because any of five accounts could change security settings or export all loan documents. Link expiry is second, since old links could leak if forwarded. Session timeout is third, as branch PCs already lock after five minutes. For each action she names an owner and a date and asks the vendor which changes can be made through settings. All three can, and the vendor confirms they will not disrupt loan processing.

### 4.4 Verifying the fix

After the changes, Leah reruns the lab with an updated export. All seven settings now meet the baseline. She keeps both outputs as evidence, dated, in the review folder. Felix stresses that verification closes the loop: a change requested is not a change made until a check confirms it. He also suggests rerunning the check every quarter, because vendor updates and staff changes can quietly undo settings over time. Leah records the date of each run and the export file used, so the evidence can be traced. She adds the quarterly check to the operations calendar with her own name as owner.

### 4.5 Synthesis and plan

To finish the course, Leah writes a one-page plan for Saltmarsh's next six months: individual email accounts as decided in chapter 1, a quarterly baseline check of the loan system, a tested break-glass procedure for the identity provider, an annual update of the architecture overview and vendor security questions for every new supplier. Each item links to a principle or finding from the course. Her manager approves the plan. Felix notes that the course's aim was not expertise, but a working habit of mapping, checking and recording that Leah can keep using.

### Worked example

Leah runs a baseline lab on synthetic loan settings, finds three gaps, prioritises and fixes them, verifies with a rerun and writes a six-month plan.

> **Synthetic case.** Settings, vendor and plan are synthetic.

### Errors and limits

Baselines cover only listed settings. Quarterly checks lapse without an owner.

### Exercises

- **EX039 — Baseline items.** Name three items in the lab's baseline. *Rubric:* 3 = multi-factor sign-in, session timeout, no shared accounts, link expiry, audit logging, two admins;; 2 = two;; 1 = vague;; 0 = none.
- **EX040 — First result.** How many settings met the baseline at first? *Rubric:* 3 = 4 of 7;; 2 = four;; 1 = vague;; 0 = none.
- **EX041 — Session gap.** What session setting failed? *Rubric:* 3 = sessions stayed open eight hours instead of thirty minutes;; 2 = eight hours;; 1 = vague;; 0 = none.
- **EX042 — Admin gap.** How many people held administrator rights? *Rubric:* 3 = five instead of two;; 2 = five;; 1 = two;; 0 = none.
- **EX043 — Hidden weakness.** What did the earlier link fix not cover? *Rubric:* 3 = link expiry;; 2 = expiry;; 1 = vague;; 0 = none.
- **EX044 — Top priority.** Why are administrator rights the top priority? *Rubric:* 3 = any of five accounts could change settings or export all documents;; 2 = broad power;; 1 = vague;; 0 = none.
- **EX045 — Timeout rank.** Why is session timeout ranked third? *Rubric:* 3 = branch PCs already lock after five minutes;; 2 = PC lock;; 1 = vague;; 0 = none.
- **EX046 — Second run.** How many settings passed after the changes? *Rubric:* 3 = 7 of 7;; 2 = all;; 1 = vague;; 0 = none.
- **EX047 — Change made.** When is a requested change truly made, according to Felix? *Rubric:* 3 = when a check confirms it;; 2 = verified;; 1 = when requested;; 0 = none.
- **EX048 — Quarterly rerun.** Why rerun the check each quarter? *Rubric:* 3 = updates and staff changes can undo settings;; 2 = drift;; 1 = vague;; 0 = none.
- **EX049 — Plan items.** Name two items in Leah's six-month plan. *Rubric:* 3 = individual email, quarterly baseline, break-glass test, overview update, supplier questions;; 2 = one;; 1 = vague;; 0 = none.
- **EX050 — Course aim.** What was the course's aim, according to Felix? *Rubric:* 3 = a working habit of mapping, checking and recording;; 2 = habit;; 1 = expertise;; 0 = none.

### Synthesis

A guided baseline check, prioritised fixes, verification and a short plan turn a month of learning into lasting practice.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Leah Brennan, Felix Ortega, Northgate Learning Centre, Saltmarsh Community Credit Union and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The overall arrangement of protections across people, processes and technology, designed to work together.

**EX002.** Because decisions made one at a time without a plan often contradict one another.

**EX003.** Tellers can view member accounts but cannot change interest rates.

**EX004.** New staff accounts start with no access and receive roles only on approval.

**EX005.** Large transfers need approval from a second staff member.

**EX006.** Because nobody can tell which teller sent which message.

**EX007.** The app-based second factor for online banking, which members find easy.

**EX008.** Context, options, the choice, reasons, consequences and when to revisit.

**EX009.** Individual accounts with access to a shared inbox.

**EX010.** Because member queries must be traceable to the person who answered them.

**EX011.** From systems that are each reasonable alone but unsafe in combination.

**EX012.** Psychological acceptability and separation of privilege, since extra approvals add friction.

**EX013.** So others can understand and challenge the reasoning later, even after the author leaves.

**EX014.** The core banking system run by a service bureau and the card processor.

**EX015.** Attempting attacks or accessing member files.

**EX016.** The chief executive and the loan system owner.

**EX017.** That reading configuration screens would not breach the support contract.

**EX018.** She used a vendor test application with fictitious details.

**EX019.** That no member information appeared in them.

**EX020.** Signs of an existing break-in, member documents exposed to the internet and any service disruption.

**EX021.** Because incident response needs different skills and authority than a review.

**EX022.** Document uploads were in a cloud folder viewable by anyone with the link.

**EX023.** No access by unknown parties.

**EX024.** After the review is accepted.

**EX025.** Within the hour after Leah reported it.

**EX026.** A new source of data exposure.

**EX027.** The core banking system run by the service bureau.

**EX028.** A member uploads documents, the loan system stores them, an officer reviews, core banking pays and the member is emailed.

**EX029.** Because each relies on another party's controls and assumptions about what was checked.

**EX030.** Its role, the data it holds, the contract owner and what happens if it fails.

**EX031.** Six services.

**EX032.** Four services.

**EX033.** A securely stored offline break-glass administrator account with a tested procedure.

**EX034.** Its contractual recovery commitments plus a manual procedure for urgent branch withdrawals.

**EX035.** It would add a supplier holding transaction data and another identity provider dependency.

**EX036.** It asked the vendor security questions before signing.

**EX037.** The first time it shapes a decision before money is spent.

**EX038.** It becomes outdated unless it is updated as systems change.

**EX039.** Multi-factor staff sign-in, session timeouts and expiring upload links, among others.

**EX040.** Four of seven.

**EX041.** Sessions stayed open for eight hours instead of thirty minutes.

**EX042.** Five people, instead of the baseline of two.

**EX043.** It removed public access but did not set link expiry.

**EX044.** Because any of the five accounts could change security settings or export all loan documents.

**EX045.** Because branch PCs already lock after five minutes.

**EX046.** All seven settings met the baseline.

**EX047.** Only when a check confirms it.

**EX048.** Because vendor updates and staff changes can quietly undo settings.

**EX049.** A quarterly baseline check of the loan system and a tested break-glass procedure, among others.

**EX050.** A working habit of mapping, checking and recording, rather than expertise.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
