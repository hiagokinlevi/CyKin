# Principal book plan — Incident response and cyber resilience / Rapid course / English

**One book, at least four weekly chapters and 20 daily lessons.** The course is an introductory, contained learning path of approximately 80 hours. The published teaching lives in [the principal manuscript](MANUSCRIPT.md); this file explains its sequence and does not substitute for a lesson. A chapter or the study timeline may grow when the technical concept requires more depth.

**Editorial state:** all four weekly chapters, 20 daily lessons and 50 exercise/answer pairs are present. Whole-volume technical, editorial, rights, accessibility and A4 verification remain open. Do not infer finished-book approval from chapter count.

[Home](../../../../../README.md) · [Course home](../../README.md) · [Edition](../README.md) · [Chapter index](../SUBJECTS.md) · [Course skill](../../skill/SKILL.md) · [Book standard](../../../../../BOOK_STANDARD.md)

## Module structure

1. [Readiness, roles and authorized scope](MANUSCRIPT.md#week-01): service promises, evidence readiness, booking invariants, authority rehearsal and a bounded first decision.
2. [Alert triage and evidence preservation](MANUSCRIPT.md#week-02): priority under changing evidence, source-hold and copy lifecycles, correlation, impact and privacy.
3. [Containment, eradication and recovery](MANUSCRIPT.md#week-03): authorized options, cause-specific checks, isolated restore, recovery gates and queue reconciliation.
4. [Guided simulation and after-action review](MANUSCRIPT.md#week-04): released injects, frozen-artifact scoring, communication, delivery/read-back and blind handoff.

## Daily lesson briefs

These short lesson briefs route the reader to published teaching inside four weekly chapters. The exercise IDs below refer to the full prompts in each lesson and worked results in the same book.

<a id="ch-01"></a>

## Chapter 01 — Incident readiness, roles and authorized scope

**Instructional week 1.** Five daily lessons follow. The chapter may be expanded when the subject demands more depth.

<a id="lesson-01"></a>

### Lesson 01 — Evidence readiness and the first case question

**Chapter 1, day 1.** [Read the complete lesson](MANUSCRIPT.md#lesson-01). Its teaching develops evidence readiness and the first case question, includes a worked checkpoint and assigns EX001. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 01 of at least 20:** [← Course home](../../README.md) · [Course lesson index](../SUBJECTS.md) · [Lesson 02 →](MANUSCRIPT.md#lesson-02)

<a id="lesson-02"></a>

### Lesson 02 — Booking invariants and behavioral baselines

**Chapter 1, day 2.** [Read the complete lesson](MANUSCRIPT.md#lesson-02). Its teaching develops booking invariants and behavioral baselines, includes a worked checkpoint and assigns EX002, EX005, EX010. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 02 of at least 20:** [← Lesson 01](MANUSCRIPT.md#lesson-01) · [Course lesson index](../SUBJECTS.md) · [Lesson 03 →](MANUSCRIPT.md#lesson-03)

<a id="lesson-03"></a>

### Lesson 03 — Service paths, dependencies and degraded modes

**Chapter 1, day 3.** [Read the complete lesson](MANUSCRIPT.md#lesson-03). Its teaching develops service paths, dependencies and degraded modes, includes a worked checkpoint and assigns EX003, EX008, EX011. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 03 of at least 20:** [← Lesson 02](MANUSCRIPT.md#lesson-02) · [Course lesson index](../SUBJECTS.md) · [Lesson 04 →](MANUSCRIPT.md#lesson-04)

<a id="lesson-04"></a>

### Lesson 04 — Authority, delegation and pre-incident rehearsal

**Chapter 1, day 4.** [Read the complete lesson](MANUSCRIPT.md#lesson-04). Its teaching develops authority, delegation and pre-incident rehearsal, includes a worked checkpoint and assigns EX006, EX013. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 04 of at least 20:** [← Lesson 03](MANUSCRIPT.md#lesson-03) · [Course lesson index](../SUBJECTS.md) · [Lesson 05 →](MANUSCRIPT.md#lesson-05)

<a id="lesson-05"></a>

### Lesson 05 — Scope, case record and bounded first decision

**Chapter 1, day 5.** [Read the complete lesson](MANUSCRIPT.md#lesson-05). Its teaching develops scope, case record and bounded first decision, includes a worked checkpoint and assigns EX004, EX007, EX009, EX012. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 05 of at least 20:** [← Lesson 04](MANUSCRIPT.md#lesson-04) · [Course lesson index](../SUBJECTS.md) · [Lesson 06 →](MANUSCRIPT.md#lesson-06)

### Continue studying — chapter 01 of 04

[← Course overview](../../README.md) · [Course lesson index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

<a id="ch-02"></a>

## Chapter 02 — Alert triage and evidence preservation

**Instructional week 2.** Five daily lessons follow. The chapter may be expanded when the subject demands more depth.

<a id="lesson-06"></a>

### Lesson 06 — A bounded triage question and revisable priority

**Chapter 2, day 1.** [Read the complete lesson](MANUSCRIPT.md#lesson-06). Its teaching develops a bounded triage question and revisable priority, includes a worked checkpoint and assigns EX014, EX015, EX016. Attempt the prompts in the lesson before reading their final results.

**TRI2 verification checkpoint:** The [same-scope continuation](MANUSCRIPT.md#ir-rapid-ch02-tri2-scope-check) adds an explicit input contract, a worked interval counterexample, four prediction cases and a [final-appendix answer](MANUSCRIPT.md#ir-rapid-ch02-tri2-scope-result). Python 3.13.5 reproduced all 25 original lines, three release challenges and four supplementary lines. A separate 128-case decision table covered 32 unbounded-absence rejections and 16 bounded same-scope conflicts; schema, guard-precedence and non-mutation checks also passed. This is scoped TRI2 verification, not whole-book approval, new lesson coverage, translation parity or a current A4 measurement. At that checkpoint, the next sequential verification target was Lesson 07.

**Continue studying — lesson 06 of at least 20:** [← Lesson 05](MANUSCRIPT.md#lesson-05) · [Course lesson index](../SUBJECTS.md) · [Lesson 07 →](MANUSCRIPT.md#lesson-07)

<a id="lesson-07"></a>

### Lesson 07 — Preservation, timestamps and package integrity

**Chapter 2, day 2.** [Read the complete lesson](MANUSCRIPT.md#lesson-07). Its teaching develops preservation, timestamps and package integrity, includes a worked checkpoint and assigns EX017, EX019, EX020, EX021. Attempt the prompts in the lesson before reading their final results.

**Lesson 07 review checkpoint:** The [copy-checkpoint teaching](MANUSCRIPT.md#ir-rapid-l07-copy-checkpoint) now distinguishes an intended buffer from file read-back, compares equal hash endpoints with different intervening histories, and exercises complete versus partial local creation. Its [worked answer](MANUSCRIPT.md#ir-rapid-l07-copy-checkpoint-result) is in this book's appendix. EX021 and its answer retain five rows but distinguish source-time kinds and each row's evidential limit. E1's two baseline outputs, the seven-line temporal program and six-line T2 program were reproduced; the independent in-memory example adds three lines, not a new daily lesson or numbered exercise. At that checkpoint, the next sequential verification target was Lesson 08. Whole-volume review and a current-source A4 rendering remain open.

**Continue studying — lesson 07 of at least 20:** [← Lesson 06](MANUSCRIPT.md#lesson-06) · [Course lesson index](../SUBJECTS.md) · [Lesson 08 →](MANUSCRIPT.md#lesson-08)

<a id="lesson-08"></a>

### Lesson 08 — A source hold is a separate lifecycle

**Chapter 2, day 3.** [Read the complete lesson](MANUSCRIPT.md#lesson-08). Its teaching distinguishes a source-hold lifecycle from a retained copy, includes a worked checkpoint and assigns EX018. Attempt the prompts in the lesson before reading their final results.

**Lesson 08 review checkpoint:** The [HOLD2-R unit](MANUSCRIPT.md#ir-rapid-l08-review-checkpoint) distinguishes the last reported effect check, an invented owner-review appointment and the exclusive technical term, then exposes multiple defects behind a first-refusal label. Its logical timeline, eight-line continuation, two practice tables and [worked answer](MANUSCRIPT.md#ir-rapid-l08-review-checkpoint-result) deepen the existing lesson. Python 3.13.5 reproduced the unchanged 33-line baseline and eight additional lines; 3,537 finite packet evaluations checked time cutoffs, scoped authorization, types, lifecycle and binding, with input non-mutation. EX018 retains its original three-row request/two-row comparison, and no new lesson or exercise ID is counted. The next sequential verification target is Lesson 09. These checks do not establish a real source hold, whole-volume approval or a current-source A4 rendering.

**Continue studying — lesson 08 of at least 20:** [← Lesson 07](MANUSCRIPT.md#lesson-07) · [Course lesson index](../SUBJECTS.md) · [Lesson 09 →](MANUSCRIPT.md#lesson-09)

<a id="lesson-09"></a>

### Lesson 09 — Correlation, quiet queries and reviewer handoff

**Chapter 2, day 4.** [Read the complete lesson](MANUSCRIPT.md#lesson-09). Its teaching develops correlation, quiet queries and reviewer handoff, includes a worked checkpoint and assigns EX022, EX024. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 09 of at least 20:** [← Lesson 08](MANUSCRIPT.md#lesson-08) · [Course lesson index](../SUBJECTS.md) · [Lesson 10 →](MANUSCRIPT.md#lesson-10)

<a id="lesson-10"></a>

### Lesson 10 — Impact bounds, denominators and privacy

**Chapter 2, day 5.** [Read the complete lesson](MANUSCRIPT.md#lesson-10). Its teaching develops impact bounds, denominators and privacy, includes a worked checkpoint and assigns EX023, EX025, EX026. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 10 of at least 20:** [← Lesson 09](MANUSCRIPT.md#lesson-09) · [Course lesson index](../SUBJECTS.md) · [Lesson 11 →](MANUSCRIPT.md#lesson-11)

### Continue studying — chapter 02 of 04

[← Chapter 01](#ch-01) · [Course lesson index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

<a id="ch-03"></a>

## Chapter 03 — Containment, eradication and recovery decisions

**Instructional week 3.** Five daily lessons follow. The chapter may be expanded when the subject demands more depth.

<a id="lesson-11"></a>

### Lesson 11 — Containment options and their service cost

**Chapter 3, day 1.** [Read the complete lesson](MANUSCRIPT.md#lesson-11). Its teaching develops containment options and their service cost, includes a worked checkpoint and assigns EX027, EX028, EX029. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 11 of at least 20:** [← Lesson 10](MANUSCRIPT.md#lesson-10) · [Course lesson index](../SUBJECTS.md) · [Lesson 12 →](MANUSCRIPT.md#lesson-12)

<a id="lesson-12"></a>

### Lesson 12 — Cause-specific correction and initial recovery gates

**Chapter 3, day 2.** [Read the complete lesson](MANUSCRIPT.md#lesson-12). Its teaching develops cause-specific correction and initial recovery gates, includes a worked checkpoint and assigns EX030, EX031, EX032. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 12 of at least 20:** [← Lesson 11](MANUSCRIPT.md#lesson-11) · [Course lesson index](../SUBJECTS.md) · [Lesson 13 →](MANUSCRIPT.md#lesson-13)

<a id="lesson-13"></a>

### Lesson 13 — Backup provenance, freshness and recovery objectives

**Chapter 3, day 3.** [Read the complete lesson](MANUSCRIPT.md#lesson-13). Its teaching develops backup provenance, freshness and recovery objectives, includes a worked checkpoint and assigns EX033, EX034. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 13 of at least 20:** [← Lesson 12](MANUSCRIPT.md#lesson-12) · [Course lesson index](../SUBJECTS.md) · [Lesson 14 →](MANUSCRIPT.md#lesson-14)

<a id="lesson-14"></a>

### Lesson 14 — Evidence-linked recovery decision records

**Chapter 3, day 4.** [Read the complete lesson](MANUSCRIPT.md#lesson-14). Its teaching develops evidence-linked recovery decision records, includes a worked checkpoint and assigns EX035, EX036. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 14 of at least 20:** [← Lesson 13](MANUSCRIPT.md#lesson-13) · [Course lesson index](../SUBJECTS.md) · [Lesson 15 →](MANUSCRIPT.md#lesson-15)

<a id="lesson-15"></a>

### Lesson 15 — Queue reconciliation before return to service

**Chapter 3, day 5.** [Read the complete lesson](MANUSCRIPT.md#lesson-15). Its teaching develops queue reconciliation before return to service, includes a worked checkpoint and assigns EX037, EX038. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 15 of at least 20:** [← Lesson 14](MANUSCRIPT.md#lesson-14) · [Course lesson index](../SUBJECTS.md) · [Lesson 16 →](MANUSCRIPT.md#lesson-16)

### Continue studying — chapter 03 of 04

[← Chapter 02](#ch-02) · [Course lesson index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

<a id="ch-04"></a>

## Chapter 04 — Guided incident simulation and after-action review

**Instructional week 4.** Five daily lessons follow. The chapter may be expanded when the subject demands more depth.

<a id="lesson-16"></a>

### Lesson 16 — Release-aware tabletop and scored handoff

**Chapter 4, day 1.** [Read the complete lesson](MANUSCRIPT.md#lesson-16). Its teaching develops release-aware tabletop and scored handoff, includes a worked checkpoint and assigns EX039, EX040, EX041, EX042. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 16 of at least 20:** [← Lesson 15](MANUSCRIPT.md#lesson-15) · [Course lesson index](../SUBJECTS.md) · [Lesson 17 →](MANUSCRIPT.md#lesson-17)

<a id="lesson-17"></a>

### Lesson 17 — After-action review and unavailable-approver branch

**Chapter 4, day 2.** [Read the complete lesson](MANUSCRIPT.md#lesson-17). Its teaching develops after-action review and unavailable-approver branch, includes a worked checkpoint and assigns EX043, EX044, EX045, EX046. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 17 of at least 20:** [← Lesson 16](MANUSCRIPT.md#lesson-16) · [Course lesson index](../SUBJECTS.md) · [Lesson 18 →](MANUSCRIPT.md#lesson-18)

<a id="lesson-18"></a>

### Lesson 18 — Frozen evidence, communication and improvement closure

**Chapter 4, day 3.** [Read the complete lesson](MANUSCRIPT.md#lesson-18). Its teaching develops frozen evidence, communication and improvement closure, includes a worked checkpoint and assigns EX047, EX049. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 18 of at least 20:** [← Lesson 17](MANUSCRIPT.md#lesson-17) · [Course lesson index](../SUBJECTS.md) · [Lesson 19 →](MANUSCRIPT.md#lesson-19)

<a id="lesson-19"></a>

### Lesson 19 — Message delivery and read-back as separate gates

**Chapter 4, day 4.** [Read the complete lesson](MANUSCRIPT.md#lesson-19). Its teaching develops message delivery and read-back as separate gates, includes a worked checkpoint and assigns EX048. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 19 of at least 20:** [← Lesson 18](MANUSCRIPT.md#lesson-18) · [Course lesson index](../SUBJECTS.md) · [Lesson 20 →](MANUSCRIPT.md#lesson-20)

<a id="lesson-20"></a>

### Lesson 20 — Blind handoff and independent reconstruction

**Chapter 4, day 5.** [Read the complete lesson](MANUSCRIPT.md#lesson-20). Its teaching develops blind handoff and independent reconstruction, includes a worked checkpoint and assigns EX050. Attempt the prompts in the lesson before reading their final results.

**Continue studying — lesson 20 of at least 20:** [← Lesson 19](MANUSCRIPT.md#lesson-19) · [Course lesson index](../SUBJECTS.md) · [Next course via lesson index →](../SUBJECTS.md)

## Primary source starting points

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — incident response in cybersecurity risk management.
- [NIST SP 800-184](https://csrc.nist.gov/pubs/sp/800/184/final) — recovery planning, tests and improvement.
- [NIST SP 800-84](https://csrc.nist.gov/pubs/sp/800/84/final) — exercise design and evaluation; review its age and scope before applying details.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) — forensic techniques; verify older technical details against current practice.

Harbor Library and all R-series classroom records are synthetic. Follow the manuscript citations for claims about real sources. The plan is not evidence of an accredited program or an approved complete book.

### Continue studying — chapter 04 of 04

[← Chapter 03](#ch-03) · [Course lesson index](../SUBJECTS.md) · [Next course via lesson index →](../SUBJECTS.md)
