# Web3, Blockchain and Cryptoasset Security: Postgraduate Diploma

- Language: English (`en`); course 147, Postgraduate diploma (2 years).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; Two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working practitioners leading blockchain and cryptoasset security decisions inside regulated organisations.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only contracts, wallets and systems you are authorised to assess, on local simulations or test networks; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic ledgers, transactions, contract inventories and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one risk manager guiding a three-institution tokenised-deposit settlement pilot, from decision framing, current practice and specialist evidence, through risk, ethics, design alternatives and controlled evaluation, to integration, difficult cases, assurance, research critique, an applied project and final review. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Nadia Rahman** | Postgraduate student and risk manager | Invented |
| **Professor Mei Tanaka** | Supervisor | Invented |
| **Westbrook Institute** | Fictional institute | Invented |
| **Harbourside Regional Credit Union** | Fictional employer and pilot partner | Invented |

### Core sources

Nakamoto, [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf); Wood, [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf); NIST [IR 8202](https://doi.org/10.6028/NIST.IR.8202); [SWC registry](https://swcregistry.io/); [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/); EEA [EthTrust Security Levels v3](https://entethalliance.org/specs/ethtrust-sl/v3/); [ConsenSys smart contract best practices](https://consensys.github.io/smart-contract-best-practices/); Atzei et al. ([2017](https://doi.org/10.1007/978-3-662-54455-6_8)); Luu et al. ([2016](https://doi.org/10.1145/2976749.2978309)). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Advanced security decision-making

### Learning outcomes

You will (1) frame security decisions under uncertainty; (2) weigh options with explicit criteria; (3) record decisions for later review.

### 1.1 The case and the decision

Nadia Rahman is a risk manager studying part-time for a postgraduate diploma at the fictional Westbrook Institute, supervised by Professor Mei Tanaka. Her employer, the fictional Harbourside Regional Credit Union, is considering a pilot with two partner credit unions to settle inter-bank transfers as tokenised deposits on a shared permissioned ledger. All people, organisations and numbers here are synthetic. Nadia's first task is to frame the decision clearly: whether to join the pilot, under what conditions, and with what safeguards. A well-framed decision names the options, the uncertainties and the people who will bear the consequences.

### 1.2 Criteria and uncertainty

Nadia lists criteria with the credit union's risk committee: settlement speed, operational resilience, control over keys, regulatory acceptability, cost and reversibility of the decision. Several are uncertain: the pilot ledger's resilience is unproven and regulators have not yet commented. She represents uncertainty with ranges rather than single numbers and identifies which uncertainties could change the decision. Reversibility receives a high weight because a pilot that cannot be exited cleanly would turn a small experiment into a lasting dependency. Making criteria explicit lets the committee disagree productively about weights rather than talking past each other.

### 1.3 Recording decisions for review

Nadia drafts a decision record: join the pilot with a capped exposure of 2 million in synthetic settlement value, a six-month term, an exit plan and named conditions for stopping early. The record states the assumptions, the evidence available and what new evidence would change the decision. Professor Tanaka notes that decisions under uncertainty should be judged by the quality of their reasoning, not only by outcomes, since good decisions can turn out badly by chance. Recording reasoning allows the committee to learn honestly when it reviews the pilot later.

### Worked example

Nadia frames the pilot decision with six criteria, high weight on reversibility, and records a capped six-month entry with stop conditions.

> **Synthetic case.** Nadia Rahman, Professor Mei Tanaka, Westbrook Institute, Harbourside Regional Credit Union and all figures are synthetic.

### Errors and limits

Judging a decision only by its outcome confuses bad luck with bad reasoning.

### Exercises

- **EX001 — Pilot purpose.** What would the pilot settle on a shared ledger? *Rubric:* 3 = inter-bank transfers as tokenised deposits;; 2 = tokenised deposits;; 1 = retail payments;; 0 = none.
- **EX002 — Weighted criterion.** Why does reversibility get a high weight? *Rubric:* 3 = an unexitable pilot becomes a lasting dependency;; 2 = exit matters;; 1 = it is cheap;; 0 = none.
- **EX003 — Exposure cap.** What exposure cap does the record set? *Rubric:* 3 = 2 million in synthetic settlement value;; 2 = 2 million;; 1 = unlimited;; 0 = none.
- **EX004 — Pilot term.** How long is the proposed term? *Rubric:* 3 = six months;; 2 = 6 months;; 1 = two years;; 0 = none.
- **EX005 — Judging decisions.** How should decisions under uncertainty be judged? *Rubric:* 3 = by the quality of reasoning, not only outcomes;; 2 = reasoning;; 1 = outcomes only;; 0 = none.

### Synthesis

Explicit criteria, honest uncertainty and recorded reasoning support sound security decisions.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Web3, blockchain and cryptoasset security: current practice

### Learning outcomes

You will (1) survey current guidance for permissioned ledgers; (2) map practice to the pilot; (3) identify gaps between guidance and reality.

### 2.1 Current guidance

Nadia reviews current guidance. NIST IR 8202 describes permissioned and permissionless ledgers, consensus approaches and their trade-offs. The EEA EthTrust Security Levels specification sets requirements for smart contract assurance. The OWASP Smart Contract Top 10 summarises common contract weaknesses, and the ConsenSys best practices give development guidance. She notes that most guidance focuses on contracts and ledgers, while comparatively little addresses governance among institutions sharing a ledger. That imbalance matters for the pilot, where three organisations must agree who operates validators, who controls privileged keys and how disputes are resolved.

### 2.2 Mapping practice to the pilot

Nadia maps guidance to the pilot's components. The settlement contract should meet an agreed EthTrust level verified by an external review. Validators should be operated by each credit union, so no single party can halt settlement. Privileged functions, such as pausing or upgrading the contract, should require approval from at least two institutions with a timelock. She records which guidance applies, how the pilot meets it and what evidence will show it. The mapping becomes a checklist for the risk committee and a basis for negotiating responsibilities with the partners.

### 2.3 Gaps between guidance and reality

Nadia identifies gaps. The partners propose that one vendor host all validators for convenience, which would concentrate operational risk. The draft contract has an upgrade function controlled by the vendor's single key. Incident procedures across the three institutions are not aligned. She records each gap with its risk and a proposed remedy. Gaps between guidance and practice are normal early in a project, and finding them before go-live is far cheaper than after. She presents the gaps neutrally, so partners see them as shared problems rather than criticism of their preparation.

### Worked example

Nadia maps guidance to the pilot and finds three gaps: vendor-hosted validators, a single-key upgrade function and unaligned incident procedures.

> **Synthetic case.** The pilot and partners are synthetic; NIST IR 8202, EEA EthTrust, OWASP SC Top 10 and ConsenSys best practices are real sources.

### Errors and limits

Applying contract-focused guidance alone misses governance risks among institutions sharing a ledger.

### Exercises

- **EX006 — Guidance imbalance.** What does most guidance under-address? *Rubric:* 3 = governance among institutions sharing a ledger;; 2 = governance;; 1 = contracts;; 0 = none.
- **EX007 — Validator operation.** Who should operate validators? *Rubric:* 3 = each credit union;; 2 = each institution;; 1 = one vendor;; 0 = none.
- **EX008 — Privileged approval.** What approval should privileged functions need? *Rubric:* 3 = at least two institutions plus a timelock;; 2 = two institutions;; 1 = vendor key;; 0 = none.
- **EX009 — Concentration gap.** Which proposal concentrates operational risk? *Rubric:* 3 = one vendor hosting all validators;; 2 = vendor hosting;; 1 = multisig;; 0 = none.
- **EX010 — Upgrade gap.** Who controls the draft upgrade function? *Rubric:* 3 = the vendor's single key;; 2 = vendor;; 1 = all three;; 0 = none.

### Synthesis

Mapping current guidance to a real design exposes gaps while they are still cheap to fix.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Web3, blockchain and cryptoasset security: specialist evidence

### Learning outcomes

You will (1) appraise specialist research; (2) judge relevance to permissioned settlement; (3) synthesise evidence for practitioners.

### 3.1 Appraising research

Nadia appraises specialist studies. Atzei and colleagues' 2017 survey classifies contract weaknesses, Luu and colleagues' 2016 paper examines how contracts can depend on conditions outside the developer's control, and Daian and colleagues' 2020 work studies transaction-ordering effects on public chains. For each she notes the question, method, data and limitations. She asks whether findings were measured on public chains with open participation, which differ from the pilot's permissioned setting. Appraisal is about understanding what a study can and cannot support, not about accepting or rejecting it wholesale.

### 3.2 Relevance to permissioned settlement

Some findings transfer directly: weaknesses in contract logic exist whatever the ledger type, so Atzei's classes and the SWC registry remain relevant. Others transfer partly: ordering effects described by Daian depend on open mempools and anonymous block producers, which the pilot lacks, but a dishonest validator operator could still reorder transactions within its turn. Nadia rates each finding as directly, partly or weakly relevant, with a reason. This structured judgement prevents both overreaction to public-chain risks and complacency about risks that still apply among known parties.

### 3.3 Synthesis for practitioners

Nadia writes a two-page synthesis for the risk committee. It explains three evidence-based points: contract logic needs independent review whatever the ledger; ordering risk is reduced but not removed among known validators; and key control remains a central risk. Each point cites its sources and states its confidence. She avoids technical detail that committee members cannot evaluate and avoids any description of how weaknesses could be used. Professor Tanaka notes that good synthesis translates evidence into decisions without distorting it, which is a core skill for senior practitioners.

### Worked example

Nadia rates research relevance to the permissioned pilot and synthesises three points: independent logic review, reduced ordering risk and central key risk.

> **Synthetic case.** The appraisal is synthetic; Atzei et al. (2017), Luu et al. (2016), Daian et al. (2020) and the SWC registry are real sources.

### Errors and limits

Transferring public-chain findings unchanged to permissioned ledgers can overstate or understate risk.

### Exercises

- **EX011 — Appraisal question.** What does Nadia ask about each study's setting? *Rubric:* 3 = whether findings came from public open chains;; 2 = setting;; 1 = author fame;; 0 = none.
- **EX012 — Direct transfer.** Which findings transfer directly? *Rubric:* 3 = contract logic weaknesses;; 2 = logic flaws;; 1 = ordering effects;; 0 = none.
- **EX013 — Partial transfer.** Why does ordering risk only partly transfer? *Rubric:* 3 = pilot lacks open mempools, but a validator could still reorder;; 2 = known validators;; 1 = fully transfers;; 0 = none.
- **EX014 — Synthesis length.** How long is the synthesis for the committee? *Rubric:* 3 = two pages;; 2 = 2 pages;; 1 = fifty pages;; 0 = none.
- **EX015 — Synthesis exclusion.** What does the synthesis deliberately avoid? *Rubric:* 3 = any description of how weaknesses could be used;; 2 = misuse detail;; 1 = citations;; 0 = none.

### Synthesis

Careful appraisal and relevance rating turn specialist research into practical guidance.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Advanced risk and ethics

### Learning outcomes

You will (1) analyse systemic and shared risk; (2) apply ethical reasoning to institutional choices; (3) balance duties to stakeholders.

### 4.1 Systemic and shared risk

A shared settlement ledger links three institutions, so a failure at one can affect all. Nadia analyses shared risks: a compromised validator at one partner, a contract defect affecting all balances, or a dispute about a settlement that the ledger records as final. She separates risks each institution controls from risks that only collective action can reduce. For collective risks she proposes shared controls, such as joint incident procedures and agreed criteria for pausing. Systemic thinking matters because members of all three credit unions could be harmed by one partner's weakness.

### 4.2 Ethical reasoning

Nadia considers ethical questions. Members' transfer data will be visible to all three institutions' validators; is that consistent with members' expectations of confidentiality? A pause would stop settlement for everyone; who has the right to impose that cost? She applies principles of harm avoidance, fairness and transparency. She recommends that only settlement amounts and pseudonymous institution references appear on the ledger, with member details kept in each credit union's own systems, and that pausing require two institutions and a published post-incident explanation to members.

### 4.3 Balancing duties

Nadia's duties pull in different directions: to her employer's commercial interest, to its members, to the partners and to regulators. She records where they conflict, for example between faster settlement and stricter controls that slow it. She recommends resolving conflicts openly through the risk committee, with dissent recorded. Professor Tanaka emphasises that ethical practice includes speaking up when a decision seems wrong and documenting that view. Nadia writes her concerns about the vendor-controlled upgrade key into the committee papers, ensuring the issue is considered rather than quietly accepted.

### Worked example

Nadia separates individual from collective risks, keeps member details off-ledger and records her concern about the vendor upgrade key in committee papers.

> **Synthetic case.** The risks and committee papers are synthetic.

### Errors and limits

Treating shared-ledger risk as each institution's private matter ignores harm that spreads to all members.

### Exercises

- **EX016 — Shared risk example.** Name one shared risk. *Rubric:* 3 = a contract defect affecting all balances;; 2 = compromised partner validator;; 1 = office fire at one branch;; 0 = none.
- **EX017 — Collective control.** What shared control does Nadia propose? *Rubric:* 3 = joint incident procedures;; 2 = agreed pause criteria;; 1 = vague;; 0 = none.
- **EX018 — Ledger data choice.** What appears on the ledger? *Rubric:* 3 = settlement amounts and pseudonymous institution references;; 2 = amounts only;; 1 = member names;; 0 = none.
- **EX019 — Pause condition.** What must accompany any pause? *Rubric:* 3 = two institutions and a published explanation;; 2 = two approvals;; 1 = nothing;; 0 = none.
- **EX020 — Speaking up.** How does Nadia raise the upgrade-key concern? *Rubric:* 3 = writes it into committee papers;; 2 = documents it;; 1 = stays silent;; 0 = none.

### Synthesis

Systemic analysis and ethical reasoning guide fair choices among institutions.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Web3, blockchain and cryptoasset security: design alternatives

### Learning outcomes

You will (1) generate design alternatives; (2) analyse trade-offs; (3) select a design with partners.

### 5.1 Generating alternatives

Nadia and the partners' engineers generate alternatives for three design questions. For validator hosting: one vendor, each institution hosting its own, or a mix with one independent operator. For privileged control: vendor key, institutional multisig, or multisig with timelock. For dispute handling: on-ledger reversal by multisig, or off-ledger compensation with the ledger left final. Generating several options before evaluating any prevents early commitment to the first idea. She records each option's description so all participants share the same understanding before discussion of preferences begins.

### 5.2 Analysing trade-offs

Each option has costs. Self-hosting gives independence but requires skills each credit union must build. A multisig with timelock protects against a single compromised key but slows emergency fixes. On-ledger reversal is convenient but means settlement is never truly final, undermining the pilot's purpose. Nadia scores options against the criteria agreed earlier and highlights where scores depend on uncertain assumptions. She notes that combined choices interact: self-hosting plus multisig spreads control most evenly, while keeping final settlement requires a clear off-ledger compensation agreement among partners.

### 5.3 Selecting with partners

The partners select self-hosted validators with a fourth independent operator, a 2-of-3 institutional multisig with a 48-hour timelock for upgrades, and an immediate pause that requires two institutions. Disputes are settled off-ledger by agreed compensation. The vendor accepts an advisory role without keys. Nadia documents the selection, the alternatives rejected and why. Agreement among partners is as important as technical merit, because a design one partner resents will be weakly supported in practice. The documented reasoning also helps regulators understand the pilot's safeguards.

### Worked example

Partners select four validators including an independent operator, a 2-of-3 multisig with a 48-hour upgrade timelock and off-ledger dispute compensation.

> **Synthetic case.** The design process is synthetic.

### Errors and limits

Choosing the first design proposed prevents comparison with better alternatives.

### Exercises

- **EX021 — Hosting alternatives.** Name one validator hosting alternative. *Rubric:* 3 = each institution hosting its own;; 2 = vendor hosting;; 1 = no validators;; 0 = none.
- **EX022 — Reversal trade-off.** Why reject on-ledger reversal? *Rubric:* 3 = settlement would never be truly final;; 2 = finality;; 1 = too slow;; 0 = none.
- **EX023 — Upgrade timelock.** What timelock applies to upgrades? *Rubric:* 3 = 48 hours;; 2 = 48h;; 1 = vague;; 0 = none.
- **EX024 — Vendor role.** What role does the vendor accept? *Rubric:* 3 = advisory without keys;; 2 = advisory;; 1 = key holder;; 0 = none.
- **EX025 — Validator total.** How many validators does the selected design have? *Rubric:* 3 = four, including an independent operator;; 2 = four;; 1 = three;; 0 = none.

### Synthesis

Generating, analysing and jointly selecting alternatives yields designs partners support.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Web3, blockchain and cryptoasset security: controlled evaluation

### Learning outcomes

You will (1) design a controlled comparison; (2) run it on seeded synthetic data; (3) interpret detection and cost together.

### 6.1 Designing the comparison

Nadia evaluates how settlement batches should be signed off before the multisig signs them. Design A uses one reviewer checking the batch file. Design B uses two reviewers from different institutions and an automatically generated summary showing totals, recipients and whether any transfer repeats an earlier batch. She builds eight synthetic batches, four containing seeded errors of different kinds, and records whether each design catches each error and how long sign-off takes. A controlled comparison on the same batches isolates the effect of the design itself rather than the particular batches each design happened to see.

### Lab — Sign-off design comparison

```python
"""Compare two settlement sign-off designs on seeded synthetic batches (read-only)."""
# batch id, seeded error (None or kind), minutes to sign under A (one reviewer), B (two reviewers + summary)
BATCHES = [
    ("S01", None, 6, 11), ("S02", "amount", 5, 12), ("S03", None, 7, 10),
    ("S04", "duplicate", 6, 13), ("S05", None, 5, 9), ("S06", "recipient", 8, 14),
    ("S07", None, 6, 10), ("S08", "duplicate", 7, 12),
]
CAUGHT_A = {"amount"}                      # single reviewer catches only amount errors
CAUGHT_B = {"amount", "duplicate", "recipient"}

def rate(caught):
    seeded = [b for b in BATCHES if b[1]]
    return sum(1 for b in seeded if b[1] in caught), len(seeded)

def main():
    for name, caught, col in (("A", CAUGHT_A, 2), ("B", CAUGHT_B, 3)):
        hit, n = rate(caught)
        mins = sorted(b[col] for b in BATCHES)
        median = (mins[3] + mins[4]) / 2
        print(f"design {name}: caught {hit}/{n}; median sign-off {median} min")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_signoff.py`. Verified output:

```text
design A: caught 1/4; median sign-off 6.0 min
design B: caught 4/4; median sign-off 11.5 min
```

### 6.2 Interpreting results

The lab shows design A catching 1 of 4 seeded errors with a median sign-off time of 6 minutes, and design B catching all 4 with a median of 11.5 minutes. Design B nearly doubles the time but catches the duplicate and recipient errors that a lone reviewer missed. Nadia notes that the results come from eight synthetic batches and seeded errors chosen by her, so they show the mechanism rather than precise real-world rates. She recommends design B and a later measurement on real pilot batches to confirm that time and detection behave similarly.

### 6.3 Cost and detection together

Reporting only detection would favour design B without question; reporting only time would favour A. Nadia presents both and estimates the cost: with about 40 batches a week, design B adds roughly three hours of reviewer time weekly across the institutions. The committee judges this worthwhile given settlement values. She also notes that the summary, not just the second reviewer, likely drives detection of duplicates, which suggests a cheaper option to test later: one reviewer with the summary. Interpreting results together with cost keeps evaluation useful for real decisions.

### Worked example

Design B catches 4 of 4 seeded errors at a median 11.5 minutes against A's 1 of 4 at 6 minutes, adding about three reviewer hours a week.

> **Synthetic case.** The batches, errors and times are synthetic.

### Errors and limits

Presenting detection without cost, or cost without detection, biases the decision.

### Exercises

- **EX026 — Design B description.** What does design B add? *Rubric:* 3 = two reviewers from different institutions and a summary;; 2 = two reviewers;; 1 = nothing;; 0 = none.
- **EX027 — Detection results.** How many errors do A and B catch? *Rubric:* 3 = A 1 of 4, B 4 of 4;; 2 = 1/4 and 4/4;; 1 = both 4;; 0 = none.
- **EX028 — Median times.** What are the median sign-off times? *Rubric:* 3 = 6 and 11.5 minutes;; 2 = 6/11.5;; 1 = equal;; 0 = none.
- **EX029 — Weekly cost.** What weekly cost does design B add? *Rubric:* 3 = about three hours of reviewer time;; 2 = three hours;; 1 = vague;; 0 = none.
- **EX030 — Cheaper variant.** What cheaper option is suggested for later testing? *Rubric:* 3 = one reviewer with the summary;; 2 = summary only;; 1 = no review;; 0 = none.

### Synthesis

Controlled comparison on seeded data shows mechanisms, and cost-aware interpretation guides choice.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Web3, blockchain and cryptoasset security: organizational integration

### Learning outcomes

You will (1) integrate ledger controls with existing processes; (2) assign responsibilities across institutions; (3) train staff.

### 7.1 Integrating with existing processes

The credit union already has payment controls, incident management and change management. Nadia integrates the pilot into them rather than creating parallel processes. Settlement batches enter the existing payment approval workflow, ledger incidents use the existing incident system with a new category, and contract or validator changes go through the change advisory board. Integration avoids a separate, less mature process that staff might not follow. She lists each place where ledger work touches an existing process and agrees the handoff with the process owner, recording the agreement.

### 7.2 Responsibilities across institutions

Nadia drafts a responsibility matrix with the partners. Each institution operates its validator, monitors its own node and holds one multisig key. The independent operator runs the fourth validator and publishes availability reports. A joint operations group meets weekly during the pilot. For each activity the matrix names who is responsible, who approves, who is consulted and who is informed. Ambiguous responsibility is a common source of failure in shared systems, because everyone assumes someone else is watching. The partners sign the matrix as an annex to the pilot agreement.

### 7.3 Training staff

Payment operations staff need to understand the new batch summary, reviewers need to know what errors to look for and keyholders need to practise signing with hardware devices. Nadia designs short training sessions with exercises on synthetic batches. She measures training by having each participant review a seeded batch; all twelve participants catch the seeded duplicate after training, compared with five of twelve before. She records attendance and results. Training is a control, and measuring it shows whether it works, just as testing any technical control would.

### Worked example

Nadia embeds the pilot in existing workflows, signs a cross-institution responsibility matrix and raises duplicate detection from 5 of 12 to 12 of 12 staff through training.

> **Synthetic case.** The processes, matrix and training results are synthetic.

### Errors and limits

Creating parallel processes for new technology produces controls staff do not follow.

### Exercises

- **EX031 — Incident integration.** How are ledger incidents handled? *Rubric:* 3 = in the existing incident system with a new category;; 2 = existing system;; 1 = separate process;; 0 = none.
- **EX032 — Independent operator duty.** What does the independent operator publish? *Rubric:* 3 = availability reports;; 2 = reports;; 1 = keys;; 0 = none.
- **EX033 — Matrix roles.** What four roles does the matrix name? *Rubric:* 3 = responsible, approves, consulted, informed;; 2 = RACI;; 1 = owner only;; 0 = none.
- **EX034 — Training baseline.** How many caught the duplicate before training? *Rubric:* 3 = five of twelve;; 2 = 5/12;; 1 = twelve;; 0 = none.
- **EX035 — Training outcome.** How many caught it after training? *Rubric:* 3 = all twelve;; 2 = 12/12;; 1 = six;; 0 = none.

### Synthesis

Integration, clear responsibilities and measured training make ledger controls part of normal work.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Web3, blockchain and cryptoasset security: difficult cases

### Learning outcomes

You will (1) analyse ambiguous situations; (2) decide under time pressure; (3) learn from near misses.

### 8.1 An ambiguous alert

In a synthetic scenario, monitoring shows a partner's validator signing blocks with a delay of several seconds and a small settlement batch appears twice in the pending queue. It could be a network fault, a misconfigured retry or something more serious. Nadia's team must decide whether to pause. She uses the joint procedure: gather facts quickly, contact the partner's operations lead, check whether the duplicate would pass the batch summary's repeat check, and decide within thirty minutes. Ambiguous situations are where procedures matter most, because they replace panic with a sequence of known steps.

### 8.2 Deciding under time pressure

Within twenty minutes the partner confirms a network fault causing retries, and the batch summary flags the duplicate, so reviewers reject it. The team decides not to pause, because the control worked and pausing would delay all settlement. Nadia records the decision, the facts known at the time and the reasoning. Under time pressure, decisions should be proportionate: pausing is a strong action with real costs. She notes that if the duplicate had not been flagged, or the partner had been unreachable, the procedure would have favoured pausing until facts were clearer.

### 8.3 Learning from near misses

The near miss reveals that the partner's retry setting could produce duplicates, and that only the batch summary stopped one reaching signing. Nadia leads a blameless review. Improvements include a contract-level check rejecting any transfer identifier already settled, and alignment of retry settings across partners. Near misses are valuable because they reveal weaknesses without causing harm. She reports the near miss to the joint operations group and the risk committee, which reinforces a culture where people report problems early instead of hiding them out of embarrassment.

### Worked example

A duplicate from a partner's retry is caught by the batch summary, the team decides not to pause, and a contract-level duplicate check is added.

> **Synthetic case.** The scenario and response are synthetic.

### Errors and limits

Pausing reflexively on every ambiguous alert imposes costs that a working control may have made unnecessary.

### Exercises

- **EX036 — Decision deadline.** Within what time must the team decide? *Rubric:* 3 = thirty minutes;; 2 = 30 minutes;; 1 = one day;; 0 = none.
- **EX037 — Fault cause.** What caused the duplicate in the scenario? *Rubric:* 3 = a network fault causing retries;; 2 = retries;; 1 = theft;; 0 = none.
- **EX038 — Pause decision.** Why does the team not pause? *Rubric:* 3 = the control worked and pausing would delay everything;; 2 = proportionality;; 1 = forgot;; 0 = none.
- **EX039 — Contract improvement.** What contract improvement follows? *Rubric:* 3 = reject any transfer identifier already settled;; 2 = duplicate check;; 1 = vague;; 0 = none.
- **EX040 — Near-miss value.** Why are near misses valuable? *Rubric:* 3 = they reveal weaknesses without harm;; 2 = learning;; 1 = they are not;; 0 = none.

### Synthesis

Clear procedures, proportionate decisions and near-miss learning handle difficult cases well.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Web3, blockchain and cryptoasset security: leadership and assurance

### Learning outcomes

You will (1) lead assurance across partners; (2) commission independent review; (3) report assurance to governing bodies.

### 9.1 Leading assurance

Nadia leads an assurance plan for the pilot. It defines what must be assured: contract correctness, key control, validator resilience, operational procedures and data protection. For each area it names the evidence: external review reports, key ceremony records, availability data, drill results and data maps. Leadership means coordinating partners who have different priorities and making sure assurance work is done and shared, not duplicated or missed. She chairs a monthly assurance meeting and keeps a shared evidence register that all three institutions can read and contribute to.

### 9.2 Commissioning independent review

The partners commission an external review of the settlement contract against an agreed EthTrust level. Nadia writes the scope: contract code, deployment configuration and privileged roles, but not partner networks. She asks reviewers to report findings with severity and evidence and to retest fixes. The review finds two medium findings and one low, all fixed and retested before go-live. She notes the EthTrust caution that no review guarantees the absence of weaknesses, and explains it to the committee so they understand what the review does and does not provide.

### 9.3 Reporting to governing bodies

Nadia reports assurance quarterly to each institution's board risk committee. The report summarises status by area, open findings, incidents and near misses, and key metrics such as availability and sign-off detection. It states residual risks and asks for decisions where needed. Each report uses the same structure, so trends are visible. Boards appreciate concise reports that separate facts from judgements. Professor Tanaka notes that assurance reporting is ultimately about enabling governance: boards cannot oversee risks they do not understand, and the report's job is to make them understandable.

### Worked example

Nadia's assurance plan covers five areas, the external review's two medium and one low findings are fixed before go-live, and boards get quarterly reports.

> **Synthetic case.** The assurance plan, review and reports are synthetic; EEA EthTrust is a real source.

### Errors and limits

Presenting an external review as a guarantee overstates what assurance provides.

### Exercises

- **EX041 — Assurance areas.** Name one assurance area. *Rubric:* 3 = validator resilience;; 2 = key control;; 1 = marketing;; 0 = none.
- **EX042 — Review scope exclusion.** What is excluded from the review scope? *Rubric:* 3 = partner networks;; 2 = networks;; 1 = contract code;; 0 = none.
- **EX043 — Review findings.** What did the external review find? *Rubric:* 3 = two medium and one low;; 2 = three findings;; 1 = vague;; 0 = none.
- **EX044 — Reporting rhythm.** How often are boards briefed? *Rubric:* 3 = quarterly;; 2 = every quarter;; 1 = yearly;; 0 = none.
- **EX045 — Report purpose.** What is assurance reporting ultimately for? *Rubric:* 3 = enabling governance;; 2 = oversight;; 1 = decoration;; 0 = none.

### Synthesis

Coordinated assurance, scoped independent review and clear reporting enable governance.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Research reading and critique

### Learning outcomes

You will (1) read research critically; (2) evaluate methods and claims; (3) identify implications for practice.

### 10.1 Reading critically

Nadia reads Perez and Livshits' 2021 study, which examined whether weaknesses reported by analysis tools in deployed contracts were actually exploited, and found that only a small fraction were. She identifies the question, data, method, results and the authors' stated limitations. She asks how exploitation was measured, what might be missed, and whether the contracts studied resemble the pilot's settlement contract. Critical reading is careful, not cynical: its aim is to understand how far a study's conclusions can be trusted and applied, using the evidence the authors present.

### 10.2 Evaluating methods and claims

The study's strength is its use of large-scale on-chain data rather than assumptions. Its limitations include the difficulty of detecting all exploitation from public data and the focus on public chains. Nadia also reads Durieux and colleagues' 2020 evaluation of analysis tools and Tsankov and colleagues' 2018 work on property-based analysis. Together they suggest that tool findings need contextual triage. She writes a critique noting that the claim is well supported for public contracts in the period studied, and less certain for private settlement contracts with different users and incentives.

### 10.3 Implications for practice

Nadia draws implications for the pilot. Tool output should be triaged by reviewers who understand the contract's context, not treated as a list of urgent defects. Equally, unexploited does not mean unexploitable, so findings in privileged functions should still be fixed. She proposes a triage rule: any finding affecting privileged roles or settlement amounts is fixed before deployment; others are assessed and documented. Professor Tanaka praises the balance between using evidence and avoiding over-generalisation. The rule is adopted by the joint operations group for future changes.

### Worked example

Nadia critiques Perez and Livshits, combines it with Durieux and Tsankov, and proposes fixing all findings touching privileged roles or settlement amounts before deployment.

> **Synthetic case.** The critique and rule are synthetic; Perez and Livshits (2021), Durieux et al. (2020) and Tsankov et al. (2018) are real sources.

### Errors and limits

Reading unexploited as unexploitable leads to ignoring findings that still matter.

### Exercises

- **EX046 — Study finding.** What did Perez and Livshits find? *Rubric:* 3 = only a small fraction of reported weaknesses were exploited;; 2 = few exploited;; 1 = all exploited;; 0 = none.
- **EX047 — Study strength.** What is the study's main strength? *Rubric:* 3 = large-scale on-chain data;; 2 = real data;; 1 = interviews;; 0 = none.
- **EX048 — Study limitation.** Name one limitation Nadia notes. *Rubric:* 3 = hard to detect all exploitation from public data;; 2 = public chains only;; 1 = vague;; 0 = none.
- **EX049 — Triage rule.** What does the triage rule require? *Rubric:* 3 = fix privileged-role and settlement findings before deployment;; 2 = fix critical ones;; 1 = ignore tools;; 0 = none.
- **EX050 — Over-generalisation caution.** Why fix findings even if unexploited elsewhere? *Rubric:* 3 = unexploited does not mean unexploitable;; 2 = still possible;; 1 = tidiness;; 0 = none.

### Synthesis

Critical reading turns research into balanced, context-aware practice rules.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Applied project

### Learning outcomes

You will (1) plan and execute an applied evaluation; (2) measure validator availability; (3) present results with caveats.

### 11.1 Planning the project

For her applied project, Nadia evaluates whether the pilot's four-validator design meets its availability target of 99.5 percent over a month, given that settlement needs three of four validators to agree. She gathers synthetic outage logs for each validator and writes a read-only script that counts hours when fewer than three validators were up. She also asks whether outages at different validators overlapped, because overlapping outages are what break the quorum. The project's value lies in testing a design assumption with data rather than relying on the vendor's assurances.

### Lab — Quorum availability from outage logs

```python
"""Count hours a 3-of-4 validator quorum was unavailable from synthetic outage logs (read-only)."""
# validator: list of (start_hour, end_hour) outages within a 720-hour month
OUTAGES = {
    "v1": [(100, 104), (400, 402)], "v2": [(102, 106)],
    "v3": [(401, 403), (600, 601)], "v4": [(650, 655)],
}
HOURS, QUORUM = 720, 3

def main():
    lost = 0
    for h in range(HOURS):
        up = sum(1 for spans in OUTAGES.values() if not any(s <= h < e for s, e in spans))
        if up < QUORUM:
            lost += 1
    print(f"validators {len(OUTAGES)}; quorum {QUORUM}; unavailable hours {lost}/{HOURS}")
    print(f"availability {100 * (HOURS - lost) / HOURS:.2f}%")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_quorum.py`. Verified output:

```text
validators 4; quorum 3; unavailable hours 3/720
availability 99.58%
```

### 11.2 Results and interpretation

The lab finds 3 unavailable hours out of 720, giving 99.58 percent availability, just above the 99.5 percent target. Two of the lost hours came from overlapping outages at validators one and two, and one from overlap at validators one and three. Nadia notes that validator one appears in both overlaps. She investigates and finds that its maintenance windows were scheduled without checking other partners' plans. Results meeting a target narrowly deserve attention: a small change, such as one more overlapping outage, would have missed it. She recommends coordinated maintenance windows across partners.

### 11.3 Presenting with caveats

Nadia presents results to the joint operations group with caveats: one month of synthetic data, hourly resolution that may hide shorter gaps, and no measurement of degraded performance short of full outage. She recommends collecting minute-level data and repeating the analysis quarterly. The group agrees a shared maintenance calendar, so no two validators are planned to be down together. Presenting caveats honestly lets the group act on the finding without over-trusting a narrow pass. Professor Tanaka grades the project highly for linking data, design assumption and operational change.

### Worked example

The quorum lab finds 3 of 720 hours unavailable (99.58 percent), both overlaps involve validator one, and partners adopt a shared maintenance calendar.

> **Synthetic case.** The outage logs and results are synthetic.

### Errors and limits

Accepting a narrow pass without examining causes misses easy improvements and hidden fragility.

### Exercises

- **EX051 — Availability target.** What availability target applies? *Rubric:* 3 = 99.5 percent;; 2 = 99.5%;; 1 = 100 percent;; 0 = none.
- **EX052 — Quorum size.** How many validators must agree? *Rubric:* 3 = three of four;; 2 = 3 of 4;; 1 = two of four;; 0 = none.
- **EX053 — Measured availability.** What availability does the lab report? *Rubric:* 3 = 99.58 percent, 3 of 720 hours lost;; 2 = 99.58%;; 1 = 95 percent;; 0 = none.
- **EX054 — Common factor.** Which validator appears in both overlaps? *Rubric:* 3 = validator one;; 2 = v1;; 1 = validator four;; 0 = none.
- **EX055 — Operational change.** What change do partners adopt? *Rubric:* 3 = a shared maintenance calendar;; 2 = coordinated maintenance;; 1 = more validators;; 0 = none.

### Synthesis

Testing design assumptions with data, and reporting caveats, drives practical improvements.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Final review and transfer

### Learning outcomes

You will (1) review the pilot against its objectives; (2) transfer learning to the organisation; (3) plan next steps.

### 12.1 Reviewing the pilot

At the end of six months Nadia reviews the pilot against the original decision record. Settlement time fell from hours to minutes; availability averaged 99.7 percent; no settlement losses occurred; one near miss and two minor incidents were handled under the joint procedures; and the exit plan was tested in a desk exercise. Assumptions are compared with outcomes: the expected training burden was underestimated, while operational costs were close to forecast. She presents successes and shortcomings together, because a review that only celebrates teaches the organisation nothing new.

### 12.2 Transferring learning

Nadia captures lessons in a short guide for the credit union: frame decisions with reversibility in mind, insist on distributed control of privileged functions, embed ledger work in existing processes, measure training and controls, and coordinate shared operations. She runs a workshop for colleagues in other departments and adds the guide to the institution's knowledge base. Transfer matters because projects end and people move on, but organisations must retain what they learned. Professor Tanaka notes that transferable lessons are stated generally enough to apply beyond the pilot.

### 12.3 Next steps

The risk committee decides to extend the pilot for a year with a higher exposure cap, conditional on minute-level availability monitoring, the contract-level duplicate check and a second external review. Nadia writes the conditions into a new decision record with review dates. She also completes her diploma with a reflective essay on leading security decisions across institutions. Reflecting on the programme, she notes that the hardest problems were not technical but about aligning partners. Her final submission links every recommendation to evidence gathered during the pilot and the course.

### Worked example

The six-month review shows minutes-level settlement, 99.7 percent availability and no losses, and the pilot is extended with three conditions.

> **Synthetic case.** The pilot results and decisions are synthetic.

### Errors and limits

A review that reports only successes prevents the organisation from learning.

### Exercises

- **EX056 — Average availability.** What was average availability over six months? *Rubric:* 3 = 99.7 percent;; 2 = 99.7%;; 1 = 90 percent;; 0 = none.
- **EX057 — Underestimated assumption.** Which assumption was underestimated? *Rubric:* 3 = the training burden;; 2 = training;; 1 = costs;; 0 = none.
- **EX058 — Extension condition.** Name one condition for extending the pilot. *Rubric:* 3 = a second external review;; 2 = minute-level monitoring;; 1 = vague;; 0 = none.
- **EX059 — Lesson example.** Name one transferable lesson. *Rubric:* 3 = distributed control of privileged functions;; 2 = embed in processes;; 1 = trust vendors;; 0 = none.
- **EX060 — Hardest problems.** What did Nadia find hardest? *Rubric:* 3 = aligning partners;; 2 = governance;; 1 = coding;; 0 = none.

### Synthesis

Honest review, transferable lessons and conditional next steps complete a postgraduate project.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Nadia Rahman, Professor Mei Tanaka, Westbrook Institute, Harbourside Regional Credit Union and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Inter-bank transfers between three credit unions as tokenised deposits.

**EX002.** A pilot that cannot be exited cleanly becomes a lasting dependency.

**EX003.** A cap of 2 million in synthetic settlement value.

**EX004.** Six months.

**EX005.** By the quality of their reasoning, not only their outcomes.

**EX006.** Governance among multiple institutions sharing one ledger.

**EX007.** Each credit union, so no single party can halt settlement.

**EX008.** Approval from at least two institutions, with a timelock.

**EX009.** One vendor hosting all validators.

**EX010.** The vendor's single key.

**EX011.** Whether findings were measured on public chains with open participation.

**EX012.** Contract logic weaknesses such as Atzei's classes and the SWC registry.

**EX013.** The pilot lacks open mempools and anonymous producers, yet a dishonest validator could still reorder.

**EX014.** Two pages.

**EX015.** Any description of how weaknesses could be used, and unevaluable detail.

**EX016.** A compromised partner validator, a contract defect or a settlement dispute.

**EX017.** Joint incident procedures and agreed pausing criteria.

**EX018.** Settlement amounts with pseudonymous institution references only.

**EX019.** Approval by two institutions and a published post-incident explanation.

**EX020.** She writes it into the risk committee papers.

**EX021.** One vendor, each institution, or a mix with an independent operator.

**EX022.** It means settlement is never truly final, undermining the pilot.

**EX023.** A 48-hour timelock under a 2-of-3 institutional multisig.

**EX024.** An advisory role without any keys.

**EX025.** Four, three institutional plus one independent operator.

**EX026.** Two reviewers from different institutions plus an automatic batch summary.

**EX027.** Design A caught 1 of 4 and design B caught 4 of 4.

**EX028.** 6 minutes for A and 11.5 minutes for B.

**EX029.** Roughly three extra reviewer hours across institutions each week.

**EX030.** A single reviewer using the automatic summary.

**EX031.** In the existing incident system under a new category.

**EX032.** Availability reports for the fourth validator.

**EX033.** Who is responsible, who approves, who is consulted and who is informed.

**EX034.** Five of twelve participants.

**EX035.** All twelve participants.

**EX036.** Within thirty minutes.

**EX037.** A network fault at the partner causing retries.

**EX038.** The batch summary caught the duplicate, and pausing would delay all settlement.

**EX039.** A check rejecting any transfer identifier that has already settled.

**EX040.** They reveal weaknesses before any harm occurs.

**EX041.** Contract correctness, key control, validator resilience, procedures or data protection.

**EX042.** The partners' own networks.

**EX043.** Two medium findings and one low, all fixed and retested.

**EX044.** Quarterly, to each institution's board risk committee.

**EX045.** Enabling boards to understand and govern the risks.

**EX046.** Only a small fraction of tool-reported weaknesses were actually exploited.

**EX047.** Its use of large-scale on-chain data.

**EX048.** Difficulty detecting all exploitation from public data, and focus on public chains.

**EX049.** Findings affecting privileged roles or settlement amounts are fixed before deployment.

**EX050.** Because unexploited does not mean unexploitable.

**EX051.** 99.5 percent over a month.

**EX052.** Three of the four validators.

**EX053.** 99.58 percent, with 3 of 720 hours unavailable.

**EX054.** Validator one.

**EX055.** A shared maintenance calendar so no two validators are down together.

**EX056.** 99.7 percent.

**EX057.** The training burden.

**EX058.** Minute-level monitoring, the duplicate check or a second external review.

**EX059.** Reversibility, distributed control, embedding in processes, measured controls or coordinated operations.

**EX060.** Aligning partners rather than technical problems.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Atzei, N., Bartoletti, M., & Cimoli, T. (2017). A survey of attacks on Ethereum smart contracts (SoK). In *Principles of Security and Trust (POST 2017)*, LNCS 10204, 164–186. Springer. <https://doi.org/10.1007/978-3-662-54455-6_8>
- Buterin, V. (2014). *Ethereum whitepaper: A next-generation smart contract and decentralized application platform*. ethereum.org. <https://ethereum.org/en/whitepaper/>
- ConsenSys Diligence. (n.d.). *Ethereum smart contract security best practices*. <https://consensys.github.io/smart-contract-best-practices/>
- Daian, P., Goldfeder, S., Kell, T., Li, Y., Zhao, X., Bentov, I., Breidenbach, L., & Juels, A. (2020). Flash Boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability. *2020 IEEE Symposium on Security and Privacy*, 910–927. <https://doi.org/10.1109/SP40000.2020.00040>
- Durieux, T., Ferreira, J. F., Abreu, R., & Cruz, P. (2020). Empirical review of automated analysis tools on 47,587 Ethereum smart contracts. *Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering*, 530–541. <https://doi.org/10.1145/3377811.3380364>
- Enterprise Ethereum Alliance. (2025). *EEA EthTrust Security Levels specification, version 3*. <https://entethalliance.org/specs/ethtrust-sl/v3/>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Luu, L., Chu, D.-H., Olickel, H., Saxena, P., & Hobor, A. (2016). Making smart contracts smarter. *Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security*, 254–269. <https://doi.org/10.1145/2976749.2978309>
- Nakamoto, S. (2008). *Bitcoin: A peer-to-peer electronic cash system*. <https://bitcoin.org/bitcoin.pdf>
- OWASP Foundation. (n.d.). *OWASP Smart Contract Top 10*. <https://owasp.org/www-project-smart-contract-top-10/>
- Perez, D., & Livshits, B. (2021). Smart contract vulnerabilities: Vulnerable does not imply exploited. *30th USENIX Security Symposium*. <https://www.usenix.org/conference/usenixsecurity21/presentation/perez>
- SmartContractSecurity. (n.d.). *Smart Contract Weakness Classification (SWC) registry*. <https://swcregistry.io/>
- Tsankov, P., Dan, A., Drachsler-Cohen, D., Gervais, A., Bünzli, F., & Vechev, M. (2018). Securify: Practical security analysis of smart contracts. *Proceedings of the 2018 ACM SIGSAC Conference on Computer and Communications Security*, 67–82. <https://doi.org/10.1145/3243734.3243780>
- Wood, G. (n.d.). *Ethereum: A secure decentralised generalised transaction ledger* (Ethereum yellow paper, continuously revised). <https://ethereum.github.io/yellowpaper/paper.pdf>
- Yaga, D., Mell, P., Roby, N., & Scarfone, K. (2018). *Blockchain technology overview* (NIST IR 8202). NIST. <https://doi.org/10.6028/NIST.IR.8202>
