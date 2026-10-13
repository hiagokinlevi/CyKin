# Systems, Endpoint and Hardware Security: Bachelor's Course

- Language: English (`en`); course 104, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; Nine offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: undergraduates learning to inventory, harden, patch, encrypt, monitor and recover the laptops and servers of a small organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only servers, endpoints and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, inventories, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the foundation chapters apply mathematics, computing, writing and ethics to endpoint security, and the specialist chapters follow one student's capstone at a small housing association from a stolen unencrypted laptop to a measured, maintained fleet. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Aisha Rahman** | Bachelor's student | Invented |
| **Dr Lewis Grant** | Tutor | Invented |
| **Gareth Lloyd** | IT officer at the partner | Invented |
| **Thornbury University** | Fictional university | Invented |
| **Bramley Housing Association** | Fictional housing association (45 laptops, 4 servers) | Invented |

### Core sources

NIST [SP 800-123](https://doi.org/10.6028/NIST.SP.800-123), [SP 800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4), [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128), [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5) and [SP 800-193](https://doi.org/10.6028/NIST.SP.800-193); [CIS Controls v8](https://www.cisecurity.org/controls/v8) and [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); DISA [STIGs](https://public.cyber.mil/stigs/); Microsoft [Windows security baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines); Linux [kernel self-protection](https://www.kernel.org/doc/html/latest/security/self-protection.html). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) reason with counts, proportions and simple inequalities about devices; (2) check claims with arithmetic; (3) connect mathematics to the course case.

### 1.1 The case behind the course

Aisha Rahman is a bachelor's student at the fictional Thornbury University. Her tutor, Dr Lewis Grant, links her to the fictional Bramley Housing Association, a charity with 45 staff laptops and four servers looked after by one IT officer, Gareth Lloyd. Last winter a laptop was stolen from a staff member's car. It was not encrypted and held tenant records, so Bramley had to report the loss and write to affected tenants. Gareth wants to know how many other laptops are in the same state and what a small charity can realistically do. Aisha's degree projects will follow this problem.

### 1.2 Proportions

If 13 of 45 laptops lack encryption, the proportion is 13 divided by 45, about 29%. Proportions let Bramley compare itself over time and with guidance, even as the number of laptops changes.

### 1.3 Inequalities as targets

Targets are often inequalities: "at least 95% of laptops encrypted" or "no critical update older than 14 days". Writing them this way makes them checkable: either the measured value satisfies the inequality or it does not.

### 1.4 Checking claims

A supplier claims its tool "fixes 90% of problems". Aisha asks: 90% of what, counted how, over what period? Mathematical reasoning starts with defining the quantity before believing the number.

### 1.5 Orders of magnitude

With 45 laptops, one stolen laptop is about 2% of the fleet, but if it holds 3,000 tenant records, its impact is far larger than 2% suggests. Counting devices and counting affected people are different measures.

### Worked example

Gareth says "most laptops are fine". Aisha asks for the count. From his notes, 32 of 45 are encrypted: 71%. She rewrites his statement as "29% of laptops, 13 devices, are not encrypted", which makes the size of the problem clear to Bramley's managers.

> **Synthetic case.** Aisha, Dr Grant, Gareth and Bramley are synthetic.

### Errors and limits

Percentages of small numbers can mislead; always show the count too.

### Exercises

- **EX001 — Case trigger.** What incident started Bramley's concern? *Rubric:* 3 = unencrypted stolen laptop with tenant records; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Proportion.** What share of 45 laptops is 13? *Rubric:* 3 = about 29%; 2 = partial; 1 = none; 0 = none.
- **EX003 — Two measures.** Why do device count and people affected differ? *Rubric:* 3 = one device can hold many records; 2 = partial; 1 = none; 0 = none.

### Synthesis

Define quantities clearly and show counts with proportions.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the parts of laptops and servers; (2) explain storage, memory and firmware; (3) relate hardware to data exposure.

### 2.1 Laptops and servers

A laptop and a server share the same building blocks: processor, memory, storage, firmware and network interfaces. Servers run continuously and provide shared services such as file storage; laptops travel and are used by one person. Travel makes laptops easier to lose.

### 2.2 Storage

Laptop storage keeps data when powered off. Without encryption, anyone who removes the disk or boots another system can read it. This is exactly what made the stolen Bramley laptop a reportable incident.

### 2.3 Firmware and the TPM

Firmware starts the machine; a Trusted Platform Module stores keys and can release the disk encryption key only when the expected boot components load. Microsoft's BitLocker documentation describes this approach for Windows laptops.

### 2.4 Memory

Memory holds working data and is cleared when power is lost. Locking or shutting down laptops when unattended reduces the time data sits in an unlocked session.

### 2.5 Inventory of hardware

Aisha records each device's model, age and whether it has a TPM. Two older laptops lack one, which affects how they can be encrypted.

### Servers in the case

Bramley's four servers hold the shared files, the finance system, the directory that controls logons and an old housing application. They sit in a small cupboard in the office. Because they hold more data than any laptop, their protection matters, but their risks differ: they rarely move, so theft is less likely, while unneeded services and missed updates matter more.

### Worked example

Gareth asks whether a password on the laptop would have been enough. Aisha explains that a login password stops someone using Windows, but not someone reading the disk directly; only encryption protects the data at rest.

> **Synthetic case.** Synthetic.

### Errors and limits

Hardware features help only when enabled; many laptops ship with encryption off.

### Exercises

- **EX004 — Travel risk.** Why are laptops more exposed than servers? *Rubric:* 3 = they travel and are lost; 2 = partial; 1 = none; 0 = none.
- **EX005 — Login password.** Why is a login password not enough? *Rubric:* 3 = disk readable directly; 2 = partial; 1 = none; 0 = none.
- **EX006 — TPM role.** What does the TPM do for encryption? *Rubric:* 3 = releases key for expected boot; 2 = partial; 1 = none; 0 = none.

### Synthesis

Data at rest on portable hardware needs encryption.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write small Python programs over lists and dictionaries; (2) print clear results; (3) test with known answers.

### 3.1 A first check

Aisha's first program reads a list of synthetic laptop records and prints those without encryption. It has three parts: data, a loop with a condition and output. Even this small check answers the question Gareth used to answer by hand.

### 3.2 Lists and dictionaries

Each laptop is a dictionary with fields such as name, encrypted and last_update. The fleet is a list of dictionaries. This structure appears in most labs in the course.

### 3.3 Clear output

Good output starts with a count, then lists details. "13 of 45 laptops not encrypted" is more useful than a long list with no summary.

### 3.4 Testing

Before trusting the program, Aisha runs it on three synthetic laptops where she knows the answer: two encrypted, one not. The program must print exactly one.

### 3.5 Standard library

Labs use only Python's standard library, so they run on any computer and add no unreviewed code to Bramley's systems.

### Building on the first check

Aisha extends her program to report two fields: encryption and days since last update. She keeps each check in its own function so that a mistake in one does not affect the other. Later chapters reuse these functions in the inventory, baseline and verification labs, so writing them carefully now saves time later.

### Questions to carry forward

Aisha ends the chapter with three questions she will return to: which devices exist, how are they configured, and how quickly do they receive fixes? Each question links to a later lab, and each answer will be recorded with its date and source so that progress can be measured honestly rather than remembered.

### Worked example

Aisha's first version prints nothing. She finds that the encrypted field is stored as the text "False", which Python treats as true in a condition. She converts the text to a boolean and adds a test with text input.

> **Synthetic case.** Synthetic.

### Errors and limits

Data types cause silent errors; test with realistic data.

### Exercises

- **EX007 — Program parts.** What are the three parts of the first program? *Rubric:* 3 = data, loop with condition, output; 2 = two; 1 = one; 0 = none.
- **EX008 — Output style.** How should output be ordered? *Rubric:* 3 = count then details; 2 = partial; 1 = none; 0 = none.
- **EX009 — Bug.** Why did the first version print nothing? *Rubric:* 3 = "False" text treated as true; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small tested programs replace manual checking.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write clear, evidenced arguments; (2) cite sources accurately; (3) structure a short report.

### 4.1 Purpose

Academic writing presents an argument supported by evidence. Aisha's first essay argues that small charities should prioritise laptop encryption.

### 4.2 Evidence

She uses Bramley's counts, CIS Controls v8, which lists data protection and secure configuration among its safeguards, and NIST SP 800-53 Rev. 5, which includes controls for protecting information at rest.

### 4.3 Citing

Each claim from a source is cited; each claim from data names the data. Unsupported opinions are avoided or clearly marked.

### 4.4 Structure

Introduction with question, evidence, counter-arguments, conclusion. Counter-arguments include cost and performance; she answers them with evidence.

### 4.5 Clarity

Short sentences, defined terms and no unexplained acronyms.

### Writing for Bramley

Aisha also learns to write for non-academic readers. Her one-page note for Bramley's managers states the problem, three recommended actions and the cost in staff time, with no citations in the main text and a short source list at the end. The same evidence supports both documents, presented differently.

Dr Grant reviews both and points out that the academic essay must discuss limits, while the management note must state decisions needed. Different purposes require different structures.

### Plagiarism and reuse

Aisha quotes sources only with quotation marks and citations, and paraphrases carefully, checking that her wording does not copy the original's structure.

### Linking principles to Bramley

Least privilege means staff use standard accounts for daily work and IT uses separate named admin accounts. Defence in depth means encryption, firewall, updates and backups each cover gaps the others leave. Fail-safe defaults mean new laptops arrive locked down and settings are relaxed only with a reason. Aisha writes one Bramley example beside each principle so that the ideas stay concrete and can be checked during the project.

### Worked example

Dr Grant marks a sentence: "encryption makes laptops completely secure". Aisha rewrites it: "encryption protects data on a lost or stolen laptop that is powered off or locked", which is accurate.

> **Synthetic case.** Synthetic.

### Errors and limits

Overclaiming in writing weakens credibility.

### Exercises

- **EX010 — Sources.** Which two sources support Aisha's argument? *Rubric:* 3 = CIS Controls v8, SP 800-53r5; 2 = partial; 1 = none; 0 = none.
- **EX011 — Structure.** Give the essay structure. *Rubric:* 3 = intro, evidence, counter-arguments, conclusion; 2 = three; 1 = two; 0 = none.
- **EX012 — Rewrite.** How was the overclaim corrected? *Rubric:* 3 = protects data when lost/stolen and off or locked; 2 = partial; 1 = none; 0 = none.

### Synthesis

Precise claims with cited evidence persuade.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain confidentiality, integrity and availability for endpoints; (2) describe common threats; (3) understand basic controls.

### 5.1 Three goals

Tenant records must stay confidential, finance records must be accurate, and staff need laptops that work. Each goal suggests controls: encryption, updates and backups.

### 5.2 Common threats

Loss and theft, malicious email attachments, unpatched software, weak passwords and misuse of administrator rights are the most common threats to small organisations' endpoints, as NIST SP 800-83 Rev. 1 on malware prevention notes.

### 5.3 Basic controls

Encryption, timely updates, standard user accounts, screen locks, backups and anti-malware form a basic set that matches CIS Controls v8's early safeguards.

### 5.4 Updates

Patching fixes known vulnerabilities. NIST SP 800-40 Rev. 4 describes patching as routine preventive maintenance rather than an emergency activity.

### 5.5 People

Staff habits matter: leaving laptops in cars, sharing passwords and clicking unexpected links.

### Proportionate security

A small charity cannot apply every control in large frameworks. CIS Controls v8 groups safeguards into implementation groups, with the first group aimed at organisations with limited IT resources. Aisha uses this group as a starting point, which gives Bramley a recognised, proportionate baseline rather than an arbitrary list.

She explains this to managers as "the essentials first", and lists the safeguards Bramley already meets and those it lacks.

### Backups

Backups protect availability and integrity: if a laptop or server fails, data can be restored. Aisha checks that backups exist and that a restore has been tested recently.

### Note

Aisha keeps these definitions in a glossary appendix for staff.

### Worked example

Aisha presents the six basic controls to Bramley's staff meeting with one example each. A staff member asks why they cannot be administrators on their own laptops. Aisha explains that admin rights let malware or mistakes change system settings, and that Gareth can install needed software quickly.

> **Synthetic case.** Synthetic.

### Errors and limits

Controls fail when staff do not understand why they exist.

### Exercises

- **EX013 — Goals.** Apply the three goals to Bramley. *Rubric:* 3 = tenant confidentiality, finance accuracy, working laptops; 2 = two; 1 = one; 0 = none.
- **EX014 — Threats.** Name four common endpoint threats. *Rubric:* 3 = loss/theft, attachments, unpatched, weak passwords, admin misuse; 2 = three; 1 = two; 0 = none.
- **EX015 — Admin question.** Why not give staff admin rights? *Rubric:* 3 = malware/mistakes change system; 2 = partial; 1 = none; 0 = none.

### Synthesis

Basic controls address the most common threats.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) use sets to compare inventories; (2) use graphs to describe dependencies; (3) apply logic to policy rules.

### 6.1 Sets for inventory

The asset register is set R; devices reporting to the management agent form set M. R minus M are devices nobody is managing; M minus R are devices nobody registered. Both differences matter.

### 6.2 Logic

Rules such as "if a laptop holds tenant data then it must be encrypted" are implications. Writing them precisely helps check which devices the rule covers.

### 6.3 Graphs

A dependency graph shows that laptops depend on the domain server for logons and the file server for documents; if the domain server fails, many laptops are affected.

### 6.4 Counting

With five yes-or-no baseline settings, there are 32 combinations; only one is fully compliant.

### 6.5 Proof habits

Discrete structures train careful reasoning: clear definitions, edge cases and no generalising from a few examples.

### Practising with Bramley's data

Aisha builds the two sets from synthetic exports and computes both differences with Python's set operations, a preview of the inventory lab in chapter 22. She tests with small examples where she knows the answer, such as one device missing from each set.

She also draws the dependency graph and counts how many laptops depend on each server, showing that the domain server is the most critical node: all 45 laptops need it for logons.

### Edge cases

She considers devices renamed during the month, which could appear in both differences under different names.

### Practical consequence

