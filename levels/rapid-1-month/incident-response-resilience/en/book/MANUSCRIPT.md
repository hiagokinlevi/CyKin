**Premise check before running the lab:** `custodian_available=True` is a classroom contact-routing default that means no failed-contact variant has been supplied. It is not a recorded successful contact, and R1–R16 do not say that a custodian answered. Every `<flag>_verified` value supplied in a variant is a declared hypothetical premise, not something the function verifies. `TASK_SCOPE_NARROWED` labels concern the B19 task-authorization question; they do not establish cause or a human actor.

**Activity-scope contract:** In one TRI2 input, `fresh_edit_verified=True` asserts at least one matching new edit, while `no_new_edits_verified=True` asserts none, for the **same object set, account/event predicate, source-coverage universe and half-open observation interval**. Freeze those details in a separate note before using the flags. Both assertions cannot hold for that one scope. A false flag means that its positive assertion is not supplied; it does not prove the opposite. The function does not receive the scope note, query manifest or timestamps and therefore cannot verify them. Do not combine findings from different windows into one input. `quiet_summary=True` is only a supplied summary, not verified absence; it may coexist with a fresh-edit finding. The added guard enforces this declared logical contract, not the truth of any source.

~~~python
from copy import deepcopy

RELEASES = {

    if c["claim_human_from_shared"]:
        return ["BLOCK_ACCOUNT_NOT_PERSON"]
    if c["fresh_edit_verified"] and c["no_new_edits_verified"]:
        return ["BLOCK_CONFLICTING_ACTIVITY_PREMISES"]
    if c["fresh_edit_verified"] and c["request_downgrade"]:
        return ["BLOCK_FRESH_ACTIVITY_DOWNGRADE"]

    labels = [

For the executed output, scenario interpretation and negative controls, read the [TRI2 worked result](#ir-rapid-ch02-tri2-result) in the final answer appendix. Predict the labels before opening the result.

<a id="ir-rapid-ch02-tri2-scope-check"></a>

##### Check the scope before treating two findings as a contradiction

A **contradiction** here means asserting both that a qualifying event exists and that no qualifying event exists in the same bounded set. It does not mean merely receiving two different-looking reports. Write the object, event predicate, source coverage and interval beside each claim before deciding whether they conflict. A policy authorizing an operation and a record of that operation are not contradictory claims; the earlier two-question example explains why authorization and service correctness must remain separate.

**Worked synthetic example, not R-series evidence.** On one fictional day, use UTC and the interval `[10:00, 10:10)` for edits to invented booking X31 under account Q7. A declared verified finding places a matching edit at 10:04. Another declared verified finding claims complete coverage and no matching edits anywhere in that same interval. The existence finding supplies a counterexample to the absence claim. Entering both flags as true must block the model's conclusion while the disagreement is investigated; it cannot establish which source is wrong or whether anyone acted maliciously.

Now change only the second claim's interval to `[10:05, 10:10)`. The 10:04 edit is outside that later interval, so the claims need not conflict. Keep two scoped notes instead of forcing them into one Boolean input. Absence in a later window does not erase a recorded earlier event or close an incident. The half-open convention includes the starting instant and excludes the ending instant; differing boundaries are part of the proposition, not cosmetic formatting.

The original program already kept priority from falling when `fresh_edit_verified=True`. It did not reject a simultaneously supplied `no_new_edits_verified=True`, and could therefore print a task-narrowing label built from incompatible premises. The added `BLOCK_CONFLICTING_ACTIVITY_PREMISES` check stops that mixed conclusion under the explicit same-scope contract. It is a fail-closed **classroom inference check**, not an instruction to stop a service, remove evidence or discard a disputed report.

**Independent practice.** Predict the four labels below before executing this supplementary listing. Then write two sentences explaining why the original X31 pair conflicts but the later-window pair need not. Run the complete TRI2 program first, then this listing in the **same fresh Python session**. It uses only copied in-memory variants. For a blocked input it prints the single block label; otherwise it prints only the final priority label, not all five assessment dimensions.

~~~python
# Run after the complete TRI2 program in the same fresh Python session.
# Each variant uses one declared object/account/event predicate and window.
conflict = deepcopy(narrow)
conflict["fresh_edit_verified"] = True
fresh_only = deepcopy(conflict)
fresh_only["no_new_edits_verified"] = False
absence_only = deepcopy(narrow)
quiet_with_fresh = deepcopy(round_b)
quiet_with_fresh.update(variant=True, fresh_edit_verified=True)

for name, sample in (
    ("SAME_SCOPE_CONFLICT", conflict),
    ("FRESH_ONLY", fresh_only),
    ("VERIFIED_ABSENCE_ONLY", absence_only),
    ("QUIET_SUMMARY_WITH_FRESH", quiet_with_fresh),
):
    # A blocked case has one label; otherwise show only the priority label.
    print(name, reassess(sample)[-1])
~~~

Compare your predictions and interval explanation with the [scope-check worked answer](#ir-rapid-ch02-tri2-scope-result) in the final appendix. The original complete program still prints 25 lines; this separate continuation prints four. Keep the original three release challenges below. This practice extends the existing supplementary lab rubric's evidence-boundary criterion, not EX014's two-row table, EX016's short note, EX024's two hypothetical pairs or the 50-exercise denominator.

**Release-guard challenge:** After the baseline program, test three explicitly synthetic Round A variants: set `retention_notice=True` without R15, set `quiet_summary=True` without R14, and set `variant=True`, `approved_addendum=True`, `training_scope_verified_complete=True`, `addendum_names_b19=True`, `no_new_edits_verified=True` and `query_coverage_known=True` without R9/R10. The three results, respectively, must be `BLOCK_UNRELEASED_CLAIM:R15`, `BLOCK_UNRELEASED_CLAIM:R14` and `BLOCK_UNRELEASED_CLAIM:R9_R10`. No case becomes a new canonical R-series record. The 20 baseline conclusions remain unchanged; the two former `CAUSE` tokens are now labeled `TASK_SCOPE` in the code and transcript. The guard checks the classroom release boundary; it does not authenticate a source or verify a real approval.

The original three release-guard controls remain required. The five additional controls in the complete program test a different boundary: the input schema and the distinction between fixed canonical metadata and separately labeled variants. An empty reference list cannot claim that records were supplied. The text `"False"` is not a Boolean false value; accepting it as a variant marker would admit invented impact into what a reader might mistake for the canonical packet. R15 does not supply an anchor, R14 does not supply complete coverage, and R1–R16 do not report a failed custodian contact. Those altered premises must not silently enter the canonical case.

The requests are rejected before a triage conclusion is printed. Empty references cannot substantiate a record-availability claim; `"False"` is not a Boolean; and the fixed packet does not supply an anchor, full query coverage or a failed custodian contact. Keep these tests within the existing supplementary rubric; no additional EX item is created.

<a id="ir-rapid-ch02-tri2-scope-result"></a>

##### Worked answer: same-scope conflict and the limits of a quiet summary

The separate [scope-check continuation](#ir-rapid-ch02-tri2-scope-check), executed after the complete TRI2 listing, prints:

~~~text
SAME_SCOPE_CONFLICT BLOCK_CONFLICTING_ACTIVITY_PREMISES
FRESH_ONLY PRIORITY_KEEP_OR_RAISE_CONTINUING_ACTIVITY
VERIFIED_ABSENCE_ONLY PRIORITY_LOWER_TASK_CONCERN_ONLY_NOT_INCIDENT_CLOSED
QUIET_SUMMARY_WITH_FRESH PRIORITY_KEEP_OR_RAISE_CONTINUING_ACTIVITY
~~~

`SAME_SCOPE_CONFLICT` retains all five narrowing premises from `narrow` and adds a fresh-edit assertion. Because the absence and existence assertions concern one declared scope, the function blocks before printing a task or priority assessment. The block does not identify the erroneous source. Preserve both underlying claims and ask their custodians to reconcile objects, predicates, time basis, interval boundaries and coverage before proposing a revised note.

`FRESH_ONLY` removes the absence assertion rather than pretending to verify it. The fresh-edit assertion remains, so the model keeps or raises the activity concern. `VERIFIED_ABSENCE_ONLY` retains the hypothetical approved narrowing without adding a fresh event. Its output lowers **only the task concern**; it does not declare the incident closed or settle cause, identity, service correctness or preservation. `QUIET_SUMMARY_WITH_FRESH` starts from Round B and adds a synthetic fresh edit. A summary with incomplete coverage is not the same proposition as verified absence, so this pair is not rejected as a logical contradiction; the activity concern remains.

**Worked interval explanation:** A matching 10:04 event belongs to `[10:00, 10:10)`, contradicting a complete no-event claim for that same set. It does not belong to `[10:05, 10:10)`, so the later-window absence claim can coexist with the earlier event, but must remain a separate scoped assessment. Neither conclusion adds an X31 event to R1–R16, authenticates an input or authorizes a production action.

**Self-check:** Award the existing evidence-boundary credit only when the answer distinguishes same-scope contradiction from different-window findings, keeps a quiet summary separate from verified absence, and preserves disputed sources instead of selecting a convenient truth. These four lines are supplementary controls; the 25 baseline lines and three original release challenges are unchanged.

##### Continue interpreting the original TRI2 baseline

The first two lines are the fixed classroom releases. They do not claim a verified victim count, compromise, a completed source hold or a identified actor. Round B changes the training-fit and preservation questions, but the R14 summary does not qualify as proof of quietness. R15 warrants prompt custodian clarification, not an invented exact deletion deadline.
