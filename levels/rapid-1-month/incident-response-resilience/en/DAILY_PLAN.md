# Daily reading plan — Incident Response / Rapid / English

**Editorial responsibility: hiagokinlevi. State: mapped draft allocation, not a completed daily edition.** One book, four subject-chapters, **22 proposed daily reading units**. All teaching, examples, exercises and final answers remain in [the single manuscript](book/MANUSCRIPT.md). This is a navigation manifest, not another textbook or a claim that 22 new native lessons were written.

[Course](../README.md) · [Chapter index](SUBJECTS.md) · [Book plan](book/PLAN.md) · [Course skill](../skill/SKILL.md) · [Daily standard](../../../../DAILY_STUDY_STANDARD.md)

Read each chapter's learning outcomes first. Before attempting an exercise, open its named input records in the book: the R1–R8 table is in Chapter 1 section 1.7, R9–R16 in Chapter 2 section 2.4, and R17–R24 in Chapter 3 section 3.2. The exercise's own evidence-release boundary still applies even if a later demonstration has been read. Never import independent laboratory fixtures into the canonical case. The first listed exercise is each day's distinct primary task; the additional assignments preserve all 50 existing numbered exercises once each.

This allocation needs workload and prerequisite review. Some existing sections are long and reference other parts of their chapter. Do not certify them as calibrated daily lessons or compress the underlying explanation to force a short session. Native daily revision must make prerequisites explicit, improve progression and retain useful technical depth in the same book. The 22-day reference is not an exact count for every civil month; show the actual calendar and resolve any difference before claiming the full dated course is covered.

## Daily index

Each row maps a continuous reading range, a worked example and distinct exercises in the manuscript. The JSON selectors are start-inclusive and end-exclusive. The reader checks source revision, unique headings, chapter boundaries and final-answer pairs; any stale or missing input blocks the view. That runtime check is not a specialist, linguistic or workload review.

| Day | Learning focus | Exercises |
|---|---|---|
| <a id="day-0001"></a>D0001 | Readiness and evidence for a decision | EX001 |
| <a id="day-0002"></a>D0002 | Normal behavior and invariants | EX002 |
| <a id="day-0003"></a>D0003 | Service paths and degraded operation | EX003 |
| <a id="day-0004"></a>D0004 | Roles, delegation and request-bound authority | EX006 |
| <a id="day-0005"></a>D0005 | Scope, chronology and opening record | EX004, EX005, EX007, EX008 |
| <a id="day-0006"></a>D0006 | First decision and readiness improvement | EX009, EX010, EX011, EX012, EX013 |
| <a id="day-0007"></a>D0007 | Triage and independent urgency dimensions | EX014, EX015, EX016 |
| <a id="day-0008"></a>D0008 | Preservation queue before collection | EX018 |
| <a id="day-0009"></a>D0009 | Copy integrity, clocks and delayed arrival | EX019, EX020, EX021 |
| <a id="day-0010"></a>D0010 | Evidence package and source-hold lifecycle | EX024 |
| <a id="day-0011"></a>D0011 | Correlation, quiet queries and handoff | EX017, EX022, EX025, EX026 |
| <a id="day-0012"></a>D0012 | Impact measurement and restricted views | EX023 |
| <a id="day-0013"></a>D0013 | Containment, tested scope and reversal | EX027, EX028, EX029, EX030, EX031, EX036 |
| <a id="day-0014"></a>D0014 | Cause-specific eradication and falsifiers | EX032 |
| <a id="day-0015"></a>D0015 | Recovery state, copies and test frames | EX033, EX034 |
| <a id="day-0016"></a>D0016 | Accepted recovery versus import success | EX035, EX037 |
| <a id="day-0017"></a>D0017 | Pending requests and safe resumption | EX038 |
| <a id="day-0018"></a>D0018 | Staged tabletop and frozen decisions | EX039, EX040, EX041, EX042, EX043, EX044 |
| <a id="day-0019"></a>D0019 | Scoring and improvement closure | EX049 |
| <a id="day-0020"></a>D0020 | Branch-specific service and communication | EX045, EX046, EX047 |
| <a id="day-0021"></a>D0021 | Delivery, version and read-back | EX048 |
| <a id="day-0022"></a>D0022 | Independent reconstruction and final handoff | EX050 |

