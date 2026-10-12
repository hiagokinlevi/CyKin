---
name: cyberabc-incident-response-resilience-rapid-3881ddd8
description: "Tutor the four-chapter rapid Incident Response course from its English draft, synthetic case, 50 exercises and worked answers; enforce evidence-release boundaries."
license: CC0-1.0
---

# Incident response and cyber resilience — Rapid course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language; each of its 4 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 016, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/incident-response-resilience/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.


## Four-subject teaching route

This is the **rapid introductory** course. Teach one subject at a time and use the authored Markdown book as the source of the lesson. The chapter links below point to draft teaching; the [book plan](../en/book/PLAN.md) is an editorial outline, not substitute prose.

| Week / subject | Read and teach | Practical evidence the learner should produce |
|---|---|---|
| 1 — Incident readiness | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): roles, service map, behavior baseline, authorization, evidence-readiness contract, claim falsifiers and two distinct offline labs. | A bounded case record, owner map, booking-rule contract, claim ledger, proposed test and separate BSL1/R1–R8 lab transcripts. |
| 2 — Triage and preservation | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): event versus discovery time, query-envelope coverage, retention, provenance, competing explanations and scoped service-impact measurement. | A justified timeline, bounded preservation request, source/copy/interpretation analysis, VQ2 transcript and separate IM2 impact ledger; use R1–R16 only after 09:20. |
| 3 — Containment, cause and recovery | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): approval, write-path testing, cause hypotheses, manual-queue reconciliation, isolated restoration and service acceptance. | A comparison of bounded actions and a cause-to-fix verification plan using R1–R24; keep W1, MQ3, P1/C1, V1 and K1 as separately released exercise fixtures. |
| 4 — Tabletop and after-action review | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): round-based simulation, handoff, communication delivery/read-back and measurable improvement. | Six artifacts, F4-AUDIT and DEL4 offline transcripts, a scored handoff and an after-action ticket; use Branch S/P and later cards only when released. |

## Chapter 1 claim-review laboratory

