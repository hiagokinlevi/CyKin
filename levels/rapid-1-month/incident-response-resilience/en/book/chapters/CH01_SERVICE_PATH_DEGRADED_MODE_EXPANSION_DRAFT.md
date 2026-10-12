# CyberABC — Rapid Incident Response and Cyber Resilience
## Chapter 01 Expansion Draft: Essential Service Paths and Degraded Modes

**Editorial status:** **Public transitional English instructional draft** for Chapter 01 of the **single principal book**, not a completed chapter, new book or A4-verified release.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 01](../MANUSCRIPT.md#ch-01).  
**Original gap:** The existing chapter identifies components and evidence custodians but does not yet teach how *different business functions* depend on different combinations of components, what happens when one required component is unavailable, and why a useful degraded activity is not necessarily an accepted booking.  
**Preserved material:** D1 evidence-readiness contracts, BSL1 business invariants, the R1–R8 claim-review laboratory, the authority matrix and existing exercise IDs. PATH1 introduces a separate, simple fictional dependency model, not a revision of the canonical Harbor Library architecture.

> **Evidence boundary:** Harbor Library is wholly fictional. R1–R8 alone are available for the 09:05 Round A decision. R9–R16 are released at 09:20 and R17–R24 before the 09:37 Round C decision; Branch S/P and P1/C1/V1 are later separate cards. **PATH1 is an independent counterfactual design exercise:** its component outages and function predictions are not new R-series events or observations of Harbor Library.

# New Chapter 01 Teaching

### 1.P1 A running component is not a delivered business service

A library website may respond while the underlying booking system cannot display current rooms or accept a reservation. A backup monitor may report a completed job while no one has shown that the resulting copy can restore a correct schedule. A help desk may still take a patron's request while the computer-based reservation cannot be accepted. All three situations illustrate the same preparedness problem: the organization can truthfully say that *some* technology remains operational without establishing that the user's promised outcome is available.

The existing Chapter 01 begins correctly with a service map and a D1 evidence-readiness contract. A service map tells the responder which components and owners matter. D1 asks whether useful observations could be obtained under authority, including source semantics and missing evidence. A third question is needed: **which exact user-facing functions would a component fault affect?** Answering it requires a function-specific dependency model rather than treating every component as either globally healthy or globally fatal.

A **service function** is a specific operation with a defined useful result. A **technical dependency** is something required to carry out that operation in the stated architecture and mode. A **degraded mode** is a deliberately narrower operating state in which some activities continue but other service commitments cannot honestly be made.

These distinctions are consistent with the emphasis on service dependencies and business function recovery in [NIST SP 800-184, *Guide for Cybersecurity Event Recovery*](https://csrc.nist.gov/pubs/sp/800/184/final) and with risk-aware response preparation in [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Those NIST publications do not specify Harbor Library's internal routes; PATH1 is original classroom reasoning material.

### 1.P2 Begin with the promise made to a patron

Imagine five distinguishable functions for a hypothetical reservation service: an informational page responding, a current list of rooms being displayed, an authorized staff member editing a booking, a front-desk employee recording a pending request, and a new backup job obtaining its source data.

The results are not interchangeable. A successful informational page response says little about reservation accuracy. An accepted staff edit is a business-state change, potentially requiring authorization and durable storage. A manual request receipt is **not** acceptance of a reservation. A backup job's access to a database is **not** a tested restore or an accepted return to service.

A weak readiness statement says, "the app is available." A more useful statement says, "the authorized staff-edit function produced the expected change to the intended booking and a reviewer checked the resulting authoritative state in a controlled test." The second statement has a testable outcome and a declared scope.

At rapid-course depth, learners should identify the **unit of success** before selecting a test. Is the question about reaching a page, viewing a current room, placing a reservation, collecting a pending request or producing a backup object? Each unit needs a different answer and may have different technical dependencies.

This framing also improves incident communication. The service owner may legitimately approve a limited request-intake workaround, but staff must not announce that rooms are confirmed while writes are unavailable. An honest degraded-service notice should explain what the user can do, what remains pending and what must occur before confirmation is possible.

### 1.P3 Express path assumptions as a small dependency table

The PATH1 teaching model uses components named `web`, `identity`, `database`, `helpdesk` and `backup`. These categories resemble the service map, but their **specific connections are invented**. The canonical R1–R8 records do not confirm this topology.

| Fictional modeled function | Required PATH1 components | Narrow business meaning |
|---|---|---|
| `site_reachable` | `web` | An informational page can respond |
| `room_view` | `web`, `database` | A room-view route is structurally possible |
| `staff_edit` | `web`, `identity`, `database` | A staff-edit route has its modeled prerequisites |
| `manual_intake` | `helpdesk` | A pending request can be received, not committed |
| `new_backup_job` | `database`, `backup` | The modeled backup process can access source data |

A component in a path is **required under this model**. If a required component is unavailable, the script predicts the function is impaired. If every required component is marked available, it predicts only **structural possibility**, not verified correctness. The model does not implement authentication, data persistence, cache validity, backup integrity, patron notification or performance.

These limitations are not weaknesses to conceal. They define which engineering question the model answers. A small, explicit model can help identify the next owner or test, provided no one promotes its predictions into real observations.

By contrast, D1's source contract asks whether an application audit or identity record could prove what actually happened. BSL1's business-rule exercise checks overlaps and cancellation semantics using separate invented booking records. PATH1 does neither. It asks which *functions* could lose their modeled prerequisites under component loss.

### 1.P4 A single component failure may impair several different functions

Consider the independent hypothetical case where the PATH1 database becomes unavailable. Because `room_view`, `staff_edit` and `new_backup_job` all list it as required, the model predicts those three functions are impaired. The informational page and manual help-desk intake do not list it, so they remain structurally possible in this simplified design.

That prediction is not equivalent to "the website is healthy." A resident might reach a page but fail to view a trustworthy room list. It is also not equivalent to "the whole library cannot help anyone." Under the fictional fallback assumption, the help desk can still receive an unconfirmed request.

An identity-service failure has another shape. It impairs the modeled staff-edit path but does not necessarily impair room viewing. This does **not** establish that Harbor Library actually permits unauthenticated read access; it reflects only the independent fixture.

A help-desk failure can remove the manual fallback while website-mediated paths remain structurally possible. During ordinary operation this might be inconvenient; during a wider outage it could remove the only permitted path for receiving new requests. Thus the business importance of a dependency depends on the operating context.

The correct incident question is therefore not simply "which component is red?" It is **which useful function is affected, what other path remains, and what legitimate promise can still be made?** Component counts cannot substitute for that analysis.

### 1.P5 Single points of failure must name their affected outcome

Calling a component a "single point of failure" is incomplete without naming the function it can prevent. In PATH1, failure of `web` alone prevents the informational page, room view and staff-edit route. It does not, under the stated fixture, prevent help-desk request intake or a new backup job.

Likewise, the database is a single required element for the modeled room view, but not for the informational page. A real application may have additional dependencies or a working alternate route; the PATH1 table provides no evidence about them.

For a function with all-required dependencies, **failure of any listed component** is sufficient to impair that particular modeled path. A real resilient design might instead have alternatives—such as two equivalent service instances or a controlled cached read. Such alternatives must be explicitly documented and tested before they are used in operational decisions.

This beginner model deliberately avoids probability estimates. A list of components does not provide failure rates, correlations, repair times or evidence that alternate capacity is usable. Assigning an invented likelihood of downtime would add precision without support.

The preparedness value of this reasoning is asking a service owner to identify what is truly essential and which alternate route can safely meet a narrower requirement. It does not authorize changing a production configuration.

### 1.P6 Available, degraded, unavailable and unknown are different conclusions

A route can be **modeled available**, **modeled impaired**, **observed to work in a bounded test**, or **not yet tested**. These statements should not be collapsed into a single green/red label.

For PATH1, the supplied Python fixture uses Boolean component availability and predicts structural status. Real components can fail partially: a database may answer reads while rejecting writes; an identity service may validate old sessions but not new ones; a cache may return stale content. In those circumstances a simple Boolean may hide important uncertainty.

If an analyst cannot determine a component's actual state, it would be improper to enter `True` merely so the model returns a green result. Record the condition as unknown and ask what observation could resolve it. The classroom script omits a third state for simplicity; the learner must report that as a modeling limitation.

A successful response from a web endpoint also does not prove that a booking change was authorized and durably committed. A help-desk receipt does not prove a room assignment exists. These are examples of **overclaiming from partial success**.

An accurate report might say, "under the selected model, the informational page path remains structurally possible, while the booking write path is predicted unavailable." It should not claim that real patrons can safely use the service without a corresponding test and owner acceptance.

### 1.P7 Design a degraded mode with explicit boundaries

A degraded mode is not simply "whatever still works." It should be defined in advance by the service owner, with conditions for activation, an approved workflow, a duration or review trigger, a message that accurately describes service limits, and a path back to normal operations.

For a hypothetical request-only help-desk mode, the owner would need to answer:

1. May staff receive requests while the authoritative reservation service is unavailable?
2. Which minimum details can be collected safely and for what purpose?
3. Does the request remain **pending** until a later authorized check?
4. Who maintains receipt order and prevents duplicates or conflicting instructions?
5. Who communicates the distinction between receipt and acceptance to patrons?
6. What is the escalation route if the desk cannot keep up or the request is urgent?
7. Who authorizes eventual reconciliation and confirms the resulting business state?
8. What observable result ends the degraded mode?

This is a **proposed business contract**, not a claim that the canonical Harbor Library help desk followed such a procedure. The later Chapter 3 MQ3 laboratory teaches detailed request reconciliation, but PATH1 asks an earlier, different question: *Would that kind of fallback function remain technically possible under a specified component fault?*

Manual intake may be unavailable by policy even when the help desk is working. Staff may lack capacity, approved paper procedures or privacy safeguards. A model's technical possibility never overrides the service owner's operating constraints.

A safe degraded-mode statement says, "the request may be recorded for review." A dangerous statement says, "the room is booked" when the accepted reservation has not been established.

### 1.P8 Readiness needs a verification plan for each function

Before accepting the function table, a service owner and technical custodian should identify the test that would challenge it. A useful test plan includes:

- The function and promised outcome.
- The proposed required components.
- The specific isolated fault or unavailable component.
- The predicted impairment or alternative behavior.
- The positive technical observation to look for.
- A negative or business-safety check.
- The responsible owner and permitted environment.
- A source and timestamp for the actual result.
- The limit of the conclusion and the required review.

For the modeled room view, a technical response alone might be insufficient if it returns stale or unauthorized data. For staff editing, a successful request does not prove the intended authoritative value was committed. For a backup job, creation does not prove the object is recoverable. For help-desk intake, a receipt does not prove the request was accepted.

This plan should be compared with existing D1 and BSL1 artifacts **without copying their content**. D1 specifies how a record could be obtained and interpreted; BSL1 defines some correct booking-state behavior; PATH1 specifies which path's prerequisites are being challenged. A real isolated test might draw on all three, but the conclusions remain separate.

If the expected negative test fails, record the failure rather than silently weakening the acceptance rule. If the input data are incomplete or the supposed fault was not actually induced, report an **inconclusive test** rather than a clean pass.

### 1.P9 Contrast a tempting wrong conclusion with a defensible one

**Incorrect hypothetical analysis:**

> "The database is down but the homepage responds, so the service is healthy. Staff can take requests at the desk, which means reservations are still confirmed. The backup component remains online, so the library can already restore everything."

This assumes that the informational page represents all booking functions; that a pending manual request is a completed reservation; and that a backup component or job outcome proves tested recovery. None of the claims follows from the PATH1 model, and no database outage appears in canonical R1–R8.

**Correct bounded analysis:**

> "In the independent PATH1 model, database unavailability predicts impairment of the room-view, staff-edit and new-backup-job paths, while the informational page and help-desk request intake remain structurally possible. Manual intake does not accept reservations, and no recovery test is supplied. These are sensitivity predictions from declared assumptions, not Harbor Library incident observations. The service owner would need to approve any degraded operating promise, and a separate authorized check would be required to establish actual function and business correctness."

The improvement is not simply cautious language. It identifies the **unit of service**, the **source of the claim** and the **missing acceptance evidence**.

### 1.P10 Compare fault scenarios without turning them into canonical events

A useful offline rehearsal changes one modeled condition at a time and records which functions change classification. The student should begin with the baseline, simulate a database failure, restore the baseline and simulate identity failure. The same process can be used for help-desk and web failures.

Without resetting the model, conclusions can become mixed: a lingering database-down condition may make an identity test appear to impair more functions than it really does. The code below avoids this by evaluating independent failure sets rather than mutating the shared route definitions.

Comparisons should be explained in business terms. If identity failure affects only the staff-edit path, that is different from database failure affecting viewing, editing and new-backup creation. If help-desk failure removes intake, the potential harm depends partly on whether users have another approved means of making requests.

A two-component failure is useful as a negative control. With both database and help desk unavailable under PATH1, the remaining informational page cannot provide accepted booking writes or receive pending requests. It would be misleading to label that state "partially operational reservation service" without specifying the limited information-only function.

The fixture provides **no frequency, probability or severity score** for these scenarios. Those require information from the service owner and measured operational evidence outside the classroom.

### 1.P11 Relationship to incident decisions at 09:05

Return to the actual fictional Round A source set. R1 reports a `desk-a` sign-in, R3 and R4 report booking changes, R5 is a patron concern, R6 describes scheduled training, R7 reports a backup-job completion and R8 lacks sufficient destination detail. These records support questions about approval, service state and identity context. They do **not** establish any PATH1 component outage.

A student might reasonably propose that the service owner clarify what would happen if the database were unavailable, or whether a request-only fallback is approved. That is a readiness question, not a finding about the incident.

A PATH1 scenario must never be inserted as an additional R-series row or used to justify the 09:05 restriction decision. Likewise, the later B19/B20 events or Branch S/P results cannot be imported backward to resolve the original uncertainty.

A high-quality responder can maintain two ledgers: the **canonical evidence ledger**, limited to released case records, and a **model/test ledger**, containing declared assumptions and hypothetical outcomes. This separation permits technically useful planning without fictionalizing production observations.

### 1.P12 Section synthesis: resilience is a bounded service promise

Resilience is not a guarantee that every component stays online. It is the ability to define important user outcomes, identify how component failure could affect them, prepare acceptable narrower modes, and test what those modes actually deliver.

A website may be reachable while current room viewing is impaired. A help desk may be able to receive a request without confirming a reservation. A backup job may be possible without demonstrating recovery. Recognizing these distinctions improves the quality of incident questions and makes subsequent service-owner decisions more defensible.

The PATH1 laboratory is purposely small. It trains one transferable habit: **predict structural consequences, identify the business promise, and demand appropriate observation before declaring service impact or recovery**.

---

## PATH1 Offline Laboratory — Functional Dependencies and Degraded Service

**Classification:** Independent, entirely synthetic modeling exercise. Not R1–R24, not the BSL1 booking-state fixture, not the technical-level L6 architecture and not a recorded Harbor Library outage.

**Environment:** Python 3 standard library, in memory. No files, network calls, real credentials or service modifications.

**Prediction task:** Before running, predict which functions remain in each scenario and whether the result means modeled staff-edit availability, request intake only or no modeled staff-edit/intake route.

### Complete Python program

~~~python
ROUTES = {
    "site_reachable": {"web"},
    "room_view": {"web", "database"},
    "staff_edit": {"web", "identity", "database"},
    "manual_intake": {"helpdesk"},
    "new_backup_job": {"database", "backup"},
}

CASES = [
    ("BASE", set()),
    ("DATABASE_DOWN", {"database"}),
    ("IDENTITY_DOWN", {"identity"}),
    ("HELPDESK_DOWN", {"helpdesk"}),
    ("WEB_DOWN", {"web"}),
    ("DATABASE_AND_HELPDESK_DOWN", {"database", "helpdesk"}),
]

def assess_failed(failed):
    available = sorted(
        name for name, needs in ROUTES.items()
        if needs.isdisjoint(failed)
    )
    impaired = sorted(set(ROUTES) - set(available))

    if "staff_edit" in available:
        mode = "STAFF_EDIT_PATH_MODELED"
    elif "manual_intake" in available:
        mode = "REQUEST_INTAKE_ONLY"
    else:
        mode = "NO_EDIT_OR_INTAKE_PATH"

    return available, impaired, mode

for name, failed in CASES:
    available, impaired, mode = assess_failed(failed)
    print(
        f"{name}: available={','.join(available)} "
        f"impaired={','.join(impaired)} mode={mode}"
    )

assert assess_failed({"database"})[2] == "REQUEST_INTAKE_ONLY"
assert "room_view" not in assess_failed({"database"})[0]
~~~

### Exact expected output — executed with Python 3

~~~text
BASE: available=manual_intake,new_backup_job,room_view,site_reachable,staff_edit impaired= mode=STAFF_EDIT_PATH_MODELED
DATABASE_DOWN: available=manual_intake,site_reachable impaired=new_backup_job,room_view,staff_edit mode=REQUEST_INTAKE_ONLY
IDENTITY_DOWN: available=manual_intake,new_backup_job,room_view,site_reachable impaired=staff_edit mode=REQUEST_INTAKE_ONLY
HELPDESK_DOWN: available=new_backup_job,room_view,site_reachable,staff_edit impaired=manual_intake mode=STAFF_EDIT_PATH_MODELED
WEB_DOWN: available=manual_intake,new_backup_job impaired=room_view,site_reachable,staff_edit mode=REQUEST_INTAKE_ONLY
DATABASE_AND_HELPDESK_DOWN: available=site_reachable impaired=manual_intake,new_backup_job,room_view,staff_edit mode=NO_EDIT_OR_INTAKE_PATH
~~~

### Interpretation, negative variant and limitations

With every component assumed available, the model predicts all five paths structurally possible. The label `STAFF_EDIT_PATH_MODELED` is **not** a successful or authorized reservation write.

When the database is down, the informational page and manual intake remain structurally possible; room viewing, staff editing and new-backup creation are impaired in the toy model. Manual intake is only request receipt, not confirmed booking service.

When identity is down, only the staff-edit path is impaired under the declared requirements. When the help desk is down, the fallback intake path disappears but the website-related routes remain. When the web component is down, request intake and the backup job remain, but the application-related functions are impaired. When both database and help desk are down, an informational page alone cannot satisfy either modeled edit or intake requirement.

**Negative sensitivity variant:** Temporarily remove the `helpdesk` dependency from `manual_intake` in a copied model. The input would then incorrectly imply that request intake does not require any component. Explain how an omitted dependency can make a model appear more resilient than its actual implementation. Restore the original dictionary after the experiment.

**Limits:** The script calculates only set-based structural predictions. It does not simulate partial outages, fallbacks, caching, transaction durability, authentication correctness, service-owner approval, actual request processing or business-state verification. The user must not interpret any printed line as a real Harbor Library event.

**Submission:** Provide six model-result rows, two contrasted function impacts, the negative-variant interpretation and one specific authorized test that would discriminate a modeled prediction from observed service correctness. A response that claims `manual_intake` proves a completed booking fails the learning objective.

---

## Targeted Exercise Refinements — Retain Existing IDs

The course already contains thirteen Chapter 01 exercises. These four supplements preserve the original prompts, exercise numbers and 0–2 rubric; they do not introduce new questions numbered EX014 or higher.

### EX003 — Service dependency

**Additional requirement:** After the existing two dependency cards, choose one PATH1 modeled function and identify a component fault that would impair it. State an authorized *functional* check and a separate *business correctness* check. Do not claim that the PATH1 fault occurred in canonical R1–R8.

### EX006 — Role assignment

**Additional requirement:** Keep the original four-row role matrix. For the possible booking outage, distinguish an approved manual-request intake procedure from actual booking acceptance; name the service owner of the hypothetical degraded-mode decision, the help-desk custodian of receipts and the reviewer who would authorize reconciliation.

### EX008 — Evidence quality

**Additional requirement:** In the R7 backup-status row, explain why modeled `new_backup_job` availability would not verify usable restore, acceptable elapsed recovery or owner-approved booking correctness. Preserve the original R6 training and R8 network-summary source limitations.

### EX009 — Decision alternatives

**Additional requirement:** Keep both original 09:05 options and their approvals. Add a clearly marked **counterfactual**: if a future authorized test found staff edits impaired but manual request intake possible, identify the one user promise that remains permitted and one that is prohibited. Do not replace the original evidence decision or invent a new R-series item.

---

## Supplementary Worked Results — Intended for Final Answer Appendix

### EX003 — Additional worked reasoning

The staff identity source and reservation database are different dependencies with different evidence questions. R1/R2 report a sign-in and dashboard use without human attribution; R3/R4 report edits and R5 reports a patron symptom without establishing correct current state. In the separate PATH1 model, `staff_edit` requires `web`, `identity` and `database`. A modeled identity failure predicts impairment of this path but is not an observed Round A outage. A suitable future isolated test would check both an approved staff-edit operation and its independently observed authoritative result. The service owner would define business acceptance; the identity and application custodians would supply permitted technical evidence. The model cannot substitute for either.

### EX006 — Additional worked reasoning

The original responsibility table remains valid: analyst and incident lead coordinate the question, service owner controls acceptable business interruption, the appropriate operators execute separately authorized actions, and recovery leads design contained verification. A hypothetical request-only degraded mode would need service-owner approval, a help-desk owner for pending receipts and a later authorized reconciliation. Staff could report that a request was received for processing, not that a reservation was confirmed. PATH1 supplies only a model of intake possibility; R1–R8 supplies no approval or actual pending queue. The four-row format remains unchanged.

### EX008 — Additional worked reasoning

R6 documents scheduled training, not permission for specified booking edits. R8 lacks destination details and cannot establish absence of transfer. R7 records a completed backup job, but not a named recoverable copy, restore timing, accepted booking values or functioning restored service. PATH1's hypothetical `new_backup_job` path is another structural premise, not recovery evidence. A future contained test would identify the copy, source time, isolated test environment, expected booking values, measured result and service owner. Until such a result is supplied, recovery correctness remains unverified.

### EX009 — Additional worked reasoning

At 09:05, preserving R1–R8 and seeking confirmation of B17/B18 training authorization remains a defensible provisional option; a restriction proposal remains separately subject to authority and operational impact. A **different** counterfactual service-failure model may suggest that a help desk could receive pending requests while accepted staff edits are unavailable. If an actual organization separately validated and approved such a mode, staff could promise only **receipt for later review**, not a completed reservation. A modeled fallback does not prove that the real service is available or that R1–R8 contains any outage. The incident lead should not backfill that fault into the original case or silently change the 09:05 reasoning.

---

## Chapter Navigation and Primary References

### Continue studying — chapter 01 of 04 (supplementary draft)

[← Course home](../../../README.md) · [Course chapter index](../../SUBJECTS.md) · [Chapter 02 →](../MANUSCRIPT.md#ch-02) · [Worked results in the principal book](../MANUSCRIPT.md#answers)

**Editorial state:** This Markdown file is a **transitional public component** of Chapter 01 of the single principal English book. It does not increase the official exercise count, certify a real incident or establish completion. Accepted prose and worked-answer refinements belong in the existing `MANUSCRIPT.md` after editorial integration and review.

### Primary sources

- [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Final April 2025; preparation and response decisions in organizational risk management.
- [NIST SP 800-184 — Guide for Cybersecurity Event Recovery](https://csrc.nist.gov/pubs/sp/800/184/final). Final December 2016; service dependencies, mission functions and recovery planning.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework). Official framework for cybersecurity outcomes.

The PATH1 model, failure scenarios, outputs, prose, exercises and answers are original **synthetic educational material**; the NIST sources neither prescribe those specific outputs nor authenticate the fictional Harbor Library. Editorial responsibility is solely [hiagokinlevi](https://github.com/hiagokinlevi). The maintainer's original content follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within their documented limits; third-party works retain their rights. No actual systems are tested.
