# Web3, Blockchain and Cryptoasset Security: Professional Programme

- Language: English (`en`); course 032, Professional programme (6 months).
- Editorial state: **published**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; Two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working practitioners in finance, IT or operations who must safeguard cryptoassets their organisation already holds.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only contracts, wallets and systems you are authorised to assess, on local simulations or test networks; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic ledgers, transactions, contract inventories and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one charity systems officer safeguarding cryptoasset donations held in a multi-signature treasury, from security foundations, service context and authorised practice, through custody review, reconciliation, workflow and controls, to case analysis, reporting, quality, a supervised laboratory and a final portfolio. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Marcus Delgado** | IT and finance systems officer | Invented |
| **Ms Ingrid Holm** | Supervisor | Invented |
| **Kestrel Professional Academy** | Fictional training provider | Invented |
| **Bayview Charity Network** | Fictional employer | Invented |

### Core sources

Nakamoto, [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf); Wood, [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf); NIST [IR 8202](https://doi.org/10.6028/NIST.IR.8202); [SWC registry](https://swcregistry.io/); [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/); EEA [EthTrust Security Levels v3](https://entethalliance.org/specs/ethtrust-sl/v3/); [ConsenSys smart contract best practices](https://consensys.github.io/smart-contract-best-practices/); Atzei et al. ([2017](https://doi.org/10.1007/978-3-662-54455-6_8)); Luu et al. ([2016](https://doi.org/10.1145/2976749.2978309)). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) apply core security principles at work; (2) relate them to cryptoasset custody; (3) set personal practice standards.

### 1.1 The case and the role

Marcus Delgado is an IT and finance systems officer taking a six-month professional programme at the fictional Kestrel Professional Academy, supervised by Ms Ingrid Holm. His employer, the fictional Bayview Charity Network, has begun accepting cryptoasset donations into a multi-signature treasury wallet and converting them to local currency monthly. Every person, address and figure here is synthetic. Marcus already manages the charity's accounts and servers, and the programme helps him apply security principles to this new area responsibly, without pretending he must become a blockchain developer to do so.

### 1.2 Core principles

Marcus revisits core principles: confidentiality, integrity and availability; least privilege; defence in depth; separation of duties; and accountability. He applies them to donations. Integrity means every donation received is recorded correctly; separation of duties means the person recording donations is not the only person who can move funds; least privilege means signers can approve payments but cannot change the signer list alone. He writes one sentence for each principle explaining how it applies at Bayview. The exercise turns familiar principles into concrete expectations for a new kind of asset.

### 1.3 Practice standards

Ms Holm asks each participant to set personal practice standards. Marcus commits to: acting only within written authorisation, keeping evidence of his checks, never handling signing keys on general-purpose computers, reporting problems promptly and honestly, and asking for help when a task exceeds his knowledge. He shares the standards with his manager. Professional standards protect the practitioner and the organisation, especially in an area where mistakes can move funds irreversibly. Writing them down early makes them easier to follow when work becomes busy or pressured.

### Worked example

Marcus maps five principles to Bayview's donations, such as separating recording from fund movement, and sets five personal practice standards.

> **Synthetic case.** Marcus Delgado, Ms Ingrid Holm, Kestrel Professional Academy, Bayview Charity Network and all figures are synthetic.

### Errors and limits

Treating cryptoassets as needing entirely new principles ignores well-tested security foundations.

### Exercises

- **EX001 — Donation flow.** What happens to cryptoasset donations at Bayview? *Rubric:* 3 = held in a multisig treasury and converted monthly;; 2 = multisig and conversion;; 1 = spent directly;; 0 = none.
- **EX002 — Separation applied.** How is separation of duties applied? *Rubric:* 3 = the recorder is not the only one who can move funds;; 2 = different people;; 1 = one person does all;; 0 = none.
- **EX003 — Least privilege applied.** What can signers not do alone? *Rubric:* 3 = change the signer list;; 2 = alter signers;; 1 = approve payments;; 0 = none.
- **EX004 — Personal standard.** Name one of Marcus's standards. *Rubric:* 3 = never handle signing keys on general-purpose computers;; 2 = act within authorisation;; 1 = work alone;; 0 = none.
- **EX005 — Standards purpose.** Why do written standards matter here? *Rubric:* 3 = mistakes can move funds irreversibly;; 2 = irreversibility;; 1 = they do not;; 0 = none.

### Synthesis

Familiar principles, applied concretely and backed by personal standards, ground cryptoasset work.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Web3, blockchain and cryptoasset security: service and stakeholder context

### Learning outcomes

You will (1) describe the donation service end to end; (2) identify stakeholders and their needs; (3) understand the regulatory context at a high level.

### 2.1 The donation service

Marcus maps the service: donors send cryptoassets to a published address; the treasury wallet, a 2-of-3 multi-signature arrangement held by the finance lead, the director and a trustee, receives them; the finance team records each donation with a receipt; once a month signers approve a transfer to a regulated exchange account; the exchange converts to local currency and pays the charity's bank account. He notes each step's owner and records. Seeing the end-to-end service shows where security matters beyond the ledger: publishing the correct address, recording donations, approving transfers and dealing with the exchange.

### 2.2 Stakeholders

Stakeholders include donors, who want their gifts to reach the charity; trustees, who are accountable for funds; the finance team; the exchange; auditors; and regulators. Marcus interviews the finance lead and a trustee. The trustee's main worry is a mistaken transfer that cannot be reversed; the finance lead worries about recording donations correctly for tax receipts. Each concern points to a control. Understanding stakeholders' needs helps Marcus prioritise and explain security work in terms that matter to the people who must approve and fund it.

### 2.3 Regulatory context

Marcus learns, at a high level, that rules for cryptoassets vary by country and change frequently, and that charities have duties around donor identity, record keeping and the prevention of misuse of funds. He does not attempt legal analysis himself. Instead he lists questions for the charity's legal adviser: what records must be kept, what checks apply to large donations and what reporting is required. NIST IR 8202 provides technical background but not legal guidance. Recognising the limits of one's expertise is part of professional practice.

### Worked example

Marcus maps the service from published address to bank account and lists legal questions for the adviser rather than attempting legal analysis.

> **Synthetic case.** The service, interviews and context are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Attempting legal conclusions without expertise risks wrong compliance decisions.

### Exercises

- **EX006 — Treasury signers.** Who holds the treasury signing roles? *Rubric:* 3 = finance lead, director and a trustee;; 2 = three officers;; 1 = one person;; 0 = none.
- **EX007 — Conversion route.** How are donations converted? *Rubric:* 3 = through a regulated exchange account to the bank;; 2 = exchange;; 1 = cash;; 0 = none.
- **EX008 — Trustee worry.** What worries the trustee most? *Rubric:* 3 = an irreversible mistaken transfer;; 2 = irreversibility;; 1 = slow website;; 0 = none.
- **EX009 — Finance worry.** What worries the finance lead? *Rubric:* 3 = recording donations correctly for receipts;; 2 = recording;; 1 = fees;; 0 = none.
- **EX010 — Legal approach.** How does Marcus handle legal questions? *Rubric:* 3 = lists them for the legal adviser;; 2 = refers them;; 1 = decides himself;; 0 = none.

### Synthesis

An end-to-end service view and stakeholder needs focus security work where it matters.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) obtain and follow written authorisation; (2) handle evidence with integrity; (3) respect privacy of donors.

