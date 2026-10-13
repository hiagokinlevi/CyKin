# Systems, Endpoint and Hardware Security: Engineering Course

- Language: English (`en`); course 127, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; Nine offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students learning to design, build, verify and operate hardened, self-restoring endpoint systems from first principles.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only servers, endpoints and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, inventories, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one engineering student from a public library PC where a patron's CV and bank statement were left behind, through mathematics, physics, programming, operating systems and security foundations, to requirements, boot-chain models, scenario analysis, hardening, restore implementation, measurement, application control, reliability, validation, trials and a thesis defense. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Mateo Rossi** | Engineering student | Invented |
| **Dr Hana Novak** | Supervisor | Invented |
| **Marta Silva** | IT lead at the partner | Invented |
| **Ardmore Institute of Technology** | Fictional institute | Invented |
| **Fernhill Library Network** | Fictional public library network | Invented |

### Core sources

NIST [SP 800-123](https://doi.org/10.6028/NIST.SP.800-123), [SP 800-40r4](https://doi.org/10.6028/NIST.SP.800-40r4), [SP 800-128](https://doi.org/10.6028/NIST.SP.800-128), [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5) and [SP 800-193](https://doi.org/10.6028/NIST.SP.800-193); [CIS Controls v8](https://www.cisecurity.org/controls/v8) and [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); DISA [STIGs](https://public.cyber.mil/stigs/); Microsoft [Windows security baselines](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines); Linux [kernel self-protection](https://www.kernel.org/doc/html/latest/security/self-protection.html). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |
| [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) use rates of change to describe how endpoint problems grow; (2) read simple functions of time; (3) connect calculus ideas to the course's engineering project.

### 1.1 The project behind the course

Mateo Rossi is an engineering student at the fictional Ardmore Institute of Technology. Throughout this five-year course he works with the fictional Fernhill Library Network, which offers 300 public-access computers across three branches: Central, Eastgate and Millbrook. Last spring a patron found another person's CV and bank statement left on a public PC, and staff regularly find toolbars and games installed by users. Fernhill's IT lead, Marta Silva, wants a public PC service that resets itself to a known, hardened state every night. Mateo's supervisor, Dr Hana Novak, agrees that this will be his running engineering project.

### 1.2 Rates of change

Calculus studies how quantities change. If unwanted software accumulates on unmanaged PCs at a roughly steady rate, the number of affected PCs grows linearly with time; if one infected PC spreads problems to others on the same network, growth can become faster than linear. The derivative describes the rate at that moment.

Section one point two develops calculus with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section one point two, Marta Silva expects calculus claims to carry owners and dates.

### 1.3 Functions of time

Mateo models the share of PCs with leftover personal files as a function f(t) of days since the last manual clean-up. Fernhill's records suggest about three new cases per day across the network, so f grows by roughly one per cent of the fleet each day until staff intervene.

Section one point three develops calculus with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section one point three, Marta Silva expects calculus claims to carry owners and dates.

### 1.4 Why rates matter for design

A nightly restore resets f to zero every 24 hours. Instead of letting problems accumulate for weeks, the design limits exposure to a single day. Thinking in rates makes the benefit of frequent resets visible.

Section one point four develops calculus with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section one point four, Marta Silva expects calculus claims to carry owners and dates.

Section one point four treats the project behind the as testable only when evidence and ticket IDs are recorded.

### 1.5 Limits and approximation

Real data are noisy; a smooth function is an approximation. Engineers use it to reason, then check it against measurements.

Section one point five develops calculus with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section one point five, Marta Silva expects calculus claims to carry owners and dates.

Section one point five treats the project behind the as testable only when evidence and ticket IDs are recorded.

For section one point five, Fernhill Library Network will not accept calculus work without a written trail.

### Worked example

Mateo plots Fernhill's manual clean-up records over three months. Between clean-ups, the count of PCs with leftover files rises almost linearly, about three per day, then drops to near zero after each clean-up. He sketches the same curve under nightly restore: a saw-tooth that never rises above a day's worth of cases.

> **Synthetic case.** Mateo, Dr Novak, Marta and Fernhill are synthetic.

### Errors and limits

A model fitted to a few months may not hold during busy periods such as exam season.

### Exercises

- **EX001 — Project goal.** What does Marta want the public PC service to do? *Rubric:* 3 = reset nightly to known hardened state; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Growth rate.** How fast did leftover-file cases grow between clean-ups? *Rubric:* 3 = about three per day, roughly linear; 2 = partial; 1 = none; 0 = none.
- **EX003 — Saw-tooth.** Describe the curve under nightly restore. *Rubric:* 3 = saw-tooth limited to one day's cases; 2 = partial; 1 = none; 0 = none.

### Synthesis

Rates of change show why frequent resets limit exposure.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) use sets, logic and graphs to describe endpoint configurations; (2) reason about allowlists as sets; (3) model a network of PCs as a graph.

### 2.1 Sets of software

The software allowed on a public PC forms a set A. The software actually executed during a week forms a set E. Anything in E but not in A, written E minus A, is unauthorised. This simple set difference is the core of application control, which Mateo will design later.

Section two point one develops discrete mathematics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section two point one, Marta Silva expects discrete claims to carry owners and dates.

### 2.2 Logic for requirements

Requirements can be written as logical statements: "if a PC is public, then USB storage is disabled". Writing them precisely avoids ambiguity, such as whether staff PCs are included.

Section two point two develops discrete mathematics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section two point two, Marta Silva expects discrete claims to carry owners and dates.

Section two point two treats sets of software logic as testable only when evidence and ticket IDs are recorded.

For section two point two, Fernhill Library Network will not accept discrete work without a written trail.

### 2.3 Graphs

Fernhill's network can be drawn as a graph: PCs, switches and servers are nodes; network links are edges. A graph shows which PCs can reach each other. If public PCs can reach staff laptops directly, a problem on one could affect the other.

Section two point three develops discrete mathematics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section two point three, Marta Silva expects discrete claims to carry owners and dates.

Section two point three treats sets of software logic as testable only when evidence and ticket IDs are recorded.

### 2.4 Counting configurations

With ten yes-or-no settings, there are 2 to the power 10, or 1,024, possible configurations. Only one is the approved baseline. Counting shows why drift is likely without automation: many ways to be wrong, one way to be right.

Section two point four develops discrete mathematics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section two point four, Marta Silva expects discrete claims to carry owners and dates.

Section two point four treats sets of software logic as testable only when evidence and ticket IDs are recorded.

### 2.5 Proof habits

Discrete mathematics trains careful reasoning: stating assumptions, checking edge cases and not generalising from a few examples.

Section two point five develops discrete mathematics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section two point five, Marta Silva expects discrete claims to carry owners and dates.

Section two point five treats sets of software logic as testable only when evidence and ticket IDs are recorded.

For section two point five, Fernhill Library Network will not accept discrete work without a written trail.

### Applying it to the project

Mateo writes the first draft of the public PC rules in logical form: every public PC must run only software in A, must have USB storage disabled and must reset nightly. Writing them this way exposes a question nobody had asked: are the catalogue kiosks public PCs? Marta decides they are, so the rules apply to them too.

### Worked example

Mateo draws Fernhill's network graph and finds that public PCs and staff laptops share one network segment at Eastgate. He records this as a design question: should public PCs be on their own segment, so the graph has no edge between them and staff devices?

> **Synthetic case.** Synthetic network.

### Errors and limits

A graph from documentation may miss links added later; verify against switch configurations.

### Exercises

- **EX004 — Set difference.** What does E minus A represent? *Rubric:* 3 = executed but not allowed software; 2 = partial; 1 = none; 0 = none.
- **EX005 — Configurations.** How many configurations do ten yes/no settings allow? *Rubric:* 3 = 1,024; 2 = partial; 1 = none; 0 = none.
- **EX006 — Eastgate graph.** What did the graph reveal at Eastgate? *Rubric:* 3 = public PCs and staff laptops share segment; 2 = partial; 1 = none; 0 = none.

### Synthesis

Sets, logic and graphs make endpoint rules and connections precise.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical properties of hardware to security; (2) explain storage persistence and power; (3) understand why hardware can fail or leak.

### 3.1 Storage persistence

Data on solid-state drives and hard disks persist without power. Deleting a file usually removes only its index, not the data. This is why a patron's "deleted" CV may still be recoverable, and why Fernhill needs full restores and disk encryption rather than relying on users to delete files.

Section three point one develops physics for computing with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section three point one, Marta Silva expects physics claims to carry owners and dates.

### 3.2 Memory and power

Memory loses its contents when power is removed, but not instantly; this is one reason why encryption keys are protected while devices are running and why devices should lock or shut down when unattended.

Section three point two develops physics for computing with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section three point two, Marta Silva expects physics claims to carry owners and dates.

Section three point two treats storage persistence memory and as testable only when evidence and ticket IDs are recorded.

### 3.3 Physical disturbance

Kim et al. (2014) showed that repeatedly accessing rows in DRAM can flip bits in neighbouring rows, a physical effect of densely packed memory cells. It shows that hardware behaviour can create security problems that software alone did not expect.

Section three point three develops physics for computing with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section three point three, Marta Silva expects physics claims to carry owners and dates.

Section three point three treats storage persistence memory and as testable only when evidence and ticket IDs are recorded.

### 3.4 Heat and reliability

Heat shortens component life. Public PCs in small enclosures fail more often, which matters when planning reliability in chapter 32.

Section three point four develops physics for computing with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section three point four, Marta Silva expects physics claims to carry owners and dates.

Section three point four treats storage persistence memory and as testable only when evidence and ticket IDs are recorded.

For section three point four, Fernhill Library Network will not accept physics work without a written trail.

### 3.5 Physical access

Anyone at a public PC has physical access: they can attach devices, reboot or open firmware menus. Physical security and firmware settings matter as much as software.

Section three point five develops physics for computing with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section three point five, Marta Silva expects physics claims to carry owners and dates.

Section three point five treats storage persistence memory and as testable only when evidence and ticket IDs are recorded.

For section three point five, Fernhill Library Network will not accept physics work without a written trail.

### Encryption and physical theft

Because physical access is unavoidable at a public PC, disk encryption matters if a machine is stolen. Encryption turns the stored data into unreadable form without the key, which the TPM releases only to the expected boot chain. This links physics, architecture and cryptography, topics later chapters develop.

### Worked example

Marta asks why staff could not just delete leftover files each evening. Mateo explains that deletion leaves data recoverable, whereas restoring the disk from a clean image overwrites the patron area, and encryption protects data if a disk is removed.

> **Synthetic case.** Synthetic.

### Errors and limits

Physical effects are complex; engineers rely on published research rather than speculation.

### Exercises

- **EX007 — Deletion.** Why is a deleted file often recoverable? *Rubric:* 3 = only index removed; 2 = partial; 1 = none; 0 = none.
- **EX008 — Kim 2014.** What did Kim et al. (2014) show? *Rubric:* 3 = DRAM row access flips neighbouring bits; 2 = partial; 1 = none; 0 = none.
- **EX009 — Physical access.** Why does physical access matter at public PCs? *Rubric:* 3 = attach devices, reboot, firmware menus; 2 = partial; 1 = none; 0 = none.

### Synthesis

Hardware physics shapes what software controls can promise.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small Python programs that read records and check conditions; (2) structure code with functions; (3) test with known answers.

### 4.1 Why program

Fernhill's 300 PCs cannot be checked by hand each day. Small programs that read configuration records and report problems make checks repeatable.

Section four point one develops programming with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section four point one, Marta Silva expects programming claims to carry owners and dates.

Section four point one treats why program variables and as testable only when evidence and ticket IDs are recorded.

For section four point one, Fernhill Library Network will not accept programming work without a written trail.

### 4.2 Variables and types

Settings come as text, numbers and true-or-false values. A program must compare like with like: "15" as text is not the number 15.

Section four point two develops programming with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section four point two, Marta Silva expects programming claims to carry owners and dates.

Section four point two treats why program variables and as testable only when evidence and ticket IDs are recorded.

For section four point two, Fernhill Library Network will not accept programming work without a written trail.

### 4.3 Functions

A function such as check(pc, requirements) returns a list of gaps. Writing it once and calling it for every PC avoids copying code.

Section four point three develops programming with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section four point three, Marta Silva expects programming claims to carry owners and dates.

Section four point three treats why program variables and as testable only when evidence and ticket IDs are recorded.

For section four point three, Fernhill Library Network will not accept programming work without a written trail.

### 4.4 Testing with known answers

Before running on real data, Mateo tests his function on two synthetic PCs: one that meets every requirement and one that fails exactly two. If the output matches, he trusts the function more.

Section four point four develops programming with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section four point four, Marta Silva expects programming claims to carry owners and dates.

Section four point four treats why program variables and as testable only when evidence and ticket IDs are recorded.

### 4.5 Standard library only

The course labs use only Python's standard library, so they run on any machine and introduce no unreviewed code.

Section four point five develops programming with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section four point five, Marta Silva expects programming claims to carry owners and dates.

Section four point five treats why program variables and as testable only when evidence and ticket IDs are recorded.

For section four point five, Fernhill Library Network will not accept programming work without a written trail.

### Reading code before running

Mateo reads every script before running it, including examples from the course. He asks what the script reads, what it writes and whether it changes anything. All course labs only read synthetic records and print results. This habit protects real systems from mistakes and from code that does more than it claims.

He also learns to keep output short and ordered: counts first, details second.

### Linking to the project

Mateo's first useful program reads a list of synthetic PC records and prints those whose USB storage setting is enabled. It is short, but it already answers a real question that Marta used to answer by walking round branches. Later chapters extend it into the hardening and restore checks.

### Worked example

Mateo's first check reports every PC as failing auto-logoff. He discovers that the records store minutes as text. Converting to numbers fixes it, and he adds a test case with text input.

> **Synthetic case.** Synthetic.

### Errors and limits

Programs fail silently when data types differ; test with realistic inputs.

### Exercises

- **EX010 — Repetition.** Why program the checks? *Rubric:* 3 = 300 PCs daily, repeatable; 2 = partial; 1 = none; 0 = none.
- **EX011 — Known-answer test.** Describe Mateo's known-answer test. *Rubric:* 3 = one passing PC, one failing exactly two; 2 = partial; 1 = none; 0 = none.
- **EX012 — Bug.** What caused every PC to fail auto-logoff? *Rubric:* 3 = minutes stored as text; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small, tested programs make checks repeatable.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write clear engineering documents; (2) tailor communication to library staff and managers; (3) record decisions.

### 5.1 Audiences

Marta needs technical detail; branch managers need to know what changes for patrons; the library board needs costs and benefits. One project, three kinds of document.

Section five point one develops engineering communication with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section five point one, Marta Silva expects engineering claims to carry owners and dates.

Section five point one treats audiences problem statements decision as testable only when evidence and ticket IDs are recorded.

For section five point one, Fernhill Library Network will not accept engineering work without a written trail.

### 5.2 Problem statements

Mateo writes a one-paragraph problem statement: personal files left on public PCs and unauthorised software, caused by PCs that keep changes indefinitely.

Section five point two develops engineering communication with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section five point two, Marta Silva expects engineering claims to carry owners and dates.

Section five point two treats audiences problem statements decision as testable only when evidence and ticket IDs are recorded.

For section five point two, Fernhill Library Network will not accept engineering work without a written trail.

### 5.3 Decision records

Each design decision is recorded with options, choice and reasons, so later readers understand why.

Section five point three develops engineering communication with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section five point three, Marta Silva expects engineering claims to carry owners and dates.

Section five point three treats audiences problem statements decision as testable only when evidence and ticket IDs are recorded.

For section five point three, Fernhill Library Network will not accept engineering work without a written trail.

### 5.4 Plain language

Avoid jargon with staff: say "the computer resets itself overnight" rather than "non-persistent image restore".

Section five point four develops engineering communication with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section five point four, Marta Silva expects engineering claims to carry owners and dates.

Section five point four treats audiences problem statements decision as testable only when evidence and ticket IDs are recorded.

For section five point four, Fernhill Library Network will not accept engineering work without a written trail.

### 5.5 Diagrams

A simple diagram of the nightly cycle helps everyone see the plan.

Section five point five develops engineering communication with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section five point five, Marta Silva expects engineering claims to carry owners and dates.

Section five point five treats audiences problem statements decision as testable only when evidence and ticket IDs are recorded.

For section five point five, Fernhill Library Network will not accept engineering work without a written trail.

Section five point five fails closed if engineering evidence is missing rather than guessing.

### Writing for the board

For the board, Mateo writes a one-page brief: the problem in two sentences, what the project will change, expected benefits in plain terms and costs in staff time and equipment. He avoids technical terms and offers a short demonstration on a lab PC. The board approves the project and asks for a progress update each quarter, which becomes part of his communication plan.

The brief and later updates are stored with the project's decision records.

### Listening

Communication runs both ways. Mateo visits each branch to hear librarians describe daily problems, which shapes the requirements.

### Writing technical notes

Technical notes for Marta use numbered steps, exact settings and expected results. Each note names the image version it applies to. When a librarian reports a problem, Marta can check the note to see what should be true and compare it with the PC.

### Worked example

A branch manager asks whether patrons will lose work. Mateo writes a one-line notice for screens: "This computer resets overnight; save your work to your own storage or email." Staff test it with patrons and adjust wording.

> **Synthetic case.** Synthetic.

### Errors and limits

Technical accuracy without clarity leads to misunderstanding and resistance.

### Exercises

- **EX013 — Three audiences.** Which three audiences need different documents? *Rubric:* 3 = Marta, branch managers, board; 2 = two; 1 = one; 0 = none.
- **EX014 — Decision records.** What does a decision record contain? *Rubric:* 3 = options, choice, reasons; 2 = two; 1 = one; 0 = none.
- **EX015 — Patron notice.** What notice did Mateo draft? *Rubric:* 3 = resets overnight; save to own storage; 2 = partial; 1 = none; 0 = none.

### Synthesis

Communicate decisions clearly to each audience.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use accumulation and integrals to estimate total exposure; (2) compare designs by area under a curve.

### 6.1 Accumulation

If f(t) is the number of PCs holding leftover personal data at time t, the area under f over a month estimates total exposure in PC-days. Integrals measure accumulation.

Section six point one develops calculus ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section six point one, Marta Silva expects calculus claims to carry owners and dates.

Section six point one treats accumulation manual clean-up nightly as testable only when evidence and ticket IDs are recorded.

### 6.2 Manual clean-up

With three new cases a day and fortnightly clean-ups, f rises from 0 to about 42 and drops: each fortnight's area is a triangle of about (14 × 42) / 2 = 294 PC-days.

Section six point two develops calculus ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section six point two, Marta Silva expects calculus claims to carry owners and dates.

Section six point two treats accumulation manual clean-up nightly as testable only when evidence and ticket IDs are recorded.

For section six point two, Fernhill Library Network will not accept calculus work without a written trail.

### 6.3 Nightly restore

With nightly resets, each day's triangle is (1 × 3) / 2 = 1.5 PC-days, or 21 per fortnight, far smaller.

Section six point three develops calculus ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section six point three, Marta Silva expects calculus claims to carry owners and dates.

Section six point three treats accumulation manual clean-up nightly as testable only when evidence and ticket IDs are recorded.

For section six point three, Fernhill Library Network will not accept calculus work without a written trail.

### 6.4 Comparing designs

The ratio, about 14 to 1, quantifies the benefit. Engineers often compare designs by such areas: total exposure, total downtime or total cost.

Section six point four develops calculus ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section six point four, Marta Silva expects calculus claims to carry owners and dates.

Section six point four treats accumulation manual clean-up nightly as testable only when evidence and ticket IDs are recorded.

For section six point four, Fernhill Library Network will not accept calculus work without a written trail.

### 6.5 Assumptions

The estimate assumes steady arrival of cases and full removal at each reset. Chapter 28 tests the second assumption.

Section six point five develops calculus ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section six point five, Marta Silva expects calculus claims to carry owners and dates.

Section six point five treats accumulation manual clean-up nightly as testable only when evidence and ticket IDs are recorded.

For section six point five, Fernhill Library Network will not accept calculus work without a written trail.

### Checking with data

Mateo compares the integral estimate with Fernhill's records. Over two fortnights of manual clean-ups, staff found 39 and 45 PCs with leftover files, close to the model's peak of about 42. The match gives some confidence in the steady-arrival assumption for normal weeks. He notes that exam season brought more cases, so the model would underestimate exposure then.

The same reasoning, accumulating a quantity over time, appears later for downtime in chapter 32.

### Units

He states units carefully: PC-days for exposure, PC-hours for downtime.

### Beyond exposure

Integrals also estimate total effort. If staff spend about 20 minutes per manual clean-up of a PC, the fortnightly effort grows with the number of affected PCs. Nightly restore removes most of this effort, linking Calculus II to objective O4 in chapter 20.

### Worked example

Dr Novak asks Mateo to state the result honestly. He writes: "Under steady-arrival assumptions, nightly restore reduces exposure from about 294 to about 21 PC-days per fortnight."

> **Synthetic case.** Synthetic.

### Errors and limits

Integrals of idealised functions give estimates, not measurements.

### Exercises

- **EX016 — Area meaning.** What does the area under f represent? *Rubric:* 3 = total exposure in PC-days; 2 = partial; 1 = none; 0 = none.
- **EX017 — Fortnight estimates.** Give the fortnight exposure for both designs. *Rubric:* 3 = 294 vs 21 PC-days; 2 = partial; 1 = none; 0 = none.
- **EX018 — Assumptions.** Which assumptions underlie the estimate? *Rubric:* 3 = steady arrival, full removal; 2 = partial; 1 = none; 0 = none.

### Synthesis

Accumulation compares designs by total exposure.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) model independent failures with the binomial distribution; (2) interpret probabilities for operations; (3) plan alerting.

### 7.1 Failure probability

Even a reliable restore job can fail. If each PC's nightly restore fails independently with probability p, the number of failures among n PCs follows a binomial distribution.

Section seven point one develops probability and statistics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seven point one, Marta Silva expects probability claims to carry owners and dates.

Section seven point one treats failure probability reading the as testable only when evidence and ticket IDs are recorded.

For section seven point one, Fernhill Library Network will not accept probability work without a written trail.

### Lab — Lab — restore failures

```python
"""Probability that at least k of n public PCs fail a nightly restore, binomial model (stdlib only)."""
from math import comb
n, p = 300, 0.004
for k in (1, 3, 5):
    pk = 1 - sum(comb(n, i) * p**i * (1-p)**(n-i) for i in range(k))
    print(f"P(at least {k} of {n} fail | p={p}) = {pk:.3f}")
print(f"expected failures per night {n*p:.1f}")
```

Run with `python3 lab_binomial.py`. Verified output:

```text
P(at least 1 of 300 fail | p=0.004) = 0.700
P(at least 3 of 300 fail | p=0.004) = 0.120
P(at least 5 of 300 fail | p=0.004) = 0.008
expected failures per night 1.2
```

### 7.2 Reading the result

With 300 PCs and p = 0.004, the expected number of failures per night is 1.2. The chance of at least one failure is 0.700, of at least three 0.120, and of at least five 0.008.

Section seven point two develops probability and statistics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seven point two, Marta Silva expects probability claims to carry owners and dates.

Section seven point two treats failure probability reading the as testable only when evidence and ticket IDs are recorded.

### 7.3 Operational meaning

Most nights at least one PC will fail to restore, so the design needs an alert and a simple fix. Five or more failures would be very unusual and suggest a shared cause, such as a bad image.

Section seven point three develops probability and statistics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seven point three, Marta Silva expects probability claims to carry owners and dates.

Section seven point three treats failure probability reading the as testable only when evidence and ticket IDs are recorded.

### 7.4 Independence

The binomial model assumes failures are independent. A network outage would break that assumption, causing many failures together.

Section seven point four develops probability and statistics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seven point four, Marta Silva expects probability claims to carry owners and dates.

