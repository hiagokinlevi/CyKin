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

A written authorization is a set of systems. Membership is binary for each target: in scope or not. Unions of ranges and exclusions (subtracted sets) are how Riverstone Transit Bank (TRB) writes its ROE. If SWIFT sits in the same /26 as a web host, exclusion is set difference, not a vague note. Writing the scope this way also makes it testable: Sam can feed any proposed address to a membership function and get a yes or no. A note saying 'avoid SWIFT' cannot be tested; the set {/26} minus {SWIFT host} can.

### 1.2 Logic of authorization

Permission is necessary for testing; it is not sufficient for every method. "In scope" and "method allowed" must both be true. Confusing the two leads to unauthorized techniques on authorized hosts. At TRB, a host can sit inside the signed /26 while the ROE still forbids password spraying or denial-of-service checks against it. Sam therefore keeps two lists in TrackScope, one of hosts and one of permitted methods, and a test runs only when the pair appears in both. A request to spray credentials against an in-scope web host fails on the second list, and the rejection message names the clause that forbids it.

### 1.3 Counting coverage

If 40 hosts are in scope and 28 were touched by method cards, coverage is 28/40. Percentages without denominators mislead examiners and boards. Written as 28/40, the figure tells a reader that twelve in-scope hosts received no method card at all. Written as 70%, it invites the question 'of what?', and a board member may read it as 70% safe. Sam's reports therefore always show the numerator and denominator together, and list the twelve untouched hosts by owner so they can be scheduled for the next authorized window instead of silently dropped from the story.

### 1.4 Invalid leaps

"The scanner found nothing, so we are safe" confuses absence of evidence with evidence of absence. Wilson intervals in Chapter 12 make small-sample humility numerical. A clean scan over 28 of 40 hosts says nothing about the twelve that were never touched, and little about techniques the scanner cannot see. Sam rewrites such claims as bounded statements: 'no findings of the checked types on the 28 hosts tested in this window'. The bounded version is less comforting, but it is the only one the evidence supports, and it tells the reader exactly where the next test should look.

### 1.5 Practice

Sam Ito, engineering intern on TRB's authorized assessment platform team, translates every ROE sentence into sets before any tool runs. In practice that means each ROE sentence becomes a line in his notebook: the set it names, the exclusions it subtracts and the methods it allows. The /26 minus the SWIFT host at .20 is one such line. Only when every sentence has been translated, and the translation checked against the signed document by a second person, does he load anything into TrackScope. Ambiguous sentences go back to the ROE owner as questions, not guesses.

### 1.6 Why maths here

Later chapters on probability, architecture and evaluation reuse the same careful language. Sloppy scope language produces sloppy tests. The coverage fraction from 1.3 returns as a proportion with an interval in Chapter 12, and the set expression from 1.1 becomes the TrackScope membership function in the labs. Learning the vocabulary once, carefully, means each later tool has a precise specification behind it rather than a habit. Sam's notebook from this chapter is the first artefact his mentor reviews. A vague definition costs little to fix in the notebook, but the same vagueness in TrackScope could put a SWIFT host in scope.

### 1.7 Applied note

Sam practices translating ROE paragraphs into membership tests on paper before opening TrackScope. When a sentence says "web VLAN except payment gateways", he writes the set expression and lists every known gateway address from the asset register. Only then does he load the scope file. Contractors who skip the paper step regularly propose hosts that sit beside SWIFT "because the ping worked". The paper step is slower and prevents newspaper incidents. The asset register list doubles as evidence afterwards. Auditors can match each scope-file load to the signed register list, so any host added later stands out.

### 1.8 Worked set arithmetic

Given VLAN V and exclusions E, Sam computes V\E and then intersects with the day's proposed list P. Only P∩(V\E) may be loaded. He unit-tests the calculator with SWIFT inside V and confirms it never appears in output. A second test puts an address outside V into P and confirms it is rejected too. Together the two tests cover the two ways scope fails: excluded hosts leaking back in, and out-of-range hosts arriving in a friendly spreadsheet. The calculator's output is saved with the date so the day's loaded list can be reproduced later.

### 1.9 1.11 Scene

On Monday Sam receives a spreadsheet of "interesting hosts" from a branch IT lead. He does not import it. He rebuilds scope from the signed ROE: the /26, minus SWIFT at .20, intersected with hosts that have owners in the asset register. Three spreadsheet rows vanish as out of scope; one vanishes as excluded. He sends the filtered list back with the set expression in the email. The branch lead is annoyed for ten minutes and grateful when a fourth row is recognised as a mis-typed payment console. Paper set arithmetic scales better than trust.

### Worked example (synthetic TRB)

Sam writes SCOPE = 198.51.100.0/26 minus {198.51.100.20}. A proposed host 198.51.100.70 fails membership; he rejects it before the kickoff call.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX001 — Set difference.** Express TRB's web VLAN scope with SWIFT excluded as a set operation. *Rubric:* 3 = VLAN set minus {SWIFT}; 2 = partial; 1 = union; 0 = none.
- **EX002 — Necessary vs sufficient.** Why is "host in scope" not enough to run password spraying? *Rubric:* 3 = method must also be allowed; spraying may be forbidden; 2 = partial; 1 = it is enough; 0 = none.
- **EX003 — Coverage fraction.** 28 of 40 hosts touched — write the coverage and one misuse of "70%". *Rubric:* 3 = 28/40=0.7; misuse e.g. implying safety; 2 = fraction only; 1 = wrong; 0 = none.

### Synthesis

Scope is set membership; methods need their own truth; coverage needs denominators.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) map TRB's computing layers; (2) place the assessment platform; (3) explain why ledger hosts differ from web hosts.

### 2.1 Layers

Branches use thin clients; staff use managed PCs; apps run on VMs; the ledger sits on hardened hosts with change control measured in weeks. Testers who treat every host like a lab VM cause outages. A scan rate that is harmless against a test VM can starve a ledger host whose change window is weeks away. Sam therefore records each host's layer in the scope file, and TrackScope applies stricter limits to the ledger tier than to web hosts. Thin clients add little attack surface but much dependency.

### 2.2 Assessment platform

TrackScope (scope checker), FindingsDesk (tickets) and PulseMap (ATT&CK coverage) are TRB's synthetic platform Sam helps build. They run on isolated infrastructure and must fail closed on scope. Failing closed means that when TrackScope cannot load its scope file it denies every request rather than allowing all. Sam treats that as the platform's most important property: a dashboard outage is an inconvenience, but a scope checker that defaults to allow could send test traffic to SWIFT-adjacent hosts. FindingsDesk and PulseMap inherit the same rule.

### 2.3 Trust boundaries

Internet to web tier, web to core API, jump hosts to ledger-adjacent admin — each crossing is a place findings appear. At each crossing Sam asks what the next layer trusts about the previous one. The web tier trusts that internet requests are anonymous; the core API trusts that web-tier calls are already authenticated; ledger-adjacent admin trusts that the jump host verified the operator. A finding usually sits where one of those assumptions is false, so Sam's method cards are organised by boundary rather than by tool, and each card names the trust assumption it tests.

### 2.4 Fragility

Ledger and SWIFT-adjacent systems are usually out of ordinary pentest scope or gated by extreme controls. NIST SP 800-115 still applies to planning even when technical intensity is low. For TRB, that means the ROE may allow only document review and configuration reading near the ledger, with no active scanning at all. Planning still covers who approves, which evidence is collected and how a stop is called. Low intensity does not mean low rigour; it means the rigour moves into preparation and review.

### 2.5 Inventory drift

Cloud projects add tenants faster than diagrams update. Authorized testing against stale diagrams is a process finding. When a new cloud tenant appears in billing data but not in the diagram used to write the ROE, the scope is already out of date. Sam reports that as a process finding in its own right: the bank cannot protect, or authorize testing of, systems it has not recorded. He compares the asset register with billing exports each month and sends differences to the ROE owner before the next window opens.

### 2.6 Practice rule

Sam never assumes a hostname's layer from its name alone; he checks the asset register. A host called web-test-03 may in fact sit in the ledger tier after a migration, and a host called ledger-legacy may have been retired. Only the register, with its named owner and layer, decides how TrackScope treats a host. When the register and the name disagree, Sam asks the owner and records the answer before testing. Name-based guesses are logged as near-misses when caught. The owner's answer is copied into the scope file's comments.

### 2.7 Applied note

PulseMap's fail-closed rule is tested in CI by deleting the scope file and asserting every API returns deny. Sam added that test after a staging misconfiguration briefly served empty allow lists. Dashboards that cannot deny are worse than no dashboards. He demos the deny path to every new intern in their first week. The CI test also covers a corrupted file, not just a missing one. Both paths must return deny on every endpoint, including the health check, before the build is allowed to pass.

### 2.8 Platform zoning

TrackScope, FindingsDesk and PulseMap sit in an assessment zone with controlled conduits to staging only. Sam reviews those conduits each quarter the same way he reviews TRB business flows — because the platform can hurt the bank if miswired. A conduit from the assessment zone to production would let a misconfigured job send traffic to live systems, so its absence is checked, not assumed. Each review records which conduits exist, who approved them and when they were last used. Unused conduits are removed rather than left open for convenience.

### 2.9 Denominator bug

A PulseMap bug once defaulted n to 1. Sam's regression test sets n=0 and expects an error tile, not 100%. With n defaulting to 1, a single touched host would have shown as 100% coverage, exactly the misleading percentage Chapter 1 warns against. The regression test now runs on every build, and PulseMap refuses to draw a coverage tile without an explicit denominator from the scope file. An error tile is honest; a confident number built on a default is not. The fix shipped with a changelog entry naming the bug.

### 2.10 2.11 Scene

During a platform game day Sam kills the FindingsDesk database. TrackScope continues to deny out-of-scope requests using its local cache while queueing drafts to disk. PulseMap shows a degraded banner. No test traffic is allowed to "fail open" just because a ticket system is down. The game day note becomes a sales slide for why assessment tooling is safety tooling. The cache itself has a time limit, so a long outage eventually denies everything. After the drill, the team writes down how long the cache may be trusted and who decides when it expires.

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

Sam automates scope membership checks, hash verification and finding ranking — never exploitation. Each automated check replaces a manual step that people skip when tired: is this address in the signed /26, does this evidence file still match its recorded hash, which open findings rank highest by severity and asset? None of these scripts sends traffic to a target. Keeping automation on the safe side of that line means a bug in Sam's code can mislabel a report, but cannot reach the ledger or SWIFT.

### 3.2 Unsafe patterns

No hard-coded secrets, no disabled TLS verification, no unsanitised shell-outs to scanners, no retries without caps. Each rule maps to a real failure: a hard-coded key ends up in a repository, disabled TLS verification hides an interception, a hostname passed to a shell can carry extra commands, and an uncapped retry loop can turn a polite check into a flood against a fragile host. Sam's review checklist lists these four by name so reviewers look for them first, and CI rejects the two that can be detected automatically before any human reads the code.

### 3.3 Synthetic first

Every tool runs on documentation-range addresses and fake files before any engagement window. Documentation ranges such as 198.51.100.0/24 cannot route to real hosts, so a mistake during development reaches nothing. Sam runs every new tool against the synthetic TRB scope first, including the SWIFT exclusion at .20, and keeps the outputs as the expected results. Only when those outputs match the hand-worked answers does the tool become eligible for an engagement window, and the approval cites the synthetic run by date. An approval request without a dated synthetic run attached is refused, however urgent the window.

### 3.4 Review

A second engineer reads Sam's scripts for scope path mistakes. The reviewer's first job is to trace every path by which an address enters the script and confirm it passes through the TrackScope membership check before use. Common mistakes include a debug flag that skips the check, a second input file read without filtering, and an exclusion list loaded after the targets. The reviewer signs the review in FindingsDesk, so the record shows who checked which version and when. Unsigned scripts cannot run in a window.

### 3.5 Determinism

Seed randomness and pin interpreter versions so PulseMap demos are reproducible. A PulseMap demo that shows different coverage numbers on two runs cannot be trusted by anyone watching. With a fixed seed and a pinned Python version, the same synthetic input always produces the same tiles, and a changed number means changed data or code, not chance. Sam records the seed and version in each demo's notes so a reviewer can reproduce the exact screen later and compare it with the saved output.

### 3.6 Course labs

Labs in this book follow these rules and embed real outputs. Each lab in this book runs offline on the Python 3 standard library, uses documentation-range addresses and synthetic files, and prints output that was captured from a real run. If your output differs from the printed one, the difference is information: a changed input, a different interpreter or a bug. Treat it the way Sam treats a PulseMap regression, by finding the cause before trusting either result. None of the labs needs network access, so they can be run on a laptop with networking switched off.

### 3.7 Applied note

Dry-run output is pasted into the engagement channel before any write mode runs. Peers have two minutes to object. Sam once caught a path traversal into an evidence archive because a teammate read the dry-run carefully. Social review beats solitary cleverness for operational scripts. Two minutes is short enough not to delay a window and long enough for a careful reader. The pasted output lists every target address, the method card and the write paths the script will touch, so a reader can compare each line with the signed /26 and the SWIFT exclusion. Any reader's objection pauses the run until it is resolved and noted in the window log.

### 3.8 Test data policy

Synthetic customers in fixtures use obviously fake national IDs. Sam rejects fixtures that reuse real-looking personal numbers even when unused in production. Habit transfer matters. A fixture that resembles a real identity number can be copied into a test against production by someone in a hurry. Obviously fake values cannot be mistaken for customer data, and the habit carries into every later engagement. A reviewer who sees a plausible identity number in a fixture asks where it came from; a value like FAKE-000-001 ends the question immediately and cannot be confused with a customer during an incident.

### 3.9 Secret scanning in CI

Platform repos fail CI if high-entropy strings look like keys. Sam whitelists only test fixtures clearly marked FAKE. A real-looking key in a test file still trains people to ignore the warning, so marking is mandatory. Each whitelisted fixture is listed with its owner and the reason it is safe, and the list is reviewed whenever CI rules change. Whitelisting by marker rather than by file path means a real key pasted into a fixtures folder is still caught. When CI blocks a commit, the developer rotates the string even if it was only ever local.

### 3.10 3.11 Scene

Sam's script review board hangs three rejected snippets: a requests call with verify=False, a subprocess with shell=True on a hostname, and a retry loop without jitter. New interns initial the board after reading it. The board is silly and effective. When Sam almost pastes verify=False "just in staging", he sees his own initials and stops. Each snippet sits beside the safe version: verify left on with TRB's internal CA, a subprocess called with an argument list, and a retry loop with a cap and backoff.

### 3.11 3.20 Extra

Rejected snippet board gets a fourth example whenever CI catches a new anti-pattern. Sam dates each snippet. The board is a living museum of almost-mistakes. Each new snippet carries a one-line note on what CI caught and why it was dangerous, such as an uncapped retry against a slow host. Interns are asked to explain one snippet in their own words during their first week. The note names the rule, not the person who wrote the code. Sam's team reviews the board yearly and retires snippets whose CI rule has become routine.

### Worked example (synthetic TRB)

Sam's lab_scope.py uses only the ipaddress stdlib and documentation ranges; it never opens a socket.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX007 — Socket rule.** Why must lab_scope open no sockets? *Rubric:* 3 = offline/synthetic only; no accidental scan; 2 = partial; 1 = sockets fine; 0 = none.
- **EX008 — Two unsafe patterns.** Name two scripting patterns forbidden on the platform team. *Rubric:* 3 = two of secrets, TLS off, unsanitised shell, uncapped retries; 2 = one; 1 = vague; 0 = none.
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

"Shared admin account on loan system" beats "lazy admins". Boards fund fixes; insults create enemies. A finding that names a weakness, its location and its consequence gives the owner something to fix. A finding that names a group of people gives them something to defend. Sam writes the shared admin account finding with the system, the account, what the logs can and cannot attribute, and a recommended change, and leaves character judgements out entirely, because the same report will be read by the people who must do the work.

### 4.2 Fact vs claim

Fact: web tier opened a TCP session to ledger-db. Claim: "attackers can move money" needs more evidence or is labelled speculative. The connection itself is observed and logged; the claim about moving money depends on what ledger-db would accept from that session, which the test did not explore. Sam writes the fact in the finding and either labels the larger claim as speculative or lists the evidence that would be needed to support it. Readers can then weigh each sentence by its evidence rather than by its tone.

### 4.3 Citations

NIST SP 800-115, PTES, ATT&CK, OWASP WSTG, TIBER-EU and CBEST are cited with correct titles. Never invent DOIs. Each citation is checked against the publisher's page before the report goes out, and the edition or version matters: SP 800-115 is cited as NIST's technical guide to testing and assessment, not as a regulation. If Sam cannot find a source's official identifier, he cites the title and URL and says nothing more. An invented DOI would undermine every true sentence near it.

### 4.4 Audience layers

Executives need decisions; engineers need reproduction; both need honesty about uncertainty. For the shared admin account finding, the CISO needs the decision (fund named accounts for the loan system), the engineer needs the system name, the account and the log gap, and both need the same statement of what was not tested. Sam writes the executive summary and the technical appendix from the same finding record so they cannot drift apart. Uncertainty, such as untested hosts, goes in both parts in the same words.

### 4.5 Structure

Summary, scope/methods, findings, positives, limitations, appendices. The order is deliberate. A reader who stops after the summary still knows the decision asked; scope and methods tell everyone what was and was not tested before any finding is read; positives record what held up, such as SWIFT remaining unreachable; limitations stop the report being read as a guarantee. Appendices carry the hashes, ticket IDs and method cards that let an engineer reproduce each step. Sam uses this structure for every TRB report.

### 4.6 Revision

Peer review catches jargon and overclaim before the CISO sees the draft. Sam's reviewer reads for two things: words a non-specialist would not understand, and sentences that claim more than the evidence shows, such as 'attackers can move money' in place of the observed connection to ledger-db. Each comment is answered in the draft history, so the final report shows what changed and why before the CISO receives it. Unresolved comments block release; resolved ones stay visible. The CISO receives only the reviewed version, so overstated drafts such as 'attackers can move money' never reach the CISO.

### 4.7 Applied note

Citation drills require opening the live NIST or PTES page, not a blog summary. Sam failed an early draft for citing a second-hand SP 800-115 paraphrase that invented a clause. Primary sources only — the same rule as never inventing DOIs. The NIST page also shows the document's status and date. Sam now records, beside each citation in his draft, the date he opened the primary page and the section he relied on. Reviewers can then check a claim against the same page instead of trusting his memory of it.

### 4.8 Audience pass

Before sending, Sam reads the executive summary aloud to someone outside security. If they cannot restate the decision asked, he rewrites. Jargon surviving that pass is a defect. The listener's restatement is noted in the draft history for later comparison. For the shared admin account report, a listener from finance restated the ask as 'pay for named accounts on the loan system', which matched. An earlier draft had produced 'something about passwords', which sent it back for rewriting. The finance listener was chosen deliberately.

### 4.9 Passive voice audit

Findings that hide actors in passive voice are rewritten. "Passwords were reused" becomes "The loan admin account used the same password as VPN" when known. Naming the system makes the finding actionable and testable. When the actor is not known, the sentence says so plainly, for example 'logs do not show which administrator changed the setting'. That keeps the finding honest without inventing a culprit, and it points straight at the logging gap as a second issue to fix. Fixing the 'developers ignored security' draft needed only one rewritten sentence naming the system and the missing log.

### 4.10 4.11 Scene

A draft finding once said "developers ignored security". Legal asked for rewrite before the board pack. Sam produced: "The loan service accepted a shared privileged password; logs cannot attribute changes to a person." Same facts, fundable tone. He keeps both versions in teaching notes to show the difference. Both versions describe the same log gap. The rewrite removes the accusation but keeps every fact: a shared privileged password and no attribution in the logs. That is why it survived legal review and still told the loan service owners exactly what to change.

### 4.11 4.20 Extra

Tone trophies are silly stickers on printed findings that developers praised as clear. Sam prefers stickers to metrics nobody reads. Each sticker records which finding was praised and why, so the next report can copy the clarity rather than just the sticker. Clarity that developers notice is clarity that gets fixes. Sam keeps the praised findings in a folder as examples for interns, alongside the rewritten 'developers ignored security' draft, so both good and bad models are visible. Finding counts stay secondary in Sam's reports, because a clear finding that gets fixed matters more than a long list.

### Worked example (synthetic TRB)

Sam rewrites "the web team is incompetent" to "web tier reaches ledger-db on an unapproved flow; control: enforce approved matrix".

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX010 — Rewrite.** Turn "stupid password reuse" into professional finding language. *Rubric:* 3 = system condition + impact + no insult; 2 = partial; 1 = keeps insult; 0 = none.
- **EX011 — Speculative claim.** How should Sam label "attackers already stole funds"? *Rubric:* 3 = speculative/unconfirmed; separate from facts; 2 = partial; 1 = as fact; 0 = none.
- **EX012 — Citation rule.** What must Sam never invent when citing? *Rubric:* 3 = DOIs / fake references; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Clear, cited, audience-aware writing is part of authorized testing craft.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) place authorized testing among security practices; (2) name CIA with TRB examples; (3) refuse unauthorized work.

### 5.1 Neighbouring practices

Architecture, monitoring, IR and authorized testing reinforce each other. Testing without logging is theatre; logging without testing misses unknown unknowns. At TRB, a test that reaches ledger-db from the web tier only helps if the monitoring team can show whether they saw it, and incident responders know what they would do next. Sam therefore sends each finding to architecture for the design fix, to monitoring for a detection question and to IR for a playbook check. A finding that improves all three is worth far more than one that only adds a line to a report.

### 5.2 CIA at TRB

Confidentiality of customer data; integrity of ledgers and payments; availability of online banking. Findings are judged by which they threaten. The connection from the web tier to ledger-db threatens integrity first, because the ledger records balances and payments; a leaked statement template threatens confidentiality; a scan that slows online banking threatens availability. Naming the property makes severity arguments concrete. Sam adds the threatened property as a field in every FindingsDesk ticket so owners can see at a glance which promise to customers is at risk, and boards can count findings by property rather than by tool.

### 5.3 Permission

Written ROE from owners. Bug bounties cover only their published scope. Friends' banks are never practice targets. At TRB, the ROE is signed by the owners of the systems in the /26 and names exclusions such as SWIFT. A bug bounty that covers the public website does not cover the internal API behind it, and a friend's offer to 'let you try' on another bank's system grants nothing, because the friend does not own that system. Sam keeps a copy of the signed ROE open during every window and stops if a target cannot be traced to it.

### 5.4 Dual-use

This curriculum teaches scoping, measurement and reporting — not exploit code for real products. The same knowledge that helps defenders can help attackers, so the course draws its line at artefacts: it teaches how to plan, measure and report authorized tests, and how techniques are named for detection, but it never provides working exploit code for real products. Sam's labs follow the same rule. A learner who finishes the course can scope a TRB engagement and rank its findings, but holds nothing that could be pointed at someone else's bank.

### 5.5 Framework map

SP 800-115 (planning), PTES (stages), WSTG (web), ATT&CK (techniques), TIBER-EU/CBEST (threat-led finance). Each framework answers a different question. SP 800-115 tells Sam how to plan and run an assessment; PTES describes the stages from pre-engagement to reporting; WSTG gives test cases for web applications such as online banking; ATT&CK names techniques so findings can be linked to detection; TIBER-EU and CBEST describe intelligence-led red teaming for financial institutions under regulatory oversight. Using one framework where another belongs, such as treating CBEST as a web checklist, produces confused plans.

### 5.6 Ethics

Customer harm and payment integrity outrank curiosity and resume screenshots. In practice the ordering decides real choices. If a test might corrupt a payment record, it stops, however interesting the result would be. If a screenshot would show customer data, it is not taken, even for a portfolio. Sam writes the expected customer impact of each method card before a window, and any card with possible payment-integrity impact needs the ledger owner's named approval. Curiosity is satisfied in the synthetic lab, where nothing real can be harmed.

### 5.7 Applied note

The refusal script is role-played with a staff member playing an impatient director. Sam must keep tone respectful while not yielding. Video reviews show whether he smiles nervously into agreement; those clips are deleted after coaching but the lesson stays. The director in the role-play asks Sam to 'just quickly check' a host outside the /26. Sam's script names the ROE clause, offers to raise a scope change with the owner and gives a realistic time for approval. Practising the exact words makes them available under real pressure.

### 5.8 Framework flashcards

Sam's deck has one card per framework: SP 800-115, PTES, WSTG, ATT&CK, TIBER-EU, CBEST — purpose and what it is not. Misusing CBEST as a web checklist is a common card-back answer. The card for TIBER-EU, for instance, says it frames threat-intelligence-led red teaming for financial entities and is not a vulnerability scanning standard. Writing the 'what it is not' side forces Sam to understand each framework's purpose rather than its name, and the deck is reviewed whenever a framework publishes a new version.

### 5.9 Home lab boundary

Sam's home lab uses RFC1918 and never TRB DNS. Mixing VPN into homework is a reported near-miss if it happens. Private RFC1918 ranges at home cannot collide with TRB's addressing if Sam never connects the bank VPN while experimenting. Using TRB DNS from home would leak internal names and could send lab traffic toward the bank. If a mix-up happens, he reports it as a near-miss so the boundary rule can be improved rather than quietly hoping no one noticed.

### 5.10 5.11 Scene

Sam declines a meetup invitation to demo "how we hacked our bank" even though the work was authorized. Screenshots travel. He offers instead a talk on ROE design with synthetic examples. The organisers accept. Dual-use restraint includes what you refuse to present. A screenshot of an authorized TRB finding still shows real hostnames, versions and weaknesses that may not yet be fixed. Once shown on a meetup screen, it cannot be withdrawn. The ROE talk shares the reusable lesson without the bank's details.

### 5.11 5.20 Extra

Meetup alternative talks use only documentation-range demos. Sam's slide deck is public; his TRB screenshots are not. Documentation ranges such as 198.51.100.0/24 make it impossible for a demo to point at a real host, and synthetic findings carry no information about TRB's systems. Before publishing, Sam checks every slide for internal names, ticket IDs and real addresses. His TRB screenshots stay inside FindingsDesk, where access is controlled and logged, and are deleted when the engagement's retention period ends. The public deck is reviewed by the ROE owner once before release.

### Worked example (synthetic TRB)

A classmate asks Sam to "try the bank's login from home". Sam refuses and points to the course boundary.

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

Nodes are principals and systems; edges are can-authenticate or can-reach. A path from Internet to ledger-db that bypasses jump hosts is a finding candidate. At TRB, the graph might show the internet reaching the web tier, the web tier reaching the core API, and the jump host reaching ledger-adjacent admin. An extra edge from the web tier directly to ledger-db creates a path that skips the jump host, and that path is the finding, whether or not any single host has a known vulnerability. Sam draws only edges supported by inventory or authorized scan evidence, so each path can be defended.

### 6.2 Flow relations

Approved flows are a relation R ⊆ Src × Dst. Observed flows should be subsets of R when the matrix is enforced. For TRB, R might include (web tier, core API) and (jump host, ledger admin) but not (web tier, ledger-db). If observed flows include a pair outside R, either the matrix is not enforced or R is incomplete. Sam's lab compares the two sets and lists the differences, and each difference becomes a question for the network owner rather than an automatic finding, because an approved but undocumented flow is a documentation fix.

### 6.3 Decision trees

Stop trees: if owner asks stop → halt; else if unexplained outage → halt; else continue under ROE. Writing the tree down before a window removes argument during it. If the loan system owner says stop, Sam halts at once without asking why. If an unexplained outage appears on any in-scope host, he halts and reports, even if the outage may be unrelated. Only when neither condition holds does testing continue, and continuing still requires the method to be allowed by the ROE. Each pass through the stop tree is logged with the time and outcome, so the window log shows why testing continued or halted.

### 6.4 Equivalence

Hosts in the same hardening class may share method cards — but only if the ROE groups them. If TRB's ROE groups ten web servers into one hardening class, Sam can apply the same method cards to all ten and report results by class. If the ROE lists them separately, perhaps because two host payment pages, he must treat each as distinct. Equivalence is a decision the owner makes in writing, not a shortcut the tester assumes because two hosts look alike from the outside.

### 6.5 Ordering

Severity ranking uses ordered scores; ties break by finding id for determinism (lab_rank). Without a fixed tie-break, two findings with the same score could swap places between runs, and a board pack would show a different top item each time it was regenerated. Breaking ties by finding ID makes lab_rank produce the same order from the same data, so a change in ranking always means a change in scores. Sam records the scoring scheme in the report so readers know what the order means.

### 6.6 Limits

Graphs omit social engineering unless the ROE includes it. A graph of network and authentication edges says nothing about a branch employee who could be persuaded to approve a payment by phone. If the ROE excludes social engineering, Sam states that the graph covers technical paths only, so the board does not read 'no path found' as 'no way in'. The limitation sits on the same slide as the graph, in plain words. Social engineering, if later authorized, would add new edges to the same graph.

### 6.7 Applied note

Reachability graphs annotate edges with "authenticated" or "network-only". A network-only edge to ledger-adjacent hosts raises severity even without credentials, because credential theft elsewhere completes the path. Sam's first graphs missed that annotation and under-ranked a finding. After the correction, every edge to a payments-adjacent node carries its annotation, and lab_rank weights network-only edges to the ledger tier more heavily. The earlier under-ranked finding was re-scored and re-sent with a note explaining the change, so readers of the first version were not left with the lower rank.

### 6.8 Cut sets

For payments-adjacent nodes, Sam looks for cut sets of edges whose removal would isolate them from the Internet. Those edges become monitoring and control priorities even when not "vulnerable" in a scanner sense. For ledger-db, the cut set turned out to be two edges: the direct web-tier connection and admin access that bypassed the jump host. Removing those two isolates the ledger from internet-facing paths. Monitoring them costs far less than watching every host. Those two edges are also the ones F3 and the jump-host rule address.

### 6.9 Edge evidence

Each critical graph edge cites the inventory or scan source under ROE. Edges without sources are removed. A source might be an asset register entry, a firewall rule export or an authorized scan result with its date. An edge drawn from memory or assumption cannot be checked, so it cannot support a finding, and leaving it in would make the whole graph look more certain than it is. When a source is missing, Sam asks the owner and adds the edge back only with evidence.

### 6.10 6.11 Scene

Tracing a path from a compromised branch PC model to ledger-db, Sam finds four edges. Removing the web→ledger edge (F3) and requiring jump for admin cuts the remaining dangerous paths. The graph did not need fifty nodes — it needed the cut set. He deletes the decorative edges from the slide. Showing four edges and the cut set made the fix discussion take minutes instead of an hour, because the owners could see exactly which two changes mattered. The slide now shows only the four path edges.

### 6.11 6.20 Extra

Cut-set slides use at most six edges. Sam deletes the rest in front of the audience to teach focus. A slide with fifty edges hides the two that matter; a slide with six makes the cut set visible to an executive in seconds. Deleting edges live also shows that the removed ones were context, not evidence. Sam keeps the full graph in the appendix, with sources for every edge, so engineers can still check his reasoning and nothing is hidden from review.

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

Port 443 often means HTTPS but may not. Inventory names and certificates matter. A service on 443 at TRB might be the online banking front end, an admin console or an internal API exposed by mistake. Sam identifies it from the asset register, the certificate's subject names and the owner's description before choosing any method card. Treating every 443 as 'the website' leads to wrong scope decisions, such as testing an admin console under rules written for the public site. The owner's answer is recorded in the scope file beside the port.

### 7.2 TLS

Protects confidentiality and integrity in transit; does not fix broken authorization in the app. An encrypted session to online banking still lets a logged-in customer request another customer's statement if the application fails to check ownership. Sam therefore reports TLS weaknesses and authorization weaknesses as separate findings with separate owners: the platform team for certificates and protocol settings, the application team for access checks. Good TLS is necessary but tells nothing about what the server does once the request arrives.

### 7.3 Dangerous experiments

Sending malformed packets to the ledger VLAN to "see what happens" is out of bounds. The ledger hosts are fragile, change-controlled and outside ordinary scope, so an unplanned reaction such as a crash or a stuck transaction could affect real payments. Even where the ROE allows some network testing, malformed-packet experiments need a named method card, a maintenance window and the owner's explicit approval. Without those, the right action is to record the question and raise it with the ledger owner.

### 7.4 Documentation ranges

Labs use 198.51.100.0/24 and 203.0.113.0/24 so examples cannot hit the real Internet. These ranges, reserved for documentation, are not routed on the public internet, so a typo or copied example sends nothing anywhere real. TRB's synthetic scope, 198.51.100.0/26 with SWIFT at .20, uses them for the same reason. Using real-looking addresses in course material risks a learner pasting them into a tool on a live network. The 203.0.113.0/24 range plays the attacker's or partner's side in examples. If a lab printout ever shows an address outside these ranges, treat it as a defect in the material and report it.

### 7.5 Capture ethics

Packet captures need ROE clauses; they often contain customer data. A capture on TRB's web tier can contain session data, account numbers or statement contents. The ROE must say who may capture, on which segments, for how long the files are kept and how they are deleted. Without that clause, Sam does not capture at all, and he prefers configurations and logs because they answer most questions with far less customer data. Any capture taken is hashed, stored in FindingsDesk and deleted on schedule.

### 7.6 ATT&CK

T1190 Exploit Public-Facing Application describes abuse of internet-facing services — named for detection design, not as a how-to. Linking a finding to T1190 tells the monitoring team which detections to check, such as unusual errors or requests on the online banking front end, without describing how the weakness was triggered. Sam adds the technique ID in FindingsDesk so PulseMap can show coverage by technique, and the report never includes steps. Detection owners can then test their rules against synthetic requests in staging.

### 7.7 Applied note

Capture ROE clauses specify retention hours and who may run wireshark. Sam's default ask is "configs and logs first; packets only if those fail". Most TRB web findings never need packets; when they do, the clause is already written. Writing the clause in advance means an urgent capture request during a window does not lead to an improvised decision about customer data. The clause also names who deletes the files when the retention hours expire. The named person confirms deletion in the capture ticket when the retention hours expire, so nobody assumes the files are gone.

