# Incident Response and Cyber Resilience — Rapid Course
## Chapter 02 Supplementary Expansion Draft: Measuring Service Impact Without Inventing a Population

**Editorial state:** **Public working draft — not an independent chapter or a complete book.** This text is a transitional expansion intended for Chapter 02 of the course's **single principal English manuscript**. The chapter remains an unfinished draft pending integration, technical review and the full book publication gate.  
**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration target:** [Chapter 02 — Alert triage and evidence preservation](../MANUSCRIPT.md#ch-02).  
**Curricular scope:** Incident Response and Cyber Resilience / Rapid course / English, course 016.  
**Learning contribution:** Define defensible units of incident impact, deduplicate reports without hiding their provenance, separate reported concerns from verified business-state mismatches, and communicate what was and was not measured.  
**Source boundary:** R1–R16 are available only by the fictional **09:20 Round B review**. R17–R24, the Chapter 3 recovery targets and all Chapter 4 branches are unavailable to this supplement's canonical 09:20 assessment.

> Harbor Library, every R-series item and the new exercise-only IM2 data below are fictional. No statements about a real library, patron, compromise, outage or export follow from these teaching fixtures. The IM2 laboratory is a separate invented comparison and must never be appended to the canonical R-series timeline.

### Why this material belongs in Chapter 02

The existing Chapter 02 teaches the difference between harm, urgency and confidence and asks the service owner for a bounded impact check. That is the right starting point. A further problem remains: even after the analyst obtains some records, what *exactly* can be counted? Four help-desk tickets may concern one booking. A booking-audit row may record a legitimate change that harmed nobody. A current-state mismatch can establish a problem for one selected booking without revealing whether ten other bookings were affected. Reporting a number without specifying its unit and evidence frame produces misleading precision.

This supplement does not reproduce the existing E1 integrity, T1/T2 query-time, Q1 correlation or VQ2 coverage laboratories. It adds a **service-impact measurement contract** and an offline example that keeps those earlier evidence limits intact.

# New Teaching

### 2.I Define the thing you are trying to count

"How many were affected?" is not an answerable technical question until an analyst defines what an *affected unit* is.

A **ticket** is a report submitted to a service channel. A **booking** is an application business object. An **edit event** is a recorded operation. A **patron** is a person or account associated with service use. One person may open multiple tickets, one ticket may discuss several bookings, and one booking may have several audit records. These objects must not be treated as interchangeable.

In Harbor Library, R5 contains a patron report about B18; R11 is a second patron report about B19. R3, R4 and R9 describe booking changes. The supplied chapter does not include a complete current authoritative-state comparison or the population of all bookings. Therefore, at the 09:20 checkpoint, the learner can identify **specific reported concerns and recorded changes**, not an independently measured total of incorrect bookings or affected people.

Before any count, write the **measurement question**:

> "Among the booking IDs included in an authorized, owner-defined comparison interval, how many have a current authoritative value that differs from the approved expected state?"

This is substantially narrower than:

> "How many patrons were harmed by the incident?"

The second question requires additional relationships and harm criteria. A room assignment discrepancy could inconvenience a patron, but whether it caused actual harm, whether multiple patrons were associated with the same room, and whether the issue was corrected before use are all separate facts.

The general incident-response goal is to assess scope and consequences based on available evidence. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places response analysis and decisions within cybersecurity risk management; the measurement contract below is original instructional material, not a prescribed NIST impact score.

### 2.J Establish four levels of impact claim

It helps beginners to classify claims before attempting to calculate a total.

| Classification | Example claim | What it establishes | What it cannot establish alone |
|---|---|---|---|
| **Reported concern** | A help-desk record says that a booking looked wrong | A report was received | That the authoritative state was incorrect or every symptom occurred as described |
| **Recorded change** | Application audit says a room assignment changed | The producer recorded a change | Whether the change was approved, harmful, durable or visible to a patron |
| **Verified state discrepancy** | An authorized comparison finds a current value differs from an owner-approved target | A mismatch exists for the *tested object and state versions*, under the comparison's trust assumptions | The size of the unexamined population, root cause or human actor |
| **Verified service consequence** | A service owner validates a specific failed reservation outcome | The documented scenario caused an unacceptable outcome within tested scope | Whether all patrons experienced the same effect |

These classifications can apply to the same booking; they are not mutually exclusive replacement labels. A report and an audit event can support investigating one booking, while a later state comparison adds a distinct, stronger claim. The analyst should preserve the original evidence and note which new source justified the upgrade.

A state discrepancy must also have a defensible reference target. "The current room is different from the old room" does not necessarily mean it is wrong: a legitimate staff edit could have been approved. The target needs an owner, version, applicable time and authority. If the target is missing, record the comparison as **unverified**, not automatically a mismatch.

### 2.K The numerator and denominator have different evidence requirements

A count needs a **numerator**, the items meeting the definition, and a **denominator**, the items in the defined population against which the count could be interpreted.

Suppose a restricted comparison examines five selected booking IDs and finds two confirmed mismatches. A precise statement is:

> "Two of the five selected IDs have a verified mismatch under the supplied comparison rules; the other three require their own status classification."

It would still be incorrect to claim:

> "Forty percent of Harbor Library bookings were corrupted."

The selected five could have been chosen because they were suspicious, reported or otherwise convenient. Without evidence that the five represent the entire relevant population or a valid sampling design, their observed proportion cannot be generalized to every booking.

Selection may be **case-driven** rather than representative. An incident analyst often investigates the most urgent known objects first. That is appropriate for containment and service repair, but it creates a biased basis for estimating prevalence. Case selection and statistical sampling are different activities.

The analyst should separate:

- **Known examined frame:** the exact identifiers selected and why.
- **Comparable items:** selected identifiers for which both approved reference and current values are available.
- **Confirmed mismatches:** comparable items that fail the declared equality or business acceptance check.
- **Unverified items:** records missing one of those comparison prerequisites.
- **Unexamined population:** objects outside the selected frame or with unknown existence or completeness.

Do not silently exclude unknown items from the report just to make the ratio look more favorable. Instead state, for example, "two mismatches, two matches and one unverified item within the five listed comparisons; no population-wide estimate available."

This approach is useful even when no percentage is calculated. Counts expressed with explicit scopes let the next analyst decide whether to broaden the inquiry or correct known business state immediately.

### 2.L Deduplicating does not mean discarding evidence

A help-desk queue may contain repeated calls, email replies or follow-up tickets about one booking. Deduplication can prevent overcounting *booking identifiers*, but it must not destroy the fact that multiple reports were received.

Consider two fictional tickets referencing the same booking. For the question "How many distinct bookings have a reported concern?" the two tickets correspond to **one booking identifier**. For the question "How much help-desk demand was received?" they remain **two separate contacts**. For the question "How many people were affected?" neither answer is sufficient unless the distinct individuals and relevant outcome are reliably established.

Always preserve the original ticket IDs. A normalized table may group them by booking identifier, but the grouping rule must be explicit and reversible. If a booking ID is absent or misspelled, do not make an automatic identity assumption from a similar time or room number.

A dangerous shortcut is to treat multiple independent reports as multiple verified incidents or to count one booking once for each edit event. Another shortcut is to collapse all reports into one and then claim that only one person was affected. Each changes the unit without informing the reader.

The source/copy/interpretation separation explained in Chapter 02 also applies here. A normalized, deduplicated view is a **derived analytical product**. Keep the source pointers and transformations visible. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) discusses log-management processes and the handling of event records at an organizational level. It does not specify the fictional deduplication procedure in this section.

