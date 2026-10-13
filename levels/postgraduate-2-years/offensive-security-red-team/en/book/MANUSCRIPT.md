# Authorized Offensive Security and Red Team: A Postgraduate Specialist's Book

- Language: English (`en`); postgraduate course, two years; approximately 600 hours of planned study.
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: experienced specialists leading organization-scale authorized testing choices.
- Relation to neighbouring books: the [bachelor's book](../../../../bachelors-4-years/offensive-security-red-team/en/book/MANUSCRIPT.md) builds foundations and a capstone; the [master's book](../../../../masters-2-years/offensive-security-red-team/en/book/MANUSCRIPT.md) emphasises research design. **This book emphasises specialist judgement, threat-led literacy and assurance leadership.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. **No authority to test real market infrastructures.** All organisations, people and numbers are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–6 cover decisions, practice, evidence, ethics, programme design and evaluation; 7–12 cover integration, difficult cases, leadership, critique, applied project and transfer. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, five exercises scored 0–3, a synthesis and a **Continue studying** block. Labs in Chapters 6, 9 and 10 read local data only.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Meridian Clearing House (MCH)** — clearing services, ordinary web tests, biennial threat-led style exercises, SWIFT-adjacent exclusions | Organisation studied throughout | Invented |
| **Amira Hassan** | Specialist leading authorized testing judgement at MCH | Invented |

### Core sources

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) structure decisions under uncertainty for authorized testing programmes; (2) separate risk acceptance from wishful thinking; (3) use decision records that examiners can follow; (4) refuse decisions that lack an owner.

### 1.1 Decision objects

At Meridian Clearing House, Amira Hassan treats each major testing choice as an object with options, evidence, uncertainties, recommendation and owner. "We should red team more" is not a decision object until options and trade-offs are written.

### 1.2 Uncertainty types

She distinguishes aleatory uncertainty (noisy detection rates) from epistemic uncertainty (unknown whether a conduit exists). Wilson-style intervals help the first; architecture workshops help the second. Mixing them produces false precision.

### 1.3 Acceptance vs deferral

Accepting residual risk requires a named acceptor, expiry and compensating control. Deferring a test because "next year is better" without a date is neither acceptance nor management — it is drift.

### 1.4 Examiner readability

Decision records answer: what was chosen, what was rejected, what evidence counted, what remains unknown. Amira rejects records that read like slogans.

### 1.5 Authority

Only roles listed in the governance charter may accept payment-adjacent residual risk. Amira escalates rather than inventing authority.

### 1.6 Practice

Weekly decision clinic: one real (synthetic) choice, twenty minutes, written record before leaving the room.

### 1.7 1.7 Narrative

Amira keeps DEC records in a folder that internal audit sampled last year without finding undated deferrals. The sample letter is pinned above her monitor. When a VP asks for a quick yes on expanding scope into participant networks, she opens a blank decision object on the projector and fills options aloud until the VP either commits ownership or withdraws. The ritual feels slow and prevents silent scope inflation across clearing participants. Three deputies have now authored DEC records audit accepted unchanged.

### Worked example (synthetic MCH)

Amira's record DEC-14 chooses quarterly WSTG-style web tests plus a biennial threat-led exercise; rejects annual threat-led for capacity reasons; lists SWIFT-adjacent systems as out of ordinary scope with CISO as acceptor of that exclusion.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX001 — Decision object fields.** List five fields of a decision object. *Rubric:* 3 = five of options, evidence, uncertainties, recommendation, owner, rejects; 2 = three; 1 = one; 0 = none.
- **EX002 — Aleatory vs epistemic.** Give one example of each at MCH. *Rubric:* 3 = both correct types; 2 = one; 1 = swapped; 0 = none.
- **EX003 — Bad deferral.** Why is "test next year" without a date a problem? *Rubric:* 3 = drift / neither accept nor manage; 2 = partial; 1 = fine; 0 = none.
- **EX004 — Authority.** Who may accept payment-adjacent residual risk? *Rubric:* 3 = roles in governance charter / CISO-level; 2 = partial; 1 = any engineer; 0 = none.
- **EX005 — DEC-14 rejects.** What does DEC-14 reject and why? *Rubric:* 3 = annual threat-led for capacity; 2 = partial; 1 = all testing; 0 = none.

### Synthesis

Decisions are owned objects with uncertainties named; slogans and undated deferrals do not count.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Current practice in authorized offensive security

### Learning outcomes

You will (1) map current practice frameworks; (2) position TIBER-EU and CBEST among lighter tests; (3) critique vendor claims; (4) keep MCH's catalogue honest.

### 2.1 Practice landscape

Organisations mix vulnerability management, periodic web application tests following OWASP WSTG themes, purple-team drills and occasional threat-led exercises under TIBER-EU or CBEST-like rules. Names are not interchangeable.

### 2.2 Threat-led specifics

TIBER-EU and CBEST emphasise intelligence-led scenarios, white-team control and learning for detection and response — not finding count maximisation. Amira cites their public guides when executives say "just pentest everything".

### 2.3 SP 800-115 and PTES

Still the backbone for planning assessment types and engagement stages. Threat-led programmes sit on top of, not instead of, scoping discipline.

### 2.4 Vendor critique

Vendors who promise "full red team in a week" without intel, white team or detection goals are selling a scan with theatre. Amira's RFP questions ask for white-team design and learning objectives.

### 2.5 MCH catalogue

A living catalogue maps each activity to what it can and cannot claim. Honesty here prevents insurance and board misstatements.

### 2.6 Currency

Amira reviews the catalogue twice a year against new framework editions.

