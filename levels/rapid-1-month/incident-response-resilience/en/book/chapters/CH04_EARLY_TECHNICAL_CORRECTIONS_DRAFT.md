# Chapter 4 §§4.1–4.8 — Independent Early Technical Corrections (DRAFT)

**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). **Edition:** English, rapid Incident Response. **Status:** proposed authorial corrections for the one [principal manuscript](../MANUSCRIPT.md#ch-04), not integrated teaching, approved exercise results or a completed book. The [publication standard](../../../../../../BOOK_STANDARD.md) still applies.

**Frozen review baseline:** public main commit 06892e0e2823dd2395e062e4c9cc5606a19488cd; MANUSCRIPT.md SHA-256 d79bdac8430a6bf994f5ae5cd53acc04d7badac35f800b48a5e1d49c78c4939d, independently calculated. The recorded 337 A4 pages and 50 numbered exercise/answer pairs are draft-length and coverage measurements, not review approval.

## Audit method and reproducible frozen-release trace

**Method:** Read the original Round A–D release table, model Branch S and the separate P1/C1 and V1 releases in that exact order, and freeze a written evidence/decision state immediately before opening each later card. Then attempt (i) to use future R17 in Round B, (ii) to use P1 in Round C and (iii) to treat a preservation request or simulated approval as a collected copy. Each violates the source-state contract; none adds a canonical incident event.

| Frozen stage | Learner's released evidence | Defensible claim | Explicitly unavailable or not established |
|---|---|---|---|
| **A / first decision 09:05 UTC** | R1–R8 only | R1 records a sign-in; R3/R4 report booking changes; R5 is a patron report; R6 allows training as a live hypothesis. | R9, later incident edits, attribution, collected preservation copy, approval or production change. R9's event at 09:03 does **not** make R9 available at 09:05. |
| **B / 09:20 UTC** | R1–R16 only | R9 records B19 activity; R10's supplied training tasks omit B19; R15 reports a 24-hour deletion policy without its start anchor. A source-specific, time-limited request and policy-clock question are defensible. | R17/R18/B20; an exact deletion instant; custodial acknowledgement, successful source hold, completed export or checked digest. Classroom role-play approval, if recorded, is a separate decision and still does not create a copy. |
| **C / 09:37 UTC** | R1–R24 only | R17/R18 change triage; R19 describes a session-revocation capability; R21 states business tolerance of a conditional pause. The team may **propose** a scoped option and request incident-lead plus relevant owner approval. | R1–R24 contain no incident-specific approval or execution receipt for revocation or pause, no Branch S/P action, no P1/C1 or V1 results. An actual classroom role-play approval needs its own separately frozen simulation decision. |
| **D1 / Branch S card, reported 09:45 UTC** | R1–R24 + Branch S | The identity administrator **reports** revoking the specified session; a query reports no subsequent matching edit in its bounded but incompletely specified range; staff must reauthenticate. | Unauthenticated actor, all-session effect, comprehensive query coverage, copied evidence, correct state of all bookings, P1/C1, V1 and completed service acceptance. |
| **D2 / later P1/C1 release** | Prior cards + P1/C1 | Under the new exercise-only approved target, B17 and B18 match; B19 and B20 mismatch. | A live correction, an executed restore, complete database coverage and the still-withheld V1 audit result. |
| **D3 / later V1 release** | Prior cards + V1 | An authorized synthetic operation succeeds and a tested unauthorized one is denied; V1's actor attribution **fails** despite its UTC timestamp. | Actual production access safety, a corrected audit, identity of the previous human actor, full business recovery and known RTO/RPO. |

**Adversarial expected results:** (a) “R17 proves the Round B analyst knew B19 was outside every approved task” is **REJECT_FUTURE_R17**; (b) “The Round C decision knew the P1 target and B19/B20 mismatches” is **REJECT_FUTURE_P1**; (c) “Round B approved preservation, therefore the original source was held and a copy was collected” is **REJECT_NO_SOURCE_OR_COPY_RECEIPT**. These labels are analytical review annotations, not outputs of an executable production validator. Retain original frozen snapshots rather than editing them after a later release.

## Correction A — §4.3 Round B: remove the unsupported deadline and the copy-status ambiguity

**Exact insertion/replacement:** Within the single §4.3 **Round B** worked-example sentence sequence, replace the sentence pair that begins “R9–R16 add an unexplained B19 edit and a retention deadline” and ends “sets a 09:35 review.” Do not modify the Round A, C or D examples.

**Finding:** R15 gives a 24-hour detailed-audit deletion duration but not a verified clock anchor or exact deadline. The phrase “retention deadline” upgrades an incomplete policy into an exact loss event. The following wording “approves preserving the narrow audit copy” is a **hypothetical role-play decision**, whereas R9–R16 provide no approval, custodian receipt, source-control effect or collected copy. The existing §4.8 report correctly says the request has no collector receipt.

**Consequence:** Students can wrongly use time arithmetic or an approved *request* as evidence that the source actually was held or the data already copied.

**Replacement teaching text:**

> **Round B.** The new R9–R16 cards add an unresolved B19 edit and a time-sensitive source-preservation risk. R15 supplies a 24-hour deletion duration but not the policy-clock anchor, so no precise deletion deadline can be stated. In the worked classroom path, the incident lead may **role-play approving a narrowly scoped preservation request**, provided that simulated decision is separately documented; the analyst asks the application custodian to clarify source and retention coverage and sets a 09:35 review. Neither the supplied R-series cards nor the simulated request approval establishes a received request, applied source hold, collected copy, collection timestamp or integrity verification. Each would require its own independently identified receipt.

**Test:** Compare this replacement against R15 and the §4.8 after-action table. Expected classification at 09:20: **preservation requested (or approval separately simulated); collection NOT SUPPLIED; source hold NOT SUPPLIED; exact deletion deadline UNKNOWN**. R17–R24 remain withheld.

## Correction B — §§4.2 and 4.4: freeze role-play approvals as separate exercise artifacts

**Exact insertion:** Immediately after the §4.4 paragraph beginning “At each round, freeze a one-paragraph state snapshot” and before the Round D claim ledger. This supplements rather than replaces the original four-round table.

**Finding:** §4.2 asks the learner to obtain a fictional Round C approval, while R1–R24 do not supply one. §4.3's worked path narrates such an approval, and §4.8 correctly says a participant must distinguish request quality from collection. Without an explicit record-status convention, a polished narrative can hide whether the facilitator actually observed the approval or merely assumed it.

**Supplemental release-and-decision contract:**

1. **Supplied records** are the immutable R1–R24 and individually released Branch S/P, P1/C1 and V1 cards. Their event timestamps are not their release timestamps.
2. A **role-play action receipt**, such as a separately labeled C-approval-v1, is a *learner/facilitator-created artifact*, not an R-series record. Include the exact owner role, approved target, scope, approval time, permitted duration, decision reference, recorded observer and the already-frozen C-action-v1 proposal. Do not create an affirmative receipt merely because a model answer says “approved.”
3. If no role-play approval was observed and recorded, freeze **approved = PENDING** for the canonical 09:37 source-only analysis. A class may still discuss the conditional outcome: “If the appropriate roles approve this scoped action, the designated operator may later act.” An approval never authenticates execution.
4. A separately released Branch S card reports an action at 09:45 under its fictional approval; it does not retroactively create a missing Round C approval receipt in an earlier learner submission. Treat the branch's negative query as bounded, not exhaustive.
5. A collection receipt is another object entirely: named producing source, exact selection, collector, actual collection time, bytes/copy ID, restricted destination, integrity check and limits. A dispatch, role read-back, request approval or source-hold proposal cannot substitute for it.

**Adversarial checks:** With **C-action-v1 present but C-approval-v1 absent**, expected Round C state is **PROPOSED / APPROVAL PENDING / EXECUTION NOT REPORTED / EFFECT UNVERIFIED**. With a *separately observed and frozen* C-approval-v1, expected state is **SIMULATED APPROVED / EXECUTION NOT REPORTED / EFFECT UNVERIFIED**. With a request approved but no copy receipt at Round B, expected copy state remains **NOT COLLECTED IN SUPPLIED EVIDENCE**. None authorizes real-world changes.

## Correction C — §4.5: explicit L2 calculation, critical gates and EX048 release contrast

**Exact insertion:** Immediately after the L2 paragraph concluding that the reconciled score is 8/12, before “How to revise L2.” Keep all six original learner excerpts and the reviewer A/B decisions unchanged.

**Independent recalculation from the six frozen learner artifacts:**

| Artifact and authorized scoring checkpoint | Reviewer A | Reviewer B | Reconciled | Determining evidence |
|---|---:|---:|---:|---|
| Timeline, assembled after release without rewriting earlier rounds | 2 | 2 | **2** | R9 marked received in Round B; R18/R21 in Round C; no human attribution |
| Round B hypotheses, frozen before R17 | 2 | 2 | **2** | R10/R9/R13 support competing explanations and a bounded next check |
| C-action-v1, frozen at 09:37 | 2 | 1 | **1** | “Identity owner consulted” supplies no incident-lead approval; service cost, fallback and interval are missing |
| D-recovery-v1, after P1/C1 and V1 | 1 | 0 | **0** | C1 contradicts “all bookings correct”; V1's actor field is blank |
| L2 final status, **after all D cards** | 2 | 2 | **2** | Status identifies Branch S action and *later* B19/B20/audit gaps with a 10:05 review |
| Improvement | 1 | 1 | **1** | No accountable test owner or repeatable closure criterion |

**Expected score:** 2 + 2 + 1 + 0 + 2 + 1 = **8/12**, lower than the **9/12** classroom pass threshold. Do not average reviewer scores into halves. A zero for a critical approval or evidence-scope artifact independently fails the published gate; this packet also fails on the 8/12 total. The D-recovery zero is not turned into a pass by a well-written final status. Record why each score is attached to the **actual frozen artifact**.

**Release contrast — two different status assignments:** The L2 status above is a **post-all-cards L2 teaching artifact** and may name B19/B20 and the blank audit actor. EX048, by contrast, explicitly requests **exactly two sentences at 09:45, after Branch S or P but before P1/C1 and V1**. Its existing worked answer correctly withholds later findings and requires an owner/checkpoint. If a student adds the P1/C1 or V1 result to EX048, reject the EX048 checkpoint even if a similar sentence earns L2's final-status score **after all cards**. A strong score at a late checkpoint never upgrades an earlier unavailable fact.

**Adversarial checks and expected verdicts:** (i) Add R17 to the frozen Round B hypotheses: **release-boundary violation; do not award the evidence-linked score on that contaminated artifact**. (ii) Add P1/C1 to frozen C-action-v1: **release-boundary violation; approval does not become established**. (iii) Award L2's final status of 2 to EX048 with V1's missing actor: **reject EX048 version until rewritten to branch-only evidence**. (iv) Replace the zero D-recovery note with a later corrected D-recovery-v2: **re-score the new version, retain the original 0 in the first attempt**.

## Correction D — EX039: show the requested DEL4 recipient/read-back fields in the five-row worked role card

**Exact insertion:** Under §EX039 — Worked result, extend the **existing five-row role card** with a column titled “Proposed update receiver and acknowledgement check.” Do not add a sixth role, replace the existing authority column, or claim actual delivery from Round A cards.

**Finding:** EX039's DEL4 extension asks for the receiver/acknowledgement role for critical updates and at least one concrete message ID/version plus expected read-back question. The original answer's five-row table omits this column; its later narrative mentions an example read-back without a definite versioned example. These are missing assessable output fields, not evidence that communication actually occurred.

| Existing role | Proposed update receiver and acknowledgement check |
|---|---|
| Incident lead | Receives the analyst's scoped intake decision request; must acknowledge **which decision, version and boundary** are being requested, not grant approval simply by receiving it |
| Analyst | Receives the incident lead's bounded instruction; reads back the exact R1–R8 scope and the next 09:05 decision question |
| Service owner | Receives a separate impact/availability question; acknowledgement must identify which essential booking function and scope are being assessed |
| Recovery lead | Receives a **planned** isolated-copy readiness question; acknowledgement states that no restore result is supplied by R7 |
| Communications contact | Receives a proposed evidence-bounded status; confirms intended audience and that attribution or recovery is not confirmed |

**One complete illustrative message field (not a delivered record):** ID **HL-IR-001-A-DECISION**, version **v1**, intended sender **Analyst**, intended recipient **Incident Lead**, stage **Round A / proposed**, route **approved internal route to be confirmed**, dispatch **NOT SUPPLIED**, receipt **NOT SUPPLIED**, read-back **NOT SUPPLIED**. Proposed read-back question: “Which R1–R8 observations support the 09:05 decision, what remains unknown, and what authority is requested?” A different role-specific draft may also pass; no invented working channel or delivery receipt is allowed.

**Test and expected outcome:** A submission listing all five roles, a recipient/acknowledgement rule for each, the v1 example and one read-back question satisfies the added **format** requirement, provided actual acknowledgement stays **not supplied**. A role list without any receiving role/version or a statement that message receipt equals change approval **does not** satisfy the DEL4 extension.

## Correction E — EX043: preserve request, approval, receipt and collected-copy states in the model answer

**Exact insertion:** Within §EX043 — Worked result, replace only the sentence that begins “The named collector records the actual query” with the following bounded conditional statement; append the short state matrix after the original DEL4 worked refinement.

**Finding:** EX043 correctly asks for the actual collection status **requested**, and its last sentences disclaim a completed export. However, “The named collector records the actual query, source, collection time, approved copy location and access list” uses present-tense activity that can be misread as a completed collection step absent from R9–R16.

**Replacement sentence:**

> If a later, separately authorized and completed collection occurs, the named collector **must then** record the actual source and query, collection time, copy identifier, restricted destination/access, transformations, integrity check and limits; none of those execution receipts is supplied at the Round B checkpoint. Until then, all collection-result fields remain **not supplied** and the task is a bounded request to the appropriate custodian.

| Evidence state at Round B | Defensible result |
|---|---|
| Request drafted | Supported as a *learner-created proposal* |
| Request sent and custodian acknowledged | **Not supplied** by R1–R16; do not infer delivery |
| Incident-specific approval | **Not supplied** in R1–R16; may only be separately role-played and frozen as a new classroom decision |
| Source hold applied and effect checked | **Not supplied** |
| Copy received with collection/integrity receipt | **Not supplied** |
| Exact R15 deletion timestamp | **Unknown** because the policy clock anchor is unspecified |

**Test:** Run the adversarial claim “lead approved a request; therefore E1 or the source audit was copied.” Expected classification: **REJECT_COPY_WITHOUT_RECEIPT**, regardless of whether the student role-played a valid decision. A later Round C request may include B20 only after its release, under a newly bounded scope.

## Correction F — EX044: make fictional role-play authority explicit rather than implied by source records

**Exact insertion:** In §EX044 — Worked result, replace the sentence “Fictional incident lead and identity owner approve the proposed identity action; the identity administrator would execute it” and the following two-sentence “State receipts for this worked path” explanation with the source-versus-role-play distinction below. Leave the remaining chosen-option, fallback, separate protection/service tests and 09:45 review content intact.

**Finding:** EX044 requires **separate proposed, approved, executed and verified states**, with unsupported stages pending. The current model treats the incident lead and identity owner as having approved the action during Round C but supplies no separately frozen role-play receipt; R1–R24 establish only R19 capability and R21 tolerance. The reference worked path may simulate approval, but must identify which evidence is a new exercise decision rather than a supplied R-series action.

**Replacement model states:**

> **Round C, 09:37 UTC — source-only evidence:** The analyst proposes narrowly scoped revocation of the identified current desk-a session, identifying the incident lead and identity owner as required approvers and the identity administrator as prospective operator. **PROPOSED: recorded as classroom recommendation; APPROVED: pending/no R-series decision receipt; EXECUTED: not reported; VERIFIED: not reported.** If the group actually role-plays and freezes a valid, separate approval decision naming the session, approvers, scope, time and review conditions, it may change only the classroom **APPROVED** state to **SIMULATED APPROVED**, with the new decision pointer. This additional classroom approval is not a canonical R1–R24 fact. The administrator may execute only in a subsequent, separately documented branch; the Branch S report at 09:45 cannot be backdated as Round C execution or verification.

**Acceptance/negative control:** (a) R17–R21 plus no newly recorded classroom decision yields **PROPOSED / APPROVAL PENDING / EXECUTION NOT REPORTED / VERIFICATION NOT REPORTED**. (b) R17–R21 plus a documented fictitious C-approval-v1 yields **PROPOSED / SIMULATED APPROVED / EXECUTION NOT REPORTED / VERIFICATION NOT REPORTED**. (c) Inserting the later Branch S action into 09:37 yields **REJECT_LATER_BRANCH_EVIDENCE**. A reviewer should score either genuinely documented approval path without claiming unperformed action.

## Source check, navigation and residual editorial limits

[NIST SP 800-84, Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final), dated **September 2006**, was checked against the [original NIST PDF](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-84.pdf): printed **§4.4–4.5, pp. 4-4–4-5**, covers facilitated discussion, data collector observations, hotwash and after-action evaluation; **Appendix A, §A.3, p. A-9 onward**, supplies an illustrative tabletop after-action report. NIST distinguishes discussion-based tabletop exercises from functional exercises and operational tests. It does **not** assign this manuscript's 0–2 scoring, 9/12 passing threshold, L2 excerpts, fictional approvals or real readiness outcome. The book's classroom model and corrective examples are original; the NIST source retains its independent rights under [RIGHTS.md](../../../../../../RIGHTS.md). No real student submissions or authenticated operational measurements were supplied.

The chapter and internal Chapter 4 lab/answer anchors in the public manuscript were found. The six EX039–EX044 IDs each have exactly one exercise prompt and one final worked-result heading. EX040's four labeled lines, EX041's six-row release chronology and EX042's three bounded hypotheses are compatible with their requested output shapes and require no replacement. The submitted correction blocks address only demonstrated wording, authority, release, review-version and DEL4 evidence-shape problems; they do not renumber exercises or change the six-output teaching rubric.

No file, credentials, real incident records, patron data, service changes, live delivery or production tests are created by these narrative corrections. A tabletop score evaluates a synthetic learner packet, not an accredited qualification, completed incident, validated source hold or recovered real system. **Chapter 4 and the principal book remain DRAFT / NOT APPROVED.**
