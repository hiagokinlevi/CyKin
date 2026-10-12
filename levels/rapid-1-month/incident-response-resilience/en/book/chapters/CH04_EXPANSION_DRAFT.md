# Incident Response and Cyber Resilience — Rapid Course
## Chapter 04 Expansion Draft: Guided Incident Simulation and After-Action Review

**Editorial status:** Unpublished English instructional expansion of Chapter 04 of the *single principal book*. This is a working chapter component, **not** another book, a separately completed lesson or a verified release.  
**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 04 of the current principal manuscript](../MANUSCRIPT.md#ch-04).  
**Original scope:** Facilitated decisions, staged evidence, assessment of six artifacts, audience-specific communication, reviewable handoff and measurable improvement.  
**Canonical sources:** [English chapter index](../../SUBJECTS.md), [book plan](../PLAN.md), and the [public book standard](../../../../../../BOOK_STANDARD.md).  
**Draft baseline:** The existing manuscript already contains the four-round tabletop, L2 reviewer comparison, F1 unavailable-approver replay and M1/M2 communication exercise. Preserve those and use the additions below selectively; do not duplicate their tables or count supplemental work as new numbered exercises.

> **Safety and provenance:** Harbor Library, all R-series evidence, facilitator injects, branch results and scoring packets are wholly synthetic. No activity involves a real library, real patron data, credentials, public notices or live system changes. All proposed controls and messages are classroom decisions unless a separately released fictional card explicitly reports a result. Primary sources cited below describe general practices, not events at Harbor Library.

# Chapter 4 — Original Teaching Expansion

### 4.A The tabletop as a controlled investigation of decisions

A tabletop is most valuable when it tests whether people can reason and coordinate under incomplete information, rather than rewarding a team for remembering the "correct" incident story. In a real response, a team rarely receives all records at the start. It must decide whether to preserve, request approval, restrict a path, protect business service or await a discriminating observation. The Harbor Library exercise recreates that decision pressure without granting any operational authority.

A facilitator should evaluate **what the learner could reasonably have concluded at each checkpoint**, not whether a final narrative agrees with a later branch. An exercise can show that a particular analysis was justified when made and later needed revision. This is not failure by itself; failing to preserve the earlier basis, hiding the new observation or pretending that later information was available all along is the more serious instructional error.

[NIST SP 800-84, *Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities*](https://csrc.nist.gov/pubs/sp/800/84/final) addresses how organizations design, conduct and evaluate such events. Its framework distinguishes tabletop discussion from functional exercises and technical tests. Here participants exercise analysis and communication against invented records. They do not demonstrate the actual effectiveness of Harbor Library's identity controls, log retention, backups or communications systems.

Before the first card, the facilitator defines an **exercise measurement contract** with five elements: capability being assessed, observable participant artifact, release boundary, success rule and an explicit nonclaim. For example: "The learner will distinguish proposed and approved containment actions from the reported execution of a later branch. The assessed artifact is the frozen Round C action card. A satisfactory card names the approver, target, service cost, fallback and verification plan. This tabletop cannot establish that any real session was revoked."

An instructor must resist moving the goalposts after seeing the learner's answer. If two options were explicitly allowed, the team should be scored on whether it analyzed the options within its authority and evidence, not on selecting the facilitator's favorite. The threshold should be declared before the round begins, and a changed rubric must be versioned as an editorial change rather than silently applied to earlier submissions.

The exercise also needs a stop rule: halt any participant who proposes opening a real account, exporting live patron records or communicating with actual users. Substitute an authorized fictional request card. A refusal to overstep scope is evidence of sound professional judgment, not reluctance to participate.

### 4.B Preserve both the event timeline and the knowledge timeline

The canonical sequence has four rounds and additional staged cards. The **event timestamp** printed in a record does not establish that the learner possessed it when that event occurred. The **release timestamp or phase** establishes when the evidence became available for the classroom decision.

| Frozen checkpoint | Available canonical records | Decision allowed | Important prohibition |
|---|---|---|---|
| Round A, 09:05 UTC | R1–R8 | Open the case, identify owners and ask whether B17/B18 changes were authorized training | Do not cite R9 despite its 09:03 event time |
| Round B, 09:20 UTC | R1–R16 | Update B19 hypotheses, request preservation and review retention uncertainty | Do not use R17's later training-owner statement |
| Round C, 09:37 UTC | R1–R24 | Propose a bounded containment action with approval, business-cost and verification fields | Do not claim the Branch S/P result or use P1/C1/V1 |
| Round D, first release | Either Branch S or Branch P, plus earlier canonical records | Evaluate the *reported branch action*, its service effects and remaining questions | Do not invent the other branch as concurrent production activity |
| Round D, subsequent release | P1/C1, then V1 as separately supplied exercise cards | Evaluate booking correctness, isolated access checks and audit attribution | Do not backdate these cards into Round C |
| Optional post-D replays | F1 or M1/M2 only when specifically released | Explore alternate authority or later communications decisions | Do not promote a replay into canonical evidence |

Within the fictitious Round D, Branch S reports at 09:45 that the identified `desk-a` session was revoked under fictional approval, the staff member must sign in again, and a narrow query shows no later edits within its range. It also says B19 remains incorrect. Branch P instead reports a 09:45 approved fifteen-minute staff-write pause and two pending manual-queue requests; ordinary writes must not be claimed resumed before an owner-reviewed decision. These cards are alternative exercise paths, not combined evidence of two simultaneous controls.

The learner should maintain two chronologies in parallel. The **source chronology** orders R1, R9, R18 and other source events by their printed times. The **availability chronology** states when each row was given to the learner. For example, R9's 09:03 edit belongs to the 09:20 Round B evidence release, while R18's 09:24 edit belongs to Round C. At 09:05, citing R9 is hindsight contamination even though its printed event time is earlier than 09:05.

At the end of each round, freeze a snapshot such as `HL-IR-001/C-action-v1` with the following metadata: round, simulated decision time, source IDs actually released, analyst's current observation and hypotheses, authority status, proposed action, unanswered question and next review condition. A later correction creates `v2` with a reason. Never replace `v1` in place: a reviewer must be able to compare the decision that was made with the knowledge then available.

### 4.C Facilitator discipline: meaningful injects, controlled variation

An inject is useful when it changes what the team could reasonably decide. Merely adding alarming words does not produce better learning. In the Harbor Library curriculum, each release has a defined question: Round A tests first-response boundaries; Round B tests B19 explanation and preservation urgency; Round C tests protective action versus legitimate service; Round D tests whether reported containment and later recovery checks support service acceptance.

The facilitator should prepare an **inject ledger** with: inject identifier, earliest release, factual content, expected decision affected, permissible source claims, prohibited inferences and fallback instructions when the learner asks for data not supplied. If an identity session detail is absent, a facilitator must not improvise a confirmed device or attacker. The appropriate reply is that the detail is unavailable in the current exercise and could be requested from a fictional custodian under the case's approval path.

A facilitator may ask a student to state the *minimum missing observation* that would change the proposal. At 09:20, a complete approved task-list addendum for B19 is more discriminatory than simply repeating a general suspicion. At 09:37, confirming the exact session-to-write relationship would affect how narrowly the team can target access, while R21's tolerability statement informs the business cost of a broader pause. An inject that resolves neither question should be recognized as context rather than treated automatically as heightened confidence.

Counterfactual branches require a reset. After Branch S, ask how the decision would differ under Branch P, but label the alternative as a **replay** and start from the same frozen Round C card. Otherwise the student may merge the reported revocation of Branch S with the two queued requests of Branch P and invent an impossible case record. A comparison can legitimately say that Branch S places more emphasis on session scope and staff reauthentication, while Branch P places more emphasis on paused writes, queue custody and resumption criteria.

The facilitator also should not reward a student for making a production-like change when the exercise permits only tabletop role-play. Instead, score whether the student specified the approval required, the exact target and a test that would detect both intended effect and legitimate-service harm. An explicit "execution not performed" field is a valid outcome.

### 4.D The six artifacts must form one coherent decision chain

The existing book requires a timeline, hypothesis table, action record, recovery plan, internal status message and improvement ticket. The artifacts are not six independent writing assignments: each has an input and output relationship with the others. A late inconsistency in one may reveal an earlier missing assumption.

**Artifact 1: Timeline.** Include the original source event time, release round and source ID. Its primary job is to prevent the analyst from proving causation merely through ordering or justifying an earlier decision with future evidence. Include a column for whether the item was actually available at the checkpoint. The timeline must not mix application activity with an interview note as if they had identical evidentiary semantics.

**Artifact 2: Hypothesis table.** Keep at least two explanations live, including authorized training and account use outside the approved plan; a display/state discrepancy may coexist with either. For each, identify supporting, conflicting or insufficient evidence and an authorized discriminator. An account label and a staff recollection are not human attribution.

**Artifact 3: Action record.** Separate recommendation, approval, execution and verification. In Round C, R19 says a session *can* be revoked and R21 says a staff-write pause is *tolerable*. Neither row confirms execution. The action record must include the expected protection, one legitimate-service negative check, uncovered routes, decision owner, fallback and review time. If an action is never executed in the round, leave its execution fields pending.

**Artifact 4: Recovery plan.** A plan is not a restore receipt. Before P1/C1 and V1 are released, its expected-state and tested-result fields must be labeled pending. After those separate later cards arrive, B19 and B20 do not match the P1 target, and V1's test audit lacks the actor despite its limited positive and denied-access observations. These failures prevent unrestricted acceptance. A later approved corrective operation and **new** comparison would be needed; nothing in these cards establishes that such a production correction occurred.

**Artifact 5: Status message.** Its audience and publication state matter. The exercise EX048 requests two internal sentences at the 09:45 branch result **before** P1/C1 and V1 are released; those later findings cannot be included. A separate post-D communication exercise can discuss the later mismatches because its evidence boundary is different. Label the two versions accordingly, and never transform a drafted message into a sent notice.

**Artifact 6: Improvement ticket.** A ticket closes a reusable capability gap, not the individual case symptom alone. Correcting B19/B20 addresses selected bookings. Testing the missing V1 audit actor or an outdated restore rehearsal addresses whether the next response can be investigated or recovered safely. A ticket needs a directly accountable owner, due date, test fixture, evidence artifact, pass/fail rule and procedure for a failed retest.

The six documents must agree on unresolved conditions. A status message claiming full recovery is inconsistent with a recovery plan that records failed booking and audit gates. A summary saying a session was revoked at 09:37 is inconsistent with the frozen Round C action proposal and the later 09:45 branch report. An evaluator should treat those as material reasoning defects, not stylistic differences.

### 4.E Evidence sufficiency is distinct from polished presentation

A learner may write a compelling narrative without identifying any source that could disprove it. Editorial evaluation should reward exact evidence boundaries over confidence of tone. An internally tidy timeline lacking release times can be dangerously misleading. A concise action card that names the missing approval is stronger than an elaborate plan written as though approval already exists.

The original six-output rubric uses 0 for absent or unsupported, 1 for incomplete, and 2 for specific, evidence-linked and properly bounded. A total of at least 9/12 with no critical zero for approval or evidence scope is a **classroom threshold**, not certification of a real system. The existing L2 calibration case illustrates how reviewer disagreement is settled using frozen artifacts rather than invented retrospective conversations. This expansion adds three assessment habits without repeating L2's score table.

First, **locate the contested field**. When one reviewer gives an action card 2 and another gives 1, ask exactly where the card states approval, affected service, execution status and fallback. "The learner told me verbally" does not repair a frozen written artifact unless the exercise explicitly recorded the statement as part of the scored submission.

Second, **distinguish a missing field from a contradicted finding**. A recovery plan that says "we still need an audit actor check" may be incomplete but honest. A plan that says "V1 proves the actor was captured" contradicts the supplied blank field; that is a substantive unsupported claim. Both may need revision, but they should not receive the same assessment merely because they are similarly short.

Third, **enforce a critical gate outside the arithmetic**. A high total cannot justify a response that invents authorization or crosses the release boundary. Record the total *and* whether evidence scope and required approval are defensible. An otherwise excellent packet that treats R21 tolerance as executed approval has not demonstrated authorized incident response.

Keep reviewers independent until they have identified the disputed evidence pointers. Then reconcile against the actual source and rubric. Document why a score changed, who made the decision and whether a new submission version was created. Do not edit the original score to erase disagreement. A score increase after the student revises is a new observation about the revised artifact, not proof that the earlier response was correct.

### 4.F Two correct branches can have different operational liabilities

Choosing Branch S or Branch P does not change the canonical pre-branch evidence. It changes what the learner must verify and hand off.

For **Branch S**, the reported session revocation is an observed *fictional branch action*, not proof of eradication. The narrow quiet query does not cover every route or time; staff reauthentication is a service effect. The next operator needs the identity-action scope and the process for restoring authorized staff access, while the service owner still needs to resolve incorrect booking state and the later V1 audit failure.

For **Branch P**, a fifteen-minute staff-write pause begins at the reported 09:45 branch checkpoint and creates two pending manual requests. Those requests are not accepted reservations. The service owner must assign custody, confirm each request identifier, assess conflicts with current state and authorize reconciliation before resuming writes. At 09:54 the planned fifteen-minute interval has not yet reached its 10:00 boundary; saying the pause expired and writes resumed would be unsupported. Even after 10:00, the planned end is not a verified resumption receipt.

A comparison worksheet should not ask simply "Which branch stopped the attack?" Neither branch establishes the cause, and an absence of matching audit rows could reflect limited coverage. Instead compare: protection aimed at, known service side effect, business owner, required post-action verification, unresolved routes, correction dependencies and risk of reversal.

A good reversal rule is observable. For Branch S, a verified unexplained booking change after the tested session revocation can trigger reassessment of other paths and proposed controls. For Branch P, an inability to reconcile queued requests or a failed business correctness check can block write resumption. Those are criteria for another decision, not automatic authority for a real intervention.

### 4.G An internal handoff must describe the *current* state, not just the history

At handoff, a new responder needs to know whether a restriction is still believed active, which observations were reported by a branch card, what later data tests failed and who can authorize the next change. An elegant incident history is insufficient if it omits those operational fields.

Use a state-oriented handoff packet:

| Field | Required content and failure to avoid |
|---|---|
| Case and checkpoint | `HL-IR-001`, current fictional round/time, and exact source release |
| Chosen branch | S **or** P, not both, with reported action time |
| Evidence inventory | R-series pointers, optional cards actually released, source limitations and access owner |
| Current control state | Named session action or staff-write pause, with untested routes and service effects |
| Business correctness | P1/C1 state only after release; list failed B19/B20 comparisons, not assumed repair |
| Access and audit | V1's limited passes and failed actor field only after release |
| Next authorization | Who may correct bookings, repair audit, resume writes or adjust a restriction |
| Revisit/rollback | Observable trigger, decision owner and next review—not a guaranteed resolution time |

A receiving analyst should be able to answer: "Can front-desk staff accept new reservations right now, and according to which supplied card?" In Branch P the answer must address paused writes and the pending manual queue; in Branch S it must address reauthentication, while noting that correct booking data is not established.

**Wrong handoff:** "The session was stopped, all bookings fixed, audit clean, incident closed." The branch can support a narrow session-action report but no production correction or audit pass. **Better handoff:** "Branch S reports the named session revoked at 09:45, with a quiet query limited to its selected range and staff reauthentication required. P1/C1 later shows B19/B20 differing from the approved target; V1 later reports two limited access results but a blank actor field. The service owner controls any correction and acceptance, the audit owner must retest attribution, and the incident lead maintains the next review; cause and other paths remain open."

The packet should include a *receiver challenge*: ask the successor to identify one claim they cannot verify from the handoff. If the receiver cannot locate a source, the sender supplies a pointer or narrows the claim. This reveals fragile handoffs while the exercise is still safe.

### 4.H Communications are acceptance-controlled artifacts, not reassuring prose

Different audiences legitimately require different levels of technical detail. The incident lead needs decisions and pending authorities. Front-desk supervisors need permitted operating workarounds. Patrons need an accurate, usable service instruction. The privacy contact needs sufficient provenance to assess an alleged data-access event. These are related messages but not interchangeable disclosures.

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) addresses coordination and communications in cybersecurity incident response and recovery. The audience matrix below is an original classroom adaptation; it does not decide legal notification duties.

| Audience | Useful content | Avoid | Approving or coordinating role |
|---|---|---|---|
| Incident lead and technical owners | Case ID, action status, exact evidence, failed acceptance checks, missing fields, next decision | An unexplained "all green" verdict | Incident lead and relevant source owners |
| Front-desk supervisor | Whether ordinary writes are available in the chosen branch, approved temporary workflow and escalation route | Account compromise claims or instructions beyond the supplied approval | Service owner and operational lead |
| Patrons | Potential room-booking discrepancy, practical *owner-confirmed* contact route and time of next update | Account names, other patrons' details, unsupported "fully restored" claims | Communications contact and service owner |
| Privacy contact | Scope and provenance of a specific allegation, sources to request and residual uncertainty | Treating a forwarded rumor as evidence of theft or R24 as permanent clearance | Privacy contact with incident lead |
| External or formal notification audience | Only facts approved under the organization's relevant obligations and procedures | Legal conclusions the exercise lacks jurisdictional and evidentiary basis to make | Designated communications, legal and privacy authorities |

A message is itself a controlled artifact with version, audience, approval, release time and superseded-version links. A draft is not an issued notice. When a fact changes after a message was actually sent, an authorized communications role would need to preserve the original and assess a correction; silently overwriting it destroys the history of what recipients were told. The fictional case supplies no record that an erroneous public message was sent.

### 4.I Work through the later communication replay without laundering rumor into evidence

Only **after Round D** does the optional M replay release M1 at 09:50 and M2 at 09:52. M1 is a front-desk supervisor's question about whether patrons can be told everything is restored. A question is not evidence of service recovery. M2 is an unattributed forwarded assertion that the newsletter list was stolen. Its origin, source system, occurrence time and evidence basis are missing; it establishes receipt of a claim, not unauthorized access.

R24, from 09:36, says no current record then established access to the newsletter or another personal-data store. That earlier bounded absence of supporting evidence is not a permanent guarantee that no access occurred. M2 does not prove the opposite. The privacy contact needs a narrow, authorized source-and-scope request, with the forwarded item preserved only as an unverified report.

**Incorrect patron draft:** "Our bookings are completely restored and your information was not affected." P1/C1 later contradicts complete booking correctness for B19/B20; V1 later fails audit attribution, and no complete exposure assessment has been supplied. The message claims much more than the available cards support.

**Safer patron-facing draft, subject to owner approval and confirmation of the contact route:** "We are reviewing discrepancies in some room bookings. If your booking appears incorrect, please use the library's confirmed assistance channel; the service team will review the details. We will provide another update after the next verification checkpoint." This provides an action without disclosing `desk-a`, naming an attacker or declaring closure.

**Restricted internal draft after the later cards:** "Branch S reports revocation of one identified session at 09:45. The current owner-approved booking comparison remains unresolved for B19/B20, and the isolated audit test lacks an actor identifier. The application and service owners are preparing limited verification; the privacy contact has an unattributed M2 allegation to assess with the incident lead. The next review is planned for 10:05." In Branch P, replace the session report with the write-pause and two pending queue items, and do not claim resumption at 09:54.

For a **privacy assessment request**, use the words "unverified forwarded statement" rather than "confirmed breach." Name the minimal sources that could determine whether any newsletter access or export occurred, source owner, time window, retention, approval and preservation requirements. The classroom has no jurisdiction, affected-person count or verified exposure facts from which to decide a statutory notification. Record who must assess applicable obligations if later evidence supports an incident.

### 4.J Use an after-action review to discover mechanisms, not blame people

An after-action review should explain **how the process produced its result**. "Communication was bad" is not a mechanism. "The internal status draft treated a proposed approval as an executed action because the handoff lacked an execution-status field" is a specific process failure that can be tested and corrected.

For each weakness, trace four steps:

1. **Observed exercise defect:** point to a frozen artifact or released fixture, not an impression of the discussion.
2. **Contributing condition:** state an assumption about why the defect occurred, then identify how it could be tested.
3. **Risk created:** name the decision or service that could be affected, without claiming an actual external loss.
4. **Corrective control:** define what will change, its owner, rehearsal input, pass condition and failure escalation.

For Harbor Library, V1's blank actor field is an observed failure of the *synthetic isolated test*. A hypothesis might be missing actor propagation through an audit mapping, but the exact mechanism is not supplied. A sound improvement ticket therefore calls for inspection and an isolated retest rather than confidently naming the root cause. The test should compare an authorized synthetic write, the expected actor and timestamp, and a denied unauthorized edit, preserving source and code/configuration version. A pass in one route covers that route and test only.

R23 motivates another independent improvement: backup-job status was available, but recent documented restore-test evidence was stale. A ticket should require a dated isolated restore of a named approved copy, measured start/end and an owner-approved data comparison. It should not promise that a backup can meet the RTO from its job-success status.

[NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) describes evaluation of exercises; [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) provides guidance for recovery planning, testing and improvement. Neither authenticates the Harbor Library fixtures or mandates the exact ticket fields used here.

### 4.K Improvement closure needs a measurable acceptance contract

An improvement ticket is not complete when a team marks a task "done." Completion should mean that the identified capability passed a defined test and a reviewer accepted evidence of the result. Prefer one owner and one verifiable weakness per ticket rather than an unbounded "improve the SOC" assignment.

A suitable ticket has: identifier; evidence pointer; risk statement; accountable owner; deadline; planned change; prerequisites; authorized isolated test; expected positive and negative outcomes; review owner; supporting artifact; and next action on failure. The ticket can remain open despite an implementation claim if the verification result is missing.

**Example — audit attribution**

- **Gap:** V1's isolated authorized booking test has a UTC timestamp but blank actor.
- **Owner:** application/audit owner; incident lead reviews closure.
- **Change:** identify and correct the missing synthetic actor-field propagation in the tested path.
- **Controlled test:** execute one approved fictional staff edit and one denied unauthorized edit in an isolated environment, capturing the application version, expected actor identifier, UTC event time, request key and authoritative state.
- **Pass:** the authorized record contains the expected actor and time and matches the declared write, while the unauthorized attempt is denied with state unchanged; the reviewer can reproduce the selection.
- **Fail:** actor remains empty, denied operation changes state, or source attribution/coverage is insufficient.
- **Interim measure:** a named owner performs restricted comparison and escalation until a passing test and explicit closure decision are recorded.

A failure should create a *new decision*, not force the score to pass. Record whether the defect was caused by the test setup, source mapping or incomplete instrumentation only after evidence supports the classification. A corrective-action ticket may legitimately close with a changed design and documented residual risk, but that is a distinct owner-approved decision—not a fabricated test pass.

For a restore-readiness ticket, require an actual isolated import and owner comparison; the mere presence of a backup file does not close it. For a handoff-readiness ticket, require a blind receiver to identify current branch status, approval state, failed gates and next action without asking the original analyst. The blind handoff is a measured learning task, not proof of future production performance.

### 4.L Design metrics that cannot be gamed by making the exercise easy

Measure outcomes rather than counts of meetings or pages. "All personnel attended training" does not show that an analyst can distinguish an unapproved action from a proposed one. "Ten backup jobs succeeded" does not show that one approved booking dataset can be restored correctly and on time.

Useful metrics for repeated, authorized exercises include the proportion of decision cards with exact source pointers, the share of approvals with separately documented execution status, the rate of handoffs that identify open booking/audit gates, and the percentage of improvement tickets closed by independently checked evidence rather than administrative status. Those metrics require clear denominators and consistent definitions. They should not be turned into a score when the sample is too small or the evidence is incomplete.

The facilitator can also measure **decision latency** from card release to a justified proposal, but speed alone is not success. A student who instantly labels `desk-a` compromised and orders account removal is fast and wrong. Another who accurately cites the evidence, names the approver and proposes a short review may be slower and safer. Record both timeliness and completeness. A high score in a tabletop cannot stand in for a technical test of a network, identity provider or recovery process.

For an improvement rehearsal, predefine an allowed response window and what constitutes an acceptable decision. Record the actual fictional start/end and whether the learner met *both* the time and safety criteria. Do not infer a real organization's response-level agreement or compliance posture from this classroom score.

### 4.M A final scenario can remain operationally open

A tabletop may end while the fictional incident remains unresolved. That is a valid learning result when the packet makes open questions actionable.

In Branch S, the narrow revoked-session report does not prove which person previously edited bookings. In Branch P, the pause and manual queue do not prove that writes will be safe after resumption. After P1/C1 and V1, B19/B20 correctness and audit attribution are still failed acceptance criteria in the supplied test record. Neither branch establishes a completed production backup restore, full access coverage or a universal absence of data exposure.

The student should state what would close each open item: source, owner, authorized test, pass/fail outcome and review deadline. A final status may therefore be "tabletop concluded; response handoff and corrective actions open" instead of "incident recovered." That distinction respects both the learner's achievement and the limits of the fictional evidence.

Before handing in the final packet, run a **contradiction review**: Does the status message promise recovery while the data table fails? Does the action card imply approval from R21 alone? Does the final timeline use R9 at 09:05 or R17 at 09:20? Does a privacy message repeat M2 as fact? Does the improvement ticket claim a test passed when only a proposal exists? Resolve these as explicit revisions, preserving earlier snapshots. This final consistency check is often more educational than adding another paragraph of incident narrative.

---

## New Offline Laboratory — F4-AUDIT: Artifact Release and Assessment Gate

**Purpose:** Demonstrate that a six-artifact packet can score well yet fail a critical approval gate, and that a later release cannot repair an earlier frozen decision. This is a new classroom-only evaluator; it does not repeat the manuscript's L2 scoring case, F1 unavailable-approver rehearsal or M1/M2 message-generation activity.

**Environment:** Python 3 standard library, in memory. No network, files, credentials, messages or state changes. All sample scores below are invented teaching input. They are *not* grades given to a real learner.

**Procedure:** Before running, predict which references are in scope for each checkpoint; identify the prohibited future reference and mixed-branch example; then predict whether an improved 11/12 packet would pass if its approval evidence were missing. Run the code and compare the exact transcript.

~~~python
LEVEL = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D_BRANCH": 4,
    "D_TARGET": 5,
    "D_ACCESS": 6,
    "M_REPLAY": 7,
}