For Bramley, this means the laptop firmware and boot settings matter as much as the operating system. Aisha adds firmware update status to the inventory fields so that it can be checked alongside software updates.

### Worked example

Aisha writes the encryption rule as a logical implication and realises it does not cover laptops that might later hold tenant data. Gareth decides all laptops must be encrypted, simplifying the rule.

> **Synthetic case.** Synthetic.

### Errors and limits

Rules with conditions create gaps when conditions change.

### Exercises

- **EX016 — Set differences.** What do R minus M and M minus R represent? *Rubric:* 3 = unmanaged registered; unregistered reporting; 2 = partial; 1 = none; 0 = none.
- **EX017 — Dependency.** What does the domain server affect? *Rubric:* 3 = logons for many laptops; 2 = partial; 1 = none; 0 = none.
- **EX018 — Rule change.** Why did Gareth simplify the rule? *Rubric:* 3 = conditions change; encrypt all; 2 = partial; 1 = none; 0 = none.

### Synthesis

Sets, logic and graphs make inventories and rules precise.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) describe office and home networks used by staff laptops; (2) explain VPNs and protocols; (3) identify network-related endpoint risks.

### 7.1 Office network

Bramley's office has a router, switch and Wi-Fi. Laptops, printers and servers share one network.

### 7.2 Home working

Many staff work from home, connecting through a VPN to reach the file server. Laptops at home may be off the office network for weeks, which affects updates and management.

### 7.3 Protocols

Laptops use HTTPS for web, SMB for file shares and DNS for names. Old SMB version 1 should be disabled, as CIS Benchmarks and Microsoft baselines advise.

### 7.4 Firewalls

The laptop firewall blocks unexpected incoming connections, protecting it on public Wi-Fi.

### 7.5 Segmentation

Servers could sit on their own segment, with access only from laptops that need them.

### VPN and updates

Updates and settings reach home laptops only when the VPN connects, unless the management service works over the internet. Aisha investigates both options with Gareth. Bramley's management tool supports internet-based management, which removes the dependency on the VPN for updates. Gareth enables it for a test group of five home workers, and their update latency improves the next month.

Aisha records this as an early, small change with a measured effect.

### Public Wi-Fi

Staff sometimes work in cafés. The laptop firewall set to the public profile blocks incoming connections.

### Applying it

Gareth tries the idea on a test laptop first, recording each setting changed and its effect on staff tasks. Only after a week without problems does it go into the shared baseline, with a note explaining why.

### Worked example

Aisha checks which laptops last connected to the office network more than 30 days ago: 11. These are mostly home workers whose updates come only when the VPN is on. This becomes an input for patching design.

> **Synthetic case.** Synthetic.

### Errors and limits

Assuming all laptops are on the office network misses home workers.

### Exercises

- **EX019 — Home effect.** How does home working affect management? *Rubric:* 3 = off network for weeks, updates delayed; 2 = partial; 1 = none; 0 = none.
- **EX020 — SMB1.** What do baselines say about SMB1? *Rubric:* 3 = disable; 2 = partial; 1 = none; 0 = none.
- **EX021 — Count.** How many laptops had not connected for 30 days? *Rubric:* 3 = 11; 2 = partial; 1 = none; 0 = none.

### Synthesis

Endpoint management must work wherever laptops are.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) build larger checks with functions and modules; (2) read CSV and JSON; (3) handle errors and missing data.

### 8.1 Functions

Aisha writes functions such as load_devices(path) and check_encryption(device), each doing one job and tested separately.

### 8.2 Files

Device exports come as CSV; agent reports as JSON. Python's csv and json modules read both.

### 8.3 Missing data

A device with no encryption field is neither encrypted nor unencrypted; it is unknown. Aisha reports unknowns separately rather than guessing.

### 8.4 Errors

If a file is missing, the program stops with a clear message.

### 8.5 Modules

Shared functions live in one module, used by several checks.

### Combining checks

Aisha's program now runs three checks, encryption, update age and agent last seen, and prints a summary table with one row per laptop and a final count for each check. The summary is short enough to read in a minute, and details are saved to a file for follow-up.

She adds tests for each check and for the summary, using synthetic data with known answers, and runs them before every change. When she later adds a fourth check, the tests confirm she has not broken the first three.

She documents how to run the program in a short readme so Gareth can run it without her.

### Logging the program's own runs

Each run records when it ran and how many devices it read, so a failed or partial run is noticed.

### Applying it

Aisha writes a one-paragraph summary of this chapter for Gareth, focusing on the practical decision it supports and the report that will show whether it is working.

### Worked example

Running on synthetic exports, Aisha's program reports 40 encrypted, 2 encrypting, 1 not encrypted and 2 unknown; without the unknown category, those two would have been silently counted as compliant.

> **Synthetic case.** Synthetic.

### Errors and limits

Treating unknown as compliant hides problems.

### Exercises

- **EX022 — Formats.** Which modules read the exports? *Rubric:* 3 = csv and json; 2 = partial; 1 = none; 0 = none.
- **EX023 — Unknowns.** How are missing fields reported? *Rubric:* 3 = as unknown, separately; 2 = partial; 1 = none; 0 = none.
- **EX024 — Result.** What did the program report? *Rubric:* 3 = 40, 2, 1, 2; 2 = partial; 1 = none; 0 = none.

### Synthesis

Handle missing data explicitly.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) design tables for devices, updates and events; (2) use keys; (3) protect personal data.

### 9.1 Tables

Devices (asset tag, model, owner role, location), updates (device, update, released, installed) and events (device, time, type).

### 9.2 Keys

Asset tags are unique keys; owner roles rather than names reduce personal data.

### 9.3 Queries

Which devices miss critical updates older than 14 days? Which devices have not reported in 30 days?

### 9.4 Retention

Records are kept for a year.

### 9.5 Privacy

No tenant data enters these tables.

### Building the tables

Aisha builds the tables in a small database file using Python's built-in sqlite3 module, loading synthetic exports. She writes the two queries from the section above and a third for laptops not seen for 30 days.

She checks that each query returns what she expects on a small test set, then runs them on the full synthetic data. The 30-day query returns six devices, which matches her manual count.

She documents each table and field in a short data dictionary, including what each value means and where it comes from, so later readers can interpret results correctly.

### Updating data

The tables are refreshed weekly from new exports; old rows are kept for trends until the retention period ends.

### Access

Only Aisha and Gareth can open the database file, which is stored on encrypted storage.

### A worked Bramley example

Aisha walks through one laptop from purchase to retirement: it is ordered and added to the register, enrolled in management, encrypted and baselined, updated monthly, checked weekly, and finally wiped and recorded as disposed. Each step names who does it and where the evidence lives. Seeing a single device's life on one page helps Gareth notice two missing steps: recording the disposal certificate and removing the device from management.

### Worked example

Aisha's query for overdue critical updates returns four devices; she checks each by hand and confirms the query is right.

> **Synthetic case.** Synthetic.

### Errors and limits

Queries are only as good as the data's timeliness.

### Exercises

- **EX025 — Tables.** Name the three tables. *Rubric:* 3 = devices, updates, events; 2 = two; 1 = one; 0 = none.
- **EX026 — Owner role.** Why store owner role instead of name? *Rubric:* 3 = reduce personal data; 2 = partial; 1 = none; 0 = none.
- **EX027 — Validation.** How did Aisha validate her query? *Rubric:* 3 = checked each result by hand; 2 = partial; 1 = none; 0 = none.

### Synthesis

Design data for the questions you must answer.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) work only with permission; (2) protect personal data; (3) communicate honestly with the partner.

### 10.1 Permission

Aisha's work at Bramley is covered by a written agreement signed by Bramley's chief executive and Dr Grant: read-only access to device reports, no access to tenant records and changes only through Gareth.

### 10.2 Personal data

Device reports include staff names. Aisha uses roles in her reports and keeps raw exports on encrypted university storage.

### 10.3 Honesty

She reports problems plainly, including those caused by past decisions.

### 10.4 Limits

She does not test laptops for weaknesses or try to access data.

### 10.5 Raising concerns

If she sees something serious, she tells Gareth the same day.

### Why authorisation matters

Authorisation protects everyone. Without it, even helpful actions could break the law or Bramley's policies, and evidence Aisha collected could be questioned. With it, both sides know what she may do, and Bramley can show regulators and funders that the student project was controlled.

The agreement also covers what happens to data at the end: Aisha deletes her copies of exports within a month of submitting her capstone and confirms deletion in writing.

### Professional codes

Professional bodies in computing publish codes of conduct that emphasise public interest, honesty and competence. Aisha reads one and notes how it applies to her work at Bramley, especially honesty about the limits of her skills.

### Limits of the approach

No single control is perfect. Aisha notes where this one depends on people remembering, where it depends on reports that may be incomplete, and where it would fail silently. For each weakness she adds a simple check to the weekly routine, so failures become visible quickly.

### Worked example

Aisha notices a shared "admin" account used on a server. She reports it to Gareth rather than investigating its use herself. Gareth disables it and creates named accounts.

> **Synthetic case.** Synthetic.

### Errors and limits

Good intentions do not replace authorisation.

### Exercises

- **EX028 — Agreement.** What does the agreement permit? *Rubric:* 3 = read-only reports, no tenant data, changes via Gareth; 2 = two; 1 = one; 0 = none.
- **EX029 — Names.** How are staff names handled? *Rubric:* 3 = roles in reports, encrypted storage; 2 = partial; 1 = none; 0 = none.
- **EX030 — Shared admin.** How was the shared admin account handled? *Rubric:* 3 = reported to Gareth; disabled, named accounts; 2 = partial; 1 = none; 0 = none.

### Synthesis

Work within permission and report concerns promptly.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain users, privileges, services and updates in Windows and Linux; (2) describe how the OS enforces separation; (3) identify hardening settings.

### 11.1 Accounts and privileges

Standard users cannot change system settings; administrators can. Bramley's laptops give many staff local admin rights, which baseline guidance from CIS and Microsoft recommends removing.

### 11.2 Services

Servers run services such as file sharing and directory services. NIST SP 800-123 advises removing services a server does not need, because each one adds risk and maintenance.

### 11.3 Updates

Operating systems receive monthly security updates. Updates need restarts, which staff often postpone.

### 11.4 Kernel and self-protection

The OS kernel enforces separation between programs. The Linux kernel self-protection documentation describes techniques that make the kernel harder to misuse; Windows includes comparable protections in its security baselines.

### 11.5 Logs

The OS records logons, installs and errors, supporting investigation.

### Linux at Bramley

The old application server runs Linux. Aisha learns basic Linux concepts: users and groups, file permissions and services managed by the init system. The same principles apply as on Windows: standard users for daily work, minimal services and regular updates. Gareth relies on the contractor for this server, so Aisha documents its settings for future reference.

She also notes that the server's operating system version is approaching the end of vendor support, which will matter in chapter 31.

### Restart planning

Bramley sets a weekly restart window for laptops and a monthly window for servers, communicated to staff in advance.

### Applying it

Gareth records the decision and its reason in the decision log, so a future officer understands why it was made.

### Worked example

Aisha checks a sample laptop's pending updates: three are installed but waiting for a restart that the user has postponed for two weeks. Until the restart, the fixes are not active.

> **Synthetic case.** Synthetic.

### Errors and limits

Installed is not the same as active; restarts matter.

### Exercises

- **EX031 — Admin advice.** What do baselines advise about local admin? *Rubric:* 3 = remove; 2 = partial; 1 = none; 0 = none.
- **EX032 — SP 800-123.** What does SP 800-123 advise about services? *Rubric:* 3 = remove unneeded; 2 = partial; 1 = none; 0 = none.
- **EX033 — Pending restart.** Why were the sample laptop's fixes inactive? *Rubric:* 3 = restart postponed; 2 = partial; 1 = none; 0 = none.

### Synthesis

Privileges, services and restarts shape endpoint security.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) summarise patch latency with mean, median and spread; (2) recognise skew; (3) choose meaningful measures.

### 12.1 Patch latency

Patch latency is the days from an update's release to its installation on a device. Aisha collects it for the last monthly update on all 45 laptops.

### Lab — Lab — patch latency

```python
"""Summarise synthetic patch latency (days from release to install) for 45 laptops (stdlib only)."""
import statistics
days = [3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 16, 18, 19,
        21, 22, 25, 28, 30, 33, 35, 41, 47, 52, 60, 68, 75, 88, 104]
print(f"laptops {len(days)}, mean {statistics.mean(days):.1f}, median {statistics.median(days)}, max {max(days)}")
print(f"within 14 days {sum(d <= 14 for d in days)}/{len(days)}, over 30 days {sum(d > 30 for d in days)}")
```

Run with `python3 lab_latency.py`. Verified output:

```text
laptops 45, mean 22.4, median 12, max 104
within 14 days 26/45, over 30 days 10
```

### 12.2 Reading the result

The mean is 22.4 days, the median 12 and the maximum 104. 26 of 45 laptops installed within 14 days; 10 took over 30 days.

### 12.3 Skew

A few very late laptops pull the mean far above the median. The distribution is skewed, so the median describes the typical laptop better and the tail count describes the problem.

### 12.4 Choosing measures

Bramley adopts two measures: share within 14 days and count over 30 days.

### Why the tail matters

The ten laptops taking over 30 days are where risk concentrates. If a critical vulnerability is exploited widely within a few weeks of a fix, those ten remain exposed. Focusing on the tail gives Bramley a manageable list rather than a vague average.

Aisha lists the ten and finds common factors: six are home workers rarely on the VPN, three have full disks and one is the laptop in a drawer. Each factor suggests a fix.

### Visualising

A simple sorted bar chart of days per laptop makes the tail visible to managers.

### Repeat

The measure is repeated monthly for each update cycle.

### Interpreting the tail

The mean of 22.4 days hides a long tail: ten laptops took over 30 days. Aisha looks at those ten individually and finds three causes: laptops left switched off, pending restarts and two broken update agents. The median of 12 shows that most laptops are fine. Fixing the tail, not the typical laptop, is where effort pays off.

### Worked example

Gareth's old report said "average 22 days", suggesting a uniform delay. Aisha shows that most laptops patch within two weeks and a tail of ten causes the problem, which points to specific devices.

