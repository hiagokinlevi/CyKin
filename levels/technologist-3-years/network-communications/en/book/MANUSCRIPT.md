# Network and Communications Security: Technologist Course

- Language: English (`en`); course 080, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; Five offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students who must build, operate and improve network security for small organisations with limited staff, through hands-on placement work.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only networks and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, flow records, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one technologist student on placement at a secondary school with a single IT technician, from computing, networking, scripting and data foundations through assets, flows, risk scenarios, requirements, a guided service lab, wireless and remote access, tooling, controls, monitoring, troubleshooting, supplier integration, automation and evaluation, to a team studio, operational handoff, field practice and a capstone tool. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Tomás Rivera** | Technologist student | Invented |
| **Hannah Okafor** | Lecturer | Invented |
| **Greystone Polytechnic** | Fictional polytechnic | Invented |
| **Ridgeway Secondary School** | Fictional partner (one IT technician) | Invented |

### Core sources

NIST [SP 800-41r1](https://doi.org/10.6028/NIST.SP.800-41r1), [SP 800-77r1](https://doi.org/10.6028/NIST.SP.800-77r1), [SP 800-94](https://doi.org/10.6028/NIST.SP.800-94), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-153](https://doi.org/10.6028/NIST.SP.800-153) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); [CIS Controls v8](https://www.cisecurity.org/controls/v8); IETF [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301) and [RFC 2827](https://www.rfc-editor.org/rfc/rfc2827). Full list in [References](#references).

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

You will (1) describe the parts of a computer system; (2) explain how services run on hosts; (3) relate hardware and software to security.

### 1.1 A technologist's view

Tomás Rivera starts the three-year technologist programme at the fictional Greystone Polytechnic, where courses mix theory with hands-on work for real organisations. His work placement partner later in the course is the fictional Ridgeway Secondary School, which has about 1,200 students, 110 staff and one IT technician, Gareth Pryce. His lecturer, Hannah Okafor, begins with computing systems because every network control eventually protects some computer: a laptop, a server, a printer or a switch. Understanding what those computers do makes it easier to see what the network must allow and what it should stop.

### 1.2 Hardware, firmware and software

A computer system has layers. Hardware includes processors, memory, storage and network interfaces. Firmware is low-level software built into devices that starts them and controls hardware; switches, printers and wireless access points run mostly on firmware. Operating systems manage resources and run applications, which provide the services people use. Each layer can have weaknesses and needs updates. Tomás notes that school printers and projectors run firmware nobody has updated in years, which matters because those devices sit on the same network as student laptops and could be misused if they have known flaws.

### 1.3 Services and clients

Many systems act as servers, offering services that clients use. The school's file server offers shared folders, the web server hosts the school's site, and the print server accepts print jobs. Each service listens on a network port and waits for requests. Clients, such as student laptops, start connections to those services. Tomás learns to describe each system by the services it offers and the clients it serves, because network rules are written in exactly those terms: which clients may reach which services on which ports, and which may not.

### 1.4 Why inventory comes first

Tomás cannot protect systems nobody has listed. With Gareth's permission, he begins an inventory of the school's main systems: servers, switches, access points, printers and projectors, with their roles, locations and owners. The CIS Controls put inventory of enterprise assets first because every later safeguard depends on it. Within a day, the inventory reveals a small server in the science department that nobody remembers setting up. Gareth investigates and finds an old data-logging system, still running and still connected to the student network, which goes on the list for review.

### Worked example

Tomás's first inventory lists 14 servers and network devices, including one forgotten science department server.

> **Synthetic case.** The school and devices are synthetic.

### Errors and limits

Assuming devices like printers need no updates leaves known weaknesses on busy networks.

### Exercises

- **EX001 — Firmware devices.** Why do printer and projector firmware matter for network security? *Rubric:* 3 = run outdated firmware on shared network, could be misused;; 2 = outdated;; 1 = not relevant;; 0 = none.
- **EX002 — Service description.** How should a system be described for writing network rules? *Rubric:* 3 = by services offered, ports and clients served;; 2 = services;; 1 = hardware;; 0 = none.
- **EX003 — Forgotten server.** What did the inventory reveal in the science department? *Rubric:* 3 = forgotten data-logging server on student network;; 2 = old server;; 1 = nothing;; 0 = none.

### Synthesis

Knowing what systems exist and what services they offer is the starting point for network security.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain addressing, routing and common services; (2) describe how the school reaches the internet; (3) identify key dependencies.

### 2.1 Local networks and addressing

Devices on a network have IP addresses, and groups of addresses form subnets. Tomás examines the school's addressing and finds that almost everything, from student laptops to the finance office, sits in one large subnet. A router connects this subnet to the internet through the school's provider. Within one subnet, devices can usually talk to each other directly without passing any filtering device. This explains why a student laptop can currently see the finance office's shared printer, a small example of a much wider problem the course will address.

### 2.2 Routing and gateways

When a device sends traffic to an address outside its own subnet, it sends it to a default gateway, usually a router or firewall, which forwards it onward. Gateways are natural places for controls because traffic must pass through them. Tomás notes that the school's gateway filters traffic to and from the internet but nothing inside, because internal traffic never reaches it. Creating separate subnets for different groups would route internal traffic through the gateway, where rules could then decide what is allowed between groups.

### 2.3 Internet services the school depends on

The school uses several internet services: DNS to translate names into addresses, DHCP to give devices addresses automatically, email hosted by a provider, an online learning platform and a cloud backup service. Tomás lists each with its provider and what happens if it fails. DNS and DHCP are especially important because nearly everything depends on them; if DHCP stops, new devices cannot join, and if DNS fails, most applications stop working even though the network itself is fine. Dependencies like these must be protected and monitored.

### 2.4 Wireless networks

Most student devices connect over wireless. The school has one wireless network for students, one for staff and one for guests, but all three lead into the same subnet, so the separation is only in name. Tomás explains to classmates that separate wireless network names are useful only if each leads to its own subnet with rules between them. NIST SP 800-153 describes how wireless networks should be separated and secured, and Tomás uses it as a reference when he later helps design changes for the school.

### Worked example

Tomás's diagram shows one large subnet behind one gateway, with three wireless networks all bridged into it.

> **Synthetic case.** The network is synthetic.

### Errors and limits

Separate wireless names that lead to the same subnet give an illusion of separation.

### Exercises

- **EX004 — Internal traffic gap.** Why does the school gateway not filter internal traffic? *Rubric:* 3 = internal traffic stays in one subnet, never reaches it;; 2 = same subnet;; 1 = misconfigured;; 0 = none.
- **EX005 — DNS failure effect.** What happens to most applications if DNS fails? *Rubric:* 3 = stop working although network is up;; 2 = stop;; 1 = nothing;; 0 = none.
- **EX006 — Wireless illusion.** Why are the school's three wireless networks not truly separate? *Rubric:* 3 = all lead to same subnet;; 2 = same subnet;; 1 = same password;; 0 = none.

### Synthesis

Subnets, gateways and dependencies determine where controls can act and what must be protected.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write simple Python scripts with the standard library; (2) process lists and text; (3) make output clear.

### 3.1 Why technologists script

Technologists repeat many tasks: checking device lists, comparing configurations, counting log entries. Doing these by hand is slow and error-prone. Short Python scripts make them fast and repeatable. Tomás's course uses only the Python standard library, so scripts run on any machine without installing anything, and all lab data are synthetic. His first scripts are short and focused, such as counting how many devices in the inventory have no named owner, and he learns to read every line he writes so that he can trust the result.

### 3.2 Lists, dictionaries and sets

Python's basic structures fit network tasks well. A list keeps items in order, such as firewall rules. A dictionary maps keys to values, such as device names to addresses. A set holds unique items and supports comparisons, such as which approved services were not seen and which seen services were not approved. Tomás practises choosing the right structure: using a set to compare two inventories takes one line and avoids mistakes that come from looping through lists by hand and missing duplicates.

### 3.3 Working with text

Logs and configuration files are text. Tomás learns to split lines into fields, strip extra spaces, convert numbers and skip blank lines. He handles errors by counting lines that do not match the expected format and reporting the count, rather than letting the script crash or quietly ignoring them. He also learns never to run text from logs as commands, because logs can contain text that a user or attacker typed. Treating input as data, never as instructions, is a basic safety rule for scripts.

### 3.4 Clear output

A script's output should answer a question. Tomás prints aligned columns with short headers, a summary line with totals and percentages, and a note of any skipped input. He avoids printing hundreds of lines when a short list of exceptions would do. Clear output helps Gareth, who will use some of Tomás's scripts after the placement, and it makes errors easier to spot, because a reader can check that the summary matches the listed items. Good output is part of good tooling, not decoration.

### Worked example

Tomás's script counts three devices with no owner and reports one malformed inventory line.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Scripts that hide skipped input can produce confident but incomplete results.

### Exercises

- **EX007 — Set comparison use.** What task suits a set comparison? *Rubric:* 3 = approved versus observed items, finding differences;; 2 = comparisons;; 1 = ordering;; 0 = none.
- **EX008 — Log text safety.** Why must log text never be run as commands? *Rubric:* 3 = may contain text typed by users or attackers;; 2 = unsafe;; 1 = slow;; 0 = none.
- **EX009 — Skipped input.** How should a script handle lines in the wrong format? *Rubric:* 3 = count and report them;; 2 = report;; 1 = crash;; 0 = none.

### Synthesis

Small, clear stdlib scripts make routine checks fast, repeatable and trustworthy.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) design simple data models for network records; (2) keep data accurate; (3) protect personal data.

### 4.1 Modelling network records

A data model decides what is recorded and how records relate. For the school, Tomás models devices, networks and owners. Each device record has a unique name, type, location, network group and owner. Each network group has a name, purpose and address range. Owners are roles, such as "science department head", rather than individuals where possible, so records stay valid when staff change. A clear model makes the inventory easy to query and helps prevent inconsistent entries, such as the same printer recorded twice under different names.

### 4.2 Formats for exchange

Data often moves between tools in formats such as CSV for tables and JSON for structured records. Tomás uses CSV for the inventory because Gareth can open it in a spreadsheet, and JSON for configuration summaries because it handles nested values. Python's standard library reads both. He documents each file's columns or fields, including units and allowed values, so that anyone receiving the data understands it. Undocumented formats lead to misreadings, such as treating a port number column as text.

### 4.3 Accuracy and maintenance

Records decay as devices are added, moved and removed. Tomás suggests that Gareth updates the inventory whenever he changes a device, and that a monthly script compares the inventory with devices seen on the network. Differences are investigated: unknown devices may be unauthorised, and listed devices not seen may have been retired. Keeping data accurate is a habit, not a project. A stale inventory is in some ways worse than none, because people trust it and make decisions on information that is no longer true.

### 4.4 Personal data in records

Network records can contain personal data, such as which student uses which laptop. Schools hold data about children, which carries extra legal care. Tomás records only what security needs: device assignments to staff roles, and student devices by year group rather than by name, unless the school's data protection lead approves otherwise. Data minimisation reduces harm if records leak and keeps the inventory focused. Tomás discusses the model with the school's data protection lead before using it, which also builds trust in his placement.

### Worked example

The inventory model has three linked tables and is approved by the data protection lead with student devices recorded by year group.

> **Synthetic case.** The model is synthetic.

### Errors and limits

Recording individual names where roles would do creates unnecessary personal data.

### Exercises

- **EX010 — Owners as roles.** Why record owners as roles rather than individuals? *Rubric:* 3 = records stay valid when staff change;; 2 = stability;; 1 = privacy only;; 0 = none.
- **EX011 — Format choice.** Why use CSV for the inventory? *Rubric:* 3 = technician can open in spreadsheet;; 2 = easy;; 1 = required;; 0 = none.
- **EX012 — Student data minimisation.** How are student devices recorded? *Rubric:* 3 = by year group unless approved otherwise;; 2 = year group;; 1 = by name;; 0 = none.

