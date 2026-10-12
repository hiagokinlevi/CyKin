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

---

## Chapter 03 — Alert intake and severity assessment

**Precise insertion:** After §3.5's original clock-normalization lab and before “Common mistakes and limits”. Retain C03–C08, their exact release times, the original four-line C3 result and EX011–EX015 unchanged. The new material teaches *repeatable intake, revision of priority under changing evidence and coverage-aware negative findings*.

### 3.E1 Intake is a provenance-preserving normalization, not a merger

At 09:04 the support desk has C02: a reporter says S42 looked unavailable, first noticed *around* 09:00. At 09:09 the case additionally receives C03's successful IdP sign-in for `svc-enroll` with `s-77` (event 08:58, ingested 09:02), C04's browser observation on `runner-03` (raw 08:54, four-minute slow clock, ingested 09:06), and C05's S42 edit record with request `q-144` (event 09:01, ingested 09:07, blank session field). Those four producers answer **different questions**. A support complaint is evidence a complaint was made; a successful authentication label is not human attribution; a browser process is not a validated session; an API edit is not proof of the current slot state.

The correct intake product uses one **case envelope** and distinct **source objects**. A case envelope contains ID, observed service, reporter channel, opened time, decision owner and review trigger. A source object contains immutable card ID, original event string, stated zone/offset, producer identity, ingestion/receipt time, release time, specific fields, known gaps, and authorization/copy status. Derived interpretations go into another column, not into a rewritten “normalized raw event.” This is analogous to logging and forensic provenance concepts discussed in the dated [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) and [SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final); neither prescribes this artificial CTN schema.

**A misleading timeline:** `08:54 runner browser → 08:58 login → 09:01 edit → 09:04 report` implicitly treats 08:54 as correct UTC and invites a causal narrative. **A corrected source-aware comparison:** C04's *estimated* normalized time is 08:58, coinciding with C03 at minute precision; C05 is reported at 09:01; C02's symptom time is approximate and may precede or follow an unknown source-state transition. C04 has no session key, C05 has no session key, and no card directly links `s-77` to `q-144`. Time overlap is a request for a discriminator, not a proof of identity.

### 3.E2 Four clocks are necessary, but not sufficient

Record the producer event time, collector ingestion time, analyst discovery/review time and learner release time as different columns. The C04 raw clock was measured four minutes slow in the scenario, so `08:54 + 00:04 = 08:58 UTC`. Keep both representations. A real offset measurement has error bars; a single fixed teaching offset does not establish exact seconds or event ordering within the minute. If ingestion lag is present, a query over event time performed before all relevant records arrived can appear quiet and later return additional events. The trainee must ask for the **query run time, ingestion cutoff, filters, source and expected delay** before interpreting absence.

For this curriculum, release time is a separate **pedagogical control**: C06's calendar entry is timestamped 08:50 but not released until 09:10, so it cannot justify a 09:09 decision. C08's expiry at 10:00 is reported at 09:14; an analyst at 09:09 cannot cite that statement, even though it later makes evidence-preservation work urgent. This distinction also prevents backdating a severity label: the record should state *09:09 provisional assessment*, followed by *09:14 reassessment* once new evidence is actually released.

### 3.E3 Severity is a decision contract with triggers, not a compromise probability

The book's P1/P2/P3 rubric is a **local classroom ranking**, not the NIST score of CTN's compromise probability. Assign separate categories:

| Question | At 09:09 | At 09:14 |
|---|---|---|
| Service impact | S42 allegedly unavailable; no approved authoritative comparison | Same unresolved state; complaint plus recorded edit still do not count affected learners |
| Causal confidence | C03/C04 temporal lead and C05 account label, no common session-request key | C06's visible work list covers S40/S41, not S42; C07 says account is shared |
| Time sensitivity | Relevant records may need authorized review; retention deadline **not supplied at this release** | C08 custodian *reports* detailed IdP source expiry at 10:00 |
| Decision cost | Account-wide disablement could disrupt enrollment; no approved operational control | Preservation request urgent while business harm of broad restriction remains unresolved |
| Review trigger | Ask service/application custodian for S42 current state and named source bounds | Request approved IdP detail now; revisit by a selected checkpoint before 10:00 or on new verified state |

At 09:14, P2 provisional is defensible for the combination of plausible enrollment harm and a reported evidence-expiry condition. It is not a statement that a human compromised the account. P1 requires evidence fitting the actual defined high-impact classroom threshold; P3 might be defended only with a documented reason the urgency/impact has changed. If a proposed query has no valid authorization, record a blocked request and escalate to the proper owner rather than silently conducting it.

### 3.E4 Design an intake falsifier for each competing explanation

A triage analyst can proceed without knowing the cause if every hypothesis has a test that could weaken it. Three candidate explanations must be kept distinct.

**H1 — normal scheduled automation or an incomplete change calendar.** The browser on runner-03 is compatible with ordinary job work and C07 later confirms `svc-enroll` has a scheduled use, but neither validates this specific S42 edit. Request a signed, versioned S42 authorization and a job-run record with request-ID semantics. A complete authorized job manifest that excludes `q-144` would weaken the “normal approved run caused the edit” explanation; absence from an incomplete manifest would not.