### 2.7 2.7 Narrative

Catalogue reviews include a red-team vendor as guest critic once a year. Amira asks them to attack the cannot-claim lines. If they can honestly say a quarterly web test proves SWIFT safety, the line is too weak. Last year's guest failed to break the lines; she still tightened one adjective. Currency reviews also hunt retired vendor slogans lingering in old board packs and redline them in the archive index.

### 2.8 2.8 Bit

Archive redlines of old packs are linked from the catalogue changelog; forgetting history is how swagger returns.

### 2.9 2.9 Bit2

Archive redlines of old packs are linked from the catalogue changelog; forgetting history is how swagger returns. Linking each redline to the changelog entry also shows reviewers which claim was softened and why.

### Worked example (synthetic MCH)

Amira rewrites a board slide from "we are CBEST compliant" to "we completed a CBEST-inspired exercise in 2025; ordinary quarterly tests exclude SWIFT-adjacent systems per catalogue".

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX006 — Not interchangeable.** Why not call every test a red team? *Rubric:* 3 = different depth/intel/detection goals; 2 = partial; 1 = same; 0 = none.
- **EX007 — Threat-led emphasis.** Name two emphases of TIBER-EU/CBEST-style tests. *Rubric:* 3 = intel-led scenarios and detection/response learning (white team); 2 = one; 1 = finding volume; 0 = none.
- **EX008 — RFP question.** Give one RFP question that weeds out theatre. *Rubric:* 3 = asks white-team/learning objectives/intel; 2 = partial; 1 = cheapest price only; 0 = none.
- **EX009 — Cannot-claim.** What must a catalogue state besides what tests do? *Rubric:* 3 = what they cannot claim; 2 = partial; 1 = logos; 0 = none.
- **EX010 — Slide rewrite.** What was wrong with "we are CBEST compliant"? *Rubric:* 3 = overclaim / imprecise; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Current practice is a catalogue of honestly named activities, not a single buzzword.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Specialist evidence

### Learning outcomes

You will (1) define specialist-grade evidence; (2) handle privileged clearing data; (3) design evidence that survives challenge; (4) refuse theatre screenshots.

### 3.1 Specialist grade

Evidence must be reproducible under the ROE, minimised, hashed, time-zoned and tied to a decision. "Looks bad in a tool" is not specialist grade.

### 3.2 Privileged data

Clearing messages and participant identifiers are highly sensitive. Amira prefers synthetic message templates even in staging when possible.

### 3.3 Challenge survival

Legal or white-team challenge asks: could another specialist reproduce this observation without your laptop folklore? If not, rewrite.

### 3.4 Theatre screenshots

Dark-themed dashboards without hashes, timestamps or scope context are rejected from the evidence vault.

### 3.5 Chain of custody

For threat-led exercises, custody logs are as important as technical artefacts.

### 3.6 Platform

FindingsDesk fields enforce hash and owner before a finding may enter board packs.

### 3.7 3.7 Narrative

Challenge drills pair two specialists: one presents evidence, the other has ten minutes to find a missing hash, timezone or ROE clause. Amira scores the challenger for catching real gaps and the presenter for calm repair. Vault rejection rates dropped afterward. Custody drills include a simulated laptop seizure asking whether hashes still prove out; a past fail funded HSM work for vault keys.

### 3.8 3.8 Bit

HSM funding used the seizure-drill fail as exhibit A in the budget memo; boring drills buy real controls.

### 3.9 3.9 Bit2

HSM funding used the seizure-drill fail as exhibit A in the budget memo; boring drills buy real controls. Treating a partial result as a fail is what made the drill credible evidence in that memo.

### 3.10 3.p9

Seizure-drill scores are pass/fail; partial hash recovery is a fail.

### 3.11 3.q10

Seizure-drill scores are pass/fail; partial hash recovery is a fail. A recovered fragment of a hash still proves the key material left the device, so the pass/fail rule has no middle grade.

### Worked example (synthetic MCH)

Amira rejects a vendor slide of a red dashboard; accepts a packet with request ids, hashes, UTC offsets and the ROE clause that allowed the check.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX011 — Four traits.** List four specialist-grade evidence traits. *Rubric:* 3 = four of reproducible, minimised, hashed, time-zoned, tied to decision; 2 = three; 1 = one; 0 = none.
- **EX012 — Synthetic preference.** Why prefer synthetic clearing templates? *Rubric:* 3 = sensitivity of real clearing data; 2 = partial; 1 = laziness; 0 = none.
- **EX013 — Challenge question.** What question tests challenge survival? *Rubric:* 3 = could another specialist reproduce without folklore; 2 = partial; 1 = is it red; 0 = none.
- **EX014 — Theatre reject.** Why reject a dark dashboard screenshot alone? *Rubric:* 3 = no hash/time/scope context; 2 = partial; 1 = aesthetics; 0 = none.
- **EX015 — Vault gate.** What does FindingsDesk require before board packs? *Rubric:* 3 = hash and owner (and related fields); 2 = one; 1 = colour; 0 = none.

### Synthesis

Specialist evidence survives challenge; theatre does not enter the vault.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) weigh systemic risk to clearing; (2) handle conflicts of interest; (3) resist optical pressure; (4) design ethical stop conditions for threat-led work.

### 4.1 Systemic risk

A careless test that disrupts settlement can harm many participants. Amira's risk lens is systemic, not only MCH-local.

### 4.2 Conflicts

Personal investments, prior employers and vendor friendships are logged. Recusal is normal, not career-limiting.

### 4.3 Optical pressure

