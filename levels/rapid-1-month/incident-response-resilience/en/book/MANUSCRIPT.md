    if s["no_new_edits_verified"] and not s["query_coverage_known"]:
        return "BLOCK_UNBOUNDED_NEGATIVE_PREMISE"
    if s["verified_fresh_edit"] and s["request_downgrade"]:
        return "BLOCK_GLOBAL_DOWNGRADE_NEW_EDIT_OPEN"

    record = (

For the executed output, scenario interpretation and negative controls, read the [TRI2 worked result](#ir-rapid-ch02-tri2-result) in the final answer appendix. Predict the labels before opening the result.

**Release-guard challenge:** After the baseline program, test three explicitly synthetic Round A variants: set `retention_notice=True` without R15, set `quiet_summary=True` without R14, and set `variant=True`, `approved_addendum=True`, `training_scope_verified_complete=True`, `addendum_names_b19=True`, `no_new_edits_verified=True` and `query_coverage_known=True` without R9/R10. The three results, respectively, must be `BLOCK_UNRELEASED_CLAIM:R15`, `BLOCK_UNRELEASED_CLAIM:R14` and `BLOCK_UNRELEASED_CLAIM:R9_R10`. No case becomes a new canonical R-series record. The 20 baseline conclusions remain unchanged; the two former `CAUSE` tokens are now labeled `TASK_SCOPE` in the code and transcript. The guard checks the classroom release boundary; it does not authenticate a source or verify a real approval.

The original three release-guard controls remain required. The five additional controls in the complete program test a different boundary: the input schema and the distinction between fixed canonical metadata and separately labeled variants. An empty reference list cannot claim that records were supplied. The text `"False"` is not a Boolean false value; accepting it as a variant marker would admit invented impact into what a reader might mistake for the canonical packet. R15 does not supply an anchor, R14 does not supply complete coverage, and R1–R16 do not report a failed custodian contact. Those altered premises must not silently enter the canonical case.

The first result rejects a positive source-availability description with no cited records. The second rejects a string before Python truthiness can turn it into a supposed variant authorization. The remaining controls reject unsupported changes to the canonical retention, query-coverage and contact premises. A blocking result identifies an input inconsistency, not a deleted source, an observed attack or a production action. Preserve the five-point supplementary lab rubric: assess these controls within its existing evidence-boundary and unsupported-claim criterion. No EX identifier is added.

The three release-guard challenge outputs are, in order, `BLOCK_UNRELEASED_CLAIM:R15`, `BLOCK_UNRELEASED_CLAIM:R14` and `BLOCK_UNRELEASED_CLAIM:R9_R10`. Each request asserts a card-derived fact that has not been supplied in its declared Round A input. These controls do not add R-series cards or change the 20 original outputs; they prevent unsupported flags from bypassing the release rule.

#### Interpretation of positive and negative controls

`QUERY_FILTER_UNKNOWN` keeps the query evidence bounded; `quiet_summary=True` opens a quality question, not a proof of absence. `RETENTION_ANCHOR_UNKNOWN` removes the quiet-summary distraction and still prints the preservation concern. `PATRON_REPORT_UNVERIFIED` does not become a verified harm count merely because the program prints a row. `CLAIM_FALSE_ATTRIBUTION` teaches that an analyst-generated claim must remain unsupported when the packet names only a shared account. `NEW_EDIT_NOT_CANONICAL`, `INVENTED_CANONICAL_IMPACT` and `NEW_EDIT_AND_GLOBAL_DOWNGRADE` actively reject inputs that invent a fixed-case event, convert a hypothetical check into canonical impact, or lower global priority despite a fresh verified edit.
