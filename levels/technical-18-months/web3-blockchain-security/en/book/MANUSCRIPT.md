# Web3, Blockchain and Cryptoasset Security: Technical Course

- Language: English (`en`); course 055, Technical course (18 months).
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; Two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical trainees learning to run, monitor and troubleshoot blockchain services safely under supervision.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only contracts, wallets and systems you are authorised to assess, on local simulations or test networks; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic ledgers, transactions, contract inventories and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one technical trainee supporting a tool library's deposit token on a three-node permissioned ledger, from service architecture, networks, identities, scripting and scope, through the system model, telemetry, failure modes, tools, control configuration and verification, to contained labs, troubleshooting, automation, dependencies, documentation and a supervised project. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Aiko Brennan** | Technical trainee | Invented |
| **Mr Tomasz Kowal** | Mentor | Invented |
| **Northfield Technical Institute** | Fictional institute | Invented |
| **Greenway Tool Library** | Fictional client (about 600 borrowers) | Invented |

### Core sources

Nakamoto, [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf); Wood, [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf); NIST [IR 8202](https://doi.org/10.6028/NIST.IR.8202); [SWC registry](https://swcregistry.io/); [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/); EEA [EthTrust Security Levels v3](https://entethalliance.org/specs/ethtrust-sl/v3/); [ConsenSys smart contract best practices](https://consensys.github.io/smart-contract-best-practices/); Atzei et al. ([2017](https://doi.org/10.1007/978-3-662-54455-6_8)); Luu et al. ([2016](https://doi.org/10.1145/2976749.2978309)). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe how services are built from components; (2) place a ledger node within a service; (3) identify single points of failure.

### 1.1 The case and the service

Aiko Brennan is a technical trainee at the fictional Northfield Technical Institute, mentored by Mr Tomasz Kowal. During her eighteen-month course she supports the fictional Greenway Tool Library, about 600 borrowers, which records refundable borrowing deposits as tokens on a permissioned Ethereum-compatible ledger with three nodes. Borrowers pay a deposit token when taking a tool and receive it back on return. Every person, address and figure here is synthetic. Aiko starts by learning how the library's service is assembled from components, because every later task depends on knowing which part does what.

### 1.2 Components of the service

The service has a web front end where borrowers reserve tools, an application server that handles reservations, a database of borrowers and tools, a deposit service that prepares token transfers, three ledger nodes and a monitoring server. Aiko draws them as boxes with arrows showing requests and data. She labels which components the library runs itself and which are rented, such as the cloud servers. Seeing the architecture helps her understand that the ledger is one part of a larger service, and that most daily work concerns the components around it.

### 1.3 Single points of failure

A single point of failure is a component whose failure stops the whole service. Aiko finds two: the application server runs on one machine, and the deposit service has no standby. The three ledger nodes are not single points, because the ledger continues with two. She records each with its impact and a possible remedy, such as a second application server or a documented manual fallback for deposits. Mr Kowal explains that identifying single points of failure early is one of the most useful contributions a technician can make to service reliability.

### Worked example

Aiko maps seven components and finds two single points of failure: the lone application server and the deposit service without standby.

> **Synthetic case.** Aiko Brennan, Mr Tomasz Kowal, Northfield Technical Institute, Greenway Tool Library and all data are synthetic.

### Errors and limits

Assuming a ledger's redundancy protects the whole service ignores single points around it.

### Exercises

- **EX001 — Library size.** How many borrowers does Greenway serve? *Rubric:* 3 = about 600;; 2 = 600;; 1 = 6,000;; 0 = none.
- **EX002 — Deposit token use.** How are deposit tokens used? *Rubric:* 3 = paid when borrowing, returned on return;; 2 = refundable deposit;; 1 = sold;; 0 = none.
- **EX003 — Not a single point.** Why are the ledger nodes not single points? *Rubric:* 3 = the ledger continues with two of three;; 2 = redundancy;; 1 = they are;; 0 = none.
- **EX004 — Remedy example.** Name one remedy for a single point. *Rubric:* 3 = a second application server;; 2 = manual deposit fallback;; 1 = delete it;; 0 = none.

### Synthesis

Knowing a service's components reveals where it can fail as a whole.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) map network connections; (2) restrict exposure of node services; (3) verify connectivity safely.

### 2.1 Mapping connections

Aiko lists every network connection in the service: borrowers to the web front end over encrypted web traffic, the application server to the database, the deposit service to one node's programming interface, nodes to each other through peer connections, and the monitoring server to all components. For each she records the port and protocol. A complete connection map makes it possible to check that only intended connections exist. She notes that encrypted protocols protect data in transit, while the map shows who should be allowed to connect to whom in the first place.

### 2.2 Restricting exposure

Node programming interfaces can submit transactions, so they must be reachable only by trusted services. Aiko checks firewall rules and finds that node three's interface accepts connections from the whole office network, not just the deposit service. She reports it, and Mr Kowal approves a change restricting it. Peer ports are limited to the other nodes' addresses. NIST IR 8202 explains that permissioned ledgers rely on controlling participation and access. Restricting exposure reduces the number of ways anything can go wrong, whether by mistake or misuse.

### 2.3 Verifying connectivity safely

After the change, Aiko verifies that the deposit service still reaches node three and that an office computer no longer can. She uses simple connection tests from authorised machines only, within the scope Mr Kowal approved in writing. She does not probe systems outside the library's own network. She records the tests and results. Verification confirms that a security change achieved its purpose without breaking the service. Technicians often skip this step, and Mr Kowal warns that unverified changes are a common cause of both outages and false confidence.

### Worked example

Aiko restricts node three's interface from the whole office network to the deposit service and verifies both outcomes from authorised machines.

> **Synthetic case.** The network and change are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Making a firewall change without verifying it can break the service or leave exposure unchanged.

### Exercises

- **EX005 — Map contents.** What does Aiko record for each connection? *Rubric:* 3 = port and protocol;; 2 = ports;; 1 = colour;; 0 = none.
- **EX006 — Exposure found.** What exposure did she find? *Rubric:* 3 = node three's interface open to the office network;; 2 = node three;; 1 = peer ports;; 0 = none.
- **EX007 — Verification scope.** What limits Aiko's connectivity tests? *Rubric:* 3 = authorised machines within written scope;; 2 = written scope;; 1 = vague;; 0 = none.
- **EX008 — Unverified change risk.** Why verify changes? *Rubric:* 3 = unverified changes cause outages and false confidence;; 2 = confirm effect;; 1 = habit;; 0 = none.

### Synthesis

Connection maps, restricted exposure and safe verification secure node networking.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) manage service and administrator accounts; (2) protect key files; (3) review access regularly.

