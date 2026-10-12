---
name: cyberabc-security-operations-blue-team-masters-0a10392d
description: "Master's course (2 years)"
license: CC0-1.0
---

# Security operations and blue team — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 176, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-operations-blue-team/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the two-year **master's course** for security operations and blue team. The book follows synthetic master's student **Tariq Haddad** of the fictional **Ashworth Institute of Technology**, supervised by **Dr. Ingrid Solberg**, through one dissertation in the corporate SOC of the fictional **Pelham Water Utility**: does adding reviewed allow-lists to the noisiest detection rules cut alert volume without suppressing attacks?

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–3 | Research question and literature method, advanced seminar, study design and ethics | EX001–EX020 |
| 4–6 | Competing explanations, proposal and pilot, data collection and analysis | lab_did.py (4), lab_strata.py (5), lab_allow.py (6); EX021–EX038 |
| 7–8 | Dissertation writing and limitations, independent review and defense | EX039–EX050 |

Verified lab facts (synthetic): tuned −173.8, control −37.2, difference-in-differences −136.5 alerts/week; stratified sample 20/45/135 of 200; allow-list replay 6 of 8 suppressed, one injected attack (PATCH-SRV2, svc_patch) suppressed.

## Safety, privacy and information boundaries

- Synthetic telemetry only; no exploit code, payloads, attack procedures or evasion guidance.
- Standard-library labs; purple-team activity only under signed authorisation, excluding OT networks.
- Pseudonymise at source; withhold detection details that would aid evasion.

## Continue the curriculum

After chapter 8, the next stop is [course 177: Incident response and cyber resilience / Master's course](../../incident-response-resilience/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