RELEASE = {
    **{f"R{i}": "A" for i in range(1, 9)},
    **{f"R{i}": "B" for i in range(9, 17)},
    **{f"R{i}": "C" for i in range(17, 25)},
    "S": "D_BRANCH",
    "P": "D_BRANCH",
    "P1": "D_TARGET",
    "C1": "D_TARGET",
    "V1": "D_ACCESS",
    "M1": "M_REPLAY",
    "M2": "M_REPLAY",
}

def validate(snapshot, refs):
    if "S" in refs and "P" in refs:
        return "BRANCH_CONFLICT"
    unknown = sorted(set(refs) - set(RELEASE))
    if unknown:
        return "UNKNOWN:" + ",".join(unknown)
    future = sorted(
        r for r in refs
        if LEVEL[RELEASE[r]] > LEVEL[snapshot]
    )
    return "FUTURE:" + ",".join(future) if future else "IN_SCOPE"

SAMPLES = [
    ("A-timeline", "A", ("R1", "R4")),
    ("B-hypotheses", "B", ("R9", "R10")),
    ("C-action", "C", ("R18", "R21")),
    ("D-status-S", "D_BRANCH", ("S",)),
    ("D-recovery", "D_ACCESS", ("P1", "C1", "V1")),
    ("D-improvement", "D_ACCESS", ("V1",)),
]

