# Professional Incident Response — Chapters 01–05 Expansion (PUBLIC DRAFT)

**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). **Course:** 039 / Incident Response and Cyber Resilience / Professional, six months. **Language:** English. **State:** temporary public teaching draft; not a second book or completed edition. Consolidation target: [MANUSCRIPT.md](../MANUSCRIPT.md). All original C01–C33 and EX001–EX060 IDs, original teaching, release chronology and answers remain authoritative until integrated.

**Integration convention:** Insert each chapter's teaching after the final existing numbered instructional subsection and before its “Common mistakes and limits” heading. Insert the corresponding worked-answer expansion immediately after the same subject's EX results within the manuscript's [worked-answer appendix](../MANUSCRIPT.md#worked-answers). These additions do not change the subject count, exercise IDs, or navigation.

## Chapter 01 — Incident lifecycle and organizational readiness

**Precise location:** after Chapter 1 §1.10, before “Common mistakes and limits”. This material develops the C01 readiness exercise for a supervised practitioner without inventing an incident at 08:40.

### Readiness is a set of independently testable decisions

C01 is a synthetic inventory, not an alert or proof that its listed capabilities function. The service owner must state what an acceptable enrollment does *before* the analyst chooses which logs to inspect. For a proposed isolated enrollment test, the business invariant might be: one authorized reservation consumes no more than one available place, returns a stable operation reference, and leaves the slot unchanged after a rejected request. This is a **proposed test condition**; the current CTN cards do not prove the implementation honors it.

Separate four planes. The **business/data plane** contains the front end, enrollment API, scheduled and manual write routes, and authoritative slot state. The **observation plane** contains application audit, identity telemetry, collector, index and restricted export. The **authority plane** contains the service owner, identity custodian, incident lead, delegated alternates and their separate rights. The **recovery plane** contains an identified copy, isolated restore method, accepted slot targets and tested return conditions. A green signal in one plane does not certify the others. A healthy collector can omit a manual write route; a working backup job can produce an unusable restore; a reachable custodian may be unable to authorize an account restriction.

A responder's dependency graph should have *typed edges*, not just boxes. “Scheduled writer → API” is a proposed data path. “API → audit store” is a proposed observation path. “Audit store → case copy” requires separate selection, custody and permission. “Service owner → approval record” is a decision path, not a technical event. Each edge should have a producer, consumer, time basis, failure signal and an accountable source to ask. Unless tested with a known synthetic event and a reviewed source receipt, mark it **claimed**, **not verified** or **failed**, never “all logs available.”

The distinction is central to [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), which places incident response within cybersecurity risk management, and [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), which describes outcomes without prescribing CTN's invented workflow. The graph and test rubric here are original teaching methods, not NIST requirements.

### A concrete failure investigation without inventing a breach

**Synthetic preparation variation, not a new C-series card.** Suppose the application owner proposes a harmless scheduled S41 write in an approved training tenant. The source audit returns a stable request ID, but the manual write route returns only an account label. The first observation can support a *scheduled-route test*, while the second prevents reliable manual-route request correlation. It is unsafe to declare that the entire enrollment API has complete audit coverage.

Meanwhile, C01's “API audit: 24 hours” has no retention anchor. It could refer to source-event age, collector visibility, query-horizon constraints or export-artifact lifetime. The last safe retrieval time differs across these interpretations. The proper next question is: which producer and dataset, which timestamp anchors the policy, what happens with ingestion lag, and what oldest expected marker can be retrieved by an authorized custodian? Adding twenty-four hours to a selected event time does not answer any of these source questions.

Finally, C01 names no after-hours identity alternate or service-owner fallback. That is a capability gap, **not evidence of malicious activity or negligence by a specific person**. Record the primary role, attempted contact, missing authority path, event that should trigger escalation and which non-disruptive work may continue. An analyst may draft a limited request; neither urgency nor access to a dashboard grants permission to use substitute credentials.

### Supervisor handoff: evidence, not assurances

Each proposed readiness test needs: decision question; exact synthetic input and producer; permitted route and approval; a positive expected row with original UTC time, slot and request ID; an unrelated S40 negative control; a collection clock and twenty-minute acceptance window; an independent reviewer; and a failure/rollback rule. The **test authorization**, **executed rehearsal receipt**, and **service readiness acceptance** are separate states. A supervisor can approve one while declining the others. The output should tell the next responder exactly which missing field, unreachable custodian or unverified route could invalidate a future incident claim.

