**Expected evidence:** four classifications matching the printed program output, a limitation for each, a request that names the smallest useful source and fields, and the Q1-V prediction. **Rubric (six points):** one point for correctly identifying both E-A candidates; one for E-B's key-and-window match without human attribution; one for E-C's zero-match limit; one for preserving E-D's explicit-key mismatch; one for a proportionate request including clock, coverage and schema; and one for predicting that E-B becomes ambiguous when its key is removed. A 6/6 score verifies reasoning on this fixture, not the trustworthiness of a real log join. The exact output and model request appear in the final answer appendix after the Chapter 2 evidence-package audit result.

<a id="ir-rapid-ch02-q1-scope"></a>

#### Q1-S — qualify identifiers and test sensitivity to clock uncertainty

**Learning goal:** Explain why equal key text is not enough to join two sources, calculate which session intervals could contain an uncertain event time, and keep input defects separate from an absence of matching evidence. Complete the four original Q1 cases first. This extension changes neither their inputs nor their four expected output lines.

**Classification and safety:** Q1-S is a separate, entirely invented fixture dated **2040-03-16**. Its realms, account and correlation keys are harmless labels, not authentication material, Harbor Library observations or additions to R1–R16. The laboratory uses only Python's standard library and in-memory data. It performs no collection, login, session access, network request, source modification or cleanup operation.

##### Equal text versus an equal identifier

A **namespace** is the context in which an identifier has its meaning. A **qualified key** retains that context with the value. In this exercise, the qualified key is the pair `(realm, key)`. Thus `(realm-a, K7)` and `(realm-b, K7)` are different identifiers even though their last component is identical. A real source contract might instead need an issuer, tenant, application, generation or another documented qualifier. Do not assume that this two-field classroom key is sufficient for every platform.

The following logical drawing represents **filtering a supplied candidate table**, not a network path or a successful authentication:

```text
Application row: realm-a | K7 | desk-x
                         |
                         v
             Select the declared realm
                /                   \
       realm-a rows             realm-b rows
       K6, desk-x               K7, desk-x
       K7, desk-x               Excluded: wrong realm
             |
             v
       Select K7 and desk-x
             |
             v
       Test the time interval
             |
             v
       Candidate relationship only
       No person, permission or intent established
```

**Text equivalent:** Start with the application's declared realm, retain only rows in that realm, then compare the explicit key, account and time. The other realm's K7 does not become evidence about this row. When the realm is unknown, stop with an unresolved namespace rather than search every realm and select a convenient result. A supplied but nonmatching key remains nonmatching; it must not be replaced by a weaker account/time lookup.