**H2 — use of a shared account outside approval.** The C05 account label and C06 omitted S42 task support concern, while shared account usage and a blank session field leave human and mechanism unknown. Request scoped IdP/session records and application-side schema clarification through distinct custodians. A validated non-session application path would weaken an assertion that `s-77` was necessary; it would not independently establish the correct cause.

**H3 — display-state divergence.** C02 may reflect a cached or stale view rather than the current authoritative slot. Compare an approved source-of-truth S42 value/version with an uncached synthetic view, recording when each was read. If the authoritative state is wrong, a *purely display-only* explanation is insufficient; if authoritative state and displayed view differ, the discrepancy deserves its own technical diagnosis. No such comparison is supplied by C02–C08.

These explanations may overlap. An authorized job can produce incorrect state; a genuine edit can coexist with a stale browser cache. The triage record should not pretend that exactly one story must win.

### 3.E5 Offline lab C3X — enforce release before using a timestamp

**Environment:** Isolated Python 3 standard library, in memory, no logs or systems contacted. This is a *release-filter rehearsal* using copied chapter metadata; it is not a new C-series record or an actual investigation query. The function reads the first element of each tuple as **release time**, not source event time.

~~~python
CARDS = {
    "C03": ("09:09", "08:58", "09:02"),
    "C04": ("09:09", "08:54", "09:06"),
    "C05": ("09:09", "09:01", "09:07"),
    "C06": ("09:10", "08:50", None),
    "C07": ("09:12", "09:12", None),
    "C08": ("09:14", "09:14", None),
}
def minute(clock):
    h, m = map(int, clock.split(":"))
    return h * 60 + m
def available(card, decision):
    return minute(CARDS[card][0]) <= minute(decision)

for decision in ("09:09", "09:10", "09:14"):
    print(decision, ",".join(k for k in CARDS if available(k, decision)))
print("early_C08:", "REJECT_FUTURE" if not available("C08", "09:09") else "ALLOW")
print("early_C06:", "REJECT_FUTURE" if not available("C06", "09:09") else "ALLOW")
~~~

**Executed output (five lines):**

~~~text
09:09 C03,C04,C05
09:10 C03,C04,C05,C06
09:14 C03,C04,C05,C06,C07,C08
early_C08: REJECT_FUTURE
early_C06: REJECT_FUTURE
~~~

**Adversarial test:** Replace C06's release time `09:10` with its earlier source event time `08:50` in a separate variant. The filter would incorrectly admit C06 at 09:09. The error is **semantic**, not a parser failure: release time is a pedagogical evidence boundary. Retain the original dictionary for the graded transcript.

The classifier does not authenticate clock fields, validate source collection, reconcile a device's time skew or tell the analyst which hypothesis is true. To pass, the learner must write the real boundary statement: “At 09:09 only C03–C05 from this set are released; C02 already exists from the prior chapter; neither C06 nor C08 can justify this checkpoint.” **Five-point local rubric:** three release lines correct, both future-control lines correct, plus a separate mandatory note that a positive classification is not proof of compromise. Explain the meaning of the `None` ingestion fields; they are *not supplied*, not zero delay.

### 3.E6 A reproducible decision-ready intake artifact

The handoff should be usable even if no new evidence arrives. Recommended fields: case/time; source observations with IDs and collector times; impact expressed as reported or verified; provisional priority and distinct confidence; available/withheld cards; pending authorizations; bounded next requests and accepting custodians; review event; prohibited inference; record author and revision. The analyst may write “no additional matching event **in the supplied table under this exact rule**,” but cannot infer “no other edit occurred” while source coverage, filtering or ingestion is unknown.

At the C08 release, record the reported 10:00 expiry as a **custodian claim** requiring timely confirmation and action by the proper owner. It is more urgent than perfect attribution, but does not justify a full tenant export. Chapter 4 will turn that preservation request into a separate case receipt and test the difference between a received export and verified bytes.

**Chapter synthesis:** Triage establishes *what to investigate next and by when*, not who did it. The clock correction C04=08:58 is valid for the stated toy input, but joining that event to C03/C05 requires more than time. Retain P2 at 09:14 as provisional and source-bounded. The next chapter handles receipt, custody and integrity, not cause attribution.

