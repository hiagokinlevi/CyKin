# Authorized Offensive Security and Red Team: A Bachelor's Course Book

- Language: English (`en`); bachelor's course, four years; approximately 3,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: broad security and computing students.
- Relation to neighbouring books: the [engineering book](../../../../engineering-5-years/offensive-security-red-team/en/book/MANUSCRIPT.md) emphasises building assessment platforms; the [technologist book](../../../../technologist-3-years/offensive-security-red-team/en/book/MANUSCRIPT.md) emphasises implementation. **This book joins theory, cases, labs and a capstone.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. **No authority to test real systems.** All organisations, people and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, measurement and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–18 build mathematical, computing, writing, ethics and security foundations; 19–30 are the authorized-testing core with laboratories; 31–40 cover advanced cases, research, comparative work, field practice, seminars and the capstone thesis. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, three exercises scored 0–3, a synthesis and a **Continue studying** block. Labs read local data only (`python3 file.py`).

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Riverstone Transit Bank (TRB)** — online banking, ledger, SWIFT gateway (excluded), assessment platform TrackScope / FindingsDesk / PulseMap | Organisation studied throughout | Invented |
| **Sam Ito** | Engineering intern on the authorized assessment platform team | Invented |

### Core sources

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) use sets and logic to describe scope; (2) apply counting to coverage; (3) spot invalid inferences in a security argument.

### 1.1 Sets for scope

A written authorization is a set of systems. Membership is binary for each target: in scope or not. Unions of ranges and exclusions (subtracted sets) are how Riverstone Transit Bank (TRB) writes its ROE. If SWIFT sits in the same /26 as a web host, exclusion is set difference, not a vague note.

### 1.2 Logic of authorization

Permission is necessary for testing; it is not sufficient for every method. \"In scope\" and \"method allowed\" must both be true. Confusing the two leads to unauthorized techniques on authorized hosts.

### 1.3 Counting coverage

If 40 hosts are in scope and 28 were touched by method cards, coverage is 28/40. Percentages without denominators mislead examiners and boards.

### 1.4 Invalid leaps

\"The scanner found nothing, so we are safe\" confuses absence of evidence with evidence of absence. Wilson intervals in Chapter 12 make small-sample humility numerical.

### 1.5 Practice

Sam Ito, engineering intern on TRB's authorized assessment platform team, translates every ROE sentence into sets before any tool runs.

### 1.6 Why maths here

Later chapters on probability, architecture and evaluation reuse the same careful language. Sloppy scope language produces sloppy tests.

### 1.7 1.7 Applied note

Sam practices translating ROE paragraphs into membership tests on paper before opening TrackScope. When a sentence says "web VLAN except payment gateways", he writes the set expression and lists every known gateway address from the asset register. Only then does he load the scope file. Contractors who skip the paper step regularly propose hosts that sit beside SWIFT "because the ping worked". The paper step is slower and prevents newspaper incidents.

### 1.8 1.8 Worked set arithmetic

Given VLAN V and exclusions E, Sam computes V\E and then intersects with the day's proposed list P. Only P∩(V\E) may be loaded. He unit-tests the calculator with SWIFT inside V and confirms it never appears in output.

### 1.9 1.11 Scene

On Monday Sam receives a spreadsheet of "interesting hosts" from a branch IT lead. He does not import it. He rebuilds scope from the signed ROE: the /26, minus SWIFT at .20, intersected with hosts that have owners in the asset register. Three spreadsheet rows vanish as out of scope; one vanishes as excluded. He sends the filtered list back with the set expression in the email. The branch lead is annoyed for ten minutes and grateful when a fourth row is recognised as a mis-typed payment console. Paper set arithmetic scales better than trust.

### Worked example (synthetic TRB)

Sam writes SCOPE = 198.51.100.0/26 minus {198.51.100.20}. A proposed host 198.51.100.70 fails membership; he rejects it before the kickoff call.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX001 — Set difference.** Express TRB's web VLAN scope with SWIFT excluded as a set operation. *Rubric:* 3 = VLAN set minus {SWIFT}; 2 = partial; 1 = union; 0 = none.
- **EX002 — Necessary vs sufficient.** Why is \"host in scope\" not enough to run password spraying? *Rubric:* 3 = method must also be allowed; spraying may be forbidden; 2 = partial; 1 = it is enough; 0 = none.
- **EX003 — Coverage fraction.** 28 of 40 hosts touched — write the coverage and one misuse of \"70%\". *Rubric:* 3 = 28/40=0.7; misuse e.g. implying safety; 2 = fraction only; 1 = wrong; 0 = none.

### Synthesis

Scope is set membership; methods need their own truth; coverage needs denominators.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) map TRB's computing layers; (2) place the assessment platform; (3) explain why ledger hosts differ from web hosts.

### 2.1 Layers

Branches use thin clients; staff use managed PCs; apps run on VMs; the ledger sits on hardened hosts with change control measured in weeks. Testers who treat every host like a lab VM cause outages.

### 2.2 Assessment platform

TrackScope (scope checker), FindingsDesk (tickets) and PulseMap (ATT&CK coverage) are TRB's synthetic platform Sam helps build. They run on isolated infrastructure and must fail closed on scope.

### 2.3 Trust boundaries

Internet to web tier, web to core API, jump hosts to ledger-adjacent admin — each crossing is a place findings appear.

### 2.4 Fragility

Ledger and SWIFT-adjacent systems are usually out of ordinary pentest scope or gated by extreme controls. NIST SP 800-115 still applies to planning even when technical intensity is low.

### 2.5 Inventory drift

Cloud projects add tenants faster than diagrams update. Authorized testing against stale diagrams is a process finding.

### 2.6 Practice rule

Sam never assumes a hostname's layer from its name alone; he checks the asset register.

### 2.7 2.7 Applied note

PulseMap's fail-closed rule is tested in CI by deleting the scope file and asserting every API returns deny. Sam added that test after a staging misconfiguration briefly served empty allow lists. Dashboards that cannot deny are worse than no dashboards. He demos the deny path to every new intern in their first week.

### 2.8 2.8 Platform zoning

TrackScope, FindingsDesk and PulseMap sit in an assessment zone with controlled conduits to staging only. Sam reviews those conduits each quarter the same way he reviews TRB business flows — because the platform can hurt the bank if miswired.

### 2.9 2.9 Denominator bug

A PulseMap bug once defaulted n to 1. Sam's regression test sets n=0 and expects an error tile, not 100%.

### 2.10 2.11 Scene

During a platform game day Sam kills the FindingsDesk database. TrackScope continues to deny out-of-scope requests using its local cache while queueing drafts to disk. PulseMap shows a degraded banner. No test traffic is allowed to "fail open" just because a ticket system is down. The game day note becomes a sales slide for why assessment tooling is safety tooling.

### Worked example (synthetic TRB)

Sam places PulseMap in the assessment VLAN, not on a branch PC image, so a compromised dashboard cannot mint scope files.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX004 — Fragile systems.** Name two TRB system classes usually out of ordinary test scope. *Rubric:* 3 = ledger and SWIFT-adjacent (or similar); 2 = one; 1 = website; 0 = none.
- **EX005 — Fail closed.** What should TrackScope do if the scope file will not load? *Rubric:* 3 = deny testing / fail closed; 2 = partial; 1 = allow all; 0 = none.
- **EX006 — Layer check.** How does Sam confirm a host's layer? *Rubric:* 3 = asset register / owner, not name guessing; 2 = partial; 1 = guess from name; 0 = none.

### Synthesis

Layers and fail-closed platform design keep authorized testing from becoming accidental production change.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write small Python tools for offline evidence; (2) refuse unsafe patterns; (3) test tools on synthetic data.

### 3.1 Purpose

Sam automates scope membership checks, hash verification and finding ranking — never exploitation.

### 3.2 Unsafe patterns

No hard-coded secrets, no disabled TLS verification, no unsanitised shell-outs to scanners, no retries without caps.

### 3.3 Synthetic first

Every tool runs on documentation-range addresses and fake files before any engagement window.

### 3.4 Review

A second engineer reads Sam's scripts for scope path mistakes.

### 3.5 Determinism

Seed randomness and pin interpreter versions so PulseMap demos are reproducible.

### 3.6 Course labs

Labs in this book follow these rules and embed real outputs.

### 3.7 3.7 Applied note

Dry-run output is pasted into the engagement channel before any write mode runs. Peers have two minutes to object. Sam once caught a path traversal into an evidence archive because a teammate read the dry-run carefully. Social review beats solitary cleverness for operational scripts.

### 3.8 3.8 Test data policy

Synthetic customers in fixtures use obviously fake national IDs. Sam rejects fixtures that reuse real-looking personal numbers even when unused in production. Habit transfer matters.

### 3.9 3.9 Secret scanning in CI

Platform repos fail CI if high-entropy strings look like keys. Sam whitelists only test fixtures clearly marked FAKE.

### 3.10 3.11 Scene

Sam's script review board hangs three rejected snippets: a requests call with verify=False, a subprocess with shell=True on a hostname, and a retry loop without jitter. New interns initial the board after reading it. The board is silly and effective. When Sam almost pastes verify=False "just in staging", he sees his own initials and stops.

### 3.11 3.20 Extra

Rejected snippet board gets a fourth example whenever CI catches a new anti-pattern. Sam dates each snippet. The board is a living museum of almost-mistakes.

### Worked example (synthetic TRB)

Sam's lab_scope.py uses only the ipaddress stdlib and documentation ranges; it never opens a socket.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX007 — Socket rule.** Why must lab_scope open no sockets? *Rubric:* 3 = offline/synthetic only; no accidental scan; 2 = partial; 1 = sockets fine; 0 = none.
- **EX008 — Two unsafe patterns.** Name two scripting patterns forbidden on the platform team. *Rubric:* 3 = two of secrets, TLS off, unsanitised shell, uncapped retries; 2 = one; 1 = none; 0 = none.
- **EX009 — Second reader.** What does the second reader look for? *Rubric:* 3 = scope path mistakes and secrets; 2 = one; 1 = style only; 0 = none.

### Synthesis

Programming here means safe, reviewed, synthetic-first automation.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write findings without blame; (2) separate facts from claims; (3) cite frameworks correctly.

### 4.1 Blame-free findings

\"Shared admin account on loan system\" beats \"lazy admins\". Boards fund fixes; insults create enemies.

### 4.2 Fact vs claim

Fact: web tier opened a TCP session to ledger-db. Claim: \"attackers can move money\" needs more evidence or is labelled speculative.

### 4.3 Citations

NIST SP 800-115, PTES, ATT&CK, OWASP WSTG, TIBER-EU and CBEST are cited with correct titles. Never invent DOIs.

### 4.4 Audience layers

Executives need decisions; engineers need reproduction; both need honesty about uncertainty.

### 4.5 Structure

Summary, scope/methods, findings, positives, limitations, appendices.

### 4.6 Revision

Peer review catches jargon and overclaim before the CISO sees the draft.

### 4.7 4.7 Applied note

Citation drills require opening the live NIST or PTES page, not a blog summary. Sam failed an early draft for citing a second-hand SP 800-115 paraphrase that invented a clause. Primary sources only — the same rule as never inventing DOIs.

### 4.8 4.8 Audience pass

Before sending, Sam reads the executive summary aloud to someone outside security. If they cannot restate the decision asked, he rewrites. Jargon surviving that pass is a defect.

### 4.9 4.9 Passive voice audit

Findings that hide actors in passive voice are rewritten. "Passwords were reused" becomes "The loan admin account used the same password as VPN" when known.

### 4.10 4.11 Scene

A draft finding once said "developers ignored security". Legal asked for rewrite before the board pack. Sam produced: "The loan service accepted a shared privileged password; logs cannot attribute changes to a person." Same facts, fundable tone. He keeps both versions in teaching notes to show the difference.

### 4.11 4.20 Extra

Tone trophies are silly stickers on printed findings that developers praised as clear. Sam prefers stickers to metrics nobody reads.

### Worked example (synthetic TRB)

Sam rewrites \"the web team is incompetent\" to \"web tier reaches ledger-db on an unapproved flow; control: enforce approved matrix\".

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX010 — Rewrite.** Turn \"stupid password reuse\" into professional finding language. *Rubric:* 3 = system condition + impact + no insult; 2 = partial; 1 = keeps insult; 0 = none.
- **EX011 — Speculative claim.** How should Sam label \"attackers already stole funds\"? *Rubric:* 3 = speculative/unconfirmed; separate from facts; 2 = partial; 1 = as fact; 0 = none.
- **EX012 — Citation rule.** What must Sam never invent when citing? *Rubric:* 3 = DOIs / fake references; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Clear, cited, audience-aware writing is part of authorized testing craft.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) place authorized testing among security practices; (2) name CIA with TRB examples; (3) refuse unauthorized work.

### 5.1 Neighbouring practices

Architecture, monitoring, IR and authorized testing reinforce each other. Testing without logging is theatre; logging without testing misses unknown unknowns.

### 5.2 CIA at TRB

Confidentiality of customer data; integrity of ledgers and payments; availability of online banking. Findings are judged by which they threaten.

### 5.3 Permission

Written ROE from owners. Bug bounties cover only their published scope. Friends' banks are never practice targets.

### 5.4 Dual-use

This curriculum teaches scoping, measurement and reporting — not exploit code for real products.

### 5.5 Framework map

SP 800-115 (planning), PTES (stages), WSTG (web), ATT&CK (techniques), TIBER-EU/CBEST (threat-led finance).

### 5.6 Ethics

Customer harm and payment integrity outrank curiosity and resume screenshots.

### 5.7 5.7 Applied note

The refusal script is role-played with a staff member playing an impatient director. Sam must keep tone respectful while not yielding. Video reviews show whether he smiles nervously into agreement; those clips are deleted after coaching but the lesson stays.

### 5.8 5.8 Framework flashcards

Sam's deck has one card per framework: SP 800-115, PTES, WSTG, ATT&CK, TIBER-EU, CBEST — purpose and what it is not. Misusing CBEST as a web checklist is a common card-back answer.

### 5.9 5.9 Home lab boundary

Sam's home lab uses RFC1918 and never TRB DNS. Mixing VPN into homework is a reported near-miss if it happens.

### 5.10 5.11 Scene

Sam declines a meetup invitation to demo "how we hacked our bank" even though the work was authorized. Screenshots travel. He offers instead a talk on ROE design with synthetic examples. The organisers accept. Dual-use restraint includes what you refuse to present.

### 5.11 5.20 Extra

Meetup alternative talks use only documentation-range demos. Sam's slide deck is public; his TRB screenshots are not.

