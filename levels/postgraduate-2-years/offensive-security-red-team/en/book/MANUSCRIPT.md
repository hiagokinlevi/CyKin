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

Amira's decision objects name the options, the evidence, the uncertainties, the recommendation and the owner before anyone says the team should red team more. At Meridian Clearing House, DEC-14 is the model: quarterly WSTG-style web tests plus a biennial threat-led exercise, with annual threat-led rejected for capacity and SWIFT-adjacent systems excluded under the CISO. Until those fields are written, a slogan is not a decision, and examiners cannot see what was traded away.

### 1.2 Uncertainty types

She distinguishes aleatory uncertainty (noisy detection rates) from epistemic uncertainty (unknown whether a conduit exists). Wilson-style intervals help the first; architecture workshops help the second. Mixing them produces false precision.

When detection rates are noisy, Amira reports them with intervals rather than a single percentage that pretends certainty. When nobody knows whether a conduit into a SWIFT-adjacent system exists, she schedules an architecture workshop instead of inventing a rate. Mixing the two kinds of uncertainty is how board packs gain false precision. Her decision records label which uncertainties are which, so a later reader knows what more data could fix and what only design work can fix.

### 1.3 Acceptance vs deferral

Accepting residual risk requires a named acceptor, expiry and compensating control. Deferring a test because "next year is better" without a date is neither acceptance nor management — it is drift.

For the SWIFT-adjacent exclusion in DEC-14, the CISO is the named acceptor, the exclusion has an expiry tied to the next catalogue review, and compensating controls are listed. Saying next year without a date would leave the exclusion as drift. Amira refuses to file acceptance without those three fields, and she refuses to treat an open-ended deferral as management. Examiners reading the record should see a deliberate choice, not a postponed conversation.

### 1.4 Examiner readability

Decision records answer: what was chosen, what was rejected, what evidence counted, what remains unknown. Amira rejects records that read like slogans.

A readable record for DEC-14 states what was chosen, what was rejected, which evidence counted and what remains unknown, including capacity limits on annual threat-led work. Slogans such as we take security seriously are deleted. Amira writes so a director who was not in the room can reconstruct the trade-off, and so a successor can continue without asking her for folklore.

### 1.5 Authority

Only roles listed in the governance charter may accept payment-adjacent residual risk. Amira escalates rather than inventing authority.

Payment-adjacent residual risk at Meridian Clearing House sits with roles named in the governance charter, usually the CISO for ordinary exclusions and the board risk committee for wider programme choices. Amira escalates when a product owner asks her to accept what she cannot. Invented authority collapses under examiner challenge, so she keeps the charter excerpt beside every acceptance record. She quotes the charter line in the escalation note so the product owner sees the limit is institutional.

### 1.6 Practice

Weekly decision clinic: one real (synthetic) choice, twenty minutes, written record before leaving the room.

The clinic uses a real synthetic choice from the week's work, such as whether to slip a threat-led exercise by a quarter. Twenty minutes is enough to write options, evidence and owner before anyone leaves. Amira keeps the written record in the decision log the same day, so the clinic does not become an undocumented chat. Juniors present first; she edits for clarity, not for softer conclusions.

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

Amira's catalogue at Meridian Clearing House names vulnerability management, WSTG-style web tests, purple-team drills and threat-led exercises as separate activities with separate claims. Calling all of them a red team is how boards hear assurance that was never bought. She corrects the names in every planning meeting until the vocabulary sticks, because wrong names produce wrong expectations about detection learning and SWIFT-adjacent coverage.

### 2.2 Threat-led specifics

TIBER-EU and CBEST emphasise intelligence-led scenarios, white-team control and learning for detection and response — not finding count maximisation. Amira cites their public guides when executives say "just pentest everything".

When executives ask to just pentest everything, Amira opens the public TIBER-EU and CBEST guides and shows the intelligence, white-team and detection-learning expectations. A week of scanning is not that programme. Her RFP language asks vendors for white-team design and learning objectives, not for a finding-count target, so MCH does not buy theatre dressed as threat-led work.

### 2.3 SP 800-115 and PTES

Still the backbone for planning assessment types and engagement stages. Threat-led programmes sit on top of, not instead of, scoping discipline.

Threat-led exercises at MCH still need the scoping habits from NIST SP 800-115 and PTES: written authorization, clear inclusions and exclusions, and stop conditions. Sitting on top of that backbone is how Amira keeps SWIFT-adjacent systems out of ordinary tests while still running a biennial scenario under white-team control. Skipping scoping because the exercise is special is how out-of-scope probes happen.

### 2.4 Vendor critique

Vendors who promise "full red team in a week" without intel, white team or detection goals are selling a scan with theatre. Amira's RFP questions ask for white-team design and learning objectives.

Amira's RFP questions ask who will act as white team, what detection goals will be measured, and how intelligence will shape scenarios. Vendors who cannot answer are scored as scan-with-theatre. She has rejected bids that promised a full red team in a week with no intel phase, and she records the rejection reason in the catalogue so the next buyer sees the pattern.

### 2.5 MCH catalogue

A living catalogue maps each activity to what it can and cannot claim. Honesty here prevents insurance and board misstatements.

Each catalogue row states what the activity can claim and cannot claim. Ordinary quarterly web tests cannot claim SWIFT safety; a biennial threat-led exercise cannot claim continuous coverage of every web change. Honesty here stops insurance questionnaires and board slides from overstating MCH's assurance. Amira treats a missing cannot-claim line as an incomplete row. Rows without a cannot-claim line are marked draft and cannot enter board packs.

### 2.6 Currency

Amira reviews the catalogue twice a year against new framework editions.

Twice-yearly reviews catch new editions of ATT&CK, WSTG, TIBER-EU and CBEST materials, and they catch retired vendor slogans still sitting in old board packs. Amira redlines those slogans in the archive index so they cannot be pasted forward. A catalogue that is never refreshed becomes a museum of last year's swagger. She diaries the next review date in the same calendar as threat-led preparation. A catalogue that skips a cycle is treated as a finding against the programme, not as a busy-season excuse.

### 2.7 2.7 Narrative

Catalogue reviews include a red-team vendor as guest critic once a year. Amira asks them to attack the cannot-claim lines. If they can honestly say a quarterly web test proves SWIFT safety, the line is too weak. Last year's guest failed to break the lines; she still tightened one adjective. Currency reviews also hunt retired vendor slogans lingering in old board packs and redline them in the archive index.

The guest critic's job is to stress the cannot-claim lines, not to sell services. When last year's guest could not honestly say a quarterly web test proves SWIFT safety, Amira still tightened an adjective that sounded too strong. She invites a different vendor the next year so the critique does not become captured. Currency reviews that follow the visit hunt leftover slogans in archived packs.

### 2.8 2.8 Bit

Archive redlines of old packs are linked from the catalogue changelog; forgetting history is how swagger returns.

Each redline links to the catalogue changelog entry that softened a claim, with the date and the reason. Reviewers who open the archive see why a phrase disappeared rather than guessing. Forgetting that history is how swagger returns in the next board cycle. Amira assigns a deputy to check that links still resolve after each catalogue publish. Broken links are treated as catalogue defects and fixed before the next publish.

### 2.9 2.9 Bit2

Archive redlines of old packs are linked from the catalogue changelog; forgetting history is how swagger returns. Linking each redline to the changelog entry also shows reviewers which claim was softened and why.

Linking redlines to changelog entries also shows which claim was softened and why, which matters when a director asks why the wording changed. Amira's rewrite from we are CBEST compliant to a time-bounded, CBEST-inspired exercise with SWIFT-adjacent exclusions is the worked example of that discipline. The archive keeps both versions so the path of the claim is visible.

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

