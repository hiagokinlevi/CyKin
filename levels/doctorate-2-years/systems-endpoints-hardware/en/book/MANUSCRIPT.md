# Systems, Endpoint and Hardware Security: Doctoral Research Track

- Language: English (`en`); course 196, Doctoral research track (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Four offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: doctoral candidates researching systems and endpoint security who must produce original, reproducible evidence with partner organisations.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only servers, endpoints and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, inventories, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one doctoral candidate from a hospital trust's monthly patch problems, through research integrity and coder agreement, the research frontier, a proposal, baseline replication and pilot, a main study with independent validation, peer critique, a reproducibility archive and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Yusuf Adeyemi** | Doctoral candidate | Invented |
| **Prof. Ingrid Solberg** | Supervisor | Invented |
| **Calder University** | Fictional university | Invented |
| **Harrowgate Health Trust** | Fictional partner | Invented |

### Core sources

NIST [SP 800-123](https://doi.org/10.6028/NIST.SP.800-123), [SP 800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4), [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128), [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5) and [SP 800-193](https://doi.org/10.6028/NIST.SP.800-193); [CIS Controls v8](https://www.cisecurity.org/controls/v8) and [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); DISA [STIGs](https://public.cyber.mil/stigs/); Microsoft [Windows security baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines); Linux [kernel self-protection](https://www.kernel.org/doc/html/latest/security/self-protection.html). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced research integrity and methods

### Learning outcomes

You will (1) frame a doctoral question in endpoint patch management; (2) design for integrity, from pre-registration to coder agreement; (3) measure agreement on labelled data before analysis.

### 1.1 The research problem

Yusuf Adeyemi is a doctoral candidate at the fictional Calder University, supervised by Prof. Ingrid Solberg. His partner organisation is the fictional Harrowgate Health Trust, which runs about 1,000 clinical and office endpoints. The trust patches everything at once each month, and two problems recur: some endpoints stay unpatched for weeks, and a bad update occasionally breaks clinical applications across every ward at the same time. NIST SP 800-40 Rev. 4 describes patching as preventive maintenance and recommends planning for both speed and the risk of disruption. Yusuf asks whether staged, ring-based deployment shortens the time to reach most endpoints while reducing update failures, compared with flat deployment.

### 1.2 Why integrity first

Endpoint data are messy: devices are offline, tickets are labelled inconsistently and outcomes can be chosen after seeing results. Yusuf pre-registers his hypotheses, primary outcomes (95th-percentile days to patch and failure rate) and analysis plan with his supervisor before collecting main-study data.

Section one point two develops advanced research integrity and methods with a Calder University note Yusuf Adeyemi can demo offline.

Under section one point two, Prof. Ingrid Solberg expects advanced claims to carry owners and dates.

Section one point two treats the research problem why as testable only when evidence and ticket IDs are recorded.

### 1.3 Coding failure tickets

Failure reasons in help-desk tickets are free text. Yusuf writes a codebook with four labels: reboot problems, disk space, application breakage and network. Two coders label 80 synthetic tickets independently.

Section one point three develops advanced research integrity and methods with a Calder University note Yusuf Adeyemi can demo offline.

Under section one point three, Prof. Ingrid Solberg expects advanced claims to carry owners and dates.

Section one point three treats the research problem why as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — coder agreement

```python
"""Cohen's kappa for two coders labelling synthetic patch-failure tickets (stdlib only)."""
import collections
a = ["reboot"]*30 + ["disk"]*12 + ["app"]*18 + ["network"]*10 + ["reboot"]*3 + ["app"]*4 + ["disk"]*3
b = ["reboot"]*30 + ["disk"]*12 + ["app"]*18 + ["network"]*10 + ["app"]*3 + ["reboot"]*4 + ["network"]*3
n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
ca, cb = collections.Counter(a), collections.Counter(b)
pe = sum(ca[k] * cb[k] for k in set(a) | set(b)) / n**2
print(f"tickets {n}, observed agreement {po:.3f}, chance {pe:.3f}, kappa {(po-pe)/(1-pe):.3f}")
```

Run with `python3 lab_kappa.py`. Verified output:

```text
tickets 80, observed agreement 0.875, chance 0.296, kappa 0.822
```

### 1.4 Reading agreement

Observed agreement is 0.875, chance agreement 0.296 and Cohen's kappa 0.822. By the bands of Landis and Koch (1977), this is almost perfect agreement. Disagreements cluster between reboot and application labels, so the codebook gains a rule: if the application fails only until a reboot, label it reboot.

Section one point four develops advanced research integrity and methods with a Calder University note Yusuf Adeyemi can demo offline.

Under section one point four, Prof. Ingrid Solberg expects advanced claims to carry owners and dates.

Section one point four treats the research problem why as testable only when evidence and ticket IDs are recorded.

### 1.5 Data ethics

Ticket text can name staff and occasionally patients. The trust's information governance lead approves a process where tickets are redacted before leaving the trust, and Yusuf works only with redacted, synthetic-structure extracts.

Section one point five develops advanced research integrity and methods with a Calder University note Yusuf Adeyemi can demo offline.

Under section one point five, Prof. Ingrid Solberg expects advanced claims to carry owners and dates.

Section one point five treats the research problem why as testable only when evidence and ticket IDs are recorded.

### Worked example

Prof. Solberg asks why kappa rather than simple agreement. Yusuf shows that with an uneven label distribution, two coders could agree often by chance; kappa corrects for that, and 0.822 is well above the 0.6 threshold they pre-registered.

> **Synthetic case.** Yusuf, Prof. Solberg, Calder and Harrowgate are synthetic.

### Errors and limits

High agreement on a pilot set does not guarantee agreement on later tickets; re-check a sample during the main study.

### Exercises

- **EX001 — Research question.** State Yusuf's research question. *Rubric:* 3 = ring vs flat: time to patch and failures; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Primary outcomes.** Which primary outcomes were pre-registered? *Rubric:* 3 = 95th pct days to patch; failure rate; 2 = one; 1 = none; 0 = none.
- **EX003 — Kappa values.** Report the lab's agreement figures. *Rubric:* 3 = 0.875, 0.296, 0.822; 2 = two; 1 = one; 0 = none.
- **EX004 — Interpretation band.** How do Landis and Koch classify 0.822? *Rubric:* 3 = almost perfect; 2 = partial; 1 = none; 0 = none.
- **EX005 — Codebook rule.** Which rule was added after disagreements? *Rubric:* 3 = app fails until reboot → reboot; 2 = partial; 1 = none; 0 = none.
- **EX006 — Redaction.** How are staff and patient names protected? *Rubric:* 3 = redacted before leaving trust, approved process; 2 = partial; 1 = none; 0 = none.
- **EX007 — Patch framing.** How does SP 800-40r4 frame patching? *Rubric:* 3 = preventive maintenance balancing speed and disruption; 2 = partial; 1 = none; 0 = none.

### Synthesis

Integrity comes from fixing questions, outcomes and coding rules before seeing results.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Systems, endpoints and hardware security: research frontier

### Learning outcomes

You will (1) survey research on patching, configuration and endpoint behaviour; (2) locate the gap Yusuf's study addresses; (3) distinguish hardware-level risks from deployment questions.

### 2.1 Patch research

Li and Paxson (2017) studied thousands of security patches across open-source projects, finding that security fixes are often smaller than other fixes and that vulnerabilities can stay in code for years. Nappa et al. (2015) measured patch deployment on client machines and showed that shared code across applications leaves some copies unpatched long after a fix is released. Both show that release is not deployment.

Section two point one develops systems endpoints and hardware security with a Calder University note Yusuf Adeyemi can demo offline.

### 2.2 Operators' view

Dietrich et al. (2018) surveyed system operators about security misconfigurations, finding that many incidents come from configuration errors under time pressure and weak processes. Patch deployment is an operator process with the same pressures.

Section two point two develops systems endpoints and hardware security with a Calder University note Yusuf Adeyemi can demo offline.

Under section two point two, Prof. Ingrid Solberg expects systems claims to carry owners and dates.

Section two point two treats patch research operators' view as testable only when evidence and ticket IDs are recorded.

### 2.3 Hardware frontier

Kocher et al. (2019) showed that speculative execution in processors can leak data across security boundaries; Kim et al. (2014) showed that repeatedly accessing DRAM rows can flip bits in neighbouring rows. Fixes for such flaws arrive as firmware, microcode and operating system updates, which increases the volume and risk of endpoint patching. NIST SP 800-193 sets out firmware resiliency principles: protect, detect and recover.

Section two point three develops systems endpoints and hardware security with a Calder University note Yusuf Adeyemi can demo offline.

### 2.4 The gap

The literature measures patch release and population-level deployment, but few studies compare deployment strategies inside one organisation with outcome data on both speed and breakage. Yusuf's study fits this gap.

Section two point four develops systems endpoints and hardware security with a Calder University note Yusuf Adeyemi can demo offline.

Under section two point four, Prof. Ingrid Solberg expects systems claims to carry owners and dates.

Section two point four treats patch research operators' view as testable only when evidence and ticket IDs are recorded.

### 2.5 Scope boundary

The study observes deployment outcomes; it does not test or reproduce any vulnerability.

Section two point five develops systems endpoints and hardware security with a Calder University note Yusuf Adeyemi can demo offline.

Under section two point five, Prof. Ingrid Solberg expects systems claims to carry owners and dates.

Section two point five treats patch research operators' view as testable only when evidence and ticket IDs are recorded.

For section two point five, Calder University will not accept systems work without a written trail.

### Worked example

An examiner on the progress panel asks whether hardware flaws are within scope. Yusuf explains that he studies how their updates are deployed, not the flaws themselves, and that firmware updates are included as a separate category because their failure modes differ.

> **Synthetic case.** Synthetic panel.

### Errors and limits

Citing famous hardware papers can make a deployment study sound more technical than it is; be precise about scope.

### Exercises

- **EX008 — Li and Paxson.** What did Li and Paxson (2017) find about security patches? *Rubric:* 3 = smaller fixes; long-lived vulnerabilities; 2 = partial; 1 = none; 0 = none.
- **EX009 — Nappa finding.** How does shared code affect patching per Nappa et al. (2015)? *Rubric:* 3 = copies stay unpatched; 2 = partial; 1 = none; 0 = none.
- **EX010 — Operators.** What did Dietrich et al. (2018) find? *Rubric:* 3 = misconfigs under pressure, weak process; 2 = partial; 1 = none; 0 = none.
- **EX011 — Hardware updates.** Why do hardware flaws matter for deployment? *Rubric:* 3 = fixes arrive as firmware/microcode/OS updates; 2 = partial; 1 = none; 0 = none.
- **EX012 — SP 800-193.** Name SP 800-193's three principles. *Rubric:* 3 = protect, detect, recover; 2 = two; 1 = one; 0 = none.
- **EX013 — Gap.** What gap does the study address? *Rubric:* 3 = in-organisation strategy comparison with speed and breakage; 2 = partial; 1 = none; 0 = none.
- **EX014 — Firmware category.** Why are firmware updates separated? *Rubric:* 3 = different failure modes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Locate the study where the literature measures release but not strategy.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Original contribution proposal

### Learning outcomes

You will (1) specify hypotheses, design and outcomes; (2) justify a quasi-experimental design; (3) plan threats to validity.

### 3.1 Hypotheses

H1: ring-based deployment reduces the 95th-percentile days to patch. H2: ring-based deployment reduces the update failure rate. Both are directional and pre-registered.

Section three point one develops original contribution proposal with a Calder University note Yusuf Adeyemi can demo offline.

Under section three point one, Prof. Ingrid Solberg expects original claims to carry owners and dates.

Section three point one treats hypotheses design rings threats as testable only when evidence and ticket IDs are recorded.

For section three point one, Calder University will not accept original work without a written trail.

### 3.2 Design

Harrowgate has two comparable hospital sites. With the trust's agreement, one site adopts rings for six months while the other continues flat deployment. Random assignment of individual endpoints is impossible because wards share devices and staff, so the design is a site-level quasi-experiment.

Section three point two develops original contribution proposal with a Calder University note Yusuf Adeyemi can demo offline.

Under section three point two, Prof. Ingrid Solberg expects original claims to carry owners and dates.

Section three point two treats hypotheses design rings threats as testable only when evidence and ticket IDs are recorded.

### 3.3 Rings

Ring 0 is 40 IT devices, patched first; ring 1 is 160 devices in pilot wards; ring 2 is the remaining 800. Each ring waits for the previous ring's failure signals before proceeding, following the staged approach discussed in SP 800-40r4.

Section three point three develops original contribution proposal with a Calder University note Yusuf Adeyemi can demo offline.

Under section three point three, Prof. Ingrid Solberg expects original claims to carry owners and dates.

Section three point three treats hypotheses design rings threats as testable only when evidence and ticket IDs are recorded.

### 3.4 Threats to validity

Sites may differ in device age or staff habits. Yusuf collects baseline data from both sites for three months before the change, so differences can be measured. Seasonal workload affects both sites equally.

Section three point four develops original contribution proposal with a Calder University note Yusuf Adeyemi can demo offline.

Under section three point four, Prof. Ingrid Solberg expects original claims to carry owners and dates.

Section three point four treats hypotheses design rings threats as testable only when evidence and ticket IDs are recorded.

### 3.5 Contribution

The thesis contributes measured effects of a common but untested practice, a codebook for failure tickets and an open, synthetic-structure dataset with analysis code.

Section three point five develops original contribution proposal with a Calder University note Yusuf Adeyemi can demo offline.

Under section three point five, Prof. Ingrid Solberg expects original claims to carry owners and dates.

Section three point five treats hypotheses design rings threats as testable only when evidence and ticket IDs are recorded.

For section three point five, Calder University will not accept original work without a written trail.

### Power and sample

With 1,000 endpoints per site and monthly cycles, Yusuf estimates that six months gives enough failures to detect a difference of about one percentage point in failure rate, based on the trust's historical rate of roughly three per cent. He records this calculation in the pre-registration, along with the decision not to extend the study if results are unclear, which prevents stopping when results look favourable.

### Approvals

The proposal is approved by Calder's research ethics committee and the trust's information governance lead. Both approvals specify that no clinical system will be changed solely for research; rings use the trust's existing deployment tool.

### Worked example

Prof. Solberg asks why not randomise wards. Yusuf explains that ward devices are managed by shared policies at site level, so splitting a site would mix treatments; site-level assignment with baseline comparison is the honest option.

> **Synthetic case.** Synthetic.

### Errors and limits

Two sites give limited generalisation; the thesis must say so.

### Exercises

- **EX015 — Hypotheses.** State H1 and H2. *Rubric:* 3 = ring reduces 95th pct days; ring reduces failures; 2 = one; 1 = none; 0 = none.
- **EX016 — Design reason.** Why is the design quasi-experimental? *Rubric:* 3 = endpoints cannot be randomised individually; 2 = partial; 1 = none; 0 = none.
- **EX017 — Ring sizes.** Give the ring sizes. *Rubric:* 3 = 40, 160, 800; 2 = partial; 1 = none; 0 = none.
- **EX018 — Baseline data.** Why collect three months of baseline data? *Rubric:* 3 = measure site differences; 2 = partial; 1 = none; 0 = none.
- **EX019 — Contributions.** List the three contributions. *Rubric:* 3 = effects, codebook, dataset and code; 2 = two; 1 = one; 0 = none.
- **EX020 — Ward randomisation.** Why not randomise wards? *Rubric:* 3 = site-level policies would mix treatments; 2 = partial; 1 = none; 0 = none.

### Synthesis

Propose a design that is honest about what assignment is possible.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Baseline replication and pilot

### Learning outcomes

You will (1) replicate the trust's baseline measures; (2) run a ring pilot; (3) check measurement and data pipelines.

### 4.1 Replicating the baseline

Before the pilot, Yusuf recomputes the trust's own patch-compliance report from raw deployment logs. His figures match the trust's to within one percentage point, confirming that he understands how the logs record installation and reboot.

Section four point one develops baseline replication and pilot with a Calder University note Yusuf Adeyemi can demo offline.

Under section four point one, Prof. Ingrid Solberg expects baseline claims to carry owners and dates.

Section four point one treats replicating the baseline pilot as testable only when evidence and ticket IDs are recorded.

### 4.2 Pilot

One month at the intervention site tests the ring mechanics and the data pipeline.

Section four point two develops baseline replication and pilot with a Calder University note Yusuf Adeyemi can demo offline.

Under section four point two, Prof. Ingrid Solberg expects baseline claims to carry owners and dates.

Section four point two treats replicating the baseline pilot as testable only when evidence and ticket IDs are recorded.

For section four point two, Calder University will not accept baseline work without a written trail.

### Lab — Lab — pilot ring timings

```python
"""Median days-to-patch per deployment ring in a synthetic pilot (stdlib only)."""
import statistics, random
random.seed(7)
rings = {"ring0 (IT, 40)": (40, 1, 3), "ring1 (pilot wards, 160)": (160, 3, 8), "ring2 (rest, 800)": (800, 7, 16)}
for name, (n, lo, hi) in rings.items():
    days = [random.randint(lo, hi) for _ in range(n)]
    print(f"{name}: median {statistics.median(days)} days, max {max(days)}")
```

Run with `python3 lab_pilot.py`. Verified output:

```text
ring0 (IT, 40): median 2.0 days, max 3
ring1 (pilot wards, 160): median 6.0 days, max 8
ring2 (rest, 800): median 11.0 days, max 16
```

### 4.3 Reading the pilot

Ring 0 reaches median 2 days (max 3), ring 1 median 6 (max 8) and ring 2 median 11 (max 16). The waits between rings work as designed, and the pipeline captures each endpoint's install and reboot times.

Section four point three develops baseline replication and pilot with a Calder University note Yusuf Adeyemi can demo offline.

Under section four point three, Prof. Ingrid Solberg expects baseline claims to carry owners and dates.

Section four point three treats replicating the baseline pilot as testable only when evidence and ticket IDs are recorded.

### 4.4 Pipeline fixes

The pilot reveals that 3% of endpoints report no reboot time because they were shut down rather than restarted; Yusuf adds a rule treating the next boot as the reboot.

Section four point four develops baseline replication and pilot with a Calder University note Yusuf Adeyemi can demo offline.

Under section four point four, Prof. Ingrid Solberg expects baseline claims to carry owners and dates.

Section four point four treats replicating the baseline pilot as testable only when evidence and ticket IDs are recorded.

### 4.5 Configuration management

The ring definitions are stored as configuration items following SP 800-128, so changes during the study are recorded.

Section four point five develops baseline replication and pilot with a Calder University note Yusuf Adeyemi can demo offline.

Under section four point five, Prof. Ingrid Solberg expects baseline claims to carry owners and dates.

Section four point five treats replicating the baseline pilot as testable only when evidence and ticket IDs are recorded.

For section four point five, Calder University will not accept baseline work without a written trail.

### Clock and identity checks

Deployment logs come from the management server and endpoint agents, whose clocks can differ. Yusuf compares server and endpoint timestamps on a sample and finds a median skew under one minute, small enough for day-level outcomes. He also checks that endpoint identifiers stay stable when devices are re-imaged; a re-imaged device keeps its asset tag, so he links records by asset tag rather than hostname.

These checks are recorded in a data quality note that later chapters cite.

### Sign-off

The trust signs off the pilot report.

### Worked example

The trust's desktop lead worries that ring 2 waits too long. Yusuf points out that ring 2's maximum of 16 days is still within the trust's 30-day policy, and the main study will test whether total time improves.

> **Synthetic case.** Synthetic.

### Errors and limits

A pilot shows feasibility, not effect; do not report pilot timings as results.

### Exercises

- **EX021 — Replication.** How close was the replication? *Rubric:* 3 = within one percentage point; 2 = partial; 1 = none; 0 = none.
- **EX022 — Pilot medians.** Give the pilot ring medians. *Rubric:* 3 = 2, 6, 11 days; 2 = two; 1 = one; 0 = none.
- **EX023 — Missing reboots.** What caused missing reboot times and how was it fixed? *Rubric:* 3 = shutdowns; next boot as reboot; 2 = partial; 1 = none; 0 = none.
- **EX024 — Ring 2 concern.** How was the ring 2 concern answered? *Rubric:* 3 = max 16 within 30-day policy; 2 = partial; 1 = none; 0 = none.
- **EX025 — Config items.** Why store rings as configuration items? *Rubric:* 3 = changes recorded; 2 = partial; 1 = none; 0 = none.
- **EX026 — Pilot limit.** What can a pilot not show? *Rubric:* 3 = effect; 2 = partial; 1 = none; 0 = none.

### Synthesis

Replicate the baseline and test the pipeline before measuring effects.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Main study and independent validation

### Learning outcomes

You will (1) analyse the main study; (2) estimate effects with uncertainty; (3) validate results independently.

### 5.1 Main data

Six months produce data on 1,000 endpoints at each site. The analysis follows the pre-registered plan.

Section five point one develops main study and independent validation with a Calder University note Yusuf Adeyemi can demo offline.

Under section five point one, Prof. Ingrid Solberg expects main claims to carry owners and dates.

Section five point one treats main data reading the as testable only when evidence and ticket IDs are recorded.

For section five point one, Calder University will not accept main work without a written trail.

### Lab — Lab — ring versus flat

```python
"""Compare ring-based and flat patch deployment on synthetic endpoints with a bootstrap CI (stdlib only)."""
import random, statistics
random.seed(42)
def site(ring, n):
    out = []
    for _ in range(n):
        days = random.gauss(9, 3) if ring else random.gauss(13, 5)
        fail = random.random() < (0.012 if ring else 0.031)
        out.append((max(1, days), fail))
    return out
r, f = site(True, 1000), site(False, 1000)
def p95(x): return sorted(d for d, _ in x)[int(0.95*len(x))]
def fr(x): return sum(fl for _, fl in x) / len(x)
diffs = []
for _ in range(2000):
    rs = [random.choice(r) for _ in r]; fs = [random.choice(f) for _ in f]
    diffs.append(fr(fs) - fr(rs))
diffs.sort()
print(f"ring: 95th pct {p95(r):.1f} days, failure rate {fr(r):.3f}")
print(f"flat: 95th pct {p95(f):.1f} days, failure rate {fr(f):.3f}")
print(f"failure-rate difference {fr(f)-fr(r):.3f}, 95% CI [{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Run with `python3 lab_main.py`. Verified output:

```text
ring: 95th pct 14.1 days, failure rate 0.011
flat: 95th pct 20.7 days, failure rate 0.028
failure-rate difference 0.017, 95% CI [0.005, 0.029]
```

### 5.2 Reading the results

At the ring site, the 95th percentile is 14.1 days and the failure rate 0.011; at the flat site, 20.7 days and 0.028. The failure-rate difference is 0.017 with a bootstrap 95% confidence interval from 0.005 to 0.029, which excludes zero. Both hypotheses are supported in this synthetic data.

Section five point two develops main study and independent validation with a Calder University note Yusuf Adeyemi can demo offline.

Under section five point two, Prof. Ingrid Solberg expects main claims to carry owners and dates.

Section five point two treats main data reading the as testable only when evidence and ticket IDs are recorded.

### 5.3 Baseline adjustment

Baseline months showed the flat site was already about two days slower at the 95th percentile. Yusuf reports both the raw difference and the difference after subtracting baseline, which is smaller but still in favour of rings.

Section five point three develops main study and independent validation with a Calder University note Yusuf Adeyemi can demo offline.

Under section five point three, Prof. Ingrid Solberg expects main claims to carry owners and dates.

Section five point three treats main data reading the as testable only when evidence and ticket IDs are recorded.

### 5.4 Independent validation

A second analyst at Calder, given only the pre-registered plan and the data, reproduces the figures independently.

Section five point four develops main study and independent validation with a Calder University note Yusuf Adeyemi can demo offline.

Under section five point four, Prof. Ingrid Solberg expects main claims to carry owners and dates.

Section five point four treats main data reading the as testable only when evidence and ticket IDs are recorded.

For section five point four, Calder University will not accept main work without a written trail.

### 5.5 Meaning

Fewer failures matter because a failed update on a clinical endpoint can stop work on a ward; faster coverage reduces the window in which known vulnerabilities are exposed.

Section five point five develops main study and independent validation with a Calder University note Yusuf Adeyemi can demo offline.

Under section five point five, Prof. Ingrid Solberg expects main claims to carry owners and dates.

Section five point five treats main data reading the as testable only when evidence and ticket IDs are recorded.

### Secondary outcomes

Pre-registered secondary outcomes include help-desk tickets per update and the share of endpoints never patched within 30 days. Both favour rings in the synthetic data, but Yusuf reports them as secondary and does not let them change the main conclusion.

### Reporting standards

Figures report counts as well as rates, and every number in the text links to the analysis script line that produced it.

### Sensitivity analysis

Yusuf repeats the analysis excluding the 3% of endpoints with imputed reboot times; the results barely change, which supports the main finding.

### Worked example

An examiner asks whether the 0.005 lower bound is practically meaningful. Yusuf converts it: at 1,000 endpoints and 12 monthly cycles, even the lower bound means about 60 fewer failed updates a year.

> **Synthetic case.** Synthetic.

### Errors and limits

Site-level designs cannot rule out unmeasured site differences.

### Exercises

- **EX027 — Lab results.** Report the main figures for both sites. *Rubric:* 3 = ring 14.1/0.011; flat 20.7/0.028; 2 = two; 1 = one; 0 = none.
- **EX028 — Confidence interval.** Give the failure-rate difference and CI. *Rubric:* 3 = 0.017 [0.005, 0.029]; 2 = partial; 1 = none; 0 = none.
- **EX029 — Baseline adjustment.** How was the baseline difference handled? *Rubric:* 3 = report raw and adjusted; 2 = partial; 1 = none; 0 = none.
- **EX030 — Validation.** How was validation done? *Rubric:* 3 = second analyst from plan and data; 2 = partial; 1 = none; 0 = none.
- **EX031 — Practical meaning.** How did Yusuf express the lower bound practically? *Rubric:* 3 = ~60 fewer failures a year; 2 = partial; 1 = none; 0 = none.
- **EX032 — Remaining threat.** Which threat remains? *Rubric:* 3 = unmeasured site differences; 2 = partial; 1 = none; 0 = none.

### Synthesis

Report effects with uncertainty, baseline adjustment and independent validation.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Peer critique and revision

### Learning outcomes

You will (1) respond to peer review; (2) revise claims; (3) strengthen limitations.

### 6.1 The critique

A workshop reviewer argues that the ring site's IT team knew it was being studied and may have worked harder, a Hawthorne effect.

Section six point one develops peer critique and revision with a Calder University note Yusuf Adeyemi can demo offline.

Under section six point one, Prof. Ingrid Solberg expects peer claims to carry owners and dates.

Section six point one treats the critique response second as testable only when evidence and ticket IDs are recorded.

For section six point one, Calder University will not accept peer work without a written trail.

### 6.2 Response

Yusuf checks help-desk staffing and overtime records: they did not differ between sites. He adds this check to the thesis and softens the claim to "consistent with" rather than "caused by".

Section six point two develops peer critique and revision with a Calder University note Yusuf Adeyemi can demo offline.

Under section six point two, Prof. Ingrid Solberg expects peer claims to carry owners and dates.

Section six point two treats the critique response second as testable only when evidence and ticket IDs are recorded.

### 6.3 Second critique

Another reviewer asks whether failures were defined consistently. Yusuf re-codes a random 20% of main-study tickets with a new coder; kappa remains above the pre-registered threshold.

Section six point three develops peer critique and revision with a Calder University note Yusuf Adeyemi can demo offline.

Under section six point three, Prof. Ingrid Solberg expects peer claims to carry owners and dates.

Section six point three treats the critique response second as testable only when evidence and ticket IDs are recorded.

For section six point three, Calder University will not accept peer work without a written trail.

### 6.4 Revision

The paper adds a limitations section on two sites, one sector and synthetic-structure data release.

Section six point four develops peer critique and revision with a Calder University note Yusuf Adeyemi can demo offline.

Under section six point four, Prof. Ingrid Solberg expects peer claims to carry owners and dates.

Section six point four treats the critique response second as testable only when evidence and ticket IDs are recorded.

For section six point four, Calder University will not accept peer work without a written trail.

### 6.5 Tone

Responses thank reviewers and address each point with evidence.

Section six point five develops peer critique and revision with a Calder University note Yusuf Adeyemi can demo offline.

Under section six point five, Prof. Ingrid Solberg expects peer claims to carry owners and dates.

Section six point five treats the critique response second as testable only when evidence and ticket IDs are recorded.

For section six point five, Calder University will not accept peer work without a written trail.

Section six point five fails closed if peer evidence is missing rather than guessing.

### Further review

A third reviewer, a hospital IT manager, asks whether rings delayed urgent patches. Yusuf checks the record: two emergency updates during the study bypassed rings under the trust's emergency process, both reaching all devices within three days. He adds this to the paper, explaining that rings are a default, not a barrier to urgent action.

The revised paper is clearer about when the findings apply and how organisations should handle exceptions.

### Revision log

Every change made in response to critique is recorded in a revision log with the reviewer's point, the evidence and the change, so examiners can trace how the argument evolved.

### Second coder detail

The new coder was trained only on the codebook and had not seen earlier labels, so agreement reflects the codebook rather than shared habits. Disagreements were resolved by discussion and recorded.

### Worked example

Prof. Solberg advises accepting the Hawthorne point openly rather than dismissing it, because the staffing check is reassuring but not conclusive.

> **Synthetic case.** Synthetic.

### Errors and limits

Defensive replies to critique weaken a thesis; evidence-based revisions strengthen it.

### Exercises

- **EX033 — Hawthorne.** What was the Hawthorne critique? *Rubric:* 3 = ring IT team worked harder knowing they were studied; 2 = partial; 1 = none; 0 = none.
- **EX034 — Staffing check.** What evidence addressed it? *Rubric:* 3 = staffing and overtime records equal; 2 = partial; 1 = none; 0 = none.
- **EX035 — Claim change.** How was the claim softened? *Rubric:* 3 = consistent with; 2 = partial; 1 = none; 0 = none.
- **EX036 — Recoding.** How was failure coding re-checked? *Rubric:* 3 = new coder on 20% sample; 2 = partial; 1 = none; 0 = none.
- **EX037 — Limitations.** Which limitations were added? *Rubric:* 3 = two sites, one sector, synthetic-structure data; 2 = two; 1 = one; 0 = none.
- **EX038 — Advice.** What did Prof. Solberg advise? *Rubric:* 3 = accept openly; 2 = partial; 1 = none; 0 = none.

### Synthesis

Revise claims to match evidence after critique.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Thesis synthesis and reproducibility archive

### Learning outcomes

You will (1) synthesise findings across chapters; (2) build a verifiable archive; (3) document data handling.

### 7.1 Synthesis

The thesis argues that staged deployment, a practice many organisations use without evidence, was associated with faster coverage and fewer failures at one trust, with a clear method others can repeat.

Section seven point one develops thesis synthesis and reproducibility archive with a Calder University note Yusuf Adeyemi can demo offline.

Under section seven point one, Prof. Ingrid Solberg expects thesis claims to carry owners and dates.

Section seven point one treats synthesis archive contents reading as testable only when evidence and ticket IDs are recorded.

### 7.2 Archive contents

The archive holds synthetic-structure data, analysis code, the codebook, the pre-registration and a readme.

Section seven point two develops thesis synthesis and reproducibility archive with a Calder University note Yusuf Adeyemi can demo offline.

Under section seven point two, Prof. Ingrid Solberg expects thesis claims to carry owners and dates.

Section seven point two treats synthesis archive contents reading as testable only when evidence and ticket IDs are recorded.

For section seven point two, Calder University will not accept thesis work without a written trail.

### Lab — Lab — archive manifest

```python
"""Build a SHA-256 manifest for a synthetic reproducibility archive (stdlib only)."""
import hashlib
files = {"data/endpoints.csv": b"id,ring,days,fail\n1,0,2,0\n2,1,5,0\n", "data/tickets.csv": b"id,label\n1,reboot\n",
         "code/analysis.py": b"print('analysis')\n", "README.md": b"# Archive\nSynthetic data only.\n"}
for p, c in sorted(files.items()):
    print(f"{hashlib.sha256(c).hexdigest()[:16]}  {len(c):3d} B  {p}")
print(f"files {len(files)}, total {sum(len(c) for c in files.values())} bytes")
```

Run with `python3 lab_archive.py`. Verified output:

```text
670d6080fde1f32f   31 B  README.md
b24ac70c193a18a2   18 B  code/analysis.py
4acf0971a914c415   34 B  data/endpoints.csv
ea54f2468a7e6b17   18 B  data/tickets.csv
files 4, total 101 bytes
```

### 7.3 Reading the manifest

Four files totalling 101 bytes in this small synthetic example each have a SHA-256 digest. Anyone can recompute the digests to confirm files are unchanged.

Section seven point three develops thesis synthesis and reproducibility archive with a Calder University note Yusuf Adeyemi can demo offline.

Under section seven point three, Prof. Ingrid Solberg expects thesis claims to carry owners and dates.

Section seven point three treats synthesis archive contents reading as testable only when evidence and ticket IDs are recorded.

For section seven point three, Calder University will not accept thesis work without a written trail.

### 7.4 Data handling

Real ticket text never enters the archive; only the synthetic-structure dataset with the same distributions is published, approved by the trust.

Section seven point four develops thesis synthesis and reproducibility archive with a Calder University note Yusuf Adeyemi can demo offline.

Under section seven point four, Prof. Ingrid Solberg expects thesis claims to carry owners and dates.

Section seven point four treats synthesis archive contents reading as testable only when evidence and ticket IDs are recorded.

For section seven point four, Calder University will not accept thesis work without a written trail.

### 7.5 Licensing

Code and synthetic data are released under an open licence.

Section seven point five develops thesis synthesis and reproducibility archive with a Calder University note Yusuf Adeyemi can demo offline.

Under section seven point five, Prof. Ingrid Solberg expects thesis claims to carry owners and dates.

Section seven point five treats synthesis archive contents reading as testable only when evidence and ticket IDs are recorded.

For section seven point five, Calder University will not accept thesis work without a written trail.

Section seven point five fails closed if thesis evidence is missing rather than guessing.

### Chapter links

The synthesis links each claim to the chapter and evidence that supports it: the codebook and kappa to chapter 1, the gap to chapter 2, the design to chapter 3, the pipeline checks to chapter 4, the effects to chapter 5 and the revisions to chapter 6. This structure helps examiners verify the argument rather than accept it.

### Verification instructions

The archive readme explains how to recompute the digests, run the analysis on the synthetic data and compare outputs with the thesis tables. A colleague unfamiliar with the work follows these steps and reproduces every table in under an hour.

### Long-term storage

The archive is deposited in Calder's institutional repository with a persistent identifier.

### Access

Anyone can download the archive without registration.

### Worked example

An archivist at Calder recomputes the digests and finds one mismatch caused by a line-ending change during copying. Yusuf fixes the copy process and re-publishes.

> **Synthetic case.** Synthetic.

### Errors and limits

Archives fail silently when files change; digests make change visible.

### Exercises

- **EX039 — Thesis claim.** Summarise the thesis claim. *Rubric:* 3 = staged deployment associated with faster, fewer failures at one trust; 2 = partial; 1 = none; 0 = none.
- **EX040 — Archive parts.** List archive contents. *Rubric:* 3 = data, code, codebook, pre-registration, readme; 2 = four; 1 = two; 0 = none.
- **EX041 — Manifest total.** How many files and bytes in the lab manifest? *Rubric:* 3 = 4 files, 101 bytes; 2 = partial; 1 = none; 0 = none.
- **EX042 — Digest use.** What do digests allow? *Rubric:* 3 = confirm files unchanged; 2 = partial; 1 = none; 0 = none.
- **EX043 — Mismatch cause.** What caused the archivist's mismatch? *Rubric:* 3 = line-ending change; 2 = partial; 1 = none; 0 = none.
- **EX044 — Real text.** Why does real ticket text not enter the archive? *Rubric:* 3 = privacy; synthetic-structure data instead; 2 = partial; 1 = none; 0 = none.

### Synthesis

A verifiable archive makes findings checkable by others.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Defense and publication plan

### Learning outcomes

You will (1) defend the thesis; (2) answer methodological questions; (3) plan publication and practice impact.

### 8.1 Defense

Yusuf presents the problem, design, results, critiques and limits in forty minutes.

Section eight point one develops defense and publication plan with a Calder University note Yusuf Adeyemi can demo offline.

Under section eight point one, Prof. Ingrid Solberg expects defense claims to carry owners and dates.

Section eight point one treats defense questions firmware result as testable only when evidence and ticket IDs are recorded.

For section eight point one, Calder University will not accept defense work without a written trail.

### 8.2 Questions

Examiners ask about generalisation, firmware updates and cost. He answers with evidence and admits where the study cannot answer.

Section eight point two develops defense and publication plan with a Calder University note Yusuf Adeyemi can demo offline.

Under section eight point two, Prof. Ingrid Solberg expects defense claims to carry owners and dates.

Section eight point two treats defense questions firmware result as testable only when evidence and ticket IDs are recorded.

For section eight point two, Calder University will not accept defense work without a written trail.

### 8.3 Firmware result

Firmware updates had a higher failure rate in both arms, supporting SP 800-193's emphasis on recovery mechanisms.

Section eight point three develops defense and publication plan with a Calder University note Yusuf Adeyemi can demo offline.

Under section eight point three, Prof. Ingrid Solberg expects defense claims to carry owners and dates.

Section eight point three treats defense questions firmware result as testable only when evidence and ticket IDs are recorded.

For section eight point three, Calder University will not accept defense work without a written trail.

### 8.4 Publication plan

One journal paper on the main effect, one practitioner report for health IT teams, and the open archive.

Section eight point four develops defense and publication plan with a Calder University note Yusuf Adeyemi can demo offline.

Under section eight point four, Prof. Ingrid Solberg expects defense claims to carry owners and dates.

Section eight point four treats defense questions firmware result as testable only when evidence and ticket IDs are recorded.

For section eight point four, Calder University will not accept defense work without a written trail.

### 8.5 Practice impact

Harrowgate keeps ring deployment and adds firmware-specific recovery checks.

Section eight point five develops defense and publication plan with a Calder University note Yusuf Adeyemi can demo offline.

Under section eight point five, Prof. Ingrid Solberg expects defense claims to carry owners and dates.

Section eight point five treats defense questions firmware result as testable only when evidence and ticket IDs are recorded.

For section eight point five, Calder University will not accept defense work without a written trail.

Section eight point five fails closed if defense evidence is missing rather than guessing.

### 8.6 Ethics reflection

He reflects on balancing research with clinical service: no clinical system was changed solely for research.

Section eight point six develops defense and publication plan with a Calder University note Yusuf Adeyemi can demo offline.

Under section eight point six, Prof. Ingrid Solberg expects defense claims to carry owners and dates.

Section eight point six treats defense questions firmware result as testable only when evidence and ticket IDs are recorded.

For section eight point six, Calder University will not accept defense work without a written trail.

### Answering the cost question

Rings require more planning: defining rings, reviewing failure signals and handling exceptions. Yusuf estimates the trust's added effort at about two staff days per month, compared with the hours saved by fewer failed updates and fewer help-desk tickets. He presents this as a rough estimate, not a full economic evaluation, and suggests a cost study as future work.

### Generalisation

The findings apply most directly to organisations with similar device fleets, central management and staff who share devices. Organisations without central management or with very different fleets would need their own evidence.

### After the defense

Examiners request minor corrections to the limitations section, which Yusuf completes within a month.

### Closing reflection

Yusuf notes that the most valuable habit was pre-registration: it kept him honest when early pilot numbers looked tempting.

### Thanks

He thanks Prof. Solberg and the trust's desktop team.

### Worked example

An examiner asks what he would do with more time. Yusuf proposes a multi-trust study with randomised start dates, which would address site differences.

> **Synthetic case.** Synthetic.

### Errors and limits

Overstating impact in a defense invites hard questions; stay with evidence.

### Exercises

- **EX045 — Questions asked.** Which topics did examiners raise? *Rubric:* 3 = generalisation, firmware, cost; 2 = two; 1 = one; 0 = none.
- **EX046 — Firmware finding.** What did firmware updates show? *Rubric:* 3 = higher failure in both arms; 2 = partial; 1 = none; 0 = none.
- **EX047 — Outputs.** What publications are planned? *Rubric:* 3 = journal paper, practitioner report, archive; 2 = two; 1 = one; 0 = none.
- **EX048 — Trust change.** What did Harrowgate change? *Rubric:* 3 = kept rings, added firmware recovery checks; 2 = partial; 1 = none; 0 = none.
- **EX049 — Future study.** What future design did Yusuf propose? *Rubric:* 3 = multi-trust randomised start dates; 2 = partial; 1 = none; 0 = none.
- **EX050 — Clinical ethics.** What ethical boundary was kept? *Rubric:* 3 = no clinical change solely for research; 2 = partial; 1 = none; 0 = none.

### Synthesis

Defend with evidence and plan impact honestly.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Yusuf Adeyemi, Prof. Ingrid Solberg, Calder University, Harrowgate Health Trust and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Whether ring-based deployment shortens time to patch most endpoints and reduces failures compared with flat deployment.

**EX002.** The 95th-percentile days to patch and the update failure rate.

**EX003.** Observed 0.875, chance 0.296, kappa 0.822.

**EX004.** Almost perfect agreement.

**EX005.** If the application fails only until a reboot, label it reboot.

**EX006.** Tickets are redacted under an approved process before leaving the trust.

**EX007.** As preventive maintenance, planning for speed and disruption risk.

**EX008.** Security fixes tend to be smaller and vulnerabilities can persist for years.

**EX009.** Shared code leaves some copies unpatched long after fixes.

**EX010.** Many incidents come from misconfiguration under time pressure and weak processes.

**EX011.** Their fixes increase the volume and risk of firmware, microcode and OS updates.

**EX012.** Protect, detect and recover.

**EX013.** Comparing deployment strategies within one organisation on both speed and breakage.

**EX014.** Their failure modes differ.

**EX015.** H1: rings reduce 95th-percentile days to patch; H2: rings reduce failure rate.

**EX016.** Shared devices and policies prevent individual randomisation.

**EX017.** Ring 0: 40, ring 1: 160, ring 2: 800.

**EX018.** To measure pre-existing site differences.

**EX019.** Measured effects, a codebook and an open dataset with code.

**EX020.** Site-level policies would mix treatments.

**EX021.** Within one percentage point of the trust's figures.

**EX022.** Ring 0: 2, ring 1: 6, ring 2: 11 days.

**EX023.** Shutdowns instead of restarts; the next boot counts as the reboot.

**EX024.** Its maximum of 16 days is within the 30-day policy.

**EX025.** So changes during the study are recorded.

**EX026.** The effect of the intervention.

**EX027.** Ring: 14.1 days, 0.011; flat: 20.7 days, 0.028.

**EX028.** 0.017, 95% CI 0.005 to 0.029.

**EX029.** Both raw and baseline-adjusted differences are reported.

**EX030.** A second analyst reproduced results from the plan and data alone.

**EX031.** About 60 fewer failed updates per year.

**EX032.** Unmeasured differences between sites.

**EX033.** The ring site's IT team may have worked harder because it was studied.

**EX034.** Staffing and overtime records did not differ.

**EX035.** To "consistent with" rather than "caused by".

**EX036.** A new coder re-labelled a random 20% sample.

**EX037.** Two sites, one sector and synthetic-structure data release.

**EX038.** Accept the Hawthorne point openly.

**EX039.** Staged deployment was associated with faster coverage and fewer failures at one trust.

**EX040.** Synthetic-structure data, code, codebook, pre-registration, readme.

**EX041.** Four files, 101 bytes.

**EX042.** Confirming files are unchanged.

**EX043.** A line-ending change during copying.

**EX044.** To protect privacy; only approved synthetic-structure data is published.

**EX045.** Generalisation, firmware updates and cost.

**EX046.** Higher failure rates in both arms.

**EX047.** A journal paper, a practitioner report and the open archive.

**EX048.** Kept rings and added firmware recovery checks.

**EX049.** A multi-trust study with randomised start dates.

**EX050.** No clinical system was changed solely for research.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Center for Internet Security. (n.d.). *CIS Benchmarks*. <https://www.cisecurity.org/cis-benchmarks>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Cooper, D., Polk, W., Regenscheid, A., & Souppaya, M. (2011). *BIOS protection guidelines* (NIST SP 800-147). NIST. <https://doi.org/10.6028/NIST.SP.800-147>
- Defense Information Systems Agency. (n.d.). *Security Technical Implementation Guides (STIGs)*. <https://public.cyber.mil/stigs/>
- Dietrich, C., Krombholz, K., Borgolte, K., & Fiebig, T. (2018). Investigating system operators' perspective on security misconfigurations. *2018 ACM SIGSAC Conference on Computer and Communications Security (CCS '18)*, 1272–1289. <https://doi.org/10.1145/3243734.3243794>
- Forrest, S., Hofmeyr, S. A., Somayaji, A., & Longstaff, T. A. (1996). A sense of self for Unix processes. *1996 IEEE Symposium on Security and Privacy*, 120–128. <https://doi.org/10.1109/SECPRI.1996.502675>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, A., Dempsey, K., Ross, R., Gupta, S., & Bailey, D. (2011, updated 2019). *Guide for security-focused configuration management of information systems* (NIST SP 800-128). NIST. <https://doi.org/10.6028/NIST.SP.800-128>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kent, K., & Souppaya, M. (2006). *Guide to computer security log management* (NIST SP 800-92). NIST. <https://doi.org/10.6028/NIST.SP.800-92>
- Kernel development community. (n.d.). *Kernel self-protection*. <https://www.kernel.org/doc/html/latest/security/self-protection.html>
- Kim, Y., Daly, R., Kim, J., Fallin, C., Lee, J. H., Lee, D., Wilkerson, C., Lai, K., & Mutlu, O. (2014). Flipping bits in memory without accessing them: An experimental study of DRAM disturbance errors. *41st International Symposium on Computer Architecture (ISCA)*, 361–372. <https://doi.org/10.1109/ISCA.2014.6853210>
- Kocher, P., Horn, J., Fogh, A., Genkin, D., Gruss, D., Haas, W., Hamburg, M., Lipp, M., Mangard, S., Prescher, T., Schwarz, M., & Yarom, Y. (2019). Spectre attacks: Exploiting speculative execution. *2019 IEEE Symposium on Security and Privacy*, 1–19. <https://doi.org/10.1109/SP.2019.00002>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Li, F., & Paxson, V. (2017). A large-scale empirical study of security patches. *2017 ACM SIGSAC Conference on Computer and Communications Security (CCS '17)*, 2201–2215. <https://doi.org/10.1145/3133956.3134072>
- Microsoft. (n.d.). *Windows security baselines*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines>
- Microsoft. (n.d.). *BitLocker overview*. <https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/>
- Microsoft. (n.d.). *Application Control for Windows*. <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol>
- Nappa, A., Johnson, R., Bilge, L., Caballero, J., & Dumitraș, T. (2015). The attack of the clones: A study of the impact of shared code on vulnerability patching. *2015 IEEE Symposium on Security and Privacy*, 692–708. <https://doi.org/10.1109/SP.2015.48>
- Regenscheid, A. (2018). *Platform firmware resiliency guidelines* (NIST SP 800-193). NIST. <https://doi.org/10.6028/NIST.SP.800-193>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., Jansen, W., & Tracy, M. (2008). *Guide to general server security* (NIST SP 800-123). NIST. <https://doi.org/10.6028/NIST.SP.800-123>
- Souppaya, M., & Scarfone, K. (2013). *Guide to malware incident prevention and handling for desktops and laptops* (NIST SP 800-83 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-83r1>
- Souppaya, M., & Scarfone, K. (2022). *Guide to enterprise patch management planning: Preventive maintenance for technology* (NIST SP 800-40 Rev. 4). NIST. <https://doi.org/10.6028/NIST.SP.800-40r4>
