# Authorized Offensive Security and Red Team: A Professional Practitioner's Guide

- Language: English (`en`); professional course, six months; approximately 360 hours of planned study.
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: entry-level practitioners joining an organisation's security team.
- Relation to neighbouring books: the [rapid course book](../../../../rapid-1-month/offensive-security-red-team/en/book/MANUSCRIPT.md) is a four-chapter introduction; the [technical book](../../../../technical-18-months/offensive-security-red-team/en/book/MANUSCRIPT.md) goes deeper into tooling and verification. **This book is a compact practitioner's guide.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. **No authority to test real systems.** All organisations, people and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, filtering, ticketing and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–3 cover foundations, context and authorization; 4–7 cover methods, tools, workflow and verification; 8–10 cover case analysis, communication and quality; 11–12 are the supervised lab and portfolio. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, five exercises scored 0–3, a synthesis and a **Continue studying** block. Labs in Chapters 3, 5 and 10 read local data only (`python3 file.py`).

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Harborline Credit Union (HCU)** — online banking, staff VPN, AS/400 core (out of scope), staging web tier | Organisation studied throughout | Invented |
| **Leo Okonkwo** | Junior security practitioner at HCU | Invented |

### Core sources

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) place authorized offensive security among other security practices; (2) name confidentiality, integrity and availability with credit-union examples; (3) explain least privilege and defense in depth; (4) list the frameworks this course uses.

### 1.1 Where offensive testing sits

Security work includes architecture, monitoring, incident response and authorized testing. Testing finds what the others missed, under written permission. It does not replace patching, logging or training.

### 1.2 CIA at a credit union

Confidentiality protects member account data; integrity protects balances and transfer instructions; availability keeps online banking usable. A finding is judged by which of these it threatens.

### 1.3 Least privilege and depth

Accounts and network paths should allow only what is needed. Several layers — network, application, identity, monitoring — mean one failure does not end the story. Testers look for places where layers are missing.

### 1.4 Frameworks you will cite

NIST SP 800-115 for planning assessments; PTES for engagement stages; OWASP WSTG for web checks; MITRE ATT&CK for technique names; TIBER-EU and CBEST for threat-led tests in finance.

### 1.5 What practitioners produce

Practitioners produce scoped plans, validated findings, clear reports and verified remediations — not piles of unconfirmed scanner noise.

### 1.6 Member trust

Members trust HCU with wages and savings. A careless test that locks accounts or leaks a statement destroys that trust faster than most technical findings. Every method Leo proposes must answer: what member harm could this cause if it goes wrong, and how do we prevent it?

### Worked example (synthetic HCU)

Leo Okonkwo joins HCU's security team. His first week is a map: online banking and the staff VPN are in the next authorized review; the core banking AS/400 is out of scope. He pins the CIA questions above his desk.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX001 — Three practices.** Name three security practices besides authorized testing. *Rubric:* 3 = three of architecture, monitoring, IR, patching, training; 2 = two; 1 = one; 0 = none.
- **EX002 — CIA match.** Match: leaked member statements; altered transfer amount; online banking down. *Rubric:* 3 = C, I, A; 2 = two; 1 = one; 0 = none.
- **EX003 — Least privilege.** Give a credit-union example of least privilege. *Rubric:* 3 = concrete account/path limited to need; 2 = vague; 1 = wrong; 0 = none.
- **EX004 — Defense in depth.** Why is one firewall not enough? *Rubric:* 3 = other layers can fail independently; app/identity/monitor still needed; 2 = partial; 1 = it is enough; 0 = none.
- **EX005 — Framework pick.** Which source would Leo open first to structure a web application test? *Rubric:* 3 = OWASP WSTG; 2 = ATT&CK; 1 = CBEST only; 0 = none.

### Synthesis

Authorized testing sits beside other practices; CIA, least privilege and public frameworks shape every engagement.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Service and stakeholder context

### Learning outcomes

You will (1) identify HCU services and who owns them; (2) explain why core banking is often out of scope; (3) map stakeholders for an engagement; (4) write a context paragraph for a test plan.

### 2.1 Services that matter

HCU runs online banking, a staff VPN, email, a member-facing website and a core banking system on an AS/400. Online banking and the VPN are internet-reachable and change often; they are common first targets for authorized review.

### 2.2 Why core banking is excluded

The AS/400 holds the system of record for balances. An accidental outage would stop branches. Unless a specialised, heavily controlled engagement is funded, it stays out of scope and is protected by compensating controls.

### 2.3 Stakeholders

The CISO authorises; the online-banking product owner accepts risk; the network team opens temporary rules; the SOC watches for test traffic; legal reviews the contract. Leo's job is to know who decides what.

### 2.4 Context in the plan

A good plan states business purpose (protect members, meet examiner expectations), services in and out of scope, and peak times to avoid (for example Friday payday).

### 2.5 Third parties

Card processors and cloud email are separate organisations. Testing them needs their authorization, not only HCU's.

### 2.6 Examiner expectations

Credit unions face safety-and-soundness exams that ask how systems are tested. Leo's context paragraph is also evidence for examiners: it shows HCU chooses scope deliberately, excludes fragile systems and schedules around operations rather than testing "everything that answers a ping."

### Worked example (synthetic HCU)