### 3.1 Written authorisation

Before reviewing the treasury setup, Marcus obtains written authorisation from the director describing the scope: read-only review of the treasury configuration and transaction history, the donation records and procedures, using synthetic test transactions on a test network where testing is needed. It excludes moving any real funds, contacting donors and testing the exchange's systems. The document names who to contact if he finds something urgent. Authorisation protects Marcus and the charity, and it clarifies expectations so that everyone knows what he will and will not do.

### 3.2 Handling evidence

Marcus collects evidence directly from sources: transaction history exported from a block explorer for the treasury address, configuration screenshots from the multisig interface and donation records from the finance system. He records the time, source and method for each and stores a SHA-256 hash of every exported file. He keeps evidence in a restricted folder. If his findings later matter in an audit or dispute, he can show exactly what he saw and when. Evidence handling is a professional discipline, not a technical extra.

### 3.3 Respecting donor privacy

Donation records include names and contact details. Marcus uses only what he needs: for reconciliation he works with receipt numbers, amounts and transaction references, not donor names. He reminds colleagues that public ledgers show transaction amounts and addresses to anyone, so linking an address to a named donor in shared documents could expose that donor's other activity. He proposes that shared reports use receipt numbers only. Privacy is part of trustworthy practice and is particularly important for charities, whose donors expect discretion.

### Worked example

Marcus works under written read-only scope, hashes every export and reconciles with receipt numbers rather than donor names.

> **Synthetic case.** The authorisation, evidence and records are synthetic.

### Errors and limits

Linking public addresses to named donors in shared documents can expose donors' other activity.

### Exercises

- **EX011 — Scope exclusion.** Name one activity excluded from scope. *Rubric:* 3 = moving real funds;; 2 = contacting donors;; 1 = reviewing configuration;; 0 = none.
- **EX012 — Urgent contact.** What does the authorisation name for urgent findings? *Rubric:* 3 = who to contact;; 2 = a contact;; 1 = vague;; 0 = none.
- **EX013 — Evidence integrity.** How are exported files protected? *Rubric:* 3 = storing a SHA-256 hash of each;; 2 = hashing;; 1 = emailing;; 0 = none.
- **EX014 — Reconciliation data.** What data does Marcus use for reconciliation? *Rubric:* 3 = receipt numbers, amounts and references;; 2 = receipts;; 1 = donor names;; 0 = none.
- **EX015 — Public ledger risk.** Why avoid linking addresses to names? *Rubric:* 3 = it could expose donors' other activity;; 2 = privacy;; 1 = cost;; 0 = none.

### Synthesis

Written authorisation, careful evidence and donor privacy define authorised practice.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Web3, blockchain and cryptoasset security: core methods

### Learning outcomes

You will (1) apply a structured review of custody arrangements; (2) use recognised guidance; (3) record findings consistently.

### 4.1 Structured custody review

Marcus reviews the treasury's custody arrangements with a structured checklist: who the signers are, how their keys are stored, what threshold is required, how signers verify what they approve, whether destinations are restricted, how lost keys are recovered and how signer changes are made. For each question he gathers evidence. A structured review ensures that important areas are not skipped because they seem routine. He finds that the signer list still includes a former finance officer who left four months ago, which is his first significant finding.