for ident, stage, refs in SAMPLES:
    print(f"{ident}: {validate(stage, refs)}")

NEGATIVES = [
    ("NEGATIVE_FUTURE_BRANCH", "C", ("R18", "S")),
    ("NEGATIVE_PREMATURE_RECOVERY", "D_BRANCH", ("S", "V1")),
    ("NEGATIVE_MIXED_BRANCHES", "D_BRANCH", ("S", "P")),
]

for ident, stage, refs in NEGATIVES:
    print(f"{ident}: {validate(stage, refs)}")

def score(values, approval_ok, scope_ok):
    total = sum(values)
    if not approval_ok or not scope_ok:
        return f"{total}/12 HARD_GATE_FAIL"
    if total >= 9:
        return f"{total}/12 CLASSROOM_THRESHOLD_MET"
    return f"{total}/12 REVISION_REQUIRED"

print("FROZEN_V1:", score((2, 1, 1, 1, 2, 1), True, True))
print("REVISED_V2:", score((2, 2, 2, 1, 2, 2), True, True))
print("NEGATIVE_NO_APPROVAL:", score((2, 2, 2, 1, 2, 2), False, True))
~~~

### Exact expected output — executed with Python 3

~~~text
A-timeline: IN_SCOPE
B-hypotheses: IN_SCOPE
C-action: IN_SCOPE
D-status-S: IN_SCOPE
D-recovery: IN_SCOPE
D-improvement: IN_SCOPE
NEGATIVE_FUTURE_BRANCH: FUTURE:S
NEGATIVE_PREMATURE_RECOVERY: FUTURE:V1
NEGATIVE_MIXED_BRANCHES: BRANCH_CONFLICT
FROZEN_V1: 8/12 REVISION_REQUIRED
REVISED_V2: 11/12 CLASSROOM_THRESHOLD_MET
NEGATIVE_NO_APPROVAL: 11/12 HARD_GATE_FAIL
~~~

