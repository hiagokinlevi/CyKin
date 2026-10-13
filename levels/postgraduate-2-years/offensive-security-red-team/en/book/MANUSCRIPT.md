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

DEC-14 rejects annual threat-led work because white-team capacity cannot cover two full cycles without borrowing SOC analysts from BAU. The CISO accepts that capacity limit in writing, and Amira files the acceptance beside the options table so a later examiner sees the trade-off was owned, not implied.

Until those five fields are written, a slogan such as we should red team more is not a decision object, and examiners cannot see what was traded away. Amira opens a blank object on the projector whenever a VP asks for a quick yes, so ownership is forced into the open before scope expands.

### 1.2 Uncertainty types

She distinguishes aleatory uncertainty (noisy detection rates) from epistemic uncertainty (unknown whether a conduit exists). Wilson-style intervals help the first; architecture workshops help the second. Mixing them produces false precision.

For DEC-14 she marks detection-rate noise as aleatory and the unknown SWIFT-adjacent conduit as epistemic. The architecture workshop that follows has a date and a named lead; inventing a percentage for the conduit would have produced false precision the board would have treated as fact.

Her decision records label which uncertainties are which, so a later reader knows what more data could fix and what only design work can fix. Mixing noisy detection rates with unknown conduits is how board packs gain a single percentage that pretends certainty.

### 1.3 Acceptance vs deferral

Accepting residual risk requires a named acceptor, expiry and compensating control. Deferring a test because "next year is better" without a date is neither acceptance nor management — it is drift.

The SWIFT-adjacent exclusion names the CISO as acceptor, expires at the next catalogue review, and lists network isolation plus jump-host MFA as compensating controls. Amira will not file acceptance if any of those three fields is blank, and she will not treat an open-ended deferral as a substitute for them.

Saying next year without a date would leave the SWIFT-adjacent exclusion as drift. Examiners reading the record should see a deliberate choice with acceptor, expiry and compensating controls, not a postponed conversation dressed as management.

### 1.4 Examiner readability

Decision records answer: what was chosen, what was rejected, what evidence counted, what remains unknown. Amira rejects records that read like slogans.

A readable DEC-14 record states that quarterly WSTG-style web tests plus a biennial threat-led exercise were chosen, that annual threat-led was rejected for capacity, and that SWIFT-adjacent systems remain excluded. A director who missed the meeting can reconstruct the trade-off without calling Amira.

Slogans such as we take security seriously are deleted from drafts before they leave her desk. She writes so a successor can continue without asking her for folklore, and so a director who was not in the room can reconstruct capacity limits on annual threat-led work.

### 1.5 Authority

Only roles listed in the governance charter may accept payment-adjacent residual risk. Amira escalates rather than inventing authority.

Payment-adjacent residual risk sits with roles named in the governance charter: the CISO for ordinary exclusions, the board risk committee for programme-wide choices. When a product owner asks Amira to accept what she cannot, she escalates with the charter excerpt attached rather than inventing authority.

Invented authority collapses under examiner challenge, so she keeps the charter excerpt beside every acceptance record. Product owners who want her signature on what only the CISO may accept receive an escalation, not a quiet nod.

### 1.6 Practice

Weekly decision clinic: one real (synthetic) choice, twenty minutes, written record before leaving the room.

The weekly clinic takes one synthetic choice — for example, slipping the threat-led exercise by a quarter — and ends with options, evidence and owner written before anyone leaves. Amira logs the record the same day so the clinic cannot become an undocumented hallway chat.

Juniors present first in the clinic; she edits for clarity, not for softer conclusions. Twenty minutes is enough when the choice is real and synthetic, such as whether to slip a threat-led exercise, and the written record lands in the decision log the same day.

### 1.7 Narrative

Amira keeps DEC records in a folder that internal audit sampled last year without finding undated deferrals. The sample letter is pinned above her monitor. When a VP asks for a quick yes on expanding scope into participant networks, she opens a blank decision object on the projector and fills options aloud until the VP either commits ownership or withdraws. The ritual feels slow and prevents silent scope inflation across clearing participants. Three deputies have now authored DEC records audit accepted unchanged.

Internal audit sampled the DEC folder last year and found no undated deferrals; the sample letter stays pinned above her monitor. When a VP wants a quick yes on participant-network scope, she fills a blank decision object on the projector until ownership is accepted or the request is withdrawn.

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

Amira's catalogue names vulnerability management, WSTG-style web tests, purple-team drills and threat-led exercises as separate rows with separate claims. Calling all of them a red team is how boards hear SWIFT assurance that was never bought, so she corrects vocabulary in every planning meeting until the names stick.

Wrong names produce wrong expectations about detection learning and SWIFT-adjacent coverage. She corrects the vocabulary until vulnerability management, web tests, purple-team drills and threat-led exercises stay separate in every planning note.

### 2.2 Threat-led specifics

TIBER-EU and CBEST emphasise intelligence-led scenarios, white-team control and learning for detection and response — not finding count maximisation. Amira cites their public guides when executives say "just pentest everything".

When executives ask to just pentest everything, she opens the public TIBER-EU and CBEST guides and shows intelligence, white-team and detection-learning expectations. Her RFP language asks for those three, not for a finding-count target, so Meridian Clearing House does not buy a scan dressed as threat-led work.

A week of scanning is not a threat-led programme under those guides. Finding-count targets are scored as theatre in her RFP, and vendors who cannot describe white-team design leave the shortlist.

### 2.3 SP 800-115 and PTES

Still the backbone for planning assessment types and engagement stages. Threat-led programmes sit on top of, not instead of, scoping discipline.

Threat-led exercises still need NIST SP 800-115 and PTES scoping: written authorization, inclusions, exclusions and stop conditions. Sitting on that backbone is how Amira keeps SWIFT-adjacent systems out of ordinary tests while still running a biennial scenario under white-team control.

Skipping scoping because the exercise is special is how out-of-scope probes happen. Written authorization, clear inclusions and exclusions, and stop conditions remain mandatory even when the scenario is intelligence-led and biennial.

### 2.4 Vendor critique

Vendors who promise "full red team in a week" without intel, white team or detection goals are selling a scan with theatre. Amira's RFP questions ask for white-team design and learning objectives.

RFP scoring asks who acts as white team, what detection goals will be measured, and how intelligence shapes scenarios. Vendors who cannot answer are scored as scan-with-theatre; she has rejected a one-week full red team bid with no intel phase and recorded the reason in the catalogue.

The catalogue records each rejection reason so the next buyer sees the pattern of scan-with-theatre bids. White-team design, detection goals and intelligence shaping are the three answers that separate a real offer from a slogan.

### 2.5 MCH catalogue

A living catalogue maps each activity to what it can and cannot claim. Honesty here prevents insurance and board misstatements.

Ordinary quarterly web tests cannot claim SWIFT safety; a biennial threat-led exercise cannot claim continuous coverage of every web change. A catalogue row without a cannot-claim line is incomplete, and Amira blocks board-pack language that invents claims the row forbids.

Honesty here stops insurance questionnaires and board slides from overstating Meridian Clearing House's assurance. Amira treats a missing cannot-claim line as an incomplete row and will not let that row enter a pack.

### 2.6 Currency

Amira reviews the catalogue twice a year against new framework editions.

Twice-yearly reviews catch new ATT&CK, WSTG, TIBER-EU and CBEST editions and redline retired vendor slogans still sitting in old board packs. A catalogue that is never refreshed becomes a museum of last year's swagger, so she dates each review and files the redline index.

