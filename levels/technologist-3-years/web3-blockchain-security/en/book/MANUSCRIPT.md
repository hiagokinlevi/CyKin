# Web3, Blockchain and Cryptoasset Security: Technologist Degree

- Language: English (`en`); course 078, Technologist degree (3 years).
- Editorial state: **published**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students learning to operate, monitor and maintain blockchain systems securely in small organisations.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only contracts, wallets and systems you are authorised to assess, on local simulations or test networks; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic ledgers, transactions, contract inventories and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one student technologist operating a makerspace's booking-credit token on a three-node permissioned ledger, from computing, networks, programming and data, through identity, architecture and evidence, to assets, data flows, risk, review methods, tooling, controls, monitoring, troubleshooting, integration, automation, evaluation, handoff, deployment, field practice and a capstone. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lucas Moreau** | Technologist student | Invented |
| **Ms Grace Adebayo** | Instructor | Invented |
| **Pinecrest Technical College** | Fictional college | Invented |
| **Tidewater Makerspace** | Fictional client (about 350 members) | Invented |

### Core sources

Nakamoto, [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf); Wood, [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf); NIST [IR 8202](https://doi.org/10.6028/NIST.IR.8202); [SWC registry](https://swcregistry.io/); [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/); EEA [EthTrust Security Levels v3](https://entethalliance.org/specs/ethtrust-sl/v3/); [ConsenSys smart contract best practices](https://consensys.github.io/smart-contract-best-practices/); Atzei et al. ([2017](https://doi.org/10.1007/978-3-662-54455-6_8)); Luu et al. ([2016](https://doi.org/10.1145/2976749.2978309)). Full list in [References](#references).

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

You will (1) describe the parts of a computer; (2) explain how software runs; (3) relate hardware to ledger nodes.

### 1.1 The case and the computer

Lucas Moreau is a student technologist at the fictional Pinecrest Technical College, guided by his instructor Ms Grace Adebayo. Over three years he will support the fictional Tidewater Makerspace, about 350 members, which issues equipment-booking credits as tokens on a small permissioned Ethereum-compatible test ledger run on three nodes. Members earn credits by teaching workshops and spend them to book laser cutters and 3D printers. Every person, address and figure in this book is synthetic. Lucas starts with the computer itself, because every ledger node is just software running on ordinary hardware with ordinary limits.

### 1.2 How software runs

A program is a set of instructions stored on disk. When started, the operating system loads it into memory and the processor executes it, reading and writing data as it goes. A ledger node is a long-running program that listens on the network, processes transactions and blocks, and saves results to disk. Lucas watches a test node start on a lab machine and sees it read its configuration, open its database, connect to peers and begin syncing. Seeing each step helps him understand later error messages, which usually point to one of those stages failing for a specific reason.

### 1.3 Hardware and ledger nodes

Lucas lists what a node needs: enough processor to validate blocks quickly, enough memory to hold recent state, fast disk for the growing database, a reliable network link and an accurate clock. The makerspace's three nodes run on small servers in a rented rack. He records each server's specification and current usage. Ms Adebayo explains that most node problems technologists meet are resource problems, such as a full disk or an overloaded processor, rather than exotic ledger faults. Knowing the hardware is the first step to keeping nodes healthy and quickly diagnosing them when they are not.

### Worked example

Lucas records each server's specification and usage, noting that a node needs processor, memory, fast disk, network and an accurate clock.

> **Synthetic case.** Lucas Moreau, Ms Grace Adebayo, Pinecrest Technical College, Tidewater Makerspace and all data are synthetic.

### Errors and limits

Blaming the ledger software for every fault overlooks common resource problems such as a full disk.

### Exercises

- **EX001 — Makerspace size.** How many members does Tidewater Makerspace have? *Rubric:* 3 = about 350;; 2 = 350;; 1 = 3,500;; 0 = none.
- **EX002 — Node startup.** Name one step Lucas sees during node start. *Rubric:* 3 = connect to peers;; 2 = open the database;; 1 = print a receipt;; 0 = none.
- **EX003 — Common fault.** What kind of problem do technologists most often meet? *Rubric:* 3 = resource problems such as a full disk;; 2 = resources;; 1 = exotic ledger faults;; 0 = none.

### Synthesis

Ordinary hardware limits explain many ledger node problems.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain addresses, ports and protocols; (2) describe how nodes talk to each other; (3) secure exposed services.

### 2.1 Addresses, ports and protocols

Every device on a network has an address, and each service on it listens on a port. Protocols define how messages are formatted and exchanged. Lucas maps the makerspace's network: the three node servers, the booking web application, members' devices and the office router. He lists which ports each node uses for peer connections and for its programming interface, which the booking application uses to read balances and submit transactions. Knowing addresses and ports lets him check what is reachable from where, which is the basis of network security and of fault finding.

### 2.2 How nodes communicate

Nodes exchange blocks and transactions with peers over the internet. On the makerspace's permissioned ledger, each node is configured with an allow-list of the other two nodes and refuses others. The booking application talks to one node's programming interface. Lucas traces a booking: a member's wallet signs a transaction, the booking application sends it to a node, the node shares it with peers, the next block includes it and the application confirms the booking. Each hop is a place where delays or failures can occur, and each needs monitoring to show where a slow booking is held up.

### 2.3 Securing exposed services

The node programming interface can submit transactions and read data, so it must not be open to the whole internet. Lucas checks and finds that one node's interface is reachable from outside the rack. He reports it, and the firewall is changed so only the booking application server can reach it. He also confirms that administrative access requires keys, not passwords. NIST IR 8202 notes that permissioned networks depend on controlling who can participate and connect. Restricting exposed services is one of the simplest and most effective controls a technologist can apply on day one.

### Worked example

Lucas finds one node's programming interface reachable from the internet and has the firewall limit it to the booking server.

> **Synthetic case.** The network and findings are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Leaving a node's programming interface open to the internet exposes functions meant only for trusted applications.

### Exercises

- **EX004 — Interface user.** Which application uses a node's programming interface? *Rubric:* 3 = the booking web application;; 2 = booking app;; 1 = members' phones directly;; 0 = none.
- **EX005 — Booking path.** Name one hop in a booking's journey. *Rubric:* 3 = node shares with peers;; 2 = wallet signs;; 1 = email;; 0 = none.
- **EX006 — Exposure fix.** How was the exposed interface fixed? *Rubric:* 3 = firewall limited it to the booking server;; 2 = firewall;; 1 = removed node;; 0 = none.

### Synthesis

Mapping addresses and ports and restricting exposed services secure node communication.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write simple scripts; (2) read structured data; (3) build small checks for ledger data.

### 3.1 Writing simple scripts

Lucas writes Python scripts using only the standard library. His first reads a text file of booking records, counts bookings per machine and prints the totals. He learns variables, loops, conditions and functions by solving real tasks. Ms Adebayo asks him to add comments explaining why, not just what, each part does, so a colleague can maintain it. Scripts save time on repetitive checks and make them consistent. A check written as a script runs the same way every time, unlike a manual check that depends on someone's attention on a busy afternoon.

### 3.2 Reading structured data

Ledger tools often output JSON, a structured text format of keys and values. Lucas reads JSON with Python's json module and extracts block numbers, transaction counts and timestamps. He handles missing fields carefully, using defaults and printing warnings rather than crashing. He also reads CSV files exported from the booking system. Structured data is easier to check than free text because fields have names. He learns to validate data before using it, checking types and ranges, so that one bad record cannot produce misleading totals that someone might act on without noticing the problem.

### 3.3 Small checks for ledger data

Lucas writes a script that compares the number of booking credits spent in the booking system with the number recorded on the ledger for the same day. If they differ, it lists the bookings involved. On a synthetic day of 64 bookings, both show 64. He then alters one test record and confirms the script reports a mismatch. Testing a check with known bad data proves it works. Ms Adebayo notes that such small scripts, kept in version control and reviewed, form the backbone of practical security operations in small organisations like the makerspace.

### Worked example

Lucas's daily comparison matches 64 bookings in both systems and correctly reports a mismatch when one test record is altered.

> **Synthetic case.** The scripts and booking data are synthetic.

### Errors and limits

A check never tested with known bad data may silently fail to detect anything.

### Exercises

- **EX007 — Comment purpose.** What should comments explain? *Rubric:* 3 = why each part does what it does;; 2 = why;; 1 = vague;; 0 = none.
- **EX008 — Missing fields.** How are missing JSON fields handled? *Rubric:* 3 = defaults and warnings rather than crashing;; 2 = warnings;; 1 = crash;; 0 = none.
- **EX009 — Synthetic day result.** How many bookings matched on the synthetic day? *Rubric:* 3 = 64;; 2 = sixty-four;; 1 = 46;; 0 = none.

### Synthesis

Simple, tested scripts that read structured data make checks reliable.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) design simple data models; (2) separate on-ledger and off-ledger data; (3) protect personal data in models.

### 4.1 Designing data models

A data model describes what information a system keeps and how pieces relate. Lucas models the makerspace's booking system: members, machines, bookings, workshops taught and credits earned. Each booking links a member to a machine and a time slot. He draws the model as boxes and lines before building anything. Good models prevent errors: a booking without a valid machine should be impossible. He also models the token side, where a credit balance belongs to an address. Seeing both models side by side shows exactly where the two systems must agree and where mistakes might creep in.

### 4.2 On-ledger and off-ledger data

Not all data should go on the ledger. Lucas keeps member names, emails and safety training records in the booking database, which can be corrected and deleted. The ledger holds only credit balances and transfers linked to addresses. A mapping from member to address is kept in the database with restricted access. He records why each item is placed where it is. NIST IR 8202 explains that ledger data is replicated and hard to remove, so careful placement protects privacy and makes later corrections possible without needing to alter an immutable record.

### 4.3 Personal data in models

Lucas marks every personal field in the model and asks whether it is needed. Birth dates were collected for no clear reason, so he proposes dropping them. Safety training dates are needed to allow machine bookings. Emails are needed for notices. He also limits who can see each field: workshop leaders see names and training status, while only the manager sees emails. Data protection begins in the model, because fields that are never collected cannot leak. The manager approves the changes and Lucas updates the model diagram and its notes accordingly.

### Worked example

Lucas keeps names and training records off-ledger, stores only balances and transfers on-ledger, and drops unneeded birth dates.

> **Synthetic case.** The data models are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Placing personal data on a replicated ledger makes later correction or deletion very hard.

### Exercises