Specialist-grade evidence at MCH can be reproduced under the ROE by another tester with the hashes, timestamps and scope context in the vault. Looks bad in a tool is rejected. Amira's FindingsDesk fields block board-pack entry until hash and owner are present, which forces the standard before anyone argues about colour themes. Reproducibility is the grade; drama is not.

### 3.2 Privileged data

Clearing messages and participant identifiers are highly sensitive. Amira prefers synthetic message templates even in staging when possible.

Clearing messages and participant identifiers stay out of ordinary evidence when synthetic templates can show the same class of issue. Amira prefers those templates even in staging, and she redacts anything that still looks too real. Sensitivity is not a reason to skip evidence; it is a reason to design safer evidence. When a real identifier appears by mistake, she stops, redacts and files an incident note.

### 3.3 Challenge survival

Legal or white-team challenge asks: could another specialist reproduce this observation without your laptop folklore? If not, rewrite.

In challenge drills, a second specialist has ten minutes to find a missing hash, timezone or ROE clause. If the observation cannot survive without Amira's laptop folklore, she rewrites it before it enters the vault. Calm repair after a catch is scored well; defensiveness is not. The drill exists so legal or white-team challenge never meets an unreproducible claim for the first time.

### 3.4 Theatre screenshots

Dark-themed dashboards without hashes, timestamps or scope context are rejected from the evidence vault.

Dark dashboards without hashes, timestamps or scope context look impressive and prove nothing. Amira's vault rejects them on sight. Theatre screenshots waste examiner time and train juniors to confuse polish with evidence. She asks for the boring artefacts first: command output, config excerpts and hashes. Juniors learn to expect rejection until the boring artefacts are present. She shows a rejected example beside an accepted one in onboarding so the difference is concrete.

### 3.5 Chain of custody

For threat-led exercises, custody logs are as important as technical artefacts.

For threat-led exercises, custody logs show who held which artefact, when it moved and who authorised the move. Amira treats a missing custody line as seriously as a missing hash. White-team and legal challenges often start with chain-of-custody questions, so the log is built during the exercise, not reconstructed afterwards. A custody gap pauses reporting until the chain is repaired in writing. White-team and legal challenges often start with custody, so the log is built during the exercise.

### 3.6 Platform

FindingsDesk fields enforce hash and owner before a finding may enter board packs.

FindingsDesk will not let a finding into a board pack without hash and owner. Amira refuses manual overrides for late slides. The platform gate is how MCH keeps specialist standards when calendar pressure rises before a committee meeting. Colour and severity fields come after those two, never instead of them. Late slides wait; the gate does not open for calendar pressure. Manual overrides for late slides are recorded as ethics near-misses when someone asks for them.

### 3.7 3.7 Narrative

Challenge drills pair two specialists: one presents evidence, the other has ten minutes to find a missing hash, timezone or ROE clause. Amira scores the challenger for catching real gaps and the presenter for calm repair. Vault rejection rates dropped afterward. Custody drills include a simulated laptop seizure asking whether hashes still prove out; a past fail funded HSM work for vault keys.

After challenge drills began, vault rejection rates fell because presenters arrived with hashes already filled. Custody drills include a seizure scenario where partial hash recovery still counts as fail, which later funded HSM work. Amira scores challengers for real gaps and presenters for calm repair, so the culture rewards finding problems early.

### 3.8 3.8 Bit

HSM funding used the seizure-drill fail as exhibit A in the budget memo; boring drills buy real controls.

The seizure-drill fail became exhibit A in the HSM budget memo because a boring, scored drill showed that key material could leave a device. Amira prefers that kind of evidence to dramatic incident stories. Funding followed the fail, which is the point of treating drills as real measurements rather than theatre. She keeps the memo exhibit with the drill score sheet in the archive.

### 3.9 3.9 Bit2

HSM funding used the seizure-drill fail as exhibit A in the budget memo; boring drills buy real controls. Treating a partial result as a fail is what made the drill credible evidence in that memo.

Treating a partial result as a fail made the drill credible in that memo. A recovered fragment still proved material left the device, so there was no middle grade that would have softened the story for finance. Amira keeps the scoring rule written beside the drill plan so later cohorts cannot invent a partial pass.

### 3.10 3.p9

Seizure-drill scores are pass/fail; partial hash recovery is a fail.

Pass, fail and partial are not three equal outcomes for seizure drills. Partial hash recovery is scored as fail. Amira's rule has no middle grade because a fragment still shows the control broke. Operators learn the rule before the drill so scoring arguments do not start after the clock stops. Operators initial the rule before the drill clock starts. The score sheet has no third column that could be filled in after a difficult conversation.

### 3.11 3.q10

Seizure-drill scores are pass/fail; partial hash recovery is a fail. A recovered fragment of a hash still proves the key material left the device, so the pass/fail rule has no middle grade.

A recovered fragment of a hash still proves key material left the device, so the pass-fail rule has no middle grade. Amira writes that sentence into the drill brief. Softening the fail after the fact would have weakened the HSM funding case and trained operators to negotiate scores.

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

A careless test that delays settlement can harm many participants beyond Meridian Clearing House. Amira's risk lens therefore asks systemic questions before local ones: who else clears through this path, and what happens if it pauses for fifteen minutes. Scenarios that need live participant impact are rejected at design time. Systemic harm is why stop authority and calendar locks exist. Systemic questions are written into the scenario design checklist.

### 4.2 Conflicts

Personal investments, prior employers and vendor friendships are logged. Recusal is normal, not career-limiting.

Amira logs personal investments, prior employers and vendor friendships in the conflict register and recuses when a decision touches them. Recusal is normal at MCH and is not treated as a career limit. Juniors see her step out of a vendor scoring meeting when a former employer bids, which teaches the habit better than a policy page alone. The register is reviewed before every vendor scoring meeting.

### 4.3 Optical pressure

Earnings dates and conference demos never justify burying findings. Management responses may sit beside findings; deletion may not.

Earnings dates and conference demos never justify burying findings. Management responses may sit beside findings in the board pack; deletion may not. Amira has refused requests to drop items before a demo week, and she records the refusal. Optical pressure is predictable; the ethics charter answers it before the email arrives. She files the refusal beside the finding so the record shows pressure was resisted.

### 4.4 Threat-led stops

White-team stop authority is written before scenarios start. Amira refuses exercises where nobody can stop the red team in minutes.

White-team stop authority is written before scenarios start, with names and phone numbers that work in minutes. Amira refuses exercises where nobody can stop the red team quickly. A simulated settlement delay of fifteen minutes is enough reason to stop mid-play, and students who continue for just one more objective fail the ethics tabletop. Phone numbers are tested the week before the exercise, not on the day.

### 4.5 Dual-use

Publishing clearing-specific exploit paths is out of scope for this curriculum and for MCH public talks.

Publishing clearing-specific exploit paths is out of scope for this curriculum and for MCH public talks. Amira's final slide lists that refusal beside no live demos against participants. Dual-use discipline is part of specialist identity, not an optional appendix when a conference slot looks attractive. Conference abstracts are checked against the refusal list before submission. Public talks are reviewed against the refusal list the same way board packs are linted.

### 4.6 Care

Ethics includes sleep, hours caps and no heroics near settlement windows.

Ethics includes sleep, hours caps and no heroics near settlement windows. Calendar locks block scenario bookings over settlement peaks and show the ethics charter as the rejection reason. Amira enforces caps so tired operators do not become the risk the programme was meant to reduce. Tired operators are sent home; the charter backs the manager who sends them. Managers who send people home are backed in writing when delivery pressure rises.