### 3.1 Service and administrator accounts

Each server runs services under dedicated accounts with limited rights. Aiko checks that the node software runs as its own user without administrator privileges and that administrators use personal accounts rather than a shared one. Personal accounts mean every administrative action is recorded against a person. She finds one server where a shared administrator account is still enabled and recommends disabling it once everyone has personal access. Accounts are identities in the operating system, and managing them carefully is the base of all other access control on the servers.

### 3.2 Protecting key files

Each node has a key file used to sign blocks, and the deposit service has credentials to submit transactions. Aiko checks file permissions: node key files are readable only by the node user, and credentials are stored in the server's protected secret store rather than plain configuration files. She finds one credential in a configuration file and arranges for it to be moved and rotated. Key files are among the most sensitive data on a server, because whoever reads them can act as that node or service without anyone noticing.

### 3.3 Regular access reviews

Aiko sets a quarterly access review: list every account on each server, compare with the approved list, remove accounts for people who have left and confirm that rights match current roles. In the first review she finds an account for a contractor whose work ended three months earlier. It is disabled. She records the review date, findings and actions. Mr Kowal explains that access tends to accumulate over time, because adding access is easy and removing it is easy to forget, so regular reviews are the only reliable remedy.

### Worked example

Aiko disables a shared administrator account and a departed contractor's account, and moves a credential from a configuration file into the secret store.

> **Synthetic case.** The accounts and findings are synthetic.

### Errors and limits

Shared administrator accounts make actions untraceable to individuals.

### Exercises

- **EX009 — Personal accounts benefit.** Why use personal administrator accounts? *Rubric:* 3 = actions are recorded against a person;; 2 = traceability;; 1 = speed;; 0 = none.
- **EX010 — Credential location.** Where should credentials be stored? *Rubric:* 3 = the server's protected secret store;; 2 = secret store;; 1 = configuration file;; 0 = none.
- **EX011 — Review finding.** What did the first access review find? *Rubric:* 3 = a contractor account three months after work ended;; 2 = old contractor;; 1 = vague;; 0 = none.
- **EX012 — Review frequency.** How often are access reviews run? *Rubric:* 3 = quarterly;; 2 = every quarter;; 1 = yearly;; 0 = none.

### Synthesis

Dedicated accounts, protected key files and regular reviews control server identities.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) write small scripts to read ledger data; (2) parse common formats; (3) validate data before use.

### 4.1 Small scripts

Aiko writes Python scripts with only the standard library to automate routine checks. Her first script asks a node for its latest block number and prints it with the time. A second compares the block numbers of all three nodes. She learns to structure scripts as small functions, add clear messages and handle errors such as a node not responding. Scripts make checks fast and consistent. Mr Kowal reviews her code and suggests storing settings like node addresses in one place, so they can be changed without editing every script.

### 4.2 Parsing common formats

Ledger tools return data in JSON, while the library's database exports CSV. Aiko uses Python's json and csv modules to read both. She extracts transfer events with sender, receiver, amount and block number, and loan records with borrower code, tool and dates. She learns that formats have quirks: numbers may arrive as text, and dates may use different formats. She converts each field explicitly. Parsing correctly is the foundation for every comparison later, because a misread field produces wrong results that look perfectly believable.

### 4.3 Validating data

Before using data, Aiko's scripts check it: amounts must be whole positive numbers, block numbers must increase, dates must be valid and borrower codes must exist in the database. Invalid records are listed separately rather than silently skipped. On a synthetic export she finds two loan records with return dates before borrow dates, caused by a data-entry error at the counter. Validation stops bad data from producing misleading results and often reveals process problems, like this one, that are worth fixing at the source rather than in every script.

### Worked example

Aiko's validation finds two loan records with return dates before borrow dates, traced to counter data entry.

> **Synthetic case.** The scripts and data are synthetic.

### Errors and limits

Silently skipping invalid records hides data problems that need fixing at the source.

### Exercises

- **EX013 — Settings advice.** What did Mr Kowal suggest about settings? *Rubric:* 3 = store them in one place;; 2 = central settings;; 1 = hard-code everywhere;; 0 = none.
- **EX014 — Format quirk.** Name one format quirk Aiko meets. *Rubric:* 3 = numbers arriving as text;; 2 = date formats;; 1 = vague;; 0 = none.
- **EX015 — Validation rule.** Name one validation rule. *Rubric:* 3 = block numbers must increase;; 2 = amounts positive whole numbers;; 1 = anything goes;; 0 = none.
- **EX016 — Invalid records found.** What invalid records were found? *Rubric:* 3 = two loans returned before they were borrowed;; 2 = date errors;; 1 = vague;; 0 = none.

### Synthesis

Small scripts that parse carefully and validate first make ledger data trustworthy.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) work within an approved scope; (2) collect evidence properly; (3) keep records that others can check.

### 5.1 Approved scope

Before any security task, Aiko confirms the scope in writing with Mr Kowal and the library manager: which systems, which activities, which times and which data. Her scope covers the library's servers, its test ledger, read-only access to the live ledger and synthetic data. It excludes borrowers' devices, the cloud provider's infrastructure and any public blockchain. If she notices something outside scope she reports it rather than investigating. Scope protects the library, the borrowers and Aiko herself, and it keeps security work lawful and predictable for everyone involved.

### 5.2 Collecting evidence

When Aiko checks something, she keeps evidence: command outputs, exported data, screenshots where nothing better exists and notes of what she did. Each item records the time, source and method. She stores a SHA-256 hash of each exported file so later changes can be detected. Evidence should come directly from systems where possible, not from memory. Mr Kowal explains that evidence allows others to verify findings and supports decisions, and that unrecorded checks are, for practical purposes, checks that never happened at all.

### 5.3 Checkable records

Aiko keeps a simple work log: date, task, scope reference, steps, evidence locations and results. When she reports that node backups are current, the log shows exactly how she checked. Another technician can repeat her steps and reach the same result. This repeatability is what makes records trustworthy. She also notes mistakes and corrections, rather than hiding them. Clear, honest records protect technicians when questions arise later and help the library show auditors or its board that its systems are properly looked after.

### Worked example

Aiko works under written scope excluding borrowers' devices, hashes every export and keeps a repeatable work log including corrections.

> **Synthetic case.** The scope, evidence and log are synthetic.

### Errors and limits

Investigating beyond written scope, even helpfully, can be unlawful and erode trust.

### Exercises

