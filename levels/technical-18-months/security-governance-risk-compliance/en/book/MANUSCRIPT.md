# Security Governance, Risk and Compliance: Technical Course

- Language: English (`en`); course 051, Technical course (18 months).
- Editorial state: **published**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical students who configure, check and document the controls behind a small business's GRC programme.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs check JSON configuration exports against a baseline, count failed sign-ins, verify firewall rules against an approved list and check certificate expiry on synthetic data. Any testing happens only in isolated virtual labs; standards are cited by edition and paraphrased, and nothing here is a real audit, attestation or legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one technical student through eighteen months centred on a building supplies retailer: services, networks, identities and scripting, scope and evidence, the GRC model, logs, failure modes, methods, configuration, verification, labs, troubleshooting, automation, provider dependencies, documentation and a supervised project. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Amina Yusuf** | Technical student | Invented |
| **Ms. Clara Bell** | Instructor | Invented |
| **Dunmore Technical College** | Fictional college | Invented |
| **Fenwick Building Supplies** | Fictional retailer, 6 branches, 180 staff, online shop | Invented |

### Core sources

NIST [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29) and its small business resources; PCI DSS v4.0; AICPA trust services criteria (SOC 2). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe the services a retail business runs; (2) identify which components support each service; (3) record owners for governance.

### 1.1 Fenwick's services

Amina Yusuf is a student on the technical course at the fictional Dunmore Technical College. Her instructor, Ms. Clara Bell, uses one running case: the fictional Fenwick Building Supplies, with six branches, one hundred and eighty staff, an online shop and card terminals at every till. Amina lists Fenwick's services: in-branch sales, the online shop, deliveries, supplier ordering and payroll. Each service relies on computers, software, networks and people, and governance must know these links to protect what matters. Payroll, for example, has no customers watching it, yet a failure there would affect all one hundred and eighty staff at once.

### 1.2 Components

For each service Amina lists components. In-branch sales rely on till computers, card terminals, the point-of-sale software and the branch network. The online shop relies on a hosted web platform, a payment gateway and the stock database. Deliveries rely on tablets and a route planning service. She learns that drawing these links shows which single component could stop several services, such as the stock database, which both the shop and branches need. Ms. Bell asks her to mark the stock database on the diagram, since an outage there would stop both the online shop and every branch till.

### 1.3 Owners

Amina records an owner for each service and component. The sales director owns in-branch sales; the e-commerce manager owns the online shop; the IT technician team owns tills, networks and the stock database. Two components, the route planning service and the branch Wi-Fi, have no clear owner. She learns that unowned components are often where problems go unnoticed, so assigning owners is one of the first and simplest governance tasks. She adds the route planning service and branch Wi-Fi to the IT lead's agenda so owners can be agreed.

### Worked example

Amina maps five Fenwick services to their components, identifies the stock database as shared and finds two unowned components.

> **Synthetic case.** Dunmore, Fenwick and all details are synthetic.

### Errors and limits

Maps omit informal tools. Owners may not accept responsibility.

### Exercises

- **EX001 — Shared component.** Which component supports both the shop and branches? *Rubric:* 3 = the stock database;; 2 = stock database, hedged with another option;; 1 = vague;; 0 = none.
- **EX002 — Unowned items.** Which two components had no owner? *Rubric:* 3 = route planning service and branch Wi-Fi;; 2 = two;; 1 = vague;; 0 = none.
- **EX003 — Why owners.** Why assign owners early? *Rubric:* 3 = unowned components are where problems go unnoticed;; 2 = visibility;; 1 = vague;; 0 = none.
- **EX004 — Service list.** Name three Fenwick services. *Rubric:* 3 = in-branch sales, online shop, deliveries;; 2 = services;; 1 = vague;; 0 = none.

### Synthesis

Mapping services to components and owners is the technical foundation of governance.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) describe a branch network design; (2) identify card payment network requirements; (3) document network changes.

### 2.1 Branch networks

Each Fenwick branch has a network for tills and card terminals, office computers and a guest Wi-Fi for trade customers. Amina learns that these should be separated so a problem in one cannot easily spread to another. She checks two branches: one has separate segments; the other connects everything to one switch. She records the difference and learns that branches built at different times often vary, which governance must find and fix. The branch with one switch lets a compromised guest device reach the tills, so she records it as the higher priority of the two.

### 2.2 Card payment requirements

Card terminals and the till software handle payment card data, which brings PCI DSS v4.0 requirements. Amina learns that keeping payment systems on their own segment, with only necessary connections allowed, reduces the number of systems in scope. She lists the connections the payment segment needs: to the payment gateway for authorisation and to IT management for updates. Anything else should be blocked, and the list itself becomes evidence for assessments. A connection from office computers to the payment segment, for instance, would bring those computers into PCI DSS scope as well.

### 2.3 Documenting changes

When a branch technician adds a new device or rule, the change should be recorded: what, why, who approved and when. Amina finds that branch changes are often made by phone with no record. She drafts a simple change form and explains that without records, nobody can tell whether the network still matches its design. She learns that change documentation is a basic control supporting both security and troubleshooting. A change form with fields for what, why, approver and date takes a technician only a minute on the phone call itself.

### Worked example

Amina compares two branch networks, lists required payment connections and drafts a change record form.

> **Synthetic case.** Branch networks are synthetic; PCI DSS v4.0 is real.

### Errors and limits

Diagrams drift. Change forms get skipped in emergencies.

### Exercises

- **EX005 — Unsegmented branch.** What problem did the second branch have? *Rubric:* 3 = everything on one switch without segments;; 2 = flat network;; 1 = vague;; 0 = none.
- **EX006 — Payment connections.** Which connections does the payment segment need? *Rubric:* 3 = payment gateway and IT management;; 2 = two;; 1 = internet;; 0 = none.
- **EX007 — Change record.** What should a change record capture? *Rubric:* 3 = what, why, who approved and when;; 2 = four;; 1 = vague;; 0 = none.
- **EX008 — Scope reduction.** How does segmentation help with PCI DSS? *Rubric:* 3 = reduces systems in scope;; 2 = scope;; 1 = vague;; 0 = none.

### Synthesis

Segmented, documented networks keep payment scope small and designs verifiable.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) manage user accounts on business systems; (2) apply least privilege on computers; (3) control administrator access.

### 3.1 User accounts

Amina learns how Fenwick creates accounts for staff on office computers, tills and cloud services. Each person should have their own account so actions can be traced. At tills, staff share a till login, which makes it impossible to know who processed a refund. She recommends individual till logins with quick card sign-in. She learns that individual accounts are the basis of accountability, and that shared accounts usually exist because individual ones were inconvenient. Individual logins would also let a branch manager see which staff member processed each refund when a till total does not match.

### 3.2 Least privilege

Office computers give every user local administrator rights so they can install software. Amina explains that this lets malware install itself with full control. She proposes removing local administrator rights and providing a software request process. She tests the change on three computers first, finding that one accounting program needs a setting adjusted. She learns that least privilege must be introduced carefully with testing, so that work continues smoothly. Her three-computer pilot found the accounting program issue before it could stop a whole office.

