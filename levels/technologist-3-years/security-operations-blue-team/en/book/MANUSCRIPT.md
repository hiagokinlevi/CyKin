# Security Operations and Blue Team: Technologist Course

- Language: English (`en`); course 084, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; seven offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
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

Mei tests this layering on the clinic 2 server, which is itself a virtual machine. The processor and memory belong to a physical host run by the IT contractor, the operating system is Windows, and the practice database and file share are applications on top. A failed remote desktop logon therefore appears in the Windows security log, while the connection that carried it appears in the firewall log, two layers describing one event.

### 1.2 The course case

**Mei Tanaka** studies on the technologist programme at the fictional **Harbourside Polytechnic** and joins the fictional **Copperleaf Managed Security**, a small provider that monitors about forty small businesses. Her mentor is SOC lead **Raj Patel**. One client is **BrightSmile Dental**, a chain of three clinics.

Copperleaf watches its forty or so clients from one SIEM, so every analyst works across many small networks that look alike but belong to different owners. BrightSmile is a typical member of that client list: three clinics, no IT staff on site, an outside contractor for support and patient records on a server. Most of the course follows Mei through BrightSmile's onboarding, its May incident and the improvements that came after it.

### 1.3 Clients and servers

At each BrightSmile clinic, reception PCs (clients) use a practice-management server that stores appointments and patient records. A file share on the same server holds X-ray images and letters.

The client and server roles explain why the server matters most. If one reception PC fails, the other reception PCs can still book patients, but if the server is encrypted every PC loses appointments, records, X-ray images and letters at the same moment. Mei therefore treats each reception PC as a route towards the server and the server itself as the asset whose loss would stop a clinic working.

### 1.4 Services

The server runs several services: the database, file sharing, and remote desktop so the clinic's IT contractor can support it from outside. Every running service is something that could be misused and something that can be monitored.

For each service Mei asks two questions: who needs it, and from where. The database is needed by reception PCs inside the clinic; the file share by the same PCs and the X-ray workstation; remote desktop only by the contractor, who connects from outside. That last answer is the one that does not fit a closed clinic network, and it is the service that later gives the attacker a way in.

### 1.5 What gets recorded

Copperleaf installs an endpoint agent on servers and PCs that sends security events to its SIEM. The clinic's firewall sends connection logs. Together they show logons, new accounts, file changes and network connections.

Each source covers a different part of what happens at a clinic. The agent sees what happens on a machine, such as a logon to the server or a new local account, but not the traffic on the wire; the firewall sees connections in and out but not what a user did after logging on. Copperleaf joins both in the SIEM so that an analyst can follow one event from the network edge to the host.

### 1.6 Roles drive monitoring

A server holding patient records needs closer monitoring than a waiting-room tablet. Mei lists each device's role so alerts can be weighted.

Mei's role column has three values for BrightSmile: critical for each clinic server, standard for reception PCs and the X-ray workstation, and low for devices such as the waiting-room tablet. An alert from a critical host is shown first in the queue, and a new administrator account on CLINIC2-SRV is ranked above the same event on a tablet with no patient data.

### 1.7 Small-business reality

Small clients have no IT staff on site; an office manager is the contact. Copperleaf's advice must be simple to act on.

At BrightSmile the office manager can restart a PC, read an email and forward it to the contractor, but cannot change firewall rules. Copperleaf therefore writes each recommendation as a short action with an owner, such as asking the contractor to disable a port forward, rather than as a technical finding the manager would have to interpret and translate alone.

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

At clinic 2 a reception PC such as 10.2.0.15 never appears on the internet under its own address; outside services see only the clinic's single public address. Inside the firewall log, a source beginning with 10. is therefore a clinic device, and a source such as 203.0.113.45 is an outside address. Mei reads every log line by first deciding which side each address belongs to.

### 2.2 Ports and services

Services listen on numbered ports: 443 for web, 3389 for remote desktop, 445 for file sharing. A firewall rule that forwards port 3389 from the internet to the server exposes remote desktop to anyone.

A port number on its own is only a label, so Mei checks what actually listens behind it. On CLINIC2-SRV port 3389 leads to the Windows remote desktop service, which accepts a username and password. A forward rule on the firewall turns that internal service into an internet service, which is why the forwarded 3389 line matters more than any other entry in the rule list.

### 2.3 Internet services

Clinics use cloud email, an online booking site and a card-payment terminal. Each creates connections the firewall logs.

These outbound services are expected, so their connections are normal background in the firewall log. Mei notes the destinations each one uses, such as the booking site and the payment provider, so that a reception PC connecting to them is not mistaken for something suspicious, and a connection to an unfamiliar destination stands out against that known list. The card-payment terminal, for instance, should only ever talk to its payment provider, so any other destination from it deserves a closer look.

### 2.4 Reading firewall logs

A log line shows time, source address, destination address, port and action (allowed or denied). Many denied connections from one external address to port 3389 suggest password guessing or scanning.

Mei reads a denied line as a refused attempt, not as a harmless one. When one external address sends dozens of attempts to 3389 within a few minutes, the pattern is guessing; when many different addresses each send a few attempts, it is broad scanning. Both are worth counting, but only an allowed connection followed by a server logon shows that someone actually got in.

### 2.5 Internal versus external

Activity from inside the clinic network is usually staff; from outside it is anyone. Detection rules treat them differently.

The difference between the two sides is written directly into Copperleaf's rules. Several failed logons whose source is 10.2.0.15 usually mean a receptionist mistyped a password after the morning start, whereas the same number from an internet address means someone outside is trying passwords. The lab in chapter 14 shows this split directly: the internal source is printed without an alert, while the external source crossing the limit is flagged.

### 2.6 Exposure

Exposed services are a common entry route. The safer design is a VPN: staff and the IT contractor connect securely first, and remote desktop is not exposed directly.

With a VPN in place, the internet sees only the VPN service, which can require MFA before any connection reaches the clinic network. Remote desktop is still used by the contractor, but only after the VPN logon succeeds. Exposure is reduced from a password box open to the world to a gateway that demands a second factor first.

### 2.7 Case

Mei filters clinic 2's firewall log for port 3389 and sees thousands of connection attempts per day from many countries.

The attempts are spread across the day and night with no pause for clinic hours, which is what automated tools produce. None of these addresses belongs to the contractor, whose support sessions are a few connections a week. The volume shows that the forwarded port has been found by internet scanners and is being tested constantly, regardless of whether any attempt has yet succeeded.

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
- **EX006 — Safer design.** What safer design replaces exposed remote desktop? *Rubric:* 3 = VPN first, no direct exposure; 2 = partial; 1 = vague; 0 = none.

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

Clinic 2 alone produces thousands of firewall lines a day, and the server adds its own events, so reading by eye cannot keep up even for one small client. Mei writes Python because a script applies the same rule to every line and gives the same answer each time, which makes the result something Raj can check rather than a personal impression.

### 3.2 Splitting lines

Each event line has a time, host, event ID and key=value fields. Splitting on spaces gives the parts; a dictionary maps event IDs to names such as "logon failure".

In the lab each line is split on spaces, so the first part is the time, the second the host, the third the event ID and the rest the key=value fields. The dictionary `names` holds four IDs: 4624 logon success, 4625 logon failure, 4720 account created and 4732 added to local group. Any line whose third part is not one of those four IDs is treated as unparsed.

### 3.3 Counting

Python's Counter adds up how often each event type appears.

Each recognised event adds one to the counter under its readable name, so the script prints a count per event type without Mei preparing a list of types beforehand. The lab uses `counts[names[parts[2]]] += 1`, and because Counter starts every key at zero there is no need to check whether an event type has been seen before. Mei checks the printed counts against the input, because a counter that silently skips an event type would make every later report wrong.

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

Mei checks the arithmetic: three failures, one success, one account creation and one group change make six parsed lines, and the one unparsed line brings the total to seven, matching the input. If those numbers did not add up, a line would have been counted twice or lost, and she would fix the parser before trusting any result from it.

### 3.5 Safe handling

Real logs contain truncated or odd lines. Programs must skip them, count them and continue.

In the lab, the guard `if len(parts) < 4 or parts[2] not in names` catches the line "broken line without fields" and adds one to `bad` instead of stopping with an error. Without that guard the script would either crash or mislabel the line, and on a real export one corrupt line would end the run before the remaining events were counted. The count of skipped lines is itself useful, because a sudden rise in unparsed lines usually means the export format changed upstream.

### 3.6 Testing

Mei runs the parser on these known lines first; the expected counts are written down before running, so a mismatch shows a bug.

For the lab lines Mei writes the expected result in advance: three failures, one success, one account created, one group change and one unparsed line. The run matches those written expectations exactly, line for line. Had the script printed two failures, she would know the parser was wrong before using it on real exports, where nobody knows the correct answer beforehand. The written expectation also helps Raj, who can review the test lines and the expected counts without running the script himself.

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

One lab line becomes a record with time 2026-05-04T01:22:10Z, host CLINIC2-SRV, user reception, action account created and target support2. Once in that form, the SIEM can answer questions such as how many accounts reception created this month, which plain text lines could only answer if someone read them one by one. The same structure applies to the firewall lines, whose source address, destination port and action become fields that rules can filter directly.

### 4.2 Consistent names

Copperleaf monitors forty clients with different systems. If one calls the field "user", another "account" and a third "UserName", every rule must handle all three. Copperleaf maps all to one common model at ingestion.

Mapping at ingestion means a rule such as alerting on a new administrator is written once against the common field name and works for every client. Without it, Copperleaf would need forty slightly different versions of each rule, and a client whose field name was forgotten would silently get no alerts at all.

### 4.3 Entities

Users, hosts and clients are entities that persist across events. A table for each holds attributes such as role, criticality and owner.

For BrightSmile the host table holds CLINIC2-SRV with role patient records, criticality high and owner the IT contractor; the user table holds reception as a shared account. When an alert names a host or user, the analyst reads these attributes instead of guessing, and the criticality is what places the alert in the queue. Keeping these attributes in one table means a change, such as a new server role, is made once and appears on every later alert.

### 4.4 Relationships

A user logs on to a host; a host belongs to a client. These links let analysts ask "which client is this host?" instantly.

The links make questions like Mei's in the worked example easy to answer. From the user support2 the analyst reaches the host CLINIC2-SRV and from the host reaches BrightSmile, so a name that exists at two clients is never confused. The same links answer the reverse question of which users have logged on to a given server in the past week.

### 4.5 Time

All times are stored in UTC with the original time zone recorded, so events from clients in different zones line up.

BrightSmile's clinics and Copperleaf's analysts may sit in different zones, and some sources log local time. The lab lines end in Z, meaning UTC, so 01:12 in the log is an hour of the night that Mei converts to clinic local time before judging whether it is out of hours. Storing the original zone keeps that conversion checkable later by anyone reviewing the case. Mei's out-of-hours rule in chapter 7 depends on this, since its 07:00 to 19:00 window is clinic local time, not UTC.

### 4.6 Raw and normalised

The original raw line is kept alongside normalised fields, so nothing is lost if parsing was wrong.

If the parser had split a field wrongly, say putting part of a username into the source address, the raw line still shows what the server actually wrote. Mei can then fix the mapping and reprocess the stored raw lines. For incidents such as BrightSmile's, the raw line is also what the client and any investigator will want to see as evidence. Keeping both forms costs extra storage, but Copperleaf accepts that cost because a lost raw line cannot be recovered later from parsed fields.

### 4.7 Case

The BrightSmile events from chapter 3 are stored with host CLINIC2-SRV, which links to client BrightSmile and criticality "high".

Because the host links to its client and criticality, the account creation at 01:22 is not just an event ID 4720 on a host name; it is a new account on a high-criticality patient-records server at a named client. That context is what lets Mei treat it as urgent without first looking up which business CLINIC2-SRV belongs to. The same lookup works at every client, so an analyst unfamiliar with BrightSmile still sees immediately that the host stores patient records.

### Enrichment

At ingestion, each event is enriched with entity data: the host's client, criticality and role. Analysts see 'CLINIC2-SRV (BrightSmile, critical, patient records)' instead of a bare name, which speeds triage and reduces mistakes when similar host names exist across clients.

### Worked example

When Mei searches for "support2", results from two clients appear: BrightSmile's new admin and an old service account at a law firm. Because each event carries the client field, she separates them immediately and confirms that only BrightSmile's is new.

> **Synthetic case.** Records and clients are invented.

### Errors and limits

Mapping to a common model can hide source-specific detail; keep the raw record.

