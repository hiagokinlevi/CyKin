# Web3, Blockchain and Cryptoasset Security: Bachelor's Degree

- Language: English (`en`); course 101, Bachelor's degree (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; Three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: undergraduate students learning blockchain and smart-contract security from foundations to a supervised capstone.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only contracts, wallets and systems you are authorised to assess, on local simulations or test networks; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic ledgers, transactions, contract inventories and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one undergraduate helping a food cooperative run a voucher token on a permissioned ledger, from mathematics, computing, programming and writing, through identity, privacy, architecture and cryptography, to models, controls, verification, operations, research, a monitoring capstone and thesis. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Sofia Lindqvist** | Undergraduate student | Invented |
| **Dr Kwame Asante** | Supervisor | Invented |
| **Harrowgate University** | Fictional university | Invented |
| **Lantern Hill Food Cooperative** | Fictional client (about 900 members) | Invented |

### Core sources

Nakamoto, [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf); Wood, [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf); NIST [IR 8202](https://doi.org/10.6028/NIST.IR.8202); [SWC registry](https://swcregistry.io/); [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/); EEA [EthTrust Security Levels v3](https://entethalliance.org/specs/ethtrust-sl/v3/); [ConsenSys smart contract best practices](https://consensys.github.io/smart-contract-best-practices/); Atzei et al. ([2017](https://doi.org/10.1007/978-3-662-54455-6_8)); Luu et al. ([2016](https://doi.org/10.1145/2976749.2978309)). Full list in [References](#references).

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

You will (1) reason with definitions and implications; (2) check claims with counterexamples; (3) express token rules precisely.

### 1.1 The case and why reasoning matters

Sofia Lindqvist is a first-year student at the fictional Harrowgate University, supervised by Dr Kwame Asante. Across four years she will help the fictional Lantern Hill Food Cooperative, about 900 members, run a voucher token on a small permissioned Ethereum-compatible test ledger. Members earn vouchers for volunteer shifts and spend them at the cooperative shop. Every person, address and number in this book is synthetic. Mathematical reasoning comes first because security claims about tokens are claims about rules, and a rule stated loosely cannot be checked. Sofia learns to write each rule so that anyone can test whether it holds.

### 1.2 Definitions and implications

A definition fixes exactly what a word means; an implication says that if one statement holds, another must follow. Sofia writes the cooperative's first rule as an implication: if a voucher is issued, then a recorded volunteer shift exists for that member. She notes the converse is a different claim: a shift does not guarantee a voucher, because a coordinator may not yet have approved it. Confusing a statement with its converse is a common reasoning error in security reviews. Writing both directions separately shows which one the system must enforce and which one is merely usual practice in the shop.

### 1.3 Counterexamples

To show a general claim is false, one counterexample is enough. A classmate claims that total vouchers in circulation can never decrease. Sofia finds a counterexample at once: when a member spends vouchers at the shop, they are redeemed and removed, so circulation falls. The corrected claim is that circulation equals vouchers issued minus vouchers redeemed. Searching for counterexamples is a habit that security work depends on, because attackers and accidents both find the cases that designers forgot. Sofia keeps a page in her notebook for each rule, listing the counterexamples she tried and whether any of them broke it.

### Worked example

Sofia states issuance as an implication from recorded shifts, separates it from its converse, and corrects a classmate's claim with one redemption counterexample.

> **Synthetic case.** Sofia Lindqvist, Dr Kwame Asante, Harrowgate University, Lantern Hill Food Cooperative and all data are synthetic.

### Errors and limits

Treating a rule and its converse as the same claim leads to controls that enforce the wrong direction.

### Exercises

- **EX001 — Cooperative scale.** How many members does Lantern Hill have? *Rubric:* 3 = about 900;; 2 = 900;; 1 = 9,000;; 0 = none.
- **EX002 — Converse error.** Why is the converse of the issuance rule a different claim? *Rubric:* 3 = a shift may exist before a coordinator approves a voucher;; 2 = not automatic;; 1 = same claim;; 0 = none.
- **EX003 — Corrected circulation claim.** What corrected claim replaces "circulation never decreases"? *Rubric:* 3 = circulation equals issued minus redeemed;; 2 = redemptions reduce it;; 1 = never decreases;; 0 = none.

### Synthesis

Precise definitions and counterexamples turn vague token rules into claims that can be checked.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe processors, memory and storage; (2) explain how a node runs; (3) relate system limits to ledger behaviour.

### 2.1 Processors, memory and storage

A computer executes instructions on a processor, keeps working data in fast memory that is lost on power failure, and keeps durable data on storage such as solid-state drives. Sofia learns these parts because a blockchain node is simply a program on such a computer. The node keeps recent state in memory for speed and writes blocks to storage so they survive restarts. If storage fills up, the node stops accepting new blocks. If memory is too small, it slows down. Understanding the hardware helps her explain later why a node falls behind or refuses to start at the cooperative.

### 2.2 How a ledger node runs

A ledger node receives transactions and blocks over the network, checks them against the rules, executes contract code in a virtual machine, and stores the result. The Ethereum Virtual Machine, described in Wood's yellow paper, gives every node the same deterministic result for the same inputs, which is why nodes can agree. Sofia sketches the node as a pipeline: receive, validate, execute, store, share. Each stage consumes processor time, memory or disk. She notes that the cooperative's test ledger runs three validator nodes on small rented servers, so resource limits matter more than they would in a large data centre.

### 2.3 Limits and behaviour

Sofia lists what happens when each resource runs short. A busy processor delays validation, so blocks arrive late. Exhausted memory causes swapping and crashes. A full disk stops the node entirely. Clock drift between servers can confuse logs and timestamps. She proposes simple monitoring for disk use, memory and clock offset on each validator, with alerts well before limits are reached. Dr Asante points out that availability is a security property: if vouchers cannot be spent because nodes are down, members lose trust in the system just as surely as they would after a theft.

### Worked example

Sofia maps a validator node as receive, validate, execute, store, share and sets alerts for disk, memory and clock offset on all three servers.

> **Synthetic case.** The cooperative's servers and ledger are synthetic; Wood's yellow paper is a real source.

### Errors and limits

Ignoring disk and clock limits leaves outages that look like software bugs.

### Exercises

- **EX004 — Validator count.** How many validator nodes does the test ledger run? *Rubric:* 3 = three;; 2 = 3;; 1 = one;; 0 = none.
- **EX005 — Determinism source.** Why can nodes agree on contract results? *Rubric:* 3 = the EVM gives the same deterministic result for the same inputs;; 2 = determinism;; 1 = luck;; 0 = none.
- **EX006 — Availability link.** Why is availability treated as security here? *Rubric:* 3 = members lose trust if vouchers cannot be spent;; 2 = outages harm;; 1 = unrelated;; 0 = none.

### Synthesis

Knowing the computer under a node explains many ledger failures before they happen.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write small programs with variables, conditions and loops; (2) test functions with examples; (3) handle invalid input safely.

### 3.1 Variables, conditions and loops

Sofia's first programs use Python's standard library only. She stores a member's voucher balance in a variable, uses a condition to decide whether a purchase is allowed, and uses a loop to apply a list of purchases in order. The program refuses any purchase larger than the balance and prints a clear message. Writing the rule in code forces her to decide what happens at the edge: a purchase exactly equal to the balance is allowed, leaving zero. Edge cases like this are where token software most often goes wrong, so she writes them down explicitly before coding anything else.

### 3.2 Testing with examples

Dr Asante asks the class to write tests before trusting any function. Sofia writes small assertions: a balance of 25 minus a purchase of 10 leaves 15; a purchase of 30 from 25 is refused; a purchase of zero is refused because it records nothing useful. She also tests a negative amount, which must be refused, since accepting it would silently increase a balance. Each test states one expected behaviour. When she later changes the function, rerunning the tests shows at once whether she broke a rule. Tests are cheap evidence that code does what its author believes it does.

### 3.3 Handling invalid input

Programs receive input they did not expect: text where a number should be, blank fields, or values far outside any normal range. Sofia's purchase function checks the type and range of every amount before using it and returns a clear error rather than crashing. She learns the principle of failing safely: when input is doubtful, the program should refuse the action and explain why, not guess. Smart contracts follow the same principle with require checks that revert a transaction. The ConsenSys smart contract best practices describe validating inputs early as a basic habit, and Sofia adopts it from her first week.

### Worked example

Sofia's purchase function refuses amounts above the balance, zero and negatives, with four assertions proving each rule.

> **Synthetic case.** Sofia's programs and balances are synthetic; ConsenSys best practices is a real source.

### Errors and limits

Accepting a negative amount can silently increase a balance instead of reducing it.

### Exercises

- **EX007 — Exact-balance purchase.** What happens when a purchase equals the balance? *Rubric:* 3 = allowed, leaving zero;; 2 = allowed;; 1 = refused;; 0 = none.
- **EX008 — Negative amount risk.** Why must a negative purchase be refused? *Rubric:* 3 = it would silently increase the balance;; 2 = wrong direction;; 1 = harmless;; 0 = none.
- **EX009 — Failing safely.** What does failing safely mean for doubtful input? *Rubric:* 3 = refuse the action and explain why;; 2 = refuse;; 1 = guess;; 0 = none.

### Synthesis

Small programs with explicit edge cases and tests build habits that secure token code needs.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) structure an argument; (2) cite sources accurately; (3) write clearly for mixed audiences.

### 4.1 Structuring an argument

Sofia's first essay asks whether a small cooperative should use a blockchain for vouchers at all. Dr Asante teaches a simple structure: state the claim, give reasons, support each reason with evidence, address the strongest objection, and conclude. Her claim is cautious: a permissioned ledger may help if members want shared, tamper-evident records, but a normal database might be enough. She lists reasons on both sides before writing a word. Structure keeps an argument honest, because a missing objection becomes visible as an empty section, and readers can see exactly which evidence supports each step of the reasoning.

### 4.2 Citing sources accurately

Sofia cites Nakamoto's 2008 paper for the idea of a public, append-only chain of blocks and NIST IR 8202 for an overview of blockchain types and their trade-offs. She records author, title, year and where the source can be found, and she checks each citation against the original rather than a summary. Dr Asante warns that inaccurate citations are a form of error that readers cannot easily detect. In security writing, a wrong citation can lead someone to rely on a claim no source actually makes. Accurate citation is therefore part of being trustworthy, not just a formatting rule.

### 4.3 Writing for mixed audiences

The cooperative's board includes a baker, a retired teacher and a nurse, none of them technical. Sofia rewrites her essay's summary in plain language: what the voucher system does, what could go wrong, and what decision the board needs to make. She replaces jargon with short explanations, such as calling a private key the secret that proves who may spend vouchers. Each technical term she keeps is defined once. The board's questions after reading show that they understood the trade-off. Writing for the people who decide is a security skill, because unclear advice leads to poor decisions.

### Worked example

Sofia argues cautiously for a permissioned ledger, cites Nakamoto and NIST IR 8202 from the originals, and writes a plain summary the board understands.

> **Synthetic case.** The essay and board are synthetic; Nakamoto (2008) and NIST IR 8202 are real sources.

### Errors and limits

Citing a summary instead of the original source risks repeating claims the source never made.

### Exercises

- **EX010 — Essay claim.** What is Sofia's cautious claim? *Rubric:* 3 = a ledger may help if members want shared tamper-evident records;; 2 = maybe;; 1 = always use blockchain;; 0 = none.
- **EX011 — Sources used.** Which two sources does she cite? *Rubric:* 3 = Nakamoto 2008 and NIST IR 8202;; 2 = one of them;; 1 = a blog;; 0 = none.
- **EX012 — Plain term.** How does she explain a private key to the board? *Rubric:* 3 = the secret that proves who may spend vouchers;; 2 = a secret;; 1 = a password reset;; 0 = none.

### Synthesis

Clear structure, accurate citation and plain language make security advice usable.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain confidentiality, integrity and availability; (2) identify assets and threats; (3) describe basic controls.

### 5.1 Confidentiality, integrity and availability

Security is often summarised as protecting confidentiality, integrity and availability. For Lantern Hill, confidentiality means members' names and shift histories stay private; integrity means voucher balances are correct and cannot be changed without authority; availability means members can spend vouchers when the shop is open. Sofia notices that a blockchain mainly strengthens integrity, by making records hard to alter, while it can weaken confidentiality, because every node holds a copy of the records. This trade-off shapes the whole design. She decides early that names will never be stored on the ledger, only pseudonymous member codes.

### 5.2 Assets and threats

Sofia lists the cooperative's assets: the vouchers themselves, the private keys that control the treasury and minting, the member list, and the reputation of the cooperative. For each asset she asks who might harm it and how, in general terms. A lost key could stop minting; a stolen key could create vouchers without shifts; a careless export could leak the member list; a long outage could damage trust. She avoids technical attack detail and focuses on outcomes. The list becomes the starting point for every later chapter, and she updates it whenever the design changes or new risks become visible.

### 5.3 Basic controls

Controls reduce risk. Sofia groups them as preventive, which stop harm, detective, which notice it, and corrective, which recover from it. For the treasury, a multi-signature wallet requiring two of three keyholders is preventive. A daily comparison of vouchers issued with approved shifts is detective. A tested backup of keyholder recovery material is corrective. She learns that no single control is enough, because every control can fail. Layering them means one failure is caught by another. The cooperative already uses similar layers for its cash box: two people count the takings, and a bookkeeper checks them weekly.

### Worked example

Sofia keeps names off the ledger, lists four assets and pairs the treasury with a 2-of-3 multisig, a daily shift comparison and tested recovery.

> **Synthetic case.** The cooperative's assets and controls are synthetic.

### Errors and limits

Assuming a blockchain improves every security property ignores its cost to confidentiality.

### Exercises

- **EX013 — Ledger trade-off.** Which property does a shared ledger tend to weaken? *Rubric:* 3 = confidentiality, because every node holds a copy;; 2 = confidentiality;; 1 = availability only;; 0 = none.
- **EX014 — Asset list.** Name one asset Sofia lists. *Rubric:* 3 = treasury and minting keys;; 2 = member list;; 1 = the shop's furniture;; 0 = none.
- **EX015 — Control types.** Give one detective control. *Rubric:* 3 = daily comparison of issued vouchers with approved shifts;; 2 = comparison;; 1 = multisig;; 0 = none.

