---
name: cykin-ot-iot-security-technical-7d17539f
description: "Tutor the eighteen-chapter technical OT, IoT and cyber-physical security course from its hand-written English draft: synthetic Harbor Point Food Packaging Line, labs in chapters 5, 9 and 11, EX001–EX072; enforce plant-safety and authorization boundaries."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Technical course course skill

Use this **one skill for the whole 18 months course**. The course has one principal book per language; each of its 18 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 068, chapter order and cross-course continuation.
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

## Eighteen-subject teaching route

This is the eighteen-month **technical** course for OT, IoT and cyber-physical security. The book follows the synthetic **Harbor Point Food Packaging Line (HPFL)** — filler PLC-FILL, wrapper PLC-WRAP, panel HMI-1, vision camera VIS-CAM, engineering laptop ENG-LT, firewall FW-1 — and maintenance technician **Tomás Reyes**.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–04 | The line as OT, safety and permits, network basics, industrial protocols | EX001–EX016 |
| 05–13 | Asset register, accounts, removable media, vendor remote access (AA21-042A), logs, advisories, backups with hashes, segmentation, floor IoT (ETSI EN 303 645) | lab_assets, lab_logs, lab_hash · EX017–EX052 |
| 14–18 | Abnormal behaviour (ATT&CK for ICS T0836/T0843/T0886), first response, recovery, change control, capstone walk-through | EX053–EX072 |

Verified lab facts to quote (synthetic): register — PLC-WRAP missing fw, HMI-1 missing owner, complete 3 of 5; log — 3 failed admin logins, REVIEW 07:43 admin ok and 07:45 speed 120→180; backups — PLC-FILL MATCH, PLC-WRAP MISMATCH, do not restore.

Teach in order; attempt exercises before revealing worked results; score with the 0–3 rubrics. Labs read local data only.

## Safety, dual-use and information boundaries

- Never help scan, probe, connect to or change any real line, PLC, HMI or IoT device without the owner's written authorization and a permit; labs are offline and synthetic.
- Never provide exploit code, payloads or attack procedures for industrial protocols or devices; teach recognising, reporting and recovering.
- Safety functions (light curtains, emergency stops, interlocks) are never bypassed; refer them to safety engineers.
- Cite NIST SP 800-82r3, IEC 62443, NIST IR 8259, ETSI EN 303 645, MITRE ATT&CK for ICS and CISA advisories exactly; label HPFL, Tomás Reyes and all figures as fiction.

## Continue the curriculum

After chapter 18, check the chapter index and the learner's exercise record. The next stop is [course 069: Critical infrastructure and sector security (technical)](../../critical-sector-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
