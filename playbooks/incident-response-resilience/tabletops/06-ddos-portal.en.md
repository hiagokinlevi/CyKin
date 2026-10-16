# TableTop 06 — Public portal disruption: restore successful submissions without punishing legitimate users

**Edition:** English · **Exercise ID:** TTX-DDOS-06 · **Catalog scenario ID:** `ddos-portal` · **Editorial date:** 2026-10-15  
**Status:** Original, fully fictional defensive classroom exercise; independent technical, accessibility and human editorial review pending.  
**Audience:** Public-service command, application/SRE, edge operations, SOC, accessibility and user support, continuity, privacy/legal, communications and independent evaluation.  
**Timing:** 15-minute briefing, 90-minute paper-and-evidence tabletop, 25-minute after-action review. Allow extra time for accessible participation.  
**Reading path:** This expands the sixth [existing catalog scenario](../../../web/tabletop/scenarios.json), rather than adding a new catalog entry. Return to the [incident-response playbook index](../README.md) afterward. See [primary sources and rights](#12-primary-sources-and-rights).

## 1. Fictional context, five questions and safe learning boundaries

**The entire case is fictional.** Organizations, participants, times, service names, user panels, edge counters, rates, measures, operational receipts, thresholds, access issues and outcomes are invented classroom evidence. No person, authority, government service, IP, autonomous-system number, individual session, real request, personal submission or actual DDoS victim appears in this file. Participants do **not** generate traffic, configure firewalls, perform load tests, run commands, query real access logs, submit actual applications or deploy any rule. All operational observations in the case are **pre-written fictional injects**. A real organization's operators must have separately approved procedures, privacy protections and service-owner permission before performing any implementation or test.

Fictional **Westmere Civic Access Office (WCAO)** offers an online permit-renewal portal **CivicBridge**. Residents view eligibility guidance at fictional route **/guide** and submit applications through conceptual route **/submit**. The route labels are illustrative, not functional URLs or attack endpoints. A campaign deadline drives a legitimate peak in demand. At the same time, edge telemetry shows requests originating from many network providers, while the application error rate grows primarily at submission. Some legitimate residents cannot complete a form. There is no supplied proof that a malicious actor coordinated traffic, that the origin failed only because of load, or that widespread provider- or country-based blocking would restore user service.

**The five distinctions at every freeze:**

1. **Traffic volume/distribution** is an observation, not proof of DDoS intent or a particular layer of attack.
2. **Application degradation** is measured by endpoint, source and denominator. A 5xx origin failure differs from an edge 429 mitigation response; do not combine them into one undifferentiated error rate.
3. **Submission attempt** is not a successful completed user transaction. Repeated requests/retries are not unique people, and a queue acknowledgment is not a completed application receipt.
4. **Rate-control effect** requires independent rule match/action receipts, legitimate-user completion tests and fairness review; applying a rule is not proof of a benefit.
5. **Recovery** needs sustained service and accessible end-to-end submission, not a quiet edge chart alone; cause may remain unknown when service is restored.

### Observable exercise objectives

- **O1 — Authority and readiness:** identify service, edge, security, continuity, accessibility, privacy and communications decision rights, competing business risks and the required reviews before mitigation.
- **O2 — Reproducible triage:** compare source- and window-labeled edge counts, application 5xx, queue/worker telemetry, protected endpoint health and representative user completion without declaring DDoS by intuition.
- **O3 — Proportionate containment:** assess **submission-endpoint-only** rate controls with count/preview first where feasible, documented owner approval, action/expiry, false-positive tests and independent readback; reject blanket country/provider blocking on the supplied evidence.
- **O4 — Competing mechanisms:** distinguish legitimate deadline demand, abusive traffic, backend/queue capacity failure, dependency misconfiguration and mixed/unknown causes by tests and disconfirming evidence.
- **O5 — Recovery:** when justified, increase **submission-service** capacity under SRE/change authority, tune or remove temporary rate controls after sustained recovery, and independently verify real permitted user journeys.
- **O6 — Learning and rights:** capture an honest operational message, essential alternate submission path, lawful minimal telemetry and an improvement backlog that measures legitimate-user cost of mitigation.

### NIST SP 800-61 Rev. 3 / CSF 2.0, not a prescribed DDoS playbook

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates cyber incident response with [NIST Cybersecurity Framework 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final). This is **not** the older SP 800-61 Rev. 2 four-step model. In this exercise, **Govern/Identify/Protect** address authority, capacity baselines, continuity and rules; **Detect** is service/edge observation; **Respond** is coordinated analysis, bounded mitigation and communications; **Recover** is owner-accepted functional return; **Identify/Improvement** records lessons. These card labels, timings, score thresholds and clinical-style "hard gates" are **original educational choices**, never an asserted NIST requirement.

| Function emphasis | Fictional decision | Limit of evidence |
|---|---|---|
| Govern / Identify / Protect | Understand demand peak, owners, approved change process, dependency and accessible fallback | Planned capacity and authority are not evidence a mitigation works |
| Detect | Compare route-specific 5xx, edge traffic diversity, queues and user outcomes | Distributed traffic alone is not a proven attack |
| Respond | Protect /submit narrowly, preserve sources, verify effect, avoid harmful broad blocks | Rules can block legitimate clients and cause retries |
| Recover | Test scaled submission workers where indicated, staged retirement of temporary rules and complete journeys | Lower origin 5xx without user completion can be false recovery |
| Identify / Improvement | Evaluate fairness, surge response and measured restoration across users | A tabletop score is not deployed-site assurance |

Primary vendor documentation here provides **technology examples**, not an assertion that CivicBridge actually uses AWS or that NIST mandates a particular WAF: [AWS WAF rate-rule scope-down settings](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-high-level-settings.html), [AWS WAF rate-limit caveats](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-caveats.html), and [AWS Shield Advanced application-layer detection logic](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-detection-application.html). The last illustrates why a changing **volume and composition** against an appropriate baseline can be more informative than raw distributed volume, while still not proving the source or purpose of any request.

## 2. Named people, teams and separate authority

All names and authorities are fictional classroom assignments. No participant has permission to touch an actual portal; real service operators would use local charters. If one person plays more than one role in a small class, the approval and independent-observer functions must still be recorded distinctly.

| Name and team | Responsible decisions | Cannot authorize or infer |
|---|---|---|
| **Ambrose Vale — Civic Incident Commander** | Open and coordinate a service/security case, prioritize response and convene decisions; accept emergency escalation under a documented charter | Unilateral cross-country blocking, bypass user-accessibility no-go, or declare DDoS attribution |
| **Dr. Linnea Frost — Public Portal Service Owner** | Define critical completion criteria, approve user/service-impacting mitigation and final business acceptance; ensure an alternate service path | Execute an unreviewed WAF rule or declare everyone served by an edge health graph |
| **Kiran Basu — Application SRE Lead** | Diagnose /submit workers, queue and dependency, approve scoped application scaling/change plan with rollback and independent service checks | Decide suspicious-traffic actor, security attribution or broad geographical blocks |
| **Roxanne Imani — Edge Network / WAF Lead** | Propose and, **after separate approval**, simulate bounded path-specific rate limits; report rule versions, match/429 counts, expiry and independent rollback | Treat match count as malicious-request count or bypass false-positive checks |
| **Professor Julien Parkes — SOC and Security Analysis** | Distinguish known events from traffic hypotheses, compare source/behavior, ask for minimal logs and advocate proportional security controls | Count a distributed source map as attack proof or approve a blanket provider ban without analysis |
| **Sima Norwood — Accessibility and Resident Experience** | Define and witness representative legitimate test journeys, identify shared-network/assistive-technology exclusion and flag disproportionate mitigation cost | Declare a backend fixed because an edge rule blocked many requests |
| **Felix Mora — Service Continuity and Help Desk** | Set alternate assisted intake/receipts, track queue/backlog and prevent duplicate resident filings | Change core rate rules or invent completion of a user submission |
| **Tenzin Rowe — Data Protection / Legal Counsel** | Restrict IP/session retention and processing to purpose, assess any jurisdiction-specific duties and review notices | Derive person identity/intent from network metadata or assign universal legal obligations |
| **Beatrice Ekwueme — Communications** | Draft truthful staff/resident notices, track review, approval, dispatch and acknowledgment as separate states | Promise a fixed recovery time or say “under DDoS attack” without an evidence-based classification |
| **Nolan Kirsch — Executive Continuity Sponsor** | Allocate incident resources, authorize exceptional continuity staffing and accept quantified enterprise residual risk in charter | Substitute for service-owner acceptance, SRE verification, accessibility review or change control |
| **Greta Sutherland — Independent Facilitator and Observer** | Release numbered synthetic cards, freeze decisions at exact exercise minutes, score only retained artifacts and record disagreements | Invent logs, supply future evidence early or operate real cloud/security tools |

**Four approval tracks remain independent:** security recommendation, edge/application change approval and owner cost acceptance, operator reported execution, and independent user/SRE verification. An order to mitigate, a deployed rule, a traffic drop and a successful resident submission are different kinds of evidence.

## 3. Facilitator packet, clocks, denominator contract and stops

Provide printed **PD-00 through PD-10** in sealed release envelopes; distribute **PD-00 only** at briefing. Give learners an empty traffic worksheet, evidence-release ledger, decision-authority log, rule/rollback form, user-cohort comparison, queue health record, continuity plan, communications draft and observer rubric.

**Three-clock rule:** each case card's UTC source observation, the **exercise minute** at which the facilitator releases it and the **exercise minute** the team freezes a decision are distinct. A late observation describing an earlier period **cannot** justify an earlier decision. Freeze one named artifact before the next card and preserve earlier reasoning after revision. Endpoint counters require their own window, point of observation, class, unit and denominator.

**Measurement conventions for this case:**

- Edge **all-path requests** are requests seen at the fictional border, including cache hits, non-submission routes and repeats. They are **not** unique residents or necessarily delivered origin requests.
- Origin **/submit HTTP 5xx** is the number of backend 5xx among requests that actually **reach the submission origin** during a fixed ten-minute window; its denominator **excludes edge-denied 429**. 429 counts are stated separately.
- **/guide 5xx** uses its own origin denominator and cannot be mixed with /submit without weighting.
- **Completion panel** means a separately reported, consenting, synthetic *scenario* cohort of fixed eligible user attempts, with standard and assistive/shared-network subcohorts. A completion is a **validated end-to-end submission receipt**, not a successful HTTP status from a preflight or queue acceptance. Requests can retry, so the panel's 200 attempts are **not** the same population as thousands of edge requests.
- **False-positive impact** is a measured legitimate journey blocked or impaired by a rule (if a verified test and reason establish it), not a raw request count or all 429 responses.
- **Per-provider/country metrics** are coarse aggregate traffic classes without human identity or real customer records. A large contributor count is not an instruction to block a geography.

**Record schema:** `decision ID | case UTC window | exercise minute / cards released | observation + source/denominator | alternatives and falsifier | service/accessibility impact | proposed scope and expiry | authority and change version | proposed/approved/simulated executed/independently observed | rollback / next check`.

**Stop card:** Do not generate an actual request flood, change live edge/network rules, inspect real users' IPs, block a whole country/provider without independently justified impact and authority, run live submission tests without service/user authorization, or claim user data or a real government incident. The only "real authorized" submission test in this document is a **fictional incident-record scenario receipt**, never an instruction to conduct one. In real organizations those tests require approved test identities, informed participants, safeguarding against duplicate or legal-effect submissions, and owner sign-off.

## 4. Progressive inject ledger and case facts

The **exercise clock** is 90 minutes; every case UTC event is entirely fictional. Decisions must be frozen **before** the next card arrives.

| Exercise minute | Revealed card | Fictional event/window UTC | Required frozen decision |
|---:|---|---|---|
| 0–7 | **PD-00** | 08:50–09:00 | Baseline denominators, owners, service/fallback |
| 8–19 | **PD-01** | 09:00–09:10 | Is this proven DDoS or service disruption with competing hypotheses? |
| 20–30 | **PD-02** | 09:12–09:18 | Queue/worker/dependency discrimination |
| 31–40 | **PD-03** | 09:19–09:22 | Count-only endpoint rule and safeguard design |
| 41–51 | **PD-04** | 09:30–09:40 | Scoped temporary control, false positives, explicit review |
| 52–60 | **PD-05** | 09:41–09:45 | Evaluate whether to widen, narrow or pause rule |
| 61–70 | **PD-06** | 09:46–09:50 | Conditioned submission-capacity scale and negative tests |
| 71–80 | **PD-07** | 09:50–10:00 | Distinct origin 5xx, edge 429 and cohort completion |
| 81–87 | **PD-08** | 10:00–10:10 | Stability and rule retirement decision |
| 88–90 | **PD-09** | 10:10–10:20 | Authorized end-to-end verification receipt and owner acceptance |
| Only after all freezes | **PD-10 optional** | 10:30 | New future observation cannot revise an earlier decision |

### Prebrief — PD-00: baseline before the peak (minute 0)

**Fictional baseline 08:50–09:00 UTC, ten complete minutes:** Edge sees **40,000 all-path requests**, from a geographically mixed set of networks with no supplied behavioral attribution. At the **/guide** origin, **12,000 requests, 120 HTTP 5xx**; at **/submit**, **4,000 requests, 80 HTTP 5xx**. No WAF rate rule is active; the queue has no known threshold breach and the submission worker pool is at ordinary capacity. A separately surveyed, simulated service panel had **200 eligible attempts**, of which **184** obtained an end-to-end validated submission receipt: **148 of 160 standard-path** and **36 of 40 assistive/shared-network** attempts. The panel is not proof of an actual production test by the learner.

**Decision:** Linnea defines one portal-wide safety principle: residents must be able to submit a completed transaction or use a staffed contingency, regardless of network origin or accessibility method. Sima defines representative user cohorts and fairness checks; Kiran names /submit application/dependency and queue monitoring; Roxanne specifies what WAF measurements can and cannot show; Julien requests source provenance. An approved internal fallback exists but has not been recently rehearsed. **No incident is yet classified as DDoS.**

**Worked baseline:** /guide 5xx = 120/12,000 = **1%**; /submit 5xx = 80/4,000 = **2%**; panel completion = 184/200 = **92%**, with subgroup rates **92.5% standard** (148/160) and **90% assistive/shared** (36/40). An HTTP response is not the same as receipt completion. These denominators are independent.

### Round 1 — PD-01: distributed surge, localized submissions failure (minutes 8–19; Detect)

**Fictional 09:00–09:10 UTC observations:** Edge totals **72,000 all-path requests**, with requests seen from **many network providers** and regions. /guide origin logs **24,000 requests, 240 HTTP 5xx**; /submit origin logs **12,000 requests, 3,600 HTTP 5xx**. The fixed 200-attempt user panel reports **94 completed**: **82/160 standard-path** and **12/40 assistive/shared-network**. No edge mitigation rule exists yet; there are no edge 429s attributed to a rate rule. Edge, origin and panel data describe different populations. A public-service deadline could plausibly increase legitimate traffic; an abusive or coordinated flood is also possible. The card does not provide an attacker, malicious traffic classification, source intent, exact queue mechanism or verified application cause.

**Decision:** Ambrose opens **WCAO-IR-006** as **public portal degradation during a surge**, with DDoS **suspected but not demonstrated**. Kiran requests endpoint/dependency/queue metrics; Roxanne requests rate distribution, protocol and actual path-specific rule eligibility, not just network-source spread; Julien asks how traffic composition differs from baseline. Sima reports that assistive users' completion fell disproportionately; Felix activates an accountable assisted submission fallback. **Do not approve blocking all traffic from countries/providers because many networks appear.**

**Calculations:** edge request change = (72,000−40,000)/40,000 = **+80%**. /guide 5xx = 240/24,000 = **1%**, unchanged. /submit 5xx = 3,600/12,000 = **30%** (up 28 percentage points from baseline). Panel completion = 94/200 = **47%**; standard = 82/160 = **51.25%**, assistive/shared = 12/40 = **30%**. The 21.25 percentage-point group gap is descriptive for this panel, not a causal finding or statistical estimate for the public.

### Round 2 — PD-02: backend evidence and cause discrimination (minutes 20–30)

**Fictional 09:12–09:18 bounded SRE observations:** submission-worker utilization is **93%**, with **580 queued tasks** versus an **owner-defined caution threshold of 300**; the queue grows over successive samples. Database query p95 remains **120 ms** in the supplied sample, close to its baseline **115 ms**, while the submission application logs indicate a high retry count during the error interval. Other dependencies, client-side failures and missing trace spans are **not fully covered**. A separate operator reports that /guide reads continued, but the application error view shows errors concentrated in **/submit**.

**Competing hypotheses:**

- **H1 legitimate capacity pressure:** real deadline demand and ordinary retries exceeded current submit-worker throughput;
- **H2 submission-backend defect:** a code path, resource leak, queue bottleneck or config regression raised errors;
- **H3 abusive request pressure:** some unapproved automated requests targeted /submit and contributed to load;
- **H4 mixed cause:** legitimate demand, retry amplification, backend limits and possibly abuse overlap.

**Discriminators:** sample request composition by **route**, session eligibility without storing personal content, completion by intended user paths, server traces and queue behavior under controlled capacity, edge request/response classes, and any authoritative approved release changes. Large request counts from many networks alone discriminate none of H1–H4. A normal sampled database p95 does **not** exclude other dependencies or a backend implementation fault.

**Decision:** Kiran proposes measuring submit-worker bottleneck and a safe staged scale **if** app owner agrees. Roxanne suggests a **Count/preview-only, route-specific** rule to estimate mitigation cost before action, and Sima requires false-positive cohort instrumentation. Julien maintains a security hypothesis and data retention proportionality. Ambrose sets a new 10-minute checkpoint rather than attributing an attacker without evidence.

### Round 3 — PD-03: count-only path scope and approval plan (minutes 31–40; Respond)

**Fictional 09:19–09:22 rule design sheet, no enforcement yet:** Roxanne proposes temporary control **RL-SUB-v1** scoped to the **/submit** path (and appropriate method/context after route owner validation) rather than **/guide** or all requests. It starts in a **count/preview state** using a defined rolling window and **conservative aggregation**, not a globally shared hard limit across all users. A design review warns that shared NATs, institutional networks, assistive technology, retries and browser challenges may distort simple IP-based fairness. Draft expiry: **20 minutes unless renewed after independent checks**; reversible removal and owner reviewed rollback are required. There is **no numerical production threshold** specified in the card; a classroom sample is insufficient to pick one without real baselines.

**Decision rights:** Linnea authorizes user/service impact, Roxanne authorizes edge rule implementation within operations delegation, Julien validates security rationale, Sima signs user-cohort test criteria, Kiran validates backend/route semantics, and Greta is the neutral reviewer. **Count mode is not containment:** it collects would-match observations and may inform a future limited action; it does **not** reduce load by itself. If a narrower control could accidentally remove an accessible path, redesign before enforcement.

**Prohibited shortcuts:** Whole-country/provid­er blocks on a source graph; challenges that only mouse or image-CAPTCHA users can pass; one IP address equated with one user; an apparently idle /guide endpoint treated as proof submission works. Document false-positive checks and accessible appeal/fallback before considering wider rules.

### Round 4 — PD-04: scoped control deployed, but its cost is visible (minutes 41–51)

**Fictional 09:30–09:40 after a separately signed scenario change `CHG-RL-1`:** Linnea approved a bounded **/submit-only** temporary rule; Roxanne's control-plane receipt **EDGE-APPLY-31** reports application at 09:30, and an independent readback **EDGE-READ-32** confirms the scope and version. Edge telemetry reports **300 rate-rule HTTP 429 responses** in this ten-minute interval, but the record does **not** classify all of them as malicious or unique users. The **/submit origin**, excluding edge-denied traffic, reports **10,000 requests, 1,200 HTTP 5xx**. A fresh representative panel of **200 authorized synthetic scenario attempts** records **162 end-to-end receipts**: **140/160 standard** and **22/40 assistive/shared-network**. The panel includes cases in which a genuine eligible workflow was blocked or challenged by the rule; the count of **individual confirmed false-positive users** is **not supplied**, so do not equate it with all 300 429 events.

**Decision:** Observe benefit *and* harm. Origin 5xx = 1,200/10,000 = **12%**, better than 30% but not restored; panel completion = 162/200 = **81%** overall, standard **87.5%**, assistive/shared **55%**, a **32.5 percentage-point** disparity. Although overall access improved from peak, accessible/shared network experience is still materially worse than baseline. Sima blocks any suggestion to **widen enforcement** before tuning and accessible route validation. Linnea may approve narrowing, bypassing known permitted accessibility needs within sound risk constraints, or temporarily backing off the rule. Kiran must still address worker/queue bottleneck; Roxanne cannot claim that 300 429s are 300 attackers.

**Conditional branch:** If the rule cannot be modified to protect legitimate submissions with an accessible tested path, the owner may remove it and pursue application scaling with monitoring/contingency. A scoped rule cannot pass on its error-rate metric while legitimate people lose functional access.

### Round 5 — PD-05: conflicting success metrics and the no-widen decision (minutes 52–60)

**Fictional 09:41–09:45 review:** A dashboard highlights the drop from **30%** to **12%** /submit-origin 5xx. A separate support desk receives a rise in complaints from residents behind a library/shared connection or using assistive software. The complaints do not identify one country, ISP, attack actor, or unique WAF rule cause for each user. The mitigation logs and approved service-test cohort show enough **positive user-journey failure** to require an accessibility review but not a precise population-wide false-positive rate. A proposed broad policy would block **two entire providers and one country** purely for having high request volumes.

**Decision:** Ambrose, Linnea and Sima **reject that broad policy** on the evidence supplied; there is no analysis of legitimate-user harm, targeted abusive behavior, rollback or service-owner acceptance. Roxanne proposes **RL-SUB-v2**, restricted to the same endpoint but with safer discrimination and monitored exceptions; Kiran proposes scaling submission workers separately; Julien records that the traffic's maliciousness is still unproven. Tenzin limits retention of potentially identifiable network data to approved purpose/window; Beatrice drafts a non-attributive service notice. The controlled continuation must preserve retry/queue behavior and avoid a rule so narrow that it fails to protect the service.

**Decision contrast:** “5xx improved, therefore expand the block” is incorrect because origin denominators exclude edge 429 and the user-panel disparity grew. “More users completed, therefore no issue” is also incorrect: a single metric masks impact on a protected accessibility path. Keep the signed 09:30 decision immutable and add a new, separate review record.

### Round 6 — PD-06: conditionally scale the submission service and tune rate control (minutes 61–70)

**Fictional 09:46–09:50 owner-approved change planning:** Kiran's read-only capacity projection and rollout record show **submit-worker queue pressure** and a tested **separate worker-pool scale-out proposal**, with code/config version preserved, health probes, documented rollback trigger and no change to /guide. Application change **APP-CAP-v2** needs Kiran's technical authorization and Linnea's service-impact approval; edge change **RL-SUB-v2** requires Roxanne's separate execution and Sima's negative-path review. The exercise does **not** claim real cloud autoscaling or WAF reconfiguration by the learners.

**A proposed acceptable plan:** (a) reserve minimal telemetry; (b) apply scoped, time-limited rate protection with false-positive monitoring; (c) add capacity **where the submit bottleneck is actually observed**; (d) test representative genuine submissions and check queue drain and downstream data correctness; (e) freeze/revert any rule if legitimate users lose disproportionate access; (f) retire temporary controls after sustained stable windows and a service-owner go. Scaling alone may not help if the true bottleneck is an external dependency, database locking or logical defect, so preserve a negative test of that assumption.

**What is not supplied yet:** validated actual effect of this new plan. A signed change request is **not** an operator receipt; a resource-scale assertion is **not** a tested completed submission; a traffic drop is **not** an explanation of cause.

### Round 7 — PD-07: improved metrics under the revised bounded treatment (minutes 71–80)

**Fictional 09:50–10:00 source packets:** A distinct operator receipt **APP-APPLY-50** states the submit-worker pool change was applied to the named version after Linnea/Kiran authorization, with a **separate independent readback** of worker count and queue trend. Edge receipts **EDGE-APPLY-51 / EDGE-READ-52** show **RL-SUB-v2** scoped to /submit with a 20-minute review expiry and an explicit rollback owner. The monitored ten-minute interval shows **10,000 /submit origin requests, 250 5xx**, and **100 edge 429** attributed to the scoped temporary rule. A new 200-attempt panel records **185 validated receipts**, including **149/160 standard-path** and **36/40 assistive/shared-network** attempts. /guide is independently checked to have **24,000 origin requests, 240 5xx**, showing its separate **1%** rate remained stable. All counts are synthetic and sampled; the 429 events are not assumed malicious, and causality between scale/rule and better outcomes cannot be proven from this one combined treatment.

**Compute before concluding:** /submit 5xx = 250/10,000 = **2.5%**; /guide 5xx = 240/24,000 = **1%**; panel completion = 185/200 = **92.5%**; standard = 149/160 = **93.125%**; assistive/shared = 36/40 = **90%**. The subgroup difference is now **3.125 percentage points** (93.125−90), compared with **32.5 points** under v1, but these are panels, not a population estimate. The edge rate rule still produced 100 429 responses, requiring attribution/false-positive monitoring: a clean panel result does not prove all 429s justified.

**Decision:** Service is **candidate for recovery**, not yet accepted. Verify queue trend, complete resident transaction semantics, stable windows, representative users, service fallbacks and independent checks before removing controls. Possible H1/H2/H3/H4 mixtures remain undetermined. Sima records no disproportionate disparity in this **defined** sample against baseline, not a universal fairness certificate.

### Round 8 — PD-08: stability required before removing temporary controls (minutes 81–87)

**Fictional 10:00–10:10 evidence:** A second complete ten-minute window after the revised change reports /submit **10,000 origin requests, 270 5xx** (**2.7%**), with /guide **24,000 origin, 240 5xx** (**1%**). Submission queue falls from **580** in the earlier sample to **90 outstanding tasks**, below the exercise's **300 caution line**; comparison is descriptive, not a guarantee of zero stuck jobs. The user panel reports **184/200** completed, including **148/160 standard** and **36/40 assistive/shared** (92% overall; 92.5% vs 90%). Edge counted **95 temporary-rule 429**; no approved analysis labels their individual legitimacy. Backend health, queue and user metrics have been stable over **two monitored ten-minute windows**, but no further longer-term capacity guarantee or root-cause attribution is supplied.

**Decision:** Linnea, Sima, Kiran and Roxanne may propose a **staged retirement** of RL-SUB-v2 after verifying legitimate traffic completion under a count/observe successor, named rollback and canary monitoring. They may also extend the rule for a **short, approved interval** if residual traffic risk justifies it and accessibility continues to pass, but not silently let temporary blocking persist forever. Do not remove all protection instantly from fear of having a rule or celebrate a green origin chart without post-removal user evidence. Felix maintains an accessible assisted submission option for anyone not yet served.

### Round 9 — PD-09: authorized end-to-end production validation inside the fictional case (minutes 88–90)

**Fictional 10:10–10:20 separately sourced receipts, released only after PD-08 is frozen:** The WCAO service owner records **TEST-AUTH-10**, authorizing designated, consenting representative residents and a trained operator to exercise an **approved, non-legally-binding test submission route** within their actual **fictional** CivicBridge production operational procedure; test transactions are tagged, protected, reconciled and designed not to file an unintended real application. An independent support observer **USER-REC-11** records **one completed authorized standard submission and one completed assisted-access submission**, each with a distinct validated end-to-end receipt. These are **fictional reported observations**, not a live test performed for this publication. After an authorized staged withdrawal **RULE-RETIRE-12**, independent edge state confirms the temporary blocking action retired; a post-withdrawal monitored window reports **9,000 /submit origin requests, 225 5xx** (**2.5%**), no 429 **attributable to RL-SUB-v2**, and a new small protected audit panel reports **92/100** successful completed submissions with assistive accessibility **not separately measured in that smaller window**.

**Evidence bounds:** This allows a **narrow service-owner acceptance** that (a) the named authorized test submissions completed, (b) route-specific error rates improved dramatically from the surge, (c) this rule version was removed under approval, and (d) a limited post-retirement panel exists. However, the tiny final panel **does not independently prove population-wide proportional fairness**, and complete all-provider availability, upstream cause and future peak resilience remain unknown. Sima's approval should explicitly reference the earlier stratified PD-07/08 cohorts plus a continued monitoring commitment; if policy requires simultaneous post-withdrawal stratified evidence, retain **conditional acceptance** pending a new properly stratified sample. No actual live application, network rule change or real user was touched by this tabletop.

**Decision:** Linnea signs **limited restored submission service**, with documented exact tests, known remaining uncertainty, accessibility follow-up, accountable rollback and future peak monitoring. Julien leaves malicious-traffic classification **unconfirmed**; Kiran owns bottleneck investigation; Roxanne records rule retirement; Beatrice may publish a bounded operational update after service owner/privacy review. No claim that DDoS was proved merely by the high-source distribution.

### Optional PD-10: future negative-control follow-up (never retroactive)

A facilitator may add a new, explicitly optional card at fictional 10:30: for example a newly discovered backend defect or a new abusive pattern with independent request-classification evidence. Assign it a **new source and release minute**, and require a **new** response instead of revising PD-03 or PD-09. Do not count this unissued card as an observed incident fact.

## 5. Reproducible evidence calculations and false-positive testing

A student can complete all arithmetic **on paper** from the fixed table below. Denominators must be preserved: edge all-path requests are **not** /submit origin requests; edge 429s are **not** origin 5xx; a successful request is not necessarily one resident receipt. No terminal, script, site, cloud account or load generator is used.

| Case UTC window | Edge all-route requests | /guide origin 5xx / requests | /submit origin 5xx / requests | Edge 429 for temporary rule | 200-attempt panel completion | Standard 160 / assistive 40 completion |
|---|---:|---|---|---:|---:|---|
| Baseline 08:50–09:00 | 40,000 | 120 / 12,000 | 80 / 4,000 | 0 | 184 / 200 | 148 / 160; 36 / 40 |
| Surge 09:00–09:10 | 72,000 | 240 / 24,000 | 3,600 / 12,000 | 0 | 94 / 200 | 82 / 160; 12 / 40 |
| RL-SUB-v1 09:30–09:40 | Not supplied | Not supplied | 1,200 / 10,000 | 300 | 162 / 200 | 140 / 160; 22 / 40 |
| v2 + worker scale 09:50–10:00 | Not supplied | 240 / 24,000 | 250 / 10,000 | 100 | 185 / 200 | 149 / 160; 36 / 40 |
| Stable 10:00–10:10 | Not supplied | 240 / 24,000 | 270 / 10,000 | 95 | 184 / 200 | 148 / 160; 36 / 40 |
| After retirement 10:10–10:20 | Not supplied | Not supplied | 225 / 9,000 | 0 attributable to retired rule | **92 / 100 in separate smaller panel** | **not stratified** |

**Worked arithmetic with limits:**

- Baseline submit = 80 ÷ 4,000 × 100 = **2%**. Peak submit = 3,600 ÷ 12,000 × 100 = **30%**. Difference = **28 percentage points**, not “28% more.”
- Peak guide = 240 ÷ 24,000 × 100 = **1%**, equal to baseline guide. Error concentration strongly supports investigating the submission route and dependencies, without eliminating abuse hypotheses.
- Edge volume ratio 72,000 ÷ 40,000 = **1.8**, or an **80% increase**, but counts from many providers do not prove a coordinated DDoS.
- Rule v1 = 1,200 ÷ 10,000 × 100 = **12%** origin submit failures. Comparing it with 30% without separately checking edge 429 and genuine completion would misstate mitigation cost.
- Panel v1 = 162 ÷ 200 = **81%**. Standard = 140/160 = **87.5%**; assistive/shared = 22/40 = **55%**; difference **32.5 points**. An improved overall mean **conceals inequitable journey failure**.
- Rule v2 and scaled capacity = 250/10,000 = **2.5%** submit 5xx, while completion = 185/200 = **92.5%**. Standard = 149/160 = **93.125%**; assistive/shared = 36/40 = **90%**, gap **3.125 points**. It is not an exact estimate of population-wide disparity or causal effect of one change.
- Second stable window = 270/10,000 = **2.7%** submit 5xx; 184/200 = **92%** completion. Queue reduction 580 → 90 = **490 fewer outstanding tasks** at those two checkpoints, not proof of no hidden backlog.
- Post-retirement = 225/9,000 = **2.5%**, and 92/100 = **92%** in a **different, smaller cohort**; the missing post-retirement subgroup breakdown must stay **unknown**, not assumed to match prior panels.

**Mandatory negative controls:** NC-1 distribute requests over many networks but keep normal legitimate campaign behavior: still **not automatically DDoS**. NC-2 introduce a submission-worker fault while edge volume remains normal: application outage without attack. NC-3 show a rate rule's low origin 5xx **only** because edge blocks more real residents: false success. NC-4 replace diverse clients with one shared NAT: an IP-based threshold may penalize a public library. NC-5 accessible user cannot complete CAPTCHA/JS challenge while standard browser passes: not acceptable mitigation. NC-6 a status 2xx or queue acknowledgment without stored validated receipt is **not** application completion. NC-7 rule count-mode matches do not mean requests were blocked; NC-8 429 rate events are not distinct malicious persons. NC-9 static database p95 does not prove no app bug. NC-10 an improved ten-minute window alone does not prove full recovery.

**Independent exercise IP-06 (paper only):** Freeze a one-page assessment at PD-01: calculate the changes for edge requests, /guide and /submit origin 5xx, panel completion and group gap. At PD-04 calculate v1 performance and decide whether to broaden. At PD-07/08 calculate two windows and define a conditional removal gate. At PD-09 evaluate whether an authorized end-to-end transaction was observed **in the fictional supplied card** and what residual fairness evidence is missing. Do not use a later card's result to justify an earlier decision. The [facilitator worked results](#10-facilitator-worked-answers-and-score-calibration) provide all expected computations and interpretation.

## 6. Containment alternatives, competing causes and conditional consequences

Each branch below is **a plan unless an explicit later inject supplies an operator and independent-effect receipt**. The aim is end-user availability with the minimum necessary traffic restriction, not maximal request blocking.

| Alternative | Approvals and evidence needed | Conditional consequence / reason to reject |
|---|---|---|
| A. Count/preview an endpoint-only rate rule | Linnea owner; Roxanne edge; Julien security; Sima accessibility; Kiran backend scope | Estimates matches and risk; **no traffic control while Count only** |
| B. Temporarily enforce **/submit-only** bounded rate control | Same approvals, expiry, independent rule readback, representative user journeys and rollback | May relieve load but can block legitimate users; v1 required tuning before widening |
| C. Escalate submit worker capacity if diagnosed | Linnea service impact, Kiran SRE approval, authorized operator/readback, dependency and rollback checks | May help observed worker/queue bottleneck; may fail if bottleneck elsewhere |
| D. Block two entire ISPs/country from source-volume chart | Would require compelling request-level evidence, impact/rights analysis and exceptional approval **not supplied** | **Reject**: could exclude ordinary users and increase disparate access |
| E. Challenge every client on every path | User and accessibility review, browser/assistive test and fallback; no evidence supplied | **Reject** on present facts: higher abandonment and hard-to-pass challenges |
| F. Remove all temporary controls instantly at first good sample | Must satisfy sustained metrics and specific anti-abuse risk decision | Premature removal may allow recurrence; use staged, monitored expiry |
| G. Keep temporary rule forever after service recovers | Requires renewed authority and evidence of continuing risk, false-positive and access cost | Expired emergency restriction is not normal default policy |
| H. Offer assisted submission while testing changes | Felix/Noelle-like continuity authority in this scenario belongs **Felix Mora**, with Linnea and Sima | Preserves service but must log completed assisted receipts without duplicates |
| I. Declare “DDoS confirmed” from many networks | Requires corroborated abuse classification, not present | **Do not** assert origin/intent; incident is disruption under investigation |

**Mechanism discriminators:** If scaled submit workers correlate with queue drain but rate controls were also tuned simultaneously, recovery **cannot** be causally assigned to scaling alone. If low /guide 5xx persists while /submit fails, investigate submit-specific queue/write paths rather than unrelated read-only CDN traffic. Compare traffic composition, not only volume, against prior deadline baselines; distinguish burstiness, retries and shared-network users. Do not infer a malicious country or provider from unclassified network origins. A rate threshold needs real workload baselines, per-route/service capacity, cost of limiting genuine users, and monitored rollback. The example cards intentionally do **not** provide a numerical threshold for direct operational use.

## 7. Safe metrics, privacy and accessibility evidence contract

This is a conceptual checklist for **authorized service owners**, not an instruction to collect personal traffic or deploy live mitigations. The classroom operates only with invented aggregate evidence.

1. **Collect only the needed aggregate sources:** edge all-path and /submit route requests, origin 5xx, edge-specific 429, worker and queue health, user completion and accessibility segments; identify their timestamps, recording systems, retry behavior and covered routes. Avoid raw URLs with user data and personal identifiers.
2. **Preserve source and derived data separately:** retain original monitored aggregate cards, named collector/time, query bounds, acquisition/retention receipts and each calculation; record missing metrics as **not supplied**, not zero.
3. **Validate classification limitations:** multiple networks do not establish malicious intent; high volume can be caused by a deadline or retries; a backend defect can occur with ordinary traffic.
4. **Record exact action scope:** rule version, request path, aggregation key type, sampling period, action (Count vs block/challenge/429), owner, expiry, rollback and independent readback. Do not combine edge-denied and origin errors into one denominator without a documented mutually exclusive request universe.
5. **Test legitimate completion:** require complete authorized transaction receipt, stable record identity and correct downstream semantics; an HTTP success alone or a captured form does not suffice. Representative assisted/accessible and shared-network contexts matter.
6. **Test false positives and discrimination:** compare proportion of successful attempted journeys by cohort, look at verified rule-linked blocked legitimate attempts, verify challenges work for assistive technologies and provide fallback. Review privacy and accessibility equity without treating a 40-person panel as population statistics.
7. **Check backend independently:** investigate queue/worker, database and downstream dependencies; propose capacity increase only where bottleneck evidence supports it, with change risk and rollback.
8. **Reassess and retire:** require at least two configured comparable observation windows plus service owner/accessibility acceptance, defined residual attack risk, rule expiration and independent post-retirement monitoring. This **two-window threshold** is a **fictional exercise gate**, not a NIST or cloud vendor prescription.
9. **Review lawful telemetry:** Tenzin authorizes minimization, retention and access to potentially identifying network logs based on actual rules; do not copy real resident sessions, geolocate individuals from group traffic or publish source addresses.
10. **Handoff:** state service status, exact applied restrictions, pending signatures, current queue/user completion, unknown cause and next check. Report what is **still disabled** so another operator cannot accidentally strand users.

Official vendor examples: [AWS WAF scope-down statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-scope-down-statements.html) allow path/category scoping; [AWS WAF request-limiting behavior](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-request-limiting.html) separates Count from effective block/challenge; [AWS WAF caveats](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-caveats.html) explain approximate rates and propagation delays. These sources explain a mechanism; they are **not proof** that the fictional rule was deployed on AWS or that any numerical threshold in a tabletop should be applied in production.

## 8. Recovery and acceptance gates for legitimate public submissions

Successful service restoration is a **multi-owner, conjunctive** decision. A green edge chart cannot make up for a red transaction or an exclusion of legitimate residents. Every line has an exact time, source, owner, approval, observed outcome, risk limit and next review.

| Gate | Required independent evidence | Authority and NO-GO condition |
|---|---|---|
| **G1 known service state** | Signed baseline, route-specific origin/edge denominators and source time | Kiran + Julien: no origin/edge denominator mixing |
| **G2 proportional rate action** | Count/preview baseline, signed path-only rule/expiry and independent state, no arbitrary geo/provider block | Roxanne + Linnea: unsupported blanket restriction fails |
| **G3 user journey** | Consent/authorized scenario real-like test with **completed validated receipt** and safe test handling | Linnea + Felix: queue or HTTP success without receipt fails |
| **G4 access/disparity** | Sima-approved standard and assistive/shared cohorts, negative control, verified false-positive review and fallback | Sima: PD-04's 32.5-point gap is a **NO-WIDEN** condition |
| **G5 backend health** | Worker queue drains below caution threshold, submit origin 5xx decreases, dependency/rollback probes | Kiran: low WAF request counts alone are insufficient |
| **G6 stability** | Two consecutive comparable ten-minute windows with source and user outcomes; no unexplained regressions | Linnea + Kiran: one green burst cannot establish sustained service |
| **G7 temporary rule retirement** | Change authorization, staged remove/count-only transition, expiry and independent post-removal state | Roxanne + Sima: do not leave an emergency block in place indefinitely |
| **G8 business continuity** | Assisted submission option, duplicate-protection and reconciliation, visible instructions for affected users | Felix + Linnea: accessible users cannot be abandoned |
| **G9 communication/privacy** | Factual operational notice, audience, review/approval/delivery state and minimized logs | Tenzin + Beatrice: no invented attacker attribution or personal disclosure |
| **G10 unresolved cause/risk** | Explicit hypotheses and missing discriminators, monitoring/escalation triggers, accountable retest | Ambrose + Nolan: restored availability does not prove DDoS cause |

**At PD-04:** Service is **not recovered** despite improved origin errors because legitimate assistive/shared users remain impeded. Widening blocks fails G4.

**At PD-07/08:** Service becomes a **candidate**, with 2.5% then 2.7% submit 5xx, queue below the caution threshold, representative outcomes approaching baseline and group gap improved. Still pending retirement and post-change verifications.

**At PD-09:** The **fictional authorized user-test receipts** support a limited service-owner restoration decision, with lower route-specific errors and the temporary rule independently retired; the final smaller panel has **no new stratified fairness count**, which remains an explicit review obligation. If WCAO's actual acceptance policy required contemporaneous accessibility cohorts after removal, the correct gate is **conditional** until obtained. The exercise does **not** claim real production health or DDoS attribution.

**Important distinction:** A real, authorized test submission is meaningful only when an approved user/service owner can show a legitimate transaction end-to-end, with legally safe test handling. In this classroom, such a receipt is **fictional evidence given to learners**. No student or AI runs a real transaction.

## 9. Required learner artifacts, scored rubric and hard stops

Every team submits six **frozen** artifacts. Reviewers score source-backed decisions, not how confidently someone narrates after the next inject.

| Artifact | Required contents | Check another reviewer can perform |
|---|---|---|
| **A1 release/evidence ledger** | PD source UTC, release/freeze minutes, edge/origin/panel populations, hypotheses and unknowns | Detect use of late PD-07 or PD-09 in earlier decisions |
| **A2 calculations and route health** | PD-00/01/04/07/08/09 arithmetic, denominators, distinct 5xx vs 429, worker queue | Reproduce percentages and points without outside data |
| **A3 authority and mitigation envelope** | Linnea/Kiran/Roxanne/Julien/Sima approvals, rule path/version/expiry, execution/readback and rollback | Is Count mistaken for enforcement or approval for effect? |
| **A4 legitimate-user fairness** | Overall and subgroup completed receipts, complaints/false positives, accessible/shared tests, owner verdict | Does aggregate gain hide a 32.5-point cohort gap? |
| **A5 recovery and continuity** | APP-CAP-v2 scope, queue drain, G1–G10, assisted submissions and duplicate controls, rule retirement | Which receipt establishes end-to-end submission? |
| **A6 communications/after-action** | Draft/review/approved/sent distinctions, no attack attribution, named fixes/due dates/falsifiable retests | Is “DDoS” claimed on traffic geography alone? |

**Original classroom scoring:** Ten criteria × **0 = missing/contradicted**, **1 = related but incomplete evidence/time/authority/limit**, **2 = correct and reproducible bounded decision** = **0–20**. Two independent evaluators cite exact frozen artifact and PD source before settling disagreement. If a card is omitted by the facilitator, dependent scores become **not observed / facilitation defect**, not participant zero. These scoring thresholds are original educational design, **not** NIST certification.

| Criterion | Full two-point standard |
|---|---|
| **C1 differentiation** | Surge, DDoS hypothesis, backend fault, legitimate peak and mixed cause kept distinct |
| **C2 metrics** | Correct origin/edge/panel denominators and exact percentage-point changes |
| **C3 response authority** | Service owner, edge, SRE, SOC, user-accessibility and independent verification distinct |
| **C4 bounded scope** | Endpoint-only, time-limited rule; no unexplained country/provider block |
| **C5 false positives** | v1 subgroup gap and count of 429 events not equated with attacker users |
| **C6 backend investigation** | Queue/worker evidence, unresolved dependencies, scale benefit unclaimed before readback |
| **C7 decision chronology** | No future PD cards used at earlier freeze; approval/action/effect separate |
| **C8 controlled restoration** | Two windows, independent rule retirement, no claims beyond actual tests |
| **C9 inclusive completion** | Standard/assistive panel and representative **completed** receipts, fallback and residual fairness unknowns |
| **C10 debrief/communication** | Factual message, named owner, timed measurable improvement, no invented attack attribution |

**Noncompensable safety/process failures:** Executing a real flood or test without authority; blocking whole geographies/providers on unclassified volume; disabling accessible routes without fallback/owner review; collecting or publishing real user identifiers; passing service based on 5xx alone despite confirmed legitimate false positives; deploying real WAF rules or using GitHub Actions in this exercise. Stop, document the defect and score it separately from arithmetic. Suggested classroom-only interpretation: 17–20 robust reasoning, 12–16 material gaps, 0–11 substantial rework. **A great paper score says nothing about a real government portal's security, uptime or compliance.**

## 10. Facilitator worked answers and score calibration

**Facilitator-only until each corresponding round is frozen.** Defensible alternate choices may receive full credit when they respect source, authority, service consequences, accessibility and independent checks. Do not invent logs, user surveys or positive outcomes not on supplied cards.

| Round | Acceptable worked decision and explanation | Unsupported shortcut and challenge |
|---|---|---|
| PD-00 | Baseline /guide 1%, /submit 2%, completed 92%, assisted 90%; define owners and fallback | “All 2xx means complete.” Where is receipt validation? |
| PD-01 | Classify degradation during surge; 80% edge volume rise, submit 30% errors, guide 1% stable, panel 47%; DDoS unproved | “Many providers means attack.” Which behavior is specifically abusive? |
| PD-02 | 93% worker utilization, 580 queue > 300 caution; investigate backend and retries, consider H1–H4 | “Normal sampled database p95 clears backend.” What about workers/queue/code? |
| PD-03 | Count-only, /submit-scoped plan with owners, accessibility tests, expiry and independent switch | “Count mode stops attackers.” Did any enforcement occur? |
| PD-04 | v1 origin 12% (improved), panel 81% but assistive 55% and gap 32.5 points: **NO WIDEN** | “300 blocks were attackers.” What proves legitimacy/uniqueness? |
| PD-05 | Reject country/ISP blocking, investigate false positives and backend scaling with privacy controls | “Broad blocking quickly reduces errors.” What is user completion cost? |
| PD-06 | Approve exact submit worker capacity + separate tuned rule under tested rollback; no success before new receipts | “Change approved means throughput fixed.” Where is effect readback? |
| PD-07 | Separate 250/10,000=2.5% origin 5xx, 100 edge 429; 185/200=92.5%, group gap 3.125 points | “Low 5xx proves fairness.” What about 429 and accessibility subgroups? |
| PD-08 | Confirm next 270/10,000=2.7%, 184/200=92%, queue 90; propose staged rule retirement | “One good ten-minute window is permanent recovery.” What next observation? |
| PD-09 | Fictional TEST-AUTH-10 and USER-REC-11 show two end-to-end test receipts; retired rule confirmed; limited conditional acceptance | “We performed real production testing.” No; the exercise supplied fictional receipts and remaining fairness gap |
| PD-10 optional | Respond to new later source as a separate decision | “Later evidence proves earlier DDoS verdict.” When was that evidence available? |

### Worked contrast: misleading origins-only success

At PD-04, a participant writes, “Our /submit origin error rate fell from 30% to 12%, therefore the rate rule worked and we should block two providers.” This is an **unjustified expansion**: origin 5xx denominator excludes edge 429, the user panel still lost 38/200 completions, and assistive/shared participants completed only 22/40. A defensible revision freezes the old statement, quantifies both benefits and exclusions, and proposes narrowed rule plus independent worker-capacity investigation, without attributing attacker intent.

### Worked contrast: targeted mitigation versus broad exclusion

One choice is a time-limited /submit-only rule with an accountable owner, synthetic count baseline, accessible user tests and quick reversal. A second is a country-wide block. On the supplied cards, the first is **conditionally defensible** because failures are endpoint-specific and impact can be measured. The second has **no verified harmful-behavior concentration, user-impact study, or broad blocking authority**; it may exclude residents behind shared/public providers. The most effective-looking attack counter can be the least acceptable service outcome.

### Independent practice IP-06 — freeze at three points

At PD-01 calculate baseline/peak error and panel contrasts, then list what H1–H4 need to be disproved. At PD-04 calculate 12%, 81%, 87.5%, 55%, and a 32.5-point gap; decide whether to widen. At PD-08 calculate two successive recovery windows and write the specific gate for removing emergency rules. At PD-09 state what authorized **fictional** end-to-end completion was supplied and which post-retirement accessibility evidence remains unknown.

**Worked result:** PD-01: surge edge +80%, guide errors unchanged at 1%, submit from 2% to 30%, panel 92% to 47%, not enough for attack classification. PD-04: rule version v1 apparently reduces origin failures yet harms assisted/shared completion; do not widen. PD-07/08: submit 2.5% and 2.7%, panel 92.5% and 92%, queues 580 to 90; owner may consider staged retirement, but causal root and all providers unknown. PD-09: two test receipt types (standard and assisted) plus 2.5% post-rule origin 5xx support **limited fictional service acceptance**; because the latest 100-attempt panel is unstratified, an independent reviewer retains a targeted post-retirement fairness recheck.

**Score reconciliation:** Observer Greta awards C5=0 when a team equates 300 edge 429 responses with 300 malicious persons. A second observer initially proposes C5=1 because the rate rule did match. The **specific asserted classification contradicts the evidence**, so 0 is appropriate for that claim; a later corrected statement is a new submission, not a silent rewrite.

## 11. Communications, debrief and capacity/mitigation improvement

**Unsent internal/public-ready draft** subject to review by Linnea, Sima, Felix, Tenzin, Ambrose and Beatrice:

> “We are addressing a temporary disruption to online submissions during a period of unusually high demand. We are monitoring application errors and service capacity and adjusting narrowly scoped protective measures to maintain access for legitimate users. Residents who cannot complete a request may use the authorized assisted channel. We will publish a verified update about successful submissions and service availability through official channels. The technical cause has not yet been established.”

**Never publish this merely because it appears in the tabletop.** Record draft, accessibility/plain-language review, service/privacy approval, sent and recipient acknowledgment separately. A live service notice should clearly describe actual supported fallback procedures and avoid implying a real investigation or regulatory finding based on classroom figures.

The 25-minute debrief asks: Did any team prematurely call this a DDoS attack? Were request, transaction and person counts confused? Did /guide stability hide /submit failure? Which data distinguished backend pressure from automation? Was the first rule's human cost visible, especially shared-network/assistive users? Did any proposal block entire countries/providers with no legitimate-user analysis? Were v1/v2 rules actually reported applied and independently read back? Did origin/edge denominators remain separate? Why is a new worker pool not proof of root cause? What evidence authorized removal of emergency controls? Did an actual completed receipt exist **only inside the fictional case**? What would a real institution need to independently approve and monitor?

| Improvement ID | Fictional accountable owner / suggested interval after exercise | Measurable follow-up in a separately authorized environment |
|---|---|---|
| **I-01 deadline surge capacity** | Kiran + Linnea / 30 days | Isolated service-load rehearsal comparing expected legitimate demand, worker queue delay, downstream p95 and error rates, with exact workload and no Internet flooding |
| **I-02 scoped mitigation and safe expiry** | Roxanne + Julien / 21 days | Review synthetic route-only count/enforce choices and rollback receipt; ensure whole-country/provider blocks fail unapproved change review |
| **I-03 inclusive transaction monitoring** | Sima + Felix / 21 days | Controlled, privacy-minimal standard, assistive and shared-network end-to-end test receipts; fail release for material group access impairment |
| **I-04 source/denominator integrity** | Kiran + Roxanne / 14 days | Frozen dashboard fixture separates edge 429, origin 5xx, queued and completed application, retries and unique consented cohort attempts |
| **I-05 assisted service fallback and duplicates** | Felix + Linnea / 30 days | Authorized offline rehearsal of alternative submission/receipt and reconciliation without duplicate filings |
| **I-06 post-rule accessibility/communication** | Sima + Beatrice + Tenzin / 14 days | Review a mock rule retirement and two drafts with clear failure/unknown wording and independently checked accessible instructions |

Dates are **fictional teaching targets**, not NIST deadlines or evidence that an organization implemented these recommendations. The tabletop ends when A1–A6, frozen decisions, independent scores, safety findings and a corrective-action plan exist. The fictional portal may have **bounded restored service** while DDoS attribution and complete real-world resilience remain unknown.

## 12. Primary sources and rights

1. [NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management (April 2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — incident response as part of CSF-aligned risk management; does not prescribe this exact exercise.
2. [NIST CSWP 29, The NIST Cybersecurity Framework 2.0 (February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — six nonprescriptive Functions and outcome-focused decisions.
3. [AWS Shield Advanced, Detection logic for application-layer threats](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-detection-application.html) — compare traffic volume/composition with historical baselines to reduce false positives; AWS-specific mechanism, not detection proof for CivicBridge.
4. [AWS WAF, Rate-based rule high-level settings](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-high-level-settings.html) — evaluation windows, aggregation, limit and scope-down.
5. [AWS WAF, Scope-down statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-scope-down-statements.html) — restrict a rule's inspected/matched request category.
6. [AWS WAF, Applying rate limiting](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-request-limiting.html) — Count versus block/challenge mechanics, with normal users possibly affected.
7. [AWS WAF, Rate-based rule caveats](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-caveats.html) — approximate rates, delayed effect and rule-setting side effects.
8. [AWS Shield Advanced, CloudWatch metrics commonly used for health checks](https://docs.aws.amazon.com/waf/latest/developerguide/health-checks-metrics.html) — application/error-health counters and resource-specific semantics.

All teams, service descriptions, population segments, edge/HTTP/queue counts, event cards, test receipts, sample results, scoring and decision examples are original **synthetic educational material**. This case contains no real resident records, offensive DDoS steps, attack traffic, cloud rule commands, IP addresses or secrets. Source documentation is linked and paraphrased and is **not copied/relicensed**. Original OpenCyber Academy writing follows [RIGHTS.md](../../../RIGHTS.md) and its CC0 scope and third-party exceptions. No academic accreditation, public-service legal compliance or real incident is claimed.