### Synthesis

The CIA properties, an asset list and layered controls form the base of security literacy.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) use sets, relations and graphs; (2) model ownership as a mapping; (3) reason about transfers as a graph.

### 6.1 Sets and relations

A set is a collection of distinct items; a relation pairs items from sets. Sofia models the cooperative's members as a set of codes and its vouchers as amounts owned by those codes. Ownership is a function from member codes to non-negative whole numbers. Writing it this way makes rules precise: no member may have a negative balance, and the sum over all members must equal circulation. A relation records which members have approved shifts in a given week. Discrete structures sound abstract, but they let Sofia state exactly what a correct ledger state looks like and therefore what an incorrect one looks like.

### 6.2 Transfers as a graph

A graph has nodes connected by edges. Sofia draws members as nodes and voucher transfers as directed edges labelled with amounts. Most edges run from members to the shop, because vouchers are mostly spent there. A few run between members, for example when a parent gives vouchers to an adult child. The graph shows patterns at a glance: a member who sends vouchers to many new addresses in a short time stands out. Graph thinking underlies many blockchain monitoring tools. Sofia treats unusual shapes as questions to investigate politely, never as proof of wrongdoing.

### 6.3 Counting and bounds

Counting arguments give simple limits. With 900 members and a rule that each member can earn at most 20 vouchers a week, weekly issuance can never exceed 18,000. If records ever show more, something is wrong. Sofia also counts the possible keyholder combinations for a 2-of-3 treasury: three pairs can sign, so losing one keyholder still leaves one working pair. Small counting results like these become checks that software can run automatically. They are easy to explain to the board, which helps the controls earn trust and support from people who are not technical.

### Worked example

Sofia models balances as a non-negative function, bounds weekly issuance at 18,000 and shows a 2-of-3 treasury has three signing pairs.

> **Synthetic case.** Members, transfers and limits are synthetic.

### Errors and limits

Treating an unusual graph pattern as proof of misuse can wrongly accuse a member.

### Exercises

- **EX016 — Ownership model.** How is ownership modelled? *Rubric:* 3 = a function from member codes to non-negative whole numbers;; 2 = a function;; 1 = a list of names;; 0 = none.
- **EX017 — Weekly bound.** What is the maximum weekly issuance? *Rubric:* 3 = 18,000;; 2 = 900 times 20;; 1 = unlimited;; 0 = none.
- **EX018 — Signing pairs.** How many pairs can sign a 2-of-3 treasury? *Rubric:* 3 = three;; 2 = 3;; 1 = one;; 0 = none.

### Synthesis

Sets, graphs and counting turn ledger rules into precise, checkable bounds.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain layered networking; (2) describe peer-to-peer gossip; (3) secure node communication.

### 7.1 Layered networking

Networks are organised in layers. The physical and link layers move bits between nearby devices; the internet layer routes packets between networks; the transport layer provides reliable streams; the application layer carries meaning, such as blocks and transactions. Sofia learns the layers so she can locate a problem: a node that cannot reach peers may have a firewall issue at the transport layer rather than a ledger bug. She draws the cooperative's three validators in different rented data centres, connected over the public internet, and marks which ports each must open to its peers and to the shop's point-of-sale terminal.

### 7.2 Peer-to-peer gossip

Blockchain nodes usually share transactions and blocks by gossip: each node tells its peers about new data, and they tell theirs. Nakamoto's paper describes broadcasting new transactions and blocks to all nodes. Gossip is resilient, because there is no single server to fail, but it means a node is only as informed as its peers. A validator connected to too few peers may fall behind. Sofia configures each validator to connect directly to the other two and to refuse unknown peers, because the ledger is permissioned. That small allow-list removes a whole class of problems that open networks must handle in other ways.

### 7.3 Securing node communication

Even on a permissioned ledger, traffic crosses the public internet. Sofia recommends encrypted, authenticated connections between validators, so that data cannot be read or altered in transit, and a firewall that allows only the known peers and the shop terminal. Administrative access uses separate keys and is restricted to two named volunteers. She also asks the hosting provider how network logs are kept. The design follows NIST IR 8202's observation that permissioned networks rely on access control rather than open participation. Network security protects the ledger before any contract code runs.

### Worked example

Sofia restricts validators to a three-node peer allow-list, encrypts and authenticates links, and limits administration to two named volunteers.

> **Synthetic case.** The network design is synthetic; Nakamoto (2008) and NIST IR 8202 are real sources.

### Errors and limits

Exposing a permissioned validator to unknown peers removes the main advantage of being permissioned.

### Exercises

- **EX019 — Fault location.** Why learn the layers? *Rubric:* 3 = to locate problems such as a firewall at the transport layer;; 2 = locate faults;; 1 = to memorise names;; 0 = none.
- **EX020 — Gossip weakness.** What is a weakness of gossip for one node? *Rubric:* 3 = it is only as informed as its peers;; 2 = few peers;; 1 = vague;; 0 = none.
- **EX021 — Peer policy.** What peer policy does Sofia configure? *Rubric:* 3 = connect to the other two and refuse unknown peers;; 2 = allow-list;; 1 = accept all;; 0 = none.

### Synthesis

Layered networking knowledge and restricted, encrypted peering protect a permissioned ledger.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) organise code into functions and modules; (2) use data structures; (3) review code for clarity and safety.

### 8.1 Functions and modules

As programs grow, Sofia splits them into small functions, each doing one job: one parses a purchase record, one checks it, one applies it. Functions are grouped into modules by purpose. This makes code easier to read, test and review. A reviewer can check the checking function alone and be confident the rule is enforced in one place. Smart contracts benefit from the same discipline, because a rule scattered across many functions is easy to miss in one of them. Dr Asante notes that most contract weaknesses in the SWC registry arise from logic that is unclear rather than from exotic tricks.

### 8.2 Data structures

Sofia uses dictionaries to map member codes to balances, lists to keep transfers in order, and sets to track which shifts have already been rewarded. The set is important: before issuing a voucher she checks the shift is not already in the set, so the same shift cannot be rewarded twice. Choosing the right structure makes the rule simple. She compares this with a smart contract, where a mapping from shift identifiers to a boolean serves the same purpose. Duplicate reward is one of the simplest and most common ways that token systems drift from their intended totals.

### 8.3 Reviewing for clarity and safety

Sofia and a classmate swap code for review. They use a short checklist: are inputs validated, are edge cases tested, are names clear, does each function do one thing, and could the same action happen twice. Her classmate finds that Sofia's function rounds voucher amounts silently when given decimals. They agree it should refuse decimals instead. Review is a conversation, not a judgement, and both learn from it. The ConsenSys best practices encourage peer review before deployment. Sofia records each finding and its fix, building a habit of documenting decisions that she will keep throughout the degree.

### Worked example

Sofia prevents double rewards with a set of rewarded shifts, and peer review changes silent rounding of decimals into refusal.

> **Synthetic case.** The code and review are synthetic; the SWC registry and ConsenSys best practices are real sources.

### Errors and limits

Silently rounding amounts hides input errors that should be refused and reported.

### Exercises

- **EX022 — Double reward guard.** What prevents a shift being rewarded twice? *Rubric:* 3 = a set of rewarded shifts checked before issuing;; 2 = a set;; 1 = nothing;; 0 = none.
- **EX023 — Review finding.** What did the classmate find? *Rubric:* 3 = silent rounding of decimal amounts;; 2 = rounding;; 1 = no tests;; 0 = none.
- **EX024 — Checklist item.** Name one checklist question. *Rubric:* 3 = could the same action happen twice;; 2 = are inputs validated;; 1 = is it fast;; 0 = none.

### Synthesis

Small functions, fitting data structures and peer review make token code safer.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) design tables and keys; (2) query data safely; (3) decide what belongs on-chain and off-chain.

### 9.1 Tables and keys

A relational database stores data in tables with rows and columns, and a primary key uniquely identifies each row. Sofia designs a members table with a code key, a shifts table with a shift key and a member code, and an approvals table recording who approved each shift. Foreign keys link the tables, so a shift cannot refer to a member who does not exist. The database enforces these rules itself. She learns that good data design prevents whole classes of error before any security control is needed, much as a well-designed contract prevents invalid states rather than detecting them afterwards.

### 9.2 Querying safely

Sofia writes queries to list approved shifts per week. She uses parameterised queries, where values are passed separately from the query text, so input can never change the meaning of the query. This prevents a well-known class of injection weakness listed by OWASP. She also limits which accounts may change data: coordinators can approve shifts, while the reporting account can only read. Separating read and write permissions means a mistake or misuse in reporting cannot alter records. These habits apply directly to the off-chain services that sit beside any blockchain system and feed it data.

### 9.3 On-chain or off-chain

Not everything belongs on a ledger. Sofia keeps names, contact details and shift notes in the database, which can be corrected and deleted under privacy law, and puts only voucher balances and transfers on the ledger, linked to pseudonymous codes. A hash of each week's approved shift list is recorded on-chain, so anyone can later check the list was not altered, without revealing its contents. This split, described in NIST IR 8202 as a common pattern, gives integrity where it matters and keeps personal data where it can be managed responsibly by the cooperative.

### Worked example

Sofia links members, shifts and approvals with foreign keys, uses parameterised queries and records only a weekly hash of approvals on-chain.

> **Synthetic case.** The database is synthetic; OWASP and NIST IR 8202 are real sources.

### Errors and limits

Putting personal data on an immutable ledger makes later correction or deletion very difficult.

### Exercises

- **EX025 — Foreign key role.** What does the foreign key prevent? *Rubric:* 3 = a shift referring to a non-existent member;; 2 = orphan rows;; 1 = slow queries;; 0 = none.
- **EX026 — Injection defence.** How does Sofia prevent injection? *Rubric:* 3 = parameterised queries;; 2 = separate values;; 1 = hiding the database;; 0 = none.
- **EX027 — On-chain record.** What is recorded on-chain about shifts? *Rubric:* 3 = a hash of each week's approved shift list;; 2 = a hash;; 1 = names;; 0 = none.

### Synthesis

Careful data design and an on-chain/off-chain split give integrity without exposing personal data.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) apply ethical principles to security work; (2) work only within authorization; (3) handle findings responsibly.

### 10.1 Ethical principles

Security students gain knowledge that could harm people if misused. Sofia's course discusses principles from professional codes: avoid harm, be honest, respect privacy, and act within the law and agreements. Applied to the cooperative, these mean she will not look at member data she does not need, will report problems honestly even if embarrassing, and will never test systems she has not been asked to test. Dr Asante stresses that ethics is practical: it shows up in small daily choices, such as closing a spreadsheet of member names when a visitor enters the room or a screen is shared.

### 10.2 Working within authorization

Before any security work, Sofia obtains written permission from the cooperative's board describing what she may examine, when, and with which data. Her authorization covers the test ledger, synthetic data and read-only access to configuration. It excludes members' devices, the shop's payment terminal and any public blockchain. If she notices something outside scope, she reports it rather than investigating. Written scope protects everyone: the cooperative knows what is happening, and Sofia can show she acted properly. Working outside authorization, even with good intentions, can be unlawful and damages trust that is hard to rebuild.

### 10.3 Handling findings responsibly

When Sofia finds that a test configuration file contains a coordinator's email address, she reports it privately to the board's contact, explains the risk in plain words and suggests removing it. She does not share the finding publicly or with classmates. The board fixes it within a day and thanks her. Responsible handling means reporting to the people who can fix a problem, giving them time, and keeping details confidential. EthTrust and other guidance assume reviewers behave this way. Sofia records the finding, the report date and the fix date in a simple log for the course.

### Worked example

Sofia works under a written scope covering the test ledger and synthetic data, and privately reports an email address found in a configuration file.

> **Synthetic case.** The authorization and finding are synthetic.

### Errors and limits

Investigating systems outside written scope, even helpfully, can be unlawful and erode trust.

### Exercises

- **EX028 — Scope exclusions.** Name one item outside Sofia's scope. *Rubric:* 3 = the shop's payment terminal;; 2 = members' devices;; 1 = the test ledger;; 0 = none.
- **EX029 — Out-of-scope action.** What should she do if she notices something outside scope? *Rubric:* 3 = report it rather than investigate;; 2 = report;; 1 = investigate quietly;; 0 = none.
- **EX030 — Finding handled.** What did Sofia find and report? *Rubric:* 3 = a coordinator's email in a test configuration file;; 2 = an email;; 1 = a stolen key;; 0 = none.

### Synthesis

Ethical principles, written authorization and private reporting make security work trustworthy.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain processes, users and permissions; (2) harden a node host; (3) keep systems patched.

### 11.1 Processes, users and permissions

An operating system runs programs as processes and decides what each may access. Every process runs as a user, and file permissions say which users can read, write or execute each file. Sofia configures the validator software to run as its own unprivileged user that can read its configuration and write only to its data folder. If the node software ever misbehaves, it cannot change system files or read other users' data. This is least privilege at the operating-system level. She checks the permissions on the folder holding the validator key and confirms that only the validator user can read it.

### 11.2 Hardening a node host

Hardening removes what a server does not need. Sofia's checklist for each validator host disables unused services, closes unused ports, requires key-based administrative login, turns off password login, and enables automatic time synchronisation so logs and blocks carry consistent times. She records each setting in a short host profile so the three servers stay identical. Differences between hosts cause confusing faults and hide mistakes. Dr Asante reminds the class that hardening is not a single event; it must be rechecked after updates, because updates sometimes re-enable services or reset configuration files to vendor defaults.

### 11.3 Patching and updates

Software flaws are found continually, and updates fix them. Sofia proposes a monthly patch window for the validator hosts, updating one server at a time so the ledger keeps running on the other two. Before each update she checks the release notes and tests the update on a spare test machine. Urgent security fixes may be applied sooner after the board's contact agrees. She keeps a log of what was updated and when. Patching one node at a time is possible because the ledger tolerates one validator being briefly offline, a property she confirms on the test network first.

### Worked example

Sofia runs the validator as an unprivileged user, hardens hosts from a shared profile and patches one server at a time monthly.

