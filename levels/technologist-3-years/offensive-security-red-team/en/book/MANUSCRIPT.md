# Authorized Offensive Security and Red Team: A Technologist's Book

- Language: English (`en`); technologist course, three years; approximately 2,400 hours of planned study.
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; nine offline labs use only the Python 3 standard library and their outputs are embedded from real runs on synthetic data. Independent technical review and the 300-page A4 verification remain open.
- Audience: technology implementers and administrators who will build, run and measure an organisation's authorized assessment capability and work alongside its defenders.
- Relation to neighbouring books: the [technical book](../../../../technical-18-months/offensive-security-red-team/en/book/MANUSCRIPT.md) focuses on tooling discipline and verification; the [bachelor's book](../../../../bachelors-4-years/offensive-security-red-team/en/book/MANUSCRIPT.md) adds broader theory. **This book is about integrating services, controls, operations and measurement around authorized testing.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification and **no authority to test any real system**. The book contains no exploit code, payloads or step-by-step attack procedures. Labs check scope, records, evidence, ratings, coverage and reports on invented data.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–9 build the computing, identity, architecture and measurement literacy a technologist needs before touching an engagement. Chapters 10–23 cover the authorized assessment life cycle: governance, scope, data flows, risk, methodology, a guided lab, tooling hygiene, controls, monitoring, troubleshooting, integration, automation and evaluation. Chapters 24–30 are research method, team studio, handoff, deployment and validation, field practice and the capstone. Each chapter contains outcomes, teaching sections, a worked example, a labelled synthetic case, errors and limits, three exercises scored 0–3, a synthesis and a **Continue studying** block. Run each lab with `python3 file.py`; none opens a network connection.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Tidewater Regional Transit (TRT)** — bus and light-rail operator with a staff portal, timetable API, internal wiki, staff VPN and a fare-payment segment that is always excluded | Organisation studied throughout | Invented |
| **Priya Natarajan** | Security technologist in TRT's engineering team | Invented |
| **Northpoint Assurance** | External testing provider contracted by TRT | Invented |

All addresses come from documentation ranges reserved by RFC 5737 (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24).

### Core sources

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide); MITRE [ATT&CK](https://attack.mitre.org/). Full list in [References](#references).

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

You will (1) describe the hardware, firmware, operating system and application layers of a computer in terms an assessor needs; (2) explain why fragile or shared systems change how a test is planned; (3) write an asset record that a scoping meeting can use; (4) recognise when a system belongs to someone who has not authorized testing.

### 1.1 Layers an assessor must name

A computing system is a stack. At the bottom sit processor, memory, storage and network interface. Firmware such as UEFI or a baseboard management controller starts the machine and often keeps running beside it. The operating system schedules processes, enforces file permissions and exposes services. Applications sit on top and hold the data the business cares about. When a test report says "the host", a reader cannot tell which layer was examined; a technologist names the layer, because the owner, the patch route and the risk are different for each.

### 1.2 Why capacity and fragility matter

Assessment traffic consumes resources. A service that answers fifty requests a minute in normal use may degrade when an inventory tool sends thousands. NIST SP 800-115 warns that testing can disrupt operations and asks planners to weigh that risk before choosing techniques. Old embedded controllers, single-threaded legacy daemons and storage arrays near their limits are the usual casualties. The answer is not to skip them silently but to record the constraint and agree a gentler method, such as configuration review, with the owner.

Priya's first ENG-712 diagram separates passenger internet paths from staff VPN paths before any prefix list is built. Trust assumptions differ on each path, so a single flat inventory would hide where authorization must change.

### 1.3 Shared and virtual infrastructure

Many systems run on hardware owned by someone else: a hosting provider, a managed-service partner, a cloud platform. The client may own the virtual machine but not the hypervisor or the storage fabric beneath it. Authorization from the client therefore covers only what the client controls. Provider terms, which sometimes require notice and sometimes forbid certain test types, must be read before planning.

Shared hosting means TRT may not see the underlying hypervisor. Priya's ENG-712 scope therefore names virtual machines and URLs TRT controls, not the provider's management plane. When a finding touches shared infrastructure she escalates to the cloud owner rather than probing sideways. Northpoint's ROE repeats that boundary so testers do not invent permission.

### 1.4 The asset record

A useful record holds: identifier, business function, owner, location (physical or logical), operating system and version, criticality, known fragility, and the authorization status for testing. Every later chapter leans on these fields: scope checks read the address, risk ratings read criticality, reports read the owner.

Priya's asset row for the staff portal carries owner, criticality and the fragile note "change freeze Fridays". Without that record lab_scope decisions look arbitrary. She updates the row when DNS moves, because a stale identifier is how OUT-OF-SCOPE hosts get tested by mistake.

### Worked example

Priya inventories the TRT timetable server. Hardware: a three-year-old rack server. Firmware: vendor BMC with its own network port. OS: a supported Linux release. Application: the timetable API. She records the BMC as a separate asset, because its network port lives on a management VLAN that Northpoint's scope does not mention. The scope meeting will need to decide whether it is in or out.

> **Synthetic case.** Tidewater Regional Transit and its timetable server are invented for this chapter.

### Errors and limits

Treating "the server" as one thing hides firmware and management interfaces. Assuming cloud tenancy grants permission over the provider's layers is a common and serious mistake. This chapter describes architecture only; it does not explain how to attack any layer.

### Exercises

- **EX001 — Hidden interface.** Why should a baseboard management controller with its own network port appear as its own asset record? *Rubric:* 3 = separate interface, separate owner/patch route, scope must decide explicitly; 2 = separate interface only; 1 = "it is part of the server"; 0 = none.
- **EX002 — Fragile daemon.** A legacy route-planning daemon crashes under heavy load. Propose how the plan should treat it. *Rubric:* 3 = record fragility, agree lower-impact method (config review or throttled check) with owner, document in ROE; 2 = exclude without discussion; 1 = test normally; 0 = none.
- **EX003 — Hosting boundary.** TRT rents virtual machines from a hosting company. Which layers can TRT authorize, and what must be checked for the rest? *Rubric:* 3 = TRT authorizes its VMs/apps; hypervisor and fabric need provider terms/notice; 2 = partly; 1 = TRT authorizes everything; 0 = none.

### Synthesis

Name the layer, record the owner and the fragility, and never let tenancy masquerade as authority over someone else's hardware.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) read address ranges in CIDR notation; (2) separate in-scope, excluded and out-of-scope addresses with a small script; (3) explain why DNS names and IP addresses can drift apart during an engagement; (4) list the internet services a transit operator typically exposes.

### 2.1 Addresses, prefixes and ownership

An IPv4 network such as 192.0.2.0/25 covers 128 addresses from .0 to .127. The prefix length tells you how many leading bits are fixed. Scope documents almost always list prefixes rather than single hosts, so a technologist must be able to test membership quickly and without mental arithmetic errors. Ownership is separate from membership: a prefix announced by a cloud provider may contain addresses that belong to thousands of customers.

lab_scope prints 192.0.2.10 and 198.51.100.20 as IN-SCOPE inside TRT's documented /25 teaching ranges. Priya teaches prefix length with those RFC 5737 addresses so learners never point tools at live transit networks. Ownership of each prefix is written beside the CIDR before Northpoint receives the list.

### 2.2 Exclusions inside ranges

Real scopes often carve holes. TRT's fare-payment segment, 192.0.2.64/27, sits inside the larger in-scope block because of how the network was historically numbered. A checker must evaluate exclusions first; otherwise the broader inclusion wins and a forbidden system is touched.

The fare carve-out 192.0.2.70 EXCLUDED sits inside a larger block on purpose. Priya's checker must honour holes, not only outer prefixes; otherwise ENG-712 would green-light fare-payment hosts. She demos the EXCLUDED line in kickoff so Northpoint sees the hole is intentional, and she fails any scope sheet that lists only outer CIDRs without the fare carve-out written beside them.

### 2.3 Names versus numbers

DNS records change. A hostname approved on Monday may resolve to a different address on Thursday after a migration, perhaps to a shared content-delivery address. Good practice is to approve both the name and the address, resolve again before each session, and stop if they diverge.

After a CDN migration the staff-portal name resolved outside the approved addresses. Priya paused ENG-712, re-ran lab_scope, and waited for a written white-team update. Names alone never authorize; numbers on the signed list do. While the session is held, Priya screenshots the old and new resolutions into evidence with a HOLD note, not a guess.

### 2.4 Typical exposed services

A transit operator usually publishes a passenger website, a timetable or real-time API, a staff remote-access gateway, mail, and sometimes a vendor support portal. ATT&CK catalogues the adversary use of remote-access gateways as T1133 External Remote Services, which is why such gateways are commonly prioritised in scope discussions.

TRT's ordinary exposed face is the passenger site, timetable API, staff VPN and mail — not fare validators. Method statements for ENG-712 list those services explicitly. Anything that looks like fare.trt.example is refused even if it answers on an interesting port.

### Lab A — scope checker

```python
"""Lab A (ch 02): classify synthetic targets against a written scope. Documentation ranges only."""
import ipaddress
IN_SCOPE = [ipaddress.ip_network(n) for n in ("192.0.2.0/25", "198.51.100.16/28")]
EXCLUDED = [ipaddress.ip_network("192.0.2.64/27")]  # fare-payment segment, carved out by the client
targets = ["192.0.2.10", "192.0.2.70", "192.0.2.200", "198.51.100.20", "203.0.113.5"]
def verdict(addr):
    ip = ipaddress.ip_address(addr)
    if any(ip in n for n in EXCLUDED):
        return "EXCLUDED"
    if any(ip in n for n in IN_SCOPE):
        return "IN-SCOPE"
    return "OUT-OF-SCOPE"
for t in targets:
    print(f"{t:15} {verdict(t)}")
print("testable:", sum(verdict(t) == "IN-SCOPE" for t in targets), "of", len(targets))
```

Run with `python3 lab_scope.py`. Verified output:

```text
192.0.2.10      IN-SCOPE
192.0.2.70      EXCLUDED
192.0.2.200     OUT-OF-SCOPE
198.51.100.20   IN-SCOPE
203.0.113.5     OUT-OF-SCOPE
testable: 2 of 5
```

### Worked example

Five candidate addresses reach Priya from Northpoint's planning sheet. The script marks 192.0.2.70 EXCLUDED because it falls in the fare-payment carve-out, and 192.0.2.200 OUT-OF-SCOPE because a /25 ends at .127. Only two of five are testable. She returns the sheet with those verdicts before any session is scheduled.

> **Synthetic case.** Addresses use RFC 5737 documentation ranges; TRT's network layout is fictional.

### Errors and limits

Checking inclusions before exclusions, trusting yesterday's DNS answer, and confusing "the client uses this address" with "the client owns it" are the classic failures. The script checks arithmetic, not legal authority.

### Exercises

- **EX004 — Range boundary.** Using the lab output, why is 192.0.2.200 out of scope even though it starts with 192.0.2? *Rubric:* 3 = /25 covers .0–.127, so .200 is outside; 2 = says outside without reason; 1 = says in scope; 0 = none.
- **EX005 — Ordering bug.** Suppose a colleague rewrites the function to test IN_SCOPE before EXCLUDED. What would 192.0.2.70 return, and why is that dangerous? *Rubric:* 3 = IN-SCOPE; fare-payment system would be tested; 2 = wrong verdict noted; 1 = no change; 0 = none.
- **EX006 — Drifting hostname.** The approved name portal.trt.example now resolves to 203.0.113.5. What should Priya do? *Rubric:* 3 = stop, the address is out of scope, confirm with owner and re-approve before testing; 2 = stop only; 1 = test the name anyway; 0 = none.

### Synthesis

Membership is arithmetic, exclusions come first, and every name is re-resolved and re-checked before a session starts.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write small, readable Python functions that make one decision each; (2) use only the standard library so a lab runs on any approved workstation; (3) test a function with known inputs before trusting it; (4) explain why assessment tooling should fail closed.

### 3.1 Why technologists program

Assessment work produces lists: hosts, accounts, findings, evidence items, retest dates. Scripts that check, sort and summarise those lists remove copying errors and make decisions repeatable. They are not attack tools. In this book every script reads invented data held in the file itself and prints a verdict.

Priya automates host and finding lists so humans spend time on HOLDs and severity, not on copying rows. Scripts that classify scope and hash evidence are in bounds; scripts that invent attack paths are not. ENG-712's operator log is generated from gate-passing actions only.

### 3.2 One function, one decision

A function such as `verdict(addr)` in Chapter 2 answers one question and returns a small set of labels. That design makes it testable: feed it an address you already know the answer for and compare. When a function both decides and prints and writes files, a bug in one part hides in the others.

verdict(addr) returns IN-SCOPE, EXCLUDED or OUT-OF-SCOPE and nothing else. That single decision is unit-tested with 192.0.2.10, 192.0.2.70 and 192.0.2.200 before every window. A helper that also edits the inventory it reads fails TRT code review, because it no longer answers one decision and a bug in the edit would hide in the verdict.

### 3.3 Standard library first

The Python standard library includes `ipaddress`, `datetime`, `hashlib`, `json`, `csv` and `collections`. These cover scope arithmetic, time windows, evidence hashing, structured records and counting. Avoiding third-party packages means no dependency review, no supply-chain surprise, and identical behaviour on the reviewer's machine.

ipaddress, datetime, hashlib and json cover ENG-712's classroom labs without third-party scanners. Priya pins the standard-library choice in the kit inventory so supply-chain arguments stay about TRT tools, not random PyPI packages pulled mid-window. If Northpoint later brings a commercial scanner, that tool gets its own row, owner and data-handling note.

### 3.4 Failing closed

If a scope file is missing or a date cannot be parsed, the safe default is "do not proceed". A checker that returns "allowed" when it hits an exception is worse than none, because it creates false confidence. Write the deny path first, then add the allow conditions.

Missing scope files make the checker fail closed to "do not proceed". Returning allowed on exception would have green-lit 192.0.2.200 in a broken parse. Priya's tests assert the closed path with a deleted-file fixture: removing the scope file in CI must yield do-not-proceed, never allowed. The fixture sits beside the ENG-712 test table so auditors can rerun the closed path.

### 3.5 Tests as evidence

A short table of inputs and expected outputs, run before each engagement, is evidence that the tooling behaves. Keep it with the engagement records so a reviewer can rerun it.

The pre-engagement test table for verdict() is filed under ENG-712 beside the ROE. When Northpoint asks whether the tool drifted, she shows the table run at kickoff, not a memory of green output. Because the run is attached to the ticket before tools start, nobody can later claim the checker was 'probably fine' without producing that artefact.

### Worked example

Priya writes a helper that returns "allowed" only when a date string parses and falls inside the window. Her first draft caught `ValueError` and returned "allowed". She rewrites it so the exception returns "STOP: unreadable time", and adds three known cases — inside, outside, malformed — to a test list that runs before each night's work.

> **Synthetic case.** Priya's helper and its test inputs are invented for teaching.

### Errors and limits

Copy-pasted snippets from forums may hide network calls or unsafe defaults; read every line. Programming skill does not create permission to test anything.

### Exercises

- **EX007 — Exception default.** A parser receives "2026-11-31 23:00" (an invalid date). What should a fail-closed window checker return? *Rubric:* 3 = a stop/deny label and the reason, never "allowed"; 2 = deny without reason; 1 = allowed; 0 = none.
- **EX008 — Library choice.** Name the standard-library module you would use to compute SHA-256 digests and one reason to prefer it over a third-party package. *Rubric:* 3 = hashlib + no extra dependency/supply-chain review/same behaviour for reviewer; 2 = module only; 1 = third-party; 0 = none.
- **EX009 — Known-answer table.** Give three test inputs with expected outputs for the Chapter 2 `verdict` function. *Rubric:* 3 = three correct pairs covering IN-SCOPE, EXCLUDED and OUT-OF-SCOPE; 2 = two correct; 1 = one; 0 = none.

### Synthesis

Small functions, standard library, deny by default, and a known-answer table kept as evidence.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) design a minimal record for a finding; (2) validate records for missing fields, wrong types and illegal values; (3) explain why controlled vocabularies make reports comparable; (4) link findings to evidence through identifiers rather than prose.

### 4.1 What a finding record needs

A finding is a claim: on this asset, this weakness exists, shown by this evidence, with this severity. The minimal fields are therefore an identifier, the asset, an ATT&CK technique ID or other weakness reference, a severity from an agreed list, and a pointer to evidence. Remediation owner, due date and status come later in the life cycle.

Finding F-01 needs id, asset, evidence id, severity and scenario before it may enter the report builder. lab_records rejects incomplete rows. Priya will not argue severity on a record that still prints missing evidence.

### 4.2 Controlled vocabularies

If one tester writes "urgent", another "P1" and a third "very bad", nobody can count criticals. A fixed set — low, medium, high, critical — lets dashboards add and compare. ATT&CK IDs such as T1078 do the same job for adversary behaviour: "valid accounts" phrased five ways is still one technique.

TRT's vocabulary is low, medium, high, critical — never urgent. lab_records flags F-02 for severity urgent so dashboards stay countable. Northpoint's writers get the same four words in the ROE appendix, so TRT dashboards remain comparable across providers and across engagements.

### 4.3 Identifiers over prose

Evidence is linked by an ID such as E-001, not by "see the screenshot from Tuesday". IDs survive renaming, translation and copying into a ticket system. Each ID must be unique within the engagement.

In ENG-712, F-09 points at E-002 by identifier, so renaming the PNG or exporting the wiki to another format does not break the link. Ticket systems receive the identifiers unchanged when findings are copied across. Before the report builder runs, chat references such as the wiki screenshot are rewritten as evidence identifiers, so every claim in the draft points to one specific file.