### 4.2 Using recognised guidance

Marcus uses recognised guidance as criteria. The OWASP Smart Contract Top 10 identifies access control as a leading weakness area, which applies to the multisig's signer management. The ConsenSys best practices discuss careful handling of privileged operations. NIST IR 8202 explains blockchain components and their trust assumptions. He maps each checklist question to guidance where it fits, so findings rest on recognised sources rather than his opinion. He notes that most guidance is written for developers, so he adapts it carefully to an operational setting.

### 4.3 Recording findings

Each finding is recorded with an identifier, description, evidence, risk rating, guidance reference and recommendation. Marcus records three: the former officer remains a signer; signers approve transfers on their everyday laptops; and there is no written procedure for recovering a lost signer key. He rates the first two high and the third medium. He discusses them with the director before writing the report, so there are no surprises. Consistent, discussed findings are more likely to be accepted and acted upon by busy managers and trustees.

### Worked example

Marcus's custody review finds a departed officer still a signer, approvals on everyday laptops and no recovery procedure, rating two high.

> **Synthetic case.** The review and findings are synthetic; OWASP SC Top 10, ConsenSys best practices and NIST IR 8202 are real sources.

### Errors and limits

Skipping routine-seeming checklist areas can miss findings like a departed signer.

### Exercises

- **EX016 — Checklist area.** Name one custody checklist area. *Rubric:* 3 = how signers verify what they approve;; 2 = key storage;; 1 = office layout;; 0 = none.
- **EX017 — First finding.** What was the first significant finding? *Rubric:* 3 = a former officer still on the signer list;; 2 = departed signer;; 1 = vague;; 0 = none.
- **EX018 — Guidance adaptation.** Why adapt guidance carefully? *Rubric:* 3 = most is written for developers;; 2 = developer focus;; 1 = it is perfect;; 0 = none.
- **EX019 — High-rated findings.** Which findings are rated high? *Rubric:* 3 = departed signer and approvals on everyday laptops;; 2 = two findings;; 1 = recovery;; 0 = none.
- **EX020 — Pre-report step.** What does Marcus do before writing the report? *Rubric:* 3 = discusses findings with the director;; 2 = discuss;; 1 = publish;; 0 = none.

### Synthesis

Structured reviews grounded in guidance produce findings that managers act on.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Web3, blockchain and cryptoasset security: tools and interpretation

### Learning outcomes

You will (1) use read-only tools to reconcile donations; (2) interpret discrepancies; (3) avoid over- and under-reacting.

### 5.1 Reconciling donations

Each donation receipt should match an incoming transfer to the treasury address. Marcus writes a read-only script that compares the finance team's receipts, each with an amount and a ledger reference, against incoming transfers exported from a block explorer. It reports receipts with no reference, references not found, amount differences and incoming transfers with no receipt. This lab uses five synthetic receipts and five synthetic transfers. It uses only Python's standard library and touches no live systems, accounts or wallets.

### Lab — Donation reconciliation

```python
"""Reconcile synthetic donation receipts with incoming ledger transfers (read-only)."""
# receipt id, amount in units, ledger tx reference recorded by the finance team
RECEIPTS = [("R-201", 500, "tx-a1"), ("R-202", 120, "tx-a2"), ("R-203", 75, "tx-a3"),
            ("R-204", 300, "tx-a4"), ("R-205", 60, None)]
# incoming transfers seen on the ledger: tx reference, amount
LEDGER = {"tx-a1": 500, "tx-a2": 120, "tx-a3": 57, "tx-a4": 300, "tx-a6": 40}

def main():
    used = set()
    for rid, amt, tx in RECEIPTS:
        if tx is None:
            print(f"{rid}: no ledger reference")
        elif tx not in LEDGER:
            print(f"{rid}: {tx} not found on ledger")
        elif LEDGER[tx] != amt:
            print(f"{rid}: amount {amt} vs ledger {LEDGER[tx]}")
        used.add(tx)
    for tx in sorted(set(LEDGER) - used):
        print(f"{tx}: incoming {LEDGER[tx]} with no receipt")
    print(f"receipts {len(RECEIPTS)}; ledger transfers {len(LEDGER)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_donations.py`. Verified output:

```text
R-203: amount 75 vs ledger 57
R-205: no ledger reference
tx-a6: incoming 40 with no receipt
receipts 5; ledger transfers 5
```

### 5.2 Interpreting discrepancies

The lab reports three issues: receipt R-203 records 75 units while the ledger shows 57; receipt R-205 has no ledger reference; and transfer tx-a6 of 40 units has no receipt. Marcus investigates each. R-203 is a typing error that swapped digits when the receipt was issued; a corrected receipt is sent. R-205 was a cash donation wrongly entered in the cryptoasset register. Tx-a6 is a genuine donation from a donor who did not request a receipt; it is recorded. Each discrepancy has an ordinary explanation, but each needed checking.

### 5.3 Proportionate response

Marcus notes that discrepancies are signals, not proof of wrongdoing. Over-reacting, such as freezing the treasury for a typing error, would harm the charity; under-reacting, such as ignoring an unreceipted transfer, could miss a misdirected payment or a reporting duty. He documents each explanation and evidence, and proposes that receipts be generated from the ledger reference rather than typed. Ms Holm notes that proportionate interpretation is the core professional skill: tools find differences, and practitioners decide what they mean using evidence and judgement.

