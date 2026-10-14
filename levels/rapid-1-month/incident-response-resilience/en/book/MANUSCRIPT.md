A stated review date is not always the same as automatic technical expiry. A platform may continue enforcement after an administrative review is overdue, or may terminate enforcement at a lease boundary. The semantics depend on the source and control. The course must not invent them.

In HOLD2, the independent fixture provides a technical `term_end`. If the lab's check time is later than that term, the program returns **TERM_EXPIRED_EFFECT_UNKNOWN**. It does not assert that a row was deleted or that deletion resumed immediately. Actual post-term source behavior requires its own authorized observation.

A valid hold receipt also should say what happens if review cannot be completed. A safe plan may require escalation before expiration, a separately approved renewal, or continuing safeguards as defined by the actual policy. The analyst cannot assume that a prior approval renews itself.

##### 2.8a.9 Release and expiration must not erase the earlier lifecycle

Before reading the final appendix, predict all 33 output lines: sixteen baseline lines, three chronology controls and fourteen acceptance controls. Explain the first blocking condition for each variant. Compare the actual run with the [HOLD2 worked result](#ir-rapid-ch02-hold2-result).

**Required learner artifacts:** Reproduce the 33 output lines; create a scenario table with the first blocking condition and a safe next request; identify why `COPY_ONLY` does not establish source hold and why `OLDEST_MISSING` does not prove deletion timing; compare requested, reported and authorized scope; identify the request/control/sentinel bindings and required lifecycle steps; propose a reviewer check for release and expiry that does not erase history or delete data. A future lifecycle entry cannot support an earlier `as_of` conclusion; even a consistent fixture does not authenticate a real hold.

**Five-point assessment for this unnumbered lab:** One point each for exact output; correct source/object/interval coverage and authorization reasoning; separation of copy from source control; correct treatment of unavailable custodian or a specifically identified oldest row; and complete request-bound lifecycle, expiry/release history and explicit effect limits. Assess the added controls within these same five criteria. The lab adds **no new EX identifier**.

#### 2.8c Practical two-role activity — custodian packet and independent review

**Purpose:** Demonstrate that a second person can distinguish a requested, approved, applied and verified source hold **without relying on the packet author's explanation**.

**Roles:** **Custodian / Packet Author** and **Independent Reviewer**. The incident-lead approval is represented only by a fictional classroom request card. There is no real source custodian, logging system or deletion mechanism involved.

**Limits of the positive control:** VALID_BOUND now depends on the explicitly declared authorization, nonempty selection, request/control bindings and complete modeled history as well as the original checks. Its positive label still means consistency of artificial premises, not authenticated approval or actual protection. The program returns the first blocking condition; several defects can coexist. Fixing one reported problem requires rerunning the complete review and does not imply all other fields were tested. `copy_retained` is deliberately irrelevant to a source-hold pass: an E1-style copy cannot repair a wrong control, missing effect check or unavailable sentinel.

**Model application to the existing numbered exercises:** EX018 requests both a selection that covers the decision question and authorization that covers the intended operation; at 09:20, IDs and receipts remain to be obtained. EX019 records only the local E1 creation and checks actually performed, with a separate pending source-control reference. EX022 asks the custodian to clarify those missing facts without saying a hold was applied. EX024 keeps receipt inconsistency separate from substantiated imminent source loss: each needs a named verifier and incident-lead review, not an automatic production action. Preserve the original artifact sizes and common 0–2 rubric; the additional program controls belong to the existing five-point HOLD2 assessment and create no new exercise ID.

### Module 2 synthetic-extract lab — worked result

The script writes **235 bytes** to each file. The SHA-256 digest for `E1.txt` is `dc973f580305633eb0a75317c5bdbd9886a8fc015e14a0b17bae09be5e3a6e37`; the digest for `E1-modified.txt` is `15287410550f021dcb81e10fc1833297ffa840ee8ffa8e75867de36df64ffa4d`. The strings have equal byte length because the single ASCII digit `3` was replaced with `4`; their different digests show the modified copy is not byte-identical to the saved original. Learners should calculate the values locally rather than trust a copied answer.
