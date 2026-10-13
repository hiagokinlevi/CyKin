# OT, IoT and Cyber-Physical Security: A Technologist's Practice Book

- Language: English (`en`); technologist course, three years; approximately 2,400 hours of planned study.
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologists who will install, operate, monitor and improve the security of OT and IoT systems at real sites.
- Relation to neighbouring books: the [technical course book](../../../../technical-18-months/ot-iot-security/en/book/MANUSCRIPT.md) is shorter and more procedural; the [bachelor's book](../../../../bachelors-4-years/ot-iot-security/en/book/MANUSCRIPT.md) adds theory and research. **This book is implementation-focused.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. No authority to access real sites. All sites, people and numbers in examples are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–9 build computing, networking, scripting and evidence foundations; 10–23 are the OT/IoT core with the guided lab in Chapter 15; 24–30 cover research, a team studio, handoff, deployment, field practice and the capstone. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, three exercises scored 0–3, a synthesis and a **Continue studying** block. Labs read local data only (`python3 file.py`).

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Northgate Cold Storage (NCS)** — ammonia refrigeration controllers PLC-R1/PLC-R2, HMI-C, historian HIST, wireless temperature loggers via GW-LOG to a vendor cloud, dock cameras | Site studied throughout | Invented |
| **Priya Nair** | Technologist trainee at NCS | Invented |

### Core sources

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final); [ISA/IEC 62443 series](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards); NIST [IR 8259](https://csrc.nist.gov/pubs/ir/8259/final); [ETSI EN 303 645 V2.1.1](https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf); MITRE [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/); CISA [AA21-042A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes

You will (1) name the computing devices in a cold-storage warehouse and what each one does; (2) separate embedded controllers from general-purpose computers; (3) explain why uptime expectations differ; and (4) start the asset notebook used through the whole course.

### 1.1 Many computers, few of them obvious

The synthetic Northgate Cold Storage (NCS) warehouse keeps frozen food at −22 °C and chilled goods at 2–4 °C. Its obvious computers are the office PCs. Less obvious are two refrigeration controllers (PLC-R1 and PLC-R2) that run the ammonia compressors, an operator screen (HMI-C), a historian (HIST), forty wireless temperature loggers that report through a gateway (GW-LOG) to a cloud service, and IP cameras on the loading dock. A technologist's first job is to see all of them.

Priya's first notebook row, for GW-LOG, already shows why: if it stops, cooling continues but the temperature record has a gap.

### 1.2 Embedded versus general-purpose

A PLC runs one control program in a fixed loop and may stay powered for a decade. A Windows HMI runs many processes, receives updates and can be infected by ordinary malware. Loggers are microcontrollers with radio and a battery; they cannot run antivirus at all. Each class needs a different protection approach, which is why NIST SP 800-82r3 discusses OT device types separately.

Priya's notebook records the class in its type column, and the three classes lead to three plans. PLC-R1 and PLC-R2 are protected by controlling who can reach them, because they cannot run security software. HMI-C is hardened like a Windows host within the vendor's certified build. The forty loggers depend entirely on the vendor's firmware and on the gateway in front of them.

### 1.3 Availability first

If an office PC reboots, someone loses ten minutes. If PLC-R1 stops, compressor suction pressure drifts and the freezer warms by roughly a degree every 15–20 minutes; after a few hours stock worth hundreds of thousands may be condemned. That consequence shapes every later decision: when to patch, how to test, who must be present.

At NCS this is why a firmware fix for PLC-R1 waits for a maintenance window with the refrigeration contractor present, and why Priya's later firewall change in Chapter 27 has a two-minute rehearsed rollback: a missing flow that blinds HMI-C for an hour matters more than the change itself.

### Worked example (synthetic NCS)

Priya Nair, a technologist trainee, builds her asset notebook: device, type (embedded or general-purpose), function, location, who changes it, what happens if it stops. Her row for GW-LOG reads: "embedded gateway; forwards logger readings to the cloud; comms room; vendor updates it remotely; if it stops, temperature records have a gap and food-safety evidence is lost, but cooling continues."

> **Synthetic case — Northgate Cold Storage.** NCS, Priya Nair and all device names are invented for teaching.

### Errors and limits

Do not assume "air-gapped" without checking for cellular modems or vendor laptops. Warming rates depend on door openings and load; use the plant's own data before quoting one.

### Exercises

- **EX001 — Embedded or general-purpose?** Classify HMI-C, PLC-R2 and a temperature logger, giving one reason each. *Rubric:* 3 = general-purpose, embedded, embedded with reasons; 2 = classes right, weak reasons; 1 = one right; 0 = none.
- **EX002 — Consequence of a stopped gateway.** State what NCS loses if GW-LOG fails for six hours and what it does not lose. *Rubric:* 3 = loses temperature records/alerts, cooling continues; 2 = one side; 1 = says freezers stop; 0 = none.
- **EX003 — Notebook row for PLC-R1.** Write the six-column asset-notebook row for PLC-R1. *Rubric:* 3 = all six columns plausible; 2 = four or five; 1 = name only; 0 = none.

### Synthesis

Seeing every computer in a facility — and knowing what each one's failure costs — is the foundation of OT security work.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) read an IP address plan and identify subnets; (2) explain what a VLAN and a firewall rule do; (3) trace how a cloud-connected logger reaches the internet; and (4) recognise the services a facility exposes outward.

### 2.1 Addresses and subnets

NCS uses 10.10.0.0/24 for offices, 10.20.0.0/24 for refrigeration control and 10.30.0.0/24 for loggers and cameras. A /24 mask means the first three numbers name the network and the last names the host. Two devices on the same subnet talk directly through the switch; devices on different subnets must pass a router or firewall, which is where policy can be applied.

Priya's trace of a logger reading shows the boundaries in use: the logger reports to GW-LOG at 10.30.0.5, and firewall rule 21 lets 10.30.0.5 reach the vendor cloud on TCP 443. The same firewall holds rule 9, "any to 10.20.0.0/24, TCP 502, allow", which lets every office address reach the refrigeration controllers' Modbus port.

### 2.2 VLANs and firewalls

A VLAN separates traffic logically on shared switches. VLANs alone do not filter: the filtering happens where traffic is routed between them. A firewall rule names source, destination, protocol and port, and whether to allow or deny. A sound default is "deny everything not explicitly allowed".

Rule 9 is the NCS example of a rule that defeats the default. It was added at commissioning so the contractor could work from any port, and nobody removed it. With rule 9 in place, the VLANs still separate broadcast traffic, but the firewall between 10.10.0.0/24 and 10.20.0.0/24 allows exactly the flow that matters most: Modbus from the office to PLC-R1 and PLC-R2. Priya's later lab finds OFFICE-7 using it.

### 2.3 Outbound cloud connections

GW-LOG opens an outbound HTTPS connection (TCP 443) to the logger vendor's cloud. Outbound connections are easier to secure than inbound ones because nobody on the internet can start a session to the gateway — provided the firewall does not also forward an inbound port to it. Remote-support tools often add exactly that forwarding, which is how many devices become internet-facing.

At NCS, rule 21 is outbound only; Priya checked that no port-forward to 10.30.0.5 exists, and recorded that check, so the claim can be re-verified after the next vendor visit.

### 2.4 Name resolution

The gateway finds the cloud by DNS. If the gateway uses an internal DNS server, a misconfiguration there can break logging plant-wide; if it uses a public resolver directly, the firewall must permit that too. Write down which.

For GW-LOG, Priya found it used the site's internal DNS server, so the rule set needed no public-resolver exception. That has a consequence for the certificate failures in Chapter 22: when LOG-03 stopped uploading on 5 October, DNS was one of the dependencies to rule out before blaming the expired certificate. A one-line note in the inventory, "GW-LOG resolver: internal DNS, 10.10.0.2", would have answered that question in seconds.

### Worked example (synthetic NCS)

Priya traces a logger reading: logger → radio → GW-LOG (10.30.0.5) → firewall rule 21 "10.30.0.5 to vendor cloud, TCP 443, allow" → internet. She also finds rule 9, "any to 10.20.0.0/24, TCP 502, allow", left from commissioning. Rule 9 lets office PCs reach the refrigeration controllers' Modbus port; she flags it for review.

> **Synthetic case — Northgate Cold Storage.** Addresses and rule numbers are invented.

### Errors and limits

A diagram may not match the firewall; the configuration export is the evidence. Never test rules by sending traffic to production controllers without a permit.

### Exercises

- **EX004 — Same subnet or not?** Are 10.20.0.11 and 10.20.0.40 on the same /24? What about 10.20.0.11 and 10.30.0.11? *Rubric:* 3 = yes, no, with reason; 2 = answers only; 1 = one right; 0 = none.
- **EX005 — Rewriting rule 9.** Rewrite rule 9 so only HMI-C (10.20.0.20) may reach the controllers on TCP 502. *Rubric:* 3 = source 10.20.0.20, destinations the PLC addresses, TCP 502, allow, plus default deny; 2 = minor gap; 1 = still "any"; 0 = none.
- **EX006 — Inbound versus outbound.** Explain why GW-LOG's outbound HTTPS is lower risk than a port-forward to it. *Rubric:* 3 = no unsolicited inbound sessions from internet; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Addresses, VLANs, rules and DNS determine which conversations are possible; reading them is how a technologist finds the unintended ones.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write short Python programs using only the standard library; (2) use lists, dictionaries and loops to process records; (3) handle missing data explicitly; and (4) keep scripts readable for colleagues who are not programmers.

### 3.1 Why technologists script

Much OT security work is comparing lists: assets in documentation versus assets seen on the network, approved flows versus observed flows, certificate dates versus today. Doing this by eye across hundreds of rows is slow and error-prone. A twenty-line script does it the same way every time, and its output can be attached to a ticket.

Priya's first such script compared the contractor's documentation with a passive observation and produced the five-line Chapter 11 output: two matches, one camera only on the network, HMI-C only in the documents and PLC-R2's version conflict.

### 3.2 Dictionaries for lookups

A Python dictionary maps a key (device name) to a value (firmware version). Checking "is this device documented?" becomes `name in docs`, which is fast and readable. Sets give union and difference directly: `set(a) - set(b)` lists what is in `a` but not `b`.

Priya's inventory script keeps one dictionary from the contractor's documents and one from passive observation, each mapping a device name to its firmware string. The union of the two key sets is the full list of devices to report; the differences are the two interesting groups, CAM-DOCK only on the network and HMI-C only in the documents.

### 3.3 Missing data is a result

When a value is absent, say so in the output. `dict.get(key)` returns `None` instead of crashing, and the script can print "-" and a status such as "only-in-docs". Silently skipping missing rows is how gaps disappear from reports.

Priya's first draft did exactly that: it looped over matches only, so CAM-DOCK, which was missing from the documents, never appeared. A colleague asked where the camera was. Her fix was one line, iterating over `sorted(set(docs) | set(seen))`, so every device prints with a status and the missing one says so. The Chapter 11 output now shows `docs=-` for CAM-DOCK rather than leaving it out.

### 3.4 Readable output

Align columns with f-string widths (`f"{name:9}"`) and put the decision at the end of each line. A reviewer can then scan the last column for anything that is not "match".

In the Chapter 11 output the last column reads match, match, only-on-network, only-in-docs and VERSION-CONFLICT, so a facilities manager can find the three lines that need action without reading the firmware strings. The device names are padded to nine characters, which keeps the documentation and network columns aligned even for CAM-DOCK. A reviewer who sees a status that is not one of the five documented values knows the script has met an input it does not understand.

### Worked example (synthetic NCS)

Priya writes a loop over two dictionaries, one from the refrigeration contractor's documentation and one from a passive network observation. Her first draft printed only matches; a colleague asked where CAM-DOCK was. She rewrote it to iterate over the union of keys so every device appears with a status. The full version is the Chapter 11 lab.

> **Synthetic case — Northgate Cold Storage.** The data are invented.

### Errors and limits

Scripts that read live devices need a permit and careful rate limits; scripts in this course read files only. Name variables for what they hold, not `x` and `y`.

### Exercises

- **EX007 — Set difference.** Given `docs = {"A", "B", "C"}` and `seen = {"B", "C", "D"}`, what do `docs - seen` and `seen - docs` return? *Rubric:* 3 = {"A"} and {"D"} with meaning; 2 = values only; 1 = one; 0 = none.
- **EX008 — Handling a missing key.** What does `{"PLC-R1": "2.4"}.get("PLC-R9")` return, and what should the script print? *Rubric:* 3 = None; print "-" plus a status; 2 = value only; 1 = says KeyError; 0 = none.
- **EX009 — Fixing the matches-only bug.** Write the one-line change that makes Priya's loop show every device. *Rubric:* 3 = iterate over `sorted(set(docs) | set(seen))`; 2 = idea right; 1 = vague; 0 = none.

### Synthesis

Small, readable scripts that report every row — including missing ones — turn list comparison into repeatable evidence.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) design a simple asset table with keys and attributes; (2) choose identifiers that survive device replacement; (3) represent relationships such as "gateway serves loggers"; and (4) keep sensitive attributes out of general tables.

### 4.1 Tables, keys and attributes

An asset table holds one row per asset. The key must be unique and stable. IP addresses are poor keys because they change when a device is re-addressed; serial numbers change when a device is replaced. NCS uses an asset tag painted on the equipment (for example "MP-1/PLC-R1"), which stays with the function.

Priya's schema keys every table on that tag, which is how the asset, logger and flow tables join cleanly even after PLC-R2's documented firmware turned out to be wrong.

### 4.2 Relationships

Forty loggers report through GW-LOG. Storing "gateway" as an attribute of each logger row creates a one-to-many relationship that lets a query answer "which loggers go dark if GW-LOG fails?" in one line. Similarly, a flow table with source and destination keys links assets into the communication picture used in Chapter 12.

Priya's loggers table holds tag, room and gateway_tag. Her query `select tag, room from loggers where gateway_tag = 'GW-LOG'` lists all forty loggers with their rooms, and that list became the impact table in NCS's continuity plan.

### 4.3 What not to store

Passwords, private keys and full configuration backups do not belong in a shared asset table. Store a reference ("credential held in vault entry OT-17") and keep the secret in a system designed for it. A spreadsheet of passwords on a shared drive is a common finding in OT assessments.

In Priya's schema, the assets table has an owner column and a source column but no credential column. HMI-C's local administrator password, which she later finds on a sticky note, belongs in the vault with a reference such as OT-17 in the table, not in a cell anyone with the spreadsheet can read.

### 4.4 Data quality fields

Add "source" (documentation, network observation, walk-down) and "last verified" date to each row. An inventory without dates cannot be trusted after a year.

PLC-R2 shows why. Its documented firmware, 2.4, came from the contractor's commissioning records; the passive capture reported 2.1; and Priya's walk-down read 2.1 from the front panel. With a source column, the row now reads firmware 2.1, source walk-down, last verified on the visit date, and a reader can see that the older value came from documents that were never updated after commissioning. Without the date, nobody would know whether the walk-down reading was last week's or two years old.

### Worked example (synthetic NCS)

Priya's schema: assets(tag, type, function, zone, firmware, owner, source, last_verified); loggers(tag, room, gateway_tag); flows(src_tag, dst_tag, protocol, port, approved). Her query "select tag, room from loggers where gateway_tag = 'GW-LOG'" lists all 40 loggers and their rooms, which became the impact list in the facility's continuity plan.

> **Synthetic case — Northgate Cold Storage.** Schema and counts are invented.

### Errors and limits

A model is only as good as its upkeep; assign an owner. Over-normalising a small facility's data can make it harder to use than a well-kept single table.

### Exercises

- **EX010 — Choosing a key.** Why is the painted asset tag a better key than the IP address for PLC-R1? *Rubric:* 3 = stable across re-addressing and replacement; tied to function; 2 = partial; 1 = "easier"; 0 = none.
- **EX011 — Query for an impact list.** Write SQL listing loggers in room "Freezer-2" served by GW-LOG. *Rubric:* 3 = correct where clause on both columns; 2 = one condition; 1 = syntax only; 0 = none.
- **EX012 — Handling a credential field.** A colleague adds a "password" column. What do you replace it with? *Rubric:* 3 = vault reference, secret elsewhere, access-controlled; 2 = remove only; 1 = encrypt the sheet; 0 = keep.

### Synthesis

A small, stable data model with keys, relationships and dates is what turns inventory into answers.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain safety, availability, integrity and confidentiality for a cold-storage site; (2) describe common OT threat sources; (3) read a public advisory and extract what matters; and (4) use ATT&CK for ICS identifiers correctly.

### 5.1 What matters at NCS

The worst outcome at NCS is an ammonia release — a safety event handled by separate gas detection and emergency ventilation. Next comes loss of cooling and condemned stock. Then integrity of temperature records, which customers and food-safety inspectors rely on. Confidentiality matters for customer contracts and camera footage. The order guides where to spend effort first.

Priya's ranking follows this order: ammonia safety stays with the gas-detection system and the refrigeration engineer; her security work starts with the paths that could stop cooling or falsify temperature records.

### 5.2 Threat sources

