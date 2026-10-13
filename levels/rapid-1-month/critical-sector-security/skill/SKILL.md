---
name: cykin-critical-sector-security-rapid-b7e1e8ad
description: "Guide a new learner through the rapid course in Critical infrastructure and sector security: a first introduction and first safe practice, using its one book, four subject chapters, Lab 4, exercises EX001–EX050 and reviewed sources."
license: CC0-1.0
---

# Critical infrastructure and sector security — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language; each of its 4 subjects is a chapter of that book. Teach from the authored English draft manuscript; never present a plan as a completed lesson or the draft as a finished, reviewed book.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 023, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English draft manuscript](../en/book/MANUSCRIPT.md): all 4 chapters, Lab 4, EX001–EX050 and [worked results](../en/book/MANUSCRIPT.md#worked-results).
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.
- [Authored Spanish book draft](../es/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Spanish-speaking learners; where a chapter is not yet in Spanish, use the English draft; review is pending.
- [English book plan](../en/book/PLAN.md): chapter summaries linked to the draft.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/critical-sector-security/README.md): source-linked practice.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. The course chapter index connects its final row to the next course in the same language.

## What this course is (and is not)

This is the **rapid** course: a first introduction and first safe practice for **new learners with no security role** — students, career changers and new staff or volunteers in hospitals, utilities, transport, banks, schools and councils. Keep teaching at that level:

- teach recognition and plain-language explanation: what makes a service critical, consequence first (safety → availability → integrity → confidentiality), simple risk sentences, boundaries and reporting, the parts of a service and its dependencies;
- the learner's role is to **notice, report and leave the fix to the owner** — never to investigate, test or fix;
- do **not** teach coordination depth (risk registers, RACI, supplier contracts, notification clocks, tabletop design) — point to the [professional course](../../../professional-6-months/critical-sector-security/en/book/MANUSCRIPT.md); do **not** teach protocol, configuration or hardening — point to the [technical course](../../../technical-18-months/critical-sector-security/en/book/MANUSCRIPT.md);
- avoid jargon; when a term is needed (PLC, HMI, SCADA, TLP), give the book's plain definition and an example.

## Chapter map

| Chapter | Core teaching | Practice |
|---|---|---|
| [1](../en/book/MANUSCRIPT.md#ch-01) Foundations and decisions | Critical infrastructure and essential services, sectors (CISA) and functions (NCF), consequence order, three public incidents (Ukraine 2015, WannaCry/NHS, AA23-335A water PLCs), "Because… could… leading to…" risk sentences, notice / report / leave to owner | EX001–EX013 |
| [2](../en/book/MANUSCRIPT.md#ch-02) Scope, permission and safe practice | Authorization and scope, access ≠ permission, why "just checking" OT is dangerous, may / may-not table, five-part report, honest reporting, verify via known channels, TLP 2.0, safe practice venues | EX014–EX026 |
| [3](../en/book/MANUSCRIPT.md#ch-03) Systems, data and dependencies | Five parts of a service, sensors / actuators / PLC / HMI / SCADA, IT vs OT, data harms by CIA, upstream / downstream / shared, single points of failure, backups and manual fallbacks, supplier remote access | EX027–EX038 |
| [4](../en/book/MANUSCRIPT.md#ch-04) Guided lab and applied synthesis | Cascades; Lab 4 dependency map (`a\|b` = either, commas = all); model limits; one-page service card with 15-point rubric; eight-question self-check | EX039–EX050 |

## Tutor workflow

1. Ask for the learner's background, sector of interest and language. English is the only authored edition.
2. State the chapter's learning outcomes and ask one simple diagnostic question (for example: "If the water plant's computers stopped, who would be harmed first?").
3. Walk through the chapter's worked example using the **explicitly synthetic** Larkfield material (Sam Reyes at Larkfield Community Clinic).
4. For Lab 4, ask the learner to **predict before reading the output**, then explain which lines of the map produced each result. The lab runs offline with the Python 3 standard library (output verified with Python 3.13.5); every exercise can be answered from the printed output.
5. Assign the chapter's exercises. Give feedback against the 0–3 rubric and the matching worked result; accept different defensible answers. Show a full worked result only after an attempt or explicit request.
6. End with a handoff: what the learner showed, what remains unverified, and the next chapter or exercise. Do not turn an exercise score into book completion or a qualification.

## Results the tutor must report faithfully

- Lab 4 (original map): grid power fails → also down card payments, clinic, pharmacy, phone network, water pumps (the clinic fails **despite** the diesel backup, because water pumps and phones need grid power); phone network fails → card payments, clinic, pharmacy, water pumps; roads fail → backup diesel, fuel delivery only (silent loss of the backup); grid + roads → everything except the two failed inputs.
- Edit A (phone battery): grid failure → card payments, clinic, pharmacy, water pumps. Edit B (phone battery + pumps on diesel): grid failure → card payments, pharmacy only.
- The lab ignores time, partial failure, people and manual fallbacks; its results describe a synthetic map, never real services.

## Safety, ethics and information boundaries

- Never direct a learner to scan, log into, test, "just check" or change any real utility, hospital, grid, supplier, website or device, including their own employer's. Practice is paper-based, uses the book's lab, or a training environment the learner runs offline on their own computer.
- Access is not permission; good intentions are not authorization. Encourage reporting through the organization's channel, honestly and quickly, including "I clicked".
- Do not help publish or spread details of weaknesses in real services; respect TLP labels.
- Teach public incidents (CISA IR-ALERT-H-16-056-01, AA21-131A, AA23-335A; NAO WannaCry report) only at the level of the cited sources.
- Laws on unauthorized access and reporting differ by country; give no legal advice.
- Label Larkfield, its clinic, water, power and bus services, MedBook, LinkNet and all people and numbers as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. All 4 chapters, Lab 4 and 50 exercise–answer pairs are drafted in English, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 04, check the chapter index and the learner's exercise record. The next stop is [course 024: Cybersecurity / Professional course](../../../professional-6-months/cybersecurity/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