### 4.4 Validation as a gate

Records are validated before they enter the report. A validator that lists every problem, rather than stopping at the first, saves round trips with the tester.

The validator lists every problem on a record in one pass. F-03 missing evidence and a bad severity on another row both appear before the author rewrites. Round trips drop when the gate is complete: on ENG-712's first dry run a validator that stopped at the first problem cost a day of back-and-forth with Northpoint's authors.

### Lab B — record validator

```python
"""Lab B (ch 04): validate synthetic finding records against a minimal schema."""
REQUIRED = {"id": str, "asset": str, "technique": str, "severity": str, "evidence": str}
SEVERITIES = {"low", "medium", "high", "critical"}
records = [
    {"id": "F-01", "asset": "trt-portal", "technique": "T1078", "severity": "high", "evidence": "E-001"},
    {"id": "F-02", "asset": "trt-wiki", "technique": "T1213", "severity": "urgent", "evidence": "E-002"},
    {"id": "F-03", "asset": "trt-vpn", "technique": "T1133", "severity": "medium"},
]
for r in records:
    problems = [f"missing {k}" for k in REQUIRED if k not in r]
    problems += [f"{k} not {t.__name__}" for k, t in REQUIRED.items() if k in r and not isinstance(r[k], t)]
    if r.get("severity") and r["severity"] not in SEVERITIES:
        problems.append(f"bad severity '{r['severity']}'")
    print(r["id"], "OK" if not problems else "; ".join(problems))
```

Run with `python3 lab_records.py`. Verified output:

```text
F-01 OK
F-02 bad severity 'urgent'
F-03 missing evidence
```

### Worked example

Northpoint delivers three draft findings. F-01 passes. F-02 uses "urgent", which is not in the agreed severity list. F-03 has no evidence pointer, so nothing supports the claim. Priya returns F-02 and F-03 with the validator's messages and accepts F-01 into the tracker.

> **Synthetic case.** These three findings and their assets are fictional TRT examples.

### Errors and limits

A schema guarantees shape, not truth: a well-formed record can still describe something that never happened. Keep the vocabulary short; too many severity grades produce argument instead of action.

### Exercises

- **EX010 — Unsupported claim.** According to the lab, what is wrong with F-03, and why does that block it from the report? *Rubric:* 3 = missing evidence; a finding without evidence cannot be verified; 2 = names problem only; 1 = says OK; 0 = none.
- **EX011 — Vocabulary repair.** How should F-02's severity be fixed, and who decides the value? *Rubric:* 3 = map to an agreed level (e.g. high/critical) by the tester with reviewer agreement, using the rating method; 2 = picks a value only; 1 = add "urgent" to list; 0 = none.
- **EX012 — Extra field.** Propose one additional field for the remediation phase and justify it in a sentence. *Rubric:* 3 = sensible field (owner, due date, status, retest date) with reason; 2 = field only; 1 = irrelevant field; 0 = none.

### Synthesis

A finding is a structured claim with a fixed vocabulary and an evidence pointer; validate before you report.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) distinguish vulnerability assessment, penetration testing and red teaming; (2) state the confidentiality, integrity and availability goals in plain words; (3) explain the difference between a control's existence and its effectiveness; (4) explain why authorization, not skill, separates testing from crime.

### 5.1 Three kinds of assessment

A vulnerability assessment enumerates known weaknesses broadly and usually stops at identification. A penetration test tries, within agreed limits, to confirm whether weaknesses can actually be used and what they lead to. A red-team exercise emulates a specific threat actor over a longer period to test detection and response as a whole, often with only a small "white team" aware of it. NIST SP 800-115 describes review, target identification and analysis, and target vulnerability validation as families of technique; PTES describes phases from pre-engagement through reporting.

### 5.2 CIA in operational words

Confidentiality: only the right people read timetable drafts and staff records. Integrity: nobody alters next week's driver roster without trace. Availability: passengers receive real-time arrivals when they need them. Every finding should say which of these it threatens, because that steers who cares and how fast.

For TRT, confidentiality covers staff roster drafts; integrity covers timetable truth; availability covers passenger information at rush hour. Priya rates F-01 shared admin as integrity and availability risk, not as a confidentiality trophy hunt.

Timetable integrity failures at rush hour hurt riders even when no personal data leaks. Priya's F-01 write-up leads with that operational CIA framing for the CISO.

### 5.3 Existence versus effectiveness

A policy that requires multi-factor authentication exists on paper. Effectiveness is shown only when an assessor observes that accounts actually cannot sign in without the second factor. Assessments measure effectiveness; audits often stop at existence. Both matter, but a report must say which one it measured.

ENG-712 does not rely on the policy PDF as proof of anything. It includes an observed staff-portal login path that still accepted a password without a second factor, recorded as evidence before it was rated. The report states that this was an effectiveness check, so a reader does not mistake a policy quote for proof that MFA works.

### 5.4 Authorization is the line

The same activity — checking whether an account is protected — is a service when written permission exists and an offence in many jurisdictions when it does not. Skill does not change that. Chapter 10 covers the documents that create permission.

Priya opens ENG-712 only after the CISO approval path has signed, and the signature timestamp is the first line in the engagement pack. Northpoint may not start quietly on staging clones before that line exists, however keen its testers are. Any activity before the signature is treated as unauthorised, even if the same check would later have been permitted.

### Worked example

A TRT manager asks Priya for "a quick pen test of the VPN before Friday". She asks what decision the result will support. The real need is to confirm that ex-contractor accounts have been disabled — an effectiveness question about one control. She proposes a targeted account review instead of a penetration test, which needs a scope, an agreement and a window that Friday cannot provide.

> **Synthetic case.** The manager's request and TRT's VPN are fictional.

### Errors and limits

Calling every scan a "pen test" inflates assurance. Labels from vendors vary; read what was actually done.

### Exercises

- **EX013 — Name the service.** A board wants to know whether the SOC would notice a realistic intruder over six weeks. Which assessment type fits, and why? *Rubric:* 3 = red-team exercise; tests detection/response over time against a threat profile; 2 = type only; 1 = vulnerability scan; 0 = none.
- **EX014 — Paper control.** TRT's policy states that all VPN logins require MFA. What evidence would show effectiveness rather than existence? *Rubric:* 3 = observed/sampled sign-in records or test accounts showing second factor enforced for all paths; 2 = vague observation; 1 = the policy document; 0 = none.
- **EX015 — Roster change.** Which CIA property is threatened if a driver roster can be altered without a trace, and who should hear first? *Rubric:* 3 = integrity; operations/roster owner and security lead; 2 = integrity only; 1 = availability; 0 = none.

### Synthesis

Choose the assessment type from the decision it must support, measure effectiveness, and remember that permission is the only line between practice and harm.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) name the OS artefacts an assessor typically asks for; (2) explain how virtualization changes isolation assumptions; (3) describe why snapshots and golden images matter to remediation; (4) refuse requests that imply live intrusion of a production hypervisor without provider permission.

### 6.1 What an operating system exposes

An OS holds accounts, process lists, listening services, package inventories, logs and configuration files. For authorized assessment these are evidence sources when the agreement allows access. A technologist who understands where each source lives can ask for exports rather than for interactive sessions, which reduces operational risk and still produces checkable artefacts.

OS evidence for TRT guests is package lists, listeners and auth logs collected under the ROE. Priya does not dump process memory for curiosity. Fare appliances stay untouched even when they share a VLAN drawing.

### 6.2 Patch and configuration state

A supported OS with current patches is different from an unsupported release that no longer receives security updates. Configuration also matters: a service that listens on every interface, a password stored in a cleartext file, a firewalled host with an unused management port left open. These are configuration facts, not exploit recipes, and they appear in findings as evidence of control gaps.

Unsupported guests on the staff VLAN become findings with owners; current patched guests do not. Configuration drift — open RDP that lab_ports would mark NOT APPROVED elsewhere — is filed with the package state, not as a separate folklore list.

### 6.3 Virtualization and shared fate

Guests share a hypervisor, storage and sometimes a network fabric. Isolation is a property of the platform's design and of how carefully it is configured. A finding that one guest can reach another guest's management interface is a platform concern, not only a guest-OS concern. Provider terms usually forbid testing the hypervisor from inside a guest; that boundary must be written into every cloud or hosting engagement.

Shared hypervisors mean one noisy test can affect neighbours. ENG-712 rate limits and dry-runs exist partly because TRT hosts sit on shared fabric. Priya notes shared fate in the residual-risk page.

### 6.4 Snapshots for remediation

When a fix is applied, a snapshot of the known-good state lets operators roll back if the change breaks something. Snapshots also freeze a moment for later review, but they can contain secrets. Store them under the same access rules as other evidence and delete them when the agreement says so.

For ENG-712 the retest plan for 2026-12-08 names the post-fix snapshots of the portal guest, so the retest compares the same build that was fixed. Without them, a dispute over whether F-01 is VALIDATED can turn into an argument about which build was examined. The snapshots are stored and deleted under the same access and retention rules as other evidence.

### Worked example

Priya asks the OS team for a package inventory export of the staff-portal VMs, not for a shell. The inventory shows an unsupported library used by a side tool. The finding cites the inventory export as evidence, lists ATT&CK technique T1195 Supply Chain Compromise as the related adversary pattern for later discussion, and recommends an upgrade path. No interactive session was needed.

> **Synthetic case.** The package inventory and unsupported library are invented for TRT.

### Errors and limits

A package list is a point-in-time artefact; it can be stale by the next day. Guest access never implies hypervisor access. This chapter does not describe how to escape a virtual machine.

### Exercises

- **EX016 — Export over shell.** Give two reasons to prefer a package-inventory export over an interactive shell on a production VM. *Rubric:* 3 = lower ops risk + reproducible evidence; 2 = one reason; 1 = shell is always better; 0 = none.
- **EX017 — Hypervisor line.** Northpoint asks to "check the hypervisor for isolation bugs" from inside a guest. What does Priya say? *Rubric:* 3 = refuse; out of TRT authority; needs provider authorization and terms; 2 = refuse only; 1 = allow; 0 = none.
- **EX018 — Snapshot secret.** A remediation snapshot of a portal VM contains a cleartext service password. How should it be handled? *Rubric:* 3 = treat as evidence/secret; restrict access; rotate the password; delete/return per agreement; 2 = restrict access; 1 = leave in ordinary storage; 0 = none.

### Synthesis

Prefer exports, respect the hypervisor boundary, and treat snapshots as both recovery tools and potential secret stores.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) describe authentication, authorization and accounting as separate decisions; (2) explain why shared and leftover accounts appear so often in assessments; (3) map common identity weaknesses to ATT&CK technique IDs; (4) design a least-privilege checklist for a staff portal.

### 7.1 Three decisions

Authentication answers "who is this?" Authorization answers "what may they do?" Accounting answers "what did they do?" A system that authenticates strongly but authorizes everyone as administrator has only solved the first question. Findings should say which decision failed.

On TRT's portal the three can fail independently: a correct password used with a leftover contractor role is still a finding. F-07's leftover VPN roles show authorization drift while authentication still works, and the missing accounting trail belongs to the same family of findings. Priya scores each decision separately in the write-up, so owners know which control to fix.

### 7.2 Shared and leftover accounts

Shared passwords for "the ops account" destroy accountability: nobody knows who used it. Leftover accounts of contractors and former staff are a classic source of unexpected access. ATT&CK catalogues the adversary use of legitimate credentials as T1078 Valid Accounts, and the creation of new accounts as T1136 Create Account. Mapping a finding to these IDs lets defenders search the same patterns in their own logs.

Shared ops passwords destroy the accounting leg; F-07 tracks ex-contractor VPN accounts for the same reason. ENG-712 recommends named accounts and revocation dates, not another shared secret.

### 7.3 Multi-factor and recovery paths

A second factor raises the cost of stolen passwords. Recovery paths — SMS reset, help-desk override, backup codes — must be protected at the same level, or they become the weak door. MFA request generation (ATT&CK T1621) is an adversary technique against push-based factors; that is a design concern for purple-team exercises, not a cue to disable MFA.

When the ROE allows it, Priya's method statement includes a review of the staff portal's recovery paths, including SMS reset and help-desk override. A strong MFA design with a weak reset process is filed as a finding rather than ignored. The review stays at configuration and process level and does not involve triggering push requests at real staff.

### 7.4 Least privilege as a checklist

For each role on the staff portal: list the actions it needs, remove the rest, and record who can grant exceptions. The checklist is evidence that authorization was designed rather than inherited.

Least privilege for portal roles is a written checklist signed by the app owner. Exceptions list who granted them and when they expire. The checklist is attached as evidence beside F-01; an unsigned checklist does not count as least-privilege evidence. At each retest Priya re-reads the exceptions list, because an expired exception that still grants rights is itself a finding.

### Worked example

Priya reviews TRT's VPN account list. Three accounts belong to contractors whose contracts ended months ago. She records a finding under T1078, evidence E-010 (the account export with last-login dates), and recommends disablement plus a quarterly review. She does not attempt to use the accounts.

> **Synthetic case.** The leftover contractor accounts are fictional TRT examples.

### Errors and limits

Listing accounts is not the same as proving they can be used; that step needs explicit authorization. Do not store recovered passwords in tickets.

### Exercises

- **EX019 — Which decision?** A portal lets any authenticated staff member edit the public timetable. Which of AAA failed, and what is the fix direction? *Rubric:* 3 = authorization; restrict edit to a publisher role; 2 = authorization only; 1 = authentication; 0 = none.
- **EX020 — ATT&CK mapping.** Map "ex-contractor VPN accounts still enabled" to a technique ID and name. *Rubric:* 3 = T1078 Valid Accounts; 2 = T1078 or Valid Accounts alone; 1 = wrong ID; 0 = none.
- **EX021 — Recovery path.** Name one recovery-path weakness that can undo MFA and a mitigation. *Rubric:* 3 = e.g. weak help-desk reset / SMS interception / unprotected backup codes + matching mitigation; 2 = names weakness; 1 = disable MFA; 0 = none.

### Synthesis

Separate who, what and what-was-done; retire leftover accounts; map identity findings to ATT&CK so defenders can hunt them.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) draw a trust-boundary diagram for a small service; (2) explain defence in depth without treating it as a slogan; (3) place network, identity and application controls on that diagram; (4) identify where assessment evidence should be collected.

### 8.1 Trust boundaries

A trust boundary is a place where assumptions change: from internet to DMZ, from DMZ to internal network, from application to database, from staff device to VPN. Crossing a boundary should require a control — authentication, encryption, a gateway, a filter. Diagrams that omit boundaries hide the places where findings matter most.

Priya's diagram shows internet, DMZ, portal and directory as separate changes of assumption, each with its own control. Fare-payment sits behind another gateway and is a different trust domain, so it never inherits portal permissions because it appears nearby on a slide. Scope follows these boundaries rather than a flat list of addresses that happen to respond.

### 8.2 Defence in depth as layers with purposes

Depth means independent layers that fail differently. A VPN, an application login and a database permission are three layers. If they all depend on the same password store, they are one layer wearing three hats. An assessor looks for shared single points of failure as carefully as for missing layers.

A purple replay in ENG-712 showed the VPN and the portal failing together in the same directory outage mode. If all three layers collapse when the directory is down, the depth is only apparent. The recommendations therefore include independent session controls rather than another layer that depends on the same password store.

### 8.3 Where evidence lives

Network evidence lives in gateway logs and packet captures when authorized. Identity evidence lives in authentication logs. Application evidence lives in access logs and configuration exports. Knowing where to ask saves interactive access that nobody needs.

For ENG-712 the evidence plan names the gateway logs, directory authentication logs and portal access logs before the window opens, along with who will export each one. Packet captures need their own explicit line in the ROE, because they can collect far more personal data than a finding requires. Priya does not start captures on shared links on her own initiative, even when a log seems incomplete.

### 8.4 Architecture and scope

Scope should follow architecture. If the fare-payment segment sits behind a different gateway with different owners, it is a different trust domain and usually a different engagement. Mixing domains in one report confuses remediation.

Because fare-payment is a separate trust domain, ENG-712's exclusions name 192.0.2.64/27 and fare.trt.example. The exclusion paragraph is read aloud at kickoff and initialled by the architecture owners, and any disagreement about where the boundary lies is resolved in writing before tools run. An exclusion paragraph that nobody has initialled is treated as unread.

### Worked example

Priya sketches TRT's staff portal: internet → reverse proxy → application servers → database; a parallel path for staff VPN → management jump host → same application tier. She marks the proxy and the jump host as trust-boundary controls. The fare-payment segment is drawn on a separate page with a note "out of scope". Northpoint's testers use the sketch to plan which logs they will request.

> **Synthetic case.** The architecture sketch and its components are invented.

### Errors and limits

Pretty diagrams that invent systems the organisation does not have waste time. Depth is not "more tools"; it is independent failure modes.

### Exercises

- **EX022 — Boundary mark.** On Priya's sketch, name two trust boundaries and one control at each. *Rubric:* 3 = two distinct boundaries with matching controls (e.g. internet→proxy TLS/auth; VPN→jump host MFA); 2 = one complete; 1 = vague; 0 = none.
- **EX023 — Shared failure.** The VPN, portal and database all accept the same Active Directory password with no MFA. Why is that not three layers? *Rubric:* 3 = one credential store/one secret; compromise of that secret defeats all three; 2 = shared password noted; 1 = still three layers; 0 = none.
- **EX024 — Evidence place.** Where would Priya look first for evidence that a staff VPN login occurred at 02:00? *Rubric:* 3 = VPN/authentication logs (identity evidence); 2 = vague logs; 1 = database; 0 = none.

### Synthesis