### 4.7 4.7 Narrative

Systemic-risk tabletop uses a simulated settlement delay of fifteen minutes. White-team students must stop a scenario mid-play when the delay appears. Amira fails any student who continues for just one more objective. Hours caps near settlement are enforced by calendar locks on scenario slots so heroics cannot be scheduled even by her.

In the systemic-risk tabletop, white-team students must stop when the simulated settlement delay appears. Continuing for one more objective is a fail. Hours caps near settlement are enforced by calendar locks on scenario bookings. Amira runs the tabletop before each threat-led year so stop muscles are rehearsed, not invented under stress.

### 4.8 4.8 Bit

Calendar locks display "ethics charter" as the rejection reason when someone tries to book over settlement peak.

When someone tries to book over settlement peak, the calendar shows ethics charter as the rejection reason. That wording tells the requester the block is policy, not a scheduling accident. Amira would rather explain a charter citation than unwind an unsafe booking after the fact. Requesters who argue with the lock are pointed to the decision clinic, not given a quiet exception. Quiet exceptions would teach the organisation that locks are optional decoration.

### 4.9 4.9 Bit2

Calendar locks display "ethics charter" as the rejection reason when someone tries to book over settlement peak. Showing the charter as the reason tells the requester that the block is a policy decision, not a scheduling accident.

Showing the charter as the reason also trains requesters to read the charter before asking. Repeated attempts become visible when rejection emails copy the charter maintainers. Amira reviews those copies quarterly as a signal of cultural pressure, not as a hunt for individuals to blame.

### 4.10 4.p9

Calendar lock rejection emails CC ethics charter maintainers automatically.

Rejection emails copy ethics charter maintainers automatically so repeated attempts to book over settlement peak are visible to the people who own the charter. Amira wants pattern visibility without personal drama. Automatic copy beats relying on the requester to escalate themselves. Quarterly pattern reviews look for teams, not for individuals to punish. Pattern reviews feed the decision clinic when the same team trips the lock repeatedly. Visibility without personal drama is the design goal of the automatic copy.

### 4.11 4.q10

Calendar lock rejection emails CC ethics charter maintainers automatically. Copying the maintainers means repeated attempts to book over settlement peak become visible to the people who own the charter.

Copying the maintainers means repeated attempts become a programme signal. If the same team hits the lock every quarter, Amira opens a decision clinic on capacity and timing rather than granting exceptions. The charter stays intact; the schedule conversation moves to the right room. Exceptions, if any, become decision objects with expiry dates — never silent calendar overrides.

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

The four alternatives are written so executives see real choices: A quarterly web only, B annual threat-led only, C quarterly web plus biennial threat-led, and D continuous automated scan theatre. Amira will not discuss a vague more testing request until it maps to one of these. DEC-14 is the record of choosing C. Mapping a vague request to A through D is the first twenty minutes of the clinic.

### 5.2 Scoring

Amira scores detection learning, operational risk, cost, staff capacity and examiner fit. D scores high on noise and low on learning.

She scores detection learning, operational risk, cost, staff capacity and examiner fit. D scores high on noise and low on learning, which is why scan theatre loses. C scores best for MCH-like organisations when capacity is honest. The score sheet is attached to the alternatives memo so the recommendation is not a matter of taste. The sheet is versioned beside DEC-14 so scores and choice stay linked.

### 5.3 Portfolio

C usually wins for MCH-like organisations. A alone under-trains detection; B alone misses regressions.

C usually wins because A alone under-trains detection and B alone misses ordinary regressions between threat-led years. Amira still shows the scores for A, B and D so directors see why C won. Portfolio language means the mix, not a single silver engagement. She shows A and B losses explicitly so directors do not reopen them without new evidence. Reopening A or B needs new evidence, not nostalgia for a simpler slide.

### 5.4 Non-goals

No claim of SWIFT coverage from ordinary web tests; no public exploit demos; no unpaid overtime as a capacity plan.

Non-goals for MCH include no SWIFT coverage claim from ordinary web tests, no public exploit demos and no unpaid overtime as a capacity plan. Amira reads them aloud at the end of the alternatives memo. A recommendation that only works if people work nights is not executable, and she will not file it. Non-goals that are only spoken are treated as missing from the memo.

### 5.5 Sensitivity

She re-scores if capacity halves; the recommendation should still be executable.

Sensitivity analysis halves capacity and also doubles vendor cost. If recommendation C collapses under both shocks, it was never robust. Current C survives halved capacity by slipping threat-led to every third year, still written and owned. Amira refuses a plan that only works in the best case. A plan that needs unpaid overtime is sent back for redesign. Redesign means fewer activities or more staff — not the same plan with hope.

### 5.6 Output

A two-page alternatives memo with a calendar graphic.

The two-page memo carries the score table, the non-goals, the sensitivity result and a calendar graphic with shaded preparation months. Executives who only see the execution week miss the intel lead time. Amira reprints the calendar after every DEC that changes cadence and stores the PDF hash beside DEC-14. The hash beside DEC-14 proves which calendar the committee saw. Without the hash, two calendars can circulate and nobody knows which one was approved.

### 5.7 5.7 Narrative

Sensitivity analysis in the alternatives memo halves capacity and also doubles vendor cost. If recommendation C collapses under both shocks, it was never robust. Current C survives halved capacity by slipping threat-led to every third year — still written and owned. Non-goals are read at the start of every workshop so brainstorming cannot quietly reintroduce theatre option D.

When capacity halves, slipping threat-led to every third year keeps a named white-team lead and a written date rather than a wish. Non-goals are read at the end so nobody leaves thinking overtime will save the plan. Amira treats a memo without sensitivity as incomplete, because examiners will ask what happens if staff leave.

### 5.8 5.8 Bit

Every-third-year threat-led still has a named white-team lead pencilled two years out; pencils beat wishes.

Every-third-year threat-led still has a named white-team lead pencilled two years out. Pencils beat wishes because a name can arrange cover. Amira checks that the pencil is still willing at each catalogue review, and she replaces the name if the person has moved roles. A pencil without a confirmed willing person is replaced before the review closes. Willingness is confirmed in a short mail filed beside the calendar graphic.

### 5.9 5.9 Bit2

Every-third-year threat-led still has a named white-team lead pencilled two years out; pencils beat wishes. Naming the lead two years out gives the white team time to arrange cover before the threat-led exercise is due.

Naming the lead two years out gives the white team time to arrange cover before the exercise is due. Amira puts the name in the calendar graphic, not only in an email. Cover that is arranged late becomes the heroics the ethics charter forbids. Late cover is logged as a near-miss against the ethics charter.

### 5.10 5.10 Story

Amira's calendar graphic uses shaded cells for threat-led preparation months, not only execution week, so executives see the true staff load. Finance once funded only the execution week and was surprised by intel lead time; the shaded cells stopped that surprise. She reprints the calendar after every DEC that changes cadence and stores the PDF hash beside DEC-14.

Finance once funded only the execution week and was surprised by intel lead time; shaded preparation cells stopped that surprise. Amira reprints the calendar after every DEC that changes cadence and stores the PDF hash beside DEC-14. Executives who see the true staff load make capacity decisions that match the programme they approved.

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

Scenario choice, control coverage, detection rules and programme outcomes each need different evaluation designs at Meridian Clearing House. Amira refuses a single score that pretends to measure all four. The lab scenario ranking is for scenario choice; detection rules need purple-team measures; programme outcomes need decision records such as DEC-14. Mixing designs is how empty metrics enter board packs. She rejects dashboards that collapse the four into one traffic-light.

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

