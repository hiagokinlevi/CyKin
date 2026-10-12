---
name: cyberabc-threat-intelligence-osint-engineering-23944a13
description: "Guide a learner through the engineering course in threat intelligence and OSINT: engineering a CTI platform with STIX/TAXII 2.1, TLP-gated dissemination, measurement, reliability, OT safety interlocks and ethical OSINT on synthetic data."
license: CC0-1.0
---

# Threat intelligence and OSINT — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 133, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/threat-intelligence-osint/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-subject teaching route

This is the five-year **engineering course** for threat intelligence and OSINT. The book follows synthetic engineering student **Kofi Mensah** as he helps **Brightwater Energy Networks (BEN)** engineer **Lantern**, an in-house CTI platform with TAXII 2.1 ingestion, STIX 2.1 storage, TLP-gated dissemination and interlocked OT recommendations.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–19 | Mathematics, computing and security foundations applied to intelligence workloads | lab_graph, lab_decay, lab_bayes, lab_dedupe · EX001–EX057 |
| 20–41 | CTI requirements, models, threat/failure analysis, methods, studios, controls, implementation, measurement, reliability, safety, integration, scale, operations, validation, maintainability, optimisation | lab_tlp, lab_feedeval, lab_avail, lab_queue · EX058–EX123 |
| 42–50 | Applied research, practice, capstone, independent review, failure trial, evidence dossier, thesis, defence | lab_drill · EX124–EX150 |

Verified lab facts (synthetic): decay crosses floor 30 after 22.2 days; precision 0.045 at prevalence 0.001; 7 raw indicators → 4 unique; TLP gate blocks GREEN→public and unknown labels; feed precision 0.50 / recall 0.60; serial availability 0.9732 → 0.9926 with redundant enrichment; drill D2 missed RTO, D3 missed RPO.

## Safety, privacy and information boundaries

- Never help collect personal data without lawful basis, evade terms of service, deanonymise people, probe partner or adversary systems, or automate OT actions without human approval.
- Enforce FIRST TLP 2.0 and partner agreements; fail closed on unknown labels.
- Cite ATT&CK (technique IDs), STIX/TAXII 2.1, the Diamond Model, Hutchins et al., NIST SP 800-150, TLP 2.0 and ICD 203 exactly; label BEN, Lantern and Kofi Mensah as fiction.

## Continue the curriculum

After chapter 50, the next stop is [course 134: Authorized offensive security and red team / Engineering course](../../offensive-security-red-team/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