Draw the boundaries, check that layers fail independently, and collect evidence from the place the control actually lives.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) write a chain-of-custody note for a digital artefact; (2) compute and verify a SHA-256 manifest; (3) explain why measurement needs a defined unit and a defined time window; (4) refuse to keep engagement evidence on personal devices.

### 9.1 Evidence is a claim's support

A finding without evidence is an opinion. Evidence can be a configuration export, a redacted screenshot, a log excerpt or a hash of a file. Capture only what proves the point; more data means more retention risk and more redaction work.

In ENG-712 the claim about the portal banner enters the report because E-001 has a matching digest. An opinion about the banner without that file is deleted in peer review. Priya captures evidence only on authorised systems and masks staff local parts before filing, so the evidence proves the point without adding retention risk.

### 9.2 Chain of custody

For each item record who collected it, when, from where, and every hand-off. NIST SP 800-86 describes integrating forensic techniques into incident response; the same discipline of labelling and integrity checking applies to assessment evidence even when the legal stakes are lower.

Custody lines for ENG-712 name who exported E-001, when, and from which host. Hand-offs to Jordan as evidence owner are logged. NIST SP 800-86 habits transfer even when the case is synthetic. A missing custody line blocks the board-pack export even when the hash matches.

### 9.3 Hashing as a tamper check

A SHA-256 digest of an artefact, stored separately from the artefact, lets a later reader detect silent edits. If the digest no longer matches, the file changed — intentionally or not — and the claim that relied on it must be revisited.

The lab shows E-001 MATCH and E-002 MISMATCH. The mismatch stopped a claim about a wiki password until the export was taken again under two-person review. Digests are stored beside the evidence files rather than only in a ticket thread that anyone can edit, so a later reader can still check them.

### Lab C — evidence manifest

```python
"""Lab C (ch 09): build a SHA-256 evidence manifest for synthetic artefacts and detect tampering."""
import hashlib
artefacts = {
    "E-001_portal_login_banner.txt": b"TRT staff portal - authorised users only\n",
    "E-002_wiki_page_export.txt": b"Runbook draft v3 (synthetic)\n",
}
manifest = {name: hashlib.sha256(data).hexdigest() for name, data in artefacts.items()}
for name, h in manifest.items():
    print(f"{h[:16]}...  {name}")
artefacts["E-002_wiki_page_export.txt"] = b"Runbook draft v4 (synthetic)\n"  # simulated later edit
for name, data in artefacts.items():
    ok = hashlib.sha256(data).hexdigest() == manifest[name]
    print(name, "MATCH" if ok else "MISMATCH")
```

Run with `python3 lab_hash.py`. Verified output:

```text
3b5ca57a4755e156...  E-001_portal_login_banner.txt
ce711fb5a92e12ef...  E-002_wiki_page_export.txt
E-001_portal_login_banner.txt MATCH
E-002_wiki_page_export.txt MISMATCH
```

### 9.4 Measurement needs units

"We scanned a lot" is not a measure. "Seven ATT&CK techniques exercised between 22:00 and 05:00; three alerted, two logged, two missed" is a measure. Chapter 19 builds a coverage matrix; this chapter only insists that numbers have units and windows.

ENG-712's purple slide uses exactly those counts for seven techniques. A coverage percentage without units or a window would invite the CISO to compare numbers that mean different things. With counts per category, the investment conversation can start from the two missed techniques and ask what log source or alert would close each gap.

### Worked example

Priya hashes two synthetic exports before filing them. Later someone "updates" the wiki export. The manifest check prints MISMATCH for that file and MATCH for the untouched banner. She treats the wiki export as unreliable until a fresh copy is taken under custody.

> **Synthetic case.** The two artefacts and the later edit are invented for the lab.

### Errors and limits

Hashes detect change; they do not prove the original was true. Personal chat apps and personal laptops are not evidence stores.

### Exercises

- **EX025 — Manifest result.** Using the lab output, which file mismatched and what does that mean for a finding that cited it? *Rubric:* 3 = E-002 wiki export; finding evidence must be re-collected or the finding paused; 2 = names file; 1 = ignore mismatch; 0 = none.
- **EX026 — Custody line.** Write a one-line custody entry for the portal banner export. *Rubric:* 3 = who, what, when, from where; 2 = two fields; 1 = vague; 0 = none.
- **EX027 — Personal laptop.** May Priya keep a copy of TRT evidence on her home laptop overnight? *Rubric:* 3 = no; approved repository only under the agreement; 2 = no; 1 = yes if encrypted; 0 = none.

### Synthesis

Minimise, label, hash, measure with units, and never park evidence on personal devices.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Authorized offensive security and red team: orientation

### Learning outcomes

You will (1) place vulnerability assessment, penetration testing and red teaming on a single life cycle; (2) name the documents that create permission; (3) explain the roles of red, blue and purple teams; (4) state the educational boundary of this book in your own words.

### 10.1 A life cycle, not a tool list

Authorized practice moves through governance and scoping, rules of engagement, execution within those rules, evidence handling, risk rating, reporting, remediation and validation. Tool names change; the life cycle does not. NIST SP 800-115 and PTES both organise work this way, even though their part titles differ.

Priya teaches the path from governance through scope, ROE, execution, evidence, rating and reporting to retest. In training runs, students who skipped straight to scanners produced a STOP for fare-system interaction. Northpoint is graded on how well it followed the life cycle before anyone looks at how clever its findings were.

### 10.2 Permission is written

Permission comes from a signed agreement that names the parties, the systems, the methods, the window, the exclusions, the data-handling rules, the emergency contact and the report audience. Verbal "go ahead" is not enough. Chapter 11 turns that agreement into checkable scope and ROE objects.

ENG-712's signed pack names the parties, systems, methods, window, exclusions, retention period, emergency contact and white-team phone number. An empty emergency contact cancels the Saturday start, exactly as the ROE labs teach. Retention and the white-team phone are checked in the same pass, because each one is needed before any activity begins.

### 10.3 Red, blue and purple

The red team (or testing provider) exercises adversary behaviours under authorization. The blue team (SOC and defenders) detects and responds. Purple teaming is structured collaboration: red announces or reveals techniques in a controlled way so blue can improve detection, with learning as the goal rather than a pure "gotcha". TIBER-EU and CBEST add a threat-intelligence-led layer used in financial-sector assurance; technologists should recognise those names even when their organisation is not a bank.

Red (Northpoint) exercises behaviours; blue (TRT SOC) detects; purple replays misses into DET-19 and DET-20. Priya refuses engagements that omit a reachable white team. Learning is a deliverable, not a soft extra.

### 10.4 What this book will not do

It will not provide exploit code, payloads or step-by-step attack procedures. It will not authorize anyone to test a real system. It teaches governance, evidence, measurement and remediation validation on synthetic data so that when a learner later joins a real team, the discipline is already in place.

No exploit code, no live authorization, no fare "just this once". Chapter 10's boundary is what Priya quotes when a panel asks for T1552.001 steps — she points at ATT&CK and stops. The refusal is practised in panel drills, not left as theory.

### Worked example

TRT's CISO asks whether they "need a red team". Priya asks which decision the result will support. The CISO wants to know whether the SOC would notice a realistic intruder. That is a purple-capable red-team question, not a vulnerability scan. Priya proposes a scoped exercise with a white-team stop authority, a written ROE and a learning review — and notes that fare-payment stays excluded.

> **Synthetic case.** The CISO conversation is invented for orientation.

### Errors and limits

Buying a "red team" product that is actually a scan wastes money and creates false assurance. Framework names on a slide are not the same as following their phases.

### Exercises

- **EX028 — Decision first.** Rewrite the CISO's need as a one-sentence assessment objective. *Rubric:* 3 = objective about SOC detection of a realistic intruder under a scoped exercise; 2 = vague objective; 1 = "run tools"; 0 = none.
- **EX029 — Document list.** Name five fields a signed agreement must contain before testing starts. *Rubric:* 3 = five from scope/exclusions/methods/window/emergency contact/data handling/report audience/parties; 2 = three; 1 = one; 0 = none.
- **EX030 — Purple goal.** In one sentence, what makes an exercise "purple" rather than purely competitive red-versus-blue? *Rubric:* 3 = structured collaboration aimed at improving detection/response, not only scoring a breach; 2 = collaboration mentioned; 1 = more tools; 0 = none.

### Synthesis

Start from the decision, write the permission, know the roles, and keep this curriculum on the defensive side of the line.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Authorized offensive security and red team: assets and context

### Learning outcomes

You will (1) turn a signed agreement into a machine-checkable scope and ROE; (2) reject planned activities that fall outside the window or the stop list; (3) explain why asset context (owner, criticality, fragility) changes method choice; (4) keep a white-team contact reachable.

### 11.1 From prose to objects

An agreement written in paragraphs becomes useful when it is also a list: in-scope prefixes and names, excluded systems, allowed activities, start and end times, forbidden activities, and an emergency contact. Checkers in Chapter 2 and in this chapter operate on those lists. Ambiguous prose such as "and related systems" is a defect, not a feature.

Prose agreements become loadable lists for lab_scope and lab_roe checkers. If a field cannot be parsed, ENG-712 does not start. Priya maintains both the narrative ROE and the machine lists.

### 11.2 Context changes the method

A high-criticality, fragile asset may be examined by configuration review only. A low-criticality staging clone may accept more active checks. The asset record from Chapter 1 supplies that context; ignoring it produces either reckless testing or wasted caution.

At TRT the fragile production portal stays on configuration review, while a labelled staging clone may receive inventory scans. The criticality field on the asset record makes that choice, not a tester's preference on the day. Recording the choice in the ROE means a reviewer can later see why the two systems were treated differently.

### 11.3 Stop lists and windows

A stop list names activities that are never allowed even inside the window — for TRT, fare-system interaction and social engineering of drivers. A window names when allowed activities may run. Both are hard gates.

In the lab output a VPN review at 06:10 returns STOP because the window ends at 05:00. In studio, stop-list drills use a fake fare hostname that must produce HOLD or STOP rather than curious traffic. Both gates are checked before each action, so an allowed method at the wrong time is still refused.

### Lab D — ROE activity checker

```python
"""Lab D (ch 11): check synthetic planned activities against the rules-of-engagement window and stop list."""
from datetime import datetime
WINDOW = (datetime(2026, 11, 3, 22, 0), datetime(2026, 11, 4, 5, 0))
FORBIDDEN = {"denial-of-service", "social engineering of drivers", "fare-system interaction"}
plan = [
    ("2026-11-03 22:30", "external service inventory"),
    ("2026-11-04 04:45", "portal authentication review"),
    ("2026-11-04 06:10", "VPN configuration review"),
    ("2026-11-03 23:00", "fare-system interaction"),
]
for when, act in plan:
    t = datetime.strptime(when, "%Y-%m-%d %H:%M")
    if act in FORBIDDEN:
        status = "STOP: forbidden activity"
    elif not (WINDOW[0] <= t <= WINDOW[1]):
        status = "STOP: outside window"
    else:
        status = "allowed"
    print(f"{when}  {act:32} {status}")
```

Run with `python3 lab_roe.py`. Verified output:

```text
2026-11-03 22:30  external service inventory       allowed
2026-11-04 04:45  portal authentication review     allowed
2026-11-04 06:10  VPN configuration review         STOP: outside window
2026-11-03 23:00  fare-system interaction          STOP: forbidden activity
```

### 11.4 White team

Someone with stop authority must be reachable throughout the window. If that person cannot be reached, the session does not start. TIBER-EU-style exercises formalise this as a white-team control function; smaller engagements still need the same idea.

White-team silence means no start: if the on-call contact does not answer, the tools stay idle and the VPN review waits. TIBER-style control functions are borrowed as an idea even though TRT is not a bank. During ENG-712 only the named liaison pages the white team; side chats do not.

### Worked example

Northpoint's draft plan includes a VPN review at 06:10 and a "fare-system interaction" at 23:00. The lab prints STOP for both — one outside the window, one forbidden. Priya cancels those lines before kickoff and keeps the two allowed activities.

> **Synthetic case.** The plan lines and the 22:00–05:00 window are fictional TRT ROE objects.

### Errors and limits

A checker cannot invent missing exclusions. If the agreement is silent, ask; do not assume.

### Exercises

- **EX031 — Two stops.** Quote the two STOP lines from the lab and the reason for each. *Rubric:* 3 = VPN review outside window; fare-system interaction forbidden; 2 = one correct; 1 = both allowed; 0 = none.
- **EX032 — Fragile context.** The timetable API is marked fragile. Which method change belongs in the ROE? *Rubric:* 3 = throttle/limit or switch to config review; written in ROE; 2 = vague caution; 1 = ignore; 0 = none.
- **EX033 — Unreachable white team.** On the morning of the window the on-call white-team contact does not answer. What happens? *Rubric:* 3 = do not start; escalate to CISO/named deputy; restart only when contact confirmed; 2 = delay; 1 = start anyway; 0 = none.

### Synthesis

Scope and ROE are lists you can check; context chooses the method; no reachable white team means no start.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Authorized offensive security and red team: data flows

### Learning outcomes

You will (1) draw a data-flow diagram for one TRT service; (2) mark where assessment evidence and personal data may appear; (3) apply data-minimisation and redaction rules; (4) choose storage and retention that match the agreement.

### 12.1 Flows, not boxes

A data-flow diagram shows what moves: a passenger request to the timetable API, a staff login to the portal, a log line to the SIEM, a backup to storage. Boxes alone do not reveal where copies of sensitive data land. Assessments that touch those paths can create new copies; the agreement must say what happens to them.

For ENG-712 Priya draws the passenger-to-API and staff-to-portal-to-SIEM flows before the engagement starts. Any finding that relies on log evidence then cites the flow it came from, and each flow is checked for personal data before the evidence design is approved. A diagram of boxes without arrows would hide exactly the retention duties that apply when a log line is copied into the evidence vault.

### 12.2 Personal and operational data

Even a transit operator holds personal data — staff identifiers, sometimes passenger account details on adjacent systems. Operational data such as driver rosters and maintenance schedules can also be sensitive. Capture the minimum that proves a finding; mask the rest before filing.

In ENG-712 login screenshots keep the staff email domain as proof but have the local part masked before they enter the vault. Roster extracts are treated as sensitive even though they are not classic personal data, because they reveal who works where and when. Both kinds of evidence run on the same 90-day retention clock as the service banners.

### 12.3 Cross-border and vendor paths

If logs are shipped to a vendor SIEM in another country, evidence may leave the jurisdiction the agreement assumed. Note the path before the engagement; do not discover it in the report draft.

Priya names any cross-border SIEM path in the agreement before the first log is shipped, treating it like a host that needs scoping. If the vendor announces mid-window that it has moved regions, log shipping pauses and a decision meeting is held. She will not invent consent for a transfer that the signed agreement never contemplated.

### 12.4 Retention clocks

Start a retention clock when evidence is collected. When the agreement's period ends, delete or return the data and record that you did. Indefinite "just in case" stores are a liability.

ENG-712 runs a 90-day clock that ends with delete or return and a written destruction record naming who deleted the evidence and when. The record is hashed into the handoff pack next to the access-control change on the vault. Keeping copies for training would need a new agreement; without one, the handoff checklist fails.

### Worked example

Priya maps the staff-portal login: browser → reverse proxy → portal app → directory; and a parallel flow portal app → application log → SIEM. A screenshot of a failed login shows a staff email address. She masks the local part before filing, keeps the domain to prove it was a staff account, and stores the file under ENG-712 with a 90-day retention note from the agreement.

> **Synthetic case.** The login flow and the masked screenshot are invented.

### Errors and limits

Redaction that leaves the secret recoverable (cropping that still shows the password in EXIF, for example) is not redaction. This chapter does not cover legal regimes in detail; follow your counsel and the agreement.

### Exercises

- **EX034 — Extra copy.** Name one place a timetable API request might be copied besides the application server, and why an assessor cares. *Rubric:* 3 = e.g. reverse-proxy logs / SIEM / CDN / WAF — each is a potential evidence and retention location; 2 = names place; 1 = nowhere; 0 = none.
- **EX035 — Masking choice.** A screenshot shows staff email `alex.rivera@trt.example`. What does Priya keep and what does she mask? *Rubric:* 3 = mask local part; keep domain or role marker to prove staff context; 2 = mask all; 1 = keep full address; 0 = none.
- **EX036 — Retention end.** ENG-712's agreement says 90 days. What two actions close the clock? *Rubric:* 3 = delete or return evidence + record the destruction/return; 2 = one action; 1 = keep forever; 0 = none.

### Synthesis

Follow the copies, minimise and mask, and close the retention clock in writing.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Authorized offensive security and red team: risk scenarios

### Learning outcomes

You will (1) rate findings with a transparent likelihood × impact matrix; (2) sort a finding list for remediation order; (3) write a short risk scenario that ties asset, technique and consequence; (4) separate severity of a weakness from urgency of a ticket.

### 13.1 Transparent rating

A 1–5 likelihood and 1–5 impact scale, multiplied, gives a score that anyone can recompute. Bands such as critical ≥ 20, high ≥ 12, medium ≥ 6, low ≥ 0 turn scores into language managers recognise. Document the scale in the report so readers are not guessing.

F-09 shows the arithmetic: likelihood 4 times impact 5 gives 20, which falls in the critical band. Priya prints that calculation in the report appendix so a director can recompute it in seconds. A score that cannot be recomputed invites argument about the tester's judgement instead of discussion of the risk, and review rejects it.

### 13.2 Scenarios connect the dots

"Shared admin account on the staff portal" is a weakness. The scenario adds: an adversary using T1078 Valid Accounts could alter public timetables (integrity) and lock out operators (availability). Scenarios make impact scores defensible.

In ENG-712 this sentence sits under F-01, linking the shared admin account to T1078 and to the integrity of public timetables. That link explains why the CISO should care before the weekend service change rather than after it. High findings without a scenario sentence are rewritten before the report builder produces the executive table.