Leo drafts: "Purpose: reduce risk to member data and authenticate online banking ahead of the annual exam. In scope: online banking web tier and staff VPN. Out of scope: AS/400 core, ATM network, third-party card processor. Avoid: Saturday morning batch window."

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX006 — Five services.** List five HCU services from the chapter. *Rubric:* 3 = five correct; 2 = four; 1 = two; 0 = none.
- **EX007 — AS/400 exclusion reason.** Why is the AS/400 usually out of scope? *Rubric:* 3 = system of record; outage stops branches; needs specialised controls; 2 = partial; 1 = "old"; 0 = none.
- **EX008 — Who authorises.** Who at HCU authorises the engagement? *Rubric:* 3 = CISO (with product owner acceptance); 2 = CISO; 1 = Leo; 0 = none.
- **EX009 — SOC role.** What does the SOC need to know before testing starts? *Rubric:* 3 = window, source IPs, expected noisy methods; so they do not treat test as real attack blindly; 2 = partial; 1 = nothing; 0 = none.
- **EX010 — Third party.** May HCU's ROE alone authorize testing the card processor? *Rubric:* 3 = no; processor's own authorization required; 2 = no; 1 = yes; 0 = none.

### Synthesis

Services, owners, exclusions and third parties belong in the plan before any method is chosen.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) complete a rules-of-engagement checklist; (2) explain evidence retention and redaction; (3) refuse work that lacks an emergency contact; (4) describe chain of custody for test data.

### 3.1 Checklist before kickoff

Every required field of the rules of engagement must be filled: scope, exclusions, methods, window, emergency contact, data handling and report audience. An empty emergency contact stops the test.

```python
"""Lab 3: validate a synthetic rules-of-engagement checklist before testing starts."""
required = ["in_scope", "out_of_scope", "allowed_methods", "window", "emergency_contact",
            "data_handling", "report_audience"]
draft = {"in_scope": "192.0.2.0/24 web and VPN", "out_of_scope": "core banking AS/400",
         "allowed_methods": "config review, authenticated web tests", "window": "Sat 08:00-12:00",
         "emergency_contact": "", "data_handling": "delete within 30 days", "report_audience": "CISO"}
missing = [k for k in required if not draft.get(k)]
print("complete" if not missing else "MISSING: " + ", ".join(missing))
for k in required:
    print(f"  {k}: {draft.get(k) or '(empty)'}")
```

Run with `python3 lab_roe.py`. Verified output:

```text
MISSING: emergency_contact
  in_scope: 192.0.2.0/24 web and VPN
  out_of_scope: core banking AS/400
  allowed_methods: config review, authenticated web tests
  window: Sat 08:00-12:00
  emergency_contact: (empty)
  data_handling: delete within 30 days
  report_audience: CISO
```

### 3.2 Evidence rules

Capture only what proves the finding. Redact member identifiers. Store evidence in the approved repository with access limited to the engagement team. Delete or return it when the agreement says so.

### 3.3 Chain of custody

Note who collected each item, when, and every hand-off. For classroom labs the log is short; for real exams it can be scrutinised.

### 3.4 Personal devices

Do not keep HCU evidence on personal laptops or chat apps. Use the issued environment.

### 3.5 Classroom versus production

These labs validate checklists on synthetic drafts; they do not replace a legal review of a real ROE.

### 3.6 When the checklist fails

If any required ROE field is empty on the morning of the test, Leo cancels the window in writing and informs the CISO and SOC. Restarting after a scramble to fill fields produces mistakes; a clean postponement is cheaper than an unauthorized hour.

### 3.7 Agreement beats habit

Even if Leo tested the same staging site last quarter, he does not reuse last quarter's ROE. Systems, owners and exclusions change. Each engagement starts from a current signed agreement, and the checklist is run against that agreement, not against memory.

### Worked example (synthetic HCU)

Leo runs the checklist on the draft ROE. It prints MISSING: emergency_contact. He will not schedule the Saturday window until the CISO names an on-call contact and the field is filled.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX011 — Missing field.** What does the lab print as the status line, and what must Leo do? *Rubric:* 3 = MISSING: emergency_contact; do not start until filled; 2 = missing only; 1 = start anyway; 0 = none.
- **EX012 — Filled contact.** If emergency_contact becomes "SOC on-call +1-555-0100", what is the status line? *Rubric:* 3 = complete; 2 = ok; 1 = still missing; 0 = none.
- **EX013 — Redaction.** A screenshot shows a member's full account number. What before filing? *Rubric:* 3 = redact/mask; keep only digits needed to prove issue; 2 = partial; 1 = file as-is; 0 = none.
- **EX014 — Personal chat.** May Leo paste evidence into a private WhatsApp chat with a colleague? *Rubric:* 3 = no; use approved repository only; 2 = no; 1 = yes if private; 0 = none.
- **EX015 — Custody note.** Write a one-line custody entry for a config export. *Rubric:* 3 = who, what, when, from where; 2 = two fields; 1 = vague; 0 = none.

### Synthesis

No emergency contact, no test; evidence is minimised, retained as agreed and never parked on personal devices.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Core methods

### Learning outcomes

You will (1) describe PTES stages in order; (2) separate discovery from validation; (3) explain why exploitation is optional and constrained; (4) choose methods that match HCU's ROE.

### 4.1 PTES backbone

PTES stages give a shared order: pre-engagement (scoping), intelligence gathering, threat modelling, vulnerability analysis, exploitation, post-exploitation and reporting. HCU's ROE currently allows analysis and authenticated web tests, not broad exploitation.

