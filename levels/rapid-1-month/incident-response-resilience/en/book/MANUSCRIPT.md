```python
from hashlib import sha256
from pathlib import Path

payload = (
    b"case_id|record_id|time_utc|source|observation\n"
    b"HL-IR-001|R9|2026-10-11T09:03:00Z|booking-audit|desk-a changed B19 from Room 1 to Room 3\n"
    b"HL-IR-001|R14|2026-10-11T09:12:00Z|application-audit|no further edits in the queried range after R9\n"
)
with Path("E1.txt").open("xb") as output:
    output.write(payload)
saved = Path("E1.txt").read_bytes()
print(len(saved), sha256(saved).hexdigest())

altered = saved.replace(b"Room 3", b"Room 4")
with Path("E1-modified.txt").open("xb") as output:
    output.write(altered)
print(len(altered), sha256(altered).hexdigest())
```

**Failure-path check: two exclusive creations are not one atomic transaction.** The required new empty directory avoids ordinary filename collisions. Python's [exclusive-create file mode](https://docs.python.org/3.13/library/functions.html#open) refuses to overwrite an existing target, but each call protects only its own file. In a separately labeled failure rehearsal where only `E1-modified.txt` already exists, the first write can create E1 and print its digest before the second write raises `FileExistsError`. That is a **partial local attempt**, not completion of both files and not an overwrite of the pre-existing file. Record which file was actually created, which operation failed and what was left unchanged. Stop; do not delete the existing object or switch to an overwrite mode to obtain the expected transcript. A new authorized empty directory permits an independent attempt with its own recorded state.

For a collection note, record the actual local time when the creation is performed. A recorded start/end interval may honestly bound the operation; a later observation time or filesystem timestamp with unverified semantics must not be relabeled as an exact creation receipt. When a time was not recorded, say so. The synthetic 09:20 review does not supply a local acquisition time.

**Procedure.** First, predict whether both files will have the same byte length and whether their SHA-256 digests will match. Then run the script and record both output lines. Read `E1.txt` and `E1-modified.txt` to locate the intentional one-byte change. Re-run the first digest on `E1.txt` and compare it with the saved value. Finally write a collection note identifying the exact file, byte count, local collection time, synthetic source, authorized classroom scope, transformation and storage location. If you cannot run Python, reason from the displayed bytes and use the worked result to check your conclusion; software execution is not required to answer the conceptual question.

The byte count is a useful reproducibility check, but equal length is not equal content. A matching digest on `E1.txt` at two checks supports the limited statement that **the bytes checked were the same at those two times**, assuming the digest calculation and recorded values are trustworthy. A differing digest for the deliberately altered copy shows that this check detects that particular edit. Neither result verifies the truth of R9 or R14, completeness of the original query, correctness of a clock, identity of the editor, legal authority or whether data left the service. The example uses SHA-256 as an integrity check, not as proof of authenticity.

**Expected submission:** the two byte counts and digests, one sentence explaining why the hashes differ, a collection note for `E1.txt`, and two explicit limits on the integrity claim. **Rubric:** one point each for correct byte/digest comparison, correctly identified modification, complete source-and-authority note, and limits that distinguish copy integrity from source truth. A score of 4/4 means the classroom task is reproducible, not that a real forensic process has been completed. The exact expected output and a model note are in the final worked-results section after EX026.

#### 2.6 Temporal coverage lab: what the analyst knew, and when

A useful timeline has at least two clocks: **event time**, as recorded by a source, and **discovery time**, when the responder received or recognized that record. A third time, **collection time**, marks when a copy was created and should be recorded separately. A query also has a **coverage interval**: the source and filters searched, the beginning and end of the search, and any ingestion delay or missing fields. These fields answer different questions. Sorting on one timestamp without naming which clock it represents can produce a fluent but false case history.

    try:
        release_interval(text, rows[0][2])
    except ValueError as exc:
        print(f"{label}: {exc}")
    else:
        raise AssertionError(label + " was not rejected")