Section seven point four treats failure probability reading the as testable only when evidence and ticket IDs are recorded.

For section seven point four, Fernhill Library Network will not accept probability work without a written trail.

### Measuring p

The value p = 0.004 is an assumption for planning. Once the pilot runs, Mateo will measure the actual failure rate from restore logs and update the model. If real failures cluster, for example at one branch, the independence assumption is wrong and alerts should consider branch-level patterns.

This cycle, assume, measure, revise, recurs throughout the course.

### Variance

The binomial variance n·p·(1−p) is about 1.2, so nightly counts of zero, one or two failures are all normal.

### Using the alert rule

The rule is written into the runbook in chapter 37 and tested in chapter 47's trial, where a deliberately bad image causes many failures at once and triggers the incident alert as predicted. This shows how a probability model becomes an operational tool.

### Worked example

Marta asks how to set the alert. Mateo proposes: alert per PC for any failure, and a separate "incident" alert if five or more fail in one night, since that probability is under 1% when the system is healthy.

> **Synthetic case.** Synthetic probability p.

### Errors and limits

Real failure probabilities must be measured; p here is an assumption.

### Exercises

- **EX019 — Expected failures.** What is the expected number of failures per night? *Rubric:* 3 = 1.2; 2 = partial; 1 = none; 0 = none.
- **EX020 — Probabilities.** Give P(at least 1), P(at least 3), P(at least 5). *Rubric:* 3 = 0.700, 0.120, 0.008; 2 = two; 1 = one; 0 = none.
- **EX021 — Incident threshold.** Why alert as an incident at five failures? *Rubric:* 3 = under 1% if healthy, suggests shared cause; 2 = partial; 1 = none; 0 = none.

### Synthesis

Probability models turn reliability into sensible alert thresholds.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) describe processors, memory, firmware and boot; (2) explain privilege levels; (3) relate architecture to security features.

### 8.1 Components

A PC has a processor, memory, storage, firmware (UEFI) and peripherals. Firmware starts first, initialises hardware and loads the bootloader, which loads the operating system.

Section eight point one develops computer architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eight point one, Marta Silva expects computer claims to carry owners and dates.

Section eight point one treats components privilege levels speculative as testable only when evidence and ticket IDs are recorded.

For section eight point one, Fernhill Library Network will not accept computer work without a written trail.

### 8.2 Privilege levels

Processors separate privileged kernel code from user code. User programs cannot directly change kernel memory; this separation underpins operating system security.

Section eight point two develops computer architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eight point two, Marta Silva expects computer claims to carry owners and dates.

Section eight point two treats components privilege levels speculative as testable only when evidence and ticket IDs are recorded.

For section eight point two, Fernhill Library Network will not accept computer work without a written trail.

### 8.3 Speculative execution

Kocher et al. (2019) showed that processors executing instructions speculatively can leak data across these boundaries. Vendors responded with microcode and operating system updates, which public PCs must receive.

Section eight point three develops computer architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eight point three, Marta Silva expects computer claims to carry owners and dates.

Section eight point three treats components privilege levels speculative as testable only when evidence and ticket IDs are recorded.

For section eight point three, Fernhill Library Network will not accept computer work without a written trail.

### 8.4 Trusted Platform Module

Many PCs include a TPM, a small chip that stores keys and records measurements of boot components. It supports disk encryption and boot integrity checks.

Section eight point four develops computer architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eight point four, Marta Silva expects computer claims to carry owners and dates.

Section eight point four treats components privilege levels speculative as testable only when evidence and ticket IDs are recorded.

For section eight point four, Fernhill Library Network will not accept computer work without a written trail.

### 8.5 Firmware settings

UEFI settings control boot order, Secure Boot and passwords. If patrons can change boot order, they can start other operating systems.

Section eight point five develops computer architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eight point five, Marta Silva expects computer claims to carry owners and dates.

Section eight point five treats components privilege levels speculative as testable only when evidence and ticket IDs are recorded.

For section eight point five, Fernhill Library Network will not accept computer work without a written trail.

### Firmware as a target

Firmware runs before the operating system and can control what loads. If firmware or its settings are changed, every later protection can be bypassed. This is why NIST SP 800-147 recommends authenticated firmware updates and SP 800-193 adds detection and recovery. For Fernhill, the practical steps are firmware passwords, Secure Boot and keeping firmware updated through the vendor's signed packages.

### Microcode

Processor microcode updates, delivered with firmware or OS updates, address issues such as speculative execution flaws.

### Checking firmware versions

Mateo records firmware versions for each PC model and compares them with vendors' latest signed releases. Twelve PCs at Millbrook are two versions behind and are scheduled for update in a quiet week.

### Worked example

Mateo inventories Fernhill's PC models and finds all have TPM 2.0 and UEFI Secure Boot support, but firmware passwords are not set. He notes this as a design input.

> **Synthetic case.** Synthetic inventory.

### Errors and limits

Hardware features help only if enabled and configured.

### Exercises

- **EX022 — Boot order.** In what order do firmware, bootloader and OS start? *Rubric:* 3 = firmware, bootloader, OS; 2 = partial; 1 = none; 0 = none.
- **EX023 — TPM role.** What does a TPM provide? *Rubric:* 3 = key storage, boot measurements; 2 = partial; 1 = none; 0 = none.
- **EX024 — Inventory finding.** What did the inventory reveal? *Rubric:* 3 = TPM and Secure Boot supported; no firmware passwords; 2 = partial; 1 = none; 0 = none.

### Synthesis

Architecture features become controls only when configured.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure larger programs; (2) use dictionaries, files and hashing; (3) handle errors carefully.

### 9.1 Data structures

Dictionaries map names to values, such as file paths to digests. Lists hold ordered records. Most of Mateo's checks use both.

Section nine point one develops programming ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nine point one, Marta Silva expects programming claims to carry owners and dates.

Section nine point one treats data structures hashing files as testable only when evidence and ticket IDs are recorded.

For section nine point one, Fernhill Library Network will not accept programming work without a written trail.

### 9.2 Hashing

A cryptographic hash such as SHA-256 produces a fixed-length digest; any change to a file changes its digest. Comparing digests is a fast way to detect changes.

Section nine point two develops programming ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nine point two, Marta Silva expects programming claims to carry owners and dates.

Section nine point two treats data structures hashing files as testable only when evidence and ticket IDs are recorded.

For section nine point two, Fernhill Library Network will not accept programming work without a written trail.

### 9.3 Files and paths

Programs read configuration and manifest files. Paths must be handled carefully so that a check reads the intended file.

Section nine point three develops programming ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nine point three, Marta Silva expects programming claims to carry owners and dates.

Section nine point three treats data structures hashing files as testable only when evidence and ticket IDs are recorded.

For section nine point three, Fernhill Library Network will not accept programming work without a written trail.

### 9.4 Errors

If a file is missing, the program should report it, not crash or skip silently. A missing file can itself be a finding.

Section nine point four develops programming ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nine point four, Marta Silva expects programming claims to carry owners and dates.

Section nine point four treats data structures hashing files as testable only when evidence and ticket IDs are recorded.

For section nine point four, Fernhill Library Network will not accept programming work without a written trail.

### 9.5 Modules

Splitting code into modules, such as one for reading data and one for checks, makes testing easier.

Section nine point five develops programming ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nine point five, Marta Silva expects programming claims to carry owners and dates.

Section nine point five treats data structures hashing files as testable only when evidence and ticket IDs are recorded.

For section nine point five, Fernhill Library Network will not accept programming work without a written trail.

### Building the manifest

The manifest lists each policy file in the golden image with its SHA-256 digest. It is generated when the image is released and stored with the release. A PC's files can then be compared with it at any time. Mateo stores manifests in version control so that each release has a matching manifest and differences between releases are easy to see.

He uses Python's hashlib module, part of the standard library.

### Readable output

The compare function prints the number of mismatches first, then each mismatched path.

### Testing the comparison

He tests three cases: identical files (no mismatches), one changed file (one mismatch) and one missing file (one missing report). Each case has an expected output written before the test runs.

### Worked example

Mateo writes a function that builds a digest manifest of the golden image's policy files and another that compares a PC's files with it. He tests by changing one synthetic file and confirming exactly one mismatch.

> **Synthetic case.** Synthetic.

### Errors and limits

Hashing detects change but does not say whether the change is harmful.

### Exercises

- **EX025 — Hash property.** What happens to a digest when a file changes? *Rubric:* 3 = it changes; 2 = partial; 1 = none; 0 = none.
- **EX026 — Missing files.** How should a missing file be handled? *Rubric:* 3 = report it; 2 = partial; 1 = none; 0 = none.
- **EX027 — Test.** How did Mateo test his compare function? *Rubric:* 3 = changed one file, expected one mismatch; 2 = partial; 1 = none; 0 = none.

### Synthesis

Hashing and careful error handling make change detection reliable.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply professional ethics to endpoint work; (2) protect patron privacy; (3) consider accessibility and harm.

### 10.1 Professional duties

Engineers owe care to the public. At Fernhill, the public are patrons, many of whom rely on library PCs for job applications and benefits.

Section ten point one develops engineering ethics and safety with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section ten point one, Marta Silva expects engineering claims to carry owners and dates.

Section ten point one treats professional duties privacy accessibility as testable only when evidence and ticket IDs are recorded.

For section ten point one, Fernhill Library Network will not accept engineering work without a written trail.

### 10.2 Privacy

The project aims to stop personal data being left behind. It must not create new privacy risks, such as logging what patrons browse. Logs record system events, not content.

Section ten point two develops engineering ethics and safety with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section ten point two, Marta Silva expects engineering claims to carry owners and dates.

Section ten point two treats professional duties privacy accessibility as testable only when evidence and ticket IDs are recorded.

### 10.3 Accessibility

Some patrons use screen readers and magnifiers. A strict design that blocks these tools would harm them. Requirements must include accessibility.

Section ten point three develops engineering ethics and safety with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section ten point three, Marta Silva expects engineering claims to carry owners and dates.

Section ten point three treats professional duties privacy accessibility as testable only when evidence and ticket IDs are recorded.

For section ten point three, Fernhill Library Network will not accept engineering work without a written trail.

### 10.4 Authorisation

Mateo works only on Fernhill systems with Marta's written agreement and tests on lab PCs, not in-use machines.

Section ten point four develops engineering ethics and safety with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section ten point four, Marta Silva expects engineering claims to carry owners and dates.

Section ten point four treats professional duties privacy accessibility as testable only when evidence and ticket IDs are recorded.

For section ten point four, Fernhill Library Network will not accept engineering work without a written trail.

### 10.5 Honesty

Reports state limitations and do not overclaim security.

Section ten point five develops engineering ethics and safety with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section ten point five, Marta Silva expects engineering claims to carry owners and dates.

Section ten point five treats professional duties privacy accessibility as testable only when evidence and ticket IDs are recorded.

For section ten point five, Fernhill Library Network will not accept engineering work without a written trail.

Section ten point five fails closed if engineering evidence is missing rather than guessing.

### Data minimisation

Mateo applies data minimisation: collect only what the design needs. Restore success, duration and installation attempts are enough to run and improve the service. Patron identities, browsing history and documents are never collected. When in doubt, he asks Fernhill's data protection officer.

He records these decisions in the project's ethics notes, reviewed each term by Dr Novak.

### Fair access

Public PCs often serve people without other internet access. A design that causes frequent outages or confusing restrictions harms them most, so reliability and clear notices are ethical as well as technical goals.

### Ethics review

Dr Novak reviews the project's ethics notes each term, checking privacy, accessibility and authorisation decisions.

### Authorisation in practice

Marta's written agreement lists what Mateo may do: configure lab PCs, read restore and event logs, and propose changes. Changes to branch PCs need Marta's approval.

### Worked example

During design, a colleague suggests recording screenshots to detect misuse. Mateo refuses on privacy grounds and proposes logging only installation attempts and restore results.

> **Synthetic case.** Synthetic.

### Errors and limits

Security designs can harm the people they protect if privacy and accessibility are ignored.

### Exercises

- **EX028 — Privacy boundary.** What may logs record? *Rubric:* 3 = system events, not content; 2 = partial; 1 = none; 0 = none.
- **EX029 — Accessibility.** Why include accessibility in requirements? *Rubric:* 3 = patrons use assistive tools; 2 = partial; 1 = none; 0 = none.
- **EX030 — Screenshot idea.** How did Mateo respond to the screenshot suggestion? *Rubric:* 3 = refused; log installs and restores only; 2 = partial; 1 = none; 0 = none.

### Synthesis

Ethics shapes what a secure design may and may not do.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) describe the networks public PCs use; (2) explain segmentation and common protocols; (3) identify network-related endpoint risks.

### 11.1 Branch networks

Each Fernhill branch has a switch connecting public PCs, staff laptops, printers and a router to the internet. Public PCs use DNS, HTTPS for browsing and a print protocol to reach the print server.

Section eleven point one develops networks and protocols with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eleven point one, Marta Silva expects networks claims to carry owners and dates.

Section eleven point one treats branch networks segmentation old as testable only when evidence and ticket IDs are recorded.

### 11.2 Segmentation

Placing public PCs on their own network segment, with firewall rules allowing only internet, printing and the management server, prevents them from reaching staff devices. This answers the design question from chapter 2.

Section eleven point two develops networks and protocols with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eleven point two, Marta Silva expects networks claims to carry owners and dates.

Section eleven point two treats branch networks segmentation old as testable only when evidence and ticket IDs are recorded.

### 11.3 Old protocols

SMB version 1, an old file-sharing protocol, has known weaknesses and should be disabled on all endpoints, as baselines from CIS and Microsoft recommend.

Section eleven point three develops networks and protocols with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eleven point three, Marta Silva expects networks claims to carry owners and dates.

Section eleven point three treats branch networks segmentation old as testable only when evidence and ticket IDs are recorded.

For section eleven point three, Fernhill Library Network will not accept networks work without a written trail.

### 11.4 Management traffic

The restore and update system needs a management connection from each PC to a central server. This traffic must be authenticated and encrypted.

Section eleven point four develops networks and protocols with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eleven point four, Marta Silva expects networks claims to carry owners and dates.

Section eleven point four treats branch networks segmentation old as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Fernhill Library Network will not accept networks work without a written trail.

### 11.5 Logging

Network devices can log connections, helping detect if a public PC tries to reach unexpected addresses.

Section eleven point five develops networks and protocols with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eleven point five, Marta Silva expects networks claims to carry owners and dates.

Section eleven point five treats branch networks segmentation old as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Fernhill Library Network will not accept networks work without a written trail.

### Name resolution and filtering

Fernhill uses a DNS filtering service that blocks known malicious domains for public PCs. This reduces risk from downloads but cannot block everything. The design therefore relies on endpoint controls too: application control blocks unapproved programs even if they are downloaded.

### Testing segmentation

After Eastgate's change, Mateo confirms with the network supplier's test report that public PCs can reach the internet, print server and management server, and cannot reach staff laptops. The report is stored as evidence for requirement verification later.

### Worked example

Mateo proposes a public PC segment at each branch. Marta checks with the network supplier, who confirms the switches support separate segments. At Eastgate, staff laptops are moved to their own segment within a week.

> **Synthetic case.** Synthetic.

### Errors and limits

Segmentation reduces exposure but does not protect a PC from threats arriving through allowed traffic, such as web downloads.

### Exercises

- **EX031 — Allowed traffic.** Which traffic should public PCs be allowed? *Rubric:* 3 = internet, printing, management; 2 = two; 1 = one; 0 = none.
- **EX032 — Management link.** What must protect management traffic? *Rubric:* 3 = authentication and encryption; 2 = partial; 1 = none; 0 = none.
- **EX033 — Segmentation limit.** What can segmentation not prevent? *Rubric:* 3 = threats through allowed traffic; 2 = partial; 1 = none; 0 = none.

### Synthesis

Segment public PCs and allow only needed traffic.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain processes, users, permissions and services; (2) describe how operating systems enforce separation; (3) identify settings that matter for public PCs.

### 12.1 Users and permissions

Operating systems run programs as users with permissions. A patron session should run as a standard user, not an administrator, so it cannot change system files or install system-wide software.

Section twelve point one develops operating systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twelve point one, Marta Silva expects operating claims to carry owners and dates.

Section twelve point one treats users and permissions services as testable only when evidence and ticket IDs are recorded.

### 12.2 Services

Background services run continuously. Unneeded services increase attack surface; NIST SP 800-123 recommends removing or disabling unnecessary services on servers, and the same principle applies to endpoints.

Section twelve point two develops operating systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twelve point two, Marta Silva expects operating claims to carry owners and dates.

Section twelve point two treats users and permissions services as testable only when evidence and ticket IDs are recorded.

For section twelve point two, Fernhill Library Network will not accept operating work without a written trail.

### 12.3 Kernel protection

The kernel enforces separation between processes. The Linux kernel self-protection project documents techniques that make the kernel harder to misuse; Windows has comparable features in its security baselines.

Section twelve point three develops operating systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twelve point three, Marta Silva expects operating claims to carry owners and dates.

Section twelve point three treats users and permissions services as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Fernhill Library Network will not accept operating work without a written trail.

### 12.4 Updates

Operating system updates fix vulnerabilities. Public PCs must receive them even though they reset nightly, so the golden image itself must be updated.

Section twelve point four develops operating systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twelve point four, Marta Silva expects operating claims to carry owners and dates.

Section twelve point four treats users and permissions services as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Fernhill Library Network will not accept operating work without a written trail.

### 12.5 Logs

The OS records events such as logons, installations and errors, which feed monitoring.

Section twelve point five develops operating systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twelve point five, Marta Silva expects operating claims to carry owners and dates.

Section twelve point five treats users and permissions services as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Fernhill Library Network will not accept operating work without a written trail.

### Least functionality

CIS Controls v8 and NIST SP 800-53 Rev. 5 both describe least functionality: configure systems to provide only essential capabilities. For public PCs that means a browser, office software, a PDF viewer, the catalogue, printing and accessibility tools, and nothing else. Every removed feature is one less thing to patch and monitor.

Mateo lists every installed program on the current image and marks each as needed or not, with librarians' input.

### Image contents list

The golden image's contents list records every installed program, service and setting group with its reason. When someone asks why a component exists, the list answers; when a component has no reason, it is removed.

### Worked example

Mateo lists services on a sample public PC and finds a remote desktop service enabled. Nobody uses it, so it is disabled in the image.

> **Synthetic case.** Synthetic.

### Errors and limits

Disabling services without checking dependencies can break features; test each change.

### Exercises

- **EX034 — Patron account.** Why should patrons run as standard users? *Rubric:* 3 = cannot change system or install system-wide; 2 = partial; 1 = none; 0 = none.
- **EX035 — Services.** What does SP 800-123 recommend about services? *Rubric:* 3 = disable unnecessary ones; 2 = partial; 1 = none; 0 = none.
- **EX036 — Image updates.** Why must the golden image be updated? *Rubric:* 3 = PCs reset to it nightly; 2 = partial; 1 = none; 0 = none.

### Synthesis

Standard users, minimal services and an updated image form the OS foundation.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) design records for inventory, restore results and events; (2) choose keys and fields; (3) protect privacy in data.

### 13.1 Records needed

The project needs an inventory of PCs (asset tag, branch, model, firmware version), nightly restore results (PC, date, success, duration) and security events (PC, time, event type).

Section thirteen point one develops data systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirteen point one, Marta Silva expects data claims to carry owners and dates.

Section thirteen point one treats records needed keys privacy as testable only when evidence and ticket IDs are recorded.

For section thirteen point one, Fernhill Library Network will not accept data work without a written trail.

### 13.2 Keys

Asset tags uniquely identify PCs even when hostnames change, so they are used as keys.

Section thirteen point two develops data systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirteen point two, Marta Silva expects data claims to carry owners and dates.

Section thirteen point two treats records needed keys privacy as testable only when evidence and ticket IDs are recorded.

For section thirteen point two, Fernhill Library Network will not accept data work without a written trail.

### 13.3 Privacy

Records never store patron names or browsing. Session records count logons, not identities.

Section thirteen point three develops data systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirteen point three, Marta Silva expects data claims to carry owners and dates.

Section thirteen point three treats records needed keys privacy as testable only when evidence and ticket IDs are recorded.

For section thirteen point three, Fernhill Library Network will not accept data work without a written trail.

### 13.4 Retention

Restore and event records are kept for one year, enough to analyse trends; older records are deleted.

Section thirteen point four develops data systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirteen point four, Marta Silva expects data claims to carry owners and dates.

Section thirteen point four treats records needed keys privacy as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Fernhill Library Network will not accept data work without a written trail.

### 13.5 Queries

Typical questions: which PCs failed restore last night, which branch has the slowest restores, which firmware versions are in use.

Section thirteen point five develops data systems with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirteen point five, Marta Silva expects data claims to carry owners and dates.

Section thirteen point five treats records needed keys privacy as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Fernhill Library Network will not accept data work without a written trail.

### Testing queries

Mateo writes the three typical queries before building the tables, then checks that each can be answered. One cannot: which branch has the slowest restores needs branch in the restore results or a join with inventory. He adds the join and confirms it works.

He also checks that records can be deleted cleanly after one year, so retention is enforced automatically rather than relying on someone remembering.

### Access to data

Only IT staff can read event records; librarians see summaries on the dashboard.

### Data for the dashboard

The same tables later feed the librarians' dashboard in chapter 35, showing PCs ready, PCs out of service and recent restore results per branch.

### Data quality

Records are checked weekly for missing or duplicated asset tags, which would distort reports.

### Naming

Field names are short and documented.

### Worked example

Mateo designs a simple table structure and tests it with a month of synthetic records. A query for PCs with old firmware finds 12 at Millbrook, which becomes an update task.

> **Synthetic case.** Synthetic.

### Errors and limits

Data designed without questions in mind often cannot answer them later.

### Exercises

- **EX037 — Inventory fields.** What fields does the inventory hold? *Rubric:* 3 = asset tag, branch, model, firmware; 2 = three; 1 = two; 0 = none.
- **EX038 — Key choice.** Why use asset tags as keys? *Rubric:* 3 = unique even when hostnames change; 2 = partial; 1 = none; 0 = none.
- **EX039 — Retention.** How long are records kept? *Rubric:* 3 = one year; 2 = partial; 1 = none; 0 = none.

### Synthesis

Design data around the questions it must answer, without personal data.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) manage code with version control and reviews; (2) write requirements and tests; (3) plan releases of images.

### 14.1 Version control

All scripts, image definitions and configuration files live in a version-controlled repository, so every change is recorded with author and reason.

Section fourteen point one develops software engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fourteen point one, Marta Silva expects software claims to carry owners and dates.

Section fourteen point one treats version control reviews requirements as testable only when evidence and ticket IDs are recorded.

For section fourteen point one, Fernhill Library Network will not accept software work without a written trail.

### 14.2 Reviews

Changes are reviewed by another person before use, catching mistakes early.

Section fourteen point two develops software engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fourteen point two, Marta Silva expects software claims to carry owners and dates.

Section fourteen point two treats version control reviews requirements as testable only when evidence and ticket IDs are recorded.

For section fourteen point two, Fernhill Library Network will not accept software work without a written trail.

Section fourteen point two fails closed if software evidence is missing rather than guessing.

### 14.3 Requirements

Requirements are numbered and testable, such as "R3: USB storage devices are blocked on public PCs".

Section fourteen point three develops software engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fourteen point three, Marta Silva expects software claims to carry owners and dates.

Section fourteen point three treats version control reviews requirements as testable only when evidence and ticket IDs are recorded.

For section fourteen point three, Fernhill Library Network will not accept software work without a written trail.

### 14.4 Tests

Each requirement has a test, run on a lab PC before an image is released.

Section fourteen point four develops software engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fourteen point four, Marta Silva expects software claims to carry owners and dates.

Section fourteen point four treats version control reviews requirements as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Fernhill Library Network will not accept software work without a written trail.

### 14.5 Releases