### 4.2 Discovery versus validation

Discovery lists possible issues; validation confirms them with evidence inside the rules. Tool output alone is discovery. A confirmed misconfiguration with a screenshot and business impact is a finding.

### 4.3 Constrained exploitation

If the ROE later allows proving a flaw, use the minimum step that shows impact, on agreed accounts, with a stop if anything unexpected happens. This course still does not teach exploit development.

### 4.4 Matching methods to ROE

Leo's plan maps each method to an ROE line. Anything not mapped is out.

### 4.5 Threat modelling light

Even without a full red-team scenario, name the likely actors (stolen member password, phishing of staff) so checks focus on what matters to HCU.

### 4.6 Intelligence gathering limits

OSINT on HCU stays with public pages and published documents. Scraping member forums, buying breach data or impersonating staff are out unless the ROE explicitly allows a social-engineering scenario — which HCU's current ROE does not.

### 4.7 Reporting as a method stage

PTES ends with reporting because findings that never reach owners change nothing. Leo budgets time for writing and review inside the engagement window rather than treating the report as unpaid overtime after testing.

### Worked example (synthetic HCU)

Leo's method table: OSINT on public HCU pages (allowed); authenticated WSTG checks on online banking staging (allowed); password spraying (forbidden); AS/400 probes (out of scope).

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX016 — Stage order.** Put in order: reporting, vulnerability analysis, pre-engagement, exploitation. *Rubric:* 3 = pre-engagement, vuln analysis, exploitation, reporting; 2 = mostly; 1 = random; 0 = none.
- **EX017 — Discovery or finding.** Tool reports outdated-banner at confidence 0.7. Is that a finding yet? *Rubric:* 3 = discovery until validated with evidence and impact; 2 = partial; 1 = already finding; 0 = none.
- **EX018 — Why spraying is forbidden.** Why does HCU forbid password spraying? *Rubric:* 3 = lockouts/member harm/noisy; not in allowed methods; 2 = partial; 1 = "slow"; 0 = none.
- **EX019 — Minimum proof.** What does "minimum step that shows impact" mean? *Rubric:* 3 = stop once impact shown; no extra pivoting; 2 = partial; 1 = full domain takeover always; 0 = none.
- **EX020 — Map a method.** Map "authenticated WSTG checks on staging" to ROE language. *Rubric:* 3 = cites allowed_methods and in_scope staging; 2 = partial; 1 = unmapped; 0 = none.

### Synthesis

Methods follow PTES order and the ROE; discovery becomes a finding only after validated evidence.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Tools and interpretation

### Learning outcomes

You will (1) treat scanners as assistants not judges; (2) filter findings by confidence and confirmation; (3) explain false positives and false negatives; (4) record tool versions in evidence.

### 5.1 Tools assist

Scanners and checklists speed discovery. They mislabel, miss context and cannot judge business impact. Leo reads every kept item.

### 5.2 Confidence floor

HCU drops unconfirmed items below a confidence floor so the report is not padded with noise.

```python
"""Lab 5: filter a synthetic tool finding list, dropping noise below a confidence floor."""
findings = [("open-redirect", 0.9, True), ("dir-listing", 0.4, False),
            ("outdated-banner", 0.7, True), ("cookie-flag", 0.85, True), ("trace-method", 0.3, False)]
FLOOR = 0.6
kept = [(n, c) for n, c, confirmed in findings if c >= FLOOR and confirmed]
for n, c in kept:
    print(f"KEEP {n:16} confidence={c}")
print(f"kept {len(kept)} of {len(findings)}; dropped {len(findings)-len(kept)}")
```

Run with `python3 lab_severity.py`. Verified output:

```text
KEEP open-redirect    confidence=0.9
KEEP outdated-banner  confidence=0.7
KEEP cookie-flag      confidence=0.85
kept 3 of 5; dropped 2
```

### 5.3 False positives and negatives

A false positive wastes fixer time; a false negative leaves risk. Sampling and manual validation reduce both; neither reaches zero.

### 5.4 Versions and settings

Record tool name, version and profile with the evidence so a retest can use the same setup.

### 5.5 OWASP WSTG as a tool of thought

Even without a scanner, WSTG gives a structured list of web checks so coverage is visible.

### 5.6 Interpreting banners

An outdated banner is a clue, not a crisis. Leo checks whether the service is internet-facing, whether the version is truly vulnerable, and whether a WAF or access rule already limits exposure before he writes a high-severity finding.

### 5.7 Base rates

If a scanner marks forty items and history shows thirty were false positives, Leo plans validation time accordingly. He does not promise the CISO "forty findings" before validation; he promises a validated set.

### 5.8 Manual spot checks

For every five automated items kept, Leo manually validates at least the highest-severity one end-to-end with an authorized account. Spot checks catch systematic tool mistakes that a confidence score cannot.

### Worked example (synthetic HCU)