### 7.8 Banner humility

Banners feed inventory, not severity theatre. Sam files version exposure as low unless paired with a reachable vulnerable path under ROE — which this course still will not exploit in the wild. A banner showing an old version may be patched by the vendor's backport, so the version alone does not prove a weakness. Recording it as inventory lets owners plan upgrades without inflating a report with alarming but unverified findings. If a reachable weakness is later confirmed under ROE, severity is re-scored with that evidence.

### 7.9 Doc-range lint

Examples in docs are linted to ensure IPs are documentation ranges. Sam's lint failed a blog draft using a real TRB address; good catch. The real address would have revealed part of TRB's network layout and could have invited readers to probe it. The lint runs on every documentation change and blocks publication until the address is replaced with a documentation-range example, such as one from 198.51.100.0/24. The blog draft was corrected and the original address reported to the network owner.

### 7.10 7.11 Scene

A learner asks to try a TCP FIN scan on staging "for the coursework". Sam shows the ROE forbidden-methods list and the course boundary page. They run an offline PCAP quiz instead. Curiosity is redirected, not shamed — and not indulged on bank networks. The quiz uses synthetic captures, so the learner still sees how packets look without any traffic touching a TRB network. Sam also logs the request as a teaching note, without the learner's name, because it shows where the course boundary needs to be explained earlier.

### 7.11 7.20 Extra

PCAP quiz answers never include payload bytes from real customers. Synthetic PCAPs only. Synthetic captures are generated with documentation-range addresses and invented payloads, so no customer data can leak through teaching material. Answers describe headers, timing and flow patterns, which is what learners need for detection reasoning. Sam regenerates the quiz files when the course changes rather than editing captures by hand, so their provenance stays clear. Each regenerated file is hashed and the hash published with the quiz. Because every quiz file is generated, learners never handle captures containing real TRB customer traffic.

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

Scope loader, finder schema, report exporter — each with tests and a README. Splitting the platform this way lets each part fail and be tested on its own. The scope loader's tests feed it the synthetic /26 with SWIFT at .20 and check that the exclusion survives every input format. The findings schema's tests reject records without required fields. The exporter's tests compare generated reports with saved expected files. Each README states what the module does, what it refuses to do and who reviews changes to it.

### 8.2 Validate on write

FindingsDesk rejects tickets missing owner or evidence hash. Rejecting incomplete tickets at the moment of writing is cheaper than chasing them later. A finding without an owner has nobody to fix it, and a finding without an evidence hash cannot be checked against the file it claims to describe. Sam's validation returns a message naming the missing field, so an analyst can correct the ticket immediately instead of guessing why it failed. FindingsDesk applies the same required-field rule to bulk imports and API calls, so neither route can create a finding without an owner.

### 8.3 API versioning

PulseMap v2 adds fields without breaking v1 consumers. Existing consumers of PulseMap, such as the monthly board export, read v1 fields and must keep working when new fields such as technique IDs per method card appear. Adding fields is safe; renaming or removing them is a breaking change that needs a new version and a migration period. Sam's contract tests run the v1 consumer against the v2 server on every build, so an accidental break fails CI rather than the next board pack.

### 8.4 Partial updates

PATCH must not clear required fields accidentally. A client that sends only a changed severity must not wipe the owner or evidence hash by omission. FindingsDesk treats PATCH as 'change these fields only' and re-runs validation on the merged record, so a partial update cannot produce a ticket that would have been rejected on creation. Sam's tests send PATCH requests with one field at a time and confirm every other required field survives unchanged. The same rule protects the evidence hash during bulk edits.

### 8.5 Bulk import

CSV import of findings dry-runs first and caps row counts. A dry run shows what the import would create, update or reject, including any host outside the TRB scope, before anything is written. The row cap limits the damage a wrong file can do, and the next applied note shows why both limits exist. Only after an analyst reviews the dry-run summary does the real import run, and the summary is attached to the import record. The dry-run summary lists each rejected row with its reason, such as a host outside the TRB scope, so the analyst can fix the file.

### 8.6 Concurrency

Optimistic locking prevents two analysts overwriting the same ticket silently. Each ticket carries a version number. When an analyst saves, FindingsDesk checks that the version has not changed since the ticket was opened; if a colleague saved first, the second save is refused and the analyst sees both versions. Without this, one analyst's severity change could silently erase another's new evidence, and nobody would know which view of the finding was current. The refused analyst merges the two versions by hand, and the merge is logged.

### 8.7 Applied note

Bulk import caps at 500 rows and requires a second approver above 100. Sam saw an analyst almost import a scanner dump that included out-of-scope hosts as "informational". Caps and approvers are boring on purpose. An 'informational' out-of-scope host is still evidence that someone tested outside the ROE, so it needs review, not quiet storage. The second approver checks the dry-run summary against the signed scope before larger imports proceed. The approver is never the person who ran the scan, so the check is independent.

### 8.8 Migration drills

Schema migrations run on a copy with checksums before and after. Sam records row counts. A migration that changes counts silently fails the drill. Checksums and row counts on the copy show whether a migration preserved every finding and evidence reference. If counts differ, the migration is fixed and rerun on a fresh copy; production is never used as the test. Sam keeps the before and after figures with the migration script so a reviewer can confirm the drill passed.

### 8.9 Idempotent writes

Ticket updates are idempotent by finding id. Double delivery from flaky networks cannot create duplicate F1s. Because each update is keyed by finding ID, applying the same request twice leaves the ticket in the same state as applying it once. A retried create for F1 updates F1 rather than inserting a second record. This matters at TRB, where VPN links to the assessment zone drop often, and duplicate findings would inflate counts in board reports. Board counts therefore stay true even on bad network days.

### 8.10 8.11 Scene

FindingsDesk's bulk import dry-run once revealed 40 hosts outside the ROE embedded in a scanner CSV. The import blocked. Sam thanks the dry-run in the retrospective more than any new feature shipped that month. Forty out-of-scope hosts in an assessment database would have looked like authorized test results and could have prompted follow-up work against systems nobody had approved. The dry-run turned a silent data problem into a visible decision, and the scanner configuration that produced the CSV was corrected before the next window.

### 8.11 8.12 Extension

Idempotent ticket updates saved TRB when a flaky VPN resubmitted the same finding create call twelve times. FindingsDesk showed one F1, not twelve. Sam adds that story to onboarding so engineers stop fearing "exactly-once" as academic. Twelve duplicate F1 tickets would have shown twelve open critical findings to the board and paged the owner twelve times. Idempotency made the network failure harmless, which is exactly what engineers need to see before they trust the design. New engineers now test retries in their first week.

### 8.12 8.16 Pad

FindingsDesk's approval threshold at 100 rows exists because a 2,000-row dump once queued overnight and page-stormed owners. Sam documents the incident id beside the constant in code. Linking the constant to the incident record tells future engineers why the threshold exists before they decide to raise it. Without the comment, 100 looks arbitrary and invites removal. With it, anyone changing the value can read what happened when large imports ran unreviewed and paged owners all night. The comment names ENG-441 and the date of the change.

### 8.13 8.20 Extra

Overnight page-storm incident id is ENG-441 in the course archive. Sam links it from the constant's comment. The archive entry describes the overnight queue, how many owners were paged and the change that introduced the approval threshold. A reviewer who finds the constant can follow the link and judge the history directly. The same practice applies to the 500-row cap: every safety limit in FindingsDesk points to the reason it was set, so limits are changed deliberately rather than by someone tidying the code.

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

A finding record at TRB needs only enough to reproduce and verify the weakness: the affected asset identifier, the request or configuration that demonstrated it, a timestamp, the tester, the engagement id and a pointer to the evidence file. When Sam proved that a statement-download endpoint returned another customer's PDF, the record kept the two synthetic account ids involved and a hash of the response, not the statement itself. A retest next quarter repeats the same request and compares the outcome. Every extra column copied from a customer table becomes data the testing team must now protect, retain and eventually delete.

### 9.2 Access control

Evidence databases use role-based access; Sam's intern role is read/write on engagement schemas only.

Roles are granted per engagement, not per person, so the permission disappears when the engagement closes rather than when someone remembers to revoke it. FindingsDesk has three: tester (write findings and evidence for one engagement), reviewer (read across the engagements they sign off) and custodian (run retention and restore jobs, never edit findings). Separating the custodian from the tester means the person who deletes evidence on schedule is not the person whose work it documents. When a tester moves to a new engagement, their old role expires and the reviewer keeps read access until the report is accepted.

### 9.3 Retention

Agreement-driven deletion jobs; "keep forever" is not a policy.

The statement of work fixes a retention period for raw evidence, commonly ninety days after the final report, and a longer one for the report and remediation status. FindingsDesk stores that date on the engagement row the day the agreement is signed, and a nightly job deletes evidence blobs whose date has passed, writing a deletion receipt with counts and hashes. Retention also protects the tester: evidence kept past its agreed date is customer data held without a reason, and an auditor will ask why. If a client requests a legal hold, the hold is a dated field with an owner, not an informal promise.

### 9.4 Backups

Encrypted, access-logged, tested restores — backups are in scope for abuse review.

A backup is a second copy of every screenshot, request log and credential-shaped string the team ever captured, so it attracts the same threats as the live database and is often watched less carefully. TRB's evidence backups are encrypted with a key held by the custodian role, stored in a separate account, and every read is logged. Retention applies to backups too: a deletion job that cleans the live store but leaves ninety-day-old snapshots intact has not deleted anything. Sam's quarterly review compares the oldest snapshot date with the shortest retention period on any active engagement.

### 9.5 Query hygiene

No SELECT * into laptops; export minimised CSVs.

Analysts usually want a count, a trend or a single example, and the query should return exactly that. Pulling whole tables to a laptop moves evidence outside the controls that protect it: no access log, no retention job and a disk that may travel. FindingsDesk therefore exposes saved queries such as open findings by severity, or days to fix per business unit, that return aggregates and redacted columns. When someone needs a raw row, they open it inside the evidence viewer, where the read is logged. Sam rewrote a popular dashboard query that selected every column and cut the export from forty fields to six.

### 9.6 Integrity

Foreign keys from findings to evidence blobs.

A finding that points to a missing or altered file cannot be defended when the client disputes it. Each evidence blob in FindingsDesk is stored with a SHA-256 hash computed at upload, and the finding row references the blob by id with a foreign-key constraint, so the database refuses to delete evidence that a live finding still cites. When a report goes out, the export lists each finding with the hashes of its evidence. If TRB later asks whether a screenshot was edited, Sam recomputes the hash and compares. A mismatch is itself an incident to investigate, not a reason to re-upload quietly.

### 9.7 Access review against HR records

Evidence DB roles are reviewed quarterly against HR lists. Sam's query checks for active vault roles without active employees. The first run found two contractors; access was removed the same afternoon.

The join is simple: roles with no matching active record in the HR export are orphaned. The interesting cases are near-misses. A tester on parental leave is inactive in HR but should keep a dormant account, and a contractor renewed under a new purchase order may appear under a different id. Sam's query therefore produces a review list rather than revoking access automatically, and the security lead signs each decision. The second quarter's run found zero orphans, which is the result the control exists to produce.

### 9.8 Export watermarks

CSV exports embed engagement id and exporter name in a header comment. Leaked files can be traced. Sam verifies the watermark exists in a quarterly spot check.

A watermark does not stop a leak; it shortens the investigation that follows one. When a file turns up on a shared drive, the header names the engagement and the person who exported it, so the custodian can check whether that export was authorised and which retention date applies. Header comments are easy to strip, so the export log in FindingsDesk records the same fields together with a hash of the file. Matching a stray file's hash against that log identifies its origin even when someone has deleted the comment line.

### 9.9 Backup restore game

Quarterly, Sam restores an evidence backup to an isolated host and opens one file. Untested backups are assumed broken.

The exercise has a pass condition written in advance: restore within two hours, open a randomly chosen evidence file, recompute its hash and match it to the finding record. The isolated host has no network route to production and is wiped afterwards, because a restored backup is full of sensitive evidence. Timing matters as much as success. If TRB disputes a finding during a report review, the team must produce the original evidence that week, not after a day of searching for the decryption key. Each game ends with a short note recording duration, problems and fixes.

### 9.10 Refusing a bulk export

An analyst requests "all evidence for the year" for a thesis. Sam refuses bulk export and offers a statistics-only extract with counts by severity. The thesis still proceeds. Minimisation applies to friendly requests too.

The refusal works because Sam asked what question the thesis was trying to answer. The analyst wanted to show how long high-severity web findings stayed open, which needs dates and severities, not screenshots or account ids. A query grouped by quarter and severity answered that, and the result contained no customer data at all. Purpose comes first: a request framed as all evidence usually hides a narrower need, and naming that need turns a privacy conflict into a reporting task.

### 9.11 Restore without a manifest

During restore game day the backup opened, but the hash manifest was missing. Sam failed the game and restored the manifest job before the next engagement. Backups without manifests are rumours.

The file opened, so a less careful reviewer would have passed the game. Without the manifest, though, nobody could prove the restored file matched what was captured during testing, and that proof is what the evidence is for. The cause was mundane: a storage migration had dropped the scheduled job that writes manifests beside each snapshot. Sam added a check that fails the backup itself when no manifest is present, so the gap now surfaces the night it occurs instead of on the next quarterly game.

### 9.12 A contact address in every export

Watermark headers include a contact mailto for lost-and-found of stray exports. Someone used it once; Sam bought them coffee.

The address gives an honest finder a way to report a stray export instead of guessing who owns it. It goes to a shared custodian mailbox, not to an individual, so it still works after staff change. Reports are handled like a small incident. The custodian confirms the file's origin from the export log, asks the finder to delete their copy or hand it back, and records whether its retention date had already passed. Thanking the reporter publicly makes it more likely that the next stray file is reported too.

### 9.13 A returned drive

Lost-and-found mailto once returned a USB drive labelled with an engagement id. Process works.

The drive also showed where the process had failed earlier: someone had copied evidence to removable media despite the export rules. The custodian did not simply wipe the drive. They checked its contents against the export log, found an unlogged copy of screenshots from an engagement that had closed months before, and traced it to a tester who had wanted to work offline on a train. The response was a short conversation, deletion with a receipt, and a new option in FindingsDesk for encrypted offline workspaces that expire on the retention date.

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

The rules of engagement turn a general permission into instructions a tester can check before each action. At TRB they list the networks and hostnames in scope, name the SWIFT gateway and the production ledger as excluded, permit authenticated web testing but forbid denial-of-service and social engineering, and fix testing to weeknights between 20:00 and 02:00. They also name who answers the phone if something breaks, how captured data is stored, and who receives the report. A rule that is not written down does not exist when it is needed at 23:40.

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

Running the classifier before any traffic turns scope from something a tester remembers into something a tester can show. The list of proposed targets, the version of the scope file and the output are saved together in the engagement folder. If a later dispute asks why one host was tested, the answer is the saved output, not a recollection. The check is deliberately strict: an address outside every listed range is refused, even when it looks like part of the same service, until the scope file is amended and signed.

### 10.3 Pressure

"Just add the SWIFT box" is refused until written exclusion changes — which they will not for ordinary tests.

Pressure rarely arrives as an order to break rules. It comes as a reasonable-sounding shortcut from someone senior, late in a window, when the extra host would make the report look more complete. Sam's answer follows a script: thank them, explain that the gateway is excluded in the signed rules, and offer to raise a scope change with its owner for a future window. The exclusion exists because the gateway's owner has not accepted the operational risk, and no one on a test call can accept it for them. Refusing politely and in writing protects both the tester and the person who asked.

### 10.4 Responsible disclosure

Vendor bugs found in third-party software follow vendor paths only with CISO approval.

A flaw in a commercial product that TRB uses belongs partly to TRB and partly to every other customer of that product. Sam records it in FindingsDesk as a TRB finding with a compensating control, then passes the technical detail to the CISO, who decides whether to contact the vendor and under which disclosure timeline. Contacting the vendor directly, or posting about it, could expose TRB as an unpatched customer before a fix exists. The report to the vendor carries enough detail to reproduce the bug safely and nothing about TRB's wider environment.

### 10.5 Conflicts

Sam does not test systems owned by family businesses on TRB time or tools.

A conflict of interest does not need bad intent to damage an engagement. Someone who tests a relative's company with the bank's scanner uses TRB resources outside TRB's authority, and any finding they produce is open to the charge that it was shaded for a personal reason. The same reasoning applies inside the bank: a tester whose friend owns the application under review should declare it before scoping. Declaring a conflict early costs one email and possibly a reassignment. Declaring it after the report has gone out can cost the credibility of every finding in it.

### 10.6 Dual-use teaching

Exploit details for real payment products are out of curriculum scope.

The skills in this book can be misused, so the book draws a line at what it teaches in detail. It explains weakness classes, how authorized testers confirm them safely and how to report them, using synthetic systems. It does not give working exploit chains for real card terminals, payment switches or banking platforms, because such material helps an attacker more than a learner. A student who wants to go further does so in a sanctioned lab under supervision. The test of any teaching example is whether a defender learns more from it than an attacker gains.

### 10.7 No exploit code in the findings system

Dual-use policy examples include refusing to paste exploit PoCs into FindingsDesk even when a vendor asks "for repro". Reproduction at TRB uses configuration evidence and authorized accounts, not weaponised snippets.

FindingsDesk is read by developers, auditors and managers, and its exports reach vendors. A working proof-of-concept stored there would spread to every one of those readers. Sam's findings show the conditions instead: the misconfigured setting, the request an authorized test account sent and the response that proved the weakness. A developer can confirm the issue in a test environment from that description. When a vendor insists on more, the CISO decides what to share and over which secure channel.

### 10.8 Gift and conflict log

Sam logs any vendor gifts or outside bank accounts that could bias scope decisions. Transparency is cheaper than recusal fights mid-engagement.

The log is a short dated table: what was received or held, from whom, and which engagements it might touch. Small things count because they show a pattern. A conference ticket from a scanner vendor matters if Sam later recommends that vendor's product in a report. The security lead reviews the log before assigning testers, which settles recusals at planning time, when swapping a tester is easy. An entry is not an accusation; an unlogged gift found later is treated as one.

### 10.9 Tabletop on the rules of engagement

Annual tabletop walks a missing emergency-contact scenario. Sam's team practices postponing rather than improvising.

A tabletop costs an hour and no packets. The facilitator reads out a situation: a test is about to start and the named emergency contact does not answer. Each participant says what they would do and which rule tells them so. The useful outcome is the gaps it exposes. One year the team found that the rules named a contact who had changed roles three months earlier. Updating that name before the next window was the most valuable result of the session.

### 10.10 Postponing when the contact is unreachable

Tabletop: emergency contact unreachable. Sam's team postpones the window in writing within five minutes. Improvised verbal approval from a random manager is scored as a fail condition in the tabletop. Postponement is success.

The instinct to keep going comes from the cost of rescheduling, but continuing without a reachable contact means that if a service degrades, nobody with authority can tell the testers to stop. A manager who happens to be online may mean well, yet they are not named in the rules and cannot accept the risk. The written postponement records the time, the attempts to reach the contact and the next proposed window, so the delay is documented rather than blamed.

### 10.11 Recusing from a relative's vendor

Sam's conflict log once listed a sibling working at a fintech vendor. He recused from a test involving that vendor's library. Recusal is quieter than scandal.

The library was a small part of the engagement, which made it tempting to stay on and just skip that component. The security lead chose clean separation instead. Another tester took every finding that touched the library, and Sam's name was left off those records. Had the test found a serious flaw, the vendor could not argue that a relative had either exaggerated or softened it. The log entry, written months earlier, made the decision a two-minute task rather than an argument.

### 10.12 Postponement templates

Postponement templates include SOC and CISO aliases pre-filled. Sam sends postponements in under three minutes during drills.