Most OT incidents are not elite attacks. They include commodity ransomware that spreads from office networks onto Windows HMIs, misused vendor remote access, mistakes during maintenance, and devices exposed to the internet with default passwords. CISA advisory AA21-042A, on a water treatment facility, describes access through desktop-sharing software combined with weak passwords — a pattern that fits many small sites.

Priya found all four patterns at NCS: a desktop-sharing tool on HMI-C, a shared HMI password on a sticky note, a forgotten cellular router and a camera exposed to the internet.

### 5.3 Reading an advisory

From any advisory extract: affected product and versions, the weakness, whether exploitation has been seen, and the recommended mitigations. Then ask whether NCS has that product (your asset table answers this) and whether the mitigation is feasible.

Priya applied this to AA21-042A and found three NCS parallels: the contractor's desktop-sharing tool on HMI-C, an HMI operating system near end of support, and a shared HMI password written on a sticky note. Her asset table answered the first question; the mitigation, supervised sessions instead of an always-on tool, was feasible because the contractor visits only a few times a month.

### 5.4 ATT&CK for ICS

MITRE ATT&CK for ICS gives names and IDs to observed adversary behaviour. T0886 *Remote Services* covers using remote-access services to reach control systems; T0883 *Internet Accessible Device* covers devices reachable from the internet. Use the IDs to label findings consistently, not to claim completeness.

Priya labels the contractor's always-on desktop-sharing tool on HMI-C as T0886, and the dock camera reachable from the internet as T0883. Neither label says the site has been attacked; each says which kind of observed behaviour the finding would enable. When a CISA advisory later cites T0886 for a product family, she can search her findings for that ID and know at once which NCS items are relevant.

### Worked example (synthetic NCS)

Priya reads AA21-042A and notes three NCS parallels: the refrigeration contractor uses a desktop-sharing tool on HMI-C; HMI-C runs an operating system near end of support; and the shared HMI password is on a sticky note. She labels the first finding T0886 and proposes removing the always-on tool in favour of supervised sessions.

> **Synthetic case — Northgate Cold Storage.** The parallels are invented; the advisory is real.

### Errors and limits

Advisories describe one situation; do not copy their mitigations without checking fit. Gas-detection safety systems are outside a security technologist's authority to modify.

### Exercises

- **EX013 — Ranking NCS concerns.** Put in order of priority: camera footage leak, ammonia release, falsified temperature records, loss of cooling. *Rubric:* 3 = release, cooling, records, footage with reasons; 2 = order only; 1 = partly right; 0 = none.
- **EX014 — Four facts from an advisory.** List the four items to extract from an ICS advisory. *Rubric:* 3 = product/versions, weakness, exploitation status, mitigations; 2 = three; 1 = two; 0 = none.
- **EX015 — Labelling a finding.** Which ATT&CK for ICS ID fits "contractor reaches HMI-C through desktop-sharing software"? *Rubric:* 3 = T0886 Remote Services; 2 = right name, no ID; 1 = T0883; 0 = none.

### Synthesis

Security literacy means ranking consequences honestly, recognising everyday threat sources, and reading advisories and ATT&CK labels with care.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) identify OS-level risks on HMIs and historians; (2) explain what virtualization changes for OT servers; (3) plan snapshots and backups that actually restore; and (4) respect vendor support constraints when hardening.

### 6.1 The HMI as a Windows host

HMI-C runs a long-term-servicing edition of Windows with the refrigeration vendor's HMI software. Its risks are ordinary: unpatched services, shared local accounts, USB sticks, and remote-desktop tools. Its constraints are not: the vendor certifies specific OS builds, and an untested update can stop the HMI runtime. Hardening therefore goes through a test unit or a vendor-approved list.

At NCS that means the vendor's approved patch list for HMI-C is checked before each maintenance window, and anything not on it is first tested on the contractor's test unit.

### 6.2 Virtualized historians

NCS runs HIST as a virtual machine on a small host in the comms room. Virtualization helps recovery — a VM can be restored from a snapshot in minutes — but concentrates risk: compromise or failure of the hypervisor affects every VM on it. Management interfaces for the hypervisor belong on an isolated management network, never on the office VLAN.

Priya's review of HIST found the hypervisor console reachable from the office VLAN; her plan moved it to the management VLAN, where only the OT management host can reach it.

### 6.3 Snapshots are not backups

A snapshot lives on the same storage as the VM; if the storage fails or ransomware encrypts it, both go. A backup is a separate copy, ideally offline or immutable, with a tested restore. Record the restore test date — an untested backup is a hope.

HIST had one snapshot, eight months old, and no separate backup. Priya's plan adds a nightly backup of the VM to a NAS on the OT management VLAN with an offline weekly copy, and a restore test into an isolated network next month.

### 6.4 Least privilege on hosts

Operators use a named, non-administrator account; the vendor runtime uses a service account that cannot log in interactively; administrator rights are granted per task and logged.

At NCS this replaced the shared "shift" login on HMI-C: operators now log in with named accounts that cannot install software, and the refrigeration vendor's runtime runs under a service account with no interactive logon. When Priya needed administrator rights to apply the allow-listing policy, she requested them for that change ticket, and the elevation was logged against the ticket number. The vendor's HMI runtime kept working because its service account, not an operator, owns the processes that talk to PLC-R1 and PLC-R2.

### Worked example (synthetic NCS)

Priya reviews HIST: one snapshot from eight months ago, no separate backup, hypervisor console reachable from the office VLAN. Her plan: nightly backup of the HIST VM to a separate NAS on the OT management VLAN with an offline weekly copy; move the hypervisor console to the management VLAN; perform and record a restore test into an isolated network next month.

> **Synthetic case — Northgate Cold Storage.** Findings are invented.

### Errors and limits

Restoring a VM onto the live network may create a duplicate host that conflicts with the original; test restores in isolation. Some vendor HMIs are not supported in virtual machines.

### Exercises

- **EX016 — Snapshot or backup?** Explain why HIST's eight-month-old snapshot does not count as a backup. *Rubric:* 3 = same storage, not independent, stale, never restored; 2 = two reasons; 1 = one; 0 = none.
- **EX017 — Moving the hypervisor console.** State the risk of the console being reachable from the office VLAN. *Rubric:* 3 = office malware/user could control or destroy all VMs; 2 = partial; 1 = vague; 0 = none.
- **EX018 — A safe restore test.** Describe how to test-restore HIST without disturbing operations. *Rubric:* 3 = restore into isolated network, verify data and services, record date; 2 = two; 1 = restore over live VM; 0 = none.

### Synthesis

OS and virtualization security in OT is mostly disciplined basics — least privilege, isolated management and backups proven by restore — inside vendor constraints.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) replace shared accounts with named accounts and roles; (2) design contractor access with time limits; (3) apply multi-factor authentication where it fits OT; and (4) review access regularly.

### 7.1 Shared passwords

At many sites one HMI password is shared by every shift and known to former staff. It cannot tell an investigator who changed a freezer setpoint, and it cannot be revoked for one person. Named accounts restore both attribution and revocation. IEC 62443-3-3 makes unique identification of human users a system requirement under its first foundational requirement.

Priya's access review at NCS found exactly this: one shared "shift" account among 11 HMI accounts, plus two accounts belonging to former staff.

A shared account also makes the evidence log weaker: an alarm acknowledged as "shift" cannot be tied to a person.

### 7.2 Roles

NCS needs three HMI roles: viewer (night security guard checking temperatures), operator (acknowledge alarms, adjust setpoints within limits) and engineer (change limits and alarm settings). The contractor's laptop that programs PLC-R1 is a separate privilege again, controlled by possession of the laptop and its project password.

The viewer role matters more than it looks. NCS's night security guard checks freezer temperatures on HMI-C during rounds; with a shared operator login, the guard could also have acknowledged alarms or changed a setpoint. A viewer account removes that by design. The contractor's programming laptop sits outside these roles because PLC-R1's project file, not HMI-C, controls what can be downloaded to the controller.

### 7.3 Contractors

The refrigeration contractor needs access a few times a month. Give the contractor named accounts that are disabled by default, enabled for a ticket and a time window, and reviewed afterwards. Remove the always-on remote-access tool identified in Chapter 5.

At NCS the two contractor accounts were always enabled. Priya set them to disabled-by-default; the facilities manager enables one for a ticket and a time window, and the session goes through the jump host, which records it. After the visit the account is disabled again, and the session record is filed with the ticket. The contractor visit pack in Chapter 25 turns these steps into a one-page form that takes four minutes.

### 7.4 Multi-factor authentication

Use MFA for remote access and for engineering tools. On the control-room HMI, a slow MFA prompt during an alarm can be harmful; physical security of the room and short screen-lock times may be the better balance. Document the choice.

Priya's choice at NCS: MFA on the jump host for contractor sessions and on the engineering tools, but not on HMI-C itself. The control room is locked, HMI-C locks after a short idle period, and operators log in with named accounts. An MFA prompt that delays an operator acknowledging a high-temperature alarm on Freezer-2 would create a worse risk than the one it removes, and that reasoning is written in the access policy.

### 7.5 Reviews

Every quarter, list enabled accounts and compare with the staff and contractor list. Disable leavers the same day HR notifies you.

At NCS this review found 11 HMI accounts: 6 current staff, 2 former staff, 1 shared "shift" account and 2 contractor accounts that were always enabled. The two former-staff accounts were disabled the same day; the shared account was replaced with named operator accounts within a month; the contractor accounts became disabled-by-default. The next quarter's review should start from that list and confirm that none of the four problems has returned, for example a new contractor account created during an emergency visit and never disabled.

### Worked example (synthetic NCS)

Priya's access review finds 11 HMI accounts: 6 current staff, 2 former staff, 1 shared "shift" account and 2 contractor accounts always enabled. Actions: disable the 2 former-staff accounts today; replace "shift" with named operator accounts within a month; set contractor accounts to disabled-by-default with ticket-based enabling.

> **Synthetic case — Northgate Cold Storage.** Counts are invented.

### Errors and limits

Account lockout on control-room screens can block an operator during an emergency; prefer alerting and delays. Some legacy PLCs have no user accounts at all; protect them through network controls.

### Exercises

- **EX019 — Choosing a role.** The night guard must check freezer temperatures on HMI-C. Which role and why? *Rubric:* 3 = viewer, least privilege, no setpoint changes; 2 = role only; 1 = operator; 0 = engineer.
- **EX020 — Contractor access design.** Write three rules for contractor HMI accounts. *Rubric:* 3 = named, disabled by default, enabled per ticket/window with review; 2 = two; 1 = one; 0 = none.
- **EX021 — Where MFA fits.** Name one NCS access path that must have MFA and one where you would document an alternative. *Rubric:* 3 = remote access/engineering path; control-room HMI with physical control; 2 = one; 1 = MFA everywhere without thought; 0 = none.

### Synthesis

Named accounts, matched roles, time-boxed contractor access and regular reviews give OT identity both accountability and safety.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) divide a small facility into zones; (2) define conduits between zones with allowed traffic; (3) place a DMZ for shared services; and (4) explain defence in depth with concrete layers.

### 8.1 Zones for NCS

IEC 62443-3-2 introduces zones (groups of assets with common security requirements) and conduits (the communication paths between them). NCS needs at least four zones: office, refrigeration control (PLC-R1, PLC-R2, HMI-C), logging and cameras (loggers, GW-LOG, CAM-DOCK), and a small DMZ holding the historian replica and the remote-access jump host.

Priya's zone diagram showed rule 9 crossing office → control directly; because no listed conduit allowed it, the architecture document itself gave the reason to remove it.

The diagram also made the DMZ's purpose concrete: it is where office users read data without entering the control zone.

### 8.2 Conduits

Each conduit lists what may cross it. Office → DMZ: HTTPS to the historian replica's reports. DMZ → control: none initiated from the DMZ except the jump host's session to HMI-C when enabled. Control → DMZ: historian replication. Logging zone → internet: GW-LOG to vendor cloud on 443 only. Everything else is denied.

Priya's conduit table has five columns: source zone, destination zone, protocol, initiator and purpose. The initiator column matters most: replication from control to DMZ is initiated by the control side, so the DMZ never needs a rule allowing it to open sessions inward.

### 8.3 Why a DMZ

Without a DMZ, office users who need temperature reports connect straight into the control zone. With it, they reach a copy, and the control zone accepts no sessions from the office at all. That single change removes the path that most commodity ransomware uses to reach HMIs.

At NCS the reports users want are temperature certificates and compressor run hours. OFFICE-7's energy macro read run hours directly from PLC-R2 over rule 9; Priya's fix had it read the same values from the historian replica in the DMZ, and only then was office → control blocked.

### 8.4 Defence in depth

Layers at NCS: zone firewalls; named accounts; allow-listing on HMI-C; passive monitoring of the control zone; offline backups; and, outside the security team's control, independent ammonia detection and emergency ventilation. Each layer assumes the one before it can fail.

Priya's evaluation in Chapter 23 shows the assumption at work: five of six controls passed, but the camera-zone rule allowed CAM-DOCK to reach HIST on a web port. The other layers, named accounts, allow-listing on HMI-C and passive monitoring, were still in place while the rule was narrowed.

### Worked example (synthetic NCS)

Priya draws the zone diagram and lists conduits in a table with source zone, destination zone, protocol, initiator and purpose. Comparing it with the current firewall, she finds the commissioning rule from Chapter 2 crossing office → control directly. The architecture document gives the reason to remove it: it is not a listed conduit.

> **Synthetic case — Northgate Cold Storage.** The zones are a teaching design.

### Errors and limits

Zones on paper mean nothing until enforced in switches and firewalls. Cameras often get forgotten; they are network devices with their own vulnerabilities and belong in a zone too.

### Exercises

- **EX022 — Placing CAM-DOCK.** Which NCS zone should the dock cameras join and why not the control zone? *Rubric:* 3 = logging/camera zone (or own zone); unrelated to control and frequently vulnerable; 2 = zone only; 1 = control zone; 0 = none.
- **EX023 — A conduit table row.** Write the row for historian replication. *Rubric:* 3 = control → DMZ, protocol/port, initiator control side, purpose; 2 = three fields; 1 = vague; 0 = none.
- **EX024 — Layers that assume failure.** Name two NCS layers and say which failure each covers. *Rubric:* 3 = two layers with specific failure covered; 2 = layers only; 1 = one; 0 = none.

### Synthesis

Zones, conduits and a DMZ convert "segment the network" into a checkable design, and defence in depth makes each layer's failure survivable.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) collect evidence with timestamps, sources and hashes; (2) separate what you saw from what you concluded; (3) count with denominators; and (4) present a measurement with its uncertainty.

### 9.1 Recording evidence

For every observation record: what was observed, where, when (with clock source), by whom and how. For exported files add a SHA-256 hash, computed with `hashlib.sha256(open(path, "rb").read()).hexdigest()`, so anyone can confirm the file has not changed.

Priya's entry E-014 is the pattern: timestamp 2026-03-03 10:22 with the laptop clock synced to NTP, her name, the firewall config exported from FW-1's web interface as fw1-0303.txt, and a SHA-256 hash recorded with the file.

The hash, beginning 9c1e…, lets anyone confirm later that the file has not changed since that entry.

### 9.2 Observation and conclusion

"Rule 9 permits any source to TCP 502 on 10.20.0.0/24 (firewall export 3 March, hash recorded)" is an observation. "Office ransomware could reach the PLCs" is a conclusion. Both belong in a report, labelled. Readers trust reports that make the line visible.

Priya's entry E-014 keeps the two on separate lines: the observation that rule 9 allows any source to TCP 502 on 10.20.0.0/24, and, on its own line, the conclusion that office hosts can reach PLC Modbus ports. A reader who disagrees with the conclusion can still rely on the observation, and can check it against the hashed export.

### 9.3 Denominators

"Five loggers have expired certificates" means little without "out of 40". "Two of 11 accounts belong to former staff" is clearer than "some leaver accounts exist". Percentages without counts hide small samples.

At NCS the denominators come from Priya's own tables: 2 former-staff accounts out of 11 HMI accounts, 1 expired logger certificate out of the 4 the Chapter 22 lab checks, 2 unapproved flows out of 5 conversations seen. Each count tells the reader both the size of the problem and the size of what was checked. A report that said "some accounts belong to leavers" would invite a reader to guess whether that meant 2 or 20.

### 9.4 Uncertainty

If you checked 10 of 40 loggers and found 2 with default passwords, the fleet rate is uncertain. Say: "2 of 10 sampled; the remaining 30 not yet checked." Avoid extrapolating "20 % of the fleet" unless the sample was random and you state the uncertainty.

At NCS, the vendor's answer that each logger has a unique password printed on its label is a claim about all 40; a sample of 10 checked on the bench tests it. If all 10 match the claim, write "10 of 10 sampled met it; 30 not checked", not "the fleet meets 5.1".

### Worked example (synthetic NCS)

Priya's evidence log entry: "E-014, 2026-03-03 10:22 (laptop clock synced to NTP), Priya Nair, exported firewall config from FW-1 web UI, file fw1-0303.txt, SHA-256 starting 9c1e…, observation: rule 9 allows any → 10.20.0.0/24 TCP 502; conclusion (separate line): office hosts can reach PLC Modbus ports."

