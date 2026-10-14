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
saved_altered = Path("E1-modified.txt").read_bytes()
print(len(saved_altered), sha256(saved_altered).hexdigest())
```

**Failure-path check: two exclusive creations are not one atomic transaction.** The required new empty directory avoids ordinary filename collisions. Python's [exclusive-create file mode](https://docs.python.org/3.13/library/functions.html#open) refuses to overwrite an existing target, but each call protects only its own file. In a separately labeled failure rehearsal where only `E1-modified.txt` already exists, the first write can create E1 and print its digest before the second write raises `FileExistsError`. That is a **partial local attempt**, not completion of both files and not an overwrite of the pre-existing file. Record which file was actually created, which operation failed and what was left unchanged. Stop; do not delete the existing object or switch to an overwrite mode to obtain the expected transcript. A new authorized empty directory permits an independent attempt with its own recorded state.

For a collection note, record the actual local time when the creation is performed. A recorded start/end interval may honestly bound the operation; a later observation time or filesystem timestamp with unverified semantics must not be relabeled as an exact creation receipt. When a time was not recorded, say so. The synthetic 09:20 review does not supply a local acquisition time.

**Procedure.** First, predict whether both files will have the same byte length and whether their SHA-256 digests will match. Then run the script and record both output lines. Read `E1.txt` and `E1-modified.txt` to locate the intentional one-byte change. Re-run the first digest on `E1.txt` and compare it with the saved value. Finally write a collection note identifying the exact file, byte count, local collection time, synthetic source, authorized classroom scope, transformation and storage location. If you cannot run Python, reason from the displayed bytes and use the worked result to check your conclusion; software execution is not required to answer the conceptual question.

The byte count is a useful reproducibility check, but equal length is not equal content. A matching digest on `E1.txt` at two checks supports the limited statement that **the bytes checked were the same at those two times**, assuming the digest calculation and recorded values are trustworthy. A differing digest for the deliberately altered copy shows that this check detects that particular edit. Neither result verifies the truth of R9 or R14, completeness of the original query, correctness of a clock, identity of the editor, legal authority or whether data left the service. The example uses SHA-256 as an integrity check, not as proof of authenticity.

**Expected submission:** the two byte counts and digests, one sentence explaining why the hashes differ, a collection note for `E1.txt`, and two explicit limits on the integrity claim. **Rubric:** one point each for correct byte/digest comparison, correctly identified modification, complete source-and-authority note, and limits that distinguish copy integrity from source truth. A score of 4/4 means the classroom task is reproducible, not that a real forensic process has been completed. The exact expected output and a model note are in the final worked-results section after EX026.

<a id="ir-rapid-l07-copy-checkpoint"></a>

##### A digest needs an object, a check time and a bounded claim

The E1 exercise has two different objects before its second file is read: `altered`, a byte string in the Python process, and `E1-modified.txt`, a named file. Hashing the first describes the intended output buffer. Reading the second and hashing the returned bytes describes what that read obtained from the named file. Those claims can agree in an ordinary successful run, but they are not the same measurement.

The revised listing above uses `saved_altered = Path("E1-modified.txt").read_bytes()` after the second file is closed and computes its second printed result from `saved_altered`. The first file already used this read-back pattern. The payload, intentional one-byte change and two expected output lines are unchanged. Python's [Path.read_bytes documentation](https://docs.python.org/3.13/library/pathlib.html#pathlib.Path.read_bytes) describes reading a file's binary contents; [exclusive creation](https://docs.python.org/3.13/library/functions.html#open) addresses a different question: whether an existing filename is overwritten.

Neither operation authenticates the original producer, verifies a storage device's crash durability, locks out a concurrent writer or records an uninterrupted custody history. Use the authorized private scratch environment specified above, rather than a shared or adversarial directory. A read-back error is a failed measurement, not a reason to substitute the intended buffer and label it a successful file check. Record the actual partial state and error; leave unperformed checks unperformed.

A reproducible integrity statement therefore needs at least the **named object**, the **bytes or digest actually measured**, the **check time or recorded operation interval**, and the **comparison reference**. The reference must be preserved as a separate record. Computing a new digest and silently replacing the old reference does not explain an unexpected difference. A timestamp in the file describes its content; it is not the time at which the analyst created or checked that file.

```text
Intended byte string --write--> Named local file --read--> Bytes obtained
       |                                                     |
       v                                                     v
Hash of intended output                              Hash of this read
                                                             |
                                             Compare with retained reference
                                                             |
                                             Report object, time and limits