Leo filters the synthetic list: open-redirect, outdated-banner and cookie-flag are kept; dir-listing and trace-method drop. He still manually validates the three kept items before they enter the report.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX021 — Lab keep count.** How many findings does the lab keep, and which are dropped? *Rubric:* 3 = 3 kept; dir-listing and trace-method dropped; 2 = count only; 1 = wrong; 0 = none.
- **EX022 — Raise the floor.** If FLOOR becomes 0.8, which items remain? *Rubric:* 3 = open-redirect and cookie-flag only; 2 = one; 1 = all three; 0 = none.
- **EX023 — False positive.** Give an HCU example of a false positive. *Rubric:* 3 = scanner flags issue that staging config shows is mitigated; 2 = partial; 1 = none; 0 = none.
- **EX024 — False negative.** Give an HCU example of a false negative. *Rubric:* 3 = issue exists but tool misses (e.g. auth logic flaw); 2 = partial; 1 = none; 0 = none.
- **EX025 — Version note.** Write the tool line Leo adds to evidence. *Rubric:* 3 = name, version, profile/settings; 2 = name only; 1 = vague; 0 = none.

### Synthesis

Tools propose; humans dispose — filter, validate, record versions, then report.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operational workflow

### Learning outcomes

You will (1) describe the day-of workflow from kickoff to debrief; (2) keep a contemporaneous activity log; (3) coordinate with the SOC; (4) handle a mid-test scope question.

### 6.1 Day-of sequence

Kickoff call confirms ROE and contacts; testers begin only inside the window; progress notes go to the engagement channel; mid-point check with the product owner if anything sensitive appears; end-of-day debrief; evidence vaulted.

### 6.2 Activity log

Every action gets a time, system, method and result. The log defends the team if an outage is blamed on testing and feeds the report.

### 6.3 SOC coordination

Send start and stop messages. If the SOC sees related alerts, they call the emergency contact rather than blocking Leo's access without notice.

### 6.4 Mid-test questions

New hostname discovered? Pause and ask. Do not "just include it."

### 6.5 End state

At stop time, stop. Unfinished checks become next-window work or explicit out-of-time notes — not silent overruns.

### 6.6 Handover between testers

If Leo ends his shift and a colleague continues, the activity log and evidence vault are the handover. Verbal notes are not enough; the colleague must see what was already validated so they do not retest destructively or miss a stop condition.

### 6.7 Communication channel discipline

Engagement chat is for scope, stops and status — not for jokes about "hacking the bank". Casual language leaks into screenshots and damages trust if an examiner later reads the channel.

### 6.8 Window extensions

If work must continue past the window, Leo stops, requests a written extension from the CISO, and waits for confirmation before any further packet leaves his laptop. Verbal "sure, keep going" is not enough.

### Worked example (synthetic HCU)

At 08:05 Leo posts "ENG-440 start — staging only". At 09:40 he finds a hostname that might be production; he pauses, asks the product owner, learns it is staging, logs the decision, continues.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX026 — Start message.** What four facts belong in Leo's start message? *Rubric:* 3 = ticket/id, scope reminder, window, tester contact; 2 = three; 1 = one; 0 = none.
- **EX027 — Log line.** Write one activity-log line for a WSTG session check. *Rubric:* 3 = time, system, method, result; 2 = three; 1 = vague; 0 = none.
- **EX028 — SOC alert.** SOC calls about alerts from Leo's IP. What does he do? *Rubric:* 3 = confirm authorized test; share window/ticket; adjust rate if asked; 2 = partial; 1 = ignore; 0 = none.
- **EX029 — New hostname.** Correct process when a new hostname appears. *Rubric:* 3 = pause; ask owner; written scope update if needed; 2 = partial; 1 = test it; 0 = none.
- **EX030 — Stop time.** The window ends with one check unfinished. What does Leo do? *Rubric:* 3 = stop; note unfinished for next window; 2 = stop; 1 = overrun; 0 = none.

### Synthesis

Workflow is kickoff, logged work, SOC visibility and pause-to-ask — never silent scope creep.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Controls and verification

### Learning outcomes

You will (1) suggest controls that match findings; (2) distinguish compensating controls; (3) plan a retest; (4) know when a control is verified.

### 7.1 Match control to finding

A shared admin password finding wants named accounts and vaulting; an open redirect wants allow-listed destinations; a missing cookie flag wants the flag set and checked in CI.

### 7.2 Compensating controls

When the ideal fix is months away, a compensating control reduces risk now — for example, VPN admin paths restricted to jump hosts while password reuse is being eliminated.

### 7.3 Retest design

Retest only the agreed findings, with the same or equivalent method, after the owner says the fix is live. Record pass or fail with evidence.

### 7.4 Verified means

Verified means Leo reproduced the original symptom as fixed (or confirmed the compensating control works), not that the owner said they fixed it.

### 7.5 Tracking

Findings become tickets with owners and dates; verification closes them.

### 7.6 Partial fixes

Sometimes owners fix one path and leave another open. Leo's retest checklist names each path from the original finding. A ticket is not closed until every listed path fails to reproduce the issue or an accepted compensating control is verified.

### 7.7 Verification owners

The person who applies a fix should not be the only person who marks it verified. Leo or another tester retests; the owner confirms deployment. Separation keeps wishful closures out of the metrics.

### 7.8 Regression watch

After a fix, Leo asks whether related paths were checked by the owner. A patched open redirect that leaves a second parameter untouched is a common regression; the retest plan names siblings when they exist.

### Worked example (synthetic HCU)

