| How many patrons are affected? | Scope matters for service and communication decisions. | Compare the approved booking audit with the help-desk queue. |
| Can the logs be trusted and retained? | A short retention window may make delay costly. | Record source, time range, export method and retention deadline. |

The initial action should be the smallest authorized check that could change the next decision. If a new edit is causing immediate harm, the incident lead can seek an urgent containment decision while collection continues. If the signal is stale and service impact is unknown, preserving records and checking the owner may be the more informative first step. Triage and containment can overlap; they are not a rigid sequence.

**Containment urgency** concerns whether additional harmful activity is sufficiently plausible or observed to justify prompt consideration of protective options. It depends on signs of continued activity, current impact, confidence in control scope and possible damage from the intervention itself. A short log-retention period does not, by itself, prove a new harmful edit or authorize account restriction.

At 09:20, R15 raises a preservation concern: the booking system keeps its detailed audit trail for only 24 hours, so evidence disappears unless someone with authority saves a copy first. The **policy anchor is unknown**. The appropriate response is to seek a bounded source-availability/preservation decision and obtain the custodian's explanation promptly, not to publish a precise countdown calculated from R9's event time.

At that same checkpoint, R9 and R11 merit investigation and continued review, but there is no **post-09:20 newly verified edit** in the released record. R14's quiet result is limited to an unspecified query range, and cannot establish that no additional activity occurred. The incident lead therefore needs a review trigger and a plan for authorized escalation without describing a containment operation as already needed or performed.

    request_downgrade=False,
    variant=False,
)