> **Synthetic case — Northgate Cold Storage.** Evidence IDs and hashes are invented.

### 9.5 Chain of custody in a small site

Small sites rarely have evidence lockers. A practical minimum at NCS is an encrypted folder per investigation, a read-only copy of every original export, and a custody log listing each transfer: who handed what to whom, when and why. If the case later goes to an insurer or to police, that log is what shows the evidence was not altered between the firewall and the report. Keep the log with the evidence, not in someone's e-mail.

Priya's E-014 export is the first entry in such a log.

### Errors and limits

Clocks on devices drift; note which clock a timestamp came from. A hash proves a file is unchanged since hashing, not that its content was true.

### Exercises

- **EX025 — Observation or conclusion?** Label: (a) "HMI-C had a desktop-sharing service running at 14:05"; (b) "the contractor was using it". *Rubric:* 3 = observation, conclusion; 2 = with weak reasoning; 1 = reversed; 0 = none.
- **EX026 — Rewriting with a denominator.** Rewrite "several loggers need new certificates". *Rubric:* 3 = count of total with date; 2 = count only; 1 = percentage only; 0 = none.
- **EX027 — Reporting a partial sample.** Write the sentence reporting 2 default-password loggers among 10 checked. *Rubric:* 3 = 2 of 10 sampled, 30 unchecked, no extrapolation; 2 = partial; 1 = "20 % of fleet"; 0 = none.

### Synthesis

Evidence becomes trustworthy when it is timestamped, hashed, counted against a denominator and kept separate from interpretation.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — OT, IoT and cyber-physical security: orientation

### Learning outcomes

You will (1) define OT, IoT and cyber-physical systems in NCS terms; (2) describe the refrigeration control loop; (3) name the main guidance documents and who they are for; and (4) explain why safety systems stay outside security changes.

### 10.1 Three overlapping terms

Operational technology monitors and controls physical processes — here, compressors, evaporator fans and valves. IoT devices are network-connected sensors and actuators — here, the wireless temperature loggers and cameras. A cyber-physical system is the loop of sensing, computing and acting on the physical world. NCS is all three at once.

At NCS the overlap is visible in one room: Freezer-2's probe feeds PLC-R1, while a wireless logger in the same room reports through GW-LOG to the cloud. One is OT, the other IoT, and both describe the same physical temperature, which is what makes the two-probe comparison in Chapter 24 possible.

### 10.2 The refrigeration loop

A temperature probe in Freezer-2 reports −21 °C; PLC-R1 compares it with the −22 °C setpoint and increases compressor capacity; more refrigerant evaporates, the room cools, and the probe reports again. An attacker who changes the setpoint, falsifies the probe or overrides the compressor command breaks the loop. ATT&CK for ICS T0836 *Modify Parameter* covers the setpoint case.

Priya's map of this loop, probe TT-F2 → PLC-R1 → compressor C-1 → evaporator → room → TT-F2, adds two independent paths: the wireless logger's second temperature view and the gas-detection panel that trips ventilation without PLC-R1.

### 10.3 Guidance map

NIST SP 800-82r3 guides OT security programmes for asset owners such as NCS. The IEC 62443 series covers industrial automation and control systems for owners, integrators and product suppliers. NIST IR 8259 describes cybersecurity activities for IoT device manufacturers, and ETSI EN 303 645 sets a baseline for consumer IoT products — useful as a checklist for buying loggers and cameras.

Priya uses EN 303 645 for exactly that purpose: her vendor questionnaire for the loggers asks the 5.1, 5.2, 5.3, 5.5 and 5.8 questions before NCS buys more.

The answers then decide whether a compensating control, such as comparing logger and PLC probes, is needed.

### 10.4 Safety stays separate

Ammonia gas detection and emergency ventilation are life-safety systems. Security work may observe and report on them, but changes go through the safety owner and the refrigeration engineer, never as a side effect of a firewall project.

At NCS this rule applies directly to Priya's firewall work. When she moved the dock cameras into their own zone, she confirmed with the refrigeration engineer that the gas-detection panel had no network connection the change could affect. If it had, the change would have gone to the safety owner first. Her reports may note that the gas-detection panel trips ventilation without PLC-R1, which reduces several cyber scenarios, but she does not test or reconfigure it.

### Worked example (synthetic NCS)

Priya maps the Freezer-2 loop: probe TT-F2 → PLC-R1 → compressor C-1 → evaporator → room → TT-F2. Beside it she notes the independent paths: wireless loggers give a second temperature view to the cloud, and the gas-detection panel trips ventilation without PLC-R1. Both reduce the chance that one compromise hides a problem.

> **Synthetic case — Northgate Cold Storage.** Tag names are invented.

### Errors and limits

Consumer IoT standards do not automatically apply to industrial devices; use them as reference questions. Loop diagrams simplify; real systems have cascades and interlocks.

### Exercises

- **EX028 — Three attack points on the Freezer-2 loop.** Name one per element: sensor, controller, actuator. *Rubric:* 3 = three plausible points; 2 = two; 1 = one; 0 = none.
- **EX029 — Choosing a buying checklist.** Which document would you use to write purchase questions for new temperature loggers? *Rubric:* 3 = ETSI EN 303 645 (or NIST IR 8259 for manufacturer activities) with reason; 2 = name only; 1 = SP 800-82 only; 0 = none.
- **EX030 — Why loggers help integrity.** Explain how the cloud loggers reduce the impact of a falsified TT-F2 reading. *Rubric:* 3 = independent measurement path reveals disagreement; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Orientation means seeing the physical loop, knowing which guidance fits which role, and keeping safety systems out of security side effects.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — OT, IoT and cyber-physical security: assets and context

### Learning outcomes

You will (1) build an inventory by combining documentation with passive observation; (2) interpret conflicts between sources; (3) add business context — function and consequence — to each asset; and (4) decide what to do about unknown devices.

### 11.1 Two sources, neither complete

Documentation from the refrigeration contractor lists what was installed; passive observation of network traffic shows what is talking now. Documentation misses later additions; observation misses devices that are quiet or switched off. NIST SP 800-82r3 recommends combining methods rather than relying on active scanning, which can disturb fragile devices.

```python
"""Lab 11: merge two synthetic NCSW asset lists and flag conflicts (no scanning)."""
eng = {"PLC-R1": "fw 2.4", "PLC-R2": "fw 2.4", "HMI-C": "win10-ltsc", "GW-LOG": "fw 1.9"}
seen = {"PLC-R1": "fw 2.4", "PLC-R2": "fw 2.1", "GW-LOG": "fw 1.9", "CAM-DOCK": "fw ?"}
for a in sorted(set(eng) | set(seen)):
    e, s = eng.get(a), seen.get(a)
    status = "match" if e == s else ("only-in-docs" if s is None else "only-on-network" if e is None else "VERSION-CONFLICT")
    print(f"{a:9} docs={e or '-':11} network={s or '-':8} {status}")
```

Run with `python3 lab_inv.py`. Verified output:

```text
CAM-DOCK  docs=-           network=fw ?     only-on-network
GW-LOG    docs=fw 1.9      network=fw 1.9   match
HMI-C     docs=win10-ltsc  network=-        only-in-docs
PLC-R1    docs=fw 2.4      network=fw 2.4   match
PLC-R2    docs=fw 2.4      network=fw 2.1   VERSION-CONFLICT
```

At NCS, the documentation lacked CAM-DOCK, and the observation lacked HMI-C; neither source alone was the inventory.

The comparison also produced PLC-R2's version conflict, which only a walk-down could settle.

### 11.2 Reading the conflicts

CAM-DOCK appears only on the network: someone installed a camera without updating records. HMI-C appears only in documentation: it may have been quiet during the observation window, or its traffic was not captured. PLC-R2 shows a version conflict — documentation says 2.4, the network shows 2.1 — which matters because an advisory might affect 2.1 but not 2.4.

Priya resolved the PLC-R2 conflict by walking the machine room with the contractor and reading the version from the front panel: 2.1. The documentation was wrong; the controller had never been upgraded. She corrected the inventory with the walk-down as source.

### 11.3 Context

For each asset add function, zone, owner and consequence of loss. The camera's consequence is low for cooling but it may be an entry point; PLC-R2's consequence is high, so its version conflict goes first.

Priya's notebook gives each of the five rows those four fields. PLC-R2: compressor control, refrigeration control zone, contractor and facilities manager, loss of cooling within hours. CAM-DOCK: dock video, currently on the logging network, logistics team, low for cooling but a possible foothold. The consequence column is what turns five statuses into an ordered work list.

### 11.4 Unknown devices

An unknown device is investigated physically before anything else: find it, identify the owner, decide whether it belongs. Never "test" an unknown device by sending it traffic.

At NCS, the unknown address 10.4.2.77 seen in Chapter 19 was traced this way: a physical search found a dock printer plugged into a camera-zone port, installed by the logistics team with an address copied from another site's plan. Nobody sent it a packet to find out what it was. It was moved, re-addressed and added to the inventory with logistics as owner.

### Worked example (synthetic NCS)

Priya walks the machine room with the contractor and reads PLC-R2's version from its front-panel display: 2.1. The documentation was wrong; the controller was never upgraded. She corrects the inventory, records the walk-down as the source, and opens a ticket to plan the upgrade with the contractor.

> **Synthetic case — Northgate Cold Storage.** The lab data and the walk-down are invented.

### Errors and limits

Passive observation depends on capture location; a mirror port on one switch sees only that switch's traffic. A device's self-reported version string can be wrong or spoofed.

### Exercises

- **EX031 — Explaining "only-in-docs".** Give two possible reasons HMI-C did not appear in the network observation. *Rubric:* 3 = quiet/off during window; capture point did not see its traffic; 2 = one; 1 = "it doesn't exist"; 0 = none.
- **EX032 — Prioritising conflicts.** Which conflict does Priya handle first and why? *Rubric:* 3 = PLC-R2 version, high consequence and advisory relevance; 2 = choice only; 1 = camera; 0 = none.
- **EX033 — Adding a fifth device.** Add `"SENS-NH3": "fw 3.0"` to `seen` only. What does the lab print for it? *Rubric:* 3 = "SENS-NH3 docs=- network=fw 3.0 only-on-network"; 2 = status only; 1 = match; 0 = none.

### Synthesis

An inventory worth trusting reconciles documents, observation and walk-downs, and puts consequence beside every row.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — OT, IoT and cyber-physical security: data flows

### Learning outcomes

You will (1) write an approved flow matrix; (2) compare observed flows with it; (3) interpret unapproved and unused approved flows; and (4) turn the comparison into firewall changes.

### 12.1 The flow matrix

A flow matrix lists every permitted conversation: source, destination, port and purpose. It is the conduit table of Chapter 8 made precise enough to test. NCS has four approved flows: HMI-C to each PLC on Modbus/TCP 502, the historian polling PLC-R1, and GW-LOG to the vendor cloud on 443.

```python
"""Lab 12: compare observed synthetic flows with the approved flow matrix."""
approved = {("HMI-C", "PLC-R1", 502), ("HMI-C", "PLC-R2", 502), ("GW-LOG", "CLOUD-LOG", 443), ("HIST", "PLC-R1", 502)}
observed = [("HMI-C", "PLC-R1", 502), ("GW-LOG", "CLOUD-LOG", 443), ("OFFICE-7", "PLC-R2", 502),
            ("HIST", "PLC-R1", 502), ("GW-LOG", "PLC-R1", 502)]
for f in observed:
    print(f"{f[0]:8} -> {f[1]:9} :{f[2]:<4} {'approved' if f in approved else 'UNAPPROVED'}")
print("approved but not seen:", sorted(approved - set(observed)))
```

Run with `python3 lab_flows.py`. Verified output:

```text
HMI-C    -> PLC-R1    :502  approved
GW-LOG   -> CLOUD-LOG :443  approved
OFFICE-7 -> PLC-R2    :502  UNAPPROVED
HIST     -> PLC-R1    :502  approved
GW-LOG   -> PLC-R1    :502  UNAPPROVED
approved but not seen: [('HMI-C', 'PLC-R2', 502)]
```

The lab compares those four approved flows with five observed conversations.

The two unapproved rows, OFFICE-7 talking to PLC-R2 and GW-LOG reaching PLC-R1, are the ones to investigate first, while the unseen HMI-C to PLC-R2 flow may simply not have occurred during the capture. Chapter 27 later shows that the list was missing the historian's polling of PLC-R2, an approved flow nobody had written down.

### 12.2 Unapproved flows

OFFICE-7 talking Modbus to PLC-R2 is exactly what rule 9 allowed. It might be an engineer's spreadsheet macro, or malware. Either way it is a path from the office to a compressor controller. GW-LOG talking to PLC-R1 is stranger: the logger gateway has no reason to speak Modbus. It could be a vendor "integration" feature or a sign of compromise.

Priya traced both. OFFICE-7 ran an energy report macro reading compressor run hours from PLC-R2; the logger vendor confirmed an unused "PLC integration" feature on GW-LOG, enabled by default, which was disabled.

### 12.3 Approved but unused

HMI-C → PLC-R2 did not appear. Perhaps the window was short; perhaps the HMI reads PLC-R2 through PLC-R1. Unused approvals are candidates for removal after checking with operations — fewer open paths, less to defend.

Chapter 27 shows the risk of reading this too quickly. The observation window also missed the historian polling PLC-R2, so the flow matrix listed HIST → PLC-R1 only. When the new rule set went live, HIST stopped receiving PLC-R2 tags within four minutes and Priya rolled back. An approved-but-unseen flow is a question for operations and the vendors, not proof the flow is unused.

### 12.4 From comparison to change

Each unapproved flow gets an owner and a decision: approve with justification (and update the matrix), or block. Blocking happens in a planned window with operations informed, because a "mystery" flow may turn out to be something the plant needs.

Priya's two decisions: OFFICE-7's energy macro was moved to read run hours from the historian replica in the DMZ, and office → control was blocked in the 20 March maintenance window after the switch; GW-LOG's "PLC integration" feature was disabled with the logger vendor's agreement, and the flow disappeared without a firewall change.

### Worked example (synthetic NCS)

Priya asks the office: OFFICE-7 runs an energy report macro that reads compressor run hours directly from PLC-R2. She proposes reading the same values from the historian replica in the DMZ instead, then blocking office → control. For GW-LOG → PLC-R1 she contacts the logger vendor, who confirms an unused "PLC integration" feature enabled by default; it is disabled and the flow disappears.

> **Synthetic case — Northgate Cold Storage.** Flows and explanations are invented.

### Errors and limits

Observation windows miss monthly or seasonal flows such as defrost schedules or end-of-month reports. Ports do not prove protocol; a flow on 502 may not be Modbus.

### Exercises

- **EX034 — Classifying a new observation.** Add `("HMI-C", "PLC-R2", 502)` to `observed`. What changes in the output? *Rubric:* 3 = it prints approved and the not-seen list becomes empty; 2 = one effect; 1 = unapproved; 0 = none.
- **EX035 — Decision for OFFICE-7.** Write the decision record for the OFFICE-7 flow. *Rubric:* 3 = cause, replacement path via DMZ, block date, owner; 2 = three; 1 = "block it"; 0 = none.
- **EX036 — Why GW-LOG → PLC-R1 is suspicious.** Explain in two sentences. *Rubric:* 3 = no business need for logger gateway to speak Modbus; bridges internet-connected zone to control; 2 = one; 1 = vague; 0 = none.

### Synthesis

Comparing observed flows with an approved matrix finds the paths nobody intended, and each one ends in an owned decision.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — OT, IoT and cyber-physical security: risk scenarios

### Learning outcomes

You will (1) write risk scenarios that link a threat, a path and a physical consequence; (2) estimate likelihood and consequence on simple scales; (3) identify existing safeguards; and (4) rank scenarios for action.

### 13.1 Scenario structure

A useful scenario reads: "[Threat] uses [path] to cause [action], leading to [consequence], unless [safeguard] works." For NCS: "Office ransomware uses the office → control flow to encrypt HMI-C, leaving operators without a screen; cooling continues on PLC logic, but alarms are invisible until the screen is restored, unless the cloud logger alerts reach the duty manager's phone."

Priya's three NCS scenarios follow this form: contractor remote tool misused to change freezer setpoints, office ransomware reaching HMI-C, and an internet-exposed camera used as a foothold.

### 13.2 Scales

A three-point consequence scale suits a small site: 1 = inconvenience, 2 = stock loss or regulatory issue, 3 = harm to people or loss of the business. Likelihood, also 1–3, is a judgement based on exposure and known threat activity. Write the reason beside each score.

Priya's scores show the scale in use: the contractor-tool scenario is consequence 2, because a changed freezer setpoint means stock loss rather than harm to people, and likelihood 2, because the tool was always on but the contractor's credentials were not known to be exposed. The camera foothold is consequence 1, likelihood 2. Each score has its reason written beside it.

### 13.3 Safeguards

