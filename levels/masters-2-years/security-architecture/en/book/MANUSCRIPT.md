# Security Architecture and Engineering: Master's Course

- Language: English (`en`); course 168, Master's course (2 years).
- Editorial state: **draft**. Chapters 1–8 of 8 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: beginning researchers in security architecture and engineering.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs count screening records, compute graph reachability under three synthetic segmentation policies and bootstrap paired results; they never scan or touch a real network. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one master's student comparing identity-based micro-segmentation with zone segmentation in simulated enterprise networks: question and literature method, an advanced seminar, study design and ethics, competing explanations, proposal and pilot, analysis, writing and limitations, and independent review and defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Kenji Albrecht** | Master's student, part-time at Vantor | Invented |
| **Dr Selin Aydın** | Supervisor | Invented |
| **Northmoor University** | Fictional university | Invented |
| **Vantor Logistics** | Fictional employer whose structure shapes the model | Invented |

### Core sources

NIST [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-160 Vol. 1 Rev. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1) and [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5); Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Shostack (2014); Anderson (2020); Wohlin et al. (2012). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Research question and literature method

### Learning outcomes

You will (1) turn an architecture interest into a focused, answerable question; (2) design a documented literature search; (3) screen sources with explicit criteria; (4) record the search so others can repeat it.

### 1.1 From interest to question

Kenji Albrecht is a master's student at the fictional Northmoor University, supervised by Dr Selin Aydın. He works part-time for the fictional Vantor Logistics, whose flat internal network lets almost any workstation reach almost any server. His interest is zero trust architecture, described in NIST SP 800-207, but an interest is not a question. Dr Aydın pushes him to narrow it. After several drafts he settles on this: in simulated enterprise networks shaped like Vantor's, how much does identity-based micro-segmentation reduce the number of servers an attacker can reach from one compromised workstation, compared with zone-based segmentation? Every person, organisation and network here is synthetic.

### 1.2 Why this question works

The question names a population, simulated networks shaped like a real type of enterprise; an intervention, identity-based micro-segmentation; a comparison, zone-based segmentation; and an outcome, reachable servers from one foothold. It can be answered within a master's timeline because it uses simulation rather than changing a production network, and it avoids the ethical and operational risks of testing on live systems. It is also limited: reachability is a proxy for attacker progress, not a measure of real incidents. Kenji writes this limitation into the question document now, so it shapes every later chapter rather than appearing only at the end.

### 1.3 Designing the search

Kenji designs his search before running it. He chooses databases, the IEEE and ACM digital libraries plus NIST publications, and writes search strings combining terms for segmentation, zero trust and lateral movement. He sets inclusion criteria: peer-reviewed studies or official standards from 2010 onward that discuss network segmentation effects on attacker movement. He excludes vendor marketing and opinion pieces, while keeping a separate list of grey literature for context. Writing criteria first prevents him from unconsciously including only studies that agree with what he expects to find, which is a well-known bias in literature reviews.

### 1.4 Screening and recording

His search returns 312 records. Screening titles and abstracts removes those outside scope, and full-text reading removes more. He records the number at each stage, the reasons for exclusion and the date of each search, in a flow table similar to those used in systematic reviews. The lab below reproduces the counts from his screening log. The final set of 27 studies is small, and he notes that most report designs or simulations rather than field measurements. Recording the search makes it repeatable, and it lets examiners judge whether important work could have been missed.

### Lab — Screening flow counts

```python
# Screening flow from a synthetic search log.
log = {"ieee": 141, "acm": 118, "nist": 53}
dupes = 46; title_abstract_out = 197; fulltext_out = 42
total = sum(log.values()); after_d = total - dupes
after_ta = after_d - title_abstract_out; included = after_ta - fulltext_out
for k, v in log.items(): print(f"source {k:5} {v}")
print(f"records {total} -> after duplicates {after_d} -> after title/abstract {after_ta} -> included {included}")
```

Run with `python3 lab_screen.py`. Verified output:

```text
source ieee  141
source acm   118
source nist  53
records 312 -> after duplicates 266 -> after title/abstract 69 -> included 27
```

### 1.5 What the literature says

Kenji summarises themes. Foundational principles, including least privilege and complete mediation from Saltzer and Schroeder (1975), underpin segmentation. NIST SP 800-207 describes policy enforcement points that make access decisions per request. Anderson (2020) gives case studies where flat networks let attackers move widely after one compromise. Simulation studies of attack graphs exist, but few compare segmentation strategies on the same networks with the same assumptions. That gap shapes his contribution: a controlled comparison under stated assumptions, not a claim about how real attackers will behave in every enterprise.

### Worked example

Kenji narrows his interest to a reachability question, writes search strings and criteria in advance, screens 312 records to 27 studies with a flow table and identifies the comparison gap.

> **Synthetic case.** Northmoor University, Vantor Logistics, Kenji, Dr Aydın and screening numbers are invented; SP 800-207, Saltzer and Schroeder (1975) and Anderson (2020) are real.

### Errors and limits

Database choice limits coverage; practitioner knowledge may sit outside indexed literature. Reachability ignores detection and response.

### Exercises