### Worked example

The lab reports R-203 at 75 versus 57, R-205 without a reference and tx-a6 of 40 without a receipt, each explained and corrected.

> **Synthetic case.** The receipts, transfers and explanations are synthetic.

### Errors and limits

Treating every discrepancy as wrongdoing, or ignoring it, are both disproportionate responses.

### Exercises

- **EX021 — Lab issue count.** How many issues does the lab report? *Rubric:* 3 = three;; 2 = 3;; 1 = five;; 0 = none.
- **EX022 — R-203 discrepancy.** What is wrong with R-203? *Rubric:* 3 = 75 recorded versus 57 on the ledger;; 2 = swapped digits;; 1 = missing;; 0 = none.
- **EX023 — R-205 explanation.** What explains R-205? *Rubric:* 3 = a cash donation entered in the wrong register;; 2 = cash entry;; 1 = theft;; 0 = none.
- **EX024 — Unreceipted transfer.** What is tx-a6? *Rubric:* 3 = a genuine 40-unit donation without a receipt request;; 2 = genuine donation;; 1 = an error;; 0 = none.
- **EX025 — Process improvement.** What process change does Marcus propose? *Rubric:* 3 = generate receipts from the ledger reference;; 2 = automatic receipts;; 1 = stop receipts;; 0 = none.

### Synthesis

Read-only reconciliation finds differences, and proportionate interpretation explains them.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Web3, blockchain and cryptoasset security: operational workflow

### Learning outcomes

You will (1) define the monthly conversion workflow; (2) build verification into each step; (3) document roles and timing.

### 6.1 Defining the workflow

Marcus documents the monthly conversion workflow with the finance lead. Step one: reconcile the month's donations. Step two: prepare a transfer proposal to the exchange deposit address on the allow-list. Step three: two signers independently verify the destination and amount on their signing devices against the written request. Step four: execute the transfer and record the transaction reference. Step five: confirm the exchange credited the amount and the bank received the converted funds. Writing the workflow down replaces memory with a shared procedure that new staff can follow.

### 6.2 Verification at each step

Each step has a check. Reconciliation must be complete before a proposal is created. The destination must match the allow-listed exchange address, which was verified once by a small test transfer and is stored in the procedure. Signers compare the first and last characters of the address on their device with the written request, and the amount with the reconciliation total. After execution, the finance lead confirms the exchange credit. Verification at each step means an error in one step is likely to be caught before funds move irreversibly.

### 6.3 Roles and timing

The workflow names roles and timing: the finance team prepares by the third working day, signers approve within two working days, and the finance lead confirms receipt within five. A signer cannot also prepare the proposal they approve. If a signer is unavailable, the trustee steps in. Marcus adds the workflow to the charity's finance manual and schedules a yearly review. Clear roles and timing prevent rushed approvals at month end, which Ms Holm notes are a common source of mistakes in any payment process.

### Worked example

Marcus documents a five-step conversion workflow with allow-listed destinations, device-based address checks and separate preparers and signers.

> **Synthetic case.** The workflow is synthetic.

### Errors and limits

Rushed month-end approvals without set timing invite payment mistakes.

### Exercises

- **EX026 — Workflow first step.** What is the first workflow step? *Rubric:* 3 = reconcile the month's donations;; 2 = reconciliation;; 1 = transfer;; 0 = none.
- **EX027 — Destination control.** How is the destination controlled? *Rubric:* 3 = allow-listed exchange address verified by a test transfer;; 2 = allow-list;; 1 = typed fresh;; 0 = none.
- **EX028 — Signer check.** What do signers compare on their devices? *Rubric:* 3 = address characters and amount against the request;; 2 = address and amount;; 1 = colours;; 0 = none.
- **EX029 — Duty separation.** What may a signer not do? *Rubric:* 3 = prepare the proposal they approve;; 2 = self-approve;; 1 = sign;; 0 = none.
- **EX030 — Timing rule.** By when must signers approve? *Rubric:* 3 = within two working days;; 2 = two days;; 1 = same hour;; 0 = none.

### Synthesis

A written workflow with checks, roles and timing makes conversions safe and repeatable.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Web3, blockchain and cryptoasset security: controls and verification

### Learning outcomes

You will (1) implement custody controls; (2) verify them with tests; (3) track remediation of findings.

### 7.1 Implementing controls

Following his findings, Marcus helps implement controls. The former officer is removed from the signer list through the multisig's change process, with two current signers approving. Signers receive dedicated hardware signing devices used only for treasury approvals. A recovery procedure is written: if a signer loses their device, the other two signers approve a signer replacement after identity checks, and the trustee holds sealed recovery instructions. A rule is added that large transfers above 2,500 units need all three signers. Each control traces back to a finding.

### 7.2 Verifying controls

Marcus verifies each control on a test network replica of the treasury with synthetic funds. A proposal approved by one signer cannot execute. A proposal with approvals from a removed signer does not count. A transfer above the large threshold with two approvals does not execute. A replacement signer can be added only with two approvals. He records each test and result. Verification on a replica allows confident testing without risk to donations, and it confirms the controls work as designed rather than as assumed.