Existing safeguards change the story. Independent ammonia detection makes a cyber-caused gas release unlikely to go unnoticed. Cloud logger alerts provide a second view of temperature. PLC logic keeps cooling if the HMI is lost. Listing safeguards stops scenarios from sounding worse than they are — and shows which safeguard is doing a lot of work.

At NCS, the cloud logger alerts carry the contractor-tool scenario: they are the safeguard that would reveal a changed freezer setpoint.

If a contractor's tool changed a setpoint, the alerts would show the room warming before the stock was spoiled.

### 13.4 Ranking

Rank by consequence first, then likelihood, then how cheaply the scenario can be reduced. A scenario with consequence 2 and an easy fix often deserves action before a consequence-3 scenario whose safeguard is already strong.

Priya's ranking follows this rule. The contractor-tool and office-ransomware scenarios both score consequence 2 and likelihood 2; ransomware comes second only because its safeguard, PLC logic that keeps cooling without HMI-C, is stronger than the cloud alerts protecting against a changed setpoint. Removing rule 9 then went first among the controls, because it was cheap and reduced two scenarios at once, as Chapter 18 explains.

### Worked example (synthetic NCS)

Priya's top three: (1) contractor remote tool misused to change freezer setpoints (consequence 2, likelihood 2, safeguard: cloud logger alerts — fix: supervised sessions); (2) office ransomware reaches HMI-C (2, 2, safeguard: PLC keeps cooling — fix: remove rule 9); (3) internet-exposed camera used as foothold (1, 2 — fix: move to camera zone).

> **Synthetic case — Northgate Cold Storage.** Scores are illustrative.

### Errors and limits

Simple scales hide differences within a category. Likelihood for deliberate attack changes quickly with news of campaigns; revisit.

### Exercises

- **EX037 — Completing a scenario sentence.** Write a scenario for "falsified logger readings" using the five-part structure. *Rubric:* 3 = all five parts; 2 = four; 1 = vague; 0 = none.
- **EX038 — Scoring with reasons.** Score scenario 1's consequence and justify it. *Rubric:* 3 = 2 with stock/food-safety reasoning and safeguard noted; 2 = score only; 1 = 3 without reason; 0 = none.
- **EX039 — A safeguard doing heavy lifting.** Which safeguard appears in more than one scenario, and what does that imply? *Rubric:* 3 = cloud logger alerts (or PLC autonomy); single point to protect and test; 2 = name only; 1 = wrong; 0 = none.

### Synthesis

Scenarios connect cyber paths to physical consequences and safeguards, and simple, reasoned scores are enough to rank action at a small site.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — OT, IoT and cyber-physical security: methods I

### Learning outcomes

You will (1) run a structured site walk-down; (2) interview operators and contractors effectively; (3) review configuration exports safely; and (4) assemble findings with evidence references.

### 14.1 Walk-down

Walk the site with someone who owns it. Look for network sockets in odd places, cellular routers in panels, labels with passwords, laptops left connected, USB sticks in HMIs, and devices not in the inventory. Photograph only with permission, and avoid capturing screens showing customer data.

Priya's walk-down at NCS found the most important item on this list: a small cellular router in panel MP-2 labelled "contractor backup access", installed two years earlier during a network outage and forgotten. It provided a second remote path to PLC-R2 that no firewall rule showed.

### 14.2 Interviews

Ask operators what they do when the HMI freezes, who calls the contractor, and what changed recently. Ask the contractor how they connect, what tools they use and where backups live. Open questions ("walk me through a remote support call") reveal more than yes/no checklists. Take notes with the interviewee's name, role and date; separate what they said from what you saw.

The interview with the contractor explained the MP-2 router in one sentence, recorded as I-04.

The contractor said the router was installed during a two-day internet outage so he could still reach PLC-R2, and nobody removed it.

### 14.3 Configuration review

Export configurations through supported interfaces with read-only accounts: firewall rule sets, switch VLAN settings, HMI user lists. Review exports on your own workstation, not on the device. Hash exports as in Chapter 9.

At NCS the firewall export came from FW-1's web interface using a read-only account, saved as fw1-0303.txt and hashed as E-014. The HMI-C user list came the same way, which is where the 11 accounts in Chapter 7 came from. Reviewing on Priya's workstation meant she could search and annotate the rule set without any risk of saving a change to FW-1 by accident, and the hash shows later that the file she reviewed is the file she exported.

### 14.4 Assembling findings

Each finding: title, evidence IDs, affected assets, scenario link, recommendation and owner. One finding per issue; combining unrelated issues makes them impossible to close.

Priya's finding F-07 follows this form: title, undocumented cellular router in MP-2; evidence, photo E-021 and interview I-04; affected asset, PLC-R2; scenario link, the contractor remote-access scenario, because it is a second remote path; recommendation, remove it, or keep it powered off and enabled only on request with the facilities manager's approval; owner, the facilities manager. It does not mention the shared HMI password, which is a separate finding with a separate owner and closing date, even though Priya found both in the same week.

### Worked example (synthetic NCS)

During the walk-down Priya finds a small cellular router in panel MP-2 labelled "contractor backup access". The contractor explains it was installed during a network outage two years ago and forgotten. Finding F-07: "Undocumented cellular router in MP-2 provides a second remote path to PLC-R2 (evidence: photo E-021, interview I-04)." Recommendation: remove, or keep powered off and enabled only on request with the facilities manager's approval.

> **Synthetic case — Northgate Cold Storage.** Panel and finding IDs are invented.

### Errors and limits

Interviews reflect memory; confirm with evidence. Never power-cycle or unplug devices during a walk-down unless the owner asks and operations agree.

### Exercises

- **EX040 — Three walk-down targets.** List three things to look for in a control panel. *Rubric:* 3 = three relevant (modems, labels with passwords, unknown devices, connected laptops); 2 = two; 1 = one; 0 = none.
- **EX041 — An open interview question.** Write one open question for the contractor about remote access. *Rubric:* 3 = open, specific to process; 2 = open but generic; 1 = yes/no; 0 = none.
- **EX042 — Writing finding F-07's recommendation options.** Give two acceptable options for the cellular router and the condition for each. *Rubric:* 3 = remove; or off by default with approval-based enabling; conditions stated; 2 = options only; 1 = leave as is; 0 = none.

### Synthesis

Walk-downs, interviews and read-only configuration reviews, tied together by evidence IDs, find the things diagrams never show.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — OT, IoT and cyber-physical security: guided lab

### Learning outcomes

You will (1) analyse synthetic logger data for temperature excursions; (2) relate alarm delay to food-safety consequence; (3) recognise how falsified data would change the result; and (4) document a lab result with inputs and output.

### 15.1 The lab question

Did Freezer-2's chilled anteroom stay at or below 5 °C, and if not, for how long and did the alarm fire? The lab uses ten synthetic readings five minutes apart and an alarm that fires only when an excursion lasts at least 10 minutes — a delay that avoids nuisance alarms from door openings.

```python
"""Lab 15: find cold-room temperature excursions in synthetic logger data (minutes, degC)."""
readings = [(0, 2.1), (5, 2.4), (10, 3.0), (15, 5.6), (20, 7.2), (25, 8.4), (30, 6.9), (35, 4.8), (40, 3.9), (45, 2.6)]
LIMIT, ALARM_DELAY = 5.0, 10
start = None
for t, v in readings:
    if v > LIMIT and start is None: start = t
    if v <= LIMIT and start is not None:
        dur = t - start
        print(f"excursion {start}-{t} min, duration {dur} min, peak {max(x for s, x in readings if start <= s < t)} C, alarm {'raised' if dur >= ALARM_DELAY else 'not raised'} (delay {ALARM_DELAY} min)")
        start = None
```

Run with `python3 lab_excursion.py`. Verified output:

```text
excursion 15-35 min, duration 20 min, peak 8.4 C, alarm raised (delay 10 min)
```

The anteroom data are synthetic set A, which Priya used for her write-up below.

Set A has 5-minute sampling, a 5 °C limit and a 10-minute alarm delay, the values her record repeats.

### 15.2 Interpreting

The excursion started at 15 minutes and ended at 35, lasting 20 minutes with a peak of 8.4 °C. The alarm fired because 20 ≥ 10. The output also tells us the resolution limit: with five-minute samples, the true start could be anywhere between minutes 10 and 15.

That five-minute uncertainty matters for a food-safety record: a customer contract that allows excursions up to 20 minutes would be met or breached depending on where in that window the excursion really began. Priya's write-up states the duration as 20 minutes, with the start uncertain by up to five, and leaves the contractual judgement to the quality manager.

### 15.3 What an attacker would change

If readings for minutes 15–30 were replaced with values around 4 °C, the script would report no excursion at all — the record would show compliance while the goods warmed. This is why Chapter 13's scenario compares cloud logger data with the PLC's own probe in the historian: two independent records are much harder to falsify consistently.

Priya's write-up lists the missing cross-check as a limitation: synthetic set A has no HIST probe to compare.

In real NCS data, HIST's probe in the anteroom would be the cross-check: a logger reading that disagrees with it is a question before it is an excursion.

### 15.4 Recording the result

Record the input file (or its hash), the script version, the limit and delay parameters, and the output. Another technologist must be able to reproduce it exactly.

Priya's record reads: "Lab 15 on anteroom readings (synthetic set A): one excursion 15–35 min, 20 min, peak 8.4 °C, alarm raised under 10-min delay. Resolution: 5-min sampling, so start uncertain by up to 5 min. Integrity check: compared with HIST probe TT-A1 — not available in synthetic set; listed as limitation." With the input file's hash and the limit of 5 °C and delay of 10 minutes recorded, another technologist can rerun it and get the same line.

### Worked example (synthetic NCS)

Priya writes: "Lab 15 on anteroom readings (synthetic set A): one excursion 15–35 min, 20 min, peak 8.4 °C, alarm raised under 10-min delay. Resolution: 5-min sampling, so start uncertain by up to 5 min. Integrity check: compared with HIST probe TT-A1 — not available in synthetic set; listed as limitation."

> **Synthetic case — Northgate Cold Storage.** All readings are invented.

### Errors and limits

The script assumes readings are ordered and evenly spaced. An excursion still running at the last sample is not reported — a bug worth fixing.

### Exercises

- **EX043 — Changing the alarm delay.** If `ALARM_DELAY = 25`, what does the lab print? *Rubric:* 3 = same excursion, "alarm not raised (delay 25 min)"; 2 = alarm state only; 1 = no excursion; 0 = none.
- **EX044 — The unfinished excursion bug.** Append `(50, 6.0)` to the readings. What happens and how would you fix it? *Rubric:* 3 = second excursion not printed; add a final check after the loop; 2 = one; 1 = says it prints; 0 = none.
- **EX045 — Falsification check.** Describe a check that would reveal replaced readings. *Rubric:* 3 = compare with independent PLC/historian probe or second logger, flag disagreement; 2 = partial; 1 = vague; 0 = none.

### Synthesis

A guided lab turns raw readings into a reproducible, bounded statement — and shows exactly where falsified data would hide.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — OT, IoT and cyber-physical security: methods II

### Learning outcomes

You will (1) apply a simple threat-modelling pass to the logger system; (2) assess an IoT product against ETSI EN 303 645 provisions; (3) review vendor documentation for security claims; and (4) record assumptions that the model depends on.

### 16.1 A quick threat-modelling pass

Draw the logger system: loggers → radio → GW-LOG → firewall → vendor cloud → web portal used by the quality manager. At each arrow ask: can someone pretend to be the sender, change the data, read it, block it, or gain more control than intended? This prompt list, adapted from STRIDE, produces a short threat list in under an hour.

Priya's pass at NCS produced, among other entries, "radio replay of old readings", with the assumption that an attacker would need to be within about 100 m of the loggers.

### 16.2 Product baseline questions

ETSI EN 303 645 gives concrete questions for each IoT product: does it ship with a universal default password (5.1)? Does the vendor publish a way to report vulnerabilities (5.2)? Can its software be updated securely (5.3)? Does it communicate securely (5.5)? Is personal data protected (5.8)? The answers can come from documentation, a vendor questionnaire and, for some items, a bench check.

The logger vendor's answers to Priya's questionnaire: unique per-device passwords on labels (5.1 met), a disclosure page (5.2 met), signed updates applied only remotely by the vendor (5.3 met with a dependency), and TLS to the cloud but an unencrypted radio link (5.5 partly met).

### 16.3 Reading vendor claims

"Bank-grade encryption" is not an answer to 5.5; "TLS 1.2 or later with server certificate validation, certificates pinned to the vendor CA" is. Ask for specifics, and note when the vendor cannot provide them.

The NCS logger vendor's answer for 5.5 was specific enough to act on: TLS to the cloud, but no encryption on the radio link between loggers and GW-LOG. That "partly met" is more useful than a confident marketing phrase, because it tells Priya exactly where the compensating control must go: comparing logger readings with PLC probes, as in Chapter 18. A vendor who could only say "secure communication" would have left the radio link unexamined.

### 16.4 Assumptions

Threat models rest on assumptions: the radio link range is about 100 m; the portal uses MFA; the vendor's cloud is operated securely. Write them down; if one proves false, revisit the model.

Priya's list for the logger system includes the roughly 100 m radio range, which defines who can attempt a replay of old readings; the vendor's statement that it applies signed updates remotely, on which 5.3 depends; and the quality manager's portal using MFA, which she had not verified. If the portal turned out to have no MFA, "cloud account compromise" would move up her list, so the assumption is marked to be checked at the next vendor review.

### Worked example (synthetic NCS)

Priya's vendor questionnaire returns: unique per-device password printed on the label (5.1 met); disclosure policy page exists (5.2 met); firmware updates signed but applied only by the vendor remotely (5.3 met with a dependency); TLS to cloud, but the radio link between loggers and gateway is unencrypted (5.5 partly met). Her threat list gains "radio replay of old readings" with the assumption "attacker within ~100 m".

> **Synthetic case — Northgate Cold Storage.** The vendor's answers are invented.

### Errors and limits

Questionnaire answers are claims; verify the most important ones. ETSI EN 303 645 targets consumer IoT; for industrial gateways IEC 62443-4-2 may be the better reference.

### Exercises

- **EX046 — STRIDE prompts at the portal.** Give one spoofing and one information-disclosure threat for the quality manager's portal. *Rubric:* 3 = two plausible threats; 2 = one; 1 = generic; 0 = none.
- **EX047 — A vague claim.** Rewrite the question you would send back to a vendor who says "military-grade security". *Rubric:* 3 = specific question about protocol, versions, validation; 2 = partial; 1 = accepts claim; 0 = none.
- **EX048 — Testing one assumption.** How would you check the "about 100 m radio range" assumption safely? *Rubric:* 3 = vendor spec plus walk test with a receiver on a bench logger in permitted areas; 2 = partial; 1 = transmit to live loggers; 0 = none.

### Synthesis

Quick threat modelling, baseline questions and written assumptions let a technologist assess an IoT product in days, not months.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — OT, IoT and cyber-physical security: tooling

### Learning outcomes

You will (1) choose safe tools for OT observation; (2) configure a passive capture on a mirror port; (3) use offline analysis tools on capture files; and (4) control tool use through permits and change records.

### 17.1 Passive first

Passive tools listen; active tools send. In OT, passive tools are the default because active probes can upset old devices. NIST SP 800-82r3 discusses the risk of active scanning in OT environments and the value of passive monitoring. A mirror (SPAN) port on the control-zone switch copies traffic to a monitoring laptop or sensor without changing the traffic itself.

Priya's capture used port 24 on control-zone switch SW-C, mirroring ports 1–8 where the PLCs, HMI-C and HIST connect.

Mirroring needed only a configuration change on SW-C, made by the network owner, with no device on ports 1–8 restarted.

### 17.2 Setting up a capture

Agree the switch port with the network owner; configure the mirror in a change window; connect a capture host whose network interface has no IP address, so it cannot transmit. Record start and end times, the switch, the mirrored ports and the packet-loss counters.

Priya's plan for NCS: SW-C port 24 mirrors ports 1–8, the capture host has IP disabled, and the capture runs 72 hours so that it includes a defrost cycle, when traffic patterns change. Loss counters are read at the start and the end, and the permit names the facilities manager as the person who can stop the work.

### 17.3 Offline analysis

Analyse captures on an isolated workstation: protocol decoders identify Modbus function codes, conversation lists show who talks to whom, and simple Python scripts like those in Chapters 11–12 compare results with the inventory and flow matrix.

Priya's 72-hour SW-C capture fed both the Chapter 11 inventory comparison and the Chapter 12 flow comparison. It also missed something: the historian's polling of PLC-R2 did not appear in the window, which is why HIST → PLC-R2 was missing from the flow matrix and the first firewall deployment in Chapter 27 had to be rolled back. Offline analysis can only report what the capture contains.

### 17.4 Controlling tools

Each tool used on site is listed in the work permit with its version and mode (passive only). Engineering tools from the contractor — PLC programming software — are not security tools; their use is the contractor's, under change control.

Priya's permit lists the capture tool and its version, passive mode only, and the switch configuration change for the mirror port, which the network owner makes.