New golden images are released in stages: lab PC, one branch, then all branches, so problems affect few PCs first.

Section fourteen point five develops software engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fourteen point five, Marta Silva expects software claims to carry owners and dates.

Section fourteen point five treats version control reviews requirements as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Fernhill Library Network will not accept software work without a written trail.

### Change history in practice

When the catalogue app broke last year, nobody could say what had changed. With version control, every image change has a record. If a new image causes problems, the team can compare it with the previous release line by line and roll back quickly. Mateo demonstrates this on a lab PC to convince Marta, who had worried that the repository would be extra work.

The repository also stores the test results for each release.

### Code review checklist

Reviews use a short checklist: does the change match a requirement, has it been tested, and does it change anything outside the public PC image?

### Testing images

Each image release runs the requirement tests on a lab PC. A release cannot move to branches until all must-have tests pass. This rule is enforced by the release checklist.

### Worked example

Marta asks why not update all PCs at once. Mateo explains that staged releases limit the impact of a bad image, citing Fernhill's past experience of an update breaking the catalogue app on every PC.

> **Synthetic case.** Synthetic.

### Errors and limits

Without tests tied to requirements, reviews check style rather than function.

### Exercises

- **EX040 — Version control.** What does version control record? *Rubric:* 3 = every change with author and reason; 2 = partial; 1 = none; 0 = none.
- **EX041 — Testable requirement.** Give an example of a testable requirement. *Rubric:* 3 = R3 USB storage blocked; 2 = partial; 1 = none; 0 = none.
- **EX042 — Staged release.** Why release images in stages? *Rubric:* 3 = limit bad image impact; 2 = partial; 1 = none; 0 = none.

### Synthesis

Engineering discipline applies to images and scripts as much as to applications.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to public PCs; (2) describe threats and vulnerabilities; (3) use security principles.

### 15.1 Goals

Confidentiality: patrons' data must not be left for others. Integrity: PCs must run only approved software and settings. Availability: PCs must be ready when the library opens.

Section fifteen point one develops security fundamentals with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifteen point one, Marta Silva expects security claims to carry owners and dates.

Section fifteen point one treats goals threats principles controls as testable only when evidence and ticket IDs are recorded.

For section fifteen point one, Fernhill Library Network will not accept security work without a written trail.

### 15.2 Threats

Threats include careless users, curious users, malicious software from websites or USB devices and equipment failures.

Section fifteen point two develops security fundamentals with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifteen point two, Marta Silva expects security claims to carry owners and dates.

Section fifteen point two treats goals threats principles controls as testable only when evidence and ticket IDs are recorded.

For section fifteen point two, Fernhill Library Network will not accept security work without a written trail.

### 15.3 Principles

Saltzer and Schroeder (1975) set out design principles including least privilege, fail-safe defaults and economy of mechanism. A public PC that resets to a minimal, locked image applies all three.

Section fifteen point three develops security fundamentals with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifteen point three, Marta Silva expects security claims to carry owners and dates.

Section fifteen point three treats goals threats principles controls as testable only when evidence and ticket IDs are recorded.

For section fifteen point three, Fernhill Library Network will not accept security work without a written trail.

### 15.4 Controls

CIS Controls v8 groups safeguards such as inventory, secure configuration and data recovery, each relevant to the project.

Section fifteen point four develops security fundamentals with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifteen point four, Marta Silva expects security claims to carry owners and dates.

Section fifteen point four treats goals threats principles controls as testable only when evidence and ticket IDs are recorded.

For section fifteen point four, Fernhill Library Network will not accept security work without a written trail.

### 15.5 Risk

Risk combines likelihood and impact; chapter 23 ranks scenarios.

Section fifteen point five develops security fundamentals with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifteen point five, Marta Silva expects security claims to carry owners and dates.

Section fifteen point five treats goals threats principles controls as testable only when evidence and ticket IDs are recorded.

For section fifteen point five, Fernhill Library Network will not accept security work without a written trail.

Section fifteen point five fails closed if security evidence is missing rather than guessing.

### Threats in plain words

Mateo explains threats to librarians without technical detail: some patrons try to install games or toolbars; some websites offer harmful downloads; USB sticks can carry malicious files; and equipment sometimes fails. Each threat links to a control in the design. This helps librarians understand why some restrictions exist and makes them allies rather than critics.

He avoids describing how attacks work and focuses on what the controls do.

### Measuring security

Each goal has a measure: leftover files found, unapproved programs blocked and PCs ready at opening.

### Linking goals to requirements

Each goal is later linked to requirements in chapter 21, so every requirement can be traced back to a security goal and forward to evidence.

### Residual risk

No design removes all risk. A patron could still photograph a screen or misuse a website; these are outside what PC controls can address.

### Worked example

Mateo maps each Saltzer and Schroeder principle to a design feature: least privilege (standard users), fail-safe defaults (USB storage blocked by default), economy of mechanism (one image for all public PCs).

> **Synthetic case.** Synthetic.

### Errors and limits

Principles guide design but do not replace testing.

### Exercises

- **EX043 — Three goals.** Apply the three goals to public PCs. *Rubric:* 3 = data not left, approved software only, ready at opening; 2 = two; 1 = one; 0 = none.
- **EX044 — Principles.** Map three principles to features. *Rubric:* 3 = least privilege, fail-safe, economy; 2 = two; 1 = one; 0 = none.
- **EX045 — CIS Controls.** Name three relevant CIS Controls areas. *Rubric:* 3 = inventory, secure configuration, data recovery; 2 = two; 1 = one; 0 = none.

### Synthesis

Classic principles map directly onto a hardened public PC design.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) define system boundaries and interfaces; (2) manage requirements through the life cycle; (3) plan verification.

### 16.1 System boundary

The system includes public PCs, the golden image, the management server, the restore mechanism and monitoring. Patron personal devices and the internet are outside.

Section sixteen point one develops systems engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section sixteen point one, Marta Silva expects systems claims to carry owners and dates.

Section sixteen point one treats system boundary interfaces life as testable only when evidence and ticket IDs are recorded.

For section sixteen point one, Fernhill Library Network will not accept systems work without a written trail.

### 16.2 Interfaces

Interfaces include the PC-to-server management channel, the print service and the network segment rules.

Section sixteen point two develops systems engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section sixteen point two, Marta Silva expects systems claims to carry owners and dates.

Section sixteen point two treats system boundary interfaces life as testable only when evidence and ticket IDs are recorded.

For section sixteen point two, Fernhill Library Network will not accept systems work without a written trail.

### 16.3 Life cycle

Requirements are defined, designed, implemented, verified, operated and retired. Each stage has outputs.

Section sixteen point three develops systems engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section sixteen point three, Marta Silva expects systems claims to carry owners and dates.

Section sixteen point three treats system boundary interfaces life as testable only when evidence and ticket IDs are recorded.

For section sixteen point three, Fernhill Library Network will not accept systems work without a written trail.

### 16.4 Configuration management

NIST SP 800-128 describes security-focused configuration management: baselines, change control and monitoring. The golden image is the baseline.

Section sixteen point four develops systems engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section sixteen point four, Marta Silva expects systems claims to carry owners and dates.

Section sixteen point four treats system boundary interfaces life as testable only when evidence and ticket IDs are recorded.

For section sixteen point four, Fernhill Library Network will not accept systems work without a written trail.

### 16.5 Verification planning

Each requirement gets a verification method: test, inspection or analysis.

Section sixteen point five develops systems engineering with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section sixteen point five, Marta Silva expects systems claims to carry owners and dates.

Section sixteen point five treats system boundary interfaces life as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Fernhill Library Network will not accept systems work without a written trail.

Section sixteen point five fails closed if systems evidence is missing rather than guessing.

### Ownership of components

Each component in the system boundary has an owner: Marta owns the image, the technician owns daily restore checks, the network supplier owns segmentation and the session system vendor owns booking. Owners approve changes affecting their components. Mateo records owners in the context diagram so that gaps are visible.

The diagram is reviewed whenever a component or interface changes.

### Interfaces as risk points

Most integration problems appear at interfaces, so each interface has a test in the verification plan.

### Life cycle outputs

Each life cycle stage produces outputs: requirement list, design records, implementation repository, verification evidence, operations runbooks and, eventually, a retirement plan for old hardware. Mateo lists these outputs at the start so nothing is forgotten. Retirement matters too: old PCs must have disks wiped before disposal, following the same care as the restore design.

### Configuration items

Each image release, script and policy file is a configuration item with a version and owner, following SP 800-128.

### Worked example

Mateo draws a context diagram with the system boundary and five interfaces, then a table linking each requirement to a verification method.

> **Synthetic case.** Synthetic.

### Errors and limits

Unclear boundaries lead to gaps where nobody owns a component.

### Exercises

- **EX046 — Boundary.** What lies outside the system boundary? *Rubric:* 3 = patron devices, internet; 2 = partial; 1 = none; 0 = none.
- **EX047 — Baseline.** What serves as the configuration baseline? *Rubric:* 3 = golden image; 2 = partial; 1 = none; 0 = none.
- **EX048 — Verification methods.** Name three verification methods. *Rubric:* 3 = test, inspection, analysis; 2 = two; 1 = one; 0 = none.

### Synthesis

Systems engineering keeps boundaries, interfaces and verification explicit.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) describe feedback loops; (2) apply them to configuration and restore; (3) avoid unstable responses.

### 17.1 Feedback

A feedback loop measures a system's state, compares it with a target and acts to reduce the difference. A thermostat is the classic example.

Section seventeen point one develops control and feedback basics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seventeen point one, Marta Silva expects control claims to carry owners and dates.

Section seventeen point one treats feedback configuration as control as testable only when evidence and ticket IDs are recorded.

For section seventeen point one, Fernhill Library Network will not accept control work without a written trail.

### 17.2 Configuration as control

The nightly restore is a feedback loop: measure (compare with the golden image), compare (detect differences) and act (restore).

Section seventeen point two develops control and feedback basics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seventeen point two, Marta Silva expects control claims to carry owners and dates.

Section seventeen point two treats feedback configuration as control as testable only when evidence and ticket IDs are recorded.

For section seventeen point two, Fernhill Library Network will not accept control work without a written trail.

### 17.3 Delay

Loops with long delays let problems grow before correction. Fortnightly manual clean-ups had a 14-day delay; nightly restore has one day.

Section seventeen point three develops control and feedback basics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seventeen point three, Marta Silva expects control claims to carry owners and dates.

Section seventeen point three treats feedback configuration as control as testable only when evidence and ticket IDs are recorded.

For section seventeen point three, Fernhill Library Network will not accept control work without a written trail.

### 17.4 Over-correction

Aggressive loops can cause disruption, such as restoring during a patron's session. The restore runs after closing time to avoid this.

Section seventeen point four develops control and feedback basics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seventeen point four, Marta Silva expects control claims to carry owners and dates.

Section seventeen point four treats feedback configuration as control as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Fernhill Library Network will not accept control work without a written trail.

### 17.5 Monitoring the loop

The loop itself must be monitored: if restores fail silently, the system drifts.

Section seventeen point five develops control and feedback basics with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section seventeen point five, Marta Silva expects control claims to carry owners and dates.

Section seventeen point five treats feedback configuration as control as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Fernhill Library Network will not accept control work without a written trail.

### Stability

A control loop should correct problems without causing new ones. If the restore loop ran too often, it might interrupt patrons; if too rarely, problems accumulate. Nightly after closing balances both. Mateo also adds a guard: if more than five PCs fail restore, the system stops releasing new images until IT investigates, preventing a bad update from repeatedly breaking PCs.

This guard links the probability work in chapter 7 to operations.

### Measuring loop health

The loop's health is measured by restore success rate and time to repair failures.

### Feedback beyond restore

Patching, allowlist reviews and baseline updates are also feedback loops with different delays: monthly, weekly and yearly.

### Delays elsewhere

A month-long patch cycle is a slower loop, acceptable because updates are tested before release.

### Worked example

Mateo sketches the loop and adds a second loop: if restore fails, alert staff, who repair the PC before opening. This nested loop handles failures of the first.

> **Synthetic case.** Synthetic.

### Errors and limits

A control loop that is not monitored can fail without anyone noticing.

### Exercises

- **EX049 — Loop steps.** Name the three steps of the restore loop. *Rubric:* 3 = measure, compare, act; 2 = two; 1 = one; 0 = none.
- **EX050 — Delay effect.** How does delay affect a loop? *Rubric:* 3 = problems grow before correction; 2 = partial; 1 = none; 0 = none.
- **EX051 — Nested loop.** What does the second loop do? *Rubric:* 3 = alert on failed restore, repair before opening; 2 = partial; 1 = none; 0 = none.

### Synthesis

Treat restore as a monitored feedback loop.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) design layered controls for public PCs; (2) place controls at firmware, OS, application and network layers; (3) explain defence in depth.

### 18.1 Layers

Firmware: Secure Boot and firmware password. OS: standard users, minimal services, disk encryption. Application: allowlist. Data: nightly restore of patron area. Network: segmentation. Monitoring: event logs and restore alerts.

Section eighteen point one develops security architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eighteen point one, Marta Silva expects security claims to carry owners and dates.

Section eighteen point one treats layers defence in depth as testable only when evidence and ticket IDs are recorded.

For section eighteen point one, Fernhill Library Network will not accept security work without a written trail.

### 18.2 Defence in depth

If one layer fails, others still protect. If the allowlist misses a program, the nightly restore removes it.

Section eighteen point two develops security architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eighteen point two, Marta Silva expects security claims to carry owners and dates.

Section eighteen point two treats layers defence in depth as testable only when evidence and ticket IDs are recorded.

For section eighteen point two, Fernhill Library Network will not accept security work without a written trail.

### 18.3 Firmware resilience

NIST SP 800-193 sets principles for protecting, detecting and recovering firmware; SP 800-147 gives BIOS protection guidelines for update authentication.

Section eighteen point three develops security architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eighteen point three, Marta Silva expects security claims to carry owners and dates.

Section eighteen point three treats layers defence in depth as testable only when evidence and ticket IDs are recorded.

For section eighteen point three, Fernhill Library Network will not accept security work without a written trail.

### 18.4 Application control

Microsoft documents application control for Windows, allowing only approved software to run.

Section eighteen point four develops security architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eighteen point four, Marta Silva expects security claims to carry owners and dates.

Section eighteen point four treats layers defence in depth as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Fernhill Library Network will not accept security work without a written trail.

Section eighteen point four fails closed if security evidence is missing rather than guessing.

### 18.5 Trade-offs

More layers add complexity and maintenance. The design keeps each layer simple.

Section eighteen point five develops security architecture with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section eighteen point five, Marta Silva expects security claims to carry owners and dates.

Section eighteen point five treats layers defence in depth as testable only when evidence and ticket IDs are recorded.

For section eighteen point five, Fernhill Library Network will not accept security work without a written trail.

Section eighteen point five fails closed if security evidence is missing rather than guessing.

### Mapping to standards

Mateo maps each layer to recognised guidance. Firmware controls map to NIST SP 800-147 and SP 800-193. OS hardening maps to the CIS Benchmarks, Microsoft security baselines and NIST SP 800-123's principles. Application control maps to CIS Controls v8 safeguards on allowlisting authorised software. Data recovery maps to CIS Controls v8 data recovery safeguards. Monitoring maps to NIST SP 800-92 on log management.

This mapping helps Fernhill's auditors and shows that the design is not invented from scratch.

### Single points of failure

The restore server and signing keys are single points of failure; later chapters add local copies and key protection.

### Dependencies between layers

If firmware were changed, the boot chain could load an altered system, and restore might not run correctly. This is why firmware and boot protections are must-haves.

### Worked example

Dr Novak asks which layer matters most. Mateo answers that the nightly restore is the backbone, because it corrects many failures of other layers, but it depends on firmware and boot protection to ensure the restore itself is trustworthy.

> **Synthetic case.** Synthetic.

### Errors and limits

Layers that depend on each other can fail together; identify dependencies.

### Exercises

- **EX052 — Layer list.** List the layers and one control each. *Rubric:* 3 = firmware, OS, app, data, network, monitoring; 2 = five; 1 = three; 0 = none.
- **EX053 — Firmware guidance.** Which NIST publications cover firmware? *Rubric:* 3 = SP 800-193, SP 800-147; 2 = partial; 1 = none; 0 = none.
- **EX054 — Backbone.** Why is restore the backbone? *Rubric:* 3 = corrects other layer failures; 2 = partial; 1 = none; 0 = none.

### Synthesis

Layered controls protect even when one layer fails.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) explain authentication for patrons and staff; (2) describe encryption at rest and in transit; (3) use digital signatures for integrity.

### 19.1 Patron sessions

Patrons log in with library card numbers via a session manager; the PC itself runs a standard local account.

Section nineteen point one develops identity and cryptography with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nineteen point one, Marta Silva expects identity claims to carry owners and dates.

Section nineteen point one treats patron sessions staff access as testable only when evidence and ticket IDs are recorded.

For section nineteen point one, Fernhill Library Network will not accept identity work without a written trail.

### 19.2 Staff access

Staff administration uses separate named accounts with multi-factor authentication.

Section nineteen point two develops identity and cryptography with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nineteen point two, Marta Silva expects identity claims to carry owners and dates.

Section nineteen point two treats patron sessions staff access as testable only when evidence and ticket IDs are recorded.

For section nineteen point two, Fernhill Library Network will not accept identity work without a written trail.

Section nineteen point two fails closed if identity evidence is missing rather than guessing.

### 19.3 Encryption at rest

Disk encryption, supported by the TPM, protects data if a PC or disk is stolen. Microsoft documents BitLocker for Windows.

Section nineteen point three develops identity and cryptography with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nineteen point three, Marta Silva expects identity claims to carry owners and dates.

Section nineteen point three treats patron sessions staff access as testable only when evidence and ticket IDs are recorded.

For section nineteen point three, Fernhill Library Network will not accept identity work without a written trail.

### 19.4 Encryption in transit

Management traffic uses TLS with certificates so PCs talk only to the genuine server.

Section nineteen point four develops identity and cryptography with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nineteen point four, Marta Silva expects identity claims to carry owners and dates.

Section nineteen point four treats patron sessions staff access as testable only when evidence and ticket IDs are recorded.

For section nineteen point four, Fernhill Library Network will not accept identity work without a written trail.

### 19.5 Signatures

Golden images and updates are signed; PCs verify signatures before applying them, as SP 800-147 recommends for firmware updates.

Section nineteen point five develops identity and cryptography with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section nineteen point five, Marta Silva expects identity claims to carry owners and dates.

Section nineteen point five treats patron sessions staff access as testable only when evidence and ticket IDs are recorded.

For section nineteen point five, Fernhill Library Network will not accept identity work without a written trail.

### Key management

Signing keys for images must be protected, because anyone holding them could sign a harmful image that PCs would accept. Initially the key sits on Marta's workstation. Mateo records this as a risk; chapter 45's independent review later moves the key to a managed hardware service. Disk encryption recovery keys are stored in Fernhill's directory service, accessible only to IT staff.

He documents who can use each key and how its use is logged.

### Certificates

Server certificates are renewed automatically, with an alert thirty days before expiry.

### Accounts for staff

Staff use separate administrative accounts only for IT tasks and normal accounts for email and browsing, reducing the impact if a normal account is compromised. Administrative logons are logged and reviewed weekly.

### Patron credentials

Library card numbers are checked by the session system, not stored on PCs.

### Logging

Signature failures are logged.

### Worked example

Mateo tests what happens if an unsigned image is offered to a lab PC. It refuses to apply it and logs an error, which is the desired behaviour.

> **Synthetic case.** Synthetic.

### Errors and limits

Encryption without good key management protects little.

### Exercises

- **EX055 — Staff accounts.** How do staff authenticate? *Rubric:* 3 = named accounts with MFA; 2 = partial; 1 = none; 0 = none.
- **EX056 — Disk encryption.** What does disk encryption protect against? *Rubric:* 3 = stolen PC or disk; 2 = partial; 1 = none; 0 = none.
- **EX057 — Unsigned image.** What happened when an unsigned image was offered? *Rubric:* 3 = refused and logged; 2 = partial; 1 = none; 0 = none.

### Synthesis

Authenticate people and verify software with cryptography.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Systems, endpoints and hardware security: engineering context

### Learning outcomes

You will (1) describe the public PC service as an engineering problem; (2) identify stakeholders and constraints; (3) set project objectives.

### 20.1 Context

Fernhill's 300 public PCs serve about 2,000 sessions a day. Staff are librarians, not IT specialists. The IT team is Marta and one technician. Budget is limited.

Section twenty point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty point one treats context stakeholders constraints objectives as testable only when evidence and ticket IDs are recorded.

For section twenty point one, Fernhill Library Network will not accept systems work without a written trail.

### 20.2 Stakeholders

Patrons want working, private PCs. Librarians want fewer problems to handle. Marta wants less manual work. The board wants cost control and no data incidents.

Section twenty point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty point two treats context stakeholders constraints objectives as testable only when evidence and ticket IDs are recorded.

For section twenty point two, Fernhill Library Network will not accept systems work without a written trail.

### 20.3 Constraints

Existing hardware must be reused; changes must not disrupt opening hours; accessibility tools must work.

Section twenty point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty point three treats context stakeholders constraints objectives as testable only when evidence and ticket IDs are recorded.

For section twenty point three, Fernhill Library Network will not accept systems work without a written trail.

### 20.4 Objectives

O1: no patron data persists beyond one day. O2: only approved software runs. O3: PCs are ready at opening. O4: manual effort falls.

Section twenty point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty point four treats context stakeholders constraints objectives as testable only when evidence and ticket IDs are recorded.

For section twenty point four, Fernhill Library Network will not accept systems work without a written trail.

### 20.5 Standards context

The design draws on CIS Benchmarks, Microsoft security baselines, NIST SP 800-123 and SP 800-40r4.

Section twenty point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty point five, Marta Silva expects systems claims to carry owners and dates.

Section twenty point five treats context stakeholders constraints objectives as testable only when evidence and ticket IDs are recorded.

For section twenty point five, Fernhill Library Network will not accept systems work without a written trail.

### Success measures

Each objective gets a measure: O1, leftover files found in spot checks; O2, unapproved programs executed; O3, PCs out of service at opening; O4, staff hours spent on PC problems per month. Baselines are collected for a month before changes, so improvement can be shown later.

The baseline month shows 42 PC failures needing manual repair, 31 leftover-file reports and about 60 staff hours on PC issues.

### Project risks

Main risks are staff time, hardware age and patron acceptance of restrictions.

### Constraints shaping design

Reusing existing hardware rules out designs needing new devices this year, which later shapes the choice in chapter 26. Accessibility constraints shape the allowlist approach in chapter 31. Recording constraints early prevents designs that cannot be used.

### Baseline evidence

The baseline month's figures are stored with collection dates for later comparison in chapters 32 and 42.

### Worked example

Marta asks whether O4 conflicts with security. Mateo shows that automation of restore and updates serves both: less manual work and more consistent security.

> **Synthetic case.** Synthetic.

### Errors and limits

Objectives that are not measurable cannot be verified.

### Exercises

- **EX058 — Constraints.** List the three constraints. *Rubric:* 3 = reuse hardware, no disruption, accessibility; 2 = two; 1 = one; 0 = none.
- **EX059 — Objectives.** State the four objectives. *Rubric:* 3 = no data beyond a day, approved software, ready at opening, less manual effort; 2 = three; 1 = two; 0 = none.
- **EX060 — O4 reconciliation.** How does automation serve both security and effort? *Rubric:* 3 = consistent and less manual; 2 = partial; 1 = none; 0 = none.

### Synthesis

Clear objectives frame the engineering work.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Systems, endpoints and hardware security: requirements

### Learning outcomes

You will (1) write security requirements from objectives; (2) make them testable; (3) prioritise them.

### 21.1 From objectives to requirements