Three concepts must also remain separate. A **session correlation label** relates records to a declared session. An **interaction identifier** relates records to one interaction, such as an individual request. A **human attribution** is a further evidential claim about who acted. The [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#event-attributes) discusses interaction identifiers as a way to preserve application-known relationships and distinguishes event time from logging time. It does not make this exercise's realm/key pair an authenticated identity.

Do not make a correlation exercise an excuse to copy live session secrets. OWASP's [session logging guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#logging-sessions-life-cycle-monitoring-creation-usage-and-destruction-of-session-ids) warns against recording raw session IDs and describes a protected correlation approach. For a real review, request only the approved non-secret correlation representation, its scope and its documented mapping. Q1-S already supplies safe invented labels; it teaches no token acquisition or session replay.

##### Time uncertainty changes a set of candidates, not the event's history

The original Q1 tests one stated event time against exact supplied session endpoints. Q1-S asks a different question: what changes when the event's comparable time is known only to lie in a **closed range** `[low, high]`? The range is an explicit assumption, not an ingestion delay, a measured probability interval or permission to use a later-released record at an earlier checkpoint.

For a session whose supplied interval is `[start, end)`, define two tests:

| Test | Meaning under the stated model | Comparison |
|---|---|---|
| Possible candidate | At least one time in the event range lies inside the session interval | `low < end` and `high >= start` |
| Covers all times | Every time in the event range lies inside that session interval | `start <= low` and `high < end` |

The endpoint asymmetry is intentional. A session includes its start but excludes its end. An event range ending exactly at the session start still overlaps at that included instant. A range starting exactly at the session end does not overlap. A range that includes the exclusive end cannot pass the all-times test. These comparisons are derived from the declared intervals; they are not a NIST severity or confidence scale.

**Work the mechanism:** Suppose realm-a/K6 lasts from 09:00 to 09:15 exclusive and realm-a/K7 from 09:02 to 09:12 exclusive. An event with no key could have occurred between 09:11 and 09:13 inclusive. K6 contains the entire range. K7 contains only the part before 09:12. Both therefore remain possible, while only K6 covers all times.

```text
UTC minute     00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
realm-a/K6     [--------------------------------------------)
realm-a/K7           [-----------------------------)
event range                                     [-----]
```

**Figure reading:** Every tick is one minute after 09:00 UTC. `[` and `]` include an endpoint; `)` excludes it. The event range intersects both session intervals but is contained only by K6. These are invented intervals, not collected timestamps. The table below gives the exact numeric endpoints independently of the drawing.

One all-times candidate is **not** a unique attribution: K7 remains possible if the event was in the earlier part of the range. The all-times test is robustness to this particular time assumption, not proof of source truth or a higher probability. Likewise, widening an assumed range until a desired session matches does not validate the range. A custodian would need to substantiate the clock relationship and bound. If no usable bound is supplied, Q1-S reports `UNRESOLVED_TIME_BOUND` instead of silently assuming zero error.

This model treats session endpoints as exact and varies only the event time. Uncertain session clocks, changes in clock offset, session-key reuse and incomplete exports require additional evidence or a different model. Do not import the example's two-minute event range into the canonical 09:20 decision.

##### Complete independent input and execution contract

The program uses **integer minutes after midnight UTC** on its artificial date: 09:00 is 540, 09:02 is 542, 09:07 is 547, 09:11 is 551, 09:12 is 552, 09:13 is 553 and 09:15 is 555. Integer endpoints make the arithmetic inspectable; the program is not a parser for production timestamps or sub-minute evidence.

| Realm | Key | Account | Start inclusive | End exclusive |
|---|---|---|---:|---:|
| realm-a | K6 | desk-x | 540 | 555 |
| realm-a | K7 | desk-x | 542 | 552 |
| realm-b | K7 | desk-x | 542 | 552 |

A repeated bare K7 across realms is permitted; a repeated **qualified** key is rejected. Repeated exported rows might represent duplicate delivery rather than two sessions, but this small program does not decide that question: preserve the packet and ask about row identity and export semantics instead of silently deduplicating conflicting records. The account and key comparisons are exact and case-sensitive; the model does not invent alias mappings or trim identifiers into equality.

`key=""` is the explicit missing-key marker for this fixture. A numeric zero is a type error, not a missing key. `realm=None` and `event_range=None` mean the required namespace or comparable time bound has not been supplied. `all_times=()` means no tested row covers every time, except when an `UNRESOLVED` status says the test was not performed; always read the status with the sets. An empty packet is unresolved. A nonempty packet with no matches still establishes only the result of filtering those supplied rows.

Run the complete listing below in a **fresh Q1-S session**, independent of the original Q1 program. It prints eleven lines. Predict them before consulting the [Q1-S worked result](#ir-rapid-ch02-q1-scope-result).

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Session:
    realm: str
    key: str
    account: str
    start: int
    end: int

# Minutes after midnight UTC on the invented date 2040-03-16.
# Keys are harmless classroom labels, not authentication tokens.
SESSIONS = (
    Session("realm-a", "K6", "desk-x", 540, 555),
    Session("realm-a", "K7", "desk-x", 542, 552),
    Session("realm-b", "K7", "desk-x", 542, 552),
)

def nonblank(value):
    return isinstance(value, str) and bool(value.strip())

def correlate(rows, realm, account, key, event_range):
    """Filter declared toy rows; do not authenticate sources or identify people."""
    if not isinstance(rows, (tuple, list)):
        raise ValueError("INVALID_PACKET")
    if not rows:
        return "UNRESOLVED_EMPTY_PACKET", (), ()
    seen = set()
    for row in rows:
        if not isinstance(row, Session):
            raise ValueError("INVALID_SESSION_ROW")
        if not all(nonblank(x) for x in (row.realm, row.key, row.account)):
            raise ValueError("INVALID_SESSION_IDENTIFIER")
        if (type(row.start) is not int or type(row.end) is not int
                or not 0 <= row.start < row.end <= 1440):
            raise ValueError("INVALID_SESSION_INTERVAL")
        identity = (row.realm, row.key)
        if identity in seen:
            raise ValueError("DUPLICATE_QUALIFIED_KEY")
        seen.add(identity)
    if not nonblank(account):
        raise ValueError("INVALID_ACCOUNT")
    if not isinstance(key, str) or (key and not nonblank(key)):
        raise ValueError("INVALID_EDIT_KEY")
    if realm is None:
        return "UNRESOLVED_NAMESPACE", (), ()
    if not nonblank(realm):
        raise ValueError("INVALID_NAMESPACE")
    if event_range is None:
        return "UNRESOLVED_TIME_BOUND", (), ()
    if (not isinstance(event_range, tuple) or len(event_range) != 2
            or any(type(x) is not int for x in event_range)
            or not 0 <= event_range[0] <= event_range[1] < 1440):
        raise ValueError("INVALID_EVENT_RANGE")
    low, high = event_range
    possible, all_times = [], []
    for row in rows:
        if row.realm != realm or row.account != account:
            continue
        if key and key != row.key:
            continue  # Never discard a supplied key to force a match.
        label = row.realm + "/" + row.key
        if low < row.end and high >= row.start:
            possible.append(label)
            if row.start <= low and high < row.end:
                all_times.append(label)
    status = "CANDIDATES_IN_SUPPLIED_ROWS" if possible else "NO_MATCH_IN_SUPPLIED_ROWS"
    return status, tuple(sorted(possible)), tuple(sorted(all_times))

CASES = (
    ("QUALIFIED_KEY", SESSIONS, "realm-a", "K7", (547, 547)),
    ("KEY_ABSENT", SESSIONS, "realm-a", "", (547, 547)),
    ("NAMESPACE_UNKNOWN", SESSIONS, None, "K7", (547, 547)),
    ("AT_EXCLUSIVE_END", SESSIONS, "realm-a", "K7", (552, 552)),
    ("BOUNDARY_UNCERTAIN", SESSIONS, "realm-a", "", (551, 553)),
    ("BOUND_UNKNOWN", SESSIONS, "realm-a", "K7", None),
    ("OMITTED_K7", (SESSIONS[0],), "realm-a", "K7", (547, 547)),
    ("EMPTY_PACKET", (), "realm-a", "K7", (547, 547)),
    ("DUPLICATE_KEY", SESSIONS + (SESSIONS[1],), "realm-a", "K7", (547, 547)),
    ("FALSE_KEY", SESSIONS, "realm-a", 0, (547, 547)),
    ("REVERSED_RANGE", SESSIONS, "realm-a", "K7", (553, 551)),
)

for name, rows, realm, key, bounds in CASES:
    try:
        status, possible, all_times = correlate(rows, realm, "desk-x", key, bounds)
    except ValueError as exc:
        print(f"{name}: {exc}")
    else:
        print(f"{name}: {status} possible={','.join(possible) or '-'} "
              f"all_times={','.join(all_times) or '-'}")
```

The central decision model can be read without Python; an empty packet also stops with an unresolved result:

```text
Validate the supplied rows and field types
        | invalid                         | valid
        v                                 v
Report input defect              Namespace and time bound supplied?
                                          | no                | yes
                                          v                   v
                                     Unresolved       Filter realm and account
                                                              |
                                                     Keep any explicit key
                                                              |
                                                  Compare the two time tests
                                                              |
                                              Report sets AND remaining limits
```

**Text equivalent:** Malformed input cannot support a match. Missing namespace or time information produces an unresolved result. Otherwise preserve the stated realm, account and any explicit key, compute possible and all-times sets, and explain their limits. No branch approves collection, selects a human actor or triggers containment. The implementation reports the first applicable problem rather than proving every untested field valid.

##### Practice, evidence and assessment

Keep the original Q1 six-point task unchanged. For this separate **Q1-S practice**, submit the eleven-line transcript and an eleven-row ledger with `case | what changed | result | blocked conclusion | smallest repair or follow-up`. Then solve four variations without changing the original packet: **(A)** set the key to K7 in the boundary-uncertain case; **(B)** use K7 with the exact range `(542, 542)`; **(C)** use K7 with `(552, 553)`; **(D)** reverse the input row order for the qualified-key case. For each, predict both candidate sets or the reason no test is possible.

Finally, write one bounded request identifying the source/realm mapping, permitted non-secret correlation fields, event and collection ranges, clock-bound evidence, relevant export omissions and approval owner. Do not request every account or supply a real token. Record which parts of the request are proposals rather than received evidence.

**Supplemental rubric, six points:** one point for the eleven reproduced lines; one for distinguishing qualified keys and refusing an unknown realm; one for correctly deriving both time tests and the four variations; one for distinguishing invalid input, unresolved prerequisites and no match in a nonempty packet; one for explaining why a unique all-times row does not eliminate a second possible row; and one for the minimal authorized request with explicit source and attribution limits. These points assess Q1-S only. They do not add a numbered EX identifier, change the course's existing 0–2 exercise rubrics or certify an operational investigation.

**Synthesis:** A useful correlation result states its identity namespace, selection, time assumptions and remaining alternatives. Type checks keep malformed inputs out of the calculation; they do not authenticate evidence. A possible set is not a probability distribution, and an all-times set is not a list of proven actors. Continue with the existing quiet-query laboratory to examine the separate question of source coverage.

<a id="ir-rapid-ch02-vq2-lab"></a>

### 2.10 Offline laboratory: when is a quiet-query claim defensible?

Award the six rubric points only when the candidate sets, limits, authorized request and variant are all present. The table and code use the same half-open interval rule, so an event exactly at S-A's 09:15 end would not match S-A. A reviewer who uses an inclusive end, silently discards E-D's explicit key or reads R13's canonical one-session summary into Q1 has changed the stated exercise input and must revise the answer. This lab is supplementary; the book still contains exactly 50 numbered exercises.

<a id="ir-rapid-ch02-q1-scope-result"></a>

### Q1-S — Qualified keys and clock sensitivity: worked result

Read the [Q1-S lesson and complete program](#ir-rapid-ch02-q1-scope) before this answer. The following eleven lines were reproduced from that program with Python 3.13.5. They describe invented inputs only.

```text
QUALIFIED_KEY: CANDIDATES_IN_SUPPLIED_ROWS possible=realm-a/K7 all_times=realm-a/K7
KEY_ABSENT: CANDIDATES_IN_SUPPLIED_ROWS possible=realm-a/K6,realm-a/K7 all_times=realm-a/K6,realm-a/K7
NAMESPACE_UNKNOWN: UNRESOLVED_NAMESPACE possible=- all_times=-
AT_EXCLUSIVE_END: NO_MATCH_IN_SUPPLIED_ROWS possible=- all_times=-
BOUNDARY_UNCERTAIN: CANDIDATES_IN_SUPPLIED_ROWS possible=realm-a/K6,realm-a/K7 all_times=realm-a/K6
BOUND_UNKNOWN: UNRESOLVED_TIME_BOUND possible=- all_times=-
OMITTED_K7: NO_MATCH_IN_SUPPLIED_ROWS possible=- all_times=-
EMPTY_PACKET: UNRESOLVED_EMPTY_PACKET possible=- all_times=-
DUPLICATE_KEY: DUPLICATE_QUALIFIED_KEY
FALSE_KEY: INVALID_EDIT_KEY
REVERSED_RANGE: INVALID_EVENT_RANGE
```

| Case | Reason for this result | Conclusion that remains blocked |
|---|---|---|
| QUALIFIED_KEY | Realm-a, K7, desk-x and 547 agree with one supplied row; realm-b/K7 is excluded before comparing time | The matching label does not authenticate a session, identify a person or approve the edit |
| KEY_ABSENT | At 547, both realm-a intervals contain the event; the absent key does not choose between them | Two candidates are not a 50/50 probability estimate |
| NAMESPACE_UNKNOWN | The required realm mapping is missing; the program does not search all realms | Empty output sets here do not mean no session matched a completed query |
| AT_EXCLUSIVE_END | 552 equals K7's excluded end; `552 < 552` is false | This does not prove no session existed in an unexamined source |
| BOUNDARY_UNCERTAIN | Both intervals intersect `[551,553]`, but only K6 contains the entire range | K6's unique all-times status does not eliminate the still-possible K7 |
| BOUND_UNKNOWN | No comparable event range is supplied; zero uncertainty is not assumed | Neither an exact match nor an exact temporal exclusion is justified |
| OMITTED_K7 | The variant deliberately supplies only K6 while the edit retains explicit K7 | A missing input row is not evidence that its session never existed; do not fall back to K6 |
| EMPTY_PACKET | No session rows were supplied, so the program records the missing input | It does not report a completed search of a real source |
| DUPLICATE_KEY | Realm-a/K7 occurs twice, violating this packet's declared uniqueness contract | The repetition does not prove two sessions or malicious duplication |
| FALSE_KEY | Integer zero is not a string, even though Python treats it as false in a conditional | It must not silently become the fixture's missing-key marker |
| REVERSED_RANGE | The lower event bound is greater than the upper bound | A malformed range cannot establish absence or malicious activity |

**Derive the decisive example.** For K6, `551 < 555` and `553 >= 540`, so it is possible; `540 <= 551` and `553 < 555`, so it also covers all times. For K7, `551 < 552` and `553 >= 542`, so it remains possible; `553 < 552` is false, so it does not cover all times. If the event were at 09:11, both would survive. If it were at 09:13, only K6 would survive. Nothing supplied chooses between those event times.

The four additional practice variations produce:

```text
A: CANDIDATES_IN_SUPPLIED_ROWS possible=realm-a/K7 all_times=-
B: CANDIDATES_IN_SUPPLIED_ROWS possible=realm-a/K7 all_times=realm-a/K7
C: NO_MATCH_IN_SUPPLIED_ROWS possible=- all_times=-
D: CANDIDATES_IN_SUPPLIED_ROWS possible=realm-a/K7 all_times=realm-a/K7
```

**A** retains explicit K7 and the range `[551,553]`: K6 is excluded by the key, while K7 intersects but does not contain the range. **B** is exactly at K7's included start, 542. **C** begins at its excluded end, 552, and therefore does not overlap it at all. **D** reverses the packet order; the same qualified match and sorted output remain. Row order is not a tie-breaker for this model. These variations change only the stated input, not the historical Q1 or Harbor Library record.

**Bounded-request model:** “Within the approved investigation scope, ask the identity and application custodians to document the relevant realm/issuer mapping and provide only the authorized non-secret correlation aliases, account identifiers and time-bounded rows needed for this comparison. Include the original timestamp meanings, collection/query bounds, evidence for any comparable-clock error bound, and known omitted rows or transformations. The incident lead must authorize any additional acquisition through the approved route; until the response arrives, namespace, coverage and clock claims remain unresolved. No human attribution, task approval or retention deadline is established by these candidate sets.” This is a proposed request, not a collection receipt or permission to operate on a live service.

**Diagnostic follow-up:** For an unknown realm, seek a source-schema mapping; for an unknown clock bound, seek clock evidence rather than inventing a tolerance. For the deliberately omitted K7, retain the original packet and the separately labeled variant. For a duplicate qualified key, investigate whether the export repeated a row or whether the key's stated uniqueness scope is wrong; do not choose the first row to make the result pass. For a type error or reversed range, retain the rejected input and request a corrected, versioned packet.

A full-credit explanation must keep these cases distinct. Syntax validation is not source authentication; a queried subset is not complete coverage; and a candidate relationship is not an identified actor. The [original Q1 lesson](#ir-rapid-ch02-q1-lab) and its six-point task remain unchanged. This supplemental answer creates no additional numbered exercise and no claim that the book's complete editorial gate has passed.

### EX027 — Worked result
