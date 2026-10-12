# OT, IoT and Cyber-Physical Security: Technical Course Book

- Language: English (`en`); technical 18 months.
- Editorial state: **draft**. Chapters 1–18 authored; exercises with worked results; offline lab verified. Review and A4 verification open.
- Synthetic plant: **Harbor Gate PLC Lab (HGPL)**.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). [CC0 1.0](../../../../../LICENSE).
- Boundary: not an accredited award; no production OT access.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## Contents

1. [Computing and service architecture](#ch-01)
2. [Networks and protocols](#ch-02)
3. [Operating systems and identities](#ch-03)
4. [Scripting and data formats](#ch-04)
5. [Security scope and evidence](#ch-05)
6. [OT, IoT and cyber-physical security: system model](#ch-06)
7. [OT, IoT and cyber-physical security: data and telemetry](#ch-07)
8. [OT, IoT and cyber-physical security: failure modes](#ch-08)
9. [OT, IoT and cyber-physical security: tools and methods](#ch-09)
10. [OT, IoT and cyber-physical security: control configuration](#ch-10)
11. [OT, IoT and cyber-physical security: verification](#ch-11)
12. [Contained laboratory I](#ch-12)
13. [OT, IoT and cyber-physical security: troubleshooting](#ch-13)
14. [OT, IoT and cyber-physical security: automation](#ch-14)
15. [OT, IoT and cyber-physical security: integration and dependencies](#ch-15)
16. [Technical documentation and safety](#ch-16)
17. [Contained laboratory II](#ch-17)
18. [Supervised technical project](#ch-18)
19. [Worked results](#worked-results)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes and connection

After this chapter you can apply **Computing and service architecture** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 1.1 Focus

**Computing and service architecture** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 1.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 1.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies computing and service architecture to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 1

**EX001** — *Objective:* apply computing and service architecture to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX002** — *Objective:* apply computing and service architecture to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX003** — *Objective:* apply computing and service architecture to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX004** — *Objective:* apply computing and service architecture to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Computing and service architecture helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes and connection

After this chapter you can apply **Networks and protocols** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 2.1 Focus

**Networks and protocols** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 2.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 2.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies networks and protocols to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 2

**EX005** — *Objective:* apply networks and protocols to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX006** — *Objective:* apply networks and protocols to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX007** — *Objective:* apply networks and protocols to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX008** — *Objective:* apply networks and protocols to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Networks and protocols helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 02 of 18

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes and connection

After this chapter you can apply **Operating systems and identities** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 3.1 Focus

**Operating systems and identities** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 3.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 3.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Laboratory activity

```python
# Lab (technical OT, synthetic): band vs CUSUM
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

On Harbor Gate PLC Lab (HGPL), the team applies operating systems and identities to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 3

**EX009** — *Objective:* apply operating systems and identities to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX010** — *Objective:* apply operating systems and identities to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX011** — *Objective:* apply operating systems and identities to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX012** — *Objective:* apply operating systems and identities to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Operating systems and identities helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 03 of 18

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes and connection

After this chapter you can apply **Scripting and data formats** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 4.1 Focus

**Scripting and data formats** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 4.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 4.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies scripting and data formats to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 4

**EX013** — *Objective:* apply scripting and data formats to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX014** — *Objective:* apply scripting and data formats to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX015** — *Objective:* apply scripting and data formats to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX016** — *Objective:* apply scripting and data formats to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Scripting and data formats helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 04 of 18

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes and connection

After this chapter you can apply **Security scope and evidence** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 5.1 Focus

**Security scope and evidence** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 5.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 5.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies security scope and evidence to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 5

**EX017** — *Objective:* apply security scope and evidence to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX018** — *Objective:* apply security scope and evidence to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX019** — *Objective:* apply security scope and evidence to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX020** — *Objective:* apply security scope and evidence to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Security scope and evidence helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 05 of 18

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — OT, IoT and cyber-physical security: system model

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: system model** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 6.1 Focus

**OT, IoT and cyber-physical security: system model** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 6.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 6.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: system model to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 6

**EX021** — *Objective:* apply ot, iot and cyber-physical security: system model to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX022** — *Objective:* apply ot, iot and cyber-physical security: system model to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX023** — *Objective:* apply ot, iot and cyber-physical security: system model to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX024** — *Objective:* apply ot, iot and cyber-physical security: system model to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: system model helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 06 of 18

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — OT, IoT and cyber-physical security: data and telemetry

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: data and telemetry** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 7.1 Focus

**OT, IoT and cyber-physical security: data and telemetry** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 7.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 7.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: data and telemetry to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 7

**EX025** — *Objective:* apply ot, iot and cyber-physical security: data and telemetry to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX026** — *Objective:* apply ot, iot and cyber-physical security: data and telemetry to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX027** — *Objective:* apply ot, iot and cyber-physical security: data and telemetry to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX028** — *Objective:* apply ot, iot and cyber-physical security: data and telemetry to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: data and telemetry helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 07 of 18

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — OT, IoT and cyber-physical security: failure modes

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: failure modes** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 8.1 Focus

**OT, IoT and cyber-physical security: failure modes** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 8.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 8.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: failure modes to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 8

**EX029** — *Objective:* apply ot, iot and cyber-physical security: failure modes to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX030** — *Objective:* apply ot, iot and cyber-physical security: failure modes to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX031** — *Objective:* apply ot, iot and cyber-physical security: failure modes to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX032** — *Objective:* apply ot, iot and cyber-physical security: failure modes to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: failure modes helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 08 of 18

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — OT, IoT and cyber-physical security: tools and methods

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: tools and methods** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 9.1 Focus

**OT, IoT and cyber-physical security: tools and methods** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 9.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 9.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: tools and methods to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 9

**EX033** — *Objective:* apply ot, iot and cyber-physical security: tools and methods to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX034** — *Objective:* apply ot, iot and cyber-physical security: tools and methods to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX035** — *Objective:* apply ot, iot and cyber-physical security: tools and methods to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX036** — *Objective:* apply ot, iot and cyber-physical security: tools and methods to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: tools and methods helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 09 of 18

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — OT, IoT and cyber-physical security: control configuration

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: control configuration** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 10.1 Focus

**OT, IoT and cyber-physical security: control configuration** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 10.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 10.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: control configuration to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 10

**EX037** — *Objective:* apply ot, iot and cyber-physical security: control configuration to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX038** — *Objective:* apply ot, iot and cyber-physical security: control configuration to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX039** — *Objective:* apply ot, iot and cyber-physical security: control configuration to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX040** — *Objective:* apply ot, iot and cyber-physical security: control configuration to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: control configuration helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 10 of 18

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — OT, IoT and cyber-physical security: verification

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: verification** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 11.1 Focus

**OT, IoT and cyber-physical security: verification** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 11.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 11.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: verification to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 11

**EX041** — *Objective:* apply ot, iot and cyber-physical security: verification to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX042** — *Objective:* apply ot, iot and cyber-physical security: verification to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX043** — *Objective:* apply ot, iot and cyber-physical security: verification to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX044** — *Objective:* apply ot, iot and cyber-physical security: verification to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: verification helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 11 of 18

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes and connection

After this chapter you can apply **Contained laboratory I** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 12.1 Focus

**Contained laboratory I** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 12.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 12.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies contained laboratory i to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 12

**EX045** — *Objective:* apply contained laboratory i to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX046** — *Objective:* apply contained laboratory i to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX047** — *Objective:* apply contained laboratory i to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX048** — *Objective:* apply contained laboratory i to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Contained laboratory I helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 12 of 18

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — OT, IoT and cyber-physical security: troubleshooting

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: troubleshooting** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 13.1 Focus

**OT, IoT and cyber-physical security: troubleshooting** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 13.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 13.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: troubleshooting to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 13

**EX049** — *Objective:* apply ot, iot and cyber-physical security: troubleshooting to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX050** — *Objective:* apply ot, iot and cyber-physical security: troubleshooting to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX051** — *Objective:* apply ot, iot and cyber-physical security: troubleshooting to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX052** — *Objective:* apply ot, iot and cyber-physical security: troubleshooting to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: troubleshooting helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 13 of 18

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — OT, IoT and cyber-physical security: automation

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: automation** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 14.1 Focus

**OT, IoT and cyber-physical security: automation** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 14.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 14.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: automation to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 14

**EX053** — *Objective:* apply ot, iot and cyber-physical security: automation to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX054** — *Objective:* apply ot, iot and cyber-physical security: automation to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX055** — *Objective:* apply ot, iot and cyber-physical security: automation to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX056** — *Objective:* apply ot, iot and cyber-physical security: automation to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: automation helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 14 of 18

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — OT, IoT and cyber-physical security: integration and dependencies

### Learning outcomes and connection

After this chapter you can apply **OT, IoT and cyber-physical security: integration and dependencies** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 15.1 Focus

**OT, IoT and cyber-physical security: integration and dependencies** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 15.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 15.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies ot, iot and cyber-physical security: integration and dependencies to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 15

**EX057** — *Objective:* apply ot, iot and cyber-physical security: integration and dependencies to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX058** — *Objective:* apply ot, iot and cyber-physical security: integration and dependencies to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX059** — *Objective:* apply ot, iot and cyber-physical security: integration and dependencies to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX060** — *Objective:* apply ot, iot and cyber-physical security: integration and dependencies to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

OT, IoT and cyber-physical security: integration and dependencies helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 15 of 18

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes and connection

After this chapter you can apply **Technical documentation and safety** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 16.1 Focus

**Technical documentation and safety** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 16.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 16.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies technical documentation and safety to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 16

**EX061** — *Objective:* apply technical documentation and safety to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX062** — *Objective:* apply technical documentation and safety to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX063** — *Objective:* apply technical documentation and safety to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX064** — *Objective:* apply technical documentation and safety to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Technical documentation and safety helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 16 of 18

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes and connection

After this chapter you can apply **Contained laboratory II** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 17.1 Focus

**Contained laboratory II** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 17.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 17.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies contained laboratory ii to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 17

**EX065** — *Objective:* apply contained laboratory ii to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX066** — *Objective:* apply contained laboratory ii to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX067** — *Objective:* apply contained laboratory ii to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX068** — *Objective:* apply contained laboratory ii to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Contained laboratory II helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 17 of 18

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes and connection

After this chapter you can apply **Supervised technical project** in an OT setting on synthetic Harbor Gate PLC Lab (HGPL), with scoped claims and explicit assumptions.

### 18.1 Focus

**Supervised technical project** for OT practitioners on Harbor Gate PLC Lab (HGPL): definitions, one worked synthetic example, and a small artefact.

### 18.2 Method

Inputs, steps, outputs with assumptions. Use Python 3 stdlib when coding. Prefer physical consequence units.

### 18.3 Safety and metrics

No production access. Report event recall/delay/FA where detection is discussed.

### Technical study note

Apply ideas to the synthetic **Harbor Gate PLC Lab (HGPL)**. State units; separate observation from claim; prefer event recall, delay and false alarms per shift. Never access production OT; use synthetic data or isolated labs with independent safety layers and stop authority. Cite NIST SP 800-82 Rev. 3, ISA/IEC 62443 and ATT&CK for ICS with versions. Keep Harbor Gate PLC Lab (HGPL) labelled synthetic.

### Teaching depth

Name Purdue levels and conduit permissions (read/write/engineering). Treat shared-PLC dual-sensor spoofing as a failure class for residual detectors. Record residual-risk owners on every recommendation. Re-verify standards before field use.

### Additional exposition

Industrial control security is learned by tying each control to a process variable and a failure mode. A firewall rule that blocks engineering downloads must still allow a tested break-glass path owned by operations. A residual alarm that fires must tell the operator which sensors disagree and what safe action is permitted. Practice writing that sentence for every control you recommend, then check whether your synthetic lab evidence actually supports it.
### Worked example

On Harbor Gate PLC Lab (HGPL), the team applies supervised technical project to a pump/PLC decision. Numbers are synthetic and support a training decision only.

### Common errors and limits

- Production testing.
- Vanity metrics.
- Unowned residual risk.
- Missing Purdue/conduit context.

### Exercises — chapter 18

**EX069** — *Objective:* apply supervised technical project to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX070** — *Objective:* apply supervised technical project to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX071** — *Objective:* apply supervised technical project to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.
**EX072** — *Objective:* apply supervised technical project to Harbor Gate PLC Lab (HGPL). *Steps:* short artefact with scope. *Evidence:* artefact. *Rubric:* 3 scoped; 2 thin; 1 vague; 0 none.

### Chapter synthesis

Supervised technical project helps when tied to physical consequences and honest OT metrics on synthetic Harbor Gate PLC Lab (HGPL).

### Continue studying — chapter 18 of 18

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results)

<a id="worked-results"></a>

## Worked results


### Chapter 1
- **EX001** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX002** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX003** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX004** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 2
- **EX005** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX006** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX007** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX008** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 3
- **EX009** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX010** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX011** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX012** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 4
- **EX013** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX014** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX015** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX016** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 5
- **EX017** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX018** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX019** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX020** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 6
- **EX021** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX022** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX023** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX024** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 7
- **EX025** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX026** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX027** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX028** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 8
- **EX029** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX030** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX031** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX032** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 9
- **EX033** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX034** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX035** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX036** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 10
- **EX037** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX038** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX039** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX040** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 11
- **EX041** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX042** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX043** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX044** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 12
- **EX045** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX046** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX047** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX048** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 13
- **EX049** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX050** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX051** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX052** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 14
- **EX053** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX054** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX055** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX056** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 15
- **EX057** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX058** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX059** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX060** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 16
- **EX061** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX062** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX063** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX064** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 17
- **EX065** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX066** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX067** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX068** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

### Chapter 18
- **EX069** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX070** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX071** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.
- **EX072** — Complete artefact for Harbor Gate PLC Lab (HGPL); synthetic only; scoped.

**End of worked results.**