### 3.3 Administrator access

IT technicians use administrator accounts for maintenance. Amina recommends separate administrator accounts used only for admin tasks, with multi-factor authentication and logging. She notes that if a technician's everyday account is compromised, attackers should not gain admin rights automatically. She learns that controlling administrator access is one of the most effective security measures, because most serious attacks depend on gaining those rights. Logging admin sessions also gives the IT lead a record to check when a setting changes unexpectedly. Every admin action thus carries a name the IT lead can review.

### Worked example

Amina replaces shared till logins, removes local admin rights after testing and separates administrator accounts with MFA.

> **Synthetic case.** Accounts and systems are synthetic.

### Errors and limits

Removing rights can break software. Card sign-in needs hardware.

### Exercises

- **EX009 — Shared till problem.** Why is a shared till login a problem? *Rubric:* 3 = cannot trace who processed a refund;; 2 = accountability;; 1 = vague;; 0 = none.
- **EX010 — Admin rights risk.** Why remove local administrator rights? *Rubric:* 3 = malware could install itself with full control;; 2 = malware;; 1 = vague;; 0 = none.
- **EX011 — Separate admin.** Why use separate administrator accounts? *Rubric:* 3 = compromise of an everyday account should not give admin rights;; 2 = separation;; 1 = vague;; 0 = none.
- **EX012 — Testing first.** Why test removal of rights on three computers first? *Rubric:* 3 = to find software that breaks;; 2 = pilot;; 1 = vague;; 0 = none.

### Synthesis

Individual accounts, least privilege and separate admin access underpin technical governance.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) read structured data formats such as JSON; (2) check configurations against a baseline with a script; (3) report deviations clearly.

### 4.1 Data formats

Amina learns that systems export configuration and status data in formats such as CSV and JSON. JSON represents records as named fields, which makes it easy to read in Python with the standard json module. Fenwick's device management tool exports laptop settings as JSON. She learns that understanding data formats lets technicians check many devices quickly instead of clicking through each one, which saves time and reduces mistakes. In the next lab, the JSON export lets one short script check all four laptops against the baseline at once.

### 4.2 Baseline check

Fenwick's baseline requires disk encryption, a screen lock within ten minutes, automatic updates and no local administrator rights. The lab checks four laptops. FW-LT01 meets the baseline. FW-LT02 lacks disk encryption. FW-LT03 has a thirty-minute screen lock and local administrator rights. FW-LT04 has automatic updates turned off. A shorter screen lock, such as five minutes, is accepted because it is stricter than the baseline. Ms. Bell asks the class why FW-LT03 fails twice, and Amina points to its thirty-minute screen lock and its local administrator rights.

### Lab — Checking laptop settings against a baseline

```python
"""Check laptop configuration exports (JSON) against a baseline (synthetic Fenwick data)."""
import json
baseline = {"disk_encryption": True, "screen_lock_minutes": 10, "auto_update": True, "local_admin": False}
export = json.loads("""[
 {"host": "FW-LT01", "disk_encryption": true, "screen_lock_minutes": 10, "auto_update": true, "local_admin": false},
 {"host": "FW-LT02", "disk_encryption": false, "screen_lock_minutes": 10, "auto_update": true, "local_admin": false},
 {"host": "FW-LT03", "disk_encryption": true, "screen_lock_minutes": 30, "auto_update": true, "local_admin": true},
 {"host": "FW-LT04", "disk_encryption": true, "screen_lock_minutes": 5, "auto_update": false, "local_admin": false}]""")
for h in export:
    bad = []
    for k, v in baseline.items():
        if k == "screen_lock_minutes":
            if h[k] > v: bad.append(f"{k}={h[k]}")
        elif h[k] != v: bad.append(f"{k}={h[k]}")
    print(h["host"], "OK" if not bad else "DEVIATION " + ", ".join(bad))
```

Run with `python3 lab_config.py`. Verified output:

```text
FW-LT01 OK
FW-LT02 DEVIATION disk_encryption=False
FW-LT03 DEVIATION screen_lock_minutes=30, local_admin=True
FW-LT04 DEVIATION auto_update=False
```

### 4.3 Reporting deviations

Amina reports each deviation with the laptop name and the failing setting, then asks the owners why. FW-LT02 was set up before encryption was standard. FW-LT03 belongs to a manager who asked for admin rights months ago. FW-LT04 had updates paused during a software problem and never resumed. She learns that each deviation has a story, and that recording the cause helps prevent the same deviation recurring on other devices. FW-LT04's paused updates, for example, suggest adding a review date whenever updates are paused for a software problem.

### Worked example

Amina reads a JSON export, finds three of four laptops deviating from the baseline and records the cause of each.

> **Synthetic case.** Laptop data are synthetic.

### Errors and limits

Exports may be out of date. Baselines need review.

### Exercises

- **EX013 — JSON benefit.** Why are JSON exports useful for checks? *Rubric:* 3 = named fields are easy to read in scripts;; 2 = structure;; 1 = vague;; 0 = none.
- **EX014 — Compliant laptop.** Which laptop met the baseline? *Rubric:* 3 = FW-LT01;; 2 = LT01;; 1 = LT03;; 0 = none.
- **EX015 — Two deviations.** Which laptop had two deviations? *Rubric:* 3 = FW-LT03, 30-minute lock and local admin;; 2 = LT03;; 1 = vague;; 0 = none.
- **EX016 — Stricter setting.** Why is FW-LT04's five-minute lock acceptable? *Rubric:* 3 = it is stricter than the ten-minute baseline;; 2 = stricter;; 1 = vague;; 0 = none.

### Synthesis

Scripts reading structured exports turn baseline checks into fast, explained findings.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) define the scope of a security task; (2) collect evidence properly; (3) respect authorisation limits.

### 5.1 Scope

Before any technical security work, Amina learns to agree scope in writing: which systems, which activities and which times are allowed. For her placement at Fenwick, the scope allows reading configuration exports, reviewing logs and checking firewall rules, but not testing for vulnerabilities on live systems. Ms. Bell stresses that working outside scope, even with good intentions, can breach rules or laws and damage trust. Her written scope also lets her answer quickly when someone at Fenwick asks her to test something not on the list.

### 5.2 Evidence

Amina learns how to collect evidence: record what was checked, when, by whom and how, and keep the original output such as an export file or screenshot. She names files consistently and stores them in a folder where they cannot be changed after collection. She learns that evidence must allow someone else to see exactly what she saw, which matters for audits and for fixing problems later. An export kept unchanged in a read-only folder can be compared later with a fresh export to see what changed.

### 5.3 Authorisation limits

During her work, Amina notices a server that appears to allow remote desktop from the internet. Testing it would be outside her scope. She reports it to the IT lead with the evidence she already has: the firewall rule showing the connection. The IT lead investigates and closes it. She learns that the correct response to something outside scope is to report it, not to investigate it herself without permission. The firewall rule she already had in hand was enough evidence for the IT lead to act without her probing the server.