> **Synthetic case.** The hosts and patch plan are synthetic.

### Errors and limits

Updating all validators at once can take the ledger offline if an update fails.

### Exercises

- **EX031 — Validator user.** How does the validator software run? *Rubric:* 3 = as its own unprivileged user;; 2 = unprivileged;; 1 = as administrator;; 0 = none.
- **EX032 — Login setting.** Which administrative login setting does Sofia require? *Rubric:* 3 = key-based login with passwords disabled;; 2 = keys;; 1 = shared password;; 0 = none.
- **EX033 — Patch order.** Why patch one server at a time? *Rubric:* 3 = the ledger keeps running on the other two;; 2 = keeps running;; 1 = faster;; 0 = none.

### Synthesis

Least privilege, hardening and staggered patching keep node hosts dependable.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) describe data with summaries; (2) reason with probability; (3) avoid common statistical mistakes.

### 12.1 Describing data

Sofia receives a synthetic year of weekly voucher issuance. She computes the mean, median and spread, and plots a histogram. Issuance is usually between 4,000 and 7,000 vouchers a week, with a holiday dip and a harvest-season peak. The median is less affected by a few unusual weeks than the mean. Summaries tell her what normal looks like, which is the basis for spotting abnormal behaviour later. She labels every chart with its source, period and units, so that a board member reading it months later can understand exactly what it shows and where the numbers came from.

### 12.2 Reasoning with probability

Probability describes uncertainty. Sofia studies Nakamoto's calculation of the chance that a minority of computing power could catch up with the honest chain after a number of confirmations, which falls quickly as confirmations increase. On the cooperative's permissioned ledger, finality works differently, but the idea of waiting for evidence before trusting a result carries over. She also estimates simple probabilities from data: if two of 52 weeks had a reconciliation mismatch, a rough weekly rate is about 4 percent. She notes that small samples give uncertain estimates, so she reports the counts behind every percentage she writes.

### 12.3 Common mistakes

Sofia lists mistakes she must avoid. Correlation is not causation: weeks with more vouchers are also weeks with more shop sales, but neither causes the other; both follow the harvest. Small samples mislead: two incidents in a year say little about next year. Base rates matter: an alert that fires on 1 percent of normal weeks will produce many false alarms if real problems are rare. She writes each mistake beside an example from the cooperative's data. Dr Asante says that honest statistics are part of security reporting, because exaggerated numbers lead to wasted effort or misplaced reassurance.

### Worked example

Sofia summarises weekly issuance with medians, estimates a mismatch rate of about 4 percent from 2 of 52 weeks and reports the counts.

> **Synthetic case.** Issuance data are synthetic; Nakamoto (2008) is a real source.

### Errors and limits

Reporting a percentage without its counts hides how uncertain a small-sample estimate is.

### Exercises

- **EX034 — Normal range.** What is normal weekly issuance? *Rubric:* 3 = between 4,000 and 7,000;; 2 = 4,000–7,000;; 1 = 18,000;; 0 = none.
- **EX035 — Mismatch estimate.** What rough weekly mismatch rate does she estimate? *Rubric:* 3 = about 4 percent from 2 of 52;; 2 = 4 percent;; 1 = 50 percent;; 0 = none.
- **EX036 — Base-rate warning.** Why do base rates matter for alerts? *Rubric:* 3 = rare problems mean many alerts are false alarms;; 2 = false alarms;; 1 = they do not;; 0 = none.

### Synthesis

Honest summaries and probability reasoning give security reports a sound base.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) distinguish authentication and authorization; (2) manage keys as identities; (3) design roles for the voucher system.

### 13.1 Authentication and authorization

Authentication proves who someone is; authorization decides what they may do. On the cooperative's ledger, a member authenticates by signing a transaction with their private key, and the voucher contract authorises the action by checking rules, such as whether the member has enough vouchers. Off-chain, coordinators log in to the shift database with passwords and a second factor. Sofia notes that a blockchain address is an identity only as strong as the protection of its key. If someone else holds the key, the contract cannot tell the difference, so key protection becomes identity protection in this system.

### 13.2 Keys as identities

Each member's wallet holds a private key. Most members use a simple mobile wallet, and the cooperative offers a custodial option where volunteers hold keys for members who prefer not to manage them. Sofia lists the trade-offs: self-custody gives control but risks loss; custody is convenient but concentrates risk with the cooperative. For the treasury and minting keys she recommends hardware devices held by three different keyholders. She also plans recovery: if a member loses their key, the board can approve reissuing their balance to a new address after checking their identity in person at the shop.

### 13.3 Roles for the voucher system

Sofia designs roles. The minter role can issue vouchers and is held by a 2-of-3 multi-signature wallet. The pauser role can stop transfers in an emergency and requires two keyholders. The administrator role can change roles and is protected by a timelock so changes are visible before they take effect. Members can only transfer and spend their own vouchers. Each role has the smallest set of powers needed. The OWASP Smart Contract Top 10 lists access control failures among the most common contract weaknesses, so she documents each role and reviews the list with Dr Asante.

### Worked example

Sofia assigns minting to a 2-of-3 multisig, pausing to two keyholders and administration behind a timelock, with in-person recovery for lost member keys.

> **Synthetic case.** The roles and wallets are synthetic; the OWASP Smart Contract Top 10 is a real source.

### Errors and limits

Treating a blockchain address as a person ignores that whoever holds the key controls it.

### Exercises

- **EX037 — Authentication on-chain.** How does a member authenticate on the ledger? *Rubric:* 3 = by signing a transaction with their private key;; 2 = signing;; 1 = password;; 0 = none.
- **EX038 — Custody trade-off.** What is the risk of custodial wallets? *Rubric:* 3 = risk concentrates with the cooperative;; 2 = concentration;; 1 = vague;; 0 = none.
- **EX039 — Administrator safeguard.** What protects the administrator role? *Rubric:* 3 = a timelock that makes changes visible first;; 2 = timelock;; 1 = nothing;; 0 = none.

### Synthesis

Clear authentication, careful custody and least-privilege roles protect the voucher system.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) identify personal data; (2) apply data minimisation; (3) reduce linkability on a shared ledger.

### 14.1 Identifying personal data

Personal data is any information relating to an identifiable person. For Lantern Hill this includes names, addresses, phone numbers, shift times and, importantly, voucher transactions linked to member codes, because a code can be tied back to a person through the database. Sofia maps where each item is stored and who can see it. She discovers that shift times reveal when a member is away from home, which some members would consider sensitive. Privacy is not only about secrets; it is about people's reasonable expectations of how information about them is used and who can see it.

### 14.2 Data minimisation

Data minimisation means collecting and keeping only what is needed. Sofia reviews the shift database and proposes removing birth dates, which were collected but never used, and deleting shift notes after a year. On the ledger she keeps only codes and amounts. She also asks whether the shop needs to see member names at the till; it does not, because the wallet proves entitlement. Each removal shrinks what could be leaked or misused. Minimisation is especially important for blockchain systems, because ledger data cannot easily be deleted once it has been written and copied to every node.

### 14.3 Reducing linkability

Even pseudonymous codes can be linked to people by patterns, such as a member who always spends at the same time each week. Sofia proposes that member codes on the ledger be different from those used in the database, with the link held only in the database under access control. She also suggests letting members use a fresh address each year. NIST IR 8202 notes that transparent ledgers expose transaction patterns, so designs must consider this. These measures reduce, but do not eliminate, linkability. She states the remaining risk plainly in her report for the board to accept or reject.

### Worked example

Sofia removes unused birth dates, separates ledger codes from database codes and offers yearly fresh addresses, stating remaining linkability honestly.

> **Synthetic case.** Member data and measures are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Assuming pseudonymous codes are anonymous ignores linkage through behaviour patterns.

### Exercises

- **EX040 — Sensitive pattern.** Why can shift times be sensitive? *Rubric:* 3 = they reveal when a member is away from home;; 2 = absence;; 1 = not sensitive;; 0 = none.
- **EX041 — Minimisation step.** Name one minimisation step. *Rubric:* 3 = remove unused birth dates;; 2 = delete old notes;; 1 = collect more;; 0 = none.
- **EX042 — Linkability measure.** How are ledger codes separated? *Rubric:* 3 = different codes on the ledger, link held in the database;; 2 = separate codes;; 1 = same codes;; 0 = none.

### Synthesis

Mapping, minimising and de-linking data protect members on a shared ledger.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) define useful security measures; (2) collect evidence reliably; (3) present measurements honestly.

### 15.1 Defining measures

A measure is useful if it informs a decision. Sofia proposes four for the voucher system: percentage of issued vouchers matched to approved shifts, number of reconciliation mismatches per month, time to restore a validator from backup, and number of privileged actions without a second approver. Each has a target agreed with the board. She avoids vanity measures, such as counting how many tests exist without asking whether they test anything important. Dr Asante adds that a measure should be easy to explain in one sentence, or the board will not use it when it matters.

### 15.2 Collecting evidence reliably

Evidence must be trustworthy. Sofia collects ledger data directly from a validator rather than from screenshots, records the time and source of each extract, and stores a SHA-256 hash of each file so later changes can be detected. Database extracts are taken through the read-only reporting account. She writes the steps as a short procedure, so another volunteer could repeat them and obtain the same results. Reliable evidence matters because decisions, and sometimes disputes between members, depend on it. Evidence that cannot be repeated or verified is easily challenged and rarely persuades anyone.

### 15.3 Presenting honestly

Sofia's first monthly report shows that 99.6 percent of vouchers matched approved shifts, with 22 unmatched out of 5,480. She explains that 20 were late approvals later confirmed and 2 were a coordinator's data-entry error, now corrected. She shows the counts, not just the percentage, and notes that one month is too short to show a trend. Honest presentation includes uncertainty and explanations. The board appreciates that she reports the error openly. Trust in security reporting grows when reports include bad news alongside good, clearly and without blame.

### Worked example

Sofia reports 22 unmatched of 5,480 vouchers (99.6 percent matched), explaining 20 late approvals and 2 entry errors, from hashed extracts.

> **Synthetic case.** Measures and figures are synthetic.

### Errors and limits

Counting tests or alerts without asking what they detect produces vanity measures.

### Exercises

- **EX043 — Measure example.** Name one of Sofia's four measures. *Rubric:* 3 = percentage of vouchers matched to approved shifts;; 2 = restore time;; 1 = number of tests;; 0 = none.
- **EX044 — Integrity of extracts.** How does she make extract changes detectable? *Rubric:* 3 = store a SHA-256 hash of each file;; 2 = hashes;; 1 = screenshots;; 0 = none.
- **EX045 — Unmatched explanation.** How were the 22 unmatched vouchers explained? *Rubric:* 3 = 20 late approvals and 2 entry errors;; 2 = late approvals;; 1 = theft;; 0 = none.

### Synthesis

Decision-focused measures, reliable collection and honest reporting make evidence useful.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) describe a system as components and trust boundaries; (2) apply defence in depth; (3) document architecture decisions.

### 16.1 Components and trust boundaries

Sofia draws the voucher system's architecture: member wallets, the shop terminal, the shift database, a small issuing service that turns approved shifts into mint requests, the treasury multisig, the voucher contract and three validators. She marks trust boundaries wherever data crosses from one owner or level of trust to another, such as from the database to the issuing service and from the service to the ledger. Each boundary needs a check: the service verifies approvals before requesting a mint, and the multisig keyholders verify the request before signing. Drawing boundaries shows where checks are missing.

### 16.2 Defence in depth

Defence in depth means layering controls so a single failure does not cause harm. For minting, Sofia's layers are: approvals in the database require a coordinator, the issuing service checks the shift is not already rewarded, the multisig requires two keyholders to sign, the contract enforces a weekly cap, and a daily reconciliation compares vouchers with shifts. An error at any one layer is caught by another. She notes that layers should be independent: if the same person controls both the approval and one multisig key, two layers collapse into one, so she separates those duties.

### 16.3 Documenting decisions

Sofia writes short architecture decision records. Each states the decision, the alternatives considered, the reasons, and the consequences. One record explains choosing a permissioned ledger over a public chain because members wanted low costs and controlled participation, accepting that the cooperative must operate validators. Another explains the weekly cap. Decision records help future volunteers understand why the system is the way it is, so they do not undo important choices by accident. Dr Asante notes that external reviewers also read them, since knowing the intent behind a design makes reviews faster and more accurate.

### Worked example

Sofia layers coordinator approval, duplicate checks, a 2-of-3 multisig, a contract weekly cap and daily reconciliation, separating approval from signing duties.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Letting one person control two layers collapses defence in depth into a single point.

### Exercises

- **EX046 — Boundary check.** What check sits at the database-to-service boundary? *Rubric:* 3 = the service verifies approvals before requesting a mint;; 2 = verify approvals;; 1 = vague;; 0 = none.
- **EX047 — Layer independence.** Why separate approval and signing duties? *Rubric:* 3 = so two layers do not collapse into one person;; 2 = independence;; 1 = speed;; 0 = none.
- **EX048 — Ledger choice reason.** Why a permissioned ledger? *Rubric:* 3 = low costs and controlled participation;; 2 = control;; 1 = popularity;; 0 = none.

### Synthesis

Clear boundaries, independent layers and recorded decisions make architecture defensible.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain hash functions and digital signatures; (2) use digests to detect change; (3) recognise cryptographic limits.

### 17.1 Hash functions

A cryptographic hash function turns any input into a fixed-length digest. Good hash functions make it infeasible to find two inputs with the same digest or to work backwards from a digest. SHA-256, used in Nakamoto's design, produces 256-bit digests, written as 64 hexadecimal characters. Changing a single character of the input changes the digest completely. Sofia uses this property to protect evidence and records: if a stored digest no longer matches a file, the file has changed. Blockchains chain blocks together by including each block's predecessor's digest, so altering an old block would break every link after it.

### 17.2 Digital signatures

A digital signature lets the holder of a private key sign a message so anyone with the matching public key can verify it. Ethereum-compatible ledgers use elliptic-curve signatures, as described in Wood's yellow paper. A valid signature shows the message came from the key holder and was not altered. It does not show the key holder intended the action wisely, or that the key was not stolen. Sofia explains this to the board: the ledger checks that the right key signed, while the cooperative's processes must check that signing was the right decision for that particular request.