- **EX017 — Scope exclusion.** Name one item outside Aiko's scope. *Rubric:* 3 = borrowers' devices;; 2 = public blockchains;; 1 = library servers;; 0 = none.
- **EX018 — Evidence integrity.** How does she make export changes detectable? *Rubric:* 3 = storing a SHA-256 hash of each file;; 2 = hashing;; 1 = renaming files;; 0 = none.
- **EX019 — Record quality.** What makes a record trustworthy? *Rubric:* 3 = another technician can repeat the steps;; 2 = repeatability;; 1 = length;; 0 = none.
- **EX020 — Mistake handling.** How are mistakes handled in the log? *Rubric:* 3 = noted with corrections, not hidden;; 2 = recorded;; 1 = deleted;; 0 = none.

### Synthesis

Written scope, proper evidence and checkable records make technical security work reliable.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Web3, blockchain and cryptoasset security: system model

### Learning outcomes

You will (1) describe the deposit token system as states and actions; (2) list its rules; (3) identify who can change what.

### 6.1 States and actions

Aiko models the deposit system. Its state includes each borrower address's token balance, the library's holding balance, the paused flag and the role list. Actions are issue deposit tokens to a borrower when they pay, lock a deposit when a tool is borrowed, release it when the tool is returned, transfer, pause and change roles. For each action she lists who may perform it and what it changes. A model like this lets a technician understand what normal activity looks like in the ledger's events and spot actions that do not fit.

### 6.2 Rules of the system

Aiko lists the rules the system must keep: the total of all balances equals tokens issued minus tokens redeemed; no balance is negative; a deposit is released only when the database shows the tool returned; and only the library's 2-of-3 staff multisig can issue tokens. These rules come from the developer's documentation and the library's policy. Writing them down gives Aiko clear things to check. Later chapters turn each rule into an automatic check that reads ledger events and the database and reports any difference.

### 6.3 Who can change what

Aiko records roles: borrowers can transfer their own tokens; the deposit service can request locks and releases; the staff multisig can issue tokens and approve releases above a threshold; an administrator role behind a 48-hour timelock can change roles; and two staff can pause. The OWASP Smart Contract Top 10 lists access control failures among the most common weaknesses. Knowing exactly who can change what tells a technician which ledger events need the closest watching, especially role changes and pauses. A written role table also gives reviewers something concrete to compare against the deployed configuration.

### Worked example

Aiko models six actions and four rules, and records that only the 2-of-3 staff multisig issues tokens while role changes wait 48 hours.

> **Synthetic case.** The system model is synthetic; the OWASP Smart Contract Top 10 is a real source.

### Errors and limits

Watching all events equally misses the role changes and pauses that matter most.

### Exercises

- **EX021 — Deposit release rule.** When may a deposit be released? *Rubric:* 3 = when the database shows the tool returned;; 2 = on return;; 1 = anytime;; 0 = none.
- **EX022 — Supply rule.** State the supply rule. *Rubric:* 3 = balances total issued minus redeemed;; 2 = totals match;; 1 = supply grows;; 0 = none.
- **EX023 — Issuer role.** Who can issue tokens? *Rubric:* 3 = the 2-of-3 staff multisig;; 2 = multisig;; 1 = the deposit service;; 0 = none.
- **EX024 — Pause holders.** Who can pause the system? *Rubric:* 3 = two staff;; 2 = 2 staff;; 1 = any borrower;; 0 = none.

### Synthesis

A state, rule and role model shows a technician what normal looks like and what to watch.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Web3, blockchain and cryptoasset security: data and telemetry

### Learning outcomes

You will (1) identify useful telemetry sources; (2) collect node and ledger metrics; (3) store telemetry safely.

### 7.1 Telemetry sources

Telemetry is the stream of data that shows how a system is behaving. For the library Aiko identifies sources: node metrics such as block height, peer count and resource use; ledger events such as transfers, locks, releases and role changes; application logs from the reservation and deposit services; and server logs for logins and system changes. She lists each source, how to read it and how often. Good telemetry lets technicians see problems early. Without it, the first sign of trouble is usually a borrower complaining at the counter.

### 7.2 Collecting metrics

Aiko writes a read-only collector that every minute records each node's block height, peer count, disk use and memory, and every hour exports new ledger events. Results go to the monitoring server with timestamps. She keeps collection light so it does not overload the nodes, having learned that heavy polling can itself slow a service. She tests the collector on the test ledger before using it on live nodes. Collected metrics become the input for alerts, reports and troubleshooting in later chapters of her course.

### 7.3 Storing telemetry safely

Telemetry can contain sensitive information, such as borrower addresses linked to loans. Aiko stores it on the monitoring server with access limited to technicians and the manager, keeps detailed events for ninety days and summaries for two years, and does not copy personal data from the database into telemetry. Logs are protected from alteration by writing daily hashes. Mr Kowal explains that telemetry is evidence, so it must be kept safely and for long enough to investigate, but not longer than needed for privacy.

### Worked example

Aiko collects node metrics every minute and events hourly, stores detail for ninety days with restricted access and writes daily log hashes.

> **Synthetic case.** The telemetry design is synthetic.

### Errors and limits

Polling nodes too heavily for telemetry can slow the service being monitored.

### Exercises

- **EX025 — Telemetry source.** Name one telemetry source. *Rubric:* 3 = node metrics such as block height;; 2 = ledger events;; 1 = weather data;; 0 = none.
- **EX026 — Collection frequency.** How often are node metrics collected? *Rubric:* 3 = every minute;; 2 = each minute;; 1 = yearly;; 0 = none.
- **EX027 — Detail retention.** How long are detailed events kept? *Rubric:* 3 = ninety days;; 2 = 90 days;; 1 = forever;; 0 = none.
- **EX028 — Log protection.** How are logs protected from alteration? *Rubric:* 3 = daily hashes;; 2 = hashing;; 1 = vague;; 0 = none.

### Synthesis

Well-chosen, lightly collected and safely stored telemetry shows how a ledger behaves.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Web3, blockchain and cryptoasset security: failure modes

### Learning outcomes

You will (1) list ways the deposit system can fail; (2) link failures to symptoms; (3) prioritise by impact.

### 8.1 Listing failure modes

Aiko lists failure modes for the deposit system: a node falls behind; two nodes fail and the ledger stops; the deposit service crashes mid-release; a staff signer loses their device; the database and ledger disagree about a loan; a role is changed unexpectedly; and a backup cannot be restored. For each she writes a short description without technical misuse detail. Listing failure modes before they happen lets the library prepare responses calmly, rather than inventing them under pressure when a borrower is waiting.

### 8.2 Linking failures to symptoms

Each failure shows itself through symptoms. A lagging node shows a growing height difference. A stopped ledger shows no new blocks. A crashed deposit service shows returns recorded in the database without matching releases on the ledger. A database-ledger disagreement appears in reconciliation. An unexpected role change appears as a privileged event without an approved change. Aiko builds a table from symptom to likely failures, so that whoever sees a symptom knows where to look first. This table becomes the front page of her troubleshooting guide.

