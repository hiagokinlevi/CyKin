# Professional Incident Response — Chapters 01–05 Expansion (PUBLIC DRAFT)

**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). **Course:** 039 / Incident Response and Cyber Resilience / Professional, six months. **Language:** English. **State:** temporary public teaching draft; not a second book or completed edition. Consolidation target: [MANUSCRIPT.md](../MANUSCRIPT.md). All original C01–C33 and EX001–EX060 IDs, original teaching, release chronology and answers remain authoritative until integrated.

**Integration convention:** Insert each chapter's teaching after the final existing numbered instructional subsection and before its “Common mistakes and limits” heading. Insert the corresponding worked-answer expansion immediately after the same subject's EX results within the manuscript's [worked-answer appendix](../MANUSCRIPT.md#worked-answers). These additions do not change the subject count, exercise IDs, or navigation.

## Chapter 01 — Incident lifecycle and organizational readiness

**Precise location:** after Chapter 1 §1.10, before “Common mistakes and limits”. This material develops the C01 readiness exercise for a supervised practitioner without inventing an incident at 08:40.

### Readiness is a set of independently testable decisions

C01 is a synthetic inventory, not an alert or proof that its listed capabilities function. The service owner must state what an acceptable enrollment does *before* the analyst chooses which logs to inspect. For a proposed isolated enrollment test, the business invariant might be: one authorized reservation consumes no more than one available place, returns a stable operation reference, and leaves the slot unchanged after a rejected request. This is a **proposed test condition**; the current CTN cards do not prove the implementation honors it.

Separate four planes. The **business/data plane** contains the front end, enrollment API, scheduled and manual write routes, and authoritative slot state. The **observation plane** contains application audit, identity telemetry, collector, index and restricted export. The **authority plane** contains the service owner, identity custodian, incident lead, delegated alternates and their separate rights. The **recovery plane** contains an identified copy, isolated restore method, accepted slot targets and tested return conditions. A green signal in one plane does not certify the others. A healthy collector can omit a manual write route; a working backup job can produce an unusable restore; a reachable custodian may be unable to authorize an account restriction.

A responder's dependency graph should have *typed edges*, not just boxes. “Scheduled writer → API” is a proposed data path. “API → audit store” is a proposed observation path. “Audit store → case copy” requires separate selection, custody and permission. “Service owner → approval record” is a decision path, not a technical event. Each edge should have a producer, consumer, time basis, failure signal and an accountable source to ask. Unless tested with a known synthetic event and a reviewed source receipt, mark it **claimed**, **not verified** or **failed**, never “all logs available.”

The distinction is central to [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), which places incident response within cybersecurity risk management, and [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), which describes outcomes without prescribing CTN's invented workflow. The graph and test rubric here are original teaching methods, not NIST requirements.

### A concrete failure investigation without inventing a breach

**Synthetic preparation variation, not a new C-series card.** Suppose the application owner proposes a harmless scheduled S41 write in an approved training tenant. The source audit returns a stable request ID, but the manual write route returns only an account label. The first observation can support a *scheduled-route test*, while the second prevents reliable manual-route request correlation. It is unsafe to declare that the entire enrollment API has complete audit coverage.

Meanwhile, C01's “API audit: 24 hours” has no retention anchor. It could refer to source-event age, collector visibility, query-horizon constraints or export-artifact lifetime. The last safe retrieval time differs across these interpretations. The proper next question is: which producer and dataset, which timestamp anchors the policy, what happens with ingestion lag, and what oldest expected marker can be retrieved by an authorized custodian? Adding twenty-four hours to a selected event time does not answer any of these source questions.

Finally, C01 names no after-hours identity alternate or service-owner fallback. That is a capability gap, **not evidence of malicious activity or negligence by a specific person**. Record the primary role, attempted contact, missing authority path, event that should trigger escalation and which non-disruptive work may continue. An analyst may draft a limited request; neither urgency nor access to a dashboard grants permission to use substitute credentials.

### Supervisor handoff: evidence, not assurances