### Synthesis

Simple, documented, accurate and minimal data models support every later security task.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core security goals; (2) identify assets, threats and risks at a school; (3) describe control types.

### 5.1 Security goals at a school

Confidentiality, integrity and availability apply to the school as to any organisation. Student records and finance data must stay confidential. Exam marks and attendance records must not be altered improperly. The learning platform and internet access must be available during lessons. Tomás notices that availability is especially visible at a school: if the network fails during an exam or a lesson, hundreds of people are affected at once, so any security change must be planned carefully to avoid disrupting teaching.

### 5.2 Assets and threats

Tomás lists the school's key assets: student records, finance systems, staff email, the learning platform, the network itself and the school's reputation. He then lists threats: a student trying to reach staff systems out of curiosity, malware arriving on a personal device, a phishing email stealing a staff password, an outdated switch being misused, and accidental damage from a misconfiguration. Threats at a school include curious students, which is less common in businesses, and controls must assume some users will test boundaries.

### 5.3 Risk and priority

Risk combines likelihood and impact. A student reaching the finance office printer is likely given the flat network, but the impact is modest. A student reaching the student records system is less likely but would have serious impact. Tomás ranks risks on a simple high, medium and low scale and discusses the ranking with Gareth. They agree that separating administrative systems from the student network is the top priority, followed by securing switch management and reviewing unapproved services. The agreed ranking is recorded with its date.

### 5.4 Types of control

Controls are preventive, detective or corrective. Network separation prevents students reaching admin systems. Logging and alerts detect unusual activity. Backups correct the effects of data loss. Tomás also distinguishes technical controls, like firewalls, from administrative ones, like an acceptable use policy that students sign. Good security combines both: a policy tells students what is not allowed, and technical controls make it difficult to break the policy, while logs show when someone tries. No single control type is sufficient on its own.

### Worked example

Tomás's risk list ranks student access to admin systems as the top risk, followed by insecure switch management.

> **Synthetic case.** Risks are synthetic.

### Errors and limits

Ignoring curious insiders such as students underestimates threats in school networks.

### Exercises

- **EX013 — Availability at a school.** Why is availability especially visible at a school? *Rubric:* 3 = network failures affect hundreds during lessons or exams;; 2 = many affected;; 1 = not important;; 0 = none.
- **EX014 — School-specific threat.** Name a threat more common at schools than businesses. *Rubric:* 3 = curious students testing boundaries;; 2 = students;; 1 = hackers;; 0 = none.
- **EX015 — Policy plus technology.** Why combine an acceptable use policy with technical controls? *Rubric:* 3 = policy states rules, technology enforces, logs detect;; 2 = both;; 1 = one is enough;; 0 = none.

### Synthesis

Goals, assets, threats and risks guide which controls a school should apply first.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) harden operating systems; (2) understand virtual machines and networks; (3) isolate test environments.

### 6.1 Operating system basics for security

Operating systems control which programs run, which users can do what and which services listen on the network. Tomás learns to check running services, open ports and user accounts on a lab machine using built-in tools. Hardening means turning off unneeded services, applying updates, setting strong account policies and enabling the host firewall. The school's file server, for instance, has remote desktop enabled for a supplier who no longer works with the school, which is an unnecessary service and an obvious hardening task.

### 6.2 Virtual machines

Virtualisation runs several virtual machines on one physical server, each with its own operating system. The school runs its web, print and DNS services as virtual machines on two hosts. Virtualisation saves hardware but concentrates risk: if a host fails or is compromised, all its virtual machines are affected. Tomás notes that the management interface of the virtualisation hosts must be especially protected, since anyone who reaches it can control every server on that host, including starting, stopping and copying them.

### 6.3 Virtual networks

Virtual machines connect through virtual switches inside the host, which can be linked to physical networks or kept internal. Separation that exists on physical switches must be repeated in virtual ones, or traffic between virtual machines may bypass controls. Tomás checks that the school's virtual switches place the finance server on its own network segment, and finds it shares a segment with the web server. He records this as a finding, since a compromised web server could otherwise reach the finance server directly.

### 6.4 Safe test environments

Virtualisation also gives Tomás a safe place to practise. He builds a small lab of virtual machines on a college laptop: a firewall, two clients and a server, all on internal virtual networks with no connection to the college or school network. He can test rules, break configurations and restore snapshots without affecting anyone. Isolated labs are how technologists learn safely; experimenting on a live school network would risk disrupting lessons and could breach the placement agreement. He saves a clean snapshot before each exercise.

### Worked example

Tomás's hardening checklist for the file server removes remote desktop and two unused services and enables the host firewall.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Separating physical networks while leaving virtual machines on one virtual segment undermines segmentation.

### Exercises

- **EX016 — Virtualisation risk.** Why must virtualisation host management be strongly protected? *Rubric:* 3 = controls all VMs on the host;; 2 = control;; 1 = slow;; 0 = none.
- **EX017 — Virtual segment finding.** What risk does sharing a segment with the web server create for finance? *Rubric:* 3 = compromised web server could reach finance directly;; 2 = direct access;; 1 = none;; 0 = none.
- **EX018 — Lab isolation.** Why keep the practice lab disconnected from other networks? *Rubric:* 3 = avoid disruption and agreement breaches;; 2 = safety;; 1 = speed;; 0 = none.

### Synthesis

Hardened hosts, protected virtualisation management and isolated labs support safe, segmented networks.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) distinguish authentication and authorisation; (2) apply least privilege; (3) manage accounts and administrator access.

### 7.1 Who are you, what may you do

Authentication checks identity, usually with a password and ideally a second factor. Authorisation decides what an authenticated user may do. At the school, students, teachers, office staff and the technician need different access. Tomás finds that the staff wireless uses a single shared passphrase that several students have learned, so it authenticates no one reliably. He recommends moving staff wireless to individual accounts, so each connection is tied to a person and leavers can be removed individually. Guests keep a separate, simpler network.

### 7.2 Least privilege

Least privilege means giving each user only the access they need. Teachers need the learning platform and shared teaching files; office staff need finance and records systems; students need the internet and learning platform. Tomás finds several teachers are in an administrator group on the file server, added years ago to fix a printing problem. He recommends removing them and solving the printing problem properly. Excess privilege is often added for convenience and rarely removed, which slowly widens access well beyond what anyone intended.

### 7.3 Administrator accounts

Administrator accounts can change systems and the network, so they need special care. Tomás recommends that Gareth uses a separate administrator account only for administrative tasks, with a second factor, and an ordinary account for email and browsing. This limits harm if his ordinary account is phished. Administrator logins are logged centrally. He also suggests a sealed record of emergency credentials kept by the head teacher, so the school is not locked out if Gareth is unavailable during an emergency.

### 7.4 Account lifecycle

Accounts must be created, changed and removed as people join, move and leave. Schools have predictable cycles: students join and leave each year, and staff change at term boundaries. Tomás proposes a review at the start of each term comparing accounts with current student and staff lists from the school office. In his first review, he finds 37 accounts for students who left last summer and two for former staff. Regular, scheduled reviews catch such leftovers before they can be misused.

### Worked example

The term review finds 39 leftover accounts, and four teachers are removed from the file server administrator group.

> **Synthetic case.** Accounts are synthetic.

### Errors and limits

Privileges added to fix one-off problems often remain for years.

### Exercises

- **EX019 — Shared passphrase problem.** Why is the shared staff wireless passphrase weak? *Rubric:* 3 = known to students, no individual identity or revocation;; 2 = shared;; 1 = short;; 0 = none.
- **EX020 — Separate admin account.** Why should Gareth use a separate administrator account? *Rubric:* 3 = limits harm if everyday account is phished;; 2 = safety;; 1 = convenience;; 0 = none.
- **EX021 — Review timing.** When should account reviews happen at a school? *Rubric:* 3 = start of each term against current lists;; 2 = termly;; 1 = yearly;; 0 = none.

### Synthesis

Individual authentication, least privilege and regular account reviews keep access aligned with need.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) design zones for the school; (2) apply default deny between zones; (3) protect management.

### 8.1 Zones for a school

A zone groups devices with similar trust and needs. Tomás proposes six zones: staff, students, administration (finance and records), guest, shared devices (printers and projectors) and management (switches, access points and virtualisation hosts). Each zone gets its own subnet. Students should reach the internet and the learning platform, staff should additionally reach teaching files and shared devices, and administration should be reachable only by office staff. The proposal is based on the risk ranking from chapter 5. Gareth reviews the list and confirms each group.

### 8.2 Default deny between zones

Traffic between zones passes through the firewall, which allows only listed flows and denies everything else. This approach, recommended in NIST SP 800-41r1, means that forgotten or new flows are blocked until someone decides to allow them. Tomás lists the needed flows for each zone pair. Students to administration has no entries at all. Students to shared devices has one entry, printing to student printers only. Writing the list forces explicit decisions instead of leaving access to chance. Each entry names its owner and reason.

### 8.3 Protecting management

Network devices and virtualisation hosts are managed through web pages or command-line sessions. If students can reach those interfaces, they could try to change the network. Tomás places all management interfaces in the management zone, reachable only from Gareth's administrator workstation, and recommends using SSH and HTTPS rather than older unencrypted protocols such as Telnet. During his review, he finds two switches with Telnet still enabled, which sends passwords in clear text across the network. Both are scheduled for SSH-only access.

### 8.4 Keeping the design simple

A school has one technician, so the design must be simple to run. Tomás resists adding more zones or complex rules. He uses consistent names, a small set of rules and a one-page diagram. He documents the reason for each zone and flow, so that Gareth or a successor can understand the design quickly. Saltzer and Schroeder's principle of economy of mechanism supports this choice: simpler designs are easier to check and less likely to hide mistakes. Gareth confirms he can explain every rule.

### Worked example

The design has six zones, fourteen needed flows and a default deny rule; two switches are flagged for disabling Telnet.

> **Synthetic case.** The design is synthetic.

### Errors and limits

Designs too complex for the available staff are quietly simplified in unsafe ways later.

### Exercises

- **EX022 — Student to admin flows.** How many flows are allowed from students to administration? *Rubric:* 3 = none; all denied by default;; 2 = none;; 1 = some;; 0 = none.
- **EX023 — Telnet risk.** Why replace Telnet on switches? *Rubric:* 3 = sends passwords in clear text;; 2 = unencrypted;; 1 = old;; 0 = none.
- **EX024 — Simplicity reason.** Which design principle supports keeping the school design simple? *Rubric:* 3 = economy of mechanism (Saltzer and Schroeder);; 2 = simplicity;; 1 = none;; 0 = none.

### Synthesis

Purposeful zones, default deny and protected management form a simple, effective school architecture.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) choose simple indicators; (2) collect evidence reliably; (3) compare before and after.

### 9.1 Choosing indicators

Tomás needs to show whether changes improve security. He chooses indicators linked to the risks: the number of zone pairs that can reach each other, the number of unapproved services on servers, the number of accounts not matching current lists, and the number of switches with insecure management protocols. Each is easy to count with a script and easy for the head teacher to understand. Good indicators move only when security actually changes, rather than when someone simply changes how they are counted.

### 9.2 Collecting evidence

Each indicator has a defined method: which data source, which script, which date. Tomás saves script outputs with dates in a project folder, so figures can be rechecked later. He avoids relying on memory or verbal reports, which cannot be verified. Evidence collected the same way each time can be compared reliably. When a method changes, such as using a new inventory source, he records the change and, where possible, measures once with both methods so the effect of the change itself is known.

### 9.3 Before and after

To show improvement, Tomás measures before changes and again afterwards. Before, all six proposed zones are effectively one, so every zone pair can reach every other: thirty ordered pairs. After implementation, he expects only the fourteen needed flows to cross between zones. He is careful to measure in similar conditions, such as during term time, because holiday periods have very different traffic. Before and after comparisons are the simplest convincing evidence that a change achieved its goal. Both measurements use the same scripts.

### 9.4 Reporting simply