> **Synthetic case.** Synthetic.

### Errors and limits

A mean alone hides tails.

### Exercises

- **EX034 — Lab figures.** Give mean, median and max. *Rubric:* 3 = 22.4, 12, 104; 2 = two; 1 = one; 0 = none.
- **EX035 — Tail.** How many laptops took over 30 days? *Rubric:* 3 = 10; 2 = partial; 1 = none; 0 = none.
- **EX036 — Measures.** Which two measures did Bramley adopt? *Rubric:* 3 = share within 14 days, count over 30; 2 = partial; 1 = none; 0 = none.

### Synthesis

Use medians and tails for skewed data.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) apply least privilege to staff and admins; (2) use named admin accounts and MFA; (3) review access.

### 13.1 Least privilege

Saltzer and Schroeder (1975) described least privilege: each user and program gets only the access it needs.

### 13.2 Staff accounts

Staff become standard users; software requests go to Gareth.

### 13.3 Admin accounts

Gareth and the contractor use separate named admin accounts with multi-factor authentication, used only for admin tasks.

### 13.4 Shared accounts

The old shared admin account is disabled so actions can be traced to people.

### 13.5 Reviews

Admin group membership is reviewed monthly.

### MFA for admins

Multi-factor authentication means an admin needs something they know and something they have. If a password is phished, the attacker still lacks the second factor. Bramley uses an authenticator app for Gareth and the contractor.

Aisha also checks whether remote access for staff uses MFA; it does not yet, so it becomes a recommendation for later work.

She documents who holds admin rights on each system and why, creating the first version of an access register.

### Separation of duties

The contractor cannot approve their own access changes; Gareth approves them, and vice versa.

### Request process

A simple form lets staff request software; Gareth aims to respond within two working days.

### Reading the evidence

Aisha compares two sources for this chapter: the relevant NIST guidance and a research paper. The guidance tells her what organisations should do; the paper tells her what tends to happen in practice. Where they differ, she notes the gap and asks which applies to an organisation of Bramley's size. This habit of reading both kinds of source carefully is one the tutor stresses throughout the course.

### Worked example

Removing local admin rights from 25 laptops leads to five requests for software in the first week; Gareth installs them centrally, and requests drop after.

> **Synthetic case.** Synthetic.

### Errors and limits

Removing rights without a request process creates frustration and workarounds.

### Exercises

- **EX037 — Principle.** Who described least privilege? *Rubric:* 3 = Saltzer and Schroeder 1975; 2 = partial; 1 = none; 0 = none.
- **EX038 — Admin use.** How are admin accounts used? *Rubric:* 3 = named, MFA, admin tasks only; 2 = two; 1 = one; 0 = none.
- **EX039 — First week.** What happened after removing admin rights? *Rubric:* 3 = five requests, installed centrally; 2 = partial; 1 = none; 0 = none.

### Synthesis

Least privilege needs a support process.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) identify personal data on endpoints; (2) apply data minimisation; (3) understand breach obligations.

### 14.1 Personal data

Laptops hold tenant names, addresses and support notes. Some notes are sensitive.

### 14.2 Minimisation

Staff should keep tenant data on the file server rather than locally. Less local data means less exposure when a laptop is lost.

### 14.3 Breach duties

Data protection law requires organisations to assess and often report personal data breaches. The stolen laptop was reported because it was unencrypted.

### 14.4 Encryption effect

If a lost laptop is encrypted and the key not compromised, the data are unreadable, which usually changes the breach assessment.

### 14.5 Retention

Old local copies are deleted.

### Breach response basics

When a device is lost, staff report it to Gareth immediately. Gareth checks whether it was encrypted, what data it held and whether it can be wiped remotely. The data protection lead decides whether the regulator must be told. Aisha writes this as a one-page procedure and tests it with a mock report.

During the mock, it takes 20 minutes to confirm encryption status from the management console, which is fast enough for the reporting deadline.

### Data inventory

Aisha also helps list which systems hold tenant data, so the procedure can quickly identify what a lost device might contain.

### Staff guidance

Guidance tells staff never to email tenant data to personal accounts.

### Turning it into a check

Aisha writes a single yes or no question that Gareth can answer each week to show this control is still working, and adds it to the routine.

### Project log entry

Privacy also shapes what Gareth may collect. Device reports carry hostnames and user names, so Aisha agrees with Bramley's manager that reports stay inside IT, are kept for ninety days and are summarised as counts whenever they leave the team, for example in board papers or her dissertation appendices.

### Worked example

Aisha surveys staff and finds many keep local copies "in case the network is slow". Gareth improves offline sync from the file server so local copies are managed and encrypted.

> **Synthetic case.** Synthetic.

### Errors and limits

Privacy controls that ignore staff needs lead to shadow copies.

### Exercises

- **EX040 — Minimisation.** What minimisation step applies to laptops? *Rubric:* 3 = keep tenant data on server; 2 = partial; 1 = none; 0 = none.
- **EX041 — Encryption effect.** How does encryption affect breach assessment? *Rubric:* 3 = data unreadable, changes assessment; 2 = partial; 1 = none; 0 = none.
- **EX042 — Shadow copies.** Why did staff keep local copies? *Rubric:* 3 = slow network; 2 = partial; 1 = none; 0 = none.

### Synthesis

Reduce personal data on endpoints and protect what remains.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) collect evidence with time and source; (2) define measures; (3) avoid misleading numbers.

### 15.1 Evidence

Agent reports, exports and logs, each saved with collection date and source.

### 15.2 Measures

Encryption share, patch latency, unmanaged devices and unneeded server services.

### 15.3 Baselines

The first measurements become the baseline for later comparison.

### 15.4 Honest presentation

Counts with percentages; tails as well as averages.

### 15.5 Storage

Evidence kept read-only.

### Collecting the baseline

Aisha collects baseline evidence in one week: a device export from the management server, an encryption report, the update status for the last monthly release, the asset register and a list of running services on each server. Each file is named with the date and source and stored read-only. She writes a short note describing how each export was produced, so the same steps can be repeated for the evaluation in chapter 39.

She also records what is missing: two laptops did not report at all, so their status is unknown. Rather than guessing, she counts them separately. This honesty matters later, because the evaluation compares like with like.

When she presents the baseline to Gareth, she shows counts first, then percentages, then a short list of the worst cases. Gareth says it is the first time he has seen the whole fleet's state on one page.

### Measures and decisions

Each measure is linked to a decision it supports: encryption share decides rollout priority; patch tails decide where to investigate; unmanaged devices decide inventory work; unneeded services decide server hardening. Measures without a decision are dropped to keep the work focused.

### Review

Dr Grant reviews the baseline method before Aisha starts making changes.

### Note

The baseline date is fixed in the dissertation.

### Worked example

Aisha's baseline table shows 32 of 45 encrypted, 26 of 45 patched within 14 days, 6 unmanaged devices and 4 unneeded server services.

> **Synthetic case.** Synthetic.

### Errors and limits

Measures changed mid-project break comparisons.

### Exercises

- **EX043 — Measures.** List the four measures. *Rubric:* 3 = encryption, latency, unmanaged, services; 2 = three; 1 = two; 0 = none.
- **EX044 — Baseline.** Give the baseline encryption and patch figures. *Rubric:* 3 = 32/45, 26/45; 2 = partial; 1 = none; 0 = none.
- **EX045 — Consistency.** Why keep measures fixed? *Rubric:* 3 = comparisons; 2 = partial; 1 = none; 0 = none.

### Synthesis

A fixed baseline makes improvement measurable.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) design layered endpoint controls; (2) place controls on devices, servers and network; (3) explain dependencies.

### 16.1 Layers

Device: encryption, standard users, firewall, updates, anti-malware. Server: minimal services, named admin accounts. Network: VPN, segmentation. Management: agent reporting, logs.

### 16.2 Defence in depth

If anti-malware misses a file, standard user rights limit what it can change.

### 16.3 Central management

A management agent applies settings and reports status, making Bramley's small IT team effective.

### 16.4 Dependencies

Reporting depends on agents being installed; patching depends on laptops connecting.

### 16.5 Simplicity

Few tools, well configured.

### Proportionate architecture

Bramley's architecture must be simple enough for one IT officer. Aisha avoids adding separate tools for each layer. Instead, the management server applies laptop settings, encryption and updates; the server role documents define services; the VPN and laptop firewall cover network protection; and a weekly routine reviews reports. Each layer is described in one paragraph with its owner and evidence source.

She checks the design against CIS Controls v8 implementation group 1 and finds it covers inventory, secure configuration, account management, data protection, vulnerability management and recovery at a basic level. This gives Bramley's managers confidence that the design is recognised, not improvised.

The architecture also names what it does not cover, such as phones, the website and suppliers' systems, so nobody assumes protection that is not there.

### Failure thinking

For each layer, Aisha asks what happens if it fails. If the management server is down, laptops keep their last settings but miss updates; if the VPN fails, home workers cannot reach files but laptops stay protected by encryption and firewall.

### Ownership

Every layer has one named owner, usually Gareth, with the contractor for servers.

### Worked example

Aisha sketches the architecture and marks the management agent as a key dependency, leading to the inventory work in chapter 22.

> **Synthetic case.** Synthetic.

### Errors and limits

Layers without monitoring may fail unseen.

### Exercises

- **EX046 — Device layer.** List device-layer controls. *Rubric:* 3 = encryption, standard users, firewall, updates, anti-malware; 2 = four; 1 = two; 0 = none.
- **EX047 — Depth example.** Give a defence-in-depth example. *Rubric:* 3 = standard rights limit missed malware; 2 = partial; 1 = none; 0 = none.
- **EX048 — Key dependency.** Which dependency leads to inventory work? *Rubric:* 3 = management agent; 2 = partial; 1 = none; 0 = none.

### Synthesis

Layer controls and manage them centrally.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain symmetric encryption, keys and hashing; (2) describe full-disk encryption; (3) manage recovery keys.

### 17.1 Symmetric encryption

Full-disk encryption uses a symmetric key to encrypt the disk. The key is protected by the TPM and optionally a PIN.

### 17.2 Recovery keys

If the TPM cannot release the key, a recovery key unlocks the disk. Recovery keys are stored in Bramley's directory, accessible only to IT.

### 17.3 Hashing

Hashes detect file changes and verify downloads.

### 17.4 TLS

VPN and web traffic are protected in transit.

### 17.5 Key management

Losing recovery keys can lock out data; leaking them defeats encryption.

### Choosing protectors

Encryption keys can be protected by the TPM alone or by the TPM plus a PIN entered at start-up. TPM-only is convenient: the laptop starts normally and the disk unlocks only if the boot components are as expected. A PIN adds protection against some physical attacks but adds a step for staff. Following Microsoft's BitLocker guidance and its own risk, Bramley chooses TPM-only for most laptops and TPM plus PIN for the two laptops used by the finance manager and chief executive, which hold the most sensitive data.

Aisha records the reasoning so the choice can be revisited if risks change.

She also explains hashing with a practical example: Gareth checks the hash of a downloaded installer against the vendor's published value before deploying it, confirming the file was not corrupted or replaced.

### Testing recovery

Before full rollout, Gareth tests retrieving a recovery key for a lab laptop and unlocking it, timing the process.

### Recovery keys

Recovery keys are stored in the directory, not on paper in desks.

### Worked example

During rollout, a laptop asks for its recovery key after a firmware update. Gareth retrieves it from the directory in two minutes, demonstrating why escrow matters.

> **Synthetic case.** Synthetic.

### Errors and limits

Encryption without recovery planning risks data loss.

### Exercises

- **EX049 — Key protection.** How is the disk key protected? *Rubric:* 3 = TPM, optional PIN; 2 = partial; 1 = none; 0 = none.
- **EX050 — Recovery storage.** Where are recovery keys stored? *Rubric:* 3 = directory, IT only; 2 = partial; 1 = none; 0 = none.
- **EX051 — Firmware event.** What happened after a firmware update? *Rubric:* 3 = recovery key needed, retrieved; 2 = partial; 1 = none; 0 = none.

### Synthesis

Encrypt and plan for recovery.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) form a research question; (2) choose a method; (3) consider ethics.

### 18.1 Question

Do monthly patch reminders sent to staff reduce patch latency?

### 18.2 Method

Compare latency for two months before and after reminders.

### 18.3 Ethics

Data are aggregated; no individual is named.

### 18.4 Limits

Other changes may affect results.

### 18.5 Plan

Pre-state the measure: share within 14 days.

### Designing the study

Aisha's study design is simple but explicit. The population is all 45 laptops. The outcome is the share patched within 14 days for each monthly update. The intervention is a reminder email sent three days after release. The comparison is two months before and two months after. Data come from the management server's update reports, which already exist, so no extra collection is needed.

She writes down in advance what result would count as improvement: a rise of at least five laptops within 14 days. Writing the threshold first prevents her from deciding afterwards that any change is meaningful.

She also lists possible confounders: holidays, new laptops and any other policy changes. Recording them early helps her interpret results honestly in chapter 33.

### Ethics check

The study uses existing device data, aggregated, with no names. Dr Grant confirms it needs only light-touch ethics approval, which she obtains.

### Communication

Staff are told that reminders are being tried and why.

### Sample size

Forty-five laptops is a small sample, so Aisha avoids percentages with false precision and reports counts beside them. She also plans to look at each month separately, since one unusual month could distort an average over only two months.

### Project log entry

Aisha keeps a dated research diary for the reminder study. Each entry notes what data were pulled, any oddities, such as a laptop rebuilt mid-month, and decisions made. When she writes up chapter 33, the diary lets her explain every exclusion instead of reconstructing reasons from memory weeks later.

### Review with the tutor

Dr Grant asks how she would know if the reminders annoyed staff enough to be ignored. Aisha adds a check on reminder open rates and a short end-of-study question, so a fading effect would show up rather than being hidden in averages.

### Worked example

Aisha writes a one-page plan and Dr Grant approves it.

> **Synthetic case.** Synthetic.

### Errors and limits

Before-after designs cannot exclude other causes.

### Exercises

