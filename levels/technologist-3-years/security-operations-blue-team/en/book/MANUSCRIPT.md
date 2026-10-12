# Security Operations and Blue Team: Technologist Course

- Language: English (`en`); course 084, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; Seven offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students preparing to work as analysts and engineers in a managed security operations service.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: monitor and respond only on systems you are authorised to defend; no exploit code, no payloads, no attack procedures and no instructions for evading detection. Detections are taught from the defender's side using synthetic telemetry. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one student through a placement at a managed SOC, from a night-time dental clinic incident through logging, detection, response, automation and evaluation to a capstone. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Mei Tanaka** | Technologist student | Invented |
| **Raj Patel** | Mentor, Copperleaf Managed Security | Invented |
| **BrightSmile Dental** | Fictional client with three clinics | Invented |
| **Harbourside Polytechnic** | Fictional college | Invented |

### Core sources

NIST [SP 800-61r3](https://doi.org/10.6028/NIST.SP.800-61r3), [SP 800-92](https://doi.org/10.6028/NIST.SP.800-92), [SP 800-137](https://doi.org/10.6028/NIST.SP.800-137) and [CSF 2.0](https://doi.org/10.6028/NIST.CSWP.29); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE D3FEND](https://d3fend.mitre.org/); [Sigma](https://github.com/SigmaHQ/sigma); Knerler, Parker and Zimmerman, *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE, 2022). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes

You will (1) describe the parts of a computer and how software runs on them; (2) explain clients, servers and services in a small business; (3) identify which parts produce security-relevant records; (4) relate system roles to monitoring needs.

### 1.1 Parts of a system

A computer has a processor, memory, storage and network connections. The operating system manages them and runs applications. Each layer can record what happens: the operating system logs logons, applications log their own actions, and network devices log connections.

### 1.2 The course case

**Mei Tanaka** studies on the technologist programme at the fictional **Harbourside Polytechnic** and joins the fictional **Copperleaf Managed Security**, a small provider that monitors about forty small businesses. Her mentor is SOC lead **Raj Patel**. One client is **BrightSmile Dental**, a chain of three clinics.

### 1.3 Clients and servers

At each BrightSmile clinic, reception PCs (clients) use a practice-management server that stores appointments and patient records. A file share on the same server holds X-ray images and letters.

### 1.4 Services

The server runs several services: the database, file sharing, and remote desktop so the clinic's IT contractor can support it from outside. Every running service is something that could be misused and something that can be monitored.

### 1.5 What gets recorded

Copperleaf installs an endpoint agent on servers and PCs that sends security events to its SIEM. The clinic's firewall sends connection logs. Together they show logons, new accounts, file changes and network connections.

### 1.6 Roles drive monitoring

A server holding patient records needs closer monitoring than a waiting-room tablet. Mei lists each device's role so alerts can be weighted.

### 1.7 Small-business reality

Small clients have no IT staff on site; an office manager is the contact. Copperleaf's advice must be simple to act on.

### Worked example

Mei's inventory for clinic 2 lists: one server (practice database, file share, remote desktop enabled), four reception PCs, one X-ray workstation and a firewall. She marks the server as critical and notes that remote desktop is reachable from the internet, a fact Raj flags as the most important line on the sheet.

> **Synthetic case.** Copperleaf, BrightSmile and all people are invented.

### Errors and limits

Inventories made from documents miss forgotten devices; confirm with network scans authorised by the client.

### Exercises

- **EX001 — System layers.** Which layers of a system can record security events? *Rubric:* 3 = OS, applications, network devices; 2 = two; 1 = one; 0 = none.
- **EX002 — Server services.** Name the services on clinic 2's server and why each matters. *Rubric:* 3 = database, file share, remote desktop: each can be misused and monitored; 2 = two; 1 = one; 0 = none.
- **EX003 — Key inventory line.** Why did Raj flag the remote desktop line? *Rubric:* 3 = reachable from internet: exposure for guessing attacks; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Knowing a system's parts, services and roles tells a SOC what to monitor and where risk is greatest.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain IP addressing, ports and common internet services; (2) distinguish internal from external traffic; (3) read firewall connection logs; (4) recognise risky exposed services.

### 2.1 Addresses

Devices have IP addresses. Clinic PCs use private addresses (10.x.x.x) inside the clinic; the firewall translates them to one public address on the internet. Logs show which side an address belongs to.

### 2.2 Ports and services

Services listen on numbered ports: 443 for web, 3389 for remote desktop, 445 for file sharing. A firewall rule that forwards port 3389 from the internet to the server exposes remote desktop to anyone.

### 2.3 Internet services

Clinics use cloud email, an online booking site and a card-payment terminal. Each creates connections the firewall logs.

### 2.4 Reading firewall logs

A log line shows time, source address, destination address, port and action (allowed or denied). Many denied connections from one external address to port 3389 suggest password guessing or scanning.

### 2.5 Internal versus external

Activity from inside the clinic network is usually staff; from outside it is anyone. Detection rules treat them differently.

### 2.6 Exposure

Exposed services are a common entry route. The safer design is a VPN: staff and the IT contractor connect securely first, and remote desktop is not exposed directly.

### 2.7 Case

Mei filters clinic 2's firewall log for port 3389 and sees thousands of connection attempts per day from many countries.

### DNS and names

Devices look up names before connecting. DNS logs from the clinic firewall show which websites PCs tried to reach, useful when checking whether a PC contacted a suspicious site.

### Worked example

Raj asks Mei to summarise. She writes: "Clinic 2's server accepts remote desktop connections from the internet on port 3389. Over seven days, 41,000 connection attempts came from 2,300 external addresses. Recommend VPN-only access." Raj sends it to the client as a high-priority recommendation.

> **Synthetic case.** Logs and figures are invented.

### Errors and limits

Firewall logs show connections, not whether logons succeeded; check the server's own logs.

### Exercises

- **EX004 — Port meaning.** What does a forwarded port 3389 mean? *Rubric:* 3 = remote desktop exposed to the internet; 2 = partial; 1 = vague; 0 = none.
- **EX005 — Internal and external.** Why treat internal and external traffic differently? *Rubric:* 3 = internal usually staff; external could be anyone; 2 = partial; 1 = same; 0 = none.
- **EX006 — Safer design.** What safer design replaces exposed remote desktop? *Rubric:* 3 = VPN first, no direct exposure; 2 = partial; 1 = none; 0 = none.

### Synthesis

Addresses, ports and firewall logs show what a network exposes and who is knocking.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write simple programs to parse log lines; (2) use lists, dictionaries and counters; (3) handle malformed input safely; (4) test a parser on known lines.

### 3.1 Why program

Logs arrive as text. A short program can split lines into fields, count events and skip broken lines faster and more reliably than reading by eye.

### 3.2 Splitting lines

Each event line has a time, host, event ID and key=value fields. Splitting on spaces gives the parts; a dictionary maps event IDs to names such as "logon failure".

### 3.3 Counting

Python's Counter adds up how often each event type appears.

### Lab — parsing event lines

```python
"""Parse synthetic Windows-style event lines into fields and count by event type."""
from collections import Counter
lines = """2026-05-04T01:12:03Z CLINIC2-SRV 4625 user=reception src=203.0.113.45
2026-05-04T01:12:05Z CLINIC2-SRV 4625 user=admin src=203.0.113.45
2026-05-04T01:12:07Z CLINIC2-SRV 4625 user=administrator src=203.0.113.45
2026-05-04T01:19:41Z CLINIC2-SRV 4624 user=reception src=203.0.113.45
2026-05-04T01:22:10Z CLINIC2-SRV 4720 user=reception target=support2
broken line without fields
2026-05-04T01:22:30Z CLINIC2-SRV 4732 user=reception target=support2 group=Administrators""".splitlines()
names = {"4624": "logon success", "4625": "logon failure", "4720": "account created", "4732": "added to local group"}
counts, bad = Counter(), 0
for ln in lines:
    parts = ln.split()
    if len(parts) < 4 or parts[2] not in names: bad += 1; continue
    counts[names[parts[2]]] += 1
for k, v in counts.items(): print(f"{k:22} {v}")
print("unparsed lines:", bad)
```

Run with `python3 lab_parse.py`. Verified output:

```text
logon failure          3
logon success          1
account created        1
added to local group   1
unparsed lines: 1
```

### 3.4 Reading the result

From seven lines, the parser counts three logon failures, one logon success, one account creation and one addition to a local group, and reports one unparsed line. The broken line was skipped and counted, not silently lost.

### 3.5 Safe handling

Real logs contain truncated or odd lines. Programs must skip them, count them and continue.

### 3.6 Testing

Mei runs the parser on these known lines first; the expected counts are written down before running, so a mismatch shows a bug.

### Keeping it readable

Mei names variables clearly, adds a one-line comment saying what the script does and stores it in Copperleaf's shared repository so Raj can review and other analysts can reuse it. A script only its author can read becomes a problem the day that person is absent.

### Rerun on new data

The same script runs unchanged on next week's export.

### Worked example

The parsed lines tell a story: three failed logons from 203.0.113.45, a success as "reception" at 01:19, then that account created "support2" and added it to Administrators at 01:22. Mei notices that a reception account should never create accounts and raises it with Raj.

> **Synthetic case.** Lines come from the lab script.

### Errors and limits

Simple splitting breaks if values contain spaces; real parsers handle quoting.

### Exercises

- **EX007 — Lab counts.** Report the counts from the parser. *Rubric:* 3 = 3 failures, 1 success, 1 created, 1 group add, 1 unparsed; 2 = most; 1 = few; 0 = none.
- **EX008 — Broken lines.** How should a parser treat broken lines? *Rubric:* 3 = skip, count and continue; 2 = partial; 1 = crash; 0 = none.
- **EX009 — Story in the lines.** What sequence do the parsed lines show? *Rubric:* 3 = failures, success as reception, new account support2 added to admins; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Simple parsers turn raw lines into countable events and reveal sequences worth investigating.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) describe security events as structured records; (2) define consistent field names; (3) relate events to entities such as users and hosts; (4) explain why consistent models matter across clients.

### 4.1 Events as records

An event becomes a record with fields: time, host, user, action, outcome, source address. Structured records can be searched, counted and joined.

### 4.2 Consistent names

Copperleaf monitors forty clients with different systems. If one calls the field "user", another "account" and a third "UserName", every rule must handle all three. Copperleaf maps all to one common model at ingestion.

### 4.3 Entities

Users, hosts and clients are entities that persist across events. A table for each holds attributes such as role, criticality and owner.

### 4.4 Relationships

A user logs on to a host; a host belongs to a client. These links let analysts ask "which client is this host?" instantly.

### 4.5 Time

All times are stored in UTC with the original time zone recorded, so events from clients in different zones line up.

### 4.6 Raw and normalised

The original raw line is kept alongside normalised fields, so nothing is lost if parsing was wrong.

### 4.7 Case

The BrightSmile events from chapter 3 are stored with host CLINIC2-SRV, which links to client BrightSmile and criticality "high".

### Enrichment

At ingestion, each event is enriched with entity data: the host's client, criticality and role. Analysts see 'CLINIC2-SRV (BrightSmile, critical, patient records)' instead of a bare name, which speeds triage and reduces mistakes when similar host names exist across clients.

### Worked example

When Mei searches for "support2", results from two clients appear: BrightSmile's new admin and an old service account at a law firm. Because each event carries the client field, she separates them immediately and confirms that only BrightSmile's is new.

> **Synthetic case.** Records and clients are invented.

### Errors and limits

Mapping to a common model can hide source-specific detail; keep the raw record.

### Exercises

