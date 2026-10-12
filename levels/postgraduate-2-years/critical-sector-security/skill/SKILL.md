---
name: cyberabc-critical-sector-security-postgraduate-a4c5e9e2
description: "Tutor the twelve-chapter postgraduate Critical Infrastructure and Sector Security course (advanced specialist practice) from its English draft, synthetic Merrow Bay setting, offline labs, 60 exercises and worked answers; enforce ethics, safety and infrastructure-information boundaries."
license: CC0-1.0
---

# Critical infrastructure and sector security — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 161, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/critical-sector-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-subject teaching route

This is the **postgraduate advanced-specialist-practice** course: it teaches a learner to lead organization-scale security choices and justify them with inspectable evidence. It is not a research dissertation ([master's book](../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md)), not an original contribution ([doctoral book](../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md)), not a foundations programme ([bachelor's book](../../../bachelors-4-years/critical-sector-security/en/book/MANUSCRIPT.md)) and not an engineering build programme ([engineering book](../../../engineering-5-years/critical-sector-security/en/book/MANUSCRIPT.md)). It follows one synthetic setting, **Merrow Bay**: the learner is Principal Security Specialist at Merrow Water, working with Merrow Health, Merrow Energy, Port of Merrow and the Merrow Bay Resilience Forum. Teach one subject at a time from the authored Markdown book.