- **EX001 — Question parts.** Name the population, intervention, comparison and outcome in Kenji's question. *Rubric:* 3 = simulated Vantor-like networks; identity micro-segmentation; zone segmentation; reachable servers from one foothold;; 2 = three;; 1 = vague;; 0 = none.
- **EX002 — Simulation choice.** Why use simulation instead of changing Vantor's network? *Rubric:* 3 = fits the timeline and avoids ethical and operational risks to live systems;; 2 = one reason;; 1 = no reason;; 0 = none.
- **EX003 — Proxy limit.** What limitation does Kenji write into the question document? *Rubric:* 3 = reachability is a proxy for attacker progress, not real incidents;; 2 = proxy;; 1 = vague;; 0 = none.
- **EX004 — Criteria first.** Why write inclusion criteria before searching? *Rubric:* 3 = to prevent selectively including agreeable studies;; 2 = bias;; 1 = no reason;; 0 = none.
- **EX005 — Screening lab.** How many records entered screening and how many studies were included? *Rubric:* 3 = 312 records, 27 included;; 2 = one number;; 1 = wrong;; 0 = none.
- **EX006 — Flat-network evidence.** What does Anderson (2020) contribute to Kenji's review? *Rubric:* 3 = case studies where flat networks allowed wide movement after one compromise;; 2 = cases;; 1 = nothing;; 0 = none.
- **EX007 — Comparison gap.** What gap did Kenji identify? *Rubric:* 3 = few studies compare segmentation strategies on the same networks under the same assumptions;; 2 = gap;; 1 = vague;; 0 = none.

### Synthesis

A good master's question is narrow, answerable and honest about its proxy, and a recorded literature search shows where it adds something new.

### Continue studying — chapter 01 of 08

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Security architecture and engineering: advanced seminar

### Learning outcomes

You will (1) compare enterprise, systems-engineering and threat-driven views of security architecture; (2) relate design principles to segmentation; (3) critique a framework claim; (4) present a seminar argument with evidence.

### 2.1 Three views of architecture

In Dr Aydın's seminar, Kenji meets three ways of seeing security architecture. The enterprise view, represented by SABSA and The Open Group's TOGAF guide on integrating risk and security, starts from business attributes and traces them down to controls. The systems-engineering view, represented by NIST SP 800-160 Vol. 1 Rev. 1, treats security as an emergent property engineered across the life cycle with explicit assurance cases. The threat-driven view, represented by Shostack (2014), starts from what can go wrong in a specific design. Each view asks a different first question, and good architects move between them deliberately.

### 2.2 Principles behind segmentation

Segmentation applies older principles. Least privilege says each workstation should reach only the services it needs. Complete mediation says every access should be checked, which SP 800-207 implements through policy enforcement points. Separation of privilege suggests that sensitive access should need more than one condition, such as device health and user identity. Economy of mechanism warns against policies so complex that nobody can verify them. Kenji notices that the last principle pulls against the others: finer segmentation enforces least privilege better but creates more rules, and every unmanaged rule is a potential gap.

### 2.3 Critiquing a framework claim

A seminar reading claims that adopting zero trust eliminates lateral movement. Kenji critiques it. SP 800-207 itself describes zero trust as a set of principles and a journey rather than a single product, and it acknowledges threats to zero trust deployments, such as compromise of the policy decision point and stolen credentials. Lateral movement can continue with a valid identity on an allowed path. The fair claim is narrower: zero trust can reduce reachable paths and make movement easier to observe. He presents this distinction with direct quotation of the publication's threats section rather than paraphrase from secondary sources.

### 2.4 Evidence in seminar argument

Dr Aydın asks every presenter to tag claims as principle, framework guidance, case evidence or measured result. Kenji's slides carry small tags. When a classmate claims that micro-segmentation always reduces incidents, Kenji asks which tag applies, and the answer is principle plus vendor case studies, not measurement. The exercise is uncomfortable but useful: it shows the class how much of architecture practice rests on reasoning and experience rather than measured outcomes, which is acceptable as long as it is stated plainly and not dressed up as proof.

### 2.5 Seminar output

Kenji's seminar paper argues that segmentation strategies should be compared on reachability and on rule complexity together, because a strategy that reduces reach but needs thousands of unmanageable rules may fail in operation. He proposes measuring both in his dissertation. The class challenges him to define complexity; he chooses the number of distinct allow rules as a simple, imperfect measure, and lists its weaknesses. The paper becomes the conceptual chapter of his dissertation, and the challenge from classmates becomes one of the competing explanations he will test later.

### Worked example

Kenji contrasts three architecture views, maps four Saltzer and Schroeder principles to segmentation, critiques the claim that zero trust eliminates lateral movement and proposes measuring reach together with rule count.

> **Synthetic case.** Seminar participants and claims are synthetic; SABSA, TOGAF G152, SP 800-160v1r1, SP 800-207 and Shostack (2014) are real.

### Errors and limits

Rule count is a crude proxy for operational complexity. Seminar tagging can oversimplify mixed evidence.

### Exercises

- **EX008 — First questions.** What first question does each architecture view ask? *Rubric:* 3 = enterprise: business attributes; systems engineering: life-cycle assurance; threat-driven: what can go wrong;; 2 = two;; 1 = one;; 0 = none.
- **EX009 — Principle tension.** Which principle pulls against fine segmentation, and why? *Rubric:* 3 = economy of mechanism, because finer segmentation creates more rules to verify;; 2 = named;; 1 = vague;; 0 = none.
- **EX010 — Zero trust threats.** Name a threat to zero trust deployments acknowledged in SP 800-207. *Rubric:* 3 = compromise of the policy decision point or stolen credentials;; 2 = one;; 1 = vague;; 0 = none.
- **EX011 — Fair zero trust claim.** What is the fair version of zero trust eliminates lateral movement? *Rubric:* 3 = it can reduce reachable paths and make movement easier to observe;; 2 = reduced;; 1 = eliminates;; 0 = none.
- **EX012 — Evidence tags.** Which four tags does Dr Aydın require on claims? *Rubric:* 3 = principle, framework guidance, case evidence, measured result;; 2 = three;; 1 = one;; 0 = none.
- **EX013 — Complexity measure.** How does Kenji measure rule complexity, and what is its weakness? *Rubric:* 3 = count of distinct allow rules; crude proxy;; 2 = measure;; 1 = vague;; 0 = none.
- **EX014 — Dual outcome reason.** Why compare strategies on reach and rule count together? *Rubric:* 3 = a strategy can reduce reach but be unmanageable in operation;; 2 = both;; 1 = reach only;; 0 = none.

