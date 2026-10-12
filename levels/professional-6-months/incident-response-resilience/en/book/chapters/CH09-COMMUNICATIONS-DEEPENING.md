# Chapter 09 supplementary teaching component — Evidence-bound communications and privacy escalation

> **Editorial status: PUBLIC DRAFT — TRANSITORY COMPONENT, NOT AN ADDITIONAL CHAPTER.** Proposed for integration into [Chapter 9 of the English professional manuscript](../MANUSCRIPT.md#ch-09). It extends the existing teaching and EX041–EX045 answer reasoning; it does not replace or renumber them. Cedar Training Network (CTN), records C01–C33 and V9 are fictional training devices.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned work and the preserved rights of cited sources are governed by [RIGHTS.md](../../../../../../RIGHTS.md).

## Outcomes and evidence-release boundary

A supervised learner completing this component can (1) build separate service and potential-data-impact claim ledgers; (2) evaluate what a negative queue observation does and does not exclude; (3) minimize access to sensitive fields while retaining a usable investigation plan; (4) create status messages with audience, owner, approval and next-update state; (5) version a correction without rewriting history; and (6) defend the existing EX041–EX045 worked answers.

At **10:45 UTC**, C30 supports only a *limited, monitored* return of the S42 enrollment service, accepted by the service owner after earlier C29 production checks. Two additional hours of observation are assigned, not already completed. **C31 does not yet exist** at that checkpoint. At 10:48 C31 introduces a staging batch, mail-sync-04, with twelve pseudonymous recipient tokens; the batch creation timestamp is 10:47. At 10:52 C32's privacy steward opens a scoped review, explicitly restricting token-to-contact mapping. At 11:00 C33 reports the twelve entries **not-dispatched in the internal queue** and a **10:49–10:51 gap in the inspected external gateway log**. None of these cards identifies twelve people or proves an external delivery.

### 9.A Different decision tracks require different epistemic status

A **service status** describes the observable condition of a business function. A **data-impact assessment** asks whether particular information was accessed, altered, transmitted, retained or exposed, and what those facts mean under applicable rules. They need different evidence, decision owners and deadlines. Service recovery can proceed while data questions remain open; a possible data signal can require escalation even when a service is operational. Treating “application back online” as a privacy verdict makes an unsupported leap.

At 11:00 the service claim is relatively narrow but concrete: C29 reports a bounded production correction, and C30 reports fifteen minutes of monitored operation followed by owner acceptance. The data question is more conditional: C31 provides a token count and internal queue event; C33 provides a scoped queue status and a missing interval in another source. A single narrative that says “we restored the service and no records were sent” misuses the confidence of the first track to answer the second. An equally poor statement says “we found a twelve-person breach” because it promotes token count and a log gap into identified victims and external transmission.

Use the following claim ledger rather than a single severity label:

| Claim at 11:00 | Evidence that supports it | Evidence that does not exist here | Owner of next decision |
|---|---|---|---|
| S42 accepted for limited service return at 10:45 | C29 production receipt and checks; C30 monitored interval and service-owner acceptance | Proof of unlimited stability, root-cause attribution or completed future monitoring | Service owner and response lead |
| Twelve pseudonymous entries staged in one queue batch | C31 scoped telemetry | Verified person mapping, message body or external recipient delivery | Queue custodian and privacy steward |
| The inspected internal batch entries were not dispatched by that queue | C33 scoped status | Complete cross-system absence of sends; certainty about external gateway gap | Queue/gateway custodians |
| A privacy and legal determination is required | C32 opens review and restricts mapping | A statutory jurisdiction, classification, affected-person count or notification deadline | Authorized privacy and legal decision owners |

The distinction between **not observed** and **observed not to occur within a validated scope** is essential. A complete, source-authoritative negative record for a specific event type may support absence *within that declared coverage*. Here, C33's queue status is bounded and the gateway has a gap. The team can report the queue's status accurately without promoting it to a universal “no transmission anywhere” assertion.

### 9.B Analyze the event path before interpreting “sent”

An outgoing notification may be represented at several stages: created, staged, selected for dispatch, submitted to a gateway, accepted by an external provider, delivered to a recipient mailbox and read by a person. These states are **not interchangeable**. A queue row that says not-dispatched describes one internal state; a gateway acceptance event, if later authenticated, would describe another stage. Neither necessarily proves end-user delivery or content disclosure without compatible semantics and scope.

For mail-sync-04, the learner should draw a **hypothetical flow**, not a purported CTN architecture diagram: producer → internal staging queue → dispatcher → gateway → external system. Mark only C31's staging and C33's reported queue status as observed. Mark the gateway interval 10:49–10:51 as unobserved due to the declared log gap. Mark dispatcher behavior, alternate export routes, contact mapping, content and external delivery as unknown. If the learner draws an arrow labeled “sent to twelve learners,” ask which supplied event proves it. None does.

The correct next evidence request is discriminating and bounded. Ask the gateway custodian for a source covering the gap or an independent authenticated receipt, the identifier-join semantics between mail-sync-04 and gateway transactions, and its retention limits. Ask the queue custodian what not-dispatched means operationally and whether retries, duplicate messages or parallel dispatch processes use other records. Every requested field must serve a decision question. This is not authority to browse the entire notification database.

The difference between event time and case-receipt time also matters. C31's event creation is 10:47 and its case release 10:48. C33 arrives at 11:00 after a scoped review; its gateway gap covers an earlier window. The response team must not describe information first received at 11:00 as though it was known at 10:45. A good status note states **as-of time** and **evidence horizon** so a later reviewer can reconstruct why a message took a particular form.

### 9.C Privacy minimization is an investigative discipline, not inaction

A restricted mapping between pseudonymous tokens and real contacts may be sensitive; unmasking it can generate another unnecessary copy of personal information. Before requesting it, the learner should state the **purpose**: would individual identification actually change a legal decision, contact duty or containment action? If the next question is only whether an outbound gateway transaction occurred, a bounded batch identifier and event metadata may suffice. If person-level mapping later becomes necessary, the privacy steward should authorize the fields, custodians, secure storage, retention and access list under the applicable policy.

Data minimization also improves evidence quality: fewer unnecessary fields mean fewer ambiguous exports, fewer uncontrolled reproductions and a clearer provenance trail. Record the exact query range, source version, collector authority, output count and known gaps. Do not paste contact details into public incident timelines or classroom exercises. A responder can preserve raw source artifacts in restricted custody while placing a redacted reference in the coordination note.

The [NIST Privacy Framework](https://www.nist.gov/privacy-framework) provides a risk-management reference for identifying and managing privacy risk. It does not determine the legal status of a particular CTN token or impose a universal notification clock. The older [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) provides forensic data-handling context and explicitly is not legal advice. A response analyst must refer classification, preservation holds, contractual notice obligations and regulatory decisions to authorized legal and privacy owners rather than inventing a jurisdiction.

A preservation escalation should state **what might be lost**, not assert that a legal hold automatically exists. For example, the queue and gateway custodians may need to preserve original records and their query-range metadata pending the privacy steward's assessment. Counsel or the designated records authority determines whether a formal preservation duty applies and to which systems, periods or custodians. The analyst can identify a potentially disappearing source but cannot issue a legal conclusion solely on the basis of C31.

### 9.D Communication has a workflow separate from drafting

A message passes through distinct states: **drafted → technically reviewed → privacy/legal reviewed where applicable → approved for a named audience → dispatched through a named channel → receipt/confirmation recorded → superseded if necessary**. Any skipped stage must follow a real emergency procedure; a draft's existence is not authorization to send it. A message may also be explicitly withheld because the evidence is inadequate. This state model prevents a responder from interpreting an unsent holding message as proof stakeholders were told.

Each message needs a small release manifest:
- **Audience and business purpose.** Internal responders need actionable source references; learners need a clear service effect and useful next step.
- **As-of time and claim sources.** Service claims cite C29/C30; potential-data claims cite C31–C33 with their limitations.
- **Restricted content check.** Remove account labels, recipient tokens, internal endpoints and speculative causal claims from public drafts.
- **Owners and approval states.** Service owner approves business wording; communications owner approves release; privacy/legal owner reviews any data-related statement within their remit.
- **Next-update obligation.** Give a definite status checkpoint, not a promised outcome, and a route for revisions.

**Appropriate restricted draft at 11:00:** “CTN-IR-014: S42 was accepted for limited return at 10:45, with continued owner monitoring. A 10:47 staging event identifies twelve pseudonymous entries in batch mail-sync-04. The scoped internal status reports not-dispatched, but the inspected gateway has a gap from 10:49 to 10:51. Neither external dispatch nor lack of all other transmissions is established. Privacy steward owns the bounded gateway/queue follow-up and will advise whether token mapping is necessary. Incident lead will issue the next status at 12:00. This note is an internal draft and has not been dispatched.”

**Appropriate learner-facing draft:** “A class enrollment slot was temporarily unavailable. CTN completed initial service checks and returned that slot to use at 10:45 UTC. Enrollment monitoring and review continue. No action is requested from learners based on this service update. We will share another status by 12:00 UTC through this channel.” This version intentionally omits the unresolved queue signal, because that data matter is not yet assessed or approved for public characterization. It is **pending service-owner and communications approval and is not sent**.

**Incorrect public draft:** “We have fully restored all services, confirmed twelve people's data are safe, and concluded no breach occurred.” The first clause exceeds the limited return; the second invents identities and a safety conclusion; the third makes an unauthorized legal/data determination despite an incomplete evidence window. A reviewer's task is not to make this shorter but to make every retained claim source-bounded and operationally useful.

### 9.E Correction and historical honesty when a later record appears

Variant **V9** is a separate exercise branch, **not another main CTN C card**. In V9 only, an authenticated gateway receipt associated with mail-sync-04 arrives at **11:20**. A learner should version the 11:00 internal note as v1 preserved and a new 11:20 note as v2, stating the receipt is new and needs its own semantic verification. A gateway acceptance could conflict with the previously inspected internal queue state without meaning the original queue observation was fabricated; records can describe different process steps, views or timestamps.

A correct V9 v2 note states what the authenticated receipt names, distinguishes **gateway record** from **person-level delivery**, requests the metadata to validate batch linkage and intended recipients, and returns the message decision to the privacy and communications owners. It must not silently replace v1 or backdate 11:20 evidence to 11:00. It also must not claim “the twelve people received it”: V9 supplies no recipient mapping or delivery confirmation.

If an approved learner-facing message had already been sent, the correction workflow would ask for its released version and whether recipients need an update. In the supplied CTN main case, the learner-facing text remains a draft. A simulated approval request in V9 should therefore be labeled **request for review of a possible revision**, not “corrected notice sent.”

The **12:00 UTC checkpoint** is an obligation to communicate a status, even if the data inquiry is still unresolved. A legitimate update can say the review continues and name the next checkpoint. The owner should never imply that an assessment's conclusion is guaranteed by an update time.

### 9.F Offline laboratory: fail-closed draft release checks

**Objective:** demonstrate that a message record with no approval cannot be marked released. **Inputs:** two invented unsent message records and a deliberately conservative local rule. **Environment:** Python 3, no network, files, queue or personal information. **Output criterion:** both draft statuses must be blocked. The code tests a **training workflow property**, not CTN's actual messaging system or a legal approval engine.

~~~python
messages = {
    "internal": {"approved": False, "sent": False, "token_map": False},
    "learner": {"approved": False, "sent": False, "token_map": False},
}
for name, record in messages.items():
    result = (
        "BLOCK"
        if not record["approved"] or record["token_map"]
        else "REVIEW"
    )
    print("C9", name, "release=" + result)
~~~

**Executed output:**

~~~text
C9 internal release=BLOCK
C9 learner release=BLOCK
~~~

The flag token_map signifies unnecessary mapping detail in this simple fixture; in a real restricted message, the lawful and approved inclusion of identifiers would need a much richer rule. Even a printed REVIEW would **not** mean dispatched: the code never sends anything and does not inspect the sent field as a completed workflow. A safe variation changes approved to True in an isolated record, then explains why a second release-owner decision and a dispatch receipt would still be needed. The test prevents casual claims of transmission; it is not an access-control system.

### 9.G EX041–EX045: targeted expansions and worked results

**EX041 — two-track ledger extension.** Require an **as-of 11:00** column and different owners. Worked service row: C30 limited return accepted at 10:45 with remaining monitoring, owner service/incident lead. Worked data row: C31 staged twelve pseudonymous entries, C33 internal status not-dispatched but external gateway gap; owner privacy steward with queue/gateway custodians, scope and delivery unresolved. A response that combines these into “incident resolved” or “twelve victims” fails evidence discipline.

**EX042 — restricted internal note extension.** Add a required field: “Which observation could change the conclusion?” A strong 100–160-word draft cites C30 separately from C31–C33, names the batch as an internal event, distinguishes no send receipt from proved nondelivery, requests a bounded gateway check and gives a 12:00 status checkpoint. The worked result should retain **not-dispatched for the inspected queue**, **gap in the inspected gateway source**, and **external transmission unconfirmed** simultaneously.

**EX043 — learner-facing update extension.** Require the learner to annotate each sentence with its evidence source or audience function in an *editor's side table*, not in the public message itself. Service effect and 10:45 limited return derive from C29/C30; no action requested is a proposed user instruction needing owner review; the 12:00 promise is a communication schedule, not a completion deadline. The draft stays **unsent** until designated approvals. A phrase guaranteeing no data impact earns no credit.

**EX044 — privacy referral extension.** The five questions should distinguish (1) token semantics and necessity of identifying contacts; (2) the queue's not-dispatched state; (3) the gateway gap and an independent discriminating source; (4) preservation/retention scope; and (5) authority for impact and notice decisions. Model request: “Please authorize only batch-linked metadata and the missing gateway window, with source identifiers and collection limits.” A full contact-list export or a self-issued legal conclusion is inappropriate.

**EX045 — V9 correction extension.** Preserve the 11:00 v1 and append an explicitly **V9-only** v2 at 11:20 describing the authenticated gateway receipt. The proposed message review asks whether receipt semantics and recipient scope change release wording; it does not assert end-user delivery or twelve identified people. Award full credit for maintaining a version diff, owner approvals pending and no retroactive rewrite of C33's earlier scoped observation. V9 must never be imported as a fact of the main CTN sequence.

### Synthesis, limitations and primary references

The offline code proves nothing about delivery or CTN approvals. The case provides no mapped recipient identities, no complete external gateway window and no applicable legal jurisdiction. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) provides current response-coordination context; the [NIST Privacy Framework](https://www.nist.gov/privacy-framework) offers risk-based privacy management; and [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) describes evidence-handling considerations but does not supply case-specific legal advice.

**Synthesis:** communicate what a source says within its scope, say what remains unknown, name the owner of the next discriminator and track whether words were only drafted, approved or actually transmitted. Recovery and possible data exposure move on different decision clocks.

### Continue studying — supplementary component for chapter 09 of 12

[← Chapter 08 (authored draft)](../MANUSCRIPT.md#ch-08) · [Course chapter index](../../SUBJECTS.md) · [Chapter 10 (authored draft) →](../MANUSCRIPT.md#ch-10)

Review [principal Chapter 09](../MANUSCRIPT.md#ch-09) for the original EX041–EX045 prompts and the [single worked-answer appendix](../MANUSCRIPT.md#worked-answers) for existing answer order.