### 8.3 Prioritising by impact

With Mr Kowal and the manager, Aiko ranks failures by impact and likelihood. An unexpected role change is rare but high impact, because it could change who controls deposits. A crashed deposit service is more likely and affects borrowers directly. A lagging node is common but low impact while the other two are healthy. The ranking guides which monitoring and runbooks she builds first. She records the reasoning, and plans to revisit it after six months of telemetry gives better evidence of what actually happens.

### Worked example

Aiko lists seven failure modes, maps symptoms to them and ranks an unexpected role change as rare but high impact.

> **Synthetic case.** The failure modes and ranking are synthetic.

### Errors and limits

Building monitoring in the order failures come to mind neglects rare high-impact events.

### Exercises

- **EX029 — Crash symptom.** What symptom shows a crashed deposit service? *Rubric:* 3 = returns without matching releases;; 2 = missing releases;; 1 = slow website;; 0 = none.
- **EX030 — Symptom table purpose.** What is the symptom table for? *Rubric:* 3 = knowing where to look first;; 2 = triage;; 1 = decoration;; 0 = none.
- **EX031 — Rare high-impact failure.** Which failure is rare but high impact? *Rubric:* 3 = an unexpected role change;; 2 = role change;; 1 = lagging node;; 0 = none.
- **EX032 — Ranking review.** When will the ranking be revisited? *Rubric:* 3 = after six months of telemetry;; 2 = six months;; 1 = never;; 0 = none.

### Synthesis

Failure modes linked to symptoms and ranked by impact guide preparation.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Web3, blockchain and cryptoasset security: tools and methods

### Learning outcomes

You will (1) choose appropriate tools for checks; (2) follow a consistent method; (3) interpret tool results carefully.

### 9.1 Choosing tools

Aiko's toolkit includes the ledger client's command-line interface for node status, her Python scripts for comparisons, a log viewer, a configuration scanner and the hardware wallet utility used by staff signers. She chooses widely used, maintained tools from trusted sources and records each tool's version. She avoids installing unknown utilities on servers. Tools can introduce risk themselves: a compromised utility on a signer's computer could misrepresent a transaction. Mr Kowal reviews her list and asks her to note which tools can change systems and which only read.

### 9.2 A consistent method

Aiko follows the same method for each check: confirm scope, collect data with a recorded tool and version, compare with the expected state, record differences, confirm important differences manually and report. A consistent method makes results comparable over time and lets others repeat them. She writes the method on one page and attaches it to her work log. Consistency also helps her notice when something changes, because the method itself stays the same and only the system's behaviour differs from one check to the next.

### 9.3 Interpreting results carefully

Tools produce results that need interpretation. When her configuration scanner flags an open port on node two, Aiko checks and finds it is the peer port, expected and limited to the other nodes. She records it as expected with the reason. Durieux and colleagues' 2020 study of contract analysis tools found frequent disagreement and many missed issues, which shows that tool output is a starting point, not a verdict. Careful interpretation prevents both ignoring real problems and chasing harmless ones that waste a technician's limited time.

### Worked example

Aiko follows a one-page method for every check and records a flagged peer port on node two as expected after manual confirmation.

> **Synthetic case.** The toolkit and results are synthetic; Durieux et al. (2020) is a real source.

### Errors and limits

Treating tool output as a verdict leads to chasing harmless flags or ignoring missed issues.

### Exercises

- **EX033 — Tool risk.** How can a tool itself introduce risk? *Rubric:* 3 = a compromised utility could misrepresent a transaction;; 2 = compromise;; 1 = cost;; 0 = none.
- **EX034 — Method step.** Name one step in Aiko's method. *Rubric:* 3 = confirm important differences manually;; 2 = collect data with recorded version;; 1 = skip scope;; 0 = none.
- **EX035 — Flag outcome.** What was the flagged port on node two? *Rubric:* 3 = the expected peer port;; 2 = peer port;; 1 = a breach;; 0 = none.
- **EX036 — Study lesson.** What does the tool study show? *Rubric:* 3 = tool output is a starting point, not a verdict;; 2 = tools miss issues;; 1 = tools are perfect;; 0 = none.

### Synthesis

Trusted tools, a consistent method and careful interpretation make checks dependable.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Web3, blockchain and cryptoasset security: control configuration

### Learning outcomes

You will (1) configure controls on nodes and services; (2) document intended settings; (3) check settings against the record.

### 10.1 Configuring node controls

Aiko helps configure node controls: peer allow-lists limited to the three nodes, programming interfaces limited to the deposit service, node software running as dedicated users, time synchronisation enabled and log retention set to ninety days. Each setting has an intended value agreed with Mr Kowal. She applies changes through the library's change process, one node at a time, confirming the ledger keeps running after each. Configuring controls carefully and in order prevents the common mistake of locking out a needed service or taking two nodes offline at once.

### 10.2 Service and ledger controls

For the deposit service Aiko confirms it holds only the credentials it needs, cannot issue tokens and can request releases only for loans marked returned. On the ledger, the developer confirms the 2-of-3 staff multisig for issuing, the 48-hour administrator timelock and two-person pause. Aiko records each setting with its location and owner. The ConsenSys best practices encourage simple, well-documented controls. She notes that a control documented clearly is easier to check and harder to change by accident during later maintenance.

### 10.3 Checking against the record

Aiko writes a read-only script that reads node configuration files and compares each setting with the intended value. The first run finds node one keeping logs for thirty days instead of ninety, a leftover from initial setup. It is corrected through a change ticket and the script rerun shows no differences. She schedules the check weekly and after every maintenance. Comparing actual settings with a record is the simplest way to catch drift, which otherwise goes unnoticed until it causes a problem during an incident or audit.

### Worked example

Aiko applies node controls one node at a time and her comparison script finds node one keeping logs for thirty days instead of ninety.

> **Synthetic case.** The controls and findings are synthetic; ConsenSys best practices is a real source.

### Errors and limits

Changing controls on several nodes at once risks taking the ledger offline.

### Exercises

- **EX037 — Interface restriction.** Who may reach node programming interfaces? *Rubric:* 3 = only the deposit service;; 2 = deposit service;; 1 = everyone;; 0 = none.
- **EX038 — Service limit.** What can the deposit service not do? *Rubric:* 3 = issue tokens;; 2 = cannot issue;; 1 = read data;; 0 = none.
- **EX039 — Drift found.** What did the first comparison find? *Rubric:* 3 = node one logs kept for thirty days instead of ninety;; 2 = log retention;; 1 = vague;; 0 = none.
- **EX040 — Check schedule.** When does the comparison run? *Rubric:* 3 = weekly and after every maintenance;; 2 = weekly;; 1 = never;; 0 = none.