- **EX010 — Common model.** Why map all clients' fields to one model? *Rubric:* 3 = rules work across clients without handling variants; 2 = partial; 1 = style; 0 = none.
- **EX011 — Raw retention.** Why keep the raw line? *Rubric:* 3 = recover if parsing wrong; nothing lost; 2 = partial; 1 = none; 0 = none.
- **EX012 — Client field.** How did the client field help Mei? *Rubric:* 3 = separated two clients' support2 accounts at once; 2 = partial; 1 = none; 0 = none.

### Synthesis

Consistent data models make multi-client monitoring searchable and reliable.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain common threats to small businesses; (2) describe ransomware from the defender's view; (3) explain why exposed remote access and weak passwords matter; (4) recognise behaviours that help defenders.

### 5.1 Small-business threats

Small businesses face phishing, account compromise, invoice fraud and ransomware. They are attacked not because they are important but because they are numerous and often lightly defended.

### 5.2 Ransomware

Ransomware encrypts files and demands payment. Before encryption, attackers usually gain access (for example through exposed remote desktop), create or abuse administrator accounts, and disable protections. Each step leaves traces defenders can detect.

### 5.3 Exposed remote access

Remote desktop open to the internet attracts automated password guessing. Weak or reused passwords make guessing succeed.

### 5.4 Helpful behaviours

Strong unique passwords, MFA on remote access, prompt updates and offline backups make attacks harder and recovery easier.

### 5.5 Health data

Dental records are sensitive personal data. A breach affects patients and brings legal duties to notify.

### 5.6 The defender's view

Defenders focus on the observable steps: access, privilege, defence changes, file activity. Detecting early steps gives time to act before encryption.

### 5.7 Case

The events from chapter 3 match the early steps: guessing, access as a weak account, a new administrator.

### Backups as defence

Ransomware's power depends on the victim lacking usable backups. BrightSmile keeps nightly backups on a device in the server room, connected to the network; Raj notes that an attacker with administrator rights could encrypt or delete them too, and recommends an offline or immutable copy.

### Worked example

Raj explains to Mei that the "support2" account appeared three minutes after access. If the SOC acts within the next few minutes — disabling the account and isolating the server — encryption may be prevented. Speed at this stage matters more than complete understanding.

> **Synthetic case.** The scenario is invented.

### Errors and limits

Not every intrusion leads to ransomware; early steps can lead to theft or fraud instead.

### Exercises

- **EX013 — Ransomware steps.** List the observable steps before encryption. *Rubric:* 3 = access, admin accounts, disabling protections, file activity; 2 = three; 1 = one; 0 = none.
- **EX014 — Why small businesses.** Why are small businesses attacked? *Rubric:* 3 = numerous and lightly defended; 2 = partial; 1 = important; 0 = none.
- **EX015 — Early action.** Why act within minutes of the new admin account? *Rubric:* 3 = chance to prevent encryption before it starts; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Understanding attacks as observable steps shows defenders where early detection prevents the worst harm.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) explain how Windows and Linux record logons, accounts and processes; (2) describe virtual machines and their monitoring; (3) relate audit settings to detection; (4) recognise account and group changes as signals.

### 6.1 Operating system events

Windows records logon successes (4624), failures (4625), account creation (4720) and group membership changes (4732) when auditing is enabled. Linux records authentication in system logs. These IDs and messages are the raw material for many SOC rules.

### 6.2 Audit settings

Events appear only if audit policy enables them. Copperleaf's onboarding checklist sets audit policy on each client server and verifies that test events arrive.

### 6.3 Processes

Process creation events show which programs ran and which program started them. A file-encryption tool started from an unusual folder is a strong signal.

### 6.4 Virtualization

Many small businesses run servers as virtual machines on one physical host. The host's management console can start, stop or snapshot every server, so access to it is highly privileged and must be monitored.

### 6.5 Snapshots

Snapshots capture a server's state and can help recovery, but are not a backup if stored on the same host an attacker controls.

### 6.6 Account changes

New accounts and additions to administrator groups are rare in small clinics. Alerting on them catches attackers who create their own access.

### 6.7 Case

BrightSmile's server is a virtual machine; the host is managed by the IT contractor.

### Updates

Operating system updates fix weaknesses attackers use. Copperleaf's agent reports patch levels, and clients receive a monthly list of overdue updates.

### Worked example

Mei checks BrightSmile's audit settings and finds process creation logging was off on the clinic 2 server — the onboarding checklist had been skipped during a rushed setup. She enables it with the contractor and confirms with a harmless test program that events now arrive.

> **Synthetic case.** Settings and events are invented.

### Errors and limits

Enabling more auditing adds volume; enable what rules and investigations need.

### Exercises

- **EX016 — Event IDs.** What do event IDs 4720 and 4732 record? *Rubric:* 3 = account created; added to local group; 2 = one; 1 = none; 0 = none.
- **EX017 — Hypervisor access.** Why must virtualization host access be monitored? *Rubric:* 3 = controls all VMs: start, stop, snapshot; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Missing setting.** What was missing on clinic 2's server and how was it fixed? *Rubric:* 3 = process creation logging off; enabled and tested; 2 = partial; 1 = none; 0 = none.

### Synthesis

Operating system and virtualization events give strong signals, but only when auditing is configured and verified.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) explain authentication, authorisation and least privilege; (2) describe shared and service accounts in small businesses; (3) apply MFA to remote access; (4) detect misuse of accounts.

### 7.1 Authentication and authorisation

Authentication proves who someone is; authorisation decides what they may do. A reception account should book appointments, not create administrator accounts.

### 7.2 Least privilege

Each account gets only the rights it needs. At BrightSmile, the reception account was a local administrator because an old booking program once needed it — an excess privilege that let the attacker create support2.

### 7.3 Shared accounts

Several receptionists share one "reception" login. Shared accounts make it impossible to tell who did what and often have weak passwords that everyone knows.

### 7.4 Service accounts

Programs run under service accounts with fixed passwords. They should not be able to log on interactively.

### 7.5 MFA on remote access

Requiring MFA for remote desktop or VPN would have stopped the password-guessing attack even with a weak password.

### 7.6 Detecting misuse

Rules alert on interactive logons by service accounts, logons by shared accounts outside opening hours and new administrator accounts.

### 7.7 Case improvement

After the incident, BrightSmile gives each receptionist a personal account, removes administrator rights from reception, and requires MFA on the new VPN.

### Account reviews

Each quarter Copperleaf sends every client a list of accounts with administrator rights and asks them to confirm each one. At BrightSmile the first review removes three former staff accounts that were still enabled, closing doors nobody was watching.

### Worked example

Mei writes a rule: alert when the "reception" account logs on outside 07:00–19:00 local time. Testing on a month of history shows two matches, both at 07:05 by the early receptionist — clocks differ slightly. She widens the window to 06:45 and documents why.

> **Synthetic case.** Accounts and events are invented.

### Errors and limits

Time-based rules break when business hours change; review them with the client.

### Exercises

- **EX019 — Excess privilege.** What excess privilege helped the attacker? *Rubric:* 3 = reception account was local admin; 2 = partial; 1 = none; 0 = none.
- **EX020 — Shared account problems.** Name two problems with shared accounts. *Rubric:* 3 = no individual accountability; weak known passwords; 2 = one; 1 = none; 0 = none.
- **EX021 — Hours rule.** How was the out-of-hours rule adjusted, and why? *Rubric:* 3 = widened to 06:45 after early receptionist matches; 2 = partial; 1 = deleted; 0 = none.

### Synthesis

Least privilege, personal accounts and MFA reduce misuse; identity rules catch what remains.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) describe zones and boundaries in a small business network; (2) place controls and sensors appropriately; (3) plan secure remote access; (4) evaluate an architecture against likely attacks.

### 8.1 Zones

Even a clinic has zones: reception PCs, the server, the X-ray workstation, guest Wi-Fi and the internet. Guest Wi-Fi should never reach the server.

### 8.2 Boundaries

The firewall separates zones and the internet. Rules should allow only needed traffic: reception PCs to the server's database and file ports, nothing from the internet inward except through the VPN.

### 8.3 Remote access

A VPN with MFA lets the IT contractor and managers connect securely. Remote desktop is then allowed only from VPN addresses.

### 8.4 Sensors

Endpoint agents on server and PCs, firewall logs and the cloud email audit log give Copperleaf visibility. The X-ray workstation runs vendor software that forbids agents, so firewall logs are its only monitoring.

### 8.5 Backups

Backups must sit outside the zone an attacker could control, or be immutable.

### 8.6 Defence in depth

No single control stops everything: VPN, MFA, least privilege, monitoring and backups together make a successful attack much harder.

### 8.7 Reviewing against attacks

Mei walks the ransomware steps from chapter 5 through the new architecture: access now needs VPN plus MFA; privilege is limited; monitoring alerts on account changes and file spikes; backups are offline.

### Documenting the architecture

Mei draws each client's network on one page: zones, firewall rules, sensors and backup location. When an alert arrives at night, the analyst can see at a glance what a host can reach and what monitoring covers it, without calling the client.

### Worked example

The architecture review finds that guest Wi-Fi and reception PCs share one network at clinic 3. Mei recommends separating them with the firewall's guest network feature. The change takes thirty minutes and costs nothing.

> **Synthetic case.** Networks and reviews are invented.

### Errors and limits

Small clients may resist changes that inconvenience staff; explain the risk plainly.

### Exercises

- **EX022 — Firewall rule set.** What inbound traffic should the clinic firewall allow from the internet? *Rubric:* 3 = only VPN; nothing else; 2 = partial; 1 = remote desktop; 0 = none.
- **EX023 — X-ray workstation.** How is the X-ray workstation monitored, and why? *Rubric:* 3 = firewall logs only; vendor forbids agents; 2 = partial; 1 = agent; 0 = none.
- **EX024 — Clinic 3 finding.** What did the review find at clinic 3? *Rubric:* 3 = guest Wi-Fi shared reception network; separated; 2 = partial; 1 = none; 0 = none.

### Synthesis

Simple zones, tight boundaries, secure remote access and layered controls give small businesses strong protection.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) build baselines of normal activity; (2) measure deviations simply and transparently; (3) preserve evidence with integrity; (4) record times and units consistently.

### 9.1 Baselines

Normal activity varies by hour. Clinic servers are busy during opening hours and almost silent at night. A baseline records typical counts for each hour.

### 9.2 Measuring deviation

Comparing tonight's count to the baseline's mean and maximum shows whether activity is unusual. Simple rules — "above the highest value seen plus a margin" — are easy to explain to clients.

### Lab — hourly logon baseline

```python
"""Hourly logon baseline for a dental clinic server over 10 working days (synthetic)."""
import statistics
hourly = {1: [0,0,0,1,0,0,0,0,0,0], 9: [14,12,15,13,16,14,12,15,13,14], 13: [9,8,10,9,11,8,9,10,9,8]}
tonight_01 = 7
for h, xs in hourly.items():
    print(f"{h:02d}:00 mean={statistics.mean(xs):4.1f} sd={statistics.pstdev(xs):3.1f} max={max(xs)}")
m, sd = statistics.mean(hourly[1]), statistics.pstdev(hourly[1])
print(f"tonight 01:00 logons={tonight_01} vs mean {m:.1f} -> {'UNUSUAL' if tonight_01 > max(hourly[1]) + 3 else 'normal'}")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
01:00 mean= 0.1 sd=0.3 max=1
09:00 mean=13.8 sd=1.2 max=16
13:00 mean= 9.1 sd=0.9 max=11
tonight 01:00 logons=7 vs mean 0.1 -> UNUSUAL
```

### 9.3 Reading the result

Over ten working days, the server averaged 0.1 logons at 01:00 (maximum 1), 13.8 at 09:00 and 9.1 at 13:00. Tonight's seven logons at 01:00 are far above the night-time maximum and flagged as unusual.

### 9.4 Evidence preservation

When an incident starts, analysts export relevant logs, record a hash for each file and note who exported what and when. Exports are stored read-only.

