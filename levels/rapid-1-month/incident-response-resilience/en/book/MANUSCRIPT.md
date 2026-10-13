| How many patrons are affected? | Scope matters for service and communication decisions. | Compare the approved booking audit with the help-desk queue. |
| Can the logs be trusted and retained? | A short retention window may make delay costly. | Record the source, requested event range and proposed collection method; ask the custodian to confirm present availability, retention anchor and any actual deadline. Mark an unverified deadline unknown. |

The initial action should be the smallest authorized check that could change the next decision. If a new edit is causing immediate harm, the incident lead can seek an urgent containment decision while collection continues. If the signal is stale and service impact is unknown, preserving records and checking the owner may be the more informative first step. Triage and containment can overlap; they are not a rigid sequence.

**Containment urgency** concerns whether additional harmful activity is sufficiently plausible or observed to justify prompt consideration of protective options. It depends on signs of continued activity, current impact, confidence in control scope and possible damage from the intervention itself. A short log-retention period does not, by itself, prove a new harmful edit or authorize account restriction.

At 09:20, R15 supplies a **reported policy** for detailed booking-audit records: a 24-hour duration with an authorized-copy provision. It does not demonstrate the policy's enforcement, its starting anchor, the oldest retrievable relevant row, or an actual deletion. The time-sensitive task is to ask the incident lead and application custodian about a bounded preservation route and current source availability. Do not add 24 hours to R9's event time or treat the 09:14 notice time as a new retention start. A retained copy, if later authorized and actually acquired, would have its own custody and retention record; its existence would not by itself show that deletion at the producing source stopped. Preservation concern is therefore justified without a confirmed loss outcome or a conclusion that an attack occurred.

At that same checkpoint, R9 and R11 merit investigation and continued review, but there is no **post-09:20 newly verified edit** in the released record. R14's quiet result is limited to an unspecified query range, and cannot establish that no additional activity occurred. The incident lead therefore needs a review trigger and a plan for authorized escalation without describing a containment operation as already needed or performed.

    request_downgrade=False,
    variant=False,
)

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

def review(s):
    problem = validate_tri2_input(s)
    if problem is not None:
        return problem
    if not set(s["refs"]).issubset(RELEASE[s["stage"]]):
        return "BLOCK_UNRELEASED_SOURCE"
    # Declared flags must be supported by cards in this release set.
    released_refs = set(s["refs"])
    if s["retention_notice"] and "R15" not in released_refs:
        return "BLOCK_UNRELEASED_CLAIM:R15"
    if s["quiet_summary"] and "R14" not in released_refs:
        return "BLOCK_UNRELEASED_CLAIM:R14"
    if s["patron_report"] and not ({"R5", "R11"} & released_refs):
        return "BLOCK_UNRELEASED_CLAIM:PATRON_REPORT"
    if (
        s["approved_addendum"] or s["training_scope_verified_complete"]
        or s["addendum_names_b19"]
    ) and not {"R9", "R10"}.issubset(released_refs):
        return "BLOCK_UNRELEASED_CLAIM:R9_R10"
    if s["verified_fresh_edit"] and not s["variant"]:
        return "BLOCK_INVENTED_CANONICAL_EVENT"
    if not s["variant"] and any((
        s["owner_state_check"], s["source_safeguard_confirmed"],
        s["approved_addendum"], s["no_new_edits_verified"],
        s["query_coverage_known"], s["retention_anchor_known"],
        s["training_scope_verified_complete"], s["addendum_names_b19"],
        not s["custodian_available"],
    )):
        return "BLOCK_INVENTED_CANONICAL_PREMISE"
    if s["no_new_edits_verified"] and not s["query_coverage_known"]:
        return "BLOCK_UNBOUNDED_NEGATIVE_PREMISE"
    if s["verified_fresh_edit"] and s["request_downgrade"]:
        return "BLOCK_GLOBAL_DOWNGRADE_NEW_EDIT_OPEN"

            and s["addendum_names_b19"]
            and s["no_new_edits_verified"]
        ):
            flags.append("DOWNGRADE_ONLY_B19_TASK_SCOPE_CONCERN")
        else:
            flags.append("DOWNGRADE_NOT_JUSTIFIED")
    if s["retention_notice"] and not s["custodian_available"]:
        flags.append("ESCALATE_CONTACT_NO_HOLD_ASSUMED")

    ("NEW_EDIT_AND_GLOBAL_DOWNGRADE",
     {"variant": True, "verified_fresh_edit": True,
      "request_downgrade": True}),
    ("VALID_B19_TASK_SCOPE_DOWNGRADE",
     {"variant": True, "request_downgrade": True,
      "approved_addendum": True,
      "training_scope_verified_complete": True,
      "addendum_names_b19": True,
      "no_new_edits_verified": True,
      "query_coverage_known": True,
      "source_safeguard_confirmed": True}),