### 7.3 Tracking remediation

Marcus tracks each finding in a simple register: description, owner, action, due date, status and verification evidence. All three original findings are closed within six weeks, each with evidence. He reports status monthly to the director and trustees. Tracking ensures findings do not stall after the review ends, which Ms Holm notes is common when reports are delivered and filed. A finding is closed only when verified, not when someone says it is fixed, so the register always reflects demonstrated rather than claimed progress.

### Worked example

Marcus removes the departed signer, issues dedicated devices, adds a recovery procedure and a three-signer rule above 2,500, verifying each on a replica.

> **Synthetic case.** The controls, tests and register are synthetic.

### Errors and limits

Closing findings on someone's word, without verification, leaves claimed fixes unproven.

### Exercises

- **EX031 — Signer removal.** How is the former officer removed? *Rubric:* 3 = through the change process with two current signers;; 2 = multisig change;; 1 = by deleting email;; 0 = none.
- **EX032 — Large transfer rule.** What applies to transfers above 2,500 units? *Rubric:* 3 = all three signers must approve;; 2 = three signers;; 1 = one signer;; 0 = none.
- **EX033 — Verification environment.** Where are controls verified? *Rubric:* 3 = a test network replica with synthetic funds;; 2 = replica;; 1 = live treasury;; 0 = none.
- **EX034 — Remediation time.** How long did closing all three findings take? *Rubric:* 3 = six weeks;; 2 = 6 weeks;; 1 = one year;; 0 = none.
- **EX035 — Closure rule.** When is a finding closed? *Rubric:* 3 = only when verified;; 2 = verified;; 1 = when reported fixed;; 0 = none.

### Synthesis

Implemented, verified and tracked controls turn findings into lasting protection.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Web3, blockchain and cryptoasset security: supervised case analysis

### Learning outcomes

You will (1) analyse a synthetic incident under supervision; (2) separate facts from assumptions; (3) produce lessons and actions.

### 8.1 The synthetic incident

Ms Holm presents a synthetic case. A staff member at another fictional charity receives an urgent email appearing to come from their director, asking them to approve a treasury transfer to a new exchange address before the end of the day. The staff member prepares the proposal and a second signer approves it without checking the address against an allow-list. Funds are sent to an address the charity does not control. The case is presented at a high level, without technical detail, so participants focus on controls and decisions.

### 8.2 Facts and assumptions

Marcus separates facts from assumptions. Facts: the request came by email; the address was new; two signers approved; no allow-list existed; funds left the treasury. Assumptions to test: that the email truly came from the director; that signers had time to verify; that the exchange could help recover funds. He notes that many incident analyses go wrong by treating assumptions as facts. He also identifies what went right: the charity noticed within hours and reported promptly to the exchange and the authorities, as its plan required.

### 8.3 Lessons and actions

Marcus draws lessons: new destinations must be verified through an independent channel, such as a phone call to a known number; allow-lists prevent last-minute address changes; urgency in a request is a warning sign that should slow approval, not speed it; and second signers must verify independently rather than trust the first. He compares them with Bayview's workflow and finds that the allow-list and device checks already address most points. He adds a rule to confirm any new destination by phone. Ms Holm grades his analysis highly for clarity.

### Worked example

Marcus separates five facts from three assumptions in the case and adds phone confirmation for any new destination to Bayview's workflow.

> **Synthetic case.** The incident and both charities are synthetic.

### Errors and limits

Treating assumptions as facts in incident analysis leads to wrong lessons.

### Exercises

- **EX036 — Request channel.** How did the fraudulent request arrive? *Rubric:* 3 = an urgent email appearing to be from the director;; 2 = email;; 1 = phone;; 0 = none.
- **EX037 — Missing control.** Which control was missing in the case? *Rubric:* 3 = an allow-list of destinations;; 2 = allow-list;; 1 = multisig;; 0 = none.
- **EX038 — Assumption to test.** Name one assumption to test. *Rubric:* 3 = that the email came from the director;; 2 = signers had time;; 1 = funds left;; 0 = none.
- **EX039 — Urgency lesson.** How should urgency in a request be treated? *Rubric:* 3 = as a warning sign that slows approval;; 2 = warning sign;; 1 = speed up;; 0 = none.
- **EX040 — Added rule.** What rule does Marcus add at Bayview? *Rubric:* 3 = confirm any new destination by phone;; 2 = phone confirmation;; 1 = vague;; 0 = none.

### Synthesis

Supervised case analysis turns others' incidents into concrete, proportionate actions.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) write clear reports for decision-makers; (2) handle sensitive findings ethically; (3) communicate with donors appropriately.

### 9.1 Reports for decision-makers

Marcus writes his review report for the director and trustees. It opens with a one-page summary: what was reviewed, three key findings, actions taken and remaining risks, in plain language. Details and evidence follow in appendices. Each finding states its impact on the charity, not just its technical nature. He avoids jargon and explains essential terms once. Trustees tell him it is the first technical report they have read fully. Reports succeed when decision-makers understand them well enough to act and to explain their decisions to others.

### 9.2 Ethics with sensitive findings