### 9.5 Consistent times

All times are UTC in records, with local time added in client reports. Mixing them causes confusion about sequence.

### 9.6 Measurement honesty

Ten days is a short baseline; holidays and staff changes alter patterns. Mei notes these limits in every report.

### Clock checks

The agent reports each host's clock offset. A server whose clock drifts several minutes would scramble the sequence of events; Copperleaf alerts when any offset exceeds one minute. During onboarding Mei found one clinic PC eleven minutes fast because it had never synchronised, and corrected it with the contractor.

### Updating baselines

Baselines are recalculated monthly from data with confirmed incidents removed, so the attacker's night does not become part of normal.

### Worked example

Mei's incident note: "01:00–02:00 UTC: 7 logons to CLINIC2-SRV (baseline mean 0.1, max 1 over 10 days). Exports E-1 (security log) and E-2 (firewall log) saved with SHA-256 hashes at 01:41 by M. Tanaka."

> **Synthetic case.** Counts come from the lab script.

### Errors and limits

Baselines learned during an undetected compromise include the attacker's activity as "normal".

### Exercises

- **EX025 — Lab baseline.** Give the 01:00 baseline and tonight's value. *Rubric:* 3 = mean 0.1, max 1; tonight 7 → unusual; 2 = partial; 1 = wrong; 0 = none.
- **EX026 — Simple rule.** Why use "above maximum plus margin" for small clients? *Rubric:* 3 = easy to explain and check; 2 = partial; 1 = accurate; 0 = none.
- **EX027 — Evidence note.** What does a good evidence note record? *Rubric:* 3 = what was exported, hash, time, by whom, read-only storage; 2 = three; 1 = one; 0 = none.

### Synthesis

Baselines make unusual activity visible; preserved, well-timed evidence makes findings trustworthy.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Security operations and blue team: orientation

### Learning outcomes

You will (1) describe what a managed SOC does for small clients; (2) explain the SOC workflow from alert to closure; (3) relate SOC work to NIST CSF 2.0 and SP 800-61r3; (4) understand roles and service agreements.

### 10.1 A managed SOC

Copperleaf provides monitoring, triage, investigation and response guidance to clients that cannot run their own SOC. It operates under service agreements that define what is monitored, response times and what Copperleaf may do on clients' systems.

### 10.2 Workflow

Logs flow into the SIEM; rules raise alerts; analysts triage, investigate and either close, advise the client or act under agreed authority; every step is recorded in the case system.

### 10.3 Authority

Copperleaf may isolate an endpoint through its agent and disable accounts it manages, but only for alert types and clients where the agreement allows. Other actions are advised, not taken.

### 10.4 Frameworks

NIST CSF 2.0 organises outcomes into Govern, Identify, Protect, Detect, Respond and Recover; Copperleaf mainly delivers Detect and Respond. NIST SP 800-61r3 frames incident response within risk management and continuous improvement.

### 10.5 Roles

Tier-1 analysts triage; senior analysts investigate; Raj leads and approves containment; client contacts receive advice and make business decisions.

### 10.6 Service levels

High-severity alerts are acknowledged within 15 minutes, 24 hours a day.

### 10.7 Mei's role

As a trainee, Mei triages under supervision and drafts client advice for Raj's review.

### Communication with clients

Clients get plain messages: what happened, what Copperleaf did, what the client should do and when the next update will come. Technical detail goes in an attachment for their IT contractor.

### Worked example

For the BrightSmile incident, the agreement allowed Copperleaf to isolate endpoints and disable local accounts. Raj approved isolating CLINIC2-SRV at 01:36 and disabling support2 and reception. The office manager was called at 01:40 and agreed to keep the clinic closed until the morning review.

> **Synthetic case.** Agreements and events are invented.

### Errors and limits

Agreements vary by client; always check before acting.

### Exercises

- **EX028 — Authority limits.** What determines what Copperleaf may do on a client system? *Rubric:* 3 = service agreement by client and alert type; 2 = partial; 1 = anything; 0 = none.
- **EX029 — CSF functions.** Which CSF functions does Copperleaf mainly deliver? *Rubric:* 3 = Detect and Respond; 2 = one; 1 = wrong; 0 = none.
- **EX030 — BrightSmile actions.** What actions were taken at BrightSmile and when? *Rubric:* 3 = server isolated 01:36, accounts disabled, manager called 01:40; 2 = partial; 1 = vague; 0 = none.

### Synthesis

A managed SOC works within agreements and frameworks, turning alerts into recorded, authorised actions.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Security operations and blue team: assets and context

### Learning outcomes

You will (1) build and maintain client asset inventories; (2) assign criticality and owners; (3) use context to prioritise alerts; (4) keep context current across many clients.

### 11.1 Why context

An alert on a host means little without knowing what the host does, who owns it and how important it is. Context turns "new admin on CLINIC2-SRV" into "new admin on the server holding patient records at a clinic that is closed tonight".

### 11.2 Inventories

For each client, Copperleaf records hosts, roles, operating systems, criticality (low, medium, high), business hours and contacts. Agents report hosts automatically; roles and criticality come from the client.

### 11.3 Criticality

Servers with patient or financial data are high; reception PCs medium; guest devices low. Criticality multiplies alert severity in queue ordering.

### 11.4 Business hours

Clinic hours make night-time activity on clinic systems more suspicious; a law firm with late workers has different hours.

### 11.5 Keeping current

Inventories decay as clients add devices. A monthly report lists new hosts seen by agents but missing roles, and Copperleaf asks the client to classify them.

### 11.6 Contacts

Every client has a primary and backup contact with phone numbers for night calls; at BrightSmile these are the office manager and the IT contractor.

### 11.7 Case

When the support2 alert fired, enrichment showed "CLINIC2-SRV — high — patient records — clinic closed".

### Context in reports

Client reports name assets by role rather than host name: 'your clinic 2 server' means more to an office manager than CLINIC2-SRV.

### Worked example

The monthly report for BrightSmile shows two unknown hosts at clinic 1. The office manager identifies one as a new card terminal and the other as a dentist's personal laptop joined to the clinic Wi-Fi. Mei records the terminal and recommends moving personal devices to guest Wi-Fi.

> **Synthetic case.** Inventories and hosts are invented.

### Errors and limits

Client-provided criticality can be wrong; question it when alerts reveal surprises.

### Exercises

- **EX031 — Context value.** How did context change the meaning of the support2 alert? *Rubric:* 3 = patient-records server at closed clinic: urgent; 2 = partial; 1 = vague; 0 = none.
- **EX032 — Inventory fields.** List four fields in a client asset inventory. *Rubric:* 3 = hosts, roles, OS, criticality, hours, contacts (four); 2 = three; 1 = one; 0 = none.
- **EX033 — Unknown hosts.** What were the two unknown hosts, and what was done? *Rubric:* 3 = card terminal recorded; personal laptop → guest Wi-Fi advised; 2 = partial; 1 = none; 0 = none.

### Synthesis

Asset context drives prioritisation; keep it current with automatic discovery and client confirmation.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Security operations and blue team: data flows

### Learning outcomes

You will (1) trace how logs flow from client sites to the SOC; (2) identify collection points, transport and storage; (3) detect gaps and delays in data flows; (4) document flows for each client.

### 12.1 The path

Events travel from the client's endpoints (agent) and firewall (syslog) over the internet to Copperleaf's collectors, then to the SIEM, where rules run and alerts go to the case system.

### 12.2 Collection points

Agents send directly over encrypted connections. Firewalls send syslog to a small collector box at each client site, which forwards it securely.

### 12.3 Delays

Agent events usually arrive within a minute; firewall logs within five. Cloud email audit logs can take up to 30 minutes.

### 12.4 Gaps

A collector box that loses power, an expired certificate or a firewall update that resets logging settings can stop data silently.

### 12.5 Monitoring the flow

Copperleaf tracks events per source per hour; a sudden drop to zero raises a data-gap alert to engineering, not to analysts' main queue.

### 12.6 Documentation

Each client has a data-flow diagram: sources, collectors, protocols and expected volumes.

### 12.7 Case

During onboarding of a new client, Mei checks the diagram against actual data and finds firewall logs missing.

### Integrity in transit

Logs travel over encrypted, authenticated connections so they cannot be read or altered on the way. Collectors buffer events if the internet link drops and send them when it returns, so short outages delay data rather than lose it. Buffers have limits; long outages still lose events, which the gap report records.

### Worked example

The new client's firewall had syslog configured to send to an old address. Mei corrects it with the client's IT contractor, then confirms in the SIEM that firewall events arrive at the expected volume. She updates the diagram's "verified" date.

> **Synthetic case.** Flows and clients are invented.

### Errors and limits

Volume checks catch total loss but not partial loss of some event types.

### Exercises

- **EX034 — Arrival times.** Give typical arrival delays for agent, firewall and cloud email logs. *Rubric:* 3 = ~1 min, ~5 min, up to 30 min; 2 = two; 1 = one; 0 = none.
- **EX035 — Silent gaps.** Name three causes of silent data gaps. *Rubric:* 3 = collector power loss, expired certificate, firewall update resetting logging; 2 = two; 1 = one; 0 = none.
- **EX036 — Onboarding fix.** What was wrong at the new client and how was it confirmed fixed? *Rubric:* 3 = syslog sent to old address; corrected; volume verified in SIEM; 2 = partial; 1 = none; 0 = none.

### Synthesis

Knowing every data flow, its delay and its failure modes keeps a SOC from monitoring blind.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Security operations and blue team: risk scenarios

### Learning outcomes

You will (1) write risk scenarios for small-business clients; (2) link scenarios to detection and response needs; (3) prioritise scenarios by likelihood and impact; (4) review scenarios after incidents.

### 13.1 What a scenario is

A risk scenario describes how harm could happen: who, through what route, to which asset, with what impact. For BrightSmile: "an external attacker guesses a password on exposed remote desktop, gains admin rights and encrypts patient records".

### 13.2 Scenarios for clinics