She dates each review and files the redline index so retired slogans cannot be pasted forward from old packs. Currency is a scheduled control, not a hope that someone will notice a stale claim.

### 2.7 Narrative

Catalogue reviews include a red-team vendor as guest critic once a year. Amira asks them to attack the cannot-claim lines. If they can honestly say a quarterly web test proves SWIFT safety, the line is too weak. Last year's guest failed to break the lines; she still tightened one adjective. Currency reviews also hunt retired vendor slogans lingering in old board packs and redline them in the archive index.

Once a year a red-team vendor attends as guest critic and attacks the cannot-claim lines. Last year's guest could not honestly say a quarterly web test proves SWIFT safety; Amira still tightened one adjective and invites a different vendor next year so the critique does not become captured.

### 2.8 Bit2

Archive redlines of old packs are linked from the catalogue changelog; forgetting history is how swagger returns. Linking each redline to the changelog entry also shows reviewers which claim was softened and why.

Archive redlines link to the catalogue changelog so reviewers see which claim was softened and why. The rewrite from we are CBEST compliant to a time-bounded CBEST-inspired exercise with SWIFT-adjacent exclusions is the worked example; both versions stay in the archive.

Linking each redline to the changelog entry also shows reviewers which claim was softened and why when a director asks about wording changes. Forgetting archive history is how swagger returns to board language.

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

Specialist-grade evidence can be reproduced under the ROE by another tester using hashes, timestamps and scope context from the vault. FindingsDesk blocks board-pack entry until hash and owner are present, so drama without those fields never reaches a committee slide.

Reproducibility is the grade; drama is not. Looks bad in a tool is rejected until another specialist can reproduce the observation under the ROE with hashes and timestamps from the vault.

### 3.2 Privileged data

Clearing messages and participant identifiers are highly sensitive. Amira prefers synthetic message templates even in staging when possible.

Clearing messages and participant identifiers stay out of ordinary evidence when synthetic templates can show the same class of issue. Amira prefers those templates even in staging and redacts anything that still looks too real before it enters the vault.

Sensitivity is not a reason to skip evidence; it is a reason to design safer evidence. Synthetic message templates that show the same class of issue keep real participant identifiers out of ordinary vault entries.

### 3.3 Challenge survival

Legal or white-team challenge asks: could another specialist reproduce this observation without your laptop folklore? If not, rewrite.

In challenge drills a second specialist has ten minutes to find a missing hash, timezone or ROE clause. If the observation cannot survive without laptop folklore, she rewrites it before vault entry; calm repair after a catch scores well, defensiveness does not.

The drill exists so legal or white-team challenge never meets an unreproducible claim for the first time. Ten minutes is enough to find a missing hash, timezone or ROE clause when the challenger is scored for catching real gaps.

### 3.4 Theatre screenshots

Dark-themed dashboards without hashes, timestamps or scope context are rejected from the evidence vault.

Dark dashboards without hashes, timestamps or scope context look impressive and prove nothing. The vault rejects them on sight; Amira asks first for command output, config excerpts and hashes so juniors learn polish is not evidence.

Theatre screenshots waste examiner time and train juniors to confuse polish with evidence. Boring artefacts — command output, config excerpts and hashes — enter the vault first; dark dashboards without context stay out.

Amira asks for the boring artefacts first and will not argue about colour themes until hashes and timestamps exist. A rejected theatre screenshot becomes a teaching example in the next challenge drill so the same polish mistake does not return.

### 3.5 Chain of custody

For threat-led exercises, custody logs are as important as technical artefacts.

For threat-led exercises, custody logs show who held which artefact, when it moved and who authorised the move. A missing custody line is treated as seriously as a missing hash, and the log is built during the exercise rather than reconstructed afterwards.

White-team and legal challenges often start with chain-of-custody questions, so the log is built during the exercise. Who held which artefact, when it moved and who authorised the move are written while memory is fresh.

### 3.6 Platform

FindingsDesk fields enforce hash and owner before a finding may enter board packs.

FindingsDesk will not let a finding into a board pack without hash and owner. Amira refuses manual overrides for late slides; colour and severity fields come after those two, never instead of them, even when a committee meeting is tomorrow.

The platform gate is how Meridian Clearing House keeps specialist standards when calendar pressure rises before a committee meeting. Manual overrides for late slides are refused even when colour and severity look ready.

### 3.7 Narrative

Challenge drills pair two specialists: one presents evidence, the other has ten minutes to find a missing hash, timezone or ROE clause. Amira scores the challenger for catching real gaps and the presenter for calm repair. Vault rejection rates dropped afterward. Custody drills include a simulated laptop seizure asking whether hashes still prove out; a past fail funded HSM work for vault keys.

After challenge drills began, vault rejection rates fell because presenters arrived with hashes filled. Custody drills include a seizure scenario where partial hash recovery still counts as fail; that fail later funded HSM work for vault keys.

### 3.8 Bit2

HSM funding used the seizure-drill fail as exhibit A in the budget memo; boring drills buy real controls. Treating a partial result as a fail is what made the drill credible evidence in that memo.

HSM funding used the seizure-drill fail as exhibit A in the budget memo. A recovered fragment still proved material left the device, so there was no middle grade; Amira keeps the pass-fail rule written beside the drill plan for later cohorts.

Treating a partial result as a fail made the drill credible evidence in the HSM budget memo. Boring drills buy real controls when the scoring rule stays written beside the plan for later cohorts.

### 3.9 3.q10

Seizure-drill scores are pass/fail; partial hash recovery is a fail. A recovered fragment of a hash still proves the key material left the device, so the pass/fail rule has no middle grade.

Seizure-drill scores are pass or fail; partial hash recovery is a fail with no middle grade. Softening the fail after the fact would have weakened the HSM case and trained operators to negotiate scores, so she writes the rule into the drill brief before the exercise starts.

Amira writes the pass-fail sentence into the drill brief before the exercise starts. Operators who want a middle grade after a fragment recovers learn that the rule does not bend for comfort.

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

A careless test that delays settlement can harm many participants beyond Meridian Clearing House. Before design sign-off she asks who else clears through the path and what a fifteen-minute pause would do; scenarios that need live participant impact are rejected at design time.

Systemic harm is why stop authority and calendar locks exist. Scenarios that need live participant impact never leave design review, because a fifteen-minute settlement pause can harm many participants beyond Meridian Clearing House.

### 4.2 Conflicts

Personal investments, prior employers and vendor friendships are logged. Recusal is normal, not career-limiting.

Personal investments, prior employers and vendor friendships go in the conflict register; Amira recuses when a decision touches them. Juniors see her leave a vendor scoring meeting when a former employer bids, which teaches the habit better than a policy page alone.

Recusal is normal at Meridian Clearing House and is not treated as a career limit. The conflict register holds personal investments, prior employers and vendor friendships before scoring meetings begin.

### 4.3 Optical pressure

Earnings dates and conference demos never justify burying findings. Management responses may sit beside findings; deletion may not.

Earnings dates and conference demos never justify burying findings. Management responses may sit beside findings in the board pack; deletion may not. Amira has refused drop requests before a demo week and records each refusal under the ethics charter.

Optical pressure is predictable; the ethics charter answers it before the email arrives. Management responses may sit beside findings; deletion of findings before a demo week is recorded as a refused request.

### 4.4 Threat-led stops