### Worked example (synthetic TRB)

A classmate asks Sam to \"try the bank's login from home\". Sam refuses and points to the course boundary.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX013 — CIA match.** Match: leaked statements; altered transfer; banking down. *Rubric:* 3 = C,I,A; 2 = two; 1 = one; 0 = none.
- **EX014 — Refuse.** Why refuse testing a friend's bank login? *Rubric:* 3 = no authorization; illegal/harmful; 2 = partial; 1 = ok if careful; 0 = none.
- **EX015 — Dual-use.** What does this course refuse to provide? *Rubric:* 3 = exploit code / attack procedures for real systems; 2 = partial; 1 = scoping help; 0 = none.

### Synthesis

Literacy is CIA, permission, frameworks and ethical refusal.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) model access as graphs; (2) use relations for flow matrices; (3) apply trees to stop decisions.

### 6.1 Access graphs

Nodes are principals and systems; edges are can-authenticate or can-reach. A path from Internet to ledger-db that bypasses jump hosts is a finding candidate.

### 6.2 Flow relations

Approved flows are a relation R ⊆ Src × Dst. Observed flows should be subsets of R when the matrix is enforced.

### 6.3 Decision trees

Stop trees: if owner asks stop → halt; else if unexplained outage → halt; else continue under ROE.

### 6.4 Equivalence

Hosts in the same hardening class may share method cards — but only if the ROE groups them.

### 6.5 Ordering

Severity ranking uses ordered scores; ties break by finding id for determinism (lab_rank).

### 6.6 Limits

Graphs omit social engineering unless the ROE includes it.

### 6.7 6.7 Applied note

Reachability graphs annotate edges with "authenticated" or "network-only". A network-only edge to ledger-adjacent hosts raises severity even without credentials, because credential theft elsewhere completes the path. Sam's first graphs missed that annotation and under-ranked a finding.

### 6.8 6.8 Cut sets

For payments-adjacent nodes, Sam looks for cut sets of edges whose removal would isolate them from the Internet. Those edges become monitoring and control priorities even when not "vulnerable" in a scanner sense.

### 6.9 6.9 Edge evidence

Each critical graph edge cites the inventory or scan source under ROE. Edges without sources are removed.

### 6.10 6.11 Scene

Tracing a path from a compromised branch PC model to ledger-db, Sam finds four edges. Removing the web→ledger edge (F3) and requiring jump for admin cuts the remaining dangerous paths. The graph did not need fifty nodes — it needed the cut set. He deletes the decorative edges from the slide.

### 6.11 6.20 Extra

Cut-set slides use at most six edges. Sam deletes the rest in front of the audience to teach focus.

### Worked example (synthetic TRB)

Sam draws web → ledger-db as an edge not in R; lab_flows later flags the same pair UNAPPROVED.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX016 — Relation view.** What does an UNAPPROVED flow mean in relation terms? *Rubric:* 3 = observed pair not in approved relation R; 2 = partial; 1 = approved; 0 = none.
- **EX017 — Path finding.** Why does a path Internet→web→ledger matter? *Rubric:* 3 = trust boundary crossings / reachability beyond intent; 2 = partial; 1 = irrelevant; 0 = none.
- **EX018 — Tie break.** How does lab_rank break equal scores? *Rubric:* 3 = by finding id; 2 = random; 1 = title length; 0 = none.

### Synthesis

Graphs and relations make architecture and flow findings precise.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) read ports and services carefully; (2) explain TLS roles; (3) avoid protocol experiments on live TRB systems.

### 7.1 Ports are not services

Port 443 often means HTTPS but may not. Inventory names and certificates matter.

### 7.2 TLS

Protects confidentiality and integrity in transit; does not fix broken authorization in the app.

### 7.3 Dangerous experiments

Sending malformed packets to the ledger VLAN to \"see what happens\" is out of bounds.

### 7.4 Documentation ranges

Labs use 198.51.100.0/24 and 203.0.113.0/24 so examples cannot hit the real Internet.

### 7.5 Capture ethics

Packet captures need ROE clauses; they often contain customer data.

### 7.6 ATT&CK

T1190 Exploit Public-Facing Application describes abuse of internet-facing services — named for detection design, not as a how-to.

### 7.7 7.7 Applied note

Capture ROE clauses specify retention hours and who may run wireshark. Sam's default ask is "configs and logs first; packets only if those fail". Most TRB web findings never need packets; when they do, the clause is already written.

### 7.8 7.8 Banner humility

Banners feed inventory, not severity theatre. Sam files version exposure as low unless paired with a reachable vulnerable path under ROE — which this course still will not exploit in the wild.

### 7.9 7.9 Doc-range lint

Examples in docs are linted to ensure IPs are documentation ranges. Sam's lint failed a blog draft using a real TRB address; good catch.

### 7.10 7.11 Scene

A learner asks to try a TCP FIN scan on staging "for the coursework". Sam shows the ROE forbidden-methods list and the course boundary page. They run an offline PCAP quiz instead. Curiosity is redirected, not shamed — and not indulged on bank networks.

### 7.11 7.20 Extra

PCAP quiz answers never include payload bytes from real customers. Synthetic PCAPs only.

### Worked example (synthetic TRB)

Sam's scope lab rejects 203.0.113.9 as OUT OF SCOPE using only local IP math.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX019 — TLS limit.** What does TLS not fix? *Rubric:* 3 = broken application authorization / logic; 2 = partial; 1 = everything; 0 = none.
- **EX020 — Doc ranges.** Why use 198.51.100.0/24 in labs? *Rubric:* 3 = documentation/reserved ranges; safe examples; 2 = partial; 1 = real TRB; 0 = none.
- **EX021 — Capture rule.** When may Sam take a packet capture? *Rubric:* 3 = when ROE allows; minimise data; 2 = partial; 1 = anytime; 0 = none.

### Synthesis

Protocol literacy without live experimentation; captures only under ROE.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) structure modules for the platform; (2) validate inputs; (3) version APIs carefully.

### 8.1 Modules

Scope loader, finder schema, report exporter — each with tests and a README.

### 8.2 Validate on write

FindingsDesk rejects tickets missing owner or evidence hash.

### 8.3 API versioning

PulseMap v2 adds fields without breaking v1 consumers.

### 8.4 Partial updates

PATCH must not clear required fields accidentally.

### 8.5 Bulk import

CSV import of findings dry-runs first and caps row counts.

### 8.6 Concurrency

Optimistic locking prevents two analysts overwriting the same ticket silently.

### 8.7 8.7 Applied note

Bulk import caps at 500 rows and requires a second approver above 100. Sam saw an analyst almost import a scanner dump that included out-of-scope hosts as "informational". Caps and approvers are boring on purpose.

### 8.8 8.8 Migration drills

Schema migrations run on a copy with checksums before and after. Sam records row counts. A migration that changes counts silently fails the drill.

### 8.9 8.9 Idempotent writes

Ticket updates are idempotent by finding id. Double delivery from flaky networks cannot create duplicate F1s.

### 8.10 8.11 Scene

FindingsDesk's bulk import dry-run once revealed 40 hosts outside the ROE embedded in a scanner CSV. The import blocked. Sam thanks the dry-run in the retrospective more than any new feature shipped that month.

### 8.11 8.12 Extension

Idempotent ticket updates saved TRB when a flaky VPN resubmitted the same finding create call twelve times. FindingsDesk showed one F1, not twelve. Sam adds that story to onboarding so engineers stop fearing "exactly-once" as academic.

### 8.12 8.16 Pad

FindingsDesk's approval threshold at 100 rows exists because a 2,000-row dump once queued overnight and page-stormed owners. Sam documents the incident id beside the constant in code.

### 8.13 8.20 Extra

Overnight page-storm incident id is ENG-441 in the course archive. Sam links it from the constant's comment.

### Worked example (synthetic TRB)

Sam adds a FindingsDesk check: empty emergency_contact in ROE metadata blocks engagement start.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX022 — Reject rule.** Name two fields that should block ticket creation if empty. *Rubric:* 3 = two of owner, evidence hash, severity; 2 = one; 1 = title colour; 0 = none.
- **EX023 — Dry-run import.** Why dry-run bulk import? *Rubric:* 3 = catch schema errors before write; 2 = partial; 1 = no need; 0 = none.
- **EX024 — Optimistic lock.** What problem does optimistic locking prevent? *Rubric:* 3 = silent overwrite of concurrent edits; 2 = partial; 1 = slow UI; 0 = none.

### Synthesis

Platform code validates, versions and refuses to start unsafe engagements.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) design minimal schemas for findings; (2) protect customer data in evidence DBs; (3) retain and delete on schedule.

### 9.1 Minimal schema

Store what retests need, not entire customer tables.

### 9.2 Access control

Evidence databases use role-based access; Sam's intern role is read/write on engagement schemas only.

### 9.3 Retention

Agreement-driven deletion jobs; \"keep forever\" is not a policy.

### 9.4 Backups

Encrypted, access-logged, tested restores — backups are in scope for abuse review.

### 9.5 Query hygiene

No SELECT * into laptops; export minimised CSVs.

### 9.6 Integrity

Foreign keys from findings to evidence blobs.

### 9.7 9.7 Applied note

Evidence DB roles are reviewed quarterly against HR lists. Sam's query checks for active vault roles without active employees. The first run found two contractors; access was removed the same afternoon.

### 9.8 9.8 Export watermarks

CSV exports embed engagement id and exporter name in a header comment. Leaked files can be traced. Sam verifies the watermark exists in a quarterly spot check.

### 9.9 9.9 Backup restore game

Quarterly, Sam restores an evidence backup to an isolated host and opens one file. Untested backups are assumed broken.

### 9.10 9.11 Scene

An analyst requests "all evidence for the year" for a thesis. Sam refuses bulk export and offers a statistics-only extract with counts by severity. The thesis still proceeds. Minimisation applies to friendly requests too.

### 9.11 9.12 Extension

During restore game day the backup opened, but the hash manifest was missing. Sam failed the game and restored the manifest job before the next engagement. Backups without manifests are rumours.

### 9.12 9.16 Pad

Watermark headers include a contact mailto for lost-and-found of stray exports. Someone used it once; Sam bought them coffee.

### 9.13 9.20 Extra

Lost-and-found mailto once returned a USB drive labelled with an engagement id. Process works.

### Worked example (synthetic TRB)

Sam's export job redacts account numbers to last four digits before analysts download CSV.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX025 — Minimalism.** Why not store full customer rows with each finding? *Rubric:* 3 = privacy/minimisation/ROE; 2 = partial; 1 = need them; 0 = none.
- **EX026 — Retention.** What triggers deletion of engagement evidence? *Rubric:* 3 = agreement schedule / retention date; 2 = partial; 1 = never; 0 = none.
- **EX027 — Role.** What should an intern role not access by default? *Rubric:* 3 = unrelated engagements / production customer DB; 2 = partial; 1 = everything; 0 = none.

### Synthesis

Databases hold the least personal data needed, with retention and roles enforced.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) list ROE essentials; (2) check targets offline; (3) handle pressure to exceed scope.

### 10.1 ROE essentials

Scope, exclusions, methods, window, emergency contacts, data handling, report audience — NIST SP 800-115 and PTES both put authorization first.

### 10.2 Offline check

lab_scope classifies proposed targets before any packet.

```python
"""Lab 10: check a synthetic TRB target list against written scope and exclusions (no traffic sent)."""
import ipaddress
scope = [ipaddress.ip_network("198.51.100.0/26")]
excluded = {ipaddress.ip_address("198.51.100.20")}  # SWIFT gateway, owner excluded
for t in ["198.51.100.5", "198.51.100.20", "198.51.100.70", "203.0.113.9"]:
    ip = ipaddress.ip_address(t)
    v = "EXCLUDED" if ip in excluded else "in scope" if any(ip in n for n in scope) else "OUT OF SCOPE"
    print(f"{t:15} {v}")
```

Run with `python3 lab_scope.py`. Verified output:

```text
198.51.100.5    in scope
198.51.100.20   EXCLUDED
198.51.100.70   OUT OF SCOPE
203.0.113.9     OUT OF SCOPE
```

### 10.3 Pressure

\"Just add the SWIFT box\" is refused until written exclusion changes — which they will not for ordinary tests.

### 10.4 Responsible disclosure

Vendor bugs found in third-party software follow vendor paths only with CISO approval.

### 10.5 Conflicts

Sam does not test systems owned by family businesses on TRB time or tools.

### 10.6 Dual-use teaching

Exploit details for real payment products are out of curriculum scope.

### 10.7 10.7 Applied note

Dual-use policy examples include refusing to paste exploit PoCs into FindingsDesk even when a vendor asks "for repro". Reproduction at TRB uses configuration evidence and authorized accounts, not weaponised snippets.

### 10.8 10.8 Gift and conflict log

Sam logs any vendor gifts or outside bank accounts that could bias scope decisions. Transparency is cheaper than recusal fights mid-engagement.

### 10.9 10.9 Tabletop ROE

Annual tabletop walks a missing emergency-contact scenario. Sam's team practices postponing rather than improvising.

### 10.10 10.11 Scene

Tabletop: emergency contact unreachable. Sam's team postpones the window in writing within five minutes. Improvised verbal approval from a random manager is scored as a fail condition in the tabletop. Postponement is success.

### 10.11 10.12 Extension

Sam's conflict log once listed a sibling working at a fintech vendor. He recused from a test involving that vendor's library. Recusal is quieter than scandal.

### 10.12 10.16 Pad

Postponement templates include SOC and CISO aliases pre-filled. Sam sends postponements in under three minutes during drills.

### 10.13 10.20 Extra

Three-minute postponement drill is timed with a visible clock. Over three minutes fails the drill.

### Worked example (synthetic TRB)

lab_scope marks 198.51.100.20 EXCLUDED and 198.51.100.70 OUT OF SCOPE; Sam removes both from the plan.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX028 — Excluded line.** What does the lab print for 198.51.100.20? *Rubric:* 3 = EXCLUDED; 2 = out of scope; 1 = in scope; 0 = none.
- **EX029 — Pressure answer.** How does Sam answer \"add SWIFT just this once\"? *Rubric:* 3 = refuse until written ROE change; SWIFT stays excluded; 2 = refuse; 1 = agree; 0 = none.
- **EX030 — ROE list.** Name five ROE essentials. *Rubric:* 3 = five of scope, exclusions, methods, window, contacts, data, audience; 2 = three; 1 = one; 0 = none.

### Synthesis

Ethics is operationalised as checklists, refusals and offline scope math.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) compare admin surfaces; (2) require jump hosts; (3) treat images as in-scope when agreed.

### 11.1 Surfaces