Each proposed readiness test needs: decision question; exact synthetic input and producer; permitted route and approval; a positive expected row with original UTC time, slot and request ID; an unrelated S40 negative control; a collection clock and twenty-minute acceptance window; an independent reviewer; and a failure/rollback rule. The **test authorization**, **executed rehearsal receipt**, and **service readiness acceptance** are separate states. A supervisor can approve one while declining the others. The output should tell the next responder exactly which missing field, unreachable custodian or unverified route could invalidate a future incident claim.


### Offline laboratory C1X — distinguish source coverage from collector appearance

**Purpose:** Test the logic of a four-row *declaration*, not a live CTN environment. This exercise is separate from C01, from the original C1 coverage fixture, and from any production collection. Run Python 3.10+ in a local isolated interpreter; it creates no files, changes no service and makes no network calls.

The invented entries deliberately separate four failure modes. A scheduled-path declaration has the expected slot and key within the twenty-minute goal. A manual-path declaration lacks a join key even though it appears to have returned quickly. An identity-detail declaration has an identifier but no retrieval measurement. A negative-control event belongs to S40 while the requested scope is S41. Predict each state before running.

~~~python
from dataclasses import dataclass

@dataclass(frozen=True)
class Probe:
    route: str
    slot: str
    wanted_slot: str
    key: str | None
    latency_min: int | None

def assess(p):
    if p.slot != p.wanted_slot:
        return "FAIL_WRONG_SLOT"
    if p.key is None:
        return "FAIL_MISSING_JOIN_KEY"
    if p.latency_min is None:
        return "UNKNOWN_NOT_RETRIEVED"
    if p.latency_min > 20:
        return "FAIL_WINDOW"
    return "PASS_DECLARED_FIXTURE"

probes = [
    Probe("scheduled_api", "S41", "S41", "req-demo-01", 9),
    Probe("manual_api", "S41", "S41", None, 4),
    Probe("identity_detail", "S41", "S41", "sid-demo-01", None),
    Probe("negative_S40", "S40", "S41", "req-demo-02", 7),
]
for p in probes:
    print(f"{p.route}: {assess(p)}")
assert assess(probes[0]) == "PASS_DECLARED_FIXTURE"
~~~

**Executed output:**

~~~text
scheduled_api: PASS_DECLARED_FIXTURE
manual_api: FAIL_MISSING_JOIN_KEY
identity_detail: UNKNOWN_NOT_RETRIEVED
negative_S40: FAIL_WRONG_SLOT
~~~

A useful interpretation states why no “overall ready” flag is produced. The scheduled test is only logically consistent *if its fields were authentic*. The manual test cannot establish a request-to-audit join. The identity test has no measured availability. The S40 control exposes a scope mismatch; silently expanding the selection to include S40 would defeat the control. Neither a plausible ID string nor a small latency number independently authenticates a log.

**Adversarial control:** Replace the first probe's slot with S40 and predict FAIL_WRONG_SLOT despite an unchanged key and latency. Then restore it and replace the manual probe's missing key with `"invented"`: the code would return PASS_DECLARED_FIXTURE, demonstrating why a passing Boolean classifier is **not a producer receipt**. Do not insert these variants into the C01 case facts.

**Submission and scoring:** Produce a four-row comparison, two explicit falsifiers, a proposed request to the application custodian and a short distinction between the executed *offline code* and an unexecuted *authorized route rehearsal*. Six local points: four correct classifications, one for identifying how the S40 negative control detects scope broadening, and one for preserving the authority/provenance limitations. An “all CTN logs verified” conclusion fails regardless of the numeric score.

### Prioritize by decision harm, not by a readiness percentage

An entry marked `yes` in the original C1 fixture is a declared teaching value. Even “2/5” is not an organizational readiness score: sources differ in criticality, time horizon and relation to safety. A source needed to preserve a short-lived identity trail may matter more to an immediate escalation than several low-value inventory cells. Conversely, a restore check may be foundational for continuity but not answer a narrow identity-attribution question. Assign each gap an **affected decision**, **failure consequence**, **last defensible decision point if known**, **safe evidence to request**, **authorizing role**, and **retest criterion**.