### Lab — Detecting altered voucher records

```python
"""Detect altered voucher records by comparing SHA-256 digests (synthetic, read-only)."""
import hashlib

def digest(record):
    return hashlib.sha256(record.encode("utf-8")).hexdigest()

ISSUED = ["V001|m014|25", "V002|m233|10", "V003|m087|40", "V004|m512|15"]
STORED = {r.split("|")[0]: digest(r) for r in ISSUED}
CURRENT = ["V001|m014|25", "V002|m233|100", "V003|m087|40", "V004|m512|15"]

def main():
    changed = [r.split("|")[0] for r in CURRENT if digest(r) != STORED[r.split("|")[0]]]
    print(f"records {len(CURRENT)}; changed {len(changed)}: {', '.join(changed)}")
    print(f"digest length {len(STORED['V001'])} hex characters")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_digest.py`. Verified output:

```text
records 4; changed 1: V002
digest length 64 hex characters
```

### 17.3 What the lab shows and its limits

The lab stores SHA-256 digests of four synthetic voucher records when they are issued, then compares them with current records. One record, V002, has had its amount changed from 10 to 100, and its digest no longer matches, so it is reported. Each digest is 64 hexadecimal characters. Sofia notes the limits: a digest detects change only if the stored digest itself is protected, for example by recording it on the ledger. Cryptography also cannot help if the original record was wrong when created. It proves consistency over time, not truth at the moment of creation.

### Worked example

The lab flags V002 among four records because its amount changed from 10 to 100, using 64-character SHA-256 digests.

> **Synthetic case.** The voucher records are synthetic; Nakamoto (2008) and Wood's yellow paper are real sources.

### Errors and limits

Trusting a digest stored beside the data it protects lets anyone who alters the data alter the digest too.

### Exercises

- **EX049 — Digest length.** How many hex characters does a SHA-256 digest have? *Rubric:* 3 = 64;; 2 = sixty-four;; 1 = 32;; 0 = none.
- **EX050 — Signature limit.** What does a valid signature not prove? *Rubric:* 3 = that the action was wise or the key not stolen;; 2 = intent;; 1 = origin;; 0 = none.
- **EX051 — Lab result.** Which record does the lab report as changed? *Rubric:* 3 = V002, from 10 to 100;; 2 = V002;; 1 = V001;; 0 = none.

### Synthesis

Hashes and signatures prove consistency and origin, while processes must ensure correctness.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) formulate a research question; (2) choose a suitable method; (3) plan data collection ethically.

### 18.1 Formulating a question

Sofia's first research project asks: how often do cooperative voucher records and ledger balances disagree, and why? A good research question is specific, answerable with available evidence and useful to someone. Hers is specific to the test ledger, answerable from reconciliation logs and useful to the board. Dr Asante helps her narrow an earlier, vaguer question about whether blockchains are secure, which no small project could answer. A focused question makes every later step clearer: what data to collect, how to analyse it and how to judge whether the answer is convincing to a careful reader.

### 18.2 Choosing a method

Sofia considers methods. A survey of members could reveal their experiences but not the true cause of mismatches. Analysis of reconciliation logs can count mismatches and classify causes. Interviews with coordinators could explain how errors arise. She chooses log analysis supported by short interviews, a mixed approach that combines counts with explanations. She writes down the strengths and weaknesses of each method and why she chose hers. Method choice should follow the question, not the researcher's favourite technique, and stating the reasons openly allows readers to judge the strength of the conclusions.

### 18.3 Planning ethically

Research involving people needs ethical approval. Sofia applies to the university's ethics committee, explaining that she will use synthetic and pseudonymised logs, interview coordinators only with their written consent, store notes securely and delete them after the project. Coordinators may withdraw at any time. She will not record names in her analysis. The committee approves with one change: interviews should avoid discussing any named member. Ethical planning protects participants and the cooperative, and it improves the research too, because participants speak more openly when they trust how their words will be used.

### Worked example

Sofia narrows her question to mismatch frequency and causes, combines log analysis with consented interviews and gains ethics approval with one change.

> **Synthetic case.** The research project and approval are synthetic.

### Errors and limits

Choosing a method before the question often answers a different question than the one asked.

### Exercises

- **EX052 — Research question.** What is Sofia's research question? *Rubric:* 3 = how often records and ledger balances disagree, and why;; 2 = mismatch frequency;; 1 = are blockchains secure;; 0 = none.
- **EX053 — Chosen method.** Which method does she choose? *Rubric:* 3 = log analysis with short interviews;; 2 = mixed;; 1 = survey only;; 0 = none.
- **EX054 — Committee change.** What change did the ethics committee require? *Rubric:* 3 = avoid discussing any named member;; 2 = no names;; 1 = vague;; 0 = none.

### Synthesis

A focused question, fitting method and ethical plan make research credible.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Web3, blockchain and cryptoasset security: scope and theory

### Learning outcomes

You will (1) define the field's scope; (2) explain consensus and smart contracts; (3) relate theory to the cooperative.

### 19.1 Scope of the field

Web3, blockchain and cryptoasset security covers the ledgers themselves, the smart contracts running on them, the keys and wallets that control assets, the off-chain services that feed and read them, and the people and processes around them. Sofia draws this scope as concentric rings around the voucher contract. NIST IR 8202 describes blockchain components and permission models, and the OWASP Smart Contract Top 10 lists common contract weaknesses. She notes that many real losses arise outside contract code, in key handling and operations, so the field's scope must include those areas even when they seem ordinary or familiar.

### 19.2 Consensus and contracts

Consensus lets independent nodes agree on one history. Nakamoto's design uses proof of work; Ethereum later moved to proof of stake; permissioned ledgers often use voting among known validators. Smart contracts are programs stored on the ledger and executed by every node, as described in Buterin's whitepaper and Wood's yellow paper. Their code is public on most ledgers and hard to change once deployed. Sofia notes the security consequence: mistakes in contract code are visible to everyone and difficult to fix, so careful design and review before deployment matter more than in ordinary software, where patches are routine.

### 19.3 Theory applied to the cooperative

Sofia applies the theory. The cooperative's ledger uses voting among three known validators, so agreement depends on at least two being honest and online. The voucher contract enforces the weekly cap and role checks. Keys control minting, pausing and administration. The shift database and issuing service sit outside the ledger but determine what is minted. She concludes that the cooperative's main risks lie in keys, the issuing service and the contract's role logic, rather than in consensus. This conclusion directs her studies: she will spend most effort where the risk actually lies.

### Worked example

Sofia concludes that keys, the issuing service and role logic, not consensus among three validators, carry the cooperative's main risks.

> **Synthetic case.** The cooperative's system is synthetic; NIST IR 8202, OWASP SC Top 10, Nakamoto, Buterin and Wood are real sources.

### Errors and limits

Focusing only on contract code misses losses arising from keys and operations.

### Exercises

- **EX055 — Field scope.** Name one area inside the field's scope beyond contracts. *Rubric:* 3 = keys and wallets;; 2 = off-chain services;; 1 = office furniture;; 0 = none.
- **EX056 — Validator agreement.** How many validators must be honest and online? *Rubric:* 3 = at least two of three;; 2 = two;; 1 = all three;; 0 = none.
- **EX057 — Main risks.** Where does Sofia place the cooperative's main risks? *Rubric:* 3 = keys, the issuing service and role logic;; 2 = keys;; 1 = consensus;; 0 = none.

### Synthesis

The field spans ledgers, contracts, keys, services and people, and risk guides where to focus.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Web3, blockchain and cryptoasset security: foundational cases

### Learning outcomes

You will (1) study weakness classes through published research; (2) extract general lessons; (3) apply lessons safely.

### 20.1 Learning from published research

Sofia studies foundational research rather than attack recipes. Atzei, Bartoletti and Cimoli's 2017 survey classifies weaknesses in Ethereum contracts, such as unexpected interactions between contracts and mistakes in handling calls. Luu and colleagues' 2016 paper describes how contract behaviour can depend on transaction ordering and other conditions developers do not control. Both papers help her understand categories of weakness at a conceptual level. She reads them for lessons about design, not for procedures. Dr Asante asks each student to summarise one weakness class in a paragraph a board member could understand.

### 20.2 General lessons

From the research Sofia extracts three lessons. First, contracts interact with other contracts and with unpredictable ordering, so they must be written to remain correct whatever happens between steps. Second, assumptions about the environment, such as timing or who calls a function, must be checked in code. Third, many weaknesses fall into known classes, catalogued in the SWC registry, so reviewers can check systematically. She summarises each lesson in plain words. The lessons apply to the voucher contract even though it is simple, because simplicity reduces but does not remove the risk of such assumptions.

### 20.3 Applying lessons safely

Sofia reviews the voucher contract design against the three lessons. She confirms that balances are updated before any external interaction, that role checks are made in every privileged function, and that no function depends on block timestamps for important decisions. She records each check and its result. She does not attempt to break the contract or write any attack code; review is done by reading and by testing expected behaviour on the test ledger with synthetic data. Applying lessons this way improves security without creating anything that could harm others if shared beyond the course.

### Worked example

Sofia checks the voucher contract for state updates before external interaction, role checks on privileged functions and no timestamp-dependent decisions.

> **Synthetic case.** The contract review is synthetic; Atzei et al. (2017), Luu et al. (2016) and the SWC registry are real sources.

### Errors and limits

Reading research for procedures rather than lessons risks producing harmful material.

### Exercises

- **EX058 — Survey source.** Which 2017 survey classifies Ethereum contract weaknesses? *Rubric:* 3 = Atzei, Bartoletti and Cimoli;; 2 = Atzei;; 1 = Nakamoto;; 0 = none.
- **EX059 — Environment lesson.** What lesson concerns the environment? *Rubric:* 3 = check assumptions about timing and callers in code;; 2 = check assumptions;; 1 = ignore it;; 0 = none.
- **EX060 — Review method.** How does Sofia review without attacking? *Rubric:* 3 = reading and testing expected behaviour with synthetic data;; 2 = reading;; 1 = attack code;; 0 = none.

### Synthesis

Published research teaches weakness classes that guide careful, defensive review.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Web3, blockchain and cryptoasset security: system models

### Learning outcomes

You will (1) model the voucher system's states and transitions; (2) identify invariants; (3) model actors and their powers.

### 21.1 States and transitions

Sofia models the voucher contract as a state machine. Its state is the set of balances, total supply, the paused flag and the role assignments. Transitions are issue, transfer, redeem, pause, unpause and change role. Each transition has preconditions, such as the caller holding the right role or having enough vouchers, and effects on the state. Writing the model as a table makes gaps visible: she notices that the design did not say whether redemption is allowed while paused. The board decides it should not be, and the specification is updated before any contract code is written.

### 21.2 Invariants

An invariant is a property that must hold in every reachable state. Sofia lists the voucher system's invariants: total supply equals the sum of balances; no balance is negative; weekly issuance never exceeds the cap; only the minter role can increase supply. For each transition she checks that, if the invariants hold before, they still hold after. This reasoning, done on paper first, guides the tests she later writes. Invariants are powerful because they summarise correctness in a few sentences, and violations can be detected automatically by monitoring software that compares the live ledger with them.

### 21.3 Actors and powers

The model also lists actors: members, the shop, coordinators, the issuing service, three keyholders, three validator operators and the board. For each, Sofia records what they can do directly and what they can influence indirectly. Coordinators cannot mint, but their approvals cause minting. Validator operators cannot change balances, but two of them together could stop the ledger. This actor model reveals indirect powers that a contract-only view would miss. She uses it to decide where extra checks are needed, such as a second coordinator approving any week with unusually many shifts.

### Worked example

Sofia's state model blocks redemption while paused, lists four invariants and reveals that coordinators indirectly cause minting.

> **Synthetic case.** The model and actors are synthetic.

### Errors and limits

Modelling only direct contract powers misses actors who cause outcomes indirectly.

### Exercises

- **EX061 — Specification gap.** What gap did the state table reveal? *Rubric:* 3 = whether redemption is allowed while paused;; 2 = redemption when paused;; 1 = vague;; 0 = none.
- **EX062 — Invariant example.** Give one voucher invariant. *Rubric:* 3 = total supply equals the sum of balances;; 2 = no negative balance;; 1 = supply grows;; 0 = none.
- **EX063 — Indirect power.** What indirect power do coordinators have? *Rubric:* 3 = their approvals cause minting;; 2 = approvals;; 1 = vague;; 0 = none.

### Synthesis

State, invariant and actor models make a token system's correctness and risks explicit.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Web3, blockchain and cryptoasset security: data and dependencies

### Learning outcomes

You will (1) trace data flows across on-chain and off-chain parts; (2) identify dependencies; (3) plan for dependency failure.

### 22.1 Tracing data flows

Sofia traces how one volunteer shift becomes vouchers. A coordinator records the shift in the database; another approves it; each night the issuing service reads approved shifts, builds a mint batch, and sends it to the keyholders; two keyholders sign; the contract mints; the shop terminal reads balances from a validator. At each step she records the data, its format, who can change it and how it is checked. The trace shows that the issuing service is a critical point: if its output is wrong, keyholders may sign an incorrect batch without noticing anything unusual.

### 22.2 Identifying dependencies

The system depends on components the cooperative does not fully control: the hosting provider for validators, the wallet application members use, the libraries used by the contract and issuing service, and the compiler that builds the contract. Sofia lists each dependency, its owner, its update frequency and how failure would show. The SWC registry includes weaknesses from outdated compilers, so she records the exact compiler version. Dependencies are part of the attack surface and the failure surface, and knowing them is the first step to managing them rather than being surprised by changes made by someone else.

### 22.3 Planning for dependency failure

For each important dependency Sofia writes what the cooperative would do if it failed. If the hosting provider has an outage, two validators in different data centres keep the ledger running. If the wallet application is withdrawn, members can export keys to another compatible wallet. If a library has a serious flaw, the issuing service can be stopped and minting done manually with extra checks. She pins library versions and reviews updates monthly. Planning ahead turns dependency failures from crises into procedures, and the board approves the plan with a yearly review date.