Patch levels, local admins and remote services differ across Windows and Linux. Findings name OS and failed control.

### 11.2 Jump hosts

Admin paths go through jump; email-VLAN RDP to servers is a finding.

### 11.3 Images

Golden images with old agents reintroduce risk when rebuilt.

### 11.4 Logging

OS logs support detection recommendations tied to ATT&CK.

### 11.5 Privileges

Hypervisor admin is a separate scope layer.

### 11.6 Hardening baselines

Deviations need tickets, not folklore.

### 11.7 11.7 Applied note

Image pipeline tickets must name the agent versions baked in. Sam rejects "latest" as a version string. Reproducible builds of golden images are treated like application releases.

### 11.8 11.8 Local admin census

A quarterly query lists local admins on staging. Unexpected names become tickets. Sam correlates with leaver lists.

### 11.9 11.9 Agent drift

Hosts whose agent version differs from the image catalogue by more than one minor version open tickets automatically.

### 11.10 11.11 Scene

A rebuilt staging host comes back with an old RDP posture. The image catalogue said it should not. Sam files both a host finding and an image-pipeline finding. Two owners, two tickets, one root cause class.

### 11.11 11.12 Extension

Local admin census found a dormant "temp" admin created during an outage. Ticket, remove, verify. Dormant temps are permanent until hunted.

### 11.12 11.14 Note 11

Image findings always CC the pipeline owner, not only the host owner.

### 11.13 11.16 Pad

Pipeline findings use a separate severity rubric weighted toward recurrence. One bad image can mint a hundred bad hosts.

### 11.14 11.20 Extra

Recurrence-weighted rubric for images is published beside host severity. Different beasts, different scales.

### Worked example (synthetic TRB)

Sam files staging RDP from email VLAN bypassing jump as a finding with screenshot hash.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX031 — Jump bypass.** Why is email-VLAN RDP to servers a finding? *Rubric:* 3 = bypasses controlled jump path/logging; 2 = partial; 1 = fine; 0 = none.
- **EX032 — Image risk.** How do stale images create weaknesses? *Rubric:* 3 = redeploy old agents/settings; 2 = partial; 1 = no risk; 0 = none.
- **EX033 — Hypervisor.** Is hypervisor admin implied by web scope? *Rubric:* 3 = no; separate layer; 2 = no; 1 = yes; 0 = none.

### Synthesis

OS findings name the layer; admin goes through jump hosts.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) compute a Wilson interval; (2) explain base rates; (3) avoid overclaiming from small n.

### 12.1 Rates

Detection rate k/n needs uncertainty. Seven of ten is not the same as seventy of one hundred.

### 12.2 Wilson interval

lab_wilson prints 95% intervals for synthetic purple-team detection counts.

```python
"""Lab 12: Wilson 95% interval for a synthetic detection rate in a purple-team exercise."""
import math
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h
for k, n in [(7, 10), (70, 100)]:
    lo, hi = wilson(k, n)
    print(f"detected {k}/{n} rate={k/n:.2f} 95% CI=({lo:.2f}, {hi:.2f})")
```

Run with `python3 lab_wilson.py`. Verified output:

```text
detected 7/10 rate=0.70 95% CI=(0.40, 0.89)
detected 70/100 rate=0.70 95% CI=(0.60, 0.78)
```

### 12.3 Base rates

Rare true issues drowned in noisy scanners waste fixer time.

### 12.4 Ranking defences

Prefer intervals that do not overlap when claiming A beats B.

### 12.5 Reporting

Managers hear counts and intervals in plain language.

### 12.6 Limits

Independence assumptions fail when tests share environment faults.

### 12.7 12.7 Applied note

When intervals overlap, Sam forbids ranking defences as winners. A slide once claimed MFA beat phishing training on overlapping Wilson intervals; he pulled the slide and asked for more trials instead of a louder font.

### 12.8 12.8 Plain-language CI

Sam requires every interval in a deck to appear once in words: "between about X and Y". Charts alone are not enough for board packs.

### 12.9 12.9 Sample size planner

A small tool suggests n for a target CI width. Sam uses it before promising detection rates to executives.

### 12.10 12.11 Scene

Finance asks for a single detection percentage for the annual report. Sam gives two sentences with intervals instead. Legal prefers his version because it cannot be read as a warranty. Uncertainty language protects the bank.

### 12.11 12.12 Extension

Sample size planner told Sam he needed n≈96 for a tight interval. He cut the claim instead of inventing data. Planners exist to shrink promises.

### 12.12 12.16 Pad

Board packs that insist on a single number get Sam's appendix with the refusal rationale. Legal endorsed the appendix.

### 12.13 12.20 Extra

Refusal appendix has legal's endorsement email hash attached. Sam loves boring integrity.

### Worked example (synthetic TRB)

Sam shows 7/10 CI (0.40,0.89) vs 70/100 (0.60,0.78) to explain why TRB funds more trials before claiming a detection win.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX034 — Interval read.** What CI does the lab print for 7/10? *Rubric:* 3 = (0.40, 0.89); 2 = approximate; 1 = wrong; 0 = none.
- **EX035 — Why wider.** Why is the 7/10 interval wider than 70/100 at the same rate? *Rubric:* 3 = smaller sample / more uncertainty; 2 = partial; 1 = bug; 0 = none.
- **EX036 — Manager sentence.** Write one plain sentence Sam could say about 7/10. *Rubric:* 3 = count + uncertainty + not definitive; 2 = partial; 1 = \"we are 70% safe\"; 0 = none.

### Synthesis

Small samples need intervals; confidence is not a security percentage.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) separate AuthN and AuthZ; (2) least-privilege test accounts; (3) map shared accounts to T1078.

### 13.1 AuthN/AuthZ

Proving identity versus allowing actions. IDOR is AuthZ failure after AuthN.

### 13.2 Test accounts

Named, timed, vaulted, least privilege.

### 13.3 Shared admins

Accountability loss; ATT&CK T1078 Valid Accounts.

### 13.4 MFA

Verify by config review, not phishing staff.

### 13.5 Service accounts

Owners and rotation dates required.

### 13.6 Leavers

Access lingering after HR termination is a classic finding.

### 13.7 13.7 Applied note

Test account expiry is enforced by a job that disables accounts at window end and pages Sam if disable fails. Manual reminders failed twice historically; the job is now a control, not a convenience.

### 13.8 13.8 Break-glass accounts

Break-glass admins are monitored and rare. Sam's review checks that break-glass was not used as daily driver during the window.

### 13.9 13.9 Vault MFA

Vault access for credentials requires MFA. Sam tested denial without MFA and filed the deny as a positive control demo.

### 13.10 13.11 Scene

A shared admin password on the loan system is rotated, but the same password is later found in a printer config. Sam's leaver-and-secrets checklist now includes "search for password reuse artefacts" after any shared-admin finding.

### 13.11 13.12 Extension

Break-glass use during a window pages the CISO channel automatically. Sam tested the page with a staging break-glass and got a stern but correct phone call.

### 13.12 13.14 Note 11

Leaver tickets auto-open from HR events within an hour; Sam audits the automation weekly.

### 13.13 13.16 Pad

Printer configs are now in the secret-search path after the reuse incident. Strange places hide passwords.

### 13.14 13.20 Extra

Secret-search path expansions are logged; scope creep in search is still scope.

### Worked example (synthetic TRB)

Shared admin on loan system becomes F1 with score 6 in lab_rank.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX037 — T1078.** Which technique fits shared valid admin passwords? *Rubric:* 3 = T1078 Valid Accounts; 2 = name; 1 = wrong; 0 = none.
- **EX038 — MFA method.** How to verify MFA without phishing? *Rubric:* 3 = configuration/policy review under ROE; 2 = partial; 1 = phish; 0 = none.
- **EX039 — Test account traits.** List three traits of a good test account. *Rubric:* 3 = named, least privilege, time-bounded/vaulted; 2 = two; 1 = one; 0 = none.

### Synthesis

Identity findings are precise about AuthN vs AuthZ and never require phishing colleagues.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) minimise customer data in evidence; (2) redact; (3) respect retention.

### 14.1 Minimisation

Proof beats bulk extracts of customer tables.

### 14.2 Redaction

Mask account numbers; keep digits that prove the issue if needed.

### 14.3 Purpose limitation

Engagement evidence is not a marketing analytics source.

### 14.4 Access

Need-to-know on evidence vaults.

### 14.5 Cross-border

Cloud regions may implicate rules; legal advises.

### 14.6 Breach risk

Evidence vaults are high-value targets; protect them.

### 14.7 14.7 Applied note

Re-identification drills pair a redacted screenshot with public org charts. If a peer can name the person, redaction fails the gate. Sam now prefers synthetic personas in most teaching screenshots.

### 14.8 14.8 Synthetic evidence library

A library of synthetic screenshots covers common findings so learners need not handle real customer pixels. Sam contributes one new synthetic each term.

### 14.9 14.9 Purpose tags

Evidence files tagged with purpose; secondary use requires a new tag and approval. Marketing cannot "just borrow" engagement screenshots.

### 14.10 14.11 Scene

Synthetic screenshot library item SS-17 shows a fake customer "Ada Example" with account ••••4242. Learners prefer it to redacting real screens. Sam measures that preference and funds more synthetic art.

### 14.11 14.12 Extension

Purpose tags blocked a well-meaning trainee from dropping engagement screenshots into a UX redesign folder. The refusal felt petty and protected a hundred customers.

### 14.12 14.14 Note 11

Synthetic Ada Example has a style guide so artists keep her obviously fake.

### 14.13 14.16 Pad

Artists sign a CLA that Ada Example may not resemble real customers. Legal insisted; Sam agreed happily.

### 14.14 14.18 Final

Privacy coaches at TRB include a five-minute desk visit when a new analyst first opens the evidence vault. Sam scripts the visit: show retention dates, show access list, show one redaction fail example, ask the analyst to repeat the minimisation rule in their own words. Desk visits catch bravado better than LMS modules. Analysts sign a tiny card that stays in the vault foyer.

### Worked example (synthetic TRB)

Sam redacts all but last four digits before attaching a screenshot to F4.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX040 — Minimisation.** Why not export the full customer table for a finding? *Rubric:* 3 = privacy/purpose/ROE; 2 = partial; 1 = need it; 0 = none.
- **EX041 — Redaction.** What does Sam redact in the screenshot example? *Rubric:* 3 = account numbers except last four / personal identifiers; 2 = partial; 1 = nothing; 0 = none.
- **EX042 — Vault.** Why protect evidence vaults strongly? *Rubric:* 3 = concentrated sensitive proof data; 2 = partial; 1 = no need; 0 = none.

### Synthesis

Privacy is minimisation, redaction, purpose limits and vault hygiene.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) hash evidence; (2) choose non-vanity metrics; (3) keep custody.

### 15.1 Hashing

Detect accidental edits before filing.

### 15.2 Metrics

Assets touched, cards run, owners assigned — not raw finding counts.

### 15.3 Custody

Who/when/where for each artifact.

### 15.4 Integrity vs truth

Matching hash ≠ live system still vulnerable.

### 15.5 Sampling

Sample closed tickets for verification evidence.

### 15.6 PulseMap

Coverage views must show denominators.

### 15.7 15.7 Applied note

Closed-ticket sampling is five tickets per month, chosen by RNG. Missing verification evidence reopens the ticket automatically. Sam publishes the reopen count so gaming the metric is visible.

### 15.8 15.8 Metric dictionary

A shared dictionary defines "touched", "validated" and "closed". Sam refuses PulseMap tiles that use undefined words.

### 15.9 15.9 Touched definition

"Touched" means a method card finished with evidence, not a ping. Sam's dictionary fight on that word was worth a week.

### 15.10 15.11 Scene

PulseMap's tile subtitle "n=2" next to a green check teaches more than a lecture on sample size. Sam deliberately leaves a small-n green tile in the training environment to provoke questions.

### 15.11 15.12 Extension

Dictionary fight ended when CISO signed the definitions. Sam frames the signed PDF in the team wiki. Words are controls.

### 15.12 15.14 Note 11

Signed metric definitions hang next to the team coffee machine — paper still works.

### 15.13 15.16 Pad

Undefined-word tiles show a yellow "define me" state instead of green. Yellow is harder to ignore.

### 15.14 15.18 Final

Measurement office hours run Thursdays. Anyone may bring a tile that feels misleading. Sam's most common fix is adding n to the subtitle or changing green to yellow. He tracks how many tiles change colour each month as a quality metric of the metrics.

### Worked example (synthetic TRB)

Sam refuses a mismatched screenshot hash and re-captures.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX043 — Vanity.** Why reject raw finding count as a KPI? *Rubric:* 3 = rewards noise; 2 = partial; 1 = best KPI; 0 = none.
- **EX044 — Hash meaning.** What does a matching hash prove? *Rubric:* 3 = unchanged since hashing; 2 = partial; 1 = system safe; 0 = none.
- **EX045 — Custody fields.** Name four custody fields. *Rubric:* 3 = who what when where; 2 = three; 1 = one; 0 = none.

### Synthesis

Evidence is hashed and attributed; metrics carry denominators.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) draw TRB zones; (2) enforce flow matrices; (3) fail closed.

### 16.1 Zones

Internet, DMZ, corporate, payments-adjacent (restricted), assessment.

### 16.2 Flows

Approved matrix is authoritative; lab_flows flags web→ledger-db.

```python
"""Lab 22: flag synthetic TRB data flows missing from the approved flow register."""
approved = {("branch-pc","core-api"), ("web","core-api"), ("core-api","ledger-db"), ("jump","ledger-db")}
seen = [("branch-pc","core-api"), ("web","core-api"), ("core-api","ledger-db"), ("web","ledger-db"), ("jump","ledger-db")]
for s, d in seen:
    print(f"{s:10} -> {d:10} {'approved' if (s,d) in approved else 'UNAPPROVED'}")
```

Run with `python3 lab_flows.py`. Verified output:

```text
branch-pc  -> core-api   approved
web        -> core-api   approved
core-api   -> ledger-db  approved
web        -> ledger-db  UNAPPROVED
jump       -> ledger-db  approved
```

### 16.3 Fail closed

Proxies and TrackScope deny when policy missing.

### 16.4 Conduits

Owned firewall rules.

### 16.5 Third parties

Processors need their own authorization.

### 16.6 Diagrams

Dated and owned.

### 16.7 16.7 Applied note

Matrix excerpts are hashed and stored beside the ROE. If network changes mid-engagement, Sam diffs the live rules against the hash and pauses if they diverge without a change ticket.

### 16.8 16.8 Conduit owners on-call

