# Chapter 2 early technical corrections — integration draft

**State:** DRAFT correction blocks, not an additional chapter or an approved book.  
**Authorship and editorial responsibility:** hiagokinlevi.  
**Language:** English. **Edition date:** 2026-10-13.  
**Target:** `levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md`, sections 2.1–2.8 only, before 2.8a, and the specified exercise/answer corrections below.  
**Source snapshot:** commit `fcb36b6041774a1b87277d2aaade436235bf7a2d`; manuscript Git blob `3885de447fee9d3b5b89787e753a239cce061355`.

[Principal manuscript](../MANUSCRIPT.md#ch-02) · [Book standard](../../../../../../BOOK_STANDARD.md) · [Rights](../../../../../../RIGHTS.md)

Integrate by the named headings and exact textual boundaries, not by historical line numbers. Retain intervening manual changes. The numbered correction blocks below are editorial units, not exercise IDs. Preserve EX014–EX019, their original artifact sizes and the common 0–2 rubric; preserve the existing MIN2 and HOLD2 extensions unless a replacement is expressly identified. No operational collection, source hold, containment, disposal, translation or book approval follows from this draft.

## C01 — Reported retention policy is not an observed deletion outcome

**Integration 1:** In section 2.1's question table, replace only the last cell of the row beginning “Can the logs be trusted and retained?” with:

Record the source, requested event range and proposed collection method; ask the custodian to confirm present availability, retention anchor and any actual deadline. Mark an unverified deadline unknown.

**Integration 2:** In section 2.2a.6, replace the paragraph beginning “At 09:20, R15 raises a preservation concern:” with:

At 09:20, R15 supplies a **reported policy** for detailed booking-audit records: a 24-hour duration with an authorized-copy provision. It does not demonstrate the policy's enforcement, its starting anchor, the oldest retrievable relevant row, or an actual deletion. The time-sensitive task is to ask the incident lead and application custodian about a bounded preservation route and current source availability. Do not add 24 hours to R9's event time or treat the 09:14 notice time as a new retention start. A retained copy, if later authorized and actually acquired, would have its own custody and retention record; its existence would not by itself show that deletion at the producing source stopped. Preservation concern is therefore justified without a confirmed loss outcome or a conclusion that an attack occurred.

**Integration 3:** In section 2.4, under “Worked 09:20 preservation queue,” replace the introductory paragraph beginning “The learner has received R9–R16” and ending “It does not add evidence to R9–R16.” with:

The learner receives R9–R16 at the **simulated 09:20 review**. R9 reports a 09:03 edit, but was not available for the learner's 09:05 decision. R15 reports a 24-hour policy concerning detailed booking-audit records, not a measured countdown or a completed deletion. The policy anchor, oldest-row availability, enforcement behavior and any authorized copy or source hold remain unconfirmed. Ask the custodian what the copy provision means in this source's actual procedure; do not assume that saving an export changes the source's removal mechanism. The queue records **proposed requests**, not approvals or completed preservation. R15's rule must not be borrowed for R14's separately labeled application-audit source, R11's help-desk record or R13's identity source without an explicit custodial mapping and policy confirmation.

**Integration 4:** In section 2.3, under “Prioritize a preservation request before copying,” replace the paragraph beginning “The queue has four distinct states:” with:

For a **copy request**, distinguish four states: **proposed**, a bounded request has been written; **approved**, an accountable owner has authorized its stated scope; **collected**, a specified copy has actually been acquired with an acquisition receipt; and **verified**, a reviewer has performed and recorded specified checks on that item. State what was verified: bytes, selection, provenance or another named property, not “everything.” Protecting records in place does not itself move a copy request to collected. A source-hold request follows a separate control lifecycle, including reported application and a bounded effect check where such a mechanism exists. Neither lifecycle substitutes for the other. Record each actual state change, actor, time and source pointer; leave missing receipts pending. This is the book's teaching model, not a required NIST form. The relevant NIST principles concern recording investigative actions and preserving the integrity and provenance of incident information under organizational procedures; see [SP 800-61 Rev. 3, RS.AN-06 and RS.AN-07](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf).

**Integration 5:** Under EX016, replace only the paragraph labeled “Additional IM2 discriminator for EX016” with:

**Additional IM2 discriminator for EX016:** At Round B, distinguish the R15 concern about **detailed booking-audit records relevant to R9** from the retention of R11's help-desk report or R13's identity source, whose policies are not supplied. Separately assess potential booking harm, uncertain cause and the absence of a measured affected-patron total. The independent IM2 fixture supplies no Harbor Library outcome. Keep the same short decision note and 0–2 rubric.

## C02 — Match each hypothesis and test to the exact field in dispute

**Integration 1:** In section 2.4, replace only the paragraph beginning “**Step 1: state observations.**” and ending “Set a near-term review time and revisit containment if changes resume or harm expands.” with the following worked explanation. Retain the R9–R16 table and the subsequent 09:20 decision table.

**Step 1: distinguish the operation from the reported symptom.** R9 is labeled **booking audit** and reports a change to B19's **room**, from Room 1 to Room 3. R11 is a help-desk report that B19's **time** looked wrong. The shared booking ID makes a bounded comparison useful; it does not make these the same field or establish that the room change caused the time complaint. R14 is separately labeled **application audit**. Confirm source identity and field semantics before treating R9 and R14 as one continuous log.

**Step 2: split the hypotheses into testable propositions.** H1 asks whether the relevant edits were within scheduled training. R10's plan names B17/B18, not B19; R12 is a recollection rather than an exhaustive approval record. H2 asks whether the B19 operation fell outside the approved task set. Neither proposition directly identifies the person controlling the account. Ask the training owner for the complete applicable plan, version, effective approval time and any B19 addendum. A document received at 09:20 may describe an earlier approval; its arrival time alone neither validates nor invalidates that earlier authority. A newly issued retrospective approval must not be presented as permission that existed at 09:03.

H3 addresses the patron's reported display or synchronization problem. Test the reported **time** separately from the audited **room** change. A proposed comparison should identify B19, the exact field, an owner-approved target and version, the authoritative stored value and its observation time, and the patron-facing value with its own observation time. None of these comparison values is supplied by R1–R16. The following are conditional interpretations, not new case facts:

| Future comparison, if authorized and adequately evidenced | Narrow conclusion | Remaining limitation |
|---|---|---|
| The relevant patron view differs from the authoritative stored time, while that stored time agrees with the applicable approved target | Supports a discrepancy between those observed representations | Does not establish the synchronization mechanism or explain the room edit |
| Contemporaneous view and stored time agree with each other but both differ from the applicable target | Weakens a display-only explanation for that observed state; supports a bounded target/state discrepancy | Does not establish its cause or exclude a separate earlier transient display problem |
| A target, version, relevant observation time or trustworthy source is missing | The proposed comparison remains unverified | Neither “correct” nor “corrupted” is warranted from the complaint alone |

A later correct view cannot, without historical evidence, prove that the earlier complaint was mistaken. Likewise, a room mismatch does not independently corroborate a time-field complaint. Keep the observations, hypothesized relationship and unanswered question separate.

**Step 3: request the smallest discriminator that can change the decision.** The training owner can address task authorization; the service owner and application custodian can define the bounded field comparison; the identity custodian can address a separately authorized session-correlation question. An identity-summary request cannot substitute for an approved-task-list check. Request source availability and preservation in parallel where justified by R15, without declaring an export, hold or loss. The incident lead retains the 09:35 review, or an earlier review on a separately verified new unexplained edit or substantiated source-availability concern. No account or service change is authorized merely by producing this analysis.

**Integration 2:** Under EX015, immediately after its original objective/inputs/output paragraph, insert this constraint, without adding an exercise or changing its three-row format:

**Discriminator check:** In each row, the named check must be capable of producing the stated weakening result. Identify the correct producer and field: R9 reports a booking-audit room change, whereas R11 reports a time-display concern. A task-approval document and identity-session detail answer different questions. This is a requirement within the existing three-row artifact and 0–2 rubric.

**Integration 3:** Replace only the two-row table under “EX014 — Worked result.” Retain its subsequent evidence-layer explanation.

| Answerable question | Supplied starting point | Authorized next source | Result that changes triage |
|---|---|---|---|
| Was the B19 room-change task within the approved training scope effective at 09:03? | R9 reports the room change; R10 lists B17/B18 but not B19 | Training owner supplies the complete applicable approved plan/version and any B19 addendum through the authorized case route | A valid, applicable B19 task approval strengthens the task-scope explanation; a confirmed complete set excluding B19 weakens it. Neither identifies the operator. |
| What, if anything, is wrong with the selected B19 room and reported time representations? | R9 reports a room edit; R11 reports a time concern; R16 requests impact assessment | Service owner authorizes a narrow, field-specific comparison; application custodian supplies time-stamped authoritative values and the relevant view against approved targets | A supported match, mismatch or missing comparator changes the bounded impact assessment. Further bookings require justified scope; no population count or common cause follows automatically. |

**Integration 4:** Replace only the three-row table under “EX015 — Worked result.” Retain the statement that the hypotheses need not be mutually exclusive.

| Hypothesis | Support | Contradiction or limit | Narrow authorized check | Result that weakens it |
|---|---|---|---|---|
| H1: scheduled training explains the edits | R6 records training; R10 names B17/B18 | R10 omits B19; R12's recollection is incomplete | Training owner supplies the complete approved task set and addenda applicable to the B19 operation | A confirmed complete applicable set excludes B19, weakening training as an explanation of all recorded edits |
| H2: B19 account use fell outside the approved task set | R9 records B19 changed under desk-a; R10's supplied plan omits B19 | Plan completeness and applicable approval are unconfirmed; R13 does not identify a human | Training owner verifies whether the exact B19 task was approved at the relevant time; request session detail separately only for a defined correlation question | A verified applicable task approval explicitly covering the B19 room change weakens the outside-plan proposition, without proving who acted or whether the resulting state was correct |
| H3: the reported time symptom reflects a display or synchronization discrepancy | R11 reports that B19's time looked wrong | No time-field comparison is supplied; R9 records a room change, not a demonstrated time-display fault | Service owner authorizes a time-aligned comparison of the relevant view, stored time and applicable approved time target | Contemporaneous view and stored time agreeing with each other but differing from the target weakens a display-only account of that observed discrepancy; an earlier transient fault remains unresolved |

## C03 — Make TRI2's input guards match its declared boundaries

**Integration:** Apply the four code fragments below inside section 2.2b's existing complete Python block. They are **integration fragments, not standalone programs**: the helper requires `BASE` and `RELEASE`; the other fragments require that helper and the existing program. Keep the original source-release guards, twenty baseline cases and assertions. Run the assembled program from the beginning in a fresh Python session.

First, insert this helper after the `BASE = dict(...)` definition and before `def review(s):`.

~~~python
def validate_tri2_input(s):
    """Validate this classroom packet, not a real evidence source."""
    if not isinstance(s, dict) or set(s) != set(BASE):
        return "BLOCK_INPUT_SCHEMA"
    if not isinstance(s["stage"], str) or s["stage"] not in RELEASE:
        return "BLOCK_UNKNOWN_STAGE"
    refs = s["refs"]
    if not isinstance(refs, (tuple, list)):
        return "BLOCK_SOURCE_LIST_TYPE"
    if not refs:
        return "BLOCK_EMPTY_SOURCE_SET"
    if any(not isinstance(ref, str) for ref in refs):
        return "BLOCK_SOURCE_ID_TYPE"
    if len(set(refs)) != len(refs):
        return "BLOCK_DUPLICATE_SOURCE_ID"
    for field in BASE:
        if field not in ("stage", "refs") and type(s[field]) is not bool:
            return "BLOCK_NON_BOOLEAN:" + field
    return None
~~~

Second, replace only the line `def review(s):` with the following function opening. Leave the original body immediately beneath it at its existing indentation.

~~~python
def review(s):
    problem = validate_tri2_input(s)
    if problem is not None:
        return problem
~~~

Third, replace the existing canonical-premise guard beginning `if not s["variant"] and any((` with the following. Keep it **after** the existing source-release and canonical fresh-edit checks, and before the bounded-negative check.

~~~python
    if not s["variant"] and any((
        s["owner_state_check"], s["source_safeguard_confirmed"],
        s["approved_addendum"], s["no_new_edits_verified"],
        s["query_coverage_known"], s["retention_anchor_known"],
        s["training_scope_verified_complete"], s["addendum_names_b19"],
        not s["custodian_available"],
    )):
        return "BLOCK_INVENTED_CANONICAL_PREMISE"
~~~

Fourth, append these independent controls after the program's existing assertions.

~~~python
controls = [
    ("EMPTY_SOURCE_SET", {**ROUND_A, "refs": (), "patron_report": False}),
    ("TEXT_FALSE", {**BASE, "variant": "False", "owner_state_check": True}),
    ("CANONICAL_ANCHOR", {**BASE, "retention_anchor_known": True}),
    ("CANONICAL_COVERAGE", {**BASE, "query_coverage_known": True}),
    ("CANONICAL_CONTACT", {**BASE, "custodian_available": False}),
]
for label, sample in controls:
    print(label + " " + review(sample))
~~~

**Terminology replacement:** In section 2.2b and its matching final TRI2 worked result only, replace the exact token `VALID_B19_CAUSE_DOWNGRADE` with `VALID_B19_TASK_SCOPE_DOWNGRADE`, and `DOWNGRADE_ONLY_B19_CAUSE_CONCERN` with `DOWNGRADE_ONLY_B19_TASK_SCOPE_CONCERN`. Apply this to the case label, code flag, two affected baseline transcript lines and their interpretation. Preserve the explicit TRI2 anchors. These are task-scope checks, not proof of a causal mechanism or human actor. All twenty baseline cases retain their conclusions; only those literal names change.

**Insert after the existing release-guard challenge:** The original three release-guard controls remain required. The five additional controls above test a different boundary: the input schema and the distinction between fixed canonical metadata and separately labeled variants. An empty reference list cannot claim that records were supplied. The text `"False"` is not a Boolean false value; accepting it as a variant marker would admit invented impact into what a reader might mistake for the canonical packet. R15 does not supply an anchor, R14 does not supply complete coverage, and R1–R16 do not report a failed custodian contact. Those altered premises must not silently enter the canonical case.

`custodian_available=True` in the original baseline remains a **model default**, not a verified successful contact. The default produces no collection or hold receipt. Requiring a separately labeled variant for a failed-contact scenario does not authenticate the default; both real contact status and any real preservation result remain unmeasured.

A declared variant can still contain an invented `owner_state_check=True` or source-safeguard flag. These guards do not verify those assertions. They validate classroom structure and provenance boundaries, not source truth, actual harm, probability, severity or permission. TRI2 remains an original CyberABC method rather than a NIST classification policy; [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) provides high-level outcomes, not these particular labels or thresholds.

**Worked-result insertion:** Immediately after the existing three-line “Supplementary release-guard challenge result” in the final TRI2 answer, add the following five-line transcript and interpretation. These lines were reproduced with the assembled Python program; they supplement rather than replace the twenty baseline lines and the three original release controls.

~~~text
EMPTY_SOURCE_SET BLOCK_EMPTY_SOURCE_SET
TEXT_FALSE BLOCK_NON_BOOLEAN:variant
CANONICAL_ANCHOR BLOCK_INVENTED_CANONICAL_PREMISE
CANONICAL_COVERAGE BLOCK_INVENTED_CANONICAL_PREMISE
CANONICAL_CONTACT BLOCK_INVENTED_CANONICAL_PREMISE
~~~

The first result rejects a positive source-availability description with no cited records. The second rejects a string before Python truthiness can turn it into a supposed variant authorization. The remaining controls reject unsupported changes to the canonical retention, query-coverage and contact premises. A blocking result identifies an input inconsistency, not a deleted source, an observed attack or a production action. Preserve the five-point supplementary lab rubric: assess these controls within its existing evidence-boundary and unsupported-claim criterion. No EX identifier is added.

## C04 — Name the clocks and reject ambiguous normalization inputs

**Integration 1:** In section 2.3, replace the entire subsection headed “Four-clock ledger and learner release,” stopping immediately before section 2.4, with the following subsection.

#### Source time, arrival, visibility, query, release and collection

A timestamp must identify both **whose clock** it uses and **what transition** it describes. A useful ledger distinguishes these fields:

| Field | Meaning and boundary |
|---|---|
| Source event or source-record time | When the source reports an operation, document observation or notice; identify which kind rather than calling every card time an operation time |
| Receiver arrival time | When a named collector or transport accepted a record, if actually measured |
| Query-visible time | When the selected store/index could return the record; an upstream arrival receipt need not establish search visibility |
| Query run time and selection | When the query ran, separately from its source, filters and selected event-time interval |
| Learner release or analyst discovery | When the classroom permitted use of a card; in a real case, record receipt and recognition separately where they differ |
| Copy acquisition time | When a particular export or local teaching copy was actually acquired or created, not when its represented event occurred |

Source clocks can be wrong, and pipeline implementations differ. A field called `ingested_at` needs a documented producer meaning: it might represent receipt, storage acceptance or indexing. Do not silently substitute one for another. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) discusses log generation, transmission, storage and use; this particular ledger is the book's instructional method, not a NIST schema.