Tomás reports indicators in a short table with the before value, the after value, the target and a one-line comment. He adds sample sizes and dates. He avoids percentages for very small counts, writing "2 of 2 switches" rather than "100 percent". The report is shared with Gareth and the head teacher monthly during the placement. Simple, honest reporting builds trust and lets the school see progress without needing technical expertise, while still giving technical readers the detail they need.

### Worked example

Before values: thirty reachable zone pairs, four unapproved services, thirty-nine leftover accounts and two Telnet switches.

> **Synthetic case.** Indicators are synthetic.

### Errors and limits

Comparing a holiday week with a term week can create false improvements.

### Exercises

- **EX025 — Zone pair count.** How many ordered zone pairs exist among six zones? *Rubric:* 3 = thirty, six times five;; 2 = 30;; 1 = 36;; 0 = none.
- **EX026 — Method change handling.** What should be done when a measurement method changes? *Rubric:* 3 = record it and measure once with both methods;; 2 = record;; 1 = ignore;; 0 = none.
- **EX027 — Small count reporting.** How should two of two switches be reported? *Rubric:* 3 = as "2 of 2", not 100 percent;; 2 = counts;; 1 = percentage;; 0 = none.

### Synthesis

Simple, reproducible indicators measured before and after show whether changes work.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Network and communications security: orientation

### Learning outcomes

You will (1) describe the field's scope; (2) relate it to the school; (3) plan the placement.

### 10.1 What the field covers

Network and communications security protects data in transit and the networks that carry it. It includes segmentation and firewalls, secure protocols such as TLS and SSH, wireless security, DNS protection, monitoring and detection, and the operational processes that keep controls working. Tomás maps each area to the school: segmentation addresses the flat network, secure protocols address Telnet on switches, wireless security addresses the shared passphrase, DNS filtering already protects students, and monitoring is mostly missing. This map shows where the placement should start.

### 10.2 From perimeter to internal controls

The school's current design trusts everything inside and filters only at the internet gateway. Modern guidance, including NIST SP 800-207 on zero trust architecture, argues that internal traffic deserves the same scrutiny as external traffic, because once an attacker or curious user is inside, a flat network offers no further resistance. Tomás does not propose full zero trust for a school with one technician, but he adopts its central idea: reduce implicit trust between groups and check access more carefully at internal boundaries.

### 10.3 Placement plan

Tomás and Gareth agree a placement plan for the coming terms. First, complete the inventory and risk list. Second, design zones and needed flows. Third, test in a lab. Fourth, implement in stages during school holidays. Fifth, introduce monitoring and routines. Each stage has a deliverable and a review with Ms Okafor. The plan respects the school's calendar, avoiding exam periods for any change. A written plan helps everyone know what to expect and when decisions are needed. Dates are shared with school leaders.

### 10.4 Agreement and boundaries

The placement agreement, signed by the head teacher, Ms Okafor and Tomás, states what he may do: review configurations and logs provided by Gareth, build lab copies, and assist Gareth with changes Gareth approves. He may not make changes alone, access student data or run tools against the school network without Gareth's explicit approval for each activity. Clear boundaries protect the school, the college and Tomás, and they are a normal part of professional practice in network security. Copies are kept by all three parties.

### Worked example

The placement plan has five stages, each with a deliverable and a review date, avoiding exam periods.

> **Synthetic case.** The plan is synthetic.

### Errors and limits

Starting technical work before agreeing boundaries risks well-meant actions that breach trust or law.

### Exercises

- **EX028 — Zero trust idea adopted.** Which zero trust idea does Tomás adopt for the school? *Rubric:* 3 = reduce implicit trust between internal groups;; 2 = internal checks;; 1 = full zero trust;; 0 = none.
- **EX029 — Exam periods.** Why does the placement plan avoid exam periods? *Rubric:* 3 = changes could disrupt exams;; 2 = disruption;; 1 = holidays;; 0 = none.
- **EX030 — Placement boundary.** Name one activity Tomás may not do alone. *Rubric:* 3 = make changes, access student data or run tools without approval;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Understanding the field's scope and agreeing a careful plan and boundaries prepare a safe placement.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Network and communications security: assets and context

### Learning outcomes

You will (1) identify network assets and owners; (2) understand school context and constraints; (3) record dependencies.

### 11.1 Network assets

Network assets include the devices that carry traffic, such as the gateway firewall, twelve switches and thirty wireless access points, and the services that make the network usable, such as DHCP, DNS and the wireless controller. Tomás adds these to the inventory with their locations, firmware versions and owners. He notes which are single points of failure: the core switch in the server room connects every building, so its failure would stop the whole school. Knowing which assets are critical helps decide where to spend effort on resilience as well as security.

### 11.2 Context and constraints

Every design must fit its context. Ridgeway has one technician, a small budget, a fixed school calendar and many users who are children. Teachers need technology to work at the start of every lesson; there is no time to troubleshoot during class. Changes are possible mainly in holidays. Safeguarding duties mean the school must filter harmful content for students and keep records of serious concerns. Tomás lists these constraints at the start of his design notes, because a design that ignores them will not be adopted or will fail in use.

### 11.3 Stakeholders

Several people care about the network for different reasons. The head teacher cares about safety, reputation and cost. Teachers care about reliability during lessons. The business manager cares about finance systems. The safeguarding lead cares about content filtering and reporting. Gareth cares about workload. Tomás meets each briefly to understand their needs. He finds that the business manager is unaware that student devices share a network with finance systems, and that once she understands, she becomes a strong supporter of separation.

### 11.4 Dependencies and suppliers

The school relies on suppliers: an internet provider, a filtering service, the learning platform, a managed print supplier and a heating control company with a remote connection. Tomás records each supplier's access: what they connect to, how and who authorises it. The heating company's connection goes directly into the main subnet through an old remote access tool. He flags it for review, recalling that forgotten supplier access is a common cause of incidents, and proposes routing it through a controlled path with named accounts.

### Worked example

The asset list adds 43 network devices; the core switch is marked as a single point of failure, and the heating company's direct access is flagged.

> **Synthetic case.** Assets and suppliers are synthetic.

### Errors and limits

Designs that ignore the school calendar and staff capacity are rarely implemented as intended.

### Exercises

- **EX031 — Single point of failure.** Which asset is a single point of failure, and why? *Rubric:* 3 = core switch connecting all buildings;; 2 = core switch;; 1 = firewall;; 0 = none.
- **EX032 — Business manager response.** Why did the business manager support separation? *Rubric:* 3 = learned finance shares network with students;; 2 = awareness;; 1 = cost;; 0 = none.
- **EX033 — Supplier access fix.** How should the heating company's access be changed? *Rubric:* 3 = controlled path with named accounts;; 2 = controlled;; 1 = removed;; 0 = none.

### Synthesis

Knowing network assets, constraints, stakeholders and suppliers grounds design in the school's reality.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Network and communications security: data flows

### Learning outcomes

You will (1) identify needed flows; (2) analyse DNS logs; (3) use flows to inform filtering and rules.

### 12.1 Mapping flows

A data flow is traffic from one group to a service for a purpose. Tomás maps flows by asking users what they do and checking logs Gareth provides. Students use the learning platform, web browsing and printing. Teachers add teaching file shares and projectors. Office staff use the finance and records systems. Each flow is written with source zone, destination, service and reason. This flow list later becomes the firewall policy, so mistakes here become mistakes in the rules, which is why he reviews it with users.

### 12.2 DNS as a window on flows

Almost every connection starts with a DNS lookup, so DNS logs show what devices try to reach. The school's filtering service blocks categories for students, such as gaming during lessons and newly registered domains, which are often used for malicious sites. NIST SP 800-81-2 discusses DNS security, including protecting resolvers. Tomás analyses a synthetic sample of DNS logs to see how filtering behaves by zone and which blocked lookups repeat, since repeated blocked lookups from one device may indicate malware rather than a curious student.

### Lab — DNS summary

```python
"""Summarise synthetic school DNS query logs by zone and blocked category (stdlib only)."""
import collections
log = [("students", "learn.example.edu", "ok"), ("students", "video.example.com", "ok"), ("students", "game.example.net", "blocked:gaming"),
       ("staff", "mail.example.org", "ok"), ("students", "x1y2z3.example.biz", "blocked:newly-registered"),
       ("students", "game.example.net", "blocked:gaming"), ("admin", "payroll.example.org", "ok"), ("guest", "news.example.com", "ok"),
       ("staff", "learn.example.edu", "ok"), ("students", "x1y2z3.example.biz", "blocked:newly-registered"),
       ("students", "x1y2z3.example.biz", "blocked:newly-registered"), ("guest", "game.example.net", "blocked:gaming")]
by_zone = collections.Counter(z for z, _, _ in log); blocked = [(z, d, r) for z, d, r in log if r != "ok"]
print("queries by zone:", dict(by_zone))
print("blocked by category:", dict(collections.Counter(r.split(":")[1] for _, _, r in blocked)))
print("repeat blocked domains:", {d: n for d, n in collections.Counter(d for _, d, _ in blocked).items() if n >= 3})
print(f"blocked share {len(blocked)}/{len(log)} = {100*len(blocked)/len(log):.1f}%")
```

Run with `python3 lab_dns.py`. Verified output:

```text
queries by zone: {'students': 7, 'staff': 2, 'admin': 1, 'guest': 2}
blocked by category: {'gaming': 3, 'newly-registered': 3}
repeat blocked domains: {'game.example.net': 3, 'x1y2z3.example.biz': 3}
blocked share 6/12 = 50.0%
```

### 12.3 Reading the summary

In the synthetic sample of twelve lookups, half are blocked: three for gaming and three for a newly registered domain. The gaming lookups come from students and one guest, which is expected curiosity. The newly registered domain is looked up three times by students, an unusual pattern for a random-looking name. Tomás flags it for Gareth to check which device made the lookups. A device repeatedly contacting a newly registered, random-looking domain could be infected and trying to reach a controller, so it deserves attention even if blocking succeeded.

### 12.4 Flows inform rules

From the flow list, Tomás drafts firewall rules for each zone pair, and from the DNS analysis he recommends that all zones use the school's resolvers, with outbound DNS to other servers blocked. This ensures filtering cannot be bypassed by configuring a different resolver, and that DNS logs remain complete. He notes that guest devices also use the school resolvers but receive lighter filtering, consistent with their internet-only access. Flows, rules and logging are designed together so that each supports the others.

### Worked example

Half of twelve synthetic lookups are blocked; a newly registered random-looking domain repeated three times is flagged for investigation.

> **Synthetic case.** Logs are synthetic.

### Errors and limits

Allowing devices to use any DNS resolver lets filtering and logging be bypassed.

### Exercises

- **EX034 — Blocked share.** What share of lookups were blocked in the sample? *Rubric:* 3 = 6 of 12, 50 percent;; 2 = half;; 1 = some;; 0 = none.
- **EX035 — Suspicious pattern.** Why flag repeated lookups of a newly registered random-looking domain? *Rubric:* 3 = possible malware contacting controller;; 2 = malware;; 1 = curiosity;; 0 = none.
- **EX036 — Resolver rule.** Why block outbound DNS to servers other than the school's? *Rubric:* 3 = prevents bypassing filtering, keeps logs complete;; 2 = bypass;; 1 = speed;; 0 = none.

### Synthesis

Flow maps and DNS logs guide rules and highlight devices needing attention.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Network and communications security: risk scenarios

### Learning outcomes

You will (1) build realistic risk scenarios; (2) trace each through the network; (3) link scenarios to controls.

### 13.1 Why scenarios

Lists of threats can feel abstract. Scenarios tell a short story of how harm could happen, step by step, which helps people understand and helps designers check controls. Tomás writes four scenarios for the school, each based on common patterns rather than real events, and traces how each would unfold on the current network and on the proposed design. Scenarios also make good teaching material for staff, who can relate to a story more easily than to a technical diagram.

### 13.2 Scenario: curious student