### Synthesis

An advanced seminar trains the student to move between architecture views, tie designs to principles and tag every claim by the kind of evidence behind it.

### Continue studying — chapter 02 of 08

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Study design, ethics and reproducibility

### Learning outcomes

You will (1) design a simulation study with controlled comparisons; (2) build a reachability model on synthetic networks; (3) address ethics when a real organisation shapes the model; (4) plan reproducibility from the start.

### 3.1 Simulation design

Kenji designs his study as a controlled simulation. He generates many synthetic networks whose structure resembles Vantor's: departments of workstations, shared servers, a few administrative jump hosts and a domain controller. For each network he applies three policies: flat, zone-based with department zones and identity-based micro-segmentation. The outcome is the number of servers reachable from a randomly chosen compromised workstation. Generating many networks rather than one guards against conclusions that depend on a single arbitrary layout, and comparing all three policies on the same network removes variation that has nothing to do with the policy.

### 3.2 The reachability model

A network is modelled as a directed graph: an edge from host A to host B means policy allows A to connect to B. An attacker on a workstation can reach anything connected by a path, assuming each hop is exploitable. That assumption is deliberately pessimistic, giving an upper bound on reach. The lab below builds one small synthetic network under the three policies and counts reachable servers with a breadth-first search. The results show the pattern Kenji expects: flat access reaches every server, zones reach fewer, identity-based rules fewer still, but jump hosts reopen paths if their rules are broad.

### Lab — Reachability under three policies

```python
# Count servers reachable from one compromised workstation under three synthetic policies (BFS).
from collections import deque
ws = ["ws-fin1", "ws-fin2", "ws-ops1", "ws-ops2"]
srv = {"erp": "fin", "payroll": "fin", "wms": "ops", "fleet": "ops", "files": "all", "dc": "all"}
dept = lambda h: h[3:6]
def edges(policy, broad_jump=False):
    E = {h: set() for h in ws + list(srv) + ["jump"]}
    for w in ws:
        for s, d in srv.items():
            if policy == "flat" or (policy == "zone" and d in (dept(w), "all")) \
               or (policy == "identity" and s == {"fin": "erp", "ops": "wms"}[dept(w)]):
                E[w].add(s)
        if policy == "identity": E[w].add("jump")
    if broad_jump: E["jump"] |= set(srv)
    return E
def reach(E, start):
    seen, q = {start}, deque([start])
    while q:
        for n in E[q.popleft()]:
            if n not in seen: seen.add(n); q.append(n)
    return len([n for n in seen if n in srv])
for p in ["flat", "zone", "identity"]:
    print(f"{p:9} servers reachable from ws-fin1: {reach(edges(p), 'ws-fin1')}")
print(f"identity + broad jump-host rule: {reach(edges('identity', True), 'ws-fin1')}")
```

Run with `python3 lab_reach.py`. Verified output:

```text
flat      servers reachable from ws-fin1: 6
zone      servers reachable from ws-fin1: 4
identity  servers reachable from ws-fin1: 1
identity + broad jump-host rule: 6
```

### 3.3 Ethics with a real partner

Although the networks are synthetic, they are shaped by Vantor's real structure, which is sensitive information. Kenji obtains his employer's written permission, agrees that no real hostnames, addresses or rules will appear in the dissertation and abstracts the structure into parameters such as department counts and server ratios. His ethics application states that no human participants are involved and that no testing touches Vantor systems. He also considers dual use: a detailed map of where Vantor is weakest would help attackers, so the dissertation reports only aggregate patterns across generated networks.

### 3.4 Reproducibility plan

From the first day, Kenji keeps code in version control, fixes random seeds for every experiment and records the parameters of each run in a configuration file stored alongside the results. He writes a short script that reruns all experiments from scratch and checks that summary numbers match the stored ones. He records software versions. Dr Aydın asks him to try running the whole pipeline on a clean machine halfway through the project, which reveals one missing dependency. Planning reproducibility early is far cheaper than reconstructing it before submission, when memory of past decisions has faded.

### 3.5 Pre-specifying analysis

Before running the main experiments, Kenji writes his analysis plan: the primary comparison is identity-based versus zone-based mean reach, with a bootstrap confidence interval; secondary measures are rule count and the effect of jump-host rule breadth. He commits the plan in his repository with a timestamp. Exploratory analyses are allowed later but must be labelled. This discipline matters even in simulation, because with many parameters it is easy to search until some setting shows a striking difference and then present it as if it had been the plan all along.

### Worked example

Kenji designs a three-policy simulation on generated networks, runs the reachability lab, writes an ethics plan that abstracts Vantor's structure and commits an analysis plan with seeds and configurations.

> **Synthetic case.** Vantor's structure parameters and the lab network are synthetic.

### Errors and limits

Assuming every hop is exploitable overstates reach; real attackers face patching and detection. Generated networks may miss unusual real topologies.

### Exercises

- **EX015 — Same-network comparison.** Why apply all three policies to the same generated network? *Rubric:* 3 = removes variation unrelated to policy;; 2 = control;; 1 = no reason;; 0 = none.
- **EX016 — Edge meaning.** What does an edge from A to B mean in the model? *Rubric:* 3 = policy allows A to connect to B;; 2 = allowed connection;; 1 = physical cable;; 0 = none.
- **EX017 — Pessimistic bound.** Why is assuming every hop exploitable called pessimistic? *Rubric:* 3 = it gives an upper bound on attacker reach;; 2 = upper bound;; 1 = optimistic;; 0 = none.
- **EX018 — Lab reach counts.** What reachable-server counts did the lab print for flat, zone and identity policies? *Rubric:* 3 = flat 6, zone 4, identity 1;; 2 = two correct;; 1 = wrong;; 0 = none.
- **EX019 — Jump host effect.** What did the lab show when the jump host's rules were broad? *Rubric:* 3 = reach rose again to 6, reopening paths;; 2 = rose;; 1 = no change;; 0 = none.
- **EX020 — Dual-use concern.** How does Kenji handle the dual-use risk of his findings? *Rubric:* 3 = reports only aggregate patterns, no Vantor-specific weak points;; 2 = aggregate;; 1 = publishes map;; 0 = none.

