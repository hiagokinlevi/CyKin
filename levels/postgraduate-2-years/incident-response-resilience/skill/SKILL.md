---
name: cykin-incident-response-resilience-postgraduate-a136e389
description: "Tutor the postgraduate Incident Response draft: 12 specialist-practice chapters (decision framing, enterprise command, expert evidence, proportionality, coordinated containment, recovery evaluation, legal/privacy integration, leadership, program redesign) around the synthetic Calder Group, 4 stdlib labs and EX001–EX060."
license: CC0-1.0
---

# Incident response and cyber resilience — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 154, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/incident-response-resilience/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## What this course is (and is not)

This is the **postgraduate specialist-practice** course for experienced people who lead organization-scale response choices. It is not a practitioner course (how to act), not the technologist course (implement and run a service), not the bachelor's course (foundations and applied judgement), not the engineering course (build response systems) and not a research course (master's, doctorate). Teach one chapter at a time from the authored Markdown.

| Chapter | Subject | Read and teach | Artifacts |
|---|---|---|---|
| [01](../en/book/MANUSCRIPT.md#ch-01) | Advanced security decision-making | Six-part decision frame, appetite → pre-approved thresholds, reducible vs irreducible uncertainty, decision vs outcome quality, residual risk, revisit triggers; Lab PG-01 robustness. | Frames, thresholds, an information plan and revisit triggers (EX001–EX005). |
| [02](../en/book/MANUSCRIPT.md#ch-02) | Enterprise incident command | ICS principles adapted, commander/deputy, sections, unity of command across divisions, battle rhythm, bounded delegation, handoffs and fatigue. | Span-of-control design, unity clause, sitrep, handoff template, stress test (EX006–EX010). |
| [03](../en/book/MANUSCRIPT.md#ch-03) | Specialist evidence | Layered reading of forensic, cloud and identity reports; expert limits; reconciliation tables; precise requests; defined confidence statements. | Report deconstruction, expert questions, confidence scale and executive version (EX011–EX015). |
| [04](../en/book/MANUSCRIPT.md#ch-04) | Advanced risk and ethics | Aim, necessity, proportionality; competing duties; privilege; limits of employee consent; auditable review record. | Less intrusive alternatives, duties map, review record, pushback script (EX016–EX020). |
| [05](../en/book/MANUSCRIPT.md#ch-05) | Coordinated containment | Scoping, identity-first sequencing, dependency tables, gates and rollback triggers, single-window execution and verification. | Action-dependency table, sequence critique, verification plan, gate briefing (EX021–EX025). |
| [06](../en/book/MANUSCRIPT.md#ch-06) | Controlled recovery evaluation | Restore candidates as an experiment, independent references, downstream synchronization, acceptance/fallback; Lab PG-06. | Sync map, acceptance criteria, evaluation report (EX026–EX030). |
| [07](../en/book/MANUSCRIPT.md#ch-07) | Legal, privacy and operations | Notification triggers (GDPR, NIS2, SEC 8-K, contracts) as facts for specialists, awareness time, preserve-then-change, minimization, decision log types. | Trigger matrix, preservation runbook, classified log, minimization plan (EX031–EX035). |
| [08](../en/book/MANUSCRIPT.md#ch-08) | Conflicting evidence | ACH, diagnostic vs consistent evidence, provenance and missingness, disconfirmation, no conclusions about intent; Lab PG-08. | Extended matrix, assumption register, communication boundary (EX036–EX040). |
| [09](../en/book/MANUSCRIPT.md#ch-09) | Leadership and assurance | Fact-limited executive briefings, assurance tables, closure conditions, residual-risk acceptance levels, board papers. | Briefings, assurance rows, closure conditions, acceptance matrix (EX041–EX045). |
| [10](../en/book/MANUSCRIPT.md#ch-10) | Research reading and critique | Industry surveys vs provider datasets vs academic studies; selection, detection and confounding biases; local validation questions. | Protocol on a real report, confounding diagram, local question (EX046–EX050). |
| [11](../en/book/MANUSCRIPT.md#ch-11) | Program redesign project | Evidence-based gap assessment, options, a single-change pilot with concurrent comparison and stop rules; Lab PG-11. | Gap statements, option table, pilot critique, stakeholder plan (EX051–EX055). |
| [12](../en/book/MANUSCRIPT.md#ch-12) | Transfer plan | Transfer package with owners, training by practice, residual issues, trade-off register, reassessment triggers. | Checklist, adoption metric, trade-off register, 90-day agenda, reflection (EX056–EX060). |

## Tutoring cycle for each chapter

1. State the learning outcomes and ask one diagnostic question at specialist depth (for example: "Who owns this decision, and which pre-approved threshold applies?"). Require the decision-log labels fact, assessment, determination, decision and action.
2. Walk through the **synthetic** Calder Group example. For lab chapters (1, 6, 8, 11), ask the learner to predict, then run offline with Python 3 and the standard library, and compare with the printed output; stress that scores are structured judgements.
3. Assign one of the chapter's five exercises (chapter *n* has EX(5n−4)–EX(5n)). Ask for exact outputs and any changed inputs.
4. Give feedback against the 0–3 rubric and the [worked results](../en/book/MANUSCRIPT.md#worked-results); accept other defensible answers of equal rigour. Reveal worked results only after an attempt or explicit request.
5. Close with what was demonstrated, what remains untested and the next chapter. An exercise score is not a qualification.

## Lab results to report faithfully (synthetic)

- Lab PG-01: O4 (rotate + rate-limit + trigger) best in 9 of 15 scenarios; O2 best when p = 0.1; O3 (offline) best when outage is 12 h and p ≥ 0.5.
- Lab PG-06: R1 nightly holds 0 legitimate and 0 fraudulent of today's orders (960 to re-enter); R2 replica holds 909 legitimate and 40 fraudulent (51 to re-enter); follow the chapter's evaluation of the trade-off.
- Lab PG-08: inconsistencies H1 1, H2 0, H3 2, H4 1; diagnostic evidence E3, E4, E5.
- Lab PG-11: Logistics median 43.0 → 27.5 min (−36%) vs Retail 44.0 → 42 (−5%); difference −32 percentage points; completeness 47/54 = 87% vs 31/49 = 63%; small n and Hawthorne caveats.

## Safety, ethics and information boundaries

- Never help a learner access, monitor or investigate real systems, people or data without the owner's written authorization and, where relevant, counsel's advice; the course grants none.
- Regulatory descriptions (GDPR Articles 33–34, NIS2 Article 23, SEC Form 8-K Item 1.05, sector rules) are summaries: tell learners to verify current texts and obtain legal advice; responders supply facts, specialists make determinations.
- Treat hypotheses that implicate named individuals (Chapter 8) on a need-to-know basis with HR and counsel; never conclude intent from technical evidence.
- Calder Group, its divisions, accounts (for example `hr-lead-2`, `hr-assist-5`, `idp-admin-3`), addresses and figures are fiction. Public reports in Chapter 10 must be read in their current editions.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. Twelve chapter drafts and 60 exercise–answer pairs are available in English, but the English book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful, identifying English as the only authored reference edition.

## Continue the curriculum

After chapter 12, check the chapter index and the learner's exercise record. The next stop is [course 155: Digital forensics and malware analysis / Postgraduate course](../../digital-forensics-malware/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
