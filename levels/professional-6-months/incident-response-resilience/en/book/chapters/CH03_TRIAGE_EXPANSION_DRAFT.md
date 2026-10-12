# Chapter 03 expansion component — Time-aware intake and provisional triage

> **Editorial state:** Public integration draft for Chapter 03 of the professional six-month English course. This transient component augments [the canonical manuscript](../MANUSCRIPT.md#ch-03) without declaring the course or any chapter complete. Exercise IDs EX011–EX015 are unchanged.
>
> **Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). [Rights and provenance](../../../../../../RIGHTS.md).

## Additional learning objectives

A practitioner who completes this material can preserve four separate clocks, create a source-faithful multi-signal intake, defend a priority under conflicting evidence, design a falsifiable false-positive gate, and escalate a time-sensitive preservation need without implying permission for account disruption. The core product is a versioned triage ledger for the synthetic Cedar Training Network (CTN) case.

## 1. The four clocks of an alert are not interchangeable

**Source event time** is the time reported by the system that generated the event. It may reflect a local clock, a server time or a display timestamp. **Ingestion time** records when a collector accepted a copy, which may lag creation. **Discovery or acknowledgement time** records when a detector or analyst identified the item for response. **Case release time** in this curriculum controls what the learner was allowed to know at a given exercise checkpoint. A support reporter's remembered "about 09:00" is neither a timestamped database mutation nor a collector receipt.

A record can be late without being false. For example, C03's IdP sign-in event is reported at 08:58 UTC and ingested at 09:02. That four-minute gap is an observed relationship between the stated times, not proof the IdP took exactly four minutes to deliver it or that the two clocks were synchronized. Queueing, scheduled polling, serialization and clock differences are candidate explanations. Source identity and clock provenance remain important even for apparently well-formed ISO timestamps.

Clock correction must record both **direction** and **uncertainty**. C04 reports a runner device timestamp of 08:54 with the device measured four minutes **slow**. The normalized estimate is 08:58 UTC; subtracting four minutes would be a sign error. If the offset were measured at a different time, a real investigator might need to account for drift or a range of possible event times. CTN provides only a fixed classroom correction, so the learner must not invent seconds or a bounded error interval. Normalize to the supplied minute precision and document its limitations.

Why avoid naive text sorting? A timestamp with an explicit +02:00 offset and one with a UTC suffix can represent the same moment while their strings look different. A symptom remembered "around 09:00" cannot properly be placed at exactly 09:00:00. Keep **raw_time**, **time_basis**, **normalized_estimate**, **offset_or_rule**, **ingested_at**, **released_at** and **time_confidence** as distinct fields.

## 2. Open one case while preserving source-specific claims

CTN's first live symptom is C02, received by support at 09:04, described as S42 "appears unavailable" and reportedly first noticed around 09:00. It does not establish the authoritative slot state. At 09:09 the learner gains C03, C04 and C05. They can be investigated in one case because they potentially affect the same service interval, but they should not be collapsed into one actor narrative.

**C03** is an IdP summary: successful sign-in for svc-enroll at 08:58, session s-77, ingested 09:02. The summary does not identify a human or a client. **C04** is an endpoint report: a browser process on runner-03, raw 08:54 corrected to approximately 08:58, ingested 09:06; it lacks a session or application request ID. **C05** is an application audit: S42 edit at 09:01, request q-144, account label svc-enroll, blank session field, ingested 09:07. These are three different producers and three different assertions.

A wrong merge is "runner-03 used session s-77 to edit S42 through q-144." That adds links the provided fields do not support. A correct investigation question is "Can an approved, more detailed IdP event associate s-77 with a client, and is there any validated relation between that session and q-144?" This question may ultimately fail; the answer must be kept unknown until relevant source evidence is obtained.