In the canonical Round B packet, R9 reports a 09:03 booking edit; R10 has a 09:04 **plan-record** timestamp, not a verified approval time; R15 has a 09:14 **notice** timestamp, not a retention start; R16 has a 09:16 owner-note timestamp, not an executed account change. All four become available to the learner at 09:20. Their actual receiver-arrival, indexing and acquisition times are not supplied. R14's printed 09:12 is the supplied card's time, not a complete query-execution manifest. Only the explicitly hypothetical T1 card assigns a 09:12 query run and its particular event window.

The difference from a source-card time to 09:20 is therefore a **source-to-learner-release interval**, not a measured transport or ingestion delay. Preserve the original text and offset, the normalized UTC value, its source-time kind and the release boundary. [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) documents date-time representations and offsets; an offset does not authenticate a clock or reconstruct a missing timestamp. R9 remains unavailable to the 09:05 R1–R8 decision despite its earlier event time.

**Integration 2:** In section 2.6, replace its complete Python block with the complete program below. Keep T1, the original three-row learner table, half-open coverage task and five-point rubric. In surrounding procedure/result wording, use “source-to-learner-release interval” rather than treating R10/R15 as operation times. Replace the old “Time-label clarification” paragraph with the contract following this program.

~~~python
from datetime import datetime, timedelta, timezone