Copperleaf uses five for small healthcare clients: ransomware via remote access, email account takeover leading to invoice fraud, lost unencrypted laptop, insider misuse of patient records, and supplier compromise (for example the IT contractor's account).

### 13.3 Likelihood and impact

Each scenario gets a rough rating. Ransomware via remote access is high likelihood (before the VPN change) and high impact.

### 13.4 Mapping to detection

For each scenario, the team lists detections that would catch its steps — failed logons, new admin accounts, rename spikes — and response actions.

### 13.5 Gaps

The supplier-compromise scenario had no specific detection: a contractor logon looks normal. Mei proposes alerting on contractor logons outside agreed support windows.

### 13.6 Review after incidents

After the BrightSmile incident, the ransomware scenario's likelihood is reduced for that client (VPN and MFA added) but kept high for clients without them.

### 13.7 ATT&CK link

Scenario steps are tagged with ATT&CK techniques for consistency across clients.

### Sharing scenarios with clients

Mei explains each scenario to the office manager in one sentence and asks which would hurt the business most. The manager ranks lost patient trust above downtime, which raises the priority of the insider-misuse scenario for BrightSmile.

### Worked example

Mei's scenario table for BrightSmile lists the five scenarios, ratings, detections and gaps. Raj approves adding the contractor-window rule and asks the IT contractor to share their support schedule.

> **Synthetic case.** Scenarios and ratings are invented.

### Errors and limits

Ratings are judgements; revisit them when the threat or client changes.

### Exercises

- **EX037 — Scenario parts.** What parts make up a risk scenario? *Rubric:* 3 = who, route, asset, impact; 2 = three; 1 = one; 0 = none.
- **EX038 — Five scenarios.** List the five healthcare scenarios. *Rubric:* 3 = ransomware remote access, email takeover fraud, lost laptop, insider misuse, supplier compromise; 2 = four; 1 = two; 0 = none.
- **EX039 — Supplier gap.** How was the supplier-compromise gap addressed? *Rubric:* 3 = alert on contractor logons outside support windows; 2 = partial; 1 = none; 0 = none.

### Synthesis

Risk scenarios connect threats to detections and responses and show where coverage is missing.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Security operations and blue team: methods I

### Learning outcomes

You will (1) design threshold detections for remote logon failures; (2) distinguish internal from external sources; (3) set thresholds from data; (4) document rules for analysts.

### 14.1 The method

A threshold rule counts events in a time window and alerts when the count passes a limit. For remote desktop guessing: failed logons from one source in 15 minutes.

### 14.2 Choosing the window

Fifteen minutes catches fast automated guessing; slower attackers need a longer window or a daily count rule.

### Lab — failures by source

```python
"""Failed remote-desktop logons by source in 15-minute windows (synthetic)."""
from collections import Counter
fails = [("203.0.113.45", 1) for _ in range(46)] + [("198.51.100.9", 1) for _ in range(3)] + [("10.2.0.15", 2) for _ in range(4)]
by_src = Counter(src for src, _ in fails)
for src, n in by_src.most_common():
    internal = src.startswith("10.")
    print(f"{src:14} failures={n:3} {'internal' if internal else 'external'} {'ALERT' if n >= 20 and not internal else ''}")
```

Run with `python3 lab_rdp.py`. Verified output:

```text
203.0.113.45   failures= 46 external ALERT
10.2.0.15      failures=  4 internal 
198.51.100.9   failures=  3 external
```

### 14.3 Reading the result

In one 15-minute window, 203.0.113.45 produced 46 failures and triggers the alert. An internal address, 10.2.0.15, had four failures — a receptionist mistyping — and is excluded from this rule. An external address with three failures is below the threshold of 20.

### 14.4 Internal sources

Internal failures are handled by a separate, higher threshold, because staff mistakes are common and attackers inside the network show other signs.

### 14.5 Setting the threshold

Mei looks at a month of history: legitimate external failures (the contractor mistyping) never exceeded six in 15 minutes. A threshold of 20 leaves margin.

### 14.6 Documentation

The rule page states purpose, logic, threshold reasoning, known benign triggers and response steps.

### Testing the rule

Before enabling the rule for all clients, Mei replays a week of historical firewall and logon data. It would have fired five times: three real guessing campaigns and two from a client's misconfigured monitoring tool repeatedly trying an old password. She adds that tool's address to a documented exception list.

### Worked example

Mei's rule page response steps: "Check whether any logon from the same source succeeded. If yes, treat as high: disable the account and call the client. If no, advise the client to restrict remote access; block the source at the firewall if the agreement allows."

> **Synthetic case.** Sources come from the lab script.

### Errors and limits

Attackers spread attempts across many addresses to stay below per-source thresholds.

### Exercises

- **EX040 — Lab result.** Which source alerts and why are the others excluded? *Rubric:* 3 = 203.0.113.45 (46); internal 10.2.0.15 excluded; 198.51.100.9 below 20; 2 = partial; 1 = wrong; 0 = none.
- **EX041 — Threshold reasoning.** How was the threshold of 20 chosen? *Rubric:* 3 = legitimate external failures never above 6 in history; margin; 2 = partial; 1 = guess; 0 = none.
- **EX042 — Response step.** What should the analyst check first after the alert? *Rubric:* 3 = whether any logon from same source succeeded; 2 = partial; 1 = block; 0 = none.

### Synthesis

Threshold rules work when windows, scopes and limits are chosen from data and documented for analysts.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security operations and blue team: guided lab

### Learning outcomes

You will (1) practise detecting mass file changes in a safe lab; (2) set a spike threshold from a baseline; (3) connect file activity to response decisions; (4) reflect on speed versus certainty.

### 15.1 The lab

The training lab replays synthetic file-share events from a clinic. No real files are touched. The exercise asks trainees to detect the start of mass renaming, a typical sign of encryption.

### 15.2 Baseline and threshold

In quiet minutes, the share sees 0–3 renames per minute. The rule sets the limit at ten times the highest quiet value: 30 renames per minute.

### Lab — rename spike

```python
"""File renames per minute on a clinic file share; flag a sudden spike (synthetic)."""
per_minute = {"01:30": 2, "01:31": 0, "01:32": 3, "01:33": 1, "01:34": 180, "01:35": 410, "01:36": 395}
baseline = [2, 0, 3, 1]
limit = 10 * max(max(baseline), 1)
for minute, n in per_minute.items():
    print(f"{minute} renames={n:4} {'SPIKE' if n > limit else ''}")
print("limit =", limit)
```

Run with `python3 lab_renames.py`. Verified output:

```text
01:30 renames=   2 
01:31 renames=   0 
01:32 renames=   3 
01:33 renames=   1 
01:34 renames= 180 SPIKE
01:35 renames= 410 SPIKE
01:36 renames= 395 SPIKE
limit = 30
```

### 15.3 Reading the result

From 01:30 to 01:33, renames stay between 0 and 3. At 01:34 they jump to 180, then 410 and 395 — far above the limit of 30. The spike begins at 01:34.

### 15.4 Response decision

A spike on a patient-records share at night is acted on immediately: isolate the server, then investigate. Waiting for certainty would let encryption continue.

### 15.5 False alarms

Legitimate bulk renames happen — for example, an X-ray system reorganising folders after an update. The response step includes a quick check of the process doing the renaming.

### 15.6 Reflection

Trainees compare their time-to-isolation in the lab. The fastest act within two minutes of the spike.

### Practising the call

The lab ends with a mock phone call: trainees explain to a role-played office manager what is happening and why the server is isolated, in under a minute and without jargon. Clear calls get faster client decisions.

### Worked example

In the real BrightSmile incident, the spike began at 01:34; Raj approved isolation at 01:36. Afterwards, the file-change log showed 985 files renamed in those three minutes. Restoring them from the previous night's backup took two hours the next morning.

> **Synthetic case.** Lab counts come from the script; the restoration figure is invented.

### Errors and limits

Some encryption tools work slowly to avoid spikes; rename-rate rules miss them.

### Exercises

- **EX043 — Threshold.** How is the spike limit set and what is it? *Rubric:* 3 = 10 × highest quiet value = 30; 2 = partial; 1 = guess; 0 = none.
- **EX044 — Spike start.** When does the spike begin and with how many renames? *Rubric:* 3 = 01:34 with 180; 2 = partial; 1 = wrong; 0 = none.
- **EX045 — Speed versus certainty.** Why isolate before fully investigating? *Rubric:* 3 = encryption continues while waiting; patient records at risk; 2 = partial; 1 = always; 0 = none.

### Synthesis

Spike detection on file activity catches encryption early, but only fast, authorised response turns detection into protection.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security operations and blue team: methods II

### Learning outcomes

You will (1) build sequence detections linking several events; (2) correlate account creation with privilege changes; (3) tune sequences to client behaviour; (4) explain sequences in alert text.

### 16.1 Sequences

Many attacks show a sequence: access, then privilege, then impact. A rule that looks for steps in order is stronger than any single step.

### 16.2 The BrightSmile sequence

Logon from an external address, then account creation by that session, then the new account added to Administrators within 30 minutes. Each step alone is sometimes legitimate; together they are rare.

### 16.3 Building the rule

Mei's rule joins three event types on host and session within 30 minutes. The alert text lists all three steps with times, so analysts do not have to search.

### 16.4 Tuning

At one client, the IT contractor routinely creates admin accounts for new staff after logging in remotely through the VPN. The rule excludes sessions from the contractor's VPN addresses during support windows but still alerts outside them.

### 16.5 Severity

Sequences on high-criticality hosts at night are rated high and page the on-call analyst.

### 16.6 Testing

Mei tests the rule against the BrightSmile events: it fires at 01:22, twelve minutes before the rename spike.

### 16.7 Value of earlier alerts

Earlier detection gives more time. If this rule had existed, isolation could have happened before any file was renamed.

### Maintaining exceptions

Exceptions expire after six months unless renewed with a reason, so old contractor arrangements do not linger as blind spots.

### Worked example

Raj asks Mei to estimate the benefit. She replays the incident: the sequence rule fires at 01:22; with the 15-minute acknowledgement target and a two-minute isolation, the server could have been isolated by about 01:39 at worst, or by 01:25 if acknowledged quickly — before the 01:34 spike in the quick case.

> **Synthetic case.** Events and timings are invented.

### Errors and limits

Sequence rules depend on all event types being logged; one missing step silences them.

### Exercises

- **EX046 — Sequence steps.** What three steps does the rule join? *Rubric:* 3 = external logon, account creation, admin group add within 30 min; 2 = two; 1 = one; 0 = none.
- **EX047 — Contractor exception.** How was the contractor's routine work handled? *Rubric:* 3 = exclude VPN addresses during support windows; alert outside; 2 = partial; 1 = exclude all; 0 = none.
- **EX048 — Benefit estimate.** What did the replay show about timing? *Rubric:* 3 = fires 01:22, 12 min before spike; quick ack could isolate before 01:34; 2 = partial; 1 = none; 0 = none.

### Synthesis

Sequence detections catch attacks earlier by linking steps, provided exceptions are narrow and all steps are logged.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Security operations and blue team: tooling

### Learning outcomes

You will (1) describe the SOC's main tools and their roles; (2) choose tools appropriate to a small managed SOC; (3) configure tools to support analyst workflow; (4) evaluate tools by outcomes rather than features.

### 17.1 The toolset

Copperleaf uses a SIEM for collection, search and rules; endpoint agents for telemetry and isolation; a case-management system for alerts and notes; and a shared knowledge base of rule pages and client profiles.

### 17.2 Fit for size

A small SOC needs tools that are easy to maintain, support many clients and integrate well. Feature-heavy tools that need a dedicated engineer can be a burden.

### 17.3 Workflow support

Knerler, Parker and Zimmerman (2022) advise leveraging tools to support analyst workflow. At Copperleaf, alerts open in the case system with enrichment and links to the client profile, so analysts rarely switch screens.

### 17.4 Multi-client separation

Tools must keep clients' data separate and show which client each alert belongs to. Mistakes here could leak one client's data to another.

### 17.5 Evaluating tools

Copperleaf judges tools by outcomes: time to triage, missed detections, effort to maintain. A trial of a new endpoint agent measures these on three clients before any decision.

### 17.6 Tool health

Tools themselves need monitoring: agent versions, SIEM storage and rule run times.

### 17.7 Avoiding tool sprawl

Each new tool needs an owner and a reason; overlapping tools are retired.

### Access to tools

Analyst accounts on the SIEM and case system use MFA and are reviewed quarterly.

### Worked example

In the endpoint agent trial, the new agent detected the same test events but reduced analyst triage time by two minutes per alert because it showed process trees directly in the alert. It also used more memory on old clinic PCs. Raj decides to adopt it only for servers and newer PCs.

> **Synthetic case.** Tools and trial results are invented.

### Errors and limits

Vendor demonstrations show best cases; trial tools in your own environment.

### Exercises

- **EX049 — Four tools.** Name the four main parts of Copperleaf's toolset. *Rubric:* 3 = SIEM, endpoint agents, case management, knowledge base; 2 = three; 1 = one; 0 = none.
- **EX050 — Client separation.** Why must tools separate clients' data? *Rubric:* 3 = prevent leaking one client's data to another; know which client; 2 = partial; 1 = none; 0 = none.
- **EX051 — Trial outcome.** What did the agent trial show and decide? *Rubric:* 3 = 2 min faster triage, more memory on old PCs; servers and newer PCs only; 2 = partial; 1 = adopted everywhere; 0 = none.

### Synthesis

Choose and configure tools for workflow and outcomes, with client separation and limited sprawl.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security operations and blue team: controls

### Learning outcomes

You will (1) recommend preventive controls after detections; (2) prioritise controls by risk reduction and cost; (3) verify controls after implementation; (4) track client adoption of advice.

### 18.1 From detection to prevention

Each incident shows which preventive control would have stopped it earlier. At BrightSmile: VPN with MFA for remote access, removal of admin rights from reception, personal accounts and offline backups.

### 18.2 Prioritising

Copperleaf ranks recommendations by risk reduction and effort. VPN with MFA is top: it removes the main entry route for little cost.

### 18.3 Client decisions

Clients decide and pay; Copperleaf advises. Clear explanations and cost estimates help clients act.

### 18.4 Verifying

After the client says a control is in place, Copperleaf checks: an external scan (authorised in the agreement) confirms port 3389 is closed; a test logon confirms MFA on the VPN.

### 18.5 Tracking adoption

A dashboard shows each client's open recommendations and age. Raj reviews it monthly with account managers.

### 18.6 Controls across clients

When one client's incident reveals a common weakness, Copperleaf checks all clients. Six other clients also exposed remote desktop.

### 18.7 Defensive technique names

Recommendations are tagged with D3FEND technique names to keep wording consistent across clients.

### Explaining cost

Mei prepares a one-page estimate for BrightSmile: VPN licence, a day of contractor time and staff training. Set beside the cost of the clinic being closed for a day and patients' records at risk, the decision is quick. Clients act faster when the trade-off is in their own terms.

### Worked example

After the incident, Mei checks all forty clients' firewall logs for inbound 3389 traffic accepted. Six clients expose remote desktop. Within a month, five have moved to VPN; the sixth, a small accountancy, has a planned date and a temporary IP allow-list.

> **Synthetic case.** Clients and results are invented.

### Errors and limits

Advice that clients do not act on reduces no risk; follow up persistently.

### Exercises

- **EX052 — BrightSmile controls.** List the four preventive controls recommended for BrightSmile. *Rubric:* 3 = VPN+MFA, remove reception admin, personal accounts, offline backups; 2 = three; 1 = one; 0 = none.
- **EX053 — Verification.** How did Copperleaf verify the VPN change? *Rubric:* 3 = authorised external scan shows 3389 closed; test logon confirms MFA; 2 = partial; 1 = client word; 0 = none.
- **EX054 — Cross-client check.** What did the cross-client check find and achieve? *Rubric:* 3 = 6 exposed; 5 moved to VPN in a month; 1 planned with allow-list; 2 = partial; 1 = none; 0 = none.

### Synthesis

Turn detections into prioritised, verified preventive controls and check every client for the same weakness.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Security operations and blue team: monitoring

### Learning outcomes

You will (1) run continuous monitoring across many clients; (2) balance alert volume with analyst capacity; (3) monitor source health and coverage; (4) report monitoring status to clients.

### 19.1 Continuous monitoring

NIST SP 800-137 describes continuous monitoring as an ongoing programme tied to risk, not a one-off check. Copperleaf monitors client systems 24 hours a day with defined frequencies for different checks.

### 19.2 Frequencies

Rules on logons and file activity run every minute; daily checks cover patch levels and account lists; monthly reports cover inventory and recommendations.

### 19.3 Capacity

Two analysts cover nights for forty clients. Rules that page at night must be precise; lower-value alerts wait for the morning queue.

### 19.4 Source health

Heartbeat checks show agents that stopped reporting. A missing heartbeat on a server is treated as an alert in its own right.

### 19.5 Coverage

For each client, the share of priority scenarios with tested detections is tracked. BrightSmile's rises from 40% to 80% after the incident work.

### 19.6 Client reporting

Monthly reports show alerts handled, incidents, open recommendations and coverage in plain language.

### 19.7 Reviewing noise

Each week the team reviews the noisiest rules and tunes or retires them.

### Handover between shifts

Night analysts hand over open alerts, source-health problems and pending client calls to the morning shift with a short written note and a five-minute conversation. Items without an owner after handover are assigned before the night shift leaves.

### Seasonal changes

Clinics close over holidays, so normal activity drops. Baselines and business hours are adjusted when clients notify closures.

### Worked example

In the weekly noise review, the "AV disabled" rule produced 10 alerts across clients, nine of them software installers briefly pausing antivirus. Mei proposes alerting only if antivirus stays disabled for more than ten minutes; Raj approves after checking the one real case lasted hours.

> **Synthetic case.** Figures are invented.

### Errors and limits

Monitoring frequency costs compute and attention; set it by risk.

### Exercises

- **EX055 — Frequencies.** Give the monitoring frequency for rules, daily checks and reports. *Rubric:* 3 = minute rules; daily patches/accounts; monthly inventory/recommendations; 2 = two; 1 = one; 0 = none.
- **EX056 — Missing heartbeat.** Why treat a missing heartbeat as an alert? *Rubric:* 3 = no monitoring of that host; could be failure or tampering; 2 = partial; 1 = ignore; 0 = none.
- **EX057 — AV rule change.** How was the AV-disabled rule tuned? *Rubric:* 3 = alert only if disabled > 10 min; real case lasted hours; 2 = partial; 1 = deleted; 0 = none.

### Synthesis

Continuous monitoring balances frequency, capacity and source health, and reports clearly to clients.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Security operations and blue team: troubleshooting

### Learning outcomes

You will (1) diagnose monitoring failures systematically; (2) use heartbeats and volumes to locate problems; (3) distinguish failure from tampering; (4) record fixes for future use.

### 20.1 Systematic diagnosis

When data stops, analysts work along the data path: is the host up, is the agent running, is the network reaching Copperleaf, is the SIEM ingesting? Each check narrows the cause.

### 20.2 Heartbeats

Agents send a heartbeat every five minutes. Gaps over ten minutes are stale; over an hour, missing.

### Lab — heartbeat check

```python
"""Find endpoint agents that missed heartbeats (synthetic; expected every 5 minutes)."""
now = 14 * 60
last = {"CLINIC1-SRV": now - 3, "CLINIC1-PC1": now - 4, "CLINIC2-SRV": now - 95, "CLINIC2-PC1": now - 2, "CLINIC3-SRV": now - 18}
for host, t in sorted(last.items()):
    gap = now - t
    state = "OK" if gap <= 10 else ("STALE" if gap <= 60 else "MISSING")
    print(f"{host:12} last heartbeat {gap:3} min ago {state}")
```

Run with `python3 lab_heartbeat.py`. Verified output:

```text
CLINIC1-PC1  last heartbeat   4 min ago OK
CLINIC1-SRV  last heartbeat   3 min ago OK
CLINIC2-PC1  last heartbeat   2 min ago OK
CLINIC2-SRV  last heartbeat  95 min ago MISSING
CLINIC3-SRV  last heartbeat  18 min ago STALE
```

### 20.3 Reading the result

CLINIC2-SRV last reported 95 minutes ago (missing) and CLINIC3-SRV 18 minutes ago (stale); the others are fine. Two servers need attention, the missing one first.

### 20.4 Failure or tampering

An attacker might stop the agent. Analysts check what happened just before the gap: was there a logon, a service stop, a reboot? A gap right after a suspicious logon is treated as an incident.

### 20.5 Fixes

CLINIC2-SRV was rebooted for updates and its agent failed to start because of a corrupted update; CLINIC3-SRV's clinic had a brief internet outage. The agent is reinstalled; the outage resolves itself.

### 20.6 Recording

Each fix goes into the knowledge base: symptoms, cause, solution.

### Escalating to engineering

Analysts handle simple cases; problems needing collector or SIEM changes go to Copperleaf's engineer with the diagnosis so far, saving repeated checks.

### Preventing repeats

The patch system now checks agent health after updates.

### Worked example

Before calling the client about CLINIC2-SRV, Mei checks the last events received: an update installation and a reboot request from the patch system at 12:31, and nothing suspicious. She records "probable failed agent start after update" and calls the IT contractor, who confirms and reinstalls the agent.

> **Synthetic case.** Hosts and times come from the lab script and invented follow-up.

### Errors and limits

Heartbeats show the agent is alive, not that every event type is being collected.

### Exercises

- **EX058 — Lab states.** Which hosts are missing or stale? *Rubric:* 3 = CLINIC2-SRV missing (95), CLINIC3-SRV stale (18); 2 = one; 1 = wrong; 0 = none.
- **EX059 — Tampering check.** How do analysts tell failure from tampering? *Rubric:* 3 = look at events just before the gap: logon, service stop, reboot; 2 = partial; 1 = assume failure; 0 = none.
- **EX060 — Root causes.** What caused the two problems? *Rubric:* 3 = failed agent start after update; brief internet outage; 2 = one; 1 = none; 0 = none.

### Synthesis

Troubleshoot along the data path, check for tampering before assuming failure, and record every fix.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Security operations and blue team: service integration

### Learning outcomes

You will (1) integrate SOC alerts with client contacts and IT contractors; (2) design escalation paths per client; (3) use ticketing and messaging integrations reliably; (4) handle integration failures.

### 21.1 Integration points

Copperleaf's case system connects to phone paging for on-call analysts, email and SMS to client contacts, and the IT contractors' ticket systems for follow-up work.

### 21.2 Escalation per client

Each client profile lists who to contact for which severity and when. BrightSmile: high severity at night — office manager by phone, then IT contractor; medium — email next business day.

### 21.3 Contractor tickets

When a fix needs the IT contractor, Copperleaf opens a ticket in the contractor's system automatically with the details and links back to the case.

### 21.4 Reliability

If an integration fails — SMS gateway down, contractor ticket rejected — the case system flags the failure and the analyst uses the fallback: phone call.

### 21.5 Message content

Automated messages are short, plain and never include sensitive data such as patient names; details stay in the secure portal.

### 21.6 Testing

Integrations are tested monthly with a test alert routed to a test contact.

### 21.7 Case

During the BrightSmile incident, the automatic SMS to the office manager failed because her number had changed.

### Language and tone

Night calls to clients start with what is happening and what Copperleaf has done, then what the client needs to decide. Analysts practise a short script so they stay calm and clear even when the client is alarmed or half asleep, and they always confirm the next contact time before ending the call.

### Worked example

Mei's analyst called the backup contact (the IT contractor), who reached the office manager. Afterwards, Copperleaf adds a quarterly contact confirmation step to every client's review and records the failed SMS as an integration issue.

> **Synthetic case.** Integrations and events are invented.

### Errors and limits

Integrations depend on details clients forget to update; verify them regularly.

### Exercises

- **EX061 — Escalation profile.** Describe BrightSmile's escalation for high severity at night. *Rubric:* 3 = office manager by phone, then IT contractor; 2 = partial; 1 = email; 0 = none.
- **EX062 — Message safety.** What must automated messages avoid? *Rubric:* 3 = sensitive data like patient names; details in portal; 2 = partial; 1 = nothing; 0 = none.
- **EX063 — SMS failure.** Why did the SMS fail and what changed? *Rubric:* 3 = number changed; quarterly contact confirmation added; 2 = partial; 1 = none; 0 = none.

### Synthesis

Integrations carry alerts to people who act; test them and keep contact data current.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Security operations and blue team: automation

### Learning outcomes

You will (1) identify SOC tasks suitable for automation; (2) design automated containment with guard rails; (3) test automation safely; (4) review automated actions.

### 22.1 What to automate

Repetitive, well-understood steps suit automation: enriching alerts, opening contractor tickets, isolating a host on a high-confidence spike. Judgement calls do not.

### 22.2 Automated containment

After BrightSmile, Copperleaf automates isolation for rename spikes on high-criticality servers, for clients whose agreements allow it, so containment does not wait for an analyst.

### 22.3 Guard rails

Automation can go wrong at scale: a bad rule could isolate every PC in a clinic. A guard limits automatic isolation to two hosts per client per hour; beyond that, the on-call analyst is paged.

### Lab — containment guard

```python
"""Automated containment with a safety guard: isolate at most 2 hosts per client per hour (synthetic)."""
alerts = [("BrightSmile", "CLINIC2-PC1", "rename spike"), ("BrightSmile", "CLINIC2-PC2", "rename spike"),
          ("BrightSmile", "CLINIC2-PC3", "rename spike"), ("Oakfield Law", "OAK-PC4", "rename spike")]
isolated = {}
for client, host, kind in alerts:
    n = isolated.get(client, 0)
    if n < 2:
        isolated[client] = n + 1
        print(f"ISOLATE {host} ({client})")
    else:
        print(f"PAGE ON-CALL: guard reached for {client}; {host} not auto-isolated")
```

Run with `python3 lab_guard.py`. Verified output:

```text
ISOLATE CLINIC2-PC1 (BrightSmile)
ISOLATE CLINIC2-PC2 (BrightSmile)
PAGE ON-CALL: guard reached for BrightSmile; CLINIC2-PC3 not auto-isolated
ISOLATE OAK-PC4 (Oakfield Law)
```

### 22.4 Reading the result

Two BrightSmile PCs are isolated automatically; the third triggers a page instead because the guard is reached. Oakfield Law's PC is isolated because that client's count is separate.

### 22.5 Testing

Automation is tested in the lab with synthetic alerts, then enabled in monitor mode (logging what it would do) for two weeks before acting.

### 22.6 Review

Every automated action is reviewed the next morning; wrong actions lead to rule or guard changes.

### Client consent

Automated isolation runs only where the client's agreement allows it. Some clients prefer a phone call before any action; their profiles mark this, and the automation pages an analyst instead. Mei reviews agreements with account managers so automation settings match what each client has signed.

### Worked example

In monitor mode, the automation would have isolated one PC wrongly: an X-ray system update renamed hundreds of files. Mei adds a check excluding the X-ray vendor's signed update process, and the review records the change.

> **Synthetic case.** Alerts come from the lab script; the monitor-mode finding is invented.

### Errors and limits

Guard rails slow response in genuine large outbreaks; the page ensures a human decides quickly.

### Exercises

- **EX064 — Automation fit.** Which tasks suit automation and which do not? *Rubric:* 3 = repetitive well-understood steps vs judgement calls; 2 = partial; 1 = all; 0 = none.
- **EX065 — Lab behaviour.** What did the guard do in the lab? *Rubric:* 3 = isolated 2 BrightSmile hosts, paged for third; Oakfield isolated separately; 2 = partial; 1 = wrong; 0 = none.
- **EX066 — Monitor-mode finding.** What did monitor mode reveal and how was it fixed? *Rubric:* 3 = X-ray update renames would isolate; exclude signed vendor update process; 2 = partial; 1 = none; 0 = none.

### Synthesis

Automate well-understood steps with guard rails, staged testing and daily review.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Security operations and blue team: evaluation

### Learning outcomes

You will (1) evaluate detection rules with precision and recall from case outcomes; (2) identify rules needing tuning or redesign; (3) consider missed detections; (4) report evaluation results.

### 23.1 Why evaluate

Rules drift as clients change. Monthly evaluation shows which rules work, which waste analyst time and which miss attacks.

### 23.2 Measures

From closed cases, each alert is a true positive (real issue) or false positive. Missed detections (false negatives) come from incidents found other ways, such as client reports. Precision is TP ÷ (TP + FP); recall is TP ÷ (TP + FN).

### Lab — monthly rule quality

```python
"""Month-end detection quality per rule from closed-alert labels (synthetic)."""
rules = {"RDP brute force": (12, 3, 0), "new local admin": (4, 6, 0), "rename spike": (2, 1, 0), "AV disabled": (1, 9, 1)}
for name, (tp, fp, fn) in rules.items():
    prec = tp / (tp + fp)
    rec = tp / (tp + fn) if tp + fn else float("nan")
    print(f"{name:16} TP={tp:2} FP={fp:2} FN={fn} precision={prec:.2f} recall={rec:.2f}")
```

Run with `python3 lab_quality.py`. Verified output:

```text
RDP brute force  TP=12 FP= 3 FN=0 precision=0.80 recall=1.00
new local admin  TP= 4 FP= 6 FN=0 precision=0.40 recall=1.00
rename spike     TP= 2 FP= 1 FN=0 precision=0.67 recall=1.00
AV disabled      TP= 1 FP= 9 FN=1 precision=0.10 recall=0.50
```

### 23.3 Reading the result

The remote-logon brute-force rule has precision 0.80 and recall 1.00. New local admin has precision 0.40 — many legitimate account changes. Rename spike has 0.67. The AV-disabled rule has precision 0.10 and missed one real case (recall 0.50), the weakest rule.

### 23.4 Actions

AV-disabled is redesigned (the ten-minute change from chapter 19, plus a check for tamper-protection events). New local admin gets the contractor-window exception from chapter 16.

### 23.5 Small numbers

A rule with three alerts a month gives unstable percentages; Mei reports counts beside rates.

### 23.6 Missed detections

The missed AV case was found by the client noticing pop-ups; the evaluation asks why the rule did not fire — the event type had changed after an antivirus update.

### Sharing results

A short version of the evaluation goes to clients in their monthly report: which alerts were real, which were noise, and what Copperleaf changed. Clients see that tuning is continuous work, not a one-off setup, and are more willing to report changes that affect rules.

### Worked example

Mei's monthly evaluation table lists each rule's counts, rates, actions and owner. Raj presents it to the team and uses it to decide where engineering time goes next month.

> **Synthetic case.** Counts come from the lab script.

### Errors and limits

Labels depend on analysts' closure decisions, which may be wrong.

### Exercises

- **EX067 — Formulas.** Write the formulas for precision and recall. *Rubric:* 3 = TP/(TP+FP); TP/(TP+FN); 2 = one; 1 = wrong; 0 = none.
- **EX068 — Weakest rule.** Which rule is weakest and why? *Rubric:* 3 = AV disabled: precision 0.10, recall 0.50; 2 = partial; 1 = other; 0 = none.
- **EX069 — Miss cause.** Why did the AV rule miss a real case? *Rubric:* 3 = event type changed after AV update; 2 = partial; 1 = unknown; 0 = none.

### Synthesis

Regular evaluation with precision, recall and counts directs tuning and reveals silent rule failures.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) frame a practical research question in a managed SOC; (2) collect and analyse operational data ethically; (3) use simple comparisons and descriptive statistics; (4) present findings with limits.