Create one intake row per card with its producer, locator, source event time, ingestion/receipt time, release time, exact reported observation, service relevance, limitations, and owner of the next bounded question. Preserve the source wording and the difference between a sensor detecting a browser and an application reporting an edit. When two systems use the same account string, compare their identifier semantics instead of assuming a stable human identity.

## 3. Time-gated triage: 09:09 → 09:10 → 09:12 → 09:14

At **09:09**, C02–C05 support a potential enrollment anomaly and separate technical signals. The analyst may document the need for a state check and narrow source review, but cannot cite an approval calendar or source-expiry deadline that has not yet been released.

At **09:10**, C06 adds an approved maintenance entry for S40/S41 at 08:50. The visible scope omits S42. This increases the reason to ask about change authorization, but does not prove that no later addendum exists. The correct status is "S42 not included in the retrieved approval entry."

At **09:12**, C07 establishes that svc-enroll is shared between a scheduled job and occasional emergency operator use. It specifically **weakens simple actor attribution**: an account label does not distinguish human, service or process. It is not itself a log of who made the 09:01 change.

At **09:14**, C08 states that detailed IdP source events for the interval expire at 10:00. This introduces a separate deadline and may change triage urgency even though causal confidence remains low. The professional decision is to prepare a **bounded export request** through the identity custodian, naming source, range, selectors, minimum fields, purpose, approval and case destination. The analyst has not yet collected those records. This checkpoint is the last one considered in this chapter. C09 and later cards belong to subsequent chapters and cannot appear in the 09:14 observation ledger.

The resulting case record should be append-only or versioned. The 09:14 summary may explain what changed relative to 09:09, but should not silently insert C06–C08 into the earlier summary. A reviewer may ask, "Would the response at 09:09 still look defensible if every later card were hidden?" The answer must rest on C02–C05 alone.

## 4. Separate priority from certainty

CTN's classroom triage priority is an operational workload decision, not proof of a breach. **P1** denotes observed major service or safety impact needing immediate owner-led coordination, **P2** denotes urgent bounded investigation for plausible meaningful harm or impending loss of relevant evidence, and **P3** denotes routine handling where no urgent gap has been established. The organization may use different categories in practice.

Build the decision from four observations or uncertainties:

1. **Potential consequence:** one enrollment slot may be affected; neither the authoritative S42 value nor number of impacted learners is established by 09:14.
2. **Evidence strength:** C05 reports an S42 edit, but links from s-77 to q-144 are missing. The shared identity introduces multiple benign or concerning explanations.
3. **Evidence-loss timing:** C08's 10:00 detailed-log expiry statement creates an urgent preservation consideration, but is not permission for bulk export.
4. **Intervention side effects:** broad svc-enroll disablement could harm legitimate enrollment, so urgency does not justify skipping the appropriate owner approval.

A defensible priority at 09:14 is **P2 provisional**: work should proceed promptly while the case retains significant uncertainty. "P1 because successful sign-in means account takeover" fails because C03 labels a success, not a compromise. "P3 because the browser could be benign" underweights the time-sensitive opportunity to preserve narrow IdP details. "P2 because data may disappear and an edit could matter; request approved records and a state check" ties the decision to a falsifiable next step.

Confidence must describe a **claim**, not just the whole case. It is reasonable to have relatively high confidence that C05 reports an API edit while having low confidence about its authorization and actor. A binary "incident confirmed/not confirmed" field loses this nuance.

## 5. Reproducible local clock-correction laboratory

This is a new synthetic Python 3 offline view of C03–C05, not an IdP query. All times and identifiers are authored classroom values, and no credentials or network calls occur. The fixed date is a **laboratory date chosen for ISO parsing**, not a claimed date of the CTN main-case events.

~~~python
from datetime import datetime, timedelta

events = [
    ("C04", "2026-10-12T08:54:00+00:00", 4),
    ("C03", "2026-10-12T08:58:00+00:00", 0),
    ("C05", "2026-10-12T09:01:00+00:00", 0),
]
for card, raw, correction_minutes in events:
    normalized = datetime.fromisoformat(raw) + timedelta(
        minutes=correction_minutes
    )
    print(
        f"C3|{card}|{normalized:%H:%M} UTC|"
        f"clock_correction={correction_minutes:+}m"
    )