- **EX052 — Question.** State the research question. *Rubric:* 3 = reminders reduce latency?; 2 = partial; 1 = none; 0 = none.
- **EX053 — Measure.** Which measure was pre-stated? *Rubric:* 3 = share within 14 days; 2 = partial; 1 = none; 0 = none.
- **EX054 — Limit.** What is the main limit? *Rubric:* 3 = other changes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plan simple studies carefully.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Systems, endpoints and hardware security: scope and theory

### Learning outcomes

You will (1) define the field's scope; (2) connect theory to Bramley; (3) place endpoint security among other areas.

### 19.1 Scope

The field covers servers, laptops, firmware and hardware: their configuration, updates, integrity and recovery.

### 19.2 Theory

Configuration management (SP 800-128), patch management (SP 800-40r4) and least privilege provide the main theories applied.

### 19.3 Hardware

Firmware and processor issues, such as those shown by Kocher et al. (2019), are fixed by updates, adding to patch volume.

### 19.4 Relation to other areas

Identity, networks and incident response connect to endpoints.

### 19.5 Bramley's place

Small organisations need proportionate controls.

### Why systems security is its own field

Systems and endpoint security sits between hardware, operating systems and organisational practice. It deals with how machines are configured, updated and recovered, and how their hardware and firmware can be trusted. NIST SP 800-53 Rev. 5 includes control families for configuration management, system and information integrity, and maintenance, all central to the field.

For Bramley, the field's concepts translate into practical questions: are all devices known, configured to a baseline, updated in time and recoverable? Aisha uses these four questions as the backbone of her capstone and later chapters.

She also notes topics outside her capstone but within the field, such as firmware integrity and hardware supply chain, and reads introductory material on them to understand the wider landscape.

### Theory into practice

Each theory becomes a routine: configuration management becomes the baseline and weekly checks; patch management becomes the monthly cycle; least privilege becomes standard users and named admin accounts.

### Reading list

Aisha reads NIST SP 800-123 for servers and SP 800-128 for configuration management as her core texts.

### Project log entry

Hardware matters too. NIST SP 800-193 describes platform firmware resiliency: protecting, detecting changes to and recovering firmware. Bramley cannot build such features, but it can buy laptops that support them, keep firmware updated through the vendor tool, and record firmware versions in the inventory alongside operating system versions.

### Worked example

Aisha writes a one-page scope statement for her capstone: laptops and servers at Bramley, excluding phones and the website.

> **Synthetic case.** Synthetic.

### Errors and limits

Unclear scope makes projects grow.

### Exercises

- **EX055 — Field scope.** What does the field cover? *Rubric:* 3 = servers, laptops, firmware, hardware; 2 = partial; 1 = none; 0 = none.
- **EX056 — Theories.** Name three theories applied. *Rubric:* 3 = configuration mgmt, patch mgmt, least privilege; 2 = two; 1 = one; 0 = none.
- **EX057 — Capstone scope.** What does Aisha's capstone exclude? *Rubric:* 3 = phones, website; 2 = partial; 1 = none; 0 = none.

### Synthesis

Define scope with theory and proportion.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Systems, endpoints and hardware security: foundational cases

### Learning outcomes

You will (1) learn from public cases of endpoint failures; (2) extract lessons; (3) apply them to Bramley.

### 20.1 Lost devices

Many reported breaches involve lost or stolen unencrypted laptops; the lesson is encryption by default.

### 20.2 Patch delays

Nappa et al. (2015) found that shared code leaves vulnerable copies unpatched long after fixes; Li and Paxson (2017) found vulnerabilities often persist for years before fixes.

### 20.3 Misconfiguration

Dietrich et al. (2018) found operators link misconfigurations to time pressure and unclear responsibility.

### 20.4 Lessons for Bramley

Encrypt all laptops, measure patch tails, clarify responsibilities.

### 20.5 Using cases

Cases are used to learn, not to blame.

### Turning cases into actions

Each lesson card links a public lesson to a Bramley action. Lost laptops: encryption on every device, verified monthly. Patch delays: measure the tail and investigate each late device. Misconfiguration under pressure: a short checklist for urgent changes and a clear owner for each server.

Aisha discusses the cards at a staff meeting. Staff find the lost-laptop card most relevant because of Bramley's own incident, and two staff admit they had left laptops in cars before. The discussion leads to a simple rule: laptops go home with staff or stay locked in the office, never in a parked car.

She avoids using cases to scare people. Each card ends with what staff can do, not what attackers might do.

### Evaluating sources

Aisha notes that research papers like Li and Paxson (2017) describe large software ecosystems; their findings support the general point that fixes take time to reach users, but their numbers do not apply directly to Bramley.

### Note

Each card is reviewed yearly.

### Project log entry

Aisha also writes a card about Bramley's own stolen laptop, describing what was lost, which controls were missing and what has changed. Staff say this local card is the most persuasive, because they recognise the office, the people and the consequences, including the letters sent to affected tenants.

### Worked example

Aisha writes three lesson cards for Bramley's staff, each with a plain example and action.

> **Synthetic case.** Synthetic.

### Errors and limits

Cases from large firms may not fit small charities directly.

### Exercises

- **EX058 — Lost device lesson.** What lesson comes from lost-laptop cases? *Rubric:* 3 = encryption by default; 2 = partial; 1 = none; 0 = none.
- **EX059 — Nappa.** What did Nappa et al. (2015) find? *Rubric:* 3 = shared code leaves copies unpatched; 2 = partial; 1 = none; 0 = none.
- **EX060 — Dietrich.** What did Dietrich et al. (2018) find? *Rubric:* 3 = time pressure, unclear responsibility; 2 = partial; 1 = none; 0 = none.

### Synthesis

Learn from cases and adapt lessons to context.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Systems, endpoints and hardware security: system models

### Learning outcomes

You will (1) model Bramley's endpoints, servers and management; (2) show data and control flows; (3) identify where controls act.

### 21.1 Components

45 laptops, four servers (file, finance, domain, an old application server), a management server, VPN and backup service.

### 21.2 Control flows

The management server sends settings and updates to agents; agents report status back.

### 21.3 Data flows

Tenant data flow from the file server to laptops and back; finance data stay on the finance server.

### 21.4 Control points

Encryption and standard users on laptops; minimal services on servers; agent reports at the management server.

### 21.5 Model use

The model guides inventory, baseline and service checks in later chapters.

### Checking the model

Aisha checks the model against the asset register and the management server. The model shows four servers; the register agrees; the management server reports only three, because the old application server was never enrolled. This mismatch becomes part of the inventory work in chapter 22.

She also checks data flows with staff: some tenant documents are sent to a partner agency by email. She adds this flow to the model, marking it for review of encryption in transit and data minimisation.

The finished model fits on one page and is stored with the project's documentation.

### Using the model in conversations

When Bramley's managers ask where tenant data live, Aisha points to the model: the file server, laptops through sync, and emails to the partner agency. This helps them understand why encryption and access controls matter at each point.

### Trust boundaries

The model marks where data cross trust boundaries: from laptops to the internet, from the office to the partner agency, and from the contractor's network into servers. Each crossing gets a control.

### Worked example

Drawing the model, Aisha notices the old application server has no backup flow, which Gareth confirms; backup is added.

> **Synthetic case.** Synthetic.

### Errors and limits

Models drift from reality; check them against inventories.

### Exercises

- **EX061 — Components.** List Bramley's four servers. *Rubric:* 3 = file, finance, domain, old application; 2 = three; 1 = two; 0 = none.
- **EX062 — Control flow.** What flows between management server and agents? *Rubric:* 3 = settings and updates out, status back; 2 = partial; 1 = none; 0 = none.
- **EX063 — Backup gap.** What gap did the model reveal? *Rubric:* 3 = old app server lacked backup; 2 = partial; 1 = none; 0 = none.

### Synthesis

Models reveal missing flows and controls.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Systems, endpoints and hardware security: data and dependencies

### Learning outcomes

You will (1) compare the asset register with management agent reports; (2) find unmanaged and unregistered devices; (3) fix dependencies.

### 22.1 Why it matters

Every control depends on the management agent. A device not reporting gets no settings, updates or monitoring. CIS Controls v8 begins with inventory for this reason.

### Lab — Lab — inventory comparison

```python
"""Compare the asset register with devices reporting to the management agent (synthetic, stdlib only)."""
register = {f"BHA-L{i:02d}" for i in range(1, 46)} | {"BHA-S01", "BHA-S02", "BHA-S03", "BHA-S04"}
reporting = (register - {"BHA-L07", "BHA-L19", "BHA-L33", "BHA-S04"}) | {"DESKTOP-7F2K", "BHA-L46"}
print(f"register {len(register)}, reporting {len(reporting)}")
print("in register, not reporting:", ", ".join(sorted(register - reporting)))
print("reporting, not in register:", ", ".join(sorted(reporting - register)))
```

Run with `python3 lab_inventory.py`. Verified output:

```text
register 49, reporting 47
in register, not reporting: BHA-L07, BHA-L19, BHA-L33, BHA-S04
reporting, not in register: BHA-L46, DESKTOP-7F2K
```

### 22.2 Reading the result

The register lists 49 devices; 47 report. Four registered devices are not reporting: laptops L07, L19, L33 and server S04. Two reporting devices are not registered: L46 and DESKTOP-7F2K.

### 22.3 Investigating

L07 is in a drawer; L19 and L33 have broken agents; S04 was never enrolled. L46 is a new laptop not yet registered; DESKTOP-7F2K is a volunteer's personal PC that joined with old credentials.

### 22.4 Fixing

Agents are repaired, S04 is enrolled, L46 registered and the personal PC removed and its access revoked.

### Keeping the inventory current

After fixes, Aisha automates the comparison to run weekly, sending Gareth a short email listing any differences. Joiners' laptops are added to the register when ordered, and leavers' laptops are marked when returned. Within a month, the weekly comparison shows no unexplained differences.

### Resolving the differences

Missing devices L07, L19, L33 and S04 are traced: two laptops were in a drawer awaiting repair, one belonged to a leaver and was never returned, and S04 is the unenrolled application server. The extra entries L46 and DESKTOP-7F2K are a new laptop not yet registered and a reception PC bought by a manager directly. Each is resolved: the leaver's laptop is recovered and wiped, the drawer laptops are recorded as spares, the new laptop is registered and the reception PC is enrolled.

### Worked example

Gareth asks how the personal PC joined. The volunteer used an old enrolment code; Gareth rotates it and limits enrolment to IT.

> **Synthetic case.** Synthetic.

### Errors and limits

Inventory differences need investigation, not just counting.

### Exercises

- **EX064 — Lab counts.** How many registered devices were not reporting, and which? *Rubric:* 3 = 4: L07, L19, L33, S04; 2 = two; 1 = one; 0 = none.
- **EX065 — Unregistered.** Which devices reported but were not registered? *Rubric:* 3 = L46, DESKTOP-7F2K; 2 = partial; 1 = none; 0 = none.
- **EX066 — Personal PC.** How was the personal PC handled? *Rubric:* 3 = removed, access revoked, enrolment code rotated; 2 = partial; 1 = none; 0 = none.

### Synthesis

Reconcile inventories to make every control reach every device.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Systems, endpoints and hardware security: methods I

### Learning outcomes

You will (1) check laptops against a baseline; (2) count gaps by setting; (3) prioritise fixes.

### 23.1 Baseline

Five settings: disk encryption, firewall, screen lock, local admin removed and automatic updates, drawn from CIS Benchmarks and Microsoft's Windows security baselines.

### Lab — Lab — baseline gaps

```python
"""Count baseline gaps per setting across synthetic laptops (stdlib only)."""
import random
random.seed(3)
settings = {"disk_encryption": 0.31, "firewall": 0.04, "screen_lock": 0.18, "local_admin_removed": 0.42, "auto_updates": 0.22}
n = 45
for s, p in settings.items():
    fails = sum(random.random() < p for _ in range(n))
    print(f"{s:20} {fails:2d}/{n} failing")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
disk_encryption      13/45 failing
firewall              1/45 failing
screen_lock           7/45 failing
local_admin_removed  25/45 failing
auto_updates          6/45 failing
```

### 23.2 Reading the result

Local admin removal fails on 25 of 45 laptops, disk encryption on 13, screen lock on 7, automatic updates on 6 and firewall on 1.

### 23.3 Priorities

Encryption first, because of the theft incident; local admin second, because it affects many settings; others follow.

### 23.4 Method

Settings are applied centrally through the management server, not laptop by laptop.

### Why local admin causes drift

Local administrators can change any setting, including the firewall and screen lock, and can install software that changes settings. Removing local admin rights reduces the ways other settings can drift, which is why it ranks second despite encryption's higher impact. Aisha links this reasoning to the drift findings of the master's study her tutor shares.

She also notes that the firewall gap affects only one laptop, so it is fixed immediately rather than waiting for a programme.

### Reporting gaps

The gap table is shared with Gareth weekly until all gaps close, so progress is visible.

### Prioritising gaps

Encryption failing on 13 laptops is the top gap because of the stolen laptop. Local admin on 25 is next, because admin rights let other settings drift. Screen lock on 7 and automatic updates on 6 follow, and the single firewall gap is fixed at once. Aisha orders work by impact and effort, not by count alone.

### Worked example

Aisha presents the gap table. Bramley's manager asks why admin rights matter so much. Aisha links them to chapter 13: with admin rights, staff or malware can undo other settings.

> **Synthetic case.** Synthetic.

### Errors and limits

Fixing the most common gap first is not always right; consider impact.

### Exercises

- **EX067 — Lab result.** Which setting failed most? *Rubric:* 3 = local admin 25/45; 2 = partial; 1 = none; 0 = none.
- **EX068 — Priority.** Why encryption first? *Rubric:* 3 = theft incident, data exposure; 2 = partial; 1 = none; 0 = none.
- **EX069 — Central fix.** How are settings applied? *Rubric:* 3 = centrally via management server; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure baseline gaps and prioritise by impact.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Systems, endpoints and hardware security: controls

### Learning outcomes

You will (1) implement encryption, account and update controls; (2) communicate changes; (3) handle exceptions.

### 24.1 Encryption rollout

Encryption is enabled in groups of ten laptops, with recovery keys escrowed and verified.