It also lists the stop conditions: any HMI alarm the operators cannot explain, or a switch CPU warning, ends the capture, and the facilities manager is told first. A stopped capture is recorded in the evidence log with its duration.

### Worked example (synthetic NCS)

Priya's capture plan: switch SW-C port 24 mirrors ports 1–8 (PLCs, HMI-C, HIST); capture host has IP disabled; 72-hour capture to include a defrost cycle; loss counters checked at start and end. The permit lists the capture tool and version and names the facilities manager as the person who can stop the work.

> **Synthetic case — Northgate Cold Storage.** Ports and durations are invented.

### Errors and limits

A mirror port can drop packets when overloaded; check counters before trusting "nothing seen". Capture files may contain sensitive data; store them encrypted and delete on schedule.

### Exercises

- **EX049 — Why no IP address?** Explain why the capture host's interface has no IP address. *Rubric:* 3 = cannot transmit/accidentally interact with OT devices; 2 = partial; 1 = speed; 0 = none.
- **EX050 — Why 72 hours?** Justify the 72-hour capture duration. *Rubric:* 3 = include periodic events like defrost and shift changes; 2 = partial; 1 = arbitrary; 0 = none.
- **EX051 — Handling the capture file.** Write two handling rules for the capture file. *Rubric:* 3 = encrypted storage with limited access; deletion date; 2 = one; 1 = vague; 0 = none.

### Synthesis

OT tooling is passive by default, configured through change control and documented so its results can be trusted and its risks contained.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — OT, IoT and cyber-physical security: controls

### Learning outcomes

You will (1) select controls for NCS's top scenarios; (2) map them to IEC 62443-3-3 foundational requirements; (3) check each control's effect on operations; and (4) plan compensating controls where devices cannot be fixed.

### 18.1 Matching controls to scenarios

Scenario 1 (contractor remote tool misused): replace the always-on tool with supervised sessions through a jump host (FR 1 identification and authentication; FR 5 restricted data flow), and record sessions (FR 6 timely response to events). Scenario 2 (office ransomware reaches HMI-C): remove rule 9 (FR 5), allow-list applications on HMI-C (FR 3 system integrity), and keep offline backups (FR 7 resource availability).

Priya's first register entry is C-04, supervised contractor sessions, linked to scenario 1 only: it does nothing for the office-ransomware or camera scenarios, which need their own controls. Its test, an attempted session without approval that must be refused, is concrete enough for the facilities manager to repeat without her.

### 18.2 Operational effects

Ask of each control: what happens on a bad day? Supervised sessions mean the contractor waits for approval at 3 a.m.; NCS needs an on-call approver. Allow-listing may block an emergency diagnostic tool; keep a documented, monitored exception process.

NCS answered the first question with an on-call approver rota, which later went on the first page of the contractor visit pack. When the night operator tested version one of the pack, she could not find the approver's number at all, so the rota became the single most important line in it. For allow-listing, the exception process names who can approve an emergency tool and how the use is logged and reviewed afterwards.

### 18.3 Compensating controls

The temperature loggers' radio link is unencrypted and cannot be changed (Chapter 16). Compensate: compare logger data with PLC probes (detect falsification); alert on sudden step changes; ask the vendor about encrypted models at the next purchase. PLC-R2 cannot authenticate Modbus clients; compensate by allowing only HMI-C and HIST to reach it.

Priya's mini-study in Chapter 24 tests the first compensating control: on four synthetic weeks with ten injected falsifications, the two-probe comparison flagged all ten within 10 minutes.

The cloud's own alert flagged none, because the falsified values stayed within range.

### 18.4 Recording controls

A control register lists control, scenario, foundational requirement, owner, test method and last test date. Untested controls are listed as "assumed".

Priya's register lists C-04, supervised contractor sessions, as tested on 2026-04-02 and passed. Removing rule 9 is listed with its test, an attempted connection from OFFICE-7 to PLC-R2:502, expected refused. Allow-listing on HMI-C is listed as "assumed" until the vendor-tested policy is deployed and a blocked test executable is recorded. The "assumed" label keeps the register honest: management can see that the plan has more controls than evidence. Chapter 23 converts most of the assumed entries into tested ones, and one of them fails its first test.

### Worked example (synthetic NCS)

Priya's register row: "C-04 Supervised contractor sessions via jump host — scenario 1 — FR 1/FR 5/FR 6 — owner facilities manager — test: attempt session without approval, expect refusal — last test 2026-04-02 passed."

> **Synthetic case — Northgate Cold Storage.** Register entries are invented.

### 18.5 Prioritising with limited budget

NCS cannot buy everything at once. Priya orders controls by how many scenarios each one reduces and how cheap it is: removing rule 9 costs one maintenance window and reduces two scenarios, so it goes first; allow-listing needs vendor testing and goes second; replacing the loggers with encrypted models waits for the normal replacement cycle, with the compensating comparison check in place meanwhile.

The order is visible in Priya's evaluation six months later: rule 9 gone, supervised sessions tested, certificates automated, loggers not yet replaced.

### Errors and limits

Mapping to foundational requirements shows coverage, not adequacy. A control that is bypassed "temporarily" for months is not a control.

### Exercises

- **EX052 — Mapping allow-listing.** Which foundational requirement does HMI application allow-listing support? *Rubric:* 3 = FR 3 system integrity with reason; 2 = FR only; 1 = FR 4; 0 = none.
- **EX053 — A bad-day check.** Describe the bad-day effect of supervised sessions and its mitigation. *Rubric:* 3 = night delay; on-call approver; 2 = one; 1 = vague; 0 = none.
- **EX054 — Compensating for PLC-R2.** List two compensating controls for PLC-R2's lack of authentication. *Rubric:* 3 = restrict sources to HMI-C/HIST; monitor writes from other hosts; 2 = one; 1 = "add password"; 0 = none.

### Synthesis

Controls are chosen for scenarios, checked against bad days, compensated where devices cannot change, and recorded with tests.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — OT, IoT and cyber-physical security: monitoring

### Learning outcomes

You will (1) build a baseline of normal communication; (2) detect new hosts against that baseline; (3) triage alerts with operations; and (4) tune monitoring to avoid alert fatigue.

### 19.1 Baselines

OT networks are repetitive: the same devices talk to the same partners on the same schedule. That makes a baseline — the set of hosts and flows seen over a representative period — a powerful detector. Anything new is worth a look. NIST SP 800-82r3 recommends monitoring tailored to OT's predictable traffic.

```python
"""Lab 19: flag hosts not present in a 7-day baseline of synthetic flow records."""
baseline_days = {"HMI-C", "PLC-R1", "PLC-R2", "HIST", "GW-LOG"}
today = ["HMI-C", "PLC-R1", "HIST", "LAPTOP-V3", "GW-LOG", "LAPTOP-V3", "PLC-R2", "UNKNOWN-10.4.2.77"]
new = []
for h in today:
    if h not in baseline_days and h not in new: new.append(h)
print("new talkers:", new)
print("events:", len(today), "unique hosts:", len(set(today)), "new:", len(new))
```

Run with `python3 lab_talkers.py`. Verified output:

```text
new talkers: ['LAPTOP-V3', 'UNKNOWN-10.4.2.77']
events: 8 unique hosts: 7 new: 2
```

Priya's capture from SW-C supplied the baseline used in the lab: five hosts, HMI-C, PLC-R1, PLC-R2, HIST and GW-LOG, seen over seven days. Anything outside that set raises a new-talker alert, which is why the contractor's laptop and the dock printer both appear in the lab output.

### 19.2 Reading the alerts

LAPTOP-V3 appeared twice; UNKNOWN-10.4.2.77 once. The laptop is probably the contractor's (check the visit log). The unknown address is in no NCS subnet at all — that is more urgent, because it suggests a misconfigured device or a path the architecture does not include.

Both were resolved within an hour. The visit log showed the contractor on site with laptop V3 from 09:00 to 11:30, matching the alert times, so that alert was closed with the visit reference. The address 10.4.2.77 turned out to be a dock printer with an address from another site's plan.

### 19.3 Triage with operations

The analyst calls the facilities manager before acting: is a contractor on site? Did anyone add equipment? Operations context resolves most alerts in minutes. Only unexplained alerts escalate.

At NCS, both of the lab's new talkers were explained this way. The facilities manager's visit log showed the contractor on site with laptop V3 from 09:00 to 11:30, so that alert closed with the visit reference. The unknown 10.4.2.77 needed a walk to the dock, where a logistics printer was found in a camera-zone port. Neither required touching the control network. Had the visit log shown no contractor that morning, LAPTOP-V3 would have escalated at once.

### 19.4 Tuning

Expected changes — scheduled contractor visits, a new logger — should be added to the baseline through a change ticket, not silenced by a blanket rule. Review alert counts monthly; if most alerts are explained routine events, improve the change-ticket link rather than raising thresholds.

For NCS, contractor visits come with a ticket, so the visit-log link from Chapter 25's contractor pack lets LAPTOP-V3's appearance be matched automatically to an open ticket.

An alert with no matching ticket then goes to the security lead rather than being closed by the operator.

### Worked example (synthetic NCS)

The visit log shows the contractor on site with laptop V3 from 09:00 to 11:30, matching the alert times. Priya closes that alert with the visit reference. The 10.4.2.77 address belongs to a dock printer installed by the logistics team with a static address from a different site's plan; it was plugged into a camera-zone port. It is moved, re-addressed and added to the inventory.

> **Synthetic case — Northgate Cold Storage.** Hosts and the printer story are invented.

### Errors and limits

A baseline captured while compromised treats the attacker as normal. Seven days may miss monthly activity.

### Exercises

- **EX055 — Extending the baseline.** If LAPTOP-V3 is added to `baseline_days`, what does the lab print as new talkers? *Rubric:* 3 = ['UNKNOWN-10.4.2.77'] and new: 1; 2 = list only; 1 = unchanged; 0 = none.
- **EX056 — Why the unknown address is urgent.** Explain in two sentences. *Rubric:* 3 = outside any NCS subnet, implies unplanned path or misconfiguration; 2 = partial; 1 = vague; 0 = none.
- **EX057 — Tuning without blinding.** Propose how scheduled contractor visits should stop generating unexplained alerts. *Rubric:* 3 = visit ticket adds laptop to time-bounded allow-list/annotation; 2 = partial; 1 = ignore laptops; 0 = none.

### Synthesis

Baselines turn OT's regularity into detection; triage with operations and change-linked tuning keep alerts meaningful.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — OT, IoT and cyber-physical security: troubleshooting

### Learning outcomes

You will (1) separate cyber causes from ordinary faults; (2) troubleshoot communication failures methodically; (3) avoid troubleshooting steps that destroy evidence; and (4) know when to stop and escalate.

### 20.1 Most faults are not attacks

When HMI-C shows stale values, the cause is usually a cable, a switch port, a failed power supply or an expired licence. Treat it as a fault first, but keep the security possibility in mind and preserve evidence while you work. Jumping to "we are hacked" wastes time; ignoring the possibility can destroy the record an investigation would need.

Priya's first stale-value fault on PLC-R2 was a patch cable with rising CRC errors; the second, a week later, was not.

### 20.2 A layered method

Work up the stack: power and link lights; switch port status and errors; IP reachability from a host on the same subnet (with permission); the protocol session (does HMI-C show a communication error code?); then application configuration. Change one thing at a time and write down each step and result.

Priya's first PLC-R2 fault followed this order: link light on, switch port showing rising CRC errors, new patch cable, errors stop, values update. She recorded the fault as physical, with the error counters as evidence. Stopping at the first layer that explained the symptom kept her from touching the PLC at all.

### 20.3 Evidence-preserving habits

Before rebooting a host that might be compromised, export its logs and note its running processes. Before replacing a device, photograph its labels and settings. A reboot clears memory that might show malware; a replacement removes the original firmware state.

When PLC-R2's values froze again a week later with no port errors, Priya compared its program against the backup before anyone restarted it, and found a difference. A restart would have run the same changed program again, so it would not have fixed anything, and it would have cleared the controller's runtime state and diagnostic buffer. The usual next step after a failed restart, downloading the backup, would have overwritten the changed program, which was the main evidence of who changed it and when. She escalated with the comparison output and the port counters attached.

### 20.4 Stop and escalate

Stop and call the security lead if you find: unknown processes or accounts, configuration changes nobody made, traffic to unknown destinations, or a device whose program differs from the backup.

At NCS, the second PLC-R2 freeze met the fourth condition: the controller's program differed from the backup, so Priya escalated instead of restarting. The same rule applied on her third site visit, when an operator asked her to "quickly reset" a frozen HMI. She declined, checked the switch port counters read-only and called the contractor, who found a failing power supply. If the freeze had had a cyber cause, the reset would have erased what the investigation needed.

### Worked example (synthetic NCS)

HMI-C shows stale PLC-R2 values. Priya checks: link light on; switch port shows rising CRC errors; a new patch cable fixes the errors and the values update. She records the fault as physical, with the error counters as evidence. A week later, PLC-R2's values freeze again with no errors on the port; this time the PLC's program comparison against the backup shows a difference, and she escalates instead of restarting the controller.

> **Synthetic case — Northgate Cold Storage.** Both events are invented.

### Errors and limits

Pinging fragile devices repeatedly can itself cause problems; keep checks light. Troubleshooting on live controllers belongs to the contractor or plant engineer.

### Exercises

- **EX058 — First three checks.** List the first three checks for stale HMI values. *Rubric:* 3 = power/link, port status/errors, protocol error on HMI (in order); 2 = two; 1 = reboot first; 0 = none.
- **EX059 — Before rebooting.** What two things do you capture before rebooting a possibly compromised HMI-C? *Rubric:* 3 = logs export and running processes/connections; 2 = one; 1 = nothing; 0 = none.
- **EX060 — The escalation trigger.** Which observation in the second event triggered escalation and why? *Rubric:* 3 = program differs from backup without a change record; possible tampering; 2 = observation only; 1 = errors; 0 = none.

### Synthesis

Troubleshoot methodically, assume faults first, preserve evidence while working, and stop the moment something has changed that nobody changed.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — OT, IoT and cyber-physical security: service integration

### Learning outcomes

You will (1) integrate OT data with business services without opening control paths; (2) design one-way or brokered data transfers; (3) secure API connections to cloud services; and (4) document integration dependencies.

### 21.1 Business wants data

Customers want temperature certificates for their stored goods; finance wants compressor energy use; the logistics system wants dock door states. Each request tempts someone to connect a business system straight to a PLC. The integration principle is: business systems read copies in the DMZ or cloud, never the control zone directly.

OFFICE-7's energy macro was this temptation in practice: it read compressor run hours straight from PLC-R2 until Priya moved it to the replica.

The macro's polling also added load on PLC-R2 at times nobody had planned for.

### 21.2 Patterns

Historian replication pushes data from the control zone to a DMZ replica (Chapter 8). For stronger guarantees, a data diode or one-way gateway allows traffic in one direction only by hardware design. For cloud services, the gateway initiates outbound TLS connections and never accepts inbound ones. Integration through files — a nightly CSV export to a shared folder — is acceptable if the share lives in the DMZ and is write-only from the control side.

At NCS, HIST pushes to the DMZ replica, and GW-LOG reaches the vendor cloud outbound only through rule 21.

### 21.3 API security

Customer certificate generation uses the logger vendor's cloud API. Use a dedicated API key per integration with least privilege (read temperatures for specific rooms), store it in a secrets vault, rotate it, and log its use. Never embed keys in spreadsheets or scripts on shared drives.

For NCS's customer certificates, the key would be scoped to reading temperatures for the rooms that customer's goods occupy, held in the vault entry referenced from the asset table, rotated at least yearly and on any staff change, and logged so that an unusual pattern, such as reads for every room, shows up. A key found in a spreadsheet on the shared drive would give anyone with the drive every room's history.

### 21.4 Dependencies

Write each integration's dependencies: the vendor cloud, DNS, certificates, the API key, the DMZ share. When one breaks, you know what else stops.

For the certificate integration at NCS: the logger vendor's cloud and its API, DNS for the cloud's name, the TLS certificate chain, the API key in the vault, and the DMZ share where the generated certificates land. LOG-03's expired certificate in Chapter 22 is a reminder that a dependency can fail quietly: the logger stopped uploading on 5 October, and the customer's certificate for that room would have had a seven-day gap without the PLC probe history in HIST.

### Worked example (synthetic NCS)

The finance team's energy macro (Chapter 12) is rebuilt: HIST pushes hourly compressor run-hours to the DMZ replica; finance's report reads the replica over HTTPS with a read-only account. The customer-certificate tool uses an API key scoped to read-only temperature data for rooms with active contracts, rotated every 90 days.

> **Synthetic case — Northgate Cold Storage.** The integrations are invented.

### Errors and limits

"Read-only" protocols can still overload a device if polled too often; poll the historian, not the PLC. Data diodes need careful configuration for protocols that expect acknowledgements.

### Exercises