Each conduit lists an on-call. During tests Sam messages the conduit on-call, not a general IT inbox, when rules misbehave.

### 16.9 16.9 Third-party column

Flow matrices include a column "third-party auth needed?". Yes rows cannot be tested under TRB ROE alone.

### 16.10 16.11 Scene

When lab_flows shows web→ledger-db, network claims the rule is temporary. Sam asks for the change ticket and kill-date. Neither exists. Temporary without expiry becomes F3's twin process finding.

### 16.11 16.12 Extension

Third-party column "yes" blocked a curious scan of the SMS vendor. Sam sent the vendor's bug bounty link instead. Boundaries can still be helpful.

### 16.12 16.14 Note 11

Kill-date calendar invites include the CISO alias as optional attendee for visibility.

### 16.13 16.16 Pad

Twin process findings link to F3 with a related-id field. Boards see technical and process debt together.

### 16.14 16.18 Final

Architecture office hours use a projector and a red pen. Unowned conduits get circled until an owner appears in the register. Sam refuses to schedule tests through unowned conduits even if the firewall rule exists. Ownership is part of authorization.

### Worked example (synthetic TRB)

lab_flows prints web -> ledger-db UNAPPROVED; Sam opens F3.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX046 — Unapproved pair.** Which flow is UNAPPROVED in the lab? *Rubric:* 3 = web→ledger-db; 2 = partial; 1 = branch-pc→core-api; 0 = none.
- **EX047 — Fail closed.** TrackScope missing policy should… *Rubric:* 3 = deny testing; 2 = partial; 1 = allow; 0 = none.
- **EX048 — Third party.** May TRB ROE alone authorize testing a card processor? *Rubric:* 3 = no; processor auth needed; 2 = no; 1 = yes; 0 = none.

### Synthesis

Architecture is zones, owned flows and fail-closed defaults.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) state what TLS does; (2) protect evidence at rest; (3) avoid inventing schemes.

### 17.1 TLS in transit

Confidentiality and integrity of sessions — not app AuthZ.

### 17.2 At rest

Evidence vault encryption and key access logs.

### 17.3 Hashes

SHA-256 for evidence integrity, not for password storage design lectures here.

### 17.4 Anti-patterns

Homegrown crypto for TrackScope tokens is forbidden.

### 17.5 Key custody

Platform keys in HSM or vault with dual control where required.

### 17.6 Limits

Crypto does not stop authorized malicious admins with valid keys.

### 17.7 17.7 Applied note

HSM export ceremonies for platform keys require two people and a reason code. Sam's intern role cannot export. He tested the denial by attempting an export in staging and filing the deny log as evidence that the control works.

### 17.8 17.8 Token lifetime

Platform tokens expire within the window plus one hour. Sam tests that expired tokens cannot file findings. Lingering tokens are findings against the platform.

### 17.9 17.9 Key ceremony notes

Ceremony notes list attendees and key ids, never secret material. Sam files notes in the vault with the same retention as evidence.

### 17.10 17.11 Scene

Sam attempts to commit a "temporary" base64 blob that looks like a key. CI fails. He is glad. The failure message links to the key ceremony doc. Guardrails should teach, not only block.

### 17.11 17.12 Extension

Token lifetime plus one hour once bit an analyst writing late. Better a re-auth than a token in a stolen laptop weeks later.

### 17.12 17.16 Pad

Ceremony deny logs are retained as positive evidence for examiners who ask whether intern roles are enforced.

### 17.13 17.20 Extra

Positive deny evidence packets are reused in onboarding week one.

### Worked example (synthetic TRB)

Sam rejects a PR that encrypts scope files with a hard-coded AES key in source.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX049 — TLS vs AuthZ.** Does TLS fix IDOR? *Rubric:* 3 = no; 2 = no; 1 = yes; 0 = none.
- **EX050 — Hard-coded key.** Why reject hard-coded AES keys in source? *Rubric:* 3 = key exposure in repo; not dual-control; 2 = partial; 1 = fine; 0 = none.
- **EX051 — Hash use here.** What are SHA-256 digests used for in this course? *Rubric:* 3 = evidence integrity; 2 = partial; 1 = encrypting traffic; 0 = none.

### Synthesis

Use standard crypto correctly; never roll your own for engagement secrets.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) pose answerable questions; (2) design small purple-team trials; (3) pre-register metrics.

### 18.1 Questions

\"Does control X raise detection of T1566 in staging?\" beats \"is security good?\".

### 18.2 Design

Fixed test set, recorded environment, sample size plan.

### 18.3 Pre-registration

Write metric and threshold before seeing results.

### 18.4 Ethics

Customer data off-limits; synthetic phishing to staff needs HR/CISO approval.

### 18.5 Negative results

Publish internally; they prevent repeated failed ideas.

### 18.6 Limits

Staging ≠ production; state threats to validity.

### 18.7 18.7 Applied note

Negative results get the same template as positive ones. Sam's "MFA prompt fatigue did not improve T1566 detection in n=40" note stopped a second identical trial the following quarter.

### 18.8 18.8 Trial registration board

A public (internal) board shows pre-registered trials and their status. Duplicate trials are rejected at a glance.

### 18.9 18.9 Power analysis humility

Sam avoids claiming significance without a plan. Most purple trials at TRB are descriptive with intervals, not pseudo-clinical trials.

### 18.10 18.11 Scene

A pre-registered trial on awareness mail fails its threshold. Sam still writes it up. The next quarter's budget meeting cites the negative result to avoid buying the same content pack again.

### 18.11 18.12 Extension

Registration board rejected a duplicate trial title within a minute. The author joined the existing trial as a helper instead of wasting a cohort.

### 18.12 18.14 Note 11

Negative results get a champagne cork icon in the board — celebration of learning, not failure.

### 18.13 18.16 Pad

Champagne cork icons are optional; the write-up is not. Sam rejects icons without prose.

### 18.14 18.20 Extra

Icons without prose are stripped by the board's markdown linter.

### Worked example (synthetic TRB)

Sam pre-registers: success if detection ≥80% on 50 T1566-style synthetic emails with Wilson lower bound ≥0.7.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX052 — Bad question.** Why is \"is security good?\" a poor research question? *Rubric:* 3 = not measurable/specific; 2 = partial; 1 = fine; 0 = none.
- **EX053 — Pre-register.** What should be written before results? *Rubric:* 3 = metric and threshold (and design); 2 = partial; 1 = nothing; 0 = none.
- **EX054 — Staff phishing.** What approvals before simulated phishing? *Rubric:* 3 = CISO/HR (and ROE); 2 = one; 1 = none; 0 = none.

### Synthesis

Answerable questions, pre-registered metrics and ethics before purple-team trials.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Scope and theory of authorized offensive security

### Learning outcomes

You will (1) compare assessment types in SP 800-115; (2) map PTES stages; (3) situate threat-led tests.

### 19.1 SP 800-115 types

Reviews, vulnerability assessments, red teaming — different depth and permission models.

### 19.2 PTES

Pre-engagement through reporting as shared stage names.

### 19.3 Threat-led

TIBER-EU and CBEST use intelligence to shape scenarios for financial entities; TRB studies them even when running lighter tests.

### 19.4 Theory of change

Testing informs risk decisions; it does not create security by itself.

### 19.5 Assurance limits

A clean test is time-bounded assurance, not a warranty.

### 19.6 Platform role

TrackScope encodes theory as executable deny rules.

### 19.7 19.7 Applied note

The assessment catalogue includes what each type cannot claim. Annual web tests cannot claim threat-led coverage; threat-led exercises cannot claim quarterly regression coverage. Sam quotes the cannot-claim line in kickoffs.

### 19.8 19.8 Assurance statement library

Approved sentences for reports include "time-bounded assurance" and forbid "guaranteed secure". Sam's linter flags forbidden phrases.

### 19.9 19.9 Insurance questionnaire map

Questionnaire answers cite the catalogue. Sam stops colleagues from answering "we pentest everything" when SWIFT is excluded.

### 19.10 19.11 Scene

An insurer questionnaire says "Do you conduct red teaming?". Sam answers with the catalogue: quarterly web tests yes; full threat-led last done 20XX; SWIFT excluded from ordinary tests. Checkbox honesty beats swagger.

### 19.11 19.12 Extension

Assurance linter failed a report for "fully secure after remediation". Sam's replacement: "residual risk accepted for F3 until 1 December with compensating jump-only admin".

### 19.12 19.14 Note 11

Catalogue cannot-claim lines are read aloud at kickoff; mumbling is corrected.

### 19.13 19.16 Pad

Kickoff mumbling earns a restart of the cannot-claim read. Clarity over comfort.

### 19.14 19.20 Extra

Cannot-claim read restarts are logged as a fun metric of mumbling.

### Worked example (synthetic TRB)

Sam's lecture note: \"CBEST-style scenarios need intel + ROE + detection goals; our quarterly web test is narrower and still valuable.\"

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX055 — Stage.** Where does PTES place reporting? *Rubric:* 3 = final stage after technical work; 2 = early; 1 = never; 0 = none.
- **EX056 — Threat-led pair.** Name the EU and UK threat-led frameworks cited. *Rubric:* 3 = TIBER-EU and CBEST; 2 = one; 1 = wrong; 0 = none.
- **EX057 — Warranty.** Why is a clean test not a warranty? *Rubric:* 3 = time-bounded / coverage limits / change; 2 = partial; 1 = it is; 0 = none.

### Synthesis

Theory ties assessment types to permissions, stages and humble assurance claims.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Foundational cases

### Learning outcomes

You will (1) analyse synthetic TRB cases; (2) separate fact/guess; (3) escalate payment risk.

### 20.1 Case packet

ROE excerpt, logs, findings draft, staff report of password reuse.

### 20.2 Labels

Fact / Guess / Action lines.

### 20.3 Escalation

Possible payment integrity impact → same-day CISO.

### 20.4 Out of scope

Personal email content stays untouched.

### 20.5 ATT&CK

Tag techniques for SOC hunting.

### 20.6 Blameless

Focus on systems and process.

### 20.7 20.7 Applied note

Facilitators ban timeline adjectives like "suddenly" unless a timestamp exists. Sam's case notes now lead with UTC times from logs, then narrative. Guess lines may not carry timestamps pretending to be facts.

### 20.8 20.8 Case clock

Every case packet states the timezone of log lines on page one. Sam lost an hour once to silent UTC; the cover line prevents it.

### 20.9 20.9 Guess budget

Each case may carry at most three Guess lines. Excess guesses become homework to gather facts.

### 20.10 20.11 Scene

Case night: a Guess line about "APT29" is removed for lack of evidence. The room groans and then writes better Fact lines about VPN logs. Attribution theatre is addictive; the bell helps.

### 20.11 20.12 Extension

Guess budget forced a team to replace an APT guess with two VPN log facts. The case got less cinematic and more true.

### 20.12 20.14 Note 11

Timestamp cover lines use ISO-8601 with offset; "morning" is banned.

### 20.13 20.16 Pad

ISO-8601 cover lines are validated by a regex in the case packet CI.

### 20.14 20.18 Final

Fact-line workshops ban adjectives for twenty minutes. Only nouns, verbs, numbers and timestamps. The constraint feels artificial and produces the cleanest case packets of the term. Sam keeps a trophy packet from last year as the standard.

### Worked example (synthetic TRB)

Sam escalates VPN password reused on personal email; resets TRB credentials; does not read personal mail.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX058 — Fact vs guess.** Label: \"staff reported reuse\" vs \"nation-state has the hash\". *Rubric:* 3 = fact vs guess; 2 = partial; 1 = both facts; 0 = none.
- **EX059 — Personal mail.** Why not read the staffer's personal email? *Rubric:* 3 = out of scope/privacy; 2 = partial; 1 = should; 0 = none.
- **EX060 — Escalate trigger.** What triggers same-day CISO escalation here? *Rubric:* 3 = credential reuse risking bank access/payments; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Cases reward labelled reasoning and fast escalation of payment-adjacent risk.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — System models

### Learning outcomes

You will (1) model online banking; (2) list entry points; (3) record assumptions.

### 21.1 Elements

Actors, entry points, stores, trust zones, external processors.

### 21.2 Entry points

Web, mobile API, staff VPN, batch peers.

### 21.3 Assumptions

\"Staging mirrors prod AuthZ\" must be validated.

### 21.4 Data flows

Customer PII paths drive minimisation.

### 21.5 Exclusions

SWIFT gateway omitted when out of scope.

### 21.6 Living models

Update on new payment callback routes.

### 21.7 21.7 Applied note

Owner workshops use physical tokens for assumptions. A token left in Open at the end blocks kickoff. The tactile rule sounds childish and works better than a spreadsheet column nobody updates.

### 21.8 21.8 Callback inventory

New payment callbacks must appear on the model within one week of change tickets. Sam's weekly diff of change tickets versus model edges catches stragglers.

### 21.9 21.9 External processor box

Processors appear as black boxes with data types crossing the boundary, not as pretend internal hosts.

### 21.10 21.11 Scene

A new mobile deep link appears in a change ticket. Within three days Sam's model gains an entry point and an assumption sticky: "AuthZ same as web?". The sticky is still Open at kickoff and becomes a residual risk sentence.

### 21.11 21.12 Extension

Callback inventory diff found a silent route from marketing site to core-api. It became a conduit review, not a marketing surprise in production.

### 21.12 21.14 Note 11

Open assumption stickies are photographed into the ROE packet before kickoff.

### 21.13 21.16 Pad

Residual risk sentences from Open stickies are pasted into the executive summary draft automatically.

### 21.14 21.18 Final

Model office hours end with a photograph of the whiteboard and an OCR pass into the assumption log. Sticky notes that OCR cannot read are rewritten. Illegible assumptions are denied assumptions.

### Worked example (synthetic TRB)

Sam's model shows web→ledger-db dashed in red as unintended.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX061 — Assumption.** How to validate staging mirrors prod AuthZ? *Rubric:* 3 = compare configs/tests with owners; 2 = partial; 1 = assume; 0 = none.
- **EX062 — Why omit SWIFT.** Why omit SWIFT from this model? *Rubric:* 3 = out of scope; 2 = partial; 1 = unimportant; 0 = none.
- **EX063 — Entry points.** Name three online-banking entry points. *Rubric:* 3 = three of web, mobile API, staff VPN, batch; 2 = two; 1 = one; 0 = none.

### Synthesis

Models make unintended flows visible and assumptions explicit.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Data and dependencies

### Learning outcomes

You will (1) map dependencies; (2) flag unapproved flows; (3) assign owners.

### 22.1 Dependencies

Core API, ledger DB, fraud service, SMS, card processor.