Compare two synthetic backlog items. Item A is missing an after-hours identity alternate; its failure mode is *permission unavailable during short retention*. Item B is missing the last isolated backup restore; its failure mode is *copy existence without verified service correctness*. Neither is “complete” just because a contact number or backup job is supplied. Item A closes when an approved delegated role has been reached during a timed rehearsal and the data-owner rule is checked. Item B closes only for the tested copy, environment and target when an authorized restore has been executed, measured, compared with approved state and accepted by the service owner. Neither criterion is a generic compliance certificate.

**Synthesis and next chapter boundary:** Chapter 1's C01 describes preparedness *before an incident*. The S41 training experiments here remain proposals and invented offline exercises. When C02 appears at 09:04 in Chapter 2, do not import the synthetic PASS state as evidence that CTN actually audited anything. Instead, carry the gaps forward as explicit owner/authority questions.

**Continue studying — professional Chapter 01 of 12:** [← Course home](../../../README.md) · [Chapter index](../../SUBJECTS.md) · [Chapter 02 →](../MANUSCRIPT.md#ch-02).

### Worked-answer expansion — EX001–EX005

**Integration:** Add the following reasoning immediately after the original Subject 1 model answers and C1 original worked result. These are *extensions*, not substitute exercise IDs. The original 0–2 per-exercise rubric remains in force.

**EX001 — Why each dependency supports a different decision.** A reviewable map should include five or more rows such as: API audit → “which request changed S41?” → application custodian → scheduled/manual coverage unverified; IdP → “which account/session fields can be produced?” → identity custodian → no after-hours alternate; support → “what was reported and received?” → support lead → no authoritative backend state; change ledger → “was S41 in a permitted task version?” → service owner → addendum process unknown; backup → “can selected slot values be reconstructed?” → recovery lead → restore correctness untested. Every row states *how to falsify readiness*: a missing scheduled route, unusable key, unavailable alternate or failed isolated restoration. C01 does not supply results for these tests. A table simply saying “SIEM: green” has no operational decision linkage.

**EX002 — Falsifiable supervised rehearsal.** Define a permission-gated nonproduction change to S41, a known unrelated S40 event, the intended query predicate (exact slot plus stable request ID), expected producer UTC time, *start at actual test event*, twenty-minute maximum until a verified matching source receipt, and a separate observed query return. An approved test procedure is not its execution; the reviewer records both. Reject if S41 is absent, S40 is wrongly included, the ID is missing, the clock cannot be interpreted or the collection is late. The original C1 fixture's “yes” does not satisfy these conditions, and C1X's PASS_DECLARED_FIXTURE is only a consistency check. This prevents using a toy result to justify a real CTN collection.

**EX003 — Missing authority is an explicit finding.** The identity custodian may have delegated evidence-export rights but the identity owner separately decides about session/account restrictions under the applicable plan. With the alternate and service-owner fallback unlisted, the correct cells are *unknown/await approved escalation*, not invented names. The incident lead can record contact attempts and seek organizational authorization; the analyst may not create an emergency power. An outcome that names a responsible role but leaves the authorization source undefined is **incomplete**, not approved.

**EX004 — What “24 hours” cannot mean without proof.** A source-event retention period requires source configuration and event-time semantics. A collector query horizon requires index settings and a representative filter/ingestion check. An export queue lifetime requires request/creation and expiration receipts. These mechanisms lead to different safe collection windows; C01 supplies none. Prepare a bounded source question rather than calculating “C01 at 08:40 means expiry tomorrow at 08:40.” If an edge-of-window rehearsal is proposed, obtain consent for its **nondestructive** method; never try deleting relevant incident material to prove protection.

**EX005 — Model 108-word handoff.** “At 08:40 UTC the CTN readiness worksheet identifies enrollment dependencies but not an after-hours identity alternate or a service-owner fallback. Its twenty-four-hour API audit claim has no verified source or clock anchor. I recommend two supervisor-approved rehearsals: first, use a harmless S41 scheduled change and unrelated S40 control to verify request-ID coverage and retrieval within twenty minutes; second, verify an authorized identity-custodian path when the primary is unavailable. The application owner should document manual-write audit coverage, and the recovery lead should propose an isolated restore acceptance test. All tests and approvals remain pending. C01 contains no evidence of a live incident or compromise.” Assess the stated owner, two measurable gaps, absence of invented outcomes and usable next shift action, not style alone.

**Chapter 01 focal review:** C1X program independently executed, exact four lines recorded; its negative controls are reasoned within their declared fixture. EX001–EX005 each retain a corresponding answer and the original assessment criteria. NIST primary pages cited near factual framing; all C01 evidence remains readiness-only. Existing [Chapter 1](../MANUSCRIPT.md#ch-01), [Chapter 2](../MANUSCRIPT.md#ch-02) and [index](../../SUBJECTS.md) anchors already occur in the manuscript/course index.

---

## Chapter 02 — Authority, scope and response roles

**Precise insertion:** After §2.11 “Handling the V2 ambiguous approval specimen” and before the original “Common mistakes and limits”. Retain the TRAIN-A01 code as the original state-lifecycle introduction; this addition develops enforceable action contracts and supervised proof of authorization.

### 2.E1 Three permissions, three different forms of evidence

When C02 reaches the CTN support desk at 09:04, the visible fact is a **reported S42 availability problem**, not a security compromise. The cloud colleague's proposed account disablement is a question. The practitioner should distinguish three kinds of permission.

*Permission to look* concerns read-only case collection. It may still expose staff identifiers, sensitive tenant events or unrelated enrollment data, so the source custodian and relevant data owner must authorize exact source, selectors, access method and retention. *Permission to interrupt* concerns an operation changing a session, account, API route or service. It requires the owner of the affected function to accept disruption and the identity/change owner to authorize the precise effect. *Permission to publish* concerns an audience and a message; it does not follow from either technical permission. A colleague who can read a console does not thereby gain all three.

Each action therefore has its own **authorization envelope**: the case and purpose, source of the trigger, named operation, smallest target and environment, start/end or lease semantics, approving role and valid delegation, executing role, service impact accepted, safeguards to preserve, success and failure observations, rollback owner, and next review. This is not a ceremonial form. If an operator discovers the cloud interface lacks session-level scope and offers account-wide disablement instead, the envelope has changed: the operator should stop and obtain a *new* authorized decision. The old decision cannot be stretched.

The [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integration of incident response with organizational risk management supports this separation of analysis and business decisions. It does **not** confer statutory authority or prescribe CTN's fictional signatories.

### 2.E2 A decision's lifecycle is not its control's lifecycle

A proposed restriction and an executed restriction are different artifacts. A useful professional case record keeps two ledgers:

| Decision ledger | Technical/change ledger |
|---|---|
| Proposal ID, version, author, evidence cutoff | Operator receipt ID, method, actual target |
| Required owners and their decision scope | Actual UTC execution time and result |
| Approved conditions, limits and expiration | Pre/post configuration and service observations |
| Denial or approval timestamp, if actually received | Route-specific positive and negative checks |
| Risk owner and review trigger | Residual risks, release/rollback receipt |

A signed request with no operator event must remain **approved, not executed**. An operator's success message without a reliable state or audit observation is **reported executed, effect unverified**. A narrow test showing a session rejected on one route is not proof that every token, account or integration was restricted. A refused approval also needs its own record; do not erase the proposal simply because the decision was “no.”

**Contrastive example:** At 09:04, “We recommend disabling svc-enroll because S42 might be unavailable; service owner not contacted; no action taken” is a weak technical remedy but an honest action-state record. “svc-enroll contained” would falsely assert both the actor/cause and operation. A stronger proposal asks for an authorized S42 state check, names the source and minimal fields, preserves the unresolved owner route in C01, and gives the incident lead a review trigger. The improvement is in controllability and evidentiary discipline, not in dramatic language.

In a supervised response, *time pressure changes escalation priority, not the logical meaning of a receipt*. An urgent decision might require the organization's documented emergency procedure; that procedure must still name what is authorized and how it is reviewed. “Emergency” alone cannot be treated as a wildcard on an account, scope or personal data.

### 2.E3 Design a rollback before deciding to risk service continuity

A rollback is not simply the inverse string of a command. Revoking a session can require a verified new login rather than un-revoking the original session; disabling a shared account may break an automation secret, integration queue or recovery job. Returning an earlier configuration can also reintroduce the same risk the intervention was meant to reduce.

At approval time, record a *measurable protective goal* (for instance, the named session cannot perform further prohibited work) separately from *permitted service goals* (staff can use approved alternative workflows; confirmed enrollment requests remain consistent). Define a trigger for intervention failure, a trigger for unacceptable business harm, a new owner decision required for reversal, and the records to preserve before changes. The controlling service owner accepts the potential business loss; the source/identity custodian defines permitted evidence handling and technology scope; the operator has no power to rewrite these decisions.

At C02 the action is still only under consideration: no target session has been supplied, so no test can yet prove a session-specific outcome. A practitioner can still prepare the *shape* of the verification: one request-linked negative test against the prohibited operation, a positive test of legitimate access, independent source/clock metadata, and a rollback checkpoint. This is preparation for Chapter 6, not a result available at 09:04.

### 2.E4 A miniature authority-validation lab

**Classification:** Entirely synthetic offline fixture C2X. Its positive flag is invented, not a signed decision, an account operation or a CTN source card. Python 3 standard library, read-only in memory, no environment access. The approval is bound to **one** named operation, environment and target.

~~~python
REQUEST = {"target": "S42", "action": "read_export", "environment": "training"}

def decide(card):
    if card.get("target") != REQUEST["target"] or card.get("action") != REQUEST["action"]:
        return "HOLD_SCOPE_MISMATCH"
    if card.get("environment") != REQUEST["environment"]:
        return "HOLD_ENVIRONMENT"
    if not card.get("approved_by_owner"):
        return "HOLD_APPROVAL"
    if not card.get("operator_receipt"):
        return "APPROVED_NOT_EXECUTED"
    if not card.get("independent_check"):
        return "REPORTED_NOT_VERIFIED"
    return "FIXTURE_GATES_DECLARED_NOT_AUTHENTICATED"

cases = [
    ("correct_scope_no_approval", {"target":"S42","action":"read_export","environment":"training","approved_by_owner":False}),
    ("wrong_action", {"target":"S42","action":"disable_account","environment":"training","approved_by_owner":True}),
    ("approval_only", {"target":"S42","action":"read_export","environment":"training","approved_by_owner":True}),
    ("operator_report_only", {"target":"S42","action":"read_export","environment":"training","approved_by_owner":True,"operator_receipt":"sim-1"}),
    ("all_flags", {"target":"S42","action":"read_export","environment":"training","approved_by_owner":True,"operator_receipt":"sim-1","independent_check":"declared"}),
]
for label, card in cases:
    print(label + ": " + decide(card))
~~~

**Executed output:**

~~~text
correct_scope_no_approval: HOLD_APPROVAL
wrong_action: HOLD_SCOPE_MISMATCH
approval_only: APPROVED_NOT_EXECUTED
operator_report_only: REPORTED_NOT_VERIFIED
all_flags: FIXTURE_GATES_DECLARED_NOT_AUTHENTICATED
~~~

The **wrong-action adversarial control** is especially important: an approval for a narrow read-only S42 export cannot be recycled to disable the account. The final “pass” does not authenticate the owner or source. A production process must validate the owner identity, delegation, approved request digest/target, applicable rules, independent receipt and actual effect. These invented strings are not sufficient security controls.

**Learner task:** For every line, name the first blocking evidence; then replace “training” with “production” in the last card and predict HOLD_ENVIRONMENT. Write a two-sentence supervisor request for the narrowly authorized read-only S42 question. Keep an alternative, broader account action separately proposed and unapproved. **Five points:** correct five classifications, with one point reserved for explaining why a copied favorable flag cannot authenticate approval (score each classification within the other four points). The output is reasoning on simulated fields only.

### 2.E5 Decision meeting and independent handoff

A useful exercise role-play has three rounds. First the analyst writes a C02-only decision note: symptom, alternative benign explanations, required service owner and proposed state check. Next a supervisor challenges the proposed account disablement: which exact new evidence would raise expected harm enough to reconsider it, which dependency could be interrupted, and what legitimate function must be preserved? Finally an independent recorder writes the current action state, making missing owner contact and absent execution receipts explicit. The second participant should be able to identify, **without asking the author**, which source request may be submitted and which disruptive option remains blocked.

A supervisor should reject “approve all controls necessary” even if the analyst is well intentioned. Such language cannot be audited for target, duration, business cost or rollback. An acceptable decision says “approved to prepare a request,” “authorized to retrieve this selected interval,” or “approved this identified control until this time with these safeguards,” followed by a separate operator/effect record as applicable.

**Chapter synthesis:** C02 justifies case intake, a bounded decision question and escalation. It does not justify an account-wide restriction. Later identity and endpoint cards can strengthen or weaken the action rationale, but they cannot retroactively fill a missing 09:04 approval. Chapter 3 adds those signals; Chapter 2 contributes the authority test through which any resulting proposal must pass.

**Continue studying — professional Chapter 02 of 12:** [← Chapter 01](../MANUSCRIPT.md#ch-01) · [Chapter index](../../SUBJECTS.md) · [Chapter 03 →](../MANUSCRIPT.md#ch-03).

### Worked-answer expansion — EX006–EX010

**Integration:** Append after the original subject 2 answer block. These are additive reasoning, not new exercises; retain the original 0–2 rubrics.

**EX006 — Why the five rights differ.** Case opening is a recorder/incident-lead activity, not a disruptive system change. Identity export is a restricted source request requiring custodian/data-owner permission. A single session revocation requires an actual target plus identity and service owner acceptance; account-wide disablement adds emergency change authority because shared enrollment work may stop. A learner notification is a separate communications/privacy decision. For each row name recommender, approving role, operator, artifact and **unavailable alternate from C01**; do not give the analyst delegated permission by assumption.

**EX007 — Versioned proposed action.** Record `CTN-IR-014 / A-01 / v1`, evidence C02 at 09:04, proposed first step a service-owner-confirmed read-only S42 state question, and conditional later account restriction whose trigger is **not yet observed**. State target and training/production distinction, legitimate enrollment cost, missing approval, missing operator, prohibited premature execution, and next check. A strong answer labels approval/collection/execution **pending** rather than inventing a 09:04 receipt. If cloud operations offers a broader operation than requested, resubmit the envelope; do not treat a shared verb as equivalent authority.

**EX008 — Alternative decision calculation.** Option A sacrifices a short analyst interval but improves service-truth evidence without service shutdown. Option B may affect one future named session, but C02 lacks its identifier and causal relevance. Option C affects all shared-account enrollment paths and carries the largest unknown blast radius. The correct choice can be provisional A while explicitly naming what **new** source and event would justify a different option. State separate protective and legitimate-service tests for B/C; a dashboard result alone is insufficient.

**EX009 — Why V2 fails.** “OK to act” lacks object, environment, allowed operation, service effect accepted, time bounds, operator, verification, rollback and authoritative delegation. The request for clarification must identify those fields *and* preserve the original message as an ambiguous version. Correct case state is **clarification requested; disruptive action not approved or executed**. C2X can return a favorable fixture label with invented flags; neither fixture proves the sender's authorization.

**EX010 — Decision record at the correct time.** Four lines: (1) observed C02 receipt 09:04 and estimated symptom noticed 09:00; (2) current S42 state/cause unknown, no justified compromise finding; (3) case opened, limited state/owner questions proposed, no approved export/account change; (4) review when a permitted authoritative state response, corroborating event or verified evidence-loss warning arrives. A later C03 sign-in is forbidden at this checkpoint even though its event time is earlier. A concise source-linked four-line answer is preferable to a long confident story unsupported by C02.

**Chapter 02 focal review:** C2X executed with five printed classifications; its negative action and environment controls respect the original TRAIN-A01 lifecycle without upgrading toy flags to real authorization. EX006–EX010 retain the original IDs and answer pairs. No C03–C08 data were imported into the 09:04 decision. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) primary publication page verified; CTN authority remains explicitly fictional.