The lab ranks synthetic scenarios by learning minus risk so high-learning, manageable-risk options surface. Supply-chain library in batch app scores highest at +4; stolen VPN with SWIFT-adjacent pivot scores +3 but carries risk 3; public web defacement scores only +1. Amira demotes a high lab score when white-team feasibility is missing, as when scenario C lacked a library inventory owner who can freeze deploys.

### 6.3 Pre-registration

Metrics and thresholds are tagged in git before results.

Metrics and thresholds are tagged in git before results so Amira cannot move the goalposts after seeing scores. Pre-registration is short: primary measure, threshold, exclusions. A peer should be able to find the tag without asking her. Changing a threshold after the fact requires an amended tag and a note in the decision log. Peers are shown where the tag lives during onboarding. Onboarding includes opening the tag on a clean clone so the habit transfers.

### 6.4 GAP language

"T1190 0/2 GAP" schedules engineering; it does not claim permanent blindness.

T-GAP schedules engineering work; it does not claim permanent blindness. Amira's language in findings and board packs stays in that lane. Saying we are blind forever is neither true nor useful, and it trains directors to ignore gaps. A dated engineering ticket is the honest companion to a T-GAP label. Board language is checked for blindness claims before export. Engineering tickets carry the same identifier as the T-GAP label for traceability.

### 6.5 Independence

White team or a peer runs the scoring on the same inputs.

White team or a peer runs the scoring on the same inputs while Amira leaves the room. Independence catches optimistic grading of her favourite scenarios. Disagreements become design notes tagged feasibility so they appear in the next scenario workshop. She would rather lose a preferred scenario than keep a score only she can defend. Optimistic grading of her own favourites is the failure mode independence exists to catch.

### 6.6 Ethics

Scenarios that need live participant impact are rejected at design time.

Live participant impact is refused while scenarios are still on paper. Synthetic clearing templates and isolated ranges are enough for learning. Amira's ethics cover sheet says synthetic-only on page one of every project. Live harm to participants is not an acceptable price for a more realistic exercise at MCH. Design-time rejection is cheaper than stopping mid-exercise under white-team pressure. Synthetic templates are listed in the scenario pack so operators do not improvise live data.

### 6.7 6.7 Narrative

White-team feasibility for scenario C includes a library inventory owner who can freeze deploys. Without that owner, Amira demotes C despite its lab score. Independent scoring means she leaves the room while a peer applies lab_scenario to the same inputs; disagreements become design notes filed beside the lab output.

White-team feasibility for scenario C includes a library inventory owner who can freeze deploys; without that owner Amira demotes C despite its lab score. Independent scoring means she leaves the room while a peer applies the same inputs. Disagreements become design notes, not quiet overrides. Feasibility is part of the score, not an afterthought.

### 6.8 6.8 Bit

Design notes from scoring disagreements are tagged FEASIBILITY so the following scenario workshop receives them without hunting.

Design notes from scoring disagreements are tagged feasibility so the next scenario workshop pulls them without a manual hunt. Amira wants disputes to improve the next design rather than vanish into chat. Tags that nobody reviews are useless; the workshop agenda pulls them by label. Workshop agendas that omit tagged notes are incomplete. Pulling notes by label is a checklist item on the workshop agenda template.

### 6.9 6.9 Bit2

Design notes from scoring disagreements are tagged FEASIBILITY so they appear in the next scenario workshop automatically. Tagging disagreements this way turns a scoring dispute into an input for designing the next scenario.

Tagging disagreements this way turns a scoring dispute into an input for designing the next scenario. Juniors learn that losing a favourite option is normal when feasibility fails. Amira reads the tagged notes aloud at the workshop so the peer who disagreed sees their point land. Hearing the note read aloud closes the loop for the peer who disagreed.

### 6.10 6.10 Story

Feasibility demotion of scenario C is communicated to the board as strength, not indecision. Amira's slide title was "We refused a high-scoring scenario we could not stop". The board applauded. Lab scores without stop owners are now labelled provisional in every packet that leaves her desk.

Feasibility demotion of scenario C is communicated to the board as strength, not indecision. Amira's slide title was we refused a high-scoring scenario we could not stop; the board approved the refusal. Provisional labels stay bright orange until white-team feasibility is confirmed. Strength is knowing when not to run a scenario.

### 6.11 6.p10

Provisional labels on scores are bright orange in the PDF export.

Provisional labels on scores are bright orange in the PDF export so nobody quotes them as final once the file leaves the team. Amira checks a sample of exports each quarter. A grey provisional label that looks final has caused trouble before; orange is hard to miss in a board pack. Sample checks include opening the PDF on a projector where orange must still read clearly. Projector checks catch contrast problems that a laptop screen hides.

### 6.12 6.q11

Provisional labels on scores are bright orange in the PDF export. The orange label keeps a provisional score from being quoted as final once the PDF leaves the team.

The orange label keeps a provisional score from being quoted as final once the PDF leaves the team. Amira's rule is that only scores with white-team feasibility confirmed may lose the orange mark. Directors have thanked her for the colour when a vendor tried to cite a provisional rank as a commitment.

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

Amira draws who receives what: SOC gets ATT&CK tags and timelines; risk gets ranked residuals; legal gets disclosure-relevant facts; participants get only what contracts allow. Oversharing into the wrong channel is how trust with clearing participants breaks. The diagram sits in the integration playbook and is reviewed when a new stakeholder appears. New stakeholders get a copy of the diagram before they receive their first finding.

### 7.2 Shadow programmes

Business units hiring boutique scanners without ROE create shadow risk. Integration means one catalogue and one authorization path.

Business units hiring boutique scanners without an ROE create shadow risk. Integration means one catalogue and one authorization path at Meridian Clearing House. Amira's amnesty week invites declarations so shadow scans enter the catalogue or stop. Undeclared scans found later become audit findings against the unit, not quiet exceptions. One authorization path means boutique scans without ROE are out of bounds by definition.

### 7.3 Cadence

Quarterly sync with SOC on noise budgets; monthly with risk on acceptance expiries; ad hoc with legal on disclosure.

Quarterly sync with SOC covers noise budgets; monthly sync with risk covers acceptance expiries; legal is ad hoc on disclosure. Amira keeps the calendar invites recurring so integration does not depend on memory. Missed syncs are logged as programme debt, not as personal failure. Programme debt from missed syncs is raised in the same forum as catalogue gaps. Recurring invites are owned by the programme calendar, not by Amira's personal mailbox alone.

### 7.4 Health metrics

Percent of findings with owners, percent of tests in catalogue, median time from finding to detection ticket.

Useful metrics include percent of findings with owners, percent of tests in the catalogue and median time from finding to detection ticket. Amira refuses vanity counts of raw findings without validation. The metrics appear in the same slide family as amnesty counts so the board sees hygiene, not theatre. Metrics without denominators are rejected the same way assurance slogans are. Denominators are required in the slide footer whenever a percentage appears.

### 7.5 Participant care

Clearing participants are customers of trust. Comms templates are pre-approved.

Clearing participants are customers of trust; communications templates are pre-approved by legal and participant management. Amira does not invent wording under pressure. A wrong phrase in a participant notice can cause market noise that no finding severity can justify. Unapproved wording is a stop, even when a participant asks for a faster reply. Faster replies use a shorter approved template, never free prose under stress. Market noise from a wrong phrase can outweigh the finding that prompted the notice.

### 7.6 Failure mode

Integration fails when testing is a heroic annual event with no backlog into BAU engineering.