- **EX010 — Model entities.** Name one entity in the booking model. *Rubric:* 3 = machines;; 2 = bookings;; 1 = weather;; 0 = none.
- **EX011 — Mapping location.** Where is the member-to-address mapping kept? *Rubric:* 3 = in the database with restricted access;; 2 = database;; 1 = on-ledger;; 0 = none.
- **EX012 — Dropped field.** Which field does Lucas propose dropping? *Rubric:* 3 = birth dates;; 2 = birth date;; 1 = email;; 0 = none.

### Synthesis

Thoughtful data models place information where it can be protected and corrected.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core security goals; (2) identify assets and threats in the makerspace; (3) describe layered controls.

### 5.1 Core security goals

Lucas learns the core goals of confidentiality, integrity and availability, plus accountability. For the makerspace, confidentiality protects members' contact and training data; integrity ensures credit balances and bookings are correct; availability means members can book machines when they need them; and accountability means actions such as granting credits can be traced to a person. He notes that the ledger strengthens integrity and accountability, because records are hard to change and signed, but does nothing for confidentiality by itself and can even weaken it if too much data is placed on-chain.

### 5.2 Assets and threats

Lucas lists assets: credit balances, the keys that issue credits, the booking database, the nodes and the makerspace's reputation. He considers threats in general terms: a lost issuing key could stop credits being granted; a misused key could grant credits without workshops; an exposed database could leak member emails; a failed node could slow bookings. He ranks them by likelihood and impact with the manager. He avoids technical attack detail and focuses on what could happen and what it would cost. The ranked list guides where effort goes first in the coming months.

### 5.3 Layered controls

Lucas learns to layer controls. Preventive controls stop problems, such as requiring two staff to approve credit grants. Detective controls notice them, such as a daily comparison of workshops taught with credits granted. Corrective controls recover, such as tested node backups. He maps each control to an asset and threat. When one layer fails, another should catch the problem. Ms Adebayo notes that small organisations often rely on a single control, such as trusting one person, and that adding a simple detective check is often the cheapest improvement available.

### Worked example

Lucas ranks five assets with the manager and pairs credit issuing with two-person approval, a daily comparison and tested backups.

> **Synthetic case.** The assets, threats and controls are synthetic.

### Errors and limits

Relying on a single control, such as trusting one person, leaves no backup when it fails.

### Exercises

- **EX013 — Accountability meaning.** What does accountability mean here? *Rubric:* 3 = actions like granting credits can be traced to a person;; 2 = traceability;; 1 = speed;; 0 = none.
- **EX014 — Asset ranking.** How are threats ranked? *Rubric:* 3 = by likelihood and impact with the manager;; 2 = likelihood and impact;; 1 = alphabetically;; 0 = none.
- **EX015 — Cheap improvement.** What is often the cheapest improvement? *Rubric:* 3 = adding a simple detective check;; 2 = detective check;; 1 = more servers;; 0 = none.

### Synthesis

Security goals, ranked assets and layered controls form a practical foundation.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) manage users and permissions; (2) run nodes in isolated environments; (3) maintain hosts safely.

### 6.1 Users and permissions

Operating systems control who can do what. Lucas creates a dedicated user for the node software on each server, gives it access only to its data and configuration folders, and removes shell access for that user. The node key file is readable only by that user. Administrators log in with their own accounts and elevate privileges only when needed, so actions are recorded per person. These steps follow the principle of least privilege. If the node software ever misbehaves or is misused, the damage it can do to the rest of the server is limited.

### 6.2 Isolation with virtualization

Virtual machines and containers isolate software. Lucas runs each node in its own container with limited memory and processor, a read-only base image and a mounted data folder. Isolation keeps a fault in one component from affecting others and makes environments reproducible. He also uses virtual machines in the college lab to rehearse upgrades without touching the makerspace's servers. Ms Adebayo warns that isolation is not perfect: containers share the host's kernel, so the host must still be hardened and patched carefully, and container images must come from trusted sources.

### 6.3 Maintaining hosts safely

Lucas sets a monthly maintenance routine: apply operating system updates to one server at a time, check that the node resynchronises, review disk usage and confirm backups. He keeps a maintenance log with dates, changes and results. Because the ledger needs two of three nodes, updating one at a time keeps it running. He tests every update in a lab virtual machine first. Careful, routine maintenance prevents many incidents, and the log helps diagnose problems later, because it shows exactly what changed and when it changed on each server.

### Worked example

Lucas runs each node in a resource-limited container as a dedicated user and updates one server at a time after lab testing.

> **Synthetic case.** The hosts and containers are synthetic.

### Errors and limits

Assuming containers fully isolate software ignores that they share the host's kernel.

### Exercises

- **EX016 — Node user restriction.** What access does the node user lack? *Rubric:* 3 = shell access;; 2 = no shell;; 1 = data folder;; 0 = none.
- **EX017 — Isolation caveat.** Why must hosts still be hardened? *Rubric:* 3 = containers share the host's kernel;; 2 = shared kernel;; 1 = they need not;; 0 = none.
- **EX018 — Rehearsal place.** Where are upgrades rehearsed? *Rubric:* 3 = lab virtual machines;; 2 = college lab;; 1 = production;; 0 = none.

### Synthesis

Least privilege, isolation and routine maintenance keep node hosts dependable.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) distinguish authentication from authorization; (2) manage keys and accounts; (3) design roles for credit issuing.

### 7.1 Authentication and authorization

Authentication confirms identity; authorization decides permissions. Staff log in to the booking system with passwords and a second factor, while members authenticate to the ledger by signing transactions with their wallet keys. The credit contract then checks authorization: only the issuer role can grant credits, and members can only spend their own. Lucas notes that a ledger cannot tell whether the right person holds a key, only whether the right key signed. So protecting keys and staff accounts is where identity security really lives for the makerspace and its credit system.

### 7.2 Keys and accounts

Lucas inventories every account and key: staff logins, administrator accounts on servers, node keys and the issuer key. For each he records the owner, purpose, storage and when it was last reviewed. He finds an old account belonging to a volunteer who left last year and has it disabled. He recommends the issuer key move from a laptop file to a hardware device. Inventories reveal forgotten access, which is a common route to problems. He schedules a review every quarter and adds account removal to the volunteer departure checklist.

### 7.3 Roles for credit issuing

Lucas designs roles with the manager. Workshop leaders can record workshops taught in the booking system. The coordinator approves them. A small issuing service prepares credit grants, and a 2-of-3 multisig of staff signs them on the ledger. An administrator role, behind a timelock, can change roles. Each role has only the powers it needs. The OWASP Smart Contract Top 10 lists access control failures as a leading weakness, so he documents roles clearly and asks the developer to add tests showing that each forbidden action is refused.

### Worked example

Lucas disables a departed volunteer's account, moves the issuer key toward hardware and places credit grants behind a 2-of-3 staff multisig.

> **Synthetic case.** The accounts, keys and roles are synthetic; the OWASP Smart Contract Top 10 is a real source.

### Errors and limits

Forgotten accounts of departed volunteers remain a route to unauthorised access.

### Exercises

- **EX019 — Ledger limitation.** What can the ledger not tell? *Rubric:* 3 = whether the right person holds the key;; 2 = who holds the key;; 1 = the balance;; 0 = none.
- **EX020 — Inventory finding.** What did the inventory reveal? *Rubric:* 3 = an account of a volunteer who left;; 2 = old account;; 1 = vague;; 0 = none.
- **EX021 — Grant signing.** Who signs credit grants on the ledger? *Rubric:* 3 = a 2-of-3 multisig of staff;; 2 = multisig;; 1 = one leader;; 0 = none.

### Synthesis

Inventories and least-privilege roles turn identity theory into protection.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) draw system components and trust boundaries; (2) place controls at boundaries; (3) record design choices.

### 8.1 Components and boundaries

Lucas draws the makerspace system: member wallets, the booking web application, its database, the issuing service, the multisig, the credit contract and three nodes. He marks trust boundaries where data crosses from one owner or trust level to another: from members' devices to the web application, from the database to the issuing service and from the service to the ledger. Each boundary is a place to check inputs and permissions. The drawing becomes a shared picture for staff and developers, and he keeps it updated whenever any component changes.

### 8.2 Controls at boundaries

At the member boundary the web application validates every input and uses secure sessions. At the database boundary the issuing service reads only approved workshops through a read-only account. At the ledger boundary multisig signers see a summary of each grant batch before signing. The contract itself enforces a monthly cap on credits per member. Lucas lists each control beside its boundary. Placing controls at boundaries means problems are stopped close to where they enter, before they can spread through the system and become harder to trace and fix.

### 8.3 Recording design choices

Lucas writes short design notes explaining choices: why a permissioned ledger was chosen, why grants are batched weekly, why the cap is set at a certain level. Each note lists the alternatives considered and the reasons. When a new developer suggests removing the batch summary to save time, the note explains that it was added after a near miss. Design notes preserve reasoning that would otherwise be lost when people change. Ms Adebayo calls them the system's memory, and she asks students to write them throughout the course.

### Worked example

Lucas places input validation, a read-only issuing account, batch summaries and a monthly contract cap at the system's boundaries.

> **Synthetic case.** The architecture and notes are synthetic.

### Errors and limits

Removing a control without knowing why it was added can reopen a risk it addressed.

### Exercises

- **EX022 — Boundary example.** Name one trust boundary Lucas marks. *Rubric:* 3 = database to issuing service;; 2 = service to ledger;; 1 = inside the database;; 0 = none.
- **EX023 — Contract control.** What does the contract enforce? *Rubric:* 3 = a monthly cap on credits per member;; 2 = cap;; 1 = vague;; 0 = none.
- **EX024 — Design note use.** How did a design note help? *Rubric:* 3 = it explained the batch summary followed a near miss;; 2 = preserved reasoning;; 1 = it did not;; 0 = none.

### Synthesis

Boundaries, controls placed at them and recorded reasoning make architecture defensible.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) choose measures that inform decisions; (2) collect evidence reliably; (3) report results clearly.

### 9.1 Choosing measures

Lucas chooses measures with the manager: percentage of credit grants matched to recorded workshops, number of node sync alerts per month, time to restore a node from backup, and number of privileged ledger actions without an approved change ticket. Each has a target. He avoids counting things just because they are easy, such as total transactions, unless they help a decision. A good measure tells someone what to do next, such as investigating an unmatched grant or fixing a slow restore, and can be explained in one plain sentence to staff and members.

### 9.2 Collecting evidence reliably

Lucas collects evidence directly from systems: ledger data from a node, booking data from the database's read-only account and restore times from timed drills. He records the source, time and method for each, and stores a SHA-256 hash of each export so later changes can be detected. He writes the steps down so another technologist can repeat them. Reliable evidence is repeatable and traceable. Evidence that relies on memory or screenshots is easily disputed, and decisions made on it may be wrong without anyone being able to tell.

