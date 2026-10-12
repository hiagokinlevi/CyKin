# Chapter 05 expansion component — Hypothesis-driven investigation and source-traceable timelines

> **Editorial state:** Public transient integration draft for Chapter 05 of the professional six-month English course. This is an expansion of [the canonical Chapter 05](../MANUSCRIPT.md#ch-05), not another book or a completed chapter. Existing exercise identifiers EX021–EX025 and the authoritative manuscript answers remain unchanged pending integration.
>
> **Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). See [CyberABC rights and provenance](../../../../../../RIGHTS.md).

## Additional learning objectives

The learner can build a replayable source-ledger timeline, distinguish matching field values from validated cross-system correlation, compare three causally different explanations, prioritize a minimum-data discriminator by decision value, and deliver a 09:26 handoff that is ready for supervised containment planning **without** fabricating authorization, execution or incident attribution.

## 1. Investigation is not narrative completion

By the start of this chapter, CTN has a preparation worksheet, a support symptom, identity and endpoint signals, an API edit, a narrow visible approval, a shared-account explanation, an expiry warning, an IdP export with acquisition gaps and a screenshot with uncertain display context. These items are evidence **about specific claims**. They do not combine automatically into a single story.

An analyst may notice that the event times cluster near 08:58–09:01. That pattern generates a question: "Could the reported sign-in, runner process and S42 write be part of one mechanism?" It does not answer it. A coherent story is especially seductive when an application audit and IdP record share an account label. Shared account names are weak identity keys; they may represent several sessions, multiple operators, jobs or credential uses. The missing relationship between session **s-77** and request **q-144** remains pivotal.

Keep an explicit **claim-to-source map**. Each assertion needs source ID, exact field or excerpt, time basis, acquisition quality and a confidence/limitation note. Separate three statement types:

- **Documented observation:** "C05 reports S42 edit at 09:01 with request q-144 and a blank session field."
- **Analyst inference:** "A shared identity could link a human or automated action to the edit, but no validated path is provided."
- **Conditional decision:** "If a scoped state check finds continuing harmful writes, escalate options to the service and change authorities."

A fourth statement type, **verified result**, requires the actual approved check and its recorded output. Nothing in C02–C12 is a containment execution or a verified restoration. The safest useful investigation is one that exposes what would make its current explanation wrong.

## 2. Preserve a two-axis timeline

A conventional event timeline answers "when did the source say the event occurred?" A professional case also needs an **availability timeline** answering "when did the responder learn it?" These axes can disagree sharply. Without both, a later reader may blame a 09:04 analyst for not acting on C12, which was unavailable until 09:26.

Use fields for **raw source time**, **normalized or estimated time**, **source card**, **source type**, **collector/case receipt**, **release time**, **supported claim**, **known time uncertainty**, and **prohibited inference**. Do not shorten "around 09:00" to a precise 09:00:00 or convert C10's time without labeling it conditional.

The essential event-time view at 09:26 is:

| Raw/normalized position | Source | What can be asserted | Key limit |
|---|---|---|---|
| 08:50 | C06, retrieved 09:10 | Visible maintenance entry approves S40 and S41 | Not proof that every addendum was checked |
| 08:54 local / ~08:58 UTC | C04, released 09:09 | Browser activity reported on runner-03 | Clock corrected four minutes; no session ID |
| 08:58 UTC | C03, released 09:09; C09 received 09:18 | svc-enroll sign-in, s-77; C09 lists runner-03 client | Export acquisition completeness and link to q-144 unresolved |
| Around 09:00; ticket 09:04 | C02 | S42 reportedly appeared unavailable | A reporter estimate, not a mutation timestamp |
| 09:01 | C05, released 09:09; C12 supplements at 09:26 | S42 edit with q-144 and self-reported batch-17 tag | Tag alone does not validate job origin |
| 08:59 IdP row / receipt 09:18 | C09 | Denied s-78 event also in supplied CSV | No established relevance to S42 change |
| Conditional 09:21 / receipt 09:22 | C10 | Unavailable state visible in screenshot | Unverified capture clock, cache and database state |
| 09:24 | C11 | Operator suggests possible late S42 addendum | Statement has no attached authoritative approval |
| 09:26 | C12 | Read-only audit view adds batch-17 tag to q-144 | Producer self-report, no verified run record |

The table intentionally contains both event and case times, but a final learner artifact should use **separate columns**. C09's 08:59 row, for example, becomes visible to the responder only on 09:18 receipt. C11 cannot be inserted as a verified addendum into the 08:50 entry; its existence is merely an operator's later claim.