def review(s):
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
    )):
        return "BLOCK_INVENTED_CANONICAL_PREMISE"
    if s["no_new_edits_verified"] and not s["query_coverage_known"]:
        return "BLOCK_UNBOUNDED_NEGATIVE_PREMISE"
    if s["verified_fresh_edit"] and s["request_downgrade"]:
        return "BLOCK_GLOBAL_DOWNGRADE_NEW_EDIT_OPEN"

            and s["addendum_names_b19"]
            and s["no_new_edits_verified"]
        ):
            flags.append("DOWNGRADE_ONLY_B19_CAUSE_CONCERN")
        else:
            flags.append("DOWNGRADE_NOT_JUSTIFIED")
    if s["retention_notice"] and not s["custodian_available"]:
        flags.append("ESCALATE_CONTACT_NO_HOLD_ASSUMED")

    ("NEW_EDIT_AND_GLOBAL_DOWNGRADE",
     {"variant": True, "verified_fresh_edit": True,
      "request_downgrade": True}),
    ("VALID_B19_CAUSE_DOWNGRADE",
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
~~~

For the executed output, scenario interpretation and negative controls, read the [TRI2 worked result](#ir-rapid-ch02-tri2-result) in the final answer appendix. Predict the labels before opening the result.

**Release-guard challenge:** After the baseline program, test three explicitly synthetic Round A variants: set `retention_notice=True` without R15, set `quiet_summary=True` without R14, and set `variant=True`, `approved_addendum=True`, `training_scope_verified_complete=True`, `addendum_names_b19=True`, `no_new_edits_verified=True` and `query_coverage_known=True` without R9/R10. The three results, respectively, must be `BLOCK_UNRELEASED_CLAIM:R15`, `BLOCK_UNRELEASED_CLAIM:R14` and `BLOCK_UNRELEASED_CLAIM:R9_R10`. No case becomes a new canonical R-series record. The 20 original TRI2 outputs remain unchanged. The guard checks the classroom release boundary; it does not authenticate a source or verify a real approval.

#### Limitations and diagnostic negative tests

**Further negative control:** Set `request_downgrade=True` while leaving `training_scope_verified_complete=False`. The expected flag is `DOWNGRADE_NOT_JUSTIFIED`. Do not remove the quiet-query or source-retention caveats merely because a respondent asks for lower priority. Restore the baseline after the exercise.

**Required learner output:** Reproduce all 20 lines, classify each scenario's most consequential limitation, explain why preservation and containment urgency can move independently, and write two versioned notes—09:05 and 09:20—with the correct release boundaries, owner, next authorized request and review trigger.

**Lab assessment, five points:** one point for exact output; one for three separate confidence layers; one for separating reported from verified impact; one for preservation versus containment review; and one for rejecting unsupported de-escalation, attribution and future-source use. This is supplementary assessment and creates **no numbered exercise ID**.

Write a separate card for each candidate source. Name the **decision it could change**, the smallest relevant field and interval, its custodian, the known or unknown loss path, the approval needed, the expected handoff artifact and the claim that would remain unproved even after collection. This reuses Chapter 1's proposed evidence-readiness contract, but now the case has a live decision point. A source that may expire soon deserves immediate contact even if the cause is uncertain; a source with no confirmed loss clock may still need a parallel availability check. Do not convert the words “high priority” into an unverified deadline. Conversely, an indefinitely retained document is not automatically less important to the hypothesis: it may simply permit a later request after the fragile source is safeguarded.

The queue has four distinct states: **proposed** means the analyst has written a bounded request; **approved** means the named owner authorized that scope; **collected** means a custodian actually produced or preserved a specified item; **verified** means a reviewer checked the item's selection, recorded bytes or other appropriate integrity properties and limitations. An approval is not a completed collection. A digest is not a source-coverage check. A “retention hold” is itself an operational action that needs a named authority and a confirmed effect; saying one was requested does not show that deletion stopped. For every state change, record the time, actor, source pointer and what remains pending.

When two requests compete for attention, compare them without inventing a numerical risk score:

Preservation should also be **proportionate**. For the next Harbor Library decision, a bounded booking-audit interval and the account's relevant sign-in summary may be useful. Exporting all patrons, all departments or unrelated accounts could increase privacy risk without improving the decision. A narrow export can still omit a relevant event; record the selection rule and keep an authorized unmodified original when available. Chapter 2 teaches the logic of a collection request and a copy-integrity check. Production evidence handling belongs to the organization's approved procedures and qualified personnel.

#### Four-clock ledger and learner release

A timestamp is meaningful only when its origin is identified. At minimum distinguish:

- **Event time:** when the source claims an operation took place.
- **Ingestion time:** when a receiving store made that operation's record available.
- **Collection time:** when a specified copy or export was actually acquired.
- **Discovery time:** when the analyst received or recognized the relevant information.

A query also has a **run time**, which is distinct from its selected event-time interval. These clocks may be identical in a simple lab but differ in a real collection pipeline. Ingesting a delayed event later does not move its original event time. Collecting a record tomorrow does not mean its event occurred tomorrow.

The Round B teaching checkpoint supplies a concrete example:

| Record | Printed event/record time | Learner's earliest permitted availability in this chapter | Interpretation |
|---|---|---|---|
| R9 — B19 edit | 09:03 UTC | 09:20 UTC | The printed event is earlier; it was not available to the learner's 09:05 decision |
| R10 — training-plan record | 09:04 UTC | 09:20 UTC | Record time does not prove when the underlying plan was originally approved |
| R15 — retention notice | 09:14 UTC | 09:20 UTC | The notice becomes available at Round B; it gives no collection receipt or deletion anchor |
| R16 — service-owner note | 09:16 UTC | 09:20 UTC | The note states an owner condition, not an executed account or service change |

These are fictional source and release times, not measurements of real ingestion delays. The actual ingestion timestamps of the producing systems are **not supplied**. Calling the difference between printed event time and release time an observed "pipeline ingestion delay" would therefore invent a measurement. At most it is the exercise's **event-to-learner-release interval**.

Time discipline protects decision review: one must assess the 09:05 decision from R1–R8, not from later-released R9 merely because R9 carries a 09:03 event timestamp. In a real case, retain original timezone or UTC offset and document normalization and clock uncertainty. [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) specifies an Internet date-time representation including timezone offsets; it does not guarantee that a source clock is accurate.

### 2.4 Worked example: the second alert

| R15 | 09:14 | Retention notice | Detailed booking audit records are deleted after 24 hours unless an authorized copy is retained. |
| R16 | 09:16 | Service-owner note | The owner requests an impact check before any account change and can approve a short booking-service pause if needed. |

**Step 1: state observations.** R9 records a later edit to `B19`; R10 does not list that booking in the planned exercise; R12 records a person's recollection, not proof that no edit occurred; R14 only covers its queried range. **Step 2: compare hypotheses.** H1 explains `B17` and `B18` better than it explains `B19`. H2 gains support from the unexpected `B19` edit but is still unconfirmed because the staff member could have forgotten or the plan could be incomplete. H3 could help explain a patron display problem but does not by itself explain the application audit record. **Step 3: choose the next authorized check.** Ask the training owner whether any unlisted task involved `B19`, request a narrow impact check for affected bookings, and ask the incident lead for a prompt, bounded preservation decision while the source remains available if possible. Ask the custodian to establish R15's actual policy anchor, oldest retrievable relevant record and feasible preservation route. No exact deletion deadline is supported yet. Set a near-term review time and revisit containment if changes resume or harm expands.

| Case decision at 09:20 UTC | Rationale | Owner | Review trigger |
|---|---|---|---|

#### Worked 09:20 preservation queue

The learner has received R9–R16 at the **simulated 09:20 review**. R9's printed event time is 09:03, but the learner did not have R9 for the earlier 09:05 decision. R15 warns that the detailed booking audit trail has a 24-hour lifespan; without an authorized copy it expires on schedule. It does **not** say whether the clock starts at event creation, ingestion, storage or another policy point; nor does it show that a copy or hold already exists. The queue below is therefore a set of **requests**, not a record of actual collection. It does not add evidence to R9–R16.

| Request and decision value | Loss/coverage question | Owner and proposed minimal scope | State at 09:20 and remaining limit |
|---|---|---|---|

altered = saved.replace(b"Room 3", b"Room 4")
with Path("E1-modified.txt").open("xb") as output:
    output.write(altered)
print(len(altered), sha256(altered).hexdigest())
```

**Procedure.** First, predict whether both files will have the same byte length and whether their SHA-256 digests will match. Then run the script and record both output lines. Read `E1.txt` and `E1-modified.txt` to locate the intentional one-byte change. Re-run the first digest on `E1.txt` and compare it with the saved value. Finally write a collection note identifying the exact file, byte count, local collection time, synthetic source, authorized classroom scope, transformation and storage location. If you cannot run Python, reason from the displayed bytes and use the worked result to check your conclusion; software execution is not required to answer the conceptual question.

The following optional lab runs entirely in memory with Python 3's standard library. It creates no files, sends no network requests and uses only fictional timestamps. R10's `05:04-04:00` text is an **exercise rendering** of its existing 09:04 UTC value, not a new event or a claim about any real location's timezone rules. The offset is explicit; the script does not guess one.

```python
from datetime import datetime, timezone

rows = [
    ("R9", "2026-10-11T09:03:00+00:00", "2026-10-11T09:20:00+00:00"),
    ("R10", "2026-10-11T05:04:00-04:00", "2026-10-11T09:20:00+00:00"),
    ("R15", "2026-10-11T09:14:00+00:00", "2026-10-11T09:20:00+00:00"),
]

for record_id, event_text, seen_text in rows:
    event = datetime.fromisoformat(event_text).astimezone(timezone.utc)
    seen = datetime.fromisoformat(seen_text).astimezone(timezone.utc)
    delay = int((seen - event).total_seconds() // 60)
    print(f"{record_id} event={event:%H:%M} UTC seen={seen:%H:%M} UTC delay={delay} min")
```

**Time-label clarification:** In this fictional program, `seen` is the 09:20 learner-release checkpoint. The three `delay` values measure event-to-learner-release intervals, **not** logging-pipeline ingestion, first detector discovery, first operator awareness or copy-collection time. Those additional times are not supplied. The printed label remains `delay` for reproducibility, but name its meaning alongside any result. A verified event timestamp after a supposedly earlier receipt under comparable clocks would require investigating the inconsistency, not accepting a negative duration as valid causal order.

**Procedure:** (1) Before running it, convert R10's offset time by hand and predict the three delays. (2) Run the code in an authorized local scratch environment, or calculate the outputs from the shown values if Python is unavailable. (3) Make a three-row table with record ID, original timestamp including offset, normalized UTC event time, learner-release time, event-to-release interval and whether the record was available at 09:05. (4) Draw the coverage interval from T1 as `09:00 ≤ event < 09:12 UTC` and put R9, the T1 end and the 09:20 review on it. (5) Write two sentences: the strongest conclusion supported by R14 with T1, and the next *authorized* check needed to assess activity after 09:12. Keep the R15 retention notice separate from any assumed deletion instant.

**Expected evidence:** R9 is 09:03 UTC and released to the learner 17 minutes later; R10 is 09:04 UTC and released 16 minutes later; R15 is 09:14 UTC and released six minutes later. None was in the learner's R1–R8 snapshot at 09:05. With T1, R14 supports only that this narrow query showed no further matching edit before 09:12. The unqueried period after 09:12 is an **evidence gap**, not a verified quiet period. The learner should request a new bounded query or an approved source comparison, record its filter and end time, and check whether logging and ingestion were working. R15 says detailed records are deleted after 24 hours unless copied; it does not give enough deletion-policy detail here to calculate the precise expiry of R9 from its event timestamp alone.

**Assessment rubric:** one point each for correct R10 normalization, three correct event-to-learner-release intervals, the 09:05 availability boundary, a T1 coverage statement that excludes post-09:12 activity, and a narrow authorized follow-up with retention uncertainty. Five points show the classroom reasoning is reproducible; they do not certify a real evidence acquisition or establish who edited B19. The printed output and a model coverage statement appear after the Chapter 2 synthetic-extract result in the final appendix.

#### A query envelope is narrower than a case conclusion

The replay query selects `application-audit` booking edits under `desk-a` with **09:00 ≤ event time < 09:12 UTC**. Its second condition is that the row was ingested **no later than the query run time**. The end boundary is exclusive. Assume all four clocks are correct, all rows belong to the same fictional date and no other filter exists; these are classroom assumptions, not evidence about production logging. First run the mental query at 09:12, then repeat the *same event window and account filter* at 09:20. Before looking at code, predict exactly which L IDs each run returns and which exclusion rule removes each other row.

This optional Python 3 standard-library program performs only the stated filtering in memory. It opens no files, sends no requests and cannot query a real service. Its minute parser is intentionally limited to a single fictional UTC day; it is not a general timestamp-normalization function.

```python
rows = [
    ("L1", "desk-a", "09:03", "09:04"),
    ("L2", "desk-a", "09:10", "09:18"),
    ("L3", "helper-b", "09:11", "09:11"),
    ("L4", "desk-a", "09:12", "09:13"),
]

def minute(utc_hhmm):
    hour, minute_part = map(int, utc_hhmm.split(":"))
    return hour * 60 + minute_part

def visible_at(query_time):
    return [
        row_id for row_id, account, event_time, ingested_time in rows
        if account == "desk-a"
        and minute("09:00") <= minute(event_time) < minute("09:12")
        and minute(ingested_time) <= minute(query_time)
    ]

for query_time in ("09:12", "09:20"):
    print(query_time, ",".join(visible_at(query_time)))
```

**Work the result in three passes.** First apply only the account and event-time filters: L1 and L2 qualify, L3 fails the account filter, and L4 sits exactly at the exclusive end. Then apply the ingestion cutoff: at 09:12 L2 is not yet visible, whereas at 09:20 it is. Finally compare the two results **without changing the event times**. The extra row in the second run is a *late arrival*, not a new post-09:12 event. Its presence would cause the response lead to revisit any conclusion that relied on the first query's apparent quiet period. It would not, by itself, identify who performed the edit or prove malicious intent.

#### EX015 — Hypothesis table

**Objective:** keep competing explanations live. **Inputs:** H1–H3 from section 2.1 and R1–R16. **Output:** three rows, each with a supporting record, a contradiction or limit, a narrow next authorized check and what result would weaken that hypothesis. You may state that a record is weak support. A score of 2 requires at least one check that could genuinely discriminate between explanations rather than simply restating the same log.

#### EX016 — Priority without false certainty

**For full credit:** The learner identifies R15's possible evidence-loss path, R9/R11's potential booking harm, unresolved attribution, the incident lead's decision authority and the 09:35 review or an earlier verified trigger.

**Additional IM2 discriminator for EX016:** At Round B, distinguish the urgency to preserve R9/R11-related evidence under R15 from confidence in a cause or a measured affected-patron total. The separate IM2 fixture supplies no Harbor Library outcome.

**TRI2 refinement:** Keep the note short. State separately that the synthetic records are supplied, B19 task authorization is unresolved, and cause or human attribution is unproved. Split time sensitivity into source-preservation contact and a conditional human review of containment; R14's quiet summary has incomplete coverage and R15 has no confirmed deletion anchor. Name the authorized P-A or impact-check request, the incident lead, and the 09:35 or earlier evidence-triggered review. This adds precision to the same artifact and 0–2 rubric, not another exercise.

#### EX019 — Collection note

**Objective:** make an exercise extract reviewable. **Inputs:** the E1 fixture in section 2.5 and R9/R14. **Output:** a collection-note table with case/item ID, source and event range, collector, authority, actual local collection time *if a file was created*, copy location, transformation and limitation. If no file was created, label the note **planned** and leave collection time and digest **not applicable**; do not pretend an export occurred. A score of 2 identifies E1 as a synthetic transcription, distinguishes original book text from the working file and records access scope. A made-up digest is not required.

**MIN2 supplementary task (after the required artifact):**

NEW_EDIT_AND_GLOBAL_DOWNGRADE BLOCK_GLOBAL_DOWNGRADE_NEW_EDIT_OPEN
VALID_B19_CAUSE_DOWNGRADE R:SUPPLIED_NOT_AUTHENTICATED I:TRAINING_SCOPE_SUPPORTED C:ACTOR_UNPROVEN H:REPORT_ONLY P:SOURCE_PROTECTED_IN_VARIANT K:B19_CONCERN_REDUCED flags=DOWNGRADE_ONLY_B19_CAUSE_CONCERN
DOWNGRADE_WITH_PRESERVATION_OPEN R:SUPPLIED_NOT_AUTHENTICATED I:TRAINING_SCOPE_SUPPORTED C:ACTOR_UNPROVEN H:REPORT_ONLY P:ANCHOR_UNKNOWN_CONTACT K:B19_CONCERN_REDUCED flags=DOWNGRADE_ONLY_B19_CAUSE_CONCERN
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

#### Interpretation of positive and negative controls

**CONFLICTING_SIGNALS** supplies an invented addendum but explicitly withholds confirmation that it represents the complete approved training scope. The interpretation remains unresolved. **PREMATURE_DOWNGRADE** shows that a desire to lower concern is not an evidentiary basis.

**VALID_B19_CAUSE_DOWNGRADE** assumes, *only inside its separate variant*, a complete approved B19 addendum, a valid bounded negative observation and a declared source safeguard. It supports a **limited reduction in the B19 outside-training concern** without establishing human attribution or every service outcome. The source-protected label is an invented premise, not verified by this program.

**DOWNGRADE_WITH_PRESERVATION_OPEN** uses the same invented task-scope and quiet-observation premises but **without** a source safeguard. Concern about the B19 explanation may narrow while preservation work remains time-sensitive. These two results are intentionally different.

### EX014 — Worked result

| Answerable question | Supplied starting point | Authorized next source | Result that changes triage |
|---|---|---|---|
| Was B19 an approved training task? | R9 shows an edit; R10 lists B17/B18 but not B19 | Training owner and a dated, approved task list or addendum | A valid addendum including B19 would strengthen H1; a complete list excluding it would weaken H1 further |
| Are bookings beyond B19 inconsistent with an owner-approved state? | R11 is a patron report; R16 requests an impact check | Service owner authorizes a narrow booking-audit and schedule comparison | Additional confirmed mismatches would increase potential harm and urgency |

The first question tests authorization; the second tests scope. Neither a missing addendum nor an empty narrow query proves the opposite claim without checking source completeness and coverage.

**TRI2 evidence layers:** In row one, R9 supplies an edit and R10 omits B19 from the supplied plan. A dated, complete, approved task addendum that explicitly names B19 could narrow the *task-scope* concern; a complete approved list that excludes it would strengthen that concern. Neither identifies the human operator. In row two, R11 is a patron report and R16 asks for impact assessment. A service-owner-authorized comparison of current authoritative values with approved targets could establish a bounded booking mismatch or show that the selected booking is correct. It would not count every affected patron or settle the cause of an audit edit.

### EX015 — Worked result

| Hypothesis | Support | Contradiction or limit | Narrow authorized check | Result that weakens it |
|---|---|---|---|---|
| H1: training explains the edits | R6 records training; R10 names B17/B18 | R10 omits B19; R12 does not recall that edit | Training owner confirms the complete approved task list and addenda | A complete approved list still omits B19 |
| H2: account used outside the plan | R9 records B19 changed under `desk-a` | R13 omits device and location; R12 is a recollection, not identity proof | Incident and identity owners authorize narrowly scoped session detail | A documented authorized B19 task with consistent identity evidence would weaken this explanation, though not prove every edit was safe |
| H3: patron display and stored state diverge | R11 reports a wrong-looking time | R9 is an application audit edit; a display fault alone does not explain it | Service owner compares patron view, authoritative state and edit history for B19 | Both views show the same incorrect underlying value, weakening a *display-only* explanation |

The hypotheses need not be mutually exclusive. A good answer identifies what each check can and cannot settle.

| Transformation and original | Fixture transcribes two rows as UTF-8 text; the book table is the retained source of the classroom transcription |
| Limitation | No production log was acquired; a saved file cannot prove the source system's completeness, clock or identity attribution |

If the learner ran `fixture.py`, replace the planned state with **completed local fixture**, record the actual creation time and scratch path, and attach the measured 235-byte SHA-256 value from the lab. Never invent a 09:20 collection time simply because the scenario's discovery checkpoint was 09:20.

**MIN2 worked extension:**

The script writes **235 bytes** to each file. The SHA-256 digest for `E1.txt` is `dc973f580305633eb0a75317c5bdbd9886a8fc015e14a0b17bae09be5e3a6e37`; the digest for `E1-modified.txt` is `15287410550f021dcb81e10fc1833297ffa840ee8ffa8e75867de36df64ffa4d`. The strings have equal byte length because the single ASCII digit `3` was replaced with `4`; their different digests show the modified copy is not byte-identical to the saved original. Learners should calculate the values locally rather than trust a copied answer.

A model note is: “`HL-IR-001/E1`; synthetic classroom extract transcribed from book records R9 and R14; event times 09:03 and 09:12 UTC; learner-created local file `E1.txt` in a scratch directory at the learner's actual collection time; classroom authorization permits only this supplied material; 235 bytes written by `fixture.py` without a live source; SHA-256 digest recorded above; working copy stored locally and deleted after the exercise.” The collection time should be the learner's actual time, not an invented 09:18 UTC. The output is **not** an original application log, and R14 covers only its queried range. Matching digests after a repeat check support byte consistency of the checked copy; they do not prove authorized account use, complete source records or the cause of B19's change.

### Chapter 2 temporal-coverage lab — worked result

The optional Python script prints the following three lines for the supplied fixture:

```text
R9 event=09:03 UTC seen=09:20 UTC delay=17 min
R10 event=09:04 UTC seen=09:20 UTC delay=16 min
R15 event=09:14 UTC seen=09:20 UTC delay=6 min
```

R10's original exercise text is `2026-10-11T05:04:00-04:00`; adding the explicit four-hour offset yields `09:04 UTC`. The three delays are `09:20 − 09:03 = 17`, `09:20 − 09:04 = 16` and `09:20 − 09:14 = 6` minutes. The event-time order is R9, R10, R15; the learner receives all three only with the Round B release at 09:20. None can justify the learner's 09:05 decision retroactively.

With exercise-only T1, the strongest negative statement is: “The specified `application-audit` query for `desk-a` booking edits in `09:00 ≤ event < 09:12 UTC` showed no further matching edit after R9.” R14 *without* T1 lacks those exact bounds. Neither version proves that no edit occurred after 09:12, through another account or in an unexamined source. A bounded request to the authorized application custodian should specify source, account filters, the new interval, an ingestion/completeness check, collector and collection time. R15 calls for a prompt retention decision; the exact deletion instant depends on policy detail not supplied here. A full-credit answer records these limits rather than filling gaps with confident words.

### Chapter 2 delayed-arrival T2 replay — worked result

The optional in-memory program prints:

```text
09:12 L1
09:20 L1,L2
```

Both runs use the same account filter and **09:00 ≤ event < 09:12 UTC** window. L1 qualifies in both. L2's event time is 09:10, so it belongs to that window, but its 09:18 ingestion time makes it invisible at the 09:12 query cutoff and visible at 09:20. L3 is excluded because its account is `helper-b`, even though its event and ingestion times are inside the interval. L4 is excluded because 09:12 is the *exclusive* end; its later ingestion time is not the reason it fails this particular selection.

The strongest correction is: “At 09:12, the specified query showed no other visible matching edit after L1; this did not establish that the event-time interval was complete.” In the T2 replay, the repeated query would later reveal L2 and require a fresh assessment, but **L2 is not a canonical Harbor Library case fact**. The next request is to the fictional application/logging custodian: “Please confirm the exact source, `desk-a` account filter, half-open event interval, each query's run and ingestion cutoff, and whether collection or indexing lag could leave relevant rows unseen; provide a scoped follow-up result under the incident lead's approval.” The custodian's reply, not the newest event timestamp alone, would determine what completeness claim is defensible. None of the four L rows establishes the human operator or intent.