### 9.3 Reporting clearly

Lucas's first monthly report shows 412 of 415 credit grants matched to workshops, with the three unmatched explained as late records later confirmed. Restore time was 38 minutes against a 60-minute target. One privileged action lacked a ticket and is under review. He shows counts, not just percentages, and explains each exception in plain words. The manager appreciates the clarity. Clear reports build trust and make problems visible early. Ms Adebayo reminds him that a report which hides problems is worse than no report, because it gives false confidence.

### Worked example

Lucas reports 412 of 415 grants matched, a 38-minute restore against 60, and one privileged action without a ticket under review.

> **Synthetic case.** The measures and results are synthetic.

### Errors and limits

Counting easy things, like total transactions, rarely informs any decision.

### Exercises

- **EX025 — Measure list.** Name one of Lucas's measures. *Rubric:* 3 = time to restore a node;; 2 = grants matched;; 1 = total transactions;; 0 = none.
- **EX026 — Export integrity.** How are export changes made detectable? *Rubric:* 3 = storing a SHA-256 hash of each export;; 2 = hashing;; 1 = screenshots;; 0 = none.
- **EX027 — Restore result.** What restore time was measured? *Rubric:* 3 = 38 minutes against 60;; 2 = 38 minutes;; 1 = 2 hours;; 0 = none.

### Synthesis

Decision-focused measures and reliable, clear reporting make evidence useful.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Web3, blockchain and cryptoasset security: orientation

### Learning outcomes

You will (1) outline the field's scope; (2) explain blocks, consensus and contracts; (3) locate the makerspace's risks.

### 10.1 Scope of the field

Web3, blockchain and cryptoasset security covers ledgers, smart contracts, keys and wallets, the services connecting them to the outside world and the people operating them. Lucas reads NIST IR 8202 for an overview of components and permission models and the OWASP Smart Contract Top 10 for common contract weaknesses. He notes that technologists work mostly on nodes, services, keys and monitoring rather than writing contracts, but must understand contracts well enough to operate them safely, read their events and recognise when something looks wrong in the data.

### 10.2 Blocks, consensus and contracts

A blockchain is a sequence of blocks, each containing transactions and the hash of the previous block, as described in Nakamoto's paper. Consensus lets nodes agree on the sequence; the makerspace's ledger uses voting among its three known nodes. Smart contracts, described in Buterin's whitepaper and Wood's yellow paper, are programs stored on the ledger and executed by every node. The credit contract keeps balances, enforces the cap and emits events. Lucas learns to read those events, because they are his main window into what the contract is doing.

### 10.3 Locating the makerspace's risks

Lucas places the makerspace's risks on his diagram. Consensus risk is low because the three nodes are known and controlled. Contract risk exists but the contract is small and was reviewed. Key risk is significant, since the issuer multisig controls credit creation. Service risk is significant, because the issuing service decides what is granted. Operational risk, from missed updates or poor monitoring, is where his work matters most. Ms Adebayo agrees and suggests his coursework focus on keys, services and operations, which matches where real losses most often arise in practice.

### Worked example

Lucas rates consensus risk low, contract risk moderate and key, service and operational risks significant, focusing his work on the last three.

> **Synthetic case.** The makerspace's risk picture is synthetic; NIST IR 8202, OWASP SC Top 10, Nakamoto, Buterin and Wood are real sources.

### Errors and limits

Focusing on consensus in a small permissioned ledger neglects the keys and services where risk concentrates.

### Exercises

- **EX028 — Technologist focus.** What do technologists mostly work on? *Rubric:* 3 = nodes, services, keys and monitoring;; 2 = operations;; 1 = writing contracts;; 0 = none.
- **EX029 — Block link.** What links each block to the previous one? *Rubric:* 3 = the previous block's hash;; 2 = hash;; 1 = a timestamp;; 0 = none.
- **EX030 — Lowest risk.** Which risk does Lucas rate lowest? *Rubric:* 3 = consensus;; 2 = consensus risk;; 1 = keys;; 0 = none.

### Synthesis

Understanding the field's parts shows a technologist where risk actually lies.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Web3, blockchain and cryptoasset security: assets and context

### Learning outcomes

You will (1) inventory ledger-related assets; (2) understand stakeholders; (3) set protection priorities.

### 11.1 Inventory of ledger assets

Lucas builds an inventory of ledger-related assets: the credit contract and its deployed address, the issuer multisig and its three signer keys, the administrator role and its timelock, three nodes with their keys and configurations, the issuing service, the booking database and backups of each. For each he records the owner, location, value to the makerspace and current protection. An inventory is the foundation of security work, because assets that are not known cannot be protected, monitored or recovered when something goes wrong with them.

### 11.2 Stakeholders

Stakeholders include members, workshop leaders, staff signers, the manager, the board, the developer who wrote the contract and the rack provider. Each cares about different things: members want fair credits and working bookings, signers want a manageable workload, the board wants low risk and cost. Lucas interviews three stakeholders briefly to understand their concerns. He learns that signers worry about signing something wrong, which suggests better batch summaries. Understanding stakeholders helps technologists design controls that people accept and actually use in their daily work.

### 11.3 Protection priorities

With the inventory and stakeholder views, Lucas sets priorities with the manager. Highest are the signer keys and the issuing service, because together they control credit creation. Next are node availability and backups, because bookings depend on them. Then the booking database's personal data. Priorities guide limited time and money: the makerspace cannot do everything at once. He records the priorities and the reasoning, and plans to revisit them after any significant change, such as adding a new type of credit or connecting to another organisation's ledger.

### Worked example

Lucas inventories eleven asset types and, after stakeholder interviews, prioritises signer keys and the issuing service, then node availability.

> **Synthetic case.** The assets and stakeholders are synthetic.

### Errors and limits

Protecting assets in the order they come to mind wastes effort on low-impact items.

### Exercises

- **EX031 — Inventory field.** Name one field recorded for each asset. *Rubric:* 3 = current protection;; 2 = owner;; 1 = colour;; 0 = none.
- **EX032 — Signer concern.** What do signers worry about? *Rubric:* 3 = signing something wrong;; 2 = mistakes;; 1 = vague;; 0 = none.
- **EX033 — Top priority.** What are the top protection priorities? *Rubric:* 3 = signer keys and the issuing service;; 2 = keys and service;; 1 = the website;; 0 = none.

### Synthesis

Inventory, stakeholder understanding and agreed priorities direct limited security effort.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Web3, blockchain and cryptoasset security: data flows

### Learning outcomes

You will (1) trace data from source to ledger; (2) find points where data can go wrong; (3) add checks along the flow.

### 12.1 Tracing the flow

Lucas traces how teaching a workshop becomes credits. The leader records the workshop in the booking system; the coordinator approves it; each week the issuing service reads approved workshops, calculates credits and builds a batch; two staff sign the batch through the multisig; the contract grants credits and emits events; the booking application shows the new balance. He writes each step, its data, who controls it and how it could fail. The trace reveals that the calculation step has no independent check, which becomes his first improvement project for the term.

### 12.2 Where data can go wrong

Data can go wrong at each step: a leader records the wrong date, a coordinator approves a duplicate, the service miscalculates, a signer approves without reading, or the contract rejects a valid grant. Lucas also considers timing: if the service runs while the database is mid-update, it may read partial data. He lists each failure point with an example. He does not consider how someone might deliberately misuse the system in detail; he focuses on errors and controls, which also protect against misuse in most cases without needing attack knowledge.

### 12.3 Adding checks

Lucas adds checks along the flow. The issuing service now compares its batch total with an independent calculation from the database and refuses to proceed if they differ. The batch summary shows each member's grant and flags any workshop already credited. After the contract grants credits, a script compares events with the batch. Each check is small and independent. Together they make it unlikely that an error passes unnoticed. He tests each check with seeded errors in synthetic data and records the results in the design notes for the developer.

### Worked example

Lucas adds an independent batch total check, duplicate flags in the summary and a post-grant event comparison, each tested with seeded errors.

> **Synthetic case.** The data flow and checks are synthetic.

### Errors and limits

A calculation step with no independent check can pass errors straight to signing.

### Exercises

- **EX034 — Unchecked step.** Which step had no independent check? *Rubric:* 3 = the credit calculation;; 2 = calculation;; 1 = signing;; 0 = none.
- **EX035 — Timing issue.** What timing problem could occur? *Rubric:* 3 = reading partial data mid-update;; 2 = partial reads;; 1 = vague;; 0 = none.
- **EX036 — Post-grant check.** What happens after credits are granted? *Rubric:* 3 = a script compares events with the batch;; 2 = event comparison;; 1 = vague;; 0 = none.

### Synthesis

Tracing flows and adding independent checks keep data correct from source to ledger.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Web3, blockchain and cryptoasset security: risk scenarios

### Learning outcomes

You will (1) write realistic risk scenarios; (2) estimate likelihood and impact; (3) choose treatments.

### 13.1 Writing scenarios

A risk scenario describes a plausible event, its cause and its consequences. Lucas writes five for the makerspace: a signer loses their hardware device; the issuing service grants a week's credits twice; a node's disk fills and it stops; a member's phone with their wallet is stolen; and the rack provider has a day-long outage. Each scenario is written in plain language without technical attack detail. Scenarios make risks concrete for staff and the board, who can then discuss them sensibly and agree on what matters most.

### 13.2 Likelihood and impact

For each scenario Lucas estimates likelihood and impact on simple scales agreed with the manager. A full disk is likely but low impact if monitored. A double grant is unlikely after the new checks but would be moderately harmful. A day-long provider outage is unlikely but would stop all bookings. He explains the reasoning for each estimate and notes that they are judgements, not measurements. Estimating together with staff improves the estimates and builds shared understanding of why some risks receive more attention and budget than others.

### 13.3 Choosing treatments

Treatments can reduce, transfer, avoid or accept a risk. Lucas proposes: for the lost device, a tested replacement procedure; for double grants, the checks already added; for full disks, alerts at 80 percent; for stolen phones, member guidance and a process to move credits to a new address after identity checks; for the provider outage, accepting the risk with a paper booking fallback. The manager approves the plan. Recording accepted risks is important, because acceptance is a deliberate decision with an owner, not an oversight that someone forgot to address.

### Worked example

Lucas writes five scenarios, rates them with staff and chooses treatments including disk alerts at 80 percent and an accepted provider-outage risk with a paper fallback.

> **Synthetic case.** The scenarios and treatments are synthetic.

### Errors and limits

Leaving a risk untreated without recording acceptance turns a decision into an oversight.

### Exercises