Earnings dates and conference demos never justify burying findings. Management responses may sit beside findings; deletion may not.

### 4.4 Threat-led stops

White-team stop authority is written before scenarios start. Amira refuses exercises where nobody can stop the red team in minutes.

### 4.5 Dual-use

Publishing clearing-specific exploit paths is out of scope for this curriculum and for MCH public talks.

### 4.6 Care

Ethics includes sleep, hours caps and no heroics near settlement windows.

### 4.7 4.7 Narrative

Systemic-risk tabletop uses a simulated settlement delay of fifteen minutes. White-team students must stop a scenario mid-play when the delay appears. Amira fails any student who continues for just one more objective. Hours caps near settlement are enforced by calendar locks on scenario slots so heroics cannot be scheduled even by her.

### 4.8 4.8 Bit

Calendar locks display "ethics charter" as the rejection reason when someone tries to book over settlement peak.

### 4.9 4.9 Bit2

Calendar locks display "ethics charter" as the rejection reason when someone tries to book over settlement peak. Showing the charter as the reason tells the requester that the block is a policy decision, not a scheduling accident.

### 4.10 4.p9

Calendar lock rejection emails CC ethics charter maintainers automatically.

### 4.11 4.q10

Calendar lock rejection emails CC ethics charter maintainers automatically. Copying the maintainers means repeated attempts to book over settlement peak become visible to the people who own the charter.

### Worked example (synthetic MCH)

Amira cancels a proposed scenario that lacked a white-team kill switch two days before a settlement peak, citing systemic risk and the ethics charter.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX016 — Systemic lens.** Why is clearing risk different from a single bank website? *Rubric:* 3 = many participants / settlement impact; 2 = partial; 1 = same; 0 = none.
- **EX017 — Recusal.** Give one valid recusal trigger. *Rubric:* 3 = investment/prior employer/vendor friendship; 2 = partial; 1 = dislike; 0 = none.
- **EX018 — Bury vs response.** What may sit beside a finding under pressure? *Rubric:* 3 = management response; not deletion; 2 = partial; 1 = deletion; 0 = none.
- **EX019 — Kill switch.** What must exist before threat-led scenarios start? *Rubric:* 3 = white-team stop authority; 2 = partial; 1 = nothing; 0 = none.
- **EX020 — Settlement peak.** Why cancel near settlement peak without kill switch? *Rubric:* 3 = systemic risk + ethics; 2 = partial; 1 = fear; 0 = none.

### Synthesis

Ethics at clearing scale includes systemic harm, recusal, refusal to bury and real stop authority.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Design alternatives for assessment programmes

### Learning outcomes

You will (1) generate programme alternatives; (2) score them on learning, risk, cost and capacity; (3) recommend a portfolio; (4) document non-goals.

### 5.1 Alternatives

A: quarterly web only. B: annual threat-led only. C: quarterly web + biennial threat-led. D: continuous automated scan theatre.

### 5.2 Scoring

Amira scores detection learning, operational risk, cost, staff capacity and examiner fit. D scores high on noise and low on learning.

### 5.3 Portfolio

C usually wins for MCH-like organisations. A alone under-trains detection; B alone misses regressions.

### 5.4 Non-goals

No claim of SWIFT coverage from ordinary web tests; no public exploit demos; no unpaid overtime as a capacity plan.

### 5.5 Sensitivity

She re-scores if capacity halves; the recommendation should still be executable.

### 5.6 Output

A two-page alternatives memo with a calendar graphic.

### 5.7 5.7 Narrative

Sensitivity analysis in the alternatives memo halves capacity and also doubles vendor cost. If recommendation C collapses under both shocks, it was never robust. Current C survives halved capacity by slipping threat-led to every third year — still written and owned. Non-goals are read at the start of every workshop so brainstorming cannot quietly reintroduce theatre option D.

### 5.8 5.8 Bit

Every-third-year threat-led still has a named white-team lead pencilled two years out; pencils beat wishes.

### 5.9 5.9 Bit2

Every-third-year threat-led still has a named white-team lead pencilled two years out; pencils beat wishes. Naming the lead two years out gives the white team time to arrange cover before the threat-led exercise is due.

### 5.10 5.10 Story

Amira's calendar graphic uses shaded cells for threat-led preparation months, not only execution week, so executives see the true staff load. Finance once funded only the execution week and was surprised by intel lead time; the shaded cells stopped that surprise. She reprints the calendar after every DEC that changes cadence and stores the PDF hash beside DEC-14.

### Worked example (synthetic MCH)

Amira's memo selects C, shows a two-year calendar, and lists D as rejected for false assurance.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX021 — Why not D.** Why reject continuous scan theatre? *Rubric:* 3 = noise without learning / false assurance; 2 = partial; 1 = it is best; 0 = none.
- **EX022 — Why C.** Why does C usually win? *Rubric:* 3 = regressions + periodic threat-led learning; 2 = partial; 1 = cheapest; 0 = none.
- **EX023 — Non-goal example.** Give one non-goal for MCH's programme. *Rubric:* 3 = no SWIFT claim from web tests / no public exploits / no overtime capacity; 2 = partial; 1 = none; 0 = none.
- **EX024 — Sensitivity.** What capacity shock should the memo test? *Rubric:* 3 = capacity halves / similar shock; 2 = partial; 1 = none; 0 = none.
- **EX025 — Calendar.** What artefact helps executives approve C? *Rubric:* 3 = two-year calendar graphic; 2 = partial; 1 = jargon; 0 = none.

### Synthesis

Programme design is a scored portfolio with non-goals, not a single purchased logo.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Controlled evaluation