### Exercises

- **EX010 — Common model.** Why map all clients' fields to one model? *Rubric:* 3 = rules work across clients without handling variants; 2 = partial; 1 = style; 0 = none.
- **EX011 — Raw retention.** Why keep the raw line? *Rubric:* 3 = recover if parsing wrong; nothing lost; 2 = partial; 1 = vague; 0 = none.
- **EX012 — Client field.** How did the client field help Mei? *Rubric:* 3 = separated two clients' support2 accounts at once; 2 = partial; 1 = vague; 0 = none.

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

BrightSmile fits the description: three clinics, an office manager instead of an IT team, and a server reachable from the internet. Nobody chose BrightSmile in particular; automated tools found an open remote desktop port among thousands of addresses, and the weak reception password did the rest. Defending such clients means closing the common openings rather than predicting a specific attacker.

### 5.2 Ransomware

Ransomware encrypts files and demands payment. Before encryption, attackers usually gain access (for example through exposed remote desktop), create or abuse administrator accounts, and disable protections. Each step leaves traces defenders can detect.

The lab events show the first two of those steps on CLINIC2-SRV: access after failed guesses, then a new account added to Administrators. Disabling protections and mass file changes would come next in the usual sequence. Because each step produces its own record, a SOC that sees the early ones has a chance to stop the sequence before files are touched.

### 5.3 Exposed remote access

Remote desktop open to the internet attracts automated password guessing. Weak or reused passwords make guessing succeed.

Clinic 2's firewall log shows how much guessing an exposed port attracts: 41,000 attempts from 2,300 addresses in seven days. With that volume, a password such as the shared reception one, known to several staff and never changed, does not need to be guessed quickly; it only needs to be on a list the tools try eventually. Exposure and weak passwords multiply each other, which is why Copperleaf recommends closing the port rather than only asking staff to choose better passwords.

### 5.4 Helpful behaviours

Strong unique passwords, MFA on remote access, prompt updates and offline backups make attacks harder and recovery easier.

Each of these behaviours breaks a different step of the attack. Unique passwords and MFA make the guessing fail, updates remove known weaknesses an attacker could use after access, and offline backups mean encryption no longer forces the client to pay. BrightSmile's later changes, personal accounts and MFA on the VPN, apply the first two directly to the route used in May. None of these behaviours needs specialist staff on site, which matters for a client whose only local contact is an office manager.

### 5.5 Health data

Dental records are sensitive personal data. A breach affects patients and brings legal duties to notify.

For BrightSmile, the server holds appointments, patient records and X-ray images, so any intrusion has to be treated as a possible exposure of patient data, not only as an outage. That is why the client needs a clear account of what the attacker could reach, which depends on the logs Copperleaf collects from the server. Patients cannot change their dental history the way a user changes a password, so data taken from the server stays sensitive for years afterwards.

### 5.6 The defender's view

Defenders focus on the observable steps: access, privilege, defence changes, file activity. Detecting early steps gives time to act before encryption.

This is why Copperleaf's rules watch for new administrator accounts, protection changes and bursts of file renames rather than trying to recognise each ransomware family. A family name changes often; the need to gain access, gain privilege and touch many files does not. Detecting at the access or privilege step leaves the most time for a response. Raj's point in the worked example follows from this: the support2 account was an early step, and the minutes after it were the defender's best opportunity.

### 5.7 Case

The events from chapter 3 match the early steps: guessing, access as a weak account, a new administrator.

In the parsed lines, the three failures from 203.0.113.45 are the guessing, the 01:19 success as reception is the access, and the support2 account added to Administrators at 01:22 is the new privilege. Nothing in those lines shows protections being disabled or files changing yet, which means the sequence was caught at its early steps. Mei maps each parsed line to a step in a short table, which later becomes the opening of the incident timeline she writes for the client.

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

The lab in chapter 3 uses exactly these four IDs, which is why it can tell the BrightSmile story from seven lines. On Linux the equivalent lines appear in system authentication logs with different wording, so Copperleaf's mapping turns both into the same common fields before any rule runs, as chapter 4 describes for field names.

### 6.2 Audit settings

Events appear only if audit policy enables them. Copperleaf's onboarding checklist sets audit policy on each client server and verifies that test events arrive.

The test matters because a rule watching for an event that is never generated will never fire, and nothing tells the analyst so. By creating a harmless test event and checking that it reaches the SIEM, the onboarding engineer proves both that the policy is set and that the agent forwards the result. BrightSmile's worked example below shows what happens when that test is skipped: process creation logging was simply never switched on at clinic 2.

### 6.3 Processes

Process creation events show which programs ran and which program started them. A file-encryption tool started from an unusual folder is a strong signal.

A process event records the program's path and its parent, for example a tool launched by a logged-on user from a temporary or download folder rather than from Program Files. On a clinic server that runs a database and a file share, new programs should be rare, so such a launch gives an analyst something specific to examine.

### 6.4 Virtualization

Many small businesses run servers as virtual machines on one physical host. The host's management console can start, stop or snapshot every server, so access to it is highly privileged and must be monitored.

For BrightSmile this means CLINIC2-SRV is one of the guests on a host that the IT contractor manages. Someone with access to that console could switch off the server or delete its snapshots without logging on to Windows at all, so events from the host matter as much as events from the server itself.

### 6.5 Snapshots

Snapshots capture a server's state and can help recovery, but are not a backup if stored on the same host an attacker controls.

A snapshot sits on the same host and storage as the server it copies. An attacker who reaches the host console can delete snapshots as easily as the contractor can create them, so a snapshot helps when an update goes wrong but cannot be relied on as the only way back after ransomware. Copperleaf therefore lists snapshots and backups separately on each client inventory, so that nobody mistakes the first for the second during an incident.

### 6.6 Account changes

New accounts and additions to administrator groups are rare in small clinics. Alerting on them catches attackers who create their own access.

At a clinic of this size an administrator account is created perhaps when a new contractor starts, which makes an unplanned 4720 followed by a 4732 for Administrators unusual. The support2 account in chapter 3 is exactly that pattern, created by a reception account that had no business creating accounts at all. Mei's rule for these events includes the creating account in the alert text, so an analyst sees immediately when reception is the creator.

### 6.7 Case

BrightSmile's server is a virtual machine; the host is managed by the IT contractor.

That arrangement means the clinic server's own logs come through Copperleaf's agent, while the host's activity depends on what the contractor's console records and shares. Mei notes on the inventory that host-level logs are not yet collected, so anything done directly on the host would not appear in the SIEM. Mei adds the contractor's name and contact details to the host entry, because any action on the hypervisor during an incident must go through them.

### Updates

Operating system updates fix weaknesses attackers use. Copperleaf's agent reports patch levels, and clients receive a monthly list of overdue updates.

### Worked example

Mei checks BrightSmile's audit settings and finds process creation logging was off on the clinic 2 server — the onboarding checklist had been skipped during a rushed setup. She enables it with the contractor and confirms with a harmless test program that events now arrive.

> **Synthetic case.** Settings and events are invented.

### Errors and limits

Enabling more auditing adds volume; enable what rules and investigations need.

### Exercises

- **EX016 — Event IDs.** What do event IDs 4720 and 4732 record? *Rubric:* 3 = account created; added to local group; 2 = one; 1 = vague; 0 = none.
- **EX017 — Hypervisor access.** Why must virtualization host access be monitored? *Rubric:* 3 = controls all VMs: start, stop, snapshot; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Missing setting.** What was missing on clinic 2's server and how was it fixed? *Rubric:* 3 = process creation logging off; enabled and tested; 2 = partial; 1 = vague; 0 = none.

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

In the BrightSmile incident both checks passed for the wrong person. Authentication succeeded because the attacker had the reception password, and authorisation allowed account creation because reception was a local administrator. Fixing either one would have limited the damage: a second factor stops the logon, and a lower privilege stops support2 being created. Copperleaf's later recommendations to BrightSmile address both checks separately, adding MFA to authentication and removing administrator rights from the reception account.

### 7.2 Least privilege

Each account gets only the rights it needs. At BrightSmile, the reception account was a local administrator because an old booking program once needed it — an excess privilege that let the attacker create support2.

The booking program that needed the right had long since been replaced, but nobody removed the privilege afterwards. Mei records this as a typical small-business gap: a right granted for one reason years ago outlives that reason, and only a review of who holds administrator rights brings it to light.

### 7.3 Shared accounts

Several receptionists share one "reception" login. Shared accounts make it impossible to tell who did what and often have weak passwords that everyone knows.

When reception logs on at 01:19, the log cannot say which receptionist it was, or whether it was a receptionist at all. A shared account also cannot be disabled quickly during an incident without stopping every reception desk, which makes containment harder on top of making attribution impossible. Personal accounts later solve both problems at once, since each receptionist can be identified and one account can be disabled without stopping the others.

### 7.4 Service accounts

Programs run under service accounts with fixed passwords. They should not be able to log on interactively.

The practice database, for example, runs under a service account whose password is set once and rarely changed. If that account is used to open an interactive logon on the server, it is almost certainly a person using stolen credentials, which is why Copperleaf alerts on it as a specific rule. Mei lists every service account found on CLINIC2-SRV in the inventory, with the program that uses it, so the rule knows exactly which accounts to watch.

### 7.5 MFA on remote access

Requiring MFA for remote desktop or VPN would have stopped the password-guessing attack even with a weak password.

In May the attacker needed only the reception password because remote desktop asked for nothing else. With a second factor, the correct password from the guessing list would still have failed at the next step, and the 01:19 success would have been another failure in the log. MFA does not make a weak password safe elsewhere, but on the remote access route it removes the attacker's main advantage, an unlimited number of guesses.

### 7.6 Detecting misuse

Rules alert on interactive logons by service accounts, logons by shared accounts outside opening hours and new administrator accounts.

Each rule follows from one of the gaps in this chapter. Service accounts should not log on interactively, the shared reception account should not be used in the middle of the night, and new administrators are rare at a clinic. Mei's worked example shows that even simple rules need tuning against real history before they go live. Each rule is documented with its purpose and the test result, so the next analyst knows why the rule exists before changing it.

### 7.7 Case improvement

After the incident, BrightSmile gives each receptionist a personal account, removes administrator rights from reception, and requires MFA on the new VPN.

Each of these changes closes one link of the chain used in May. Personal accounts make each logon traceable to a person, removing administrator rights stops a reception logon from creating accounts, and MFA on the VPN stops a guessed password from being enough. Remote desktop is no longer exposed directly, so the 3389 forward is gone. Mei updates the client inventory with these changes, so later alerts are judged against the new design rather than the old one.

### Account reviews

Each quarter Copperleaf sends every client a list of accounts with administrator rights and asks them to confirm each one. At BrightSmile the first review removes three former staff accounts that were still enabled, closing doors nobody was watching.

### Worked example

Mei writes a rule: alert when the "reception" account logs on outside 07:00–19:00 local time. Testing on a month of history shows two matches, both at 07:05 by the early receptionist — clocks differ slightly. She widens the window to 06:45 and documents why.

> **Synthetic case.** Accounts and events are invented.

### Errors and limits

Time-based rules break when business hours change; review them with the client.

### Exercises

- **EX019 — Excess privilege.** What excess privilege helped the attacker? *Rubric:* 3 = reception account was local admin; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Shared account problems.** Name two problems with shared accounts. *Rubric:* 3 = no individual accountability; weak known passwords; 2 = one; 1 = vague; 0 = none.
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

Each zone has its own trust level: reception PCs handle bookings and records, the server stores them, the X-ray workstation runs vendor software, and guest Wi-Fi carries patients' phones. Placing patients' devices on the same network as the server would let any infected phone reach the file share. The X-ray workstation also deserves its own zone, because it cannot run an agent and its traffic should therefore be as predictable as possible.

### 8.2 Boundaries

The firewall separates zones and the internet. Rules should allow only needed traffic: reception PCs to the server's database and file ports, nothing from the internet inward except through the VPN.

Writing rules this way means anything not listed is refused by default. If a reception PC later tries to reach the server on an unexpected port, the firewall denies and logs it, and that denied line becomes evidence Copperleaf can see rather than a connection that silently succeeds. The rule list is short at a clinic, so Mei can read every entry during a review and check that each one has a named reason to exist.

### 8.3 Remote access

A VPN with MFA lets the IT contractor and managers connect securely. Remote desktop is then allowed only from VPN addresses.