A subtle contradiction remains: a reporter first noticed an S42 symptom around 09:00, while the application audit edit is timestamped 09:01. Possible explanations include the imprecision of "around," an earlier or independent symptom, clock uncertainty, a separate front-end issue or more than one change. The evidence does not select among them. An investigator should preserve the tension rather than adjusting a recorded timestamp to make a smooth narrative.

## 3. Graph joins require field semantics, not coincident labels

Represent events as nodes and asserted relationships as typed edges. A **same-source match** may be meaningful when the producing system guarantees identifier uniqueness in the relevant scope. A **cross-source match** requires evidence that both systems use the same namespace and emit the identifier for the same transaction. A **causal edge** needs more than equality; it needs a validated mechanism and appropriate temporal/semantic context.

At 09:26, C03 and C09 report **s-77**. In the supplied C09 rows, s-77 is associated with client **runner-03**. C04 separately reports a browser process on device **runner-03**. This device/client text similarity makes a useful investigative lead but is not a direct process-to-session join. C05 and C12 both bind **q-144** to the API edit; C12 adds a **self-reported batch-17 tag**. That label is not cryptographic proof that the scheduled job originated the request or had the S42 edit within approved scope.

A dangerous shortcut is to cross the graph from s-77 to q-144 merely because both records include svc-enroll around the same time. The API's session field is **blank**. Unless another permitted source supplies a verified shared identifier or tested relationship, the direct edge is missing. Neither a confident prose description nor a dashboard correlation score creates that evidence.

The distinction is especially important for accountability. Even a validated task-to-request join (which has **not** been released at the C12 checkpoint) would identify a technical mechanism, not necessarily the human who configured, triggered or controlled the task. Do not import later chapter findings such as C13–C20 into the 09:26 analysis.

## 4. Reproducible offline join-audit exercise

This Python 3 fixture demonstrates which explicit identifier equalities are visible **within supplied synthetic records**. It does not query CTN, validate the provenance of C09, compute a human identity or infer a causal relationship from account labels.

~~~python
records = [
    ("C03", "identity", {"session_id": "s-77", "account": "svc-enroll"}),
    ("C09", "identity", {"session_id": "s-77", "client": "runner-03"}),
    ("C04", "endpoint", {"device": "runner-03"}),
    ("C05", "application", {"request_id": "q-144", "account": "svc-enroll", "session_id": None}),
    ("C12", "application", {"request_id": "q-144", "claimed_tag": "batch-17"}),
]
allowed = {
    ("C03", "C09", "session_id"),
    ("C05", "C12", "request_id"),
}
for first, second, key in sorted(allowed):
    a = next(fields for card, _, fields in records if card == first)[key]
    b = next(fields for card, _, fields in records if card == second)[key]
    print(f"C5|{first}<->{second}|{key}|{a}|match={a == b}")
print("C5|s-77_to_q-144|DIRECT_JOIN=NO")
~~~

**Executed output for this exact fixture:**

~~~text
C5|C03<->C09|session_id|s-77|match=True
C5|C05<->C12|request_id|q-144|match=True
C5|s-77_to_q-144|DIRECT_JOIN=NO
~~~

The two "match=True" statements test **value equality for the specified fields**. They do not independently verify source provenance or full identifier semantics. The final "DIRECT_JOIN=NO" is an explicit analyst annotation based on the absent shared key. It is not the result of a hidden graph algorithm. The distinction between equality and validated causation is part of the learning outcome.

Safe negative test: insert a proposed edge ("C03", "C05", "session_id") and inspect the values. C05's session is None, so the match cannot be established. An invalid or missing field should lead to an **unknown** edge, not an automatic assertion that the two events are unrelated. Similarly, adding a shared account comparison would return equal labels but would not make the join trustworthy. A source validation request must ask the relevant owners whether identifiers are globally unique, reused, transformed or omitted along any route.

## 5. Use three competing mechanisms, not a favorite story

**H1: a scheduled job changed the wrong slot.** Supporting leads include the shared account, runner/client reference and batch-17 tag. However, C12's tag is self-reported, C06 visibly approves S40/S41 rather than S42, and no validated job-run-to-q-144 link is yet supplied. A minimum discriminator is an approved, bounded run record that names q-144 and lists the job's intended/authorized slots, accompanied by verified identifier semantics. A record containing a **different** request ID would challenge H1; a missing record would leave it unresolved unless completeness was independently established.

**H2: an unauthorized use of the shared identity caused the edit.** C07 allows for occasional emergency operator use; C05 reports an S42 edit and the visible approval omits S42. The hypothesis has multiple weaknesses: no validated session/request relation, no source showing an individual operator, no evidence of intent, and C11's claim of a possible late addendum. A discriminating request is a minimally scoped identity access trail and the authoritative change ledger for S42, under their respective custodians. A validated approval could challenge the "unauthorized" part but would not by itself prove which mechanism executed the edit.