A student finds the finance office printer in a list of network devices and prints to it repeatedly as a joke. Then the student finds a web page for the finance server and tries common passwords. On the current flat network, every step is possible. In the proposed design, students cannot reach the administration zone at all, so the printer and server are invisible, and denied attempts are logged. The scenario shows that separation removes the opportunity rather than relying on the student's restraint.

### 13.3 Scenario: infected laptop

A teacher's laptop is infected at home and brought into school. The malware searches the network for file shares and remote desktop services. On the current network, it finds the file server, whose remote desktop is open, and the finance server. In the proposed design, staff can reach teaching file shares but not finance; remote desktop is disabled; and denied connections generate logs that monitoring can notice. Tomás notes that the teaching file share remains reachable, so backups and host protection remain essential.

### 13.4 Scenario: misused supplier access

The heating company's old remote access tool is still connected directly to the main subnet. If its credentials were stolen, someone could connect from outside and reach any device. In the proposed design, supplier access goes through a controlled path with named accounts, reaches only the heating controller and is logged. This scenario persuades the head teacher to prioritise fixing supplier access, because it shows how a small, forgotten connection could expose the whole school to people outside it. The fix is scheduled first.

### Worked example

Four scenarios are traced; three are blocked early in the proposed design and one is limited to teaching files.

> **Synthetic case.** Scenarios are synthetic.

### Errors and limits

Scenarios that assume attackers behave exactly as designers expect miss alternative paths.

### Exercises

- **EX037 — Separation versus restraint.** How does the student scenario show the value of separation? *Rubric:* 3 = removes opportunity instead of relying on restraint;; 2 = removes access;; 1 = punishes;; 0 = none.
- **EX038 — Remaining exposure.** What remains reachable for an infected staff laptop? *Rubric:* 3 = teaching file shares;; 2 = files;; 1 = nothing;; 0 = none.
- **EX039 — Supplier scenario effect.** Why did the supplier scenario change priorities? *Rubric:* 3 = showed outsiders could reach whole school;; 2 = exposure;; 1 = cost;; 0 = none.

### Synthesis

Scenarios turn abstract risks into stories that test controls and persuade decision makers.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Network and communications security: methods I

### Learning outcomes

You will (1) write requirements; (2) plan zone migration; (3) design tests from requirements.

### 14.1 Requirements

Tomás writes requirements that state what must be true. R1: students and guests cannot reach the administration or management zones. R2: traffic between zones is denied unless listed as a needed flow. R3: network devices are managed only from the management zone using encrypted protocols. R4: staff wireless uses individual accounts. R5: all zones use the school's DNS resolvers. R6: firewall and switch logs are sent to a central store and kept for ninety days. Numbered requirements let tests, changes and reports refer to them precisely.

### 14.2 Planning migration

Moving from one subnet to six zones affects every device. Tomás plans the migration in stages during the summer holiday: first create the management zone and move switches and access points into it; then create the administration zone and move finance and records systems; then separate students, staff, shared devices and guests. Each stage has a test list and a rollback step. Staging limits the number of things that can go wrong at once and makes problems easier to trace.

### 14.3 Designing tests

Tests come from requirements. For R1, a test device in the student zone attempts connections to administration and management services, expecting all to fail, and also to the learning platform, expecting success. For R3, Tomás confirms switch management works over SSH from the management zone and fails from the staff zone, and that Telnet is disabled. Each test has an expected result recorded before running. Testing both what should work and what should fail catches rules that are too strict as well as too loose.

### 14.4 Fixed-address devices

Many school devices have fixed addresses set by hand: printers, projectors and the heating controller. They will not move to new zones automatically. Tomás and Gareth list them from the inventory, plan new addresses and schedule each change. Projectors in classrooms need testing before term starts, because a projector that fails on the first day of term causes immediate disruption. Fixed-address devices are often the most time-consuming part of a migration, so they are planned in detail rather than handled ad hoc.

### Worked example

Six requirements, three migration stages and twenty-two tests are planned; forty-one fixed-address devices are scheduled for readdressing.

> **Synthetic case.** Plans are synthetic.

### Errors and limits

Tests that only check permitted flows miss rules that allow too much.

### Exercises

- **EX040 — Migration order.** Which zone is created first, and why? *Rubric:* 3 = management, so network devices are protected and reachable for later steps;; 2 = management;; 1 = students;; 0 = none.
- **EX041 — R1 test design.** Describe a test for R1. *Rubric:* 3 = student test device to admin/management fails, learning platform succeeds;; 2 = attempt;; 1 = vague;; 0 = none.
- **EX042 — Projector timing.** Why test projectors before term starts? *Rubric:* 3 = failures disrupt first lessons;; 2 = disruption;; 1 = none;; 0 = none.

### Synthesis

Clear requirements, staged migration and requirement-based tests make change safe.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Network and communications security: guided lab

### Learning outcomes

You will (1) compare approved and observed services; (2) investigate differences; (3) record decisions.

### 15.1 Approved services

A server should offer only the services it needs. Tomás and Gareth write an approved service list for key servers and devices: the web server offers HTTP and HTTPS, the file server offers file sharing, the print server offers the printing protocol, the DNS server offers DNS and switches offer SSH for management. Anything else is unapproved until someone justifies it. The approved list is part of the configuration baseline and is reviewed whenever services change. Gareth signs off the list as its owner.

### 15.2 Observed services

To compare reality with the list, Gareth exports a service inventory from the servers' own management tools and the switches' configurations, which Tomás receives as a synthetic, sanitised file for the lab. He does not scan the school network; observed services come from the systems themselves with Gareth's authorisation. The lab compares the two sets and reports differences in both directions: services observed but not approved, and approved services not observed. The comparison is repeated each term, so new services that appear between reviews are noticed and either approved or removed.

### Lab — Service comparison

```python
"""Compare an approved service list with a synthetic observed service inventory (stdlib only; no scanning)."""
approved = {("web01", 443), ("web01", 80), ("files01", 445), ("print01", 631), ("dns01", 53), ("mgmt-sw1", 22)}
observed = {("web01", 443), ("web01", 80), ("web01", 8080), ("files01", 445), ("files01", 3389), ("print01", 631),
            ("print01", 9100), ("dns01", 53), ("mgmt-sw1", 22), ("mgmt-sw1", 23)}
extra, missing = sorted(observed - approved), sorted(approved - observed)
for h, p in extra: print(f"UNAPPROVED {h}:{p}")
for h, p in missing: print(f"MISSING    {h}:{p}")
print(f"approved {len(approved)}, observed {len(observed)}, unapproved {len(extra)}, missing {len(missing)}")
```

Run with `python3 lab_services.py`. Verified output:

```text
UNAPPROVED files01:3389
UNAPPROVED mgmt-sw1:23
UNAPPROVED print01:9100
UNAPPROVED web01:8080
approved 6, observed 10, unapproved 4, missing 0
```

### 15.3 Reading the comparison

The comparison finds four unapproved services and none missing. The file server offers remote desktop, which the old supplier used. A switch still has Telnet enabled, matching the earlier finding. The print server offers a raw printing port in addition to the approved protocol, which some old printers need. The web server offers a second web port used by a forgotten test site. Each finding is discussed: remote desktop and Telnet are disabled, the test site is removed, and the raw printing port is kept for now but restricted to the shared devices zone.

### 15.4 Recording decisions

Each finding becomes a decision record: what was found, what was decided, who decided and when to review. The raw printing port, kept for compatibility, gets a review date for when the old printers are replaced. Recording decisions prevents the same finding from being raised and argued again at every review, and shows auditors that exceptions were considered deliberately. The approved service list is updated to include the restricted printing port with its reason. Records are stored with the inventory.

### Worked example

Four unapproved services are found; three are removed and one is kept with restrictions and a review date.

> **Synthetic case.** Service data are synthetic.

### Errors and limits

Removing services without checking their users can break needed functions.

### Exercises

- **EX043 — Comparison result.** What does the comparison report? *Rubric:* 3 = 4 unapproved, 0 missing, naming them;; 2 = 4 unapproved;; 1 = some;; 0 = none.
- **EX044 — Kept exception.** Which unapproved service is kept, and how? *Rubric:* 3 = raw printing port restricted to shared devices zone with review date;; 2 = printing port;; 1 = none;; 0 = none.
- **EX045 — Data source.** Where do observed services come from in this lab? *Rubric:* 3 = systems' own management data, authorised, not scanning;; 2 = exports;; 1 = scanning;; 0 = none.

### Synthesis

Comparing approved and observed services finds unnecessary exposure and leads to recorded decisions.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Network and communications security: methods II

### Learning outcomes

You will (1) secure wireless networks; (2) protect remote access; (3) apply encryption to management and services.

### 16.1 Wireless done properly

Tomás redesigns the school's wireless: a staff network with individual accounts checked against the school's directory, a student network with student accounts, a guest network with a passphrase changed termly and internet-only access, and each network linked to its own zone. Access point management sits in the management zone. Client isolation on the guest and student networks stops devices talking to each other directly. These steps follow NIST SP 800-153 guidance and turn the existing wireless names into real separation.

### 16.2 Remote access for staff

Some staff need school systems from home. The current approach exposes the file server directly to the internet with a password, which is risky. Tomás proposes a VPN with individual accounts and a second factor, placing remote users in a restricted zone that reaches only teaching files and the learning platform. NIST SP 800-77r1 describes IPsec VPN design, and SP 800-52r2 covers TLS configuration if a TLS-based VPN is chosen. Remote finance access is limited to office staff and logged.

### 16.3 Encrypted management

All device management uses encrypted protocols: SSH for command line and HTTPS for web interfaces. Telnet and plain HTTP management are disabled. Tomás also checks that the HTTPS certificates on management pages are valid and that management accounts are individual rather than a shared "admin" login. Encrypted management protects credentials from anyone listening on the network, and individual accounts make logs meaningful because they show who made each change rather than just that "admin" did. Old shared logins are disabled once individual ones work.

### 16.4 TLS on school services

The school's web services should use current TLS. SP 800-52r2 recommends TLS 1.2 or later. Tomás checks the school's web server, learning platform connection and email settings with Gareth and finds the web server still accepts TLS 1.0. Gareth updates the configuration, and they confirm modern browsers still connect. TLS 1.3, described in RFC 8446, is enabled where supported. Keeping TLS current protects passwords and personal data in transit between users and school services. The check is repeated each term with the same steps.

### Worked example

Four wireless networks map to four zones; remote access moves to a VPN; Telnet is disabled; the web server drops TLS 1.0.

> **Synthetic case.** Configurations are synthetic.

### Errors and limits

A VPN that gives remote users full network access recreates a flat network from home.

### Exercises

- **EX046 — Client isolation purpose.** Why enable client isolation on student wireless? *Rubric:* 3 = stops student devices attacking each other;; 2 = isolation;; 1 = speed;; 0 = none.
- **EX047 — Remote access change.** Why replace direct internet exposure of the file server? *Rubric:* 3 = risky; VPN with MFA and restricted zone instead;; 2 = risk;; 1 = speed;; 0 = none.
- **EX048 — Individual management accounts.** Why use individual management accounts rather than one admin login? *Rubric:* 3 = logs show who made changes;; 2 = accountability;; 1 = easier;; 0 = none.

### Synthesis

Proper wireless separation, controlled remote access and encryption close common gaps.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Network and communications security: tooling

### Learning outcomes

You will (1) choose suitable tools; (2) use them safely and with authorisation; (3) maintain tooling.

### 17.1 Choosing tools

Technologists use many tools: configuration managers, log collectors, monitoring dashboards and small scripts. Tomás chooses tools for the school by asking what problem each solves, whether Gareth can run it alone, what it costs and how it is supported. He prefers built-in features of existing equipment, such as the firewall's logging and the switches' configuration export, before adding new products. Every new tool adds something to maintain, update and secure, so tools must earn their place. Tomás writes a short note for each choice.

### 17.2 Authorised use