Each objective yields requirements. O1 yields R4 nightly restore of the patron area and R8 staff disk encryption. O2 yields R5 application control in enforce mode and R3 USB storage blocked.

Section twenty-one point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-one point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-one point one treats from objectives to requirements as testable only when evidence and ticket IDs are recorded.

### 21.2 Boot integrity

R1 Secure Boot enabled and R2 firmware password set protect the restore mechanism itself.

Section twenty-one point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-one point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-one point two treats from objectives to requirements as testable only when evidence and ticket IDs are recorded.

For section twenty-one point two, Fernhill Library Network will not accept systems work without a written trail.

### 21.3 Operations

R6 automatic logoff after 15 minutes idle; R7 remote logging of security events; R9 alert on restore failure.

Section twenty-one point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-one point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-one point three treats from objectives to requirements as testable only when evidence and ticket IDs are recorded.

For section twenty-one point three, Fernhill Library Network will not accept systems work without a written trail.

### 21.4 Accessibility

R10 approved accessibility tools available on every PC.

Section twenty-one point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-one point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-one point four treats from objectives to requirements as testable only when evidence and ticket IDs are recorded.

For section twenty-one point four, Fernhill Library Network will not accept systems work without a written trail.

Section twenty-one point four fails closed if systems evidence is missing rather than guessing.

### 21.5 Priorities

R1, R4 and R5 are must-haves; R9 and R10 are must-haves for safe operation and fairness.

Section twenty-one point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-one point five, Marta Silva expects systems claims to carry owners and dates.

Section twenty-one point five treats from objectives to requirements as testable only when evidence and ticket IDs are recorded.

For section twenty-one point five, Fernhill Library Network will not accept systems work without a written trail.

### Requirement attributes

Each requirement has an identifier, statement, source objective, priority, verification method and owner. For example, R4: the patron area is restored to the golden state every night; source O1; must-have; verified by test; owner Marta. Recording attributes makes later traceability simple and lets anyone see why a requirement exists.

Requirements are reviewed with stakeholders before design starts, and any change later needs a recorded reason.

### Avoiding solution bias

Mateo phrases requirements as outcomes, not products, so different solutions can be compared in chapter 26.

### Reviewing requirements

Requirements are reviewed again after the studio in chapter 25, when patron guidance about saving work is added as a new requirement linked to O1 and O3.

### Traceability start

A traceability table links each requirement to its objective now, and later to design, tests and evidence. Starting it early is much easier than building it at the end.

### Worked example

Mateo reviews the ten requirements with Marta and a librarian. The librarian adds that the accessibility reader must be available without staff help, refining R10.

> **Synthetic case.** Synthetic.

### Errors and limits

Requirements written only by engineers often miss user needs.

### Exercises

- **EX061 — Boot requirements.** Which requirements protect boot? *Rubric:* 3 = R1 Secure Boot, R2 firmware password; 2 = partial; 1 = none; 0 = none.
- **EX062 — O2 requirements.** Which requirements implement O2? *Rubric:* 3 = R5 app control, R3 USB block; 2 = partial; 1 = none; 0 = none.
- **EX063 — R10 refinement.** How was R10 refined? *Rubric:* 3 = reader available without staff help; 2 = partial; 1 = none; 0 = none.

### Synthesis

Testable requirements trace back to objectives and users.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Systems, endpoints and hardware security: system and data models

### Learning outcomes

You will (1) model the boot chain and measured components; (2) compare observed measurements to a manifest; (3) interpret mismatches.

### 22.1 Boot chain model

Firmware verifies the bootloader, which verifies the kernel; the kernel loads an initial file system and then applies the kiosk policy. Each component can be measured by its digest.

Section twenty-two point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-two point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-two point one treats boot chain model manifest as testable only when evidence and ticket IDs are recorded.

### 22.2 Manifest

The golden image release includes a manifest of expected digests for each component.

Section twenty-two point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-two point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-two point two treats boot chain model manifest as testable only when evidence and ticket IDs are recorded.

For section twenty-two point two, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — boot measurements

```python
"""Compare synthetic boot-component digests with an expected manifest (stdlib only)."""
import hashlib
expected = {c: hashlib.sha256(f"{c}-v2.1".encode()).hexdigest() for c in ("firmware", "bootloader", "kernel", "initrd", "kiosk-policy")}
observed = dict(expected)
observed["kiosk-policy"] = hashlib.sha256(b"kiosk-policy-v2.0").hexdigest()
for c in expected:
    print(f"{c:13} {'match' if observed[c] == expected[c] else 'MISMATCH'}  {observed[c][:12]}")
print(f"{sum(observed[c] != expected[c] for c in expected)} of {len(expected)} components differ")
```

Run with `python3 lab_boot.py`. Verified output:

```text
firmware      match  a46bac657b78
bootloader    match  7e5ecd63dec1
kernel        match  eafae6b3a1ca
initrd        match  0a6473933bba
kiosk-policy  MISMATCH  9ad757800d10
1 of 5 components differ
```

### 22.3 Reading the result

Four components match the manifest; the kiosk policy does not. One of five components differs.

Section twenty-two point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-two point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-two point three treats boot chain model manifest as testable only when evidence and ticket IDs are recorded.

For section twenty-two point three, Fernhill Library Network will not accept systems work without a written trail.

### 22.4 Interpreting

The mismatch shows the PC is running policy version 2.0, not 2.1. Investigation finds the PC was offline during the update. The fix is to reapply the release, not to treat the PC as compromised.

Section twenty-two point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-two point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-two point four treats boot chain model manifest as testable only when evidence and ticket IDs are recorded.

### 22.5 Data model

Measurement results are stored with PC, date, component and status.

Section twenty-two point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-two point five, Marta Silva expects systems claims to carry owners and dates.

Section twenty-two point five treats boot chain model manifest as testable only when evidence and ticket IDs are recorded.

For section twenty-two point five, Fernhill Library Network will not accept systems work without a written trail.

### Measured boot and attestation

With a TPM, each boot component's measurement can be recorded in secure registers. A management server can request these measurements and compare them with expected values, a process called attestation. Fernhill's design uses a simpler version: a startup script computes digests of key files and reports them. The lab shows the comparison logic.

Mateo notes that the simple version relies on the OS being trustworthy enough to report honestly, which Secure Boot supports.

### Response rule

Mismatch after one restore triggers a reapply; mismatch after two triggers investigation.

### Storing results

Measurement results are kept for a year and summarised weekly, showing how often mismatches occur and how quickly they are fixed.

### Worked example

Marta asks whether a mismatch means an attack. Mateo explains that most mismatches are update failures; the response is to restore and recheck, escalating only if a mismatch persists after restore.

> **Synthetic case.** Synthetic digests.

### Errors and limits

Measurements show difference, not cause.

### Exercises

- **EX064 — Chain order.** Describe the boot chain verification order. *Rubric:* 3 = firmware→bootloader→kernel→initrd→policy; 2 = partial; 1 = none; 0 = none.
- **EX065 — Lab result.** What did the measurement show? *Rubric:* 3 = 1 of 5 differ: kiosk-policy; 2 = partial; 1 = none; 0 = none.
- **EX066 — Mismatch cause.** What caused the mismatch? *Rubric:* 3 = PC offline during update; 2 = partial; 1 = none; 0 = none.

### Synthesis

Model the boot chain and compare measurements to a manifest.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Systems, endpoints and hardware security: threat and failure analysis

### Learning outcomes

You will (1) list misuse and failure scenarios; (2) rank by likelihood and impact; (3) link scenarios to requirements.

### 23.1 Scenarios

Mateo lists seven scenarios, from personal files left behind to a staff laptop lost unencrypted, rating likelihood and impact from 1 to 5.

Section twenty-three point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-three point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-three point one treats scenarios reading the ranking as testable only when evidence and ticket IDs are recorded.

For section twenty-three point one, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — scenario ranking

```python
"""Rank synthetic failure and misuse scenarios by likelihood x impact (stdlib only)."""
sc = [("patron leaves personal files on PC", 5, 3), ("unauthorised software installed by patron", 4, 4),
      ("USB device carries malware", 3, 4), ("firmware update fails and bricks PC", 2, 4),
      ("restore job fails silently", 2, 5), ("staff laptop lost unencrypted", 1, 5), ("boot settings changed in firmware menu", 2, 3)]
for name, l, i in sorted(sc, key=lambda s: -s[1]*s[2]):
    print(f"{l*i:2d}  L{l} I{i}  {name}")
```

Run with `python3 lab_scenarios.py`. Verified output:

```text
16  L4 I4  unauthorised software installed by patron
15  L5 I3  patron leaves personal files on PC
12  L3 I4  USB device carries malware
10  L2 I5  restore job fails silently
 8  L2 I4  firmware update fails and bricks PC
 6  L2 I3  boot settings changed in firmware menu
 5  L1 I5  staff laptop lost unencrypted
```

### 23.2 Reading the ranking

Top: unauthorised software installed by a patron (16), personal files left behind (15), malware via USB (12), silent restore failure (10). Firmware update failure scores 8, boot settings changed 6, lost staff laptop 5.

Section twenty-three point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-three point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-three point two treats scenarios reading the ranking as testable only when evidence and ticket IDs are recorded.

### 23.3 Linking to requirements

Software installs map to R5; files to R4; USB to R3; silent restore failure to R9; firmware update failure to firmware resilience; boot settings to R2; staff laptop to R8.

Section twenty-three point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-three point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-three point three treats scenarios reading the ranking as testable only when evidence and ticket IDs are recorded.

### 23.4 Coverage

Every scenario has at least one requirement; silent restore failure, though lower ranked, has severe impact.

Section twenty-three point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-three point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-three point four treats scenarios reading the ranking as testable only when evidence and ticket IDs are recorded.

For section twenty-three point four, Fernhill Library Network will not accept systems work without a written trail.

### Reasoning for ratings

Each rating carries one sentence of reasoning. For example, unauthorised software installs score likelihood 4 because staff report them weekly, and impact 4 because toolbars can capture what patrons type. Personal files score likelihood 5 because they occur daily, impact 3 because exposure is usually limited to the next user. Writing reasons lets Marta and Dr Novak challenge specific judgements.

The ratings are revisited after deployment to see which scenarios still occur.

### No attack detail

Scenarios describe outcomes, not methods, keeping the analysis defensive.

### Updating the analysis

After deployment, the team re-rates scenarios: personal files left behind drops to likelihood 1, because restore removes them nightly; unauthorised software drops to 1 after enforcement. Re-rating shows the design's effect in risk terms.

### Including staff devices

Staff laptops are included because they connect to the same management server.

### Worked example

Dr Novak asks why the lost laptop scores low. Mateo explains staff laptops rarely leave buildings and few exist, but impact is high, so R8 remains a must-have.

> **Synthetic case.** Synthetic ratings.

### Errors and limits

Scores are judgements; record reasons for each.

### Exercises

- **EX067 — Top three.** Name the top three scenarios. *Rubric:* 3 = software install, files left, USB malware; 2 = two; 1 = one; 0 = none.
- **EX068 — Silent failure.** Why does silent restore failure matter despite rank? *Rubric:* 3 = impact 5; 2 = partial; 1 = none; 0 = none.
- **EX069 — Mapping.** Which requirement addresses USB malware? *Rubric:* 3 = R3; 2 = partial; 1 = none; 0 = none.

### Synthesis

Rank scenarios and ensure each maps to a requirement.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Systems, endpoints and hardware security: methods I

### Learning outcomes

You will (1) verify an image against hardening requirements; (2) use benchmarks and STIGs as sources; (3) close gaps.

### 24.1 Sources

CIS Benchmarks and Microsoft baselines provide recommended settings; DISA STIGs offer stricter options. Mateo selects ten requirements relevant to kiosks.

Section twenty-four point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-four point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-four point one treats sources reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-four point one, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — image hardening check

```python
"""Check a synthetic kiosk image configuration against hardening requirements (stdlib only)."""
req = {"secure_boot": True, "firmware_password": True, "usb_storage": False, "user_is_admin": False, "autorun": False,
       "disk_encryption": True, "app_control": "enforce", "auto_logoff_min": 15, "remote_logging": True, "smb1": False}
image = {"secure_boot": True, "firmware_password": False, "usb_storage": False, "user_is_admin": False, "autorun": False,
         "disk_encryption": True, "app_control": "audit", "auto_logoff_min": 15, "remote_logging": True, "smb1": False}
gaps = [k for k in req if image[k] != req[k]]
print(f"requirements {len(req)}, met {len(req)-len(gaps)}")
for g in gaps: print(f"  gap: {g} (required {req[g]}, image {image[g]})")
```

Run with `python3 lab_harden.py`. Verified output:

```text
requirements 10, met 8
  gap: firmware_password (required True, image False)
  gap: app_control (required enforce, image audit)
```

### 24.2 Reading the result

Eight of ten requirements are met. Gaps: firmware password not set, and application control in audit rather than enforce mode.

Section twenty-four point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-four point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-four point two treats sources reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-four point two, Fernhill Library Network will not accept systems work without a written trail.

### 24.3 Closing gaps

Firmware passwords are set through the vendor's management tool. Application control stays in audit until chapter 31 evaluates the allowlist, avoiding blocking needed tools.

Section twenty-four point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-four point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-four point three treats sources reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-four point three, Fernhill Library Network will not accept systems work without a written trail.

### 24.4 Recording

Each gap and decision is recorded in the image release notes.

Section twenty-four point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-four point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-four point four treats sources reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-four point four, Fernhill Library Network will not accept systems work without a written trail.

### Choosing among sources

CIS Benchmarks offer levels: Level 1 settings are practical for most organisations, Level 2 stricter. DISA STIGs are designed for defence systems and can be too strict for a library. Mateo chooses mostly Level 1 settings plus a few kiosk-specific ones, such as USB storage blocking, and records why each was chosen.

He checks each setting against accessibility needs, since some strict settings disable features screen readers use.

### Repeatable check

The hardening check runs automatically on each new image release, so gaps cannot slip in unnoticed.

### Firmware password process

Setting firmware passwords on 300 PCs by hand would take days. The vendor's management tool sets them centrally, and the password is stored in Fernhill's password manager with access limited to IT. The process is documented so it can be repeated for new PCs.

### Recording versions

The check records the benchmark version used, so later reviews know which recommendations were considered.

### Worked example

Marta asks why not enforce immediately. Mateo explains that enforcing an untested allowlist might block accessibility tools, harming patrons; audit first collects evidence.

> **Synthetic case.** Synthetic.

### Errors and limits

Copying benchmark settings without testing can break needed functions.

### Exercises

- **EX070 — Lab gaps.** Which two gaps were found? *Rubric:* 3 = firmware password, app control audit; 2 = partial; 1 = none; 0 = none.
- **EX071 — Sources.** Name three sources for settings. *Rubric:* 3 = CIS, Microsoft baselines, STIGs; 2 = two; 1 = one; 0 = none.
- **EX072 — Audit first.** Why keep application control in audit? *Rubric:* 3 = avoid blocking needed tools; 2 = partial; 1 = none; 0 = none.

### Synthesis

Check images against requirements and close gaps deliberately.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) present an initial design for critique; (2) respond to feedback; (3) iterate.

### 25.1 Studio format

Students present designs to peers and industry guests, who critique them.

Section twenty-five point one develops design studio with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-five point one, Marta Silva expects design claims to carry owners and dates.

Section twenty-five point one treats studio format mateo's design as testable only when evidence and ticket IDs are recorded.

For section twenty-five point one, Fernhill Library Network will not accept design work without a written trail.

Section twenty-five point one fails closed if design evidence is missing rather than guessing.

### 25.2 Mateo's design

A hardened golden image, nightly restore of the patron area, Secure Boot with firmware password, application control, USB storage blocked, public segment and monitoring.

Section twenty-five point two develops design studio with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-five point two, Marta Silva expects design claims to carry owners and dates.

Section twenty-five point two treats studio format mateo's design as testable only when evidence and ticket IDs are recorded.

For section twenty-five point two, Fernhill Library Network will not accept design work without a written trail.

### 25.3 Feedback

A guest asks how patrons save work. Another asks what happens when the restore server is down.

Section twenty-five point three develops design studio with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-five point three, Marta Silva expects design claims to carry owners and dates.

Section twenty-five point three treats studio format mateo's design as testable only when evidence and ticket IDs are recorded.

For section twenty-five point three, Fernhill Library Network will not accept design work without a written trail.

### 25.4 Responses

Patrons can save to their own USB storage? No: USB storage is blocked, so the notice directs them to email or cloud storage; a print-to-PDF option helps. If the server is down, PCs restore from a local protected copy.

Section twenty-five point four develops design studio with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-five point four, Marta Silva expects design claims to carry owners and dates.

Section twenty-five point four treats studio format mateo's design as testable only when evidence and ticket IDs are recorded.

### 25.5 Iteration

The local restore copy becomes a design change.

Section twenty-five point five develops design studio with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-five point five, Marta Silva expects design claims to carry owners and dates.

Section twenty-five point five treats studio format mateo's design as testable only when evidence and ticket IDs are recorded.

For section twenty-five point five, Fernhill Library Network will not accept design work without a written trail.

Section twenty-five point five fails closed if design evidence is missing rather than guessing.

### Learning from critique

After the studio, Mateo groups feedback into three types: misunderstanding (fix the explanation), new requirement (add and trace) and alternative idea (evaluate later). The saving-work question exposed a missing requirement for patron guidance; the server-down question revealed a resilience gap. Both lead to design changes.

He thanks the guests and sends them a short note on what changed, which builds relationships for later reviews.

### Studio records

Studio feedback and responses are stored with the decision records.

### Preparing for studio

Mateo prepares a ten-minute presentation, a one-page summary and a list of open questions he wants feedback on. Asking specific questions gets more useful critique than asking guests for general comments.

### Peer review roles

Each student also reviews one peer's design, practising critique as well as receiving it. Mateo reviews a hospital kiosk design and learns from its approach to cleaning shared keyboards, a physical hygiene issue with parallels to data hygiene.

### Worked example

A peer suggests allowing USB storage for read-only use. Mateo records it as an option to evaluate, weighing patron needs against malware risk.

> **Synthetic case.** Synthetic.

### Errors and limits

Defending a design instead of listening wastes the studio.

### Exercises

- **EX073 — Guest questions.** What two questions did guests ask? *Rubric:* 3 = saving work; server down; 2 = partial; 1 = none; 0 = none.
- **EX074 — Server down.** How does the design handle server outage? *Rubric:* 3 = local protected copy; 2 = partial; 1 = none; 0 = none.
- **EX075 — Read-only USB.** How was the read-only USB idea handled? *Rubric:* 3 = recorded as option to evaluate; 2 = partial; 1 = none; 0 = none.

### Synthesis

Studio critique improves designs when feedback is recorded and weighed.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Systems, endpoints and hardware security: architecture alternatives

### Learning outcomes

You will (1) compare alternative architectures; (2) evaluate trade-offs; (3) select with reasons.

### 26.1 Alternative A

Full disk reimage nightly from the network: strongest reset, but slow and network-heavy.

Section twenty-six point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-six point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-six point one treats alternative alternative alternative criteria as testable only when evidence and ticket IDs are recorded.

For section twenty-six point one, Fernhill Library Network will not accept systems work without a written trail.

### 26.2 Alternative B

Patron-area restore plus signed golden image updates monthly: faster, less traffic, relies on strong OS protection for system areas.

Section twenty-six point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-six point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-six point two treats alternative alternative alternative criteria as testable only when evidence and ticket IDs are recorded.

For section twenty-six point two, Fernhill Library Network will not accept systems work without a written trail.

### 26.3 Alternative C

Thin clients with sessions hosted centrally: easier to manage but needs new hardware and server capacity.

Section twenty-six point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-six point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-six point three treats alternative alternative alternative criteria as testable only when evidence and ticket IDs are recorded.

For section twenty-six point three, Fernhill Library Network will not accept systems work without a written trail.

### 26.4 Criteria

Security, restore time, network load, cost and accessibility.

Section twenty-six point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-six point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-six point four treats alternative alternative alternative criteria as testable only when evidence and ticket IDs are recorded.

For section twenty-six point four, Fernhill Library Network will not accept systems work without a written trail.

Section twenty-six point four fails closed if systems evidence is missing rather than guessing.

### 26.5 Choice

B with a weekly full reimage: daily patron reset, weekly system reset, using existing hardware.

Section twenty-six point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-six point five, Marta Silva expects systems claims to carry owners and dates.

Section twenty-six point five treats alternative alternative alternative criteria as testable only when evidence and ticket IDs are recorded.

For section twenty-six point five, Fernhill Library Network will not accept systems work without a written trail.

### Scoring alternatives

Mateo scores each alternative from 1 to 5 on each criterion. A scores 5 on security but 2 on network load and 3 on restore time. B scores 4 on security, 4 on restore time and 4 on network load. C scores 4 on security but 1 on cost. B's total is highest, and a weekly full reimage raises its security score by resetting system areas too.

He shows the scoring table to Marta and notes that the scores are judgements, so the table supports discussion rather than replacing it.

### Revisiting

The choice will be revisited when hardware is replaced, when C may become affordable.

### Communicating the choice

The choice is explained to librarians in plain words: computers clear patron files every night and fully refresh once a week.

### Sensitivity

Mateo checks whether changing one score would alter the choice. Only a large change in cost would favour C, so the decision is robust.

### Documentation

The decision record includes the scoring table.

### Agreement

Marta and Dr Novak agree with the choice.

### Worked example

The board asks for the cost of C. Mateo estimates new hardware at a cost Fernhill cannot meet this year; C is recorded as a future option.

> **Synthetic case.** Synthetic.

### Errors and limits

Choosing on a single criterion hides costs elsewhere.

### Exercises

- **EX076 — Alternatives.** Name the three alternatives. *Rubric:* 3 = full reimage, patron restore, thin clients; 2 = two; 1 = one; 0 = none.
- **EX077 — Criteria.** List the selection criteria. *Rubric:* 3 = security, time, network, cost, accessibility; 2 = four; 1 = two; 0 = none.
- **EX078 — Choice.** What was chosen? *Rubric:* 3 = B plus weekly full reimage; 2 = partial; 1 = none; 0 = none.

### Synthesis

Compare alternatives on several criteria and record the choice.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Systems, endpoints and hardware security: control design

### Learning outcomes

You will (1) specify each control in detail; (2) define parameters and failure behaviour; (3) document dependencies.

### 27.1 Restore control

Runs at 22:00 after closing; restores the patron area from the protected copy; verifies digests; reports result.

Section twenty-seven point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-seven point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-seven point one treats restore control application control as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point one, Fernhill Library Network will not accept systems work without a written trail.

### 27.2 Application control

Allowlist of approved programs by publisher signature and path; audit mode first, then enforce.

Section twenty-seven point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-seven point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-seven point two treats restore control application control as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point two, Fernhill Library Network will not accept systems work without a written trail.

### 27.3 Boot control

Secure Boot on; firmware password set; boot order locked to internal disk.

Section twenty-seven point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-seven point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-seven point three treats restore control application control as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point three, Fernhill Library Network will not accept systems work without a written trail.

### 27.4 Failure behaviour

If restore fails, the PC shows "out of service" at next start and alerts staff; it does not open a session.

Section twenty-seven point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-seven point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-seven point four treats restore control application control as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point four, Fernhill Library Network will not accept systems work without a written trail.

### 27.5 Dependencies

Restore depends on boot integrity; alerts depend on logging; updates depend on signing keys.

Section twenty-seven point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-seven point five, Marta Silva expects systems claims to carry owners and dates.

Section twenty-seven point five treats restore control application control as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point five, Fernhill Library Network will not accept systems work without a written trail.

### Logging design

Each control logs its own actions: restore start, end, success and digest result; application control blocks; firmware setting checks; USB block events. Logs go to the central server with time synchronised, following NIST SP 800-92 guidance on consistent timestamps and protected storage. Logs exclude patron content.

Mateo specifies which events trigger alerts and which are only stored, to avoid alert fatigue.