- **EX037 — Scenario example.** Name one of Lucas's scenarios. *Rubric:* 3 = a signer loses their hardware device;; 2 = node disk fills;; 1 = meteor strike;; 0 = none.
- **EX038 — Disk treatment.** How is the full-disk risk treated? *Rubric:* 3 = alerts at 80 percent;; 2 = alerts;; 1 = accept;; 0 = none.
- **EX039 — Accepted risk.** Which risk is accepted, with what fallback? *Rubric:* 3 = provider outage, with paper booking;; 2 = paper fallback;; 1 = double grants;; 0 = none.

### Synthesis

Concrete scenarios, shared estimates and recorded treatments make risk management practical.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Web3, blockchain and cryptoasset security: methods I

### Learning outcomes

You will (1) use checklists to review ledger operations; (2) apply standards as criteria; (3) record findings consistently.

### 14.1 Operational checklists

Lucas builds a checklist for reviewing ledger operations. Questions include: are all nodes on the approved client version, is each node's programming interface restricted, are signer keys on hardware devices, are backups recent and tested, are privileged actions matched to approved changes, and are monitoring alerts reviewed. Each question needs evidence, not just a yes. He runs the checklist monthly. Checklists help technologists cover the same ground every time, reducing the chance that an important item is forgotten during a busy week at the makerspace.

### 14.2 Standards as criteria

For contract-related items Lucas refers to the EEA EthTrust Security Levels specification and the SWC registry, and for development practices to the ConsenSys best practices. He does not review contract code deeply himself, but he checks that the developer's documentation shows the contract was reviewed against these standards and that the compiler version is fixed. Using recognised standards makes findings credible and easy to discuss. He notes that EthTrust itself states that meeting its requirements does not guarantee the absence of weaknesses, and he says so in his reports.

### 14.3 Recording findings

Each finding gets an identifier, description, evidence, severity and recommended action. In his first monthly review Lucas records three findings: one node runs an older client version, monitoring alerts were not reviewed for a week during holidays, and a backup restore has not been tested for two months. All are rated low or medium. He agrees owners and dates with the manager. Consistent records let progress be tracked over months and make it easy to show the board how the makerspace's security has improved over time.

### Worked example

Lucas's first monthly checklist review records an old client version, a week of unreviewed alerts and an untested backup, each with an owner and date.

> **Synthetic case.** The checklist review is synthetic; EEA EthTrust, the SWC registry and ConsenSys best practices are real sources.

### Errors and limits

Answering checklist questions without evidence turns review into guesswork.

### Exercises

- **EX040 — Checklist question.** Name one checklist question. *Rubric:* 3 = are signer keys on hardware devices;; 2 = are backups tested;; 1 = is the office tidy;; 0 = none.
- **EX041 — Standard caution.** What caution does EthTrust state? *Rubric:* 3 = meeting requirements does not guarantee no weaknesses;; 2 = no guarantee;; 1 = full guarantee;; 0 = none.
- **EX042 — Review finding.** Name one finding from the first review. *Rubric:* 3 = an older client version on one node;; 2 = untested backup;; 1 = stolen key;; 0 = none.

### Synthesis

Evidence-based checklists anchored in standards make reviews consistent and credible.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Web3, blockchain and cryptoasset security: guided lab

### Learning outcomes

You will (1) check node synchronisation from height samples; (2) interpret lag; (3) respond with a runbook step.

### 15.1 Why synchronisation matters

Each node should hold the same chain. If one falls behind, applications reading from it see old balances, and if two fall behind, the ledger may stop producing blocks. Lucas collects block heights from the three nodes every minute and checks whether any node is more than two blocks behind the highest. This lab uses five synthetic samples. It is read-only and uses only Python's standard library. Monitoring synchronisation is one of the most basic and valuable checks a technologist can run, and it often reveals problems before members notice anything.

### Lab — Node synchronisation check

```python
"""Flag ledger nodes that lag behind the highest block height (synthetic, read-only)."""
# minute: heights reported by node-a, node-b, node-c
SAMPLES = [
    (0, 1200, 1200, 1199), (1, 1206, 1206, 1205), (2, 1212, 1211, 1207),
    (3, 1218, 1218, 1209), (4, 1224, 1223, 1210),
]
NAMES = ("node-a", "node-b", "node-c")
MAX_LAG = 2

def main():
    for minute, *heights in SAMPLES:
        top = max(heights)
        for name, h in zip(NAMES, heights):
            if top - h > MAX_LAG:
                print(f"minute {minute}: {name} lags {top - h} blocks")
    print(f"samples {len(SAMPLES)}; threshold {MAX_LAG} blocks")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_sync.py`. Verified output:

```text
minute 2: node-c lags 5 blocks
minute 3: node-c lags 9 blocks
minute 4: node-c lags 14 blocks
samples 5; threshold 2 blocks
```

### 15.2 Interpreting the lag

The lab reports that node-c lags 5 blocks at minute 2, 9 at minute 3 and 14 at minute 4, while node-a and node-b stay within one block of each other. The growing lag suggests node-c has stopped keeping up, rather than suffering a brief delay. Lucas considers likely causes: a full disk, an overloaded processor, lost peer connections or a clock problem. He checks disk use first, because the earlier chapter showed it is the most common cause. In this synthetic case, node-c's disk is at 99 percent, which explains its inability to store new blocks.

### 15.3 Responding with a runbook

Lucas follows the runbook step for a lagging node: confirm the other two nodes are healthy, point the booking application at a healthy node, free disk space by moving old logs as the runbook describes, restart the node and watch it catch up. Node-c recovers within twenty minutes. He records the event and finds that the 80 percent disk alert had never been enabled on node-c, so he enables it. Ms Adebayo notes that runbooks turn diagnosis into consistent action, so any trained volunteer can respond safely, even late in the evening when no experienced staff member is available.

### Worked example

The lab flags node-c lagging 5, 9 and then 14 blocks; a full disk is found, the runbook restores it in twenty minutes and the missing 80 percent disk alert is enabled.

> **Synthetic case.** The heights, disk usage and recovery are synthetic.

### Errors and limits

Treating a growing lag as a brief delay lets a failing node drift further behind.

### Exercises

- **EX043 — Lag threshold.** What lag threshold does the lab use? *Rubric:* 3 = two blocks;; 2 = 2 blocks;; 1 = ten blocks;; 0 = none.
- **EX044 — Lagging node.** Which node lags, and by how much at minute 4? *Rubric:* 3 = node-c, 14 blocks;; 2 = node-c;; 1 = node-a;; 0 = none.
- **EX045 — Root cause found.** What caused node-c's lag? *Rubric:* 3 = its disk was at 99 percent;; 2 = full disk;; 1 = network;; 0 = none.

### Synthesis

Simple height monitoring and a runbook catch and fix lagging nodes quickly.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Web3, blockchain and cryptoasset security: methods II

### Learning outcomes

You will (1) use automated tools carefully; (2) combine tools with manual checks; (3) interpret output with context.

### 16.1 Automated tools

Lucas learns that automated tools help with routine checks: configuration scanners compare servers with baselines, log tools search for patterns, and contract analysers flag code patterns linked to known weaknesses. Durieux and colleagues' 2020 study of contract analysis tools found they often disagreed and each missed many issues. Lucas concludes that tools are aids, not judges. He uses them to cover ground quickly, then checks important results by hand. Ms Adebayo asks the class to record each tool's version and settings, since results depend on both and must be reproducible later.

### 16.2 Combining tools and manual checks

When a configuration scanner flags a node for an open port, Lucas checks manually and confirms the port is the peer port, which is expected and restricted by the firewall allow-list. He records it as a false positive with the reason. When it flags a missing time-synchronisation service, the manual check confirms it, and he fixes it. Combining tools with manual checks avoids two errors: ignoring real problems because tools are noisy, and acting on false alarms that waste time and erode trust in the tools themselves.

### 16.3 Interpreting output with context

Context changes meaning. An alert about a large credit transfer is concerning on a weekday afternoon but expected on the monthly day when the makerspace refunds unused workshop deposits. Lucas adds context notes to his monitoring guide, describing normal patterns by day and season. Perez and Livshits' 2021 study found that many weaknesses reported by tools in deployed contracts were never exploited, a reminder that output must be weighed in context. Interpreting with context helps technologists respond proportionately rather than treating every alert as an emergency.

### Worked example

Lucas confirms a flagged peer port is an expected false positive, fixes a confirmed missing time service and documents normal monthly refund patterns.

> **Synthetic case.** The tool results and patterns are synthetic; Durieux et al. (2020) and Perez and Livshits (2021) are real sources.

### Errors and limits

Acting on every tool alert without manual confirmation wastes effort and erodes trust in tools.

### Exercises

- **EX046 — Tool study.** What did Durieux et al. find? *Rubric:* 3 = tools often disagreed and each missed many issues;; 2 = disagreement;; 1 = perfect tools;; 0 = none.
- **EX047 — False positive.** Which flag was a false positive? *Rubric:* 3 = the open peer port;; 2 = peer port;; 1 = missing time service;; 0 = none.
- **EX048 — Context pattern.** When is a large transfer expected? *Rubric:* 3 = on the monthly deposit refund day;; 2 = refund day;; 1 = never;; 0 = none.

### Synthesis

Tools speed up checks, manual confirmation keeps them honest and context gives meaning.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Web3, blockchain and cryptoasset security: tooling

### Learning outcomes

You will (1) assemble a safe toolkit; (2) manage tool versions; (3) keep tooling read-only where possible.

### 17.1 Assembling a toolkit

Lucas assembles a toolkit: the ledger client's command-line interface for reading node status, a small set of Python scripts for checks, a log viewer, a configuration scanner and a hardware wallet utility for signers. He documents each tool's purpose, source and owner. He chooses widely used, maintained tools and avoids installing unknown utilities from unverified sources. A toolkit is part of the attack surface: a compromised tool on a signer's computer could misrepresent what is being signed, so tool choice is itself a security decision.

### 17.2 Managing versions

Each tool has a pinned version recorded in a simple list. Updates are tested in the college lab before use at the makerspace. Lucas checks release notes for security fixes and breaking changes. He learns that the SWC registry lists weaknesses linked to outdated compilers, and the same principle applies to operational tools: old versions accumulate known problems. He schedules a quarterly tooling review. Version management sounds dull, but it prevents surprises, such as a script that suddenly fails because a tool changed its output format overnight.

### 17.3 Read-only by default

Most of Lucas's tools only read data. His scripts use the node's read interface and the database's read-only account. The only tools that can change the ledger are the multisig signing tools, used by staff on dedicated devices. Keeping monitoring and reporting tools read-only means a bug or misuse cannot alter balances or roles. He labels every script with whether it reads or writes. Ms Adebayo calls this one of the most effective habits in operations: separate the many tools that look from the few tools that change.