### 24.2 Account changes

Local admin is removed with a request process for software.

### 24.3 Update policy

Updates install automatically with a forced restart after seven days' notice.

### 24.4 Exceptions

Two old laptops without TPMs use password-based encryption until replaced.

### 24.5 Communication

Staff receive a short note before each change.

### Pilot group

Before rolling out to all staff, Gareth and Aisha apply each change to a pilot group of five laptops, including one from each team. Pilot users report any problems for a week. The pilot finds one problem: a scanner driver needs admin rights to install, which Gareth then deploys centrally.

After the pilot, rollout proceeds in groups of ten each week, with a pause if more than one problem appears. This approach follows the staged deployment advice in NIST SP 800-40 Rev. 4.

Each group's completion is recorded with the date and any issues.

### Change log

Every change is recorded in a log with date, devices, reason and result.

### Expiry dates

The two TPM-less laptops are scheduled for replacement within six months.

### Rollback

Each change has a rollback step written before rollout, so a problem can be reversed within an hour. During rollout, one group's screen lock setting conflicts with a presentation tool; the rollback is used for that group, the setting is adjusted and the group is redone the next week.

### Project log entry

Communication runs alongside each group. Staff receive a short note two days before their laptop changes, explaining what they will notice, such as a new screen-lock delay, and whom to call. Help requests during rollout fall compared with an earlier unannounced change, which Gareth notes for future projects.

### Review with the tutor

Dr Grant asks what would make her stop the rollout. Aisha writes a stop rule: two help requests about the same setting in one group pauses the next group until the cause is understood.

### Worked example

One staff member's specialist housing software needs admin rights to update. Gareth packages its updates centrally instead.

> **Synthetic case.** Synthetic.

### Errors and limits

Exceptions without expiry become permanent.

### Exercises

- **EX070 — Rollout size.** How was encryption rolled out? *Rubric:* 3 = groups of ten, keys escrowed; 2 = partial; 1 = none; 0 = none.
- **EX071 — Restart policy.** What is the restart policy? *Rubric:* 3 = forced after seven days' notice; 2 = partial; 1 = none; 0 = none.
- **EX072 — TPM exception.** How were laptops without TPMs handled? *Rubric:* 3 = password-based encryption until replaced; 2 = partial; 1 = none; 0 = none.

### Synthesis

Implement controls in stages with communication and managed exceptions.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) triage missing updates by severity and age; (2) identify overdue items; (3) plan remediation.

### 25.1 Policy

Critical updates within 14 days; important within 30.

### Lab — Lab — update triage

```python
"""Triage synthetic missing updates by severity and age (stdlib only)."""
missing = [("BHA-L03", "critical", 41), ("BHA-L11", "important", 12), ("BHA-L19", "critical", 88), ("BHA-S02", "critical", 33),
           ("BHA-L25", "moderate", 60), ("BHA-L33", "important", 47), ("BHA-S03", "important", 5), ("BHA-L40", "critical", 9)]
rank = {"critical": 0, "important": 1, "moderate": 2}
for d, s, age in sorted(missing, key=lambda m: (rank[m[1]], -m[2])):
    flag = "OVERDUE" if (s == "critical" and age > 14) or (s == "important" and age > 30) else ""
    print(f"{d:8} {s:9} {age:3d} days {flag}")
print(f"overdue {sum(1 for d,s,a in missing if (s=='critical' and a>14) or (s=='important' and a>30))}/{len(missing)}")
```

Run with `python3 lab_triage.py`. Verified output:

```text
BHA-L19  critical   88 days OVERDUE
BHA-L03  critical   41 days OVERDUE
BHA-S02  critical   33 days OVERDUE
BHA-L40  critical    9 days 
BHA-L33  important  47 days OVERDUE
BHA-L11  important  12 days 
BHA-S03  important   5 days 
BHA-L25  moderate   60 days 
overdue 4/8
```

### 25.2 Reading the result

Four of eight missing updates are overdue: critical on L19 (88 days), L03 (41) and S02 (33), and important on L33 (47).

### 25.3 Causes

L19 and L33 were not reporting (chapter 22); L03 has a full disk; S02 waits for a maintenance window.

### 25.4 Actions

Agents fixed, disk cleaned, finance server window booked.

### Setting the policy

The 14-day and 30-day windows come from discussion between Gareth and Bramley's manager, informed by NIST SP 800-40 Rev. 4's emphasis on balancing speed and disruption. Critical updates fix flaws that could be exploited easily, so they need quicker action. Aisha writes the policy in one paragraph and the manager approves it.

The triage lab turns the policy into a daily list. Aisha explains that the list is only as accurate as the management server's data, linking back to the inventory work: devices not reporting cannot show missing updates.

She also checks severity labels against vendor descriptions to make sure they are applied consistently.

### Exploitation likelihood

For overdue critical updates, Aisha checks whether the vulnerability is listed as likely to be exploited, using EPSS scores described by Jacobs et al. (2021), to decide which to fix first when several are overdue.

### Exceptions

If an update must be delayed, the delay is recorded with a reason and a new date, and reviewed weekly.

### Project log entry

Gareth keeps the triage list visible on a shared board in the IT room. Each overdue item shows its device, update, days overdue and next action. Seeing four of eight overdue at the first run is uncomfortable, but within two weeks the board is clear and stays mostly clear afterwards.

### Review with the tutor

Dr Grant asks whether the 14-day window suits servers as well as laptops. Aisha keeps it, but notes that server updates wait for the monthly window, so servers are checked against that window instead.

### Worked example

Gareth asks why L40's critical update is not overdue. Aisha shows it is 9 days old, within the 14-day policy.

> **Synthetic case.** Synthetic.

### Errors and limits

Severity alone ignores age; age alone ignores severity.

### Exercises

- **EX073 — Lab overdue.** Which updates were overdue? *Rubric:* 3 = L19, L03, S02 critical; L33 important; 2 = three; 1 = two; 0 = none.
- **EX074 — Causes.** Why were L19 and L33 overdue? *Rubric:* 3 = not reporting; 2 = partial; 1 = none; 0 = none.
- **EX075 — L40.** Why was L40 not overdue? *Rubric:* 3 = 9 days, within 14; 2 = partial; 1 = none; 0 = none.

### Synthesis

Combine severity and age to find overdue updates.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Systems, endpoints and hardware security: methods II

### Learning outcomes

You will (1) harden servers; (2) remove unneeded services; (3) plan server patching.

### 26.1 Server role

Each server's documented role defines needed services.

### 26.2 SP 800-123

NIST's server security guide recommends removing unneeded services and applications and patching regularly.

### 26.3 Patching servers

Servers are patched in a monthly window after backups are verified.

### 26.4 Admin access

Named admin accounts only.

### 26.5 Logging

Server logs go to a central store.

### Role documents

Each server's role document lists purpose, owner, users, needed services, data held, backup method and patch window. For the finance server, the role is the finance application and database, used by three staff, backed up nightly and patched on the second Sunday. For the file server, the role is shared folders and printing for the office.

Writing the role documents takes Aisha and Gareth an afternoon but immediately raises questions: does the file server still need printing, now that printers connect directly? The answer is no, which feeds chapter 30.

Role documents are stored with the server inventory and reviewed yearly.

### Backups before patching

Before each server patch, Gareth confirms the latest backup completed and a restore test was done in the last quarter.

### Contractor access

The contractor's access is limited to the servers they support.

### Patch windows

Servers are patched in a fixed monthly window after the backup check. The finance server is patched after month-end, so staff are not disrupted during busy periods. The window is agreed with staff and published on the calendar, so everyone knows when brief outages may happen.

### Project log entry

Hardening the servers follows the CIS Benchmark for each operating system, applied selectively. Gareth and the contractor go through the benchmark's level one items, mark which apply to each role, and record why any are skipped. Skipped items are few and each has a named reason, such as an application dependency.

### Worked example

Aisha drafts role documents for each server with Gareth; the old application server's role is unclear, prompting a talk with its users.

> **Synthetic case.** Synthetic.

### Errors and limits

Without role documents, nobody knows which services are needed.

### Exercises

- **EX076 — Role doc.** What defines needed services? *Rubric:* 3 = documented role; 2 = partial; 1 = none; 0 = none.
- **EX077 — Patch window.** When are servers patched? *Rubric:* 3 = monthly after backup verification; 2 = partial; 1 = none; 0 = none.
- **EX078 — Unclear role.** What did the old server's unclear role prompt? *Rubric:* 3 = talk with users; 2 = partial; 1 = none; 0 = none.

### Synthesis

Document roles to harden servers.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Systems, endpoints and hardware security: verification

### Learning outcomes

You will (1) verify encryption after rollout; (2) handle unknown and in-progress states; (3) close gaps.

### 27.1 Verification

Agent reports show each laptop's encryption state.

### Lab — Lab — encryption verification

```python
"""Verify disk encryption status after rollout from synthetic agent reports (stdlib only)."""
status = {"encrypted": 40, "encrypting": 2, "not_encrypted": 1, "no_report": 2}
total = sum(status.values())
for k, v in status.items(): print(f"{k:14} {v:2d}")
print(f"verified encrypted {status['encrypted']}/{total} ({status['encrypted']/total*100:.0f}%)")
```

Run with `python3 lab_encrypt.py`. Verified output:

```text
encrypted      40
encrypting      2
not_encrypted   1
no_report       2
verified encrypted 40/45 (89%)
```

### 27.2 Reading the result

40 of 45 verified encrypted (89%); 2 still encrypting, 1 not encrypted and 2 not reporting.

### 27.3 Follow-up

The two encrypting finish overnight; the unencrypted laptop had a failed TPM and is fixed; the two silent laptops are tracked down.

### 27.4 Final state

After follow-up, 45 of 45 are verified.

### Why verify

Turning encryption on is not the same as confirming it is on. Encryption can fail if the TPM is disabled, the disk is full or the laptop is offline during setup. Verification uses agent reports from each laptop, cross-checked by spot-checking five laptops by hand.

Aisha also verifies that each laptop's recovery key is in the directory. One laptop's key is missing because it was encrypted manually before the rollout; Gareth backs up the key and records the fix.

She repeats the verification monthly as part of the weekly routine's monthly extension.

### Reporting

Bramley's manager receives a one-line monthly status: laptops verified encrypted out of total.

### Evidence

Each verification run is saved with its date.

### The five remaining

Of the 45 laptops, 40 are encrypted at first verification. The five remaining include two without a usable TPM, two that were offline and one with a full disk. The offline ones are encrypted when they return; the full disk is cleaned up; the two old laptops get a password protector until replaced. A month later all 45 are verified encrypted.

### Project log entry

Verification also covers removable media. Bramley's policy says files on USB sticks must be encrypted, but checking is harder than for laptops. Aisha recommends issuing encrypted sticks and blocking unknown ones through the management server, and notes this as follow-up work rather than claiming it was done.

### Worked example

One silent laptop is with a staff member on leave; Gareth verifies it on return.

> **Synthetic case.** Synthetic.

### Errors and limits

Counting "encrypting" as done is premature.

### Exercises

- **EX079 — Lab result.** What share was verified encrypted? *Rubric:* 3 = 40/45 (89%); 2 = partial; 1 = none; 0 = none.
- **EX080 — Other states.** Give the other states. *Rubric:* 3 = 2 encrypting, 1 not, 2 no report; 2 = two; 1 = one; 0 = none.
- **EX081 — Final.** What was the final verified count? *Rubric:* 3 = 45/45; 2 = partial; 1 = none; 0 = none.

### Synthesis

Verify every device and resolve each exception.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Systems, endpoints and hardware security: failure analysis

### Learning outcomes

You will (1) analyse update failures by cause; (2) find the biggest fixable causes; (3) reduce failures.

### 28.1 Data

Failure codes from a month of update attempts.

### Lab — Lab — update failures

```python
"""Group synthetic update failure codes by cause (stdlib only)."""
import collections
codes = ["disk_full"]*9 + ["pending_reboot"]*14 + ["offline"]*6 + ["driver_conflict"]*3 + ["unknown"]*2
c = collections.Counter(codes)
for k, v in c.most_common(): print(f"{k:16} {v:2d} ({v/len(codes)*100:.0f}%)")
print(f"total {len(codes)}")
```

Run with `python3 lab_failures.py`. Verified output:

```text
pending_reboot   14 (41%)
disk_full         9 (26%)
offline           6 (18%)
driver_conflict   3 (9%)
unknown           2 (6%)
total 34
```

### 28.2 Reading the result

Of 34 failures, pending reboots cause 14 (41%), full disks 9 (26%), offline laptops 6 (18%), driver conflicts 3 (9%) and unknown 2 (6%).

### 28.3 Fixes

Forced restarts address reboots; disk clean-up tasks address full disks; VPN-based updates address offline laptops.

### 28.4 Re-measure

Next month failures fall.

### Pending reboots

Updates often need a restart to complete. Staff postpone restarts because they are busy. A forced restart after seven days' notice, introduced in chapter 24, addresses this. Aisha also suggests a friendly reminder on day five.

For full disks, a scheduled clean-up removes temporary files; two laptops need larger disks. For offline laptops, internet-based management removes the dependence on the VPN.

The next month, failures drop from 34 to 15, with pending reboots falling most. Aisha reports this with the caveat that one month may vary.

### Unknown failures

The two unknown failures are investigated individually; one is a corrupted update cache, fixed by resetting it.

### Driver conflicts

Driver conflicts are reported to the laptop vendor.

### Reading the breakdown

The 34 failures split into reboot 14, disk 9, offline 6, driver 3 and unknown 2. Most have simple, routine causes. Aisha explains that this is common: update failures are mostly operational, not mysterious, and grouping them by cause turns a frustrating list into a short set of fixes. She records the breakdown monthly so trends can be seen.

### Project log entry

Aisha draws a simple chart of failures by cause each month. After the fixes, the reboot bar shrinks most sharply, the disk bar more slowly as two disk upgrades wait for delivery. The chart makes the effect of each fix visible to Gareth without any statistics beyond counting.

### Worked example

Gareth was planning to buy a new patch tool. The analysis shows most failures come from reboots and disks, which policy changes fix without new tools.

