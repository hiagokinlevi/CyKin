# Week 1 input review — public integration draft

**Authorship and editorial responsibility: hiagokinlevi.** English rapid Incident Response edition. Revision: `W1-input-01`.

**DRAFT — NOT YET CONSOLIDATED INTO THE PRINCIPAL BOOK.** This is a temporary correction and enrichment batch for the existing **Lessons 01–05 in Chapter 01**, not another principal book, five newly completed lessons, a translation, or an approved edition. The [principal manuscript](MANUSCRIPT.md) remains the course's teaching source. The draft contains five review units, three executable extensions and five supplementary practice tasks with their explained answers at the end. Original EX001–EX050 and their assessment requirements are not renumbered or replaced.

**Source boundary:** the reviewed first-week text was read at repository revision `8f1e55e592556eef7e040d62532745bf49d47e87`, manuscript Git blob `7f28b32e7db8edd813a0e7905ccd685ddab27c11`. Before publication, changes through `c0eccee4b5e81c08598a8e812a2ca1fabff25d96` were compared: the intervening rapid-book change was to VQ2 in Chapter 02, not the first-week passages below. That later manuscript blob is `c8709f94a2f70258695bcd3a3ddf1412d41f22b4`. Git blob identifiers here are version references, not new A4 measurements.

**Why this is a separate draft:** the connected editing interface provides whole-file replacement rather than a bounded patch operation, and the current manuscript exceeds one megabyte. It was not replaced with an incomplete reconstruction. Consolidation, final-book answer placement and removal of this temporary instructional copy remain required. Do not count this file in manuscript coverage or daily-lesson totals.