The departed signer finding could embarrass the former officer and the finance team. Marcus presents it factually, as a process gap in leaver procedures rather than anyone's fault, and does not speculate about intentions. He shares the report only with people who need it. He also reports honestly that the review did not cover the exchange's controls, so trustees do not assume more assurance than was provided. Ethical reporting is accurate, fair to individuals and clear about its own limits, even when that is uncomfortable.

### 9.3 Communicating with donors

Trustees ask whether to tell donors about the review. Marcus suggests a short, accurate statement in the annual report: the charity reviewed how it safeguards cryptoasset donations, strengthened its controls and will review them yearly. He advises against detailed technical disclosure that could help someone target the charity and against overstating security with phrases like fully secure. Clear, honest communication maintains donor trust. The director approves the statement, and Marcus files the decision with the report for future reference by trustees.

### Worked example

Marcus's report opens with a one-page plain summary, presents the departed signer as a leaver-process gap and proposes a modest donor statement.

> **Synthetic case.** The report and communications are synthetic.

### Errors and limits

Claiming a charity is fully secure overstates assurance and invites misplaced trust.

### Exercises

- **EX041 — Summary content.** What does the one-page summary contain? *Rubric:* 3 = scope, three findings, actions and remaining risks;; 2 = key findings;; 1 = all evidence;; 0 = none.
- **EX042 — Fair framing.** How is the departed signer finding framed? *Rubric:* 3 = as a leaver process gap, not a person's fault;; 2 = process gap;; 1 = blame;; 0 = none.
- **EX043 — Stated limit.** What limit does the report state? *Rubric:* 3 = the exchange's controls were not covered;; 2 = exchange not reviewed;; 1 = vague;; 0 = none.
- **EX044 — Donor statement.** What does Marcus suggest telling donors? *Rubric:* 3 = controls were reviewed, strengthened and will be reviewed yearly;; 2 = short statement;; 1 = full technical detail;; 0 = none.
- **EX045 — Phrase to avoid.** Which kind of phrase does he advise against? *Rubric:* 3 = fully secure;; 2 = overstatement;; 1 = thank you;; 0 = none.

### Synthesis

Clear, fair and honest reporting serves trustees, staff and donors.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Web3, blockchain and cryptoasset security: quality and troubleshooting

### Learning outcomes

You will (1) monitor workflow quality; (2) troubleshoot problems methodically; (3) improve the process from evidence.

### 10.1 Monitoring quality

Marcus tracks simple quality measures for the donation workflow: percentage of donations reconciled within five days, number of discrepancies per month and their causes, time from proposal to approval, and any approvals outside the documented steps. After three months, reconciliation within five days rises from 70 to 95 percent, and discrepancies fall from six to two a month after receipts were generated from ledger references. Measures show whether controls are working in practice, and trends help catch slippage early before it becomes a habit.

### 10.2 Methodical troubleshooting

One month, a transfer to the exchange shows as executed on the ledger, but the exchange account shows no credit after a day. Marcus follows a method: confirm the transaction reference and destination on a block explorer, check that it matches the allow-listed address, check the exchange's status page and contact the exchange's support through the documented channel. The transaction and address are correct; the exchange reports a delay in crediting deposits from that network. The funds are credited the next day. He records the timeline and evidence.

### 10.3 Improving from evidence

From the delay, Marcus adds a step to the workflow: check the exchange's status page before initiating a transfer, and avoid transfers during announced maintenance. He also records the expected crediting time for the network. From the quality measures, he finds approvals sometimes take four days, mostly when the trustee travels, and proposes scheduling approvals around trustees' calendars. Ms Holm notes that continuous improvement based on measured evidence is what keeps controls usable over time, rather than letting them become burdens people work around.

### Worked example

Reconciliation within five days rises from 70 to 95 percent, a delayed exchange credit is traced to the exchange, and a status-page check is added.

> **Synthetic case.** The measures, delay and improvements are synthetic.

### Errors and limits

Assuming funds are lost when a credit is delayed, without checking, causes needless alarm.

### Exercises

- **EX046 — Reconciliation improvement.** How did on-time reconciliation change? *Rubric:* 3 = from 70 to 95 percent;; 2 = 95 percent;; 1 = unchanged;; 0 = none.
- **EX047 — Discrepancy trend.** How did monthly discrepancies change? *Rubric:* 3 = from six to two;; 2 = fell;; 1 = rose;; 0 = none.
- **EX048 — Delay cause.** What caused the missing exchange credit? *Rubric:* 3 = an exchange delay crediting that network;; 2 = exchange delay;; 1 = wrong address;; 0 = none.
- **EX049 — Added step.** What step is added before transfers? *Rubric:* 3 = check the exchange's status page;; 2 = status check;; 1 = vague;; 0 = none.
- **EX050 — Approval delay cause.** Why did approvals sometimes take four days? *Rubric:* 3 = the trustee was travelling;; 2 = travel;; 1 = no reason;; 0 = none.

### Synthesis

Quality measures and methodical troubleshooting drive evidence-based improvements.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) check treasury proposals against policy; (2) interpret readiness results; (3) decide what must happen before signing.

### 11.1 Purpose of the check

Before signers approve any proposal, Bayview's policy requires: every signer on the list is current, the destination is on the allow-list, ordinary proposals have two current approvals and proposals of 2,500 units or more have three. Marcus writes a read-only script that reads a synthetic signer list and pending proposals and reports which are ready and which are not, with reasons. In the supervised lab, Ms Holm reviews his script and its output. It uses only Python's standard library and synthetic data, and it cannot sign or send anything.