### 22.2 Flow lab

lab_flows marks web→ledger-db UNAPPROVED.

### 22.3 Ownership

Each flow has a control owner.

### 22.4 Third parties

Separate authorization.

### 22.5 Breaks

Vendor outages are stops, not hammering opportunities.

### 22.6 Secrets

API keys in repos are TRB findings.

### 22.7 22.7 Applied note

Kill-dates on temporary flows page both the owner and Sam three days prior. If nobody responds, TrackScope marks the flow expired and denies tests that relied on it until renewed in writing.

### 22.8 22.8 Secret scanning cadence

Repo secret scans run on TRB-owned code listed in ROE. Sam opens findings for keys with no owner in the asset model.

### 22.9 22.9 Expiry page text

Pages for kill-dates include the original business reason. Renewals without reasons are denied.

### 22.10 22.11 Scene

Kill-date pages fire; the owner is on leave. Backup owner renews with a reason. Sam notes the backup-owner field as mandatory going forward — single-owner expiry pages are fragile.

### 22.11 22.12 Extension

Expiry without reason was denied; the owner wrote "PCI segmentation project delay". Now the risk is visible, not eternal.

### 22.12 22.14 Note 11

Backup owners must acknowledge in the ticket UI; silence is not acceptance.

### 22.13 22.16 Pad

Mandatory backup-owner fields block ticket closeout. Sam loves blocking closeout.

### 22.14 22.18 Final

Flow expiry postmortems ask whether the original business reason still exists. If the project finished, the flow dies. If the project continues, a new kill-date is mandatory. Eternal temporary rules are renamed findings in the postmortem notes.

### Worked example (synthetic TRB)

Sam tickets UNAPPROVED web→ledger-db to network and app owners jointly.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX064 — Lab line.** Quote the UNAPPROVED lab line. *Rubric:* 3 = web -> ledger-db UNAPPROVED; 2 = partial; 1 = wrong; 0 = none.
- **EX065 — Joint ticket.** Why ticket network and app together? *Rubric:* 3 = flow needs both routing and app behaviour changes; 2 = partial; 1 = only one; 0 = none.
- **EX066 — Vendor hammer.** What if SMS vendor times out? *Rubric:* 3 = stop related checks; no retry storm; 2 = partial; 1 = flood retries; 0 = none.

### Synthesis

Dependencies and flows are owned; unapproved edges become tickets.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Methods I

### Learning outcomes

You will (1) build method cards; (2) bind methods to ROE; (3) set rate limits.

### 23.1 Cards

Purpose, ROE clause, tool/settings, stops, evidence.

### 23.2 WSTG

Select auth, session, access control themes for online banking staging.

### 23.3 Rates

Caps protect availability.

### 23.4 Forbidden

Spraying and DoS remain forbidden.

### 23.5 Quiet vs noisy

Prefer quiet methods when detection is also under test.

### 23.6 Freeze

Method set freezes after kickoff unless ROE amends.

### 23.7 23.7 Applied note

Quiet methods are preferred during purple windows so SOC signal is interpretable. Sam schedules noisy inventory scrapes on separate days. Mixing them produced a useless alert blizzard once; the calendar now prevents it.

### 23.8 23.8 Card library ownership

Each method card has an owner engineer. Unowned cards cannot be scheduled. Sam claims ownership before proposing a card in kickoff.

### 23.9 23.9 Noise budget sheet

SOC signs a noise budget per window. Exceeding it is a stop condition Sam respects immediately.

### 23.10 23.11 Scene

SOC noise budget is 30 alerts per hour. Sam's method card would generate about 80. He splits the card across two days. The SOC lead buys him coffee; the window stays green.

### 23.11 23.12 Extension

Noise budget sheet is signed like a mini-ROE. Sam treats SOC signatures with the same respect as CISO signatures.

### 23.12 23.14 Note 11

Noise budget overruns trigger an automatic method-card pause flag in TrackScope.

### 23.13 23.16 Pad

Pause flags clear only with SOC countersign. Sam cannot clear his own noise overrun.

### 23.14 23.18 Final

Method card librarianship is a rotating duty. Each month a different engineer audits five cards for ROE clause drift. Sam's audit found a card citing a retired ROE section; it was suspended in an hour.

### Worked example (synthetic TRB)

Sam's IDOR card: 1 req/s, two test users, stop on 5xx burst.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX067 — Card fields.** List five method-card fields. *Rubric:* 3 = five from chapter; 2 = three; 1 = one; 0 = none.
- **EX068 — Forbidden pair.** Name two forbidden methods. *Rubric:* 3 = spraying and DoS; 2 = one; 1 = WSTG auth; 0 = none.
- **EX069 — Freeze.** Why freeze methods after kickoff? *Rubric:* 3 = prevent silent scope/method creep; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Methods are cards bound to ROE with rates and freezes.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Controls

### Learning outcomes

You will (1) match controls to findings; (2) rank findings; (3) propose compensating controls.

### 24.1 Match

Shared admin → named accounts+vault; unapproved flow → firewall+app deny; weak MFA enrolment → enrolment fix.

### 24.2 Ranking lab

lab_rank orders F1,F3,F4 at score 6 before F2 at 3.

```python
"""Lab 24: rank synthetic TRB findings by likelihood x impact, ties by id."""
f = [("F1","Shared admin on loan system",2,3),("F2","Verbose error pages",3,1),
     ("F3","Web tier reaches ledger DB directly",2,3),("F4","Weak MFA enrolment check",3,2)]
for i,t,l,m in sorted(f, key=lambda x:(-x[2]*x[3], x[0])):
    s=l*m; print(f"{i} {s} {'high' if s>=6 else 'medium' if s>=3 else 'low':6} {t}")
```

Run with `python3 lab_rank.py`. Verified output:

```text
F1 6 high   Shared admin on loan system
F3 6 high   Web tier reaches ledger DB directly
F4 6 high   Weak MFA enrolment check
F2 3 medium Verbose error pages
```

### 24.3 Compensating

Jump-only admin while passwords uniqued.

### 24.4 Ownership

Every control has a named owner and date.

### 24.5 Verify later

Chapter 30 retests.

### 24.6 Overclaim

Do not call a control \"prevents all APT\" .

### 24.7 24.7 Applied note

Ranking meetings freeze scores before discussion of personalities. Sam collects scores silently, then reveals. Lobbying to demote a finding because a team is "busy" happens after scores, where it is visible as risk acceptance.

### 24.8 24.8 Acceptance language

Risk acceptance uses a form with amount, expiry and CISO signature. Verbal "we'll live with it" does not close F3.

### 24.9 24.9 Rank reveal

Scores display only after all raters submit. Sam's facilitation script blocks early reveals.

### 24.10 24.11 Scene

Rank reveal shows F2 last. The web team still wants F2 fixed first because it is easy. Sam records easy-but-low as a separate "hygiene" track so it does not displace F3's funding.

### 24.11 24.12 Extension

Hygiene track fixed F2 in three days without stealing the F3 budget meeting. Parallel tracks keep easy work from starving hard work.

### 24.12 24.14 Note 11

Hygiene track WIP limits keep it from becoming a dumping ground for ignored risk.

### 24.13 24.16 Pad

Hygiene WIP limit is three. Fourth easy fix waits. Focus is a control.

### 24.14 24.18 Final

Funding boards receive ranked lists with a one-page plain-language cover. Sam practices the cover aloud until he can deliver it in ninety seconds. Boards remember the cover longer than the appendix.

### Worked example (synthetic TRB)

Sam presents ranked list; board funds F1/F3/F4 first.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX070 — Rank order.** Which finding ranks last in the lab? *Rubric:* 3 = F2; 2 = F1; 1 = F4; 0 = none.
- **EX071 — Compensating.** Give a compensating control for shared admin. *Rubric:* 3 = jump-only/MFA/monitoring while uniquing; 2 = partial; 1 = ignore; 0 = none.
- **EX072 — Score.** What is F4's score and band? *Rubric:* 3 = 6 high; 2 = 6; 1 = 3; 0 = none.

### Synthesis

Controls match findings; ranking drives funding; compensating controls buy time.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) run scope, Wilson and flow labs under supervision; (2) peer-check; (3) refuse bad evidence.

### 25.1 Notebook

Outputs of lab_scope, lab_wilson, lab_flows with initials.

### 25.2 Peer check

Compare scope classifications.

### 25.3 Planted fault

Refuse mismatched hash evidence.

### 25.4 Time box

Two hours hard stop.

### 25.5 No production

Live TRB scanning fails the lab.

### 25.6 Sign-off

Supervisor signs on discipline, not novelty.

### 25.7 25.7 Applied note

Lab I planted faults include a scope file with SWIFT removed from exclusions. Learners who do not notice fail. Sam failed that variant once as a student and now writes exclusions first every time.

### 25.8 25.8 Notebook hashes

Lab notebooks include hashes of the lab scripts used. Version skew is a common excuse Sam removes by pinning hashes.

### 25.9 25.9 Peer SWIFT trap

The planted scope variant is rotated so word cannot spread between sittings. Sam keeps three variants.

### 25.10 25.11 Scene

Lab I variant B hides an exclusion by renaming SWIFT to "pay-gw-01". Learners who only string-search "SWIFT" fail. Sam teaches exclusion by asset id, not by marketing name.

### 25.11 25.12 Extension

Variant C uses an exclusion listed only in an appendix table. Learners who skip appendices fail. Sam loves appendix discipline.

### 25.12 25.14 Note 11

Asset-id exclusions are printed on the lab desk laminated card.

### 25.13 25.16 Pad

Laminated cards are versioned; old cards are hole-punched as void.

### 25.14 25.18 Final

Laboratory I briefings show a failed notebook from a prior year (with permission) where hashing was skipped. Seeing a real fail is more persuasive than a rubric bullet. Sam thanks the alumnus who allowed the anonymised share.

### Worked example (synthetic TRB)

Sam refuses planted bad evidence and catches a peer marking SWIFT in scope.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX073 — Labs used.** Which three labs are in the notebook? *Rubric:* 3 = scope, wilson, flows; 2 = two; 1 = one; 0 = none.
- **EX074 — Fail condition.** What fails Lab I immediately? *Rubric:* 3 = live/production scanning; 2 = partial; 1 = finishing early; 0 = none.
- **EX075 — SWIFT mistake.** What should a peer marking SWIFT in scope be told? *Rubric:* 3 = EXCLUDED; remove; 2 = partial; 1 = ok; 0 = none.

### Synthesis

Lab I grades authorization discipline and evidence integrity.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Methods II

### Learning outcomes

You will (1) chain findings ethically; (2) stop at minimum proof; (3) document chains.

### 26.1 Chaining

Only inside ROE; stop at impact proof.

### 26.2 Minimum proof

No extra pivoting \"for fun\".

### 26.3 Documentation

Chain diagram in appendix with times.

### 26.4 Detection goals

Note whether SOC saw stages — purple synergy.

### 26.5 Payment adjacency

Extra approvals before anything payment-near.

### 26.6 No exploit kit

Course still provides no exploit development.

### 26.7 26.7 Applied note

Chain diagrams use the same asset ids as FindingsDesk. Freehand hostnames caused a broken link in an appendix once; ids made the appendix mechanically checkable.

### 26.8 26.8 Impact catalogue

Allowed impact proofs for chains are catalogued (cross-user read, config change). "Domain admin" is not an allowed classroom impact at TRB.

### 26.9 26.9 Stop-on-impact banner

Method cards show a banner "stop when impact proven". Sam measures average steps after impact; fewer is better.

### 26.10 26.11 Scene

After impact proof on cross-user read, Sam's next action is stop, not pivot to admin. His chain appendix's last box is green "STOP — impact shown". Juniors copy the box into their cards.

### 26.11 26.12 Extension

Impact catalogue forbids ransomware simulation on bank networks in coursework. Someone always asks; the catalogue answers before Sam must.

### 26.12 26.14 Note 11

STOP boxes are green on purpose — restraint is success, not failure.

### 26.13 26.16 Pad

Green STOP boxes are stickers juniors put on printed cards. Culture is tactile.

### 26.14 26.18 Final

Chain ethics posters hang in the jump room: "Impact then stop". Visitors sometimes laugh; operators do not. Sam watches new contractors read the poster before their first chain.

### Worked example (synthetic TRB)

Sam chains unapproved flow + weak session control to show cross-user read risk, then stops.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX076 — Minimum proof.** What does minimum proof mean? *Rubric:* 3 = stop once impact shown; no extra pivot; 2 = partial; 1 = full takeover always; 0 = none.
- **EX077 — Payment-near.** What extra step before payment-adjacent tests? *Rubric:* 3 = extra approvals/ROE check; 2 = partial; 1 = none; 0 = none.
- **EX078 — Chain doc.** What belongs in the chain appendix? *Rubric:* 3 = steps/times/evidence links; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Chains stay inside ROE, prove impact minimally and document clearly.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Verification

### Learning outcomes

You will (1) plan retests; (2) read coverage labs; (3) close only with evidence.

### 27.1 Retest

Same methods, agreed window.

### 27.2 Coverage lab

lab_coverage flags T1190 GAP.

```python
"""Lab 27: summarise synthetic purple-team results per ATT&CK technique."""
runs = [("T1078",True),("T1078",True),("T1078",False),("T1566",True),("T1566",False),("T1190",False),("T1190",False)]
from collections import defaultdict
d = defaultdict(lambda:[0,0])
for t, hit in runs: d[t][1]+=1; d[t][0]+=hit
for t in sorted(d): k,n=d[t]; print(f"{t} detected {k}/{n} {'GAP' if k/n<0.5 else 'ok'}")
```

Run with `python3 lab_coverage.py`. Verified output:

```text
T1078 detected 2/3 ok
T1190 detected 0/2 GAP
T1566 detected 1/2 ok
```

### 27.3 Closure

FIXED with evidence or accepted risk signed.

### 27.4 Partial

STILL OPEN keeps ticket alive.

### 27.5 Scope freeze

No new hunt on retest day.

### 27.6 Communicate

Same-day owner note.

### 27.7 27.7 Applied note

GAP stories offered to SOC include log source, technique and a sample detection idea — not a demand to "buy a tool". Sam's T1190 note pointed at WAF and origin logs already licensed.

### 27.8 27.8 Retest calendar

Retest windows are booked when findings file, not after owners panic. Sam's template suggests a date 14 days out.

### 27.9 27.9 GAP to backlog

GAP rows create detection backlog items with technique ids. PulseMap links to those items.

### 27.10 27.11 Scene

T1190 GAP with n=2 becomes a detection spike story: "instrument WAF bypass logs". Two weeks later SOC has a rule in staging. Small n still can drive engineering if framed as a gap, not a doom claim.