The [final answer appendix](book/MANUSCRIPT.md#answers) remains in the same book. Attempt the selected prompt before revealing the answer. This edition's existing supplemental labs retain their own worked results and assessment rules.

## Revision-bound allocation

<!-- cykin:daily-plan:start -->
```json
{"schema":1,"level":"rapid-1-month","area":"incident-response-resilience","language":"en","state":"mapped-draft","source_blob_sha":"b91edc4bd76d02822e634cbb90e904bc337b6fc2","lessons":[
{"id":"D0001","chapter":1,"title":"Readiness and evidence that can answer a decision","start":"### 1.1 Response is part of risk management","end":"### 1.2a Normal booking behavior and service invariants","example":"#### Test whether readiness is usable","exercises":["EX001"]},
{"id":"D0002","chapter":1,"title":"Normal booking behavior and business invariants","start":"### 1.2a Normal booking behavior and service invariants","end":"### 1.2b Essential service paths and degraded modes","example":"#### A contrasting wrong and correct interpretation","exercises":["EX002"]},
{"id":"D0003","chapter":1,"title":"Service paths and honest degraded operation","start":"### 1.2b Essential service paths and degraded modes","end":"### 1.3 Roles and decision authority","example":"#### Contrast a tempting wrong conclusion with a defensible one","exercises":["EX003"]},
{"id":"D0004","chapter":1,"title":"Roles, delegation and request-bound authority","start":"### 1.3 Roles and decision authority","end":"### 1.4 Scope, authorization and safety","example":"#### 1.3a.9 Two complete contrasting examples: a valid delegation and an unsafe substitute","exercises":["EX006"]},
{"id":"D0005","chapter":1,"title":"Scope, source chronology and the opening record","start":"### 1.4 Scope, authorization and safety","end":"### 1.8 Guided readiness workshop: prepare the first decision","example":"### 1.6 Worked example: the unusual sign-in","exercises":["EX004","EX005","EX007","EX008"]},
{"id":"D0006","chapter":1,"title":"A reviewable first decision and readiness improvement","start":"### 1.8 Guided readiness workshop: prepare the first decision","end":"### Chapter 1 exercises","example":"### 1.9 Build a decision gate from incomplete evidence","exercises":["EX009","EX010","EX011","EX012","EX013"]},
{"id":"D0007","chapter":2,"title":"Triage and independent dimensions of urgency","start":"### 2.1 An alert is a question to investigate","end":"### 2.3 Preserve what supports the next decision","example":"#### 2.2a.9 Example one — correct 09:05 assessment without hindsight","exercises":["EX014","EX015","EX016"]},
{"id":"D0008","chapter":2,"title":"A bounded preservation queue before collection","start":"### 2.3 Preserve what supports the next decision","end":"### 2.5 Contained lab: preserve and check a synthetic extract","example":"### 2.4 Worked example: the second alert","exercises":["EX018"]},
{"id":"D0009","chapter":2,"title":"Copy integrity, clock meaning and delayed arrival","start":"### 2.5 Contained lab: preserve and check a synthetic extract","end":"### 2.8 Evidence package audit: integrity is one link in a longer chain","example":"#### Optional T2 replay: a late row in the same event window","exercises":["EX019","EX020","EX021"]},
{"id":"D0010","chapter":2,"title":"Evidence packages and the source-hold lifecycle","start":"### 2.8 Evidence package audit: integrity is one link in a longer chain","end":"### 2.9 Contained lab: correlate records without inventing an actor","example":"#### 2.8a.13 Correct example — a complete but explicitly hypothetical hold receipt","exercises":["EX024"]},
{"id":"D0011","chapter":2,"title":"Correlation, quiet queries and a bounded handoff","start":"### 2.9 Contained lab: correlate records without inventing an actor","end":"### 2.14 Define the thing you are trying to count","example":"#### Q1-S — qualify identifiers and test sensitivity to clock uncertainty","exercises":["EX017","EX022","EX025","EX026"]},
{"id":"D0012","chapter":2,"title":"Measure impact and minimize the review view","start":"### 2.14 Define the thing you are trying to count","end":"### Chapter 2 exercises","example":"### 2.20 Contrastive worked example at the Round B decision","exercises":["EX023"]},
{"id":"D0013","chapter":3,"title":"Containment choices, tested scope and reversal","start":"### 3.1 A decision loop rather than a fixed sequence","end":"### 3.4 Eradication requires a supported cause","example":"#### Make the comparison observable","exercises":["EX027","EX028","EX029","EX030","EX031","EX036"]},
{"id":"D0014","chapter":3,"title":"A cause-specific eradication claim and its falsifier","start":"### 3.4 Eradication requires a supported cause","end":"### 3.5 Verify recovery, not merely activity","example":"#### Build a cause-to-fix contract","exercises":["EX032"]},
{"id":"D0015","chapter":3,"title":"Recovery state, copy selection and test frames","start":"### 3.5 Verify recovery, not merely activity","end":"### 3.8a Measure recovery time and the recovered data point","example":"### 3.6 Guided reconciliation and return-to-service lab","exercises":["EX033","EX034"]},
{"id":"D0016","chapter":3,"title":"Measure accepted recovery, not a successful import","start":"### 3.8a Measure recovery time and the recovered data point","end":"### 3.12 Reconcile a manual queue before resuming writes","example":"#### RTE3.5 Contrastive worked example: measured service acceptance","exercises":["EX035","EX037"]},
{"id":"D0017","chapter":3,"title":"Pending requests, duplicate effects and safe resumption","start":"### 3.12 Reconcile a manual queue before resuming writes","end":"### Chapter 3 exercises","example":"#### Worked contrast: a confident but unsafe restart","exercises":["EX038"]},
{"id":"D0018","chapter":4,"title":"A staged tabletop and a frozen decision record","start":"### 4.1 Exercise purpose and boundaries","end":"### 4.5 Score the evidence and the handoff","example":"### 4.3 Worked tabletop: one acceptable path","exercises":["EX039","EX040","EX041","EX042","EX043","EX044"]},
{"id":"D0019","chapter":4,"title":"Score actual artifacts and verify improvement closure","start":"### 4.5 Score the evidence and the handoff","end":"### 4.10 Optional communication replay: a request for reassurance and an unverified claim","example":"#### Calibrate a score against the artifact that existed at the checkpoint","exercises":["EX049"]},
{"id":"D0020","chapter":4,"title":"Branch-specific service and communication decisions","start":"### 4.10 Optional communication replay: a request for reassurance and an unverified claim","end":"### 4.19 Verify the delivery side of incident coordination","example":"### 4.10 Optional communication replay: a request for reassurance and an unverified claim","exercises":["EX045","EX046","EX047"]},
{"id":"D0021","chapter":4,"title":"Delivery, recipient, version and read-back","start":"### 4.19 Verify the delivery side of incident coordination","end":"### 4.21 Blind handoff and independent state reconstruction","example":"#### 4.19.14 Contrastive worked example: delivered does not mean safely coordinated","exercises":["EX048"]},
{"id":"D0022","chapter":4,"title":"Independent reconstruction and final handoff","start":"### 4.21 Blind handoff and independent state reconstruction","end":"### Chapter 4 exercises","example":"#### 4.21.15 Correct worked handoff","exercises":["EX050"]}
]}
```
<!-- cykin:daily-plan:end -->

## Continue studying

Return to the [daily index](#daily-index), inspect the [four subject-chapters](SUBJECTS.md), or read the [whole book](book/MANUSCRIPT.md). Daily completion remains unverified until the learner actually studies, attempts the tasks and receives feedback. The next editorial work is to review D0001–D0005 for prerequisite order, reasonable daily workload and explicit native daily navigation, without deleting the original teaching or the remaining exercises.