### Synthesis

A sound simulation study controls comparisons, states pessimistic assumptions, protects partner information and fixes its analysis and seeds in advance.

### Continue studying — chapter 03 of 08

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Security architecture and engineering: competing explanations

### Learning outcomes

You will (1) list rival explanations for an expected result; (2) design checks that distinguish them; (3) recognise artefacts of modelling choices; (4) decide in advance what would change your conclusion.

### 4.1 Rivals to the main hypothesis

Kenji expects identity-based micro-segmentation to reduce reach. Before testing, he lists rivals that could produce the same pattern. First, the difference might come from the number of allowed edges alone, not from identity: any policy with fewer edges would look better. Second, it might depend on network size, appearing only in small networks. Third, it might be an artefact of how he generated identity rules, giving each workstation exactly one server. Fourth, results could hinge on jump hosts, which the lab in chapter 3 showed can erase the benefit. Each rival predicts something different that he can check.

### 4.2 Checks that separate rivals

For the edge-count rival, Kenji adds a control policy: random edges removed from the flat network until it has the same number of edges as the identity policy. If identity still beats this random control, structure matters, not just edge count. For the size rival, he generates networks at three sizes. For the generation artefact, he varies how many servers each identity may reach, from one to four. For jump hosts, he varies their rule breadth. Each check is a small experiment written into the plan before the main runs, so the dissertation can report which rivals survived.

### 4.3 Modelling artefacts

Simulation results can reflect modelling choices rather than reality. Kenji's model treats every host as equally exploitable, ignores time and assumes policies are enforced perfectly. If real enforcement points are misconfigured a fraction of the time, identity policies with many fine rules may leak more than zone policies with few broad ones. He adds a misconfiguration parameter that randomly adds a small share of unintended edges. This connects back to the economy-of-mechanism concern from the seminar: complex rule sets offer more chances for error, and the model should be able to show that trade-off rather than assume it away.

### 4.4 What would change the conclusion

Kenji writes down, before seeing results, what would make him conclude that identity-based segmentation does not offer a meaningful advantage: if its mean reach is within one server of the random-edge control, or if a misconfiguration rate of two per cent erases most of the difference. Writing these thresholds in advance protects him from moving the goalposts after seeing the data. Dr Aydın notes that most master's dissertations never state such conditions, and that doing so is one of the clearest signs of research maturity an examiner can see.

### 4.5 Discussing rivals with practitioners

Kenji presents his rival list to two Vantor network engineers. They add a rival he had missed: in practice, identity-based rules are often written by copying templates, so many workstations end up with the same broad access, reducing the benefit. He adds a template parameter that makes a share of workstations inherit a broad rule set. Practitioners know failure modes that literature rarely records, and asking them early improves the model's realism. He acknowledges their contribution in the dissertation without naming them, as agreed.

### Worked example

Kenji lists five rivals, adds a random-edge control, size and generation variations, a misconfiguration rate and a template-copy parameter, and writes thresholds that would overturn his expectation.

> **Synthetic case.** Rivals, thresholds and engineer input are synthetic.

### Errors and limits

No list of rivals is complete. Parameters added to model reality can multiply runs and tempt selective reporting.

### Exercises

- **EX021 — Edge-count rival.** What does the random-edge control test? *Rubric:* 3 = whether identity's advantage comes from structure or just fewer edges;; 2 = structure;; 1 = nothing;; 0 = none.
- **EX022 — Generation artefact.** How does Kenji test the identity-rule generation artefact? *Rubric:* 3 = varies how many servers each identity may reach from one to four;; 2 = varies;; 1 = ignores;; 0 = none.
- **EX023 — Misconfiguration parameter.** Why add a misconfiguration rate to the model? *Rubric:* 3 = real enforcement errs, and complex rule sets offer more chances for error;; 2 = errors;; 1 = not needed;; 0 = none.
- **EX024 — Overturn thresholds.** State one pre-set condition that would overturn Kenji's expectation. *Rubric:* 3 = identity within one server of random control, or two per cent misconfiguration erasing most of the gain;; 2 = one;; 1 = vague;; 0 = none.
- **EX025 — Practitioner rival.** Which rival did the engineers add? *Rubric:* 3 = template copying gives many workstations the same broad access;; 2 = template;; 1 = vague;; 0 = none.
- **EX026 — Maturity sign.** What does Dr Aydın call a clear sign of research maturity? *Rubric:* 3 = stating in advance what would change the conclusion;; 2 = advance conditions;; 1 = long thesis;; 0 = none.

### Synthesis

Listing rivals, testing each with a designed check and fixing overturn conditions in advance turns an expected result into a tested one.

### Continue studying — chapter 04 of 08

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Proposal and pilot

### Learning outcomes

You will (1) write a concise dissertation proposal; (2) run a pilot to test code and parameters; (3) estimate how many simulated networks are needed; (4) adjust the plan from pilot evidence.

### 5.1 The proposal

Kenji's proposal fits on six pages. It states the question, the three policies and the random-edge control, the outcomes of mean reach and rule count, the rival checks and overturn thresholds, the ethics agreement with Vantor and the timeline. It lists deliverables: a dissertation, a code repository with fixed seeds and a short practitioner brief. Dr Aydın asks him to cut the background section in half and expand the methods, because reviewers judge feasibility by methods. The committee approves it with one condition: a pilot must confirm that the simulation runs within the available computing time.