The contractor's support sessions continue as before, but each starts with a VPN logon and a second factor. On the firewall, the rule for 3389 now names the VPN address range as its only permitted source, so the internet scanners that produced 41,000 attempts in a week see nothing to try. Any remote desktop connection that does not come from the VPN range is now refused at the firewall and logged as denied, which is easy to alert on.

### 8.4 Sensors

Endpoint agents on server and PCs, firewall logs and the cloud email audit log give Copperleaf visibility. The X-ray workstation runs vendor software that forbids agents, so firewall logs are its only monitoring.

The X-ray gap is a deliberate trade-off rather than an oversight, because installing an agent would breach the vendor's support terms. Mei records it so that analysts know any investigation of that workstation must rely on connection records alone, which show where it talked to but not what ran on it.

### 8.5 Backups

Backups must sit outside the zone an attacker could control, or be immutable.

BrightSmile's nightly backups sit on a network device in the server room, inside the same zone as the server. Raj's recommendation of an offline or immutable copy follows from this rule: a backup an administrator can delete is not safe from an attacker who has become administrator. An offline copy is disconnected after each backup run, while an immutable copy cannot be altered or deleted until its retention period ends, even by an administrator. Either choice means the most recent good copy survives an attacker who controls the clinic network.

### 8.6 Defence in depth

No single control stops everything: VPN, MFA, least privilege, monitoring and backups together make a successful attack much harder.

The May incident shows how the layers would have worked together. Without exposure the guessing would not have started; with MFA it would not have succeeded; with least privilege support2 could not have been created; and with offline backups even a successful encryption would not have been final. Copperleaf presents the layers to BrightSmile as a short list, so the office manager can see which ones are already in place and which remain open.

### 8.7 Reviewing against attacks

Mei walks the ransomware steps from chapter 5 through the new architecture: access now needs VPN plus MFA; privilege is limited; monitoring alerts on account changes and file spikes; backups are offline.

At each step Mei asks what the attacker would now need and what Copperleaf would see. Guessing the reception password is no longer enough without the second factor, and a new administrator or a burst of file renames now raises an alert. If encryption still started despite all this, an offline copy would remain for recovery.

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
- **EX024 — Clinic 3 finding.** What did the review find at clinic 3? *Rubric:* 3 = guest Wi-Fi shared reception network; separated; 2 = partial; 1 = vague; 0 = none.

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

In the lab, the baseline for CLINIC2-SRV covers three hours over ten working days: 01:00, when the clinic is closed, 09:00, when reception starts, and 13:00, after lunch. The night hour holds nine zeros and a single one, while 09:00 ranges from 12 to 16 logons. These two shapes, a near-silent night and a busy morning, are what make an unusual hour stand out at all.

### 9.2 Measuring deviation

Comparing tonight's count to the baseline's mean and maximum shows whether activity is unusual. Simple rules — "above the highest value seen plus a margin" — are easy to explain to clients.

The lab's rule is exactly of that kind: tonight's 01:00 count is unusual if it exceeds the night maximum of 1 plus a margin of 3, so anything above 4 is flagged. Mei could explain that sentence to the office manager in one line, which would be much harder for a model based on standard deviations alone, even though the lab prints those as well.

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

Mei checks the figures by hand before writing them up. The ten 09:00 values sum to 138, which gives 13.8 as the mean, and the 01:00 values sum to 1, giving 0.1. With a night limit of 4, seven logons are almost twice the limit, so the flag does not depend on a borderline value or a rounding choice. The standard deviations are printed too, but the flag itself uses only the maximum and the margin, which keeps the decision easy to explain.

### 9.4 Evidence preservation

When an incident starts, analysts export relevant logs, record a hash for each file and note who exported what and when. Exports are stored read-only.

For BrightSmile, Mei exported the security log as E-1 and the firewall log as E-2 and recorded a SHA-256 hash for each. If anyone later questions whether E-1 was changed, recomputing its hash and comparing it to the note settles the question. Read-only storage prevents accidental edits by the analysts who open the exports during the investigation.

### 9.5 Consistent times

All times are UTC in records, with local time added in client reports. Mixing them causes confusion about sequence.

Mei's incident note records 01:00–02:00 UTC, and the client report adds the clinic's local time beside it. If the note had mixed the server's UTC entries with a local time from a phone call, the 01:36 isolation could appear to come before the 01:22 account creation, and the client would read a sequence that never happened. Analysts at Copperleaf write UTC in every case entry, and only the client-facing summary converts times, which keeps the conversion in one place.

### 9.6 Measurement honesty

Ten days is a short baseline; holidays and staff changes alter patterns. Mei notes these limits in every report.

A ten-day baseline also covers only working days, so a Saturday clinic session or an early-opening week could produce night or early logons the baseline has never seen. Mei writes the period and the number of days next to every figure, so a reader knows that "maximum 1" means one in ten nights, not one in a year. When a baseline is recalculated, Mei compares the new maximum with the old one, so a sudden jump in normal activity is noticed rather than absorbed.

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

For BrightSmile this means Copperleaf watches the clinic servers and PCs through its agent and the firewall logs, triages what the rules raise and tells the office manager what to do. It does not run the clinic's IT; changes to the firewall or the hypervisor remain the IT contractor's work, carried out on Copperleaf's advice.

### 10.2 Workflow

Logs flow into the SIEM; rules raise alerts; analysts triage, investigate and either close, advise the client or act under agreed authority; every step is recorded in the case system.

The BrightSmile alert on the incident night followed exactly this path. The server's events reached the SIEM, the new-administrator rule raised an alert, Mei triaged it, Raj approved containment, and Copperleaf isolated the server and disabled two accounts. Each of those steps has an entry in the case system with a time and a name, which later lets the team rebuild the night exactly.

### 10.3 Authority

Copperleaf may isolate an endpoint through its agent and disable accounts it manages, but only for alert types and clients where the agreement allows. Other actions are advised, not taken.

Under BrightSmile's agreement, isolating an endpoint and disabling local accounts were permitted, so Copperleaf could act on CLINIC2-SRV at night without waiting for the morning. Changing the firewall's forwarding rule was not, so closing port 3389 was advised to the contractor instead. Mei checks the agreement first because a client with different terms may allow only advice.

### 10.4 Frameworks

NIST CSF 2.0 organises outcomes into Govern, Identify, Protect, Detect, Respond and Recover; Copperleaf mainly delivers Detect and Respond. NIST SP 800-61r3 frames incident response within risk management and continuous improvement.

The BrightSmile incident night maps onto those six functions quite directly. Detect covers the new-administrator alert, Respond covers isolation and account disabling, and Recover covers restoring files and service the next day. Govern and Identify still matter, because Mei's inventory and the client agreement belong there, but they are mostly the client's responsibility with Copperleaf's advice.

### 10.5 Roles

Tier-1 analysts triage; senior analysts investigate; Raj leads and approves containment; client contacts receive advice and make business decisions.

On the BrightSmile night, Mei triaged as the analyst on shift, Raj approved containment as lead, and the office manager decided to keep the clinic closed until the morning review. Each decision sat with the person entitled to make it. Separating these roles keeps a trainee from taking actions alone and keeps business choices with the client. Clear roles also matter at handover, because the next shift can see in the case system who approved which action and why.

### 10.6 Service levels

High-severity alerts are acknowledged within 15 minutes, 24 hours a day.

Fifteen minutes is short because of how fast the early steps move. On CLINIC2-SRV only three minutes passed between the reception logon at 01:19 and the creation of support2 at 01:22, so an alert left waiting until the morning would arrive after the damage. Acknowledgement starts the clock on investigation; it does not mean the alert is resolved. The service level applies at night as well, which is why Copperleaf keeps an analyst on shift and a lead reachable by phone around the clock.

### 10.7 Mei's role

As a trainee, Mei triages under supervision and drafts client advice for Raj's review.

Supervision means Mei's decisions are checked before they reach a client. She can triage an alert and propose closing it, but a containment action or a message to BrightSmile goes through Raj first. Her drafts on the incident night, such as the incident note, were reviewed by him before anything was sent to the office manager. Raj's review also teaches, because each correction to a draft shows Mei what a client needs to read and what can be left out.

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

The extra words in that enriched line change what the analyst decides. A new administrator on a test machine during working hours might wait for the morning queue, whereas the same event on the patient-records server of a closed clinic justifies waking Raj. Mei's role sheet from chapter 1 is what provides those words; without it the alert would read only as a host name and an event ID.

### 11.2 Inventories

For each client, Copperleaf records hosts, roles, operating systems, criticality (low, medium, high), business hours and contacts. Agents report hosts automatically; roles and criticality come from the client.

The split matters because the agent can see that CLINIC2-SRV exists and runs Windows, but cannot know that it holds patient records or that the clinic closes in the evening. Those facts come from the office manager and the contractor. Mei's inventory for clinic 2 combines both kinds: agent-reported hosts plus the roles and hours the client confirmed.

### 11.3 Criticality

Servers with patient or financial data are high; reception PCs medium; guest devices low. Criticality multiplies alert severity in queue ordering.

In practice, the same rule produces different priorities by host. A new local administrator on CLINIC2-SRV, rated high, lands at the top of the queue, while the same event on a guest device would sit lower. Mei checks this ordering on the queue view, because a wrong criticality rating would push a serious alert below routine ones. Mei applies the ratings the client gave, but questions them when an alert reveals a host doing more than its rating suggests.

### 11.4 Business hours

Clinic hours make night-time activity on clinic systems more suspicious; a law firm with late workers has different hours.

BrightSmile's clinics close in the evening, and Mei's out-of-hours rule uses a window from 06:45 to 19:00 local time for the reception account. A law firm client with staff working late would need a different window, so the hours are stored per client rather than written into the rule. The 01:19 reception logon on the incident night fell well outside BrightSmile's hours. Stored hours also feed the enrichment line on alerts, which is how "clinic closed" appeared beside the support2 alert on the incident night.

### 11.5 Keeping current

Inventories decay as clients add devices. A monthly report lists new hosts seen by agents but missing roles, and Copperleaf asks the client to classify them.

The worked example shows why the report matters: in one month clinic 1 gained a new card terminal and a dentist's personal laptop, neither of which anyone had mentioned. Without the report, an alert from the laptop would have arrived with no role and no owner, and the analyst would have spent the first minutes finding out what it was.

### 11.6 Contacts

Every client has a primary and backup contact with phone numbers for night calls; at BrightSmile these are the office manager and the IT contractor.

On the incident night these contacts were used in order. The office manager was called at 01:40 and agreed to keep the clinic closed, and the IT contractor was the person who would later change the firewall and restore the server. Mei checks the numbers during onboarding, because a wrong number discovered at night costs time that cannot be recovered.

### 11.7 Case

When the support2 alert fired, enrichment showed "CLINIC2-SRV — high — patient records — clinic closed".

Each part of that line came from a different place. The host name came from the agent, the high criticality and patient-records role from the client inventory, and "clinic closed" from the stored business hours compared with the alert time. Mei did not need to look anything up before deciding that the alert was urgent. That one enriched line is also what Raj read when Mei phoned him, so the decision to isolate the server rested on facts already in front of both of them.

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
- **EX033 — Unknown hosts.** What were the two unknown hosts, and what was done? *Rubric:* 3 = card terminal recorded; personal laptop → guest Wi-Fi advised; 2 = partial; 1 = vague; 0 = none.

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

For BrightSmile, the server's agent sends Windows events and the firewall sends syslog through the collector box at the clinic. Both arrive at Copperleaf's collectors and then the SIEM, where the new-administrator rule ran. A break anywhere on that path stops alerts, which is why Mei learns the path before trusting what she sees in the SIEM.

### 12.2 Collection points

Agents send directly over encrypted connections. Firewalls send syslog to a small collector box at each client site, which forwards it securely.

The difference between the two methods is practical rather than a matter of preference. An agent on CLINIC2-SRV can send its own events securely, but a small clinic firewall usually speaks only syslog and cannot encrypt it. The collector box sits inside the clinic, receives that syslog over the local network and forwards it securely, so firewall lines never cross the internet unprotected. Because the collector box has its own power and network connection, Mei lists it in the BrightSmile inventory as a monitored device like any other.

### 12.3 Delays

Agent events usually arrive within a minute; firewall logs within five. Cloud email audit logs can take up to 30 minutes.

These delays affect how analysts should read recent results in the SIEM. A firewall event at 01:30 may arrive at 01:35, so an empty firewall result at 01:31 does not prove that nothing happened. For a suspected email account takeover, Mei waits for the cloud audit log to catch up before concluding that a mailbox rule was not created. Mei records these typical delays on each client's data-flow diagram, so an analyst can judge how long to wait before treating a missing event as absent.