White-team stop authority is written before scenarios start. Amira refuses exercises where nobody can stop the red team in minutes.

White-team stop authority is written before scenarios start, with names and phone numbers that work in minutes. A simulated settlement delay of fifteen minutes is enough reason to stop mid-play; students who continue for one more objective fail the ethics tabletop.

Amira refuses exercises where nobody can stop the red team in minutes. Names and phone numbers that work under stress are written before scenarios start, and the ethics tabletop fails anyone who continues after the simulated delay.

### 4.5 Dual-use

Publishing clearing-specific exploit paths is out of scope for this curriculum and for MCH public talks.

Publishing clearing-specific exploit paths is out of scope for this curriculum and for MCH public talks. Amira's final slide lists that refusal beside no live demos against participants; dual-use discipline is part of specialist identity, not an optional appendix for a conference slot.

Clearing-specific exploit paths stay out of public talks and out of this curriculum. Dual-use discipline is part of specialist identity; a conference slot that wants live demos against participants is refused on the final slide.

### 4.6 Care

Ethics includes sleep, hours caps and no heroics near settlement windows.

Ethics includes sleep, hours caps and no heroics near settlement windows. Calendar locks block scenario bookings over settlement peaks and show the ethics charter as the rejection reason, so tired operators do not become the risk the programme was meant to reduce.

Amira enforces hours caps so tired operators do not become the risk the programme was meant to reduce. Calendar locks that show the ethics charter as the rejection reason make the policy visible at booking time.

### 4.7 Narrative

Systemic-risk tabletop uses a simulated settlement delay of fifteen minutes. White-team students must stop a scenario mid-play when the delay appears. Amira fails any student who continues for just one more objective. Hours caps near settlement are enforced by calendar locks on scenario slots so heroics cannot be scheduled even by her.

In the systemic-risk tabletop, white-team students must stop when the simulated settlement delay appears. Continuing for one more objective is a fail. Amira runs the tabletop before each threat-led year so stop muscles are rehearsed, not invented under stress.

### 4.8 Bit2

Calendar locks display "ethics charter" as the rejection reason when someone tries to book over settlement peak. Showing the charter as the reason tells the requester that the block is a policy decision, not a scheduling accident.

When someone tries to book over settlement peak, the calendar shows ethics charter as the rejection reason. Repeated attempts become visible when rejection emails copy the charter maintainers; Amira reviews those copies quarterly as a signal of cultural pressure, not as a hunt for individuals.

Showing the charter as the reason also trains requesters to read the charter before asking. Quarterly review of copied rejection emails is a signal of cultural pressure on settlement-peak bookings, not a hunt for individuals to blame.

### 4.9 4.q10

Calendar lock rejection emails CC ethics charter maintainers automatically. Copying the maintainers means repeated attempts to book over settlement peak become visible to the people who own the charter.

Calendar lock rejection emails CC ethics charter maintainers automatically. If the same team hits the lock every quarter, Amira opens a decision clinic on capacity and timing rather than granting exceptions; the charter stays intact and the schedule conversation moves to the right room.

Copying the maintainers means repeated attempts to book over settlement peak become visible to the people who own the charter. Exceptions are not granted quietly; capacity and timing move to a decision clinic instead.

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

The four alternatives are written so executives see real choices: A quarterly web only, B annual threat-led only, C quarterly web plus biennial threat-led, and D continuous automated scan theatre. Amira will not discuss a vague more testing request until it maps to one of these; DEC-14 records choosing C.

DEC-14 is the record of choosing C — quarterly web plus biennial threat-led — after A, B and D were scored. A vague more testing request that does not map to one of the four alternatives is sent back until it does.

### 5.2 Scoring

Amira scores detection learning, operational risk, cost, staff capacity and examiner fit. D scores high on noise and low on learning.

She scores detection learning, operational risk, cost, staff capacity and examiner fit. D scores high on noise and low on learning; C scores best for MCH-like organisations when capacity is honest. The score sheet attaches to the alternatives memo so the recommendation is not a matter of taste.

D loses because it scores high on noise and low on learning. C wins for Meridian Clearing House when capacity is honest; the attached score sheet keeps the recommendation from becoming a matter of taste.

### 5.3 Portfolio

C usually wins for MCH-like organisations. A alone under-trains detection; B alone misses regressions.

C usually wins because A alone under-trains detection and B alone misses ordinary regressions between threat-led years. Amira still shows scores for A, B and D so directors see why C won; portfolio language means the mix, not a single silver engagement.

Portfolio language means the mix of activities, not a single purchased logo. Directors still see scores for A, B and D so they understand why A alone under-trains detection and B alone misses regressions.

### 5.4 Non-goals

No claim of SWIFT coverage from ordinary web tests; no public exploit demos; no unpaid overtime as a capacity plan.

Non-goals include no SWIFT coverage claim from ordinary web tests, no public exploit demos, and no unpaid overtime as a capacity plan. She reads them aloud at the end of the alternatives memo; a recommendation that only works if people work nights is not executable.

A recommendation that only works if people work nights is not executable, and she will not file it. Non-goals are read aloud so unpaid overtime cannot quietly become the capacity plan.

### 5.5 Sensitivity

She re-scores if capacity halves; the recommendation should still be executable.

Sensitivity analysis halves capacity and also doubles vendor cost. Current C survives halved capacity by slipping threat-led to every third year with a named white-team lead and a written date. Amira refuses a plan that only works in the best case.

If recommendation C collapses under both shocks — halved capacity and doubled vendor cost — it was never robust. Current C survives by slipping threat-led to every third year with a named lead and a written date still owned.

### 5.6 Output

A two-page alternatives memo with a calendar graphic.

The two-page memo carries the score table, the non-goals, the sensitivity result and a calendar graphic with shaded preparation months. Executives who only see the execution week miss the intel lead time that Finance once failed to fund.

Executives who only see the execution week miss the intel lead time. The calendar graphic with shaded preparation months sits beside the score table and sensitivity result on the two-page memo.

Finance once funded only the execution week and was surprised by intel lead time; the shaded cells stopped that surprise. Amira will not send an alternatives memo that lacks the calendar graphic, because executives then approve a programme they have not staffed.

### 5.7 Narrative

Sensitivity analysis in the alternatives memo halves capacity and also doubles vendor cost. If recommendation C collapses under both shocks, it was never robust. Current C survives halved capacity by slipping threat-led to every third year — still written and owned. Non-goals are read at the start of every workshop so brainstorming cannot quietly reintroduce theatre option D.

When capacity halves, slipping threat-led to every third year keeps a named white-team lead and a written date rather than a wish. Non-goals are read at workshop end so nobody leaves thinking overtime will save the plan; a memo without sensitivity is incomplete.

### 5.8 Bit2

Every-third-year threat-led still has a named white-team lead pencilled two years out; pencils beat wishes. Naming the lead two years out gives the white team time to arrange cover before the threat-led exercise is due.

Every-third-year threat-led still has a named white-team lead pencilled two years out. Naming the lead that early gives the white team time to arrange cover before the exercise is due; Amira puts the name in the calendar graphic, not only in an email.

Cover that is arranged late becomes the heroics the ethics charter forbids. Pencilling the white-team lead two years out is how Meridian Clearing House keeps every-third-year threat-led executable.

### 5.9 Story

Amira's calendar graphic uses shaded cells for threat-led preparation months, not only execution week, so executives see the true staff load. Finance once funded only the execution week and was surprised by intel lead time; the shaded cells stopped that surprise. She reprints the calendar after every DEC that changes cadence and stores the PDF hash beside DEC-14.

