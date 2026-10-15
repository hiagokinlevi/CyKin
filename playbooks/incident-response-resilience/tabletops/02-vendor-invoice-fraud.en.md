# TableTop 02 — Vendor invoice fraud: an urgent bank-change request before payment

**Edition:** English · **Exercise ID:** TTX-VIF-02 · **Catalog scenario ID:** vendor-invoice-fraud · **Edition date:** 2026-10-15  
**Editorial status:** Original fictional defensive exercise; independent human and technical review remain pending.  
**Audience:** Accounts payable, finance, treasury, procurement, supplier liaison, SOC, messaging/endpoint operations, legal/privacy, communications and executive incident command.  
**Format:** Paper-only facilitated incident simulation, 15-minute briefing, 90-minute timed rounds and 25-minute debrief. A participant may combine roles in a small class, but decision authorities must remain independent.  
**Scope:** This document expands the existing [scenario 02 in the ten-entry catalog](../../../web/tabletop/scenarios.json), rather than adding a catalog entry, a book chapter, a quiz bank or a deployed website feature. See [primary sources and rights](#12-primary-sources-and-rights) and the [incident-response playbook index](../README.md).

## 1. Fictional context, safety and learning contract

**All organization names, people, service paths, source events, payment records, messages, times, indicators and outcomes below are invented teaching fixtures.** No live vendor, bank, email account, invoice or employee is involved. All domains end in the reserved **.example** top-level domain; account labels are fictional tokens, not routing instructions. Do not send a payment, contact real suppliers, forward suspicious material, click embedded links, open attachments, test credentials, change mailbox configuration or disclose personal data to run this exercise. In a real incident use the organization's authorized incident and payment processes.

Fictional **Eastbridge Medical Logistics (EML)** distributes time-sensitive sterile supplies to healthcare customers. Its procurement team depends on fictional critical supplier **Meridian Care Supply**. A previously approved invoice, **INV-7742** for **USD 286,400**, is queued for the **14:30 UTC** payment cutoff. The approved beneficiary token in the vendor master and last verified payment record is **BANK-OLD-42**. Neither the amount nor the time makes an urgent account change legitimate. A plausible email requests **BANK-NEW-99** hours before cutoff, seemingly from the supplier, with a similar-looking domain, a different Reply-To address and an attachment an AP employee has already opened. The bank-change request is a **suspicion**, not a consummated fraud, confirmed compromised mailbox or diverted payment.

The training challenge is to stop an unsupported beneficiary change **without pretending that a delayed payment is free of service cost**. The team must maintain supply continuity, limit possible endpoint/email exposure, protect evidence, contact a trusted supplier representative through a channel independently obtained **before** this message, and preserve financial controls under executive pressure.

### Six observable objectives

1. **O1 — Govern the payment:** prevent an unverified master-data change or release while naming AP, procurement, controller and treasury rights, conflict-of-interest controls and timeboxes.
2. **O2 — Detect with source discipline:** distinguish display name, From, Reply-To, envelope sender, authenticated domain, approved vendor identity and actual instruction authority.
3. **O3 — Contain and preserve safely:** retain the original message, full headers and attachment without re-opening active content; track the employee's exposure and unresolved execution question.
4. **O4 — Verify independently:** use a pre-existing supplier contact and a recorded callback, separate supplier confirmation from two distinct internal approvals and from evidence of payment execution.
5. **O5 — Scope mailbox and financial risk:** discriminate lookalike impersonation, genuine delegated change, and internal/supplier account misuse without claiming any is proved by a lone indicator.
6. **O6 — Recover and learn:** specify safe release/hold criteria, bounded mailbox remediation if indicated, exact payment-state reconciliation, reviewed communications and measurable improvements.

### NIST SP 800-61 Rev. 3 / CSF 2.0 mapping

[NIST SP 800-61 Rev. 3 (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates incident response with [NIST CSF 2.0 (February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final). The current approach is **not** the retired Rev. 2 four-phase checklist: **Govern, Identify and Protect** establish risk, roles and safeguards; **Detect, Respond and Recover** describe incident-related outcomes, with continuous improvement. This tabletop's phases, timing, rubric and delegated authorizers are **original classroom choices**, not a compulsory NIST transaction workflow.

| Exercise phase | Relevant CSF 2.0 functions | Evidence-based decision |
|---|---|---|
| Vendor record, bank-change policy, authority matrix, cutoff and fallback | Govern / Identify / Protect | What was approved before an unexpected email? |
| Suspicious message, opened attachment, header differences | Detect | Which signals actually support impersonation or compromise hypotheses? |
| Payment hold, source preservation, trusted callback, bounded technical investigation | Respond | Which action is justified, who may approve it, and how will its effect be checked? |
| Release only after supplier + internal verification; conditional mailbox recovery and payment reconciliation | Recover | What independent receipts prove the desired state, and what remains unknown? |
| After-action control drill and signed policy retest | Identify / Govern | Could a new team detect and prevent the same weakness? |

**Primary-source boundaries:** [FBI BEC guidance](https://www.fbi.gov/how-we-can-help-you/common-frauds-and-scams/business-email-compromise) recommends independent verification of altered bank details; the [FBI IC3 BEC public advisory](https://www.ic3.gov/PSA/2016/PSA160614) explicitly distinguishes previously known telephone numbers and secondary sign-off from contact information in an email. [NIST SP 800-177 Rev. 1](https://csrc.nist.gov/pubs/sp/800/177/r1/final) describes SPF, DKIM and DMARC as sending-domain authentication mechanisms; passing them **does not** grant authority to redirect this customer's funds. The fictional role charter below is not a legal determination for any real payment or jurisdiction.

## 2. Teams with named decision rights

These are **simulated delegations** for a classroom; actual signing limits, audit duties and bank rails must come from current institutional policy. A person cannot approve both sides of a two-person control by role-play, and executive urgency cannot substitute for the authorization ledger.

| Named role / team | Authorized simulated work | Cannot authorize or conclude |
|---|---|---|
| **Nadia Flores — Accounts Payable (AP)** | Receive/triage invoice; apply hold to the bank-change request and affected pending batch; preserve original invoice; initiate a change ticket with evidence | Change beneficiary from email alone, self-approve or assert settlement from a queued item |
| **Owen Malik — Finance Controller** | Decide financial-control exception handling and, once evidence is complete, act as first independent authorized internal approver | Override supplier callback, silently replace BANK-OLD-42 or count his approval twice |
| **Grace Bell — Treasury / Payment Operations** | Independently authorize a verified beneficiary destination as second approver; check payment register/bank status and stop or initiate a permitted transfer | Treat a schedule/cutoff as proof of execution; bypass AP/controller segregation |
| **Felix Chen — Procurement / Vendor Master Owner** | Retrieve the vendor contact and approved banking baseline from the *pre-existing* signed register; independently organize supplier verification | Certify bank control merely from the incoming message or sign for the supplier |
| **Leila Okafor — Meridian Care Supply, pre-existing supplier liaison** | Answer only a callback placed to the number in the prior vendor register; attest supplier instructions and the supplier's records **within what she knows** | Approve EML's internal controls, attest bank ownership without her approved supplier process or release EML's payment |
| **Theo Park — SOC Incident Commander** | Open the cyber case, prioritize hypotheses, authorize proportionate SOC investigation within policy and set reassessment triggers | Release money, designate a sender as criminal from lookalike text, or declare mailbox intrusion without evidence |
| **Jonas Silva — SOC Evidence Custodian** | Secure original MIME, envelope/authentication and messaging/endpoint logs through permitted read-only exports, chain of custody, hashes and access control | Open a suspect file in the employee's mailbox, treat an attachment preview as executed malware or invent telemetry |
| **Marta Ruiz — Messaging / Endpoint Infrastructure** | Confirm available log coverage, propose reversible user/session/device actions and independently check authorized changes | Reset/disable every account or erase evidence without proportionate authorization and service review |
| **Isabel Cole — Legal and Privacy** | Preserve sensitive records, determine applicable assessment, reporting, law-enforcement and data-notice questions from substantiated facts | Call an attempted BEC a legal breach or assign a universal reporting deadline from classroom signals |
| **Dana Moore — Communications** | Draft bounded supplier/internal notices and record reviewer, approval, delivery and acknowledgment status | Publish "funds stolen," "account hacked," or "supplier guilty" on conjecture |
| **Evelyn Hart — Executive Incident Sponsor** | Set risk escalation, resource allocation and supply-continuity priorities; ask for escalation to banks or counsel **if facts justify** | Remove dual control or independent callback because a critical supplier is urgent |
| **Jordan Reed — Neutral Facilitator and Scoring Observer** | Release signed synthetic cards; time and freeze artifacts; score against pre-announced evidence | Change a card after release, simulate a real mailbox action, invent a callback result or coach the scored decision |

**Distinct gates:** (a) *Supplier authenticity* from the **pre-registered contact**; (b) *AP/vendor-master reconciliation* by Nadia and Felix; (c) *dual internal financial approval* by Owen **and** Grace; (d) *bank batch execution* by an authorized operator; (e) *independent banking/payment-register readback*. Each gate needs its own case receipt and scope. Supplier contact does not approve the customer's money movement; two internal signatures cannot retroactively validate an unverified supplier request.

## 3. Participant packet, clocks and hypothesis discipline

The facilitator gives each team the **blank** ledgers, previously signed vendor-master excerpt and role charter, but withholds cards VF-01 to VF-09 until the assigned exercise minute. **VF-00 alone is initially available.** Cards show fictional event times in UTC, which must not be mistaken for exercise release minutes or participant decision times. Record three separate clocks:

- **Case/event time:** what a source says happened, possibly with timezone, device or ingestion offset.
- **Facilitator release minute:** when participants were entitled to see a specific card.
- **Freeze time:** when the team committed a position before the next card.

A later card describing an earlier event is **not** evidence the team knew it then. Distinguish **observation → competing hypotheses → missing discriminator → selected action → named authority → independent verification → consequence/next trigger**.

**Fixed competing hypotheses at start:** H1: a lookalike-domain impersonator sent a fraudulent instruction without mailbox access; H2: a genuine vendor change was sent via an unexpectedly delegated but unverified domain; H3: AP or vendor mailbox access was abused; H4: a harmless but abnormal internal process/request was mishandled. These are analytical alternatives, **not equal-probability claims** and not conclusions. Log which card would weaken or support each one.

**Stop card:** "Do not change live supplier details, wire money, reply to suspect sender, call email-provided contact, replay/open the attachment, reset a real mailbox, expose genuine customer data or perform a live technical test." Pause and document any unsafe proposal. Evidence must be synthetic or authorized, read-only and minimized.

### Minimal frozen decision record

| Field | Requirement |
|---|---|
| ID / clock | Decision ID, fictional case checkpoint, exercise minute, person recording |
| Evidence | Released VF IDs, source reliability, observation versus interpretation, missing facts |
| Options | At least two alternatives, payment/supply cost, uncertainty and what observation discriminates |
| Rights | Supplier proof; AP/vendor-master owner; controller; treasury; SOC/IT (as relevant), **separate** |
| Status | Proposed / approved / simulated executed / independently verified / released or held |
| Safeguards | Preservation, privacy, rollback or hold expiry policy, next trigger and owner |

Sample frozen entry **D-03**: "At exercise minute 28, only VF-00 to VF-03 are available; hold BANK-NEW-99, inspect already-approved master BANK-OLD-42, request callback via supplier master, preserve raw message; proposed=recorded, AP-hold=simulated, verified-hold=pending; controller/treasury release not approved; review after signed callback." Even if later proof arrives, preserve D-03 and create a later revision, not a retrospective edit.

## 4. Progressive injects: facilitator release ledger

The facilitator uses a **90-minute exercise clock** plus a separate 25-minute debrief. Event times are **fictional** UTC; exercise minutes are lesson pacing, not elapsed incident time. Later card content is forbidden in earlier frozen decisions.

| Exercise minute | Card (case time) | Teams prompted | Required frozen output |
|---:|---|---|---|
| 0–8 | VF-00 (08:45 baseline) | AP, Finance, Procurement | Baseline, criticality, known contact, authority map |
| 9–19 | VF-01 (09:06 email), VF-02 (09:14 opened) | AP, SOC, IT | Incident opening and immediate hold/preservation proposal |
| 20–31 | VF-03 (09:23 payment-state snapshot) | Finance, Treasury, Procurement | Hold readback, vendor-master and invoice comparison |
| 32–43 | VF-04 (09:36 headers/authentication) | SOC, IT, AP | Evidence analysis, alternate hypotheses and copy policy |
| 44–55 | VF-05 (10:02 verified contact record) | Procurement, supplier, Finance | Callback challenge, unanswered-contact branch and routing |
| 56–67 | VF-06 (10:19 supplier callback statement) | Supplier, AP, Controller | Reassessed beneficiary and approval posture |
| 68–79 | VF-07 (10:44 mailbox audit), VF-08 (11:02 endpoint view) | SOC, IT, Legal, Communications | Bounded access/attachment inquiry and message draft |
| 80–90 | VF-09 (14:15 cutoff checkpoint, **released late**) | Treasury, Executive, observer | Final release/hold decision, acceptance gates and debrief snapshot |

### Prebrief — VF-00: the baseline (minute 0)

**Supplied, fictional 08:45 UTC:** INV-7742 is queued for 14:30 UTC. Vendor-master signed snapshot **VM-2026-10-13** lists "Meridian Care Supply," approved account token **BANK-OLD-42**, approved supplier callback reference **VC-17** (obtained months before this exercise) and purchasing owner Felix. Invoice amount USD 286,400; associated purchase-order receipt is **pending comparison**, not automatically matched. The old account is a baseline to verify, **not** an unconditional right to pay. The critical supplier supports time-sensitive healthcare replenishment, but no actual supply shutdown or contractual late-fee effect is supplied. The finance policy requires bank-detail change verification, vendor-master reconciliation, Owen's authorization and Grace's **different-person** treasury sign-off before release. No named exception permits email-only changes.

**Round decision:** Nadia holds any unexpected proposed beneficiary change once detected; Felix retrieves VC-17 without using the message; Owen checks authority and the cutoff. Ravi/Evelyn may coordinate supply escalation, not invent a bank-change exception. **What remains unknown:** invoice acceptance, contact availability, legitimate change request, whether the batch has already been sent, the true sender, attachment behavior, and account access.

### Round 1 — VF-01 + VF-02: the bait and opened attachment (minutes 9–19; Detect)

**VF-01, message stamped 09:06 UTC:** AP receives "Urgent: INV-7742—updated remittance account before today's run." Display name says **Meridian Care Supply – Billing**. Visible From is **billing@meridian-care-supp1y.example** (digit **1** in "supp1y", not the letter **l** in the approved **meridian-care-supply.example**). Reply-To appears as **ap-confirm@remit-center.example**, a different third domain. The body urges BANK-NEW-99 and says the invoice must be paid before 14:30; it contains an apparent signed note. The new-bank token has **not** been verified as belonging to the supplier.

**VF-02, help-desk statement at 09:14:** Nadia's colleague **Eli Brooks** reports he **opened a displayed attachment**, "INV-7742-Updated-Details.pdf," in a workstation viewer. He cannot confirm whether the attachment was downloaded locally, whether a link was followed, whether a macro/executable action ran, or whether any credentials were entered. No full original header file or endpoint acquisition is supplied yet. The fact an attachment was viewed is **not** proof of malware execution, exfiltration or successful login by an adversary.

**Decision request:** Nadia freezes requested BANK-NEW-99 and asks Grace for a batch hold check; Theo opens synthetic case **EML-IR-002** with separate *payment diversion* and *endpoint/mailbox exposure* questions; Jonas requests an original **MIME/EML export with full header/body and unchanged attachment bytes** via a supported admin/e-discovery channel, not by re-forwarding the file; Marta requests covered endpoint and mailbox telemetry with time/source labels. Keep Eli available for a non-blaming factual interview. **Stop condition:** nobody opens the attachment again or uses a number or link from the suspicious message.

**Conditional alternatives:** If participants pay because the supplier sounds urgent, record a policy/safety failure **without claiming a transfer actually occurred**. If participants immediately wipe Eli's endpoint, mark preservation and scope defects; pause any live action. A narrowly approved, reversible endpoint restriction can be considered **after** ownership, impact and available evidence are reviewed, not assumed executed.

### Round 2 — VF-03: queue is not settlement (minutes 20–31; Respond)

**VF-03, AP/treasury reports at 09:23 UTC:** Payment system shows **INV-7742 = queued / not released**; the beneficiary snapshot is **BANK-OLD-42**. A separate **draft vendor-master edit** proposes BANK-NEW-99 but has no approver receipt. An automated batch scheduler may pick up approved entries before the cutoff. Treasury has **not** supplied a bank acknowledgment or settlement proof for any transfer. A screen saying "queued" is not a transfer receipt; a draft edit is not an enacted master change.

**Decision:** Nadia documents **hold requested** for the invoice and the specific change ticket; Grace checks the control-plane **hold applied** readback, affected batch ID, destination, expiry and any alternate disbursement route. Felix compares original purchase order, invoice ID, vendor ID, baseline banking token and change authority. Owen records independent finance review, not approval of the new account. Evelyn asks whether safe deferment or supply escalation is needed; the answer remains tied to supplier and finance evidence.

**Worked contrast:** Defensible line: "VF-03 shows no release yet; request and independently confirm a hold across scheduled and manual paths." Defective line: "There was no fraud, because it's only queued." Both fraud intent and later transfer behavior remain unproved.

**Conditional branches:** A real hold readback recorded in a separately labeled participant **exercise action receipt** may establish only the **specified batch's** status. If a second payment path has not been checked, it remains unknown. If the participant cannot verify the hold, annotate "hold pending / request made" and immediately escalate; do not mark safe by intention.

### Round 3 — VF-04: headers, provenance and safe attachment custody (minutes 32–43; Detect / Respond)

**VF-04, read-only messaging export at 09:36 UTC:** A fictional immutable admin export, **EML-SRC-004**, preserves the synthetic message and original attachment byte stream. Its simplified header field record (illustrative values, **not an actual raw MIME header dump**) is:

| Field or record | Synthetic value | Proper interpretation / limit |
|---|---|---|
| Display name | "Meridian Care Supply – Billing" | Freely presented text, not identity proof |
| From | billing@meridian-care-supp1y.example | Similar-looking but **not** approved supplier domain |
| Reply-To | ap-confirm@remit-center.example | Responses would be directed elsewhere; not itself proof of who sent it |
| Envelope return-path | bounce@meridian-care-supp1y.example | SMTP return path, distinct from legal vendor authority |
| SPF | pass for meridian-care-supp1y.example | Authenticates sending source for that **lookalike** domain only |
| DKIM | pass; d=meridian-care-supp1y.example | Signed by lookalike domain; not an approved bank-change attestation |
| DMARC | pass, aligned with the lookalike From | Alignment against the **lookalike**, not equivalence to meridian-care-supply.example |
| Message date / received | 09:06 / 09:07 UTC, respectively | Message-provided versus server time; check clock sources separately |
| Attachment | INV-7742-Updated-Details.pdf; SHA-256 recorded in evidence system | Hash links captured bytes to a later identical copy; it does not certify content is harmless |
| Collection status | Source export supplied; independent hash readback **pending** | A named source record alone does not complete custody verification |

See [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322) for From/Reply-To field roles and [NIST SP 800-177 Rev. 1](https://csrc.nist.gov/pubs/sp/800/177/r1/final) for email trust technologies. A pass for a different controlled domain is **compatible with an impersonation hypothesis**, not proof of compromise of the real supplier domain or the AP mailbox. An attacker can legitimately authenticate mail sent from a lookalike they control.

**Safe handling decision:** Jonas retains original raw MIME/EML and original attachment byte stream in an access-controlled case repository; assigns separate **source / acquisition / analysis-derivative** IDs; documents lawful collection authority, collector, source mailbox, UTC/offset, immutable storage location, SHA-256 computation and **readback** of the copy. Mark any step **pending** until performed. Do not use personal mail forwarding, cloud preview of a second copy, mass distribution, live execution or public malware-sample services. If specialist static inspection is warranted, use a separately approved isolated workflow and a derived copy. Marta preserves gateway metadata and authentication logs for their actual retention window.

**Hypothesis test:** H1 is now more plausible because the visible From and aligned DMARC domain differ from the signed supplier domain; H2 is not eliminated until verified supplier contact; H3 still needs evidence of mailbox entry or misuse. **Negative control:** even if the original supplier domain had passed SPF/DKIM/DMARC, that alone would not authorize a payment change.

### Round 4 — VF-05: genuine out-of-band verification (minutes 44–55)

**VF-05, 10:02 UTC:** Felix obtains vendor-master record VC-17 from the signed procurement register dated before the suspicious message. It names **Leila Okafor** as the approved supplier liaison and stores a pre-existing contact number **inside the fictional register**, which is **not printed** in the participant packet. The message body itself includes a different "urgent remittance desk" number. A first simulated callback attempt to VC-17 is marked **no answer**, not rejected and not a positive verification.

**Decision:** Felix initiates callback only to VC-17; writes **request attempt ≠ connection ≠ authenticated conversation ≠ authorized bank-account instruction**. If unavailable, use pre-established alternate escalation in the supplier register or procurement contract, and keep BANK-NEW-99 frozen. Nadia and Grace maintain their distinct hold/batch checks. Evelyn negotiates a *contingent* supplier-continuity path with procurement without substituting an email-provided number. Dana drafts a neutral internal operations advisory (not an accusatory supplier alert).

**Conditional branches:** (A) **No answer before cutoff**: hold beneficiary change; escalate continuity/cutoff cost for a documented enterprise decision, never waive caller identity. (B) **Call connects**: use existing knowledge to verify that the party is the recorded authorized contact and ask whether any bank change was requested; log what was said and limitations. A callback receipt **does not** prove the external bank actually belongs to the supplier unless the authorized supplier process confirms the necessary details. Do not pre-release VF-06.

### Round 5 — VF-06: supplier says the bank details did not change (minutes 56–67)

**VF-06, 10:19 UTC:** A **fictional** callback receipt **CALL-17** says Felix dialed VC-17 independently, confirmed the listed liaison Leila through the approved supplier-contact protocol, and Leila said **Meridian Care Supply did not request a beneficiary change for INV-7742**, the supplier still records BANK-OLD-42, and supply questions should be escalated through the established relationship channel. This is a signed **classroom statement by a specified person**; it is not a bank ownership attestation, an investigation of the lookalike sender, or proof that supplier systems are uncompromised. No record in the scenario contradicts Leila's statement.

**Decisions by team:** Felix records suspected external impersonation and flags vendor-master protection; Nadia rejects BANK-NEW-99 and starts reconciling the legitimate invoice and goods receipt; Owen verifies the authorization basis for paying **the old approved destination**; Grace independently checks cutoff batch, destination, second approval and alternate disbursement routes. An old beneficiary entry is not itself enough to release money if there is an invoice/receipt mismatch. Theo keeps the attachment/mailbox investigation distinct from supplier confirmation. Isabel advises on allegation wording and evidence retention.

**Defensible branch:** Reject proposed BANK-NEW-99, confirm original beneficiary and commercial obligation, then decide payment **only** if both internal approvers sign a destination-specific, transaction-specific instruction and Grace receives a safe payment-register readback. **Unacceptable branch:** Reopen the suspicious email to "confirm" the old details or claim that CALL-17 proves who sent the lookalike message.

### Round 6 — VF-07 + VF-08: mailbox/attachment scoping, not automatic compromise (minutes 68–79)

**VF-07, 10:44 UTC:** A **synthetic**, privacy-minimized IdP audit lists one successful sign-in to Eli's corporate identity at **08:58 UTC** from an unfamiliar network label **NET-X**; the exported card supplies **neither** device identity, authenticated-user confirmation, geolocation assurance nor full sign-in history. A separate mailbox audit excerpt shows **no new forwarding rule in its queried 09:00–10:30 UTC range**, but earlier rules, delegated access, OAuth grants, existing sessions and other routes are **not covered**. This is a possible account-access lead, not proof of unauthorized access or clean account state.

**VF-08, 11:02 UTC:** A managed endpoint report covering Eli's workstation between **09:10 and 10:30 UTC** shows the document viewer started at 09:14 and **no suspicious child process in this covered data**. It does not cover memory-only behaviors, file content beyond metadata, telemetry before 09:10, malicious links handled elsewhere or network actions outside logged scope. A help-desk statement says Eli did not knowingly enter credentials, but his recollection is not forensic proof. **No supplied indicator confirms malware execution, exfiltration or mailbox takeover.**

**SOC/IT decisions:** Theo decides whether further bounded access/endpoint inquiry is proportional. Jonas asks for full sign-in audit with device and risk context, session/consent history, delegated access, existing mailbox forwarding and relevant message traces under least privilege; Marta checks collection coverage and advises **conditional** credential/session remediation. If evidence later supports unauthorized access, obtain scoped approval to revoke sessions/tokens, reset authentication factors, review rules and OAuth grants, preserve original receipts, and independently confirm continued account control. If evidence remains ambiguous, preserve case status as **suspected / not established**, enforce targeted monitoring and scope-limited access safeguards instead of proclaiming compromise.

**Legal/communications decisions:** Isabel limits personal data capture to what is needed for the investigation and checks applicable law/contract terms if disclosure evidence emerges. Dana drafts: "**A suspicious payment-instruction email was received; the proposed change is on hold while the vendor and internal controls are verified. We have not established a diverted payment or unauthorized mailbox access. Updates will follow after verified checks.**" The message is **unsent** until approved by the appropriate executive, finance, legal and security owners. Do not publicly attribute criminal intent to the supplier.

**Alternative test:** A bounded absence of a rule in a queried window is not absence of all forwarding routes, just as a quiet endpoint interval is not proof that an opened attachment was harmless.

### Round 7 — VF-09: cutoff, ledger and bounded recovery (minutes 80–90)

**VF-09, case checkpoint 14:15 UTC, deliberately released only after VF-08 decisions freeze:** Grace obtains a **fictional, read-only** payment-register checkpoint for INV-7742: **status held / no payment released in the specified treasury batch**; recorded destination **BANK-OLD-42**; draft BANK-NEW-99 edit rejected in vendor-master workflow; **CALL-17 available**; Owen and Grace have **not** supplied final invoice-specific dual-release signatures. An independent bank settlement acknowledgment is **not supplied**. No later payment route, actual supplier receipt, or successful disbursement is proved. A procurement note says interruption could affect next-week supply scheduling, but gives no quantified harm and no approved exception.

**Final options to compare:** **Option A — keep the specific payment on hold** pending invoice/receipt reconciliation and two different-person approvals, with Felix/Leila coordinating supply; **Option B — conditionally release to BANK-OLD-42** only after verified invoice/receipt, trusted supplier contact, controller and treasury signatures, authorized operator action and independent register/bank readback; **Option C — release to BANK-NEW-99** based on the suspicious email, which **fails** the authorization gate. Mark B as a **future conditional permission**, not an accomplished payment. The card supplies no payment execution event, so **the canonical scenario ends with an unresolved payment hold**, not a fictitious prevented-loss figure, compromised account or completed remittance.

**Escalation:** Evelyn may authorize resources and a documented supplier continuity intervention; she cannot waive the dual control. If the hold outlasts a vendor deadline, record a service-risk escalation and schedule another callback via VC-17. If a distinct later bank receipt shows a transfer to an unexpected beneficiary, activate the organization's financial institution and incident/legal reporting response **immediately** and record that as a **new optional hypothetical**, not a fact in VF-09. The [FBI's BEC guidance](https://www.fbi.gov/how-we-can-help-you/common-frauds-and-scams/business-email-compromise) describes promptly engaging the financial institution when fraud is detected; the tabletop never represents that a recall was actually requested.

## 5. Conditional consequences and independent negative controls

**Consequences are conditional teaching branches, not observations.** An alternative scenario result requires a newly numbered facilitator card, separate release time and a frozen prior decision; never edit VF-00–VF-09 to reward hindsight.

| Choice or hypothesis | Under which additional evidence it could be defensible | What must remain unclaimed |
|---|---|---|
| Put the payment/change on hold | Finance and Treasury record a batch- and destination-specific hold receipt and verify scheduled and manual paths | That a requested hold was applied everywhere, or money recovered |
| Make an independent callback | VC-17 existed before VF-01; caller and response are recorded with approved supplier validation | That callback attests bank ownership in every banking system |
| Pay the old beneficiary | Invoice/receipt and old beneficiary independently matched; two distinct internal approvers sign; action and reconciliation are observed | That VM-2026-10-13 alone settles invoice legitimacy or that a queued payment was sent |
| Treat the email as impostor-controlled | Domain and Reply-To anomaly, CALL-17 negative supplier statement and other evidence support this **working assessment** | That an identified person committed fraud, or real supplier mailbox was compromised |
| Investigate Eli's mailbox | Context for NET-X, sessions, delegates, rules, message access and endpoint telemetry is obtained through authorized scope | That one unfamiliar sign-in proves account takeover, or a narrow negative query clears the account |
| Initiate account/session recovery | A reviewed compromise or risk threshold and documented approval justify proportionate action with preservation and independent validation | That reset proves all attacker access ended or that infection was confirmed |
| Issue staff or supplier notice | Finance, security, legal and executive reviewers authorize bounded wording and its channel | That an unsent draft, extortion-style phrasing or speculation is a delivered notice |

**Negative controls the facilitator must test:** NC-1: DKIM/DMARC passing for the **lookalike domain** must not validate supplier identity. NC-2: An attachment **opened** is not evidence malware **ran**. NC-3: "No forwarding rule in 09:00–10:30" is not "no mailbox exposure." NC-4: A payment **queued** or **held in one batch** is not settlement or proof all rails are blocked. NC-5: One authenticated callback does not replace independent controller/treasury approval. NC-6: A late VF-09 register cannot repair a premature VF-03 "no release anywhere" statement.

## 6. Mail and endpoint evidence: safe and reproducible reasoning

The classroom does not require a machine lab. A reversible, approved **paper examination** is sufficient, so no executable malware or active attachment is published. A facilitator can reproduce the evidence reasoning using the fixed headers in VF-04 and the defined query coverage in VF-07/VF-08.

1. **Preserve source identity:** Request the original MIME message with complete headers, transport authentication results, envelope metadata and attachment bytes through an authorized email-admin/e-discovery method; record case ID, collector, source mailbox and legal basis.
2. **Preserve provenance:** Keep source record separate from acquired copy, working analyst derivative, gateway event and user recollection. Write acquisition time, source time, ingestion time, timezone and observed offsets separately.
3. **Verify bytes:** Record SHA-256 on the acquired file and an independently computed readback hash, with tool/version and named operator. This establishes equality of the *tested bytes*, not identity of the purported sender, absence of malicious content or safe payment instructions. **No actual hash string is provided**; do not fabricate a computed result.
4. **Inspect cautiously:** Avoid opening the original attachment or sending it to a public analyzer. A trained responder may request separately approved, isolated static analysis of a derivative. Do not perform that action in this tabletop; log "not evaluated" rather than inventing process, sandbox or signature outcomes.
5. **Bound account claims:** Compare token/session activity, conditional-access data, approved devices, forwarding rules, delegates, OAuth consents, mailbox audit and sent/deleted items with known coverage and retention. A negative finding is always tied to its source and search window.
6. **Preserve privacy:** Keep personal mailbox content restricted by role, need and retention/legal hold, with log access separated from finance approval. Evidence preservation and account remediation are different activities.
7. **Close technical decisions conditionally:** If an incident response authority approves token revocation or endpoint isolation after a documented risk assessment, record the action's actual receipt, effect verification and rollback/restore process. An approval alone never proves technical effectiveness.

**Worked header contrast:** VF-04's From and DKIM/DMARC domains align with **meridian-care-supp1y.example**, not the vendor-master **meridian-care-supply.example**. The divergence plus supplier callback supports holding the change. It **does not** support "DMARC failed," "supplier's legitimate domain was forged," "Eli's mailbox was hacked" or "the bank transfer happened." RFC 5322 distinguishes From and Reply-To semantics; domain authentication says nothing by itself about a vendor-master bank-change authority.

## 7. Finance recovery: gates, receipts and what is still missing

A complete financial recovery path is **not** synonymous with ending a cybersecurity ticket. For every future release decision, create a signed **transaction envelope** naming invoice ID, vendor ID, source order/receipt, exact destination **token**, currency/amount, approved batch, change history, requester, independent verified supplier callback, two distinct internal authorizers, operator, cutoff, check time and post-release proof. No live bank account number is ever needed in this teaching file.

| Gate | Required evidence | Owner / rejection rule |
|---|---|---|
| G1 Invoice and goods/service obligation | Signed PO/receipt match or documented authorized exception; amount and duplicate-payment check | Nadia + Felix: missing comparison means **not validated** |
| G2 Beneficiary | Bank destination reconciled to approved vendor master and pre-existing supplier callback / supplier verification process | Felix: emailed BANK-NEW-99 stays rejected |
| G3 Two internal approvals | Separate Owen and Grace decisions, with timestamps, scopes and no role/person duplication | Finance Controller + Treasury: any missing approval means **do not release** |
| G4 Execution authorization | Named authorized payment operator, approved destination, selected batch, limit and cut-off checks | Grace: a queued/draft record is not an execution receipt |
| G5 Independent readback | Final register shows destination, status and batch ID; bank acknowledgments only if actually supplied; exceptions escalated | Treasury observer: distinguish instructed, released, acknowledged and settled |
| G6 Mailbox/endpoint restoration | When applicable, source-preserving investigation, approved session/identity actions, reauthentication checks and monitoring | Theo + Marta: no automatic "compromised" label based on VF-07 |
| G7 Supply continuity | Vendor contact, next service/supply obligation, non-payment impact and escalation | Felix + Evelyn: urgency never waives G1–G5 |

**Worked recovery path:** After VF-06, a team may legitimately **reject BANK-NEW-99** and prepare **BANK-OLD-42** for consideration. But VF-09 supplies no final invoice match and no two-release signatures. Therefore the strongest supported closure at minute 90 is: "**Bank-change request rejected; the named batch remains on hold at the reported checkpoint; authorized payment release not evidenced; supplier-continuity contact made; payment and mailbox investigations remain open with named next checks.**" That is a bounded outcome, not a failure to finish the tabletop.

**If actual funds were later misdirected (not supplied):** Activate financial institution fraud/recall procedures and any applicable law-enforcement/regulatory process immediately through trusted contacts; retain payment IDs, bank receipts, timestamps and message sources, preserve confidentiality and avoid a fabricated recovery guarantee. This is contingency advice, not a claim of a completed payment or recovery.

## 8. Communications and executive decisions

**Internal draft, unsent until reviewed:** "An unverified email requested a late change to a critical supplier's bank destination. The proposed change is frozen and the specified invoice batch is under finance review. We are independently verifying supplier instructions, payment-control status and whether any mailbox or endpoint access needs further investigation. Do not reply to the suspicious message or process account changes outside the approved vendor-master workflow."

**Supplier draft via VC-17, unsent:** "We are reviewing a payment-instruction message that appears to reference INV-7742. Please use our established procurement contact channel for any required verification. Our team will report a confirmed payment decision through its approved process; do not infer that payment has been issued." Do not email evidence to the suspect Reply-To. If CALL-17 is still unavailable, label the supplier draft **not delivered**.

**Executive checkpoint, fictional 14:15:** Evelyn receives three separated statuses: **financial** (specific batch held, not proof of universal no transfer), **supplier** (CALL-17 disputes the proposed change, invoice/match still under review) and **cyber** (lookalike indicators; mailbox/attachment compromise not established). Evelyn can commission risk mitigation and service-continuity options, but cannot sign Owen's and Grace's controls on their behalf.

Dana records **drafted / reviewed / approved / dispatched / acknowledged** separately, with channel and next update trigger. Isabel assesses legal reporting and privacy impact if **additional facts** warrant it, not by treating suspicious payment instructions as a proven data breach.

## 9. Required learner outputs, rubric and observer calibration

Submit all six items at the defined freeze times. The assessor evaluates records **available to another shift without oral repair**, not agreement with a preferred narrative.

| Artifact | Exact deliverable | Relevant gate |
|---|---|---|
| **A1 Incident and chronology ledger** | VF release time, source/event time, frozen observations, hypotheses, uncertainty and next inquiry | O2 / no hindsight |
| **A2 Payment and bank-change ledger** | VM baseline, suspicious change, invoice obligation, each hold/readback, alternate rails, approval statuses | G1–G5 |
| **A3 Callback verification record** | VC-17 provenance, dial/callback receipt, verified supplier party, words and limits, actions taken | Supplier gate / Felix |
| **A4 Technical evidence register** | Original MIME and attachment acquisition requests, source/copy/derivative, hashes/readback statuses, permitted queries and omissions | O3 / O5 |
| **A5 Decision/communications sheet** | Two defensible choices and their costs, authorizers, proposed vs executed, unsent/approved wording | Finance / SOC / Isabel / Dana |
| **A6 After-action backlog** | Observed deficiency, owner, deadline, measurable negative-control rehearsal and independent sign-off | O6 |

**Scoring:** Ten criteria, each **0** absent/contradicted, **1** relevant but missing source/time/authority/limit, **2** reproducible and explicitly bounded: **0–20** total. This scoring scheme is original instruction, not an NIST rating. Observers must cite frozen artifact ID and VF card; if the facilitator skips a card, label **not observed / facilitator error** instead of scoring missing participant knowledge as zero.

| Criterion | Full 2-point evidence |
|---|---|
| **C1 Payment urgency and authority** | Names cutoff and supplier cost but refuses email-only authority; keeps AP, controller, treasury separate |
| **C2 Hold scope and readback** | Separate requested/applied, named batch, manual/scheduled paths and status at 14:15 |
| **C3 Header meaning** | Correctly compares From, Reply-To and SPF/DKIM/DMARC for lookalike domain; no authority leap |
| **C4 Safe attachment handling** | Original source/byte evidence, custody/readback limits, no unsafe opening or invented execution |
| **C5 Callback authenticity** | VC-17 predates email; no use of email-supplied contact; attempt/answer/attestation distinguished |
| **C6 Dual control** | Invoice, supplier and bank checks + Owen/Grace distinct approvals, no single-person override |
| **C7 Mailbox scoping** | VF-07/08 positive and limited negatives separated; no unsupported takeover/clearance conclusion |
| **C8 Release chronology** | Frozen decisions use only released cards; no VF-06 or VF-09 used early |
| **C9 Payment recovery and communications** | No stolen-funds claim; released/settled statuses distinguished, reviewed unsent messages and contingency |
| **C10 Debrief/remediation** | Five concrete action owners, measurable retests, timing and negative controls |

**Noncompensable critical-control failure:** Directing payment to BANK-NEW-99 without callback and required approvals; using contact details only from suspicious email as the callback; executing live attachment/account/payment changes for the exercise; or exposing real confidential data. Stop the exercise and record **critical gate failed** even if points would otherwise be high. An excellent paper result does not certify enterprise or banking readiness.

Suggested **classroom-only** interpretation: 17–20 strong, 12–16 material gaps, 0–11 major rework. Report missing injects, unresolved score disputes, lack of independent human review and critical gates separately.

## 10. Facilitator worked answers and alternate decisions

**Use only after the corresponding round closes.** These examples demonstrate sufficiency, not a single preordained answer. Any alternate may pass if its authorization, provenance, scope, risks and independent checks are equally defensible.

| Round | Acceptable frozen answer (with reason) | Tempting but unsound answer (and correct facilitation) |
|---|---|---|
| VF-00 | Treat BANK-OLD-42 as the signed baseline, not a guaranteed payment authorization; map Owen + Grace; check PO match | "Critical supplier means payment must be sent." Ask who approved the invoice and destination |
| VF-01/02 | Hold proposed change; open separate cyber questions; request source-preserving message/attachment export | "Opened attachment = malware." Ask for execution-specific evidence and avoid re-opening it |
| VF-03 | Confirm hold by named batch and readback; search for alternate routes; no released money is documented in card | "Queued proves fraud did not happen anywhere." Ask what paths the card covers |
| VF-04 | Domain auth passes for lookalike; preserve raw MIME, source vs copy and readback; vendor identity remains independently unverified | "DMARC pass verifies real supplier." Compare exact spelling against signed master |
| VF-05 | Call only pre-existing VC-17; no answer remains **pending**; do not switch channels to email Reply-To | "Vendor sent new urgent number." Ask when and where that number was previously verified |
| VF-06 | Record Leila's negative statement; reject proposed BANK-NEW-99; keep Owen/Grace release gates and invoice comparison | "Callback alone authorizes BANK-OLD-42 payment." Ask for internal two-person receipt |
| VF-07/08 | Investigate NET-X/device/session and exact rule-query coverage; maintain possible access and opened-file uncertainty separately | "A clean 09:10–10:30 scan clears mailbox." Ask for earlier sessions, other routes and detection limits |
| VF-09 | Name held batch and unsatisfied release conditions; propose controlled old-destination payment only after gates | "14:15 held means no diverted money ever." Ask for bank acknowledgment and all disbursement paths |

**Facilitator adjudication example 1 (C3):** Learner writes at VF-04: "SPF, DKIM and DMARC passed, so it came from Meridian." Observer scores **0**, because the exact authenticated domain is the **lookalike**; passing lookalike authentication cannot satisfy vendor-master supplier authority. If they correct it after VF-06, retain the old artifact and score the correction as a **later** response, not a rewritten earlier decision.

**Facilitator adjudication example 2 (C2):** Learner writes at VF-03: "Hold requested for INV-7742." Observer may assign **1**, not 2, if no evidence of application, batch scope or alternate payment route follows. A later VF-09 receipt may support an updated bounded state, not retroactively validate the incomplete VF-03 record.

**Facilitator adjudication example 3 (C7):** One observer suggests 2 because VF-08 contains no suspicious child process; another suggests 0 because the learner declared "device and mailbox clean." Compare A4/A5 against the criterion: an unconditional clearance is contradicted by omitted coverage, so **reconcile to 0** for that claim. A supported limited negative observation earns credit only if its timeframe and omissions are explicit.

**Independent practice variant, no new facts:** At VF-05 assume Leila is unreachable through any existing approved channel before cutoff. In **P-02** write a 100-word executive decision comparing (i) hold with quantified *unknown* supply cost and procurement escalation and (ii) release to previously approved BANK-OLD-42 **only if** invoice, existing beneficiary, prior approval and dual controls are actually validated without a callback to authorize any **new bank change**. **Worked answer:** Neither choice can authorize BANK-NEW-99. Continue hold if current policy makes callback mandatory for the contested transaction or invoice status is unresolved. If the previously approved unchanged-account payment is independently permitted by written policy and all normal checks pass, Owen and Grace may consider release under that **separate** documented scope; log the missing callback, fraud inquiry and supply risk. Never invent a waiver from executive urgency. This variant does not change the canonical VF-06 outcome.

## 11. Debrief and improvement backlog

Set aside 25 minutes: each team answers **what was known when**, which source or claim was over-read, which control could have stopped an erroneous change, who paid the business cost of a hold, which contact was genuinely independent, what the opened attachment does **not** establish, whether any mailbox access remains unknown, and whether a new shift can reconstruct hold/approval/settlement statuses from A1–A6. Debate both false-positive delay and false-negative payment exposure without implying either occurred in the exercise.

| Fictional action ID / observed gap | Owner, suggested target after exercise | Independently testable follow-up |
|---|---|---|
| **I-01 — Payment-change callback register** | Felix, Procurement; 14 days | Retest VC-17 provenance and a random pre-existing alternate using a synthetic spoofed message; evidence of rejection of message-provided number |
| **I-02 — Two-person beneficiary control** | Owen and Grace; 21 days | Drill maker/controller/treasury separation and verify no one identity can approve both or alter approved destination post-signature |
| **I-03 — Batch hold coverage** | Grace / Treasury; 21 days | Test scheduled and permitted manual routes in an isolated payment simulator; record an actual hold acknowledgment and negative alternate-route check |
| **I-04 — Header/attachment evidence readiness** | Jonas and Marta; 30 days | Reproducible synthetic MIME preservation, safe restricted acquisition, independent hash readback and scope-labeled sign-in/rule queries |
| **I-05 — Supply continuity and bounded communication** | Evelyn, Leila, Isabel and Dana; 30 days | Two mock events (unreachable vendor; confirmed unauthorized beneficiary) with separate signed factual drafts and lawful escalation decisions |

The targets are **fictional planning intervals**, not NIST mandates or a promise of completed remediation. Debrief with the facilitator's score, dissenting ratings, safety stop findings and unresolved evidence requests; assign a later supervised retest only when an accountable real organization authorizes it. The **exercise** is complete when A1–A6, frozen decisions, rubric and action backlog are recorded. The **fictional incident** is intentionally not established as a completed fraud or restored transaction. The ten-entry site catalog, course books and live payment systems remain untouched.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3 (final, April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — response across CSF 2.0 functions, decision and risk management; this tabletop's role/score design is not NIST-mandated.
2. [NIST Cybersecurity Framework 2.0, CSWP 29 (final, February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — six nonprescriptive Functions and cybersecurity outcome taxonomy.
3. [FBI, Business Email Compromise](https://www.fbi.gov/how-we-can-help-you/common-frauds-and-scams/business-email-compromise) — vendor-payment impersonation, independent verification and prompt reporting/financial-institution escalation when warranted.
4. [FBI IC3, Business E-mail Compromise: The 3.1 Billion Dollar Scam (June 2016)](https://www.ic3.gov/PSA/2016/PSA160614) — **historical** original advisory documenting pre-existing-number callbacks, payment-change two-person review and lookalike domain detection; numerical headline is not a current estimate.
5. [NIST SP 800-177 Rev. 1, Trustworthy Email (February 2019)](https://csrc.nist.gov/pubs/sp/800/177/r1/final) — SPF, DKIM, DMARC and other email trust guidance; not a certificate of bank-account authority.
6. [RFC 5322, Internet Message Format](https://www.rfc-editor.org/rfc/rfc5322) — semantics of From, Reply-To, Date and other message fields; header fixture is a didactic abstraction, not a captured raw message.
7. [CISA, Avoiding Social Engineering and Phishing Attacks](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks) — verify uncertain requests by contacting the company independently rather than through attacker-supplied information.

All named entities, attachments, bank tokens, timestamps, financial amounts, exercise metrics, cards, branches and example decisions are **newly authored fictional teaching material**. External primary references are linked, attributed and paraphrased, **not reproduced or relicensed**. Rights in the original writing follow [OpenCyber Academy RIGHTS.md](../../../RIGHTS.md) and its CC0 scope/third-party exceptions. This document does not provide legal, banking or forensic certification and is not a substitute for an authorized incident-response or payment-control procedure.