For the shared VPN admin password, HCU enables MFA and named accounts in two weeks (ideal) and, meanwhile, restricts admin paths to the jump host (compensating). Leo retests both.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX031 — Control match.** Suggest a control for open redirect. *Rubric:* 3 = allow-list redirect targets / remove parameter; 2 = partial; 1 = "firewall"; 0 = none.
- **EX032 — Compensating example.** Give one compensating control for password reuse on VPN admin. *Rubric:* 3 = restrict admin to jump host / MFA / monitoring; 2 = partial; 1 = ignore; 0 = none.
- **EX033 — Retest trigger.** When does retest start? *Rubric:* 3 = after owner confirms fix live / in agreed window; 2 = partial; 1 = immediately always; 0 = none.
- **EX034 — Not verified.** Owner emails "we fixed it" with no details. Is it verified? *Rubric:* 3 = no; need retest evidence; 2 = no; 1 = yes; 0 = none.
- **EX035 — Retest scope.** May Leo test unrelated new URLs during retest? *Rubric:* 3 = no; only agreed findings unless scope extended; 2 = no; 1 = yes; 0 = none.

### Synthesis

Controls match findings; compensating controls buy time; verification is a retest with evidence.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Supervised case analysis

### Learning outcomes

You will (1) analyse a synthetic HCU case file; (2) separate facts from guesses; (3) propose next authorized steps; (4) escalate when needed.

### 8.1 The case file

A synthetic packet holds: ROE excerpt, three validated findings, activity log, and a note that a staff member reused the VPN password on a personal email (reported by the staff member).

### 8.2 Facts versus guesses

Fact: password reuse was reported. Guess: an attacker already has the password. Leo labels guesses clearly.

### 8.3 Next steps inside ROE

Force VPN password reset for that account; check VPN logs for unusual sessions; do not touch personal email (out of scope).

### 8.4 Escalation

Member-data exposure risk and password reuse across personal services go to the CISO the same day.

### 8.5 ATT&CK label

Password reuse enabling VPN access maps to T1078 Valid Accounts for the SOC's detection search.

### 8.6 Writing for the case file

Case notes use timestamps, ticket ids and labels Fact/Guess/Action. Free-form narrative is fine for the summary, but the labelled lines are what the CISO and auditors can scan in a minute during an incident.

### 8.7 Time to escalate

Leo uses a simple rule: if member funds, large-scale personal data or safety systems might be affected, escalate within an hour. Lower-impact items follow the normal finding process.

### 8.8 SOC collaboration on the case

Leo shares the ATT&CK technique and account id with the SOC so they can hunt, but he does not paste member PII into the ticket. Hunt queries use account handles and time ranges.

### Worked example (synthetic HCU)

Leo's case note: "Facts: staff report of VPN password reused on personal email; Findings F1–F3 validated. Guesses: none about external abuse yet. Actions: reset, log review, CISO brief. Out of scope: personal email content."

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX036 — Fact extract.** List two facts from the case file. *Rubric:* 3 = two clearly factual items; 2 = one; 1 = guess as fact; 0 = none.
- **EX037 — Guess label.** Rewrite "attackers definitely have the password" as a labelled guess. *Rubric:* 3 = labelled uncertainty; 2 = partial; 1 = still certain; 0 = none.
- **EX038 — Out of scope action.** Why not read the staff member's personal email? *Rubric:* 3 = out of scope / no authorization / privacy; 2 = partial; 1 = should read; 0 = none.
- **EX039 — Same-day escalate.** What triggers same-day CISO escalation here? *Rubric:* 3 = credential reuse risk to VPN/member services; 2 = partial; 1 = nothing; 0 = none.
- **EX040 — ATT&CK.** Which technique name helps the SOC search detections for this case? *Rubric:* 3 = T1078 Valid Accounts; 2 = name only; 1 = wrong; 0 = none.

### Synthesis

Case work separates facts from guesses, acts only inside scope and escalates real risk the same day.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) write for executives and for engineers; (2) handle pressure to hide findings; (3) apply responsible disclosure ethics; (4) structure the HCU report.

### 9.1 Two voices

Executives get risk, affected members, decisions and dates. Engineers get reproduction, evidence and fix guidance. Mixing them produces a report nobody finishes.

### 9.2 Pressure

Someone may ask to drop a finding before an exam. Leo's answer: findings stay; owners may add a management response. Ethics beat convenience.

### 9.3 Responsible handling

Do not publish HCU findings publicly. Do not share with friends. Vendor bugs found in third-party software follow the vendor's disclosure path only with CISO approval.

### 9.4 Report structure

Executive summary; scope and methods; findings by severity; positive observations; retest plan; appendices.

### 9.5 Threat-led language

If HCU later sponsors a CBEST or TIBER-EU style test, reports also describe scenarios and detection gaps, still without publishing exploit detail.

### 9.6 Positive observations

Reports should also note what worked: MFA on VPN, rapid SOC response to the start message, clean staging isolation. Positive observations show balance and tell leaders which investments are paying off.

### 9.7 Clear recommendations

Each finding's recommendation names a concrete change, an owner role and a suggested date. "Improve security" is not a recommendation; "set Cookie Secure and HttpOnly on the session cookie in the online-banking app by 1 November, owner: app-sec" is.

### 9.8 Review before send

A peer reads the executive summary for blame language, missing decisions and unexplained jargon. Ten minutes of review prevents a rewrite under examiner pressure.

### Worked example (synthetic HCU)