### Worked example

Lucas's toolkit pins versions, is reviewed quarterly and keeps all monitoring scripts read-only, with writes limited to signing tools on dedicated devices.

> **Synthetic case.** The toolkit is synthetic; the SWC registry is a real source.

### Errors and limits

Running monitoring scripts with write access lets a bug alter balances or roles.

### Exercises

- **EX049 — Tool risk.** Why is tool choice a security decision? *Rubric:* 3 = a compromised tool could misrepresent what is signed;; 2 = tool compromise;; 1 = cost;; 0 = none.
- **EX050 — Tooling review.** How often are tools reviewed? *Rubric:* 3 = quarterly;; 2 = every quarter;; 1 = never;; 0 = none.
- **EX051 — Writing tools.** Which tools can change the ledger? *Rubric:* 3 = the multisig signing tools on dedicated devices;; 2 = signing tools;; 1 = all scripts;; 0 = none.

### Synthesis

A documented, versioned and mostly read-only toolkit reduces operational risk.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Web3, blockchain and cryptoasset security: controls

### Learning outcomes

You will (1) configure preventive controls; (2) verify they work; (3) document control ownership.

### 18.1 Configuring preventive controls

Lucas helps configure preventive controls. On the ledger: the 2-of-3 multisig for grants, the monthly per-member cap, and a 48-hour timelock on administrator actions. On nodes: firewall allow-lists, restricted programming interfaces and dedicated service users. In the booking system: two-step approval of workshops and multi-factor login for staff. Each setting is recorded with its intended value. Preventive controls stop many problems before they start, and documenting intended values makes it possible to detect when a setting drifts away from what was agreed.

### 18.2 Verifying controls

A control is only as good as evidence that it works. Lucas tests each on the test ledger: a single signer cannot complete a grant; a grant above the cap is refused; an administrator action waits 48 hours; an outside address cannot connect to a node; a staff login without the second factor fails. He records each test with date and result. One test fails: the cap on the test ledger is set higher than intended. The developer corrects it, and Lucas retests successfully. Testing turns assumed protection into demonstrated protection.

### 18.3 Control ownership

Every control needs an owner who ensures it keeps working. Lucas lists owners: the manager owns the multisig signer list, the developer owns contract settings, Lucas owns node configurations and the coordinator owns workshop approvals. Owners review their controls quarterly and after changes. Without owners, controls decay quietly as people come and go. He adds the owner list to the handover file. The OWASP Smart Contract Top 10 highlights access control failures, many of which arise when nobody is clearly responsible for keeping role settings correct.

### Worked example

Lucas tests five controls, finds the test-ledger cap set too high, has it corrected and retested, and assigns an owner to each control.

> **Synthetic case.** The controls and tests are synthetic; the OWASP Smart Contract Top 10 is a real source.

### Errors and limits

Controls without owners decay quietly as people come and go.

### Exercises

- **EX052 — Timelock length.** How long is the administrator timelock? *Rubric:* 3 = 48 hours;; 2 = 48h;; 1 = 1 hour;; 0 = none.
- **EX053 — Failed control test.** Which control test failed? *Rubric:* 3 = the cap was set higher than intended;; 2 = cap;; 1 = multisig;; 0 = none.
- **EX054 — Signer list owner.** Who owns the multisig signer list? *Rubric:* 3 = the manager;; 2 = manager, hedged with another option;; 1 = Lucas;; 0 = none.

### Synthesis

Configured, tested and owned controls provide lasting protection.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Web3, blockchain and cryptoasset security: monitoring

### Learning outcomes

You will (1) monitor privileged ledger events; (2) match events to approved changes; (3) escalate unmatched events.

### 19.1 What to monitor

Privileged events show changes to the system's rules: roles granted or revoked, pauses, cap changes and contract upgrades. Each should correspond to an approved change ticket or incident record. Lucas writes a read-only script that reads these events and checks each against a list of approved references. Unmatched events are not automatically wrong, but they must be explained. Monitoring privileged events is one of the highest-value checks for a token system, because these actions can change who controls credits or how the contract behaves for everyone.

### Lab — Privileged event matching

```python
"""Match privileged ledger events to approved change tickets (synthetic, read-only)."""
EVENTS = [
    ("blk 5021", "RoleGranted", "minter", "CHG-104"),
    ("blk 5390", "Paused", "-", "INC-007"),
    ("blk 5391", "Unpaused", "-", "INC-007"),
    ("blk 6012", "RoleGranted", "admin", None),
    ("blk 6450", "CapChanged", "200->250", "CHG-111"),
    ("blk 6702", "Upgraded", "v1.3", "CHG-115"),
]
APPROVED = {"CHG-104", "INC-007", "CHG-111"}

def main():
    unmatched = [e for e in EVENTS if e[3] not in APPROVED]
    print(f"privileged events {len(EVENTS)}; unmatched {len(unmatched)}")
    for blk, kind, detail, ref in unmatched:
        print(f"  {blk} {kind} {detail} ref={ref}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_privlog.py`. Verified output:

```text
privileged events 6; unmatched 2
  blk 6012 RoleGranted admin ref=None
  blk 6702 Upgraded v1.3 ref=CHG-115
```

### 19.2 Interpreting the result

The lab reads six privileged events and finds two unmatched. At block 6012 an admin role was granted with no ticket reference at all. At block 6702 the contract was upgraded to version 1.3 citing ticket CHG-115, which is not in the approved list. The other four events match approved tickets or an incident. Lucas does not assume misuse. He checks the change system: CHG-115 was approved late in the day and the export he used was taken before approval. The admin grant, however, has no ticket at all and needs urgent explanation.

### 19.3 Escalating unmatched events

Following the runbook, Lucas escalates the unmatched admin grant to the manager within the hour, with the block number and evidence. The manager confirms the developer granted a temporary admin role during testing on the wrong network and forgot to remove it. The role is revoked through the timelocked process, a ticket is raised retrospectively and the developer's deployment checklist gains a network confirmation step. For CHG-115, Lucas changes the export to run after the daily approval window closes, removing the timing gap that caused the false alarm.

### Worked example

The lab finds two unmatched events of six; CHG-115 is a timing gap in the export, while the ticketless admin grant is escalated and revoked.

> **Synthetic case.** The events, tickets and response are synthetic.

### Errors and limits

Ignoring an unmatched privileged event can leave unexpected control in place.

### Exercises

- **EX055 — Event count.** How many privileged events does the lab read? *Rubric:* 3 = six;; 2 = 6;; 1 = two;; 0 = none.
- **EX056 — Ticketless event.** Which event had no ticket at all? *Rubric:* 3 = admin role grant at block 6012;; 2 = admin grant;; 1 = upgrade;; 0 = none.
- **EX057 — CHG-115 explanation.** Why was CHG-115 unmatched? *Rubric:* 3 = the export was taken before approval;; 2 = timing;; 1 = fraud;; 0 = none.

### Synthesis

Matching privileged events to approvals and escalating gaps keeps control visible.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Web3, blockchain and cryptoasset security: troubleshooting

### Learning outcomes

You will (1) diagnose faults methodically; (2) separate symptoms from causes; (3) record fixes for reuse.

### 20.1 Methodical diagnosis

When members report that bookings are slow to confirm, Lucas follows a method: define the symptom precisely, gather data, form hypotheses, test them one at a time and confirm the fix. He measures that confirmations take about forty seconds instead of the usual twelve. He checks node health, block production times, the booking application's logs and the network between them. A methodical approach avoids guessing and changing several things at once, which can hide the real cause or introduce new problems that are even harder to trace afterwards.

### 20.2 Symptoms and causes

Block production is normal, so the ledger is not slow. The booking application logs show it waits for a node response for thirty seconds before retrying another node. The node it prefers, node-b, has a high response time because its programming interface is overloaded by a reporting script running every minute. The symptom is slow bookings; the cause is a reporting script running too often against the same node the application uses. Separating symptom from cause leads to the right fix rather than adding more servers or replacing software unnecessarily.

### 20.3 Recording fixes

Lucas moves the reporting script to node-a and reduces its frequency to every ten minutes. Confirmations return to about twelve seconds. He records the symptom, data gathered, hypotheses, tests, cause and fix in a troubleshooting log, with a short summary at the top for quick reading. Next time a similar symptom appears, anyone can check the log first. Ms Adebayo notes that recorded fixes are an organisation's accumulated experience; without them, the same problems are rediscovered painfully by every new volunteer who joins the team.

### Worked example

Slow confirmations of about forty seconds are traced to an overloaded node-b interface, fixed by moving and slowing a reporting script, restoring twelve seconds.

> **Synthetic case.** The fault and fix are synthetic.

### Errors and limits

Changing several things at once can hide the real cause of a fault.

### Exercises

- **EX058 — Measured delay.** How slow were confirmations? *Rubric:* 3 = about forty seconds instead of twelve;; 2 = forty seconds;; 1 = two seconds;; 0 = none.
- **EX059 — Root cause.** What caused the slow bookings? *Rubric:* 3 = a reporting script overloading node-b's interface;; 2 = overloaded interface;; 1 = slow blocks;; 0 = none.
- **EX060 — Fix applied.** What fix was applied? *Rubric:* 3 = moved the script to node-a every ten minutes;; 2 = move and slow script;; 1 = new servers;; 0 = none.

### Synthesis

Methodical diagnosis separates symptoms from causes and recorded fixes speed future work.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Web3, blockchain and cryptoasset security: service integration

### Learning outcomes

You will (1) integrate the ledger with business services; (2) handle failures between services; (3) protect service credentials.

### 21.1 Integrating services

The booking application, the issuing service, an email notification service and the makerspace's accounting software all interact with the ledger. Lucas documents each integration: what it reads or writes, which node it uses, which credentials it holds and what happens if it fails. He finds that the accounting export reads balances directly from the ledger each night, while the booking system uses its own cached copy. If they disagree, staff may be confused. He proposes a single nightly snapshot used by both, which simplifies reconciliation and reduces the number of reads against nodes.

### 21.2 Handling failures between services

Services fail independently. If a node is unavailable, the booking application should switch to another; if the issuing service fails mid-batch, it must not grant credits twice when restarted; if the email service is down, bookings should still proceed and notices queue. Lucas reviews each service's behaviour on failure using the test ledger and finds that the issuing service lacks a record of completed batches. The developer adds one, so a restart resumes safely. Designing for failure between services prevents small outages from causing incorrect credits or lost bookings.

### 21.3 Protecting credentials

