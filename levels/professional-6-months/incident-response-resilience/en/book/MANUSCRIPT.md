### Exercises — subject 2

<a id="exercise-ex006"></a>

**EX006 — Role-and-right matrix.** Input: C01 and C02. For case opening, bounded log retrieval, session revocation, account disablement and learner notification, name the recommending, approving and executing role; mark unknown escalation routes. A 2-point result keeps those responsibilities distinct.

<a id="exercise-ex007"></a>

**EX007 — Action request.** Input: the cloud colleague's “disable now” question at 09:04. Draft a proposed action record with target, trigger, service risk, approval, operator, expiry and verification. Fields unsupported by C02 must say *pending*, not contain invented receipts. A 2-point result recommends a bounded first step rather than asserting account misuse.

**C2 extension for EX007:** Give the action a revision and list which precise tuple fields are still blank. Compare its status with the four states in the offline TRAIN-A01 fixture; do not transfer that fixture's simulated approval to CTN.

<a id="exercise-ex008"></a>

**EX008 — Option comparison.** Input: choices A, B and C in §2.4. Produce the four-cell comparison for each and select the most defensible first step at 09:04. A 2-point result explains why a later checkpoint might change the selection.

<a id="exercise-ex009"></a>

**EX009 — Approval ambiguity.** Fictional variant `V2`: a supervisor writes “OK to act,” without target or duration. Compose the precise clarification request and a one-sentence case status. Do not import V2 into the main C02 decision. A 2-point result leaves action unexecuted and names missing scope.

**C2 extension for EX009:** State which missing action-tuple fields prevent the phrase from crossing the approval gate. In a copy of TRAIN-A01, remove `scope` after setting its Boolean approval flag; explain the resulting state and why even that script cannot authenticate an approver.

<a id="exercise-ex010"></a>

**EX010 — Decision record.** Input: C01, C02 and your EX006–EX009 work. Write a four-line decision log with observation, inference, action status and next review trigger. A 2-point result distinguishes a proposed preservation request from an approved export.

### Subject synthesis

The decision right belongs to a role and a bounded action, not to the incident label. C02 supports intake and owner escalation, not a tenant-wide change. Chapter 3 will add identity and application signals; revisit the options with the new cards while preserving the 09:04 record as it was.

### Subject 2: EX006–EX010

<a id="answer-ex006"></a>

**EX006 — Model rights matrix.** Case opening: analyst recommends/records, incident lead coordinates, no system change. Bounded IdP retrieval: analyst requests, identity custodian approves under policy and performs export; other data owners may be required by local rules. Session revocation: analyst recommends, identity owner and service owner/emergency-change role approve the named session, authorized identity operator executes and verifies. Account disablement: service owner plus emergency-change authority weigh enrollment impact; authorized operator executes only a scoped approval. External learner notification: communications/privacy owner approves content and audience; designated communicator publishes. C01 lacks the after-hours identity alternate and service-owner fallback; mark both *unknown*, rather than assign a fictional person.

**Additional worked reasoning (EX006 — Why the five rights differ.):** Case opening is a recorder/incident-lead activity, not a disruptive system change. Identity export is a restricted source request requiring custodian/data-owner permission. A single session revocation requires an actual target plus identity and service owner acceptance; account-wide disablement adds emergency change authority because shared enrollment work may stop. A learner notification is a separate communications/privacy decision. For each row name recommender, approving role, operator, artifact and **unavailable alternate from C01**; do not give the analyst delegated permission by assumption.

**Week 2 applied result (EX006).** An acceptable five-row submission treats (1) case intake as a recorded analyst/lead activity with a ticket receipt, (2) IdP export as a data-access decision with selected source, fields and custodian receipt, (3) session restriction as an identity **and** affected-service decision with a named session, operator receipt and service check, (4) shared-account disablement as a broader service/change decision with dependent-route and rollback observations, and (5) learner notice as a communications/privacy decision with approved audience and delivery receipt only if actually sent. The analyst may recommend each row, but cannot supply the missing approval merely by being the case owner. C01 leaves the after-hours identity alternate and service-owner fallback **unknown**. A matrix that labels either “on-call admin” because the person is reachable fails the authority-source column.

<a id="answer-ex007"></a>

**EX007 — Model action request.** `CTN-IR-014 / A-01`: trigger C02 report received 09:04; proposed first action is bounded support validation and owner contact, not disablement. Target S42 symptom and relevant service owner; expected effect better state/context with no service disruption. Account disablement is a **contingent alternative** whose target, time limit, service dependency, rollback and success check must be agreed before approval. Approval = pending; operator = pending; execution time = blank; verification = pending. The cloud colleague's question is not a receipt of any of these steps.

**Additional worked reasoning (EX007 — Versioned proposed action.):** Record `CTN-IR-014 / A-01 / v1`, evidence C02 at 09:04, proposed first step a service-owner-confirmed read-only S42 state question, and conditional later account restriction whose trigger is **not yet observed**. State target and training/production distinction, legitimate enrollment cost, missing approval, missing operator, prohibited premature execution, and next check. A strong answer labels approval/collection/execution **pending** rather than inventing a 09:04 receipt. If cloud operations offers a broader operation than requested, resubmit the envelope; do not treat a shared verb as equivalent authority.

**Week 2 applied result (EX007).** A valid main-case v1 is `CTN-IR-014 / A-01 / v1`, purpose *verify reported S42 availability*, target *S42 authoritative state*, no disruptive method, source C02 received 09:04, service owner/custodian **to be identified**, approval/operator/collection/verification **pending**, next review *owner response or corroborating permitted record*. A hypothetical v2 that adds `ALL_SLOTS` or a session/account change is a **new approval request**, not an amendment covered by v1. In the separate W2 classroom fixture, `SIM-DEC-01` binds only revision 1, read-only S42 training fields, 13:50–14:10 UTC, the training custodian and a 14:20 expiry. The five program lines are `MATCHES_DECLARED_TUPLE_ONLY`, `REAPPROVAL_REQUIRED`, `REAPPROVAL_REQUIRED`, `EXPIRED`, `NO_DECISION_RECORD` in order. None is an authenticated approval or an export receipt.