### Parameters as configuration

Times, thresholds and lists are kept in configuration files under version control, not hard-coded in scripts.

### Reviewing the design

Marta and Dr Novak review each control specification before implementation, checking parameters, failure behaviour and logging.

### Interfaces of controls

Restore reports to the management server; application control reports blocks; both feed the dashboard.

### Review cycle

Specifications are reviewed after each verification round.

### Change control

Changes to parameters need approval.

### Accessibility in controls

Each control specification includes a note on accessibility impact. For example, the auto-logoff warning must be readable by screen readers.

### Worked example

Mateo asks Marta what staff should see for an out-of-service PC. They agree on a simple screen with a phone number for IT.

> **Synthetic case.** Synthetic.

### Errors and limits

Controls without defined failure behaviour fail open by accident.

### Exercises

- **EX079 — Restore schedule.** When does restore run and what follows? *Rubric:* 3 = 22:00; verify digests; report; 2 = partial; 1 = none; 0 = none.
- **EX080 — Failure behaviour.** What happens if restore fails? *Rubric:* 3 = out of service, alert, no session; 2 = partial; 1 = none; 0 = none.
- **EX081 — Dependencies.** What does restore depend on? *Rubric:* 3 = boot integrity; 2 = partial; 1 = none; 0 = none.

### Synthesis

Define each control's parameters, failure behaviour and dependencies.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Systems, endpoints and hardware security: implementation I

### Learning outcomes

You will (1) implement the restore mechanism on lab PCs; (2) detect session changes; (3) verify that restore reverts them.

### 28.1 Implementation

Mateo configures three lab PCs with the golden image and restore script.

Section twenty-eight point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-eight point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-eight point one treats implementation test session reading as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point one, Fernhill Library Network will not accept systems work without a written trail.

### 28.2 Test session

A synthetic session changes the browser home page and saves a CV in the patron area.

Section twenty-eight point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-eight point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-eight point two treats implementation test session reading as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point two, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — session changes and restore

```python
"""Detect files changed during a patron session and confirm the nightly restore reverts them (synthetic)."""
import hashlib
def h(b): return hashlib.sha256(b).hexdigest()
golden = {"/sys/policy.cfg": h(b"policy v3"), "/apps/browser.cfg": h(b"home=library"), "/home/patron/.keep": h(b"")}
after_session = dict(golden, **{"/apps/browser.cfg": h(b"home=other"), "/home/patron/cv.docx": h(b"cv")})
after_restore = dict(golden)
changed = [p for p in after_session if golden.get(p) != after_session[p]]
print(f"changed or added during session: {len(changed)} -> {', '.join(changed)}")
left = [p for p in after_restore if golden.get(p) != after_restore[p]] + [p for p in golden if p not in after_restore]
print(f"differences after restore: {len(left)}")
```

Run with `python3 lab_restore.py`. Verified output:

```text
changed or added during session: 2 -> /apps/browser.cfg, /home/patron/cv.docx
differences after restore: 0
```

### 28.3 Reading the result

Two items changed or were added during the session: the browser configuration and the CV. After restore, there are zero differences from the golden manifest.

Section twenty-eight point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-eight point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-eight point three treats implementation test session reading as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point three, Fernhill Library Network will not accept systems work without a written trail.

### 28.4 Assumption checked

This confirms the chapter 6 assumption of full removal for the patron area.

Section twenty-eight point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-eight point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-eight point four treats implementation test session reading as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point four, Fernhill Library Network will not accept systems work without a written trail.

### 28.5 Edge cases

Tests also cover a session ended by power loss and a PC rebooted mid-restore; both restore correctly at next start.

Section twenty-eight point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-eight point five, Marta Silva expects systems claims to carry owners and dates.

Section twenty-eight point five treats implementation test session reading as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point five, Fernhill Library Network will not accept systems work without a written trail.

### Test plan

The implementation test plan lists each scenario: normal session, power loss mid-session, reboot mid-restore, files in unusual locations and a full disk. Each has expected results. Running them on three lab PCs takes two days and finds the temp folder issue, which would otherwise have left patron files behind in production.

Tests are repeated after every change to the restore script.

### Performance check

Restore takes about five minutes on lab PCs, well within the window.

### Recording results

Each test result is stored with the image version, PC, date and tester. The temp folder fix is recorded as a change with its reason.

### Next

Measurement in chapter 29 extends tests to branch PCs during a pilot week.

### Lessons

Testing unusual locations matters because patrons save files wherever software suggests.

### Worked example

A test reveals that files saved in a temporary folder outside the patron area survived restore. Mateo adds that folder to the restore scope and re-tests.

> **Synthetic case.** Synthetic.

### Errors and limits

Restore scope must include every location patrons can write.

### Exercises

- **EX082 — Lab changes.** What changed during the test session? *Rubric:* 3 = browser config, CV added; 2 = partial; 1 = none; 0 = none.
- **EX083 — Post-restore.** How many differences remained after restore? *Rubric:* 3 = 0; 2 = partial; 1 = none; 0 = none.
- **EX084 — Temp folder.** What did the temp folder test reveal? *Rubric:* 3 = files survived outside scope; 2 = partial; 1 = none; 0 = none.

### Synthesis

Test restore against real session behaviour and fix scope gaps.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Systems, endpoints and hardware security: measurement

### Learning outcomes

You will (1) measure restore times across branches; (2) summarise variation; (3) check against the operating window.

### 29.1 Measures

Restore duration per PC per night, by branch, over a week of pilot operation.

Section twenty-nine point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-nine point one, Marta Silva expects systems claims to carry owners and dates.

Section twenty-nine point one treats measures reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point one, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — restore timing

```python
"""Summarise synthetic nightly restore times across branches (stdlib only)."""
import statistics
t = {"Central": [6.1, 6.4, 5.9, 6.8, 7.2, 6.0, 6.3], "Eastgate": [8.9, 9.4, 9.1, 12.8, 9.0, 9.2, 9.3],
     "Millbrook": [5.2, 5.5, 5.1, 5.4, 5.3, 5.6, 5.2]}
for b, xs in t.items():
    print(f"{b:9} median {statistics.median(xs):.1f} min, max {max(xs):.1f}, stdev {statistics.stdev(xs):.2f}")
allx = [x for xs in t.values() for x in xs]
print(f"all: median {statistics.median(allx):.1f}, within 15-min window {sum(x <= 15 for x in allx)}/{len(allx)}")
```

Run with `python3 lab_timing.py`. Verified output:

```text
Central   median 6.3 min, max 7.2, stdev 0.47
Eastgate  median 9.2 min, max 12.8, stdev 1.39
Millbrook median 5.3 min, max 5.6, stdev 0.18
all: median 6.3, within 15-min window 21/21
```

### 29.2 Reading the result

Central median 6.3 minutes (max 7.2), Eastgate median 9.2 (max 12.8, stdev 1.39), Millbrook median 5.3 (max 5.6). All 21 sampled restores finished within the 15-minute window.

Section twenty-nine point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-nine point two, Marta Silva expects systems claims to carry owners and dates.

Section twenty-nine point two treats measures reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point two, Fernhill Library Network will not accept systems work without a written trail.

### 29.3 Eastgate variation

Eastgate is slower and more variable. Investigation finds older disks and a congested network link.

Section twenty-nine point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-nine point three, Marta Silva expects systems claims to carry owners and dates.

Section twenty-nine point three treats measures reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point three, Fernhill Library Network will not accept systems work without a written trail.

### 29.4 Action

Eastgate's disks are scheduled for replacement and its restore traffic is staggered.

Section twenty-nine point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section twenty-nine point four, Marta Silva expects systems claims to carry owners and dates.

Section twenty-nine point four treats measures reading the result as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point four, Fernhill Library Network will not accept systems work without a written trail.

### Why spread matters

If restore times varied widely, some nights might overrun the window and leave PCs unavailable at opening. The standard deviation shows how predictable restores are. Eastgate's 1.39 minutes is much larger than Millbrook's 0.18, signalling that something there is unstable. Investigating spread often reveals hardware or network problems before they cause failures.

Mateo plots each branch's times on a simple chart for the dashboard.

### Sampling

The lab uses seven nights per branch; production monitoring uses every PC every night.

### Pilot setup

The pilot week runs restore on a sample of seven PCs per branch, chosen to include each hardware model. Results are collected automatically.

### Communicating

Branch staff are told about the pilot and asked to report any PC problems at opening.

### Linking to requirements

The 15-minute window is part of R4, so timing results also count as verification evidence.

### Alert on slow restore

A restore exceeding 13 minutes triggers a warning, giving time to act before the window closes.

### Repeat

Timing is re-measured monthly.

### Worked example

Marta asks whether 12.8 minutes is a problem. Mateo notes it is within the window but close enough that growth could exceed it, so the fix is worthwhile.

> **Synthetic case.** Synthetic.

### Errors and limits

Medians hide outliers; report maximum and spread too.

### Exercises

- **EX085 — Lab medians.** Give the branch medians. *Rubric:* 3 = 6.3, 9.2, 5.3; 2 = two; 1 = one; 0 = none.
- **EX086 — Window.** How many restores fit the window? *Rubric:* 3 = 21/21; 2 = partial; 1 = none; 0 = none.
- **EX087 — Eastgate cause.** Why is Eastgate slower? *Rubric:* 3 = older disks, congested link; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure spread as well as averages and act on outliers.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify requirements on lab PCs; (2) record evidence; (3) distinguish pass, fail and untested.

### 30.1 Verification

For each requirement, Mateo runs its test on lab PCs and records evidence: screenshots of settings, logs and test outputs.

Section thirty point one develops verification laboratory with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty point one, Marta Silva expects verification claims to carry owners and dates.

Section thirty point one treats verification examples recording independence as testable only when evidence and ticket IDs are recorded.

For section thirty point one, Fernhill Library Network will not accept verification work without a written trail.

### 30.2 Examples

R1 verified by firmware report; R3 by inserting a synthetic USB storage device and confirming block; R6 by idle timeout test.

Section thirty point two develops verification laboratory with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty point two, Marta Silva expects verification claims to carry owners and dates.

Section thirty point two treats verification examples recording independence as testable only when evidence and ticket IDs are recorded.

For section thirty point two, Fernhill Library Network will not accept verification work without a written trail.

### 30.3 Recording

Each result is pass, fail or untested, with date and tester.

Section thirty point three develops verification laboratory with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty point three, Marta Silva expects verification claims to carry owners and dates.

Section thirty point three treats verification examples recording independence as testable only when evidence and ticket IDs are recorded.

For section thirty point three, Fernhill Library Network will not accept verification work without a written trail.

Section thirty point three fails closed if verification evidence is missing rather than guessing.

### 30.4 Independence

A technician repeats three tests without Mateo present.

Section thirty point four develops verification laboratory with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty point four, Marta Silva expects verification claims to carry owners and dates.

Section thirty point four treats verification examples recording independence as testable only when evidence and ticket IDs are recorded.

For section thirty point four, Fernhill Library Network will not accept verification work without a written trail.

Section thirty point four fails closed if verification evidence is missing rather than guessing.

### 30.5 Findings

Remote logging (R7) is not reaching the central server from one lab PC due to a firewall rule.

Section thirty point five develops verification laboratory with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty point five, Marta Silva expects verification claims to carry owners and dates.

Section thirty point five treats verification examples recording independence as testable only when evidence and ticket IDs are recorded.

For section thirty point five, Fernhill Library Network will not accept verification work without a written trail.

### Evidence quality

Evidence should allow someone else to check the result. Screenshots show settings at a moment; logs show events with timestamps; test outputs show results. Mateo stores each with the requirement ID, date and tester, and avoids evidence that contains patron data.

He also records the image version tested, so evidence stays linked to the right release.

### Fixing failures

Failed requirements get a fix, a re-test and a note explaining the cause.

### Planning the lab

Mateo schedules verification over two days, grouping tests by setup: firmware tests first, then OS, application, network and monitoring. Grouping saves time and reduces mistakes when switching contexts.

Each test has a written procedure so the technician can repeat it independently.

### Independent repeats

The technician repeats R1, R3 and R6 independently. All match Mateo's results.

### Release decision

The image is not released until R7 is fixed.

### Coverage

Every requirement has a test before release, and the test list is reviewed when requirements change.

### Timing

The lab finishes within the planned two days.

### Worked example

The technician's repeat of R3 passes. R7's failure is logged and a rule fix scheduled.

> **Synthetic case.** Synthetic.

### Errors and limits

Verification by the designer alone can miss errors.

### Exercises

- **EX088 — R3 test.** How was R3 verified? *Rubric:* 3 = insert synthetic USB, confirm block; 2 = partial; 1 = none; 0 = none.
- **EX089 — Result states.** What states can a verification have? *Rubric:* 3 = pass, fail, untested; 2 = partial; 1 = none; 0 = none.
- **EX090 — R7 finding.** Why did R7 fail? *Rubric:* 3 = firewall rule; 2 = partial; 1 = none; 0 = none.

### Synthesis

Verify each requirement with recorded, independent evidence.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Systems, endpoints and hardware security: implementation II

### Learning outcomes

You will (1) evaluate an application allowlist against a week of executions; (2) protect accessibility; (3) decide when to enforce.

### 31.1 Audit data

With application control in audit mode for a week, the system logs every program that would have been blocked.

Section thirty-one point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-one point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-one point one treats audit data reading the as testable only when evidence and ticket IDs are recorded.

For section thirty-one point one, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — allowlist evaluation

```python
"""Evaluate an application allowlist against a synthetic week of execution events (stdlib only)."""
allow = {"browser.exe", "office.exe", "pdfviewer.exe", "catalogue.exe", "printclient.exe"}
events = [("browser.exe", 900), ("office.exe", 310), ("pdfviewer.exe", 220), ("catalogue.exe", 150),
          ("printclient.exe", 400), ("game_setup.exe", 6), ("toolbar_installer.exe", 3), ("accessibility_reader.exe", 14)]
blocked = [(e, n) for e, n in events if e not in allow]
total = sum(n for _, n in events)
print(f"executions {total}, would be blocked {sum(n for _, n in blocked)}")
for e, n in blocked: print(f"  {e}: {n}")
```

Run with `python3 lab_allow.py`. Verified output:

```text
executions 2003, would be blocked 23
  game_setup.exe: 6
  toolbar_installer.exe: 3
  accessibility_reader.exe: 14
```

### 31.2 Reading the result

Of 2,003 executions, 23 would be blocked: game_setup.exe (6), toolbar_installer.exe (3) and accessibility_reader.exe (14).

Section thirty-one point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-one point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-one point two treats audit data reading the as testable only when evidence and ticket IDs are recorded.

For section thirty-one point two, Fernhill Library Network will not accept systems work without a written trail.

### 31.3 Interpretation

The game and toolbar installers are exactly what the control should stop. The accessibility reader is a needed tool missing from the list.

Section thirty-one point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-one point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-one point three treats audit data reading the as testable only when evidence and ticket IDs are recorded.

For section thirty-one point three, Fernhill Library Network will not accept systems work without a written trail.

### 31.4 Fix and enforce

The reader is added by publisher signature; another audit week shows only unwanted installers blocked; enforce mode begins.

Section thirty-one point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-one point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-one point four treats audit data reading the as testable only when evidence and ticket IDs are recorded.

For section thirty-one point four, Fernhill Library Network will not accept systems work without a written trail.

### Allowlist design choices

Allowlists can identify programs by file path, by file hash or by publisher signature. Paths are easy but weak, because a user might place a different program at an allowed path if permissions allow. Hashes are precise but break with every update. Publisher signatures balance both: any version signed by an approved publisher runs. Microsoft's application control documentation describes these rule types. Fernhill uses publisher rules for most software and hash rules for a few unsigned tools.

Patrons run as standard users who cannot write to program folders, which also protects path-based rules.

### Monitoring blocks

After enforcement, each block is logged. A weekly review checks for new needed tools blocked by mistake.

### Communicating

Librarians are told what patrons will see if a program is blocked and how to request additions.

### Second audit week

The second audit week confirms only unwanted installers are blocked.

### Fairness

Protecting accessibility tools is a fairness requirement, not a convenience.

### Worked example

A librarian confirms that two patrons use the reader daily. Without the audit week, enforcing would have blocked them.

> **Synthetic case.** Synthetic.

### Errors and limits

Audit periods must be long enough to see weekly patterns.

### Exercises

- **EX091 — Lab counts.** How many executions would be blocked and which? *Rubric:* 3 = 23: game 6, toolbar 3, reader 14; 2 = two; 1 = one; 0 = none.
- **EX092 — Reader fix.** How was the reader added? *Rubric:* 3 = by publisher signature; 2 = partial; 1 = none; 0 = none.
- **EX093 — Audit value.** What did the audit week prevent? *Rubric:* 3 = blocking accessibility users; 2 = partial; 1 = none; 0 = none.

### Synthesis

Audit before enforcing and protect accessibility.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Systems, endpoints and hardware security: reliability

### Learning outcomes

You will (1) calculate availability and MTBF; (2) compare before and after self-restore; (3) interpret reliability figures.

### 32.1 Data

In a month, 42 PC failures occurred across 300 PCs. Before self-restore, each took about 18 hours to fix manually; after, about half an hour.

Section thirty-two point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-two point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-two point one treats data reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-two point one, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — availability

```python
"""Availability of the public PC service from synthetic failure and repair data (stdlib only)."""
pcs, hours = 300, 24*30
failures, mttr_before, mttr_after = 42, 18.0, 0.5
for label, mttr in (("before self-restore", mttr_before), ("after self-restore", mttr_after)):
    down = failures * mttr
    print(f"{label}: downtime {down:.0f} PC-hours, availability {1 - down/(pcs*hours):.4f}")
print(f"MTBF per PC {pcs*hours/failures:.0f} hours")
```

Run with `python3 lab_avail.py`. Verified output:

```text
before self-restore: downtime 756 PC-hours, availability 0.9965
after self-restore: downtime 21 PC-hours, availability 0.9999
MTBF per PC 5143 hours
```

### 32.2 Reading the result

Downtime falls from 756 to 21 PC-hours; availability rises from 0.9965 to 0.9999. MTBF per PC is about 5,143 hours.

Section thirty-two point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-two point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-two point two treats data reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-two point two, Fernhill Library Network will not accept systems work without a written trail.

### 32.3 Meaning

Fewer PCs out of service means patrons wait less and staff handle fewer complaints.

Section thirty-two point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-two point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-two point three treats data reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-two point three, Fernhill Library Network will not accept systems work without a written trail.

### 32.4 Assumptions

Failure count is assumed unchanged; self-restore may also reduce failures, which would further improve results.

Section thirty-two point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-two point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-two point four treats data reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-two point four, Fernhill Library Network will not accept systems work without a written trail.

### Definitions

Availability is the share of time a service is usable: one minus downtime divided by total time. MTBF, mean time between failures, is total operating time divided by the number of failures. MTTR, mean time to repair, is average repair time. Availability improves by reducing failures (raising MTBF) or speeding repair (lowering MTTR). Self-restore mainly lowers MTTR, because a PC that misbehaves is fixed overnight automatically instead of waiting for a technician.

Mateo explains these terms on one slide for the board.

### Measuring after

Three months after deployment, the team will measure actual failures and repair times to check the estimate.

### Patron view

From a patron's view, availability means fewer "out of order" signs.

### Board reporting

The board receives the downtime figure quarterly.

### Uncertainty

The 42-failure figure comes from one month; another month might differ. Mateo presents the result as an estimate to be checked against three months of data.

### Linking

Availability links to objective O3.

### Format

Figures appear with units.

### Worked example

The board asks for one number. Mateo offers "downtime fell from 756 to 21 PC-hours a month", which is concrete and understandable.

> **Synthetic case.** Synthetic.

### Errors and limits

Availability figures with four decimals can look more precise than data support.

### Exercises

- **EX094 — Downtime.** Give downtime before and after. *Rubric:* 3 = 756 vs 21 PC-hours; 2 = partial; 1 = none; 0 = none.
- **EX095 — Availability.** Give availability before and after. *Rubric:* 3 = 0.9965 vs 0.9999; 2 = partial; 1 = none; 0 = none.
- **EX096 — MTBF.** What is MTBF per PC? *Rubric:* 3 = ~5,143 hours; 2 = partial; 1 = none; 0 = none.

### Synthesis

Reliability figures show operational value in concrete terms.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Systems, endpoints and hardware security: safety and resilience

### Learning outcomes

You will (1) plan for failures of the design itself; (2) recover from bad images and firmware updates; (3) test recovery.

### 33.1 Bad image

If a released image breaks PCs, staged release limits impact, and PCs can roll back to the previous signed image.

Section thirty-three point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-three point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-three point one treats bad image firmware updates as testable only when evidence and ticket IDs are recorded.

For section thirty-three point one, Fernhill Library Network will not accept systems work without a written trail.

### 33.2 Firmware updates

NIST SP 800-193 emphasises recovery for firmware. Fernhill keeps vendor recovery tools and tests firmware updates on lab PCs first.

Section thirty-three point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-three point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-three point two treats bad image firmware updates as testable only when evidence and ticket IDs are recorded.

For section thirty-three point two, Fernhill Library Network will not accept systems work without a written trail.

### 33.3 Server outage

PCs restore from local protected copies for up to a week without the server.

Section thirty-three point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-three point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-three point three treats bad image firmware updates as testable only when evidence and ticket IDs are recorded.

For section thirty-three point three, Fernhill Library Network will not accept systems work without a written trail.

### 33.4 Recovery drills

Each quarter, the team practises rolling back an image on lab PCs.

Section thirty-three point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-three point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-three point four treats bad image firmware updates as testable only when evidence and ticket IDs are recorded.

For section thirty-three point four, Fernhill Library Network will not accept systems work without a written trail.

### 33.5 Human factors

Instructions are short and printed, for use under pressure.

Section thirty-three point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-three point five, Marta Silva expects systems claims to carry owners and dates.

Section thirty-three point five treats bad image firmware updates as testable only when evidence and ticket IDs are recorded.

For section thirty-three point five, Fernhill Library Network will not accept systems work without a written trail.

Section thirty-three point five fails closed if systems evidence is missing rather than guessing.

### Fail-safe design

When something goes wrong, the PC should fail in a safe state. An out-of-service screen is safe: no patron uses a PC in an unknown state. Opening a session on a PC whose restore failed would be unsafe, because the previous patron's files might remain. Saltzer and Schroeder (1975) called this fail-safe defaults: deny by default when uncertain.

Mateo applies the same rule to updates: a PC that cannot verify a new image's signature keeps its current image.

### Documentation for recovery

Each recovery procedure lists prerequisites, such as keys and tools, so they are prepared in advance.

### Test cadence

Recovery tests run quarterly and after any major change.

### Shared responsibility for recovery

Vendors supply firmware recovery tools; Fernhill keeps them ready.

### People in recovery

At least two trained people can perform each recovery step.

### Communication during recovery

Librarians receive a short message explaining which PCs are affected and when they will return.

### Approval

Recovery plans are approved.

### Worked example

A drill reveals that rollback requires a key held only by Marta. A second authorised person is added.

> **Synthetic case.** Synthetic.

### Errors and limits

Recovery that depends on one person is fragile.

### Exercises

- **EX097 — Bad image.** How is a bad image handled? *Rubric:* 3 = staged release, rollback to previous signed; 2 = partial; 1 = none; 0 = none.
- **EX098 — Server outage.** How long can PCs work without the server? *Rubric:* 3 = up to a week; 2 = partial; 1 = none; 0 = none.
- **EX099 — Drill finding.** What did the drill reveal? *Rubric:* 3 = key only with Marta; 2 = partial; 1 = none; 0 = none.

### Synthesis

Design recovery for the design's own failures.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Systems, endpoints and hardware security: integration

### Learning outcomes

You will (1) integrate the design with library services; (2) manage dependencies on printing, catalogue and session systems; (3) test end to end.

### 34.1 Services

