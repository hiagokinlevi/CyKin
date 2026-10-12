# Chapter 06 supplementary teaching component — Control scope, authority, and observable containment

> **Editorial status: PUBLIC DRAFT — TRANSITORY COMPONENT, NOT AN ADDITIONAL CHAPTER.** Intended for integration into Chapter 6 of the single English [professional manuscript](../MANUSCRIPT.md#ch-06). It deepens, but does not replace, the existing section or duplicate exercise IDs. The Cedar Training Network (CTN) case and records C01–C33 are synthetic. Use no production systems or third-party accounts.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned writing follows the scope of [RIGHTS.md](../../../../../../RIGHTS.md). Third-party references retain their respective rights.

## Learning outcomes and precise starting checkpoint

After this component, a supervised responder should be able to (1) convert an evidence-bounded harm hypothesis into a control requirement; (2) select a target and enumerate possible bypass routes; (3) distinguish tolerable service impact from valid authorization; (4) specify state transitions from proposal to approval, execution, observed effect and expiry; (5) explain exactly which additional observation would invalidate the containment claim; and (6) defend an EX026–EX030 answer against an independent reviewer.

Begin at the **09:35 UTC checkpoint**. C13 establishes an owner-approved, read-only S42 observation: version 19 is unavailable, whereas the preserved 08:30 reference was open. C14 excludes q-144 from the complete manifest **of the approved batch-17 run**, not from every conceivable job. C15 reports no S42 addendum in the authoritative ledger through 09:33. C16 permits an *impact estimate* for a ten-minute S42 write hold. At this moment there is neither C17 approval nor C18 execution nor C19 test. Statements using later cards belong to later versions of the action record. The shared account's human user is still unknown.

### 6.A Define the containment property rather than the device setting

A device or application configuration is an implementation; a **containment property** is a falsifiable statement about behavior. “Enable guard g-22” is a prospective change request. “No unapproved S42 write is accepted through any in-scope route while the hold is active, and approved S40/S41 operations remain available” is a property that can be tested. The distinction matters when several paths reach the same state store. A front-end form may enforce a rule while a direct API, job worker or internal maintenance path uses a different authorization boundary. CTN does **not** provide evidence that any such alternate route was used during its real case; those routes are questions for the owner, not findings.

Write the control requirement as a five-part tuple: **asset and operation; initiating conditions; intended denial or permission; observation source; exception and expiry rule**. For CTN the asset is the S42 enrollment-state write, not the whole tenant or all actions by svc-enroll. The initiating condition is the owner-authorized temporary hold during investigation. The expected denial is an attempted in-scope S42 mutation that does not commit, while S40 remains available. An audit record must include a recognizable route and request identifier. The exception is not “security team may do anything”; it is a separately approved maintenance action with its own record, or an escalation if the hold harms legitimate enrollment. The expiry is an explicit boundary, not merely a reminder.

This property exposes an important ambiguity. A dashboard's “guard enabled” describes **configuration state**, whereas “request denied” describes one **observed transaction**. Neither alone establishes that the system enforces the guard uniformly. A verifier must ask whether the routing table, application handler, job path, background repair interface and state-store writes share the same enforcement boundary. If the owner cannot enumerate the routes, the verifier records “coverage unknown” and names who can resolve it. Do not fill the gap with confidence language.

The widely applicable principle is to make response actions proportionate to known risk and explicitly governed; [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates incident response with organizational cyber-risk management. The tuple and CTN guard are original course methods, not NIST-mandated fields.

### 6.B A decision comparison that treats availability as evidence

The initial decision is not “which intervention is strongest?” but “which supported intervention reduces a sufficiently likely harm path without causing an unaccepted business loss?” Compare the *proposed* session restriction, bounded S42 write hold and account-wide disablement using the same denominator: an additional unauthorized or mistaken S42 edit during the evaluation window.

Restricting s-77 is potentially cheap because it appears session-specific, yet C03's session and C05's q-144 have no verified join. If the session belongs to a healthy component, an otherwise sound session action could have zero incident benefit and nonzero availability cost. A successful IdP revocation would verify the session state, **not** that the S42 write path had been stopped. For account-wide disablement, the expected interruption of the legitimate approved batch-17 path is a first-class outcome, not an inconvenient side note. That action has more dependencies, a larger rollback plan and a higher approval threshold. It may become warranted if evidence later shows a broad active credential risk, but C13–C16 alone do not establish that condition.

A ten-minute S42 hold is narrower in *blast radius*, but narrowness and coverage are separate dimensions. It might still be wrong if most mutations come from an unguarded job route or the hold blocks a time-critical legitimate enrollment operation. Therefore the candidate must specify two independent acceptance axes: **security effect** (no accepted in-scope S42 writes on tested routes) and **business preservation** (S40/S41 function; owner-recorded S42 delay stays within tolerance). One axis cannot compensate numerically for a failure on the other when either is mandatory.

A useful decision sheet lists for each option: the suspected harm path; source cards and confidence; the least privilege target; affected services and named dependency owner; expected duration; rollback actuator and decision owner; minimally invasive test; test blind spots; collection/retention consequences; and the exact stop condition. Where a field is unknown, retain “unknown” and assign the question. Recording the unknown is more informative than a falsely complete risk score.

### 6.C Authority is an event with a scope, not a job title

Organizational roles establish who can **request**, **approve**, **operate** and **independently check** a change; they do not merge those actions. In CTN the analyst prepares the case-bound recommendation. The service owner accepts a business availability tradeoff, the incident lead coordinates a time-limited response, the application operator performs the approved configuration change, and another authorized observer inspects the resulting records. This separation is a design choice of the case. A real organization must map it to its actual delegated-authority matrix and emergency procedure.

An approval event should be reconstructable as a small contract: **case ID, target, action, allowed routes, forbidden collateral actions, approver and capacity, effective window, operator, rollback owner, evidence-preservation duties and escalation**. The phrase “approve containment” is insufficient because it could be misread to authorize a session purge, a shared-account disablement or a database rewrite. For C17 the authorized object is **only the S42 write hold** through 09:47. There is no authority to disable svc-enroll, alter S40/S41 or make a final actor attribution. C16 only says the initial interruption might be tolerable; its evidentiary role is an impact assessment, not a signature.

An operator's receipt should bind the approval to the actual configuration version, reported start time, outcome and error condition. C18 reports g-22 enabled at 09:39. That receipt deserves preservation but is not independently sufficient to claim enforcement. C19 at 09:42 observes q-147 denied on one S42 application route while q-148 for S40 succeeds. This supports observed route behavior at that timestamp, not global coverage. A supervisor asking “Was containment successful?” should receive the calibrated answer: **the approved hold was reported enabled and one route showed the intended selective denial; other routes are unverified**.

Avoid collapsing these records into a single green checkbox. Each transition has a different evidence producer and a different possible failure: approver identity or scope could be missing; a change could be approved but not deployed; it could be deployed to the wrong environment; it could take effect on one path and fail elsewhere; or it could remain after expiry. A practical record carries status and source separately so the next shift can investigate each link.

### 6.D Chronology as a permission-and-observation ledger

Use immutable checkpoints for a reproducible incident narrative:

| UTC checkpoint | Permitted statement at that time | Statement that is **not** yet justified |
|---|---|---|
| 09:35 (C13–C16) | S42 is unavailable in the read-only owner-approved view; propose a bounded hold because a further S42 write is a plausible harm. | “The S42 hold is approved or active.” |
| 09:37 (C17) | Service owner and incident lead have approved the S42-only hold until 09:47, with a named operator and rollback. | “The operator deployed it; all write paths are blocked.” |
| 09:39 (C18) | Operator reports configuration g-22 enabled under C17. | “Every potential write route was tested.” |
| 09:42 (C19) | One application route denies q-147 for S42 and accepts q-148 for S40 in observed audit records. | “Alternate API, database and job paths cannot write S42.” |
| 09:47 planned expiry | A future decision/checkpoint specified by C17; by 09:42 no renewal is shown. | “The restriction will automatically remain until incident closure.” |

A later chapter adds C20 and a **new** C21 extension approval at 09:46:30, followed by a 09:46:45 operator receipt. That development must not be added to the 09:42 knowledge column. A past decision is evaluated against evidence and authority available **then**, not against a tidy retrospective account. If a review finds a decision imperfect, preserve the original and append a correction with its timestamp.

The expiry needs active ownership. A time-based rollback may create a new exposure window, but quietly overriding the expiry is itself unauthorized scope expansion. Before expiry, the service owner should be asked whether the observed benefit and legitimate cost justify a new approval; if no decision arrives, follow the actual fail-safe/default procedure recorded in the authorization, not the analyst's assumption. C17 states an automatic expiry. Chapter 7's C21 later documents renewal; no reader may silently substitute that fact at the Chapter 6 decision point.

### 6.E Two worked arguments: a defensible recommendation and a seductive mistake

**Defensible 09:35 note:** “The owner-approved C13 view shows S42 unavailable and associates the stored state with q-144, while C14's complete approved-run manifest lacks that request. The person or process behind q-144 remains unresolved. To reduce the chance of another S42 change while the source question is investigated, request a ten-minute S42-only hold, conditional on explicit service-owner and incident-lead approval. Ask the application owner which write routes it covers. Appoint an operator and rollback owner, preserve audit records, test one S42 denial and a legitimate S40 acceptance through approved observations, and label any untested route unverified. Do not disable svc-enroll based only on these cards.”

**Incorrect note:** “C14 proves an attacker used svc-enroll. C16 approved emergency containment, so disable the account until the forensic investigation finishes and record the issue resolved when the portal shows S42 unavailable.” It turns a missing request in one manifest into human attribution, misclassifies tolerability as authorization, expands the intervention to a shared dependency, and uses a user-facing symptom as proof of prevention. Worse, a portal that still displays unavailable might simply be showing the very business harm the team wants to repair. The correct revision states the narrow harm, proposes an action, names its decision owner and insists on a bounded verification claim.

When discussing alternatives, explain **why rejected** as well as **why chosen**. A session-only action is rejected for insufficient session/request linkage, not because sessions never matter. Account disablement is deferred because the expected business cost is broader than supported harm, not because it could never be legitimate. The S42 hold is provisional because its enforcement surface and operating cost must be tested.

### 6.F Offline laboratory: state-machine and route-coverage separation

**Objective.** Demonstrate that authorization, reported execution and observed effect cannot be inferred from one another. **Inputs.** Four synthetic tuples reflecting C16–C19 and a separately labeled V6 route fixture. **Environment.** Python 3 standard library only, disconnected from networks; no login, file write or command against a tenant. **Success condition.** Reproduce the exact lines below; explain why all-route coverage remains unknown in CTN even though V6 fails a route test.

~~~python
checkpoints = [
    ("09:35", False, False, ()),
    ("09:37", True, False, ()),
    ("09:39", True, True, ()),
    ("09:42", True, True, ("application",)),
]
for clock, approved, reported, observed in checkpoints:
    state = (
        "proposal" if not approved else
        "authorized" if not reported else
        "reported-enabled" if not observed else
        "observed-one-route"
    )
    all_routes = "verified" if len(observed) == 3 else "unknown"
    print(f"C6 {clock} {state}; all-routes={all_routes}")

# V6 is an isolated training variant, never a CTN incident card.
v6 = {"browser": False, "api": True, "S40": True}
verdict = "PASS" if (
    not (v6["browser"] or v6["api"]) and v6["S40"]
) else "FAIL"
print("C6 V6 all-route=", verdict)
~~~

**Executed result** (Python 3, in-memory fixture):

~~~text
C6 09:35 proposal; all-routes=unknown
C6 09:37 authorized; all-routes=unknown
C6 09:39 reported-enabled; all-routes=unknown
C6 09:42 observed-one-route; all-routes=unknown
C6 V6 all-route= FAIL
~~~

The boolean **False** for a V6 write means denied, and **True** means accepted; the API's accepted S42 write fails V6's all-route denial criterion. The CTN state-machine deliberately has no all-route evidence. Its arbitrary three-route threshold is a teaching placeholder, **not** a known CTN route count or a real coverage estimator. A reviewer should reject the program if it is used to turn a fixture assumption into operational assurance. To extend safely, introduce a local fictional inventory with three named routes and require one independently sourced result per route; do not generate writes to a real service.

### 6.G Focused enrichment of existing exercises and worked results

The following are supplementary decision criteria and solution reasoning for the **existing** IDs, not additional or renumbered exercises. Integrate teaching into Chapter 6 and the explanations into the book's single worked-answer appendix.

**EX026 — impact ledger extension and rationale.** Add a **reliability column** to the requested four rows: C13 is strong for the observed stored state because the custodian queries the owner-designated source; C10 is weak for authoritative state because screenshot clock/cache provenance are unresolved; C15 is strong for the official ledger's absence of an addendum **through 09:33**, not for all possible emergency communications; and C05/C14 label a service account and exclude one approved job run, not a person. Worked interpretation: “confirmed stored-state mismatch; display corroboration conditional; approved-ledger scope insufficient for S42; human attribution unknown.” An examiner should mark down any claim that the absence of approval proves adversarial intent.

**EX027 — option review extension and rationale.** In addition to the benefits/costs/approvals, ask the learner to specify which source could falsify *each* candidate's benefit. For s-77 restriction, a fresh, authorized S42 write unassociated with s-77 would show the session action insufficient for that harm. For an S42 hold, an accepted S42 write on a separate route shows inadequate guard coverage. For account disablement, failing batch-17 demonstrates unacceptable collateral effect even if suspect calls stop. Worked selection: propose the limited hold at 09:35, conditional on explicit approval; C16 remains only tolerance. Do not award the full score merely for saying “least privilege.”

**EX028 — receipt-chain extension and rationale.** Require four distinct source references and prohibit backfilling: 09:35 recommendation, 09:37 C17 authorization, 09:39 C18 reported change, 09:42 C19 observed one-route result. The difference between **reported** and **observed** must appear in the verbs. Worked conclusion: “one tested application route selectively denied S42 and allowed S40; alternate routes unverified; hold planned to expire 09:47.” The extension is not a new ID and makes no claim about the later C21 extension.

**EX029 — rollback extension and rationale.** Require an explicit *decision trigger*, *operator action receipt* and *post-action verification* as separately fillable fields; leave actual receipt and observation blank. Expiry, out-of-tolerance legitimate enrollment harm and an observed bypass are three distinct reasons to convene the owner. Worked answer preserves C17–C19 and records the need to compare guard version, S42/S40 behavior and unexpected edit monitoring. The historical case's future C21 must not appear as a known approval in a 09:42 card.

**EX030 — isolated V6 extension and rationale.** Require a one-line truth table: browser S42 denied, API S42 accepted, S40 accepted. Worked conclusion: the browser-only observation would yield a false sense of global safety; the V6 all-route criterion fails because the API route accepts a write. The next task is an application-owner review of shared enforcement points and a controlled retest of both routes. **Never cite V6 to claim the main CTN guard was bypassed.**

### Limits, handoff, and sources

This component does not prove that a control was deployed outside the fictional C17–C19 case; the executable test validates only local logic over invented tuples. The control surface, integrity of operational receipts, human actor, number of affected enrollments and unobserved routes remain unresolved. Incident response should retain source provenance and coordinate with authorized owners; the older [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) offers context for forensic evidence handling but is not a current universal operational runbook. The CISA [federal incident and vulnerability response playbooks announcement](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/2fc7609) describes standardized decision-oriented procedures for federal civilian systems; CTN's approval form is a separate fictional adaptation, not a mandatory federal control.

**Synthesis.** Containment quality is the product of a bounded harm claim, explicit authority, a correctly scoped intervention, an observed result and a known expiry or reauthorization gate. Missing one component is not fixed by calling the others “green.” Hand Chapter 7 a versioned case record, not a conclusion about intent.

### Continue studying — supplementary component for chapter 06 of 12

[← Chapter 05 (authored draft)](../MANUSCRIPT.md#ch-05) · [Course chapter index](../../SUBJECTS.md) · [Chapter 07 (authored draft) →](../MANUSCRIPT.md#ch-07)

Return to the [Chapter 06 principal draft](../MANUSCRIPT.md#ch-06) to read the canonical lesson and its original EX026–EX030 statements; the [single book answer appendix](../MANUSCRIPT.md#worked-answers) remains authoritative until integration and review.