### 2.M Missing information is an impact result, not a reason to guess

An absent owner-approved target, missing current-state row, incomplete query filter or unreliable source timestamp makes some impact claims **unverified**. This classification does not say the booking is healthy or broken.

A response team must distinguish:

1. **Negative observation:** a defined, functioning, appropriately scoped test produced evidence supporting an absence or expected result within its bounds.
2. **Missing observation:** the record or comparison needed for the test was not supplied or could not be trusted.
3. **Contradictory observation:** a properly conducted comparison produced a result that fails the accepted target.

A query that returns no relevant audit rows while collection health is unknown belongs in the second category for any broad absence claim. A state comparison that explicitly shows a different accepted value may support the third category—but only if the target and current value have adequate provenance.

R14's quiet summary is a reminder: a bounded log query cannot certify that no changes occurred outside its query envelope. R15's 24-hour retention policy adds urgency to preserving the source needed for an impact comparison, but its exact deletion anchor remains unknown. These limits affect what can be measured as well as what can be investigated.

### 2.N A defensible impact ledger

A useful impact ledger contains one row per selected business object, with separate columns for the sources that describe it. It should not put a free-form narrative in place of a test result.

| Field | Explanation |
|---|---|
| Booking ID | Exact identifier within approved scope |
| Selection reason | Audit edit, help-desk report or owner-defined test frame |
| Related evidence | Pointers to source records and query or collection receipts |
| Approved reference | Expected value, version, approval owner and applicable time |
| Current authoritative value | Observed value, source, time and collection method |
| Comparison state | Match, mismatch or unverified |
| Reported service effect | Reported concern, verified consequence or not assessed |
| Uncertainty | Missing records, source-health limits or conflicting interpretations |
| Next action and owner | Bounded comparison, correction proposal or preservation request |