Public PCs must work with the session booking system, the print service and the catalogue.

Section thirty-four point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-four point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-four point one treats services dependencies end-to-end test as testable only when evidence and ticket IDs are recorded.

For section thirty-four point one, Fernhill Library Network will not accept systems work without a written trail.

### 34.2 Dependencies

Each service is listed with owner, interface and test.

Section thirty-four point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-four point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-four point two treats services dependencies end-to-end test as testable only when evidence and ticket IDs are recorded.

For section thirty-four point two, Fernhill Library Network will not accept systems work without a written trail.

Section thirty-four point two fails closed if systems evidence is missing rather than guessing.

### 34.3 End-to-end test

A tester books a session, prints, uses the catalogue and the reader, logs off and confirms restore.

Section thirty-four point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-four point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-four point three treats services dependencies end-to-end test as testable only when evidence and ticket IDs are recorded.

For section thirty-four point three, Fernhill Library Network will not accept systems work without a written trail.

### 34.4 Issues

Printing fails after restore because a printer mapping is stored in the patron area; it is moved to the system image.

Section thirty-four point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-four point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-four point four treats services dependencies end-to-end test as testable only when evidence and ticket IDs are recorded.

For section thirty-four point four, Fernhill Library Network will not accept systems work without a written trail.

### 34.5 Change coordination

Service owners are told before image releases.

Section thirty-four point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-four point five, Marta Silva expects systems claims to carry owners and dates.

Section thirty-four point five treats services dependencies end-to-end test as testable only when evidence and ticket IDs are recorded.

For section thirty-four point five, Fernhill Library Network will not accept systems work without a written trail.

Section thirty-four point five fails closed if systems evidence is missing rather than guessing.

### Integration testing schedule

Integration tests run after each image release and each change to a dependent service. The tester follows a script covering booking, logon, browsing, printing, catalogue use, the accessibility reader, logoff and overnight restore. Results are recorded with the image version and service versions.

The session system vendor is asked to notify Fernhill before updates, so tests can be scheduled. When the vendor forgets once, the end-to-end test after restore catches a logon issue before opening.

### Interface records

Each interface record lists data exchanged, protocol, owner and contact.

### Change calendar

A shared calendar shows planned changes across services to avoid clashes.

### Results

End-to-end tests pass after the printer fix.

### Vendor relationships

Contacts at each vendor are recorded with escalation routes, so integration problems are resolved quickly.

### Lesson

The printer problem showed that restore scope affects integration.

### Ownership

Each dependency has a named owner at Fernhill and at the vendor, and a review date. Owners are told about planned image releases a week ahead.

### Worked example

The catalogue supplier updates its app; the allowlist needs updating by signature. Because rules use publisher signatures, the new version runs without changes.

> **Synthetic case.** Synthetic.

### Errors and limits

Integration problems often appear only end to end.

### Exercises

- **EX100 — Services.** Which services must integrate? *Rubric:* 3 = booking, print, catalogue; 2 = two; 1 = one; 0 = none.
- **EX101 — Print issue.** Why did printing fail after restore? *Rubric:* 3 = mapping in patron area; 2 = partial; 1 = none; 0 = none.
- **EX102 — Signature rules.** Why did the catalogue update work without changes? *Rubric:* 3 = publisher signature rule; 2 = partial; 1 = none; 0 = none.

### Synthesis

Test the whole patron journey end to end.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) present the integrated design; (2) respond to expert critique; (3) prioritise improvements.

### 35.1 Presentation

Mateo presents the design with measurements: restore times, availability and allowlist results.

Section thirty-five point one develops design studio ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-five point one, Marta Silva expects design claims to carry owners and dates.

Section thirty-five point one treats presentation critique responses improvements as testable only when evidence and ticket IDs are recorded.

For section thirty-five point one, Fernhill Library Network will not accept design work without a written trail.

### 35.2 Critique

A guest from another library asks about cost of maintaining the allowlist. Another asks about patrons who need software not on the list.

Section thirty-five point two develops design studio ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-five point two, Marta Silva expects design claims to carry owners and dates.

Section thirty-five point two treats presentation critique responses improvements as testable only when evidence and ticket IDs are recorded.

For section thirty-five point two, Fernhill Library Network will not accept design work without a written trail.

### 35.3 Responses

Maintenance takes about an hour a week; a request form lets librarians propose additions, reviewed weekly.

Section thirty-five point three develops design studio ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-five point three, Marta Silva expects design claims to carry owners and dates.

Section thirty-five point three treats presentation critique responses improvements as testable only when evidence and ticket IDs are recorded.

For section thirty-five point three, Fernhill Library Network will not accept design work without a written trail.

### 35.4 Improvements

Add a dashboard for librarians; automate weekly reimage reports.

Section thirty-five point four develops design studio ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-five point four, Marta Silva expects design claims to carry owners and dates.

Section thirty-five point four treats presentation critique responses improvements as testable only when evidence and ticket IDs are recorded.

For section thirty-five point four, Fernhill Library Network will not accept design work without a written trail.

Section thirty-five point four fails closed if design evidence is missing rather than guessing.

### 35.5 Prioritising

Dashboard first, because librarians are the daily users.

Section thirty-five point five develops design studio ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-five point five, Marta Silva expects design claims to carry owners and dates.

Section thirty-five point five treats presentation critique responses improvements as testable only when evidence and ticket IDs are recorded.

For section thirty-five point five, Fernhill Library Network will not accept design work without a written trail.

Section thirty-five point five fails closed if design evidence is missing rather than guessing.

### Turning critique into a plan

Mateo lists studio comments in a table with response and priority. Dashboard for librarians: high, because it reduces calls to IT. Automated reimage reports: medium. Read-only USB: rejected with reasons. Thin clients: future. The table goes to Marta and Dr Novak, who agree the order.

He sends the table to the studio guests, closing the loop.

### Demonstration

The studio includes a live demonstration of a session being restored overnight, using a lab PC and a recorded timelapse.

### Peer learning

Mateo also learns from peers' designs, borrowing the idea of a simple status page.

### Studio outcome

The design is approved for deployment.

### Feedback record

Comments and responses are stored.

### Dashboard design

The dashboard shows, per branch, PCs ready, out of service and blocked programs this week, with simple colours and text labels. Librarians test a mock-up and ask for a clear 'call IT' button, which is added.

### Prioritising time

Mateo estimates hours for each improvement.

### Next

Work begins on the dashboard.

### Timing

Work starts next week.

### Worked example

A peer questions read-only USB again. Mateo presents his evaluation: the scenario ranking shows USB malware at 12, so he keeps USB storage blocked and offers email and cloud saving.

> **Synthetic case.** Synthetic.

### Errors and limits

Improvements without priority compete for limited time.

### Exercises

- **EX103 — Maintenance.** How much time does allowlist maintenance take? *Rubric:* 3 = about an hour a week; 2 = partial; 1 = none; 0 = none.
- **EX104 — Requests.** How can librarians request software? *Rubric:* 3 = form reviewed weekly; 2 = partial; 1 = none; 0 = none.
- **EX105 — USB decision.** Why keep USB storage blocked? *Rubric:* 3 = malware scenario 12; alternatives offered; 2 = partial; 1 = none; 0 = none.

### Synthesis

Present evidence and prioritise improvements for users.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Systems, endpoints and hardware security: performance and scale

### Learning outcomes

You will (1) assess performance impacts; (2) plan for growth; (3) avoid bottlenecks.

### 36.1 Performance

Application control adds negligible delay to program start; restore runs after hours.

Section thirty-six point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-six point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-six point one treats performance network load growth as testable only when evidence and ticket IDs are recorded.

For section thirty-six point one, Fernhill Library Network will not accept systems work without a written trail.

### 36.2 Network load

Weekly full reimages generate large traffic; they are staggered by branch.

Section thirty-six point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-six point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-six point two treats performance network load growth as testable only when evidence and ticket IDs are recorded.

For section thirty-six point two, Fernhill Library Network will not accept systems work without a written trail.

### 36.3 Growth

Fernhill plans 60 more PCs. Restore server capacity is checked: current peak use is 40%.

Section thirty-six point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-six point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-six point three treats performance network load growth as testable only when evidence and ticket IDs are recorded.

For section thirty-six point three, Fernhill Library Network will not accept systems work without a written trail.

### 36.4 Bottlenecks

Eastgate's link is the main bottleneck; upgrading it is recommended.

Section thirty-six point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-six point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-six point four treats performance network load growth as testable only when evidence and ticket IDs are recorded.

For section thirty-six point four, Fernhill Library Network will not accept systems work without a written trail.

### 36.5 Monitoring

Performance metrics join the dashboard.

Section thirty-six point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-six point five, Marta Silva expects systems claims to carry owners and dates.

Section thirty-six point five treats performance network load growth as testable only when evidence and ticket IDs are recorded.

For section thirty-six point five, Fernhill Library Network will not accept systems work without a written trail.

Section thirty-six point five fails closed if systems evidence is missing rather than guessing.

### Measuring performance impact

To check that security controls do not slow patrons down, Mateo measures program start times with application control off and on across 50 launches each. The difference is under a tenth of a second, which patrons will not notice. Logon time is also measured before and after hardening, showing no meaningful change.

These measurements answer a librarian's concern that security would make PCs slow.

### Storage growth

Local restore copies need disk space; Mateo checks that every PC model has enough free space for two image versions.

### Load testing

He simulates all branches reimaging at once to find the upper limit, then confirms staggering keeps load well below it.

### Future capacity

Capacity is reviewed annually.

### Reporting

Performance results go into the thesis and the board update, showing that security did not slow PCs.

### Interpreting

Performance and capacity are sufficient for current and planned use.

### Risks

The Eastgate link remains a risk until upgraded.

### Monitoring

Server load is shown on the IT dashboard.

### Patron experience

Librarians report no complaints about speed after hardening, matching the measurements. Mateo keeps the measurement scripts so they can be rerun after future changes, such as a new browser version that could affect start times.

### Worked example

Mateo simulates adding 60 PCs: peak server use rises to about 48%, within capacity.

> **Synthetic case.** Synthetic.

### Errors and limits

Scaling estimates must be checked after growth.

### Exercises

- **EX106 — Reimage traffic.** How is reimage traffic managed? *Rubric:* 3 = staggered by branch; 2 = partial; 1 = none; 0 = none.
- **EX107 — Capacity.** What is current peak server use and after growth? *Rubric:* 3 = 40% → ~48%; 2 = partial; 1 = none; 0 = none.
- **EX108 — Bottleneck.** What is the main bottleneck? *Rubric:* 3 = Eastgate link; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plan capacity and remove bottlenecks before growth.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Systems, endpoints and hardware security: operations

### Learning outcomes

You will (1) define daily operations; (2) set alerts and runbooks; (3) train staff.

### 37.1 Daily routine

Each morning the technician checks the restore report and repairs failed PCs before opening.

Section thirty-seven point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-seven point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-seven point one treats daily routine alerts runbooks as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point one, Fernhill Library Network will not accept systems work without a written trail.

### 37.2 Alerts

Per-PC restore failures and the five-failure incident threshold from chapter 7 alert IT.

Section thirty-seven point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-seven point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-seven point two treats daily routine alerts runbooks as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point two, Fernhill Library Network will not accept systems work without a written trail.

### 37.3 Runbooks

Short runbooks cover failed restore, out-of-service PCs and image rollback.

Section thirty-seven point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-seven point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-seven point three treats daily routine alerts runbooks as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point three, Fernhill Library Network will not accept systems work without a written trail.

### 37.4 Patching

Monthly OS updates follow SP 800-40r4 planning: test in lab, release to one branch, then all.

Section thirty-seven point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-seven point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-seven point four treats daily routine alerts runbooks as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point four, Fernhill Library Network will not accept systems work without a written trail.

### 37.5 Training

Librarians learn to recognise an out-of-service screen and call IT.

Section thirty-seven point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-seven point five, Marta Silva expects systems claims to carry owners and dates.

Section thirty-seven point five treats daily routine alerts runbooks as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point five, Fernhill Library Network will not accept systems work without a written trail.

### Patch management

NIST SP 800-40 Rev. 4 describes patch management as preventive maintenance with planning for risk. Fernhill's monthly cycle includes: collect updates, build a test image, run requirement and integration tests, release to Millbrook first, then the other branches after two nights without problems. Emergency updates follow a shorter path with the same tests in compressed form.

Each release's dates and results are recorded, giving evidence of timely patching.

### Escalation

If more than five PCs fail at a branch, the technician escalates to Marta immediately.

### Weekly review

Each week, Marta reviews restore failures, blocks and requests.

### Handover between shifts

The technician leaves a short note for the next day's staff.

### Measuring operations

Operations measures include restore success rate, time to repair failures and PCs ready at opening, all shown on the dashboard.

### Runbook example

The failed restore runbook says: check the dashboard, restart the PC, run manual restore, confirm digests, and if it fails again, swap the PC and log a ticket.

### Training records

Each trained person is recorded.

### Holiday cover

A backup person covers the technician's leave, using the same runbooks.

### Review

Runbooks are reviewed quarterly.

### Worked example

On the first operational night, two PCs fail to restore; alerts arrive, and both are repaired by 08:30.

> **Synthetic case.** Synthetic.

### Errors and limits

Operations without runbooks depend on memory.

### Exercises

- **EX109 — Morning task.** What does the technician do each morning? *Rubric:* 3 = check restore report, repair failures; 2 = partial; 1 = none; 0 = none.
- **EX110 — Patching flow.** How are monthly updates released? *Rubric:* 3 = lab, one branch, all; 2 = partial; 1 = none; 0 = none.
- **EX111 — First night.** What happened on the first night? *Rubric:* 3 = two failures, fixed by 08:30; 2 = partial; 1 = none; 0 = none.

### Synthesis

Routine, alerts and runbooks keep the service reliable.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Systems, endpoints and hardware security: validation

### Learning outcomes

You will (1) validate that requirements are met in operation; (2) trace requirements to evidence; (3) identify gaps.

### 38.1 Validation

Validation asks whether the system meets user needs in real use; verification asked whether it met requirements in tests.

Section thirty-eight point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-eight point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-eight point one treats validation reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point one, Fernhill Library Network will not accept systems work without a written trail.

### Lab — Lab — traceability

```python
"""Requirements traceability: which requirements have passing verification evidence (synthetic)."""
reqs = {"R1 secure boot": "pass", "R2 firmware password": "pass", "R3 no USB storage": "pass", "R4 nightly restore": "pass",
        "R5 app control enforce": "pass", "R6 auto logoff": "pass", "R7 remote logging": "fail", "R8 staff disk encryption": "pass",
        "R9 restore alert": "untested", "R10 accessibility tools": "pass"}
c = {s: sum(v == s for v in reqs.values()) for s in ("pass", "fail", "untested")}
print(f"requirements {len(reqs)}: pass {c['pass']}, fail {c['fail']}, untested {c['untested']}")
for r, v in reqs.items():
    if v != "pass": print(f"  {r}: {v}")
```

Run with `python3 lab_trace.py`. Verified output:

```text
requirements 10: pass 8, fail 1, untested 1
  R7 remote logging: fail
  R9 restore alert: untested
```

### 38.2 Reading the result

Of 10 requirements, 8 pass, 1 fails (R7 remote logging) and 1 is untested (R9 restore alert in production).

Section thirty-eight point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-eight point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-eight point two treats validation reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point two, Fernhill Library Network will not accept systems work without a written trail.

### 38.3 Closing

R7's firewall fix is applied and re-tested; R9 is tested by deliberately failing a lab PC's restore and checking the alert.

Section thirty-eight point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-eight point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-eight point three treats validation reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point three, Fernhill Library Network will not accept systems work without a written trail.

### 38.4 User validation

Librarians report fewer patron complaints and no leftover files found in a month.

Section thirty-eight point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-eight point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-eight point four treats validation reading the result as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point four, Fernhill Library Network will not accept systems work without a written trail.

### Verification versus validation

Verification asks: did we build it right? Validation asks: did we build the right thing? A PC could pass every requirement test yet frustrate patrons, for example if the logoff timer were too short for people filling in long forms. Validation therefore includes librarian feedback and patron comments collected at the desk.

One comment asks for longer idle time for job applications. After discussion, auto-logoff stays at 15 minutes but shows a warning two minutes before, with a button to continue.

### Evidence links

Each requirement in the table links to its evidence file.

### Closing gaps

Every failed or untested item gets an owner and date.

### Patron comments

Comment cards at each branch ask patrons whether PCs worked and whether anything was confusing.

### Acting on feedback

The two-minute warning is tested with librarians, who confirm patrons understand it.

### Final table

All requirements are linked to passing evidence after fixes.

### Validation report

A short report summarises validation for Marta.

### Ongoing validation

Comment cards continue after the project.

### Worked example

After fixes, the traceability table shows 10 of 10 passing, with evidence links.

> **Synthetic case.** Synthetic.

### Errors and limits

Passing tests do not guarantee users are satisfied; ask them.

### Exercises

- **EX112 — Lab status.** Give the traceability counts. *Rubric:* 3 = 8 pass, 1 fail, 1 untested; 2 = partial; 1 = none; 0 = none.
- **EX113 — Failing items.** Which requirements failed or were untested? *Rubric:* 3 = R7, R9; 2 = partial; 1 = none; 0 = none.
- **EX114 — User evidence.** What did librarians report? *Rubric:* 3 = fewer complaints, no leftover files; 2 = partial; 1 = none; 0 = none.

### Synthesis

Validate in operation and trace every requirement to evidence.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Systems, endpoints and hardware security: maintainability

### Learning outcomes

You will (1) design for long-term maintenance; (2) document; (3) plan for staff changes.

### 39.1 Documentation

The repository holds image definitions, scripts, runbooks and decision records.

Section thirty-nine point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-nine point one, Marta Silva expects systems claims to carry owners and dates.

Section thirty-nine point one treats documentation simplicity staff changes as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point one, Fernhill Library Network will not accept systems work without a written trail.

### 39.2 Simplicity

One image for all public PCs and few custom scripts keep maintenance manageable.

Section thirty-nine point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-nine point two, Marta Silva expects systems claims to carry owners and dates.

Section thirty-nine point two treats documentation simplicity staff changes as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point two, Fernhill Library Network will not accept systems work without a written trail.

### 39.3 Staff changes

Two people can perform every task; documentation is tested by a new technician.

Section thirty-nine point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-nine point three, Marta Silva expects systems claims to carry owners and dates.

Section thirty-nine point three treats documentation simplicity staff changes as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point three, Fernhill Library Network will not accept systems work without a written trail.

### 39.4 Vendor changes

Hardware refreshes require testing firmware and Secure Boot settings on new models.

Section thirty-nine point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-nine point four, Marta Silva expects systems claims to carry owners and dates.

Section thirty-nine point four treats documentation simplicity staff changes as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point four, Fernhill Library Network will not accept systems work without a written trail.

### 39.5 Review cycle

The design is reviewed annually against updated benchmarks.

Section thirty-nine point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section thirty-nine point five, Marta Silva expects systems claims to carry owners and dates.

Section thirty-nine point five treats documentation simplicity staff changes as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point five, Fernhill Library Network will not accept systems work without a written trail.

Section thirty-nine point five fails closed if systems evidence is missing rather than guessing.

### Maintaining baselines

Benchmarks and vendor baselines change. Each year Mateo's successor compares the image settings with the latest CIS Benchmark and Microsoft baseline, records differences and decides which to adopt. NIST SP 800-128 calls this maintaining the baseline configuration through change control. Without it, a once-strong image slowly falls behind.

The annual review also checks whether any requirement is obsolete.

### Technical debt

Quick fixes, such as a temporary script, are logged as debt with a plan to replace them.

### Training

New staff complete a short training using the runbooks and a lab PC.

### Licences

Software licences are tracked so updates are not blocked by expired licences.

### Retirement

Old PCs are wiped and disposed of securely.

### Successor planning

A named successor is trained.

### Dependencies

Maintenance depends on vendor support for PC models; end-of-support dates are tracked.

### Budget

Annual maintenance time is estimated and included in Fernhill's plan.

### Simplicity check

Each new feature must justify its maintenance cost.

### Annual checklist

An annual checklist covers baseline comparison, requirement review, firmware support dates, licence renewals and documentation review. It takes about a day and keeps the design current.

### Worked example

A new technician follows the runbooks for a week without help, finding one unclear step, which is fixed.

> **Synthetic case.** Synthetic.

### Errors and limits

Systems maintained by one expert become fragile when they leave.

### Exercises

- **EX115 — Repository.** What does the repository hold? *Rubric:* 3 = image definitions, scripts, runbooks, decisions; 2 = three; 1 = two; 0 = none.
- **EX116 — Staff resilience.** How is staff change handled? *Rubric:* 3 = two people per task, tested docs; 2 = partial; 1 = none; 0 = none.
- **EX117 — Review.** How often is the design reviewed? *Rubric:* 3 = annually; 2 = partial; 1 = none; 0 = none.

### Synthesis

Simplicity and documentation sustain the system.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify resilience features; (2) test recovery; (3) record results.

### 40.1 Tests

Mateo tests rollback, server outage, firmware recovery and restore alert.

Section forty point one develops verification laboratory ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty point one, Marta Silva expects verification claims to carry owners and dates.

Section forty point one treats tests rollback outage firmware as testable only when evidence and ticket IDs are recorded.

For section forty point one, Fernhill Library Network will not accept verification work without a written trail.

Section forty point one fails closed if verification evidence is missing rather than guessing.

### 40.2 Rollback

A deliberately broken image on a lab PC is rolled back in ten minutes.

Section forty point two develops verification laboratory ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty point two, Marta Silva expects verification claims to carry owners and dates.

Section forty point two treats tests rollback outage firmware as testable only when evidence and ticket IDs are recorded.

For section forty point two, Fernhill Library Network will not accept verification work without a written trail.

### 40.3 Outage

With the server disconnected for three days, lab PCs restore from local copies each night.

Section forty point three develops verification laboratory ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty point three, Marta Silva expects verification claims to carry owners and dates.

Section forty point three treats tests rollback outage firmware as testable only when evidence and ticket IDs are recorded.

For section forty point three, Fernhill Library Network will not accept verification work without a written trail.

### 40.4 Firmware recovery

A simulated failed firmware update on a lab PC is recovered with the vendor's recovery tool.

Section forty point four develops verification laboratory ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty point four, Marta Silva expects verification claims to carry owners and dates.

Section forty point four treats tests rollback outage firmware as testable only when evidence and ticket IDs are recorded.

For section forty point four, Fernhill Library Network will not accept verification work without a written trail.

### 40.5 Results

All four tests pass; results are recorded with evidence.

Section forty point five develops verification laboratory ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty point five, Marta Silva expects verification claims to carry owners and dates.

Section forty point five treats tests rollback outage firmware as testable only when evidence and ticket IDs are recorded.

For section forty point five, Fernhill Library Network will not accept verification work without a written trail.

Section forty point five fails closed if verification evidence is missing rather than guessing.

### Test design for resilience

Each resilience test has a hypothesis, setup, action, expected result and recovery steps. For the outage test: hypothesis, lab PCs restore from local copies without the server; setup, disconnect server; action, run three nights; expected, all restores succeed; recovery, reconnect server and check reports. Writing tests this way keeps them safe and repeatable.

All tests use lab PCs, never patron PCs during opening hours.

### Results table

A table records each test, date, result and evidence link.

### Follow-ups

Each finding, such as the USB stick requirement, gets an owner.

### Repeat

Tests repeat annually.

### Learning

Tests turn assumptions into evidence.

### Sharing

Results are shared with Marta.

### Comparison

Results are compared with chapter 33's design expectations.

### Gaps

Only the USB stick gap was found.

### Confidence

Passing tests increase confidence that recovery will work.

### Records

Evidence joins the dossier.

### Safety rules

No test runs on patron PCs during opening hours, and every test has a written rollback. These rules are part of the test procedures, approved by Marta.

### Documentation