Each integration uses credentials: database passwords, node access tokens and email service keys. Lucas moves them from configuration files into the server's protected secret store, gives each service its own credential, and sets rotation dates. No service shares credentials with another, so a leak affects only one. He also confirms that the issuing service cannot sign grants itself; it only prepares batches for human signers. Separating preparation from signing keeps the most powerful action, creating credits, under human control even if a service is compromised.

### Worked example

Lucas proposes a shared nightly snapshot, gets a completed-batch record added to the issuing service and moves credentials into a protected store, one per service.

> **Synthetic case.** The integrations and credentials are synthetic.

### Errors and limits

Sharing one credential across services lets a single leak affect all of them.

### Exercises

- **EX061 — Snapshot proposal.** What does Lucas propose for balances? *Rubric:* 3 = a single nightly snapshot used by booking and accounting;; 2 = shared snapshot;; 1 = more reads;; 0 = none.
- **EX062 — Restart safety.** What did the issuing service lack? *Rubric:* 3 = a record of completed batches;; 2 = batch record;; 1 = a logo;; 0 = none.
- **EX063 — Signing separation.** Can the issuing service sign grants? *Rubric:* 3 = no, it only prepares batches for human signers;; 2 = no;; 1 = yes;; 0 = none.

### Synthesis

Documented integrations, failure-aware design and separate credentials make services safe together.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Web3, blockchain and cryptoasset security: automation

### Learning outcomes

You will (1) automate routine checks safely; (2) detect configuration drift; (3) keep humans in decisions.

### 22.1 Automating routine checks

Lucas automates the checks he has been running by hand: node synchronisation, privileged event matching, grant reconciliation and configuration comparison. Each runs on a schedule, writes results to a dated log and sends a summary email each morning. Automation makes checks consistent and frees time for investigation. He keeps every automated check read-only and reviews the code with a classmate before deploying it. Ms Adebayo warns that automation can hide problems if no one reads the output, so each summary names a person responsible for reading it that day.

### Lab — Configuration drift check

```python
"""Compare node configurations with an approved baseline (synthetic, read-only)."""
BASELINE = {"client": "2.4.1", "rpc_public": False, "peers": "allowlist", "log_days": 90, "ntp": True}
NODES = {
    "node-a": {"client": "2.4.1", "rpc_public": False, "peers": "allowlist", "log_days": 90, "ntp": True},
    "node-b": {"client": "2.4.0", "rpc_public": False, "peers": "allowlist", "log_days": 90, "ntp": True},
    "node-c": {"client": "2.4.1", "rpc_public": True, "peers": "allowlist", "log_days": 30, "ntp": True},
}

def main():
    total = 0
    for node, cfg in NODES.items():
        diffs = [f"{k}={cfg[k]!r} (baseline {v!r})" for k, v in BASELINE.items() if cfg.get(k) != v]
        total += len(diffs)
        print(f"{node}: {'ok' if not diffs else '; '.join(diffs)}")
    print(f"settings checked {len(BASELINE) * len(NODES)}; drift {total}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_drift.py`. Verified output:

```text
node-a: ok
node-b: client='2.4.0' (baseline '2.4.1')
node-c: rpc_public=True (baseline False); log_days=30 (baseline 90)
settings checked 15; drift 3
```

### 22.2 Reading drift and keeping humans in charge

The drift lab compares five settings on three nodes, fifteen in total, and finds three differences: node-b runs client 2.4.0 instead of 2.4.1, and node-c has a public programming interface and keeps logs for only 30 days instead of 90. Node-a matches. Lucas treats the public interface as urgent and the others as routine. He does not let the script change settings automatically; a person reviews each difference and applies fixes through the change process. Automation detects; people decide and act, especially when changes affect live nodes.

### 22.3 Follow-up and lessons

Investigation shows node-c's interface became public after a provider maintenance reset its firewall, and its log setting reverted at the same time. Node-b had missed the last update window. All three are fixed through tickets and the drift check rerun shows no differences. Lucas adds the drift check to run after every provider maintenance notice. He notes that drift is normal in real systems, because updates, resets and manual fixes all change settings, and that only regular comparison with a baseline keeps it under control.

### Worked example

The drift lab finds 3 differences in 15 settings: node-b's client version, and node-c's public interface and 30-day logs, traced to a provider reset.

> **Synthetic case.** The node configurations and investigation are synthetic.

### Errors and limits

Letting automation change live settings without review can turn a detection into an outage.

### Exercises

- **EX064 — Settings compared.** How many settings does the drift lab compare in total? *Rubric:* 3 = fifteen;; 2 = 15;; 1 = five;; 0 = none.
- **EX065 — Urgent drift.** Which drift is treated as urgent? *Rubric:* 3 = node-c's public programming interface;; 2 = public interface;; 1 = log days;; 0 = none.
- **EX066 — Drift cause.** What caused node-c's drift? *Rubric:* 3 = a provider maintenance reset;; 2 = provider reset;; 1 = an attacker;; 0 = none.

### Synthesis

Automated drift detection with human decisions keeps node configurations aligned.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Web3, blockchain and cryptoasset security: evaluation

### Learning outcomes

You will (1) evaluate controls and monitoring against goals; (2) use seeded tests; (3) report strengths and gaps.

### 23.1 Setting evaluation goals

After a year Lucas evaluates the makerspace's ledger controls and monitoring. Goals were agreed earlier: every credit grant matched to a workshop, every privileged event matched to an approval, node lag detected within five minutes, and restores within one hour. He collects evidence from logs, drills and reports for each goal. Evaluating against pre-agreed goals keeps the evaluation honest, because it cannot be adjusted to fit results after the fact, and it gives the board a clear picture of whether the investment in security is paying off.

### 23.2 Seeded tests

To test detection, Lucas seeds synthetic problems into the test environment: an unmatched grant, a privileged event without a ticket, a node stopped to create lag and a configuration change. The monitoring detects all four, with node lag found in three minutes. He also seeds a subtle case: a grant matched to a workshop recorded for the wrong member. Monitoring misses it, because matching checks only workshop identifiers. Seeded tests show what monitoring really catches, including gaps that normal operation would never reveal because the problem had simply not happened yet.

### 23.3 Reporting strengths and gaps

Lucas reports that all four main goals are met and describes the gap: grants matched to the wrong member pass unnoticed. He recommends extending matching to check member identity as well as workshop, and adding a monthly sample review by the coordinator. He presents strengths and gaps together with evidence. The board approves the recommendations. Ms Adebayo notes that evaluations which only confirm success are of limited use; finding a gap is the most valuable outcome, because it shows exactly where to improve next.

### Worked example

Monitoring detects all four seeded problems, node lag within three minutes, but misses a grant matched to the wrong member, leading to identity-aware matching.

> **Synthetic case.** The evaluation and seeded tests are synthetic.

### Errors and limits

Evaluating only with problems monitoring was designed for hides the gaps it cannot see.

### Exercises

- **EX067 — Lag detection time.** How quickly was node lag detected? *Rubric:* 3 = three minutes;; 2 = 3 minutes;; 1 = an hour;; 0 = none.
- **EX068 — Missed case.** Which seeded case was missed? *Rubric:* 3 = a grant matched to the wrong member;; 2 = wrong member;; 1 = unmatched grant;; 0 = none.
- **EX069 — Gap fix.** What is recommended to close the gap? *Rubric:* 3 = match member identity as well as workshop;; 2 = identity matching;; 1 = vague;; 0 = none.

### Synthesis

Goal-based evaluation with seeded tests reveals real strengths and gaps.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) frame a practical research question; (2) collect and analyse operational data; (3) report findings with limits.

### 24.1 Framing a question

Lucas's applied research question is: does the morning summary email reduce the time between a problem occurring and someone acting on it? He chooses it because the makerspace introduced the email halfway through the year, giving before and after periods. He defines the measure as hours from the first log evidence of a problem to the first recorded action. A practical question, tied to a real change and measurable from existing records, is achievable within a term and useful to the organisation that has to decide whether to keep the email.

### 24.2 Collecting and analysing data

Lucas extracts 18 problems from the logs: 9 before the email and 9 after. Median time to action was 26 hours before and 7 hours after. He plots each problem on a timeline and notes that two of the slow ones before the email happened over holiday weekends. He also checks whether problem types differed between periods; they were broadly similar. With only 18 cases, he reports the medians and individual values rather than complex statistics, so readers can see the data directly and judge the difference for themselves.

### 24.3 Reporting with limits

Lucas reports that action times were shorter after the email, while noting limits: small numbers, possible other changes such as more experienced volunteers, and holiday effects. He does not claim the email alone caused the improvement. He recommends keeping the email and continuing to record action times so the finding can be checked over a longer period. Ms Adebayo praises the honest framing. Practical research does not need to be large to be useful, but it must be honest about what it can and cannot show to readers.

### Worked example

Median time to action falls from 26 hours (9 problems) to 7 hours (9 problems) after the morning email, reported with limits on causation.

> **Synthetic case.** The problems and times are synthetic.

### Errors and limits

Claiming a single change caused an improvement ignores other changes in the same period.

### Exercises

- **EX070 — Research measure.** How is time to action measured? *Rubric:* 3 = hours from first log evidence to first recorded action;; 2 = hours to action;; 1 = minutes of downtime;; 0 = none.
- **EX071 — Before and after medians.** What were the median times? *Rubric:* 3 = 26 hours before, 7 after;; 2 = 26/7;; 1 = equal;; 0 = none.
- **EX072 — Alternative explanation.** Name one alternative explanation. *Rubric:* 3 = more experienced volunteers;; 2 = holidays;; 1 = vague;; 0 = none.

### Synthesis

Practical research on real changes, reported with limits, informs operational decisions.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) plan work as a team; (2) divide responsibilities; (3) review each other's work.

### 25.1 Planning as a team

In the studio module Lucas joins three classmates to build an improved monitoring dashboard for the makerspace. They plan in two-week cycles, agreeing goals, tasks and a short demonstration at the end of each cycle. They keep a shared board of tasks and a decision log. The makerspace manager attends demonstrations and gives feedback. Planning in short cycles lets the team adjust early when something does not work, rather than discovering problems at the end. Ms Adebayo assesses both the product and how the team worked together throughout.

### 25.2 Dividing responsibilities

The team divides work by strength and interest: one member builds the data collection, one the dashboard pages, one the alert rules and Lucas the testing and documentation. Each piece has an owner and a reviewer. They agree interfaces between pieces early, such as the format of data passed from collection to the dashboard. Clear division prevents duplicate work and gaps. They also agree that only read-only access to nodes and the database will be used, so their project cannot affect live credits or bookings at the makerspace.

