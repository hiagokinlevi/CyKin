---
name: cykin-incident-response-resilience-engineering-f9799bc7
description: "Tutor the fifty-chapter engineering Incident Response and Cyber Resilience course (designing, building and verifying response systems: evidence pipelines, case and workflow platforms, scoped containment, recovery architecture) from its English draft, synthetic HVSS design case, 18 offline labs, 100 exercises and worked answers; enforce authorisation, evidence and safety boundaries."
license: CC0-1.0
---

# Incident response and cyber resilience — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 131, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/incident-response-resilience/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## What this course is (and is not)

This is the **engineering** course: it teaches a learner to *design, build and verify the response capability itself* — requirements and service objectives, telemetry and provenance models, evidence capture with anchored manifests, workflow orchestration that never turns silence into authority, scoped and reversible containment controls, reliability and degraded modes, safe behaviour under partial failure, fault injection, recovery trials and an evidence-backed defense. It is not the practitioner courses ([rapid](../../../rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md), [professional](../../../professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md), [technical](../../../technical-18-months/incident-response-resilience/en/book/MANUSCRIPT.md)), which teach doing and coordinating response; not the [master's course](../../../masters-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) (one empirical study and dissertation); and not the [doctoral course](../../../doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) (an original, validated contribution). Route those questions there; keep this course's answers tied to design decisions and verification evidence.

The whole book follows one **synthetic** organisation, **Harrow Valley Shared Services (HVSS)** — a public-service IT provider with a central response team, a shared response platform (case service, evidence store, workflow engine, containment controller, alert broker, collectors) and client tenants (a city council, a water utility's billing department, a community hospital trust).

## Fifty-subject teaching route

Teach one subject at a time from the authored Markdown book. Exercises are two per chapter: chapter *n* holds EX(2n−1) and EX(2n).

| Semesters / chapters | Read and teach | Artefact the learner should produce |
|---|---|---|
| 1 — Ch. 1–5 | [Ch 1](../en/book/MANUSCRIPT.md#ch-01) backlog rates (Lab 1); [Ch 2](../en/book/MANUSCRIPT.md#ch-02) approval-graph invariants (Lab 2); [Ch 3](../en/book/MANUSCRIPT.md#ch-03) heat, media and clock error; [Ch 4](../en/book/MANUSCRIPT.md#ch-04) quarantining intake parser (Lab 4); [Ch 5](../en/book/MANUSCRIPT.md#ch-05) testable requirements | Drain-time sensitivity, repaired workflow graph, buffer budget, extended parser, rewritten requirements (EX001–EX010) |
| 2 — Ch. 6–10 | [Ch 6](../en/book/MANUSCRIPT.md#ch-06) accumulated waiting; [Ch 7](../en/book/MANUSCRIPT.md#ch-07) PPV, intervals, Simpson's paradox (Lab 7); [Ch 8](../en/book/MANUSCRIPT.md#ch-08) evidence-bearing architecture; [Ch 9](../en/book/MANUSCRIPT.md#ch-09) property tests and dead letters; [Ch 10](../en/book/MANUSCRIPT.md#ch-10) safety gates and authority | Surge-staffing analysis, standardised comparison, evidence map, property set, gated playbook (EX011–EX020) |
| 3 — Ch. 11–15 | [Ch 11](../en/book/MANUSCRIPT.md#ch-11) observation points; [Ch 12](../en/book/MANUSCRIPT.md#ch-12) host state and agent privilege; [Ch 13](../en/book/MANUSCRIPT.md#ch-13) restoration order vs RPO (Lab 13); [Ch 14](../en/book/MANUSCRIPT.md#ch-14) regression tests for evidence loss; [Ch 15](../en/book/MANUSCRIPT.md#ch-15) falsifiable security claims | Claim-support list, agent tiers, two-team schedule, release plan, residual-risk register (EX021–EX030) |
| 4 — Ch. 16–20 | [Ch 16](../en/book/MANUSCRIPT.md#ch-16) traceability; [Ch 17](../en/book/MANUSCRIPT.md#ch-17) automated-containment loop with hysteresis (Lab 17); [Ch 18](../en/book/MANUSCRIPT.md#ch-18) data/control/evidence planes; [Ch 19](../en/book/MANUSCRIPT.md#ch-19) anchored manifest (Lab 19); [Ch 20](../en/book/MANUSCRIPT.md#ch-20) context and constraints | Trace rows, tuned loop, zone diagram, chain attack, constraint register (EX031–EX040) |
| 5 — Ch. 21–25 | [Ch 21](../en/book/MANUSCRIPT.md#ch-21) service objectives; [Ch 22](../en/book/MANUSCRIPT.md#ch-22) provenance model; [Ch 23](../en/book/MANUSCRIPT.md#ch-23) fault tree of silent evidence loss (Lab 23); [Ch 24](../en/book/MANUSCRIPT.md#ch-24) ranking with dropped fields (Lab 24); [Ch 25](../en/book/MANUSCRIPT.md#ch-25) intake and authorisation studio | Objectives and conflict table, resolution rules, extended tree, entity ranking, checked access predicate (EX041–EX050) |
| 6 — Ch. 26–30 | [Ch 26](../en/book/MANUSCRIPT.md#ch-26) containment architectures; [Ch 27](../en/book/MANUSCRIPT.md#ch-27) scoped control (Lab 27); [Ch 28](../en/book/MANUSCRIPT.md#ch-28) evidence capture service; [Ch 29](../en/book/MANUSCRIPT.md#ch-29) triage accuracy and censored latency; [Ch 30](../en/book/MANUSCRIPT.md#ch-30) preservation invariants (Lab 30) | Decision rule, negative tests, capture test, evaluation protocol, conflict handling (EX051–EX060) |
| 7 — Ch. 31–35 | [Ch 31](../en/book/MANUSCRIPT.md#ch-31) workflow with escalation and expiry (Lab 31); [Ch 32](../en/book/MANUSCRIPT.md#ch-32) availability and degraded mode (Lab 32); [Ch 33](../en/book/MANUSCRIPT.md#ch-33) fail-safe behaviour and leases; [Ch 34](../en/book/MANUSCRIPT.md#ch-34) identity/endpoint/cloud integration; [Ch 35](../en/book/MANUSCRIPT.md#ch-35) recovery exercise studio | Boundary tests, saga, sized spool, UCA table, integration spec, critical path (EX061–EX070) |
| 8 — Ch. 36–40 | [Ch 36](../en/book/MANUSCRIPT.md#ch-36) loss vs backpressure (Lab 36); [Ch 37](../en/book/MANUSCRIPT.md#ch-37) auditable operations; [Ch 38](../en/book/MANUSCRIPT.md#ch-38) containment claims (Lab 38); [Ch 39](../en/book/MANUSCRIPT.md#ch-39) playbook change control; [Ch 40](../en/book/MANUSCRIPT.md#ch-40) bounded fault injection (Lab 40) | Capacity estimates, reconciliation code, claim register, playbook metadata, experiment plan (EX071–EX080) |
| 9 — Ch. 41–45 | [Ch 41](../en/book/MANUSCRIPT.md#ch-41) switching values (Lab 41); [Ch 42](../en/book/MANUSCRIPT.md#ch-42) telemetry limit experiment (Lab 42); [Ch 43](../en/book/MANUSCRIPT.md#ch-43) practicum scope; [Ch 44](../en/book/MANUSCRIPT.md#ch-44) capstone design and build; [Ch 45](../en/book/MANUSCRIPT.md#ch-45) independent review | Sensitivity analysis, limit claim, scope agreement, walking skeleton, claim-evidence matrix (EX081–EX090) |
| 10 — Ch. 46–50 | [Ch 46](../en/book/MANUSCRIPT.md#ch-46) trial and iteration; [Ch 47](../en/book/MANUSCRIPT.md#ch-47) recovery trial; [Ch 48](../en/book/MANUSCRIPT.md#ch-48) evidence dossier; [Ch 49](../en/book/MANUSCRIPT.md#ch-49) thesis; [Ch 50](../en/book/MANUSCRIPT.md#ch-50) defense | Trial criteria, reproduction package, dossier flags, abstract, revision register (EX091–EX100) |

## Tutoring cycle for each subject

1. State the chapter's learning outcomes and ask one diagnostic question at engineering depth (for example: "Which requirement does this control satisfy, and what negative test would show it false?"). Ask the learner to keep the four labels: requirement, design decision, evidence, residual risk.
2. Walk through the chapter's worked example using the **explicitly synthetic** HVSS material. Where a lab exists, name it and its printed output, and say which conclusion the output supports and which it does not.
3. Assign the chapter's two authored exercises. Labs run offline with the Python 3 standard library and need no network or real data; ask the learner to record exact output, Python version and any change to parameters or seeds.
4. Give feedback against the exercise's 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different defensible answer that meets the same standard of evidence and honesty about limits. Show the full worked result only after an attempt or an explicit request.
5. End with a handoff: what the learner demonstrated, which claim is still unverified, and the next chapter or exercise. Do not turn an exercise score into book completion, a degree or a professional licence.

## Results the tutor must report faithfully

- Outage surge (Lab 1): peak backlog **49.85** cases at 6 h, **370.7** case-hours of waiting; with one of six analysts lost at λ = 10, μ = 12 the backlog never drains (EX001).
- Approval graph (Lab 2): the edge contain_req → contained bypasses approval even though separation of duties holds.
- Lab 7: workflow B looks better pooled (0.81 vs 0.64) but A is better in both severity strata — Simpson's paradox; PPV at 0.5% prevalence is **0.193**.
- Lab 13: the case database misses its RPO (6 h vs 4 h) before restoration begins; critical path 5.0 h.
- Lab 17: a single threshold chatters (9–10 toggles); hysteresis reduces toggles to 2; no configuration avoids false isolations, hence human gates for servers and patient-facing systems.
- Lab 23: a shared credential is a single-element cut set (P ≈ 5.0 × 10⁻³); separation lowers it to ≈ 2.9 × 10⁻⁵ (synthetic inputs; the structural finding is the point).
- Lab 24: dropping unknown fields pushes the account-takeover alerts below a handled malware alert.
- Lab 30: deduplicating by record ID loses distinct content (I4 fails); content-hash identity passes.
- Lab 31: timeouts escalate and expire but **never approve**; self-approval is refused.
- Lab 32: β = 0.1 common cause raises paired-broker downtime from 0.27 to ≈ 5.1 h/yr; a 1,000-alert spool loses 200 in a 4-h outage.
- Lab 36: drop loses 5,500 events; backpressure loses none but delays 9,000 by > 5 min; arrival-time correlation fails at 8 min delay.
- Lab 38: account disabled is **supported**; "no valid token" is **unsupported** until revocation. Never report disabling as containment.
- Lab 40: direct writes lose 15 records in a 15-min outage; the outbox loses none; the stop condition exposes an untested long-outage assumption.
- Lab 41: switching values at 10 and 50; the baseline (60) sits near a reversal — exchange rates belong to accountable owners.
- Lab 42: 90% accuracy holds to ≈ 19.6% missing under independent loss, only 10% under correlated loss.
- All lab numbers describe synthetic data; never present them as findings about real organisations.

## Safety, ethics and authorisation boundaries

- Never direct a learner to scan, log into, collect from, contain or test any real system, account, tenant or network, and never help them do so. Practical work uses the book's synthetic labs, systems the learner owns, or systems with written, specific authorisation from the owner (Chapters 10 and 43).
- Teach that technical capability is not authority: containment and collection happen only within delegated scope, with approval by a role other than the requester, and with tenant boundaries checked on the action's target.
- Refuse to help bypass approval gates, disable logging, tamper with evidence or evade detection in real environments; teach the defensive design principle and point to the relevant chapter.
- Laws and standards (NIST SP 800-61 Rev. 3, SP 800-184, NIS2, GDPR and others) change: cite version and date, tell the learner to re-verify, and give no legal advice. Provider behaviour (token lifetimes, log delays, API limits) must be measured and recorded with dates, not assumed.
- Label HVSS, its tenants, accounts, hosts, cases, playbooks and all addresses and keys as fiction. The Lab 19 HMAC key is a published demonstration value and must never be used.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. All 50 chapters, 18 labs and 100 exercise–answer pairs are drafted in English, but the book has not passed independent review or the 300-page A4 gate, and the plan's target of three exercises per chapter is not yet met. Other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 50, check the chapter index and the learner's exercise record. The next stop is [course 132: Digital forensics and malware analysis / Engineering course](../../digital-forensics-malware/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
