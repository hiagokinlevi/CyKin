---
name: cykin-threat-intelligence-osint-bachelor-10ac083a
description: "Teach the four-year bachelor's threat intelligence and OSINT course: forty subjects following a synthetic hospital-trust intern, with stdlib labs on synthetic data, ethical OSINT and TLP 2.0 handling."
license: CC0-1.0
---

# Threat intelligence and OSINT — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 110, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/threat-intelligence-osint/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-subject teaching route

This is the four-year **bachelor's course** for threat intelligence and OSINT. The book follows synthetic intern **Amara Diallo** at **Halden County Health Trust (HCHT)**, a fictional hospital group that belongs to the fictional **Health Sector Sharing Circle (HSSC)**, from foundations through a lookalike-domain early-warning capstone.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–18 | Reasoning, computing, programming, writing, security literacy, networks, data, ethics, OS, probability, identity, privacy, evidence, architecture, cryptography, research methods | lab_csvfeed, lab_sql, lab_wep, lab_redact · EX001–EX054 |
| 19–32 | CTI scope and theory, cases, system models, sources, ATT&CK coding, controls, Laboratory I, Admiralty grading, verification, failure analysis, operations, Laboratory II (STIX by hand), kill-chain timelines, interfaces | lab_freq, lab_admiralty, lab_phases · EX055–EX096 |
| 33–40 | Research methods II, comparative project, capstone proposal, field practice, evidence review seminar, capstone implementation, evaluation, thesis | EX097–EX120 |

Verified lab facts (synthetic): feed validation accepts 3 and rejects 2; SQL returns files.example TLP:CLEAR and portal-login.example TLP:GREEN with 2 stale; C2 "very likely" at 60% is inconsistent and "probable" is off-scale; redaction keeps the adversary address; T1566 and T1486 lead at 3/5; Admiralty I-1 B2 act, I-3 A5 hold, I-5 F6; delivery to C2 in 32 minutes.

## Safety, privacy and information boundaries

- Never help collect personal data without lawful basis, break terms of service, use fake personas, deanonymise people, or contact or probe adversary infrastructure.
- Enforce FIRST TLP 2.0 (CLEAR, GREEN, AMBER, AMBER+STRICT, RED) and never route patient data through intelligence channels.
- Cite ATT&CK, STIX/TAXII 2.1, the Diamond Model, Hutchins et al., NIST SP 800-150, TLP 2.0 and ICD 203 exactly; label HCHT, HSSC and Amara Diallo as fiction.

## Continue the curriculum

After chapter 40, the next stop is [course 111: Authorized offensive security and red team / Bachelor's course](../../offensive-security-red-team/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