**Interpretation:** The first six rows confirm only that each displayed reference is *permitted in that stage*, not that the artifact's interpretation is correct. The first negative control rejects Branch S as evidence in Round C. The second rejects V1 at the first Branch S release; P1/C1 and V1 must enter later. The third detects mutually exclusive Branch S and P reports incorrectly combined as one case path.

The frozen example totals 8/12, below the declared classroom threshold. The revised example totals 11/12 and meets the *numeric classroom* threshold if the explicit approval and evidence-scope checks also hold. Removing the approval evidence yields `HARD_GATE_FAIL` even though the score remains 11/12. The program does not decide whether a source is authentic, whether an action was truly approved or whether a recovery criterion passed: `approval_ok` and `scope_ok` are assumed input flags to be justified by a human reviewer with evidence.

**Negative test:** Change `("D-status-S", "D_BRANCH", ("S",))` to include `"V1"` and observe `FUTURE:V1`. Restore the original tuple before interpreting the baseline results. A correct result proves only that the classroom release rule was enforced by the script, not that a real system is secure.

**Required learner artifacts:** the exact twelve-line transcript; a six-row artifact table with checkpoint, references, proposed score, evidence pointer and one missing field; a short explanation of the approval hard gate; and a versioned correction of one deliberately premature claim. The learner must not modify actual incident records or contact an outside system.