### Learning outcomes

You will (1) design evaluations of scenarios and controls; (2) use scoring that balances learning and risk; (3) pre-register; (4) report gaps without doom.

### 6.1 Evaluation targets

Scenario choice, control coverage, detection rules and programme outcomes each need different designs.

### 6.2 Scoring lab

lab_scenario ranks synthetic scenarios with score = 2×learning − risk so high-learning, manageable-risk options surface.

```python
"""Lab 6: score synthetic TIBER-style scenario options by detection learning vs ops risk (1-3)."""
opts = [("A","Stolen VPN + SWIFT-adjacent pivot",3,3),("B","Public web defacement only",1,1),
        ("C","Supply-chain library in batch app",3,2),("D","Branch Wi-Fi rogue AP",2,2)]
for i,t,learn,risk in sorted(opts, key=lambda x:(-(x[2]*2-x[3]), x[0])):
    print(f"{i} score={learn*2-risk:+d} learn={learn} risk={risk} {t}")
```

Run with `python3 lab_scenario.py`. Verified output:

```text
C score=+4 learn=3 risk=2 Supply-chain library in batch app
A score=+3 learn=3 risk=3 Stolen VPN + SWIFT-adjacent pivot
D score=+2 learn=2 risk=2 Branch Wi-Fi rogue AP
B score=+1 learn=1 risk=1 Public web defacement only
```

### 6.3 Pre-registration

Metrics and thresholds are tagged in git before results.

### 6.4 GAP language

"T1190 0/2 GAP" schedules engineering; it does not claim permanent blindness.

### 6.5 Independence

White team or a peer runs the scoring on the same inputs.

### 6.6 Ethics

Scenarios that need live participant impact are rejected at design time.

### 6.7 6.7 Narrative

White-team feasibility for scenario C includes a library inventory owner who can freeze deploys. Without that owner, Amira demotes C despite its lab score. Independent scoring means she leaves the room while a peer applies lab_scenario to the same inputs; disagreements become design notes filed beside the lab output.

### 6.8 6.8 Bit

Design notes from scoring disagreements are tagged FEASIBILITY so they appear in the next scenario workshop automatically.

### 6.9 6.9 Bit2

Design notes from scoring disagreements are tagged FEASIBILITY so they appear in the next scenario workshop automatically. Tagging disagreements this way turns a scoring dispute into an input for designing the next scenario.

### 6.10 6.10 Story

Feasibility demotion of scenario C is communicated to the board as strength, not indecision. Amira's slide title was "We refused a high-scoring scenario we could not stop". The board applauded. Lab scores without stop owners are now labelled provisional in every packet that leaves her desk.

### 6.11 6.p10

Provisional labels on scores are bright orange in the PDF export.

### 6.12 6.q11

Provisional labels on scores are bright orange in the PDF export. The orange label keeps a provisional score from being quoted as final once the PDF leaves the team.

### Worked example (synthetic MCH)

lab_scenario ranks supply-chain library scenario highest among the four; Amira still subjects it to white-team feasibility before funding.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX026 — Top scenario.** Which option ranks first in the lab? *Rubric:* 3 = C supply-chain; 2 = A; 1 = B; 0 = none.
- **EX027 — Score formula.** What is the lab's score formula? *Rubric:* 3 = 2×learn − risk; 2 = learn×risk; 1 = risk only; 0 = none.
- **EX028 — Why not auto-fund.** Why not fund C only from the lab ranking? *Rubric:* 3 = need white-team feasibility / broader criteria; 2 = partial; 1 = always auto-fund; 0 = none.
- **EX029 — GAP tone.** How should a small-n GAP be reported? *Rubric:* 3 = schedules engineering; not permanent doom; 2 = partial; 1 = we are blind forever; 0 = none.
- **EX030 — Pre-register.** Where do metrics live before results? *Rubric:* 3 = dated git tag / registration; 2 = partial; 1 = after results; 0 = none.

### Synthesis

Controlled evaluation ranks learning against risk and refuses doom language for small samples.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Organizational integration

### Learning outcomes

You will (1) integrate testing with SOC, risk, legal and participants; (2) design information flows; (3) avoid shadow programmes; (4) measure integration health.

### 7.1 Integration map

Amira draws who receives what: SOC gets ATT&CK tags and timelines; risk gets ranked residuals; legal gets disclosure-relevant facts; participants get only what contracts allow.

### 7.2 Shadow programmes

Business units hiring boutique scanners without ROE create shadow risk. Integration means one catalogue and one authorization path.

### 7.3 Cadence

Quarterly sync with SOC on noise budgets; monthly with risk on acceptance expiries; ad hoc with legal on disclosure.

### 7.4 Health metrics

Percent of findings with owners, percent of tests in catalogue, median time from finding to detection ticket.

### 7.5 Participant care

Clearing participants are customers of trust. Comms templates are pre-approved.

### 7.6 Failure mode

Integration fails when testing is a heroic annual event with no backlog into BAU engineering.

### 7.7 7.7 Narrative

Shadow-programme amnesty week invites business units to declare boutique scans. Declared scans enter the catalogue or stop. Undeclared scans found later become audit findings against the unit lead. Participant comms templates are versioned; Amira rejects ad-lib emails during test-related incidents involving participants.

### 7.8 7.8 Bit

Amnesty week metrics — declared, catalogued, stopped — go to the board risk committee in one slide.

### 7.9 7.9 Bit2

Amnesty week metrics — declared, catalogued, stopped — go to the board risk committee in one slide. Keeping the three counts on one slide lets the committee see whether declarations led to tools actually being stopped.