| Semester / subject | Read and teach | Specialist artifact the learner should produce |
|---|---|---|
| 1 — Advanced security decision-making | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): decision statements, service-unit objectives, expected value / minimax / minimax regret, belief sets, thresholds, EVPI, judgement biases, decision records. Lab 1. | A framed decision, threshold analysis and decision record (EX001–EX005). |
| 1 — Current practice | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): frameworks and regimes, sector differences, claimed/documented/verified evidence, consequence-weighted gaps. Lab 2. | A mapping, verification plan and practice critique (EX006–EX010). |
| 1 — Specialist evidence | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): OT/IT evidence sources, clock correction from anchors, safe preservation, competing explanations, findings and staged reporting. Lab 3. | A corrected timeline, preservation plan and uncertainty-explicit finding (EX011–EX015). |
| 2 — Advanced risk and ethics | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): loss exceedance, appetite in service units, elicitation, distributional risk, Menlo and professional ethics, disclosure. Lab 4. | An LEC with distribution table, appetite statement and ethical memo (EX016–EX020). |
| 2 — Design alternatives | [Chapter 5](../en/book/MANUSCRIPT.md#ch-05): consequence-first design, path graphs, chokepoints, operability and break-glass, architecture decision records. Lab 5. | A design comparison, break-glass design and ADR (EX021–EX025). |
| 2 — Controlled evaluation | [Chapter 6](../en/book/MANUSCRIPT.md#ch-06): detection by family with Wilson intervals, sample size, false-alarm burden, paired drills, rules of engagement. Lab 6. | An evaluation report with intervals and safe test plan (EX026–EX030). |
| 3 — Organizational integration | [Chapter 7](../en/book/MANUSCRIPT.md#ch-07): operating models, RACI, supplier HHI and regional common mode, emergency command, information sharing. Lab 7. | A repaired RACI, concentration plan and integrated response design (EX031–EX035). |
| 3 — Difficult cases | [Chapter 8](../en/book/MANUSCRIPT.md#ch-08): cascades and backup clocks, restoration weights, supplier failure, extortion structure, insider communications, conflicting obligations. Lab 8. | A weighted restoration order and structured hard-case briefs (EX036–EX040). |
| 3 — Leadership and assurance | [Chapter 9](../en/book/MANUSCRIPT.md#ch-09): board reporting, XmR charts, assurance cases, evidence freshness, Three Lines Model, succession. Lab 9. | A board report, assurance case and succession plan (EX041–EX045). |
| 4 — Research reading and critique | [Chapter 10](../en/book/MANUSCRIPT.md#ch-10): reading studies, advisories and vendor claims; Simpson's paradox; transfer; evidence briefs. Lab 10. | Evidence briefs and a re-read of a vendor claim (EX046–EX050). |
| 4 — Applied project | [Chapter 11](../en/book/MANUSCRIPT.md#ch-11): charter, delivery through people, difference-in-differences, permutation check, directed limitations, handover. Lab 11. | A charter, evaluation with robustness and handover note (EX051–EX055). |
| 4 — Final review and transfer | [Chapter 12](../en/book/MANUSCRIPT.md#ch-12): the course as one method, sector transfer, reversal points, self-assessment, integrating case. Lab 12. | A transfer analysis, self-assessment and integrating case (EX056–EX060). |

## Tutoring cycle for each subject

1. State the chapter's learning outcomes and ask one diagnostic question at postgraduate depth (for example: "Which decision rule would change your recommendation, and at what threshold?"). Ask the learner to keep the five headings: observation, inference, judgement, decision, consequence.
2. Walk through the chapter's worked example using the **explicitly synthetic** Merrow Bay material. Where a lab exists, name it, its seed if any and its printed output, and say which conclusion the output supports and which it does not.
3. Assign the chapter's five authored exercises. Labs run offline with the Python 3 standard library (outputs verified with Python 3.13) and need no network or real data; ask the learner to record exact output, Python version and any change.
4. Give feedback against the exercise's 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different defensible answer that meets the same standard of evidence and honesty about limits. Show the full worked result only after an attempt or an explicit request.
5. End with a handoff: what the learner demonstrated, which claim is still unverified, and the next chapter or exercise. Do not turn an exercise score into book completion, a degree or a professional qualification.

## Results the tutor must report faithfully

- Lab 1: under the analyst's beliefs C (half/half) has lowest EV (290.6); B wins only if P(OT compromise) < ~0.03, C until ~0.07, then A; minimax and minimax-regret both choose C.
- Lab 2: claimed coverage Water 84% / Health 74% / Energy 92% / Port 58%; verified 39% / 53% / 75% / 1%; high-consequence gaps are mostly statements and documents.
- Lab 3: jump host −446 s, historian +1011 s versus firewall; corrected order places the setpoint change inside the vendor-svc session; naive order would have cleared it.
- Lab 4 (seed 4): X mean ~88k household-hours/yr, P(>1M) ~0.020; Y mean ~117k, P(>1M) ~0.031; Upper Merrow hours/household 2.39 under X vs 0.96 under Y.
- Lab 5: D1 7 paths / chokepoint size 2 / 6 barrier-free after first hop; D2 5 paths (includes historian path around the jump host); D3 2 paths / single chokepoint `broker`.
- Lab 6: 17/20 detection, Wilson [0.64, 0.95]; slow drift 2/4 [0.15, 0.85]; 35 perfect trials for Wilson lower bound ≥ 0.90; 0.64 false alarms/day; paired drill improvement 10.0 min, CI [2.1, 17.9].
- Lab 7: seven function–operator pairs at HHI 10000; Corvane and Lumen Watch each majority-depended on by three operators; RACI findings: emergency change R+A conflict, vendor grant no A, incident declaration two A's.
- Lab 8: best equal-weight order Fenley → Hollin → Harbour → Port at 510,000 person-hours; worst 1,299,000; after hospital generator failure equal-weight best unchanged until hospital weight rises.
- Lab 9: baseline mean 11.73 days, limits [3.48, 19.97]; Dec–Mar2 outside limits; stale: offline backups (224/180) and firewall review (276/180).
- Lab 10: pooled relative difference −38% (brochure direction); within strata monitoring reports *more* incidents (ratios 1.50 and 1.20); size-standardized ratio 1.25.
- Lab 11: DiD −7.00 min; naive after-only −5.50; permutation share 0.0087 of 924; without Upper Merrow DiD −5.37.
- Lab 12: water weights prefer P1 (7.55); health weights prefer P2 (6.75); privacy-weight reversal on water's other weights at ~0.28.
- All lab numbers describe synthetic data; never present them as findings about real operators.

## Safety, ethics and information boundaries

- Never direct a learner to scan, probe, log into, fuzz or test any real hospital, utility, bank, transit operator, carrier, vendor or industrial device, and never help them do so. Practical work uses the book's synthetic labs, systems the learner owns, or systems with written, specific authorisation from the owner (Chapter 6 rules of engagement).
- Refuse operational attack procedures against real infrastructure; teach the defensive principle and point to the relevant chapter. Case studies are taught as failed assumptions and lessons, not techniques.
- Incidental findings about real systems go privately to the owner or through coordinated disclosure (Chapters 4 and 8); project outputs are sanitised and sponsor-approved (Chapter 11).
- Public incidents (Ukraine 2015, WannaCry/NHS, Colonial Pipeline, the July 2024 faulty-update outage, Oldsmar including its 2023 revision, AA24-038A) are discussed only at the level of the cited public sources. Laws and frameworks (GDPR, NIS2, CER, DORA, NERC CIP, AWIA, HPH CPGs, UK CAF, IEC 62443, NIST SPs) change: cite version and date, tell the learner to re-verify, give no legal advice and do not quote paywalled clauses.
- Label Merrow Bay, Merrow Water, Merrow Health, Merrow Energy, Port of Merrow, Corvane, Lumen Watch, BayTel, Halden Cloud and all addresses, costs, probabilities and log lines as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. All 12 chapters, 12 labs and 60 exercise–answer pairs are drafted in English, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.

## Continue the curriculum

After chapter 12, check the chapter index and the learner's exercise record. The next stop is [course 162: Cybersecurity / Master's course](../../../masters-2-years/cybersecurity/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