Some network tools can disrupt systems or reveal sensitive information if misused. Tomás uses tools only within the agreed scope and with Gareth's approval for each activity. He does not run discovery or testing tools against the school network; instead, he works with data exported by the systems themselves, as in the guided lab. The placement agreement makes this explicit. Authorised, careful use protects the school and Tomás and is expected of every professional in the field. Each approval is noted with its date.

### 17.3 Log collection

Tomás helps Gareth set up a central log collector on a small virtual machine in the management zone. Firewalls, switches and the wireless controller send logs to it using syslog, whose format is defined in RFC 5424. Logs are kept for ninety days, meeting requirement R6. The collector itself is protected: only Gareth can log in, and logs cannot be deleted from the devices that send them. A central store makes it possible to search across devices when investigating a problem.

### 17.4 Maintaining tools

Tools need care. The log collector needs disk space monitoring, updates and a check that every device is still sending logs. Scripts need tests and documentation. Tomás writes a short maintenance checklist covering each tool: what to check, how often and what to do if something is wrong. He also records which tools depend on which accounts and certificates. Unmaintained tools fail quietly, and a silent log collector is worse than none because people believe they have evidence they do not.

### Worked example

The school adopts one new tool, a log collector, and documents maintenance for it and four scripts.

> **Synthetic case.** Tooling is synthetic.

### Errors and limits

Adding tools without maintenance plans creates new weaknesses and silent failures.

### Exercises

- **EX049 — Tool selection questions.** List three questions for choosing a tool. *Rubric:* 3 = problem solved, can technician run it, cost or support;; 2 = two;; 1 = one;; 0 = none.
- **EX050 — No scanning.** How does Tomás obtain service data without scanning? *Rubric:* 3 = exports from systems with authorisation;; 2 = exports;; 1 = scans;; 0 = none.
- **EX051 — Silent collector risk.** Why is a silent log collector dangerous? *Rubric:* 3 = people believe they have evidence they lack;; 2 = false confidence;; 1 = none;; 0 = none.

### Synthesis

Fewer, well-chosen, authorised and maintained tools serve a small team best.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Network and communications security: controls

### Learning outcomes

You will (1) implement zone rules; (2) review rule order; (3) verify controls against requirements.

### 18.1 Implementing rules

During the summer holiday, Gareth and Tomás implement the firewall rules from the needed-flows list. Each rule has a source zone, destination, service, action and comment naming the flow and requirement. Specific allow rules come first, followed by a final rule denying everything else, as recommended in NIST SP 800-41r1. They implement one zone at a time, testing after each, so that any problem can be traced to the most recent change rather than to a whole batch of rules at once.

### 18.2 Rule order and overlap

Firewalls usually apply the first matching rule. A broad rule placed early can hide later, more specific ones. Tomás reviews the order and finds a rule allowing staff to reach "any" shared device, placed above a rule intended to block staff from the heating controller, which sits in the shared devices zone. The broad rule would let staff reach the controller. They narrow it to printers and projectors only. Wool's 2004 study of firewall configurations found such ordering errors common, which is why reviews matter.

### 18.3 Switch-level controls

Some controls live on switches. Unused switch ports are disabled so that nobody can plug in an unknown device in a corridor. Ports in classrooms are assigned to the correct zone. Management access to switches is limited to the management zone. Tomás also enables features that stop a device on one port from pretending to be the network's gateway, a common trick that can redirect traffic. These switch controls complement the firewall by enforcing separation at the point where devices connect.

### 18.4 Verifying controls

After implementation, Tomás runs the tests from chapter 14. Twenty of twenty-two pass at first. One failure shows a classroom projector unreachable from staff because its new address was mistyped; another shows the guest zone able to reach a shared printer because of a rule using the wrong zone. Both are fixed and the full test list is rerun. Every result is recorded with the date and configuration version, building the evidence that the controls meet the requirements. The results go into the evidence folder.

### Worked example

Rules are implemented zone by zone; one broad rule is narrowed; twenty-two tests pass after two fixes.

> **Synthetic case.** Rules and tests are synthetic.

### Errors and limits

Broad allow rules placed early can silently override specific restrictions.

### Exercises

- **EX052 — Broad rule problem.** What did the broad staff rule allow by mistake? *Rubric:* 3 = reaching the heating controller;; 2 = controller;; 1 = printers;; 0 = none.
- **EX053 — Unused ports.** Why disable unused switch ports? *Rubric:* 3 = stop unknown devices being plugged in;; 2 = unknown devices;; 1 = power;; 0 = none.
- **EX054 — Guest printer failure.** What caused the guest-to-printer test failure? *Rubric:* 3 = rule used wrong zone;; 2 = wrong zone;; 1 = typo;; 0 = none.

### Synthesis

Ordered, commented rules plus switch-level controls, verified by tests, enforce the design.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Network and communications security: monitoring

### Learning outcomes

You will (1) collect and review alerts; (2) measure alert precision; (3) tune detection.

### 19.1 What to monitor

With central logs in place, Tomás and Gareth decide what to watch. They choose repeated denied connections from student or guest devices towards administration or management, configuration changes on network devices, failed administrator logins, and alerts from the firewall's intrusion detection feature. NIST SP 800-94 describes intrusion detection and prevention systems and their tuning. Monitoring is chosen to match the risks and scenarios from earlier chapters, rather than enabling every possible alert. Each alert type has an owner, a short response note and a review date, so alerts lead to action rather than accumulating unread.

### 19.2 Alert quality

Not all alerts are useful. Gareth labels a synthetic sample of alerts from the first weeks as true, meaning they needed attention, or false, meaning they were harmless. Tomás calculates precision for each rule: the share of its alerts that were true. Rules with low precision waste Gareth's limited time and teach him to ignore alerts, which could cause a real one to be missed. Measuring precision turns a vague feeling that "there are too many alerts" into evidence about which rules need tuning.

### Lab — Alert precision

```python
"""Alert volume and precision by rule from a synthetic, labelled IDS sample (stdlib only)."""
import collections
alerts = [("policy-p2p", True)] * 4 + [("policy-p2p", False)] * 2 + [("dns-tunnel-heuristic", False)] * 9 + \
         [("dns-tunnel-heuristic", True)] * 1 + [("old-tls", True)] * 6 + [("smb-from-guest", True)] * 3
tot, tp = collections.Counter(), collections.Counter()
for r, ok in alerts: tot[r] += 1; tp[r] += ok
for r in tot: print(f"{r:22}{tot[r]:3} alerts  precision {tp[r]/tot[r]:.2f}")
print(f"overall {sum(tp.values())}/{len(alerts)} = {sum(tp.values())/len(alerts):.2f}")
```

Run with `python3 lab_alerts.py`. Verified output:

```text
policy-p2p              6 alerts  precision 0.67
dns-tunnel-heuristic   10 alerts  precision 0.10
old-tls                 6 alerts  precision 1.00
smb-from-guest          3 alerts  precision 1.00
overall 14/25 = 0.56
```

### 19.3 Reading the precision

Of twenty-five alerts, fourteen were true, an overall precision of 0.56. The DNS tunnelling heuristic produced ten alerts with only one true, precision 0.10, mostly triggered by the learning platform's long, random-looking names. The old TLS rule and the guest file-sharing rule had precision 1.00. The peer-to-peer policy rule had 0.67. Tomás recommends tuning the DNS heuristic by excluding the learning platform's known domains, which should remove most false alerts while keeping the rule active for other traffic. High-precision rules are left unchanged.

### 19.4 Tuning safely

Tuning must not hide real problems. Tomás makes the DNS exclusion as narrow as possible, naming specific domains rather than whole categories, records why it was added and sets a review date. After tuning, he checks the next two weeks: DNS alerts fall from about ten to two a fortnight, and both are worth a look. He also keeps a small set of test events that should always alert, so he can confirm tuning has not accidentally silenced the rule entirely.

### Worked example

Overall precision is 0.56; the DNS heuristic's 0.10 precision is improved by a narrow, documented exclusion.

> **Synthetic case.** Alerts and labels are synthetic.

### Errors and limits

Broad exclusions added to reduce noise can silence real detections.

### Exercises

- **EX055 — Overall precision.** What is the overall alert precision in the sample? *Rubric:* 3 = 14 of 25, 0.56;; 2 = 0.56;; 1 = high;; 0 = none.
- **EX056 — Low precision cause.** Why did the DNS heuristic have low precision? *Rubric:* 3 = learning platform's random-looking names triggered it;; 2 = false triggers;; 1 = attacks;; 0 = none.
- **EX057 — Tuning check.** How does Tomás confirm tuning did not silence the rule? *Rubric:* 3 = test events that should always alert;; 2 = tests;; 1 = trust;; 0 = none.

### Synthesis

Measuring alert precision and tuning narrowly keep monitoring useful for a small team.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Network and communications security: troubleshooting

### Learning outcomes

You will (1) troubleshoot network problems methodically; (2) use logs and tests; (3) avoid weakening controls.

### 20.1 A method for problems

When something stops working after segmentation, the temptation is to remove rules until it works. Tomás follows a method instead: define the problem precisely, gather evidence from logs and tests, form a hypothesis, test it, fix the cause and verify. For example, "the science lab printer stopped printing at 9 a.m." is precise; "printing is broken" is not. Precise problem statements save time because they point to specific devices, zones and times to examine in the logs. Each step is noted in the ticket.

### 20.2 Logs as evidence

Denied connection logs are often the fastest way to find a missing flow. When the science lab printer fails, Tomás searches the firewall logs for denies involving its address around 9 a.m. He finds that teachers' laptops are trying to reach it on a port not in the needed-flows list, because this older printer uses a different printing protocol. The fix is a narrow rule allowing that protocol from staff to that printer only, recorded with its reason and owner.

### 20.3 Do not weaken controls

A common mistake is to fix problems with broad rules: "allow staff to everything in the shared devices zone". This works immediately but undoes segmentation, as the heating controller example showed. Tomás makes each fix as narrow as possible and records it. He also checks whether the problem reveals a gap in the flow list, updating it so the same problem does not recur at another site. Troubleshooting done well improves the design rather than eroding it. Gareth reviews every new rule weekly.

### 20.4 Communicating with users

During troubleshooting, the affected teacher needs to know what is happening. Tomás tells her the problem has been found and will be fixed within the hour, and suggests a nearby printer meanwhile. After fixing it, he confirms with her that it works. Clear communication reduces frustration and discourages workarounds such as students bringing in their own wireless devices. Gareth adds a simple form for reporting problems, including device, location and time, which makes later diagnosis much faster. The form is linked from the staff intranet.

### Worked example

The printer problem is traced through deny logs to a missing protocol and fixed with one narrow rule in under an hour.

> **Synthetic case.** The problem is synthetic.

### Errors and limits

Removing rules until things work quickly undoes segmentation.

### Exercises

- **EX058 — Precise statement.** Rewrite "printing is broken" as a precise problem statement. *Rubric:* 3 = specific printer, location and time;; 2 = specific;; 1 = still vague;; 0 = none.
- **EX059 — Printer cause.** Why was the science lab printer unreachable? *Rubric:* 3 = used protocol not in flow list;; 2 = missing protocol;; 1 = broken;; 0 = none.
- **EX060 — Report form fields.** Which details should a problem report include? *Rubric:* 3 = device, location and time;; 2 = details;; 1 = name only;; 0 = none.

### Synthesis

Methodical troubleshooting with logs and narrow fixes restores service without weakening security.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Network and communications security: service integration

### Learning outcomes

You will (1) integrate security with school services; (2) coordinate with suppliers; (3) keep services working through change.

### 21.1 The learning platform

The learning platform is hosted by a supplier on the internet and used by every student and teacher. After segmentation, Tomás confirms each zone that needs it can reach it: students, staff and remote VPN users. He checks that the platform's single sign-on works from every zone, since sign-on often depends on extra domains that are easy to miss. One missing domain in the DNS filter briefly blocks student logins during testing; adding it to the allowed list fixes the issue before term starts.

