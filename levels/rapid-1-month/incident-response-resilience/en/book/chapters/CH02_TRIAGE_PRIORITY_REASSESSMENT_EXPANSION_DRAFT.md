# Incident Response and Cyber Resilience — Rapid Course

## Chapter 02 Transitional Expansion Draft: Reassessing Triage Priority Under Changing Evidence

**Editorial status:** **Public transitional English teaching component** for Chapter 02 of the **single principal book**; not another chapter, a completed book, a NIST incident-severity standard, or a verified incident report.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 02 — Alert triage and evidence preservation](../MANUSCRIPT.md#ch-02), particularly §2.2.  
**Specific learning gap:** Reassess a provisional response priority when source records become available at different checkpoints, an apparently quiet query has unspecified coverage, business harm is reported but not independently verified, or preservation may become time-sensitive even though malicious cause and attribution remain unproven.  
**Existing lessons retained:** R1–R16 source tables and the H1/H2/H3 explanations; E1 byte integrity; T1/T2 temporal and ingestion examples; VQ2 query-envelope logic; IM2 impact counts; HOLD2 source-hold verification; MIN2 review-field minimization; the Chapter 03 RB3 reversal exercise; and the original 50 numbered exercises and answers. This draft adds **a decision-time reassessment record**, not another query/hold/impact test.

> **Fiction, authority, and source-release boundary:** Harbor Library is fictional. Round A offers R1–R8 at 09:05; Round B offers R1–R16 at 09:20, even though R9's reported event time is 09:03. R17–R24 and all Branch S/P, P1/C1, V1, W1, MQ3, RTE3 and RB3 cards are unavailable to either checkpoint. The independent **TRI2** laboratory introduces invented variant flags and hypothetical outcomes only; it creates **no new R-series observations**, authorizations, evidence copies, source holds, verified recovery states or human attribution.

# Chapter 02 — New Teaching: Reassessment Without False Precision

### 2.2a.1 Why a priority decision must be revisable

The existing §2.2 distinguishes potential harm, time sensitivity, and confidence using a small qualitative matrix. That is a sound starting point, but an analyst needs to know **how to revisit all three dimensions when information changes**. A record can have an earlier event timestamp yet arrive later. A new source may support a previously uncertain fact while leaving its cause unknown. Evidence can become harder to preserve even while there is no proof of an attacker. A service owner may verify a booking-state mismatch without establishing who caused it.

Priority should therefore be written as a **checkpoint-specific recommendation**, not as a permanent label attached to a ticket. A useful note tells the incident lead what is concerning now, what can be lost through delay, which important claims remain weak, who owns the next authorized check, and which observation would require reassessment.

A provisional priority is not the answer to "Did a cyberattack occur?" It is an answer to "Which bounded response work deserves attention next, given the evidence and operational risk available at this checkpoint?" The answer can remain time-sensitive without attributing malicious conduct, and it can be revised without concealing the earlier reasoning.

[NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) explains incident response as part of cybersecurity risk management and emphasizes organizational context. [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) provides flexible high-level outcomes for understanding, assessing, prioritizing and communicating cybersecurity risks. Neither establishes the specific categories, labels or decision thresholds in this exercise. **TRI2 is an original CyberABC method** for teaching bounded reassessment, not a NIST-defined incident classification or automatic containment policy.

### 2.2a.2 First freeze what the analyst actually knows

Before comparing possible harm or urgency, identify the **decision checkpoint and released sources**. Otherwise an apparently precise priority record may rely on information the earlier responder did not have.

At 09:05 the learner has R1–R8: R1 reports the `desk-a` sign-in, R3/R4 report B17/B18 edits, R5 records a patron concern, and R6 reports scheduled training. R7 is a backup-job status and R8 a network summary without destination detail. These records support investigating the booking changes and training explanation. They do not prove unauthorized account control, restore success, information transfer, or a broad population impact.

At 09:20 R9–R16 become available. R9 reports a B19 edit whose event time was 09:03, R10 lists B17/B18 in the supplied plan but not B19, R11 records a second patron report, R12 provides a staff recollection, R13 a limited identity summary, R14 an application-audit quiet-query summary, R15 a 24-hour deletion notice without a known anchor, and R16 a service-owner request for impact assessment before account change.

The correct interpretation is not that the Round A analyst ignored R9. The learner did not receive it until Round B. In the review ledger, preserve **reported event time**, **learner availability time**, and **decision time** as different fields. A reviewer should be able to reconstruct the 09:05 decision from only the then-released records.

The TRI2 code checks this boundary. A deliberate attempt to cite R9 during Round A is rejected before any interpretation or priority discussion occurs. That output represents a classroom release rule; it is not a statement that the underlying event did not occur.

### 2.2a.3 Confidence is not one number

A single "confidence: medium" label mixes several logically independent questions. A beginner can reason more accurately by writing three separate fields:

1. **Confidence in the record as supplied:** Is the named item present in the released classroom packet, with a source and stated content? In a live case this would additionally require relevant source authentication and collection/provenance review.
2. **Confidence in interpretation:** Does the record support the asserted business or security meaning? A booking edit may be recorded accurately while its authorization remains disputed.
3. **Confidence in cause and attribution:** Does available evidence connect the operation to a specific causal mechanism or person? A staff account label or nearby sign-in time is not human attribution.

These fields can move differently. At 09:20 the *record* of the B19 edit is now available; the *interpretation* that it was unauthorized remains unsettled because a training-plan omission is not proof that no other approved instruction existed; and the *identity* of the operator is not established by R13's limited summary.

A useful report states these as separate sentences:

> "R9 is a supplied synthetic booking-audit record describing a B19 change. The approved scope of that operation remains unresolved because the supplied plan lists B17/B18 but not B19. The human controlling the session is not established."

This is more useful than labeling the entire case "high confidence" without saying confidence **in what**. It also prevents another error: downgrading every field just because attribution is weak. A patron-facing booking problem can require action even when the cause is unknown.

TRI2 uses descriptive statuses rather than calibrated probabilities. The code cannot authenticate any real source or measure an actual probability of compromise, and its labels must not be interpreted as a universal confidence scale.

### 2.2a.4 A record can be reliable while the hypothesis remains weak

An analyst sometimes treats independent evidence as a vote: three records agree, therefore the cause is established. But agreement depends on **what proposition the sources actually address**. R9 describes an application edit; R10 is a training-plan document; R12 is a staff recollection. These do not measure the same fact. Their differing contents can legitimately strengthen the need for an authorization check without proving account theft.

Consider three statements:

- "The supplied booking-audit row reports a B19 edit."
- "The supplied training plan omits B19."
- "An unauthorized person used the staff account."

The first two follow from the records' stated contents. The third is a causal attribution and does not follow automatically. An incomplete training plan or forgotten approved task remains a possible explanation; neither alternative is itself confirmed.

**Conflicting signals should increase attention to the discriminator**, not force the team to choose one story immediately. The training owner might provide a dated, approved addendum; a source custodian might supply reliable session-to-request mapping; the service owner might confirm a current booking mismatch. Each has a different purpose.

A full, owner-confirmed task list that includes a particular booking could reduce concern that *that booking's task* was outside the plan. It still does not prove the human operator, establish every booking state, or resolve evidence-retention risk. A separate valid observation is required for each stronger claim.

### 2.2a.5 Potential harm and verified impact are different dimensions

A patron report is evidence of a reported problem, not automatic proof of an incorrect authoritative reservation value. At 09:05, R5 records a concern about B18. At 09:20, R11 adds a B19 concern, but neither record provides an owner-approved comparison of current versus expected booking values.

A **potential-harm note** asks which business function could be affected if the concern is accurate: patron scheduling, room availability, front-desk integrity or continuity of reservations. It may require quick attention when the full impact is unknown.

A **verified-impact note** requires a different type of source: an authorized current-state observation compared with an accepted target, with scope and provenance adequate for the question. Its conclusion is still limited to the objects actually checked. It does not magically establish how many people were affected.

The IM2 laboratory already teaches that report counts, event counts, booking IDs and people are distinct units, and that a biased subset cannot estimate the whole population. TRI2 does **not** recalculate those counts. It teaches what happens to a *priority recommendation* when a bounded impact check is actually supplied or remains missing.

For example, a future **independent synthetic variant** in which an owner-approved comparison confirms a mismatch can justify revisiting potential business harm. That observation cannot be inserted into canonical R1–R16, which contains no completed authoritative state comparison.

At both checkpoints, the correct discipline is to state: potential consequences are being assessed; measured impact remains unknown unless an appropriate source has actually verified it.

### 2.2a.6 Split time sensitivity into preservation and containment concerns

The original matrix places multiple urgent issues in one time-sensitivity column. For decision making, it helps to track **two independent urgency questions**.

**Preservation urgency** concerns whether a decision-relevant source may become unavailable if the team waits. It depends on source retention, availability, owner response, collection authority and any verified preservation control. The clock can matter even if the initial interpretation is wrong.

**Containment urgency** concerns whether additional harmful activity is sufficiently plausible or observed to justify prompt consideration of protective options. It depends on signs of continued activity, current impact, confidence in control scope and possible damage from the intervention itself. A short log-retention period does not, by itself, prove a new harmful edit or authorize account restriction.

At 09:20, R15 raises preservation concern: detailed booking-audit records are deleted after 24 hours unless an authorized copy is retained. The **policy anchor is unknown**. The appropriate response is to seek a bounded source-availability/preservation decision and obtain the custodian's explanation promptly, not to publish a precise countdown calculated from R9's event time.

At that same checkpoint, R9 and R11 merit investigation and continued review, but there is no **post-09:20 newly verified edit** in the released record. R14's quiet result is limited to an unspecified query range, and cannot establish that no additional activity occurred. The incident lead therefore needs a review trigger and a plan for authorized escalation without describing a containment operation as already needed or performed.

A team may honestly say that evidence-preservation contact is time-sensitive while its cause attribution remains low or unproven. Those statements do not conflict.

### 2.2a.7 A quiet query is not a negative observation until its scope is understood

A common reassessment error is:

> "The dashboard shows no new alerts, so lower the priority."

That may be reasonable only after the observer establishes what the query measured. For R14, the supplied card says no further booking edits appear after R9 **within the queried range**. It does not provide all the source, account, time, ingestion and completeness details needed for a universal absence claim.

A query might use an interval that excludes the time of interest, an account filter that excludes another path, a source that does not include the relevant operation, or a log store that has not finished ingesting records. The absence of a returned row is therefore narrower than "no new edit occurred."

VQ2 already teaches query-envelope conditions, and T2 demonstrates delayed arrival. The present lesson does not duplicate those mechanics. It asks what a response lead should do **with** an imperfect negative observation: leave the containment concern open for review and request the missing query manifest or better-bounded observation through the authorized custodian.

A *valid negative result* can narrow the concern for a specified tested path and interval. Even then, it cannot prove the absence of malicious behavior on every route, and it does not establish human attribution or solve a preservation problem. The reduction must be scoped to the proposition that the negative test could actually refute.

TRI2 emits `QUIET_NOT_NEGATIVE_PROOF` when a case relies on an apparently quiet summary whose coverage is not established. That warning does not claim that a new edit occurred; it prevents the unsupported opposite conclusion.

### 2.2a.8 How to write an evidence-changing review checkpoint

A useful priority note is not merely a timestamp followed by a color. It should answer these seven questions:

| Question | What belongs in the provisional note |
|---|---|
| What was available? | Checkpoint and exact released source IDs |
| What could be harmed? | User/service outcome and scope, marked potential or verified |
| What does each confidence field mean? | Record availability, event interpretation and cause/attribution separately |
| What could be lost through waiting? | Source retention or continuing-activity concern, with explicit missing anchors |
| What is proposed next? | One bounded, authorized information request or decision review, not automatic execution |
| Who owns it? | Incident lead, service owner and/or relevant custodian according to the request |
| When must it change? | Named review time or an observable event that triggers earlier reassessment |

For Round A, a classroom answer may favor **prompt review** with the training owner and a 09:15 checkpoint, without concluding compromise. This is justified by R1–R8's booking changes, user report and scheduled training. It is not a claim that the organization adopted a numbered severity category.

For Round B, the incident lead can keep a prompt, bounded review at **09:35 or earlier on a verified new unexplained edit or material source-availability concern**. The newly released B19 edit increases the need for explanation; R15 separately raises preservation urgency. The next proposed step may involve asking the application custodian for the retention anchor and feasibility of P-A, plus a service-owner-approved impact check.

The note should distinguish "will request" from "requested," "approved," "collected" and "verified." None of those latter states is supplied for a real Round B collection or hold. An attractive priority label cannot substitute for authorization.

### 2.2a.9 Example one — correct 09:05 assessment without hindsight

**Correct record, canonical Round A only:**

> "At 09:05 UTC, Harbor Library's supplied R1–R8 records report a desk-a sign-in, booking edits to B17/B18 and a patron concern about B18. R6 records scheduled training but does not show that those particular edits were approved. The potential service consequence warrants prompt review; there is no verified broad impact, human attribution or demonstrated ongoing attack. The incident lead proposes asking the training owner for the approved task list and preserving the current synthetic records within the classroom scope, with a review at 09:15 or sooner if a separately verified new unexplained edit is supplied."

This note has a specific checkpoint, source set, service concern, interpretation limit, proposed authorized next question, owner and review. Its **confidence in the case records being supplied** is not the same as confidence that the changes were unauthorized. R7's completed backup job and R8's limited network summary do not settle the cause.

A reviewer must not say that the 09:05 lead already knew B19 was changed at 09:03. R9 is released only at 09:20, and its event timestamp cannot backdate its availability. A retrospective discussion can identify that later source as new information but must preserve the earlier decision's actual basis.

Neither the original note nor the comparison claims a real identity operation, account restriction, source copy or production log review. The phrase **prompt review** is a locally reasoned fictional priority description, not a NIST-prescribed severity grade.

### 2.2a.10 Example two — incorrect 09:20 downgrade

**Incorrect synthetic Round B handoff:**

> "R14 shows no edits after B19, so the issue is over. R12 cannot remember B19, which proves a thief used desk-a; nevertheless the case can be marked low because no further alarms were seen. R15's 24 hours means we have until exactly 09:03 tomorrow to export the evidence, and R11 proves another patron's booking was corrupted."

This text simultaneously overstates a negative query, fabricates a human attribution, invents a retention anchor and equates a patron report with an authoritative business-state mismatch. It cannot support a defensible downgrade. The contradiction between "proved theft" and "case over" also shows why a single severity label is not useful without specific evidence claims.

**Corrected bounded Round B assessment:**

> "At 09:20 UTC, R9 adds a B19 booking edit whose event time was 09:03; R10's supplied training plan names B17/B18 but not B19, while R12 is an unverified recollection about the action. The account operator, approval and root cause remain unresolved. R11 reports a patron concern but does not measure current booking correctness or population impact. R14 is a quiet summary with incomplete query coverage, and R15 reports a 24-hour source policy with no confirmed anchor. The incident lead keeps a prompt, scoped review, seeks an authorized application-custodian retention and query-scope clarification plus a service-owner impact comparison, and will reassess at 09:35 or earlier on a verified new edit or a substantiated source-loss risk."

The correction preserves each level of confidence separately. It treats the preservation question as urgent without claiming malicious cause and avoids selecting any production containment control. The report does not assert that a real source hold was applied. Its review time is a **classroom decision checkpoint**, not an operational requirement imposed by NIST.

A good learner can explain why the priority is provisional without saying "we have no confidence in anything." The source cards are available, the authorization hypothesis is contested and the actor is unknown; those are different propositions.

### 2.2a.11 Reassess sequentially when a new card arrives

A review must start with the **previous frozen decision**, not a blank slate. A useful sequence is:

1. **Freeze the prior note.** Identify what the analyst could defend at the earlier checkpoint and which observations were missing.
2. **Declare the new release.** Add only the cards actually supplied at the new checkpoint; preserve their event and availability times.
3. **List the changed claims.** Did the new card add a source record, contradict an interpretation, verify a business mismatch, or merely describe another report?
4. **Check the three confidence fields separately.** A new record may raise confidence in its *content being supplied* without establishing the meaning or actor.
5. **Re-evaluate potential versus verified harm.** Name the legitimate business unit affected or still unmeasured.
6. **Re-evaluate preservation and containment urgency independently.** Record the relevant custodian and authorized test for each.
7. **Write the next provisional note.** Keep a decision owner, next review time/trigger, proposed authorized request and unresolved limitations.
8. **Version rather than overwrite.** Save the 09:05 note and the 09:20 revision independently, with a short statement of what changed.

The change from Round A to Round B is not automatically an escalation in every dimension. It is a **richer evidence set**. R9 adds a specific booking-edit question and R15 introduces an evidence-availability concern that was not released earlier; the human actor remains unknown. A measured service mismatch still requires an approved comparison not present in R1–R16.

This process allows the team to be responsive without treating every new card as equal in significance. A retention notice may change how quickly the team contacts a custodian, while an owner-approved task addendum may change the interpretation of one booking. Neither must move every dimension in the same direction.

### 2.2a.12 Reassess on conflicting signals without forcing a verdict

Incident sources may pull the interpretation in different directions. R9 reports B19 edited, R10 omits B19 from the supplied plan and R12 records that the staff member does not remember B19. These facts create uncertainty about authorization. They do not independently prove account takeover, identity theft or deliberate action.

A beginner should avoid treating conflicting evidence as a mathematical vote. One high-quality source may be more directly relevant to a specific question than several weak contextual reports, but assessing quality requires scope, producer semantics, completeness, possible bias and timing. A staff recollection is context; a complete, dated approved plan would answer the task-scope question more directly, if it actually exists and is verified.

When sources conflict, write:

- The exact proposition in dispute.
- What each source supports and does not support.
- What observation would discriminate between competing explanations.
- Who can authorize or produce that observation.
- What decision remains safe while waiting.
- What future result would strengthen, weaken or leave the hypothesis unchanged.

The proper output is often a **specific unresolved hypothesis**, not "medium confidence" in a generalized attack story. This is a valuable result because it makes the next verification work reproducible for another analyst.

The TRI2 `CONFLICTING_SIGNALS` variant models an incomplete approved-task addendum: the analyst cannot downgrade solely because a document is present if its scope or completeness is not verified.

### 2.2a.13 Reassess on increased preservation risk without claiming a breach

At 09:20, R15 reports a 24-hour policy for detailed booking-audit records, subject to an authorized copy. The record does not identify the event/ingestion/storage anchor, the exact deletion job, the oldest still-accessible relevant row, or a confirmed effective hold. That uncertainty is itself operationally meaningful.

The response team can request rapid custodian clarification and appropriate preservation authorization **before** proving an attack. Such a request protects the ability to test competing explanations later; it does not assert that the leading malicious explanation is true. Equally, the notice does not justify collecting unrelated patron information or using an unapproved account to change retention settings.

If the custodian is unavailable, the note should record the failed contact, the accountable incident lead, a designated approved escalation route and the remaining uncertainty. Do not turn the absence of a response into proof that data were deleted. Do not assume that filing a request applied a hold.

The existing HOLD2 chapter addition teaches how to distinguish source hold requests, approval, application and verified effect. TRI2 instead asks **how that uncertainty affects the provisional urgency and next review**, without replaying HOLD2's test or inventing a successful hold.

A useful phrase is: "Evidence-availability concern is time-sensitive; cause confidence remains unproven; exact deletion deadline unknown." Those three facts can all be true at the same checkpoint.

### 2.2a.14 A new verified edit is a conditional review trigger, not a command

An incident lead may specify that a **future, source-verified unexplained booking edit** should cause an immediate reevaluation of containment options. This does not mean such an edit has occurred after the 09:20 Round B review. It is a conditional threshold attached to the provisional decision.

A trigger must say what counts as verified for the specific purpose. At minimum, a relevant custodian would need to check the source, timestamp semantics, selected booking/object, possible approved task and source coverage. The team would then bring the result to the incident lead and service owner for a decision.

The trigger does **not** authorize an automatic account disable, pause or data collection outside scope. Choosing a containment action requires its own risk and authorization assessment, and the later Chapter 3 comparison is outside the two checkpoints here.

TRI2 includes a fictional `NEW_EDIT_VERIFIED` input as an independent scenario. The code marks it **variant-only**; an attempt to insert the same flag into a canonical snapshot is explicitly rejected. This guards against a common learning error: performing an interesting counterfactual and then treating its event as if it had appeared in the R-series evidence.

The proper human question after a verified new edit is which intervention, if any, would now be proportionate, given potential harm and business costs. The toy classifier deliberately does not make that selection.

### 2.2a.15 A justified downgrade must specify which concern decreased

"Priority lowered" is not a complete assessment. Which aspect became less concerning, what new evidence justified that change, and what remained unresolved?

Suppose a **separately labeled future synthetic variant** supplies an owner-approved, complete training addendum explicitly authorizing the B19 task and a properly bounded, complete quiet observation for a specified subsequent interval. Those inputs could reduce **concern that B19 was outside the approved training scope**, while still leaving the human operator unproven. They cannot establish that every booking is correct or that no other activity occurred outside the tested interval.

The preservation question also remains separate. If detailed records still face an unknown retention anchor and no effective source safeguard has been independently substantiated, the team should not abandon preservation simply because the B19 authorization hypothesis became less concerning.

Another variant might include a separately verified and approved preservation safeguard, reducing source-loss concern **within its tested source scope**. Even then the team should not call the entire incident resolved. The conclusion is a limited change in one concern, not a global proof of safety.

TRI2 provides two contrasting downgrade cases: one with a **declared synthetic source safeguard**, and one with the same task-scope evidence but **source preservation still unconfirmed**. Both may show reduced *B19 authorization concern*; only the first prints a fixture-only protected-source status. Neither automatically assigns a lower NIST severity, executes containment or closes the case.

A downgrade based solely on R14's quiet summary with unknown filters is unjustified. A contradiction in a source should be resolved by obtaining stronger evidence, not by choosing whichever report supports the desired lower priority.

### 2.2a.16 What the model can and cannot classify

The TRI2 script deliberately prints **descriptive evidence states**, not a numeric severity, risk score, attack probability or action recommendation. Its six columns mean:

| Printed prefix | Interpretation |
|---|---|
| `R` | Record availability inside the supplied classroom set; not authenticated production source provenance |
| `I` | Support for the current event interpretation or task-scope explanation |
| `C` | Whether a human actor has been established; it remains unproven here |
| `H` | Reported potential harm versus a separately asserted bounded verified business observation |
| `P` | Evidence-preservation concern, source contact or declared synthetic safeguard |
| `K` | Whether the concern about continuing or out-of-scope activity deserves another human review |

The `flags` field lists important reasoning barriers such as a quiet query without known coverage, an unsupported attribution claim or a requested downgrade not justified by the supplied conditions.

None of these values authorizes a control. A result such as `K:NEW_EDIT_REVIEW` asks for **human reevaluation**; it is not a request to disable an account. A result such as `P:SOURCE_PROTECTED_IN_VARIANT` means the invented Boolean input claimed a safeguard, not that the code independently verified a source hold.

The code's first check is the evidence release boundary. If a Round A packet references R9, the entire assessment stops with `BLOCK_UNRELEASED_SOURCE`. The classifier also rejects a "verified new edit" flag when the input is presented as canonical rather than a synthetic variant.

The source and event confidence categories do not attempt to measure real probabilities. A real organization would need its own criteria, evidence quality controls, authorized response plan and responsible decision makers. For the rapid course, the aim is to make unsupported claims and reassessment points visible.

### 2.2a.17 Versioned priority notes prevent hindsight revision

When the team receives new information, preserve the old decision rather than silently replacing it. A minimal revision log might contain:

| Field | Round A note | Round B update |
|---|---|---|
| Evidence boundary | R1–R8 by 09:05 | R1–R16 by 09:20 |
| Relevant unresolved operation | B17/B18 authorization | B19 authorization added |
| Service impact | Patron report, no verified comparison | Second patron report, still no authoritative comparison |
| Source availability concern | No R15 rule released | R15 retention notice; anchor unknown |
| Interpretation | Scheduled training plausible but unproved | Training task scope more specifically contested for B19 |
| Cause attribution | Unproved | Still unproved |
| Next requested work | Training-owner clarification | B19 approval check, bounded impact and source-retention clarification |
| Owner and review | Incident lead; 09:15 or verified trigger | Incident lead; 09:35 or earlier verified trigger |

These descriptions do not claim that no loss risk existed before R15 was released; they say the **learner had not yet received that notice**. The distinction matters when reviewing whether an earlier decision was reasonable from the information then available.

A revision should identify which evidence caused the change. "Updated priority after new information" is vague. "Added R9/R10/R15 to the permitted set at 09:20; separated unresolved B19 authorization from preservation contact concerning R15" is testable.

A reviewer should also ask whether the new priority note still includes the original bounded approval constraints. A source becoming more urgent does not dissolve the need for permission, and a new suspicion does not identify an attacker.

### 2.2a.18 Section synthesis: urgency and certainty can move independently

The Chapter 2 triage skill is not selecting the most alarming label. It is writing a provisional decision note that distinguishes **what the records say**, **what those events mean**, **who or what caused them**, **what harm could follow**, **what harm has been verified**, **which evidence may disappear**, and **whether continuing activity requires urgent owner review**.

At 09:05, R1–R8 permit a prompt assessment, training-owner question and bounded review. At 09:20, R9–R16 add a B19 authorization question, a second patron report, an imperfect quiet-query summary and a short-retention notice with no confirmed anchor. Preservation concern can rise while cause attribution remains unknown.

A valid reclassification is limited to the evidence that supports it. A wrong-source negative query cannot lower concern about unseen activity. An approved task addendum may narrow the B19 explanation without proving the human actor. A custodian who cannot be reached increases uncertainty about evidence availability but does not prove evidence loss. A verified new edit would demand fresh human attention but would not automatically select a control.

The following offline lab uses these principles as **structural review labels**. It does not classify a real incident, make an operational decision, or extend any canonical R-series record.

---

## TRI2 Offline Laboratory — Reassessment Under Incomplete Evidence

**Classification:** Independent teaching-only fixture. The labels TRI2 and its Boolean variant fields are not original Harbor Library records, measured operational outcomes, or accepted source-hold receipts.

**Goal:** Show why different dimensions change independently when evidence becomes available; identify unsupported negative-query, attribution, harm and downgrade claims; preserve the Round A/Round B release boundary; and show which human review question remains open.

**Environment:** Python 3 standard library, entirely in memory; no files, network access, accounts, collection, retention-control changes, notifications or operational actions.

**Important model contract:** The `R:SUPPLIED_NOT_AUTHENTICATED` output means a synthetic case card is present for the learner. It does not mean a producer's log has been independently authenticated. `H:VERIFIED_BOUNDED` and `P:SOURCE_PROTECTED_IN_VARIANT` are assertions made **inside invented variant inputs**; the program does not actually conduct an impact comparison or source-hold test. `C:ACTOR_UNPROVEN` always remains true because no simulated human attribution is established.

### Input and predictive exercise

Before executing, predict why R9 is unavailable at 09:05, why R14's quiet summary cannot prove no more edits, why an R15 loss concern cannot become a deletion deadline, and why a valid addendum might justify a **narrow B19 explanation reassessment** without ending preservation work. Then execute the exact program.

### Full Python 3 code

~~~python
from copy import deepcopy

RELEASE = {
    "A": {f"R{i}" for i in range(1, 9)},
    "B": {f"R{i}" for i in range(1, 17)},
}

BASE = dict(
    stage="B",
    refs=("R9", "R10", "R11", "R12", "R13", "R14", "R15", "R16"),
    record_provided=True,
    owner_state_check=False,
    patron_report=True,
    quiet_summary=True,
    query_coverage_known=False,
    retention_notice=True,
    retention_anchor_known=False,
    source_safeguard_confirmed=False,
    custodian_available=True,
    verified_fresh_edit=False,
    approved_addendum=False,
    training_scope_verified_complete=False,
    no_new_edits_verified=False,
    claim_human_actor=False,
    request_downgrade=False,
    variant=False,
)

def review(s):
    if not set(s["refs"]).issubset(RELEASE[s["stage"]]):
        return "BLOCK_UNRELEASED_SOURCE"
    if s["verified_fresh_edit"] and not s["variant"]:
        return "BLOCK_INVENTED_CANONICAL_EVENT"

    record = (
        "R:SUPPLIED_NOT_AUTHENTICATED"
        if s["record_provided"] else "R:UNVERIFIED"
    )
    interpretation = (
        "I:TRAINING_SCOPE_SUPPORTED"
        if s["approved_addendum"]
        and s["training_scope_verified_complete"]
        else "I:CONTESTED_OR_INCOMPLETE"
    )
    cause = "C:ACTOR_UNPROVEN"

    harm = (
        "H:VERIFIED_BOUNDED"
        if s["owner_state_check"]
        else "H:REPORT_ONLY" if s["patron_report"]
        else "H:NOT_MEASURED"
    )
    preserve = (
        "P:SOURCE_CONTACT_BLOCKED"
        if s["retention_notice"]
        and not s["custodian_available"]
        else "P:SOURCE_PROTECTED_IN_VARIANT"
        if s["source_safeguard_confirmed"]
        else "P:ANCHOR_UNKNOWN_CONTACT"
        if s["retention_notice"]
        and not s["retention_anchor_known"]
        else "P:RETENTION_NEEDS_CHECK"
        if s["retention_notice"]
        else "P:NO_RELEASED_LOSS_RULE"
    )
    contained = (
        "K:NEW_EDIT_REVIEW"
        if s["verified_fresh_edit"]
        else "K:B19_CONCERN_REDUCED"
        if s["approved_addendum"]
        and s["training_scope_verified_complete"]
        and s["no_new_edits_verified"]
        else "K:OPEN_HYPOTHESES"
    )

    flags = []
    if s["quiet_summary"] and not s["query_coverage_known"]:
        flags.append("QUIET_NOT_NEGATIVE_PROOF")
    if s["claim_human_actor"]:
        flags.append("ATTRIBUTION_CLAIM_UNSUPPORTED")
    if s["request_downgrade"]:
        if (
            s["approved_addendum"]
            and s["training_scope_verified_complete"]
            and s["no_new_edits_verified"]
        ):
            flags.append("DOWNGRADE_ONLY_B19_CAUSE_CONCERN")
        else:
            flags.append("DOWNGRADE_NOT_JUSTIFIED")
    if s["retention_notice"] and not s["custodian_available"]:
        flags.append("ESCALATE_CONTACT_NO_HOLD_ASSUMED")
    if s["verified_fresh_edit"]:
        flags.append("REVIEW_ON_NEW_VERIFIED_SIGNAL")

    return " ".join([
        record, interpretation, cause, harm, preserve,
        contained,
        "flags=" + (",".join(flags) if flags else "NONE"),
    ])

def case(**changes):
    s = deepcopy(BASE)
    s.update(changes)
    return review(s)

ROUND_A = deepcopy(BASE)
ROUND_A.update(
    stage="A",
    refs=("R1", "R3", "R4", "R5", "R6"),
    retention_notice=False,
    quiet_summary=False,
)

CASES = [
    ("ROUND_A_0905", ROUND_A),
    ("ROUND_B_0920", BASE),
    ("UNRELEASED_R9_AT_A",
     {**ROUND_A, "refs": ("R1", "R9")}),
    ("QUERY_FILTER_UNKNOWN", {"variant": True}),
    ("RETENTION_ANCHOR_UNKNOWN",
     {"variant": True, "quiet_summary": False}),
    ("PATRON_REPORT_UNVERIFIED",
     {"variant": True, "quiet_summary": False,
      "retention_notice": False}),
    ("CLAIM_FALSE_ATTRIBUTION",
     {"variant": True, "claim_human_actor": True}),
    ("CUSTODIAN_UNAVAILABLE",
     {"variant": True, "custodian_available": False}),
    ("NEW_EDIT_VERIFIED",
     {"variant": True, "verified_fresh_edit": True}),
    ("NEW_EDIT_NOT_CANONICAL",
     {"verified_fresh_edit": True}),
    ("CONFLICTING_SIGNALS",
     {"variant": True, "approved_addendum": True,
      "training_scope_verified_complete": False}),
    ("PREMATURE_DOWNGRADE",
     {"variant": True, "request_downgrade": True}),
    ("VALID_B19_CAUSE_DOWNGRADE",
     {"variant": True, "request_downgrade": True,
      "approved_addendum": True,
      "training_scope_verified_complete": True,
      "no_new_edits_verified": True,
      "query_coverage_known": True,
      "source_safeguard_confirmed": True}),
    ("DOWNGRADE_WITH_PRESERVATION_OPEN",
     {"variant": True, "request_downgrade": True,
      "approved_addendum": True,
      "training_scope_verified_complete": True,
      "no_new_edits_verified": True,
      "query_coverage_known": True,
      "source_safeguard_confirmed": False}),
    ("OWNER_VERIFIED_IMPACT",
     {"variant": True, "owner_state_check": True}),
    ("SOURCE_SAFEGUARDED_IN_VARIANT",
     {"variant": True,
      "source_safeguard_confirmed": True}),
]

for label, values in CASES:
    result = review(values) if "stage" in values else case(**values)
    print(label + " " + result)

assert review(ROUND_A).startswith("R:SUPPLIED")
assert case(verified_fresh_edit=True) == (
    "BLOCK_INVENTED_CANONICAL_EVENT"
)
~~~

### Exact expected output — executed with Python 3

~~~text
ROUND_A_0905 R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:NO_RELEASED_LOSS_RULE K:OPEN_HYPOTHESES flags=NONE
ROUND_B_0920 R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF
UNRELEASED_R9_AT_A BLOCK_UNRELEASED_SOURCE
QUERY_FILTER_UNKNOWN R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF
RETENTION_ANCHOR_UNKNOWN R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=NONE
PATRON_REPORT_UNVERIFIED R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:NO_RELEASED_LOSS_RULE K:OPEN_HYPOTHESES flags=NONE
CLAIM_FALSE_ATTRIBUTION R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF,ATTRIBUTION_CLAIM_UNSUPPORTED
CUSTODIAN_UNAVAILABLE R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:SOURCE_CONTACT_BLOCKED K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF,ESCALATE_CONTACT_NO_HOLD_ASSUMED
NEW_EDIT_VERIFIED R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:NEW_EDIT_REVIEW flags=QUIET_NOT_NEGATIVE_PROOF,REVIEW_ON_NEW_VERIFIED_SIGNAL
NEW_EDIT_NOT_CANONICAL BLOCK_INVENTED_CANONICAL_EVENT
CONFLICTING_SIGNALS R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF
PREMATURE_DOWNGRADE R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF,DOWNGRADE_NOT_JUSTIFIED
VALID_B19_CAUSE_DOWNGRADE R:SUPPLIED_NOT_AUTHENTICATED I:TRAINING_SCOPE_SUPPORTED C:ACTOR_UNPROVEN H:REPORT_ONLY P:SOURCE_PROTECTED_IN_VARIANT K:B19_CONCERN_REDUCED flags=DOWNGRADE_ONLY_B19_CAUSE_CONCERN
DOWNGRADE_WITH_PRESERVATION_OPEN R:SUPPLIED_NOT_AUTHENTICATED I:TRAINING_SCOPE_SUPPORTED C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:B19_CONCERN_REDUCED flags=DOWNGRADE_ONLY_B19_CAUSE_CONCERN
OWNER_VERIFIED_IMPACT R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:VERIFIED_BOUNDED P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF
SOURCE_SAFEGUARDED_IN_VARIANT R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:SOURCE_PROTECTED_IN_VARIANT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF
~~~

### Interpretation of positive and negative controls

**ROUND_A_0905:** The selected supplied records support a reported booking concern and unresolved explanations. They do not include R15's loss notice or R9's B19 edit. The `P:NO_RELEASED_LOSS_RULE` status means no such rule was released to the learner at this checkpoint; it does **not** mean retention risk did not exist.

**ROUND_B_0920:** The learner now has R9–R16, including R15, but its source-retention anchor is unknown. R14's quiet summary lacks the coverage necessary for a broad negative conclusion. The actor remains unproven.

**UNRELEASED_R9_AT_A** is rejected because it improperly tries to use R9 at the 09:05 decision, regardless of R9's earlier printed event time.

**QUERY_FILTER_UNKNOWN** keeps the quiet-query limitation visible rather than reducing concern. **RETENTION_ANCHOR_UNKNOWN** removes the quiet-query flag in a variant while preserving the unresolved preservation anchor. The two warnings are independent.

**PATRON_REPORT_UNVERIFIED** illustrates why an uncorroborated report does not become a verified authoritative-state mismatch. **CLAIM_FALSE_ATTRIBUTION** flags an unsupported claim to know the person controlling the account without filling in an invented identity.

**CUSTODIAN_UNAVAILABLE** creates a contact/escalation gap while continuing to hold the source-hold status unconfirmed. This does not establish that any log was deleted. **NEW_EDIT_VERIFIED** is an independent future hypothetical observation requiring human review of continued activity; it does not choose containment. **NEW_EDIT_NOT_CANONICAL** blocks an attempt to append the same invented event to the canonical case.

**CONFLICTING_SIGNALS** supplies an invented addendum but explicitly withholds confirmation that it represents the complete approved training scope. The interpretation remains unresolved. **PREMATURE_DOWNGRADE** shows that a desire to lower concern is not an evidentiary basis.

**VALID_B19_CAUSE_DOWNGRADE** assumes, *only inside its separate variant*, a complete approved B19 addendum, a valid bounded negative observation and a declared source safeguard. It supports a **limited reduction in the B19 outside-training concern** without establishing human attribution or every service outcome. The source-protected label is an invented premise, not verified by this program.

**DOWNGRADE_WITH_PRESERVATION_OPEN** uses the same invented task-scope and quiet-observation premises but **without** a source safeguard. Concern about the B19 explanation may narrow while preservation work remains time-sensitive. These two results are intentionally different.

**OWNER_VERIFIED_IMPACT** illustrates a separate hypothetical authorized business-state observation that can move harm from reported to **verified within a bounded scope**. It supplies no affected-person population count. **SOURCE_SAFEGUARDED_IN_VARIANT** demonstrates that a hypothetical preservation effect can be declared without resolving cause, attribution or patron impact.

### Limitations and diagnostic negative tests

The program does **not** read any case files, query logs, test retention policies, authenticate a source, assess human identity, or verify a business state. Values such as `owner_state_check=True`, `no_new_edits_verified=True` and `source_safeguard_confirmed=True` are **invented premises** for independent variants, not real evidence collected by the script. It cannot calculate probabilities, incident severity, actual retention deadlines or appropriate live containment.

The result labels are educational and may be rejected or refined by an organization's actual decision policy. The ordering of checks is simplified: first validate release, then flag invented canonical events, then describe dimensions and limitations. Real cases may have multiple independent uncertainties not represented here.

**Further negative control:** Set `request_downgrade=True` while leaving `training_scope_verified_complete=False`. The expected flag is `DOWNGRADE_NOT_JUSTIFIED`. Do not remove the quiet-query or source-retention caveats merely because a respondent asks for lower priority. Restore the baseline after the exercise.

**Required learner output:** Reproduce all 16 lines, classify each scenario's most consequential limitation, explain why preservation and containment urgency can move independently, and write two versioned notes—09:05 and 09:20—with the correct release boundaries, owner, next authorized request and review trigger.

**Lab assessment, five points:** one point for exact output; one for three separate confidence layers; one for separating reported from verified impact; one for preservation versus containment review; and one for rejecting unsupported de-escalation, attribution and future-source use. This is supplementary assessment and creates **no numbered exercise ID**.

---

## Two-Role Practical Activity — Frozen Priority Review and Independent Reassessment

**Purpose:** Determine whether a reviewer can explain why a provisional priority changed, stayed open or narrowed using the actually released source cards, without the writer's retrospective coaching or invented production evidence.

**Roles:** **Round A/B Triage Analyst** prepares and freezes the two source-bounded decision packets. **Independent Review Lead** evaluates the packet using the permitted R-series table and produces a separate, frozen reassessment. A facilitator may observe but must not supply missing evidence or reveal later cards prematurely.

### Preparation and sealed packet

The analyst creates `TRI2-A-v1` with checkpoint 09:05, R1–R8 evidence pointers, reported versus inferred statements, potential harm, separate confidence layers, owner, a proposed authorized training-owner check and 09:15 review condition. The analyst then freezes that packet unchanged.

Only then does the facilitator release R9–R16 for the 09:20 reassessment. The analyst prepares `TRI2-B-v1`, identifying which statements changed because R9/R10/R11/R12/R14/R15 became available. The packet does not contain R17–R24 or later branch results. It preserves R15's unknown deletion anchor and R14's incomplete query coverage.

The analyst may add a **separately marked synthetic variant** card illustrating an approved addendum or custodian unavailability, but must give it a distinct name and must not mix its result into the canonical Round B note.

### Independent review

Without asking the analyst to explain what they intended, the review lead:

1. Reconstructs the evidence set legitimately available at each checkpoint.
2. Classifies each major claim by **record content, interpretation, and cause/attribution**.
3. Separates potential business harm from the consequences actually verified.
4. Identifies preservation-urgency evidence and unknown loss clock.
5. Identifies continuing-activity concern without treating R14 as a complete negative finding.
6. Names the permitted next request, its custodian/owner and the relevant approval boundary.
7. Identifies whether the 09:05 provisional note remained justified at the time and why 09:20 warrants a revised note.
8. States the next review time or precise future observation that would trigger earlier reconsideration.

The lead writes `TRI2-review-v1` and freezes it **before** the two roles discuss disagreements. A reviewer who uses R9 to fault the 09:05 analyst for ignoring it fails the chronological requirement. A reviewer who describes the notice as proof that logs were deleted also fails the source-semantics requirement.

### Adjudication and improvement

Compare the two frozen notes and receiver answer with the canonical sources. Record whether a problem came from a missing source pointer, an unsupported interpretation, an inappropriate priority change, an incomplete owner/request field or a violation of the release boundary.

If the packet requires correction, create `TRI2-A-v2` or `TRI2-B-v2` with a documented change. Do **not** overwrite the old note or pretend that the revised understanding existed earlier.

**Bounded pass:** Both checkpoints have correct release sets, all three confidence layers are distinguished, reported harm is not counted as verified impact, preservation urgency is separate from containment concern, and the next proposed request and review trigger are authorized and specific.

**Critical fail:** Attribution is asserted without supporting evidence; R14's quiet result is generalized beyond its unknown query bounds; an exact R15 deletion deadline is invented; a synthetic variant is imported into canonical R1–R16; an earlier decision is justified with later sources; or a production control is selected/executed without the proper fictional approval path.

**Limits:** This practice tests two learners' written reasoning under a synthetic tabletop, not the actual capacity of an organization to contact a custodian or contain a cyberattack. A correct priority note does not prove the next request was performed.

---

## Targeted Refinements of Existing Exercises — EX014, EX016, EX024 Only

Preserve the original exercise numbers, required output formats and 0–2 rubric. **No new EX IDs and no additional chapter-scoring denominator** are introduced.

### EX014 — Triage question (retain the **two-row table**)

Keep the existing two answerable questions with their record IDs, bounded source/custodian and result that changes triage. Add one short **evidence-layer explanation to each row**: (a) which supplied record content is available, (b) which interpretation a custodian could strengthen or weaken, and (c) which causal/actor claim would still remain unproven even after the proposed check. Do not add a third question or claim the checks already occurred.

**2-point acceptance:** The two rows remain discriminating and authorized, and the learner explicitly distinguishes a better-supported B19 task-scope explanation from attribution. A question about booking-state impact cannot be answered solely by a patron complaint.

### EX016 — Priority without false certainty (retain the **short decision note**)

Keep the original checkpoint, separate potential harm, urgency, confidence, provisional priority, decision owner and observable review trigger. Add **three short confidence clauses**—record supplied, event/task interpretation unresolved, cause unproven—and split urgency into **preservation contact** and **possible containment reevaluation**. At 09:20, identify R15's unknown anchor and R14's bounded quiet result. Preserve the proposed authorized P-A/impact-check path, 09:35 review and earlier verified trigger.

**2-point acceptance:** The note does not assign a NIST severity category or calculate a deadline from R15. A weak attack attribution cannot eliminate preservation urgency; a patron report is not a verified affected-person count. Keep it a concise decision artifact rather than replacing it with a long incident report.

### EX024 — Escalation threshold (retain exactly **two hypothetical observation/response pairs**)

The first pair should concern a **future source-verified new unexplained booking edit or owner-confirmed material booking-state mismatch**, with a named verifying custodian and incident-lead/service-owner decision review. The second should concern **future verified loss of relevant source availability or inability to obtain the needed retention clarification**, naming the source/custodian, selection and authorized escalation. Each pair must say why the trigger affects *containment consideration* or *preservation urgency* rather than claiming a newly proved attacker.

**2-point acceptance:** Exactly two hypothetical pairs with observable conditions, verifier, harm/loss rationale, decision owner and earlier-review trigger. Neither scenario is already observed in R1–R16, and a custodian who is unavailable is not silently reported to have deleted evidence.

---

## Supplementary Worked Answers — For the Principal Manuscript's Final Appendix

### EX014 — Additional worked reasoning

The required two-row table can remain focused on **B19 authorization** and **booking-impact scope**. For the first row, R9 supplies a B19 edit and R10 omits B19 from the supplied plan; the dated approved training plan or addendum held by the training owner could strengthen or weaken whether B19 was in the authorized task scope. A complete approved inclusion would narrow that *task-scope* concern, but it would not authenticate the human operator. For the second row, R11 supplies a patron report and R16 requests an impact check; the service owner can authorize a bounded comparison of authoritative booking values with approved targets. That comparison would move selected business-state conclusions from reported to verified or unresolved, **not** measure all affected patrons without a complete frame. The record, interpretation and attribution layers remain explicitly separate.

### EX016 — Additional short worked priority note

> **Checkpoint and owner:** 09:20 UTC, incident lead. **Available records:** R1–R16; R9 records B19 edited, R10's supplied plan omits B19, and R11 reports a patron concern. **Potential harm:** room-booking correctness may be affected, but no owner-approved authoritative comparison or affected-patron total is supplied. **Confidence:** the records are available as synthetic source statements; B19 authorization remains contested; the human operator and malicious cause are unproven. **Urgency:** obtain a timely, authorized P-A source/retention clarification because R15 reports a 24-hour deletion policy with unknown anchor, while containment requires separate review of continuing harm; R14's quiet summary does not establish its full coverage. **Provisional priority:** prompt bounded review, not a NIST-defined category. **Next request:** application custodian and service owner provide permitted source, retention and impact checks under incident-lead coordination. **Review:** 09:35 UTC or sooner upon a verified unexplained new edit or substantiated source-availability failure.

The answer is a short **classroom decision note** rather than a numerical attack probability. It does not assert that source preservation or a service restriction occurred. It also preserves the earlier 09:05 record without backdating R9 or R15.

### EX024 — Additional worked reasoning

| Future hypothetical observation | Verifier and why it changes the assessment | Decision response |
|---|---|---|
| A **new, source-verified unexplained booking edit after 09:20**, or an owner-confirmed material state mismatch | Application custodian checks the record and applicable selection; service owner confirms the affected business target. This would increase concern about continuing harmful activity or verified service impact, without by itself identifying an attacker. | Incident lead and relevant service/identity owners **reconvene** promptly to consider proportionate, separately authorized containment options; no control is automatically executed. |
| A **future custodian-confirmed inability to preserve/retrieve a necessary selected source item**, or an authenticated source-loss warning | Application custodian checks which source and interval are affected, whether the item was expected to exist and whether the loss path is supported. This increases preservation urgency or uncertainty, not proof of malicious deletion. | Incident lead seeks an authorized alternative preservation/source decision and escalates through the approved route, with a near-term review; the exact R15 deletion deadline remains unknown. |

Neither future observation is part of the canonical R1–R16 input. The first pair is about potential ongoing harm and containment review; the second is about evidence availability. The exercise does not infer a human operator, source deletion time, or completed response.

---

## Synthesis, Navigation and Primary Sources

A defensible provisional priority is a **versioned, owner-owned decision under uncertainty**, not a permanent numeric incident grade. Its three confidence layers—record supplied, event interpreted, cause attributed—must remain separate. The same is true of potential versus verified harm, and urgency to preserve evidence versus urgency to consider containment. Reassessment changes only the propositions that new, properly released and interpreted evidence can support.

R1–R8 remain the 09:05 decision basis. R1–R16 become available at 09:20. The TRI2 variants are not canonical source observations and cannot justify earlier decisions, a real hold, identity attribution or a production action.

### Continue studying — chapter 02 of 04 (public supplementary draft)

[← Chapter 01](../MANUSCRIPT.md#ch-01) · [Course chapter index](../../SUBJECTS.md) · [Chapter 03 →](../MANUSCRIPT.md#ch-03) · [Principal book and worked answers](../MANUSCRIPT.md#answers)

**Editorial integration note:** This is a **transitional public component** of Chapter 02 of the single English manuscript. Accepted teaching, TRI2, and the three existing exercise/answer refinements are intended for later consolidation into `MANUSCRIPT.md` by the maintainer. This file creates no new numbered exercise, subject, course skill or verified A4 page count and does not claim book completion.

### Verified official primary sources and provenance

- [NIST SP 800-61 Revision 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), final April 2025. Supports incident response as part of organizational cybersecurity risk management, preparation, analysis, coordination and response. **It does not prescribe TRI2 confidence columns or severity labels.**
- [NIST Cybersecurity Framework 2.0 (CSWP 29)](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), February 2024. Provides flexible high-level outcomes for assessing, prioritizing and communicating risk; it **does not prescribe a single incident triage matrix**.
- [NIST SP 800-92 — Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final), September 2006. Provides source and log-management background, including availability and retention considerations. It does **not** define the R14 query, R15 anchor or TRI2 algorithm.

TRI2's labels, Python fixture, conditional new-edit and addendum cases, review method and example messages are **original synthetic educational constructs**. None is reported by NIST or observed in production. Editorial responsibility belongs only to [hiagokinlevi](https://github.com/hiagokinlevi). Maintainer-owned original material follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within their documented limits; third-party source rights are preserved. No external service is contacted and no operational control or evidence hold is executed.