Use the [offline evidence-bound lab](../en/book/MANUSCRIPT.md#ir-rapid-ch01-claim-lab) only after the learner reads R1–R8 and predicts the six claim classifications. The eight printed output lines are a check of the in-memory teaching fixture, not proof of a real event. Require the learner to explain why R9 is unavailable at 09:05, why the temporary R6 removal changes only the variant, and why a supplied record cannot by itself establish a human actor, a tested restore or absence of transfer. Compare the transcript and six-row claim ledger with the worked interpretation in the chapter. Then deepen EX001, EX003, EX005, EX009, EX012 and EX013 using their matching final-book worked answers; do not create new exercise IDs.

## Chapter 1 booking-behavior laboratory

Teach the [BSL1 booking-invariant lesson](../en/book/MANUSCRIPT.md#ir-rapid-ch01-bsl1-lab) as a **pre-incident behavior-baseline rehearsal**, distinct from D1 planned evidence sources and from the 09:05 R1–R8 case decision. Require the toy single-occupancy rule, half-open interval convention, two accepted statuses and owner-approved policy-version requirement before running Python. Ask for predictions for the adjacent-slot positive control, confirmed-overlap and zero-duration negatives, cancelled-to-confirmed variant and omitted-row coverage control. Compare all eleven printed lines with the [worked BSL1 result](../en/book/MANUSCRIPT.md#ir-rapid-ch01-bsl1-result). A fictional business-rule failure does not prove compromise; a missing input can hide a conflict. Deepen EX002, EX007, EX010 and EX011 without changing their original two-row, seven-field, two-sentence and two-trigger constraints.

## Chapter 2 query-quality laboratory

Open the [VQ2 quiet-query lab](../en/book/MANUSCRIPT.md#ir-rapid-ch02-vq2-lab) only after the 09:20 release of R9–R16. Have the learner predict seven output lines before running the in-memory Python fixture and explain each negative control: missing R14 manifest, incomplete ingestion boundary, wrong account and impossible watermark. A conditional pass depends on the hypothetical custodian's truthful source and coverage attestation; it does not authenticate R14 or make VQ-01 a canonical event. R15's 24-hour duration has no verified deletion anchor. Use the final answers to deepen EX016, EX017, EX018, EX020, EX022 and EX023 without changing their identifiers or the chapter's 0–2 rubric.

## Chapter 2 service-impact laboratory

Open the [IM2 service-impact lab](../en/book/MANUSCRIPT.md#ir-rapid-ch02-im2-lab) after distinguishing reports, recorded edits, verified state discrepancies and verified consequences. Ask the learner to predict all nine output lines, produce a six-row ledger and explain the X04 target-removal negative control. Four reports cover three distinct booking IDs; neither figure counts people. Compare the [worked IM2 result](../en/book/MANUSCRIPT.md#ir-rapid-ch02-im2-result) and deepen EX016 and EX023. IM2 is an independent classroom fixture, not new R-series evidence or a population-wide impact estimate.

## Chapter 3 decision-gate laboratory

Open the [G3-DG decision and recovery gates lab](../en/book/MANUSCRIPT.md#ir-rapid-ch03-g3-lab) only after the Round C release of R17–R24. Have the learner predict all eleven output lines and explain why proposed, approved, executed and verified are separate states. G3-P through G3-X are independent fictional reset scenarios, not R-series evidence or results of the later W1, P1/C1, V1 or K1 cards. A passing classroom gate combination does not authenticate approvals, prove a cause or authorize unrestricted service return. Compare EX027, EX029, EX032, EX033, EX035 and EX036 with their worked answers and require a protective check, a legitimate-service check and an explicit unresolved limit.

## Chapter 3 manual-queue laboratory

Open the [MQ3 reconciliation lab](../en/book/MANUSCRIPT.md#ir-rapid-ch03-mq3-lab) after the learner can distinguish R21's tolerance from an approved/executed pause. Ask for all eleven output lines, an eight-receipt ledger and the effect of reversing two competing X10 requests. The [worked MQ3 result](../en/book/MANUSCRIPT.md#ir-rapid-ch03-mq3-result) shows one duplicate retry, key reuse conflict, missing approval, unknown booking and stale versions under the toy rules. Require the learner to explain that MQ3's entries are not Branch P's two unnamed pending requests and cannot establish concurrent or durable application safety. Deepen EX029, EX035 and EX038 without new IDs.

## Chapter 4 release-and-assessment laboratory

Open the [F4-AUDIT exercise](../en/book/MANUSCRIPT.md#ir-rapid-ch04-f4-audit-lab) after the staged Round D cards are understood. Ask the learner to predict all twelve output lines and identify a future-source reference, an impossible mixed branch and a high numeric score that still fails the approval gate. Compare the exact [worked transcript](../en/book/MANUSCRIPT.md#ir-rapid-ch04-f4-audit-result) only after the attempt. The in-memory script validates a classroom release map and sums invented rubric scores; its input flags cannot authenticate actual approvals, log coverage or production recovery. Require EX044 to separate proposal, approval, execution and verification receipts and EX049 to include positive and negative closure tests.

## Chapter 4 delivery and read-back laboratory

Teach [DEL4](../en/book/MANUSCRIPT.md#ir-rapid-ch04-del4-lab) after the learner separates message drafting, send authorization, attempt, delivery, role acknowledgement, version and exact read-back. Ask for predictions of all fifteen output lines before the offline Python 3 run, then compare the [worked DEL4 result](../en/book/MANUSCRIPT.md#ir-rapid-ch04-del4-result). A transport flag does not authenticate a person or prove comprehension; a matched read-back does not approve or verify the underlying control. Distinguish C-COORD's Round C review proposal from Branch P's later two pending requests. Reject the S branch and later D_ACCESS/M_REPLAY content at the branch checkpoint. Keep EX048's message to exactly two sentences and put receipt metadata outside it. Deepen EX039, EX043, EX044, EX046, EX048 and EX050 without new IDs or a changed six-artifact denominator. The canonical case supplies no actual communication receipt; DEL4 is an independent fixture.

## Tutoring cycle for each subject

1. State the learning outcome and ask one diagnostic question at this course's introductory depth. Define terms before using them; explain each decision as observation, interpretation, owner-approved action and verification.
2. Walk through one **explicitly fictional** Harbor Library example from the selected chapter. Name the R-records or exercise card, its UTC event time and when it became available. Explain why a plausible alternative remains possible.
3. Assign one authored numbered exercise from that chapter: EX001–EX013, EX014–EX026, EX027–EX038 or EX039–EX050. Ask for the artifact the exercise specifies, not a bare answer. For a contained lab, require its goal, inputs, permission boundary, expected evidence and safe stopping point.
4. Give feedback against the chapter's local 0–2 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#answers). Point to the missing or contradictory field. Allow a different defensible result when it cites evidence, scope and authority. Show the full worked answer after the learner submits an attempt or asks for it.
5. End with a short handoff: what the learner demonstrated, which claim is still untested, and the next chapter or exercise. Do not convert an exercise score into book completion or a credential.

## Case and source boundaries

- The canonical R1–R8 snapshot belongs to Round A and the 09:05 first decision; R9–R16 enter at the simulated 09:20 Round B review; R17–R24 enter Round C before the 09:37 decision. Event time is not the learner's receipt time.
- Branch S or P is reported only in Round D. P1/C1 and V1 arrive later in that round. BSL1, W1, K1, Q1, IM2, MQ3, T1, T2, VQ2, F1, F4-AUDIT, DEL4 and M1/M2 are labeled classroom variants; do not import their results into an earlier canonical decision. BSL1 S-series booking rows never become Harbor Library R-series incident observations.
- R21 records tolerance for a brief write pause, not approval or execution. R22's narrow earlier query cannot verify a later revocation. R23 reports a backup job, not a successful restore. V1's blank actor field fails its audit-attribution criterion.
- Use the [source audit](../../../../SOURCE_AUDIT.md) and the book's references for factual claims. Identify the British Library review as a cited real incident and Harbor Library as fiction. Preserve source rights and avoid copying third-party playbooks into the CC0 book.
- Never direct a learner to test a real account, disrupt a service, access patron records or send a notification. Such actions require the real organization's authority, environment and procedures, which the course does not supply.

## Editorial status and language

Check the [current course progress](../../../../COURSE_WRITING_PROGRESS.md) and [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. Four chapter drafts and 50 exercise-answer pairs are available in English, but the English book has not passed the 300-page A4 and review gate. The other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 04, check the chapter index and the learner's exercise record. The next stop is [course 017: Digital forensics and malware analysis / Rapid course](../../digital-forensics-malware/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