> **Synthetic case.** Synthetic.

### Errors and limits

Tools rarely fix process causes.

### Exercises

- **EX082 — Top cause.** What was the top failure cause? *Rubric:* 3 = pending reboot 41%; 2 = partial; 1 = none; 0 = none.
- **EX083 — Second.** What was second? *Rubric:* 3 = disk full 26%; 2 = partial; 1 = none; 0 = none.
- **EX084 — Tool decision.** Why not buy a new tool? *Rubric:* 3 = causes are process; 2 = partial; 1 = none; 0 = none.

### Synthesis

Analyse failures before buying solutions.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Systems, endpoints and hardware security: operations

### Learning outcomes

You will (1) review admin logons; (2) set simple alerts; (3) run a weekly routine.

### 29.1 Logon review

Admin logons to servers are reviewed weekly.

### Lab — Lab — admin logons

```python
"""Review synthetic administrator logons and flag unusual ones (stdlib only)."""
logons = [("it-gareth", "BHA-S01", "09:12"), ("it-gareth", "BHA-S02", "10:40"), ("it-contractor", "BHA-S03", "14:05"),
          ("it-gareth", "BHA-L22", "11:30"), ("admin", "BHA-S04", "02:47"), ("it-contractor", "BHA-S01", "23:15"),
          ("it-gareth", "BHA-S01", "16:20")]
named = {"it-gareth", "it-contractor"}
for u, h, t in logons:
    hr = int(t[:2]); flags = []
    if u not in named: flags.append("shared/default account")
    if hr < 7 or hr >= 20: flags.append("out of hours")
    if flags: print(f"{t} {u:14} {h}: {', '.join(flags)}")
print(f"logons {len(logons)}")
```

Run with `python3 lab_logons.py`. Verified output:

```text
02:47 admin          BHA-S04: shared/default account, out of hours
23:15 it-contractor  BHA-S01: out of hours
logons 7
```

### 29.2 Reading the result

Of 7 logons, 2 are flagged: the default "admin" account on S04 at 02:47, and the contractor on S01 at 23:15.

### 29.3 Investigation

The 23:15 logon was planned maintenance; the 02:47 default-account logon was a scheduled task using the old account, which is reconfigured and the account disabled.

### 29.4 Routine

Weekly: logon review, failed updates, unmanaged devices.

### What logon records show

Windows records successful and failed sign-ins in its security log, and the management server can collect them centrally. NIST SP 800-92 describes log management as collecting, storing and reviewing records so that unusual events can be noticed. For Bramley, the question is modest: did anyone sign in to a server at a strange hour, or fail many times in a row?

Aisha's lab reads seven synthetic records, each with an account, a server, an hour and a result. It flags records outside working hours and accounts with repeated failures. Two of seven are flagged: a late-night sign-in by the contractor account and three failures by a staff account.

Gareth checks both. The contractor was doing agreed maintenance, which had not been written in the change log; the staff member had forgotten a changed password. Neither is an incident, but both lead to small improvements: contractors now log planned work in advance, and the password reset process is explained again.

Aisha stresses that a flag is a question, not a verdict. Most flags will have ordinary explanations, and the point of the review is to know them.

### Keeping the review small

A weekly ten-minute review is sustainable for one officer; a daily hour is not. The flags are therefore tuned to produce a handful of items per week. If the list grows long, the rules are adjusted rather than ignored.

### Privacy

Logon records are personal data. They are kept for 90 days, viewed only by IT and used only for security.

### Contractor access

Contractor accounts are enabled only for agreed maintenance windows.

### Worked example

Aisha writes the weekly routine as a one-page checklist taking about 30 minutes.

> **Synthetic case.** Synthetic.

### Errors and limits

Out-of-hours alone is not suspicious; check context.

### Exercises

- **EX085 — Lab flags.** Which logons were flagged? *Rubric:* 3 = admin S04 02:47; contractor S01 23:15; 2 = partial; 1 = none; 0 = none.
- **EX086 — 02:47 cause.** What explained the 02:47 logon? *Rubric:* 3 = scheduled task with old account; 2 = partial; 1 = none; 0 = none.
- **EX087 — Routine.** What does the weekly routine cover? *Rubric:* 3 = logons, failed updates, unmanaged; 2 = two; 1 = one; 0 = none.

### Synthesis

Simple weekly reviews catch leftovers.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) compare running services with documented needs; (2) remove unneeded services; (3) verify servers.

### 30.1 Purpose

Applying SP 800-123's advice to Bramley's servers.

### Lab — Lab — server services

```python
"""Compare running services on synthetic servers with documented needs, per SP 800-123 (stdlib only)."""
servers = {"BHA-S01 file": ({"smb", "backup-agent", "mgmt-agent", "print-spooler", "telnet"}, {"smb", "backup-agent", "mgmt-agent"}),
           "BHA-S02 finance": ({"db", "backup-agent", "mgmt-agent", "web-admin"}, {"db", "backup-agent", "mgmt-agent"}),
           "BHA-S03 domain": ({"directory", "dns", "mgmt-agent", "backup-agent"}, {"directory", "dns", "mgmt-agent", "backup-agent"}),
           "BHA-S04 old-app": ({"legacy-app", "ftp", "mgmt-agent"}, {"legacy-app", "mgmt-agent"})}
t = 0
for s, (run, need) in servers.items():
    extra = sorted(run - need); t += len(extra)
    print(f"{s}: {'ok' if not extra else 'unneeded: ' + ', '.join(extra)}")
print(f"unneeded services {t}")
```

Run with `python3 lab_services.py`. Verified output:

```text
BHA-S01 file: unneeded: print-spooler, telnet
BHA-S02 finance: unneeded: web-admin
BHA-S03 domain: ok
BHA-S04 old-app: unneeded: ftp
unneeded services 4
```

### 30.2 Reading the result

Four unneeded services: print-spooler and telnet on the file server, web-admin on finance and ftp on the old application server. The domain server is fine.

### 30.3 Removal

Each is disabled after checking with users and testing.

### 30.4 Verification

A re-run shows zero unneeded services.

### Fewer services, fewer worries

Every running service is code that must be patched and configured. Saltzer and Schroeder (1975) described economy of mechanism and least privilege: keep systems as simple as possible and give each part only what it needs. The CIS Benchmarks put this into practice by recommending that unneeded services be disabled.

Aisha's lab compares each server's running services against its role document. The file server still runs a print spooler, although printers now connect directly; the old application server runs a web service nobody uses; and two other leftover services appear. Four services in total are unneeded.

Gareth disables them one at a time, after checking with users and noting each change. He waits a week between changes so any problem can be traced to a single step. No problems appear.

The role documents and the service list now agree, and the lab runs monthly to catch new services that appear after software installs.

### Checking with owners

Before turning anything off, Gareth asks the server owner and the contractor whether the service is used. Asking first avoids surprises and builds trust.

### Re-enabling

Each disabled service has a note on how to turn it back on if needed.

### Firewall rules

Matching firewall rules for the disabled services are removed too.

### Worked example

The finance team uses web-admin occasionally. It is replaced by remote access through the admin workstation.

> **Synthetic case.** Synthetic.

### Errors and limits

Removing services without asking users can break workflows.

### Exercises

- **EX088 — Lab result.** How many unneeded services and where? *Rubric:* 3 = 4: file (2), finance (1), old app (1); 2 = two; 1 = one; 0 = none.
- **EX089 — Verification.** What did the re-run show? *Rubric:* 3 = zero; 2 = partial; 1 = none; 0 = none.
- **EX090 — Finance.** How was web-admin replaced? *Rubric:* 3 = remote access via admin workstation; 2 = partial; 1 = none; 0 = none.

### Synthesis

Remove unneeded services and verify.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Systems, endpoints and hardware security: advanced cases

### Learning outcomes

You will (1) handle harder endpoint cases; (2) balance security with service; (3) document decisions.

### 31.1 Legacy server

The old application server runs software that only works on an unsupported OS. Options: replace, isolate or accept risk. Bramley isolates it on its own segment with limited access while a replacement is procured.

### 31.2 Firmware updates

Vendor firmware updates fix hardware-level issues such as speculative execution flaws (Kocher et al., 2019). Bramley applies them in small groups after checking recovery keys, because firmware changes can trigger recovery prompts.

### 31.3 Volunteers

Volunteers sometimes need temporary access. They get managed loan laptops rather than using personal devices.

### 31.4 Home Wi-Fi

Staff home networks are outside Bramley's control; the laptop firewall and VPN protect traffic.

### 31.5 Decision records

Each case has a written decision with reasons.

### Writing the routine

The weekly routine is a one-page checklist Gareth follows every Monday morning: review the inventory comparison, check update compliance and overdue items, confirm backups completed, scan the logon flags, and note anything unusual. Monthly, he adds the encryption verification and the services check. Each step names its report and the expected time.

Aisha times the routine over three weeks; it takes about forty minutes. She trims one step that duplicated another, bringing it under thirty-five minutes.

The routine includes what to do when something looks wrong: record it, decide if it is urgent, and fix or schedule. Urgent items, such as an unencrypted laptop or a missing backup, are handled the same day.

### Cover

A colleague is trained to follow the routine when Gareth is on leave.

### Records

Each week's completed checklist is saved, building evidence for audits.

### Worked example

The legacy software vendor offers a supported version next year. The isolation decision records an expiry date aligned to the upgrade.

> **Synthetic case.** Synthetic.

### Errors and limits

Isolation without an end date becomes permanent.

### Exercises

- **EX091 — Legacy options.** What options existed for the legacy server? *Rubric:* 3 = replace, isolate, accept; 2 = two; 1 = one; 0 = none.
- **EX092 — Firmware care.** Why check recovery keys before firmware updates? *Rubric:* 3 = may trigger recovery prompts; 2 = partial; 1 = none; 0 = none.
- **EX093 — Volunteers.** How do volunteers get access? *Rubric:* 3 = managed loan laptops; 2 = partial; 1 = none; 0 = none.

### Synthesis

Hard cases need documented, time-limited decisions.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Systems, endpoints and hardware security: interdisciplinary interfaces

### Learning outcomes

You will (1) connect endpoint security with HR, finance and law; (2) coordinate across roles.

### 32.1 HR

New staff get laptops configured before day one; leavers' accounts are disabled on their last day and laptops wiped.

### 32.2 Finance

Budget for replacing old laptops is planned three years ahead.

### 32.3 Law

Data protection duties shape encryption and breach response.

### 32.4 Facilities

Laptops are stored securely overnight in the office.

### 32.5 Coordination

A short monthly meeting covers joiners, leavers and purchases.

### Why recovery matters

Hardening reduces how often things go wrong; recovery decides how bad it is when they do. NIST SP 800-34 and the CIS Controls both stress tested backups and planned restoration. For Bramley, the key systems are the finance server and file server, and the key question is how long staff can work without them.

Aisha and Bramley's manager agree targets: the file server should be back within one working day with no more than one day's data lost; the finance server within two days. Laptops can be rebuilt from the management server in about two hours each, since data sync to the file server.

A restore test is run on a spare machine: Gareth restores the file server's backup and checks a sample of folders. It takes five hours, within the target. The finance database restore reveals that the application's licence file was not in the backup, which is fixed.

This test shows why backups must be restored, not just made: the missing file would have caused days of delay in a real event.

### Offline copy

One backup copy is kept offline and rotated weekly, protecting against ransomware that might reach online backups.

### Recovery contacts

A short list of contacts, including the contractor and the finance software vendor, is stored with the plan, on paper as well as online.

### Laptop loss

For a lost laptop, the steps are: report, confirm encryption, revoke access, issue a replacement.

### Worked example

HR forgot to tell IT about a leaver; the monthly meeting now includes a leavers list check.

> **Synthetic case.** Synthetic.

### Errors and limits

Security gaps often lie between departments.

### Exercises

- **EX094 — Leavers.** What happens for leavers? *Rubric:* 3 = disable on last day, wipe laptop; 2 = partial; 1 = none; 0 = none.
- **EX095 — Finance link.** How does finance support security? *Rubric:* 3 = planned replacements; 2 = partial; 1 = none; 0 = none.
- **EX096 — Gap.** What gap did the meeting close? *Rubric:* 3 = unreported leaver; 2 = partial; 1 = none; 0 = none.

### Synthesis

Endpoint security depends on other departments.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse the reminder study; (2) interpret results; (3) state limits.

### 33.1 Results

Share within 14 days rose from 26 of 45 to 33 of 45 after reminders.

### 33.2 Confounders

Forced restarts started the same month, so reminders cannot take all credit.

### 33.3 Conclusion

Reminders plus forced restarts are associated with improvement.

### 33.4 Ethics

No individual is named.

### 33.5 Next

A future study could stagger changes.

### Reading the result

The reminder study compares two months before with two months after. Before, an average of 26 of 45 laptops were patched within 14 days; after, 33. The rise of seven exceeds the five-laptop threshold set in advance, so Aisha reports a likely improvement.

She is careful with the claim. The after period included the new forced restart policy, which may also have helped. With only two months on each side, chance variation is possible. She therefore says the reminders and restart policy together were associated with improvement, and recommends continuing both while monitoring.

Dr Grant praises the honest wording and suggests a longer comparison as future work.

### Staff feedback

A short survey finds most staff found the reminders helpful and not annoying; three asked for fewer emails, so reminders are combined into one weekly message.

### What would change the conclusion

If compliance fell back after reminders stopped, that would support their effect; Aisha notes this as a test.

### Data

All data are aggregated counts.

### Checking month by month

Looking at each month separately, the before months show 25 and 27 laptops patched within 14 days, and the after months show 32 and 34. The rise holds in both after months, which makes chance a less likely explanation, though not impossible.

### Project log entry

Aisha also reports what she cannot conclude. She cannot say reminders alone caused the rise, nor that the effect will last. She can say that the result met the threshold set in advance, held in both months, and did not come with complaints from staff.

### Worked example

Dr Grant asks Aisha to rewrite "reminders worked" as "improvement coincided with reminders and forced restarts".

> **Synthetic case.** Synthetic.

### Errors and limits

Simultaneous changes confound simple comparisons.

### Exercises