### Worked example

Sofia finds the issuing service is a critical point and plans responses for hosting, wallet and library failures, with pinned versions.

> **Synthetic case.** The data flows and dependencies are synthetic; the SWC registry is a real source.

### Errors and limits

Assuming dependencies are stable leaves the system unprepared when they change or fail.

### Exercises

- **EX064 — Critical point.** Which component does the trace show is critical? *Rubric:* 3 = the issuing service;; 2 = issuing service;; 1 = the shop;; 0 = none.
- **EX065 — Compiler record.** Why record the exact compiler version? *Rubric:* 3 = outdated compilers are a known weakness class;; 2 = compiler risk;; 1 = style;; 0 = none.
- **EX066 — Library response.** What happens if a library has a serious flaw? *Rubric:* 3 = stop the issuing service and mint manually with extra checks;; 2 = manual minting;; 1 = ignore;; 0 = none.

### Synthesis

Tracing flows and planning for dependency failure make hidden risks manageable.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Web3, blockchain and cryptoasset security: methods I

### Learning outcomes

You will (1) apply checklist-based review; (2) use standards as review criteria; (3) record review findings consistently.

### 23.1 Checklist-based review

A checklist turns knowledge into a repeatable review. Sofia builds one for the voucher contract from the OWASP Smart Contract Top 10 and the SWC registry, phrased as questions: are all privileged functions restricted, are external calls made after state updates, are arithmetic limits handled, is the compiler pinned, are events emitted for every change. Each question has a yes, no or not applicable answer with evidence. Checklists do not find everything, but they ensure known issues are not forgotten, and they let different reviewers produce comparable results on the same code over time.

### 23.2 Standards as criteria

The EEA EthTrust Security Levels specification defines requirements a contract should meet at different levels of assurance. Sofia maps her checklist to EthTrust requirements where they correspond, so findings can be reported against a recognised standard rather than personal opinion. She notes that the specification itself states that meeting its requirements does not guarantee a contract is free of weaknesses. Using standards gives reviews a shared language and makes results easier for others to trust. She records the specification version used, because requirements change between versions and readers need to know which applied.

### 23.3 Recording findings

Each finding is recorded with an identifier, location, description, severity, related standard requirement, evidence and recommended fix. Severity considers both impact and likelihood. Sofia reviews the voucher contract and records two findings: one function that changes the weekly cap emits no event, so changes are hard to monitor; and the compiler version is a range rather than a fixed value. Both are rated low severity. She shares them with the developer, who fixes both within a week. Consistent records make findings easy to track, verify and report to the board in plain language.

### Worked example

Sofia's checklist review finds a missing event on the cap-change function and an unpinned compiler, both low severity and fixed within a week.

> **Synthetic case.** The review is synthetic; OWASP SC Top 10, the SWC registry and EEA EthTrust are real sources.

### Errors and limits

Treating a passed checklist as proof of security ignores weaknesses the checklist does not cover.

### Exercises

- **EX067 — Checklist sources.** Which sources shape the checklist? *Rubric:* 3 = OWASP SC Top 10 and the SWC registry;; 2 = OWASP;; 1 = a forum;; 0 = none.
- **EX068 — Standard caveat.** What does EthTrust say about meeting its requirements? *Rubric:* 3 = it does not guarantee freedom from weaknesses;; 2 = no guarantee;; 1 = full guarantee;; 0 = none.
- **EX069 — Review findings.** What two findings does Sofia record? *Rubric:* 3 = missing cap-change event and unpinned compiler;; 2 = missing event;; 1 = stolen funds;; 0 = none.

### Synthesis

Checklists anchored in standards produce consistent, trusted review findings.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Web3, blockchain and cryptoasset security: controls

### Learning outcomes

You will (1) select controls for keys, contracts and operations; (2) balance security with usability; (3) verify controls work.

### 24.1 Selecting controls

Sofia selects controls for each risk area. For keys: hardware devices, a 2-of-3 multisig, and documented recovery. For contracts: role restrictions, the weekly cap, a pause function, a timelock on administration and events for every change. For operations: daily reconciliation, monitoring of privileged actions and a tested incident procedure. She links each control to a risk from her earlier asset list, so every control has a reason and no important risk is left uncovered. The board can see why each control exists and what would be lost if it were removed to save effort.

### 24.2 Balancing usability

Controls that are too hard to use are bypassed. Sofia notices that requiring two keyholders for every small mint batch causes delays, because keyholders are volunteers with jobs. She proposes one weekly batch at a fixed time, so keyholders can plan, instead of nightly batches. Members' wallets stay simple; the cooperative's custodial option remains for those who prefer it. She explains that good security fits the way people actually work. The ConsenSys best practices note that complexity increases the chance of errors, and that applies to procedures just as much as to code.

### 24.3 Verifying controls work

A control that has never been tested may not work. Sofia schedules tests: a keyholder signs a test transaction on the test ledger each month to confirm devices work; the pause function is exercised on the test network each quarter; reconciliation is run against a deliberately altered synthetic dataset to confirm it detects the change. Each test result is recorded. She finds that one keyholder's device firmware needs an update before it will sign, which would have caused a delay in a real emergency. Testing controls turns assumptions into evidence and reveals problems while there is still time.

### Worked example

Sofia moves to one weekly mint batch for usability and finds through monthly testing that one keyholder device needs a firmware update.

> **Synthetic case.** The controls and tests are synthetic; ConsenSys best practices is a real source.

### Errors and limits

Assuming an untested control works can fail exactly when it is first needed.

### Exercises

- **EX070 — Key controls.** Name one key control. *Rubric:* 3 = hardware devices;; 2 = 2-of-3 multisig;; 1 = shared password;; 0 = none.
- **EX071 — Batch change.** Why move to a weekly batch? *Rubric:* 3 = volunteer keyholders can plan, avoiding delays;; 2 = usability;; 1 = cheaper gas;; 0 = none.
- **EX072 — Test discovery.** What did monthly signing tests reveal? *Rubric:* 3 = a keyholder device needed a firmware update;; 2 = firmware;; 1 = nothing;; 0 = none.

### Synthesis

Risk-linked, usable and regularly tested controls provide real protection.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) replay ledger events to compute balances; (2) compare replayed state with a snapshot; (3) investigate mismatches calmly.

### 25.1 Why replay events

Every voucher transfer emits an event recording sender, receiver and amount. Issuance uses a zero sender, and redemption uses a zero receiver. By replaying all events in order, Sofia can compute what every balance should be, independently of the contract's own stored balances. Comparing the two is a strong check: if they differ, either an event was missed, the snapshot is stale, or something unexpected happened. This lab uses six synthetic events and a snapshot of four members. It is read-only and uses only Python's standard library, so it can run safely on any computer.

### Lab — Event replay against a snapshot

```python
"""Replay synthetic Transfer events and compare with a balance snapshot (read-only)."""
# (from, to, amount); "0x0" as sender means issuance, as receiver means redemption
EVENTS = [
    ("0x0", "m01", 50), ("0x0", "m02", 30), ("m01", "m03", 20),
    ("m02", "0x0", 10), ("0x0", "m04", 40), ("m03", "m04", 5),
]
SNAPSHOT = {"m01": 30, "m02": 20, "m03": 15, "m04": 50}

def main():
    bal = {}
    for f, t, a in EVENTS:
        if f != "0x0":
            bal[f] = bal.get(f, 0) - a
        if t != "0x0":
            bal[t] = bal.get(t, 0) + a
    diff = [m for m in sorted(SNAPSHOT) if SNAPSHOT[m] != bal.get(m, 0)]
    print(f"events {len(EVENTS)}; replayed supply {sum(bal.values())}; snapshot supply {sum(SNAPSHOT.values())}")
    for m in diff:
        print(f"mismatch {m}: replay {bal.get(m, 0)} snapshot {SNAPSHOT[m]}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_events.py`. Verified output:

```text
events 6; replayed supply 110; snapshot supply 115
mismatch m04: replay 45 snapshot 50
```

### 25.2 Reading the result

The lab replays six events and computes a supply of 110 vouchers, while the snapshot shows 115. One member differs: m04, with 45 in the replay and 50 in the snapshot. The other three members match exactly. Sofia does not assume wrongdoing. She lists possible explanations: a missed issuance event in her extract, a snapshot taken after a later event, or an issuance that bypassed events. She checks the extract's block range first, because the simplest explanation is usually a data-collection gap. In this synthetic case, the extract ended one block early, missing a valid issuance.

### 25.3 Investigating calmly

Sofia records the mismatch, the explanations considered, the checks made and the conclusion. She updates the extraction procedure so the block range is always recorded and compared with the snapshot's block. Dr Asante praises the calm approach: mismatches are signals to investigate, not proof of an incident. Jumping to conclusions can cause unnecessary alarm or wrongly blame someone. Equally, ignoring mismatches can let a real problem grow. A clear, recorded investigation is the right response, and she shares the improved procedure with the other volunteers so the same gap does not recur.

### Worked example

The lab replays six events to a supply of 110 against a snapshot of 115, isolating m04 (45 versus 50), traced to an extract ending one block early.

> **Synthetic case.** The events, snapshot and investigation are synthetic.

### Errors and limits

Comparing data from different block ranges creates mismatches that are artefacts, not incidents.

### Exercises

- **EX073 — Zero address meaning.** What does a zero sender indicate? *Rubric:* 3 = issuance;; 2 = minting;; 1 = redemption;; 0 = none.
- **EX074 — Replay totals.** What supplies do the replay and snapshot show? *Rubric:* 3 = 110 and 115;; 2 = 110/115;; 1 = equal;; 0 = none.
- **EX075 — Mismatch cause.** What caused m04's mismatch in the case? *Rubric:* 3 = the extract ended one block early;; 2 = block range;; 1 = theft;; 0 = none.

### Synthesis

Event replay gives an independent check, and calm investigation explains its differences.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Web3, blockchain and cryptoasset security: methods II

### Learning outcomes

You will (1) use automated analysis carefully; (2) combine tools with manual review; (3) interpret tool output critically.

### 26.1 Automated analysis

Automated tools scan contract code for patterns associated with known weaknesses. Durieux and colleagues' 2020 study evaluated several such tools on large sets of contracts and found that they disagreed often and each missed many issues, while also reporting false positives. Tsankov and colleagues' 2018 work described security analysis that checks properties rather than patterns. Sofia learns that tools are useful but limited. She runs one widely used open-source analyser on the voucher contract in the course's test environment, under supervision, and saves its output for comparison with her manual review.

### 26.2 Combining tools and review

The tool reports five items. Sofia compares them with her manual checklist. Two match her earlier findings, already fixed. Two are false positives: the tool flags a pattern that is safe in context because of a role check it did not understand. One is new: a function lacks an explicit check that the amount is above zero. She confirms it manually and records it as a low-severity finding. Combining approaches catches more than either alone. She notes that the tool found something she had missed, and she had found issues the tool missed, which matches what the research suggested.

### 26.3 Interpreting critically

Sofia writes guidance for interpreting tool output: treat every item as a question, confirm it by reading the code, record why false positives are safe, and never treat a clean result as proof of security. She also records the tool version, because results change between versions. Perez and Livshits' 2021 study found that many reported weaknesses in deployed contracts were never actually exploited, a reminder that a finding's real risk depends on context. Interpreting critically avoids both panic about harmless reports and false confidence from clean ones, and it keeps reviews grounded in evidence.

### Worked example

The analyser reports five items: two already fixed, two false positives explained by role checks, and one new missing zero-amount check confirmed manually.

> **Synthetic case.** The analysis is synthetic; Durieux et al. (2020), Tsankov et al. (2018) and Perez and Livshits (2021) are real sources.

### Errors and limits

Treating a clean tool report as proof of security ignores the many issues tools miss.

### Exercises

- **EX076 — Tool study finding.** What did Durieux et al. find about tools? *Rubric:* 3 = they disagreed and each missed many issues;; 2 = disagreement;; 1 = all perfect;; 0 = none.
- **EX077 — Tool output breakdown.** How did the five tool items break down? *Rubric:* 3 = two fixed, two false positives, one new;; 2 = 2/2/1;; 1 = all new;; 0 = none.
- **EX078 — Context lesson.** What did Perez and Livshits remind readers? *Rubric:* 3 = reported weaknesses were often never exploited;; 2 = context matters;; 1 = all exploited;; 0 = none.

### Synthesis

Tools and manual review complement each other when output is interpreted critically.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Web3, blockchain and cryptoasset security: verification

### Learning outcomes

You will (1) write tests from invariants; (2) use test networks safely; (3) record verification evidence.

### 27.1 Tests from invariants

Sofia turns each invariant into tests. After every test action, the test checks that total supply equals the sum of balances, no balance is negative and weekly issuance is within the cap. She writes tests for normal actions, edge cases and forbidden actions: an issuance by a non-minter must be refused, a transfer while paused must be refused, and a mint that would exceed the cap must be refused. Testing forbidden actions is as important as testing allowed ones, because security failures usually mean something forbidden became possible without anyone noticing.

### 27.2 Using test networks safely

All tests run on the cooperative's private test network with synthetic members and vouchers that have no value. Test keys are separate from production keys and are clearly labelled. Sofia never uses production keys in tests and never deploys test contracts to the live ledger. The test network is reset regularly. These boundaries mean mistakes during testing cannot affect real members. Dr Asante notes that confusion between test and production environments is a common cause of real incidents, so clear labelling and separation are themselves security controls, not mere tidiness or convenience.

### 27.3 Recording verification evidence

Sofia stores test results with the contract version, compiler version, test network block and date. A summary shows 42 tests, all passing, with the invariant checks run after each. When the developer changes the contract, the tests are rerun and the new results stored alongside the old. This record lets the board and any external reviewer see exactly what was verified and when. Verification evidence is only valuable if it clearly corresponds to the code actually deployed, so she records the deployed contract's code hash and compares it with the tested build.

### Worked example

Sofia runs 42 invariant-checked tests, including forbidden actions, on a separate test network and matches the deployed code hash to the tested build.

> **Synthetic case.** The tests and networks are synthetic.

### Errors and limits

Using production keys on a test network risks real loss from test mistakes.