### Worked example

Amina works under a written scope, collects traceable evidence and reports an out-of-scope concern instead of testing it.

> **Synthetic case.** Scope and findings are synthetic.

### Errors and limits

Scopes can be unclear. Evidence folders need access control.

### Exercises

- **EX017 — Excluded activity.** Which activity was outside Amina's scope? *Rubric:* 3 = vulnerability testing of live systems;; 2 = testing;; 1 = vague;; 0 = none.
- **EX018 — Evidence record.** What should an evidence record include? *Rubric:* 3 = what, when, who, how and original output;; 2 = record;; 1 = vague;; 0 = none.
- **EX019 — Out-of-scope response.** What should you do on spotting something outside scope? *Rubric:* 3 = report it with existing evidence;; 2 = report;; 1 = test it;; 0 = none.
- **EX020 — Unchangeable storage.** Why store evidence where it cannot be changed? *Rubric:* 3 = so others can trust it shows exactly what was seen;; 2 = integrity;; 1 = vague;; 0 = none.

### Synthesis

Written scope, careful evidence and respect for limits make technical security work trustworthy.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Security governance, risk and compliance: system model

### Learning outcomes

You will (1) explain how GRC fits with technical work; (2) model Fenwick's governance roles; (3) connect technical tasks to policies and risks.

### 6.1 GRC and technicians

Amina learns that governance sets rules and priorities, risk management decides what matters most and compliance checks obligations are met. Technicians make these work: they configure systems, collect evidence and fix problems. Ms. Bell explains that understanding GRC helps technicians see why tasks matter. A baseline check is not busywork; it supports a policy, reduces a risk and produces evidence an assessor may ask for. Ms. Bell gives an example: the encryption baseline check reduces the lost laptop risk and answers a question the card payment assessor may ask.

### 6.2 Fenwick's roles

Fenwick's finance director is accountable for security. An IT lead manages a team of three technicians. Branch managers own local tasks such as confirming staff leavers. An external assessor checks card payment compliance each year. Amina draws these roles and the flow of information between them, noting that technicians report issues to the IT lead, who reports risks to the finance director. The drawing also shows that the external assessor depends on evidence that technicians produce, such as firewall rule lists.

### 6.3 Connecting tasks

Amina builds a table linking technical tasks to policies, risks and obligations. Laptop encryption links to the data protection policy and the lost device risk. Firewall rule reviews link to the network policy and card payment obligations. Log reviews link to the monitoring policy and account misuse risk. She learns that this table helps technicians prioritise when time is short and explains to managers why technical work deserves resources. When time is short, for instance, the firewall review ranks above a log review because it also carries card payment obligations.

### Worked example

Amina explains GRC's link to technical work, models Fenwick's roles and maps technical tasks to policies, risks and obligations.

> **Synthetic case.** Fenwick's roles are synthetic.

### Errors and limits

Tables simplify complex links. Roles change.

### Exercises

- **EX021 — Baseline purpose.** Why is a baseline check not busywork? *Rubric:* 3 = it supports a policy, reduces a risk and produces evidence;; 2 = purpose;; 1 = vague;; 0 = none.
- **EX022 — Accountable person.** Who is accountable for security at Fenwick? *Rubric:* 3 = the finance director;; 2 = finance director, hedged with another option;; 1 = IT lead;; 0 = none.
- **EX023 — Firewall links.** Which policy and obligation do firewall reviews support? *Rubric:* 3 = network policy and card payment obligations;; 2 = links;; 1 = vague;; 0 = none.
- **EX024 — Table use.** How does the task table help technicians? *Rubric:* 3 = prioritise when time is short;; 2 = priorities;; 1 = vague;; 0 = none.

### Synthesis

Linking technical tasks to policies, risks and obligations shows why they matter.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Security governance, risk and compliance: data and telemetry

### Learning outcomes

You will (1) use logs as governance data; (2) count and flag unusual events; (3) decide what to do with alerts.

### 7.1 Logs as data

Systems record events such as sign-ins, changes and errors. Amina learns that logs are governance data: they show whether controls work and whether something unusual happened. Fenwick's cloud services produce sign-in logs with time, result and account. She learns to read them with a script and that keeping logs for a defined period is often required by policy and by payment card rules, so retention must be planned. Ms. Bell notes that a retention period chosen without checking payment card rules may delete logs that an assessor later asks for.

### 7.2 Counting failures

The lab reads twelve sign-in log lines and counts failures per account. The admin account has seven failures in a few minutes and is flagged because it exceeds five. j.park has two failures followed by a success, likely a mistyped password. s.ali has one failure. Three accounts had failures in total. Amina notes that repeated failures on an administrator account could indicate someone guessing the password. j.park's success straight after two failures fits a typing error far better than an attack on that account.

### Lab — Counting failed sign-ins per account

```python
"""Count failed sign-ins per account from synthetic log lines; flag accounts above 5."""
from collections import Counter
log = """2026-09-14T08:01 FAIL j.park
2026-09-14T08:02 FAIL j.park
2026-09-14T08:02 OK j.park
2026-09-14T09:10 FAIL admin
2026-09-14T09:10 FAIL admin
2026-09-14T09:11 FAIL admin
2026-09-14T09:11 FAIL admin
2026-09-14T09:12 FAIL admin
2026-09-14T09:12 FAIL admin
2026-09-14T09:13 FAIL admin
2026-09-14T10:30 FAIL s.ali
2026-09-14T10:31 OK s.ali"""
c = Counter(l.split()[2] for l in log.splitlines() if " FAIL " in l)
for a, n in c.most_common(): print(f"{a}: {n} failures{'  ALERT' if n > 5 else ''}")
print(f"lines {len(log.splitlines())}; accounts with failures {len(c)}")
```

Run with `python3 lab_logs.py`. Verified output:

```text
admin: 7 failures  ALERT
j.park: 2 failures
s.ali: 1 failures
lines 12; accounts with failures 3
```

### 7.3 Acting on alerts

Amina reports the admin account alert to the IT lead. They check and find the failures came from an unknown internet address. The account already had multi-factor authentication, so the guesses failed. The IT lead blocks the address and renames the generic admin account. Amina learns that alerts need a response procedure and that context, such as source address and whether other controls held, determines how serious an alert is. Renaming the generic admin account also makes it a less obvious target for the same guessing.

### Worked example

Amina counts sign-in failures, flags seven on the admin account and supports a response that blocks the source and renames the account.

> **Synthetic case.** Log lines are synthetic.

### Errors and limits

Simple thresholds miss slow attacks. Logs can be incomplete.

### Exercises