### 13.3 Severity versus urgency

A critical finding on a decommissioned staging host may be low urgency. A medium finding on a system under active attack may be high urgency. Tickets carry both fields; collapsing them into one number loses information.

Priya runs a weekly triage sort with owners that orders tickets by urgency first. A medium finding on a system being actively abused can therefore move ahead of a critical one on a staging host that is about to be switched off. Owners see both values on the ticket, so the order is explained rather than mysterious.

### Lab E — finding scorer

```python
"""Lab E (ch 13): rate synthetic findings with a 1-5 likelihood x impact matrix and sort them."""
BANDS = [(20, "critical"), (12, "high"), (6, "medium"), (0, "low")]
findings = [
    ("F-01", "shared admin account on staff portal", 4, 4),
    ("F-04", "verbose error page on timetable API", 3, 1),
    ("F-07", "unreviewed VPN accounts of ex-contractors", 3, 5),
    ("F-09", "wiki page with plaintext service password", 4, 5),
]
def band(s):
    return next(name for floor, name in BANDS if s >= floor)
for fid, title, lik, imp in sorted(findings, key=lambda f: -(f[2] * f[3])):
    s = lik * imp
    print(f"{fid} L{lik} x I{imp} = {s:2d} {band(s):8} {title}")
```

Run with `python3 lab_score.py`. Verified output:

```text
F-09 L4 x I5 = 20 critical wiki page with plaintext service password
F-01 L4 x I4 = 16 high     shared admin account on staff portal
F-07 L3 x I5 = 15 high     unreviewed VPN accounts of ex-contractors
F-04 L3 x I1 =  3 low      verbose error page on timetable API
```

### 13.4 NIST language

NIST SP 800-30 Rev. 1 describes risk as a function of threat, vulnerability and impact (among other framings). The classroom matrix is a simplification for ordering work, not a full enterprise risk assessment.

Priya puts the citation to SP 800-30 under the matrix figure, labelling the 1 to 5 scale as a classroom simplification of its ideas. Examiners can then see where the approach comes from and what it leaves out, such as threat-source analysis. Nobody reading the report should think TRT has invented its own theory of risk.

### 13.5 Communicating scores upward

When Priya presents the ordered list, she spends more time on the top two scenarios than on the low finding. Boards can absorb a handful of well-narrated risks; they cannot absorb a spreadsheet dump. She keeps the full table in an appendix for auditors and puts three sentences in the executive summary: what matters, why, and what decision she needs this week. In ENG-712's oral summary F-09 and F-01 lead, while the low verbose-error finding gets a single line.

### Worked example

Four TRT findings enter the scorer. The wiki plaintext password (T1552.001 Credentials In Files) tops the list at 20 critical. The verbose timetable error page scores 3 low. Priya presents the ordered list to the remediation board with one-sentence scenarios attached.

> **Synthetic case.** The four findings and their scores are invented.

### Errors and limits

Do not invent likelihood numbers without a reason. CVSS (see FIRST CVSS v4.0) scores vulnerabilities; organisational risk also needs context the matrix must state.

### Exercises

- **EX037 — Top of list.** Which finding does the lab rank first, and what is its band? *Rubric:* 3 = F-09 critical (score 20); 2 = F-09 only; 1 = wrong finding; 0 = none.
- **EX038 — Scenario sentence.** Write a one-sentence risk scenario for F-07 (ex-contractor VPN accounts). *Rubric:* 3 = asset + technique/actor path + consequence to CIA; 2 = two of three; 1 = restates title; 0 = none.
- **EX039 — Urgency split.** F-04 is low severity on a production API that is currently being probed from the internet. What urgency do you assign and why? *Rubric:* 3 = raised urgency despite low severity because of active probing; 2 = raised without reason; 1 = ignore probing; 0 = none.

### Synthesis

Score transparently, narrate the scenario, and keep severity and urgency as separate dials.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Authorized offensive security and red team: methods I

### Learning outcomes

You will (1) map engagement phases to NIST SP 800-115 and PTES; (2) choose review versus validation techniques based on risk; (3) write a method statement that a ROE can quote; (4) keep technique descriptions at the ATT&CK ID level without operational detail.

### 14.1 Two maps of the same journey

NIST SP 800-115 groups techniques into review, target identification and analysis, and target vulnerability validation, wrapped by planning and post-testing activities. PTES names pre-engagement, intelligence gathering, threat modelling, vulnerability analysis, exploitation, post-exploitation and reporting. A technologist does not need to memorise every subsection; they need to place each planned activity in a phase and know which document the client prefers.

SP 800-115 and PTES name stages; Priya maps ENG-712 activities onto both so Northpoint and auditors share vocabulary. Threat-led extras sit on top of scoping discipline, not instead of it.

### 14.2 Review before validation

Configuration review, document review and log review often answer the question with less operational risk than active validation. Use validation when the decision truly needs confirmation that a weakness is reachable under the agreed limits — and only then.

For the staff portal, reviewing the authentication configuration answered the MFA question with far less risk than any password experiment. Active validation is kept for cases where the CISO's decision depends on proof that a weakness can actually be reached under the ROE. A request for such validation needs a one-line decision statement before any active check runs.

### 14.3 Method statements

A method statement is a short, non-procedural description: "External service inventory of in-scope prefixes using approved scanners at agreed rates; authentication configuration review of the staff portal; no denial-of-service, no fare-system interaction, no social engineering." It belongs in the ROE.

ENG-712's statement stays at that level: inventory at agreed rates, review of portal authentication, and the three exclusions. Step-by-step exploit instructions belong neither in this book nor in the engagement deliverables. On the peer rubric, any dual-use detail in a method statement fails the safety criterion however complete the rest of the package is.

### 14.4 ATT&CK at ID level

Refer to behaviours as T1595 Active Scanning, T1046 Network Service Discovery, T1078 Valid Accounts. Do not expand them into how-to steps. Defenders can open the ATT&CK pages; attackers do not need this book.

Every deliverable links to the ATT&CK technique pages instead of pasting procedure text. Expanding these identifiers into recipes would break the educational boundary set in Chapter 10. A defender who needs more detail can follow the link, and the report stays useful to the SOC without becoming a manual for an attacker.

### Worked example

Priya drafts the method statement for TRT's November window. Planning and ROE cite SP 800-115 planning controls. Execution lists inventory (identification) and authentication review (validation of a control's effectiveness). Reporting and remediation validation close the loop. The statement never describes how to bypass authentication.

> **Synthetic case.** The November method statement is invented for TRT.

### Errors and limits

Copying a method list from a vendor datasheet without matching it to scope produces unauthorized activity. "Exploitation" in PTES is a phase name, not a licence for uncontrolled attacks.

### Exercises

- **EX040 — Phase placement.** Place "authentication configuration review of the staff portal" into an SP 800-115 technique family and a PTES phase. *Rubric:* 3 = review or validation (SP) + vulnerability analysis or equivalent PTES phase, with brief reason; 2 = one correct; 1 = wrong; 0 = none.
- **EX041 — Method sentence.** Write a one-sentence method statement for inventory of TRT's in-scope prefixes that includes a hard limit. *Rubric:* 3 = inventory + in-scope only + rate/window/exclusion limit; 2 = inventory only; 1 = unlimited scan; 0 = none.
- **EX042 — ID only.** Why does the book cite T1046 by ID rather than describing scanning steps? *Rubric:* 3 = defensive mapping without teaching attack procedures; 2 = brevity; 1 = because steps are secret; 0 = none.

### Synthesis

Name the phase, prefer review when it answers, write the method as limits plus intent, and stop at the technique ID.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Authorized offensive security and red team: guided lab

### Learning outcomes

You will (1) run a three-gate pipeline that admits an action only when target, time and activity all pass; (2) maintain an operator log of admitted actions; (3) explain why a HOLD is a success, not a failure; (4) hand the log to a reviewer as evidence of discipline.

### 15.1 Three gates

Every planned action has a target address, a timestamp and an activity name. The target must sit in the in-scope prefix, the timestamp inside the window, and the activity on the approved list. Fail any gate and the action does not proceed.

In the Lab F output A2 is held on the activity gate and A3 on the target gate, so neither reaches the operator log. Priya screenshots both HOLD lines into the training notes, because for ENG-712 the gates are the product and improvisation is the defect.

### 15.2 The operator log

Only actions that pass all three gates are written to the operator log. The log is evidence that the team stayed inside the agreement. A log full of improvisation is a finding against the testing team itself.

In the lab only A1 and A4 pass all three gates, so they are the only entries in the operator log. Priya reviews the log before the CISO session and compares it with the chat history. Any action that appears in chat but not in the log is a shadow action and becomes a process finding against Northpoint.

### Lab F — guided pipeline

```python
"""Lab F (ch 15): guided pipeline - an action is logged only if target, time and activity all pass."""
import ipaddress
from datetime import datetime
scope = ipaddress.ip_network("192.0.2.0/25")
window = (datetime(2026, 11, 3, 22, 0), datetime(2026, 11, 4, 5, 0))
approved = {"service inventory", "authentication review", "configuration review"}
actions = [
    ("A1", "192.0.2.12", "2026-11-03 22:15", "service inventory"),
    ("A2", "192.0.2.12", "2026-11-03 22:40", "password spraying"),
    ("A3", "192.0.2.140", "2026-11-03 23:05", "configuration review"),
    ("A4", "192.0.2.30", "2026-11-04 01:20", "authentication review"),
]
log = []
for aid, ip, when, act in actions:
    checks = {
        "target": ipaddress.ip_address(ip) in scope,
        "time": window[0] <= datetime.strptime(when, "%Y-%m-%d %H:%M") <= window[1],
        "activity": act in approved,
    }
    failed = [k for k, ok in checks.items() if not ok]
    print(aid, "PROCEED" if not failed else "HOLD (" + ",".join(failed) + ")")
    if not failed:
        log.append(aid)
print("operator log entries:", log)
```

Run with `python3 lab_pipeline.py`. Verified output:

```text
A1 PROCEED
A2 HOLD (activity)
A3 HOLD (target)
A4 PROCEED
operator log entries: ['A1', 'A4']
```

### 15.3 HOLD is a feature

A2 is held because "password spraying" is not an approved activity. A3 is held because the target is outside the /25. Those HOLDs protect TRT and Northpoint. Celebrating a HOLD in the debrief teaches juniors that restraint is professional.

Debriefs give HOLDs and fare-payment STOPs the same recognition as findings. Studio grades award points for documented HOLDs that prevented out-of-scope or out-of-window work. Juniors who hide a HOLD to look productive fail the studio grade, because hiding it removes the evidence that the gates worked.

### 15.4 Reviewer use

A reviewer should be able to replay the gates against the log. If an entry appears that would not pass, the engagement has a process failure regardless of whether anything "interesting" was found.

Peer review of ENG-712 training packs includes running the gate checks again on every log entry. If an entry would have been held, the engagement records a process failure even when the related finding looks impressive. Process is graded beside findings, so a strong result cannot hide a log the gates would have rejected.

### Worked example

Four candidate actions enter the pipeline. A1 and A4 proceed; A2 and A3 hold. The operator log contains only `['A1', 'A4']`. Priya attaches that printout to the engagement records before the night shift ends.

> **Synthetic case.** The four actions and the pipeline results are invented for the guided lab.

### Errors and limits

The pipeline does not replace human judgement about fragility or ongoing incidents; it only enforces the three hard gates. Soft concerns still need a person.

### Exercises

- **EX043 — Hold reasons.** Why do A2 and A3 hold, according to the lab? *Rubric:* 3 = A2 activity not approved; A3 target out of scope; 2 = one correct; 1 = both proceed; 0 = none.
- **EX044 — Log contents.** What does the operator log contain after the run, and why is that list evidence? *Rubric:* 3 = ['A1','A4']; proves only gated actions were performed; 2 = names list; 1 = includes holds; 0 = none.
- **EX045 — Soft concern.** The timetable API is fragile but A4's target and activity are allowed. What extra step should a human take? *Rubric:* 3 = apply ROE throttle/fragility note or switch method; confirm with white team if unsure; 2 = vague caution; 1 = ignore; 0 = none.

### Synthesis

Three hard gates, a log of only what passed, and human judgement still applied on top.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Authorized offensive security and red team: methods II

### Learning outcomes

You will (1) contrast web-application testing literacy (OWASP WSTG) with network-focused methods; (2) explain what threat-led frameworks (TIBER-EU, CBEST) add; (3) choose a method mix for a transit operator that is not a bank; (4) write exclusion language that survives contact with reality.

### 16.1 OWASP WSTG as a catalogue

The OWASP Web Security Testing Guide organises checks for web applications: configuration, identity, input handling, business logic and more. A technologist uses it as a coverage checklist for the staff portal and timetable API, not as a licence to run every check. Each selected check still needs a ROE line.

For ENG-712 Priya marks which WSTG areas were run against the staff portal and which against the timetable API, and which were deliberately left out. That record is what gives a coverage statement its meaning for readers. A report that just says the team followed WSTG cannot tell a reader whether business-logic checks on the API were done or skipped.

### 16.2 Threat-led assurance

TIBER-EU and CBEST describe intelligence-led exercises used especially in financial-market infrastructure. They add a threat-intelligence phase, a white-team control function and a learning-focused replay. TRT is not a bank, but borrowing the white-team and learning-review ideas improves any red-team exercise.

TIBER/CBEST ideas — intel, white team, learning replay — are borrowed cautiously for TRT. Priya does not claim CBEST compliance for a bus operator. She claims white-team reachability and purple tickets, and her slides say explicitly that borrowing these ideas does not let TRT claim bank-style compliance.

### 16.3 Mixing methods without mixing scopes

A single engagement can include a WSTG-informed portal review and a limited network inventory, provided both sit inside the same agreement and exclusions. Mixing in an unstated "quick look" at fare-payment systems violates the agreement even if the method is gentle.

The ENG-712 agreement holds both the portal review and the network inventory, with the same exclusions applying to each. A quiet look at a fare-payment host would still be contact with an excluded system, and the scope checker would return STOP for it. Scope creep is treated as a stop condition, never as a stretch goal for a quiet afternoon.

### 16.4 Exclusion language that works

"Fare-payment systems, including hosts in 192.0.2.64/27 and any hostname under fare.trt.example, are excluded from all activities." This beats "sensitive systems are out of scope", which nobody can check.

The precise version can be loaded straight into the scope checker, which can then return STOP for any address in 192.0.2.64/27 or any name under fare.trt.example. Peer review rejects vague exclusion wording because no tool and no reviewer can test against it. At kickoff, checkable exclusion strings are a gate as firm as having an emergency contact on the ROE.

### Worked example

Priya proposes for next quarter: WSTG-informed configuration and identity checks on the staff portal; inventory of in-scope prefixes; a half-day purple replay of T1078 and T1133 with the SOC. Fare-payment stays excluded by prefix and by hostname pattern. The CISO accepts the mix because each piece maps to a decision.

> **Synthetic case.** The quarterly mix is a fictional planning artefact.

### Errors and limits

Name-dropping TIBER-EU without a threat-intelligence provider or white team is theatre. WSTG coverage percentages without severity context mislead boards.

### Exercises

- **EX046 — Borrowed practice.** Name two TIBER-EU/CBEST ideas TRT can borrow without being a bank. *Rubric:* 3 = white-team control + learning/replay review (or TI-led scenario design); 2 = one; 1 = full CBEST certification claim; 0 = none.
- **EX047 — Exclusion rewrite.** Improve "sensitive systems are out of scope" for TRT's fare segment. *Rubric:* 3 = names prefix and/or hostname pattern and "all activities"; 2 = names systems vaguely; 1 = leaves original; 0 = none.
- **EX048 — WSTG selection.** Why might Priya select identity checks and skip intrusive business-logic fuzzing on the first portal engagement? *Rubric:* 3 = risk/fragility/ROE limits / decision needs; 2 = vague caution; 1 = always run everything; 0 = none.

### Synthesis

Pick catalogues for coverage, borrow white-team discipline from threat-led frameworks, and write exclusions a script can check.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Authorized offensive security and red team: tooling

### Learning outcomes

You will (1) inventory assessment tools with owner, purpose and data handled; (2) apply a change-control note before upgrading a tool mid-engagement; (3) explain supply-chain risk for assessment tooling; (4) keep classroom labs on the Python standard library.

### 17.1 Tools are in scope of governance

Anything that touches client systems or client data is part of the engagement's attack surface — including the tester's own laptop and scanners. An inventory lists each tool, who maintains it, what data it stores, and whether it may leave the approved environment.

For ENG-712 each laptop and scanner gets an inventory row that records disk encryption and how long any local evidence cache is kept. Evidence held on a tester's machine runs on the same retention clock as evidence in the vault. A lost laptop follows the same incident path as a lost badge, because either one can expose client data.

### 17.2 Change control mid-flight

Upgrading a scanner halfway through a window can change its behaviour and invalidate comparisons. Note the version at kickoff; defer upgrades unless the white team agrees that a security fix in the tool itself requires it.

Pinned versions protect the before and after comparisons in purple-team work: if the scanner changes between runs, a difference in results might come from the tool rather than the client's controls. When a security fix in the tool itself cannot wait, the white team initials the upgrade, and the initials are stored next to the version pin in the log.

### 17.3 Supply chain of tools

Assessment software comes from vendors and open-source projects. Prefer signed releases, verify checksums when provided, and avoid random scripts from the internet. ATT&CK T1195 Supply Chain Compromise is usually discussed as an adversary technique against the client; it applies to the testing team too.