[Course home](../../README.md) · [Edition](../README.md) · [Native lesson index](../SUBJECTS.md) · [Single course skill](../../skill/SKILL.md) · [Worked review answers](#w1-review-answers) · [Integration checklist](#w1-integration)

| Existing lesson | Review unit | Additional learning, not a repeated chapter |
|---|---|---|
| [01 — Evidence readiness](MANUSCRIPT.md#lesson-01) | [1 — Check the input contract](#w1-review-01) | Separate a source pointer, a declared input frame and a proposition actually supported by that frame. |
| [02 — Booking invariants](MANUSCRIPT.md#lesson-02) | [2 — Do not turn an empty input into a clean schedule](#w1-review-02) | Add explicit coverage and clock-format checks without changing the original booking invariant. |
| [03 — Service paths](MANUSCRIPT.md#lesson-03) | [3 — Reject unknown names; model unknown states](#w1-review-03) | Distinguish an invalid component identifier from an unresolved component state; test all partial states of the five-component model. |
| [04 — Authority rehearsal](MANUSCRIPT.md#lesson-04) | [4 — A string is not a confirmation](#w1-review-04) | Reject implicit Boolean coercion while retaining the existing role, scope, expiry and receipt-binding checks. |
| [05 — Bounded first decision](MANUSCRIPT.md#lesson-05) | [5 — Repair an unsupported observation](#w1-review-05) | Correct a source-overclaim without erasing valid chronology or weakening the original seven-field exercise. |

## Scope and safe use

Read the corresponding native lesson before each review unit. All examples remain paper exercises or in-memory Python fixtures. Do not connect to a real library, account, service, log platform, telephone system or patron database. The programs neither issue permissions nor execute containment. R1–R8 remain the entire canonical Round A packet. BSL1's S-series bookings, PATH1's components and AR1's identities and receipts remain separate teaching fixtures.

For the three code extensions, start a **fresh Python session for each laboratory**. Run that laboratory's complete principal-book listing first, then its extension below. For AR1, run both the original AR1 listing and its request-bound approval listing before the new type gate. This order is a prerequisite, not an optional convenience: the extensions deliberately reuse the original definitions instead of silently replacing them. Do not mix unrelated laboratory globals in one session. No additional package installation is needed.

The examples were executed locally with **Python 3.13.5**, without optimization. The original BSL1, PATH1 and AR1 baseline logic was transcribed from the reviewed source into isolated local test sessions. Their 11, 6 and 19 printed lines, respectively, reproduced; the AR1 total includes its existing four-line receipt-binding supplement. These are scoped program checks, not a byte-for-byte archive verification of the entire book or proof of learner competence.

## What was found, and what was not found

The published BSL1 checker returns an empty findings list for an empty input and accepts `9:00` in its `minute` helper. The published PATH1 function ignores a misspelled component such as `databsae`, because that value intersects none of its dependency sets. Both the original AR1 evaluator and its receipt-binding extension accept the string `"false"` in an otherwise valid confirmation field. These behaviors were reproduced in local copies of the relevant source logic.

Those results are **limitations at the boundary of the teaching inputs**. They do not show a production vulnerability or a real approval failure. The supplied baseline examples still behave as documented. The appropriate improvement is to state and test additional preconditions, not to claim that every conclusion of the existing laboratories was wrong.

Separately, the example incident record in section 1.5 calls the sign-in outside ordinary hours, but the released packet supplies no ordinary-hours policy. This is a wording defect: chronology is supplied; the claimed operating-hours comparison is not.

<a id="w1-review-01"></a>

## Review unit 1 — Check the input contract before interpreting the result

### Objective and distinction

After this unit, explain why a program's correct calculation can still be irrelevant to the intended incident question. Identify three separate things: **the selected source version**, **the declared input frame**, and **the exact proposition being tested**.

Lesson 01 already teaches an evidence-readiness contract: name a useful question, a source, a custodian, collection conditions and a rehearsal. The additional step here is to test the boundary between that contract and the input actually handed to a checker. A table can be internally well formed yet belong to a different version or omit an object required by the decision.

A **source pointer** identifies where the reader should look. It does not by itself establish the truth, completeness or applicability of what is found. A **declared input frame** states which objects the current comparison is supposed to cover. It is not evidence that the frame includes every relevant production object. A **test proposition** states the narrow condition the program can evaluate once those inputs are accepted.

For example, the original BSL1 program can inspect supplied booking intervals. It cannot independently determine whether an exporter omitted a booking, whether its policy was approved for the relevant service, or whether the rows describe the current incident. Those questions do not become true because the overlap function executes correctly.

### A three-stage review

~~~text
Accept the declared input contract?
    no -> reject or request clarification; no business pass
    yes
     |
     v
Evaluate the stated model on those inputs
     |
     v
Report the result within that scope
    + name what the source and model cannot establish
~~~

**Text explanation:** the first stage checks whether the input can be used under this particular contract. The second applies the declared rule. The third prevents a narrow calculation from becoming an unsupported incident finding. None of the arrows authenticates a producer, establishes authorization or supplies a missing record.

Begin by freezing the expected frame before looking at the outcome. Suppose a reviewer is given a declared six-object BSL1 frame, S01–S06. A second file contains only S01 and reports no conflict. That result might be correct **for S01 alone**. It cannot answer the six-object question unless the missing five objects are accounted for. Silently redefining the expected frame to match the returned file would change the question after seeing the answer.

Next inspect field meaning, not only field presence. A field called `confirmed` might contain a Boolean, text, an integer or no value. A value that a programming language treats as true is not necessarily an affirmative statement under the exercise's schema. Unit 4 makes that difference executable.

Finally inspect the sentence the analyst writes. Even an authentic R4 pointer supports the fact that a cancellation was recorded; it does not supply approval, the human actor or a fresh owner-approved booking-state comparison. Type checking is not semantic proof. Conversely, a malformed input is not evidence that a malicious change happened. It is a reason to stop that comparison and seek a usable source.

### Worked example

A proposed review note says: “The checker returned no findings, so all six bookings are safe.” The attached input contains only S01. The first error is a **frame mismatch**, before any question about whether the overlap calculation is correct. The second error is promoting a fixture result into service safety. A defensible replacement is: “No overlap was found in the declared one-row comparison; this input does not answer the six-row rehearsal question or establish a real service state.”

To answer the original question, the reviewer should retain the one-row input and its result, request the missing frame or an explicit owner-approved scope revision, and rerun the relevant comparison. Do not invent the absent rows, infer that they were deleted, or overwrite the first result.

### Supplementary practice W1-R1

**Objective:** separate input admissibility from the meaning of a computed result. **Inputs:** the three reports below, the original R4 limitation, and the BSL1 six-object frame described above. **Required artifact:** three rows containing admissibility decision, narrow supported statement, missing evidence and next bounded request. **Constraints:** no new R-series facts; no production collection; retain both the submitted input and its declared scope.

| Report | Supplied material |
|---|---|
| A | Declared frame S01–S06; only S01 supplied; checker prints no findings. |
| B | Declared frame S01 only; S01 supplied; checker prints no findings. |
| C | R4 is correctly quoted, but the writer concludes that an identified human made an approved cancellation. |

**Assessment:** one point for each correctly reasoned row, one for distinguishing a missing frame from a negative finding, and one for preserving the canonical case boundary. Five points assess this supplementary task only. A claim of real approval, human attribution or safe production state requires correction regardless of the total. [Worked answer](#w1-answer-01).

### Synthesis and Continue studying

A usable input, a correct calculation and a justified operational conclusion are different achievements. Preserve the boundary between them.

[← Native Lesson 01](MANUSCRIPT.md#lesson-01) · [Course index](../SUBJECTS.md) · [Review unit 2 →](#w1-review-02)

<a id="w1-review-02"></a>

## Review unit 2 — Do not turn an empty input into a clean schedule

### Objective and observed behavior

Explain how to reject an incomplete or uninterpretable rehearsal frame while preserving the original booking-rule findings. This unit extends [BSL1](MANUSCRIPT.md#ir-rapid-ch01-bsl1-lab); it does not change its half-open interval convention, confirmed/cancelled status meanings or S01–S06 fixture.

In the original program, `inspect([])` returns `[]`. This is consistent with checking pairs in an empty sequence: there are no supplied conflicting pairs. It is not a demonstration of a healthy six-booking frame. Similarly, `minute("9:00")` returns 540 because the parser converts the two numeric pieces; it does not enforce a two-digit hour representation. The original baseline uses well-formed strings, so its existing results are not invalidated by these probes.

The proposed guard makes the rehearsal's additional contract explicit. The expected identifiers must be a nonempty frozen set; each row must contain five nonempty strings; clock fields must use exactly two ASCII digits, a colon and two ASCII digits, with valid hour/minute ranges; statuses must have the two defined meanings; identifiers must be unique and exactly match the declared frame.

These are **local teaching conventions**, not universal requirements for real booking APIs. An actual service may validly use JSON lists, other status models or a different timestamp representation. It needs its own documented interpretation. The [Python regular-expression documentation](https://docs.python.org/3/library/re.html#re.fullmatch) explains full-string matching; it does not prescribe our time or booking contract.

### Why the duration finding must survive

S06 has equal start and end times. Both fields are interpretable under the clock contract. The original invariant therefore still reports `INVALID_INTERVAL S06`; the guard does not quietly repair the end time, drop the row or reinterpret it as a cancellation. Input admission and business-rule findings remain separate.

The same distinction applies to a complete frame that contains a genuine modeled conflict. A good guard must admit the interpretable rows and let the original rule report the conflict. Rejecting every problematic input would prevent the learner from seeing the business condition the laboratory is designed to teach.

### Reproducible BSL1 extension

Run the complete original BSL1 listing first in a fresh session. Predict five new lines before running the following extension. The result is conditional on the supplied expected frame; neither identifier equality nor strict syntax authenticates a source.

~~~python
# Run after the complete BSL1 listing, in the same Python session.
import re

W1_BSL_EXPECTED = frozenset({"S01", "S02", "S03", "S04", "S05", "S06"})

def w1_inspect_scoped(rows, expected_ids=W1_BSL_EXPECTED):
    if type(expected_ids) is not frozenset or not expected_ids:
        raise ValueError("INVALID_EXPECTED_SCOPE")
    if any(type(item) is not str or not item.strip() for item in expected_ids):
        raise ValueError("INVALID_EXPECTED_SCOPE")
    if type(rows) not in (list, tuple) or not rows:
        raise ValueError("EMPTY_OR_INVALID_INPUT")
    ids = []
    for row in rows:
        if type(row) not in (list, tuple) or len(row) != 5:
            raise ValueError("INVALID_ROW_SHAPE")
        if any(type(item) is not str or not item.strip() for item in row):
            raise ValueError("INVALID_FIELD_TYPE")
        row_id, room, start, end, status = row
        ids.append(row_id)
        for text in (start, end):
            if re.fullmatch(r"[0-9]{2}:[0-9]{2}", text) is None:
                raise ValueError("CLOCK_FORMAT")
            minute(text)  # Reuse BSL1's hour/minute range check.
        if status not in {"CONFIRMED", "CANCELLED"}:
            raise ValueError("UNKNOWN_STATUS")
    if len(ids) != len(set(ids)):
        raise ValueError("DUPLICATE_ID")
    if frozenset(ids) != expected_ids:
        raise ValueError("COVERAGE_MISMATCH")
    return inspect(rows)  # Preserve BSL1's overlap/duration findings.

def w1_show_bsl(label, rows, expected_ids=W1_BSL_EXPECTED):
    try:
        issues = w1_inspect_scoped(rows, expected_ids)
    except ValueError as error:
        print(label, "INPUT_REJECTED", str(error))
    else:
        print(label, "EVALUATED", ";".join(issues) if issues else "NO_FINDINGS_IN_SCOPE")

w1_bad_clock = [
    (row[0], row[1], "9:00", row[3], row[4]) if row[0] == "S01" else row
    for row in BOOKINGS
]
w1_show_bsl("W1_BASE", BOOKINGS)
w1_show_bsl("W1_EMPTY", [])
w1_show_bsl("W1_MISSING_S04", [r for r in BOOKINGS if r[0] != "S04"])
w1_show_bsl("W1_BAD_CLOCK", w1_bad_clock)
w1_show_bsl("W1_NARROW_SCOPE", [BOOKINGS[0]], frozenset({"S01"}))
~~~

The last call deliberately declares a different one-object frame. It is not a repaired version of the six-object test. Keep those two reports separate. Also retain the original BSL1 status-change and omitted-row sensitivity demonstrations: they teach what the unguarded model sees, whereas this extension teaches whether a result answers a predeclared frame.

### Supplementary practice W1-R2

**Objective:** diagnose empty, missing and malformed input without suppressing valid invariant findings. **Inputs:** BSL1's six original rows and the five calls above. **Required artifact:** the five-line output, a five-row explanation of admission versus invariant result, and one proposed source request for the missing-S04 case. **Constraints:** preserve S06 unchanged; do not modify the original `BOOKINGS`; do not redefine the six-object frame to obtain a green result. Explain whether checking identifiers proves authentic or complete real-world collection.

**Assessment:** one point each for the unchanged baseline findings, empty-input rejection, missing-row rejection, strict clock explanation, and correctly limited one-row result. Claims of source authentication or service repair must be corrected. Original EX002, EX005 and EX010 keep their two-row, four-row and two-sentence requirements; this supplementary artifact is not inserted into those required fields. [Worked answer](#w1-answer-02).

### Synthesis and Continue studying

“No findings in the supplied rows” is not the same claim as “the intended input was complete,” and neither is a universal service-safety finding.

[← Review unit 1](#w1-review-01) · [Course index](../SUBJECTS.md) · [Review unit 3 →](#w1-review-03)

<a id="w1-review-03"></a>

## Review unit 3 — Reject unknown names; model unknown states

### Objective and counterexample

Distinguish an **invalid component identifier** from a **valid component with unknown state**. Then explain why a known failed prerequisite can establish modeled impairment even when another prerequisite is unresolved.

The original [PATH1](MANUSCRIPT.md#ir-rapid-ch01-path1-lab) evaluates a set of failed components. If the supplied set is `{"databsae"}`, the misspelled name intersects none of the five route dependency sets. The original function consequently returns every modeled function as available. This is a reproducible input-boundary limitation, not a report that a database or real service was healthy.

An identifier guard should reject that spelling rather than guess that the writer intended `database`. Silent correction could conceal a wrong source, a schema change or a different component. Request an explicit corrected input and preserve the original one.

A different problem arises when `database` is spelled correctly but its state is not known. Rejecting its name would be wrong; entering `False` would invent an outage; entering `True` would invent availability. The extension uses `None` to represent this narrowly defined unknown condition, with every component explicitly present in the state dictionary.

### Reason through three states

PATH1 defines each route as an **all-required** set. Under that model, a function is:

| Classification | Meaning under the declared dependency model |
|---|---|
| `IMPAIRED` | At least one required component is explicitly false. |
| `UNRESOLVED` | No required component is false, but at least one is unknown. |
| `POSSIBLE` | Every required component is explicitly true. |

Consider staff editing, which requires web, identity and database. With web and identity true and database unknown, the route is unresolved. With web true, identity false and database unknown, the route is impaired regardless of how the database uncertainty is later resolved. The known failed prerequisite is sufficient **within this model**. That conclusion does not identify the cause of a real outage, quantify harm or establish that an alternate architecture is absent.

Manual intake depends only on helpdesk in PATH1. If helpdesk is true, that route can remain possible while staff editing is impaired. “Possible” still means a modeled route, not a confirmed room booking, an approved fallback procedure or observed delivery of service.

### Reproducible PATH1 extension

Run the complete original PATH1 listing first in a fresh session. Predict the first four new lines manually. The final loop checks all `3^5 = 243` partial assignments across the five components. For each assignment, it enumerates every complete Boolean assignment consistent with the declared unknowns and compares each function's possible outcomes with the three-state classification.

This comparison is an independent calculation over a **finite declared model**. It does not verify real topology, measurements, permissions, alternate paths or service correctness. For real systems, the assumptions themselves require authorized observation and owner review.

~~~python
# Run after the complete PATH1 listing, in the same Python session.
W1_COMPONENTS = frozenset().union(*ROUTES.values())

def w1_assess_failed(failed):
    if type(failed) not in (set, frozenset):
        raise ValueError("INVALID_FAILURE_SET")
    if not failed.issubset(W1_COMPONENTS):
        raise ValueError("UNKNOWN_COMPONENT")
    return assess_failed(failed)

def w1_assess_state(state):
    if type(state) is not dict or set(state) != set(W1_COMPONENTS):
        raise ValueError("COMPONENT_SET_MISMATCH")
    if any(value is not None and type(value) is not bool for value in state.values()):
        raise ValueError("INVALID_COMPONENT_STATE")
    result = {}
    for function, needs in sorted(ROUTES.items()):
        values = [state[component] for component in needs]
        if any(value is False for value in values):
            result[function] = "IMPAIRED"
        elif any(value is None for value in values):
            result[function] = "UNRESOLVED"
        else:
            result[function] = "POSSIBLE"
    return result

try:
    w1_assess_failed({"databsae"})
except ValueError as error:
    print("W1_TYPO", str(error))
w1_state = {component: True for component in W1_COMPONENTS}
w1_state["database"] = None
print("W1_UNKNOWN_DB", w1_assess_state(w1_state)["staff_edit"])
w1_state["identity"] = False
print("W1_UNKNOWN_DB_IDENTITY_DOWN", w1_assess_state(w1_state)["staff_edit"])
print("W1_MANUAL", w1_assess_state(w1_state)["manual_intake"])

# Independent finite check: compare each partial assignment with every
# complete Boolean assignment consistent with it. No real system is queried.
from itertools import product
w1_names = sorted(W1_COMPONENTS)
w1_checked = 0
for values in product((False, True, None), repeat=len(w1_names)):
    partial = dict(zip(w1_names, values))
    unknown = [name for name in w1_names if partial[name] is None]
    completions = []
    for fill in product((False, True), repeat=len(unknown)):
        complete = {**partial, **dict(zip(unknown, fill))}
        completions.append(complete)
    actual = w1_assess_state(partial)
    for function, needs in ROUTES.items():
        outcomes = {all(complete[name] is True for name in needs) for complete in completions}
        expected = ("POSSIBLE" if outcomes == {True} else
                    "IMPAIRED" if outcomes == {False} else "UNRESOLVED")
        if actual[function] != expected:
            raise AssertionError((partial, function, actual[function], expected))
    w1_checked += 1
print("W1_PARTIAL_STATES_CHECKED", w1_checked)
~~~

### Supplementary practice W1-R3

**Objective:** justify a result under incomplete component knowledge. **Inputs:** the five PATH1 functions, their original dependencies and the extension above. **Required artifact:** the five-line transcript; a table for all five functions with database unknown and all other components true; a second table after identity alone becomes false; and a two-sentence service-owner message distinguishing modeled intake from confirmed booking acceptance. **Constraints:** do not turn unknown into false, repair the typo silently, or import any modeled failure into R1–R8.

**Assessment:** one point each for typo rejection, the first complete function table, the second complete table, the limited service-owner message, and explaining what the finite enumeration does not verify. The original EX003 still requires its two dependency cards; this table is separate supplementary practice. [Worked answer](#w1-answer-03).

### Synthesis and Continue studying

An invalid name is an input defect. An unknown state is an unresolved premise. A known failed prerequisite can settle a modeled route without settling every other uncertainty.

[← Review unit 2](#w1-review-02) · [Course index](../SUBJECTS.md) · [Review unit 4 →](#w1-review-04)

<a id="w1-review-04"></a>

## Review unit 4 — A string is not a confirmation

### Objective and mechanism

Explain why a type check belongs before authority evaluation, and why it must not replace the authority evaluation itself.

The original [AR1](MANUSCRIPT.md#ir-rapid-ch01-ar1-lab) reads `if not item["confirmed"]`. Under [Python's documented truth-value rules](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), a nonempty string is truthy. Consequently the characters `"false"` do not behave like the Boolean `False`. Converting that string with `bool()` does not fix the meaning. Similarly, equality tests alone can blur Boolean and integer values; this teaching gate intentionally requires the exact Boolean type.

The defect is not that AR1's original `confirmed=False` test was wrong: that baseline still produces a hold. The additional counterexample uses a different type. In the reviewed source, the otherwise valid request with `confirmed="false"` passes both the original routing function and the later request-bound receipt check. The receipt check protects request association, not Boolean field interpretation. Two useful controls can therefore coexist with an untested input boundary.

This demonstration concerns the **toy validator only**. Its original confirmation flag was already a simulated premise, not a real callback or identity proof. The new type gate prevents one category of unintended interpretation; it cannot make the supplied flag an authenticated fact.

### Preserve separate checks

Keep these questions in order: is the field interpretable under this contract; does the confirmation actually say true; does the current role and delegation cover the exact request; is the receipt bound to that request; and what real-world proof would be required before relying on any of those premises?

The proposed wrapper checks the shape of the approval container and exact Boolean types for confirmation, escalation and the current registry's revocation flag. It then calls the **existing** receipt-bound evaluator, retaining the original role, custodian, scope and time checks. This is deliberately not a complete schema validator: missing unrelated fields, malformed timestamps, arbitrary custom objects and authenticity remain outside its claimed coverage.

Do not map all unexpected text to false. A schema mismatch and an explicit negative confirmation are different findings. Do not automatically escalate malformed input because a string happens to be truthy. The safe outcome is a visible input hold and a request for a correctly typed, source-supported record.

### Reproducible AR1 extension

Run the original AR1 program **and** its request-bound approval listing in a fresh session. The extension below does not edit `BASE`, `PAUSE` or their nested approvals; changed examples use independent copies. Predict eight new output lines. Pay particular attention to the exact 14:30 endpoint: the delegate's end is exclusive in the original contract.

~~~python
# Run after AR1 AND its request-bound approval listing, in the same session.
# This adds a narrow type gate. It is not a full request-schema validator.
def w1_evaluate_typed(card):
    if type(card) is not dict or type(card.get("approvals")) is not dict:
        return "HOLD_INPUT_APPROVAL_SHAPE"
    if type(card.get("escalate")) is not bool:
        return "HOLD_INPUT_ESCALATE_TYPE"
    if type(REGISTRY["delegation"].get("revoked")) is not bool:
        return "HOLD_INPUT_REVOCATION_TYPE"
    for item in card["approvals"].values():
        if type(item) is not dict or type(item.get("confirmed")) is not bool:
            return "HOLD_INPUT_CONFIRMATION_TYPE"
    # Do not replace the role/scope/time/receipt checks with the type check.
    return evaluate_with_approval_binding(card)

w1_text_false = deepcopy(valid_audit)
w1_text_false["approvals"]["incident_lead"]["confirmed"] = "false"
w1_real_false = deepcopy(valid_audit)
w1_real_false["approvals"]["incident_lead"]["confirmed"] = False
print("W1_ORIGINAL_TEXT_FALSE", evaluate_with_approval_binding(w1_text_false))
print("W1_TYPED_TEXT_FALSE", w1_evaluate_typed(w1_text_false))
print("W1_TYPED_REAL_FALSE", w1_evaluate_typed(w1_real_false))
print("W1_TYPED_VALID", w1_evaluate_typed(valid_audit))
print("W1_TYPED_REUSED_RECEIPT", w1_evaluate_typed(reused_receipt))
for clock in ("13:00", "14:29", "14:30"):
    card = {**valid_pause, "as_of": utc("2026-09-15T" + clock + "Z")}
    print("W1_DELEGATE_" + clock, w1_evaluate_typed(card))
~~~

### Supplementary practice W1-R4

**Objective:** distinguish input rejection, explicit nonconfirmation, request-scope rejection and delegation expiry. **Inputs:** the original AR1 rules, issued synthetic receipts, and the eight calls above. **Required artifact:** eight output lines; a four-row comparison of text false, Boolean false, valid true and reused receipt; plus a three-time delegation check for 13:00, 14:29 and 14:30. Explain why passing the new type gate is not a new approval.

**Constraints:** do not add real credentials or callback details; keep the issued receipt binding unchanged; use the original half-open delegate interval; preserve EX006's four responsibility rows and EX013's three-row gap register plus ticket. **Assessment:** one point each for the type distinction, explicit false hold, preserved receipt binding, exact expiry boundary and refusal to claim real authorization. [Worked answer](#w1-answer-04).

### Synthesis and Continue studying

A correctly typed Boolean is a usable field, not authenticated consent. A request-bound receipt and a type gate address different failure modes; neither replaces the other.

[← Review unit 3](#w1-review-03) · [Course index](../SUBJECTS.md) · [Review unit 5 →](#w1-review-05)

<a id="w1-review-05"></a>

## Review unit 5 — Repair an unsupported observation without erasing evidence

### Objective and source correction

Revise a claim that exceeds its source while preserving useful chronology, uncertainty and the exact original exercise format.

The example record in section 1.5 currently says that two booking edits followed a sign-in **outside ordinary hours**. R1 provides the 08:40 sign-in time; R3 and R4 provide the 08:43 and 08:44 edit times. R6 reports scheduled training from 08:30 to 09:00. None of those records defines ordinary operating hours or an approved sign-in schedule. The chronology is supported; the ordinary-hours comparison is not.

Do not replace the unsupported statement with its opposite. The packet also does not prove that the sign-in was ordinary or approved. A good correction removes the unsupported qualifier and keeps the question open.

**Proposed replacement for the section 1.5 Observation cell:**

> R1 records a staff-account sign-in at 08:40 UTC; R3 and R4 record booking changes at 08:43 and 08:44 UTC. Ordinary operating hours and authorization of these changes are not supplied.

**Proposed section 1.6 heading:** `Worked example: a sign-in followed by booking changes`.

The shared Round A preview also calls its scope “Chapters 01–05.” In this edition those are **Lessons 01–05 within Chapter 01**. Correct that label without moving the records or changing their release boundary. The hypothetical introductory example in Lesson 01 may still discuss what an unusual-hour alert could say; it must remain visibly hypothetical rather than a new fact about R1.

### Trace support at the level of the sentence

A sentence can mix a valid observation with an unsupported qualifier. A reviewer should not classify the entire sentence as either perfectly supported or entirely useless. Split it into propositions: a sign-in was reported; two later edits were reported; the time was unusual; the edits were approved; a human identity was established. The first two have pointers in the packet; the others need evidence not supplied there.

This method also prevents a style edit from becoming a factual change. Replacing “recorded cancellation” with “unauthorized cancellation” is not merely stronger wording. It adds a decision about permission. Replacing “patron reported a problem” with “the service failed” adds independent verification. A useful correction log records the original wording, the unsupported addition, the narrow replacement and the evidence needed to revisit it.

The [NIST SP 800-61 Rev. 3 publication](https://csrc.nist.gov/pubs/sp/800/61/r3/final) situates incident response within cybersecurity risk management, and the [CSF 2.0 publication](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) describes organizational cybersecurity outcomes. Those sources provide context, not Harbor Library facts or a prescribed wording template. The seven-field correction below is original editorial reasoning over the supplied exercise.

### Supplementary practice W1-R5

**Objective:** produce an evidence-bounded intake record. **Inputs:** R1–R8, the original section 1.5 `HL-IR-001` and `T-104` context, the 09:00 intake checkpoint, and EX007's requirements. **Required artifact:** exactly seven labeled fields in the original order: case ID/open time; service; reporter/source; observed signal with pointers; assessment/uncertainty; scope/authority; next question/owner/review. Add a separate one-sentence correction note explaining the removed ordinary-hours qualifier.

**Constraints:** do not claim a completed interview, collection, restriction, 09:05 decision, confirmed compromise or tested restore at the 09:00 intake. Keep the patron report distinct from verified booking-state harm. **Assessment:** one point each for correct time and source context, bounded observation, explicit unresolved authorization/state, permitted scope, and a proposed owner/review route. A seven-field form containing unsupported facts must still be corrected. This supplements EX007; it does not create EX051. [Worked answer](#w1-answer-05).

### Synthesis and Continue studying

A good correction narrows the claim to its evidence without erasing the evidence. The absence of an operating-hours rule establishes an unknown, not an ordinary or extraordinary event.

[← Review unit 4](#w1-review-04) · [Course index](../SUBJECTS.md) · [Native Lesson 06 →](MANUSCRIPT.md#lesson-06)

<a id="w1-review-answers"></a>

# Final appendix — worked review answers

These answers belong to W1-R1–W1-R5 in this temporary draft. They do not replace the principal book's EX001–EX050 answers. During consolidation, move each answer into the **same principal book's final worked-results appendix**, preserving its dedicated anchor and updating its exercise link.

<a id="w1-answer-01"></a>

## W1-R1 — Worked answer

| Report | Admissibility and supported conclusion | Missing evidence and bounded next step |
|---|---|---|
| A | The input does not satisfy the declared six-object frame. The one-row calculation may be correct but cannot answer the announced question. | Request the missing objects or a separately justified scope revision. Retain the partial input and do not call it a complete clean result. |
| B | The one-object frame is satisfied. No overlap in that declared input is a narrow model result. | A six-object question, real source completeness, approved policy applicability and production correctness remain untested. Do not inflate the conclusion. |
| C | The R4 pointer supports a recorded cancellation, not the appended human-identity or approval claims. | Request the approved task context and appropriate authorized identity evidence through their owners; do not report those checks as performed. |

Report A is not equivalent to a complete frame with no findings. Report B is not intrinsically invalid merely because it is small: its stated scope is different. Report C illustrates a semantic overclaim that a row-count validator would not detect. A correct answer preserves all three distinctions and keeps model fixtures outside the canonical incident ledger.

[Return to the task](#w1-review-01) · [Course index](../SUBJECTS.md)

<a id="w1-answer-02"></a>

## W1-R2 — Worked answer

The executed five-line extension transcript is:

~~~text
W1_BASE EVALUATED CONFLICT S03/S04;INVALID_INTERVAL S06
W1_EMPTY INPUT_REJECTED EMPTY_OR_INVALID_INPUT
W1_MISSING_S04 INPUT_REJECTED COVERAGE_MISMATCH
W1_BAD_CLOCK INPUT_REJECTED CLOCK_FORMAT
W1_NARROW_SCOPE EVALUATED NO_FINDINGS_IN_SCOPE
~~~

The base frame is admitted because its six identifiers and interpretable fields satisfy the new contract. It still contains the original S03/S04 conflict and S06 zero-duration finding. A reviewer who removes S06 to make the test look cleaner changes the evidence instead of correcting the model.

The empty input is rejected before interpretation. Removing S04 fails the expected-frame comparison; the wrapper therefore does not present the reduced conflict count as an answer to the original six-object question. The bounded follow-up is to ask the rehearsal custodian for the declared missing object or an explicit revised scope, not to invent its content.

The `9:00` input fails this extension's exact format rule even though the original parser can interpret it numerically. That difference is a documented choice about the toy input contract, not proof that all one-digit hours are invalid in real systems.

The last call deliberately asks a one-object question. Its no-findings result remains restricted to that declared frame. Matching expected identifiers demonstrates neither authenticity nor that the expected set represents every relevant object in an actual service.

[Return to the task](#w1-review-02) · [Original BSL1 result](MANUSCRIPT.md#ir-rapid-ch01-bsl1-result)

<a id="w1-answer-03"></a>

## W1-R3 — Worked answer

The executed five-line transcript is:

~~~text
W1_TYPO UNKNOWN_COMPONENT
W1_UNKNOWN_DB UNRESOLVED
W1_UNKNOWN_DB_IDENTITY_DOWN IMPAIRED
W1_MANUAL POSSIBLE
W1_PARTIAL_STATES_CHECKED 243
~~~

| Function | Database unknown; every other component true | Database unknown; identity false; other components true |
|---|---|---|
| `site_reachable` | `POSSIBLE` | `POSSIBLE` |
| `room_view` | `UNRESOLVED` | `UNRESOLVED` |
| `staff_edit` | `UNRESOLVED` | `IMPAIRED` |
| `manual_intake` | `POSSIBLE` | `POSSIBLE` |
| `new_backup_job` | `UNRESOLVED` | `UNRESOLVED` |

The identity failure changes staff editing because identity is required for that function. It does not settle the database state or affect functions that do not depend on identity in this model. With a known false prerequisite, every completion of the remaining unknowns still leaves the staff-edit conjunction false. With only the database unknown, some completions permit the route and others impair it, so unresolved is the appropriate classification.

An acceptable two-sentence message is: “In the independent PATH1 model, staff editing is impaired when identity is false, while database-dependent viewing remains unresolved. Help-desk intake remains structurally possible, but no approved fallback procedure, confirmed reservation or actual service result has been demonstrated.”

The final loop checks 243 partial assignments and five function classifications per assignment, or 1,215 model comparisons. It neither authenticates component states nor validates the dependency table against a real system. The six original all-known PATH1 scenarios were also checked through the identifier guard without changing their outputs.

[Return to the task](#w1-review-03) · [Original PATH1 result](MANUSCRIPT.md#ir-rapid-ch01-path1-result)

<a id="w1-answer-04"></a>

## W1-R4 — Worked answer

The executed eight-line transcript is:

~~~text
W1_ORIGINAL_TEXT_FALSE REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_TYPED_TEXT_FALSE HOLD_INPUT_CONFIRMATION_TYPE
W1_TYPED_REAL_FALSE HOLD_CONFIRMATION_MISSING
W1_TYPED_VALID REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_TYPED_REUSED_RECEIPT HOLD_RECEIPT_SCOPE_MISMATCH
W1_DELEGATE_13:00 REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_DELEGATE_14:29 REHEARSAL_PATH_VALID_NOT_EXECUTED
W1_DELEGATE_14:30 HOLD_DELEGATION_EXPIRED
~~~

| Input | Interpretation |
|---|---|
| Text `"false"` | Invalid confirmation type under the declared Boolean contract; the new wrapper stops before authority evaluation. |
| Boolean `False` | Interpretable explicit nonconfirmation; the existing confirmation check holds the request. |
| Boolean `True` with all original valid premises | Type gate passes; the unchanged authority and receipt checks produce a simulated valid path, not execution. |
| Reused receipt for TR-02 | Well-typed confirmation does not repair the request mismatch; the existing binding check still holds it. |

The delegation starts inclusively at 13:00 and ends exclusively at 14:30. Therefore 13:00 and 14:29 can satisfy the time condition; 14:30 cannot. The source fixture's other role, scope and confirmation premises are still required at each time. The boundary test is not permission to execute after a prior check has passed.

The new type check does not verify a real callback, prove consent, authenticate an issuer or create a delegation. It also does not fully validate every request field. A correct improvement ticket identifies this specific input class, preserves the existing valid and invalid authority tests, and leaves broader schema and identity assurance as separate work.

[Return to the task](#w1-review-04) · [Original AR1 result](MANUSCRIPT.md#ir-rapid-ch01-ar1-result)

<a id="w1-answer-05"></a>

## W1-R5 — Worked answer

| Original seven-field format | Evidence-bounded 09:00 intake entry |
|---|---|
| 1. Case ID and opened at | `HL-IR-001`; 2026-10-11 09:00 UTC. |
| 2. Service | Harbor Library room booking; service owner to be confirmed. |
| 3. Reporter and source | Help-desk ticket `T-104` from the section 1.5 case context; R5 records the 08:48 patron report that B18 disappeared. |
| 4. Observed signal with pointers | R1 records the 08:40 `desk-a` sign-in; R3 records the 08:43 B17 move; R4 records the 08:44 B18 cancellation; R5 records the later patron report. |
| 5. Assessment and uncertainty | Investigate the reported changes and symptom. Compromise, human actor, task approval, ordinary operating hours and correct current booking state are not established. R6 supplies a scheduled training interval, not approval of these changes. |
| 6. Permitted scope and authority | Read, annotate and compare the supplied synthetic R1–R8 packet. No new collection, real-system access or disruptive action is authorized by this exercise. |
| 7. Next question, owner and review | Propose that the incident lead coordinate a service/training-owner check of whether B17/B18 were approved tasks before the 09:05 decision checkpoint; retain the section 1.5 09:15 review as a later planned review, not a performed action. |

**Correction note:** The ordinary-hours qualifier was removed because the packet does not supply the policy needed to compare the 08:40 sign-in with normal operating hours.

The note does not establish the opposite claim that the sign-in was ordinary. It preserves valid source ordering while separating the patron report from a verified state comparison. The proposed 09:05 checkpoint and planned 09:15 review are not source-event timestamps and are not recorded as completed decisions at 09:00.

Alternative wording is acceptable when the same seven fields, evidence limits, pending-owner status and proposed actions remain explicit. A shorter record that omits the source limit is not improved merely by being concise.

[Return to the task](#w1-review-05) · [Original EX007 answer](MANUSCRIPT.md#ex007--worked-result) · [Next native lesson](MANUSCRIPT.md#lesson-06)

<a id="w1-integration"></a>

# Editorial integration and verification checkpoint

**Actually completed for this draft:** source-grounded review of the selected first-week passages; local reproduction of the BSL1 11-line, PATH1 six-line and AR1 19-line baseline sequences; execution of all three new extensions; the 243-state/1,215-comparison PATH1 finite check; and 56 additional local regression checks covering malformed clocks, missing/duplicate rows, expected-frame errors, unknown components, invalid state types, strict confirmation/escalation/revocation types and preservation of selected valid/receipt-bound outcomes. These counts describe specific checks, not a percentage of whole-book verification.

The new extension transcripts contain five BSL1 lines, five PATH1 lines and eight AR1 lines. The three code blocks above are the student-facing extensions; the extra operational regression harness is not a new course resource or a claim of independent expert review. No network target, production account, restore operation or student performance was tested. No A4 render, translation audit, website deployment or complete-book approval was performed.

## Exact consolidation steps still pending

1. Re-read the current `MANUSCRIPT.md` and compare its SHA and affected passages with the pinned source above. Preserve concurrent edits, including the Chapter 02 VQ2 work. Do not overwrite the book with this draft.
2. Integrate unit 1 after the existing Lesson 01 evidence-readiness discussion; unit 2 after the complete BSL1 listing; unit 3 after the complete PATH1 listing; and unit 4 after AR1's existing request-bound approval listing. Preserve all original examples and output transcripts. Make the added guards the documented entry points for the new probes, not replacements for the baseline demonstrations.
3. In Lesson 05, apply the exact observation-cell and section-heading corrections above. Correct the shared packet's “Chapters 01–05” label to “Lessons 01–05 in Chapter 01.” Retain the original R1–R8 facts, case times and EX007 format.
4. Move the five supplementary answers into the principal book's final appendix and verify every prompt-to-answer and previous/index/next link. Retain original EX001–EX050 and their rubrics. W1-R1–W1-R5 remain supplementary identifiers, not five new native days.
5. Update the single course skill's BSL1, PATH1 and AR1 instructions to distinguish the original transcripts from the new input-guard practice, the exact prerequisites, and the limited verification claims. Do not create a second skill.
6. Re-run the combined listings from their final book locations, check source and navigation consistency, then remove this temporary instructional copy from the current tree while preserving Git history and updating its referring links. Record the actual integrated revision before changing any manuscript coverage or page status.

**Next editorial position:** consolidate and verify this first-week batch in native Lessons 01–05 and their final answers; then continue the sequential review at **Lesson 06 — A bounded triage question and revisable priority**, comparing the current Chapter 02 source rather than an older copy. The learner's existing next lesson remains determined by [SUBJECTS.md](../SUBJECTS.md), not by this editorial checkpoint.

Original maintainer-owned material follows [CC0 1.0](../../../../../LICENSE) within [RIGHTS.md](../../../../../RIGHTS.md). Python and NIST references remain external works with their own rights. No external source is presented as certifying these original fixtures or this draft.
