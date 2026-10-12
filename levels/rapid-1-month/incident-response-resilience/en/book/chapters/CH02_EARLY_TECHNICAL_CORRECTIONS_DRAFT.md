# Chapter 02 — Early Technical and Instructional Corrections (English)

**Editorial status:** **Public transitional correction component**, intended for the existing [Chapter 02](../MANUSCRIPT.md#ch-02) and the final worked-answer appendix of the **single principal English book**. This is not another chapter, a revised completed manuscript, or a claim of real incident-response capability.  
**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi).  
**Integration boundary:** Only §§2.1–2.8 (strictly before §2.8a), plus the existing EX014–EX019 worked-answer area where specified. Do not renumber exercises, change their prescribed formats, duplicate TRI2/E1/T1/T2, or incorporate any R17–R24 or later branch information.

> **Canonical time and fiction:** At 09:05 the learner has R1–R8. R9–R16 are released only at 09:20, even when their printed event timestamps are earlier. R14 is an incompletely described quiet-query summary. R15 gives a *24-hour policy duration* with no confirmed deletion anchor or deadline. TRI2 cases, optional T1/T2 fixtures, local E1 files and the adversarial checks below are synthetic and cannot become additional R-series records, production collections or completed source holds.

## Correction 01 — Ground each TRI2 evidence flag in its released record

**Exact placement:** §2.2b, in the existing `review(s)` Python function. Insert the code below **immediately after** its current first release check, which returns `BLOCK_UNRELEASED_SOURCE`, and **before** the existing `verified_fresh_edit` and `variant` checks. Keep the remainder of the existing function, the twenty baseline TRI2 cases and their published output unchanged.

### Insert into the existing Python function

~~~python
    # A model flag about a canonical card requires that card
    # to be present in the learner's declared released source set.
    # Independent future scenarios remain explicitly labelled variants.
    released_refs = set(s["refs"])
    if s["retention_notice"] and "R15" not in released_refs:
        return "BLOCK_UNRELEASED_CLAIM:R15"
    if s["quiet_summary"] and "R14" not in released_refs:
        return "BLOCK_UNRELEASED_CLAIM:R14"
    if (s["patron_report"]
            and not ({"R5", "R11"} & released_refs)):
        return "BLOCK_UNRELEASED_CLAIM:PATRON_REPORT"
    if (
        s["approved_addendum"]
        or s["training_scope_verified_complete"]
        or s["addendum_names_b19"]
    ) and not {"R9", "R10"}.issubset(released_refs):
        return "BLOCK_UNRELEASED_CLAIM:R9_R10"
~~~

**Why this changes the lesson:** The original TRI2 correctly rejects a literal R9 citation in Round A, but its Boolean fields are not themselves linked to the released IDs. With `ROUND_A` and `retention_notice=True`, the original function will discuss the R15 retention anchor at 09:05 even though R15 was not yet supplied. Similarly, `quiet_summary=True` can inject R14's quiet-query limitation into Round A, and a source-less training-addendum variant can reduce B19 concern even when R9/R10 do not belong to the input set. A model that checks only `refs` but not **which flags depend on those refs** has an incomplete evidence-release guard.

The insertion checks only provenance *within the classroom release set*. It does **not** authenticate real logs or prove that a named custodian completed a comparison. For genuine source provenance, external, authorized evidence handling is necessary; a model flag is still just a simulated premise.

### Add a separate adversarial demonstration after the existing TRI2 program

~~~python
# Run only AFTER the complete TRI2 program above.
adversarial = [
    (
        "R15_TOO_EARLY",
        {**ROUND_A, "retention_notice": True}
    ),
    (
        "R14_TOO_EARLY",
        {**ROUND_A, "quiet_summary": True}
    ),
    (
        "B19_WITHOUT_R9_R10",
        {
            **ROUND_A, "variant": True,
            "approved_addendum": True,
            "training_scope_verified_complete": True,
            "addendum_names_b19": True,
            "no_new_edits_verified": True,
            "query_coverage_known": True,
        }
    ),
]
for label, scenario in adversarial:
    print(label, review(scenario))
~~~

**Exact supplementary output, executed with Python 3 after adding the guard:**

~~~text
R15_TOO_EARLY BLOCK_UNRELEASED_CLAIM:R15
R14_TOO_EARLY BLOCK_UNRELEASED_CLAIM:R14
B19_WITHOUT_R9_R10 BLOCK_UNRELEASED_CLAIM:R9_R10
~~~

The **twenty existing TRI2 outputs remain literally unchanged** under the insertion. The three new negative tests are additional fixture variants, not new canonical records or numbered exercises. For a failing result, the correct response is to restore the previous checkpoint's evidence boundary rather than silently adding missing later cards.

**Pass criterion:** All twenty original lines still match the principal appendix, and all three supplementary negative tests are blocked exactly as above. **Fail criterion:** R14, R15 or B19-task interpretation appears in a supposed 09:05 canonical decision because of an ungrounded flag.

---

## Correction 02 — Remove an apparent collection before the exercise release

**Exact placement A:** §2.3, the first `Collection-note field | Example for a synthetic classroom export` table. Retain its layout and other rows, but replace these three cells:

| Existing row | Corrected classroom example |
|---|---|
| Source and range | **Proposed** booking-audit event-time selection, 08:30–09:15 UTC; producer, interval filter and available rows still to be confirmed. |
| Collected at | **Not performed in this illustrative card.** R9–R16 become available to the learner only at the 09:20 Round B release; any actual local teaching-copy creation must use and record the learner's *actual* later time. |
| Method | **Planned only:** transcribe permitted, supplied synthetic rows as UTF-8 **after release**, in an approved local scratch directory. This is not a production source export or evidence that all requested records exist. |

**Reason for the correction:** The current example says `collected at 09:18 UTC`, although the synthetic R9–R16 material is first released to the learner at 09:20. That invented collection receipt can misteach the relation between event time, learner receipt time and actual creation of a copy. The corrected example is a **plan**. It does not claim an earlier ingestion event, an actual local export or a hidden source.

**Exact placement B:** §2.4, “Worked example: the second alert,” Step 3. Replace the clause **“ask the incident lead to authorize preservation before R15's retention deadline”** with:

> Ask the incident lead for a prompt, bounded preservation decision **while the source remains available if possible**, and ask the application custodian to establish R15's actual policy anchor, oldest retrievable relevant record and feasible preservation route. **No exact deletion deadline is currently supported.**

**Exact placement C:** The first §2.4 `Case decision at 09:20 UTC` table, its sole `Owner` cell. Replace the current `Incident lead authorizes; analyst records the copy` wording with:

> Incident lead is the **proposed approval owner** for bounded classroom analysis and for a separate authorized source request; analyst records only the synthetic case note **unless a real local exercise copy was actually created and documented**. P-A/P-B remain proposed for any source-system collection.

This avoids confusing a proposal, a classroom permission and a completed source copy without changing the table's row count or the later P-A/P-B request definitions.

---

## Correction 03 — Protect the learner's existing files in the E1 lab

**Exact placement:** §2.5, in the E1 `python` listing that writes `E1.txt` and `E1-modified.txt`.

The original script uses `Path(...).write_bytes(...)` on fixed names. In a directory that already contains a learner's file named `E1.txt`, this **overwrites that file without warning**. This is a concrete local scratch-safety defect even though the lab does not use production evidence.

Keep the literal `payload`, its two rows, the existing printed byte counts and SHA-256 values, and the final `saved.replace(...)` expression. Make **only these two code replacements**:

**Replace:**

~~~python
Path("E1.txt").write_bytes(payload)
~~~

**With:**

~~~python
# Run only in a new, authorized local scratch directory.
# Exclusive creation refuses to overwrite an existing file.
with Path("E1.txt").open("xb") as output:
    output.write(payload)
~~~

**Replace:**

~~~python
Path("E1-modified.txt").write_bytes(altered)
~~~

**With:**

~~~python
with Path("E1-modified.txt").open("xb") as output:
    output.write(altered)
~~~

**Exact normal output, reproduced after both replacements:**

~~~text
235 dc973f580305633eb0a75317c5bdbd9886a8fc015e14a0b17bae09be5e3a6e37
235 15287410550f021dcb81e10fc1833297ffa840ee8ffa8e75867de36df64ffa4d
~~~

**Supplementary negative test:** In a *disposable temporary directory only*, create an innocent file named `E1.txt` and rerun the revised lab. Exclusive creation raises `FileExistsError` instead of overwriting the pre-existing file. This negative test was executed; the original program was separately observed to replace a pre-existing marker in an isolated temporary directory.

The learner should select an **empty authorized scratch directory** and keep the two newly created files and the measured receipt if they need to complete EX019's collection-note exercise. If a name collision occurs, stop and choose a new directory; do not delete or rename the existing file to force the exercise to pass. The resulting E1 remains a **synthetic local transcription**, not an authenticated production export or a source-retention hold.

**Pass criterion:** Normal E1 bytes and digests remain exactly as published and existing files are never overwritten. **Fail criterion:** A pre-existing local file is silently replaced, or the output is interpreted as proof that the underlying R9/R14 source was complete.

---

## Correction 04 — Make the three time values mean what the code measures

**Exact placement:** §2.6, immediately after the optional temporal-coverage Python 3 listing and before the current `Procedure` paragraph. Insert:

> **Time-label clarification:** In this fictional program the `seen` field is the **09:20 learner-release/availability checkpoint**. Thus `delay=17 min`, `delay=16 min` and `delay=6 min` measure the interval from each printed record time to **release to the learner**, not a measured logging-pipeline ingestion delay, first detector discovery, first operator awareness or collection time. None of those additional source timestamps is supplied. The print label `delay` is retained to preserve the existing reproducible transcript; its precise meaning must be written beside any learner result. If an independent future source returned a later event time than its purported earlier learner receipt under verified comparable clocks, the observer should stop and investigate the timing inconsistency rather than treat a negative duration as valid causal order.

**Original output retained, reproduced with Python 3:**

~~~text
R9 event=09:03 UTC seen=09:20 UTC delay=17 min
R10 event=09:04 UTC seen=09:20 UTC delay=16 min
R15 event=09:14 UTC seen=09:20 UTC delay=6 min
~~~

**Instructional limit:** This is a **precision clarification**, not another source event or a promise that UTC clock normalization validates source time accuracy. The original §2.7 T2 replay still has independent event and ingestion times and remains an exercise-only example.

---

## Correction 05 — EX018 worked answer must be a real three-row request

**Exact placement:** Final answer appendix, `### EX018 — Worked result`. Replace **only the first table** currently headed `Needed fact | Why the lead asks` with the following **three-row P-A request**. Keep the existing two-row P-A/P-B comparison and its sound explanatory discussion; do not create another exercise ID.

| P-A request element | Specific source, object and proposed event interval | Policy-anchor / oldest-row question | Authority, custodian, storage and state |
|---|---|---|---|
| 1. Detailed booking audit relevant to R9 | **Proposed** booking-audit source for B17–B19, with a requested **08:30–09:20 UTC** event-time range, to be confirmed by the custodian; R9 reports a B19 edit. | R15 gives a 24-hour duration but **no verified start anchor or exact expiry**. Ask which detailed row is oldest and whether it is still retrievable. | Incident lead to approve source request; booking/application custodian to confirm producer, fields and source availability. Restricted authorized copy location and collector are **planned, not created**. State: **proposed**. |
| 2. Application-audit summary and its supporting query | **Separately named** application-audit source behind R14, with a **proposed 08:30–09:20 UTC** selection for custodian review; query filters, actual producer and index coverage **not supplied**. | Do not assume R15's deletion rule also applies to the application-audit source. Request the actual retention rule and queried interval/ingestion limits, without inferring a deletion instant. | Incident lead to approve only the minimum necessary selection; application/logging custodian to identify producer and permit a restricted storage/collector arrangement. No query re-run or export shown. State: **proposed**. |
| 3. P-A authority, preservation and copy-control decision | Both above sources remain **distinct** until their namespaces, object IDs and selected ranges are checked. No collection/hold follows merely from writing P-A. | Request the source-specific policy anchor, earliest available relevant item, potential loss path, and any **separate** source-hold capability and confirmation process. | Approval owner: incident lead under fictional rules; executing custodian and copy collector to be named after permission. Planned restricted evidence location, access list, source/copy receipts and review trigger must be documented before claiming collection. State: **proposed**, not approved, collected or verified. |

**Required explanatory sentence after the table:**

> A prompt, bounded preservation proposal may be justified before the cause of B19's edit is known because a relevant source might become unavailable, but R15 alone does not prove when deletion occurs, that a hold exists or that a collection has taken place.

This corrected answer meets the exercise's **three P-A rows**, sources, proposed intervals, unknown deadline anchor, collector/authority/storage scope and distinct status requirements. It does not overwrite the existing **two-row P-A/P-B comparison**, the MIN2/HOLD2 supplementary reasoning, or any answer for EX014–EX017/EX019. The two parallel requests remain *proposed* at the 09:20 teaching checkpoint.

**Assessment boundary:** Full credit under the unchanged 0–2 rubric requires the respondent to keep R14's query source distinct from R9's booking-audit record, preserve R15's missing anchor, and avoid converting a source request, copy, or hold into a completed action.

---

## Corrections Summary and Continue Studying

These five focused changes teach one consistent principle: an answer should never grow more confident than the released source or the operation actually performed. TRI2's labels require released supporting cards; a simulated collection cannot predate its lesson release; files used for local labs must not be overwritten; an event-to-release gap is not measured ingestion; and an EX018 model request must contain the structured fields the student is required to produce.

**The original TRI2 twenty-line output, E1 two-line hash output, temporal-coverage three lines and T2 two-line output remain unchanged.** The supplementary TRI2 three-line guard is an independent negative control. T1 is query metadata, not another standalone program. R9–R16 remain available only from 09:20; no R17+ observation or later variant has been inserted.

### Continue studying — chapter 02 of 04 (transitional corrections)

[← Chapter 01](../MANUSCRIPT.md#ch-01) · [Course chapter index](../../SUBJECTS.md) · [Chapter 03 →](../MANUSCRIPT.md#ch-03) · [Worked results in the principal book](../MANUSCRIPT.md#answers)

### Official primary sources and rights

- [NIST SP 800-61 Revision 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final). April 2025; the RS.AN-06 and RS.AN-07 discussion supports preserving the integrity, provenance, appropriate access and retention of response records. It does **not** prescribe the TRI2 flags, example timestamps or E1 program.
- [NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final). August 2006; advises on IT-oriented forensic source and copy handling while warning that it is not an all-inclusive procedure or legal advice.
- [NIST SP 800-92 — Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final). September 2006; discusses enterprise logging infrastructure and practices, not the TRI2 query or a source-specific 24-hour clock.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework). February 2024; general risk-management outcomes, not a mandatory TRI2 priority scheme.
- [RFC 3339 — Date and Time on the Internet: Timestamps](https://www.rfc-editor.org/rfc/rfc3339.html), IETF; defines a format for offsets but does **not** authenticate source clocks or establish incident ingestion times.

All Harbor Library inputs, T1/T2/TRI2/E1 exercises and corrective examples are **synthetic educational material**. The new release guards, E1 safety fix, EX018 table and outputs are original CyberABC teaching material, not claims made by NIST or facts about a real organization. Editorial responsibility is exclusively [hiagokinlevi](https://github.com/hiagokinlevi); original maintainer-owned content follows [RIGHTS.md](../../../../../../RIGHTS.md) and [CC0 1.0](../../../../../../LICENSE), subject to third-party rights. No real system, account, data source, retention setting or production file is accessed. These corrections do not constitute a full chapter/book approval or independently remeasured A4 edition.