### 27.11 27.12 Extension

Retest calendar invites include the method card hash so owners prepare the same build. Version skew is the enemy of honest FIXED.

### 27.12 27.14 Note 11

Detection backlog items link both ways to PulseMap GAP rows.

### 27.13 27.16 Pad

Method card hashes in invites are SHA-256 prefixes of eight hex chars — enough to spot skew.

### 27.14 27.18 Final

Detection backlog grooming includes PulseMap once a sprint. GAP rows without backlog ids are defects in the grooming, not in the SOC. Sam files those defects against the platform process.

### Worked example (synthetic TRB)

PulseMap-style lab shows T1190 0/2 GAP; SOC prioritises public-facing detection engineering.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX079 — GAP line.** What does the lab print for T1190? *Rubric:* 3 = detected 0/2 GAP; 2 = partial; 1 = ok; 0 = none.
- **EX080 — T1078.** Is T1078 GAP or ok in the lab? *Rubric:* 3 = ok (2/3); 2 = GAP; 1 = missing; 0 = none.
- **EX081 — Closure rule.** When may a finding close as FIXED? *Rubric:* 3 = retest evidence shows closed; 2 = partial; 1 = owner email only; 0 = none.

### Synthesis

Verification mixes retest honesty with detection coverage gaps.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Failure analysis

### Learning outcomes

You will (1) classify tool/process/people causes; (2) run blameless reviews; (3) turn causes into fixes.

### 28.1 Causes

Tool misconfig, process gaps, unclear ROE, skill gaps — rarely \"bad people\".

### 28.2 Timeline

Facts first.

### 28.3 Blameless

Seek systemic fixes.

### 28.4 Drift vs attack

Decide with evidence.

### 28.5 Actions

Owner + date per cause.

### 28.6 Platform

TrackScope bugs get engineering tickets too.

### 28.7 28.7 Applied note

Failure reviews invite the platform on-call even when the mistake looks human. Often the UI invited the error. Sam's TrackScope copy change after one review cut a class of scope mis-clicks.

### 28.8 28.8 UI affordances

If three analysts make the same TrackScope mistake, UX changes before more training. Sam files UX tickets with screenshots of the confusing control.

### 28.9 28.9 Five whys cap

Reviews stop at five whys or first actionable systemic fix. Endless why theatre is cut.

### 28.10 28.11 Scene

Five whys on the stale inventory stop at "CMDB API had no schema version field". Action: add schema version and a TrackScope checksum. Training the intern who imported the stale file is not the primary action.

### 28.11 28.12 Extension

UX ticket from failure review changed a dropdown default from "allow" to "deny". Mis-clicks dropped the following month. Defaults are destiny.

### 28.12 28.14 Note 11

UX tickets require a before/after screenshot of the control that confused people.

### 28.13 28.16 Pad

Before/after UX screenshots live in the same vault path as engagement evidence with a ux- prefix.

### 28.14 28.18 Final

Failure review templates force a "platform or process change?" checkbox. If neither is checked, the review is incomplete. Training-only outcomes need explicit justification.

### Worked example (synthetic TRB)

A false production hit trace shows a stale inventory feed; Sam files platform + CMDB actions.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX082 — Blameless.** What does a blameless review seek? *Rubric:* 3 = systemic fixes not punishment; 2 = partial; 1 = scapegoat; 0 = none.
- **EX083 — Action form.** What two fields must each corrective action have? *Rubric:* 3 = owner and date; 2 = one; 1 = none; 0 = none.
- **EX084 — Stale feed.** Why can stale inventory cause a production hit? *Rubric:* 3 = wrong host classified in scope; 2 = partial; 1 = cannot; 0 = none.

### Synthesis

Failure analysis produces owned systemic fixes, including to the platform.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Operations

### Learning outcomes

You will (1) run day-of workflow; (2) coordinate SOC; (3) hand over between shifts.

### 29.1 Kickoff

Confirm ROE, contacts, window.

### 29.2 Logging

Contemporaneous activity log.

### 29.3 SOC

Start/stop messages; expect alert noise coordination.

### 29.4 Handover

Log + vault beats verbal notes.

### 29.5 End

Hard stop at window end.

### 29.6 On-call hygiene

Sleep and spare credentials matter on multi-day tests.

### 29.7 29.7 Applied note

Hard-stop drills include pulling the network cable on the jump host at T-minus zero. Sam's muscle memory is to stop typing before arguing for five more minutes. Arguments happen in the next ROE, not in overtime.

### 29.8 29.8 Channel etiquette

Engagement chat forbids joke screenshots of customer data. Sam moderates with a pinned rule and one warning.

### 29.9 29.9 Hours counter

A bot announces hours worked in-window. Crossing the max posts a stop reminder.

### 29.10 29.11 Scene

At 16:55 Sam's unfinished card is written as "next window". At 17:00 the cable-pull drill begins. He has already hit save. The drill is boring when preparation is good.

### 29.11 29.12 Extension

Hours counter at 9.5 hours posts "wind down". At 10 it posts "hard stop approaching". Sam winds down. Machismo is out of policy.

### 29.12 29.14 Note 11

Wind-down posts include a link to the unfinished-card template.

### 29.13 29.16 Pad

Unfinished-card template includes ROE id so next window inherits authorization context.

### 29.14 29.18 Final

Shift handovers use a five-line paste template. Sam rejects freeform novels. The next operator should be productive in three minutes, not thirty.

### 29.15 29.19 Boost

Hard-stop culture includes thanking people who stop early with unfinished work. Sam's retrospective shout-outs name the unfinished cards that respected the clock. Overtime heroes are coached, not praised. The difference shows up in fewer emergency change tickets after test weeks and in SOC analysts who still trust the engagement calendar.

### 29.16 29.20 Extra

Shout-outs for early stops appear in the monthly ops newsletter.

### Worked example (synthetic TRB)

Sam's stop at 17:00 leaves an unfinished card scheduled for the next authorized window only.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX085 — Start message.** Name four facts in a start message. *Rubric:* 3 = id, scope, window, contact; 2 = three; 1 = one; 0 = none.
- **EX086 — Hard stop.** What if work remains at window end? *Rubric:* 3 = stop; reschedule authorized window; 2 = stop; 1 = overrun; 0 = none.
- **EX087 — Handover medium.** What two artifacts make a safe shift handover? *Rubric:* 3 = activity log and vaulted evidence; 2 = one; 1 = verbal only; 0 = none.

### Synthesis

Operations are kickoff, logged work, SOC visibility and hard stops.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) run ranking and retest labs; (2) pass a stop drill; (3) file a mini report.

### 30.1 Build

lab_rank + lab_retest + one-page report.

### 30.2 Stop drill

Compliant message within two minutes.

```python
"""Lab 30: compare synthetic before/after statuses for a TRB retest."""
before={"F1":"open","F3":"open","F4":"open"}; after={"F1":"closed","F3":"open","F4":"closed"}
for k in sorted(before): print(k, before[k], "->", after[k], "FIXED" if after[k]=="closed" else "STILL OPEN")
print("fixed", sum(after[k]=="closed" for k in before), "of", len(before))
```

Run with `python3 lab_retest.py`. Verified output:

```text
F1 open -> closed FIXED
F3 open -> open STILL OPEN
F4 open -> closed FIXED
fixed 2 of 3
```

### 30.3 Honesty

Leave STILL OPEN open.

### 30.4 Peer pressure

Refuse mismatched evidence.

### 30.5 Time box

Two hours.

### 30.6 Pass bar

Stop + honesty + coherent report.

### 30.7 30.7 Applied note

Lab II peer pressure scripts include "the hash is only off by one character". Sam's refused answer is always re-capture. Close-enough hashes are how evidence loses court and regulator trust.

### 30.8 30.8 Report skeleton

Lab II reports use a skeleton with REQUIRED markers. Missing STILL OPEN explanation fails the automated check Sam wrote.

### 30.9 30.9 Skeleton CI

PRs of Lab II reports fail CI if REQUIRED sections are empty. Sam likes mechanical honesty.

### 30.10 30.11 Scene

Lab II CI rejects a report that marks F3 closed with comment "owner said so". Sam's error message quotes the course rule. Mechanical enforcement beats sermonising.

### 30.11 30.12 Extension

Skeleton CI looks for the string STILL OPEN when lab_retest would show open items. Students cannot hide openness by omission.

### 30.12 30.14 Note 11

CI message quotes the rule number from the course handbook.

### 30.13 30.16 Pad

Handbook rule numbers in CI make appeals easy: cite the rule, do not argue with the bot.

### 30.14 30.18 Final

Laboratory II debriefs vote on the best refusal of the day. The winner explains their wording. Celebrating refusal makes the next one easier.

### 30.15 30.20 Extra

Best-refusal vote winners get to update the refusal example card.

### Worked example (synthetic TRB)

lab_retest shows F1/F4 FIXED, F3 STILL OPEN; Sam's report keeps F3 open.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX088 — Retest counts.** How many FIXED vs STILL OPEN? *Rubric:* 3 = 2 FIXED, 1 STILL OPEN; 2 = partial; 1 = all fixed; 0 = none.
- **EX089 — Stop limit.** Stop message time limit? *Rubric:* 3 = two minutes; 2 = fast; 1 = next day; 0 = none.
- **EX090 — F3 handling.** May the report close F3 without evidence? *Rubric:* 3 = no; 2 = no; 1 = yes; 0 = none.

### Synthesis

Lab II stresses stopping fast and reporting honest retest results.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Advanced cases

### Learning outcomes

You will (1) analyse multi-finding cases; (2) prioritise under board pressure; (3) keep ethics when optics collide.

### 31.1 Packet

Ranked findings, unfinished retest, board asking to bury F3 before earnings.

### 31.2 Ethics

Findings stay; management responses allowed beside them.

### 31.3 Prioritisation

Payment-adjacent and unapproved ledger flows first.

### 31.4 Communication

Prepare exec and engineer versions.

### 31.5 Legal

Involve legal if disclosure duties may apply — Sam escalates, does not decide alone.

### 31.6 Record

Keep the bury request in the engagement file.

### 31.7 31.7 Applied note

Pressure emails are forwarded to the CISO alias with a short factual header. Sam does not debate earnings calendars with product managers alone. The alias reply becomes the record.

### 31.8 31.8 Escalation SLA

Pressure-to-bury emails get a same-day acknowledgment from the CISO alias even if the full reply waits. Silence looks like assent.

### 31.9 31.9 Optics vs integrity

Training slides include a past anonymised bury request and the CISO reply supporting the tester. Culture is taught with artefacts.

### 31.10 31.11 Scene

The bury-request email and CISO reply are printed (redacted) in ethics class. Students see that refusal is supported. Culture is evidence, not slogans.

### 31.11 31.12 Extension

Ethics class votes on whether they would have refused; then they read the CISO reply. Most change their vote. Artefacts teach.

### 31.12 31.14 Note 11

Redacted pressure artefacts live in the ethics folder with access logs.

### 31.13 31.16 Pad

Ethics folder access logs are reviewed termly for unexpected readers.

### 31.14 31.18 Final

CISO alias response time is measured. Sam's ethics slides include the median response time to pressure emails. Slow silence is tracked as a risk to culture.

### Worked example (synthetic TRB)

Sam refuses to drop F3; offers a management response paragraph; informs supervisor and CISO.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX091 — Bury request.** Correct response to \"drop F3 until earnings\"? *Rubric:* 3 = refuse; offer management response; escalate; 2 = refuse; 1 = drop; 0 = none.
- **EX092 — First priority.** Which class of finding outranks verbose errors before earnings? *Rubric:* 3 = payment-adjacent / ledger flow issues; 2 = partial; 1 = banners; 0 = none.
- **EX093 — Record.** Why record the bury request? *Rubric:* 3 = ethics/audit trail; 2 = partial; 1 = no need; 0 = none.

### Synthesis

Advanced cases test ethics under optical pressure as much as technical skill.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Interdisciplinary interfaces

### Learning outcomes

You will (1) work with legal, HR, SOC and developers; (2) translate findings; (3) respect other professions' constraints.

### 32.1 Legal

Contracts, disclosure, privacy — Sam brings facts, not legal conclusions.

### 32.2 HR

Staff-affecting simulations need HR paths.

### 32.3 SOC

Detection engineering consumes ATT&CK tags and timelines.

### 32.4 Developers

Want reproduction and safe fix patterns.

### 32.5 Executives

Want decisions and dates.

### 32.6 Friction

Procurement and change windows are real; plan for them.

### 32.7 32.7 Applied note

Translation packets are generated from FindingsDesk fields so exec and engineer texts cannot disagree on CVSS-like scores or asset ids. Sam once found a drift of severity words between emails; templates removed it.

### 32.8 32.8 Glossary bridge

A mini glossary maps "conduit", "control", and "finding" for legal readers. Sam attaches it when legal joins late.

### 32.9 32.9 RACI snippet

Each major finding carries a tiny RACI: who fixes, who verifies, who accepts. Sam fills it in FindingsDesk fields.

### 32.10 32.11 Scene

RACI fields auto-suggest owners from the asset register. Sam still confirms with a human. Autosuggest without confirmation once mailed a finding to a former employee.

### 32.11 32.12 Extension

RACI autosuggest once chose a deactivated user; confirmation call caught it. Sam keeps the call even when busy.

### 32.12 32.14 Note 11

Confirmation calls are logged as "owner confirmed 15:04" in the ticket.

### 32.13 32.16 Pad

Owner confirmed timestamps must be during business hours unless on-call is noted.

### 32.14 32.18 Final

Interdisciplinary office hours invite legal monthly. Sam brings one finding and asks how they would phrase disclosure duties. The mutual translation compounds.

### Worked example (synthetic TRB)

Sam's F3 packet includes a firewall rule proposal for network and a code-side deny checklist for app-sec.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX094 — Legal role.** What does Sam bring to legal? *Rubric:* 3 = facts/evidence/timeline not legal conclusions; 2 = partial; 1 = legal advice; 0 = none.
- **EX095 — Dual packet.** Why both firewall and app checklist for F3? *Rubric:* 3 = needs network and app controls; 2 = partial; 1 = only one needed; 0 = none.
- **EX096 — HR path.** When must HR be involved? *Rubric:* 3 = staff-affecting simulations/phishing exercises; 2 = partial; 1 = never; 0 = none.

### Synthesis

Interdisciplinary work translates one finding into each profession's artifacts.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse purple-team results; (2) respect threats to validity; (3) report uncertainty.

### 33.1 Analysis