The calendar graphic uses shaded cells for threat-led preparation months, not only execution week. Finance once funded only the execution week and was surprised by intel lead time; she reprints the calendar after every DEC that changes cadence and stores the PDF hash beside DEC-14.

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

Amira refuses a single score that pretends to measure scenarios, detection rules and programme outcomes together. The lab scenario ranking is for scenario choice; detection rules need purple-team measures; programme outcomes need decision records such as DEC-14. Mixing designs is how empty metrics enter board packs.

Mixing scenario ranks, purple-team measures and DEC-14 outcomes into one empty metric is how board packs lose meaning. Each evaluation target keeps its own design so directors are not sold a single score that pretends to measure all four.

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

lab_scenario ranks C supply-chain library in batch app at +4, A stolen VPN with SWIFT-adjacent pivot at +3, D branch Wi-Fi rogue AP at +2 and B public web defacement at +1 using score equals 2 times learning minus risk. She demotes a high lab score when white-team feasibility is missing.

Supply-chain library in batch app scores highest at +4; stolen VPN with SWIFT-adjacent pivot scores +3 but carries risk 3; public web defacement scores only +1. White-team feasibility still decides funding after the lab rank.

### 6.3 Pre-registration

Metrics and thresholds are tagged in git before results.

Metrics and thresholds are tagged in git before results so she cannot move the goalposts after seeing scores. Pre-registration states primary measure, threshold and exclusions; changing a threshold later requires an amended tag and a note in the decision log.

A peer should be able to find the pre-registration tag without asking her. Primary measure, threshold and exclusions are short on purpose; amended tags after the fact require a decision-log note.

Changing a threshold after seeing scores requires an amended tag and a decision-log note that names why. Pre-registration is how Meridian Clearing House keeps evaluation honest when favourite scenarios underperform.

### 6.4 GAP language

"T1190 0/2 GAP" schedules engineering; it does not claim permanent blindness.

T1190 0/2 GAP schedules engineering; it does not claim permanent blindness. A dated engineering ticket is the honest companion to a T-GAP label, and doom language that says forever blind trains directors to ignore gaps.

Amira's language in findings and board packs stays in the GAP-schedules-engineering lane. Saying we are blind forever is neither true nor useful when a dated ticket can close the gap.

A dated engineering ticket is the honest companion to a T1190 0/2 GAP label. Doom language that claims permanent blindness trains directors to ignore gaps that engineering could close.

### 6.5 Independence

White team or a peer runs the scoring on the same inputs.

White team or a peer runs the scoring on the same inputs. Independence catches optimistic grading of favourite scenarios; disagreements become design notes tagged FEASIBILITY so they appear in the next scenario workshop.

She would rather lose a preferred scenario than keep a score only she can defend. Peer scoring on the same inputs catches optimistic grading before funding decisions lock in.

Disagreements become design notes tagged FEASIBILITY so they appear in the next scenario workshop automatically. Independence is not optional politeness; it is how optimistic grading of favourite scenarios is caught.

### 6.6 Ethics

Scenarios that need live participant impact are rejected at design time.

Scenarios that need live participant impact are rejected at design time. Synthetic clearing templates and isolated ranges are enough for learning; the ethics cover sheet says synthetic-only on page one of every project.

Live harm to participants is not an acceptable price for a more realistic exercise at Meridian Clearing House. Synthetic-only on page one of every project is the ethics cover that makes that refusal mechanical.

Synthetic clearing templates and isolated ranges are enough for learning at Meridian Clearing House. The ethics cover sheet that says synthetic-only on page one makes live participant impact a design-time rejection, not a negotiation mid-exercise.

### 6.7 Narrative

White-team feasibility for scenario C includes a library inventory owner who can freeze deploys. Without that owner, Amira demotes C despite its lab score. Independent scoring means she leaves the room while a peer applies lab_scenario to the same inputs; disagreements become design notes filed beside the lab output.

White-team feasibility for scenario C includes a library inventory owner who can freeze deploys; without that owner Amira demotes C despite its +4 lab score. Disagreements become design notes, not quiet overrides.

Feasibility is part of the score, not an afterthought. Without a library inventory owner who can freeze deploys, scenario C is demoted despite its +4 lab score, and the demotion is written as a design note.

### 6.8 Bit2

Design notes from scoring disagreements are tagged FEASIBILITY so they appear in the next scenario workshop automatically. Tagging disagreements this way turns a scoring dispute into an input for designing the next scenario.

Design notes from scoring disagreements are tagged FEASIBILITY so they appear in the next scenario workshop. Juniors learn that losing a favourite option is normal when feasibility fails; she reads the tagged notes aloud so the peer who disagreed sees their point land.

Tagging disagreements FEASIBILITY turns a scoring dispute into an input for designing the next scenario. Reading the notes aloud at the workshop shows juniors that losing a favourite option is normal when stop owners are missing.

### 6.9 Story

Feasibility demotion of scenario C is communicated to the board as strength, not indecision. Amira's slide title was "We refused a high-scoring scenario we could not stop". The board applauded. Lab scores without stop owners are now labelled provisional in every packet that leaves her desk.

Feasibility demotion of scenario C is communicated to the board as strength, not indecision. Her slide title was We refused a high-scoring scenario we could not stop; lab scores without stop owners are labelled provisional in every packet that leaves her desk.

### 6.10 6.q11

Provisional labels on scores are bright orange in the PDF export. The orange label keeps a provisional score from being quoted as final once the PDF leaves the team.

Provisional labels on scores are bright orange in the PDF export so a provisional rank cannot be quoted as final once the PDF leaves the team. Only scores with white-team feasibility confirmed may lose the orange mark.

Directors have thanked her for the orange colour when a vendor tried to cite a provisional rank as a commitment. Only scores with white-team feasibility confirmed may lose the provisional mark.

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

Amira draws who receives what: SOC gets ATT&CK tags and timelines; risk gets ranked residuals; legal gets disclosure-relevant facts; participants get only what contracts allow. Oversharing into the wrong channel is how trust with clearing participants breaks.

The diagram sits in the integration playbook and is reviewed when a new stakeholder appears. Oversharing into the wrong channel is how trust with clearing participants breaks, so recipients are drawn before findings move.

### 7.2 Shadow programmes

Business units hiring boutique scanners without ROE create shadow risk. Integration means one catalogue and one authorization path.

Business units hiring boutique scanners without ROE create shadow risk. Amnesty week invites declarations so shadow scans enter the catalogue or stop; undeclared scans found later become audit findings against the unit, not quiet exceptions.

Integration means one catalogue and one authorization path at Meridian Clearing House. Undeclared boutique scans found after amnesty week become audit findings against the unit, not quiet exceptions.

Amnesty week invites declarations so shadow scans enter the catalogue or stop. Business units that hire boutique scanners without ROE create shadow risk; one catalogue and one authorization path are the integration answer.

### 7.3 Cadence

Quarterly sync with SOC on noise budgets; monthly with risk on acceptance expiries; ad hoc with legal on disclosure.

Quarterly sync with SOC on noise budgets, monthly with risk on acceptance expiries, and ad hoc with legal on disclosure stay on recurring invites. Missed syncs are logged as programme debt so integration does not depend on memory.

Amira keeps the calendar invites recurring so integration does not depend on memory. Quarterly SOC noise-budget syncs and monthly risk acceptance-expiry reviews are programme debt when missed, not personal failure.