An analyst should not add patron names or unrelated account details to a shared impact summary when booking identifiers and controlled references are sufficient. The service owner can evaluate business consequences and authorize further checks within the relevant privacy rules. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) provides source-aware guidance for incorporating forensic techniques into incident response; it does not provide a blanket authorization to collect personal data.

The impact ledger's **selection reason** is especially important. If every row was selected because someone complained, a ratio from those rows cannot estimate how common a problem is among people who did not complain. If the source is a partial application audit, the ledger cannot measure omitted write paths or disappeared records. State the missing part of the frame before recommending a new collection.

### 2.O Contrastive worked example at the Round B decision

**Plausible but incorrect assessment:**

> "R3, R4 and R9 show three booking edits, and R5 and R11 contain two patron reports. Five patrons were affected, so the incident has a confirmed five-user impact."

This is an invalid unit conversion. The three application changes are not five distinct people. The two help-desk reports are observations of reports, not independent verification of two incorrect authoritative states. R3/R4 may include approved training work. Nothing in the Round B case establishes a complete distinct-patron population or the final approved booking targets.

**Correct bounded assessment:**

> "By the fictional 09:20 Round B review, Harbor Library has source records reporting changes to B17, B18 and B19, plus patron complaints involving B18 and B19. The approved scope and current authoritative state for those bookings have not been fully verified. The incident lead should request a bounded, service-owner-approved comparison of the relevant booking identifiers with the correct target state, preserving its source coverage and retention limitations. No total of affected patrons can yet be established from the supplied material."

This assessment makes a useful decision while refusing a fabricated count. It does not need to delay all protective action until every record is available; urgency, ongoing potential harm and evidence loss remain separate considerations.

### 2.P Communicate a lower bound without claiming completeness

If an authorized comparison later verifies that two selected booking states are inconsistent with approved targets, the analyst can sometimes state **at least two identified mismatches among the checked items**. That is a lower bound for the known, explicitly identified objects under the test assumptions. It is not the total affected booking count unless the investigated frame is complete.

For a public message, even a correct internal count may be too specific if it exposes other patrons or could be misread as exhaustive. An internal service owner may need booking IDs, approved targets and corrective owners; a patron-facing note may only need to acknowledge a possible room-booking discrepancy and describe the owner-confirmed assistance channel. The communications role must not convert "we have identified two incorrect selected bookings" into "only two bookings were affected."