```

**Time-label clarification and input contract:** `source` means the source-card time: an edit for R9, a plan record for R10, and a retention notice for R15. `released` means the learner's 09:20 release. The dates and offsets are the existing synthetic fixture, not new case evidence. This minute-aligned exercise requires an explicit UTC offset and refuses a source timestamp later than its release under the assumed comparable clocks. It rejects sub-minute values rather than silently rounding them. This is not a general RFC 3339 validator or a real clock-verification tool. In particular, Python's [datetime documentation](https://docs.python.org/3.13/library/datetime.html#datetime.datetime.astimezone) explains that converting a naive datetime can use the machine's local timezone; this program rejects that ambiguity before conversion.

Predict the original three intervals and all four rejection reasons before running. None of the malformed-input controls is an R-series event. A chronological rejection calls for investigation of timestamp meaning and clock assumptions; it does not establish malicious activity. Keep ingestion, query execution and copy creation unknown when they have no separate evidence.

**Procedure:** (1) Before running it, convert R10's offset time by hand and predict the three source-to-learner-release intervals. (2) Run the code in an authorized local scratch environment, or calculate the outputs from the shown values if Python is unavailable. (3) Make a three-row table with record ID, original timestamp including offset, normalized UTC source-card time and kind, learner-release time, source-to-learner-release interval and whether the record was available at 09:05. (4) Draw the coverage interval from T1 as `09:00 ≤ event < 09:12 UTC` and put R9, the T1 end and the 09:20 review on it. (5) Write two sentences: the strongest conclusion supported by R14 with T1, and the next *authorized* check needed to assess activity after 09:12. Keep the R15 retention notice separate from any assumed deletion instant.

##### EX021 — Time ordering

**Objective:** separate event order from causal inference. **Inputs:** R9, R10, R12, R15 and R16; use T1 only for the optional final sentence. **Output:** five ordered rows with ID, UTC event time, source and one uncertainty about cause. Mark that R9–R16 reached the learner at 09:20 despite earlier event times. Optionally state which interval T1 leaves uncovered. A score of 2 preserves event/discovery separation and does not treat temporal precedence as authorization or attribution.

**Worked answer:** [EX021 in the final appendix](#ex021--worked-result).

<!-- open-cyber-academy:lesson-navigation:start lesson-07 -->
#### Continue studying — lesson 07 of at least 20

[← Lesson 06](#lesson-06) · [Course lesson index](../SUBJECTS.md) · [Lesson 08 →](#lesson-08)

Continue to the next authored daily lesson.
<!-- open-cyber-academy:lesson-navigation:end -->

**MIN2 worked extension:**

Matching E1 SHA-256 values at two actual checks support only a bounded consistency claim about the **specified copied bytes** and method. They do not show that the source was complete, correctly timed, lawfully collected or authorized for broader distribution. A technical reviewer may need a derived view with unnecessary contact fields excluded. The view's field policy, row scope and transformation receipt must be recorded separately from the raw copy's integrity comparison. Neither redaction nor a digest establishes anonymization or human attribution; those require their own substantiation.

### EX021 — Worked result

| Order | Record and supplied UTC time | Source |
|---:|---|---|
| 1 | R9, 09:03 | Booking audit: B19 edit |
| 2 | R10, 09:04 | Training plan: B17/B18 named |
| 3 | R12, 09:08 | Staff interview note |
| 4 | R15, 09:14 | Retention notice |
| 5 | R16, 09:16 | Service-owner note |

These are **record event or observation times** in the fictional dataset. The learner first receives R9–R16 at the simulated 09:20 review. R10's timestamp is the time of the supplied plan record, not proof that the plan itself was first written after R9. Ordering cannot establish who made the B19 edit, whether it was authorized or whether it caused the patron's report. If optional T1 is used, its interval ends before 09:12; it supplies no coverage of later activity.

### EX022 — Worked result
