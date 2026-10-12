---
name: cyberabc-threat-intelligence-osint-technologist-73ec917a
description: "Teach the three-year technologist threat intelligence and OSINT course: thirty subjects following a synthetic municipal IT work-study student, with stdlib labs on synthetic data, ethical OSINT and TLP 2.0 handling."
license: CC0-1.0
---

# Threat intelligence and OSINT — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 087, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/threat-intelligence-osint/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Thirty-subject teaching route

This is the three-year **technologist course** for threat intelligence and OSINT. The book follows synthetic work-study student **Lena Park** in the security team of **Corvale Municipal Services (CMS)**, a fictional city IT service that belongs to the fictional **Municipal Cyber Exchange (MCX)**, from foundations to a capstone indicator pipeline.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–09 | Computing, networks, programming, data models, security literacy, operating systems, identity, architecture, evidence | lab_defang, lab_stix · EX001–EX027 |
| 10–23 | CTI orientation, assets, data flows, risk scenarios, methods, guided lab, pivoting, tooling, controls, monitoring, troubleshooting, integration, automation, evaluation | lab_dedupe, lab_match, lab_expiry · EX028–EX069 |
| 24–30 | Applied research, team studio, handoff, deployment, field practice, capstone build and assessment | EX070–EX090 |

Verified lab facts (synthetic): refanging gives two domains and one IPv4, while 203.0.113.300 and "notes" are invalid; the bundle has 1 indicator, 1 attack-pattern (T1566) and 2 relationships, one dangling to malware--z; 6 raw indicators become 3 unique with provenance kept; ws-114 has 1 hit and ws-207 has 2, and pay-portal.example.org is not matched; expiry flags the 42-day address and the 113-day domain.

## Safety, privacy and information boundaries

- Never help collect personal data without lawful basis, break terms of service, use fake accounts, uncover redacted registrants, or contact, scan or download from adversary infrastructure.
- Enforce FIRST TLP 2.0; fail closed on unknown labels; never automate outward AMBER or RED sharing; use RFC 5737 addresses and `.example` domains in teaching.
- Cite ATT&CK, STIX/TAXII 2.1, the Diamond Model, Hutchins et al., NIST SP 800-150, TLP 2.0 and ICD 203 exactly; label CMS, MCX and Lena Park as fiction.

## Continue the curriculum

After chapter 30, the next stop is [course 088: Authorized offensive security and red team / Technologist course](../../offensive-security-red-team/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