Use intervals; avoid p-hacking by switching metrics post hoc.

### 33.2 Validity

Staging, alert fatigue, shared accounts threaten generalisation.

### 33.3 Adaptive evaluation

Adversaries adapt; static test sets age.

### 33.4 Disclosure of limits

Every study lists limits in the abstract.

### 33.5 Data sharing

Synthetic datasets preferred for sharing.

### 33.6 Ethics revisit

Re-check approvals if methods expand mid-study.

### 33.7 33.7 Applied note

Validity sections list at least three threats every time: environment, sample size, and adversary adaptation. Sam's template will not compile the report PDF if the list has fewer than three.

### 33.8 33.8 Adaptation log

When attackers or systems change, Sam logs which static tests are stale. The log feeds the next trial's design.

### 33.9 33.9 Stale-test date

Tests carry a review-by date. Past-due tests cannot support assurance claims until refreshed.

### 33.10 33.11 Scene

Stale-test dates turn orange at thirty days and red at ninety. Red tests cannot be cited in assurance statements until re-run. Sam likes traffic lights more than paragraphs of policy.

### 33.11 33.12 Extension

Orange tests get scheduled; red tests block citations. Sam's assurance checklist literally asks "any red tests cited?" with a no-box required.

### 33.12 33.14 Note 11

Traffic-light API is queried by the report build; red citations fail the build.

### 33.13 33.16 Pad

Report builds call the traffic-light API; offline builds fail closed.

### 33.14 33.18 Final

Research office hours ban the word "prove" unless a pre-registered threshold is cited. Sam rings a small bell. The room self-corrects by week three.

### Worked example (synthetic TRB)

Sam reports T1190 GAP with n=2 and refuses to claim \"zero detection forever\".

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX097 — Post hoc.** Why not change the success metric after seeing data? *Rubric:* 3 = p-hacking / biased claim; 2 = partial; 1 = fine; 0 = none.
- **EX098 — n=2.** How should Sam talk about n=2 GAP? *Rubric:* 3 = honest small-n uncertainty; 2 = partial; 1 = proof of zero forever; 0 = none.
- **EX099 — Adaptive.** Why do static test sets age? *Rubric:* 3 = adversaries and systems change; 2 = partial; 1 = they do not; 0 = none.

### Synthesis

Research honesty is intervals, listed limits and stable metrics.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two assessment approaches; (2) use TRB criteria; (3) recommend a mix.

### 34.1 Options

Quarterly WSTG-style web test vs annual threat-led scenario exercise.

### 34.2 Criteria

Cost, coverage, detection learning, operational risk, examiner expectations.

### 34.3 Evidence

Use synthetic past results and Wilson intervals.

### 34.4 Recommendation

Mix: keep quarterly web tests; fund threat-led every other year.

### 34.5 Non-goals

Not recommending zero testing.

### 34.6 Presentation

Ten slides, decisions last.

### 34.7 34.7 Applied note

Comparison tables include a "capacity to execute" row. Threat-led every year scored high on learning and low on capacity; every other year won. Ignoring capacity produces shelfware programmes.

### 34.8 34.8 Cost honesty

Comparison tables include staff hours, not only vendor invoices. Internal quarterly tests are not free.

### 34.9 34.9 Capacity row data

Capacity estimates come from last year's hours, not optimism. Sam cites the hours file.

### 34.10 34.11 Scene

Capacity row: last year threat-led consumed 1,200 hours. Quarterly web tests consumed 400. The mix recommendation falls out of the arithmetic more than out of fashion.

### 34.11 34.12 Extension

Hours file is exported from time tracking, not remembered. Sam's first handmade estimate was 40% low. Humility is a spreadsheet.

### 34.12 34.14 Note 11

Hours export is attached to the comparative project appendix as evidence.

### 34.13 34.16 Pad

Comparative appendices refuse handmade hour estimates without a time-tracking export hash.

### 34.14 34.18 Final

Comparative project defences ask "what would you cut first if budget halves?". Sam prepares that answer before the nice answer. Capacity thinking is the point.

### 34.15 34.19 Boost

When presenting the mix recommendation, Sam brings a one-page calendar for two years showing quarterly web tests and a shaded threat-led quarter. Visual capacity beats abstract ratios. Executives approve calendars more readily than adjectives like "robust programme". He leaves copies of the calendar in the board portal the same day.

### 34.16 34.20 Extra

Two-year calendar PDF is the artefact boards forward to finance.

### Worked example (synthetic TRB)

Sam's comparison table scores detection learning higher for threat-led and regression coverage higher for quarterly WSTG.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX100 — Higher regression.** Which approach better catches web regressions each quarter? *Rubric:* 3 = quarterly WSTG-style; 2 = threat-led only; 1 = neither; 0 = none.
- **EX101 — Detection learning.** Which tends to teach SOC more about realistic paths? *Rubric:* 3 = threat-led scenario exercises; 2 = banner scans; 1 = neither; 0 = none.
- **EX102 — Mix.** What mix does Sam recommend? *Rubric:* 3 = quarterly web + threat-led every other year; 2 = partial; 1 = zero testing; 0 = none.

### Synthesis

Comparison uses explicit criteria; the answer is usually a mix, not a silver bullet.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) write a scoped capstone proposal; (2) list non-goals; (3) define success metrics.

### 35.1 Scope

Build a scope-diff tool for TrackScope with tests and a short evaluation on synthetic inventories.

### 35.2 Non-goals

No integration with every ticket system; no exploit modules.

### 35.3 Metrics

Precision/recall on planted inventory drifts; fail-closed on corrupt files.

### 35.4 Risks

Time, data access, reviewer availability.

### 35.5 Advisor

Checkpoints every two weeks.

### 35.6 Ethics

Synthetic inventories only.

### 35.7 35.7 Applied note

Non-goals are printed on the proposal cover in bold. Sam's advisor grades whether a mid-project feature creep violated a printed non-goal. Bold text makes the violation embarrassing enough to stop.

### 35.8 35.8 Checkpoint demos

Every two weeks Sam demos fail-closed, not new UI chrome. Advisors grade control of scope creep.

### 35.9 35.9 Cover non-goals

Printers in the lab reprint non-goals posters for Sam's desk during build week.

### 35.10 35.11 Scene

Mid-build, a friend suggests adding LLM summarisation of findings. Sam points at the bold non-goals. The feature waits for a new proposal. Bold text earns its ink.

### 35.11 35.12 Extension

Non-goals poster includes "no LLM feature in v1". Visitors laugh; Sam points at the signed proposal. Laughter is fine; creep is not.

### 35.12 35.14 Note 11

Non-goals poster is photographed into the capstone repo README.

### 35.13 35.16 Pad

README photograph of non-goals must be dated within the build week.

### 35.14 35.18 Final

Proposal checkpoints include a non-goals quiz: advisor names a tempting feature; Sam must say no and point to the cover. Failing the quiz delays code merge.

### Worked example (synthetic TRB)

Sam's proposal is two pages; advisor accepts after he adds an explicit non-goal: no live TRB scanning.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX103 — Non-goal.** Name one required non-goal. *Rubric:* 3 = no exploit modules or no live scanning / no all-ticket integrations; 2 = partial; 1 = none; 0 = none.
- **EX104 — Metric.** Give one success metric for scope-diff. *Rubric:* 3 = precision/recall on planted drifts or fail-closed on corrupt files; 2 = vague; 1 = \"works\"; 0 = none.
- **EX105 — Ethics line.** What data may the capstone use? *Rubric:* 3 = synthetic inventories only; 2 = partial; 1 = production customer DB; 0 = none.

### Synthesis

Proposals win by narrow scope, non-goals and measurable success.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) complete a placement-style reflection; (2) sanitise reports; (3) translate academic methods to ops.

### 36.1 Placement

Shadow TRB assessment operations (synthetic in this course).

### 36.2 Sanitise

No customer identifiers in academic write-ups.

### 36.3 Translation

Wilson intervals become board-usable sentences.

### 36.4 Conflicts

Gift policies and vendor dinners — follow TRB rules.

### 36.5 Journal

Weekly: learned, broken assumption, question.

### 36.6 Useful output

Leave a runbook improvement behind.

### 36.7 36.7 Applied note

Leave-behind testing uses a timer: the host technician gets fifteen minutes alone. Sam may answer clarifying questions but not touch the keyboard. Keyboard touches mean the leave-behind failed.

### 36.8 36.8 Sanitisation checklist

Before academic upload, Sam runs a checklist: names, account numbers, IPs, hostnames. A peer initials it.

### 36.9 36.9 Peer initial box

Sanitisation forms without peer initials are rejected by the academic upload script.

### 36.10 36.11 Scene

Peer initials on sanitisation once caught a hostname containing a customer surname. Sam buys the peer lunch. Checklists with teeth make kindness easy.

### 36.11 36.12 Extension

Sanitisation peer once was Sam's sternest critic. He chooses stern peers on purpose. Kind peers miss surnames in hostnames.

### 36.12 36.14 Note 11

Sanitisation peer initials are a required PDF form field; blank fails upload. Sam chooses peers who previously caught his mistakes, not friends who skim. The upload script rejects forms under 10 KB as likely blank. Process pedantry protects citizens whose names must never enter academic mirrors. That sentence is the chapter's privacy oath.

### 36.13 36.16 Pad

Blank-form size gate once caught a peer who uploaded a photo of a blank table. Pedantry wins.

### 36.14 36.20 Extra

Privacy oath sentence is signed on the vault foyer card.

### Worked example (synthetic TRB)

Sam's sanitised reflection describes a stop drill without naming real customers or staff.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX106 — Sanitise.** What must academic write-ups remove? *Rubric:* 3 = customer identifiers / sensitive specifics; 2 = partial; 1 = nothing; 0 = none.
- **EX107 — Journal trio.** What three lines go in the weekly journal? *Rubric:* 3 = learned, broken assumption, question; 2 = two; 1 = one; 0 = none.
- **EX108 — Leave-behind.** Name a useful leave-behind. *Rubric:* 3 = runbook improvement / checklist; 2 = partial; 1 = malware; 0 = none.

### Synthesis

Field practice is sanitised reflection plus something the host keeps.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critique a peer dossier; (2) give actionable feedback; (3) receive critique without defensiveness.

### 37.1 Format

20 minutes present, 20 critique, 10 actions.

### 37.2 Checklist

Scope clarity, evidence hashes, severity rationale, privacy, overclaim.

### 37.3 Feedback

Specific line references; suggest fixes.

### 37.4 Receiving

Write actions; avoid debating every point live.

### 37.5 Compare

Optionally compare to a published methodology checklist (PTES/WSTG), not to Instagram lore.

### 37.6 Record

Seminar note filed with capstone.

### 37.7 37.7 Applied note

Seminar declined feedback requires a written reason the presenter accepts. "I disagree" without reason keeps the comment open. Sam's dossier once had six open comments; none remained after he wrote reasons or fixes.

### 37.8 37.8 Action expiry

Seminar actions older than fourteen days without state change page Sam. Stale actions are declined or done.

### 37.9 37.9 State machine

Comment states are open, fixed, declined, risk-accepted. Sam's tracker forbids other strings.

### 37.10 37.11 Scene

Open seminar comments page Sam at day 10. He declines one with reason "out of scope for thesis" and fixes two. Day 14 board is clear. The pager teaches closure.

### 37.11 37.12 Extension

State machine API rejects "kinda done". Sam is grateful for pedantic software when tired.

### 37.12 37.14 Note 11

Pager messages include deep links to the comment thread.

### 37.13 37.16 Pad

Deep links open the exact comment; Sam forbids "see thread" without links.

### 37.14 37.18 Final

Comment hygiene week every term closes stale threads. Sam enjoys the clean board more than new features. Closure is a deliverable.

### 37.15 37.19 Boost

Sam's seminar tracker exports a weekly CSV of open comments by presenter. Public (team-visible) open counts create gentle pressure without shame. Presenters with zero opens get a thank-you note. The social protocol closes more threads than any angry reminder ever did in prior terms.

### 37.16 37.20 Extra

Thank-you notes for zero opens are templated but personally sent.

### Worked example (synthetic TRB)

Peer catches Sam's missing denominator on a coverage slide; Sam adds it before the CISO rehearsal.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX109 — Checklist item.** Name four seminar checklist items. *Rubric:* 3 = four from chapter; 2 = three; 1 = one; 0 = none.
- **EX110 — Feedback quality.** What makes feedback actionable? *Rubric:* 3 = specific lines + suggested fix; 2 = partial; 1 = \"bad vibes\"; 0 = none.
- **EX111 — Denominator.** Why add denominators on coverage slides? *Rubric:* 3 = avoid misleading percentages; 2 = partial; 1 = decoration; 0 = none.

### Synthesis

Seminars improve dossiers through specific, recorded critique.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) build the scope-diff tool; (2) test fail-closed paths; (3) document for operators.

### 38.1 Build

Diff two synthetic inventories; flag only-in-docs / only-on-network / type conflicts.

### 38.2 Fail closed

Corrupt YAML → deny with reason.

### 38.3 Tests

Golden fixtures; no network.

### 38.4 Docs

Operator README with examples.

### 38.5 Freeze

Feature freeze before evaluation week.

### 38.6 Handover

Shadow an operator running it alone.

### 38.7 38.7 Applied note

Golden fixtures include a deliberately corrupt scope and a near-match inventory designed to trick fuzzy matching. Sam's tool must not "helpfully" merge near-matches without an explicit flag.

### 38.8 38.8 Fuzzy match flag

Near-match inventory names require --ack-fuzzy to merge. Default is to list them separately as conflicts.

### 38.9 38.9 Corrupt fixture names

Fixtures named corrupt-*.yaml must deny. A CI property test generates random corruption.

### 38.10 38.11 Scene

Random corruption property test flips bits in YAML until deny triggers. Sam watches it find a parser path that returned empty allow. Property tests are rude and helpful.

### 38.11 38.12 Extension

Corrupt fixtures include truncated files and wrong encodings. Deny must trigger on all. Sam's property test grows a new mutation each term.

### 38.12 38.14 Note 11

Each new mutation in the property test gets a name and a one-line intent.

### 38.13 38.16 Pad

Mutation names look like "trunc-mid-yaml" so failures read clearly in CI.

### 38.14 38.18 Final

Operator day uses a fresh account with no Sam aliases in shell history. If the operator needs history, docs failed. Clean accounts are honest tests.

### 38.15 38.19 Boost

Fuzzy-match acknowledgements require typing the phrase "I accept merge risk" exactly. Copy-paste from a wiki is fine; clicking through is not. Sam wants a moment of friction before inventories collapse distinct hosts into one. That friction has prevented at least one production host from inheriting a staging-only note.

