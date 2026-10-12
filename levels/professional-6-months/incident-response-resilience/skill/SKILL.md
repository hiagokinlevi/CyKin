---
name: cyberabc-incident-response-resilience-professional-19e11913
description: "Tutor the professional Incident Response course through its five authored English subjects, CTN case, 25 exercises and answers; preserve case time, evidence and authority boundaries."
license: CC0-1.0
---

# Incident response and cyber resilience — Professional course skill

Use this **one skill for the whole 6 months course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/incident-response-resilience/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters and exercises actually present; review is pending.
## Authored five-subject route

This six-month professional course has **12 planned subjects**. The English principal book currently authors subjects 1–5 and EX001–EX025 with answers; subjects 6–12 remain outlines. Teach only the authored subject as published text; identify an outline or your own explanation as such.

| Subject | Read and teach | Learner artifact |
|---|---|---|
| 1. Readiness | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): service dependencies, owner gaps, falsifiable evidence-readiness test. | Source/owner map and bounded rehearsal contract; EX001–EX005. |
| 2. Authority | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): role-specific decisions and approval-versus-execution. | Scoped action request with blank unapproved fields; EX006–EX010. |
| 3. Triage | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): source times, provisional priority and review triggers. | Four-source intake and P2 rationale; EX011–EX015. |
| 4. Preservation | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): bounded export, receipts, checksum limits and screenshot time. | C09/C10 evidence package and local V4 hash result; EX016–EX020. |
| 5. Investigation | [Chapter 5](../en/book/MANUSCRIPT.md#ch-05): source-traceable timeline and H1/H2/H3 discriminators. | 09:26 supervisor handoff and next-request plan; EX021–EX025. |

## Tutoring and feedback

1. Check the selected chapter's learning outcomes and ask a diagnostic question. Teach at a supervised practitioner depth: require a named service, source, custodian, decision owner and verification method, not a generic list of response phases.
2. Release only the fictional CTN cards available at that chapter checkpoint. Chapter 1 has C01; Chapter 2 adds C02 at 09:04; Chapter 3 receives C03–C05 at 09:09, C06 at 09:10, C07 at 09:12 and C08 at 09:14; Chapter 4 adds C09 and C10; Chapter 5 adds C11 at 09:24 and C12 at 09:26. The V2 and V4 fixtures are separate variants, not main-case observations.
3. Ask the learner to produce one numbered exercise artifact before showing its worked answer. Score against that exercise's 0–2 rule. Accept an alternative conclusion only if it cites the released sources, uncertainty and authority. Then show the matching answer in the [book appendix](../en/book/MANUSCRIPT.md#worked-answers) and explain the difference.
4. Carry the previous artifact into the next subject: readiness gaps → action charter → timed intake → source receipts → hypothesis and handoff. Ask which observation would falsify each inference. End with the next authorized, bounded question, never with an invented execution result.

## Case and authority boundaries

- C04's 08:54 device reading is four minutes slow, so its normalized estimate is 08:58 UTC. C10's 11:21 UTC+02:00 display converts conditionally to 09:21 UTC; its case receipt is 09:22. Keep raw, normalized, ingestion and release times distinct.
- C03/C09 report `s-77`; C09 associates a client with `runner-03`; C05/C12 report `q-144` and a self-reported `batch-17` tag. No supplied field directly joins `s-77` to `q-144` or attributes a human. C06's visible approval excludes S42, but C11's possible addendum is unverified.
- The V4 checksum checks only the invented 34-byte local payload. It is not C09's missing source-object digest. The C10 screenshot is not authoritative slot state. A P2 priority is a local teaching decision, not a confirmed compromise.
- Use only synthetic, sanitized or genuinely authorized environments. Never direct a learner to alter a real tenant, disable a shared account, bulk-export records or notify users from this lesson alone. The book and this skill do not grant operational permission.

## Editorial and language state

Use the [course progress table](../../../../COURSE_WRITING_PROGRESS.md), [source audit](../../../../SOURCE_AUDIT.md) and [book standard](../../../../BOOK_STANDARD.md). Five chapter drafts and 25 exercise-answer pairs are available in English; the 12-chapter, 60-exercise book is incomplete and has not passed 300 A4 pages or independent review. Other language folders are working outlines until translated and reviewed after the full English set.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