### 5.2 Pilot goals

The pilot runs the full pipeline on twenty small networks. Its goals are practical: confirm that the code produces sensible reach values, check the run time per network, find bugs and measure how much results vary between networks. It is not meant to answer the question. Kenji writes a test that compares the breadth-first search with a simple brute-force count on tiny networks where the right answer can be checked by hand, a known-answer test similar in spirit to test vectors. The test catches a bug in which jump-host edges were added twice, inflating reach in one policy.

### 5.3 How many networks

Using the pilot's variation, Kenji estimates how many networks he needs for the main comparison. The standard deviation of the difference between identity and zone reach across pilot networks is about two servers. To estimate the mean difference within about half a server with ninety-five per cent confidence, he needs roughly sixty networks per size. He chooses two hundred per size to allow for the extra parameters from the rival checks. Run time from the pilot shows this fits easily on a laptop overnight, so the committee's computing condition is met.

### 5.4 Adjusting the plan

The pilot also shows that at the smallest network size, zone and identity policies often give identical reach because each department has only one server. Kenji drops that size and adds a larger one, documenting the change and its reason in his plan's change log. He also discovers that the misconfiguration parameter at ten per cent makes all policies nearly flat, so he limits the range to zero to five per cent, a range the Vantor engineers consider realistic. Each adjustment is recorded before the main runs begin.

### 5.5 Pilot reporting

Kenji's pilot report is two pages: what was run, what was found, what changed and why. It includes the bug found by the known-answer test and the dropped network size. Dr Aydın stresses that the report should be honest about problems, because examiners trust a study more when they can see how it was debugged. The report becomes an appendix to the dissertation. Kenji also tags the code version used for the pilot in his repository, so the main experiments start from a known, tested state rather than from code still changing.

### Worked example

Kenji writes a six-page proposal, pilots twenty networks, fixes a double-counted jump-host bug with a known-answer test, sizes the main study at two hundred networks per size and logs two plan adjustments.

> **Synthetic case.** Pilot numbers and committee decisions are synthetic.

### Errors and limits

Sample-size estimates from a small pilot are themselves uncertain. Dropping a network size changes the population the results describe.

### Exercises

- **EX027 — Committee condition.** What condition did the committee attach to approval? *Rubric:* 3 = a pilot confirming the simulation fits the available computing time;; 2 = pilot;; 1 = vague;; 0 = none.
- **EX028 — Known-answer bug.** What bug did the known-answer test catch? *Rubric:* 3 = jump-host edges added twice, inflating reach;; 2 = jump-host;; 1 = vague;; 0 = none.
- **EX029 — Networks needed.** How many networks per size did the estimate require, and how many were chosen? *Rubric:* 3 = about sixty needed; two hundred chosen;; 2 = one figure;; 1 = wrong;; 0 = none.
- **EX030 — Dropped size.** Why was the smallest network size dropped? *Rubric:* 3 = one server per department made zone and identity reach identical;; 2 = reason;; 1 = vague;; 0 = none.
- **EX031 — Misconfiguration range.** What range was set for misconfiguration, and why? *Rubric:* 3 = zero to five per cent, considered realistic by engineers;; 2 = range;; 1 = ten per cent;; 0 = none.
- **EX032 — Tagging pilot code.** Why tag the pilot code version? *Rubric:* 3 = so main experiments start from a known tested state;; 2 = known state;; 1 = no reason;; 0 = none.

### Synthesis

A short proposal and an honest pilot turn a research plan into a tested pipeline with a justified sample size.

### Continue studying — chapter 05 of 08

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Data collection and analysis

### Learning outcomes

You will (1) run the main simulation and collect results reproducibly; (2) compare policies with bootstrap confidence intervals; (3) evaluate rival checks; (4) present results without overstating them.

### 6.1 Running the main study

Kenji runs two hundred networks at each of three sizes, applying the flat, zone, identity and random-edge policies, with the rival parameters varied as planned. Every run writes its configuration, seed and results to a file, and the rerun script confirms that a random sample of runs reproduces exactly. He resists the urge to look at results while runs are still incomplete, because early peeking tends to shape later decisions. When all runs finish, he computes the pre-specified primary comparison first, before any exploratory analysis, and records the time he did so.

### 6.2 Bootstrap comparison

The primary comparison is the mean difference in reachable servers between zone and identity policies on the same networks. Kenji uses a bootstrap: he resamples networks with replacement many times, recomputes the mean difference each time and takes the middle ninety-five per cent of those values as a confidence interval. The bootstrap needs few assumptions about the shape of the data. The lab below runs this procedure on synthetic paired results for one network size and also compares identity with the random-edge control, reporting both intervals and the mean rule counts.

### Lab — Bootstrap comparison of policies

```python
# Bootstrap CIs for paired synthetic results (servers reachable) across 200 generated networks.
import random, statistics
random.seed(42)
nets = []
for _ in range(200):
    zone = random.randint(4, 9); ident = max(0, zone - random.choice([1, 2, 2, 3, 3, 4]))
    ctrl = max(ident, ident + random.choice([0, 1, 2, 2, 3]))
    nets.append((zone, ident, ctrl, random.randint(18, 26), random.randint(60, 75)))
def boot(diffs, B=4000):
    m = [statistics.mean(random.choices(diffs, k=len(diffs))) for _ in range(B)]; m.sort()
    return statistics.mean(diffs), m[int(.025 * B)], m[int(.975 * B)]
for name, i in [("zone - identity", 0), ("control - identity", 2)]:
    est, lo, hi = boot([n[i] - n[1] for n in nets])
    print(f"{name:20} mean {est:.2f}  95% CI [{lo:.2f}, {hi:.2f}]")
print(f"mean rules: zone {statistics.mean(n[3] for n in nets):.1f}, identity {statistics.mean(n[4] for n in nets):.1f}")
```

