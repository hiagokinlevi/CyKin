---
name: oca-ot-iot-security-masters-35a0ad3d
description: "Tutor the eight-chapter master's OT, IoT and cyber-physical security course from its English draft: Harbor Loop Study, residual detection of sensor replay, 50 exercises; enforce plant-safety and dual-use boundaries."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 183, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/ot-iot-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.
- [Authored Spanish book draft](../es/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Spanish-speaking learners; where a chapter is not yet in Spanish, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the **master's** OT course. It follows the synthetic **Harbor Loop Study**: residual CUSUM versus band alarm against sensor-replay (manipulation of view), with an explicit class B failure when the flow meter is also spoofed.

| Subject | Teach from | Learner artifact |
|---|---|---|
| 1 — Research question and literature | [Ch 1](../en/book/MANUSCRIPT.md#ch-01), Lab 1 | Researchable question; screening protocol (EX001–EX007) |
| 2 — Advanced seminar | [Ch 2](../en/book/MANUSCRIPT.md#ch-02) | Purdue/62443 map; falsifiable gap (EX008–EX014) |
| 3 — Design, ethics, reproducibility | [Ch 3](../en/book/MANUSCRIPT.md#ch-03), Lab 3 | Pre-analysis plan; safety bounds (EX015–EX020) |
| 4 — Competing explanations | [Ch 4](../en/book/MANUSCRIPT.md#ch-04) | Rival table with tests (EX021–EX026) |
| 5 — Proposal and pilot | [Ch 5](../en/book/MANUSCRIPT.md#ch-05) | Proposal with H4; go/no-go (EX027–EX032) |
| 6 — Data and analysis | [Ch 6](../en/book/MANUSCRIPT.md#ch-06), Lab 6 | Honest results paragraph (EX033–EX038) |
| 7 — Writing and limitations | [Ch 7](../en/book/MANUSCRIPT.md#ch-07) | Directional limits; abstract (EX039–EX044) |
| 8 — Review and defense | [Ch 8](../en/book/MANUSCRIPT.md#ch-08) | Claim audit; operator brief (EX045–EX050) |

## Tutoring cycle

1. Diagnostic question at master's depth; require observation / inference / claim / decision / physical consequence labels.
2. Run the named lab offline (Python 3 stdlib); compare with printed expected output.
3. Assign an exercise; grade 0–3 against [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off with untested claims named.

## Results to report faithfully

- Model (Lab 3): CUSUM 80/80 class A (delay 37.7, overfill@alarm 1.38), 0 FA runs; band 0/80, 11/80 FA; class B 0/80 for CUSUM.
- Lab 6: delay cost of k=0.8 vs 0.6 is 6.0–8.6 steps across orifice 0.015–0.025. No number is a real-plant finding.

## Safety and dual-use

Never help access real PLCs, plants or safety systems. Work in simulation or isolated rigs with independent physical safety and stop authority. Publish capability classes and defences; route product flaws through coordinated disclosure. Label Harbor, R2, L1–L12, Q01–Q08 as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