A product manager asks Leo to remove the open-redirect finding until after the exam. Leo refuses, offers to include the manager's remediation plan beside the finding, and informs his supervisor.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX041 — Exec sentence.** Write one executive sentence for open redirect on online banking. *Rubric:* 3 = risk to members + decision ask; 2 = partial; 1 = jargon only; 0 = none.
- **EX042 — Engineer detail.** What three technical points do engineers need? *Rubric:* 3 = reproduction, evidence ref, fix guidance; 2 = two; 1 = one; 0 = none.
- **EX043 — Drop request.** How does Leo answer a request to drop a finding? *Rubric:* 3 = refuse; offer management response; tell supervisor; 2 = refuse; 1 = drop it; 0 = none.
- **EX044 — Public blog.** May Leo blog about HCU's findings after the test? *Rubric:* 3 = no; confidential under agreement; 2 = no; 1 = yes anonymised freely; 0 = none.
- **EX045 — Report order.** Order: appendices, executive summary, findings. *Rubric:* 3 = summary, findings, appendices; 2 = partial; 1 = wrong; 0 = none.

### Synthesis

Tell the truth in the right voice; never drop findings under pressure; keep results inside the agreement.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Quality and troubleshooting

### Learning outcomes

You will (1) review tickets for completeness; (2) troubleshoot a stalled remediation; (3) measure engagement quality; (4) fix process gaps without blame.

### 10.1 Complete tickets

Each remediation ticket needs an owner, a due date and a verification note. Incomplete tickets hide risk.

### 10.2 Stalled fixes

If a due date passes, Leo checks whether the owner changed, the fix is blocked, or the finding was misunderstood — then escalates with facts.

### 10.3 Quality metrics

Useful metrics: percent of findings with owners, median time to retest, count of scope pauses. Vanity metrics (raw finding count) mislead.

```python
"""Lab 10: check synthetic remediation tickets for owner, due date and verification note."""
tickets = [
    {"id": "T-12", "owner": "app-sec", "due": "2026-11-01", "verified": "retest ok"},
    {"id": "T-15", "owner": "", "due": "2026-11-01", "verified": ""},
    {"id": "T-18", "owner": "network", "due": "", "verified": "pending"},
    {"id": "T-21", "owner": "app-sec", "due": "2026-10-20", "verified": "retest ok"},
]
for t in tickets:
    gaps = [k for k in ("owner", "due", "verified") if not t[k]]
    print(f"{t['id']} {'OK' if not gaps else 'INCOMPLETE: ' + ','.join(gaps)}")
print("closed-ready:", sum(1 for t in tickets if t["owner"] and t["due"] and t["verified"] == "retest ok"))
```

Run with `python3 lab_ticket.py`. Verified output:

```text
T-12 OK
T-15 INCOMPLETE: owner,verified
T-18 INCOMPLETE: due
T-21 OK
closed-ready: 2
```

### 10.4 Blameless process fixes

If two tickets lacked owners, improve the template rather than only criticising people.

### 10.5 Troubleshooting tests

When a retest fails unexpectedly, verify you hit the same system and version the owner fixed.

### 10.6 Retest failures

If a retest still finds the issue, Leo files evidence, keeps the ticket open, and asks whether the fix was deployed to the system he tested. Many "failed retests" are version mismatches, not ignored work.

### 10.7 Sampling quality

Once a month Leo samples five closed tickets and checks that evidence of verification exists. Missing evidence reopens the ticket. Sampling catches process drift early.

### 10.8 Escalation ladder

Tickets slip first to the owner, then to the owner's manager, then to the CISO with the original due date and the number of nudges. The ladder is written so escalation is not personal.

### Worked example (synthetic HCU)

Leo's ticket check shows T-12 and T-21 closed-ready; T-15 lacks owner and verified; T-18 lacks due. He assigns T-15 to app-sec, sets T-18's due date with network, and updates the ticket template to require those fields.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX046 — Closed-ready count.** What does the lab print for closed-ready? *Rubric:* 3 = closed-ready: 2; 2 = 2; 1 = 4; 0 = none.
- **EX047 — T-15 gaps.** What is wrong with T-15? *Rubric:* 3 = missing owner and verified; 2 = one; 1 = nothing; 0 = none.
- **EX048 — Stall questions.** Give two questions Leo asks when a due date slips. *Rubric:* 3 = two of owner change, blocker, misunderstanding, priority; 2 = one; 1 = blame; 0 = none.
- **EX049 — Bad metric.** Why is "number of findings" a weak quality metric? *Rubric:* 3 = encourages noise / punishes thorough scoping; 2 = partial; 1 = it is best; 0 = none.
- **EX050 — Template fix.** What template change prevents the T-15/T-18 gaps? *Rubric:* 3 = require owner, due, verified before ticket can leave triage; 2 = partial; 1 = none; 0 = none.

### Synthesis

Quality is complete tickets, honest metrics and process fixes when the same gap repeats.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) run a supervised lab using only synthetic data and prior labs; (2) produce a mini report; (3) peer-review another learner's scope check; (4) reflect on mistakes.

### 11.1 Lab brief

Using lab_roe, lab_severity and lab_ticket outputs already produced, build a three-section mini report for HCU: authorization readiness, discovery filter result, remediation hygiene.

### 11.2 Peer review

Swap scope-check notes with a peer. Score 0–3 on: exclusions present, emergency contact present, methods match ROE.

### 11.3 Reflection

Write three lines: what you nearly did wrong, what caught it, what you will do next time.