- **EX025 — Log retention.** Why must log retention be planned? *Rubric:* 3 = policy and card rules often require it;; 2 = requirements;; 1 = vague;; 0 = none.
- **EX026 — Flagged account.** Which account was flagged and why? *Rubric:* 3 = admin, 7 failures above 5;; 2 = admin;; 1 = j.park;; 0 = none.
- **EX027 — j.park reading.** How did Amina interpret j.park's failures? *Rubric:* 3 = likely a mistyped password, followed by success;; 2 = typo;; 1 = vague;; 0 = none.
- **EX028 — Response actions.** What actions followed the alert? *Rubric:* 3 = block the address and rename the admin account;; 2 = two;; 1 = vague;; 0 = none.

### Synthesis

Logs become governance data when counted, flagged and acted on with context.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security governance, risk and compliance: failure modes

### Learning outcomes

You will (1) identify how technical controls fail; (2) plan detection for each failure; (3) record failure modes in the risk register.

### 8.1 How controls fail

Amina learns that controls can fail in many ways. Backups can run but miss files. Updates can be paused and forgotten. Firewall rules can be added and never removed. Accounts can stay active after people leave. Certificates can expire. She writes each as a failure mode: what goes wrong, how it would show and what the impact would be. She learns that thinking about failure in advance makes controls more reliable. For backups, the failure mode reads: the job runs, misses files and the gap shows only during a restore.

### 8.2 Detecting failure

For each failure mode, Amina asks how Fenwick would notice. Missed files would show only in restore tests. Paused updates would show in compliance reports. Stale firewall rules would show in rule reviews. Active leaver accounts would show in reconciliation. Expiring certificates would show in expiry checks. She learns that some failures are silent until something breaks, so regular checks must be scheduled to find them before customers or attackers do. Missed backup files, for instance, will stay invisible until a restore test, which is why restore tests appear later in her schedule.

### 8.3 Register entries

Amina records the main failure modes in Fenwick's risk register with owners and detection checks. For example, the certificate expiry failure mode is owned by the IT lead, with a monthly expiry check. She learns that recording failure modes makes them part of governance, so checks are scheduled and reviewed rather than relying on someone remembering. Linking each failure mode to a named check also tells an assessor which evidence to ask for. If a monthly check is skipped, the missing entry shows up when the register is reviewed, before a certificate actually expires.

### Worked example

Amina lists five control failure modes, plans detection for each and records them in the register with owners.

> **Synthetic case.** Failure modes are synthetic.

### Errors and limits

Lists miss novel failures. Checks may fail too.

### Exercises

- **EX029 — Backup failure.** How would missed backup files be detected? *Rubric:* 3 = restore tests;; 2 = restore;; 1 = vague;; 0 = none.
- **EX030 — Silent failures.** Why must checks be scheduled? *Rubric:* 3 = some failures are silent until something breaks;; 2 = silent;; 1 = vague;; 0 = none.
- **EX031 — Certificate owner.** Who owns the certificate expiry failure mode? *Rubric:* 3 = the IT lead;; 2 = IT lead, hedged with another option;; 1 = vague;; 0 = none.
- **EX032 — Failure mode parts.** What three things does each failure mode describe? *Rubric:* 3 = what goes wrong, how it shows, impact;; 2 = three;; 1 = vague;; 0 = none.

### Synthesis

Planning detection for each failure mode keeps controls reliable.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Security governance, risk and compliance: tools and methods

### Learning outcomes

You will (1) use a simple risk method; (2) apply a control checklist; (3) choose tools suited to a small team.

### 9.1 Risk method

Fenwick uses a simple method: list risks, rate likelihood and impact from one to five, multiply for a score and treat the highest first. Amina helps rate risks for the online shop. She learns the method is quick but has limits: very different risks can get the same score, and a rare but severe event can look low. She notes these limits and suggests discussing the top risks in more detail rather than relying only on scores. A one-in-twenty chance of a payment gateway breach, for example, may score lower than frequent shop slowdowns despite a far worse impact.

### 9.2 Checklists

Amina uses a control checklist based on the NIST CSF 2.0 small business resources to review Fenwick's basics: inventory, accounts, updates, backups, logging and incident response. Each item is marked in place, partly in place or missing, with evidence. The checklist reveals that incident response is missing a written plan. She learns that checklists help small teams cover essentials without needing deep expertise in every area. The missing incident response plan becomes a register entry with an owner rather than a note on the checklist.

### 9.3 Choosing tools

Fenwick's small IT team cannot run complex governance software. Amina recommends using tools they already have: the ticketing system for tasks, spreadsheets with validation for the register and short scripts for checks. She learns that the best tool is one the team will actually use and maintain, and that adding software without people to run it often increases risk rather than reducing it. Ms. Bell observes that a spreadsheet with validation, kept current by three technicians, gives Fenwick more than an unused governance platform.

### Worked example

Amina rates shop risks with a simple method, reviews basics with a CSF-based checklist and recommends existing tools.

> **Synthetic case.** Ratings and checklist results are synthetic; CSF 2.0 resources are real.

### Errors and limits

Scores hide severity. Checklists miss context.

### Exercises

- **EX033 — Method limit.** What is one limit of the multiply-scores method? *Rubric:* 3 = rare severe events can look low;; 2 = severity;; 1 = vague;; 0 = none.
- **EX034 — Missing item.** What did the checklist reveal as missing? *Rubric:* 3 = a written incident response plan;; 2 = incident plan;; 1 = vague;; 0 = none.
- **EX035 — Tool choice.** What tools did Amina recommend? *Rubric:* 3 = ticketing, validated spreadsheets and short scripts;; 2 = existing tools;; 1 = vague;; 0 = none.
- **EX036 — Checklist ratings.** How is each checklist item marked? *Rubric:* 3 = in place, partly in place or missing, with evidence;; 2 = three states;; 1 = vague;; 0 = none.

### Synthesis

Simple methods, checklists and familiar tools suit small technical teams.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Security governance, risk and compliance: control configuration

### Learning outcomes

You will (1) configure controls to meet policy; (2) document configuration decisions; (3) test before and after changes.

### 10.1 Configuring to policy

Amina helps configure controls to match Fenwick's policies. She enables multi-factor authentication for all cloud accounts, sets backup jobs to include the stock database and online shop data, and configures alerts for repeated sign-in failures. For each, she checks the policy requirement and chooses settings that meet it. She learns that configuration is where policy becomes real, and that small setting choices can make a large difference. Including the stock database in backups, for example, protects the one component that both the shop and the branches depend on.

### 10.2 Documenting decisions

Some settings involve trade-offs. Amina sets the sign-in alert threshold at five failures within ten minutes. Lower would cause many false alarms from mistyped passwords; higher might miss guessing. She records the decision and reason in the configuration notes. She learns that documenting why a setting was chosen helps future technicians adjust it sensibly rather than guessing or reverting it without understanding. If false alarms later prove frequent, the recorded reason shows exactly which trade-off to revisit. The note sits beside the setting itself, so it is found by whoever next opens the configuration.

### 10.3 Testing changes