### 7.10 7.10 Story

Amnesty week produced twelve declarations; eight catalogued, four stopped. The slide to risk committee used those three numbers only. Amira refuses amnesty narratives without counts. Units that stayed silent and were later found scanning received findings with owners named in the minutes.

### 7.11 7.p10

Amnesty counts are archived with the committee minute hash.

### 7.12 7.q11

Amnesty counts are archived with the committee minute hash. Tying the counts to the minute hash means a later reader can check that the reported figures were the ones the committee saw.

### Worked example (synthetic MCH)

Amira's integration scorecard shows 100% catalogue coverage but slow detection-ticket time; she funds a PulseMap-to-backlog bridge.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX031 — Recipients.** Name three recipient groups and what they get. *Rubric:* 3 = three correct pairs; 2 = two; 1 = one; 0 = none.
- **EX032 — Shadow risk.** What makes a boutique scan a shadow programme? *Rubric:* 3 = outside ROE/catalogue/authorization path; 2 = partial; 1 = using vendors; 0 = none.
- **EX033 — Health metric.** Give two integration health metrics. *Rubric:* 3 = two from chapter; 2 = one; 1 = vanity finding count; 0 = none.
- **EX034 — Heroic annual.** Why does a heroic annual-only event fail integration? *Rubric:* 3 = no BAU backlog / no continuous improvement; 2 = partial; 1 = it is ideal; 0 = none.
- **EX035 — Bridge.** What bridge does Amira fund in the worked example? *Rubric:* 3 = PulseMap-to-backlog; 2 = partial; 1 = more scans; 0 = none.

### Synthesis

Integration is one catalogue, named recipients and BAU backlog — not annual heroics.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Difficult cases

### Learning outcomes

You will (1) handle ambiguous scope; (2) handle insider-sensitive findings; (3) handle vendor refusal; (4) keep records under stress.

### 8.1 Ambiguous scope

When a hostname might be participant-owned, Amira pauses and seeks written clarification. Guessing is not a specialist skill.

### 8.2 Insider-sensitive

Findings that imply staff misconduct go through HR paths with minimal necessary detail. Testing is not a witch hunt.

### 8.3 Vendor refusal

Vendors who refuse reasonable authorized testing of their components trigger risk acceptance or replacement decisions — not silent hope.

### 8.4 Record under stress

Difficult cases generate more pressure emails. All go to the CISO alias with factual headers.

### 8.5 Time

Difficult cases get explicit time boxes so they cannot starve ordinary catalogue work forever.

### 8.6 Support

Amira pairs juniors with a senior on any case that involves HR or participants.

### 8.7 8.7 Narrative

Insider-sensitive playbooks include a one-page HR liaison script that Amira rehearses so staff do not overshare in tickets. Time boxes for difficult cases appear on the same board as product findings so infinite investigations are visible debt. Juniors always pair with a senior when HR or participants are involved.

### 8.8 8.8 Bit

HR script versioning follows the same change control as ROE templates; freelanced empathy is not a control.

### 8.9 8.9 Bit2

HR script versioning follows the same change control as ROE templates; freelanced empathy is not a control. Putting the HR script under ROE-style change control means a well-meant wording change cannot reach an employee unreviewed.

### 8.10 8.p9

HR script changes require HR and Amira countersignatures the same day.

### 8.11 8.q10

HR script changes require HR and Amira countersignatures the same day. Same-day countersignature prevents a script edited in the morning from being used in an afternoon interview without both owners' approval.

### Worked example (synthetic MCH)

A maybe-participant host appears mid-window; Amira stops related methods in 4 minutes, emails the white team, and resumes only on written scope update.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX036 — Pause rule.** What does Amira do on ambiguous ownership? *Rubric:* 3 = pause; written clarification; 2 = pause; 1 = guess; 0 = none.
- **EX037 — HR path.** How are staff-misconduct-implying findings handled? *Rubric:* 3 = HR path; minimal detail; 2 = partial; 1 = public channel; 0 = none.
- **EX038 — Vendor refuse.** What decisions follow vendor refusal to allow testing? *Rubric:* 3 = risk acceptance or replacement; 2 = one; 1 = ignore; 0 = none.
- **EX039 — Pressure email.** Where do pressure emails go? *Rubric:* 3 = CISO alias with factual header; 2 = partial; 1 = delete; 0 = none.
- **EX040 — Stop time.** How fast did Amira stop in the worked example? *Rubric:* 3 = about 4 minutes / minutes; 2 = same day; 1 = next week; 0 = none.

### Synthesis

Difficult cases pause for writing, protect people and leave records.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Leadership and assurance

### Learning outcomes

You will (1) write assurance statements that survive audit; (2) lead without theatre; (3) coach refusal skills; (4) validate statements with a linter lab.

### 9.1 Assurance language

Time-bounded, scope-bounded, method-bounded. Forbidden: fully secure, guaranteed, hack-proof, 100% coverage.

```python
"""Lab 9: validate a synthetic assurance statement against a forbidden-phrase list."""
forbidden = ["fully secure", "guaranteed", "hack-proof", "100% coverage"]
text = "Quarterly web tests and a 2025 threat-led exercise provide time-bounded assurance; SWIFT remains excluded from ordinary tests."
hits = [f for f in forbidden if f in text.lower()]
print("CLEAN" if not hits else "FORBIDDEN: " + ", ".join(hits))
print("chars", len(text))
```

Run with `python3 lab_assurance.py`. Verified output:

```text
CLEAN
chars 126
```

### 9.2 Lab