Integration fails when testing is a heroic annual event with no backlog into BAU engineering. Amira insists every finding that needs a fix has a ticket in the ordinary engineering queue. Heroics without backlog produce the same issues next year, which examiners notice. BAU tickets are the proof that testing feeds engineering rather than a once-a-year show. Backlog age is reviewed with engineering so heroic clears do not become the norm.

### 7.7 7.7 Narrative

Shadow-programme amnesty week invites business units to declare boutique scans. Declared scans enter the catalogue or stop. Undeclared scans found later become audit findings against the unit lead. Participant comms templates are versioned; Amira rejects ad-lib emails during test-related incidents involving participants.

Shadow-programme amnesty week invites business units to declare boutique scans; declared scans enter the catalogue or stop. Undeclared scans found later become audit findings against the unit. Amira publishes the rules before the week starts so nobody can claim surprise. Amnesty without consequences for later concealment is theatre.

### 7.8 7.8 Bit

Amnesty week metrics — declared, catalogued, stopped — go to the board risk committee in one slide.

Declared, catalogued and stopped counts travel to the board risk committee on a single slide. Amira refuses amnesty narratives without counts. Twelve declarations, eight catalogued and four stopped is the kind of line the committee can act on. A slide without the three counts is sent back before it reaches the committee. The committee slide is generated from the same spreadsheet that feeds the archive hash.

### 7.9 7.9 Bit2

Amnesty week metrics — declared, catalogued, stopped — go to the board risk committee in one slide. Keeping the three counts on one slide lets the committee see whether declarations led to tools actually being stopped.

Keeping the three counts on one slide lets the committee see whether declarations led to catalogue entry or to stops. Amira does not bury stopped scans in a footnote. Transparency about stops shows the amnesty had teeth. Stopped scans on the slide show the amnesty had consequences, not only hospitality.

### 7.10 7.10 Story

Amnesty week produced twelve declarations; eight catalogued, four stopped. The slide to risk committee used those three numbers only. Amira refuses amnesty narratives without counts. Units that stayed silent and were later found scanning received findings with owners named in the minutes.

Amnesty week produced twelve declarations, eight catalogued and four stopped. The slide to the risk committee used those three numbers only. Amira refuses amnesty narratives without counts. Uncounted stories cannot be checked against the minute hash later. The twelve/eight/four counts stay in the same spreadsheet that feeds the archive.

### 7.11 7.p10

Amnesty counts are archived with the committee minute hash.

Amnesty counts are archived with the committee minute hash so a later reader can check that the reported figures were the ones the committee saw. Amira files the hash the same day as the meeting. Archive without integrity is just another folder of claims. Same-day filing stops arguments about which numbers were shown. Arguments about numbers end when the hash matches the minute attachment. The minute attachment and the counts must hash-verify together before archive close.

### 7.12 7.q11

Amnesty counts are archived with the committee minute hash. Tying the counts to the minute hash means a later reader can check that the reported figures were the ones the committee saw.

Tying the counts to the minute hash means a later reader can check that the reported figures were the ones the committee saw. Amira has used that check when a unit disputed whether it had declared. The hash settled the dispute without a long argument. Units that dispute the counts meet the hash before they meet another meeting.

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

When a hostname might be participant-owned, Amira pauses and seeks written clarification. Guessing is not a specialist skill at Meridian Clearing House. The pause is logged with the time and the question asked. Written clarification from the white team or the participant contact is filed before any further probe. Written clarification is filed before any further packet leaves the tester's laptop. The question asked is quoted in the log so later readers see what was unclear.

### 8.2 Insider-sensitive

Findings that imply staff misconduct go through HR paths with minimal necessary detail. Testing is not a witch hunt.

Findings that imply staff misconduct go through HR paths with minimal necessary detail. Testing is not a witch hunt. Amira's one-page HR liaison script is rehearsed so staff do not overshare in tickets. Juniors always pair with a senior when HR or participants are involved. Minimal necessary detail means no gossip fields in the ticket. Gossip fields are removed from the ticket schema for insider-sensitive cases.

### 8.3 Vendor refusal

Vendors who refuse reasonable authorized testing of their components trigger risk acceptance or replacement decisions — not silent hope.

Vendors who refuse reasonable authorized testing of their components trigger risk acceptance or replacement decisions, not silent hope. Amira brings the refusal to the CISO with options written as a decision object. Hoping a vendor will cooperate next year without a date is drift under another name. Options are written as accept risk, replace component or obtain testing rights — not wait and see.

### 8.4 Record under stress

Difficult cases generate more pressure emails. All go to the CISO alias with factual headers.

Difficult cases generate more pressure emails; all go to the CISO alias with factual headers. Amira does not debate findings in side threads that examiners will never see. The alias creates a record that survives staff changes and mood. Side threads are redirected to the alias with a short factual summary. Factual headers name the case id and the decision needed, not the mood of the sender.

### 8.5 Time

Difficult cases get explicit time boxes so they cannot starve ordinary catalogue work forever.

Difficult cases get explicit time boxes so they cannot starve ordinary catalogue work forever. Time boxes appear on the same board as product findings, so infinite investigations are visible debt. Amira renews a box only with a written reason and a new end date. Visible debt on the board is how infinite cases get management attention. Renewals without a written reason are rejected by the board admin as incomplete.

### 8.6 Support

Amira pairs juniors with a senior on any case that involves HR or participants.

Amira pairs juniors with a senior on any case that involves HR or participants. Solo juniors under that stress invent process. Pairing is scheduled, not left to who happens to be free, and the senior's name is on the case file. Scheduled pairing beats hoping a senior walks by. The senior's name on the case file is what makes pairing auditable. Free pairing is not a plan; the schedule entry is the plan.

### 8.7 8.7 Narrative

Insider-sensitive playbooks include a one-page HR liaison script that Amira rehearses so staff do not overshare in tickets. Time boxes for difficult cases appear on the same board as product findings so infinite investigations are visible debt. Juniors always pair with a senior when HR or participants are involved.

Insider-sensitive playbooks include a one-page HR liaison script that Amira rehearses so staff do not overshare in tickets. Time boxes for difficult cases appear on the same board as product findings. Juniors always pair with a senior when participants are in scope. Rehearsal prevents the first real case from being the first practice.

### 8.8 8.8 Bit

HR script versioning follows the same change control as ROE templates; freelanced empathy is not a control.

HR script versioning follows the same change control as ROE templates; improvised empathy is not a control. A well-meant wording change cannot reach an employee unreviewed. Amira and HR countersign changes the same day before the script is used. Improvised wording is rejected even when it sounds kinder. Kinder wording still needs both countersignatures before it reaches an employee. Both signatures are checked before the script leaves the change-control folder.

### 8.9 8.9 Bit2

HR script versioning follows the same change control as ROE templates; freelanced empathy is not a control. Putting the HR script under ROE-style change control means a well-meant wording change cannot reach an employee unreviewed.

Putting the HR script under ROE-style change control means a well-meant wording change cannot reach an employee unreviewed. Amira has rejected a same-morning edit that lacked HR's countersignature. The afternoon interview waited; the process did not bend. An unsigned morning edit stays in the change folder until both owners arrive.

### 8.10 8.p9

HR script changes require HR and Amira countersignatures the same day.

Changes to the HR script need both HR and Amira to sign that day. Same-day countersignature prevents a script edited in the morning from being used in an afternoon interview without both owners' approval. The rule is written on the script cover. The cover rule is read aloud when a change is proposed under time pressure. Time pressure is the usual reason people ask to skip the cover rule — and the usual reason to keep it.

### 8.11 8.q10

HR script changes require HR and Amira countersignatures the same day. Same-day countersignature prevents a script edited in the morning from being used in an afternoon interview without both owners' approval.