### 25.3 Reviewing each other's work

Every change is reviewed by another team member before merging. Reviews check correctness, clarity and safety: does the code only read data, are errors handled, are credentials kept out of the code? Lucas's review catches a credential accidentally written into a configuration file in the repository; it is removed, rotated and the file added to the ignore list. Peer review spreads knowledge and catches mistakes that authors overlook. The team finishes the dashboard on time, and the manager adopts it for daily use the following month.

### Worked example

The team builds a read-only dashboard in two-week cycles, and Lucas's review catches a committed credential that is removed and rotated.

> **Synthetic case.** The team, project and review are synthetic.

### Errors and limits

Skipping review lets mistakes like committed credentials reach shared repositories.

### Exercises

- **EX073 — Cycle length.** How long is each planning cycle? *Rubric:* 3 = two weeks;; 2 = 2 weeks;; 1 = six months;; 0 = none.
- **EX074 — Lucas's responsibility.** What does Lucas own in the team? *Rubric:* 3 = testing and documentation;; 2 = testing;; 1 = dashboard pages;; 0 = none.
- **EX075 — Review catch.** What did Lucas's review catch? *Rubric:* 3 = a credential written into a configuration file;; 2 = committed credential;; 1 = a typo;; 0 = none.

### Synthesis

Short cycles, clear ownership and peer review produce safe team results.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Web3, blockchain and cryptoasset security: operational handoff

### Learning outcomes

You will (1) prepare systems for handoff; (2) document runbooks; (3) transfer knowledge to operators.

### 26.1 Preparing for handoff

The makerspace plans for its volunteers to run the ledger operations day to day, with Lucas available for escalation. He prepares a handoff package: system diagram, asset inventory, control owners, monitoring guide, runbooks, credential locations (not the credentials themselves) and open issues. He checks that every automated check has a named reader and every runbook has been tested. A system is ready for handoff when someone else can run it safely without the original builder present, which is a higher standard than simply working while the builder watches.

### 26.2 Writing runbooks

Runbooks give step-by-step instructions for common tasks and problems: restarting a node, responding to lag, handling an unmatched privileged event, rotating a service credential, replacing a lost signer device and restoring from backup. Each runbook starts with when to use it, lists steps with expected results, and ends with how to confirm success and whom to inform. Lucas writes them in plain language and has a volunteer follow each on the test ledger. Two steps are unclear and he rewrites them. Tested runbooks work under pressure; untested ones often fail at the worst moment.

### 26.3 Transferring knowledge

Lucas runs three short sessions for volunteers: an overview of the system, a walk-through of the monitoring dashboard and a practice drill responding to a seeded lagging node. Volunteers ask questions he had not considered, which he adds to a frequently asked questions page. He shadows the volunteers for two weeks, intervening only when needed. Knowledge transfer is complete when volunteers handle routine work confidently and know when to escalate. The manager signs off the handoff, and Lucas moves to an advisory role for the remainder of the course.

### Worked example

Lucas hands off with a tested runbook set, three training sessions and two weeks of shadowing before the manager signs off.

> **Synthetic case.** The handoff and sessions are synthetic.

### Errors and limits

Handing off untested runbooks leaves operators with instructions that fail under pressure.

### Exercises

- **EX076 — Handoff standard.** When is a system ready for handoff? *Rubric:* 3 = when someone else can run it safely without the builder;; 2 = without builder;; 1 = when it compiles;; 0 = none.
- **EX077 — Runbook example.** Name one runbook topic. *Rubric:* 3 = replacing a lost signer device;; 2 = restoring from backup;; 1 = ordering lunch;; 0 = none.
- **EX078 — Shadowing period.** How long does Lucas shadow volunteers? *Rubric:* 3 = two weeks;; 2 = 2 weeks;; 1 = one day;; 0 = none.

### Synthesis

A complete package, tested runbooks and supported practice make operational handoff safe.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) plan a safe deployment; (2) validate before and after release; (3) roll back if needed.

### 27.1 Planning a deployment

The developer prepares version 1.4 of the credit contract, adding a per-member identity check suggested by Lucas's evaluation. Lucas helps plan the deployment: test on the test ledger, external review of the change, approval through the change process, a timelocked upgrade on the live ledger and post-deployment checks. The plan names who does each step and when. The timelock gives members and staff 48 hours of notice. Planning deployments carefully matters because contract changes affect every member at once and can be hard to reverse once complete.

### 27.2 Validating before and after

Before release, Lucas runs the configuration check and confirms all tests pass, the compiler version is pinned and the code hash of the reviewed build matches the one proposed for upgrade. After release, he confirms the new code hash on the ledger, that roles and the cap are unchanged, that a small test grant works and that monitoring sees the expected events. He records each check. Validation before and after confirms both that the right thing was deployed and that it behaves as expected in the live environment, not just in testing.

### 27.3 Rolling back if needed

The plan includes a rollback: if post-deployment checks fail, signers pause grants and propose a timelocked return to version 1.3, with members informed. Lucas rehearses the rollback on the test ledger and measures the time needed. In the real deployment all checks pass and no rollback is needed. He records the deployment as complete. Ms Adebayo notes that a deployment plan without a rehearsed rollback assumes success, and that assumption is exactly what experienced technologists learn not to make when real members depend on the system.

### Worked example

Version 1.4 deploys through a 48-hour timelock with code hash matching before and after, and a rehearsed rollback proves unnecessary.

> **Synthetic case.** The deployment and versions are synthetic.

### Errors and limits

Deploying without a rehearsed rollback assumes success that may not come.

### Exercises

- **EX079 — New contract feature.** What does version 1.4 add? *Rubric:* 3 = a per-member identity check;; 2 = identity check;; 1 = higher cap;; 0 = none.
- **EX080 — Hash check.** What hash check is done before release? *Rubric:* 3 = reviewed build hash matches the proposed upgrade;; 2 = code hash;; 1 = vague;; 0 = none.
- **EX081 — Rollback target.** What would rollback return to? *Rubric:* 3 = version 1.3;; 2 = 1.3;; 1 = version 1.0;; 0 = none.

### Synthesis

Planned, validated and reversible deployments protect members from change risk.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) work in a real operational setting; (2) handle routine and unexpected tasks; (3) reflect on professional practice.

### 28.1 Working in the field

Lucas spends a term working with the makerspace's volunteers two days a week. He handles routine tasks, such as monthly maintenance and checklist reviews, and helps with member questions about credits. He learns the rhythm of the organisation: busy evenings, quiet mornings and a monthly board meeting where decisions are made. Field practice shows him that technical work happens among people with other priorities. He schedules maintenance in quiet mornings and brings proposals to the board with short written summaries that members can read beforehand.

### 28.2 Unexpected tasks

One afternoon a member reports that their phone was stolen and asks whether their credits are safe. Lucas follows the runbook: he helps the member contact staff, who verify their identity in person, and the signers approve moving the member's credits to a new address under the documented process. The old address is noted in monitoring. Another day a node's server loses power; the other two keep the ledger running and Lucas restarts it after power returns. Handling unexpected tasks calmly depends on preparation done long before.

### 28.3 Reflecting on practice

Lucas keeps a weekly journal. He notes that his early explanations to members were too technical and that drawings helped. He reflects on an ethical moment: a volunteer asked him to look up another member's booking history out of curiosity, and he declined, explaining that access is for operational need only. Reflection helps him see his own development. Ms Adebayo reads the journal and discusses it with him monthly. She notes that professional judgement grows through practice and honest reflection, not from technical knowledge alone.

### Worked example

Lucas helps move a member's credits after a stolen phone using the documented process and declines a curiosity request for booking history.

> **Synthetic case.** The placement and events are synthetic.

### Errors and limits

Looking up member data out of curiosity breaches the principle of access for need only.

### Exercises

- **EX082 — Maintenance timing.** When does Lucas schedule maintenance? *Rubric:* 3 = quiet mornings;; 2 = mornings;; 1 = busy evenings;; 0 = none.
- **EX083 — Stolen phone response.** How are a member's credits protected after phone theft? *Rubric:* 3 = verified in person and moved to a new address by signers;; 2 = moved;; 1 = vague;; 0 = none.
- **EX084 — Declined request.** What did Lucas decline? *Rubric:* 3 = looking up another member's booking history;; 2 = curiosity lookup;; 1 = a raise;; 0 = none.

### Synthesis

Field practice and reflection build the judgement that technical knowledge alone cannot.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) define and build a capstone improvement; (2) test it with seeded data; (3) document it for operators.

### 29.1 Defining the capstone

Lucas's capstone is a reconciliation service that compares, each hour, credits granted on the ledger with approved workshops, including member identity, and compares credit spending with bookings. It sends alerts for mismatches and produces a monthly summary for the board. Objectives are measurable: detect all seeded mismatches, alert within fifteen minutes, raise no more than one false alarm per week and reduce manual checking time by half. The scope is read-only. Ms Adebayo approves the plan, noting it builds on gaps found in his evaluation.

### 29.2 Building and testing

Lucas builds the service in Python with the standard library and read-only access. He tests it with synthetic datasets containing seeded problems: a grant without a workshop, a grant to the wrong member, a spend without a booking and a duplicate grant. The service detects all four, alerting within nine minutes. On a clean month it raises one false alarm, caused by a booking cancelled and rebooked within a minute; he adjusts the matching window and the false alarm disappears. Every change is reviewed by a classmate before deployment.

### 29.3 Documenting for operators

Lucas writes an operator guide: what the service checks, what each alert means, the first steps for each and whom to contact. He adds runbook links and explains how to restart the service and where logs are stored. A volunteer follows the guide in a trial without help. He also writes a maintenance note listing dependencies and their versions. Documentation ensures the capstone continues to be useful after he graduates, which the makerspace board named as its main condition for adopting student work into daily operations.

### Worked example

Lucas's read-only reconciliation service detects all four seeded problems within nine minutes and removes a rebooking false alarm by adjusting the matching window.

> **Synthetic case.** The capstone and tests are synthetic.

### Errors and limits

A capstone without operator documentation stops being used when its builder leaves.

### Exercises

- **EX085 — False-alarm limit.** What weekly false-alarm limit was set? *Rubric:* 3 = no more than one;; 2 = one;; 1 = ten;; 0 = none.
- **EX086 — Seeded detection.** How quickly did alerts arrive? *Rubric:* 3 = within nine minutes;; 2 = nine minutes;; 1 = an hour;; 0 = none.
- **EX087 — False alarm fix.** What caused the false alarm? *Rubric:* 3 = a booking cancelled and rebooked within a minute;; 2 = rebooking;; 1 = a node fault;; 0 = none.

### Synthesis