### 21.2 Managed printing

The managed print supplier monitors printer supplies and faults over the network. Its monitoring server must reach printers in the shared devices zone, but nothing else. Tomás and the supplier agree a narrow rule allowing their collection service to reach printers on the monitoring port only, with logging. The supplier also confirms which printer firmware updates they apply and when. Integrating suppliers this way lets them do their job without giving them wide access that would weaken the design. The rule is reviewed when the contract renews.

### 21.3 Heating controls

The heating company's direct remote access tool is replaced with access through the school VPN, using a named account for each engineer, reaching only the heating controller and logged. The company was initially reluctant, worried about delays in emergencies. Tomás and Gareth test the new path with the company's engineer, showing it takes under two minutes to connect. The contract is updated to require this path and notice of any changes. The scenario from chapter 13 is now addressed. The old remote access tool is uninstalled afterwards.

### 21.4 Change windows and communication

Integration changes happen in agreed windows, announced to staff and suppliers in advance with the expected effects and a contact for problems. Tomás drafts the announcements in plain language and Gareth sends them. After each window, a short note confirms what changed and lists any known issues. Regular, predictable communication builds confidence that the network team is careful, which in turn makes staff more willing to report problems early instead of improvising their own fixes. Announcements go out at least a week ahead, so teachers can plan lessons around any disruption.

### Worked example

Three supplier services are integrated with narrow rules; the heating company moves to named VPN accounts.

> **Synthetic case.** Suppliers are synthetic.

### Errors and limits

Giving suppliers broad access to avoid integration work undermines segmentation.

### Exercises

- **EX061 — Missing sign-on domain.** What caused the brief student login failure? *Rubric:* 3 = sign-on domain missing from DNS allowed list;; 2 = missing domain;; 1 = platform outage;; 0 = none.
- **EX062 — Print supplier rule.** What access does the print supplier receive? *Rubric:* 3 = only printers on monitoring port, logged;; 2 = printers;; 1 = full;; 0 = none.
- **EX063 — Heating reluctance.** How was the heating company's reluctance addressed? *Rubric:* 3 = tested new path, under two minutes to connect;; 2 = demonstration;; 1 = forced;; 0 = none.

### Synthesis

Careful integration lets school services and suppliers work within the secure design.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Network and communications security: automation

### Learning outcomes

You will (1) automate configuration backups; (2) detect drift with diffs; (3) automate safely.

### 22.1 Why automate

Gareth has many routine tasks and little time. Automation handles tasks that are repetitive, error-prone and easy to define: backing up configurations, comparing them with approved versions and checking certificates for expiry. Tomás chooses these first because they need no judgement and their output is easy to check. He avoids automating changes to live devices at this stage, since a mistaken automated change could affect the whole school at once, and a technician working alone may not notice quickly. Each automated task replaces a manual one.

### 22.2 Configuration backups

Each night, a small script collects the running configuration of each switch and the firewall using their export features, over encrypted management connections from the management zone. Configurations are stored with dates in a protected folder, and the script reports which devices failed to export. Backups support recovery after failures and give a history of changes. Tomás tests restoring a switch configuration in the lab to confirm the backups are complete and usable. Backups are kept for one year, and the folder is itself copied to the school's cloud backup service.

### Lab — Configuration drift

```python
"""Show drift between an approved and a running synthetic switch configuration (stdlib difflib)."""
import difflib
approved = """hostname sw-library
vlan 10 name staff
vlan 20 name students
vlan 30 name guest
interface port1 vlan 20
interface port2 vlan 20
ssh enable
telnet disable
logging host 10.50.9.10""".splitlines()
running = """hostname sw-library
vlan 10 name staff
vlan 20 name students
vlan 30 name guest
interface port1 vlan 20
interface port2 vlan 10
ssh enable
telnet enable
logging host 10.50.9.10""".splitlines()
d = [l for l in difflib.unified_diff(approved, running, "approved", "running", lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
print("\n".join(d)); print("changed lines:", len(d) // 2)
```

Run with `python3 lab_diff.py`. Verified output:

```text
-interface port2 vlan 20
+interface port2 vlan 10
-telnet disable
+telnet enable
changed lines: 2
```

### 22.3 Reading the drift

The synthetic comparison of the library switch's approved and running configuration shows two changes. Port 2 moved from the student zone to the staff zone, and Telnet has been re-enabled. Either could have a good explanation, such as a temporary fix, but neither went through change control. Gareth checks: a teacher asked for a staff connection in the library, and Telnet was enabled by mistake during a firmware update. Port 2 is approved with a change record; Telnet is disabled again.

### 22.4 Automating safely

Automated scripts run with privileged access, so they must be protected. Tomás stores the script's credentials in the operating system's protected store rather than in the script, limits the account to read-only export permissions and logs every run. The script is version-controlled and tested. If it fails, it alerts Gareth rather than retrying endlessly. These precautions ensure automation reduces risk rather than adding a new weakness that an attacker could exploit to change devices. Gareth reviews the script's run log each week as part of his routine.

### Worked example

Nightly backups cover thirteen devices; the drift report finds two changes, one approved and one reverted.

> **Synthetic case.** Configurations are synthetic.

### Errors and limits

Automation with broad write access can spread one mistake to every device.

### Exercises

- **EX064 — Drift findings.** What two changes does the drift comparison show? *Rubric:* 3 = port 2 to staff VLAN, Telnet enabled;; 2 = two;; 1 = one;; 0 = none.
- **EX065 — Read-only account.** Why give the backup script read-only permissions? *Rubric:* 3 = limits harm if misused or compromised;; 2 = safety;; 1 = speed;; 0 = none.
- **EX066 — Restore test.** Why test restoring a backup in the lab? *Rubric:* 3 = confirm backups complete and usable;; 2 = verify;; 1 = unnecessary;; 0 = none.

### Synthesis

Safe, read-only automation for backups and drift detection saves time and catches unapproved changes.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Network and communications security: evaluation

### Learning outcomes

You will (1) evaluate the changes against requirements; (2) measure support impact; (3) report results.

### 23.1 Requirements check

At the end of the autumn term, Tomás evaluates each requirement. R1 is met: tests and logs show no student or guest connections to administration or management. R2 is met: only listed flows cross zones. R3 is met: management uses SSH and HTTPS only from the management zone, apart from the Telnet slip caught by drift detection. R4 is met for staff wireless. R5 is met: all zones use school resolvers. R6 is met for logs, with ninety days confirmed in December.

### 23.2 Security indicators

Reachable zone pairs fell from thirty to the fourteen needed flows between zones. Unapproved services fell from four to one restricted exception. Leftover accounts fell from thirty-nine to zero after the termly review. Switches with insecure management fell from two to zero, briefly one when Telnet reappeared. Tomás reports each with before and after values and dates. These indicators show improvement in the risks ranked highest in chapter 5, which is the strongest argument for the project's value. The figures are shared with the governors.

### 23.3 Support impact

Security changes should not make support worse. Tomás compares network tickets before and after, using the time from report to resolution. He also asks whether runbooks written during the project helped. The synthetic ticket data show resolution times falling, which he attributes partly to clearer zones and logs that make problems easier to diagnose, and partly to the new reporting form. He notes that other factors could contribute, such as fewer new devices in the autumn term. He records these caveats beside the result.

### Lab — Resolution times

```python
"""Median time to resolve synthetic network tickets before and after runbooks (stdlib only)."""
import statistics
before = [95, 40, 210, 60, 130, 75, 300, 55, 90, 120]
after = [35, 50, 45, 80, 30, 150, 40, 60, 25, 55]
for n, x in (("before", before), ("after", after)):
    print(f"{n:7} n={len(x)} median {statistics.median(x):.1f} min, max {max(x)} min")
print(f"median change {100*(statistics.median(after)-statistics.median(before))/statistics.median(before):.1f}%")
```

Run with `python3 lab_mttr.py`. Verified output:

```text
before  n=10 median 92.5 min, max 300 min
after   n=10 median 47.5 min, max 150 min
median change -48.6%
```

### 23.4 Reading the times

The median resolution time falls from 92.5 to 47.5 minutes, a 48.6 percent reduction, and the longest ticket falls from 300 to 150 minutes. With ten tickets in each period, Tomás treats the result as encouraging rather than conclusive and uses medians because a single long ticket would distort the mean. He recommends continuing to record times so that a full year of data can confirm whether the improvement lasts. He also notes that fewer new devices joined in autumn, which could explain part of the change.

### Worked example

All six requirements are met; the median ticket resolution time falls by about half.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Small samples of tickets can show large changes by chance.

### Exercises

- **EX067 — Reachability change.** How did reachable zone pairs change? *Rubric:* 3 = thirty to fourteen needed flows;; 2 = reduced;; 1 = none;; 0 = none.
- **EX068 — Median change.** What was the median resolution change? *Rubric:* 3 = 92.5 to 47.5 minutes, −48.6%;; 2 = about half;; 1 = some;; 0 = none.
- **EX069 — Median reason.** Why use the median for ticket times? *Rubric:* 3 = one long ticket distorts mean;; 2 = skew;; 1 = easier;; 0 = none.

### Synthesis

Evaluation against requirements and support measures shows security improved without harming service.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) frame a small applied study; (2) collect data ethically; (3) analyse and report honestly.

### 24.1 A practical question

Ms Okafor asks each student to complete a small applied study. Tomás asks: does labelling alerts with a short response note reduce the time Gareth takes to handle them? The question is narrow, matters to the school and can be answered with data Gareth already records. He states the measure, time from alert to closure, and the comparison: four weeks without response notes against four weeks with them, during comparable term periods. He writes the question and comparison down before collecting any data, so the analysis cannot drift.

### 24.2 Ethics and consent

The study involves Gareth's work, so Tomás explains its purpose and asks for his consent, making clear that the study evaluates the process, not his performance. Data are anonymised before analysis and stored on college storage. The college's ethics checklist is completed and signed by Ms Okafor. Even small studies involving people need this care, because workers can feel judged by measurement, and trust is essential to a placement. Gareth may withdraw at any time, and the data would then be deleted without question.

### 24.3 Analysis

Tomás compares median handling times and checks the spread. Handling times fall from a median of 18 minutes to 11 with response notes. He looks for other explanations: were alerts in the second period simpler? He checks alert types and finds a similar mix. Was Gareth less busy? Ticket volumes were similar. These checks do not prove the notes caused the change, but they make other explanations less likely, which is as much as a small study can do. He reports the spread as well as medians.

### 24.4 Reporting

Tomás writes a four-page report: question, method, data, results, limitations and recommendation. Limitations include the small sample, one technician and the short period. He recommends keeping response notes and reviewing them each term. He presents the report to Gareth first, who adds context, then to Ms Okafor. Reporting honestly, including limitations, makes the study useful for the school and a good example of applied research for the course. The school keeps a copy of the report with its operational documents, so the evidence remains available after the placement.

### Worked example

Median handling time falls from 18 to 11 minutes with response notes, with a similar alert mix in both periods.

> **Synthetic case.** The study is synthetic.

### Errors and limits

Studies of people's work without consent and clear purpose damage trust.

### Exercises

- **EX070 — Study measure.** What does the study measure? *Rubric:* 3 = time from alert to closure;; 2 = handling time;; 1 = alerts;; 0 = none.
- **EX071 — Alternative explanation check.** Name one alternative explanation Tomás checked. *Rubric:* 3 = simpler alerts or lower workload;; 2 = one;; 1 = none;; 0 = none.
- **EX072 — Consent framing.** How was the study framed to Gareth? *Rubric:* 3 = evaluates process, not performance;; 2 = process;; 1 = performance;; 0 = none.

### Synthesis

Small, ethical, honest applied studies produce useful evidence for practice.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) work in a team on a network design; (2) divide roles; (3) review each other's work.

### 25.1 The studio task