- **EX061 — Choosing a pattern.** Logistics wants dock door states every minute. Which pattern and why? *Rubric:* 3 = historian/DMZ replica or one-way push, no direct PLC access; 2 = pattern only; 1 = direct poll; 0 = none.
- **EX062 — Scoping an API key.** Write the scope for the certificate tool's API key. *Rubric:* 3 = read-only, specific rooms/customers, no write/admin, rotation; 2 = partial; 1 = full access; 0 = none.
- **EX063 — An integration dependency list.** List four dependencies of the customer-certificate integration. *Rubric:* 3 = four relevant; 2 = three; 1 = one or two; 0 = none.

### Synthesis

Integration gives the business its data through copies, one-way paths and scoped credentials — never through new doors into the control zone.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — OT, IoT and cyber-physical security: automation

### Learning outcomes

You will (1) automate routine checks such as certificate expiry; (2) design automation that reports rather than changes OT systems; (3) schedule and log automated jobs; and (4) handle failures of the automation itself.

### 22.1 What to automate

Good candidates are repetitive checks with clear rules: certificate expiry, backup completion, inventory drift (Chapter 11 run weekly), flow comparison (Chapter 12 run daily on new captures). Poor candidates are actions on live controllers; those stay manual and approved.

```python
"""Lab 22: report days until expiry for synthetic IoT logger certificates."""
from datetime import date
today = date(2026, 10, 12)
certs = {"LOG-01": date(2026, 11, 2), "LOG-02": date(2027, 6, 30), "LOG-03": date(2026, 10, 5), "LOG-04": date(2026, 12, 20)}
for dev, exp in sorted(certs.items(), key=lambda kv: kv[1]):
    d = (exp - today).days
    flag = "EXPIRED" if d < 0 else "renew-now" if d <= 30 else "plan" if d <= 90 else "ok"
    print(f"{dev} expires {exp} in {d:4} days -> {flag}")
```

Run with `python3 lab_certs.py`. Verified output:

```text
LOG-03 expires 2026-10-05 in   -7 days -> EXPIRED
LOG-01 expires 2026-11-02 in   21 days -> renew-now
LOG-04 expires 2026-12-20 in   69 days -> plan
LOG-02 expires 2027-06-30 in  261 days -> ok
```

Priya's checks start with the certificate expiry check above; its first run found one expired certificate and one due for renewal.

The check reads each logger's certificate expiry from the vendor's export and sorts loggers into expired, renew-now, plan and ok. Its first run gave LOG-03 expired, LOG-01 at 21 days, LOG-04 at 69 days and LOG-02 ok at 261 days.

### 22.2 Reading the report

LOG-03's certificate expired a week ago, so that logger is probably failing to connect and readings are missing. LOG-01 has 21 days left and needs renewal now, given vendor lead times. LOG-04 should be planned; LOG-02 is fine. Sorting by expiry date puts the urgent items first.

Priya scheduled the check at 06:00 daily. Its first run opened tickets for LOG-03 and LOG-01. The vendor confirmed LOG-03 had stopped uploading on 5 October; the quality manager recorded a seven-day gap in the cloud records for that room, covered by the PLC probe history in HIST.

### 22.3 Report, do not change

The script prints and could e-mail the report; it does not renew certificates by itself. Renewal goes through the vendor's process, because an automated renewal that fails halfway could leave a logger offline.

Priya's check opens tickets; it does not act. LOG-01, with 21 days left, was renewed through the vendor's process within the week, and the ticket records the new expiry date. Had the script tried to renew LOG-03 automatically and failed halfway, NCS could have lost a second logger without knowing. Keeping the script report-only also means it needs no write access to the vendor portal, so its credentials are worth less if the management host is compromised.

### 22.4 Scheduling and logging

Run the check daily from a scheduler on a management host in the OT management VLAN, write output to a log with timestamps, and alert if the job did not run. A silent automation failure is worse than no automation, because people stop checking manually.

At NCS the job runs on the OT management host at 06:00, logs each run with its timestamp, and the scheduler raises an alert if no log line appears by 06:15. That alert matters because the certificate check is the only reason anyone looks at logger expiry dates now.

### Worked example (synthetic NCS)

Priya schedules the check at 06:00 daily. The first run triggers a ticket for LOG-03 (expired) and LOG-01 (renew now). The vendor confirms LOG-03 stopped uploading on 5 October; the quality manager records a seven-day gap in the cloud records for that room, covered by the PLC probe history in HIST.

> **Synthetic case — Northgate Cold Storage.** Dates and devices are invented.

### Errors and limits

The script uses a fixed "today" date so its output is reproducible; a production version would use the current date. Certificate dates must come from the devices or vendor, not from a manually typed table.

### Exercises

- **EX064 — Changing thresholds.** If "renew-now" applied at ≤ 60 days, which devices change status? *Rubric:* 3 = no status changes, with LOG-04 still "plan" at 69 days; 2 = right conclusion, no reason; 1 = says LOG-04 becomes renew-now; 0 = none.
- **EX065 — Using the real date.** What line change makes the script use the current date, and what is lost? *Rubric:* 3 = `today = date.today()`; reproducibility of documented output; 2 = one; 1 = vague; 0 = none.
- **EX066 — Detecting a silent failure.** Describe how NCS would notice if the 06:00 job stopped running. *Rubric:* 3 = heartbeat/expected-log check alerts when no run recorded by deadline; 2 = partial; 1 = "someone notices"; 0 = none.

### Synthesis

Automate checks that report clearly and fail loudly; keep changes to OT devices in human, approved hands.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — OT, IoT and cyber-physical security: evaluation

### Learning outcomes

You will (1) evaluate whether controls achieved their purpose; (2) design simple tests with expected results; (3) measure before and after; and (4) report effectiveness honestly, including failures.

### 23.1 Did it work?

After six months of changes at NCS — rule 9 removed, supervised contractor sessions, camera zone, certificate automation — management asks whether the site is "more secure". An evaluation answers narrower, testable questions: is the office → control path closed? Do contractor sessions require approval? Are certificates renewed before expiry?

Each question maps to a control in Priya's register and to a test that can fail. Asking "is NCS more secure?" would invite a yes that nobody could check; asking whether OFFICE-7 can still reach PLC-R2:502 invites a refused connection in a firewall log, which anyone can check.

### 23.2 Tests with expected results

For each control, write the test and the expected result before running it: "From OFFICE-7, attempt a TCP connection to PLC-R2:502 in the maintenance window; expected: refused at the firewall and logged." "Contractor attempts to connect without approval; expected: jump host denies." Tests that touch the control zone are run in maintenance windows with operations informed.

Priya's table had six such tests with expected results written first. Five passed. The sixth found the camera-zone rule letting CAM-DOCK reach HIST on a web port, because a broad "camera to server" rule had been written instead of one naming the video recorder.

### 23.3 Before and after

Measures that existed before changes give a comparison: unapproved flows per week (before: 2 types; after: 0), HMI accounts belonging to leavers (before 2; after 0), days of logger data lost to expired certificates (before 7 in one incident; after 0 in six months).

All three measures existed before the changes because Priya's earlier work produced them: the Chapter 12 flow comparison counted the unapproved flows, the Chapter 7 review counted the leaver accounts and the Chapter 22 check dated the LOG-03 gap. Without that baseline, the six-month evaluation could only have said that the problems were not seen now.

### 23.4 Honest reporting

Report what failed. If one contractor still used the cellular router (Chapter 14) because it was switched on for an emergency and never switched off, say so, with the corrective action. Evaluations that report only successes stop being believed.

Priya's evaluation reports its one failure the same way: the camera-zone rule allowed CAM-DOCK to reach HIST on a web port; the corrective action narrows the rule to the video recorder only, and a retest is scheduled. Reporting five of six as five of six is what makes the five believable.

### Worked example (synthetic NCS)

Priya's evaluation table: six controls, six tests, five passed. The failure: the camera-zone firewall allowed CAM-DOCK to reach HIST on a web port because of a broad "camera to server" rule. Corrective action: narrow the rule to the video recorder only; retest scheduled.

> **Synthetic case — Northgate Cold Storage.** Results are invented.

### Errors and limits

A passed test shows the control worked at test time for that case; drift can undo it. Before-and-after counts can change for reasons other than the control.

### Exercises

- **EX067 — Writing a test.** Write the test and expected result for "only HMI-C and HIST can reach PLC-R1". *Rubric:* 3 = test from a non-approved host plus approved host, expected outcomes, window; 2 = one side; 1 = vague; 0 = none.
- **EX068 — Interpreting a before/after count.** Unapproved flows fell from 2 types to 0. Name one reason other than the controls. *Rubric:* 3 = observation window/capture placement changed or seasonal activity absent; 2 = vague; 1 = minimal attempt; 0 = none.
- **EX069 — Reporting the failure.** Write the evaluation line for the camera rule failure. *Rubric:* 3 = test, result, cause, corrective action, retest date; 2 = three; 1 = "minor issue"; 0 = none.

### Synthesis

Evaluation turns "more secure" into specific tests with expected results, compared before and after, with failures reported as plainly as passes.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) frame a small applied research question from operational practice; (2) choose data and a method that fit; (3) define a measure and a comparison; and (4) find and use credible sources.

### 24.1 Questions from practice

Applied research at technologist level answers a question someone at the site actually has. "Does comparing logger data with PLC probes detect falsified readings faster than the cloud's own alert?" is such a question; it is specific, measurable on recorded or synthetic data, and its answer changes what NCS does.

Priya's mini-study takes that question: four synthetic weeks of anteroom data with ten injected falsifications, comparing her two-probe check with the cloud's own high-temperature alert.

The hypothesis is that falsified readings that stay within range are invisible to a threshold alert.

### 24.2 Data and method

Use historical data the owner provides, or synthetic data with realistic properties, and say which. A method can be as simple as replaying recorded weeks with injected falsifications and measuring how long each check takes to flag them. The method must be repeatable by someone else.

Priya's method was this replay: four synthetic weeks of anteroom readings, with ten falsifications injected at known times, run through both the two-probe comparison and the cloud's high-temperature alert. She labels the data synthetic in every table and keeps the injection script, so someone else can regenerate the same weeks.

### 24.3 Measures and comparisons

Choose measures before running: time to detect, false alerts per week. Compare against the current practice (the cloud alert) rather than against nothing. Report counts: "detected 9 of 10 injected falsifications; 1 false alert in 4 weeks".

Priya's result fits this pattern: the two-probe comparison with a 2 °C tolerance flagged all ten falsifications within 10 minutes; the cloud's alert flagged none, because the falsified values stayed in range. She also needs the false-alert count for the two-probe check over the four weeks, without which the comparison is incomplete. Her stated limitation is that synthetic noise is simpler than real door openings, which may cause disagreements between probes.

### 24.4 Sources

Use primary and peer-reviewed sources. Giraldo et al. (2018, *ACM Computing Surveys*, doi:10.1145/3203245) survey physics-based attack detection — the idea of checking sensor data against physical expectations, which is what comparing two independent probes does. NIST SP 800-82r3 gives programme context. Vendor blog posts are background, not evidence.

Priya's study cites Giraldo et al. to frame the two-probe check as a simple physics-based consistency test, not as proof that it works at NCS. Her evidence for that is her own four-week result.

### Worked example (synthetic NCS)

Priya's mini-study uses four synthetic weeks of anteroom data with ten injected falsifications. The two-probe comparison (tolerance 2 °C) flags all ten within 10 minutes; the cloud's high-temperature alert flags none, because the falsified values stay in range. She reports the limitation: synthetic noise is simpler than real door-opening patterns.

> **Synthetic case — Northgate Cold Storage.** Data and results are invented.

### Errors and limits

Small studies support local decisions, not general claims. Do not tune the tolerance on the same injected cases you report.

### Exercises

- **EX070 — Turning curiosity into a question.** Rewrite "are our loggers any good?" as an applied research question. *Rubric:* 3 = specific measure, data, comparison; 2 = two; 1 = vague; 0 = none.
- **EX071 — Choosing a comparison.** Why compare the two-probe check with the cloud alert rather than with "no check"? *Rubric:* 3 = shows improvement over current practice; realistic decision; 2 = partial; 1 = vague; 0 = none.
- **EX072 — Using Giraldo et al.** State how the survey relates to Priya's study. *Rubric:* 3 = physics-based/consistency checks frame; survey for context and methods, not proof; 2 = partial; 1 = cites as proof; 0 = none.

### Synthesis

Applied research asks a real site question, measures against current practice and leans on sources that can be checked.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) plan a team project with roles and milestones; (2) run short design reviews; (3) manage scope and dependencies; and (4) produce a deliverable a site can use.

### 25.1 The studio project

Teams of three take one NCS improvement from idea to deliverable in six weeks. This cohort's brief: a "contractor visit pack" — the procedure, forms and checks that let a refrigeration contractor do remote or on-site work securely without slowing repairs.

Priya's team took this brief, and its first version failed the most important test: the night operator.

Version one took the contractor 14 minutes to complete, and the night operator could not find who to call for approval. The team had six weeks, three owners and a weekly review with the facilities manager, which is where that failure was reported and acted on.

### 25.2 Roles

One student owns the procedure text, one the technical checks (jump-host configuration, visit-log integration with monitoring from Chapter 19), one the user test with a real contractor and operator. Each role has a named reviewer from the site. Shared work lives in one versioned folder.

In Priya's team, the user-test owner ran the session with the contractor and the night operator that exposed the 14-minute form. The technical-checks owner tied the visit log to the Chapter 19 new-talker alerts, so a contractor laptop on site during a ticket is expected rather than flagged.

### 25.3 Reviews

Weekly 20-minute reviews follow one format: what changed, what we learned, what we need, what is at risk. The site reviewer can stop work that would affect operations.

At NCS the site reviewer was the facilities manager, and the format worked in week three, when the team reported the 14-minute test result under "what we learned" and the missing approver number under "what is at risk". The review decided to put the approver rota on the first page before any more procedure text was written.

### 25.4 Scope and dependencies

The pack depends on the jump host existing and the on-call approver rota (Chapter 18). If either slips, the team writes the pack against the agreed design and marks the dependency, rather than inventing a workaround.

In Priya's team the dependency was real: the jump host was still being configured when the pack was drafted. The pack therefore describes the agreed design, sessions through the jump host enabled per ticket, and marks the jump-host steps "pending C-04 deployment" rather than describing a temporary workaround through the desktop-sharing tool that the project was meant to remove.

### 25.5 Usable deliverables

Test with the people who will use it. If the contractor cannot complete the visit form in under five minutes at 3 a.m., it will be skipped.

Priya's team learned this directly. The first version of the contractor visit pack took 14 minutes to complete, and the night operator could not find the approver's number. Version two put the approver rota on the first page, cut the form to six fields and pre-filled site details. The retest took four minutes, and the contractor asked for a copy to use at another site, which is the best evidence a usability test can produce.

### Worked example (synthetic NCS)

Priya's team tests the pack with the contractor and the night operator. The first version took 14 minutes to complete; the operator could not find the approver's number. Version two puts the approver rota on the first page, cuts the form to six fields and pre-fills site details. The retest takes four minutes, and the contractor asks for a copy for another site.

> **Synthetic case — Northgate Cold Storage.** The team, pack and timings are invented.

### Errors and limits

Teams under-estimate review time; plan for it. A pack that is not owned by the site after handover will decay.

### Exercises

- **EX073 — A review report.** Write the four-line weekly review for week 3. *Rubric:* 3 = changed, learned, need, risk all specific; 2 = three; 1 = vague; 0 = none.
- **EX074 — Handling a slipped dependency.** The jump host is delayed four weeks. What does the team do? *Rubric:* 3 = write against design, mark dependency, inform site, no workaround; 2 = partial; 1 = invent workaround; 0 = none.
- **EX075 — Measuring usability.** Propose two measures for the user test. *Rubric:* 3 = completion time and errors/missed steps (or user rating); 2 = one; 1 = "feedback"; 0 = none.

### Synthesis

Studio work succeeds when roles, reviews and dependencies are explicit and the deliverable is tested by the people who must use it.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — OT, IoT and cyber-physical security: operational handoff

### Learning outcomes

You will (1) define what a security improvement must hand over to operations; (2) check a handoff package for completeness; (3) transfer ownership with sign-off; and (4) plan the first months after handoff.

### 26.1 Projects end, systems continue

The firewall changes, monitoring and contractor pack only protect NCS if someone operates them after the project team leaves. A handoff transfers knowledge, documents and responsibility from the project to the people who run the site day to day.

```python
"""Lab 26: check a synthetic operational handoff package for required items."""
REQUIRED = ["asset list", "flow matrix", "runbook", "contacts", "backup location", "open risks", "restore test date"]
package = {"asset list": "v3", "flow matrix": "v2", "runbook": "v1", "contacts": "", "backup location": "NAS-OT/backups", "open risks": "3 items"}
missing = [r for r in REQUIRED if not package.get(r)]
print(f"present {len(REQUIRED)-len(missing)}/{len(REQUIRED)}; missing: {missing}")
print("handoff", "BLOCKED" if missing else "ready")
```

Run with `python3 lab_handoff.py`. Verified output:

```text
present 5/7; missing: ['contacts', 'restore test date']
handoff BLOCKED
```