### 7.4 Health metrics

Percent of findings with owners, percent of tests in catalogue, median time from finding to detection ticket.

Health metrics are percent of findings with owners, percent of tests in catalogue, and median time from finding to detection ticket. She refuses vanity counts of raw findings without validation; the metrics appear beside amnesty counts on the same slide family.

Vanity counts of raw findings without validation stay off management slides. Percent of findings with owners, catalogue coverage and median time to detection ticket appear beside amnesty counts so the board sees hygiene.

### 7.5 Participant care

Clearing participants are customers of trust. Comms templates are pre-approved.

Clearing participants are customers of trust; communications templates are pre-approved by legal and participant management. A wrong phrase in a participant notice can cause market noise that no finding severity can justify, so Amira does not invent wording under pressure.

Amira does not invent wording under pressure when a participant notice is needed. Pre-approved templates from legal and participant management are the only words that leave the building.

A wrong phrase in a participant notice can cause market noise that no finding severity can justify. Pre-approved templates are the only channel; Amira does not invent wording when pressure rises.

### 7.6 Failure mode

Integration fails when testing is a heroic annual event with no backlog into BAU engineering.

Integration fails when testing is a heroic annual event with no backlog into BAU engineering. Every finding that needs a fix must have a ticket in the ordinary engineering queue; heroics without backlog produce the same issues next year.

Examiners notice when the same issues return next year because heroics never entered the ordinary engineering queue. Every finding that needs a fix must have a BAU ticket before Amira calls integration healthy.

### 7.7 Narrative

Shadow-programme amnesty week invites business units to declare boutique scans. Declared scans enter the catalogue or stop. Undeclared scans found later become audit findings against the unit lead. Participant comms templates are versioned; Amira rejects ad-lib emails during test-related incidents involving participants.

Shadow-programme amnesty week invites business units to declare boutique scans; declared scans enter the catalogue or stop. Rules are published before the week starts; amnesty without consequences for later concealment is theatre.

Amnesty without consequences for later concealment is theatre. Rules published before the week starts stop anyone from claiming surprise when undeclared scans become findings.

### 7.8 Bit2

Amnesty week metrics — declared, catalogued, stopped — go to the board risk committee in one slide. Keeping the three counts on one slide lets the committee see whether declarations led to tools actually being stopped.

Amnesty week metrics — declared, catalogued, stopped — go to the board risk committee in one slide. Keeping the three counts together lets the committee see whether declarations led to tools actually being stopped rather than buried in a footnote.

Amira does not bury stopped scans in a footnote. Transparency about the stopped count on the same slide as declared and catalogued shows the amnesty had teeth.

### 7.9 Story

Amnesty week produced twelve declarations; eight catalogued, four stopped. The slide to risk committee used those three numbers only. Amira refuses amnesty narratives without counts. Units that stayed silent and were later found scanning received findings with owners named in the minutes.

Amnesty week produced twelve declarations; eight catalogued, four stopped. The slide to risk committee used those three numbers only. Units that stayed silent and were later found scanning received findings with owners named in the minutes.

Amira refuses amnesty narratives without counts. Twelve declared, eight catalogued and four stopped are the only numbers on the risk-committee slide; uncounted stories cannot be checked against the minute hash later.

### 7.10 7.q11

Amnesty counts are archived with the committee minute hash. Tying the counts to the minute hash means a later reader can check that the reported figures were the ones the committee saw.

Amnesty counts are archived with the committee minute hash so a later reader can check that the reported figures were the ones the committee saw. Amira has used that check when a unit disputed whether it had declared; the hash settled the dispute.

Tying the counts to the minute hash means a later reader can check that the reported figures were the ones the committee saw. Disputes about whether a unit declared end when the hash is produced.

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

When a hostname might be participant-owned, Amira pauses and seeks written clarification. The pause is logged with the time and the question asked; written clarification from the white team or the participant contact is filed before any further probe.

Guessing is not a specialist skill at Meridian Clearing House. Written clarification is filed before any further probe when a hostname might be participant-owned, and the pause itself is logged with time and question.

### 8.2 Insider-sensitive

Findings that imply staff misconduct go through HR paths with minimal necessary detail. Testing is not a witch hunt.

Findings that imply staff misconduct go through HR paths with minimal necessary detail. Testing is not a witch hunt; her one-page HR liaison script is rehearsed so staff do not overshare in tickets that examiners might later read.

Testing is not a witch hunt. Minimal necessary detail through HR paths protects people; the rehearsed one-page liaison script stops oversharing in tickets that examiners might later read.

### 8.3 Vendor refusal

Vendors who refuse reasonable authorized testing of their components trigger risk acceptance or replacement decisions — not silent hope.

Vendors who refuse reasonable authorized testing of their components trigger risk acceptance or replacement decisions — not silent hope. Amira brings the refusal to the CISO as a decision object with options written; hoping for next year without a date is drift.

Hoping a vendor will cooperate next year without a date is drift under another name. Risk acceptance or replacement decisions are written as decision objects when authorized testing of a component is refused.

### 8.4 Record under stress

Difficult cases generate more pressure emails. All go to the CISO alias with factual headers.

Difficult cases generate more pressure emails; all go to the CISO alias with factual headers. She does not debate findings in side threads that examiners will never see; the alias creates a record that survives staff changes and mood.

The CISO alias creates a record that survives staff changes and mood. Factual headers on every pressure email keep difficult-case debates out of side threads examiners will never see.

Amira does not debate findings in side threads that examiners will never see. Difficult cases generate more pressure emails; factual headers to the CISO alias keep the record complete when staff change.

### 8.5 Time

Difficult cases get explicit time boxes so they cannot starve ordinary catalogue work forever.

Difficult cases get explicit time boxes so they cannot starve ordinary catalogue work forever. Time boxes appear on the same board as product findings; she renews a box only with a written reason and a new end date.

Infinite investigations are visible debt when time boxes sit on the same board as product findings. Renewal needs a written reason and a new end date; silent starvation of catalogue work is refused.

### 8.6 Support

Amira pairs juniors with a senior on any case that involves HR or participants.

Juniors always pair with a senior on any case that involves HR or participants. Solo juniors under that stress invent process; pairing is scheduled with the senior's name on the case file, not left to who happens to be free.

Pairing is scheduled, not left to who happens to be free, and the senior's name is on the case file. Solo juniors under HR or participant stress invent process that later fails challenge.

### 8.7 Narrative

Insider-sensitive playbooks include a one-page HR liaison script that Amira rehearses so staff do not overshare in tickets. Time boxes for difficult cases appear on the same board as product findings so infinite investigations are visible debt. Juniors always pair with a senior when HR or participants are involved.

Insider-sensitive playbooks include a one-page HR liaison script that Amira rehearses so staff do not overshare in tickets. Time boxes for difficult cases appear on the same board as product findings so infinite investigations are visible debt.

### 8.8 Bit2

HR script versioning follows the same change control as ROE templates; freelanced empathy is not a control. Putting the HR script under ROE-style change control means a well-meant wording change cannot reach an employee unreviewed.

HR script versioning follows the same change control as ROE templates; freelanced empathy is not a control. She has rejected a same-morning edit that lacked HR's countersignature; the afternoon interview waited rather than bending the process.

Putting the HR script under ROE-style change control means a well-meant wording change cannot reach an employee unreviewed. Same-morning edits without HR countersignature are rejected even when the interview is that afternoon.