A review should ask which wording remains true if additional relevant source records arrive later. "Two mismatches were identified in the approved five-object comparison" remains true, assuming that comparison was valid. "Only two bookings were affected" can become false as soon as an additional affected object is found. The first is therefore a more resilient and auditable statement.

### 2.Q Failure modes and acceptance limits

| Failure mode | Misleading conclusion | Safer interpretation |
|---|---|---|
| Repeated tickets for one booking | Each ticket represents a new affected booking | Keep ticket count and distinct booking count separate |
| A booking changed in an audit | The change harmed a patron | Validate authorization, approved expected state and service outcome |
| Five suspicious objects examined | Results describe the full population | State the selected frame and avoid prevalence extrapolation |
| Reference target unavailable | No mismatch was found | Comparison is unverified, not passed |
| Current record absent | Booking was deleted | Query, retention, source or export may be incomplete |
| Matching source and current values | All service outcomes are correct | Check applicable version, time, authorization and user-facing result |
| Two confirmed mismatches in a subset | Exactly two bookings were affected overall | At least two were identified within the declared subset, if trusted |
| No new complaint in the help desk | No further harm occurred | Reporting channels and coverage are incomplete observations |

A beginner has met this section's objective when they can select the correct unit, preserve source and derived identifiers, distinguish confirmed mismatch from missing comparison evidence, and write a decision-ready conclusion without claiming a measured population they never examined.

---

## Original Offline Laboratory — IM2: Reports, Distinct Bookings and Confirmed Mismatches

**Classification:** Independently invented, offline-only teaching fixture. IM2 is **not** an additional Harbor Library R-series release, not an approved production comparison, and not P1/C1 from Chapter 03. Identifiers X01–X05 and X99 are fictitious classroom business objects; T01–T04 are fictitious report references.

**Goal:** Separate ticket count, distinct reported booking IDs, verified mismatches in an examined frame and unverified comparisons. Demonstrate how removing an approved reference changes the strength of a claim without changing the underlying hypothetical current value.

**Environment:** Python 3 standard library, in memory. No file operations, network calls, credentials, database writes or real identities.

**Input assumptions:** The dictionary `TARGET` supplies an artificial owner-designated comparison target; `CURRENT` supplies an artificial current-state view. These values are inputs invented for the exercise, not real owner approvals or authenticated exports. A value `None` means the target is missing. The report tuples are separate source observations; repeated booking references are preserved.

Before running, predict: (a) the number of reports, (b) the number of distinct booking references in those reports, (c) which examined IDs mismatch, and (d) what happens when the reference target for X04 is removed in a *variant*.

~~~python
TARGET = {
    "X01": "Room A",
    "X02": "Room B",
    "X03": "Room C",
    "X04": "Room D",
    "X05": None,
}

CURRENT = {
    "X01": "Room A",
    "X02": "Room C",
    "X03": "Room C",
    "X04": "Room B",
    "X05": "Room A",
}

REPORTS = [
    ("T01", "X02"),
    ("T02", "X02"),
    ("T03", "X05"),
    ("T04", "X99"),
]

def classify(target, current, reports):
    ids = sorted(
        set(target) | set(current) |
        {booking_id for _, booking_id in reports}
    )

    counts = {
        "MATCH": 0,
        "MISMATCH": 0,
        "UNVERIFIED": 0,
    }

    results = {}

    for booking_id in ids:
        expected = target.get(booking_id)
        observed = current.get(booking_id)

        if expected is None or observed is None:
            status = "UNVERIFIED"
        elif expected == observed:
            status = "MATCH"
        else:
            status = "MISMATCH"

        results[booking_id] = status
        counts[status] += 1

    distinct_report_ids = {
        booking_id for _, booking_id in reports
    }

    print(
        "reports:", len(reports),
        "unique_booking_refs:", len(distinct_report_ids)
    )

    for booking_id in ids:
        print(f"{booking_id}: {results[booking_id]}")

    print(
        "counts:",
        ",".join(f"{key}={value}" for key, value in counts.items())
    )

    return results