### Exercises

- **EX079 — Forbidden action test.** Give one forbidden action that is tested. *Rubric:* 3 = issuance by a non-minter;; 2 = transfer while paused;; 1 = normal transfer;; 0 = none.
- **EX080 — Environment separation.** Why keep test and production keys separate? *Rubric:* 3 = test mistakes cannot affect real members;; 2 = isolation;; 1 = speed;; 0 = none.
- **EX081 — Deployment match.** How is tested code matched to deployed code? *Rubric:* 3 = compare the deployed code hash with the tested build;; 2 = code hash;; 1 = by name;; 0 = none.

### Synthesis

Invariant-based tests on separated networks, with matched records, give trustworthy verification.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Web3, blockchain and cryptoasset security: failure analysis

### Learning outcomes

You will (1) analyse a failure without blame; (2) identify root and contributing causes; (3) turn findings into improvements.

### 28.1 A synthetic failure

In a synthetic exercise, the issuing service sends a mint batch containing one week's shifts twice, because a scheduled job restarted after a server update. Keyholders sign without noticing, since the batch looked normal. The contract's weekly cap blocks the second half, so only part of the duplicate is minted. Daily reconciliation detects 310 extra vouchers the next morning. The board pauses transfers for two hours, the extra vouchers are removed with the members' agreement, and the system resumes. No member loses vouchers. Sofia leads the analysis of what happened and why.

### 28.2 Root and contributing causes

Sofia uses a blameless approach: the goal is to understand the system, not to punish people. The root cause is the issuing service lacking a check that a week has already been processed. Contributing causes include the restart after an update, keyholders having no summary showing whether a week was new, and reconciliation running only daily. She also notes what worked: the weekly cap limited the error and reconciliation detected it. Recording what worked matters, because those controls should be kept and strengthened rather than removed in future changes to reduce effort.

### 28.3 Turning findings into improvements

Sofia proposes three improvements: the issuing service records processed weeks and refuses repeats; each batch sent to keyholders includes a summary showing the week number and whether it was already processed; and reconciliation runs every hour. Each improvement has an owner and a deadline. She writes a short report in plain language for members, explaining what happened, that no one lost vouchers and what is changing. Clear communication after a failure maintains trust. The improvements are later tested on the test network with a simulated restart, confirming the repeat is refused.

### Worked example

A duplicated batch adds 310 extra vouchers, limited by the cap and caught by reconciliation; fixes add repeat refusal, batch summaries and hourly checks.

> **Synthetic case.** The failure and response are synthetic.

### Errors and limits

Blaming individuals for a system gap hides the root cause and discourages honest reporting.

### Exercises

- **EX082 — Extra vouchers.** How many extra vouchers were detected? *Rubric:* 3 = 310;; 2 = three hundred ten;; 1 = 3,100;; 0 = none.
- **EX083 — Root cause.** What was the root cause? *Rubric:* 3 = no check that a week was already processed;; 2 = missing repeat check;; 1 = a keyholder;; 0 = none.
- **EX084 — Controls that worked.** Which controls limited and detected the error? *Rubric:* 3 = the weekly cap and reconciliation;; 2 = cap;; 1 = vague;; 0 = none.

### Synthesis

Blameless analysis finds causes, keeps what worked and drives tested improvements.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Web3, blockchain and cryptoasset security: operations

### Learning outcomes

You will (1) run routine security operations; (2) respond to incidents with a plan; (3) maintain records and handovers.

### 29.1 Routine operations

Sofia writes a weekly operations routine for volunteers: confirm all three validators are in sync, check disk and memory alerts, review privileged actions in the past week, confirm reconciliation results, check pending library updates and confirm keyholder availability for the next batch. Each item takes a few minutes and is recorded in a shared log. Routines catch problems early, when they are small. She designs the routine to fit in thirty minutes, because a routine that takes too long will be skipped by busy volunteers, which is worse than a shorter routine done reliably.

### 29.2 Responding to incidents

The incident plan defines what counts as an incident, who is contacted, and the first steps. For example, if reconciliation shows an unexplained mismatch above 50 vouchers, the duty volunteer contacts two keyholders, who decide whether to pause transfers. The plan lists contacts, decision rules and how to inform members. It avoids technical detail that could be misused and focuses on decisions and communication. Sofia runs a tabletop exercise where the board talks through a scenario. They find that no one knew who should inform members, so a named communications lead is added.

### 29.3 Records and handovers

Volunteers change often. Sofia keeps a handover file listing current keyholders, validator operators, open issues, recent incidents, pending updates and where procedures are stored. When a volunteer leaves, a checklist removes their access and transfers their duties. She notes that the 2-of-3 multisig must be updated promptly when a keyholder leaves, or the cooperative risks having too few active signers. Good records make the system resilient to people changes, which in small organisations are often a greater risk than technical failures or attacks from outsiders.

### Worked example

Sofia's thirty-minute weekly routine, a pause threshold of 50 unexplained vouchers and a named communications lead strengthen operations.

> **Synthetic case.** The routine, plan and exercise are synthetic.

### Errors and limits

A routine too long for volunteers will be skipped, leaving problems undetected.

### Exercises

- **EX085 — Routine length.** How long is the weekly routine designed to take? *Rubric:* 3 = thirty minutes;; 2 = 30 minutes;; 1 = all day;; 0 = none.
- **EX086 — Pause threshold.** What mismatch triggers contacting keyholders? *Rubric:* 3 = an unexplained mismatch above 50 vouchers;; 2 = above 50;; 1 = any mismatch;; 0 = none.
- **EX087 — Tabletop gap.** What gap did the tabletop exercise reveal? *Rubric:* 3 = no one knew who should inform members;; 2 = communications;; 1 = no gaps;; 0 = none.

### Synthesis

Short routines, a decision-focused incident plan and good handovers keep operations dependable.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) check a deployment configuration against policy; (2) interpret configuration findings; (3) decide whether to deploy.

### 30.1 Configuration as evidence

Before deploying an updated voucher contract, the cooperative's policy requires checks: the treasury multisig has at least two signers, mint and upgrade actions have timelocks of at least 48 hours, the compiler is pinned, and every test passes. Sofia writes these as a small read-only script that reads a synthetic configuration and reports any differences from the policy. Turning policy into an automatic check means it is applied the same way every time, without relying on memory, and the output becomes evidence for the deployment decision recorded by the board.

### Lab — Deployment configuration check

```python
"""Check a synthetic deployment configuration against a written policy (read-only)."""
CONFIG = {
    "treasury_threshold": (2, 3), "mint_timelock_h": 24, "upgrade_timelock_h": 48,
    "pause_holders": 2, "compiler_pinned": True, "tests_passed": 41, "tests_total": 42,
}
def main():
    issues = []
    m, n = CONFIG["treasury_threshold"]
    if m < 2:
        issues.append("treasury needs at least 2 signers")
    for k in ("mint_timelock_h", "upgrade_timelock_h"):
        if CONFIG[k] < 48:
            issues.append(f"{k} {CONFIG[k]} < 48")
    if not CONFIG["compiler_pinned"]:
        issues.append("compiler not pinned")
    if CONFIG["tests_passed"] != CONFIG["tests_total"]:
        issues.append(f"tests {CONFIG['tests_passed']}/{CONFIG['tests_total']}")
    print(f"checks 4; issues {len(issues)}")
    for i in issues:
        print(" -", i)

if __name__ == "__main__":
    main()
```

Run with `python3 lab_config.py`. Verified output:

```text
checks 4; issues 2
 - mint_timelock_h 24 < 48
 - tests 41/42
```

### 30.2 Reading the result

The script runs four checks and reports two issues. The mint timelock is 24 hours, below the 48-hour policy, and 41 of 42 tests pass. The treasury threshold of two of three and the pinned compiler meet the policy. Sofia investigates: the developer had shortened the mint timelock during testing to speed things up and forgot to restore it; the failing test concerns the zero-amount check added after the tool review. Both are fixable. She records the findings with the configuration version and date, so the record can be compared with the next run.

### 30.3 Deciding whether to deploy

Sofia recommends not deploying until both issues are fixed. The developer restores the 48-hour timelock and fixes the failing test, and the script then reports no issues. The board approves deployment at its next meeting, and two keyholders sign the deployment. Sofia notes that a configuration check is only as good as its policy: if the policy omits something important, the script will not catch it. She proposes reviewing the policy annually. Automated checks make good decisions easier, but people still decide, and the decision is recorded with its evidence.

### Worked example

The script reports a 24-hour mint timelock below 48 and 41/42 tests passing; both are fixed before the board approves deployment.

> **Synthetic case.** The configuration and deployment are synthetic.

### Errors and limits

A configuration check cannot catch risks its policy does not include.

### Exercises

- **EX088 — Check count.** How many checks does the script run? *Rubric:* 3 = four;; 2 = 4;; 1 = two;; 0 = none.
- **EX089 — Timelock issue.** What timelock issue is reported? *Rubric:* 3 = mint timelock 24 hours below 48;; 2 = 24 < 48;; 1 = upgrade too long;; 0 = none.
- **EX090 — Deployment recommendation.** What does Sofia recommend before deploying? *Rubric:* 3 = fix both issues first;; 2 = wait;; 1 = deploy now;; 0 = none.

### Synthesis

Policy-as-checks provide consistent deployment evidence, while people make the final decision.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Web3, blockchain and cryptoasset security: advanced cases

### Learning outcomes

You will (1) analyse transaction-ordering risks conceptually; (2) study key-management incidents at a high level; (3) relate advanced cases to small systems.

### 31.1 Transaction ordering

On public ledgers, the order of transactions within a block is chosen by the block producer, and others can see pending transactions before they are included. Daian and colleagues' 2020 study, Flash Boys 2.0, documented how this visibility lets automated agents profit by reordering or inserting transactions, harming ordinary users and potentially the stability of consensus. Sofia studies the paper conceptually. She notes the cooperative's permissioned ledger has only three known validators and no open trading, so this risk is much smaller, but any future connection to public markets would bring it into scope and require fresh analysis.

### 31.2 Key-management incidents

Many large losses in the cryptoasset field have involved the compromise or misuse of keys controlling privileged functions, rather than flaws in contract logic. Sofia reads public summaries at a high level only, noting patterns: too few signers, keys held on internet-connected machines, and no delay before privileged actions took effect. She compares these patterns with the cooperative's design: three keyholders on hardware devices, a 2-of-3 threshold and timelocks on administration. She concludes the design addresses the main patterns, while recognising that people can still be deceived into signing, so batch summaries remain essential.

### 31.3 Relating cases to small systems

Advanced cases from large systems can seem irrelevant to a 900-member cooperative, but their lessons scale down. Transaction-ordering research teaches that visible pending actions can be exploited, so the cooperative should not reveal planned batches publicly in advance. Key incidents teach that signing processes need clear information and independent checks. Sofia writes a one-page note for the board summarising three lessons and the corresponding controls. Dr Asante praises her for drawing lessons without copying details that could be misused. Learning from others' incidents is cheaper than learning from one's own.

### Worked example

Sofia relates Flash Boys 2.0 and key-incident patterns to the cooperative, keeping batches unannounced and relying on hardware keys, 2-of-3 signing and summaries.

> **Synthetic case.** The cooperative's analysis is synthetic; Daian et al. (2020) is a real source.

### Errors and limits

Dismissing large-system incidents as irrelevant misses lessons that apply at small scale.

### Exercises

- **EX091 — Ordering study.** Which 2020 study documented transaction reordering? *Rubric:* 3 = Daian et al., Flash Boys 2.0;; 2 = Flash Boys 2.0;; 1 = Nakamoto;; 0 = none.
- **EX092 — Key incident pattern.** Name one pattern in key-related losses. *Rubric:* 3 = too few signers;; 2 = keys on connected machines;; 1 = strong timelocks;; 0 = none.
- **EX093 — Ordering lesson applied.** How does the cooperative apply the ordering lesson? *Rubric:* 3 = do not announce planned batches publicly;; 2 = keep batches private;; 1 = publish batches;; 0 = none.

### Synthesis

Advanced cases teach scalable lessons about ordering, keys and signing processes.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Web3, blockchain and cryptoasset security: interdisciplinary interfaces

### Learning outcomes

You will (1) connect security with law and governance; (2) consider economics and incentives; (3) involve users and communities.

### 32.1 Law and governance

Token systems sit within legal and governance frameworks. The cooperative's vouchers are a membership benefit, not an investment, and its lawyer confirmed they are redeemable only at the shop. Sofia learns that legal classification shapes duties, such as record keeping and consumer protection. Governance defines who decides: the board approves policy, members vote on major changes and keyholders act on board decisions. She maps each security control to its governance owner. Clear governance ensures controls have authority behind them and that emergency actions, like pausing, are accountable to members afterwards.

### 32.2 Economics and incentives

Security depends on incentives. Volunteers serve as keyholders out of goodwill, so the cooperative must keep their burden reasonable. Members might be tempted to record extra shifts if vouchers were valuable enough, so the weekly cap and coordinator approval limit the incentive. Sofia considers whether vouchers could be traded outside the cooperative; the contract allows member-to-member transfers, which could create an informal market. The board decides to monitor this rather than restrict it immediately. Thinking about incentives helps predict behaviour that pure technical analysis would miss, both from honest members and from occasional opportunists.

### 32.3 Users and communities

Sofia runs two short sessions with members at the shop, explaining wallets, backups and how to recognise suspicious messages asking for keys. Older members prefer the custodial option, while younger members value self-custody. She collects feedback that the wallet's recovery process is confusing, and the cooperative produces a simple printed guide. Users are part of the security system, and their understanding and trust determine whether controls succeed. Involving the community also brings ideas Sofia had not considered, such as a volunteer helper available at the shop each Saturday morning.

### Worked example

Sofia maps controls to governance owners, monitors informal voucher trading and adds a printed recovery guide after member feedback.

> **Synthetic case.** The governance, incentives and sessions are synthetic.

### Errors and limits

Ignoring incentives misses behaviour that technical analysis alone cannot predict.

### Exercises