lab_assurance checks a synthetic statement against forbidden phrases.

### 9.3 Leadership behaviours

Amira praises early stops, funded negative results and clean catalogues more than dramatic finds.

### 9.4 Coaching refusal

Role-play pressure monthly. Score calm and firm separately.

### 9.5 Board education

Teach directors what ordinary tests cannot claim about SWIFT-adjacent systems.

### 9.6 Succession

Document decisions so a successor can continue without folklore.

### 9.7 9.7 Narrative

Forbidden-phrase linter runs on every board pack export. A vendor paste once introduced hack-proof; CI blocked the pack. Succession folders include three CLEAN statements and three FORBIDDEN counterexamples with explanations so deputies learn by contrast.

### 9.8 9.8 Bit

Vendor warning letters enclose the forbidden list as Appendix A; some vendors update their marketing decks.

### 9.9 9.9 Bit2

Vendor warning letters enclose the forbidden list as Appendix A; some vendors update their marketing decks. Attaching the list makes the warning specific: the vendor sees exactly which claims the team will not accept.

### 9.10 9.10 Story

When CI blocked hack-proof, Amira forwarded the raw CI log to the vendor without scolding. The vendor's next deck used time-bounded assurance. She keeps that before-and-after pair for leadership seminars on quiet influence and refuses to tell the story as a victory over the vendor.

### 9.11 9.p10

Before-and-after vendor decks are stored as evidence of influence, not of mockery.

### 9.12 9.q11

Before-and-after vendor decks are stored as evidence of influence, not of mockery. Keeping both versions shows auditors that the warning changed vendor claims, which is the point of sending it.

### Worked example (synthetic MCH)

lab_assurance prints CLEAN for Amira's statement; a draft with "fully secure" would fail.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX041 — Forbidden list.** Name three forbidden assurance phrases. *Rubric:* 3 = three of fully secure, guaranteed, hack-proof, 100% coverage; 2 = two; 1 = one; 0 = none.
- **EX042 — Lab result.** What does the lab print for the sample statement? *Rubric:* 3 = CLEAN; 2 = forbidden; 1 = error; 0 = none.
- **EX043 — Praise targets.** Name two behaviours Amira praises. *Rubric:* 3 = two of early stops, negative results, clean catalogues; 2 = one; 1 = drama only; 0 = none.
- **EX044 — Board lesson.** What must directors learn about SWIFT-adjacent systems? *Rubric:* 3 = ordinary tests do not cover them; 2 = partial; 1 = fully covered; 0 = none.
- **EX045 — If forbidden present.** What would lab print if "fully secure" appeared? *Rubric:* 3 = FORBIDDEN: fully secure; 2 = CLEAN; 1 = nothing; 0 = none.

### Synthesis

Leadership is honest assurance language, coached refusal and praise for restraint.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) critique abstracts on purple-team and threat-led methods; (2) demand n and limits; (3) connect papers to MCH decisions; (4) reject citation theatre.

### 10.1 Reading purpose

Amira reads to improve MCH decisions, not to decorate reports with names.

```python
"""Lab 10: checklist score for a synthetic paper abstract on purple-team methods."""
abs_ = {"question":True,"method":True,"n":False,"limits":True,"ethics":True}
for k,v in abs_.items():
    print(f"{k:8} {'ok' if v else 'MISSING'}")
print("pass" if all(abs_.values()) else "revise")
```

Run with `python3 lab_critique.py`. Verified output:

```text
question ok
method   ok
n        MISSING
limits   ok
ethics   ok
revise
```

### 10.2 Abstract checklist

Question, method, n, limits, ethics — lab_critique scores a synthetic abstract.

### 10.3 Citation theatre

Footnotes to unread papers are unethical in assurance contexts. She opens sources.

### 10.4 Transfer

A paper without operationalisable actions gets a "watch" tag, not a programme change.

### 10.5 Limits empathy

Generous reading still requires limits sections; missing limits fail the checklist.

### 10.6 Seminar

Monthly paper club with the critique checklist on the wall.

### 10.7 10.7 Narrative

Paper club fails any presenter who cannot state n from memory after reading. Amira is kind about nerves and unkind about missing limits. Transfer of critique skill includes letting a junior run club while she stays silent for the first thirty minutes.

### 10.8 10.8 Bit

Silent-thirty metric tracks how long Amira stays quiet; the goal is longer each quarter as juniors lead.

### 10.9 10.9 Bit2

Silent-thirty metric tracks how long Amira stays quiet; the goal is longer each quarter as juniors lead. A rising silent-thirty number is evidence that juniors are running debriefs without waiting for Amira.

### 10.10 10.10 Story

Paper club's wall checklist is a printed lab_critique output. When someone skips n, Amira points at MISSING without speaking. Juniors now pre-check n before volunteering to present. She measures pre-check rates each term and publishes them without naming people.

### 10.11 10.p10

Pre-check rate posters use cohort letters, never names.

### 10.12 10.q11

Pre-check rate posters use cohort letters, never names. Cohort letters let teams compare pre-check rates without singling out any individual operator.

### Worked example (synthetic MCH)

lab_critique returns revise because n is MISSING; Amira sends the abstract back to the authoring team.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX046 — Missing field.** Which checklist field is MISSING in the lab? *Rubric:* 3 = n; 2 = ethics; 1 = question; 0 = none.
- **EX047 — Lab verdict.** What final word does the lab print? *Rubric:* 3 = revise; 2 = pass; 1 = CLEAN; 0 = none.
- **EX048 — Citation theatre.** Why is unread footnoting unethical in assurance? *Rubric:* 3 = misleads readers about evidence basis; 2 = partial; 1 = fine; 0 = none.
- **EX049 — Watch tag.** When does a paper get only a watch tag? *Rubric:* 3 = no operationalisable action; 2 = partial; 1 = always change programme; 0 = none.
- **EX050 — Checklist five.** List the five abstract checklist fields. *Rubric:* 3 = question, method, n, limits, ethics; 2 = four; 1 = two; 0 = none.

