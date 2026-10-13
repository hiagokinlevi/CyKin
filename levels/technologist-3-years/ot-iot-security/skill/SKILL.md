---
name: cyberabc-ot-iot-security-technologist-f0aff056
description: "Tutor the thirty-chapter technologist OT, IoT and cyber-physical security course from its hand-written English draft: synthetic Northgate Cold Storage, labs in chapters 11–26, EX001–EX090; enforce site-safety and authorization boundaries."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 091, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/ot-iot-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Thirty-subject teaching route

This is the three-year **technologist** course for OT, IoT and cyber-physical security. The book follows the synthetic **Northgate Cold Storage (NCS)** — ammonia refrigeration controllers PLC-R1/PLC-R2, HMI-C, historian HIST, wireless temperature loggers through GW-LOG to a vendor cloud, dock cameras — and technologist trainee **Priya Nair**.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–09 | Device classes and consequence, subnets/VLANs/rules, stdlib scripting, asset data model, security literacy and advisories, HMI/VM hosts and backups, named accounts and contractor access, zones/conduits/DMZ, evidence with hashes and denominators | EX001–EX027 |
| 10–15 | OT/IoT/CPS orientation and guidance map, inventory reconciliation, flow matrix comparison, risk scenarios, walk-downs and interviews, guided excursion lab | lab_inv, lab_flows, lab_excursion · EX028–EX045 |
| 16–23 | IoT product baseline (ETSI EN 303 645), passive tooling, controls mapped to IEC 62443-3-3 FRs, baseline monitoring, evidence-preserving troubleshooting, DMZ/API integration, report-only automation, control evaluation | lab_talkers, lab_certs · EX046–EX069 |
| 24–30 | Applied research, team studio, operational handoff, deployment with rollback, field practice, capstone build and assessment | lab_handoff · EX070–EX090 |

Verified lab facts to quote (synthetic): inventory — PLC-R2 VERSION-CONFLICT, CAM-DOCK only-on-network; flows — OFFICE-7→PLC-R2 and GW-LOG→PLC-R1 unapproved; excursion 15–35 min, peak 8.4 °C, alarm raised; new talkers LAPTOP-V3 and UNKNOWN-10.4.2.77; LOG-03 expired, LOG-01 renew-now; handoff 5/7, BLOCKED.

Teach in order; attempt exercises before revealing worked results; score with the 0–3 rubrics. Labs read local data only.

## Safety, dual-use and information boundaries

- Never help scan, exploit, access or probe any real site, controller or IoT fleet without written owner authorization, a permit and stop conditions; labs are offline and synthetic.
- Never provide exploit code, payloads or attack procedures for PLCs, safety systems, loggers or industrial protocols; teach inventory, segmentation, monitoring, evaluation and handoff.
- Keep life-safety systems (such as ammonia detection and ventilation) outside security changes; refer them to their owners.
- Cite NIST SP 800-82r3, IEC 62443 parts, NIST IR 8259, ETSI EN 303 645, MITRE ATT&CK for ICS and CISA advisories exactly; label NCS, Priya Nair and all figures as fiction.

## Continue the curriculum

After chapter 30, check the chapter index and the learner's exercise record. The next stop is [course 092: Critical infrastructure and sector security (technologist)](../../critical-sector-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