### 24.1 The question

Mei asks: "Do clients who received a 15-minute security briefing report suspicious emails more often than those who did not?"

### 24.2 Data

Copperleaf briefed twelve clients last year as part of onboarding; eighteen others were not briefed. The phishing report mailbox records reports by client.

### 24.3 Measure

Reports per 100 staff per quarter, so client sizes are comparable.

### 24.4 Comparison

Briefed clients averaged 4.1 reports per 100 staff per quarter; others 1.6. The difference is large, but the groups were not randomly chosen: briefed clients joined more recently and may differ in other ways.

### 24.5 Ethics

Data are aggregated per client; no individual staff are identified. Clients agreed to anonymised use in Copperleaf's improvement work.

### 24.6 Limits

Confounding by joining date and client type; small numbers; reports are not the same as resisting phishing.

### 24.7 Next step

Mei proposes briefing six of the unbriefed clients next quarter, chosen by lot, and comparing with the other twelve unbriefed — a fairer test.

### Literature

Mei reads Alahmadi et al. (2022) on how analysts experience alarms and notes that user reports are a form of human sensor. She also reads Sundaramurthy et al. (2014), whose researchers worked inside SOCs to understand practice, which encourages her to talk to client contacts about why they report or do not, rather than relying on numbers alone.

### Presenting