### Synthesis

Carefully configured, documented and regularly compared controls stay effective.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Web3, blockchain and cryptoasset security: verification

### Learning outcomes

You will (1) verify controls with planned tests; (2) use the test ledger safely; (3) record verification results.

### 11.1 Planned tests

Aiko writes a verification plan listing each control and how to test it. A single staff signature must not issue tokens. A release for a loan not marked returned must be refused. An administrator change must wait 48 hours. An outside computer must not reach node interfaces. A login with a shared account must fail. Each test has an expected result. Planning tests in advance ensures nothing is forgotten and that results can be compared with expectations objectively rather than interpreted after the fact.

### 11.2 Using the test ledger safely

All ledger tests run on the library's separate test ledger with synthetic borrowers and tokens of no value. Test keys are clearly labelled and kept apart from live keys. Aiko never uses live keys for testing and never sends test transactions to the live ledger. The test ledger is reset after each round. Mr Kowal explains that confusing test and live environments is a common cause of real incidents, so separation and labelling are themselves important controls, not just good housekeeping practices.

### 11.3 Recording results

Aiko records each test: date, environment, steps, expected and actual result. Four of five tests pass. The release test fails: a release for a loan not yet returned succeeds on the test ledger, because the deposit service checks the database but the database's test copy marked all loans returned by default. She reports it, the test data is corrected and the test passes. The finding shows that tests depend on realistic data. She stores the results with the configuration and contract versions tested.

### Worked example

Four of five planned tests pass; the release test fails because test data marked all loans returned by default, and passes after correction.

> **Synthetic case.** The tests and results are synthetic.

### Errors and limits

Testing with unrealistic data can make a control appear broken or working when it is not.

### Exercises

- **EX041 — Planned test.** Name one planned test. *Rubric:* 3 = a single signature must not issue tokens;; 2 = release refused for unreturned loan;; 1 = deploy to live;; 0 = none.
- **EX042 — Key separation.** How are test keys kept apart? *Rubric:* 3 = clearly labelled and separate from live keys;; 2 = labelled;; 1 = shared;; 0 = none.
- **EX043 — Failing test.** Which test failed at first? *Rubric:* 3 = the release test for an unreturned loan;; 2 = release;; 1 = timelock;; 0 = none.
- **EX044 — Failure cause.** Why did it fail? *Rubric:* 3 = test data marked all loans returned by default;; 2 = bad test data;; 1 = code bug;; 0 = none.

### Synthesis

Planned tests on a separate ledger, with recorded results, verify controls honestly.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) verify backups by digest and age; (2) interpret backup problems; (3) act on the results.

### 12.1 Why verify backups

Backups protect the library against node failure, but only if they are complete and recent. Each night the nodes' data is copied to a backup disk and a SHA-256 digest of each copy is recorded. Aiko writes a read-only check that recalculates each digest and compares it with the recorded one, and checks that each backup is no older than 24 hours. This contained lab uses three synthetic backups. It reads only local test data and uses Python's standard library, so it cannot affect any live system.

### Lab — Backup digest and age check

```python
"""Verify synthetic node backups by digest and age (read-only)."""
import hashlib

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

# name, content now on backup disk, digest recorded at backup time, age in hours
CONTENT = {"node1": "chaindata-node1-h8812", "node2": "chaindata-node2-h8812", "node3": "chaindata-node3-h8790"}
RECORDED = {"node1": sha("chaindata-node1-h8812"), "node2": sha("chaindata-node2-h8811"), "node3": sha("chaindata-node3-h8790")}
AGE_H = {"node1": 6, "node2": 6, "node3": 52}
MAX_AGE_H = 24

def main():
    for n in sorted(CONTENT):
        notes = []
        if sha(CONTENT[n]) != RECORDED[n]:
            notes.append("digest mismatch")
        if AGE_H[n] > MAX_AGE_H:
            notes.append(f"age {AGE_H[n]}h > {MAX_AGE_H}h")
        print(f"{n}: {'ok' if not notes else '; '.join(notes)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_backup.py`. Verified output:

```text
node1: ok
node2: digest mismatch
node3: age 52h > 24h
```

### 12.2 Interpreting the results

The lab reports node1's backup as ok, node2's as a digest mismatch and node3's as 52 hours old, beyond the 24-hour limit. A digest mismatch means the stored backup is not the one recorded: it may have been overwritten, corrupted or recorded incorrectly. An old backup means recent changes would be lost on restore. Aiko investigates: node2's backup job was rerun by hand after the digest was recorded, so the copy is newer than its record; node3's backup job has been failing silently since a disk path changed.

### 12.3 Acting on the results

Aiko records both findings and raises tickets. For node2, the backup procedure is changed so the digest is always recorded after the final copy, and a fresh backup with a matching digest is taken. For node3, the disk path is corrected, the job is rerun and an alert is added for any failed backup job. She then performs a test restore of node3 on a lab machine to confirm the new backup works. Mr Kowal notes that the restore test is what finally proves a backup, since a digest only proves the file has not changed.

### Worked example

The lab finds node2's digest mismatched after a manual rerun and node3's backup 52 hours old from a silently failing job; both are fixed and a restore is tested.

> **Synthetic case.** The backups and findings are synthetic.

### Errors and limits

A backup job that fails silently leaves the organisation believing it is protected.

### Exercises

- **EX045 — Age limit.** What maximum backup age does the lab allow? *Rubric:* 3 = 24 hours;; 2 = 24h;; 1 = 52 hours;; 0 = none.
- **EX046 — Lab results.** What does the lab report for node2 and node3? *Rubric:* 3 = node2 digest mismatch, node3 52 hours old;; 2 = mismatch and age;; 1 = all ok;; 0 = none.
- **EX047 — Node3 cause.** Why was node3's backup old? *Rubric:* 3 = the job failed silently after a disk path change;; 2 = path change;; 1 = deliberate;; 0 = none.
- **EX048 — Final proof.** What finally proves a backup works? *Rubric:* 3 = a test restore;; 2 = restoring;; 1 = a digest;; 0 = none.

### Synthesis

Checking digest and age, then testing a restore, proves backups can be relied on.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Web3, blockchain and cryptoasset security: troubleshooting

### Learning outcomes

You will (1) troubleshoot methodically; (2) use telemetry to test hypotheses; (3) record solutions.

### 13.1 A reported problem

Counter staff report that returned tools sometimes take more than ten minutes to show a released deposit, while it usually takes under one. Aiko defines the symptom precisely: delays occur only for some returns, mostly in the afternoon. She gathers telemetry for the affected period: block production, node heights, deposit service logs and database timings. A precise symptom narrows the search. Mr Kowal reminds her to change nothing until she has data, because changes made in a hurry can hide the real cause and create new problems.