**H3: the displayed S42 symptom does not represent current authoritative state.** C10 has unverified cache, capture clock and context, so the display could be stale or otherwise misleading. However, C05 still reports an edit, which H3 cannot erase. A minimum discriminator is a service-owner-authorized read-only comparison of current S42 state, version and last request ID against an independently obtained uncached, synthetic or privacy-limited client view. A matching incorrect backend value would challenge a purely display-only explanation; a correct backend state could narrow current service impact, not prove there was never a bad write.

H1–H3 are **not mutually exclusive**. A wrong-slot write could coexist with an outdated front-end view. Shared-identity misuse could occur through a scheduled task. A professional matrix should describe support, counterpoints and the **specific observation that would falsify a clause**, rather than assigning unjustified probabilities. The next action should reduce uncertainty relevant to a service or containment decision.

## 6. Rank evidence requests by decision value and acquisition risk

A good request is narrow enough to fail. Compare two candidate records.

**Request A: authoritative S42 state and last-change context.** Owner: application/service custodian after local approval. Scope: S42 only, selected status/version/last request ID and timestamp, minimal personal data. Decision value: whether an ongoing service state problem exists and how urgently a scoped intervention might be needed. Possible outcomes: currently wrong state; currently correct state; query unavailable/unauthorized; ambiguous version evidence. None has been observed at 09:26.

**Request B: preserved q-144 job-run and identifier semantics.** Owner: scheduler/job and application custodians under permitted case scope. Scope: interval surrounding 09:01, run ID, task, produced request ID, expected slot list and source-object reference. Decision value: whether H1 has a substantiated technical route. Possible outcomes: validated run/request match, mismatched run, missing fields or unavailable producer. No outcome has yet been received. A self-reported batch-17 string is insufficient.

C11's suggested change addendum is an important **separate targeted check** with the change authority. It does not eliminate the need to show actual behavior and state. These requests should be queued against acquisition urgency, privacy sensitivity, owner availability and potential change to response planning. "Export everything to investigate H2" increases risk while obscuring the exact decision at stake.

A decision table can ask: if S42 is wrong **and** a continuing harmful write is supported, prepare a scoped intervention proposal for Chapter 06; if state is correct and q-144 matches authorized work through a validated record, consider a documented downgrade review; if results remain missing, preserve unknowns, document the cost of additional collection and avoid broad changes without authorization. Those are **future branches**, not current observations or preapprovals.

## 7. Compare false causal certainty with actionable uncertainty

Bad conclusion: "At 08:58 attacker on runner-03 signed in as svc-enroll, used batch-17 to edit S42 at 09:01 and hid the approval." This asserts an attacker, device-to-session join, job origin, causal link and motive absent from C02–C12. C11's operator statement does not prove approval was hidden. Technical-sounding certainty is not the same as source-backed reasoning.

Good conclusion: "C03/C09 report s-77 and C09 associates a runner-03 client; C04 independently reports a runner browser at a corrected 08:58 estimate. C05/C12 report q-144 and a self-reported batch-17 tag. These items remain connected by leads rather than a validated session-to-request join. The visible approval omits S42, while a claimed addendum is unverified. Obtain approved S42 state and job/approval records before choosing a control."

The second conclusion is operationally stronger: the supervisor can identify the exact missing evidence and the proposed owners. It also protects later lessons from retroactively changing the Chapter 05 checkpoint. Mechanism, actor, intent and authorization are separate questions with distinct evidence requirements.

## 8. Write the 09:26 handoff as an approval-gated decision input

The handoff to Chapter 06 should be a **versioned snapshot** at 09:26, not a statement that containment was performed. It needs the case priority and why, observations with source IDs, unresolved alternatives, evidence quality gap, exact requests, actor-attribution limit and next decision gate.

Model handoff (approximately 165 words):

> At 09:26 CTN-IR-014 remains P2 provisional: C02 reports an enrollment symptom and C05 records an S42 edit through q-144, but the current authoritative slot state and extent of harm remain unverified. C03 reports s-77 at 08:58; C04's corrected runner event is temporally coincident, and C09's supplied rows name runner-03, without a validated session-to-request join. C09 also lacks original object/digest and collection-method metadata. C12 adds a self-reported batch-17 tag to q-144, not a validated job run. C06's visible approval covers S40/S41; C11 mentions a possible S42 addendum without supplying one. C10 depicts an unavailable UI, not authoritative state. Wrong-slot automation, unauthorized shared-account use and display mismatch remain open explanations. Request a service-owner-approved S42 state/last-change check and a custodian-approved q-144 job-run/source-ID comparison; request authoritative change scope separately. Do not identify a human actor or make a broad account change on this evidence. Reassess once these records arrive or new harm is observed.

