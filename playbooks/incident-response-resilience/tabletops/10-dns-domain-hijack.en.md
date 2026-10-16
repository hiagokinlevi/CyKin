# TableTop 10 — Domain routing hijack: restoring DNS without inventing donation losses

**Edition:** English · **Exercise ID:** TTX-DNS-10 · **Catalog scenario ID:** `dns-domain-hijack` · **Editorial date:** 2026-10-15  
**Status:** Original fictional defensive classroom exercise; independent technical, payment/privacy and human editorial review pending.  
**Format:** Facilitated paper-only exercise: 15-minute briefing, 90-minute progressive injects, 25-minute debrief; expand timing for accessible participation.  
**Audience:** Nonprofit governance, domain ownership, registrar administration, authoritative and recursive DNS operations, web/application engineering, security/forensics, fundraising, payment operations, privacy/legal, donor services, communications and neutral observers.  
**Navigation:** [Previous authored TableTop — 09 Web application compromise](09-web-application-compromise.en.md) · [Incident-response playbooks index](../README.md) · [Original ten-scenario catalog](../../../web/tabletop/scenarios.json). This is scenario **10 of 10** in the original index, **not** an eleventh incident or a deployed web feature. See [primary sources and rights](#12-primary-sources-and-rights).

## 1. Entirely fictional situation, safety boundaries and objectives

**Everything here is synthetic:** the nonprofit, participants, domain, registrar, DNS operator, servers, resolver cohorts, payment provider, timestamps, session records, zone revisions, record destinations, transaction references, test receipts and outcomes are invented classroom fixtures. The name **harborlight-aid.example** uses a reserved example top-level domain and **DOC-IP-GOOD** and **DOC-IP-UNKNOWN** are symbolic destination labels, **not routable IP addresses or live DNS record values**. No domain-registrar account, credentials, executable command, zone modification syntax, real donor record, working payment method, phishing content or domain hijacking technique is provided. Learners neither query production DNS nor make charges or registrar changes.

**Fictional nonprofit:** **Harborlight Neighborhood Aid (HNA)** runs a public information website and a donation entry page at the symbolic name **donate.harborlight-aid.example**. A separately governed payment processor, fictional **Aurora Donation Services (ADS)**, handles authorized donation transactions. HNA's approved DNS change log **Z-APP-41** maps the donation hostname to **DOC-IP-GOOD**. At incident start, some users can still reach a donation page, while other observations show intermittent resolution to **DOC-IP-UNKNOWN**. A read-only authoritative-zone observation differs from the approved change log, and the registrar audit shows a new session. Neither proves a particular human initiated a change nor what any donor actually saw, submitted or paid.

**Core risk:** Intermittent access is a **service-integrity incident requiring urgent investigation**. The anomalous authoritative state could result from an unauthorized change, an administrative mistake or asynchronous authoritative publication; recursive caches may also return older values. The registrar session needs its own attribution evidence. The case does **not** prove donor redirection to a malicious site, phishing, stolen donations, payment-processor intrusion, transaction failure, credit-card disclosure or a legally reportable breach.

### Seven distinctions learners must preserve

1. **Domain-registration account versus authoritative DNS:** The registrar controls domain registration and potentially delegation and provider settings; authoritative name servers serve the zone. A new registrar session does not by itself show that session changed the zone or that the registry transferred ownership.
2. **Approved zone versus served zone:** A signed change log is authorized *intent*. An independently sourced answer from each authoritative name server is observed *served state*. Compare name, type, intended answer, source identity, serial/revision and time.
3. **Authoritative answer versus recursive cache:** An authoritative server's current answer differs from a recursive resolver's possibly cached answer. Correcting an authoritative RRset does not flush every public cache immediately.
4. **TTL, propagation and timing:** A TTL limits how long the cached RRset may be retained under standard behavior. A change to TTL now cannot retroactively reduce the remaining cache lifetime of answers cached earlier; stale configurations, client caches and exceptions can complicate observations.
5. **DNS resolution versus browser transaction:** A DNS answer does not establish which endpoint the browser actually contacted, certificate/HTTPS state, rendered content, cookie/cache path, or that a donor finished a transaction.
6. **Donation page reached versus payment confirmed:** A displayed page, a donation button and a checkout handoff are not payment authorization, captured/settled funds, confirmation by the payment provider or a recipient's receipt.
7. **Anomaly versus cause and impact:** A new session and unauthorized-by-register zone state justify action and investigation; they do not alone prove account compromise, attacker attribution, donation theft, exfiltration or loss amount.

### Observable objectives

- **O1 — Governance:** Verify registrant/domain owner, trusted registrar/DNS provider contacts, delegated approvers, payment-service boundaries, safe donor-continuity plan and change freeze authority.
- **O2 — Source-aware detection:** Reconcile signed zone log, authoritative answers, registrar sessions, recursive snapshots and browser observations by their distinct clocks, scopes and confidence.
- **O3 — Proportionate containment:** Freeze registrar changes with the owner; preserve session and zone history; restore only unauthorized-by-register RRsets through a controlled reviewed process without blindly changing delegation or destroying evidence.
- **O4 — Payment/data caution:** Obtain independent payment-processor and web/transaction records before claiming failed, diverted or stolen donations; minimize personal donor information.
- **O5 — Trustworthy recovery:** Restore verified authoritative zone and registrar access, coordinate TTL/caches with DNS provider and verify sampled recursive, browser and donation-completion evidence separately.
- **O6 — Reproducible practice:** Work a fixed resolver/TTL example, compare alternate decisions and submit five independently solvable exercises with worked results.
- **O7 — Improvement:** Test registrar MFA, two-person DNS changes, protected recovery channels and external authoritative/recursive drift monitoring without promising universal visibility.

### NIST SP 800-61 Rev. 3 / CSF 2.0 — a teaching mapping, not a mandated playbook

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), final April 2025, is a [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) Community Profile and supersedes the former Rev. 2 four-phase checklist. **Govern, Identify and Protect** contribute preparation and risk ownership; **Detect, Respond and Recover** provide incident-specific objectives; improvement is continuous. Card clocks, domain-authority charters, rubrics and two-person approvals in this text are original educational designs, **not a claim that NIST prescribes these exact actions**.