- **EX094 — Voucher classification.** How are the vouchers classified? *Rubric:* 3 = a membership benefit redeemable only at the shop;; 2 = membership benefit;; 1 = an investment;; 0 = none.
- **EX095 — Incentive control.** What limits the incentive to record extra shifts? *Rubric:* 3 = the weekly cap and coordinator approval;; 2 = cap;; 1 = nothing;; 0 = none.
- **EX096 — Member feedback.** What feedback did members give? *Rubric:* 3 = the recovery process was confusing;; 2 = recovery;; 1 = vague;; 0 = none.

### Synthesis

Law, governance, economics and community engagement shape whether security works in practice.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse data with appropriate statistics; (2) assess reliability of coding; (3) report results with limitations.

### 33.1 Analysing the mismatch data

Sofia returns to her research question with a year of synthetic reconciliation logs. She finds 14 mismatch events across 52 weeks. She classifies their causes: 6 late approvals, 4 extract timing gaps, 3 data-entry errors and 1 duplicated batch. She reports counts and proportions and plots mismatches over time, noting fewer after hourly reconciliation began. She avoids claiming the change caused the improvement, since other changes happened at the same time, such as new coordinator training. Careful analysis distinguishes what the data show from what one might hope they show.

### 33.2 Reliability of coding

Classifying causes involves judgement, so Sofia asks a classmate to classify the 14 events independently using the same definitions. They agree on 12. She calculates Cohen's kappa, a measure of agreement beyond chance, and interprets the result using Landis and Koch's 1977 guidelines, which describe ranges from slight to almost perfect agreement. They discuss the two disagreements and refine one definition. Checking reliability shows that her classification is not just personal opinion. Reporting the agreement figure lets readers judge how much weight to give her categories and conclusions.

### 33.3 Reporting with limitations

Sofia's report states its limitations: one year of data, a single cooperative, synthetic logs prepared for the course, and possible confounding from training changes. She explains how each limits the conclusions. She recommends the cooperative continue collecting data so later analysis can test whether hourly reconciliation truly reduces mismatches. Stating limitations openly strengthens a report, because readers can trust that the author has considered what could be wrong. Dr Asante says that a modest, well-supported conclusion is more valuable than a dramatic one that collapses under questioning by assessors.

### Worked example

Sofia classifies 14 mismatches (6 late approvals, 4 timing gaps, 3 entry errors, 1 duplicate), agrees on 12 of 14 with a classmate and reports limitations.

> **Synthetic case.** The logs and coding are synthetic; Landis and Koch (1977) is a real source.

### Errors and limits

Claiming a change caused an improvement ignores other changes happening at the same time.

### Exercises

- **EX097 — Mismatch count.** How many mismatch events were found in the year? *Rubric:* 3 = 14;; 2 = fourteen;; 1 = 52;; 0 = none.
- **EX098 — Coding agreement.** On how many events did the classifiers agree? *Rubric:* 3 = 12 of 14;; 2 = 12;; 1 = all;; 0 = none.
- **EX099 — Confounder.** What confounds the improvement after hourly reconciliation? *Rubric:* 3 = new coordinator training at the same time;; 2 = training;; 1 = nothing;; 0 = none.

### Synthesis

Careful analysis, reliability checks and stated limits make research conclusions trustworthy.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare design options against criteria; (2) gather evidence for each option; (3) recommend with justification.

### 34.1 Framing the comparison

The board asks whether the cooperative should keep its permissioned ledger or move vouchers to an ordinary database with signed audit logs. Sofia frames a comparison against agreed criteria: integrity of records, privacy, cost, operational burden on volunteers, member trust and ability to recover from errors. Each criterion has a weight agreed with the board before any option is scored, so the result cannot be tuned to favour a preferred answer. Framing the comparison carefully ensures the decision rests on the cooperative's priorities rather than on enthusiasm for any particular technology.

### 34.2 Gathering evidence

For each option Sofia gathers evidence: costs from hosting invoices, volunteer time from the operations log, integrity from reconciliation results, privacy from her data map and member trust from a short survey. The ledger scores higher on shared tamper evidence and member trust; the database scores higher on privacy, cost and ease of correcting errors. She cites NIST IR 8202's guidance that organisations should consider whether a blockchain is needed at all. Gathering evidence for both options fairly prevents the comparison from becoming a defence of the existing choice.

### 34.3 Recommending with justification

The weighted scores are close: 3.6 for the ledger and 3.4 for the database. Sofia tests sensitivity: if privacy's weight rises slightly, the database wins. She recommends keeping the ledger for now, because members value shared records, while reducing data on it further and reviewing the decision in two years. She presents the closeness openly so the board understands that the choice is a judgement, not an obvious answer. The board accepts the recommendation and records its reasoning, including the review date, in the decision records.

### Worked example

Weighted scores of 3.6 for the ledger and 3.4 for the database lead Sofia to recommend keeping the ledger, with less data and a two-year review.

> **Synthetic case.** The comparison and scores are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Setting weights after scoring lets a comparison be tuned to a preferred answer.

### Exercises

- **EX100 — Alternative option.** What alternative to the ledger is compared? *Rubric:* 3 = an ordinary database with signed audit logs;; 2 = database;; 1 = public chain;; 0 = none.
- **EX101 — Weighted scores.** What weighted scores did the options receive? *Rubric:* 3 = 3.6 ledger, 3.4 database;; 2 = 3.6/3.4;; 1 = equal;; 0 = none.
- **EX102 — Sensitivity result.** What does the sensitivity test show? *Rubric:* 3 = a slightly higher privacy weight favours the database;; 2 = privacy shifts it;; 1 = no change;; 0 = none.

### Synthesis

Fair evidence, pre-agreed weights and sensitivity testing support honest recommendations.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) define a capstone problem and objectives; (2) plan methods and evaluation; (3) manage scope and risk.

### 35.1 Choosing the capstone

For her capstone Sofia proposes to build a monitoring service for the cooperative that checks the voucher ledger against its invariants and the shift database every hour, alerts volunteers to mismatches and privileged actions, and produces a monthly report. The problem is clear: current checks are spread across scripts and manual steps. Objectives are measurable: detect all seeded mismatches in test data, alert within ten minutes, and reduce weekly routine time by a third. Dr Asante approves the proposal, noting that it builds directly on her earlier labs and research.

### 35.2 Methods and evaluation

Sofia plans to build the service with Python's standard library and read-only access to a validator and the reporting database. She will evaluate it with synthetic datasets containing seeded mismatches, measure detection and alert time, and ask volunteers to rate its usefulness after a month of use. She defines success before starting, so results cannot be reinterpreted later. Evaluation also includes checking false alarms, because a monitor that alerts too often will be ignored. The plan lists each evaluation step with its expected output and the evidence it will produce.

### 35.3 Scope and risk

Sofia limits scope: the service will only read data and send alerts, never change the ledger or database. Features such as automatic pausing are excluded, because they would require write access and careful governance. She lists project risks: delays in getting test data, volunteer availability for evaluation and her own exam schedule. For each she plans a response, such as preparing synthetic data herself if needed. Clear scope protects both the cooperative and the project timeline, and read-only design means a bug in her service cannot alter any member's balance.

### Worked example

Sofia proposes a read-only hourly monitor with targets of detecting all seeded mismatches, alerting within ten minutes and cutting routine time by a third.

> **Synthetic case.** The capstone proposal is synthetic.

### Errors and limits

Giving a student monitoring project write access adds risk without adding needed function.

### Exercises

- **EX103 — Capstone objective.** Name one measurable objective. *Rubric:* 3 = alert within ten minutes;; 2 = detect all seeded mismatches;; 1 = be fast;; 0 = none.
- **EX104 — Excluded feature.** Which feature is excluded and why? *Rubric:* 3 = automatic pausing, needing write access;; 2 = auto-pause;; 1 = reporting;; 0 = none.
- **EX105 — False alarm concern.** Why evaluate false alarms? *Rubric:* 3 = a monitor that alerts too often is ignored;; 2 = alert fatigue;; 1 = irrelevant;; 0 = none.

### Synthesis

Clear objectives, pre-defined evaluation and tight scope make a capstone achievable.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) work within a real organisation's constraints; (2) communicate with non-technical staff; (3) reflect on practice.

### 36.1 Working within constraints

Sofia spends a term working two days a week with the cooperative. She learns its constraints: limited money, volunteers with changing availability, an old office computer and a board that meets monthly. She adapts. Documentation is kept short and printed, meetings are scheduled around the shop's busy hours and changes are bundled into the monthly board meeting rather than requested ad hoc. She learns that security in a small organisation succeeds when it respects these realities, and that recommendations ignoring them are politely accepted and then quietly forgotten by everyone involved.

### 36.2 Communicating with staff

The shop manager asks why the till sometimes shows a balance that differs from the member's wallet for a few seconds. Sofia explains that the till reads from a validator that may be one block behind, and that the difference resolves quickly. She suggests a small message on the till screen. Explaining in plain words, with an everyday comparison to a bank card payment showing as pending, builds trust. She keeps a list of questions staff ask and turns the most common into a one-page frequently asked questions sheet kept beside the till.

### 36.3 Reflecting on practice

Each week Sofia writes a short reflection: what happened, what she learned and what she would do differently. She notices that her early recommendations were too technical and that people engaged more when she began with the problem they experienced. She also reflects on ethical moments, such as declining to look at a member's transaction history out of curiosity. Reflection turns experience into lasting learning. Dr Asante reads the reflections monthly and comments on them, and they become part of her assessed portfolio for the field practice module.

### Worked example

Sofia adapts to monthly board cycles, explains till lag with a pending-payment comparison and records weekly reflections.

> **Synthetic case.** The placement and conversations are synthetic.

### Errors and limits

Recommendations that ignore an organisation's constraints are accepted and then forgotten.

### Exercises

- **EX106 — Till difference.** Why does the till briefly differ from the wallet? *Rubric:* 3 = the validator may be one block behind;; 2 = lag;; 1 = theft;; 0 = none.
- **EX107 — Explanation comparison.** What everyday comparison does Sofia use? *Rubric:* 3 = a bank card payment showing as pending;; 2 = pending payment;; 1 = a recipe;; 0 = none.
- **EX108 — Reflection insight.** What did reflection show about early recommendations? *Rubric:* 3 = they were too technical;; 2 = too technical;; 1 = perfect;; 0 = none.

### Synthesis

Respecting constraints, communicating plainly and reflecting turn practice into learning.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critique published evidence; (2) compare studies fairly; (3) apply evidence to practice decisions.

### 37.1 Critiquing published evidence

In a seminar, Sofia's group critiques Durieux and colleagues' 2020 tool evaluation. They ask: what contracts were used, how were weaknesses confirmed, what counted as a correct detection, and could the results generalise to other contracts or newer tools? They note strengths, such as a large dataset and published materials, and limitations, such as the difficulty of knowing the true set of weaknesses. Critique does not mean dismissing a study; it means understanding exactly what it shows. Each student writes a one-page critique following a common structure provided by Dr Asante.

### 37.2 Comparing studies fairly

The group compares Durieux and colleagues' findings with Perez and Livshits' 2021 study of whether reported weaknesses were exploited. The studies ask different questions: one about tool accuracy, the other about real-world exploitation. Sofia notes that combining them suggests tools flag many issues, some of which are false or unexploited, while still missing others. Fair comparison respects each study's design and does not force agreement where questions differ. The group writes a short synthesis noting where the evidence agrees, where it differs and where it is silent.

### 37.3 Applying evidence to decisions

The cooperative asks whether to buy a commercial analysis service. Sofia uses the seminar's synthesis: tools catch some issues but miss others, so any service should complement, not replace, manual review and testing. Given the contract's small size and the cooperative's budget, she recommends one external manual review before major changes rather than a subscription. She cites the studies in her recommendation. Applying evidence to decisions is the purpose of reviewing it, and she records the decision and evidence together for later reference by the board.

### Worked example

Sofia's group critiques Durieux et al. and compares it with Perez and Livshits, leading her to recommend one external manual review before major changes.

> **Synthetic case.** The seminar and recommendation are synthetic; Durieux et al. (2020) and Perez and Livshits (2021) are real sources.

### Errors and limits

Forcing studies with different questions into agreement misrepresents both.

### Exercises

- **EX109 — Critique question.** Name one question asked of the tool study. *Rubric:* 3 = how weaknesses were confirmed;; 2 = what contracts were used;; 1 = who funded the seminar;; 0 = none.
- **EX110 — Study difference.** How do the two studies differ? *Rubric:* 3 = tool accuracy versus real-world exploitation;; 2 = different questions;; 1 = identical;; 0 = none.
- **EX111 — Service recommendation.** What does Sofia recommend instead of a subscription? *Rubric:* 3 = one external manual review before major changes;; 2 = manual review;; 1 = buy the service;; 0 = none.

### Synthesis

Fair critique and synthesis of evidence support practical security decisions.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) implement a read-only monitoring service; (2) test it with seeded data; (3) document operation for volunteers.

### 38.1 Building the monitor

Sofia implements the monitor as a small Python program using only the standard library. Every hour it reads new ledger events from a validator through a read-only interface, reads approved shifts from the reporting database, recomputes balances by replaying events, checks the invariants, and compares issuance with approved shifts. It also lists any privileged action, such as a role change or pause. Results are written to a dated log, and alerts are sent by email to the duty volunteer. The code is reviewed by a classmate and by the cooperative's developer before use.

### 38.2 Testing with seeded data

Sofia prepares synthetic datasets with seeded problems: a missing issuance event, a balance mismatch, an issuance without an approved shift, an unexpected role change and a duplicated batch. The monitor detects all five and alerts within six minutes of each hourly run. She also runs it on a clean month of data, where it raises no alerts. A first version raised a false alarm when a shift was approved after midnight; she fixed the date logic and reran all tests. Seeded testing gives clear evidence that the monitor detects what it should.

### 38.3 Documenting operation

Sofia writes a two-page guide for volunteers: what the monitor checks, what each alert means, the first steps for each, and who to contact. Each alert type links to the relevant part of the incident plan. She also documents how to restart the monitor, where logs are kept and how to update the list of privileged functions. A volunteer with no programming background follows the guide successfully during a trial. Documentation makes the service maintainable after Sofia graduates, which the board had specifically asked for when approving her capstone.