**Assessment:** Award one point each for exact transcript, correct future/mixed-branch reasoning, separation of score from critical gate, versioned non-backdating correction and explicit explanation that a tabletop score does not verify production containment/recovery. The lab is supplemental; no new numbered exercise ID is created.

---

## Targeted Refinements to Existing Exercises

Retain the existing EX039–EX050 sequence and 0–2 numbered-exercise rubric. Add only the following six deeper checks and incorporate their answers into the final worked-results appendix of the single book when approved.

### EX041 — Evidence chronology

**Add to the prompt:** Require both a source-event timeline and an explicit release/availability note for each of the six rows. Ask the learner to mark a hypothetical erroneous sentence, "At 09:05 we already knew B19 changed at 09:03," as invalid and rewrite it without introducing new facts. A full-credit answer must keep R17/R18 unavailable to Round B and must not equate event order with identity or causation.

### EX044 — Decision checkpoint

**Add to the prompt:** Include four distinct state labels—proposed, approved, executed, verified—for the chosen control at the 09:37 checkpoint, with "pending" where no corresponding receipt exists. Specify one protective test, one legitimate-service negative check, the uncovered path and the service owner who may authorize rollback/resumption. Explain why R21 tolerance does not satisfy the approval field. Score 2 only if no later Branch S/P result is cited at this checkpoint.