- **EX097 — Result.** How did the share change? *Rubric:* 3 = 26→33 of 45; 2 = partial; 1 = none; 0 = none.
- **EX098 — Confounder.** What confounds the result? *Rubric:* 3 = forced restarts same month; 2 = partial; 1 = none; 0 = none.
- **EX099 — Rewrite.** How was the conclusion rewritten? *Rubric:* 3 = coincided with both; 2 = partial; 1 = none; 0 = none.

### Synthesis

Name confounders honestly.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare Bramley with a similar organisation; (2) identify transferable practices.

### 34.1 Partner

A second charity of similar size shares anonymised measures.

### 34.2 Comparison

It encrypts all laptops but patches more slowly.

### 34.3 Practices

It uses a simple loan-laptop scheme Bramley adopts; Bramley shares its forced restart policy.

### 34.4 Limits

Organisations differ in staff and software.

### 34.5 Value

Comparison suggests ideas, not proof.

### Explaining to non-specialists

Bramley's board includes tenants and volunteers without technical backgrounds. Aisha writes the board summary in plain words: what happened with the stolen laptop, what has changed, what the numbers show and what still needs money or time. She avoids terms like TPM and baseline, or explains them in a sentence.

The summary leads with the main message: every laptop is now encrypted, so a stolen laptop would no longer expose tenant data. Then it shows four before-and-after numbers and two remaining risks: the old application server and limited IT cover.

Board members ask good questions, such as what happens if Gareth leaves; the answer is the documented routine and a trained colleague. The board approves funding to replace the old server.

### One page

The summary fits on one page with a small table. Detail is in an appendix for those who want it.

### Tone

The tone is calm and factual, crediting staff for cooperating.

### Follow-up

A six-month update to the board is scheduled.

### Visuals

One simple bar chart shows the four before-and-after measures side by side. Aisha avoids colours that carry no meaning and labels every bar with its count, so the board can read it at a glance.

### Project log entry

Before the meeting, Aisha rehearses the presentation with Gareth playing a sceptical board member. His questions about cost and staff time lead her to add a single line showing hours spent, which turns out to be the board's first question.

### Worked example

Both charities agree to share measures quarterly.

> **Synthetic case.** Synthetic.

### Errors and limits

Comparing without context can mislead.

### Exercises

- **EX100 — Difference.** How did the other charity differ? *Rubric:* 3 = all encrypted, slower patching; 2 = partial; 1 = none; 0 = none.
- **EX101 — Exchange.** What practices were exchanged? *Rubric:* 3 = loan laptops; forced restarts; 2 = partial; 1 = none; 0 = none.
- **EX102 — Agreement.** What did they agree? *Rubric:* 3 = quarterly sharing; 2 = partial; 1 = none; 0 = none.

### Synthesis

Comparisons spread good practice.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) propose a capstone; (2) define scope, method and success criteria.

### 35.1 Proposal

A sustainable endpoint security programme for Bramley.

### 35.2 Scope

Laptops and servers; excludes phones and website.

### 35.3 Method

Baseline, implement, verify, measure, hand over.

### 35.4 Criteria

100% encrypted; 90% patched within 14 days; zero unneeded services; unmanaged devices at most one.

### 35.5 Approval

Dr Grant and Bramley approve.

### Professional responsibilities

IT staff have privileged access, which brings duties: use access only for work, respect privacy, report problems honestly and keep skills current. Professional codes, such as those of the BCS and ACM, express these duties. Aisha discusses them with Gareth, who notes that small organisations rarely write them down but rely on them heavily.

In the project, these duties show up in concrete choices. Logon records are reviewed only for security. Survey data are anonymous. The stolen laptop incident is reported to the regulator as required, and the report is honest about what was not in place.

Aisha also considers her own role as a student: she has access only to synthetic copies and summary reports, not tenant records, which Bramley's manager confirms in writing.

### Raising concerns

If Aisha had found something serious, such as an ongoing breach, the agreed route was to tell Gareth and the manager immediately, not to investigate alone.

### Learning

She lists courses Gareth could take to keep skills current, within budget.

### Accountability

Every privileged action in the project is traceable to a named account and a recorded reason. This protects staff as well as tenants, because it shows that access was used properly.

### Project log entry

The capstone proposal itself is reviewed for ethics: it states what data are used, who sees them, how long they are kept and how staff are informed. Bramley's manager signs the proposal, giving Aisha clear written permission for the work she will do.

### Worked example

Gareth asks whether 90% is ambitious. Aisha shows the current 73% after reminders and argues 90% is achievable with forced restarts.

> **Synthetic case.** Synthetic.

### Errors and limits

Criteria without a baseline are guesses.

### Exercises

- **EX103 — Criteria.** State the success criteria. *Rubric:* 3 = 100% enc, 90% patched, 0 services, ≤1 unmanaged; 2 = three; 1 = two; 0 = none.
- **EX104 — Method.** Give the method steps. *Rubric:* 3 = baseline, implement, verify, measure, handover; 2 = four; 1 = two; 0 = none.
- **EX105 — 90% case.** Why is 90% achievable? *Rubric:* 3 = 73% now plus forced restarts; 2 = partial; 1 = none; 0 = none.

### Synthesis

Base criteria on measured baselines.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) support Bramley staff directly; (2) teach simple habits; (3) gather feedback.

### 36.1 Sessions

Aisha runs short sessions on locking screens, reporting lost devices and restart notices.

### 36.2 Desk time

She spends two afternoons at Bramley answering questions.

### 36.3 Feedback

Staff ask for clearer restart messages.

### 36.4 Changes

Messages are rewritten.

### 36.5 Boundaries

She does not access tenant data.

### Sustaining the work

Projects often fade when the student leaves. To avoid this, Aisha hands over everything Bramley needs: the weekly routine, the labs as small scripts with instructions, the role documents, the recovery plan and the decision log. Each document names an owner and a review date.

She also runs two handover sessions, one with Gareth and one with the colleague who covers him. In each session, they perform the routine together while Aisha watches and answers questions. Small improvements to the instructions come out of these sessions.

Six weeks after handover, Aisha checks in: the routine has run every week, and one new laptop was correctly added and encrypted.

### Budget

Ongoing costs are small: the existing management licences and staff time of about one hour a week.

### Keeping documents alive

Documents are reviewed yearly or after any incident, whichever comes first.

### Escalation

The contractor remains the escalation route for server problems.

### Measuring sustainability

Aisha defines success after handover as the routine running at least three weeks in four and no unexplained inventory differences for a month. Both are met at the six-week check.

### Project log entry

Community practice also means sharing. With the manager's approval, Aisha writes an anonymised two-page guide for other small housing associations on the routine and baseline, using only synthetic examples and no Bramley details that could identify systems.

### Review with the tutor

Dr Grant asks how Bramley would notice if the routine quietly stopped. Aisha suggests the manager glances at the saved weekly checklists each month, a two-minute check that makes gaps visible.

### Worked example

A staff member reports a lost USB stick; Aisha helps Gareth follow the incident process.

> **Synthetic case.** Synthetic.

### Errors and limits

Training without follow-up fades.

### Exercises

- **EX106 — Topics.** What did sessions cover? *Rubric:* 3 = screen lock, reporting lost devices, restarts; 2 = two; 1 = one; 0 = none.
- **EX107 — Feedback.** What did staff ask for? *Rubric:* 3 = clearer restart messages; 2 = partial; 1 = none; 0 = none.
- **EX108 — USB event.** What did Aisha do about the lost USB stick? *Rubric:* 3 = helped Gareth follow incident process; 2 = partial; 1 = none; 0 = none.

### Synthesis

Community practice builds habits.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) review evidence critically; (2) challenge claims; (3) improve evidence quality.

### 37.1 Seminar

Students present evidence for their projects; peers challenge.

### 37.2 Aisha's evidence

Agent reports, logs, lab outputs and staff feedback.

### 37.3 Challenge

A peer asks whether agent reports can be wrong. Aisha spot-checks five laptops by hand; all match.

### 37.4 Improvement

She adds spot checks to the routine.

### 37.5 Lesson

Evidence from one source should be cross-checked.

### Limitations

The project has clear limits. It covers laptops and servers but not phones or the website. Data come from one organisation over a few months, so results may not generalise. The reminder study had no control group. Some measures depend on the management server's reports, which can miss devices that do not check in.

Aisha states these limits plainly in her dissertation. Dr Grant explains that examiners respect honest limits more than inflated claims, and that limits also point to future work.

She proposes three follow-ups: extend management to phones, run the reminder comparison for a full year, and test recovery for the finance server again after its replacement.

### Generalising carefully

Other small housing associations may find the approach useful, but should adapt targets and tools to their size and risk.

### Threats to validity

Seasonal patterns and staff changes may affect patch results.

### Reflection

Aisha notes that she underestimated how long checking with staff would take.

### Measurement limits

Several measures depend on devices reporting. A device that stops reporting can look compliant by omission, so Aisha counts non-reporting devices separately in every result.

### Project log entry

In the evidence review seminar, peers challenge each other's claims. A classmate asks whether Bramley's encryption rate would have risen anyway after the theft. Aisha agrees that the theft created urgency and says verification, not motivation, is what her lab measures.

### Review with the tutor

Dr Grant asks which limitation worries her most. She names non-reporting devices, because they can make results look better than reality, and explains how each table counts them separately.

### Worked example

Another peer asks about staff feedback bias; Aisha notes it is self-selected.

> **Synthetic case.** Synthetic.

### Errors and limits

Unchecked evidence can be confidently wrong.

### Exercises

- **EX109 — Challenge.** What challenge did a peer raise? *Rubric:* 3 = agent reports wrong?; 2 = partial; 1 = none; 0 = none.
- **EX110 — Spot check.** How was it answered? *Rubric:* 3 = five laptops checked by hand, all match; 2 = partial; 1 = none; 0 = none.
- **EX111 — Feedback bias.** What bias affects staff feedback? *Rubric:* 3 = self-selected; 2 = partial; 1 = none; 0 = none.

### Synthesis

Cross-check evidence sources.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) complete the programme; (2) run routines; (3) document.

### 38.1 Implementation

All controls in place; weekly routine running.

### 38.2 Documentation

Runbooks for encryption, updates, inventory and server checks.

### 38.3 Training

Gareth's assistant is trained.

### 38.4 Issues

A failed laptop needs reimaging; documented process works.

### 38.5 Timeline

Completed in one term.

### Structuring the dissertation

The dissertation follows a standard structure: introduction, background, method, design and implementation, evaluation, discussion and conclusion. Each chapter answers a question: why it matters, what is known, how the work was done, what was built, what changed and what it means. Aisha writes the method chapter first, since it was already planned, and the introduction last.

She uses the references in the course list, citing standards for practices and papers for evidence. Every figure is checked against its source data, and the labs' outputs are reproduced in an appendix with the synthetic data used.

Dr Grant reviews drafts chapter by chapter. His main comments are to shorten the background, make the evaluation table clearer and move detailed procedures to appendices.

### Writing clearly

Aisha uses short sentences, active voice and defined terms. Each paragraph starts with its main point.

### Academic integrity

All sources are cited; quoted text is marked; the tutor's suggestions are acknowledged.

### Deadlines

She plans two weeks for final proofreading.

### Appendices

Appendices hold the labs, synthetic data, role documents and the routine, so the main text stays readable while every claim remains checkable.

### Project log entry

Implementation is tracked against the proposal's plan. Two tasks slip, the server replacement and phone management, both outside her control. She records the slips, their reasons and the new owners rather than quietly dropping them from the dissertation.

### Review with the tutor

Dr Grant asks which claim in the draft is weakest. She points to the staff survey, which had few responses, and softens the wording accordingly.

### Worked example

Gareth's assistant runs the weekly routine alone and finds an unmanaged new laptop, enrolling it.

> **Synthetic case.** Synthetic.

### Errors and limits

Programmes reliant on one person are fragile.

### Exercises

- **EX112 — Runbooks.** Which runbooks exist? *Rubric:* 3 = encryption, updates, inventory, server checks; 2 = three; 1 = two; 0 = none.
- **EX113 — Training.** Who was trained? *Rubric:* 3 = Gareth's assistant; 2 = partial; 1 = none; 0 = none.
- **EX114 — Routine finding.** What did the assistant find? *Rubric:* 3 = unmanaged new laptop; 2 = partial; 1 = none; 0 = none.

### Synthesis

Document and train so the programme lasts.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) compare before and after measures; (2) judge success; (3) state limits.

### 39.1 Measures

Same as the baseline from chapter 15.

### Lab — Lab — before and after

```python
"""Before and after metrics for Bramley's endpoint programme (synthetic, stdlib only)."""
m = [("laptops encrypted", 32, 45, 45, 45), ("patched within 14 days", 26, 45, 41, 45),
     ("unneeded server services", 4, None, 0, None), ("unmanaged devices", 6, None, 1, None)]
for name, b, bt, a, at in m:
    if bt: print(f"{name}: {b}/{bt} -> {a}/{at}")
    else: print(f"{name}: {b} -> {a}")
```

Run with `python3 lab_compare.py`. Verified output:

```text
laptops encrypted: 32/45 -> 45/45
patched within 14 days: 26/45 -> 41/45
unneeded server services: 4 -> 0
unmanaged devices: 6 -> 1
```

### 39.2 Reading the result

Encrypted laptops rose from 32 to 45 of 45; patched within 14 days from 26 to 41 of 45; unneeded server services fell from 4 to 0; unmanaged devices from 6 to 1.

### 39.3 Against criteria

Encryption, services and unmanaged criteria met; patching at 91% meets the 90% target.

### 39.4 Limits

One organisation, a few months, other changes coincided.

### Before and after

The evaluation lab compares the baseline with the final measures. Encrypted laptops rose from 32 to 45; laptops patched within 14 days rose from 26 to 41; unneeded server services fell from 4 to 0; unmanaged devices fell from 6 to 1. The remaining unmanaged device is the old application server, due for replacement.

Aisha presents the numbers with their sources and dates, and repeats the measurement method from chapter 15 so the comparison is fair. Where a number depends on reporting devices, she notes how many reported.

She links each change to the action that caused it, while acknowledging that several actions overlapped, as discussed in chapter 33.