Before changing backup settings, Amina tests restore of the current backup. After the change, she runs a new backup and restores sample files from the stock database. Both tests pass. She records the results. She learns that testing before and after a change shows both that the old state worked and that the change did not break anything, which provides useful evidence of a controlled change. The before-and-after restore results go into the change record as evidence that the backup change was controlled.

### Worked example

Amina configures MFA, backups and alerts to policy, documents the alert threshold reasoning and tests backups before and after change.

> **Synthetic case.** Configurations are synthetic.

### Errors and limits

Thresholds need tuning. Tests sample only some files.

### Exercises

- **EX037 — Threshold choice.** What alert threshold did Amina set? *Rubric:* 3 = five failures within ten minutes;; 2 = 5 in 10;; 1 = vague;; 0 = none.
- **EX038 — Threshold trade-off.** Why not set the threshold lower? *Rubric:* 3 = many false alarms from mistyped passwords;; 2 = false alarms;; 1 = vague;; 0 = none.
- **EX039 — Before-after tests.** Why test both before and after a change? *Rubric:* 3 = shows old state worked and change broke nothing;; 2 = baseline;; 1 = vague;; 0 = none.
- **EX040 — Backup scope.** Which data were added to backup jobs? *Rubric:* 3 = the stock database and online shop data;; 2 = two;; 1 = vague;; 0 = none.

### Synthesis

Controls become real through documented configuration and before-and-after testing.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Security governance, risk and compliance: verification

### Learning outcomes

You will (1) verify firewall rules against an approved list; (2) investigate unapproved rules; (3) record verification results.

### 11.1 Approved rules

Fenwick keeps a list of approved firewall rules for its branch network: who may connect to what, on which port. Amina learns that verification compares the actual configuration with the approved list. Differences mean either the list is out of date or the firewall has unapproved rules. PCI DSS v4.0 expects regular review of network security controls, and verification is how that review becomes evidence. Each difference is then resolved one way or the other: the list is updated with approval, or the rule is removed.

### 11.2 Finding unapproved rules

The lab compares five firewall rules with three approved ones. Three match. Two are unapproved: one allows remote desktop from anywhere to the payment terminal segment on port 3389, and another allows office computers to reach the payment gateway. Amina treats the first as urgent because it exposes payment systems to the internet. She reports both to the IT lead with the evidence. Port 3389 open to the internet on the payment terminal segment is the kind of exposure that PCI DSS segmentation is meant to prevent.

### Lab — Verifying firewall rules against an approved list

```python
"""Verify firewall rules against an approved list (synthetic branch firewall)."""
approved = {("any", "web-shop", 443), ("branch-pos", "payment-gw", 443), ("it-admin", "branch-pos", 22)}
rules = [("any", "web-shop", 443), ("branch-pos", "payment-gw", 443), ("it-admin", "branch-pos", 22),
         ("any", "branch-pos", 3389), ("office", "payment-gw", 443)]
for r in rules: print(r, "approved" if r in approved else "UNAPPROVED")
print(f"rules {len(rules)}; unapproved {sum(r not in approved for r in rules)}")
```

Run with `python3 lab_rules.py`. Verified output:

```text
('any', 'web-shop', 443) approved
('branch-pos', 'payment-gw', 443) approved
('it-admin', 'branch-pos', 22) approved
('any', 'branch-pos', 3389) UNAPPROVED
('office', 'payment-gw', 443) UNAPPROVED
rules 5; unapproved 2
```

### 11.3 Investigating and recording

The IT lead finds that a support company added the remote desktop rule for a one-off repair and never removed it. The office rule was added when a manager needed to check payments, which should be done through the gateway's web portal instead. Both rules are removed. Amina records the verification, findings, causes and fixes. She learns that verification finds what change control missed, so both controls are needed. The support company's rule also shows why the contract should require temporary rules to be removed after work.

### Worked example

Amina verifies five firewall rules, finds two unapproved including an urgent remote desktop exposure and records causes and fixes.

> **Synthetic case.** Rules are synthetic; PCI DSS v4.0 is real.

### Errors and limits

Approved lists can be wrong. Verification is periodic.

### Exercises

- **EX041 — Unapproved count.** How many rules were unapproved? *Rubric:* 3 = two;; 2 = 2;; 1 = three;; 0 = none.
- **EX042 — Urgent rule.** Which unapproved rule was urgent? *Rubric:* 3 = remote desktop from anywhere to the payment segment;; 2 = RDP;; 1 = vague;; 0 = none.
- **EX043 — RDP cause.** Why did the remote desktop rule exist? *Rubric:* 3 = a support company added it for a one-off repair;; 2 = support;; 1 = vague;; 0 = none.
- **EX044 — Two controls.** Why are both change control and verification needed? *Rubric:* 3 = verification finds what change control missed;; 2 = complementary;; 1 = vague;; 0 = none.

### Synthesis

Verification against approved lists finds risky drift that change control alone misses.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) practise a control test in a safe lab; (2) follow a written test procedure; (3) compare results with expectations.

### 12.1 Safe lab

In the contained laboratory, Amina practises on a virtual copy of a Fenwick branch: a till computer, an office computer, a firewall and a file server, all running in isolated virtual machines with synthetic data. Nothing connects to Fenwick's real systems. Ms. Bell explains that labs let students try tests and make mistakes without risking business operations or real customer data. Ms. Bell adds that the lab mirrors a real branch closely enough that procedures tested here can be reused at Fenwick.

### 12.2 Test procedure

Amina follows a written procedure to test the leaver process: create a test user, mark them as a leaver in the lab's HR list, run the reconciliation script and check that the account is flagged and disabled within the agreed time. She records each step and result. The account is flagged but not disabled because the disable step requires manual approval that nobody gave in the lab scenario. The missing approval is a property of the process, not of the script, which is why the next section compares expected and actual results.

### 12.3 Comparing

The expected result was disablement within one day. The actual result was flagged but still active. Amina notes the gap: the process depends on a person approving, and no reminder exists if approval is forgotten. She recommends an escalation if approval is not given within one day. She learns that labs reveal process gaps, not just technical faults, because they test the whole sequence from start to finish. A one-day escalation would also give the leaver process a measurable target for later checks.

### Worked example

Amina tests the leaver process in an isolated lab, finds disablement stalls without approval and recommends escalation.

> **Synthetic case.** The lab environment and data are synthetic.

### Errors and limits

Labs differ from production. Scenarios simplify.

### Exercises

- **EX045 — Lab isolation.** Why is the lab isolated? *Rubric:* 3 = to avoid risking real systems and data;; 2 = safety;; 1 = vague;; 0 = none.
- **EX046 — Lab result.** What was the actual result of the leaver test? *Rubric:* 3 = flagged but not disabled;; 2 = stalled;; 1 = disabled;; 0 = none.
- **EX047 — Gap cause.** Why was the account not disabled? *Rubric:* 3 = required manual approval was not given;; 2 = approval;; 1 = vague;; 0 = none.
- **EX048 — Recommendation.** What did Amina recommend? *Rubric:* 3 = escalation if approval not given within one day;; 2 = escalation;; 1 = vague;; 0 = none.