Priya verifies checksums before the window opens, and the step is a line on the kickoff checklist. A script found online that claims only to parse JSON is still refused if it is unsigned and unreviewed, because it would run on a machine holding client evidence. A compromised testing tool could do exactly the harm that T1195 describes for clients.

### 17.4 Classroom constraint

Every lab in this book uses only the Python 3 standard library and synthetic data. That is intentional: learners practise decision logic without depending on commercial scanners or building attack tooling.

The constraint also keeps every lab reproducible on any machine with Python 3, without licences or network access. Commercial scanners may appear later at work, but they arrive through TRT's procurement and change control, with their own inventory rows and version pins. The decisions practised here, about gates, scope and evidence, carry over unchanged to those tools.

### Worked example

Northpoint's kit list for TRT names two inventory scanners (versions pinned), a note-taking vault, and the ROE checkers from this course. A junior suggests adding a new "credential checker" found online. Priya rejects it: no owner, no checksum, no change-control entry, and the ROE does not list credential-guessing activities.

> **Synthetic case.** The kit list and the rejected tool are invented.

### Errors and limits

A pinned old version with a known tool vulnerability is also a risk; plan upgrades between engagements. Personal cloud sync of tool output can leak evidence.

### Exercises

- **EX049 — Kit fields.** Name four fields every tool entry on the kit list should carry. *Rubric:* 3 = four of name/version/owner/purpose/data handled/approved environment; 2 = two; 1 = name only; 0 = none.
- **EX050 — Mid-window upgrade.** A scanner vendor releases a feature update on day two of the window. What is the default action? *Rubric:* 3 = defer; keep pinned version; upgrade only with white-team agreement if a security fix demands it; 2 = defer only; 1 = upgrade immediately; 0 = none.
- **EX051 — Random script.** Why refuse an untracked script that "just checks passwords"? *Rubric:* 3 = no owner/checksum + activity may be outside ROE + evidence/data handling unknown; 2 = one reason; 1 = allow if it works; 0 = none.

### Synthesis

Inventory the kit, pin versions, treat tool supply chain seriously, and keep teaching labs boring by design.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Authorized offensive security and red team: controls

### Learning outcomes

You will (1) map common assessment findings to control families in NIST SP 800-53 and CSF 2.0 language; (2) distinguish compensating controls from missing controls; (3) write a remediation recommendation that names a control, an owner and a check; (4) avoid promising "full security".

### 18.1 Controls as answers to findings

A finding is a gap; a control is how the organisation closes it. NIST SP 800-53 Rev. 5 provides control families (access control, audit and accountability, identification and authentication, and many others). NIST CSF 2.0 organises outcomes into Govern, Identify, Protect, Detect, Respond and Recover. Reports that recommend "be careful" help nobody; reports that recommend "enforce MFA on all VPN paths (IA-family control); owner: identity team; check: quarterly account review" create work.

Findings map to SP 800-53 families and CSF functions in the recommendation line. F-01 points at identity controls; missed T1021 points at detect/respond work. Owners see a control verb, not only a problem.

### 18.2 Compensating controls

If MFA cannot yet cover a legacy path, a compensating control might be a jump host with session recording and a shorter session timeout. Document the compensation and the plan to remove it. Assessors should test whether the compensation actually works, not merely whether it is written down.

Every compensation carries an end date and a retest hook, so it cannot quietly become permanent. Assessors check that the jump host really records sessions and that the shorter timeout really ends idle sessions, rather than accepting the design document. A compensation that is never revisited turns into an accepted risk without a named approver.

### 18.3 Detect and respond are controls too

Purple-team work often finds that Prevent failed but Detect also failed. Recommendations then land in the Detect and Respond functions: a new alert, a runbook step, a playbook link. D3FEND offers defensive technique vocabulary that can sit beside ATT&CK IDs in a mature programme.

When ENG-712 found that both prevention and detection failed for a technique, the result was a DET ticket and a runbook step rather than advice to monitor more. D3FEND verbs make the recommendation specific enough for a detection engineer to act on and for a later exercise to retest. Each recommendation also names an owner, so it reaches someone who can act.

### 18.4 Forbidden assurance phrases

"Fully secure", "guaranteed", "hack-proof" and "100% coverage" are false and forbidden in TRT reports. Time-bounded, scope-bounded statements are the professional alternative.

TRT lists these phrases in the ROE appendix, so vendors cannot claim they did not know, and drafts containing them are returned until rewritten. The replacement statement for ENG-712 is bounded in time and scope, saying what was tested, in which window and within which limits. Review checks every draft for the listed phrases before the pack reaches the CISO, and a reviewer who finds one also checks the surrounding paragraph for an unbounded claim.

### Worked example

For F-07 (ex-contractor VPN accounts) Priya recommends: disable the three accounts within 48 hours (Protect / access control); institute a joiner-mover-leaver review every 90 days (Govern); add a SIEM alert for VPN logins from accounts with end-dated contracts (Detect). She refuses a vendor draft that called the VPN "fully secured after remediation".

> **Synthetic case.** The control recommendations are invented for TRT's F-07.

### Errors and limits

Control catalogues are large; pick the few that match the finding. Mapping every finding to twenty controls creates noise.

### Exercises

- **EX052 — Control triple.** For F-09 (plaintext password on wiki), write control + owner + check. *Rubric:* 3 = e.g. remove secret + secrets vault / wiki owner / scan or review check; 2 = two parts; 1 = "fix it"; 0 = none.
- **EX053 — Compensation.** Give one compensating control for a legacy VPN path that cannot yet do MFA. *Rubric:* 3 = concrete compensation (jump host, recording, short timeout, allow list) + temporary nature; 2 = vague extra monitoring; 1 = ignore; 0 = none.
- **EX054 — Forbidden phrase.** Rewrite "The portal is now hack-proof" as a professional sentence. *Rubric:* 3 = time/scope-bounded assurance without absolute claims; 2 = softer but still absolute; 1 = keeps hack-proof; 0 = none.

### Synthesis

Name the control, the owner and the check; allow temporary compensations; never sell absolute safety.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Authorized offensive security and red team: monitoring

### Learning outcomes

You will (1) build an ATT&CK coverage matrix from a purple-team log; (2) interpret alerted, logged and missed outcomes; (3) propose one detection improvement per missed technique; (4) keep the matrix scoped to the exercise.

### 19.1 Coverage as a conversation

A coverage matrix does not claim the organisation detects "everything". It shows, for the techniques exercised in a named window, whether the SOC alerted, merely logged, or missed. That conversation drives investment.

TRT's coverage slides open with the window dates and the list of techniques exercised, so the matrix cannot be read as a statement about everything. Any claim of universal detection is deleted in review, because seven techniques in one night cannot support it. Discussions about investment then use the three words alerted, logged and missed, which point directly to what needs to be built.

### 19.2 Alerted, logged, missed

Alerted means a person or playbook was notified in time to act. Logged means the telemetry existed but nobody was woken. Missed means the behaviour left no usable telemetry. Logged is not success if the exercise assumed a responding analyst.

SOC leaders sometimes read logged as partly working, so Priya explains it against the exercise goal. If the exercise assumed an analyst would respond, a technique that was only logged counts as a miss for that goal. It still opens a DET ticket, even though the telemetry existed, because nobody acted in time.

### Lab G — coverage matrix

```python
"""Lab G (ch 19): ATT&CK technique coverage matrix from a synthetic purple-team log."""
log = [
    ("T1078", "Initial Access", "alerted"), ("T1133", "Initial Access", "logged"),
    ("T1087", "Discovery", "missed"), ("T1069", "Discovery", "alerted"),
    ("T1021", "Lateral Movement", "missed"), ("T1213", "Collection", "logged"),
    ("T1567", "Exfiltration", "alerted"),
]
order = ["alerted", "logged", "missed"]
for tid, tactic, outcome in log:
    print(f"{tid:6} {tactic:17} " + " ".join("X" if o == outcome else "." for o in order))
n = len(log)
for o in order:
    k = sum(1 for _, _, x in log if x == o)
    print(f"{o:8} {k}/{n} = {100 * k / n:.1f}%")
```

Run with `python3 lab_coverage.py`. Verified output:

```text
T1078  Initial Access    X . .
T1133  Initial Access    . X .
T1087  Discovery         . . X
T1069  Discovery         X . .
T1021  Lateral Movement  . . X
T1213  Collection        . X .
T1567  Exfiltration      X . .
alerted  3/7 = 42.9%
logged   2/7 = 28.6%
missed   2/7 = 28.6%
```

### 19.3 From miss to backlog

Each missed technique becomes a backlog item: which log source, which alert logic, which owner, which test to prove it later. Tie the item to the ATT&CK ID so future exercises can retest the same cell.

DET-19 and DET-20 follow this pattern for T1021 and T1087: each names the log source, the alert logic, an owner and a retest plan. The ATT&CK tag lets the next purple cycle find the same cell. A miss recorded without a tag tends to land in the wrong queue and is never retested.

### 19.4 Navigator and D3FEND

ATT&CK Navigator visualises coverage layers. D3FEND names defensive techniques that can counter a given offensive technique. Together they help a technologist talk to both red and blue without inventing a private vocabulary.

Priya imports the set of techniques actually exercised in ENG-712 into Navigator rather than displaying a generic enterprise heat map. D3FEND links sit on the cells where a recommendation is made. A heat map that does not reflect the exercised set is rejected as decoration, because it suggests coverage nobody measured.

### 19.5 Retesting the same cells

A coverage matrix earns its keep only if the next exercise reopens the same cells. Priya tags DET-19 and DET-20 with T1021 and T1087 so the following purple cycle can print a before/after row. Without that discipline the organisation rediscovers the same misses and calls it a new insight.

Exercising new and interesting techniques does not excuse skipping the cells that missed last time. If those rows still show a miss, the backlog items are reopened with their owners.

### Worked example

TRT's purple log covers seven techniques. Three alerted (42.9%), two logged (28.6%), two missed (28.6%). The misses are T1087 Account Discovery and T1021 Remote Services. Priya opens two backlog tickets: directory audit logging to the SIEM for T1087, and jump-host session alerts for T1021.

> **Synthetic case.** The seven-technique log and percentages are invented.

### Errors and limits

A matrix from one exercise is not an enterprise maturity score. Do not hide misses to protect feelings; the learning is the product.

### Exercises

- **EX055 — Percentages.** Quote the three outcome percentages printed by the lab. *Rubric:* 3 = alerted 42.9%, logged 28.6%, missed 28.6%; 2 = two correct; 1 = one; 0 = none.
- **EX056 — Backlog item.** Write a backlog ticket title for the T1021 miss. *Rubric:* 3 = names T1021 + detection/alert goal + system (jump host/remote services); 2 = vague detection ticket; 1 = "try harder"; 0 = none.
- **EX057 — Logged ≠ done.** Why is a "logged" outcome for T1133 not enough if the exercise expected a responding analyst? *Rubric:* 3 = telemetry without notification/response fails the detect-and-respond goal; 2 = partial; 1 = logged is success; 0 = none.

### Synthesis

Measure what this exercise exercised, tell the truth about misses, and turn each miss into a named detection task.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Authorized offensive security and red team: troubleshooting

### Learning outcomes

You will (1) build a fault tree for a failed assessment session; (2) separate tooling faults, scope faults and environment faults; (3) write a go/no-go note after a mid-window incident; (4) keep troubleshooting notes as engagement evidence.

### 20.1 Sessions fail for boring reasons

DNS drift, an expired tester certificate, a SIEM collector down, a white-team phone on silent, a scope sheet with a typo — these stop work more often than exotic problems. A fault tree starts with "session cannot proceed" and branches into authorization, connectivity, tooling and safety.

Priya gives these ordinary faults the first thirty minutes of any stuck ENG-712 session: she checks that names still resolve to approved addresses, that tester certificates are valid, that the SIEM collector is receiving and that the white-team phone rings. Only when all four are healthy does the team look for anything unusual. Most stuck sessions end at the first or second check.

### 20.2 Three fault classes

Scope faults: the target is no longer approved. Tooling faults: the checker or scanner misbehaves. Environment faults: the client's system is unstable or an incident is already in progress. Mis-classifying an environment fault as a tooling fault leads to "trying again" when the right move is to stop.

Each class has a different owner: scope faults go to the white team, tooling faults to Northpoint's own kit lead and environment faults to TRT operations. Priya's go/no-go note names the class so that the right person is paged. Filing an environment fault as a tooling fault would have Northpoint retrying against a system that operations is trying to stabilise.

### 20.3 Go / no-go

After any unexpected event — a crash, a complaint, a SIEM outage — the team writes a short go/no-go note: what happened, which fault class, who was informed, decision, signature/time. No-go is a professional outcome.

During a SIEM outage, for example, the team pauses traffic and writes the note before sending anything more, because activity the SOC cannot see produces noise without evidence value. The note records the timestamp of the last technique that was observed normally. That timestamp keeps the purple-team counts honest when the session resumes.

### 20.4 Parallel incident

If TRT's SOC is already handling a real incident, assessment activity that adds noise is usually suspended. NIST SP 800-61 Rev. 3 discusses incident response coordination; assessment teams must know how to stand down.

Priya's ROE for ENG-712 states the suspension path explicitly, including who tells Northpoint to stand down and who later says it may resume. The path is rehearsed in studio with a fake SOC page before the live engagement. Adding assessment noise while analysts work a real incident would compete for the attention the incident needs.

### Worked example

At 23:10 the timetable API starts timing out. Northpoint's inventory tool is blamed first. Priya's fault tree asks whether any other client reported the outage — yes, the NOC did, before the scan rate increased. Classification: environment fault (pre-existing fragility). Decision: no-go for active checks; continue with document review only after white-team approval.

> **Synthetic case.** The 23:10 timeout and NOC report are invented.

### Errors and limits

Troubleshooting notes that blame people rather than systems poison purple-team trust. Do not hide a no-go from the report's limitations page.

### Exercises

- **EX058 — Classify.** A tester laptop clock is wrong, so the ROE checker marks every action outside the window. Fault class and first fix? *Rubric:* 3 = tooling (or local environment of tester); fix clock/NTP; re-run checker; 2 = class only; 1 = scope fault; 0 = none.
- **EX059 — Stand down.** SOC declares an active ransomware investigation (synthetic). What does the assessment team do? *Rubric:* 3 = suspend noisy activity; notify white team; wait for written resume; 2 = pause vaguely; 1 = continue quietly; 0 = none.
- **EX060 — Go/no-go fields.** List five fields a go/no-go note should contain. *Rubric:* 3 = five of event/time/class/informees/decision/signature; 2 = three; 1 = one; 0 = none.

### Synthesis

Tree first, classify second, write the decision, and stand down when the organisation is already fighting a fire.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Authorized offensive security and red team: service integration

### Learning outcomes

You will (1) place the assessment service among identity, logging, ticketing and change-management services; (2) define hand-off interfaces with owners and SLAs; (3) explain why assessment findings must enter the same tracker as other risks; (4) avoid shadow IT for evidence and tickets.

### 21.1 Assessment as a service

An authorized assessment capability is a service with inputs (requests, agreements), processes (scoped execution) and outputs (findings, reports, retest results). It depends on identity (who may approve), logging (where evidence of activity goes), ticketing (where findings live) and change management (when fixes roll out). Drawing those dependencies prevents the assessment team from inventing parallel tools that nobody else watches.

Treating the work as a service changes what Priya measures. Alongside critical counts she tracks queue time from a stop call to white-team acknowledgement and the rate at which findings reopen after retest. A provider with many criticals but slow acknowledgements and frequent reopens may serve TRT worse than a quieter one.

### 21.2 Interfaces and SLAs

Each interface needs an owner and a response expectation: white-team acknowledgement within fifteen minutes of a stop call; remediation ticket acknowledgement within two business days; evidence repository access revoked within one day of engagement close. SLAs without owners are decorations.

For ENG-712 these expectations are written into the agreement, each with a named owner, and Priya tracks them during the engagement. A missed acknowledgement appears as process debt on the signed evaluation sheet. An interface without an owner tends to become a place where stop calls and tickets go unanswered.

### 21.3 One risk tracker

Findings that live only in a PDF never meet their owners. Export them into the organisation's risk or vulnerability tracker with the same severity vocabulary Chapter 4 required. Keep the PDF as the narrative; keep the tracker as the work queue.

In ENG-712 F-01 and F-07 exist as tracker tickets before any slide deck is built, using the same severity words as the report. A deck that arrives before the tickets is sent back unpublished. The tracker is where owners and due dates live, so a finding that never reaches it never gets fixed.

### 21.4 Shadow IT

Personal drives, unmanaged chat channels and private boards for "just this engagement" become the place evidence goes to die — or to leak. Use the approved services even when they feel slower.

The rule covers temporary files too: a screenshot saved to a desktop folder called evidence_tmp is outside the vault and its retention clock. Weekly vault audits sample laptops and shared drives for such shadow folders during the engagement. Chapter 25's quiet-channel rule applies in the same way, so evidence and ROE details move only through approved services.

### Worked example

Priya integrates Northpoint's outputs with TRT's tracker: each finding becomes a ticket with ATT&CK ID, severity, owner and due date; the PDF report is attached. The evidence vault grants Northpoint time-bounded access that expires at retention end. The SOC receives a calendar invite for the purple replay before the window opens, not after.

> **Synthetic case.** The integration pattern is invented for TRT's tooling landscape.

### Errors and limits

Integration that floods the SOC with raw scanner noise trains people to ignore tickets. Filter and rate findings before they enter the tracker.

### Exercises