### EX047 — Recovery acceptance

**Add to the prompt:** Once P1/C1 and then V1 are explicitly released, give each of the original four acceptance criteria a result state of limited pass, fail or not tested, **plus** the source card that supports it. Require a named owner for each failed gate and a condition for time-bounded restricted operation or refusal of unrestricted return. A status of "fully restored" fails regardless of presentation quality if B19/B20 discrepancies or the blank audit actor remain uncorrected.

### EX048 — Internal update

**Add to the prompt:** Preserve the exact two-sentence constraint **at the 09:45 branch-only checkpoint**, before P1/C1/V1. Include the operational side effect specific to the chosen branch, a next decision owner and a statement of unresolved cause/impact. Ask the learner to separately identify one sentence that would be impermissible because it relies on a later card. Do not merge the optional M1/M2 replay into the original EX048 update.

### EX049 — Improvement ticket

**Add to the prompt:** Require an accountable owner, due date, input fixture, one positive acceptance observation, one negative failure control, the receipt a reviewer will inspect, and a reopened-work condition. Choose **one** program gap—the V1 actor field or the R23 restore-test readiness—not the correction of an individual booking. A ticket cannot be closed by the words "fixed" or "policy updated" without measured evidence.

### EX050 — Final handoff and self-assessment

**Add to the prompt:** Name the exact chosen branch; distinguish reported branch execution from Round C proposal and from still-pending booking corrections; present the six-output 0–2 self-score and approval/scope critical gates separately. Include a contested-score note pointing to one frozen artifact and explain how a later revision is linked without rewriting the original. A full-credit answer is possible even if the overall classroom packet falls short of 9/12, provided the learner reports the failure and necessary revisions accurately.

