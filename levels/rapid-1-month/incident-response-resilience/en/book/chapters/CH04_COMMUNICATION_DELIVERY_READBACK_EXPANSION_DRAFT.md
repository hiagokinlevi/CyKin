# Incident Response and Cyber Resilience — Rapid Course

## Chapter 04 Public Expansion Draft: Verified Delivery, Read-back, and Fallback of Incident Coordination Messages

**Editorial status:** **Public transitional component of Chapter 04 of the one principal English book.** This is not an independent fifth chapter, a completed book, a verified live communications test, or a separate course skill.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 04 — Guided incident simulation and after-action review](../MANUSCRIPT.md#ch-04).  
**New learning gap:** A team can draft and approve a correct status or action instruction but still fail to deliver it, reach the accountable role, communicate the current version, or obtain an accurate operational read-back. The existing chapter addresses message content, audiences, approvals, branch selection, L2 scoring, F4-AUDIT, F1 and M1/M2; this supplement develops **communication-path verification and acknowledgements** without recreating those exercises.  
**Exercise IDs preserved:** EX039, EX043, EX044, EX046, EX048, and EX050 receive focused assessment refinements and corresponding worked reasoning. No new EX IDs or canonical incident records are created.

> **Fiction and safety:** Harbor Library, the incident records and all laboratory messages are fictional. Nothing here authorizes a call, text, email, account operation, security test or public notice involving an actual organization. The DEL4 teaching messages, attempts, acknowledgements, versions and outcomes are **independent synthetic fixtures**, not R-series evidence, not a Branch S/P result, and not a delivered message in the canonical case.

### Canonical availability and scenario rules

The original tabletop releases **R1–R8** in Round A for the 09:05 decision; **R9–R16** only in Round B at 09:20; **R17–R24** only in Round C before the 09:37 decision. The first Round D card reports **either Branch S or Branch P** at 09:45, not both. **P1/C1** is a later separate recovery card; **V1** arrives after its own release. The optional F1 unavailable-approver and M1/M2 communication replays remain independent teaching variants. An event time in an R-series record never moves its classroom release to an earlier round.

This supplement's examples sometimes select a *hypothetical Branch P replay after its release* so that front-desk instructions can be evaluated. That does not place Branch P in the Round C decision, does not treat R21's tolerability statement as approval, and does not provide any of Branch P's two queued request IDs. No packet is assumed sent to a real person.

# New Teaching — The Delivery Side of Incident Coordination

### 4.19.1 An accurate message can fail operationally after approval

Previous sections teach how to write a defensible update and decide which audience should receive it. An additional operational question remains: **How does the response lead know that a time-critical instruction reached the role that must act on it, with the correct version and meaning?**

A message may be carefully worded, approved and stored in the case record, yet never leave the author's draft. It may be sent to an unavailable channel, delivered to the wrong distribution group, received by someone without operational responsibility, or acknowledged by a person who interpreted it differently. A successful transport attempt also does not prove that an instruction was understood or performed. These are different potential failures with different evidence requirements.

Consider a fictional staff-write pause. If a front-desk supervisor continues to accept ordinary writes because the approved temporary procedure never reached the desk, the message-handling failure can cause service confusion even when the control decision itself was justified. Conversely, an unsanctioned fallback message telling staff to resume writes can undermine a continuing pause. A response team therefore needs to evaluate **message delivery as a bounded operational process**, distinct from message authorship and the technical validity of the original decision.

[NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), particularly its incident-response coordination and communication discussion under RS.CO, recognizes the need to communicate appropriate information to responsible stakeholders. [NIST SP 800-34 Revision 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) discusses contingency-plan activation, notification and recovery coordination. The exact delivery and read-back contract below is an **original CyberABC teaching model**, not a NIST-required acknowledgement protocol.

The rapid-course outcome is specific: a learner should be able to say whether a message was *drafted, authorized for transmission, attempted, delivered, acknowledged for a particular version, correctly read back, or still unresolved*. A claim of completed operational action needs independent execution and verification evidence; no communication receipt automatically supplies it.

### 4.19.2 Build a chain of receipts, not a single "sent" checkbox

Treat the communication lifecycle as several distinguishable claims:

| State or receipt | Narrow claim it may support | Important excluded claim |
|---|---|---|
| Draft created | The author prepared particular wording | Anybody received it |
| Wording approved | The designated authority approved this message for this scope | The associated containment action was approved or executed |
| Dispatch attempted | A chosen route was used or queued for transmission | The receiver's system accepted or displayed it |
| Delivered | The declared channel recorded delivery to its destination | The intended human or responsible role read it |
| Role acknowledgement | A response associated with the intended role and version was recorded | The recipient interpreted every instruction correctly |
| Read-back checked | The recipient repeated the required operational meaning in the test scope | The real control or service state changed |
| Action completed and verified | Separate sources support the approved operational outcome | All other incident questions are resolved |

Real communication systems use differing semantics. An email server's acceptance receipt is not always a human delivery or reading receipt. A messaging application's "delivered" indicator may represent a device, not the accountable shift supervisor. An automated read receipt can be generated by software or a preview. A short reply saying "OK" may acknowledge a conversation without identifying the particular instruction or its conditions.

The training contract should therefore define each event with a **producer and limit**. If the fictional coordination method can prove only dispatch to a gateway, record *dispatch accepted*, not *recipient acknowledged*. If the recipient's read-back is missing, report it as pending rather than fill in an assumption based on ordinary work habits. This is the same evidence discipline used earlier in the book, now applied to coordination rather than incident telemetry.

A response lead also should avoid treating silence as consent. A recipient who fails to answer may be busy, disconnected, off shift, unable to access the selected channel, or unsure of the request. Those possibilities do not grant the sender approval to execute a service change. The appropriate outcome is a planned escalation through previously authorized contacts and procedures, recorded as a separate event.

### 4.19.3 Message approval and action approval are different decisions

An especially dangerous ambiguity arises when a carefully approved message describes a *proposed* operational control. The message may be cleared for internal coordination while the proposed action remains unapproved.

At the canonical 09:37 Round C checkpoint, R19 says the identified current session **can** be revoked, and R21 says a short staff-write pause is **tolerable** under specified business conditions. Neither record says that an actual session was revoked or that the staff-write pause was executed. A communication such as "Please review the proposed session restriction with the identity owner" could be authorized to send without authorizing the restriction itself.

The coordination record should carry two separate fields:

- **Approval to communicate:** Which role approved the wording, audience, classification and channel?
- **Approval to execute:** Which accountable authority approved the operational action, target, duration and conditions, and where is its receipt?

One must not be inferred from the other. A communications contact may approve a patron-facing draft but have no authority to stop the booking service. A service owner may approve a pause but not authorize disclosure of account details to an external recipient. A message reporting the Branch S 09:45 revocation is also different from an independent identity-system receipt that would verify the control's current technical effect.

The useful negative test is to ask whether a recipient could mistake the communication for an execution order. If so, change its action verb and state label: "proposal awaiting identity approval" should not be written as "disable now." In an authorized real system, the change process and message-routing process must retain their own evidence and permissions. The tabletop does not create those permissions.

This separation prevents a successful read-back from being used as false evidence that an earlier control was validly approved. The recipient can correctly repeat an instruction that was never authorized. The response lead must inspect *both* the sender's permission and the recipient's comprehension before relying on the communication as coordination evidence.

### 4.19.4 Define a message envelope that identifies the exact instruction

For internal incident coordination, content alone is not enough to tell whether a receipt refers to the right instruction. Two updates might mention the same case and the same account but give different operational directions.

A **message envelope** is a small set of metadata accompanying the bounded instruction. It should include:

| Field | Why it matters |
|---|---|
| Case ID | Binds the message to the correct incident |
| Message ID and version | Distinguishes an updated instruction from an older one |
| Frozen release checkpoint | Prevents later branch facts entering earlier communications |
| Chosen branch, if any | Prevents mutually exclusive Branch S/P instructions being combined |
| Intended role | Specifies which function must receive and answer, not just a personal address |
| Approved audience and channel | Bounds information exposure and permitted delivery method |
| Action/status label | Says whether the text is information, proposal, request for approval, or authorized operational instruction |
| Required read-back | Defines what the recipient must repeat to show actionable understanding |
| Acknowledgement owner and deadline | Defines who follows up if a response is missing |
| Reference to superseded version | Makes withdrawn or corrected instructions traceable |
| Receipt/source pointer | Supports later review of dispatch, delivery and acknowledgement |

These are **proposed educational fields**. R1–R24 does not supply a real communication system, message IDs, authenticated delivery logs or a validated staff contact list. The absence of those fields is itself a preparation gap, not a reason to invent them in the canonical record.

The message ID and version are especially useful when two messages concern a changing situation. Suppose an initial approved hypothetical communication says "continue the manual queue while staff writes are paused." A later message may report a proposed resumption, conditional on reconciliation and a new service-owner decision. It is not sufficient for the later message to have a more recent timestamp: the receiver must be able to identify the current version and the exact action authority.

A valid envelope does not magically authenticate its producer. An attacker or mistaken operator can place plausible IDs in a forged message. In an actual organization, role identity and channel trust must be addressed through approved authentication and verification processes. Our offline lab models role/version checks using simple literal fields and explicitly does not perform cryptographic authentication.

### 4.19.5 Distinguish transport evidence from proof of comprehension

Imagine an approved internal instruction to the fictional front desk has been transmitted through the designated channel. The sender sees a delivery indication. The coordinator might then say, "The front desk knows what to do."

That claim is too strong without additional evidence. The delivery indicator may only show that a device or server accepted the message. It does not prove the current desk supervisor saw the content, associated it with the active shift or understood whether new bookings must remain queued.

A **role acknowledgement** should reference the exact case and message version, and it should come from the function responsible for the next step. A response from another staff member may be valuable context but does not automatically satisfy that requirement. The role rule needs to reflect the actual organization: if a documented alternate has been delegated the task, that delegation must be established, not guessed from the person's proximity to the incident.

A **read-back** asks the recipient to restate the critical operational instruction rather than merely saying "seen." For the teaching example, the distinction might be:

- Weak acknowledgement: "OK."
- Meaningful bounded read-back: "For this exercise's Branch P message, keep new booking requests in the manual queue until the service owner authorizes a verified resumption; do not treat the planned end time as automatic permission."

The read-back need not reproduce every word verbatim in a real-world design, but the acceptance criterion should identify the essential action and prohibitions. Our lab uses exact strings for determinism, not because exact string equality is a universal way to measure comprehension. A real training evaluator would review whether the recipient accurately paraphrased the essential meaning and could act under the approved process.

Even a perfect read-back does not establish that the manual queue is properly kept, that a system is paused or that booking data is correct. Those outcomes need separate operational evidence. It is possible for a person to understand an instruction yet be unable to execute it because the necessary software, authorization or resources are unavailable.

### 4.19.6 Use stage-aware messages in the Harbor Library tabletop

A useful communication rehearsal should check whether the message contains **only facts available at the checkpoint when it is supposedly drafted or issued**. An accurate later sentence may have been unavailable earlier.

At **Round A, 09:05**, the case has R1–R8 only. A suitable internal coordination message could request the training-owner task list and identify current uncertainty. It cannot mention B19 or a confirmed credential compromise.

At **Round B, 09:20**, R9–R16 may be discussed. R15 makes a bounded preservation contact urgent, but its 24-hour retention rule has no confirmed policy anchor. The message may request source availability and policy clarification; it cannot assert a specific deletion instant or that an export has been completed without a receipt.

At **Round C, 09:37**, R17–R24 may inform a proposed response option. R21 supports discussing a fifteen-minute staff-write pause but is not the actual pause approval. A message can request the proper decision and identify service costs; it cannot say Branch P has already occurred.

At the **first Round D branch release, 09:45**, select **either Branch S or Branch P**. Under S, an internal message may report the fictional session revocation, narrow quiet query and staff reauthentication, while retaining the limits on other access paths. Under P, it may report the fictional pause and two pending manual requests, but not the contents of those requests or proof of successful reconciliation. A message for one branch must not silently include the other's reported effects.

**P1/C1 and V1 arrive later**, each as its own card. Their booking mismatches and audit failure cannot be inserted into an earlier 09:45 message produced before their release. **M1/M2** are optional post-D communication injects with still later release times. If the facilitator uses them, M2 is an unverified forwarded claim and must not be converted into an established exposure report.

This stage discipline is already taught in the book's F4-AUDIT exercise. The **new** challenge here is whether the correct stage-aware message was routed, received, acknowledged and read back in the declared scope. Passing the first part does not prove the second.

### 4.19.7 Channel failure is an operational condition, not permission to broaden recipients

During a disruption, the normal coordination channel might be unavailable. A recovery plan should define **approved alternatives before the incident**. An alternative route may be an organizational telephone tree, an approved independent messaging service or a designated communications coordinator. The right choice depends on local policy, trust, confidentiality, accessibility and records requirements.

Do not improvise a fallback by forwarding restricted incident details through a personal account or an unrelated public group. A channel that remains reachable may be unsuitable for sensitive operational information. It also may be difficult to preserve evidence of what was delivered, to whom and when. The response lead should ask whether the chosen fallback supports the necessary classification of the message and whether recipient identity can be checked.

A beginner-friendly fallback plan can have three levels:

1. **Primary route:** use the approved organizational channel to the accountable role, with the prescribed message ID and version.
2. **Authorized alternate:** after the specified failure or acknowledgement condition, try a preapproved independent route to the same responsible role or its *documented* alternate, preserving the minimum necessary content.
3. **Escalation:** if the required acknowledgement cannot be obtained, report the unresolved communication state to the incident lead for a risk decision; do not infer consent.

The fallback must not be treated as successful simply because the sender clicked a second "send" control. It needs its own attempt, delivery and acknowledgement evidence. If the alternate lacks confidentiality or proper records, the message may need to be shortened to a request for contact rather than the full operational instruction.

[NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) addresses notification and coordination in contingency planning. [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) discusses training and exercises for plan capabilities. Neither source specifies Harbor Library's channels or approves sending messages on personal accounts. The specific fallback steps above are an original small-team teaching contract.

### 4.19.8 Set an acknowledgement rule without inventing a service-level agreement

An instruction may be urgent because a front-desk team needs to know whether writes are currently paused. A response lead might define a target response window for that internal role. However, the canonical Harbor Library exercise supplies **no operational messaging service-level agreement**, no contact reliability measurement and no approved fallback roster. The learner should not invent a real organization's maximum acknowledgement latency.

For a classroom rehearsal, a deadline can be explicitly marked as **hypothetical** and chosen by the facilitator as part of the fixture. The response coordinator then tracks whether the expected acknowledgement arrived by that invented time. That measures student reasoning on a supplied rule; it does not create a contractual obligation or prove the same performance in production.

The needed concepts are:

- **Deadline for the receipt:** When should a particular role acknowledge this particular version?
- **Observation cut-off:** When did the coordinator check the receipt store or exercise card?
- **Escalation condition:** What happens if there is no valid response by the declared threshold?
- **No-reply meaning:** "Unconfirmed as of the check," not "the instruction was rejected" or "approval granted."
- **Recovery of contact:** How does a later authenticated acknowledgement change the status without erasing the earlier gap?

Do not confuse response-time measurement with event-time ordering. A valid acknowledgement must refer to the message version that was actually in effect and must be associated with the expected role. A fast acknowledgement from the wrong recipient can be less useful than a slower correct one. Conversely, a correct recipient may reply after the response lead already changed the instruction; that acknowledgement is evidence concerning the **old version**, not proof that the newer instruction was understood.

An escalation route should identify who owns the risk decision when the communication remains uncertain. It should not give the coordinator unrestricted authority to interrupt a service or publicize technical details.

### 4.19.9 Version changes and delayed acknowledgements create a different hazard

A communication update may be issued because the team's recommendation or service state changed. A recipient might have acknowledged version 1, while version 2 is now the operative message. If the incident record stores only "acknowledged = yes," the coordinator may mistakenly conclude that the current instruction was accepted.

Define the receipt key as the **message ID, version and intended role**. An acknowledgement lacking one of those fields may remain usable as context but should not satisfy the current-message read-back gate without further verification.

For an explicit classroom variant, suppose a hypothetical Branch P message initially describes the paused-write workflow. A later version corrects the wording of the return condition. An acknowledgement for the earlier version proves, at most, that the older text reached someone under the stated role checks. It does not demonstrate that the recipient knows the newer condition.

A version change should therefore include a **supersedes** pointer and an explanation of what changed. If recipients may have acted on the earlier message, the coordinator should identify whether a new correction or callback is needed. Silently editing an already-dispatched draft creates a false history of what was transmitted.

Multiple messages can also cross in transit. The more recent one may arrive first, while an old retry arrives later. A robust operational plan should tell recipients how to verify which instruction is current before taking an irreversible action. The rapid course does not implement such a distributed communications system; it trains the reasoning necessary to recognize its failure modes.

This is separate from L2's revision scoring. L2 asks whether a learner's **artifact** was complete at its frozen checkpoint. The issue here is whether a **recipient** has acknowledged the *current authorized operational meaning* of a specific message version.

### 4.19.10 Retries are not evidence of more independent instructions

When delivery is uncertain, a coordinator may need to retry through an approved route. That introduces two counting problems. First, multiple attempts may refer to the same logical message. Second, the recipient may encounter duplicate copies after having already acknowledged one.

A delivery ledger should preserve **all attempts** for auditability but group them under the same message ID and version for the purpose of deciding whether the operational instruction is current. Sending the same version twice does not create two independent approvals or two separate write-pause decisions. If two attempts use different channels, each attempt retains its own routing evidence and trust limitation.

The difference is similar to the manual-queue reconciliation problem in Chapter 3, but it concerns **communications**, not business booking writes. The fact that one logical message has two attempts does not guarantee exactly-once reading or exactly-once operational execution. A later recipient who sees the retry might mistakenly perform the instruction twice unless the instruction and action workflow have appropriate safeguards.

An acknowledgement should therefore avoid ambiguous references such as "I handled your second message." It should identify the specific message ID/version and what action, if any, is proposed or already completed. The coordinator records whether the recipient's read-back was checked and whether an execution receipt is still pending elsewhere.

Retry success should also be measured honestly. If a primary attempt was never confirmed and a fallback produced a valid read-back, the ledger should retain the primary gap and the fallback success. Rewriting the whole incident communication as "delivered on first attempt" would hide the very weakness the after-action review should address.

### 4.19.11 Role identity and device delivery are not equivalent

Many organizations have roles shared across shifts. The "front desk" is an operational function, not necessarily one named person's permanent device. A response instruction might arrive on the shift mailbox when the responsible supervisor has just left. A success indicator for that mailbox says little about whether the *current accountable role* is prepared to act.

A useful route contract distinguishes three addresses:

- The **logical recipient role** responsible for the outcome.
- The **technical endpoint or contact route** used for transport.
- The **authenticated human or documented alternate** who can provide the required acknowledgement under the organization's rules.

This separation matters in a shift transition. If an old shift member replies that they read version 1, the incoming shift still may need a new handoff and valid read-back for version 2. The response lead should not infer that role continuity follows from mailbox continuity.

An alternate may be valid when appointed under an approved procedure, but not merely because another person responded first. The workbook should allow the coordinator to mark a reply from an unrelated role as **not satisfying** the required acknowledgement while still retaining it as a received message.

This is distinct from F1. F1 asks what to do when the **service owner who approves a write pause is unavailable**. Here the service owner may be available and the instruction may be valid, yet the **operational receiving role** may not have acknowledged the current direction. A failure at the reception boundary does not change who can authorize the underlying control.

An authorized functional exercise could test this with role rotation and a bounded delivery simulation. This chapter's offline lab uses literal role names without contacting any real device or authenticating a real person.

### 4.19.12 Operational handoff requires a confirmed next holder of the task

A response team may transfer an open task between shifts. A handoff note can be complete on paper yet fail operationally if nobody assumes responsibility for the next check. The sending responder should identify the exact recipient role, the current decision, the open obligations, the next checkpoint and the source pointers needed to proceed.

Use an **ownership read-back** for critical tasks:

> "I am receiving responsibility for the bounded Branch P queue review, not permission to resume writes. The two pending requests remain unverified; the service owner must decide on resumption and booking reconciliation."

This is an invented example of a good read-back *after* a Branch P release. It does not mean that the canonical two queue requests have been inspected or resolved. It confirms only that the recipient understands the pending obligation within the simulated exchange.

A bad handoff would say:

> "Writes were paused, the window probably ended, so the next shift can turn everything back on."

It invents authority from elapsed planned time and omits the service and data acceptance requirements. Even if the statement was successfully delivered, the content is unsafe. Communication delivery quality and instruction correctness are two gates, not one.

The handoff packet should also identify which planned work has **not** been approved. A transfer of responsibility does not promote an unapproved proposal to an executed action. The next responder can prepare the required request, confirm the status through the relevant owner and record a new result. The original sender's unfinished work must remain traceable.

A recipient challenge is appropriate: ask the new role holder to state one reason why the service must remain restricted or why a particular verification is still pending. A correct answer demonstrates useful comprehension in the classroom. It does not prove actual technical recovery.

### 4.19.13 Audience restrictions apply to the fallback path too

An internal operational instruction may contain details that should not appear in a patron-facing status. Sending it through a fallback channel does not change the audience classification. A communication failure is not permission to forward account names, booking identifiers or unverified exposure rumors broadly.

For the canonical case, technical owners may need to know that a specific session action was reported in Branch S. Front-desk supervisors may need instructions about permitted booking intake. Patrons may need a practical, owner-confirmed help route without the account name. The privacy contact may need to evaluate M2's **unverified forwarded claim** after its optional release. The message-delivery ledger should reflect those distinct audiences, and the fallback route must not silently expand them.

If a public status draft is approved but an approved publication channel is unavailable, the fact that the team can reach a private messaging group does not automatically make that group an acceptable substitute. The responsible communications and service owners must decide the audience and means under the organization's process. The tabletop supplies no jurisdiction or legal notification threshold and cannot decide whether a statutory notice is owed.

A safe fallback might send a minimal contact request through an approved alternate and leave sensitive details in an authorized channel. That can be operationally less informative than the original message, but it reduces the risk of disclosure through an unverified route. Record the difference: "contact requested" is not "incident details delivered," and neither is "recipient understood the operating instruction."

The extra verification requirement is not bureaucratic decoration. During a stressful incident, recipients may act on whichever message they see first. Separating role, version, authorization and channel trust prevents a perfectly formatted but misrouted instruction from becoming an avoidable additional service failure.

### 4.19.14 Contrastive worked example: delivered does not mean safely coordinated

**Incorrect fictitious conclusion after a Branch P release:**

> "The front-desk update was approved and the sending tool marked it delivered, so everyone knows the pause is active and can safely resume writes at 10:00. The message has an acknowledgement, therefore the two queued reservations must have been completed."

This makes several unsupported leaps. A delivered indicator does not identify the current operational role or prove comprehension. The acknowledgement may refer to an earlier version or an unrelated role. The planned end of the fictional fifteen-minute interval does not establish a completed resumption decision. The Branch P card reports two **pending** requests, not completed bookings. Nothing about a communication receipt supplies the business-state or queue-reconciliation evidence needed to accept full service.

**Correct bounded classroom assessment:**

> "Only after the separate Branch P card is released may the coordination note report a 09:45 fictional staff-write pause and two pending manual requests. The recipient must be reached through an approved role/channel, acknowledge the current instruction version and correctly state that requests remain queued until the service owner decides on reconciliation and resumption. If transport, role acknowledgement or read-back is missing, the coordination state remains unconfirmed and must be escalated under the prescribed exercise rule. Even a successful read-back does not prove write-path effectiveness, booking correctness or permission to resume."

This preserves three boundaries at once: what evidence was released, what communication result was checked, and what operational action still needs separate approval and verification.

In a technical incident review, a precise statement such as "the current front-desk instruction version has a valid read-back in the approved classroom route" is more defensible than "all staff were informed." The former identifies exactly what was demonstrated; the latter suggests a coverage the fixture does not measure.

### 4.19.15 An after-action review should locate the failed communication link

If the coordination process fails, the improvement plan should address the **specific link** that failed. "Communicate faster next time" is too general to test. Possible defects include an outdated contact route, missing alternate, unclear message version, absent role acknowledgement, an insecure fallback, or an instruction whose critical condition was not reflected in the read-back.

Each defect needs its own evidence:

| Observed teaching failure | Possible program improvement | Concrete retest |
|---|---|---|
| Dispatch attempted but no delivery confirmation | Verify the approved channel and escalation route | Simulate channel loss; require a recorded fallback decision within the declared exercise window |
| Delivered to a shared mailbox but role acknowledgement missing | Define an accountable shift role and accepted alternate | Run a shift-change drill with exact message ID/version read-back |
| Old message version acknowledged | Include version and supersedes reference in every critical instruction | Present delayed old acknowledgement; checker must reject it for the newer instruction |
| "OK" received without meaningful confirmation | Define the essential action and read-back question | Recipient states the pause/resumption condition correctly before acceptance |
| Unapproved fallback selected | Maintain an approved, classification-aware alternate route | Simulate primary failure; require the learner to hold sensitive detail until a valid route exists |

The exercise should make a distinction between a **working process** and a **plausible description** of that process. A roster written into a playbook is not a tested emergency contact path. A read-back field in a template is not a received read-back. An after-action ticket closes only when the declared functional or tabletop test has been completed and a reviewer can inspect the result.

[NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) offers general exercise and evaluation guidance. Its functional-exercise examples illustrate that participants can rehearse notification procedures; our precise receipt statuses and negative controls are original teaching constructs, not a direct copy or NIST pass standard.

### 4.19.16 Measure recipient coverage without fabricating a success rate

A team may report "100% communicated" after receiving one acknowledgement. That statement is meaningless without a declared set of required recipient roles and a rule for which receipts count.

For an exercise, define the **required recipient set** before sending. A narrow Branch P internal instruction might require the front-desk supervisor and service owner under a chosen fictional procedure. A privacy allegation may require the privacy contact instead, only after the M replay releases the claim. Do not count irrelevant or future roles simply to enlarge the denominator.

For each required role, track the **current message version**, permitted channel, dispatch attempt, delivery status, role acknowledgement and read-back result. If the same person acknowledges twice, do not treat that as two distinct roles covered. If the message changes, the earlier version's acknowledgement does not count for the new version. If an attempt is unconfirmed, it remains in the record as a gap.

A bounded measure might be expressed as: "Of the two roles required by the declared classroom routing rule, one provided a current-version read-back and one remained unconfirmed at the check." This still does not measure the entire organization, every shift or actual behavior. If the required recipient set was never approved, the success ratio is **not well defined**; the proper improvement is to establish the routing contract, not to guess a percentage.

Time can also be measured, but it must be interpreted carefully. A short delay to the wrong audience is not successful coordination. An acknowledged instruction with incorrect operational meaning is not a pass. A communication exercise should therefore score both the **timeliness** of an attempt and the **validity** of the receipt. These may lead to different recommendations.

Never report transport-delivered percentage as operator-comprehension percentage unless the evidence contract actually connects those measurements.

### 4.19.17 From tabletop reasoning to an authorized functional rehearsal

This rapid course exercises reasoning with synthetic records. It cannot validate the reliability of a real email service, telephone tree, emergency contact list or authentication control. A later authorized functional test would require additional procedures and safeguards.

A responsible test plan would define the exact message category, approved recipients and alternate contacts, expected channels, start and end conditions, permitted test data, minimum retained receipt metadata, participant consent or notice under the organization's policy, and an immediate stop rule if a real operational effect would occur. A message should be unmistakably marked as an exercise to prevent participants from treating it as a live incident instruction.

An observer would record what the sender did, what the transport system actually reported, which role replied, which version was acknowledged, what the recipient understood and whether any intended *separate* operational task was completed. If there was an outage, the observer should preserve the failure and escalation rather than retroactively claim the fallback succeeded. A reviewer should check whether the procedure could be performed when the usual approver or channel was unavailable, but without granting new authority that the exercise never specified.

A passing functional notification test would support only the tested participants, routes, channels and time window. It would not prove that a production incident will unfold identically, that the recipients are always reachable or that the service can be restored. The difference between a training outcome and an operational guarantee must remain explicit.

This is a useful bridge from an introductory tabletop to later technical education: describe the required signal and proof, test it in isolation, identify the condition that would invalidate the conclusion, and preserve the limits.

### 4.19.18 Section synthesis: coordination is verified at the receiving boundary

Incident coordination is not complete merely because a good message was drafted or approved. The response team needs a bounded record showing that the **right role** received the **current version** through an **approved route**, that a valid acknowledgement and read-back were obtained when required, and that unanswered contacts were escalated without inventing permission.

None of those receipts proves an account was disabled, a write pause held, a backup restored or the booking schedule corrected. Those remain separate technical and business acceptance questions handled elsewhere in the book. The added skill is to make communication failure visible before it silently becomes operational failure.

The Harbor Library release rules remain unchanged: Round A R1–R8, Round B R9–R16, Round C R17–R24, then one reported Branch S/P result in Round D, followed by P1/C1 and V1 only at their later releases; F1 and M1/M2 are independent optional variants. The communication lab below demonstrates its own invented receipt outcomes without inserting them into that history.

---

## DEL4 Offline Laboratory — Read-back and Message-Delivery Gate

**Laboratory status:** Entirely synthetic, in-memory exercise. DEL4 does **not** send any messages, authenticate recipients or interact with a booking system. The fixture selects a hypothetical Branch P communication context **after** a Branch P release; it does not assert the canonical branch occurred outside that exercise.

**Goal:** Distinguish dispatch authorization, approved channel, attempt, transport delivery, acknowledgement role, message version and read-back. Reject later-card content at an earlier checkpoint and a message belonging to the other branch. Treat missing and overdue acknowledgements as unresolved or escalated, **not** tacit consent.

**Environment:** Python 3 standard library, no files, network, email, SMS, telephone calls, credentials or side effects.

**Fixture fields:** The strings are simulated assertions; `authorized=True` represents only fictitious permission to dispatch a message, *not* approval to execute a service change. `delivered=True` is a synthetic transport field, not proof of human reception. Exact text equality implements this laboratory's narrow read-back check, not a universal natural-language comprehension test. `overdue` is a facilitator-supplied Boolean, not a measured contractual deadline.

### Reproducible Python 3 program

~~~python
RELEASE = {
    "C": 3,
    "D_BRANCH": 4,
    "D_ACCESS": 6,
    "M_REPLAY": 7,
}

def packet(
    name, release="D_BRANCH", branch="P", role="FrontDesk",
    version=2, authorized=True, channel_ok=True, attempted=True,
    delivered=True, ack_role="FrontDesk", ack_version=2,
    readback="Keep requests pending",
    expected="Keep requests pending", overdue=False
):
    return dict(
        name=name, release=release, branch=branch, role=role,
        version=version, authorized=authorized, channel_ok=channel_ok,
        attempted=attempted, delivered=delivered, ack_role=ack_role,
        ack_version=ack_version, readback=readback, expected=expected,
        overdue=overdue,
    )

FIXTURES = [
    packet(
        "C-COORD", release="C", branch="ANY", role="IncidentLead",
        version=1, ack_role="IncidentLead", ack_version=1,
        expected="Review proposal only", readback="Review proposal only"
    ),
    packet("P-NO-AUTH", authorized=False),
    packet("P-NO-SEND", attempted=False),
    packet("P-WRONG-CHANNEL", channel_ok=False),
    packet("P-NO-DELIVERY", delivered=False, overdue=True),
    packet("P-ACK-PENDING", ack_role=None, ack_version=None, readback=None),
    packet(
        "P-ACK-OVERDUE", ack_role=None, ack_version=None,
        readback=None, overdue=True
    ),
    packet("P-WRONG-ROLE", ack_role="Analyst"),
    packet("P-STALE-VERSION", ack_version=1),
    packet("P-WRONG-READBACK", readback="Resume writes now"),
    packet("P-VERIFIED-READBACK"),
    packet("S-BRANCH", branch="S"),
    packet("D-RECOVERY", release="D_ACCESS"),
    packet("M2-PRIVACY", release="M_REPLAY"),
]

def evaluate(p, checkpoint="D_BRANCH", selected_branch="P"):
    if RELEASE[p["release"]] > RELEASE[checkpoint]:
        return "FUTURE_RELEASE"
    if p["branch"] not in ("ANY", selected_branch):
        return "WRONG_BRANCH"
    if not p["authorized"]:
        return "HOLD_NOT_AUTHORIZED"
    if not p["channel_ok"]:
        return "HOLD_CHANNEL_NOT_APPROVED"
    if not p["attempted"]:
        return "READY_NOT_SENT"
    if not p["delivered"]:
        return "ESCALATE_DELIVERY" if p["overdue"] else "DELIVERY_UNCONFIRMED"
    if p["ack_role"] is None:
        return "ESCALATE_ACK" if p["overdue"] else "ACK_PENDING"
    if p["ack_role"] != p["role"]:
        return "ACK_WRONG_ROLE"
    if p["ack_version"] != p["version"]:
        return "ACK_STALE_VERSION"
    if p["readback"] != p["expected"]:
        return "READBACK_MISMATCH"
    return "READBACK_CONFIRMED_IN_FIXTURE"

for item in FIXTURES:
    print(f"{item['name']}: {evaluate(item)}")

# Two attempts at the same logical message version.
ATTEMPTS = [
    ("P-VERIFIED-READBACK", 2, "primary"),
    ("P-VERIFIED-READBACK", 2, "retry"),
]
print(
    "RETRY_CHECK attempts=", len(ATTEMPTS),
    "logical_versions=", len({(n, v) for n, v, _ in ATTEMPTS}),
    sep=""
)

assert evaluate(FIXTURES[10]) == "READBACK_CONFIRMED_IN_FIXTURE"
assert evaluate(FIXTURES[12]) == "FUTURE_RELEASE"
~~~

### Exact expected output — executed in Python 3

~~~text
C-COORD: READBACK_CONFIRMED_IN_FIXTURE
P-NO-AUTH: HOLD_NOT_AUTHORIZED
P-NO-SEND: READY_NOT_SENT
P-WRONG-CHANNEL: HOLD_CHANNEL_NOT_APPROVED
P-NO-DELIVERY: ESCALATE_DELIVERY
P-ACK-PENDING: ACK_PENDING
P-ACK-OVERDUE: ESCALATE_ACK
P-WRONG-ROLE: ACK_WRONG_ROLE
P-STALE-VERSION: ACK_STALE_VERSION
P-WRONG-READBACK: READBACK_MISMATCH
P-VERIFIED-READBACK: READBACK_CONFIRMED_IN_FIXTURE
S-BRANCH: WRONG_BRANCH
D-RECOVERY: FUTURE_RELEASE
M2-PRIVACY: FUTURE_RELEASE
RETRY_CHECK attempts=2logical_versions=1
~~~

### Worked interpretation

**C-COORD** simulates a correctly read-back Round C coordination message saying only "Review proposal only." It does not approve or execute the session restriction or write pause.

**P-NO-AUTH** blocks dispatch because the invented permission flag is false. This is a send-authorization failure, not evidence that the operational control was accepted or rejected.

**P-NO-SEND** shows that an authorized message can remain untransmitted. **P-WRONG-CHANNEL** detects an explicitly unapproved route rather than improvising delivery. **P-NO-DELIVERY** demonstrates the overdue delivery-escalation condition; the program has no evidence the recipient actually received anything.

**P-ACK-PENDING** and **P-ACK-OVERDUE** distinguish a missing acknowledgement still within the hypothetical window from an overdue missing acknowledgement. Neither status grants consent. **P-WRONG-ROLE** rejects a response from a function other than the intended receiving role. **P-STALE-VERSION** rejects an acknowledgement of version 1 for version 2. **P-WRONG-READBACK** identifies a contradiction between "Keep requests pending" and "Resume writes now"; the presence of a reply does not make the instruction safe.

**P-VERIFIED-READBACK** is the most favorable **limited classroom** outcome. It means that the fixture's declared role, version and expected string match after its assumed transport flags. It still does not prove the authenticity of an individual, the real effectiveness of a write pause, reconciliation of the two canonical Branch P requests, or approved resumption.

**S-BRANCH** prevents mixing Branch S into a selected Branch P packet. **D-RECOVERY** refuses a later V1/P1/C1-stage message at the first branch release; **M2-PRIVACY** refuses optional M2 material until its distinct later replay. The source-release checks protect the teaching scenario, not a real information system.

**RETRY_CHECK** prints two attempt records for one logical message ID/version pair. The attempts should remain separately auditable, but they do not create two independent instructions or acknowledgements. The compact concatenation of the final line results from the deliberate `sep=""` formatting in the Python fixture; it is a harmless print detail, not a missing field in the event model.

### Negative tests, safeguards and limits

Before running, predict which of the statuses would require immediate fictional escalation and which would require correcting the audience, message version or wording. The learner may change only a copy of one fixture row at a time, label the variant and rerun. For example, replacing `P-STALE-VERSION`'s acknowledgement version with 2 should allow the later read-back check to pass under its other assumptions. Replacing `P-VERIFIED-READBACK`'s message branch with S must make the same row fail in the selected Branch P context.

The code is **not** a communications platform. It cannot verify whether a message was cryptographically authenticated, whether a human read a device notification, whether an alternate channel was suitable under a real organization's privacy policy, or whether a required action was carried out. It does not connect to anything and does not send messages.

**Learner submission:** Reproduce all fifteen output lines, identify the seven distinct barriers from dispatch authorization through read-back, write a one-paragraph Branch P communication limitation statement and identify one additional source that would be needed to prove an actual approved operational outcome. A successful submission must not call the synthetic flags real delivery receipts.

**Supplementary laboratory rubric (five points):** one point for exact output; one for the approval/send distinction; one for correct role/version/read-back interpretation; one for the stage and branch exclusions; and one for evidence, security and operational-limit reasoning. The laboratory does not create a new EX039–EX050 identifier or change the canonical exercise count.

---

## Targeted Refinements to Existing Chapter 04 Exercises — No New IDs

Preserve the original twelve exercise IDs, their required formats and the book's existing 0–2 evaluation scale. These six additions address the *receiving side* of coordination, not the content-drafting or authority tests already present.

### EX039 — Role and scope card: define receiving responsibility

**Additional task:** In the existing five-row role card, add a column naming **who receives and acknowledges a critical update for each role**, and distinguish an authorized alternate from an arbitrary available person. For one role, give the question the recipient must read back and one approved response route in a hypothetical future plan. Do not invent an actual Harbor Library phone number, channel configuration or delivered message.

**Full-credit condition:** The original five responsibilities and approval boundaries remain intact. The student separates contactability from authority and identifies one source or test needed before claiming an emergency route actually works. Round A remains R1–R8 only.

### EX043 — Preservation request: delivery is not collection

**Additional task:** At Round B, distinguish three statuses for the proposed R15 retention question: preservation request drafted, request demonstrably received by the relevant custodian, and source copy actually collected and verified. Define how the incident lead would follow up if the custodian's receipt were unconfirmed, without inventing the 24-hour policy anchor or assuming a retention hold took effect.

**Full-credit condition:** The original source, bounded interval, permission and privacy fields remain present. A correctly delivered request is not called an executed export; no exact deletion deadline is fabricated.

### EX044 — Decision checkpoint: confirm proposal transmission without inventing approval

**Additional task:** At 09:37, supplement the proposal/approval/execution/verification card with a **coordination message status**: message proposed, authorized to send if separately permitted, delivered or not confirmed, and current-version role acknowledgement if supplied. State why receipt of a recommendation is not incident-lead/identity-owner approval of session revocation or service-owner approval of a pause.

**Full-credit condition:** The Round C action remains a proposal unless its separate authority is recorded. Branch S/P, P1/C1 and V1 are unavailable at this checkpoint. A valid read-back does not prove an executed control.

### EX046 — Branch P review: confirm the receiving role's understanding

**Additional task:** Only after the Branch P release, add one proposed front-desk instruction envelope containing the Branch P message version, expected receiving role and an explicit read-back that **the two pending requests remain queued until approved reconciliation**. Mark dispatch, delivery and read-back as **not supplied** unless a separate independent exercise card provides them; do not invent the two requests' identifiers or outcomes.

**Full-credit condition:** The queue-and-return note still names the service owner's reconciliation and resumption authority. The message's planned 10:00 pause end is not treated as verified automatic resumption.

### EX048 — Internal update: preserve two sentences and add a separate receipt note

**Additional task:** Keep the original **exactly two sentences** at the 09:45 **branch-only** checkpoint. Beneath the two sentences, add a separately labeled *proposed delivery-check field* with intended audience, current message version, approved route requirement and acknowledgement status. The additional field is metadata, not a third sentence of the status draft. Do not include later P1/C1/V1 findings, F1 or M1/M2.

**Full-credit condition:** The two-sentence message states only available branch facts and uncertainty. The receipt note does not claim the message was delivered or acknowledged without supporting evidence.

### EX050 — Final handoff: keep open communications obligations visible

**Additional task:** After the chosen branch and later P1/C1 and V1 releases, add one row to the final handoff showing an **unconfirmed receiving-role instruction** and the next authorized escalation or read-back requirement, if no such receipt is supplied. The six-output self-score and approval/evidence critical gates remain separate; do not automatically lower the original rubric just because an independent delivery test was not part of the supplied canonical case. Identify what a future functional exercise would have to measure to close the communications capability gap.

**Full-credit condition:** The existing booking and audit failures remain explicit; a communication receipt is not presented as restored service, and a missing reply is not classified as consent.

---

## Supplementary Worked Answers — For the Final Appendix of the Principal Book

### EX039 — Additional worked reasoning

The incident lead, analyst, service owner, recovery lead and communications contact retain the chapter's existing responsibilities. A receiving-route extension can say, for example, that the **incident lead** must acknowledge a bounded action-decision request and that a **front-desk supervisor** would acknowledge an approved operational intake instruction *if one is later issued*. The role and its documented alternate must be specified before a real exercise. A message reaching a shared mailbox does not establish the current accountable supervisor's comprehension. For a fictional plan, the read-back might require the recipient to state the message ID/version and the unresolved booking-intake condition. No real route is validated by the R1–R8 snapshot; the card remains a proposed readiness contract. The learner must not elevate the role receiving a message into the role authorized to approve a service disruption.

### EX043 — Additional worked reasoning

At Round B, R15 creates a time-sensitive preservation question but not a verified deletion deadline. The incident lead can draft an authorized, bounded request for the application custodian that identifies relevant audit source, selection, retention-policy anchor, minimal fields and access scope. **Request prepared** is one status. **Custodian receipt confirmed** would require a separate credible acknowledgement for that request/version; no such receipt exists in R9–R16. **Collected/verified** would require a distinct export or preservation receipt and the proper copy checks, likewise not supplied. If acknowledgement is missing, the lead should follow the organization's approved escalation route and record the gap rather than assume a hold was placed. The request's delivery, even if later proved, would not establish that deletion stopped or that the source was complete.

### EX044 — Additional worked reasoning

At 09:37, R17/R18 support reconsidering the unexplained B20 activity, while R19 and R21 inform possible controls. A **coordination message** to request identity-owner review may be drafted and potentially authorized for transmission, but the action still requires the separate incident-lead and identity-owner decision under the fictional rules. A hypothetical delivery or acknowledgement of that request is not a revocation receipt. R21 remains a tolerability statement, not approval or execution of a write pause. No canonical communication transmission or role read-back is supplied at Round C, so those fields remain **not reported**. The actual protective and legitimate-service tests also remain proposed. Later Branch S/P cards must not be inserted into the frozen 09:37 action.

### EX046 — Additional worked reasoning

Only within the subsequently released **Branch P** can the learner report the fictional staff-write pause at 09:45 and **two pending** manual requests. An appropriate proposed front-desk envelope should reference the chosen P branch, an exact version, the front-desk receiving role, an approved internal route and a required read-back: maintain pending intake and do not treat the planned 10:00 time as unconditional resumption approval. No message delivery, queue-entry identity or recipient acknowledgement is recorded by the branch card, so these must remain pending in the new communication ledger. The service owner still must approve and verify reconciliation and resumption. W1, MQ3, P1/C1 and V1 are separate fixtures and cannot supply the two unnamed Branch P requests or the missing communication receipt.

### EX048 — Additional worked reasoning

**Branch S — original two-sentence internal message:**

> "At 09:45 UTC, Harbor Library is reviewing unexplained booking edits, and the fictional identity administrator reports the identified `desk-a` session was revoked, with staff reauthentication required. The incident lead and service owner will check the limited booking evidence and front-desk impact at the next checkpoint, while the cause and wider effects remain unconfirmed."

**Branch P — original two-sentence internal message:**

> "At 09:45 UTC, Harbor Library is reviewing unexplained booking edits, and the fictional service owner reports a fifteen-minute staff-write pause with two requests pending in a manual queue. The incident lead and service owner will review permitted intake and queue obligations before any resumption decision, while the cause and wider effects remain unconfirmed."

**Separate proposed receipt note, not part of the two sentences:** "Recipient role: current front-desk supervisor; message version: to be assigned under an approved route; dispatch/delivery/role acknowledgement: not supplied; read-back to request: current intake and return-to-service condition." P1/C1 and V1 are deliberately excluded because EX048 occurs before those cards' release. The message is a classroom draft, not a delivered operational instruction.

### EX050 — Additional worked reasoning

A final Branch S or Branch P handoff must still distinguish the frozen Round C proposal from the later **reported** fictional branch action, preserve P1/C1's B19/B20 mismatches and V1's failed audit actor, and identify the unresolved cause and responsible owners. If the learner adds a communications row, it should say that **no authenticated current-version role acknowledgement has been supplied in the canonical case**. A later authorized functional rehearsal could test an approved channel, recipient role, message-version acknowledgement, meaningful read-back and escalation after a simulated channel failure. That proposal does not change the learner's original six-artifact scoring denominator or invent a new recovery pass. The case remains open on the evidence actually supplied, and the communication preparedness question is a distinct improvement item rather than proof that a real message failed.

---

## Synthesis and Continue Studying

The new skill is **communication delivery assurance within a bounded incident-response process**. A defensible internal message still needs the correct stage and source boundary, permission to send, approved audience and channel, delivery/acknowledgement evidence where available, version-consistent read-back and escalation when any critical link remains unconfirmed.

A successful DEL4 classroom classification proves only the internal logic of its invented input flags. It does not prove the authenticity of a real recipient, technical execution of a containment measure, correct bookings, successful recovery or freedom from exposure. Those conclusions require their own authorized observations.

### Continue studying — chapter 04 of 04 (public supplementary draft)

[← Chapter 03](../MANUSCRIPT.md#ch-03) · [Course chapter index](../../SUBJECTS.md) · [Principal manuscript and worked answers](../MANUSCRIPT.md#answers) · [Next course via the chapter index](../../SUBJECTS.md)

**Editorial integration reminder:** This file is a **transitional component** of the existing Chapter 04, not a separate fifth chapter or new numbered exercise set. Consolidate accepted teaching, exercise refinements and gabaritos into the one public `MANUSCRIPT.md`; perform independent review and A4 measurement after integration. Do not infer manuscript completion from page length or exercise count alone.

### Primary sources and rights

- [NIST SP 800-61 Revision 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025 final; the RS.CO incident-response communications context supports preparing appropriate stakeholder coordination, not DEL4's invented receipt states.
- [NIST SP 800-34 Revision 1, updated edition — Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). Updated November 2010; contingency activation, notification and coordination context, not a claim that Harbor Library used any channel.
- [NIST SP 800-84 — Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities](https://csrc.nist.gov/pubs/sp/800/84/final). Final September 2006; exercise design, conduct and evaluation, not a prescribed DEL4 scoring rule.

The primary works remain third-party publications subject to their own rights. The message envelopes, statuses, scripts, rubrics, example communications and all Harbor Library/DEL4 artifacts are **original synthetic instructional material**. Editorial responsibility is assigned only to [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned content follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE) within the stated limits. No real communication was sent and no production system was accessed.