### Worked example

The monitor detects all five seeded problems within six minutes, raises no alerts on a clean month, and a fixed midnight date bug removes a false alarm.

> **Synthetic case.** The monitor, datasets and trial are synthetic.

### Errors and limits

Testing only with clean data cannot show whether a monitor detects real problems.

### Exercises

- **EX112 — Seeded problems.** How many seeded problems did the monitor detect? *Rubric:* 3 = all five;; 2 = five;; 1 = three;; 0 = none.
- **EX113 — False alarm cause.** What caused the early false alarm? *Rubric:* 3 = a shift approved after midnight;; 2 = date logic;; 1 = network;; 0 = none.
- **EX114 — Guide test.** Who successfully followed the guide? *Rubric:* 3 = a volunteer without programming background;; 2 = a volunteer;; 1 = only Sofia;; 0 = none.

### Synthesis

A reviewed, seeded-tested and documented monitor can outlast its builder.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against objectives; (2) gather user feedback; (3) identify improvements and limits.

### 39.1 Evaluating against objectives

Sofia evaluates the monitor against her proposal. It detected all seeded mismatches, meeting the first objective. Alerts arrived within six minutes, meeting the ten-minute target. Weekly routine time fell from thirty to eighteen minutes, a reduction of 40 percent, exceeding the target of a third. She presents each result with its evidence: test logs, alert timestamps and volunteers' routine logs. Measuring against pre-defined objectives makes the evaluation honest, because she cannot redefine success after seeing the results, and the board can check every claim against the stored evidence.

### 39.2 User feedback

After a month of use, five volunteers rate the monitor. Four find it useful and one finds the email alerts too frequent during the first week, when several late approvals caused alerts. Sofia adjusts the rule so that a mismatch caused by a shift approved within the past 24 hours produces a note in the daily summary rather than an immediate alert. Feedback shows that good technical results do not guarantee a good user experience. She records each piece of feedback and her response, so future maintainers understand why the rules are set the way they are.

### 39.3 Improvements and limits

Sofia lists improvements for the future: a simple web dashboard, checks on validator health and integration with the cooperative's calendar for keyholder availability. She also states limits: the monitor depends on one validator for data; it cannot detect problems in data that never reach the database; and it was evaluated for only one month. She recommends a second data source and a longer evaluation. Being clear about limits helps the cooperative decide how much to rely on the monitor, and it shows assessors a mature understanding of evaluation.

### Worked example

The monitor meets all objectives, cutting routine time 40 percent, and feedback leads to recent-approval mismatches being moved to the daily summary.

> **Synthetic case.** The evaluation and feedback are synthetic.

### Errors and limits

Judging success only on technical tests misses whether users find a tool usable.

### Exercises

- **EX115 — Routine reduction.** By how much did weekly routine time fall? *Rubric:* 3 = from thirty to eighteen minutes, 40 percent;; 2 = 40 percent;; 1 = 10 percent;; 0 = none.
- **EX116 — Rule adjustment.** How was the alert rule adjusted? *Rubric:* 3 = recent-approval mismatches go to the daily summary;; 2 = summary note;; 1 = removed alerts;; 0 = none.
- **EX117 — Stated limit.** Name one limit of the monitor. *Rubric:* 3 = depends on one validator for data;; 2 = one-month evaluation;; 1 = vague;; 0 = none.

### Synthesis

Objective-based evaluation, user feedback and stated limits complete a capstone honestly.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write a bachelor's thesis from project evidence; (2) present to a mixed audience; (3) hand over responsibly.

### 40.1 Writing the thesis

Sofia's thesis argues that a small community organisation can operate a voucher ledger safely if it combines simple contract rules, careful key management, independent reconciliation and volunteer-friendly operations. Chapters cover the cooperative, the system model, controls, research on mismatches, the comparison with a database and the monitoring capstone. Each claim cites evidence from her logs and tests or from verified sources such as NIST IR 8202, the OWASP Smart Contract Top 10 and EEA EthTrust. Dr Asante reviews each draft chapter and marks any claim that lacks clear evidence or a citation.

### 40.2 Presenting to a mixed audience

Sofia presents to assessors and to the cooperative's board. She uses one diagram of the system, three key results and one honest limitation, avoiding dense slides. Assessors ask why she kept the ledger when the database scored nearly as well; she explains the members' preference for shared records and the planned review. A board member asks what happens after she graduates; she points to the handover plan. Answering in plain language for both audiences shows real understanding. The assessors award a high grade, noting the quality of her evidence and her clear writing.

### 40.3 Responsible handover

Sofia hands over the monitor, documentation, test datasets and decision records to the cooperative's developer and two trained volunteers. She removes her own access, confirms the keyholder list is current, and schedules a check-in three months later. She writes a final note to members thanking them and explaining what the project changed. Reflecting on four years, she notes that the most valuable skills were clear reasoning, honest evidence and working respectfully with people. The degree ends with a working system, trained volunteers and her access properly removed.

### Worked example

Sofia's thesis argues safe small-scale operation from evidence, her presentation answers the ledger-versus-database question, and she removes her own access at handover.

> **Synthetic case.** The thesis, presentation and handover are synthetic; NIST IR 8202, OWASP SC Top 10 and EEA EthTrust are real sources.

### Errors and limits

Leaving a graduate's access in place after handover creates an unmanaged privileged account.

### Exercises

- **EX118 — Thesis argument.** What does the thesis argue? *Rubric:* 3 = a small organisation can run a voucher ledger safely with rules, keys, reconciliation and friendly operations;; 2 = combined controls;; 1 = blockchains are always safe;; 0 = none.
- **EX119 — Assessor question.** What did assessors ask about the ledger choice? *Rubric:* 3 = why keep it when the database scored nearly as well;; 2 = ledger versus database;; 1 = its colour;; 0 = none.
- **EX120 — Handover step.** Name one handover step. *Rubric:* 3 = remove her own access;; 2 = schedule a three-month check-in;; 1 = keep admin rights;; 0 = none.

### Synthesis

An evidence-based thesis, clear presentation and responsible handover complete the degree.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Sofia Lindqvist, Dr Kwame Asante, Harrowgate University, Lantern Hill Food Cooperative and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About 900 members.

**EX002.** A recorded shift does not guarantee a voucher, because approval may still be pending.

**EX003.** Circulation equals vouchers issued minus vouchers redeemed.

**EX004.** Three validator nodes on small rented servers.

**EX005.** The Ethereum Virtual Machine executes deterministically, so identical inputs give identical results.

**EX006.** If nodes are down and vouchers cannot be spent, members lose trust as they would after a theft.

**EX007.** It is allowed and leaves a balance of zero.

**EX008.** Subtracting a negative amount would increase the balance silently.

**EX009.** Refuse the action with a clear reason instead of guessing.

**EX010.** A permissioned ledger may help if members want shared tamper-evident records, though a database might suffice.

**EX011.** Nakamoto's 2008 paper and NIST IR 8202.

**EX012.** As the secret that proves who may spend vouchers.

**EX013.** Confidentiality, because every node holds a copy of the records.

**EX014.** Vouchers, private keys, the member list or the cooperative's reputation.

**EX015.** A daily comparison of vouchers issued against approved shifts.

**EX016.** As a function from member codes to non-negative whole-number balances.

**EX017.** 18,000 vouchers, from 900 members times 20.

**EX018.** Three pairs, so one lost keyholder still leaves a working pair.

**EX019.** So faults can be located, for example a transport-layer firewall rather than a ledger bug.

**EX020.** A node with too few peers may fall behind because it learns only from them.

**EX021.** Each validator connects to the other two and refuses unknown peers.

**EX022.** A set of already rewarded shifts checked before any voucher is issued.

**EX023.** Decimal amounts were rounded silently instead of being refused.

**EX024.** Validated inputs, tested edges, clear names, single-purpose functions, or repeated actions.

**EX025.** A shift row that refers to a member who does not exist.

**EX026.** By using parameterised queries that pass values separately from the query text.

**EX027.** A hash of each week's approved shift list, not its contents.

**EX028.** Members' devices, the payment terminal or any public blockchain.

**EX029.** Report it to the board instead of investigating it.

**EX030.** A coordinator's email address in a test configuration file, reported privately.

**EX031.** As a dedicated unprivileged user limited to its configuration and data folder.

**EX032.** Key-based administrative login with password login turned off.

**EX033.** So the ledger continues on the remaining two validators if an update fails.

**EX034.** Usually between 4,000 and 7,000 vouchers a week.

**EX035.** About 4 percent, from 2 mismatching weeks out of 52.

**EX036.** When real problems are rare, even a small false-alarm rate yields mostly false alarms.

**EX037.** By signing a transaction with their private key.

**EX038.** Convenience comes at the cost of concentrating risk with the cooperative.

**EX039.** A timelock, so role changes are visible before they take effect.

**EX040.** They reveal when a member is likely to be away from home.

**EX041.** Removing unused birth dates or deleting shift notes after a year.

**EX042.** Ledger codes differ from database codes, with the link kept under access control.

**EX043.** Matched percentage, monthly mismatches, validator restore time or unapproved privileged actions.

**EX044.** By storing a SHA-256 hash of each extract file.

**EX045.** Twenty were late approvals and two were data-entry errors.

**EX046.** The issuing service verifies each approval before requesting a mint.

**EX047.** If one person held both, two layers would collapse into one.

**EX048.** Members wanted low costs and controlled participation, accepting validator operation.

**EX049.** 64 hexadecimal characters.

**EX050.** It does not prove the key holder acted wisely or that the key was not stolen.

**EX051.** V002, whose amount changed from 10 to 100.

**EX052.** How often cooperative records and ledger balances disagree, and why.

**EX053.** Log analysis supported by short consented interviews.

**EX054.** Interviews must avoid discussing any named member.

**EX055.** Ledgers, keys and wallets, off-chain services or people and processes.

**EX056.** At least two of the three validators.

**EX057.** In keys, the issuing service and the contract's role logic.

**EX058.** The 2017 survey by Atzei, Bartoletti and Cimoli.

**EX059.** Assumptions about timing or callers must be checked in code.

**EX060.** By reading the design and testing expected behaviour on the test ledger with synthetic data.

**EX061.** Whether redemption was allowed while the contract was paused.

**EX062.** Supply equals the sum of balances, no negative balance, cap respected or only minter increases supply.

**EX063.** Their approvals cause vouchers to be minted, though they cannot mint directly.

**EX064.** The issuing service, whose wrong output keyholders might sign unnoticed.

**EX065.** Because outdated compilers appear as a weakness class in the SWC registry.

**EX066.** Stop the issuing service and mint manually with extra checks.

**EX067.** The OWASP Smart Contract Top 10 and the SWC registry.

**EX068.** Meeting its requirements does not guarantee a contract is free of weaknesses.

**EX069.** A cap-change function emitting no event and an unpinned compiler version.

**EX070.** Hardware devices, a 2-of-3 multisig or documented recovery.

**EX071.** So volunteer keyholders can plan, avoiding nightly delays.

**EX072.** One keyholder's device needed a firmware update before it would sign.

**EX073.** Issuance of new vouchers.

**EX074.** 110 from the replay and 115 in the snapshot.

**EX075.** The extract ended one block early, missing a valid issuance.

**EX076.** Tools often disagreed, each missed many issues and some reported false positives.

**EX077.** Two already fixed, two false positives and one new finding.

**EX078.** Many reported weaknesses in deployed contracts were never exploited, so risk depends on context.

**EX079.** Non-minter issuance, transfer while paused or a mint exceeding the cap.

**EX080.** So mistakes during testing cannot affect real members or funds.

**EX081.** By comparing the deployed contract's code hash with the tested build.

**EX082.** 310 extra vouchers.

**EX083.** The issuing service lacked a check that a week had already been processed.

**EX084.** The weekly cap limited it and daily reconciliation detected it.

**EX085.** About thirty minutes.

**EX086.** An unexplained reconciliation mismatch above 50 vouchers.

**EX087.** No one knew who should inform members, so a communications lead was named.

**EX088.** Four checks.

**EX089.** The mint timelock is 24 hours, below the 48-hour policy.

**EX090.** Do not deploy until both issues are fixed.

**EX091.** Daian and colleagues' 2020 study, Flash Boys 2.0.

**EX092.** Too few signers, keys on internet-connected machines or no delay on privileged actions.

**EX093.** By not revealing planned mint batches publicly in advance.

**EX094.** As a membership benefit redeemable only at the cooperative shop.

**EX095.** The weekly cap and coordinator approval of shifts.

**EX096.** That the wallet's recovery process was confusing.

**EX097.** 14 mismatch events across 52 weeks.

**EX098.** They agreed on 12 of the 14 events.

**EX099.** New coordinator training happened at the same time.

**EX100.** An ordinary database with signed audit logs.

**EX101.** 3.6 for the ledger and 3.4 for the database.

**EX102.** If privacy's weight rises slightly, the database option wins.

**EX103.** Detect all seeded mismatches, alert within ten minutes or cut routine time by a third.

**EX104.** Automatic pausing, because it would require write access and careful governance.

**EX105.** Because a monitor that alerts too often will be ignored.

**EX106.** The till reads from a validator that may be one block behind.

**EX107.** A bank card payment that shows as pending.

**EX108.** They were too technical; starting from people's problems worked better.

**EX109.** What contracts were used, how weaknesses were confirmed, what counted as detection, or generalisability.

**EX110.** One studies tool accuracy, the other real-world exploitation of reported weaknesses.

**EX111.** One external manual review before major changes.

**EX112.** All five seeded problems.

**EX113.** A shift approved after midnight confused the date logic.

**EX114.** A volunteer with no programming background.

**EX115.** From thirty to eighteen minutes, a 40 percent reduction.

**EX116.** Mismatches from shifts approved in the last 24 hours go to the daily summary instead of an alert.

**EX117.** Reliance on one validator, blindness to data missing from the database, or a one-month evaluation.

**EX118.** Safe operation is possible by combining simple rules, key management, reconciliation and volunteer-friendly operations.

**EX119.** Why she kept the ledger when the database scored nearly as well.

**EX120.** Removing her access, confirming keyholders, scheduling a check-in or handing over documentation.

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
