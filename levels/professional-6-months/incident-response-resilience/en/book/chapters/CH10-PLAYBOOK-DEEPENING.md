# Chapter 10 supplementary teaching component — Testable playbook design and negative controls

> **Editorial status: PUBLIC DRAFT — TRANSITORY COMPONENT, NOT AN ADDITIONAL CHAPTER.** Intended for integration into [Chapter 10 of the single professional English manuscript](../MANUSCRIPT.md#ch-10). It deepens the existing P0/P1 teaching and EX046–EX050 answer reasoning; it does not create, rename or renumber exercises. Cedar Training Network (CTN), C01–C33, V10 and V10b are fictional teaching materials.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). The [rights policy](../../../../../../RIGHTS.md) governs the original work; externally cited standards and playbooks retain their own rights.

## Competencies and case boundary

On completing this component, the learner should be able to (1) convert a misleading prose checklist into a decision-controlled playbook; (2) specify inputs, owners, exits and evidence artifacts for seven gates; (3) reason over the main CTN case without retroactively exposing future cards; (4) test a harmless negative control and an unavailable-approver branch; (5) separate document quality from operational effectiveness; and (6) justify the existing EX046–EX050 worked answers.

Chapter 10 is a **retrospective engineering exercise** after the main CTN cards through C33 have been released. That does not authorize rewriting earlier decisions with later evidence. In a timeline-based walkthrough, Gate 3 at 09:35 must not use C20, C29 or C33; Gate 5 at C27 must stop on the failed audit criterion even though C28 later succeeds in an isolated copy. Variants V10 and V10b are **parallel synthetic tests**, not corrections to historical CTN C cards. The goal is to build a safer future procedure, not to pretend a draft playbook executed the original incident.

### 10.A A playbook is a decision interface, not a command transcript

The defective specimen **P0** says, in essence, respond to any sign-in alert by disabling a shared account, restoring the latest backup, checking whether the portal loads, emailing a breach notice and closing the incident. It looks efficient because it hides the questions an operator must answer: whether the alert affects the business, what an account supports, what permission exists, whether backup data are correct, what the service test covers and whether any data exposure is established.

A deployable playbook should instead act as a **decision interface** between evidence, accountable owners and operational procedures. It can prescribe how to ask and document questions without granting action rights. A separate operator runbook, reviewed for the real architecture and authorization, may eventually define safe commands. The classroom P1 is not that operator runbook. This distinction protects a novice from treating a generic text example as permission to disconnect production accounts or send notifications.

Treat each gate as a typed contract with these fields: **entry condition; required evidence; permitted analyst output; decision owner; approval boundary; operator if applicable; pass/fail/unknown branch; stop/escalate condition; emitted case artifact; next checkpoint**. The words *unknown*, *unavailable* and *not authorized* must be first-class branch values. If the only outputs are “yes” and “proceed,” the playbook will eventually force an unsafe decision when inputs are missing.

This design is aligned in spirit with [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), which integrates response with organizational cyber-risk management. The CTN gate fields are **original teaching choices** and should not be represented as mandatory clauses from that publication.

### 10.B Seven gates as a controlled workflow

A usable P1 design supports the following **seven gates, numbered 0–6**, without inventing an eighth stage or changing the existing specimen's scope.

| Gate | Contract question | Output that another responder can inspect | Failure or unknown branch |
|---|---|---|---|
| 0 — Intake | What source, event time, reporter and business function justify case opening? | Case record and raw wording, with source reference | Route uncertain service linkage to triage, not automatic disruption |
| 1 — Preserve and bound | Which source, fields, time window and custodian can test the claim? | Scoped collection request, provenance and expiry risk | Missing access approval = stop access and escalate authorized preservation |
| 2 — Prioritize | What are impact, confidence and source-loss urgency? | Provisional severity with next review condition | No reliable score = record unknown and refer to incident lead |
| 3 — Contain | Which least-disruptive target is expected to limit harm, and who approves it? | Action-specific proposal, permission, operator, rollback, test | No approval or untestable scope = **no disruptive execution** |
| 4 — Verify cause | What mechanism is supported, what would disconfirm it, and what baseline is approved? | Versioned claim/evidence ledger and cause-to-fix contract | Unproven attribution remains unknown; do not destroy original source |
| 5 — Recover | Which target data, service paths, identity controls, audit and rollback must pass? | Preannounced acceptance sheet, isolated results, separate production receipts | Any mandatory test failure = no-go until a new reviewed decision |
| 6 — Communicate/review | What audience needs which supported facts, who may release them and when is the next status? | Versioned draft, approvals, dispatch receipt if sent, assigned improvement | Missing release approval = draft only; data question goes to privacy/legal owner |

This is intentionally **not** a rigid chronological claim that a service cannot preserve evidence before an incident lead assigns severity. Some gates may be revisited as new evidence arrives. But revisiting does not make an earlier authority grant larger: C21's extension is a new permission event, not a retrospective reinterpretation of C17. Gate dependencies should be explicit. A cause hypothesis does not itself authorize account disablement, and an isolated recovery pass does not imply production approval.

The P1 record should include a **source horizon** for every branch. At 09:14, the team can discuss initial priority and C08 retention; at 09:35 it has C13–C16; at 09:42 it has C17–C19; at 09:54 it can discuss C20–C23; at 10:16 it can reject C27; at 10:45 it can recognize C30's limited acceptance; at 11:00 it has C31–C33's bounded data question. A second reader should be able to reconstruct the decision without looking at cards not yet released.

### 10.C Test inputs must be selected to reveal wrong branches

A walk-through that tests only the main CTN case is inadequate. Because the main case includes a confirmed stored-state problem, a flawed playbook may appear useful even if it would unnecessarily disrupt a harmless alert. Negative controls expose whether the procedure can **do less** when evidence justifies less.

**Main CTN branch:** C13 confirms the S42 state discrepancy; C14/C15 narrow approval and job-origin claims; Gate 3 proposes a scoped hold. C17 approves it, C18 reports it enabled and C19 shows one observed route behavior. Gate 4 accepts C20's verified q-144 mechanism without naming a human; C22/C23 leave separate identity questions. Gate 5 refuses C27 after the blank audit actor and then recognizes C28 only as an isolated candidate pass; C29/C30 supply later, distinct production and limited acceptance records. Gate 6 prepares, but does not send, status drafts while C31–C33 remain uncertain about external delivery.

**V10 negative control:** A separate alert names the shared account, but the owner-approved read-only slot state is correct, an approved run manifest includes the exact questioned request, and no unexpected task or data signal is present **in the supplied scope**. The correct branch is bounded documentation and review, **not account disablement, restore or breach notice**. A supervisor may determine whether downgrade or closure is appropriate under the real criteria. This variant cannot disprove the actual main case because it is a different evidence set.

**V10b missing-approver test:** The relevant owner is unavailable while an authorized source faces a stated retention limit. The correct result is an authorized **preservation escalation** and a pending disruptive decision. The analyst must not make “emergency” mean “approval invented by the playbook.” A readiness defect should be recorded if there is no reachable alternate. The test succeeds when the procedure safely stops despite pressure to make progress.

These branches challenge three different failure modes: **incorrectly treating harm as universal**, **incorrectly treating harmlessness as impossible**, and **incorrectly treating missing authority as permission**. An assessor should not report “the playbook handled three incidents.” It handled one fictional main case and two separate hypothetical tests. The purpose is decision validation, not an operational case count.

### 10.D Separate approval, execution and independent verification in the data model

A common documentation anti-pattern is a single “completed” field shared by the approver, operator and reviewer. That field has no stable meaning. Instead record an **approval object** with approver, scope, issue time and expiry; an **execution object** with operator, target version, time and error/receipt; and a **verification object** with independent observer, source, query/route coverage and verdict. All three carry a reference to the case and action ID. If a step has not occurred, its object is pending, not filled with anticipated success.

For CTN, the P1 implementation might show C17 as approval, C18 as reported execution and C19 as one-route observation. It must not collapse them to “S42 completely blocked.” At C21 an approval **extension** and a separate operator receipt update the allowed time, not every other permission field. At C24 the task-only disablement is distinct from the C25 later identity action. These are natural examples for a **state-machine review**: no transition to “verified” without an observation; no transition to “executed” without the required authority; no silent extension at expiry.

Quality assurance should include **stale-input tests**. What happens when the state read is older than the proposed change? What if the service owner changes the approved target? What if an evidence source expires before the custodian replies? What if the alleged negative control contains a hidden unexplained request not represented in its approved manifest? The playbook should route each inconsistency to a bounded new question and stop the relevant action. It should not hardcode that a task name or account label alone is suspicious enough to disable an identity.

### 10.E Document scoring is not release certification

The principal manuscript's six criteria use 0 for absent or contradicted, 1 for vague but recognizable and 2 for explicit, testable condition/owner/artifact: (1) trigger and bounded scope, (2) roles and approvals, (3) source provenance and uncertainty, (4) containment verification and rollback, (5) recovery acceptance and failed-test handling, and (6) audience-specific communications and review.

P0 earns **1/12** in the existing worked assessment: its generic “portal loads” supplies only a vague observable recovery condition worth 1; the other fields are unusable or unsafe. The P1 **document design** can score **12/12** because the seven gates express those conditions. Neither result says that P1 operated safely on any real system. The scorer should attach evidence from the actual text, not negotiate points to make a preferred draft look publishable.

A separate **operational readiness gate** is still required. Before live adoption, a real owner must verify contacts and delegation, retention procedures, architecture-specific route coverage, approved tools, simulation outcomes, accessibility, security/privacy review and change control. A high score with no owner approval is still **draft**. The [CISA federal cyber incident and vulnerability response playbooks](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/2fc7609) illustrate why documented coordination paths matter; they were written for federal civilian systems, and local adaptation requires scope and rights review.

Metrics are equally vulnerable to gaming. “Time to first action” might reward immediate unauthorized account disablement; “time to close” might reward avoiding questions. Prefer measurements whose numerators and denominators encourage auditable decisions, for example: number of **approved disruptive actions with complete target/expiry/rollback fields** divided by all disruptive actions performed; percentage of recovery candidates correctly stopped on a mandatory failure; and number of privacy-sensitive drafts dispatched without designated approval (target zero). Record sampling window and exclusions. A denominator of zero should be reported as **not applicable**, not “100% compliance.”

### 10.F Worked good and bad release reasoning

**Defensible P1 draft 0.2 note:** “Replaced P0's automatic shared-account disable, latest-backup restore and unsupported breach message with seven evidence- and authority-gated decisions. Walked the main CTN cards only at their release checkpoints; stopped C27's failed audit gate; and kept C28 isolated from C29 production approval. V10 produced no disruptive action on an owner-confirmed harmless path; V10b escalated bounded evidence preservation without inventing an approver. Remaining before release: real owner delegation and technical route tests, privacy/communications approval mapping, and a witnessed simulation with retained results. Status: **training draft, not for production**.” This describes work performed without claiming the playbook passed field validation.

**Incorrect note:** “P1 scored 12/12, fixed incident response and has been deployed. Any unavailable owner can be bypassed for urgent actions.” It confuses written-field coverage with demonstrated operations, overrides the permission boundary precisely where the V10b test demands restraint, and asserts deployment absent any case receipt. It also avoids the uncomfortable result that a valid operational response sometimes consists of **not acting disruptively**.

### 10.G Offline laboratory: rubric score and branch conditions

**Goal:** verify the classroom P0 score and that a missing approver or absent harm cannot result in a disruptive action in a tiny decision model. **Inputs:** six P0 criterion scores and three isolated branch tuples. **Safety:** standard Python 3 only, no network, no file access, no real response commands. **Success:** output exactly matches the lines below, and the learner explains that a branch result is a **recommendation state**, not a record of execution.

~~~python
criteria = [0, 0, 0, 0, 1, 0]
print("C10 P0 points=", sum(criteria))
branches = [
    ("CTN", True, True),
    ("V10", True, False),
    ("V10b", False, True),
]
for branch, authority, harm in branches:
    decision = (
        "PROPOSE-AND-VERIFY" if authority and harm
        else "NO-DISRUPTION" if not harm
        else "ESCALATE-NO-EXECUTION"
    )
    print("C10", branch, "=" + decision)
~~~

**Executed output:**

~~~text
C10 P0 points= 1
C10 CTN =PROPOSE-AND-VERIFY
C10 V10 =NO-DISRUPTION
C10 V10b =ESCALATE-NO-EXECUTION
~~~

The CTN **authority=True** fixture represents a deliberately simplified point **after** relevant approval, not permission at the 09:35 proposal checkpoint. PROPOSE-AND-VERIFY does **not** execute anything. The toy boolean harm field discards evidence strength, impact and scope; therefore this model cannot replace the seven-gate record. Its value is to fail visibly on two unsafe shortcuts. A stronger classroom test would inject an expired approval and an unverified route; both should leave action pending until a fresh owner decision. These are proposed test cases, not reported CTN outcomes.

### 10.H Extensions to EX046–EX050 and worked-answer rationale

**EX046 — defect inventory extension.** A high-quality answer groups flaws by *failure mechanism* rather than counting synonyms. Worked categories: indiscriminate trigger; absent owner approval; shared-account dependency harm; excessive containment scope; backup-versus-business-target mismatch; missing alternate-route and audit tests; speculative notice; premature closure/no next checkpoint. Cite C14 for legitimate batch-17, C17/C19 for narrow guarded action and verification, C26 for snapshot regression, C27 for failed audit criterion, C30 for ongoing monitoring and C31–C33 for unresolved data status. At least six independently reasoned flaws must state likely consequences.

**EX047 — seven-gate rewrite extension.** Require one example of a **blocked** branch and the artifact that records it. Model structure: Gate 0 opens and bounds the case; 1 requests custodian-controlled evidence; 2 records provisional priority; 3 proposes a scoped, approval-gated intervention; 4 tests a cause hypothesis against a preserved baseline; 5 checks owner-approved data/routes/audit/rollback and stops on failure; 6 creates versioned audience status with release owners. No gate grants blanket operational authority. Strong work includes an owner, explicit stop and next step for each gate.

**EX048 — three-branch walkthrough extension.** Main case: propose, approve and separately observe controls as C cards arrive; do not prematurely promote C28 to production. V10: correct owner-confirmed state and approved request mean no observed harm path within supplied scope; document and avoid disruption. V10b: missing authority plus retention risk means authorized preservation escalation and **no disruptive execution**. A correct answer includes **different evidence scope and decision state in every row**, with no cross-branch reuse of findings.

**EX049 — quality-score extension.** Model P0 0+0+0+0+1+0 = **1/12**; P1 as written can earn **2 in all six criteria = 12/12** for document structure. The scorer must cite the gate fields supporting each point and keep a second checklist for technical test, owner approval and exercised usability. The rubric is frozen before testing; lowering a criterion after the fact to preserve a perfect score is a quality defect. A document may look perfect while real route coverage or emergency availability is unknown.

**EX050 — versioned release-note extension.** A 100–160-word draft 0.2 note should name the main CTN, V10 and V10b branch results, at least two outstanding owner/technical checks, one assigned improvement with a falsifiable retest, and the words **not for production**. The improvement might be: “Service owner to establish after-hours alternate; test simulated unavailable-owner escalation until a signed preservation request is obtained.” This is a proposed work item, not evidence it was implemented. The model must neither claim the book reached 300 verified A4 pages nor that Chapter 11's future simulation has already passed.

### Synthesis, sources, and handoff

The code exercises a small classifier and does not validate a deployed playbook. The case's negative controls are synthetic and contain no external operational data. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) and the [CISA federal playbook publication](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/2fc7609) offer primary guidance on response integration, recovery exercises and documented coordination. The [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) reference is older exercise-program guidance whose practical applicability should be reviewed rather than treated as a current platform specification.

**Synthesis:** a safe playbook encodes the ability to stop. It forces the user to separate evidence from hypothesis, proposal from permission, execution from independent verification, and draft words from sent communications. Its document score is the beginning of quality assurance, not the end of operational review.

### Continue studying — supplementary component for chapter 10 of 12

[← Chapter 09 (authored draft)](../MANUSCRIPT.md#ch-09) · [Course chapter index](../../SUBJECTS.md) · [Chapter 11 (authored draft) →](../MANUSCRIPT.md#ch-11)

Read the [principal Chapter 10](../MANUSCRIPT.md#ch-10) for P0/P1 and the original EX046–EX050 prompts; the [one-book worked-answer appendix](../MANUSCRIPT.md#worked-answers) remains the canonical location for exercise numbering until supervised integration.