### 12.4 Gaps

A collector box that loses power, an expired certificate or a firewall update that resets logging settings can stop data silently.

Each of these failures looks the same in the SIEM: the source goes quiet. A quiet source at night could be a sleeping clinic or a broken feed, which is why the next measure compares volumes against what the source normally sends rather than waiting for someone to notice that alerts have stopped. None of these causes is an attack, yet each leaves the SOC blind in the same way as an attacker who deliberately stopped the logging.

### 12.5 Monitoring the flow

Copperleaf tracks events per source per hour; a sudden drop to zero raises a data-gap alert to engineering, not to analysts' main queue.

Sending these alerts to engineering keeps analysts focused on security alerts while still making sure someone fixes the feed. Each data-gap alert records which source dropped and when, so if an incident later falls into that window, the case can state plainly that the source was not reporting at the time. Hourly counts also reveal a source that drops gradually, for example a firewall whose log volume halves after an update changed its settings.

### 12.6 Documentation

Each client has a data-flow diagram: sources, collectors, protocols and expected volumes.

For BrightSmile, the diagram shows the agent on each server and PC, the firewall sending syslog to the collector box at each clinic and the cloud email audit log pulled directly. The expected volume beside each source is what the gap monitor compares against, and the verified date shows when someone last checked the diagram against reality. The diagram is short enough to read during an alert, which matters when an analyst needs to know quickly whether a quiet source is expected.

### 12.7 Case

During onboarding of a new client, Mei checks the diagram against actual data and finds firewall logs missing.

The diagram said firewall syslog was flowing, but the SIEM showed no firewall events from that client at all. A diagram records intent, while the SIEM records what actually arrives, so Mei treats any disagreement between them as a fault to investigate before she accepts the onboarding as complete. Checking this during onboarding, before the client relies on the service, is far cheaper than discovering the gap during an incident.

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
- **EX036 — Onboarding fix.** What was wrong at the new client and how was it confirmed fixed? *Rubric:* 3 = syslog sent to old address; corrected; volume verified in SIEM; 2 = partial; 1 = vague; 0 = none.

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

Each part of the BrightSmile scenario points to something to watch. "External attacker" points to the firewall log, "guesses a password" to failed logons, "gains admin rights" to new administrator accounts and "encrypts patient records" to file activity on the server. Written that way, a scenario is already half a detection plan.

### 13.2 Scenarios for clinics