Each test procedure is stored in the repository with its results and the image version tested.

### Worked example

The firmware test reveals the recovery tool requires a USB stick; one is stored securely at each branch.

> **Synthetic case.** Synthetic.

### Errors and limits

Resilience features that are never tested may not work when needed.

### Exercises

- **EX118 — Rollback time.** How long did rollback take? *Rubric:* 3 = ten minutes; 2 = partial; 1 = none; 0 = none.
- **EX119 — Outage test.** How long was the server disconnected? *Rubric:* 3 = three days; 2 = partial; 1 = none; 0 = none.
- **EX120 — Firmware finding.** What did the firmware test reveal? *Rubric:* 3 = recovery needs USB stick; stored at branches; 2 = partial; 1 = none; 0 = none.

### Synthesis

Test resilience features before relying on them.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Systems, endpoints and hardware security: system optimization

### Learning outcomes

You will (1) optimise restore and update processes; (2) reduce cost and effort; (3) keep security intact.

### 41.1 Targets

Reduce restore time at Eastgate, reduce weekly reimage traffic and reduce allowlist maintenance.

Section forty-one point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-one point one, Marta Silva expects systems claims to carry owners and dates.

Section forty-one point one treats targets restore traffic allowlist as testable only when evidence and ticket IDs are recorded.

For section forty-one point one, Fernhill Library Network will not accept systems work without a written trail.

### 41.2 Restore

Replacing Eastgate's disks cuts its median from 9.2 to about 6 minutes.

Section forty-one point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-one point two, Marta Silva expects systems claims to carry owners and dates.

Section forty-one point two treats targets restore traffic allowlist as testable only when evidence and ticket IDs are recorded.

For section forty-one point two, Fernhill Library Network will not accept systems work without a written trail.

### 41.3 Traffic

Differential reimaging sends only changed blocks, reducing weekly traffic by about two thirds.

Section forty-one point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-one point three, Marta Silva expects systems claims to carry owners and dates.

Section forty-one point three treats targets restore traffic allowlist as testable only when evidence and ticket IDs are recorded.

For section forty-one point three, Fernhill Library Network will not accept systems work without a written trail.

### 41.4 Allowlist

Publisher-based rules reduce manual updates.

Section forty-one point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-one point four, Marta Silva expects systems claims to carry owners and dates.

Section forty-one point four treats targets restore traffic allowlist as testable only when evidence and ticket IDs are recorded.

For section forty-one point four, Fernhill Library Network will not accept systems work without a written trail.

Section forty-one point four fails closed if systems evidence is missing rather than guessing.

### 41.5 Guardrail

Every optimisation is re-verified against requirements before release.

Section forty-one point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-one point five, Marta Silva expects systems claims to carry owners and dates.

Section forty-one point five treats targets restore traffic allowlist as testable only when evidence and ticket IDs are recorded.

For section forty-one point five, Fernhill Library Network will not accept systems work without a written trail.

Section forty-one point five fails closed if systems evidence is missing rather than guessing.

### Measuring optimisation

Each optimisation is measured before and after. Eastgate's median restore falls from 9.2 to about 6 minutes after the disk replacement; weekly reimage traffic falls by about two thirds with differential reimaging; allowlist requests needing manual hash updates fall from several a month to almost none with publisher rules. Each result is recorded with the date and method.

Mateo also checks for side effects: none of the optimisations changes any requirement's test result after the boot-file fix.

### Cost

Disk replacement costs are modest compared with staff time saved.

### Prioritising

Optimisations are chosen by benefit per hour of effort.

### Documentation

Changes are documented in the repository.

### Guardrails

No optimisation may change failure behaviour.

### Review

Marta approves each optimisation.

### Lessons

Optimisation must preserve every requirement.

### Next

Further optimisation waits for hardware refresh.

### Sharing

Results go to the studio.

### Measurement

Each change is measured again after a month.

### Method

Each optimisation follows the same steps: measure, change on a lab PC, verify requirements, release to one branch, measure again and release widely.

### Communication

Branch staff are told when optimisations are released and what, if anything, they might notice.

### Record

Results are logged.

### Worked example

Differential reimaging initially misses a changed boot file; re-verification catches it, and the method is adjusted to always include boot components.

> **Synthetic case.** Synthetic.

### Errors and limits

Optimisation that skips verification can silently weaken security.

### Exercises

- **EX121 — Eastgate.** How much did new disks improve Eastgate? *Rubric:* 3 = 9.2 → ~6 minutes; 2 = partial; 1 = none; 0 = none.
- **EX122 — Traffic.** How much did differential reimaging cut traffic? *Rubric:* 3 = about two thirds; 2 = partial; 1 = none; 0 = none.
- **EX123 — Catch.** What did re-verification catch? *Rubric:* 3 = missed boot file; 2 = partial; 1 = none; 0 = none.

### Synthesis

Optimise only with re-verification.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Systems, endpoints and hardware security: applied research

### Learning outcomes

You will (1) ask a research question from the project; (2) collect data; (3) relate findings to literature.

### 42.1 Question

Does nightly restore reduce help-desk calls about public PCs?

Section forty-two point one develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-two point one, Marta Silva expects systems claims to carry owners and dates.

Section forty-two point one treats question data findings literature as testable only when evidence and ticket IDs are recorded.

For section forty-two point one, Fernhill Library Network will not accept systems work without a written trail.

Section forty-two point one fails closed if systems evidence is missing rather than guessing.

### 42.2 Data

Call logs for three months before and after deployment, categorised by topic.

Section forty-two point two develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-two point two, Marta Silva expects systems claims to carry owners and dates.

Section forty-two point two treats question data findings literature as testable only when evidence and ticket IDs are recorded.

For section forty-two point two, Fernhill Library Network will not accept systems work without a written trail.

### 42.3 Findings

Calls about slow or broken PCs fall by about half; calls about saving work rise slightly.

Section forty-two point three develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-two point three, Marta Silva expects systems claims to carry owners and dates.

Section forty-two point three treats question data findings literature as testable only when evidence and ticket IDs are recorded.

For section forty-two point three, Fernhill Library Network will not accept systems work without a written trail.

### 42.4 Literature

Forrest et al. (1996) proposed defining normal behaviour of Unix processes to detect anomalies; Mateo notes that a fixed image makes "normal" easier to define, supporting future monitoring work.

Section forty-two point four develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-two point four, Marta Silva expects systems claims to carry owners and dates.

Section forty-two point four treats question data findings literature as testable only when evidence and ticket IDs are recorded.

### 42.5 Limits

Other changes, such as new staff, may also affect calls.

Section forty-two point five develops systems endpoints and hardware security with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-two point five, Marta Silva expects systems claims to carry owners and dates.

Section forty-two point five treats question data findings literature as testable only when evidence and ticket IDs are recorded.

For section forty-two point five, Fernhill Library Network will not accept systems work without a written trail.

### Method details

Calls are categorised by a librarian and an IT technician separately for a sample of 100 calls, agreeing on 91. Disagreements are discussed and the category rules clarified. Mateo compares three months before deployment with three months after, excluding the deployment month itself.

He reports counts by category with percentages and notes that the number of sessions was similar in both periods, which supports comparison.

### Ethics

Call records are anonymised before analysis; only categories and dates are used.

### Sharing

Results are shared with Fernhill and the studio.

### Link to design

The findings lead to the clearer notice and print-to-PDF guide, closing the loop between research and design.

### Future research

Mateo suggests studying whether a fixed image makes anomaly monitoring practical.

### Limitations

The study covers one network and six months.

### Validity

Two coders reduce bias in categories.

### Next steps

A longer study could track seasonal effects.

### Presentation

Mateo presents the study at the institute's student research day, with a poster showing call categories before and after.

### Data storage

Data are deleted after analysis.

### Worked example

The rise in saving-work calls leads to a clearer notice and a print-to-PDF guide.

> **Synthetic case.** Synthetic.

### Errors and limits

Before-and-after studies cannot exclude other causes.

### Exercises

- **EX124 — Question.** State the research question. *Rubric:* 3 = does nightly restore reduce help-desk calls; 2 = partial; 1 = none; 0 = none.
- **EX125 — Findings.** What changed in calls? *Rubric:* 3 = broken PCs halved; saving work rose; 2 = partial; 1 = none; 0 = none.
- **EX126 — Forrest link.** How does Forrest et al. (1996) relate? *Rubric:* 3 = fixed image makes normal easier to define; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small research questions from practice improve designs.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a public-service organisation; (2) follow its governance; (3) deliver under supervision.

### 43.1 Placement

Mateo spends a term at Fernhill supporting deployment to all branches.

Section forty-three point one develops industry or public-service practice with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-three point one, Marta Silva expects industry claims to carry owners and dates.

Section forty-three point one treats placement governance supervision professional as testable only when evidence and ticket IDs are recorded.

For section forty-three point one, Fernhill Library Network will not accept industry work without a written trail.

### 43.2 Governance

Changes go through Fernhill's change board; data handling follows its privacy policy.

Section forty-three point two develops industry or public-service practice with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-three point two, Marta Silva expects industry claims to carry owners and dates.

Section forty-three point two treats placement governance supervision professional as testable only when evidence and ticket IDs are recorded.

For section forty-three point two, Fernhill Library Network will not accept industry work without a written trail.

### 43.3 Supervision

Marta supervises daily; Dr Novak reviews weekly.

Section forty-three point three develops industry or public-service practice with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-three point three, Marta Silva expects industry claims to carry owners and dates.

Section forty-three point three treats placement governance supervision professional as testable only when evidence and ticket IDs are recorded.

For section forty-three point three, Fernhill Library Network will not accept industry work without a written trail.

Section forty-three point three fails closed if industry evidence is missing rather than guessing.

### 43.4 Professional conduct

Mateo does not access patron accounts and works only on approved tasks.

Section forty-three point four develops industry or public-service practice with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-three point four, Marta Silva expects industry claims to carry owners and dates.

Section forty-three point four treats placement governance supervision professional as testable only when evidence and ticket IDs are recorded.

For section forty-three point four, Fernhill Library Network will not accept industry work without a written trail.

### 43.5 Delivery

All three branches move to the new design during the term.

Section forty-three point five develops industry or public-service practice with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-three point five, Marta Silva expects industry claims to carry owners and dates.

Section forty-three point five treats placement governance supervision professional as testable only when evidence and ticket IDs are recorded.

For section forty-three point five, Fernhill Library Network will not accept industry work without a written trail.

### Daily work

During the placement, Mateo's days include checking restore reports with the technician, preparing branch rollouts, answering librarians' questions and updating documentation. He keeps a daily log of tasks and lessons, which later feeds the dossier.

He learns how public-service constraints shape engineering: budgets are fixed, timing depends on community needs and every change must be explained to non-specialists.

### Rollout steps

Each branch rollout follows a checklist: notify staff, deploy after closing, run end-to-end tests, monitor for a week.

### Feedback

Marta's mid-term feedback asks for shorter emails to librarians, which he adopts.

### Boundaries

He never works alone on production systems.

### Reflection

Mateo reflects that the placement taught him to plan around people as much as technology.

### Evidence

Placement records join the dossier.

### Supervision value

Weekly reviews with Dr Novak help Mateo connect placement work to course concepts.

### Placement report

He writes a placement report for the institute.

### Skills gained

He gains skills in change management, stakeholder communication and working under supervision in a live service.

### Closing

Marta provides a written reference describing his work and conduct.

### Daily log

His log records each task and lesson.

### Worked example

A branch manager asks to delay rollout during a busy exam period. The change board agrees, and the branch goes last.

> **Synthetic case.** Synthetic.

### Errors and limits

Ignoring local timing can damage trust even if the change is good.

### Exercises

- **EX127 — Governance.** Which governance applied? *Rubric:* 3 = change board, privacy policy; 2 = partial; 1 = none; 0 = none.
- **EX128 — Conduct.** What did Mateo avoid? *Rubric:* 3 = patron accounts, unapproved tasks; 2 = partial; 1 = none; 0 = none.
- **EX129 — Delay.** How was the exam-period request handled? *Rubric:* 3 = branch went last; 2 = partial; 1 = none; 0 = none.

### Synthesis

Work within the organisation's governance and timing.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define the capstone scope; (2) plan work and risks; (3) set acceptance criteria.

### 44.1 Scope

The capstone delivers the full self-restoring hardened public PC service, documented and handed to Fernhill.

Section forty-four point one develops engineering capstone with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-four point one, Marta Silva expects engineering claims to carry owners and dates.

Section forty-four point one treats scope work plan risks as testable only when evidence and ticket IDs are recorded.

For section forty-four point one, Fernhill Library Network will not accept engineering work without a written trail.

### 44.2 Work plan

Remaining tasks: dashboard, firmware update process, final documentation.

Section forty-four point two develops engineering capstone with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-four point two, Marta Silva expects engineering claims to carry owners and dates.

Section forty-four point two treats scope work plan risks as testable only when evidence and ticket IDs are recorded.

For section forty-four point two, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-four point two fails closed if engineering evidence is missing rather than guessing.

### 44.3 Risks

Hardware delays, staff availability and vendor changes.

Section forty-four point three develops engineering capstone with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-four point three, Marta Silva expects engineering claims to carry owners and dates.

Section forty-four point three treats scope work plan risks as testable only when evidence and ticket IDs are recorded.

For section forty-four point three, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-four point three fails closed if engineering evidence is missing rather than guessing.

### 44.4 Acceptance criteria

All ten requirements passing; restore within window for 30 consecutive nights; documentation tested by a new technician.

Section forty-four point four develops engineering capstone with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-four point four, Marta Silva expects engineering claims to carry owners and dates.

Section forty-four point four treats scope work plan risks as testable only when evidence and ticket IDs are recorded.

For section forty-four point four, Fernhill Library Network will not accept engineering work without a written trail.

### 44.5 Approval

Marta and Dr Novak approve the plan.

Section forty-four point five develops engineering capstone with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-four point five, Marta Silva expects engineering claims to carry owners and dates.

Section forty-four point five treats scope work plan risks as testable only when evidence and ticket IDs are recorded.

For section forty-four point five, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-four point five fails closed if engineering evidence is missing rather than guessing.

### Risk responses

For hardware delays, he orders replacement disks early. For staff availability, tasks are scheduled around the technician's leave. For vendor changes, he subscribes to vendor notices. Each risk has an owner and a trigger for action.

The plan is a one-page table reviewed weekly with Dr Novak.

### Schedule

The capstone runs over two terms with milestones every four weeks.

### Quality

Each milestone includes tests against requirements.

### Communication

Monthly updates go to the board.

### Contingency

Two weeks of slack absorb delays.

### Stakeholder sign-off

Branch managers confirm the rollout schedule.

### Scope control

New requests go to a future list unless they affect requirements.

### Tracking

A simple board tracks tasks.

### Assumptions

The plan assumes hardware arrives on time and staff remain available.

### Approval record

Approvals are stored.

### Visibility

The plan is visible to all stakeholders.

### Reporting

Progress is reported monthly.

### Why criteria matter

Acceptance criteria tell everyone when the project is finished. Without them, work tends to grow without end. Mateo's criteria are measurable and agreed in advance, so acceptance is a check, not a negotiation.

### Plan updates

When the hardware delay happens, the plan is updated and stakeholders informed.

### Worked example

The firmware update process is the riskiest task; Mateo schedules it first so problems surface early.

> **Synthetic case.** Synthetic.

### Errors and limits

Leaving the riskiest task last risks failure at the end.

### Exercises

- **EX130 — Remaining tasks.** What tasks remained? *Rubric:* 3 = dashboard, firmware process, documentation; 2 = two; 1 = one; 0 = none.
- **EX131 — Criteria.** State the acceptance criteria. *Rubric:* 3 = 10 passing, 30 nights, docs tested; 2 = two; 1 = one; 0 = none.
- **EX132 — Ordering.** Why schedule firmware first? *Rubric:* 3 = riskiest; surface problems early; 2 = partial; 1 = none; 0 = none.

### Synthesis

Set clear acceptance criteria and tackle risks early.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) undergo independent review; (2) address findings; (3) improve the design.

### 45.1 Reviewer

An engineer from another council reviews the design and evidence.

Section forty-five point one develops independent design review with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-five point one, Marta Silva expects independent claims to carry owners and dates.

Section forty-five point one treats reviewer findings response recording as testable only when evidence and ticket IDs are recorded.

For section forty-five point one, Fernhill Library Network will not accept independent work without a written trail.

Section forty-five point one fails closed if independent evidence is missing rather than guessing.

### 45.2 Findings

Strong restore and layering; weaker monitoring of firmware versions; signing key storage needs improvement.

Section forty-five point two develops independent design review with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-five point two, Marta Silva expects independent claims to carry owners and dates.

Section forty-five point two treats reviewer findings response recording as testable only when evidence and ticket IDs are recorded.

For section forty-five point two, Fernhill Library Network will not accept independent work without a written trail.

### 45.3 Response

Firmware versions join the dashboard; signing keys move to a hardware security module service.

Section forty-five point three develops independent design review with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-five point three, Marta Silva expects independent claims to carry owners and dates.

Section forty-five point three treats reviewer findings response recording as testable only when evidence and ticket IDs are recorded.

For section forty-five point three, Fernhill Library Network will not accept independent work without a written trail.

### 45.4 Recording

Findings and responses are recorded.

Section forty-five point four develops independent design review with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-five point four, Marta Silva expects independent claims to carry owners and dates.

Section forty-five point four treats reviewer findings response recording as testable only when evidence and ticket IDs are recorded.

For section forty-five point four, Fernhill Library Network will not accept independent work without a written trail.

Section forty-five point four fails closed if independent evidence is missing rather than guessing.

### 45.5 Value

External eyes see what the team overlooked.

Section forty-five point five develops independent design review with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-five point five, Marta Silva expects independent claims to carry owners and dates.

Section forty-five point five treats reviewer findings response recording as testable only when evidence and ticket IDs are recorded.

For section forty-five point five, Fernhill Library Network will not accept independent work without a written trail.

Section forty-five point five fails closed if independent evidence is missing rather than guessing.

### Preparing for review

Mateo sends the reviewer the requirements, design records, test evidence and measurements a week in advance, with a short guide to where things are. Preparation lets the reviewer spend time on judgement rather than searching. The review meeting lasts two hours, with findings written up the next day.

He treats every finding as useful, even ones he disagrees with, and records reasons when he decides not to act.

### Follow-up

Actions from the review are tracked to completion and shown to the reviewer.

### Firmware dashboard

The dashboard now shows firmware versions by model.

### Key ceremony

Key moves follow a documented procedure with two people present.

### Reviewer independence

The reviewer had no part in the design, so findings are independent.

### Thanks

Mateo thanks the reviewer.

### Outcome

The design is improved in two areas.

### Records

Findings are stored.

### Timing

Actions finish within a month.

### Value of outside views

The reviewer's experience with another council's kiosks brought practical knowledge Mateo lacked, such as how often firmware settings reset after hardware repairs.

### Recording disagreements

One suggestion, adding full attestation, is deferred with reasons: it needs new tooling.

### Final review status

All review actions are closed and confirmed with the reviewer within a month.

### Worked example

The reviewer asks how the team would notice a firmware downgrade. Mateo adds a check comparing firmware versions to the approved list nightly.

> **Synthetic case.** Synthetic.

### Errors and limits

Reviews only help if findings are acted on.

### Exercises

- **EX133 — Weak points.** What weaknesses did the review find? *Rubric:* 3 = firmware monitoring, key storage; 2 = partial; 1 = none; 0 = none.
- **EX134 — Key response.** How were signing keys improved? *Rubric:* 3 = HSM service; 2 = partial; 1 = none; 0 = none.
- **EX135 — Downgrade check.** How is a firmware downgrade noticed? *Rubric:* 3 = nightly version comparison; 2 = partial; 1 = none; 0 = none.

### Synthesis

Act on independent review findings.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) complete implementation; (2) meet acceptance criteria; (3) prepare handover.

### 46.1 Implementation

Dashboard, firmware process and documentation are completed.

Section forty-six point one develops engineering capstone ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-six point one, Marta Silva expects engineering claims to carry owners and dates.

Section forty-six point one treats implementation acceptance handover residual as testable only when evidence and ticket IDs are recorded.

For section forty-six point one, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-six point one fails closed if engineering evidence is missing rather than guessing.

### 46.2 Acceptance

Ten requirements pass; restore within window for 30 nights; a new technician uses the docs successfully.

Section forty-six point two develops engineering capstone ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-six point two, Marta Silva expects engineering claims to carry owners and dates.

Section forty-six point two treats implementation acceptance handover residual as testable only when evidence and ticket IDs are recorded.

For section forty-six point two, Fernhill Library Network will not accept engineering work without a written trail.

### 46.3 Handover

Mateo hands over to Marta and the technician with a walkthrough.

Section forty-six point three develops engineering capstone ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-six point three, Marta Silva expects engineering claims to carry owners and dates.

Section forty-six point three treats implementation acceptance handover residual as testable only when evidence and ticket IDs are recorded.

For section forty-six point three, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-six point three fails closed if engineering evidence is missing rather than guessing.

### 46.4 Residual risks

Older hardware and dependence on vendor firmware support remain.

Section forty-six point four develops engineering capstone ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-six point four, Marta Silva expects engineering claims to carry owners and dates.

Section forty-six point four treats implementation acceptance handover residual as testable only when evidence and ticket IDs are recorded.

For section forty-six point four, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-six point four fails closed if engineering evidence is missing rather than guessing.

### 46.5 Sign-off

Fernhill signs off acceptance.

Section forty-six point five develops engineering capstone ii with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-six point five, Marta Silva expects engineering claims to carry owners and dates.

Section forty-six point five treats implementation acceptance handover residual as testable only when evidence and ticket IDs are recorded.

For section forty-six point five, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-six point five fails closed if engineering evidence is missing rather than guessing.

### Handover pack

The handover pack includes the repository, runbooks, dashboard guide, contact list, risk register and a schedule of recurring tasks: daily restore checks, weekly allowlist review, monthly patching, quarterly recovery drills and annual baseline review. Marta and the technician walk through each item with Mateo and sign that they understand it.

Residual risks are listed with owners and review dates.

### Acceptance evidence

The 30-night restore record, requirement table and documentation test results are stored as acceptance evidence.

### Celebration

The team marks the milestone with the branch staff.

### Support

Mateo agrees to answer questions for a month.

### Post-handover check

A month later, Mateo checks with Marta: no unresolved issues remain.

### Lessons

He records lessons for future projects.

### Measures at handover

At handover, restore success is above 99% and no leftover files have been reported for a month.

### Ownership

Marta becomes the service owner.

### Final status

At acceptance, ten of ten requirements pass, restores meet the window for 30 nights and the new technician has used the runbooks successfully. Fernhill's board receives a short summary.

### Support period

During the month of support, Mateo answers three questions, all added to the runbooks.

### Sign-off record

Signed acceptance is stored.

### Worked example

On night 23, one branch's restores run late due to a power cut; the team checks the criteria, which allow documented external events, so the run continues.

> **Synthetic case.** Synthetic.

### Errors and limits

Acceptance criteria should define how to treat external events.

### Exercises

- **EX136 — Acceptance results.** Were the criteria met? *Rubric:* 3 = yes: 10 pass, 30 nights, docs; 2 = partial; 1 = none; 0 = none.
- **EX137 — Residual risks.** Name the residual risks. *Rubric:* 3 = older hardware, vendor firmware; 2 = partial; 1 = none; 0 = none.
- **EX138 — Power cut.** How was the power cut treated? *Rubric:* 3 = documented external event; 2 = partial; 1 = none; 0 = none.

### Synthesis

Meet criteria and hand over with residual risks stated.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a full failure and recovery trial; (2) measure recovery; (3) learn lessons.

### 47.1 Trial

With Fernhill's agreement, a branch simulates a bad image release after closing time.

Section forty-seven point one develops failure and recovery trial with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-seven point one, Marta Silva expects failure claims to carry owners and dates.