A morning edit must not reach an afternoon interview unless both owners already signed. Amira treats a missing signature as a stop, not as a delay to negotiate. Employees deserve reviewed words. An interview that waits for signatures is still better than unreviewed words. The stop is written into the playbook so juniors do not invent a workaround.

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

Assurance language at MCH is time-bounded, scope-bounded and method-bounded. Forbidden phrases include fully secure, guaranteed, hack-proof and 100 percent coverage. The lab checks a synthetic statement and prints CLEAN when the quarterly web tests and 2025 threat-led exercise wording stays inside the rules. Amira runs the same check on every board pack export. Board exports that fail the lab are blocked the same day, not patched after the meeting.

### 9.2 Lab

lab_assurance checks a synthetic statement against forbidden phrases.

lab_assurance rejects forbidden phrases before a pack can leave. A vendor paste once introduced hack-proof and CI blocked the pack. Amira keeps that incident as a teaching case. The lab is small on purpose so deputies can run it without her. Deputies run the lab monthly so the skill does not sit with Amira alone. Monthly runs keep the clean and forbidden examples fresh in deputies' hands. Fresh examples beat a dusty slide that deputies only watch Amira operate.

### 9.3 Leadership behaviours

Amira praises early stops, funded negative results and clean catalogues more than dramatic finds.

Amira praises early stops, funded negative results and clean catalogues more than dramatic finds. Leadership behaviours shape what juniors chase. A culture that only celebrates fireworks will bury pauses and refuse negative results, which is how unsafe exercises continue. What leaders praise becomes what the next exercise optimises for. She thanks people for pauses in the same forum where finds are celebrated. Celebrating pauses in public is how early stops become status rather than embarrassment.

### 9.4 Coaching refusal

Role-play pressure monthly. Score calm and firm separately.

Monthly role-play puts pressure on a specialist to soften wording; scores separate calm from firm. Amira wants both: calm tone and firm refusal. Soft panic and angry collapse both fail. The score sheet is shared so people know what good looks like. Shared score sheets stop debates about whether firm meant rude. Firm without calm reads as anger; calm without firm reads as surrender. Angry collapse and soft panic are both scored as fails on the shared sheet.

### 9.5 Board education

Teach directors what ordinary tests cannot claim about SWIFT-adjacent systems.

Directors must learn that ordinary tests do not cover SWIFT-adjacent systems. Amira's board education pack uses the catalogue cannot-claim lines and the rewritten CBEST-inspired slide. Teaching happens before exam season, not during a finding argument. Exam-season arguments are the wrong classroom for first lessons about SWIFT exclusions. First lessons belong in scheduled board education, not in a heated finding thread. Scheduled education gives directors language before they meet a SWIFT exclusion in anger.

### 9.6 Succession

Document decisions so a successor can continue without folklore.

Documented decisions such as DEC-14 and the two-year calendar let a successor continue without folklore. Amira answers questions in transfer but does not keep secret side rules. Succession folders include three CLEAN statements and three FORBIDDEN counterexamples with explanations. Secret side rules are a succession failure even if the work was excellent. Hallway advice is written into DEC records or discarded. Discarded hallway advice is not lost work; it is how folklore dies on purpose.

### 9.7 9.7 Narrative

Forbidden-phrase linter runs on every board pack export. A vendor paste once introduced hack-proof; CI blocked the pack. Succession folders include three CLEAN statements and three FORBIDDEN counterexamples with explanations so deputies learn by contrast.

The forbidden-phrase linter runs on every board pack export. When a vendor paste introduced hack-proof, CI blocked the pack. Succession folders include three CLEAN statements and three FORBIDDEN counterexamples so deputies learn by contrast. Amira forwards raw CI logs without scolding when a vendor needs to see the failure.

### 9.8 9.8 Bit

Vendor warning letters enclose the forbidden list as Appendix A; some vendors update their marketing decks.

Vendor warning letters enclose the forbidden list as appendix A so the warning is specific. Some vendors update their marketing decks. Amira stores before-and-after decks as evidence of influence, not of mockery, and refuses to tell the story as a victory over the vendor. Mockery would close the door the warning is meant to open. The next vendor conversation needs an open door more than a good story for seminars.

### 9.9 9.9 Bit2

Vendor warning letters enclose the forbidden list as Appendix A; some vendors update their marketing decks. Attaching the list makes the warning specific: the vendor sees exactly which claims the team will not accept.

Attaching the list makes the warning specific: the vendor sees exactly which claims the team will not accept. Amira's quiet influence seminar uses that pair. Specificity beats a vague please be careful letter that changes nothing. Vague caution letters are rewritten until they quote the forbidden list by name.

### 9.10 9.10 Story

When CI blocked hack-proof, Amira forwarded the raw CI log to the vendor without scolding. The vendor's next deck used time-bounded assurance. She keeps that before-and-after pair for leadership seminars on quiet influence and refuses to tell the story as a victory over the vendor.

When CI blocked hack-proof, Amira forwarded the raw CI log to the vendor without scolding. The vendor's next deck used time-bounded assurance. She keeps that before-and-after pair for leadership seminars on quiet influence and refuses to tell the story as a victory over the vendor.

### 9.11 9.p10

Before-and-after vendor decks are stored as evidence of influence, not of mockery.

Vendor decks from before and after the warning are filed to show influence, not mockery. Amira labels the folder accordingly. Mockery would poison the next vendor conversation; evidence of change supports the programme. Folder labels shape how later readers tell the story. Later readers should learn influence, not scorn, from the folder. Scorn in the archive would teach the wrong lesson to the next specialist. Influence without scorn is the standard for that folder.

### 9.12 9.q11

Before-and-after vendor decks are stored as evidence of influence, not of mockery. Keeping both versions shows auditors that the warning changed vendor claims, which is the point of sending it.

Keeping both versions shows auditors that the warning changed vendor claims, which is the point of sending it. Amira can produce the pair when asked how MCH handles assurance language from suppliers. Influence without a record is a story; influence with a record is assurance work. Suppliers who ask what changed receive the before-and-after pair under NDA.

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

Amira reads to improve Meridian Clearing House decisions, not to decorate reports with names. lab_critique scores a synthetic abstract on question, method, n, limits and ethics; a missing n prints MISSING and revise. She opens sources she cites. Footnotes to unread papers are unethical in assurance contexts. Unread citations are removed before a critique note is filed. Decoration footnotes are deleted in the same edit pass as forbidden assurance phrases.

### 10.2 Abstract checklist

Question, method, n, limits, ethics — lab_critique scores a synthetic abstract.

The abstract checklist asks whether question, method, n, limits and ethics are present. lab_critique marks each ok or MISSING. Amira fails any presenter who cannot state n from memory after reading. Kindness about nerves does not extend to missing limits. MISSING on n is enough reason to send a presenter back to the paper. Presenters who return with n stated from memory are scheduled preferentially next month. Preferential scheduling rewards the habit without naming anyone who struggled.

### 10.3 Citation theatre

Footnotes to unread papers are unethical in assurance contexts. She opens sources.

Citation theatre — footnotes to unread papers — is unethical in assurance contexts. Amira opens sources and expects juniors to do the same. A paper club culture that bluffs citations will eventually bluff assurance language to the board. Bluffed citations are corrected in the club minutes without humiliation theatre. Minutes note the correction so the bluff does not spread as a citation tip. Citation tips that are actually bluffs are dangerous in assurance writing.

### 10.4 Transfer

A paper without operationalisable actions gets a "watch" tag, not a programme change.