```

**Text alternative:** A buffer hash measures the buffer. A file read produces the bytes for a file-check hash. Compare that measured value with the retained reference and identify the check's time and object. None of these steps establishes source truth, full query coverage, uninterrupted custody or production collection authority.

###### Equal endpoints do not reconstruct the interval between them

Suppose an authorized reviewer checks a copy at two instants and obtains the same digest. That is useful evidence about those observations. It cannot establish that the copy remained unchanged at every unobserved instant between them. The distinction does not require a hash collision: a byte sequence could change and later be replaced by exactly the original sequence.

The following independent example supplies three **invented in-memory states**, named first, middle and last. They are not observations of E1, an R-series record or a real storage system. The middle state is supplied solely to make two possible histories distinguishable. Run this complete Python 3 listing in a fresh session. It creates and changes no files and needs no network access.

```python
from hashlib import sha256

# Independent in-memory illustration, not E1 or an R-series record.
original = b"practice-value=3\n"
changed = b"practice-value=4\n"

histories = {
    "UNCHANGED": (original, original, original),
    "CHANGED_THEN_SAME": (original, changed, original),
    "CHANGED_AT_END": (original, changed, changed),
}
for label, states in histories.items():
    first, middle, last = (sha256(value).hexdigest() for value in states)
    print(f"{label} endpoints_equal={first == last} "
          f"middle_equals_first={middle == first}")