### 11.4 Supervisor gate

The supervisor signs only if exclusions and emergency contact are present and no out-of-scope target appears.

### 11.5 Time box

The lab runs in one sitting with a hard stop, practising window discipline.

### 11.6 Pairing rule

During the supervised lab, one learner drives and one checks the ROE on every step. Roles swap halfway. The checker may halt the driver at any time; halts are scored as good catches, not as failures.

### 11.7 Lab evidence pack

The mini report appendix includes the raw lab outputs (lab_roe, lab_severity, lab_ticket) so the supervisor can recompute the same conclusions. Screenshots of chat are optional; reproducible outputs are required.

### 11.8 Cleanup

At lab end, Leo deletes local copies of synthetic evidence from the desktop and confirms the vault holds the only copy. Cleanup is part of the graded checklist.

### 11.9 After sign-off

When the supervisor signs, Leo files the mini report under ENG-CLASS-11 and schedules a fifteen-minute debrief with his mentor to turn the reflection lines into checklist updates for the real ROE process.

### Worked example (synthetic HCU)

Leo's reflection: "Nearly scheduled without emergency contact; checklist caught it; next time I run lab_roe before proposing any window." Supervisor signs his mini report.

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX051 — Mini report sections.** Name the three sections of the lab brief. *Rubric:* 3 = authorization readiness, discovery filter, remediation hygiene; 2 = two; 1 = one; 0 = none.
- **EX052 — Peer score item.** Name two peer-review scoring items. *Rubric:* 3 = two of exclusions, emergency contact, methods match; 2 = one; 1 = vague; 0 = none.
- **EX053 — Supervisor refusal.** What missing item makes the supervisor refuse to sign? *Rubric:* 3 = missing exclusions or emergency contact or out-of-scope target present; 2 = partial; 1 = low finding count; 0 = none.
- **EX054 — Reflection quality.** What makes a useful reflection line? *Rubric:* 3 = specific mistake, detector, next behaviour; 2 = partial; 1 = "I did fine"; 0 = none.
- **EX055 — Synthetic only.** Why does this lab forbid live scanning of HCU? *Rubric:* 3 = authorization/classroom limits; synthetic data enough for skills; 2 = partial; 1 = live is fine; 0 = none.

### Synthesis

The supervised lab proves you can refuse incomplete authorizations, filter noise and close the loop — on synthetic data.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a portfolio of artifacts from this course; (2) present to a supervisor; (3) identify gaps for the next course; (4) restate standing safety rules.

### 12.1 Portfolio contents

ROE checklist result; scope-check output; filtered finding list; one executive finding paragraph; one engineer finding paragraph; ticket hygiene screenshot; reflection from the supervised lab.

### 12.2 Presentation

Ten minutes: context of HCU, how you stayed in scope, top two findings, verification plan, what you will not do alone yet.

### 12.3 Gaps

Leo notes he has not yet led a threat-led (CBEST/TIBER-style) scenario or a full WSTG pass — topics for longer courses.

### 12.4 Standing rules

No authorization, no test. No exploit code on real systems. Stop means stop. Evidence stays controlled.

### 12.5 Handoff

Store the portfolio in HCU's training record so the next supervisor sees evidence, not only a completion tick.

### 12.6 Portfolio integrity

Artifacts in the portfolio must be the ones Leo actually produced in this course, with dates. Replacing them with polished samples from the internet misrepresents skill and is treated as academic dishonesty.

### 12.7 Continuing education

After acceptance, Leo schedules one skill to deepen each month — this quarter, OWASP WSTG session management — and records it next to the portfolio so progress is visible.

### 12.8 Safety restatement on the portfolio cover

The first page of Leo's portfolio states: no real systems were tested in this course; all labs used synthetic data; exploit code was neither used nor requested.

### Worked example (synthetic HCU)

Leo presents; the supervisor accepts the portfolio with one action: add the emergency-contact near-miss to the team onboarding page. Next course link: AI security (043).

> **Synthetic case — Harborline Credit Union (HCU).** The credit union, Leo Okonkwo and all figures are invented for teaching.

### Errors and limits

Local policies and laws differ; follow HCU's authorization and your jurisdiction. This book never authorizes testing of real systems.

### Exercises

- **EX056 — Seven artifacts.** List five portfolio artifacts. *Rubric:* 3 = five from the contents list; 2 = three; 1 = one; 0 = none.
- **EX057 — Presentation must-say.** What must Leo say about scope in the presentation? *Rubric:* 3 = how he stayed in scope / exclusions / pause-to-ask; 2 = partial; 1 = skip it; 0 = none.
- **EX058 — Gap honesty.** Why list gaps in the portfolio? *Rubric:* 3 = shows limits; guides next training; builds trust; 2 = partial; 1 = hide gaps; 0 = none.
- **EX059 — Standing rule.** State the standing rule about exploit code. *Rubric:* 3 = never on real systems / not taught for use outside auth lab policy; 2 = partial; 1 = ok if careful; 0 = none.
- **EX060 — Next course.** What is the next course number and topic? *Rubric:* 3 = 043 AI security; 2 = AI; 1 = wrong; 0 = none.

### Synthesis

A portfolio proves authorized practice; gaps and safety rules travel with you to the next course.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Harborline Credit Union, Leo Okonkwo and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** Architecture, security monitoring and incident response (patching and staff training also count).