A paper without operationalisable actions gets a watch tag, not a programme change. Amira will not rewrite DEC-14 because a paper sounded exciting. Transfer into MCH work needs a clear action, an owner and a fit to the catalogue. Watch tags are reviewed quarterly; programme changes need a stronger bar. Exciting papers can still earn a watch tag and a second read next quarter. A second read next quarter is cheaper than a wrong programme change this month.

### 10.5 Limits empathy

Generous reading still requires limits sections; missing limits fail the checklist.

Generous reading still requires limits sections; missing limits fail the checklist. Amira is unkind about missing limits and kind about nerves. Empathy without standards produces soft assurance. Standards without empathy are brittle; empathy without standards is empty. The checklist fails missing limits even when the rest of the abstract sings. Singing abstracts still fail when limits are absent from the page. Soft assurance is the risk when empathy outruns the checklist.

### 10.6 Seminar

Monthly paper club with the critique checklist on the wall.

Monthly paper club runs with the critique checklist on the wall — a printed lab_critique output. When someone skips n, Amira points at MISSING without speaking. Operators now verify n before they offer to present. Pointing at the wall checklist keeps her voice out of the correction. Silence while pointing keeps the correction about the paper, not about her authority. Authority that stays silent can still enforce a checklist on the wall.

### 10.7 10.7 Narrative

Paper club fails any presenter who cannot state n from memory after reading. Amira is kind about nerves and unkind about missing limits. Transfer of critique skill includes letting a junior run club while she stays silent for the first thirty minutes.

Paper club fails any presenter who cannot state n from memory after reading. Amira is kind about nerves and unkind about missing limits. Transfer of critique skill includes letting a junior run club while she stays silent for the first thirty minutes. The silent-thirty metric should rise each quarter.

### 10.8 10.8 Bit

Silent-thirty metric tracks how long Amira stays quiet; the goal is longer each quarter as juniors lead.

The silent-thirty metric tracks how long Amira stays quiet; the goal is longer each quarter as juniors lead. A rising number is evidence that juniors can run debriefs without waiting for her. She publishes the metric without naming people. Publishing the metric without names keeps the focus on the habit. Habit metrics belong in programme health slides beside catalogue currency. Programme health slides should show critique habits beside catalogue currency.

### 10.9 10.9 Bit2

Silent-thirty metric tracks how long Amira stays quiet; the goal is longer each quarter as juniors lead. A rising silent-thirty number is evidence that juniors are running debriefs without waiting for Amira.

A rising silent-thirty number is evidence that juniors are running debriefs without waiting for Amira. She celebrates the rise in the same tone she uses for clean catalogues. Succession of critique skill matters as much as succession of DEC-14. Critique skill that needs her in the room is not yet transferred.

### 10.10 10.10 Story

Paper club's wall checklist is a printed lab_critique output. If a presenter skips n, she points at MISSING and stays quiet. Juniors now pre-check n before volunteering to present. She measures pre-check rates each term and publishes them without naming people.

Paper club's wall checklist is a printed lab_critique output. When someone skips n, Amira points at MISSING without speaking. Juniors now pre-check n before volunteering to present. She measures pre-check rates each term and publishes them without naming people.

### 10.11 10.p10

Pre-check rate posters use cohort letters, never names.

Pre-check rate posters use cohort letters, never names, so teams can compare rates without singling out any individual operator. Amira wants learning pressure, not humiliation. Cohort letters are enough to see whether the habit is spreading. Learning pressure without humiliation is a deliberate design choice. Initials and names are stripped in the same review that checks cohort letters. The same review strips both names and informal nicknames. Cohort letters are enough; personal identity never belongs on the poster.

### 10.12 10.q11

Pre-check rate posters use cohort letters, never names. Cohort letters let teams compare pre-check rates without singling out any individual operator.

Cohort letters let teams compare pre-check rates without singling out any individual operator. Amira has rejected a draft poster that used initials. The rule matches the amnesty slide discipline: counts and patterns, not a blame list. Posters that drift toward initials are pulled before they hang. Blame lists are the wrong tool for a learning metric. Cohort letters remain the only identity the poster may carry.

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

Build a scenario-scoring sheet and assurance linter integrated with FindingsDesk fields; evaluate on synthetic past exercises. Amira's project brief forbids live participant scanning, exploit modules and LLM auto-bury of findings. The deliverable must run when she may not type, during solo-run week. Solo-run success is the acceptance test for the handover. If she must type for the tool to work, the handover has failed.

### 11.2 Non-goals

No live participant scanning; no exploit modules; no LLM auto-bury of findings.

Non-goals are checked at every biweekly checkpoint: no live participant scanning, no exploit modules, no LLM auto-bury of findings. Amira answers first with her own near-miss about an LLM summary feature. Checkpoint quizzes ask which non-goal you nearly violated this sprint. Near-misses about LLM features are first-class checkpoint content. LLM near-misses are filed with other ethics near-misses, not joked away. Joking away an LLM near-miss is how non-goals erode between checkpoints.

### 11.3 Pre-registration

Precision of forbidden-phrase catch; ranking correlation with white-team expert order on a frozen set.

Pre-registration names precision of forbidden-phrase catch and ranking correlation with white-team expert order on a frozen set. Tags go in git before evaluation runs. Amira will not tune thresholds after seeing how her favourite scenarios score. Frozen evaluation sets stop quiet threshold shopping. Threshold shopping after results is treated as a research integrity failure. Integrity failures on thresholds are escalated the same way dual-use slips are.

### 11.4 Handover

Operators run the linter alone; Amira may not type.

Operators run the linter alone; Amira may not type during solo-run week. A freshly created operator account with empty shell history and a sealed envelope of ROE excerpts is the setup. If the operator phones her, the call is logged as a documentation defect. Documentation defects become README patches the same afternoon when possible. Thanking the operator who found a doc defect is part of closing the defect. Closing a doc defect includes the thank-you in the commit message when possible.

### 11.5 Ethics cover

Synthetic-only declaration on page one.

Synthetic-only declaration sits on page one of every project repo. Ethics cover sheets are mechanically checked for the word synthetic before merges accept. Amira's near-miss answers from others stay anonymous; her own near-miss stays named to model candour. Mechanical checks beat trusting authors to remember the word synthetic. Merge hooks do not argue; they reject and cite the ethics cover rule. Authors who forget synthetic meet a reject, not a debate. The reject message cites the ethics cover rule in one line.

### 11.6 Time box

Eight weeks with biweekly checkpoints.

Eight weeks with biweekly checkpoints keep the project inside a specialist time box. Amira refuses open-ended build time that starves catalogue work. Checkpoints quiz non-goals and show whether solo-run readiness is real. Open-ended build time is a catalogue risk, not a gift to the project. Catalogue work keeps its staff even when the project is interesting. Interesting projects do not get to cannibalise the catalogue calendar. Staff time for catalogue reviews is protected in the same calendar as checkpoints.

### 11.7 11.7 Narrative

Checkpoint quizzes ask which non-goal you nearly violated this sprint; Amira answers first with her own near-miss about an LLM summary feature. Ethics cover sheets are mechanically checked for the word synthetic before project repos accept merges. Solo-run week forbids her typing.

Checkpoint quizzes ask which non-goal you nearly violated this sprint; Amira answers first with her own near-miss about an LLM summary feature. Ethics cover sheets are mechanically checked for the word synthetic before project repos accept merges. Solo-run week forbids her typing so operators must succeed from the docs alone.

### 11.8 11.8 Bit

Near-miss answers are stored anonymously when others share; Amira's own near-miss stays named to model candour.