### 8.9 8.q10

HR script changes require HR and Amira countersignatures the same day. Same-day countersignature prevents a script edited in the morning from being used in an afternoon interview without both owners' approval.

HR script changes require HR and Amira countersignatures the same day so a morning edit cannot reach an afternoon interview without both owners. A missing signature is a stop, not a delay to negotiate; employees deserve reviewed words.

Same-day countersignature prevents a script edited in the morning from being used in an afternoon interview without both owners' approval. Amira treats a missing signature as a stop; employees deserve reviewed words.

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

lab_assurance checks a synthetic statement against forbidden phrases — fully secure, guaranteed, hack-proof, 100 percent coverage — and prints CLEAN with chars 126 for the quarterly web tests and 2025 threat-led exercise wording. Amira runs the same check on every board pack export.

Assurance language at Meridian Clearing House is time-bounded, scope-bounded and method-bounded. Forbidden phrases never leave in a board pack export because the same linter that printed CLEAN for the synthetic statement runs on every pack.

### 9.2 Lab

lab_assurance checks a synthetic statement against forbidden phrases.

lab_assurance rejects forbidden phrases before a pack can leave. A vendor paste once introduced hack-proof and CI blocked the pack; she keeps that incident as a teaching case so deputies can run the lab without her.

The lab is small on purpose so deputies can run it without her. A vendor paste that introduced hack-proof and was blocked by CI remains the teaching case for why the check sits before pack leave.

Amira keeps the hack-proof CI block as a teaching case. Deputies run lab_assurance without her so the check does not depend on one person before a pack leaves.

### 9.3 Leadership behaviours

Amira praises early stops, funded negative results and clean catalogues more than dramatic finds.

Amira praises early stops, funded negative results and clean catalogues more than dramatic finds. A culture that only celebrates fireworks will bury pauses and refuse negative results, which is how unsafe exercises continue.

Leadership behaviours shape what juniors chase. Praising early stops, funded negative results and clean catalogues more than dramatic finds is how Meridian Clearing House keeps unsafe exercises from continuing for applause.

A culture that only celebrates fireworks will bury pauses and refuse negative results. Praising early stops and funded negative results is how unsafe exercises lose their applause incentive.

### 9.4 Coaching refusal

Role-play pressure monthly. Score calm and firm separately.

Monthly role-play puts pressure on a specialist to soften wording; scores separate calm from firm. Soft panic and angry collapse both fail. The score sheet is shared so people know what good looks like before the next pressure email arrives.

Amira wants both calm tone and firm refusal. Monthly role-play scores them separately so soft panic and angry collapse are both visible failures before a real pressure email arrives.

The score sheet is shared before the next pressure email arrives so people know what good looks like. Soft panic and angry collapse both fail; calm and firm are scored separately on purpose.

### 9.5 Board education

Teach directors what ordinary tests cannot claim about SWIFT-adjacent systems.

Directors must learn that ordinary tests do not cover SWIFT-adjacent systems. Her board education pack uses the catalogue cannot-claim lines and the rewritten CBEST-inspired slide; teaching happens before exam season, not during a finding argument.

Teaching happens before exam season, not during a finding argument. The board education pack uses catalogue cannot-claim lines and the rewritten CBEST-inspired slide so directors learn ordinary tests do not cover SWIFT-adjacent systems.

Directors who learn cannot-claim lines before exam season do not argue findings with SWIFT myths. The rewritten CBEST-inspired slide is part of the education pack, not an emergency handout mid-dispute.

### 9.6 Succession

Document decisions so a successor can continue without folklore.

Documented decisions such as DEC-14 and the two-year calendar let a successor continue without folklore. Succession folders include three CLEAN statements and three FORBIDDEN counterexamples with explanations so deputies learn by contrast.

Amira answers questions in transfer but does not keep secret side rules. DEC-14, the two-year calendar and CLEAN versus FORBIDDEN pairs in the succession folder let a successor continue without folklore.

Succession folders include three CLEAN statements and three FORBIDDEN counterexamples with explanations. Documented decisions such as DEC-14 beat hallway folklore when a successor must continue without Amira.

### 9.7 Narrative

Forbidden-phrase linter runs on every board pack export. A vendor paste once introduced hack-proof; CI blocked the pack. Succession folders include three CLEAN statements and three FORBIDDEN counterexamples with explanations so deputies learn by contrast.

Forbidden-phrase linter runs on every board pack export. When CI blocked hack-proof, she forwarded the raw CI log to the vendor without scolding; succession folders keep CLEAN and FORBIDDEN pairs so deputies learn by contrast.

Amira forwards raw CI logs without scolding when a vendor needs to see the failure. Succession folders include three CLEAN statements and three FORBIDDEN counterexamples so deputies learn by contrast before they own a pack.

### 9.8 Bit2

Vendor warning letters enclose the forbidden list as Appendix A; some vendors update their marketing decks. Attaching the list makes the warning specific: the vendor sees exactly which claims the team will not accept.

Vendor warning letters enclose the forbidden list as Appendix A; some vendors update their marketing decks. Attaching the list makes the warning specific; a vague please be careful letter changes nothing.

Amira's quiet influence seminar uses the before-and-after vendor deck pair. Specificity beats a vague please be careful letter; Appendix A with the forbidden list is what makes some vendors update their marketing decks.

### 9.9 Story

When CI blocked hack-proof, Amira forwarded the raw CI log to the vendor without scolding. The vendor's next deck used time-bounded assurance. She keeps that before-and-after pair for leadership seminars on quiet influence and refuses to tell the story as a victory over the vendor.

When CI blocked hack-proof, Amira forwarded the raw CI log without scolding. The vendor's next deck used time-bounded assurance. She keeps that before-and-after pair for leadership seminars on quiet influence and refuses to tell it as a victory over the vendor.

### 9.10 9.q11

Before-and-after vendor decks are stored as evidence of influence, not of mockery. Keeping both versions shows auditors that the warning changed vendor claims, which is the point of sending it.

Before-and-after vendor decks are stored as evidence of influence, not of mockery. Keeping both versions shows auditors that the warning changed vendor claims; influence without a record is a story, influence with a record is assurance work.

Amira can produce the pair when asked how Meridian Clearing House handles assurance language from suppliers. Influence with a record is assurance work; influence without a record is only a story.

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

lab_critique scores a synthetic abstract on question, method, n, limits and ethics; a missing n prints MISSING and revise. Amira reads to improve MCH decisions, not to decorate reports with names, and she opens sources she cites.

She opens sources she cites. A missing n on the synthetic abstract prints MISSING and revise; decorating reports with unread names is not how Meridian Clearing House improves decisions.

### 10.2 Abstract checklist

Question, method, n, limits, ethics — lab_critique scores a synthetic abstract.

The abstract checklist asks whether question, method, n, limits and ethics are present. She fails any presenter who cannot state n from memory after reading; kindness about nerves does not extend to missing limits.

lab_critique marks each checklist field ok or MISSING. Kindness about nerves does not extend to missing limits; presenters who cannot state n from memory after reading fail the club.

Amira fails any presenter who cannot state n from memory after reading. The checklist — question, method, n, limits, ethics — is the same one lab_critique scores on the synthetic abstract.

### 10.3 Citation theatre

Footnotes to unread papers are unethical in assurance contexts. She opens sources.

Footnotes to unread papers are unethical in assurance contexts. A paper club culture that bluffs citations will eventually bluff assurance language to the board, so she opens sources and expects juniors to do the same.

