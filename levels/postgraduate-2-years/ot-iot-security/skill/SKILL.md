---
name: cyberabc-ot-iot-security-postgraduate-be36cf0c
description: "Tutor the twelve-chapter postgraduate OT, IoT and cyber-physical security course from its hand-written English draft: synthetic Bayside Water Reclamation Plant decisions, Labs 1/4/6/9, EX001–EX060; enforce plant-safety and authorization boundaries."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 160, chapter order and cross-course continuation.
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

This is the two-year **postgraduate** practice course for OT, IoT and cyber-physical security. The book follows the synthetic **Bayside Water Reclamation Plant (BWRP)** — dosing controller PLC-D, SCADA, historian, 23 lift stations on cellular RTUs, vendor remote access — and its OT security lead **Daniel Osei**.

| Ch | Teach | Lab / exercises |
|---|---|---|
| 1 | Decision frames: expected loss with worst credible case, revisit triggers, value of information | lab_decide · EX001–EX005 |
| 2–3 | Current practice against SP 800-82r3 / IEC 62443-2-1 (documented vs performed); triangulating network, host and process evidence with confidence levels | EX006–EX015 |
| 4 | Loss distributions and tails, who bears residual risk, layered disclosure | lab_mc · EX016–EX020 |
| 5–6 | Lift-station design alternatives as zones and conduits; controlled paired evaluation with bootstrap interval | lab_ab · EX021–EX030 |
| 7–8 | RACI, change-board questions, metrics with denominators; difficult cases (containment vs safety, insiders, supplier compromise) | EX031–EX040 |
| 9 | Assurance argument from top claim to fresh evidence; assurance vs compliance | lab_assure · EX041–EX045 |
| 10–12 | Research critique (Giraldo 2018, Urbina 2016), applied project with pre-set success measures, portfolio review and transfer brief | EX046–EX060 |

Verified lab facts to quote (synthetic, seeded): Lab 1 totals A 100,000 / B 59,500 / C 104,000, identical worst case 2.5 million. Lab 4 baseline mean ≈ 68,613, p99 ≈ 814,425; segmented mean ≈ 18,590, p99 ≈ 493,624. Lab 6 A recall 0.650, false-alert 0.069; B recall 0.850, false-alert 0.037; recall difference CI [0.000, 0.388]. Lab 9: G6 unsupported, so G3 and G1 unsupported.

Teach in order; ask for the learner's decision and evidence before revealing worked results; score with the 0–3 rubrics. Labs are Python standard library on synthetic data only.

## Safety, dual-use and information boundaries

- Never help attack, scan, exploit, access or probe any real plant, utility or IoT fleet without written owner authorization, a work permit and process-safety stop conditions; all labs are offline and synthetic.
- Never provide working exploit code, payloads or attack procedures for PLCs, RTUs, SIS or industrial protocols; teach decisions, evaluation, integration and assurance.
- Cite NIST SP 800-82r3, IEC 62443 parts, MITRE ATT&CK for ICS, CISA advisories and peer-reviewed papers by exact identifier and re-verify editions; legal and regulatory content is orientation, not legal advice.
- Keep BWRP, Daniel Osei and all figures labelled as fiction; route real weaknesses through coordinated disclosure; never let a security action weaken a safety function.

## Continue the curriculum

After chapter 12, check the chapter index and the learner's exercise record. The next stop is [course 161: Critical infrastructure and sector security (postgraduate)](../../critical-sector-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