### Synthesis

Contained labs test whole processes safely and expose gaps between steps.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Security governance, risk and compliance: troubleshooting

### Learning outcomes

You will (1) troubleshoot a control that produces wrong results; (2) use evidence to test hypotheses; (3) fix causes rather than symptoms.

### 13.1 The problem

Fenwick's weekly backup report shows success, but a restore test from the online shop data fails. Amina is asked to troubleshoot. She lists hypotheses: the backup job covers the wrong folder, the backup is corrupted, or the restore procedure is wrong. She learns that troubleshooting starts with clear hypotheses and evidence for each, rather than changing settings at random and hoping the problem disappears. Each hypothesis points to a different check: the folder list, the backup file integrity or the restore steps.

### 13.2 Testing hypotheses

Amina checks the backup job's folder list and finds it points to an old location used before the shop platform was upgraded. The new data live elsewhere. The backup reports success because it successfully backs up the old, empty folder. She confirms by restoring the old folder, which works but contains outdated files. She learns that a success message only shows that a job ran, not that it protected the right data. The reliable success messages had hidden the gap since the shop platform upgrade.

### 13.3 Fixing the cause

Amina updates the folder path, runs a new backup and restores sample files successfully. She also adds a check to the change procedure: when a system is upgraded, backup coverage must be reviewed. She learns that fixing the immediate problem is not enough; the cause was a change process that did not consider backups, so the process must change too. The new check would have caught the old folder path when the shop platform was upgraded. Without the procedure change, the next platform upgrade could silently break backups again.

### Worked example

Amina tests three hypotheses, finds the backup pointing to an old folder and fixes both the path and the change process.

> **Synthetic case.** The troubleshooting case is synthetic.

### Errors and limits

Hypothesis lists can miss causes. Success reports can mislead.

### Exercises

- **EX049 — Hypotheses.** Name the three hypotheses Amina listed. *Rubric:* 3 = wrong folder, corrupted backup, wrong restore procedure;; 2 = three;; 1 = vague;; 0 = none.
- **EX050 — Misleading success.** Why did the backup report success? *Rubric:* 3 = it backed up an old, empty folder;; 2 = wrong target;; 1 = vague;; 0 = none.
- **EX051 — Process fix.** What process change did Amina add? *Rubric:* 3 = review backup coverage after system upgrades;; 2 = change process;; 1 = vague;; 0 = none.
- **EX052 — Success meaning.** What does a backup success message show? *Rubric:* 3 = a job ran, not that the right data were protected;; 2 = ran;; 1 = protected;; 0 = none.

### Synthesis

Troubleshooting with hypotheses finds root causes, which often lie in processes.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Security governance, risk and compliance: automation

### Learning outcomes

You will (1) automate a recurring check; (2) set warning and alert levels; (3) ensure automated results reach owners.

### 14.1 Choosing what to automate

Amina looks for recurring checks that are easy to automate and costly to forget. Certificate expiry is a good candidate: an expired certificate can stop the online shop or remote access, and checking dates manually is tedious. She writes a script that reads a list of certificates and their expiry dates and reports how many days remain. She learns that automation is best for simple, repetitive checks with clear rules. A certificate list with expiry dates is a simple input with a clear rule, which makes it a safer first automation than complex log analysis.

### 14.2 Warning levels

The script warns when thirty days or fewer remain and alerts when a certificate has expired. On the first of October, the lab finds the remote access certificate expired three days earlier, the shop certificate due in nineteen days with a warning, and two others fine at forty-five and one hundred and fifty-one days. The expired certificate explains complaints from staff who could not connect from home over the weekend. Had the script been running a month earlier, the remote access certificate would have triggered a warning about thirty days before it expired.

### Lab — Certificate expiry warnings and alerts

```python
"""Certificate expiry check: warn within 30 days, alert if expired (synthetic)."""
from datetime import date
today = date(2026, 10, 1)
certs = {"shop.fenwick.example": date(2026, 10, 20), "mail.fenwick.example": date(2027, 3, 1),
         "vpn.fenwick.example": date(2026, 9, 28), "pos-api.fenwick.example": date(2026, 11, 15)}
for n, d in sorted(certs.items(), key=lambda x: x[1]):
    left = (d - today).days
    s = "EXPIRED" if left < 0 else "WARN" if left <= 30 else "ok"
    print(f"{n}: {left} days {s}")
```

Run with `python3 lab_certs.py`. Verified output:

```text
vpn.fenwick.example: -3 days EXPIRED
shop.fenwick.example: 19 days WARN
pos-api.fenwick.example: 45 days ok
mail.fenwick.example: 151 days ok
```

### 14.3 Reaching owners

An automated check is useless if nobody reads it. Amina sets the script to run daily and send results to the IT lead and the ticketing system, creating a ticket for any warning or alert. The expired certificate is renewed the same day and the shop certificate within a week. She learns that automation must include delivery to owners and a follow-up path, or it becomes another ignored report. Creating a ticket for each warning gives every result an owner and a closure record.

### Worked example

Amina automates certificate expiry checks, finds one expired and one in warning and routes results to tickets.

> **Synthetic case.** Certificates and dates are synthetic.

### Errors and limits

Lists can omit certificates. Tickets can be ignored.

### Exercises

- **EX053 — Automation candidate.** Why is certificate expiry a good automation candidate? *Rubric:* 3 = simple, repetitive and costly to forget;; 2 = fit;; 1 = vague;; 0 = none.
- **EX054 — Expired certificate.** Which certificate had expired? *Rubric:* 3 = vpn.fenwick.example, 3 days earlier;; 2 = VPN;; 1 = shop;; 0 = none.
- **EX055 — Warning certificate.** Which certificate was in warning? *Rubric:* 3 = shop, 19 days left;; 2 = shop;; 1 = mail;; 0 = none.
- **EX056 — Delivery path.** How do results reach owners? *Rubric:* 3 = daily email to IT lead and tickets for warnings and alerts;; 2 = tickets;; 1 = vague;; 0 = none.

### Synthesis

Automation works when checks are simple and results reach owners with a follow-up path.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security governance, risk and compliance: integration and dependencies

### Learning outcomes

You will (1) identify dependencies on external providers; (2) check provider assurance; (3) plan for provider failure.

### 15.1 Dependencies

Fenwick depends on providers: the online shop platform, the payment gateway, the cloud email service and a support company for branch networks. Amina lists what each provides, what data it handles and what happens if it fails. The shop platform and payment gateway are critical; if either fails, online sales stop. She learns that dependencies on providers are part of Fenwick's risk, even though Fenwick does not run those systems. Ms. Bell asks what happens if the cloud email service fails, and Amina notes that orders and supplier messages would stop although sales would continue.

### 15.2 Provider assurance

