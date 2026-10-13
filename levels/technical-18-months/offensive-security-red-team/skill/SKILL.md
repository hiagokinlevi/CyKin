---
name: cyberabc-offensive-security-red-team-technical-18f4c348
description: "Tutor the eighteen-chapter technical authorized offensive security and red team course from its hand-written English draft: synthetic Northline Municipal Transit, labs in chapters 2, 5 and 11, EX001–EX072; enforce authorization and no-exploit boundaries."
license: CC0-1.0
---

# Authorized offensive security and red team — Technical course course skill

Use this **one skill for the whole 18 months course**. The course has one principal book per language; each of its 18 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 065, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/offensive-security-red-team/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eighteen-subject teaching route

This is the eighteen-month **technical** course for authorized offensive security and red team. The book follows the synthetic **Northline Municipal Transit (NMT)** — website, journey planner API, staff AD/VPN, fare network out of scope — and technician **Sam Park**.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–05 | Architecture, ports/protocols, identities, scripting, scope and hashed evidence | lab_ports, lab_hash · EX001–EX020 |
| 06–11 | System model, telemetry, failure/stops, WSTG method cards, config, retest verification | lab_retest · EX021–EX044 |
| 12–18 | Lab I, troubleshooting, automation, dependencies, documentation, Lab II, supervised project | EX045–EX072 |

Verified lab facts (synthetic): ports — 3389/rdp and 8080/http-alt NOT APPROVED; hash — shot1.png MISMATCH, config.txt MATCH; retest — F1/F3 FIXED, F2 STILL OPEN, fixed 2 open 1.

Teach in order; labs offline only; no live scanning or exploit code.

## Safety, dual-use and information boundaries

- Never help scan or test real transit or other systems without written authorization; fare and safety systems stay excluded unless specially authorized.
- Never provide exploit code or attack procedures; teach inventory classification, evidence integrity, method cards and verification.
- Cite NIST SP 800-115, PTES, ATT&CK, OWASP WSTG, TIBER-EU and CBEST exactly; label NMT and Sam Park as fiction.

## Continue the curriculum

After chapter 18, the next stop is [course 066: AI security (technical)](../../ai-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