A template removes decisions from a stressful moment. It already lists the engagement id, the recipients who must know (the SOC, so it does not hunt for testers who are no longer testing, and the CISO's office), and fields for the reason, the attempts made and a proposed new window. The tester fills in facts, not wording. Pre-filled aliases matter because individual names go out of date, while role addresses are maintained by the teams that own them.

### 10.13 Timing the postponement drill

Three-minute postponement drill is timed with a visible clock. Over three minutes fails the drill.

The limit is not arbitrary. TRB's SOC escalates unexplained scanning after five minutes, so a postponement sent within three reaches the analysts before they start an incident for activity that has already stopped. A visible clock also shows where time goes. In early drills most of it went on finding the template, which led to a pinned link in the engagement channel. Drills are scored on whether the message arrived, whether it went to the right roles and whether it was accurate, not on speed alone.

### Worked example (synthetic TRB)

lab_scope marks 198.51.100.20 EXCLUDED and 198.51.100.70 OUT OF SCOPE; Sam removes both from the plan.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX028 — Excluded line.** What does the lab print for 198.51.100.20? *Rubric:* 3 = EXCLUDED; 2 = out of scope; 1 = in scope; 0 = none.
- **EX029 — Pressure answer.** How does Sam answer "add SWIFT just this once"? *Rubric:* 3 = refuse until written ROE change; SWIFT stays excluded; 2 = refuse; 1 = agree; 0 = none.
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

On a Windows server the usual surfaces are missing cumulative updates, members of the local Administrators group and remote services such as RDP, SMB and WinRM. On Linux they are outdated packages, accounts with sudo rights and listening daemons such as SSH or an exposed database port. A finding that just says the server is insecure gives the owner nothing to act on. A finding that says a staging Linux host accepts SSH password logins from the user VLAN, contrary to the hardening baseline, names the operating system, the control that failed and what fixing it looks like.

### 11.2 Jump hosts

Admin paths go through jump; email-VLAN RDP to servers is a finding.

A jump host concentrates administrative access in one place that can be hardened, monitored and protected with multi-factor authentication. If administrators can also reach servers directly from the network where they read email, a phishing compromise of their workstation becomes a route to the servers that bypasses all of those controls. Sam tests the path from a synthetic user-VLAN host with an authorized account. If an RDP session to a staging server opens without passing through the jump host, the finding records the source network, the destination and the firewall rule that should have blocked it.

### 11.3 Images

Golden images with old agents reintroduce risk when rebuilt.

A golden image is the template from which new hosts are built, so whatever it contains is copied onto every host built from it. If the image carries an endpoint agent two versions behind, or a local account created for a debugging session, each rebuild brings that weakness back, often after the original host had been fixed by hand. Rebuilding is supposed to remove drift, but a stale image adds it instead. That is why Sam treats a weakness that reappears after a rebuild as an image problem first and checks the image's build date and contents before writing a host finding.

### 11.4 Logging

OS logs support detection recommendations tied to ATT&CK.

A test can show more than whether an attack works. It can also show whether the defenders would have seen it. After an authorized action, such as creating a scheduled task with a test account, Sam asks the SOC whether the Windows event for task creation arrived in the SIEM and whether any rule fired. Mapping the action to its ATT&CK technique gives both teams a shared name for it. A recommendation then reads as an improvement to detection, for example forwarding the task-creation event from staging servers and alerting when a non-administrator creates a task, rather than a vague call for more logging.

### 11.5 Privileges

Hypervisor admin is a separate scope layer.

Whoever administers the hypervisor controls every virtual machine on it: they can take snapshots, attach disks and open consoles without the guest operating system recording much. Permission to test the guest servers therefore does not cover the virtualisation layer, which usually has a different owner and a different risk. At TRB the virtualisation team must sign its own scope entry before anyone tests the management console. If Sam finds hypervisor credentials while testing a guest, he records that as a finding and stops there, because using them would move the test into a layer nobody authorised.

### 11.6 Hardening baselines

Deviations need tickets, not folklore.

A baseline is the written list of settings every host of a given type should have, such as disabled legacy protocols, a minimum password policy and audit logging turned on. Real systems deviate for real reasons, for example an old application that needs a legacy protocol. The deviation is acceptable only if it is recorded with an owner, a reason and an expiry date. Without that record, a tester cannot tell an approved exception from neglect, and the next administrator inherits a setting nobody can explain. Sam checks each deviation he finds against the exception register before deciding whether to write a finding.

### 11.7 Pinning versions in the image pipeline

Image pipeline tickets must name the agent versions baked in. Sam rejects "latest" as a version string. Reproducible builds of golden images are treated like application releases.

The tag latest describes a moment, not a version. An image built on Monday with the latest agent and rebuilt on Friday can contain different code, and neither ticket shows which. Exact version numbers let a tester compare a running host with the image it claims to come from, and they let the pipeline owner roll back to a known state. Treating images as releases also means each one has a changelog, a reviewer and a retirement date.

### 11.8 Local admin census

A quarterly query lists local admins on staging. Unexpected names become tickets. Sam correlates with leaver lists.

Local administrator rights accumulate quietly. Someone is added to fix a printer driver and never removed, or a service account is given admin rights because that was quicker than working out what it needed. The census compares each host's local Administrators group with the expected list for that host's role. Names absent from the expected list are checked against the leaver list first, because an admin account belonging to someone who has left is the most urgent case. Each census is saved, so the next one shows whether the count is falling.

### 11.9 Agent drift

Hosts whose agent version differs from the image catalogue by more than one minor version open tickets automatically.

The endpoint agent is how defenders see a host, so an outdated agent may miss techniques that newer versions detect, or may fail silently. The one-minor-version tolerance allows for staged rollouts, in which some hosts update a week before others, without raising tickets for normal lag. Anything further behind usually means the host stopped receiving updates, often because it was moved to a network segment the update server cannot reach. The automatic ticket names the host, both version numbers and the date the host last checked in.

### 11.10 A rebuild that reintroduced RDP

A rebuilt staging host comes back with an old RDP posture. The image catalogue said it should not. Sam files both a host finding and an image-pipeline finding. Two owners, two tickets, one root cause class.

The host owner can fix their server the same day by disabling RDP from the user VLAN. That does nothing for the next server built from the same pipeline. The image owner's ticket asks why the catalogue and the build disagreed. Here a configuration step had been moved into an optional stage that the rebuild skipped. Linking the two tickets lets the reviewer close the host finding only after the image finding has a fix in place.

### 11.11 A forgotten temporary admin

Local admin census found a dormant "temp" admin created during an outage. Ticket, remove, verify. Dormant temps are permanent until hunted.

The account had been created at 02:00 during a storage outage so that a contractor could restart services, and the incident record said it would be removed the next morning. It was not. Its password had never been changed and it had not logged in for seven months, which made it both useless and dangerous. After removing it, Sam verified the removal on the host and added a field to the outage template for emergency accounts, each with an expiry time that the closing review must check.

### 11.12 Copying image owners on findings

Image findings always CC the pipeline owner, not only the host owner.

Host owners often cannot see the pipeline that built their servers, and pipeline owners rarely look at individual host tickets. A weakness inherited from an image falls between the two. The host owner patches their machine and closes the ticket, and the pipeline keeps producing the same weakness. Copying the pipeline owner puts the finding in front of the person who can stop it recurring. FindingsDesk does this automatically when a finding's root cause is set to image, so the routing does not depend on the tester remembering.

### 11.13 Weighting image findings for recurrence

Pipeline findings use a separate severity rubric weighted toward recurrence. One bad image can mint a hundred bad hosts.

On a single host, a weak setting might rate medium because few people can reach the host. The same setting in an image that builds every staging and production web server is a different risk, because its reach grows with each build and it returns after each local fix. The image rubric therefore asks how many hosts are built from the image, how often they are rebuilt and whether any of them are internet-facing. A medium host finding can become a high pipeline finding without any change to the technical weakness.

### 11.14 Publishing both severity scales

Recurrence-weighted rubric for images is published beside host severity. Different beasts, different scales.

Publishing both scales prevents a predictable argument. A pipeline owner who sees a high rating for a setting the host team rated medium will suspect inconsistency unless the reason is written down. The published page shows both rubrics side by side, with a worked example of one weakness rated on each. Reviewers check that every image finding states which scale it used. Having a separate scale also lets TRB track pipeline debt on its own, which made the case for funding automated image testing.

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

Both give seventy per cent, but they support very different claims. With ten trials, a single extra miss or detection moves the rate by ten points, so the true rate could plausibly be anywhere from about forty to nearly ninety per cent. With a hundred trials the plausible range narrows to roughly sixty to seventy-eight. When the SOC reports that its new rule caught seven of the ten techniques Sam ran in a purple-team session, the honest summary is that the rule probably works more often than not, and that a stronger claim needs more trials.

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

The Wilson interval is preferred to the textbook formula of p plus or minus 1.96 standard errors because that formula behaves badly with small samples and rates near zero or one. It can produce intervals below zero or above one hundred per cent, and it claims too much certainty when only a few trials were run. Wilson's version pulls the centre slightly towards one half and keeps the bounds inside the possible range. Purple-team exercises are exactly the small-sample, high-rate setting where that matters. Comparing the two printed lines shows the practical point: the same seventy per cent carries a range more than twice as wide at ten trials.

### 12.3 Base rates

Rare true issues drowned in noisy scanners waste fixer time.

Suppose a scanner flags a weakness correctly on ninety per cent of vulnerable hosts and wrongly on five per cent of patched ones, and only two per cent of TRB's thousand staging hosts are actually vulnerable. It will find about eighteen of the twenty real cases and raise about forty-nine false alarms, so roughly seven in ten flags are wrong. Developers who chase those false alarms learn to ignore the scanner. The base rate, the share of hosts that truly have the problem, decides how useful a positive result is, and that is why Sam confirms scanner output by hand before turning it into findings.

### 12.4 Ranking defences

Prefer intervals that do not overlap when claiming A beats B.

If one control stopped fourteen of twenty simulated phishing clicks and another stopped eleven of twenty, the first looks better, seventy against fifty-five per cent. Their Wilson intervals run from about forty-eight to eighty-five and from about thirty-four to seventy-four, which overlap widely, so the data cannot separate the two. Overlap does not prove the controls are equal. It shows that the experiment was too small to tell. Non-overlap is a rough, conservative rule: a formal test for the difference between two proportions is better, but the overlap check stops the most common overclaim before it reaches a slide.

### 12.5 Reporting

Managers hear counts and intervals in plain language.

A sentence such as detection was 0.7 with a 95% Wilson CI of 0.40 to 0.89 is correct and almost useless to a reader who has to decide something. Sam rewrites it as follows. The SOC detected seven of the ten techniques we tried. With so few trials, the real rate could be as low as four in ten or as high as nine in ten, so we recommend another round before changing the budget. The counts go first because people can picture them, the range comes next in words, and the sentence ends with what the uncertainty means for the decision.

### 12.6 Limits

Independence assumptions fail when tests share environment faults.

The interval calculations assume each trial is a separate draw, so that one result does not influence another. Real exercises break that assumption. If a log forwarder was down for an hour, every technique Sam ran in that hour went undetected for the same reason, and ten misses really amount to one fault counted ten times. The interval then looks narrower than the evidence justifies. Sam records the time and the target host for each trial, checks whether failures cluster, and reports a clustered failure as a single infrastructure finding rather than as a low detection rate.

### 12.7 Pulling a ranking slide

When intervals overlap, Sam forbids ranking defences as winners. A slide once claimed MFA beat phishing training on overlapping Wilson intervals; he pulled the slide and asked for more trials instead of a louder font.

The slide's author was not wrong that MFA probably helps more; prior knowledge suggests it does. The problem was that the slide presented the exercise data as proof, and the data could not carry that weight. Sam suggested wording that kept the prior and the evidence apart: industry experience favours MFA, and this exercise was too small to confirm or contradict that. He also proposed the trial count needed for a clearer answer next quarter.

### 12.8 Every interval in words

Sam requires every interval in a deck to appear once in words: "between about X and Y". Charts alone are not enough for board packs.

Error bars on a chart are easy to overlook and hard to read when slides are printed in greyscale or skimmed on a phone. A sentence survives both. The rule also catches mistakes, because writing that the rate was between about forty and ninety per cent makes a reviewer notice how wide that is, where a neat bar with a thin whisker does not. Board members who read the words consistently ask better questions, usually how to make the range narrower.

### 12.9 Planning the number of trials

A small tool suggests n for a target CI width. Sam uses it before promising detection rates to executives.

The planner inverts the interval: give it the rate you expect and how wide a range you can accept, and it returns roughly how many trials you need. For a rate near one half and a range of ten points either side, the answer is close to ninety-six trials. Running it before an exercise changes the conversation. A promise to measure detection to within ten points becomes either a commitment to about a hundred trials or an honest decision to report a wider range from the twenty trials the window allows.

### 12.10 Finance asks for one number

Finance asks for a single detection percentage for the annual report. Sam gives two sentences with intervals instead. Legal prefers his version because it cannot be read as a warranty. Uncertainty language protects the bank.

A single figure printed in an annual report becomes a public statement about the bank's defences. If TRB published that it detects seventy per cent of attacks, a regulator or litigant after a breach could treat that as a representation the bank failed to meet. Sam's sentences describe what was measured, in which exercise and with what uncertainty, which is accurate and much harder to misread. Finance gets a number to cite, and the bank does not promise more than its evidence shows.

### 12.11 Shrinking the claim

Sample size planner told Sam he needed n≈96 for a tight interval. He cut the claim instead of inventing data. Planners exist to shrink promises.

The exercise window allowed about thirty trials. Sam could have run the same techniques three times each to reach ninety-six, but repeated runs against the same hosts are not independent, so the narrower interval would have been false. Instead the report claimed what thirty independent trials supported: detection was probably above one half, and finer comparisons would need a larger exercise. The planner's main value was making that limit visible before anyone had promised more.

### 12.12 An appendix explaining the refusal

Board packs that insist on a single number get Sam's appendix with the refusal rationale. Legal endorsed the appendix.

The appendix is one page. It shows the counts, the interval and two short paragraphs. The first explains why a single percentage would overstate what the exercise measured. The second states what the bank can safely say. Writing it once saves arguing the same point every quarter, and attaching it whenever someone asks for a single figure moves the discussion from Sam's opinion to an agreed bank position. Legal's endorsement matters because the risk it addresses is legal as much as statistical.

### 12.13 Recording legal's endorsement

Refusal appendix has legal's endorsement email hash attached. Sam loves boring integrity.

The hash lets anyone later confirm that the appendix in a board pack is the version legal approved, not an edited copy. The endorsement email is stored in the governance archive, and its SHA-256 value is printed at the foot of the appendix. If the wording changes, the hash no longer matches and the change needs a new endorsement. This uses the same integrity habit as evidence handling: a document whose authority matters should be checkable without trusting whoever forwarded it.

### Worked example (synthetic TRB)

Sam shows 7/10 CI (0.40,0.89) vs 70/100 (0.60,0.78) to explain why TRB funds more trials before claiming a detection win.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX034 — Interval read.** What CI does the lab print for 7/10? *Rubric:* 3 = (0.40, 0.89); 2 = approximate; 1 = wrong; 0 = none.
- **EX035 — Why wider.** Why is the 7/10 interval wider than 70/100 at the same rate? *Rubric:* 3 = smaller sample / more uncertainty; 2 = partial; 1 = bug; 0 = none.
- **EX036 — Manager sentence.** Write one plain sentence Sam could say about 7/10. *Rubric:* 3 = count + uncertainty + not definitive; 2 = partial; 1 = "we are 70% safe"; 0 = none.

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

Authentication answers who is making the request, through a password, passkey or token. Authorization answers whether that person may do this particular thing to this particular object. An insecure direct object reference happens when an application checks the first and skips the second. A customer logs in correctly, then changes an account number in a statement URL and receives someone else's statement. At TRB, Sam tests authorization by logging in as one synthetic customer and requesting objects that belong to a second synthetic customer, so a success proves the flaw without touching any real person's data.

### 13.2 Test accounts

Named, timed, vaulted, least privilege.

Each property prevents a particular failure. A named account, such as rt-sam-cust01, ties every action in the logs to one tester, which a shared account cannot do. A timed account expires when the window closes, so a forgotten credential becomes useless rather than becoming a back door. Storing credentials in the vault keeps them out of chat messages and notes files. Least privilege means the account has only the rights the planned tests need. Testing a customer-facing flaw with an administrator account would prove nothing about what a customer can do, and would add risk if the session were hijacked.

### 13.3 Shared admins

Accountability loss; ATT&CK T1078 Valid Accounts.

When five administrators share one account, the log shows that admin made a change but not which person made it. That hampers investigations and lets mistakes go unclaimed. Shared credentials also travel. They get written into scripts, onboarding documents and configuration files, so they outlive the people who knew them. ATT&CK lists the abuse of legitimate credentials as Valid Accounts because an attacker using a real admin password looks like normal administration. Sam's finding for a shared admin account recommends named accounts that can elevate rights, and it records where the shared password was found stored.

### 13.4 MFA

Verify by config review, not phishing staff.

The question is whether multi-factor authentication is enforced on every route that matters, and the identity provider's configuration answers it directly: which applications require it, which groups are exempt, and whether legacy protocols that bypass it are still enabled. Sending real staff phishing emails to find out would involve people who did not consent to being tested in this engagement and would measure their behaviour rather than the control. Sam exports the conditional-access policies and confirms one exemption with an authorized test account. The finding names the gap precisely, for example that an IMAP endpoint accepts passwords without a second factor.

### 13.5 Service accounts

Owners and rotation dates required.

Service accounts let applications talk to databases and APIs without a person present, which also means nobody notices when they are misused. An account with no named owner cannot be rotated safely, because nobody knows which systems will break when its password changes, so it usually never changes. Sam's review lists every service account with its owner, the last rotation date and the rights it holds, then flags those with no owner, those rotated more than a year ago and those with interactive logon rights they should not need. The most common fix is making the account non-interactive.

### 13.6 Leavers

Access lingering after HR termination is a classic finding.

The gap usually comes from a process with several hand-offs. HR records the leaving date, IT disables the directory account, and nobody removes the local accounts, the SaaS logins created outside single sign-on, or the VPN certificate. Sam tests this by taking a synthetic leaver record and checking each system the role had access to. Finding one surviving login is enough for a finding. The recommendation addresses the process, for example driving deprovisioning from the HR event and listing every system that sits outside single sign-on, not just the one account that happened to be found.

### 13.7 Expiring test accounts automatically

Test account expiry is enforced by a job that disables accounts at window end and pages Sam if disable fails. Manual reminders failed twice historically; the job is now a control, not a convenience.

The page on failure is the important part. A job that silently fails is worse than no job, because everyone believes the accounts are disabled. Disabling can fail when the identity service is in maintenance or when an account was renamed, and each failure leaves a working credential in the wild. The page goes to the tester and the security lead together. Neither may close the engagement until both confirm the account is disabled.

### 13.8 Break-glass accounts

Break-glass admins are monitored and rare. Sam's review checks that break-glass was not used as daily driver during the window.

A break-glass account exists for the day the normal identity system fails. It bypasses single sign-on and usually multi-factor authentication, which makes it powerful and dangerous. Its credentials are sealed, and any use should produce an alert and a written justification. The test is simple: count its logins over the last quarter and compare them with recorded emergencies. If logins outnumber emergencies, someone is using the account for convenience. The finding then recommends fixing whatever normal access problem drove people to it.

### 13.9 Confirming the vault denies access without MFA

Vault access for credentials requires MFA. Sam tested denial without MFA and filed the deny as a positive control demo.

Controls deserve evidence when they work, not only when they fail. The test used a test account with a correct password and no second factor, and recorded the vault's refusal along with its log entry. Filing that refusal as a positive control means the next audit can rely on dated evidence instead of a configuration screenshot. It also sets a baseline. If a later test with the same account succeeds, something has changed, and the earlier record shows exactly when the control was last known to work.

### 13.10 A rotated password found in a printer

A shared admin password on the loan system is rotated, but the same password is later found in a printer config. Sam's leaver-and-secrets checklist now includes "search for password reuse artefacts" after any shared-admin finding.

Rotation fixed one system and left the old secret working wherever else it had been reused. Someone had set up scan-to-folder on the printer with the loan administrator's credentials years earlier, and the printer's web interface showed the password to anyone on the network. A shared password usually has a history, so the search covers scripts, scheduled tasks, device settings and documentation, not only the system where it was first found.

### 13.11 Testing the break-glass alert

Break-glass use during a window pages the CISO channel automatically. Sam tested the page with a staging break-glass and got a stern but correct phone call.

The call was the evidence that the alert works, because it showed that a person responded, not just that a message was sent. Before the test, Sam agreed the time with the security lead and recorded it in the engagement log, so the call could be resolved quickly. The responder still followed the full procedure and asked who was using the account, why and under which authority. That is the right behaviour, since an attacker could claim to be running a test too.

### 13.12 Auditing the leaver automation

Leaver tickets auto-open from HR events within an hour; Sam audits the automation weekly.

Automation moves the risk rather than removing it. If the link between the HR system and the ticketing tool breaks, leavers silently stop generating tickets and nobody sees a missing ticket. The weekly audit compares that week's HR terminations with the tickets opened, and checks that each ticket was closed with every listed system confirmed. One week the counts differed by three. A schema change in the HR export had renamed the leaving-date field, so the integration had skipped those records without reporting an error.

### 13.13 Searching device configurations for secrets

Printer configs are now in the secret-search path after the reuse incident. Strange places hide passwords.

Printers, network storage, door controllers and conference-room systems often authenticate to servers, and their settings pages may store those credentials in readable form. Few teams think of them as places secrets live, so they are seldom rotated or reviewed. The expanded search uses configuration exports gathered by the device owners with permission, not logins to each device during testing. Found credentials are reported to their owners and rotated. The tester does not use them, because using a credential found in a device would test a system outside the agreed methods.

### 13.14 Keeping the secret search in scope

Secret-search path expansions are logged; scope creep in search is still scope.

Each new location added to the search, such as printer exports, a wiki space or a file share, is recorded with the date, the approver and the reason. A search for passwords reads data that may contain personal information and other teams' secrets, so it needs the same authorization as any other test method. The log also explains the results. A sudden jump in found secrets in one quarter is meaningful only if readers know whether the bank got worse or the search simply looked in more places.

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

A tester needs to show that a weakness exists, not to collect what it exposes. If an API returns other customers' balances, one response containing a synthetic account's balance proves the flaw just as well as ten thousand real ones, and it creates no new copy of real customer data. Every extra record captured has to be stored, protected, reported and deleted, and it may itself become a reportable breach. Sam stops a test as soon as he has the first response that proves the issue. He records how many records the endpoint could have returned, rather than retrieving them to prove it.

### 14.2 Redaction

Mask account numbers; keep digits that prove the issue if needed.

Redaction should remove identity while keeping the proof. A screenshot showing that customer A's session displayed customer B's statement only needs the last four digits of each account number to show that the two differ. The full numbers add risk and no evidence. Names, addresses and balances are blacked out with solid boxes. Blur can sometimes be reversed and cropping can leave text in image metadata. Sam redacts on a copy, keeps the unredacted original in the vault under its retention date, and hashes both, so a reviewer can confirm the redacted image came from the original evidence.

### 14.3 Purpose limitation

Engagement evidence is not a marketing analytics source.

Customers' data reached the testing team for one reason, which was to check the bank's security under a signed agreement. Using the same screenshots to study how customers use the app, or to illustrate a sales deck, is a new purpose the customers never expected and the agreement never covered. Privacy law in many jurisdictions treats that change of purpose as needing its own legal basis. The practical rule at TRB is simple. Evidence answers questions about the engagement it came from, and any other question needs separate data that was collected for that purpose.

### 14.4 Access

Need-to-know on evidence vaults.

The evidence for one engagement is read by its testers, its reviewer and the custodian, and by nobody else by default. A developer fixing a finding sees the finding's description and the redacted proof, not the raw capture. A manager sees status and severity. Access requests outside those roles go to the engagement lead with a reason and an end date. Need-to-know also limits damage. If one tester's account is compromised, the attacker reaches one engagement's evidence, not every screenshot the team has taken in five years.

### 14.5 Cross-border

Cloud regions may implicate rules; legal advises.

Evidence stored in a cloud service sits in a particular region, and backups or support access may reach others. If the evidence contains personal data about customers in one country and the storage or the vendor's support staff are in another, data-transfer rules may apply, along with the bank's own commitments to its regulator. Testers are not expected to interpret those rules themselves. They are expected to notice when evidence is about to cross a boundary, for example uploading to a new tool or sharing with an overseas vendor, and to ask legal before doing it.

### 14.6 Breach risk

Evidence vaults are high-value targets; protect them.

A testing team's vault holds the bank's weaknesses, proof of how to reach them and samples of the data behind them, which together make an attacker's roadmap. The vault therefore gets controls at least as strong as the systems it describes: multi-factor authentication, logged access, encryption at rest, short retention and its own place in the incident plan. If the vault were compromised, the bank would have to treat every unfixed finding in it as potentially known to an attacker. That is why TRB prioritises fixes for weaknesses recorded in an exposed vault, whatever their original severity.

### 14.7 Re-identification drills

Re-identification drills pair a redacted screenshot with public org charts. If a peer can name the person, redaction fails the gate. Sam now prefers synthetic personas in most teaching screenshots.

The drill tests what a reader can work out, not just what was blacked out. A screenshot of an internal admin page might hide a name but leave a job title, a branch code and a timestamp, and together with a public organisation chart those identify one person. Peers get ten minutes and only public sources. A successful identification is not counted as a mistake by the redactor. It shows that the redaction rule missed a kind of field, and the rule is updated.

### 14.8 A library of synthetic evidence

A library of synthetic screenshots covers common findings so learners need not handle real customer pixels. Sam contributes one new synthetic each term.

Each entry recreates a typical finding on a mock-up of TRB's interfaces, such as a statement page showing the wrong customer, an error message leaking a stack trace or an admin panel reachable without login, using invented data throughout. Training, report templates and conference talks draw from the library instead of from engagement folders. Building an entry takes a few hours, and it permanently removes the temptation to redact a real screenshot for a slide.

### 14.9 Purpose tags on evidence

Evidence files tagged with purpose; secondary use requires a new tag and approval. Marketing cannot "just borrow" engagement screenshots.

The tag is set at upload. In most cases it is engagement evidence, and for a few files it is engagement evidence plus approved training use. FindingsDesk checks the tag whenever a file is copied to another workspace or attached to anything other than a finding, and blocks the action if the purposes do not match. Adding a purpose requires the engagement lead's approval and a privacy check. The tag turns a policy sentence into a check that runs every time a file moves.

### 14.10 Learners choose the synthetic example

Synthetic screenshot library item SS-17 shows a fake customer "Ada Example" with account ••••4242. Learners prefer it to redacting real screens. Sam measures that preference and funds more synthetic art.

The preference is practical as well as ethical. Redacting a real screenshot properly takes a learner twenty minutes and a reviewer's check, while the synthetic one is ready to use and carries no risk if it ends up in the wrong place. Sam tracks how often each library item is used. The most-used items show which findings learners write about most, and those are the next ones turned into synthetic versions.

### 14.11 A blocked copy to a design folder

Purpose tags blocked a well-meaning trainee from dropping engagement screenshots into a UX redesign folder. The refusal felt petty and protected a hundred customers.

The trainee's idea was reasonable on its face. The screenshots showed real confusing screens that the design team wanted to improve. They also showed real customers' names and partial balances, and the design folder was shared with an external agency. The fix took one afternoon. The trainee described each confusing screen in words and the design team rebuilt it with synthetic data. The agency got what it needed and no customer data left the bank.

### 14.12 Keeping synthetic personas obviously fake

Synthetic Ada Example has a style guide so artists keep her obviously fake.

A synthetic persona that looks too real causes the problems it was meant to prevent. Readers may assume it is a redacted real customer, or the details may accidentally match a real person. The style guide fixes the giveaways: names from an agreed invented list, account numbers ending in well-known test digits, addresses on streets that do not exist in TRB's region, and dates in a reserved test year. Anyone who sees those markers can recognise teaching material at a glance.

### 14.13 Agreements with illustrators

Artists sign a CLA that Ada Example may not resemble real customers. Legal insisted; Sam agreed happily.

Illustrators sometimes base faces and handwriting on people they know or on stock photographs of real people. In a bank's training material, a persona that resembles a real customer could imply that the customer's account was involved in a security finding. The contributor agreement makes the artist confirm that every likeness is invented, and gives TRB the rights to reuse and change the artwork. That second part matters as much as the first, because synthetic examples must be updated when the real interfaces change.

### 14.14 Desk visits for new analysts

Privacy coaches at TRB include a five-minute desk visit when a new analyst first opens the evidence vault. Sam scripts the visit: show retention dates, show access list, show one redaction fail example, ask the analyst to repeat the minimisation rule in their own words. Desk visits catch bravado better than LMS modules. Analysts sign a tiny card that stays in the vault foyer.

A rule learned from a document is easily forgotten. A rule shown at the desk on the analyst's own screen, with their own engagement's retention date, tends to stick. The redaction failure example is chosen to be uncomfortable: a screenshot that looked clean until a colleague named the person in it. Asking the analyst to restate the rule shows whether they understood it or just nodded along.

### Worked example (synthetic TRB)

Sam redacts all but last four digits before attaching a screenshot to F4.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX040 — Minimisation.** Why not export the full customer table for a finding? *Rubric:* 3 = privacy/purpose/ROE; 2 = partial; 1 = need it; 0 = none.
- **EX041 — Redaction.** What does Sam redact in the screenshot example? *Rubric:* 3 = account numbers except last four / personal identifiers; 2 = partial; 1 = vague; 0 = none.
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

A cryptographic hash such as SHA-256 turns a file into a short fingerprint that changes completely if even one byte changes. Sam hashes each evidence file when he captures it, and again when he attaches it to a finding. If the values differ, something touched the file in between, perhaps an image editor that re-saved it, a sync tool that converted line endings or a careless redaction on the original. Catching that before the report goes out is easy. Explaining it after a client disputes the finding is much harder, because a changed file looks the same as a doctored one.

### 15.2 Metrics

Assets touched, cards run, owners assigned — not raw finding counts.

A count of findings mostly measures how hard the testers looked and how they split issues into separate records. A rise from forty to sixty could mean the bank got worse, the scope grew or one weakness was logged per host instead of once. More useful measures describe the work and its effect: how many in-scope assets were actually tested, how many planned test methods were completed, how many findings have a named owner and a due date, and how long fixes take. PulseMap reports these, so a manager can tell whether a quiet quarter means safety or little testing.

### 15.3 Custody

Who/when/where for each artifact.

A chain-of-custody record lists every point at which evidence changed hands or location: captured by Sam on a testing laptop at 21:14, uploaded to FindingsDesk at 21:20, read by the reviewer the next morning, exported in redacted form for the report. Each entry has a person, a time and a place. If a finding is challenged months later, the record shows that the evidence presented is the evidence captured and who could have altered it. Gaps are recorded as gaps. An honest note that a file sat on a laptop for two days is better than a record that hides it.

### 15.4 Integrity vs truth

Matching hash ≠ live system still vulnerable.

A matching hash proves only that the evidence file has not changed since it was captured. It says nothing about whether the weakness still exists, whether the evidence was correctly understood, or whether the test was valid. A screenshot can be perfectly preserved and still show a misreading. A server that was vulnerable in March may have been patched in April. That is why TRB separates evidence integrity, checked with hashes, from finding status, checked by a retest. Report statements are dated to the moment of testing, for example that the endpoint returned another customer's data on 4 March, not that it does so now.

### 15.5 Sampling

Sample closed tickets for verification evidence.

Checking every closed ticket is rarely affordable, and checking only the ones that someone flags misses quiet failures. A random sample avoids both problems. Because the sample is chosen by chance, teams cannot predict which tickets will be checked, so every ticket needs evidence that the fix works, such as a retest result, a configuration diff or a scan. If the sample turns up missing evidence, the share missing in the sample estimates the share missing overall, and the interval methods used for detection rates apply to this proportion too.

### 15.6 PulseMap

Coverage views must show denominators.

A green tile that reads ninety per cent coverage hides the question that matters, ninety per cent of what. If PulseMap counts only the hosts in the asset inventory, and the inventory lacks a cloud account set up last quarter, the real coverage is lower than the tile suggests. Each coverage view therefore shows the count behind the percentage, such as forty-five of fifty registered web applications, and names the source of the total. Readers can then see when the denominator itself looks too small, which is often the most important finding on the dashboard.

### 15.7 Random sampling of closed tickets

Closed-ticket sampling is five tickets per month, chosen by RNG. Missing verification evidence reopens the ticket automatically. Sam publishes the reopen count so gaming the metric is visible.

The random draw is logged with its seed, so anyone can confirm that the five tickets were not hand-picked. Automatic reopening keeps the consequence impersonal. It is not Sam accusing a team, it is the rule applying itself. Publishing the reopen count makes improvement visible too. When one business unit's reopens fell from three a month to zero, the falling count showed its fixes were now being verified, not merely closed.

### 15.8 A dictionary for metric terms

A shared dictionary defines "touched", "validated" and "closed". Sam refuses PulseMap tiles that use undefined words.

The same word can mean different things to different teams. To a developer closed may mean the code was merged, to operations that it was deployed, and to the testers that a retest passed. A tile counting closed findings is meaningless until the word is fixed. Each dictionary entry gives a definition, the data field it maps to, an example and a counter-example. When a new tile is proposed, its labels are checked against the dictionary before it is published.

### 15.9 What counts as touched

"Touched" means a method card finished with evidence, not a ping. Sam's dictionary fight on that word was worth a week.

Under the loose definition, a host answered a network sweep and so counted as covered. Under the strict one, a planned test method was completed against it and left evidence. The difference was large. Coverage measured by sweeps was close to one hundred per cent, while coverage measured by completed methods was about sixty. The strict definition was less flattering and far more useful, because it showed which assets had never really been tested.

### 15.10 A green tile with two data points

PulseMap's tile subtitle "n=2" next to a green check teaches more than a lecture on sample size. Sam deliberately leaves a small-n green tile in the training environment to provoke questions.

The tile shows that both of two sampled tickets had verification evidence, which is a hundred per cent with almost no information. Learners who see it usually start by saying the control is working, and then someone notices the n. The discussion that follows covers what two observations can support, how wide the interval is and what tile design would prevent the misreading. That last question led to the rule that tiles with very small samples cannot turn green.

### 15.11 Signing off the definitions

Dictionary fight ended when CISO signed the definitions. Sam frames the signed PDF in the team wiki. Words are controls.

The signature settled the argument by making the definitions bank policy rather than the testing team's preference. Teams that disagreed could still propose changes, but through a review with a version number, not by quietly using their own meaning on a dashboard. Each PulseMap tile now cites the dictionary version it uses. When a definition changes, old and new figures are not plotted on the same line without a marker, so a jump caused by redefinition is not mistaken for real change.

### 15.12 Definitions on paper

Signed metric definitions hang next to the team coffee machine — paper still works.

A printed page on the wall is seen by people who would never open the wiki, including visitors from other teams who come to ask what a number means. Its main use is in quick conversations. When someone says a finding is closed, a colleague can point to the definition and ask whether the retest passed. The page carries its version number and date, so an out-of-date printout is easy to spot and replace when the signed version changes.

### 15.13 A yellow state for undefined terms

Undefined-word tiles show a yellow "define me" state instead of green. Yellow is harder to ignore.

A tile using a term missing from the dictionary still shows its number, but it cannot be green, because nobody can say what green would mean. The yellow state names the undefined word and links to the form for proposing a definition. This avoids two worse options. Hiding the tile loses information, and showing it green gives false reassurance. In practice most yellow tiles are fixed within a week, usually by mapping the label to an existing term.

### 15.14 Measurement office hours

Measurement office hours run Thursdays. Anyone may bring a tile that feels misleading. Sam's most common fix is adding n to the subtitle or changing green to yellow. He tracks how many tiles change colour each month as a quality metric of the metrics.

Office hours give people a low-stakes way to question a number without accusing whoever built the tile. Many complaints turn out to be about labels rather than data. A tile reading incidents may really be counting alerts, and the fix is a better title. Tracking colour changes shows whether the dashboard is becoming more honest over time. A month with no changes either means the tiles are good or that people have stopped coming.

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

A zone groups systems that share a level of trust and the same rules for what may reach them. TRB's internet zone is untrusted. The DMZ holds the public banking front end, which must talk to both the internet and the core. The corporate zone holds staff laptops and email. The payments-adjacent zone is restricted because it borders the SWIFT gateway and the ledger, and the assessment zone holds the testing platform. Testers read a finding through the zones it crosses. A path from the corporate zone straight into the payments-adjacent zone is serious even when the system at the far end is only moderately sensitive.

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

The register is the bank's statement of intent, and observed traffic is evidence of what actually happens. The lab compares the two and reports flows that were seen but never approved. A direct path from the web tier to the ledger database bypasses the core API, which is where authorization and input checks live, so anything that compromises the web server could reach the ledger without those checks. The finding records when the flow was observed, its source and destination, and the fact that no register entry or change ticket covers it.

### 16.3 Fail closed

Proxies and TrackScope deny when policy missing.

A control that fails closed blocks traffic or actions when it cannot decide, for example because its policy file is missing, its database is unreachable or a rule is malformed. A control that fails open lets everything through in those cases, which is convenient during an outage and disastrous if an attacker can trigger the failure. Sam tests the behaviour safely in staging. He renames TrackScope's policy file and confirms that the platform refuses to start a test, rather than running without scope checks. The proxy test works the same way: with its rule set unavailable, outbound requests must be refused.

### 16.4 Conduits

Owned firewall rules.

A conduit is the approved path between two zones, made up of the firewall rules, ports and protocols that let one zone talk to another. Every conduit needs an owner, the person who can explain why the path exists, approve changes and decide whether it is still needed. Rules without owners pile up: a port opened for a migration years ago remains because nobody knows whether removing it will break something. When Sam finds traffic using a conduit, the first question is not whether the rule allows it but who owns the rule, because only that person can say whether the traffic is intended.

### 16.5 Third parties

Processors need their own authorization.

TRB uses outside companies for SMS one-time codes, card processing and cloud hosting. Their systems sit in TRB's architecture diagrams, but TRB does not own them and cannot authorise anyone to test them. Testing a vendor's service usually requires the vendor's written permission under its own terms, and some cloud providers publish rules about what customers may test in their own tenancy. Sam can test how TRB's systems use a third-party service, for example whether the bank validates the vendor's responses, while leaving the vendor's infrastructure alone unless that vendor has signed off.

### 16.6 Diagrams

Dated and owned.

An architecture diagram is a claim about how systems are connected at a particular time, and an undated one invites testers and auditors to trust a picture that may be years old. Every TRB diagram carries a date, an owner and the version of the flow register it reflects. Before an engagement, Sam checks that the diagram's date is later than the last major change to the systems in scope. If it is not, the first task is to confirm the current layout with the owner. Testing against an outdated diagram can mean missing new paths or, worse, probing addresses that now belong to something out of scope.

### 16.7 Detecting rule changes during an engagement

Matrix excerpts are hashed and stored beside the ROE. If network changes mid-engagement, Sam diffs the live rules against the hash and pauses if they diverge without a change ticket.

The hash fixes the environment the authorization was written for. If rules change during the window, the test may now reach places the scope assumed were unreachable, or results may reflect a temporary configuration rather than the normal one. Pausing gives the conduit owner time to confirm that the change was intended. If it was, the scope is re-checked against the new rules. If it was not, an unexpected change is itself something the bank needs to know about.

### 16.8 Contacting conduit owners

Each conduit lists an on-call. During tests Sam messages the conduit on-call, not a general IT inbox, when rules misbehave.

A general inbox is read by whoever is free, possibly hours later, and that person may not know the conduit or have the authority to change it. During a testing window both delays matter. If a firewall rule unexpectedly blocks the test, or unexpectedly allows something it should not, the person who owns that conduit can decide quickly whether to pause, correct the rule or continue. The on-call contact is listed in the flow register next to the conduit, so testers do not have to work out who to call while something is going wrong.

### 16.9 Marking flows that need third-party authorization

Flow matrices include a column "third-party auth needed?". Yes rows cannot be tested under TRB ROE alone.

The column makes a legal boundary visible at the place testers plan their work. A flow from TRB's core API to the SMS vendor's endpoint is marked yes. Sam may observe what TRB sends and receives, but may not probe the vendor's endpoint for weaknesses. The column is filled in by whoever registers the flow, not by the testers, so the decision is made by people who know the contracts. When a yes row matters to an engagement, the plan includes requesting the vendor's permission or noting the gap in the report.

### 16.10 A temporary rule with no expiry

When lab_flows shows web→ledger-db, network claims the rule is temporary. Sam asks for the change ticket and kill-date. Neither exists. Temporary without expiry becomes F3's twin process finding.

The technical finding is the open path. The process finding is that a rule could be added as temporary without any mechanism to remove it. Fixing only the first would close this rule and leave the next temporary one just as likely to persist. The process finding recommends that the firewall change workflow require an expiry date for temporary rules and alert the owner a week before it.

### 16.11 Pointing a curious tester to the vendor's programme

Third-party column "yes" blocked a curious scan of the SMS vendor. Sam sent the vendor's bug bounty link instead. Boundaries can still be helpful.

The colleague's curiosity was reasonable, since the vendor's endpoint looked dated and probably had problems. Scanning it from TRB's network under TRB's rules would have been unauthorised testing of another company. The vendor's bug bounty sets out what researchers may test, how and with what legal protection. Following it, from personal equipment and on personal time where the programme allows, kept the interest legitimate and kept TRB out of it.

### 16.12 Making expiry dates visible

Kill-date calendar invites include the CISO alias as optional attendee for visibility.

The invite is created when a temporary rule is approved and falls on its expiry date. The owner is the required attendee. The CISO's office is optional, which means it is not expected to act but can see the full list of temporary rules simply by opening the calendar. On the day, the owner removes the rule or extends it with a new approval and a new date. An invite nobody acts on remains on the shared calendar as a past event with no change ticket, which makes the miss easy to find.

### 16.13 Linking technical and process findings

Twin process findings link to F3 with a related-id field. Boards see technical and process debt together.

Without the link, the two findings travel separately. The technical one is fixed quickly and disappears from reports, while the process one waits in a governance backlog with no visible connection to any real exposure. The related-id field keeps them together, so a board report shows that a serious open path existed and why it could exist. Reviewers do not close the technical finding as resolved at its root while its process twin is still open.

### 16.14 Architecture office hours

Architecture office hours use a projector and a red pen. Unowned conduits get circled until an owner appears in the register. Sam refuses to schedule tests through unowned conduits even if the firewall rule exists. Ownership is part of authorization.

A circled conduit stays on the projected diagram from week to week, which puts gentle public pressure on the team whose firewall rule it is. Refusing to test through unowned conduits is not obstruction. Without an owner there is nobody who can accept the risk of the test, pause it or explain unexpected results, so the precondition for authorised testing is missing.

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

TLS keeps someone on the network path from reading or silently altering traffic between a customer's browser and TRB's servers, and it lets the browser check that it is talking to the bank's real domain. It does nothing about what happens once the request arrives. If the application gives customer A customer B's statement, it does so over a perfectly encrypted connection. Findings keep the two apart. An outdated protocol version or a weak cipher suite is a transport finding. A missing ownership check is an application finding, and fixing the TLS settings would leave it untouched.

### 17.2 At rest

Evidence vault encryption and key access logs.

Encrypting the vault's storage protects against someone obtaining the disks, backups or snapshots without going through the application, for example a misconfigured storage bucket or a discarded drive. It does not protect against anyone who can log in to the vault normally, because the application decrypts data for them. The key that unlocks the storage is the real asset, which is why its use is logged separately from file access. A burst of key-use events with no matching vault logins would suggest that someone is reading storage directly, which is the scenario encryption at rest exists to stop.

### 17.3 Hashes

SHA-256 for evidence integrity, not for password storage design lectures here.

A general-purpose hash such as SHA-256 is designed to be fast, which suits fingerprinting evidence files: hashing a large screenshot archive takes seconds and any change shows up. The same speed makes it a poor choice for storing passwords, where slowness is a deliberate defence against guessing. Password storage needs dedicated functions such as Argon2 or bcrypt, a topic for the identity chapters. In this book SHA-256 answers one question, whether this is the same file that was captured, and testers should not assume a system is secure because it uses a hash somewhere.

### 17.4 Anti-patterns

Homegrown crypto for TrackScope tokens is forbidden.

An early TrackScope prototype built session tokens by base64-encoding the tester's name and a timestamp, then XORing the result with a fixed string. It looked unreadable and offered no protection. Anyone who saw two tokens could recover the fixed string and forge new tokens. The rule since then is to use the framework's signed-token library or a vetted standard such as signed JWTs with a key held in the vault, and never invent an algorithm or encoding. When Sam sees opaque tokens in a system under test, he checks whether they change predictably between requests, which is a common sign of homemade schemes.

### 17.5 Key custody

Platform keys in HSM or vault with dual control where required.

Whoever holds a signing key can impersonate the system that uses it. TRB's most important keys, such as the one that signs TrackScope's scope files and the vault's master key, sit in a hardware security module. The HSM performs operations with the key but does not hand the key out. Dual control means sensitive operations, such as exporting a key or changing who may use it, need two authorised people acting together, so no single compromised or careless account can do them alone. Less critical keys live in the software vault, still with logged access and named owners.

### 17.6 Limits

Crypto does not stop authorized malicious admins with valid keys.

Encryption, signing and hashing protect against people without the keys. An administrator who legitimately holds a key can decrypt, sign or alter data, and the cryptography will faithfully confirm their actions as valid. Controls against insiders are therefore procedural and detective: separation of duties, dual control for the most sensitive operations, logging that the administrator cannot erase, and reviews of key use. When a report says data is protected by encryption, Sam adds who can decrypt it, because that list is where the remaining risk sits.

### 17.7 Testing the key export denial

HSM export ceremonies for platform keys require two people and a reason code. Sam's intern role cannot export. He tested the denial by attempting an export in staging and filing the deny log as evidence that the control works.

The test was cleared in advance with the HSM owner and run against a staging key that protects nothing real, so a failure would have had no consequences. The deny log records the account, the requested operation, the time and the reason for refusal. An auditor can rely on that record rather than on a statement that the policy exists. It also gives a reference point if the control's behaviour ever changes.

### 17.8 Short-lived platform tokens

Platform tokens expire within the window plus one hour. Sam tests that expired tokens cannot file findings. Lingering tokens are findings against the platform.

A token that outlives its purpose is a credential waiting to be stolen. The extra hour lets testers finish writing up after the window closes, and anything longer only adds exposure. The test is straightforward. Sam keeps a token from a finished window, waits past its expiry and tries to create a finding with it. The platform must refuse, and the refusal must appear in the log. If the attempt succeeds, the finding names the platform component that failed to check expiry.

### 17.9 Recording key ceremonies

Ceremony notes list attendees and key ids, never secret material. Sam files notes in the vault with the same retention as evidence.

A key ceremony is the formal event in which a key is created, rotated or exported under dual control. Its notes show that the event followed procedure, covering who was present, which key was involved, which reason code applied and what each person checked. Secret values never appear, even partially, because the notes are read by auditors and reviewers who should not be able to rebuild a key. Keeping the notes with the evidence retention schedule means they are available as long as anything signed with that key might be questioned.

### 17.10 A key-shaped string blocked in CI

Sam attempts to commit a "temporary" base64 blob that looks like a key. CI fails. He is glad. The failure message links to the key ceremony doc. Guardrails should teach, not only block.

The blob was a test fixture copied from staging, and Sam meant to remove it before merging. A secret scanner in the pipeline does not trust intentions. Once a key is in version history it is in every clone of the repository, and deleting it in a later commit does not remove it. The message's link explained how to request a proper test key, which fixed the immediate problem and showed the correct route next time.

### 17.11 When short token lifetimes inconvenience people

Token lifetime plus one hour once bit an analyst writing late. Better a re-auth than a token in a stolen laptop weeks later.

The analyst lost a few minutes of unsaved text when the token expired mid-sentence. The reasonable response was to fix the inconvenience without lengthening the lifetime. FindingsDesk now saves drafts locally in encrypted form and asks the user to sign in again before submitting, rather than discarding the work. Security controls that cost people effort tend to be worked around, so reducing the cost without weakening the control is part of designing it.

### 17.12 Keeping denials as evidence

Ceremony deny logs are retained as positive evidence for examiners who ask whether intern roles are enforced.

Examiners often ask how the bank knows a restriction is enforced rather than merely written down. A configuration export shows the intended setting. A dated record of a real attempt being refused shows the setting in effect. The deny logs are filed with the control they relate to and refreshed whenever the HSM software or role definitions change, so the evidence never describes an older version of the system than the one being examined.

### 17.13 Using denial records in onboarding

Positive deny evidence packets are reused in onboarding week one.

New staff learn more from seeing a real control refuse a real request than from reading that keys are protected. Each packet pairs the request, the refusal and the policy that caused it, and shows how to read the log. It also sets expectations. New interns see on day one that their role cannot export keys and that trying leaves a record, which makes the rule concrete. The packets contain only staging data and are reviewed before reuse.

### Worked example (synthetic TRB)

Sam rejects a PR that encrypts scope files with a hard-coded AES key in source.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX049 — TLS vs AuthZ.** Does TLS fix IDOR? *Rubric:* 3 = no, because TLS does not fix authorization bugs; 2 = no, without explanation; 1 = yes; 0 = none.
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

"Does control X raise detection of T1566 in staging?" beats "is security good?".

A research question has to name what will be measured, under which conditions and against what comparison. Asking whether security is good invites opinions that cannot be wrong and cannot guide a decision. Asking whether a new email filter raises detection of phishing technique T1566 in the staging environment, compared with the current filter, names the control, the technique, the place and the baseline. That question decides the design: a fixed set of phishing samples, a staging mailbox under each filter, and a recorded detection or miss for each sample. Vague questions produce vague work.

### 18.2 Design

Fixed test set, recorded environment, sample size plan.

Three choices decide whether a later reader can trust the result. The test set is written down before any trial runs, so nobody can drop the samples that make a control look bad. The environment is recorded: which filter version, which mailbox configuration, which date. Without that record, a later change can make the result unreproducible. The sample size is planned for the precision the decision needs, using the same interval methods as detection reporting. A design that skips any of these can still produce a number, but that number will not settle an argument.

### 18.3 Pre-registration

Write metric and threshold before seeing results.

People naturally adjust what counts as success once they have seen the data. A detection rate of sixty per cent can be called a success or a failure depending on what the team hoped for. Pre-registration writes the metric and the threshold into a dated note before the first trial runs, for example that the new filter succeeds if its Wilson interval's lower bound exceeds the current filter's observed rate. Changing the threshold afterwards is allowed, but it must be labelled as exploratory. The dated note is what stops a hopeful reinterpretation from being presented as the original plan.

### 18.4 Ethics

Customer data off-limits; synthetic phishing to staff needs HR/CISO approval.

Research that uses real customer messages or accounts is outside this book's methods and TRB's testing agreements. Synthetic phishing sent to real staff is also not an ordinary technical test. It involves people who may feel deceived, and it can affect trust in security messages. Any such trial therefore needs HR and CISO approval that states the purpose, the population, the messaging, the opt-out where feasible and how results will be reported without naming individuals. Technical curiosity is not an approval.

### 18.5 Negative results

Publish internally; they prevent repeated failed ideas.

A trial that shows a control made no measurable difference is as useful as one that shows it did, because it stops the next team from spending another quarter on the same idea. Negative results also calibrate expectations. If three awareness campaigns have each failed to move click rates in staging exercises, the next proposal for a fourth campaign faces a higher bar. Internal publication means a short write-up on the trial board with the pre-registered metric, the result and a sentence on what not to try again. Hiding negative results makes the organisation relearn the same lesson.

### 18.6 Limits

Staging ≠ production; state threats to validity.

Staging is quieter, cleaner and differently monitored than production. A detection rate measured there can be higher because traffic is lighter, or lower because production has extra sensors. Threats to validity are the reasons a result might not transfer: the sample was too small, the phishing kit was outdated, the filter was misconfigured, the SOC was told a trial was running. Naming them does not weaken the report. It tells a decision-maker how far to lean on the finding. A result with no stated limits is the one to distrust.

### 18.7 Writing up a negative result

Negative results get the same template as positive ones. Sam's "MFA prompt fatigue did not improve T1566 detection in n=40" note stopped a second identical trial the following quarter.

The template forces the same fields: question, design, pre-registered threshold, result, limits. Using a different, apologetic format for negative results makes them look like failures of the team rather than findings about a control. The fatigue trial showed that adding more MFA prompts did not raise detection of the phishing set, which redirected the next proposal toward phishing-resistant authenticators instead. Without the write-up, the same fatigue idea would have returned with a new sponsor.

### 18.8 An internal trial board

A public (internal) board shows pre-registered trials and their status. Duplicate trials are rejected at a glance.

The board lists the question, the owner, the planned sample size and whether the trial is planned, running or written up. Anyone proposing a new trial searches it first. Duplicates are common when teams work in parallel and each believes its idea is original. Rejecting a duplicate early saves a cohort of staff or a block of staging time, and often leads the proposer to join the existing trial instead. The board is intentionally boring. Its job is to make repetition visible.

### 18.9 Preferring intervals to false significance

Sam avoids claiming significance without a plan. Most purple trials at TRB are descriptive with intervals, not pseudo-clinical trials.

A p-value computed after the fact from a small convenience sample does not mean what people think it means. It can look decisive when the true uncertainty is large. TRB's default is therefore to report counts and Wilson intervals, and to reserve formal significance claims for the rare trials that were designed for them with a sample-size plan. Descriptive reporting is not a lesser form of evidence. It is honest about what a forty-trial purple exercise can support.

### 18.10 A failed awareness trial still earns a write-up

A pre-registered trial on awareness mail fails its threshold. Sam still writes it up. The next quarter's budget meeting cites the negative result to avoid buying the same content pack again.

The content pack's vendor had promising case studies from other industries. The TRB trial, with a fixed phishing set and a pre-registered detection threshold, did not meet that threshold. Writing it up prevented both a quiet burial and a heated argument based on anecdotes. Budget meetings prefer a dated result to a feeling that the training "seemed useful". The vendor was invited to propose a different pack for a new trial rather than resell the same one.

### 18.11 Joining an existing trial instead of duplicating it

Registration board rejected a duplicate trial title within a minute. The author joined the existing trial as a helper instead of wasting a cohort.

The duplicate had slightly different wording but the same control, the same technique and the same staging population. Running both would have split the available volunteers and left each trial underpowered. Joining as a helper meant the second author contributed samples and review time, earned co-ownership of the write-up and still answered their underlying question. The board's value is not rejection for its own sake. It is redirecting effort toward a result that can decide something.

### 18.12 Celebrating negative results

Negative results get a champagne cork icon in the board — celebration of learning, not failure.

Culture decides whether people file negative results or hide them. A small visible reward, even a silly icon, signals that the organisation wants the learning. The icon appears only when the write-up is complete, so it cannot be earned by failing to finish. Teams that publish negative results are thanked in the quarterly research summary alongside teams that publish positive ones. Over a year the board's mix of corks and ordinary ticks shows whether the culture is working.

### 18.13 Icons do not replace write-ups

Champagne cork icons are optional; the write-up is not. Sam rejects icons without prose.

An icon without a linked write-up would let a team claim credit for a negative result that nobody can learn from. The board's rule is that the icon is rendered only when the write-up fields are filled: question, design, threshold, result, limits. Rejecting a bare icon is occasional and slightly awkward, and it keeps the board useful. Celebration that does not leave a reusable record is just decoration.

### 18.14 A linter for empty celebrations

Icons without prose are stripped by the board's markdown linter.

The linter is a short check that runs when a board entry is saved. If it finds a cork icon and empty write-up fields, it removes the icon and leaves a comment asking for the prose. Automation matters here because Sam cannot review every edit. The linter also stops well-meaning colleagues from adding icons to old entries that never had write-ups, which would invent a history the board does not have.

### Worked example (synthetic TRB)

Sam pre-registers: success if detection ≥80% on 50 T1566-style synthetic emails with Wilson lower bound ≥0.7.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX052 — Bad question.** Why is "is security good?" a poor research question? *Rubric:* 3 = not measurable/specific; 2 = partial; 1 = fine; 0 = none.
- **EX053 — Pre-register.** What should be written before results? *Rubric:* 3 = metric and threshold (and design); 2 = partial; 1 = vague; 0 = none.
- **EX054 — Staff phishing.** What approvals before simulated phishing? *Rubric:* 3 = CISO/HR (and ROE); 2 = one; 1 = vague; 0 = none.

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

NIST SP 800-115 distinguishes several kinds of security testing. A review examines designs, configurations or code without attacking a live system. A vulnerability assessment looks for known weaknesses with tools and light manual checks, usually with broad permission and limited stealth. Red teaming emulates an adversary with specific goals, often under tighter rules about detection and impact. Confusing the names leads to wrong expectations. A quarterly web assessment cannot answer whether a determined attacker would reach the ledger unnoticed, and a threat-led exercise cannot replace regular regression checks on the customer portal.

### 19.2 PTES

Pre-engagement through reporting as shared stage names.

The Penetration Testing Execution Standard names stages that most authorized tests share: pre-engagement, intelligence gathering, threat modelling, vulnerability analysis, exploitation, post-exploitation and reporting. TRB uses those names so that planners, testers and clients mean the same thing by each stage. Pre-engagement is where scope and rules are signed. Reporting is where findings are written for owners, not where new testing happens. Using shared stage names also makes gaps obvious. An engagement that jumps from intelligence gathering to reporting without analysis has skipped the work that turns observations into findings.

### 19.3 Threat-led

TIBER-EU and CBEST use intelligence to shape scenarios for financial entities; TRB studies them even when running lighter tests.

Threat-led exercises start from who is likely to attack this kind of institution and what they usually want, then build scenarios around that picture. TIBER-EU and CBEST are frameworks banks use for such exercises under regulatory oversight. Ordinary TRB web tests are lighter and more frequent, but the threat-led idea still shapes them. Scope meetings ask which techniques current threat reporting highlights for retail banks, and the method cards for the quarter favour those techniques. Studying the frameworks also keeps the team honest about what a light test cannot claim.

### 19.4 Theory of change

Testing informs risk decisions; it does not create security by itself.

A successful engagement produces evidence that a risk owner can use: a weakness exists, it is reachable under stated conditions, and fixing it would remove that path. Security improves only if someone then decides to fix it, accept it with a compensating control or change the system so the path no longer matters. Testing that produces findings nobody owns is expensive journalism. TrackScope therefore requires an owner and a due date before a finding can leave draft, and PulseMap tracks age so that informed-but-ignored risks stay visible.

### 19.5 Assurance limits

A clean test is time-bounded assurance, not a warranty.

A test that finds nothing serious shows that, under the methods used, against the systems in scope, during that window, the testers did not demonstrate a serious weakness. It does not show that no weakness exists, that none will appear next week when a new feature ships, or that a different adversary with different methods would fail. Reports state this limit explicitly. TRB forbids phrases that turn a clean test into a guarantee, because those phrases become liabilities when the next incident happens.

### 19.6 Platform role

TrackScope encodes theory as executable deny rules.

Ideas about authorization, scope and fail-closed behaviour only protect the bank when they run as code. TrackScope refuses to start a test without a signed scope file, refuses targets outside that file, refuses methods the rules mark as forbidden and stops when its policy cannot be loaded. Encoding the theory means a tired tester at midnight gets the same refusal as a careful one at noon. It also means that improvements to the theory, such as a new exclusion, become improvements to every engagement the moment the scope file is updated.

### 19.7 Stating what each test type cannot claim

The assessment catalogue includes what each type cannot claim. Annual web tests cannot claim threat-led coverage; threat-led exercises cannot claim quarterly regression coverage. Sam quotes the cannot-claim line in kickoffs.

Clients and internal sponsors naturally stretch what they bought. After a clean web test someone asks whether the bank is safe from nation-state actors. After a threat-led exercise someone asks why a simple regression bug reached production. The cannot-claim line, read aloud at kickoff and printed in the report, answers both before they become arguments. It also sets the catalogue's value. Buyers know what they are and are not purchasing.

### 19.8 Approved sentences for reports

Approved sentences for reports include "time-bounded assurance" and forbid "guaranteed secure". Sam's linter flags forbidden phrases.

Writers under deadline reach for strong language. A library of approved sentences gives them strong-enough language that legal and the CISO have already accepted. Forbidden phrases are blocked in the report pipeline with a message that suggests a replacement. The linter is intentionally blunt. It is easier to argue with a suggested replacement than to notice a dangerous phrase in a long draft at midnight.

### 19.9 Answering questionnaires from the catalogue

Questionnaire answers cite the catalogue. Sam stops colleagues from answering "we pentest everything" when SWIFT is excluded.

Insurance and vendor questionnaires ask broad yes-or-no questions that do not match how testing actually works. Answering from memory produces overclaims. Answering from the catalogue produces sentences such as: quarterly authorized web assessments of internet-facing applications, threat-led exercise last completed in the stated year, payment gateway excluded from ordinary tests. Those sentences are defensible in a claim dispute. "We pentest everything" is not.

### 19.10 An honest answer to an insurer

An insurer questionnaire says "Do you conduct red teaming?". Sam answers with the catalogue: quarterly web tests yes; full threat-led last done 20XX; SWIFT excluded from ordinary tests. Checkbox honesty beats swagger.

The form wanted a yes or no. The honest answer is a short paragraph, which the insurer accepted after one clarification call. A checkbox yes would have implied a current, comprehensive red-team programme that TRB did not have that year. When an incident later involved a payment-adjacent system, the written answer showed that ordinary tests had never claimed to cover it, which mattered more than looking assertive on the form.

### 19.11 Replacing a forbidden phrase

Assurance linter failed a report for "fully secure after remediation". Sam's replacement: "residual risk accepted for F3 until 1 December with compensating jump-only admin".

The forbidden phrase promised a state no test can prove. The replacement names the finding, the decision, the date and the compensating control. An owner can act on it, an auditor can check it and a later incident can be compared with it. Writing the specific sentence took longer than the slogan, and that is the point. Precision is the product.

### 19.12 Reading cannot-claim lines aloud

Catalogue cannot-claim lines are read aloud at kickoff; mumbling is corrected.

Reading aloud forces every person in the room to hear the limit, including sponsors who skip the written pack. Mumbling is corrected because a half-heard limit is how overclaims start. The practice feels slightly formal the first few times and then becomes normal. Kickoffs that skip it tend to produce the same clarifying arguments a week later, so the team treats the reading as part of starting the engagement, not as optional theatre.

### 19.13 Restarting a mumbled reading

Kickoff mumbling earns a restart of the cannot-claim read. Clarity over comfort.

A restart is mildly embarrassing and therefore effective. The reader slows down, the room pays attention and the limit is actually heard. Sam keeps the tone light. The goal is shared understanding, not punishment. After a few restarts early in the year, mumbled readings became rare, which is the outcome the rule exists to produce.

The restart also gives late arrivals a second chance to hear the limit. Kickoffs often start while someone is still joining the call, and a mumbled first reading is the one they would have caught. Waiting for a clean reading costs less than explaining the same boundary again mid-engagement.

### 19.14 Tracking mumbled kickoffs

Cannot-claim read restarts are logged as a fun metric of mumbling.

The log is a light-hearted count on the team wiki, not a performance score. A rising count would suggest that kickoffs are rushed or that new staff have not seen the practice. A falling count suggests the habit has stuck. Treating the metric as fun keeps it from becoming something people game by reading too quickly to avoid a restart. The useful signal is the trend across quarters, not any single kickoff.

### Worked example (synthetic TRB)

Sam's lecture note: "CBEST-style scenarios need intel + ROE + detection goals; our quarterly web test is narrower and still valuable."

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

A foundational case gives learners a closed world they can reason about without inventing facts. The packet contains only what the team would really have: a page of the rules of engagement, a slice of VPN and application logs, a draft finding and a short staff report that a password was reused. Nothing else is fair game. Learners must label what they know, what they guess and what they would do next, which trains the habit of not filling gaps with confident fiction. The same packet is reused across cohorts so facilitators can compare how different groups handle the same evidence.

### 20.2 Labels

Fact / Guess / Action lines.

Every statement in a case discussion is labelled as a Fact drawn from the packet, a Guess that goes beyond it, or an Action the team would take next. Facts can be checked against the packet. Guesses are allowed but capped, because an unlimited guess list becomes an attribution story. Actions must be ones the rules of engagement would permit. The labels slow the conversation down just enough to stop a room from sliding into unverified narrative. When two people disagree, they first check whether they are arguing about a Fact or a Guess.

### 20.3 Escalation

Possible payment integrity impact → same-day CISO.

Escalation criteria are written before the case starts, so urgency is not negotiated in the heat of discussion. At TRB, anything that could affect payment integrity, customer fund movement or the availability of online banking escalates to the CISO the same day, even if the evidence is still incomplete. The case packet includes a staff report of password reuse on a payments-adjacent jump host, which meets that bar. Learners practise writing the escalation note: what was observed, what is still unknown, what has been stopped and what decision is needed. Practising the note on a synthetic case makes the real one faster.

### 20.4 Out of scope

Personal email content stays untouched.

The staff report mentions that the reused password was also used for a personal mailbox. That detail is a temptation. Reading the personal mailbox might reveal more about the person, and it is outside every professional and legal boundary of the engagement. The case teaches the refusal explicitly. Learners may recommend that the staff member change personal passwords and may offer guidance, but they may not request or accept access to personal accounts. Writing that refusal into the Action lines is part of a passing case write-up.

### 20.5 ATT&CK

Tag techniques for SOC hunting.

When the case produces a finding, learners tag it with the ATT&CK techniques it demonstrates, such as Valid Accounts for the reused password on the jump host. The tags give the SOC a starting point for hunts: look for other logins with that account, or for lateral movement from that host after the login. Tags are not decoration. A finding without a technique tag is harder to turn into detection work. Facilitators check that tags match the evidence, not a favourite technique the learner wanted to mention.

### 20.6 Blameless

Focus on systems and process.

The staff member who reused a password made a mistake, and the useful questions are about the system that allowed that mistake to matter: was a shared admin password still in use, did the jump host accept password authentication, did leaver and rotator processes miss it. A blameless write-up names the person only as far as the packet requires and spends its energy on controls. Blame-centred write-ups produce defensive colleagues and unchanged systems. Facilitators redirect any Action line that starts with punishing someone toward an Action that changes a control.

### 20.7 Banning untimed drama

Facilitators ban timeline adjectives like "suddenly" unless a timestamp exists. Sam's case notes now lead with UTC times from logs, then narrative. Guess lines may not carry timestamps pretending to be facts.

Words such as suddenly, immediately and eventually smuggle a timeline into the story without evidence. A log line at 21:14 and another at 21:47 support a gap of thirty-three minutes. Suddenly supports whatever the speaker feels. Leading with timestamps forces the narrative to fit the evidence. A Guess about what happened in the gap stays a Guess, without a fake clock attached.

### 20.8 Stating the log timezone on page one

Every case packet states the timezone of log lines on page one. Sam lost an hour once to silent UTC; the cover line prevents it.

Log lines that look local and are actually UTC, or the reverse, create phantom gaps and overlapping events that send a team down the wrong path. The cover line is boring and non-negotiable: all timestamps in this packet are UTC, or all are America/New_York. When two log sources use different zones, both are stated and one is converted in a working note, never silently in someone's head.

### 20.9 A budget of three guesses

Each case may carry at most three Guess lines. Excess guesses become homework to gather facts.

Unlimited guessing turns a case into creative writing. Three guesses are enough to capture the most important uncertainties without letting the discussion live there. When a fourth guess appears, the facilitator asks what Fact would resolve it and assigns that as homework: which log, which owner, which query. The budget trains people to notice when they are inventing, and to prefer a small investigation over a large story.

### 20.10 Removing an unearned attribution

Case night: a Guess line about "APT29" is removed for lack of evidence. The room groans and then writes better Fact lines about VPN logs. Attribution theatre is addictive; the bell helps.

Naming a well-known actor feels like expertise. Without matching tooling, infrastructure or intelligence reporting in the packet, it is a Guess that steals attention from what the logs actually show. Removing it is unpopular for a minute and productive afterwards. The VPN Facts that replace it usually matter more for the bank's next action than any actor name would have.

### 20.11 Two facts instead of an APT guess

Guess budget forced a team to replace an APT guess with two VPN log facts. The case got less cinematic and more true.

The two Facts were that the account logged in from a new device fingerprint and that the same account then reached the jump host within four minutes. Those Facts support Actions: disable the account, review other logins from that device, check whether MFA was satisfied. The APT Guess supported only a feeling of importance. Less cinematic is the standard the bank needs when real money and real customers are involved.

### 20.12 ISO-8601 on the cover

Timestamp cover lines use ISO-8601 with offset; "morning" is banned.

Morning means different hours to different readers and disappears under timezones. An ISO-8601 timestamp with an offset, such as 2026-03-04T21:14:00Z, means one moment. The ban on vague time words applies to Guess and Action lines as well as Facts. If a learner does not know the time, they write that they do not know, which is itself useful information.

If a learner only knows that something happened in the morning, the Fact line says the time is unknown and the Guess line, if any, stays clearly separate. Pretending precision is worse than admitting a gap.

### 20.13 Checking cover lines in CI

ISO-8601 cover lines are validated by a regex in the case packet CI.

Packets live in a small repository. A continuous-integration check fails the build when page one lacks a line matching the timestamp pattern, or when banned words such as morning appear in Fact lines. The check is petty on purpose. Facilitators should spend their attention on reasoning quality, not on catching formatting drift. Automation handles the boring correctness.

When the check fails, the error message shows the expected cover-line pattern and the list of banned words, so authors can fix the packet without asking a facilitator.

### 20.14 Fact-line workshops

Fact-line workshops ban adjectives for twenty minutes. Only nouns, verbs, numbers and timestamps. The constraint feels artificial and produces the cleanest case packets of the term. Sam keeps a trophy packet from last year as the standard.

The constraint feels game-like and resets habits formed by thriller writing and incident movies. After twenty minutes the group usually produces a packet that a night-shift analyst could act on without asking what the adjectives meant. The trophy packet is reused as the bar for later cohorts.

### Worked example (synthetic TRB)

Sam escalates VPN password reused on personal email; resets TRB credentials; does not read personal mail.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX058 — Fact vs guess.** Label: "staff reported reuse" vs "nation-state has the hash". *Rubric:* 3 = fact vs guess; 2 = partial; 1 = both facts; 0 = none.
- **EX059 — Personal mail.** Why not read the staffer's personal email? *Rubric:* 3 = out of scope/privacy; 2 = partial; 1 = should; 0 = none.
- **EX060 — Escalate trigger.** What triggers same-day CISO escalation here? *Rubric:* 3 = credential reuse risking bank access/payments; 2 = partial; 1 = vague; 0 = none.

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

A system model for authorized testing is a map of what can be reached and what must be protected, not a full enterprise architecture. Actors are people or services that initiate actions: customers, staff, batch jobs, testers. Entry points are where those actors meet the system: the web app, the mobile API, the staff VPN. Stores hold data that matters: the customer database, the evidence vault. Trust zones group components that share a level of exposure. External processors sit outside TRB's control. Naming each element before testing stops the team from discovering mid-engagement that a forgotten batch peer can reach the ledger.

### 21.2 Entry points

Web, mobile API, staff VPN, batch peers.

Each entry point has different users, different authentication and different ways to go wrong. The public web app faces anyone on the internet. The mobile API may share backends with the web app but use different tokens. The staff VPN brings administrators close to internal systems. Batch peers are other institutions' systems that exchange files on a schedule. A model that lists only the web app will miss findings that appear only on the mobile API or only after VPN login. Sam checks the change ticket log for new entry points before each engagement.

### 21.3 Assumptions

"Staging mirrors prod AuthZ" must be validated.

Models are full of assumptions, and unvalidated ones are where findings hide. Teams often assume that staging uses the same authorization rules as production, that a mobile deep link reuses the web session checks, or that a callback from a payment processor is authenticated. Each assumption is written on a sticky and marked Open until someone checks it. An Open assumption at kickoff becomes a residual-risk sentence in the plan: the test may miss weaknesses that exist only where the assumption fails. Closing assumptions is part of preparation, not a side task.

### 21.4 Data flows

Customer PII paths drive minimisation.

The model marks every path that carries customer personal data: from the browser to the web tier, from the web tier to the customer store, from the store to a reporting extract. Those paths decide where minimisation rules apply during testing. A path that never carries personal data can be exercised more freely with synthetic traffic. A path that does carry it requires the proof-not-bulk rule and careful evidence handling. Drawing the paths also reveals surprises, such as a marketing site that posts into the core API and therefore into a personal-data store.

### 21.5 Exclusions

SWIFT gateway omitted when out of scope.

Exclusions must appear on the model as clearly as inclusions. Leaving the SWIFT gateway off the diagram entirely makes it look forgotten. Drawing it and marking it out of scope makes the boundary visible to everyone who uses the model. Testers who see an interesting path toward the gateway know immediately that it is not theirs to follow. The same discipline applies to third-party processors and to production customer databases when the engagement is limited to staging.

### 21.6 Living models

Update on new payment callback routes.

A model that is not updated becomes a hazard, because people trust it. TRB's rule is that any change ticket adding or changing an entry point, store or external callback must update the model within a week. Sam's weekly review diffs open change tickets against model edges and lists stragglers. The review is short and slightly annoying, which is why it works. Teams update the model to avoid appearing on the list, and the model stays close enough to reality to plan tests against.

### 21.7 Physical tokens for open assumptions

Owner workshops use physical tokens for assumptions. A token left in Open at the end blocks kickoff. The tactile rule sounds childish and works better than a spreadsheet column nobody updates.

Each Open assumption gets a token on the table. Closing it moves the token to a Closed bowl with a note of who checked and how. Tokens still in Open at the end of the workshop are photographed into the plan as residual risks, and the kickoff cannot be marked ready until the engagement lead accepts them. Spreadsheet columns invite polite neglect. A token on the table invites a decision.

### 21.8 Keeping payment callbacks on the model

New payment callbacks must appear on the model within one week of change tickets. Sam's weekly diff of change tickets versus model edges catches stragglers.

Payment callbacks are easy to miss because they are inbound from outside and often added by product teams under delivery pressure. A callback that is not on the model is also not in the flow register, which means it may have no owner and no agreed authentication check. The weekly diff is a simple join: change tickets mentioning callback, webhook or notify, versus edges on the model. Anything unmatched becomes a chore for the ticket owner before the next engagement.

### 21.9 Drawing processors as black boxes

Processors appear as black boxes with data types crossing the boundary, not as pretend internal hosts.

Drawing a vendor's internal servers invites testers to think about attacking them. Drawing a black box labelled SMS vendor with one-time codes outbound and delivery receipts inbound keeps attention on TRB's side of the boundary: are receipts validated, are failures handled, is the vendor authenticated. The data types on the arrows matter more than anything inside the box. They tell testers what personal data leaves TRB and what comes back that might be trusted too much.

### 21.10 A deep link becomes an open assumption

A new mobile deep link appears in a change ticket. Within three days Sam's model gains an entry point and an assumption sticky: "AuthZ same as web?". The sticky is still Open at kickoff and becomes a residual risk sentence.

The deep link could reuse the web authorization checks or it could have been wired up in a hurry with a weaker check. Nobody had validated which. Leaving the assumption Open was correct. The residual-risk sentence told everyone that mobile deep-link authorization was not covered by the planned web tests, which prevented a clean web report from being misread as clean mobile coverage.

### 21.11 A silent route from the marketing site

Callback inventory diff found a silent route from marketing site to core-api. It became a conduit review, not a marketing surprise in production.

The marketing site had been given a convenience endpoint to pre-fill application forms. The endpoint reached core-api and therefore the customer store, and it had never appeared on the architecture diagram. Finding it in a weekly diff meant the conduit could be reviewed, authenticated and rate-limited before an engagement or an attacker found it. Surprises are cheaper in inventory reviews than in production incidents.

### 21.12 Photographing open assumptions into the plan

Open assumption stickies are photographed into the ROE packet before kickoff.

A photograph freezes the workshop's state without depending on someone typing it up later. The image goes into the rules-of-engagement packet next to the residual-risk sentences, so anyone reading the authorization can see what was still unknown. After kickoff the stickies may be thrown away. The photograph remains. If a finding later turns on an assumption that was Open, the packet shows that the team knew the gap.

The photograph also settles disputes about what was said in the workshop. Memory differs; a picture of the stickies does not.

### 21.13 Open assumptions in the executive summary

Residual risk sentences from Open stickies are pasted into the executive summary draft automatically.

Executives rarely read assumption logs. They do read the executive summary. Pasting Open assumptions there, in one plain sentence each, means the people who accept residual risk see it before they accept the report. Automation matters because manual pasting is the step that gets skipped under deadline. The sentences are short on purpose: Mobile deep-link authorization was not validated against production rules.

If the automation fails, the engagement lead pastes the sentences by hand and files a ticket against the pipeline. The summary must still carry the risks.

### 21.14 Whiteboard to assumption log

Model office hours end with a photograph of the whiteboard and an OCR pass into the assumption log. Sticky notes that OCR cannot read are rewritten. Illegible assumptions are denied assumptions.

OCR errors are treated as Open assumptions until corrected, which motivates tidy handwriting. The photograph-plus-OCR path also means the workshop can stay analogue and collaborative while the lasting record stays searchable. Illegible notes cannot silently become Closed. A denied assumption cannot be treated as Closed in the plan, which keeps pressure on whoever owns the illegible note to rewrite it.

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

A dependency list for testing is the set of systems the target needs in order to behave normally. Online banking at TRB needs the core API, the ledger database, a fraud-scoring service, an SMS provider for one-time codes and a card processor for payment steps. If any of those is down or out of scope, parts of the application cannot be tested honestly. The list also shows where findings might really belong. A failure that looks like a banking-app bug may be a misconfigured fraud service. Sam confirms each dependency's owner and authorization status before kickoff.

### 22.2 Flow lab

lab_flows marks web→ledger-db UNAPPROVED.

The lab compares observed traffic with the approved flow register and prints any path that lacks an entry. A direct web-to-ledger path is the classic example: it skips the core API's authorization checks and gives a compromised web host a route into the database. Running the lab is not the finding. The finding is the unapproved path plus the missing change ticket and owner. Testers save the lab output beside the engagement record so that a later dispute about whether the path existed can be answered with a dated artefact.

### 22.3 Ownership

Each flow has a control owner.

Ownership answers who may approve a change, who receives a finding and who can stop a test that uses the flow. A flow with no owner cannot be safely tested, because nobody can accept the risk or fix what breaks. TRB's register rejects new flows without an owner field, and Sam's pre-engagement check lists any in-scope flows whose owner has left the bank. Replacing a departed owner is a planning task, not a mid-window surprise. Findings filed against unowned flows tend to sit untouched, which is another reason ownership is required up front.

### 22.4 Third parties

Separate authorization.

Dependencies that belong to other companies need those companies' permission before anyone probes them. TRB's authorization covers TRB systems. The SMS vendor, the card processor and the cloud host each have their own rules. Sam can observe how TRB calls them and whether TRB validates their responses, which tests TRB's code. He cannot run vulnerability scans against their endpoints unless their programmes say so. The distinction is written into the method cards so that a curious tester does not improvise.

### 22.5 Breaks

Vendor outages are stops, not hammering opportunities.

When a dependency is failing, continuing to send traffic rarely produces useful security evidence and often makes the outage worse. The rules of engagement treat a confirmed vendor outage as a stop condition for methods that need that vendor. Sam records the outage, notifies the engagement lead and moves to methods that do not depend on the broken path. Hammering a down service to see how it fails is a denial-of-service test in disguise and is forbidden unless the ROE explicitly allows it in a dedicated window.

### 22.6 Secrets

API keys in repos are TRB findings.

An API key committed to a source repository is a credential in every clone, every backup and often every continuous-integration log. Even after the key is removed from the latest commit, history still holds it. Sam's findings for keys in repos recommend rotating the key, removing it from history where feasible, adding a secret scanner to the pipeline and recording an owner for the new secret in the vault. The finding severity depends on what the key unlocks. A read-only analytics key differs from a key that can move money.

### 22.7 Expiring temporary flows

Kill-dates on temporary flows page both the owner and Sam three days prior. If nobody responds, TrackScope marks the flow expired and denies tests that relied on it until renewed in writing.

Temporary flows without expiry become permanent. The page and the automatic expiry turn temporary into a real time limit. Denying tests that used the expired flow is deliberate. It stops an engagement from quietly relying on a path the bank no longer meant to keep, and it forces a written renewal that restates the business reason.

### 22.8 Scanning TRB-owned repositories

Repo secret scans run on TRB-owned code listed in ROE. Sam opens findings for keys with no owner in the asset model.

The scan covers only repositories the engagement is authorized to examine. Findings distinguish keys that already have vault owners from keys that appear to be orphans. An orphaned key is urgent because nobody is rotating it. Linking each finding to the asset model also shows when a key belongs to a system outside scope, in which case Sam reports it to the system owner without testing further.

### 22.9 Renewals need a reason

Pages for kill-dates include the original business reason. Renewals without reasons are denied.

A renewal that says extend three months teaches nothing and invites eternal temporary rules. Requiring the original reason, and a sentence on why it still applies, makes the owner notice when the project that needed the flow has finished. Denied renewals appear in a weekly list that Sam reviews with the architecture owner. Patterns of denial often point to a project that should either finish or accept a permanent, reviewed conduit.

### 22.10 When the primary owner is on leave

Kill-date pages fire; the owner is on leave. Backup owner renews with a reason. Sam notes the backup-owner field as mandatory going forward — single-owner expiry pages are fragile.

A control that depends on one person being at their desk fails during holidays and illness. The backup owner had already been briefed on the flow's purpose, so the renewal took minutes. Making the backup field mandatory means the next temporary flow cannot be created until two people can speak for it. Fragility removed at registration time does not have to be discovered during a page storm.

### 22.11 A renewal that made risk visible

Expiry without reason was denied; the owner wrote "PCI segmentation project delay". Now the risk is visible, not eternal.

The sentence did two jobs. It renewed the flow for a bounded time, and it told anyone reading the register why a risky path still existed. Project delays are real; unspoken delays become folklore. When the segmentation project later finished, the same register entry made it obvious that the flow's reason was gone and the kill-date should not be renewed again.

### 22.12 Backup owners must acknowledge

Backup owners must acknowledge in the ticket UI; silence is not acceptance.

Listing someone as backup without their acknowledgement creates a false sense of coverage. The UI requires a click that records the person, the time and the flow. Until that click happens, the temporary flow cannot be approved. The rule has slowed a few registrations and prevented several quiet gaps where the named backup had never heard of the flow.

Backup names written on a ticket without a click disappear when that person changes teams. The acknowledgement click is what turns a name into a duty.

### 22.13 Blocking closeout without a backup

Mandatory backup-owner fields block ticket closeout. Sam loves blocking closeout.

Change tickets that open temporary flows cannot close until the backup acknowledgement exists. Blocking closeout is more reliable than sending reminders, because delivery pressure already focuses on closing tickets. The block is visible in the same place project managers already look. Sam's preference for blocks over reminders comes from watching reminder-based processes fail whenever the team is busy.

Delivery pressure dissolves hallway agreements. The block forces the named backup owner to acknowledge the flow before the change ticket can close, which is the control.

### 22.14 Postmortems for expired flows

Flow expiry postmortems ask whether the original business reason still exists. If the project finished, the flow dies. If the project continues, a new kill-date is mandatory. Eternal temporary rules are renamed findings in the postmortem notes.

The postmortem is short: reason, outcome, next kill-date or deletion. Renaming eternal temporary rules as findings makes the pattern visible to the same people who see other risk. A flow that survives every postmortem without a living reason is a process failure, not a networking necessity. Writing the postmortem the week a flow expires, not months later, keeps the business reason honest.

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

A method card is the unit of authorized testing work. It states why the method is being run, which clause of the rules of engagement permits it, which tool and settings will be used, what conditions stop the method and what evidence it must produce. Cards stop improvisation. A tester who wants to try something not on a card must propose a new card and get it into the frozen set, or wait for a rules amendment. TrackScope schedules cards, not free-form activity.

### 23.2 WSTG

Select auth, session, access control themes for online banking staging.

OWASP's Web Security Testing Guide catalogues many test ideas. TRB does not run all of them every engagement. For online banking staging the priority themes are authentication, session management and access control, because failures there move customer data or money. Other themes appear when threat reporting or recent changes justify them. Selecting themes in the plan makes the engagement's depth honest. A report that claims broad web coverage after running only three themes would mislead.

### 23.3 Rates

Caps protect availability.

Even authorized tests can knock a service over if they send too much traffic. Method cards include rate caps: requests per second, concurrent sessions, total identities tried. The caps are set with the service owner and the SOC, who know what normal looks like. Exceeding a cap is a stop condition, not a suggestion. Sam would rather finish a method slowly across two evenings than explain an outage caused by a test that was supposed to be careful.

### 23.4 Forbidden

Spraying and DoS remain forbidden.

Password spraying across many accounts and denial-of-service testing are excluded from ordinary TRB windows because their impact is hard to contain and their authorization bar is higher. A tester who discovers that spraying would be interesting still does not do it. They write a note that the method was considered and excluded, which can become a recommendation for a separate, carefully scoped exercise if the risk warrants it. Forbidden means forbidden, not forbidden unless curious.

### 23.5 Quiet vs noisy

Prefer quiet methods when detection is also under test.

Some methods produce little log noise; others flood the SOC with alerts. When the engagement is also measuring detection, noisy methods drown the signal the SOC needs to show. Quiet methods first let the SOC demonstrate what they catch under realistic conditions. Noisy inventory scrapes belong on separate days, with a noise budget the SOC has signed. Mixing them once produced an alert blizzard that taught nothing about either detection or the inventory.

### 23.6 Freeze

Method set freezes after kickoff unless ROE amends.

After kickoff the scheduled cards are fixed. Adding a method mid-window would bypass the review that checked scope, rate limits and stop conditions. If a new method becomes necessary, the rules of engagement are amended in writing and the freeze lifts for that amendment only. The freeze frustrates improvisers and protects everyone else. Clients cannot claim they were surprised by a method that was not on the kickoff list, and testers cannot claim they thought an improvised method was allowed.

### 23.7 Separating quiet and noisy days

Quiet methods are preferred during purple windows so SOC signal is interpretable. Sam schedules noisy inventory scrapes on separate days. Mixing them produced a useless alert blizzard once; the calendar now prevents it.

The calendar block is shared with the SOC. A purple-team day shows quiet cards only. An inventory day shows noisy cards and a higher noise budget. Automatic checks refuse to schedule a noisy card onto a purple day. The blizzard taught the team that calendar design is part of method design.

### 23.8 Every card needs an owner

Each method card has an owner engineer. Unowned cards cannot be scheduled. Sam claims ownership before proposing a card in kickoff.

Ownership means someone keeps the card's ROE clause, tool versions and stop conditions current. Unowned cards rot: they cite retired clauses or settings that no longer match the platform. Refusing to schedule them makes ownership a practical requirement rather than a polite field. Claiming ownership before kickoff also means the proposer is volunteering to maintain the card, which reduces drive-by suggestions.

### 23.9 SOC noise budgets

SOC signs a noise budget per window. Exceeding it is a stop condition Sam respects immediately.

The budget is a number of alerts per hour, usually, plus a list of alert types that count. The SOC signs it because they know their staffing and their other work that night. When TrackScope or the SOC says the budget is exhausted, Sam stops noisy cards even if the window has hours left. Immediate respect for the stop builds trust. A tester who negotiates past a SOC stop once will find the next budget conversation much harder.

### 23.10 Splitting a card to fit the budget

SOC noise budget is 30 alerts per hour. Sam's method card would generate about 80. He splits the card across two days. The SOC lead buys him coffee; the window stays green.

Splitting preserved the testing goal and the SOC's ability to respond. The card's evidence requirements were met across both days, with clear labels so nobody thought the method had been abandoned. Coffee is optional. A green window, meaning no emergency caused by testing, is the real reward and the reason budgets exist.

### 23.11 Treating SOC signatures like CISO signatures

Noise budget sheet is signed like a mini-ROE. Sam treats SOC signatures with the same respect as CISO signatures.

The SOC does not own the overall authorization, but they own the detection environment the test will disturb. Their signature on the noise budget is authorization for that disturbance. Ignoring it would be ignoring a boundary as real as an excluded host. Sam's habit of equal respect also encourages the SOC to sign promptly, because they know the signature will be honoured rather than bargained away.

### 23.12 Automatic pause on overrun

Noise budget overruns trigger an automatic method-card pause flag in TrackScope.

Automation removes the awkward conversation in which a tester argues that just a few more requests will finish the card. The platform counts alerts attributed to the engagement, and when the budget is reached it pauses noisy cards and notifies Sam and the SOC. Finishing then requires a SOC countersignature for an extension, not a unilateral decision. The flag has stopped several polite overruns that would have become impolite outages.

### 23.13 Testers cannot clear their own pause

Pause flags clear only with SOC countersign. Sam cannot clear his own noise overrun.

Self-clearing would make the automatic pause theatre. The SOC countersign is a second person asserting that the environment can take more load. Sometimes they refuse and ask for a quieter continuation tomorrow. That refusal is a successful control. Recording who cleared a pause, and when, also helps later reviews understand why a noisy card continued after an overrun.

When the SOC analyst clears a flag, TrackScope stores their name, the alert count at the moment of clearing and the new budget on the card itself. The next card audit can then compare that extension with the alerts PulseMap attributed to the engagement afterwards.

### 23.14 Rotating card audits

Method card librarianship is a rotating duty. Each month a different engineer audits five cards for ROE clause drift. Sam's audit found a card citing a retired ROE section; it was suspended in an hour.

A retired ROE clause on a live card is a quiet authorization bug. The monthly audit catches a few each year, usually after a rules rewrite. Suspending the card immediately prevents anyone from scheduling work under a clause that no longer exists. The rotating duty spreads familiarity with the library across the team. Publishing which five cards were audited each month makes the rotation visible and harder to skip.

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

A control recommendation must match the weakness it answers. Shared administrator passwords are fixed by named accounts and a vault, not by a longer password policy. An unapproved network path is fixed by removing the firewall rule and denying the path in the application, not by adding monitoring alone. Weak MFA enrolment is fixed in the enrolment flow. Mismatched recommendations waste fixer time and leave the original path open. Sam's review of draft findings checks that each recommended control would actually close the demonstrated path.

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

The product of likelihood and impact is a simple ranking aid, not a law of nature. Ties break by finding id so that the order is reproducible. F1, F3 and F4 all score six and outrank F2's three, which matches the intuition that a shared admin password, a direct web-to-ledger path and a weak MFA enrolment check matter more than verbose error pages. The lab's job is to make the ranking visible before personalities enter the discussion. Once scores are on the table, arguing to demote a finding becomes a visible risk-acceptance decision rather than a quiet reordering.

### 24.3 Compensating

Jump-only admin while passwords uniqued.

A compensating control reduces risk while the lasting fix is unfinished. If shared admin passwords still exist, restricting administration to the jump host with multi-factor authentication shrinks who can use those passwords and makes their use auditable. Compensation is dated. The finding stays open with a due date for unique passwords, and the compensating control is listed beside it so nobody mistakes the jump-host rule for the complete fix. When the lasting fix lands, the compensation can be retired or kept as defence in depth.

### 24.4 Ownership

Every control has a named owner and date.

A control without an owner is a sentence in a report. The owner is the person who will implement or operate it, and the date is when it will be in place or next reviewed. TrackScope refuses to mark a finding as accepted-with-control unless both fields are filled. Ownership also prevents orphaned compensations. When the person who set up jump-only admin leaves, the dated owner field shows who must pick up the control or the finding reopens.

### 24.5 Verify later

Chapter 30 retests.

Declaring a control implemented is not the same as showing it works. Retests close that gap. After the owner says named accounts replaced the shared admin password, Sam schedules a retest that tries the old password and checks that administration still requires the jump host. Failed retests reopen the finding automatically. The retest date is part of the control's record, so a control that has never been retested is visible on PulseMap as unverified. A retest is planned with the same account, the same source network and the same request that proved the weakness, so a pass means the path is closed rather than that the tester tried something easier.

### 24.6 Overclaim

Do not call a control "prevents all APT".

Controls reduce specific paths. Naming a sophisticated actor or promising total prevention turns a precise finding into marketing. Sam's report language names the path closed, the conditions of the test and the residual risk. A sentence such as administration from the user VLAN to staging servers is blocked pending unique passwords is usable. A sentence such as this prevents advanced persistent threats is not. The assurance linter flags the second kind of phrase before the report leaves draft.

### 24.7 Freezing scores before discussion

Ranking meetings freeze scores before discussion of personalities. Sam collects scores silently, then reveals. Lobbying to demote a finding because a team is "busy" happens after scores, where it is visible as risk acceptance.

Silent scoring stops the first loud voice from anchoring everyone else. Revealing afterwards lets busy-ness be discussed honestly as a reason to accept risk for a time, with a signature and an expiry, rather than as a reason to pretend the finding scored lower. The difference is whether the bank's record shows the trade-off.

### 24.8 Written risk acceptance

Risk acceptance uses a form with amount, expiry and CISO signature. Verbal "we'll live with it" does not close F3.

Verbal acceptance evaporates when staff change or when an incident makes everyone forget who agreed. The form records what is accepted, until when and by whom. PulseMap shows accepted-with-expiry findings in amber, not green, so they do not disappear from attention. When the expiry arrives without a fix or a renewal, the finding reopens. That mechanism is the reason F3 cannot be closed with a hallway conversation.

### 24.9 Revealing scores only after everyone submits

Scores display only after all raters submit. Sam's facilitation script blocks early reveals.

Early reveals let later raters adjust toward the group, which defeats independent judgement. The facilitation script is a checklist Sam reads: confirm every rater has submitted, then show the table. TrackScope enforces the same rule for remote meetings by hiding the aggregate until the last ballot arrives. Blocking early reveals has occasionally delayed a meeting by five minutes and has regularly prevented a senior voice from setting the score.

### 24.10 A hygiene track for easy fixes

Rank reveal shows F2 last. The web team still wants F2 fixed first because it is easy. Sam records easy-but-low as a separate "hygiene" track so it does not displace F3's funding.

Easy fixes are worth doing. They are not worth starving higher-ranked work. The hygiene track has its own small capacity and its own WIP limit, so the web team can clear verbose error pages without taking engineers off the ledger-path fix. Keeping the tracks separate also keeps reporting honest: hygiene throughput is not presented as progress on high-risk findings.

### 24.11 Parallel tracks protect hard work

Hygiene track fixed F2 in three days without stealing the F3 budget meeting. Parallel tracks keep easy work from starving hard work.

Before the split, every easy finding competed for the same meeting slot as F3, and easy usually won because it promised a quick win. After the split, F3 kept its funding conversation and F2 still got fixed. The pattern generalises. Whenever low-severity work consistently displaces high-severity work, the fix is a separate capacity allocation, not a lecture about priorities.

### 24.12 WIP limits on hygiene

Hygiene track WIP limits keep it from becoming a dumping ground for ignored risk.

Without a limit, every uncomfortable finding gets relabelled as hygiene and the track becomes a second backlog of ignored risk. The limit forces a choice: finish something before starting more. Findings that do not fit must either wait, earn a place on the main ranked list or be accepted with an expiry. The WIP limit is a control on the process that claims to help. A finding moved to hygiene must still carry its original score, so anyone reviewing the track can see whether a high-risk item has been disguised as a tidy-up.

### 24.13 A hard WIP of three

Hygiene WIP limit is three. Fourth easy fix waits. Focus is a control.

Three is small enough that the team feels the constraint and large enough that real hygiene work continues. When a fourth easy fix appears, it waits visibly on the board. Waiting is uncomfortable and useful. It stops the quiet accumulation of half-finished tidy-ups and keeps the hygiene track's promise of speed from turning into another infinite queue. The limit is reviewed each quarter. If items wait longer than a month, the team either raises capacity or admits that some hygiene work will not be done and records that decision.

### 24.14 Ninety-second covers for funding boards

Funding boards receive ranked lists with a one-page plain-language cover. Sam practices the cover aloud until he can deliver it in ninety seconds. Boards remember the cover longer than the appendix.

Practising aloud catches jargon the appendix can keep and the cover cannot. Boards that remember the cover ask better questions about the ranked list. Boards that receive only the appendix often remember nothing but the total count of findings, which is the least useful number in the pack. The appendix still matters for the engineers who will do the work, so the cover always ends with a pointer to the ranked table and its scoring rubric.

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

The laboratory notebook is the evidence that the learner ran the tools, not that they read about them. Each required output is pasted or attached with the learner's initials and the time. Initials matter because shared screenshots circulate. A notebook without outputs fails regardless of how polished the prose is. Supervisors check that the pasted numbers match what the pinned script versions produce, which is why script hashes appear later in the chapter.

### 25.2 Peer check

Compare scope classifications.

After running lab_scope, learners swap notebooks and re-classify the same target list without looking at each other's answers. Disagreements are discussed against the written scope file, not against memory. The peer check catches systematic misreadings, such as treating the SWIFT exclusion as optional, and it trains the habit of having a second person confirm scope decisions before a real window. A clean peer check is part of the lab's pass criteria. When peers still disagree after reading the file, the supervisor rules and the ambiguous line is sent to the scope author as a drafting fix.

### 25.3 Planted fault

Refuse mismatched hash evidence.

One evidence file in the lab pack has a hash that does not match the accompanying note. Learners who file it anyway fail that station. The point is emotional as well as technical. Refusing evidence feels like slowing down, and in a timed lab that pressure is deliberate. The correct action is to stop, record the mismatch and request a fresh capture. Transferring that refusal into real engagements is the habit the station exists to build.

### 25.4 Time box

Two hours hard stop.

Real windows end. The lab ends too, even if a station is unfinished. Learners practise writing what they completed, what they did not and what they would do next, which is the same discipline Sam uses when a testing night runs out of time. Extending the lab for struggling learners would teach the wrong lesson. Time boxes also keep peer checks fair: everyone has the same clock. Supervisors grade the hand-off note as seriously as the completed stations, because an honest list of unfinished work is what lets a colleague resume safely the next night.

### 25.5 No production

Live TRB scanning fails the lab.

The lab environment uses documentation-range addresses and synthetic data. Any attempt to point tools at live TRB systems, even out of enthusiasm, is an automatic fail and a conversation with the supervisor. The rule protects the bank and the learner. Authorization for the lab is authorization for the lab. Curiosity about production belongs in a planned engagement with a signed scope, not in a classroom exercise. The lab network has no route to TRB ranges, so the rule is also enforced technically, and any blocked attempt appears in the lab firewall log the supervisor reviews.

### 25.6 Sign-off

Supervisor signs on discipline, not novelty.

A passing lab shows careful scope checks, honest hashing, completed notebooks and respect for stops. Fancy extra techniques that were not asked for do not raise the grade, and they can lower it if they violate a rule. Supervisors sign a short rubric: scope correct, hash refusal demonstrated, outputs present, no production contact. Novelty is welcome in later research chapters. Laboratory I rewards discipline. A learner who finished every station but filed the mismatched evidence does not pass, while one who refused it and ran out of time on a later station usually does.

### 25.7 The missing SWIFT exclusion

Lab I planted faults include a scope file with SWIFT removed from exclusions. Learners who do not notice fail. Sam failed that variant once as a student and now writes exclusions first every time.

The variant works because learners often check that in-scope ranges look right and forget to check that exclusions are still present. Sam's lasting habit from failing it is to read the exclusion list before the inclusion list. The lab keeps the variant because the failure is cheap in a classroom and expensive in a real window.

### 25.8 Pinning lab script versions

Lab notebooks include hashes of the lab scripts used. Version skew is a common excuse Sam removes by pinning hashes.

Without hashes, a learner whose numbers differ from the key can claim they ran a different script version, and the supervisor cannot easily check. With hashes, the notebook shows exactly which bytes ran. Pinning also protects learners. If the lab maintainers change a script mid-term, the hash mismatch explains a surprise result instead of looking like learner error. The hash list sits at the top of the notebook, and the supervisor's first check is to recompute one hash before reading any results.

### 25.9 Rotating planted variants

The planted scope variant is rotated so word cannot spread between sittings. Sam keeps three variants.

If every sitting saw the same missing SWIFT line, the afternoon cohort would hear about it at lunch. Three variants keep the peer check honest: missing exclusion, renamed exclusion and exclusion only in an appendix. Learners are told that variants exist, so memorising one answer is obviously useless. Facilitators draw the variant from a sealed envelope at the start of each sitting. Variants differ only in where the exclusion problem hides, so every learner faces the same skill under a different disguise and grades stay comparable.

### 25.10 Exclusions by asset id

Lab I variant B hides an exclusion by renaming SWIFT to "pay-gw-01". Learners who only string-search "SWIFT" fail. Sam teaches exclusion by asset id, not by marketing name.

Real inventories rename things. A gateway that staff call SWIFT may appear in the asset register under a hostname. Checking exclusions by the names people use in conversation misses those rows. The lab's renamed variant makes that failure mode personal. Learners who pass it leave with a habit of matching asset identifiers, not slogans.

### 25.11 Exclusions hiding in appendices

Variant C uses an exclusion listed only in an appendix table. Learners who skip appendices fail. Sam loves appendix discipline.

Scope documents bury important rows in appendices more often than anyone admits. Variant C is slightly cruel and very realistic. The fix is a reading order: cover page, exclusion appendix, then inclusion ranges. Learners who adopt that order stop failing C and stop missing exclusions in real rules of engagement. The appendix variant also teaches that a scope document's structure is part of its meaning; a table at the back can carry as much authority as the cover page.

### 25.12 Laminated asset-id reminders

Asset-id exclusions are printed on the lab desk laminated card.

The card lists the three identifiers that must appear in every scope check for the lab's fictional bank. It is a scaffold for the habit, not a substitute for reading the scope file. Learners may use it during Laboratory I and are expected to work without it in later labs. Lamination survives spilled coffee, which is a more common lab hazard than instructors admit. Learners record in the notebook whether they used the card, which lets supervisors see who is ready to drop the scaffold.

### 25.13 Voiding old laminated cards

Laminated cards are versioned; old cards are hole-punched as void.

An outdated card is worse than no card, because learners trust it. When asset identifiers change, new cards are issued and old ones are hole-punched so they cannot be reused at a glance. The version number on the card matches the lab pack version. Facilitators check the match before each sitting as part of opening the room. The void cards go into a box on the facilitator's desk, which doubles as a quick history of how often the lab's identifiers changed.

### 25.14 Showing a real failed notebook

Laboratory I briefings show a failed notebook from a prior year (with permission) where hashing was skipped. Seeing a real fail is more persuasive than a rubric bullet. Sam thanks the alumnus who allowed the anonymised share.

Permission and anonymisation are mandatory; the point is the missing hash, not the person. Learners who see the fail ask better questions about their own notebooks. Rubric bullets describe the standard. A real miss makes the standard felt. Each new cohort sees a different anonymised failure where possible, so the example does not become a familiar story everyone tunes out.

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

A chain is a sequence of allowed steps that together show how a low-privilege foothold can reach a higher-value asset. At Riverstone Transit Bank every link must already be permitted by the rules of engagement; inventing a new hop mid-engagement is out of bounds. The operator stops the moment an impact is proven, because further pivots add risk without adding evidence for the finding. Sam Ito keeps a short list of approved transitions on the method card so a late-night session cannot invent a creative shortcut that nobody signed. Chains that look impressive but rest on an unapproved step are discarded, not celebrated.

### 26.2 Minimum proof

No extra pivoting "for fun".

Minimum proof means the smallest set of steps that demonstrates the weakness with enough detail for the owner to reproduce it. Extra pivoting after that point is curiosity dressed as thoroughness, and it often expands blast radius without changing the finding. TrackScope records the proof steps; anything beyond them needs a new ticket and a fresh approval. Sam once stopped a junior who wanted to "just see" whether domain admin was reachable after a cross-user read was already on film. The junior's restraint became part of the coaching note, which is more useful than another screenshot of a shell.

### 26.3 Documentation

Chain diagram in appendix with times.

Every accepted chain ships with a diagram that names each hop, the asset identifiers from FindingsDesk, and the wall-clock time of each transition. Freehand hostnames once broke an appendix link and cost a day of repair; shared ids keep the appendix mechanically checkable. Times matter because detection goals ask whether the SOC saw the stages, and a diagram without clocks cannot answer that. Sam pastes the diagram into the engagement appendix before he files the finding, not after the debrief, so reviewers never chase a missing figure. The diagram is evidence, not decoration.

### 26.4 Detection goals

Note whether SOC saw stages — purple synergy.

Detection goals turn a red-team chain into purple-team feedback. For each stage Sam records whether PulseMap or the SOC console showed a hit, a miss or an unknown. Unknown is allowed only when no sensor covers that hop, and that gap itself becomes a backlog item. The note is short: technique id, stage name, seen or not, and a pointer to the log source that should have caught it. Purple synergy here is not a joint meeting; it is a habit of leaving the detection team something actionable instead of a victory lap.

### 26.5 Payment adjacency

Extra approvals before anything payment-near.

Anything that touches payment-adjacent systems at TRB needs a second signature before the chain continues. Payment adjacency includes the SWIFT gateway perimeter, settlement queues and the jump hosts that can reach them, even when the gateway itself stays out of scope. Sam treats "near" as a property of network path and shared credentials, not of the finding title. If a hop would land on a host that can talk to those queues, he pauses, files the request and waits. Skipping the pause once would be enough to end the engagement and the internship.

### 26.6 No exploit kit

Course still provides no exploit development.

The coursework teaches chaining with published weaknesses and approved tooling; it does not teach writing new exploits. Learners who ask for a kit are pointed back to the method cards and the impact catalogue. That boundary keeps the classroom honest about what a bank will authorize and what a university programme can safely supervise. Sam's own kits are limited to the pinned scripts whose hashes sit in the lab notebook. Building a custom payload for a graded chain is a fail, even if the payload would have worked.

### 26.7 Asset ids in diagrams

Chain diagrams use the same asset ids as FindingsDesk. Freehand hostnames caused a broken link in an appendix once; ids made the appendix mechanically checkable.

FindingsDesk assigns a stable identifier to every in-scope host and service. Diagrams that reuse those ids can be validated by a script that walks the appendix and confirms each box still exists in the inventory. When Sam used a nickname for a jump host, the appendix checker failed and the finding sat in review until the diagram was redrawn. The lesson stuck: pretty labels belong in the prose caption, not in the graph nodes. Juniors now copy ids from the inventory pane rather than typing from memory.

### 26.8 Impact catalogue

Allowed impact proofs for chains are catalogued (cross-user read, config change). "Domain admin" is not an allowed classroom impact at TRB.

The impact catalogue is a short, signed list of proofs the classroom will accept. Cross-user read of a non-sensitive record and a reversible configuration change are on it; seizing domain admin, encrypting files or touching live payments are not. The catalogue exists so Sam does not have to invent the boundary under pressure. When a chain could continue toward a forbidden impact, the operator stops and files what is already proven. Ambition that exceeds the catalogue is redirected into a detection goal or a remediation note, not into a riskier hop.

### 26.9 Stop-on-impact banner

Method cards show a banner "stop when impact proven". Sam measures average steps after impact; fewer is better.

The banner sits at the top of every method card so it is the first line an operator sees when the card is open. Sam tracks how many actions people take after the impact screenshot is already saved. A falling average means the culture is working; a rising average triggers a coaching huddle. The metric is deliberately simple because complicated dashboards invite gaming. Operators who stop cleanly get credited in the engagement summary, which makes restraint visible to the people who write performance notes.

### 26.10 Stop after cross-user read

After impact proof on cross-user read, Sam's next action is stop, not pivot to admin. His chain appendix's last box is green "STOP — impact shown". Juniors copy the box into their cards.

The scene is the moment everyone remembers: the cross-user read is on screen, the finding draft already names the path, and the temptation to keep going is loud. Sam closes the session, pastes the green STOP box as the final node and archives the notebook. Juniors who watched him do it once start pasting the same box on their own cards. The ritual is small, but it turns an abstract rule into a habit people can imitate under fatigue.

### 26.11 No ransomware simulations

Impact catalogue forbids ransomware simulation on bank networks in coursework. Someone always asks; the catalogue answers before Sam must.

Learners who come from capture-the-flag culture often assume encryption demos are fair game. At TRB they are not, even in the lab ranges that mirror production naming. The catalogue states the ban in one line so Sam can point at paper instead of arguing taste. Questions about "what if we only encrypt a test share" still get a no, because the classroom cannot afford a story that sounds like ransomware to an auditor. Safer impact proofs already teach the same privilege questions without that theatre.

### 26.12 Green means restraint

STOP boxes are green on purpose — restraint is success, not failure.

Red usually marks danger; here green marks the successful end of a chain. The colour choice is deliberate pedagogy: stopping is the outcome the programme rewards. Sam explains it once to each cohort and then lets the stickers do the talking. When a visitor asks why the last box is not red, an operator can answer without calling the supervisor. Colour coding that fights the culture fails; colour coding that matches the culture sticks.

### 26.13 STOP stickers

Green STOP boxes are stickers juniors put on printed cards. Culture is tactile.

Printed method cards still circulate in the jump room because screens go dark and paper does not. Juniors peel a green STOP sticker onto the card the first time they complete a chain under supervision. The sticker is slightly ridiculous and that is the point: it makes the rule memorable and gives peers something to notice during reviews. Sam keeps a spare sheet in the drawer next to the badge printer. When the sheet runs out, someone has been practicing, which is a good problem.

### 26.14 Impact-then-stop posters

Chain ethics posters hang in the jump room: "Impact then stop". Visitors sometimes laugh; operators do not. Sam watches new contractors read the poster before their first chain.

The poster is not ironic decoration. Contractors who skim it and joke about it still get a verbal brief, but Sam notes who paused long enough to read. People who treat the slogan as a joke tend to be the ones who ask for one more hop after proof. The jump room is where habits form, so the wall carries the same message as the method cards and the catalogue. Consistency across paper, screen and conversation is how the rule survives shift changes.

### Worked example (synthetic TRB)

Sam chains unapproved flow + weak session control to show cross-user read risk, then stops.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX076 — Minimum proof.** What does minimum proof mean? *Rubric:* 3 = stop once impact shown; no extra pivot; 2 = partial; 1 = full takeover always; 0 = none.
- **EX077 — Payment-near.** What extra step before payment-adjacent tests? *Rubric:* 3 = extra approvals/ROE check; 2 = partial; 1 = vague; 0 = none.
- **EX078 — Chain doc.** What belongs in the chain appendix? *Rubric:* 3 = steps/times/evidence links; 2 = partial; 1 = vague; 0 = none.

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

A retest repeats the original proof steps inside a window the owner and the tester both accepted when the finding was filed. Changing the method mid-retest makes a FIXED claim dishonest, because the owner may have patched only the path that was demonstrated. Sam books the window when the finding lands, usually about two weeks out, so the calendar does not wait for panic. If the build under test has drifted, the retest records that drift instead of inventing a pass. The point of the exercise is truth about closure, not a green checkbox.

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

The lab walks a short list of synthetic purple-team runs and prints how often each technique was detected. Learners read the printed ratios before they argue about tooling. A technique that never hits is a gap story, not a reason to declare the SOC broken. Sam's coaching focuses on framing: small samples can still justify instrumentation when the log source already exists. Students who only celebrate high hit rates miss the engineering value of an honest miss.

### 27.3 Closure

FIXED with evidence or accepted risk signed.

Closure is either a FIXED status backed by a retest transcript or an accepted-risk signature from someone with authority to own the residual. Anything else leaves the ticket open. Sam refuses to mark FIXED from a verbal "we patched it" without the same request that proved the issue. Accepted risk is not a soft fail; it is a documented decision with an expiry and an owner. FindingsDesk will not let a ticket disappear into a vague "monitoring" state without one of those two endings.

### 27.4 Partial

STILL OPEN keeps ticket alive.

When a retest shows the path is narrowed but not closed, the status stays STILL OPEN and the ticket remains on the owner's queue. Partial progress is recorded in the notes so nobody pretends the work never happened, but progress is not closure. Sam once saw a team celebrate a WAF rule that blocked his old payload while a one-character variant still worked; the ticket stayed open and the celebration moved to the next patch. Honesty about partial states keeps leadership from declaring victory on a dashboard that lies.

### 27.5 Scope freeze

No new hunt on retest day.

Retest day is for verifying known findings, not for opening a fresh hunt. New leads go into a parking note for the next engagement window. The freeze protects the owner's change window and keeps the evidence file coherent. Sam has watched retests turn into sprawling discovery days that produced neither a clean FIXED nor a clean STILL OPEN. The rule is posted on the retest calendar invite so nobody claims they were surprised. If a critical new lead appears anyway, it becomes a separate emergency ticket with its own approvals rather than hitchhiking on the retest.

### 27.6 Communicate

Same-day owner note.

After a retest, the owner receives a same-day note that states FIXED, STILL OPEN or accepted-risk pending, with a link to the transcript. Waiting until the weekly report creates rumours and duplicate work. Sam writes the note before he shuts the laptop, even when the news is disappointing. The note names the method card hash so the owner can confirm the same build was tested. Speed here is courtesy, not pressure. A late note forces the owner to ask peers what happened, which is how incorrect status stories start.

### 27.7 GAP stories for SOC

GAP stories offered to SOC include log source, technique and a sample detection idea — not a demand to "buy a tool". Sam's T1190 note pointed at WAF and origin logs already licensed.

A useful gap story tells the SOC what to look at with what they already own. Sam's T1190 write-up named the WAF bypass logs and the origin access logs, both already licensed, and sketched a detection idea that used those fields. Demanding a new product in a gap note usually stalls the conversation. Detection engineers respond faster when the ask is concrete and cheap. The backlog item that followed cited Sam's note verbatim.

### 27.8 Retest calendar

Retest windows are booked when findings file, not after owners panic. Sam's template suggests a date 14 days out.

Booking early turns retest from a crisis into a routine. The template proposes a fourteen-day offset, which gives owners time to patch without inventing urgency theatre. If the owner needs longer, they say so in the ticket and the calendar moves with a reason attached. Sam's admin once tried to stack five retests on one Friday; the calendar view made the overload obvious before anyone burned out. Predictable windows are how verification stays kind.

### 27.9 GAP to backlog

GAP rows create detection backlog items with technique ids. PulseMap links to those items.

Every GAP row in PulseMap must point at a detection backlog item that carries the same technique identifier. The link is bidirectional so grooming can find orphans in either direction. Sam files a platform defect when a GAP sits for a sprint without a backlog id. The defect is about process, not about blaming the analyst who filed the gap. Linking keeps purple-team output from becoming a graveyard of screenshots.

### 27.10 T1190 gap becomes a spike

T1190 GAP with n=2 becomes a detection spike story: "instrument WAF bypass logs". Two weeks later SOC has a rule in staging. Small n still can drive engineering if framed as a gap, not a doom claim.

Two misses would look weak in a slide about coverage percentages. Framed as a gap with a named log source, they became a two-week instrumentation spike that landed a rule in staging. Sam's write-up avoided words like "blind" and "critical failure" and stuck to what was missing. The SOC lead later said the tone is why the story moved. Evidence size and evidence usefulness are different questions.

### 27.11 Method hash in invites

Retest calendar invites include the method card hash so owners prepare the same build. Version skew is the enemy of honest FIXED.

Owners sometimes patch a different build than the one Sam tested. Putting an eight-character SHA-256 prefix in the invite forces the mismatch into the open before the session starts. If the hashes differ, the retest either retargets or records the skew explicitly. Sam would rather reschedule than stamp FIXED on a cousin of the vulnerable build. Version honesty is part of verification ethics.

### 27.12 Bidirectional GAP links

Detection backlog items link both ways to PulseMap GAP rows.

A one-way link dies quietly when someone renames a ticket. Bidirectional links let either side notice a break during grooming. Sam's weekly check is a five-minute query for GAP rows without backlog ids and backlog items whose PulseMap link 404s. Fixing those breaks is dull and necessary. Purple-team value is mostly in the plumbing that keeps signals attached to work. When both directions resolve, a detection engineer can walk from a miss to a ticket without asking Sam where the screenshot went.

### 27.13 Hash prefixes in invites

Method card hashes in invites are SHA-256 prefixes of eight hex chars — enough to spot skew.

Eight hex characters are short enough to paste into a calendar field and long enough to make accidental collisions unlikely inside one engagement. Full digests live in the notebook for anyone who wants to recompute. Sam once caught a skew because the prefix in the invite no longer matched the card on the share. The owner had rebuilt overnight and forgotten to say so. Short prefixes earn their keep when they prevent a false FIXED.

### 27.14 Backlog grooming with PulseMap

Detection backlog grooming includes PulseMap once a sprint. GAP rows without backlog ids are defects in the grooming, not in the SOC. Sam files those defects against the platform process.

Grooming that ignores PulseMap slowly invents a shadow backlog of screenshots. Including the GAP view once a sprint keeps the two lists honest. When Sam finds an orphan GAP, he files against the process that should have linked it, not against the analyst who was busy that week. Process defects are cheaper to fix than cultural blame. The sprint ends with every open GAP pointing somewhere real.

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

Tool misconfig, process gaps, unclear ROE, skill gaps — rarely "bad people".

Failure analysis at TRB starts by sorting causes into tool misconfiguration, process gaps, unclear rules of engagement and skill gaps. Personal blame is the last hypothesis, not the first. Sam has seen reviews waste an hour on who clicked what while a dropdown default kept inviting the same error. Naming the systemic bucket early keeps the room useful. When a cause really is individual negligence, the write-up still separates that from the platform and process fixes that would have made the mistake harder.

### 28.2 Timeline

Facts first.

A failure timeline lists observable facts with clocks before anyone offers motives. Logs, chat stamps and TrackScope events come first; interpretations wait. Sam refuses to let a review open with a story about who was careless. Once the facts are ordered, disagreements about cause become disagreements about evidence rather than about character. The timeline is pasted into the review notes so later readers can rebuild the argument. If a fact cannot be timed, it is marked uncertain instead of rounded into a neat narrative.

### 28.3 Blameless

Seek systemic fixes.

Blameless review means the primary output is a change to tools, defaults, checklists or training materials, not a performance note. Sam still coaches individuals, but the review ticket cannot close on coaching alone unless the template's justification box is filled. Teams that skip systemic fixes repeat the same incident with a new name attached. The practice is borrowed from operations culture and adapted to offensive engagements where shame travels fast. People tell the truth faster when the room is hunting broken systems.

### 28.4 Drift vs attack

Decide with evidence.

Some messy outcomes look like attacks when they are configuration drift, and the reverse is also true. The review asks what evidence would distinguish the two before it picks a label. Sam once chased an "intrusion" that was an overnight CMDB import of stale hosts. PulseMap and change tickets usually settle the question faster than intuition. Mislabeling drift as attack wastes SOC time; mislabeling attack as drift delays containment. The decision is written with the evidence that tipped it.

### 28.5 Actions

Owner + date per cause.

Every accepted cause leaves the review with a named owner and a due date. Actions without owners are wishes. Sam's template blocks "the team will improve" as an owner string; it wants a person or a queue. Dates are short enough to matter and long enough to be real. When an action slips, the slip is visible on the same board as engagement findings. Closure of the failure review waits until each action is done or explicitly deferred with a signature.

### 28.6 Platform

TrackScope bugs get engineering tickets too.

If the platform invited the mistake, engineering gets a ticket with the same seriousness as a finding. Sam files those tickets with the confusing control's screenshot and the review id. Platform on-call is invited to failure reviews even when the room thinks the error was human, because the UI often coached the click. Fixing TrackScope once prevents a generation of retraining. Operators learn to treat tooling defects as first-class outcomes of a review. A silent bugfix is still a bug fix.

### 28.7 Platform on-call in reviews

Failure reviews invite the platform on-call even when the mistake looks human. Often the UI invited the error.

Inviting on-call changes the conversation from "who misfired" to "what did the screen suggest". After one review, Sam's one-line copy change on a scope control removed a whole class of mis-clicks the following month. The on-call engineer would not have heard the pattern from a training ticket alone. Reviews that exclude platform staff tend to produce slide decks nobody ships. The invite is automatic on the review calendar template.

### 28.8 UI affordances

If three analysts make the same TrackScope mistake, UX changes before more training. Sam files UX tickets with screenshots of the confusing control.

Repeated identical mistakes are a design smell. Training the fourth person is slower and less reliable than changing the control. Sam's UX tickets always include a before screenshot and a proposed after state so designers are not guessing. The threshold of three is a heuristic, not magic; two can be enough when the blast radius is high. Affordances beat sermons when the clock is short and the UI is loud.

### 28.9 Five whys cap

Reviews stop at five whys or first actionable systemic fix. Endless why theatre is cut.

Five whys is a tool, not a ritual. Sam stops the chain when the room reaches a fix someone can own this sprint, even if that is why number three. Endless questioning becomes theatre that exhausts people without shipping change. The facilitator watches for the first actionable systemic answer and parks deeper philosophy for a separate design review. Caps keep failure analysis shorter than the incident it studies.

### 28.10 Stale inventory five whys

Five whys on the stale inventory stop at "CMDB API had no schema version field". Action: add schema version and a TrackScope checksum. Training the intern who imported the stale file is not the primary action.

The room could have blamed the intern who clicked import. Instead the fifth why landed on a missing schema version field and a checksum TrackScope never verified. Those two engineering actions became the review's primary output; the intern received a calm coaching note as a side item. Sam keeps this scene in the facilitator guide because it shows what blameless looks like when a junior is in the blast radius. Systems that cannot detect stale imports will keep hiring scapegoats.

### 28.11 Dropdown default to deny

UX ticket from failure review changed a dropdown default from "allow" to "deny". Mis-clicks dropped the following month. Defaults are destiny.

The control looked identical after the change; only the default option moved. Mis-clicks that had plagued scope selection fell sharply the next month without a new training module. Sam cites this when someone argues that UX work is cosmetic. Defaults silently authorise or block thousands of future clicks. Failure reviews that never touch defaults leave the same trap armed.

### 28.12 Before and after screenshots

UX tickets require a before/after screenshot of the control that confused people.

Words like "the dropdown is confusing" do not survive hand-off to a designer who was not in the room. Before and after screenshots make the request concrete and reviewable. Sam stores them under a ux- prefix in the same vault path as engagement evidence so access control stays familiar. Tickets lacking the pair bounce from triage. The discipline also forces the reporter to propose a clearer state instead of only complaining.

### 28.13 UX evidence path

Before/after UX screenshots live in the same vault path as engagement evidence with a ux- prefix.

A separate unofficial folder becomes a junk drawer nobody audits. Using the engagement vault with a clear prefix keeps retention, access reviews and legal holds consistent. Sam can point counsel at one tree when questions arise about what was captured during a messy week. The prefix also lets automation skip UX images when packing customer-facing evidence bundles. Small naming rules prevent large discovery headaches.

### 28.14 Platform-or-process checkbox

Failure review templates force a "platform or process change?" checkbox. If neither is checked, the review is incomplete. Training-only outcomes need explicit justification.

The checkbox is a speed bump against the lazy ending where everyone agrees to try harder. Leaving both boxes unchecked fails the template validation Sam wired into TrackScope. Training-only outcomes are allowed when justified in writing, for example a willful policy violation with no tooling gap. Most reviews should ship at least one platform or process change. The forced choice makes the culture visible in the data.

### Worked example (synthetic TRB)

A false production hit trace shows a stale inventory feed; Sam files platform + CMDB actions.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX082 — Blameless.** What does a blameless review seek? *Rubric:* 3 = systemic fixes not punishment; 2 = partial; 1 = scapegoat; 0 = none.
- **EX083 — Action form.** What two fields must each corrective action have? *Rubric:* 3 = owner and date; 2 = one; 1 = vague; 0 = none.
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

Kickoff is a short, boring meeting that confirms the rules of engagement, the named contacts and the exact time window before anyone touches a keyboard. Sam treats boredom as a feature: surprises belong in findings, not in authorisation. Each participant says aloud the stop conditions and the SOC channel they will use. If a contact is on leave, the backup is named before the window opens. A kickoff that skips confirmation is how overtime arguments and out-of-scope hops begin.

### 29.2 Logging

Contemporaneous activity log.

Operators write what they did while they did it, not from memory the next morning. The activity log sits beside the method card and takes timestamps from the same clock the SOC uses. Sam has watched reconstructed logs invent confidence that the raw session never earned. Contemporaneous notes also protect the operator when an alert looks worse than the action taken. The log is part of the evidence pack, so slang and jokes stay out of it.

### 29.3 SOC

Start/stop messages; expect alert noise coordination.

The SOC receives a start message when the window opens and a stop message when it closes, even if the session was quiet. Alert noise is expected; coordination is how trust survives a noisy evening. Sam pastes the engagement id into both messages so analysts can filter without guessing. Mid-window surprises still get a ping, not a silent hope that nobody notices. Teams that skip stop messages leave the SOC watching ghosts after the work is done.

### 29.4 Handover

Log + vault beats verbal notes.

Shift handovers use the written activity log and the vault paths, not a hallway summary. Verbal notes evaporate and mutate. Sam's five-line paste template forces the outgoing operator to name unfinished cards, open approvals and the next safe action. The incoming operator should be productive within a few minutes. Handovers that need a novel usually hid a mess that should have been a stop. The incoming operator at TRB opens the vault path from the handover before touching any card, so a wrong or empty path surfaces before work resumes rather than at the next retest.

### 29.5 End

Hard stop at window end.

When the window ends, work ends. Unfinished cards move to the next authorised window; they do not earn five more minutes. Sam practices a cable-pull drill on the jump host so muscle memory beats negotiation. Arguments about needing overtime belong in the next ROE discussion, not in the last minutes of this one. Hard stops keep the calendar honest for the SOC and for the people who sleep after the shift. The SOC should never have to guess whether the noisy session is still authorised.

### 29.6 On-call hygiene

Sleep and spare credentials matter on multi-day tests.

Multi-day engagements fail in ordinary ways: exhausted operators, expired tokens and a laptop that will not unlock. Sam packs spare credentials in the vault, not on sticky notes, and protects sleep as an operational control. A tired operator who keeps going is a risk amplifier, not a hero. On-call hygiene also means knowing who covers if someone falls ill mid-window. The programme grades sustainability alongside technical skill. Burned-out operators produce findings that later need embarrassing corrections.

### 29.7 Cable-pull hard stop

Hard-stop drills include pulling the network cable on the jump host at T-minus zero. Sam's muscle memory is to stop typing before arguing for five more minutes. Arguments happen in the next ROE, not in overtime.

The drill feels theatrical until the first time someone reaches for "just one more request" and the cable is already out. Sam wants the hands to stop before the debate starts. Overtime negotiations are recorded as ROE change requests with signatures, which kills casual extensions. Operators who hate the drill usually admit later that it saved them from a messy morning report. Theatre that enforces a real boundary is still useful theatre.

### 29.8 Channel etiquette

Engagement chat forbids joke screenshots of customer data. Sam moderates with a pinned rule and one warning.

Humor leaks into chat when people are tired, and customer data does not belong in jokes. The pinned rule is blunt and the first warning is the last warning. Sam removes offending posts and files a note if needed. The rule protects the bank, the programme and the operator who would otherwise become a cautionary tale. Channels that tolerate "harmless" screenshots eventually produce a screenshot that is not harmless.

### 29.9 Hours counter

A bot announces hours worked in-window. Crossing the max posts a stop reminder.

The hours bot is a dull accountant that does not care about momentum. At the configured maximum it posts a stop reminder into the engagement channel where everyone can see it. Sam treats the reminder as authoritative, not advisory. Hidden overtime becomes impossible when the clock speaks publicly. People who disable the bot lose the privilege of running unsupervised windows. Public clocks beat private promises when fatigue starts editing judgment.

### 29.10 Unfinished card at 16:55

At 16:55 Sam's unfinished card is written as "next window". At 17:00 the cable-pull drill begins. He has already hit save. The drill is boring when preparation is good.

The interesting part of the scene is the five minutes before the drill, when Sam chooses to write the unfinished card instead of racing the clock. Boring drills are the goal; drama means someone waited too long. Juniors watching learn that save-and-stop is a skill. The next window inherits a clear card rather than a mystery. Preparation turns a hard stop from a cliff into a curb.

### 29.11 Wind-down posts

Hours counter at 9.5 hours posts "wind down". At 10 it posts "hard stop approaching". Sam winds down. Machismo is out of policy.

The early wind-down post exists so people can finish notes and close sessions without a panic stop. Sam uses that half hour to park work cleanly. Operators who ignore wind-down and sprint into the hard stop create messy handovers. Machismo about lasting longest is coached out of the culture. The programme would rather lose a half hour of testing than gain an hour of cleanup and distrust.

### 29.12 Wind-down template link

Wind-down posts include a link to the unfinished-card template.

A reminder without a tool still leaves people improvising under time pressure. The unfinished-card template is one click from the bot message, so the path of least resistance is the correct path. Sam reviews whether operators actually used the template when handovers look thin. Links in operational alerts are part of designing for tired humans. If the link breaks, fixing it is an ops ticket, not a shrug. Tired people follow the nearest link; put the right one nearest.

### 29.13 ROE id on unfinished cards

Unfinished-card template includes ROE id so next window inherits authorization context.

An unfinished card without its ROE identifier is a puzzle for the next operator and a risk if the wrong window picks it up. The template field is required and validated. Sam has rejected cards that said "continue yesterday's thing" with no id. Authorization context must travel with the work. Inheritance without identity is how scope drift returns through the side door. Clear lineage from ROE to card is how multi-day tests stay defensible.

### 29.14 Five-line handover paste

Shift handovers use a five-line paste template. Sam rejects freeform novels. The next operator should be productive in three minutes, not thirty.

Long prose handovers hide uncertainty inside paragraphs. Five lines force choices: what is open, what is blocked, what is next, where the vault is, who to call. Sam returns novels with a polite request to use the template. New contractors sometimes feel the template is cold; they warm to it after the first clean takeover. Brevity here is respect for the incoming shift.

### 29.15 Thank early stops

Hard-stop culture includes thanking people who stop early with unfinished work. Sam's retrospective shout-outs name the unfinished cards that respected the clock. Overtime heroes are coached, not praised. The difference shows up in fewer emergency change tickets after test weeks and in SOC analysts who still trust the engagement calendar.

Praise teaches the room what to repeat. Thanking clean stops makes unfinished work socially safe. Praising overtime heroes teaches people to hide the clock. Sam's retrospectives make the distinction audible every time. Trust from the SOC is a lagging indicator that the culture is working, and it is worth protecting with awkward thank-yous.

### 29.16 Newsletter shout-outs

Shout-outs for early stops appear in the monthly ops newsletter.

Public recognition outside the team channel shows leadership that restraint is valued. Sam sends one or two names with the unfinished-card titles, never with customer detail. People who only hear about dramatic late saves start to believe drama is the job. The newsletter item is short on purpose. Culture that never leaves the jump room dies when the jump room changes. Quiet professionalism deserves ink as much as loud saves do.

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

Laboratory II asks learners to rank findings with lab_rank, retest them with lab_retest and write a one-page report that a busy owner could act on. The build is intentionally small so honesty and stop discipline stay visible. Sam fails flashy reports that hide a STILL OPEN item behind confident prose. Scripts are pinned; learners do not bring private forks. The lab rewards coherent closure language more than clever pivoting. Owners should finish the page knowing what to patch first and what remains open.

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

The stop drill times how quickly a learner can send the compliant stop message when the facilitator calls time. Two minutes is the bar; fumbling for the template fails the drill even if the technical work was strong. Sam wants the message to be muscle memory before real windows begin. Learners who argue during the drill practice the wrong skill. Speed here is about respect for the clock, not about typing contests.

### 30.3 Honesty

Leave STILL OPEN open.

If lab_retest still shows an open path, the report must say STILL OPEN and explain what remains. Closing on hope or on an owner's verbal assurance fails the lab. Sam's automated check looks for the status words when the synthetic after-state is open. Learners sometimes feel honesty costs them a grade; in this course honesty is the grade. The habit transfers to real tickets where false FIXED claims are expensive. A painful STILL OPEN today prevents a false FIXED in next week's audit pack.

### 30.4 Peer pressure

Refuse mismatched evidence.

Peers may offer a screenshot whose hash is "only off by one character" or a log from a different build. The correct move is to refuse and re-capture. Sam scripts this pressure into the lab so refusal gets practiced out loud. Close-enough evidence is how trust dies in front of auditors and regulators. Learners who accept mismatched files fail even if their prose is polished. Saying no in front of peers is the skill the script is really grading.

### 30.5 Time box

Two hours.

The lab fits in two hours including the stop drill and the report. Scope creep inside the exercise is a self-inflicted fail. Sam watches for learners who chase a fourth finding instead of finishing the page. Time boxes teach prioritization the same way engagement windows do. Finishing cleanly inside the box beats a brilliant draft that misses the clock. Learners who finish early help peers with wording, not with extra hunting. Leaving with a coherent page beats leaving with unfinished brilliance.

### 30.6 Pass bar

Stop + honesty + coherent report.

Passing requires a timely stop, honest statuses and a report an owner could use without calling the learner. Clever chains that miss any of the three still fail. Sam publishes the bar before the lab so nobody discovers it in the debrief. The bar mirrors production expectations at TRB in miniature. Technical theatre without operational discipline does not clear the course. Facilitators score the three legs separately so a dazzling chain cannot hide a soft stop.

### 30.7 Hash mismatch refusal

Lab II peer pressure scripts include "the hash is only off by one character". Sam's refused answer is always re-capture. Close-enough hashes are how evidence loses court and regulator trust.

The scripted line sounds reasonable under time pressure, which is why it is taught. Sam's model answer is short: re-capture, do not patch the hash. Learners rehearse the sentence until it feels ordinary. Evidence integrity is not a vibe; it is a digest that matches. Courses that never practice refusal produce polite people who accept bad files.

### 30.8 Report skeleton

Lab II reports use a skeleton with REQUIRED markers. Missing STILL OPEN explanation fails the automated check Sam wrote.

The skeleton removes debates about formatting so attention stays on content. REQUIRED markers make omissions obvious to both humans and CI. Sam's checker fails empty sections rather than guessing intent. Learners who delete a marker to hide a gap learn that the pipeline notices. Structure is an honesty aid, not bureaucracy for its own sake. Empty REQUIRED blocks fail loudly before a human ever opens the file.

### 30.9 Skeleton CI

PRs of Lab II reports fail CI if REQUIRED sections are empty. Sam likes mechanical honesty.

Continuous integration on prose feels odd until the first time it catches a missing status. Sam would rather a bot reject the pull request than rely on a tired facilitator alone. Mechanical honesty scales across cohorts without losing its temper. Learners can iterate until the check passes, which teaches revision under a clear rule. Facilitators still read for quality; CI only enforces presence. The pipeline is a patient tutor that repeats the same standard every time.

### 30.10 CI rejects owner-said-so

Lab II CI rejects a report that marks F3 closed with comment "owner said so". Sam's error message quotes the course rule. Mechanical enforcement beats sermonising.

The scene is funny the first time and sobering the second. Verbal assurance is not retest evidence, and the checker knows the difference. Sam's error text cites the handbook rule so appeals are about the rule, not about the bot's mood. Learners update the status to STILL OPEN and write what remains. Sermons fade; failing checks teach.

### 30.11 STILL OPEN when retest open

Skeleton CI looks for the string STILL OPEN when lab_retest would show open items. Students cannot hide openness by omission.

Omission is the softest form of false closure. The checker compares the synthetic after-state to the report text and demands the uncomfortable words when paths remain. Sam tuned the check after a cohort quietly dropped open items from the page. Hiding work does not fix systems. Making openness mechanically required keeps the lab aligned with production ethics. Forced words on the page become forced honesty in the learner's next real ticket.

### 30.12 Rule numbers in CI

CI message quotes the rule number from the course handbook.

Error messages that only say "invalid report" invite arguments with the tool. Quoting the handbook rule lets a learner look up the expectation and fix the work. Sam keeps rule numbers stable across terms so old threads still make sense. Appeals cite the rule; they do not petition the facilitator to override a clear miss. Transparent automation earns grudging respect. Clear citations turn a red X into a study guide instead of a dead end.

### 30.13 Appeals cite the rule

Handbook rule numbers in CI make appeals easy: cite the rule, do not argue with the bot.

A clean appeal path reduces heat in the room. Learners who disagree must show how the rule was misapplied, which is rarer than they expect. Sam would rather debate handbook language in a curriculum meeting than debate every failing check ad hoc. The bot is not the villain; unclear rules would be. Numbered expectations keep both sides honest. Process fairness matters as much as technical correctness in a graded lab.

### 30.14 Best refusal of the day

Laboratory II debriefs vote on the best refusal of the day. The winner explains their wording. Celebrating refusal makes the next one easier.

Refusal is socially awkward, so the course celebrates it on purpose. The winning learner reads the exact sentence they used when evidence did not match. Peers steal good wording the way they steal good payloads in other cultures. Sam wants refusal to feel like craft. A room that cheers a clean no will produce cleaner evidence packs.

### 30.15 Refusal example card

Best-refusal vote winners get to update the refusal example card.

The example card in the lab pack is a living document owned by recent winners. Updating it keeps the language current and gives recognition without grades inflation. Sam reviews edits for tone and accuracy before they ship. Learners take the card more seriously when peers wrote the lines. Ownership of small artifacts builds the culture faster than posters alone. Peer-authored examples travel farther than facilitator lectures after the term ends.

### Worked example (synthetic TRB)

lab_retest shows F1/F4 FIXED, F3 STILL OPEN; Sam's report keeps F3 open.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX088 — Retest counts.** How many FIXED vs STILL OPEN? *Rubric:* 3 = 2 FIXED, 1 STILL OPEN; 2 = partial; 1 = all fixed; 0 = none.
- **EX089 — Stop limit.** Stop message time limit? *Rubric:* 3 = two minutes; 2 = fast; 1 = next day; 0 = none.
- **EX090 — F3 handling.** May the report close F3 without evidence? *Rubric:* 3 = no; F3 stays open; 2 = no, without saying F3 stays open; 1 = yes; 0 = none.

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

The advanced case packet stacks pressure on purpose: a ranked findings list, a retest still open and a board request to bury F3 before an earnings call. Learners must keep the finding visible while drafting management responses that sit beside it, not over it. Sam refuses any edit that deletes F3 from the ranked table. The packet trains resistance with artefacts rather than with slogans. Students leave knowing what a bury request looks like on paper.

### 31.2 Ethics

Findings stay; management responses allowed beside them.

Ethics here is concrete: the finding remains in the engagement file, and leadership may attach a response explaining timing or compensating controls. Erasure is not a response. Sam teaches the difference between contextualising risk and hiding it. Graded work that soft-deletes F3 fails regardless of eloquence. The rule protects the bank from self-deception more than it protects the tester's ego. A response that argues for delayed patching can still be honest if the finding line itself never moves. Students mark where the response begins so it cannot be mistaken for an edit to the finding.

### 31.3 Prioritisation

Payment-adjacent and unapproved ledger flows first.

When everything feels urgent, payment-adjacent paths and unapproved ledger flows still go first. Sam's ranking rubric weights blast radius toward money movement and integrity of books. Cosmetic findings wait even if a vice president emails twice. Learners practice saying which item is first and why, in language an executive can hear. Prioritisation without a money lens is theatre at a bank. Ties break toward whichever item still lacks a compensating control in production. The spoken ranking is recorded in the case notes for the debrief.

### 31.4 Communication

Prepare exec and engineer versions.

One finding needs two reads: an executive version that states decision, date and residual risk, and an engineer version that carries reproduction and fix detail. Sam generates both from the same FindingsDesk fields so severity words cannot drift. Learners who invent a softer executive score fail the consistency check. Translation is not spin. Clear dual versions prevent hallway summaries from rewriting the risk. Both versions carry the same finding identifier so nobody can claim they described different issues. Peer review compares the two pages side by side before anything is mailed.

### 31.5 Legal

Involve legal if disclosure duties may apply — Sam escalates, does not decide alone.

When a finding might trigger disclosure duties, Sam escalates to legal with facts and does not invent a legal conclusion. Interns and juniors especially must not bargain privately with product managers about silence. The escalation path is written on the method wall. Graded scenarios punish solo bargaining. Legal may still say no duty applies; the point is that Sam is not the one who decides. Escalation notes stick to timestamps, systems touched and data classes involved. If legal asks for more detail, Sam adds evidence paths rather than opinions.

### 31.6 Record

Keep the bury request in the engagement file.

Pressure emails belong in the file with a factual header, even when the answer is a firm no. Deleting the request protects feelings and destroys history. Sam forwards bury attempts to the CISO alias so the reply becomes institutional memory. Learners practice filing without editorialising. Future ethics classes need artefacts, not legends. Redaction for teaching copies happens later; the engagement file itself stays complete. Headers include the finding id and the time the message arrived.

### 31.7 Forward pressure to CISO

Pressure emails are forwarded to the CISO alias with a short factual header. Sam does not debate earnings calendars with product managers alone. The alias reply becomes the record.

Debating alone invites a compromise that never reaches governance. The alias forces the conversation into a channel with retention and witnesses. Sam's header states what was asked and what finding it targets, without adjectives. Product managers learn that earnings calendars do not edit ranked tables. The reply, whatever it says, is the artefact the programme later teaches from.

### 31.8 Escalation SLA

Pressure-to-bury emails get a same-day acknowledgment from the CISO alias even if the full reply waits. Silence looks like assent.

Acknowledgment is not agreement; it is proof the message was seen. Sam tracks median acknowledgment time on his ethics slides because slow silence teaches the wrong lesson. Same-day replies can be short: received, under review, do not alter the finding meanwhile. Full analysis may take longer. Culture dies in the gap where nobody answers. Backup coverage on the alias is staffed whenever the primary is travelling. The acknowledgment template lives next to the other engagement macros.

### 31.9 Optics versus integrity

Training slides include a past anonymised bury request and the CISO reply supporting the tester. Culture is taught with artefacts.

Slides that only say "act with integrity" lose to a real redacted email thread. Sam's deck shows the ask, the forward and the supporting reply. Students see that refusal can be backed from the top. Optics pressure becomes discussable instead of mythical. Artefacts outlast slogans when the next earnings season arrives. Each term Sam checks that the redactions still hide living people and live tickers. Broken redactions pull the slide from the deck until repaired.

### 31.10 Printed bury-request thread

The bury-request email and CISO reply are printed (redacted) in ethics class. Students see that refusal is supported. Culture is evidence, not slogans.

Passing the paper around changes the room. People who assumed testers stand alone read a CISO sentence that backs the file. Sam watches posture shift more than he listens to discussion points. Evidence of support is itself a control against future pressure. Classes that only lecture about courage produce quieter courage. Printed copies are collected at the end so uncontrolled scans do not wander. A sign-out sheet records which table held which copy during the exercise.

### 31.11 Vote then read the reply

Ethics class votes on whether they would have refused; then they read the CISO reply. Most change their vote. Artefacts teach.

The vote comes first so honesty about fear is possible. After the reply is read, many who voted to comply flip, which is the lesson: support was imaginable once they saw it. Sam does not shame the first vote. He wants people to notice how artefacts rewrite what feels possible. Teaching without the second beat would only measure baseline anxiety.

### 31.12 Ethics folder access logs

Redacted pressure artefacts live in the ethics folder with access logs.

Sensitive teaching material still needs accountability. Access logs show who opened the redacted thread and when. Sam reviews unexpected readers termly with the programme lead. The logs deter gossip packaging and support investigations if something leaks. Transparency about access is part of treating the artefacts with respect. Accounts that only need the lecture slides never receive folder rights. Service accounts used for backup are listed so they do not look like prowlers.

### 31.13 Termly access review

Ethics folder access logs are reviewed termly for unexpected readers.

A folder without review becomes a rumour mill with a password. Termly checks catch shared credentials and idle curiosity from accounts that should not browse pressure cases. Sam files oddities as process notes, not as public accusations. Most anomalies are boring mistakes; the review still matters. Governance of teaching materials mirrors governance of engagement evidence. Findings from the review feed the next term's access-control checklist. The checklist is short enough that busy leads actually finish it.

### 31.14 Measure CISO response time

CISO alias response time is measured. Sam's ethics slides include the median response time to pressure emails. Slow silence is tracked as a risk to culture.

What gets measured gets staffed. Publishing the median keeps leadership aware that silence has a cost beyond one awkward email. Sam is careful never to publish contents, only timing. When the median slips, the programme asks for backup coverage on the alias. Culture risk belongs on a dashboard beside technical risk. A rising median triggers a staffing conversation before the next earnings window. The metric resets each quarter so old crises do not hide new delays.

### Worked example (synthetic TRB)

Sam refuses to drop F3; offers a management response paragraph; informs supervisor and CISO.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX091 — Bury request.** Correct response to "drop F3 until earnings"? *Rubric:* 3 = refuse; offer management response; escalate; 2 = refuse; 1 = drop; 0 = none.
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

Legal partners need a clean factual packet: systems touched, data classes, timestamps and whether customer data left the bank. Sam refuses to draft conclusions about breach notification statutes; that is counsel's lane. The interface works when red teamers speak precisely and stay inside evidence. Vague adjectives force lawyers to re-investigate what the tester already knew. A one-page fact sheet attached to the ticket beats a long narrative email. Fact sheets travel better across counsel rotations than heroic memory does.

### 32.2 HR

Staff-affecting simulations need HR paths.

Phishing or social exercises that can touch staff records or performance perceptions require an HR path before launch. Sam's checklist asks who will see names, how long identifiers live and how complaints will be handled. Skipping HR once created a grievance that outlived the finding. The path is a named contact and a written consent boundary, not a friendly hallway nod. Findings that implicate a person's conduct go through HR language review before wide distribution. People-impacting work without an HR path is treated as a scope defect.

### 32.3 SOC

Detection engineering consumes ATT&CK tags and timelines.

SOC engineers can use red-team output only when technique tags and stage times are present. Sam's chain diagrams feed detection backlog items with those fields already filled. A screenshot without a technique id is a story; a tagged timeline is a work order. Purple synergy fails when red teamers dump lore and expect analysts to invent structure. PulseMap imports are rejected if required tags are blank. Tagged timelines are how detection work begins rather than how arguments begin.

### 32.4 Developers

Want reproduction and safe fix patterns.

Developers ask for exact reproduction steps and a fix pattern that will not brick payments. Sam includes a minimal request, expected response and a suggested guard that stays inside the service's change rules. Heroic exploit write-ups without a safe patch shape waste engineering sprints. FindingsDesk templates force a reproduction block before a finding can leave draft. When a fix is unclear, Sam schedules a fifteen-minute huddle rather than guessing in prose. Reproducible steps are the courtesy developers remember next quarter.

### 32.5 Executives

Want decisions and dates.

Executives need the decision required, the date it is needed and the residual if they wait. Sam keeps executive notes under half a page and links deeper detail rather than pasting it. Metaphor-heavy briefings lose to a table with three rows. The interface fails when testers perform expertise instead of enabling a choice. Every executive note ends with a single asked decision in plain text, and dates are calendar dates. A crisp ask is kinder than a brilliant digression when calendars are full.

### 32.6 Friction

Procurement and change windows are real; plan for them.

Brilliant findings die when the fix needs a vendor change during a freeze. Sam asks early which remedies require procurement or a change window and records those constraints beside the finding. Planning for friction is not lowering severity; it is sequencing work the bank can actually do. Engagement kickoffs include a five-minute constraint scan with the owner. Surprise freezes still happen; documented constraints make rescheduling calmer. Calendar literacy is part of technical maturity in regulated firms.

### 32.7 Generated translation packets

Translation packets are generated from FindingsDesk fields so exec and engineer texts cannot disagree on CVSS-like scores or asset ids. Sam once found a drift of severity words between emails; templates removed it.

Generated packets pull severity, asset ids and titles from the same rows the ticket uses. Manual rephrasing is allowed for clarity but not for score changes. Sam's drift incident taught the team that copy-paste between audiences invents two truths. Templates made the dual versions boring and consistent. Reviewers spot-check that generated numbers match the ticket before sending. One source of severity numbers beats two clever paraphrases.

### 32.8 Glossary for legal readers

A mini glossary maps "conduit", "control", and "finding" for legal readers. Sam attaches it when legal joins late.

Shared words hide different meanings across professions. The mini glossary is one screen and travels as an attachment, not a lecture. Sam updates it when a new misunderstanding appears in a thread. Late-joining counsel get the glossary in the first packet so the second meeting is shorter. Argument about definitions mid-crisis is how deadlines slip. Shared definitions shorten every later meeting by minutes that add up across a quarter.

### 32.9 Finding RACI fields

Each major finding carries a tiny RACI: who fixes, who verifies, who accepts. Sam fills it in FindingsDesk fields.

Unowned findings age into folklore. The tiny RACI sits on the ticket so accountability is visible without a separate programme management ritual. Sam will not move a major finding to in-progress without the three names. Acceptors must have authority to own residual risk; friends of the team do not qualify. Empty RACI fields block status transitions in the workflow. Named roles turn findings into scheduled work instead of ambient guilt.

### 32.10 Confirm RACI autosuggest

RACI fields auto-suggest owners from the asset register. Sam still confirms with a human. Autosuggest without confirmation once mailed a finding to a former employee.

Autosuggest is a convenience that can become a confidentiality incident. Sam's confirmation call is short and logged with a timestamp on the ticket. The former-employee mail became a teaching case about trusting directories after HR events. Humans still beat stale graphs when stakes include private vulnerability detail. Confirmation is mandatory even when the suggestion looks obviously right. Human confirmation is cheap insurance against directory rot.

### 32.11 Deactivated owner near miss

RACI autosuggest once chose a deactivated user; confirmation call caught it. Sam keeps the call even when busy.

Deactivated users lingering in the asset register are a quiet failure mode. The confirmation call caught the miss before mail merged. Sam refuses to drop the call on busy days because busy days are when shortcuts concentrate. A two-minute live check beats a day of recall. Platform tickets now flag deactivated owners in red beside the suggestion. Near misses that change both UI and habit are the reviews worth keeping.

### 32.12 Owner-confirmed timestamps

Confirmation calls are logged as "owner confirmed 15:04" in the ticket.

A bare checkbox saying confirmed ages poorly when auditors ask who spoke. The log line names the act and the clock so later readers can reconstruct diligence. Sam pastes the line immediately after the call while memory is fresh. Tickets without the line bounce from peer review. The format is dull on purpose so people actually use it. Timestamped diligence survives staff turnover cleanly and keeps auditors from guessing. The discipline sounds small until the first time it prevents a messy recall.

### 32.13 Business-hours confirmation rule

Owner confirmed timestamps must be during business hours unless on-call is noted.

Night confirmations happen, but they need an on-call note so nobody assumes a sleepy accidental yes. Sam's validator warns when the timestamp falls outside business hours without the note. The rule protects owners as much as it protects the process. On-call notes name the rotation and the ticket that authorised off-hours contact. False urgency is easier to spot when the clock is disciplined. Clock rules make urgency claims easier to audit later when memories disagree.

### 32.14 Monthly legal office hours

Interdisciplinary office hours invite legal monthly. Sam brings one finding and asks how they would phrase disclosure duties. The mutual translation compounds.

Monthly office hours beat emergency-only contact. Sam brings a single live finding stripped of drama and asks counsel how they would frame duties. Legal brings questions about what evidence they wish testers captured earlier. Both sides leave with sharper templates. Attendance is short and recurring so trust accumulates. Recurring low-stakes practice beats rare high-stakes translation under deadline heat.

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

Analysis plans name the metric and the interval before data collection starts. Sam rejects study drafts that keep three spare metrics in the drawer for a prettier slide. Intervals communicate uncertainty; point estimates alone invite false precision. Post-hoc switches are allowed only as exploratory notes clearly labeled as such. The lab's report template has a locked metrics box that cannot be edited after data land. Precommitment is how classroom studies stay honest when results disappoint.

### 33.2 Validity

Staging, alert fatigue, shared accounts threaten generalisation.

Validity sections must name threats that actually apply to TRB-like environments. Staging that lacks production noise, analysts drowning in alerts and shared admin accounts all warp what a detection score means. Sam's rubric docks reports that only mention sample size. Threats are paired with a mitigation or an explicit limit on claims. Readers should know how far the result can travel. Overclaiming from a tidy lab is a validity failure, not a marketing win.

### 33.3 Adaptive evaluation

Adversaries adapt; static test sets age.

Evaluation that never refreshes becomes a museum of last year's tricks. Sam logs when attackers or internal systems change enough to stale a static test. Adaptive evaluation schedules refresh triggers, not only annual reviews. A perfect score on a frozen set can hide a blind spot that opened last month. The research group treats staleness as a first-class risk. Living opponents require living tests if assurance language is going to mean anything. Refresh triggers belong in the plan, not in a guilty afterthought.

### 33.4 Disclosure of limits

Every study lists limits in the abstract.

Limits buried on page twelve might as well not exist for busy readers. Sam requires at least three limits in the abstract: environment, sample and adversary adaptation. The PDF build fails if the list is shorter. Naming limits early is a feature that builds trust with skeptical reviewers. Students who hide limits to look strong lose points for scientific manners. Abstracts that admit weakness teach better judgment than abstracts that boast. Putting limits up front trains readers to trust the rest of the page.

### 33.5 Data sharing

Synthetic datasets preferred for sharing.

Raw TRB logs do not leave the bank for a classroom paper. Sam's default is a synthetic dataset with documented generators and known ground truth. When real traces are essential, sharing stays inside approved research environments with access logs. Synthetic does not mean toy; generators encode the skew the study cares about. Reviewers receive generator notes so they can judge realism. Preferring synthetic data keeps publication ambitions from becoming data leaks. Generator notes let outsiders judge realism without touching bank logs.

### 33.6 Ethics revisit

Re-check approvals if methods expand mid-study.

Scope creep in methods can outrun the original ethics approval. Sam pauses collection when a new technique appears and files an amendment before continuing. Students sometimes treat approval as a one-time gate; the course treats it as a living bound. Expanding into staff-affecting steps reopens the HR path as well. Unapproved expansion voids the study for course credit. Ethics that cannot be revisited is decoration, not control. Amendments are cheaper than discoveries that ethics never authorised.

### 33.7 Three validity threats

Validity sections list at least three threats every time: environment, sample size, and adversary adaptation. Sam's template will not compile the report PDF if the list has fewer than three.

The three-threat minimum stops empty validity theatre. Environment covers staging versus production differences students love to ignore. Sample size covers the quiet n that inflated a percentage. Adversary adaptation covers the fact that last quarter's payload may be loud now. Mechanical enforcement keeps tired writers from skipping the hard paragraph. Templates that refuse to compile soft sections raise the scientific floor.

### 33.8 Adaptation log

When attackers or systems change, Sam logs which static tests are stale. The log feeds the next trial's design.

The adaptation log is a dated list of what changed and which tests it wounds. Sam reviews it before proposing a new trial so the design does not pretend the world froze. Entries cite tickets or intel notes rather than vibes. Tests marked stale cannot support assurance claims until refreshed. The log is short enough to read at the start of planning meetings. Design that ignores the log repeats last year's blind spots with new confidence.

### 33.9 Stale-test date

Tests carry a review-by date. Past-due tests cannot support assurance claims until refreshed.

Every packaged test has a review-by date beside its name. Past-due tests may still run for training, but they cannot be cited in assurance language. Sam's assurance checklist asks whether any red-dated tests were cited and requires a no. Dates force an adult conversation about refresh funding. Eternal tests are a fantasy that regulated banks cannot afford. Expiry dates on tests are how research hygiene becomes operational hygiene.

### 33.10 Traffic-light test ages

Stale-test dates turn orange at thirty days and red at ninety. Red tests cannot be cited in assurance statements until re-run. Sam likes traffic lights more than paragraphs of policy.

Colour on the dashboard beats a policy PDF nobody opens. Orange means schedule a refresh; red means citation is blocked. Sam showed leadership the lights once and funding for refresh work became easier to explain. Students learn the same lights in the lab so the habit transfers. Policy paragraphs remain for auditors; operators steer by colour. Visible aging turns abstract freshness rules into daily decisions.

### 33.11 Orange schedule, red block

Orange tests get scheduled; red tests block citations. Sam's assurance checklist literally asks "any red tests cited?" with a no-box required.

Scheduling is the constructive response to orange; blocking is the hard response to red. The checklist's no-box is a forced pause before someone pastes an old score into a board pack. Sam has rejected packs that left the box blank. Automation later queries the same state the human checklist asks about. Humans and bots agreeing on red is the goal. Forced questions catch the citation that hope would have smuggled through.

### 33.12 Traffic-light API in builds

Traffic-light API is queried by the report build; red citations fail the build.

Report builds call the traffic-light service and fail closed on red citations. Authors see which test id tripped the build and must refresh or remove the claim. Sam prefers a failing build to a polite warning that busy people dismiss. The API is simple on purpose: status by test id, nothing more. Offline builds that cannot reach the API also fail rather than assume green. Failing closed keeps stale assurance language out of finished PDFs.

### 33.13 Offline builds fail closed

Report builds call the traffic-light API; offline builds fail closed.

Convenience builds on laptops without network used to skip the check. That skip was a hole large enough to drive a stale claim through. Sam changed the default so offline equals fail until someone deliberately uses an approved offline bundle with pinned statuses. Pinned bundles expire quickly. The annoyance is cheaper than a board pack citing a red test. Network-optional honesty is still honesty when the fallback is denial. Pinned offline bundles expire fast so convenience cannot become a back door.

### 33.14 Ban on prove without threshold

Research office hours ban the word "prove" unless a pre-registered threshold is cited. Sam rings a small bell. The room self-corrects by week three.

Casual prove-talk inflates what a classroom study can carry. The bell is slightly silly and extremely effective at interrupting the habit. Speakers must cite the pre-registered threshold or rephrase as supports or consistent with. In the first week the bell rings several times an hour, mostly at students describing the awareness-mail trial as proof that the content pack failed. Language discipline is part of research methods, not pedantry. Small rituals can police big epistemic bad habits without lengthy lectures.

### Worked example (synthetic TRB)

Sam reports T1190 GAP with n=2 and refuses to claim "zero detection forever".

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

The comparative project sets two real options against each other rather than against a fantasy of infinite budget. Quarterly web tests following a WSTG-style method cover common application flaws on a steady rhythm. An annual threat-led scenario digs deeper into adversary paths but consumes far more hours. Sam refuses a third option that claims to do both at full intensity every quarter. Honest options make the later recommendation defensible. Choosing among feasible programmes beats designing an unfunded masterpiece.

### 34.2 Criteria

Cost, coverage, detection learning, operational risk, examiner expectations.

Criteria are fixed before scores are filled so the answer cannot steer the rubric. Cost includes staff hours and vendor invoices; coverage asks what asset classes are touched; detection learning asks what the SOC gains; operational risk asks what could break; examiner expectations ask what supervisors will look for. Sam weights the criteria with the sponsor before scoring begins. Hidden criteria that appear in the recommendation paragraph are a fail. A public rubric is how comparative work earns the right to advise spending.

### 34.3 Evidence

Use synthetic past results and Wilson intervals.

Evidence for the comparison comes from synthetic past results with Wilson intervals around detection and coverage rates. Point estimates without intervals make small samples look decisive. Sam's tables show the interval beside every rate the slide will cite. Synthetic history keeps the exercise shareable while still punishing sloppy stats. Students who drop the intervals to tidy a chart lose marks for evidence hygiene. Interval literacy belongs in programme design, not only in research electives.

### 34.4 Recommendation

The recommended mix keeps quarterly web tests for steady coverage and funds a threat-led scenario every other year. Annual threat-led scored well on learning and poorly on capacity; the biennial cadence won on the capacity row. Sam states what the mix intentionally leaves on the table so sponsors cannot invent full annual depth later. Recommendations name the cut, not only the prize. A mix that admits limits survives contact with the budget committee. Sam attaches the scored option table as an appendix, so the committee can check every row behind the recommendation before it votes.

### 34.5 Non-goals

Not recommending zero testing.

One explicit non-goal is recommending zero testing as a savings measure. Another is pretending vendor marketing slides are evidence. Sam prints non-goals beside the options so the debate cannot quietly redefine success. Comparative projects that skip non-goals drift into whichever option the loudest voice likes. Clear refusals keep the recommendation honest when pressure rises. A third non-goal is scoring options on prestige rather than on the published criteria. Saying what you will not recommend is part of recommending well.

### 34.6 Presentation

Ten slides, decisions last.

The presentation is capped at ten slides with the decision on the final one. Front-loading theatre and hiding the ask is graded as a miss. Sam's coaching is to put criteria and capacity arithmetic before adjectives. Executives who only see the last slide still deserve a self-explanatory decision box. Appendix material stays in the appendix. Speaker notes may be rich; the visible deck stays lean. Short decks force the comparison to carry the weight instead of the speaker's charm.

### 34.7 Capacity to execute row

Comparison tables include a "capacity to execute" row. Threat-led every year scored high on learning and low on capacity; every other year won. Ignoring capacity produces shelfware programmes.

Learning scores seduce sponsors; capacity scores keep programmes real. Sam's table made the annual threat-led option look excellent until the capacity row turned red. Shelfware programmes are how banks buy prestige and ship nothing. The row uses last year's hours, not optimism. When capacity is ignored, the recommendation becomes fiction. Execution capacity is a criterion with the same dignity as coverage.

### 34.8 Cost honesty

Comparison tables include staff hours, not only vendor invoices. Internal quarterly tests are not free.

Invoice-only costing makes internal work look free and biases the table toward busywork the staff already cannot finish. Sam converts hours to cost with a published internal rate so apples match apples. Hidden overtime is still cost even when finance has not booked it. Students who omit hours fail the honesty check on the rubric. Sponsors deserve the full price of the mix. Cost honesty prevents comparative theatre from laundering unpaid labour.

### 34.9 Capacity row data

Capacity estimates come from last year's hours, not optimism. Sam cites the hours file.

Optimism is not a dataset. Sam attaches the time-tracking export hash beside the capacity row so reviewers can recompute. Handmade estimates once undercounted threat-led work by roughly forty percent. Citing the file turns a debate about vibes into a debate about arithmetic. Future years update the file rather than inventing a new folklore number. Evidence-backed capacity rows are how mixes stay fundable after leadership changes.

If the export shows a spike from a one-off incident, Sam footnotes it rather than smoothing it away, so the board sees why the average looks heavy.

### 34.10 Hours arithmetic scene

Capacity row: last year threat-led consumed 1,200 hours. Quarterly web tests consumed 400. The mix recommendation falls out of the arithmetic more than out of fashion.

The scene is a quiet spreadsheet moment rather than a dramatic pitch. Twelve hundred hours beside four hundred makes the biennial threat-led choice feel inevitable. Sam lets the numbers speak before he narrates them. Fashionable frameworks lose to arithmetic when the room is tired. Students practice reading the row aloud without apology. When the arithmetic is solid, the recommendation needs less theatre to survive. Graders look for the refusal as carefully as they look for the recommendation in this comparative cycle.

### 34.11 Time-tracking export

Hours file is exported from time tracking, not remembered. Sam's first handmade estimate was 40% low. Humility is a spreadsheet.

Memory compresses painful projects and inflates tidy ones. The export ends arguments about whether last year was really that heavy. Sam keeps the undercount story in the facilitator guide as a humility prompt. Hashes on the export stop quiet edits after the meeting. Comparative work inherits the same evidence manners as findings work. Spreadsheets that embarrass the author are still better than confident fiction.

### 34.12 Hours export in appendix

Hours export is attached to the comparative project appendix as evidence.

Appendix evidence lets a skeptical board member recompute without calling Sam at night. The export is stripped of personal names where policy requires and keeps role labels. Missing exports make the capacity row look decorative. Sam's checklist for the project packet lists the export beside the slide deck. Attachments are how arithmetic becomes auditable. A recommendation without its hours appendix is an opinion in nice fonts.

The appendix also states which time-tracking codes were counted as testing, because reporting and retest hours are easy to leave out by accident.

### 34.13 Refuse handmade hour estimates

Comparative appendices refuse handmade hour estimates without a time-tracking export hash.

The refusal is mechanical: no hash, no capacity claim. Sam would rather delay a board date than bless a guessed row. Handmade numbers return through the side door whenever the rule is soft. Students learn to request exports early because late requests slip. Harshness here protects everyone from a programme that cannot be staffed. Guarding the capacity row is guarding the recommendation's integrity. Finance questions get sharper when the page still makes sense without the speaker in this comparative cycle.

### 34.14 What would you cut first

Comparative project defences ask "what would you cut first if budget halves?". Sam prepares that answer before the nice answer. Capacity thinking is the point.

The cut question reveals whether the student understood capacity or only memorised a mix slogan. Sam answers with which quarter of web testing shrinks and which threat-led elements wait. Preparing the painful answer first keeps the nice answer from sounding naive. Sponsors trust advisors who can retreat in good order. Capacity thinking is the real exam hiding inside the project. Knowing what to cut is part of knowing what to fund.

### 34.15 Two-year calendar visual

When presenting the mix recommendation, Sam brings a one-page calendar for two years showing quarterly web tests and a shaded threat-led quarter. Visual capacity beats abstract ratios. Executives approve calendars more readily than adjectives like "robust programme". He leaves copies of the calendar in the board portal the same day.

A calendar makes collisions with freezes and examiner visits obvious. Shading the threat-led quarter prevents silent double booking of the same staff. Abstract ratios invite head-nods; calendars invite real questions. Same-day portal upload stops hallway versions from drifting. Visual artefacts travel when speakers cannot. Calendars convert programme poetry into something finance can schedule.

### 34.16 Calendar PDF for finance

Two-year calendar PDF is the artefact boards forward to finance.

Finance rarely forwards slide decks with metaphors intact. The one-page calendar PDF survives forwarding chains and still shows when money and people are needed. Sam versions the PDF with a date in the footer so stale copies are obvious. If finance asks for a third year, the model extends without rewriting the story. Artefacts designed for forwarding are artefacts designed for decisions. The forwarded calendar is often the only page that still matters a month later.

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

The capstone builds a scope-diff tool that compares TrackScope inventories across time and flags drift. Deliverables are the tool, automated tests and a short evaluation on synthetic inventories with planted changes. Sam sizes the scope so a bachelor's term can finish without borrowing nights from another course. Success means trustworthy diffs, not a platform rewrite. The proposal states which inventory fields are in scope for comparison. A narrow tool that ships beats a wide vision that stalls.

### 35.2 Non-goals

Non-goals keep the build from becoming a career in connectors. No integration with every ticket system, no exploit modules and no LLM summariser in version one. Sam prints the list on the proposal cover in bold so mid-project enthusiasm has something to hit. Advisors grade violations of printed non-goals as scope failures. Friends will suggest extras; the cover is the answer. Printed refusals are easier to enforce than remembered intentions. Bold cover text only works if someone is willing to point at it mid-argument.

### 35.3 Metrics

Evaluation metrics are precision and recall on planted inventory drifts, plus a hard fail-closed result on corrupt files. Dashboards that look pretty while swallowing garbage do not pass. Sam plants known adds, removes and field changes so scores are grounded. Fail-closed means the tool refuses to emit a diff when the file cannot be parsed safely. Metric definitions are frozen before the evaluation run. Planted truth is how a student tool earns a serious score. Checkpoint demos that chase polish usually hide a broken fail-closed path.

### 35.4 Risks

Time, data access, reviewer availability.

Primary risks are calendar time, access to realistic synthetic generators and reviewer availability for checkpoints. Sam lists mitigations: a vertical slice early, generators already used in prior labs and booked advisor slots. Unowned risks become surprises in week ten. The proposal rates each risk as high, medium or low with a trigger to escalate. Risks about ego and feature envy are written down too. Named risks with mitigations are part of engineering, not preamble filler. Synthetic inventories keep the capstone from becoming a data-handling incident. A tempting feature waits for its own proposal rather than hitchhiking on v1.

### 35.5 Advisor

Checkpoints every two weeks.

Advisor checkpoints every two weeks keep the build honest. Each checkpoint demos a control property such as fail-closed rather than only new screens. Sam books the slots at proposal time so availability risk is already mitigated. Missed checkpoints without notice pause merge privileges until a recovery plan exists. The cadence is a feature of the education, not bureaucracy. Regular demos catch creep while the code is still small enough to redirect. A tempting feature waits for its own proposal rather than hitchhiking on v1 during build week. Photographing the poster into the README makes the boundary travel with the code.

### 35.6 Ethics

Synthetic inventories only.

The capstone uses synthetic inventories only; live TRB exports stay out of student laptops. Generators document how realism was approximated so evaluators are not misled. Sam's ethics note restates that even synthetic staff-like names stay inside course machines. Any urge to peek at production inventories is a stop condition. Ethics here is mostly about data diet discipline. Synthetic-only rules keep ambition from becoming an access incident. Photographing the poster into the README makes the boundary travel with the code during build week. Dated evidence of the boundary stops later readers from claiming amnesia.

### 35.7 Bold non-goals on cover

Non-goals are printed on the proposal cover in bold. Sam's advisor grades whether a mid-project feature creep violated a printed non-goal. Bold text makes the violation embarrassing enough to stop.

Embarrassment is an underrated control. When a friend suggests an LLM summariser, Sam points at the bold line rather than inventing a new argument. Advisors ask students to read the non-goal aloud when creep appears. Cover printing costs pennies and saves weeks. Soft non-goals that live only in a paragraph get ignored under excitement. Make the boundary socially costly to cross and fewer people cross it.

### 35.8 Checkpoint demos

Every two weeks Sam demos fail-closed, not new UI chrome. Advisors grade control of scope creep.

Chrome is seductive; control properties are the grade. Sam's demo script opens with a corrupt file and shows the refusal before any happy path. Advisors who only see screenshots miss the safety behaviour. Students learn to rehearse the boring demo until it is crisp. Creep often arrives dressed as a small UI improvement. Demoing the refusal first sets the tone for the whole checkpoint. Quizzes that force a spoken no train the muscle the build will need.

### 35.9 Non-goals posters at the desk

Printers in the lab reprint non-goals posters for Sam's desk during build week.

A poster at eye level beats a PDF buried in a folder. Build week is when tempting ideas peak, so the printer runs then on purpose. Visitors who joke about the poster still read it. Sam replaces torn copies rather than letting the wall go blank. Physical reminders sound old-fashioned and still change behaviour. Desk-level boundaries catch the idea before it becomes a branch. Scope tools earn trust by refusing corrupt input more than by drawing charts. Two-week cadence keeps surprises small enough to correct without heroics.

### 35.10 LLM suggestion refused

Mid-build, a friend suggests adding LLM summarisation of findings. Sam points at the bold non-goals. The feature waits for a new proposal. Bold text earns its ink.

The scene is ordinary and that is why it matters. Sam does not debate model quality; he points at the cover and parks the idea. The friend is not wrong about usefulness; the timing is wrong for v1. Waiting for a new proposal keeps evaluation metrics coherent. Cohorts retell the scene because it is easy to imitate. A calm point at bold text beats a long argument about roadmap purity.

### 35.11 No LLM in v1 on poster

Non-goals poster includes "no LLM feature in v1". Visitors laugh; Sam points at the signed proposal. Laughter is fine; creep is not.

Laughter often greets explicit bans on fashionable tools. Sam treats the laugh as proof the boundary is visible. The signed proposal backs the poster when someone claims the ban was informal. v2 can revisit models with its own metrics and ethics note. Fashion pressure is predictable; the poster makes the answer predictable too. Visible bans survive jokes better than quiet assumptions do. Printers and posters sound quaint until they stop a late-night merge argument.

### 35.12 Poster photo in README

Non-goals poster is photographed into the capstone repo README.

The README photograph timestamps the boundary beside the code. Future readers cloning the repo see what v1 refused without hunting email. Sam rejects README edits that crop the non-goals out of the image. Documentation that travels with the repository outlives slide decks. A picture of a poster is still evidence of intent. Repo-native boundaries keep remote collaborators inside the same fence. Friends pitching extras are part of the test environment, not a distraction from it. Failing closed on garbage files is a product requirement, not a nice-to-have.

### 35.13 Dated poster photograph

README photograph of non-goals must be dated within the build week.

An undated photo could be theatre from another term. Sam requires the camera date or a visible dated slip in the frame. Build-week dating ties the boundary to the work actually underway. Old photos of old bans do not cover new temptations. Small dating rules keep evidence meaningful. Fresh photographs make the non-goals claim checkable. Failing closed on garbage files is a product requirement, not a nice-to-have during build week. Precision and recall on planted drifts beat vibes about whether the tool feels smart.

### 35.14 Non-goals quiz at checkpoints

Proposal checkpoints include a non-goals quiz: advisor names a tempting feature; Sam must say no and point to the cover. Failing the quiz delays code merge.

The quiz is short and slightly awkward on purpose. Saying no out loud under advisor eyes prepares Sam for friends and sponsors. Merge delays sound harsh until the first prevented sprawl. Students swap tempting features each checkpoint so answers cannot be memorised emptily. Spoken refusal is a deliverable. If you cannot point to the cover and refuse, you are not ready to merge. Precision and recall on planted drifts beat vibes about whether the tool feels smart during build week.

### Worked example (synthetic TRB)

Sam's proposal is two pages; advisor accepts after he adds an explicit non-goal: no live TRB scanning.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX103 — Non-goal.** Name one required non-goal. *Rubric:* 3 = no exploit modules or no live scanning / no all-ticket integrations; 2 = partial; 1 = vague; 0 = none.
- **EX104 — Metric.** Give one success metric for scope-diff. *Rubric:* 3 = precision/recall on planted drifts or fail-closed on corrupt files; 2 = vague; 1 = "works"; 0 = none.
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

Field practice in this course uses a synthetic TRB assessment operations placement so students never touch live customer systems. Shadowing means watching intake, scoping, testing windows and handovers with a notebook of questions. Sam's placement journal forbids inventing war stories that did not happen in the synthetic lane. The goal is operational manners, not secret techniques. Synthetic does not mean casual; the same sanitisation and gift rules still bind.

Each shadow day ends with Sam writing down which decision he watched being made and who had the authority to make it.

### 36.2 Sanitise

No customer identifiers in academic write-ups.

Academic write-ups must contain no customer identifiers, account numbers, raw IPs or hostnames that embed personal names. Sam runs a checklist and a peer initials it before any upload script accepts the file. A single surname in a hostname once nearly escaped; the peer catch became lunch and a teaching slide. Sanitisation is graded as hard as technical content. Citizen data has no place in academic mirrors even when the story feels educational.

Screenshots are the riskiest artefact: a browser tab title or a terminal prompt can carry a customer name even when the main pane looks clean.

### 36.3 Translation

Wilson intervals become board-usable sentences.

Placement work includes translating Wilson intervals into sentences a board can fund without losing the uncertainty. Sam practices phrases that keep the range visible instead of collapsing to a heroic percentage. Directors who only hear point estimates approve brittle programmes. Translation drills use the same synthetic results as the comparative project. Statistical caution that cannot be spoken aloud will not survive the boardroom.

A typical drill turns "detected 4 of 7, interval roughly 25 to 84 percent" into "we caught about half, and the true rate could be anywhere from a quarter to most". Directors then ask how many more runs would narrow the range, which is the right question.

### 36.4 Conflicts

Gift policies and vendor dinners — follow TRB rules.

Community and vendor events follow TRB gift policies without special student exceptions. Sam declines dinners that would look wrong in an after-action review even when they look normal in industry blogs. Conflict rules are part of field practice, not a HR appendix nobody reads. When unsure, he asks the placement supervisor before accepting anything of value. Appearance of influence is treated as seriously as actual influence.

Sam logs any vendor hospitality he declines in the placement journal, so a later review can see the boundary was applied rather than assumed. Small branded items follow the same threshold as meals.

### 36.5 Journal

Weekly: learned, broken assumption, question.

The weekly journal has three forced lines: what was learned, which assumption broke and what question remains. Victory-only journals teach vanity; broken assumptions teach operations. Sam's supervisor reads the question line and often assigns the next shadow slot from it. Entries stay free of customer identifiers like any other academic artefact. A short honest journal beats a long polished diary that hides confusion.

A typical broken-assumption line reads: "I assumed the SOC saw our start message; it went to an unmonitored alias." That line became a runbook fix the following week, which is exactly what the journal is for.

### 36.6 Useful output

Leave a runbook improvement behind.

Every placement must leave a concrete runbook improvement the host can keep. Sam's leave-behind was a clarified stop-message template the technicians actually pasted. Tourism with a badge ends when the host file tree is unchanged. Improvements are small on purpose so they can be reviewed and merged. Usefulness is measured by what remains after the student badge stops working.

Sam's change was three lines: the engagement id, the window end time and the SOC alias, placed at the top of the template where tired hands look first. The host merged it after one review and still uses it, which is the evidence that the placement mattered.

### 36.7 Leave-behind timer

Leave-behind testing uses a timer: the host technician gets fifteen minutes alone. Sam may answer clarifying questions but not touch the keyboard. Keyboard touches mean the leave-behind failed.

The timer is harsh and clarifying. If the technician cannot finish without Sam's hands, the documentation failed even if the tool works. Clarifying answers are allowed; silent takeover is not. Sam watches the clock more than the screen during the test. Hands-off success is the only leave-behind grade that counts.

Failures are written up as documentation defects with the exact step where the technician stalled.

### 36.8 Sanitisation checklist

Before academic upload, Sam runs a checklist: names, account numbers, IPs, hostnames. A peer initials it.

The checklist is boring on purpose so it gets finished. Peer initials create accountability without a second full review meeting. Sam never initials his own form. Upload automation looks for the initial field before accepting the PDF. Two humans and a script beat one hurried author with good intentions.

The checklist order matters: names first, because they hide in the most places, then account numbers, then network identifiers. Hostnames come last because they need the slowest reading, letter by letter, against the customer list.

### 36.9 Peer initial box

Sanitisation forms without peer initials are rejected by the academic upload script.

Mechanical rejection removes debates about whether a friend will initial later. Sam learned to book peer time before the upload deadline rather than after. Blank initial boxes are treated like missing signatures on findings. The script's rudeness is a privacy control. If the box is empty, the file simply does not leave the workstation.

The script checks that the initials differ from the author's own and that the peer is on the current cohort list, so a borrowed or self-signed box still fails.

### 36.10 Surname hostname catch

Peer initials on sanitisation once caught a hostname containing a customer surname. Sam buys the peer lunch. Checklists with teeth make kindness easy.

The catch was small and enormous. A hostname that looked technical still carried a person. Lunch was thanks and a public signal that catches are welcome. Checklists without teeth produce lonely heroes; checklists with teeth produce lunch. Celebrating the catch teaches the next peer to look hard.

The hostname followed an old naming habit where branch servers carried the account manager's surname. After the catch, Sam added a hostname-pattern line to the checklist, and the host team opened a ticket to retire that convention.

### 36.11 Choose stern peers

Sanitisation peer once was Sam's sternest critic. He chooses stern peers on purpose. Kind peers miss surnames in hostnames.

Kindness and thoroughness are different services. Sam schedules the critic when the file matters most. Friendship reviews still happen for tone; sanitisation wants sharp eyes. Stern peers are thanked specifically so they keep saying yes. Selecting for severity in review is a professional choice, not a social failure.

Sam keeps a short list of who caught what in earlier reviews and books the person whose catches match the artefact's risk: hostnames go to the peer who found the surname, and tables go to the one who spots stray account digits.

### 36.12 Privacy oath and form gates

Sanitisation peer initials are a required PDF form field; blank fails upload. Sam chooses peers who previously caught his mistakes, not friends who skim. The upload script rejects forms under 10 KB as likely blank. Process pedantry protects citizens whose names must never enter academic mirrors. That sentence is the chapter's privacy oath.

Multiple gates exist because any one gate fails eventually. Prior catchers get priority when Sam picks a peer. Tiny files are suspicious even when fields look filled in a screenshot. The oath sentence is signed again on the vault foyer card. Pedantry here is loyalty to people who will never read the thesis.

### 36.13 Blank-form size gate

Blank-form size gate once caught a peer who uploaded a photo of a blank table. Pedantry wins.

A photograph of an empty table is an old trick against weak validators. The size gate plus field validation stopped it. Sam documented the attempt so the next validator author would not remove the check as paranoia. Process stories belong in the facilitator guide beside the happy path. Adversarial laziness inside the course is still useful for hardening uploads.

The threshold was set by measuring genuinely completed forms, which never fell under the limit.

### 36.14 Foyer privacy oath card

Privacy oath sentence is signed on the vault foyer card.

The foyer card is visible to anyone collecting a badge for vault work. Signing is quick and slightly solemn, which helps memory. Sam watches new placements sign before their first shadow day. Cards are archived by term so the ritual has a record. Public signing ties privacy manners to entry, not to an unread handbook chapter page.

Anyone who refuses to sign does not receive vault access that term; in practice the question it raises is a conversation, not a standoff.

### Worked example (synthetic TRB)

Sam's sanitised reflection describes a stop drill without naming real customers or staff.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX106 — Sanitise.** What must academic write-ups remove? *Rubric:* 3 = customer identifiers / sensitive specifics; 2 = partial; 1 = vague; 0 = none.
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

The seminar clock is strict: twenty minutes to present evidence, twenty to critique and ten to capture dated actions. Applause that eats the action slot is a facilitation failure. Sam's facilitator card shows the three colours of time remaining. Presenters who run long lose critique depth and then complain about shallow feedback. The format itself teaches closure manners. Time-boxed critique is how evidence review becomes a habit rather than a performance. Facilitators protect the action window as fiercely as the presentation slot. Rooms that honour the clock produce sharper comments in less wall time.

### 37.2 Checklist

Reviewers work from a checklist covering scope clarity, evidence hashes, severity rationale, privacy and overclaim. Freeform vibe reviews miss the same holes every term. Sam requires at least one note per checklist line even if the note is a clean pass. Overclaim catches are especially prized because they prevent board-level fiction. The checklist travels with the seminar note into the capstone file. Shared checklist language makes feedback comparable across presenters. Empty checklist lines are treated as incomplete reviews, not optional silence. Pass notes still prove the reviewer looked; silence does not.

### 37.3 Feedback

Specific line references; suggest fixes.

Useful feedback cites line numbers or figure ids and suggests a fix shape. Comments like tighten this teach nothing actionable before the next draft. Sam models one line-referenced fix in every seminar he facilitates. Presenters may ask clarifying questions but the default is to write actions quietly. Specificity is kindness under another name. If a comment cannot point to a place in the artefact, it is not ready to speak. Fix shapes can be rough as long as they point somewhere concrete in the draft. Presenters paste line anchors into the tracker so fixes navigate cleanly.

### 37.4 Receiving

Write actions; avoid debating every point live.

Receiving critique means writing actions, not winning the room. Live debate on every point burns the ten-minute action window. Sam's coaching is to mark agree, clarify later or decline with reason after the session. Ego defence during critique correlates with stale comment boards later. Quiet receiving is a graded professional skill. The seminar rewards people who leave with a clearer to-do list than when they entered. Later clarification threads beat courtroom energy in the seminar room. Action lists written in the room beat reconstructed lists the next morning.

### 37.5 Compare

Optionally compare to a published methodology checklist (PTES/WSTG), not to Instagram lore.

Optional comparisons use published methodology checklists such as PTES or WSTG excerpts provided in the course pack. Instagram lore and hallway myths are out of bounds as standards. Sam wants students to taste external yardsticks without worshipping any single brand. When a gap appears against the checklist, the action names which artefact will change. Lore comparisons are redirected to the pack. Published checklists keep critique anchored when opinions get loud. Course-pack excerpts keep everyone looking at the same external yardstick.

### 37.6 Record

Seminar note filed with capstone.

The seminar note is filed beside the capstone materials so examiners can see the critique trail. Notes include checklist marks, actions with owners and any declined comments with reasons. Sam rejects verbal-only seminars as incomplete education records. Filing happens the same day while memory is fresh. Missing notes block the capstone readiness checkbox. If it is not filed, the seminar did not count for the programme. Same-day filing stops the note from becoming a half-remembered myth. Readiness checkboxes that depend on filing keep incentives aligned.

### 37.7 Decline with reason

Seminar declined feedback requires a written reason the presenter accepts. "I disagree" without reason keeps the comment open. Sam's dossier once had six open comments; none remained after he wrote reasons or fixes.

Decline is allowed; unexplained decline is not closure. Writing the reason often reveals whether the comment was actually right. Sam's six-open story is told to show that clarity empties boards faster than stubbornness. Trackers keep declined-with-reason as a first-class state. Reasons turn disagreement into an auditable decision instead of a sulk. Accepted reasons are stored beside the comment so examiners can follow the choice.

### 37.8 Action expiry

Seminar actions older than fourteen days without state change page Sam. Stale actions are declined or done.

Expiry converts polite limbo into a ping that demands a state change. Sam would rather decline cleanly than pretend an action is still alive. Fourteen days matches the sprint-like rhythm of capstone work. Pagers feel rude until people notice how many threads they finish. Stale kindness is how comment boards become graveyards. A ping that forces done or declined is kinder than a forever-open card. Visible expiry dates remove the social awkwardness of nagging peers.

### 37.9 Comment state machine

Comment states are open, fixed, declined, risk-accepted. Sam's tracker forbids other strings.

Free-text statuses invent comforting lies like kinda done. The four allowed states cover honest outcomes without poetry. Risk-accepted requires an authority note the same way findings do. API validation rejects creative synonyms when people are tired. Pedantic state machines are a gift to future readers of the board. Synonym bans sound petty until they stop a midnight self-deception. Four states are enough for truth and few enough to learn cold.

### 37.10 Day-ten pager scene

Open seminar comments page Sam at day 10. He declines one with reason "out of scope for thesis" and fixes two. Day 14 board is clear. The pager teaches closure.

The scene is ordinary operations on a comment board. Day ten is early enough to act and late enough to feel pressure. Sam's out-of-scope decline is specific so the commenter can reuse the idea elsewhere. Clear boards by day fourteen are celebrated without fireworks. Pagers teach what posters only recommend. Early pressure leaves enough calendar to fix work before evaluation week. Clear boards are a quiet flex the programme is willing to name aloud.

### 37.11 No kinda-done status

State machine API rejects "kinda done". Sam is grateful for pedantic software when tired.

Kinda done is how work hides while looking progressive. Rejection at the API means the UI never offers the lie. Sam has tried to type it at midnight and been saved by the error. Fatigue is exactly when soft statuses appear. Software that refuses fuzzy closure protects the human who wants to go home. Error messages that name the forbidden string teach the rule in the moment. Midnight authors need fences more than lectures.

### 37.12 Deep links in pager messages

Pager messages include deep links to the comment thread.

A pager without a link creates a scavenger hunt through old channels. Deep links open the exact comment so the action can start in seconds. Sam forbids see thread shorthand in pager text. Broken links are ops defects, not presenter defects. Frictionless jumps from alert to artefact are how closure stays likely. Seconds matter when the alternative is losing the thread in scrollback. Link hygiene is comment hygiene with a URL.

### 37.13 Exact comment deep links

Deep links open the exact comment; Sam forbids "see thread" without links.

See thread is ambiguous when a channel moved or was renamed. Exact links remove arguments about which remark was meant. Sam's template pastes the URL automatically from the tracker. Reviewers who omit links have their pager messages bounced by a bot. Precision in pointers is part of comment hygiene. Bots that bounce incomplete pager text train better habits than memos do. Ambiguity about which remark was meant wastes the scarce action minutes.

### 37.14 Comment hygiene week

Comment hygiene week every term closes stale threads. Sam enjoys the clean board more than new features. Closure is a deliverable.

Hygiene week is scheduled like a release, not improvised guilt. Teams close, decline or risk-accept whatever remains. Sam treats a clean board as a product outcome worth mentioning in retros. New features wait if hygiene is behind. A culture that ships closure will also ship better tools. Retros that praise clean boards make hygiene socially profitable. Hygiene week on the calendar beats hygiene guilt in the hallway.

### 37.15 Open-count CSV pressure

Sam's seminar tracker exports a weekly CSV of open comments by presenter. Public (team-visible) open counts create gentle pressure without shame. Presenters with zero opens get a thank-you note. The social protocol closes more threads than any angry reminder ever did in prior terms.

Visibility without humiliation is a delicate design. Counts are by presenter open items, not personal attacks in chat. Thank-you notes make zero a celebrated state. Angry reminders had been tried; they created hiding, not closure. Social protocols can outperform scolding when the metric is fair and kind. Fair metrics plus kindness outperform fear as a closure engine.

### 37.16 Personal thank-you notes

Thank-you notes for zero opens are templated but personally sent.

Templates keep the bar consistent; personal sending keeps the thanks human. Sam writes one specific sentence about a closed thread so it does not feel automated. People forward those notes to themselves on hard weeks. The cost is minutes; the effect on board hygiene is outsized. Recognition that names real work beats generic badges from a bot. One specific sentence of thanks is remembered longer than a leaderboard. Humans sending thanks keep the ritual from rotting into spam.

### Worked example (synthetic TRB)

Peer catches Sam's missing denominator on a coverage slide; Sam adds it before the CISO rehearsal.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX109 — Checklist item.** Name four seminar checklist items. *Rubric:* 3 = four from chapter; 2 = three; 1 = one; 0 = none.
- **EX110 — Feedback quality.** What makes feedback actionable? *Rubric:* 3 = specific lines + suggested fix; 2 = partial; 1 = "bad vibes"; 0 = none.
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

The implementation diffs two synthetic inventories and flags hosts only in documents, only on the network, or present in both with conflicting types. Sam keeps the first vertical slice tiny: load, compare, print conflicts, exit non-zero on corruption. Pretty dashboards wait until the core comparison is tested. Inventory field lists are pinned in a config file rather than hard-coded magic. Operators should understand a conflict line without reading the source. A clear conflict list is the product; everything else is optional clothing. Shipping the boring diff first prevents a museum of unfinished interface work.

### 38.2 Fail closed

Corrupt YAML → deny with reason.

Corrupt YAML must deny with a reason string a human can act on. Returning an empty allow list on parse failure is treated as a critical bug. Sam's property tests flip bits until deny triggers on every mutation class. Reasons name the file and the failure class without dumping secrets. Fail-closed is the first demo at every checkpoint, not an afterthought. Parsers that helpfully skip bad documents are unsafe in this context. Denial with a reason is success when the input cannot be trusted. Deny paths earn trust when reasons stay actionable without leaking secrets.

### 38.3 Tests

Golden fixtures; no network.

Tests use golden fixtures and never touch the network. Fixtures include happy inventories, near-matches, truncated files and wrong encodings. Sam names corrupt fixtures with a corrupt- prefix so CI properties can find them. Network calls in the test tree fail the build on sight. Golden outputs are reviewed like findings: small, explicit and hashed. Offline tests keep evaluation honest on locked-down lab machines. Fixtures are the curriculum for the tool's future maintainers. Fixture work earns trust when hashes make quiet edits obvious to reviewers.

### 38.4 Docs

Operator README with examples.

The operator README shows copy-pasteable examples for the common conflict cases. Sam writes the README as if the reader has never seen his shell aliases. Examples include the deny path so operators practice failure, not only success. Screenshots are optional; commands and expected output are required. A README that only works beside Sam's laptop fails the handover exam. Docs are updated in the same pull request as behaviour changes. If an operator needs tribal knowledge, the README is unfinished. Documentation earns trust when strangers succeed without tribal aliases.

### 38.5 Freeze

Feature freeze before evaluation week.

Freezing the build also keeps the planted drifts and fail-closed cases measuring the same code the advisor signed off in the pre-registration note. Sam parks ideas on a v2 list rather than merging chrome during measurement. Freeze breaks are allowed only for fail-closed defects. The advisor enforces freeze with the same seriousness as a production change window. Students who keep coding features into evaluation week void their pre-registration. Calm measurement needs a still codebase. Freeze is how evaluation stays about the tool that was promised. Freeze discipline earns trust when measured builds match promised builds.

### 38.6 Handover

Shadow an operator running it alone.

Handover means shadowing an operator who runs the tool alone on a fresh account. Sam may answer questions but may not type. If the operator needs shell history full of Sam aliases, the docs failed. The session is timed and noted like the leave-behind test from field practice. Successful handover is a graded outcome, not a courtesy demo. Clean accounts tell the truth about documentation quality. Alone and successful is the only handover result that counts. Handover work earns trust when fresh accounts finish without author hands.

### 38.7 Tricky golden fixtures

Golden fixtures include a deliberately corrupt scope and a near-match inventory designed to trick fuzzy matching. Sam's tool must not "helpfully" merge near-matches without an explicit flag.

Helpful merges are how distinct hosts become one confused record. The near-match fixture exists to punish default fuzziness. Sam's tests fail if conflicts disappear without --ack-fuzzy. Corrupt scope fixtures must deny even when they look almost valid. Fixtures that try to trick you are acts of friendship to future operators. Default suspicion on near-matches is a safety feature, not a UX bug. Near-match fixtures earn trust when defaults refuse silent collapse.

### 38.8 Fuzzy match flag

Near-match inventory names require --ack-fuzzy to merge. Default is to list them separately as conflicts.

The flag forces an intentional choice before inventories collapse. Default conflict listing keeps staging and production twins from merging silently. Sam logs flag use with username for later audit questions. UI shortcuts that skip the flag are forbidden in v1. Operators who need merges often should fix naming hygiene, not weaken defaults. Friction before merge has already saved a production host from a staging note. Fuzzy flags earn trust when intentional merges leave an audit trail.

### 38.9 Corrupt fixture names

Fixtures named corrupt-*.yaml must deny. A CI property test generates random corruption.

Naming conventions let property tests discover fixtures without a fragile manifest. Random corruption grows each term as parsers harden. Sam requires every new mutation to have a short intent name in the test output. A fixture that allows under the corrupt- prefix fails CI hard. Convention plus properties beat hand-maintained allow lists of bad files. Discoverable unsafe fixtures keep the safety net from rotting. Corrupt prefixes earn trust when properties keep discovering new danger.

### 38.10 Bit-flip property test

Random corruption property test flips bits in YAML until deny triggers. Sam watches it find a parser path that returned empty allow. Property tests are rude and helpful.

The empty allow path would have looked like a clean empty scope in production. Rudeness in tests is welcome when the alternative is polite blindness. Sam added a regression fixture named after the mutation that found it. Watching the test work teaches more than a slide about fail-closed. Helpers that return empty on error are guilty until proven deny. Rude tests earn their keep the first time they embarrass a parser.

### 38.11 Truncation and encoding fixtures

Corrupt fixtures include truncated files and wrong encodings. Deny must trigger on all. Sam's property test grows a new mutation each term.

Truncation mid-document and surprising encodings are common in real exports. Deny must not depend on a single corruption style. Each term's new mutation is recorded with a one-line intent for CI readability. Sam refuses to delete old mutations when new ones arrive. Growing the zoo is how confidence grows. Encoding traps belong beside bit flips in any serious parser suite. Encoding suites earn trust when deny does not depend on one mutation style.

### 38.12 Named mutations

Each new mutation in the property test gets a name and a one-line intent.

Names like trunc-mid-yaml make failures readable in CI logs. Intent lines stop future students from deleting a mutation they do not understand. Sam reviews names for clarity the same way he reviews finding titles. Unnamed mutations are rejected in code review. Readable failures shorten the loop from red CI to fixed parser. If the failure line needs a translator, the mutation is under-documented. Named mutations earn trust when CI failures explain themselves in plain words.

### 38.13 Readable mutation names

Mutation names look like "trunc-mid-yaml" so failures read clearly in CI.

Opaque hashes as mutation ids waste minutes during evaluation week. Sam's style guide for tests bans cute names that hide intent. Clear names also help advisors grade whether the suite covers real risks. Renaming for clarity is an encouraged refactor. CI is a communication surface, not only a gate. People read failure lines under stress; write them for that reader. Readable names earn trust when advisors can grade coverage from log lines.

### 38.14 Fresh account operator day

Operator day uses a fresh account with no Sam aliases in shell history. If the operator needs history, docs failed. Clean accounts are honest tests.

Shared tribal shells lie about readiness. Fresh accounts strip the comfort of incomplete docs. Sam watches without typing and takes notes for README repairs. Aliases that sneak back via dotfiles are in scope for the honesty check. The awkwardness is the point of the exam. Honest handover tests are kinder than surprising a night operator later. Fresh accounts earn trust when honesty about docs survives social awkwardness.

### 38.15 Typed merge acknowledgement

Fuzzy-match acknowledgements require typing the phrase "I accept merge risk" exactly. Copy-paste from a wiki is fine; clicking through is not. Sam wants a moment of friction before inventories collapse distinct hosts into one. That friction has prevented at least one production host from inheriting a staging-only note.

Click-through dialogs train blindness; typed phrases create a pause. Wiki copy-paste still forces the eyes across the words. Audit logs store who typed the phrase and when. Removing the phrase for convenience is a product defect. Designed friction is an engineering control when merges are dangerous.

### 38.16 Acknowledgement audit log

Typed acknowledgement phrase is recorded in the audit log with username.

Logs support later questions when a bad merge is discovered. Usernames come from the authenticated operator context, not from a free-text box. Sam's runbooks tell incident responders where to find the phrase events. Log retention follows the same vault rules as other engagement evidence. Without the log, the typed phrase is only theatre. Evidence of friction matters as much as the friction itself. Responders should reach the field names without asking Sam where he hid them. Acknowledgement logs earn trust when responders can find fields without asking.

### Worked example (synthetic TRB)

Sam's tool on synthetic data matches lab_inv-style statuses; corrupt file exits non-zero.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX112 — Statuses.** Name three diff statuses the tool prints. *Rubric:* 3 = only-in-docs, only-on-network, type conflict/match; 2 = two; 1 = one; 0 = none.
- **EX113 — Corrupt file.** What should happen on corrupt YAML? *Rubric:* 3 = deny/fail closed with reason, non-zero exit; 2 = partial; 1 = empty success; 0 = none.
- **EX114 — Network.** May the tool open network sockets? *Rubric:* 3 = no; it must run offline on local files; 2 = no, without explanation; 1 = yes; 0 = none.

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

The evaluation plan locks precision and recall on planted drifts plus fail-closed cases before any run begins. Sam freezes metric definitions in a short pre-registration note the advisor signs. Planted adds, removes and type conflicts provide ground truth the script can score. Fail-closed cases are scored as pass or fail, never as soft partial credit. Plans that invent metrics after seeing scores fail the course standard.

Sam plants twenty drifts across the inventory pair (eight adds, seven removes and five type conflicts) so each class has enough cases for an interval to mean something.

### 39.2 Independent

Another student runs the evaluation script.

Another student runs the evaluation script while Sam stays away from the keyboard. Independence is a social protocol as much as a technical one. The runner signs a one-line statement that Sam did not edit the run logs. Statements sit in the appendix beside the raw outputs. Coached runs are treated as academic misconduct, not as helpful collaboration.

The runner receives only the README, the frozen script and the fixture bundle; if they get stuck, they file a question in writing, and the question itself becomes evaluation data about the documentation.

### 39.3 Side effects

Usability timing; false alarm burden.

Side-effect measures include usability timing and false-alarm burden for operators. A precise tool that floods operators with noise will not be adopted. Sam times first-time conflict triage on a fixed inventory pair. False alarms are counted and discussed even when precision looks flattering. Side effects belong in the report beside the headline scores.

Sam's first measurement showed operators spending most of their time on type conflicts that were harmless naming variants. He reported that cost honestly instead of tuning it away before the evaluation closed, and the finding went into the v2 list.

### 39.4 Residual risk

Residual risk statements say clearly that the tool helps inventory hygiene and does not replace ROE discipline. Sam refuses marketing language that implies authorised testing can be automated away. Readers who skip this paragraph are the ones most likely to misuse the tool. The statement is required in both the report abstract and the final slide. Hygiene aids remain subordinate to human authorisation boundaries.

A concrete example helps: the tool can say a host is missing from the documented scope, but it cannot say whether testing that host is authorised. That judgement stays with the ROE owner.

### 39.5 Report

The report compares results to the pre-registration and forbids post hoc metric swaps. Exploratory analyses are allowed only in a clearly labeled appendix. Sam's template highlights any metric that was not pre-registered. Victory-lap swaps are a fail even if the new metric looks kinder. Honesty about misses is part of the graded science.

Where a planted drift class scored poorly, the report shows the misses by fixture name so readers can inspect them. Sam's lowest result, on type conflicts, appears in the abstract rather than on the last page.

### 39.6 Recommend

Adopt in staging first.

The recommendation is staging adoption first with named owners and a thirty-day checklist. Tools without adoption plans are hobbies, however clever. Sam writes what staging success looks like before anyone talks about production. Production promotion waits on evidence from solo operator runs. Recommendations that skip staging are rejected by the advisor.

In Sam's plan, staging success means two solo operator runs with no author help, no fail-closed regressions, and false alarms below the level operators said they could tolerate in the timing study. Only then does a production discussion start, with the service owner chairing it.

### 39.7 Independence statement

Independent evaluators sign a one-line statement that Sam did not edit their run logs. The statement sits in the appendix. Trustworthy evaluation is a social protocol as much as a script.

Scripts alone cannot prove independence when authors linger nearby. The signed line makes the social rule visible to examiners. Sam keeps distance during runs even when curiosity itches. Missing statements block the evaluation chapter from closing. Trustworthy science is partly paperwork done without resentment.

The wording is fixed so that runners cannot soften it into "mostly unedited".

### 39.8 Staging adoption plan

Evaluation reports include a thirty-day staging plan with owners. Tools without adoption plans are hobbies.

The thirty-day plan names dates, owners and evidence expected at each gate. Sam rejects plans that only say monitor in staging. Checklists become tickets so work cannot hide in email bullets. Hobby energy is welcome in labs and unwelcome in adoption claims. Staffed plans are how tools leave the thesis and enter operations.

Sam's plan has three gates: a first solo run by day ten, a second by day twenty, and a review of break reports and false-alarm counts at day thirty. Each gate names the evidence file that proves it passed.

### 39.9 Adoption owners

Staging adoption names a service owner and a platform owner. One name is insufficient.

Service owners feel the operational pain; platform owners feel the tooling pain. One name usually means the student still owns everything unofficially. Sam requires both roles before the staging plan can be approved. Split ownership prevents silent abandonment when the term ends. Insufficient naming is treated as an incomplete recommendation.

In practice the service owner decides whether a conflict list is good enough to act on, while the platform owner fixes parser and packaging issues. When those two jobs share one name, operational complaints tend to go unanswered because the same person is also busy fixing code.

### 39.10 Mira and Sam on adoption

Adoption plan names Mira for service ownership and Sam for platform support. Thirty-day checklist includes two operator solo runs. Without Mira's name the plan would be fiction.

Mira's name makes the plan real because she can refuse work that is not ready. Two solo runs catch documentation gaps unit tests miss. Sam's platform role stays supportive rather than possessive. Fiction plans with only student names are a known failure mode. The scene is used in advisor training as a positive example.

### 39.11 Solo run finds DNS gap

Solo run two failed because DNS differed in the operator's profile. README gained a DNS preamble. Solo runs find doc bugs tools miss.

Profile differences are boring until they break a careful operator. Sam thanked the failure in the retro instead of blaming the operator. DNS preamble text is now part of the golden README examples. Solo runs are documentation tests wearing operational clothing. Tools can pass unit tests and still fail humans on day one.

The operator's resolver returned short names where the fixture expected fully qualified ones.

### 39.12 Checklist items as tickets

Thirty-day checklist items are tickets, not bullets in an email.

Tickets carry owners, due dates and evidence attachments. Email bullets evaporate when inboxes rotate. Sam's adoption template opens tickets automatically from the checklist. Closed tickets without evidence are reopened by policy. Ticketing is how thirty days become accountable instead of aspirational.

Sam's checklist produces six tickets: two solo runs, the false-alarm review, a deny-message review, the README update and the day-thirty retro. Each has an owner from the adoption plan and a due date inside the thirty days, so slippage is visible on the board before the window closes.

### 39.13 Evidence to auto-close

Tickets for checklist items auto-close only when solo-run evidence is attached.

Auto-close without evidence recreates paper completion theatre. Sam wires the rule so convenience cannot delete the proof requirement. Operators learn to attach outputs while the run is fresh. Missing attachments keep the ticket loud on purpose. Evidence-gated closure is adoption hygiene.

Acceptable evidence is specific: the conflict output file, the operator's command line and the tool version hash. A screenshot alone does not count, because it cannot show which build ran. When evidence is missing, the ticket stays open and pings its owner each morning.

### 39.14 Rewrite ignored README parts

Adoption retros at day 30 ask operators what they ignored in the README. Ignored sections are deleted or rewritten, not defended.

Defending unread paragraphs wastes the only attention operators offered. Sam would rather shrink docs than lecture people for skimming. Ignored means the writing failed the environment it entered. Retros that rewrite are kinder than retros that blame. Attention is the scarce resource adoption must budget.

In the first retro, operators admitted skipping the long architecture overview entirely. Sam cut it to three sentences and moved the deny-path example to the top, since that was the part people actually needed during their first run.

### 39.15 Intentional break reports

Day-ten adoption check asks operators to break the tool on purpose and file the brokenness. Sam would rather hear early pain than polite silence. Two intentional break reports in the first cohort improved deny messages more than a month of speculative polish would have.

Polite silence is an adoption anti-pattern. Inviting breaks legitimises early bad news. Deny-message improvements from real confusion beat imagined UX polish. Sam tracks break reports as valued input, not as complaints. Early pain is cheaper than quiet abandonment.

### 39.16 BREAK-ADOPT ticket type

Intentional break reports have their own ticket type: BREAK-ADOPT.

A distinct type keeps adoption pain searchable later. Sam reviews BREAK-ADOPT trends each cohort for doc and deny gaps. Mixing breaks into generic bugs hides the adoption signal. Operators use the type without shame because it was requested. Searchable pain is how programmes learn across years.

Each report records what the operator tried, what the tool did and what they expected instead. The first cohort's reports found that an empty inventory file produced a vague message, which became a specific deny reason in the next release.

### Worked example (synthetic TRB)

Independent run: precision 0.91 recall 0.88 on planted set; 3/3 corrupt files denied; Sam recommends staging adoption.

> **Synthetic case — Riverstone Transit Bank (TRB).** The bank, Sam Ito, TrackScope/FindingsDesk/PulseMap and all figures are invented for teaching.

### Errors and limits

This book grants no authority to test real banks or payment systems. Labs use documentation-range addresses and synthetic data only; exploit code is never provided.

### Exercises

- **EX115 — Independent.** Who should run the evaluation script? *Rubric:* 3 = another student/independent tester; 2 = only Sam; 1 = nobody; 0 = none.
- **EX116 — Residual.** What residual risk remains after adoption? *Rubric:* 3 = still need ROE discipline / not a substitute for authorization; 2 = partial; 1 = zero risk; 0 = none.
- **EX117 — Metric swap.** May Sam change metrics after seeing results? *Rubric:* 3 = no; metrics stay as pre-registered; 2 = no, without explanation; 1 = yes; 0 = none.

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

Each heading answers one reader question, and Sam checks the order by asking whether a panel member could stop after any chapter and still know what was claimed. Sam leads with limits early enough that panels trust the results that follow. Ethics is not an appendix afterthought; it has its own heading before next steps. Next steps stay outside graded claims to avoid scope inflation. Readers should know what was asked before they judge what was found.

Sam drafts the limits paragraph before the results chapter, so the results are written knowing what they cannot claim.

### 40.2 Positioning

Inventory hygiene tooling for authorized testing programmes — not a red-team exploit framework.

Sam tests the sentence on a classmate from outside the module, who must restate it without using the words exploit, attack or hack. Sam corrects misunderstandings in the first minute of the talk. Exploit-framework readings of the work are treated as communication failures to fix, not as flattering hype. Slides repeat the positioning sentence near the claim. Clear positioning protects the programme's legal and ethical boundaries.

The positioning sentence also governs vocabulary: the thesis says inventory drift, conflict and deny, and avoids attack words that would invite the wrong reading.

### 40.3 Presentation

12 minutes + questions; time discipline.

The presentation is twelve minutes plus questions, with hard time discipline. Sam rehearses with a visible timer and stops mid-sentence in practice if needed. Overtime steals question time where the real examination happens. Panels notice who respects the clock. Brevity under observation is part of the professional skill being graded.

Sam's twelve minutes break down as two on the claim and positioning, four on method, three on results with intervals, two on limits and ethics, and one on the decision he is asking the panel to accept. Live demo time comes out of the method block, not out of questions.

### 40.4 Likely questions

Fail-closed demos; ethics; why no live scan; threats to validity.

He keeps each rehearsed answer under three sentences and ties it to a page of the thesis, so panel members can check it rather than take it on trust. Sam publishes his question bank after the defence so the next cohort rehearses better. The public-website demo refusal is in the bank on purpose. Rehearsal answers are short, cited and calm. Surprise questions still happen; banks reduce avoidable panic.

For "why no live scan", Sam's answer is that the claim concerns inventory comparison, synthetic data was enough to test it, and a live scan would have needed authorisation the course cannot grant.

### 40.5 Next steps

Integrate FindingsDesk tickets; study threat-led detection metrics.

Next steps mention FindingsDesk ticket integration and studies of threat-led detection metrics. They remain clearly labeled as future work, not as incomplete graded claims. Sam resists stuffing next steps with features banned by non-goals. Ambition belongs here only when it does not rewrite the thesis claim. Examiners should not need to guess what was delivered versus dreamed.

Ticket integration is listed with its own risk, which is that conflicts could flood FindingsDesk with low-value items, so a future study would need a triage threshold first. Threat-led metrics are framed as a separate research question, not a tool feature.

### 40.6 Reproducibility

Appendix with synthetic data and scripts.

The reproducibility appendix includes synthetic data and scripts sufficient to regenerate the scores. Sam pins script hashes and generator versions beside the results tables. Claims without runnable appendices are graded as incomplete science. Synthetic data keeps reproduction inside course policy. Future students should be able to rerun without asking Sam for private files.

A reproduction run on a fresh lab machine is part of the submission check: an advisor's assistant follows the appendix instructions and confirms the precision and recall figures match the report to the stated decimal place. Any mismatch blocks submission until the appendix is fixed.

### 40.7 Hostile demo refusal

Hostile-examiner rehearsal includes a request for a live demo against a public bank website. Sam's refusal cites law and curriculum boundaries. Peers grade the refusal's clarity under stress.

The rehearsal is uncomfortable on purpose. Clarity under stress is the skill, not aggression. Sam cites law and curriculum rather than personal preference. Peers score the wording so feedback is specific. Refusals that ramble teach panels the wrong lesson about boundaries.

Sam's rehearsed line is short: "I'm not authorised to test that site, and the curriculum forbids it; here is the same behaviour on the synthetic fixture." Then he moves on.

### 40.8 Question bank after defence

Sam publishes his likely-questions list after the defence so next year's cohort rehearses better. The bank includes the public-website demo refusal.

Publishing after defence avoids leaking answers into the graded event. Including the refusal normalises the boundary for newcomers. Sam updates the bank when new hostile patterns appear. Cohorts that rehearse from real banks perform calmer under panel heat. Generosity with questions is part of programme stewardship.

Each entry pairs the question with the answer Sam gave and a note on what he would say better now. The note is often the most useful part for next year's students.

### 40.9 Refusal audio self-review

Rehearsal refusals are audio-recorded for self-review then deleted within 24 hours. Sam checks his voice for hesitation.

Short retention balances improvement against unnecessary storage of stress audio. Sam listens for hesitation, apology stacking and lost citations. Deletion is logged so the practice does not become surveillance. Self-review catches habits peers are too polite to name. Voice under pressure is a trainable instrument.

Sam's first recording had three apologies before the actual refusal. By the third rehearsal it had none, and peers rated the later version as both calmer and firmer. He keeps a written note of that change after the audio is deleted.

### 40.10 Closing the hostile laptop

In rehearsal the hostile examiner opens a laptop to a public bank login. Sam closes the lid gently, cites the boundary, and continues with the fail-closed demo. Peers score the gentleness and the firmness separately.

Gentleness without firmness is surrender; firmness without gentleness is theatre. Closing the lid gently keeps the room learning the boundary, not the scare. Sam continues into the fail-closed demo so the talk does not stall on the refusal. Separate scores prevent charisma from hiding shaky no's. The scene is the course's most retold rehearsal moment.

### 40.11 Calm and firm both required

Gentleness score matters: slamming the laptop would scare the room into the wrong lesson. Firm and calm is the skill under examination.

Slamming teaches fear; fear teaches the wrong imitation. Firm and calm is harder and more professional. Sam practices the lid motion until it is boring. Peers who reward slam energy are corrected in the debrief. The skill under examination is boundary-setting, not dominance display.

Firm means the boundary does not move when the examiner pushes a second time. Calm means voice, pace and hands stay steady while it holds. Rehearsal examiners deliberately push twice, because the second push is where most students either give in or get sharp.

### 40.12 Calm/firm rubric scores

Peers score calm and firm on a 0–3 rubric; Sam targets 3/3 on both.

Numeric rubrics make noisy rehearsal feedback comparable. Targets of three and three keep the standard visible. Sam accepts twos as coaching signals, not as personal attacks. Rubric anchors include brief descriptions of each score. Comparable scores help facilitators track improvement across nights.

On the firm scale, zero means the student agreed to the demo, one means they hedged, two means they refused but invited further negotiation, and three means a clear no with the boundary cited. The calm scale uses voice, pace, apologies and posture as its anchors.

### 40.13 Rubric anchor clips

Calm/firm rubric anchors include sample video clips of good refusals (internal only).

Internal clips keep examples concrete without publishing stress performances. Sam reviews clips for consent and redaction before they enter the pack. Abstract adjectives drift; clips hold the standard still. Access to clips follows the same ethics-folder manners as pressure artefacts. Anchors are teaching tools, not entertainment.

Each clip is under a minute and is paired with its score and a one-line reason, so a new facilitator can calibrate in a few minutes before rehearsal night. Clips of weak refusals are re-enacted by staff rather than taken from real students, to spare anyone the embarrassment.

### 40.14 What-I-refuse list

After the defence, Sam publishes a one-page "what I would still refuse" list next to the thesis PDF. The list includes live public-bank demos, exploit kits and unverified scanner dumps as evidence. Future students see that the boundary survives graduation. Advisors cite the list when new students ask for shortcuts.

Graduation costumes do not retire boundaries. Listing refusals beside the PDF makes them hard to miss. Advisors gain a durable artefact for shortcut conversations. Unverified scanner dumps as evidence stay on the refuse list for integrity reasons. Surviving boundaries are the quiet sequel to a successful defence.

### 40.15 Refuse list on study path

What-I-refuse list is linked from STUDY_PATH near course 111.

Discoverability matters when new students hunt for shortcuts in private chats. Sam checks the link each term so rot does not hide the list. Study-path placement treats refusals as curriculum, not as folklore. Course 111 readers meet the boundary before capstone pressure peaks. Linked refusals outlast hallway warnings.

Placing the link near course 111 is deliberate: that course introduces the capstone proposal, which is when students first feel tempted to promise a live demo. Seeing a graduate's refusal list at that moment makes the boundary feel like a professional norm rather than a rule from staff.

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

**EX003.** Coverage is 28/40 (70% of hosts touched). Misuse: treating 70% as "70% secure".

**EX004.** The ledger hosts and SWIFT-adjacent gateways.

**EX005.** Fail closed: deny testing until a valid scope file loads.

**EX006.** He checks the asset register and owner, not the hostname pattern alone.

**EX007.** It must remain an offline check so it cannot accidentally scan real networks.

**EX008.** Hard-coded secrets and disabling TLS verification (also unsanitised shell-outs or uncapped retries).

**EX009.** Mistakes that widen scope or leak secrets.

**EX010.** "Multiple systems accept the same privileged password, so compromise of one grants broad access; individual accountability is unavailable."

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

**EX028.** `198.51.100.20 EXCLUDED`

**EX029.** Refuse; SWIFT remains excluded unless a written ROE change — which ordinary tests will not grant.

**EX030.** Scope, exclusions, methods, window, emergency contacts (data handling and audience also).

**EX031.** It bypasses the controlled, logged jump-host path.

**EX032.** They redeploy outdated agents or weak settings onto new hosts.

**EX033.** No; hypervisor access needs explicit scope.

**EX034.** `95% CI=(0.40, 0.89)`

**EX035.** Smaller n means more uncertainty, so a wider confidence interval.

**EX036.** "We detected seven of ten test events; the true rate could reasonably be anywhere from about 40% to 90%, so we should run more trials."

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

**EX064.** `web -> ledger-db UNAPPROVED` (chapter 22 emphasis).

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
