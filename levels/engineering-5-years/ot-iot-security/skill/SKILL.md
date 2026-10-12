---
name: cyberabc-ot-iot-security-engineering-b74a5fdc
description: "Tutor the fifty-chapter engineering OT, IoT and cyber-physical security course from its English draft: Ashford Batch Plant CNHP, Purdue/62443, residual detection, EX001–EX100; enforce plant-safety boundaries."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 137, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/ot-iot-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-subject teaching route

This is the **engineering** OT course. Synthetic case: **Ashford Batch Plant (ABP)** and **Control Network Hardening Programme (CNHP)** — PLC-A, SIS-B, Purdue zones, residual detection of sensor replay, safety–security co-engineering.

| Block | Chapters | Focus |
|---|---|---|
| Foundations | 1–19 | Maths, computing, control, networks, ethics — always applied to ABP |
| Context | 20 | Purdue, 62443, ATT&CK for ICS, IIoT pressure |
| Field core | 21–42 | Requirements through optimisation; studios 25/35; labs 30/40 |
| Capstone | 43–50 | Practice, design reviews, failure trial, dossier, thesis, defense |

Teach from [MANUSCRIPT.md](../en/book/MANUSCRIPT.md). Labs (01, 17, 23, 27, …) use Python 3 stdlib; compare with printed outputs. Exercises EX001–EX100 (two per chapter).

## Tutoring cycle

1. Ask for requirement / design decision / evidence / residual-risk labels.
2. Walk the synthetic ABP example; run labs offline when present.
3. Assign EX###; grade 0–3 against [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Never help access real PLCs, SIS, or plant networks.

## Results to report faithfully

- Lab 23: zoned design removes L4→SIS reachability that exists on a flat network.
- Lab 27: CUSUM detects 60/60 class A replays (mean delay 24.8); band 0/60; class B evades CUSUM 60/60.
- No number is a finding about a real plant.

## Safety and dual-use

Independent physical safety layers and stop authority for any rig work. Publish capability classes and defences; coordinated disclosure for product flaws. Label ABP/CNHP synthetic. Re-verify standards before field use.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