Amina checks what assurance each provider offers. The payment gateway publishes its PCI DSS compliance status. The shop platform provides a SOC 2 report under non-disclosure. The support company has no formal assurance. She records these and recommends that the support company's contract include security requirements, such as removing temporary rules after work. She learns that assurance varies widely and that contracts can fill gaps where formal reports do not exist. For the support company, a contract clause requiring removal of temporary rules would have prevented the remote desktop exposure she found earlier.

### 15.3 Planning for failure

For critical providers, Amina helps plan responses to failure. If the shop platform fails, Fenwick will post a notice and take phone orders. If the payment gateway fails, branches can still take cards through terminals with a separate connection. She learns that dependency planning makes outages less damaging and that simple manual fallbacks can keep a business running while providers recover. Each fallback should also be tested, since terminals with a separate connection only help if that connection actually works.

### Worked example

Amina lists four provider dependencies, records their assurance and plans fallbacks for the shop and payment gateway.

> **Synthetic case.** Providers and plans are synthetic; PCI DSS and SOC 2 are real.

### Errors and limits

Assurance reports have limited scope. Fallbacks need practice.

### Exercises

- **EX057 — Critical providers.** Which providers are critical for online sales? *Rubric:* 3 = shop platform and payment gateway;; 2 = two;; 1 = email;; 0 = none.
- **EX058 — Missing assurance.** Which provider had no formal assurance? *Rubric:* 3 = the network support company;; 2 = support company;; 1 = vague;; 0 = none.
- **EX059 — Contract gap fill.** How can contracts help where formal reports are missing? *Rubric:* 3 = include security requirements such as removing temporary rules;; 2 = contracts;; 1 = vague;; 0 = none.
- **EX060 — Shop fallback.** What is the fallback if the shop platform fails? *Rubric:* 3 = post a notice and take phone orders;; 2 = manual;; 1 = vague;; 0 = none.

### Synthesis

Provider dependencies need assurance checks, contract terms and practical fallbacks.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write clear technical procedures; (2) include safety and authorisation steps; (3) keep documents current.

### 16.1 Clear procedures

Amina writes procedures for tasks she has learned: running the baseline check, verifying firewall rules, checking certificates and testing restores. Each procedure lists the purpose, prerequisites, steps, expected results and what to do if results differ. She writes in short numbered steps with exact commands where needed. She learns that good procedures let another technician perform a task correctly the first time without asking the author. Including the expected result lets a technician tell at once whether a firewall verification or restore has gone wrong.

### 16.2 Safety and authorisation

Each procedure includes safety steps. Before changing a firewall, confirm the change is approved and schedule it outside trading hours. Before restoring data, restore to a test location, not over live data. Before running scripts, confirm they run against the correct system. She learns that technical mistakes can stop branches trading, so safety checks are part of professional practice and protect both the business and the technician. Restoring to a test location first, for example, would prevent outdated files from overwriting current online shop data.

### 16.3 Keeping current

Amina adds an owner and review date to each procedure and a change log at the end. When the shop platform was upgraded, the backup procedure became wrong, which caused the earlier failure. She recommends reviewing procedures whenever related systems change. She learns that out-of-date procedures can be worse than none, because they give confidence while leading people to do the wrong thing. Her review rule would have flagged the backup procedure as soon as the shop platform upgrade was approved.

### Worked example

Amina writes four procedures with safety and authorisation steps, owners, review dates and change logs.

> **Synthetic case.** Procedures are synthetic.

### Errors and limits

Procedures go stale. Steps can be skipped.

### Exercises

- **EX061 — Procedure parts.** What does each procedure list? *Rubric:* 3 = purpose, prerequisites, steps, expected results, what to do if different;; 2 = five;; 1 = vague;; 0 = none.
- **EX062 — Restore safety.** Where should data be restored first? *Rubric:* 3 = a test location, not over live data;; 2 = test location;; 1 = live;; 0 = none.
- **EX063 — Stale danger.** Why can out-of-date procedures be worse than none? *Rubric:* 3 = they give false confidence and lead to wrong actions;; 2 = false confidence;; 1 = vague;; 0 = none.
- **EX064 — Firewall timing.** When should firewall changes be scheduled? *Rubric:* 3 = outside trading hours, after approval;; 2 = timing;; 1 = vague;; 0 = none.

### Synthesis

Clear, safe and current procedures let technicians work correctly and protect the business.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) run a combined control exercise in a safe lab; (2) respond to an injected problem; (3) write a short incident note.

### 17.1 The exercise

In the second laboratory, Amina runs a combined exercise on the virtual branch. She performs a baseline check, verifies firewall rules, checks certificates and reconciles accounts. Midway, Ms. Bell injects a problem: a new firewall rule appears allowing file sharing from the guest Wi-Fi to the file server, and a test account becomes active again. Amina must notice and respond using her procedures. The injected problems match failure modes from her register: a rule added without approval and an account active after it should be off.

### 17.2 Responding

The firewall verification flags the new rule as unapproved. The account reconciliation flags the reactivated test account. Amina follows the procedures: she records the findings, reports to the instructor acting as IT lead, recommends removing the rule and disabling the account and waits for approval before acting. Once approved, she makes the changes and re-runs both checks, which now pass. Re-running the checks after the changes produces evidence that the fixes worked, not merely that they were attempted. Waiting for approval before acting keeps her within the authority limits she agreed at the start.

### 17.3 Incident note

Amina writes a short incident note: what was found, when, how it was detected, what actions were taken, by whom and with what approval, and what should prevent recurrence. She suggests that guest Wi-Fi be blocked from internal systems by default, so a single rule cannot open it. She learns that incident notes create a record for learning and accountability, and that writing them promptly keeps details accurate. Blocking guest Wi-Fi by default would turn a single risky rule into a deliberate exception that needs approval.

### Worked example

Amina detects an injected firewall rule and reactivated account, responds with approval and writes an incident note with a preventive suggestion.

> **Synthetic case.** The exercise is synthetic and isolated.

### Errors and limits

Injected problems are known to be coming. Labs simplify.

### Exercises

- **EX065 — Injected problems.** Which two problems were injected? *Rubric:* 3 = guest Wi-Fi file sharing rule and reactivated test account;; 2 = two;; 1 = vague;; 0 = none.
- **EX066 — Approval step.** What did Amina do before making changes? *Rubric:* 3 = waited for approval;; 2 = approval;; 1 = acted at once;; 0 = none.
- **EX067 — Note contents.** What does the incident note include? *Rubric:* 3 = finding, time, detection, actions, approval and prevention;; 2 = contents;; 1 = vague;; 0 = none.
- **EX068 — Preventive idea.** What preventive measure did Amina suggest? *Rubric:* 3 = block guest Wi-Fi from internal systems by default;; 2 = default deny;; 1 = vague;; 0 = none.

### Synthesis

Combined exercises test detection, controlled response and clear incident records.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) deliver a supervised technical GRC project; (2) measure results; (3) hand over to the client.

### 18.1 The project