### 13.2 Testing hypotheses

Aiko lists hypotheses: a slow node, a stalled deposit service queue, database locking or slow signer approvals for releases above the threshold. Telemetry shows nodes healthy and blocks regular. Deposit service logs show releases above the threshold waiting for staff multisig approval, while small releases are quick. Afternoon delays match times when only one signer is on duty. The cause is process, not technology: large releases need two signers and only one is present. Testing each hypothesis against data avoids blaming the ledger for a staffing pattern.

### 13.3 Recording and solving

The manager adjusts rosters so two signers are available during opening hours, and the threshold for multisig release is reviewed and kept, since it protects larger deposits. Aiko records the symptom, hypotheses, evidence, cause and solution in the troubleshooting log, with a summary line for quick searching. Delays drop to under a minute for all but a few cases. She notes that many technical-looking problems have human or process causes, and good troubleshooting follows the evidence wherever it leads, even away from the technology.

### Worked example

Delayed releases are traced to large releases waiting for a second signer in the afternoon, solved by rostering two signers during opening hours.

> **Synthetic case.** The problem and solution are synthetic.

### Errors and limits

Assuming a technical cause can hide a process problem such as signer availability.

### Exercises

- **EX049 — Symptom definition.** How does Aiko define the symptom? *Rubric:* 3 = some returns over ten minutes, mostly afternoons;; 2 = afternoon delays;; 1 = website slow;; 0 = none.
- **EX050 — Hypothesis list.** Name one hypothesis tested. *Rubric:* 3 = stalled deposit service queue;; 2 = slow node;; 1 = sunspots;; 0 = none.
- **EX051 — Actual cause.** What was the actual cause? *Rubric:* 3 = only one signer on duty for large releases;; 2 = signer availability;; 1 = slow node;; 0 = none.
- **EX052 — Threshold decision.** What happened to the multisig threshold? *Rubric:* 3 = reviewed and kept;; 2 = kept;; 1 = removed;; 0 = none.

### Synthesis

Methodical troubleshooting follows evidence to the real cause, technical or not.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Web3, blockchain and cryptoasset security: automation

### Learning outcomes

You will (1) automate routine checks safely; (2) schedule and report results; (3) keep people in control of changes.

### 14.1 Choosing what to automate

Aiko automates checks she runs repeatedly: node height comparison, configuration comparison, backup digest and age, reconciliation of releases against returns, and matching privileged events to approved changes. She chooses these because they are frequent, rule-based and read-only. She does not automate actions such as pausing or changing settings, because those need human judgement and approval. Automation is most valuable for checks that people would otherwise skip when busy, and least appropriate for decisions that carry real risk if made wrongly.

### 14.2 Scheduling and reporting

Each check runs on a schedule on the monitoring server and writes results to a dated log. A morning summary email lists anything needing attention, with links to details. Urgent findings, such as an unapproved role change, send an immediate alert to the duty technician. Aiko names who reads the summary each day. She tests each scheduled check with seeded problems in the test environment before relying on it. Mr Kowal warns that automated reports nobody reads are worse than none, because they create false confidence.

### 14.3 Keeping people in control

All automated checks are read-only. When a check finds a problem, a person decides what to do and makes changes through the change process. Aiko documents each check's purpose, inputs, schedule and owner, and keeps the scripts in version control with peer review. She also adds a heartbeat: if a check does not run, an alert is sent. This prevents silent failure of the automation itself. People remain responsible for decisions, while automation ensures that the information they need arrives reliably and on time.

### Worked example

Aiko automates five read-only checks with a morning summary, immediate alerts for unapproved role changes and a heartbeat for missed runs.

> **Synthetic case.** The automation is synthetic.

### Errors and limits

Automating risky actions like pausing removes the human judgement they require.

### Exercises

- **EX053 — Automation criteria.** Why were these checks chosen for automation? *Rubric:* 3 = frequent, rule-based and read-only;; 2 = routine;; 1 = random;; 0 = none.
- **EX054 — Not automated.** Which actions are not automated? *Rubric:* 3 = pausing or changing settings;; 2 = risky actions;; 1 = reporting;; 0 = none.
- **EX055 — Urgent alert example.** What sends an immediate alert? *Rubric:* 3 = an unapproved role change;; 2 = role change;; 1 = normal transfers;; 0 = none.
- **EX056 — Heartbeat purpose.** What does the heartbeat detect? *Rubric:* 3 = a check that fails to run;; 2 = silent automation failure;; 1 = slow blocks;; 0 = none.

### Synthesis

Read-only automation with named readers and heartbeats supports human decisions.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Web3, blockchain and cryptoasset security: integration and dependencies

### Learning outcomes

You will (1) document integrations with other systems; (2) track dependencies and versions; (3) plan for dependency changes.

### 15.1 Documenting integrations

The deposit system connects to the reservation application, the borrower database, an email service for reminders and the library's accounting software. Aiko documents each integration: what data flows, in which direction, which credentials are used and what happens if it fails. She finds the accounting export reads balances directly from a node every night, adding load at the same time as backups. She proposes moving the export an hour later. Documented integrations make the effects of changes predictable and reveal conflicts that would otherwise remain hidden.

### 15.2 Tracking dependencies

Aiko lists dependencies with versions: the ledger client, the operating system, Python, libraries used by the deposit service, the compiler version used for the contract and the hardware wallet firmware. For each she records the owner, how updates are announced and when it was last updated. The SWC registry includes weaknesses linked to outdated compilers, and similar risks apply to other dependencies. A dependency list turns vague worries about outdated software into specific items with owners, dates and an update plan everyone can follow.

### 15.3 Planning for changes

Dependencies change: a library releases a security fix, the cloud provider changes a setting, or the wallet firmware needs an update. Aiko writes a simple plan: check announcements monthly, test updates on the test ledger, apply them through change tickets one component at a time and confirm checks pass afterwards. For urgent fixes, a faster path requires the manager's approval. She also lists what to do if a dependency is withdrawn. Planning turns dependency changes into routine work rather than emergencies that disrupt borrowers.

### Worked example

Aiko documents four integrations, moves the nightly accounting export after backups and tracks six dependency types with owners and update dates.

> **Synthetic case.** The integrations and dependencies are synthetic; the SWC registry is a real source.

### Errors and limits

Untracked dependencies become outdated unnoticed until a problem forces an urgent update.

### Exercises

- **EX057 — Load conflict.** What conflict did Aiko find? *Rubric:* 3 = accounting export reading nodes during backups;; 2 = export timing;; 1 = vague;; 0 = none.
- **EX058 — Dependency example.** Name one tracked dependency. *Rubric:* 3 = hardware wallet firmware;; 2 = ledger client;; 1 = office chairs;; 0 = none.
- **EX059 — Update path.** How are routine updates applied? *Rubric:* 3 = tested, then one component at a time through tickets;; 2 = tested and staged;; 1 = all at once;; 0 = none.
- **EX060 — Urgent fix path.** What does the urgent path require? *Rubric:* 3 = the manager's approval;; 2 = approval;; 1 = vague;; 0 = none.

### Synthesis

Documented integrations and tracked dependencies make change predictable.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write clear technical documents; (2) include safety and scope limits; (3) keep documents current.

### 16.1 Writing clearly

Aiko writes documents for different readers: runbooks for technicians, a short overview for the manager and a one-page guide for counter staff. Each starts with its purpose and audience. Runbooks use numbered steps with expected results. She avoids jargon or explains it once. Mr Kowal reviews her drafts and asks her to test each runbook by having another trainee follow it. Two steps confuse the trainee and she rewrites them. Clear documentation lets the library operate safely when Aiko is not there, which is the real test of any technical work.

### 16.2 Safety and scope limits

Each document states what it covers and what it does not. Runbooks warn where a step could affect live borrowers and say when to stop and escalate. For example, the node restart runbook says never to restart two nodes at once and to escalate if the remaining nodes are not healthy. Documents describe defensive tasks only and contain no instructions that could be used to misuse the system. Including limits protects people who follow the documents under pressure, when it is easy to go further than intended.

### 16.3 Keeping documents current

Documents become outdated when systems change. Aiko adds a review date and owner to each, and links documents to change tickets so that a change prompts a review of affected documents. After the deposit service update she finds two runbooks referring to an old command and updates them. She keeps a change history at the end of each document. Mr Kowal explains that an out-of-date runbook can be more dangerous than none, because people trust it and follow wrong steps confidently.

### Worked example

Aiko's runbooks are tested by another trainee, warn never to restart two nodes at once and are linked to change tickets for review.

> **Synthetic case.** The documents are synthetic.

### Errors and limits

Out-of-date runbooks are trusted and followed even when their steps are wrong.

### Exercises

- **EX061 — Runbook test.** How are runbooks tested? *Rubric:* 3 = another trainee follows them;; 2 = peer follows;; 1 = not tested;; 0 = none.
- **EX062 — Restart warning.** What does the restart runbook warn? *Rubric:* 3 = never restart two nodes at once;; 2 = one at a time;; 1 = restart all;; 0 = none.
- **EX063 — Review trigger.** What prompts a document review? *Rubric:* 3 = a linked change ticket;; 2 = system change;; 1 = vague;; 0 = none.
- **EX064 — Outdated danger.** Why can outdated runbooks be dangerous? *Rubric:* 3 = people trust and follow wrong steps;; 2 = false trust;; 1 = they are not;; 0 = none.

### Synthesis

Clear, limited and current documentation lets others operate a system safely.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) build a transfer-rate baseline; (2) flag unusual hours; (3) investigate an alert calmly.

### 17.1 Why baselines help

Many problems show up as unusual activity: a stuck service retrying transfers, a mistaken batch or misuse of an account. To recognise unusual activity, Aiko first measures normal activity. She takes ten hours of synthetic transfer counts from a normal week as a baseline, computes the mean and standard deviation, and sets an alert limit at the mean plus three standard deviations. Then she checks a new day's hourly counts against the limit. The lab is read-only and uses only Python's standard library and synthetic data.

### Lab — Transfer rate against a baseline

```python
"""Flag hours whose transfer count is far above a baseline (synthetic, read-only)."""
import statistics

BASELINE = [12, 15, 11, 14, 13, 16, 12, 14, 15, 13]   # transfers per hour, normal week sample
TODAY = {9: 14, 10: 17, 11: 13, 12: 41, 13: 15, 14: 12}

def main():
    mean = statistics.mean(BASELINE)
    sd = statistics.stdev(BASELINE)
    limit = mean + 3 * sd
    print(f"baseline mean {mean:.1f}; sd {sd:.2f}; limit {limit:.1f}")
    for hour, n in TODAY.items():
        if n > limit:
            print(f"hour {hour}: {n} transfers above limit")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_rate.py`. Verified output:

```text
baseline mean 13.5; sd 1.58; limit 18.2
hour 12: 41 transfers above limit
```

### 17.2 Reading the result

The baseline mean is 13.5 transfers per hour with a standard deviation of 1.58, giving a limit of 18.2. Hours 9, 10, 11, 13 and 14 are within normal range, but hour 12 shows 41 transfers, far above the limit. Aiko does not assume misuse. She checks the deposit service logs and finds that at noon a community repair event returned 27 tools at once, each releasing a deposit. The spike is real but legitimate. She records the alert, the explanation and the evidence in the monitoring log. Writing the explanation down lets the next technician recognise a similar event quickly instead of escalating it from scratch.

### 17.3 Improving the alert

Aiko notes that simple statistical limits cannot know about planned events. She adds a calendar of community events to the monitoring notes, so duty technicians can check it first, and suggests that the library tells technicians in advance about large return days. She keeps the limit unchanged, because it caught a genuine spike and would catch an unplanned one too. Mr Kowal praises her for investigating before acting and for improving context rather than weakening the alert to avoid one explained false alarm.

### Worked example

The rate lab sets a limit of 18.2 from a 13.5 mean and flags 41 transfers at hour 12, explained by a repair event returning 27 tools.

> **Synthetic case.** The counts and event are synthetic.

### Errors and limits

Raising an alert limit to silence one explained spike weakens detection of unplanned ones.

### Exercises

- **EX065 — Baseline values.** What are the baseline mean and limit? *Rubric:* 3 = mean 13.5, limit 18.2;; 2 = 13.5/18.2;; 1 = 41;; 0 = none.
- **EX066 — Flagged hour.** Which hour is flagged and with how many transfers? *Rubric:* 3 = hour 12 with 41;; 2 = hour 12;; 1 = hour 9;; 0 = none.
- **EX067 — Spike explanation.** What explained the spike? *Rubric:* 3 = a repair event returning 27 tools;; 2 = repair event;; 1 = misuse;; 0 = none.
- **EX068 — Alert improvement.** How is the alert improved? *Rubric:* 3 = adding an events calendar for context;; 2 = context;; 1 = raising the limit;; 0 = none.

### Synthesis

Baselines detect unusual activity, and context explains it without weakening alerts.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) plan and deliver a supervised improvement; (2) test and hand it over; (3) reflect on the course.

### 18.1 Planning the project