---

## Supplementary Worked Answers — Final Appendix Placement

### EX041 — Expanded worked reasoning

The source chronology may contain R1 (08:40, Round A), R4 (08:44, Round A), R9 (09:03, Round B release at 09:20), R15 (09:14, Round B), R18 (09:24, Round C) and R21 (09:29, Round C). The correct sentence is: "R9 describes a B19 edit with event time 09:03 UTC, but the learner first received R9 in Round B at 09:20; therefore R9 could not support the 09:05 Round A decision." R17 and R18 were not available for the Round B assessment. Chronology alone cannot identify who operated `desk-a` or prove that one event caused another. The student should retain both the original source time and release checkpoint.

### EX044 — Expanded worked reasoning

At 09:37, R17 limits the known approved training list, R18 records B20 changed, and a narrower revocation can be **proposed**. The incident lead and identity owner are required for approval under the fictional role rules, but no Round D execution receipt has yet been released. The identity administrator would act only after approval. A proposed protective check would inspect denial of the identified session and later bounded booking-audit coverage; a legitimate-service check would confirm necessary staff reauthentication and booking continuity. Other sessions and application faults remain outside the narrow scope. R21 expresses service-owner tolerance for a short pause, not signed approval, execution or proof of effectiveness. Branch S/P must not be imported backward. Execution and verification fields remain pending until appropriately staged evidence exists.

### EX047 — Expanded worked reasoning

Only after the later Round D cards are released: P1/C1 shows B17 and B18 matching the approved target but B19 and B20 mismatching. The booking-correctness acceptance check therefore **fails** for the supplied restricted comparison. V1's authorized synthetic test booking and denied unauthorized edit are **limited passes** for those tested identities and paths, not for the complete live service. V1's audit record contains a UTC time but blank actor, so audit attribution **fails**. The service owner must approve any booking correction and a new comparison; the application/audit owner must repair and retest the actor field. The incident lead and service owner may *propose* a restricted mode with documented compensating checks and review time, but the cards do not justify unconditional return. Another unexplained edit or unreconciled queue item is a potential reassessment trigger.