At NCS the receiving owner is the facilities manager, and the people running it are the night operators who will see the alerts first.

Priya's handoff checklist has seven items; the first run found five present and marked the handoff BLOCKED.

### 26.2 Reading the check

The package lacks contacts and a restore-test date. Missing contacts mean that at 3 a.m. nobody knows whom to call for the jump host or the logger vendor. Missing restore evidence means the backup in the package might not work. Both block handoff because each one fails exactly when the site needs it.

Priya fixed both before sign-off: she added a contacts sheet listing the approver rota, contractor, logger vendor, internet provider and security lead, and restored HIST into an isolated VM, recording 2026-10-09 as the test date. The rerun showed 7/7 items present.

### 26.3 Sign-off

The receiving owner — the facilities manager — signs that they understand each item and accept responsibility. Sign-off without a walkthrough is a signature, not a handoff; walk through the runbook together and let the operator perform one task while you watch.

Priya's walkthrough with the night operator found what a document review had missed: the runbook referred to a menu that the HMI vendor had renamed. The step was corrected before sign-off. That single correction would have cost a confused operator many minutes during a real alert, at an hour when nobody from the project team would answer the phone.

### 26.4 Hypercare

For the first four weeks, the project team remains on call, reviews alerts with operations weekly and fixes documentation gaps found in real use. Then responsibility moves fully to the site.

At NCS the four weeks would cover at least one contractor visit, so the visit pack, the jump-host approval and the new-talker link are all exercised once in real use. Weekly reviews look at the drift checker's report and the certificate tickets with the facilities manager. Gaps found go into the runbook the same week, and the end of hypercare is recorded in the handoff file with the list of corrections made.

### Worked example (synthetic NCS)

Priya adds the contacts sheet (approver rota, contractor, logger vendor, internet provider, security lead) and performs a restore test of HIST into an isolated VM, recording 2026-10-09 as the date. The rerun shows 7/7 items present. During the walkthrough, the night operator finds that the runbook refers to a menu that the HMI vendor renamed; the step is corrected before sign-off.

> **Synthetic case — Northgate Cold Storage.** The package contents are invented.

### Errors and limits

A complete checklist does not prove quality; the walkthrough does. Contacts go stale quickly; give them a review date.

### Exercises

- **EX076 — After adding contacts only.** If only `"contacts": "sheet v1"` is added, what does the lab print? *Rubric:* 3 = present 6/7, missing restore test date, BLOCKED; 2 = one line right; 1 = ready; 0 = none.
- **EX077 — Why contacts block handoff.** Explain in one sentence. *Rubric:* 3 = in an incident nobody knows whom to call; failure at the critical moment; 2 = partial; 1 = vague; 0 = none.
- **EX078 — Designing a walkthrough task.** Choose one task the operator should perform during the walkthrough and justify it. *Rubric:* 3 = specific, frequent or critical task (approve contractor session/check alert); 2 = task only; 1 = read the document; 0 = none.

### Synthesis

A handoff is complete when the package is whole, the owner has walked through it and signed, and a short hypercare period has caught what documents missed.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) plan the deployment of a security change in an OT site; (2) define validation checks and rollback; (3) coordinate with operations and contractors; and (4) record the deployment as evidence.

### 27.1 The change

NCS will deploy the new control-zone firewall rule set that replaces rule 9 with explicit flows. The change is small in text but large in effect: if a needed flow is missing, an HMI could lose its PLC values or the historian could stop recording.

Priya's first deployment proved the point: the matrix lacked the historian's polling of PLC-R2, and HIST lost those tags four minutes after the change.

The flow had not appeared during the 72-hour capture window, and nobody had listed it from memory. The rollback plan, rehearsed beforehand, is what turned that gap into a five-minute interruption instead of a lost morning of temperature records.

### 27.2 The plan

Pre-requisites: approved flow matrix (Chapter 12); rules reviewed by a second person; tested on a bench firewall with replayed traffic; maintenance window agreed for a low-load period; contractor on call. Steps: back up the current rule set; apply the new set; validate; monitor for 24 hours. Rollback: restore the backup, which takes two minutes and is rehearsed.

Priya's deployment used this plan on a Tuesday at 06:00. At 06:04 HIST stopped receiving PLC-R2 tags; she rolled back at 06:09 and values recovered. The missing flow was added with the historian vendor's confirmation, and the second deployment on Thursday passed all four validation checks.

### 27.3 Validation checks

Defined in advance and observable: HMI-C shows live values from both PLCs; HIST records new data points for every tag group; GW-LOG uploads succeed; the test from OFFICE-7 to PLC-R2:502 is refused and logged. Any failure in the first three triggers rollback unless fixed within ten minutes.

On the Tuesday attempt the second check failed: HIST stopped recording PLC-R2's tag group at 06:04. Because the failure was understood but not fixable within ten minutes, Priya rolled back at 06:09 rather than editing rules live. The fourth check is the security one; it passed both times, which shows that a rule set can be secure and still break operations.

### 27.4 Recording

Record times, who did what, the hash of old and new rule sets, validation results and any deviations. This record is evidence for the evaluation in Chapter 23 and for future audits.

Priya's record for the two deployments shows the value of this: the Tuesday entry lists the 06:04 failure, the 06:09 rollback and the missing HIST → PLC-R2 flow as the cause; the Thursday entry lists the corrected rule set's hash and four passed checks. The Chapter 23 evaluation cites both, and an auditor reading it later can see that the first attempt failed safely, which is itself evidence that the rollback works.

### Worked example (synthetic NCS)

Deployment on Tuesday 06:00. At 06:04 HIST stops receiving PLC-R2 tags: the matrix listed HIST → PLC-R1 only, because historian polling of PLC-R2 had been missed in the observation window. Priya rolls back at 06:09, values recover, and the missing flow is added to the matrix with the historian vendor's confirmation. The second deployment on Thursday passes all four checks.

> **Synthetic case — Northgate Cold Storage.** The timeline is invented.

### Errors and limits

Bench testing cannot reproduce every device behaviour. Validation only covers what you thought to check; keep monitoring after the window.

### Exercises

- **EX079 — Ordering the steps.** Put in order: validate, apply new rules, back up current rules, monitor 24 h. *Rubric:* 3 = back up, apply, validate, monitor; 2 = one swap; 1 = random; 0 = none.
- **EX080 — Why the HIST flow was missed.** Explain how the missing flow got past the matrix and how to prevent it next time. *Rubric:* 3 = observation window/historian polling not captured; confirm with owners and longer captures; 2 = one; 1 = blame; 0 = none.
- **EX081 — A rollback criterion.** Write the rollback criterion for the GW-LOG check. *Rubric:* 3 = uploads failing for > 10 minutes after change → rollback; 2 = vague timing; 1 = minimal attempt; 0 = none.

### Synthesis

Deployment in OT is planned, validated against pre-defined checks, reversible within minutes and recorded as evidence — and rollback is a success, not a failure.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) work safely on an industrial site under supervision; (2) follow site rules for permits, PPE and lock-out; (3) communicate with operators, contractors and managers; and (4) reflect on field experience.

### 28.1 Site safety first

An ammonia refrigeration plant has hazards a computing student may not expect: toxic gas, moving machinery, cold rooms where exposure is limited, forklifts on the dock. Before any visit: site induction, required PPE, knowledge of alarm signals and muster points, and an escort. Never enter the machine room without the refrigeration engineer's permission.

Priya's visits always start at the gatehouse induction, and she enters the machine room only with the contractor or refrigeration engineer.

The induction covers ammonia alarms and muster points, which apply to her as to anyone.

### 28.2 Permits and lock-out

Work on panels may require a permit-to-work and, for electrical isolation, lock-out/tag-out by qualified staff. A technologist reading a front-panel display may need an escort; touching anything inside a live panel is not part of the role.

At NCS, Priya read PLC-R2's version from its front-panel display with the contractor beside her; that is observation, not work on the panel. The MP-2 cellular router was photographed, not unplugged: removing it was the facilities manager's decision, made after the contractor confirmed what it was for.

### 28.3 Communication

Operators know the plant; listen first. Explain what you will do, how long it takes and how it could affect them. Before leaving, tell the shift lead what you did and what you found that matters to them today.

On her third visit, when an operator asked her to reset a frozen HMI, Priya explained why she would not and what she could do instead: check the switch port counters, which was permitted read-only, and call the contractor. Before leaving, she told the shift lead the cause, a failing power supply, and that no security issue had been found.

### 28.4 Reflection

After each visit, write: what I did, what I observed, what I would do differently, and any safety or ethical question. Reflection is assessed in this chapter because it is how field judgement grows.

Priya's entry for her third visit might read: did, checked switch port counters for a frozen HMI and called the contractor; observed, a failing power supply as the cause, confirmed by the contractor; differently, ask on arrival who handles HMI faults on that shift; ethical question, the operator's request that she reset the HMI as "the IT person", which she declined because a reset could destroy evidence and was not her task under the site procedure. Assessors look for the last line most.

### Worked example (synthetic NCS)

On Priya's third visit an operator asks her to "quickly reset" a frozen HMI because she is "the IT person". She declines: HMI resets are the operator's or contractor's task under the site procedure, and a reset might destroy evidence if the freeze has a cyber cause. She helps by checking the switch port counters (permitted read-only) and calls the contractor, who finds a failing power supply.

> **Synthetic case — Northgate Cold Storage.** The visit is invented.

### Errors and limits

Field placements vary; follow the host's rules even where they differ from this book. Reflection notes must not include customer data or credentials.

### Exercises

- **EX082 — Pre-visit checklist.** List four things to have before entering NCS's machine room. *Rubric:* 3 = induction, PPE, escort/permission, alarm/muster knowledge; 2 = three; 1 = laptop; 0 = none.
- **EX083 — Declining the reset politely.** Write what Priya says to the operator. *Rubric:* 3 = declines, explains role and evidence reason, offers help, calls right person; 2 = partial; 1 = refuses curtly; 0 = resets.
- **EX084 — A reflection entry.** Write the "what I would do differently" line for that visit. *Rubric:* 3 = specific, actionable improvement; 2 = vague; 1 = minimal attempt; 0 = none.

### Synthesis

Field practice builds the habits that keep people safe and keep the plant trusting security staff: preparation, staying in role, clear communication and reflection.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) build a capstone artefact that solves a defined NCS problem; (2) work in increments with tests; (3) keep a decision log; and (4) prepare the artefact for assessment and handover.

### 29.1 The capstone brief

Priya's capstone: an "OT drift checker" that runs weekly on NCS's management host, combining the Chapter 11 inventory comparison, the Chapter 12 flow comparison, the Chapter 19 new-talker check and the Chapter 22 certificate check into one report with a single exit status. It reads exported files only and never contacts devices.

Each of the four checks already exists and has been run on NCS data; the capstone's work is combining them, validating their inputs and making the result something the facilities manager can run without Priya.

### 29.2 Increments

Week 1: one script that runs the four checks on sample files and prints sections. Week 2: a common output format (check, item, status, evidence file). Week 3: tests for each check using small fixtures, including empty inputs. Week 4: scheduling, logging and the "job did not run" alert. Each increment works end to end before the next begins.

Week 3 found a real defect: an empty capture file made the new-talker check report every baseline host as missing rather than "no data". Priya added a "no-data" status that fails the run, because an empty input usually means the capture failed.

### 29.3 Decision log

Examples: "Decision 3 — report exit status non-zero if any check returns UNAPPROVED, EXPIRED or VERSION-CONFLICT; alternative (always zero) rejected because the scheduler could not alert." "Decision 5 — no automatic remediation; all actions via tickets."

A further decision came from week 3: "Decision 6 — an empty input file produces status NO-DATA and a non-zero exit; alternative (treat as zero events) rejected because it reported every baseline host as missing, and an empty capture usually means the capture failed." Each entry names the alternative and the reason it lost, so an assessor can disagree with the reason rather than guess at it.

### 29.4 Ready for assessment

The artefact folder contains the code, tests, sample inputs, a README with how to run it, the decision log and a short operations guide. An assessor must be able to run it from a clean checkout and get the documented output.

Priya's folder met this with 23 tests that pass from a clean checkout. The operations guide is where her assessor later found the gap: the facilities manager could run the checker but still needed help to interpret VERSION-CONFLICT.

A reviewer can follow every status from the input files to the report without asking her.

### Worked example (synthetic NCS)

At week 3 Priya's tests reveal that an empty capture file makes the new-talker check report every baseline host as missing rather than "no data". She adds a "no-data" status that fails the run, because an empty input usually means the capture failed — exactly what the site needs to know.

> **Synthetic case — Northgate Cold Storage.** The capstone is a teaching example.

### Errors and limits

Combining checks multiplies the ways input files can be wrong; validate inputs first. A tool that only Priya can run is not finished.

### Exercises

- **EX085 — Choosing exit statuses.** Which statuses should make the drift checker exit non-zero? *Rubric:* 3 = UNAPPROVED, EXPIRED, VERSION-CONFLICT, no-data (any problem); 2 = some; 1 = vague; 0 = none.
- **EX086 — A test fixture.** Describe a fixture that tests the certificate check's boundary at 30 days. *Rubric:* 3 = cert exactly 30 days out expects renew-now, 31 expects plan; 2 = one; 1 = vague; 0 = none.
- **EX087 — Why no auto-remediation?** Justify decision 5 in two sentences. *Rubric:* 3 = actions on OT need approval/context; automated mistakes could stop operations; 2 = one; 1 = vague; 0 = none.

### Synthesis

A capstone build is small increments, tests at the edges, logged decisions and an artefact someone else can run.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) assess a capstone against its brief and criteria; (2) present results to technical and site audiences; (3) answer questions about limitations; and (4) plan your next learning steps.

### 30.1 Criteria

The capstone is assessed on: problem fit (does it address an NCS need?), technical correctness (do tests pass and outputs match?), safety and authorization (read-only, no device contact, documented scope), usability (can the site run it?), and honesty (are limitations stated?). Each scored 0–3 with written evidence.

Priya scored herself 3, 3, 3, 2 and 3 on these, with usability at 2 because interpreting VERSION-CONFLICT still needed help. The assessor agreed on every criterion and suggested a plain-language "what to do" column for each status.

The column was added before the final submission.

### 30.2 Demonstration

Run the tool live from a clean checkout on sample inputs, then show the report from a real (owner-approved, sanitized) week. Narrate one finding from the report to resolution: the drift checker flagged a VERSION-CONFLICT for a logger gateway after a vendor update, and the inventory was corrected.

Priya's narrated finding follows the drift checker's output from VERSION-CONFLICT to a corrected inventory row, the same path PLC-R2's 2.4/2.1 conflict took by hand in Chapter 11. Showing the clean-checkout run first proves the tool works; showing the real week proves the site uses it.

### 30.3 Questions to prepare for

"What happens if the capture is from the wrong switch?" "How do you know the flow matrix is right?" "What would an attacker who knows about the checker do?" "Who maintains it after you?" Answer with evidence or with "I don't know, and here is how I would find out."

Priya's limitations page already answers two: it names capture placement, a capture from the wrong switch would show none of the PLC traffic, and baseline poisoning, an attacker present during the baseline week would be treated as normal. Her answer to "who maintains it" is the facilities manager, with the operations guide and the 23 tests.

### 30.4 Next steps

Technologists continue into bachelor's study, vendor or sector certifications, or roles in OT operations. Keep following CISA ICS advisories for the products you support and revisit NIST SP 800-82r3 and the IEC 62443 parts that apply to your role.

For a technologist leaving NCS, the products to follow are the ones in Priya's inventory: the refrigeration PLCs, HMI-C's Windows build and HMI software, GW-LOG and the loggers, and the dock cameras. A CISA advisory naming any of them should lead straight to the asset table, the firmware column and the drift checker's next run.

### Worked example (synthetic NCS)

Priya's self-assessment: problem fit 3 (site uses it weekly); correctness 3 (all 23 tests pass from clean checkout); safety 3 (read-only, permit on file); usability 2 (the facilities manager runs it, but interpreting VERSION-CONFLICT still needs help); honesty 3 (limitations page lists capture placement and baseline poisoning). The assessor agrees on every criterion, including usability at 2 for the same reason, and suggests a plain-language "what to do" column.

> **Synthetic case — Northgate Cold Storage.** Scores are illustrative.

### Errors and limits

Demonstrations on curated data can hide brittleness; include one messy input. Self-assessment tends to be generous on usability.

### Exercises

- **EX088 — Scoring honesty.** What evidence would justify a 3 for honesty? *Rubric:* 3 = explicit limitations section with specific failure modes and untested areas; 2 = brief caveat; 1 = vague; 0 = none.
- **EX089 — The attacker question.** Draft an answer to "what would an attacker who knows about the checker do?" *Rubric:* 3 = act between weekly runs or poison baseline/inventory; mitigations; 2 = partial; 1 = denies; 0 = none.
- **EX090 — The usability fix.** Write the "what to do" text for a VERSION-CONFLICT line. *Rubric:* 3 = plain steps: confirm on device with contractor, update inventory, check advisories; 2 = partial; 1 = jargon; 0 = none.