Run with `python3 lab_compare.py`. Verified output:

```text
zone - identity      mean 2.43  95% CI [2.29, 2.56]
control - identity   mean 1.56  95% CI [1.42, 1.71]
mean rules: zone 22.2, identity 67.7
```

### 6.3 Rival checks

The random-edge control reaches noticeably more servers than identity, so structure, not just edge count, explains much of the benefit. The advantage holds across network sizes, though it shrinks for the smallest remaining size. Allowing identities to reach up to four servers reduces but does not remove the advantage. Template copying is the strongest rival: when a third of workstations inherit a broad rule set, most of the advantage disappears. Misconfiguration at five per cent narrows the gap but leaves it above Kenji's overturn threshold. He reports each rival check in a table with its result.

### 6.4 The complexity trade-off

Identity policies need many more allow rules than zone policies: in the lab, roughly three times as many on average. Kenji presents reach and rule count side by side, so readers can see the trade-off rather than only the security gain. He does not claim to know how many rules an organisation can manage, but he notes that the template-copy result suggests organisations often cope with rule complexity by copying, which undermines the benefit. This connects the quantitative results back to the economy-of-mechanism principle discussed in the seminar.

### 6.5 Presenting results honestly

Kenji's results chapter states effects with intervals, explains what each check showed and labels any exploratory analysis. He avoids saying identity segmentation is secure or that zone segmentation is insecure. He writes that, under the model's assumptions, identity-based segmentation reduced worst-case reach from a single compromised workstation compared with zone segmentation, that much of this gain depended on avoiding template-copied broad rules, and that it required about three times as many rules. That sentence is longer than a headline, but every word is supported by a reported result.

### Worked example

Kenji runs six hundred networks, computes bootstrap intervals for zone minus identity and random control minus identity, reports rival checks in a table and presents reach with rule counts.

> **Synthetic case.** All results are from synthetic simulations.

### Errors and limits

Bootstrap intervals describe variation across generated networks, not uncertainty about real enterprises. Exploratory findings need confirmation.

### Exercises

- **EX033 — Early peeking.** Why avoid looking at results before runs finish? *Rubric:* 3 = early peeking tends to shape later decisions;; 2 = bias;; 1 = no reason;; 0 = none.
- **EX034 — Bootstrap steps.** Describe the bootstrap Kenji uses. *Rubric:* 3 = resample networks with replacement, recompute mean difference, take middle 95%;; 2 = partial;; 1 = vague;; 0 = none.
- **EX035 — Lab intervals.** What mean differences did the lab report for zone minus identity and control minus identity? *Rubric:* 3 = about 2.4 and 1.6 servers, both intervals above zero;; 2 = one;; 1 = wrong;; 0 = none.
- **EX036 — Strongest rival.** Which rival check removed most of the advantage? *Rubric:* 3 = template copying of broad rules for a third of workstations;; 2 = template;; 1 = size;; 0 = none.
- **EX037 — Rule ratio.** Roughly how many more rules did identity policies need than zone policies in the lab? *Rubric:* 3 = about three times as many;; 2 = ratio;; 1 = fewer;; 0 = none.
- **EX038 — Supported sentence.** Why does Kenji avoid calling identity segmentation secure? *Rubric:* 3 = results only support reduced modelled reach under assumptions, with conditions;; 2 = conditional;; 1 = it is secure;; 0 = none.

### Synthesis

Careful analysis reports pre-specified comparisons with intervals, tests every rival and keeps security gains and operational costs side by side.

### Continue studying — chapter 06 of 08

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Dissertation writing and limitations

### Learning outcomes

You will (1) structure a dissertation around its argument; (2) write limitations that are specific and useful; (3) connect findings to architecture practice responsibly; (4) prepare a practitioner brief.

### 7.1 Structure around the argument

Kenji structures his dissertation so each chapter supports one step of the argument: the question and its gap, the conceptual chapter from the seminar, the method and pilot, the results and rival checks, and the discussion. He writes the discussion first in outline, then checks that every claim in it points back to a result. Claims without support are cut or moved to future work. Dr Aydın reminds him that examiners read the abstract, introduction and conclusion closely and look for any mismatch with the results chapter, so those three sections must be written last and checked line by line.

### 7.2 Specific limitations

Kenji's limitations are concrete. The model assumes every hop is exploitable, so reach is an upper bound. Networks were generated from parameters abstracted from one employer and may not represent organisations with very different structures, such as hospitals with many legacy devices. Policies were assumed to be enforced exactly except for the misconfiguration parameter. Time, detection and response were not modelled. Rule count is a crude measure of complexity. For each limitation he states its likely direction of effect on his findings, which helps readers judge whether it weakens or strengthens the conclusions.

### 7.3 Connecting to practice

In the discussion, Kenji relates findings to standards without overreaching. NIST SP 800-207 recommends per-request access decisions; his results suggest that the benefit depends heavily on avoiding broad template rules. SP 800-53 Rev. 5 includes controls for boundary protection and least privilege, and his complexity result suggests organisations should plan for rule management, not only rule creation. He frames these as considerations for architects, not as requirements. He also states that his study cannot say whether real attackers would exploit the paths his model found, which only field evidence could establish.

### 7.4 The practitioner brief

Kenji writes a two-page brief for Vantor and similar organisations. It explains in plain language that, in simulations shaped like their network, identity-based segmentation reduced how far an attacker could move from one compromised laptop, but that copying broad rule templates removed most of the benefit, and that identity rules were about three times as many to manage. It recommends piloting on one department with rule reviews. It links to the full dissertation and lists the limitations. He checks the brief with Dr Aydın to ensure it says nothing the dissertation does not support.