original = classify(TARGET, CURRENT, REPORTS)

# Negative control: remove the approved comparison
# value from a copy, without modifying the baseline.
variant = dict(TARGET)
variant.pop("X04")

negative_status = (
    "UNVERIFIED"
    if variant.get("X04") is None
    else "MISMATCH"
)

print("negative_X04_target_removed:", negative_status)

assert original["X04"] == "MISMATCH"
assert variant.get("X04") is None
~~~

### Exact expected output — executed with the fixture

~~~text
reports: 4 unique_booking_refs: 3
X01: MATCH
X02: MISMATCH
X03: MATCH
X04: MISMATCH
X05: UNVERIFIED
X99: UNVERIFIED
counts: MATCH=2,MISMATCH=2,UNVERIFIED=2
negative_X04_target_removed: UNVERIFIED
~~~

### Worked interpretation

Four report rows refer to only three distinct booking IDs: X02 appears twice, while X05 and X99 each appear once. This is **not** a count of distinct people. Report count and distinct business-object count answer different questions.

The examined comparison contains two matches, X01 and X03. X02 and X04 are mismatches under the declared synthetic target/current inputs. X05 is unverified because its target is missing, even though a current value exists. X99 is unverified because neither the target nor the current comparison row is supplied; a report references it, but the ledger has no authoritative state for it.

The laboratory demonstrates a nonreported mismatch: X04 is a mismatch in the supplied comparison even though no help-desk ticket in `REPORTS` references X04. Conversely, a reported concern about X05 does not by itself prove that the current value is incorrect. This is why a report-only sample cannot reliably characterize every state discrepancy.

The negative variant removes only X04's reference value. Its classification becomes `UNVERIFIED` rather than `MISMATCH`. No simulated current booking state changed. The shift is caused by weakened **evidence**, not by an automatically repaired business condition. Restore the original target after the variant and retain both results distinctly.

The defensible classroom statement is: "Of six identifiers encountered across these small supplied sources, two match, two mismatch and two cannot be evaluated; four reports cover three distinct booking references. These numbers characterize only the IM2 fixture, not Harbor Library's complete bookings or patrons."

### Reproducibility and limitations

The code checks exact string equality, not room availability rules, approved changes, person-to-booking relationships, clock normalization or database consistency. `None` is a local missing-value convention; a real schema must distinguish missing, null, deleted and legitimately empty state according to producer semantics.

A production analyst would require source identifiers, selection manifest, approval owner, effective target version, authoritative current-state timestamp and privacy/access controls before treating the comparison as evidence. The toy script supplies none of those provenance receipts, and its computed results must never be called a measured incident impact.

**Required learner artifacts:** Copy the nine-line output; produce a six-row impact ledger with evidence status and source limitations; explain in two sentences why "four affected patrons" is unsupported; and report exactly what changed in the negative test. A response fails if it equates report count with affected people, silently discards X99, claims all bookings were examined or treats the variant as a correction.

---

## Integration with Existing EX016 and EX023 — No Additional Exercise IDs

### EX016 — Priority without false certainty: supplementary discriminator

**Added input:** At the canonical 09:20 Round B checkpoint, R9 records a B19 edit, R11 records a patron concern and R15 reports a short retention period whose deletion anchor remains unknown. Explain why urgency to preserve relevant evidence can be high while *confidence in a particular cause and measured patron impact* remains low.

**2-point criterion:** Keep potential service harm, loss urgency, confidence and proposed next decision in separate fields. Do not use IM2's mismatch counts as new canonical Harbor Library observations or infer a population total.

### EX023 — Impact check: supplementary measurement contract