rows = [
    ("R9", "2026-10-11T09:03:00+00:00", "2026-10-11T09:20:00+00:00"),
    ("R10", "2026-10-11T05:04:00-04:00", "2026-10-11T09:20:00+00:00"),
    ("R15", "2026-10-11T09:14:00+00:00", "2026-10-11T09:20:00+00:00"),
]

def utc(text):
    try:
        value = datetime.fromisoformat(text)
    except (TypeError, ValueError) as exc:
        raise ValueError("INVALID_TIMESTAMP") from exc
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("OFFSET_REQUIRED")
    return value.astimezone(timezone.utc)

def release_interval(source_text, release_text):
    source, released = utc(source_text), utc(release_text)
    if source > released:
        raise ValueError("SOURCE_AFTER_RELEASE")
    if any(value.second or value.microsecond for value in (source, released)):
        raise ValueError("MINUTE_PRECISION_REQUIRED")
    minutes = (released - source) // timedelta(minutes=1)
    return source, released, minutes

for record_id, source_text, release_text in rows:
    source, released, minutes = release_interval(source_text, release_text)
    print(
        f"{record_id} source={source:%H:%M} UTC "
        f"released={released:%H:%M} UTC interval={minutes} min"
    )

# Independent malformed-input controls, not additional R-series facts.
for label, text in (
    ("NO_OFFSET", "2026-10-11T09:03:00"),
    ("FUTURE_SOURCE", "2026-10-11T09:21:00+00:00"),
    ("BAD_CLOCK", "2026-10-11T25:03:00+00:00"),
    ("SUB_MINUTE", "2026-10-11T09:03:30+00:00"),
):
    try:
        release_interval(text, rows[0][2])
    except ValueError as exc:
        print(f"{label}: {exc}")
    else:
        raise AssertionError(label + " was not rejected")
