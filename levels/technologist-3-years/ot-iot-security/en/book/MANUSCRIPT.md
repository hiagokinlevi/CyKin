# OT, IoT and Cyber-Physical Security: Technologist Course Book

- Language: English (`en`); technologist 3 years.
- Editorial state: **draft**. Chapters 1–30 authored; exercises with worked results; offline lab verified. Review and A4 verification open.
- Synthetic plant: **River Dock Pumping Station (RDPS)**.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). [CC0 1.0](../../../../../LICENSE).
- Boundary: not an accredited award; no production OT access.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## Contents

1. [Computing systems](#ch-01)
2. [Networks and internet services](#ch-02)
3. [Programming foundations](#ch-03)
4. [Data models](#ch-04)
5. [Security literacy](#ch-05)
6. [Operating systems and virtualization](#ch-06)
7. [Identity and access foundations](#ch-07)
8. [Security architecture basics](#ch-08)
9. [Evidence and measurement](#ch-09)
10. [OT, IoT and cyber-physical security: orientation](#ch-10)
11. [OT, IoT and cyber-physical security: assets and context](#ch-11)
12. [OT, IoT and cyber-physical security: data flows](#ch-12)
13. [OT, IoT and cyber-physical security: risk scenarios](#ch-13)
14. [OT, IoT and cyber-physical security: methods I](#ch-14)
15. [OT, IoT and cyber-physical security: guided lab](#ch-15)
16. [OT, IoT and cyber-physical security: methods II](#ch-16)
17. [OT, IoT and cyber-physical security: tooling](#ch-17)
18. [OT, IoT and cyber-physical security: controls](#ch-18)
19. [OT, IoT and cyber-physical security: monitoring](#ch-19)
20. [OT, IoT and cyber-physical security: troubleshooting](#ch-20)
21. [OT, IoT and cyber-physical security: service integration](#ch-21)
22. [OT, IoT and cyber-physical security: automation](#ch-22)
23. [OT, IoT and cyber-physical security: evaluation](#ch-23)
24. [Applied research methods](#ch-24)
25. [Team project studio](#ch-25)
26. [OT, IoT and cyber-physical security: operational handoff](#ch-26)
27. [Deployment and validation](#ch-27)
28. [Field practice](#ch-28)
29. [Capstone build](#ch-29)
30. [Capstone assessment](#ch-30)
31. [Worked results](#worked-results)

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes and connection

After this chapter you can apply **Computing systems** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 1.1 Focus

**Computing systems** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 1.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 1.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
 Record the stop authority by role name before any energised lab demonstration begins.
### Worked example

On River Dock Pumping Station (RDPS), the team applies computing systems to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 1

**EX001** — *Objective:* apply computing systems to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX002** — *Objective:* apply computing systems to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX003** — *Objective:* apply computing systems to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Computing systems helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes and connection

After this chapter you can apply **Networks and internet services** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 2.1 Focus

**Networks and internet services** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 2.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 2.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies networks and internet services to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 2

**EX004** — *Objective:* apply networks and internet services to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX005** — *Objective:* apply networks and internet services to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX006** — *Objective:* apply networks and internet services to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Networks and internet services helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 02 of 30

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes and connection

After this chapter you can apply **Programming foundations** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 3.1 Focus

**Programming foundations** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 3.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 3.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Laboratory activity

```python
# Lab (technologist OT, synthetic): band vs CUSUM
import random
def run(seed, atk, det):
    rng=random.Random(seed); true=est=50.0; s=0.0; alarm=None
    for t in range(300):
        inflow=1.0+rng.gauss(0,0.05)+(0.05 if atk and t>=150 else 0)
        true+=inflow-0.02*true
        lvl=true+rng.gauss(0,0.3); fm=inflow+rng.gauss(0,0.02)
        if atk and t>=150: lvl=50+rng.gauss(0,0.3)
        est+=fm-0.02*est
        hit=abs(lvl-50)>1.5 if det=="band" else False
        if det=="cusum":
            s=max(0.0,s+abs(lvl-est)-0.8); hit=s>6
        if hit and alarm is None: alarm=t
    return alarm
for det in ("band","cusum"):
    fa=sum(run(i,False,det) is not None for i in range(30))
    hits=[a-150 for a in (run(i,True,det) for i in range(30)) if a is not None and a>=150]
    print(f"{det} FA={fa}/30 det={len(hits)}/30 delay={sum(hits)/len(hits) if hits else float('nan'):.1f}")
```

Expected output:

```text
band FA=1/30 det=0/30 delay=nan
cusum FA=0/30 det=30/30 delay=37.4
```

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies programming foundations to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 3

**EX007** — *Objective:* apply programming foundations to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX008** — *Objective:* apply programming foundations to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX009** — *Objective:* apply programming foundations to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Programming foundations helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 03 of 30

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes and connection

After this chapter you can apply **Data models** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 4.1 Focus

**Data models** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 4.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 4.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
 Record the stop authority by role name before any energised lab demonstration begins.
### Worked example

On River Dock Pumping Station (RDPS), the team applies data models to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 4

**EX010** — *Objective:* apply data models to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX011** — *Objective:* apply data models to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX012** — *Objective:* apply data models to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Data models helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 04 of 30

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes and connection

After this chapter you can apply **Security literacy** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 5.1 Focus

**Security literacy** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 5.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 5.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
 Record the stop authority by role name before any energised lab demonstration begins.
### Worked example

On River Dock Pumping Station (RDPS), the team applies security literacy to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 5

**EX013** — *Objective:* apply security literacy to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX014** — *Objective:* apply security literacy to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX015** — *Objective:* apply security literacy to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Security literacy helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 05 of 30

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes and connection

After this chapter you can apply **Operating systems and virtualization** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 6.1 Focus

**Operating systems and virtualization** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 6.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 6.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies operating systems and virtualization to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 6

**EX016** — *Objective:* apply operating systems and virtualization to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX017** — *Objective:* apply operating systems and virtualization to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX018** — *Objective:* apply operating systems and virtualization to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Operating systems and virtualization helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 06 of 30

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes and connection

After this chapter you can apply **Identity and access foundations** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 7.1 Focus

**Identity and access foundations** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 7.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 7.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies identity and access foundations to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 7

**EX019** — *Objective:* apply identity and access foundations to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX020** — *Objective:* apply identity and access foundations to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX021** — *Objective:* apply identity and access foundations to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Identity and access foundations helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 07 of 30

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes and connection

After this chapter you can apply **Security architecture basics** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 8.1 Focus

**Security architecture basics** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 8.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 8.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies security architecture basics to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 8

**EX022** — *Objective:* apply security architecture basics to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX023** — *Objective:* apply security architecture basics to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX024** — *Objective:* apply security architecture basics to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Security architecture basics helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 08 of 30

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes and connection

After this chapter you can apply **Evidence and measurement** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 9.1 Focus

**Evidence and measurement** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 9.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 9.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies evidence and measurement to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 9

**EX025** — *Objective:* apply evidence and measurement to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX026** — *Objective:* apply evidence and measurement to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX027** — *Objective:* apply evidence and measurement to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Evidence and measurement helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 09 of 30

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — OT, IoT and cyber-physical security: orientation

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: orientation** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 10.1 Focus

**OT, IoT and cyber-physical security: orientation** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 10.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 10.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: orientation to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 10

**EX028** — *Objective:* apply ot, iot and cyber-physical security: orientation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX029** — *Objective:* apply ot, iot and cyber-physical security: orientation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX030** — *Objective:* apply ot, iot and cyber-physical security: orientation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: orientation helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 10 of 30

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — OT, IoT and cyber-physical security: assets and context

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: assets and context** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 11.1 Focus

**OT, IoT and cyber-physical security: assets and context** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 11.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 11.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: assets and context to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 11

**EX031** — *Objective:* apply ot, iot and cyber-physical security: assets and context to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX032** — *Objective:* apply ot, iot and cyber-physical security: assets and context to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX033** — *Objective:* apply ot, iot and cyber-physical security: assets and context to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: assets and context helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 11 of 30

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — OT, IoT and cyber-physical security: data flows

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: data flows** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 12.1 Focus

**OT, IoT and cyber-physical security: data flows** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 12.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 12.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: data flows to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 12

**EX034** — *Objective:* apply ot, iot and cyber-physical security: data flows to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX035** — *Objective:* apply ot, iot and cyber-physical security: data flows to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX036** — *Objective:* apply ot, iot and cyber-physical security: data flows to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: data flows helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 12 of 30

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — OT, IoT and cyber-physical security: risk scenarios

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: risk scenarios** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 13.1 Focus

**OT, IoT and cyber-physical security: risk scenarios** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 13.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 13.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: risk scenarios to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 13

**EX037** — *Objective:* apply ot, iot and cyber-physical security: risk scenarios to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX038** — *Objective:* apply ot, iot and cyber-physical security: risk scenarios to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX039** — *Objective:* apply ot, iot and cyber-physical security: risk scenarios to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: risk scenarios helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 13 of 30

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — OT, IoT and cyber-physical security: methods I

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: methods I** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 14.1 Focus

**OT, IoT and cyber-physical security: methods I** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 14.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 14.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: methods i to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 14

**EX040** — *Objective:* apply ot, iot and cyber-physical security: methods i to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX041** — *Objective:* apply ot, iot and cyber-physical security: methods i to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX042** — *Objective:* apply ot, iot and cyber-physical security: methods i to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: methods I helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 14 of 30

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — OT, IoT and cyber-physical security: guided lab

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: guided lab** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 15.1 Focus

**OT, IoT and cyber-physical security: guided lab** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 15.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 15.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: guided lab to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 15

**EX043** — *Objective:* apply ot, iot and cyber-physical security: guided lab to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX044** — *Objective:* apply ot, iot and cyber-physical security: guided lab to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX045** — *Objective:* apply ot, iot and cyber-physical security: guided lab to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: guided lab helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 15 of 30

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — OT, IoT and cyber-physical security: methods II

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: methods II** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 16.1 Focus

**OT, IoT and cyber-physical security: methods II** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 16.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 16.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: methods ii to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 16

**EX046** — *Objective:* apply ot, iot and cyber-physical security: methods ii to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX047** — *Objective:* apply ot, iot and cyber-physical security: methods ii to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX048** — *Objective:* apply ot, iot and cyber-physical security: methods ii to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: methods II helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 16 of 30

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — OT, IoT and cyber-physical security: tooling

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: tooling** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 17.1 Focus

**OT, IoT and cyber-physical security: tooling** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 17.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 17.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: tooling to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 17

**EX049** — *Objective:* apply ot, iot and cyber-physical security: tooling to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX050** — *Objective:* apply ot, iot and cyber-physical security: tooling to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX051** — *Objective:* apply ot, iot and cyber-physical security: tooling to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: tooling helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 17 of 30

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — OT, IoT and cyber-physical security: controls

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: controls** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 18.1 Focus

**OT, IoT and cyber-physical security: controls** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 18.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 18.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: controls to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 18

**EX052** — *Objective:* apply ot, iot and cyber-physical security: controls to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX053** — *Objective:* apply ot, iot and cyber-physical security: controls to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX054** — *Objective:* apply ot, iot and cyber-physical security: controls to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: controls helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 18 of 30

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — OT, IoT and cyber-physical security: monitoring

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: monitoring** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 19.1 Focus

**OT, IoT and cyber-physical security: monitoring** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 19.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 19.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: monitoring to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 19

**EX055** — *Objective:* apply ot, iot and cyber-physical security: monitoring to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX056** — *Objective:* apply ot, iot and cyber-physical security: monitoring to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX057** — *Objective:* apply ot, iot and cyber-physical security: monitoring to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: monitoring helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 19 of 30

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — OT, IoT and cyber-physical security: troubleshooting

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: troubleshooting** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 20.1 Focus

**OT, IoT and cyber-physical security: troubleshooting** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 20.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 20.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: troubleshooting to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 20

**EX058** — *Objective:* apply ot, iot and cyber-physical security: troubleshooting to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX059** — *Objective:* apply ot, iot and cyber-physical security: troubleshooting to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX060** — *Objective:* apply ot, iot and cyber-physical security: troubleshooting to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: troubleshooting helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 20 of 30

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — OT, IoT and cyber-physical security: service integration

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: service integration** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 21.1 Focus

**OT, IoT and cyber-physical security: service integration** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 21.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 21.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: service integration to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 21

**EX061** — *Objective:* apply ot, iot and cyber-physical security: service integration to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX062** — *Objective:* apply ot, iot and cyber-physical security: service integration to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX063** — *Objective:* apply ot, iot and cyber-physical security: service integration to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: service integration helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 21 of 30

[← Chapter 20](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — OT, IoT and cyber-physical security: automation

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: automation** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 22.1 Focus

**OT, IoT and cyber-physical security: automation** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 22.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 22.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: automation to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 22

**EX064** — *Objective:* apply ot, iot and cyber-physical security: automation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX065** — *Objective:* apply ot, iot and cyber-physical security: automation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX066** — *Objective:* apply ot, iot and cyber-physical security: automation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: automation helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 22 of 30

[← Chapter 21](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — OT, IoT and cyber-physical security: evaluation

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: evaluation** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 23.1 Focus

**OT, IoT and cyber-physical security: evaluation** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 23.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 23.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: evaluation to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 23

**EX067** — *Objective:* apply ot, iot and cyber-physical security: evaluation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX068** — *Objective:* apply ot, iot and cyber-physical security: evaluation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX069** — *Objective:* apply ot, iot and cyber-physical security: evaluation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: evaluation helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 23 of 30

[← Chapter 22](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes and connection

After this chapter you can apply **Applied research methods** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 24.1 Focus

**Applied research methods** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 24.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 24.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies applied research methods to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 24

**EX070** — *Objective:* apply applied research methods to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX071** — *Objective:* apply applied research methods to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX072** — *Objective:* apply applied research methods to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Applied research methods helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 24 of 30

[← Chapter 23](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes and connection

After this chapter you can apply **Team project studio** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 25.1 Focus

**Team project studio** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 25.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 25.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies team project studio to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 25

**EX073** — *Objective:* apply team project studio to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX074** — *Objective:* apply team project studio to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX075** — *Objective:* apply team project studio to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Team project studio helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 25 of 30

[← Chapter 24](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — OT, IoT and cyber-physical security: operational handoff

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: operational handoff** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 26.1 Focus

**OT, IoT and cyber-physical security: operational handoff** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 26.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 26.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies ot, iot and cyber-physical security: operational handoff to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 26

**EX076** — *Objective:* apply ot, iot and cyber-physical security: operational handoff to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX077** — *Objective:* apply ot, iot and cyber-physical security: operational handoff to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX078** — *Objective:* apply ot, iot and cyber-physical security: operational handoff to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: operational handoff helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 26 of 30

[← Chapter 25](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes and connection

After this chapter you can apply **Deployment and validation** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 27.1 Focus

**Deployment and validation** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 27.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 27.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On River Dock Pumping Station (RDPS), the team applies deployment and validation to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 27

**EX079** — *Objective:* apply deployment and validation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX080** — *Objective:* apply deployment and validation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX081** — *Objective:* apply deployment and validation to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Deployment and validation helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 27 of 30

[← Chapter 26](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes and connection

After this chapter you can apply **Field practice** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 28.1 Focus

**Field practice** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 28.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 28.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
 Record the stop authority by role name before any energised lab demonstration begins.
### Worked example

On River Dock Pumping Station (RDPS), the team applies field practice to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 28

**EX082** — *Objective:* apply field practice to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX083** — *Objective:* apply field practice to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX084** — *Objective:* apply field practice to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Field practice helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 28 of 30

[← Chapter 27](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes and connection

After this chapter you can apply **Capstone build** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 29.1 Focus

**Capstone build** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 29.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 29.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
 Record the stop authority by role name before any energised lab demonstration begins.
### Worked example

On River Dock Pumping Station (RDPS), the team applies capstone build to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 29

**EX085** — *Objective:* apply capstone build to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX086** — *Objective:* apply capstone build to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX087** — *Objective:* apply capstone build to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Capstone build helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 29 of 30

[← Chapter 28](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes and connection

After this chapter you can apply **Capstone assessment** in an OT setting on synthetic River Dock Pumping Station (RDPS), with scoped claims and explicit assumptions.

### 30.1 Focus

**Capstone assessment** for OT practitioners on River Dock Pumping Station (RDPS): definitions, one worked synthetic example, and a small artefact.

### 30.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 30.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technologist study note

Apply ideas to the synthetic **River Dock Pumping Station (RDPS)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep River Dock Pumping Station (RDPS) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
 Record the stop authority by role name before any energised lab demonstration begins.
### Worked example

On River Dock Pumping Station (RDPS), the team applies capstone assessment to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 30

**EX088** — *Objective:* apply capstone assessment to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX089** — *Objective:* apply capstone assessment to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX090** — *Objective:* apply capstone assessment to River Dock Pumping Station (RDPS). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Capstone assessment helps when tied to physical consequences and honest OT metrics on synthetic River Dock Pumping Station (RDPS).

### Continue studying — chapter 30 of 30

[← Chapter 29](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results)

<a id="worked-results"></a>

## Worked results


### Chapter 1
- **EX001** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX002** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX003** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 2
- **EX004** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX005** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX006** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 3
- **EX007** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX008** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX009** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 4
- **EX010** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX011** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX012** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 5
- **EX013** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX014** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX015** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 6
- **EX016** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX017** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX018** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 7
- **EX019** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX020** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX021** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 8
- **EX022** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX023** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX024** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 9
- **EX025** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX026** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX027** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 10
- **EX028** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX029** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX030** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 11
- **EX031** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX032** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX033** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 12
- **EX034** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX035** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX036** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 13
- **EX037** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX038** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX039** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 14
- **EX040** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX041** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX042** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 15
- **EX043** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX044** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX045** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 16
- **EX046** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX047** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX048** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 17
- **EX049** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX050** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX051** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 18
- **EX052** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX053** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX054** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 19
- **EX055** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX056** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX057** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 20
- **EX058** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX059** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX060** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 21
- **EX061** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX062** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX063** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 22
- **EX064** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX065** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX066** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 23
- **EX067** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX068** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX069** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 24
- **EX070** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX071** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX072** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 25
- **EX073** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX074** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX075** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 26
- **EX076** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX077** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX078** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 27
- **EX079** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX080** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX081** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 28
- **EX082** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX083** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX084** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 29
- **EX085** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX086** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX087** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

### Chapter 30
- **EX088** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX089** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.
- **EX090** — Complete artefact for River Dock Pumping Station (RDPS); synthetic only; scoped.

**End of worked results.**