This is a supervisor decision input, not a complete incident finding. It should have a revision identifier and a record of who received it. A reviewer should be able to follow every field back to its original card without external access.

## 9. EX021–EX025: deeper exercises and worked-answer supplements

**EX021 — Source-traceable timeline.** Objective: reconstruct what was known and when. Input: C02–C12. Required artifact: at least seven rows with raw/normalized event time, source, case receipt/release, claim and explicit limitation. Model core: C06 08:50 scope (retrieved 09:10); C04 08:54/08:58; C03 08:58; C02 about 09:00/09:04; C05 09:01; C09 08:58/08:59 rows received 09:18; C10 conditional 09:21/09:22; add C11 09:24 and C12 09:26. Two points require approximate/conditional time labels and chronology restrictions.

**EX022 — Join audit.** Objective: distinguish equality, hypothesis and validated causation. Input: C03–C05, C09/C12. Deliver a graph or table with **supported-in-supplied-source** edges C03↔C09 on s-77 and C05↔C12 on q-144, a candidate C09 runner-client relationship, and an explicitly **unsupported** s-77↔q-144 direct join. State how owners could validate shared identifier namespaces through a permitted known-good transaction. Two points require refusing human attribution and classifying the batch tag as self-reported.

**EX023 — Hypothesis matrix.** Objective: maintain three testable explanations. Input: C05–C12. For H1, H2 and H3 supply one source-based lead, one challenge, one minimally scoped discriminator and a predicted observation that would weaken it. Example: a verified q-144 producer other than the approved batch would challenge a simple H1 story; authoritative current S42 mismatch would challenge purely display-only H3. At 09:26 these are predictions, not received results. Two points require that negative search results do not automatically become proofs.

**EX024 — Minimal next request.** Objective: choose data by decision value, not volume. Input: 09:26 case ledger. Model request one to application/service custodian for approved minimal S42 state/version/last request; request two to job/application custodians for bounded q-144 producer/run relation. Identify approving role, purpose, selection limits, receipt expected and the branch affected by each possible result. Separately note the possible C11 addendum check. Two points require no unbounded dump and no assertion that either result has already arrived.

**EX025 — Professional handoff.** Objective: produce a 140–200-word decision-ready note. Input: EX021–EX024. The model paragraph above demonstrates a source-bound format. Scoring checks provisional priority, normalized times, conflicting explanations, incomplete C09 provenance, targeted requests, no malicious human attribution, no containment execution, and an explicit owner-review trigger. A two-point handoff remains usable even if a later card disproves its favored hypothesis, because it preserves the original evidence and conditional logic.

### Common mistakes and operational limits

- Using a single event-time sort to imply a responder could see data before release.
- Replacing a blank application session field with s-77 based on nearby time and the same account label.
- Treating the batch-17 tag as validated job execution or the C11 statement as an actual approved addendum.
- Declaring "no impact" because current state has not yet been checked, or "confirmed outage" from one screenshot.
- Preferring the hypothesis with the most suggestive labels instead of the one with an independently testable discriminator.
- Confusing a proposed control branch with its authorization, execution receipt or verified effect.
- Importing C13–C20 findings from the subsequent containment and eradication chapters into the 09:26 evidence set.

### Source and originality notes

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) provides response-in-risk-management context but does not prescribe CTN's hypothesis scores or action approvals.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) is historical IT-forensics guidance on examining and reporting digital evidence, not proof of a particular CTN source.
- All CTN case cards, the join graph, Python example and exercise scoring supplements are fictional original teaching materials. No production system, personal data or live credential is involved.

### Synthesis and handoff boundary

The completed five-chapter **draft sequence** has practiced readiness, authority, triage, evidence provenance and hypothesis testing. It has **not** established a human actor, executed containment, removed a cause, or restored service. Its usable outcome is a versioned 09:26 record with unresolved questions and owners. The next authored chapter introduces new cards and separate approval, execution and verification events; those events must not be backdated.

### Continue studying — Chapter 05 of 12 (integration draft)

[← Chapter 04](../MANUSCRIPT.md#ch-04) · [Chapter index](../../SUBJECTS.md) · [Canonical Chapter 05](../MANUSCRIPT.md#ch-05) · [Chapter 06 →](../MANUSCRIPT.md#ch-06)