A tested, documented capstone turns coursework into lasting operational value.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) assess the capstone against objectives; (2) gather operator feedback; (3) present results and next steps.

### 30.1 Assessing against objectives

Lucas assesses his capstone. It detected all seeded mismatches; alerts arrived within nine minutes against a fifteen-minute target; false alarms averaged 0.5 per week over a month of live use; and manual checking time fell from about two hours to forty minutes a week, a reduction of two thirds. He presents each result with evidence: test logs, alert timestamps and volunteers' time records. Assessing against pre-defined objectives makes his claims checkable, and the assessors can trace each figure to its source in the project folder.

### 30.2 Operator feedback

Four volunteers who used the service for a month give feedback. They find alerts clear and the monthly summary useful for board meetings. One suggests grouping several small alerts into one message during busy periods. Another asks for a simple page showing the last successful run, so they know the service is working. Lucas implements the status page and plans the grouping as future work. Feedback shows how real operators experience the tool, which matters as much as technical performance when deciding whether a tool will continue to be used.

### 30.3 Presenting results and next steps

Lucas presents to assessors and the makerspace board with one diagram, four results and one limitation: the service depends on a single node for ledger data. He recommends reading from two nodes and comparing. Assessors ask how he would know if the service itself stopped; he shows the new status page. The board adopts the service permanently. Reflecting on three years, Lucas notes that the most valuable lessons were careful checking, clear documentation and respect for the people who run systems every day.

### Worked example

The capstone meets all objectives, cutting manual checking by two thirds with 0.5 false alarms a week, and a status page is added after operator feedback.

> **Synthetic case.** The assessment, feedback and presentation are synthetic.

### Errors and limits

A monitoring service with no visible status can fail silently without anyone noticing.

### Exercises

- **EX088 — Time saving.** How much did manual checking fall? *Rubric:* 3 = from about two hours to forty minutes, two thirds;; 2 = two thirds;; 1 = vague;; 0 = none.
- **EX089 — Feedback implemented.** Which feedback did Lucas implement? *Rubric:* 3 = a status page showing the last successful run;; 2 = status page;; 1 = alert grouping;; 0 = none.
- **EX090 — Stated limitation.** What limitation did Lucas state? *Rubric:* 3 = dependence on a single node for ledger data;; 2 = single node;; 1 = vague;; 0 = none.

### Synthesis

Evidence-based assessment, operator feedback and honest limits complete a technologist's capstone.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Lucas Moreau, Ms Grace Adebayo, Pinecrest Technical College, Tidewater Makerspace and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About 350 members.

**EX002.** Reading configuration, opening the database, connecting to peers or syncing.

**EX003.** Resource problems, such as a full disk or overloaded processor.

**EX004.** The booking web application.

**EX005.** Wallet signs, application submits, node shares, block includes, application confirms.

**EX006.** The firewall now lets only the booking application server reach it.

**EX007.** Why each part does what it does, not only what.

**EX008.** With defaults and printed warnings instead of crashing.

**EX009.** 64 bookings in both systems.

**EX010.** Members, machines, bookings, workshops taught or credits earned.

**EX011.** In the booking database under restricted access.

**EX012.** Birth dates, collected for no clear reason.

**EX013.** Actions such as granting credits can be traced to a responsible person.

**EX014.** By likelihood and impact, agreed with the manager.

**EX015.** Adding a simple detective check.

**EX016.** Shell access, and anything outside its data and configuration folders.

**EX017.** Because containers share the host's kernel.

**EX018.** In virtual machines in the college lab.

**EX019.** Whether the right person holds a key, only that the right key signed.

**EX020.** An active account belonging to a volunteer who left last year.

**EX021.** A 2-of-3 multisig of staff.

**EX022.** Members' devices to the web app, database to service, or service to ledger.

**EX023.** A monthly cap on credits per member.

**EX024.** It showed the batch summary was added after a near miss, preventing its removal.

**EX025.** Matched grants, sync alerts, restore time or privileged actions without tickets.

**EX026.** By storing a SHA-256 hash of each export.

**EX027.** 38 minutes against a 60-minute target.

**EX028.** Nodes, services, keys and monitoring rather than contract authoring.

**EX029.** The hash of the previous block.

**EX030.** Consensus risk, because the three nodes are known and controlled.

**EX031.** Owner, location, value or current protection.

**EX032.** Signing something wrong, which points to better batch summaries.

**EX033.** The signer keys and the issuing service.

**EX034.** The issuing service's credit calculation.

**EX035.** The service reading partial data while the database is being updated.

**EX036.** A script compares contract events with the signed batch.

**EX037.** Lost signer device, double grant, full disk, stolen phone or provider outage.

**EX038.** With alerts when disk use reaches 80 percent.

**EX039.** The day-long provider outage, with a paper booking fallback.

**EX040.** Client versions, restricted interfaces, hardware keys, tested backups, matched privileged actions or reviewed alerts.

**EX041.** Meeting its requirements does not guarantee the absence of weaknesses.

**EX042.** An old client version, unreviewed alerts during holidays or an untested backup.

**EX043.** More than two blocks behind the highest node.

**EX044.** Node-c, lagging 14 blocks at minute 4.

**EX045.** Its disk was 99 percent full.

**EX046.** Contract analysis tools often disagreed and each missed many issues.

**EX047.** The open peer port, expected and restricted by the allow-list.

**EX048.** On the monthly day for refunding unused workshop deposits.

**EX049.** A compromised tool on a signer's computer could misrepresent what is being signed.

**EX050.** Quarterly.

**EX051.** Only the multisig signing tools, used on dedicated devices.

**EX052.** 48 hours.

**EX053.** The test-ledger cap was set higher than intended.

**EX054.** The manager.

**EX055.** Six privileged events.

**EX056.** The admin role grant at block 6012.

**EX057.** The export was taken before the ticket's late-day approval.

**EX058.** About forty seconds instead of the usual twelve.

**EX059.** A frequent reporting script overloading node-b's programming interface.

**EX060.** The script moved to node-a and now runs every ten minutes.

**EX061.** One nightly snapshot used by both booking and accounting.

**EX062.** A record of completed batches, so restarts could double grants.

**EX063.** No; it only prepares batches for human signers.

**EX064.** Fifteen settings, five on each of three nodes.

**EX065.** Node-c's public programming interface.

**EX066.** A provider maintenance reset of its firewall and settings.

**EX067.** Within three minutes.

**EX068.** A grant matched to a workshop recorded for the wrong member.

**EX069.** Extending matching to member identity and adding a monthly sample review.

**EX070.** Hours from first log evidence of a problem to the first recorded action.

**EX071.** 26 hours before the email and 7 hours after.

**EX072.** More experienced volunteers or holiday timing of slow cases.

**EX073.** Two weeks.

**EX074.** Testing and documentation.

**EX075.** A credential accidentally written into a configuration file in the repository.

**EX076.** When someone else can run it safely without the original builder present.

**EX077.** Node restart, lag, unmatched events, credential rotation, lost signer device or restore.

**EX078.** Two weeks of shadowing, intervening only when needed.

**EX079.** A per-member identity check from the evaluation.

**EX080.** The reviewed build's code hash matches the one proposed for upgrade.

**EX081.** Version 1.3, through a timelocked proposal.

**EX082.** In quiet mornings.

**EX083.** After in-person identity checks, signers move the credits to a new address.

**EX084.** A volunteer's request to look up another member's booking history.

**EX085.** No more than one false alarm per week.

**EX086.** Within nine minutes, for all four seeded problems.

**EX087.** A booking cancelled and rebooked within a minute.

**EX088.** From about two hours to forty minutes a week, roughly two thirds.

**EX089.** A status page showing the service's last successful run.

**EX090.** The service depends on a single node for ledger data.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Atzei, N., Bartoletti, M., & Cimoli, T. (2017). A survey of attacks on Ethereum smart contracts (SoK). In *Principles of Security and Trust (POST 2017)*, LNCS 10204, 164–186. Springer. <https://doi.org/10.1007/978-3-662-54455-6_8>
- Buterin, V. (2014). *Ethereum whitepaper: A next-generation smart contract and decentralized application platform*. ethereum.org. <https://ethereum.org/en/whitepaper/>
- ConsenSys Diligence. (n.d.). *Ethereum smart contract security best practices*. <https://consensys.github.io/smart-contract-best-practices/>
- Daian, P., Goldfeder, S., Kell, T., Li, Y., Zhao, X., Bentov, I., Breidenbach, L., & Juels, A. (2020). Flash Boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability. *2020 IEEE Symposium on Security and Privacy*, 910–927. <https://doi.org/10.1109/SP40000.2020.00040>
- Durieux, T., Ferreira, J. F., Abreu, R., & Cruz, P. (2020). Empirical review of automated analysis tools on 47,587 Ethereum smart contracts. *Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering*, 530–541. <https://doi.org/10.1145/3377811.3380364>
- Enterprise Ethereum Alliance. (2025). *EEA EthTrust Security Levels specification, version 3*. <https://entethalliance.org/specs/ethtrust-sl/v3/>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Luu, L., Chu, D.-H., Olickel, H., Saxena, P., & Hobor, A. (2016). Making smart contracts smarter. *Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security*, 254–269. <https://doi.org/10.1145/2976749.2978309>
- Nakamoto, S. (2008). *Bitcoin: A peer-to-peer electronic cash system*. <https://bitcoin.org/bitcoin.pdf>
- OWASP Foundation. (n.d.). *OWASP Smart Contract Top 10*. <https://owasp.org/www-project-smart-contract-top-10/>
- Perez, D., & Livshits, B. (2021). Smart contract vulnerabilities: Vulnerable does not imply exploited. *30th USENIX Security Symposium*. <https://www.usenix.org/conference/usenixsecurity21/presentation/perez>
- SmartContractSecurity. (n.d.). *Smart Contract Weakness Classification (SWC) registry*. <https://swcregistry.io/>
- Tsankov, P., Dan, A., Drachsler-Cohen, D., Gervais, A., Bünzli, F., & Vechev, M. (2018). Securify: Practical security analysis of smart contracts. *Proceedings of the 2018 ACM SIGSAC Conference on Computer and Communications Security*, 67–82. <https://doi.org/10.1145/3243734.3243780>
- Wood, G. (n.d.). *Ethereum: A secure decentralised generalised transaction ledger* (Ethereum yellow paper, continuously revised). <https://ethereum.github.io/yellowpaper/paper.pdf>
- Yaga, D., Mell, P., Roby, N., & Scarfone, K. (2018). *Blockchain technology overview* (NIST IR 8202). NIST. <https://doi.org/10.6028/NIST.IR.8202>