~~~

**Time-label clarification and input contract:** `source` means the source-card time: an edit for R9, a plan record for R10, and a retention notice for R15. `released` means the learner's 09:20 release. The dates and offsets are the existing synthetic fixture, not new case evidence. This minute-aligned exercise requires an explicit UTC offset and refuses a source timestamp later than its release under the assumed comparable clocks. It rejects sub-minute values rather than silently rounding them. This is not a general RFC 3339 validator or a real clock-verification tool. In particular, Python's [datetime documentation](https://docs.python.org/3.13/library/datetime.html#datetime.datetime.astimezone) explains that converting a naive datetime can use the machine's local timezone; this program rejects that ambiguity before conversion.

Predict the original three intervals and all four rejection reasons before running. None of the malformed-input controls is an R-series event. A chronological rejection calls for investigation of timestamp meaning and clock assumptions; it does not establish malicious activity. Keep ingestion, query execution and copy creation unknown when they have no separate evidence.

**Integration 3:** In the final “Chapter 2 temporal-coverage lab — worked result,” replace the original three-line transcript with these seven lines, and replace its arithmetic paragraph with the paragraph following them. Retain its bounded T1 interpretation.

~~~text
R9 source=09:03 UTC released=09:20 UTC interval=17 min
R10 source=09:04 UTC released=09:20 UTC interval=16 min
R15 source=09:14 UTC released=09:20 UTC interval=6 min
NO_OFFSET: OFFSET_REQUIRED
FUTURE_SOURCE: SOURCE_AFTER_RELEASE
BAD_CLOCK: INVALID_TIMESTAMP
SUB_MINUTE: MINUTE_PRECISION_REQUIRED
~~~

R10's explicit `05:04-04:00` normalizes to 09:04 UTC. The source-to-release intervals remain 17, 16 and 6 minutes; they do not measure logging-pipeline delay. The controls reject a missing offset, a source time after the release, an invalid hour and an input finer than the stated minute precision. Rejecting the last input is a teaching-contract choice, not a claim that real logs should discard seconds. The same complete program produced the same seven lines under both UTC and America/New_York host timezone settings. This does not validate any production clock.

## C05 — T2: valid clock syntax does not establish complete coverage

**Integration 1:** In section 2.7, replace the paragraph beginning “This optional Python 3 standard-library program performs only” and its following complete Python block with this introduction and program. Retain the L1–L4 table, original half-open selection and subsequent worked reasoning.

This optional program operates only on the in-memory T2 fixture. Its last column is treated as **query-visible time**; T2 assumes no additional delay between the listed ingestion and search visibility. This simplifying assumption must not be applied to a real collector without checking its semantics. All rows use one fictional UTC day and comparable accurate clocks. The parser validates `HH:MM`, and the program rejects a row visible before its event under those assumptions. It validates the whole supplied packet before filtering, so an irrelevant account cannot hide malformed timestamps. It is still not a production parser, a transport simulation or an ingestion-completeness check.

~~~python
import re

rows = (
    ("L1", "desk-a", "09:03", "09:04"),
    ("L2", "desk-a", "09:10", "09:18"),
    ("L3", "helper-b", "09:11", "09:11"),
    ("L4", "desk-a", "09:12", "09:13"),
)

def minute(text):
    if not isinstance(text, str) or not re.fullmatch(r"[0-9]{2}:[0-9]{2}", text):
        raise ValueError("BLOCK_INVALID_HHMM")
    hour, minute_part = map(int, text.split(":"))
    if not (0 <= hour <= 23 and 0 <= minute_part <= 59):
        raise ValueError("BLOCK_INVALID_HHMM")
    return hour * 60 + minute_part

def visible_at(query_time, sample_rows=rows):
    query = minute(query_time)
    validated = []
    # Validate the supplied packet before applying account/time filters.
    for row_id, account, event_time, visible_time in sample_rows:
        event, visible = minute(event_time), minute(visible_time)
        if visible < event:
            raise ValueError("BLOCK_VISIBILITY_BEFORE_EVENT:" + row_id)
        validated.append((row_id, account, event, visible))
    return [
        row_id for row_id, account, event, visible in validated
        if account == "desk-a"
        and minute("09:00") <= event < minute("09:12")
        and visible <= query
    ]

for query_time in ("09:12", "09:20"):
    print(query_time, ",".join(visible_at(query_time)))

for label, query, sample in (
    ("BAD_MINUTE", "09:12", rows + (("X", "desk-a", "08:63", "09:04"),)),
    ("INVALID_QUERY", "25:99", rows),
    ("VISIBLE_BEFORE_EVENT", "09:12",
     rows + (("X", "desk-a", "09:10", "09:00"),)),
):
    try:
        visible_at(query, sample)
    except ValueError as exc:
        print(f"{label}: {exc}")
    else:
        raise AssertionError(label + " was not rejected")

without_l2 = tuple(row for row in rows if row[0] != "L2")
print("OMITTED_L2:", ",".join(visible_at("09:20", without_l2)))
assert rows[1] == ("L2", "desk-a", "09:10", "09:18")
~~~

**Insert after that code:** Predict the original two query results, the three malformed-input rejections and the omitted-row control. `08:63` must not be normalized accidentally to 09:03; `25:99` is not a valid query clock. An earlier visibility time contradicts this fixture's declared clock contract. In real evidence, such a discrepancy could instead reflect a misunderstood field or source clock and would need investigation.

The `OMITTED_L2` case is equally important: every remaining field is well formed, but the later query returns only L1 because L2 was removed from that variant's input. Syntax validation cannot discover a record it was never given. Retain the complete original packet separately. Neither a successful parser run nor a repeated quiet query establishes source completeness. These controls remain outside canonical R1–R16 and add no exercise ID. Assess their reasoning within the existing five-point T2 rubric's timing, exclusion and bounded-follow-up criteria.

**Integration 2:** In the final “Chapter 2 delayed-arrival T2 replay — worked result,” replace the two-line transcript with the following six lines. Keep the existing explanation of L1–L4 and append the interpretation below.

~~~text
09:12 L1
09:20 L1,L2
BAD_MINUTE: BLOCK_INVALID_HHMM
INVALID_QUERY: BLOCK_INVALID_HHMM
VISIBLE_BEFORE_EVENT: BLOCK_VISIBILITY_BEFORE_EVENT:X
OMITTED_L2: L1
~~~

The first two lines are unchanged: the late L2 becomes visible without moving its 09:10 event time; L4 remains excluded at the 09:12 exclusive end. The next three lines demonstrate input rejection, not observed incident events. The last line comes from a separate packet lacking L2: its quiet result is compatible with missing input and cannot prove no matching event occurred. Source coverage requires independent, appropriately authorized evidence about the producer, collection/index path and selection, not just successful filtering of available rows.

## C06 — E1 partial creation and retention must have honest states

**Integration 1:** In section 2.5, insert the following immediately after the existing Python block. Do not change its payload, filenames, exclusive-create modes, two original output lines or SHA-256 values.

**Failure-path check: two exclusive creations are not one atomic transaction.** The required new empty directory avoids ordinary filename collisions. Python's [exclusive-create file mode](https://docs.python.org/3.13/library/functions.html#open) refuses to overwrite an existing target, but each call protects only its own file. In a separately labeled failure rehearsal where only `E1-modified.txt` already exists, the first write can create E1 and print its digest before the second write raises `FileExistsError`. That is a **partial local attempt**, not completion of both files and not an overwrite of the pre-existing file. Record which file was actually created, which operation failed and what was left unchanged. Stop; do not delete the existing object or switch to an overwrite mode to obtain the expected transcript. A new authorized empty directory permits an independent attempt with its own recorded state.

For a collection note, record the actual local time when the creation is performed. A recorded start/end interval may honestly bound the operation; a later observation time or filesystem timestamp with unverified semantics must not be relabeled as an exact creation receipt. When a time was not recorded, say so. The synthetic 09:20 review does not supply a local acquisition time.

**Integration 2:** In the final “Chapter 2 synthetic-extract lab — worked result,” replace the entire paragraph beginning “A model note is:” with the following paragraph. Keep the preceding 235-byte counts and both digests unchanged.

A completed-run model note must be populated from the learner's actual work: “HL-IR-001/E1; local teaching transcription of R9 and R14, not a production export; original source retained in this public book; learner-created E1.txt in the recorded authorized scratch location; actual local creation time or recorded operation interval attached, or explicitly not recorded; classroom scope limited to the supplied synthetic material; 235 bytes and the measured SHA-256 value attached; access limited to the permitted learner/reviewer; retention and any disposal remain subject to the authorized exercise procedure.” This is a template, not evidence that the learner ran the program. A planned or partially failed attempt must keep its actual state. Do not claim deletion after the exercise unless a separately authorized disposal actually occurred and was recorded; retain material needed for the stated peer comparison until that review is complete. The hash does not prove R14's query coverage, source truth, actor identity or collection authority.

**Integration 3:** Under EX019 and again after its final worked-result table, insert the same short state criterion below. Preserve the original collection-note table and the separate MIN2 derivative and HOLD2 source-control extensions.

**State criterion within the existing 0–2 rubric:** A completed local E1 file, a second-file failure and a planned collection are different states. Record only the file, time, integrity measurement, transfer or disposal actually evidenced; mark unrecorded or unperformed fields explicitly. Do not claim that failure to create the second file invalidated or erased an already created first file. A retained copy is not an applied source hold. This criterion adds no row-count requirement, exercise ID or production permission.

## Integration boundary

Keep the canonical R1–R16 cards unchanged. Keep the original 09:05 and 09:20 release rules, exercise IDs, two-row EX014 table, three-row EX015 table, short EX016 note, two EX017 claim/limit pairs and follow-up, three-row EX018 P-A request plus two-row P-A/P-B comparison, and EX019 collection-note format. EX017's existing T1 limitation and EX018's proposal-versus-collection distinction remain valid; this draft does not replace those answers merely to increase length.

These replacements deepen the specific reasoning and executable failure paths; they are not a new manuscript, a translation baseline, an A4 measurement or a completion decision. After integration, check the affected transcripts and exercise/answer pairs in the single principal manuscript before treating these temporary blocks as superseded.