### 38.16 38.20 Extra

Typed acknowledgement phrase is recorded in the audit log with username.

### Worked example (synthetic TRB)

Sam's tool on synthetic data matches lab_inv-style statuses; corrupt file exits non-zero.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX112 — Statuses.** Name three diff statuses the tool prints. *Rubric:* 3 = only-in-docs, only-on-network, type conflict/match; 2 = two; 1 = one; 0 = none.
- **EX113 — Corrupt file.** What should happen on corrupt YAML? *Rubric:* 3 = deny/fail closed with reason, non-zero exit; 2 = partial; 1 = empty success; 0 = none.
- **EX114 — Network.** May the tool open network sockets? *Rubric:* 3 = no; 2 = no; 1 = yes; 0 = none.

### Synthesis

Implementation is offline, tested, fail-closed and operator-documented.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate against pre-registered metrics; (2) run independent tests; (3) state residual risk.

### 39.1 Plan

Precision/recall on planted drifts; fail-closed cases.

### 39.2 Independent

Another student runs the evaluation script.

### 39.3 Side effects

Usability timing; false alarm burden.

### 39.4 Residual risk

Tool helps inventory hygiene; does not replace ROE discipline.

### 39.5 Report

Results vs pre-registration; no post hoc metric swaps.

### 39.6 Recommend

Adopt in staging first.

### 39.7 39.7 Applied note

Independent evaluators sign a one-line statement that Sam did not edit their run logs. The statement sits in the appendix. Trustworthy evaluation is a social protocol as much as a script.

### 39.8 39.8 Staging adoption plan

Evaluation reports include a thirty-day staging plan with owners. Tools without adoption plans are hobbies.

### 39.9 39.9 Adoption owners

Staging adoption names a service owner and a platform owner. One name is insufficient.

### 39.10 39.11 Scene

Adoption plan names Mira for service ownership and Sam for platform support. Thirty-day checklist includes two operator solo runs. Without Mira's name the plan would be fiction.

### 39.11 39.12 Extension

Solo run two failed because DNS differed in the operator's profile. README gained a DNS preamble. Solo runs find doc bugs tools miss.

### 39.12 39.14 Note 11

Thirty-day checklist items are tickets, not bullets in an email.

### 39.13 39.16 Pad

Tickets for checklist items auto-close only when solo-run evidence is attached.

### 39.14 39.18 Final

Adoption retros at day 30 ask operators what they ignored in the README. Ignored sections are deleted or rewritten, not defended.

### 39.15 39.19 Boost

Day-ten adoption check asks operators to break the tool on purpose and file the brokenness. Sam would rather hear early pain than polite silence. Two intentional break reports in the first cohort improved deny messages more than a month of speculative polish would have.

### 39.16 39.20 Extra

Intentional break reports have their own ticket type: BREAK-ADOPT.

### Worked example (synthetic TRB)

Independent run: precision 0.91 recall 0.88 on planted set; 3/3 corrupt files denied; Sam recommends staging adoption.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX115 — Independent.** Who should run the evaluation script? *Rubric:* 3 = another student/independent tester; 2 = only Sam; 1 = nobody; 0 = none.
- **EX116 — Residual.** What residual risk remains after adoption? *Rubric:* 3 = still need ROE discipline / not a substitute for authorization; 2 = partial; 1 = zero risk; 0 = none.
- **EX117 — Metric swap.** May Sam change metrics after seeing results? *Rubric:* 3 = no; 2 = no; 1 = yes; 0 = none.

### Synthesis

Evaluation is independent, pre-registered and humble about residual risk.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) structure the thesis; (2) defend limits; (3) state next steps.

### 40.1 Structure

Claim, background, method, results, limits, ethics, next steps.

### 40.2 Positioning

Inventory hygiene tooling for authorized testing programmes — not a red-team exploit framework.

### 40.3 Presentation

12 minutes + questions; time discipline.

### 40.4 Likely questions

Fail-closed demos; ethics; why no live scan; threats to validity.

### 40.5 Next steps

Integrate FindingsDesk tickets; study threat-led detection metrics.

### 40.6 Reproducibility

Appendix with synthetic data and scripts.

### 40.7 40.7 Applied note

Hostile-examiner rehearsal includes a request for a live demo against a public bank website. Sam's refusal cites law and curriculum boundaries. Peers grade the refusal's clarity under stress.

### 40.8 40.8 Question bank

Sam publishes his likely-questions list after the defence so next year's cohort rehearses better. The bank includes the public-website demo refusal.

### 40.9 40.9 Refusal recording

Rehearsal refusals are audio-recorded for self-review then deleted within 24 hours. Sam checks his voice for hesitation.

### 40.10 40.11 Scene

In rehearsal the hostile examiner opens a laptop to a public bank login. Sam closes the lid gently, cites the boundary, and continues with the fail-closed demo. Peers score the gentleness and the firmness separately.

### 40.11 40.12 Extension

Gentleness score matters: slamming the laptop would scare the room into the wrong lesson. Firm and calm is the skill under examination.

### 40.12 40.14 Note 11

Peers score calm and firm on a 0–3 rubric; Sam targets 3/3 on both.

### 40.13 40.16 Pad

Calm/firm rubric anchors include sample video clips of good refusals (internal only).

### 40.14 40.19 Boost

After the defence, Sam publishes a one-page "what I would still refuse" list next to the thesis PDF. The list includes live public-bank demos, exploit kits and unverified scanner dumps as evidence. Future students see that the boundary survives graduation. Advisors cite the list when new students ask for shortcuts.

### 40.15 40.20 Extra

What-I-refuse list is linked from STUDY_PATH near course 111.

### Worked example (synthetic TRB)

Sam's abstract states exactly what was shown: offline scope-diff accuracy on synthetic inventories and fail-closed behaviour — nothing more.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX118 — Positioning.** What is the thesis not? *Rubric:* 3 = not an exploit framework; 2 = partial; 1 = a malware kit; 0 = none.
- **EX119 — Abstract test.** What is the advisor's abstract test? *Rubric:* 3 = reader knows exactly what was shown; 2 = partial; 1 = buzzwords; 0 = none.
- **EX120 — Next course area.** Name one next-step topic Sam lists. *Rubric:* 3 = FindingsDesk integration or threat-led detection metrics; 2 = vague; 1 = exploit kits; 0 = none.

### Synthesis

The thesis claims only what the evaluation showed and rehearses hard questions.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Riverstone Transit Bank, Sam Ito and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** The in-scope set is the VLAN address set minus the singleton containing the SWIFT gateway.

**EX002.** Scope covers hosts; methods need separate permission. Password spraying is often forbidden even on in-scope hosts.

**EX003.** Coverage is 28/40 (70% of hosts touched). Misuse: treating 70% as \"70% secure\".

**EX004.** The ledger hosts and SWIFT-adjacent gateways.

**EX005.** Fail closed: deny testing until a valid scope file loads.

**EX006.** He checks the asset register and owner, not the hostname pattern alone.

**EX007.** It must remain an offline check so it cannot accidentally scan real networks.

**EX008.** Hard-coded secrets and disabling TLS verification (also unsanitised shell-outs or uncapped retries).

**EX009.** Mistakes that widen scope or leak secrets.

**EX010.** \"Multiple systems accept the same privileged password, so compromise of one grants broad access; individual accountability is unavailable.\"

**EX011.** Label it speculative or omit it until evidence exists; keep it out of the facts list.

**EX012.** He must never invent DOIs or fabricated references.

**EX013.** Confidentiality; integrity; availability.

**EX014.** There is no written authorization; access attempts can be illegal and harmful.

**EX015.** Exploit code and step-by-step attack procedures for real products.

**EX016.** The observed (src,dst) pair is not a member of the approved flow relation.

**EX017.** It shows reachability that crosses trust boundaries beyond the intended architecture.

**EX018.** It sorts by descending score then by finding id.

**EX019.** It does not fix broken application authorization or business logic.

**EX020.** They are reserved documentation addresses, safe for examples.

**EX021.** Only when the ROE allows, with minimisation of customer data.

**EX022.** Owner and evidence hash (severity also reasonable).

**EX023.** To catch schema and scope errors before any ticket is written.

**EX024.** Two analysts silently overwriting each other's ticket updates.

**EX025.** Privacy and ROE minimisation — findings need proof, not bulk personal data.

**EX026.** The retention schedule in the engagement agreement.

**EX027.** Other engagements' evidence and production customer databases.

**EX028.** `198.51.100.20   EXCLUDED`

**EX029.** Refuse; SWIFT remains excluded unless a written ROE change — which ordinary tests will not grant.

**EX030.** Scope, exclusions, methods, window, emergency contacts (data handling and audience also).

**EX031.** It bypasses the controlled, logged jump-host path.

**EX032.** They redeploy outdated agents or weak settings onto new hosts.

**EX033.** No; hypervisor access needs explicit scope.

**EX034.** `95% CI=(0.40, 0.89)`

**EX035.** Smaller n means more uncertainty, so a wider confidence interval.

**EX036.** \"We detected seven of ten test events; the true rate could reasonably be anywhere from about 40% to 90%, so we should run more trials.\"

**EX037.** T1078 Valid Accounts.

**EX038.** Review configuration and policy under the ROE.

**EX039.** Named to a person, least privilege for the method, time-bounded and vaulted.

**EX040.** It exceeds purpose and ROE minimisation; proof needs samples, not bulk data.

**EX041.** Account numbers (leaving last four if needed) and other personal identifiers.

**EX042.** They concentrate sensitive proof data attractive to attackers and insiders.

**EX043.** It rewards noise and punishes careful validation.

**EX044.** The file is unchanged since the digest was recorded.

**EX045.** Collector, description, timestamp and storage location (hash too).

**EX046.** `web -> ledger-db UNAPPROVED`

**EX047.** Deny testing until policy loads.

**EX048.** No; the processor must authorize its own systems.

**EX049.** No. TLS does not fix authorization bugs.

**EX050.** The key leaks with the repo and bypasses proper key custody.

**EX051.** Integrity checks on evidence files.

**EX052.** It is not specific or measurable.

**EX053.** The metric, threshold and trial design.

**EX054.** CISO and HR approval under a written ROE.

**EX055.** As a late/final stage after the technical stages.

**EX056.** TIBER-EU and CBEST.

**EX057.** It is time-bounded, coverage-limited and invalidated by later change.

**EX058.** The report is a fact; nation-state possession is a guess without evidence.

**EX059.** It is out of scope and a privacy violation; TRB can reset its own credentials without reading it.

**EX060.** A bank VPN password exposed outside TRB risks unauthorized access to banking systems.

**EX061.** Compare configurations and run agreed tests with owners — do not assume.

**EX062.** It is out of scope for the engagement, so modelling it invites accidental testing.

**EX063.** Web, mobile API and staff VPN (batch peers also).

**EX064.** `web        -> ledger-db  UNAPPROVED` (chapter 22 emphasis).

**EX065.** Fixing an unapproved flow may need both firewall/routing and application changes.

**EX066.** Stop related checks and avoid retry storms.

**EX067.** Purpose, ROE clause, tool/settings, stop conditions, evidence expected.

**EX068.** Password spraying and denial-of-service tests.

**EX069.** To prevent silent expansion of techniques beyond what was authorized.

**EX070.** F2 (verbose error pages) with score 3.

**EX071.** Restrict admin to jump hosts and require MFA while passwords are made unique.

**EX072.** Score 6, band high.

**EX073.** lab_scope, lab_wilson and lab_flows.

**EX074.** Attempting to scan live TRB systems.

**EX075.** SWIFT is EXCLUDED and must be removed from the plan.

**EX076.** Demonstrate impact with the least action, then stop.

**EX077.** Explicit extra approvals and ROE confirmation.

**EX078.** Ordered steps with times and evidence links.

**EX079.** `T1190 detected 0/2 GAP`

**EX080.** ok — detected 2/3.

**EX081.** When retest evidence shows the issue is closed.

**EX082.** Systemic fixes rather than individual blame.

**EX083.** Owner and due date.

**EX084.** A production host may be wrongly marked in scope if inventory is stale.

**EX085.** Engagement id, scope reminder, window and tester contact.

**EX086.** Stop and reschedule into a new authorized window.

**EX087.** The activity log and vaulted evidence index.

**EX088.** F1 and F4 FIXED; F3 STILL OPEN (fixed 2 of 3).

**EX089.** Two minutes.

**EX090.** No. F3 stays open.

**EX091.** Refuse to remove it, offer a management response beside it, and escalate the request.

**EX092.** Payment-adjacent and unapproved ledger-flow findings.

**EX093.** It creates an audit trail if pressure recurs and protects the integrity of the assurance process.

**EX094.** Facts, evidence and timeline — not legal conclusions.

**EX095.** Unapproved web→ledger access may need both network enforcement and application-layer denial.

**EX096.** When simulations affect staff (for example phishing exercises).

**EX097.** It biases claims (p-hacking) and violates pre-registration.

**EX098.** As a small-sample gap needing more trials, not proof of permanent zero detection.

**EX099.** Adversaries and systems change, so old tests miss new behaviours.

**EX100.** Quarterly WSTG-style web tests.

**EX101.** Threat-led scenario exercises.

**EX102.** Keep quarterly web tests and fund threat-led exercises every other year.

**EX103.** No exploit modules (or no live TRB scanning; or no integration with every ticket system).

**EX104.** Precision and recall on planted inventory drifts, or fail-closed behaviour on corrupt scope files.

**EX105.** Synthetic inventories only.

**EX106.** Customer identifiers and other sensitive specifics.

**EX107.** One learning, one broken assumption and one question for the supervisor.

**EX108.** A runbook improvement or checklist the team can use without Sam.

**EX109.** Scope clarity, evidence hashes, severity rationale and privacy (overclaim also).

**EX110.** It points to specific lines and suggests a concrete fix.

**EX111.** Percentages without denominators mislead decision makers.

**EX112.** only-in-docs, only-on-network and type-conflict (and match).

**EX113.** Fail closed with a clear reason and a non-zero exit code.

**EX114.** No. It must run offline on local files.

**EX115.** Another student or independent tester.

**EX116.** The tool does not replace ROE discipline or authorization checks.

**EX117.** No. Metrics stay as pre-registered.

**EX118.** It is not a red-team exploit framework.

**EX119.** A reader should know exactly what was shown and what was not.

**EX120.** Integrating FindingsDesk tickets or studying threat-led detection metrics.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v3.1 Specification Document. <https://www.first.org/cvss/v3.1/specification-document>
- MITRE ATT&CK, including T1078 Valid Accounts. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