```

**Work the example before running:** `UNCHANGED` and `CHANGED_THEN_SAME` have exactly the same first and last bytes. An observer given only those endpoints cannot distinguish their histories. The supplied middle observation separates them. `CHANGED_AT_END` instead leaves different bytes at the final observation, so the endpoint comparison detects that particular change. The program illustrates limited observability; it does not determine who changed a file, whether any real change occurred, or how a production evidence store should be implemented.

The appropriate wording is **“the measured values matched at the two recorded checks”**, not **“the copy could never have changed.”** Additional authorized custody records, access controls and observations may strengthen a real preservation account, but their existence and scope must be evidenced separately. A third matching sample would still not observe every instant. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) provides source-aware forensic guidance in an IT response context, not a certification that this classroom copy has legal evidentiary standing.

###### Independent checkpoint practice

First predict and then reproduce the program's three lines. Submit three claim-review rows with `claim | supported finding | missing evidence | next safe step` for these deliberately faulty statements: **A**, “the former `sha256(altered)` expression was a read-back of the second file”; **B**, “matching endpoint hashes prove the copy never changed”; and **C**, “the second exclusive creation failed, so the first file was never created.” For C, use the explicitly supplied failure scenario in which only `E1-modified.txt` existed initially and the first output line was printed. Do not infer that scenario from every possible error.

Then predict the E1 program's outcome for four separately prepared starting states: neither output name exists; only E1 exists; only E1-modified exists; both exist. Record expected printed-line count, whether either new file is created and which existing bytes must remain untouched. These are predictions unless actually tested. The ordinary learner run still requires a fresh authorized directory with neither output present; do not delete an existing object to create a convenient starting state.

Use EX019's existing collection-note format to record only what was actually created and measured. Keep EX020's five claim rows, adding the endpoint limitation to their existing explanations rather than treating it as a new exercise. This supplementary checkpoint does not change the course's exercise count or confer collection authority. Assess the artifact by whether the learner identifies the measured object, preserves the initial and partial states, limits the endpoint inference and proposes a source-supported next check. [Worked checkpoint answer](#ir-rapid-l07-copy-checkpoint-result).

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

##### Interpret the time field before ordering the records

A timestamp's **representation** and its **meaning** are different. Converting `05:04-04:00` to `09:04 UTC` preserves the represented instant; it cannot tell us whether that instant is an operation, a plan record, an approval, a source query or an analyst's later acquisition. Sorting correctly formatted values without identifying those meanings can create a false causal or authorization sequence.

For example, a faulty reading says: “R9's edit is at 09:03 and R10's plan is at 09:04, therefore the operation preceded its authorization.” The ordering of the two supplied record times is correct, but the conclusion needs an **effective authorization time** that R10 does not provide. The plan-record time is not proof of when the plan was first written or approved. Ask the training owner for the applicable version and approval evidence; do not infer that authorization was either present or absent from this ordering alone.

The same error can create a fabricated preservation deadline. R15's 09:14 timestamp belongs to a **retention notice**. It is not a supplied retention-start timestamp for R9. Neither adding 24 hours to 09:14 nor adding it to R9's 09:03 establishes a deletion instant without the source policy's actual anchor and enforcement semantics. Keep the loss concern visible while the custodian clarifies it.

For EX021, retain five rows and annotate each supplied timestamp with its kind: R9 reports an edit; R10 identifies a plan record; R12 an interview note; R15 a retention notice; R16 a service-owner note. A note's timestamp is not automatically the time of every action discussed in it. Add a specific uncertainty in each row, not one general disclaimer that hides which inference is missing. The common 09:20 learner release remains a separate field or table note; it is neither a source event nor evidence that a local copy was created.

**Independent self-check:** Before opening EX021's final answer, explain why a plan-record time cannot settle prior authorization and why a notice time cannot start an unprovided deletion clock. Then identify the owner and missing record that could resolve each question. Correct arithmetic, correct source-time meaning and sufficient evidence for a decision are three separate requirements.

Predict the original three intervals and all four rejection reasons before running. None of the malformed-input controls is an R-series event. A chronological rejection calls for investigation of timestamp meaning and clock assumptions; it does not establish malicious activity. Keep ingestion, query execution and copy creation unknown when they have no separate evidence.

**Procedure:** (1) Before running it, convert R10's offset time by hand and predict the three source-to-learner-release intervals. (2) Run the code in an authorized local scratch environment, or calculate the outputs from the shown values if Python is unavailable. (3) Make a three-row table with record ID, original timestamp including offset, normalized UTC source-card time and kind, learner-release time, source-to-learner-release interval and whether the record was available at 09:05. (4) Draw the coverage interval from T1 as `09:00 ≤ event < 09:12 UTC` and put R9, the T1 end and the 09:20 review on it. (5) Write two sentences: the strongest conclusion supported by R14 with T1, and the next *authorized* check needed to assess activity after 09:12. Keep the R15 retention notice separate from any assumed deletion instant.

##### EX021 — Time ordering

**Objective:** order source-reported times without inventing operation, approval or collection times. **Inputs:** R9, R10, R12, R15 and R16; use T1 only for the optional final sentence. **Output:** exactly five ordered rows with ID, supplied UTC time, source and time kind, and one specific uncertainty or unsupported inference for that row. Mark the common 09:20 learner release separately from these source-card times; it does not supply local collection or source-ingestion times. Optionally state which interval T1 leaves uncovered, including its exclusive end. A score of 2 identifies the edit, plan-record, interview-note, retention-notice and service-owner-note times correctly, preserves the learner-release boundary, and does not turn record order into proof of authorization, attribution or a deletion deadline.

**Worked answer:** [EX021 in the final appendix](#ex021--worked-result).

<!-- open-cyber-academy:lesson-navigation:start lesson-07 -->
#### Continue studying — lesson 07 of at least 20

[← Lesson 06](#lesson-06) · [Course lesson index](../SUBJECTS.md) · [Lesson 08 →](#lesson-08)

Continue to the next authored daily lesson.
<!-- open-cyber-academy:lesson-navigation:end -->

**MIN2 worked extension:**

Matching E1 SHA-256 values at two actual checks support only a bounded consistency claim about the **specified copied bytes** and method. They do not show that the source was complete, correctly timed, lawfully collected or authorized for broader distribution. A technical reviewer may need a derived view with unnecessary contact fields excluded. The view's field policy, row scope and transformation receipt must be recorded separately from the raw copy's integrity comparison. Neither redaction nor a digest establishes anonymization or human attribution; those require their own substantiation.

<a id="ir-rapid-l07-copy-checkpoint-result"></a>

### Lesson 07 copy-checkpoint practice — worked result

The independent [in-memory example](#ir-rapid-l07-copy-checkpoint) prints:

```text
UNCHANGED endpoints_equal=True middle_equals_first=True
CHANGED_THEN_SAME endpoints_equal=True middle_equals_first=False
CHANGED_AT_END endpoints_equal=False middle_equals_first=False
```

The first two histories have identical endpoint bytes, not merely coincidentally equal digests. Their supplied middle states differ. The third history leaves a different final value. Thus the endpoint comparison detects the third example but cannot distinguish the first two without the middle observation. The program does not establish that E1 or any actual evidence was modified.

| Faulty claim | Supported finding | Missing evidence | Next safe step |
|---|---|---|---|
| A — The former buffer hash was a second-file read-back | The former expression `sha256(altered)` measured the in-memory byte string. The revised listing hashes `saved_altered`, obtained by reading the named file. | The former expression by itself had no second-file read result or check receipt. | Read the permitted file, retain the measured digest and check time, and identify the object. Do not relabel an intended value as a measurement. |
| B — Matching endpoints prove no intervening change | The values matched at the two recorded checks, subject to the method and reference being trustworthy. | The unobserved interval and an independently supported custody history. | Keep the endpoint result narrow; request relevant authorized custody/access records when the decision requires them. Do not allege a modification merely because it cannot be excluded. |
| C — Second-file failure means nothing was created | In the specified second-name collision, E1 was created and its read-back result printed before the failure. | Successful second-file creation and read-back are absent. | Record the partial attempt, preserve E1 and the pre-existing second file, and stop. A separate fresh authorized directory permits a new attempt, not a rewrite of the first one. |

For the four deterministic filename-collision scenarios, assume ordinary local files, successful permitted operations up to any collision, and no concurrent changes:

| Names present before the run | Printed result lines | Newly created files | Existing bytes |
|---|---:|---|---|
| Neither | 2 | E1.txt and E1-modified.txt | No previous output file exists in this scenario |
| E1.txt only | 0 | None; the first exclusive open raises `FileExistsError` | E1.txt remains unchanged; E1-modified.txt is not created |
| E1-modified.txt only | 1 | E1.txt only; the second exclusive open raises `FileExistsError` | The pre-existing E1-modified.txt remains unchanged |
| Both | 0 | None; the first exclusive open fails before the second is attempted | Both remain unchanged |

These expected states were reproduced for the original and revised listings with Python 3.13.5 in separate local test directories. The successful revised run reread both files and reproduced the existing 235-byte counts and published digests. A repeat run in a successful directory failed at the first exclusive open without changing either file. These checks cover the declared local cases, not every filesystem failure, competing writer or durability guarantee.

The EX019 note must distinguish a **planned transcription**, a **completed local file**, and a **partially completed attempt**. A failed overall run does not erase the first successful operation. Conversely, a first printed line does not prove that both files were created. A later check time is not an exact creation time unless a separate record substantiates that claim. The fictional 09:20 release supplies neither local timestamp.

For EX020, keep two supported and three unsupported claims. In the supported consistency row, specify the two actual checks and state that an intervening change-and-return is not excluded by those endpoints. In the unsupported rows, retain the separate limits on source completeness/truth, source clock/human identity and collection authority. The new read-back does not upgrade any of those claims.

[Return to the checkpoint](#ir-rapid-l07-copy-checkpoint) · [EX019](#ex019--worked-result) · [EX020](#ex020--worked-result) · [Lesson 08](#lesson-08)

### EX021 — Worked result

| Order | Record and supplied UTC time | Source and time kind | Specific uncertainty or unsupported inference |
|---:|---|---|---|
| 1 | R9, 09:03 | Booking audit; reported B19 edit time | The account label does not identify the human or prove the edit was authorized. |
| 2 | R10, 09:04 | Training plan; supplied plan-record time | This is not an effective approval time or proof that the plan was first written after R9. Ask the training owner for the applicable version and approval evidence. |
| 3 | R12, 09:08 | Staff interview note; supplied note time | The recollection does not establish the time of every recalled action, the completeness of the task list or who performed the B19 edit. |
| 4 | R15, 09:14 | Retention notice; supplied notice time | The source's retention-start anchor and actual deletion deadline remain unknown; this notice does not start a new 24-hour clock. |
| 5 | R16, 09:16 | Service-owner note; supplied note time | Requesting an impact check and describing pause authority do not establish that the check or pause was approved and executed. |

**Separate availability note:** All five cards first become available to the learner with R9–R16 at the simulated **09:20** review. None may justify the earlier 09:05 R1–R8 decision. These are differently typed source-card times, not five instances of a single operation clock. No local copy-creation time, source-ingestion time or completed collection follows from this table.

The supplied order is R9 → R10 → R12 → R15 → R16. It cannot establish who made the B19 edit, whether it was authorized or whether it caused the patron's report. R10's record time does not date the plan's first authorship or effective approval; R15's notice time does not anchor deletion. The training owner and source custodian would need to supply those distinct missing records through the authorized route. Those requests remain proposed.

If optional T1 is used, its event-time interval is **09:00 ≤ event < 09:12 UTC**. It excludes an event exactly at 09:12 as well as later events. Its specified window and account filter do not establish ingestion completeness. Without T1, canonical R14's exact window remains unspecified. A full-credit answer gives a limit for each of the five rows, not merely a correct sort.

### EX022 — Worked result
