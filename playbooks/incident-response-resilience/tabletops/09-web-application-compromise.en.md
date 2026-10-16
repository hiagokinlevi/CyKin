# TableTop 09 — Web application compromise: search-query errors, authorization and evidence-limited recovery

**Edition:** English · **Exercise ID:** TTX-WAC-09 · **Catalog scenario ID:** `web-application-compromise` · **Editorial date:** 2026-10-15  
**Editorial state:** Original fictional defensive teaching exercise; independent technical, privacy and human review pending.  
**Audience:** Application owner, application engineering, DB engineering, SOC, forensic evidence, data ownership, IAM, release/change authority, continuity, quality assurance, legal/privacy, communications, executive command and independent observer.  
**Timing:** 15-minute briefing, 90-minute inject-based tabletop, 25-minute debrief. No terminal, live database, customer record, active exploit or production feature-flag operation is required.  
**Navigation:** [Previous authored TableTop — 08, Lost field laptop](08-lost-laptop.en.md) · [Supplementary incident-response playbook index](../README.md) · [Next catalog scenario — 10, Domain routing hijack (summary only; its authored tabletop is not yet verified)](../../../web/tabletop/scenarios.json). This document expands, rather than duplicates, [the ninth item in the original ten-scenario catalog](../../../web/tabletop/scenarios.json). See [primary references and rights](#12-primary-references-and-rights).

## 1. Synthetic situation, investigation question and safety boundary

**Everything in this scenario is invented:** the organization, product, customer identifiers, participants, service logs, timestamps, queries as conceptual labels, row/operation counts, approvals, test results and outcomes. No real user data, executable database query, injection string, live network endpoint, useful access credential, customer record or exploitation instruction appears here. The route names **/customer-search** and **/account-view** are inert, fictional conceptual labels, not an invitation to call a URL. Do not run active exploitation, security scanning, error-triggering probes, or adversarial test traffic against production to “confirm” any suspected flaw. All tests described as performed are **prewritten fictional facilitator fixtures**, not work executed by an assistant or learner.

**Fictional organization:** **Mosswick Membership Services (MMS)** operates a member portal named **Everglade Account Desk**, supporting approved account lookups and normal member profile views. Its search service queries a database through service role **DB-SEARCH-4**, which should be restricted to data allowed for the authenticated member and to an approved read-only search view. Normal **/account-view** traffic uses an independent access path; search has a separately controlled, owner-approved feature flag **FLAG-SEARCH-9**.

At **09:07 UTC**, a change to **/customer-search** is introduced without a recorded review/production approval. Soon afterward, application responses contain unexpected DB errors, database logs show malformed-query errors and a spike in read-query executions. The initial count of individual customer records that may have been read, returned to a user, disclosed outside permitted scope or ultimately affected is **unknown**. No source establishes that an attacker exploited SQL injection, that a customer read someone else's records, that bytes were exfiltrated or that a legally defined breach occurred.

### Six distinctions required at every decision

1. **Unreviewed change**: source/deployment or configuration records show a modification not matching the approved release ledger. This is a change-control finding, not yet proof of a security exploit or a malicious developer.
2. **Malformed query**: an application/DB error indicates an invalid database command was attempted, but it does not uniquely establish SQL injection, its cause, or successful unauthorized result rows.
3. **Elevated DB read volume**: a count of query executions or logical page reads is **not** a count of unique customer records, authorized records returned, bytes leaving the system, or people accessing data.
4. **Authenticated principal**: a database role or application session label is not a reliable human attribution or proof of an authorization decision for a particular customer record.
5. **Query succeeded versus records exposed**: an accepted read can be within policy, cached, repeated, filtered by tenant, or returned to a permitted application cache. Only source-backed lineage can support which exact records, recipients and boundaries were involved.
6. **Recovery of search service versus closure of data impact**: reviewed code, least-privilege DB role and safe functional tests can restore an approved search path while the historic data-risk inquiry remains open.

### Learning objectives

- **O1 — Prepare and govern**: assign application, data, database, IAM, evidence, change and privacy decision rights; identify authorized fallback service.
- **O2 — Detect and interpret**: distinguish app 5xx, DB query error, read-query volume, logging completeness, source clocks and actor/record hypotheses.
- **O3 — Preserve and contain**: save bounded application/database query traces and release records; approve a **search-only** feature-flag disablement with implementation/readback and a stable unaffected profile path.
- **O4 — Determine privilege and data scope**: compare the actual DB role and authenticated member boundaries with approved policy, without using live exploitation or inventing affected-record totals.
- **O5 — Recover safely**: review parameter binding and tenant-aware authorization, correct query generation, narrow DB permissions and run nonoffensive, isolated positive and negative tests before monitored production acceptance.
- **O6 — Improve demonstrably**: maintain honest user/data communication, a scoreable worked exercise packet and predeployment testing, access-review and data-impact checklists with accountable retests.

### NIST and OWASP mapping; no invented compliance or required choreography

[NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), final April 2025, is a **CSF 2.0 Community Profile** rather than the former Rev. 2 incident-life-cycle checklist. [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) contributes **Govern, Identify and Protect** to preparation and safeguards; **Detect, Respond and Recover** frame incident decisions and lessons feed improvement. These roles, paper injects, timings and scoring are an **original pedagogical application**, not prescribed NIST mandates.

| Function emphasis | Teaching action | Nonclaim |
|---|---|---|
| Govern / Identify / Protect | Current inventory, feature flag ownership, tenant/data contracts, release approval and DB privilege baseline | A documented policy does not prove effective production enforcement |
| Detect | Compare route-specific 5xx, DB errors, read executions, source and clock windows | More reads or malformed queries alone are not successful data theft |
| Respond | Preserve trace/custody, approve narrow feature-flag stop, review actual DB grants, coordinate data owner | A change ticket or feature-flag proposal is not proof it was applied |
| Recover | Review parameterized tenant-scoped fix, least-privilege read role, isolated then approved production tests | A passing happy-path search is not authorization or impact closure |
| Govern / Identify/Improvement | Source-to-release gates, targeted query tests, review of access and evidence impact checklist | A tabletop score is not certification or proof of production security |

The **OWASP Application Security Verification Standard (ASVS) v5.0.0** provides stable verification criteria; particularly [v5.0.0-1.2.4](https://github.com/OWASP/ASVS/blob/v5.0.0_release/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.json) calls for data selection/queries protected by parameterized queries, ORMs, frameworks or equivalent injection protections. This is a **defensive control target**, not proof this case is SQL injection. The [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) explains parameter binding and defense-in-depth least privilege; it does not replace **per-record/tenant authorization**. No attack payloads or executable SQL are included.

## 2. Named teams, decision rights and limits

Every named participant below belongs solely to this fictional case. Real organizations must use current production delegation, privacy restrictions and emergency change processes. Teams may share discussion but **cannot substitute one person's verbal agreement for independent approval, operator action and readback**.

| Team and named participant | Responsible decisions and reason | Cannot authorize or infer |
|---|---|---|
| **Maren Cobalt — Incident Commander** | Open security incident, assign source questions, prioritize reversible containment and coordinate scope/communication | Declare exploit, data theft, human malice or mandatory breach notification from error counters |
| **Ishan Cedric — Portal Product Owner** | Define protected search and unaffected profile functionality; approve service-impacting flag suspension and release acceptance | Rewrite data-owner classification, perform unauthorized production change or certify DB evidence alone |
| **Rhea Ashcroft — Application Engineering** | Compare unreviewed change to approved source, review query construction/validation and tenant checks, propose a reviewed patch | Run active probes against production or claim SQL injection proven from malformed errors |
| **Bogdan Wiese — Database Operations** | Preserve existing read-only DB logs via approved source, evaluate role permissions and implement independently approved least-privilege grants | Count logical reads as unique records or grant/change privileges without data-owner and change authority |
| **Nima Gallow — Customer Data Owner** | Define permitted customer fields/tenant access, minimum data-impact questions and approve scoped collection/claims about affected data | Conclude record exposure from a number of DB executions or inspect unrelated customer contents without necessity |
| **Althea Innes — Evidence and Forensic Custodian** | Collect approved source/clock/query-trace metadata, access and release records; protect provenance, integrity and case access | Execute suspicious queries, copy raw customer data broadly or equate a request with acquisition |
| **Leandro Vos — IAM and Access Reviewer** | Compare effective service DB grants with approved tenant/data authorizations, review identity delegation and scoped role proposal | Declare human initiator from a service account name or delete role evidence prematurely |
| **Mirael Smeaton — Change and Feature Flag Owner** | Execute exact **approved** FLAG-SEARCH-9 stop and eventual re-enable with separate operator receipts/independent readback | Self-approve application impact, disable unrelated portal routes or assume a requested flag has taken effect |
| **Tova Arden — Independent Test and Quality Lead** | Plan safe, isolated normal/invalid/tenant-boundary tests; verify failures and separate production acceptance evidence | Generate offensive payloads in production or call one passing lookup a full security clearance |
| **Dustin Orrell — Member-Service Continuity** | Provide accurate fallback for customer searches without duplicate submissions or unsafe disclosure; measure impact of disabled search | Override feature-flag owner, invent successful member search or disregard data minimization |
| **Liora Finch — Legal and Privacy** | Determine data-minimizing inquiry, contract/legal questions, controlled retention and any notification analysis from facts/jurisdiction | Announce a reportable breach, record count or universal deadline absent evidence |
| **Rowan Thacker — Communications** | Draft evidence-limited member/staff notices with authorizers, next update and delivery status | Say customer records were stolen, all data are unaffected, or fix is deployed without receipts |
| **Vesper Solis — Executive Sponsor** | Coordinate resources and organizational risk/continuity escalation within delegated limits | Waive Nima's data-owner or Ishan's service acceptance and independent test gates |
| **Ellis Fenmar — Neutral Facilitator/Observer** | Release inject cards, freeze scores, maintain facts unchanged and reconcile independent evaluator reasons | Manufacture a log line, count nonexistent records or operate live systems |

**Two-owner boundary:** Ishan owns search continuity and the impact of disabling a feature; Nima owns permitted data use/impact claims. Database/flag operators act only under exact authorized change scope. Tova provides independent functional/security evidence. Althea controls the integrity of case sources. A plan, approval, “deployed” message, independent observed state and data owner's acceptance are **distinct receipts**.

## 3. Preparation, three clocks, packet and evidence contract

The exercise lasts **90 minutes** plus briefing/debrief. The facilitator distributes **WC-00** at minute zero and withholds **WC-01 to WC-10** until their stated release times. Give participants blank evidence/release ledger, search failure matrix, change/flag envelope, database grants sheet, data-impact worksheet, isolated test record, monitored return gate and observer rubric. Every case datum is a **synthetic, source-labeled fixture**, not an observation collected from an actual service.

Maintain three separate clocks: **fictional source/event time UTC**, **exercise minute when Ellis reveals a card**, and **exercise minute of frozen learner decision**. Logs may also contain ingestion time. A later-released card describing an earlier event **cannot** justify a prior conclusion. On revision, preserve the original signed reasoning and add a versioned correction.

**Minimum decision record:** `ID | source/event UTC | card release/freeze minute | observed record and denominator | hypotheses/negative control | affected app route/DB scope | customer/service harm of action | authorities | proposed/approved/simulated-executed/independently-verified | rollback/expiry | source needed next`. “Unknown” is a valid and frequently required value.

**Log/source discipline:** Request the original, retained app/DB query traces, time alignment, schema/version identity, request correlation and role data through a **permitted read-only** interface; preserve source versus archived copy versus analyst derivation, access authorization, restricted location, collector/time, integrity readback and query coverage. Avoid copying raw SQL user inputs, full customer rows, personal identifiers or passwords into the shared exercise. A hash of an archive proves selected bytes match, not that logs are complete or that returned result content is harmless.

**Stop card:** No live attack traffic, exploit string, fuzzing, unauthorized DB query, production table dump, direct use of customer records, broad credential reset or public assertion of breach. If someone proposes “try a suspicious input on production to verify SQLi,” freeze the unsafe proposal and direct it to a reviewed **nonproduction fixture**, with no payload in the teaching file. A live incident uses the real organization's change, incident and privacy procedures.

## 4. Progressive timed injects and fixed source records

The cards are fictional UTC on the same simulated incident day. Do not invent additional telemetry to resolve an ambiguity. The optional last card is a **new** continuation, not a replacement of a frozen decision.

| Exercise minute | Inject | Source UTC | Core decision to freeze |
|---:|---|---|---|
| 0–7 | **WC-00** | 08:50–09:00 | Source/change and tenant/DB permission baseline |
| 8–17 | **WC-01** | 09:07–09:20 | Unexpected errors and route-specific effect; no premature exploit claim |
| 18–27 | **WC-02** | 09:21 | Query traces, malformed/volume versus unique records |
| 28–36 | **WC-03** | 09:28 | Data owner impact questions and rights |
| 37–46 | **WC-04** | 09:41–09:46 | Owner-approved feature flag, scope and independent readback |
| 47–56 | **WC-05** | 09:53 | Source preservation receipts and DB effective grants |
| 57–65 | **WC-06** | 10:04 | Historical read volume/time coverage and negative findings |
| 66–73 | **WC-07** | 10:25 | Initial isolated fix fails a tenant boundary gate |
| 74–81 | **WC-08** | 10:44 | Revised fix/least-privilege isolated test passes |
| 82–90 | **WC-09** | 11:12–11:25 | Approved bounded production return and audit window |
| Only after all freezes | **WC-10 optional** | 12:10 | Later data-scope inquiry, not a retroactive outcome |

### WC-00 — Before the unreviewed change (minute 0; Govern / Identify / Protect)

**Fictional 08:50–09:00 baseline packet:** Owner Ishan has approved search route **/customer-search**, member profile route **/account-view**, app release baseline **APP-RELEASE-27** and current valid feature flag **FLAG-SEARCH-9 = enabled**. Data owner Nima's approved policy restricts a member's search results to the member's own authorized tenant and the minimum fields needed for the requested service. It is **not** evidence every deployed role/endpoint enforces this rule. A planned deployment through signed **CHG-27** does not include a new search implementation. The app's DB service role is **DB-SEARCH-4**; its *actual effective grants* are not supplied until later. Search can be disabled without removing /account-view and without permanently deleting members' data.

**Read-only ten-minute synthetic metrics:** Search receives **2,000 requests**, with **20 HTTP 5xx**; profile receives **2,000**, with **20 HTTP 5xx**. DB audit summarizes **300 search-service read-query executions**, a *query-execution count*, not rows and not distinct member records. The case provides no attack classification or data breach.

**Worked baseline:** search 5xx rate = 20/2,000 = **1%**; profile = 20/2,000 = **1%**. This rate is a service-health comparison, not an acceptable loss threshold prescribed by NIST. An access-control rule is only as effective as the real code/DB grants enforcing it.

### Round 1 — WC-01: unreviewed search modification and localized errors (minutes 8–17; Detect)

**Fictional 09:07 change and 09:10–09:20 observations:** A source/deployment ledger shows search code marker **SEARCH-R-14** introduced at 09:07 without a matching signed review in the **supplied, complete release register for this time**. Application metrics show **2,400 /customer-search requests, 624 HTTP 5xx**. Profile metrics show **2,000 /account-view requests, 20 HTTP 5xx**. A DB service summary shows **1,800 read-query executions** attributed to DB-SEARCH-4 in this window. No row IDs, returned result cardinality, client payloads, tenant ownership, recipient downloads, attacker identifiers or complete retention coverage are supplied.

**Decisions by team:** Maren opens **MMS-IR-009** as *search degradation with possible security impact*; Ishan declares the search path critical but separable from normal member profile access; Rhea reviews intended vs actual release authority without running production probes; Bogdan preserves DB audit windows; Althea opens evidence custodianship; Nima requests a purpose- and owner-limited impact inquiry rather than guessed record totals. Dustin prepares an approved search fallback. **No one declares SQL injection or data theft proved.**

**Worked metrics:** search 5xx = **624/2,400 = 26%**; profile = **20/2,000 = 1%**, unchanged; DB read-query executions = **1,800/300 = 6×** baseline (a **500% increase** in this particular count). A query execution can read repeated pages or none; it cannot be multiplied into affected customer counts.

### Round 2 — WC-02: malformed query errors are a clue, not a payload or successful exploit (minutes 18–27)

**Fictional 09:21 source-labeled query-trace summary:** App trace type **APP-T-21** has **180 DB syntax/shape errors** correlated with the 09:10–09:20 search interval. **DB-T-21** reports **a subset** of rejected statement shapes and a simultaneous increase in successful **read** operations under DB-SEARCH-4. No raw SQL, exploit input, statement text, bound-parameter material, customer name or actual returned record list is included. The 180 malformed errors are **not** an additional disjoint class of 624 application 5xx; overlap is possible and cannot be calculated from the supplied sources. It remains unknown whether the code built dynamic unparameterized SQL, whether unexpected input reached an interpreter, whether a database schema or query planner regression occurred, or whether an application bug simply generated invalid statements.

**Competing hypotheses:** H1 unreviewed query builder defect, H2 mismatch between app and DB schema/version, H3 unusual legitimate search load or retry amplification, H4 attempted injection or authorization bypass, H5 a mixed cause. These are **not equal-probability** findings. To discriminate, request **reviewed code-to-query binding evidence**, captured trace IDs and status, qualified DB grant list, normal-error regression comparison and sampled backend dependencies. **Do not attempt exploitation in production** to see what input might “work.”

**Decision:** Rhea proposes a code review in an approved offline development copy; Bogdan preserves bounded existing DB events; Maren prioritizes a reversible search-only feature suspension with Ishan's owner approval if errors persist. Nima holds data-impact conclusions pending relevant record/recipient evidence. The malformed-query finding supports **risk assessment and defensive correction**, not an announced vulnerability classification.

### Round 3 — WC-03: involve the data owner before impact claims (minutes 28–36)

**Fictional 09:28 owner/data map:** Nima provides a signed data-classification and access-purpose map: **member directory attributes** may be shown to the authenticated matching tenant; **restricted case notes** must not be returned by portal search; raw customer data can be copied for investigation only under reviewed necessity and lawful access. The supplied owner record lists **no approved export** associated with the unusual interval. A DB read counter alone does not show that an export occurred. Some responses may be served from application caches, and the available logs do not yet bind each query to unique row IDs and a particular recipient. The total potentially affected records remains **unknown**.

**Teams decide:** Nima defines a minimal evidence/impact checklist: source tenant, query identity, result cardinality **if available**, returned fields, app data path, authenticated recipient authorization, actual exposure beyond intended tenant, logging coverage and source confidence. Liora reviews data minimization/retention and jurisdiction-specific notification questions only after facts; Althea plans access-restricted metadata acquisition. Leandro compares customer-facing authorization policy with the effective DB role without assuming they are equivalent. Ishan accepts service-impacting protective flag decisions but cannot pronounce data impact on Nima's behalf.

**Negative control:** A large number of DB reads on a restricted service may raise concern, but **lack of a record count must stay unknown**, not “none affected” or “1,800 customers exposed.”

### Round 4 — WC-04: owner-approved search-only containment with effect verification (minutes 37–46; Respond)

**Fictional 09:41–09:46:** Ishan approves **FLAG-AUTH-41** to disable **/customer-search only**, with user-impact explanation, time-bounded review, rollback owner and unaffected /account-view validation. Mirael's **FLAG-APPLY-43** reports the feature flag changed to disabled at 09:43. Independent service configuration readback **FLAG-READ-45** verifies FLAG-SEARCH-9 disabled **for the named search route** at 09:45. An authorized **synthetic** functional observer receipt **PORTAL-46** says search is unavailable by design and /account-view still loads its permitted profile test; no actual customer data were used. The test is a paper-provided fictional observation, not a live trial performed here.

**Response decision:** Maren records **approved → simulated operator-applied → independently readback** as separate statuses. Ishan and Dustin activate a defined safe search fallback with qualified support personnel and no copies of member records outside policy. Althea protects original app/DB logs from deletion during the change. Bogdan/Leandro conduct a grants review under approved read-only access. **No broad portal shutdown** is justified from the supplied localized failure. A disabled route stops **that path** prospectively, not all alternate APIs or earlier database reads.

**Conditional consequence:** If FLAG-READ-45 or service test were absent, the status would remain **applied-reported / effect pending**, not “confirmed contained.” If profile service failed, Ishan would stop or revise the change with a specific authorized rollback, not call it success.

### Round 5 — WC-05: source preservation and effective privilege inventory (minutes 47–56)

**Fictional 09:53 evidence and IAM packet:**

- Forensic request **REQ-48** asks for existing app traces (09:00–09:50), DB query shape/status records, release-register history, IAM policy revisions and feature-flag events. A request is **not** a collected source.
- Read-only archive **ARC-51** has an acquisition receipt from the approved log store for **app and DB metadata 09:05–09:50**, with collector, source route, UTC offsets, restricted case location and retention time. Independent copy-byte readback **HASH-52** succeeds for **that slice**, but no customer-content export or complete multi-region access-log proof exists.
- Effective role snapshot **DB-GRANT-53** shows DB-SEARCH-4 **read rights on an approved member-search view**, **plus unnecessarily broad read rights for restricted case-note metadata**. It shows no write/admin permission in this snapshot; neither the existence of the grant nor its name proves it was used.
- Release history confirms SEARCH-R-14 lacked the specified reviewer approval. The historical application-to-DB network route and tenant session/source correlation are **incomplete**.

**Decisions:** Althea labels `requested / archived copy / independent byte readback / analyzed` separately. Bogdan/Leandro identify the extra read grant as a **least-privilege policy gap**, seek a reviewed, narrow role proposal and retain original effective-grant evidence before changes. Nima decides whether case-note metadata is sensitive and whether a real data-impact inquiry needs more authorized sources. Rhea designs a reviewed parameter-bound, tenant-aware fix without using the questionable production query as a test harness. **Do not equate available privilege with observed data access.**

### Round 6 — WC-06: unusual reads and coverage/attribution limits (minutes 57–65)

**Fictional 10:04 independent read-only assessment:** Althea and Bogdan correlate the synthetic 09:10–09:20 events by trace ID, service principal and source window. **TRACE-604** demonstrates repeated successful **read-query executions** over the approved member-search view by DB-SEARCH-4; its **logical page-read counter** is **6,400**, but the actual unique records examined, returned to the application or visible to a customer are not recorded. An aggregate data summary also identifies an unexplained rise in reads of the **member view**, with no supplied access to case-note contents. Customer-facing session logs for the event window are **partly missing**, so no actor/tenant-to-result reconstruction is complete.

A 09:46–10:03 service sample after the feature stop shows **no new malformed-query surge on the disabled search route**; it does **not** prove historic data safety or rule out another path. 6,400 *logical page reads* is not **6,400 customers**, nor is 1,800 successful/attempted query executions the number of rows in result sets.

**Decisions:** Nima retains “number of affected customer records and disclosure status **unknown**.” Maren updates the incident to **confirmed search change-control defect with abnormal DB behavior and elevated potential data risk**, not confirmed exfiltration. Liora requests a bounded legal/privacy review if subsequent specific unauthorized access evidence emerges. Leandro/Maren reject a proposal to use an administrative all-records query in production for curiosity; Althea preserves already available original sources and requests missing app-session correlation from approved custodians.

**Negative control:** “No anomalous reads in a short post-flag window” is a bounded **continuing-activity** observation under that rule, not a finding about **past data exposure**. A service principal without session binding cannot identify a malicious human.

### Round 7 — WC-07: first isolated candidate fails the tenant authorization test (minutes 66–73; Recover)

**Fictional 10:25, nonproduction review/test fixture only:** Rhea proposes change **FIX-Q-1**: use parameter binding rather than interpolating user-controlled material into query structure; validate expected input shape; keep the search feature behind FLAG-SEARCH-9 for controlled promotion. Tova's **isolated fixture** reports: (a) normal test-only member search passes; (b) **safe invalid-format input** is rejected with a consistent application-level 4xx without sending malformed SQL; (c) a **synthetic foreign-tenant directory record** is unexpectedly visible to a logged-in test principal whose authorization should exclude it. The result does **not** identify an exploit payload; the test is a scripted safe authorization negative control over mock records. There is **no production query or real customer data** involved.

**Decision:** **NO-GO** for production restore. Rhea must repair tenant authorization independently of parameterization; Nima owns permission expectations, Tova witnesses the negative test, Leandro reviews DB grants and Ishan maintains the search flag disabled until corrected acceptance. A patch that rejects malformed input can still disclose *well-formed but unauthorized* data if authorization checks are incorrect.

**Worked contrast:** “Safe parameter binding means secure search” is incomplete: parameter binding separates code from data but does not automatically enforce row-level tenant access. A passing invalid-input test is not a substitute for an authorization test.

### Round 8 — WC-08: reviewed candidate and narrowed role pass isolated gates (minutes 74–81)

**Fictional 10:44 updated isolated fixture:** Reviewed change **FIX-Q-2** carries distinct sign-offs from Rhea and the service/QA reviewers. It uses a **reviewed parameterized query interface**, explicit authenticated tenant-scoping at the application boundary, a **DB-SEARCH-LEAST** role granted only approved read-only member-search view access, and disallows the earlier unnecessary restricted case-note grant. **The paper case gives no SQL statement or payload.**

Tova's separately labeled **QA-44** nonproduction tests report: (i) two permitted test-only searches return the correct within-tenant synthetic records; (ii) an invalid-format test is safely rejected; (iii) a foreign-tenant mock record is not visible; (iv) an attempted unrelated case-note read by the **new test role** is denied; (v) no unsafe side effects appear in the tested read-only fixture. Independent change review confirms the intended artifact and role policy version match the signed proposal. **Not supplied**: production deployment, production customer data, complete threat eradication, exhaustive row-level proof or historic impact attribution.

**Decision:** The revised candidate **may proceed to a separately authorized bounded production change** if change/rollback, privacy, functionality and monitoring gates are met. Nima approves the **permitted data semantics**, Ishan approves search return criteria, Bogdan/Leandro approve scope-limited DB-role grants, Tova owns independent test acceptance, Mirael executes only after approvals. A successful isolated test is **not** a production receipt.

### Round 9 — WC-09: approved return and independent no-continuing-read check (minutes 82–90)

**Fictional 11:12–11:25 owner-approved production acceptance packet** (reported as an inject, **not** implemented by this classroom):

- **CHG-RETURN-112** is signed by Ishan, Rhea, Nima for data purpose, and the independent DB/change owners. It scopes the change to /customer-search, FIX-Q-2 and DB-SEARCH-LEAST, with monitored rollback and a separately authorized re-enable of FLAG-SEARCH-9.
- **APPLY-115** and **FLAG-REOPEN-116** are *fictional operator receipts*. Separate independent app/DB policy readbacks **APP-READ-117** and **DB-ROLE-READ-118** confirm the **named** versions, feature state and effective DB-SEARCH-LEAST grants. Unaffected /account-view remained available in its covered service check.
- An authorized, strictly safe **production acceptance record** using approved test-only member identities—not hostile payloads—reports **normal search completion** and correct tenant-bound records. A safe malformed-format sample was **rejected** by validation **without database interpreter execution of hostile content**; an independent owner-reviewed negative authorization check received no foreign-tenant result.
- Independent audit evidence **AUD-25** for fictional **11:15–11:25 UTC** shows **2,000 /customer-search requests and 24 HTTP 5xx** (1.2%); **320 search read-query executions** in that ten-minute period (versus prior **300** baseline), and **no continuing unusual read-query pattern in the covered, independently reviewed app/DB sources**. The coverage explicitly excludes unknown earlier events, uninstrumented access paths and any historical recipient/data lineage the organization cannot reconstruct.

**Decision:** Ishan can accept **limited restored search function** for the tested route and time; Nima can accept the permitted output fields/tenants for the tested fixture and production-safe acceptance receipts, but **cannot** conclude every historical data exposure question resolved. Bogdan/Leandro independently verify least-privilege grant and absence of ongoing anomaly in **the observed window**. Maren retains the historical incident open for time-scoped forensic/data-risk review; Liora controls any later legal reporting decision. A lower error rate and secure test result **do not** prove there were zero unauthorized reads before mitigation.

**Worked acceptance numbers:** baseline search 1% vs peak 26% vs restored **24/2,000 = 1.2%**; execution count baseline 300, peak 1,800, restored 320. The increase at peak is 1,500 executions (500%) and later reduction is 1,480 from the peak; neither delta equals distinct customer records. “No continuing anomaly” is the independent review's **bounded result**, not a guarantee that all legitimate user paths or every DB logging class was observed.

### WC-10 — Optional follow-on evidence; never retroactively attributed

Only after all WC-09 decisions freeze, a facilitator may issue a *separately numbered and sourced* card reporting a new record-level authorization discrepancy **or** an independently supported clean finding for a specific covered slice. If new evidence establishes access to particular records by an unauthorized recipient, Nima/Liora and Maren reassess scope and obligations **in that future branch**. It must **not** be inserted into WC-01 through WC-09 or converted into a fabricated current record count, legal breach or actor identification. The canonical incident retains historical unknowns.

## 5. Mechanism: safe query construction versus row-level authorization

**Definition:** Injection risk arises when untrusted data can influence the *structure* interpreted as a database command. Parameter binding or a reviewed safe query interface separates expected input values from command structure. Independent **authorization** determines which tenant/record/field the authenticated requester may see, regardless of whether input is syntactically valid. Least-privilege DB permissions constrain the application service's *potential authority*, but do not replace application-level row/tenant checks or a data owner's approval.

**Worked comparison, with no executable SQL:**

| Layer | Before/under investigation | Reviewed design and safe evidence | Important limit |
|---|---|---|---|
| User input | Abnormal search request forms and errors; specific payload **not retained here** | Validate format/length and bind data values in a nonproduction fixture | Malformed request is not automatically an exploit |
| Query generation | SEARCH-R-14 lacked review; query shape errors appear in logs | FIX-Q-2 uses reviewed parameter binding / safe API | Correct syntax alone is not authorization |
| Tenant/data decision | Access policy says only correct member/tenant allowed; enforcement needs proof | Negative foreign-tenant test rejects cross-tenant result | A fixture cannot prove all production routes safe |
| DB service authority | DB-SEARCH-4 held unnecessary case-note metadata read grant | DB-SEARCH-LEAST has minimal read-only approved view; unrelated read denied in test | Grant presence is not proof of its past use |
| Runtime observations | 1,800 read-query executions, 180 syntax errors and 624 app 5xx | Restored scoped window 320 read-query executions, 24 app 5xx, independent read review | Events/rows/bytes/recipients are different populations |
| Historical impact | Source-session/result coverage incomplete | Nima leads purpose-specific evidence assessment | Impact count and exfiltration remain unknown |

**Why a safe negative test matters:** At WC-07 the first patch passes valid search and invalid-format rejection but fails **foreign-tenant data authorization**. Deployment would remain unacceptable even if DB errors fell to zero. At WC-08 the next *independently reviewed* candidate passes both input and authorization constraints **in isolation**, allowing a narrow production acceptance process, not instant clearance.

**Primary implementation guidance:** [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release) and the [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) support prepared/parameterized APIs and least-privilege database accounts. The [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) explains enforcing access rules for each request and denying by default. This educational source discussion **never** supplies a working attack string or encourages production exploitation.

## 6. Reproducible evidence arithmetic and negative controls

A learner can reproduce this fixture without software, SQL access or personal data. Keep denominators, query types, time windows and claimed observation status explicit.

| Ten-minute window | Search requests | Search HTTP 5xx | Search 5xx rate | DB search read-query executions | Profile HTTP 5xx |
|---|---:|---:|---:|---:|---|
| 08:50–09:00 baseline | 2,000 | 20 | 1% | 300 | 20 / 2,000 = 1% |
| 09:10–09:20 anomaly | 2,400 | 624 | 26% | 1,800 | 20 / 2,000 = 1% |
| 11:15–11:25 bounded recovery | 2,000 | 24 | 1.2% | 320 | Separately checked normal, no rate supplied |

**Arithmetic:** 624 ÷ 2,400 = **0.26** = **26%**. Difference from baseline = **25 percentage points**. Read-query executions: 1,800 ÷ 300 = **6×**; increment = 1,500, or **500%** increase. Recovery error rate: 24 ÷ 2,000 = **1.2%**, a 24.8 percentage-point reduction from the peak. Recovery read-query volume 320 is near the baseline of 300 but need not be identical under real workloads. **None** of these quantities describes unique records, successful unauthorized disclosures, distinct users or confirmed data movement.

**Negative controls:**

- **NC-1:** A schema migration mismatch or application defect can produce malformed queries without an adversary.
- **NC-2:** A DB role with extra read privilege represents risk but does not prove it accessed those tables.
- **NC-3:** A 6× increase in query executions can result from retries or repeated allowed searches; it is not a 6× record count.
- **NC-4:** A feature flag change proposal is not an applied flag; an operator “applied” event still needs independent route-state/readback.
- **NC-5:** A disabled search route may leave other routes intact and cannot retroactively undo completed reads.
- **NC-6:** A parameterized query with invalid inputs safely rejected can still return foreign-tenant data for **valid** input when authorization is defective.
- **NC-7:** A correct least-privilege DB role is only one enforcement layer; the application must still apply customer/tenant authorization.
- **NC-8:** The absence of continued anomalous reads in a **covered** window is not proof no prior data access or unlogged route existed.
- **NC-9:** A low app 5xx count is not a positive identity/authorization or service-to-data outcome test.
- **NC-10:** Unreviewed deployment is a governance/process fact, not proof the deploying developer had malicious intent.

## 7. Safe preservation, bounded containment and conditional alternatives

Every response below is a **paper decision**, unless the corresponding released fixture explicitly includes separate authorization and effect receipts. This checklist does not confer authority over anyone's production application.

1. **Preserve specific clocks and sources:** Identify original app request/error metadata, DB query-shape/status logs, release/version/flag state, IAM grants and separately covered audit windows. Record precise source UTC and ingestion lag; separate evidence request, copied archive, immutable location, hash readback and analysis notes.
2. **Avoid active proof-by-exploitation:** No attack payload, red-team probe or arbitrary query is needed. Inspect the reviewed change history and permitted passive traces, then use **safe mock inputs in an isolated environment** for regression tests.
3. **Open owner-scoped incident questions:** Ishan names application paths and continuity needs; Nima names authorized customer/tenant data and determines whether more source metadata is needed before making claims.
4. **Apply narrow feature-flag mitigation:** Request owner approval for **FLAG-SEARCH-9** only, record time/expiry/rollback and have a different reviewer confirm actual route state and that /account-view still works. If logging would be lost by a change, coordinate minimally necessary preservation first when feasible without dangerous delay.
5. **Review effective privilege before tightening:** Bogdan and Leandro document actual DB-SEARCH-4 grants and session/delegation impact; propose DB-SEARCH-LEAST for a named purpose. Changes must not destroy the evidence that an overly broad grant existed.
6. **Test code and data scope conjunctively:** Review parameter binding, query builder behavior, expected input validation and tenant-scope enforcement in an isolated fixture. Require an **invalid-format** negative test and an **unauthorized-tenant** negative test. A safe SQL parser alone is insufficient.
7. **Protect nonaffected services:** Continue /account-view where independently verified safe/available; Dustin supplies an approved support fallback without exporting member data outside policy.
8. **Require post-release checks:** Review exact code artifact, DB-role state, route-feature state, test-only normal search, negative malformed-format input, negative tenant access, source-clock logging and stable error/read-query behavior in a named time window.
9. **Evaluate data impact separately:** Nima and Liora decide how to obtain record-level/recipient correlation if needed and lawful. Do not query entire customer tables merely to manufacture a number; mark unobservable history as unknown.
10. **Report only supported findings:** “Malformed SQL observed,” “search change lacked approval,” “role had extra read grant,” and “no ongoing anomaly in one covered window” are distinct findings. “Confirmed SQL injection,” “data exfiltrated,” “records affected,” or “legal breach” require additional evidence not in this canonical fixture.

| Alternative | Authority and prerequisites | Conditional consequence / failure |
|---|---|---|
| **A. Disable entire customer portal** | Ishan service impact, Nima data risks, continuity owner and exceptional scope justification | Not proportional while /account-view remains healthy and a search-only flag is available |
| **B. Suspend /customer-search via approved flag** | Ishan approval, Mirael operation, independent FLAG-READ-45 and PORTAL-46 | Bounded effective containment for search, not previous reads or other routes |
| **C. Actively exploit production input** | No case authorization or safe rationale | Reject: could harm customer data, pollute evidence or produce unauthorized access |
| **D. Copy all customer tables for forensic review** | Separate legal necessity, data owner and restricted handling would be required | Not justified by counts alone; risk of unnecessary sensitive data copying |
| **E. Narrow DB role immediately without source preservation** | Bogdan/Leandro authorized change and minimal prior grant evidence | Possible service interruption and lost historical policy trace; preserve scope where safe |
| **F. Restore first reviewed fix FIX-Q-1** | Tenant boundary must pass but WC-07 explicitly fails | **NO-GO**, despite normal/invalid tests |
| **G. Stage FIX-Q-2 with new least-privilege role** | Owner, QA, IAM/DB and change approvals; independent staging tests | WC-08 passes isolated gates; production is a **separate** question |
| **H. Accept monitored production return WC-09** | Signed owner gates, independent app/DB/flag readbacks, safe tests and covered audit | Supports only defined search service/period, historical impact remains open |
| **I. Declare no breach because reads normalize** | Nima/Liora impact assessment and missing historical evidence required | Unsupported; no continuing abnormal volume does not establish historical disclosure absence |

## 8. Recovery contract and conjunctive acceptance gates

A source-reviewed patch is **not** complete recovery by itself. Engineering, data, identity, operation, customer experience and historical risk must have separately documented statuses. “Gate passed” means source, owner, time and scope are explicit; unsupplied evidence is **pending**, never green by default.

| Gate | Evidence needed | Owner / NO-GO condition |
|---|---|---|
| **G1 trace and integrity** | Source windows/app+DB trace correlation, copy/readback, retention/gaps, pre/post flag chronology | Althea: missing history and query coverage must be explicit |
| **G2 app release authority** | Reviewed source diff, approved artifact/version, exact /customer-search target and rollback | Rhea/Ishan/Mirael: unreviewed FIX-Q-1 is not a production release |
| **G3 safe query construction** | Reviewed bind/ORM usage, safe allowed input formats, nonproduction invalid-format negative test | Rhea/Tova: malformed input must not shape interpreter commands |
| **G4 tenant authorization** | Signed permitted fields and independent cross-tenant denial test | Nima/Tova: **WC-07 failure is hard NO-GO** |
| **G5 least-privilege DB role** | DB-SEARCH-LEAST effective grants/read-only view, unrelated case-note read denied | Bogdan/Leandro: absence of admin is not enough when other reads excessive |
| **G6 search continuity** | /account-view remains usable, approved fallback and no user data duplication | Ishan/Dustin: avoid unnecessarily disabling unrelated routes |
| **G7 controlled production enablement** | Separate CHG-RETURN-112, APPLY/FLAG operation, independent code/flag/role readbacks | Mirael and distinct owner/QA: WC-08 isolated success not deployment |
| **G8 bounded functional proof** | Approved test-only normal search, safe invalid input rejection and owner-reviewed tenant negative check | Tova/Nima: green 2xx alone is not authorization |
| **G9 ongoing anomaly review** | Independent named-window logs with stable read-query rate and no renewed abnormal reads in the **covered** sources | Althea/Bogdan: quiet 11:15–11:25 not a complete historical clean bill |
| **G10 separate data-risk closure** | Data owner review of fields/tenants/recipients, logging gaps, legal counsel sign-off as warranted, residual unknowns | Nima/Liora/Maren: historic affected count unknown, no breach verdict invented |

**At WC-04:** The affected search route is disabled, profile remains available, and investigation continues; service is **not** restored.  
**At WC-07:** First isolated fix fails foreign-tenant result negative control; **NO-GO** despite parameterization.  
**At WC-08:** Revised isolated fixture passes query, authorization and privilege checks; production acceptance **not yet evidenced**.  
**At WC-09:** Owner-approved released change, independent code/role/flag readback, safe normal/invalid/tenant tests and **independently reviewed absence of continuing anomalous reads within 11:15–11:25 UTC** support **limited search-service recovery**. The historical set and number of affected customer records remains **unknown**, and data/privacy impact review is not automatically complete.

**No diagram is provided:** The source/claim matrices and release ledger directly explain the mechanism and decision rights. A decorative arrows diagram would add no necessary fact and could suggest a nonexistent actual data path.

## 9. Independent exercises, required artifacts and evaluation

Participants may complete the following tasks using only released paper cards. They must be able to solve the problems **without a database**, personal records, exploit strings or accessing a real website. Keep all early decisions frozen before the later worked-answer cards.

### Independent practice EX-TTX09-01 — Evidence, errors and hypotheses

**Objective:** separate application faults, possible injection and data-impact claims. **Inputs:** WC-00 to WC-02. **Task:** calculate search/profile origin error rates and DB-query execution change; classify “malformed queries,” “SQL injection succeeded,” “1,800 unique customers read,” and “search change was unreviewed.” **Required artifact:** source/clock/denominator table with at least two alternate mechanisms and the next safe discriminator. **Scoring:** 2 points correct arithmetic, 2 hypothesis humility, 2 data-record limit, 2 named next source = **8**.

### Independent practice EX-TTX09-02 — Containment with service preservation

**Objective:** preserve evidence and minimize user impact. **Inputs:** WC-00 through WC-04. **Task:** compare (A) entire portal shutdown, (B) a signed search-only feature-flag suspension with independent readback, (C) live exploit testing. Name product owner, operator, evidence custodian, fallback and stop/rollback. **Required artifact:** frozen signed change envelope with action/effect status and two negative controls. **Scoring:** 2 scoped choice, 2 authorities, 2 evidence preservation, 2 unaffected-path test = **8**.

### Independent practice EX-TTX09-03 — Least privilege is not observed data theft

**Objective:** assess DB service effective grants and permitted data use. **Inputs:** WC-03, WC-05 and WC-06. **Task:** make a four-column table for (permitted member-search view, excess case-note metadata grant, observed reads, missing recipient/row mapping). Recommend safe grant change and two privacy-bounded evidence requests. **Required artifact:** DB grant/source/impact matrix with owner signature status. **Scoring:** 2 permission/actual-use distinction, 2 named excess grant, 2 minimal evidence plan, 2 unknown historic impact = **8**.

### Independent practice EX-TTX09-04 — Two sequential candidate tests and no hindsight

**Objective:** demonstrate conjunctive release gating. **Inputs:** WC-07, then WC-08, then WC-09 at their release times. **Task:** freeze a NO-GO for FIX-Q-1, a separate isolated-pass/production-pending verdict for FIX-Q-2, and a bounded monitored production-acceptance decision when WC-09 arrives. Include safe malformed-format negative test and foreign-tenant authorization negative test. **Required artifact:** three separately signed decision records and G1–G10 status, no discarded earlier result. **Scoring:** 2 initial hard no-go, 2 independent second tests, 2 separate production gates, 2 residual data unknowns = **8**.

### Independent practice EX-TTX09-05 — Impact and communication without invented records

**Objective:** communicate the most the evidence actually establishes. **Inputs:** WC-01 through WC-09, respecting releases. **Task:** draft a 100-word internal operational update, record drafted/reviewed/approved/sent status, explain why 1,800 query executions and 6,400 logical page reads cannot be converted to affected-record count, and identify two missing record/recipient proofs. **Required artifact:** unsent message, data-owner review note and next evidence trigger. **Scoring:** 2 truthful scope, 2 no record/exfil leap, 2 qualified reviewers, 2 actionable next source = **8**.

### Required cross-team artifacts

| Artifact | Minimum contents | How independent observer challenges it |
|---|---|---|
| **A1 source, clocks and hypotheses** | Card/source event UTC, release/freeze time, observations versus H1–H5 and next falsifier | Did WC-06 or WC-09 appear in an earlier decision? |
| **A2 service error/data evidence** | Baseline/peak rates, DB query/row type distinction, APP-T/DB-T sources, unknown records | Which source counts actual unique returned records? |
| **A3 incident/feature-flag envelope** | Ishan approval, Mirael applied/readback, preservation scope, unaffected route, rollback and expiry | Was a flag requested, applied or independently checked? |
| **A4 privilege and data-owner review** | Effective grants, extra case-note permission, viewed object evidence/unknowns, Nima/legal approvals | Does an allowed DB grant prove use or disclosure? |
| **A5 code/query/recovery acceptance** | FIX-Q-1 NO-GO, FIX-Q-2 isolated pass, WC-09 independent app/DB/flag and functional/audit gates | Did cross-tenant denial and production checks independently pass? |
| **A6 communication and lessons** | Review/approval/dispatch distinction, no breach count, retest owner/deadline and ongoing open inquiries | Would public text confuse abnormal reads with exfiltration? |

## 10. Facilitator worked answers, rubric and independent scoring

**Keep worked answers from participants until their respective round decisions are frozen.** Different choices may earn full marks if the reason, owner, evidence, safety, reversibility and independent verifier are equally strong. Never insert a hypothetical observation into the fixed canonical cards to produce an easy ending.

### Worked answer — EX-TTX09-01

Search error baseline = 20/2,000 = **1%**, peak = 624/2,400 = **26%**, a **25 percentage-point** increase. Profile stays 20/2,000 = **1%**. Search-service read-query executions rise from 300 to 1,800, **6×** or **500% above baseline**, in those two differently timed windows. The 180 malformed errors may overlap search 5xx, so cannot simply be added to 624. “Malformed query shapes” and “unreviewed SEARCH-R-14” are observations in their defined sources; “injection succeeded” and “1,800 customer records affected” are **not established**. Possible code/schema/retry/abuse causes require approved source-diff and query-binding review, not a live exploit.

### Worked answer — EX-TTX09-02

**Choose B provisionally:** Ishan approves only search suspension, Mirael implements, Althea preserves original traces and independent FLAG-READ-45 / PORTAL-46 verify the named route disabled and /account-view functional. The feature flag does not undo earlier DB reads. Broad portal shutdown is disproportionate on present evidence; active production exploitation to “prove” SQL injection is unsafe and unauthorized. A completed change ticket **without** flag readback would remain effect-pending. Dustin manages a no-leak support fallback.

### Worked answer — EX-TTX09-03

Nima's owner record permits member-search view for a matching authenticated tenant and rejects restricted notes. DB-GRANT-53 reveals DB-SEARCH-4's **extra case-note metadata read grant**, but WC-05 provides **no proof that grant was used**. TRACE-604's 6,400 logical reads/operations over member-search view are **not** 6,400 customer records; historic recipient and unique row mapping absent. Propose separately approved DB-SEARCH-LEAST with view-only read and independent denied unrelated read in nonproduction. Ask for exact source/DB role grants at the time and minimally necessary request/recipient/tenant correlation if retained, under Nima/Liora-approved access. Do not copy all customer rows into a case note.

### Worked answer — EX-TTX09-04

1. **WC-07 NO-GO:** FIX-Q-1 passes normal and invalid-format tests but leaks **synthetic foreign-tenant fixture content**, so authorization gate G4 fails.
2. **WC-08 isolated candidate only:** FIX-Q-2 binds values, constrains tenant membership, DB-SEARCH-LEAST denied unrelated read, normal/invalid/foreign-tenant tests pass **in the safe fixture**. G7–G9 production outcomes not yet supplied.
3. **WC-09 bounded recovery:** owner-approved CHG-RETURN-112 and separate app/DB/flag receipts, safe test-only normal search and invalid-format rejection, owner-reviewed foreign-tenant denial, independent logs showing no **continuing** unusual reads in the **named 11:15–11:25 UTC** window. Accept search operations **within that scope**, keeping G10 historic data-impact investigation open. Never use WC-09 to backfill WC-07 decisions.

### Worked answer — EX-TTX09-05

A defensible message is below in section 11. Data-risk explanation: **1,800 read-query executions** count actions under a DB role, and **6,400 logical page reads** count storage/internal read units, not unique customer rows, records sent to clients or data exported. The query may repeat the same view, error before returning results, return multiple or no rows; this scenario gives no row/recipient linkage. Request scoped tenant/result correlation and separate authorized downstream access/delivery proof if available. Nima/Liora should review any public data-impact claim before Rowan dispatches it. Keep message **unsent** until authorized.

### Whole-exercise rubric (0–20)

Two independent evaluators score only **frozen source-backed** artifacts. For each: **0 = absent/contradicted**, **1 = a relevant but incomplete scope, authority, clock, evidence or limit**, **2 = reproducible and correctly bounded answer**. Sum **ten × two = 20**. If a facilitator omits a needed inject, mark the dependent criterion **not observed / exercise-conduct defect**, not student failure. Preserve first decisions and disputes; later corrections receive a new card/decision ID. Classroom score is **not** NIST or OWASP certification.

| Criterion | Full two-point standard |
|---|---|
| **C1 event interpretation** | Change-control defect, syntax errors, abnormal reads and injection hypotheses distinguished |
| **C2 clock/denominator integrity** | WC release/freeze chronology, 1%/26%/1.2%, 300/1,800/320 and source windows correct |
| **C3 evidence custody** | Requested vs acquired vs readback, source coverage, no sensitive dump or active probe |
| **C4 data-owner limitation** | Nima's tenant/class rules, unique affected-record number **unknown**, no inferred exfil or legal verdict |
| **C5 feature-flag containment** | Exact route-only owner approval, operator and independent flag/profile readback |
| **C6 DB privilege** | Extra case-note metadata read grant recognized but not assumed used; least privilege tested |
| **C7 secure-query mechanism** | Reviewed parameter binding plus independent tenant access control and invalid input negative test |
| **C8 recovery no-go** | WC-07 failing cross-tenant negative test blocks first fix despite other green outcomes |
| **C9 production acceptance** | WC-08 isolated pass distinct from WC-09 released app/DB/flag/test/monitored audit receipts |
| **C10 communication and learning** | Data-impact uncertainty, approved/unsent notice, concrete owners, negative tests and deadlines |

**Noncompensable process stops:** attempting live production exploitation, unauthorized DB reads/dumps, exposing real customer data, bypassing Nima's impact review, restoring FIX-Q-1 after its failed tenant test, unsanctioned production edits or inventing a record count/breach finding. Stop the exercise, record **critical control failure**, and refer actual emergency actions to the application's authorized incident/change owners. The classroom-only interpretation is **17–20** strong, **12–16** material gaps, **0–11** substantial rework, always with independent reviewer dissent and skipped-card limitations. A strong score does not prove a real portal secure.

**Score calibration:** If a participant at WC-07 says “parameterized queries passed, ship FIX-Q-1,” observer Ellis awards **C8=0** because the foreign-tenant negative test **failed**, even if a second observer initially suggests 1 for technical effort. Preserve the unsuccessful decision and the later WC-08 evidence as a **new** version; no retroactive upgrade. If a learner claims 1,800 exposed customers, **C4=0** for a directly unsupported record count rather than partial credit for mentioning DB logs.

## 11. Communication, debrief and measurable improvement

**Fictional unsent operational draft**, for Ishan, Nima, Maren, Liora and Rowan to review before any distribution:

> “We are investigating an issue in the customer-search function following a software change that was not recorded in the normal approval process. We temporarily disabled that search path while retaining other verified portal functions, and reviewed application and database evidence. A revised search function has passed defined query and authorization checks and a monitored, limited service return is being assessed. Existing records do not yet establish how many customer records, if any, were accessed beyond authorization. We will communicate verified updates through approved channels as the data-impact assessment continues.”

A draft is **not** a sent notice. Rowan tracks `drafted / reviewed / approved / sent / acknowledged` separately. Do not imply a confirmed breach, a verified attacker, universal clean state or legally fixed notice duty. Any external communication in a real case depends on applicable law, contracts and facts assessed by Nima/Liora.

**25-minute debrief:** What source proves the unreviewed search change? What distinguishes malformed DB commands from successful injection? Which metric was a *query count* versus row/record count? Why did /account-view remain available while search degraded? Did the team preserve original app+DB source windows before changes? Who authorized FLAG-SEARCH-9? Which receipt demonstrates applied scope? What did the excess DB grant mean, and which source would show its actual use? Why was FIX-Q-1 unacceptable even with normal search and invalid input tests passing? What did FIX-Q-2 add in authorization and least privilege? Which independent production receipts and log windows support a **limited** recovery? What facts remain unknown for data impact and notification?

| Improvement ID | Fictional owner and target after exercise | Independently falsifiable rehearsal |
|---|---|---|
| **I-01 reviewed predeployment query gates** | Rhea + Tova / 21 days | In a nonproduction fixture, reject an unreviewed query-builder diff and malformed-format handling error before release; preserve reviewer receipt |
| **I-02 row/tenant authorization negatives** | Nima + Tova / 28 days | Safe mock users across two tenants; permitted search passes and unrelated tenant fixture is denied under approved tests |
| **I-03 DB least-privilege owner review** | Bogdan + Leandro / 21 days | Versioned DB role diff removes case-note read, verifies permitted view, denies unrelated metadata query in isolated fixture |
| **I-04 reliable app/DB trace preservation** | Althea + Maren / 30 days | Synthetic incident retains correlated trace/request ID, app/DB clocks, hash readback and source gaps without copying customer contents |
| **I-05 feature-flag reversibility and unaffected service** | Mirael + Ishan + Dustin / 14 days | Exercise search-only disable/enable with independent state/route readback, profile path and customer fallback checks |
| **I-06 evidence-based data impact checklist** | Nima + Liora / 30 days | Compare two synthetic cases: large query counts with missing row/recipient evidence vs verified unauthorized cross-tenant result; reviewers do not invent a record count |
| **I-07 accurate incident communications** | Rowan + Vesper / 14 days | Reject two unsupported drafts (“all data safe” / “mass breach confirmed”) and approve a source-limited update with review/dispatch receipts |

Dates are **synthetic pedagogical targets**, not legal/NIST requirements or completed remediation. The **tabletop** completes when A1–A6, five independent exercises and their worked answers, rubric and after-action ownership are recorded. Its **fictional search-service restoration** can be conditionally accepted while historic data impact remains unresolved. No real incident, academic accreditation, compliance attestation or security guarantee is claimed.

## 12. Primary references and rights

1. [NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management (April 2025, final)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — CSF-integrated incident governance and response, not a prescribed query forensic checklist.
2. [NIST CSWP 29 — Cybersecurity Framework 2.0 (February 2024)](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) — nonprescriptive outcome and six Functions.
3. [OWASP ASVS v5.0.0 stable release](https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release) — original OWASP authored verification criteria; includes `v5.0.0-1.2.4` query protection. The ASVS authors' CC BY-SA license remains theirs and is not relicensed by this work.
4. [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — parameterized queries, safe APIs and least-privilege DB grants.
5. [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — enforce authorization for every request and authenticated resource.
6. [NIST SP 800-92, Guide to Computer Security Log Management (September 2006, final)](https://csrc.nist.gov/pubs/sp/800/92/final) — historical primary guidance on enterprise log-management sources and retention; not a complete modern forensic procedure.
7. [NIST SP 800-86, Guide to Integrating Forensic Techniques into Incident Response (August 2006, final)](https://csrc.nist.gov/pubs/sp/800/86/final) — historical source/custody reasoning; not a basis for unauthorized production testing or customer-data collection.

All names, services, markers, counters, permissions, traces, mock tests, decision gates and answers are **original fictional instructional content**. No third-party textual material, code, malicious payload, real customer identifier or proprietary dataset is reproduced. External primary works retain their own rights. The author's original OpenCyber Academy contributions follow [RIGHTS.md](../../../RIGHTS.md), including CC0 scope and exceptions. This is **not** a genuine compromise finding, breach conclusion, NIST/OWASP certification, legal advice or deployment instruction.
