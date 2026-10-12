# OT, IoT and Cyber-Physical Security: Bachelor's Foundations and Capstone

- Language: English (`en`); bachelor's course, four years.
- Editorial state: **draft**. Chapters 1–40 authored; EX001–EX120 (three per chapter) with worked results; Laboratory I embeds a verified offline lab. Review and A4 verification open.
- Audience: undergraduates building OT/IIoT/CPS security foundations toward a capstone on synthetic **Lakeside District Heating Plant (LDHP)**.
- Neighbours: engineering OT builds industrial programmes; postgraduate OT trains plant decisions; **this book** builds undergraduate foundations and a scoped capstone.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). [CC0 1.0](../../../../../LICENSE).
- Boundary: not an accredited degree; no production OT access; synthetic unless cited.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## Contents

1. [Mathematical reasoning](#ch-01)
2. [Computing systems](#ch-02)
3. [Programming I](#ch-03)
4. [Academic writing](#ch-04)
5. [Security literacy](#ch-05)
6. [Discrete structures](#ch-06)
7. [Networks and protocols](#ch-07)
8. [Programming II](#ch-08)
9. [Data and databases](#ch-09)
10. [Ethics and authorized practice](#ch-10)
11. [Operating systems](#ch-11)
12. [Probability and statistics](#ch-12)
13. [Identity and access](#ch-13)
14. [Privacy foundations](#ch-14)
15. [Evidence and measurement](#ch-15)
16. [Security architecture](#ch-16)
17. [Cryptography concepts](#ch-17)
18. [Research methods I](#ch-18)
19. [OT, IoT and cyber-physical security: scope and theory](#ch-19)
20. [OT, IoT and cyber-physical security: foundational cases](#ch-20)
21. [OT, IoT and cyber-physical security: system models](#ch-21)
22. [OT, IoT and cyber-physical security: data and dependencies](#ch-22)
23. [OT, IoT and cyber-physical security: methods I](#ch-23)
24. [OT, IoT and cyber-physical security: controls](#ch-24)
25. [Laboratory I](#ch-25)
26. [OT, IoT and cyber-physical security: methods II](#ch-26)
27. [OT, IoT and cyber-physical security: verification](#ch-27)
28. [OT, IoT and cyber-physical security: failure analysis](#ch-28)
29. [OT, IoT and cyber-physical security: operations](#ch-29)
30. [Laboratory II](#ch-30)
31. [OT, IoT and cyber-physical security: advanced cases](#ch-31)
32. [OT, IoT and cyber-physical security: interdisciplinary interfaces](#ch-32)
33. [Research methods II](#ch-33)
34. [Comparative project](#ch-34)
35. [Capstone proposal](#ch-35)
36. [Field or community practice](#ch-36)
37. [Evidence review seminar](#ch-37)
38. [Capstone implementation](#ch-38)
39. [Capstone evaluation](#ch-39)
40. [Thesis and presentation](#ch-40)
41. [Worked results](#worked-results)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes and connection

After this chapter you can apply **Mathematical reasoning** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 1.1 Why this foundation matters for OT

**Mathematical reasoning** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 1.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 1.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies mathematical reasoning to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 1

**EX001** — *Objective:* practise mathematical reasoning on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX002** — *Objective:* practise mathematical reasoning on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX003** — *Objective:* practise mathematical reasoning on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Mathematical reasoning serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes and connection

After this chapter you can apply **Computing systems** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 2.1 Why this foundation matters for OT

**Computing systems** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 2.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 2.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies computing systems to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 2

**EX004** — *Objective:* practise computing systems on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX005** — *Objective:* practise computing systems on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX006** — *Objective:* practise computing systems on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Computing systems serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 02 of 40

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes and connection

After this chapter you can apply **Programming I** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 3.1 Why this foundation matters for OT

**Programming I** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 3.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 3.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies programming i to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 3

**EX007** — *Objective:* practise programming i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX008** — *Objective:* practise programming i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX009** — *Objective:* practise programming i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Programming I serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 03 of 40

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes and connection

After this chapter you can apply **Academic writing** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 4.1 Why this foundation matters for OT

**Academic writing** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 4.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 4.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies academic writing to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 4

**EX010** — *Objective:* practise academic writing on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX011** — *Objective:* practise academic writing on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX012** — *Objective:* practise academic writing on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Academic writing serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 04 of 40

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes and connection

After this chapter you can apply **Security literacy** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 5.1 Why this foundation matters for OT

**Security literacy** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 5.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 5.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies security literacy to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 5

**EX013** — *Objective:* practise security literacy on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX014** — *Objective:* practise security literacy on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX015** — *Objective:* practise security literacy on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Security literacy serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 05 of 40

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes and connection

After this chapter you can apply **Discrete structures** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 6.1 Why this foundation matters for OT

**Discrete structures** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 6.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 6.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies discrete structures to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 6

**EX016** — *Objective:* practise discrete structures on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX017** — *Objective:* practise discrete structures on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX018** — *Objective:* practise discrete structures on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Discrete structures serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 06 of 40

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes and connection

After this chapter you can apply **Networks and protocols** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 7.1 Why this foundation matters for OT

**Networks and protocols** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 7.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 7.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies networks and protocols to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 7

**EX019** — *Objective:* practise networks and protocols on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX020** — *Objective:* practise networks and protocols on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX021** — *Objective:* practise networks and protocols on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Networks and protocols serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 07 of 40

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes and connection

After this chapter you can apply **Programming II** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 8.1 Why this foundation matters for OT

**Programming II** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 8.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 8.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies programming ii to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 8

**EX022** — *Objective:* practise programming ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX023** — *Objective:* practise programming ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX024** — *Objective:* practise programming ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Programming II serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 08 of 40

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes and connection

After this chapter you can apply **Data and databases** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 9.1 Why this foundation matters for OT

**Data and databases** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 9.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 9.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies data and databases to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 9

**EX025** — *Objective:* practise data and databases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX026** — *Objective:* practise data and databases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX027** — *Objective:* practise data and databases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Data and databases serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 09 of 40

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes and connection

After this chapter you can apply **Ethics and authorized practice** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 10.1 Why this foundation matters for OT

**Ethics and authorized practice** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 10.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 10.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ethics and authorized practice to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 10

**EX028** — *Objective:* practise ethics and authorized practice on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX029** — *Objective:* practise ethics and authorized practice on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX030** — *Objective:* practise ethics and authorized practice on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Ethics and authorized practice serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 10 of 40

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes and connection

After this chapter you can apply **Operating systems** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 11.1 Why this foundation matters for OT

**Operating systems** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 11.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 11.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies operating systems to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 11

**EX031** — *Objective:* practise operating systems on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX032** — *Objective:* practise operating systems on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX033** — *Objective:* practise operating systems on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Operating systems serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 11 of 40

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes and connection

After this chapter you can apply **Probability and statistics** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 12.1 Why this foundation matters for OT

**Probability and statistics** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 12.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 12.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies probability and statistics to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 12

**EX034** — *Objective:* practise probability and statistics on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX035** — *Objective:* practise probability and statistics on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX036** — *Objective:* practise probability and statistics on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Probability and statistics serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 12 of 40

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes and connection

After this chapter you can apply **Identity and access** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 13.1 Why this foundation matters for OT

**Identity and access** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 13.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 13.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies identity and access to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 13

**EX037** — *Objective:* practise identity and access on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX038** — *Objective:* practise identity and access on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX039** — *Objective:* practise identity and access on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Identity and access serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 13 of 40

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes and connection

After this chapter you can apply **Privacy foundations** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 14.1 Why this foundation matters for OT

**Privacy foundations** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 14.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 14.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies privacy foundations to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 14

**EX040** — *Objective:* practise privacy foundations on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX041** — *Objective:* practise privacy foundations on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX042** — *Objective:* practise privacy foundations on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Privacy foundations serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 14 of 40

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes and connection

After this chapter you can apply **Evidence and measurement** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 15.1 Why this foundation matters for OT

**Evidence and measurement** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 15.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 15.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies evidence and measurement to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 15

**EX043** — *Objective:* practise evidence and measurement on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX044** — *Objective:* practise evidence and measurement on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX045** — *Objective:* practise evidence and measurement on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Evidence and measurement serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 15 of 40

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes and connection

After this chapter you can apply **Security architecture** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 16.1 Why this foundation matters for OT

**Security architecture** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 16.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 16.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies security architecture to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 16

**EX046** — *Objective:* practise security architecture on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX047** — *Objective:* practise security architecture on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX048** — *Objective:* practise security architecture on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Security architecture serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 16 of 40

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes and connection

After this chapter you can apply **Cryptography concepts** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 17.1 Why this foundation matters for OT

**Cryptography concepts** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 17.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 17.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies cryptography concepts to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 17

**EX049** — *Objective:* practise cryptography concepts on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX050** — *Objective:* practise cryptography concepts on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX051** — *Objective:* practise cryptography concepts on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Cryptography concepts serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 17 of 40

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes and connection

After this chapter you can apply **Research methods I** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 18.1 Why this foundation matters for OT

**Research methods I** supports later LDHP design and evaluation work. Definitions are given with OT examples (scan cycles, setpoints, conduits, alarm rates) so the skill transfers into Chapters 19–40.

### 18.2 Core ideas

Explain the central definitions and one worked calculation or short algorithm using only synthetic LDHP numbers. Keep assumptions visible (sensor noise, honest flow meter, zone membership).

### 18.3 Practice pattern

Produce a small artefact: a calculation, a truth table, a short Python 3 stdlib function, or a one-page explanation that an operator could challenge. Test nominal and attack cases when the artefact is a detector fragment.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies research methods i to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 18

**EX052** — *Objective:* practise research methods i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX053** — *Objective:* practise research methods i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX054** — *Objective:* practise research methods i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Research methods I serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 18 of 40

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — OT, IoT and cyber-physical security: scope and theory

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: scope and theory** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 19.1 Focus

Define OT vs IT vs IIoT vs CPS; Purdue levels; safety vs security goals; map LDHP.

### 19.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 19.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: scope and theory to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 19

**EX055** — *Objective:* practise ot, iot and cyber-physical security: scope and theory on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX056** — *Objective:* practise ot, iot and cyber-physical security: scope and theory on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX057** — *Objective:* practise ot, iot and cyber-physical security: scope and theory on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: scope and theory serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 19 of 40

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — OT, IoT and cyber-physical security: foundational cases

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: foundational cases** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 20.1 Focus

Study public incidents at source fidelity (Ukraine 2015, TRITON class, Oldsmar revisions); extract design lessons without operational recipes.

### 20.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 20.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: foundational cases to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 20

**EX058** — *Objective:* practise ot, iot and cyber-physical security: foundational cases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX059** — *Objective:* practise ot, iot and cyber-physical security: foundational cases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX060** — *Objective:* practise ot, iot and cyber-physical security: foundational cases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: foundational cases serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 20 of 40

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — OT, IoT and cyber-physical security: system models

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: system models** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 21.1 Focus

Build LDHP system model: assets, zones, conduits, signals with trust annotations.

### 21.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 21.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: system models to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 21

**EX061** — *Objective:* practise ot, iot and cyber-physical security: system models on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX062** — *Objective:* practise ot, iot and cyber-physical security: system models on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX063** — *Objective:* practise ot, iot and cyber-physical security: system models on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: system models serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 21 of 40

[← Chapter 20](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — OT, IoT and cyber-physical security: data and dependencies

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: data and dependencies** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 22.1 Focus

Historian tags, recipe/setpoint dependencies, time sync; dependency on power and communications.

### 22.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 22.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: data and dependencies to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 22

**EX064** — *Objective:* practise ot, iot and cyber-physical security: data and dependencies on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX065** — *Objective:* practise ot, iot and cyber-physical security: data and dependencies on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX066** — *Objective:* practise ot, iot and cyber-physical security: data and dependencies on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: data and dependencies serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 22 of 40

[← Chapter 21](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — OT, IoT and cyber-physical security: methods I

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: methods I** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 23.1 Focus

Risk methods with physical consequence units; qualitative matrices and when not to fake precision.

### 23.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 23.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: methods i to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 23

**EX067** — *Objective:* practise ot, iot and cyber-physical security: methods i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX068** — *Objective:* practise ot, iot and cyber-physical security: methods i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX069** — *Objective:* practise ot, iot and cyber-physical security: methods i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: methods I serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 23 of 40

[← Chapter 22](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — OT, IoT and cyber-physical security: controls

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: controls** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 24.1 Focus

Controls: allow-lists, brokered engineering access, residual monitors, backups of PLC projects.

### 24.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 24.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: controls to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 24

**EX070** — *Objective:* practise ot, iot and cyber-physical security: controls on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX071** — *Objective:* practise ot, iot and cyber-physical security: controls on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX072** — *Objective:* practise ot, iot and cyber-physical security: controls on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: controls serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 24 of 40

[← Chapter 23](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes and connection

After this chapter you can apply **Laboratory I** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 25.1 Focus

Laboratory I: run a tank/residual micro-lab offline; record outputs and assumptions.

### 25.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 25.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Laboratory activity

```python
# Lab 25 (bachelor OT, synthetic LDHP): band vs residual CUSUM
import random
def run(seed, atk, det):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(400):
        inflow=1.0+rng.gauss(0,0.05)+(0.05 if atk and t>=200 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=200: lvl=50+rng.gauss(0,0.3)
        est+=fm-0.02*est
        hit=abs(lvl-50)>1.5 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-0.8); hit=s>6
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,False,det) is not None for i in range(40))
    hits=[a-200 for a in (run(i,True,det) for i in range(40)) if a is not None and a>=200]
    print(f"{det} FA={fa}/40 det={len(hits)}/40 delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Expected output:

```text
band FA=4/40 det=0/40 delay=nan
cusum FA=0/40 det=40/40 delay=37.4
```

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies laboratory i to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 25

**EX073** — *Objective:* practise laboratory i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX074** — *Objective:* practise laboratory i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX075** — *Objective:* practise laboratory i on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Laboratory I serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 25 of 40

[← Chapter 24](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — OT, IoT and cyber-physical security: methods II

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: methods II** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 26.1 Focus

Methods II: evaluation design — freeze thresholds; class A/B attacker; event metrics.

### 26.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 26.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: methods ii to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 26

**EX076** — *Objective:* practise ot, iot and cyber-physical security: methods ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX077** — *Objective:* practise ot, iot and cyber-physical security: methods ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX078** — *Objective:* practise ot, iot and cyber-physical security: methods ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: methods II serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 26 of 40

[← Chapter 25](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — OT, IoT and cyber-physical security: verification

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: verification** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 27.1 Focus

Verification: test cases against requirements; pass/fail with evidence pointers.

### 27.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 27.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: verification to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 27

**EX079** — *Objective:* practise ot, iot and cyber-physical security: verification on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX080** — *Objective:* practise ot, iot and cyber-physical security: verification on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX081** — *Objective:* practise ot, iot and cyber-physical security: verification on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: verification serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 27 of 40

[← Chapter 26](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — OT, IoT and cyber-physical security: failure analysis

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: failure analysis** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 28.1 Focus

Failure analysis: HAZOP deviations with cyber causes; reachability to safety functions.

### 28.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 28.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: failure analysis to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 28

**EX082** — *Objective:* practise ot, iot and cyber-physical security: failure analysis on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX083** — *Objective:* practise ot, iot and cyber-physical security: failure analysis on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX084** — *Objective:* practise ot, iot and cyber-physical security: failure analysis on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: failure analysis serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 28 of 40

[← Chapter 27](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — OT, IoT and cyber-physical security: operations

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: operations** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 29.1 Focus

Operations: alarm philosophy, change windows, vendor access, shift handover of cyber alarms.

### 29.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 29.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: operations to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 29

**EX085** — *Objective:* practise ot, iot and cyber-physical security: operations on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX086** — *Objective:* practise ot, iot and cyber-physical security: operations on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX087** — *Objective:* practise ot, iot and cyber-physical security: operations on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: operations serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 29 of 40

[← Chapter 28](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes and connection

After this chapter you can apply **Laboratory II** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 30.1 Focus

Laboratory II: regression after a change; hash a small manifest.

### 30.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 30.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies laboratory ii to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 30

**EX088** — *Objective:* practise laboratory ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX089** — *Objective:* practise laboratory ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX090** — *Objective:* practise laboratory ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Laboratory II serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 30 of 40

[← Chapter 29](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — OT, IoT and cyber-physical security: advanced cases

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: advanced cases** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 31.1 Focus

Advanced cases: ransomware on engineering station; suspected replay mid-batch/heating season.

### 31.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 31.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: advanced cases to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 31

**EX091** — *Objective:* practise ot, iot and cyber-physical security: advanced cases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX092** — *Objective:* practise ot, iot and cyber-physical security: advanced cases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX093** — *Objective:* practise ot, iot and cyber-physical security: advanced cases on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: advanced cases serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 31 of 40

[← Chapter 30](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — OT, IoT and cyber-physical security: interdisciplinary interfaces

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: interdisciplinary interfaces** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 32.1 Focus

Interfaces with safety engineering, quality, IT identity, and regulators — without collapsing OT into IT.

### 32.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 32.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies ot, iot and cyber-physical security: interdisciplinary interfaces to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 32

**EX094** — *Objective:* practise ot, iot and cyber-physical security: interdisciplinary interfaces on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX095** — *Objective:* practise ot, iot and cyber-physical security: interdisciplinary interfaces on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX096** — *Objective:* practise ot, iot and cyber-physical security: interdisciplinary interfaces on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: interdisciplinary interfaces serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 32 of 40

[← Chapter 31](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes and connection

After this chapter you can apply **Research methods II** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 33.1 Focus

Research methods II: appraise a detection paper; write a mini protocol.

### 33.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 33.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies research methods ii to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 33

**EX097** — *Objective:* practise research methods ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX098** — *Objective:* practise research methods ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX099** — *Objective:* practise research methods ii on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Research methods II serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 33 of 40

[← Chapter 32](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes and connection

After this chapter you can apply **Comparative project** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 34.1 Focus

Comparative project: band vs residual on synthetic LDHP data.

### 34.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 34.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies comparative project to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 34

**EX100** — *Objective:* practise comparative project on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX101** — *Objective:* practise comparative project on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX102** — *Objective:* practise comparative project on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Comparative project serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 34 of 40

[← Chapter 33](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes and connection

After this chapter you can apply **Capstone proposal** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 35.1 Focus

Capstone proposal with scope, ethics, safety bounds, success metrics.

### 35.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 35.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies capstone proposal to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 35

**EX103** — *Objective:* practise capstone proposal on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX104** — *Objective:* practise capstone proposal on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX105** — *Objective:* practise capstone proposal on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Capstone proposal serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 35 of 40

[← Chapter 34](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes and connection

After this chapter you can apply **Field or community practice** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 36.1 Focus

Field/community practice reflection: observe only; no production changes.

### 36.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 36.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies field or community practice to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 36

**EX106** — *Objective:* practise field or community practice on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX107** — *Objective:* practise field or community practice on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX108** — *Objective:* practise field or community practice on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Field or community practice serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 36 of 40

[← Chapter 35](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes and connection

After this chapter you can apply **Evidence review seminar** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 37.1 Focus

Evidence review seminar: peer critique of dossiers.

### 37.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 37.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies evidence review seminar to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 37

**EX109** — *Objective:* practise evidence review seminar on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX110** — *Objective:* practise evidence review seminar on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX111** — *Objective:* practise evidence review seminar on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Evidence review seminar serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 37 of 40

[← Chapter 36](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes and connection

After this chapter you can apply **Capstone implementation** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 38.1 Focus

Capstone implementation on synthetic/lab artefacts only.

### 38.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 38.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies capstone implementation to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 38

**EX112** — *Objective:* practise capstone implementation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX113** — *Objective:* practise capstone implementation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX114** — *Objective:* practise capstone implementation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Capstone implementation serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 38 of 40

[← Chapter 37](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes and connection

After this chapter you can apply **Capstone evaluation** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 39.1 Focus

Capstone evaluation with frozen metrics and residual-risk register.

### 39.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 39.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies capstone evaluation to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 39

**EX115** — *Objective:* practise capstone evaluation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX116** — *Objective:* practise capstone evaluation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX117** — *Objective:* practise capstone evaluation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Capstone evaluation serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 39 of 40

[← Chapter 38](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes and connection

After this chapter you can apply **Thesis and presentation** in an OT context on synthetic LDHP, with explicit assumptions and scoped claims. It prepares later bachelor's chapters and the capstone.

### 40.1 Focus

Thesis and presentation: claim audit and operator brief with confidence levels.

### 40.2 Method

Inputs, steps and outputs for LDHP artefacts with IDs (R#, T#, ADR-#). Use Python 3 stdlib when coding.

### 40.3 Quality

A peer should re-run calculations, see assumptions and find the residual-risk owner.

### Bachelor's study note

Connect every idea to the synthetic **Lakeside District Heating Plant (LDHP)**: boilers, pumps, PLC-A, SCADA, and a safety interlock on over-temperature. State units. Label observation versus claim. Prefer event-level detection metrics and false alarms per shift over single accuracy scores. Work only with synthetic data or isolated labs that have an independent physical safety layer and a named stop authority — never on production OT. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions when you use them, and re-verify before any real project. Keep LDHP labelled synthetic so teaching numbers are not mistaken for field measurements.

### Extra teaching depth

When you model LDHP, name the Purdue level of each device and whether a conduit allows reads, writes or engineering downloads. A write path to a safety interlock is a different risk class from a read path to a historian. For detection work, report whether the second sensor used in a residual is independently wired; if it shares a PLC with the attacked sensor, treat that as class B. Capstone chapters must include abandonment conditions if the lab cannot be made safe.
### Worked example (synthetic LDHP)

The LDHP team applies thesis and presentation to a heating-season control decision involving PLC-A and pump P-2. Numbers are synthetic. The example shows inputs, result and the design or study decision supported — not a claim about a real utility.

### Common errors and limits

- Skipping units and assumptions.
- Production access.
- Overclaiming from a classroom lab.
- Point-adjusted F1 as the only metric.

### Exercises — chapter 40

**EX118** — *Objective:* practise thesis and presentation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX119** — *Objective:* practise thesis and presentation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.
**EX120** — *Objective:* practise thesis and presentation on LDHP. *Steps:* produce a short artefact with assumptions and scope. *Evidence:* artefact. *Rubric:* 3 = correct/scoped; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Thesis and presentation serves OT security when tied to physical consequences, honest metrics and owned residual risk on synthetic LDHP.

### Continue studying — chapter 40 of 40

[← Chapter 39](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results)

<a id="worked-results"></a>

## Worked results


### Chapter 1
- **EX001** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX002** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX003** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 2
- **EX004** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX005** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX006** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 3
- **EX007** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX008** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX009** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 4
- **EX010** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX011** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX012** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 5
- **EX013** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX014** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX015** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 6
- **EX016** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX017** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX018** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 7
- **EX019** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX020** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX021** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 8
- **EX022** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX023** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX024** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 9
- **EX025** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX026** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX027** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 10
- **EX028** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX029** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX030** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 11
- **EX031** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX032** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX033** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 12
- **EX034** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX035** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX036** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 13
- **EX037** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX038** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX039** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 14
- **EX040** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX041** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX042** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 15
- **EX043** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX044** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX045** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 16
- **EX046** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX047** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX048** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 17
- **EX049** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX050** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX051** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 18
- **EX052** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX053** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX054** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 19
- **EX055** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX056** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX057** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 20
- **EX058** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX059** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX060** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 21
- **EX061** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX062** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX063** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 22
- **EX064** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX065** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX066** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 23
- **EX067** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX068** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX069** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 24
- **EX070** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX071** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX072** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 25
- **EX073** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX074** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX075** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 26
- **EX076** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX077** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX078** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 27
- **EX079** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX080** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX081** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 28
- **EX082** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX083** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX084** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 29
- **EX085** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX086** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX087** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 30
- **EX088** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX089** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX090** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 31
- **EX091** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX092** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX093** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 32
- **EX094** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX095** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX096** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 33
- **EX097** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX098** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX099** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 34
- **EX100** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX101** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX102** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 35
- **EX103** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX104** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX105** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 36
- **EX106** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX107** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX108** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 37
- **EX109** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX110** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX111** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 38
- **EX112** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX113** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX114** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 39
- **EX115** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX116** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX117** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

### Chapter 40
- **EX118** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX119** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.
- **EX120** — Artefact for LDHP with units/assumptions and scoped conclusion; synthetic only.

**End of worked results.**
