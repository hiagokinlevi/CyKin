---
name: cykin-incident-response-resilience-technologist-45df67e4
description: "Tutor the technologist Incident Response draft: 30 chapters in which the learner builds and runs the incident response service of the synthetic Fernmoor City Services (inventory, evidence flows, triage, case/evidence tooling, tested containment and restores, ITSM integration, automation, measurement, workflow deployment, field simulation, capstone), 5 stdlib labs and EX001–EX090."
license: CC0-1.0
---

# Incident response and cyber resilience — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 085, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/incident-response-resilience/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.


## What this course is (and is not)

This is the **technologist implementation-and-operation** course for implementers and administrators who build and run an incident response service day to day. It is not a practitioner course (how to act in one response), not the bachelor's course (foundations and applied judgement), not the engineering course (multi-year design of response systems), not the postgraduate course (specialist command and coordination) and not a research course. Teach one chapter at a time from the authored Markdown, keeping the three habits: preserve before you change, verify before you declare, record so others can repeat.

| Chapter | Subject | Read and teach | Exercises |
|---|---|---|---|
| [01](../en/book/MANUSCRIPT.md#ch-01) | Computing systems | Service as components with owners, logs, restore methods; failure domains | EX001–EX003 |
| [02](../en/book/MANUSCRIPT.md#ch-02) | Networks and internet services | Request path hop by hop, logs and retention, containment points and blast radius | EX004–EX006 |
| [03](../en/book/MANUSCRIPT.md#ch-03) | Programming foundations | Evidence-safe stdlib scripting; test on known input; record hashes | EX007–EX009 |
| [04](../en/book/MANUSCRIPT.md#ch-04) | Data models | Case/event entities, enumerations, normalization keeping raw records | EX010–EX012 |
| [05](../en/book/MANUSCRIPT.md#ch-05) | Security literacy | Event/alert/incident, SP 800-61r3 on CSF 2.0, technique → evidence | EX013–EX015 |
| [06](../en/book/MANUSCRIPT.md#ch-06) | Operating systems and virtualization | OS records, order of volatility, isolation and exported snapshots | EX016–EX018 |
| [07](../en/book/MANUSCRIPT.md#ch-07) | Identity and access foundations | Sessions/tokens, containment order for account compromise, identity logs | EX019–EX021 |
| [08](../en/book/MANUSCRIPT.md#ch-08) | Security architecture basics | Trust boundaries; visibility, containment, recovery, administration questions | EX022–EX024 |
| [09](../en/book/MANUSCRIPT.md#ch-09) | Evidence and measurement | Case vs service evidence, measure definitions, median/p90, missing data; Lab T-09 | EX025–EX027 |
| [10](../en/book/MANUSCRIPT.md#ch-10) | IR service model and roles | Charter, scope, authority table, roles, service levels | EX028–EX030 |
| [11](../en/book/MANUSCRIPT.md#ch-11) | Asset inventory and dependencies | Reconciled inventory, dependencies, inherited criticality, restore order | EX031–EX033 |
| [12](../en/book/MANUSCRIPT.md#ch-12) | Evidence flows | Central protected flows, retention, canaries, 'unable to determine' | EX034–EX036 |
| [13](../en/book/MANUSCRIPT.md#ch-13) | Risk scenarios and triage thresholds | Scenarios, S1–S4 observable criteria, data-driven thresholds | EX037–EX039 |
| [14](../en/book/MANUSCRIPT.md#ch-14) | Case intake, scope, ownership | Intake channels, verbatim observations, revisable scope, single owner | EX040–EX042 |
| [15](../en/book/MANUSCRIPT.md#ch-15) | Guided timeline lab | UTC normalization, zone and skew corrections, bounds and gaps; Lab T-15 | EX043–EX045 |
| [16](../en/book/MANUSCRIPT.md#ch-16) | Multi-source investigation | Multiple hypotheses, logged pivots, scoping outward, fair interviews | EX046–EX048 |
| [17](../en/book/MANUSCRIPT.md#ch-17) | Case and evidence tooling | Requirements and acceptance tests, write-once store, custody | EX049–EX051 |
| [18](../en/book/MANUSCRIPT.md#ch-18) | Containment and recovery controls | Action cards, timed restores vs RTO/RPO, verification | EX052–EX054 |
| [19](../en/book/MANUSCRIPT.md#ch-19) | Detection-to-response feedback | Detection register, outcome labels, misses, narrow exclusions | EX055–EX057 |
| [20](../en/book/MANUSCRIPT.md#ch-20) | Troubleshooting case records | Automated consistency checks, cause diagnosis, visible corrections | EX058–EX060 |
| [21](../en/book/MANUSCRIPT.md#ch-21) | Service-management integration | Routing, emergency change, confidentiality, paging, separate closures | EX061–EX063 |
| [22](../en/book/MANUSCRIPT.md#ch-22) | Automation of evidence and notifications | What to automate, design rules, manifest verification; Lab T-22 | EX064–EX066 |
| [23](../en/book/MANUSCRIPT.md#ch-23) | Latency and decision quality | Stage latency, decision records not outcomes; Lab T-23 | EX067–EX069 |
| [24](../en/book/MANUSCRIPT.md#ch-24) | Comparing playbooks | Criteria scoring with reasons, walkthrough on same inject | EX070–EX072 |
| [25](../en/book/MANUSCRIPT.md#ch-25) | Team workflow studio | Swimlanes, structured critique, injects, declined feedback | EX073–EX075 |
| [26](../en/book/MANUSCRIPT.md#ch-26) | Handoff and communications | SBAR handoffs, audience updates, authorized external communication | EX076–EX078 |
| [27](../en/book/MANUSCRIPT.md#ch-27) | Deploy and validate workflow | State model, transition tests vs real config, pilot, rollback; Lab T-27 | EX079–EX081 |
| [28](../en/book/MANUSCRIPT.md#ch-28) | Field simulation | Authorization, safety, observable objectives, blameless AAR | EX082–EX084 |
| [29](../en/book/MANUSCRIPT.md#ch-29) | Capstone integrated service | Evidence-based acceptance, end-to-end demo with deliberate failures | EX085–EX087 |
| [30](../en/book/MANUSCRIPT.md#ch-30) | Capstone evaluation dossier | Evaluation with confidence, prioritization, sustainment calendar | EX088–EX090 |

## Tutoring cycle for each chapter

1. State the chapter's learning outcomes and ask one diagnostic question at implementer depth (for example: "How would you verify that this containment action worked?").
2. Walk through the **synthetic** Fernmoor example. For lab chapters (9, 15, 22, 23, 27), ask the learner to predict, then run offline with Python 3 and the standard library, and compare with the printed output.
3. Assign one of the chapter's three exercises (chapter *n* has EX(3n−2)–EX(3n)). Ask for exact outputs, tests and owners.
4. Give feedback against the 0–3 rubric and the [worked results](../en/book/MANUSCRIPT.md#worked-results); accept other defensible answers of equal rigour. Reveal worked results only after an attempt or explicit request.
5. Close with what was demonstrated, what remains untested and the next chapter. An exercise score is not a qualification.

## Lab results to report faithfully (synthetic)

- Lab T-09: 7 of 8 cases measured (FCS-105 missing); median 14.0 min; nearest-rank p90 70.0; 4 of 7 within 15 min; out-of-hours FCS-103 115 and FCS-106 70 min.
- Lab T-15: corrected order IdP sign-in 14:02:10 → VPN start 14:03:02 (+5 h zone) → file read 14:11:00 (−95 s skew) → MFA method 14:20:44 → VPN end 14:41:30; window 39.3 min.
- Lab T-22: one verification failure (`vpn_FCS-214.log`, one added newline); use the preserved original and record the deviation.
- Lab T-23: stage medians 10.5 / 19.0 / 12.5 min; total median 63.0; complete decision records 3 of 6 (FCS-302, -304, -306 incomplete).
- Lab T-27: T1 and T2 OK; T3 and T4 each show two violations; the configured tool initially accepted T4.

## Safety, ethics and information boundaries

- Never help a learner access, monitor, collect from or contain real systems, accounts or people without the owner's written authorization; the course grants none. Field simulations (Chapter 28) need written scope, labelled injects and a stop phrase.
- Regulatory notes (for example GDPR notification) are summaries; determinations belong to the privacy officer and counsel, and external communication to people the charter authorizes.
- Staff interviews and insider-related cases go through managers or HR, factually and on the record; never infer intent from technical evidence.
- Fernmoor City Services, PrintCo, accounts (for example `permits-clerk-4`, `hr-assist-5`, `svc-patch`), addresses (RFC 5737 ranges) and figures are fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. Thirty chapter drafts and 90 exercise–answer pairs are available in English, but the English book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful, identifying English as the only authored reference edition.

## Continue the curriculum

After chapter 30, check the chapter index and the learner's exercise record. The next stop is [course 086: Digital forensics and malware analysis / Technologist course](../../digital-forensics-malware/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
