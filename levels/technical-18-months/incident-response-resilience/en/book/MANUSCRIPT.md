# Incident Response and Cyber Resilience: Technical Foundations and Lab Practice

- Language: English (`en`); technical course, up to 18 months; approximately 1,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–8 of 18, EX001–EX032 and their worked results are authored. Ten chapters, substantial expansion, source review, technical and accessibility review, and the 300-page A4 verification remain open.
- Audience: technical operators learning to model services, interpret evidence and verify controls under supervision. Entry knowledge: basic networking, operating systems, scripting and permitted lab practice.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited standards retain their own rights.
- Educational boundary: every system, account, log and address in the Lumen Library Reservations case is synthetic. This book grants no access or change authority for a real environment.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read chapters 1–8 in order. Each chapter is one curricular subject and begins with a technical model, then tests it against a reproducible **offline** fixture. Before reading the worked result, write the artifact requested by an exercise and explain which observation would falsify your conclusion. The remaining ten chapter positions have summaries in the [book plan](PLAN.md); those summaries are **not authored lessons**. The finished technical course targets 72 exercises, at least 50 of which must be substantive and worked in the book, plus a verified minimum of 300 A4 pages.

The case is **Lumen Library Reservations (LLR)**, an invented reservation service. It is separate from the professional book's Cedar Training Network case. Documentation-only names and addresses follow [RFC 6761's `.test` reservation](https://www.rfc-editor.org/rfc/rfc6761.html) and [RFC 5737's TEST-NET blocks](https://www.rfc-editor.org/rfc/rfc5737.html). Do not query these names or addresses on a network; the fixtures below are sufficient. Sources support protocol and response concepts, **not** the fictional LLR observations.

## Contents

1. [Computing and service architecture](#ch-01) — dependency and trust-boundary model with a testable failure-domain lab.
2. [Networks and protocols](#ch-02) — read a synthetic DNS/TCP/TLS/HTTP chain without inferring a cause from one status code.
3. [Operating systems and identities](#ch-03) — distinguish process, principal, session and human with bounded records.
4. [Scripting and data formats](#ch-04) — validate a synthetic CSV bundle without losing rejected records.
5. [Security scope and evidence](#ch-05) — keep authority, original bytes and provenance separate.
6. [Response system models and service dependencies](#ch-06) — compare route-level impact and reversible options.
7. [Event-source mapping and log retention](#ch-07) — choose a source and prioritize time-bound requests.
8. [Identity, host and network failure modes](#ch-08) — discriminate competing explanations with bounded clocks and sources.
9–18. [Planned technical subjects](PLAN.md#ch-09) — collection, controlled changes, recovery and final integration; teaching remains to be written.

The worked-results appendix contains EX001–EX032, four per authored chapter. Section numbers in the manuscript are teaching sections; the course's subject index is the authoritative chapter list.

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes and connection

The learner will draw a service dependency graph, separate a **data path** from a **control path**, identify trust boundaries and use the model to predict which decisions are at risk when a component fails. At technical depth, a diagram must be falsifiable: every arrow needs a producing system, an expected behavior, an owner and a testable observation. The graph will guide Chapter 2's network-source choices and Chapter 3's identity analysis. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places response within organizational cybersecurity risk management; the particular LLR graph is an original lab model.

### 1.1 Model the service outcome first

LLR's user outcome is “an authorized patron can see an available study room and reserve it without losing an existing reservation.” That statement is more useful for incident response than “the portal is online.” The portal may render a page while the write path is broken; a backup job may succeed while the restored data would overwrite newer reservations. Separate **availability** (can a request be served?), **correctness** (is the returned reservation state right?), **authorization** (does the requesting principal have the required right?) and **auditability** (can an owner reconstruct the change?). A healthy front page alone proves none of the other three.

The invented components are: `edge`, a gateway that receives browser requests; `api`, the reservation application; `idp`, an identity service; `db`, the authoritative reservation store; `worker`, an approved reminder/synchronization job; and `backup`, a service that takes versioned copies of `db`. Treat the names as roles, not hostnames. The dependency rule is “A depends on B if B's failure **can** prevent A from meeting its stated outcome.” This conservative relation does not mean every B failure will always cause an A outage: caches, fallbacks and degraded modes may exist. A field test must check them.

| Consumer | Needed producer(s) for this lab | Owner to ask | What a failure could impair |
|---|---|---|---|
| `edge` | `api` | Gateway owner | Visible search/reservation response; edge health may still be green. |
| `api` | `idp`, `db` | Application and identity owners | Authorization decision and authoritative reservation state. |
| `worker` | `idp`, `db` | Job owner | Scheduled processing; it may retry after a restart. |
| `backup` | `db` | Recovery owner | New recoverable copies, but not necessarily the current user-facing path. |
| `idp`, `db` | none *in this simplified graph* | Their respective custodians | Their own dependencies are deliberately omitted and must be discovered before real use. |

An arrow `edge → api` says the edge depends on the API. A **failure domain** is the set of components a failure might affect under the graph. A **blast-radius hypothesis** predicts this domain before testing; it is not a measured impact count. If `idp` becomes unavailable, `api` and `worker` may fail authentication-dependent functions, and `edge` may surface their API failure. `backup` is not downstream of `idp` in this graph. If `db` fails, `api`, `worker`, `backup` and then `edge` may be affected. These conclusions depend on the *assumed* arrows. A service owner might show that `api` can serve read-only cached pages while writes fail, which would refine the graph rather than invalidate the method.

### 1.2 Separate the planes and boundaries

The **request/data path** is browser → edge → api → db, with an authorization check through idp. The **scheduled path** is worker → idp/db, and may issue API requests through a route the diagram has not yet shown. The **control path** comprises configuration, credentials, deployment permissions and backup/restore approvals. A responder considering an emergency change should map both: disabling one `idp` principal could stop an unwanted session **and** the approved worker. Restoring a whole `db` snapshot could put the portal back online while discarding later legitimate reservations. “Small change” is about **scope and dependencies**, not just the number of commands.

Mark a trust boundary whenever authority, ownership or data handling changes: browser to edge, edge to api, api/worker to idp, application to db, and production db to backup copy. For each crossing ask: which principal is asserted, how does the receiver verify it, what record is generated, how long is that record retained, and who can retrieve it? Do not assume TLS alone supplies the application principal: it protects a transport channel according to its configuration, while application authorization and audit are separate checks. Chapter 2 will distinguish those observations precisely.

A **source of truth** is an owner-designated record for a particular decision at a particular time, not a magic system that answers all questions. `db` may be authoritative for stored reservation values, `idp` for session status and the change ledger for approval scope. A browser screenshot is an observation of a displayed page. A backup digest checks byte identity of a given copy, not whether the copy has the latest accepted business state. In a case record, write which question each source can answer and one limitation.

### 1.3 Worked example: a two-component alert

Suppose LLR receives a fictional 12:04 alert: the edge reports HTTP errors and the worker's last run did not finish. It is tempting to name an “edge attack.” The graph says `api`, `idp` and `db` are shared upstream explanations for some combination of these symptoms; the edge itself may be healthy. The two symptoms also could be unrelated. The technical response is to request **read-only, owner-approved** status for the API, identity dependency and database, using a bounded time window. The responder should not restart or disable anything from this alert alone. A second observation might show edge-to-API timeout while worker reached `db` normally, which would narrow the failure domain. A green edge health probe would not settle a failing reservation function if it tests only a static page.

Record the model as a hypothesis ledger: `observed = edge errors and worker unfinished`; `inferred = shared dependency possible`; `discriminators = API request trace, idp availability, db read status, worker error class`; `authority = owners for each read`; `action = no production change yet`. This prevents a diagram from becoming a story that is treated as fact.

### 1.4 Offline lab: compute a conservative dependency closure

Use Python 3 with this literal fixture. It reads no files or network resources and changes no system setting. The direction of each set is **consumer → producers**. `downstream(failed)` finds consumers whose required producer is in the accumulated affected set. Its output is a **potential-impact set under the lab graph**, not a measured outage.

```python
dependencies = {
    "edge": {"api"},
    "api": {"idp", "db"},
    "worker": {"idp", "db"},
    "backup": {"db"},
    "idp": set(),
    "db": set(),
}

def downstream(failed):
    affected = {failed}
    while True:
        new = {name for name, producers in dependencies.items()
               if name not in affected and producers & affected}
        if not new:
            return sorted(affected - {failed})
        affected |= new

print("idp:", downstream("idp"))
print("db:", downstream("db"))
```

The expected first line is `idp: ['api', 'edge', 'worker']`; the second is `db: ['api', 'backup', 'edge', 'worker']`. Verify by tracing arrows by hand. A **negative control** is to remove the `edge` dependency on `api` in a copy of the fixture and observe that `edge` disappears from both closures. That is not proof the real edge is independent; it demonstrates that conclusions are sensitive to an assumed arrow. Restore the original literal fixture after the test. In a real environment, validate each arrow with the owner and a permitted service test before using this graph to authorize containment.

### 1.5 Failure and rollback evidence

Before any response change, compare three questions: what harm might the current condition cause; what dependencies would the proposed change interrupt; and what observable result would justify keeping or rolling back the change? In LLR, revoking the shared worker principal might stop a suspected unauthorized job, but it can also halt legitimate reminders and reservation synchronization. The response lead can **propose** the action; identity and service owners must decide the exact principal, duration, alternative and rollback; an authorized operator executes; an observer checks both abuse path and legitimate worker function. The lab deliberately performs none of those steps. A paper plan must leave approval and execution blank until real receipts exist.

### Common errors and limits

- Reversing arrow direction and claiming the producer depends on its consumer. Write the dependency convention beside the graph.
- Treating a conservative closure as an incident impact count. It lists possibilities under assumptions, not observed failures.
- Treating “gateway healthy” as “reservations work.” Probe the user outcome and the write path separately in an approved test.
- Using a backup copy as the whole-business restore target without comparing current legitimate data.
- Inferring one human actor from a service-account name; Chapter 3 will show why this is unsafe.

### Exercises — subject 1

**EX001 — Service map.** Objective: identify decisions supported by each component. Inputs: the six LLR components and the table in §1.1. In a local Markdown table, list consumer, producer, owner, one decision source and one unverified assumption for all six. No system access is needed. Evidence: a map another learner can read without guessing arrow direction. Rubric: 2 = all six, direction and limits correct; 1 = map present but one owner/assumption vague; 0 = no testable map.

**EX002 — Failure closures.** Objective: reason through propagation. Input: the literal Python fixture in §1.4. Run it offline or trace it by hand; record exact sorted outputs for `idp` and `db`, then remove `edge → api` in a copy and state which output members change. Evidence: original and control outputs with a sentence about what closure does *not* prove. Rubric: 2 = both exact outputs and correct negative control; 1 = one correct closure; 0 = reversed edges or claimed measured outage.

**EX003 — Trust-boundary worksheet.** Objective: choose minimally sufficient evidence. Inputs: browser, edge, API, IdP, DB and backup roles. For three distinct crossings, name asserted principal, receiving check, expected record, custodian and one missing/untested field. Use only fictional names. Evidence: three-row worksheet. Rubric: 2 = transport and application authority separated with testable gaps; 1 = boundaries named without field/owner; 0 = “TLS proves the user” or invented collected logs.

**EX004 — Change-risk review.** Objective: preserve business function during a proposed control. Input: the hypothetical shared worker principal at §1.5. Write a 120–180-word request comparing targeted job pause with principal revocation: harm avoided, service risk, approving roles, expiry, positive/negative verification, rollback owner. Mark all actions proposed. Evidence: paper approval request. Rubric: 2 = both options, distinct rights and checks; 1 = risk named without rollback/test; 0 = claims a real action was performed.

### Subject synthesis

A response begins with a service and a falsifiable graph, not an alert label. The offline closure shows what the **model predicts**; the owner and source checks determine what actually happened. Chapter 2 adds protocol and network evidence so a responder can distinguish a broken path from a guessed cause.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes and connection

The learner will trace a reservation request across name lookup, transport, TLS and HTTP, say exactly what each observation establishes, and choose a bounded next evidence source. Chapter 1 supplied the components and trust boundaries; Chapter 2 tests whether a network record can identify the failing **segment** without overclaiming the responsible system or actor. Chapter 3 will add host processes and identity records. The protocol descriptions use [RFC 9110 for HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html) and [RFC 8446 for TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html); LLR's trace and thresholds are invented.

### 2.1 Five questions in one request path

When a user says “the portal failed,” ask five distinct questions. **Name resolution:** what address did the client's resolver report and when? **Reachability:** was a transport connection established to that address? **Protected channel:** did a TLS handshake complete with the intended peer under the local trust policy? **Application request:** what method, target, request ID and response did the edge observe? **Upstream work:** did the API and database actually process the same request? A “yes” to an earlier question does not answer the later ones. A DNS answer can be cached, a TCP handshake can succeed while application data fails, a TLS handshake can complete while the HTTP service returns an error, and a gateway can return a page while an upstream write has failed.

For this **offline fixture**, `portal.example.test` is a synthetic label, not a live DNS name. RFC 6761 notes that `.test` names are special-use and may resolve differently across networks, so the exercise supplies a **fabricated DNS result** and instructs no lookup. `192.0.2.10` and `198.51.100.20` come from RFC 5737 documentation blocks. A real network capture requires organizational permission and privacy review, because addresses, headers and payloads can be sensitive even if the analyst only wants a status code. This chapter uses a short written trace instead.

TLS 1.3 is designed to protect client-server communication against eavesdropping, tampering and message forgery when correctly deployed. It does **not** prove that an application's logged user was entitled to reserve a room or that a specific human pressed a button. Conversely, seeing a TLS handshake in an edge log without an independently linked API request does not prove that the API received it. Keep **transport identity**, **application principal** and **human attribution** as separate fields. In the lab, the edge sees a request ID that the API log does not show in the supplied sample; absence from a sample is not proof of absence from the whole system.

### 2.2 Synthetic trace with event and collection times

All rows below are **fictional observations**, supplied together at exercise time 12:06 UTC. Event times are source-reported UTC. The limited API log sample covers 12:00:00–12:00:10 and may be incomplete; no packet payload is provided. The `trace` column contains only classroom labels.

| ID | Event UTC | Producer and supplied observation | Supported claim | Open question |
|---|---|---|---|---|
| N01 | 12:00:00 | Client-side resolver record: `portal.example.test → 198.51.100.20`, TTL 60 s. | One resolver supplied that answer in this fixture. | Was the browser using this resolver/cache? |
| N02 | 12:00:01 | Edge connection summary: client `192.0.2.10` completed TCP connection to `198.51.100.20:443`. | This client-to-edge transport connection completed. | What happened after connection? |
| N03 | 12:00:02 | Edge reports TLS 1.3 handshake completed for the connection. | The edge reports a completed protected channel. | Which certificate/policy checks did the client apply? |
| N04 | 12:00:03 | Edge reports `GET /rooms`, `request_id=r-201`, HTTP **503**, `upstream_timeout=true`. | The edge returned a server-side failure for this request and labelled an upstream timeout. | Which upstream dependency was slow or unreachable? |
| N05 | sample 12:00:00–12:00:10 | Supplied API log sample has **no** `r-201` row. | The supplied sample contains no matching row. | Is logging complete, and does the edge preserve IDs across hops? |
| N06 | 12:03:00 | Edge static `/health` request `r-209` returned HTTP **200**. | That edge health endpoint responded successfully later. | Does it test the reservation API or database? Not stated. |

The trace narrows one segment: the client reached an edge that performed TLS and generated an HTTP response. A **DNS failure for this particular recorded connection** is inconsistent with N02/N03, though N01 alone would not prove browser resolution. N04's 503 means the request did not obtain the expected successful resource response; per RFC 9110, a status code describes the response semantics, not the complete root-cause chain. The edge's `upstream_timeout=true` is a **producer claim** to investigate, not independently corroborated evidence that `api` failed. N05 might result from an API reachability problem, dropped or transformed request ID, log delay, short sample window or incomplete logging. N06's static health check cannot certify `/rooms` or writes. Do not classify this as an attack solely because an alert fired.

### 2.3 Choose a capture point by decision value

If the immediate decision is whether to restart the API, the lowest-risk discriminator is often an owner-approved comparison of **edge upstream metrics and API request/access logs** for `r-201` and adjacent requests, including the log pipeline's coverage and time basis. Ask for a narrow 12:00:00–12:00:10 UTC window and the ID semantics: does the edge pass `r-201` unchanged? If it does, a validated API log with no matching receipt can strengthen a path-to-API hypothesis; if it generates a new upstream ID, the absence of `r-201` is expected and a mapping record is needed. A second bounded check of API-to-database health may be necessary if the API did receive and time out. Only owners can approve those records or any restart.

A packet summary from the client-to-edge link answers **transport** questions but may add little about the edge-to-API failure. A broad packet capture can create privacy and storage costs without supplying a join key. Prefer the source that can change the decision with the least collection. Record producer, time window, query, custodian, retention, permission, expected discriminator and what a negative result would mean. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) provides a high-level log-management foundation; its 2006 technical specifics are not a modern vendor recipe.

### 2.4 Offline lab: classify the supplied chain

Copy the six rows into a local Markdown file or use the exact dictionary below in Python 3. The script has no imports, files or network calls. It computes only **which stages have a supplied positive observation** and prints an interpretation boundary. Do not rewrite `api_seen=False` as “the API received nothing”; it means the *supplied sample* lacks a row.

```python
trace = {"dns_answer": True, "tcp_to_edge": True,
         "tls_at_edge": True, "edge_http_status": 503,
         "api_sample_has_r201": False, "static_health_status": 200}
print("client-to-edge:", "observed" if trace["tcp_to_edge"] and trace["tls_at_edge"] else "not established")
print("rooms request:", trace["edge_http_status"])
print("API sample contains r-201:", trace["api_sample_has_r201"])
print("static health proves rooms success:", False)
```

Expected output is `client-to-edge: observed`, `rooms request: 503`, `API sample contains r-201: False`, `static health proves rooms success: False` on four lines. The negative control is to change `tcp_to_edge` to `False` in a **copy** of the dictionary and observe `client-to-edge: not established`; that changed fixture cannot be used to reinterpret N02. A technical report should carry the original and variant labels separately, just as incident cards have provenance. The code deliberately does not guess whether the API, database, network or logger caused the 503.

### 2.5 Time and failure-domain caution

The rows are ordered by source-reported event time, but no clock accuracy measurements are supplied. N01's TTL is a DNS cache parameter, **not** a guaranteed time during which the browser used that answer. N05's sample window brackets 12:00:03, but an async log could arrive after the interval. N06 is nearly three minutes later and tests a different endpoint. A real comparison would retain event time, collection time, source clock, interval boundaries and known lag. Chapter 3's host and identity records will add another set of time bases; they must be normalized before a causal timeline is asserted.

### Common errors and limits

- Calling a completed TLS handshake proof that application authorization succeeded. Transport and application rights are separate.
- Treating an edge 503 as proof that the API process crashed. The edge's label and the absent sampled API row need corroboration.
- Using a static 200 health response to close a reservation incident. Test the affected function under approval.
- Turning a log sample's missing row into “nothing happened.” State the sample coverage and pipeline lag first.
- Running a live DNS query or packet capture against invented addresses when the supplied offline data answers the lesson.

### Exercises — subject 2

**EX005 — Claim ladder.** Objective: avoid cross-layer inference. Inputs: N01–N06. In a six-row Markdown table, give one supported claim and one unproven claim per row. Highlight the first stage where the expected `/rooms` outcome fails. Evidence: table with row IDs. Rubric: 2 = all six and correct boundary at N04; 1 = trace mostly right with one overclaim; 0 = labels TLS or N06 as reservation success.

**EX006 — Bounded evidence request.** Objective: pick a discriminator. Input: N04/N05 and the Chapter 1 graph. Write a read-only request to the edge/API custodians for a 12:00:00–12:00:10 UTC interval, exact ID semantics, expected fields, permission, retention and two possible outcomes. Evidence: request record, not a claim of collection. Rubric: 2 = scope, owner and both interpretations; 1 = useful source but unbounded or no negative-case meaning; 0 = unauthorized capture/restart.

**EX007 — Offline classifier.** Objective: reproduce and challenge a tool result. Run §2.4's code or reason by inspection. Give the four exact output lines, then change only `tcp_to_edge` in a copy and report the changed first line and why that variant cannot negate N02. Evidence: original/variant transcript. Rubric: 2 = exact output and source separation; 1 = output without limitation; 0 = claims a root cause from the printout.

**EX008 — Clock and symptom note.** Objective: make a cautious handoff. Inputs: N01 12:00:00 with TTL 60, N04 12:00:03 and N06 12:03:00. Write 110–160 words with observation, inference, uncertainty and next owner. Explain why the TTL and static health response do not determine the 12:00 `/rooms` outcome. Evidence: handoff note. Rubric: 2 = time bases and endpoint difference explicit; 1 = diagnosis plausible but timing vague; 0 = declares DNS compromised or service recovered.

### Subject synthesis

The trace tells us **where an observed request got**, not who caused a failure. By preserving layer, source and time, the responder can request a narrower discriminator than “collect all traffic.” Chapter 3 adds process and identity evidence, where a matching account name can be as misleading as a matching timestamp.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — chapter 02 of 18

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes and connection

The learner will distinguish a **host process**, an **operating-system account**, an **identity principal**, a **session** and a **human**; reconstruct only supported joins across host, IdP and application records; and specify a safe collection request when a join key is missing. Chapter 2 left the API-path explanation open. This chapter asks whether identity and host records narrow an observed reservation change without turning a service account into a person. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) informs coordinated response, while [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) provides forensic vocabulary from 2006; current OS/vendor collection details require separate verification.

### 3.1 Name the layers before joining them

A **process** is an executing program instance in a host namespace, identified locally by fields such as PID, start time and executable path. A PID can be reused after exit and is meaningless without host and time. An **OS account** supplies local privilege context for a process, but a daemon's account is not necessarily the user who initiated a request. An **identity principal** is an entity represented to an IdP or application; it may be a human, service or workload identity. A **session** is a particular authenticated context with an identifier and lifetime; a service principal can have many sessions. A **human actor** is a person whose actions require independent attribution evidence. These categories overlap but are not interchangeable.

An application may log a principal label but omit the session ID. A host may log a process owned by a service account but omit the IdP token used on an outbound request. Nearby timestamps and the same account string make a **hypothesis**, not a cryptographic or semantic join. To claim a direct join, ask the producer whether two records share an identifier with the same meaning and whether the logs cover the relevant route. A shared identity can be used by a legitimate scheduler and an emergency operator; a label alone cannot distinguish them. Blank `actor` means the producer did not provide a value, not that an anonymous attacker has been identified.

The response decision also has a service dependency. In the Chapter 1 graph, the `worker` and `api` both depend on `idp`; a broad principal disablement could stop approved scheduled work. A scoped read-only request for status and source coverage is safer than an unsupervised account action. A later containment proposal must include target session/principal, approving roles, expected legitimate service effect, verification and rollback. This chapter performs only a paper and offline analysis.

### 3.2 Synthetic host/identity/application bundle

The following records are **fictional LLR data**. They are supplied as snippets, not certified complete exports. All event times are source-reported UTC; the custodian has not supplied clock-offset measurements or original-object digests. No record contains personal information.

| ID | Source event | Supplied record | What it supports | Missing for a stronger claim |
|---|---|---|---|---|
| I01 | 11:58:00 | IdP reports `principal=svc-reserve`, `session=sid-88`, `client=runner-02`, outcome `success`. | A sign-in for that principal/session/client in the sampled IdP record. | Token binding to a specific API request; person behind it. |
| H01 | 11:58:04 | Host `runner-02` reports process PID 420, start 11:58:04, executable `/opt/llr/worker`, OS user `svc-reserve`. | A process with that name and local privilege context existed in the sampled host record. | Whether it used `sid-88`, its code integrity and initiator. |
| A01 | 12:00:03 | API audit reports reservation `R42` changed, `request_id=r-202`, `principal=svc-reserve`, **session field blank**. | The API recorded a change under that principal label. | Direct `sid-88 → r-202` key, approval scope and human attribution. |
| I02 | 12:00:04 | IdP reports denied `session=sid-89` for `svc-reserve` from `runner-02`. | A separate denied attempt in the sampled identity record. | Whether it is related to A01; a denial does not undo an earlier success. |
| CH01 | 11:50 | Change calendar lists approved worker job for reservations `R40` and `R41` until 12:10. | Those two reservations are in the visible change scope. | Any approved R42 addendum or emergency exception. |

`A01` is not the same request as Chapter 2's `r-201`: its request ID is `r-202`, and this chapter's bundle asks a distinct question about a reservation **change**, not the earlier `/rooms` 503. Both may belong to the same synthetic service, but no supplied producer links them. `CH01` shows that R42 lies outside the **visible** approval record, not that a person acted maliciously. The next bounded request should ask the application owner whether `r-202` carried an IdP session/actor mapping in a restricted server-side source and ask the change owner whether a valid R42 addendum exists. A trustworthy negative response requires coverage and version information, not just a search screenshot.

### 3.3 A timeline with uncertainty and hypothesis branches

At 11:58:00, I01 reports an IdP success. Four seconds later, H01 reports a process start on the named runner. At 12:00:03 A01 reports a change; one second later I02 reports a denied attempt. Because source clocks and collection paths are not verified, do **not** infer a four-second causal chain or treat I02 as proof that the A01 request failed. Three hypotheses remain plausible in the supplied evidence: **H1**, the approved worker was misconfigured to touch R42; **H2**, an unapproved operator or different task used the shared principal; **H3**, a change/addendum record is missing from the supplied calendar. A fourth option is an API audit error. Each has a falsifiable discriminator: a complete signed job manifest and request-ID map for H1; approved operator/session-to-request records for H2; versioned change ledger for H3; and an authoritative R42 state/audit reconciliation for the logging-error option. The provided snippets do not settle any branch.

At this point a technical analyst should preserve the snippets and request narrow source metadata: source object ID, producer, query, interval, collector, time basis, field definitions and digest of the *copy actually received*. A digest helps detect byte changes between copies; it does not prove completeness, correct collection or truth. If identity logs expire sooner than the calendar, prioritize a permitted preservation request with an owner and time limit, but do not silently expand it to all staff sign-ins. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) discusses log-management processes at a high level; real retention and access must be confirmed with the actual system owners.

### 3.4 Worked join audit

Draw four nodes: `I01/sid-88`, `H01/runner-02:PID420`, `A01/r-202`, `CH01/R40-R41`. `I01` and `H01` share a client/host **label** `runner-02`, but no session ID in H01. `I01` and `A01` share principal label `svc-reserve`, but A01 lacks a session ID. `A01` and `CH01` refer to different reservation sets, so CH01 is evidence of an approval-scope tension. The graph has **dotted candidate edges**, not validated direct joins. Do not turn the dotted I01–A01 edge into a solid arrow because the times are close. An extra record keyed by `r-202` and a producer-validated `sid-88` mapping could change that conclusion; so could an approved R42 addendum. Until then, the claim is “an R42 change was recorded under a shared principal outside the visible change scope.”

**Offline check:** paste the dictionary into Python 3 or reason about it on paper. It has no environment access. A blank value is deliberately represented as an empty string. The code tests only whether a **literal matching session key exists**; it cannot validate source semantics.

```python
idp = {"principal": "svc-reserve", "session": "sid-88", "client": "runner-02"}
api = {"principal": "svc-reserve", "session": "", "request": "r-202"}
same_principal = idp["principal"] == api["principal"]
direct_session_join = bool(api["session"]) and idp["session"] == api["session"]
print("same principal label:", same_principal)
print("direct session join:", direct_session_join)
```

Expected lines: `same principal label: True` and `direct session join: False`. In a **separate synthetic variant**, set `api["session"] = "sid-88"`; the second line becomes `True` as a string comparison. Even that variant would require proof that the two producers use the same session namespace and the copied records are authentic before it supports a case conclusion. Restore the original fixture for the main LLR analysis. The test guards against a common automation bug: treating an empty session field as if it matched any successful session for the same principal.

### 3.5 Safe next actions and verification design

At the current checkpoint, preserve the raw snippets and a derived timeline separately; ask the identity custodian for a scoped session-to-request mapping if one exists and the application/change owners for R42 state and approval scope. The decision record should have explicit fields: `source IDs; request window; custodian; permission; expected field; what a no-result means; collection receipt; remaining uncertainty`. A read-only check must still respect data minimization and access control. If an owner later considers restriction, compare **one session**, **one task** and **whole-principal** options against the Chapter 1 dependency graph. The record needs an expiry, operator, service-health check and rollback owner before approval; this manuscript provides no actual operator procedure or credentials.

Verification should include both security and legitimate-function conditions. For example, if a narrow task pause is approved, a positive check asks whether the task stopped issuing out-of-scope R42 changes; a negative/business check asks whether approved R40/R41 work still functions. A failure to see R42 changes in a short sample is not proof that the path cannot recur; record coverage and next observation. Those checks belong to later containment chapters and a separately authorized lab. Here the learner designs them without touching a service.

### Common errors and limits

- Reading `svc-reserve` as a person's name or an intruder identity. It is a principal label shared by several possible workflows.
- Matching H01 PID 420 to a later process without host and start-time scope. PIDs can be reused.
- Claiming I02's denied attempt negates I01's earlier success or A01's application record.
- Treating a blank A01 session field as a wildcard join or evidence of deliberately hidden identity.
- Treating CH01's missing R42 approval as proof no approval exists anywhere; ask for a versioned, bounded ledger check.

### Exercises — subject 3

**EX009 — Entity separation.** Objective: prevent false attribution. Inputs: I01, H01, A01, I02. Draw a five-column matrix for host process, OS account, IdP principal, session and human, and fill only supported fields. State one identifier needed for each proposed join. Evidence: matrix with empty/unknown cells retained. Rubric: 2 = distinguishes all five and no human attribution; 1 = four categories with one ambiguity; 0 = labels the service account as a person.

**EX010 — Timeline and alternatives.** Objective: preserve time and source limits. Inputs: I01–I02, H01, A01, CH01. Produce four timed event rows plus a separate change-scope row, then H1–H3 with one supporting item and one discriminator each. Evidence: source-linked Markdown. Rubric: 2 = no causal join from proximity and R42 scope tension stated; 1 = useful timeline with weak discriminator; 0 = claims actor or intent.

**EX011 — Join-check lab.** Objective: reproduce a bounded parser inference. Run §3.4's code or calculate its booleans by hand, then run the separate `api["session"]="sid-88"` variant. Report exact two-line outputs for both and the extra producer-semantic check needed before a real direct join. Evidence: original and variant transcript. Rubric: 2 = outputs and source-authenticity caveat; 1 = outputs only; 0 = main case recorded as a direct join.

**EX012 — Collection and control proposal.** Objective: connect evidence request to a reversible choice. Inputs: A01/CH01 and the Chapter 1 graph. Write a 150–200-word plan for a scoped `r-202` mapping request, a versioned R42 approval check, and a **proposed** task-versus-principal restriction comparison. Name custodians, expiry/retention question, approved-change role, positive/negative verification and rollback owner. Evidence: paper request with blank execution fields. Rubric: 2 = exact scope and separate authorization/verification; 1 = plausible but missing one owner or negative check; 0 = directs an unapproved real change.

### Subject synthesis

Host, identity and application records answer different questions. A shared label and close timestamps are starting points for an investigation, not a validated session-to-request edge or a human identity. Chapter 4 adds schema and parser checks so later source comparisons do not quietly discard malformed or ambiguous records.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 18

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes and connection

The learner will read a small CSV log bundle, state a schema before parsing, reject ambiguous rows without deleting them, and produce a deterministic, inspectable summary. Chapter 3 showed why a matching principal label is not an identity join. Chapter 4 asks a prior question: did the transformation preserve the source fields and report its own failures? Chapter 5 will attach authority and provenance to the resulting evidence package. [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180.html) documents a common CSV format, while the [Python CSV library](https://docs.python.org/3/library/csv.html) handles quoting and dictionary rows; neither publication says that a parsed row is authentic incident evidence. All LLR rows here are original fictional teaching data.

### 4.1 A parser is a claim-making instrument

Before writing a script, name the question and the decision it may support. In this chapter the question is: “Which supplied rows are structurally fit for a later request-ID comparison?” The output is **not** a statement about the source system's completeness. A transformation may preserve the original order and still silently drop malformed rows, coerce a missing field into an empty string, or join two records with reused identifiers. Each behavior changes what an analyst might conclude. A good parser therefore has two outputs: accepted records and an explicit rejection report. The rejection report is part of the result, not a pile of errors to hide.

Define a minimum schema for the lab: **event_id** is nonblank and unique within this supplied bundle; **event_utc** is a UTC timestamp with a trailing Z; **source** is one of edge or api; **request_id** and **kind** are nonblank. A unique event ID in one file is still not a cross-system join key. That requires producer semantics and coverage. Decide whether a blank request ID is permitted **before** observing its effect on a favored hypothesis. Here the lab rejects it because the exercise is a request-ID comparison; in another workflow the row might remain useful in a separate, explicitly lower-resolution collection.

The raw input is a byte sequence. The parser's normalized object is a new artifact with its own creation time, version, code and rejected-row count. Do not overwrite the raw bytes. An operator should record the character encoding, line-ending and export mechanism; changing CRLF to LF or reserializing JSON changes the bytes even if the visible fields look similar. The short inline fixture below avoids file I/O, so it cannot demonstrate that a real collection preserved bytes or that its source clock was correct. It demonstrates deterministic logic on an already supplied string.

### 4.2 Worked fixture: two accepted rows and three rejections

This is **branch L4**, a teaching copy unrelated to the main case's verified evidence. Its E1/E2 labels and familiar request IDs are deliberately copied into a new synthetic CSV to test the parser. Do not promote these rows into the Chapter 2 or 3 case record. Line 1 is the header; lines 2–6 are data. The line number in the rejection report is a position in this literal string, not a source-system event number.

~~~csv
event_id,event_utc,source,request_id,kind
E1,2026-10-11T12:00:03Z,edge,r-201,http_503
E2,2026-10-11T12:00:03Z,api,r-202,room_R42_write
E2,2026-10-11T12:00:04Z,api,r-203,room_R40_write
E3,bad-time,edge,r-204,http_200
E4,2026-10-11T12:00:05Z,edge,,http_503
~~~

Run the following code with Python 3 on a local interpreter, or trace it by hand. It uses only the literal in-memory string. The code explicitly detects extra/missing columns, duplicate accepted IDs, invalid times and blank required fields. Its order of checks is part of the lab contract: the second E2 is classified as a duplicate before any other check. For a real log format, build tests for quoted delimiters, embedded newlines, encoding errors, oversized fields and version changes before using a parser operationally.

~~~python
import csv
import io
from datetime import datetime

data = """event_id,event_utc,source,request_id,kind
E1,2026-10-11T12:00:03Z,edge,r-201,http_503
E2,2026-10-11T12:00:03Z,api,r-202,room_R42_write
E2,2026-10-11T12:00:04Z,api,r-203,room_R40_write
E3,bad-time,edge,r-204,http_200
E4,2026-10-11T12:00:05Z,edge,,http_503
"""
required = ["event_id", "event_utc", "source", "request_id", "kind"]
accepted, rejected, seen = [], [], set()
reader = csv.DictReader(io.StringIO(data))
assert reader.fieldnames == required
for line, row in enumerate(reader, start=2):
    if set(row) != set(required) or any(value is None for value in row.values()):
        rejected.append((line, "column_count"))
        continue
    if not row["event_id"] or not row["request_id"] or not row["kind"]:
        rejected.append((line, "missing_required"))
        continue
    if row["event_id"] in seen:
        rejected.append((line, "duplicate_id"))
        continue
    try:
        if not row["event_utc"].endswith("Z"):
            raise ValueError("not UTC Z")
        datetime.fromisoformat(row["event_utc"].replace("Z", "+00:00"))
    except ValueError:
        rejected.append((line, "bad_time"))
        continue
    if row["source"] not in {"edge", "api"}:
        rejected.append((line, "unknown_source"))
        continue
    seen.add(row["event_id"])
    accepted.append(row)
print("accepted_ids:", [row["event_id"] for row in accepted])
print("rejected:", rejected)
~~~

The expected output is **accepted_ids: ['E1', 'E2']** and **rejected: [(4, 'duplicate_id'), (5, 'bad_time'), (6, 'missing_required')]**. This is an exact local result for the fixture, not an assertion that LLR's real API emitted the second line. Record the interpreter version if reproducing the run. A variant with E4's request ID set to r-205 accepts E4 as a third row; that change is a **new input**, so keep both transcripts. Another variant that changes the second E2's event ID to E5 accepts it if all other fields pass. It does not make its R40 change factually approved.

### 4.3 Normalize only with an audit trail

For each accepted row, keep the raw line position, original text or byte offset, parser version, reason for acceptance and normalized fields. The lab returns a Python dictionary so the student can inspect fields; it does not serialize a production evidence store. If you later emit JSON, choose a stable encoding and ordering for reproducibility, and be alert to duplicate JSON member names: many decoders keep a later value without warning. A schema version should tell future readers whether a missing field was absent in the source or introduced by transformation. Preserve unknown fields in a separate quarantine or reject them with a reason; never silently throw them away because they do not fit a favored analysis.

The two accepted rows contain **different** request IDs. Even if E1 and E2 share a timestamp at one-second precision, the normalized table does not join them. To turn them into one transaction, the gateway and API custodians would need to validate an explicit ID mapping or a trusted parent-child relationship plus source coverage. Likewise a parser can say “no accepted API row for r-201 in this five-line fixture,” but it cannot say “the API never received r-201.” The latter would require a complete, validated source over the relevant interval and a known ID scheme. This is the same evidence boundary taught in Chapter 2, now enforced by software.

A technical review should probe negative controls. Change one field at a time: malformed time, duplicate ID, blank request ID, extra column, an accepted row whose source label is outside the allowed set. Predict the rejection reason and compare it with the actual result. A parser that crashes on one bad line can lose later valid lines; a parser that keeps everything without flags can contaminate a join. The failure policy must be chosen for the decision. Here invalid rows remain visible in a rejection list. They should not be “repaired” by guesswork; request a corrected export from its custodian.

### Common errors and limits

- Splitting CSV on commas instead of using a parser. Quoted fields can contain commas or line breaks.
- Normalizing a time string without preserving the original spelling, offset and source clock information.
- Reusing an event ID from a different producer as if it were globally unique.
- Treating clean parse output as an authenticated, complete log export.
- Editing the main case record when running a clearly marked L4 counterfactual.

### Exercises — subject 4

**EX013 — Schema contract.** Objective: make the transformation reviewable. Inputs: the L4 CSV and §4.1. Write a five-row schema table with type, requiredness, accepted values or format, rejection reason and a source-semantic question for each field. State why event_id and request_id have different roles. Evidence: Markdown table. Rubric: 2 = all five fields and distinct identifier scopes; 1 = validation rules without producer questions; 0 = treats event_id as a human or global transaction key.

**EX014 — Parser transcript and variants.** Objective: reproduce a deterministic result. Run §4.2 offline or trace it. Record both exact printed lines, then apply the E4 request-ID variant in a copy and explain the changed accepted/rejected sets. Keep the original transcript. Evidence: two transcripts and a two-sentence limitation. Rubric: 2 = exact line numbers and variant result, with no real-case inference; 1 = counts only; 0 = silently drops rejected rows.

**EX015 — Cross-source join review.** Objective: resist a false match. Inputs: accepted E1/E2, N04/N05 and A01. Produce a four-column claim table: proposed join, supplied support, missing producer semantics and allowed next request. Include an alternative in which the gateway maps r-201 to r-202, marked **hypothetical**. Evidence: table, not an identity attribution. Rubric: 2 = no join from time/label alone and a bounded mapping request; 1 = uncertainty named but no discriminator; 0 = claims E1/E2 prove the same request.

**EX016 — Review a parser failure.** Objective: identify transformation risk. A learner changes the script to discard the rejected list and to replace bad-time with 12:00:00Z. Explain two ways this can change a later timeline, propose a corrected output contract and state who can authorize a source correction. Evidence: short review note with one negative control. Rubric: 2 = preserves raw/rejection provenance and rejects invented timestamps; 1 = mentions bad data without a control; 0 = accepts the invented time as evidence.

### Subject synthesis

A parser is part of the evidence chain. It can make source limits visible or erase them. L4 has two accepted and three rejected rows, yet none is a new main-case observation. Chapter 5 takes that separation into authorization, raw-byte preservation and collection receipts.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — chapter 04 of 18

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes and connection

The learner will distinguish a proposed evidence request from an approved scope, demonstrate byte-level integrity on an offline copy, and write a receipt that lets another operator reconstruct who collected what and when. Chapter 4 produced accepted and rejected rows; Chapter 5 asks whether the **original** and **derived** objects can be traced to a custodian and whether the requested collection was permitted. Chapter 6 will use those limits when comparing response options. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places response actions and records within risk management; [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) describes IT forensic practice and data sources. The latter dates from 2006 and is not a current OS tool recipe or legal opinion. The L5 receipt is an original classroom design.

### 5.1 Authority has fields, not a feeling

“We need the logs” is not a collection scope. A technical request names the case identifier, decision question, source system, object or query, time window, fields, permitted method, privacy limit, collector, authorizer, expiration, storage destination and prohibited expansions. It also identifies the owner who can explain producer semantics. Read permission for an edge snippet does not automatically authorize a tenant-wide identity export, a database copy, a host memory image or a production configuration change. A responder can prepare a narrow proposal while these approvals remain blank.

For this chapter only, branch **AUTH-L5** is an invented classroom approval card: at 12:06 UTC it permits an offline trainee to inspect the literal L4 CSV and a supplied in-memory byte string, with no live systems, no personal data and no external network. It expires at the end of the exercise. That card is **not** a retrospective approval for the Chapter 3 proposal concerning r-202, nor authority for an actual LLR tenant. A separate overbroad request says “export all identity sessions, image runner-02 and restart the API.” The trainee must reject that request: neither the source scope nor the change is covered by AUTH-L5. The appropriate next action would be a bounded new request to the relevant custodians and service owner, not an improvised expansion.

This distinction has technical consequences. If an export command searches too wide a time interval, it may disclose unrelated records and consume the evidence source while the desired short-retention rows expire. If a collector changes a live file's access time or rotates a log, the action can alter the evidence being measured. The answer is not a universal “never touch”; it is a documented, approved method selected for the decision, with known side effects and an alternative if a source is too volatile. The lab below deliberately avoids these operational risks by creating bytes in memory.

### 5.2 Original bytes, derived rows and receipts

Name three objects separately. **Original** is the exact supplied byte sequence. **Working copy** is a copy of those bytes in a controlled workspace. **Derived report** is the parser's accepted/rejected summary, with code and parameters. A SHA-256 digest over bytes can detect a difference between two objects *if* the expected digest itself came from a trusted path; it cannot certify the source system, the collector's authorization, the row semantics, completeness of a query or the absence of an earlier alteration. [Python's hashlib documentation](https://docs.python.org/3/library/hashlib.html) specifies the byte-hashing interface used in the demonstration. The lab's digest comparison is a teaching check, not a certified custody process.

Run this with Python 3. It reads no external file. The content is a deliberately tiny fictional line set; the corrected variant changes one event ID. The expected printed result is given below so a learner can verify the distinction without treating a hexadecimal digest as a magical truth label.

~~~python
from hashlib import sha256

original = b"event_id,event_utc\nE1,2026-10-11T12:00:03Z\n"
working = bytes(original)
altered = original.replace(b"E1", b"E9", 1)
print("original_bytes:", len(original))
print("copy_matches:", sha256(original).digest() == sha256(working).digest())
print("altered_matches:", sha256(original).digest() == sha256(altered).digest())
~~~

The model output is **original_bytes: 43**, **copy_matches: True**, **altered_matches: False**. Verify the byte count locally. The result does not prove that the original bytes came from an edge server; the code constructed them. In a real approved collection, record the source object identifier and retrieval method alongside the digest, then make the independently held original available for authorized review. A digest of a normalized CSV is a different claim from a digest of raw export bytes. Do not compare them and call a mismatch “tampering” when the transformation itself changed line endings or encoding.

A minimal **receipt** for L5 would have: classroom object L5-original; custodian “exercise publisher”; supplied 12:06 UTC; collector “trainee”; AUTH-L5 scope; exact byte count and SHA-256 hex value; method “literal in-memory copy”; working-copy identifier; derived parser version; access restriction; no production claim. A later correction should be an additional receipt with a new version and reason, never a replacement that deletes the first. For a production process, the organization must choose its own retention, chain-of-custody and legal controls; this book does not provide a legal standard.

### 5.3 Worked decision: reject expansion, preserve a useful gap

Suppose the learner wants to explain why the L4 CSV lacks an accepted API row for r-201. Under AUTH-L5, the trainee may inspect only the supplied teaching bytes and record the accepted/rejected counts. The card does not authorize a live API query. The proper handoff distinguishes:

| Statement | Status under AUTH-L5 | Next decision |
|---|---|---|
| The literal copy contains two accepted and three rejected L4 rows. | Reproducible classroom result. | Preserve both raw string and parser transcript. |
| The real API did not receive r-201. | **Unsupported.** | Ask the application custodian for a bounded, approved interval and ID-mapping definition. |
| A full identity export would settle attribution. | **Unsupported and out of scope.** | Request a precise decision question and source/privacy review; an export may still not identify a human. |
| The altered in-memory bytes differ from the original. | Reproducible integrity comparison. | Record which object was altered and why; do not call it a hostile change. |

The table is a technical control on language. A respondent can say “this fixture has no accepted API r-201 row” and cite the parser, but should not say “there is no API evidence.” The latter conflates supplied scope with universe of possible records. A rejected malformed row may be relevant to quality even if unusable for a direct join. Keep it visible in the package.

### 5.4 Reproducibility and limitation checklist

Another trainee should be able to run the same code and compare the same bytes. Supply the original literal data, interpreter version, parser code/version, check order, selected time window, acceptance criteria and expected output. Ask a second trainee to introduce a one-byte variant and verify that the original digest remains unchanged while the variant digest differs. Then ask the harder question: what does that prove about LLR? The correct answer is “nothing about the origin or truth of LLR records beyond the supplied fixture.” A reproducible transformation supports review of a **method**, not independent authentication of a **source**.

### Common errors and limits

- Treating a request for evidence as approval to collect it.
- Hashing only a reserialized report and calling it the source object's digest.
- Assuming equal digests establish source authenticity, authority or completeness.
- Deleting the rejected-row report because it complicates a narrative.
- Expanding a read-only scope into process termination or service restart.

### Exercises — subject 5

**EX017 — Scope gate.** Objective: enforce a written boundary. Inputs: AUTH-L5 and the overbroad request in §5.1. Classify each proposed action (read L4 CSV, compute its digest, export all IdP sessions, image runner-02, restart API) as allowed or not allowed; name a custodian and approval needed for one rejected source request. Evidence: five-row decision table. Rubric: 2 = only the offline actions allowed and no implied production permission; 1 = one scope ambiguity; 0 = performs or recommends an unapproved real action.

**EX018 — Byte-integrity lab.** Objective: reproduce and interpret §5.2. Run or inspect the code, record all three exact output lines, then change E9 to E1 in the variant and state which comparison changes. Explain why equal bytes do not authenticate the source. Evidence: transcript and limitation. Rubric: 2 = exact byte count/booleans and semantic limit; 1 = booleans without source caveat; 0 = calls the original a verified edge export.

**EX019 — Collection receipt.** Objective: make a derived claim traceable. Write a receipt for L5-original and a separate one for L5-altered with object name, origin claim, authority, collector, collection time, byte count or check result, method, digest role, storage/access rule and relationship between versions. Leave any unknown source fields explicitly unknown. Evidence: two Markdown receipts. Rubric: 2 = versioned, distinguish original from variant and avoid false provenance; 1 = hashes only; 0 = rewrites the first receipt as if no change occurred.

**EX020 — Evidence-package review.** Objective: catch a misleading claim. A peer writes “sha256 matched, therefore r-201 never reached API.” Identify at least three separate inference errors and rewrite the conclusion in a source-bounded sentence. Name one approved discriminator and one privacy boundary. Evidence: review note. Rubric: 2 = byte equality, source completeness and ID semantics separated; 1 = generic uncertainty; 0 = retains the unsupported universal claim.

### Subject synthesis

Authority controls what may be collected; provenance controls what may be claimed; a digest controls only a defined byte comparison. A technically clean result can still be outside scope or epistemically weak. Chapter 6 will use these distinctions to model service impact and compare response choices without executing them.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — chapter 05 of 18

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Response system models and service dependencies

### Learning outcomes and connection

The learner will refine the Chapter 1 component graph into route-specific service dependencies, compare containment choices with their legitimate-service costs, and define a recovery target without mistaking a backup timestamp for a safe restore point. Chapters 4 and 5 established that a parsed record and a byte-identical copy still need source semantics and authority. Chapter 6 brings those limits into response design. The method is an original LLR teaching model; [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) supplies the wider risk-management context and [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) supports planning and testing recovery against mission needs.

### 6.1 Component graphs are deliberately conservative

Chapter 1's graph said the API depends on both identity and database. That is a useful first approximation for the **reservation outcome**, but it does not say whether each API function fails under every upstream fault. A technical responder should model **routes and modes**, not merely hosts. Search may be served from a cache during a database outage, while a new reservation write fails. The cache might be stale or disabled, so this mode must be validated with a permitted test and an owner-approved correctness criterion. The graph represents possible dependency, not guaranteed loss of each function.

Branch **L6** is an independent, hypothetical exercise. It does not add observations to N01–N06 or prove a production LLR outage. Its stated assumptions are: the edge and API can serve a limited cached room list without a database call for five minutes; a reservation write checks identity and authoritative database; the worker needs identity and database; a new backup needs database. The five-minute cache assumption is **only** for the lab. It must not be inserted into the main case timeline. The table below states each route's needed components, decision owner and a result that would challenge the assumed path.

| Route | Required in L6 | Owner for a real validation | Challenge to the model |
|---|---|---|---|
| Cached room read | edge, api | Application and gateway owners | A stale or disabled cache gives a different result. |
| Reservation write | edge, api, idp, db | Application, identity and database owners | A fallback authorization or queued write changes the route. |
| Approved worker job | worker, idp, db | Job and identity owners | Job may retry or use a different credential. |
| New backup copy | backup, db | Recovery and database owners | Existing old copies are not this route's outcome. |

This matrix separates “a function might still respond” from “the whole service is correct.” A cached room list can return HTTP 200 while a reservation attempt is rejected or queued. A backup service can have an older copy while **new** backups fail. For any proposed action, name the business outcome to preserve, not just whether a process is up. A negative control is to add db to the cached-read route and compare the affected routes; this exposes the dependence of the answer on an assumption rather than a change in observed evidence.

### 6.2 Offline route-impact model

Run this Python 3 fixture offline. It reads no live status. The program checks whether a failed component appears in a route's **required** set; it does not calculate the probability of an outage, account for graceful degradation or approve any control.

~~~python
routes = {
    "cached_room_read": {"edge", "api"},
    "reservation_write": {"edge", "api", "idp", "db"},
    "approved_worker": {"worker", "idp", "db"},
    "new_backup": {"backup", "db"},
}

def possibly_impaired(failed):
    return sorted(name for name, required in routes.items()
                  if failed in required)

print("idp:", possibly_impaired("idp"))
print("db:", possibly_impaired("db"))
control = {name: set(required) for name, required in routes.items()}
control["cached_room_read"].add("db")
print("db with cache disabled:",
      sorted(name for name, required in control.items() if "db" in required))
~~~

The expected output is **idp: ['approved_worker', 'reservation_write']**, **db: ['approved_worker', 'new_backup', 'reservation_write']**, and **db with cache disabled: ['approved_worker', 'cached_room_read', 'new_backup', 'reservation_write']**. The third line changes only the model. It is not new telemetry. A real test would require the service owner to define success for read, write, audit and retry paths and to authorize the probe. Do not send synthetic requests to a real endpoint.

### 6.3 Choose controls using both positive and negative checks

Suppose a separate fictional incident hypothesis says an unapproved R42-changing task may still be running. A **task-specific pause** could target that task while allowing approved R40/R41 work to continue, but only if a validated task-to-request mapping identifies the target. A **shared-principal revocation** might block a broader path but, from the graph, could also break reservation writes and the worker. A **read-only fallback** could protect current state while sacrificing new reservations. These are **candidate controls**, not actions performed in LLR. Causal language matters: “the task stopped after the hold” does not prove the hold caused it if the task had already finished.

Build a control contract with seven fields: verified trigger, exact target, approving role, operator, duration and expiry, positive check, and negative/business check plus rollback owner. A better contract also records a pre-change baseline, expected source fields, privacy restriction and stop condition. For a task-specific hold, a positive check might be “no further R42 writes on both documented routes over an approved window.” A negative check might be “approved R40/R41 job completes and reservation write audit remains intact.” If route coverage is unknown, the check is incomplete. If the wrong task is selected, the control may disrupt service without reducing the suspected harm.

The **rollback** is not simply “undo the command.” State who restores the task, what version is restored, how credentials and queued work are handled, and what test establishes safe resumption. A missed expiry can turn a temporary containment step into a long outage. Conversely, rolling back before an alternate control is in place can restore a harmful path. Record the decision owner for both keeping and reversing the change. In this book the execution, verification and rollback fields remain **blank** until an explicitly authorized exercise produces receipts.

### 6.4 Recovery point is a business-data question

L6 also supplies a hypothetical backup inventory: the last candidate copy was made at **11:55 UTC**, and an owner-designated reservation ledger has an accepted legitimate write at **11:58 UTC**. At a 12:04 decision, restoring the whole 11:55 copy *might* discard that accepted write. This is a **three-minute data-point gap**, not a measured RPO or proof of loss. Ask the database and service owners whether the copy includes later changes, whether there is a protected journal or replay path, and whether an isolated restore can be checked against the accepted ledger before production use.

Recovery needs at least two gates. A **technical gate** checks provenance, byte integrity, schema, dependencies and route behavior in isolation. A **business gate** checks the owner-approved reservation set, permitted downtime, privacy and sign-off. A snapshot digest can pass the first byte check while failing the business gate. A service can return HTTP 200 while silently losing a reservation. [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) discusses planning, testing and improvement of recovery; the 11:55/11:58 example and gates are original LLR classroom artifacts.

### Common errors and limits

- Reusing a component-level closure as a precise route-level impact report.
- Treating a cached successful read as proof that writes or fresh data are safe.
- Choosing principal revocation before validating which process and session use it.
- Recording a proposed hold as executed, or an executed hold as verified.
- Calling the newest copy a safe restore point without comparing accepted later writes.

### Exercises — subject 6

**EX021 — Route contract.** Objective: refine Chapter 1 without silently replacing it. For L6's four routes, write required components, expected user outcome, owner, one unverified fallback and a negative test. Explain why the component graph remains conservative. Evidence: four-row Markdown table. Rubric: 2 = routes and assumptions distinct; 1 = route map without correctness criterion; 0 = treats a static health probe as reservation success.

**EX022 — Model outputs.** Objective: reproduce §6.2. Run or inspect the code and report the three exact lines. Then explain why adding db to cached_room_read changes the third line but not any observed LLR event. Evidence: transcript and sensitivity note. Rubric: 2 = all sets and model-versus-evidence distinction; 1 = correct sets only; 0 = claims real service impact.

**EX023 — Control comparison.** Objective: make a reversible decision plan. Compare task pause, shared-principal revocation and read-only mode for suspected R42 change: trigger evidence, likely harm avoided, legitimate-service risk, approving roles, positive/negative checks, expiry and rollback owner. Keep execution fields blank. Evidence: control matrix and recommendation conditional on a validated task map. Rubric: 2 = all three options and route coverage; 1 = options but one missing verification dimension; 0 = orders a live change from this fixture.

**EX024 — Restore-point challenge.** Objective: defend business correctness. Inputs: 11:55 candidate copy, 11:58 accepted write, 12:04 decision. Calculate the apparent timestamp gap, give three source questions and two gates before any whole-copy restore. State what remains unknown about journal coverage and RPO. Evidence: restore request. Rubric: 2 = three-minute gap but no data-loss certainty, with technical and business gates; 1 = recognizes older copy but no owner check; 0 = declares safe production restore.

### Subject synthesis

Route-level models expose where a blanket action can hurt legitimate users. L6's predicted impact is conditional on invented route assumptions; no control has been approved or executed. Chapter 7 asks which event sources could verify those assumptions and which records might disappear first.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — chapter 06 of 18

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Event-source mapping and log retention

### Learning outcomes and connection

The learner will map a decision question to producers and fields, distinguish event, ingestion, collection and query time, and prioritize a short-lived source without turning a retention label into a guaranteed deletion deadline. Chapter 6 posed route and control questions; Chapter 7 constructs a request plan that could answer them. Chapter 8 will test how missing or delayed records affect competing failure hypotheses. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) is older, high-level guidance for log-management processes; this chapter's source inventory and clock exercise are original, not prescribed by NIST.

### 7.1 Ask what the source can decide

For a response question such as “Did the API receive r-201?” the candidate sources are not interchangeable. The edge can report that it returned 503 and labelled an upstream timeout. An API access log may show receipt under a different upstream ID. An IdP record can show a session decision but may not include the application request ID. A host process record may show a worker start but not the request it issued. The first step is a **source matrix**: decision question, producer, expected identifying fields, interval, owner, clock basis, collection path, retention anchor and a known gap. A later query result should cite the matrix row that makes it relevant.

The source may fail to answer the question for five different reasons: the event was never emitted; it was emitted but not transported; it arrived late; it was stored but omitted by the query; or it expired or became inaccessible. “No row found” is ambiguous until coverage and ID semantics are tested. A query should use both an in-range positive control and a known out-of-range or absent negative control when permitted. Record the query timestamp and filter. An empty API sample from Chapter 2 cannot settle whether r-201 reached the API, particularly because the gateway may rewrite IDs. Chapter 4's rejected-row report is another coverage limit: a source record may be present but unusable under the selected schema.

The inventory below is **L7**, a separate fictional retention-planning branch. It does not assert that the main case has these retention policies or that any log was exported. Each duration is a classroom assumption with an explicit anchor; the custodian must verify both in an organization. A “10-minute” statement without an anchor is not enough to calculate an expiry. An identity source could retain a detail row from event time, ingestion time or last access, producing different deadlines.

| Source | Decision it might support | Claimed retention and anchor in L7 | Limitation |
|---|---|---|---|
| Identity detail | Whether a stated session was accepted and from which client class. | 10 minutes after event time 11:58:00 UTC. | Session may not map to application request. |
| Edge ring | Whether a gateway saw an upstream attempt and its mapped ID. | 15 minutes after ingestion 12:00:05 UTC. | Gateway clock and mapping behavior unverified. |
| API audit | Whether a request was processed, rejected or queued. | 24 hours after ingestion 12:00:04 UTC. | Sample completeness and write-path coverage unknown. |
| Host volatile state | Whether a process/token is still present. | Until restart; no clock deadline supplied. | May disappear immediately; collection can change state. |

At an exercise planning time of **12:06 UTC on 11 October 2026**, identity detail has the shortest *calculated* timed window, but the host volatile source has an **unknown** deadline and may need simultaneous owner contact. The table does not authorize collection. The priority is to ask the relevant custodians and incident lead for a narrow, approved preservation path, with a privacy limit and exact fields. If that cannot be arranged before a proposed expiry, record the loss risk and escalate; do not run an unauthorized bulk export.

### 7.2 Calculate, then challenge, an expiry hypothesis

Run this Python 3 code offline. It calculates three expiry hypotheses from literal UTC timestamps. The code does not check whether a logging system actually retains data for that long, whether clocks are synchronized or whether a legal hold overrides normal disposal. Its result is a planning aid that must be confirmed with the custodian.

~~~python
from datetime import datetime, timedelta

specs = [
    ("identity_detail", "2026-10-11T11:58:00+00:00", 10),
    ("edge_ring", "2026-10-11T12:00:05+00:00", 15),
    ("api_audit", "2026-10-11T12:00:04+00:00", 1440),
]
for name, anchor, minutes in specs:
    expiry = datetime.fromisoformat(anchor) + timedelta(minutes=minutes)
    print(name, expiry.strftime("%Y-%m-%dT%H:%M:%SZ"))
~~~

Expected output: **identity_detail 2026-10-11T12:08:00Z**, **edge_ring 2026-10-11T12:15:05Z**, **api_audit 2026-10-12T12:00:04Z**. From 12:06:00 UTC the first calculated window is two minutes. That is not a “two-minute permission” or a certified retention promise. If the identity row was ingested at 12:01 rather than emitted at 11:58, a source that anchors on ingestion would yield a different expiry. Record that as a variant, not as a correction to L7. A source clock offset could similarly move an apparent event-time anchor. Never silently replace the raw time.

### 7.3 Build a bounded preservation queue

A queue item must tell an authorized collector exactly what to request and why. Example **Q7-1** asks the identity custodian, under an incident-lead-approved case scope, to preserve only the detailed session rows for the L7 principal/session identifier during **11:57:30–11:59:30 UTC**, including producer event time, ingestion time, source object ID, session semantics and collection receipt. It asks the custodian to confirm the retention anchor and source clock. It expressly excludes unrelated accounts and broad user attributes. The request is **pending** until the custodian and authorized role accept it.

Q7-2 asks the gateway custodian for a bounded **12:00:00–12:00:10 UTC** mapping of r-201 to any upstream ID and the upstream timeout fields, plus source coverage and producer time. Q7-3 asks the application custodian for an API audit sample covering the same interval, filtered only after documenting possible ID rewriting. These requests might be pursued in parallel if owners and authority exist. Their order should reflect disappearance risk, decision value and collection cost, not just which tool is easiest. A short-retention source with no decision relevance should not automatically outrank a less volatile source that can settle an urgent containment question.

An answer can be **unavailable** as well as positive or negative. If the identity custodian reports that the detail row expired, record the reported time, source, query and coverage; do not fill the gap with a guess. If an export arrives, carry forward its raw-byte receipt and transformation report from Chapters 4–5. If only a screenshot arrives, record its limited provenance and seek a source record where appropriate. A screenshot can show an interface at capture time but may omit filters and earlier data. The analyst's timeline should retain both source event time and the later time when the analyst learned of it.

### 7.4 Coverage test as a small experiment

Suppose a later **separate L7 test** has a known synthetic control event at 12:00:06 that the API custodian says was emitted. Querying the exact 12:00:00–12:00:10 window should return it if the pipeline, fields and access path are working. If it does not, the missing r-201 row is even less informative. If the control appears, that improves confidence in this interval and source but does not prove complete coverage of all routes or that the request ID was preserved unchanged. The test should document the control's producer receipt, not merely an analyst-created string in a spreadsheet. A negative control outside the interval helps reveal accidental overbroad queries. Neither control should be run against production without permission.

### Common errors and limits

- Treating a retention duration without an anchor as an exact deletion deadline.
- Equating event time, ingestion time, collection time and query-run time.
- Searching by one request ID without checking whether the gateway rewrites it.
- Letting a synthetic control event become a main-case observation.
- Prioritizing easy collection over decision value and disappearance risk.

### Exercises — subject 7

**EX025 — Source matrix.** Objective: map three decision questions to producers. For “did r-201 reach API?”, “did a session exist?” and “did a worker process start?”, give source, expected fields, custodian, clock basis, retention question and one absence interpretation that remains unresolved. Evidence: three-row matrix. Rubric: 2 = producer limits and ID mapping explicit; 1 = sources listed without absence conditions; 0 = turns a missing sample row into a universal fact.

**EX026 — Expiry transcript and variant.** Objective: reproduce §7.2. Give the three exact output lines and calculate time remaining for identity detail at 12:06:00 UTC. Then assume **only in a variant** that identity retention starts from ingestion at 12:01:00; compute its 10-minute expiry and explain why this does not rewrite L7. Evidence: two calculations. Rubric: 2 = correct dates/times and anchor caveat; 1 = one arithmetic error; 0 = calls the estimate permission to export.

**EX027 — Priority queue.** Objective: write actionable, lawful requests. At 12:06, rank identity detail, host volatile state, edge ring and API audit for initial owner contact. Give a reason and a bounded query for the first two, distinguish unknown host expiry from timed retention, and state what to record if one source is unavailable. Evidence: queue with owner and status fields. Rubric: 2 = risk and decision value together, approval pending; 1 = ranked list without scope; 0 = instructs a broad export.

**EX028 — Coverage experiment.** Objective: distinguish absence from no event. Design the L7 in-range and out-of-range controls for a 12:00:00–12:00:10 query. State what each outcome supports and what it cannot prove about r-201 or unobserved routes. Evidence: experiment card. Rubric: 2 = controls, producer receipt and bounded inference; 1 = positive control only; 0 = treats a successful control as proof of total completeness.

### Subject synthesis

Source selection is a technical and authorization decision. The expiry script makes assumptions inspectable; it does not create or extend access. Chapter 8 will use source limits and uncertain clock ordering to compare a network fault, identity denial, host restart and maintenance without inventing a culprit.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — chapter 07 of 18

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Identity, host and network failure modes

### Learning outcomes and connection

The learner will distinguish authentication, authorization, host and network symptoms; correct reported times under an explicit clock-offset model; and request observations that discriminate competing explanations. Chapter 7 established which sources could answer a question and which might be incomplete. Chapter 8 applies that discipline to a mixed-symptom packet. The lab is **L8**, a separate fictional branch. It is not a later discovery about N01–N06, I01–I02, H01 or A01. [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) supplies general HTTP status semantics; the L8 labels, clocks and diagnoses are original teaching fixtures.

### 8.1 Name the failure layer and the user outcome

An **authentication** error concerns establishing the claimed identity; an **authorization** error concerns whether an established principal may perform an action. A service may report HTTP 401 for an authentication challenge, 403 for a refusal and 503 for temporary service unavailability under appropriate HTTP semantics. Those codes are observations from a particular component, not diagnoses of the whole path. A gateway can produce 503 because an upstream call timed out, while the underlying cause is DNS, routing, queue pressure, an application dependency, a database delay or a deliberate maintenance action. An IdP denial does not prove a malicious user: expired credentials, clock skew, policy rollout and client configuration are possible. A host restart does not prove compromise: patching, crash recovery and operator action are possibilities.

LLR's **user outcome** remains a correct, authorized room reservation with an audit trail. L8 instead supplies a bounded symptom packet for a teaching variant at approximately 12:00 UTC:

| ID | Reported source time | Fictional observation | What it does not establish |
|---|---|---|---|
| F81 | Edge 12:00:03, edge clock measured +2 s | GET /rooms returned 503 with gateway upstream-timeout label and request r-401. | Which upstream component caused the timeout. |
| F82 | IdP 12:00:00, IdP clock measured −1 s | One API-to-IdP call reports a timeout. | A global IdP outage or policy denial. |
| F83 | Runner host 11:59:58, offset uncertain ±3 s | Boot identifier differs from the prior supplied host inventory. | That the restart caused F81 or was unauthorized. |
| F84 | Change calendar 11:59 | A switch-maintenance window was scheduled for this path. | That the switch was actually changed at 11:59. |
| F85 | API query collected 12:06 | A 12:00:00–12:00:10 sample has no literal r-401 field. | That the API never saw the request; ID mapping and coverage are unknown. |

This packet includes **one** IdP timeout, not an authentication rejection. Do not label it 401, 403 or “credentials stolen.” The edge's 503 says what the client got. The calendar is a planned change, not an execution receipt. The changed boot ID supports the hypothesis that the host restarted; it does not identify why. An API sample with no literal r-401 may be missing a mapped request ID. The packet gives enough to form testable hypotheses, not enough to select a single root cause.

### 8.2 Normalize clocks without pretending to order every event

For a source whose clock is **ahead** of UTC by two seconds, subtract two seconds from its reported time. For a source **behind** UTC by one second, add one second. The formula is corrected UTC = source-reported time − measured source offset. That correction should carry the offset measurement time and uncertainty; clocks can drift. Run the following code offline to reproduce the two stated estimates.

~~~python
from datetime import datetime, timedelta

def corrected(raw, offset_seconds):
    reported = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    return (reported - timedelta(seconds=offset_seconds)).strftime(
        "%H:%M:%S"
    )

print("F81 corrected:", corrected("2026-10-11T12:00:03Z", 2))
print("F82 corrected:", corrected("2026-10-11T12:00:00Z", -1))
~~~

The expected output is **F81 corrected: 12:00:01** and **F82 corrected: 12:00:01**. The matching second does **not** establish which event came first or whether they share a transaction. F83's ±3-second uncertainty overlaps both estimates, and F84 has no execution timestamp. A proper technical timeline keeps raw time, correction rule, measurement uncertainty, producer and collection time in separate columns. It can state “temporally compatible” while refusing to draw a causal arrow. If an offset measurement is stale, record that as a limitation rather than fabricating subsecond precision.

### 8.3 Competing hypotheses and discriminators

Build a decision table instead of choosing the most vivid story. For each hypothesis, state what the packet supports, what remains unknown, a least-invasive owner-approved observation and a result that would weaken it.

| Hypothesis | Present support | Bounded discriminator | A weakening result |
|---|---|---|---|
| Path-specific network interruption to IdP | One API-to-IdP timeout and a scheduled switch window. | Network owner supplies an approved execution receipt plus path metrics for the API–IdP segment. | No change executed and validated path metrics show normal connectivity in the relevant interval. |
| Identity service/policy issue | One timeout involving IdP. | IdP custodian checks same-interval request IDs, policy version and reachability from another client class. | The same request succeeded under the validated mapping, with no relevant policy change. |
| Host restart affecting worker | Different boot ID on runner. | Host owner supplies boot reason, service dependency, process start and job queue status. | Runner is outside the affected edge/API path and the worker finished normally. |
| API or database delay | Edge labels upstream timeout. | Application/database owners check bounded upstream trace and authoritative data route. | Validated trace shows normal processing within the edge deadline for mapped r-401. |
| Unauthorized activity | Mixed failures could coexist with an incident. | First establish a source-linked unauthorized action, target and authority ledger status. | A complete approved change record explains the tested action; other hypotheses still need review. |

The “weakening” column does not mechanically disprove a hypothesis. A query can be incomplete, and a path can fail intermittently. The responder should update confidence only within the tested interval and source coverage. A scheduled maintenance record may explain timing but not prove execution; an execution receipt plus a path-specific metric is stronger. Even then, attribution of a human or intent requires separate evidence. These distinctions matter because premature principal revocation or service restart can destroy useful volatile state and affect approved reservation work.

### 8.4 A two-step supervised troubleshooting lab

Step one is a **paper request**, not live access. Ask the network and application custodians for a 11:59:55–12:00:10 UTC window, including offset measurement, upstream mapping of r-401, timeout class, interface/path metrics, collection receipt and limits. Ask the change owner for a versioned maintenance execution record; a calendar entry alone is insufficient. Simultaneously ask the identity custodian whether the F82 timeout is one request or part of a broader pattern, with privacy-limited fields. The incident lead should approve the source scope, and each custodian should confirm query coverage.

Step two is a **conditional interpretation**. If a complete gateway-to-API trace maps r-401 to an API request that reached the database after the gateway deadline, API/database latency becomes more plausible; the IdP timeout may be separate. If the trace shows a drop on the API-to-IdP path concurrent with an approved switch change, network maintenance gains support. If the sources cannot be collected, retain multiple hypotheses and record the evidence gap. Do not choose a winner from a missing row. A useful handoff says which user outcomes are impaired, which claims are source-bounded, what authority is pending and what next observation would change the action.

A **negative-control variant V8** changes only F82: the IdP custodian now supplies a validated successful response for the same mapped API request. That weakens a complete IdP outage for this transaction but does not prove that the edge's 503 was unrelated to identity for every request, or that the network was healthy everywhere. Keep the original and variant separate. The lab's purpose is to practice revising a hypothesis when better evidence arrives, not to issue a final diagnosis.

### Common errors and limits

- Reading one 503 as proof of a cyberattack or one IdP timeout as a credential failure.
- Calling a scheduled maintenance window an executed change.
- Ordering two corrected one-second timestamps despite overlapping clock uncertainty.
- Treating a changed boot ID as a human attribution.
- Using a successful control on one route to claim every route was healthy.

### Exercises — subject 8

**EX029 — Symptom separation.** Objective: keep layers distinct. For F81–F85, list producer, observed field, affected user outcome, one plausible failure layer and one unsupported inference. Explain why F82 is a timeout rather than an authentication denial. Evidence: five-row Markdown table. Rubric: 2 = all five with source limits; 1 = one conflation; 0 = declares stolen credentials or completed maintenance.

**EX030 — Clock transcript.** Objective: reproduce §8.2 and preserve uncertainty. Report both exact output lines, the correction formula, F83's uncertainty and why matching corrected seconds cannot order F81/F82. Evidence: raw/corrected timeline. Rubric: 2 = both outputs plus uncertainty; 1 = arithmetic only; 0 = asserts causality from time coincidence.

**EX031 — Discriminator matrix.** Objective: compare explanations without a premature action. For network, IdP/policy, host, API/DB and unauthorized-activity hypotheses, provide one supporting row, a custodian, an approved observation and a weakening result. Mark authorization status **pending**. Evidence: five-row table. Rubric: 2 = source-specific and falsifiable; 1 = generic “check logs”; 0 = orders a live restart or principal revocation.

**EX032 — Variant handoff.** Objective: update a conclusion with a negative control. Write a 160–220-word handoff contrasting original F82 with V8's validated success. Include the corrected clock, remaining r-401 mapping gap, maintenance execution question, service risk of a broad control and next owner. Evidence: versioned note, not final diagnosis. Rubric: 2 = variant kept separate and bounded next request; 1 = notes success but overstates scope; 0 = announces universal recovery or actor.

### Subject synthesis

The packet supports several explanations, each with a different discriminator. Technical response requires source-specific, time-bounded and authorized tests; no code output, status code or calendar entry by itself assigns cause or actor. Chapter 9 is currently a **plan** for host and network evidence collection methods. Stop the required authored sequence here until that chapter is written.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — chapter 08 of 18

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 plan →](PLAN.md#ch-09)

The next chapter is an outline, not yet an authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results and assessment notes

### Subject 1: EX001–EX004

**EX001 — Model service map.** A complete map lists `edge → api` (gateway owner; decide whether the user request reached upstream; static health coverage unverified), `api → idp,db` (application/identity/database owners; decide authorization and stored reservation outcome; fallback/clock coverage unverified), `worker → idp,db` (job owner; decide whether scheduled work can continue; retry behavior unverified), `backup → db` (recovery owner; decide whether new copies can be made; isolated restore not demonstrated), and `idp`/`db` as producers with **no further dependencies supplied**. That is six rows if `idp` and `db` are separate. A reviewer should reject a diagram that reverses the arrows or calls the simplified graph complete. Two points require an owner and a falsifiable unknown for every row; a valid alternative owner title is acceptable if its decision right is specified.

**EX002 — Model closures.** The code prints `idp: ['api', 'edge', 'worker']` and `db: ['api', 'backup', 'edge', 'worker']`. For the negative control, replace `"edge": {"api"}` with `"edge": set()` **in a copy**. The new outputs are `idp: ['api', 'worker']` and `db: ['api', 'backup', 'worker']`: `edge` disappears in both because no remaining dependency path reaches it. The output is a graph-derived potential-impact set; it cannot show that any actual request failed or that an edge cache would not mask an API loss.

**EX003 — Model boundary worksheet.** Browser→edge: asserted browser session, edge authentication/transport check, request/access record, gateway custodian, client certificate or app-session mapping **not supplied**. Edge→API: asserted service identity/request ID, API authorization/route check, `r-201` or mapped upstream ID, application owner, ID-preservation semantics **untested**. API→DB: asserted application role, DB permission check and read/write audit, database custodian, write-path coverage **unverified**. One may instead use DB→backup with backup-object/version metadata. TLS channel completion alone does not supply the application user or prove the DB saw a write. A full-score worksheet makes each missing field testable and names its custodian.

**EX004 — Model change comparison.** “At 12:04 the edge error and unfinished worker run are reports, not proof that `svc-reserve` is malicious. A targeted pause of one verified out-of-scope task might limit unwanted changes while preserving the approved worker; its target and scheduler scope must first be confirmed. Revoking the shared principal would affect `api`/`worker` dependency paths and may stop legitimate R40/R41 work. I request read-only owner-approved API, IdP and job records before any change. If a continuing harmful task is confirmed, the service and identity owners should approve the exact target, operator, expiry, rollback owner and expected effect. The request must record who observed the task, when the observation was made, and which evidence would falsify the concern. Positive test: no further out-of-scope R42 changes in a stated window. Negative/business test: approved R40/R41 operation continues. Approval, execution and verification remain **pending**.” Different prose can pass if it names both options, risks, boundaries and falsifiable checks.

### Subject 2: EX005–EX008

**EX005 — Model claim ladder.** N01: one supplied resolver answer; not proof the browser used it. N02: client-to-edge TCP completed; not proof the API was reached. N03: edge reports TLS completion; not proof of app authorization. N04: edge returned **503** for `GET /rooms`, first observed failure of the expected room-list outcome; not proof of API crash or attack. N05: no `r-201` in the supplied 10-second API sample; not proof the API never received a request. N06: static `/health` returned **200** at 12:03; not proof the affected `/rooms` function recovered. Six bounded pairs and N04 as failure stage earn two points. A learner may note that client certificate validation is not supplied; that is a useful limitation, not a contradiction.

**EX006 — Model request.** “Gateway and application custodians: under case-approved read-only access, please preserve the 12:00:00–12:00:10 UTC edge upstream metrics and API access/audit interval for `r-201`; state producer clocks, collection time, retention, original object IDs, whether the gateway carries `r-201` unchanged or maps it to a new upstream ID, and any timeout/queue fields. If a validated, complete API source with stable ID semantics shows no matching receipt, path-to-API or queueing becomes more plausible. If a mapped receipt exists, inspect the API-to-DB dependency next. No restart or broad capture is requested.” This is a **request**, not an export receipt. Two points require the narrow scope, custodian/authority and both interpretation branches.

**EX007 — Model classifier transcript.** Original: `client-to-edge: observed`; `rooms request: 503`; `API sample contains r-201: False`; `static health proves rooms success: False`. Variant with only `tcp_to_edge=False`: first line `client-to-edge: not established`; the other three lines remain as above because the code does not alter their literal inputs. The variant is an artificial counterfactual that contradicts N02 and **cannot rewrite** the supplied trace. No output identifies the root cause of N04.

**EX008 — Model cautious handoff.** “At 12:00:00 a supplied resolver row gave `portal.example.test` a 60-second TTL; this does not prove which resolver answer the browser used throughout that minute. At 12:00:01–03, the edge recorded a connection, TLS completion and a 503 for `GET /rooms` with `r-201` and an upstream-timeout label. The supplied API sample has no `r-201`, but source coverage and ID mapping are unknown. A 12:03 static `/health` 200 tests a different endpoint and does not establish room-list or write-path recovery. Under the owners' read-only permission, request bounded edge upstream and API logs with producer clocks and request-ID semantics. Record the query window and the custodian's coverage statement. Do not restart a service or name an attacker from this packet.” A result may use different wording but must keep event times, endpoint distinction and an owner-led discriminator.

### Subject 3: EX009–EX012

**EX009 — Model entity matrix.** Host process = H01 `runner-02`, PID 420, start 11:58:04; OS account = H01 `svc-reserve`; IdP principal = I01/I02 `svc-reserve` and A01 label; IdP session = I01 `sid-88`, I02 **separate denied** `sid-89`; human = **unknown**. H01 has no session ID; A01 has a blank session field; no person field exists. To join I01→A01, request producer-validated session/request mapping for `r-202`; to join H01→I01, request a host/process-to-token relationship with stable host/time context. A matching label is insufficient.

**EX010 — Model timeline.** 11:58:00 I01 successful `sid-88` reported; 11:58:04 H01 process start on `runner-02`; 12:00:03 A01 R42 change under shared principal, blank session; 12:00:04 I02 denied `sid-89`. Separately, CH01's **11:50** approved calendar covers R40/R41 through 12:10 but not R42 in the supplied version. H1 misconfigured worker: shared principal and nearby process are suggestive; ask for complete signed job manifest and `r-202` mapping. H2 other task/operator: R42 is outside visible scope; ask for authorized session/request trail and task inventory. H3 missing addendum: ask change owner for the versioned R42 ledger. Clock offset and export completeness are unverified. Neither four-second spacing nor I02's denial proves a causal path.

**EX011 — Model join-check outputs.** Original: `same principal label: True` and `direct session join: False`. Separate variant with `api["session"] = "sid-88"`: `same principal label: True` and `direct session join: True`. The booleans test **strings in two synthetic dictionaries**. Before a real case join, establish that both producers use the same session namespace, capture the source objects and collection method, and check whether the mapping can be forged or altered. The original A01 remains unjoined even though its principal label matches I01.

**EX012 — Model paper proposal.** “Preserve I01/H01/A01/CH01 snippets without overwriting their raw forms. Ask the application custodian, under a bounded 11:58–12:01 UTC approval, whether a restricted audit source maps `r-202` to a session ID, with source object, collection time, field semantics and retention. Ask the change owner for the official versioned R42 approval scope; a missing row in this snippet is not a complete ledger result. Ask the identity owner how long the relevant session detail remains and who may collect it. Record the producer clock basis and collector so the resulting join can be independently checked. If a continuing unapproved task is later confirmed, compare an exact task pause with shared-principal revocation. Service and identity owners must approve target and expiry; an authorized operator and rollback owner remain pending. Positive check: observed out-of-scope R42 writes stop in a defined window. Negative check: approved R40/R41 worker operations and audit continue. The rollback owner should restore the approved task only after verifying the intended scope and recording the result. No change is executed by this request.” Equivalent text passes when it retains source limits and both verification dimensions.

### Subject 4: EX013–EX016

**EX013 — Model schema contract.** A full-score table is:

| Field | Type and acceptance rule | Rejection in L4 | Producer-semantic question |
|---|---|---|---|
| event_id | Nonblank text, unique within this bundle. | Missing or previously accepted ID. | Unique only per export, per source, or across exports? |
| event_utc | UTC timestamp ending Z, parseable by the stated Python function. | Missing, non-Z or unparsable. | Event, ingestion or export time? |
| source | Text from the local set edge/api. | Missing or outside that set. | Which system generated the record, and how is it verified? |
| request_id | Nonblank text. | Missing or blank. | Carried unchanged, remapped or newly assigned at each hop? |
| kind | Nonblank event-type text. | Missing or blank. | Observation, business-state change or synthetic test code? |

The parser also checks column count. An event_id identifies a record under an export-specific uniqueness rule; a request_id may identify a transaction only when producers agree on its mapping. Neither identifies a human. Two points require rules and source questions. A different decision-purpose might quarantine rather than reject a blank request ID, but that alternate rule must be stated before interpreting results.

**EX014 — Model transcript.** Original output:

~~~text
accepted_ids: ['E1', 'E2']
rejected: [(4, 'duplicate_id'), (5, 'bad_time'), (6, 'missing_required')]
~~~

In a separate copy, set E4's blank request ID to r-205. The exact output becomes **accepted_ids: ['E1', 'E2', 'E4']** and **rejected: [(4, 'duplicate_id'), (5, 'bad_time')]**. E4 is now a valid local parser row, not main-case edge evidence. The duplicate E2 remains line 4 and invalid-time E3 remains line 5. A report stating only “three valid rows” omits which input changed, the two remaining rejections and the provenance limitation.

**EX015 — Model join review.** Proposed E1↔E2 join: **unsupported**, because E1 carries r-201 and E2 carries r-202. Equal second-level times are not a mapping rule. Proposed N04↔E1 comparison: both use fictional edge r-201 labels, but E1 is a separate L4 copied fixture, not an authenticated duplicate of N04. Proposed A01↔E2 comparison: both mention r-202 and R42, but A01 is main-case application evidence and E2 is an L4 synthetic line; their source histories cannot be merged. Request a validated 12:00:00–12:00:10 UTC upstream-ID mapping, producer clocks, original object IDs and query coverage from the gateway and application custodians. **Hypothetical branch:** if authenticated mapping says r-201 becomes r-202, a transaction link gains support within its tested scope; it still does not attribute a person or settle R42 approval.

**EX016 — Model parser review.** Discarding the rejection list hides the unparsable time on line 5 and the duplicate accepted ID on line 4. Assigning 12:00:00Z to E3 invents temporal order and might create a false correlation. The corrected output contract retains raw input, accepted rows with line positions, rejected rows with exact reasons, code version and collection context; it does not emit a guessed time as source data. A negative-control copy changes only E3's timestamp to a valid synthetic value and checks that its rejection changes. Only the source custodian can supply a corrected export under approved scope. An analyst may annotate uncertainty, not silently repair a producer record.

### Subject 5: EX017–EX020

**EX017 — Model scope gate.**

| Proposed action | AUTH-L5 result | Why |
|---|---|---|
| Inspect literal L4 CSV offline. | Allowed. | Named classroom input only. |
| Compute its in-memory digest. | Allowed. | No external collection or production change. |
| Export all IdP sessions. | **Not allowed.** | Identity source and privacy scope not covered. |
| Image runner-02. | **Not allowed.** | Live host and volatile-state collection not covered. |
| Restart API. | **Not allowed.** | Production change, not a read-only classroom task. |

For a future session-detail request, the identity custodian would specify fields and retention while the incident lead/privacy role approves a bounded purpose under local policy. That future approval remains **pending**. A full result separates trainee permission from organizational authority.

**EX018 — Model byte transcript.**

~~~text
original_bytes: 43
copy_matches: True
altered_matches: False
~~~

Replacing E9 with E1 in the variant makes altered equal to original, so **altered_matches: True**; keep the first transcript. The bytes were constructed in Python. Their equal digest does not authenticate an edge export or establish completeness. The 43-byte original has SHA-256 **adb14f1f662e41419d94dc3fcdf6aa1f1af5daab822c98a493d64fb8629443bf**. The E9 variant has SHA-256 **51435bf940b015c8872e4e226e4619dd584684988482d730052006cd32c3eb77**. These are reproducible lab values, not independently trusted custodian digests.

**EX019 — Model versioned receipts.** Receipt L5-1: object **L5-original**, supplied by the **exercise publisher** at classroom time 12:06 UTC; collector trainee; AUTH-L5; method literal in-memory copy; length **43 bytes**; SHA-256 **adb14f1f662e41419d94dc3fcdf6aa1f1af5daab822c98a493d64fb8629443bf**; access local exercise; production source **unknown/not claimed**. Receipt L5-2: object **L5-altered**, derived from L5-1 by replacing the first E1 with E9; length **43 bytes**; SHA-256 **51435bf940b015c8872e4e226e4619dd584684988482d730052006cd32c3eb77**; collector trainee; method in-memory variant; relationship “derived classroom control”; access local exercise. Record the actual variant-creation time when performed; it is **pending** in the prompt. Neither receipt grants real retention or legal custody status.

**EX020 — Model review.** The peer's sentence makes three unsupported jumps: equal SHA-256 values compare the **chosen bytes**, not exporter authority or honesty; L4 is a five-line synthetic bundle with three rejected rows, not a complete API corpus; and r-201 may be mapped to another upstream ID. A bounded rewrite is: “The supplied L4 bytes match the retained classroom copy; among its two accepted rows there is no API row bearing the literal r-201 identifier.” Ask for an owner-approved, privacy-limited gateway/API 12:00:00–12:00:10 mapping and source-coverage check. If a validated mapped receipt appears, revise the hypothesis; if not, preserve the source-limit statement rather than declare universal absence.

### Subject 6: EX021–EX024

**EX021 — Model route contract.** Cached room read requires edge/api in L6 and aims to display a room list; the application owner must test freshness and cache-enabled behavior, with stale data as a negative condition. Reservation write requires edge/api/idp/db and aims to create an authorized, auditable booking; a negative check attempts a disallowed reservation in an isolated approved test. Approved worker requires worker/idp/db and aims to process an authorized R40/R41 job; retry and duplicate-write behavior remain unknown. New backup requires backup/db and aims to produce a restorable **new** object; an old copy's presence is not this outcome. Chapter 1's component graph is conservative about API dependency; L6 refines individual routes under a hypothetical cache assumption. A static health probe is not a successful write.

**EX022 — Model route outputs.**

~~~text
idp: ['approved_worker', 'reservation_write']
db: ['approved_worker', 'new_backup', 'reservation_write']
db with cache disabled: ['approved_worker', 'cached_room_read', 'new_backup', 'reservation_write']
~~~

Adding db to cached_room_read changes only a copy of the route definition. It reveals that predicted db impact is sensitive to the cache assumption; it does not add measured outage or alter N01–N06. Seek an owner-approved cached-read correctness and freshness check before using either output operationally.

**EX023 — Model control comparison.** A task pause requires validated R42 task/request mapping; it might stop a narrow harmful task but can pause approved work if mapping or scheduler scope is wrong. Service/job owner approval and a task operator are pending. Positive test: no further out-of-scope R42 changes on documented routes. Negative test: approved R40/R41 work and audit continue. Record expiry and rollback owner. Shared-principal revocation needs stronger evidence because it may affect reservation_write and approved_worker; identity and service owners must approve exact principal/session/duration, with abuse and business-path tests. Read-only mode might protect current state but blocks new bookings; the service owner must approve fallback, expiry and reconciliation. The first **conditional proposal**, if a continuing task is confirmed and mapped, is a narrow task pause with route coverage and rollback. Otherwise request read-only evidence. Execution and verification remain **blank**.

**EX024 — Model restore challenge.** Copy timestamp 11:55 to accepted write 11:58 gives an apparent **three-minute gap**. Ask whether the copy includes later commits despite its label; whether a protected journal can replay the accepted write; and whether the owner-designated ledger is complete and independently checkable. Technical gate: verify copy provenance/bytes/schema in isolation and compare a replay candidate without touching production. Business gate: owner checks expected reservations, permitted downtime, privacy and staged-return approval. The exercise supplies no measured RPO and does not prove loss. Whole-copy production restore remains pending.

### Subject 7: EX025–EX028

**EX025 — Model source matrix.** For r-201 reaching API: use gateway mapping/upstream trace plus application access/audit; seek edge ID, mapped upstream ID, route, outcome and producer time. Gateway/application custodians must confirm 12:00:00–12:00:10 coverage and ID semantics; a missing literal key may be mapped. For a session existing: use IdP detail with session identifier, decision, event/ingestion time and identity custodian; absence may reflect retention or query scope. For a worker starting: use host process/boot record plus scheduler manifest with PID/start/boot ID and job owner; absence may reflect disabled logging or another host. Each row needs retention anchor and collection method. r-201 absence in an incomplete API sample remains unresolved.

**EX026 — Model expiry calculation.**

~~~text
identity_detail 2026-10-11T12:08:00Z
edge_ring 2026-10-11T12:15:05Z
api_audit 2026-10-12T12:00:04Z
~~~

At 12:06:00, the identity estimate has **two minutes** remaining. In a **separate ingestion-anchor variant**, 12:01:00 plus ten minutes yields **12:11:00 UTC** on 11 October 2026. That variant changes the rule, not L7's stated event anchor. Ask the custodian which anchor, clock and actual retention behavior apply before treating either estimate as a deadline. Neither calculation grants permission.

**EX027 — Model initial queue.** Contact host and identity owners **in parallel** at 12:06 because volatile host state has no known deadline and calculated identity-detail expiry is 12:08. For identity detail request only 11:57:30–11:59:30 session rows, source clock, original object and retention anchor under incident-lead/privacy approval; export status **pending**. For host ask its custodian for a minimal read-only status/boot and process-record proposal limited to runner-02, with method, side effects and authority pending; do not image it from this exercise. Next contact gateway for 12:00:00–12:00:10 ID mapping; API audit is less time-critical under L7's **claimed** 24-hour window but still has high decision value. Another order can earn full credit if it explains immediate contact for both volatile and timed sources. If unavailable, record custodian statement, query window, collection time and hypothesis gap.

**EX028 — Model coverage experiment.** Under separately approved L7 testing, the API custodian supplies a known control event with producer receipt at **12:00:06**. A 12:00:00–12:00:10 query should return it; an independently identified event at **11:59:50** should be excluded. If the first is missing, pipeline/filter/permission or clock behavior is suspect, making r-201 absence weaker. If the first appears and second does not, tested source/window coverage gains limited support but other routes and ID mapping remain unverified. If the out-of-range control appears, query scope or time semantics differ. Do not create events in production without authorization.

### Subject 8: EX029–EX032

**EX029 — Model symptom table.** F81 is an edge-produced 503/upstream-timeout for one room-list read: gateway/upstream path symptom, not proof of attack. F82 is an IdP-produced **timeout** on one API call: no returned authentication decision is supplied, so it is **not** a denial or a 401/403 record. F83 is a host-produced changed boot ID: runner restart plausible, cause and link to room-list failure unknown. F84 is a change-calendar schedule: execution unknown. F85 is an API query lacking literal r-401: source coverage and gateway mapping unknown. A good table names producer and scope in every row, keeps the reservation user outcome unverified and infers no human actor.

**EX030 — Model corrected clock transcript.**

~~~text
F81 corrected: 12:00:01
F82 corrected: 12:00:01
~~~

Correction is **reported source time − measured source offset**: edge +2 seconds becomes 12:00:01, IdP −1 second also becomes 12:00:01. F83's ±3-second uncertainty overlaps that moment and F84 lacks an execution timestamp. Equal one-second estimates do not order the events or prove causation. Preserve raw time, offset measurement time, uncertainty, producer and collection time.

**EX031 — Model five-way discriminator.** Network interruption: F82 and F84 are suggestive; network custodian should supply 11:59:55–12:00:10 path metrics and versioned execution receipt; no executed change and normal validated path behavior would weaken it. IdP/policy: F82 motivates same-request result and policy-version check; validated success for the mapped request weakens complete outage. Host restart: F83 motivates boot reason, worker status and dependency check; runner outside affected path with normal job completion weakens direct causation. API/DB delay: F81 motivates mapped upstream timing and authoritative route check; within-deadline processing would weaken it. Unauthorized activity: mixed symptoms alone are insufficient; ask incident lead/change owner for a source-linked unauthorized action and ledger status. A complete approved record for the tested action weakens that specific claim. Collection and control approvals remain **pending**. No row selects an actor.

**EX032 — Model versioned handoff.** “Version 1, L8 teaching branch, 12:06 UTC: F81 reports one edge 503 for r-401 and F82 reports one API-to-IdP timeout. With supplied offsets, both source times estimate 12:00:01 UTC; clock uncertainty does not establish order or causation. The runner boot ID changed near this interval, while F84 is only a scheduled maintenance window. The API sample lacks a literal r-401, but the gateway may remap that identifier and source coverage is unverified. The reservation write outcome has not been measured. I request owner-approved gateway mapping, API/IdP path timing and a versioned maintenance execution receipt for 11:59:55–12:00:10, including clocks and collection limits. I do not recommend broad principal revocation or API restart from this packet: either could interrupt legitimate bookings or change useful state. Version 2, separate V8 negative control: the IdP custodian now supplies a validated success for the same mapped API request. That weakens a complete IdP outage **for this transaction**; it does not establish all identity paths as healthy or explain the edge 503. Application and network owners should compare mapped upstream deadline and path metrics next. Authority to collect or change production remains pending.” Other wording passes if it preserves variant separation, next owner and service risk.

## Glossary for authored chapters

- **Dependency graph:** a model of which component's behavior may be needed by another; arrows and assumptions must be explicit.
- **Failure domain:** components that *might* be affected under a specified dependency hypothesis, not an observed outage count.
- **Trust boundary:** a crossing where authority, ownership or data-handling rules change.
- **Producer claim:** an observation reported by a particular logging source, whose scope and collection quality must be recorded.
- **Direct join:** a link through a matching identifier whose semantics and provenance are validated across producers.
- **Service principal:** a workload or service identity label, not automatically a human identity.
- **Parser rejection report:** excluded rows with input positions and explicit reasons retained.
- **Collection receipt:** the defined object's source claim, authority, collector, method, time and integrity check.
- **Retention anchor:** the event, ingestion or other time from which a duration is counted.
- **Route-level dependency:** components required for one outcome under stated assumptions.
- **Clock offset:** measured difference between producer-reported and reference time, with uncertainty.

## References and case boundaries

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (2025): current incident-response recommendations in cybersecurity risk management; LLR's service map and exercises are original.
- [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) (2006): high-level log-management guidance; the synthetic trace and source requests are original, and dated implementation details require current verification.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) (2006): forensic vocabulary from an IT perspective, not a current OS tool procedure or legal custody standard.
- [RFC 8446, TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html) (2018): transport protocol design; a handshake is not an application authorization decision.
- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) (2022): request/response and status-code semantics; LLR's 503 and health records are fictional.
- [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737.html) (2010) and [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761.html) (2013): documentation address blocks and special-use test names used in the offline fixture.
- [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180.html) (2005) and [Python CSV documentation](https://docs.python.org/3/library/csv.html): CSV format and parsing behavior, not log-source authentication.
- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html): byte-digest interface for the L5 comparison.
- [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) (2016): recovery planning and testing; L6's route and snapshot example is original.