For her supervised project, Amina builds a weekly check pack for Fenwick: the baseline check, firewall verification, certificate expiry check and account reconciliation, run by one script that creates tickets for findings. She agrees scope and success criteria with the IT lead: all four checks running weekly, findings reaching tickets and the IT team able to maintain the pack. She keeps a project log of decisions and problems. Ms. Bell notes that the agreed success criteria will let both of them judge the project objectively at the end.

### 18.2 Results

After six weeks, all four checks run weekly. They find eleven issues, including two laptops without encryption, one unapproved firewall rule and three leaver accounts. All issues become tickets, and nine are closed within two weeks. The IT lead reports that checks that used to be skipped now happen reliably. Amina reports results honestly, noting two tickets still open because they need a supplier's help. Two leaver accounts or one unapproved rule found weekly is evidence the pack catches what manual checks had missed.

### 18.3 Handover

Amina hands over the script, procedures, test data, a list of known limitations and a short training session for the technicians. One technician adds a new check during training, showing the pack can be extended. Ms. Bell assesses the project as meeting all criteria and praises the honest reporting. Amina reflects that technical GRC work is about reliable routines, clear evidence and careful handover rather than complex tools. The technician's new check during training is the strongest sign that the pack will survive her departure.

### Worked example

Amina delivers a weekly check pack finding eleven issues, closes nine within two weeks and hands over with training.

> **Synthetic case.** The project and results are synthetic.

### Errors and limits

Six weeks is short. Some issues need suppliers.

### Exercises

- **EX069 — Pack checks.** Which four checks does the pack run? *Rubric:* 3 = baseline, firewall verification, certificate expiry, account reconciliation;; 2 = four;; 1 = vague;; 0 = none.
- **EX070 — Issues found.** How many issues did the checks find in six weeks? *Rubric:* 3 = eleven;; 2 = 11;; 1 = vague;; 0 = none.
- **EX071 — Closed tickets.** How many issues were closed within two weeks? *Rubric:* 3 = nine;; 2 = 9;; 1 = eleven;; 0 = none.
- **EX072 — Extensibility proof.** What showed the pack could be extended? *Rubric:* 3 = a technician added a new check during training;; 2 = extension;; 1 = vague;; 0 = none.

### Synthesis

A supervised project succeeds through reliable routines, honest results and a careful handover.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Amina Yusuf, Ms. Clara Bell, Dunmore Technical College, Fenwick Building Supplies and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The stock database.

**EX002.** The route planning service and the branch Wi-Fi.

**EX003.** Because problems in unowned components often go unnoticed.

**EX004.** For example in-branch sales, the online shop and deliveries (also supplier ordering and payroll).

**EX005.** Everything was connected to one switch with no separation.

**EX006.** Connections to the payment gateway and to IT management for updates.

**EX007.** What changed, why, who approved it and when.

**EX008.** It reduces the number of systems in scope for card data requirements.

**EX009.** Because nobody can tell who processed a refund or sale.

**EX010.** Because malware could install itself with full control.

**EX011.** So that compromising an everyday account does not give attackers admin rights.

**EX012.** To find problems, such as an accounting program needing a setting change, before rolling out.

**EX013.** Because named fields make records easy to read and check with scripts.

**EX014.** FW-LT01.

**EX015.** FW-LT03, with a 30-minute screen lock and local administrator rights.

**EX016.** Because a five-minute lock is stricter than the ten-minute requirement.

**EX017.** Testing for vulnerabilities on live systems.

**EX018.** What was checked, when, by whom, how, and the original output.

**EX019.** Report it with the evidence you already have, without investigating further.

**EX020.** So others can trust that it shows exactly what was observed.

**EX021.** Because it supports a policy, reduces a risk and produces evidence.

**EX022.** The finance director.

**EX023.** The network policy and card payment obligations.

**EX024.** It helps them prioritise when time is short and justify resources.

**EX025.** Because policy and payment card rules often require logs to be kept for a defined period.

**EX026.** The admin account, with seven failures, above the threshold of five.

**EX027.** As a likely mistyped password, since a success followed.

**EX028.** Blocking the source address and renaming the generic admin account.

**EX029.** Through restore tests.

**EX030.** Because some failures stay silent until something breaks.

**EX031.** The IT lead, with a monthly expiry check.

**EX032.** What goes wrong, how it would show and what its impact would be.

**EX033.** Rare but severe events can look low, and different risks can tie.

**EX034.** A written incident response plan.

**EX035.** The ticketing system, validated spreadsheets and short scripts.

**EX036.** As in place, partly in place or missing, with evidence.

**EX037.** Five failures within ten minutes.

**EX038.** Because it would cause many false alarms from mistyped passwords.

**EX039.** To show the old state worked and the change did not break anything.

**EX040.** The stock database and online shop data.

**EX041.** Two.

**EX042.** The rule allowing remote desktop from anywhere to the payment terminal segment.

**EX043.** A support company added it for a one-off repair and never removed it.

**EX044.** Because verification finds changes that change control missed.

**EX045.** So tests and mistakes cannot affect business operations or real customer data.

**EX046.** The account was flagged but not disabled.

**EX047.** Because the disable step needed manual approval that nobody gave.

**EX048.** An escalation if approval is not given within one day.

**EX049.** The job covers the wrong folder, the backup is corrupted, or the restore procedure is wrong.

**EX050.** Because it successfully backed up the old, empty folder.

**EX051.** A check that backup coverage is reviewed whenever a system is upgraded.

**EX052.** Only that the job ran, not that it protected the right data.

**EX053.** Because it is a simple, repetitive check with clear rules and costly consequences if forgotten.

**EX054.** The remote access (VPN) certificate, three days earlier.

**EX055.** The shop certificate, with 19 days left.

**EX056.** The script runs daily and sends results to the IT lead, creating tickets for warnings and alerts.

**EX057.** The online shop platform and the payment gateway.

**EX058.** The support company for branch networks.

**EX059.** By including security requirements, such as removing temporary rules after work.

**EX060.** Posting a notice and taking phone orders.

**EX061.** Purpose, prerequisites, steps, expected results and what to do if results differ.

**EX062.** To a test location, not over live data.

**EX063.** Because they give confidence while leading people to do the wrong thing.

**EX064.** Outside trading hours, after confirming approval.

**EX065.** A firewall rule allowing guest Wi-Fi to reach the file server and a reactivated test account.

**EX066.** She reported the findings and waited for approval.

**EX067.** What was found, when, how it was detected, actions taken with approval and what prevents recurrence.

**EX068.** Blocking guest Wi-Fi from internal systems by default.

**EX069.** The baseline check, firewall verification, certificate expiry check and account reconciliation.

**EX070.** Eleven.

**EX071.** Nine.

**EX072.** A technician added a new check during the training session.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- AICPA. (2017). *2017 Trust services criteria for security, availability, processing integrity, confidentiality, and privacy (with revised points of focus — 2022)*. American Institute of CPAs. <https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- PCI Security Standards Council. (2022). *Payment Card Industry Data Security Standard: Requirements and testing procedures, v4.0*. <https://www.pcisecuritystandards.org/document_library/>
