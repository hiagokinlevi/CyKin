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