### Unchanged measures

Some measures barely moved, such as screen lock compliance, which was already high; she reports these too, rather than only successes.

### Cost of the work

Total staff time over the project was roughly 60 hours for Gareth, which the manager judges good value.

### Answering the research question

Aisha's question was whether a small organisation could reach and keep a basic secure endpoint baseline with one officer. The evidence says yes, with clear routines and modest tools.

### Project log entry

Aisha checks the evaluation against her original research question and success criteria from the proposal. Three of four criteria are fully met; the unmanaged device target misses by one because of the old server, which she reports plainly with its replacement date.

### Worked example

Bramley's board asks what the stolen-laptop incident would look like now. Aisha explains that an encrypted laptop's data would be unreadable, likely changing the breach assessment.

> **Synthetic case.** Synthetic.

### Errors and limits

Short evaluation periods may not show seasonal problems.

### Exercises

- **EX115 — Lab results.** Give the four before-and-after figures. *Rubric:* 3 = 32→45, 26→41, 4→0, 6→1; 2 = three; 1 = two; 0 = none.
- **EX116 — Patching target.** Was the patching target met? *Rubric:* 3 = 41/45 = 91% ≥ 90%; 2 = partial; 1 = none; 0 = none.
- **EX117 — Incident now.** How would the incident differ now? *Rubric:* 3 = data unreadable; 2 = partial; 1 = none; 0 = none.

### Synthesis

Evaluate against pre-set criteria and state limits.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write and present the capstone; (2) reflect on learning; (3) plan next steps.

### 40.1 Thesis

Problem, baseline, design, implementation, evaluation, limits.

### 40.2 Presentation

Aisha presents to Thornbury and Bramley.

### 40.3 Questions

About cost, staff acceptance and sustainability.

### 40.4 Reflection

She learned that small organisations need simple, well-run controls more than advanced tools.

### 40.5 Next

She plans graduate study in systems security.

### Looking back

At the end, Aisha reviews the journey from the stolen laptop to a measured, maintained fleet. The key lessons are simple: know your devices, set and keep a baseline, update in time, encrypt, keep only needed services, review logs lightly and test recovery. None of these is new, but doing them consistently in a small organisation takes planning and patience.

She credits Gareth and Bramley's staff, whose cooperation made the changes stick. She also notes what she would do differently: involve staff earlier and plan more time for checking with users.

The dissertation is submitted on time, and Bramley keeps the routine running after she leaves.

### Career reflections

Aisha considers roles in IT operations and security, and notes the value of being able to explain technical work to boards.

### Future work

Extending management to phones is the top recommendation.

### Thanks

She thanks her tutor, Gareth and the staff.

### Final message

The final message to Bramley is that security is maintained, not finished. The routine, owners and review dates keep the work alive, and the board update keeps it visible. Aisha closes by noting that the stolen laptop, painful at the time, became the reason Bramley's endpoints are now well managed.

### Project log entry

At the presentation, examiners ask what she would recommend to an organisation with no IT officer. She suggests a managed service with the same routine written into the contract, so the checks still happen and are still reported.

### Worked example

Gareth says the weekly routine is now part of his job description.

> **Synthetic case.** Synthetic.

### Errors and limits

Reflection should be specific.

### Exercises

- **EX118 — Structure.** Give the thesis structure. *Rubric:* 3 = problem, baseline, design, implementation, evaluation, limits; 2 = four; 1 = two; 0 = none.
- **EX119 — Questions.** What topics were asked? *Rubric:* 3 = cost, acceptance, sustainability; 2 = two; 1 = one; 0 = none.
- **EX120 — Lesson.** What did Aisha learn? *Rubric:* 3 = simple well-run controls over advanced tools; 2 = partial; 1 = none; 0 = none.

### Synthesis

Present results and reflect specifically.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Aisha Rahman, Dr Lewis Grant, Gareth Lloyd, Thornbury University, Bramley Housing Association and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** A stolen, unencrypted laptop holding tenant records.

**EX002.** About 29%.

**EX003.** One device may hold thousands of people's records.

**EX004.** They travel and are easily lost or stolen.

**EX005.** The disk can be read directly without logging in.

**EX006.** Stores the key and releases it only to the expected boot components.

**EX007.** Data, a loop with a condition and output.

**EX008.** A count first, then details.

**EX009.** The text "False" was treated as true.

**EX010.** CIS Controls v8 and NIST SP 800-53 Rev. 5.

**EX011.** Introduction, evidence, counter-arguments, conclusion.

**EX012.** Encryption protects data on a lost or stolen laptop that is off or locked.

**EX013.** Tenant records confidential, finance accurate, laptops working.

**EX014.** Loss and theft, malicious attachments, unpatched software, weak passwords, admin misuse.

**EX015.** Admin rights let malware or mistakes change system settings.

**EX016.** Registered devices not managed; managed devices not registered.

**EX017.** Logons for many laptops.

**EX018.** Because data locations change, so all laptops must be encrypted.

**EX019.** Laptops may be off the office network for weeks, delaying updates.

**EX020.** Disable it.

**EX021.** 11.

**EX022.** The csv and json modules.

**EX023.** As unknown, reported separately.

**EX024.** 40 encrypted, 2 encrypting, 1 not encrypted, 2 unknown.

**EX025.** Devices, updates and events.

**EX026.** To reduce personal data.

**EX027.** She checked each result by hand.

**EX028.** Read-only device reports, no tenant data, changes only through Gareth.

**EX029.** Replaced by roles; raw exports on encrypted storage.

**EX030.** Reported to Gareth, who disabled it and created named accounts.

**EX031.** Remove standing local admin rights.

**EX032.** Remove services the server does not need.

**EX033.** The required restart was postponed.

**EX034.** Mean 22.4, median 12, maximum 104 days.

**EX035.** 10.

**EX036.** Share within 14 days and count over 30 days.

**EX037.** Saltzer and Schroeder (1975).

**EX038.** Named accounts with MFA, used only for admin tasks.

**EX039.** Five software requests, installed centrally.

**EX040.** Keep tenant data on the file server rather than locally.

**EX041.** It makes data unreadable, usually changing the assessment.

**EX042.** In case the network was slow.

**EX043.** Encryption share, patch latency, unmanaged devices, unneeded services.

**EX044.** 32 of 45 encrypted; 26 of 45 within 14 days.

**EX045.** Changing them breaks comparisons.

**EX046.** Encryption, standard users, firewall, updates, anti-malware.

**EX047.** Standard user rights limit damage if anti-malware misses a file.

**EX048.** The management agent.

**EX049.** By the TPM and optionally a PIN.

**EX050.** In the directory, accessible only to IT.

**EX051.** The laptop needed its recovery key, retrieved in two minutes.

**EX052.** Whether monthly reminders reduce patch latency.

**EX053.** Share of laptops patched within 14 days.

**EX054.** Other changes may affect results.

**EX055.** Servers, laptops, firmware and hardware.

**EX056.** Configuration management, patch management, least privilege.

**EX057.** Phones and the website.

**EX058.** Encryption by default.

**EX059.** Shared code leaves vulnerable copies unpatched long after fixes.

**EX060.** Misconfigurations linked to time pressure and unclear responsibility.

**EX061.** File, finance, domain and old application servers.

**EX062.** Settings and updates out; status reports back.

**EX063.** The old application server had no backup.

**EX064.** Four: L07, L19, L33 and S04.

**EX065.** L46 and DESKTOP-7F2K.

**EX066.** Removed, access revoked and the enrolment code rotated.

**EX067.** Local admin removal, 25 of 45.

**EX068.** Because of the theft incident and data exposure.

**EX069.** Centrally through the management server.

**EX070.** In groups of ten with recovery keys escrowed.

**EX071.** Forced restart after seven days' notice.

**EX072.** Password-based encryption until replacement.

**EX073.** Critical on L19, L03, S02; important on L33.

**EX074.** They were not reporting.

**EX075.** It was 9 days old, within policy.

**EX076.** The server's documented role.

**EX077.** Monthly, after verifying backups.

**EX078.** A conversation with its users.

**EX079.** 40 of 45, 89%.

**EX080.** 2 encrypting, 1 not encrypted, 2 not reporting.

**EX081.** 45 of 45.

**EX082.** Pending reboots, 41%.

**EX083.** Full disks, 26%.

**EX084.** Main causes are fixed by policy, not tools.

**EX085.** Default admin on S04 at 02:47 and contractor on S01 at 23:15.

**EX086.** A scheduled task using the old account.

**EX087.** Logon review, failed updates and unmanaged devices.

**EX088.** Four: print-spooler and telnet on file, web-admin on finance, ftp on old app.

**EX089.** Zero unneeded services.

**EX090.** Remote access through the admin workstation.

**EX091.** Replace, isolate or accept risk.

**EX092.** Firmware changes can trigger recovery prompts.

**EX093.** Through managed loan laptops.

**EX094.** Accounts disabled on the last day and laptops wiped.

**EX095.** By planning laptop replacements.

**EX096.** An unreported leaver.

**EX097.** From 26 to 33 of 45.

**EX098.** Forced restarts started the same month.

**EX099.** Improvement coincided with reminders and forced restarts.

**EX100.** All laptops encrypted but slower patching.

**EX101.** Loan laptops to Bramley; forced restarts to the other charity.

**EX102.** To share measures quarterly.

**EX103.** 100% encrypted, 90% patched within 14 days, zero unneeded services, at most one unmanaged.

**EX104.** Baseline, implement, verify, measure, hand over.

**EX105.** Current 73% plus forced restarts.

**EX106.** Locking screens, reporting lost devices, restart notices.

**EX107.** Clearer restart messages.

**EX108.** Helped Gareth follow the incident process.

**EX109.** Whether agent reports can be wrong.

**EX110.** Five laptops checked by hand; all matched.

**EX111.** It is self-selected.

**EX112.** Encryption, updates, inventory, server checks.

**EX113.** Gareth's assistant.

**EX114.** An unmanaged new laptop.

**EX115.** Encrypted 32→45; patched 26→41; services 4→0; unmanaged 6→1.

**EX116.** Yes, 91%.

**EX117.** The data would be unreadable.

**EX118.** Problem, baseline, design, implementation, evaluation, limits.

**EX119.** Cost, staff acceptance and sustainability.

**EX120.** Simple, well-run controls matter more than advanced tools.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Center for Internet Security. (n.d.). *CIS Benchmarks*. <https://www.cisecurity.org/cis-benchmarks>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Cooper, D., Polk, W., Regenscheid, A., & Souppaya, M. (2011). *BIOS protection guidelines* (NIST SP 800-147). NIST. <https://doi.org/10.6028/NIST.SP.800-147>
- Defense Information Systems Agency. (n.d.). *Security Technical Implementation Guides (STIGs)*. <https://public.cyber.mil/stigs/>
- Dietrich, C., Krombholz, K., Borgolte, K., & Fiebig, T. (2018). Investigating system operators' perspective on security misconfigurations. *2018 ACM SIGSAC Conference on Computer and Communications Security (CCS '18)*, 1272–1289. <https://doi.org/10.1145/3243734.3243794>
- Forrest, S., Hofmeyr, S. A., Somayaji, A., & Longstaff, T. A. (1996). A sense of self for Unix processes. *1996 IEEE Symposium on Security and Privacy*, 120–128. <https://doi.org/10.1109/SECPRI.1996.502675>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, A., Dempsey, K., Ross, R., Gupta, S., & Bailey, D. (2011, updated 2019). *Guide for security-focused configuration management of information systems* (NIST SP 800-128). NIST. <https://doi.org/10.6028/NIST.SP.800-128>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kent, K., & Souppaya, M. (2006). *Guide to computer security log management* (NIST SP 800-92). NIST. <https://doi.org/10.6028/NIST.SP.800-92>
- Kernel development community. (n.d.). *Kernel self-protection*. <https://www.kernel.org/doc/html/latest/security/self-protection.html>
- Kim, Y., Daly, R., Kim, J., Fallin, C., Lee, J. H., Lee, D., Wilkerson, C., Lai, K., & Mutlu, O. (2014). Flipping bits in memory without accessing them: An experimental study of DRAM disturbance errors. *41st International Symposium on Computer Architecture (ISCA)*, 361–372. <https://doi.org/10.1109/ISCA.2014.6853210>
- Kocher, P., Horn, J., Fogh, A., Genkin, D., Gruss, D., Haas, W., Hamburg, M., Lipp, M., Mangard, S., Prescher, T., Schwarz, M., & Yarom, Y. (2019). Spectre attacks: Exploiting speculative execution. *2019 IEEE Symposium on Security and Privacy*, 1–19. <https://doi.org/10.1109/SP.2019.00002>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Li, F., & Paxson, V. (2017). A large-scale empirical study of security patches. *2017 ACM SIGSAC Conference on Computer and Communications Security (CCS '17)*, 2201–2215. <https://doi.org/10.1145/3133956.3134072>
- Microsoft. (n.d.). *Windows security baselines*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines>
- Microsoft. (n.d.). *BitLocker overview*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/>
- Microsoft. (n.d.). *Application Control for Windows*. <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol>
- Nappa, A., Johnson, R., Bilge, L., Caballero, J., & Dumitraș, T. (2015). The attack of the clones: A study of the impact of shared code on vulnerability patching. *2015 IEEE Symposium on Security and Privacy*, 692–708. <https://doi.org/10.1109/SP.2015.48>
- Regenscheid, A. (2018). *Platform firmware resiliency guidelines* (NIST SP 800-193). NIST. <https://doi.org/10.6028/NIST.SP.800-193>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., Jansen, W., & Tracy, M. (2008). *Guide to general server security* (NIST SP 800-123). NIST. <https://doi.org/10.6028/NIST.SP.800-123>
- Souppaya, M., & Scarfone, K. (2013). *Guide to malware incident prevention and handling for desktops and laptops* (NIST SP 800-83 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-83r1>
- Souppaya, M., & Scarfone, K. (2022). *Guide to enterprise patch management planning: Preventive maintenance for technology* (NIST SP 800-40 Rev. 4). NIST. <https://doi.org/10.6028/NIST.SP.800-40r4>