Others' near-miss answers stay anonymous in storage; Amira's own stays named to model candour. Naming her own near-miss signals to juniors that admitting one carries no penalty. Anonymous storage for others prevents the quiz from becoming a fear exercise. Leaders go first on candour so juniors are not the only ones exposed. Candour that only travels downward trains silence upward. Silence upward is the failure mode candour from leaders is meant to prevent.

### 11.9 11.9 Bit2

Near-miss answers are stored anonymously when others share; Amira's own near-miss stays named to model candour. Amira naming her own near-miss signals to juniors that admitting one carries no penalty.

Amira naming her own near-miss signals to juniors that admitting one carries no penalty. She repeats the habit in decision clinics. Candour that only juniors show is not candour; leaders go first. Decision clinics open with a leader near-miss when candour feels costly. Going first is a leadership behaviour scored the same way early stops are praised.

### 11.10 11.10 Story

Solo-run week uses a freshly created operator account with empty shell history and a sealed envelope of ROE excerpts. If the operator phones Amira, the call is logged as a doc defect. Two calls in cohort one became README patches the same afternoon and a thank-you to the operator.

Solo-run week uses a freshly created operator account with empty shell history and a sealed envelope of ROE excerpts. If the operator phones Amira, the call is logged as a doc defect. Two calls in cohort one became README patches the same afternoon and a thank-you to the operator.

### 11.11 11.p10

Sealed envelopes use wax stamps for theatre that reminds people the ROE is special.

Wax stamps on sealed envelopes are theatre that reminds people the ROE is special. The ceremony is deliberate: opening a sealed ROE envelope should feel different from opening routine paperwork. Amira keeps the stamp in the white-team kit. The stamp lives in the white-team kit so the ceremony is repeatable. Repeatable ceremony beats a one-off flourish that nobody can restage. If the stamp is missing, the envelope still seals; the ceremony waits for the kit.

### 11.12 11.q11

Sealed envelopes use wax stamps for theatre that reminds people the ROE is special. The ceremony is deliberate: opening a sealed ROE envelope should feel different from opening routine paperwork.

Opening the sealed ROE envelope is meant to feel unlike routine paperwork, on purpose. Juniors remember the feeling when they later handle production ROEs. Theatre here serves care, not swagger. Production ROE handling is graded on the same care the wax stamp taught. Production ROEs deserve the same care the wax stamp was meant to teach.

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

The portfolio holds decision records, a catalogue page, evidence standards, an ethics charter excerpt, evaluation results, assurance examples, critique notes and the project handover. Amira reviews it once for residual sensitive data. Synthetic examples replace anything that could identify participants. Residual sensitive data is removed before the portfolio is stored. Storage access is limited to supervisors and the named successor during transfer. Named successor access during transfer is revoked when the transfer form is signed.

### 12.2 Transfer

Successor reads DEC-14 and the two-year calendar aloud; Amira answers questions but does not retain secret folklore.

The successor reads DEC-14 and the two-year calendar aloud; Amira answers questions but does not retain secret folklore. Transfer day includes walking introductions to SOC and legal. Email alone is not transfer. The successor's first catalogue update posts under their name with Amira only copied. Visible handoff means the successor's name is on the next catalogue update. Copied only means Amira can answer questions without owning the update.

### 12.3 Research questions

How to measure detection learning across biennial threat-led exercises without exhausting white-team capacity remains open.

How to measure detection learning across biennial threat-led exercises without exhausting white-team capacity remains open. Amira names a watcher and a quarterly invite before she exits. Leaving the question without an owner would make it folklore that dies when she leaves. An open question without a watcher becomes folklore that dies at transfer. Watchers who go silent are replaced in the same way expired acceptances are.

### 12.4 Dual-use

Amira's final slide lists refusals: no public clearing exploit detail, no live demos against participants, no assurance without denominators.

Amira's final slide lists refusals: no public clearing exploit detail, no live demos against participants, no assurance without denominators. Dual-use discipline closes the course the same way it opened integrity in chapter one. She will not trade those refusals for a conference invitation. Conference invitations do not rewrite the refusal list. The refusal list is printed on the final slide and left on the table after she exits.

### 12.5 Next course

AI security (158) is next in the curriculum path.

AI security is next in the curriculum path. Amira tells successors which skills from this course transfer — decision objects, catalogue honesty, assurance language — and which do not. The next course does not grant authority to test real AI systems without a new ROE. Authority to test AI systems requires a new ROE, not this course certificate. Certificate language that implied live AI testing authority is forbidden in the handout. Handout language is linted for implied authority the same way board packs are.

### 12.6 Care

Transfer includes introducing the successor to SOC and legal personally.

Transfer includes introducing the successor to SOC and legal personally. Walking introductions include a five-minute shadow of the SOC stand-up so the successor hears noise-budget language in the wild. Amira will not sign the transfer form without the SOC shadow completed. Personal introductions beat an email that nobody answers in week one. Week-one unanswered email is the failure mode personal introductions exist to prevent. Personal introductions create a face the successor can call when email stalls.

### 12.7 12.7 Narrative

Transfer day includes walking introductions to SOC and legal; email alone is not transfer. Open research questions get named watchers before she exits. The successor's first catalogue update posts under their name with Amira only CC'd — the visible handoff.

Transfer day includes walking introductions to SOC and legal; email alone is not transfer. Open research questions get named watchers before she exits. The successor's first catalogue update posts under their name with Amira only copied — the visible handoff. Folklore ends when names and dates replace hallway advice.

### 12.8 12.8 Bit

Watcher for the open research question receives a quarterly calendar invite with Amira optional — succession of curiosity.

The watcher for the open research question receives a quarterly calendar invite with Amira optional. Succession of curiosity matters. Leaving her optional tests whether the question survives without her steering it. Optional attendance is the test of whether curiosity is institutional. Institutional curiosity shows up on the calendar without her name required. Her name optional is the experiment; the invite itself is the institution.

### 12.9 12.9 Bit2

Watcher for the open research question receives a quarterly calendar invite with Amira optional — succession of curiosity. Leaving Amira optional on the invite tests whether the question survives without her steering it.

Leaving Amira optional on the invite tests whether the question survives without her steering it. If attendance collapses, the watcher escalates to the CISO for a new owner rather than quietly dropping the topic. Curiosity needs governance too. A quiet drop of the research question is escalated as a succession defect.

### 12.10 12.10 Story

Walking introductions include a five-minute shadow of the SOC stand-up so the successor hears noise-budget language in the wild. Amira schedules the shadow even when calendars resist. Transfer without SOC reality is incomplete and she will not sign the transfer form without it.

The walking tour includes five minutes in the SOC stand-up so the successor hears noise-budget language in the wild. Amira schedules the shadow even when calendars resist. Transfer without SOC reality is incomplete, and she will not sign the transfer form without it.

### 12.11 12.p10

Transfer form has a checkbox "SOC shadow completed" that blocks signature when empty.

The transfer form has a checkbox SOC shadow completed that blocks signature when empty. Blocking signature until the shadow is done makes it a precondition rather than a recommendation. Amira has refused to sign when the box was empty despite schedule pressure. Empty checkboxes block signature even when calendars are full. Full calendars are not a reason to skip the SOC shadow precondition. She has walked away from a signature table when the box was empty.

### 12.12 12.q11

Transfer form has a checkbox "SOC shadow completed" that blocks signature when empty. Blocking signature until the SOC shadow is done makes the shadow a precondition rather than a recommendation.

Blocking signature until the SOC shadow is done makes the shadow a precondition rather than a recommendation. The successor and Amira both initial the box. Precondition language is how MCH keeps transfer from becoming a paperwork fiction. Initials on the transfer form without the shadow box checked are rejected.

Initials without the shadow box checked never close transfer at Meridian Clearing House.

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