### Lab — Treasury proposal policy check

```python
"""Check pending treasury proposals against a written policy (synthetic, read-only)."""
SIGNERS = {"finance-lead": "active", "director": "active", "trustee-a": "active", "former-cfo": "left"}
THRESHOLD = 2
# proposal id, amount, destination on allow-list?, approvals so far
PROPOSALS = [("P-31", 800, True, ["finance-lead"]), ("P-32", 4200, True, ["director", "trustee-a"]),
             ("P-33", 950, False, ["finance-lead", "former-cfo"])]
LARGE = 2500   # policy: large payments need 3 approvals

def main():
    gone = [s for s, st in SIGNERS.items() if st != "active"]
    if gone:
        print(f"signer list includes departed: {', '.join(gone)}")
    for pid, amt, allowed, appr in PROPOSALS:
        valid = [a for a in appr if SIGNERS.get(a) == "active"]
        need = 3 if amt >= LARGE else THRESHOLD
        notes = []
        if not allowed:
            notes.append("destination not on allow-list")
        if len(valid) < need:
            notes.append(f"active approvals {len(valid)}/{need}")
        print(f"{pid} ({amt}): {'ready' if not notes else '; '.join(notes)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_treasury.py`. Verified output:

```text
signer list includes departed: former-cfo
P-31 (800): active approvals 1/2
P-32 (4200): active approvals 2/3
P-33 (950): destination not on allow-list; active approvals 1/2
```

### 11.2 Interpreting the output

The script first warns that the signer list still includes a departed former-cfo, which must be fixed before relying on any approvals. P-31 for 800 units has one active approval of two needed. P-32 for 4,200 units has two of three needed because it is large. P-33 for 950 units goes to a destination not on the allow-list, and one of its two approvals came from the departed signer, so only one counts. No proposal is ready. Marcus notes that P-33 needs particular attention because both its destination and its approvals fail policy.

### 11.3 Deciding next steps

Marcus recommends: remove the departed signer immediately through the change process; reject P-33 and ask the preparer to explain the new destination, confirming it by phone before any new proposal; collect the missing approvals for P-31 and P-32 in the normal way. Ms Holm asks why not simply add the new destination to the allow-list. He explains that adding destinations is itself a controlled change that requires independent verification. The supervised lab shows that automated policy checks inform, but people decide and follow the documented process.

### Worked example

The script warns of a departed signer and finds P-31 at 1 of 2, P-32 at 2 of 3 and P-33 failing both allow-list and approvals; none is ready.

> **Synthetic case.** The signers and proposals are synthetic.

### Errors and limits

Counting approvals from departed signers lets an outdated list override policy.

### Exercises

- **EX051 — Departed signer warning.** Which signer triggers a warning? *Rubric:* 3 = former-cfo;; 2 = the departed CFO;; 1 = director;; 0 = none.
- **EX052 — P-32 status.** Why is P-32 not ready? *Rubric:* 3 = large amount needs 3 approvals, has 2;; 2 = needs three;; 1 = wrong destination;; 0 = none.
- **EX053 — P-33 problems.** What is wrong with P-33? *Rubric:* 3 = destination not allow-listed and only one active approval;; 2 = two failures;; 1 = vague;; 0 = none.
- **EX054 — Ready count.** How many proposals are ready? *Rubric:* 3 = none of the three;; 2 = none, without saying of how many;; 1 = all;; 0 = no answer.
- **EX055 — Allow-list addition.** Why not just add P-33's destination to the allow-list? *Rubric:* 3 = adding destinations is a controlled change needing verification;; 2 = controlled change;; 1 = no reason;; 0 = none.

### Synthesis

Policy checks reveal unready proposals, and documented processes decide what happens next.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a professional portfolio; (2) review outcomes against goals; (3) plan continuing development.

### 12.1 Assembling the portfolio

Marcus assembles a portfolio of his work: the authorisation, the custody review report, the donation reconciliation script and results, the documented workflow, the controls register with verification evidence, the case analysis, the quality measures and his reflections. Each item has a short note explaining what it shows. He removes donor personal data and replaces sensitive addresses with placeholders. A portfolio demonstrates competence through real work rather than claims, and it gives future employers and colleagues evidence of how he approaches problems.

### 12.2 Reviewing outcomes

Marcus reviews his goals from the start of the programme: understand the charity's cryptoasset donations, find and fix the main custody weaknesses, make conversions safer and keep donors' trust. Evidence shows all three original findings closed, discrepancies reduced from six to two a month, a documented workflow in use and trustees satisfied with reporting. He also notes gaps: he did not review the exchange's controls, and the charity still relies on a single exchange. He recommends assessing a second exchange during the next year as a contingency.

### 12.3 Continuing development

Marcus plans his development: a course on payment fraud prevention, reading the EEA EthTrust specification to understand contract assurance better, and joining a practitioner community for charities handling digital assets. Ms Holm's final assessment praises his evidence-based approach, proportionate judgement and clear reporting. She notes that he stayed within his scope and asked for help when needed. Marcus reflects that the programme taught him that cryptoasset security relies on the same disciplines as any financial control: clear roles, verification and honest records.

### Worked example