- **EX061 — Interface owner.** Name three assessment interfaces and an owner role for each. *Rubric:* 3 = three distinct interfaces with roles (e.g. white-team/CISO, tracker/vuln management, vault/security eng); 2 = two; 1 = one; 0 = none.
- **EX062 — PDF only.** Why is a PDF report alone a weak integration? *Rubric:* 3 = no work queue/owner/due date; findings stall; 2 = hard to search; 1 = PDF is enough; 0 = none.
- **EX063 — Shadow board.** A tester creates a private Trello for TRT findings. What should Priya require instead? *Rubric:* 3 = use TRT's approved tracker; export/migrate; disable the private board; 2 = migrate only; 1 = allow private board; 0 = none.

### Synthesis

Treat assessment as a service with named interfaces, one tracker and no shadow stores.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Authorized offensive security and red team: automation

### Learning outcomes

You will (1) automate report tables and status counts from structured findings; (2) decide which steps must stay human; (3) apply rate limits and dry-run flags to any automation that could touch systems; (4) version automation scripts with the engagement.

### 22.1 Automate the boring, inspectable parts

Building a Markdown table from a finding list, counting open versus fixed, sorting by severity — these are ideal for scripts. They reduce copy errors and produce identical artefacts for the reviewer.

Priya's rule of thumb is that a script may rearrange what a person already decided but may not decide anything itself. Sorting four findings by severity is safe because the severities were set during validation; guessing a severity for a record that lacks one is not. When the builder and a hand-made table disagree, the difference is treated as a bug in one of them and traced before the draft goes out.

### Lab H — report builder

```python
"""Lab H (ch 22): build a Markdown executive table from synthetic findings."""
from collections import Counter
findings = [
    {"id": "F-01", "sev": "high", "status": "open", "tid": "T1078"},
    {"id": "F-04", "sev": "low", "status": "accepted", "tid": "T1190"},
    {"id": "F-07", "sev": "high", "status": "open", "tid": "T1133"},
    {"id": "F-09", "sev": "critical", "status": "fixed", "tid": "T1552"},
]
rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}
print("| ID | Severity | ATT&CK | Status |")
print("|---|---|---|---|")
for f in sorted(findings, key=lambda f: (rank[f["sev"]], f["id"])):
    print(f"| {f['id']} | {f['sev']} | {f['tid']} | {f['status']} |")
c = Counter(f["status"] for f in findings)
print(f"open={c['open']} fixed={c['fixed']} accepted={c['accepted']}")
```

Run with `python3 lab_report.py`. Verified output:

```text
| ID | Severity | ATT&CK | Status |
|---|---|---|---|
| F-09 | critical | T1552 | fixed |
| F-01 | high | T1078 | open |
| F-07 | high | T1133 | open |
| F-04 | low | T1190 | accepted |
open=2 fixed=1 accepted=1
```

### 22.2 Keep humans on the gates

Authorization decisions, white-team calls, severity disputes and go/no-go notes stay human. Automating "approve scope" is how organisations accidentally authorize the wrong prefix.

The line is drawn at decisions that change who or what may be touched. A script can tell the white team that a planned card targets an address outside the signed scope list, but only a named person can say whether the card stops or the scope is amended. Proposals to automate scope approval for ENG-712 are closed with a pointer to this rule rather than debated each time.

### 22.3 Dry-run and rate limits

Any automation that could send traffic needs a dry-run mode that prints what it would do, and a rate limit agreed in the ROE. Classroom labs never send traffic; production tools must still show the same discipline.

A dry run for an ENG-712 tool lists every target address, the method card it belongs to and the planned send rate, so the white team can compare it with the signed ROE before anything leaves the laptop. When the ROE asks for proof that rates were respected, that printed list is filed with the other engagement evidence and kept for the same retention period.

### 22.4 Version with the engagement

Store the exact script version (commit hash or file hash) in the engagement record so a reviewer can regenerate the table later. Unversioned "final_final_v3.py" files are not evidence.

Priya records a SHA-256 of the builder beside each generated table, the same way she does in the worked example. Months later an auditor can rerun the hashed script on the archived JSON and check that the table in the report is identical. A file called final_v3.py with no hash cannot be tied to any table, so archive review rejects it however tidy the output looks.

### 22.5 What not to scrape

Automation that pulls production passwords, session cookies or personal data into a report builder is a data-handling incident waiting to happen. The builder in this chapter reads only the fields a human already filed as findings. If a field is missing, the script should fail loudly rather than invent a default severity.

The safe pattern is a builder that only accepts the fields of a filed finding: identifier, title, severity, status and owner. Continuous-integration tests feed it synthetic fixtures, including deliberately broken records with no severity, to prove that it stops with an error. A builder that reached into consoles for cookies or passwords would turn a reporting convenience into a data-handling incident under the agreement.

### Worked example

Priya runs the report builder on four synthetic findings. It prints F-09 critical first, then the two highs, then the low, and summarises open=2 fixed=1 accepted=1. She pastes the table into the draft report and records the script's SHA-256 beside the attachment.

> **Synthetic case.** The four findings and the printed table are invented.

### Errors and limits

Automation that silently drops findings with unknown severity is a defect; fail loudly. Do not auto-close tickets from a scanner without human review.

### Exercises

- **EX064 — Table order.** In the lab output, which finding appears first and why? *Rubric:* 3 = F-09; critical ranks above high/low; 2 = F-09 only; 1 = wrong order logic; 0 = none.
- **EX065 — Human gate.** Name two decisions that must not be automated in TRT's process. *Rubric:* 3 = two of authorize scope / severity dispute / go-no-go / white-team stop; 2 = one; 1 = automate everything; 0 = none.
- **EX066 — Version evidence.** How should Priya prove which script built the table? *Rubric:* 3 = store commit or SHA-256 of the script with the engagement; 2 = vague version note; 1 = remember it; 0 = none.

### Synthesis

Automate tables and counts; keep authorization human; dry-run anything that touches systems; version the scripts.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Authorized offensive security and red team: evaluation

### Learning outcomes

You will (1) define evaluation criteria before an engagement ends; (2) score process quality separately from finding count; (3) run a lessons-learned review that produces backlog items; (4) refuse vanity metrics.

### 23.1 Criteria before close

Evaluation answers: did we stay in scope, did we meet the decision the CISO needed, did defenders learn, did remediation start? Write those criteria in the ROE or kickoff notes so future-you cannot invent softer ones after a messy week.

For ENG-712 the four questions were written into the kickoff notes as yes or no items: stayed in scope, supported the CISO's coverage decision, gave defenders something to learn, started remediation. Priya fills them in before the CISO reads the sheet, and the finding count appears only as a supporting line, so a long appendix cannot stand in for a missed criterion.

### 23.2 Process quality ≠ trophy count

An engagement that finds nothing but demonstrates solid gates, clean evidence and a useful purple replay can be a success. An engagement that finds dozens of issues by ignoring exclusions is a failure with a long appendix. Score discipline explicitly.

Priya's studio rubric puts this on its first page, because students tend to measure themselves by the length of the findings table. In ENG-712 a quiet engagement with clean gates and a useful purple replay would still have met all four criteria. A team that produced many findings by crossing a STOP line would fail the scope criterion, and no finding count can repair that.

### 23.3 Lessons learned

Within two weeks, red, blue and white teams meet. Each miss from the coverage matrix becomes a ticket. Each process fault becomes a procedure change. Capture what to stop, start and continue.

DET-19 from the coverage story is the model miss ticket: it names the uncovered ATT&CK technique, the matrix cell it came from and the detection owner. Process faults are written as edits to a procedure, such as the clock-sync check before kickoff that ENG-712 added. Holding the meeting within two weeks matters because people still remember why a choice was made.

### 23.4 Vanity metrics

"Hosts scanned", "packets sent" and "criticals found" without context encourage the wrong behaviour. Prefer "techniques exercised", "percent alerted", "findings accepted into tracker within SLA" and "retests closed".

On a management slide Priya replaces a row such as hosts scanned with the number of techniques exercised and the share that raised an alert. The second pair answers the question the CISO asked about SOC coverage; the first only measures how busy the testers were. She removes vanity rows in the same review pass that strips forbidden assurance phrases from the report.

### 23.5 Sharing results without shame

Publish the evaluation sheet to the people who lived the exercise. Hiding a low process score from the SOC while celebrating a high finding count teaches the wrong lesson. TRT's rule is that the same sheet the CISO signs is the sheet the team reads in the retrospective.

In ENG-712 the SOC saw the full sheet, including the clock-sync process fault, at the same retrospective where the two detection backlog items were discussed. Hearing about a weak process score from a summary weeks later would have felt like blame. Seeing it beside the findings made it a shared problem with an owner and a date.

### Worked example

TRT's evaluation sheet for ENG-712: scope adherence 100% (no STOP breaches); decision supported (SOC coverage numbers delivered); two detection backlog items opened; one process change (clock sync check before kickoff). Finding count is recorded but not used as the primary score. The CISO signs the sheet.

> **Synthetic case.** The evaluation sheet is invented.

### Errors and limits

Blaming individuals in the lessons-learned meeting destroys purple-team trust. Keep the minutes about systems and procedures.

### Exercises

- **EX067 — Primary score.** Why is "criticals found" a weak primary evaluation score? *Rubric:* 3 = rewards volume/scope abuse; ignores process and learning; 2 = one reason; 1 = it is the best score; 0 = none.
- **EX068 — Criterion.** Write one pre-declared criterion that measures defender learning. *Rubric:* 3 = measurable learning criterion (e.g. backlog items opened per miss, replay attendance); 2 = vague learning; 1 = finding count; 0 = none.
- **EX069 — Stop/start/continue.** Give one stop, one start and one continue from ENG-712's story so far. *Rubric:* 3 = three concrete items grounded in prior chapters; 2 = two; 1 = one; 0 = none.

### Synthesis

Declare criteria early, score discipline, convert lessons into tickets, and ignore vanity counters.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) pose a research question about assessment practice that can be answered with synthetic or authorized data; (2) choose a method (measurement study, case comparison, structured interview); (3) state ethics and limits up front; (4) write an abstract checklist that catches missing pieces.

### 24.1 Questions worth asking

Examples: Does a three-gate pipeline reduce out-of-scope attempts in student exercises? Which ATT&CK techniques does TRT's SOC alert on after one purple cycle? How long do remediation tickets of each severity stay open? Each question names a population, a measure and a limit.

A question such as whether red teaming works fails this test, because it names no population and no measure. Priya's studio question about out-of-scope attempts passes: the population is studio exercises, the measure is OUT-OF-SCOPE lines in the checker log, and the limit is that student behaviour may differ from a contracted team. Questions that could only be answered by testing real users without their knowledge are rejected outright.

### 24.2 Methods that fit technologists

Measurement studies on ticket and coverage data; before/after comparisons when a control changes; structured interviews with SOC analysts about alert quality. Laboratory exploit research is out of scope for this course.

The common thread is data a technologist already handles: ticket timestamps, coverage matrix cells and the words of analysts who triage the alerts. A before and after comparison around DET-19, for example, can count how often the new detection fired on replayed synthetic activity. Proposals that drift towards novel exploit development are redirected, because they need a laboratory and an authorisation this course cannot provide.

### 24.3 Ethics first

No covert testing of real users, no collection of personal data beyond the agreement, no publication of client identifiers. Label synthetic data. Obtain approval before interviewing staff.

Each of these rules has a concrete check that a reviewer can run before submission. Synthetic logs carry a label in their file names and headers, interview consent is written and filed before any abstract is drafted, and every public draft is searched for client names and identifiers before it is uploaded to the seminar. A draft that fails the search goes back to its author rather than being edited quietly by a reviewer.

### 24.4 Abstract checklist

A passable abstract states the question, the method, the sample size n, the limits and the ethics posture. Missing n is a common failure mode in student papers.

Priya's worked example shows the minimum: n = 3 exercises and 12 actions, stated in the abstract next to the limit that the data are synthetic. Seminar grading treats a missing limits line as seriously as a missing n, because both let a reader overestimate what the study shows. The ethics line names the posture, here no live systems, rather than saying ethics was considered.

### 24.5 Reproducibility for technologists

A classmate should be able to rerun the counts from the synthetic logs and obtain the same fractions. Priya stores the input files beside the abstract and notes the Python version. Reproducibility here is not about exotic environments; it is about not waving at numbers that nobody else can rebuild.

For the HOLD-fraction mini-study this means the three synthetic exercise logs, the counting script and a note of the Python version sit in one folder beside the abstract. A classmate who reruns the script should arrive at the same count of HOLDs out of 12 actions. A screenshot of a spreadsheet total is not accepted, because nobody can check how it was produced.

### Worked example

Priya's mini-study asks: after introducing the operator log, what fraction of planned actions were HOLDs in three synthetic exercises? Method: count pipeline outputs. n = 3 exercises, 12 actions. Limit: synthetic only. Ethics: no live systems. She refuses to claim the result generalises to all vendors.

> **Synthetic case.** The mini-study design is invented for coursework.

### Errors and limits

Harvesting production logs for a paper without approval is still a data-handling breach. Tiny n needs humble claims.

### Exercises

- **EX070 — Question shape.** Rewrite "Are red teams good?" as a measurable research question for TRT. *Rubric:* 3 = names measure, population, timeframe; 2 = partly measurable; 1 = still vague; 0 = none.
- **EX071 — Missing n.** An abstract describes method and limits but not sample size. What does the checklist say? *Rubric:* 3 = n MISSING → revise; 2 = incomplete; 1 = fine as-is; 0 = none.
- **EX072 — Ethics line.** Write one ethics sentence Priya can put in her abstract. *Rubric:* 3 = no live systems / synthetic or authorized data / no personal data beyond agreement; 2 = vague ethics; 1 = none needed; 0 = none.

### Synthesis

Ask a measurable question, pick a humble method, put ethics in the abstract, and never skip n.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) form a small team with named roles (lead, evidence, liaison); (2) run a planning checklist before any lab work; (3) deliver a mid-studio review against the evaluation criteria from Chapter 23; (4) practise conflict resolution when scope opinions differ.

### 25.1 Roles beat heroics

Lead keeps the ROE and timeline. Evidence owner runs manifests and custody. Liaison speaks to the (synthetic) white team and SOC. Rotating roles across studios builds breadth; leaving everything to the strongest writer builds a single point of failure.

Each role has a card on the studio wall, photographed into the evidence folder at the start, so there is a record of who held which duty. In the worked example Sam is the liaison and therefore holds the only white-team contact number. Rotating the cards between studios means everyone eventually runs a manifest, keeps an ROE and makes a difficult call to the white team.

### 25.2 Planning checklist

Agreement fields complete; scope lists loadable by the checker; kit inventory pinned; evaluation criteria written; communication channel tested. No checklist, no lab time. The instructor may fail a studio that cannot produce the checklist at the door.

Every item is answered yes or no at the door. An agreement with an empty exclusion field or a scope list that the checker cannot load means the lab clock does not start, however close the team claims to be. Testing the communication channel before work begins is on the list because a liaison who cannot reach the white team during a HOLD has no safe way to continue.

### 25.3 Mid-studio review

Halfway through, the team presents: gates passed so far, HOLDs encountered, evidence count, risks to delivery. Instructors score process, not drama.

Platform B's mid-review is a good example: four gates passed, one HOLD on a drifting DNS name and six evidence items hashed. Reporting the HOLD openly earns credit, because it shows the gate working. A HOLD that was hidden and found later costs more than one declared early, since it suggests the team would have kept going without the white team's decision.

### 25.4 Conflict on scope

When members disagree whether a hostname is in scope, the rule is: stop, re-read the agreement, ask the liaison to confirm with white team. The loudest voice does not win.

Platform B met exactly this case with its drifting DNS name: the team paused that target, and Sam asked the white team for a written decision. The decision is filed under the hostname's evidence identifier, so a later reader can see why the name was tested or left alone. A confident memory of what the scope meant is never a substitute for the signed list.

### 25.5 Quiet channels

Studio chatter that contains evidence hashes, account names or ROE details stays on the approved channel, not on personal messaging apps. Sam as liaison is the only person who pages the white team. Parallel side chats create conflicting instructions and lost custody.

During the studio the instructors sample messages weekly to check that no hashes or ROE details have leaked into personal SMS or email. The approved channel's log doubles as part of the custody record, showing when each hash was shared and with whom. When two classmates each page the white team, the team ends up with two answers and no clear record of which one applied.

### Worked example

Studio team "Platform B" assigns Priya as lead (for the exercise), Jordan as evidence, Sam as liaison. Their mid-review shows four gates passed, one HOLD on a drifting DNS name, six evidence items hashed. They ask for a written decision on the drifted name and pause that target.

> **Synthetic case.** Platform B and its members other than Priya are invented classmates.

### Errors and limits

Studios that skip the liaison and "just ping the CISO casually" train bad habits. Keep communications on the approved channel.

### Exercises

- **EX073 — Role map.** Assign lead, evidence and liaison responsibilities in one sentence each. *Rubric:* 3 = three distinct responsibility sentences; 2 = two; 1 = one; 0 = none.
- **EX074 — Drift conflict.** Jordan thinks the drifted hostname is "close enough". What does the team do? *Rubric:* 3 = stop; re-check agreement; liaison confirms with white team; no testing until written OK; 2 = stop only; 1 = test anyway; 0 = none.
- **EX075 — Mid-review contents.** List four items a mid-studio review should show. *Rubric:* 3 = four of gates/HOLDs/evidence count/risks/criteria progress; 2 = two; 1 = findings only; 0 = none.

### Synthesis

Name the roles, clear the checklist, review the process halfway, and settle scope disputes with the agreement — not volume.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Authorized offensive security and red team: operational handoff

### Learning outcomes

You will (1) write a handoff package that operations can act on without the testing team present; (2) include residual risk and known unknowns; (3) transfer evidence access cleanly; (4) schedule the retest window before demobilising.

### 26.1 What operations need

Owners need: each finding with severity, scenario, evidence pointer, recommended control, and a suggested due date. They do not need a travelogue of every tool the testers ran. Cut narrative that does not change a decision.

