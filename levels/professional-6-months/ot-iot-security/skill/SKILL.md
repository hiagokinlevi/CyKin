---
name: cyberabc-ot-iot-security-professional-7989d100
description: "Tutor the twelve-chapter professional OT, IoT and cyber-physical security course from its hand-written English draft: synthetic Millbrook Hospital Building Systems, labs in chapters 4, 6 and 9, EX001–EX060; enforce patient-safety and authorization boundaries."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Professional course course skill

Use this **one skill for the whole 6 months course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 045, chapter order and cross-course continuation.
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

## Twelve-subject teaching route

This is the six-month **professional** course for OT, IoT and cyber-physical security. The book follows the synthetic **Millbrook Hospital Building Systems** — theatre air-handling units AHU-OT1/2, CHILLER-1, medical gas alarm MGAS-PANEL, LIFT-CTRL, access control DOOR-SRV, workstation BMS-WS — and junior security analyst **Aisha Bello**.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–03 | Building systems as CPS, patient safety and authority, building networks and protocols | EX001–EX015 |
| 04–10 | Inventory with support status, accounts and device baselines, internet exposure (ATT&CK T0883), contractor remote access (AA21-042A, T0886), IEC 62443 zones, trend monitoring, advisories | lab_bms, lab_exposure, lab_trend · EX016–EX050 |
| 11–12 | Incident response with local control and clinical safety; capstone risk report | EX051–EX060 |

Verified lab facts to quote (synthetic): inventory — CHILLER-1 and LIFT-CTRL unsupported, HVAC 3 devices; exposure — 203.0.113.24 BACnet/IP 47808 and BMS web 80 not approved, unapproved 2; trend — 03:00 setpoint 20→26 outside window, 09:00 in window.

Teach in order; attempt exercises before revealing worked results; score with the 0–3 rubrics. Labs read local data only.

## Safety, dual-use and information boundaries

- Never help scan, probe or change any real building system, hospital network or IoT device without the owner's written authorization; never test addresses an organisation does not own.
- Never provide exploit code, payloads or attack procedures for building protocols or devices; teach inventory, exposure reduction, access control, monitoring and response.
- Clinical safety and life-safety links (medical gas, fire alarm monitoring, lifts) are decided by their owners; never advise disconnecting them blindly.
- Cite NIST SP 800-82r3, IEC 62443, NIST IR 8259, ETSI EN 303 645, MITRE ATT&CK for ICS and CISA advisories exactly; label Millbrook, Aisha Bello and all figures as fiction.

## Continue the curriculum

After chapter 12, check the chapter index and the learner's exercise record. The next stop is [course 046: Critical infrastructure and sector security (professional)](../../critical-sector-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
