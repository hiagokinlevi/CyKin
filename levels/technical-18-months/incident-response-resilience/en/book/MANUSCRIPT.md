# Incident Response and Cyber Resilience: Technical Foundations and Lab Practice

- Language: English (`en`); technical course, up to 18 months; approximately 1,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–3 of 18, EX001–EX012 and their worked results are authored. Fifteen chapters, substantial expansion, source review, technical and accessibility review, and the 300-page A4 verification remain open.
- Audience: technical operators learning to model services, interpret evidence and verify controls under supervision. Entry knowledge: basic networking, operating systems, scripting and permitted lab practice.
- Author and editorial responsibility: [hiagokinlevi](https://github.com/hiagokinlevi). Original maintainer-owned teaching text is dedicated under [CC0 1.0](../../../../../LICENSE); cited standards retain their own rights.
- Educational boundary: every system, account, log and address in the Lumen Library Reservations case is synthetic. This book grants no access or change authority for a real environment.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md) · [Worked results](#worked-results)

## How to use this draft

Read chapters 1–3 in order. Each chapter is one curricular subject and begins with a technical model, then tests it against a reproducible **offline** fixture. Before reading the worked result, write the artifact requested by an exercise and explain which observation would falsify your conclusion. The remaining fifteen chapter positions have summaries in the [book plan](PLAN.md); those summaries are **not authored lessons**. The finished technical course targets 72 exercises, at least 50 of which must be substantive and worked in the book, plus a verified minimum of 300 A4 pages.

The case is **Lumen Library Reservations (LLR)**, an invented reservation service. It is separate from the professional book's Cedar Training Network case. Documentation-only names and addresses follow [RFC 6761's `.test` reservation](https://www.rfc-editor.org/rfc/rfc6761.html) and [RFC 5737's TEST-NET blocks](https://www.rfc-editor.org/rfc/rfc5737.html). Do not query these names or addresses on a network; the fixtures below are sufficient. Sources support protocol and response concepts, **not** the fictional LLR observations.

## Contents

1. [Computing and service architecture](#ch-01) — dependency and trust-boundary model with a testable failure-domain lab.
2. [Networks and protocols](#ch-02) — read a synthetic DNS/TCP/TLS/HTTP chain without inferring a cause from one status code.
3. [Operating systems and identities](#ch-03) — distinguish process, principal, session and human with bounded records.
4–18. [Planned technical subjects](PLAN.md#ch-04) — scripting, evidence, response systems, telemetry, troubleshooting, preservation, controlled changes and final integration; teaching remains to be written.

The worked-results appendix contains EX001–EX012, four per authored chapter. Section numbers in the manuscript are teaching sections; the course's subject index is the authoritative chapter list.

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

Host, identity and application records answer different questions. A shared label and close timestamps are starting points for an investigation, not a validated session-to-request edge or a human identity. Chapter 4's **plan** describes the next subject, scripting and data formats; authored teaching and exercises for that subject are not yet available. Stop the required course sequence here until that chapter is written.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — chapter 03 of 18

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 plan →](PLAN.md#ch-04)

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

## Glossary for authored chapters

- **Dependency graph:** a model of which component's behavior may be needed by another; arrows and assumptions must be explicit.
- **Failure domain:** components that *might* be affected under a specified dependency hypothesis, not an observed outage count.
- **Trust boundary:** a crossing where authority, ownership or data-handling rules change.
- **Producer claim:** an observation reported by a particular logging source, whose scope and collection quality must be recorded.
- **Direct join:** a link through a matching identifier whose semantics and provenance are validated across producers.
- **Service principal:** a workload or service identity label, not automatically a human identity.

## References and case boundaries

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (2025): current incident-response recommendations in cybersecurity risk management; LLR's service map and exercises are original.
- [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) (2006): high-level log-management guidance; the synthetic trace and source requests are original, and dated implementation details require current verification.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) (2006): forensic vocabulary from an IT perspective, not a current OS tool procedure or legal custody standard.
- [RFC 8446, TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html) (2018): transport protocol design; a handshake is not an application authorization decision.
- [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) (2022): request/response and status-code semantics; LLR's 503 and health records are fictional.
- [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737.html) (2010) and [RFC 6761](https://www.rfc-editor.org/rfc/rfc6761.html) (2013): documentation address blocks and special-use test names used in the offline fixture.

Every LLR observation and worked result is invented for teaching. No primary source is cited as evidence that LLR exists or that its events occurred.