[NIST SP 800-81 Rev. 3, Secure DNS Deployment Guide](https://csrc.nist.gov/pubs/sp/800/81/r3/final), **final March 19, 2026**, covers authoritative and recursive DNS roles, security and DNS deployment. [RFC 1034](https://www.rfc-editor.org/info/rfc1034/) and [RFC 1035](https://www.rfc-editor.org/info/rfc1035/) establish core DNS resource-record, authoritative/recursive and caching concepts; [RFC 2308](https://www.rfc-editor.org/info/rfc2308/) specifies negative caching for NXDOMAIN/NODATA, a separate condition **not observed** in this case. Those references explain why a changed zone and the cache seen by one donor may diverge; they do not make a favorable DNS result a payment guarantee.

| Exercise phase | Relevant CSF 2.0 Functions | Boundaries and evidence |
|---|---|---|
| Prepared domain/change governance | Govern / Identify / Protect | Registrant proof, verified contact paths, change authority, MFA/lock limits, approved RRsets, website/processor owners |
| Detect and analyze inconsistent answers | Detect | Authoritative versus recursive versus browser; source identity, TTL/window, session history and unknown attribution |
| Preserve and contain specific zone/registrar risks | Respond | Owner-approved registrar freeze, immutable evidence, scoped restoration and provider verification |
| Rebuild known-good DNS and donor function | Recover | Authoritative unanimity, sample recursive refresh, HTTPS/application identity and independent processor test receipts |
| Review causes, gaps and controls | Identify/Improvement, Govern | External drift checks, dual approval, registrar MFA and measured response/retest |

## 2. Named teams, authorities and decision boundaries

All roles and delegations are **fictional**. Real-world account recovery, zone edits and payment actions require verified registrant and contracted-provider authorization. A learner may represent several characters, but owner approval, operator action and independent verification remain **separate signatures and states**.

| Team / named person | May decide, record or approve in this exercise | Cannot infer or authorize |
|---|---|---|
| **Halden Rook — Nonprofit Domain and Registrant Owner** | Establish registered-owner identity, approve registrar change freeze, accept approved DNS zone restoration and limited public-domain return | Declare the registrar session malicious, certify payment success or unilaterally erase evidence |
| **Selene Whitford — Authoritative DNS / Zone Steward** | Compare signed zone revision, authoritative name-server observations, zone history/TTL and rollback candidate; prepare scoped restoration with owner approval | Infer all recursive caches refreshed, change the domain without dual review or assert donor payments |
| **Octavia Pryce — Registrar Security Liaison** | Contact registrar through existing independent contract channel, preserve access history, propose account restrictions, rotate/revalidate registrar access with Halden | Equate a new login session with verified human actor or treat transfer lock as a blanket zone-change freeze |
| **Mikhail Duvall — Security Incident Commander** | Open the case, prioritize source collection, qualify competing hypotheses and coordinate a bounded response | Claim phishing or transfer of funds from a DNS anomaly alone |
| **Nerissa Volkov — Forensic Evidence Custodian** | Collect authorized read-only registrar/zone/DNS/web logs, preserve source/export/derivative, clocks and integrity | Query donor accounts broadly, retain personal data without need or call a collection request a receipt |
| **Sable Nkrumah — Web/Application Owner** | Verify approved web origin, TLS/site identity and signed application content; design safe browsing and redirect-chain acceptance fixture | Conclude a correct DNS RR proves every browser reached the legitimate site |
| **Fernanda Kwok — Fundraising and Donor Experience** | Define donor-continuity impacts, safe alternative contact, complaint triage and no-double-charge/reconciliation requirements | Attribute donor complaints to fraudulent redirection without corroboration |
| **Clemens Alder — Payment Processor and Treasury Liaison** | Verify approved ADS merchant destination, transaction/test-processor records and settlement/exception scope through pre-established provider contact | Assert stolen donations, payment-provider compromise or completed charges from page screenshots |
| **Mireya Sorrel — Communications** | Draft factual donor-facing notices, route to owner/legal/payment reviewers and record drafted/approved/dispatched statuses | Publish “phishing,” “money stolen” or “everything secure” without evidence |
| **Lakshmi Nevin — Legal and Privacy** | Set evidence minimization/retention, contractual/notification assessment and a safe test-payment authorization process | Invent a jurisdiction-wide legal deadline or exposure verdict |
| **Yvette Crowe — Service Continuity Lead** | Coordinate approved donation alternatives, contact availability and handoff when the public page is unreliable | Change DNS, accept payments on unreviewed channels or claim a charge without processor evidence |
| **Gideon Pasternak — Executive Sponsor** | Allocate approved incident resources, escalate to board/provider and accept properly qualified business risk | Override registrant ownership, provider authority or a failed donation-verification gate |
| **Inez Koller — Neutral Facilitator/Observer** | Release sealed cards, timestamp frozen decisions, enforce safe/no-hindsight rules and score source-labeled artifacts | Invent donations, direct real registrant actions or revise earlier facts after a later card |

**Distinct gate owners:** Domain change/freeze belongs to **Halden**; Selene owns authoritative-zone comparison; Octavia controls registrar coordination; independent verification is assigned by Mikhail/Nerissa; Sable checks application identity; Clemens is the trusted processor-contact gate; Lakshmi approves necessary data/payment-test protections; Fernanda/Yvette assess donors. A registrar lock, registrar session termination, zone revision, recursive-cache state and payment acceptance are **different administrative and technical objects**.

## 3. Participant packet, three clocks and no-risk facilitation rules

The facilitator supplies paper cards **DH-00 through DH-10** and releases **DH-00 only** at briefing; withhold later injects and worked answers. Participant packet includes blank **A1–A6** sheets, signed approved DNS zone baseline, role/approval charter, historical change ledger form, empty authoritative/recursive source matrix, registrar-session comparison, hypothetical payment-reconciliation form and independent rubric.

**Three clocks are mandatory:** (1) fictional event UTC/time from each source, including its retention/collection delay; (2) exercise minute when that source was released; (3) exercise minute of the learner's frozen decision. Browser observation timestamps and authoritative or recursive resolution may be seconds/minutes apart. A later card describing an earlier record does **not** authorize a prior decision by hindsight. Preserve the initial record and add a new version as evidence changes.

**Source type distinctions:**

- **Registry/registrar administrative log:** account sessions, who is recorded as principal, MFA/role status and accepted administrative change requests. Alone it cannot prove that a DNS operator or human caused a served authoritative answer.
- **Approved DNS change log:** what RRsets, DNS provider, delegation and owner-approved revision *should* be deployed. It is an authorization source, not a live availability or cache observation.
- **Authoritative DNS answer:** what that named authoritative server serves for `qname/type/class` and its zone serial/time. An authoritative answer is a **current source-specific observation**, not a universal browser outcome.
- **Recursive resolver answer:** may reuse cached RRsets until its remaining TTL or local policy permits refresh; provider caching, DNSSEC handling, and multi-tier client/browser caching may differ.
- **Browser/HTTPS experience:** may be influenced by local cache, connection reuse, device/network and redirect chains after DNS; a visible page does not prove the underlying hostname or the payment-provider domain was correct.
- **Donation completion:** requires a trusted, separately authorized application/processor transaction receipt and reconciliation, not just a loaded page or a donor statement.

**Decision row schema:** `decision ID | source/event UTC | exercise release and freeze minutes | sources and coverage | observation vs hypothesis | competing explanations and discriminators | affected name/RRset/resolver/browser/processor | proposed action with service cost | owner/operator/independent check | requested/approved/simulated executed/verified | expiry/rollback | next trigger`.

**No-risk contract:** No actual DNS/registrar commands or account access, no rewriting domain delegation in production, no impersonating donors, no real payment-card data, no live donation, no phishing landing page, no testing an unfamiliar destination, no harvesting query/client identifiers and no secrets. A **fictional provider test transaction** mentioned later is an instructor-supplied mock receipt from a properly authorized processor sandbox, **not a transaction performed by participants**. Actual organizations must use their contracted registrar/DNS/payment processes.

**Stop card:** A participant proposes to visit the unknown destination, enter a donor payment, replay registrar session credentials, replace NS/delegation blindly, erase historical logs, flush arbitrary third-party caches without authority or claim fraud without processor evidence. Pause the exercise and require a scoped, source-backed alternative. Real emergency action belongs to the verified owner and its providers.

## 4. Progressive inject schedule and canonical fictional evidence

All case times are fictional UTC on one incident day. The 90-minute **exercise clock** is a separate teaching timer; earlier frozen decisions cannot use later findings.

| Exercise minute | Card | Case event / source time UTC | Main decision |
|---:|---|---|---|
| 0–7 | **DH-00** | 08:30 baseline | Approved zone, TTL assumptions, owners, processor boundaries |
| 8–17 | **DH-01** | 09:10–09:16 | Intermittent donor reports; page visible is not payment proof |
| 18–28 | **DH-02** | 09:17–09:21 | Authoritative/recursive observations and classification |
| 29–38 | **DH-03** | 09:24 | New registrar session; actor/change uncertainty |
| 39–48 | **DH-04** | 09:30–09:34 | Freeze and log preservation receipts |
| 49–58 | **DH-05** | 09:42 | Authorized zone rollback and independent authoritative readback |
| 59–67 | **DH-06** | 09:45–09:56 | TTL/cache contrast and sampled recursive results |
| 68–75 | **DH-07** | 10:04 | Payment processor and browser logs, impact unknown |
| 76–82 | **DH-08** | 10:18–10:22 | Registrar access rotation and independent verification |
| 83–90 | **DH-09** | 10:30–10:44 | Recovery acceptance with sampled DNS and independent donation test |
| After all freezes only | **DH-10 optional** | 11:10 | Future cache or processor exception, new source required |

### Prebrief — DH-00: authority baseline is not the live answer (minute 0)

**Fictional 08:30 signed preparation file:** HNA's registrar of record and DNS provider are named in its verified governance vault, with emergency **pre-existing** support channels. Halden and Selene control DNS change process **Z-APP-41**: `donate.harborlight-aid.example` (symbolic A-type destination) should serve **DOC-IP-GOOD** through **AUTH-A** and **AUTH-B**. Current approved zone label **ZONE-41**, serial **SER-410**, has a positive RRset TTL of **1,800 seconds (30 minutes)**. The signed change log has **no owner-approved alteration** to that destination or delegation after 08:30. The 1,800-second TTL is a *fictional zone fixture*, not a real domain recommendation.

ADS, the payment processor, is separately owned. The authorized merchant binding is **MERCHANT-GOOD** in HNA's trusted contract record; no processor log or current web transaction is supplied. HNA's policy calls for **two distinct people** to approve DNS destination changes, but the registrar's actual MFA and recent access details are not yet known.

**Decision:** Halden identifies authorized freeze scope and provider contacts; Selene identifies authoritative source-of-truth names and TTL; Fernanda/Yvette plan safe donor service continuity; Clemens names exactly what processor evidence would prove a test donation completed; Lakshmi restricts donor-personal-data collection. Mikhail does **not** label an attack from baseline policy alone.

### Round 1 — DH-01: the page loads for some people (minutes 8–17; Detect)

**Fictional 09:10–09:16:** Two permitted, **fictional** service-desk observations report differing experiences: **OBS-D1** sees a familiar-looking donation page from a managed browser; **OBS-D2** reports the donation link intermittently reaches an unfamiliar page/error presentation. Neither observer records a completed transaction, browser-origin verification, exact DNS cache state, certified screenshots or actual money movement. A synthetic support tally lists six inquiries, not a statistically representative donor population and not a count of failed donations.

**Decision:** Fernanda distinguishes **website reachability** from donation completion; Yvette activates an authorized donor-support alternative without directing people to unknown pages. Sable requests safe source-labeled website/redirect observations in an approved isolated browsing workflow; never open an unknown address from a live user machine in this tabletop. Mikhail opens **HNA-IR-010** as *intermittent domain-routing integrity discrepancy*, suspected hijack among alternative causes. Halden initiates registrar and DNS provider coordination.

**Alternatives:** Misconfigured authoritative zone, incomplete publication to secondaries, legitimate cached earlier answer, different browser paths, or unauthorized administrative change could all contribute. **No evidence** yet proves phishing, a stolen donation or a payment-provider breach.

### Round 2 — DH-02: served authoritative state differs from the approved change log (minutes 18–28)

**Fictional 09:17–09:21 read-only DNS observations**, all for the same symbolic name/type/class, with source name, serial, time and TTL provenance recorded:

| Source and clock | Answer / revision | Directly supported observation | Boundary |
|---|---|---|---|
| **AUTH-A**, 09:17 | **DOC-IP-UNKNOWN**, **SER-411** | Authoritative server serves unapproved-by-register destination at this checkpoint | Not proof of actor, malicious content or delivered browser visit |
| **AUTH-B**, 09:18 | **DOC-IP-GOOD**, **SER-410** | Second authoritative server still serves prior approved zone | Inconsistent authoritative state; not proof that AUTH-B is universally right |
| **REC-R1**, 09:19 | **DOC-IP-GOOD**, remaining TTL 900 seconds | Sample recursive sees approved answer | Could be cached; cannot prove current authoritative uniformity |
| **REC-R2**, 09:20 | **DOC-IP-UNKNOWN**, remaining TTL 1,500 seconds | Sample recursive sees unfamiliar answer | May be cache or recent authoritative response; not its original source |
| **Browser BR-1**, 09:21 | Familiar-looking page | Application/UI observation only | Does not identify resolver cache path, TLS origin or payment completion |

**Decision and worked inference:** With the supplied **complete approved change log Z-APP-41**, **AUTH-A at SER-411 serves a destination outside the approved zone**; this is a specific **unapproved-by-register authoritative configuration state**, not yet proof of how it arose. AUTH-B lags/matches previous state, while two recursive samples differ. A page can appear normal for some donors **while another resolver retains an unfamiliar answer**. Halden directs a scoped investigation and prepares a controlled change freeze; Selene records qname/RR type/TTL/server/serial rather than declaring the whole Internet has been redirected.

**No unwarranted leap:** Many DNS records or DNS service identities could be involved, but this card shows only the named RRset and two authoritative servers. Do not assert that the registry delegation changed, that DNSSEC validated the unknown record, or that any donor submitted data to it.

### Round 3 — DH-03: a new registrar session is an investigative lead, not human attribution (minutes 29–38)

**Fictional 09:24 preserved registrar audit summary:** An account history query shows registrar session **REG-S59**, established at **09:04 UTC** under administration role **REG-OPS**, with network label **NET-NEW** that is not in the current approved operator shift log. The report lacks confirmed human operator/device identity, trusted MFA event correlation, session action list completeness and DNS provider API linkage. Another summary mentions a zone publication activity near 09:12 by **DNS-PUBLISHER**, a different service identity; no source binds REG-S59 to that publication. The audit does **not** show a completed registrar transfer, nameserver delegation change or definitively compromised account.

**Competing explanations:** H1 unauthorized registrar or DNS-service access; H2 legitimate but undocumented shift/provider maintenance; H3 erroneous approved-system publication; H4 stale/partial authoritative synchronization plus recursive caching; H5 combinations. Do not treat every hypothesis as equally likely or infer a criminal actor from a network label.

**Decisions:** Octavia obtains trusted provider confirmation of session source/actions and account-recovery options **via the pre-existing channel**; Nerissa seeks authorized minimal registrar-session and DNS-publisher audit copies; Selene compares the actual zone revision chain; Mikhail records the need to test whether REG-S59 was even permitted to modify this RRset. Halden does not authorize blind delegation edits. Lakshmi ensures personal account audit collection remains limited and lawful.

### Round 4 — DH-04: freeze registrar changes and preserve history without destroying it (minutes 39–48; Respond)

**Fictional 09:30–09:34 authorization/evidence card:** Halden signs **REG-FREEZE-A30**, a time-bounded instruction to the **verified registrar contact** to suspend unauthorized/pending administrative domain changes while the case is assessed. Octavia records registrar acknowledgment **REG-FREEZE-ACK32**, but the card says only that the registrar has placed **the specified account's high-risk change workflow into review/hold**; independent observation of all account actions, all delegated DNS-provider APIs and all caches is **not** provided. **Do not conflate a registrar transfer lock with a universal lock on DNS RRset changes.**

Nerissa obtains a **read-only registrar-session source archive** and **DNS zone/history export** as **SRC-REG-33** and **SRC-ZONE-34**, with named collector/source/UTC scope. A separate verification of copies' bytes is **requested**, not yet completed. The canonical source/zone history is preserved before any proposed rollback. The frozen log shows **no approval** for SER-411 in the complete scoped change ledger, but still lacks identity of actor.

**Decision:** Halden approves a **narrow freeze** and consultation about provider-side publishing rights; Selene plans a reviewed restore of the named unauthorized RRset, not wholesale domain transfer, DNSSEC key replacement or registrar account reset without dependency review. Octavia ensures the registrar knows how an emergency approved change would be allowed **under a verified owner process**. Yvette handles donor-service impact. Mikhail refuses to claim the freeze automatically removed cached unknown answers.

**Conditional:** If the freeze would also block the controlled fix, the verified registrant and provider must approve a specifically bounded emergency restoration exception; do not defeat security by publishing in an untracked side channel.

### Round 5 — DH-05: correct the authorized source and independently observe authoritative convergence (minutes 49–58)

**Fictional 09:42 source-controlled DNS restoration:** Halden signs **ZONE-RESTORE-42** to restore the named donation RRset to **DOC-IP-GOOD** from the previously signed Z-APP-41/ZONE-41 baseline; Selene prepares a versioned candidate through the provider's approved review pipeline, and distinct DNS change approver **Octavia** witnesses the independent authorization. Operator receipt **DNS-APPLY-43** states publication of the **new revision SER-412** at 09:43, leaving unrelated records/delegation untouched. A separate authorized read-only observer obtains **AUTH-READ-45** at 09:45: **AUTH-A and AUTH-B both serve DOC-IP-GOOD at SER-412** for the exact donation name/type. A source/copy integrity receipt **HASH-46** at 09:46 verifies the archived registrar/zone extracts' **acquired bytes**, not the completeness or truth of each original log.

**Decisions:** A verified **current authoritative-zone recovery** is supported for that RRset at 09:45. It does **not** establish which recursive resolvers still cache an earlier answer, which browser connected previously, whether donations were processed or whether the registrar identity is trustworthy after the incident. Selene and Octavia coordinate TTL/caching expectations with the authoritative DNS provider and registrar. Halden leaves registrar access remediation and payment review pending.

**Why no immediate universal 'all clear':** The authoritative answer is the source-of-truth observation **now**, but DNS clients may still use earlier recursive/browser caches until expiry/revalidation. A correct answer cannot undo a past misroute or determine historic visits.

### Round 6 — DH-06: caches are a separate, source-bound restoration problem (minutes 59–67)

**Fictional 09:45–09:56 sample:** The previous zone records used **1,800 seconds** positive TTL. At the 09:45 restored authoritative checkpoint, REC-R1 still returns DOC-IP-GOOD; **REC-R2 still returns DOC-IP-UNKNOWN** with **1,000 seconds remaining TTL** on a response cached earlier; REC-R3 returns DOC-IP-GOOD on an independent sampling channel. At **09:56**, REC-R2 reports DOC-IP-UNKNOWN with **340 seconds remaining** (a difference of 11 minutes = 660 seconds), and the new authoritative zone still reports DOC-IP-GOOD. This is **one synthetic recursive cache** complying with decrementing TTL for the supplied interval, not an exhaustive model of the Internet.

**Reproducible arithmetic:** At 09:45, REC-R2 remaining TTL 1,000 seconds = **16 minutes 40 seconds**. Eleven minutes later (660 seconds), expected remaining TTL = 1,000−660 = **340 seconds** = **5 minutes 40 seconds**. If no refresh/eviction policy changes and the resolver honors that TTL, a cache purge/re-query may happen **at or before roughly 10:01:40 UTC**. This is a **conditional estimate for REC-R2's reported cache**, **not** an instruction to flush someone else's resolver and **not** a global propagation deadline. Replacing the authoritative RRset with a shorter TTL **today** does not shorten an answer that REC-R2 already cached under an earlier TTL. Browser caches, local resolvers, CNAME chains, and negative caching (if it occurred) require separate observations.

**Decision:** Selene avoids declaring an active newly compromised authoritative server solely from REC-R2's stale answer. Yvette ensures donors are given an approved support/alternate contact without directing them to an unknown site; Sable and Fernanda maintain browser/origin/processor uncertainty; Mikhail requests sampling that records which source, qname, type, remaining TTL and time were checked. Do not silently reinterpret an old cache as an active new zone mutation.

### Round 7 — DH-07: payment provider truth is not visible in DNS logs (minutes 68–75)

**Fictional 10:04 read-only application and payment packets:** Sable's approved web access-log summary for the affected period contains **120 HTTPS requests to the trusted donation page origin** and **35 simulated checkout-button events** during a specified sample. These are counts of web events, not unique donors, authorized checkout initiations or completed donations. Because DNS/browser routing was inconsistent, the official web logs **do not cover users who may have reached an unfamiliar address**. Browser-path provenance and TLS identity are only partially reconstructed.

Clemens receives ADS's authorized **merchant activity statement PAY-SCOPE-04** for merchant **MERCHANT-GOOD** in the **09:00–10:00 UTC provider reporting window**: it explicitly reports that **the submitted settlement/reconciliation dataset for that window is still pending** and supplies **no verified count of completed, declined, canceled, diverted or disputed transactions**. It contains no indication of processor compromise, but the lack of a finding in this incomplete view is **not** proof of no issue. No independent provider evidence is supplied about an unknown destination or another merchant account.

**Decision:** Fernanda/Clemens preserve claims as **“donation outcome unknown; no established loss, payment diversion or processor compromise.”** Lakshmi determines if limited donor inquiries and contract/payment-provider correlation are warranted, with confidentiality and minimization. Mikhail will not convert 35 button events into “35 lost donations” or 120 HTTPS requests into successful charges. Sable checks application/site identity and certificate/redirect-chain questions through **safe provider-owned logs/fixtures**, not visits to the unfamiliar destination. Mireya drafts cautious operational copy rather than fundraising alarm claims.

**Negative control:** A trusted official donation page loading for one sampled browser does not prove other browsers saw the right site earlier, nor that their donations completed. A suspicious DNS RRset is not direct payment processing evidence.

### Round 8 — DH-08: revoke untrusted registrar sessions and restore administrative trust (minutes 76–82)

**Fictional 10:18–10:22 IAM/registrar receipts:** Halden authorizes **REG-ACCESS-18** to revoke named old registrar sessions, rotate authorized registrar access and enroll individually accountable authorized people in the registrar's MFA mechanism. Octavia executes through a **separate verified registrar support/admin workflow**; provider operation **REG-APPLY-20** says sessions including REG-S59 have been terminated and registrar access credentials rotated. Independent registrar account/security readback **REG-STATE-22** confirms, **for the named account at 10:22**, MFA is enabled for the two designated administrators and the stale sessions are absent from the active-session list. Recovery contacts and an emergency owner-review workflow are revalidated without using a domain-hosted mailbox alone as the only recovery dependency.

**Decision:** Halden and Octavia may mark **bounded registrar administration containment** for the specified account. They cannot claim the historic REG-S59 user was malicious, that an earlier DNS provider API session is necessarily terminated, or that every historical DNS answer has expired. Selene checks separately controlled authoritative DNS publication identities; Mikhail/Nerissa retain source evidence and open attribution issues. The revised change-control rule requires two distinct named reviewers for future changes.

**Registrar lock nuance:** ICANN explains that registrar/transfer locks may protect transfers, but the exact lock and what it prevents depends on registrar functionality; it is **not** evidence that every DNS record is immutable. [ICANN guidance for registrants](https://www.icann.org/en/blogs/details/do-you-have-a-domain-name-heres-what-you-need-to-know-26-3-2018-en) recommends unique passwords, multistep authentication where available and transfer-lock review. The simulated governance gates are HNA's original exercise policy, not ICANN-imposed incident choreography.

### Round 9 — DH-09: bounded DNS and donation-flow acceptance with residual cache uncertainty (minutes 83–90)

**Fictional 10:30–10:44 independent verification packet**, released only after DH-08 freezes:

- **AUTH-FINAL-30:** A qualified read-only observer checks both **AUTH-A** and **AUTH-B**, receiving **DOC-IP-GOOD** at **SER-412** for the named donation RRset and confirming the approved source revision under Halden/Selene's access policy.
- **REC-FINAL-33:** A separately sampled set of **REC-R1, REC-R2 and REC-R3** returns **DOC-IP-GOOD** with source/time/TTL recorded at 10:33; a fourth known remote resolver **REC-R4 is not sampled** and some browser/local caches remain unknown. The sample is **3 of 3**, not “all public resolvers.”
- **SITE-34:** Sable and Fernanda receive a fictional authorized managed-browser/HTTPS route review attesting that **the sampled donation page** presents the approved HNA site identity, correct tested navigation and the **known ADS checkout binding**; it is not a retrospective observation of affected donors.
- **PAY-TEST-36:** Clemens and a separate ADS-qualified verifier supply a **fictional processor sandbox**, **nonmonetary** test record for **MERCHANT-GOOD**: an approved test donation journey completed with matching website state, payment-provider sandbox acknowledgment, exact test transaction correlation and independent receipt verification. **No real donation or payment occurs in the exercise.**
- **PAY-HISTORY-OPEN:** The earlier 09:00–10:00 reporting reconciliation and any possible diversion/fraud inquiry are still **not substantiated** by complete provider logs. Browser caches and recursive resolvers outside the sample may retain stale states.

**Decision:** Halden can sign a **limited domain/site/donation-path operational return** for the observed RRset, resolver sample and independently tested sandbox flow. Fernanda/Clemens accept only the tested donor experience and processor binding, not actual historic donation totals. Mikhail keeps session attribution, residual caches, possible past website exposure and payment impact as **explicit open questions**. Lakshmi approves truthful donor communications, not a claim of universal safety or “no losses.” A team may require further sample diversity before broader acceptance; it must identify the missing evidence without moving the historic goalposts.

**Critical acceptance wording:** “At 10:30–10:44, two sampled authoritative servers and three sampled recursive resolvers served the approved destination; an authorized sandbox flow completed with independent ADS confirmation. **Other caches, earlier browser destinations and historical donor outcomes remain unknown.**” This is stronger than an unsupported general “DNS fixed, all payments safe.”

### DH-10 — Optional future branch only, after final freeze

At a **later** fictional 11:10 a facilitator can release a **new, independently sourced** payment-processor reconciliation or remote-recursive result. A confirmed additional authorized donation or a documented mismatch would change later decisions only within its exact period. Neither is present in the canonical exercise, and neither can be invented to retroactively validate an earlier statement, assign a fraud loss or identify REG-S59's actor.

## 5. Technical mechanism: why correct DNS now does not prove correct donations earlier

**Authoritative data:** A validated name/type/class answer from AUTH-A/B describes what those named zone servers served at the measured time. The zone revision serial **SER-411** on AUTH-A was outside approved Z-APP-41, while AUTH-B still served SER-410. That is **authoritative inconsistency and a specific authorization gap**, not proof of a registrar transfer or a malicious web page.

**Recursive caching:** A resolver answering from cache can return an earlier resource-record set while current authoritative servers are correct. The TTL attached to cached data constrains ordinary remaining lifetime, but the timestamp of the cache fill, how local resolvers apply TTL limits, cached CNAME dependencies and browser caches matter. The **same name** can appear intermittent to different users if their recursive resolvers cached different answers at different times. No central participant can guarantee that every resolver instantly purged a prior answer.

**Browser and HTTPS:** DNS resolution chooses an addressing path, not what the complete browser session eventually displays. Connection reuse, HTTP redirects, HSTS/TLS validation, CDN, proxy and browser cache state may differ. A visible familiar-looking donation page does not prove the effective origin, processor handoff or prior user experience. A DNSSEC-valid answer (not supplied here) would authenticate appropriately signed DNS data; it would **not** attest to the nonprofit's authorized business change or a payment's legitimacy.

**Payment outcome:** Only the processor and trusted organization transaction evidence can establish what was authorized, captured, settled, refunded or disputed. Even **provider data** need timestamp, merchant identity, scope and reconciliation coverage. A page hit or checkout button event is not a completed transfer or fraud-loss unit.

### Worked evidence ladder

| Proposed statement | Source supporting it | Defensible conclusion or limit |
|---|---|---|
| Domain donation RRset differs from approved change log | DH-00 Z-APP-41; DH-02 AUTH-A at SER-411 | **Confirmed unauthorized-by-register authoritative state**, actor/cause not proved |
| Registrar session was new | DH-03 REG-S59 under REG-OPS | Session exists; human identity/actions/connection to DNS publication not proved |
| Some recursive resolvers return unfamiliar address | DH-02 REC-R2; DH-06 cache | **Observed cache answer** at given source/time; could remain after authoritative fix |
| A donor page worked for some | DH-01 OBS-D1 | A page observation, not origin/processor identity nor completed donation |
| Registrar change freeze requested and acknowledged | DH-04 REG-FREEZE-A30 / ACK32 | Specified high-risk change workflow placed on hold; not every delegated API frozen |
| Authoritative zone now matches approved | DH-05 AUTH-READ-45 | Exact RRset at AUTH-A/B matches SER-412; recursion/user paths separate |
| Session/credential rotation was verified | DH-08 REG-STATE-22 | Bounded named registrar account; external DNS identities and historic actor unknown |
| Sampled recursive destination is approved | DH-09 REC-FINAL-33 | Three sampled recursive sources now good; caches elsewhere unknown |
| A donation flow completed independently | DH-09 PAY-TEST-36 | **Synthetic approved sandbox test**, not a real payment or historical reconciliation |
| Donations were stolen / processor compromised | **No supplied evidence** | **Not established**; do not write a monetary total or breach accusation |

**No structural diagram:** A generic resolver-to-browser-to-processor arrow chain could misleadingly imply an observed network path. The evidence ladder and source matrix give the necessary mechanism and provenance without fictional wiring presented as measured fact.

## 6. Reproducible TTL and sample analysis: independent negative controls

**Fixed classroom data, no DNS software required:**

| Checkpoint | AUTH-A | AUTH-B | REC-R1 | REC-R2 | REC-R3 | Payment outcome |
|---|---|---|---|---|---|---|
| DH-02, 09:17–09:21 | UNKNOWN / SER-411 | GOOD / SER-410 | GOOD / TTL 900 | UNKNOWN / TTL 1,500 | Not sampled | Not observed |
| DH-05, 09:45 | GOOD / SER-412 | GOOD / SER-412 | Not resampled | Not resampled | Not sampled | Not observed |
| DH-06, 09:45 | GOOD / SER-412 | GOOD / SER-412 | GOOD | UNKNOWN / TTL 1,000 | GOOD | Not observed |
| DH-06, 09:56 | GOOD / SER-412 | GOOD / SER-412 | Not resampled | UNKNOWN / TTL 340 | Not resampled | Not observed |
| DH-09, 10:30–10:44 | GOOD / SER-412 | GOOD / SER-412 | GOOD | GOOD | GOOD | Sandbox receipt; history pending |

The symbolic columns GOOD/UNKNOWN mean **DOC-IP-GOOD** and **DOC-IP-UNKNOWN**, not real IPs. Blank/unmeasured cells are **not** zero or evidence of absence.

**Calculations and scope:**

1. DH-02 authoritative sample at the same approximate checkpoint: **1 of 2** sampled authoritative servers served an approved answer (50% of that tiny named pair), while **1 of 2** served an unapproved-by-register destination. This cannot be projected to public traffic percentages.
2. DH-02 recursive sample: **1 of 2** returned GOOD; **1 of 2** returned UNKNOWN. A resolver result is not a donor, and the samples were not a random population survey.
3. DH-05 authoritative sample: **2 of 2** serve GOOD at SER-412. This verifies that pair at **09:45**, not every delegated server in existence or all caches.
4. From **09:45 to 09:56** is **11 minutes = 660 seconds**. REC-R2 TTL **1,000−660 = 340 seconds**; a conditional remainder of **5 minutes 40 seconds**. If it continues decrementing without refresh, expiration is at approximately **10:01:40**. A browser's own cache may behave differently. Do not rewrite or externally flush resolver state in this exercise.
5. DH-09 recursive sample: **3 of 3** approved after the later monitoring period. The correct general conclusion is “all **sampled** recursors returned the approved destination at the named times”; it is invalid to claim “100% of Internet clients are safe.”
6. DH-07 **120** web origin requests and **35** button events have **no denominator linking them to distinct donations** and lack a completed provider record. They cannot be converted into stolen, failed or completed donations. The DH-09 sandbox receipt counts **one fictional authorized test**, not historic donor funds.

**Mandatory negative controls:**

- **NC-1:** Authoritative GOOD at two servers does not flush or invalidate all recursive/browser caches.
- **NC-2:** REC-R2 returning UNKNOWN after the fix does not necessarily prove a *new* malicious zone change.
- **NC-3:** Registrar session REG-S59 does not prove a specific human made zone changes.
- **NC-4:** A registrar **transfer lock** is not necessarily a DNS-record modification freeze.
- **NC-5:** A signed zone log describes authorization, not live authoritative propagation.
- **NC-6:** DNSSEC validation (if present) would not prove the RRset was authorized by HNA's business owner.
- **NC-7:** An ordinary page load or HTTPS status does not prove a completed donation.
- **NC-8:** A processor merchant-test pass cannot establish the outcome of earlier unknown donor journeys.
- **NC-9:** Absence of anomalies in incomplete provider logs is unknown, not a “zero losses” conclusion.
- **NC-10:** A shorter TTL set after an event does not shorten an answer already cached under an earlier TTL.
- **NC-11:** A good three-resolver sample is not a global census or a guarantee against future drift.
- **NC-12:** A later receipt must not be imported into a previous frozen decision.

### Independent practice EX-TTX10-01 — Observation, hypothesis and ownership

**Objective:** distinguish a zone authorization gap from actor and payment claims. **Inputs:** DH-00 to DH-03 only. **Task:** classify: (a) AUTH-A serves an unapproved-by-register destination, (b) registrar account definitely compromised, (c) REG-S59 operator changed DNS, (d) donor funds stolen, (e) AUTH-B still serves an approved zone. For each write source/time, observation/hypothesis/unsupported, discriminator and responsible team. **Artifact:** five-row frozen claim matrix. **Rubric:** 2 points per accurate source/limit pair = **10**.

### Independent practice EX-TTX10-02 — Preservation, freeze and controlled restoration

**Objective:** apply proportionate owner authorization without destroying source history. **Inputs:** DH-03 to DH-05. **Task:** compare (A) wholesale registrar transfer/delegation reset, (B) Halden-approved account change freeze with independent registrar acknowledgment, read-only archives and reviewed donation RRset restoration, (C) immediate “all clear” from one authoritative answer. Record separate `approved / applied / independently verified` states, rollback owner and donor-service cost. **Artifact:** decision envelope A3. **Rubric:** 2 authority, 2 evidence preservation, 2 narrow scope, 2 honest verification = **8**.

### Independent practice EX-TTX10-03 — Resolver TTL and temporal evidence

**Objective:** explain why a corrected zone and a stale recursive cache can coexist. **Inputs:** DH-02, DH-05 and DH-06. **Task:** calculate REC-R2 TTL remainder after eleven minutes and conditional expiry time; write two things the TTL **cannot** establish; compare authoritative versus sampled recursive evidence. **Artifact:** time/source matrix with worked seconds. **Rubric:** 2 arithmetic, 2 source boundaries, 2 conditional timing, 2 remaining gaps = **8**.

### Independent practice EX-TTX10-04 — Donations are not inferred from pages or DNS

**Objective:** preserve payment-impact uncertainty and processor/source roles. **Inputs:** DH-01, DH-07 and DH-09 in release order. **Task:** construct distinct statuses for web page reached, checkout-button observed, processor-authorized test completion, historical transaction capture/settlement and unknown recipient interaction. State whose independent records would be needed for a donation-loss or data-disclosure claim. **Artifact:** safe donor-impact sheet with no PII or real merchant values. **Rubric:** 2 distinctions, 2 trusted provider, 2 uncertainty, 2 privacy/communication = **8**.

### Independent practice EX-TTX10-05 — Conjunctive recovery and residual caches

**Objective:** decide a bounded operational return under residual historical uncertainty. **Inputs:** DH-05, DH-06, DH-08 and DH-09. **Task:** score gates G1–G10 as pass/pending/not evaluated; freeze one decision before DH-09, then a separate final one. Require both authoritative sources, a named recursive sample, registrar access remediation, site identity and independently verified sandbox donation completion. List what remains unknown. **Artifact:** signed owner/processor acceptance and monitoring handoff. **Rubric:** 2 chronology, 2 DNS state, 2 processor evidence, 2 residual-cache/historic limits = **8**.

## 7. Containment alternatives, consequences and source custody

The table lists **fictional response options**, not executable domain takeover or DNS modification instructions. Only authorized real-world domain, DNS and payment providers can act in production.

| Alternative | Necessary owner authority and evidence | Conditional effect and failure mode |
|---|---|---|
| **A. Freeze high-risk registrar changes** | Halden verified registrant; Octavia authenticated pre-existing provider channel, scoped freeze and readback | Constrains named registrar workflow, not cached answers or all external DNS provider APIs |
| **B. Preserve session, zone and DNS logs before scoped restore** | Nerissa permitted source exports with collector/time/retention and independent copy-readback | Captures a bounded history; preserve state without relying on hashes as proof of truth |
| **C. Controlled restore of unapproved RRset** | Halden owner, Selene DNS review, second change approver, signed Z-APP-41 and distinct operator/readback | Corrects named authoritative state prospectively; earlier cache/browser history remains |
| **D. Blindly replace domain delegation/registrar** | Would require independent verified need, dependency assessment and higher-risk authorization **not supplied** | Reject; can disrupt legitimate site/email and obscure root cause |
| **E. Rotate trusted registrar access and enforce MFA** | Halden/Octavia verified account, revocation/rotation receipt, independent account-state verification | Narrows future account misuse risk, but cannot determine who used REG-S59 earlier |
| **F. Shorten DNS TTL and declare instant propagation** | Provider/owner TTL review and source-specific monitoring would be required | Reject instant claim: caches holding old records retain their own remaining TTL |
| **G. Ask donors to retry via an unverified link** | No acceptable recipient/trust justification | Reject; worsens impersonation or duplicate-charge risk |
| **H. Direct donors to approved continuity channel** | Yvette/Fernanda/website owner and legal review; avoid collecting payment data outside ADS | Maintains support, but does not establish completed payments or recover hypothetical losses |
| **I. Publicly announce stolen donations or phishing** | Direct page/content/payment-provider and lawful evidence necessary | Unsupported from this case, even with a clearly wrong zone entry |
| **J. Accept bounded return after DH-09** | Halden/DNS/registrar/website/processor owners and independent tested receipts | A sampled operational recovery; historic donor outcomes and unsampled caches remain unresolved |

### Evidence custody: minimum source set, maximum restraint

1. **Source ownership:** identify registrar of record, contracted DNS authoritative provider, nonprofit domain owner, web host and payment processor. Do not assume the same admin identity controls all layers.
2. **Read-only sources:** request named registrar-session and change history, zone serial/version snapshots, authoritative answer observations, recursive samples, web request/redirect summaries and processor confirmation scope through approved channels.
3. **Source/copy/analysis separation:** keep exact query name/type/class, authoritative versus cached status, source ID, event/collection UTC, TTL remaining, operator and immutable copy reference. Preserve registrar logs before rotation where feasible without permitting continuing abuse indefinitely.
4. **Approval trail:** preserve the signed zone-change ledger and independent registrar/DNS change approval, including any deliberately empty approved change list for the incident period.
5. **Identity limitations:** new session plus new zone revision is **correlation**, not a human identity or proven causal chain. Review signed provider activity and the allowed paths before attributing actions.
6. **Data minimization:** provider transaction evidence may contain sensitive donor data. Use anonymous counts, transaction-status metadata and trusted processor references; any personal/card data acquisition requires separate lawful necessity and access controls.
7. **Administrative containment:** process the owner-approved registrar freeze, DNS provider restriction and session rotation as separate controls with separate receipts. A request made is **not** the same as an applied freeze or a verified absence of active sessions.
8. **Controlled zone rollback:** use the approved prior revision and a versioned, reviewed change, avoiding blanket modification of unrelated DNS, MX, nameservers or security settings. Independent provider-authoritative readbacks determine actual current state.
9. **Cache and user revalidation:** define source-diverse and timed recursive samples, sample browser/site TLS identity and redirect behavior and track results over relevant TTL windows. No blanket "Internet propagated" claim from a few points.
10. **Processor reconciliation:** accept donation completion only from authorized, independently verified provider transaction evidence, and keep historical reporting gaps explicit; do not infer lost funds by subtraction of page views.
11. **Continuity and legal/communications:** notify staff/donors only with owner, legal and payment-reviewed facts, a safe approved contact and a next update trigger. No invented regulator or notification clock.
12. **Handoff and ongoing monitoring:** record which RRsets/administrator identities were checked, source clocks, unexamined caches, open provider cases and external drift alarms with named owners.

**Tradeoff example:** At DH-04 an executive proposes immediate changes to all nameservers. Yet only one donation RRset is observed wrong and the registrar session-to-publication link is unknown. A narrow owner-approved freeze and preservation plus a reviewed single-RRset restore minimizes collateral outage and retains root-cause sources. If a new source later proves delegation itself is maliciously changed, a distinct authorized change decision could be justified; this is **not** an observed DH-04 fact.

## 8. Recovery acceptance gates, TTL monitoring and risk limits

**No single success proves restoration.** Authoritative answers, recursive caches, registrar access, website/TLS and payment processor evidence each require a **distinct source and owner**. A recovery worksheet records `pass / fail / pending / not evaluated` against a time and exact observation window.

| Gate | Required independently verifiable receipt | Accountable owner and rejection rule |
|---|---|---|
| **G1 registered owner/authority** | Verified domain registrant, approved Z-APP-41, two-person DNS change policy, provider support contacts | Halden: no change on email-only claim or invented owner |
| **G2 preservation and provenance** | Historical registrar session source, zone/source revisions, archive/copy status, acquisition/UTC/limits | Nerissa: no erased history or invented attribution |
| **G3 registrar change freeze** | REG-FREEZE-A30 and ACK32 for scope, plus provider-side activity follow-up | Octavia/Halden: transfer lock alone is insufficient |
| **G4 approved authoritative zone** | AUTH-A/B answer on exact RRset/serial SER-412, signed owner restore and independent readback | Selene: one correct authoritative server is not convergence |
| **G5 access trust restored** | REG-APPLY-20, REG-STATE-22 and scoped MFA/session check, independent administrator | Octavia: password reset request is not all-session revocation |
| **G6 recursive cache samples** | Source-diverse REC-R1/R2/R3 times/answer/remaining TTL, with unsampled REC-R4 recorded | Selene: three samples do not prove every resolver or browser cache |
| **G7 application/site identity** | Approved browser test identity/TLS/site/redirect chain and named ADS handoff in managed fixture | Sable/Fernanda: correct DNS RR is not a secure rendered page |
| **G8 donation completion** | Authorized processor sandbox flow with correlation, ADS acknowledgment and independent test receipt | Clemens: page view or button is not settled donation |
| **G9 historical payment/data impact** | Complete relevant provider reconciliation, coverage of past paths/merchant IDs and legal/privacy owner decision | Clemens/Lakshmi: **pending**; no asserted fraud-loss number |
| **G10 monitored return and communications** | Owner-signed bounded operational decision, external drift sample cadence, safe donor support, review window and truthful message | Halden/Gideon/Mireya: no permanent universal all-clear |

**At DH-02:** 1/2 of sampled authoritative answers differs from the approved source, so a domain-routing incident is active and unconditional restoration is **NO-GO**.  
**At DH-04:** Registrar freeze acknowledgment is bounded; caches and authoritative mismatch remain, so site/donation acceptance is **NO-GO**.  
**At DH-05:** 2/2 sampled authoritative servers serve the restored revision, but recursive caches can still retain UNKNOWN. **Do not reopen as fully safe** solely on authoritative recovery.  
**At DH-06:** REC-R2 continues to hold a stale unfamiliar answer with decreasing TTL. Monitor and maintain donor continuity; do not invent a global cache flush.  
**At DH-08:** Registrar credentials are rotated, session revocation/MFA verified for the account; donation/browser acceptance is still pending.  
**At DH-09:** Independent authoritative + named recursive + site-identity + payment-sandbox evidence can support a **limited operational go** for the sampled/current workflow. G9 historic donation/data impact remains **pending**, and unknown caches/clients remain in G6 monitoring.

**Important timing distinction:** If a large segment of donor browser caches remains unknown, a real organization's acceptance policy might require additional sampled resolution or a longer monitoring interval. The classroom describes a **bounded** result, not a universal declaration of safety. No "zero lost donations" statement is warranted.

## 9. Participant artifacts and evaluation rubric

Participants submit six source-backed, **frozen** artifacts before the debrief. The observer scores the original submitted versions, not oral explanations after future cards arrive.

| Artifact | Required content | Observer's discriminating question |
|---|---|---|
| **A1 timeline and source boundaries** | Source UTC, release/freeze minute, qname/type/serial/TTL, authoritative/recursive/browser/provider distinctions | Did someone cite DH-09 in a DH-02 decision? |
| **A2 registrar/zone authority matrix** | Z-APP-41, AUTH-A/B, REG-S59, DNS publisher, alternate causes and missing binding | Does a new session identify who altered the zone? |
| **A3 containment/change/evidence receipt** | Owner freeze, archive/copy integrity, exact RRset restore, distinct approvals, applied/readback/rollback states | Is a transfer lock confused with a zone edit freeze? |
| **A4 cache/browser status and calculations** | REC-R1/2/3 observed answers, TTL math, unsampled resolvers/browser uncertainty and no universal deadline | Does a current GOOD authoritative answer prove no stale cache? |
| **A5 donor/payment risk and acceptance** | ADS merchant ID, website/TLS/processor test receipts, historic reporting gaps, continuity and open legal/privacy issues | Which record proves a completed donation, not a button click? |
| **A6 communication, rubric and backlog** | Draft/reviewed/sent distinctions, no unfounded loss claim, owners, measured drift/MFA/dual approval retests | Are people reassured or alarmed beyond the evidence? |

**Ten-criterion educational rubric:** **0** = missing or contradicted, **1** = relevant but missing a critical source/clock/scope/authority/limit, **2** = bounded, reproducible and independently supportable. Maximum **20**. The roles and scoring are **original classroom constructs**, not NIST or ICANN compliance tests. Two independent observers cite the exact released card and frozen artifact. If the facilitator failed to release a required card, mark the corresponding criterion **not observed / exercise defect**, rather than zeroing the learner.

| Criterion | Two-point evidence |
|---|---|
| **C1 domain owner and registrar authority** | Exact registrant/registrar/provider distinction and verifiable contact path |
| **C2 DNS source semantics** | Authoritative vs recursive vs browser; named record/serial/TTL and limited sample |
| **C3 correct factual classification** | Unapproved zone state, session anomaly and non-attribution correctly separated |
| **C4 safe containment** | Scoped owner freeze, immutable source/copy record, dual-reviewed RRset restore |
| **C5 cache reasoning** | 1,000−660=340 s; no claim of global propagation or retroactive TTL shortening |
| **C6 administrative recovery** | Verified registrar session rotation, MFA and limits of transfer lock |
| **C7 payment/data humility** | No conversion of 35 button events to donations; pending historical provider statement |
| **C8 site and donation verification** | Safe authorized browser/HTTPS test and independent processor sandbox acknowledgment |
| **C9 recovery chronology** | DH-02/05/06/09 distinct frozen verdicts, source-diverse sample and remaining caches |
| **C10 improvement/communication** | Bounded notice, no phishing/loss accusation and measurable owner/dual-approval/drift fixes |

**Noncompensable stops:** Using a real registrar credential, publishing attack or takeover instructions, making real DNS or payment changes for the exercise, visiting unfamiliar site with donor data, falsely claiming a domain/processor is fully secure, manufacturing stolen-donation totals, erasing relevant history or conducting unauthorized personal-data collection. Stop, record the **critical safety/process failure**, and have real-world professionals follow their actual provider plans. Classroom interpretation: **17–20 strong**, **12–16 material gaps**, **0–11 major rework**, always stating skipped cards and independent reviewer disagreement.

## 10. Facilitator worked answers, counterexamples and independent practice solutions

**Keep this section hidden until the matching stage is frozen.** Another path earns credit if evidence, rights, operational side effects and independent checks are comparably sound. Never make late evidence retroactively available.

| Card | Defensible worked decision and mechanism | Common wrong inference and correction |
|---|---|---|
| DH-00 | Signed Z-APP-41 is the allowed target; contract identifies registrar, DNS and ADS owners | “Approved zone means it is served everywhere.” Check actual authoritative source |
| DH-01 | Classify intermittent domain integrity issue with no payment verdict; support donors safely | “Page works for me, so no incident.” Which resolver/browser/processor source? |
| DH-02 | AUTH-A SER-411 wrong-by-register, AUTH-B SER-410 approved; recursive samples disagree | “Someone hijacked and stole money.” Which human/payment evidence? |
| DH-03 | REG-S59 is a session, not actor or zone change; seek action/MFA/provider join | “New network means attacker.” Who actually performed which action? |
| DH-04 | Owner freeze + provider ACK scoped; preserve registrar/zone originals; restore narrowly later | “Registrar locked means all DNS immutable.” What does exact lock cover? |
| DH-05 | Two authoritative answers now on SER-412, but cache/processor state open | “DNS corrected everywhere.” How do caches behave? |
| DH-06 | REC-R2 remains UNKNOWN under TTL; compute remainder and sample further | “Stale recursor proves fresh compromise.” What was its prior cache? |
| DH-07 | 120 web hits and 35 button events are not completed donations; ADS history incomplete | “35 donations lost.” Where is provider transaction reconciliation? |
| DH-08 | Bounded registrar session rotation and MFA; DNS provider identity and historical cause separately open | “MFA enabled now proves session was never abused.” When is the claim supported? |
| DH-09 | Source-specific authoritative + three recursor + web identity + sandbox processor pass: bounded return | “All donors received money, no phishing.” Which historical/browser evidence exists? |
| DH-10 optional | Future evidence is a new dated update only | “Later evidence validates earlier confident statement.” Freeze timing matters |

### Worked answer — EX-TTX10-01

(a) **Observed unapproved-by-register authoritative state** at AUTH-A SER-411, given complete Z-APP-41 scope (DH-00/02). Next discriminator: source publication history and signed approvals. (b) **Registrar compromise not established**; only a new session exists, needing verified session-origin/actions and trust data (DH-03). (c) **REG-S59 as zone editor not established**; it is not linked to DNS-PUBLISHER. (d) **Donation theft unproved**: no processor logs or recipient/transaction evidence are available. (e) AUTH-B serving GOOD/SER-410 **observed** at 09:18, not proof the whole Internet remained correct. The owner is Halden for administrative response, Selene for authoritative comparison, Octavia for registrar history and Clemens for processor findings.

### Worked answer — EX-TTX10-02

Prefer **B**: Halden's verified registrant approval REG-FREEZE-A30, Octavia's provider acknowledgment limited to the specified registrar workflow, Nerissa's read-only registrar/zone archive with later byte readback, and Selene's independently reviewed single-RRset restoration authorized by a distinct second reviewer. At DH-04 **freeze ACK exists** but authoritative restore has **not yet been released**; at DH-05 **DNS-APPLY-43 and AUTH-READ-45** justify specific authoritative recovery. Do not order blanket NS/registrar transfer absent delegation evidence; do not claim site safe from a single source.

### Worked answer — EX-TTX10-03

REC-R2 at 09:45 reports remaining TTL **1,000 seconds = 16 minutes 40 seconds**. After 11 minutes (660 s), the expected remainder **340 seconds = 5 minutes 40 seconds** at 09:56. Conditional expiration, assuming no cache refresh/policy change, is about **10:01:40 UTC**. A current authoritative GOOD does not clear REC-R2's stale answer, and decreasing TTL does not prove which browser or donor used that resolver. A shorter newly assigned TTL cannot retroactively age a previously cached RRset. Source-bound comparisons: at DH-02 authoritative GOOD **1/2**, sample recursive GOOD **1/2**; at DH-05 authoritative GOOD **2/2**; at DH-09 recursive GOOD **3/3** among named samples, never a global census.

### Worked answer — EX-TTX10-04

A **page observation** at DH-01 is only page visibility. DH-07's **35 checkout-button events** are interface actions on the trusted origin, not complete/declined/stolen payments. **PAY-SCOPE-04** explicitly leaves historical reconciliation **pending**; no proper transaction denominator is supplied. At DH-09 a **single fictitious sandbox test** can prove that a test-only journey reached the authorized merchant and produced a verified ADS acknowledgment, without charging anyone. Source needed for historic claims: ADS merchant/capture/settlement/refund/dispute records for the exact window, payment-bound website transaction identifiers and authorized investigation of any other merchant/recipient path. No fraud, phishing or privacy breach claim can be made from the fixed evidence.

### Worked answer — EX-TTX10-05

Before DH-09, freeze **limited authoritative + registrar remediation**: G1 owner known, G2 source archive partial/readback evidence now available, G3 registrar freeze bounded, G4 AUTH-A/B GOOD, G5 registrar access rotated, G6 REC-R2 cache remained UNKNOWN at DH-06 and broader recursive state **pending**, G7 website identity **not independently accepted**, G8 processor flow **not tested**, G9 historical impact **pending**, G10 monitoring/communication **proposed**. After DH-09, a **new** bounded acceptance may mark G6 **passed for 3 named recursors only**, G7 a specified browser/HTTPS fixture pass, G8 a verified authorized sandbox receipt, and G10 owner-signed monitored return if recorded. G9 remains pending; unsampled REC-R4 and past browser caches cannot be written off. This is operational return of named routes, **not** historic monetary or legal closure.

**Scoring calibration:** A participant writes at DH-05 “both authoritative servers are fixed, so all donors have safe payment access.” C9 should score **0** for that contradictory universal conclusion, even if two authoritative receipts were correctly named; DNS caches and processor checks remain unsupplied. A separate DH-09 statement may score well when it uses source-specific evidence and preserves prior uncertainty. A different learner writes “REG-S59 session is new and therefore the administrator committed fraud.” C3 should score **0** because actor/intent attribution contradicts available provenance.

## 11. Communication, debrief and measurable follow-ups

**Draft only, not approved or sent** — to be reviewed by Halden, Selene, Fernanda, Clemens, Lakshmi and Mireya:

> “We are reviewing an inconsistency affecting how some networks reach our donation website. The organization and its domain provider are restoring the approved domain configuration and checking access and cache behavior across multiple sources. Some donation pages may be intermittently unavailable or appear different while the review continues. We are using verified support channels and will publish a further update after checking our website identity and the approved payment-provider flow. We have not established any diversion of donations or compromise of the payment provider.”

The draft must not direct donors to an unfamiliar endpoint or solicit payment data by email. Mireya logs `drafted / technical reviewed / data-payment reviewed / owner-approved / issued / acknowledged` separately. A real external notice would depend on verified findings, actual applicable law/contracts, recipient scope and the approved continuity channel; no universal reporting deadline is claimed.

**25-minute debrief questions:** Which source showed an unauthorized-by-register RRset? Why did two authoritative servers disagree? What did REG-S59 prove and not prove? Could a transfer lock stop zone edits? Which records needed preservation before session rotation and rollback? Why can REC-R2 stay UNKNOWN after SER-412 appears authoritative? What does 1,000−660 mean, and what does it **not** mean for all browsers? Did anyone miscount web hits or button events as donations? Which payment-provider receipt, if any, supports a completed **test**? How would the team avoid duplicate charges or untrusted support channels? Which unsampled caches and history remain open at final acceptance? Could a different shift reproduce every change from the frozen artifacts?

| Improvement item | Fictional owner / target interval from exercise | Reproducible defensive retest |
|---|---|---|
| **I-01 registrar MFA and recovery identity** | Halden + Octavia / 14 days | Isolated registrar-account control review verifies per-person MFA, old session revocation, secured recovery contact and monitored change alerts |
| **I-02 dual review for DNS edits** | Selene + Halden / 21 days | Synthetic zone diff with unknown RRset is rejected absent two distinct signatures, controlled apply/readback and rollback |
| **I-03 external authoritative drift detection** | Selene + Mikhail / 21 days | Approved outside-in fixture compares AUTH-A/B and signed zone log, alerts on mismatched serial/target with source/timestamp |
| **I-04 cache-aware donor experience** | Sable + Fernanda / 30 days | Timed authorized multi-resolver/browser fixture demonstrates 1 stale cache while both authoritative servers are GOOD; test never claims global propagation |
| **I-05 processor evidence and donation continuity** | Clemens + Yvette / 28 days | Synthetic page event, processor sandbox completion, pending settlement and unrelated merchant conditions yield four distinct states with no false theft count |
| **I-06 registrar/provider incident source readiness** | Nerissa + Octavia / 21 days | Read-only original zone/session export, authorized copy/readback, missing source gap and independent signer/source provenance test |
| **I-07 truthful donor communication** | Mireya + Lakshmi + Gideon / 14 days | Review misleading “donations stolen” and “all clear” drafts; issue only a scenario-limited, owner-reviewed update with safe contact path |

All intervals are **fictional educational targets**, not NIST/ICANN deadlines or actions actually completed. The tabletop can be scored when A1–A6, EX-TTX10-01 through EX-TTX10-05 and independent observer findings are submitted. The fictional **current authoritative zone and sampled donation route** may be restored at DH-09 while causal attribution, unsampled recursive/browser caches and earlier donation-impact reconciliation remain **unresolved**. No real breach, criminal activity, lost donation, formal accreditation or compliance guarantee is asserted.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management (final April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — incident-response risk governance and the CSF 2.0 Community Profile.
2. [NIST CSWP 29 — Cybersecurity Framework 2.0 (final February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — nonprescriptive six Functions.
3. [NIST SP 800-81 Rev. 3 — Secure Domain Name System (DNS) Deployment Guide (final March 2026)](https://csrc.nist.gov/pubs/sp/800/81/r3/final) — authoritative/recursive DNS integrity and security roles, not a prescribed incident-specific cache purge.
4. [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/info/rfc1034/) — authoritative data, recursive lookup and cached TTL semantics.
5. [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/info/rfc1035/) — DNS records/message formats and protocol role background.
6. [RFC 2308 — Negative Caching of DNS Queries](https://www.rfc-editor.org/info/rfc2308/) — TTL handling for negative responses; **none is asserted** in the supplied case.
7. [ICANN — How to Protect Your Domain Name Against Domain Hijacking or Unauthorized Transfers](https://www.icann.org/en/blogs/details/do-you-have-a-domain-name-heres-what-you-need-to-know-26-3-2018-en) — registrar account protections, multistep authentication and limits of registrar locks.
8. [ICANN — About Locked Domain](https://www.icann.org/resources/pages/locked-2013-05-03-en) — registrar/transfer lock terminology and transfer scope; not proof that all DNS record changes are frozen.
9. [ICANN SSAC — Measures to Protect Domain Registration Services Against Exploitation or Misuse, SAC040](https://www.icann.org/en/ssac/publications/documents/sac040-executive-summary-for-measures-to-protect-domain-registration-services-against-exploitation-or-misuse-19-08-2009-en) — historical primary advisory on account/registration protection, not this fictional case's actual facts.

All parties, domains, access sessions, record labels, log cards, cache results, processor events, questions and worked answers are **original fictional educational material**. External sources are credited and paraphrased, **not reproduced, endorsed or relicensed**. Original OpenCyber Academy writing falls under [RIGHTS.md](../../../RIGHTS.md) and the maintainer's CC0 dedication scope and third-party exceptions. This publication includes no offensive hijack steps, live domain administration, payment details or confidential donor data. It is **not** evidence of actual diversion, phishing, data loss, law violation or a real-world resilience certification.