**Added task:** Extend the original proposed comparison request with four explicit definitions: (1) unit of measurement, (2) selected business-object frame, (3) distinction among reported concerns, recorded edits and verified state discrepancies, and (4) a prohibition on inferring a population-wide rate from case-selected rows. As an optional offline practice, use IM2 to show why duplicated tickets and missing target values must remain visible.

**2-point criterion:** An approved, bounded query includes exact identifiers, source, event-time interval, expected reference/current state fields, owner, privacy scope and a report of which outcomes are *not yet measured*. A good answer does not present a proposed query as completed collection or an IM2 toy result as a real affected-user count.

---

## Supplementary Worked Answers for Final-Book Appendix

### EX016 — Additional worked reasoning

At 09:20, the evidence supports investigating a recorded B19 edit (R9) and a reported user concern (R11). It does not supply an approved target comparison, a complete list of affected bookings, or a link from each reported concern to a unique person. R15 adds a legitimate urgency to investigate source availability because detailed audit material has a 24-hour deletion rule with unknown policy anchor. The incident lead can prioritize a narrow preservation decision and owner-approved impact comparison without declaring credential compromise or broad patron impact. A verified continuing unexplained edit or newly confirmed business-state mismatch could increase the urgency of containment; a validated approved change could weaken the related unauthorized-use explanation. All decisions remain bounded by actual released evidence.

### EX023 — Additional worked reasoning

Define the primary impact unit as **distinct booking IDs compared against an owner-approved expected value**, not the number of application events or help-desk contacts. In the canonical Round B case, B17–B19 are relevant selected objects; a real authoritative state comparison has not been performed in the supplied R1–R16 data. The service owner proposes the reference state and authorizes a bounded view; the application custodian provides exact source, selection manifest, timestamp semantics and collection receipt if later performed. A suitable analytical result distinguishes booking ID, edit pointer, help-desk report pointer, expected value, observed current value, match/mismatch/unverified state and unresolved source or authorization limit. Do not report a count of affected patrons or a percentage of all bookings without a trustworthy population frame.

For the **separate IM2 practice only**, the exact comparison yields two matches, two mismatches and two unverified IDs across the six encountered identifiers, while four reports reference three distinct bookings. X04 demonstrates that a mismatch may be absent from the report set. X05 demonstrates that a complaint alone cannot prove the authoritative value is wrong. The X04 target-removal negative test changes its classification to unverified without changing the current value. These are teaching results, not new Harbor Library incident findings.

---

## Synthesis and Continue Studying

A defensible incident-impact assessment states **what was counted, how the units were selected, which evidence supports each status, what remains unverified and whether the result can or cannot represent the wider population**. The analyst must not turn a report, an audit event, a partial comparison or a quiet query into a universal claim of harm or safety.

This supplementary draft remains a component of Chapter 02 of the existing single English book. The next authored chapter explores approved containment and recovery options; it does not inherit IM2's invented records as canonical evidence.

### Continue studying — chapter 02 of 04 (supplementary draft)

[← Chapter 01](../MANUSCRIPT.md#ch-01) · [Course chapter index](../../SUBJECTS.md) · [Chapter 03 →](../MANUSCRIPT.md#ch-03) · [Final worked-results appendix](../MANUSCRIPT.md#answers)

### Primary references and rights

- [NIST SP 800-61 Revision 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). Final April 2025; incident-response analysis and risk-management context.
- [NIST SP 800-92 — Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final). Final September 2006; source and log-management background, not a prescription for this algorithm.
- [NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final). Final August 2006; source-aware evidence considerations, not authority to collect personal data or a legal forensic certification.

These primary works support general concepts only. The invented Harbor Library and IM2 observations, Python fixture, classifications and exercise answers are original educational material, not facts or text taken from the cited works. Original maintainer-owned CyberABC content is dedicated under [CC0 1.0](../../../../../../LICENSE) within the limits of the [rights notice](../../../../../../RIGHTS.md); third-party works retain their own rights. This public draft is **not** an A4 page validation or a complete book release.
