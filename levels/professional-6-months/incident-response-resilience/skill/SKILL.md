---
name: cyberabc-incident-response-resilience-professional-19e11913
description: "Tutor the professional Incident Response course through ten authored English subjects, CTN case, 50 exercises and answers; preserve case time, evidence and authority boundaries."
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

## Authored ten-subject route

This six-month professional course has **12 planned subjects**. The English principal book currently authors subjects 1–10 and EX001–EX050 with answers; subjects 11–12 remain outlines. Teach only authored subjects as published text; identify an outline or your own explanation as such.

| Subject | Read and teach | Learner artifact |
|---|---|---|
| 1. Readiness | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): service dependencies, owner gaps, falsifiable evidence-readiness test. | Source/owner map and bounded rehearsal contract; EX001–EX005. |
| 2. Authority | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): role-specific decisions and approval-versus-execution. | Scoped action request with blank unapproved fields; EX006–EX010. |
| 3. Triage | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): source times, provisional priority and review triggers. | Four-source intake and P2 rationale; EX011–EX015. |
| 4. Preservation | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): bounded export, receipts, checksum limits and screenshot time. | C09/C10 evidence package and local V4 hash result; EX016–EX020. |
| 5. Investigation | [Chapter 5](../en/book/MANUSCRIPT.md#ch-05): source-traceable timeline and H1/H2/H3 discriminators. | 09:26 supervisor handoff and next-request plan; EX021–EX025. |
| 6. Containment | [Chapter 6](../en/book/MANUSCRIPT.md#ch-06): option comparison, bounded approval, receipt and effect. | C17/C18/C19 action-state record and V6 route-coverage check; EX026–EX030. |
| 7. Eradication | [Chapter 7](../en/book/MANUSCRIPT.md#ch-07): validated task-to-request join, second identity path, positive/negative checks. | C20–C24 cause-to-fix contract and read-only manifest comparison; EX031–EX035. |
| 8. Recovery | [Chapter 8](../en/book/MANUSCRIPT.md#ch-08): data-target comparison, isolated no-go/pass, production and owner acceptance. | C25–C30 recovery gate and in-memory value diff; EX036–EX040. |
| 9. Communications | [Chapter 9](../en/book/MANUSCRIPT.md#ch-09): service versus privacy status, message approval and versioning. | C31–C33 internal/public drafts and privacy referral; EX041–EX045. |
| 10. Playbook quality | [Chapter 10](../en/book/MANUSCRIPT.md#ch-10): repair P0, walk P1 and score six design criteria. | Main-case, V10 and V10b branch artifacts; EX046–EX050. |

## Tutoring and feedback

1. Check the selected chapter's learning outcomes and ask a diagnostic question. Teach at a supervised practitioner depth: require a named service, source, custodian, decision owner and verification method, not a generic list of response phases.
2. Release only the fictional CTN cards available at that chapter checkpoint. Chapters 1–5 receive C01–C12 in book order; Chapter 6 adds C13–C19, with C16 tolerance distinct from C17 approval; Chapter 7 adds C20–C24 and a newly approved hold extension C21; Chapter 8 adds C25–C30; Chapter 9 adds C31–C33. Chapter 10 uses the case and separate P0/P1 playbook specimens. V2, V4, V6, V9, V10 and V10b are variants, never main-case observations.
3. Ask the learner to produce one numbered exercise artifact before showing its worked answer. Score against that exercise's 0–2 rule. Accept an alternative conclusion only if it cites the released sources, uncertainty and authority. Then show the matching answer in the [book appendix](../en/book/MANUSCRIPT.md#worked-answers) and explain the difference.
4. Carry the previous artifact into the next subject: readiness → authority → timed intake → source receipts → hypotheses → scoped hold → cause-to-fix → recovery gate → audience-specific status → playbook. Ask which observation would falsify each inference. End with the next authorized, bounded question, never with an invented execution result.

## Case and authority boundaries

- C04's 08:54 device reading is four minutes slow, so its normalized estimate is 08:58 UTC. C10's 11:21 UTC+02:00 display converts conditionally to 09:21 UTC; its case receipt is 09:22. Keep raw, normalized, ingestion and release times distinct.
- C03/C09 report `s-77`; C09 associates a client with `runner-03`; C05/C12 report `q-144` and a self-reported `batch-17` tag. No supplied field directly joins `s-77` to `q-144` or attributes a human. C14 excludes `q-144` from the approved batch, C15 finds no S42 addendum in the official ledger, and C20 validates the different `sync-override` task-to-request link. Mechanism is stronger than actor attribution.
- C16 is tolerance only. C17 approves a S42 hold to 09:47; C18 reports execution; C19 checks one route. C21 separately extends the hold to 10:07. C24 reports the task disabled, with a short observation window; C25 later addresses one identity method and session. Do not mark every path eradicated.
- C26's intact snapshot would regress approved S40/S41 changes. C27 fails the preannounced alternate-route audit gate; C28 passes an isolated retest; C29 is a separate production action; C30 is a limited owner acceptance after 15 minutes. C31–C33 do not prove external delivery or no exposure. P0/P1 scores assess playbook text, not real-world effectiveness.
- The V4 checksum checks only the invented 34-byte local payload. It is not C09's missing source-object digest. The C10 screenshot is not authoritative slot state. A P2 priority is a local teaching decision, not a confirmed compromise.
- Use only synthetic, sanitized or genuinely authorized environments. Never direct a learner to alter a real tenant, disable a shared account, bulk-export records or notify users from this lesson alone. The book and this skill do not grant operational permission.

## Editorial and language state

Use the [course progress table](../../../../COURSE_WRITING_PROGRESS.md), [source audit](../../../../SOURCE_AUDIT.md) and [book standard](../../../../BOOK_STANDARD.md). Ten chapter drafts and 50 exercise-answer pairs are available in English; the 12-chapter, 60-exercise book is incomplete and has not passed 300 A4 pages or independent review. Other language folders are working outlines until translated and reviewed after the full English set.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
