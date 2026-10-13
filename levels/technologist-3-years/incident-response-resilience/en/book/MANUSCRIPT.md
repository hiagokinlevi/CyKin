# Incident Response and Cyber Resilience: Building and Running the Response Service

- Language: English (`en`); technologist course, three years; approximately 2400 hours of planned study (course 085 of 207 in the [study path](../../../../../STUDY_PATH.md)).
- Editorial state: **draft**. Chapters 1–30 of 30 have authored teaching text, exercises EX001–EX090 and matching worked results; five chapters include an offline Python lab whose printed output was verified with Python 3 and the standard library. Independent subject-matter review, source re-verification, accessibility review, language editing and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: technology implementers and administrators — system, network, identity, cloud and service-desk staff and junior security operators — who will build, operate and maintain an organization's incident response service day to day.
- Relation to the other books in this area: the practitioner books ([rapid](../../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [professional](../../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md), [technical](../../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md)) teach how to act in a response; the [bachelor's book](../../../../bachelors-4-years/incident-response-resilience/en/book/MANUSCRIPT.md) builds foundations and applied judgement; the [engineering book](../../../../engineering-5-years/incident-response-resilience/en/book/MANUSCRIPT.md) designs response systems as a multi-year engineering programme; the [postgraduate book](../../../../postgraduate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) teaches specialist command and coordination; the [master's](../../../../masters-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) and [doctoral](../../../../doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) books teach research. **This technologist book teaches implementation and operation**: mapping systems and evidence, configuring tools and evidence flows, building tested containment and recovery actions, integrating with service management, automating safely, measuring the service and keeping it running.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited works keep their own rights.
- Educational boundary: an independent educational blueprint, not an accredited qualification, legal advice or authority to access any real system or data. Every organization (notably the fictional municipal provider **Fernmoor City Services** and its suppliers), person, account, address, case and number in an example or exercise is **synthetic** unless a sentence cites a public source. Addresses use the RFC 5737 documentation ranges and domains use `example`.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read the thirty chapters in order; together they build and run one incident response service for a fictional city services provider. Chapters 1–9 lay the technical foundations a response implementer needs: systems, networks, programming, data models, security vocabulary, operating systems, identity, architecture and measurement. Chapters 10–15 establish the service: charter and roles, inventory, evidence flows, severity and triage, intake and a guided timeline lab. Chapters 16–20 implement investigation methods, case and evidence tooling, containment and recovery controls, detection feedback and record repair. Chapters 21–25 integrate the service with IT service management, automate it, evaluate it and design workflows with peers. Chapters 26–30 operate it: handoffs and communications, workflow deployment, an authorized field simulation, the integrated capstone and the improvement dossier.

Each chapter has learning outcomes, teaching sections, a synthetic worked example, common errors and limits, three exercises with 0–3 rubrics and a synthesis, followed by a **Continue studying** block. Labs in Chapters 9, 15, 22, 23 and 27 run offline with the Python 3 standard library; compare your output with the printed expected output and investigate any difference.

Three habits run through the book: **preserve before you change** (evidence first, then containment), **verify before you declare** (an action is done only when a test proves it), and **record so others can repeat** (owners, times, hashes, decisions and corrections in the case).

## Contents

1. [Computing systems](#ch-01)
2. [Networks and internet services](#ch-02)
3. [Programming foundations](#ch-03)
4. [Data models](#ch-04)
5. [Security literacy](#ch-05)
6. [Operating systems and virtualization](#ch-06)
7. [Identity and access foundations](#ch-07)
8. [Security architecture basics](#ch-08)
9. [Evidence and measurement](#ch-09)
10. [Incident response service model and operating roles](#ch-10)
11. [Asset inventory and business-service dependencies](#ch-11)
12. [Evidence flows across identity, endpoint and cloud](#ch-12)
13. [Incident risk scenarios and triage thresholds](#ch-13)
14. [Case intake, scope and ownership methods](#ch-14)
15. [Guided lab: reconstruct a bounded incident timeline](#ch-15)
16. [Investigation methods across multiple data sources](#ch-16)
17. [Case-management and evidence-storage tooling](#ch-17)
18. [Containment and recovery control implementation](#ch-18)
19. [Detection-to-response monitoring and feedback](#ch-19)
20. [Troubleshoot incomplete or contradictory case records](#ch-20)
21. [Integrate response with service management](#ch-21)
22. [Automate repeatable evidence and notification tasks](#ch-22)
23. [Evaluate response latency and decision quality](#ch-23)
24. [Applied methods: compare two incident playbooks](#ch-24)
25. [Team studio: build and critique a response workflow](#ch-25)
26. [Operational handoff and communications practice](#ch-26)
27. [Deploy and validate an incident case workflow](#ch-27)
28. [Field simulation with authorized stakeholders](#ch-28)
29. [Capstone: integrated response and recovery service](#ch-29)
30. [Capstone evaluation and improvement dossier](#ch-30)

The [worked results](#worked-results) contain EX001–EX090. A [glossary](#glossary) and [references](#references) close the book.

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes and connection

You will be able to (1) describe a business service as a set of compute, storage, network and identity components with named owners; (2) identify failure domains that would delay detection, response or recovery; and (3) record the component facts an incident responder needs before the first incident arrives. This is the opening chapter of a three-year technologist course: you will build and run a working incident response service for one fictional organization, **Fernmoor City Services** (synthetic), a municipal provider of appointments, permits and water billing for about 180,000 residents. Every later chapter uses the component map you begin here.

### 1.1 Why a responder starts with the system, not the attack

An incident is handled on real machines. A responder who does not know where an application runs, where its data lives, who may change it and what it depends on will lose the first hours of any case asking those questions. NIST SP 800-61 Rev. 3 places incident response inside cybersecurity risk management under the CSF 2.0 functions; its preparation activities assume the organization already knows its assets and their criticality. The technologist's job is to make that assumption true.

### 1.2 Components of a service

A **service** is what a customer experiences ("book an appointment"). It is delivered by **components**: compute (virtual machines, containers, serverless functions), storage (databases, file shares, object stores, backups), network paths (load balancers, firewalls, DNS), identity (directory, single sign-on, service accounts) and external suppliers. For each component record: name, role, environment (production, test), location, owner team, change authority, data held, logs produced, and how it is restored.

### 1.3 Failure domains and change ownership

A **failure domain** is the set of components that fail together because they share something: a host, a power feed, a cloud region, an administrator credential, a deployment pipeline. Response planning cares about two kinds: domains that an attacker can cross with one foothold (shared admin accounts), and domains that a containment action would take down together (isolating a hypervisor stops every guest). **Change ownership** says who may alter a component. During an incident you need that person reachable, or a pre-agreed emergency authority.

### 1.4 Worked example (synthetic): the appointment service

*Fictional.* Fernmoor's appointment service runs on three application hosts (`appt-app-1..3`) behind one load balancer, with one PostgreSQL primary (`appt-db-1`) and a read replica, nightly backups to an object store, and sign-in through the city's identity provider. All three application hosts are patched by one automation account, `svc-patch`, and log only to local disk with seven-day rotation.

Map findings: (a) `svc-patch` is a failure domain — a stolen credential reaches every host; (b) local-only logs mean evidence disappears after seven days and may be altered by an intruder on the host; (c) the database has an owner (Data Platform team) but the load balancer has none listed — nobody can approve blocking traffic at 02:00; (d) the restore of `appt-db-1` has never been timed.

Response-relevant actions, each with an owner: forward application logs to central collection (Platform, 30 days); split `svc-patch` into per-environment accounts with restricted scope (Identity); name a load-balancer owner and an out-of-hours deputy (Network); schedule a timed restore test (Data Platform, see Chapter 18).

### 1.5 Practice activity

Pick one service you can legitimately describe (a home lab or the synthetic service above). Produce a one-page component table and mark each component's failure domain and restore method.

### 1.6 Common errors and limits

- Mapping servers but not identities and pipelines, which are the most common shared failure domains.
- Listing a team as owner without a reachable person or rota.
- Treating the map as finished; it decays with every change unless tied to change management (Chapter 21).
- Recording "backed up" without a tested restore time.

### Exercises — chapter 1

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX001 — Component table.** *Inputs:* §1.4. *Steps:* write a table with component, role, owner, logs, restore method for the appointment service. *Rubric:* 3 = all eight components (three app hosts, LB, primary, replica, backup store, IdP) with gaps marked; 2 = most components; 1 = hosts only; 0 = none.

**EX002 — Failure domains.** *Steps:* name three failure domains in the appointment service and say whether each matters for intrusion spread, containment impact or recovery. *Rubric:* 3 = three domains each correctly classified with reason; 2 = two; 1 = one or unclassified; 0 = none.

**EX003 — Owner gap.** *Steps:* write the request you would send to obtain a load-balancer owner and deputy. *Rubric:* 3 = states why (incident authority at any hour), what is needed (named owner, deputy, contact route, emergency change authority) and a deadline; 2 = missing authority or deadline; 1 = vague; 0 = none.

### Chapter synthesis

A response service protects systems it understands. Map each service as components with owners, logs and restore methods; mark shared failure domains; and treat every unknown owner or untested restore as a preparation task with an owner of its own.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes and connection

You will be able to (1) trace how a resident's request reaches a Fernmoor service through DNS, load balancers, firewalls and TLS; (2) identify which network records exist at each hop and how long they are kept; and (3) choose network containment points and predict their side effects. Chapter 1 mapped components; this chapter connects them and asks where evidence and control live on the path.

### 2.1 The request path

A typical request: the browser resolves `appointments.fernmoor.example` through DNS (RFC 1035), opens a TLS 1.3 connection (RFC 8446) to a content-delivery or load-balancing edge, which forwards to an application host inside a segmented network, which queries the database on another segment. Each hop can log: DNS query logs, edge access logs (client address, URL, status, bytes), firewall connection logs, application logs, database logs. Each hop is also a possible control point.

### 2.2 What network evidence can and cannot tell you

Network logs show who connected to what, when and how much data moved. They usually do not show content, because TLS encrypts it; decryption at an edge is a design choice with privacy implications. Source addresses may be shared (carrier NAT, proxies, cloud egress) or spoofed for connectionless traffic. A **flow record** summarizes a connection (addresses, ports, bytes, duration). NIST SP 800-92 discusses log management, including the need to plan retention and protect integrity.

### 2.3 Time and addressing

Correlating hops needs synchronized clocks; NTP (RFC 5905) keeps hosts aligned, and timestamps written in RFC 3339 form with an explicit offset remove ambiguity. Documentation in this book uses the address ranges reserved by RFC 5737 (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) and the `example` domain so that no real system is implied.

### 2.4 Containment points and side effects

Options include blocking an address at the edge, blocking a URL path, disabling a DNS record, isolating a host's network segment, or cutting an egress route. Each has a **blast radius**: blocking a shared egress address may block an entire mobile carrier's customers; removing a DNS record stops every user. A technologist pre-builds the common containment actions, records their side effects and their rollback, and tests them in a non-production environment.

### 2.5 Worked example (synthetic): enumeration of permit records

*Fictional.* Fernmoor's permit portal shows edge access logs with 41,000 requests in one hour to `/api/permits/{id}` from 203.0.113.0/24, with ids increasing sequentially and 98% `200 OK`. Firewall logs confirm only the edge talks to the app tier. Application logs show no authentication on that endpoint for "public" permits, but the responses include applicant phone numbers.

Analysis: the network evidence shows *volume, sequence and source*; it cannot show whether the requester was a researcher, a competitor or a criminal. Containment options: (a) rate-limit the path at the edge — low side effect, reversible in seconds; (b) block 203.0.113.0/24 — fast but bypassable and could block a legitimate shared egress; (c) disable the endpoint — stops the exposure entirely but breaks the public permit lookup. The duty lead chose (a) immediately and (c) after the service owner agreed, while application owners removed phone numbers from the response. Edge logs were exported before rotation for the case (Chapter 17).

### 2.6 Common errors and limits

- Treating an IP address as an identity.
- Blocking at the narrowest point you can reach rather than the point with the best side-effect profile.
- Forgetting that edge logs often rotate in hours; export first.
- Relying on log times without knowing the clock source.

### Exercises — chapter 2

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX004 — Hop table.** *Steps:* for the permit portal path, list each hop, the log it produces, a typical retention to verify, and one control action. *Rubric:* 3 = DNS, edge, firewall, app, DB each with log, retention-to-verify and control; 2 = four hops; 1 = two; 0 = none.

**EX005 — Side effects.** *Steps:* for options (a)–(c) in §2.5, state side effect, rollback and time to apply. *Rubric:* 3 = all three with plausible side effects and rollback; 2 = two; 1 = one; 0 = none.

**EX006 — Limits of evidence.** *Steps:* write three sentences for the case record stating what the network logs establish and what they do not. *Rubric:* 3 = facts (volume, pattern, source range, status codes) vs unknowns (identity, intent, content beyond logged fields), no attribution; 2 = mixes one inference; 1 = attributes intent; 0 = none.

### Chapter synthesis

Know the request path hop by hop: what each hop logs, how long it keeps it, and what control it offers. Choose containment by side-effect profile and reversibility, export volatile logs first, and keep network facts separate from conclusions about identity or intent.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 30

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes and connection

You will be able to (1) write small, readable Python programs that parse, filter and summarize incident data; (2) make scripts safe for evidence (read-only, deterministic, logged); and (3) test a script against a known input before trusting its output. Chapters 1–2 described systems and paths; from here on you will automate the repetitive parts of the response service, and every automation starts as a small script.

### 3.1 Why a responder programs

Response work repeats: normalizing timestamps, extracting accounts from logs, counting events per source, building evidence manifests. Doing it by hand is slow and error-prone under pressure. A technologist writes scripts that a colleague can read, rerun and check. This book's labs use only the Python 3 standard library so they run offline on any workstation without installing packages — a deliberate choice for an evidence workstation.

### 3.2 Core constructs you will use

Variables and types (strings, integers, lists, dictionaries); loops and comprehensions; functions with clear inputs and outputs; reading files line by line; the `csv`, `json`, `datetime`, `hashlib`, `collections` and `statistics` modules. Prefer explicit names (`signin_events`) over clever one-liners.

### 3.3 Evidence-safe scripting

Rules: open evidence files read-only and write results to a separate folder; never modify originals; make output deterministic (sort before printing); record the script version (hash or commit) and the input file hashes in the case notes; fail loudly on malformed lines rather than silently skipping them, or count and report what was skipped. NIST SP 800-86 emphasizes preserving the integrity of data during examination; a script is part of the examination method.

### 3.4 Testing before trusting

Before running a parser over a real export, run it over a tiny input you can verify by eye, including edge cases: an empty field, a timestamp without a zone, a duplicated line. Compare the output with what you expect. If they differ, fix the script or your expectation, then record why.

### 3.5 Worked example (synthetic): counting failed sign-ins

*Fictional.* Fernmoor's identity provider exports sign-in events as CSV with columns `time,user,result,src`. The duty lead asks: which accounts had more than five failures in the export, and from how many sources? A minimal, evidence-safe approach:

```text
read rows with csv.DictReader (file opened read-only)
for each row: if result == "failure": count[user] += 1; sources[user].add(src)
report users with count > 5, sorted by count descending, with len(sources)
report number of rows skipped for missing fields
```

Tested first on a ten-line file containing one row with an empty `user`, the script reported "skipped 1", which is correct. Run on the real export, it listed `water-billing-2` with 37 failures from 29 sources — a pattern consistent with password spraying that the analyst then examined alongside successful sign-ins (Chapter 16). The script and input hashes were attached to the case.

### 3.6 Common errors and limits

- Silently dropping malformed lines, which hides exactly the anomalies you need.
- Mixing time zones when comparing timestamps.
- Editing evidence in a spreadsheet that reformats dates and strips leading zeros.
- Treating a script's output as fact without a test on known input.

### Exercises — chapter 3

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX007 — Pseudocode to Python.** *Steps:* turn the §3.5 pseudocode into a standard-library Python script. *Rubric:* 3 = uses csv, Counter/dict and set, sorts output, reports skipped rows, opens input read-only; 2 = works but no skipped count or not sorted; 1 = partial; 0 = none.

**EX008 — Test input.** *Steps:* design a ten-line test file and the exact expected output. *Rubric:* 3 = includes a user above and at the threshold, an empty field, duplicate sources, and states expected output; 2 = missing edge cases; 1 = no expected output; 0 = none.

**EX009 — Evidence note.** *Steps:* write the case-note entry recording how the script was used. *Rubric:* 3 = script identifier/hash, input file and hash, time, operator, result summary, skipped rows; 2 = missing hashes; 1 = result only; 0 = none.

### Chapter synthesis

Write small, readable, standard-library scripts; keep evidence read-only and outputs deterministic; test on known input first; and record script and input hashes so another responder can reproduce your result.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 30

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes and connection

You will be able to (1) design a case record and an event record with typed, required fields; (2) normalize events from different sources into a common schema; and (3) explain how a poor data model produces wrong answers in an investigation. Chapter 3 gave you scripts; scripts need consistent data. The case model you design here is implemented in a tool in Chapter 17 and deployed in Chapter 27.

### 4.1 Entities and relationships

An incident service handles a few core entities: **case** (one managed incident or suspected incident), **event** (a timestamped observation from a source), **artefact** (a preserved item with a hash), **action** (something done, by whom, when, with what approval), **decision** (a choice with its owner and rationale) and **asset/identity** (what was affected). Relationships: a case has many events, artefacts, actions and decisions; an event references assets and identities.

### 4.2 Fields, types and required values

Each field needs a type and a rule. Times: RFC 3339 with offset, stored in UTC. Identifiers: stable keys, not display names (an account id survives a name change). Enumerations: fixed lists for status, severity and source, so that counts mean something. Required fields: what must be known before a record is valid (a case needs an owner and a severity; an action needs an actor and a time). Free text is valuable but should not replace structured fields that you will need to count.

### 4.3 Normalization

Sources name things differently: `user`, `UserPrincipalName`, `actor.id`. A **mapping** translates each source's fields into your schema and records the original value. Keep the raw event too: normalization can be wrong, and evidence must remain reviewable. Data-model ideas used by security tools (for example common event schemas published by vendors and open projects) are useful references, but the essential discipline is the same: one meaning per field.

### 4.4 Worked example (synthetic): severity counts that lied

*Fictional.* Fernmoor's first incident spreadsheet had a free-text "Severity" column. Values included "High", "high", "HIGH - maybe", "P1", "sev2?" and blanks. A monthly report counted only exact "High", showing 3 high incidents; a reviewer re-coding by hand found 11. The fix was an enumeration (`S1`–`S4` with definitions from Chapter 13), a required field at triage, and a separate `severity_note` free-text field for nuance. Historic rows were re-coded by two people independently; disagreements (2 of 64) were resolved and recorded.

A normalized event record adopted at the same time:

```text
event_id      string   required  source-unique id or generated hash
case_id       string   optional  link once triaged
time_utc      RFC3339  required  converted, original kept in raw
source        enum     required  idp | edge | fw | endpoint | app | cloud
actor_id      string   optional  stable account id
asset_id      string   optional  from the inventory (Chapter 11)
action        string   required  normalized verb, e.g. signin, file_read
outcome       enum     required  success | failure | unknown
raw           text     required  original line or JSON
```

### 4.5 Common errors and limits

- Free-text fields for anything you will later count.
- Display names as keys.
- Dropping the raw record after normalization.
- Converting times without recording the original zone or the correction applied.

### Exercises — chapter 4

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX010 — Case schema.** *Steps:* define ten fields for a case record with type and required/optional. *Rubric:* 3 = includes id, title, status enum, severity enum, owner, opened/updated times UTC, affected services, links to events/actions, closure reason; 2 = seven sensible fields; 1 = unstructured; 0 = none.

**EX011 — Mapping.** *Steps:* map an IdP field set (`createdDateTime`, `userId`, `ipAddress`, `status.errorCode`) into the §4.4 event schema. *Rubric:* 3 = correct mapping, outcome derived from error code, raw kept, time conversion noted; 2 = one error; 1 = partial; 0 = none.

**EX012 — Recode check.** *Steps:* explain why two independent coders were used for historic severity and how to report agreement. *Rubric:* 3 = reduces individual bias, measure agreement (for example percent agreement 62/64), resolve and record disagreements; 2 = no measure; 1 = vague; 0 = none.

### Chapter synthesis

Define entities and fields with types, enumerations and required values; normalize sources into one meaning per field while keeping raw records; and never count free text. A clean case model is the foundation of every later measurement.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 30

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes and connection

You will be able to (1) use the vocabulary of event, alert, incident, vulnerability, threat and risk precisely; (2) relate common attack techniques to the evidence and controls in your service; and (3) explain the response lifecycle in the current NIST framing. Chapters 1–4 gave you systems, networks, code and data; this chapter gives you the language the response service is built on.

### 5.1 Precise terms

An **event** is any observable occurrence. An **alert** is an event or pattern that a detection rule flagged for attention. An **incident** is an occurrence that actually or imminently jeopardizes confidentiality, integrity or availability, or violates policy. A **vulnerability** is a weakness; a **threat** is a circumstance or actor with potential to exploit it; **risk** combines likelihood and impact. Most alerts are not incidents, and many incidents begin as something other than an alert — a call from a resident, a supplier notice, a journalist's question.

### 5.2 The lifecycle in NIST SP 800-61 Rev. 3

Rev. 3 (April 2025) replaces the earlier four-phase lifecycle with a mapping onto the CSF 2.0 functions: Govern, Identify and Protect support preparation; Detect, Respond and Recover cover the incident itself; improvement feeds back into all functions. For a technologist this means the response service is not a separate island: inventory (Identify), access control (Protect), monitoring (Detect) and recovery planning (Recover) are all parts of it.

### 5.3 Techniques and their evidence

MITRE ATT&CK catalogues adversary tactics and techniques observed in real intrusions. You do not need to memorize it; you need to connect a technique to where its traces would appear in *your* systems. For example: valid-account use appears in identity logs; persistence through new authentication methods appears in identity audit logs; data collection appears in file-server or database audit logs; exfiltration appears in edge or egress flow logs.

### 5.4 Worked example (synthetic): from alert to incident

*Fictional.* At 08:40 an alert fires: "impossible travel" for `water-billing-2` — a sign-in from Fernmoor and, eleven minutes later, from a foreign hosting provider. The duty analyst checks: the second sign-in failed MFA; no session was created; the account owner confirms she was at work. Classification: alert true-positive for suspicious activity, **not** an incident yet (no jeopardy realized), but it joins the password-spraying pattern found in Chapter 3. The analyst opens a case at low severity because the password is evidently known to someone else, resets it, and records the decision. Had MFA been approved, the same alert would have been an incident: valid credentials used by an unauthorized party.

### 5.5 Defence in depth, briefly

No single control is reliable. The example shows layers: a detection rule raised an alert; MFA blocked the session; a human verified with the owner; a script found the broader pattern. Your service should know which layer caught each case — that information drives improvement (Chapter 19).

### 5.6 Common errors and limits

- Calling every alert an incident, which floods the case system, or calling nothing an incident until damage is proven, which delays response.
- Using ATT&CK labels as conclusions rather than hypotheses to test.
- Treating the lifecycle as strictly sequential; containment and investigation overlap.

### Exercises — chapter 5

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX013 — Classify.** *Steps:* classify five synthetic occurrences as event, alert, incident or not security-relevant, with reason: a failed sign-in; a firewall deny; a resident reporting a phishing SMS using Fernmoor's name; ransomware note on a file server; a detection rule on a known admin script. *Rubric:* 3 = all five defensible with reasons; 2 = four; 1 = two; 0 = none.

**EX014 — Technique to evidence.** *Steps:* for three techniques (valid accounts, adding an MFA method, bulk file reads), name the Fernmoor log where traces would appear and one control. *Rubric:* 3 = correct source and control for each; 2 = two; 1 = one; 0 = none.

**EX015 — CSF mapping.** *Steps:* map five response-service activities to CSF 2.0 functions. *Rubric:* 3 = five correct (e.g., inventory–Identify, MFA–Protect, alerting–Detect, containment–Respond, restore test–Recover); 2 = four; 1 = two; 0 = none.

### Chapter synthesis

Use event, alert and incident precisely; place response inside the CSF 2.0 functions as Rev. 3 does; connect each technique to the evidence it leaves in your own systems; and record which layer caught each case so the service can improve.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 30

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes and connection

You will be able to (1) locate the operating-system records a responder needs on Linux and Windows hosts; (2) choose a collection order that respects volatility; and (3) use virtualization features (snapshots, isolation) for response without destroying evidence. Chapter 5 connected techniques to evidence; this chapter goes inside the host.

### 6.1 What the operating system records

Linux: authentication logs (location varies by distribution), the systemd journal, shell histories (unreliable — users and attackers can disable them), cron and systemd unit files (persistence), package logs. Windows: Security, System and Application event logs, PowerShell operational logs when enabled, scheduled tasks and services (persistence), registry run keys. Both: running processes, network connections, loaded modules and logged-in sessions — all volatile.

### 6.2 Order of volatility

NIST SP 800-86 advises collecting the most volatile data first when it matters: memory and running state, then network connections, then disk. A technologist decides *before* incidents which hosts justify memory capture (for example, servers handling personal data) and pre-installs or pre-approves the collection tools, so that collection is a runbook step rather than an improvisation.

### 6.3 Virtualization for response

Hypervisors and clouds offer powerful response features. A **snapshot** preserves disk (and sometimes memory) state quickly; it lives inside the same platform, so it must be exported and hashed to become independent evidence. **Network isolation** of a virtual machine (moving it to a quarantine segment) stops lateral movement while keeping it running for collection. Beware: reverting a snapshot destroys evidence of what happened after it; deleting and rebuilding a VM before collection loses the case.

### 6.4 Worked example (synthetic): a suspicious process on `permit-app-2`

*Fictional.* The endpoint agent flags `/tmp/.x/kworkerd` running as the web service user on `permit-app-2`, a VM. The runbook "Linux server suspected compromise" is followed:

1. Open a case, record time and who approved collection (service owner on call).
2. Take a memory capture with the pre-approved tool to the evidence share; hash it.
3. Record process list, network connections and open files; hash outputs.
4. Request a hypervisor snapshot with memory; export it to the evidence store; hash it.
5. Move the VM to the quarantine network (only the evidence share reachable).
6. Do not reboot or rebuild until the investigation lead releases the host.

Findings later showed an outbound connection to 203.0.113.77 on port 443 and a cron entry re-launching the binary. Because the VM was isolated rather than rebuilt, the team could confirm the cron persistence and check the other two app hosts for the same entry — one had it.

### 6.5 Common errors and limits

- Rebooting "to be safe", losing memory and connections.
- Treating an internal snapshot as preserved evidence without export and hash.
- Running investigation tools from the compromised host's own binaries, which may be altered.
- Collecting everything from every host, overwhelming storage and analysts; scope by hypothesis.

### Exercises — chapter 6

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX016 — Persistence checklist.** *Steps:* list five persistence locations to check on Linux and five on Windows. *Rubric:* 3 = ten correct locations; 2 = seven; 1 = four; 0 = none.

**EX017 — Order of collection.** *Steps:* put these in collection order and justify: disk image, process list, memory, firewall rules, network connections. *Rubric:* 3 = memory, processes/connections, firewall config, disk with volatility reasoning; 2 = one swap; 1 = random; 0 = none.

**EX018 — Snapshot risk.** *Steps:* explain two ways snapshots can harm an investigation and how to prevent each. *Rubric:* 3 = revert destroys later evidence; snapshot inside compromised platform not independent — export, hash, restrict reverts; 2 = one; 1 = vague; 0 = none.

### Chapter synthesis

Know where each operating system records activity and persistence; collect by volatility using pre-approved tools; use isolation and exported, hashed snapshots instead of reboots and rebuilds; and scope collection by hypothesis.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 30

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes and connection

You will be able to (1) explain authentication, authorization, sessions and tokens as a responder needs them; (2) list identity actions that contain an account compromise and the order in which to perform them; and (3) identify the identity logs that must be retained. Identity appeared in every earlier example; most of Fernmoor's real cases will be identity cases.

### 7.1 Authentication, authorization and sessions

**Authentication** proves who is acting (password, authenticator, certificate). **Authorization** decides what they may do (roles, groups, policies). After sign-in, a **session** or **token** represents the authenticated identity; refresh tokens can extend access for days without a new password. NIST SP 800-63B describes authenticator types and their assurance; phishing-resistant authenticators (such as FIDO2 security keys) resist the credential-relay attacks that defeat one-time codes and push approvals.

### 7.2 Types of identity

Human accounts, privileged administrator accounts, service accounts (used by software), and external identities (suppliers, residents). Service accounts are frequently over-privileged, never rotated and unmonitored — Chapter 1's `svc-patch` is typical.

### 7.3 Containing an account compromise

Order matters. If you reset the password first but leave sessions and authentication methods, an attacker with a valid refresh token or a newly registered MFA device keeps access. A typical sequence: (1) preserve identity logs for the account; (2) revoke sessions and refresh tokens; (3) remove attacker-added authentication methods and application consents; (4) reset the credential; (5) check for mailbox rules, forwarding and API keys created by the account; (6) monitor for re-entry. For privileged accounts, also review what they changed.

### 7.4 Logs to retain

Sign-in logs (interactive and non-interactive), audit logs (role changes, method changes, consents), and application access logs. Default retention in many identity platforms is short; extend it or export centrally. CISA's federal playbooks list identity and credential review among standard response steps.

### 7.5 Worked example (synthetic): an MFA method added at night

*Fictional.* At 02:14 Fernmoor's IdP audit log records a new authenticator app registered for `permits-clerk-4`, from 198.51.100.23, after an approved push at 02:12. The clerk was asleep and says she tapped "approve" on a notification to stop it buzzing. The duty analyst follows the identity runbook: exports 30 days of sign-in and audit logs (hashed), revokes sessions, deletes the new authenticator, resets the password with identity verification by her manager, and searches for mailbox rules — finding a rule forwarding messages containing "invoice" to an external address, which is removed and preserved as evidence. A follow-up change, owned by the Identity team, enables number-matching for push approvals and schedules security keys for permit staff.

### 7.6 Common errors and limits

- Password reset alone, leaving sessions and methods intact.
- Forgetting non-interactive sign-ins and service principals.
- Destroying the attacker's artefacts (mailbox rule) without preserving them first.
- Blaming the user for an approval-fatigue design weakness.

### Exercises — chapter 7

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX019 — Sequence.** *Steps:* order these and justify: reset password; revoke sessions; export logs; remove new MFA method; check forwarding rules. *Rubric:* 3 = export, revoke, remove method, reset, check rules (or rules before reset with reason) with justification; 2 = one misplacement; 1 = reset first; 0 = none.

**EX020 — Service account review.** *Steps:* list four questions to ask about `svc-patch` after a compromise. *Rubric:* 3 = where used, privileges vs need, last rotation and credential storage, sign-in sources and anomalies; 2 = three; 1 = one; 0 = none.

**EX021 — User communication.** *Steps:* write a 60-word message to the clerk explaining what happened and what to do next without blame. *Rubric:* 3 = factual, no blame, clear next steps (report unexpected prompts, new sign-in method), contact; 2 = slightly blaming or vague; 1 = technical jargon; 0 = none.

### Chapter synthesis

Identity is the commonest incident surface. Understand sessions and tokens, contain compromises in an order that removes all access paths, preserve before you change, retain identity logs long enough, and fix design weaknesses rather than blaming users.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 30

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes and connection

You will be able to (1) read an architecture diagram for trust boundaries, segmentation and control points; (2) evaluate whether the architecture supports detection, containment and recovery; and (3) propose small architectural changes that make response faster. Chapters 1–7 described parts; this chapter looks at how they are arranged.

### 8.1 Trust boundaries and segmentation

A **trust boundary** is where data or control passes between zones with different trust: internet to edge, edge to application, application to database, corporate network to production, supplier to Fernmoor. **Segmentation** limits which zones can talk to which. Good segmentation turns a compromise of one zone into a contained case; flat networks turn it into a city-wide outage. NIST SP 800-207 describes zero trust architecture, which moves from network location to per-request verification of identity and device; few organizations are there yet, but its principles guide incremental change.

### 8.2 Architecture for response

Ask four questions of any design. *Visibility:* do logs at each boundary reach central collection? *Containment:* can one zone, host or identity be isolated without stopping unrelated services? *Recovery:* are backups separated from production administration (different credentials, immutability)? *Administration:* is privileged access through controlled paths (jump hosts, privileged access management) rather than from any workstation? NIST SP 800-160 Vol. 2 frames these as cyber-resiliency techniques such as segmentation, redundancy and non-persistence.

### 8.3 Worked example (synthetic): the water-billing design review

*Fictional.* Fernmoor's water-billing system has a web front end, an application server, a database and a nightly file transfer to a payment supplier. Review findings:

| Question | Finding | Response impact | Proposed change | Owner |
|---|---|---|---|---|
| Visibility | DB audit off; SFTP logs local | cannot tell what data left | enable DB audit for export queries; forward SFTP logs | Data Platform |
| Containment | front end and app on one VLAN with HR systems | isolating billing cuts HR | separate billing VLAN with explicit rules | Network |
| Recovery | backups written by the same domain admin used daily | ransomware could delete backups | dedicated backup credential and immutable copy | Infrastructure |
| Administration | admins RDP from laptops | stolen laptop session reaches DB | jump host with MFA and session logging | Identity |

Each change was entered in the service-management system (Chapter 21) with the response rationale, so that the change board saw why it mattered.

### 8.4 Small changes, large effect

Technologists rarely redesign a system; they make it respondable. Typical high-value changes: forward one missing log source; create a quarantine segment and test moving a VM into it; give backups their own credentials; put administration behind a jump host. Each change should have an acceptance test ("from the quarantine segment, only the evidence share is reachable").

### 8.5 Common errors and limits

- Drawing segments that exist on paper but not in firewall rules — verify with a connectivity test.
- Assuming cloud resources are segmented by default.
- Security changes without a rollback or owner.
- Ignoring supplier connections as trust boundaries.

### Exercises — chapter 8

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX022 — Boundary list.** *Steps:* list five trust boundaries in the water-billing system. *Rubric:* 3 = internet–web, web–app, app–DB, admin–servers, Fernmoor–payment supplier; 2 = four; 1 = two; 0 = none.

**EX023 — Acceptance test.** *Steps:* write acceptance tests for the four proposed changes in §8.3. *Rubric:* 3 = each test observable and pass/fail; 2 = three; 1 = vague; 0 = none.

**EX024 — Prioritize.** *Steps:* rank the four changes and justify by response impact and effort. *Rubric:* 3 = defensible ranking with both impact and effort (backup separation commonly first); 2 = impact only; 1 = no reasons; 0 = none.

### Chapter synthesis

Read architecture for trust boundaries and ask four response questions: visibility, containment, recovery and administration. Propose small, testable changes with owners and acceptance tests that make each system respondable.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 30

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes and connection

You will be able to (1) distinguish evidence preserved for a case from data measured about the service; (2) define a small set of response-service measures with exact definitions; and (3) compute and interpret latency measures honestly, including missing data. This closes the first-year foundations. From Chapter 10 onward you will build the service, and you will measure it with the definitions set here.

### 9.1 Two kinds of evidence

**Case evidence** answers "what happened in this incident?" — logs, images, artefacts, preserved with hashes and custody (Chapter 17). **Service evidence** answers "how well does our response service work?" — times, counts, completeness of records, outcomes of exercises. The first serves investigation and possibly legal processes; the second serves management and improvement. Both need provenance.

### 9.2 Defining a measure

A useful measure has: a name; a precise start and end event (for example, "time to triage = triage-start time minus alert time, both from case-system fields"); a population (which cases); handling of missing values; a reporting statistic (median and a high percentile rather than mean, because response times are skewed); a target with rationale; and an owner. Without exact definitions, two teams will report different numbers for the "same" metric.

### 9.3 Honest reporting

Report how many cases were measured and how many were missing. Separate out-of-hours from in-hours if the service model differs. Small numbers vary a lot; seven cases do not establish a trend. Avoid incentives that improve the number but not the service — for example, clicking "triage start" before actually looking.

### 9.4 Lab T-09 (synthetic): triage latency

The script below computes time to triage for eight synthetic Fernmoor cases, using RFC 3339 timestamps. Predict the median before running it.

```python
# Lab T-09: triage latency from synthetic Fernmoor case records (stdlib only)
from datetime import datetime
from statistics import median
cases = [  # case id, alert time, triage start (UTC, RFC 3339)
 ("FCS-101","2026-03-02T08:00:00Z","2026-03-02T08:12:00Z"),
 ("FCS-102","2026-03-02T09:30:00Z","2026-03-02T09:36:00Z"),
 ("FCS-103","2026-03-02T22:10:00Z","2026-03-03T00:05:00Z"),
 ("FCS-104","2026-03-03T07:45:00Z","2026-03-03T07:59:00Z"),
 ("FCS-105","2026-03-03T13:20:00Z",None),
 ("FCS-106","2026-03-04T02:00:00Z","2026-03-04T03:10:00Z"),
 ("FCS-107","2026-03-04T10:00:00Z","2026-03-04T10:09:00Z"),
 ("FCS-108","2026-03-04T11:00:00Z","2026-03-04T11:21:00Z"),
]
p = lambda s: datetime.fromisoformat(s.replace("Z","+00:00"))
mins = {c:(p(t)-p(a)).total_seconds()/60 for c,a,t in cases if t}
missing = [c for c,a,t in cases if not t]
v = sorted(mins.values())
print("measured", len(v), "of", len(cases), "missing", missing)
print("median minutes", median(v))
k = max(1, round(0.9*len(v)))  # nearest-rank p90
print("p90 minutes (nearest rank)", v[k-1])
print("within 15 min target", sum(x<=15 for x in v), "of", len(v))
off = [c for c,a,t in cases if t and not 7 <= p(a).hour < 19]
print("out-of-hours alerts", off, "minutes", [mins[c] for c in off])
```

Expected output:

```text
measured 7 of 8 missing ['FCS-105']
median minutes 14.0
p90 minutes (nearest rank) 70.0
within 15 min target 4 of 7
out-of-hours alerts ['FCS-103', 'FCS-106'] minutes [115.0, 70.0]
```

Interpretation: the median (14 minutes) meets a 15-minute target, but only 4 of 7 measured cases did, the nearest-rank 90th percentile is 70 minutes, and both slow cases were out of hours. One case had no triage time at all — itself a finding about record completeness. The honest summary: "In-hours triage is usually within target; out-of-hours triage is not; one record is incomplete; numbers are too few for a trend." That points to a specific improvement (on-call paging, Chapter 21) rather than a general exhortation.

### 9.5 Common errors and limits

- Reporting means of skewed times.
- Hiding missing records instead of counting them.
- Changing a definition mid-year without restating earlier figures.
- Using service measures to blame individuals, which corrupts the data.

### Exercises — chapter 9

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX025 — Definition card.** *Steps:* write a definition card for "time to contain". *Rubric:* 3 = start/end events and fields, population, missing-value rule, statistics, target and owner; 2 = missing two elements; 1 = name only; 0 = none.

**EX026 — Re-run with a change.** *Steps:* in the lab, give FCS-105 a triage start of 13:31 and recompute median, p90 and within-target count. *Rubric:* 3 = 8 measured, median 13.0, p90 70.0, 5 of 8 within 15; 2 = one value wrong; 1 = attempted; 0 = none.

**EX027 — Summary for the manager.** *Steps:* write a four-sentence summary of the original lab output. *Rubric:* 3 = median and percentile, within-target count, out-of-hours finding, missing record, caution on small n; 2 = omits one; 1 = mean or single number; 0 = none.

### Chapter synthesis

Keep case evidence and service evidence distinct; define each measure exactly; report medians, percentiles, counts and missing values; separate structural conditions such as out-of-hours; and turn the result into a specific, testable improvement.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — chapter 09 of 30

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Incident response service model and operating roles

### Learning outcomes and connection

You will be able to (1) define Fernmoor's incident response service with its customers, scope, authority and service levels; (2) assign operating roles with clear handoffs; and (3) write the service charter that later chapters implement. This is the turning point of the course: from now on you are building and running a service, not studying components.

### 10.1 Response as a service

The FIRST CSIRT Services Framework describes services a response team may offer: information security event management, incident management, vulnerability management, situational awareness and knowledge transfer. A technologist chooses which services Fernmoor will provide now, documents them in a **service catalog** entry and defines how customers request them. ISO/IEC 27035 similarly describes planning and preparing an incident management capability before incidents occur.

### 10.2 Charter elements

Mission and scope (which systems, which organizations — does the service cover the water utility's operational technology? Fernmoor decided: not yet, refer to the OT team); customers (city departments, residents via the contact centre); authority (what the service may do without asking — for example isolate a workstation — and what needs the system owner or executive approval); hours (business hours with on-call out of hours); service levels (time to acknowledge, time to triage by severity); interfaces (service desk, IT operations, legal, privacy, communications, suppliers); and review cadence.

### 10.3 Roles

- **Duty analyst:** watches the queue, triages, opens cases, performs runbook steps.
- **Incident lead:** owns a case at severity S1–S2, coordinates, decides within authority, escalates.
- **Technical responders:** platform, identity, network, application staff who execute changes.
- **Communications and liaison:** internal updates, resident communication with the communications office, supplier contact.
- **Approver:** the system owner or on-call manager for actions beyond the duty analyst's authority.
- **Scribe:** keeps the case record current during major incidents.

One person may hold several roles in a small team, but a case always has exactly one named lead. The Google SRE book's chapter on managing incidents gives a practical model of separating the incident commander from the people doing hands-on work.

### 10.4 Worked example (synthetic): Fernmoor's first charter

*Fictional.* The Response Desk is three technologists plus an on-call rota shared with IT operations. Service levels: acknowledge S1 within 15 minutes at any hour, S2 within 30 minutes in hours and 60 out of hours; triage within 60 minutes of acknowledgment. Pre-approved actions for the duty analyst: disable a user account, revoke sessions, isolate a single workstation, block a single external address at the edge. Actions needing the system owner: isolate a server, disable a public service. Actions needing the director: notify regulators or residents (with counsel and the privacy officer). Review: monthly service report; charter review yearly or after any S1.

### 10.5 Common errors and limits

- A charter that grants no authority, so every action waits for a meeting.
- Service levels without the staffing to meet them.
- Roles named but not trained or rostered.
- Scope ambiguity discovered during a crisis (OT, suppliers, residents' data held by a contractor).

### Exercises — chapter 10

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX028 — Authority table.** *Steps:* build a table of eight response actions and who may authorize each at Fernmoor. *Rubric:* 3 = eight actions graded duty analyst/system owner/director with reasons; 2 = six; 1 = unstructured; 0 = none.

**EX029 — Role card.** *Steps:* write a one-paragraph role card for the incident lead. *Rubric:* 3 = responsibilities, authority limits, handoff duty, escalation triggers, what they must not do (hands-on work in S1); 2 = missing two; 1 = vague; 0 = none.

**EX030 — Scope decision.** *Steps:* argue whether the service should cover the water utility's OT systems in year one. *Rubric:* 3 = considers skills, tooling, safety, interface with OT team, phased approach with referral path; 2 = one-sided; 1 = assertion; 0 = none.

### Chapter synthesis

Define response as a service: scope, customers, authority, hours, service levels, interfaces and review. Assign roles with one named lead per case and pre-approved actions that let the service act quickly within limits.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — chapter 10 of 30

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Asset inventory and business-service dependencies

### Learning outcomes and connection

You will be able to (1) build an inventory that links technical assets to business services and owners; (2) model dependencies so that response and recovery can be prioritized; and (3) keep the inventory current through automated discovery and change records. Chapter 1 mapped one service; this chapter scales that map across Fernmoor and makes it a living data source for the case system.

### 11.1 Inventory as response data

CSF 2.0 places asset management under Identify. For response, the inventory must answer within minutes: what is this host or account, which service does it support, who owns it, how critical is it, where are its logs, and how is it restored? An inventory that answers only "what hardware do we own" is not enough.

### 11.2 Sources and reconciliation

Combine sources: cloud and hypervisor APIs, endpoint agent lists, identity directory, network scans of authorized ranges, the configuration management database (CMDB), and owners' attestations. Each source misses something. Reconcile by stable identifiers and flag disagreements: a host in the agent list but not the CMDB has no owner; a CMDB entry with no agent check-in may be dead or unmonitored.

### 11.3 Dependencies and criticality

A **business service** depends on technical services (database, identity, DNS) and suppliers. Model dependencies as edges: `appointments → appt-db-1`, `appointments → idp`, `water-billing → payment-supplier-sftp`. **Criticality** comes from the service's impact if unavailable or disclosed, set with the service owner (for example tiers 1–3 with recovery time objectives, following NIST SP 800-34 contingency-planning concepts). Shared dependencies such as identity and DNS inherit the highest criticality of anything depending on them.

### 11.4 Worked example (synthetic): which restore first?

*Fictional.* After a storage failure caused by a malicious deletion, five Fernmoor systems are down: `idp-proxy`, `appt-db-1`, `permit-app-1`, `billing-db`, `intranet-wiki`. Inventory data:

| System | Supports | Tier | Depends on |
|---|---|---|---|
| idp-proxy | sign-in for all staff apps | 1 (inherited) | — |
| billing-db | water billing | 1 | idp-proxy (admin) |
| appt-db-1 | appointments | 2 | idp-proxy |
| permit-app-1 | permits | 2 | idp-proxy, permits DB (up) |
| intranet-wiki | staff wiki (holds runbooks!) | 3 | idp-proxy |

Order: `idp-proxy` first (everything depends on it), then `billing-db`, then `appt-db-1` and `permit-app-1` in parallel. The wiki is tier 3, but it holds the runbooks; the team used the offline runbook copy, and recorded a finding: critical response documents must not depend on the systems they help restore.

### 11.5 Keeping it current

Automate discovery runs daily; create a work item for every unreconciled asset; require an inventory update as part of every change (Chapter 21); review tier assignments with owners yearly.

### 11.6 Common errors and limits

- Inventory without owners or services.
- Forgetting identities, certificates and suppliers as assets.
- Criticality set by IT alone without business owners.
- Response documentation hosted only on systems that may be down.

### Exercises — chapter 11

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX031 — Reconcile.** *Steps:* given four discrepancies (agent-only host, CMDB-only host, cloud VM with no tag, scan-found host in no source), say what each likely means and the action. *Rubric:* 3 = all four plausible with actions; 2 = three; 1 = one; 0 = none.

**EX032 — Dependency graph.** *Steps:* draw the dependency edges for the five systems in §11.4 plus DNS. *Rubric:* 3 = all edges including DNS for all, correct direction, inherited tier noted; 2 = missing DNS; 1 = partial; 0 = none.

**EX033 — Inventory query.** *Steps:* list the six inventory fields a duty analyst needs when an alert names a hostname. *Rubric:* 3 = service, owner/on-call, tier, environment, log locations, restore method; 2 = four; 1 = two; 0 = none.

### Chapter synthesis

Make the inventory a response tool: link assets to services, owners, tiers, logs and restore methods; reconcile sources continuously; model dependencies so shared services inherit criticality; and never let response documents depend on what they restore.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — chapter 11 of 30

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Evidence flows across identity, endpoint and cloud

### Learning outcomes and connection

You will be able to (1) design the collection path for identity, endpoint and cloud evidence into a central store; (2) set retention and integrity controls on each flow; and (3) verify that a flow actually delivers what an investigation will need. Chapter 11 told you what exists; this chapter makes sure its evidence arrives somewhere safe before an incident.

### 12.1 Why flows, not just logs

A log that exists only on the source system is fragile: it rotates, it can be altered by an intruder, and it is unavailable if the system is down. An **evidence flow** moves records from source to a central store with known latency, retention, access control and integrity protection. NIST SP 800-92 recommends centralized log management with protected storage and planned retention.

### 12.2 Three flow families

**Identity:** sign-in and audit logs via the provider's export or API to the central store; include non-interactive sign-ins and administrative actions. **Endpoint:** agent telemetry (processes, network, file events) and operating-system logs; plus on-demand collection capability for memory and files. **Cloud:** control-plane audit logs (who changed what), data-plane logs where enabled (object reads, database queries) and network flow logs. For each flow record the fields received, the delay, the cost and the retention.

### 12.3 Integrity and access

Write central logs to storage the source administrators cannot alter (separate account or tenant, write-once or object-lock features where available). Restrict read access to the response and audit functions and log access to the logs. Hash exported evidence sets (FIPS 180-4 SHA-256) when they leave the store for a case.

### 12.4 Verifying a flow

A flow is verified when a known test event appears in the central store with correct fields and timestamp within the expected delay. Do this at onboarding and periodically ("canary" events), because flows silently break when credentials expire or formats change.

### 12.5 Worked example (synthetic): the missing data-read logs

*Fictional.* During a permit-data case, the team asked: did anyone download the `permits-archive` storage bucket? Control-plane logs showed a new access key created for `svc-reports` at 14:05; but object-read logging had never been enabled, so no record could show which objects were read. The case concluded "unable to determine", which forced a cautious privacy assessment. Afterwards the team built a flow matrix:

| Flow | Source | Fields checked | Delay | Retention | Immutability | Canary |
|---|---|---|---|---|---|---|
| IdP sign-ins | IdP API | user, app, src, result, MFA | 5 min | 400 days | object lock | weekly test sign-in |
| Endpoint | agent | process, parent, hash, user | 2 min | 90 days hot | vendor-managed | EICAR test file |
| Cloud control plane | audit log | principal, action, resource | 15 min | 400 days | separate account | tag change on test bucket |
| Cloud data reads | object access logs | principal, object, bytes | 60 min | 180 days | separate account | read of canary object |

The data-read flow was enabled for buckets holding personal data, with its storage cost approved by the data owner.

### 12.6 Common errors and limits

- Assuming default logging captures data access.
- Storing logs where an attacker with admin rights can delete them.
- Never testing flows after onboarding.
- Retention shorter than typical detection delay; intrusions are often found weeks later.

### Exercises — chapter 12

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX034 — Flow card.** *Steps:* complete a flow card for file-server audit logs. *Rubric:* 3 = source, fields, delay, retention with rationale, immutability, access, canary test; 2 = missing two; 1 = partial; 0 = none.

**EX035 — Canary design.** *Steps:* design canary tests for identity and cloud control-plane flows and an alert if they fail. *Rubric:* 3 = specific test events, schedule, expected appearance window, alert route and owner; 2 = no alert; 1 = vague; 0 = none.

**EX036 — Unable to determine.** *Steps:* write the case-record paragraph for §12.5 explaining what could and could not be established. *Rubric:* 3 = facts (key creation, time, principal), gap (no object-read logs), consequence for assessment, remediation; 2 = missing consequence; 1 = speculative; 0 = none.

### Chapter synthesis

Build evidence flows, not isolated logs: central, timely, retained long enough, protected from source administrators and verified by canaries. When a flow is missing, say "unable to determine" plainly and fix the flow.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — chapter 12 of 30

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — Incident risk scenarios and triage thresholds

### Learning outcomes and connection

You will be able to (1) write incident risk scenarios for Fernmoor's services; (2) define severity levels with observable criteria; and (3) set triage thresholds that decide when an alert becomes a case and when a case escalates. Chapters 10–12 built the service's charter, inventory and evidence; triage rules decide how that service spends its limited attention.

### 13.1 Scenarios

A **risk scenario** describes a plausible incident in concrete terms: actor or cause, entry, affected asset, impact and the evidence that would reveal it. Examples for Fernmoor: credential phishing of permit staff leading to resident-data access; ransomware on file servers halting billing; supplier compromise of the payment SFTP; public portal enumeration; insider misuse of the billing database. Scenarios come from the inventory (what matters), threat information (what happens to similar organizations, for example sector advisories) and past cases. NIST SP 800-61 Rev. 3 ties response preparation to the organization's risk assessment; scenarios are the operational form of that link.

### 13.2 Severity levels

Severity must be decided in minutes with incomplete information, so criteria must be observable. Fernmoor's scale:

- **S1 Critical:** tier-1 service unavailable or confirmed exfiltration of sensitive personal data, or active spread across systems.
- **S2 High:** confirmed compromise of an account or host with access to tier-1/2 data, contained to that asset so far.
- **S3 Medium:** suspicious activity requiring investigation, no confirmed compromise; or confirmed compromise of a low-impact asset.
- **S4 Low:** policy violation or blocked attack with no compromise.

Severity can go up or down as facts arrive; record each change with its reason.

### 13.3 Triage thresholds

Thresholds connect detections to actions: which alerts open a case automatically, which need an analyst decision, which are suppressed. They should be based on scenarios and data: a rule whose alerts were 95% benign over three months needs tuning, not an automatic case. Escalation thresholds name the triggers that move a case to S1 or wake the director: personal data involved, public service down beyond its recovery time objective, media inquiry, regulator contact.

### 13.4 Worked example (synthetic): applying the scale

*Fictional.* Three alerts arrive within an hour.

1. Edge blocked 3,000 login attempts against the staff portal from one range; no successes. → S4, no case; rule counts feed a weekly report.
2. `billing-clerk-7` signed in from a new country, approved MFA, downloaded 4,200 customer records via the billing export. The clerk is on leave. → S2 immediately (confirmed account compromise with tier-1 data access); escalate to S1 if export to an external location is confirmed. The incident lead is paged; the privacy officer is informed under the escalation threshold.
3. Endpoint detection on a reception PC: macro document blocked. → S4 if blocked and no execution; S3 if any child process ran.

### 13.5 Common errors and limits

- Severity based on how alarming an alert *sounds* rather than criteria.
- Never lowering severity, which exhausts the team.
- Thresholds copied from a vendor default without reference to local scenarios.
- Escalation triggers that depend on a judgement nobody is authorized to make.

### Exercises — chapter 13

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX037 — Write a scenario.** *Steps:* write the ransomware-on-file-servers scenario with entry, assets, impact, early evidence and detection gaps. *Rubric:* 3 = all five concrete and linked to inventory; 2 = missing gaps; 1 = generic; 0 = none.

**EX038 — Classify cases.** *Steps:* assign S1–S4 to five synthetic situations: lost unencrypted laptop of a permits officer; DDoS slows appointments for 20 minutes; confirmed web shell on `permit-app-2`; an employee emails a spreadsheet of residents to a personal address; billing database encrypted. *Rubric:* 3 = all defensible with criteria cited; 2 = four; 1 = two; 0 = none.

**EX039 — Tuning decision.** *Steps:* a rule produced 240 alerts in 90 days, 3 true positives (all S3). Propose a threshold decision. *Rubric:* 3 = calculates ~1.25% precision, keeps detection but tunes or enriches, measures again, avoids suppressing outright without analysis; 2 = no measurement; 1 = suppress; 0 = none.

### Chapter synthesis

Write concrete scenarios from your inventory and threat information; define severity by observable criteria; tune triage thresholds with data; and specify escalation triggers someone is authorized to act on.

<!-- cyberabc:chapter-navigation:start ch-13 -->
### Continue studying — chapter 13 of 30

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — Case intake, scope and ownership methods

### Learning outcomes and connection

You will be able to (1) run a structured intake that turns a report into a case; (2) state a case scope that is specific and revisable; and (3) assign and transfer ownership without gaps. Chapter 13 decided which events deserve a case; this chapter is about opening that case well.

### 14.1 Intake channels

Reports reach Fernmoor through detection alerts, the service desk, staff emails to the response mailbox, residents via the contact centre, suppliers and external parties (researchers, other CSIRTs, law enforcement). Each channel needs a route into the same case system and an acknowledgment to the reporter. A public security contact (for example a `security.txt` file published per RFC 9116) helps external reporters find the right channel.

### 14.2 Intake questions

Who reported, how to reach them, what they observed (exact words), when, which systems or accounts, what they have already done (rebooted? forwarded the email to colleagues?), and whether evidence exists (screenshots, original email with headers). Record observations separately from interpretations.

### 14.3 Scope statements

A scope statement says what the case covers *now*: affected assets and identities, time window, question to answer. Example: "Determine whether `billing-clerk-7` was used by an unauthorized party between 1 and 9 June and what data that account accessed." Scope changes as evidence arrives; record each change, because unrecorded scope creep is how cases become endless, and unrecorded narrowing is how related activity is missed.

### 14.4 Ownership

Every case has one owner at all times. Ownership transfers explicitly (Chapter 26) with acknowledgment. Tasks inside a case also have owners and due times. Related cases are linked rather than merged until evidence shows the same incident.

### 14.5 Worked example (synthetic): a resident's call

*Fictional.* A resident calls the contact centre: she received an email "from Fernmoor Water" asking her to pay an overdue bill through a link; she paid €84. The contact-centre agent uses the intake form: caller details; exact email text and sender address (`billing@fernmoor-water.example`, not Fernmoor's real domain `fernmoor.example`); time received; link domain; payment made; whether others have reported (two similar calls today). The duty analyst opens case FCS-221, S3, scope: "Phishing campaign impersonating Fernmoor billing, 10 June onward; identify domains, volume of residents affected, and whether Fernmoor data was used to target them." Tasks: request header copy from the resident (owner: contact centre); check whether recipients match Fernmoor's billing list (owner: Data Platform); prepare a resident warning with communications (owner: liaison). The resident is told to contact her bank; Fernmoor does not handle her payment dispute but records it.

When the Data Platform check showed that all three callers' addresses were in a billing export sent to a print supplier, scope expanded to include the supplier; the change and its reason were recorded and severity raised to S2.

### 14.6 Common errors and limits

- Recording interpretations as observations ("phishing attack by criminals").
- Vague scope ("investigate the phishing").
- Merging cases before evidence connects them.
- Unacknowledged reporters who stop reporting.

### Exercises — chapter 14

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX040 — Intake form.** *Steps:* design a ten-field intake form for the contact centre. *Rubric:* 3 = reporter/contact, observation verbatim, time, systems/accounts, actions taken, evidence available, harm (e.g., payment), other reports, agent, consent to follow-up; 2 = seven; 1 = few; 0 = none.

**EX041 — Scope rewrite.** *Steps:* rewrite three vague scopes into specific ones. *Rubric:* 3 = each has assets/identities, window and question; 2 = two; 1 = one; 0 = none.

**EX042 — Scope change record.** *Steps:* write the record for the supplier expansion in §14.5. *Rubric:* 3 = old scope, new scope, triggering evidence, time, who approved, severity change; 2 = missing approval; 1 = vague; 0 = none.

### Chapter synthesis

Route every channel into one case system; capture observations verbatim; write specific, revisable scopes and record each change with its reason; and keep one named owner per case and per task.

<!-- cyberabc:chapter-navigation:start ch-14 -->
### Continue studying — chapter 14 of 30

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — Guided lab: reconstruct a bounded incident timeline

### Learning outcomes and connection

You will be able to (1) normalize timestamps from sources with different zones and clock errors; (2) merge them into a bounded timeline with each correction recorded; and (3) state what the timeline shows and what remains unknown. This guided lab applies Chapters 4, 9, 12 and 14 to one case.

### 15.1 Why timelines matter

A timeline orders events so that causes can be distinguished from effects. It answers "what happened first?", "how long did the actor have?" and "what was the earliest evidence we missed?". It is only as good as its clocks: a five-minute error can reverse a sign-in and a file access.

### 15.2 Normalization rules

Convert every timestamp to UTC in RFC 3339 form. For each source, record the original format, its zone (explicit, configured or assumed) and any measured clock offset. Measure offsets at collection by comparing the source's clock with an NTP-synchronized reference (RFC 5905); record the measurement. Never silently "fix" a time; keep original and corrected values.

### 15.3 Bounding

A **bounded** timeline has a defined start and end and a defined set of sources. State them. Gaps inside the bound are as important as events: "VPN logs present; file server logs only from 14:00; no endpoint data for the clerk's laptop".

### 15.4 Lab T-15 (synthetic): permits-clerk-4

Case FCS-214 (fictional): did someone use `permits-clerk-4` to read the permits archive? Sources: identity provider logs in UTC; VPN appliance logs in local time without a zone (the appliance is configured for UTC−5); file-server audit logs whose clock was measured 95 seconds fast at collection. The script applies each correction and prints the merged timeline.

```python
# Lab T-15: reconstruct a bounded timeline from three synthetic sources
from datetime import datetime, timedelta, timezone
# Source clocks: IdP logs UTC; VPN appliance local time UTC-5 (no zone in log);
# file server clock measured 95 seconds fast against NTP at collection.
idp = [("2026-05-11T14:02:10Z","signin ok user=permits-clerk-4 from 198.51.100.23 mfa=push-approved"),
       ("2026-05-11T14:20:44Z","mfa method added user=permits-clerk-4")]
vpn = [("2026-05-11 09:03:02","session start user=permits-clerk-4 src=198.51.100.23"),
       ("2026-05-11 09:41:30","session end user=permits-clerk-4")]
fs  = [("2026-05-11T14:12:35Z","bulk read 412 files share=permits-archive user=permits-clerk-4")]
ev=[]
for t,m in idp: ev.append((datetime.fromisoformat(t.replace("Z","+00:00")),"IdP",m,"none"))
for t,m in vpn:
    d=datetime.strptime(t,"%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone(timedelta(hours=-5)))
    ev.append((d.astimezone(timezone.utc),"VPN",m,"+5h zone"))
for t,m in fs:
    ev.append((datetime.fromisoformat(t.replace("Z","+00:00"))-timedelta(seconds=95),"FS",m,"-95s skew"))
for d,s,m,c in sorted(ev):
    print(d.strftime("%Y-%m-%dT%H:%M:%SZ"), s.ljust(3), f"[{c}]", m)
first=min(e[0] for e in ev); last=max(e[0] for e in ev)
print("window minutes", round((last-first).total_seconds()/60, 1))
```

Expected output:

```text
2026-05-11T14:02:10Z IdP [none] signin ok user=permits-clerk-4 from 198.51.100.23 mfa=push-approved
2026-05-11T14:03:02Z VPN [+5h zone] session start user=permits-clerk-4 src=198.51.100.23
2026-05-11T14:11:00Z FS  [-95s skew] bulk read 412 files share=permits-archive user=permits-clerk-4
2026-05-11T14:20:44Z IdP [none] mfa method added user=permits-clerk-4
2026-05-11T14:41:30Z VPN [+5h zone] session end user=permits-clerk-4
window minutes 39.3
```

Reading the result: the IdP sign-in (14:02:10) precedes the VPN session (14:03:02) by under a minute from the same address, consistent with one actor. The bulk read of 412 files at corrected 14:11:00 falls inside the session. The new MFA method at 14:20:44 suggests persistence. Without the zone correction, the VPN session would have appeared five hours *before* the sign-in; without the skew correction, the file read would have moved by 95 seconds — not decisive here but recorded. What remains unknown: whether the clerk herself was acting (she must be interviewed with her manager, Chapter 16), and what was done with the 412 files.

### 15.5 Timeline record format

Each row: corrected UTC time, source, original timestamp, correction applied, event, actor, asset, evidence reference (file and hash), analyst note. Analyst notes are labelled as interpretation.

### 15.6 Common errors and limits

- Assuming a log without a zone is UTC.
- Ignoring measured skew because it is small.
- Mixing interpretation into event descriptions.
- Unbounded timelines that grow until nobody can read them.

### Exercises — chapter 15

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX043 — Wrong assumption.** *Steps:* rerun the lab treating VPN times as UTC. Describe the resulting timeline and the false conclusion it invites. *Rubric:* 3 = VPN session appears at 09:03–09:41, before sign-in, implying VPN access without the IdP sign-in and ending before the file read; explains the false conclusion; 2 = describes only; 1 = partial; 0 = none.

**EX044 — Gap statement.** *Steps:* write the bound and gap statement for FCS-214. *Rubric:* 3 = start/end, sources, known gaps (laptop endpoint, data after read, email), impact on conclusions; 2 = missing impact; 1 = vague; 0 = none.

**EX045 — Timeline row.** *Steps:* write the full record row for the file-server event. *Rubric:* 3 = all §15.5 fields with original and corrected times and hash reference; 2 = missing original or hash; 1 = partial; 0 = none.

### Chapter synthesis

Normalize every time to UTC with recorded zone and skew corrections, keep originals, bound the timeline by window and sources, state gaps explicitly and keep interpretation labelled. Small clock errors can invert causality; corrections are evidence too.

<!-- cyberabc:chapter-navigation:start ch-15 -->
### Continue studying — chapter 15 of 30

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — Investigation methods across multiple data sources

### Learning outcomes and connection

You will be able to (1) frame investigation questions as testable hypotheses; (2) pivot across identity, endpoint, network and cloud data using shared keys; and (3) document findings with their supporting and contradicting evidence. Chapter 15 built one timeline; this chapter teaches the method for growing a case across sources without losing rigour.

### 16.1 Questions and hypotheses

Start from the scope question and list plausible explanations. For FCS-214: H1 the clerk read the archive for work; H2 an external actor used her credentials; H3 a malicious insider used her account. For each hypothesis, ask what evidence would be expected if it were true and what would contradict it. Chamberlin's "multiple working hypotheses" and Platt's "strong inference" are old but still the right discipline: seek evidence that discriminates, not evidence that merely fits your favourite.

### 16.2 Pivoting

A **pivot** follows a shared key from one source to another: account id from IdP to file server; source address from IdP to edge and VPN; host name from endpoint to inventory; file hash from endpoint to threat information; access key id from cloud audit to data-read logs. Record each pivot (from, key, to, query, result) so the path can be repeated.

### 16.3 Scoping outward

When a hypothesis gains support, ask what else the actor could reach: other accounts used from the same address; other hosts with the same persistence; other buckets accessed with the same key. This is where inventory dependencies (Chapter 11) guide the search.

### 16.4 Worked example (synthetic): FCS-214 continued

Pivot 1: source 198.51.100.23 in IdP logs over 30 days → also used for failed sign-ins against 14 other staff accounts on 9–10 May (password spraying). Pivot 2: those 14 accounts in IdP success logs → one more success, `hr-assist-5`, on 10 May, no MFA prompt because a legacy protocol was allowed. Pivot 3: `hr-assist-5` in mailbox audit → an inbox rule hiding messages from the service desk. Pivot 4: the clerk's interview (with her manager, recorded) → she was in a training session at 14:00–15:00 on 11 May with her laptop closed; her approval of a push at 14:02 came from her phone during the session.

Hypothesis table:

| Evidence | H1 clerk for work | H2 external actor | H3 insider |
|---|---|---|---|
| Spraying from same address against 14 accounts | inconsistent | consistent | inconsistent |
| Clerk in training, laptop closed | inconsistent | consistent | neutral |
| New MFA method at 14:20 | inconsistent | consistent | weakly consistent |

H2 is best supported. Scope expanded to include `hr-assist-5`; legacy protocols were scheduled for disablement.

### 16.5 Interviews

Interviewing staff is part of investigation but involves people's rights and employment. Fernmoor's rule: interviews about a staff member's account are arranged with their manager or HR, are factual and non-accusatory, and are recorded in the case.

### 16.6 Common errors and limits

- Seeking only confirming evidence.
- Unrecorded pivots that nobody can repeat.
- Treating an address as one actor without checking shared infrastructure.
- Concluding intent from technical evidence alone.

### Exercises — chapter 16

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX046 — Expected evidence.** *Steps:* for H1–H3 in §16.1, list two items of evidence each would predict. *Rubric:* 3 = two discriminating predictions for each; 2 = some non-discriminating; 1 = one hypothesis only; 0 = none.

**EX047 — Pivot log.** *Steps:* write the pivot log for pivots 1–3. *Rubric:* 3 = from, key, to, query, result for each; 2 = missing queries; 1 = narrative; 0 = none.

**EX048 — Interview plan.** *Steps:* write five neutral questions for the clerk interview. *Rubric:* 3 = factual, open, non-accusatory, cover location, devices, prompts received, use of archive, other observations; 2 = one leading question; 1 = accusatory; 0 = none.

### Chapter synthesis

Investigate with multiple hypotheses and discriminating evidence; pivot across sources by shared keys and log every pivot; scope outward using dependencies; and handle interviews fairly and on the record.

<!-- cyberabc:chapter-navigation:start ch-16 -->
### Continue studying — chapter 16 of 30

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — Case-management and evidence-storage tooling

### Learning outcomes and connection

You will be able to (1) select or configure a case-management tool that implements the Chapter 4 data model; (2) set up an evidence store with integrity, custody and access controls; and (3) write acceptance criteria for both. Chapters 14–16 showed how cases are run; this chapter provides the tools that hold them.

### 17.1 Case-management requirements

Requirements follow from the data model and the service: structured fields with enumerations; required fields by status; links between cases, events, artefacts, actions and decisions; task assignment with due times; an immutable activity history (who changed what, when); role-based access with case-level restriction for sensitive cases (HR, insider); search and export; and an API for automation (Chapter 22). Fernmoor compared an open-source incident platform, a module of its existing IT service-management tool and a spreadsheet; the spreadsheet failed on history, access control and required fields.

### 17.2 Evidence store requirements

The evidence store holds preserved artefacts: log exports, images, memory captures, screenshots, emails. Requirements: storage separate from production administration; write-once or versioned storage; SHA-256 hashing on ingest (FIPS 180-4) and periodic verification; a custody record for each item (who collected, when, from where, every transfer and access); restricted and logged access; retention aligned with records and legal policy; and capacity for large images. ISO/IEC 27037 and NIST SP 800-86 describe the identification, collection, acquisition and preservation steps that this store supports.

### 17.3 Custody in practice

For most internal cases, a well-kept digital custody log is enough: item id, description, source, collector, time, hash, storage location, and each access with purpose. If a case may go to court or a regulator, involve counsel early; stricter procedures may apply.

### 17.4 Worked example (synthetic): acceptance testing the tools

*Fictional.* Fernmoor chose the ITSM module with a security-incident record type plus an object-storage bucket in a separate cloud account for evidence. Acceptance criteria and results:

| Criterion | Test | Result |
|---|---|---|
| Severity required at triage | move test case to triage without severity | blocked — pass |
| HR cases restricted | analyst outside HR group opens HR test case | denied, attempt logged — pass |
| History immutable | admin edits a closed case field | change recorded in history — pass |
| Evidence write-once | delete test artefact with response role | denied by object lock — pass |
| Hash on ingest | upload test file, compare stored hash with local | match — pass |
| Access logged | download artefact | access log entry within 5 min — **fail (60 min delay)** |

The failing criterion was accepted with a documented risk and a fix date; the go-live note recorded it.

### 17.5 Common errors and limits

- Evidence on analysts' laptops or shared drives.
- Hashes computed but never verified again.
- Case tools whose administrators can silently edit history.
- Choosing a tool for features rather than tested acceptance criteria.

### Exercises — chapter 17

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX049 — Requirements list.** *Steps:* list eight must-have requirements for the case tool, each traceable to a chapter. *Rubric:* 3 = eight traceable requirements; 2 = six; 1 = generic; 0 = none.

**EX050 — Custody log.** *Steps:* write custody entries for a memory capture from `permit-app-2` from collection to analysis. *Rubric:* 3 = collection entry with hash, transfer to store, each access with purpose and person, verification; 2 = missing accesses; 1 = one line; 0 = none.

**EX051 — Failed criterion.** *Steps:* write the risk-acceptance note for the access-log delay. *Rubric:* 3 = description, impact, compensating control, owner, fix date, approver; 2 = missing compensating control; 1 = vague; 0 = none.

### Chapter synthesis

Choose tools by tested acceptance criteria derived from your data model and service: structured, access-controlled, history-preserving case records and a separate, write-once, hashed and logged evidence store with custody records.

<!-- cyberabc:chapter-navigation:start ch-17 -->
### Continue studying — chapter 17 of 30

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Containment and recovery control implementation

### Learning outcomes and connection

You will be able to (1) implement pre-built containment actions with tested side effects and rollback; (2) implement and time recovery procedures, including restoring from backup; and (3) verify that containment and recovery worked. Chapters 6–8 showed containment ideas; this chapter turns them into implemented controls the duty analyst can trigger safely.

### 18.1 Containment actions as products

Each common containment action becomes a documented, tested capability: disable account and revoke sessions; isolate an endpoint through the agent; move a VM to quarantine; block an address or domain at the edge and DNS resolver; disable a public feature behind a flag; rotate a service credential. For each: trigger (who may run it), procedure or automation, expected side effects, verification step and rollback. Test each quarterly in a non-production environment and record the time taken.

### 18.2 Recovery

NIST SP 800-184 describes recovery planning: prioritized restoration, validated clean sources, and improvement. Recovery controls include immutable or offline backups, documented restore procedures with measured times, clean build images, and validation steps before reconnecting to production. Restore tests should restore to an isolated environment and check data integrity, not just that the job "succeeded".

### 18.3 Verification

Containment is complete only when verified: the account cannot sign in (test), sessions are gone (check active sessions list), the host cannot reach anything but the evidence share (connectivity test), the blocked address produces denials (edge log). Recovery is complete when the service owner accepts functional tests and monitoring is in place for re-infection.

### 18.4 Worked example (synthetic): timed restore of `appt-db-1`

*Fictional.* Chapter 1 noted the appointment database restore had never been timed. The team ran a test:

| Step | Planned | Actual | Note |
|---|---|---|---|
| Retrieve nightly backup from object store | 10 min | 9 min | |
| Restore to isolated DB host | 30 min | 71 min | restore tool single-threaded; documented flag cut it to 28 min on retest |
| Integrity checks (row counts, checksum of key tables vs backup report) | 15 min | 15 min | |
| Point-in-time recovery from WAL to 1 h before incident | 20 min | not possible | WAL archiving off — **finding** |
| Application smoke test | 10 min | 12 min | |

Results: recovery time 107 minutes on first run, 64 on retest, against a tier-2 objective of 4 hours — met. Recovery point: up to 24 hours of appointments could be lost because WAL archiving was off — an objective of 1 hour was **not** met. A change enabled WAL archiving to the separate backup account; a retest showed point-in-time recovery working.

### 18.5 Common errors and limits

- Containment that has never been tested and fails at 03:00.
- "Backup succeeded" without a restore test.
- Restoring into production before validating that the backup is clean.
- Forgetting to verify containment; the attacker's second account still works.

### Exercises — chapter 18

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX052 — Action card.** *Steps:* write the action card for "move VM to quarantine segment". *Rubric:* 3 = trigger/authority, steps, side effects, verification, rollback, test record; 2 = missing two; 1 = steps only; 0 = none.

**EX053 — Restore test plan.** *Steps:* write a restore test plan for `billing-db`. *Rubric:* 3 = isolated target, timed steps, integrity checks, RPO/RTO comparison, findings and owner; 2 = no integrity checks; 1 = vague; 0 = none.

**EX054 — Verify containment.** *Steps:* list verification checks for containing a compromised `svc-reports` cloud key. *Rubric:* 3 = key disabled/deleted, API call with key fails, no other keys for principal, audit shows no new keys, resources created by key reviewed; 2 = three; 1 = one; 0 = none.

### Chapter synthesis

Turn containment and recovery into tested products with authority, side effects, verification and rollback; time restores in isolation and compare with recovery objectives; and never call an action done until verification proves it.

<!-- cyberabc:chapter-navigation:start ch-18 -->
### Continue studying — chapter 18 of 30

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-19"></a>

## Chapter 19 — Detection-to-response monitoring and feedback

### Learning outcomes and connection

You will be able to (1) connect each detection rule to a response action and an owner; (2) record case outcomes back against the detections that raised them; and (3) use that feedback to tune, retire or create detections. Chapter 13 set thresholds; Chapter 18 built actions; this chapter closes the loop between them.

### 19.1 From rule to runbook

Every detection that can open a case should point to a runbook: what the analyst checks first, what evidence to preserve, which containment action applies and who approves it. A rule without a runbook produces inconsistent triage; a runbook without a rule depends on luck. Fernmoor keeps a **detection register**: rule id, scenario (Chapter 13), data source (Chapter 12), runbook, owner, last tuned date and quality figures.

### 19.2 Outcome labels

When a case closes, the analyst labels the triggering alert: true positive (malicious or policy-violating activity), benign true positive (the rule worked, the activity was authorized), false positive (the rule matched something it should not), or undetermined. These labels, collected over months, show which rules earn their cost. The CSF 2.0 Detect function includes continuous monitoring and analysis of adverse events; feedback labels are how monitoring improves.

### 19.3 Coverage and misses

Also record cases that *no* detection found: reports from residents, suppliers or staff. Each miss is a candidate for a new detection or a data-source gap. Mapping cases to ATT&CK techniques helps reveal which techniques you detect and which you only learn about by accident.

### 19.4 Worked example (synthetic): a quarter's register

*Fictional.* Q2 detection register excerpt:

| Rule | Alerts | TP | Benign TP | FP | Undet. | Cases found by other means for this technique |
|---|---:|---:|---:|---:|---:|---:|
| R-07 impossible travel | 52 | 4 | 31 | 15 | 2 | 1 |
| R-12 new MFA method off-hours | 9 | 3 | 6 | 0 | 0 | 0 |
| R-19 bulk file read | 120 | 1 | 104 | 15 | 0 | 1 |
| R-23 edge enumeration | 6 | 2 | 0 | 4 | 0 | 0 |

Decisions: R-07 — add known corporate VPN egress as enrichment to cut benign TPs; R-12 — keep, high value; R-19 — most benign TPs are the nightly backup account; exclude it *only* for its scheduled window and host, and alert if it reads outside; R-23 — tune threshold upward and add sequential-id detection. Two cases came from staff reports (a phished account and an insider spreadsheet); both added detection ideas to the backlog with owners.

### 19.5 Common errors and limits

- Treating benign true positives as false positives, which leads to removing good rules.
- Broad exclusions ("ignore the backup account") that create blind spots attackers can use.
- Never labelling outcomes, so no rule is ever improved.
- Counting alerts as a productivity measure.

### Exercises — chapter 19

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX055 — Precision.** *Steps:* compute the share of R-07 and R-19 alerts that were true positives and interpret. *Rubric:* 3 = R-07 4/52 ≈ 7.7%, R-19 1/120 ≈ 0.8%, with interpretation that benign TPs dominate and enrichment helps; 2 = numbers only; 1 = wrong; 0 = none.

**EX056 — Safe exclusion.** *Steps:* write the R-19 exclusion precisely. *Rubric:* 3 = account, host, time window, share; alert on any deviation; review date; 2 = missing deviation alert; 1 = broad; 0 = none.

**EX057 — From miss to rule.** *Steps:* for the insider spreadsheet case found by a staff report, propose a detection with its data source and runbook first step. *Rubric:* 3 = specific logic (e.g., large export from billing DB to personal email/external domain), source, threshold, runbook step involving HR/privacy; 2 = vague logic; 1 = idea only; 0 = none.

### Chapter synthesis

Link every detection to a runbook and owner, label outcomes at closure, record cases no rule found, and tune with narrow, monitored exclusions. The detection register is how the response service learns.

<!-- cyberabc:chapter-navigation:start ch-19 -->
### Continue studying — chapter 19 of 30

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-20"></a>

## Chapter 20 — Troubleshoot incomplete or contradictory case records

### Learning outcomes and connection

You will be able to (1) detect incomplete or contradictory case records systematically; (2) diagnose their causes in process, tooling or data; and (3) correct records without destroying the original history. Chapters 17–19 built tools and feedback; real records still go wrong, and a technologist must repair both the record and the cause.

### 20.1 Types of defect

- **Missing:** no triage time, no closure reason, no owner for a period.
- **Contradictory:** action time before decision time; status "closed" with open tasks; severity S4 but a regulator notification recorded.
- **Inconsistent with evidence:** case says host isolated at 10:00; endpoint logs show it communicating at 10:30.
- **Duplicated:** two cases for the same incident with diverging facts.

### 20.2 Finding defects

Run automated checks against the case database: required fields by status, ordering constraints (opened ≤ triage ≤ decision ≤ action ≤ closed), cross-field rules (S1 requires an incident lead), and reconciliation with evidence sources (claimed containment vs telemetry). Run them nightly and in the monthly report. Sample a few cases manually each month as well; automated checks only find the defects you anticipated.

### 20.3 Diagnosing causes

Ask why each defect happened. Typical causes: a field that cannot be filled on mobile; clocks on a tool set to local time; an automation writing the action time when the job was queued, not when it ran; analysts working in chat and updating the case later from memory; unclear definitions. Fix the cause, not only the record — otherwise the defect returns.

### 20.4 Correcting records

Never overwrite silently. Add a correction entry: field, old value, new value, source of the correct value, who corrected, when. The history must show both. For cases with legal or regulatory relevance, involve counsel before correcting anything material.

### 20.5 Worked example (synthetic): isolation that wasn't

*Fictional.* The nightly check flagged FCS-245: "host `reception-pc-3` isolated 10:02 (action recorded)" but endpoint telemetry showed DNS queries to an unknown domain at 10:27. Diagnosis: the automation recorded the time the isolation request was *queued*; the agent on that PC was offline (laptop lid closed), so isolation applied only at 10:41 when it reconnected. The 25 minutes of activity were real and in scope. Corrections: action time updated with a correction entry (10:02 queued, 10:41 applied, source agent log); case scope extended to the 10:27 domain. Cause fix: the automation now records `requested_at` and `confirmed_at` separately and alerts if confirmation does not arrive within 5 minutes; the runbook adds "verify isolation in console".

### 20.6 Common errors and limits

- Fixing records by hand without fixing the process that broke them.
- Rewriting history to look tidy.
- Trusting automation timestamps without knowing what event they record.
- Checks so noisy that analysts ignore them.

### Exercises — chapter 20

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX058 — Check rules.** *Steps:* write six automated consistency rules for the case database. *Rubric:* 3 = six precise rules covering required fields, ordering, cross-field, evidence reconciliation; 2 = four; 1 = vague; 0 = none.

**EX059 — Correction entry.** *Steps:* write the correction entry for FCS-245. *Rubric:* 3 = field, old, new, source, who, when, reason; 2 = missing source; 1 = overwrite; 0 = none.

**EX060 — Root cause.** *Steps:* for "triage times missing for 30% of out-of-hours cases", list three plausible causes and a test for each. *Rubric:* 3 = three causes with discriminating tests; 2 = causes without tests; 1 = one; 0 = none.

### Chapter synthesis

Check records automatically and by sampling, diagnose each defect to its process or tooling cause, correct with visible history, and fix the cause so the defect does not return.

<!-- cyberabc:chapter-navigation:start ch-20 -->
### Continue studying — chapter 20 of 30

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 →](#ch-21)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-21"></a>

## Chapter 21 — Integrate response with service management

### Learning outcomes and connection

You will be able to (1) connect security incidents to IT service-management processes for incidents, problems, changes and configuration; (2) design an emergency change path for containment; and (3) prevent the two common failures — security cases lost in the IT queue, and security changes that break services. Chapter 17 placed the case tool inside the ITSM platform; this chapter integrates the processes.

### 21.1 Where the processes meet

**IT incident management** restores normal service; **security incident response** also investigates, preserves evidence and may need confidentiality. **Problem management** finds root causes; **change management** controls modifications; the **configuration management database** (CMDB) holds the inventory (Chapter 11). Frameworks such as ITIL describe these practices; ISO/IEC 20000-1 specifies requirements for a service-management system. The integration points: routing (an IT ticket that looks like security becomes a security case, restricted), linking (outages caused by a security incident link both records), changes (containment and remediation are changes), and problems (recurring security causes become problems with owners).

### 21.2 Emergency change

Containment cannot wait for a weekly change board. Define a security emergency change: pre-approved standard changes for the actions in Chapter 18 (logged after the fact), and an emergency change path for others with a named approver available at any hour, a minimum record (what, why, risk, rollback) and a retrospective review at the next board. The goal is speed with accountability.

### 21.3 Confidentiality

Security cases may involve staff misconduct, personal data or attacker monitoring of IT tickets. Use restricted record types; keep sensitive details out of broadly visible change titles ("Rotate credentials for service X" rather than "Attacker has svc-patch password").

### 21.4 On-call integration

The response on-call rota should live in the same paging system as IT operations, with escalation if unacknowledged. Chapter 9's lab showed out-of-hours triage delays; Fernmoor's fix was paging S1–S2 to the response on-call through the IT paging tool with a 15-minute escalation to the deputy.

### 21.5 Worked example (synthetic): linking a ransomware outage

*Fictional.* At 06:10 the service desk logs "billing system slow, files renamed". The ITSM rule matches the keywords "renamed" and "ransom" and routes a restricted security case, paging the response on-call (acknowledged 06:16). Records created and linked: security case FCS-260 (S1), IT major incident INC-8812 for the billing outage (visible to service desk, with neutral wording), emergency change CHG-3301 to isolate `fs-01` (approved by the on-call infrastructure manager at 06:31), and later problem PRB-140 "shared admin credential across file servers". Status updates to the service desk came from INC-8812; investigation details stayed in FCS-260.

### 21.6 Common errors and limits

- Security cases closed by IT once the service is restored, before investigation ends.
- Emergency changes without retrospective review.
- Sensitive details in broadly visible tickets.
- Separate paging systems that nobody watches at night.

### Exercises — chapter 21

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX061 — Routing rules.** *Steps:* write four rules that route IT tickets to security cases. *Rubric:* 3 = specific triggers (keywords, categories, asset tier, reporter type) with restriction and paging; 2 = vague triggers; 1 = one; 0 = none.

**EX062 — Emergency change record.** *Steps:* write CHG-3301 minimum record. *Rubric:* 3 = what, why (neutral), risk, rollback, approver, time, link to case, retrospective date; 2 = missing rollback; 1 = vague; 0 = none.

**EX063 — Closure rule.** *Steps:* define when INC-8812 and FCS-260 may each be closed. *Rubric:* 3 = INC on service restoration and owner acceptance; FCS on investigation complete, residual risk accepted, review done; linked problem open as needed; 2 = one; 1 = same rule; 0 = none.

### Chapter synthesis

Integrate response with incident, change, problem and configuration processes; give containment a fast, accountable emergency change path; protect confidentiality; and keep service restoration and security closure as separate, linked decisions.

<!-- cyberabc:chapter-navigation:start ch-21 -->
### Continue studying — chapter 21 of 30

[← Chapter 20](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 →](#ch-22)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-22"></a>

## Chapter 22 — Automate repeatable evidence and notification tasks

### Learning outcomes and connection

You will be able to (1) choose which response tasks to automate and which to keep human; (2) build evidence-collection automation that preserves integrity; and (3) automate internal notifications with safeguards against error. Chapter 3 introduced scripting; Chapters 17–21 provided the tools and processes into which automation now plugs.

### 22.1 What to automate

Good candidates are frequent, well-defined and low-judgement: enriching an alert with inventory and identity data; exporting standard log sets for a case; hashing and registering artefacts; creating linked records; paging; reminding owners of overdue tasks; drafting status updates from case fields. Keep humans for judgement and irreversible or high-impact actions: severity decisions beyond rules, external notifications, disabling public services, contacting employees. CISA's playbooks and many security-orchestration tools follow the same split between automated enrichment and human-approved response.

### 22.2 Design rules

Each automation has an owner, a version under source control, tests with known inputs, logging of every run (inputs, outputs, errors), idempotence (running twice does no harm), safe failure (on error, stop and alert a human rather than half-complete), and least-privilege credentials stored in a secrets manager, not in the script.

### 22.3 Lab T-22 (synthetic): evidence manifest with verification

This script builds a SHA-256 manifest for three exported files of case FCS-214, then simulates a later verification in which one file was re-saved by a text editor that added a newline. It prints the manifest, the failure and a structured note for the case.

```python
# Lab T-22: build and verify an evidence manifest (SHA-256, FIPS 180-4)
import hashlib, json
items = {"idp_export_FCS-214.json": b'{"user":"permits-clerk-4","events":12}\n',
         "vpn_FCS-214.log": b"09:03:02 session start\n09:41:30 session end\n",
         "fs_audit_FCS-214.csv": b"time,user,files\n14:12:35,permits-clerk-4,412\n"}
manifest = {n: hashlib.sha256(b).hexdigest() for n,b in sorted(items.items())}
for n,h in manifest.items(): print(h[:16], len(items[n]), n)
# later verification: one file was re-saved by an editor that added a trailing newline
items["vpn_FCS-214.log"] += b"\n"
bad = [n for n,b in sorted(items.items()) if hashlib.sha256(b).hexdigest()!=manifest[n]]
print("verification failures:", bad)
note = {"case":"FCS-214","failed":bad,"action":"use preserved original; record deviation"}
print(json.dumps(note, sort_keys=True))
```

Expected output:

```text
bdeae596d177e5ad 45 fs_audit_FCS-214.csv
ae76b3b651ddaa47 39 idp_export_FCS-214.json
847409adc14e0145 44 vpn_FCS-214.log
verification failures: ['vpn_FCS-214.log']
{"action": "use preserved original; record deviation", "case": "FCS-214", "failed": ["vpn_FCS-214.log"]}
```

The manifest shows the first 16 hex characters of each hash and the byte length (store the full hash in practice). A single added byte changes the hash completely, so verification detects the edit; the response is to use the preserved original from the write-once store and record the deviation, not to "fix" the working copy. The structured note is suitable for the case API.

### 22.4 Notifications

Internal notifications (page the on-call, inform the privacy officer at S2 with personal data, update the service desk) can be automated from case fields. Safeguards: templates reviewed by the owners; recipients from a maintained directory, not typed; rate limits; a test mode; and a human check for any message leaving Fernmoor. External notifications to residents, regulators or the press are drafted by automation at most, approved and sent by people authorized by the charter (Chapter 10).

### 22.5 Worked example (synthetic): enrichment that misled

*Fictional.* An enrichment step added the inventory owner to each alert. A stale CMDB entry named a person who had left Fernmoor; the automation paged her personal phone for three weeks. Fixes: the automation now validates owners against the active directory and falls back to the team rota; the inventory reconciliation (Chapter 11) flags owners who left.

### 22.6 Common errors and limits

- Automating a broken process, which produces wrong results faster.
- Credentials embedded in scripts.
- Silent partial failures.
- Automations nobody owns after their author moves on.

### Exercises — chapter 22

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX064 — Automate or not.** *Steps:* classify eight tasks as automate, automate-with-approval or human: enrich alert; disable user; isolate workstation; notify regulator; hash artefacts; create IT incident link; email all staff about phishing; page on-call. *Rubric:* 3 = all defensible with reasons; 2 = six; 1 = three; 0 = none.

**EX065 — Extend the lab.** *Steps:* modify the lab to store and print the full SHA-256 and to report files added or missing since the manifest. *Rubric:* 3 = code reports changed, added and missing; full hash; tested by adding a file; 2 = one of added/missing; 1 = attempted; 0 = none.

**EX066 — Run log.** *Steps:* define the fields an automation run log must record. *Rubric:* 3 = automation id/version, trigger, case id, inputs (with hashes), outputs, errors, start/end time, credential identity; 2 = five; 1 = two; 0 = none.

### Chapter synthesis

Automate frequent, well-defined, low-judgement tasks with owners, tests, logs, idempotence, safe failure and least privilege; verify evidence by hash against preserved originals; and keep humans in charge of judgement and anything leaving the organization.

<!-- cyberabc:chapter-navigation:start ch-22 -->
### Continue studying — chapter 22 of 30

[← Chapter 21](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 →](#ch-23)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-23"></a>

## Chapter 23 — Evaluate response latency and decision quality

### Learning outcomes and connection

You will be able to (1) break response time into stages and find where delay accumulates; (2) evaluate decision quality from the record rather than from outcomes; and (3) combine both into a service review that leads to specific changes. Chapter 9 defined measures; Chapters 17–22 produced the records; now you evaluate the service.

### 23.1 Stage latency

Total response time hides where delay lives. Split it: detect → triage (queue and on-call), triage → decision (information gathering and authority), decision → containment (execution and change path). Each stage has different causes and fixes: paging for the first, evidence access and pre-approval for the second, automation and tested actions for the third.

### 23.2 Decision quality

A good outcome does not prove a good decision, and a bad outcome does not prove a bad one; judging decisions by outcomes is hindsight bias (Fischhoff, 1975). Evaluate decisions by what the record shows was known and done at the time: was there a named owner, were the key facts gathered, were options considered, was a rollback or revisit condition stated? Fernmoor's decision record requires four elements: **owner**, **evidence** relied on, **option** chosen with alternatives, and **rollback** or revisit condition.

### 23.3 Lab T-23 (synthetic): six cases

```python
# Lab T-23: stage latency and decision-quality checks for six synthetic cases
from statistics import median
# minutes: detect->triage, triage->decision, decision->contain; decision record fields present
cases = {"FCS-301":(9,25,14,{"owner","evidence","option","rollback"}),
         "FCS-302":(31,12,6,{"owner","option"}),
         "FCS-303":(7,48,22,{"owner","evidence","option","rollback"}),
         "FCS-304":(12,15,95,{"owner","evidence","option"}),
         "FCS-305":(5,20,11,{"owner","evidence","option","rollback"}),
         "FCS-306":(64,18,9,{"evidence","option"})}
need = {"owner","evidence","option","rollback"}
for i,name in enumerate(["detect->triage","triage->decision","decision->contain"]):
    v=[c[i] for c in cases.values()]
    print(f"{name:18} median {median(v):5.1f} max {max(v)}")
tot={k:sum(c[:3]) for k,c in cases.items()}
print("total median", median(tot.values()))
for k,c in cases.items():
    miss=sorted(need-c[3])
    if miss: print(k, "total", tot[k], "missing", miss)
q=sum(1 for c in cases.values() if need<=c[3])
print("complete decision records", q, "of", len(cases))
```

Expected output:

```text
detect->triage     median  10.5 max 64
triage->decision   median  19.0 max 48
decision->contain  median  12.5 max 95
total median 63.0
FCS-302 total 49 missing ['evidence', 'rollback']
FCS-304 total 122 missing ['rollback']
FCS-306 total 91 missing ['owner', 'rollback']
complete decision records 3 of 6
```

Interpretation: the medians look acceptable, but the maxima reveal three different problems. FCS-306 waited 64 minutes for triage and had no recorded owner — a paging and ownership issue. FCS-304 took 95 minutes from decision to containment and lacked a rollback — consistent with an untested, unprepared action (it was a firewall change without a pre-built procedure). FCS-302 decided quickly but without recorded evidence or rollback — speed bought with poor decision hygiene. Only half the decision records were complete. These are records of six cases; they suggest where to look, not statistically established causes.

### 23.4 From evaluation to change

For each finding, propose one change, an owner and a measure to check it: build and test the firewall containment action (target: decision → contain ≤ 30 minutes for that action); make `owner` and `rollback` required fields at decision status (target: 100% completeness); review on-call escalation for S2 out of hours. Re-evaluate after a quarter with the same definitions.

### 23.5 Common errors and limits

- Judging decisions by outcomes.
- Only reporting totals or means.
- Treating six cases as proof.
- Measuring individuals instead of the system; people will game the fields.

### Exercises — chapter 23

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX067 — Recompute.** *Steps:* add `rollback` to FCS-304 and `owner` to FCS-306 in the lab; what changes? *Rubric:* 3 = complete records 4 of 6, FCS-304 no longer listed, FCS-306 lists only rollback; latencies unchanged; 2 = partly right; 1 = attempted; 0 = none.

**EX068 — Decision review.** *Steps:* review FCS-302's decision (disabled a public form within 6 minutes on an analyst's hunch; it turned out to be a real attack). Was it a good decision? *Rubric:* 3 = separates outcome from process; notes missing evidence and rollback; acknowledges speed was appropriate if authority existed; recommends recording; 2 = judges by outcome only partly; 1 = "good because it worked"; 0 = none.

**EX069 — Change proposal.** *Steps:* write one change proposal for FCS-304's finding. *Rubric:* 3 = problem with data, change, owner, measure, review date; 2 = missing measure; 1 = vague; 0 = none.

### Chapter synthesis

Split latency into stages to find where delay lives, evaluate decisions by the recorded process rather than outcomes, keep sample sizes in view, and convert each finding into an owned, measurable change.

<!-- cyberabc:chapter-navigation:start ch-23 -->
### Continue studying — chapter 23 of 30

[← Chapter 22](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 →](#ch-24)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-24"></a>

## Chapter 24 — Applied methods: compare two incident playbooks

### Learning outcomes and connection

You will be able to (1) compare two playbooks for the same scenario against explicit criteria; (2) test them with a tabletop walkthrough using the same inject; and (3) recommend a merged or chosen playbook with evidence. Chapters 18–23 built and measured actions; playbooks package them for a scenario.

### 24.1 What a playbook is

A **playbook** is a scenario-level guide: when it applies, roles, decision points, the runbooks it invokes, communications and closure criteria. A **runbook** is a step-level procedure for one task. CISA's federal incident response playbook is a public example of a scenario-level structure; many organizations also publish or share sector playbooks. A playbook should be short enough to use under stress and precise at decision points.

### 24.2 Comparison criteria

Fernmoor's criteria: (1) **trigger clarity** — can the duty analyst tell when it applies? (2) **decision points** — are decisions, owners and authority explicit? (3) **evidence preservation** before change; (4) **actionability** — does each step name a runbook or command? (5) **communications** — who is told, when, by whom? (6) **closure** — measurable conditions; (7) **fit** — does it match Fernmoor's tools and charter? Score each 0–2 with a written reason; scores are structured judgements, not measurements.

### 24.3 Testing by walkthrough

Read both playbooks against the same scripted inject with two different teams (or the same team on different days, noting learning effects). Time to first containment decision, number of questions the playbook could not answer, and errors made are recorded.

### 24.4 Worked example (synthetic): business email compromise

*Fictional.* Playbook A is a vendor template (14 pages); Playbook B was written by Fernmoor's Response Desk (3 pages linking runbooks). Inject: "Finance reports an invoice payment changed to a new bank account after an email from a known supplier."

| Criterion | A | B | Notes |
|---|---:|---:|---|
| Trigger clarity | 1 | 2 | A covers all email threats generically |
| Decision points | 1 | 2 | A lacks who approves payment recall |
| Evidence first | 2 | 1 | B omits preserving message headers before deleting |
| Actionability | 0 | 2 | A says "contain the account" without steps |
| Communications | 2 | 1 | A includes bank and supplier contact; B only internal |
| Closure | 1 | 1 | both vague |
| Fit | 0 | 2 | A references tools Fernmoor lacks |
| Total | 7 | 11 | |

Walkthrough: team using B reached the first containment decision in 12 minutes versus 31 with A, but forgot to contact the bank about recalling the payment — the most time-critical step in real BEC cases. Recommendation: adopt B, import A's evidence-preservation step and its bank/supplier communications section, and add measurable closure conditions (payment recall status, mailbox rules removed, supplier notified, verification of supplier's legitimate contact).

### 24.5 Common errors and limits

- Picking the longer playbook because it looks thorough.
- Testing two playbooks on the same team back-to-back without noting learning effects.
- Treating total scores as precise; read the criterion-level gaps.
- Playbooks that duplicate runbook detail and go stale.

### Exercises — chapter 24

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX070 — Scoring reasons.** *Steps:* write one-sentence reasons for B's scores on evidence-first and communications. *Rubric:* 3 = specific, refer to text omissions; 2 = generic; 1 = score only; 0 = none.

**EX071 — Closure conditions.** *Steps:* write five measurable closure conditions for the merged BEC playbook. *Rubric:* 3 = five measurable (recall outcome recorded, rules removed and verified, sessions revoked, supplier contacted via verified channel, finance procedure change logged); 2 = three; 1 = vague; 0 = none.

**EX072 — Test design.** *Steps:* design a fairer comparison than §24.4's. *Rubric:* 3 = two comparable teams or counterbalanced order, same inject, measures defined in advance, observer, noted limits; 2 = partial; 1 = vague; 0 = none.

### Chapter synthesis

Compare playbooks with explicit criteria, scored with reasons, and test them by walkthrough on the same inject. Combine the strengths of each into a short, actionable playbook with measurable closure conditions.

<!-- cyberabc:chapter-navigation:start ch-24 -->
### Continue studying — chapter 24 of 30

[← Chapter 23](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 →](#ch-25)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-25"></a>

## Chapter 25 — Team studio: build and critique a response workflow

### Learning outcomes and connection

You will be able to (1) build, as a team, an end-to-end response workflow for one scenario from intake to closure; (2) critique another team's workflow with a structured protocol; and (3) revise your workflow based on critique and evidence. Chapter 24 compared existing playbooks; in this studio you design one and expose it to peers.

### 25.1 Studio brief

Each team receives a Fernmoor scenario (for example "compromised supplier account uploads a malicious file to the permits portal") and must produce: a swimlane diagram (roles across the top, steps down), the case states it passes through, decision points with owners and authority, the runbooks invoked (existing or new), evidence preserved at each step, communications, and closure conditions. Deliverables must use the Chapter 4 data model and the Chapter 10 charter; deviations must be justified.

### 25.2 Critique protocol

A structured critique keeps feedback useful and humane. Fernmoor's protocol, adapted from design-studio practice: (1) the presenting team walks through the workflow for eight minutes without interruption; (2) reviewers ask clarifying questions only; (3) reviewers give feedback in three labelled forms — *"I like…"* (specific strength), *"I wonder…"* (open question), *"What if…"* (alternative); (4) a reviewer runs one inject through the workflow aloud, and everyone notes where it stalls; (5) the presenting team summarizes what they will change and what they will keep, with reasons. Critique addresses the workflow, not the people.

### 25.3 Evidence in critique

Opinions are useful, but evidence is better. Where possible, support a critique with data from earlier chapters: "Our detection register shows supplier-account alerts are rare (Chapter 19); your workflow depends on an alert that does not exist." "Chapter 18's test showed isolating a VM takes 6 minutes; your step assumes 1."

### 25.4 Worked example (synthetic): the supplier upload workflow

*Fictional.* Team Heron's workflow: intake from a malware detection on the portal file store → duty analyst triage → incident lead → disable supplier account → remove file → notify supplier → close.

Critique highlights:
- *I like:* the explicit decision to disable the supplier account with the portal owner's approval recorded.
- *I wonder:* whether any residents downloaded the file before removal — the workflow never asks.
- *What if:* the supplier account was not compromised but the supplier's own system was? Disabling the account would not tell you.
- Inject run: "Supplier says nobody at their company uploaded anything." The workflow stalled — no step for coordinated investigation with the supplier, and no contract contact list.

Revision: added steps "preserve the file and portal access logs before removal" and "query portal logs for downloads; if any, escalate to S2 and assess resident notification with privacy officer"; added a supplier coordination runbook referencing the contract's security clause and a verified contact list; closure now requires "download exposure determined". The team recorded which feedback they declined (a suggestion to block all supplier uploads permanently) and why (the business depends on them; compensating control: malware scanning before publication).

### 25.5 Common errors and limits

- Workflows that end at containment and forget recovery, communication and review.
- Critique that becomes personal or vague ("feels complicated").
- Accepting all feedback without reasoning, producing a bloated workflow.
- No inject run, so stalls stay hidden.

### Exercises — chapter 25

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX073 — Swimlane.** *Steps:* draw (or tabulate) the revised Heron workflow with roles as lanes. *Rubric:* 3 = duty analyst, incident lead, portal owner, privacy officer, supplier liaison lanes with ordered steps, decisions and evidence points; 2 = missing a lane; 1 = linear list; 0 = none.

**EX074 — Critique.** *Steps:* write two "I like", two "I wonder" and two "What if" items on the revised workflow. *Rubric:* 3 = specific, workflow-focused, at least one evidence-supported; 2 = generic; 1 = personal or vague; 0 = none.

**EX075 — Declined feedback.** *Steps:* write the record for declining one critique. *Rubric:* 3 = feedback, decision, reason, compensating control, review date; 2 = missing control; 1 = dismissal; 0 = none.

### Chapter synthesis

Design workflows end to end with roles, states, decisions, evidence and closure; critique them with a structured, evidence-supported protocol and live injects; and record both accepted and declined feedback with reasons.

<!-- cyberabc:chapter-navigation:start ch-25 -->
### Continue studying — chapter 25 of 30

[← Chapter 24](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 →](#ch-26)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-26"></a>

## Chapter 26 — Operational handoff and communications practice

### Learning outcomes and connection

You will be able to (1) perform shift and ownership handoffs that lose nothing; (2) write status updates for different audiences at a set cadence; and (3) coordinate communication with residents, suppliers and authorities through the people authorized to speak. Chapter 25 designed workflows; many fail at the seams — between shifts, teams and audiences.

### 26.1 Handoffs

Information is lost at handoffs. A structured handoff covers: case summary and current severity; scope and what is known/unknown; actions in progress with owners and expected completion; pending decisions and who owns them; risks and things to watch; next update times; and the explicit acceptance of ownership by the incoming person. Healthcare's SBAR (situation, background, assessment, recommendation) is a well-known structure that adapts well. The handoff is written in the case and spoken live; the incoming lead reads back key points.

### 26.2 Status updates

Set a cadence by severity (S1: every 60 minutes internally; S2: twice daily) and keep it even when there is "nothing new" — silence breeds rumour. Tailor to audience: technical responders need indicators and tasks; service owners need impact and expected restoration; executives need facts, decisions required, risks and next update; the service desk needs what to tell callers. Every update separates **facts**, **current assessment** and **next steps**, and gives the time of the next update. The Google SRE book's incident management chapter recommends a living incident document and regular updates for the same reasons.

### 26.3 External communication

Residents, media, regulators, suppliers and law enforcement are contacted only by people the charter authorizes, with the communications office, counsel and privacy officer as required. Technologists supply accurate facts and review drafts for technical correctness. Regulatory deadlines (for example the GDPR's 72-hour notification to the supervisory authority where feasible) are tracked in the case from the recorded awareness time; the determination belongs to the privacy officer and counsel.

### 26.4 Worked example (synthetic): night-to-day handoff for FCS-260

*Fictional.* At 07:00 the night lead hands FCS-260 (ransomware on `fs-01`) to the day lead.

*Situation:* S1; billing file processing down since 06:10 yesterday; `fs-01` isolated; `fs-02` clean by scan. *Background:* initial access likely a shared admin credential (assessment, moderate confidence); credential rotated 23:40. *Assessment:* restore of billing share from immutable copy 60% complete, ETA 10:00; unknown whether files were copied out — egress logs under review by R. Lin, due 09:00. *Recommendation / pending decisions:* director to decide at 09:30 whether to inform residents of billing delay (draft ready with communications); privacy officer awaiting egress result for notification assessment; awareness time recorded 08:20 yesterday. *Watch:* any sign-in by old admin credential (alert R-31 active). *Next updates:* executive 09:30, service desk 08:00.

Day lead read back the pending decisions and accepted ownership at 07:12; the case shows both names and the time.

### 26.5 Common errors and limits

- Handoffs by chat message without acceptance.
- Updates that mix facts and speculation.
- Technologists speaking to media or residents directly.
- Missing the start of a regulatory clock because awareness time was not recorded.

### Exercises — chapter 26

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX076 — Handoff note.** *Steps:* write an SBAR handoff for FCS-214 at end of day. *Rubric:* 3 = all four parts, open actions with owners, pending decisions, watch items, explicit acceptance; 2 = missing acceptance; 1 = narrative; 0 = none.

**EX077 — Three audiences.** *Steps:* write 50-word updates on FCS-260 at 09:30 for the executive, the service desk and the technical team. *Rubric:* 3 = each tailored with facts/assessment/next and next-update time; 2 = two tailored; 1 = same text; 0 = none.

**EX078 — Clock tracking.** *Steps:* define the case fields needed to track external notification deadlines. *Rubric:* 3 = awareness time and who recorded, applicable regimes (determined by privacy/counsel), deadline per regime, owner, status, sent time and reference; 2 = missing owner; 1 = one field; 0 = none.

### Chapter synthesis

Make handoffs structured, written, spoken and accepted; keep a steady update cadence tailored to each audience with facts separated from assessment; and leave external communication to authorized people while you supply accurate facts and track deadlines from a recorded awareness time.

<!-- cyberabc:chapter-navigation:start ch-26 -->
### Continue studying — chapter 26 of 30

[← Chapter 25](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 →](#ch-27)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-27"></a>

## Chapter 27 — Deploy and validate an incident case workflow

### Learning outcomes and connection

You will be able to (1) implement the case workflow as a state model with transition rules in the case tool; (2) validate it with automated tests before deployment; and (3) deploy it with training, a pilot and a rollback plan. Chapters 4, 17, 20 and 25 produced the data model, tool, checks and workflow design; now they go live.

### 27.1 The state model

Fernmoor's case states: `new → triage → investigating → containing → recovering → review → closed`, with `closed-benign` reachable from triage or investigating. Transition rules enforce the process: entering `containing` requires a recorded approval; `closed-benign` requires a triage note; `closed` requires a review record. Disallowed transitions (for example `triage → containing` without investigation, or `containing → closed` without recovery and review) are blocked or require an override with justification that is logged.

### 27.2 Validating before deployment

Write tests: sequences of transitions with expected acceptance or rejection. Run them against a model of the rules and then against the configured tool in a test instance. This is the same discipline as testing a parser on known input (Chapter 3).

### 27.3 Lab T-27 (synthetic): transition tests

```python
# Lab T-27: validate an incident case workflow against its state model
ALLOWED = {"new":{"triage"}, "triage":{"closed-benign","investigating"},
           "investigating":{"containing","closed-benign"}, "containing":{"recovering"},
           "recovering":{"review"}, "review":{"closed"}, "closed-benign":set(), "closed":set()}
REQUIRES = {"containing":"approval", "closed":"review_record", "closed-benign":"triage_note"}
def check(case, steps):
    s="new"; errors=[]
    for to,fields in steps:
        if to not in ALLOWED[s]: errors.append(f"{s}->{to} not allowed")
        need=REQUIRES.get(to)
        if need and need not in fields: errors.append(f"{to} lacks {need}")
        s=to
    print(case, "OK" if not errors else "; ".join(errors), "| final:", s)
check("T1",[("triage",set()),("investigating",set()),("containing",{"approval"}),
            ("recovering",set()),("review",set()),("closed",{"review_record"})])
check("T2",[("triage",set()),("closed-benign",{"triage_note"})])
check("T3",[("triage",set()),("containing",set())])
check("T4",[("triage",set()),("investigating",set()),("containing",{"approval"}),("closed",set())])
```

Expected output:

```text
T1 OK | final: closed
T2 OK | final: closed-benign
T3 triage->containing not allowed; containing lacks approval | final: containing
T4 containing->closed not allowed; closed lacks review_record | final: closed
```

T1 is a full S2 lifecycle and passes. T2 is a benign close and passes. T3 jumps from triage to containment without approval and fails on both rules. T4 skips recovery and review and closes without a review record — two violations. When the same tests were run against the configured tool in the test instance, T4 was *accepted* — the tool's rule for `closed` checked only the review field's presence, not the state order. The configuration was corrected and all four tests re-run; this is why tests run against the real configuration, not only the model.

### 27.4 Deployment

Plan: train all duty analysts and leads with a one-hour walkthrough and two practice cases in the test instance; pilot with one team for four weeks; measure record completeness (Chapter 20 checks) and analyst feedback; fix issues; then roll out. Rollback: keep the previous workflow configuration exportable and a documented switch-back procedure; open cases at the time of rollback are mapped state by state. Emergency override: the incident lead may force a transition with a justification; every override is reviewed weekly.

### 27.5 Worked example (synthetic): pilot results

*Fictional.* Four-week pilot with the Response Desk (23 cases): record completeness improved from 71% (previous quarter, same checks) to 96%; two overrides, both justified (a case reopened after closure; a duplicate merged). Analysts reported that the approval field was slow on mobile; it was made a one-tap selection from the on-call approver list. One defect: a case in `recovering` could not link a new IT change; fixed before rollout. Because the comparison is with a previous quarter and the team knew it was being observed, part of the improvement may not persist; completeness continues to be measured monthly.

### 27.6 Common errors and limits

- Rules so strict that analysts work outside the tool.
- Testing only the model, not the tool configuration.
- Deploying without training or a rollback.
- Before/after comparisons presented as proof without caveats.

### Exercises — chapter 27

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX079 — New test.** *Steps:* write two more test sequences for the lab — one valid path through `closed-benign` from investigating, one invalid reopen from `closed`. Predict output. *Rubric:* 3 = sequences and correct predicted output (OK; "closed->investigating not allowed"); 2 = one; 1 = attempted; 0 = none.

**EX080 — Override policy.** *Steps:* write the override rule. *Rubric:* 3 = who may override, justification required, logged, weekly review, reporting of override rate; 2 = no review; 1 = vague; 0 = none.

**EX081 — Rollback plan.** *Steps:* write a rollback plan for the workflow deployment. *Rubric:* 3 = trigger criteria, decision owner, configuration restore, open-case mapping, communication, verification; 2 = missing mapping; 1 = vague; 0 = none.

### Chapter synthesis

Implement the workflow as a state model with enforced transitions, test it against the real configuration with known sequences, deploy with training, pilot, measured results and a rollback, and govern overrides openly.

<!-- cyberabc:chapter-navigation:start ch-27 -->
### Continue studying — chapter 27 of 30

[← Chapter 26](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 →](#ch-28)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-28"></a>

## Chapter 28 — Field simulation with authorized stakeholders

### Learning outcomes and connection

You will be able to (1) plan a field simulation (functional exercise) with written authorization, safety controls and clear objectives; (2) run it with real stakeholders and real tools in a controlled way; and (3) evaluate performance against objectives and turn findings into owned improvements. Chapter 27 deployed the workflow; a simulation tests whether people, tools and processes work together under realistic pressure.

### 28.1 Exercise types

NIST SP 800-84 distinguishes tabletop exercises (discussion), functional exercises (performing tasks in a simulated operational environment) and full-scale exercises. A **field simulation** in this course is a functional exercise: staff use the real case tool, paging, evidence store and pre-built containment actions against test systems, while injects are delivered by an exercise control team.

### 28.2 Authorization and safety

Before anything runs: written authorization from the system owners and the director, stating scope (which systems, test accounts and hours), excluded systems, who may stop the exercise, and how real incidents are handled during it. Safety controls: every inject and message labelled "EXERCISE"; actions only against test systems or test accounts; a "real-world" code phrase that halts play; the service desk and on-call managers briefed; no surprise for residents. The Menlo Report's principles — respect for persons, beneficence, justice, respect for law and public interest — are a useful check that an exercise does not harm or deceive people.

### 28.3 Design

Objectives tied to capabilities (for example "page S1 on-call within 15 minutes"; "preserve identity evidence before containment"; "deliver an executive update within 60 minutes"); a scenario with a master scenario event list (injects with times, deliverer and expected actions); roles (players, controllers, evaluators, observers); evaluation guides per objective; and a hot wash immediately afterwards plus a written after-action report.

### 28.4 Worked example (synthetic): "Quiet Meter"

*Fictional.* Scenario: a compromised supplier account accesses the water-billing test environment. Authorization signed by the billing system owner and director; scope: `billing-test` environment and five test accounts; 09:00–13:00 on a Tuesday.

| Objective | Measure | Result | Finding |
|---|---|---|---|
| Page S2 on-call ≤ 15 min after alert | case timestamps | 9 min | met |
| Preserve IdP evidence before containment | case record order | not met — sessions revoked before export | runbook step order unclear on mobile |
| Disable supplier account via action card ≤ 10 min | console log | 7 min | met |
| Executive update ≤ 60 min with facts/assessment/next | evaluator check | 72 min; mixed speculation | template not used |
| Supplier contact via verified channel | inject response | used email from the alert | contract contact list not in case tool |

Improvement plan: reorder the identity runbook with an enforced "export complete" checkbox (owner Response Desk, 2 weeks); add the update template to the case tool (ITSM owner, 1 month); load supplier contacts from contracts into the inventory (Procurement, 6 weeks); re-test objectives 2, 4 and 5 in the next quarter's exercise.

### 28.5 Common errors and limits

- Exercising without written authorization or a stop mechanism.
- Objectives that cannot be observed.
- Blaming individuals in the after-action report.
- Findings without owners and re-test dates.

### Exercises — chapter 28

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX082 — Authorization letter.** *Steps:* draft the authorization for "Quiet Meter". *Rubric:* 3 = scope, exclusions, dates/times, test accounts, stop authority and code phrase, real-incident handling, signatories; 2 = missing stop; 1 = vague; 0 = none.

**EX083 — Inject list.** *Steps:* write five injects with time, deliverer, content and expected action. *Rubric:* 3 = five coherent injects testing the objectives; 2 = three; 1 = unrelated; 0 = none.

**EX084 — Finding write-up.** *Steps:* write the after-action entry for objective 2 without blaming individuals. *Rubric:* 3 = observation, impact, root cause in process/tool, recommendation, owner, re-test; 2 = missing re-test; 1 = blames; 0 = none.

### Chapter synthesis

Exercise for real only with written authorization, labelled injects, a stop mechanism and limited scope; design observable objectives; evaluate without blame; and turn each finding into an owned change with a re-test date.

<!-- cyberabc:chapter-navigation:start ch-28 -->
### Continue studying — chapter 28 of 30

[← Chapter 27](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 →](#ch-29)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-29"></a>

## Chapter 29 — Capstone: integrated response and recovery service

### Learning outcomes and connection

You will be able to (1) integrate the components built across this course into a running response and recovery service for Fernmoor; (2) demonstrate it end to end against acceptance criteria with operational evidence; and (3) document it so that another team can operate it. This capstone draws on every chapter; Chapter 30 evaluates it.

### 29.1 Capstone scope

The integrated service must include: charter and roles (Ch10); inventory with dependencies and tiers (Ch11); verified evidence flows with canaries (Ch12); severity scale and triage thresholds (Ch13); intake channels (Ch14); case tool and evidence store meeting acceptance criteria (Ch17); tested containment and recovery actions with timed restores (Ch18); detection register with outcome labels (Ch19); consistency checks (Ch20); ITSM integration and emergency change (Ch21); automations with run logs (Ch22); measures and monthly review (Ch9, Ch23); playbooks for at least three scenarios (Ch24–25); handoff and communication templates (Ch26); deployed workflow (Ch27); and an exercise programme (Ch28).

### 29.2 Acceptance criteria

Each component needs a criterion that can be demonstrated with evidence, not a statement. Examples: "Canary events for all four flows appear within their stated delay for 14 consecutive days (query output attached)"; "Each pre-built containment action has a test record within 90 days"; "Restore of tier-1 systems meets RTO and RPO in the latest test (test report)"; "Workflow tests T1–T6 pass against the production configuration (test log)". The CSF 2.0 Profile approach — comparing current with target outcomes — gives a structure for presenting coverage.

### 29.3 End-to-end demonstration

Run one realistic synthetic case through the whole service in the test environment, from detection to post-incident review, while an assessor observes. Collect the operational evidence the service produces: case record with history, evidence manifest with verification, change records, run logs, updates and the review. The demonstration should also include one deliberate failure (for example, a canary flow disabled) to show monitoring catches it.

### 29.4 Worked example (synthetic): Fernmoor capstone excerpt

*Fictional.* Demonstration case "invoice fraud via compromised supplier mailbox" in the test environment.

| Component | Criterion | Evidence | Result |
|---|---|---|---|
| Evidence flows | 4/4 canaries within delay for 14 days | scheduled query export | pass |
| Containment actions | 6/6 tested in 90 days | action test log | 5/6 — DNS sinkhole test 120 days old; retested during capstone, pass |
| Recovery | billing-db RTO 2 h / RPO 15 min | restore report | RTO 1 h 40, RPO 10 min — pass |
| Workflow | T1–T6 pass on production config | test log | pass |
| Automation | evidence manifest verified, run logged | run log, manifest | pass |
| Deliberate failure | disabled identity canary alerts in ≤ 30 min | alert record | alerted at 22 min — pass |
| Handoff | SBAR with acceptance | case history | pass |
| Communications | executive update template used | case record | pass; one speculative phrase flagged |

Operating documentation: a service handbook (one page per component, owner, how to operate, how to test), a runbook index and a calendar of recurring tests.

### 29.5 Common errors and limits

- Acceptance by assertion ("flows are configured") instead of evidence.
- Demonstrating only the happy path.
- Documentation that only the builder understands.
- Treating a test environment demonstration as proof of production behaviour without production tests.

### Exercises — chapter 29

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX085 — Criteria.** *Steps:* write evidence-based acceptance criteria for four components not in the §29.4 table (inventory, triage thresholds, ITSM routing, exercise programme). *Rubric:* 3 = four measurable criteria with evidence artefacts; 2 = three; 1 = assertions; 0 = none.

**EX086 — Handbook page.** *Steps:* write the handbook page for the evidence store. *Rubric:* 3 = purpose, owner, how to use, controls, recurring tests, failure handling, links; 2 = missing tests; 1 = vague; 0 = none.

**EX087 — Deliberate failures.** *Steps:* propose three more deliberate failures for the demonstration and what should detect each. *Rubric:* 3 = three realistic failures with detecting control and expected time; 2 = two; 1 = vague; 0 = none.

### Chapter synthesis

Integrate every built component into one service with evidence-based acceptance criteria, demonstrate it end to end including deliberate failures, and document it so another team can operate and test it.

<!-- cyberabc:chapter-navigation:start ch-29 -->
### Continue studying — chapter 29 of 30

[← Chapter 28](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 →](#ch-30)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-30"></a>

## Chapter 30 — Capstone evaluation and improvement dossier

### Learning outcomes and connection

You will be able to (1) evaluate the capstone service against its criteria and measures honestly; (2) prioritize improvements with owners, effort and expected effect; and (3) assemble an improvement dossier that hands the service into steady operation. This final chapter closes the course and the service's first build cycle.

### 30.1 Evaluation

Combine three kinds of evidence: **acceptance results** (Chapter 29), **service measures** over a period (time to triage, stage latencies, record completeness, detection outcome labels — Chapters 9, 19, 20, 23) and **exercise findings** (Chapter 28). For each component, state: met / partly met / not met, the evidence, and confidence (how much data, how representative). Report limitations: small case counts, test-environment demonstrations, observer effects.

### 30.2 Prioritization

List improvement items from all sources. For each: problem with evidence, proposed change, owner, effort (S/M/L), expected effect on a named measure, and dependencies. Prioritize with a simple, explicit rule — for example, first items that protect recovery or evidence integrity, then items with large expected effect and small effort. NIST SP 800-61 Rev. 3 emphasizes that lessons learned feed improvement across all CSF functions; the dossier is that feedback made concrete.

### 30.3 Sustaining the service

A response service decays without maintenance: owners move, flows break, playbooks go stale. Build a sustainment calendar (monthly measures and checks, quarterly action tests and restore tests, semi-annual exercises, annual charter review), ownership for every component, and a backlog process. Blameless post-incident reviews (as in the SRE book's postmortem culture and Dekker's just culture) keep people reporting problems.

### 30.4 Worked example (synthetic): Fernmoor's first-year dossier

*Fictional.* Excerpt of the evaluation:

| Area | Status | Evidence | Confidence |
|---|---|---|---|
| Evidence flows | met | 14-day canaries; one flow outage detected in 22 min | high |
| Triage latency | partly met | median 11 min; out-of-hours p90 41 min vs 30 target (n = 19) | moderate (small n) |
| Decision records | met | completeness 96% (pilot) → 94% (quarter) | moderate |
| Recovery | partly met | billing-db met; permits file share restore untested | high for tested, none for untested |
| Supplier coordination | not met | exercise objective 5 failed; contacts not loaded | high |

Top improvements (priority order): (1) restore test for permits share — protects recovery; owner Infrastructure; S; measure: tested RTO/RPO. (2) load supplier contacts into inventory — owner Procurement; M; measure: exercise objective 5. (3) second on-call for out-of-hours peaks — owner IT director; M; measure: out-of-hours p90 ≤ 30 min over two quarters. (4) phishing-resistant authenticators for staff with resident-data access — owner Identity; L; measure: share of such staff with security keys, and identity-case count.

The dossier closes with the sustainment calendar, the owner list, open risks formally accepted by the director (OT scope still excluded; referral procedure in place), and a list of what the evaluation could not show.

### 30.5 Common errors and limits

- Reporting only successes.
- Improvements without measures, so no one knows whether they worked.
- No sustainment plan; the service degrades within a year.
- Confidence claims that ignore small samples.

### Exercises — chapter 30

Attempt each exercise before opening the [worked results](#worked-results). Every case, organization, person, address and number in an exercise is synthetic unless a cited public source is named.

**EX088 — Evaluation row.** *Steps:* write an evaluation row for "detection register" using Chapter 19 data. *Rubric:* 3 = status, evidence with figures, confidence with reason, limitation; 2 = missing confidence; 1 = assertion; 0 = none.

**EX089 — Prioritize.** *Steps:* rank five improvement items (permits restore test; supplier contacts; second on-call; security keys; mobile runbook fix) with your rule and justify. *Rubric:* 3 = explicit rule applied consistently with effort/effect; 2 = ranking with partial reasons; 1 = list; 0 = none.

**EX090 — Sustainment calendar.** *Steps:* write a twelve-month sustainment calendar. *Rubric:* 3 = monthly, quarterly, semi-annual and annual activities with owners covering measures, checks, action/restore tests, exercises, charter and inventory review; 2 = missing owners; 1 = partial; 0 = none.

### Chapter synthesis

Evaluate the service with acceptance results, measures and exercise findings, stating confidence and limits; prioritize improvements by an explicit rule with owners and measures; and hand over a sustainment calendar so the service keeps working after the course ends.

<!-- cyberabc:chapter-navigation:start ch-30 -->
### Continue studying — chapter 30 of 30

[← Chapter 29](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

This is the final chapter of this course; the index links the next course in the full study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

Each worked result shows one defensible answer. Implementation exercises often admit several good answers; full credit goes to answers that meet the same standard of precision, testability, ownership and honesty about limits. Lab outputs were produced with Python 3 and the standard library. Fernmoor City Services and all cases, people and numbers are synthetic unless a cited source is named.

### Chapter 1: EX001–EX003

**EX001.** | Component | Role | Owner | Logs | Restore | — `appt-app-1..3` | application | Platform | local, 7 days (gap) | rebuild from image | `appt-lb` | load balancing | **none (gap)** | unknown (gap) | config export? (gap) | `appt-db-1` | primary DB | Data Platform | DB logs local | nightly backup, untimed (gap) | replica | read scale | Data Platform | DB logs | promote | object store | backups | Data Platform | provider access logs (check enabled) | provider versioning | IdP | sign-in | Identity | central | provider-managed. Gaps are part of the answer.

**EX002.** (1) `svc-patch` across all hosts — intrusion spread. (2) The single load balancer — containment impact (blocking at the LB stops all users) and availability. (3) Backups in the same administrative domain as production — recovery: an attacker with admin rights could delete them. Accept the shared hypervisor or region if justified.

**EX003.** "To: Network lead. During an incident we may need to block or redirect traffic at `appt-lb` at any hour. Please name an owner and an out-of-hours deputy, their contact route (rota or phone bridge), and confirm they hold emergency change authority under the change policy. We need this by 30 April to complete the response contact list."

### Chapter 2: EX004–EX006

**EX004.** DNS resolver — query log — check days kept — sinkhole or remove record. Edge — access log — often hours to days, export — rate-limit, block path or range. Firewall — connection log — days to weeks — segment or deny rule. Application — request/app log — per config (Chapter 1 found 7 days local) — disable feature. Database — query/audit log if enabled — verify — revoke application role or make read-only.

**EX005.** (a) Rate limit: legitimate heavy users slowed; remove rule; seconds. (b) Range block: blocks every user behind that range, attacker may switch; delete rule; seconds to minutes. (c) Disable endpoint: public lookup unavailable, call-centre load rises; re-enable after fix; minutes plus change approval.

**EX006.** "Edge logs show about 41,000 requests in one hour from addresses in 203.0.113.0/24 to sequential permit ids, 98% successful. The responses served included applicant phone numbers. The logs do not identify who controlled those addresses or why, and do not show anything beyond the logged request fields."

### Chapter 3: EX007–EX009

**EX007.**
```text
import csv, sys
from collections import Counter, defaultdict
fails = Counter(); srcs = defaultdict(set); skipped = 0
with open(sys.argv[1], newline="", encoding="utf-8") as f:   # read-only
    for row in csv.DictReader(f):
        if not row.get("user") or not row.get("result"):
            skipped += 1; continue
        if row["result"] == "failure":
            fails[row["user"]] += 1; srcs[row["user"]].add(row["src"])
for user, n in sorted(fails.items(), key=lambda x: (-x[1], x[0])):
    if n > 5: print(user, n, len(srcs[user]))
print("skipped", skipped)
```

**EX008.** Rows: six failures for `a` from two sources (one source repeated), five failures for `b` (at threshold, not reported), one success for `a`, one row with empty user, header. Expected: `a 6 2` then `skipped 1`.

**EX009.** "2026-04-14T10:22Z (UTC), operator J. Okafor (synthetic). Ran `count_failures.py` (SHA-256 3f1a…, repo commit 8c2d…) on `idp_signins_0413.csv` (SHA-256 91b0…, read-only copy). Result: 1 account over threshold (`water-billing-2`, 37 failures, 29 sources). Skipped rows: 0. Output saved as `FCS-118/derived/failures.txt`."

### Chapter 4: EX010–EX012

**EX010.** `case_id` string req; `title` string req; `status` enum req (new, triage, investigating, containing, recovering, review, closed, closed-benign — see Chapter 27); `severity` enum S1–S4 req at triage; `owner` person id req; `opened_utc`, `updated_utc` RFC 3339 req; `services` list of asset ids; `reporter` string; `closure_reason` enum req when closed; links: `events`, `actions`, `decisions`, `artefacts`.

**EX011.** `createdDateTime` → `time_utc` (already UTC; keep original); `userId` → `actor_id`; `ipAddress` → stored as attribute `src`; `status.errorCode` → `outcome` = success if 0, else failure; `action` = signin; `source` = idp; entire JSON → `raw`.

**EX012.** One person's interpretation of ambiguous labels is a source of error; two independent coders reveal ambiguity. Report percent agreement (62 of 64, 97%) and how the two disagreements were resolved; keep both original and final codes.

### Chapter 5: EX013–EX015

**EX013.** Failed sign-in — event. Firewall deny — event (working control). Phishing SMS impersonating Fernmoor — incident affecting residents and brand; open a case (fraud against residents, possible takedown work). Ransomware note — incident, high severity. Rule on known admin script — alert, likely benign after verification; tune the rule.

**EX014.** Valid accounts — IdP sign-in logs; MFA and conditional access. Adding an MFA method — IdP audit log; alert on method changes and require re-verification. Bulk file reads — file-server audit log; least-privilege share permissions and volume alerts.

**EX015.** Asset inventory — Identify. Phishing-resistant MFA — Protect. Alert rules and triage — Detect. Isolating a host — Respond. Timed restore test — Recover. Govern accepts the policy and roles (Chapter 10).

### Chapter 6: EX016–EX018

**EX016.** Linux: crontabs (user and system), systemd units and timers, shell profile files, `authorized_keys`, init scripts or `rc.local`. Windows: Run/RunOnce registry keys, scheduled tasks, services, startup folders, WMI event subscriptions.

**EX017.** Memory first (most volatile, holds process and key material), then process list and network connections (change within seconds), then firewall/host configuration, then disk image (persists). If the memory tool would heavily alter state, record that choice.

**EX018.** (1) Reverting to a snapshot overwrites post-snapshot changes — restrict revert rights during a case and note snapshots in the case. (2) A snapshot stored in the same platform could be deleted or altered by an attacker with platform rights — export to the separate evidence store and hash immediately.

### Chapter 7: EX019–EX021

**EX019.** Export logs (preserve before change) → revoke sessions and tokens (cut current access) → remove new MFA method (prevent re-authentication) → reset password with verified identity → check forwarding/mailbox rules (preserve then remove). Checking rules before reset is also acceptable if preserved; the key error is resetting first and leaving tokens.

**EX020.** On which hosts and pipelines is it used? What privileges does it hold versus what it needs? When was its credential last rotated, and where is it stored? From which sources does it sign in, and are there sign-ins outside the automation hosts or schedule?

**EX021.** "Hi Ana, overnight someone who had your password triggered a sign-in prompt, and it was approved. We have removed their access, reset your password and removed a forwarding rule they created. You did nothing unusual — these prompts are designed to be tapped. Please report any unexpected prompt to the Service Desk. Thanks, Response Desk."

### Chapter 8: EX022–EX024

**EX022.** Internet → web front end; web → application server; application → database; administrator workstations → servers; Fernmoor SFTP → payment supplier (and supplier → Fernmoor if two-way).

**EX023.** DB audit: run a test export query and find it in central logs within 5 minutes. VLAN: from the billing VLAN, connections to HR hosts fail and approved flows succeed. Backups: daily admin credential cannot delete or modify the immutable copy (test with a dummy file). Jump host: direct RDP from a laptop to the DB server fails; a session via jump host requires MFA and appears in session logs.

**EX024.** 1. Backup separation — protects recovery from the worst case, moderate effort. 2. DB audit and SFTP logs — needed to answer "what left?", low effort. 3. Jump host — reduces spread, moderate effort. 4. VLAN separation — valuable but needs application dependency analysis, higher effort. Other orders are acceptable with reasons.

### Chapter 9: EX025–EX027

**EX025.** Name: time to contain. Start: `decision_time` of the first approved containment decision; end: `action_time` of the containment action recorded as verified effective. Population: cases S1–S3 with a containment action in the period. Missing: count separately; never impute. Statistics: median and nearest-rank p90, with n. Target: S1 within 60 minutes of decision (rationale: limits spread observed in exercises). Owner: Response Desk lead.

**EX026.** FCS-105 adds 11 minutes. Sorted values: 6, 9, 11, 12, 14, 21, 70, 115; median (12+14)/2 = 13.0; nearest rank for p90 is round(7.2) = 7th value = 70.0; within 15 minutes: 6, 9, 11, 12, 14 = 5 of 8.

**EX027.** "Of eight cases, seven had a recorded triage time; the median was 14 minutes against a 15-minute target, but only four of seven met it. Both slow cases (115 and 70 minutes) began out of hours. One case lacks a triage time, which we are correcting. Eight cases are too few to show a trend; we propose testing on-call paging next quarter."

### Chapter 10: EX028–EX030

**EX028.** Duty analyst: disable user account; revoke sessions; isolate one workstation; block one external IP at edge. System owner: isolate a server; disable a public feature; restore from backup. Director (with counsel/privacy): external notification to regulators or residents; engaging an external response firm under contract. Reasons: reversibility and business impact rise down the list.

**EX029.** "The incident lead owns one S1–S2 case end to end: sets objectives, assigns tasks, approves actions within the charter, keeps the decision log, sets the update cadence and escalates when actions exceed authority, when personal data may be involved, or when the case exceeds four hours without containment. In S1 the lead coordinates and does not perform hands-on changes. At shift end the lead performs a recorded handoff (Chapter 26)."

**EX030.** A defensible answer: not in year one as a full service, because OT incidents involve physical safety, different protocols and vendor constraints the team cannot yet support; instead define a referral and joint-case procedure with the OT team, share IT-side evidence, and plan an OT extension after training. Accept inclusion if staffing and safety governance are addressed.

### Chapter 11: EX031–EX033

**EX031.** Agent-only: real host without CMDB record — assign owner, add record. CMDB-only: decommissioned or agent missing — verify; either retire record or install agent. Untagged cloud VM: unknown owner and purpose — identify creator from cloud audit log, tag or remove under change control. Scan-only host: shadow IT or unmanaged device — investigate as potential risk; onboard or remove.

**EX032.** DNS → needed by all five; `billing-db`, `appt-db-1`, `permit-app-1`, `intranet-wiki` → `idp-proxy`; `permit-app-1` → permits DB. `idp-proxy` and DNS inherit tier 1.

**EX033.** Business service supported; owner and on-call contact; criticality tier; environment (production/test); where its logs are and how long kept; how it is restored and expected restore time.

### Chapter 12: EX034–EX036

**EX034.** Source: Windows file servers' Security log (object access on sensitive shares). Fields: time, account, share, path, access type, source host. Delay: ≤5 min via forwarder. Retention: 400 days (exceeds typical detection delays; agreed with records officer). Immutability: central store in separate account with object lock. Access: response and audit roles; access logged. Canary: scheduled read of `canary.txt` by a test account every day; alert if absent within 15 minutes.

**EX035.** Identity: test account signs in at 06:00 daily to a test application; expected in store within 10 minutes. Cloud: automation changes a tag on `canary-bucket` hourly; expected within 30 minutes. A scheduled query checks for both; if absent, alert the log-platform on-call and open a ticket owned by Platform; the duty analyst is informed that evidence may be incomplete.

**EX036.** "Cloud audit logs show an access key created for `svc-reports` at 14:05 UTC from 198.51.100.40 and used for list operations. Object-read logging was not enabled on `permits-archive`, so we cannot determine whether objects were downloaded or which ones. The privacy assessment therefore treats the archive's contents as potentially accessed. Object-read logging has since been enabled for personal-data buckets."

### Chapter 13: EX037–EX039

**EX037.** Entry: phished credential or exposed remote access; lateral movement via shared admin account. Assets: `fs-01/02` (billing exports, permits archive), backups. Impact: billing and permits halted; possible data theft before encryption. Early evidence: unusual admin sign-ins, mass file renames, backup deletion attempts, egress spikes. Gaps: file-server audit logs not central (Chapter 12), no alert on backup deletion.

**EX038.** Laptop: S2 (possible personal-data exposure; escalate with privacy officer). DDoS 20 minutes: S3 (degradation, not tier-1 outage beyond objectives). Web shell: S2 (confirmed host compromise, tier-2). Spreadsheet to personal email: S2 (confirmed disclosure risk of personal data; privacy and HR). Billing DB encrypted: S1 (tier-1 unavailable).

**EX039.** Precision 3/240 ≈ 1.25%. Keep the detection because it found real S3 cases; add enrichment (asset tier, known-good sources) and raise the threshold to analyst queue rather than automatic case; re-measure after 30 days. Suppress entirely only if the three true positives would be caught by another rule.

### Chapter 14: EX040–EX042

**EX040.** Reporter name and contact; channel; verbatim observation; time observed; systems/accounts/domains mentioned; actions already taken; evidence available (keep original email, screenshot); harm suffered (payment, data entered); aware of other reports; agent name and consent to be contacted.

**EX041.** "Investigate the server" → "Determine whether `permit-app-2` was accessed without authorization from 1 May to now and whether it was used to reach the permits DB." "Check the account" → "Establish whether `hr-assist-5` sign-ins between 3 and 5 June were by the owner, and list data accessed." "Look into the outage" → "Identify the cause of appointments unavailability on 12 June 09:10–10:40 and whether it was malicious."

**EX042.** "2026-06-11T15:40Z. Old scope: phishing impersonating billing from 10 June. New scope adds: whether the billing export sent to PrintCo (synthetic supplier) on 2 June was exposed. Trigger: all three reporting residents' addresses appear in that export and in no other common list checked. Approved by incident lead M. Duarte. Severity S3 → S2; privacy officer informed."

### Chapter 15: EX043–EX045

**EX043.** With no zone correction the VPN session runs 09:03:02–09:41:30 UTC, about five hours before the IdP sign-in at 14:02:10 and ending before the file read at 14:11. It invites the false conclusion that someone used the VPN without the identity provider (suggesting a VPN bypass) and that the file read happened outside any VPN session — sending the investigation after a non-existent appliance vulnerability.

**EX044.** "Bound: 2026-05-11 14:00–15:00 UTC. Sources: IdP sign-in and audit (complete in window), VPN appliance (complete), file-server audit (complete from 14:00). Gaps: no endpoint telemetry from the clerk's laptop; no record of data leaving after the read; mailbox activity not yet examined. Conclusions about use of the 412 files and about who was at the keyboard remain open."

**EX045.** `2026-05-11T14:11:00Z | FS fs-02 | original 2026-05-11T14:12:35Z | −95 s skew measured 2026-05-12T09:00Z against NTP reference | bulk read 412 files on share permits-archive | actor permits-clerk-4 | asset fs-02 | evidence fs_audit_FCS-214.csv sha256 bdeae596… | note (interpretation): read occurs within the VPN session from 198.51.100.23.`

### Chapter 16: EX046–EX048

**EX046.** H1: sign-in from Fernmoor's usual address/device; file access matching a work ticket. H2: sign-in from unusual infrastructure also targeting other accounts; activity while clerk demonstrably elsewhere. H3: sign-in from a colleague's device or internal address; access to data unrelated to the clerk's duties but related to the insider's interests.

**EX047.** P1: IdP → key src=198.51.100.23 → IdP failures 30 days; query `src == 198.51.100.23 and result == failure`; 14 accounts, 9–10 May. P2: IdP → keys 14 account ids → IdP successes; query `user in list and result == success and src == 198.51.100.23`; `hr-assist-5` 10 May, legacy protocol. P3: IdP → key `hr-assist-5` → mailbox audit; query `user == hr-assist-5 and operation == New-InboxRule`; rule hiding service-desk mail.

**EX048.** Where were you between 13:30 and 15:30 on 11 May? Which devices did you have with you, and were any used? Did you receive any sign-in prompts that day; what did you do? Do you use the permits archive in your work; when last? Have you noticed anything unusual with your account recently?

### Chapter 17: EX049–EX051

**EX049.** Severity/status enumerations (Ch4, Ch13); required fields per status (Ch4); case links to events/artefacts/actions/decisions (Ch4); task owners and due times (Ch14); immutable history (Ch17); case-level access restriction (Ch16 interviews, HR cases); API for automation (Ch22); export for reports and measures (Ch9, Ch23).

**EX050.** E-0412 memory image `permit-app-2.mem`, collected 2026-06-02T03:14Z by J. Okafor with pre-approved tool v3.2, SHA-256 9c4e…; 03:31Z uploaded to evidence store `fcs-evidence/FCS-230/`, hash verified match; 2026-06-02T09:05Z accessed by R. Lin for analysis (working copy to analysis VM); 2026-06-09 verification run, hash match. Each line names the person and purpose.

**EX051.** "Risk: evidence-store access entries appear after up to 60 minutes instead of 5. Impact: delayed detection of misuse of evidence. Compensating control: evidence-store access restricted to five named responders; daily review of the access log by the Response Desk lead. Owner: Platform. Fix date: 30 July. Approved by IT security manager, 1 July."

### Chapter 18: EX052–EX054

**EX052.** Trigger: system owner approves (duty analyst may request). Steps: record VM id and current network; snapshot and export (Ch6); change NIC to `quarantine` segment via hypervisor console or automation; confirm. Side effects: service on that VM unavailable; dependent services may error. Verification: from VM, only evidence share reachable; from production, VM unreachable. Rollback: return NIC to original segment after release by incident lead. Test: quarterly on `test-vm-q`, last 2026-04-02, 6 minutes.

**EX053.** Target: isolated restore host in a separate network. Steps (each timed): retrieve latest backup; restore; apply logs to a chosen point; integrity checks — row counts by table vs backup manifest, checksums of customer and invoice tables, sample of ten invoices compared with the source; application connects in test mode. Compare measured RTO/RPO with tier-1 objectives (e.g., 2 h / 15 min). Record findings with owners and retest dates.

**EX054.** Key status shows disabled (then deleted after evidence preserved); a test call with the key returns access denied; principal has no other active keys; audit log shows no keys created after containment; resources, policies and users created by the key reviewed and removed if malicious; data-read logs checked for activity up to containment time.

### Chapter 19: EX055–EX057

**EX055.** R-07: 4/52 ≈ 7.7% true positives; 31 benign TPs mean the rule fires on real travel or VPN egress — enrichment with corporate egress and travel notices should reduce noise without losing detections. R-19: 1/120 ≈ 0.8%; dominated by the backup account; a narrow exclusion is justified, and the remaining FPs need review.

**EX056.** "Exclude account `svc-backup` reading from host `bk-01` on shares `fs-01\billing$` and `fs-02\permits$` between 01:00 and 03:00 local. Any read by `svc-backup` outside that window, from another host or on another share raises R-19b at S3. Review 30 September (owner: Response Desk)."

**EX057.** Rule: more than 500 rows exported from `billing-db` by a human account followed within 2 hours by an outbound email with an attachment to a non-Fernmoor domain from that account. Sources: DB audit (Ch8 change) and mail gateway logs. Runbook first step: preserve both records, do not contact the employee, inform the incident lead, who involves HR and the privacy officer before any interview.

### Chapter 20: EX058–EX060

**EX058.** (1) status ≥ triage requires severity and owner. (2) `opened ≤ triage_start ≤ first_decision ≤ first_action ≤ closed`. (3) status closed requires all tasks closed and `closure_reason`. (4) severity S1 requires an incident lead distinct from the duty analyst. (5) any external notification requires severity ≤ S2 or a recorded justification. (6) each containment action with `confirmed_at` must be matched by telemetry showing the effect within 15 minutes, else flag.

**EX059.** "Correction 2026-06-20T08:15Z by R. Lin. Field `actions[2].time`: old 10:02 UTC; new: requested 10:02, applied 10:41. Source: endpoint console isolation log entry 7733 (agent reconnected 10:41). Reason: automation recorded queue time. Scope note added for DNS activity 10:27."

**EX060.** (1) On-call analysts triage from phone where the field is hidden — test: compare missing rate for cases handled via mobile vs desktop. (2) Out-of-hours cases auto-escalate past triage status — test: inspect status transitions for those cases. (3) Analysts triage in chat and never update — test: compare chat timestamps with case updates for a sample.

### Chapter 21: EX061–EX063

**EX061.** (1) Keywords "ransom", "encrypted", "phishing", "hacked" in description → security triage queue, restricted, notify duty analyst. (2) Any ticket on a tier-1 asset in category "unauthorized access" → security case S2 provisional, page on-call. (3) Tickets from the contact centre tagged "scam using Fernmoor name" → security case S3. (4) Mass password-reset requests (>5 in an hour from one department) → security review.

**EX062.** "CHG-3301 (emergency). What: move `fs-01` network interface to quarantine segment. Why: contain linked security case FCS-260 (restricted). Risk: billing file processing unavailable until release. Rollback: return interface to production segment on incident-lead release. Approved: on-call infrastructure manager, 06:31. Executed 06:38, verified 06:41. Retrospective: change board 15 June."

**EX063.** INC-8812 closes when billing service is restored and the service owner accepts functional tests. FCS-260 closes only when scope questions are answered or declared undeterminable, eradication is verified, notifications are decided, residual risk is accepted by the owner and the post-incident review is complete; PRB-140 stays open until the shared credential is eliminated.

### Chapter 22: EX064–EX066

**EX064.** Enrich alert — automate. Hash artefacts — automate. Create IT incident link — automate. Page on-call — automate. Disable user — automate-with-approval (pre-approved for duty analyst; one-click after human decision). Isolate workstation — automate-with-approval. Email all staff — human (communications approval; risk of panic or error). Notify regulator — human (director with counsel and privacy officer).

**EX065.**
```text
cur = {n: hashlib.sha256(b).hexdigest() for n, b in items.items()}
changed = sorted(n for n in manifest if n in cur and cur[n] != manifest[n])
missing = sorted(n for n in manifest if n not in cur)
added   = sorted(n for n in cur if n not in manifest)
for n, h in sorted(manifest.items()): print(h, n)
print("changed", changed, "missing", missing, "added", added)
```
Test by adding `items["extra.txt"] = b"x"` and deleting one key; expect each list populated accordingly.

**EX066.** Automation name and version (commit hash); trigger (event or person); case id; start and end time UTC; inputs with hashes; outputs and where stored; errors and exit status; identity/credential used; whether any action was skipped or retried.

### Chapter 23: EX067–EX069

**EX067.** Stage latencies and totals are unchanged. FCS-304 drops from the missing list; FCS-306 now lists only `['rollback']`. FCS-302 still lacks evidence and rollback and FCS-306 lacks rollback, so the script prints "complete decision records 4 of 6" (301, 303, 304, 305).

**EX068.** The outcome was good, but the record shows no evidence relied on and no rollback, so the process cannot be judged good from the record. If the analyst had authority to disable the form (charter) and acted on signals she can describe, the speed was appropriate; the fix is to record the evidence and rollback afterwards and add the form to the pre-built containment actions.

**EX069.** "Problem: FCS-304 took 95 minutes from decision to containment because the edge firewall block had no procedure. Change: build and test an action card and automation for edge address/range blocks (Ch18). Owner: Network. Measure: decision → contain for this action ≤ 30 minutes in the next three uses and in a quarterly test. Review: Q4 service review."

### Chapter 24: EX070–EX072

**EX070.** Evidence-first 1: B's first step deletes the malicious message from mailboxes but never says to export it with full headers first. Communications 1: B notifies the incident lead and finance manager but never the bank (payment recall) or the supplier through a verified channel.

**EX071.** (1) Bank recall requested and outcome recorded with reference. (2) Malicious mailbox rules removed and verified absent by audit query. (3) Sessions revoked and credentials reset for compromised mailbox(es), confirmed in IdP. (4) Supplier informed via phone number from the contract file, not from the email. (5) Finance change to require call-back verification for bank-detail changes approved and logged.

**EX072.** Two teams of similar experience; each uses one playbook first and the other on a different but equivalent inject later (counterbalanced); measures (time to first decision, unanswered questions, critical steps missed) defined beforehand; an observer with a checklist; limits recorded (small n, tabletop not live).

### Chapter 25: EX073–EX075

**EX073.** Lanes: Duty analyst — receive detection; preserve file and portal logs (evidence); open case S3; query downloads. Incident lead — decide severity; approve escalation to S2 if downloads; coordinate. Portal owner — approve supplier account disable; remove file; confirm. Supplier liaison — contact supplier via verified contract contact; request their investigation. Privacy officer — assess resident notification if downloads. Closure: all lanes' conditions met, review scheduled.

**EX074.** I like: preservation before removal; download query with a clear S2 trigger. I wonder: how long portal logs are retained (Chapter 12 matrix shows 30 days — enough?); who covers supplier liaison out of hours. What if: the malicious file was an image that renders in browsers — does malware scanning catch it? What if the supplier is unreachable for 48 hours?

**EX075.** "Feedback: permanently block supplier uploads. Decision: declined. Reason: permit processing depends on supplier uploads daily. Compensating control: all uploads quarantined and scanned before publication; uploads from new devices require supplier MFA. Review: after next supplier-related case or in six months."

### Chapter 26: EX076–EX078

**EX076.** S: FCS-214, S2; account `permits-clerk-4` misused by external actor 11 May; `hr-assist-5` also compromised. B: password spraying from 198.51.100.23; legacy protocol allowed MFA bypass. A: both accounts contained (sessions revoked, methods removed, reset); use of 412 archive files unknown. R/pending: Identity to disable legacy protocols (owner T. Ruiz, due Friday); privacy officer decision on notification pending file-use assessment; watch R-12 alerts for both accounts. Next update 09:00. Incoming lead accepts at 17:10, read back pending decisions.

**EX077.** Executive: "Billing restore 80% complete, expected 10:30. No evidence yet that data left; egress review completes 11:00. Decision needed now: notify residents of billing delay (draft ready). Next update 12:00." Service desk: "Billing systems are being restored after a security incident; bills are delayed, no action needed by residents; payments are safe. Next update 12:00." Technical: "Restore 80%; integrity checks start 10:30 (owner Data Platform). Egress review of 05:00–06:10 flows ongoing (R. Lin). R-31 quiet. Next sync 11:00."

**EX078.** `awareness_time` and `awareness_recorded_by`; `regimes` list (e.g., GDPR Art. 33, contract with supplier X) as determined by privacy officer/counsel; per regime: `deadline`, `owner`, `status` (assessing, not required, drafted, sent), `sent_time`, `reference`; `determination_note` with author.

### Chapter 27: EX079–EX081

**EX079.** Valid: `check("T5",[("triage",set()),("investigating",set()),("closed-benign",{"triage_note"})])` → `T5 OK | final: closed-benign`. Invalid: a full T1 path then `("investigating",set())` → `T6 closed->investigating not allowed | final: investigating`. Reopening should be a separate, logged action (new linked case or override).

**EX080.** "Only the incident lead or Response Desk lead may force a transition. A justification of at least one sentence and a link to supporting evidence are mandatory. Overrides are logged with user and time, reviewed weekly by the Response Desk lead, and the monthly service report shows the override count and rate; a rising rate triggers a workflow review."

**EX081.** Triggers: workflow blocks S1/S2 handling, or completeness falls below the previous baseline for two weeks. Owner: Response Desk lead with ITSM platform owner. Steps: export current configuration; restore previous configuration from version control; map open cases (new/triage→open, investigating/containing→in progress, recovering/review→resolved pending review); announce to analysts; verify with a test case; record in change log.

### Chapter 28: EX082–EX084

**EX082.** "Exercise Quiet Meter is authorized on 14 October 09:00–13:00 in the `billing-test` environment using accounts `ex-supplier-1`, `ex-clerk-1..4`. Production systems, real resident data and external parties are excluded. All communications are marked EXERCISE. Any participant may stop play with the phrase 'REAL WORLD'; the exercise director (Response Desk lead) may end it. A real incident takes priority; controllers pause play. Signed: billing system owner, IT director."

**EX083.** 09:05 controller: alert R-12 "new MFA method for ex-supplier-1" → open case, triage. 09:20 controller as billing owner: "test billing data export ran unexpectedly" → scope, preserve logs. 09:40 controller as supplier: email "we did not log in today" → verified-channel contact. 10:00 controller as director: "I need an update in 15 minutes" → executive update. 10:30 controller: "the account just signed in again from a new address" → verify containment, extend scope.

**EX084.** "Observation: identity sessions were revoked at 09:24 before the IdP evidence export at 09:31. Impact: sign-in records for the period were still available, but in a real case token-level evidence could be lost. Cause: the mobile view of the runbook lists steps in two columns, making order ambiguous. Recommendation: single-column mobile runbook and a mandatory 'export complete' checkbox before revocation. Owner: Response Desk. Re-test: Q1 exercise."

### Chapter 29: EX085–EX087

**EX085.** Inventory: ≥ 98% of agent-reporting hosts reconciled to an owner and tier (reconciliation report). Triage thresholds: every case-opening rule in the register has a scenario, runbook and owner, and was reviewed within 90 days (register export). ITSM routing: four synthetic tickets matching each rule create restricted security cases and page on-call (test record with timestamps). Exercise programme: at least one functional exercise in the last 6 months with after-action items tracked to closure or re-test (AAR and tracker).

**EX086.** "Evidence store — purpose: preserve case artefacts with integrity. Owner: Platform (operations), Response Desk (use). Use: upload via case tool action 'Add evidence'; hash computed on ingest; custody entries automatic. Controls: separate account, object lock 400 days, access restricted to responders, access logged. Recurring tests: monthly hash verification of a sample, quarterly delete-attempt test, access-log delay check. Failure: if verification fails, freeze item, use original, open problem record. Links: Ch17 acceptance tests, custody procedure."

**EX087.** (1) Edge log forwarding stops — canary edge request missing alerts within 15 min. (2) Paging integration broken — synthetic S1 test page unacknowledged escalates to deputy within 15 min and raises an ITSM alert. (3) Backup job writes but immutability disabled — weekly configuration check flags object-lock off within 24 h.

### Chapter 30: EX088–EX090

**EX088.** "Detection register — partly met. Evidence: all four case-opening rules have scenario, runbook and owner; Q2 outcome labels recorded for 187 alerts; precision R-07 7.7%, R-19 0.8% before tuning; two cases found by staff reports with backlog items. Confidence: moderate — one quarter of data. Limitation: post-tuning effect not yet measured."

**EX089.** Rule: recovery and evidence integrity first, then high effect/low effort. (1) Permits restore test (recovery, S). (2) Mobile runbook fix (evidence integrity, S, exercise finding). (3) Supplier contacts (exercise failure, M). (4) Second on-call (out-of-hours latency, M, cost). (5) Security keys (large risk reduction but L effort; start procurement now, so it may run in parallel). Other rankings acceptable with a consistent rule.

**EX090.** Monthly: service measures and consistency-check report (Response Desk lead); detection outcome review (Response Desk); evidence-store sample hash verification (Platform). Quarterly: containment action tests (owners per action); restore tests by tier (Infrastructure/Data Platform); inventory reconciliation review (Platform); workflow tests T1–T6 (ITSM owner). Semi-annual: functional exercise with AAR (Response Desk with stakeholders). Annual: charter, severity scale and scope review (IT director); playbook review (Response Desk); dossier update.

<a id="glossary"></a>

## Glossary

- **Acceptance criterion** — An observable, pass/fail test that shows a component meets its requirement, supported by evidence.
- **Awareness time** — The recorded moment the organization became reasonably certain of a potentially reportable incident; starts many notification clocks.
- **Benign true positive** — An alert where the rule matched as designed but the activity was authorized.
- **Blast radius** — The set of users and services affected by an action such as a block or isolation.
- **Canary event** — A scheduled synthetic event used to verify that an evidence flow still delivers records within its expected delay.
- **Case** — One managed incident or suspected incident with an owner, scope, severity and linked records.
- **Chain of custody** — The record of who collected, held, transferred and accessed an evidence item, when and why.
- **Containment action card** — A documented, tested containment capability with authority, steps, side effects, verification and rollback.
- **Emergency change** — A change made outside the normal schedule to contain an incident, with minimum record and retrospective review.
- **Evidence flow** — A path that moves records from a source into a protected central store with known delay, retention and integrity controls.
- **Failure domain** — A set of components that fail or are compromised together because they share something.
- **Field simulation** — A functional exercise in which staff use real tools and processes against test systems under written authorization.
- **Handoff** — A structured, accepted transfer of case ownership or shift responsibility.
- **Pivot** — Following a shared key (account, address, host, hash) from one data source to another during an investigation.
- **Playbook** — A scenario-level guide naming roles, decision points, runbooks, communications and closure conditions.
- **Recovery point objective (RPO)** — The maximum acceptable amount of data loss measured in time.
- **Recovery time objective (RTO)** — The maximum acceptable time to restore a service.
- **Runbook** — A step-level procedure for one response task.
- **Scope statement** — A specific, revisable statement of the assets, identities, time window and question a case covers.
- **Severity** — A level (S1–S4 at Fernmoor) set by observable criteria that determines response urgency and escalation.
- **State model** — The allowed case states and transitions, with rules for what each transition requires.
- **Time to triage** — Triage-start time minus alert time, both from case-system fields.

<a id="references"></a>

## References

Standards, regulations and web pages change. Versions and dates below are those consulted for this draft (October 2026); re-verify before relying on them. Fernmoor City Services and every other organization (including suppliers such as PrintCo), person, case, address and number in this book is synthetic unless a sentence cites a public source.

- National Institute of Standards and Technology. [Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile, SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025; supersedes Rev. 2 (2012).
- National Institute of Standards and Technology. [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework). February 2024.
- Bartock, M., et al. [Guide for Cybersecurity Event Recovery, NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final). December 2016.
- Grance, T., et al. [Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities, NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final). September 2006 (check currency before relying on details).
- Kent, K., et al. [Guide to Integrating Forensic Techniques into Incident Response, NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final). August 2006 (tool-specific details dated).
- Kent, K., and Souppaya, M. [Guide to Computer Security Log Management, NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final). September 2006.
- Swanson, M., et al. [Contingency Planning Guide for Federal Information Systems, NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). 2010, updated 2010.
- National Institute of Standards and Technology. [Digital Identity Guidelines: Authentication and Authenticator Management, SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html). Revision 4 edition consulted.
- Ross, R., et al. [Developing Cyber-Resilient Systems: A Systems Security Engineering Approach, NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final). December 2021.
- FIRST. [CSIRT Services Framework, version 2.1](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1). 2019.
- ISO/IEC 27035 series, *Information technology — Information security incident management* (Parts 1–4; consult current editions).
- Cybersecurity and Infrastructure Security Agency. [Federal Government Cybersecurity Incident and Vulnerability Response Playbooks](https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf). November 2021.
- European Union. [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj), in particular Articles 5, 33 and 34.
- Dittrich, D., and Kenneally, E. [The Menlo Report: Ethical Principles Guiding Information and Communication Technology Research](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf). U.S. Department of Homeland Security, August 2012.
- Chamberlin, T. C. The method of multiple working hypotheses. *Science* (old series) 15:92–96, 1890; reprinted in *Science* 148:754–759, 1965. https://doi.org/10.1126/science.148.3671.754
- Platt, J. R. Strong inference. *Science* 146(3642):347–353, 1964. https://doi.org/10.1126/science.146.3642.347
- Fischhoff, B. Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty. *Journal of Experimental Psychology: Human Perception and Performance* 1(3):288–299, 1975. https://doi.org/10.1037/0096-1523.1.3.288
- Dekker, S. *Just Culture: Restoring Trust and Accountability in Your Organization*, 3rd ed. CRC Press, 2016.
- Mills, D., et al. [Network Time Protocol Version 4, RFC 5905](https://www.rfc-editor.org/rfc/rfc5905). 2010.
- Klyne, G., and Newman, C. [Date and Time on the Internet: Timestamps, RFC 3339](https://www.rfc-editor.org/rfc/rfc3339). 2002.
- Arkko, J., et al. [IPv4 Address Blocks Reserved for Documentation, RFC 5737](https://www.rfc-editor.org/rfc/rfc5737). 2010.
- Mockapetris, P. [Domain Names — Implementation and Specification, RFC 1035](https://www.rfc-editor.org/rfc/rfc1035). 1987.
- Rescorla, E. [The Transport Layer Security (TLS) Protocol Version 1.3, RFC 8446](https://www.rfc-editor.org/rfc/rfc8446). 2018.
- National Institute of Standards and Technology. [Secure Hash Standard (SHS), FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final). August 2015.
- Foudil, E., and Shafranovich, Y. [A File Format to Aid in Security Vulnerability Disclosure, RFC 9116](https://www.rfc-editor.org/rfc/rfc9116). 2022.
- Rose, S., et al. [Zero Trust Architecture, NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final). August 2020.
- Beyer, B., Jones, C., Petoff, J., and Murphy, N. R. (eds.). *Site Reliability Engineering*. O'Reilly, 2016; chapters [Managing Incidents](https://sre.google/sre-book/managing-incidents/) and [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/).
- ISO/IEC 27037:2012, *Guidelines for identification, collection, acquisition and preservation of digital evidence*.
- ISO/IEC 20000-1:2018, *Information technology — Service management — Part 1: Service management system requirements*.
- AXELOS. *ITIL Foundation: ITIL 4 Edition*. TSO, 2019.
- MITRE. [ATT&CK](https://attack.mitre.org/) knowledge base of adversary tactics and techniques.
