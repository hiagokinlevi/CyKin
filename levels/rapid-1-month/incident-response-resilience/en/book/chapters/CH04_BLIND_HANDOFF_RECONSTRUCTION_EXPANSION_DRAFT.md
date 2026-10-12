# Incident Response and Cyber Resilience — Rapid Course

## Chapter 04 Expansion Draft: Blind Handoff and Independent State Reconstruction

**Editorial status:** **Public transitional English instructional draft** for Chapter 04 of the course's **one principal book**. Not a separate chapter, final publication, qualification, or technical validation of real incident response.
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).
**Integration target:** [Chapter 04 of MANUSCRIPT.md](../MANUSCRIPT.md#ch-04).
**Scope:** Test whether a responder who did not create a case packet can reconstruct its evidence, temporal boundaries, last reported actions, failed service gates, accountable owners and next safe request without assistance from the original author.
**Do not duplicate:** L2 reviewer calibration, F4-AUDIT release-and-score logic, F1 unavailable approver, M1/M2 public communication replay, DEL4 message delivery/read-back or the existing six-artifact score.

> **Fictional release boundary.** Harbor Library and every R-series record are fictional. The learner has R1–R8 at 09:05 in Round A; R9–R16 only at 09:20 in Round B; R17–R24 only in Round C before 09:37. Round D first supplies **one** chosen Branch S or P at 09:45. P1/C1 are released later in Round D; V1 arrives afterward. The independent F1 and M1/M2 replays cannot enter earlier decisions. BH4 packets and receiver statements below are newly invented classroom examples, not added events or verified case observations.

# New Chapter 04 Teaching

### 4.21.1 The missing question in a conventional handoff

An analyst can write an accurate history yet leave the next responder unable to act safely. The writer remembers the discussion, knows which colleague supplied context and remembers why certain options were rejected. A new on-call responder may possess only the saved case packet. If that document says "account handled, recovery pending," the receiver must guess which account action occurred, whether it was proposed or executed, what was tested, and who owns the remaining work.

Chapter 04 already tells students to preserve a source ledger, freeze decisions before revealing new cards, give a reproducible handoff and score six artifacts. Section 4.15 briefly proposes a blind receiver test. The missing lesson is **how to prove that a receiver can actually reconstruct the decision state** rather than simply reading a polished summary.

The target is a repeatable two-role exercise: a sender freezes an evidence-linked packet; an independent receiver reviews it without speaking to the sender, locates the referenced evidence, reconstructs the relevant states and chooses a safe next request. A third evaluator can compare that answer with the supplied records, or the two participants can perform the comparison after the first answer is frozen.

[NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) gives official guidance for designing, conducting and evaluating IT training and exercises. The [FEMA HSEEP guidance](https://preptoolkit.fema.gov/web/hseep-resources/policy-and-guidance) addresses evaluation of observable exercise capabilities and improvement planning. The specific blind reconstruction contract is original CyberABC teaching material, not a scoring scheme mandated by either source.

### 4.21.2 Define what blind means before starting

Blind does **not** mean withholding valid evidence. The receiver may open the permitted canonical R-series table, the chosen branch card and the later P1/C1/V1 material if those cards have been released for the selected checkpoint. Blind means **no explanation from the person who wrote the packet** while the first reconstruction is being prepared.

A complete contract therefore states the checkpoint, allowed sources, packet version, required receiver answers, forbidden assistance, submission deadline if one is used, evidence-preservation rule and pass/fail criteria. These elements must be established before the sender knows how the receiver will respond. Otherwise a facilitator can unintentionally move the success criteria after observing a confusing packet.

A cold receiver should not be allowed to rely on an off-record comment, a remembered classroom conversation or later facts that were not included in the declared release. Conversely, if the packet explicitly locates an allowed source, a receiver who follows that link is doing exactly what the test is intended to measure.

The facilitator may permit two distinct phases. First, an **unaided reconstruction**, whose answer is frozen. Second, a **clarification and improvement phase**, where sender and receiver discuss failures and issue a corrected version. Results from the second phase cannot be presented as though the first packet passed unassisted.

A passing blind handoff demonstrates a narrow educational capability: two people can transfer a bounded fictional incident decision using written sources. It does not prove live-system containment, real communication delivery, tested backups or operational staffing readiness.

### 4.21.3 Separate three documents with three different owners

The exercise uses a **sender packet**, a **receiver reconstruction** and an **evaluation record**. Combining them makes it harder to determine whether the receiver derived the answer or was simply given it.

The sender packet contains the case ID, checkpoint, chosen branch, versioned prior decisions, canonical source references, reported actions, unresolved business conditions, next accountable roles and review triggers. It can point to the book's existing six outputs; it is not a new seventh output in the chapter's scoring rubric.

The receiver independently writes what the packet establishes, which sources support those findings, what remains uncertain and which request should be made next. It should not claim to have performed a technical verification merely because it located an existing classroom record.

The evaluator records whether the receiver's statements follow the supplied evidence, whether critical sources could be located, which stage boundaries were crossed, whether the suggested act requires approval and what changed in any later revision. An evaluator should give a reason for each failure rather than an unexplained mark of "incorrect."

A missing pointer is primarily a packet problem if the source cannot be located under the declared conditions. A correct pointer ignored by the receiver may indicate a comprehension or navigation problem. A source that has not yet been released is neither of those; it is outside the exercise's permitted evidence.

Each outcome requires a different improvement. A sender cannot fix a missing document by saying "I explained it during the meeting," because that explanation is exactly the dependency a blind test is intended to reveal.

### 4.21.4 Reconstruct the knowledge boundary before the incident story

One of the receiver's first tasks is to identify what **could be known at the relevant decision time**. This is not the same as arranging every event in chronological order.

R9 describes a B19 edit at 09:03, but the student receives R9 only in Round B at 09:20. It cannot justify the initial 09:05 decision. R17 and R18 become available in Round C and cannot retroactively justify the 09:20 triage. R21 is available by the 09:37 checkpoint, but it merely says a brief staff-write pause is tolerable; it does not report an approved or executed pause.

The Branch S or P report appears only in Round D at 09:45. P1/C1 and then V1 become usable only in their separate later release steps. A packet drafted at the first Branch D checkpoint cannot discuss V1's failed actor field as though that fact was then known. A later complete handoff can discuss the failure, but it must not rewrite the earlier snapshot.

A useful sender packet therefore has **event-time** and **available-at** columns. A receiver should reconstruct a decision using only evidence available at that frozen point, while keeping later revisions as separately versioned records.

A packet that backdates a later source can reach a plausible final conclusion for the wrong reason. The blind test must reject that causal and temporal shortcut, even when the student happened to know the later result from reading the book.

### 4.21.5 Locate the evidence; do not merely repeat a conclusion

"See attached logs" is not a sufficient source pointer. The receiver must know which R-series item, branch report or exercise card substantiates each material statement. In a classroom manuscript, the record ID and correct chapter link can serve as a test locator. In a real authorized investigation, the source might require a restricted evidence store, collection receipt and access permissions.

Consider the statement "staff writes were paused." The receiving responder should ask whether this refers to R21's **tolerance statement** at 09:29, a proposal made by the lead at 09:37, or a **fictional Branch P report** of a pause at 09:45. Those are different sources and do not support the same claim.

Similarly, R23's backup-job result does not substantiate a successful restore. P1/C1 supports a limited booking-state comparison after its later release; V1 supports two limited access-test observations and a failed audit attribution check. A reviewer needs those separate pointers to diagnose why unrestricted return has not been shown.

An important source rule is **locatable does not mean sufficient**. A functioning link to R21 cannot transform tolerability into authorization. A valid link to V1 cannot prove booking correctness because V1's function is different. The receiver should identify both the supporting source and what it does **not** establish.

If a required source pointer is absent, record "not located from this packet" and request correction. Do not treat missing information as evidence that the tested outcome was negative or safe.

### 4.21.6 Reconstruct recommendation, approval, execution and verification separately

The sender may compress an intervention into a phrase such as "session contained." A blind receiver must unpack it into states with source support.

At Round C, the analyst can propose a bounded current-session restriction and request appropriate approval. R19 says that the current session can be revoked; this is a capability statement, not an execution receipt. The 09:37 action remains a **proposal** under the fixed checkpoint.

Under the separately released Branch S report at 09:45, the specified current session was **reported revoked** under fictional approval. That historical report does not establish that every session was removed, that a malicious actor was identified or that the action remains independently verified indefinitely.

Under the alternative Branch P report, staff writes were reported paused for fifteen minutes at 09:45 and two manual requests were pending. The planned end of that interval does not prove automatic resumption. The receiver must not claim that the two pending requests are accepted bookings.

A precise handoff distinguishes **proposed at checkpoint C**, **approved or reported executed by a later branch**, and **technical effect independently verified within a known scope**. It may need to say that the current technical state is unknown beyond the last supplied report.

This is why merely finding an approval signature or reading a message is not enough. A separate operational result must support an execution or effectiveness claim. The blind test evaluates whether the responder knows when to stop short of that claim.

### 4.21.7 A last reported state is not a verified current state

A new on-call responder often asks, "What is the system doing right now?" The packet may not contain a fresh observation at the moment of handoff. The correct answer then distinguishes a **last reported condition** from a **current independently observed condition**.

For Branch S, the last supplied branch action is a 09:45 report of revocation, accompanied by a narrow quiet booking query and staff reauthentication requirement. That does not verify all other paths, or a later independent identity check. A responder should not tell the owner that every write route is secure merely because no later edit appeared in one bounded query.

For Branch P, the last reported pause began at 09:45. A receiver at a later, unspecified time cannot infer whether writes resumed from arithmetic alone. The two pending requests also have no supplied approval or completed disposition. Their status must remain pending until a separate owner-approved reconciliation is evidenced.

An accurate current-state entry might read: **"last branch-reported control noted; current effective status not independently verified in the available packet."** This is an actionable limit, because it tells the next responder what needs checking.

An incorrect entry such as "pause automatically ended at 10:00" invents a transition. The responder could then issue a dangerous service instruction based on an event that has never been documented.

The baseline BH4 script below deliberately requires the separate state "not independently verified" even when a historical branch report is available.

### 4.21.8 Reconstruct the failed gates without replacing them with hope

After P1/C1 and V1 are released, the next responder should understand why full service acceptance is not supported. P1/C1 shows B17 and B18 matching their approved target but B19 and B20 different. The four-booking correctness gate therefore has **failed items** requiring owner-reviewed correction.

V1's isolated test reports that one permitted synthetic action worked and one prohibited synthetic action was denied. These are **limited passes** for their tested operations, not universal access guarantees. V1 also shows a blank actor field in the audit of the permitted action. That is a failed attribution criterion, not merely an unknown that can be considered a pass.

A cold receiver must reconstruct this **mixed evidence**, not compress it to "restore passed" or "everything failed." The correct handoff identifies the successful limited observations and the failed mandatory criteria separately.

Neither the P1/C1 comparison nor V1 says that the actual production system has been corrected or that a later independent comparison passed. R23's earlier backup-status report cannot supply the missing restore evidence. The later RTE3 synthetic recovery-time fixture is also a distinct lab, not a historical Harbor Library result.

A good receiver can turn these failures into a narrow request for the service owner and audit owner. A bad receiver might choose the newest backup or close the case despite the unresolved mismatches; that is precisely the next-action failure this exercise must detect.

### 4.21.9 The next safe act is a request, not an unapproved repair

Reconstructing the past is only useful if it supports a responsible next decision. Ask the receiver to state **one next action**, the person authorized to approve it, the evidence the action requires and the review trigger.

In the later Branch S scenario, a defensible choice is to request a service-owner-approved B19/B20 correction plan and a new bounded booking-state comparison, while also assigning the audit owner to investigate and retest the blank actor field. The request can be prepared by the incident team, but no source grants automatic permission to overwrite production bookings.

For Branch P, the next request must additionally account for the two unnamed manual-queue items. A new responder may request a restricted manifest, approval status and reconciliation plan; they may not mark the two entries fulfilled based on the separate MQ3 lab or on a guessed queue content.

Unsafe next steps include immediately resuming writes, claiming full recovery after a limited login test or treating the 09:45 reported control as an unrestricted continuing guarantee. A receiver who makes such a recommendation fails the safety purpose even if they located every source.

The next review should include an observable event or deadline: a verified new unexplained edit, a failed correction comparison, an unsuccessful audit retest or a required owner response not received. The trigger is a **future condition**, not a newly supplied R-series fact.

The receiver's next-action card should therefore distinguish **may request now** from **may execute only after specified authorization**.

### 4.21.10 A sealed packet must identify its exact inputs

The sender should freeze an inventory with version and contents before handing it over. The manifest need not reproduce every record, but it must identify the allowed source and the exact records or sections that support important claims.

A late Round D packet for Branch S might cite R17/R18 in Chapter 3, Branch S in Chapter 4, and the separately released P1/C1 and V1 in Chapter 3. The receiving responder can then follow those pointers to verify the narrow statement about training authorization, later booking changes, branch action, incorrect selected booking values and failed audit actor.

If C1 is missing from the manifest, an assertion that B19/B20 fail the approved target is not independently reconstructible from the packet alone. The correct test result is **missing pointer**, not proof of correct bookings.

The sender also should list important omissions: no authenticated real operator identified, no production correction result, no full service acceptance, no verified current control status beyond the reported branch scope. Those declarations are useful because they prevent the receiver from filling blanks with customary assumptions.

A source locator is not permission to bypass actual access rules. In real response work, evidence access must be appropriately authorized. The fictional book uses public synthetic sources, but the concept of permitted scope still matters to how the packet is evaluated.

An effective packet can be short if its pointers and decisions are precise. Adding pages of narrative cannot replace an absent source or owner.

### 4.21.11 Two roles, two independent records

The sender writes the packet, then stops contributing information. The receiver reviews the packet and permitted citations without verbal or written assistance from the sender. The evaluator compares the receiver's first frozen answer with the canonical cards.

This procedure exposes a difference that ordinary peer review may hide: the sender may be able to explain the packet, yet the packet itself may not contain the explanation. If the sender supplies an important source only after a question from the receiver, that later disclosure may improve the packet but cannot make the first attempt pass unaided.

The receiver should have a fixed set of questions:

1. What phase and branch are in scope?
2. What facts were available to the earlier 09:37 decision?
3. What was only proposed then, and what did the later branch report?
4. Where can each material source be located?
5. Which business and audit checks passed narrowly, failed or remain unknown?
6. What safe request comes next, who owns it and what triggers reassessment?

The sender should not be permitted to correct a receiver's answer until the receiver has submitted it. The receiver should not search unreleased variants or ask the facilitator to supply a missing "answer" that the packet was meant to include.

A first attempt should remain frozen and attributable to the learner's work, even if later revisions demonstrate substantial improvement.

### 4.21.12 A third-party observation must distinguish packet defects from learner defects

An evaluator should not reduce all reconstruction failures to "poor communication." The root of a failed handoff may lie in the sender's evidence pointers, in the receiver's interpretation, or in an explicitly unavailable source.

If C1 is absent from an otherwise complete packet, the sender has not provided the location necessary to assess the booking-state comparison. If C1 is correctly located and the receiver ignores it, the receiver's retrieval or reasoning needs improvement. If C1 has not yet been released, the test must not demand that the receiver use it.

These distinctions inform corrective work. A missing source pointer may be fixed by updating the packet manifest. A misunderstood action state may require clearer labels or receiver training. An unavailable authorized source may require an owner-controlled follow-up rather than a documentation rewrite.

The evaluator should retain the packet version, receiver version, test checkpoint, specific failed question and supported classification. A corrected packet is a **new version**. The earlier result is not erased.

This is important when the organization later reports exercise improvement. A high pass rate after sender coaching should not be described as the same outcome as independent first-attempt reconstruction.

### 4.21.13 Hard failures and ordinary deficiencies are not equivalent

The blind-handoff contract should have **non-negotiable safety boundaries**. A receiver who cites a future card at an earlier checkpoint, merges Branch S and P, invents approval or execution, declares full recovery despite P1/C1/V1 failures, or recommends an unapproved live change has failed even if every other paragraph is well written.

Other deficiencies are more localized but still matter: missing a source locator, omitting a next owner or leaving out a review trigger can prevent a new responder from safely continuing the case. These require correction but do not necessarily reveal the same misunderstanding as an unauthorized-action proposal.

The learning test therefore uses two layers. First, detect critical breaches of source release, action history and authorization. Second, assess completeness of the remaining required fields and the receiver's reconstruction. A passing packet needs both.

This does **not** change Chapter 4's existing six-output 0–2 rubric. That rubric still totals 12 across timeline, hypothesis table, action record, recovery plan, internal status message and improvement ticket. The blind test is a **validation attachment**, not a seventh scored output.

A packet can score highly in its six documentation categories and still fail blind reconstruction. That distinction is the principal instructional contribution of this supplement.

### 4.21.14 Wrong worked handoff

**Incorrect synthetic summary at a later Branch S checkpoint:**

> "The incident lead revoked the account at 09:37 and the problem is fixed. The service has recovered, the backup passed, and the new shift can close the ticket. All evidence is somewhere in the logs."

This confuses the 09:37 proposal with the later 09:45 branch report and broadens a specific session action into an unspecified account revocation. It claims recovery without addressing the B19/B20 mismatch or V1's blank audit actor. It also lacks usable source pointers and responsible owners.

The sentence "all evidence is in the logs" does not tell a new responder where to find R17, the relevant branch card, the approved P1 target, C1 comparison or V1 audit result. A reader may know that the sentence is unsafe, but cannot repair it without consulting the actual permitted sources.

A receiver should refuse to accept the stated closure, record why the source claims fail and request an owner-approved next step. The safe answer does not require inventing an alternative attacker story or recovering a missing source through unauthorized access.

If the handoff was already frozen, the sender cannot make it retroactively correct by saying "I meant only the current session." The correction belongs in a new version with specific evidence and scope.

### 4.21.15 Correct worked handoff

**Correct bounded synthetic Branch S summary after the separately released P1/C1 and V1 cards:**

> "Case HL-IR-001: At the 09:37 Round C checkpoint, R17 and R18 supported reviewing an unexplained B20 edit outside the known approved training list; the bounded session response was proposed then. Branch S later reports revocation of the identified current desk-a session at 09:45, staff reauthentication and a quiet result only inside the branch's query range. Other routes, the human operator and current technical state beyond that report remain unverified. The later P1/C1 comparison shows B19/B20 inconsistent with the approved targets; V1 has limited access passes but a failed actor-attribution field. Full service acceptance is not established. The service owner should decide on a bounded correction request and new comparison; the application/audit owner should repair and retest attribution; the lead reconvenes on a verified unexplained edit or failed retest."

The receiver can locate R17/R18 in Chapter 3, Branch S in Chapter 4 and P1/C1/V1 through their later Chapter 3 teaching cards. The wording distinguishes proposal, reported execution, known test limits and proposed correction. It also does not treat the source set as proving real production recovery.

For an equally defensible Branch P packet, replace the session report with the pause and two pending manual items at 09:45. The service owner must still decide whether or when writes resume and how the queue is reconciled. Never mix the two alternative reports in one chosen branch history.

The packet's adequacy is still subject to an independent receiver test. A model answer written by the author is not evidence that another participant can reconstruct it unaided.

### 4.21.16 Use failed reconstruction to improve the actual packet

The blind exercise should conclude with a short, evidence-linked improvement task. If the receiver incorrectly called the 09:37 proposal executed, specify whether the packet lacked action-state labels or the receiver misinterpreted a clear source. If the receiver could not locate C1, verify whether the manifest contained a working source pointer. If the receiver recommended immediate production correction, check whether the packet clearly marked owner approval as required.

A good improvement ticket has one observed failure, its frozen packet and receiver answer, an owner, a proposed correction, a retest and a pass/fail condition. An example is:

- **Observed defect:** receiver treated the Branch S report as evidence that every session and booking path remained secure.
- **Packet change:** add a separate last-reported action and current-effect-unknown field, with the branch card pointer.
- **Retest:** give the revised sealed packet to a different participant or conduct a separately labeled second round under the same declared checkpoint.
- **Pass:** receiver independently reports the specific last action, its limits, the failed later gates and the next approval request.
- **Fail:** receiver still declares full recovery or proposes an unapproved action.

This turns a vague recommendation to "improve handoffs" into a specific capability test. [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) and [FEMA's exercise-evaluation guidance](https://preptoolkit.fema.gov/web/hseep-resources/policy-and-guidance) support the broader practice of documenting observed exercise performance and corrective actions; the exact card and thresholds here are CyberABC's own.

### 4.21.17 A passing tabletop does not measure real incident capability

The BH4 program checks invented dictionaries, not actual source provenance, live systems or human comprehension. An ordinary participant could correctly answer all six questions in a quiet classroom and still struggle with missing evidence, inaccessible sources or time pressure during an actual event.

A valid exercise report therefore distinguishes **structural packet validity**, **human reconstruction performance** and **operational control verification**. The first can be assisted by a small script. The second requires an observed independent human answer. The third would need appropriate organizational authorization, technical sources and safe tests outside this fictional course.

The exercise should record these boundaries explicitly. A successful BH4 script does not authenticate a GitHub link, execute a write pause, verify an identity provider, fix booking values or certify a backup. A student may use the script to predict failure categories but must still produce a real written reconstruction to demonstrate the intended skill.

An instructor should not turn the classroom score into an accreditation claim. CyberABC is a learning collection; the materials develop reasoning through controlled and auditable practice.

### 4.21.18 Section synthesis and next learning step

The essential outcome is an **independent receiver who can continue a case safely**. The receiver must identify the checkpoint, select the right branch, locate permitted evidence, distinguish proposed from reported executed actions, mark failed and untested service criteria, request the next owner-approved action and identify what would trigger a new decision.

A handoff without those properties may be readable but incomplete. A detailed handoff that falsely declares recovery may be more dangerous than a concise one that exposes the gaps. The safest transfer preserves source pointers, uncertainty and decision authority rather than hiding them inside a polished narrative.

This lesson does not alter the canonical Harbor Library timeline or any already released fixture. It adds a reproducible exercise that makes the sender's documentation and the new receiver's unaided understanding observable and correctable.

---

## BH4 Offline Laboratory — Reconstruction State and Negative Controls

**Classification:** Entirely synthetic, independent BH4 teaching fixture. It is not R1–R24, Branch S/P, P1/C1, V1, F1, F4-AUDIT, L2, DEL4 or an observed production handoff.

**Goal:** Verify the internal structure of a frozen packet and an invented receiver answer. Reject later evidence used prematurely, mixed branches, missing source pointers, action-state rewrites, recovery overclaims, absent owners, unsafe steps, missing triggers and a receiver misunderstanding.

**Environment:** Python 3 standard library, memory only. No network calls, credentials, files, messaging, service changes or real evidence access.

**Fixture scope:** The baseline is a fictional Branch S reconstruction *after* P1/C1 and V1 have been separately released. It keeps Round C action status `PROPOSED`, the later Branch S 09:45 status `REPORTED`, and the present technical effect `NOT_INDEPENDENTLY_VERIFIED`. Its data and audit gates remain failed. A separate valid Branch P variant uses the other mutually exclusive branch. The exact strings are classroom assertions, not authenticated operational receipts.

### Complete Python 3 code

~~~python
from copy import deepcopy

STAGES = {
    "A": 1, "B": 2, "C": 3,
    "D_BRANCH": 4, "D_TARGET": 5, "D_ACCESS": 6,
}
RELEASE = {
    **{f"R{i}": "A" for i in range(1, 9)},
    **{f"R{i}": "B" for i in range(9, 17)},
    **{f"R{i}": "C" for i in range(17, 25)},
    "S": "D_BRANCH", "P": "D_BRANCH",
    "P1": "D_TARGET", "C1": "D_TARGET",
    "V1": "D_ACCESS",
}
ROOT = "MANUSCRIPT.md#"
LOCATOR = {
    "R17": ROOT + "ch-03", "R18": ROOT + "ch-03",
    "S": ROOT + "ch-04", "P": ROOT + "ch-04",
    "P1": ROOT + "ch-03", "C1": ROOT + "ch-03",
    "V1": ROOT + "ch-03",
}
BASE = {
    "checkpoint": "D_ACCESS",
    "branch": "S",
    "refs": ["R17", "R18", "S", "P1", "C1", "V1"],
    "locators": {
        key: LOCATOR[key]
        for key in ["R17", "R18", "S", "P1", "C1", "V1"]
    },
    "C_action": "PROPOSED",
    "D_report": "SESSION_REVOKED_REPORTED_0945",
    "current_effect": "NOT_INDEPENDENTLY_VERIFIED",
    "data_gate": "FAIL_B19_B20",
    "audit_gate": "FAIL_ACTOR",
    "full_service": "NOT_ACCEPTED",
    "next_action": "REQUEST_CORRECTION_PLAN_AND_RETEST",
    "next_owner": "ServiceOwner",
    "next_authority": "OWNER_APPROVAL_REQUIRED",
    "revisit_trigger": "VERIFIED_NEW_EDIT_OR_FAILED_RETEST",
    "receiver": {
        "branch": "S", "C_action": "PROPOSED",
        "D_report": "SESSION_REVOKED_REPORTED_0945",
        "current_effect": "NOT_INDEPENDENTLY_VERIFIED",
        "data_gate": "FAIL_B19_B20",
        "audit_gate": "FAIL_ACTOR",
        "full_service": "NOT_ACCEPTED",
        "next_action": "REQUEST_CORRECTION_PLAN_AND_RETEST",
        "next_owner": "ServiceOwner",
    },
}

def inspect(p):
    refs = set(p["refs"])
    if (
        {"S", "P"}.issubset(refs)
        or (p["branch"] == "S" and "P" in refs)
        or (p["branch"] == "P" and "S" in refs)
    ):
        return "FAIL_BRANCH_MIX"
    if p["branch"] not in {"S", "P"} or p["branch"] not in refs:
        return "FAIL_BRANCH_NOT_GROUNDED"
    bad = sorted(
        ref for ref in refs
        if ref not in RELEASE
        or STAGES[RELEASE[ref]] > STAGES[p["checkpoint"]]
    )
    if bad:
        return "FAIL_FUTURE_OR_UNKNOWN:" + ",".join(bad)
    no_link = sorted(
        ref for ref in refs if not p["locators"].get(ref)
    )
    if no_link:
        return "FAIL_MISSING_POINTER:" + ",".join(no_link)
    if (
        p["C_action"] != "PROPOSED"
        or not p["D_report"].endswith("_REPORTED_0945")
    ):
        return "FAIL_ACTION_HISTORY"
    if p["current_effect"] != "NOT_INDEPENDENTLY_VERIFIED":
        return "FAIL_CURRENT_STATE_OVERCLAIM"
    if (
        p["data_gate"] != "FAIL_B19_B20"
        or p["audit_gate"] != "FAIL_ACTOR"
        or p["full_service"] != "NOT_ACCEPTED"
    ):
        return "FAIL_RECOVERY_OVERCLAIM"
    if not p["next_owner"]:
        return "FAIL_NO_OWNER"
    if (
        p["next_authority"] != "OWNER_APPROVAL_REQUIRED"
        or p["next_action"] != "REQUEST_CORRECTION_PLAN_AND_RETEST"
    ):
        return "FAIL_UNAUTHORIZED_NEXT_STEP"
    if not p["revisit_trigger"]:
        return "FAIL_NO_TRIGGER"
    for key in (
        "branch", "C_action", "D_report", "current_effect",
        "data_gate", "audit_gate", "full_service",
        "next_action", "next_owner",
    ):
        if p["receiver"].get(key) != p[key]:
            return "FAIL_RECEIVER_RECONSTRUCTION:" + key
    return "PASS_BOUNDED_RECONSTRUCTION"

VARIANTS = [
    ("BASE_S", {}),
    ("FUTURE_CARD", {"checkpoint": "D_BRANCH"}),
    ("MIXED_BRANCH", {"refs": BASE["refs"] + ["P"]}),
    (
        "MISSING_POINTER",
        {
            "locators": {
                k: v for k, v in BASE["locators"].items()
                if k != "C1"
            }
        },
    ),
    ("REWRITE_ROUND_C", {"C_action": "REPORTED_EXECUTED"}),
    ("CLAIM_FULL_RECOVERY", {"full_service": "ACCEPTED"}),
    ("NO_NEXT_OWNER", {"next_owner": ""}),
    ("UNSAFE_ACTION", {"next_action": "RESUME_WRITES_NOW"}),
    ("NO_REVIEW_TRIGGER", {"revisit_trigger": ""}),
    (
        "INCORRECT_RECEIVER",
        {"receiver": {**BASE["receiver"], "D_report": "PROPOSED"}},
    ),
]

for name, changes in VARIANTS:
    p = deepcopy(BASE)
    p.update(changes)
    print(name, inspect(p))

# A separate valid Branch P choice, not a combined branch.
p = deepcopy(BASE)
p["branch"] = "P"
p["refs"] = ["P" if v == "S" else v for v in p["refs"]]
p["locators"] = {
    "P" if k == "S" else k: v
    for k, v in p["locators"].items()
}
p["D_report"] = "PAUSE_REPORTED_0945"
p["receiver"] = {
    **p["receiver"],
    "branch": "P",
    "D_report": "PAUSE_REPORTED_0945",
}
print("BASE_P", inspect(p))
~~~

### Exact expected output — executed in Python 3

~~~text
BASE_S PASS_BOUNDED_RECONSTRUCTION
FUTURE_CARD FAIL_FUTURE_OR_UNKNOWN:C1,P1,V1
MIXED_BRANCH FAIL_BRANCH_MIX
MISSING_POINTER FAIL_MISSING_POINTER:C1
REWRITE_ROUND_C FAIL_ACTION_HISTORY
CLAIM_FULL_RECOVERY FAIL_RECOVERY_OVERCLAIM
NO_NEXT_OWNER FAIL_NO_OWNER
UNSAFE_ACTION FAIL_UNAUTHORIZED_NEXT_STEP
NO_REVIEW_TRIGGER FAIL_NO_TRIGGER
INCORRECT_RECEIVER FAIL_RECEIVER_RECONSTRUCTION:D_report
BASE_P PASS_BOUNDED_RECONSTRUCTION
~~~

### Worked interpretation, evidence limits and negative controls

`BASE_S` is a **limited structural pass** for the declared artificial packet, not a human comprehension test or proof of production recovery. `FUTURE_CARD` rejects citing P1/C1/V1 when only the first branch card has been released. `MIXED_BRANCH` rejects incompatible S/P histories. `MISSING_POINTER` makes C1 unlocatable in the artificial manifest. `REWRITE_ROUND_C` refuses to turn the earlier 09:37 proposal into a reported execution.

`CLAIM_FULL_RECOVERY` rejects an unrestricted service-acceptance statement while the canonical teaching comparison still has B19/B20 differences and V1's failed actor. `NO_NEXT_OWNER` blocks an unowned next task. `UNSAFE_ACTION` blocks immediate write resumption without the declared owner-approved plan. `NO_REVIEW_TRIGGER` makes the next review untestable. `INCORRECT_RECEIVER` shows that a structurally complete packet can coexist with a **different, wrong receiver reconstruction**.

`BASE_P` is a separate reset and may pass the same **narrow classroom** consistency rules while using Branch P instead of S. It does not state that the pause remains active at an unknown later moment or that its two pending queue requests were processed.

The script checks literal values and release stages. It does not authenticate real source files, test link availability, perform natural-language comprehension, verify live approvals or record human performance. Even the `receiver` dictionary is a fabricated response, not a real student submission.

**Negative experiment:** Change only the receiver's `D_report` value and observe `FAIL_RECEIVER_RECONSTRUCTION:D_report`; restore it to the reported branch status for the baseline. Alternatively, remove C1's manifest pointer and observe `FAIL_MISSING_POINTER:C1`. Never treat a missing pointer as proof that the booking comparison passed.

**Required lab submission:** Eleven output lines, a per-variant failure table, the identified source-release boundary, a one-paragraph distinction between packet validity and independent human reconstruction, and a proposed next safe request for each selected branch.

---

## Two-Role Practical Exercise — A Handoff Without the Author

**Roles:** Sender and Receiver. A facilitator may evaluate them separately but is not required for the basic two-role activity. All notes concern fictional records only.

**Goal:** Determine whether the receiver can reconstruct the case and select a safe action **without the sender explaining or correcting the packet**.

1. **Declare the stage and branch.** Choose the first Branch D checkpoint or the later D checkpoint after P1/C1/V1; explicitly restrict inputs accordingly. Use only Branch S or only Branch P.
2. **Sender prepares the packet.** Include case ID, release ledger, frozen Round C proposal, selected reported branch, available source pointers, known failed/unknown acceptance criteria, responsible owners and review trigger. Retain the existing six chapter outputs.
3. **Freeze sender version.** Save it as `BH4-packet-v1` with a declared classroom checkpoint. The sender must not silently modify it while the receiver works.
4. **Receiver works alone.** Provide the packet and the permitted synthetic source cards. The sender gives no hints. The receiver writes the six reconstruction answers in §4.21.11 using exact record and card identifiers.
5. **Freeze receiver answer.** Save `BH4-receiver-v1`. The receiver must explicitly state any unlocatable source or uncertain action status rather than guess.
6. **Adjudicate against sources.** Compare the two frozen artifacts with the permitted R-series and cards. Distinguish sender omissions, receiver mistakes and unavailable evidence. Apply the critical safety failures before any ordinary completeness score.
7. **Choose the next safe action.** The receiver identifies the owner-approved correction/retest or, for Branch P, queue-disposition request and resumption condition. The response cannot itself execute a system change.
8. **Retest with a new version if necessary.** Keep the failed original; submit a new packet version and separately frozen reconstruction so improvement can be measured.

**Pass:** The receiver finds the source-supported checkpoint, one branch, proposal/report distinction, failed or unknown gates, next approval owner and trigger; no future cards, invented completed correction or unauthorized action appear.

**Fail:** A critical release or branch error, fabricated approval/execution, unsupported recovery claim or unsafe next action is present. A missing source locator, owner or trigger also blocks a fully satisfactory reconstruction, with a specific fix recorded.

**Evidence to retain:** Sender packet, receiver first answer, source-locator checklist, failed/passed conditions, reviewer explanation and any later version history. These are supplementary test materials, not new numbered exercises or real incident artifacts.

---

## Targeted Refinements to Existing Exercises — No New IDs

Preserve the book's existing EX039–EX050 sequence, 0–2 grading framework and **six scored artifacts**. Only the four specified exercises gain additional cold-receiver checks; their original output formats do not change.

### EX045 — Branch S review

Keep the existing **four-row claim ledger**, with two supported and two unestablished claims, based on **Branch S only and before P1/C1/V1 release**, plus its one authorized next check. Add a **source locator check** to each row: can the independent receiver find the branch pointer and state its limit without contacting the sender? If a pointer is missing, report the missing source rather than a negative booking-state finding. Do not add later cards to the pre-release answer.

### EX046 — Branch P review

Keep the original **queue-and-return note** with two unnamed pending requests, their custodian, write-block evidence limit, proposed owner-approved resumption condition, continued-restriction signal and next checkpoint. Add a blind receiver prompt: "What can you safely say about the two requests, and who may approve resumption?" The receiver must report pending queue work and avoid automatic acceptance or return merely because the fifteen-minute period may have elapsed. Do not use MQ3, P1/C1 or V1 at the Branch P-only checkpoint.

### EX047 — Recovery acceptance

Keep the existing **four-row** return-to-service checklist after the **separate** P1/C1 and V1 releases: booking correctness, authorized access, denied unauthorized access and actor/time audit visibility. Add a receiver task to locate each source and classify its criterion as failed, limited pass or untested. A correct packet explains B19/B20 mismatches and the V1 blank actor without calling full recovery established. The receiver may request owner-approved corrections and retests, not perform unapproved changes.

### EX050 — Final handoff and self-assessment

Keep the required **one-paragraph handoff**, the **six-row 0–2 self-score** and contested-score note. Add BH4 as a **separately labeled validation attachment**, not a seventh scored output: packet/receiver version, available-source set, chosen branch, historical action status, failed gates, next safe request, accountable owner, trigger and result of the independent reconstruction. A correction after sender feedback must be versioned, not backdated.

---

## Supplementary Worked Answers — For the Principal Book's Final Appendix

### EX045 — Additional worked reasoning

At the Branch S-only checkpoint, the specified current `desk-a` session was **reported revoked** at 09:45, and the branch's narrow booking query reported no later matching edits within its queried range. Those are the two bounded supported claims. The identity of the human behind the original edits is not established, and the report does not show that every booking is correct or every access path is closed. A blind receiver should locate the Branch S card in Chapter 4 and explain its narrow scope. P1/C1 and V1 remain withheld; they cannot appear in this four-row answer. If the branch card is missing from the sealed packet, the correct output is a missing-pointer defect and a request for the source, not a claim that revocation failed or booking correctness passed.

### EX046 — Additional worked reasoning

The chosen Branch P card separately reports a fifteen-minute staff-write pause starting at 09:45 and **two pending manual requests**. Their IDs, approvals and final effects are not supplied. A receiving responder should identify the front-desk intake custodian and the service owner who must approve queue reconciliation and any resumption. A planned end around 10:00 does not prove that writes restarted; that requires a separate approved state transition and verification. The receiver must not import Branch S, future P1/C1/V1 results or MQ3's invented request rows. The bounded next step is to request the approved queue manifest and current operating-state check, not silently process requests or resume service.

### EX047 — Additional worked reasoning

Only after P1/C1 and V1 are released, the four-row acceptance answer may say that B17/B18 match the approved P1 target while B19/B20 differ in C1; the booking correctness criterion therefore fails in the limited comparison. V1's permitted test operation and denied unauthorized operation are two **limited passes** in an isolated copy, but its audit actor is blank and the attribution criterion fails. An independent receiver should locate the P1/C1 and V1 cards, maintain those different statuses and request service-owner-approved correction plus a new source-backed comparison and application/audit-owner retest. No supplied card establishes a completed production correction or unrestricted service acceptance.

### EX050 — Additional worked reasoning

An acceptable final handoff clearly states the 09:37 Round C action was a **proposal**, the later chosen Branch S or P card **reported** a specific fictional action at 09:45, and the current effect beyond that report is not independently verified. After later releases, P1/C1 and V1 leave B19/B20 correctness and actor attribution unresolved or failed; accepted full recovery is not proved. The service owner owns correction and acceptance decisions, the application/audit owner owns attribution retesting, and the incident lead owns the next risk review. A verified new unexplained edit or failed retest is an escalation trigger.

The supplementary BH4 attachment should preserve `BH4-packet-v1` and `BH4-receiver-v1` separately, showing which sources the receiver located and which safe next request was selected without sender assistance. It does not change the six scored outputs or the original 12-point denominator. A high document score does not override a future-source leak, branch mixture, invented execution or unauthorized next act. If the receiver initially rewrites the 09:37 proposal as executed, retain that failure and submit a corrected `v2` rather than silently editing the first version.

---

## Synthesis and Continue Studying

A handoff is operationally useful within its declared scope when an unfamiliar receiver can independently locate permitted sources, reconstruct the checkpoint and action history, identify failed and unknown service conditions and choose a safe, accountable next request. A good narrative alone cannot demonstrate that capability. A successfully delivered message alone cannot demonstrate it either.

BH4 provides a reproducible **structural** check and a separate human two-role exercise. Its invented results do not verify any real booking system, identity control, backup or organization-wide readiness.

### Continue studying — chapter 04 of 04 (public supplementary draft)

[← Chapter 03](../MANUSCRIPT.md#ch-03) · [Course chapter index](../../SUBJECTS.md) · [Principal book and worked answers](../MANUSCRIPT.md#answers) · [Next course via chapter index](../../SUBJECTS.md)

**Editorial integration note:** This Markdown is a **transitional public component** of the one principal English book. Its teaching, existing EX045/EX046/EX047/EX050 refinements and worked answers are intended for later integration in the same `MANUSCRIPT.md`. It adds no new numbered subject, exercise or course skill. The book remains a draft pending technical, language, rights and A4 completion review.

### Official primary sources and provenance

- [NIST SP 800-84 — Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final), September 2006: exercise design, conduct and evaluation.
- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), April 2025: risk-managed incident response and coordination.
- [FEMA HSEEP 2020 — Policy and Guidance](https://preptoolkit.fema.gov/web/hseep-resources/policy-and-guidance): exercise objectives, evaluation, after-action records and improvement planning.
- [NIST SP 800-184 — Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final), December 2016: recovery planning and validation.

These sources support general educational methods, not the fictional Harbor Library records, BH4 state labels or test outcomes. The instructional text, synthetic test cards and program are original CyberABC content. Editorial responsibility is assigned only to [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned content follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within documented limits. Third-party works retain their own rights. No real system was accessed or modified.