In the second year, Ms Okafor runs a team studio. Tomás's team of four designs network security for a fictional primary school with similar needs but no technician, relying on a managed service provider. The team must produce a zone design, needed flows, rules, a monitoring plan and a handover pack for the provider. The task tests whether students can apply what they learned at Ridgeway to a new context with different constraints. Each team presents its design to classmates and Ms Okafor at the end of term for questions and marks.

### 25.2 Roles and coordination

The team divides roles: one leads the zone design, one the rules, one monitoring and one documentation, with Tomás coordinating. They meet twice a week, track tasks on a shared board and keep decisions in a log. Clear roles avoid duplicated effort, but the team also agrees that everyone reviews everything, so knowledge is shared. Coordination takes time, but without it, pieces designed separately often fail to fit together. Roles rotate halfway through so everyone experiences each part of the design work.

### 25.3 Peer review

Each team member's work is reviewed by another. Reviewing the rules, Tomás finds a rule allowing the provider remote access to every zone, which contradicts the design's principle of narrow supplier access. The author explains it was a placeholder; it is replaced with specific flows. Reviews catch such errors because reviewers read what was written, not what was intended. The team keeps review comments and responses in the log, showing how the design improved. Reviews follow a short checklist of common errors.

### 25.4 Adapting to context

The primary school has no technician, so the design must be simpler than Ridgeway's and rely on the provider. The team reduces zones to four, chooses a provider-managed firewall with clear reporting and writes a one-page guide for the head teacher on what to check monthly. Adapting a design to a different context, rather than copying it, is a key professional skill, and the studio deliberately chose a context that forced such adaptation. The guide is tested by a parent volunteer who reads it cold.

### Worked example

The team's design uses four zones, eleven flows and a monthly checklist for the head teacher.

> **Synthetic case.** The studio school is fictional.

### Errors and limits

Copying a design from one organisation to another without adapting it to staff and context leads to failure.

### Exercises

- **EX073 — Placeholder rule.** What did Tomás find in peer review? *Rubric:* 3 = provider remote access to every zone;; 2 = broad rule;; 1 = none;; 0 = none.
- **EX074 — Fewer zones reason.** Why does the primary school design use four zones? *Rubric:* 3 = no technician, simpler to run;; 2 = simpler;; 1 = cheaper;; 0 = none.
- **EX075 — Everyone reviews.** Why does everyone review everything despite divided roles? *Rubric:* 3 = shared knowledge, pieces fit;; 2 = sharing;; 1 = slow;; 0 = none.

### Synthesis

Team studios practise coordination, peer review and adaptation of designs to new contexts.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Network and communications security: operational handoff

### Learning outcomes

You will (1) prepare operations for the long term; (2) write runbooks; (3) transfer ownership.

### 26.1 Runbooks

A runbook gives step-by-step instructions for a routine task. Tomás writes runbooks for adding a new device to the right zone, handling a blocked-service report, reviewing weekly alerts, restoring a switch from backup and running the termly account review. Each includes when to use it, steps, expected results and what to do if something goes wrong. He tests each runbook by having another student follow it in the lab without help, fixing unclear steps. Runbooks are stored with the network documentation and updated after every incident.

### 26.2 Routines

Gareth's weekly routine takes about thirty minutes: review alert summaries, check the drift report, confirm every device sent logs and check certificates expiring within sixty days. Termly tasks include the account review and the service comparison. Annual tasks include reviewing zones and flows with stakeholders. A written schedule makes the routines visible to the head teacher, who can check they are happening, and helps a replacement technician pick them up. Each completed routine is ticked off in a shared log, so missed weeks are easy to spot.

### 26.3 Ownership and support

Each part of the design has an owner: Gareth for network devices and rules, the business manager for administration zone access decisions, the safeguarding lead for filtering categories, and suppliers for their services under contract. Tomás records these in a responsibility table approved by the head teacher. He also arranges, with the school's agreement, a small support contract with a local provider for emergencies when Gareth is unavailable. Owners are reminded of their duties at the start of each school year.

### 26.4 Handover meeting

At the handover meeting, Tomás walks through the documentation, routines and open items with Gareth, the head teacher and Ms Okafor. Open items include replacing the old printers that need the raw printing port and reviewing the DNS exclusion in spring. Gareth signs acceptance of the documentation. A formal handover marks the point where responsibility clearly passes, so nothing falls between the end of the placement and normal operations. The signed acceptance is filed with the documentation, and Ms Okafor confirms the placement objectives were met.

### Worked example

Five runbooks, a weekly thirty-minute routine and a responsibility table are handed over with two open items.

> **Synthetic case.** Handover is synthetic.

### Errors and limits

Runbooks never tested by someone else often contain steps only the author understands.

### Exercises

- **EX076 — Runbook test.** How were runbooks tested? *Rubric:* 3 = another student followed them unaided in lab;; 2 = followed;; 1 = reviewed;; 0 = none.
- **EX077 — Weekly routine items.** List three weekly routine items. *Rubric:* 3 = alerts, drift report, log arrival or certificates;; 2 = two;; 1 = one;; 0 = none.
- **EX078 — Open item.** Name one open item at handover. *Rubric:* 3 = replace old printers or review DNS exclusion;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Tested runbooks, written routines and clear ownership let operations continue after the project.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) deploy remaining changes; (2) validate with users; (3) confirm requirements in operation.

### 27.1 Remaining deployment

In the spring holiday, Gareth and Tomás deploy the remaining changes: student wireless individual accounts, client isolation on student wireless and the VPN for remote staff. They follow the same staged approach: lab rehearsal, change window, tests and rollback plan. The deployment takes two days. One problem appears: some older student laptops cannot use the new wireless authentication method. They are placed on a temporary restricted network until replaced, with an end date agreed. The rollback plan is ready but not needed.

### 27.2 Validating with users

Validation asks whether the network meets people's real needs, not just the written requirements. Tomás asks a sample of teachers, office staff and students, through a short form, whether anything they need stopped working or became harder. Most report no change; three report issues, including a teacher who cannot reach a shared folder from home, which was missing from the VPN's allowed list. Validation catches needs that requirements missed and builds users' confidence. Every reported issue receives a reply explaining the fix.

### 27.3 Requirements in operation

Tomás rechecks the requirements under normal school operation rather than test conditions. Logs from a full week show no denied traffic suggesting a broken need, other than the reported folder, now fixed. Drift reports show no unapproved changes. Alerts are reviewed on time. Confirming requirements in operation matters because tests in quiet holidays may miss behaviour that only appears when 1,200 people use the network during lessons. He records the week used and the counts found, so the operational check can be repeated each term with the same method.

### 27.4 Temporary arrangements

Temporary arrangements, such as the restricted network for old laptops, tend to become permanent if nobody tracks them. Tomás records each with an owner, a reason and an end date in the open items list. Gareth reviews the list monthly. When the old laptops are replaced at the end of the year, the temporary network is removed. Tracking temporary measures is a simple habit that prevents gradual weakening of the design. The list also shows each item's age, making old exceptions stand out.

### Worked example

Remaining changes are deployed in two days; user validation finds three issues, all fixed; one temporary network is tracked to removal.

> **Synthetic case.** Deployment is synthetic.

### Errors and limits

Temporary exceptions without end dates become permanent weaknesses.

### Exercises

- **EX079 — Old laptops.** How were older laptops handled? *Rubric:* 3 = temporary restricted network with end date;; 2 = temporary;; 1 = excluded;; 0 = none.
- **EX080 — Validation finding.** What did validation find for remote access? *Rubric:* 3 = shared folder missing from VPN allowed list;; 2 = folder;; 1 = none;; 0 = none.
- **EX081 — Operational check.** Why recheck requirements during term? *Rubric:* 3 = holiday tests miss full-use behaviour;; 2 = real use;; 1 = unnecessary;; 0 = none.

### Synthesis

Staged deployment, user validation and tracked exceptions confirm the design works in daily use.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) work professionally in a live school; (2) handle incidents with supervision; (3) reflect on practice.

### 28.1 Professional conduct in a school

Working in a school has particular rules. Tomás wears his visitor badge, signs in and out, never works alone with students, and avoids looking at screens showing student information. He schedules work around lessons and keeps noise and disruption minimal. Safeguarding training is required before the placement. Professional conduct is part of technical work in such settings; a technically excellent change made in a way that breaks safeguarding rules would be a serious failure. Gareth briefs him on the school's specific rules.

### 28.2 A real incident

During the spring term, alerts show repeated denied connections from one student laptop towards the administration zone, along with DNS lookups of a newly registered domain. Following the runbook, Gareth disconnects the laptop from the network and contacts the student's head of year. The laptop is found to have malware from a game download. It is cleaned and returned. Segmentation stopped the attempts reaching administration, and monitoring made the event visible within minutes. The student's family is informed by the school following its normal procedures.

### 28.3 Supervision and boundaries

Tomás assists Gareth during the incident but does not act alone, consistent with the placement agreement. He helps search logs and drafts the incident note. He does not handle the student or the device directly. Working under supervision in real incidents teaches how procedures play out in practice while protecting the school and the student. Afterwards, Gareth and Tomás review the incident and update the runbook to include contacting the safeguarding lead when a student's device is involved. The incident note is filed.

### 28.4 Reflective practice

Tomás keeps a reflective journal during field practice. After the incident, he writes about what went well, what was unclear and what he would do differently. He notes that the runbook did not say who should speak to the student, which caused a short delay. Reflection turns experience into learning and gives material for his capstone. Ms Okafor reads the journal monthly and discusses it with him, linking events to course concepts. Entries are short and written the same day.

### Worked example

One malware incident is contained within minutes; the runbook gains a safeguarding contact step.

> **Synthetic case.** The incident is synthetic.

### Errors and limits

Students on placement acting alone in incidents can breach agreements and harm trust.

### Exercises

- **EX082 — Incident detection.** How was the infected laptop noticed? *Rubric:* 3 = repeated denies and DNS lookups of new domain;; 2 = alerts;; 1 = complaint;; 0 = none.
- **EX083 — Runbook update.** What was added to the runbook after the incident? *Rubric:* 3 = contact safeguarding lead for student devices;; 2 = safeguarding;; 1 = none;; 0 = none.
- **EX084 — Tomás's role.** What did Tomás do during the incident? *Rubric:* 3 = searched logs and drafted note under supervision;; 2 = assisted;; 1 = led;; 0 = none.

### Synthesis

Professional conduct, supervised incident work and reflection make field practice valuable.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) build a capstone deliverable; (2) integrate earlier work; (3) test thoroughly.

### 29.1 Choosing the capstone

For his capstone, Tomás builds a "network health pack" for Ridgeway: a set of scripts and a one-page dashboard that combine the drift report, log arrival check, certificate expiry, alert precision and account review status into a single weekly summary for Gareth and the head teacher. The capstone integrates earlier work into something the school will use every week, which makes it both a learning exercise and a lasting contribution. Gareth agrees the scope and confirms the summary would save him time each week.

### 29.2 Building it

Tomás uses the standard library only, so the pack runs on the school's existing management server. Each check is a small function with tests. The summary is a simple text and HTML page with green, amber and red statuses and a short explanation for anything amber or red. He keeps the design modular so Gareth can add checks later. All development happens in the lab with synthetic data; only after testing does Gareth install it at school with real data under his control.

### 29.3 Testing

Tomás writes tests for each check with normal, edge and failure cases: a device that stopped sending logs yesterday, a certificate expiring in 59 days, a configuration with one changed line, and an empty alert file. He also tests the whole pack end to end with a full synthetic week. Two bugs are found: a date comparison off by one day and a crash on an empty file. Both are fixed and tests added so they cannot return unnoticed. The tests run before every release.

### 29.4 Security of the pack

The pack reads sensitive configuration and log data, so it runs under a read-only account in the management zone, stores no credentials in code, writes output only to a protected folder and logs its own runs. The HTML summary contains no passwords, addresses or student data. Tomás asks a classmate to review the code for security issues. Building secure tooling is part of the capstone's assessment, since a monitoring tool that leaks data would undermine the purpose of the project.