Copperleaf uses five for small healthcare clients: ransomware via remote access, email account takeover leading to invoice fraud, lost unencrypted laptop, insider misuse of patient records, and supplier compromise (for example the IT contractor's account).

Each of the five matches something Copperleaf's clinics actually have: exposed or remote access, cloud email used for supplier payments, laptops carried between clinics, staff with access to records, and an outside contractor holding administrator rights. A scenario that does not match a client's assets, such as one involving a data centre, is left off the list.

### 13.3 Likelihood and impact

Each scenario gets a rough rating. Ransomware via remote access is high likelihood (before the VPN change) and high impact.

The rating is kept rough on purpose, using high, medium and low rather than percentages that would suggest precision nobody has. For BrightSmile before the VPN change, likelihood was high because the port was exposed and attracting 41,000 attempts a week, and impact was high because the server held all patient records. Mei writes one sentence beside each rating explaining it, so the rating can be challenged on its reasons rather than on its label.

### 13.4 Mapping to detection

For each scenario, the team lists detections that would catch its steps — failed logons, new admin accounts, rename spikes — and response actions.

For the ransomware scenario the mapping is concrete: failed logons from outside cover guessing, the new-administrator rule covers privilege, and the rename spike covers encryption. Each detection has a planned response, such as isolating the host or disabling an account. A step with no detection beside it is a gap, which is exactly what the next measure looks for.

### 13.5 Gaps

The supplier-compromise scenario had no specific detection: a contractor logon looks normal. Mei proposes alerting on contractor logons outside agreed support windows.

The contractor is supposed to log on to BrightSmile's systems, so rules about remote logons or administrator activity cannot tell their normal work from an attacker using their account. Support windows give a reference: a contractor logon at a time no support was scheduled is worth asking about, even though it may still turn out to be legitimate.

### 13.6 Review after incidents

After the BrightSmile incident, the ransomware scenario's likelihood is reduced for that client (VPN and MFA added) but kept high for clients without them.

The change is client-specific because the reason for the high rating changed only at BrightSmile. Clients that still forward remote desktop from the internet keep the high rating, and Mei's table records why each client's rating differs, so a later reviewer can see that the difference rests on a control, not on guesswork. The table keeps the earlier rating beside the new one, so the effect of the VPN and MFA change on BrightSmile's risk is visible to the client.

### 13.7 ATT&CK link

Scenario steps are tagged with ATT&CK techniques for consistency across clients.

Tagging lets Copperleaf ask questions across its forty clients, such as which scenarios rely on valid accounts or on remote services, using one shared vocabulary. Mei uses the ATT&CK names published by MITRE rather than inventing her own labels, so another analyst or the client's contractor can look each technique up independently. The tags do not replace the scenario text; they sit beside each step so that the same step is labelled the same way for every client in Copperleaf's records.

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
- **EX039 — Supplier gap.** How was the supplier-compromise gap addressed? *Rubric:* 3 = alert on contractor logons outside support windows; 2 = partial; 1 = vague; 0 = none.

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

The rule has three parts that each need a decision: what is counted, over how long, and at what number the alert fires. In the lab the count is failed remote desktop logons, grouped by source address, and the limit is 20 for external sources. Every later choice in this chapter adjusts one of those three parts against real history.

### 14.2 Choosing the window

Fifteen minutes catches fast automated guessing; slower attackers need a longer window or a daily count rule.

The trade-off in choosing a window is noise against how much it can reach. A long window catches a patient attacker who tries one password every few minutes, but it also gathers more ordinary mistakes from the contractor and staff. Mei keeps the 15-minute rule for fast guessing and would cover slow attempts with a separate daily count, rather than stretching one rule to cover both. Whichever window is chosen is written on the rule page, so an analyst knows which kind of guessing the rule can and cannot see.

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

Mei checks the lab input against the printout: the list holds 46 entries for 203.0.113.45, three for 198.51.100.9 and four for 10.2.0.15, and the output shows the same three counts. Only the first source both comes from outside and reaches 20, so exactly one ALERT is printed, which is what the rule was written to do.

### 14.4 Internal sources

Internal failures are handled by a separate, higher threshold, because staff mistakes are common and attackers inside the network show other signs.

Inside a clinic, several failures in a row usually mean a receptionist on a cold morning or a forgotten password after a change. An attacker already inside would more often show up through other rules, such as a new administrator or an unusual process, so a high threshold for internal failures loses little while removing most daily noise.

### 14.5 Setting the threshold

Mei looks at a month of history: legitimate external failures (the contractor mistyping) never exceeded six in 15 minutes. A threshold of 20 leaves margin.

Six legitimate failures against a limit of 20 means an honest user would need to make more than three times their worst recorded month of mistakes to trigger the rule. The 46 failures from 203.0.113.45 are more than double the limit, so the gap between normal and attack in this data is wide enough to set the limit without fine adjustment.

### 14.6 Documentation

The rule page states purpose, logic, threshold reasoning, known benign triggers and response steps.

For this rule, the benign triggers include the monitoring tool found during testing, and the response steps are the ones in the worked example. An analyst meeting the alert at night reads the page, not Mei's memory, so anything Mei learned while building the rule must be written there before the rule goes live. The page also records the testing replay and the exception list for the misconfigured monitoring tool, with the reason each exception was granted.

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

The replay uses the same kind of per-minute counts that the real file share at clinic 2 produced on the incident night, but no clinic data and no encryption program are involved. Trainees see only numbers on a screen, which keeps the exercise safe while still asking them to make the decision an analyst faces at 01:34.

### 15.2 Baseline and threshold

In quiet minutes, the share sees 0–3 renames per minute. The rule sets the limit at ten times the highest quiet value: 30 renames per minute.

The baseline values 2, 0, 3 and 1 give a highest quiet value of 3, so ten times that is 30. The code also uses `max(max(baseline), 1)`, which keeps the limit at 10 or above even if every quiet minute were zero; without that guard, a share with no quiet renames would get a limit of zero and alert on its first rename.

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

The jump is large compared with the limit: 180 is six times 30, and 410 is nearly fourteen times. Nothing between the quiet minutes and the spike approaches the limit, so the start time does not depend on how the limit is set. Adding 180, 410 and 395 gives 985 renames, matching the file-change count in the worked example. Mei also notes that the spike continues at 01:36, the minute Raj approved isolation, so encryption was still running when containment began.

### 15.4 Response decision

A spike on a patient-records share at night is acted on immediately: isolate the server, then investigate. Waiting for certainty would let encryption continue.

On the incident night every minute of waiting cost hundreds of files: 410 renames at 01:35 alone. Isolation stops the server talking to the network, which halts encryption from a remote session, and the investigation then works on preserved logs. Raj's approval two minutes after the spike start is the kind of speed this measure asks for. The investigation that follows can still find that the renames were legitimate, and isolation can then be reversed with little lasting harm to the clinic.

### 15.5 False alarms

Legitimate bulk renames happen — for example, an X-ray system reorganising folders after an update. The response step includes a quick check of the process doing the renaming.

The check is short: which program and account are performing the renames. An X-ray vendor's update tool running under its service account after a scheduled update explains a spike, whereas an unknown program launched from the support2 session does not. Process creation logging, switched on at clinic 2 in chapter 6, is what makes that check possible on that server.

### 15.6 Reflection

Trainees compare their time-to-isolation in the lab. The fastest act within two minutes of the spike.

Two minutes matters because of the per-minute counts: at the replayed rates, each extra minute is several hundred more renamed files. Trainees who hesitate usually do so waiting for proof of encryption, and the comparison shows them that the spike itself, on a patient-records share at night, is already enough to act on. The lab records each trainee's time from the spike to the isolation decision, so the comparison is based on measured times rather than impressions.

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

For BrightSmile the order was a logon as reception at 01:19, then support2 created at 01:22, then support2 added to Administrators, and finally renames at 01:34. Single-step rules caught pieces of this; a rule that knows the order can recognise the pattern while it is still at the second or third step. Each step is also visible on its own in the logs, so the sequence rule adds certainty without needing any new data source at the client.

### 16.2 The BrightSmile sequence

Logon from an external address, then account creation by that session, then the new account added to Administrators within 30 minutes. Each step alone is sometimes legitimate; together they are rare.

A contractor creating an account for a new receptionist is legitimate, and a remote logon by the contractor is legitimate. What makes BrightSmile's case rare is that the same external session did all three things within minutes, at night, from an account that should never create accounts. Requiring all three steps cuts the false alarms that each step alone would produce.

### 16.3 Building the rule

Mei's rule joins three event types on host and session within 30 minutes. The alert text lists all three steps with times, so analysts do not have to search.

Joining on session means the account creation must come from the same logon that arrived from outside, not merely from the same host. That detail prevents an unrelated local account change, made by someone else on the server, from being stitched to an external logon that happened to occur at about the same time.

### 16.4 Tuning

At one client, the IT contractor routinely creates admin accounts for new staff after logging in remotely through the VPN. The rule excludes sessions from the contractor's VPN addresses during support windows but still alerts outside them.

The exclusion is deliberately narrow: it needs both the contractor's VPN address and a time within the agreed support window. If the contractor's account were stolen and used at night, or from somewhere other than their VPN, the sequence would still alert. That keeps routine onboarding of staff quiet without blinding the rule to the supplier scenario of chapter 13.

### 16.5 Severity

Sequences on high-criticality hosts at night are rated high and page the on-call analyst.

The BrightSmile sequence on CLINIC2-SRV at 01:22 meets both conditions: high criticality and night time. Paging means the on-call analyst is alerted by phone rather than waiting for someone to look at the queue, which is what the 15-minute acknowledgement target from chapter 10 assumes for high-severity alerts. The same sequence on a medium-criticality reception PC during opening hours is rated lower and waits in the queue for the analyst on shift. Mei writes both cases on the rule page, so the on-call analyst can see why a page arrived and how the rating was reached.

### 16.6 Testing

Mei tests the rule against the BrightSmile events: it fires at 01:22, twelve minutes before the rename spike.

The rule fires at 01:22 because that is when the third condition could be met: support2 was created by the external session and added to Administrators. The firing time is set by the attacker's last step, not by when the rule runs, so it is as early as the data allows. The test also confirms that the alert text lists the logon at 01:19, the creation at 01:22 and the group change, as the rule design requires.

### 16.7 Value of earlier alerts

Earlier detection gives more time. If this rule had existed, isolation could have happened before any file was renamed.

In the real incident isolation came at 01:36, two minutes after the spike, and 985 files were renamed before it took effect. The sequence rule shifts the alert twelve minutes earlier, which in the quick case moves isolation ahead of the first rename and in the slow case still shortens the encryption time considerably. Mei is careful to call this an estimate from the replay, because nobody can know exactly how the attacker would have reacted to an earlier isolation.

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
- **EX048 — Benefit estimate.** What did the replay show about timing? *Rubric:* 3 = fires 01:22, 12 min before spike; quick ack could isolate before 01:34; 2 = partial; 1 = vague; 0 = none.

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

Each tool answers a different need on an incident night. The SIEM found the support2 account, the agent isolated CLINIC2-SRV, the case system recorded who approved what and when, and the knowledge base held the rule page and BrightSmile's profile with its contacts. Losing any one of them would have slowed the response at a specific step.

### 17.2 Fit for size

A small SOC needs tools that are easy to maintain, support many clients and integrate well. Feature-heavy tools that need a dedicated engineer can be a burden.

Copperleaf is a small provider covering about forty clients, so every hour spent tuning a tool is an hour not spent on alerts. A tool that needs constant attention from a specialist engineer would leave the analysts short-handed; one that can be maintained by the existing team fits the size of the service.

### 17.3 Workflow support

Knerler, Parker and Zimmerman (2022) advise leveraging tools to support analyst workflow. At Copperleaf, alerts open in the case system with enrichment and links to the client profile, so analysts rarely switch screens.

On the BrightSmile night, the alert opened with the enriched host line and links to the client profile and contacts, so Mei did not have to search three systems before phoning Raj. Fewer screens means fewer chances to copy a wrong host name or call the wrong client during the first critical minutes.

### 17.4 Multi-client separation

Tools must keep clients' data separate and show which client each alert belongs to. Mistakes here could leak one client's data to another.

Mei's search for support2 in chapter 4 shows the risk: two clients had accounts with the same name. If the tools had not carried the client field, she might have isolated a law firm's server or reported the wrong client's activity to BrightSmile. Client separation is therefore checked on every new search view and report template. Access rights follow the same principle, so an analyst who views one client's alert cannot accidentally open another client's raw logs.

### 17.5 Evaluating tools

Copperleaf judges tools by outcomes: time to triage, missed detections, effort to maintain. A trial of a new endpoint agent measures these on three clients before any decision.

Using the same three measures for every trial lets Raj compare a new tool with the current one on Copperleaf's own work rather than on a vendor's list of features. Three clients is a small sample, so the trial results guide the decision without being treated as proof that the tool will behave the same on every client.

### 17.6 Tool health

Tools themselves need monitoring: agent versions, SIEM storage and rule run times.

An old agent version might stop sending a new event type, full SIEM storage can drop events, and a rule that takes too long may not finish before the next run starts. Each failure removes detection quietly in the same way as a broken log feed, so these measures go to engineering alongside the data-gap alerts. Mei's onboarding check of BrightSmile's agents includes their version, so an outdated agent on a clinic PC is listed and updated.

### 17.7 Avoiding tool sprawl

Each new tool needs an owner and a reason; overlapping tools are retired.

An owner is the person who updates the tool, watches its health and decides when it is no longer needed. Without one, a tool keeps running with old settings and nobody notices when it stops working. Two tools doing the same job also double the alerts analysts must reconcile without finding anything new. When the new endpoint agent is adopted for servers, Raj names its owner and records which old agent features it replaces on those hosts.

### Access to tools

Analyst accounts on the SIEM and case system use MFA and are reviewed quarterly.

### Worked example

In the endpoint agent trial, the new agent detected the same test events but reduced analyst triage time by two minutes per alert because it showed process trees directly in the alert. It also used more memory on old clinic PCs. Raj decides to adopt it only for servers and newer PCs.

> **Synthetic case.** Tools and trial results are invented.

### Errors and limits

Vendor demonstrations show best cases; trial tools in your own environment.

### Exercises

- **EX049 — Four tools.** Name the four main parts of Copperleaf's toolset. *Rubric:* 3 = SIEM, endpoint agents, case management, knowledge base; 2 = three; 1 = one; 0 = none.
- **EX050 — Client separation.** Why must tools separate clients' data? *Rubric:* 3 = prevent leaking one client's data to another; know which client; 2 = partial; 1 = vague; 0 = none.
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

Mei lists each control against the step it would have broken: VPN with MFA against the guessing and the 01:19 logon, removing admin rights from reception against creating support2, personal accounts against the untraceable shared logon, and offline backups against the encryption. The list turns the incident timeline into a plan for prevention.

### 18.2 Prioritising

Copperleaf ranks recommendations by risk reduction and effort. VPN with MFA is top: it removes the main entry route for little cost.

Ranking by risk reduction and effort puts VPN with MFA first because it removes the route that produced 41,000 attempts a week, at the price of a VPN licence and about a day of contractor time. Removing admin rights from reception is also cheap, while personal accounts need more setup time and staff training, so they come later in the plan. Offline backups are ranked high too, because they limit the impact of any attack that gets past the other controls despite the first two changes.

### 18.3 Client decisions

Clients decide and pay; Copperleaf advises. Clear explanations and cost estimates help clients act.

BrightSmile's office manager decides how much to spend and when the clinic can tolerate a change, because only she knows the clinics' budget and patient schedule. Copperleaf's job is to make the choice clear, which is why Mei's one-page estimate puts the cost of the VPN next to the cost of a closed clinic. When a client chooses not to act, Copperleaf records the decision and the reason, so the remaining risk is visible at the next review.

### 18.4 Verifying

After the client says a control is in place, Copperleaf checks: an external scan (authorised in the agreement) confirms port 3389 is closed; a test logon confirms MFA on the VPN.

The scan and the test logon check what the client reported rather than relying on it. A forwarding rule left behind for an old purpose, or MFA enabled for some users only, would look fine in a status update but fail these checks. Mei records the date and result of each check on the client's recommendation list.

### 18.5 Tracking adoption

A dashboard shows each client's open recommendations and age. Raj reviews it monthly with account managers.

Age matters because a recommendation that has been open for months usually means the client is stuck, not that the risk has gone away. In Raj's monthly review, old items get a call from the account manager to find out what is blocking them, such as cost, contractor time or a vendor restriction. The dashboard also shows closed items with their verification date, so Raj can see that a control was checked rather than only reported as done.

### 18.6 Controls across clients

When one client's incident reveals a common weakness, Copperleaf checks all clients. Six other clients also exposed remote desktop.

The check uses data Copperleaf already holds: firewall logs showing accepted inbound connections on 3389. Finding six exposed clients turns one incident into protection for others before they are attacked. It also shows clients that the service learns from incidents across its whole client base, not only at the client that was hit. The five clients that moved to VPN within a month were then checked in the same way as BrightSmile, with an external scan and a test logon.

### 18.7 Defensive technique names

Recommendations are tagged with D3FEND technique names to keep wording consistent across clients.

D3FEND is published by MITRE as a vocabulary of defensive techniques, so the same control, for example multi-factor authentication, is named identically in every client's list. Consistent names let Copperleaf count how many clients have adopted each control and compare progress without reading every recommendation by hand. The tags are added beside the plain wording, so the office manager still reads "add MFA to the VPN" while Copperleaf's records hold the standard technique name. Mei checks each tag against the published D3FEND list rather than writing it from memory.

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
- **EX054 — Cross-client check.** What did the cross-client check find and achieve? *Rubric:* 3 = 6 exposed; 5 moved to VPN in a month; 1 planned with allow-list; 2 = partial; 1 = vague; 0 = none.

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

Tied to risk means the checks follow the scenarios rather than a fixed list of everything a tool can collect. For BrightSmile, ransomware via remote access drives minute-by-minute rules on logons, accounts and renames, while slower changes such as patch levels are checked daily. The programme is reviewed when the scenarios or the client's systems change.

### 19.2 Frequencies

Rules on logons and file activity run every minute; daily checks cover patch levels and account lists; monthly reports cover inventory and recommendations.

The frequency of each check follows how fast the harm it watches for can happen. On the incident night, three minutes separated the reception logon from the creation of support2, so logon and account rules must run every minute. An overdue patch or a forgotten account stays the same for days, so a daily list catches it without spending compute every minute. Each check's frequency is written on its rule page, so a reviewer can question it against the scenario it serves.

### 19.3 Capacity

Two analysts cover nights for forty clients. Rules that page at night must be precise; lower-value alerts wait for the morning queue.

With two people watching forty clients, one high-severity incident such as BrightSmile's can take one analyst for an hour or more, leaving the other alone with everything else. A night page that turns out to be noise therefore costs real attention. Only rules with a proven record, such as the sequence rule, are allowed to page at night.

### 19.4 Source health

Heartbeat checks show agents that stopped reporting. A missing heartbeat on a server is treated as an alert in its own right.

A server that falls silent may have rebooted, lost its network or had its agent stopped by an attacker, and the SIEM cannot tell those apart from the silence alone. Treating the missing heartbeat as an alert forces someone to find out which it was. The heartbeat lab in chapter 20 shows the states Copperleaf uses: OK, stale and missing.

### 19.5 Coverage

For each client, the share of priority scenarios with tested detections is tracked. BrightSmile's rises from 40% to 80% after the incident work.

BrightSmile has five priority scenarios, so 40% means two had tested detections and 80% means four. The fifth, the scenario without a tested detection, stays visible as a gap in the monthly report. Mei records which scenarios are covered rather than only the percentage, because the same number could hide very different gaps at another client. Coverage counts only detections that were tested on replayed or lab data, so a rule that exists but has never fired in a test does not raise the figure.

### 19.6 Client reporting

Monthly reports show alerts handled, incidents, open recommendations and coverage in plain language.

For the office manager at BrightSmile, plain language means a sentence such as "none of this month's alerts needed your action" rather than rule names and event IDs. Open recommendations appear with their age, so she can see that the offline backup copy, for example, is still waiting for a decision. Coverage is shown as the number of priority scenarios with a tested detection, which the office manager can follow without knowing how the rules work. Incidents are described in a few sentences each, with what Copperleaf did and what the client was asked to do.

### 19.7 Reviewing noise

Each week the team reviews the noisiest rules and tunes or retires them.

Noise is measured by how many alerts a rule produced and how many led to action. The worked example shows the method on the antivirus rule, where nine of ten alerts were installers. Tuning changes the condition so the real cases still fire; retiring is for rules that never produce anything worth an analyst's time. The review also records the change and the date, so if a tuned rule later misses something, the team can trace the miss to that decision.

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

The order follows the path the events travel, so each check rules out one part. If the host is up but the agent is not running, the fault is on the host; if the agent runs but nothing reaches the collectors, the network is suspect. Checking in a fixed order prevents an analyst from reinstalling an agent when the real cause was an expired certificate.

### 20.2 Heartbeats

Agents send a heartbeat every five minutes. Gaps over ten minutes are stale; over an hour, missing.

With a five-minute interval, a ten-minute gap means two heartbeats in a row were missed, which is more than ordinary delay. A gap of over an hour means about twelve heartbeats in a row were missed. The two thresholds separate a brief interruption, such as a clinic's internet blip, from a sustained loss that needs someone to act. Both thresholds appear in the lab code, `gap <= 10` for OK and `gap <= 60` for stale, so the states printed are exactly the rule described here.

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

Mei checks the gaps against the thresholds: 95 minutes is above 60, so CLINIC2-SRV is missing; 18 is above 10 but below 60, so CLINIC3-SRV is stale; and 2, 3 and 4 minutes are all within 10. The order of attention follows from criticality and length of gap, which here both point to CLINIC2-SRV first. Because the lab measures minutes from the current time, the same script run later would print larger gaps for the same hosts.

### 20.4 Failure or tampering

An attacker might stop the agent. Analysts check what happened just before the gap: was there a logon, a service stop, a reboot? A gap right after a suspicious logon is treated as an incident.

The BrightSmile incident makes this question concrete: an attacker with administrator rights on a server can stop the agent before encrypting files. If a missing heartbeat on CLINIC2-SRV had followed a night logon by reception, Mei would have treated it as part of the incident rather than as a maintenance fault.

### 20.5 Fixes

CLINIC2-SRV was rebooted for updates and its agent failed to start because of a corrupted update; CLINIC3-SRV's clinic had a brief internet outage. The agent is reinstalled; the outage resolves itself.

The two causes found here call for quite different actions from Copperleaf. A corrupted agent on CLINIC2-SRV needs the contractor to reinstall it, while the internet outage at clinic 3 needs nothing from Copperleaf except to confirm that buffered events arrive once the link returns. Mei checks that CLINIC3-SRV's heartbeat returns to OK before closing that item.

### 20.6 Recording

Each fix goes into the knowledge base: symptoms, cause, solution.

For CLINIC2-SRV the entry reads, in effect: missing heartbeat after a patch reboot, agent failed to start because of a corrupted update, fixed by reinstalling. The next analyst who sees a missing heartbeat after patching can start from that entry rather than from the beginning of the data path. Entries are short and searchable by symptom, because an analyst at night searches for what they see, not for the cause they have yet to find. After the CLINIC2-SRV fix, the patch system also checks agent health after updates, which the entry records as the prevention step.

### Escalating to engineering

Analysts handle simple cases; problems needing collector or SIEM changes go to Copperleaf's engineer with the diagnosis so far, saving repeated checks.

### Preventing repeats

The patch system now checks agent health after updates.

### Worked example

Before calling the client about CLINIC2-SRV, Mei checks the last events received: an update installation and a reboot request from the patch system at 12:24, a minute before its last heartbeat at 12:25, and nothing suspicious. She records "probable failed agent start after update" and calls the IT contractor, who confirms and reinstalls the agent.

> **Synthetic case.** Hosts and times come from the lab script and invented follow-up.

### Errors and limits

Heartbeats show the agent is alive, not that every event type is being collected.

### Exercises

- **EX058 — Lab states.** Which hosts are missing or stale? *Rubric:* 3 = CLINIC2-SRV missing (95), CLINIC3-SRV stale (18); 2 = one; 1 = wrong; 0 = none.
- **EX059 — Tampering check.** How do analysts tell failure from tampering? *Rubric:* 3 = look at events just before the gap: logon, service stop, reboot; 2 = partial; 1 = assume failure; 0 = none.
- **EX060 — Root causes.** What caused the two problems? *Rubric:* 3 = failed agent start after update; brief internet outage; 2 = one; 1 = vague; 0 = none.

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

Each integration carries an alert to a person who can act on it. Paging reaches the on-call analyst, messages reach the client contacts, and tickets give the contractor a record of the work they are asked to do. On the incident night the SMS integration was the one that failed, which is why the fallbacks below exist.

### 21.2 Escalation per client

Each client profile lists who to contact for which severity and when. BrightSmile: high severity at night — office manager by phone, then IT contractor; medium — email next business day.

Matching contacts to severity avoids two opposite mistakes: waking the office manager for a medium alert that can wait until morning, and emailing her about a high-severity incident she would not see until the next day. The order matters as well, since at night BrightSmile wants the manager called first and the contractor second.

### 21.3 Contractor tickets

When a fix needs the IT contractor, Copperleaf opens a ticket in the contractor's system automatically with the details and links back to the case.

For BrightSmile, the ticket for closing the 3389 forward and setting up the VPN would carry the case link, so the contractor sees the evidence and Copperleaf sees when the work was done. Automatic tickets also remove the step where an analyst retypes the details, which is where host names and times get copied wrongly. The ticket status flows back to the case, so the analyst can close the case only after the contractor marks the work done.

### 21.4 Reliability

If an integration fails — SMS gateway down, contractor ticket rejected — the case system flags the failure and the analyst uses the fallback: phone call.

The fallback matters because the case system can report a failed SMS but cannot make the client read it. A phone call either reaches someone or tells the analyst immediately that it did not, which is exactly the information needed to move on to the next contact on the list. The analyst records the fallback call in the case, with the time and who answered, so the failure and its workaround are both visible later.

### 21.5 Message content

Automated messages are short, plain and never include sensitive data such as patient names; details stay in the secure portal.

An SMS can be read on a lock screen or by a family member, so a message about BrightSmile would say that a high-severity alert needs a call, not which patient records were on the server. The office manager then logs in to the portal or takes the analyst's call to hear the details. The same rule applies to email, which can be forwarded or read on shared clinic PCs where other staff may see it.

### 21.6 Testing

Integrations are tested monthly with a test alert routed to a test contact.

The test alert travels the same path as a real one, through paging, SMS and email, but goes to a contact set up for testing so no client is disturbed. A failed test then shows the broken link during working hours, when fixing it is easy, rather than at night during an incident. Each test result is recorded with the date, so a failed integration can be traced to the month in which it stopped working.

### 21.7 Case

During the BrightSmile incident, the automatic SMS to the office manager failed because her number had changed.

The failure was not technical: the gateway sent the message, but to an old number that the client had never updated. Monthly integration tests would not have caught it, because they use a test contact rather than the client's own details. That gap is what the quarterly contact confirmation in the worked example closes. The night analyst recorded the failed SMS in the case at the time, which later made the cause easy to identify during the review.

### Language and tone

Night calls to clients start with what is happening and what Copperleaf has done, then what the client needs to decide. Analysts practise a short script so they stay calm and clear even when the client is alarmed or half asleep, and they always confirm the next contact time before ending the call.

### Worked example

The night analyst called the backup contact (the IT contractor), who reached the office manager. Afterwards, Copperleaf adds a quarterly contact confirmation step to every client's review and records the failed SMS as an integration issue.

> **Synthetic case.** Integrations and events are invented.

### Errors and limits

Integrations depend on details clients forget to update; verify them regularly.

### Exercises

- **EX061 — Escalation profile.** Describe BrightSmile's escalation for high severity at night. *Rubric:* 3 = office manager by phone, then IT contractor; 2 = partial; 1 = email; 0 = none.
- **EX062 — Message safety.** What must automated messages avoid? *Rubric:* 3 = sensitive data like patient names; details in portal; 2 = partial; 1 = nothing; 0 = none.
- **EX063 — SMS failure.** Why did the SMS fail and what changed? *Rubric:* 3 = number changed; quarterly contact confirmation added; 2 = partial; 1 = vague; 0 = none.

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

Enriching alerts and opening tickets follow fixed steps that a script does the same way each time. Isolating on a spike is also fixed once the conditions are agreed. Deciding whether a contractor's late logon is legitimate needs context a script does not have, such as a phone call, so it stays with an analyst. Each automated step is listed on a page with its trigger and its limits, so analysts know exactly what the system will do without them.

### 22.2 Automated containment

After BrightSmile, Copperleaf automates isolation for rename spikes on clinic servers and PCs, for clients whose agreements allow it, so containment does not wait for an analyst.

The reason is the timing on the incident night: the spike began at 01:34 and isolation came at 01:36, and 985 files were renamed over those minutes. Automated isolation acts in the minute the spike is detected, which removes the time an analyst needs to read the alert, check the client and reach Raj for approval.

### 22.3 Guard rails

Automation can go wrong at scale: a bad rule could isolate every PC in a clinic. A guard limits automatic isolation to two hosts per client per hour; beyond that, the on-call analyst is paged.

The limit is a trade-off: a real outbreak could affect more than two hosts in an hour, but then a person should be deciding anyway. Paging the on-call analyst at that point means a faulty rule cannot cut a whole clinic off its server and PCs, while a real outbreak still gets a quick human decision.

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

The guard counts per client, which is why OAK-PC4 at Oakfield Law is isolated even though BrightSmile has already reached its limit. A global limit would have let one client's outbreak use up the automation for every other client. Mei checks the printout against the code: two isolations, one page, then one isolation for the second client.

### 22.5 Testing

Automation is tested in the lab with synthetic alerts, then enabled in monitor mode (logging what it would do) for two weeks before acting.

Monitor mode shows what the automation would have done on real alerts without acting on them. Two weeks gives time for routine events such as software updates to appear. The worked example shows the value: the X-ray update would have caused one wrong isolation, and it was found before any clinic PC was cut off. Only after monitor mode shows no unexplained actions is the automation switched to act, and the switch date is recorded on the rule page.

### 22.6 Review

Every automated action is reviewed the next morning; wrong actions lead to rule or guard changes.

The review asks two questions for each action: was the host really in trouble, and did isolation help. A wrong isolation leads to a change, such as the exclusion for the X-ray vendor's signed update process. Each change is recorded so the next review can check whether it worked. The reviewer also checks automated actions that were correct, because a correct isolation still needs the client informed and the host later released. A host left isolated after the threat is cleared stops a clinic working just as surely as the attack would have.

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
- **EX066 — Monitor-mode finding.** What did monitor mode reveal and how was it fixed? *Rubric:* 3 = X-ray update renames would isolate; exclude signed vendor update process; 2 = partial; 1 = vague; 0 = none.

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

BrightSmile alone shows how clients change: new personal accounts, a VPN, a new card terminal and a dentist's laptop, all within a few months. Each change can make a rule noisier or blind, for instance when the reception account no longer exists for the out-of-hours rule to watch. Monthly evaluation catches such drift before it shows up as a missed incident.

### 23.2 Measures

From closed cases, each alert is a true positive (real issue) or false positive. Missed detections (false negatives) come from incidents found other ways, such as client reports. Precision is TP ÷ (TP + FP); recall is TP ÷ (TP + FN).

The two measures answer different questions about the same rule. Precision asks how much of an analyst's time on a rule's alerts was well spent; recall asks how many real problems the rule caught. A rule can score well on one and badly on the other, and the AV-disabled rule shows the worst case, with both low.

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

Mei verifies the rates by hand: 12 of 15 brute-force alerts were real, giving 0.80; 4 of 10 new-admin alerts, giving 0.40; 2 of 3 rename alerts, giving 0.67; and 1 of 10 AV alerts, giving 0.10. For AV-disabled, one caught and one missed real case gives recall of 1 out of 2, which is 0.50. The brute-force rule is both precise and complete this month, so it needs no change and serves as the model for the others.

### 23.4 Actions

AV-disabled is redesigned (the ten-minute change from chapter 19, plus a check for tamper-protection events). New local admin gets the contractor-window exception from chapter 16.

Each action targets the cause found in the closed cases. Nine of the ten AV alerts were installers briefly pausing protection, so requiring ten minutes removes them, while the tamper-protection check aims at the missed case. For the new-admin rule, legitimate contractor work explains much of the noise, so the support-window exception addresses that directly. Each action has an owner in Mei's table, and next month's evaluation shows whether the changed rules actually improved.

### 23.5 Small numbers

A rule with three alerts a month gives unstable percentages; Mei reports counts beside rates.

The rename-spike rule shows why: two real alerts and one false give 0.67, but one more false alarm next month would drop it to 0.50 with nothing really changed. Printing "2 of 3" beside the rate lets Raj see that the change rests on a single alert, so he does not redesign a rule because of chance. Counts also show volume, which rates hide: a rule with 15 alerts and one with 3 can share a rate while costing analysts very different amounts of time.

### 23.6 Missed detections

The missed AV case was found by the client noticing pop-ups; the evaluation asks why the rule did not fire — the event type had changed after an antivirus update.

The cause was outside the rule itself: an antivirus update renamed the event the rule was looking for, so the rule kept running and kept matching nothing. Mei proposes a check that each rule's source event still arrives, similar to the data-gap monitoring of chapter 12, so a renamed event shows up as a drop instead of as silence.

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

Mei keeps the question narrow on purpose so that it can be answered. It names one intervention, the 15-minute briefing, one outcome, reports of suspicious emails, and one comparison, briefed against unbriefed clients. A broader question such as whether briefings make clients safer would have no single measure that Mei could count from Copperleaf's data. Mei writes the question down before looking at any data, so the comparison cannot be reshaped afterwards to fit an interesting result.

### 24.2 Data

Copperleaf briefed twelve clients last year as part of onboarding; eighteen others were not briefed. The phishing report mailbox records reports by client.

Thirty clients in total, twelve briefed and eighteen not, is the sample the data allow. The groups were not chosen by Mei: briefing began as part of onboarding, which is why the newer clients are the briefed ones. The phishing report mailbox already tags each report with its client, so no new data collection was needed. Mei also notes that the mailbox only counts emails people chose to report, so it says nothing about suspicious emails nobody noticed.

### 24.3 Measure

Reports per 100 staff per quarter, so client sizes are comparable.

A client with sixty staff will send more reports than one with ten, even if each person behaves the same. Dividing by staff numbers and fixing the period to one quarter puts a small clinic and a larger firm on the same scale. Mei takes staff numbers from the client profiles, which list them for licensing. A quarter is long enough to smooth out a single busy week, yet short enough to compare with the follow-up Mei proposes for next quarter. The measure is written down before the comparison is run, together with how staff numbers are counted.

### 24.4 Comparison

Briefed clients averaged 4.1 reports per 100 staff per quarter; others 1.6. The difference is large, but the groups were not randomly chosen: briefed clients joined more recently and may differ in other ways.

The ratio is 4.1 divided by 1.6, about 2.6, which Mei rounds rather than quoting more decimals than the data justify. Because newer clients may have newer email systems or staff more used to reporting, the difference may come partly or wholly from those other features rather than from the briefing itself.

### 24.5 Ethics

Data are aggregated per client; no individual staff are identified. Clients agreed to anonymised use in Copperleaf's improvement work.

Working with counts per client rather than per person means no analyst sees which receptionist did or did not report an email. That matters at small clients, where a single report could otherwise point to one named person. The agreement with clients covers use in improvement work only, not publication outside Copperleaf. The ethics note goes into Mei's write-up, so readers know how the data were handled before they see any figure.

### 24.6 Limits

Confounding by joining date and client type; small numbers; reports are not the same as resisting phishing.

Each limit points to a specific weakness in what the comparison can show. Joining date and client type could explain the gap without any effect of the briefing; twelve and eighteen clients are too few for stable averages; and a report shows that someone noticed an email, not that others in the same business did not click it. Mei lists these limits in the summary for Raj, beside the figures rather than in a footnote that a busy reader would skip.

### 24.7 Next step

Mei proposes briefing six of the unbriefed clients next quarter, chosen by lot, and comparing with the other twelve unbriefed — a fairer test.

Choosing by lot means Mei cannot, even unintentionally, pick the clients most likely to report anyway. The six briefed and twelve unbriefed clients would then differ mainly in whether they received the briefing, so a difference next quarter would be easier to attribute to it, though six clients is still a small group. The proposal keeps the same measure, reports per 100 staff per quarter, so the follow-up result can be compared directly with this one.

### Literature

Mei reads Alahmadi et al. (2022) on how analysts experience alarms and notes that user reports are a form of human sensor. She also reads Sundaramurthy et al. (2014), whose researchers worked inside SOCs to understand practice, which encourages her to talk to client contacts about why they report or do not, rather than relying on numbers alone.

### Presenting

Mei presents the result to Copperleaf's team with a chart of rates per client group, the caveats and the proposed follow-up, in ten minutes.

### Worked example

Mei's summary: "Briefed clients reported about 2.6 times as many suspicious emails per 100 staff, but briefed clients differ in joining date and type. A small randomised follow-up is proposed." Raj approves the follow-up.

> **Synthetic case.** Figures are invented.

### Errors and limits

Observational comparisons suggest; randomised comparisons test.

### Exercises

- **EX070 — Comparable measure.** Why use reports per 100 staff per quarter? *Rubric:* 3 = clients differ in size; rate comparable; 2 = partial; 1 = simpler; 0 = none.
- **EX071 — Confounding.** Why can the 4.1 vs 1.6 difference not be credited to briefings alone? *Rubric:* 3 = groups not random; joining date and type differ; 2 = partial; 1 = it can; 0 = none.
- **EX072 — Fairer test.** What follow-up did Mei propose? *Rubric:* 3 = brief 6 unbriefed chosen by lot, compare with other 12; 2 = partial; 1 = vague; 0 = none.

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

Two weeks is a target the team must justify step by step, because onboarding has many dependencies on the client. "Monitored and verified" means more than agents installed; it means every data flow on the diagram has been shown to deliver test events, as Mei did when she found the misdirected firewall syslog in chapter 12. The brief also asks for evidence that each step happened, which is where Mei's verification work becomes central to the team's design.

### 25.2 Mei's team

Mei, a networking student and a programming student divide the work: data flows and verification (Mei), firewall and VPN checks (networking), and automation of the onboarding checklist (programming).

The split follows each student's training, and each part touches the others: Mei's verification needs the networking student's firewall checks, and the programming student's checklist records both. Mei takes data flows because she has already found a real fault in one, and verification is where most onboarding problems appear. Each student owns one part but reviews the others, so a misunderstanding about how the parts connect is caught before the pilot.

### 25.3 Design

Day 1–2: agreement and contacts; day 3–5: agents and syslog; day 6–8: verification with test events per data flow; day 9–10: baseline collection; day 11–14: rule enablement and first report.

The order of the blocks follows the dependencies between the onboarding steps. Contacts and an agreement come first because nothing may be installed without them; verification comes before baselines because a baseline from a broken feed would be wrong; and rules are enabled last because they need both the data and the baseline. Each block of days also has a named owner within the team of three. Days 6 to 8 are Mei's verification block, which gives three days to find and fix faults like the misdirected syslog before baselines start.

### 25.4 Critique

Raj and a client account manager critique the design. The account manager notes clients rarely respond within a day; the team adds a reminder step and a "waiting on client" status so delays are visible.

The critique changed the plan rather than only the slides. A day's wait on the client at each of several steps could stretch two weeks to three. With the reminder step and the new status, the account manager sees which client step is overdue and can chase it, and the team's own work is not blamed for the delay.

### 25.5 Integration

The automated checklist marks each step done only when evidence is attached, such as a screenshot of test events arriving.

Requiring evidence closes the gap between "configured" and "working" that caused the missing firewall logs in chapter 12. A step marked done without a screenshot or a SIEM search result simply stays open, so the checklist cannot report a client as monitored while one of its feeds is still pointing to an old address. The evidence attached at each step also becomes part of the client's record, so later analysts can see when each feed was first verified.

### 25.6 Teamwork

Weekly stand-ups and a shared board keep the three parts aligned.

Stand-ups surfaced the dependency problems early, for instance when the checklist needed a field for evidence from the networking student's VPN checks that had not been planned. A shared board showed each part's open items, so the three students could see when one part was blocking another rather than discovering it at integration. The board also held the waiting-on-client items, so the team could see which delays came from the client and which from their own work. Each stand-up ended with a named person for every blocked item, which kept small problems from waiting a week.

### 25.7 Presentation

The final presentation shows the two-week plan, evidence requirements and the dashboard.

The audience is Raj and the account manager, so the presentation leads with the plan a client would follow and the evidence each step produces. The dashboard shows how a client's onboarding status would appear, including the waiting-on-client status added after the critique, which addresses the account manager's main concern. The team also shows the pilot plan with the veterinary practice, so the audience can judge the design against a real client rather than a slide. Questions from Raj and the account manager focus on the waiting-on-client status and on how the checklist proves each data flow.

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

For the sequence rule, Mei knows why it joins three events on one session and why contractor sessions in support windows are excluded. An analyst meeting the alert at night does not, unless the handoff passes that knowledge on. Handoff is finished when another analyst can handle the alert correctly without calling Mei. Mei treats the questions analysts ask during handoff as evidence of what the runbook still fails to explain.

### 26.2 Runbooks

Each alert type gets a runbook: what the alert means, what to check first, decision points, actions allowed per client agreement, and how to close. Mei writes the runbook for the sequence rule from chapter 16.

For the sequence rule, the runbook starts by explaining that the alert means an external session created an account and made it an administrator within 30 minutes. It then asks the analyst to check whether the session came from the contractor's VPN inside a support window, and states the actions each client's agreement allows, such as isolating the host or disabling the account.

### 26.3 Training

A 20-minute session walks analysts through the runbook using the BrightSmile replay. Each analyst then triages two lab alerts alone.

The BrightSmile replay is a good training case because analysts know how it ended: support2 created at 01:22 and renames starting at 01:34. Seeing the sequence alert at 01:22 shows them how much time the rule gives. Triaging two lab alerts alone then checks that they can apply the runbook without help. Short sessions fit the shift pattern, so analysts can attend between shifts without leaving the night queue short of people.

### 26.4 Confirming understanding

Mei checks that analysts reach the right decisions in the lab. One analyst isolates on a contractor-window alert that should have been a phone call; the runbook is clarified.

The mistake came from the runbook, not the analyst: it listed isolation among the actions but did not say that an alert from the contractor's account outside a support window should first lead to a call to the contractor. Mei adds that step, because isolating a server during an agreed emergency repair would stop the repair.

### 26.5 Ownership

The rule has an owner (Mei during placement, then a named engineer), a review date and a feedback channel.

Naming a person rather than a team means someone is responsible for answering analysts' questions and for the review date. When Mei's placement ends, the named engineer takes over the rule with its runbook and change history. The review date ensures the contractor exceptions are checked before they expire. The feedback channel collects analysts' comments in one place, which is how the two wording changes during the first fortnight were found.

### 26.6 Go-live

The rule goes live on a Monday morning, not before a weekend, so problems are found while staff are available.

A Monday start gives a full working week, with Mei and the engineers present, to see the rule's first real alerts. If it misfired on a Friday night, two analysts covering forty clients would have to deal with it alone until Monday, the situation that the night-capacity limits of chapter 19 are meant to avoid. Mei also tells the night analysts that the rule is new, so an unusual alert in the first week is reported to her rather than quietly closed.

### 26.7 Feedback

Analysts' comments in the first two weeks lead to two wording changes in the alert text.

The feedback came from analysts handling real alerts, who found that two phrases in the alert text were unclear at a glance. Small changes like these matter because the alert text is the first thing read at night. Mei records both changes in the rule's history so later readers can see why the wording differs from the first version. Mei also checks the three firings in the worked example against the runbook, to see whether analysts followed it.

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

Three pilot clients are enough to show whether a rule floods the queue or throws errors in real data, without exposing all forty clients to a fault at once. For the sequence rule, an expected volume is a handful of alerts a month per client; a pilot client producing dozens a day would stop the rollout until the cause was found.

### 27.2 Validation

Validation asks whether rules catch the behaviour they target in each client's real environment. Copperleaf runs authorised test actions on each client's systems with a test account: create a local account and add it to Administrators, then remove it.

The test account steps are the second and third parts of the BrightSmile sequence without any of the harm: an account is created, made an administrator and then removed. If the rule fires, Copperleaf knows that this client's servers log the needed events and that they reach the SIEM. If it does not fire, something on that path is broken.

### 27.3 Authorisation

Tests are listed in the service agreement and scheduled with the client contact. They never touch real data.

Listing the tests in the agreement means the client has already agreed in writing to the kind of action, and scheduling means the contact knows when it will happen. A test account that appeared unannounced on a clinic server would look exactly like support2, and could start a real incident response at the client. The client contact also receives the test account name in advance, so their own staff can recognise it if they notice it.

### 27.4 Evidence

Each client's validation record shows test time, expected alert, actual alert time and analyst who confirmed.

The difference between expected and actual alert time also shows delay. If the account change happened at 12:00 and the alert arrived at 12:02, the record shows a two-minute path from the client's server to the analyst. Naming the analyst who confirmed means the record can be checked later by asking the person involved. Together the records for all forty clients form the evidence behind the statement that the sequence scenario's coverage is verified rather than assumed.

### 27.5 Failures

At four clients the sequence rule did not fire. At three, account-management auditing was disabled; at one, the agent was an old version.

Both causes are of the kind chapter 6 warned about: events appear only if auditing enables them, and an agent must be able to forward them. Neither failure showed up in normal operation, because without the test there was simply no alert, and a missing alert looks exactly like a quiet day. Mei records which clients failed and why, so the fixes can be tracked and the same causes checked at future onboardings.

### 27.6 Fixes and retest

Auditing is enabled and the agent upgraded; retests pass.

The retest repeats the same account test, so a pass shows the fix worked rather than assuming it. For the three clients with auditing disabled, Mei also asks how the onboarding step for audit policy was missed, since a skipped checklist step was the cause at BrightSmile's clinic 2. The upgraded agent at the fourth client is also added to the tool-health list, so its version is watched after future updates. Each retest result is added to the client's validation record beside the failed first attempt, keeping both visible.

### 27.7 Exceptions

One client's vendor-managed system cannot have auditing enabled; the gap is recorded and the client informed.

Recording the gap means the client's coverage report shows that this system is not covered by the sequence rule, rather than implying it is. The client can then decide whether to ask the vendor for another way to log account changes, or accept the gap knowing what it means. The exception is reviewed at the client's next review, in case the vendor later offers a way to enable auditing on that system. Mei writes the reason for the exception in plain terms, naming the vendor restriction, so a later analyst does not try to enable auditing and breach the vendor's terms.

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

Rotating shifts lets Mei see how the work differs across the day: daytime brings client calls and onboarding, evenings bring alerts after clinics close. Supervision by Raj continues the arrangement from chapter 10, where her decisions are checked before they reach a client, but over eight weeks the checks become lighter as she shows reliable judgement. Evening shifts also give her experience of the hours when clinics are closed and suspicious activity stands out most clearly.

### 28.2 Conduct

She signs confidentiality terms, never discusses clients outside work and uses client data only in Copperleaf's systems.

These terms matter more at a provider that sees forty clients' data. A remark about one dental client's incident in the wrong place could identify the business and its patients. Keeping client data inside Copperleaf's systems also means her placement journal describes cases without copying logs or names out of those systems. She also signs the same access terms as permanent staff, including MFA on her SIEM and case-system accounts.

### 28.3 Daily work

Triage of medium alerts, drafting client advice for review, onboarding checks and the weekly noise review.

Medium alerts are the right level for a trainee: they need real triage but rarely need containment at night. Drafting advice for review builds on her work since chapter 10, and onboarding checks and the noise review use the verification and evaluation skills from chapters 12 and 23 in daily practice rather than as exercises. Each kind of task is reviewed by Raj at first, and the review becomes lighter as her drafts and decisions need fewer corrections.

### 28.4 Client contact

By week four, Mei makes routine client calls herself, with Raj listening in for the first few.

Raj listening in lets him correct tone and content while the call is still a learning exercise. Routine calls include confirming a new device or asking about an account change. Mei's worked example from week six shows why practice matters: the office manager's defensive reaction needed calm wording that is easier to learn on routine calls. After each early call Raj gives brief feedback, usually on wording, which Mei then records in her journal for the week.

### 28.5 Mistakes

In week three, Mei closes an alert as benign without checking the client's business hours; Raj spots it in review. The alert was benign, but the check was required. She adds it to her personal checklist.

Raj's lesson in this case was about the method, not about the outcome. Business hours are the context that decides whether an action at a given time is suspicious, as the BrightSmile enrichment line "clinic closed" showed. Closing without checking them was right by luck, and the personal checklist makes the check a habit rather than a memory.

### 28.6 Journal

A weekly journal records cases, decisions, mistakes and lessons; her polytechnic tutor reviews it.

The journal gives the tutor evidence of learning that Raj's evaluation alone would not show, such as how Mei reasoned about a decision. Recording mistakes alongside successes, as with the week-three business-hours slip, lets both the tutor and Mei see whether a lesson was actually applied later. Entries are short and dated, so the tutor can follow her progress week by week without reading long reports. Mei describes each case by type and decision, keeping client names and logs out of the journal as her confidentiality terms require.

### 28.7 Evaluation

Raj's evaluation covers technical skill, judgement, communication and reliability.

Each criterion links to things Raj saw during the placement. Technical skill shows in triage and onboarding checks, judgement in decisions such as when to call a client, communication in her calls and drafts, and reliability in handover notes and promised calls kept. The evaluation and the journal together go to her polytechnic. Raj bases each judgement on specific cases from the placement, so Mei and her tutor can see the evidence behind every comment. Mei's handover notes, with promised calls at the top, are among the evidence for the reliability criterion.

### Shift handover

At every shift change Mei writes a handover note: open cases, client calls promised, alerts being watched and anything unusual. The incoming analyst reads it and asks questions before Mei leaves. Raj points out that the most common failure in managed SOCs is a promise to call a client back that gets lost at handover, so Mei puts promised calls at the top of every note, with the time and the client contact's name. In week five, an evening analyst thanks her because a client called asking for an update and the note told him exactly what had been promised. Good handovers make the service continuous even though people change every eight hours.

### Worked example

Mei's journal, week six: "Called a dental client at 19:40 about a new admin account. The office manager was defensive, thinking we suspected her. I explained it was a routine check of any new admin. She confirmed she had created it for a locum dentist. Lesson: say 'routine check' first."

> **Synthetic case.** The placement is invented.

### Errors and limits

Placements vary by host; tutors ensure learning goals are met.

### Exercises

- **EX082 — Daily work.** List three daily tasks Mei performed. *Rubric:* 3 = triage, drafting advice, onboarding checks, noise review (three); 2 = two; 1 = one; 0 = none.
- **EX083 — Week-three mistake.** What was Mei's mistake and her response? *Rubric:* 3 = closed without checking business hours; added to checklist; 2 = partial; 1 = vague; 0 = none.
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

Each component of the package answers one step of the BrightSmile incident. The sequence rule catches the account creation that took place at 01:22, the rename-spike rule with isolation stops encryption like that which started at 01:34, heartbeat gaps catch an attacker or fault silencing a server, and the coverage report shows each client what is protected.

### 29.2 Requirements

Detect the BrightSmile sequence within 5 minutes of the admin-group change; isolate on rename spikes within 2 minutes; page on server heartbeat gaps over 15 minutes at night; no more than one false page per client per month.

The requirements are written as numbers so they can be tested. Five minutes for the sequence alert leaves room within the 15-minute acknowledgement target; two minutes for isolation matches the fastest trainees in the chapter 15 lab; 15 minutes for heartbeat pages separates a reboot from a real loss; and the false-page limit protects the two night analysts.

### 29.3 Building

Rules are written in the SIEM, automation in Copperleaf's playbook tool, reports from SIEM queries. Everything is stored in version control with change notes.

Using Copperleaf's existing tools means the package can be maintained by the team after Mei leaves rather than needing a new system. Version control with change notes gives the history that the runbooks and the evaluation rely on, so anyone can see which version of a rule was running when a given alert fired. Each change note links to its lab test, so a reviewer can check that a rule was tested in the form it was deployed.

### 29.4 Testing

Each component is tested in the lab with synthetic events: the BrightSmile replay, the rename spike and a stopped agent.

Each of these tests uses a scenario whose correct answer is known in advance. The BrightSmile replay should produce a sequence alert after the admin-group change, the rename spike should trigger isolation, and a stopped agent should produce a heartbeat page. Synthetic events keep the tests safe, and known answers make a failure obvious, as the heartbeat test showed. Mei writes the expected result of each test before running it, as she did with her first parser in chapter 3.

### 29.5 Guard rails

The isolation guard from chapter 22 is reused; heartbeat paging respects client maintenance windows.

Reusing the guard means the limit of two automatic isolations per client per hour, tested in chapter 22, applies here too. Respecting maintenance windows stops the heartbeat rule paging when a contractor reboots a server on schedule, which would otherwise break the requirement of no more than one false page per client per month. Maintenance windows are taken from each client's profile, so an undocumented window can still cause a false page, as the assessment later found.

### 29.6 Documentation

Runbooks for each alert, a client-facing summary and an owner list.

Each runbook follows the pattern from chapter 26, so analysts meet familiar steps for the new alerts. The client-facing summary tells an office manager in plain language what the package watches and what Copperleaf may do automatically, and the owner list names who maintains each rule after Mei's placement ends. The documentation is stored in version control with the rules, so a change to a rule and its runbook are reviewed together. Each runbook names the requirement its alert serves, which lets an analyst see at night why the alert matters and how quickly it must be handled.

### 29.7 Peer review

A senior analyst reviews logic and runbooks before deployment.

The senior analyst checks that each rule's logic matches its requirement and that the runbooks give clear decisions at night. A reviewer who did not build the package is more likely to see an unstated assumption, such as a maintenance window that is not documented for every client, which later caused one false page. Review comments and Mei's responses are kept with the change notes, so the reasoning behind each design choice remains available to the future owner. The reviewer also checks that every requirement has a test, so nothing in the package goes live untested.

### Version control and change notes

Every rule and playbook in the package is stored with a change note that explains what changed, why, who reviewed it and how it was tested. If an alert misbehaves after go-live, the team can see exactly which change caused it and roll it back to the previous version within minutes. Mei tags the first deployable set as version 1.0 so later comparisons have a clear baseline, and links each tag to its test results in the lab.

### Worked example

Lab tests: sequence alert in 2 minutes after the admin-group event; isolation 70 seconds after spike detection; heartbeat page 16 minutes after the agent stopped — one minute over the target because the check runs every five minutes. Mei changes the check interval to two minutes and retests: 13 minutes.

> **Synthetic case.** The build and test results are invented.

### Errors and limits

Lab timings exclude real-world delays such as slow client links.

### Exercises

- **EX085 — Package parts.** List the four parts of the package. *Rubric:* 3 = sequence rule, rename spike with isolation, heartbeat gaps, coverage report; 2 = three; 1 = one; 0 = none.
- **EX086 — Requirements.** State two requirements of the package. *Rubric:* 3 = e.g. sequence within 5 min; isolate within 2 min; heartbeat page >15 min; ≤1 false page/month (two); 2 = one; 1 = vague; 0 = none.
- **EX087 — Heartbeat fix.** Why did the heartbeat test miss its target and what fixed it? *Rubric:* 3 = 5-min check interval; changed to 2 min; 13 min; 2 = partial; 1 = vague; 0 = none.

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

Each kind of evidence in the plan covers something that the others cannot. Lab results show the components work on known events, client tests show that each client's systems produce and deliver the events, and a month of live operation shows how often the package pages without a real attack. Twelve healthcare clients are the population the package was built for.

### 30.2 Client validation

With agreement from each client, Copperleaf runs the account test (chapter 27) and a stopped-agent test during maintenance windows. Rename spikes are tested only in the lab, since generating them on client systems would disrupt work.

The account test and stopped-agent test are both harmless and reversible, so they can run on live systems with the client's agreement. A rename spike cannot be produced without changing hundreds of real files, which is why that test stays in the lab, the trade-off Mei later explains to an assessor in the worked example.

### 30.3 Results

Sequence alerts arrived in 1–4 minutes at all twelve clients. Heartbeat pages arrived in 11–14 minutes. In live operation, false pages averaged 0.4 per client per month. Rename isolation is verified in the lab only.

Mei sets each of these figures against the requirement it is meant to meet. One to four minutes is within the five-minute target for sequence alerts, 11 to 14 minutes is within the 15-minute target for heartbeat pages, and 0.4 false pages per client per month is within the limit of one. Only rename isolation has no live figure, and Mei says so.

### 30.4 Live event

One real event occurred: a clinic PC's new admin account at night, caught by the sequence rule and contained before any file activity. The account belonged to an attacker using a phished contractor password.

This event matches the supplier scenario from chapter 13: an attacker using the contractor's stolen password. The sequence rule's contractor exception did not hide it, because the exception applies only inside agreed support windows from the contractor's VPN addresses, and this logon was at night. Containment before any file activity is what the sequence rule was built to achieve.

### 30.5 Reflection

What worked: reusing tested components, staged deployment. What did not: the first heartbeat interval; one client's maintenance window was undocumented, causing a false page.

Both failures were found by the evaluation process rather than by clients. The five-minute heartbeat interval missed the 15-minute target by one minute in the lab and was shortened to two minutes, and the false page from an undocumented maintenance window points to recording every client's maintenance windows before go-live. Mei records both points in her report, so the future owner knows the heartbeat interval was changed and why.

### 30.6 Presentation

Mei presents to Copperleaf's team and her assessors: requirements, evidence, the live event, limits and maintenance plan.

Mei's presentation follows the order of the assessment criteria, so assessors can match each part to what they grade. The live event shows the package working on a real attack, and the limits, such as rename isolation verified only in the lab, are stated by Mei before anyone has to ask. The presentation uses the same requirement table as the report, so figures quoted aloud can be checked against the written evidence.

### 30.7 Handover

The package passes to a named engineer with a review date.

The handover repeats the ownership pattern from chapter 26: a named engineer, a review date and the runbooks with their change history. When Mei's placement ends, the package keeps working because its owner has the requirements, test records and version 1.0 tag needed to maintain it and judge future changes against. The engineer receives the package in version control with its 1.0 tag, the validation records from client tests and the month of live results. The review date is set so the first review falls after another period of live operation, when new figures can be compared with the assessed month.

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
- **EX089 — Live event.** Describe the live event caught. *Rubric:* 3 = night admin account by phished contractor password; contained before files; 2 = partial; 1 = vague; 0 = none.
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