<a id="answer-ex008"></a>

**EX008 — Model comparison.** A, bounded triage: harm avoided = reduces mistaken disruption; harm introduced = analyst time; uncertainty = present S42 state; verify with owner-authorized read-only check. B, targeted session restriction: possible ongoing-use reduction; risk = breaks an automation session; uncertainty = session-to-harm relation; verify by scoped session status and service-health checks after approval. C, account/tenant change: broader possible restriction; risk = all enrollment writes or other services fail; uncertainty = whether shared account caused anything; verify broad policy state, service checks and rollback. At 09:04 select **A** because C02 alone supports a symptom, not an identified malicious session. A newly verified destructive action could change the balance, subject to owner approval.

**Additional worked reasoning (EX008 — Alternative decision calculation.):** Option A sacrifices a short analyst interval but improves service-truth evidence without service shutdown. Option B may affect one future named session, but C02 lacks its identifier and causal relevance. Option C affects all shared-account enrollment paths and carries the largest unknown blast radius. The correct choice can be provisional A while explicitly naming what **new** source and event would justify a different option. State separate protective and legitimate-service tests for B/C; a dashboard result alone is insufficient.

**Week 2 applied result (EX008).** Select A at C02-only 09:04, pending a custodian-authorized state result. Its potential protective result is a named S42 state/version with source metadata; a broad, unauthenticated screenshot would fail that requirement. For B, name the *missing* live session and causal link, and propose a route-specific prohibition test **plus** a normal-user and scheduled-path acceptance test after a real scoped approval. For C, name broad identity/service/change ownership, the expected loss of enrollment writes, and dependent-service/rollback checks; the account label alone cannot justify it. In a separately labeled W2 branch, a later validated `lab-session-7` link could make B a candidate, but no candidate becomes an executed result. If the platform only offers account-wide scope, compare a new C rather than calling it B.

<a id="answer-ex009"></a>

**EX009 — Model clarification for V2.** “Please identify the exact account or session, permitted action, environment, maximum duration, service impact accepted, operator, rollback owner and approval reference; does your ‘OK’ cover a bounded log request or a disruptive tenant change?” Case status: “V2 supervisor message received; scope insufficient for action; no production change approved or executed.” V2 is separate from C02. “OK to act” should not be stretched to authorize an unspecified tenant-wide edit.

**Additional worked reasoning (EX009 — Why V2 fails.):** “OK to act” lacks object, environment, allowed operation, service effect accepted, time bounds, operator, verification, rollback and authoritative delegation. The request for clarification must identify those fields *and* preserve the original message as an ambiguous version. Correct case state is **clarification requested; disruptive action not approved or executed**. C2X can return a favorable fixture label with invented flags; neither fixture proves the sender's authorization.

**Week 2 applied result (EX009).** A precise follow-up names request ID and revision, proposed operation, exact target/environment, fields or affected objects, interval and expiry, operator, service risk, verifier and rollback owner; it asks which right the sender holds and whether their answer covers only read-only retrieval or a disruptive change. Preserve V2's original text as an unresolved communication artifact. The resulting status line is **“V2 clarification requested; no disruptive action approved, executed or verified.”** In the separate W2 offline gate, replacing `read_export` with `disable_account` must return `REAPPROVAL_REQUIRED` even if the invented `SIM-DEC-01` string is present. A code result cannot authenticate the sender or fill an absent delegation.

<a id="answer-ex010"></a>

**EX010 — Model four-line log.** Observation: “09:04 support received C02; S42 reportedly unavailable, first noticed around 09:00.” Inference: “Potential enrollment issue; cause and authoritative state unknown.” Action status: “Case opened, service/identity owner contact and bounded preservation request **proposed**; no export, restriction or notification recorded.” Trigger: “Revisit after owner state check, relevant source receipt, new reports or a verified retention deadline.” This preserves what the analyst knew at 09:04.

**Additional worked reasoning (EX010 — Decision record at the correct time.):** Four lines: (1) observed C02 receipt 09:04 and estimated symptom noticed 09:00; (2) current S42 state/cause unknown, no justified compromise finding; (3) case opened, limited state/owner questions proposed, no approved export/account change; (4) review when a permitted authoritative state response, corroborating event or verified evidence-loss warning arrives. A later C03 sign-in is forbidden at this checkpoint even though its event time is earlier. A concise source-linked four-line answer is preferable to a long confident story unsupported by C02.

**Week 2 applied result (EX010).** Header: `CTN-IR-014 / decision v1 / knowledge cutoff 09:04 UTC`. Four lines: (1) **Observation** — C02 received at 09:04; reporter estimates S42 unavailable since about 09:00; authoritative state not checked. (2) **Inference** — possible enrollment issue, with cause and actor unknown; a benign state/report mismatch remains possible. (3) **Action state** — case opened, limited owner-authorized state question proposed; no export, restriction, account change or learner notice recorded. (4) **Review trigger** — permitted authoritative response, a corroborating source receipt or a verified loss window. A falsifier for the tentative “current issue” inference would be an approved authoritative S42 state/version showing normal availability at the relevant time, interpreted with the reporter's viewing context. A later C03 release belongs to a new version; an earlier event timestamp alone cannot enter v1.

**C2 worked action-state rehearsal for EX007/EX009.** Executing the exact Chapter 2 Python fixture prints:
