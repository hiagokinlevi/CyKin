# Chapter 3 §§3.5–3.8a — Recovery Technical Corrections (DRAFT)

**Editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). **English rapid course.** These independently reviewed blocks are proposals, not integrated lessons or publication approval. [Sole principal manuscript](../MANUSCRIPT.md#ch-03) · [Book standard](../../../../../../BOOK_STANDARD.md).

**Review baseline:** Public main commit fff4e2f5b0f79895abd5a20959511704930bb547; MANUSCRIPT.md SHA-256 4781f6a7bbc0a6f94fd8f3ab30b038be0e89de153e29eecd4f596bc8b3752093. The recorded 327-page A4 preflight and 50 matched exercise/answer IDs do not make the book complete.

**Release firewall:** R1–R8 at 09:05, R1–R16 at 09:20, and R1–R24 for the canonical 09:37 decision. P1/C1 and V1 are *later* fictional §3.6 lab releases; K1 is a further optional replay; RTE3 is an unrelated 2026-01-15 synthetic exercise. None of their favorable or unfavorable results can be retroactively imported into the 09:37 decision.

## Independent reproduction of unchanged original programs

The two complete original Listing 3.1 Python blocks were executed sequentially in their own isolated Python 3.13.5 namespace; all **six** published lines matched literally:

~~~text
B17: MATCH target=Room 4 current=Room 4
B18: MATCH target=Cancelled current=Cancelled
B19: MISMATCH target=Room 1 current=Room 3
B20: MISMATCH target=Room 3 current=Room 1
counts: MATCH=2, MISMATCH=2, MISSING_CURRENT=0, UNEXPECTED_CURRENT=0
rejected variant: current: duplicate booking ID B20
~~~

The complete original RTE3 Python program was run separately; all **eight** published lines matched literally:

~~~text
BASELINE_ACCEPTED age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=85m_WITHIN_120m
MISSING_INTERRUPTION age=UNKNOWN unrecovered=0_KNOWN_UNRECOVERED RTO=UNKNOWN_INTERRUPTION
OLD_COPY age=55m_OVER_30m unrecovered=UNBOUNDED RTO=NO_ACCEPTANCE_GATES
ACCEPTANCE_FAILED age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=NO_ACCEPTANCE_GATES
NO_OWNER_RECEIPT age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=NO_OWNER_ACCEPTANCE
KNOWN_MISSING_WRITE age=10m_WITHIN_30m unrecovered=1_KNOWN_UNRECOVERED RTO=NO_ACCEPTANCE_GATES
INCOMPLETE_LEDGER age=10m_WITHIN_30m unrecovered=UNBOUNDED RTO=NO_OWNER_ACCEPTANCE
UNVERIFIED_CLOCK age=UNKNOWN unrecovered=0_KNOWN_UNRECOVERED RTO=UNKNOWN_CLOCK
~~~

Matching the expected text is evidence of program reproducibility, *not* proof of sufficient acceptance rules.

## Correction A — Listing 3.1 requires an independent P1 frame

**Insertion:** At the end of §3.7, directly after Listing 3.1 part 2 and before its “Expected evidence” paragraph. Append the five supplemental output lines in the final answer appendix immediately after the original “Chapter 3 CSV comparison lab — worked result”. Keep the original program and its six output lines unchanged.

**Finding — section, input, result:** Remove B19 from both the target and current CSV strings. The original script prints MATCH=2, MISMATCH=1, MISSING_CURRENT=0, UNEXPECTED_CURRENT=0, even though the expected four-booking comparison frame is now missing B19. Supplying two header-only CSVs produces counts of zero in all four categories. The original duplicate check does work and should be retained.

**Consequence:** Symmetrical missing source rows can appear to satisfy a four-ID comparison when no independent expected-ID frame is enforced. The input is a deliberately manipulated classroom variant, *not* proof of source deletion. A zero count of missing rows within the supplied union is not evidence that the requested frame was complete.

**Corrective teaching:** The independently declared test frame is B17, B18, B19, B20. Check target membership against that set first, then classify missing or extra current rows as review items. This validates only the four-ID toy exercise; the true approval, provenance, completeness of an operational booking database, and authorization to make corrections remain external to this code.

**Complete executable standalone Python 3 correction (in memory, no files or network):**

~~~python
import csv
from io import StringIO

EXPECTED_IDS = frozenset({'B17', 'B18', 'B19', 'B20'})
P1 = '''booking_id,state
B17,Room 4
B18,Cancelled
B19,Room 1
B20,Room 3
'''
C1 = '''booking_id,state
B17,Room 4
B18,Cancelled
B19,Room 3
B20,Room 1
'''

def read_csv(source):
    reader = csv.DictReader(StringIO(source))
    if reader.fieldnames != ['booking_id', 'state']:
        raise ValueError('bad header')
    result = {}
    for row in reader:
        if None in row or not row['booking_id'] or not row['state']:
            raise ValueError('invalid field count or empty field')
        key, value = row['booking_id'].strip(), row['state'].strip()
        if not key or not value or key in result:
            raise ValueError('blank value or duplicate booking ID')
        result[key] = value
    return result

def assess_frame(target_csv, current_csv):
    target, current = read_csv(target_csv), read_csv(current_csv)
    missing_target = sorted(EXPECTED_IDS - target.keys())
    extra_target = sorted(target.keys() - EXPECTED_IDS)
    if missing_target or extra_target:
        return (f'REJECT_TARGET_FRAME missing={",".join(missing_target) or "-"} '
                f'extra={",".join(extra_target) or "-"}')
    missing_current = sorted(EXPECTED_IDS - current.keys())
    extra_current = sorted(current.keys() - EXPECTED_IDS)
    matches = sum(target[key] == current[key] for key in EXPECTED_IDS & current.keys())
    mismatches = sum(target[key] != current[key] for key in EXPECTED_IDS & current.keys())
    state = 'REVIEW_CURRENT_FRAME' if missing_current or extra_current else 'FRAME_COMPLETE_FOR_FOUR_IDS'
    return (f'{state} MATCH={matches} MISMATCH={mismatches} '
            f'MISSING_CURRENT={len(missing_current)} UNEXPECTED_CURRENT={len(extra_current)}')

CASES = [
    ('BASE', P1, C1),
    ('BOTH_OMIT_B19', P1.replace('B19,Room 1\n', ''), C1.replace('B19,Room 3\n', '')),
    ('HEADER_ONLY', 'booking_id,state\n', 'booking_id,state\n'),
    ('MISSING_CURRENT_B20', P1, C1.replace('B20,Room 1\n', '')),
    ('EXTRA_CURRENT_B21', P1, C1 + 'B21,Room 2\n'),
]
for label, expected, observed in CASES:
    print(f'{label}: {assess_frame(expected, observed)}')
assert assess_frame(P1, C1).startswith('FRAME_COMPLETE_FOR_FOUR_IDS')
~~~

**Exact independently tested five-line output:**

~~~text
BASE: FRAME_COMPLETE_FOR_FOUR_IDS MATCH=2 MISMATCH=2 MISSING_CURRENT=0 UNEXPECTED_CURRENT=0
BOTH_OMIT_B19: REJECT_TARGET_FRAME missing=B19 extra=-
HEADER_ONLY: REJECT_TARGET_FRAME missing=B17,B18,B19,B20 extra=-
MISSING_CURRENT_B20: REVIEW_CURRENT_FRAME MATCH=2 MISMATCH=1 MISSING_CURRENT=1 UNEXPECTED_CURRENT=0
EXTRA_CURRENT_B21: REVIEW_CURRENT_FRAME MATCH=2 MISMATCH=2 MISSING_CURRENT=0 UNEXPECTED_CURRENT=1
~~~

Even the four-ID baseline has two mismatches and cannot be accepted as corrected service. A later operator would need specific approval and a *new* authoritative comparison. V1's blank actor remains a distinct audit failure.

## Correction B — RTE3: no full-service RTO pass with unsupported data or gates

**Insertion:** In §3.8a, after the existing complete RTE3 Python program and before “Check your eight-line transcript”. Add the corrective nine-line transcript after the original eight-line “RTE3 — Worked result” in the final appendix. Do not modify its original fixture or labels.

**Finding — section, input, result:** In the original RTE3 code, removing W-B only from restored_writes while all gate Booleans remain True prints *unrecovered=1_KNOWN_UNRECOVERED* **and simultaneously** *RTO=85m_WITHIN_120m*. Set ledger_complete=False with the same positive gates and the result becomes *unrecovered=UNBOUNDED* **and** the same favorable RTO. Set gates={} and the program still reports a favorable RTO because its any() check has an empty iterable. Set technical_ready=None and it also measures a favorable RTO, despite lacking a declared milestone.

**Consequence:** The calculated interval can be promoted to a **passed full-service recovery objective** in the face of contradictory mandatory evidence. The original negative examples preset the data gate to False and therefore do not challenge these combinations independently.

**Corrective teaching:** Only a complete *declared test-frame* ledger with no known unrecovered accepted operations and with all four mandatory gates—data, authorized, denied and audit—supports the toy *full-service* acceptance result. A restricted service with a knowingly missing operation would require a separately scoped, approved exception and its own metric. A copy-age screen is not a claim of zero data loss or demonstrated RPO.

**Complete executable standalone Python 3 correction (in memory, no files or network):**

~~~python
from copy import deepcopy
from datetime import datetime

DAY = '2026-01-15'
RTO_TARGET_MIN, RPO_TARGET_MIN = 120, 30
REQUIRED_GATES = {'data', 'authorized', 'denied', 'audit'}

def at(clock):
    return None if clock is None else datetime.fromisoformat(f'{DAY}T{clock}:00+00:00')

BASE = {
    'interrupted': at('09:45'), 'copy_at': at('09:35'),
    'technical_ready': at('10:20'), 'accepted_at': at('11:10'),
    'clock_verified': True,
    'gates': {'data': True, 'authorized': True, 'denied': True, 'audit': True},
    'owner_receipt': True,
    'accepted_writes': {'W-A', 'W-B'}, 'restored_writes': {'W-A', 'W-B'},
    'ledger_complete': True,
}

def stricter_measure(row):
    i, s, t, a = (row[k] for k in ('interrupted', 'copy_at', 'technical_ready', 'accepted_at'))
    clocks_ok = row['clock_verified'] is True
    age = 'UNKNOWN'
    if clocks_ok and i is not None and s is not None and s <= i:
        delta = int((i-s).total_seconds() // 60)
        age = f'{delta}m_{"WITHIN" if delta <= RPO_TARGET_MIN else "OVER"}_{RPO_TARGET_MIN}m'
    missing = row['accepted_writes'] - row['restored_writes']
    coverage = 'UNBOUNDED' if row['ledger_complete'] is not True else f'{len(missing)}_KNOWN_UNRECOVERED'
    if i is None:
        outcome = 'UNKNOWN_INTERRUPTION'
    elif not clocks_ok:
        outcome = 'UNKNOWN_CLOCK'
    elif t is None:
        outcome = 'UNKNOWN_TECHNICAL_READY'
    elif t < i or (a is not None and (a < t or a < i)):
        outcome = 'INVALID_ORDER'
    elif set(row['gates']) != REQUIRED_GATES:
        outcome = 'REQUIRED_GATES_MISSING'
    elif any(row['gates'][k] is not True for k in REQUIRED_GATES):
        outcome = 'NO_ACCEPTANCE_GATES'
    elif row['ledger_complete'] is not True:
        outcome = 'DATA_COVERAGE_UNKNOWN'
    elif missing:
        outcome = 'KNOWN_UNRECOVERED_WRITES'
    elif row['owner_receipt'] is not True or a is None:
        outcome = 'NO_OWNER_ACCEPTANCE'
    else:
        minutes = int((a-i).total_seconds() // 60)
        outcome = f'{minutes}m_{"WITHIN" if minutes <= RTO_TARGET_MIN else "OVER"}_{RTO_TARGET_MIN}m'
    return f'age={age} unrecovered={coverage} RTO={outcome}'

VARIANTS = [
    ('BASELINE', {}),
    ('MISSING_WRITE_DESPITE_GREEN_GATES', {'restored_writes': {'W-A'}}),
    ('INCOMPLETE_LEDGER_DESPITE_GREEN_GATES', {'ledger_complete': False}),
    ('NO_REQUIRED_GATES', {'gates': {}}),
    ('NO_TECHNICAL_READY', {'technical_ready': None}),
    ('AUDIT_FAILED', {'gates': {**BASE['gates'], 'audit': False}}),
    ('NO_OWNER_RECEIPT', {'owner_receipt': False, 'accepted_at': None}),
    ('MISSING_INTERRUPTION', {'interrupted': None}),
    ('BAD_TIME_ORDER', {'accepted_at': at('10:19')}),
]
for label, changes in VARIANTS:
    case = deepcopy(BASE)
    case.update(changes)
    print(f'{label}: {stricter_measure(case)}')
assert stricter_measure(BASE).endswith('RTO=85m_WITHIN_120m')
~~~

**Exact independently tested nine-line output:**

~~~text
BASELINE: age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=85m_WITHIN_120m
MISSING_WRITE_DESPITE_GREEN_GATES: age=10m_WITHIN_30m unrecovered=1_KNOWN_UNRECOVERED RTO=KNOWN_UNRECOVERED_WRITES
INCOMPLETE_LEDGER_DESPITE_GREEN_GATES: age=10m_WITHIN_30m unrecovered=UNBOUNDED RTO=DATA_COVERAGE_UNKNOWN
NO_REQUIRED_GATES: age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=REQUIRED_GATES_MISSING
NO_TECHNICAL_READY: age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=UNKNOWN_TECHNICAL_READY
AUDIT_FAILED: age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=NO_ACCEPTANCE_GATES
NO_OWNER_RECEIPT: age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=NO_OWNER_ACCEPTANCE
MISSING_INTERRUPTION: age=UNKNOWN unrecovered=0_KNOWN_UNRECOVERED RTO=UNKNOWN_INTERRUPTION
BAD_TIME_ORDER: age=10m_WITHIN_30m unrecovered=0_KNOWN_UNRECOVERED RTO=INVALID_ORDER
~~~

**Limits:** BASELINE remains a positive *synthetic selected-scope consistency result* only. The code never authenticates source clocks, approved user outcomes, complete institution-wide journals, the real service owner or production recovery. It calculates snapshot age separately from the evidence of recovered accepted operations. No status denotes globally zero data loss. The 85-minute value cannot be used for the canonical 09:37 case.

## Correction C — Exercise-to-answer output correspondence, EX033–EX035

**Insertion:** Add each small model answer table beneath the corresponding original “EX033 — Worked result”, “EX034 — Worked result” or “EX035 — Worked result” section in the manuscript's final appendix. Keep the original exercise IDs, worded learning goals, existing 0–2 scoring contract and all original answer content. These are missing **requested answer formats**, not additional exercises.

### EX033 — Compact RTE3 measurement card

**Input:** EX033 asks for an isolated restore plan, four *not tested* booking rows, and a separate compact measurement card. The existing answer provides the necessary reasoning but no standalone card.

| Required field | Model answer status |
|---|---|
| Essential-service interruption event | Source, owner and actual timestamp **not supplied** for canonical Harbor Library |
| Copy and isolated restoration | Copy ID, claimed capture time, authorized isolated environment and actual start/end **to be obtained/measured** |
| Technical-ready milestone | **Not measured**; import or page load is not service acceptance |
| Booking correctness | After P1 release, B17–B20 target values known for the synthetic lab; no separately restored copy comparison supplied |
| Access and audit gates | Separate V1 tests have limited permitted/denied outcomes and a **blank audit actor**; V1 is not a completed restore |
| Owner acceptance endpoint | Scope, authority and acceptance time **not supplied**; canonical recovery elapsed time **unknown** |

The original four B17–B20 expected-state rows remain **not tested** until an approved, observed restore and independent comparison are recorded.

### EX034 — Three requested measurement columns

**Input and reproducible calculation:** The hypothetical midnight copy is 09:45 − 00:00 = **9h45** old, exceeding the **30m** objective by **9h15** as a standalone copy-age screen. Neither amount is a proven lost-data duration. The original model answer gives this reasoning but not the explicitly requested three-column artifact.

| Copy age screen | Accepted-operation evidence after copy | Actual restored/verified operation result |
|---|---|---|
| **9h45 old; 9h15 beyond** hypothetical standalone 30m screen | **Unknown**: R23 supplies no complete, durable post-copy accepted-operation ledger or verified replay source | **Not measured**: no actual owner-approved restore, new authoritative state comparison or proven irrecoverable accepted operation |

An illustrative two-hour RTO cannot be marked achieved from R23, or from K1's later fictional 11- and 14-minute isolated import trials.

### EX035 — Acceptance-time evidence row

**Input:** EX035 requires three acceptance checks (booking, access, audit) **and a separate acceptance-time evidence row** under the RTE3 extension. The original answer correctly describes that condition in narrative form but leaves its explicit row unstated.

| Acceptance check | Expected evidence | Currently available exercise result | Owner and next action |
|---|---|---|---|
| Scoped owner acceptance and interruption-to-service elapsed time | Verified interruption start, passed booking/access/audit gates, owner acceptance/rejection time and declared restricted/full service scope | **Unmeasured and unaccepted for full return**: C1 still mismatches P1 on B19/B20, V1 lacks its audit actor, and no canonical full-service acceptance timestamp is provided | Service owner and incident lead retain a pending decision; require new authorized booking/audit checks and a dated scoped approval before calculating elapsed recovery |

The original three rows remain. Add the conditional fourth **queue** gate only after the separate Branch P release; that queue is not K1, MQ3, V1 or RTE3.

## Verified boundaries; no further corrective blocks required

**§3.6 P1/C1/V1:** The original case comparison correctly marks B17/B18 as matches and B19/B20 as mismatches. V1 supports limited permitted/denied tests while its missing actor is a real *exercise result* failure. An approved correction still requires later new-state verification. No P1/C1/V1 values justify the canonical 09:37 decision.

**§3.8 K1:** No Python listing is provided in K1, so there is no K1 program to execute. Its 09:45 candidate age screens are correct: K-A 45m, K-B 25m, K-C 7m. K-A's four-row P1 match does not establish recovery of other legitimate work; K-B has a digest mismatch; K-C has B19/B20 mismatches despite its more recent timestamp. A 14m or 11m isolated import and read is not an accepted service-level RTO measurement. The existing K1 worked table describes appropriately limited candidate-level gates, so no replacement of its values is warranted.

**Primary-source and rights checks:** [NIST SP 800-34 Rev. 1 updated final](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), [NIST SP 800-184 final](https://csrc.nist.gov/pubs/sp/800/184/final), [NIST RTO glossary](https://csrc.nist.gov/glossary/term/recovery_time_objective) and [NIST RPO glossary](https://csrc.nist.gov/glossary/term/recovery_point_objective) were verified at their official pages. Their definitions and recovery-test guidance do **not** prescribe the book's original or corrected validators. Preserve third-party rights under [RIGHTS.md](../../../../../../RIGHTS.md).

**Anchors and safety:** The manuscript's [RTE3 lab anchor](../MANUSCRIPT.md#ir-rapid-ch03-rte3-lab) and [worked-result anchor](../MANUSCRIPT.md#ir-rapid-ch03-rte3-result) exist. The two corrective programs are standalone, Python-standard-library and in-memory only. They never import real records, access a service, write files, delete data or execute recovery. Neither the chapter nor the book is approved; the manuscript remains the canonical draft until an explicit maintainer integration.