### 7.5 Writing process

Kenji writes in short daily sessions, keeping a list of open questions at the top of each chapter file. He sends chapters to Dr Aydın one at a time and records her comments and his responses in a table, as he will later be asked to do for examiners. A classmate reads the results chapter without context and marks every sentence she cannot verify from a table or figure; Kenji rewrites those sentences. This cold-reader check catches assumptions that the author no longer notices because he has lived with the work for months.

### Worked example

Kenji outlines the discussion first, cuts unsupported claims, writes five specific limitations with their direction of effect, relates findings to SP 800-207 and SP 800-53 Rev. 5 and drafts a checked two-page brief.

> **Synthetic case.** The dissertation drafts and reader comments are synthetic; SP 800-207 and SP 800-53 Rev. 5 are real.

### Errors and limits

Direction-of-effect statements are themselves judgements. Practitioner briefs risk being read without their limitations.

### Exercises

- **EX039 — Last sections.** Which sections are written last and why? *Rubric:* 3 = abstract, introduction, conclusion, so they match results;; 2 = named;; 1 = first;; 0 = none.
- **EX040 — Limitation direction.** Why state the likely direction of each limitation's effect? *Rubric:* 3 = helps readers judge whether it weakens or strengthens conclusions;; 2 = direction;; 1 = not needed;; 0 = none.
- **EX041 — SP 800-53 link.** What does Kenji's complexity result suggest regarding SP 800-53 Rev. 5 boundary controls? *Rubric:* 3 = plan for rule management, not only rule creation;; 2 = management;; 1 = nothing;; 0 = none.
- **EX042 — Field evidence gap.** What can only field evidence establish? *Rubric:* 3 = whether real attackers would exploit the modelled paths;; 2 = real attackers;; 1 = simulation shows;; 0 = none.
- **EX043 — Brief recommendation.** What does the brief recommend Vantor do? *Rubric:* 3 = pilot on one department with rule reviews;; 2 = pilot;; 1 = full rollout;; 0 = none.
- **EX044 — Cold reader.** What did the cold-reader check catch? *Rubric:* 3 = sentences not verifiable from a table or figure;; 2 = unsupported;; 1 = typos;; 0 = none.

### Synthesis

A dissertation persuades when every claim traces to a result, limitations are specific and practitioner advice stays within the evidence.

### Continue studying — chapter 07 of 08

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Independent review and defense

### Learning outcomes

You will (1) obtain independent review of code and results; (2) prepare for an oral defense; (3) respond to examiner criticism; (4) plan follow-up work.

### 8.1 Independent code review

Before submission, a doctoral student in another group reviews Kenji's code using only the repository and its documentation. She reruns all experiments from scratch on her machine and matches the stored summaries, which confirms reproducibility. She also finds that the random-edge control removed edges from the flat network uniformly, whereas a fairer control might preserve each workstation's degree. Kenji adds this alternative control as a sensitivity analysis; it narrows the identity advantage slightly but leaves it clear. He acknowledges the reviewer and records the change in his revision table.

### 8.2 Preparing the defense

Kenji lists likely questions: why simulation instead of field data, why breadth-first reach rather than attack likelihood, how parameters were chosen, what would change his conclusion and how practitioners should use the results. For each he prepares a short answer pointing to a section and a result. He rehearses with two classmates, who interrupt and challenge. Dr Aydın advises him to answer the question asked rather than the one he prepared, to admit uncertainty plainly and to use the overturn thresholds he wrote in chapter 4 as evidence of his discipline.

### 8.3 Responding to criticism

In the defense, the external examiner argues that reachability without exploit likelihood exaggerates differences between policies. Kenji agrees that reach is an upper bound, explains why he chose it for tractability and transparency, and suggests weighting edges by exploit likelihood as future work. A second examiner asks whether the template-copy rival undermines the whole recommendation. Kenji answers that it qualifies it: identity segmentation helps only if rule management prevents broad templates, which is a practical finding in itself. The examiners accept the dissertation with minor corrections.

### 8.4 Corrections and archiving

Kenji completes corrections within the allowed time: clarifying the bootstrap description, adding the degree-preserving control to the main text and expanding the discussion of exploit likelihood. He archives the final code, configurations and results with a persistent identifier from his university repository and includes a SHA-256 manifest of the archived files. Vantor reviews the final version and confirms that no sensitive structure is revealed. The archive allows others to rerun or extend the study with different network shapes. It also lets examiners and later readers check that the published numbers came from the archived code.

### 8.5 Follow-up work

Kenji lists follow-up studies: weighting edges by exploit likelihood, modelling detection and response time, testing on network shapes from other sectors and running a field pilot at Vantor that measures real rule counts and access attempts. He offers the code to another student. His reflection notes that the most useful moments were when his expectations were challenged, by the random control, by the template-copy rival and by the examiner's critique, because each made his final claim smaller but much more defensible. He now treats a challenged expectation as progress rather than as a setback.

### Worked example

Kenji's code is rerun by an independent reviewer, a degree-preserving control is added, he defends the upper-bound choice and template finding and archives the corrected study with a manifest.

> **Synthetic case.** Reviewers, examiners and outcomes are synthetic.

### Errors and limits

Independent rerun confirms reproducibility, not validity of assumptions. Minor corrections can still change emphasis.

### Exercises