Marcus's portfolio evidences three closed findings and discrepancies down from six to two monthly, and he recommends assessing a second exchange.

> **Synthetic case.** The portfolio, review and plans are synthetic; EEA EthTrust is a real source.

### Errors and limits

Including donor personal data in a portfolio breaches the privacy it should demonstrate.

### Exercises

- **EX056 — Portfolio sanitising.** How is the portfolio sanitised? *Rubric:* 3 = donor data removed, sensitive addresses replaced by placeholders;; 2 = redaction;; 1 = vague;; 0 = none.
- **EX057 — Original goals.** Name one of Marcus's original goals. *Rubric:* 3 = make conversions safer;; 2 = fix custody weaknesses;; 1 = learn to trade;; 0 = none.
- **EX058 — Remaining dependency.** What dependency remains? *Rubric:* 3 = reliance on a single exchange;; 2 = one exchange;; 1 = vague;; 0 = none.
- **EX059 — Development step.** Name one development step planned. *Rubric:* 3 = reading the EthTrust specification;; 2 = fraud prevention course;; 1 = vague;; 0 = none.
- **EX060 — Final reflection.** What did Marcus conclude about cryptoasset security? *Rubric:* 3 = it relies on the same disciplines as financial control;; 2 = same disciplines;; 1 = entirely new;; 0 = none.

### Synthesis

A sanitised portfolio, honest review and development plan complete professional practice.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Marcus Delgado, Ms Ingrid Holm, Kestrel Professional Academy, Bayview Charity Network and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** They go into a multi-signature treasury wallet and are converted to local currency monthly.

**EX002.** The person recording donations is not the only person able to move funds.

**EX003.** Change the signer list alone.

**EX004.** Authorised work, kept evidence, no keys on general computers, honest reporting or asking for help.

**EX005.** Because mistakes can move funds irreversibly, so standards must hold under pressure.

**EX006.** The finance lead, the director and a trustee, in a 2-of-3 arrangement.

**EX007.** Monthly transfer to a regulated exchange that pays the charity's bank account.

**EX008.** A mistaken transfer that cannot be reversed.

**EX009.** Recording donations correctly for tax receipts.

**EX010.** He lists questions for the charity's legal adviser.

**EX011.** Moving real funds, contacting donors or testing the exchange's systems.

**EX012.** The person to contact if something urgent is found.

**EX013.** By storing a SHA-256 hash of every exported file.

**EX014.** Receipt numbers, amounts and transaction references, not donor names.

**EX015.** Because public ledger data could then reveal that donor's other activity.

**EX016.** Signers, key storage, threshold, verification, destinations, recovery or signer changes.

**EX017.** A finance officer who left four months ago remained a signer.

**EX018.** Because most guidance is written for developers, not operations.

**EX019.** The departed signer and approvals on everyday laptops.

**EX020.** He discusses the findings with the director to avoid surprises.

**EX021.** Three issues.

**EX022.** The receipt shows 75 units while the ledger shows 57.

**EX023.** A cash donation wrongly entered in the cryptoasset register.

**EX024.** A genuine 40-unit donation whose donor did not request a receipt.

**EX025.** Generating receipts from the ledger reference instead of typing them.

**EX026.** Reconciling the month's donations.

**EX027.** It must match the allow-listed exchange address verified by a small test transfer.

**EX028.** The address's first and last characters and the amount against the written request.

**EX029.** Prepare the same proposal they approve.

**EX030.** Within two working days.

**EX031.** Through the multisig change process, approved by two current signers.

**EX032.** All three signers must approve.

**EX033.** On a test network replica of the treasury with synthetic funds.

**EX034.** Within six weeks.

**EX035.** Only when the fix is verified with evidence.

**EX036.** By an urgent email appearing to come from the director.

**EX037.** An allow-list of destination addresses.

**EX038.** That the email was genuine, that signers had time, or that the exchange could help.

**EX039.** As a warning sign that should slow approval down.

**EX040.** Confirming any new destination by phone to a known number.

**EX041.** What was reviewed, three key findings, actions taken and remaining risks.

**EX042.** As a gap in leaver procedures rather than anyone's fault.

**EX043.** That the exchange's controls were not reviewed.

**EX044.** A short statement that controls were reviewed, strengthened and will be reviewed yearly.

**EX045.** Overstating phrases such as fully secure.

**EX046.** From 70 percent to 95 percent within five days.

**EX047.** From six to two a month.

**EX048.** The exchange was delayed in crediting deposits from that network.

**EX049.** Checking the exchange's status page and avoiding announced maintenance.

**EX050.** Mostly because the trustee was travelling.

**EX051.** The departed former-cfo still on the signer list.

**EX052.** At 4,200 units it needs three active approvals and has two.

**EX053.** Its destination is not on the allow-list and only one approval is from an active signer.

**EX054.** None of the three.

**EX055.** Adding a destination is itself a controlled change requiring independent verification.

**EX056.** Donor personal data removed and sensitive addresses replaced with placeholders.

**EX057.** Understanding donations, fixing custody weaknesses, safer conversions or keeping donor trust.

**EX058.** The charity still relies on a single exchange.

**EX059.** A fraud-prevention course, reading EthTrust or joining a practitioner community.

**EX060.** It relies on the same disciplines as any financial control: roles, verification and honest records.

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