### Synthesis

Critique demands n, limits and ethics; unread citations are theatre.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) deliver a specialist project for MCH; (2) keep non-goals; (3) evaluate with pre-registration; (4) hand over to operations.

### 11.1 Project brief

Build a scenario-scoring sheet and assurance linter integrated with FindingsDesk fields; evaluate on synthetic past exercises.

### 11.2 Non-goals

No live participant scanning; no exploit modules; no LLM auto-bury of findings.

### 11.3 Pre-registration

Precision of forbidden-phrase catch; ranking correlation with white-team expert order on a frozen set.

### 11.4 Handover

Operators run the linter alone; Amira may not type.

### 11.5 Ethics cover

Synthetic-only declaration on page one.

### 11.6 Time box

Eight weeks with biweekly checkpoints.

### 11.7 11.7 Narrative

Checkpoint quizzes ask which non-goal you nearly violated this sprint; Amira answers first with her own near-miss about an LLM summary feature. Ethics cover sheets are mechanically checked for the word synthetic before project repos accept merges. Solo-run week forbids her typing.

### 11.8 11.8 Bit

Near-miss answers are stored anonymously when others share; Amira's own near-miss stays named to model candour.

### 11.9 11.9 Bit2

Near-miss answers are stored anonymously when others share; Amira's own near-miss stays named to model candour. Amira naming her own near-miss signals to juniors that admitting one carries no penalty.

### 11.10 11.10 Story

Solo-run week uses a freshly created operator account with empty shell history and a sealed envelope of ROE excerpts. If the operator phones Amira, the call is logged as a doc defect. Two calls in cohort one became README patches the same afternoon and a thank-you to the operator.

### 11.11 11.p10

Sealed envelopes use wax stamps for theatre that reminds people the ROE is special.

### 11.12 11.q11

Sealed envelopes use wax stamps for theatre that reminds people the ROE is special. The ceremony is deliberate: opening a sealed ROE envelope should feel different from opening routine paperwork.

### Worked example (synthetic MCH)

Amira's project catches 100% of planted forbidden phrases on the frozen set; operators complete solo runs on week seven; non-goals hold.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX051 — Non-goals.** Name two project non-goals. *Rubric:* 3 = two of no live scan, no exploits, no LLM auto-bury; 2 = one; 1 = none; 0 = none.
- **EX052 — Metric.** Give one pre-registered metric. *Rubric:* 3 = forbidden-phrase catch precision or ranking correlation; 2 = vague; 1 = vibes; 0 = none.
- **EX053 — Solo run.** Why must Amira not type during handover? *Rubric:* 3 = docs must suffice for operators; 2 = partial; 1 = she should type; 0 = none.
- **EX054 — Cover.** What declaration opens the project packet? *Rubric:* 3 = synthetic-only; 2 = partial; 1 = live OK; 0 = none.
- **EX055 — Week seven.** What happens in week seven in the worked example? *Rubric:* 3 = operator solo runs; 2 = partial; 1 = go live on participants; 0 = none.

### Synthesis

The applied project ships guarded tooling with solo-run proof and intact non-goals.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) assemble a specialist portfolio; (2) transfer programme ownership; (3) state remaining research questions; (4) restate dual-use limits.

### 12.1 Portfolio

Decision records, catalogue page, evidence standards, ethics charter excerpt, evaluation results, assurance examples, critique notes, project handover.

### 12.2 Transfer

Successor reads DEC-14 and the two-year calendar aloud; Amira answers questions but does not retain secret folklore.

### 12.3 Research questions

How to measure detection learning across biennial threat-led exercises without exhausting white-team capacity remains open.

### 12.4 Dual-use

Amira's final slide lists refusals: no public clearing exploit detail, no live demos against participants, no assurance without denominators.

### 12.5 Next course

AI security (158) is next in the curriculum path.

### 12.6 Care

Transfer includes introducing the successor to SOC and legal personally.

### 12.7 12.7 Narrative

Transfer day includes walking introductions to SOC and legal; email alone is not transfer. Open research questions get named watchers before she exits. The successor's first catalogue update posts under their name with Amira only CC'd — the visible handoff.

### 12.8 12.8 Bit

Watcher for the open research question receives a quarterly calendar invite with Amira optional — succession of curiosity.

### 12.9 12.9 Bit2

Watcher for the open research question receives a quarterly calendar invite with Amira optional — succession of curiosity. Leaving Amira optional on the invite tests whether the question survives without her steering it.

### 12.10 12.10 Story

Walking introductions include a five-minute shadow of the SOC stand-up so the successor hears noise-budget language in the wild. Amira schedules the shadow even when calendars resist. Transfer without SOC reality is incomplete and she will not sign the transfer form without it.

### 12.11 12.p10

Transfer form has a checkbox "SOC shadow completed" that blocks signature when empty.

### 12.12 12.q11

Transfer form has a checkbox "SOC shadow completed" that blocks signature when empty. Blocking signature until the SOC shadow is done makes the shadow a precondition rather than a recommendation.

### Worked example (synthetic MCH)

Amira's transfer day ends with the successor posting the first catalogue update under their own name; Amira is CC only.

