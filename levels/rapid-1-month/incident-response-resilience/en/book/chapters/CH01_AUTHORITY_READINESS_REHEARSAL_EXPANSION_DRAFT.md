# Incident Response and Cyber Resilience — Rapid Course

## Chapter 01 Transitional Expansion Draft: Rehearsing Authority Before an Incident

**Editorial status:** **Public, transitional instructional component** for Chapter 01 of the **single principal English book**. It is not a new course chapter, a final publication, a verified 300-page book, or a source of authority over any real organization.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 01 — Incident readiness, roles and authorized scope](../MANUSCRIPT.md#ch-01).  
**Specific learning gap:** Test **before** an incident whether the current authority register identifies the correct owner, custodians, permitted alternate, version, scope, expiry, approved confirmation route, and stop/escalation path for a proposed evidence request or service change.  
**Preserve rather than repeat:** D1 evidence-source readiness, BSL1 booking invariants, PATH1 functional dependencies, the Chapter 01 authority-role matrix, the R1–R8 evidence classification laboratory, and the Chapter 04 F1 replay. None is replaced by this independent pre-incident exercise.

> **Provenance and chronological boundary:** All Harbor Library records and all examples below are fictional. The Chapter 01 case has R1–R8 at its 09:05 Round A decision. R9–R16 appear only in Round B at 09:20, R17–R24 only in Round C, and Branch S/P and other cards later. The separate **AR1** registry rehearsal takes place on the invented date **2026-09-15**, before the fictional incident, uses only abstract training objects `TR-01` and `TR-02`, and does **not** create case events, real people, real permissions or collection receipts. No AR1 verdict is an approval to operate on production.

# Chapter 01 — New Teaching

### 1.AR1 From knowing a job title to proving a usable decision route

A response plan may correctly say that the service owner approves an interruption and the incident lead approves a bounded collection. That statement is necessary but not enough to know that a future decision can be executed lawfully and safely. What if the primary owner changed positions last month? What if the listed alternate can authorize a small room-booking pause but not an export of unrelated patron data? What if the approval route works during office hours but nobody has tested the designated contact channel? What if the delegation was revoked or its date passed?

An incident response team should discover such gaps **before** a real event forces a difficult choice. The preparation question is not "Does a person appear in a chart?" It is **"Can a reviewer reconstruct an exact, currently valid path from a named request to the responsible decision maker and custodian, with explicit scope and a safe result when the path fails?"**

The current book's §1.3 teaches the distinction between recommendation, approval, execution and verification. This supplement asks students to **rehearse whether those stages are reachable through current authority records**. A successful pre-incident rehearsal demonstrates only that the simulated routing and verification rules were applied correctly for a declared version and time. It does not preapprove later actions or establish that a real person answered a real message.

[NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places incident-response planning and coordination within Cybersecurity Framework 2.0 risk management. [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) addresses the design, conduct and evaluation of IT plan tests and exercises. The versioned authority-register and validation procedure developed here are **original educational techniques** for exploring those documented concerns, not forms prescribed by NIST.

### 1.AR2 A role name is not proof that a particular person holds authority

A service map may name "service owner," "identity administrator," "application custodian" and "incident lead." Each label describes responsibility, but the label alone does not establish which person currently fills the role, which specific actions they can approve, or whether a listed alternate is allowed to sign on the primary's behalf.

A **role** is a category of responsibility. An **appointment** associates that role with a verified organizational identity for a declared time. A **delegation** gives a defined subset of authority to another person or role under explicit terms. A **custodian** manages an object or source and may carry out an authorized request but does not automatically own the business risk decision. A **requester** can explain why evidence is needed; being the requester is not the same as granting the request.

Before an incident, a reviewer should be able to locate the actual authoritative governance record for each appointment and delegation, together with its issuer, approval status, version and validity period. In a real organization, that record may depend on employment status, identity-management groups, formal delegations or other governed systems. The CyberABC exercise does not assume any particular implementation.

A name typed into a spreadsheet is weaker evidence than a current, owner-reviewed appointment supported by the organization's authoritative process. A contact-list entry may remain useful after a person leaves a role, but it is no longer a valid decision source unless the governance system says otherwise. If the reviewer cannot establish the appointment, the correct outcome is to **hold the action and escalate**, not to treat familiarity with the person's name as proof of authority.

### 1.AR3 Establish a versioned register with explicit acceptance questions

A useful **authority readiness register** needs more than columns for name and phone number. It must tell an independent reviewer whether the proposed decision route is valid for the operation under consideration. At minimum, it should identify:

| Register field | What the reviewer must establish |
|---|---|
| Register ID and version | Which edition was checked, and whether it is still current |
| Issuing/maintaining role | Who is accountable for appointments and record corrections |
| Effective and review interval | When this edition begins and ceases to be relied upon |
| Service and operation | Which business system and class of decision it governs |
| Primary decision role | Who can approve this defined operation |
| Custodian/operator | Who may receive the authorized request and perform the bounded task |
| Delegated substitute | Who may substitute for the primary, under what documented authority |
| Delegate restrictions | Permitted operation, objects, duration and any required additional approval |
| Confirmation path | Approved independent route for confirming the respondent's identity and current mandate |
| Required receipt fields | How request, decision scope, version and approval are recorded |
| Negative checks | What must be rejected before permission is relied on |
| Safe escalation | Which governance or incident-lead process receives blocked requests without granting new authority |

The register itself also needs **provenance**. A file named `latest-authority.xlsx` is not adequate evidence of being latest. A change identifier, accountable issuer, recorded review and version transition should make it possible to determine whether a local copy is obsolete. The reader should know which system is authoritative and how to resolve a conflict between two copies.

A register can be a paper table for the introductory exercise. The skill being taught is validating an explicit set of claims, not choosing a particular database or ticketing vendor. Its fields are fictional instructional design choices; no NIST source is presented as requiring this exact schema.

### 1.AR4 Scope belongs to the delegation, not merely to the original request

Suppose the service owner can authorize a temporary pause of one staff-booking write route. An alternate may be delegated authority for **that specific pause**, for a short period. That delegation does not automatically allow the alternate to approve a production database restore, disable every account, retrieve patron newsletter records or extend the pause indefinitely.

The request must therefore be compared with the **allowed operation and object scope** in the register. The same named alternate might have different authority for evidence collection and for a disruptive service control. A delegate approved for one operation should be rejected for another unless a separate valid record covers it.

The AR1 fixture uses two deliberately narrow activities. First, a request to review a synthetic training-audit selection containing only `TR-01` or `TR-02` requires the fictional incident lead's decision and a designated audit custodian. Second, a request to *prepare* a staff-write pause requires both fictional incident-lead and service-owner decision roles; a documented alternate may fill the service-owner role only for that narrow class of pause.

This is a rehearsal of **route validity**, not the execution of either action. The output `REHEARSAL_PATH_VALID_NOT_EXECUTED` never means "audit collected" or "write pause applied." In a real incident, the team would still need a current business decision, collection or change authorization, operator receipt, technical verification and applicable privacy safeguards.

Scope checking should fail closed. If the request includes an unrelated object, the checker should not silently ignore that object and approve the rest as if the original request were unchanged. It should return a hold condition and require an explicitly corrected request.

### 1.AR5 Validity periods and expiry are operational safety controls

An alternate's authority may be valid only for a specified interval. A reviewer needs to know both the effective start and the last valid instant, and should use a consistent time basis. In the AR1 teaching model, the delegation is effective from 13:00 to **before 14:30 UTC** on the fictional rehearsal date. A check at 14:15 can satisfy the time condition; a check at 14:31 cannot.

The strict rule matters: **a previously valid delegation is not indefinitely valid**. The fact that a person approved something yesterday does not grant them the same scope today. A register also can expire as a whole. A delegate cannot be treated as current under an edition that the governance process no longer accepts merely because the individual delegation date looks recent.

The exercise should distinguish expiry from revocation. **Expiry** means the delegated validity interval has elapsed. **Revocation** means a governed decision withdrew the delegation before its nominal end. Either should block reliance on the alternate for the affected operation.

If a timestamp is missing or cannot be compared, do not select the value that makes the test pass. The appropriate state is *unverified time or authority*, subject to review. The AR1 script assumes UTC-aware timestamps and rejects two explicit expired cases; it is not a substitute for authenticating clocks in real organizational records.

An approaching expiry can also be a readiness maintenance trigger. The team should review critical delegations before their deadlines, identify the next approved owner and rehearse the updated route. This prevents a contact list from becoming a silent single point of failure.

### 1.AR6 The owner, approver and custodian can be different people

A request might be valid in business purpose but routed to the wrong custodian. For example, a service owner may approve a limited interruption while an application operator is the only role permitted to apply it. An incident lead may approve a narrow evidence request while the application custodian retrieves records. A collector may not be authorized to approve expanded collection merely because they possess technical access.

The register should model both **who may decide** and **who may carry out the approved task**, as separate checks. A valid approver with an invalid executor is not a valid execution route. Conversely, a valid executor with no valid approval must not carry out the action.

In AR1, the imaginary training-audit request names an audit custodian; the staff-write-pause request names an application operator. Swapping them produces a **wrong-custodian** result even when the requested scope and approver fields are otherwise correct.

This is not meant to impose an organization-wide requirement that every small-team role be held by a distinct human. The book already explains that small organizations may combine roles. The relevant requirement is that the **logical decisions and evidence for each stage remain distinguishable**. A single person holding multiple documented roles must still exercise each role within its applicable authority.

When the same individual would propose, approve and execute a high-impact change, the organization may require additional independent review according to its actual governance. AR1 does not create such a requirement or grant exceptions. It teaches learners to record the unresolved policy question rather than invent a separation-of-duties rule.

### 1.AR7 Use a registered confirmation route rather than an unverified reply

Knowing the correct role is not enough if the request arrives through an untrusted or unregistered channel. A message from an account displaying a familiar name may not authenticate the person or their current role. A successful email delivery indicator does not establish decision authority.

An authority-readiness rehearsal should specify **how the requester can verify a response through a route independently obtained from the approved register**. A common concept is a callback or trusted organizational confirmation channel. The concrete method in a real deployment depends on the organization's identity controls, communications policy and threat model.

The AR1 script represents this complex requirement through the literal field `registered-callback` and a Boolean confirmation flag. These are **toy assertions** supplied by the exercise. They are not identity proof, a secret challenge, a cryptographic signature, a real phone call or consent.

The pre-incident question is: does the plan name a tested route that would let a reviewer distinguish a valid approver from an impersonator or an obsolete contact? A process that says "send an email to the owner" but has no procedure for verifying a surprising or high-impact instruction remains incomplete.

A negative rehearsal should deliberately supply an unregistered messaging channel and confirm that the proposed action is held. Another should withhold confirmation even when the name and route match. In neither case may the team interpret silence as approval.

This concept differs from the Chapter 4 DEL4 laboratory, which tests message delivery, version acknowledgement and read-back **during simulated incident coordination**. AR1 tests **pre-incident trust in the authority path itself**, before any incident action is selected.

### 1.AR8 An approval receipt must identify the bounded decision

A fictional reviewer may receive a response saying "approved." That word alone is insufficient if it does not identify the request, target and scope, the respondent's role, the applicable register version and whether the approval remains current. An approval can be genuine for one task and irrelevant to another.

A useful planned receipt identifies the request ID, decision, operation, objects, approving role and identity, confirmation route, time, restrictions, expiry or review condition and the governing register version. The actual organization may use an established ticket or change process; this chapter does not prescribe a new production system.

AR1 uses a small `SIM-RECEIPT` placeholder to represent the presence of a fictional approval receipt. If the placeholder is absent, the toy validator returns `HOLD_APPROVAL_MISSING`. The presence of that placeholder **does not authenticate the approver or authorize a real action**; it merely lets the learner practice checking that a distinct receipt is part of the planned route.

This is an important epistemic limit. Software can check that fields exist and that values fit a rule. It cannot automatically establish that a real person consciously authorized a service disruption unless the surrounding organizational identity and decision processes supply that evidence.

During a rehearsal, explicitly label the result `valid simulated path, not executed`. This avoids the failure mode in which a "successful drill" is copied into an actual incident ticket and mistaken for a real approval.

### 1.AR9 Two complete contrasting examples: a valid delegation and an unsafe substitute

**Correct example — limited, current, confirmed route in a pre-incident rehearsal.**

On the invented rehearsal date 2026-09-15 at 14:15 UTC, the register version is `AR-3` and is within its stated validity interval. A practice request concerns only the fictional `staff-write-route` operation `pause_staff_writes`. The simulated incident lead `lead-sim` has a separate decision receipt. The named service owner `owner-sim` has issued a documented, unrevoked delegation allowing `alternate-sim` to fill the service-owner approval role for **this operation and object only**, effective from 13:00 until before 14:30 UTC. The designated executing role is `app-operator-sim`.

Both fictional approvals have scoped training receipts and confirmations through the register's stated `registered-callback` route. The validator returns `REHEARSAL_PATH_VALID_NOT_EXECUTED`. The correct interpretation is: **the specified routing conditions passed in the isolated exercise**. No production pause was approved, performed or verified; no real person's identity was authenticated by this script.

A packet suitable for a two-person pre-incident review would preserve the register version, delegate scope and expiry, simulated approval fields, expected operator, check time, stop conditions and the result. The receiving reviewer could reproduce the decision and identify which evidence a real implementation would need.

**Incorrect example — a plausible but expired and unverified substitute.**

At 14:31 UTC in a different artificial run, the same delegate's permitted interval has ended. Suppose someone copies the old owner's name from a contact list, adds a request affecting unrelated booking or newsletter objects, and sends it through an unregistered chat account saying that the matter is urgent. The request is not valid merely because the alternate previously held a relevant delegation or because the channel is available.

The first applicable rejection may be **delegation expired** or **scope exceeded**, depending on what the validator checks first. A real reviewer should record **all** discovered defects in the case's correction work, not interpret one program output as approval of everything it did not mention. The team must not fabricate a new delegation or allow the custodian to act based on that request.

The **correct response** is to hold collection or service change, identify the accountable governance/incident-lead escalation route, obtain a current register or designated approver through authorized channels, and record the unresolved decision. Escalation is an attempt to obtain authority, not an alternative form of authority.

These two examples are not events in the R1–R8 incident and must not be inserted into its 09:05 timeline.

### 1.AR10 A safe escalation path does not grant permission

An emergency contact path may be necessary when the ordinary approver or alternate cannot be validated. But the word "escalate" is often misused to mean "find anyone senior enough to say yes." That approach undermines the reason for recording delegations and bounded authority.

A valid escalation procedure specifies **who receives the blocked decision**, which information may be disclosed, which role verifies the current appointment, how to obtain or clarify authorization, and what the technical operator must **not** do while the decision is unresolved.

For a collection request whose approval is missing, the analyst may continue assessing **already supplied and authorized** records under the permitted scope. That does not authorize access to a new system. For a potentially disruptive change with no verified service-owner route, the coordinator may document risks and request a valid decision; it does not authorize execution based on urgency alone.

AR1 includes `SAFE_ESCALATION`. The output is `ESCALATE_HOLD_DELEGATION_EXPIRED`: an escalation is requested **while the original action remains held**. This is deliberately different from `REHEARSAL_PATH_VALID_NOT_EXECUTED`.

A stronger real-world program might have a separately documented emergency authorization mechanism. If so, its scope, prerequisites, accountable approver and verification would need to be tested as another explicitly versioned authority rule. AR1 neither assumes nor invents such a mechanism.

This differs from the Chapter 4 F1 replay, where an approver becomes unavailable **during** a fictional response. The current exercise instead tests whether the **pre-incident register and fallback process are ready and current**, well before any R-series incident starts.

### 1.AR11 A register must be tested against negative controls

A contact list can appear correct in the easiest path but fail when a person leaves, a delegation expires or a request changes scope. A meaningful readiness test therefore needs both **positive and negative controls**.

The positive control asks whether the correct approvers, scope, version, custodian, receipts and confirmation flags produce a limited readiness pass. Another positive control tests the specifically documented delegate within the valid time window. Those checks demonstrate only the logic of the simulated register.

Negative controls deliberately change **one property at a time**: replace the approver with the wrong person, broaden the requested objects, omit the approval receipt, use an outdated register version, change the custodian, use an unapproved confirmation channel, suppress confirmation, revoke a delegate, or advance the test time beyond expiration. Each should produce a distinct hold reason.

Why insist on this? If the checker accepts every test, it may not be enforcing any real constraint. If it rejects even valid requests, the organization could be unable to act efficiently when a real incident requires a decision. The quality of a readiness control depends on both kinds of behavior.

The lab outputs one primary rejection code for reproducibility. In an actual review, other defects may coexist. Reviewers should avoid declaring that all unreported fields were valid merely because the checker stopped at the first failure.

A negative control does not create an incident. Changing a training receipt's date to simulate expiry does not mean anyone's real delegation expired.

### 1.AR12 Version drift and parallel copies

Authority records frequently change when employees rotate, services move between teams or emergency contacts are updated. A pre-incident rehearsal should include a **version consistency check**. The requester, approving role and custodian should have a reliable way to determine that they are using the same current register edition.

In AR1, version `AR-3` is the synthetic current edition. A copied request still referring to `AR-2` fails with `HOLD_STALE_REGISTER`. The program does not attempt to infer that the older edition may still be "close enough."

There is a separate whole-register validity interval. The example edition is accepted only from September 1 until before October 1, 2026. A check on October 2 returns `HOLD_REGISTER_OUT_OF_DATE` even when its content otherwise resembles a valid request.

These checks answer different questions. A **version mismatch** means the request is not relying on the designated current edition; **register expiry** means the edition's declared relying period has passed. An individual delegate can also expire while the register itself remains valid. A quality test distinguishes the three rather than calling all of them "contact error."

If two remote copies disagree, no spreadsheet title or locally cached value should win merely because it is convenient. The organization's governance owner needs a defined authoritative source and correction path. The response lead should hold any action whose authority cannot be resolved safely.

### 1.AR13 Proof of identity and proof of authority are independent

A caller may genuinely be the person they claim to be, yet lack authority for a particular collection or disruption. Conversely, a directory entry may correctly list a role that belongs to someone else now. The exercise should therefore distinguish **identity confidence** from **decision-scope confidence**.

An approved callback method can help validate who is responding, assuming the real organization implements it properly. It does not establish that the respondent's delegation covers all objects. A versioned delegation can establish the documented scope but does not prove that a particular message was sent by the listed delegate. Both checks matter.

AR1's literal strings are not authentication. The field `confirmed=True` is provided by the instructor as an input premise; no challenge response, access token, signature or real telephone call is performed. The script cannot verify the employee roster, actual phone numbers or current organizational approvals.

An introductory student should be able to say: "The synthetic identity field matched the expected delegate and the synthetic route was declared confirmed; in a real environment I would need authenticated confirmation and an authoritative current delegation record before relying on either." That is more defensible than claiming the code has authenticated a human.

The reviewer must also avoid using the registry as permission to gather unrelated identity records. Authority to approve a booking-audit request is not an unlimited right to investigate everyone associated with the service.

### 1.AR14 Rehearsal artifacts and closure evidence

A useful pre-incident rehearsal leaves behind more than a passing screenshot. The evidence package should identify the tested register version, simulated operation, affected object scope, check time, primary and alternate decision roles, designated custodian, confirmation-route requirement, fixture input, expected status and actual status.

It should separately record that the exercise used **fictional identities and receipts**, that no production action occurred and that the program did not authenticate any real source. An independent reviewer should be able to rerun the same script and understand why each negative case was held.

A remediation ticket might be opened if a rehearsal finds an outdated or missing alternate, ambiguous scope, no approved confirmation channel, overlapping delegation periods, or an owner without a defined callback path. A ticket is not closed by merely updating a contact page. Its closure test should repeat the relevant positive and negative cases under a reviewed register version and retain the result.

For example, a stale-delegation correction could require: a named register steward, a dated current record, a documented successor, an explicitly limited operation and expiry, a confirmed callback route and an independent test in which the old expired delegate is rejected while the current designated route passes. That is a measurable capability improvement.

The training evaluator should avoid assigning a percentage of "organizational authority correctness" based on the toy cases. A small synthetic test validates only its specified fixtures.

### 1.AR15 How to use this preparation without contaminating Round A

The canonical Harbor Library incident begins with R1–R8, not the AR1 rehearsal. The R-series table reports a sign-in, dashboard access, booking changes, a patron report, scheduled training, backup-job completion and a network summary with missing destination detail. It does not contain AR1's roster, delegation issue dates, approval receipts, or confirmation routes.

A responder at 09:05 can use the **general practice** learned from AR1: confirm the proper owner, scope and approval before expanding collection or restricting service. But the responder cannot assert "the owner has already approved because AR1 passed," or include the rehearsal's invented personnel as actual Harbor Library actors.

The Chapter 01 case itself authorizes a bounded classroom analysis of the supplied synthetic records only. All further evidence collection and production-like control changes remain proposed unless the fictional case explicitly supplies a later approval and result. AR1 adds no such result.

In a future organization, pre-incident authority validation reduces a type of uncertainty; it does not eliminate the need for a contemporaneous decision at the moment of incident response. An earlier rehearsal's success may support confidence in the procedure while still requiring current appointment checks, case-specific scope, approval and execution receipts.

This is the key distinction from D1 (does the proposed evidence source exist and work?), BSL1 (does the service meet an approved business invariant?), PATH1 (which functions depend on which components?), and F1 (what happens when an approver is unavailable during an incident?). **AR1 evaluates the governed permission path in preparation**, before any of those actions is needed.

### 1.AR16 Section synthesis

An authority map is not complete just because its role names are sensible. A team should be able to determine whether the current register version is valid, whether the correct person or documented delegate may approve an exact operation and object scope, whether the designated custodian is appropriate, whether the decision was confirmed through an approved route, and whether a missing or invalid condition stops the request.

A valid simulated path must not become a real approval. An invalid path must lead to a documented hold and safe escalation, not silent substitution of a senior-sounding person. The student who can make those distinctions is better prepared to coordinate under pressure without treating urgency as authorization.

The following Python fixture provides a reproducible set of positive and negative authority checks. It deliberately returns **no executed production action** in every scenario.

---

## AR1 Python 3 Offline Laboratory — Versioned Authority and Delegation Checks

**Classification:** Entirely fictional, pre-incident laboratory performed against an invented register. It is **not** an incident, real employee directory, organizational approval, authenticated callback, R-series evidence or the in-incident F1 replay.

**Learning objective:** Check requested operation and object scope, current register version, named approver or valid delegate, custodian, receipt, confirmation route and expiration before allowing even a simulated readiness-path pass. Demonstrate that escalation **holds** the unsafe request rather than authorizing it.

**Environment:** Python 3 standard library only. Everything runs in memory. No files, network, accounts, telephony, chat applications, credentials, privileged operations or personal data.

**Fixture:** The artificial authority register is `AR-3`, declared valid September 1 to before October 1, 2026. The separate delegate `alternate-sim` is permitted to fill the service-owner role only for the training `pause_staff_writes` operation on `staff-write-route` from 13:00 to before 14:30 UTC on September 15, unless revoked. The training-audit example concerns only `TR-01` and `TR-02`. Literal identities are role aliases and do not correspond to real humans.

### Reproducible program

~~~python
from datetime import datetime
from copy import deepcopy

def utc(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

REGISTRY = {
    "version": "AR-3",
    "valid_from": utc("2026-09-01T00:00Z"),
    "valid_until": utc("2026-10-01T00:00Z"),
    "approver": {
        "incident_lead": "lead-sim",
        "service_owner": "owner-sim",
    },
    "delegation": {
        "delegate": "alternate-sim",
        "role": "service_owner",
        "operations": {"pause_staff_writes"},
        "scope": {"staff-write-route"},
        "valid_from": utc("2026-09-15T13:00Z"),
        "valid_until": utc("2026-09-15T14:30Z"),
        "revoked": False,
    },
    "custodians": {
        "training-audit": "audit-custodian-sim",
        "staff-write-route": "app-operator-sim",
    },
}

RULES = {
    "collect_training_audit": {
        "resource": "training-audit",
        "allowed": {"TR-01", "TR-02"},
        "roles": ("incident_lead",),
    },
    "pause_staff_writes": {
        "resource": "staff-write-route",
        "allowed": {"staff-write-route"},
        "roles": ("incident_lead", "service_owner"),
    },
}

def approval(principal, receipt="SIM-RECEIPT",
             route="registered-callback", confirmed=True):
    return {
        "principal": principal,
        "receipt": receipt,
        "route": route,
        "confirmed": confirmed,
    }

BASE = {
    "version": "AR-3",
    "as_of": utc("2026-09-15T14:15Z"),
    "operation": "collect_training_audit",
    "resource": "training-audit",
    "objects": {"TR-01"},
    "executor": "audit-custodian-sim",
    "approvals": {"incident_lead": approval("lead-sim")},
    "delegation_revoked": False,
    "escalate": False,
}

PAUSE = {
    **deepcopy(BASE),
    "operation": "pause_staff_writes",
    "resource": "staff-write-route",
    "objects": {"staff-write-route"},
    "executor": "app-operator-sim",
    "approvals": {
        "incident_lead": approval("lead-sim"),
        "service_owner": approval("alternate-sim"),
    },
}

def evaluate(c):
    reason = None
    if c["version"] != REGISTRY["version"]:
        reason = "STALE_REGISTER"
    elif not (REGISTRY["valid_from"] <= c["as_of"]
              < REGISTRY["valid_until"]):
        reason = "REGISTER_OUT_OF_DATE"
    elif c["operation"] not in RULES:
        reason = "UNKNOWN_OPERATION"
    else:
        rule = RULES[c["operation"]]
        if (c["resource"] != rule["resource"]
                or not c["objects"].issubset(rule["allowed"])):
            reason = "SCOPE_EXCEEDED"
        elif c["executor"] != REGISTRY["custodians"][c["resource"]]:
            reason = "WRONG_CUSTODIAN"
        else:
            for role in rule["roles"]:
                item = c["approvals"].get(role)
                if item is None or not item.get("receipt"):
                    reason = "APPROVAL_MISSING"
                    break

                if item["principal"] != REGISTRY["approver"][role]:
                    delegate = REGISTRY["delegation"]
                    if (item["principal"] != delegate["delegate"]
                            or role != delegate["role"]
                            or c["operation"] not in delegate["operations"]
                            or not c["objects"].issubset(delegate["scope"])):
                        reason = "WRONG_APPROVER"
                        break
                    if c["delegation_revoked"]:
                        reason = "DELEGATION_REVOKED"
                        break
                    if not (delegate["valid_from"] <= c["as_of"]
                            < delegate["valid_until"]):
                        reason = "DELEGATION_EXPIRED"
                        break

                if item["route"] != "registered-callback":
                    reason = "UNAPPROVED_CHANNEL"
                    break
                if not item["confirmed"]:
                    reason = "CONFIRMATION_MISSING"
                    break

    if reason is None:
        return "REHEARSAL_PATH_VALID_NOT_EXECUTED"
    if c["escalate"]:
        return "ESCALATE_HOLD_" + reason
    return "HOLD_" + reason

CASES = [
    ("VALID_AUDIT", BASE),
    ("VALID_DELEGATED_PAUSE", PAUSE),
    ("EXPIRED_DELEGATE",
     {**PAUSE, "as_of": utc("2026-09-15T14:31Z")}),
    ("WRONG_PERSON",
     {**PAUSE, "approvals": {
         **PAUSE["approvals"],
         "service_owner": approval("visitor-sim")}}),
    ("EXCESS_SCOPE",
     {**BASE, "objects": {"TR-01", "newsletter-sim"}}),
    ("APPROVAL_ABSENT",
     {**PAUSE, "approvals": {
         "incident_lead": approval("lead-sim")}}),
    ("STALE_VERSION", {**BASE, "version": "AR-2"}),
    ("WRONG_CUSTODIAN",
     {**BASE, "executor": "app-operator-sim"}),
    ("BAD_CHANNEL",
     {**BASE, "approvals": {
         "incident_lead": approval(
             "lead-sim", route="unregistered-chat")}}),
    ("NO_CONFIRMATION",
     {**BASE, "approvals": {
         "incident_lead": approval(
             "lead-sim", confirmed=False)}}),
    ("REVOKED_DELEGATE",
     {**PAUSE, "delegation_revoked": True}),
    ("EXPIRED_REGISTER",
     {**BASE, "as_of": utc("2026-10-02T14:15Z")}),
    ("MISSING_RECEIPT",
     {**BASE, "approvals": {
         "incident_lead": approval(
             "lead-sim", receipt="")}}),
    ("SAFE_ESCALATION",
     {**PAUSE,
      "as_of": utc("2026-09-15T14:31Z"),
      "escalate": True}),
]

for name, case in CASES:
    print(name, evaluate(case))

assert evaluate(BASE) == "REHEARSAL_PATH_VALID_NOT_EXECUTED"
assert (evaluate(CASES[-1][1])
        == "ESCALATE_HOLD_DELEGATION_EXPIRED")
~~~

### Exact expected output — executed with Python 3

~~~text
VALID_AUDIT REHEARSAL_PATH_VALID_NOT_EXECUTED
VALID_DELEGATED_PAUSE REHEARSAL_PATH_VALID_NOT_EXECUTED
EXPIRED_DELEGATE HOLD_DELEGATION_EXPIRED
WRONG_PERSON HOLD_WRONG_APPROVER
EXCESS_SCOPE HOLD_SCOPE_EXCEEDED
APPROVAL_ABSENT HOLD_APPROVAL_MISSING
STALE_VERSION HOLD_STALE_REGISTER
WRONG_CUSTODIAN HOLD_WRONG_CUSTODIAN
BAD_CHANNEL HOLD_UNAPPROVED_CHANNEL
NO_CONFIRMATION HOLD_CONFIRMATION_MISSING
REVOKED_DELEGATE HOLD_DELEGATION_REVOKED
EXPIRED_REGISTER HOLD_REGISTER_OUT_OF_DATE
MISSING_RECEIPT HOLD_APPROVAL_MISSING
SAFE_ESCALATION ESCALATE_HOLD_DELEGATION_EXPIRED
~~~

### Worked interpretation and failure modes

The first two scenarios are positive controls. They state only that the **simulated authority routing** satisfies the declared AR1 requirements at the selected time. Both still end in `NOT_EXECUTED` because no training fixture represents an actual collection or service change.

`EXPIRED_DELEGATE` moves the rehearsal to 14:31, past the delegate's 14:30 exclusive end. `WRONG_PERSON` replaces the alternate with an arbitrary alias that has no recorded role. `EXCESS_SCOPE` requests an unrelated newsletter object in addition to an authorized training identifier. Those tests must be held even though other fields remain valid.

`APPROVAL_ABSENT` omits the service-owner role receipt required by the pause rule. `STALE_VERSION` uses AR-2 while the declared current register is AR-3. `WRONG_CUSTODIAN` names an application operator for an audit custody task. These are different gaps and need different corrections.

`BAD_CHANNEL` supplies an unregistered route; `NO_CONFIRMATION` withholds a confirmation even on the nominally registered route. Both demonstrate that a plausible name and approval field are not enough. In actual operations, identity and organizational authority would require independently credible proof, beyond these booleans.

`REVOKED_DELEGATE` rejects an alternate whose delegation was expressly withdrawn. `EXPIRED_REGISTER` rejects a date outside the register's own validity, independently of any one delegate. `MISSING_RECEIPT` lacks the simulated decision receipt.

`SAFE_ESCALATION` is the safety control: it **does not pass**. The result asks the responsible escalation process to obtain a current authorized decision while the proposed operation remains held. A trainee who describes it as emergency approval has misunderstood the lesson.

The function returns the **first** detected failure. In a real review there may be several simultaneous deficiencies. The evaluator should preserve any additional defects and must not infer that untested fields are valid from a single error code.

**Technical limits:** The model relies on invented role identifiers, a hardcoded register, synthetic receipts, declared confirmation flags and UTC-aware Python timestamps. It does not validate a corporate identity system, detect a forged approval, authenticate a person, prove a delegation was issued by a real governance owner, authorize a real collection, or execute an action. An actual program would require source provenance, verified identities, revocation information, appropriate approval evidence and permitted channels. A Python pass is **never** permission.

**Learner submission:** Record the 14 output lines, classify each scenario as valid routing, held request or escalation-with-hold, explain the distinct cause of at least five negative controls, and identify which real-world records and verification procedures would be required before relying on a comparable workflow.

---

## AR1 Practical Two-Role Rehearsal — Frozen Packet and Independent Response

**Objective:** Before a simulated incident, verify that a second person can reconstruct the correct authority route from the **current register and request packet**, identify an expired or out-of-scope delegation, and choose a safe escalation without asking the packet author to invent a missing approval.

**Roles:** **Register Steward / Packet Author** and **Independent Readiness Reviewer**. A facilitator may observe but does not change the declared outcomes after seeing the reviewer's first answer.

**Only permitted data:** The artificial AR1 register, synthetic request and simulated receipts. No real employee details, company directories, telephones, credentials or services may be used.

### Phase 1 — Author freezes the packet

The steward prepares `AR1-packet-v1` and records:

1. Register ID, version, issuer role, effective interval and source status.
2. Training operation and permitted object set.
3. Primary approving role and named delegate, including issuer, operation scope, validity and revocation state.
4. Executing custodian/operator for the selected task.
5. Declared registered confirmation route and what a real confirmation would have to establish.
6. A simulated request ID, selected time, named requested operation and objects.
7. The expected safe output if the primary/alternate path cannot be verified.
8. The explicit statement **"training review only; no current incident or production authorization."**

The packet must be frozen before the reviewer begins. A missing field is kept missing; the author may not silently repair the record after learning the reviewer's objection.

### Phase 2 — Reviewer reconstructs independently

Give the reviewer a clearly labelled **valid scenario** and an **expired-delegate scenario**, in that order. Without help from the packet author, the reviewer must identify: current register edition; correct approval roles; whether the named delegate is still valid for the exact request; correct custodian; approved confirmation route; whether all required simulated receipts are present; and the decision to **hold** or **escalate** if any condition fails.

The reviewer submits `AR1-review-v1` with a small field-by-field table and one paragraph explaining the safe next step. A reviewer who says "the person is familiar, so act immediately" fails even if they correctly identify the contact.

The reviewer may consult the frozen register and request but may not ask the author whether a missing delegation "probably exists." If a field needed for authorization is absent, the correct response is **unknown/hold** with a request for an authoritative source.

### Phase 3 — Preserve and adjudicate

Freeze the first response. Compare its decision with the source fields and code output. Record each discrepancy as a **missing packet field**, **incorrect interpretation**, or **unresolved source/authority question**. Do not erase the first submission when corrected evidence becomes available.

A follow-up `AR1-packet-v2` can replace an expired delegation with a newly approved fictitious record, but that new version needs its own validity and confirmation tests. The second attempt is not proof that the first packet was adequate.

### Acceptance and failure rules

A **bounded pass** requires the reviewer to identify the correct version, service/operation/scope, valid or invalid delegation, custodian, confirmation requirement and safe hold/escalation condition, without claiming execution. A **critical fail** occurs if the reviewer accepts an expired/revoked alternate, wrong person, unauthorized objects, missing decision receipt or unverified channel as permission to proceed. A **correctable fail** includes a missing version reference or unclear packet pointer that leaves the reviewer unable to determine authority; the current request remains held until corrected.

This is a **preparedness rehearsal**. Its performance does not say what happened in Harbor Library's R1–R8 incident. It measures a small versioned authority-check procedure, not the actual reliability of a real organization's emergency staffing.

---

## Targeted Refinements — Preserve Existing EX004, EX006, EX009 and EX013

The original Chapter 01 has thirteen numbered exercises. Add **only** the following bounded assessments; retain their existing output formats, chronology, scoring denominator and final-book worked-answer structure. AR1 is an unnumbered supplementary laboratory and does not create additional EX IDs.

### EX004 — Scope boundary

**Additional check:** In the existing short scope decision rejecting a real-world library search, state what the learner would need to see in an **authoritative, current, scope-bound** approval before any future new collection could even be proposed to the designated custodian. Use AR1 to name a stale-register or excessive-object-scope failure as a **separate readiness example**, not as an incident fact.

**Full-credit criterion:** Keep the original permitted objects, reason for rejecting real-site access, contained alternative and stop/escalation condition. An expired delegation or unverified confirmation path must block the proposed additional collection. No simulated valid AR1 result grants permission over a real website.

### EX006 — Role assignment

**Additional check:** Preserve the **original four-row responsibility table**. For the evidence-preservation and possible booking-outage rows, add a short reference to where a **current owner/delegate appointment and custodian assignment** would be checked before relying on it. State which approval remains pending if a substitute is expired, and what evidence would verify that an authorized operator actually performed a later action.

**Full-credit criterion:** The analyst, incident lead, service owner, custodian/operator and reviewer retain distinct logical responsibilities. A published directory listing is not enough to prove a valid delegate, and a positive rehearsal is not an executed collection or service change.

### EX009 — Decision alternatives

**Additional check:** Keep the original **two-option 09:05 matrix**, R1–R8-only evidence and review triggers. For the restriction option, add a **pre-incident preparedness question**: if the service owner or permitted alternate could not be verified through the current register, would the analyst still have authority to impose the restriction? Explain the safe answer without importing AR1's fictitious people or its September rehearsal as a case result.

**Full-credit criterion:** Recommendation and approval remain separate; no missing reply is treated as permission. The chosen provisional option continues to be justified by available case evidence, not by a fabricated expired owner at 09:05.

### EX013 — Readiness gap

**Additional check:** Retain the **three-row gap register plus one improvement ticket**. Where the owner/alternate record is identified as a gap, require a versioned authority-register review and a negative readiness drill checking an expired delegate, wrong approver or excess scope. Define the accountable register steward, completion evidence and a fail/reopen rule. Do not duplicate the in-incident F1 replay.

**Full-credit criterion:** The ticket cannot close merely when a contact list is edited. It must demonstrate, under a frozen simulated version, that a valid path passes and invalid routes remain blocked, with the original inputs and independent result preserved.

---

## Supplementary Worked Answers — For the Principal Book's Final Appendix

### EX004 — Additional worked reasoning

The proposed real-site account search is outside the classroom's authorization; only supplied R1–R8 can be analyzed. An additional real organizational collection would require a documented business question, permitted objects and source, current approving role, custodian, verified appointment/delegation and a confirmed scope-bound decision through an authorized process. A copied old register or an email from an unverified person does not grant authority. In the separate AR1 fixture, a request including an unrelated object returns `HOLD_SCOPE_EXCEEDED` and a stale edition returns `HOLD_STALE_REGISTER`. Neither result says those conditions occurred in Harbor Library's 09:05 case. The safe alternative remains documenting the missing detail and requesting a bounded decision from the proper incident lead and custodian, without accessing any real website.

### EX006 — Additional worked reasoning

The existing four-row table still allocates disruption tolerance to the service owner, collection approval to the incident lead, bounded execution to the appropriate custodian/operator and verification to a reviewer. An authority register could, **before an incident**, demonstrate how the named owner and alternate appointments would be checked and how a role's scope or expiry would be verified. A temporary alternate whose mandate is expired cannot approve a write pause merely because the person was once listed. The request must be held and escalated through an approved route. A completed classroom AR1 test does not mean the synthetic R1–R5 copy was collected or that a live restriction happened. Any later real execution would need a separately authorized receipt and result check.

### EX009 — Additional worked reasoning

The original 09:05 choice uses R1–R8 and may provisionally favor preserving supplied records and testing the scheduled-training explanation, subject to its review time and the risk of further change. Seeking a temporary restriction is a proposal, not an order; the incident lead and service-owner approval, target scope, legitimate service cost and verification plan remain necessary under the case rules. A **pre-incident authority rehearsal** such as AR1 could help the organization identify a valid alternate route before a future disruption. If no current authorized service-owner route can be established, the analyst must not invent approval or treat silence as consent; instead record the hold, document risk and seek the designated governance/incident-lead escalation. The AR1 scenario itself is not a new Round A event or proof that the Harbor Library owner was absent.

### EX013 — Additional worked reasoning

A high-value readiness ticket addresses the missing certainty about service owner and alternate assignments. The incident lead and designated register steward create or review a **versioned, source-linked authority record** showing primary role, restricted alternate, operation/object scope, effective interval, revocation state, named custodian and approved confirmation route. The rehearsal runs at least one positive valid path and one expired or unauthorized negative path using invented identities. It passes when the independent reviewer reconstructs the expected routing from the frozen packet, the valid test remains explicitly **not executed**, and invalid tests return holds or a hold-and-escalate status. It fails if an expired delegate, wrong person, widened scope or absent receipt is accepted; the steward must correct the governed source, version the packet and retest. Publishing a contact spreadsheet without demonstrated failure detection does not close the ticket. The separate F1 incident replay remains outside this pre-incident exercise.

---

## Synthesis, Navigation and Primary Sources

A response plan's owner map becomes operationally useful when the team can verify a **current decision route** before an incident: correct register edition, scope-bound appointment or delegation, permitted operation, custodian, confirmed identity route, required receipt and safe escalation. A test that correctly **blocks** invalid requests can be as important as one that accepts a narrowly valid synthetic route. Neither supplies permission for real collection or live service change.

### Continue studying — chapter 01 of 04 (supplementary public draft)

[← Course home](../../../README.md) · [Course chapter index](../../SUBJECTS.md) · [Chapter 02 →](../MANUSCRIPT.md#ch-02) · [Principal book and worked answers](../MANUSCRIPT.md#answers)

**Editorial integration:** This is a **transitional public component** of the existing English Chapter 01. Accepted teaching, EX004/EX006/EX009/EX013 refinements and their worked answers must be consolidated into the one `MANUSCRIPT.md` after independent editorial review. No additional subject, exercise or course skill is created. This file does not prove A4 completion or organizational accreditation.

### Verified official primary references

- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Final April 2025; organizational preparation, roles and incident-response coordination in wider cybersecurity risk management.
- [NIST SP 800-84 — Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final). Final September 2006; designing, conducting and evaluating plan tests and exercises.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework). Official current framework for governance and cybersecurity outcomes.

These sources support broad preparation and exercise concepts. **NIST does not prescribe the specific AR1 fields, delegated personas, callback strings, dates, sample approvals or Python outcomes.** All such material is original, entirely synthetic CyberABC instruction, not documented incident evidence. Editorial responsibility belongs only to [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned material follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within their limits; third-party works retain their rights. This material authorizes **no real service access or control change**.