Mei presents the result to Copperleaf's team with a chart of rates per client group, the caveats and the proposed follow-up, in ten minutes.

### Worked example

Mei's summary: "Briefed clients reported 2.5 times more suspicious emails per 100 staff, but briefed clients differ in joining date and type. A small randomised follow-up is proposed." Raj approves the follow-up.

> **Synthetic case.** Figures are invented.

### Errors and limits

Observational comparisons suggest; randomised comparisons test.

### Exercises

- **EX070 — Comparable measure.** Why use reports per 100 staff per quarter? *Rubric:* 3 = clients differ in size; rate comparable; 2 = partial; 1 = simpler; 0 = none.
- **EX071 — Confounding.** Why can the 4.1 vs 1.6 difference not be credited to briefings alone? *Rubric:* 3 = groups not random; joining date and type differ; 2 = partial; 1 = it can; 0 = none.
- **EX072 — Fairer test.** What follow-up did Mei propose? *Rubric:* 3 = brief 6 unbriefed chosen by lot, compare with other 12; 2 = partial; 1 = none; 0 = none.

### Synthesis

Practical research uses comparable measures, recognises confounding and moves toward fairer tests.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) work in a team to design a SOC improvement; (2) divide roles and integrate work; (3) present a design for critique; (4) incorporate feedback.

### 25.1 The brief

Teams of three design an onboarding package that brings a new small client to "monitored and verified" within two weeks.

### 25.2 Mei's team

Mei, a networking student and a programming student divide the work: data flows and verification (Mei), firewall and VPN checks (networking), and automation of the onboarding checklist (programming).

### 25.3 Design

Day 1–2: agreement and contacts; day 3–5: agents and syslog; day 6–8: verification with test events per data flow; day 9–10: baseline collection; day 11–14: rule enablement and first report.

### 25.4 Critique

Raj and a client account manager critique the design. The account manager notes clients rarely respond within a day; the team adds a reminder step and a "waiting on client" status so delays are visible.

### 25.5 Integration

The automated checklist marks each step done only when evidence is attached, such as a screenshot of test events arriving.

### 25.6 Teamwork

Weekly stand-ups and a shared board keep the three parts aligned.

### 25.7 Presentation

The final presentation shows the two-week plan, evidence requirements and the dashboard.

### Documentation

The package includes a client-facing one-page guide explaining what will happen each day, what the client must do, and who to call. The account manager reports that clients appreciated knowing the plan in advance.

### Lessons for the team

The team notes that integrating three parts took longer than building each, and plans integration time from the start next time.

### Worked example

The team pilots the package with a real new client, a veterinary practice. Monitoring is verified on day 12; the only delay was waiting for the client to approve the firewall change, which the "waiting on client" status made visible to the account manager.

> **Synthetic case.** The studio and client are invented.

### Errors and limits

Pilots with one client show feasibility, not typical timing.

### Exercises

- **EX073 — Role split.** How did the team divide the work? *Rubric:* 3 = data flows/verification, firewall/VPN, automation; 2 = two; 1 = one; 0 = none.
- **EX074 — Critique response.** What did the account manager's critique add? *Rubric:* 3 = reminder step and waiting-on-client status; 2 = partial; 1 = nothing; 0 = none.
- **EX075 — Pilot result.** What happened in the pilot? *Rubric:* 3 = verified day 12; delay from client approval visible; 2 = partial; 1 = failed; 0 = none.

### Synthesis

Team studios turn separate skills into an integrated, critiqued design tested in a pilot.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Operational handoff

### Learning outcomes

You will (1) hand over a new detection or process to operations; (2) write runbooks analysts can follow; (3) train analysts and confirm understanding; (4) plan ownership and review.

### 26.1 What handoff means

A detection built by an engineer becomes the analysts' daily work. Handoff ensures they understand it, can act on it and know whom to ask.

### 26.2 Runbooks

Each alert type gets a runbook: what the alert means, what to check first, decision points, actions allowed per client agreement, and how to close. Mei writes the runbook for the sequence rule from chapter 16.

### 26.3 Training

A 20-minute session walks analysts through the runbook using the BrightSmile replay. Each analyst then triages two lab alerts alone.

### 26.4 Confirming understanding

Mei checks that analysts reach the right decisions in the lab. One analyst isolates on a contractor-window alert that should have been a phone call; the runbook is clarified.

### 26.5 Ownership

The rule has an owner (Mei during placement, then a named engineer), a review date and a feedback channel.

### 26.6 Go-live

The rule goes live on a Monday morning, not before a weekend, so problems are found while staff are available.

### 26.7 Feedback

Analysts' comments in the first two weeks lead to two wording changes in the alert text.

### Retiring old procedures

When the new rule goes live, the old manual check it replaces is removed from the shift checklist, so analysts are not doing duplicate work. The change is noted in the shift log and in the rule's change history, which lets anyone reviewing the rule later see what it replaced and why.

### Worked example

Two weeks after go-live, the rule has fired three times: one real sequence at a client's accounts PC (contained) and two contractor actions outside agreed windows that turned out to be agreed emergencies. Mei adds a field for "emergency support approved by" to contractor tickets so analysts can check quickly.

> **Synthetic case.** Runbooks and events are invented.

### Errors and limits

Runbooks cannot cover every variation; analysts must escalate when unsure.

### Exercises

- **EX076 — Runbook contents.** List the runbook sections. *Rubric:* 3 = meaning, first checks, decisions, allowed actions, closure; 2 = four; 1 = two; 0 = none.
- **EX077 — Training check.** What did the lab check reveal and how was it fixed? *Rubric:* 3 = analyst isolated on contractor-window alert; runbook clarified; 2 = partial; 1 = nothing; 0 = none.
- **EX078 — Go-live timing.** Why go live on a Monday morning? *Rubric:* 3 = problems found while staff available; 2 = partial; 1 = random; 0 = none.

### Synthesis

Handoff turns a detection into reliable practice through runbooks, training, ownership and early feedback.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) deploy detections across many clients safely; (2) validate detections with authorised tests; (3) record validation evidence per client; (4) manage exceptions and failures.

### 27.1 Staged deployment

New rules go to three pilot clients, then to the rest in groups. Each stage has a check: alert volume within expectations, no errors.

### 27.2 Validation

Validation asks whether rules catch the behaviour they target in each client's real environment. Copperleaf runs authorised test actions on each client's systems with a test account: create a local account and add it to Administrators, then remove it.

### 27.3 Authorisation

Tests are listed in the service agreement and scheduled with the client contact. They never touch real data.

### 27.4 Evidence

Each client's validation record shows test time, expected alert, actual alert time and analyst who confirmed.

### 27.5 Failures

At four clients the sequence rule did not fire. At three, account-management auditing was disabled; at one, the agent was an old version.

### 27.6 Fixes and retest

Auditing is enabled and the agent upgraded; retests pass.

### 27.7 Exceptions

One client's vendor-managed system cannot have auditing enabled; the gap is recorded and the client informed.

### Scheduling with clients

Tests are booked for quiet periods agreed with each client's contact, often a lunchtime or after hours. The client is told the exact test window and the test account name in advance, so if their own staff notice the account they know it is expected. After the test, Copperleaf confirms by email that the account was removed. Clients who cannot be reached to schedule are listed as unvalidated rather than tested without notice, and the account manager follows up. This keeps validation within what each client has agreed, and it builds trust that Copperleaf's actions on their systems are always announced and reversible.

### Worked example

Mei's validation summary: 40 clients tested; 36 passed first time; 3 fixed by enabling auditing; 1 fixed by upgrading the agent; 1 permanent exception recorded for a vendor-managed system at a client that otherwise passed. Coverage for the sequence scenario is now verified rather than assumed.

> **Synthetic case.** Results are invented.

### Errors and limits

Validation with test accounts proves the rule fires on that action, not on every variant an attacker might use.

### Exercises

- **EX079 — Validation test.** Describe the authorised validation test. *Rubric:* 3 = test account created and added to Administrators, then removed; 2 = partial; 1 = attack; 0 = none.
- **EX080 — Failure causes.** Why did the rule fail at four clients? *Rubric:* 3 = auditing disabled at 3; old agent at 1; 2 = partial; 1 = unknown; 0 = none.
- **EX081 — Exception handling.** How was the unfixable system handled? *Rubric:* 3 = gap recorded; client informed; 2 = partial; 1 = ignored; 0 = none.

### Synthesis

Deploy in stages, validate per client with authorised tests and record every pass, fix and exception.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) work in a live managed SOC under supervision; (2) apply professional conduct with clients; (3) contribute to daily operations; (4) reflect on practice in a journal.

### 28.1 The placement

Mei's final field practice is eight weeks full-time at Copperleaf, rotating between day and evening shifts under Raj's supervision.

### 28.2 Conduct

She signs confidentiality terms, never discusses clients outside work and uses client data only in Copperleaf's systems.

### 28.3 Daily work

Triage of medium alerts, drafting client advice for review, onboarding checks and the weekly noise review.

### 28.4 Client contact

By week four, Mei makes routine client calls herself, with Raj listening in for the first few.

### 28.5 Mistakes

In week three, Mei closes an alert as benign without checking the client's business hours; Raj spots it in review. The alert was benign, but the check was required. She adds it to her personal checklist.

### 28.6 Journal

A weekly journal records cases, decisions, mistakes and lessons; her polytechnic tutor reviews it.

### 28.7 Evaluation

Raj's evaluation covers technical skill, judgement, communication and reliability.

### Shift handover

At every shift change Mei writes a handover note: open cases, client calls promised, alerts being watched and anything unusual. The incoming analyst reads it and asks questions before Mei leaves. Raj points out that the most common failure in managed SOCs is a promise to call a client back that gets lost at handover, so Mei puts promised calls at the top of every note, with the time and the client contact's name. In week five, an evening analyst thanks her because a client called asking for an update and the note told him exactly what had been promised. Good handovers make the service continuous even though people change every eight hours.

### Worked example

Mei's journal, week six: "Called a dental client at 19:40 about a new admin account. The office manager was defensive, thinking we suspected her. I explained it was a routine check of any new admin. She confirmed she had created it for a locum dentist. Lesson: say 'routine check' first."

> **Synthetic case.** The placement is invented.

### Errors and limits

Placements vary by host; tutors ensure learning goals are met.

### Exercises

- **EX082 — Daily work.** List three daily tasks Mei performed. *Rubric:* 3 = triage, drafting advice, onboarding checks, noise review (three); 2 = two; 1 = one; 0 = none.
- **EX083 — Week-three mistake.** What was Mei's mistake and her response? *Rubric:* 3 = closed without checking business hours; added to checklist; 2 = partial; 1 = none; 0 = none.
- **EX084 — Call lesson.** What did the defensive client teach Mei? *Rubric:* 3 = frame as routine check first; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Supervised field practice builds judgement, client skills and reflective habits.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) build a capstone improvement for the managed SOC; (2) integrate detection, automation and reporting; (3) test the build safely; (4) document it for operations.

### 29.1 The capstone

Mei builds a "ransomware early warning" package for all healthcare clients: the sequence rule, the rename-spike rule with automated isolation and guard, heartbeat-gap alerts on servers, and a monthly coverage report.

### 29.2 Requirements

Detect the BrightSmile sequence within 5 minutes of the admin-group change; isolate on rename spikes within 2 minutes; page on server heartbeat gaps over 15 minutes at night; no more than one false page per client per month.

### 29.3 Building

Rules are written in the SIEM, automation in Copperleaf's playbook tool, reports from SIEM queries. Everything is stored in version control with change notes.

### 29.4 Testing

Each component is tested in the lab with synthetic events: the BrightSmile replay, the rename spike and a stopped agent.

### 29.5 Guard rails

The isolation guard from chapter 22 is reused; heartbeat paging respects client maintenance windows.

### 29.6 Documentation

Runbooks for each alert, a client-facing summary and an owner list.

### 29.7 Peer review

A senior analyst reviews logic and runbooks before deployment.

### Version control and change notes

Every rule and playbook in the package is stored with a change note that explains what changed, why, who reviewed it and how it was tested. If an alert misbehaves after go-live, the team can see exactly which change caused it and roll it back to the previous version within minutes. Mei tags the first deployable set as version 1.0 so later comparisons have a clear baseline, and links each tag to its test results in the lab.

### Worked example

Lab tests: sequence alert in 2 minutes after the admin-group event; isolation 70 seconds after spike detection; heartbeat page 16 minutes after the agent stopped — one minute over the target because the check runs every five minutes. Mei changes the check interval to two minutes and retests: 13 minutes.

> **Synthetic case.** The build and test results are invented.

### Errors and limits

Lab timings exclude real-world delays such as slow client links.

### Exercises

- **EX085 — Package parts.** List the four parts of the package. *Rubric:* 3 = sequence rule, rename spike with isolation, heartbeat gaps, coverage report; 2 = three; 1 = one; 0 = none.
- **EX086 — Requirements.** State two requirements of the package. *Rubric:* 3 = e.g. sequence within 5 min; isolate within 2 min; heartbeat page >15 min; ≤1 false page/month (two); 2 = one; 1 = none; 0 = none.
- **EX087 — Heartbeat fix.** Why did the heartbeat test miss its target and what fixed it? *Rubric:* 3 = 5-min check interval; changed to 2 min; 13 min; 2 = partial; 1 = none; 0 = none.

### Synthesis

A capstone build integrates rules, automation and reporting, tested against explicit requirements.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) assess the capstone against requirements with evidence; (2) validate on client systems with authorisation; (3) reflect on what worked and what did not; (4) present results to the SOC and assessors.

### 30.1 Assessment plan

Each requirement is checked with lab results, authorised client tests and one month of live operation across twelve healthcare clients.

### 30.2 Client validation

With agreement from each client, Copperleaf runs the account test (chapter 27) and a stopped-agent test during maintenance windows. Rename spikes are tested only in the lab, since generating them on client systems would disrupt work.

### 30.3 Results

Sequence alerts arrived in 1–4 minutes at all twelve clients. Heartbeat pages arrived in 11–14 minutes. In live operation, false pages averaged 0.4 per client per month. Rename isolation is verified in the lab only.

### 30.4 Live event

One real event occurred: a clinic PC's new admin account at night, caught by the sequence rule and contained before any file activity. The account belonged to an attacker using a phished contractor password.

### 30.5 Reflection

What worked: reusing tested components, staged deployment. What did not: the first heartbeat interval; one client's maintenance window was undocumented, causing a false page.

### 30.6 Presentation

Mei presents to Copperleaf's team and her assessors: requirements, evidence, the live event, limits and maintenance plan.

### 30.7 Handover

The package passes to a named engineer with a review date.

### Assessor criteria

Assessors grade clarity of requirements, quality of evidence, honesty about limits and the maintenance plan.

### Next steps

After assessment, the package enters normal review cycles with the named engineer.

### Worked example

An assessor asks why rename isolation was not tested on client systems. Mei explains that creating hundreds of renamed files on a live clinic share risks disrupting patient care; lab evidence plus the guard rail is the proportionate choice, and the limitation is stated in her report.

> **Synthetic case.** The assessment is invented.

### Errors and limits

One month and twelve clients give an early picture; continue measuring.

### Exercises

- **EX088 — Results summary.** Summarise the capstone results. *Rubric:* 3 = sequence 1–4 min; heartbeat 11–14 min; 0.4 false pages; rename lab only; 2 = partial; 1 = one; 0 = none.
- **EX089 — Live event.** Describe the live event caught. *Rubric:* 3 = night admin account by phished contractor password; contained before files; 2 = partial; 1 = none; 0 = none.
- **EX090 — Lab-only test.** Why was rename isolation tested only in the lab? *Rubric:* 3 = live test could disrupt patient care; proportionate; stated limit; 2 = partial; 1 = forgot; 0 = none.

### Synthesis

Assess against requirements with proportionate evidence, report limits and hand over for ongoing ownership.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Mei Tanaka, Raj Patel, BrightSmile Dental, Harbourside Polytechnic and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The operating system, the applications and the network devices can all record events.

**EX002.** The practice database, the file share and remote desktop; each is a possible target and a source of monitoring data.

**EX003.** Because remote desktop reachable from the internet exposes the server to password-guessing attacks.

**EX004.** The server's remote desktop service is reachable by anyone on the internet.

**EX005.** Internal traffic usually comes from staff devices, while external traffic could come from anyone.

**EX006.** Require a VPN connection first and stop exposing remote desktop directly.

**EX007.** Three logon failures, one success, one account created, one group addition and one unparsed line.

**EX008.** Skip them, count how many, and keep going.

**EX009.** Failed logons from one address, a successful logon as "reception", then creation of "support2" and its addition to Administrators.

**EX010.** So one rule can work for every client without handling each system's field names.

**EX011.** So the original can be checked or re-parsed if normalisation was wrong.

**EX012.** It let her immediately separate BrightSmile's new account from an older account at another client.

**EX013.** Gaining access, creating or abusing administrator accounts, disabling protections and then mass file activity.

**EX014.** Because there are many of them and they are often lightly defended.

**EX015.** Because acting at this early stage can stop the attack before files are encrypted.

**EX016.** 4720 records account creation; 4732 records addition to a local security group.

**EX017.** Because whoever controls the host can stop, copy or snapshot every server on it.

**EX018.** Process creation logging was off; it was enabled with the contractor and verified with a test program.

**EX019.** The reception account had local administrator rights, letting the attacker create support2.

**EX020.** No one can tell who used them, and their passwords tend to be weak and widely known.

**EX021.** The window was widened to start at 06:45 because the early receptionist logged on just after 07:00 on slightly different clocks.

**EX022.** Only VPN connections; nothing else should be allowed inward.

**EX023.** Through firewall logs only, because the vendor's software forbids installing agents.

**EX024.** Guest Wi-Fi shared the reception network; they were separated using the firewall's guest feature.

**EX025.** The 01:00 baseline mean is 0.1 with a maximum of 1; tonight there were 7 logons, flagged as unusual.

**EX026.** Because clients and analysts can understand and verify it easily.

**EX027.** What was exported, its hash, when, by whom, and that it was stored read-only.

**EX028.** The service agreement, which lists permitted actions per client and alert type.

**EX029.** Detect and Respond.

**EX030.** The server was isolated at 01:36, support2 and reception disabled, and the office manager called at 01:40.

**EX031.** It showed the alert was on the high-criticality patient-records server while the clinic was closed, making it urgent.

**EX032.** Hosts, roles, criticality and business hours (also operating systems and contacts).

**EX033.** A new card terminal, which was recorded, and a dentist's personal laptop, which was advised onto guest Wi-Fi.

**EX034.** About one minute for agents, five for firewall logs and up to 30 minutes for cloud email audit logs.

**EX035.** A collector losing power, an expired certificate and a firewall update resetting logging settings.

**EX036.** Syslog pointed to an old address; after correction, firewall events were seen arriving at expected volume.

**EX037.** Who causes harm, by what route, to which asset, with what impact.

**EX038.** Ransomware via remote access, email takeover leading to fraud, lost unencrypted laptop, insider misuse of records, and supplier compromise.

**EX039.** By alerting on IT contractor logons outside agreed support windows.

**EX040.** 203.0.113.45 alerts with 46 failures; 10.2.0.15 is internal and excluded; 198.51.100.9 had only 3.

**EX041.** A month of history showed legitimate external failures never exceeded six in 15 minutes, so 20 leaves a margin.

**EX042.** Whether any logon from the same source succeeded.

**EX043.** Ten times the highest quiet-minute value, which gives 30 renames per minute.

**EX044.** At 01:34, with 180 renames.

**EX045.** Because every minute of waiting lets encryption continue on patient records.

**EX046.** An external logon, account creation in that session, and the new account added to Administrators within 30 minutes.

**EX047.** Sessions from the contractor's VPN addresses during support windows are excluded; outside those windows the rule still alerts.

**EX048.** The rule would fire at 01:22, twelve minutes before the spike, allowing isolation before encryption if acknowledged quickly.

**EX049.** The SIEM, endpoint agents, the case-management system and the knowledge base.

**EX050.** To avoid exposing one client's data to another and to show clearly which client each alert concerns.

**EX051.** It cut triage by two minutes but used more memory on old PCs, so it was adopted only for servers and newer PCs.

**EX052.** VPN with MFA, removing admin rights from reception, personal accounts and offline backups.

**EX053.** An authorised external scan confirmed port 3389 closed, and a test logon confirmed MFA on the VPN.

**EX054.** Six clients exposed remote desktop; five moved to VPN within a month and one had a plan with a temporary allow-list.

**EX055.** Logon and file rules every minute; patch and account checks daily; inventory and recommendation reports monthly.

**EX056.** Because the host is no longer monitored, whether from failure or tampering.

**EX057.** To alert only when antivirus stays off for more than ten minutes, which still catches the real case that lasted hours.

**EX058.** CLINIC2-SRV is missing at 95 minutes and CLINIC3-SRV stale at 18 minutes.

**EX059.** By checking what happened just before the gap — a suspicious logon or service stop suggests tampering, an update and reboot suggest failure.

**EX060.** A corrupted update stopped the agent starting on CLINIC2-SRV; clinic 3 had a short internet outage.

**EX061.** Phone the office manager first, then the IT contractor.

**EX062.** Sensitive data such as patient names; details stay in the secure portal.

**EX063.** The office manager's number had changed; quarterly contact confirmation was added for all clients.

**EX064.** Repetitive, well-understood steps such as enrichment and high-confidence isolation suit it; judgement calls do not.

**EX065.** It isolated two BrightSmile PCs, paged on-call for the third, and isolated Oakfield Law's PC under its own count.

**EX066.** An X-ray software update would have been isolated; the vendor's signed update process was excluded.

**EX067.** Precision = TP ÷ (TP + FP); recall = TP ÷ (TP + FN).

**EX068.** AV disabled, with precision 0.10 and recall 0.50.

**EX069.** An antivirus update had changed the event type the rule relied on.

**EX070.** Because clients differ in size, a rate per 100 staff allows fair comparison.

**EX071.** The groups were not chosen randomly; briefed clients joined later and may differ in other ways.

**EX072.** Brief six unbriefed clients chosen by lot and compare them with the remaining twelve.

**EX073.** Mei took data flows and verification, the networking student firewall and VPN checks, and the programming student checklist automation.

**EX074.** A reminder step and a "waiting on client" status to make client delays visible.

**EX075.** Monitoring was verified on day 12; the only delay, waiting for client approval, was visible thanks to the new status.

**EX076.** What the alert means, what to check first, decision points, actions allowed per agreement and how to close.

**EX077.** One analyst isolated a host when a phone call was correct; the runbook was clarified.

**EX078.** So any problems appear while staff are available to fix them.

**EX079.** Creating a local test account, adding it to Administrators and then removing it, as agreed with the client.

**EX080.** Account-management auditing was off at three clients and one had an old agent version.

**EX081.** The gap was recorded as a permanent exception and the client informed.

**EX082.** Triage of medium alerts, drafting client advice and onboarding checks.

**EX083.** She closed an alert without checking business hours and added the check to her personal checklist.

**EX084.** To open with "this is a routine check" so clients do not feel accused.

**EX085.** The sequence rule, the rename-spike rule with guarded isolation, heartbeat-gap alerts and a monthly coverage report.

**EX086.** Detect the sequence within 5 minutes and isolate on rename spikes within 2 minutes.

**EX087.** The five-minute check interval added delay; checking every two minutes brought it to 13 minutes.

**EX088.** Sequence alerts in 1–4 minutes, heartbeat pages in 11–14 minutes, 0.4 false pages per client per month, and rename isolation verified in the lab only.

**EX089.** A night-time admin account created with a phished contractor password, caught by the sequence rule and contained before any file activity.

**EX090.** Because generating mass renames on live clinic shares could disrupt care; lab evidence with guard rails was proportionate and the limit was reported.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and telemetry in this book are synthetic unless a sentence cites a public source.


- Alahmadi, B. A., Axon, L., & Martinovic, I. (2022). 99% false positives: A qualitative study of SOC analysts' perspectives on security alarms. *31st USENIX Security Symposium*, 2783–2800. <https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi>
- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Dempsey, K., Chawla, N. S., Johnson, A., Johnston, R., Jones, A. C., Orebaugh, A., Scholl, M., & Stine, K. (2011). *Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations* (NIST SP 800-137). <https://doi.org/10.6028/NIST.SP.800-137>
- Hassan, W. U., Guo, S., Li, D., Chen, Z., Jee, K., Li, Z., & Bates, A. (2019). NoDoze: Combatting threat alert fatigue with automated provenance triage. *NDSS Symposium*. <https://doi.org/10.14722/ndss.2019.23349>
- Kaloroumakis, P. E., & Smith, M. J. (2021). *Toward a Knowledge Graph of Cybersecurity Countermeasures* (MITRE D3FEND). The MITRE Corporation. <https://d3fend.mitre.org/resources/D3FEND.pdf>
- Kent, K., & Souppaya, M. (2006). *Guide to Computer Security Log Management* (NIST SP 800-92). <https://doi.org/10.6028/NIST.SP.800-92>
- Knerler, K., Parker, I., & Zimmerman, C. (2022). *11 Strategies of a World-Class Cybersecurity Operations Center* (2nd ed.). The MITRE Corporation. <https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center>
- Kokulu, F. B., Soneji, A., Bao, T., Shoshitaishvili, Y., Zhao, Z., Doupé, A., & Ahn, G.-J. (2019). Matched and mismatched SOCs: A qualitative study on security operations center issues. *ACM CCS 2019*, 1955–1970. <https://doi.org/10.1145/3319535.3354239>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). <https://doi.org/10.6028/NIST.CSWP.29>
- Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident Response Recommendations and Considerations for Cybersecurity Risk Management* (NIST SP 800-61 Rev. 3). <https://doi.org/10.6028/NIST.SP.800-61r3>
- SigmaHQ. *Sigma: Generic signature format for SIEM systems* (rule specification and repository). <https://github.com/SigmaHQ/sigma>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Strom, B. E., Applebaum, A., Miller, D. P., Nickels, K. C., Pennington, A. G., & Thomas, C. B. (2018, rev. 2020). *MITRE ATT&CK: Design and Philosophy* (MP180360R1). The MITRE Corporation. <https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf>
- Sundaramurthy, S. C., Case, J., Truong, T., Zomlot, L., & Hoffmann, M. (2014). A tale of three security operation centers. *ACM Workshop on Security Information Workers (SIW '14)*, 43–50. <https://doi.org/10.1145/2663887.2663904>
- van Os, R. (2016). *SOC-CMM: Designing and Evaluating a Tool for Measurement of Capability Maturity in Security Operations Centers* (Master's thesis). Luleå University of Technology. <https://ltu.diva-portal.org/smash/get/diva2:1031560/FULLTEXT02>
- Vielberth, M., Böhm, F., Fichtinger, I., & Pernul, G. (2020). Security operations center: A systematic study and open challenges. *IEEE Access*, 8, 227756–227779. <https://doi.org/10.1109/ACCESS.2020.3045514>
- Zimmerman, C. (2014). *Ten Strategies of a World-Class Cybersecurity Operations Center*. The MITRE Corporation. ISBN 978-0-692-24310-7. <https://www.mitre.org/sites/default/files/publications/pr-13-1028-mitre-10-strategies-cyber-ops-center.pdf>