assert review(ROUND_A).startswith("R:SUPPLIED")
assert case(verified_fresh_edit=True) == (
    "BLOCK_INVENTED_CANONICAL_EVENT"
)

# Independent input-contract controls, not additional R-series facts.
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

For the executed output, scenario interpretation and negative controls, read the [TRI2 worked result](#ir-rapid-ch02-tri2-result) in the final answer appendix. Predict the labels before opening the result.

**Release-guard challenge:** After the baseline program, test three explicitly synthetic Round A variants: set `retention_notice=True` without R15, set `quiet_summary=True` without R14, and set `variant=True`, `approved_addendum=True`, `training_scope_verified_complete=True`, `addendum_names_b19=True`, `no_new_edits_verified=True` and `query_coverage_known=True` without R9/R10. The three results, respectively, must be `BLOCK_UNRELEASED_CLAIM:R15`, `BLOCK_UNRELEASED_CLAIM:R14` and `BLOCK_UNRELEASED_CLAIM:R9_R10`. No case becomes a new canonical R-series record. The 20 baseline conclusions are preserved; task-scope labels do not claim causal attribution. The guard checks the classroom release boundary; it does not authenticate a source or verify a real approval.

The original three release-guard controls remain required. The five additional controls in the complete program test a different boundary: the input schema and the distinction between fixed canonical metadata and separately labeled variants. An empty reference list cannot claim that records were supplied. The text `"False"` is not a Boolean false value; accepting it as a variant marker would admit invented impact into what a reader might mistake for the canonical packet. R15 does not supply an anchor, R14 does not supply complete coverage, and R1–R16 do not report a failed custodian contact. Those altered premises must not silently enter the canonical case.

`custodian_available=True` in the original baseline remains a **model default**, not a verified successful contact. The default produces no collection or hold receipt. Requiring a separately labeled variant for a failed-contact scenario does not authenticate the default; both real contact status and any real preservation result remain unmeasured.

A declared variant can still contain an invented `owner_state_check=True` or source-safeguard flag. These guards do not verify those assertions. They validate classroom structure and provenance boundaries, not source truth, actual harm, probability, severity or permission. TRI2 remains an original CyberABC method rather than a NIST classification policy; [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) provides high-level outcomes, not these particular labels or thresholds.

#### Limitations and diagnostic negative tests

**Further negative control:** Set `request_downgrade=True` while leaving `training_scope_verified_complete=False`. The expected flag is `DOWNGRADE_NOT_JUSTIFIED`. Do not remove the quiet-query or source-retention caveats merely because a respondent asks for lower priority. Restore the baseline after the exercise.

**Required learner output:** Reproduce the 20 baseline lines and five input-contract control lines; record the three separate release-guard challenge results, classify each scenario's most consequential limitation, explain why preservation and containment urgency can move independently, and write two versioned notes—09:05 and 09:20—with the correct release boundaries, owner, next authorized request and review trigger.

**Lab assessment, five points:** one point for exact output; one for three separate confidence layers; one for separating reported from verified impact; one for preservation versus containment review; and one for rejecting unsupported de-escalation, attribution and future-source use. This is supplementary assessment and creates **no numbered exercise ID**.

Write a separate card for each candidate source. Name the **decision it could change**, the smallest relevant field and interval, its custodian, the known or unknown loss path, the approval needed, the expected handoff artifact and the claim that would remain unproved even after collection. This reuses Chapter 1's proposed evidence-readiness contract, but now the case has a live decision point. A source that may expire soon deserves immediate contact even if the cause is uncertain; a source with no confirmed loss clock may still need a parallel availability check. Do not convert the words “high priority” into an unverified deadline. Conversely, an indefinitely retained document is not automatically less important to the hypothesis: it may simply permit a later request after the fragile source is safeguarded.

For a **copy request**, distinguish four states: **proposed**, a bounded request has been written; **approved**, an accountable owner has authorized its stated scope; **collected**, a specified copy has actually been acquired with an acquisition receipt; and **verified**, a reviewer has performed and recorded specified checks on that item. State what was verified: bytes, selection, provenance or another named property, not “everything.” Protecting records in place does not itself move a copy request to collected. A source-hold request follows a separate control lifecycle, including reported application and a bounded effect check where such a mechanism exists. Neither lifecycle substitutes for the other. Record each actual state change, actor, time and source pointer; leave missing receipts pending. This is the book's teaching model, not a required NIST form. The relevant NIST principles concern recording investigative actions and preserving the integrity and provenance of incident information under organizational procedures; see [SP 800-61 Rev. 3, RS.AN-06 and RS.AN-07](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf).

When two requests compete for attention, compare them without inventing a numerical risk score:

Preservation should also be **proportionate**. For the next Harbor Library decision, a bounded booking-audit interval and the account's relevant sign-in summary may be useful. Exporting all patrons, all departments or unrelated accounts could increase privacy risk without improving the decision. A narrow export can still omit a relevant event; record the selection rule and keep an authorized unmodified original when available. Chapter 2 teaches the logic of a collection request and a copy-integrity check. Production evidence handling belongs to the organization's approved procedures and qualified personnel.

<a id="four-clock-ledger-and-learner-release"></a>

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

### 2.4 Worked example: the second alert

| R15 | 09:14 | Retention notice | Detailed booking audit records are deleted after 24 hours unless an authorized copy is retained. |
| R16 | 09:16 | Service-owner note | The owner requests an impact check before any account change and can approve a short booking-service pause if needed. |

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

| Case decision at 09:20 UTC | Rationale | Owner | Review trigger |
|---|---|---|---|

#### Worked 09:20 preservation queue

The learner receives R9–R16 at the **simulated 09:20 review**. R9 reports a 09:03 edit, but was not available for the learner's 09:05 decision. R15 reports a 24-hour policy concerning detailed booking-audit records, not a measured countdown or a completed deletion. The policy anchor, oldest-row availability, enforcement behavior and any authorized copy or source hold remain unconfirmed. Ask the custodian what the copy provision means in this source's actual procedure; do not assume that saving an export changes the source's removal mechanism. The queue records **proposed requests**, not approvals or completed preservation. R15's rule must not be borrowed for R14's separately labeled application-audit source, R11's help-desk record or R13's identity source without an explicit custodial mapping and policy confirmation.

| Request and decision value | Loss/coverage question | Owner and proposed minimal scope | State at 09:20 and remaining limit |
|---|---|---|---|

altered = saved.replace(b"Room 3", b"Room 4")
with Path("E1-modified.txt").open("xb") as output:
    output.write(altered)
print(len(altered), sha256(altered).hexdigest())
```

**Failure-path check: two exclusive creations are not one atomic transaction.** The required new empty directory avoids ordinary filename collisions. Python's [exclusive-create file mode](https://docs.python.org/3.13/library/functions.html#open) refuses to overwrite an existing target, but each call protects only its own file. In a separately labeled failure rehearsal where only `E1-modified.txt` already exists, the first write can create E1 and print its digest before the second write raises `FileExistsError`. That is a **partial local attempt**, not completion of both files and not an overwrite of the pre-existing file. Record which file was actually created, which operation failed and what was left unchanged. Stop; do not delete the existing object or switch to an overwrite mode to obtain the expected transcript. A new authorized empty directory permits an independent attempt with its own recorded state.

For a collection note, record the actual local time when the creation is performed. A recorded start/end interval may honestly bound the operation; a later observation time or filesystem timestamp with unverified semantics must not be relabeled as an exact creation receipt. When a time was not recorded, say so. The synthetic 09:20 review does not supply a local acquisition time.

**Procedure.** First, predict whether both files will have the same byte length and whether their SHA-256 digests will match. Then run the script and record both output lines. Read `E1.txt` and `E1-modified.txt` to locate the intentional one-byte change. Re-run the first digest on `E1.txt` and compare it with the saved value. Finally write a collection note identifying the exact file, byte count, local collection time, synthetic source, authorized classroom scope, transformation and storage location. If you cannot run Python, reason from the displayed bytes and use the worked result to check your conclusion; software execution is not required to answer the conceptual question.

The following optional lab runs entirely in memory with Python 3's standard library. It creates no files, sends no network requests and uses only fictional timestamps. R10's `05:04-04:00` text is an **exercise rendering** of its existing 09:04 UTC value, not a new event or a claim about any real location's timezone rules. The offset is explicit; the script does not guess one.

```python
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
```

**Time-label clarification and input contract:** `source` means the source-card time: an edit for R9, a plan record for R10, and a retention notice for R15. `released` means the learner's 09:20 release. The dates and offsets are the existing synthetic fixture, not new case evidence. This minute-aligned exercise requires an explicit UTC offset and refuses a source timestamp later than its release under the assumed comparable clocks. It rejects sub-minute values rather than silently rounding them. This is not a general RFC 3339 validator or a real clock-verification tool. In particular, Python's [datetime documentation](https://docs.python.org/3.13/library/datetime.html#datetime.datetime.astimezone) explains that converting a naive datetime can use the machine's local timezone; this program rejects that ambiguity before conversion.

Predict the original three intervals and all four rejection reasons before running. None of the malformed-input controls is an R-series event. A chronological rejection calls for investigation of timestamp meaning and clock assumptions; it does not establish malicious activity. Keep ingestion, query execution and copy creation unknown when they have no separate evidence.

**Procedure:** (1) Before running it, convert R10's offset time by hand and predict the three source-to-learner-release intervals. (2) Run the code in an authorized local scratch environment, or calculate the outputs from the shown values if Python is unavailable. (3) Make a three-row table with record ID, original timestamp including offset, normalized UTC source time and its kind, learner-release time, source-to-learner-release interval and whether the record was available at 09:05. (4) Draw the coverage interval from T1 as `09:00 ≤ event < 09:12 UTC` and put R9, the T1 end and the 09:20 review on it. (5) Write two sentences: the strongest conclusion supported by R14 with T1, and the next *authorized* check needed to assess activity after 09:12. Keep the R15 retention notice separate from any assumed deletion instant.

**Expected evidence:** R9 is 09:03 UTC and released to the learner 17 minutes later; R10 is 09:04 UTC and released 16 minutes later; R15 is 09:14 UTC and released six minutes later. None was in the learner's R1–R8 snapshot at 09:05. With T1, R14 supports only that this narrow query showed no further matching edit before 09:12. The unqueried period after 09:12 is an **evidence gap**, not a verified quiet period. The learner should request a new bounded query or an approved source comparison, record its filter and end time, and check whether logging and ingestion were working. R15 reports a 24-hour detailed-record policy with an authorized-copy provision; it does not give enough deletion-policy detail here to calculate the precise expiry of R9 from its event timestamp alone.

**Assessment rubric:** one point each for correct R10 normalization, three correct source-to-learner-release intervals, the 09:05 availability boundary, a T1 coverage statement that excludes post-09:12 activity, and a narrow authorized follow-up with retention uncertainty. Five points show the classroom reasoning is reproducible; they do not certify a real evidence acquisition or establish who edited B19. The printed output and a model coverage statement appear after the Chapter 2 synthetic-extract result in the final appendix.

#### A query envelope is narrower than a case conclusion

The replay query selects `application-audit` booking edits under `desk-a` with **09:00 ≤ event time < 09:12 UTC**. Its second condition is that the row was ingested **no later than the query run time**. The end boundary is exclusive. Assume all four clocks are correct, all rows belong to the same fictional date and no other filter exists; these are classroom assumptions, not evidence about production logging. First run the mental query at 09:12, then repeat the *same event window and account filter* at 09:20. Before looking at code, predict exactly which L IDs each run returns and which exclusion rule removes each other row.

This optional program operates only on the in-memory T2 fixture. Its last column is treated as **query-visible time**; T2 assumes no additional delay between the listed ingestion and search visibility. This simplifying assumption must not be applied to a real collector without checking its semantics. All rows use one fictional UTC day and comparable accurate clocks. The parser validates `HH:MM`, and the program rejects a row visible before its event under those assumptions. It validates the whole supplied packet before filtering, so an irrelevant account cannot hide malformed timestamps. It is still not a production parser, a transport simulation or an ingestion-completeness check.

```python
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
```

Predict the original two query results, the three malformed-input rejections and the omitted-row control. `08:63` must not be normalized accidentally to 09:03; `25:99` is not a valid query clock. An earlier visibility time contradicts this fixture's declared clock contract. In real evidence, such a discrepancy could instead reflect a misunderstood field or source clock and would need investigation.

The `OMITTED_L2` case is equally important: every remaining field is well formed, but the later query returns only L1 because L2 was removed from that variant's input. Syntax validation cannot discover a record it was never given. Retain the complete original packet separately. Neither a successful parser run nor a repeated quiet query establishes source completeness. These controls remain outside canonical R1–R16 and add no exercise ID. Assess their reasoning within the existing five-point T2 rubric's timing, exclusion and bounded-follow-up criteria.

**Work the result in three passes.** First apply only the account and event-time filters: L1 and L2 qualify, L3 fails the account filter, and L4 sits exactly at the exclusive end. Then apply the ingestion cutoff: at 09:12 L2 is not yet visible, whereas at 09:20 it is. Finally compare the two results **without changing the event times**. The extra row in the second run is a *late arrival*, not a new post-09:12 event. Its presence would cause the response lead to revisit any conclusion that relied on the first query's apparent quiet period. It would not, by itself, identify who performed the edit or prove malicious intent.

#### EX015 — Hypothesis table

**Objective:** keep competing explanations live. **Inputs:** H1–H3 from section 2.1 and R1–R16. **Output:** three rows, each with a supporting record, a contradiction or limit, a narrow next authorized check and what result would weaken that hypothesis. You may state that a record is weak support. A score of 2 requires at least one check that could genuinely discriminate between explanations rather than simply restating the same log.

**Discriminator check:** In each row, the named check must be capable of producing the stated weakening result. Identify the correct producer and field: R9 reports a booking-audit room change, whereas R11 reports a time-display concern. A task-approval document and identity-session detail answer different questions. This is a requirement within the existing three-row artifact and 0–2 rubric.

#### EX016 — Priority without false certainty

**For full credit:** The learner identifies R15's possible evidence-loss path, R9/R11's potential booking harm, unresolved attribution, the incident lead's decision authority and the 09:35 review or an earlier verified trigger.

**Additional IM2 discriminator for EX016:** At Round B, distinguish the R15 concern about **detailed booking-audit records relevant to R9** from the retention of R11's help-desk report or R13's identity source, whose policies are not supplied. Separately assess potential booking harm, uncertain cause and the absence of a measured affected-patron total. The independent IM2 fixture supplies no Harbor Library outcome. Keep the same short decision note and 0–2 rubric.

**TRI2 refinement:** Keep the note short. State separately that the synthetic records are supplied, B19 task authorization is unresolved, and cause or human attribution is unproved. Split time sensitivity into source-preservation contact and a conditional human review of containment; R14's quiet summary has incomplete coverage and R15 has no confirmed deletion anchor. Name the authorized P-A or impact-check request, the incident lead, and the 09:35 or earlier evidence-triggered review. This adds precision to the same artifact and 0–2 rubric, not another exercise.

#### EX019 — Collection note

**Objective:** make an exercise extract reviewable. **Inputs:** the E1 fixture in section 2.5 and R9/R14. **Output:** a collection-note table with case/item ID, source and event range, collector, authority, actual local collection time *if a file was created*, copy location, transformation and limitation. If no file was created, label the note **planned** and leave collection time and digest **not applicable**; do not pretend an export occurred. A score of 2 identifies E1 as a synthetic transcription, distinguishes original book text from the working file and records access scope. A made-up digest is not required.

**State criterion within the existing 0–2 rubric:** A completed local E1 file, a second-file failure and a planned collection are different states. Record only the file, time, integrity measurement, transfer or disposal actually evidenced; mark unrecorded or unperformed fields explicitly. Do not claim that failure to create the second file invalidated or erased an already created first file. A retained copy is not an applied source hold. This criterion adds no row-count requirement, exercise ID or production permission.

**MIN2 supplementary task (after the required artifact):**

NEW_EDIT_AND_GLOBAL_DOWNGRADE BLOCK_GLOBAL_DOWNGRADE_NEW_EDIT_OPEN
VALID_B19_TASK_SCOPE_DOWNGRADE R:SUPPLIED_NOT_AUTHENTICATED I:TRAINING_SCOPE_SUPPORTED C:ACTOR_UNPROVEN H:REPORT_ONLY P:SOURCE_PROTECTED_IN_VARIANT K:B19_CONCERN_REDUCED flags=DOWNGRADE_ONLY_B19_TASK_SCOPE_CONCERN
DOWNGRADE_WITH_PRESERVATION_OPEN R:SUPPLIED_NOT_AUTHENTICATED I:TRAINING_SCOPE_SUPPORTED C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:B19_CONCERN_REDUCED flags=DOWNGRADE_ONLY_B19_TASK_SCOPE_CONCERN
OWNER_VERIFIED_IMPACT R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:VERIFIED_BOUNDED P:ANCHOR_UNKNOWN_CONTACT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF
SOURCE_SAFEGUARDED_IN_VARIANT R:SUPPLIED_NOT_AUTHENTICATED I:CONTESTED_OR_INCOMPLETE C:ACTOR_UNPROVEN H:REPORT_ONLY P:SOURCE_PROTECTED_IN_VARIANT K:OPEN_HYPOTHESES flags=QUIET_NOT_NEGATIVE_PROOF
~~~

**Supplementary release-guard challenge result:**

~~~text
R15_TOO_EARLY BLOCK_UNRELEASED_CLAIM:R15
R14_TOO_EARLY BLOCK_UNRELEASED_CLAIM:R14
B19_WITHOUT_R9_R10 BLOCK_UNRELEASED_CLAIM:R9_R10
~~~

The first two variants declare a later card's content in a 09:05 source set; the last tries to interpret B19's training scope without either relevant card. The guard refuses the unsupported claim rather than quietly adding missing cards. None changes the twenty baseline case results or proves authentic provenance outside this fixture.

**Input-contract controls from the complete TRI2 program:**

~~~text
EMPTY_SOURCE_SET BLOCK_EMPTY_SOURCE_SET
TEXT_FALSE BLOCK_NON_BOOLEAN:variant
CANONICAL_ANCHOR BLOCK_INVENTED_CANONICAL_PREMISE
CANONICAL_COVERAGE BLOCK_INVENTED_CANONICAL_PREMISE
CANONICAL_CONTACT BLOCK_INVENTED_CANONICAL_PREMISE
~~~

The first result rejects a positive source-availability description with no cited records. The second rejects a string before Python truthiness can turn it into a supposed variant authorization. The remaining controls reject unsupported changes to the canonical retention, query-coverage and contact premises. A blocking result identifies an input inconsistency, not a deleted source, an observed attack or a production action. Preserve the five-point supplementary lab rubric: assess these controls within its existing evidence-boundary and unsupported-claim criterion. No EX identifier is added.

#### Interpretation of positive and negative controls

**CONFLICTING_SIGNALS** supplies an invented addendum but explicitly withholds confirmation that it represents the complete approved training scope. The interpretation remains unresolved. **PREMATURE_DOWNGRADE** shows that a desire to lower concern is not an evidentiary basis.

**VALID_B19_TASK_SCOPE_DOWNGRADE** assumes, *only inside its separate variant*, a complete approved B19 addendum, a valid bounded negative observation and a declared source safeguard. It supports a **limited reduction in the B19 outside-training concern** without establishing human attribution or every service outcome. The source-protected label is an invented premise, not verified by this program.

**DOWNGRADE_WITH_PRESERVATION_OPEN** uses the same invented task-scope and quiet-observation premises but **without** a source safeguard. Concern about the B19 explanation may narrow while preservation work remains time-sensitive. These two results are intentionally different.

### EX014 — Worked result

| Answerable question | Supplied starting point | Authorized next source | Result that changes triage |
|---|---|---|---|
| Was the B19 room-change task within the approved training scope effective at 09:03? | R9 reports the room change; R10 lists B17/B18 but not B19 | Training owner supplies the complete applicable approved plan/version and any B19 addendum through the authorized case route | A valid, applicable B19 task approval strengthens the task-scope explanation; a confirmed complete set excluding B19 weakens it. Neither identifies the operator. |
| What, if anything, is wrong with the selected B19 room and reported time representations? | R9 reports a room edit; R11 reports a time concern; R16 requests impact assessment | Service owner authorizes a narrow, field-specific comparison; application custodian supplies time-stamped authoritative values and the relevant view against approved targets | A supported match, mismatch or missing comparator changes the bounded impact assessment. Further bookings require justified scope; no population count or common cause follows automatically. |

The first question tests task authorization; the second tests a bounded business-state comparison. Neither a missing addendum nor an empty narrow query proves the opposite claim without checking source completeness and coverage.

**TRI2 evidence layers:** In row one, R9 supplies an edit and R10 omits B19 from the supplied plan. A dated, complete, approved task addendum that explicitly names B19 could narrow the *task-scope* concern; a complete approved list that excludes it would strengthen that concern. Neither identifies the human operator. In row two, R11 is a patron report and R16 asks for impact assessment. A service-owner-authorized comparison of current authoritative values with approved targets could establish a bounded booking mismatch or show that the selected booking is correct. It would not count every affected patron or settle the cause of an audit edit.

### EX015 — Worked result

| Hypothesis | Support | Contradiction or limit | Narrow authorized check | Result that weakens it |
|---|---|---|---|---|
| H1: scheduled training explains the edits | R6 records training; R10 names B17/B18 | R10 omits B19; R12's recollection is incomplete | Training owner supplies the complete approved task set and addenda applicable to the B19 operation | A confirmed complete applicable set excludes B19, weakening training as an explanation of all recorded edits |
| H2: B19 account use fell outside the approved task set | R9 records B19 changed under desk-a; R10's supplied plan omits B19 | Plan completeness and applicable approval are unconfirmed; R13 does not identify a human | Training owner verifies whether the exact B19 task was approved at the relevant time; request session detail separately only for a defined correlation question | A verified applicable task approval explicitly covering the B19 room change weakens the outside-plan proposition, without proving who acted or whether the resulting state was correct |
| H3: the reported time symptom reflects a display or synchronization discrepancy | R11 reports that B19's time looked wrong | No time-field comparison is supplied; R9 records a room change, not a demonstrated time-display fault | Service owner authorizes a time-aligned comparison of the relevant view, stored time and applicable approved time target | Contemporaneous view and stored time agreeing with each other but differing from the target weakens a display-only account of that observed discrepancy; an earlier transient fault remains unresolved |

The hypotheses need not be mutually exclusive. A good answer identifies what each check can and cannot settle.

| Transformation and original | Fixture transcribes two rows as UTF-8 text; the book table is the retained source of the classroom transcription |
| Limitation | No production log was acquired; a saved file cannot prove the source system's completeness, clock or identity attribution |

**State criterion within the existing 0–2 rubric:** A completed local E1 file, a second-file failure and a planned collection are different states. Record only the file, time, integrity measurement, transfer or disposal actually evidenced; mark unrecorded or unperformed fields explicitly. Do not claim that failure to create the second file invalidated or erased an already created first file. A retained copy is not an applied source hold. This criterion adds no row-count requirement, exercise ID or production permission.

If the learner ran `fixture.py`, replace the planned state with **completed local fixture**, record the actual creation time and scratch path, and attach the measured 235-byte SHA-256 value from the lab. Never invent a 09:20 collection time simply because the scenario's discovery checkpoint was 09:20.

**MIN2 worked extension:**

The script writes **235 bytes** to each file. The SHA-256 digest for `E1.txt` is `dc973f580305633eb0a75317c5bdbd9886a8fc015e14a0b17bae09be5e3a6e37`; the digest for `E1-modified.txt` is `15287410550f021dcb81e10fc1833297ffa840ee8ffa8e75867de36df64ffa4d`. The strings have equal byte length because the single ASCII digit `3` was replaced with `4`; their different digests show the modified copy is not byte-identical to the saved original. Learners should calculate the values locally rather than trust a copied answer.

A completed-run model note must be populated from the learner's actual work: “HL-IR-001/E1; local teaching transcription of R9 and R14, not a production export; original source retained in this public book; learner-created E1.txt in the recorded authorized scratch location; actual local creation time or recorded operation interval attached, or explicitly not recorded; classroom scope limited to the supplied synthetic material; 235 bytes and the measured SHA-256 value attached; access limited to the permitted learner/reviewer; retention and any disposal remain subject to the authorized exercise procedure.” This is a template, not evidence that the learner ran the program. A planned or partially failed attempt must keep its actual state. Do not claim deletion after the exercise unless a separately authorized disposal actually occurred and was recorded; retain material needed for the stated peer comparison until that review is complete. The hash does not prove R14's query coverage, source truth, actor identity or collection authority.

### Chapter 2 temporal-coverage lab — worked result

The optional Python script prints the following seven lines for the supplied fixture and its independent controls:

```text
R9 source=09:03 UTC released=09:20 UTC interval=17 min
R10 source=09:04 UTC released=09:20 UTC interval=16 min
R15 source=09:14 UTC released=09:20 UTC interval=6 min
NO_OFFSET: OFFSET_REQUIRED
FUTURE_SOURCE: SOURCE_AFTER_RELEASE
BAD_CLOCK: INVALID_TIMESTAMP
SUB_MINUTE: MINUTE_PRECISION_REQUIRED
```

R10's explicit `05:04-04:00` normalizes to 09:04 UTC. The source-to-release intervals remain 17, 16 and 6 minutes; they do not measure logging-pipeline delay. The controls reject a missing offset, a source time after the release, an invalid hour and an input finer than the stated minute precision. Rejecting the last input is a teaching-contract choice, not a claim that real logs should discard seconds. The same complete program produced the same seven lines under both UTC and America/New_York host timezone settings. This does not validate any production clock.

With exercise-only T1, the strongest negative statement is: “The specified `application-audit` query for `desk-a` booking edits in `09:00 ≤ event < 09:12 UTC` showed no further matching edit after R9.” R14 *without* T1 lacks those exact bounds. Neither version proves that no edit occurred after 09:12, through another account or in an unexamined source. A bounded request to the authorized application custodian should specify source, account filters, the new interval, an ingestion/completeness check, collector and collection time. R15 calls for a prompt retention decision; the exact deletion instant depends on policy detail not supplied here. A full-credit answer records these limits rather than filling gaps with confident words.

### Chapter 2 delayed-arrival T2 replay — worked result

The optional in-memory program prints:

```text
09:12 L1
09:20 L1,L2
BAD_MINUTE: BLOCK_INVALID_HHMM
INVALID_QUERY: BLOCK_INVALID_HHMM
VISIBLE_BEFORE_EVENT: BLOCK_VISIBILITY_BEFORE_EVENT:X
OMITTED_L2: L1
```

Both runs use the same account filter and **09:00 ≤ event < 09:12 UTC** window. L1 qualifies in both. L2's event time is 09:10, so it belongs to that window, but its 09:18 ingestion time makes it invisible at the 09:12 query cutoff and visible at 09:20. L3 is excluded because its account is `helper-b`, even though its event and ingestion times are inside the interval. L4 is excluded because 09:12 is the *exclusive* end; its later ingestion time is not the reason it fails this particular selection.

The first two lines are unchanged: the late L2 becomes visible without moving its 09:10 event time; L4 remains excluded at the 09:12 exclusive end. The next three lines demonstrate input rejection, not observed incident events. The last line comes from a separate packet lacking L2: its quiet result is compatible with missing input and cannot prove no matching event occurred. Source coverage requires independent, appropriately authorized evidence about the producer, collection/index path and selection, not just successful filtering of available rows.

The strongest correction is: “At 09:12, the specified query showed no other visible matching edit after L1; this did not establish that the event-time interval was complete.” In the T2 replay, the repeated query would later reveal L2 and require a fresh assessment, but **L2 is not a canonical Harbor Library case fact**. The next request is to the fictional application/logging custodian: “Please confirm the exact source, `desk-a` account filter, half-open event interval, each query's run and ingestion cutoff, and whether collection or indexing lag could leave relevant rows unseen; provide a scoped follow-up result under the incident lead's approval.” The custodian's reply, not the newest event timestamp alone, would determine what completeness claim is defensible. None of the four L rows establishes the human operator or intent.