- **EX045 — Rerun confirmation.** What did the independent reviewer's rerun confirm? *Rubric:* 3 = reproducibility: results matched stored summaries;; 2 = matched;; 1 = validity;; 0 = none.
- **EX046 — Fairer control.** What fairer control did the reviewer suggest and with what effect? *Rubric:* 3 = degree-preserving random control; narrowed advantage slightly but it stayed clear;; 2 = control;; 1 = removed advantage;; 0 = none.
- **EX047 — Upper-bound defense.** How did Kenji answer the exaggeration criticism? *Rubric:* 3 = agreed reach is an upper bound, chosen for tractability, suggested likelihood weighting;; 2 = agreement plus reason;; 1 = denied;; 0 = none.
- **EX048 — Template qualifies.** How did Kenji frame the template-copy finding? *Rubric:* 3 = it qualifies the recommendation: benefit requires rule management against broad templates;; 2 = qualifies;; 1 = undermines;; 0 = none.
- **EX049 — Archive contents.** What does Kenji's archive contain? *Rubric:* 3 = final code, configurations, results and a SHA-256 manifest;; 2 = three items;; 1 = data from Vantor;; 0 = none.
- **EX050 — Valued moments.** Which moments does Kenji find most useful in reflection? *Rubric:* 3 = when expectations were challenged by control, rival and examiner;; 2 = challenged;; 1 = praise;; 0 = none.

### Synthesis

Independent review and a candid defense make a master's result smaller, stronger and ready for others to build on.

### Continue studying — chapter 08 of 08

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Kenji Albrecht, Dr Selin Aydın, Northmoor University, Vantor Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Population: simulated networks like Vantor's; intervention: identity-based micro-segmentation; comparison: zone segmentation; outcome: servers reachable from one compromised workstation.

**EX002.** It fits a master's timeline and avoids the risks of experimenting on a production network.

**EX003.** That reachability only approximates attacker progress and does not measure real incidents.

**EX004.** To avoid unconsciously choosing only studies that support the expected answer.

**EX005.** 312 records were screened and 27 studies were included.

**EX006.** Case studies showing attackers moving widely through flat networks after a single compromise.

**EX007.** Few studies compare segmentation strategies on identical networks with identical assumptions.

**EX008.** Enterprise asks which business attributes matter; systems engineering asks how security is engineered and assured across the life cycle; threat-driven asks what can go wrong in this design.

**EX009.** Economy of mechanism, since finer segmentation multiplies rules that must be understood and verified.

**EX010.** Compromise of the policy decision or enforcement components, or misuse of stolen valid credentials.

**EX011.** That zero trust can reduce the paths available and make lateral movement easier to detect, not eliminate it.

**EX012.** Principle, framework guidance, case evidence and measured result.

**EX013.** By the number of distinct allow rules, which is a crude proxy that ignores rule interaction and change frequency.

**EX014.** Because a strategy that cuts reach but needs unmanageable rules may fail in practice.

**EX015.** To ensure differences in reach come from the policy rather than from different network layouts.

**EX016.** That the policy permits host A to open a connection to host B.

**EX017.** Because it assumes the attacker always succeeds at each hop, so the result is an upper bound on reach.

**EX018.** Flat reached 6 servers, zone reached 4 and identity-based reached 1.

**EX019.** With a broad jump-host rule, identity-based reach rose back to 6 servers, showing jump hosts can reopen paths.

**EX020.** He reports only aggregate patterns across generated networks, never a map of Vantor's specific weaknesses.

**EX021.** Whether identity segmentation helps because of its structure rather than simply because it allows fewer edges.

**EX022.** By varying the number of servers each workstation identity may reach, from one to four.

**EX023.** Because real policies are sometimes misconfigured, and fine-grained rule sets give more opportunities for such errors.

**EX024.** If identity's mean reach is within one server of the random-edge control.

**EX025.** That identity rules are often copied from templates, giving many workstations the same broad access.

**EX026.** Writing down, before seeing results, the observations that would change the conclusion.

**EX027.** That a pilot must show the simulation runs within the available computing time.

**EX028.** Jump-host edges were being added twice, inflating reach under one policy.

**EX029.** About sixty per size were needed; Kenji chose two hundred to allow for the rival checks.

**EX030.** Because each department had only one server, so zone and identity policies gave identical reach.

**EX031.** Zero to five per cent, because ten per cent made all policies nearly flat and engineers judged the lower range realistic.

**EX032.** So the main experiments begin from a tested, identifiable version of the code.

**EX033.** Because seeing partial results tends to influence later analysis choices.

**EX034.** He resamples networks with replacement many times, recomputes the mean difference and uses the middle 95% of values as the interval.

**EX035.** Zone minus identity was about 2.4 servers and random control minus identity about 1.6 (2.43 and 1.56), both with intervals above zero.

**EX036.** Template copying, when a third of workstations inherited a broad rule set.

**EX037.** About three times as many allow rules.

**EX038.** Because the evidence supports only reduced modelled reach under stated assumptions and conditions, not a general security claim.

**EX039.** The abstract, introduction and conclusion, so they can be checked against the final results.

**EX040.** So readers can see whether each limitation would likely shrink or enlarge the reported effect.

**EX041.** That organisations should plan to manage rules over time, not just create them.

**EX042.** Whether real attackers would actually use the paths the model found.

**EX043.** Pilot identity segmentation in one department with regular rule reviews.

**EX044.** Sentences that could not be verified from any table or figure.

**EX045.** That the experiments reproduce exactly from the repository and documentation.

**EX046.** A control preserving each workstation's degree; it narrowed the identity advantage slightly but left it clear.

**EX047.** He agreed reach is an upper bound, explained it was chosen for tractability and transparency, and proposed likelihood-weighted edges as future work.

**EX048.** As a qualification: identity segmentation helps only when rule management prevents broad template rules.

**EX049.** The final code, run configurations, results and a SHA-256 manifest of the files.

**EX050.** The moments when his expectations were challenged, which made his claim smaller but more defensible.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- The Open Group. (2016, revised 2022). *Integrating risk and security within a TOGAF enterprise architecture* (TOGAF Series Guide G152). The Open Group.
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