Section forty-seven point one treats trial detection recovery lessons as testable only when evidence and ticket IDs are recorded.

For section forty-seven point one, Fernhill Library Network will not accept failure work without a written trail.

### 47.2 Detection

Restore digests fail; the five-failure alert fires within minutes.

Section forty-seven point two develops failure and recovery trial with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-seven point two, Marta Silva expects failure claims to carry owners and dates.

Section forty-seven point two treats trial detection recovery lessons as testable only when evidence and ticket IDs are recorded.

For section forty-seven point two, Fernhill Library Network will not accept failure work without a written trail.

Section forty-seven point two fails closed if failure evidence is missing rather than guessing.

### 47.3 Recovery

Rollback to the previous image completes for the branch in 40 minutes.

Section forty-seven point three develops failure and recovery trial with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-seven point three, Marta Silva expects failure claims to carry owners and dates.

Section forty-seven point three treats trial detection recovery lessons as testable only when evidence and ticket IDs are recorded.

For section forty-seven point three, Fernhill Library Network will not accept failure work without a written trail.

### 47.4 Lessons

The runbook lacked a step for confirming printer mappings after rollback.

Section forty-seven point four develops failure and recovery trial with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-seven point four, Marta Silva expects failure claims to carry owners and dates.

Section forty-seven point four treats trial detection recovery lessons as testable only when evidence and ticket IDs are recorded.

For section forty-seven point four, Fernhill Library Network will not accept failure work without a written trail.

### 47.5 Improvement

The step is added and tested.

Section forty-seven point five develops failure and recovery trial with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-seven point five, Marta Silva expects failure claims to carry owners and dates.

Section forty-seven point five treats trial detection recovery lessons as testable only when evidence and ticket IDs are recorded.

For section forty-seven point five, Fernhill Library Network will not accept failure work without a written trail.

Section forty-seven point five fails closed if failure evidence is missing rather than guessing.

### Trial safety

The trial is planned with clear limits: one branch, after closing, lab-signed test image, with rollback ready and Marta present. A stop condition is defined: if rollback fails for any PC, the technician restores it manually from the local copy. Patrons are not affected.

The plan is approved by Fernhill's change board.

### Measurements

The team records detection time, rollback time and any manual steps needed.

### Debrief

A debrief the next day lists what worked and what to improve.

### Repeat

The trial will be repeated yearly.

### Communication

Branch staff are told the next morning that a trial took place and that PCs were ready as usual.

### Evidence

Trial records join the dossier.

### Comparison

Results match the design's expectations except the printer step.

### Confidence

The trial increases confidence in rollback.

### Approval

The change board accepts the results.

### Why trials matter

A trial tests people and procedures as well as technology. The runbook gap would not have appeared in a technical test alone; it needed someone following the steps under realistic conditions.

### Improvement tracking

The added printer step is tested on the next release and works as expected.

### Recovery check

Every branch PC is ready by morning.

### Worked example

Marta notes that without the trial, the printer issue would have appeared on a busy morning.

> **Synthetic case.** Synthetic.

### Errors and limits

Trials outside opening hours protect patrons while testing realistically.

### Exercises

- **EX139 — Detection.** How was the bad image detected? *Rubric:* 3 = digest failures, five-failure alert; 2 = partial; 1 = none; 0 = none.
- **EX140 — Recovery time.** How long did branch rollback take? *Rubric:* 3 = 40 minutes; 2 = partial; 1 = none; 0 = none.
- **EX141 — Lesson.** What did the trial reveal? *Rubric:* 3 = missing printer step; 2 = partial; 1 = none; 0 = none.

### Synthesis

Rehearse failure to find gaps before real incidents.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble evidence for assessment; (2) link claims to evidence; (3) keep privacy.

### 48.1 Contents

Requirements, design records, test results, measurements, reviews, trials and operations data.

Section forty-eight point one develops evidence dossier with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-eight point one, Marta Silva expects evidence claims to carry owners and dates.

Section forty-eight point one treats contents linking privacy integrity as testable only when evidence and ticket IDs are recorded.

For section forty-eight point one, Fernhill Library Network will not accept evidence work without a written trail.

Section forty-eight point one fails closed if evidence evidence is missing rather than guessing.

### 48.2 Linking

Each claim in the thesis links to dossier items.

Section forty-eight point two develops evidence dossier with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-eight point two, Marta Silva expects evidence claims to carry owners and dates.

Section forty-eight point two treats contents linking privacy integrity as testable only when evidence and ticket IDs are recorded.

For section forty-eight point two, Fernhill Library Network will not accept evidence work without a written trail.

Section forty-eight point two fails closed if evidence evidence is missing rather than guessing.

### 48.3 Privacy

No patron data appear; operational data are aggregated.

Section forty-eight point three develops evidence dossier with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-eight point three, Marta Silva expects evidence claims to carry owners and dates.

Section forty-eight point three treats contents linking privacy integrity as testable only when evidence and ticket IDs are recorded.

For section forty-eight point three, Fernhill Library Network will not accept evidence work without a written trail.

Section forty-eight point three fails closed if evidence evidence is missing rather than guessing.

### 48.4 Integrity

Files carry digests so assessors can confirm they are unchanged.

Section forty-eight point four develops evidence dossier with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-eight point four, Marta Silva expects evidence claims to carry owners and dates.

Section forty-eight point four treats contents linking privacy integrity as testable only when evidence and ticket IDs are recorded.

For section forty-eight point four, Fernhill Library Network will not accept evidence work without a written trail.

Section forty-eight point four fails closed if evidence evidence is missing rather than guessing.

### 48.5 Review

Dr Novak checks a sample of links.

Section forty-eight point five develops evidence dossier with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-eight point five, Marta Silva expects evidence claims to carry owners and dates.

Section forty-eight point five treats contents linking privacy integrity as testable only when evidence and ticket IDs are recorded.

For section forty-eight point five, Fernhill Library Network will not accept evidence work without a written trail.

Section forty-eight point five fails closed if evidence evidence is missing rather than guessing.

### Organising the dossier

The dossier is organised by requirement and by chapter of the thesis. An index lists each item with a short description, date and digest. Assessors can enter through a claim in the thesis or through a requirement. Mateo tests the index by asking a classmate to find five items; all are found within minutes.

Large files such as logs are summarised, with full versions available on request.

### Version control

The dossier is versioned, so later corrections are visible.

### Retention

Fernhill keeps a copy for its records.

### Access

Access is limited to assessors and Fernhill IT.

### Final check

Before submission, every link is tested.

### Archive

The dossier is archived with digests.

### Assessor guide

A one-page guide explains how to navigate it.

### Completeness

Every requirement has at least one evidence item.

### Readability

Summaries use plain language.

### Updates

Late evidence is added with dates.

### Structure example

For requirement R4, the dossier links the requirement record, the restore control specification, the lab output from chapter 28, the timing data from chapter 29, the 30-night acceptance record and the trial report.

### Assessor feedback

Assessors note the dossier is easy to navigate and complete.

### Digests

Each item carries a digest so assessors can confirm it has not changed since submission.

### Worked example

An assessor picks the availability claim and follows links to the lab output and failure records in under five minutes.

> **Synthetic case.** Synthetic.

### Errors and limits

Claims without evidence weaken the thesis.

### Exercises

- **EX142 — Contents.** List four dossier items. *Rubric:* 3 = requirements, designs, tests, measurements, reviews, trials, ops; 2 = four; 1 = two; 0 = none.
- **EX143 — Privacy.** How is privacy protected? *Rubric:* 3 = no patron data, aggregated; 2 = partial; 1 = none; 0 = none.
- **EX144 — Integrity.** How can assessors confirm files are unchanged? *Rubric:* 3 = digests; 2 = partial; 1 = none; 0 = none.

### Synthesis

A linked dossier makes claims checkable.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write the engineering thesis; (2) synthesise design, evidence and lessons; (3) state limitations.

### 49.1 Structure

Problem, requirements, design, implementation, verification, validation, operations, lessons.

Section forty-nine point one develops engineering thesis with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-nine point one, Marta Silva expects engineering claims to carry owners and dates.

Section forty-nine point one treats structure key results lessons as testable only when evidence and ticket IDs are recorded.

For section forty-nine point one, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-nine point one fails closed if engineering evidence is missing rather than guessing.

### 49.2 Key results

Exposure reduced from about 294 to 21 PC-days per fortnight (estimate); availability 0.9999; help-desk breakdown calls halved.

Section forty-nine point two develops engineering thesis with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-nine point two, Marta Silva expects engineering claims to carry owners and dates.

Section forty-nine point two treats structure key results lessons as testable only when evidence and ticket IDs are recorded.

For section forty-nine point two, Fernhill Library Network will not accept engineering work without a written trail.

### 49.3 Lessons

Audit before enforce; test restore scope; design recovery for the design.

Section forty-nine point three develops engineering thesis with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-nine point three, Marta Silva expects engineering claims to carry owners and dates.

Section forty-nine point three treats structure key results lessons as testable only when evidence and ticket IDs are recorded.

For section forty-nine point three, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-nine point three fails closed if engineering evidence is missing rather than guessing.

### 49.4 Limitations

One organisation; synthetic-structure figures; older hardware.

Section forty-nine point four develops engineering thesis with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-nine point four, Marta Silva expects engineering claims to carry owners and dates.

Section forty-nine point four treats structure key results lessons as testable only when evidence and ticket IDs are recorded.

For section forty-nine point four, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-nine point four fails closed if engineering evidence is missing rather than guessing.

### 49.5 Contribution

A tested, documented design for public PC services others can adapt.

Section forty-nine point five develops engineering thesis with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section forty-nine point five, Marta Silva expects engineering claims to carry owners and dates.

Section forty-nine point five treats structure key results lessons as testable only when evidence and ticket IDs are recorded.

For section forty-nine point five, Fernhill Library Network will not accept engineering work without a written trail.

Section forty-nine point five fails closed if engineering evidence is missing rather than guessing.

### Writing process

Mateo writes the thesis chapter by chapter, starting with methods and results while details are fresh, then the introduction and discussion. Dr Novak reviews each chapter. Figures are generated by scripts so they can be re-created if data change.

He keeps a list of claims and checks each against the dossier before submission.

### Discussion

The discussion compares results with expectations: restore and availability performed as planned; help-desk calls about saving work rose, which was not anticipated.

### Future work

Thin clients, attestation and longer studies are proposed.

### Acknowledgements

He thanks Fernhill staff and Dr Novak.

### Final review

Dr Novak signs off the thesis for submission.

### Formatting

Tables and figures follow the institute's style.

### Word count

It stays within the limit.

### Claims check

Every claim is checked.

### Accessibility

The thesis follows accessible formatting.

### Submission

It is submitted on time.

### Abstract

A short abstract states problem, method and results.

### Key message

The thesis's key message is that a simple, tested reset design, built with users, can greatly reduce privacy and integrity problems on public computers.

### Peer reading

Two classmates read drafts and flag unclear passages, which Mateo rewrites.

### Structure note

Each chapter begins with a short summary and ends with links to evidence.

### Worked example

Dr Novak asks Mateo to separate estimates from measurements. He labels each figure accordingly.

> **Synthetic case.** Synthetic.

### Errors and limits

Mixing estimates and measurements misleads readers.

### Exercises

- **EX145 — Structure.** Give the thesis structure. *Rubric:* 3 = problem to lessons sequence; 2 = partial; 1 = none; 0 = none.
- **EX146 — Results.** State two key results. *Rubric:* 3 = exposure estimate, availability, calls halved; 2 = two; 1 = one; 0 = none.
- **EX147 — Labelling.** How were figures labelled? *Rubric:* 3 = estimate vs measurement; 2 = partial; 1 = none; 0 = none.

### Synthesis

Synthesise honestly, separating estimates from measurements.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend the thesis; (2) answer questions; (3) reflect on professional growth.

### 50.1 Defense

Mateo presents in thirty minutes and answers questions.

Section fifty point one develops final defense with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifty point one, Marta Silva expects final claims to carry owners and dates.

Section fifty point one treats defense questions answers reflection as testable only when evidence and ticket IDs are recorded.

For section fifty point one, Fernhill Library Network will not accept final work without a written trail.

Section fifty point one fails closed if final evidence is missing rather than guessing.

### 50.2 Questions

Examiners ask about privacy, accessibility and long-term costs.

Section fifty point two develops final defense with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifty point two, Marta Silva expects final claims to carry owners and dates.

Section fifty point two treats defense questions answers reflection as testable only when evidence and ticket IDs are recorded.

For section fifty point two, Fernhill Library Network will not accept final work without a written trail.

Section fifty point two fails closed if final evidence is missing rather than guessing.

### 50.3 Answers

Logs hold no content; accessibility tools were protected by audit-first; costs are mainly staff time, which fell.

Section fifty point three develops final defense with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifty point three, Marta Silva expects final claims to carry owners and dates.

Section fifty point three treats defense questions answers reflection as testable only when evidence and ticket IDs are recorded.

For section fifty point three, Fernhill Library Network will not accept final work without a written trail.

### 50.4 Reflection

Mateo learned that users shape security designs as much as threats do.

Section fifty point four develops final defense with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifty point four, Marta Silva expects final claims to carry owners and dates.

Section fifty point four treats defense questions answers reflection as testable only when evidence and ticket IDs are recorded.

For section fifty point four, Fernhill Library Network will not accept final work without a written trail.

Section fifty point four fails closed if final evidence is missing rather than guessing.

### 50.5 Next

Fernhill hires him part-time to maintain the service.

Section fifty point five develops final defense with a Fernhill Library Network note Mateo Rossi can demo offline.

Under section fifty point five, Marta Silva expects final claims to carry owners and dates.

Section fifty point five treats defense questions answers reflection as testable only when evidence and ticket IDs are recorded.

For section fifty point five, Fernhill Library Network will not accept final work without a written trail.

Section fifty point five fails closed if final evidence is missing rather than guessing.

### Preparing the defense

Mateo rehearses with classmates, who ask hard questions. He prepares short answers with evidence for privacy, accessibility, costs, firmware risk and generalisation. He also prepares to admit limits: one organisation, older hardware and estimates mixed with measurements, clearly labelled.

Rehearsal helps him keep answers short.

### Examiners' view

Examiners praise the link between requirements and evidence, the care for accessibility and privacy, and the honest labelling of estimates.

### Course review

The course moved from mathematics and physics through programming, systems, security, requirements, design, implementation, verification, operations and research to a thesis and defense, all anchored in one public-service project.

### Continuing

Mateo plans to follow vendor firmware notices, benchmark updates and research on endpoint integrity.

### Boundaries

All testing used lab PCs and synthetic data or agreed trials outside opening hours.

### Thanks

Mateo thanks everyone who helped.

### Outcome

Mateo passes with minor corrections.

### Final reflection

He notes that patient, careful testing mattered more than clever technology.

### Advice to future students

Mateo advises future students to start conversations with users early, test assumptions with data and label estimates honestly.

### Legacy

The service continues to run at Fernhill using the documented design and runbooks.

### Feedback

Examiners recommend the thesis to future students.

### Worked example

An examiner asks what he would change. He says he would involve librarians from the first week.

> **Synthetic case.** Synthetic.

### Errors and limits

Reflection should name specific changes.

### Exercises

- **EX148 — Examiner topics.** Which topics did examiners raise? *Rubric:* 3 = privacy, accessibility, costs; 2 = two; 1 = one; 0 = none.
- **EX149 — Accessibility answer.** How was accessibility protected? *Rubric:* 3 = audit-first allowlist; 2 = partial; 1 = none; 0 = none.
- **EX150 — Change.** What would Mateo change? *Rubric:* 3 = involve librarians from week one; 2 = partial; 1 = none; 0 = none.

### Synthesis

Defend with evidence and reflect specifically.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Mateo Rossi, Dr Hana Novak, Marta Silva, Ardmore Institute of Technology, Fernhill Library Network and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Reset itself every night to a known, hardened state.

**EX002.** About three per day, roughly linearly.

**EX003.** A saw-tooth that never exceeds one day's worth of cases.

**EX004.** Software executed but not on the allowed list.

**EX005.** 1,024.

**EX006.** Public PCs and staff laptops share one network segment.

**EX007.** Deletion usually removes only the index, not the data.

**EX008.** Repeated DRAM row access can flip bits in neighbouring rows.

**EX009.** Users can attach devices, reboot or open firmware menus.

**EX010.** Because 300 PCs need repeatable daily checks.

**EX011.** One synthetic PC meeting all requirements and one failing exactly two.

**EX012.** Minutes were stored as text.

**EX013.** Marta, branch managers and the library board.

**EX014.** Options, the choice and the reasons.

**EX015.** "This computer resets overnight; save your work to your own storage or email."

**EX016.** Total exposure in PC-days.

**EX017.** About 294 PC-days manual, about 21 with nightly restore.

**EX018.** Steady arrival of cases and full removal at each reset.

**EX019.** 1.2.

**EX020.** 0.700, 0.120 and 0.008.

**EX021.** Its probability is under 1% when healthy, suggesting a shared cause.

**EX022.** Firmware, then bootloader, then operating system.

**EX023.** Key storage and boot measurements.

**EX024.** TPM 2.0 and Secure Boot supported but no firmware passwords.

**EX025.** The digest changes.

**EX026.** Report it as a finding.

**EX027.** By changing one synthetic file and confirming exactly one mismatch.

**EX028.** System events, not browsing content.

**EX029.** Some patrons rely on screen readers and magnifiers.

**EX030.** He refused and proposed logging only installation attempts and restore results.

**EX031.** Internet, printing and the management server.

**EX032.** Authentication and encryption.

**EX033.** Threats arriving through allowed traffic such as web downloads.

**EX034.** They cannot change system files or install system-wide software.

**EX035.** Remove or disable unnecessary services.

**EX036.** PCs reset to it nightly, so updates must be in the image.

**EX037.** Asset tag, branch, model and firmware version.

**EX038.** They stay unique when hostnames change.

**EX039.** One year.

**EX040.** Every change with author and reason.

**EX041.** R3: USB storage devices are blocked on public PCs.

**EX042.** To limit the impact of a bad image.

**EX043.** Patron data not left behind, only approved software, PCs ready at opening.

**EX044.** Standard users, USB blocked by default, one simple image.

**EX045.** Inventory, secure configuration and data recovery.

**EX046.** Patron personal devices and the internet.

**EX047.** The golden image.

**EX048.** Test, inspection and analysis.

**EX049.** Measure, compare, act.

**EX050.** Problems grow before correction.

**EX051.** Alerts staff to repair failed restores before opening.

**EX052.** Firmware Secure Boot; OS standard users; app allowlist; data restore; network segmentation; monitoring logs.

**EX053.** SP 800-193 and SP 800-147.

**EX054.** It corrects failures of other layers.

**EX055.** Separate named accounts with multi-factor authentication.

**EX056.** Data exposure if a PC or disk is stolen.

**EX057.** The PC refused it and logged an error.

**EX058.** Reuse hardware, no disruption to opening hours, accessibility tools must work.

**EX059.** No patron data beyond one day; only approved software; ready at opening; less manual effort.

**EX060.** Automation reduces manual work and makes security consistent.

**EX061.** R1 Secure Boot and R2 firmware password.

**EX062.** R5 application control and R3 USB storage blocked.

**EX063.** The reader must be available without staff help.

**EX064.** Firmware verifies bootloader, which verifies kernel, then initial file system and policy.

**EX065.** One of five components, the kiosk policy, differed.

**EX066.** The PC was offline during the update.

**EX067.** Unauthorised software (16), personal files (15), USB malware (12).

**EX068.** Its impact is severe (5).

**EX069.** R3.

**EX070.** Firmware password not set; application control in audit mode.

**EX071.** CIS Benchmarks, Microsoft baselines and DISA STIGs.

**EX072.** To avoid blocking needed tools like accessibility readers.

**EX073.** How patrons save work and what happens when the server is down.

**EX074.** PCs restore from a local protected copy.

**EX075.** Recorded as an option to evaluate.

**EX076.** Full nightly reimage, patron-area restore with signed updates, thin clients.

**EX077.** Security, restore time, network load, cost and accessibility.

**EX078.** B with a weekly full reimage.

**EX079.** At 22:00, then digest verification and reporting.

**EX080.** The PC shows out of service, alerts staff and opens no session.

**EX081.** Boot integrity.

**EX082.** The browser configuration and a saved CV.

**EX083.** Zero.

**EX084.** Files outside the restore scope survived.

**EX085.** Central 6.3, Eastgate 9.2, Millbrook 5.3 minutes.

**EX086.** All 21.

**EX087.** Older disks and a congested network link.

**EX088.** By inserting a synthetic USB storage device and confirming it is blocked.

**EX089.** Pass, fail or untested.

**EX090.** A firewall rule blocked logging.

**EX091.** 23: game_setup 6, toolbar_installer 3, accessibility_reader 14.

**EX092.** By publisher signature.

**EX093.** Blocking patrons who rely on the reader.

**EX094.** 756 and 21 PC-hours.

**EX095.** 0.9965 and 0.9999.

**EX096.** About 5,143 hours.

**EX097.** Staged release and rollback to the previous signed image.

**EX098.** Up to a week.

**EX099.** The rollback key was held only by Marta.

**EX100.** Session booking, printing and the catalogue.

**EX101.** The printer mapping was stored in the patron area.

**EX102.** Rules use publisher signatures.

**EX103.** About an hour a week.

**EX104.** Through a request form reviewed weekly.

**EX105.** The USB malware scenario scores 12; email and cloud saving are offered.

**EX106.** Staggered by branch.

**EX107.** 40% now, about 48% after adding 60 PCs.

**EX108.** Eastgate's network link.

**EX109.** Checks the restore report and repairs failed PCs.

**EX110.** Lab, then one branch, then all.

**EX111.** Two failures, repaired by 08:30.

**EX112.** 8 pass, 1 fail, 1 untested.

**EX113.** R7 remote logging failed; R9 restore alert untested.

**EX114.** Fewer complaints and no leftover files in a month.

**EX115.** Image definitions, scripts, runbooks and decision records.

**EX116.** Two people can do every task, and documentation is tested.

**EX117.** Annually.

**EX118.** Ten minutes.

**EX119.** Three days.

**EX120.** Recovery requires a USB stick, now stored at each branch.

**EX121.** Median from 9.2 to about 6 minutes.

**EX122.** About two thirds.

**EX123.** A missed changed boot file.

**EX124.** Whether nightly restore reduces help-desk calls about public PCs.

**EX125.** Broken-PC calls halved; saving-work calls rose slightly.

**EX126.** A fixed image makes normal behaviour easier to define.

**EX127.** Fernhill's change board and privacy policy.

**EX128.** Accessing patron accounts or unapproved tasks.

**EX129.** The branch was scheduled last.

**EX130.** Dashboard, firmware update process and documentation.

**EX131.** All requirements passing, 30 nights within window, documentation tested.

**EX132.** It is riskiest, so problems surface early.

**EX133.** Firmware version monitoring and signing key storage.

**EX134.** Moved to a hardware security module service.

**EX135.** A nightly comparison with the approved version list.

**EX136.** Yes: requirements, 30 nights and documentation test.

**EX137.** Older hardware and vendor firmware support dependence.

**EX138.** As a documented external event.

**EX139.** Digest failures triggered the five-failure alert.

**EX140.** 40 minutes.

**EX141.** A missing printer-mapping check.

**EX142.** Requirements, design records, tests, measurements, reviews, trials, operations data.

**EX143.** No patron data; operational data aggregated.

**EX144.** By file digests.

**EX145.** Problem, requirements, design, implementation, verification, validation, operations, lessons.

**EX146.** Exposure 294→21 PC-days (estimate), availability 0.9999, breakdown calls halved.

**EX147.** As estimates or measurements.

**EX148.** Privacy, accessibility and long-term costs.

**EX149.** By the audit-first allowlist approach.

**EX150.** Involve librarians from the first week.

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
