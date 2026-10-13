---
name: cyberabc-critical-sector-security-technical-36c3b4bc
description: "Tutor the eighteen-chapter technical Critical Infrastructure and Sector Security course (hands-on protocols, hardening, detection, verification and troubleshooting) from its English draft, synthetic Kestrel Vale operations centre, fifteen offline labs, 72 exercises and worked answers; enforce safety, authorization and infrastructure-information boundaries."
license: CC0-1.0
---

# Critical infrastructure and sector security — Technical course course skill

Use this **one skill for the whole 18 months course**. The course has one principal book per language; each of its 18 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 069, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/critical-sector-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.
- [Authored Spanish book draft](../es/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Spanish-speaking learners; where a chapter is not yet in Spanish, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eighteen-subject teaching route

This is the **technical hands-on** course: it teaches a technical operator to open industrial protocol frames, audit and harden hosts, configure and verify conduit firewalls, detect failure modes and unauthorized commands, troubleshoot by eliminating hypotheses and produce evidence another technician can check. It is not the implementer's whole-service build ([technologist book](../../../technologist-3-years/critical-sector-security/en/book/MANUSCRIPT.md)), not managerial decision-making (professional course) and not a first introduction (rapid course). It follows one synthetic setting, **Kestrel Vale**: the learner is a technical officer at the Kestrel Vale Regional Operations Centre (KVROC), which supervises Kestrel Water stations KW-01..KW-12 (Modbus/TCP RTUs at 10.10.*n*.2), Kestrel Grid substation SS-3 (DNP3 outstation 10, master 1, front end fep-01) and Kestrel General Hospital's building-management system. Teach one subject at a time from the authored Markdown book.

| Stage — subject | Read and teach | Artifact the learner should produce |
|---|---|---|
| 1 — Computing and service architecture | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): field/control/supervisory layers; control, monitoring and management paths; poll-cycle budget; shared platforms. Lab 1. | A three-path diagram and a verified poll-cycle redesign (EX001–EX004). |
| 1 — Networks and protocols | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): unauthenticated protocols, Modbus data model, MBAP header, read vs write functions. Lab 2. | Hand and code decodes and a write allowlist (EX005–EX008). |
| 1 — Operating systems and identities | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): effective sshd configuration (first value wins), UID 0, service shells, groups, safe hardening order. Lab 3. | A prioritized hardening plan and service-account design (EX009–EX012). |
| 1 — Scripting and data formats | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): csv/json parsing, fail-closed validation order, reject vs quarantine, record coordinates. Lab 4. | A strict validator and a monitoring summary (EX013–EX016). |
| 1 — Security scope and evidence | [Chapter 5](../en/book/MANUSCRIPT.md#ch-05): technical scope, passive first, evidence fields and hashes, four labels. | A repaired scope and an evidence record (EX017–EX020). |
| 1 — System model | [Chapter 6](../en/book/MANUSCRIPT.md#ch-06): zones and conduits (ISA/IEC 62443 vocabulary), sector differences, declared vs observed. | A zone/conduit model with complete conduit entries (EX021–EX024). |
| 2 — Data and telemetry | [Chapter 7](../en/book/MANUSCRIPT.md#ch-07): sources and blind spots, RFC 5424 PRI, clock-offset correction, UTC timelines. Lab 7. | A corrected timeline with stated uncertainty (EX025–EX028). |
| 2 — Failure modes | [Chapter 8](../en/book/MANUSCRIPT.md#ch-08): gap, stuck, spike, drift, range, stale, loss of control authority; explainable rules. Lab 8. | Conditional rules and fault-vs-attack checks (EX029–EX032). |
| 2 — Tools and methods | [Chapter 9](../en/book/MANUSCRIPT.md#ch-09): method choice, known-answer tests, DNP3 link header and CRC-16/DNP, CRC is not authentication. Lab 9. | A validated checker and control-byte decodes (EX033–EX036). |
| 2 — Control configuration | [Chapter 10](../en/book/MANUSCRIPT.md#ch-10): first-match rule sets, shadowed/redundant/broadening rules, time-bound supplier access, change planning. Lab 10. | A corrected rule set and supplier-access specification (EX037–EX040). |
| 2 — Verification | [Chapter 11](../en/book/MANUSCRIPT.md#ch-11): testable requirements, positive and negative tests, evidence rule, verified/failed/untested. Lab 11. | A traceability record and honest status report (EX041–EX044). |
| 2 — Contained laboratory I | [Chapter 12](../en/book/MANUSCRIPT.md#ch-12): socketpair containment, Modbus responder with write policy, exception codes 01/02/03, lab rubric. Lab 12. | A function-16 extension and a lab assessment (EX045–EX048). |
| 3 — Troubleshooting | [Chapter 13](../en/book/MANUSCRIPT.md#ch-13): eight-step method, predictions before comparison, fault-to-incident escalation, the KW-04 router bypass. Lab 13. | Hypothesis tables, an escalation message and a bypass fix (EX049–EX052). |
| 3 — Automation | [Chapter 14](../en/book/MANUSCRIPT.md#ch-14): SHA-256 manifests, four drift outcomes, preserve-before-revert, auto-fix limits, protecting automation. Lab 14. | Ordered actions, an auto-fix list and a preservation record (EX053–EX056). |
| 3 — Integration and dependencies | [Chapter 15](../en/book/MANUSCRIPT.md#ch-15): interdependency types, reverse-graph search, shared components (esx-03), integration points as boundaries. Lab 15. | Impact paths, degraded-mode test and export redesign (EX057–EX060). |
| 3 — Technical documentation and safety | [Chapter 16](../en/book/MANUSCRIPT.md#ch-16): work instructions with expected results, operations' safety authority, protection systems out of bounds, transient devices, no secrets. | A repaired work instruction and transient-device policy (EX061–EX064). |
| 3 — Contained laboratory II | [Chapter 17](../en/book/MANUSCRIPT.md#ch-17): rules from the model, episodes and window trade-off, self-monitoring pipeline, blind spots. Lab 17. | A fixed pipeline and duty-lead summary (EX065–EX068). |
| 3 — Supervised technical project | [Chapter 18](../en/book/MANUSCRIPT.md#ch-18): project phases, manifest and external seal, handling late additions, project rubric. Lab 18. | A project plan, seal verification and self-assessment (EX069–EX072). |

## Tutoring cycle for each subject

1. State the chapter's learning outcomes and ask one diagnostic question at technician depth (for example: "What exact command or field would you check, and what output would prove it?"). Ask the learner to keep the four labels: observed, inferred, done, open.
2. Walk through the chapter's worked example using the **explicitly synthetic** Kestrel Vale material. Where a lab exists, name it and its printed output, and say which conclusion the output supports and which it does not.
3. Assign the chapter's four authored exercises. Labs run offline with the Python 3 standard library (outputs verified with Python 3.13.5), need no network, privileges or real data, and write files only inside a temporary directory; Lab 12 uses `socket.socketpair()` inside one process. Ask the learner to record exact output, Python version and any change.
4. Give feedback against the exercise's 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different defensible answer that meets the same standard of evidence and honesty about limits. Show the full worked result only after an attempt or an explicit request.
5. End with a handoff: what the learner demonstrated, which claim is still unverified, and the next chapter or exercise. Do not turn an exercise score into book completion or a qualification.

## Results the tutor must report faithfully

- Lab 1: sequential cycle 11.33 s against a 5 s requirement (fails); slowest KW-06 2.76 s; 14.57 s with KW-06 dead; 6.00 s with per-station channels and KW-06 dead.
- Lab 2: two unauthorized writes from 10.30.3.7 (fc 5 coil 160 ON; fc 16 at register 7); one approved engineering write (register 7 = 300); two malformed frames (length; protocol id 1); fc 43 marked for review.
- Lab 3: ten findings on HIST-02, including effective `PasswordAuthentication yes` despite a commented `no`, UID-0 `backup2`, `vendor` in `sudo` and `ops-admins`, `histsvc` with `/bin/bash`.
- Lab 4: 2 accept, 6 reject, 2 quarantine (KW-04 chlorine 7.9; KW-09 75 min in the future), each with its line number.
- Lab 7: after correction the RTU session (23:19:03Z) follows the HMI start (23:16:40Z); two lines unparsed (BSD format; nil timestamp).
- Lab 8: KW-02 stuck 20 readings; KW-05 gap 7 minutes; KW-07 spike 2.96 → 9.8 → 2.97 (in range); KW-01 clean.
- Lab 9: CRC-16/DNP check value 0xEA82 asserted; three valid frames, one CRC failure (ffff vs 1506), one bad start bytes, and one valid-CRC frame from unknown source 77.
- Lab 10: R5 shadowed by R4; tests 2, 4 and 5 fail (R4 allows RDP and SMB; R6 lets 10.20.0.12 reach KW-04).
- Lab 11: verified 3/6 — REQ-3 and REQ-4 failed, REQ-6 untested, T8 ignored for lack of evidence.
- Lab 12: normal read and echo write; exceptions 86/03, 86/02, 88/01, 83/02; only register 7 changed (250 → 300).
- Lab 13: H4 (RTU register map changed) is the only consistent hypothesis; unapproved configuration session → preserve and treat as possible incident.
- Lab 14: debug.sh new; ntp.conf approved change (CHG-2210); sshd_config unapproved; manifest digest prefix fdea74f1d09e359c.
- Lab 15: esx-03 is the only component shared by all three services (7 dependants); gps-clock affects water and grid.
- Lab 17: 10 records, 9 parsed, 1 dropped (malformed, from the new talker), 12 alerts in 5 episodes for 10.20.0.31 including three writes of 65,535 to KW-04 register 7.
- Lab 18: seal prefix 062b9a1fd700dd0eac04b3a8; after a later edit, 04-tests.csv MISMATCH and the other four OK.
- All lab numbers describe synthetic data; never present them as findings about real operators.

## Safety, ethics and information boundaries

- Never direct a learner to scan, probe, log into, fuzz, write to or test any real utility, substation, hospital, carrier, vendor or industrial device, and never help them do so. Practical work uses the book's contained labs, systems the learner owns, or systems with written, specific authorization from the owner (Chapter 5). In control networks prefer passive methods (Chapters 5 and 9).
- Refuse operational attack procedures against real infrastructure, including crafting writes or commands for real devices; teach the defensive principle and point to the relevant chapter. Public incidents (CISA IR-ALERT-H-16-056-01, AA23-335A, AA24-038A) are taught only at the level of the cited sources, as failed assumptions and lessons.
- Protection relays, safety instrumented systems and medical gas or ventilation alarms are out of bounds for security work (Chapter 16).
- Incidental findings about real systems go privately to the owner or through coordinated disclosure. Keep secrets, register maps and network diagrams of real infrastructure out of notes, tickets and screenshots.
- Standards and guidance (NIST SPs, ISA/IEC 62443, CISA CPGs, NCSC CAF, Modbus and DNP3 documents, RFCs) change: cite version and date, tell the learner to re-verify, and give no legal advice.
- Label Kestrel Vale, KVROC, Kestrel Water, Kestrel Grid, Kestrel General Hospital and all people, addresses, frames, accounts, values and log lines as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. All 18 chapters, 15 labs and 72 exercise–answer pairs are drafted in English, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 18, check the chapter index and the learner's exercise record. The next stop is [course 070: Cybersecurity / Technologist course](../../../technologist-3-years/cybersecurity/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