Priya builds the executive table with the report builder and leaves out any due date that has no owner, since a date nobody holds will not be met. Each owner then gets a finding sheet that opens with the scenario and the due date. Notes on which tools were run go to an optional appendix for readers who need to reproduce the work.

### 26.2 Residual risk and unknowns

Every engagement ends with things not tested — excluded segments, techniques not exercised, windows that were shortened. List them. Boards hate surprises more than they hate incomplete work that is honestly bounded.

For ENG-712 the residual-risk page names two gaps in plain words: the fare-payment segment was not tested, and technique T1021 still produced no alert. The handoff checklist treats a residual page without the fare-payment line as incomplete. Writing the gaps down now costs a short paragraph, while a board finding out about them later costs trust in the whole engagement.

### 26.3 Access transfer

Tester accounts, VPN profiles and vault grants end on the handoff date. Operations receives read access to the evidence package under its own roles. Shared mailboxes used "just for the test" are closed.

On the ENG-712 handoff call Priya reads the revocation checklist aloud with Northpoint present, and the VPN profiles are revoked that same afternoon. The evidence vault is switched to TRT-only access control, but only after operations confirms it can open the files. Any Northpoint access that still works after the handoff date is logged as a finding against the engagement itself.

### 26.4 Retest on the calendar

A remediation due date without a retest slot is a wish. Book the validation window (Chapter 27) before the testing team disperses. A handoff without a booked retest is marked incomplete on the evaluation sheet.

For ENG-712 the retest is booked for 2026-12-08 while Northpoint's testers are still engaged, and the calendar invitation is attached to the handoff pack. Booking it early means the people who know the findings will be available to run the checks. A handoff pack that arrives without the invitation is marked incomplete until the slot is agreed.

### 26.5 Warm introductions

A handoff meeting where Priya introduces each finding owner by name beats an email dump. Ten minutes of face-to-face (or video) clarification prevents a week of misrouted tickets. She records attendance so the evaluation sheet can show that operations actually received the work.

Priya tracks one simple measure of how well this worked: the number of tickets that reach the wrong team in the first week after handoff. An owner who has heard the scenario explained in person is less likely to bounce a ticket back as not theirs. The attendance list from the meeting goes into the evaluation sheet as proof of delivery.

### Worked example

Priya's handoff pack for ENG-712: executive table from the report builder; four finding sheets; residual-risk page (fare-payment untested; T1021 still missed); evidence vault ACL flipped to TRT-only; retest slot booked for 2026-12-08. Northpoint's VPN profiles are revoked the same afternoon.

> **Synthetic case.** The handoff pack contents are invented.

### Errors and limits

Handoffs that dump raw scanner exports without triage create ticket floods. Do not revoke evidence access before operations confirms it can open the files.

### Exercises

- **EX076 — Pack contents.** Name five artefacts in a minimum handoff pack. *Rubric:* 3 = five of exec table/findings/residual risk/evidence pointers/ACL note/retest date; 2 = three; 1 = PDF only; 0 = none.
- **EX077 — Unknown.** Write one residual-risk sentence for TRT's fare-payment exclusion. *Rubric:* 3 = states exclusion + that no assurance is claimed there; 2 = mentions exclusion; 1 = claims fare is fine; 0 = none.
- **EX078 — Revoke order.** In which order should vault ACL flip and Northpoint VPN revoke happen, and why? *Rubric:* 3 = confirm TRT can read evidence, then revoke tester access; 2 = either order with weak reason; 1 = revoke first blindly; 0 = none.

### Synthesis

Hand over decisions and evidence, say what you did not test, move access carefully, and book the retest before goodbye.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) decide VALIDATED, REOPENED or NOT RETESTED from retest observations; (2) refuse to mark a finding closed on a verbal "we fixed it"; (3) record validation evidence under the same custody rules; (4) feed failures back into the risk tracker.

### 27.1 Validation is a test of the fix

Remediation validation asks whether the agreed fix removed the problem under the same scope and method constraints. It is not a brand-new engagement, and it is not a rubber stamp.

For ENG-712 the retest uses the same scope list and method cards as the original engagement. Using the visit to probe the excluded fare-payment hosts would be a safety failure, however convenient it might seem. The lab's three status labels keep the language honest by making testers say exactly what was checked and what was not.

### Lab I — retest status

```python
"""Lab I (ch 27): decide remediation-validation status from synthetic retest observations."""
retests = [
    ("F-01", "shared admin account", True, True),
    ("F-07", "ex-contractor VPN accounts", True, False),
    ("F-09", "plaintext password on wiki", False, None),
]
for fid, title, fix_claimed, check_passed in retests:
    if not fix_claimed:
        status = "NOT RETESTED - no fix declared"
    elif check_passed:
        status = "VALIDATED"
    else:
        status = "REOPENED"
    print(f"{fid} {status:30} {title}")
```

Run with `python3 lab_retest.py`. Verified output:

```text
F-01 VALIDATED                      shared admin account
F-07 REOPENED                       ex-contractor VPN accounts
F-09 NOT RETESTED - no fix declared plaintext password on wiki
```

### 27.2 Three statuses

VALIDATED: fix claimed and the check passed. REOPENED: fix claimed but the check failed. NOT RETESTED: no fix declared, so no check yet. Closing a ticket without one of the first two (or an explicit risk acceptance) is a process defect.

The lab output gives one example of each: F-01 VALIDATED, F-07 REOPENED and F-09 NOT RETESTED. Words such as resolved or mostly fixed are rewritten into one of the three labels before the report goes to the CISO. An explicit risk acceptance is the only other way a ticket can close, and it is recorded separately.

### 27.3 Same custody

Retest evidence — a new configuration export, a new log excerpt — gets hashed and filed like the original. "Looks fine on my screen" is not evidence.

For F-01 the new evidence is filed as E-101 with its own digest, next to the original discovery evidence in the same vault layout. A peer who opens the finding can then compare the before and after files directly. An agreement on a screen share that the setting looks fine leaves nothing that can be verified later.

### 27.4 Risk acceptance

Sometimes an owner accepts a residual risk with a named approver and a review date. That is a legitimate close path; silence is not.

An acceptance in the tracker needs two fields to be valid: the name of the person accepting the risk and a review date. Priya's team turns each review date into a calendar reminder two weeks before it falls due. An acceptance with either field empty is reopened, because nobody can be held to a decision that has no owner.

### 27.5 Partial fixes

Sometimes an owner fixes two of three accounts and asks to close the ticket. Priya's rule is to validate what was claimed, reopen or split the finding for what remains, and never let a partial fix erase the whole issue. The tracker should show residual work, not a green checkbox that hides it.

The worked example shows why: F-07 reopened because ex-contractor accounts could still authenticate after a claimed fix, so closing it on the owner's word would have hidden live access. A child ticket split off for any remaining account keeps the parent finding identifier so an examiner can follow the history.

### Worked example

Three findings enter retest. F-01 validates. F-07 reopens because ex-contractor accounts still authenticate. F-09 was never declared fixed. Priya updates the tracker: F-01 closed with evidence E-101; F-07 severity remains high and due date resets; F-09 stays open awaiting a fix claim.

> **Synthetic case.** The three retest outcomes are invented.

### Errors and limits

Retesting only the happy path and ignoring alternate entry points can falsely validate. Stay inside the original scope unless a new agreement says otherwise.

### Exercises

- **EX079 — Lab statuses.** Quote the three statuses the lab prints. *Rubric:* 3 = VALIDATED, REOPENED, NOT RETESTED - no fix declared; 2 = two; 1 = one; 0 = none.
- **EX080 — Verbal close.** An owner says F-07 is fixed but refuses a retest window. What status and next step? *Rubric:* 3 = remains open / not validated; escalate; no close without check or formal acceptance; 2 = keep open; 1 = close on verbal; 0 = none.
- **EX081 — Acceptance fields.** Name three fields a risk-acceptance record needs. *Rubric:* 3 = three of approver/reason/review date/residual risk statement/scope; 2 = two; 1 = one; 0 = none.

### Synthesis

No fix claim, no retest; no evidence, no close; acceptance is explicit or it did not happen.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) prepare a field kit checklist for an on-site or remote supervised session; (2) practise professional conduct with operations staff; (3) handle an unexpected production event during a window; (4) debrief with facts, not folklore.

### 28.1 Field kit

Written ROE and emergency contacts (offline copy); pinned tool versions; scope checker and ROE checker; evidence vault credentials that work; a tested out-of-band phone path to the white team; a notepad for custody lines when systems are down. Fancy dashboards are optional; the checklist is not.

The offline copy matters more than it seems during a long night on site. A phone can be the only device holding the ROE and the white-team number, and a dead battery on a station platform then leaves the tester unable to check a boundary or call anyone. Priya carries a printed ROE and contact sheet, and the conduct checklist fails a kit that lacks them.

### 28.2 Conduct

Assessment staff are guests in operations' house. Explain what you are about to do in plain language, keep to the window, and never surprise a change manager with traffic during a freeze. Purple-team success depends on trust built in these small moments.

In practice this means telling the duty controller what the next check will touch before starting it. If a Friday roster cutover is scheduled, an almost finished check stops and moves to the next window, even though the target is in scope. The change manager owns that cutover, and testers who ignore it lose the access they need for the rest of the engagement.

### 28.3 Unexpected events

A breaker trip, a passenger-information outage, a medical emergency on site — none of these appear in the ROE, and all of them mean stop noisy work and yield to operations. Resume only on white-team instruction.

The ROE cannot list every emergency, so the default when something unexpected happens is to stop. Restarting needs an explicit go from the white team, and the log records the name of the person who gave it and the time. That record later shows that the pause and the resume were decisions, not drift.

### 28.4 Debrief with facts

"The SOC was asleep" is folklore. "T1021 produced no alert for 40 minutes; ticket DET-19 opened" is a fact. Field notes should support the second style.

Writing the forty-minute silence on T1021 and the DET-19 ticket gives the SOC something to fix and a way to check that it has been fixed. Insulting wording about the SOC is edited out of field notes, and a note author who uses it gets a conduct finding raised through the liaison. Blame closes down exactly the conversations a purple team needs.

### 28.5 Remote field practice

When the session is remote rather than on-site, the kit still applies: out-of-band phone, offline ROE, tested screen-sharing that does not expose unrelated desktop files. Priya closes every other window before joining the white-team call. Accidental disclosure of another client's screen is a field failure even if no packet was sent.

Remote work adds its own risks, such as a chat notification popping up during screen sharing or a file from another client visible on the desktop. Before a white-team call Priya tests her screen sharing with a classmate and confirms that only the agreed window is visible. The offline ROE and the out-of-band phone stay on her desk exactly as they would on site.

### Worked example

During a supervised evening window the passenger-information displays fail city-wide for an unrelated reason. Priya halts inventory traffic, notifies the white team, and switches to offline evidence labelling. When the NOC clears the event, the white team authorises a shortened resume. The debrief cites the halt time and the DET tickets, not personalities.

> **Synthetic case.** The display outage and halt are invented field practice.

### Errors and limits

Field heroics that "finish the scan anyway" during an outage are how assessment teams get banned. Take the no-go.

### Exercises

- **EX082 — Kit item.** Why carry an offline ROE copy? *Rubric:* 3 = vault/VPN may be down; still need scope/emergency contacts; 2 = backup vaguely; 1 = unnecessary; 0 = none.
- **EX083 — Freeze.** A change freeze starts two hours early. What does the team do with planned active checks? *Rubric:* 3 = stop active checks; confirm with white team/change manager; reschedule; 2 = pause; 1 = squeeze them in; 0 = none.
- **EX084 — Fact line.** Rewrite "The SOC ignored us" as a factual debrief sentence. *Rubric:* 3 = names technique, time-to-alert or miss, ticket ID; 2 = partial fact; 1 = keeps blame; 0 = none.

### Synthesis

Pack the checklist, behave as a guest, yield to real events, and debrief with ticketed facts.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) assemble an end-to-end authorized assessment package for a synthetic TRT request; (2) include scope objects, ROE, method statement, evidence plan, rating scale and report template; (3) run every lab checker against the package; (4) submit a build that a peer can operate without asking you questions.

### 29.1 The build artefacts

1. Request and decision statement. 2. Scope lists (prefixes, names, exclusions). 3. ROE (window, allowed activities, stop list, white-team contact). 4. Method statement mapped to SP 800-115/PTES/WSTG as used. 5. Kit inventory with versions. 6. Evidence plan (what, where, retention). 7. Rating scale and bands. 8. Report template with executive table hook. 9. Retest plan. 10. Evaluation criteria.

Missing any one of the ten fails the capstone completeness score. The order follows the life of an engagement, so the completeness score walks the artefacts in the same sequence on the peer score sheet. A package with sparkling findings but no evidence plan or retest plan is incomplete. In Priya's worked example every one of the ten artefacts is present, including exclusion of fare-payment by both prefix and hostname.

### 29.2 Operate what you built

A peer loads your scope into `lab_scope.py` patterns, your ROE into `lab_roe.py` patterns, and your findings into `lab_score.py` and `lab_report.py`. If they cannot, the build is incomplete.

In the worked example a peer runs the checkers on Priya's package and gets the same STOP and IN-SCOPE results she documented. That reproduction by someone other than the author is what operability means here. If the scope checker cannot load the submitted lists, operability fails before any slide is looked at, because a polished presentation of an unusable package does not help an operations team.

### 29.3 No exploit content

The package contains zero attack procedures. Anyone asking for them during the capstone is redirected to the educational boundary in Chapter 10.

The capstone tests whether students can design and run an assessment service, not whether they can attack something, so attack steps add nothing to the grade. A student who asks for exploit detail during the build is redirected to Chapter 10 and receives a safety deduction. The rubric has no exception for requests framed as being for teaching purposes, since a written procedure works the same way whoever reads it later.

### 29.4 Peer review rubric

Peers score: completeness of the ten artefacts, checkability, clarity of residual-risk language, and safety (no dual-use detail). Finding volume is irrelevant.

Dual-use detail fails the safety criterion even in an otherwise complete package. A peer who awards extra marks for a long findings list has invented a criterion, and that score sheet is voided and redone. The point of the rubric is that a reviewer could hand the package to an operations team and expect it to work, with residual-risk wording that a manager can repeat accurately.

### 29.5 Time box

The capstone build is scored on completeness and operability inside a fixed studio window, not on endless polish. Priya freezes scope lists forty-eight hours before peer review so checkers stop moving. Last-minute aesthetic edits that break a CSV column fail the peer test.

The lead announces the freeze in the studio channel at T minus 48 hours, and after that point the scope lists are not edited. A column renamed for neatness after the freeze can stop the scope checker loading the CSV, which would fail the peer test. Polishing the slides is still allowed, provided the files the checkers read do not change.

### Worked example

Priya's capstone package for a synthetic "staff-portal identity assurance" request fills all ten artefacts, excludes fare-payment by prefix and hostname, pins three tools, and includes the Chapter 22 table hook. A peer runs the checkers and produces the same STOP/IN-SCOPE results she documented.

> **Synthetic case.** The capstone request and peer are invented.

### Errors and limits

Beautiful prose that a checker cannot load fails the technologist outcome. Copying another team's package without understanding it fails too.

### Exercises

- **EX085 — Ten artefacts.** List any eight of the ten build artefacts. *Rubric:* 3 = eight correct from the chapter list; 2 = five; 1 = three; 0 = none.
- **EX086 — Peer test.** What two outcomes prove a peer can operate your package? *Rubric:* 3 = checkers run + matching documented verdicts; 2 = one; 1 = peer likes the prose; 0 = none.
- **EX087 — Safety fail.** A teammate adds a page of password-spraying steps "for realism". What do you do? *Rubric:* 3 = remove; cite educational boundary; refuse dual-use content; 2 = move to appendix; 1 = keep; 0 = none.

### Synthesis

Build the whole service on paper and in checkers; let a peer run it; keep exploit detail out.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) present the capstone package to a review panel; (2) defend scope, method and residual-risk choices with cited frameworks; (3) answer "what would you refuse?" correctly; (4) identify your next course step without claiming the book is finished.

### 30.1 Panel agenda

Ten minutes: decision and scope. Ten minutes: method and gates. Ten minutes: evidence, rating and report. Ten minutes: purple-team learning and retest. Ten minutes: questions. The panel holds the ROE and the checker outputs while you speak.

Priya keeps a visible timer on the desk, and the panel kit checklist fails readiness if one is missing. The time boxes protect the later blocks: a candidate who spends twenty minutes on technical detail leaves no time to show purple-team learning or the retest plan. Because the panel holds the ROE and checker outputs, every claim can be checked against an artefact as it is made.

### 30.2 Defence with citations

When asked why exclusions come first, cite Chapter 2 and the ROE practice. When asked why you borrow a white team, cite TIBER-EU/CBEST ideas. When asked how you rated F-09, show the matrix. Opinions without artefacts score poorly.

Priya practises these answers aloud and keeps them on a one-page crib sheet, which the panel allows on the desk. For F-09 she opens the rating matrix and walks through the likelihood and impact cells rather than defending the rating from memory. An answer that points to an artefact lets the panel check it, while a confident opinion leaves them nothing to verify.

### 30.3 The refusal question

Panels ask what you would refuse. Strong answers: testing without a reachable white team; fare-payment contact; mid-window scope expansion by chat; providing exploit steps; keeping evidence on a personal laptop. Weak answers: "nothing, we are flexible."

Each strong answer names a condition and the reason it ends the work, such as no reachable white team meaning nobody can authorise a stop or a restart. Oral safety fails if any of the four classes of refusal is missing: white-team absence, fare-payment contact, chat-based scope expansion and exploit steps. A flexible answer suggests the candidate has not yet thought about where the boundaries are.

