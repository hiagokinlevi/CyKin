A stated review date is not always the same as automatic technical expiry. A platform may continue enforcement after an administrative review is overdue, or may terminate enforcement at a lease boundary. The semantics depend on the source and control. The course must not invent them.

In HOLD2, the independent fixture provides a technical `term_end`. If the lab's assessment cutoff is at or after that exclusive term end, the program returns **TERM_EXPIRED_EFFECT_UNKNOWN**. It does not assert that a row was deleted or that deletion resumed immediately. Actual post-term source behavior requires its own authorized observation.

A valid hold receipt also should say what happens if review cannot be completed. A safe plan may require escalation before expiration, a separately approved renewal, or continuing safeguards as defined by the actual policy. The analyst cannot assume that a prior approval renews itself.

##### 2.8a.9 Release and expiration must not erase the earlier lifecycle

Before reading the final appendix, predict all 33 output lines: sixteen baseline lines, three chronology controls and fourteen acceptance controls. Explain the first blocking condition for each variant. Compare the actual run with the [HOLD2 worked result](#ir-rapid-ch02-hold2-result).

**Required learner artifacts:** Reproduce the 33 output lines; create a scenario table with the first blocking condition and a safe next request; identify why `COPY_ONLY` does not establish source hold and why `OLDEST_MISSING` does not prove deletion timing; compare requested, reported and authorized scope; identify the request/control/sentinel bindings and required lifecycle steps; propose a reviewer check for release and expiry that does not erase history or delete data. A future lifecycle entry cannot support an earlier `as_of` conclusion; even a consistent fixture does not authenticate a real hold.

**Five-point assessment for this unnumbered lab:** One point each for exact output; correct source/object/interval coverage and authorization reasoning; separation of copy from source control; correct treatment of unavailable custodian or a specifically identified oldest row; and complete request-bound lifecycle, expiry/release history and explicit effect limits. Assess the added controls within these same five criteria. The lab adds **no new EX identifier**.

<a id="ir-rapid-l08-review-checkpoint"></a>

##### HOLD2-R — A review deadline is not a new source observation

**Learning goal:** Write a hold-review note that separates the age of the last reported observation, an owner-review appointment and the end of a stated technical term. Then explain why a first-refusal label is not a complete defect inventory. Complete the 33-line HOLD2 program above before this checkpoint; its inputs, outputs and five-point assessment remain unchanged.

**Independent review metadata:** For this checkpoint only, add an invented owner-review appointment at **10:15 UTC on 2040-03-15** for HOLD2-CTRL-01. It is a scheduled decision, not a completed review, a new authorization, a source query or a renewal. Keep it outside the fixed HOLD2 packet schema. All existing source, object and receipt values remain the artificial HOLD2 values, not Harbor Library evidence.

###### Read three clocks without turning one into another

The requested event interval selects *which records* matter. Activation and the technical term describe a reported control. The last effect-check time dates the supplied observation. An owner-review appointment says when a decision is due. A later `as_of` selects the information cutoff at which the packet is assessed; it cannot manufacture a new source observation.

```text
Event selection: [09:00, 09:30)       Which source events are requested?
Reported control:       09:40 -------------------------- 11:30 excluded
Reported effect check:          10:00
Owner review due:                       10:15
Later assessment:                              11:29
                                      same 10:00 observation; age 89 min
```

**Text alternative:** The event interval ends at 09:30; reported activation is at 09:40; the only reported effect check is at 10:00. The additional owner review is due at 10:15. At an 11:29 assessment, the observation is 89 minutes old even though the stated technical term has not reached its exclusive 11:30 end. This is a logical ordering, not a scale drawing or proof of continuous protection.

Consider the claim: "The 11:29 run returned a positive label, so the source was checked again at 11:29." The calculation is reproducible, but the claim changes its meaning. HOLD2 checks the consistency of the same supplied packet. Its last reported effect observation remains 10:00. The correct age is `11:29 - 10:00 = 89 minutes`. That arithmetic measures neither uninterrupted hold effectiveness nor a probability that protection has failed.

At 10:15, a different question becomes due: has the owner made the scheduled review decision? No review-completion receipt is supplied. The appointment does not expire the technical mechanism, renew its authority, authorize a release or refresh the source observation. At **11:30 exactly**, however, the fixed HOLD2 term ends under the exclusive-end convention and the original function returns `TERM_EXPIRED_EFFECT_UNKNOWN`. The historical 10:00 check remains recorded. Neither this label nor an overdue appointment proves that data were deleted.

There is no universal maximum acceptable observation age in this fixture. A real decision would need an owner-defined review procedure, source capabilities, relevant change signals and authorized new observations. Do not invent a fifteen-minute freshness policy merely because this particular appointment is fifteen minutes after the check. The checkpoint supplies an appointment, not a measured risk threshold.

**Worked review wording:** "At the artificial 10:15 assessment, the packet still contains only the reported 10:00 effect check for HOLD2-CTRL-01 on booking-audit-sim; that observation is fifteen minutes old. The additional owner review is due, with no completed review or new source check supplied, while the recorded technical term ends at 11:30 exclusive. Seek the owner's decision and an appropriately authorized, source-bound current-state check; do not report renewal, current protection or deletion as observed."

This note identifies what the next reviewer must obtain without silently replacing the earlier record. In the original `FUTURE_EFFECT_CHECK` control, setting `as_of` to 09:45 while retaining the 10:00 history correctly fails. Neither moving the cutoff forward nor deleting an inconvenient history row supplies missing evidence.

###### A first refusal is not a complete diagnosis

The function uses ordered `return` statements. Python's [function documentation](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions) explains that returning a value exits that function call. Once HOLD2 reports `WRONG_SOURCE`, later coverage, authorization and observation checks have not all been evaluated. The label identifies the first blocking condition under this program, not the only problem in the packet or a complete operational state.

For example, a deliberately defective receipt can name the wrong source, include unapproved BX-99, and provide neither a verified-effect assertion nor an available-sentinel assertion. Changing only the source in a **separately labeled hypothetical packet** exposes the next block; it does not establish that a custodian corrected a real control. Even after the object scope is aligned, missing effect evidence and an unavailable sentinel remain different questions. A negative result should be accompanied by the known outstanding issues and the receipts needed to resolve them, not by an invented sequence of completed repairs.

The original negative variants sometimes retain other baseline fields so that one early guard can be studied. Their reassuring or conflicting later fields cannot override the refusal. Do not use the label `PROPOSED_ONLY`, for example, as proof that an inherited history was exhaustively checked and contains no application entry. HOLD2 is a first-refusal consistency checker for this teaching contract, not a production lifecycle reconstruction engine.

###### Run the independent predictions in the HOLD2 session

Run the complete program above in a fresh session, then run this continuation in that same session. It prints **eight additional lines** and does not redefine `status`, change `BASE`, write files, contact a source or perform a hold/release. Its first four packets change only the assessment cutoff. Its four `MULTI` packets are independent hypothetical inputs, not a record of an operator fixing a source. The additional review appointment is deliberately not inserted into the strict original schema.

~~~python
# Run after the complete HOLD2 listing, in the same fresh session.
# The review appointment is additional invented metadata, not a receipt.
owner_review_due = utc("10:15")
frozen_base = deepcopy(BASE)
assert status(BASE) == "BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE"
effect_times = [utc(clock) for kind, clock in BASE["history"]
                if kind == "EFFECT_CHECKED"]
assert len(effect_times) == 1
last_check = effect_times[0]

for clock in ("10:00", "10:15", "11:29", "11:30"):
    sample = variant({"as_of": utc(clock)})
    age_minutes = (sample["as_of"] - last_check) // timedelta(minutes=1)
    due = "DUE" if sample["as_of"] >= owner_review_due else "NOT_DUE"
    print(f"REVIEW {clock}: last_check={last_check:%H:%M} "
          f"age_min={age_minutes} owner_review={due} "
          f"result={status(sample)}")

# Four separate hypothetical packets, not successive operational repairs.
for label, wrong_source, extra_object, effect in (
    ("MULTI_A", True, True, False),
    ("MULTI_B", False, True, False),
    ("MULTI_C", False, False, False),
    ("MULTI_D", False, False, True),
):
    sample = variant({"effect_checked": effect,
                      "oldest_retrievable": False})
    if wrong_source:
        sample["receipt"]["source"] = "identity-detail-sim"
    if extra_object:
        sample["receipt"]["objects"].add("BX-99")
    print(f"{label}: {status(sample)}")

assert BASE == frozen_base  # The original packet and its history are unchanged.
~~~

The age calculation uses floor division by a one-minute `timedelta`; the quotient is exact for these minute-aligned inputs. Python documents [duration arithmetic](https://docs.python.org/3.13/library/datetime.html#timedelta-objects). No system clock is read. `DUE` means the invented appointment has been reached, with no completion supplied; it is not an observation of the control. Adding `owner_review_due` to `BASE` would instead violate the original fixed schema.

**Independent practice:** Before running, prepare a four-row review table for 10:00, 10:15, 11:29 and 11:30, with the last reported check, its age, owner-review status, term status and one unsupported claim. Then prepare four `MULTI` rows naming the first refusal, at least one remaining declared issue when present, and the specific authorized clarification needed. Explain why a corrected receipt must be preserved as a new version and reviewed again in full, rather than silently editing the prior input until it passes.

Finally, write two sentences correcting "the 11:29 positive result proves current protection" and "fixing MULTI_A's source proves every other field passed." For EX018, keep the existing three-row P-A request and two-row P-A/P-B comparison; its custodian-question field can ask separately for the last observed effect, the next owner review and the technical term's actual semantics. In canonical Round B, those hold details remain **not supplied**, both requests remain **proposed**, R15's retention anchor remains unknown and P-B has no supplied retention duration. Do not borrow the HOLD2-R appointment or term.

Assess these explanations within the existing HOLD2 criteria for output, scoped authorization, copy/source separation, missing observations and lifecycle limits. A full-credit answer keeps all three clocks distinct and identifies untested or unresolved conditions beyond the first diagnostic. This checkpoint adds no daily lesson or numbered exercise. [Worked checkpoint answer](#ir-rapid-l08-review-checkpoint-result).

#### 2.8c Practical two-role activity — custodian packet and independent review

**Purpose:** Demonstrate that a second person can distinguish a requested, approved, applied and verified source hold **without relying on the packet author's explanation**.

**Roles:** **Custodian / Packet Author** and **Independent Reviewer**. The incident-lead approval is represented only by a fictional classroom request card. There is no real source custodian, logging system or deletion mechanism involved.

**Limits of the positive control:** VALID_BOUND now depends on the explicitly declared authorization, nonempty selection, request/control bindings and complete modeled history as well as the original checks. Its positive label still means consistency of artificial premises, not authenticated approval or actual protection. The program returns the first blocking condition; several defects can coexist. Fixing one reported problem requires rerunning the complete review and does not imply all other fields were tested. `copy_retained` is deliberately irrelevant to a source-hold pass: an E1-style copy cannot repair a wrong control, missing effect check or unavailable sentinel.

**Model application to the existing numbered exercises:** EX018 requests both a selection that covers the decision question and authorization that covers the intended operation; at 09:20, IDs and receipts remain to be obtained. EX019 records only the local E1 creation and checks actually performed, with a separate pending source-control reference. EX022 asks the custodian to clarify those missing facts without saying a hold was applied. EX024 keeps receipt inconsistency separate from substantiated imminent source loss: each needs a named verifier and incident-lead review, not an automatic production action. Preserve the original artifact sizes and common 0–2 rubric; the additional program controls belong to the existing five-point HOLD2 assessment and create no new exercise ID.

<a id="ir-rapid-l08-review-checkpoint-result"></a>

### HOLD2-R — Review age and first-refusal practice: worked result

Read the [checkpoint](#ir-rapid-l08-review-checkpoint) and make the predictions first. Running its continuation after the unchanged 33-line HOLD2 program produced these eight additional lines with Python 3.13.5:

~~~text
REVIEW 10:00: last_check=10:00 age_min=0 owner_review=NOT_DUE result=BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE
REVIEW 10:15: last_check=10:00 age_min=15 owner_review=DUE result=BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE
REVIEW 11:29: last_check=10:00 age_min=89 owner_review=DUE result=BOUNDED_SOURCE_HOLD_CONFIRMED_IN_FIXTURE
REVIEW 11:30: last_check=10:00 age_min=90 owner_review=DUE result=TERM_EXPIRED_EFFECT_UNKNOWN
MULTI_A: WRONG_SOURCE
MULTI_B: AUTHORIZED_SCOPE_EXCEEDED
MULTI_C: EFFECT_NOT_VERIFIED
MULTI_D: OLDEST_ROW_UNAVAILABLE
~~~

| Assessment cutoff | Last reported check and age | Additional owner review | Stated technical term | Unsupported claim |
|---|---|---|---|---|
| 10:00 | 10:00; 0 minutes | Not yet due | Before the exclusive 11:30 end | Even a zero-age artificial assertion does not authenticate a real source or prove all rows were protected |
| 10:15 | 10:00; 15 minutes | Due; completion not supplied | Before the stated end | Reaching the appointment neither completes the review nor expires or renews the control |
| 11:29 | 10:00; 89 minutes | Due; completion not supplied | Before the stated end | Reassessing the same packet is not a new 11:29 source check |
| 11:30 | 10:00; 90 minutes | Due; completion not supplied | At its excluded end | Expiration of the stated term is not an observation of deletion or post-term control behavior |

For the decisive 11:29 row, 89 minutes is the difference between the supplied cutoff and the supplied observation time. It does not estimate the duration of any protection failure. The positive function result tests the artificial packet's declared consistency; the earlier observation does not establish continued effect. A safe next step is to seek the overdue owner decision and an authorized source/control check, retaining the earlier observation and explicitly recording whatever is newly obtained. No renewal, release, source check or deletion was performed by the program.

| Independent packet | First returned block | Other declared issue still requiring attention | Next authorized clarification, not an executed repair |
|---|---|---|---|
| MULTI_A | `WRONG_SOURCE` | Receipt also includes BX-99 beyond the supplied object authorization; effect and sentinel assertions are unfavorable | Ask for the request-bound receipt for the intended source, retaining the wrong-source version; then re-evaluate the entire packet |
| MULTI_B | `AUTHORIZED_SCOPE_EXCEEDED` | Effect is not verified and the oldest-row assertion is unfavorable | Ask the custodian and approving role to explain the unapproved reported selection and provide appropriate scoped evidence; do not retroactively invent permission |
| MULTI_C | `EFFECT_NOT_VERIFIED` | The selected oldest row is also reported unavailable | Request the authorized non-destructive effect observation and investigate the sentinel's expected existence, source selection and retrieval path separately |
| MULTI_D | `OLDEST_ROW_UNAVAILABLE` | No additional failing declared gate is supplied, but authenticity, complete source coverage and the reason for absence remain unproved | Seek source-specific evidence about the expected sentinel and retrieval limits; do not conclude malicious deletion or a known deletion time |

The packets are not a historical sequence. MULTI_D's `effect_checked=True` is supplied as a distinct artificial premise, not obtained by running MULTI_C. An operator cannot create verification evidence by changing that flag. Similarly, a first diagnostic is not an exhaustive defect list: earlier guards prevent later branches from deciding this call. The four rows therefore require both a diagnostic and an evidence request, not just different labels.

**Two-sentence correction:** "The 11:29 run reassesses a packet whose only reported effect check remains at 10:00, so current source protection is not newly observed. Aligning the source in a separate MULTI_A variant merely allows later checks to run; it does not prove that scope, authority, effect or sentinel coverage passed."

For EX018, put separate last-check, owner-review and technical-term questions into the existing proposed request, not invented answers. Keep the original three-row P-A and two-row comparison artifacts. Neither the 10:15 appointment nor the 11:30 term belongs to Harbor Library; both P-A and P-B remain proposed at 09:20, and their unsupplied source-hold receipts remain pending.

**Verification boundary:** Local checks reproduced the original 33 lines and these eight lines. Finite tests also examined all 1,440 same-day minute cutoffs with both copy-retention flags, 512 request/receipt/authority object-set combinations, 24 receipt-interval boundary cases, and additional type, lifecycle and binding controls. Inputs and the baseline were unchanged after the tested calls. These checks test the declared model and reported calculations, not a real hold, source authenticity, deletion prevention, actual independent learner performance or the whole-book editorial gate.

[Return to the checkpoint](#ir-rapid-l08-review-checkpoint) · [EX018](#ex018--worked-result) · [Lesson 09](#lesson-09)

### Module 2 synthetic-extract lab — worked result

The script writes **235 bytes** to each file. The SHA-256 digest for `E1.txt` is `dc973f580305633eb0a75317c5bdbd9886a8fc015e14a0b17bae09be5e3a6e37`; the digest for `E1-modified.txt` is `15287410550f021dcb81e10fc1833297ffa840ee8ffa8e75867de36df64ffa4d`. The strings have equal byte length because the single ASCII digit `3` was replaced with `4`; their different digests show the modified copy is not byte-identical to the saved original. Learners should calculate the values locally rather than trust a copied answer.