Amira opens sources and expects juniors to do the same. Citation theatre in assurance contexts is unethical because unread footnotes become unread confidence in board language.

A paper club culture that bluffs citations will eventually bluff assurance language to the board. Unread footnotes are unethical in assurance contexts; she opens sources and expects juniors to do the same.

### 10.4 Transfer

A paper without operationalisable actions gets a "watch" tag, not a programme change.

A paper without operationalisable actions gets a watch tag, not a programme change. She will not rewrite DEC-14 because a paper sounded exciting; transfer into MCH work needs a clear action, an owner and a fit to the catalogue.

Transfer into Meridian Clearing House work needs a clear action, an owner and a fit to the catalogue. Exciting papers without operationalisable actions stay on a watch tag, not in a DEC-14 rewrite.

### 10.5 Limits empathy

Generous reading still requires limits sections; missing limits fail the checklist.

Generous reading still requires limits sections; missing limits fail the checklist. Amira is unkind about missing limits and kind about nerves; empathy without standards produces soft assurance that examiners will not accept.

Empathy without standards produces soft assurance. Missing limits fail the checklist even when the reader is generous; she is kind about nerves and unkind about that gap.

Missing limits fail the checklist even when the abstract is otherwise generous. Empathy without that standard produces soft assurance examiners will not accept at Meridian Clearing House.

### 10.6 Seminar

Monthly paper club with the critique checklist on the wall.

Monthly paper club runs with the critique checklist on the wall — a printed lab_critique output showing MISSING for n. Operators now verify n before they offer to present, which raised pre-check rates without naming individuals.

Operators now verify n before they offer to present. The printed lab_critique output on the wall — showing MISSING for n on the synthetic abstract — raised pre-check rates without naming individuals.

Monthly paper club runs with the printed lab_critique output on the wall. Verifying n before offering to present raised pre-check rates; the wall checklist makes the standard visible without a speech.

### 10.7 Narrative

Paper club fails any presenter who cannot state n from memory after reading. Amira is kind about nerves and unkind about missing limits. Transfer of critique skill includes letting a junior run club while she stays silent for the first thirty minutes.

Paper club fails any presenter who cannot state n from memory after reading. Transfer of critique skill includes letting a junior run club while she stays silent for the first thirty minutes; the silent-thirty metric should rise each quarter.

The silent-thirty metric should rise each quarter as juniors lead. Transfer of critique skill includes letting a junior run club while she stays silent for the first thirty minutes after a presenter fails to state n.

### 10.8 Bit2

Silent-thirty metric tracks how long Amira stays quiet; the goal is longer each quarter as juniors lead. A rising silent-thirty number is evidence that juniors are running debriefs without waiting for Amira.

Silent-thirty metric tracks how long Amira stays quiet; the goal is longer each quarter as juniors lead. A rising number is evidence that juniors run debriefs without waiting for her, celebrated in the same tone as clean catalogues.

She celebrates the rise in the same tone she uses for clean catalogues. Succession of critique skill matters as much as succession of DEC-14; a rising silent-thirty number is the evidence.

### 10.9 Story

Paper club's wall checklist is a printed lab_critique output. When someone skips n, Amira points at MISSING without speaking. Juniors now pre-check n before volunteering to present. She measures pre-check rates each term and publishes them without naming people.

Paper club's wall checklist is a printed lab_critique output. When someone skips n, she points at MISSING without speaking. Juniors now pre-check n before volunteering; she measures pre-check rates each term and publishes them without naming people.

If a presenter skips n, she points at MISSING and stays quiet. Pre-check rates each term are published without naming people so the habit spreads without a blame list.

### 10.10 10.q11

Pre-check rate posters use cohort letters, never names. Cohort letters let teams compare pre-check rates without singling out any individual operator.

Pre-check rate posters use cohort letters, never names, so teams can compare rates without singling out any operator. She has rejected a draft poster that used initials; the rule matches amnesty slide discipline: counts and patterns, not a blame list.

Cohort letters let teams compare pre-check rates without singling out any individual operator. The rule matches amnesty slide discipline: counts and patterns, never initials on a public poster.

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

Build a scenario-scoring sheet and assurance linter integrated with FindingsDesk fields; evaluate on synthetic past exercises. The brief forbids live participant scanning, exploit modules and LLM auto-bury of findings; the deliverable must run when she may not type during solo-run week.

Amira's project brief forbids live participant scanning, exploit modules and LLM auto-bury of findings. Solo-run week proves the deliverable runs when she may not type; FindingsDesk field integration is part of the brief, not an optional polish.

### 11.2 Non-goals

No live participant scanning; no exploit modules; no LLM auto-bury of findings.

Non-goals are checked at every biweekly checkpoint: no live participant scanning, no exploit modules, no LLM auto-bury of findings. Amira answers first with her own near-miss about an LLM summary feature so juniors see candour is expected.

Checkpoint quizzes ask which non-goal you nearly violated this sprint. Her own near-miss about an LLM summary feature is the first answer, so juniors see that candour is expected and non-goals are checked every biweekly meeting.

### 11.3 Pre-registration

Precision of forbidden-phrase catch; ranking correlation with white-team expert order on a frozen set.

Precision of forbidden-phrase catch and ranking correlation with white-team expert order on a frozen set are tagged in git before evaluation runs. She will not tune thresholds after seeing how her favourite scenarios score.

Tags go in git before evaluation runs. Precision of forbidden-phrase catch and ranking correlation with white-team expert order on a frozen set are the pre-registered measures; tuning after seeing favourite scores is refused.

Amira will not tune thresholds after seeing how her favourite scenarios score. Pre-registration of forbidden-phrase precision and ranking correlation on a frozen set keeps the applied project honest.

### 11.4 Handover

Operators run the linter alone; Amira may not type.

Operators run the linter alone; Amira may not type. A freshly created operator account with empty shell history and a sealed envelope of ROE excerpts is the setup; if the operator phones her, the call is logged as a documentation defect.

If the operator phones her, the call is logged as a documentation defect. Empty shell history and a sealed envelope of ROE excerpts force solo success from the docs alone during handover week.

Operators run the linter alone; Amira may not type during solo-run week. A phone call to her is a documentation defect logged against the README, not a quiet rescue that hides gaps.

### 11.5 Ethics cover

Synthetic-only declaration on page one.

Synthetic-only declaration sits on page one of every project repo. Ethics cover sheets are mechanically checked for the word synthetic before merges accept; her near-miss answers from others stay anonymous, her own near-miss stays named to model candour.

Ethics cover sheets are mechanically checked for the word synthetic before merges accept. Near-miss answers from others stay anonymous; her own near-miss stays named so candour is modelled from the top.

Synthetic-only declaration on page one is mechanical: merges reject covers that lack the word. Candour about near-misses is modelled by naming her own and anonymising others.

### 11.6 Time box

Eight weeks with biweekly checkpoints.

Eight weeks with biweekly checkpoints keep the project inside a specialist time box. She refuses open-ended build time that starves catalogue work; checkpoints quiz non-goals and show whether solo-run readiness is real.

Amira refuses open-ended build time that starves catalogue work. Eight weeks with biweekly checkpoints quiz non-goals and show whether solo-run readiness is real before the clock ends.

Checkpoints quiz non-goals and show whether solo-run readiness is real before the eight-week clock ends. Open-ended build time that starves catalogue work is refused even when the tooling looks promising.