print("C3|C04_C03_same_minute=True|direct_join=False")
~~~

**Output executed with these fixture values:**

~~~text
C3|C04|08:58 UTC|clock_correction=+4m
C3|C03|08:58 UTC|clock_correction=+0m
C3|C05|09:01 UTC|clock_correction=+0m
C3|C04_C03_same_minute=True|direct_join=False
~~~

The final line is an explicit **analyst conclusion from the fixture**, not a computed assertion from a hidden join algorithm. A matching minute does not create a shared transaction key. In a real parser, the source's offset convention and time-zone handling would need independent validation. The code is deliberately small so the learner can inspect the sign of the correction and reproduce each visible output.

Perform two safe mutations: change the C04 correction from +4 to -4 and observe the incorrect 08:50 value; then restore +4 and alter C05's application event time. Neither mutation should silently change the C03/C04 join status, because no join key appears. Write a paragraph distinguishing the **model input**, the **executed parser result**, and the **hypothesis** about relationship between the events.

## 6. A false-positive decision is an evidence gate

"False positive" is not a polite way to say "we cannot prove compromise." A false-positive conclusion must have an explicit closure question and supporting discriminators. For C04, a plausible benign mechanism is expected scheduled runner activity. A relevant discriminator would be an authorized job/run record with matching identifiers and confirmed expected process behavior. At 09:14 that record has not been received. Therefore "scheduled job explains C04" is a hypothesis only.

For C06, a second benign explanation is an approval addendum that was not shown in the retrieved calendar. A discriminator is a signed or otherwise authoritative S42-scoped change record from the change custodian. Absence from the **retrieved entry** is not proof of absence from every ledger. The concerning hypothesis is out-of-scope account use to change S42; a discriminator requires reliable source relationships, decision scope, and evidence of the specific path. An unsuccessful search is not automatically proof no record exists: record dataset, query, account and time limitations.

False positives can coexist with genuine service symptoms. A browser detector might be noisy while an S42 edit is real. Closing the whole case because one sensor is benign would conflate distinct claim scopes. Conversely, a later approved S42 edit would not alone prove the front-end was displaying accurate, timely state to all users. Closure rules should require the service owner to assess the relevant user-facing outcome under the organization's approved incident process.

## 7. Draft a bounded escalation before source expiry

At 09:14, write a message that a supervisor can act on. It must specify the source expiry claim, why narrow detail matters, a proposed custodian and range, and an independent state check. For example:

> At 09:14, the CTN enrollment case is P2 provisional. Support reports an S42 symptom, and the API records request q-144; an IdP summary reports session s-77 and an endpoint report shows a roughly coincident browser event. There is no validated session-to-request join or human attribution. C06's visible approval covers S40/S41 only, and C07 identifies shared use of the account. C08 states detailed IdP records expire at 10:00. Please route an authorized, minimum-field svc-enroll export for 08:50–09:05 through the identity custodian and ask the application owner for present S42 state. C01's missing after-hours identity alternate remains unresolved. Reassess on these results or before loss of the detailed source; no disruptive action is approved or executed.

This escalation is deliberately cautious. "Please route" is a proposal, not a statement of collection approval. The exact desired fields should live in the related request: event ID, original event time/zone, account, session, client and outcome, plus collection/source metadata as policy permits. The record should specify who requested this and when; the custodian must confirm which data can legally be retrieved.

A prioritization rubric is useful only if another responder can reproduce it. Require the reviewer to identify each source card cited, the 09:14 cut-off, the unknown actor, service-impact gap, expiry claim and next checkpoint. If any future card is smuggled into the 09:14 argument, the exercise fails chronology regardless of technical plausibility.