### Synthesis

A capstone assessment checks fit, correctness, safety, usability and honesty — and the best answers to hard questions name limits and next steps.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Northgate Cold Storage, Priya Nair and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** HMI-C — general-purpose: a Windows PC running many processes and updates. PLC-R2 — embedded: one control program in a fixed scan loop. Logger — embedded: a battery microcontroller with radio and no general operating system.

**EX002.** NCS loses the cloud temperature record and any remote alerts for six hours, a gap in food-safety evidence; it does not lose cooling, because the compressors are controlled by PLC-R1/R2 independently of the gateway.

**EX003.** PLC-R1 | embedded controller | runs ammonia compressors 1–2 and suction pressure control | machine room panel MP-1 | refrigeration contractor via engineering laptop | freezer warms and stock is at risk within hours.

**EX004.** 10.20.0.11 and 10.20.0.40 share the network 10.20.0 under a /24 mask, so yes. 10.20.0.11 and 10.30.0.11 differ in the third octet, so they are on different subnets and traffic must be routed.

**EX005.** "Rule 9: allow TCP 502 from 10.20.0.20 (HMI-C) to 10.20.0.11 and 10.20.0.12 (PLC-R1, PLC-R2)", with the existing final rule "deny any to any" below it. (Because HMI-C and the PLCs share a subnet, the rule only bites where traffic is routed; the key change is removing access from other subnets.)

**EX006.** With outbound-only HTTPS the gateway starts every session and the firewall drops unsolicited inbound packets, so internet hosts cannot reach the gateway's services; a port-forward lets anyone on the internet attempt to connect to it.

**EX007.** `docs - seen` = {"A"} (documented but not observed); `seen - docs` = {"D"} (observed on the network but undocumented).

**EX008.** It returns `None`. The script should print "-" for the value and a status such as "only-on-network" or "missing" rather than crash or skip the row.

**EX009.** `for name in sorted(set(docs) | set(seen)):` — looping over the union guarantees that devices present in only one source still produce an output line.

**EX010.** The painted tag identifies the function at a fixed location; it survives re-addressing (which changes IP) and hardware replacement (which changes serial number), so history and findings stay attached to the right row.

**EX011.** `select tag from loggers where room = 'Freezer-2' and gateway_tag = 'GW-LOG';`

**EX012.** Replace it with a "credential reference" column holding the vault entry ID (e.g. OT-17); the password itself lives in the access-controlled vault with logging, never in the shared table.

**EX013.** Ammonia release (harm to people) first; loss of cooling (stock loss, food safety) second; falsified temperature records (food-safety evidence and customer trust) third; camera footage leak (privacy and confidentiality) fourth.

**EX014.** The affected product and versions; the weakness described; whether exploitation has been observed; and the mitigations recommended (vendor fix or workaround).

**EX015.** T0886 Remote Services — the contractor's access uses a remote service to reach a control-system host.

**EX016.** It sits on the same storage as the VM (a storage failure or ransomware takes both), it is eight months stale, and it has never been restored, so there is no evidence it would work.

**EX017.** Anyone or any malware on the office VLAN that obtains the console credentials can stop, delete or encrypt every VM on the host, including HIST, in one action.

**EX018.** Restore the backup into a VM attached to an isolated test network with no route to production, start it, check that the historian service runs and recent data are present, then record the date, duration and result.

**EX019.** Viewer: the guard only needs to read temperatures and alarms, so least privilege rules out acknowledging alarms or changing setpoints.

**EX020.** (1) Each contractor engineer has a named account — no shared contractor login. (2) Accounts are disabled by default. (3) An account is enabled only for an approved ticket and a fixed time window, and the session is reviewed afterwards.

**EX021.** MFA required: the contractor's remote session into the OT network (and the engineering laptop's project login). Documented alternative: the control-room HMI-C console, protected by a locked room and a short screen-lock time instead of an MFA prompt during alarms.

**EX022.** The logging-and-camera zone (or a dedicated camera zone): cameras have no role in refrigeration control and often run vulnerable firmware, so placing them in the control zone would give a weak device a direct path to PLC-R1/R2.

**EX023.** Source zone: refrigeration control (HIST). Destination: DMZ (historian replica). Protocol: the historian's replication service on its fixed TCP port. Initiator: control side. Purpose: provide office reporting without office access to the control zone.

**EX024.** Allow-listing on HMI-C covers the failure of the firewall to stop malware arriving by USB; offline backups cover the failure of every preventive layer when ransomware encrypts HIST.

**EX025.** (a) Observation — a recorded state at a time. (b) Conclusion — inferred; it requires session logs or the contractor's confirmation.

**EX026.** "On 12 October, 2 of the 4 temperature-logger certificates checked were expired or due within 30 days; the other 36 loggers have not yet been checked" — using the actual count from the certificate check.

**EX027.** "Of 10 loggers checked on 4 March, 2 still accepted the vendor default password; the other 30 loggers have not yet been checked."

**EX028.** Sensor: falsify or disconnect TT-F2 so it reads colder than reality. Controller: change PLC-R1's Freezer-2 setpoint (T0836). Actuator: force compressor C-1 off through a manual override or output manipulation.

**EX029.** ETSI EN 303 645: its provisions (no universal default passwords, vulnerability disclosure, updatable software, secure communication) translate directly into purchase questions; NIST IR 8259 is a good complement for asking what the manufacturer does.

**EX030.** The loggers measure Freezer-2 independently and report by a different path; if TT-F2 is falsified to read −22 °C while the room warms, the logger data will disagree and reveal the problem.

**EX031.** HMI-C may have been idle or powered off during the observation window, or the mirror port did not see its traffic (for example, it talks to the PLCs through a switch that was not monitored).

**EX032.** PLC-R2's version conflict: it controls compressors (high consequence), and the real firmware (2.1) determines whether advisories apply, whereas the camera is low consequence for cooling.

**EX033.** `SENS-NH3  docs=-           network=fw 3.0   only-on-network` — it appears because the loop iterates over the union of both sources.

**EX034.** A new line `HMI-C -> PLC-R2 :502 approved` appears, and "approved but not seen" becomes an empty list `[]` because every approved flow has now been observed.

**EX035.** "Flow OFFICE-7 → PLC-R2:502: energy report macro reading compressor run hours. Replacement: read run hours from the historian replica in the DMZ. Block office → control on 20 March in the maintenance window after the macro is switched. Owner: Priya Nair with the facilities manager."

**EX036.** The logger gateway's only job is forwarding temperatures to the cloud, so it has no need to speak Modbus to a compressor controller. Because it is internet-connected, such a flow links an external service to the control zone.

**EX037.** "A compromised logger-vendor cloud account (threat) uses the vendor portal (path) to alter stored Freezer-2 readings (action), so food-safety records show compliance during a real excursion and spoiled stock is shipped (consequence), unless HIST's independent PLC temperature record is compared with the cloud data (safeguard)."

**EX038.** Consequence 2: a setpoint change can warm freezers and condemn stock or breach food-safety rules, but it is unlikely to harm people because ammonia safety is independent, and cloud logger alerts limit how long it goes unnoticed.

**EX039.** The cloud logger alerts appear as the safeguard for setpoint misuse and also give the second view when HMI-C is lost; NCS should monitor that the alerting path itself works (test alerts, gateway health), because many scenarios lean on it.

**EX040.** Cellular or Wi-Fi routers inside the panel; labels or notes showing passwords; devices or cables not in the inventory (for example a laptop left connected to a PLC port).

**EX041.** "Walk me through the last time you connected to NCS remotely — from your office to the moment you saw the HMI screen."

**EX042.** Option 1: remove the router if the contractor confirms the primary remote path covers all support needs. Option 2: keep it powered off and enable it only on request, approved by the facilities manager for a stated time, if a backup path is genuinely needed during network outages.

**EX043.** `excursion 15-35 min, duration 20 min, peak 8.4 C, alarm not raised (delay 25 min)` — the excursion is unchanged but 20 < 25.

**EX044.** The reading at 50 minutes starts a new excursion (`start = 50`) but the loop ends before any reading returns to ≤ 5 °C, so nothing is printed. Fix: after the loop, if `start is not None`, print the open excursion with "ongoing at last sample".

**EX045.** Compare each logger reading with the PLC's own probe recorded in HIST (or a second logger in the same room) and flag any interval where they differ by more than an agreed tolerance, such as 2 °C.

**EX046.** Spoofing: an attacker phishes the quality manager's portal password and logs in as them. Information disclosure: the portal's export function exposes temperature histories of other customers' storage if access controls are weak.

**EX047.** "Please state the protocol and version used between the gateway and your cloud, how the gateway validates the server certificate, and whether the logger-to-gateway radio link is encrypted and authenticated (and with what algorithm)."

**EX048.** Use the vendor's radio specification, then with permission place a bench logger and a receiver from the vendor's tool kit at increasing distances inside NCS's site boundary, recording where reception stops; no transmission to live loggers.

**EX049.** With no IP address the host cannot send packets onto the control network, so the capture cannot accidentally interact with or disturb the PLCs, HMI or historian.

**EX050.** Seventy-two hours spans several defrost cycles, shift changes and a weekend pattern, so periodic flows that a short capture would miss are recorded in the baseline.

**EX051.** Store the capture only on an encrypted volume accessible to the named analysts; delete it (and any copies) 90 days after the report is accepted, recording the deletion.

**EX052.** FR 3 system integrity: allow-listing prevents unauthorised software from running on HMI-C, protecting the integrity of the host that operators rely on.

**EX053.** A 3 a.m. breakdown means the contractor cannot connect until someone approves the session, delaying repair while freezers warm; mitigate with an on-call approver rota and a phone number the contractor can call.

**EX054.** Allow Modbus to PLC-R2 only from HMI-C and HIST at the firewall, and alert on any Modbus write to PLC-R2 from another source seen by passive monitoring.

**EX055.** `new talkers: ['UNKNOWN-10.4.2.77']` and the summary line becomes `events: 8 unique hosts: 7 new: 1`.

**EX056.** 10.4.2.77 is not in any of NCS's three subnets, so either a device is misconfigured or traffic is arriving by a path the architecture does not include. Either case needs prompt investigation before it becomes normal.

**EX057.** When a contractor visit is booked, the ticket records the laptop's identity and the visit window, and the monitoring tool annotates alerts from that laptop during the window as "expected – ticket N" while still logging them.

**EX058.** (1) Power and link lights on PLC-R2 and its switch port; (2) the switch port's status and error counters; (3) the communication error code or status shown on HMI-C for PLC-R2.

**EX059.** Export the Windows event logs and record the list of running processes and active network connections (with time and hash of the exported files).

**EX060.** The program comparison showed PLC-R2's logic differed from the stored backup with no change record, which could mean tampering; restarting or reloading would destroy that evidence, so escalation comes first.

**EX061.** Have the PLC's door states recorded in HIST and pushed to the DMZ replica (or a one-way export), and let the logistics system read the replica; the logistics system never connects to the control zone.

**EX062.** Read-only access to temperature series for rooms with active customer contracts; no write, configuration or user-management permissions; key stored in the vault and rotated every 90 days, with use logged.

**EX063.** The logger vendor's cloud API and its availability; the scoped API key in the vault; DNS resolution of the API host; the TLS certificate chain used by the API (and the certificate tool's server).

**EX064.** No status changes: LOG-01 (21 days) is already renew-now, LOG-04 (69 days) is still above 60 and stays "plan", LOG-02 stays ok and LOG-03 stays expired.

**EX065.** Replace `today = date(2026, 10, 12)` with `today = date.today()`. The output then changes every day, so the verified output printed in the book can no longer be reproduced exactly.

**EX066.** The job writes a "completed" line with a timestamp; a separate monitor checks at 06:15 that today's line exists and raises an alert to the OT inbox if it does not.

**EX067.** In the maintenance window, from OFFICE-7 and from GW-LOG attempt TCP connections to PLC-R1:502 — expected: refused and logged at the firewall. From HMI-C and HIST confirm normal polling continues — expected: values update on the HMI and in the historian.

**EX068.** The "after" capture may have covered a different period or switch port, or the energy macro may simply not have run that week, so fewer flows could reflect observation differences rather than the control.

**EX069.** "Test 6 (camera zone isolation) FAILED on 2 September: CAM-DOCK reached HIST on TCP 80 because rule 31 allowed cameras to any server. Corrective action: restrict rule 31 to the video recorder; retest on 16 September."

**EX070.** "Over the last 12 weeks of NCS data, what percentage of logger readings arrived in the cloud within 15 minutes, and does that percentage differ between the old and new gateway firmware?"

**EX071.** NCS already relies on the cloud alert, so the decision is whether to add the two-probe check; comparing against current practice shows the extra value, while comparing with "no check" would overstate it.

**EX072.** Giraldo et al. describe detecting attacks by checking sensor data against physical expectations; Priya's two-probe comparison is a simple instance of that idea, so the survey frames and justifies the approach without proving it works at NCS.

**EX073.** Changed: form cut to six fields with site details pre-filled. Learned: the night operator could not find the approver's number. Need: the current on-call approver rota from the facilities manager. Risk: jump-host configuration not yet tested end to end.

**EX074.** Keep writing the pack for the agreed jump-host design, mark the steps that depend on it as "pending jump host", tell the site reviewer, and do not create an interim path such as reopening the old remote tool.

**EX075.** Time for the contractor to complete the visit form (target under five minutes) and the number of steps missed or done in the wrong order during the observed test.

**EX076.** `present 6/7; missing: ['restore test date']` followed by `handoff BLOCKED`.

**EX077.** Without a contacts sheet, during a night incident the operator cannot reach the approver, contractor or vendor, so the controls fail at the moment they are needed.

**EX078.** Approving and then closing a contractor remote session through the jump host: it is the task most likely to happen at night under pressure, and watching the operator do it shows whether the runbook steps are clear.

**EX079.** Back up the current rule set; apply the new rules; validate the four checks; monitor for 24 hours.

**EX080.** The 72-hour capture or its switch port did not include the historian's PLC-R2 polling, so the flow never entered the matrix; next time, confirm every flow list with each system owner (here the historian vendor) and compare with the historian's own configuration, not only captures.

**EX081.** "If GW-LOG uploads fail (no successful upload in the vendor portal) for more than 10 minutes after the change, restore the previous rule set."

**EX082.** Completed site induction; the required PPE (for example gas monitor, cold-room clothing, safety boots); explicit permission and an escort from the refrigeration engineer; knowledge of the ammonia alarm signal and the muster point.

**EX083.** "I'm not allowed to reset the HMI — that's in the operator and contractor procedure, and if something odd caused the freeze we'd lose the evidence. I can check the network port right now and I'll call the contractor for you."

**EX084.** "Before visits I will ask the shift lead which tasks operators expect from 'IT', so I can explain my role at the start instead of in the middle of a fault."

**EX085.** Any status indicating a problem: UNAPPROVED (flow), EXPIRED or renew-now (certificate), VERSION-CONFLICT or only-on-network (inventory), new talkers, and the new no-data status for empty inputs.

**EX086.** A fixture with "today" fixed at 2026-10-12, one certificate expiring 2026-11-11 (30 days, expect renew-now) and one expiring 2026-11-12 (31 days, expect plan).

**EX087.** Changes to firewalls, devices or certificates in OT need operational context and approval, which a weekly script does not have. An automated "fix" that misfires could cut off cooling visibility or contractor access when the site needs it.

**EX088.** A limitations section that names specific failure modes (wrong capture point, baseline captured during compromise, vendor-side changes not visible), lists what was not tested, and is linked from the report's first page.

**EX089.** "They could act within the week between runs, or get their device into the baseline or inventory so it looks normal. The checker narrows the window but does not close it; daily runs, change-ticket review of baseline additions and real-time monitoring of control-zone writes reduce that gap."

**EX090.** "The device reports a different firmware version from our records. Ask the contractor or vendor to confirm the version on the device, update the inventory with the confirmed version and source, then check CISA advisories for that version."

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. DOIs were checked against Crossref.

- CISA (2021). AA21-042A: Compromise of U.S. Water Treatment Facility. <https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-042a>
- ETSI EN 303 645 V2.1.1 (2020-06). Cyber Security for Consumer Internet of Things: Baseline Requirements. <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- Giraldo, J., et al. (2018). A Survey of Physics-Based Attack Detection in Cyber-Physical Systems. ACM Computing Surveys. <https://doi.org/10.1145/3203245>
- ISA/IEC 62443 series of standards (overview; parts 3-2 and 3-3 and 4-2 are cited in the text). <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards>
- MITRE ATT&CK for ICS, including T0836 Modify Parameter, T0883 Internet Accessible Device and T0886 Remote Services. <https://attack.mitre.org/matrices/ics/>
- NIST IR 8259 (2020). Foundational Cybersecurity Activities for IoT Device Manufacturers. <https://csrc.nist.gov/pubs/ir/8259/final>
- NIST SP 800-82 Rev. 3 (2023). Guide to Operational Technology (OT) Security. <https://csrc.nist.gov/pubs/sp/800/82/r3/final>