### 11.7 Narrative

Checkpoint quizzes ask which non-goal you nearly violated this sprint; Amira answers first with her own near-miss about an LLM summary feature. Ethics cover sheets are mechanically checked for the word synthetic before project repos accept merges. Solo-run week forbids her typing.

Checkpoint quizzes ask which non-goal you nearly violated this sprint; Amira answers first with her LLM summary near-miss. Solo-run week forbids her typing so operators must succeed from the docs alone; ethics covers are checked for synthetic before merges.

Solo-run week forbids her typing so operators must succeed from the docs alone. Ethics cover sheets are mechanically checked for synthetic before project repos accept merges; checkpoint quizzes keep non-goals visible each sprint.

### 11.8 Bit2

Near-miss answers are stored anonymously when others share; Amira's own near-miss stays named to model candour. Amira naming her own near-miss signals to juniors that admitting one carries no penalty.

Near-miss answers are stored anonymously when others share; Amira's own near-miss stays named to model candour. Naming her own miss signals that admitting one carries no penalty; she repeats the habit in decision clinics so leaders go first.

Candour that only juniors show is not candour; leaders go first. She repeats naming her own near-miss in decision clinics so admitting one carries no penalty in the culture.

### 11.9 Story

Solo-run week uses a freshly created operator account with empty shell history and a sealed envelope of ROE excerpts. If the operator phones Amira, the call is logged as a doc defect. Two calls in cohort one became README patches the same afternoon and a thank-you to the operator.

Solo-run week uses a freshly created operator account with empty shell history and a sealed envelope of ROE excerpts. Two calls in cohort one became README patches the same afternoon and a thank-you to the operator; phones to Amira log as doc defects.

### 11.10 11.q11

Sealed envelopes use wax stamps for theatre that reminds people the ROE is special. The ceremony is deliberate: opening a sealed ROE envelope should feel different from opening routine paperwork.

Sealed envelopes use wax stamps so opening a sealed ROE envelope feels different from routine paperwork. Juniors remember that feeling when they later handle production ROEs; theatre here serves care, not swagger.

Opening the sealed ROE envelope is meant to feel unlike routine paperwork, on purpose. Wax stamps are theatre that serves care; juniors remember the feeling when they later handle production ROEs.

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

The portfolio holds decision records, catalogue page, evidence standards, ethics charter excerpt, evaluation results, assurance examples, critique notes and project handover. Amira reviews once for residual sensitive data; synthetic examples replace anything that could identify participants.

Synthetic examples replace anything that could identify participants before the portfolio leaves her review. Decision records, catalogue page, evidence standards, ethics excerpt, evaluation results, assurance examples, critique notes and project handover all sit in one pack.

### 12.2 Transfer

Successor reads DEC-14 and the two-year calendar aloud; Amira answers questions but does not retain secret folklore.

Successor reads DEC-14 and the two-year calendar aloud; Amira answers questions but does not retain secret folklore. Transfer day includes walking introductions to SOC and legal; the successor's first catalogue update posts under their name with Amira only copied.

Email alone is not transfer. Walking introductions to SOC and legal, plus the successor's first catalogue update under their own name with Amira only copied, make the handoff visible and owned.

### 12.3 Research questions

How to measure detection learning across biennial threat-led exercises without exhausting white-team capacity remains open.

How to measure detection learning across biennial threat-led exercises without exhausting white-team capacity remains open. Amira names a watcher and a quarterly invite before she exits so the question does not die as hallway folklore when she leaves.

Leaving the open research question without an owner would make it folklore that dies when she leaves. A named watcher and a quarterly invite are set before exit so detection-learning measurement across biennial exercises stays alive.

### 12.4 Dual-use

Amira's final slide lists refusals: no public clearing exploit detail, no live demos against participants, no assurance without denominators.

Her final slide lists refusals: no public clearing exploit detail, no live demos against participants, no assurance without denominators. Dual-use discipline closes the course the same way integrity opened it; she will not trade those refusals for a conference invitation.

She will not trade those refusals for a conference invitation. No public clearing exploit detail, no live demos against participants, and no assurance without denominators close the course the same way integrity opened it.

### 12.5 Next course

AI security (158) is next in the curriculum path.

AI security is next in the curriculum path. She tells successors which skills transfer — decision objects, catalogue honesty, assurance language — and which do not; the next course does not grant authority to test real AI systems without a new ROE.

The next course does not grant authority to test real AI systems without a new ROE. Decision objects, catalogue honesty and assurance language transfer; authority to touch new systems does not.

Amira tells successors which skills from this course transfer and which do not. AI security is next; authority to test real AI systems still needs a new ROE and is not inherited from this book.

### 12.6 Care

Transfer includes introducing the successor to SOC and legal personally.

Transfer includes introducing the successor to SOC and legal personally. Walking introductions include a five-minute shadow of the SOC stand-up; she will not sign the transfer form without the SOC shadow completed.

Amira will not sign the transfer form without the SOC shadow completed. Personal introductions to SOC and legal are part of care, not optional courtesy when calendars resist.

Walking introductions include a five-minute shadow of the SOC stand-up so the successor hears noise-budget language in the wild. Care means she will not sign transfer without that shadow completed.

### 12.7 Narrative

Transfer day includes walking introductions to SOC and legal; email alone is not transfer. Open research questions get named watchers before she exits. The successor's first catalogue update posts under their name with Amira only CC'd — the visible handoff.

Transfer day includes walking introductions to SOC and legal; email alone is not transfer. Open research questions get named watchers before she exits; the successor's first catalogue update posts under their name with Amira only CC'd.

Folklore ends when names and dates replace hallway advice. Named watchers for open research questions and a successor posting under their own name are how transfer leaves writing rather than a personality cult.

### 12.8 Bit2

Watcher for the open research question receives a quarterly calendar invite with Amira optional — succession of curiosity. Leaving Amira optional on the invite tests whether the question survives without her steering it.

Watcher for the open research question receives a quarterly calendar invite with Amira optional. Leaving her optional tests whether the question survives without her steering; if attendance collapses, the watcher escalates to the CISO for a new owner.

If attendance collapses, the watcher escalates to the CISO for a new owner rather than quietly dropping the topic. Curiosity needs governance too; Amira optional on the invite is the test.

### 12.9 Story

Transfer day puts the successor in a five-minute SOC stand-up shadow so noise-budget language is heard live, not only in a slide. Amira schedules the shadow even when calendars resist. Transfer without SOC reality is incomplete and she will not sign the transfer form without it.

Amira will not call transfer complete until the successor has shadowed five minutes of SOC stand-up and heard noise-budget talk in context. Transfer without SOC reality is incomplete; she schedules the shadow even when calendars resist and will not sign without it.

Amira schedules the SOC stand-up shadow even when calendars resist. Transfer without SOC reality is incomplete; five minutes of noise-budget language in the wild is a precondition, not a recommendation.

### 12.10 12.q11

Transfer form has a checkbox "SOC shadow completed" that blocks signature when empty. Blocking signature until the SOC shadow is done makes the shadow a precondition rather than a recommendation.

Transfer form has a checkbox SOC shadow completed that blocks signature when empty. The successor and Amira both initial the box; initials without the shadow box checked never close transfer at Meridian Clearing House.

Precondition language is how Meridian Clearing House keeps transfer from becoming a paperwork fiction. Blocking signature until the SOC shadow is done, with both initials on the box, makes the shadow real.

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