### Worked example

The health pack runs five checks weekly; testing finds two bugs, both fixed with new tests.

> **Synthetic case.** The pack is synthetic.

### Errors and limits

Tools developed on live data before testing risk errors and data exposure.

### Exercises

- **EX085 — Capstone purpose.** What does the network health pack provide? *Rubric:* 3 = single weekly summary of five checks;; 2 = summary;; 1 = alerts;; 0 = none.
- **EX086 — Bugs found.** Name the two bugs found in testing. *Rubric:* 3 = off-by-one date comparison, crash on empty file;; 2 = two;; 1 = one;; 0 = none.
- **EX087 — Pack security.** List two security measures for the pack. *Rubric:* 3 = read-only account, no credentials in code, protected output, no sensitive data;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

A tested, secure capstone tool integrates earlier work into lasting value for the school.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) present the capstone; (2) evaluate its value; (3) reflect on the programme.

### 30.1 Presentation

Tomás presents his capstone to Ms Okafor, an external assessor from industry, and Gareth. He explains the school's starting point, the changes made over the placement, the evidence of improvement and the health pack. He demonstrates the pack with synthetic data. The assessor asks what happens when Gareth is away; Tomás shows that the summary goes to the head teacher too and that the support contract covers emergencies. Gareth adds his own view of how the changes affected daily work at the school.

### 30.2 Evaluating value

To show the pack's value, Tomás reports Gareth's feedback after six weeks of use: the weekly review takes twenty minutes instead of thirty, and the pack caught one device that stopped logging within a day. He is careful not to overclaim: six weeks is short, and one catch is not a trend. The assessor values the honest evaluation and the fact that the school continues to use the tool after the placement ends. He suggests reviewing the pack's value again after a full school year.

### 30.3 Assessment criteria

The capstone is assessed on technical quality, security of the tool, evidence of value, documentation and professional practice. Tomás's documentation includes installation steps, a user guide, test results and a maintenance note. The assessor notes that the documentation would let another technician maintain the tool, which is an important criterion for work in organisations with few staff, where a tool understood only by its author soon becomes a liability. The assessor also checks that tests are included and pass. Marks are moderated.

### 30.4 Reflection on the programme

Tomás reflects on three years. He started thinking security meant tools and rules; he finishes understanding that it also means inventories, people, suppliers, routines and honest evidence. He notes that small, steady improvements at Ridgeway, such as termly account reviews and drift detection, mattered as much as the big segmentation change. He plans to work as a network technologist in education, where he has seen how much difference careful, practical work can make. Ms Okafor adds the reflection to the course's examples for future students.

### Worked example

The capstone passes with commendation for honest evaluation and maintainable documentation.

> **Synthetic case.** The assessment is synthetic.

### Errors and limits

Claiming broad benefits from a few weeks' use overstates a tool's value.

### Exercises

- **EX088 — Absence plan.** How does the health pack handle Gareth's absence? *Rubric:* 3 = summary to head teacher, support contract;; 2 = shared;; 1 = none;; 0 = none.
- **EX089 — Measured value.** Give two measured benefits after six weeks. *Rubric:* 3 = review 30 to 20 minutes, one logging failure caught;; 2 = one;; 1 = none;; 0 = none.
- **EX090 — Maintainability criterion.** Why is maintainability important in small organisations? *Rubric:* 3 = tool understood only by author becomes a liability;; 2 = few staff;; 1 = none;; 0 = none.

### Synthesis

The technologist route ends with practical, evidenced improvements and a maintainable contribution.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Tomás Rivera, Hannah Okafor, Greystone Polytechnic, Ridgeway Secondary School and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** They often run outdated firmware while sharing a network with many users.

**EX002.** By the services it offers, their ports and which clients use them.

**EX003.** A forgotten data-logging server still connected to the student network.

**EX004.** Internal traffic stays within one subnet and never passes the gateway.

**EX005.** Most stop working, even though the network itself still functions.

**EX006.** All three lead into the same subnet without rules between them.

**EX007.** Finding services that are observed but not approved, and the reverse.

**EX008.** Logs may contain text typed by users or attackers.

**EX009.** Count them and report the number in the output.

**EX010.** Records remain valid when the people in those roles change.

**EX011.** Gareth can open and edit it in a spreadsheet.

**EX012.** By year group rather than by name, unless otherwise approved.

**EX013.** A failure during lessons or exams affects hundreds of people at once.

**EX014.** Curious students testing what they can reach.

**EX015.** The policy states rules, technical controls enforce them and logs show attempts.

**EX016.** Anyone reaching it can control every virtual machine on that host.

**EX017.** A compromised web server could reach the finance server directly.

**EX018.** To avoid disrupting real users and breaching agreements.

**EX019.** Students know it, and it cannot identify or revoke individuals.

**EX020.** It limits harm if his everyday account is phished.

**EX021.** At the start of each term, compared with current student and staff lists.

**EX022.** None; that zone pair has no allowed flows.

**EX023.** Telnet sends passwords unencrypted across the network.

**EX024.** Saltzer and Schroeder's economy of mechanism.

**EX025.** Thirty, since each of six zones pairs with five others.

**EX026.** Record the change and, if possible, measure once with both methods.

**EX027.** As "2 of 2 switches" rather than 100 percent.

**EX028.** Reducing implicit trust and checking access at internal boundaries.

**EX029.** Any change could disrupt exams, where availability is critical.

**EX030.** Make changes to the school network without Gareth's approval.

**EX031.** The core switch, because it connects every building.

**EX032.** She learned that student devices share a network with finance systems.

**EX033.** Routed through a controlled path with named accounts.

**EX034.** Six of twelve, 50 percent.

**EX035.** It may indicate an infected device trying to reach a controller.

**EX036.** It stops devices bypassing filtering and keeps DNS logs complete.

**EX037.** Separation removes the opportunity, so safety does not depend on the student's restraint.

**EX038.** The teaching file shares, so backups and host protection stay essential.

**EX039.** It showed how a forgotten connection could expose the whole school to outsiders.

**EX040.** Management, so network devices are protected and manageable for later stages.

**EX041.** From the student zone, connections to admin and management fail while the learning platform works.

**EX042.** A projector failure on the first day of term disrupts lessons immediately.

**EX043.** Four unapproved services and none missing.

**EX044.** The raw printing port, restricted to the shared devices zone with a review date.

**EX045.** From the systems' own management exports with Gareth's authorisation, not scanning.

**EX046.** It stops student devices connecting directly to each other.

**EX047.** Direct exposure is risky; a VPN with a second factor and restricted access is safer.

**EX048.** Logs then show which person made each change.

**EX049.** What problem it solves, whether Gareth can run it, and its cost.

**EX050.** He uses data exported by the systems themselves with Gareth's approval.

**EX051.** People believe logs exist when they do not.

**EX052.** It let staff reach the heating controller in the shared devices zone.

**EX053.** To stop anyone plugging unknown devices into the network.

**EX054.** A rule referred to the wrong zone.

**EX055.** Fourteen of twenty-five, precision 0.56.

**EX056.** The learning platform's long, random-looking names triggered it.

**EX057.** He keeps test events that should always trigger the rule.

**EX058.** "The science lab printer stopped printing at 9 a.m."

**EX059.** It used a printing protocol not in the needed-flows list.

**EX060.** The device, location and time of the problem.

**EX061.** A single sign-on domain missing from the DNS filter's allowed list.

**EX062.** Only printers in the shared devices zone, on the monitoring port, logged.

**EX063.** By testing the new path together and showing it takes under two minutes.

**EX064.** Port 2 moved to the staff zone and Telnet was re-enabled.

**EX065.** It limits the damage if the script or its account is misused.

**EX066.** To confirm the backups are complete and actually usable.

**EX067.** From thirty to the fourteen needed flows.

**EX068.** From 92.5 to 47.5 minutes, a 48.6 percent reduction.

**EX069.** A single long ticket would distort the mean.

**EX070.** The time from alert to closure.

**EX071.** Whether alerts in the second period were simpler.

**EX072.** As an evaluation of the process, not of his performance.

**EX073.** A placeholder rule giving the provider access to every zone.

**EX074.** With no technician, a simpler design is easier to run.

**EX075.** To share knowledge and make sure the pieces fit together.

**EX076.** Another student followed each in the lab without help.

**EX077.** Reviewing alerts, checking the drift report and confirming log arrival.

**EX078.** Replacing the old printers that need the raw printing port.

**EX079.** On a temporary restricted network with an agreed end date.

**EX080.** A teacher's shared folder was missing from the VPN allowed list.

**EX081.** Holiday tests may miss behaviour seen only during full use.

**EX082.** Repeated denied connections and lookups of a newly registered domain.

**EX083.** A step to contact the safeguarding lead when a student's device is involved.

**EX084.** He searched logs and drafted the incident note under Gareth's supervision.

**EX085.** A single weekly summary combining five health checks.

**EX086.** A date comparison off by one day and a crash on an empty file.

**EX087.** A read-only account and no credentials stored in code.

**EX088.** The summary also goes to the head teacher, and a support contract covers emergencies.

**EX089.** The weekly review fell from thirty to twenty minutes, and one logging failure was caught.

**EX090.** With few staff, a tool only its author understands soon becomes a liability.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Barker, E., Dang, Q., Frankel, S., Scarfone, K., & Wouters, P. (2020). *Guide to IPsec VPNs* (NIST SP 800-77 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-77r1>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Chandramouli, R., & Rose, S. (2013). *Secure Domain Name System (DNS) deployment guide* (NIST SP 800-81-2). NIST. <https://doi.org/10.6028/NIST.SP.800-81-2>
- Claise, B., Trammell, B., & Aitken, P. (2013). *Specification of the IP Flow Information Export (IPFIX) protocol* (RFC 7011). IETF. <https://www.rfc-editor.org/rfc/rfc7011>
- Ferguson, P., & Senie, D. (2000). *Network ingress filtering* (RFC 2827, BCP 38). IETF. <https://www.rfc-editor.org/rfc/rfc2827>
- Gerhards, R. (2009). *The Syslog protocol* (RFC 5424). IETF. <https://www.rfc-editor.org/rfc/rfc5424>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kaufman, C., Hoffman, P., Nir, Y., Eronen, P., & Kivinen, T. (2014). *Internet Key Exchange Protocol Version 2 (IKEv2)* (RFC 7296). IETF. <https://www.rfc-editor.org/rfc/rfc7296>
- Kent, S., & Seo, K. (2005). *Security architecture for the Internet Protocol* (RFC 4301). IETF. <https://www.rfc-editor.org/rfc/rfc4301>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Lepinski, M., & Kent, S. (2012). *An infrastructure to support secure Internet routing* (RFC 6480). IETF. <https://www.rfc-editor.org/rfc/rfc6480>
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Paxson, V. (1999). Bro: A system for detecting network intruders in real-time. *Computer Networks*, 31(23–24), 2435–2463. <https://doi.org/10.1016/S1389-1286(99)00112-7>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., & Hoffman, P. (2009). *Guidelines on firewalls and firewall policy* (NIST SP 800-41 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-41r1>
- Scarfone, K., & Mell, P. (2007). *Guide to intrusion detection and prevention systems (IDPS)* (NIST SP 800-94). NIST. <https://doi.org/10.6028/NIST.SP.800-94>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *2010 IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Souppaya, M., & Scarfone, K. (2012). *Guidelines for securing wireless local area networks (WLANs)* (NIST SP 800-153). NIST. <https://doi.org/10.6028/NIST.SP.800-153>
- Sriram, K., & Montgomery, D. (2019). *Resilient interdomain traffic exchange: BGP security and DDoS mitigation* (NIST SP 800-189). NIST. <https://doi.org/10.6028/NIST.SP.800-189>
- Wool, A. (2004). A quantitative study of firewall configuration errors. *Computer*, 37(6), 62–67. <https://doi.org/10.1109/MC.2004.2>
