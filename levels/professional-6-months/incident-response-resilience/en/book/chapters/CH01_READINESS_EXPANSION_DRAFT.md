# Chapter 01 expansion component — Service readiness as a testable contract

> **Editorial state:** Public integration draft for Chapter 01 of the English professional (six-month) course. This is a transient component, not a second book, released chapter, completed A4 measurement, or modification of the canonical manuscript. Integrate with [Chapter 01](../MANUSCRIPT.md#ch-01) after review. Exercise IDs EX001–EX005 and their existing answers remain authoritative until integration.
>
> **Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching material is within the scope of [CyberABC rights](../../../../../../RIGHTS.md); third-party sources retain their rights.

## Additional learning objectives

By the end of this expansion, a supervised responder can (1) describe a service boundary as a dependency and evidence graph; (2) write a source contract with an objective collection-quality test; (3) distinguish log availability from end-to-end diagnostic coverage; (4) expose a single-point-of-contact risk without inventing delegated authority; and (5) review another analyst's readiness artifact against falsifiable acceptance criteria. The product is a rehearsal-ready pack that a custodian could actually execute later in an **authorized training environment**.

## 1. The service boundary precedes the telemetry boundary

At the C01 checkpoint, Cedar Training Network (CTN) has only a fictional readiness worksheet, not a live security event. The enrollment service's intended behavior is more useful than a list of security tools: a learner selects a class, the front end requests availability, the API checks and changes a slot, the identity layer authenticates privileged calls, a queue may send a notification, and the recovery path must reconstruct a consistent enrollment state. This is an **intended service model**, not an observed trace. It must not be narrated as if the system has been inspected.

A dependency is anything whose failure could change a meaningful service outcome. Distinguish four kinds. A **functional dependency** moves or validates enrollment data; an **administrative dependency** provides decision rights and access; an **observability dependency** produces evidence about those transactions; a **recovery dependency** permits a tested return to an acceptable state. One element may belong to several classes. For example, an identity provider can be necessary for staff sign-in and for the audit record that would later explain a privileged edit.

Service owners need a definition of normal behavior that is precise enough to test. "Enrollment works" is vague. An operational criterion might be: "For an authorized synthetic class with one available seat, a reservation request either commits one reservation and returns its new version, or fails without consuming the seat." This proposed invariant is a **new teaching test definition**, not a fact about CTN's implemented transaction model. A responder should ask the API owner whether partial writes, retries, and queue delays change the invariant.

Consider two incorrect inventories:

- "SIEM, firewall, IdP, backup" names technologies but cannot identify which one supplies the authoritative S42 state, who can access a relevant time range, or which business action it supports.
- "API → database → backup" adds direction but omits decision owners, authorization, evidence retention, scheduled-job write paths and the ability to verify a restore.

A stronger inventory contains a decision question on each edge. "API audit → request correlation" is useful only if the application actually emits a stable request identifier. "Backup → safe restoration" requires a known restore procedure, recovery owner, comparison baseline and isolated acceptance test. A completed backup job is evidence that a backup operation reported success, not proof that reconstructed S40, S41 and S42 values are correct.

## 2. Build a graph whose edges can fail

A service graph must distinguish **data flow** from **evidence flow**. A slot change may travel from scheduled job to API to data store. The corresponding evidence may instead travel from API audit to a logging collector to a retention tier, and from IdP to a different collector. The responder's correlation plan depends on whether those paths share fields such as request ID or session ID. C01 supplies no executed end-to-end correlation proof.

A practical five-column source card asks:

| Question | Operational answer required | Example of an unsafe shortcut |
|---|---|---|
| Which decision? | Determine whether a particular slot was edited by a named request ID. | "Find out what happened." |
| Which producer? | API audit, including whether job and manual routes both emit request IDs. | "The SIEM has everything." |
| Which time anchor? | Source event UTC, collector receipt, retention anchor and export latency. | "Logs last 24h." |
| Which custodian and gate? | Authorized application custodian, primary and approved alternate if documented. | "Anyone on call can pull it." |
| What would disprove coverage? | A permitted test edit not appearing in the selected export within a defined window. | "No alert means no gap." |

Treat each edge as **claimed**, **test planned**, **tested-pass**, **tested-fail**, or **not observable**. Those statuses cannot be collapsed into a reassuring check mark. A source can pass one test and still lack another route. A supported, well-scoped statement is: "The known-good scheduled-path event was retrieved with slot and request identifiers within 20 minutes during training rehearsal R1." The unsupported extension is: "All enrollment writes are always logged." Even R1 requires a date, dataset, permitted tenant, operator, baseline, selection query and evidence receipt before that statement can be used.

Dependency criticality is contextual. An after-hours identity contact gap may be urgent not because identity always dominates the case, but because the source might become irretrievable while the only known custodian is unreachable. A backup-restore test may be important for resilience but may not be the first response to a short retention gap. Explain the **decision affected**, not just a red/yellow/green category.

## 3. Separate readiness assurance from incident assertions

C01 is a worksheet discovered at 08:40 UTC. Its missing after-hours identity alternate and service-owner fallback are readiness defects; they do not indicate a compromise. Its "API audit: 24 hours" entry is an unverified statement. The first task is to preserve these unknowns.

There are at least four plausible anchors behind the 24-hour phrase: source event age before deletion, time available in a query interface, lifetime of a queued export, or a published service/contract objective. A rolling retention period could also differ by dataset or ingestion delay. C01 does **not** tell us which interpretation applies, and a professional responder must not calculate a hard evidence-loss time from it. Ask the custodian which exact dataset, clocks, query filters, delays and deletion mechanism support the claim. Then design a permitted test near the edge, if organizational policy allows it.

An operational readiness measure should pair an objective with a failure mode. For example:

- Objective: retrieve a synthetic S41 scheduled-job edit with source event timestamp, slot ID and request ID within twenty minutes.
- Input and condition: authorized nonproduction tenant, preapproved test identity, known synthetic S41 record and one scheduled write.
- Negative control: S40 has no matching S41 request and must be absent from the S41-specific result.
- Measurements: job trigger time, API acknowledgement, producer event time, collection start and completion, field presence and number of selected rows.
- Failure criterion: missing audit event, missing stable request ID, unrelated S40 included, collection outside the agreed window, or undocumented clock relation.
- Remediation proposal: ask the application custodian to repair field coverage, source routing, or query semantics; **do not** rewrite the data or claim that coverage was repaired.

A negative control guards against a dangerously broad query. It does not prove that every unrelated change is excluded. Use an explicit field equality predicate for a slot and request when possible, rather than a timestamp-only proximity filter that may accidentally mix concurrent operations.

## 4. A reproducible offline coverage rehearsal

The following **new synthetic fixture** tests whether a trainee can preserve missing states rather than interpret every inventory row as operationally verified. It is not the CTN production inventory, and no source collection is carried out. It uses Python 3 standard library features only, makes no network request, writes no files and needs no credentials.

~~~python
dependencies = [
    ("api_audit", "app_owner", "request_id", "yes"),
    ("idp_detail", "identity_custodian", "session_id", "unknown"),
    ("support_ticket", "support_lead", "received_at", "yes"),
    ("backup_copy", "recovery_lead", "restore_test", "no"),
    ("change_ledger", "service_owner", "scope_id", "unknown"),
]
for source, owner, key, status in dependencies:
    print(f"C1|{source}|{owner}|{key}|{status}")
gaps = [source for source, _, _, status in dependencies if status != "yes"]
verified = sum(status == "yes" for *_, status in dependencies)
print("C1|gaps=" + ",".join(gaps))
print(f"C1|verified_sources={verified}/{len(dependencies)}")
~~~

**Executed output (Python 3, against the exact fixture above):**

~~~text
C1|api_audit|app_owner|request_id|yes
C1|idp_detail|identity_custodian|session_id|unknown
C1|support_ticket|support_lead|received_at|yes
C1|backup_copy|recovery_lead|restore_test|no
C1|change_ledger|service_owner|scope_id|unknown
C1|gaps=idp_detail,backup_copy,change_ledger
C1|verified_sources=2/5
~~~

Here, "yes" is **fixture status**, not actual verification of a CTN source. The denominator is five listed records, not all service components or all telemetry paths. Never report "40% ready" as an institutional maturity finding. The measurement only says two of the five classroom rows are marked yes. Change "idp_detail" to yes and run again; the gap list should shrink by one, but that still would not demonstrate an approved identity export route or a named after-hours alternate.

Use a second, manual fault-injection exercise: pretend the support contact is unavailable, then attempt to follow the map to an alternate. If the alternate field is blank, the test **fails as a contact path**, even though the script still prints that the ticket source is marked yes. This contrast demonstrates why automated coverage arithmetic cannot replace operational ownership tests.

## 5. Runbooks need decision rights as well as contact addresses

A contact is a place to ask a question, not necessarily the person authorized to answer it. Draft an owner card with four independent slots: data custodian, service decision owner, execution operator and incident coordinator. The same real person might occupy multiple slots under a local policy; keep their **function at each decision** visible. For a read-only IdP export, record who grants access to protected log data and who produces the receipt. For disabling an account, record who accepts enrollment disruption and who can implement a reversible control. Do not assume the custodian is the change approver.

An alternate must be established **before** the primary becomes unavailable. An invented escalation contact would conceal a readiness defect. C01's blank entries therefore remain "not supplied." A supervisor should be given an explicit choice: confirm an authorized alternate under the organization's actual policy, or record that a requested action cannot proceed via this route. The practitioner may prepare an escalation draft but cannot grant themselves privileges because a source might expire.

Use the following owner unavailability test: ask an alternate to identify the approved export pathway and the exact decision they can make. Stop if the contact is unknown or cannot explain the required scope. Log the attempted rehearsal as **not performed** until it actually occurs. This is a legitimate negative finding in a readiness review; it is not evidence of breach, negligence, or authorization to use an emergency override.

## 6. Compare a quick inventory with a defensible readiness contract

A spreadsheet listing systems can be assembled rapidly and is useful for orientation, but its failure is **false completeness**. A decision-centered contract costs more effort: each source has a bounded question, selectors, clock semantics, route coverage, owner, approval condition and a verification receipt. The trade-off is worth making for high-impact decisions such as "who changed S42?" and "can a clean version be restored without erasing valid changes?"

There is a similar choice between a single rehearsal and stratified tests. One scheduled-path edit can verify a narrow happy path. Distinct scheduled, manual and emergency write routes may emit different audit fields, use different identities or bypass different collection components. Separate tests avoid extrapolation. Negative tests matter, too: deliberately query S40 under the S41 selector and inspect whether false matches appear. A test that cannot fail in a defined way is a demonstration, not an assurance check.

Do not stage these tests in the production environment on the strength of a learning exercise. A permitted training tenant, synthetic classes, nonpersonal identifiers, documented owner approval and a bounded cleanup plan are prerequisites. If a local laboratory cannot simulate one dependency, write "not evaluated" and design a tabletop substitute instead of fabricating an output.

## 7. Review the readiness pack before handing it to Chapter 02

A reviewer should ask whether every statement can be labeled as **model**, **proposed test**, **observed test result**, or **unverified assumption**. For C01, only the fact that a worksheet was supplied at 08:40 and its recorded omissions are scenario observations. The proposed S41/S40 tests have no observed outcome. The reviewer also checks accessibility: column headings should identify the decision being made; file paths and role abbreviations should be expanded on first use; the handoff should remain intelligible without a diagram.

A defensible shift handoff gives the next responder a useful action even when nothing dramatic happened: "Before any S42 live case, obtain the authorized identity alternative, confirm the service-owner decision route and test whether source/collector clocks and retention anchors are understood. Use a limited synthetic S41 edit with S40 as negative control to check request-ID fields and retrieval latency. No CTN incident has been observed at C01." This is readiness work. Chapter 02 uses these unresolved ownership gaps when C02 later reports an S42 symptom; the next chapter must not retroactively treat C01 as an incident alert.

## EX001–EX005: deeper exercise work and reviewable answer supplements

The following augment the five existing IDs, rather than creating replacements. Score using the current manuscript's 0–2 criteria. An artifact earns two only when a second responder can test or act on it without inventing a fact.

**EX001 — Dependency map.** Objective: design a five-source decision graph. Input: C01 and the stated CTN service model. Deliver a table for API audit, IdP detail, support, change ledger and backup. Annotate each connection with "claim/tested/not supplied" and write a missing-field query for its custodian. Example model decision: "API audit would support a slot/request join; the scheduled-path request-ID coverage is unverified." Incorrect: "API audit proves every S42 change has a user." Assess whether the learner provides all five decision/owner/gap triples and keeps the C01 checkpoint.

**EX002 — Evidence contract.** Objective: make the S41 audit claim falsifiable. Input: synthetic S41 and S40, twenty-minute retrieval window. Deliver selectors, timing start/end rules, required fields, positive and negative checks, permitted custodian and failure fallback. A worked acceptance condition is "record found for S41 and intended request, S40 absent under the exact S41 query, required fields present and retrieval completed within twenty minutes." This is a **conditional acceptance rule**, not a lab result. The assessor rejects claims of completed collection without a receipt.

**EX003 — Escalation matrix.** Objective: separate information custody from change authorization. Input: C01 owner gaps. Make three rows: IdP export; account restriction; service disruption tolerance. Identity custodian may collect under approved scope, identity/service and emergency-change authorities decide a disruptive account action, and service owner decides tolerable enrollment impact. The after-hours alternates remain blank/unknown. A good reviewer asks "Who can decide when the primary cannot respond?" A correct answer may be "the provided scenario does not say," followed by escalation through the actual organization.

**EX004 — Retention ambiguity.** Objective: avoid fictional deadlines. Input: "API audit: 24 hours." Produce three possible anchors and one custodian question for each. Model: "Is 24 hours counted from producer event time, from collector ingestion, or from availability in the export queue?" All are possibilities; none is CTN fact. Next: propose a lawful/authorized edge-of-window rehearsal and a fallback to a second source if the primary is not available. A "delete at 08:40 tomorrow" answer is not supported.

**EX005 — Shift handoff.** Objective: turn the four artifacts into a 90–140-word action note. A model reviewer checks for the service outcome, two priority gaps, named roles, S41/S40 authorized test, retention clarification, proposed/observed status and no compromise conclusion. One defensible opening is: "C01 is a preparation worksheet, not an alert. Enrollment depends on application, identity, support, change and recovery processes, but the after-hours identity path and the service-owner fallback have not been supplied." Finish with named proposed tests and a specific next checkpoint. Do not assert that any source was already tested.

### Source boundaries and references

- [NIST SP 800-61 Rev. 3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) supports integrating incident response with organizational cybersecurity risk management. The CTN service cards and readiness contract above are original exercises, not NIST-mandated forms.
- [NIST SP 800-92 (final, 2006)](https://csrc.nist.gov/pubs/sp/800/92/final) supports log-management planning. Its age matters; it is not a guarantee about a modern cloud export service.
- [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) addresses cybersecurity event recovery planning and testing. A successful backup job does not replace this component's isolated recovery-acceptance design.

### Synthesis

Readiness is measurable only **within the explicit scope of a completed test**. Inventory, approval path, evidence path and recovery test must each have an owner and an observable failure condition. C01's gaps are inputs to a supervised response workflow, not grounds for declaring an incident.

### Continue studying — Chapter 01 of 12 (integration draft)

[Course home](../../../README.md) · [Chapter index](../../SUBJECTS.md) · [Canonical Chapter 01](../MANUSCRIPT.md#ch-01) · [Chapter 02 →](../MANUSCRIPT.md#ch-02)