> **Synthetic case — Meridian Clearing House (MCH).** The clearing organisation, Amira Hassan and all figures are invented for teaching.

### Errors and limits

Threat-led and clearing-system tests require specialised legal authorization. This book uses synthetic scenarios only and never supplies exploit code or live targeting advice for market infrastructures.

### Exercises

- **EX056 — Portfolio count.** List five portfolio artefacts. *Rubric:* 3 = five from list; 2 = three; 1 = one; 0 = none.
- **EX057 — Folklore.** What must not remain only in Amira's head? *Rubric:* 3 = decision rationale / programme rules; 2 = partial; 1 = everything secret; 0 = none.
- **EX058 — Open question.** State one remaining research question. *Rubric:* 3 = measuring detection learning vs white-team capacity; 2 = vague; 1 = none; 0 = none.
- **EX059 — Refusal list.** Name two final refusals. *Rubric:* 3 = two of no public exploits, no live participant demos, no assurance without denominators; 2 = one; 1 = none; 0 = none.
- **EX060 — Next course.** What is course 158? *Rubric:* 3 = AI security; 2 = AI; 1 = wrong; 0 = none.

### Synthesis

Transfer leaves writing, refusals and an open research question — not a personality cult.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Meridian Clearing House, Amira Hassan and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** Options, evidence, uncertainties, recommendation and owner (rejected options also).

**EX002.** Aleatory: varying detection rates across trials; epistemic: unknown whether a conduit to the clearing core exists.

**EX003.** It neither accepts residual risk nor schedules management; it is unmanaged drift.

**EX004.** Only roles listed in the governance charter (typically CISO-level), not inventing authority.

**EX005.** Annual threat-led exercises, for capacity reasons.

**EX006.** Because assessment types differ in depth, intelligence use and detection-learning goals.

**EX007.** Intelligence-led scenarios and learning for detection and response (with white-team control).

**EX008.** Describe your white-team design and detection-learning objectives for the engagement.

**EX009.** What each activity cannot claim.

**EX010.** It overclaims and blurs a one-time inspired exercise with ongoing ordinary-test exclusions.

**EX011.** Reproducible, minimised, hashed and time-zoned (tied to a decision also).

**EX012.** Real clearing messages and participant identifiers are highly sensitive.

**EX013.** Could another specialist reproduce this observation without laptop folklore?

**EX014.** It lacks hash, timestamp and scope context — theatre, not evidence.

**EX015.** Evidence hash and owner at minimum.

**EX016.** Disruption can affect many participants and settlement, not only one institution's website.

**EX017.** A personal investment, prior employer relationship or close vendor friendship affecting impartiality.

**EX018.** A management response may sit beside it; the finding may not be deleted.

**EX019.** Written white-team authority to stop the exercise in minutes.

**EX020.** Systemic settlement risk plus the ethics charter requiring a kill switch.

**EX021.** It creates noise and false assurance without detection learning.

**EX022.** It catches web regressions quarterly and still funds periodic threat-led learning.

**EX023.** No claim of SWIFT coverage from ordinary web tests.

**EX024.** A scenario where staff capacity halves (or similar).

**EX025.** A two-year calendar showing when each activity runs.

**EX026.** C — Supply-chain library in batch app.

**EX027.** score = 2×learning − risk.

**EX028.** Ranking informs; white-team feasibility and broader criteria still decide funding.

**EX029.** As a gap that schedules engineering work, not as permanent blindness.

**EX030.** In a dated git tag or equivalent registration before results.

**EX031.** SOC: ATT&CK tags/timelines; risk: ranked residuals; legal: disclosure-relevant facts (participants: contract-limited comms).

**EX032.** It runs outside the authorized catalogue and ROE path.

**EX033.** Percent of findings with owners and median time from finding to detection ticket (catalogue coverage also).

**EX034.** It leaves no backlog into business-as-usual engineering.

**EX035.** A PulseMap-to-detection-backlog bridge.

**EX036.** Pause and seek written clarification before continuing.

**EX037.** Through HR with only the minimum necessary detail.

**EX038.** Formal risk acceptance or replacement of the component.

**EX039.** To the CISO alias with a factual header.

**EX040.** Within minutes (about four) of noticing the ambiguity.

**EX041.** Fully secure, guaranteed and hack-proof (100% coverage also).

**EX042.** `CLEAN`

**EX043.** Early stops and funded negative results (clean catalogues also).

**EX044.** That ordinary tests do not cover SWIFT-adjacent systems.

**EX045.** `FORBIDDEN: fully secure`

**EX046.** `n`

**EX047.** `revise`

**EX048.** It misleads readers about the evidence basis of claims.

**EX049.** When it offers no operationalisable action for MCH.

**EX050.** Question, method, n, limits and ethics.

**EX051.** No live participant scanning and no exploit modules (no LLM auto-bury also).

**EX052.** Precision of forbidden-phrase detection (or ranking correlation with white-team order).

**EX053.** If operators need her hands, documentation failed.

**EX054.** A synthetic-only declaration.

**EX055.** Operators complete solo runs.

**EX056.** Decision records, catalogue page, evidence standards, ethics excerpt and evaluation results (others also).

**EX057.** Decision rationales and programme rules — they must be written.

**EX058.** How to measure detection learning across biennial threat-led exercises without exhausting white-team capacity.

**EX059.** No public clearing exploit detail and no live demos against participants.

**EX060.** AI security.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v3.1 Specification Document. <https://www.first.org/cvss/v3.1/specification-document>
- MITRE ATT&CK, including T1078 Valid Accounts. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