### 30.4 After the panel

Pass means the package meets the Chapter 29 rubric and the oral defence showed judgement. It does not mean the manuscript has passed A4 or independent review. The next course in the study path is course 089, AI and machine-learning security for technologists.

Before questions end, Priya says aloud that the package uses synthetic data and that a pass carries no live authority. That sentence is on the pass-script checklist, because candidates sometimes describe a course pass as if it certified them to test real systems. Saying the limits clearly is part of the judgement the panel is assessing.

### 30.5 Portfolio entry

After the panel, Priya files a short portfolio note: which artefacts she led, which refusal she practised, which detection tickets she opened. The note cites ENG-712 and labels everything synthetic. Future employers reading a portfolio should see judgement, not a claim that she "hacked a transit agency."

Priya's note lists the evaluation sheet and the handoff pack as artefacts she led, the fare-payment refusal as the one she practised, and DET-19 as a ticket she opened. Wording such as hacked a transit agency is banned from the note, because it is false for a synthetic exercise and suggests the wrong attitude to an employer.

### Worked example

Priya presents ENG-712's package. She is asked to expand into fare-payment "just this once". She refuses, quotes the exclusion language, and offers a separate engagement proposal if the fare owner authorises it. She is asked for exploit steps for T1552.001; she points to the ATT&CK page and to the book's boundary. The panel marks safety and residual-risk honesty as strengths.

> **Synthetic case.** The panel exchange is invented for assessment practice.

### Errors and limits

Memorising framework names without tying them to a decision fails. Claiming accreditation from this draft fails.

### Exercises

- **EX088 — Refuse list.** Give three distinct refusals a technologist must be ready to make. *Rubric:* 3 = three from no white team / excluded systems / chat scope change / exploit steps / personal evidence stores; 2 = two; 1 = one; 0 = none.
- **EX089 — Citation defence.** In one sentence, defend why logged ≠ alerted using Chapter 19 language. *Rubric:* 3 = detect-and-respond goal needs notification/response, not only telemetry; 2 = partial; 1 = logged is enough; 0 = none.
- **EX090 — Next step.** What is the next course after this book's chapter 30, and what must you not claim about this draft? *Rubric:* 3 = course 089 AI security + no claim of finished/A4/accredited book; 2 = one part; 1 = wrong course; 0 = none.

### Synthesis

Present artefacts, cite frameworks, practise refusal, and leave with humility about what a draft manuscript is.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Tidewater Regional Transit, Priya Natarajan, Northpoint Assurance and every figure are synthetic. Lab-based answers quote the verified outputs printed in the chapters. Any answer that meets the rubric scores equally.

**EX001.** The BMC is reachable on its own network port, is patched through vendor firmware rather than the OS, and may sit on a management VLAN outside the written scope. A separate record forces the scope meeting to include or exclude it explicitly.

**EX002.** Record the crash-under-load fragility in the asset record, agree with the owner a lower-impact method such as configuration review or a heavily throttled check in a supervised window, and write that limit into the rules of engagement.

**EX003.** TRT can authorize testing of its own virtual machines, operating systems and applications. The hypervisor, storage and network fabric belong to the hosting company, so its terms of service must be read and any required notice given before planning.

**EX004.** A /25 fixes the first 25 bits, so 192.0.2.0/25 spans .0 through .127. The address .200 lies in the upper half of the /24, which is not listed, so the lab prints OUT-OF-SCOPE.

**EX005.** It would return IN-SCOPE, because 192.0.2.70 is also inside 192.0.2.0/25. The fare-payment segment that the client carved out would then be tested, breaching the agreement.

**EX006.** Stop testing that name. 203.0.113.5 is outside every approved prefix; Priya confirms with the system owner what changed and obtains written re-approval for the new address before any further work.

**EX007.** It should return a stop label such as "STOP: unreadable time". November has 30 days, so the string cannot parse; an unparseable time must never be treated as inside the window.

**EX008.** `hashlib`. It ships with Python, so it needs no dependency review, introduces no supply-chain risk and gives the reviewer identical results.

**EX009.** 192.0.2.10 → IN-SCOPE; 192.0.2.70 → EXCLUDED; 203.0.113.5 → OUT-OF-SCOPE (any equivalent trio covering all three labels scores 3).

**EX010.** The validator prints `missing evidence`. Without an evidence identifier no reviewer can check the claim, so it cannot appear as a finding until evidence is attached.

**EX011.** Replace "urgent" with one of low/medium/high/critical. The tester proposes the level using the agreed rating method (Chapter 13) and the reviewer confirms it; the vocabulary itself is not extended.

**EX012.** Example: `owner` — the named person or team accountable for the fix, so the remediation tracker can route and chase the finding. Due date, status or retest date with a reason also score 3.

**EX013.** A red-team exercise. It emulates a defined threat actor over weeks with limited awareness among defenders, so it measures detection and response as a whole rather than listing weaknesses.

**EX014.** Sign-in records sampled across every VPN entry path, or authorized test accounts, showing that no session was established without the second factor. The written policy proves only that the control exists.

**EX015.** Integrity. The operations team that owns the roster and TRT's security lead should hear first, because a silent alteration could put the wrong driver on a route.

**EX016.** An export avoids interactive access that could disrupt a production VM, and it produces a reproducible artefact that a reviewer can re-examine without reopening a shell.

**EX017.** She refuses. Hypervisor testing is outside TRT's tenancy; it needs written authorization from the hosting provider under its terms, which the current engagement does not include.

**EX018.** Store the snapshot under evidence access rules, rotate the exposed password immediately, and delete or return the snapshot when the agreement's retention period ends.

**EX019.** Authorization failed: authentication succeeded for many people, but the edit privilege was too broad. Restrict timetable edits to a named publisher role and log every change.

**EX020.** T1078 Valid Accounts — legitimate credentials that should no longer be usable remain usable. Lab H (Chapter 22) files the same finding, F-07, under T1133 External Remote Services, and both mappings are correct: T1133 names the exposed service (the staff VPN), while T1078 names the valid accounts that still work through it. The exercise asks about the accounts, so T1078 earns full marks; a report can list both IDs for F-07.

**EX021.** Example: a help-desk password-reset procedure that accepts a name and employee number over the phone without a callback. Mitigate with stronger identity proofing and a second channel. SMS reset interception or unprotected backup codes with matching mitigations also score 3.

**EX022.** Example: (1) internet → reverse proxy — TLS termination and reverse-proxy authentication; (2) staff VPN → jump host — MFA and allow-listed management access. Equivalent distinct pairs score 3.

**EX023.** All three depend on the same secret in the same directory. Stealing or guessing that password crosses every layer at once, so the depth is illusory.

**EX024.** The VPN gateway or central authentication log — the identity evidence for that path. Application or database logs may show later activity but do not prove the VPN login itself.

**EX025.** `E-002_wiki_page_export.txt` prints MISMATCH. Any finding that cited that export must pause until a fresh copy is collected under custody and re-hashed; the altered file is no longer reliable evidence.

**EX026.** Example: "2026-11-03 21:40 Priya Natarajan exported portal login banner from trt-portal under ticket ENG-712; stored in evidence/ENG-712/E-001_portal_login_banner.txt."

**EX027.** No. Evidence stays in the approved engagement repository under the agreement's access and retention rules, not on personal equipment.

**EX028.** Example: "Determine, in a time-bounded authorized exercise with white-team oversight, whether TRT's SOC detects and responds to a realistic intruder against the staff portal and VPN, excluding fare-payment systems."

**EX029.** Any five of: parties, in-scope systems, exclusions, allowed methods, time window, emergency contact, data-handling rules, report audience. Naming five distinct required fields scores 3.

**EX030.** Purple teaming structures collaboration — often with planned reveals or joint reviews — so defenders improve detection and response; the primary product is learning, not a competitive score.

**EX031.** `2026-11-04 06:10 VPN configuration review STOP: outside window` and `2026-11-03 23:00 fare-system interaction STOP: forbidden activity`.

**EX032.** Write a hard limit: configuration review only, or active checks throttled to an agreed rate inside the window, and record that limit in the ROE so testers cannot improvise.

**EX033.** Do not start the session. Escalate to the CISO or named deputy, confirm a reachable stop authority, and only then reopen the window in writing.

**EX034.** Example: reverse-proxy access logs, a WAF, a CDN edge, or the SIEM. Any of these may hold a copy that becomes assessment evidence and that must follow the agreement's retention rules.

**EX035.** Mask `alex.rivera` (the local part) and keep `@trt.example` or a label such as "staff account" so the finding still proves a staff identity was involved without exposing the person.

**EX036.** Delete or return every ENG-712 evidence item when day 90 arrives, and write a short record that destruction or return happened, who did it, and when.

**EX037.** F-09 with score 20 in the critical band — the wiki page with a plaintext service password.

**EX038.** Example: "Ex-contractor VPN accounts (T1078) could let a former contractor reach the management jump host and disrupt staff-portal operations (availability/integrity)."

**EX039.** Raise urgency (for example, treat the ticket as due this week) even though severity stays low, because active internet probing increases the chance the weakness is found before a routine fix cycle.

**EX040.** SP 800-115: review (configuration review) or, if confirming enforcement, target vulnerability validation. PTES: vulnerability analysis (or a clearly argued adjacent phase). Naming both with a short reason scores 3.

**EX041.** Example: "Inventory listening services on in-scope prefixes only, at the agreed request rate inside the ROE window, with fare-payment addresses excluded."

**EX042.** Technique IDs let defenders and reports map behaviours consistently without providing operational attack procedures that this educational book deliberately withholds.

**EX043.** A2 holds because the activity ("password spraying") is not on the approved list. A3 holds because 192.0.2.140 is outside the in-scope /25.

**EX044.** `['A1', 'A4']`. The list is evidence that only actions passing target, time and activity gates were recorded as performed.

**EX045.** Honour the fragility note in the ROE — throttle or switch to configuration review — and if the note is unclear, ask the white team before proceeding even though the hard gates passed.

**EX046.** A white-team with stop authority, and a structured learning or replay review after the exercise. Scenario design guided by threat intelligence is also acceptable as a second idea.

**EX047.** Example: "All fare-payment systems are excluded from every activity, including hosts in 192.0.2.64/27 and any name under fare.trt.example."

**EX048.** The first engagement's decision is about identity control effectiveness; intrusive fuzzing raises fragility risk and may exceed the ROE. Select checks that answer the decision inside the agreed limits.

**EX049.** Any four of: name, version, owner/maintainer, purpose, data handled, approved environment, checksum/signature reference.

**EX050.** Keep the pinned version. Defer the feature upgrade to after the window; only consider a mid-window change if it is a security fix and the white team agrees in writing.

**EX051.** The script has no owner or integrity check, may perform activities the ROE forbids, and may store or transmit evidence outside approved handling rules.

**EX052.** Example: remove the password from the wiki and store it in the approved secrets vault (Protect); owner = wiki/service owner; check = automated secret scan of the wiki space plus a spot review in 30 days.

**EX053.** Example: force the legacy path through a jump host with MFA and session recording, shorten session lifetime to one hour, and track a date to retire the legacy path.

**EX054.** Example: "As of 2026-11-10, within the staff-portal scope of ENG-712, the previously reported identity findings have been remediated and retested; residual risk remains outside that scope."

**EX055.** alerted 3/7 = 42.9%; logged 2/7 = 28.6%; missed 2/7 = 28.6%.

**EX056.** Example: "Detect T1021 Remote Services on jump hosts — alert SOC on interactive sessions outside change windows."

**EX057.** The exercise goal was detection and response. A log line that nobody sees does not produce a response, so the outcome fails the goal even though telemetry existed.

**EX058.** Tooling (tester environment): correct the clock via NTP or manual set, verify time against the white team's clock, and re-run the ROE checker before any further action.

**EX059.** Suspend activities that could add noise or risk, notify the white team immediately, and resume only on written instruction after the incident commander agrees.

**EX060.** Any five of: event description, timestamp, fault class, people informed, decision (go/no-go), conditions to resume, signature/name of decision-maker.

**EX061.** Example: white-team stop calls → CISO/on-call security manager; finding tickets → vulnerability-management owner; evidence vault access → security engineering. Other coherent triples score 3.

**EX062.** A PDF has no owner field, no due date and no workflow state, so remediation stalls unless someone manually copies every finding into a tracker.

**EX063.** Require all findings in TRT's approved tracker, migrate anything already on the private board, and shut the board down so evidence and status cannot diverge.

**EX064.** F-09 appears first because its severity is critical, which the builder ranks above high and low.

**EX065.** Example: approving scope changes, and issuing a go/no-go after an incident. White-team stop authority and final severity adjudication also score.

**EX066.** Record the script's commit hash or SHA-256 digest in the engagement folder next to the generated table so a reviewer can regenerate and compare.

**EX067.** It rewards finding more issues even by unsafe methods, and it ignores whether the team stayed in scope, whether defenders learned, and whether remediation started.

**EX068.** Example: "For every missed technique in the coverage matrix, a detection backlog ticket with owner and ATT&CK ID is opened within five business days."

**EX069.** Example: Stop — mid-window tool upgrades without white-team OK. Start — clock sync check before kickoff. Continue — three-gate pipeline with operator log. Other coherent triples score 3.

**EX070.** Example: "Over two quarterly purple-team cycles at TRT, what percentage of exercised ATT&CK techniques moved from missed to alerted?"

**EX071.** Mark n as MISSING and revise the abstract before submission; without sample size readers cannot judge the claim.

**EX072.** Example: "This study uses only synthetic exercise logs and does not involve live TRT systems or personal data."

**EX073.** Lead: owns ROE adherence and timeline. Evidence: custody, hashing and repository hygiene. Liaison: white-team/SOC communication and written confirmations.

**EX074.** Stop testing that name, re-read the approved list, and have the liaison obtain a written white-team decision before any further action.

**EX075.** Any four of: gates passed, HOLDs and reasons, evidence items counted/hashed, risks to delivery, progress against pre-declared evaluation criteria, open questions for white team.

**EX076.** Any five of: executive finding table, per-finding sheets, residual-risk/unknowns page, evidence index with hashes, ACL/transfer note, booked retest window, method/ROE copy.

**EX077.** Example: "Fare-payment systems (192.0.2.64/27 and fare.trt.example) were excluded; this engagement provides no assurance about those systems."

**EX078.** Confirm TRT operators can open the evidence package under their new ACL, then revoke Northpoint's VPN and vault grants, so remediation never loses access to proof.

**EX079.** F-01 VALIDATED; F-07 REOPENED; F-09 NOT RETESTED - no fix declared.

**EX080.** Leave F-07 open (not validated). Escalate to the remediation owner and CISO; close only after a successful retest or a written risk acceptance.

**EX081.** Any three of: named approver, reason, residual-risk statement, review/expiry date, scope of acceptance, linked finding ID.

**EX082.** If the vault or VPN is unavailable you still need the scope, exclusions and emergency contact numbers; paper or an offline encrypted copy keeps the gates enforceable.

**EX083.** Stop active checks immediately, confirm the freeze with the white team and change manager, and reschedule inside a written window.

**EX084.** Example: "T1021 activity from 22:10–22:50 produced no SOC alert; detection backlog ticket DET-19 was opened."

**EX085.** Any eight of: request/decision, scope lists, ROE, method statement, kit inventory, evidence plan, rating scale, report template, retest plan, evaluation criteria.

**EX086.** The peer can run the relevant checkers on your lists, and the printed verdicts match what your documentation predicted.

**EX087.** Delete the page, remind the team of the Chapter 10 educational boundary, and refuse any dual-use procedural content in the submission.

**EX088.** Example: refuse to start without a reachable white team; refuse any fare-payment activity; refuse to supply exploit procedures. Chat-based scope expansion and personal-laptop evidence stores also count.

**EX089.** A logged outcome means telemetry existed but the detect-and-respond goal fails if no analyst or playbook was notified in time to act.

**EX090.** Next is course 089, AI and machine-learning security (technologist). Do not claim this draft is an accredited qualification or that it has passed the 300-page A4 and independent-review gates.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v4.0 Specification Document. <https://www.first.org/cvss/v4.0/specification-document>
- IETF RFC 5737. IPv4 Address Blocks Reserved for Documentation. <https://www.rfc-editor.org/rfc/rfc5737>
- IETF RFC 9116. A File Format to Aid in Security Vulnerability Disclosure (security.txt). <https://www.rfc-editor.org/rfc/rfc9116>
- MITRE ATT&CK Enterprise matrix and technique pages (e.g. T1078 Valid Accounts, T1133 External Remote Services, T1552.001 Credentials In Files). <https://attack.mitre.org/>
- MITRE ATT&CK Navigator. <https://mitre-attack.github.io/attack-navigator/>
- MITRE D3FEND. <https://d3fend.mitre.org/>
- NIST CSWP 29 (2024). The NIST Cybersecurity Framework (CSF) 2.0. <https://doi.org/10.6028/NIST.CSWP.29>
- NIST SP 800-30 Rev. 1 (2012). Guide for Conducting Risk Assessments. <https://doi.org/10.6028/NIST.SP.800-30r1>
- NIST SP 800-53 Rev. 5 (2020). Security and Privacy Controls for Information Systems and Organizations. <https://doi.org/10.6028/NIST.SP.800-53r5>
- NIST SP 800-61 Rev. 3 (2025). Incident Response Recommendations and Considerations for Cybersecurity Risk Management. <https://doi.org/10.6028/NIST.SP.800-61r3>
- NIST SP 800-86 (2006). Guide to Integrating Forensic Techniques into Incident Response. <https://doi.org/10.6028/NIST.SP.800-86>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Application Security Verification Standard (ASVS). <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