**EX002.** Confidentiality; integrity; availability.

**EX003.** A teller account that can view balances but cannot approve wires above a set amount.

**EX004.** Attackers who bypass or abuse an allowed path still face application checks, identity controls and monitoring; one layer failing should not expose everything.

**EX005.** OWASP Web Security Testing Guide — it is organised around web application test cases.

**EX006.** Online banking, staff VPN, email, member website, core banking AS/400.

**EX007.** It is the system of record for balances; testing mistakes could halt branches, so it needs a specialised, carefully controlled engagement if tested at all.

**EX008.** The CISO authorises; the online-banking product owner accepts residual risk for that service.

**EX009.** The time window, source addresses and which methods may look like attacks, so analysts can distinguish authorized testing from a real incident.

**EX010.** No. The card processor is a separate organisation; its systems need its own written authorization.

**EX011.** `MISSING: emergency_contact` — he blocks the kickoff until the CISO provides a contact and the checklist passes.

**EX012.** `complete`

**EX013.** Mask the account number so the finding remains provable without exposing the member's identifier.

**EX014.** No. Evidence stays in the approved repository under the agreement's access rules.

**EX015.** "2026-10-18 09:12 Leo Okonkwo exported VPN config from jump host JUMP-1 under ticket ENG-440; stored in evidence/ENG-440/vpn.txt."

**EX016.** Pre-engagement, vulnerability analysis, exploitation, reporting.

**EX017.** It is discovery until someone confirms it, records evidence and explains impact under the ROE.

**EX018.** It can lock member or staff accounts and disrupt service; it is outside the allowed methods list.

**EX019.** Demonstrate the security effect with the least action needed, then stop — no extra systems or data access.

**EX020.** Allowed under "authenticated web tests" against the in-scope online banking staging system.

**EX021.** Kept 3 of 5; dropped dir-listing and trace-method.

**EX022.** open-redirect (0.9) and cookie-flag (0.85); outdated-banner (0.7) drops.

**EX023.** A scanner reports directory listing, but the staging server returns a login page for that path when checked with an authorized account.

**EX024.** An access-control flaw on a transfer page that no scanner checks because it needs a valid member session and business steps.

**EX025.** "OWASP ZAP 2.15, API scan profile 'HCU-staging-auth', run 2026-10-18 by Leo Okonkwo."

**EX026.** Engagement id, systems in scope, time window and a reachable contact for the tester.

**EX027.** "09:12 staging.examplebank.test — WSTG session timeout check — cookie persisted after logout — evidence E14."

**EX028.** Confirm it is ENG-440, share the ROE window and ticket, and reduce rate or pause if the SOC asks.

**EX029.** Pause testing of that name, ask the product owner or CISO, and continue only after a recorded scope decision.

**EX030.** Stop on time, record the unfinished check, and schedule it only inside a new authorized window.

**EX031.** Allow-list the redirect destinations or remove user-controlled redirects.

**EX032.** Restrict VPN admin interfaces to the jump host network and require MFA while passwords are uniqued.

**EX033.** After the owner states the fix is deployed and within the retest window in the ticket.

**EX034.** No. Verification requires Leo's retest evidence, not only an email.

**EX035.** No. Retest stays on the agreed findings unless a written scope extension says otherwise.

**EX036.** The ROE excludes personal email; a staff member reported reusing the VPN password on personal email.

**EX037.** "Guess (unconfirmed): the password may also be known to others if the personal email was breached; no HCU log evidence yet."

**EX038.** Personal email is outside HCU authorization and privacy boundaries; HCU can reset its own VPN credentials without reading it.

**EX039.** A VPN password exposed outside HCU could let someone reach staff services; that risk needs CISO visibility immediately.

**EX040.** T1078 Valid Accounts.

**EX041.** "Online banking can send members to attacker-controlled sites after login; we ask approval to fix within seven days."

**EX042.** Reproduction steps, evidence reference and concrete fix guidance.

**EX043.** Refuse to remove it, offer to print a management response next to it, and tell his supervisor about the request.

**EX044.** No. Engagement results are confidential under the agreement unless HCU explicitly authorises a public release.

**EX045.** Executive summary, then findings, then appendices.

**EX046.** `closed-ready: 2`

**EX047.** INCOMPLETE: owner,verified

**EX048.** Has the owner changed? What blocker is open? Was the finding misunderstood?

**EX049.** It rewards filing noise and punishes careful validation; severity and closure quality matter more.

**EX050.** Make owner, due date and verification fields mandatory before a ticket leaves triage.

**EX051.** Authorization readiness, discovery filter result and remediation hygiene.

**EX052.** Exclusions present; emergency contact present; methods match the ROE.

**EX053.** Missing exclusions, missing emergency contact, or any out-of-scope target in the plan.

**EX054.** It names a specific near-miss, what caught it and a concrete next-time behaviour.

**EX055.** The classroom authorization covers synthetic exercises only; live scanning needs a separate ROE and would risk real services.

**EX056.** ROE checklist result, scope-check output, filtered findings, executive paragraph, engineer paragraph (tickets and reflection also count).

**EX057.** How he stayed inside the ROE, including exclusions and at least one pause-to-ask example.

**EX058.** Honest limits guide the next course and show the supervisor what not to assign unsupervised yet.

**EX059.** Never use exploit code against real systems; this course does not provide it.

**EX060.** Course 043: AI security.

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