**Continue studying — professional Chapter 03 of 12:** [← Chapter 02](../MANUSCRIPT.md#ch-02) · [Chapter index](../../SUBJECTS.md) · [Chapter 04 →](../MANUSCRIPT.md#ch-04).

### Worked-answer expansion — EX011–EX015

**Integration:** Append after original subject 3's C3 model results. Preserve exercise IDs and 0–2 rubrics.

**EX011 — Four independent intake lines.** C02 remains a reporter-observed symptom, noticed approximately 09:00 and received 09:04. C03 source sign-in 08:58, ingested 09:02, released 09:09, account/session label without human/client. C04 raw 08:54 corrected to *estimated* 08:58, ingested 09:06 and released 09:09, endpoint process without a shared key. C05 API edit 09:01, ingested 09:07, released 09:09, request `q-144`, session missing. Each line identifies a custodian and one safe next query; a joined “runner session edited S42” observation is false.

**EX012 — Clock arithmetic and causality.** For C04 measured four minutes slow, normalized UTC = 08:54 + 00:04 = **08:58**. The equality with C03 holds only at the presented minute precision. There is no evidence of exact order, identity or session/request linkage. In the original C3 lab, reversing the sign gives 08:50; C3X separately shows why an older event timestamp cannot waive the release gate. Neither mutation changes canonical C04.

**EX013 — Provisional P2 decision.** Reported S42 service concern plus C05 recorded edit implies plausible but unmeasured impact; shared `svc-enroll`, no cross-source join and incomplete calendar limit attribution. C08's 10:00 expiry, released at 09:14, raises *preservation urgency*, not proven compromise. Name an owner-approved IdP 08:50–09:05 request and separate read-only S42 state check, with reassessment before 10:00 or on verified new damage. A P1 label without its defined high-impact evidence fails the rationale.

**EX014 — Closure must have evidence.** Benign candidates: ordinary runner process and an omitted approved addendum; concerning candidate: use of shared account outside scope. For each, specify what would falsify the explanation—a verified job-to-request link, signed change scope, and trustworthy session/application identifier semantics as appropriate. Current C04/C06/C07 do not supply these discriminators, so the learner's result remains hypotheses, not “false positive” or “attacker confirmed.”

**EX015 — Handoff (119 words).** “At 09:14, CTN-IR-014 is P2 provisional. Support reports S42 unavailable, and C05 records an S42 edit via q-144. C03 describes an svc-enroll sign-in with s-77; C04's runner browser time corrects to approximately 08:58, but no direct join identifies an operator or cause. C06 lists approved work on S40–S41 and does not show an S42 addendum. C08 reports IdP detail expiry at 10:00, so please authorize the identity custodian to preserve a narrow 08:50–09:05 source selection and provenance. In parallel ask the application owner to compare current authoritative S42 state. C01 lacks an after-hours identity alternate. Neither export nor restriction has occurred. Reassess before expiry or immediately on verified new harm.”

**Chapter 03 focal review:** C3X lab independently reproduced with exactly five lines; future-evidence controls reject C06/C08 at 09:09. EX011–EX015 match the four-line intake, corrected timestamp, P2 matrix, falsifiers and 90–150-word escalation request. Official [SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and dated [SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) pages checked; no invented source ingestion or operational action.

---

## Chapter 04 — Evidence preservation and case records

**Precise insertion:** After existing §4.10 “Make a preservation queue based on reversible loss and decision value” and before the original “Common mistakes and limits”. Leave the original C09/C10 source cards, V4 hash exercise and EX016–EX020 in place. This addition deepens the distinction among **source, approved collection, copied bytes, verified integrity and inferential use**.

### 4.E1 Five objects in an evidence workflow

Incident records are often described as a “chain of custody,” but that phrase is too easily reduced to recording a checksum. The supervised practitioner should separate at least five identifiable objects.

1. **Producer record set.** The events still held by an application, identity service or storage system, under its actual retention and deletion semantics. A custodian may be able to query a subset without showing that all expected events were generated.
2. **Selection and authorization.** A case-specific decision naming the permitted producer, account/object selectors, event interval, sensitive fields, collecting role and purpose. An approved plan does not automatically stop source deletion or deliver any bytes.
3. **Collection event.** An operator actually retrieves defined data, records method, query, source, creation/retrieval time, object identity and destination, and reports omissions or errors.
4. **Preserved copy and check.** Identified bytes are kept under appropriate restricted access, with a digest computed and compared as defined. Equality supports consistency of the *checked bytes* under its trust assumptions; it cannot establish truth or completeness of the producer.
5. **Analytical derivative.** A projected CSV, redacted screenshot, normalized timeline or chart derived from preserved records. It needs source pointers, selection/transformation method and a separate copy identity; it is not the original source simply because it looks clean.

The workflow has different failure conditions. A preservation **request** may be correctly scoped but never acknowledged. A collector may report success while the export lacks source metadata. A hash may match despite omission of relevant rows in the query. A screenshot may show an accurate image of a cached page but not the authoritative slot state. An analyst who collapses these distinct states into “evidence collected and verified” makes later independent review impossible.

The [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) guide discusses forensic techniques and source-sensitive acquisition in response, while [SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) addresses log-management concerns. Both publications date from 2006. Their concepts support asking about provenance and records but do not determine CTN's specific legal duties, cloud retention implementation or real collection privileges. The method below is an original teaching contract, not legal evidence-handling advice.

### 4.E2 What the C09 and C10 cards really establish

At 09:14, C08 reports that detailed identity events in the relevant synthetic window expire at 10:00. The analyst can **request** a narrow `svc-enroll` 08:50–09:05 UTC collection from the identity custodian. At 09:16, C09 subsequently supplies a reported approval; at 09:18 it supplies a case-copy receipt describing two events at 08:58/08:59. The material is richer than the earlier summary, but object identity, byte count and digest are not supplied. A conscientious record says: **copy received according to case card; source completeness unknown; byte-integrity comparison not possible with the supplied fields**. It does not retroactively mark the 09:14 request “received.”

C10 is a different source: a support screenshot displaying “11:21 UTC+02:00,” received at 09:22. Subtracting two hours yields a **conditional displayed UTC value of 09:21**. The arithmetic does not authenticate the screenshot's capture-device clock, timezone-label correctness, page cache freshness or current authoritative S42 state. Keep the raw display string, claimed offset, conversion, receipt time and confidence in the time source in different columns. If the screenshot shows “unavailable,” that is evidence that an image displayed the symptom under its asserted capture conditions—not that the backend was unavailable at 09:21.

The original V4 byte string is a **separate laboratory artifact**, with its published 34-byte length and SHA-256. It cannot be repurposed as C09's missing digest. A training participant may compute the correct V4 checksum and still have absolutely no basis for saying the C09 export was complete or unmodified. The byte layer and source-provenance layer are different evidence classes.

### 4.E3 A source-hold request cannot be substituted for a retained case copy

Suppose the identity custodian can preserve records at their original source but cannot yet release a selected export. That may reduce immediate loss risk, but the investigator still lacks a case copy and cannot report an integrity check. Conversely, a one-time copy may be retained while the producer continues deleting source rows under its ordinary policy. The case therefore needs two separate ledgers: **source-preservation control** and **collected-item custody**. Do not infer the first from the second.

A hold ledger should name the exact source namespace and objects/interval, approved decision, reported mechanism, effective/expiry or review terms, application receipt, non-destructive effect observation, and current residual limitations. A copy ledger should name the item/source, collection authority, actual time, selector, transfer, byte count, digest/check, restricted destination and handling history. A positive digest is not a hold-effect receipt. If a source never supported a hold, state that limitation and seek an authorized alternative rather than inventing a feature.

The strongest next request concerning C09 is therefore **narrow**, not “send all IdP records”: obtain the particular source object identifier, query envelope including interval semantics, collector details, byte-count/digest record if they exist and any source-health limitation. If an item is unavailable, document the unanswered field. C08's 10:00 source-expiry claim changes scheduling urgency; it does not authorize the analyst to bypass restricted access.

### 4.E4 Construct a reviewable collection manifest

For a supervised, authorized collection, an independent reviewer should be able to reconstruct the following chain:

| Question | Evidence to seek | Failure if omitted |
|---|---|---|
| Why collect? | Case question, affected service, minimization rationale | Retain unrelated personal records without decision value |
| From where? | Source namespace, collection identity, version and storage tier | Mistake an aggregate dashboard for detailed producer logs |
| What exactly? | Query filter, account/slot, event time window, field semantics, inclusive/exclusive endpoints | Treat an empty partial query as complete event absence |
| With whose permission? | Actual decision owner, scope, permitted operator, valid time | Assume ability to use an interface grants approval |
| When was it collected? | Source event, ingestion, request, copy creation and receipt times, each identified | Order events by convenient file timestamps |
| What bytes? | Copy identifier, byte count, digest algorithm/value and actual verification action | Assert authenticity from an unexamined digest claim |
| Who could inspect it? | Restricted location, receiving role, access/transfer history | Spread raw identity/patron data to unnecessary recipients |
| How was it transformed? | Versioned field projection, redaction, normalization and source pointers | Present a derivative as original or erase omitted context |

A manifest with missing fields is not automatically dishonest; it is **incomplete for the claims those fields would support**. That is a useful result. The custodian may supplement it later, maintaining original timestamps and versions. The learner should never backfill today's digest into a historical receipt as if it were recorded at the time.

### 4.E5 Controlled contrast: byte integrity, source authenticity and data meaning

Take three hypothetical submissions. In **A**, a known local file has two matching SHA-256 checks but no originating source or approved selection: byte consistency is supported, source authenticity and completeness remain unknown. In **B**, a log export has a detailed query manifest and custodian signature, but its stored bytes no longer match the recorded digest: do not rely on the disputed copy until the discrepancy is investigated, even though the query metadata are plausible. In **C**, both copy identity and bytes are checked, but the application field labelled `actor` contains a shared automation account: producer provenance may be stronger, yet human attribution remains unproved.

These are different axes. There is no “overall evidence verified” state that follows from any one positive check. A reviewer should score each axis and name the next bounded question: source health/completeness, exact bytes and transfer, or identifier semantics. Neither a screenshot nor a copied text transcription can answer all three.

### 4.E6 Offline laboratory C4X — detect which preservation receipt is missing

**Environment:** Python 3 standard library, entirely in memory. The following tuples are invented *receipt-state illustrations* and **not C09/C10 replacements**. No source export or hashing occurs. The model deliberately refuses a claim of checked bytes when approval or a received item is absent.

~~~python
from datetime import datetime, timedelta

def status(card):
    if not card["approved"]:
        return "REQUEST_ONLY"
    if card["received_at"] is None:
        return "APPROVED_NOT_RECEIVED"
    if card["object_id"] is None or card["digest"] is None:
        return "COPY_RECEIVED_INTEGRITY_UNVERIFIED"
    if card["checked"] is not True:
        return "DIGEST_RECORDED_NOT_CHECKED"
    return "COPY_BYTES_CHECKED_SOURCE_COMPLETENESS_UNKNOWN"

cases = [
    ("REQUEST", False, None, None, None, None),
    ("APPROVAL", True, None, None, None, None),
    ("CTN_C09_LIMIT", True, "09:18", None, None, None),
    ("UNRECHECKED", True, "09:18", "toy-1", "sha256:toy", False),
    ("CHECKED_FIXTURE", True, "09:18", "toy-1", "sha256:toy", True),
]
for name, approved, received_at, object_id, digest, checked in cases:
    print(name, status(dict(approved=approved, received_at=received_at,
                            object_id=object_id, digest=digest, checked=checked)))
raw = datetime(2026, 10, 12, 11, 21)
print("C10_UTC_CONDITIONAL", (raw - timedelta(hours=2)).strftime("%H:%M"))
~~~

**Executed output:**

~~~text
REQUEST REQUEST_ONLY
APPROVAL APPROVED_NOT_RECEIVED
CTN_C09_LIMIT COPY_RECEIVED_INTEGRITY_UNVERIFIED
UNRECHECKED DIGEST_RECORDED_NOT_CHECKED
CHECKED_FIXTURE COPY_BYTES_CHECKED_SOURCE_COMPLETENESS_UNKNOWN
C10_UTC_CONDITIONAL 09:21
~~~

The fifth scenario uses **invented `sha256:toy` text**, not an actual digest or verified byte sequence. Its flag tests only how to label a declaration; it does not authenticate a sample. **Adversarial control:** set `checked=True` while removing the digest; the result remains COPY_RECEIVED_INTEGRITY_UNVERIFIED. Set `approved=False` on a purported received copy; the first gate says REQUEST_ONLY, demonstrating that the tuple is **inconsistent** rather than evidence of valid authority. An actual receipt system should flag contradictory states explicitly instead of treating this toy gate as comprehensive.

**Required learner artifacts:** Six output lines; one missing-evidence table for C09 and C10; a source-versus-copy ledger; a least-privilege two-request preservation queue; one sentence explaining why the C10 normalized time is conditional. **Rubric, six local points:** exact transcript (two), proper C09 status and V4 separation (one), C10 clock/cache limit (one), bounded custodian/approval/provenance requests (one), and safe negative-control explanation (one). No real contact or collection is part of the exercise.

### 4.E7 Build the Chapter 5 handoff from retained gaps

A professional handoff should identify *what is missing in a way that changes the next investigation*. For C09, unresolved source-object ID and digest affect confidence in the retained export's provenance and integrity. For C10, unknown capture clock/cache affect conclusions about the apparent time and service state. The C03/C09 session field might suggest an identity relationship; C05's blank application session still prevents a direct link from `s-77` to `q-144`. These are three different gaps with three different custodians/tests. A single sentence “more evidence needed” does not instruct the next analyst.

Do not discard the raw C10 display once it has been normalized; retain both times and the conversion method. Do not modify C09 to add a byte count not supplied. When the Chapter 5 investigation starts, source pointers should survive exactly as recorded, while competing hypotheses and derived timelines may change with each new card.

**Chapter synthesis:** The evidence workflow is not completed by approval, file existence or a hash alone. C09 supplies a reported received copy but lacks key provenance/integrity fields; C10 is a limited screenshot observation. Both are useful if their uncertainties remain visible. Chapter 5 will compare their clues against other source records without converting a missing session join into proof.

**Continue studying — professional Chapter 04 of 12:** [← Chapter 03](../MANUSCRIPT.md#ch-03) · [Chapter index](../../SUBJECTS.md) · [Chapter 05 →](../MANUSCRIPT.md#ch-05).

### Worked-answer expansion — EX016–EX020

**Integration:** Append immediately after original subject 4 C4 worked laboratory output. Preserve the original exercise questions, exact V4 digest and 0–2 rubrics.

**EX016 — Proposed collection request.** At 09:14 C08 supports urgency to ask the identity custodian for a narrowly scoped 08:50–09:05 `svc-enroll` IdP detail source, preserving original timestamps, session/client fields, event IDs, producer/copy metadata and an explicit restricted location. Identity/data-owner authorization and actual collector/time are **pending**, not complete. The purpose is a bounded source availability and correlation question, not “download the tenant.” An actual expiry at 10:00 is a custodian statement in C08, not a blanket data-access permission.

**EX017 — Two different receipt statuses.** C09 has a reported permission at 09:16 and case-copy receipt at 09:18 for events 08:58/08:59, but no supplied source object ID, byte count or digest; its integrity/completeness remain unverified. C10's display is 11:21 UTC+02:00, conditionally 09:21 UTC, with support receipt at 09:22, missing original capture clock/cache context. Do not make a single “09:18 verified evidence” entry for both. A receipt is evidence of receiving the claimed object, not proof of authoritative meaning.

**EX018 — V4 digest and its boundary.** The published V4 payload has **34 bytes**, with SHA-256 `1407e98f466990ff5aa4eee42cd30291826490e2c910ee57887824e6946136cc`. A second digest after a one-byte mutation differs despite equal byte length. This checks the chosen classroom strings only; nothing in the 34-byte fixture can authenticate C09's actual source export. Award the integrity point for reproducible bytes **and** a clear statement that source authority and coverage remain separate.

**EX019 — Conditional screenshot time.** 11:21 at an asserted UTC+02:00 offset corresponds to 09:21 UTC. C10 entered the case at 09:22, not at 09:21. Without evidence about capture-device clock accuracy, page freshness and source state, label the conversion conditional and the symptom a screenshot observation. No current backend S42 value is established by the picture.

**EX020 — Decision-oriented two-source queue.** Request the C09 producer/export metadata and actual bounded query/collection receipt from the identity custodian under the existing approval, before the reported 10:00 expiry when possible. Separately request an authorized read-only S42 current version/value and last-change reference from the application/service owner, with minimal fields. The first improves evidence availability/provenance; the second informs business impact. They can proceed in parallel if custodians and permissions permit, but neither result was supplied at 09:22. Preserve those distinct questions instead of broadening the export.

**Chapter 04 focal review:** C4X reproduced six lines exactly, including conditional 09:21 calculation. Its receipt-state strings are declared fixtures, not authenticated records. EX016–EX020 still align with their source cards and original answers; V4's original checksum remains unchanged. [SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) and [SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) primary publication pages were consulted; no third-party passages reproduced.

---

## Chapter 05 — Investigation, hypotheses and timeline building

**Precise insertion:** After §5.10 “Compare false causal certainty with actionable uncertainty” and before the existing “Common mistakes and limits”. Keep C11's 09:24 statement, C12's 09:26 read-only view and all existing C5 source/answer IDs unchanged. This extension develops an investigative method a supervisor can review and hand to Chapter 6 without claiming a cause or human actor.

### 5.E1 A timeline is an argument with provenance, not an ordered story

A professional timeline should preserve **four dimensions per row**: original producer event time (and precision), a normalized comparison time with its transformation, the case's knowledge/receipt time, and the exact claim the record can support. If the source says *approximately* 09:00, its normalized comparison time is still approximate. If a device shows 08:54 on a clock declared four minutes slow, the classroom estimate is 08:58; a professional should retain the raw 08:54 and ask about the offset's uncertainty before treating the equality with the 08:58 IdP sign-in as an exact overlap.

The timeline's **scope** should be fixed before presenting it. At 09:22 C09 has been received and C10 shows a displayed unavailable slot, but neither C11 nor C12 exists in the learner's released state. A table assembled at 09:26 may use both later cards if marked as released at their actual times; a frozen 09:22 decision may not be silently rewritten with the new `batch-17` tag. An incident review should retain the earlier decision even when the hypothesis changes.

Consider the following useful time uncertainties. C02 says a symptom was noticed *around* 09:00, while C05 reports an S42 edit at 09:01. If both descriptions are reliable, the symptom could precede that edit. It may concern an earlier unrelated problem, a clock difference, caching, or imprecise recollection. The correct procedure is **not** to move the support time to 09:02 to make a fluent story. Record the tension; then ask for a new, authorized discriminator such as a front-end trace linked to the reported symptom. Investigation quality improves when contradictions remain visible.

At 09:26 a source-aware timeline can name C03 and C09's matching `s-77`, C09's claimed client `runner-03`, C04's independently observed runner browser, C05's application request `q-144`, and C12's self-reported `batch-17`. Its graph must not add `s-77 → q-144`: the application's session field is blank, and the job tag lacks proven producer semantics.

### 5.E2 An investigative graph needs different edge types

An investigation graph represents records as nodes and **typed, challengeable links** as edges. A source identifier shared within one producer can support a bounded equality statement if that producer's uniqueness/namespace contract is established. A label shared across two producers is weaker: the strings may use different namespaces, represent proxies or omit translation steps. A causal link is stronger still and needs a tested mechanism and matching operation context. Finally, a human-actor attribution needs independent evidence beyond an account, task or session label, especially when C07 explicitly says the account can be used by both automation and emergency operators.

A responsible graph therefore distinguishes:

| Edge type | Example in current case | What remains unproven |
|---|---|---|
| Source-value equality | C03 and C09 both supply `s-77` | C09 original-object completeness; person behind the account |
| Application-key equality | C05 and C12 both name `q-144` | The external origin of the request |
| Cross-source label similarity | C09 client `runner-03`, C04 device `runner-03` | Process-to-session identity and comparable field semantics |
| Missing direct relationship | C09 `s-77` to C05 `q-144` | Any validated session/request join |
| Claimed job provenance | C12 `batch-17` tag | That a real approved job emitted `q-144` |
| Authorized task scope | C06 lists S40 and S41; C11 suggests an addendum | Existence, effective time and scope of any S42 addendum |

This model is useful because *evidence can narrow a mechanism without identifying a person*. An approved scheduler run later found to emit `q-144` might support H1 for a technical path, but still would not establish who configured the task. The present checkpoint does **not** contain that validated run. Equally, C06's missing S42 in the visible calendar raises concern but does not prove that no separate approval was ever granted.

### 5.E3 Choose a discriminator that can fail, not a request for “everything”

A hypothesis becomes operational when the team names which result would strengthen it, which would weaken it, and what happens if the source is incomplete.

**H1: an automated job wrote the wrong slot.** Current leads: scheduled use of the shared account, runner-03 client field in C09 and C12's tag. Against it: no preserved, validated job run for `q-144`, and visible approval includes S40/S41 only. Request the minimal job-run record including source, run ID, request ID, actual slot selection, event time, code/task version and job approval. If a complete, authenticated run manifest for that interval excludes `q-144`, H1 as an explanation of *that request* weakens. If the manifest is partial, absence remains unknown.

**H2: the shared account was used outside the approved task scope.** Current leads: C05 S42 edit under `svc-enroll`, while C06 does not list S42. Alternative: C11 reports a possible addendum; emergency humans may share the account. Request the approved change ledger/version and bounded identity records, with documented field semantics. A valid S42 addendum plus coherent job/request path could weaken an unauthorized-use hypothesis but would not by itself establish that the current slot is correct. A denied collection does not automatically strengthen H2.

**H3: the displayed symptom differs from current backend state.** Current leads: C02 and C10 are observations of a report/image, neither an authoritative S42 read. Against a *pure display-only* theory: C05 records an actual application edit which H3 must explain or accommodate. Ask the service owner to approve an authoritative S42 value/version read and a separately observed uncached view, retaining timestamps. An incorrect authoritative value would prevent the analyst from closing the incident as solely a display issue; a matching correct backend and inconsistent displayed view could strengthen the display/caching branch for that time.

The strongest test is not necessarily the one most likely to confirm the analyst's favorite theory. It is the one that **changes a decision under the available authority and loss risk**. The service-owner S42 state check affects potential patron harm; the job-run/request-ID check affects the mechanism; the addendum affects authorization. Keep these questions separate even if a single custodian can coordinate them.

### 5.E4 How to handle negative evidence without overpromising

“No matching record” can mean different things. A scoped, healthy, known-complete query may support the absence of a particular recorded event **within its declared window**. A query with unspecified filters, delayed ingestion, unavailable historical records or a nonfunctional producer supports much less. If the cross-source identifier is missing entirely, no query on account label and time can manufacture it. A false claim that “no join means the sign-in and edit are unrelated” is as unwarranted as “the sign-in caused the edit.”

The collection quality of C09 matters even though its `s-77` row is informative: missing original-object ID, byte count and digest limit claims about the acquired copy's integrity; none of those gaps means its values must be false. Preserve uncertainty instead of substituting either trust or distrust as a certainty. Another responder may later obtain those missing receipts, validate the same bytes and change the confidence rating, while the original 09:26 record remains versioned.

At a supervised decision point, the analyst can record **confidence in the leading mechanism = unresolved**, **confidence that a producer reported S42 changed = supported within the supplied application record**, and **confidence that current backend state is incorrect = not measured**. Severity and intervention urgency can still be nonzero. Confidence must be attached to a *particular claim*, not to the entire case as if one percentage explained every dimension.

### 5.E5 Offline lab C5X — compare identifier equality with an absent join

**Environment:** Python 3 standard library, no files, requests, credentials or source modifications. The five edges are *invented representations* of the bounded source-card claims, and `C05-NEGATIVE` is an exercise-only adversarial control, **not another CTN case card**.

~~~python
edges = [
    ("C03-C09", "same_namespace", "s-77", "s-77"),
    ("C05-C12", "same_namespace", "q-144", "q-144"),
    ("C09-C05", "cross_namespace", "s-77", None),
    ("C09-C04", "cross_namespace", "runner-03", "runner-03"),
    ("C05-NEGATIVE", "same_namespace", "q-144", "q-999"),
]

def classify(edge):
    name, namespace, left, right = edge
    if left is None or right is None:
        return "UNKNOWN_MISSING_KEY"
    if left != right:
        return "UNMATCHED_VALUE_IN_TEST"
    return ("VALUE_EQUAL_SEMANTICS_UNVERIFIED"
            if namespace == "same_namespace"
            else "LABEL_EQUAL_NAMESPACE_UNVERIFIED")

for edge in edges:
    print(edge[0], classify(edge))
~~~

**Executed output (five lines):**

~~~text
C03-C09 VALUE_EQUAL_SEMANTICS_UNVERIFIED
C05-C12 VALUE_EQUAL_SEMANTICS_UNVERIFIED
C09-C05 UNKNOWN_MISSING_KEY
C09-C04 LABEL_EQUAL_NAMESPACE_UNVERIFIED
C05-NEGATIVE UNMATCHED_VALUE_IN_TEST
~~~

The result is **not causal proof**. Even when values match, the producer's key namespace and provenance require independent verification. The direct session-to-request edge remains unknown because no shared key is supplied. **Adversarial control:** replace the `None` in C09-C05 with `"s-77"`; the displayed status would change to LABEL_EQUAL_NAMESPACE_UNVERIFIED, **not** to confirmed causal join or actor attribution. Replacing the negative q-999 with q-144 changes only the equality status in that controlled fixture. Neither mutation changes C05 or C12 source facts.

**Required learner artifacts:** Five statuses, a three-hypothesis matrix, one graph distinguishing observed and unobserved edges, two least-privilege evidence requests, and a 09:26 handoff preserving current source gaps. **Five-point local scoring:** one for correct equalities, one for the missing link, one for cross-namespace ambiguity, one for the negative control and one for evidence requests that name owners and falsifiers. A learner who names a human attacker or reports `batch-17` as a validated run fails the evidence boundary.

### 5.E6 An operationally usable 09:26 supervisor handoff

At 09:26 the analyst's next decisions should be presented as *conditional*, rather than a recommendation to take immediate broad action. If a permitted authoritative S42 check later finds continuing wrong slot state or new harmful writes, the incident lead can ask the service/identity owners to compare Chapter 6 controls and their cost. If a verified `q-144` job-run and complete approved S42 scope later arrive, the team can review whether a downgrade is defensible. If the owner or source is unavailable, the record should say which claim is blocked and what preservation or escalation remains possible; it should not silently treat lack of evidence as safety.

A complete handoff has a **decision clock** in addition to an event clock. At 09:26 C11 and C12 are usable. A reviewer must not import Chapter 6's later C13–C19 scope, approvals, execution receipts or controls into the assessment. Nor should a person be named behind `svc-enroll`: this case has a shared identity and no validated actor-to-operation edge. The next chapter's function is to plan reversible, owner-approved protection options, not to reward certainty unsupported by this chapter.

**Chapter synthesis:** A source-traceable timeline and a typed evidence graph produce actionable uncertainty: identified service question, current supported observations, explicit contradictions, missing joins and prioritized requests. Keeping the missing links visible allows a supervisor to take proportionate steps if harm becomes verified, without treating a hypothesis as an observation.

**Continue studying — professional Chapter 05 of 12:** [← Chapter 04](../MANUSCRIPT.md#ch-04) · [Chapter index](../../SUBJECTS.md) · [Chapter 06 →](../MANUSCRIPT.md#ch-06).

### Worked-answer expansion — EX021–EX025

**Integration:** Append after the original Subject 5 C5 join-audit worked result, keeping the original EX021–EX025 answers and rubrics.

**EX021 — Reconstruct the sources, not only the order.** Seven sufficient entries include: C06 approval event 08:50 **released 09:10** (S40/S41 only); C04 raw 08:54 estimated 08:58, ingested 09:06/released 09:09 (no session); C03 IdP 08:58, ingested 09:02/released 09:09 (`s-77`, no person); C02 approximately 09:00 symptom/09:04 receipt (report); C05 09:01 edit/09:07 ingestion/released 09:09 (`q-144`, blank session); C09 detailed identity events 08:58/08:59, received 09:18 (missing object/integrity metadata); C10 displayed 11:21 UTC+02:00 *conditionally* 09:21 UTC, received 09:22 (unknown clock/cache). C11 at 09:24 and C12 at 09:26 can be added **only** in the later final timeline. Each row includes exact card pointer and limitation; a time-sorted story without receipt/release does not meet the required artifact.

**EX022 — Exact-field join reasoning.** C03/C09 share `s-77` in identity fields; C05/C12 share `q-144` in application fields. C09's `runner-03` client matches a *label* in C04 but not an authenticated process/session join. C05 has no session ID, so `s-77` cannot be directly joined to `q-144`. Request producer documentation or an approved known-good trace where the same explicit transaction/session identifier is emitted across both sources. The original C5 and new C5X lab are equality demonstrations; neither identifies a person or proves that batch-17 truly ran.

**EX023 — Competing explanations with falsifiers.** H1 scheduled-job S42 mistake: tag and client are leads, but request/run validation and approved scope are missing; a trustworthy complete job manifest excluding `q-144` would weaken H1. H2 outside-scope account use: visible approval omits S42, but the possible addendum and shared account complicate intent; a valid S42 scope plus correlated authorized run could weaken H2. H3 display/state divergence: screenshot source/cache unknown and C05 reports an edit; a proven incorrect backend state would defeat an exclusively display-only answer. Each row needs a **different authorized check** that could fail; speculative certainty scores zero for source quality.

**EX024 — Two bounded owner requests.** First, service/application owner to confirm *current S42 state, version, last change/request ID and observed time* by an authorized read-only selection, without other learner data; a wrong state would raise immediate service consequence, while a correct state changes the impact hypothesis. Second, job/application custodians to provide a preserved `q-144` run record, producer ID, relevant task version and approved slot list, with verified identifier semantics; a valid match changes H1, a mismatch or missing source leaves it open. The C11 addendum question should be recorded separately. No response or collection receipt is supplied at 09:26.

**EX025 — Handoff model (approx. 157 words).** “At 09:26, CTN-IR-014 remains P2 provisional: C02 reports an S42 enrollment symptom and C05 records an S42 edit via q-144, but the current authoritative slot state and number affected remain unmeasured. C03 and C09 report session s-77, with C09 naming client runner-03; C04's corrected browser time is near the same minute, without a process-to-session key. C12 attaches an unverified batch-17 tag to q-144, not a proven job run. C06's visible task list covers S40/S41; C11 mentions a possible S42 addendum without producing it. C09 lacks complete source-copy provenance and C10 is a displayed symptom with unverified clock/cache. Ask the service owner for a bounded S42 state check and application/job custodians for a preserved q-144 run and validated join semantics. No human actor, approved control or collected follow-up is established. Review before further source loss or on verified harmful change.” A 140–200-word answer should preserve two live explanations, one explicit forbidden overclaim, scope/authority and next gate.

**Chapter 05 focal review:** C5X independently executed with five matching output lines; one missing key and one deliberately mismatched ID are explicit negative controls. All five existing exercise IDs remain paired to original and expanded answers. The case stops at C12 at 09:26; Chapter 6 C13–C19 is not invoked. Current and dated primary sources support conceptual source handling, while the graph test is expressly original and synthetic.

---

## Batch 01–05 editorial integration notes (not teaching)

The five sections above expand their corresponding existing chapters, rather than creating additional curricular subjects. They retain original exercises EX001–EX025, and their worked-answer additions belong in the **same manuscript's final appendix**. Each new Python fixture uses only standard-library, isolated in-memory values, with its literal transcript and a negative control. None is a new canonical CTN record or a completed production operation. Link targets are the existing professional manuscript anchors ch-01 through ch-06 and the edition's SUBJECTS.md. Chapter 6 begins with a new authorization decision after C12; the Chapter 5 handoff does not pre-approve containment.

This is an open public expansion draft, not a final editorial review or an A4 measurement. The book's previous 109-page preflight refers to the earlier manuscript snapshot; this temporary file has not been integrated or rendered into a new A4 release. Technical, factual, source-rights, accessibility, linguistic and whole-volume review remain necessary under [BOOK_STANDARD.md](../../../../../../BOOK_STANDARD.md). Do not declare the professional book complete.
