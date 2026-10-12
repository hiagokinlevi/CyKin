# OT, IoT and Cyber-Physical Security: Postgraduate Practice and Applied Project

- Language: English (`en`); postgraduate course, two years; approximately 1,200 hours planned.
- Editorial state: **draft**. Chapters 1–12 authored; EX001–EX060 with worked results; Lab 6 verified. Review and A4 verification open.
- Audience: practitioners deepening OT/IIoT/CPS security judgment for plant decisions.
- Neighbours: engineering OT builds systems; master's OT designs studies; **this book** trains advanced practice, evaluation and organisational integration on the synthetic **Bayside Water Reclamation Plant (BWRP)**.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). [CC0 1.0](../../../../../LICENSE) for original text.
- Boundary: not an accredited award; no production access; synthetic unless cited.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## Contents

1. [Advanced security decision-making](#ch-01)
2. [OT, IoT and cyber-physical security: current practice](#ch-02)
3. [OT, IoT and cyber-physical security: specialist evidence](#ch-03)
4. [Advanced risk and ethics](#ch-04)
5. [OT, IoT and cyber-physical security: design alternatives](#ch-05)
6. [OT, IoT and cyber-physical security: controlled evaluation](#ch-06)
7. [OT, IoT and cyber-physical security: organizational integration](#ch-07)
8. [OT, IoT and cyber-physical security: difficult cases](#ch-08)
9. [OT, IoT and cyber-physical security: leadership and assurance](#ch-09)
10. [Research reading and critique](#ch-10)
11. [Applied project](#ch-11)
12. [Final review and transfer](#ch-12)
13. [Worked results](#worked-results)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes and connection

After this chapter you can apply **Advanced security decision-making** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 1.1 Decisions under physical constraint

Postgraduate OT work is decision work: accept residual risk, choose a zone boundary, freeze a detector threshold, postpone a patch because a batch is running. Every decision needs options, evidence, a consequence unit in physical terms (litres spilled, batches scrapped, hours of local-only operation), and an owner.

### 1.2 A decision record

Write: context; options; evaluation criteria (safety, availability, detectability, operability, cost); evidence; decision; residual risk; review date. The synthetic **Bayside Water Reclamation Plant (BWRP)** Control Hardening Board uses this template for every CNHP-equivalent change.

### 1.3 Common failure

Deciding from a vendor slide without a plant-specific consequence unit. Another: deciding in IT change advisory without an OT engineer who can veto on scan-time or safety grounds.

### 1.4 Worked example

BWRP must choose whether engineering access to PLC-A uses a jump host with MFA or a direct VPN. Criteria favour jump host on reachability reduction; residual risk is vendor emergency access delay — owned by operations manager with a break-glass procedure tested quarterly.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 1

**EX001** — *Objective:* apply chapter 1 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX002** — *Objective:* apply chapter 1 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX003** — *Objective:* apply chapter 1 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX004** — *Objective:* apply chapter 1 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX005** — *Objective:* apply chapter 1 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Advanced security decision-making improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — OT, IoT and cyber-physical security: current practice

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: current practice** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 2.1 Current practice landscape

Plants mix decades-old Modbus devices, newer OPC UA, cellular IIoT sensors and cloud historians. NIST SP 800-82 Rev. 3 and ISA/IEC 62443 are the usual anchors; ATT&CK for ICS frames adversary behaviour. Air gaps are rarer than slides claim.

### 2.2 What "good" looks like in practice

Inventory that includes serial and wireless; zone map with conduit allow-lists; engineering access brokered; backups of PLC projects restored in drill; detection that includes process invariants; SIS independence respected.

### 2.3 Gaps you will meet

Shared operator accounts; flat level-2 networks; vendors with standing VPN; detectors tuned to silence; safety bypasses left open. Your job is to prioritise by consequence, not by novelty.

### 2.4 Worked example

BWRP inventory finds three undocumented cellular modems on clarifier instruments. Decision: inventory, firewall, and replace standing connections with brokered sessions — before buying a new SOC use case.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 2

**EX006** — *Objective:* apply chapter 2 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX007** — *Objective:* apply chapter 2 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX008** — *Objective:* apply chapter 2 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX009** — *Objective:* apply chapter 2 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX010** — *Objective:* apply chapter 2 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: current practice improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 02 of 12

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — OT, IoT and cyber-physical security: specialist evidence

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: specialist evidence** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 3.1 Specialist evidence types

Process data, network captures from span ports, PLC project diffs, alarm histories, HAZOP worksheets, and public advisories. Each has bias: captures miss serial; projects lag as-built; advisories omit your configuration.

### 3.2 Reading detection papers

Demand adversary model, threshold discipline, event-level metrics, impact at detection, and second-context validation. Point-adjusted F1 alone is insufficient (Arp et al.; OT-specific impact metrics from Urbina et al.).

### 3.3 Incident evidence

Use public reports at their fidelity. Manipulation of view and SIS targeting are documented classes; do not invent operational detail.

### 3.4 Worked example

A vendor claims "99% anomaly accuracy" on BWRP. Appraisal checklist fails: no event delay, thresholds not frozen, no class B test. Procurement requires a controlled evaluation (Chapter 6).

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 3

**EX011** — *Objective:* apply chapter 3 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX012** — *Objective:* apply chapter 3 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX013** — *Objective:* apply chapter 3 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX014** — *Objective:* apply chapter 3 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX015** — *Objective:* apply chapter 3 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: specialist evidence improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 03 of 12

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes and connection

After this chapter you can apply **Advanced risk and ethics** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 4.1 Risk in OT units

Likelihood × consequence fails if consequence is "IT impact". Use physical units and safety severity. Include adversary capability classes (casual, intentional, nation-state) as in 62443 SL thinking — as hypotheses, not labels on real actors.

### 4.2 Ethics

Menlo principles; never test on production; dual-use review before publishing evasion detail; justice for under-resourced utilities who cannot patch quickly.

### 4.3 Risk acceptance

A signed acceptance for an unauthenticated protocol on an isolated skid must name the owner, expiry and compensating controls (physical access, monitoring).

### 4.4 Worked example

BWRP accepts Modbus on a local skid inside a locked cabinet with serial-only and a residual monitor on the downstream flow — reviewed annually.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 4

**EX016** — *Objective:* apply chapter 4 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX017** — *Objective:* apply chapter 4 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX018** — *Objective:* apply chapter 4 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX019** — *Objective:* apply chapter 4 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX020** — *Objective:* apply chapter 4 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Advanced risk and ethics improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 04 of 12

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — OT, IoT and cyber-physical security: design alternatives

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: design alternatives** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 5.1 Alternatives to compare

Flat network; Purdue+DMZ; Purdue+unidirectional gateway for historian export; micro-segmented level 1. Score reachability to SIS, operability of engineering access, cost and alarm load.

### 5.2 Detection alternatives

Band alarms only; network IDS; residual CUSUM; vendor ML appliance. Compare with frozen thresholds and class A/B attacks on a model before a pilot.

### 5.3 Worked example

BWRP shortlists residual CUSUM + jump host + zoned conduits. Unidirectional gateway deferred: recipe upload still needs a bidirectional engineering path with stronger brokerage.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 5

**EX021** — *Objective:* apply chapter 5 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX022** — *Objective:* apply chapter 5 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX023** — *Objective:* apply chapter 5 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX024** — *Objective:* apply chapter 5 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX025** — *Objective:* apply chapter 5 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: design alternatives improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 05 of 12

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — OT, IoT and cyber-physical security: controlled evaluation

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: controlled evaluation** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 6.1 Controlled evaluation

Freeze thresholds; define attack classes; report event recall, delay, false alarms per shift, overfill at alarm; include failure class B.

### 6.2 Lab 6

```python
'''+lab6+'''
```

Expected output:

```text
frozen k=0.8
band A FA=0/70 det=0/70 delay=nan
band B FA=0/70 det=0/70 delay=nan
cusum A FA=0/70 det=70/70 delay=32.5
cusum B FA=0/70 det=0/70 delay=nan
```

(Exact delay may vary slightly with platform float; detect counts and FA must match.)

### 6.3 Interpreting results

CUSUM wins on class A; both fail on class B — architectural requirement for independent sensing remains.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 6

**EX026** — *Objective:* apply chapter 6 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX027** — *Objective:* apply chapter 6 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX028** — *Objective:* apply chapter 6 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX029** — *Objective:* apply chapter 6 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX030** — *Objective:* apply chapter 6 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: controlled evaluation improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 06 of 12

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — OT, IoT and cyber-physical security: organizational integration

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: organizational integration** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 7.1 Integration points

OT security fails when it is a side project. Integrate with operations (alarm philosophy), maintenance (change windows), safety (MOC for cyber changes), and IT (identity, vulnerability management) without letting IT patch windows break validated builds.

### 7.2 RACI for conduits

Every conduit has an owner who can approve allow-list changes. Engineering access is a controlled activity, not a standing privilege.

### 7.3 Worked example

BWRP adds cyber alarms to the same priority scheme as process alarms; residual-high is priority 2 with a defined response.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 7

**EX031** — *Objective:* apply chapter 7 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX032** — *Objective:* apply chapter 7 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX033** — *Objective:* apply chapter 7 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX034** — *Objective:* apply chapter 7 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX035** — *Objective:* apply chapter 7 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: organizational integration improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 07 of 12

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — OT, IoT and cyber-physical security: difficult cases

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: difficult cases** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 8.1 Difficult cases

Legacy controllers that cannot authenticate; vendor-only diagnostic protocols; safety system patching; ransomware on the engineering workstation; suspected compromise during a batch.

### 8.2 Playbooks

Contain without unsafe shutdown; preserve evidence; escalate to safety officer when trips are involved; communicate to customers if quality may be affected.

### 8.3 Worked example

Suspected replay on T-1: run local, enable residual monitor, capture span, do not rewrite PLC logic until impact assessed.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 8

**EX036** — *Objective:* apply chapter 8 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX037** — *Objective:* apply chapter 8 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX038** — *Objective:* apply chapter 8 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX039** — *Objective:* apply chapter 8 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX040** — *Objective:* apply chapter 8 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: difficult cases improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 08 of 12

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — OT, IoT and cyber-physical security: leadership and assurance

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: leadership and assurance** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 9.1 Assurance arguments

Claim → evidence → residual risk. Assurance cases for CNHP-like programmes cite tests, drills and independent reviews.

### 9.2 Leadership behaviours

Stop-work authority for unsafe cyber tests; funding for independent sensors; refusing vanity metrics.

### 9.3 Worked example

Plant manager rejects a dashboard that shows only "threats blocked" without false-alarm and delay metrics.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 9

**EX041** — *Objective:* apply chapter 9 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX042** — *Objective:* apply chapter 9 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX043** — *Objective:* apply chapter 9 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX044** — *Objective:* apply chapter 9 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX045** — *Objective:* apply chapter 9 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

OT, IoT and cyber-physical security: leadership and assurance improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 09 of 12

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes and connection

After this chapter you can apply **Research reading and critique** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 10.1 Critique method

Summarise claim, method, data, adversary model, metrics, limits. Score against the checklist in Chapter 3.

### 10.2 Replication mindset

Can you reimplement enough to test the headline number? If not, the paper is not yet engineering evidence.

### 10.3 Worked example

Critique a fictional paper claiming ML detection on a public water dataset with point-adjusted F1 0.99 — rewrite what it can support.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 10

**EX046** — *Objective:* apply chapter 10 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX047** — *Objective:* apply chapter 10 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX048** — *Objective:* apply chapter 10 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX049** — *Objective:* apply chapter 10 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX050** — *Objective:* apply chapter 10 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Research reading and critique improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 10 of 12

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes and connection

After this chapter you can apply **Applied project** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 11.1 Project scope

Deliver for BWRP: zone map, five requirements, controlled evaluation report (Lab 6), residual-risk register, operator brief.

### 11.2 Boundaries

Synthetic or authorised lab only; no production scanning; dual-use review on any evasion discussion.

### 11.3 Milestones

Proposal; design; evaluation; dossier; transfer briefing.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.


Deliverables must include a requirements trace to tests, a residual-risk register with owners and review dates, and an operator brief that states what is high / medium / unknown confidence. Cap the project if safety bounds cannot be met.
### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 11

**EX051** — *Objective:* apply chapter 11 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX052** — *Objective:* apply chapter 11 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX053** — *Objective:* apply chapter 11 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX054** — *Objective:* apply chapter 11 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX055** — *Objective:* apply chapter 11 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Applied project improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 11 of 12

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes and connection

After this chapter you can apply **Final review and transfer** to OT decisions on synthetic BWRP with explicit consequence units, evidence and residual-risk ownership. It connects prior postgraduate chapters to the applied project.

### 12.1 Transfer

What operations must do Monday: brokered engineering access; residual monitor on critical tanks; class B acknowledged as architectural gap.

### 12.2 Personal competence map

Skills gained vs gaps (e.g., functional safety certification pathways outside this course).

### 12.3 Worked example

One-page transfer brief with confidence levels: high for class A detection in model; medium for zoned reachability; none for dual-sensor attacker without independent wiring.

### Postgraduate practice note

State the physical consequence unit for every recommendation. Separate observation from claim. Freeze evaluation thresholds before validation data are examined. Never direct work against production OT. Label BWRP and all lab numbers synthetic. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS versions before field use. Prefer event recall, delay, false alarms per shift and impact at detection over single aggregate accuracy scores.

### Depth for postgraduate practice

Spell out the physical consequence unit (overflow volume, off-spec batches, hours on local control, spurious SIS trips) before ranking options. Write observation / inference / claim / decision / physical consequence labels on every evidence note. Freeze detector thresholds and allow-lists before examining validation traces. Integrate operations, maintenance and safety change control so cyber changes cannot bypass management of change. Treat ATT&CK for ICS techniques as capability hypotheses, not frequencies. Prefer event recall, detection delay, false alarms per shift and impact at detection when reading vendors or papers. Never authorise or assist production OT access from this course; use synthetic BWRP data or isolated labs with independent safety layers and stop authority. Re-verify NIST SP 800-82 Rev. 3, ISA/IEC 62443 and related standards by version before field use.

### Common errors and limits

- IT-only consequence units.
- Production testing.
- Vanity metrics without delay/FA/impact.
- Unowned residual risk.

### Exercises — chapter 12

**EX056** — *Objective:* apply chapter 12 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX057** — *Objective:* apply chapter 12 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX058** — *Objective:* apply chapter 12 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX059** — *Objective:* apply chapter 12 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.
**EX060** — *Objective:* apply chapter 12 to BWRP. *Steps:* produce a short artefact (decision record, checklist, critique, or calculation) with assumptions and residual-risk owner. *Evidence:* artefact. *Rubric:* 3 = scoped and owned; 2 = thin; 1 = vague; 0 = none.

### Chapter synthesis

Final review and transfer improves plant decisions only when physical consequences, frozen evaluations and owned residual risks are explicit. BWRP remains synthetic.

### Continue studying — chapter 12 of 12

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results)

<a id="worked-results"></a>

## Worked results


### Chapter 1

- **EX001** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX002** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX003** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX004** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX005** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 2

- **EX006** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX007** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX008** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX009** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX010** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 3

- **EX011** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX012** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX013** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX014** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX015** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 4

- **EX016** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX017** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX018** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX019** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX020** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 5

- **EX021** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX022** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX023** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX024** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX025** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 6

- **EX026** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX027** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX028** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX029** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX030** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 7

- **EX031** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX032** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX033** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX034** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX035** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 8

- **EX036** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX037** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX038** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX039** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX040** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 9

- **EX041** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX042** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX043** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX044** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX045** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 10

- **EX046** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX047** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX048** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX049** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX050** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 11

- **EX051** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX052** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX053** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX054** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX055** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

### Chapter 12

- **EX056** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX057** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX058** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX059** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.
- **EX060** — Artefact complete for BWRP with consequence unit, assumptions, evidence pointer and residual-risk owner; overclaims rewritten with scope.

**End of worked results.**
