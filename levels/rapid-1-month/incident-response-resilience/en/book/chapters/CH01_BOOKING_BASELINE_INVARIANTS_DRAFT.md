# Incident Response and Cyber Resilience — Rapid Course
## Chapter 01 Supplementary Expansion Draft: Normal Booking Behavior and Service Invariants

**Editorial status:** **Public transitional instructional draft** for Chapter 01 of the course's **single principal English book**. This is not a separate volume, a completed chapter, an A4-verified publication or an additional curricular subject.
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).
**Integration target:** [Chapter 01 — Incident readiness, roles and authorized scope](../MANUSCRIPT.md#ch-01).
**Specific gap addressed:** Defining and safely testing the expected **business behavior** of a room-booking service before an incident, rather than inferring correctness from available logs, component uptime or a plausible explanation.
**Existing content to preserve:** D1 evidence-readiness contract, R1–R8 claim-review lab, roles and authority matrix, incident record, and all existing numbered exercises.

> **Fiction and chronology:** Harbor Library is entirely fictional. The canonical 09:05 Round A decision uses R1–R8 only. R9–R16, R17–R24, later case branches and P1/C1/V1 are not available at that decision. The independent BSL1 fixture below is invented for this supplementary classroom lesson and does **not** add bookings, events or observations to the canonical Harbor Library case.

# New Chapter 01 Teaching

### 1.A What does it mean for a service to work correctly?

Incident readiness is easier to discuss when the organization can explain what its service promises to legitimate users. A web page can respond while the function behind it is wrong. For a study-room service, a patron may see a confirmation yet not obtain a valid room, or may see a cancellation while the room remains unavailable to someone else. These situations have different operational causes, but they illustrate a common preparation problem: knowing that software is reachable is not enough to specify a correct business outcome.

The current Chapter 01 identifies the booking application, staff identity service, database, backup and help desk. That **service map** names components and owners. Its D1 **evidence-readiness contract** asks which source might record a relevant event, what its fields mean and whether the team could retrieve it responsibly. The separate question developed here is: **What observable condition would mean that the booking service met a defined business requirement?**

A **behavior baseline** is a documented description of acceptable operation in a specified version and context. It might identify which reservation states are valid, when a room is occupied, whether a cancellation releases a slot, how overlapping times are handled and what should happen to an invalid request. The rule's owner must be clear. A responder should not invent the booking policy during an incident merely to make a preferred theory fit the data.

This is related to identifying important services and their consequences for organizational risk. The [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) organizes ongoing cybersecurity risk management, and [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates incident-response preparation with those risk-management activities. Neither source prescribes the booking rules in this example. The rules are deliberately fictional, but the discipline of defining and testing a service outcome is reusable.

At introductory level, the learner should ask three questions: What legitimate task does the user expect to complete? What result would be unacceptable even though the application remains reachable? Which conditions must be specified before we can judge that result? A clear answer is more useful than an unexplained green health indicator.

### 1.B Trace the legitimate user journey before imagining an attacker

A useful behavior baseline begins with a normal user journey. In a hypothetical Harbor Library service, a patron chooses a room and time, submits a request, receives an accepted or rejected response and later looks up the resulting booking. A permitted staff member might move or cancel that booking. The canonical R1–R8 table does not specify actual endpoints, database transaction rules or the organization's full approval workflow, so this journey is a **proposed teaching model**, not a verified implementation.

Break the proposed journey into small outcomes:

| User intention | Expected result under an approved policy | Negative behavior worth testing |
|---|---|---|
| Search for a slot | Available times follow the room's accepted occupancy rules | A confirmed occupied slot is shown as free |
| Request a booking | A permitted, conflict-free request receives a consistent outcome | A conflicting booking appears accepted |
| Change a booking | Only the requested, permitted object changes | The wrong booking or room changes |
| Cancel a booking | Its state is recorded and occupancy is updated under the policy | A cancelled room remains blocked without justification |
| Review a booking | The view reflects the correct booking and relevant update rules | An obsolete or unrelated reservation is displayed |

The table does not establish that any of these errors happened in the canonical case. It describes the **questions an owner-approved rehearsal could test** before an incident. The behavior criteria should be defined in words a front-desk worker can understand. If the requirement cannot be explained without the name of a programming framework or database product, it may be too tied to implementation detail to express the actual user promise.

Notice also that the positive and negative outcomes are different. Showing that one ordinary reservation succeeds does not show that an invalid overlap will be rejected. Showing that a cancellation returns a success response does not show that the correct room became available. Readiness requires a small set of independent questions, not one vaguely successful demonstration.

The journey should include its *boundaries*: the intended room type, the time period tested, permitted roles and what counts as a completed booking. A library might have shared rooms or provisional reservations, but those capabilities are not specified in the exercise. The learner must not assume them simply to explain an observed problem away.

### 1.C Convert vague expectations into testable invariants

An **invariant** is a property that should stay true whenever its stated conditions apply. For a simplified single-occupancy study room, one plausible rule is that two **confirmed** bookings must not occupy overlapping time intervals in the same room. A second rule may be that a cancelled booking does not occupy its old slot. A third may require every accepted interval to end later than it starts.

An invariant is useful only with a complete contract:

1. **Scope:** Which rooms, statuses, time representation and application version does the rule cover?
2. **Preconditions:** What must be true before applying the rule?
3. **Expected behavior:** Which values are valid and which must fail?
4. **Verification:** What result would demonstrate compliance for the selected inputs?
5. **Failure meaning:** What can be concluded when the check fails, and what remains uncertain?

For the BSL1 teaching fixture, the scope is intentionally narrow: one fictional day, single-occupancy rooms, two recognized statuses and six synthetic booking objects. Other status meanings and room-sharing rules are not silently invented. The invariant applies to this model alone.

A testable rule is better than "the system should not make mistakes." For example: "Under the single-occupancy rule, no two confirmed rows with the same room may have intersecting half-open time intervals." The rule specifies both the objects and the condition. It also supplies a falsifier: one correctly interpreted pair of confirmed same-room overlapping intervals would violate the stated policy.

That finding would still not identify the cause. It might result from a programming defect, administrative action, race condition, test-data error or misuse. The invariant is about **business-state consistency**. A security incident finding requires a separate investigation of authorization, mechanism and impact.

This separation lets the analyst state a useful technical problem without claiming more than the evidence supports: "The supplied model contains an overlap that violates the declared occupancy rule" is defensible for the fixture; "the attacker stole a staff account and corrupted reservations" is not.

### 1.D Time boundaries are part of service semantics

Room reservations are time-based commitments. If one booking uses Room A from 09:00 to 10:00 and another uses the room from 10:00 to 11:00, their time boundaries meet but do not necessarily conflict. If the first ends at 10:30, the second overlaps it. A policy must specify how it treats starts and ends.

The BSL1 lab uses **half-open intervals**, where the start is included and the end is excluded. In mathematical notation this is [start, end). Under this teaching convention, a 09:00–10:00 booking does not conflict with a 10:00–11:00 booking. A 09:00–10:30 booking conflicts with a 10:00–11:00 booking. A row beginning and ending at 11:00 has zero duration and is invalid.

The overlap condition for two valid intervals is: the first starts before the second ends **and** the second starts before the first ends. Comparing only whether start times are equal misses overlapping intervals with different starts. Treating both endpoints as inclusive creates false conflict reports for adjacent bookings under the declared convention.

These details matter operationally. An invalid time boundary can create a user-visible scheduling defect while the application is technically responsive. A discrepancy may result from ordinary implementation errors, an incorrect policy or a mismatched timezone rather than deliberate malicious behavior.

A real application would also need to define operating hours, timezones, daylight-saving transitions and cross-date reservations. The beginner lab deliberately avoids those extra dimensions by using one fixed fictional day with HH:MM times. This avoids implying that a short teaching parser is a production scheduling implementation.

Also keep **booking time** distinct from **incident evidence time**. R1 and R3 contain source-event timestamps used to understand the canonical case. The BSL1 room intervals describe times when a customer could occupy a space. One type of time is not a substitute for the other. A source event at 08:43 does not mean the reservation it changed was scheduled for 08:43.

### 1.E A reservation's status changes how its interval is interpreted

Consider two records for the same room and time. If both are confirmed, the simplified policy sees a conflict. If one is cancelled, the cancelled record no longer occupies the slot under this rule. Counting every historical row as active would produce false positives; treating every unfamiliar status as harmless could hide real conflicts.

BSL1 recognizes exactly two statuses: **CONFIRMED** and **CANCELLED**. Confirmed bookings participate in occupancy comparisons; cancelled bookings do not. Other values are not mapped automatically. If a new status is introduced by a system change, the service owner must explain how it affects occupancy, and the checker must be updated under a versioned contract before a result is trusted.

A status change can be legitimate or unauthorized. The fact that the cancelled state releases a room **does not** prove the cancellation was approved. Nor does it establish that the user was notified or the historical audit is complete. Those require separate tests and evidence. The original canonical R4 records a B18 cancellation, but it contains no owner-approved target state and does not establish the current occupancy behavior of B18.

The status rule is therefore a **preparation aid**. It lets a team articulate which state would be correct *if* the approved conditions were known. It cannot turn a printed application event into a verified business outcome.

A useful control question is: "If the status input changes while room and time stay constant, which result should change?" The BSL1 negative variant later alters a cancelled item to confirmed and thereby introduces another overlap. This shows that the model is sensitive to the status field rather than hardcoding a preferred answer.

### 1.F Approval of a business rule must be versioned

The meaning of a correct booking can change. A library might introduce shared rooms, alter operating hours, allow temporary holds or change cancellation behavior. In that situation, a test that correctly enforced last year's rule might be wrong for today's approved service.

Each baseline should therefore carry a small **rulebook version** and owner-approved assumptions. Suggested fields include: version, owner, effective date, affected functions, accepted statuses, room categories, time interpretation, sample allowed/forbidden inputs, tested implementation version and a review trigger. These fields define correct business behavior; they do not replace D1's logging fields or the incident response authorization matrix.

Imagine a baseline version that forbids every same-room overlap. A future version might distinguish single-occupancy rooms from a shared study space. A collision in the shared room could then be permitted according to a newly approved rule. The responsible process is to retain both versions, record why the policy changed, and retest the new rule deliberately.

Do not rewrite history by applying a future policy to an older decision without saying so. A test should report which version it checked and whether that version was applicable to the operation being examined.

In the canonical Harbor Library record, R6 only shows that front-desk training was scheduled. It does not supply a complete approved booking-rule version for B17 and B18. The learner can request the relevant business specification from the service owner but cannot assert that BSL1's rules were already active in Harbor Library's actual fictional environment.

A beginner should understand the distinction between "the program is wrong" and "our documented expectation is wrong." Those lead to different next steps. Fixing the program without confirming the policy can create a new error; revising a policy simply to excuse an unexplained failure can conceal a problem. An approved contract and reproducible test help a reviewer identify which assumption requires correction.

### 1.G Baseline violations do not prove cyber compromise

A security alert and a failed business invariant can appear together or separately. Neither automatically explains the other.

Suppose an isolated checker finds two confirmed bookings overlapping in Room B. The result supports a statement about that fixture under its chosen policy. It does not show that a staff credential was stolen. Potential explanations include a logic defect, a malformed import, a manual administrative error, an out-of-date rulebook or intentional unauthorized change. Each explanation would require its own discriminator.

Conversely, an unauthorized account session may exist while every booking invariant still passes. A person might view an unauthorized record without changing a reservation. Thus the absence of a business-state problem does not prove the absence of a security problem.

This matters at the first response checkpoint. An analyst who observes a suspicious sign-in may be tempted to label any later booking error as the attacker's work. But temporal proximity is not causal proof. R1 reports a successful desk-a sign-in, R3 and R4 report booking changes, and R5 records a patron concern. At 09:05, those observations support investigation; they do not provide an authenticated explanation or a current-state comparison against a complete approved baseline.

Use a four-level vocabulary:

- **Requirement specified:** the service owner has defined a rule for a declared scope.
- **Fixture evaluated:** a controlled program has applied that rule to selected teaching inputs.
- **Operational discrepancy verified:** a separately authorized, trustworthy comparison shows that a live service did not meet the applicable rule.
- **Security mechanism established:** independent investigation connects the discrepancy to an unauthorized cause.

BSL1 reaches the second level only. R1–R8 do not prove the third or fourth through association with BSL1. Keeping these claims separate helps the response team investigate a genuine service fault promptly without automatically accusing a user or minimizing a possible security concern.

### 1.H Positive tests, negative tests and control conditions

A useful readiness rehearsal should not simply seek a green result. It should show that valid input is accepted **and** invalid input is rejected under known conditions.

The BSL1 positive example consists of adjacent bookings. One confirmed Room A reservation ends at 10:00, and another confirmed Room A reservation begins at 10:00. Under the half-open convention, the pair does not overlap.

The primary negative example contains confirmed Room B reservations for 09:00–10:00 and 09:30–10:30. Because the intervals intersect, the checker should flag a conflict.

A second negative example is a confirmed booking with start and end both at 11:00. The room itself may be available, but the reservation has invalid duration. The overlap test must not be the sole acceptance rule.

The cancellation control checks a different assumption. A cancelled Room A 09:00–10:00 record is ignored for active occupancy. In a separate variant, changing only that status to confirmed makes it conflict with the existing active booking. The test reveals why the status meaning is essential.

A third sensitivity test removes an overlapping row from a working input. The checker now reports fewer problems. That does not mean the underlying system was repaired; it means the checker no longer sees every relevant object. In a real case, this is the risk of a filtered or incomplete current-state export.

Every one of these results needs a scope limitation. A successful adjacent-interval comparison says nothing about every room or day. A flagged overlap is not a measured patron impact. A missing overlap in an incomplete input is not proof of a safe schedule.

### 1.I Distinguish contract failure, input failure and source absence

When a checker returns a problem, the learner should classify what kind of problem it is.

A **contract failure** occurs when an interpretable input violates the declared business rule—for example, two valid, confirmed bookings overlap in the same single-occupancy room.

An **input-quality failure** occurs when the supplied data cannot be interpreted under the contract. A zero-length interval, duplicate booking identifier or unknown status is not necessarily the same failure as a double booking. It may reflect malformed test data, an exporter defect or an upstream application problem.

A **coverage limitation** occurs when relevant records are absent from the supplied test frame. If an overlapping row is omitted, the checker may report no conflict despite the unchanged larger population. This is not a demonstration that the rule passed in the intended complete scope.

These categories should remain visible in the result. Otherwise the team may investigate application behavior when it actually needs an approved source-quality check, or it may dismiss a genuine conflict as an exporter error without evidence.

The fact that a Python assertion succeeds does not authenticate the input source. For BSL1, this is acceptable because the fixture is intentionally synthetic. A real owner-approved comparison would additionally require a declared source, complete selection, timestamps, access permissions and an authoritative current-state view. Those are separate evidence questions covered by other chapters and D1; the baseline lab does not duplicate them.

A novice should be able to explain the result in one sentence: "In the provided BSL1 data, the checker found one active room conflict and one invalid duration; its broader correctness claims are limited to the six synthetic rows and the stated policy."

### 1.J A contrasting wrong and correct interpretation

**Plausible but incorrect:**

> "R1 shows the attacker signed in. R3 and R4 show the attacker changed bookings. Our new booking test found a double booking, therefore Harbor Library suffered a confirmed attack that damaged its schedule."

This merges unrelated datasets and makes unsupported causal claims. R1 contains an account label, not a verified human identity. R3/R4 record operations without establishing their authorization. The BSL1 test uses S-series objects unrelated to the R-series case. It cannot be treated as new evidence about B17 or B18.

**Defensible classroom interpretation:**

> "At the fictional 09:05 checkpoint, R1–R8 justify asking whether the recorded B17/B18 changes were approved and whether the patron's reported symptom corresponds to the authoritative schedule. The operator, the complete training scope and current business-state correctness remain unresolved. Separately, the BSL1 fixture demonstrates how to define and check two booking invariants on invented objects; those checks make no finding about the Harbor Library incident."

The better interpretation identifies a valid next question while preserving the source boundary. It also avoids saying that an absence of BSL1 findings would clear the account or prove that no data exposure occurred. A business invariant is one useful part of readiness, not a universal security detector.

The official [NIST SP 800-34 Rev. 1 updated edition](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) addresses evaluating systems and operations for contingency requirements and priorities. It does not define Harbor Library's booking policy or confirm any R-series event. The teaching application here is that an organization benefits from understanding critical service outcomes before disruption, rather than inventing a correctness test only after something looks suspicious.

### 1.K Make the baseline portable across a service change

A rule should remain understandable when software or hosting changes. The statement "the database query returned zero rows" depends on a particular implementation and selection. The statement "two confirmed single-occupancy bookings must not overlap in the same room" expresses a business expectation that can be evaluated through different authorized test paths.

That portability supports incident readiness. If a service migrates from a monolith to separate components, its logging sources may change. Its core business promise might remain stable. A behavior baseline gives the service owner a way to recognize whether the migration still produces acceptable results; D1 must separately be updated to identify where evidence can now be collected.

Portability does not mean universality. A later service version may legitimately alter the policy. The rule therefore needs version, scope and change history. A good test can report both the expected result for the old policy and the proposed new result, without erasing the previous acceptance record.

Consider a fictional software update that changes how cancelled bookings are represented. If a baseline suddenly flags conflicts, the team should first check whether cancelled entries are being incorrectly counted as active or the effective status meaning changed. That is a question about contract and test alignment, not yet a finding of compromise.

The service owner should define the intended user outcome and approve changes to its meaning. The technical team can express and rehearse the rule in code. The incident-response team can later use the approved rule as a reference while investigating a reported service failure. None of these roles gains authority to inspect real patron data merely because a demonstration program exists.

### 1.L A reporting template for the first-month learner

After a baseline rehearsal, a learner should produce a **contract report**, not an incident report. The document should identify its rule version, input IDs, assumed room occupancy, status semantics, interval convention, positive and negative expected results, executed or reasoned output, and the exact claims the check cannot establish.

A clear report might state:

> "BSL1-v1 applies to six fictional one-day booking rows. The checker tests interval validity and same-room overlaps among confirmed bookings under half-open time boundaries. It finds S03/S04 in conflict and S06 invalid. An independent status-change variant adds an S01/S05 conflict; omitting S04 from a copied input removes one detected conflict without proving service repair. No real booking state, user, account, log source or production service was tested."

This is a useful artifact because another learner can reproduce every relevant classification from the declared input. It also keeps the failure of a *toy requirement* from becoming an unsupported real-world incident claim.

For a beginner, the accepted result is not complicated mathematics or a comprehensive application security assessment. It is an explanation that connects **business expectation → declared assumptions → reproducible comparison → constrained conclusion**. The next curricular stage can then teach how an incident-response analyst obtains trustworthy observations and separates them from hypotheses.

This report complements, rather than replaces, the existing D1 evidence-readiness contract, R1–R8 claim-review laboratory and case handoff. The tools answer different questions, and a mature readiness packet keeps those boundaries explicit.

### 1.M Section synthesis: preparedness begins with an explicit promise

The service map says what systems may matter. The behavior baseline says what legitimate service is supposed to achieve. The evidence-readiness plan says which authorized sources might later support or challenge a claim. The case decision record states what the team actually knows and which next action requires approval. These are complementary artifacts with distinct purposes.

For Harbor Library, an invariant about confirmed room occupancy offers a practical example of normal behavior. It neither establishes that B17/B18 were incorrectly modified nor supplies a human actor, authorized task list, restore result or data-transfer conclusion. The canonical 09:05 judgment still relies on R1–R8 only.

A sound first-month student should finish by being able to explain why an allowed adjacent booking passes, why an overlapping confirmed pair fails, why cancellation changes occupancy, why incomplete inputs can hide a conflict, and why none of those fixture results alone proves a security incident. That is additional substantive readiness knowledge, not another retelling of the incident case.

---

## BSL1 Offline Laboratory — Booking Invariants and Controlled Sensitivity Tests

**Goal:** Reproduce a deterministic business-invariant check for a small fictional booking set, then demonstrate how a status change or missing input changes what the checker can report.

**Environment:** Python 3 standard library, memory only. No file creation, network requests, authentication, personal records or production changes.

**Fixture classification:** The IDs S01–S06 are invented BSL1 training objects and have no relationship to canonical Harbor Library bookings B17–B20 or R1–R8.

**Rules:** Confirmed bookings occupy the room interval, cancelled bookings do not. Booking intervals are half-open [start, end), the end must be strictly later than the start, and simultaneous confirmed overlaps in the same room are disallowed under this toy single-occupancy policy.

| ID | Room | Start | End | Status |
|---|---|---|---|---|
| S01 | Room A | 09:00 | 10:00 | CONFIRMED |
| S02 | Room A | 10:00 | 11:00 | CONFIRMED |
| S03 | Room B | 09:00 | 10:00 | CONFIRMED |
| S04 | Room B | 09:30 | 10:30 | CONFIRMED |
| S05 | Room A | 09:00 | 10:00 | CANCELLED |
| S06 | Room C | 11:00 | 11:00 | CONFIRMED |

Before running, predict the base findings. Explain why S01 and S02 do not overlap, and why S05 does not occupy its room slot. Then predict the outcome when S05 alone changes to confirmed and when S04 is intentionally omitted from an incomplete working copy.

### Reproducible Python 3 program

~~~python
from itertools import combinations

BOOKINGS = [
    ("S01", "Room A", "09:00", "10:00", "CONFIRMED"),
    ("S02", "Room A", "10:00", "11:00", "CONFIRMED"),
    ("S03", "Room B", "09:00", "10:00", "CONFIRMED"),
    ("S04", "Room B", "09:30", "10:30", "CONFIRMED"),
    ("S05", "Room A", "09:00", "10:00", "CANCELLED"),
    ("S06", "Room C", "11:00", "11:00", "CONFIRMED"),
]

def minute(text):
    hours, minutes = map(int, text.split(":"))
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError("invalid clock field")
    return hours * 60 + minutes

def overlaps(a, b):
    return (
        minute(a[2]) < minute(b[3])
        and minute(b[2]) < minute(a[3])
    )

def inspect(rows):
    if len({r[0] for r in rows}) != len(rows):
        raise ValueError("duplicate booking ID")

    issues = []
    for row_id, room, start, end, status in rows:
        if status not in {"CONFIRMED", "CANCELLED"}:
            issues.append(f"UNKNOWN_STATUS {row_id}")
        if minute(start) >= minute(end):
            issues.append(f"INVALID_INTERVAL {row_id}")

    active = [
        row for row in rows
        if (
            row[4] == "CONFIRMED"
            and minute(row[2]) < minute(row[3])
        )
    ]

    for first, second in combinations(active, 2):
        if first[1] == second[1] and overlaps(first, second):
            issues.append(f"CONFLICT {first[0]}/{second[0]}")

    return sorted(issues)

baseline = inspect(BOOKINGS)
for issue in baseline:
    print("BASE", issue)
print("BASE_COUNT", len(baseline))

print(
    "BOUNDARY_S01_S02",
    "OVERLAP" if overlaps(BOOKINGS[0], BOOKINGS[1])
    else "NO_OVERLAP",
)

print(
    "CANCELLED_S05",
    "NOT_OCCUPYING"
    if BOOKINGS[4][4] == "CANCELLED"
    else "OCCUPYING",
)

# Controlled status-change variant: S05 only.
variant = [
    (*row[:4], "CONFIRMED") if row[0] == "S05" else row
    for row in BOOKINGS
]
changed = inspect(variant)
for issue in changed:
    print("VARIANT", issue)
print("VARIANT_COUNT", len(changed))

# Incomplete-input negative control: omit S04 only.
incomplete = [row for row in BOOKINGS if row[0] != "S04"]
missing = inspect(incomplete)
for issue in missing:
    print("INCOMPLETE", issue)
print("INCOMPLETE_COUNT", len(missing))

assert baseline == ["CONFLICT S03/S04", "INVALID_INTERVAL S06"]
assert len(changed) == 3
assert len(missing) == 1
~~~

### Exact expected output — verified by executing the fixture

~~~text
BASE CONFLICT S03/S04
BASE INVALID_INTERVAL S06
BASE_COUNT 2
BOUNDARY_S01_S02 NO_OVERLAP
CANCELLED_S05 NOT_OCCUPYING
VARIANT CONFLICT S01/S05
VARIANT CONFLICT S03/S04
VARIANT INVALID_INTERVAL S06
VARIANT_COUNT 3
INCOMPLETE INVALID_INTERVAL S06
INCOMPLETE_COUNT 1
~~~

### Worked result, interpretation and limitations

**Baseline:** The confirmed Room B intervals S03/S04 overlap, and S06's interval has zero duration. Under the toy rules, those are two findings. S01/S02 meet at 10:00 without overlapping; S05 is cancelled and therefore not counted as active occupancy.

**Status sensitivity:** Changing S05 from cancelled to confirmed causes a new same-room overlap with S01 while preserving all other baseline inputs. The total increases to three findings. This is a changed *input assumption*, not a newly observed canonical incident.

**Incomplete-input negative control:** Removing S04 from the working copy hides the S03/S04 conflict. The checker reports only S06's invalid interval. A smaller issue count does **not** prove that booking behavior improved; the input population became incomplete.

**Technical limits:** This is a sequential comparison of six artificial rows. It does not implement transactions, concurrency, source authentication, authorization rules, historical changes, room-sharing policies, patron notification or actual booking impacts. The program assumes one fictional date and uses a simplified HH:MM parser. The user must not run or adapt it against any real booking service without the relevant organization's explicit authority.

**Required artifact:** Submit the exact output, a classification table for the baseline and both variants, the applicable business-rule assumptions, and two sentences explaining why neither the simulated errors nor the missing S04 result prove anything about canonical R1–R8. Keep a prediction recorded before execution; a copied expected transcript without an actual run should be labeled as such.

---

## Targeted Refinements of Existing Exercises — No New IDs

The original chapter already contains EX001–EX013. This supplement deepens only **EX002, EX007, EX010 and EX011**, preserving their existing structural constraints. The selected four were not the main exercises expanded in the prior Chapter 01 editorial pass.

### EX002 — First two questions

**Add:** For the training-scope question, state what approved normal booking behavior would need to be confirmed for B17/B18, as distinct from the R6 calendar entry. For the second question, name which observed account or booking source could support a discriminator and which business-contract question would remain open even if that check succeeded.

**Full credit:** The original two-row artifact still names two questions, source pointers, relevant custodians and how alternative answers change the decision. BSL1 is a teaching comparison, not evidence that its policy was approved or violated for canonical B17/B18.

### EX007 — Minimal incident record

**Add:** Retain **exactly seven** labeled opening fields at 09:00. In the existing uncertainty field, explain that a recorded booking change and patron report do not establish the correct owner-approved current booking state. Do not add an eighth field, import a BSL1 result or insert the 09:05 decision into the opening record.

**Full credit:** Seven-field structure, source pointers, synthetic scope and proposed question remain intact; the normal-service correctness criterion is appropriately marked unverified.

### EX010 — Two-sentence internal update

**Add:** Preserve **exactly two sentences** at the 09:00 intake checkpoint. One sentence must distinguish the R3/R4 booking-change records and R5 patron report from a verified incorrect business state. The other must name the proposed service-owner check of expected behavior before the 09:05 decision.

**Full credit:** Two bounded sentences, clear audience, named proposed check, and no claimed real action or BSL1 event in the canonical case.

### EX011 — Escalation trigger

**Add:** In one hypothetical trigger, state what a future owner-approved booking-state comparison would have to demonstrate to establish a violation of an applicable service invariant. State who would confirm that the rule and test scope are valid. Keep the second trigger as a separate potential continued-activity signal. Neither trigger is present in R1–R8.

**Full credit:** Both triggers are explicitly hypothetical, evidence-linked, scoped and authorized. An unverified business rule or missing comparison value is not misreported as a confirmed service failure or cyber compromise.

---

## Supplementary Worked Answers — For the Final Appendix of the Principal Book

### EX002 — Additional worked reasoning

The first question asks whether R3's B17 move and R4's B18 cancellation were specifically included in a complete, dated and approved training task list. R6 supplies a scheduled training interval only, not the authorized operations. A confirmed approved list including B17/B18 strengthens the training hypothesis for those actions; a confirmed complete list excluding one weakens it. The second question requests a bounded account or application check under incident-lead coordination to help discriminate expected activity from potential misuse. R1 identifies an account label, not the human operator. Even a successful authorized source comparison would not establish that current booking values meet a fully specified business policy without an appropriate target-state test. BSL1's unrelated S-series outcomes are not evidence for B17 or B18.

### EX007 — Additional worked reasoning

The seven opening fields stay as in the original answer: case HL-IR-001 with 09:00 time, room-booking service, T-104/R5 reporting context, relevant R1/R3/R4/R5 source events, provisional uncertainty, R1–R8 classroom scope and a proposed training-owner question for 09:05. The assessment field may add that the owner-approved **correct current booking state is unknown**. A report or audit event does not independently establish an invariant violation. No BSL1 test result or later approval appears in this case opening, and the seven-field constraint is preserved.

### EX010 — Additional two-sentence model message

"At 09:00 UTC, application records R3–R4 report changes to B17/B18 following the R1 desk-a sign-in, while help-desk record R5 reports a B18 concern; the cause, approved behavior and current booking correctness remain unverified. The incident lead proposes asking the service/training owner whether those edits match approved tasks and what correct booking outcome should be checked, before the 09:05 decision checkpoint."

This message is written for an internal service-owner audience. It reports no confirmed attacker, executed control, completed collection or real baseline-test result.

### EX011 — Additional worked reasoning

**Hypothetical trigger one:** A future authorized comparison, reviewed by the service owner against the **applicable approved policy version**, shows two confirmed single-occupancy bookings overlapping in the same room, or a selected booking diverging from the owner-approved target. The application/data custodian must establish the comparison's source and scope. This could increase business-harm urgency; it does not prove the cause was malicious. No such comparison is supplied in canonical R1–R8, and BSL1's S03/S04 conflict is a separate laboratory result.

**Hypothetical trigger two:** A newly released and verified application record shows another unexplained booking edit outside a complete approved task list. The appropriate custodian confirms its source and event range, while the incident lead and service/identity owners review proportionate options. This is an escalation condition, not an event already present at 09:05. If logging coverage or training approval is missing, the result remains uncertain rather than automatically being classified as a verified unauthorized action.

---

## Section Synthesis and Navigation

A service map identifies components. D1 describes prospective evidence retrieval. The **behavior baseline** defines what correct legitimate booking operation means under a declared policy. A separate incident assessment uses authorized observations and approval to decide what should happen next. None of these four artifacts can substitute for another.

The BSL1 activity teaches interval boundaries, active-status meaning, negative tests and incomplete-input limitations without creating new Harbor Library incident facts. It provides additional normal-service preparation at rapid-course depth while preserving the case's R1–R8 evidence boundary.

### Continue studying — chapter 01 of 04 (public supplementary draft)

[← Course home](../../../README.md) · [Course chapter index](../../SUBJECTS.md) · [Chapter 02 →](../MANUSCRIPT.md#ch-02) · [Principal book and final worked answers](../MANUSCRIPT.md#answers)

**Editorial integration reminder:** This Markdown file is a transitional component of the one English principal book, not a new book or an additional curricular chapter. It does not increase the 50 numbered exercises. Manuscript integration, link validation, technical and language review, rights checking and A4 measurement remain separate required steps.

### Primary sources and rights

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework). Organizational risk-management framework. It does not prescribe the BSL1 booking invariants.
- [NIST SP 800-61 Revision 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Final April 2025; incident-response preparation and wider risk-management context.
- [NIST SP 800-34 Revision 1, updated edition — Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final). November 2010 update; evaluating operations to inform contingency planning and priorities.

All Harbor Library and BSL1 objects, rule versions, test outcomes, examples and exercise-answer additions are fictional original teaching constructs. These primary sources provide general context and do not authenticate the scenario. Editorial responsibility belongs only to [hiagokinlevi](https://github.com/hiagokinlevi). Maintainer-owned original material follows the [CyberABC rights notice](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE), subject to third-party rights. No real service, account or personal record is accessed.