For her final project Aiko proposes a release reconciliation service: every fifteen minutes it compares tools marked returned in the database with deposit releases on the ledger and alerts if a return has no release after twenty minutes, or a release has no matching return. Objectives are to detect all seeded mismatches, keep false alarms below one a week and halve the time staff spend checking releases by hand. The scope is read-only. Mr Kowal approves the plan and agrees weekly progress meetings.

### 18.2 Testing and handing over

Aiko builds the service with the standard library and tests it with synthetic data containing a return without a release, a release without a return and a duplicate release. It detects all three. On two weeks of synthetic normal data it raises one false alarm, from a return entered twice at the counter; she adds a duplicate check on returns. Staff checking time falls from about an hour to twenty-five minutes a week. She writes an operator guide, trains two staff and hands the service over with a scheduled review.

### 18.3 Reflecting on the course

Aiko reflects on eighteen months: the most useful skills were careful scoping, reading telemetry, methodical troubleshooting and clear documentation. She notes that several problems she met looked technical but had process causes, like signer rosters. She also notes the value of saying what she did not check. Mr Kowal's final assessment praises her evidence-based work and her respect for scope. The library keeps her service in use, and Aiko continues as a part-time technician while preparing for further study in the following year.

### Worked example

Aiko's read-only release reconciliation detects all three seeded mismatches, gains a duplicate-return check and cuts staff checking from about an hour to twenty-five minutes weekly.

> **Synthetic case.** The project, results and reflection are synthetic.

### Errors and limits

Handing over a service without trained operators leaves it unused when its builder leaves.

### Exercises

- **EX069 — Release alert rule.** When does the service alert for a return? *Rubric:* 3 = no release after twenty minutes;; 2 = twenty minutes;; 1 = immediately;; 0 = none.
- **EX070 — Seeded detection.** How many seeded mismatches were detected? *Rubric:* 3 = all three;; 2 = three;; 1 = one;; 0 = none.
- **EX071 — False alarm fix.** What fixed the false alarm? *Rubric:* 3 = a duplicate check on returns;; 2 = duplicate check;; 1 = raising limits;; 0 = none.
- **EX072 — Time saved.** How did weekly checking time change? *Rubric:* 3 = from about an hour to twenty-five minutes;; 2 = about halved;; 1 = unchanged;; 0 = none.

### Synthesis

A supervised, tested and handed-over improvement completes a technical course well.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Aiko Brennan, Mr Tomasz Kowal, Northfield Technical Institute, Greenway Tool Library and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About 600 borrowers.

**EX002.** Borrowers pay a deposit token for a tool and get it back on return.

**EX003.** The ledger keeps running with two of the three nodes.

**EX004.** A second application server or a documented manual fallback for deposits.

**EX005.** The port and protocol of each connection.

**EX006.** Node three's programming interface accepted connections from the whole office network.

**EX007.** Tests only from authorised machines within the scope approved in writing.

**EX008.** Because unverified changes often cause outages or false confidence.

**EX009.** So every administrative action is recorded against a person.

**EX010.** In the server's protected secret store.

**EX011.** An account for a contractor whose work ended three months earlier.

**EX012.** Quarterly.

**EX013.** Store settings such as node addresses in one place.

**EX014.** Numbers arriving as text or dates in different formats.

**EX015.** Positive whole amounts, increasing blocks, valid dates or existing borrower codes.

**EX016.** Two loan records with return dates before borrow dates.

**EX017.** Borrowers' devices, the cloud provider's infrastructure or public blockchains.

**EX018.** By storing a SHA-256 hash of each exported file.

**EX019.** Another technician can repeat the steps and reach the same result.

**EX020.** They are recorded with their corrections rather than hidden.

**EX021.** Only when the database shows the tool has been returned.

**EX022.** The total of all balances equals tokens issued minus tokens redeemed.

**EX023.** Only the library's 2-of-3 staff multisig.

**EX024.** Two staff members together.

**EX025.** Node metrics, ledger events, application logs or server logs.

**EX026.** Every minute, with events exported hourly.

**EX027.** Ninety days, with summaries for two years.

**EX028.** By writing daily hashes of the logs.

**EX029.** Returns recorded in the database without matching releases on the ledger.

**EX030.** So whoever sees a symptom knows where to look first.

**EX031.** An unexpected role change.

**EX032.** After six months of telemetry provide better evidence.

**EX033.** A compromised utility on a signer's computer could misrepresent a transaction.

**EX034.** Confirm scope, collect, compare, record, confirm manually or report.

**EX035.** The peer port, expected and limited to the other nodes.

**EX036.** Tool output is a starting point needing interpretation, since tools disagree and miss issues.

**EX037.** Only the deposit service.

**EX038.** It cannot issue tokens.

**EX039.** Node one kept logs for thirty days instead of ninety.

**EX040.** Weekly and after every maintenance.

**EX041.** Single-signature issuing, unreturned release, timelock wait, outside access or shared login.

**EX042.** They are clearly labelled and kept separate from live keys.

**EX043.** The release test for a loan not yet returned.

**EX044.** The test database marked all loans returned by default.

**EX045.** 24 hours.

**EX046.** Node2 has a digest mismatch and node3 is 52 hours old.

**EX047.** Its backup job had failed silently since a disk path changed.

**EX048.** A successful test restore.

**EX049.** Some released deposits take over ten minutes, mostly in the afternoon.

**EX050.** Slow node, stalled queue, database locking or slow signer approvals.

**EX051.** Large releases needed two signers but only one was on duty.

**EX052.** It was reviewed and kept, since it protects larger deposits.

**EX053.** They are frequent, rule-based and read-only.

**EX054.** Actions such as pausing or changing settings.

**EX055.** An unapproved role change.

**EX056.** When a scheduled check does not run.

**EX057.** The nightly accounting export added node load at the same time as backups.

**EX058.** Ledger client, operating system, Python, libraries, compiler or wallet firmware.

**EX059.** Tested on the test ledger, then applied one component at a time through change tickets.

**EX060.** The manager's approval.

**EX061.** By having another trainee follow each one.

**EX062.** Never restart two nodes at once, and escalate if the others are unhealthy.

**EX063.** A change ticket affecting the documented system.

**EX064.** People trust them and follow wrong steps confidently.

**EX065.** A mean of 13.5 transfers per hour and a limit of 18.2.

**EX066.** Hour 12, with 41 transfers.

**EX067.** A community repair event returned 27 tools at once.

**EX068.** By adding a community events calendar for duty technicians, keeping the limit.

**EX069.** When a returned tool has no matching release after twenty minutes.

**EX070.** All three seeded mismatches.

**EX071.** Adding a duplicate check on returns entered twice.

**EX072.** From about an hour to twenty-five minutes a week.

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
