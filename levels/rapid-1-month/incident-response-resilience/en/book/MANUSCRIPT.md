    if s["no_new_edits_verified"] and not s["query_coverage_known"]:
        return "BLOCK_UNBOUNDED_NEGATIVE_PREMISE"
    if s["verified_fresh_edit"] and s["no_new_edits_verified"]:
        return "BLOCK_CONFLICTING_ACTIVITY_PREMISES"
    if s["verified_fresh_edit"] and s["request_downgrade"]:
        return "BLOCK_GLOBAL_DOWNGRADE_NEW_EDIT_OPEN"

    record = (

For the executed output, scenario interpretation and negative controls, read the [TRI2 worked result](#ir-rapid-ch02-tri2-result) in the final answer appendix. Predict the labels before opening the result.

<a id="ir-rapid-ch02-tri2-scope-check"></a>

##### Same-scope claims: a quiet summary is not verified absence

A **contradiction** in this exercise means asserting both that at least one qualifying event exists and that no qualifying event exists in the same bounded set. Two reports that look different are not necessarily contradictory. Before supplying `verified_fresh_edit=True` or `no_new_edits_verified=True`, freeze the object set, account and event predicate, source-coverage universe, time basis and half-open observation interval in a scope note. Within one TRI2 input, both flags refer to that **same scope**. A false flag means its positive assertion is not supplied; it does not prove the opposite. The program receives no scope note, manifest or timestamps and cannot verify them.

**Worked synthetic example, separate from R1–R16.** On one fictional day in UTC, consider edits to invented booking X31 under account Q7 during `[10:00, 10:10)`. A declared verified finding places a matching edit at 10:04. A second declared finding claims complete coverage and no matching edits in that same interval. The 10:04 event is a counterexample to the absence claim. Both positive assertions cannot describe the same set consistently. The new guard returns `BLOCK_CONFLICTING_ACTIVITY_PREMISES`, preserving the disagreement for investigation rather than producing a combined assessment.

Now change only the absence claim's interval to `[10:05, 10:10)`. The 10:04 event falls outside that later interval, so the claims need not conflict. Keep two scoped notes instead of forcing their flags into one TRI2 input. A half-open interval includes its starting instant and excludes its ending instant. An absence finding for a later interval does not erase the earlier event, identify an operator or close an incident.

The original fresh-edit branch already kept `K:NEW_EDIT_REVIEW` when a fresh edit was asserted. That conservative output did not make an accompanying same-scope absence assertion consistent. The added check rejects the inconsistent combination before a multidimensional result is printed. It does not change what supports `I:TRAINING_SCOPE_SUPPORTED`: that separate authorization label still requires the three applicable addendum premises. An earlier guard rejects an absence assertion without declared query coverage as `BLOCK_UNBOUNDED_NEGATIVE_PREMISE`; when both defects occur, that earlier block is reported first. These labels identify a classroom input problem, not a command to stop a service, delete evidence or choose which source is truthful.

`quiet_summary=True` is different again: it says a summary was supplied, not that a completed, adequately scoped absence check was verified. It can coexist with a fresh-edit assertion without becoming this contradiction. The original R14 summary remains incomplete evidence; the new check neither authenticates it nor expands its coverage.

**Independent practice.** Predict all four results below, then write two sentences explaining why the first X31 pair conflicts but the later-window pair need not. Run the complete TRI2 program first, followed by this separate continuation in the **same fresh Python session**. It uses only copied in-memory synthetic inputs and prints every assessment field, not merely the activity label.

~~~python
# Run after the complete TRI2 listing in the same fresh Python session.
# These flags refer to one declared object/predicate/coverage/time scope.
same_scope = {
    **BASE, "variant": True, "verified_fresh_edit": True,
    "no_new_edits_verified": True, "query_coverage_known": True,
}
fresh_only = {**same_scope, "no_new_edits_verified": False}
absence_only = {**same_scope, "verified_fresh_edit": False}
quiet_with_fresh = {**BASE, "variant": True, "verified_fresh_edit": True}

for label, sample in (
    ("SAME_SCOPE_CONFLICT", same_scope),
    ("FRESH_ONLY", fresh_only),
    ("ABSENCE_WITHOUT_ADDENDUM", absence_only),
    ("QUIET_SUMMARY_WITH_FRESH", quiet_with_fresh),
):
    print(label + " " + review(sample))
~~~

Compare your predictions and interval explanation with the [worked scope answer](#ir-rapid-ch02-tri2-scope-result) in the final appendix. The complete program still prints its original 25 lines; this continuation prints four additional lines. Retain the three release challenges below. This practice uses the existing supplementary lab rubric's evidence-boundary criterion; it changes neither EX014's two-row table, EX016's short note, EX024's two hypothetical pairs nor the 50-exercise denominator.

**Release-guard challenge:** After the baseline program, test three explicitly synthetic Round A variants: set `retention_notice=True` without R15, set `quiet_summary=True` without R14, and set `variant=True`, `approved_addendum=True`, `training_scope_verified_complete=True`, `addendum_names_b19=True`, `no_new_edits_verified=True` and `query_coverage_known=True` without R9/R10. The three results, respectively, must be `BLOCK_UNRELEASED_CLAIM:R15`, `BLOCK_UNRELEASED_CLAIM:R14` and `BLOCK_UNRELEASED_CLAIM:R9_R10`. No case becomes a new canonical R-series record. The 20 baseline conclusions remain unchanged; the two former `CAUSE` tokens are now labeled `TASK_SCOPE` in the code and transcript. The guard checks the classroom release boundary; it does not authenticate a source or verify a real approval.

The original three release-guard controls remain required. The five additional controls in the complete program test a different boundary: the input schema and the distinction between fixed canonical metadata and separately labeled variants. An empty reference list cannot claim that records were supplied. The text `"False"` is not a Boolean false value; accepting it as a variant marker would admit invented impact into what a reader might mistake for the canonical packet. R15 does not supply an anchor, R14 does not supply complete coverage, and R1–R16 do not report a failed custodian contact. Those altered premises must not silently enter the canonical case.

The first result rejects a positive source-availability description with no cited records. The second rejects a string before Python truthiness can turn it into a supposed variant authorization. The remaining controls reject unsupported changes to the canonical retention, query-coverage and contact premises. A blocking result identifies an input inconsistency, not a deleted source, an observed attack or a production action. Preserve the five-point supplementary lab rubric: assess these controls within its existing evidence-boundary and unsupported-claim criterion. No EX identifier is added.

The three release-guard challenge outputs are, in order, `BLOCK_UNRELEASED_CLAIM:R15`, `BLOCK_UNRELEASED_CLAIM:R14` and `BLOCK_UNRELEASED_CLAIM:R9_R10`. Each request asserts a card-derived fact that has not been supplied in its declared Round A input. These controls do not add R-series cards or change the 20 original outputs; they prevent unsupported flags from bypassing the release rule.

<a id="ir-rapid-ch02-tri2-scope-result"></a>

##### Worked scope answer: reconcile the proposition before revising the decision

The separate [TRI2 scope continuation](#ir-rapid-ch02-tri2-scope-check), executed after the complete listing, prints exactly:

~~~text
SAME_SCOPE_CONFLICT BLOCK_CONFLICTING_ACTIVITY_PREMISES
FRESH_ONLY R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:NEW_EDIT_REVIEW flags=REVIEW_ON_NEW_VERIFIED_SIGNAL
ABSENCE_WITHOUT_ADDENDUM R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=NONE
QUIET_SUMMARY_WITH_FRESH R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:NEW_EDIT_REVIEW flags=QUIET_NOT_NEGATIVE_PROOF,REVIEW_ON_NEW_VERIFIED_SIGNAL
~~~

`SAME_SCOPE_CONFLICT` supplies both bounded activity assertions and is rejected. The model cannot identify which underlying claim is wrong. Retain both reports; compare the objects, account/event predicate, time basis, interval boundaries and coverage with their custodians before proposing a revised assessment. Do not silently remove the inconvenient claim or treat the block as proof of compromise.

`FRESH_ONLY` removes the absence assertion without claiming that its opposite was independently verified. The fresh-edit assertion remains, so `K:NEW_EDIT_REVIEW` and its review flag remain. `ABSENCE_WITHOUT_ADDENDUM` removes the fresh-edit assertion instead. A bounded absence premise alone does not supply an applicable authorization addendum: `I:CONTESTED_OR_INCOMPLETE` and `K:OPEN_HYPOTHESES` remain. These two cases deliberately keep authorization, continuing activity, harm and preservation as different questions.

`QUIET_SUMMARY_WITH_FRESH` supplies a hypothetical fresh edit while retaining the baseline's incomplete quiet-summary coverage. It therefore prints both `QUIET_NOT_NEGATIVE_PROOF` and `REVIEW_ON_NEW_VERIFIED_SIGNAL`. A supplied summary is not the universal no-event proposition that would contradict a matching event. All non-blocked examples still say that records are not authenticated, the actor is unproven, harm is report-only and the retention anchor requires contact. None reports a completed hold, establishes source truth or authorizes a production action.

**Worked two-sentence interval answer:** The matching 10:04 edit belongs to `[10:00, 10:10)`, so it contradicts a complete no-matching-edit claim for that same set. It does not belong to `[10:05, 10:10)`, so a later-window absence claim can coexist with the earlier event but must remain a separate scoped assessment.

For the existing evidence-boundary credit, require the distinction between same-scope contradiction and different-window findings, between a quiet summary and verified absence, and between an unresolved disagreement and a discarded source. No X31 event enters R1–R16. These four supplementary results do not replace the 25 original output lines or the three release challenges; continue interpreting those baseline cases below.

#### Interpretation of positive and negative controls

`QUERY_FILTER_UNKNOWN` keeps the query evidence bounded; `quiet_summary=True` opens a quality question, not a proof of absence. `RETENTION_ANCHOR_UNKNOWN` removes the quiet-summary distraction and still prints the preservation concern. `PATRON_REPORT_UNVERIFIED` does not become a verified harm count merely because the program prints a row. `CLAIM_FALSE_ATTRIBUTION` teaches that an analyst-generated claim must remain unsupported when the packet names only a shared account. `NEW_EDIT_NOT_CANONICAL`, `INVENTED_CANONICAL_IMPACT` and `NEW_EDIT_AND_GLOBAL_DOWNGRADE` actively reject inputs that invent a fixed-case event, convert a hypothetical check into canonical impact, or lower global priority despite a fresh verified edit.