## 8. EX011–EX015: deeper assessment and worked-answer notes

**EX011 — Intake form.** Objective: preserve producer boundaries. Input: C02–C05 as released at 09:09. Required artifact: four rows with event/receipt/release clocks, source locators, service relevance, missing correlation field and a responsible next question. Model: C02 has approximate noticed time and 09:04 receipt; C03 has 08:58 sign-in/09:02 ingestion; C04 has raw 08:54, corrected 08:58/09:06 ingestion; C05 has 09:01 edit/09:07 ingestion and a blank session. All C03–C05 released 09:09. Two points require distinct source rows and no invented actor.

**EX012 — Clock reconciliation.** Objective: apply offset direction without inventing precision. Input: C03/C04. Calculate 08:54 + four minutes = **08:58 UTC estimate**. Explain that coincidence at the minute level prompts investigation but supplies no source join. Model reasoning must identify the measurement as a synthetic fixed offset and decline subsecond ordering. Reversing the sign or asserting common causation is a failure of the critical criterion.

**EX013 — Priority decision.** Objective: document a risk-informed decision under uncertainty. Input: C02–C08 and local P1–P3 meanings. Model: P2 provisional at 09:14, service impact plausible but not established, account attribution weak, relevant details threatened by 10:00 expiry. Include event-based review (custodian response or S42 state) plus checkpoint before expiry. A valid alternative priority requires an explicit locally supported rubric and the same evidence/authority cautions.

**EX014 — False-positive gate.** Objective: distinguish hypotheses from established exclusions. Input: C04/C06/C07. For each benign hypothesis, identify an independent bounded artifact that would support it; for the concerning hypothesis, name the specific missing join and approved scope check. Model: signed S42 addendum would narrow the authorization question; job-run evidence would clarify expected runner behavior; a trusted session/request relation would inform actor/path analysis but may still not identify a human. Do not mark any artifact as received at 09:14.

**EX015 — Shift escalation.** Objective: get a timely and authorized handoff without overclaiming. Input: C02–C08. Produce 90–150 words with P2 rationale, C08 deadline, bounded IdP request, S42 state check, C01 owner gap and reassessment trigger. Model status: export **requested**, not collected; state check **proposed**, not observed; svc-enroll **not disabled**. Two points require this status distinction, exact source cutoff and operationally useful role assignments.

### Common errors and operational limits

- Confusing receipt with event time; correct by retaining each timestamp and its source.
- Treating equal clock minutes as proof of a session-to-request join; correct by requiring shared identifiers with validated semantics.
- Backdating an expiry warning to 09:09; correct by keeping C08 at its 09:14 release.
- Using possible benign behavior to dismiss the service impact question; correct by evaluating each claim separately.
- Asking for every IdP record because a source may expire; correct with custodian-approved selectors and a bounded purpose.
- Treating a provisional priority as a compromise verdict; correct with an uncertainty and next-test ledger.

### Sources and originality

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) situates detection, response and recovery in organizational cybersecurity risk management, without defining CTN's P1–P3 formula.
- [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) is a historical final reference on log-management processes. Its age requires validation against a current provider and retention policy; it is not an IdP-specific timing claim.
- The synthetic C02–C08 case and code are educational material. No external source has been copied into the exercises.

### Synthesis

Good triage preserves a time-specific decision: what was known, by which source, what remains unknown, and what authorized request can reduce decision uncertainty. At 09:14, P2 reflects urgency and plausible service risk, **not** confirmed misuse. Chapter 04 adds a separately documented collection approval and new evidence; neither may be assumed in the Chapter 03 ledger.

### Continue studying — Chapter 03 of 12 (integration draft)

[← Chapter 02](../MANUSCRIPT.md#ch-02) · [Chapter index](../../SUBJECTS.md) · [Canonical Chapter 03](../MANUSCRIPT.md#ch-03) · [Chapter 04 →](../MANUSCRIPT.md#ch-04)