### EX048 — Expanded worked reasoning

**Branch S, exactly two sentences at the branch-only 09:45 checkpoint:**

> "At 09:45 UTC, Harbor Library is reviewing unexplained booking changes, and the fictional identity administrator reports that the identified `desk-a` session was revoked under the exercise approval; the staff member must sign in again. The incident lead and service owner will review the bounded booking evidence and operational impact at the next checkpoint, while the operator of the earlier edits, full booking correctness and wider cause remain unconfirmed."

**Branch P, exactly two sentences at the branch-only 09:45 checkpoint:**

> "At 09:45 UTC, Harbor Library is reviewing unexplained booking changes, and the fictional service owner reports a fifteen-minute staff-write pause with two requests pending in a manual queue. The incident lead and service owner will check the write restriction and queue before any approved resumption decision, while the cause and complete patron impact remain unconfirmed."

Both drafts exclude P1/C1 and V1 because EX048 occurs before those cards are released. "V1 proved the audit actor" would be both premature and contradicted by the later card. These are internal drafts, not real or issued public messages.

### EX049 — Expanded worked reasoning

An acceptable single-gap ticket is `IR-IMPROVE-AUDIT`. Evidence pointer: V1's isolated authorized edit includes a UTC time but blank actor. Accountable owner: application/audit owner; the incident lead reviews closure. Due date: 30 days after the fictional tabletop, subject to owner acceptance. Change: identify and correct the actor-field propagation in the isolated audit path. Interim measure: named reviewer performs restricted comparisons of authorized test changes and escalates unexplained state while attribution remains incomplete. **Positive test:** a controlled authorized synthetic edit produces matching request, expected actor, UTC time and accepted state. **Negative test:** an unauthorized synthetic edit is denied with state unchanged; a deliberately omitted actor field causes the acceptance check to fail. Closure requires retained test inputs, source/version, output, reviewer and explicit pass; a missing actor or unavailable source reopens work. Correcting B19/B20 alone would not close this repeatable auditability gap. A restore-readiness ticket based on R23 is also valid if it independently measures an isolated recovery and checks data correctness rather than relying on a backup-job notification.

### EX050 — Expanded worked reasoning

A valid Branch S final handoff records that the 09:37 action was **proposed**, whereas Branch S subsequently reports the narrow session revocation at 09:45 under fictional approval. The branch's quiet query remains limited to its unspecified coverage. Later P1/C1 demonstrates unresolved B19/B20 booking discrepancies; V1 demonstrates narrow access passes but an audit actor failure. No production correction, complete restore or identified human actor is supplied. The service owner owns booking-state acceptance, the audit owner owns attribution retest, and the incident lead owns further restriction/review decisions.

A defensible six-artifact self-score for an explicitly *hypothetical revised learner packet* could be Timeline 2, Hypotheses 2, Action 2, Recovery 1, Status 2, Improvement 2, totaling **11/12**—but only if its actual frozen artifacts support those scores and the critical approval/scope gates pass. This is not a grade preassigned to the real learner. If the action record lacks explicit approval, the critical gate fails despite the total. If recovery claims "complete" contrary to P1/C1 or V1, the recovery score must be reduced and the claim corrected. A reviewer disagreement is resolved by locating the missing source or field in the frozen artifact and submitting a named `v2`; later evidence must never be inserted into a Round C `v1` decision.

---

## Section Synthesis and Continue Studying

The Harbor Library tabletop succeeds as education when the learner can keep each observation within its release boundary, compare decisions without manufacturing approval, maintain separate protection and business-service checks, communicate honestly with different audiences and close improvement actions only through verified tests. The scenario is not resolved by the last discussion round: incorrect booking comparisons, failed audit attribution, uncertain cause and untested wider routes remain as documented follow-up work.

### Continue studying — chapter 04 of 04 (expansion draft)

[← Chapter 03 of the principal manuscript](../MANUSCRIPT.md#ch-03) · [Course chapter index](../../SUBJECTS.md) · [Principal book and worked results](../MANUSCRIPT.md#answers) · [Next course via the chapter index](../../SUBJECTS.md)

**Editorial note:** This file is a draft component of the existing English book, not a new principal book. Its supplemental laboratory and revised scoring tasks do not increase the canonical count of EX001–EX050. The public manuscript, actual A4 page count, technical review and publication status require separate editorial integration and verification.

### Primary sources and rights

- [NIST SP 800-84 — Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final). Final September 2006; exercise design, conduct and evaluation. Its date and older examples require contextual review for contemporary use.
- [NIST SP 800-61 Revision 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Final April 2025; incident response, coordination and recovery within cybersecurity risk management.
- [NIST SP 800-184 — Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final). Final December 2016; recovery planning, testing and improvement.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework). Framework-level risk management outcomes; it does not prescribe Harbor Library's event sequence, rubric or approval forms.

The cited sources support general educational methods and factual context; they do not authenticate any invented R-series item, branch, review score, communication or G3/F4 laboratory result. The original teaching material is attributed editorially to hiagokinlevi in accordance with the [CyberABC rights notice](../../../../../../RIGHTS.md); third-party works retain their rights. No real-system access, invasive activity or published legal notification is proposed.
