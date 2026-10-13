# Web3, Blockchain and Cryptoasset Security: Engineering Degree

- Language: English (`en`); course 124, Engineering degree (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; Seven offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students learning to design, verify, operate and assure blockchain systems as complete engineered systems.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only contracts, wallets and systems you are authorised to assess, on local simulations or test networks; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic ledgers, transactions, contract inventories and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one engineering student designing and assuring a permissioned community-energy token ledger, from mathematics, computing and cryptography foundations, through requirements, architecture, control and verification, to operations, evaluation, deployment and thesis defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Jonas Weber** | Engineering student | Invented |
| **Dr Amara Nwosu** | Supervisor | Invented |
| **Avalon Polytechnic University** | Fictional university | Invented |
| **Brightwater Community Energy Cooperative** | Fictional client (about 400 households, 3 validators) | Invented |

### Core sources

Nakamoto, [Bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf); Wood, [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf); NIST [IR 8202](https://doi.org/10.6028/NIST.IR.8202); [SWC registry](https://swcregistry.io/); [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/); EEA [EthTrust Security Levels v3](https://entethalliance.org/specs/ethtrust-sl/v3/); [ConsenSys smart contract best practices](https://consensys.github.io/smart-contract-best-practices/); Atzei et al. ([2017](https://doi.org/10.1007/978-3-662-54455-6_8)); Luu et al. ([2016](https://doi.org/10.1145/2976749.2978309)). Full list in [References](#references).

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

You will (1) describe change with rates and limits; (2) model token supply growth; (3) read rates from data.

### 1.1 The case and why calculus

Jonas Weber is an engineering student at the fictional Avalon Polytechnic University, supervised by Dr Amara Nwosu. Over five years he will help the fictional Brightwater Community Energy Cooperative, about 400 member households, design and secure a system that records solar energy credits as tokens on a permissioned Ethereum-compatible ledger. Every person, contract and number in this book is synthetic. Calculus may seem distant from blockchain security, but engineers constantly reason about rates: how fast credits are issued, how quickly balances change, and how fast an abnormal flow must be noticed before it causes harm.

### 1.2 Rates of change

A derivative describes how fast one quantity changes with respect to another. If the cooperative issues credits in proportion to energy generated, total supply S(t) grows at rate dS/dt equal to generation in kilowatt-hours per hour times credits per kilowatt-hour. On a sunny afternoon the rate is high; at night it is zero. Jonas models supply as the integral of issuance minus redemptions. This gives a baseline for normal behaviour: if supply ever rises faster than generation could explain, something is wrong, whether a meter fault, a software error or misuse of the minting function.

### 1.3 Reading rates from data

Real data are discrete: the ledger records events, not smooth curves. Jonas estimates rates using differences over fixed intervals, such as credits minted per hour, and smooths noise with moving averages. He plots a synthetic week and marks the maximum plausible issuance rate from the cooperative's installed solar capacity of 1.2 megawatts. Any hour exceeding that bound deserves investigation. Calculus here is a practical tool: it turns a physical limit into a numerical threshold that a monitoring system can check automatically, which later chapters will build into the design.

### Worked example

Jonas models supply as the integral of issuance minus redemption and sets an hourly issuance ceiling from the 1.2 MW installed capacity.

> **Synthetic case.** Jonas Weber, Dr Amara Nwosu, Avalon Polytechnic University, Brightwater Community Energy Cooperative and all data are synthetic.

### Errors and limits

Treating any rise in token supply as normal ignores physical limits that should bound issuance.

### Exercises

- **EX001 — Cooperative size.** How many households does Brightwater serve? *Rubric:* 3 = about 400;; 2 = 400;; 1 = 4,000;; 0 = none.
- **EX002 — Supply model.** How does Jonas model supply? *Rubric:* 3 = integral of issuance minus redemptions;; 2 = integral;; 1 = constant;; 0 = none.
- **EX003 — Issuance bound.** What sets the issuance ceiling? *Rubric:* 3 = installed solar capacity of 1.2 MW;; 2 = capacity;; 1 = price;; 0 = none.

### Synthesis

Rates and integrals turn physical limits into checkable bounds for token systems.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) use sets, functions and logic for ledger reasoning; (2) explain hash functions; (3) verify a hash chain.

### 2.1 Sets and functions

A ledger can be described with discrete mathematics. Accounts form a set; balances are a function from accounts to non-negative integers; a transaction is a function from one balance state to the next. Jonas writes the transfer rule in logic: a transfer of amount a from x to y is valid only if balance(x) is at least a, and afterwards balance(x) decreases by a while balance(y) increases by a. Writing rules precisely like this exposes edge cases, such as a transfer to oneself or of zero, that informal descriptions often miss.

### 2.2 Hash functions

A cryptographic hash function maps any input to a fixed-size output in a way that is easy to compute but practically impossible to reverse or to find two inputs with the same output. Nakamoto's Bitcoin paper chains blocks by including each block's hash in the next, so changing any earlier record changes every later hash. Jonas learns that this gives tamper evidence rather than tamper prevention: anyone can rewrite a copy of the data, but the change becomes visible to anyone who checks the chain against a trusted head value.

### Lab — Hash chain check

```python
"""Hash-chain integrity check on a synthetic ledger of energy-credit records (read-only)."""
import hashlib

RECORDS = ["mint 100 to coop", "transfer 20 coop->h01", "transfer 15 coop->h02",
           "transfer 5 h01->h03", "burn 10 from h02"]

def build(records):
    prev, chain = "0" * 64, []
    for r in records:
        h = hashlib.sha256((prev + r).encode()).hexdigest()
        chain.append((r, prev, h)); prev = h
    return chain

def verify(chain):
    prev = "0" * 64
    for i, (r, p, h) in enumerate(chain):
        if p != prev or hashlib.sha256((p + r).encode()).hexdigest() != h:
            return i
        prev = h
    return None

def main():
    chain = build(RECORDS)
    print("blocks", len(chain), "head", chain[-1][2][:12])
    print("intact chain: first bad index =", verify(chain))
    edited = list(chain); r, p, h = edited[2]
    edited[2] = ("transfer 50 coop->h02", p, h)
    print("edited record 2: first bad index =", verify(edited))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_chain.py`. Verified output:

```text
blocks 5 head 73420780eb14
intact chain: first bad index = None
edited record 2: first bad index = 2
```

### 2.3 Reading the check

Jonas's standard-library script builds a five-record synthetic chain with SHA-256 and verifies it. The intact chain reports no bad index. When the script edits the amount in record 2 without recomputing hashes, verification reports the first bad index as 2. If an editor recomputed every later hash, the chain would verify internally, but its head would no longer match the head value held by other parties. Jonas notes that integrity therefore depends on distributing and comparing head values, which is the role consensus plays in a real network.

### Worked example

The lab builds a five-block SHA-256 chain, verifies it intact and detects an edited record at index 2.

> **Synthetic case.** Records and the script are synthetic; Nakamoto (2008) is a real source.

### Errors and limits

Believing a hash chain prevents tampering, rather than revealing it to those who compare heads, overstates its protection.

### Exercises

- **EX004 — Transfer precondition.** What must hold for a transfer of a from x? *Rubric:* 3 = balance(x) at least a;; 2 = enough balance;; 1 = vague;; 0 = none.
- **EX005 — Tamper evidence.** Does a hash chain prevent or reveal tampering? *Rubric:* 3 = reveals it to those who compare;; 2 = reveals;; 1 = prevents;; 0 = none.
- **EX006 — Bad index.** Which index did the lab flag after editing? *Rubric:* 3 = 2;; 2 = index 2;; 1 = vague;; 0 = none.

### Synthesis

Precise logical rules and hash chains provide the mathematical basis of ledger integrity.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate energy and physical limits to computing; (2) explain why physical meters matter; (3) reason about device trust.

### 3.1 Energy and computation

Every computation consumes energy, and blockchains make this visible. Nakamoto's design secures Bitcoin through proof of work, where miners spend electricity to propose blocks. Brightwater's permissioned ledger instead uses a small set of known validator nodes, so it consumes little energy, but it trusts those operators. Jonas compares the two in terms of physical cost and trust assumptions, as NIST IR 8202 does in its discussion of consensus models. He concludes that the cooperative's choice suits a small community where members know the operators, but that it shifts security onto node governance.

### 3.2 Meters as physical inputs

The token system starts with physics: solar panels generate electricity measured by smart meters, which report readings that become credits. If a meter is faulty, tampered with or misconfigured, the ledger faithfully records wrong data. Jonas learns that a blockchain guarantees the integrity of what is recorded, not the truth of what was measured. He studies meter accuracy classes and calibration intervals, and notes that physical plausibility checks, such as comparing generation with sunlight data, are needed at the boundary between the physical and digital worlds.

### 3.3 Device trust

Meters are small computers with firmware, clocks and network connections. Jonas lists ways their readings could be wrong without anyone intending harm: clock drift misaligning hourly totals, power cuts causing missing data and firmware bugs. He proposes that each meter sign its readings with a device key, so the ledger can at least confirm which device sent which reading. Signing does not prove the reading is accurate, but it stops readings being silently attributed to the wrong household, which is a common source of disputes.

### Worked example

Jonas compares proof-of-work and permissioned consensus by energy and trust, and proposes signed meter readings plus plausibility checks against sunlight data.

> **Synthetic case.** Meters, readings and the cooperative are synthetic; Nakamoto (2008) and NIST IR 8202 are real sources.

### Errors and limits

Assuming a blockchain makes meter data true ignores the physical input boundary.

### Exercises

- **EX007 — Consensus choice.** What consensus does Brightwater use? *Rubric:* 3 = small set of known validator nodes;; 2 = permissioned;; 1 = proof of work;; 0 = none.
- **EX008 — Ledger guarantee.** What does a blockchain guarantee about meter data? *Rubric:* 3 = integrity of what is recorded, not truth of measurement;; 2 = integrity;; 1 = accuracy;; 0 = none.
- **EX009 — Signing benefit.** What does meter signing give? *Rubric:* 3 = confirms which device sent which reading;; 2 = attribution;; 1 = accuracy;; 0 = none.

### Synthesis

Physical inputs and device trust bound what any ledger can guarantee.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write clear standard-library programs; (2) model ledger records as data; (3) test simple functions.

### 4.1 Programs as precise rules

Jonas's first programming course uses Python with only the standard library. He writes small functions that model ledger operations: one that applies a transfer to a dictionary of balances, one that checks whether a transfer is valid and one that prints balances. Each function does one thing and has a name that says what. He learns that a program is a precise version of a rule, so ambiguity in the rule becomes a bug in the program. Writing the transfer rule from chapter two in code reveals that he had not decided what happens to zero-value transfers.

### 4.2 Records and data structures

Ledger records become tuples or small classes: operation, sender, receiver, amount and timestamp. Jonas stores balances in a dictionary keyed by account identifier and keeps a list of records in order. He chooses integers for amounts, never floating-point numbers, because floating-point arithmetic introduces rounding errors that could create or destroy small amounts of value. This decision mirrors guidance in the EEA EthTrust specification about rounding affecting value, and it is one of the first places where a programming choice becomes a security property.

### 4.3 Testing

For each function Jonas writes tests with known answers: a valid transfer, a transfer exceeding the balance, a zero transfer and a transfer to oneself. He runs them after every change. When he alters the transfer function to support fees, two tests fail, showing he forgot to deduct the fee from the sender. Testing early builds a habit he will need when contracts handle real value: in systems where deployed code is hard to change, finding errors before deployment is far cheaper than after.

### Worked example

Jonas's ledger functions use integer amounts and pass four tests; adding fees breaks two tests and reveals a missing deduction.

> **Synthetic case.** Code and tests are synthetic; EEA EthTrust is a real source.

### Errors and limits

Using floating-point numbers for token amounts introduces rounding errors that can create or destroy value.

### Exercises

- **EX010 — Undecided rule.** What rule had Jonas not decided? *Rubric:* 3 = zero-value transfers;; 2 = zero;; 1 = fees;; 0 = none.
- **EX011 — Amount type.** Why use integers for amounts? *Rubric:* 3 = avoid floating-point rounding errors;; 2 = rounding;; 1 = speed;; 0 = none.
- **EX012 — Fee bug.** What did failing tests reveal? *Rubric:* 3 = fee not deducted from sender;; 2 = missing deduction;; 1 = nothing;; 0 = none.

### Synthesis

Precise, tested functions with integer amounts form the base of trustworthy ledger code.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write requirements and reports clearly; (2) explain blockchain trade-offs to non-specialists; (3) record decisions.

### 5.1 Writing for readers

Jonas must explain technical choices to the cooperative's board, which includes a retired teacher, an electrician and an accountant. He learns to start with the decision needed, then give the options, the trade-offs and his recommendation in plain words. He avoids jargon or defines it once: a smart contract is a program stored on the ledger that runs automatically when called. A short, clear note respects readers' time and helps them make good decisions, which is the purpose of engineering communication.

### 5.2 Explaining trade-offs

The board asks whether the system should use a public blockchain or the cooperative's own permissioned ledger. Jonas explains in a table: a public chain offers wide independence but exposes transactions publicly and costs fees; a permissioned ledger is cheaper and private but relies on trusting the node operators. He cites NIST IR 8202 for the distinction. He states his recommendation, the permissioned ledger with published governance rules, and the conditions under which he would change it. Honest trade-offs build trust more than confident promises.

### 5.3 Decision records

Jonas keeps decision records: short notes stating the decision, context, options considered, the choice and its consequences, with the date and who approved it. The first records the ledger choice, the second the use of integer amounts. Months later, when a new board member asks why the system is not on a public chain, the record answers in two minutes. Decision records preserve reasoning across years and people, which matters in a five-year project and in security, where forgotten reasons lead to unsafe changes.

### Worked example

Jonas presents a one-page trade-off table to the board, who approve a permissioned ledger with published governance; the decision is recorded.

> **Synthetic case.** Board members and decisions are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Presenting only the recommended option without trade-offs denies decision-makers the information they need.

### Exercises

- **EX013 — Note structure.** How does Jonas structure board notes? *Rubric:* 3 = decision, options, trade-offs, recommendation;; 2 = decision first;; 1 = jargon;; 0 = none.
- **EX014 — Ledger recommendation.** What did Jonas recommend? *Rubric:* 3 = permissioned ledger with published governance;; 2 = permissioned;; 1 = public chain;; 0 = none.
- **EX015 — Record value.** How did a decision record help later? *Rubric:* 3 = answered a new member's question quickly;; 2 = reasoning preserved;; 1 = vague;; 0 = none.

### Synthesis

Clear writing, honest trade-offs and decision records make engineering choices understandable and durable.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use integrals and series for accumulation; (2) model fee accumulation and decay; (3) estimate long-run behaviour.

### 6.1 Accumulation

Integrals measure accumulation over time. Jonas uses them to model how credits accumulate in a reserve contract that receives a small fee on each transfer. If transfers occur at rate r(t) and the fee is a fraction f, the reserve after time T is the integral of f times r(t) from zero to T, minus any withdrawals. He compares this model with a synthetic month of data and finds the reserve slightly smaller than predicted. Investigating the gap reveals rounding down on each fee, a small difference that adds up over thousands of transfers.

### 6.2 Series and repeated effects

Many small repeated effects form series. Jonas computes the cumulative rounding loss from per-transfer truncation over many transfers and shows that it is bounded by the number of transfers times one unit, a simple bound that lets the cooperative decide whether the loss matters. The EthTrust specification warns that rounding can be abused when an operation can be repeated, so Jonas notes that the design must ensure rounding never favours the person initiating a transaction. Series analysis makes repeated small effects visible before they become disputes.

### 6.3 Long-run behaviour

Jonas also models credits that expire after a year to encourage use, which produces exponential-like decay of old credits. Using integrals, he estimates the steady-state supply when issuance and expiry balance. He checks the model against simulated data and finds agreement within two percent. Long-run models help the board understand what the system will look like in five years, and give security monitoring a reference: a supply far from the steady state indicates either changed behaviour or a fault. He records the model's assumptions.

### Worked example

The reserve model reveals truncation loss bounded by one unit per transfer, and a steady-state supply model matches simulation within 2%.

> **Synthetic case.** Data and models are synthetic; EEA EthTrust is a real source.

### Errors and limits

Ignoring rounding direction in repeated operations can let users gain value at others' expense.

### Exercises

- **EX016 — Reserve formula.** How is the reserve modelled? *Rubric:* 3 = integral of fee fraction times transfer rate minus withdrawals;; 2 = integral;; 1 = constant;; 0 = none.
- **EX017 — Rounding bound.** What bounds cumulative truncation loss? *Rubric:* 3 = number of transfers times one unit;; 2 = one unit each;; 1 = vague;; 0 = none.
- **EX018 — Rounding direction.** Which way must rounding never favour? *Rubric:* 3 = the person initiating the transaction;; 2 = initiator;; 1 = cooperative;; 0 = none.

### Synthesis

Integrals and series reveal cumulative effects such as rounding and expiry that shape system behaviour.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) model uncertain events; (2) estimate rates and intervals; (3) distinguish anomalies from noise.

### 7.1 Probability models

Many security questions are probabilistic. Jonas models meter faults as rare independent events and uses the Poisson distribution to estimate how many faulty readings to expect each month among 400 meters. With a historical fault rate of one per thousand meter-days, he expects about twelve per month. Observing twenty in one month is unusual but possible; observing sixty would strongly suggest a systematic problem, such as a firmware update gone wrong. Probability turns gut feelings about whether something is odd into quantified statements.

### 7.2 Estimates and intervals

Point estimates hide uncertainty. Jonas learns to report intervals: from a pilot of fifty households over three months, the rate of disputed credit records is estimated with a 95 percent interval rather than a single figure. The interval is wide because the sample is small, which tells the board that more data are needed before setting service targets. Reporting uncertainty honestly prevents decisions based on false precision, a lesson that recurs in measurement and validation chapters later. He reports the interval alongside every estimate.

### 7.3 Anomaly or noise

Monitoring must separate genuine anomalies from normal variation. Jonas compares a fixed threshold, such as more than two thousand credits minted in an hour, with a statistical one based on the mean and spread of past hours. The statistical threshold adapts to seasons but can be slowly shifted by gradual misuse; the fixed one is simple but must be reviewed. He recommends using both, with the physical capacity bound from chapter one as a hard limit, so that each method covers the other's weakness.

### Worked example

Jonas expects about 12 meter faults per month at one per thousand meter-days, reports a wide interval for dispute rates, and recommends combined fixed and statistical thresholds.

> **Synthetic case.** Rates, meters and thresholds are synthetic.

### Errors and limits

Reporting a single estimate from a small pilot hides how uncertain it is.

### Exercises

- **EX019 — Expected faults.** How many faults per month does Jonas expect? *Rubric:* 3 = about twelve;; 2 = 12;; 1 = 400;; 0 = none.
- **EX020 — Wide interval.** Why is the dispute-rate interval wide? *Rubric:* 3 = small pilot sample;; 2 = few data;; 1 = error;; 0 = none.
- **EX021 — Combined thresholds.** Why use both fixed and statistical thresholds? *Rubric:* 3 = each covers the other's weakness;; 2 = complementary;; 1 = cheaper;; 0 = none.

### Synthesis

Probability models, intervals and combined thresholds help separate real anomalies from noise.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) describe how processors, memory and storage run programs; (2) explain the EVM as a virtual machine; (3) relate architecture to cost and limits.

### 8.1 Machines and programs

A processor fetches instructions from memory, executes them and stores results, guided by a program counter. Jonas studies registers, memory hierarchy and storage, learning why reading from disk is far slower than from memory. These ideas carry over to virtual machines, which are programs that imitate a processor. Understanding the layers helps him reason about where things can go wrong: a correct program can still fail if the machine beneath it behaves differently from what the programmer assumed. He relates each layer to ledger nodes.

### 8.2 The Ethereum virtual machine

Wood's yellow paper specifies the Ethereum virtual machine, a stack-based machine with its own instructions, memory and persistent storage for each contract. Every instruction has a gas cost, which limits how much computation a transaction can perform. Brightwater's ledger runs a compatible machine. Jonas learns that storage writes are among the most expensive operations, which influences design: storing every meter reading on-chain would be costly, so the system may store totals on-chain and detailed readings off-chain with hashes linking them.

### 8.3 Limits and failure

Gas limits mean a function that loops over an ever-growing list may eventually cost more than a block allows and become impossible to call. The SWC registry lists denial-of-service weaknesses of this kind. Jonas notes the defensive lesson: design functions whose cost is bounded regardless of how many members join, for example by letting each member claim their own credits rather than distributing to everyone in one transaction. Architecture knowledge thus shapes contract design choices that affect availability years after deployment.

### Worked example

Jonas plans on-chain totals with off-chain readings linked by hashes, and per-member claims instead of loops over all members.

> **Synthetic case.** Designs and the cooperative are synthetic; Wood's yellow paper and the SWC registry are real sources.

### Errors and limits

Writing contract functions that loop over unbounded lists risks making them impossible to call as data grows.

### Exercises

- **EX022 — EVM type.** What kind of machine is the EVM? *Rubric:* 3 = stack-based virtual machine;; 2 = stack;; 1 = register;; 0 = none.
- **EX023 — Expensive operation.** Which operations are among the most expensive? *Rubric:* 3 = storage writes;; 2 = storage;; 1 = additions;; 0 = none.
- **EX024 — Bounded design.** How does Jonas avoid unbounded loops? *Rubric:* 3 = members claim their own credits;; 2 = per-member claims;; 1 = bigger blocks;; 0 = none.

### Synthesis

Understanding processors and the EVM's gas model leads to designs with bounded cost.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure larger programs; (2) handle errors explicitly; (3) test properties as well as examples.

### 9.1 Structure

As programs grow, Jonas organises code into modules: one for ledger state, one for validation rules, one for reporting. Each module has a small public interface and hides its internal details. He writes docstrings explaining each function's purpose and assumptions. Structure matters for security because reviewers must understand code to judge it; a tangled program hides mistakes, while a clear structure lets a reviewer check each rule in one place, as the EthTrust specification's emphasis on documented contract logic suggests.

### 9.2 Explicit errors

Jonas learns to handle errors explicitly rather than ignoring them. When a transfer is invalid, his function raises a clear exception instead of silently doing nothing, and callers must decide what to do. This mirrors a contract weakness listed in the SWC registry: unchecked return values from low-level calls, where a failed call is treated as success. In both Python and contracts, the defensive rule is the same: a failure must be visible to the code that depends on the result, otherwise state and reality drift apart.

### 9.3 Property tests

Example tests check specific cases; property tests check rules that should hold for many inputs. Jonas writes a simple generator of random valid transfer sequences using a fixed seed and checks that total balances always equal supply and no balance goes negative. The property test finds a bug that no example caught: a transfer to oneself doubled the balance due to an update order mistake. Property testing is the beginning of invariant thinking, which later chapters use to verify contracts.

### Worked example

A seeded property test finds a self-transfer bug that doubled balances, which example tests had missed.

> **Synthetic case.** Code, tests and bugs are synthetic; EEA EthTrust and the SWC registry are real sources.

### Errors and limits

Silently ignoring failed operations lets recorded state drift from reality.

### Exercises

- **EX025 — Module split.** How does Jonas organise modules? *Rubric:* 3 = state, validation, reporting;; 2 = three modules;; 1 = one file;; 0 = none.
- **EX026 — SWC parallel.** Which SWC weakness parallels silent errors? *Rubric:* 3 = unchecked return values from low-level calls;; 2 = unchecked return;; 1 = overflow;; 0 = none.
- **EX027 — Property bug.** What did the property test find? *Rubric:* 3 = self-transfer doubled the balance;; 2 = self-transfer;; 1 = nothing;; 0 = none.

### Synthesis

Clear structure, explicit errors and property tests make larger programs reviewable and reliable.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to financial systems; (2) consider members who could be harmed; (3) set safety principles for the project.

### 10.1 Duties of engineers

Engineering codes of ethics ask practitioners to hold paramount the safety and welfare of the public, to act within their competence and to be honest about limits. Jonas applies these to the cooperative: members rely on credits to reduce energy bills, some are elderly or on low incomes, and errors could cost them money or trust. He writes that his duty includes refusing to deploy code he has not adequately tested, and telling the board plainly when a risk remains, even if that delays the project.

### 10.2 Who could be harmed

Jonas lists stakeholders: members who earn and spend credits; members without smartphones who rely on statements; the board, legally responsible for funds; node operators; and the local utility. For each he notes possible harms: lost credits from bugs, privacy loss if household generation patterns are published, exclusion if the system is hard to use, and liability for the board. Thinking about harm by stakeholder helps him design protections, such as keeping household readings off the shared ledger and providing paper statements on request.

### 10.3 Project safety principles

Jonas and Dr Nwosu agree principles for the project: work only on test networks and synthetic data until approved; never handle members' private keys; disclose any discovered weakness privately to the responsible party; and never publish details that could help someone take credits that are not theirs. The board adopts these principles. Written principles guide decisions when deadlines press, and make clear to everyone that security work on financial systems is done defensively and with permission. Dr Nwosu reviews them each year with the board.

### Worked example

Jonas lists five stakeholder groups and their harms; the board adopts four safety principles for the project.

> **Synthetic case.** Stakeholders and principles are synthetic.

### Errors and limits

Deploying untested code under deadline pressure puts members' money at risk.

### Exercises

- **EX028 — Paramount duty.** What do codes ask engineers to hold paramount? *Rubric:* 3 = safety and welfare of the public;; 2 = public welfare;; 1 = profit;; 0 = none.
- **EX029 — Privacy protection.** How are household patterns protected? *Rubric:* 3 = readings kept off the shared ledger;; 2 = off-chain;; 1 = published;; 0 = none.
- **EX030 — Safety principle.** Name one project safety principle. *Rubric:* 3 = never handle members' private keys;; 2 = test networks only;; 1 = vague;; 0 = none.

### Synthesis

Ethical duties and written safety principles keep financial-system engineering focused on members' welfare.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain how ledger nodes communicate; (2) describe peer-to-peer and permissioned networking; (3) protect node connections.

### 11.1 How nodes talk

A blockchain is a network of nodes that share transactions and blocks. Nakamoto's paper describes broadcasting new transactions to all nodes and having nodes accept the longest valid chain. Brightwater's permissioned ledger has three validator nodes, one at the cooperative and two at partner organisations, plus read-only nodes for applications. Jonas maps the traffic: transactions arrive at an application gateway, are forwarded to validators, and blocks are shared among validators. Understanding these paths tells him where an outage or interception would affect the system.

### 11.2 Permissioned networking

Unlike a public network where anyone can connect, Brightwater's validators accept connections only from known peers identified by certificates. Jonas learns to read the node configuration: allowed peer lists, ports and transport encryption. He finds that one partner node also exposes its administrative interface on a public address, a configuration mistake rather than an intended feature. He reports it privately to the partner, who restricts the interface to their internal network. Checking configuration against intent is a basic but valuable network security habit.

### 11.3 Protecting connections

Jonas recommends that all node-to-node and application-to-node connections use encrypted, mutually authenticated channels, that administrative interfaces are reachable only from management networks, and that each node runs on a separate provider or site so one outage does not halt the ledger. He documents the network diagram and peer list as configuration records. These measures address availability and integrity of communication, which matter as much as contract correctness because a ledger that nodes cannot reach cannot process members' transactions. Each recommendation is linked to a requirement.

### Worked example

Jonas maps three validators and gateways, finds one partner's admin interface publicly exposed, and recommends mutually authenticated channels and separated sites.

> **Synthetic case.** Nodes, partners and findings are synthetic; Nakamoto (2008) is a real source.

### Errors and limits

Exposing node administrative interfaces to public networks invites misuse.

### Exercises

- **EX031 — Validator count.** How many validators does Brightwater run? *Rubric:* 3 = three;; 2 = 3;; 1 = one;; 0 = none.
- **EX032 — Exposed interface.** What configuration mistake was found? *Rubric:* 3 = admin interface on a public address;; 2 = exposed admin;; 1 = vague;; 0 = none.
- **EX033 — Site separation.** Why run nodes at separate sites? *Rubric:* 3 = one outage does not halt the ledger;; 2 = availability;; 1 = cost;; 0 = none.

### Synthesis

Known peers, encrypted channels and protected admin interfaces secure ledger networking.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) describe processes, permissions and isolation; (2) harden node hosts; (3) manage secrets on servers.

### 12.1 Processes and permissions

An operating system runs programs as processes with permissions limiting what each can do. Jonas learns how user accounts, file permissions and service accounts work on Linux servers that host ledger nodes. He checks that the node software runs as its own unprivileged user rather than as the system administrator, so a fault in the node cannot change the rest of the server. Least privilege at the operating-system level is the same principle as in contract access control: give each component only what it needs.

### 12.2 Hardening hosts

Hardening reduces what could go wrong on a server. Jonas's checklist for node hosts includes applying security updates promptly, disabling unused services, restricting remote administration to named administrators with strong authentication, enabling a host firewall that allows only required ports, and synchronising clocks, since block timestamps and logs depend on accurate time. He applies the checklist to the cooperative's node in a test environment first, then in production during an agreed window, recording each change. He reruns the checklist quarterly and records any drift found.

### 12.3 Secrets on servers

Validator nodes hold signing keys that authorise blocks. If stolen, a key could let someone impersonate a validator. Jonas recommends storing validator keys in a hardware security module or at least an encrypted keystore readable only by the node user, never in shared folders or code repositories. He also recommends separate keys per node and a documented process for rotating them. The EthTrust specification's security considerations mention hardware security modules for critical key storage, which supports this choice. Rotation is rehearsed on the test network.

### Worked example

The node runs as an unprivileged user; a hardening checklist is applied in test then production; validator keys move to protected storage with rotation documented.

> **Synthetic case.** Servers, keys and changes are synthetic; EEA EthTrust is a real source.

### Errors and limits

Storing validator signing keys in shared folders or repositories exposes them to theft.

### Exercises

- **EX034 — Node user.** How should node software run? *Rubric:* 3 = as its own unprivileged user;; 2 = unprivileged;; 1 = as root;; 0 = none.
- **EX035 — Clock reason.** Why synchronise clocks? *Rubric:* 3 = timestamps and logs depend on accurate time;; 2 = time;; 1 = speed;; 0 = none.
- **EX036 — Key storage.** Where should validator keys be stored? *Rubric:* 3 = HSM or encrypted keystore for node user only;; 2 = protected store;; 1 = repository;; 0 = none.

### Synthesis

Least privilege, hardened hosts and protected keys secure the machines beneath the ledger.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) design on-chain and off-chain data; (2) link them with hashes; (3) protect member privacy.

### 13.1 What goes where

Not all data belongs on a ledger. Jonas sorts Brightwater's data into three groups: data that must be shared and tamper-evident, such as credit balances and transfers; data that is private, such as household names and detailed meter readings; and operational data, such as logs. Balances go on-chain; private data stays in the cooperative's database; operational data goes to a logging system. NIST IR 8202 notes that data on a ledger is hard to remove, which is a strong reason to keep personal data off it.

### 13.2 Linking with hashes

To connect off-chain readings with on-chain credits without publishing readings, Jonas designs a monthly commitment: the cooperative computes a hash summarising all readings and publishes only that hash on-chain. Later, anyone given a household's readings can check they match the commitment. This lets disputes be resolved with evidence while keeping data private. He notes that hashes of small, guessable data, such as a single reading, could be reversed by trying all values, so commitments include random padding. The padding is stored securely with the readings.

### 13.3 Database protection

The off-chain database now holds the most sensitive data. Jonas applies standard protections: access restricted to named staff, encryption at rest, backups tested by restoration, and audit logging of queries. He also plans data retention: readings older than seven years are deleted unless needed for a dispute. Moving data off-chain does not remove the need to secure it; it moves the responsibility to systems the cooperative controls, where conventional security practices apply. Jonas tests restoration quarterly and records the time taken, so the board knows how long recovery would take.

### Worked example

Balances go on-chain, readings stay off-chain with monthly padded hash commitments, and the database is encrypted, access-logged and backed up.

> **Synthetic case.** Data and designs are synthetic; NIST IR 8202 is a real source.

### Errors and limits

Putting personal data on a ledger makes it practically impossible to remove later.

### Exercises

- **EX037 — On-chain data.** Which data goes on-chain? *Rubric:* 3 = credit balances and transfers;; 2 = balances;; 1 = names;; 0 = none.
- **EX038 — Commitment design.** How are readings linked to the ledger? *Rubric:* 3 = monthly hash commitment published on-chain;; 2 = hash;; 1 = full data;; 0 = none.
- **EX039 — Padding reason.** Why add random padding to commitments? *Rubric:* 3 = small guessable data could be reversed by trying values;; 2 = guessing;; 1 = style;; 0 = none.

### Synthesis

Careful placement of data, hash commitments and database protection balance transparency and privacy.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) apply development lifecycle practices; (2) use version control and review; (3) manage dependencies safely.

### 14.1 Lifecycle

Jonas follows a lifecycle: requirements, design, implementation, verification, deployment and maintenance, with each stage producing artefacts that the next uses. For contracts, the lifecycle has an unusual feature: after deployment, code is hard or impossible to change, so verification must be thorough before release. The EthTrust specification notes that the cost of patching contracts after deployment is generally much higher than in other software. Jonas plans more time for review and testing than he would for an ordinary web application.

### 14.2 Version control and review

All code, configuration and documentation live in version control. Every change goes through a pull request reviewed by another person, with tests run automatically. Jonas learns to write small, focused changes with clear descriptions, because reviewers catch more in small changes. He also tags each released version and records the exact compiler version and settings used, so the deployed bytecode can be reproduced and matched to reviewed source, a requirement EthTrust places on conformance claims. Reviewers use a short checklist for each change.

### 14.3 Dependencies

Contracts and tools depend on libraries written by others. Jonas lists every dependency, pins exact versions and records where each came from. He prefers widely reviewed libraries and reads release notes before upgrading. He notes the risk that a dependency could be compromised or contain a bug, and plans to review changes in dependencies with the same care as the cooperative's own code. Supply-chain care matters especially when code will control value and cannot easily be patched. Each upgrade is recorded in a decision note.

### Worked example

The project records compiler versions and settings for reproducible builds, uses reviewed pull requests, and pins all dependencies.

> **Synthetic case.** Code, reviews and dependencies are synthetic; EEA EthTrust is a real source.

### Errors and limits

Upgrading dependencies without reading changes can import bugs into code that controls value.

### Exercises

- **EX040 — Lifecycle difference.** What is unusual about the contract lifecycle? *Rubric:* 3 = code is hard to change after deployment;; 2 = immutability;; 1 = vague;; 0 = none.
- **EX041 — Build record.** What is recorded for each release? *Rubric:* 3 = exact compiler version and settings;; 2 = compiler;; 1 = nothing;; 0 = none.
- **EX042 — Dependency practice.** How are dependencies managed? *Rubric:* 3 = listed, pinned, provenance recorded;; 2 = pinned;; 1 = latest always;; 0 = none.

### Synthesis

Disciplined lifecycle, review and dependency practices suit code that is hard to change after deployment.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to ledgers; (2) describe common contract weakness classes; (3) think like a defender.

### 15.1 CIA for ledgers

Jonas applies the classic security goals. Integrity matters most for balances: credits must not be created, lost or moved without authority. Availability matters because members need to use credits when bills are due. Confidentiality matters for household data kept off-chain. He notes that blockchains strengthen integrity through replication and consensus, but can weaken confidentiality because shared data is visible to all nodes. Balancing these goals shapes the design decisions in later chapters. He writes one sentence per goal explaining how the platform will meet it, which the board reads before approving design work.

### 15.2 Weakness classes

Jonas studies weakness classes from the SWC registry and the OWASP Smart Contract Top 10, including access control flaws, re-entrancy where an external call lets code be entered again before state is updated, unchecked external call results, arithmetic and rounding errors, and reliance on manipulable price data. Atzei and colleagues (2017) organise similar weaknesses by their cause. He studies each from the defender's side: what the weakness is, why it occurs, and which design patterns and review checks prevent it.

Re-entrancy, for example, is prevented by updating state before any external call, a check a reviewer can confirm line by line.

### 15.3 Defender's mindset

Thinking like a defender means asking what could go wrong for each function and who could cause it, intentionally or by mistake. Jonas practises with the cooperative's planned transfer function: what if amounts are zero, larger than balances, or sent to the contract itself; what if the function is called twice at once; what if an administrator key is lost. Each question becomes a requirement or test. The aim is to find problems on paper and in tests before anyone else finds them in production.

### Worked example

Jonas maps integrity, availability and confidentiality to the ledger, studies five weakness classes from public registries, and turns failure questions into requirements.

> **Synthetic case.** Functions and questions are synthetic; the SWC registry, OWASP Smart Contract Top 10 and Atzei et al. (2017) are real sources.

### Errors and limits

Learning weaknesses as attack recipes rather than as design failures to prevent misdirects defensive effort.

### Exercises

- **EX043 — Most important goal.** Which goal matters most for balances? *Rubric:* 3 = integrity;; 2 = correctness;; 1 = confidentiality;; 0 = none.
- **EX044 — Ledger weakness.** Which goal can blockchains weaken? *Rubric:* 3 = confidentiality;; 2 = privacy;; 1 = integrity;; 0 = none.
- **EX045 — Re-entrancy meaning.** What is re-entrancy? *Rubric:* 3 = an external call lets code be entered again before state is updated;; 2 = re-entry;; 1 = overflow;; 0 = none.

### Synthesis

Security goals, weakness classes and a defender's questions provide the foundation for contract security.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) view the token platform as a system of systems; (2) manage interfaces; (3) trace requirements across components.

### 16.1 System of systems

Brightwater's platform is more than contracts: meters, a data gateway, the off-chain database, the ledger with validators, contracts, a member web app, paper statements and support staff. Jonas draws a context diagram showing each component and its interfaces. Systems engineering teaches that failures often occur at interfaces, where assumptions differ, such as the gateway assuming meter timestamps are in UTC while meters report local time. Seeing the whole system helps him find such mismatches early. He reviews the diagram with each component owner.

### 16.2 Interface agreements

For each interface Jonas writes an agreement: data format, units, timing, error handling and who owns it. The meter-to-gateway agreement states readings in watt-hours with UTC timestamps and signed by the device. The gateway-to-contract agreement states that minting requests are batched hourly and must not exceed the capacity bound. Written agreements turn implicit assumptions into checked rules, and they give reviewers something concrete to verify at each boundary. Each agreement is signed by both owners and stored with the architecture records, and any change requires the agreement to be updated before code changes are merged.

### 16.3 Traceability

Jonas builds a traceability matrix linking each requirement to the components that implement it and the tests that verify it. For example, the requirement that no more credits are minted than generation allows traces to the gateway's bound check, the contract's per-hour cap and a monitoring alert, each with a test. When a requirement changes, the matrix shows what else must change. Traceability is how engineers show that a system does what was intended, not just that each part works alone.

### Worked example

A context diagram exposes a UTC versus local-time mismatch; interface agreements and a traceability matrix link the minting cap to three components and tests.

> **Synthetic case.** Components and requirements are synthetic.

### Errors and limits

Testing components separately without checking interfaces misses mismatched assumptions.

### Exercises

- **EX046 — Interface failure.** What interface mismatch was found? *Rubric:* 3 = UTC versus local timestamps;; 2 = time zones;; 1 = vague;; 0 = none.
- **EX047 — Agreement content.** Name two items in an interface agreement. *Rubric:* 3 = format and units;; 2 = timing, owner;; 1 = colour;; 0 = none.
- **EX048 — Minting trace.** Which components implement the minting cap? *Rubric:* 3 = gateway check, contract cap, monitoring alert;; 2 = three;; 1 = one;; 0 = none.

### Synthesis

Context diagrams, interface agreements and traceability manage complexity across a token platform.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) describe feedback loops; (2) relate them to monitoring and response; (3) design safe automatic responses.

### 17.1 Feedback loops

Control theory studies systems that measure output and adjust input to reach a goal. A thermostat measures temperature and switches heating. Jonas sees a parallel in security operations: monitoring measures system behaviour, compares it with expected behaviour and triggers a response. Like any control loop, monitoring has delay, noise and the risk of overreacting. Understanding feedback helps him design responses that stabilise the system rather than causing new problems. He sketches the loop for the token platform, labelling the sensor, the comparison, the controller and the actuator, so that each part can be examined for delay and error.

### 17.2 Monitoring as feedback

For the token platform, Jonas defines measured signals: minting per hour, transfers per hour, queued administrative actions and node health. Each signal has a set point or range and an alert threshold. When minting exceeds the capacity bound, the loop should respond. He considers delays: an alert that takes a day to reach a human is too slow for a problem that grows each hour. The EthTrust specification notes that monitoring can enable rapid response but that automated responses can also be triggered deliberately to cause disruption.

### 17.3 Safe automatic responses

Jonas designs a limited automatic response: if minting exceeds the cap, the gateway stops submitting new minting requests and alerts staff, but the contract itself is not paused automatically, because pausing affects all members. A pause requires a multi-signature decision by two board members within a documented procedure. This balances speed with caution. Feedback design teaches that the safest automatic responses are narrow and reversible, with broader actions left to humans who can judge context. The procedure is written into the runbook and tested.

### Worked example

Jonas defines four monitored signals and an automatic gateway stop for excess minting, while contract pauses require a two-person decision.

> **Synthetic case.** Signals and procedures are synthetic; EEA EthTrust is a real source.

### Errors and limits

Automatically pausing an entire contract on any alert lets false alarms, or deliberate triggers, disrupt all members.

### Exercises

- **EX049 — Control parallel.** What does monitoring parallel in control theory? *Rubric:* 3 = a feedback loop;; 2 = loop;; 1 = open loop;; 0 = none.
- **EX050 — Automatic action.** What happens automatically on excess minting? *Rubric:* 3 = gateway stops minting requests and alerts staff;; 2 = gateway stop;; 1 = contract paused;; 0 = none.
- **EX051 — Pause decision.** Who decides a contract pause? *Rubric:* 3 = two board members via multisig;; 2 = two people;; 1 = script;; 0 = none.

### Synthesis

Monitoring is a feedback loop; safe responses are narrow, fast and reversible, with broad actions left to people.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) define trust boundaries for the platform; (2) choose defence in depth; (3) document the security architecture.

### 18.1 Trust boundaries

A trust boundary is where data or control passes between parts with different levels of trust. Jonas marks boundaries on the context diagram: between meters and the gateway, between the internet and the member app, between the cooperative's systems and partner validators, and between administrators and contracts. Each boundary needs checks: authentication, validation or authorisation. Boundaries also show where an assumption about trust is being made, such as trusting partner validators to follow the agreed software version. He lists the check required at each boundary.

### 18.2 Defence in depth

Jonas layers protections so no single failure causes harm. For minting, the gateway checks capacity, the contract enforces an hourly cap, the minting role requires a multi-signature, a timelock delays role changes and monitoring alerts on anomalies. If any one layer fails, others still limit damage. He documents which threat each layer addresses and what happens if it fails. Defence in depth is especially valuable in contract systems because a single unnoticed flaw can otherwise have permanent effects. The board reviews the layers yearly.

### 18.3 Architecture document

The security architecture document describes components, trust boundaries, data flows, privileged roles, key management, monitoring and incident response. It references public guidance, including EthTrust's discussion of upgradeable contracts and ConsenSys best practices. Jonas presents it to Dr Nwosu and a partner engineer, who ask him to add how validator software upgrades are coordinated. The document becomes the reference against which later designs and reviews are checked. He adds the requested section, records the reviewers' comments and their resolution, and stores the document with the decision records so that later changes to the architecture can be compared against it.

### Worked example

Jonas marks four trust boundaries, layers five protections around minting and writes a security architecture document reviewed by two engineers.

> **Synthetic case.** Components and reviews are synthetic; EEA EthTrust and ConsenSys best practices are real sources.

### Errors and limits

Relying on a single control for a high-value function leaves no protection if it fails.

### Exercises

- **EX052 — Boundary example.** Name one trust boundary. *Rubric:* 3 = meters to gateway;; 2 = admin to contracts;; 1 = vague;; 0 = none.
- **EX053 — Minting layers.** How many layers protect minting? *Rubric:* 3 = five;; 2 = 5;; 1 = one;; 0 = none.
- **EX054 — Review addition.** What did reviewers ask to add? *Rubric:* 3 = coordination of validator software upgrades;; 2 = upgrades;; 1 = nothing;; 0 = none.

### Synthesis

Clear trust boundaries and layered controls, documented in one architecture, guide secure design.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) explain keys, signatures and addresses; (2) verify Merkle inclusion proofs; (3) plan key custody.

### 19.1 Keys and signatures

Blockchain identities are key pairs. A private key signs transactions; the matching public key, or an address derived from it, lets anyone verify the signature. Wood's yellow paper specifies how Ethereum accounts and signatures work. Jonas learns that whoever holds a private key controls the account, with no password reset. This makes key custody the central identity question: losing a key loses access, and leaking it gives control to someone else. Members' keys, administrator keys and validator keys each need different custody arrangements.

### 19.2 Merkle trees

A Merkle tree hashes data in pairs up to a single root, so one short root commits to many items. A proof that an item is included needs only the hashes along its path, a logarithmic number. Brightwater's monthly commitment of meter readings uses a Merkle root, so a household can verify its own readings were included without seeing others'. Jonas writes a standard-library script to build a tree over eight synthetic readings and verify inclusion proofs, which only reads data and prints results.

### Lab — Merkle inclusion

```python
"""Merkle root and inclusion-proof verification for synthetic meter readings (read-only)."""
import hashlib
H = lambda b: hashlib.sha256(b).digest()
LEAVES = [f"meter-{i:02d}:{kwh}".encode() for i, kwh in enumerate([12, 9, 15, 7, 11, 14, 8, 10])]

def levels(leaves):
    lv = [[H(x) for x in leaves]]
    while len(lv[-1]) > 1:
        cur = lv[-1]; lv.append([H(cur[i] + cur[i + 1]) for i in range(0, len(cur), 2)])
    return lv

def proof(lv, idx):
    out = []
    for layer in lv[:-1]:
        sib = idx ^ 1; out.append((layer[sib], sib < idx)); idx //= 2
    return out

def check(leaf, pr, root):
    h = H(leaf)
    for sib, left in pr:
        h = H(sib + h) if left else H(h + sib)
    return h == root

def main():
    lv = levels(LEAVES); root = lv[-1][0]
    print("leaves", len(LEAVES), "root", root.hex()[:12], "proof length", len(proof(lv, 5)))
    print("meter-05 included:", check(LEAVES[5], proof(lv, 5), root))
    print("altered meter-05 included:", check(b"meter-05:41", proof(lv, 5), root))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_merkle.py`. Verified output:

```text
leaves 8 root 88c2dfaf0abe proof length 3
meter-05 included: True
altered meter-05 included: False
```

### 19.3 Reading the proof

The script builds a tree over eight readings, prints the root and produces a three-hash proof for meter-05. The genuine reading verifies as included; an altered reading with the same proof does not. Jonas notes that proofs are short because the tree has three levels, and that the root must be obtained from the ledger, not from the party providing the proof, otherwise the check is meaningless. He then drafts custody plans: members may use cooperative-managed custody or their own wallets; administrators use hardware keys within multi-signature wallets.

### Worked example

The lab verifies meter-05's reading with a three-hash proof and rejects an altered value; custody plans distinguish member, administrator and validator keys.

> **Synthetic case.** Readings, keys and plans are synthetic; Wood's yellow paper is a real source.

### Errors and limits

Checking a Merkle proof against a root supplied by the same party as the proof gives no assurance.

### Exercises

- **EX055 — Key loss.** What happens if a private key is lost? *Rubric:* 3 = access is lost with no reset;; 2 = lost access;; 1 = reset;; 0 = none.
- **EX056 — Proof size.** How many hashes were in meter-05's proof? *Rubric:* 3 = three;; 2 = 3;; 1 = eight;; 0 = none.
- **EX057 — Root source.** Where must the root come from? *Rubric:* 3 = the ledger, not the proof provider;; 2 = ledger;; 1 = provider;; 0 = none.

### Synthesis

Keys, signatures and Merkle proofs underpin identity and verifiable data, with custody as the central risk.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Web3, blockchain and cryptoasset security: engineering context

### Learning outcomes

You will (1) describe the cooperative's token system in context; (2) identify stakeholders and constraints; (3) define the engineering problem.

### 20.1 The system in context

Entering the specialist part of the degree, Jonas restates the engineering problem. Brightwater wants members to earn credits for solar generation and spend them on energy bills or transfer them to neighbours. The system must be accurate, available, private for household data and understandable to members. It runs on the cooperative's permissioned ledger with two partner validators. Constraints include a small budget, one part-time developer, members with varying digital skills and regulatory obligations around financial records. He writes these down as the project's starting facts.

### 20.2 Stakeholders and constraints

Jonas revisits stakeholders with new detail. Members want reliability and simplicity; the board wants accountability and low risk; partners want clear operating agreements; the utility wants accurate redemption data; auditors want evidence. Constraints shape solutions: with one developer, the design must be simple enough to maintain; with limited budget, external audits must be targeted. He records each constraint and how it influences choices, so that later designs can be judged against reality, not an ideal. The board confirms the list before design starts.

### 20.3 The engineering problem

Jonas writes the problem statement: design, implement and verify a credit token system and its operations so that credits are issued only for verified generation, transferred only by their holders, redeemable reliably, and governed by accountable, transparent controls, while keeping household data private. Each phrase becomes a requirement area in the next chapter. A precise problem statement keeps a multi-year project focused and gives reviewers a standard against which to judge the final result. Dr Nwosu and the board approve the statement as written.

### Worked example

Jonas writes a one-paragraph problem statement covering issuance, transfer, redemption, governance and privacy, with recorded constraints.

> **Synthetic case.** The cooperative, stakeholders and constraints are synthetic.

### Errors and limits

Starting design without stating constraints leads to solutions the cooperative cannot maintain.

### Exercises

- **EX058 — Credit uses.** What can members do with credits? *Rubric:* 3 = spend on bills or transfer to neighbours;; 2 = spend;; 1 = mine;; 0 = none.
- **EX059 — Developer constraint.** What does having one developer imply? *Rubric:* 3 = design must be simple to maintain;; 2 = simplicity;; 1 = vague;; 0 = none.
- **EX060 — Problem areas.** Name two requirement areas from the statement. *Rubric:* 3 = issuance and governance;; 2 = transfer, privacy;; 1 = colour;; 0 = none.

### Synthesis

A clear problem statement grounded in stakeholders and constraints frames the specialist engineering work.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Web3, blockchain and cryptoasset security: requirements

### Learning outcomes

You will (1) write security requirements for issuance, transfer and governance; (2) make them testable; (3) prioritise them.

### 21.1 Functional security requirements

Jonas writes requirements as testable statements. Issuance: credits are minted only by the minting role, only against signed meter batches, and never above the hourly capacity cap. Transfer: only the holder can move their credits, amounts are positive integers, and balances never go negative. Redemption: redeemed credits are burned and reported to the utility within a day. Each statement names who, what and under which condition, so that a test or review can check it. Vague requirements such as "the system must be secure" are rewritten until they say exactly what secure means here.

### 21.2 Governance requirements

Governance requirements cover privileged actions. Any change to contract code, the minting role or the cap requires approval by three of five board keyholders and a 48-hour timelock before execution, giving members and monitors time to see it. Emergency pause requires two of five and is announced to members within an hour. All privileged actions are logged with a change reference. Jonas links these to EthTrust's recommendation of timelock delays for sensitive operations and to its discussion of access control for upgradeable contracts, citing sources for each choice.

### 21.3 Testability and priority

For each requirement Jonas notes how it will be verified: unit test, property test, review checklist item, configuration check or monitoring alert. He then prioritises using impact on members and likelihood: minting controls and transfer correctness are highest, redemption reporting next, and user interface conveniences lowest. The board reviews the list and agrees the priorities. Testable, prioritised requirements let a small team focus scarce review time where failure would cause the most harm. The list is revisited whenever the threat analysis changes, so priorities stay aligned with risk.

### Worked example

Jonas writes issuance, transfer, redemption and governance requirements with a verification method each; minting and transfer correctness are ranked highest.

> **Synthetic case.** Requirements and priorities are synthetic; EEA EthTrust is a real source.

### Errors and limits

Writing requirements like "the system must be secure" gives reviewers nothing to check.

### Exercises

- **EX061 — Minting requirement.** Under what conditions may credits be minted? *Rubric:* 3 = by minting role, against signed batches, under hourly cap;; 2 = three conditions;; 1 = anytime;; 0 = none.
- **EX062 — Upgrade approval.** What approval do code changes need? *Rubric:* 3 = three of five keyholders and a 48-hour timelock;; 2 = 3-of-5 plus timelock;; 1 = one person;; 0 = none.
- **EX063 — Highest priority.** Which requirements are highest priority? *Rubric:* 3 = minting controls and transfer correctness;; 2 = minting;; 1 = interface;; 0 = none.

### Synthesis

Testable, sourced and prioritised requirements guide design and verification effort.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Web3, blockchain and cryptoasset security: system and data models

### Learning outcomes

You will (1) model contract state and transitions; (2) model roles and data flows; (3) check models against requirements.

### 22.1 State model

Jonas models the credit contract as a state machine. State includes balances, total supply, the hourly minted amount, the paused flag and role assignments. Transitions are mint, transfer, burn, pause, unpause and role changes, each with preconditions and effects. Writing the model before code clarifies questions: does pausing stop burning for redemption? He decides it should not, so members can still redeem during an investigation, and records this as a requirement. A state model is the specification against which code and tests are later checked.

### 22.2 Roles and flows

A role model lists each role, who holds it and what transitions it may perform: holders transfer and burn their own credits; the minting role, held by the gateway's multi-signature wallet, mints; the governance role, held by the board multi-signature with timelock, changes parameters; the pauser role, held by a two-of-five board wallet, pauses. Data-flow diagrams show readings moving from meters to the gateway, batches to the contract and redemption events to the utility. Together, these models show who can change what, and where data goes.

### 22.3 Checking models

Jonas checks the models against requirements using the traceability matrix. He finds one gap: the model lets the governance role change the minting cap without limit, so a mistaken change could allow far more minting than generation supports. He adds a requirement that the cap cannot exceed the capacity bound defined in configuration, itself changeable only through governance with a timelock. Checking models before implementation finds design errors when they are cheapest to fix, long before code exists. The fix is traced in the matrix.

### Worked example

The state model clarifies that burning continues while paused; a model check finds an unbounded cap change and adds a capacity limit.

> **Synthetic case.** Models and roles are synthetic.

### Errors and limits

Writing code before modelling state and roles leaves design gaps to be discovered in production.

### Exercises

- **EX064 — Pause decision.** Does pausing stop burning for redemption? *Rubric:* 3 = no, members can still redeem;; 2 = no;; 1 = yes;; 0 = none.
- **EX065 — Minting role holder.** Who holds the minting role? *Rubric:* 3 = the gateway's multisig wallet;; 2 = gateway multisig;; 1 = a member;; 0 = none.
- **EX066 — Model gap.** What gap did the model check find? *Rubric:* 3 = unbounded cap change by governance;; 2 = cap;; 1 = vague;; 0 = none.

### Synthesis

State, role and data-flow models make designs checkable against requirements before implementation.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Web3, blockchain and cryptoasset security: threat and failure analysis

### Learning outcomes

You will (1) identify threats and failures systematically; (2) rank them by impact and likelihood; (3) map them to controls.

### 23.1 Systematic identification

Jonas works through each component and interface, asking what could go wrong from malicious action, error or failure. He uses weakness classes from the SWC registry and the OWASP Smart Contract Top 10 as prompts for contract threats, and adds operational failures: lost administrator keys, validator outages, meter firmware faults and gateway bugs. Each item records the component, cause, effect on members and existing controls. A systematic method ensures familiar risks are not the only ones considered. He reviews the list with the developer.

### 23.2 Ranking

He ranks each threat and failure by impact on members and likelihood given current controls, using a simple three-level scale and a short justification. Highest-ranked items include a compromised gateway key minting excessive credits, a contract error allowing balances to go negative, and loss of two board keys preventing governance actions. Lower items include temporary loss of one validator. Ranking is judgement, so Jonas records reasons and asks a partner engineer to challenge the top ten. The challenge moves two items up a level.

### 23.3 Mapping to controls

Each high-ranked item maps to controls from the architecture: the gateway key is in a two-of-three multi-signature with the hourly cap and monitoring; negative balances are prevented by checks and tested as an invariant; board key loss is handled by five keyholders with a threshold of three and a documented key replacement procedure. Items without adequate controls become actions with owners. Mapping threats to controls shows whether the design addresses what matters, and exposes gaps for the next design iteration.

### Worked example

Jonas lists 34 threats and failures, ranks three as highest, and maps each to controls, leaving two actions for the design studio.

> **Synthetic case.** Threats, rankings and actions are synthetic; the SWC registry and OWASP Smart Contract Top 10 are real sources.

### Errors and limits

Considering only well-publicised contract attacks misses operational failures like lost keys.

### Exercises

- **EX067 — Prompt sources.** What prompts contract threats? *Rubric:* 3 = SWC registry and OWASP Smart Contract Top 10;; 2 = registries;; 1 = news;; 0 = none.
- **EX068 — Top threat.** Name a highest-ranked item. *Rubric:* 3 = compromised gateway key minting excess;; 2 = negative balances;; 1 = one validator down;; 0 = none.
- **EX069 — Key-loss control.** How is board key loss addressed? *Rubric:* 3 = five keyholders, threshold three, replacement procedure;; 2 = 3 of 5;; 1 = nothing;; 0 = none.

### Synthesis

Systematic, ranked and mapped threat analysis connects risks to concrete controls.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Web3, blockchain and cryptoasset security: methods I

### Learning outcomes

You will (1) use invariants to reason about token systems; (2) replay logs to check invariants; (3) interpret violations.

### 24.1 Invariants

An invariant is a property that must hold in every state. For the credit system, Jonas states three: the sum of all balances equals total supply; no balance is negative; and total supply never exceeds the configured cap. The EthTrust specification describes invariant testing as checking assumptions that should remain true in all circumstances. Invariants are powerful because they do not depend on particular inputs: if any sequence of operations breaks one, there is a defect or misuse to investigate.

### 24.2 Replaying logs

Jonas writes a standard-library script that replays a synthetic log of mints, transfers and burns, tracking balances and supply, and reports any step that would break an invariant. It reads only the synthetic log and prints results. Replaying recorded history against invariants is a practical method for both testing contracts before deployment and auditing operations afterwards, because it checks what actually happened rather than what was intended. Jonas tests the script first on a short log with one deliberate overdraft and one deliberate cap breach, confirming that both are reported at the expected steps before using the lab log.

### Lab — Invariant replay

```python
"""Replay a synthetic token log and check supply invariants (read-only)."""
LOG = [("mint", None, "coop", 1000), ("transfer", "coop", "h01", 200), ("transfer", "coop", "h02", 150),
       ("transfer", "h01", "h03", 50), ("burn", "h02", None, 30), ("transfer", "h03", "h04", 60),
       ("transfer", "h02", "h05", 100), ("mint", None, "coop", 500)]
CAP = 1400

def main():
    bal, supply, issues = {}, 0, []
    for i, (op, src, dst, amt) in enumerate(LOG):
        if src is not None:
            if bal.get(src, 0) < amt:
                issues.append(f"step {i}: {src} balance {bal.get(src, 0)} < {amt}"); continue
            bal[src] -= amt
        if dst is not None:
            bal[dst] = bal.get(dst, 0) + amt
        supply += amt if op == "mint" else -amt if op == "burn" else 0
        if supply > CAP:
            issues.append(f"step {i}: supply {supply} exceeds cap {CAP}")
        if sum(bal.values()) != supply:
            issues.append(f"step {i}: balances != supply")
    print("steps", len(LOG), "final supply", supply, "holders", sum(1 for v in bal.values() if v))
    for x in issues:
        print("issue:", x)

if __name__ == "__main__":
    main()
```

Run with `python3 lab_invariant.py`. Verified output:

```text
steps 8 final supply 1470 holders 5
issue: step 5: h03 balance 50 < 60
issue: step 7: supply 1470 exceeds cap 1400
```

### 24.3 Interpreting violations

The replay processes eight steps and reports two issues. At step 5, h03 tries to transfer 60 while holding only 50; the script rejects the step, as a correct contract would. At step 7, a mint raises supply to 1,470, above the 1,400 cap, meaning the synthetic log contains a mint the cap should have blocked. Jonas explains that the first is the system working correctly, while the second indicates either a cap misconfiguration or a missing check, and would trigger investigation.

Separating expected rejections from unexpected successes keeps the replay from raising alarms on correct behaviour.

### Worked example

The replay of eight steps rejects an overdraft at step 5 and flags supply of 1,470 exceeding the 1,400 cap at step 7.

> **Synthetic case.** The log and script are synthetic; EEA EthTrust is a real source.

### Errors and limits

Treating every invariant report as an attack ignores cases where the check simply rejected invalid input.

### Exercises

- **EX070 — Three invariants.** State the three invariants. *Rubric:* 3 = balances sum to supply, none negative, supply under cap;; 2 = three;; 1 = one;; 0 = none.
- **EX071 — Step 5 meaning.** What does step 5 show? *Rubric:* 3 = an overdraft correctly rejected;; 2 = rejection;; 1 = attack;; 0 = none.
- **EX072 — Step 7 meaning.** What does step 7 show? *Rubric:* 3 = supply 1,470 exceeds 1,400 cap;; 2 = cap breach;; 1 = nothing;; 0 = none.

### Synthesis

Invariants checked by replay reveal defects and misconfigurations that example tests can miss.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) develop alternative designs collaboratively; (2) critique designs against requirements; (3) choose a direction.

### 25.1 Studio format

In the first design studio, Jonas and three classmates each sketch a design for credit issuance and governance, then present to peers and Dr Nwosu. Each design must state assumptions, show the state and role models, and explain how it meets the top requirements. The studio format encourages divergent thinking first and critique second, so that the team does not lock onto the first idea. Jonas's design uses a single credit contract with role-based access; a classmate proposes separate contracts for minting and transfers.

### 25.2 Critique

Critique follows a structure: does the design meet each high-priority requirement, what new risks does it introduce, and can the cooperative maintain it? Peers point out that Jonas's single contract concentrates all roles in one place, making upgrades riskier, while the split design adds interfaces between contracts that need careful checking. A partner engineer notes that the split design's minting contract could be simpler to review. Structured critique turns opinions into reasons linked to requirements. Jonas records every critique point with its reasoning.

### 25.3 Choosing a direction

The studio agrees to carry two alternatives forward for formal comparison in the next chapter: a single contract with roles, and a split design with a minimal minting contract. Jonas records the decision and the reasons, and lists questions to answer, such as how upgrades would work in each. Choosing a direction does not mean picking a winner yet; it means narrowing options to those worth analysing carefully. The studio's record becomes part of the design history. The questions guide the next chapter's analysis.

### Worked example

Four designs are presented; critique narrows them to a single role-based contract and a split design with a minimal minting contract.

> **Synthetic case.** Designs, students and critiques are synthetic.

### Errors and limits

Adopting the first design without considering alternatives misses better options.

### Exercises

- **EX073 — Studio requirement.** What must each studio design state? *Rubric:* 3 = assumptions, models and how it meets top requirements;; 2 = assumptions;; 1 = colours;; 0 = none.
- **EX074 — Single-contract concern.** What concern was raised about Jonas's design? *Rubric:* 3 = concentrates roles, riskier upgrades;; 2 = concentration;; 1 = vague;; 0 = none.
- **EX075 — Carried forward.** How many alternatives were carried forward? *Rubric:* 3 = two;; 2 = 2;; 1 = four;; 0 = none.

### Synthesis

Studios generate alternatives and critique them against requirements before committing.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Web3, blockchain and cryptoasset security: architecture alternatives

### Learning outcomes

You will (1) compare architectures with criteria; (2) analyse upgradeability options; (3) select and justify an architecture.

### 26.1 Criteria

Jonas compares the two alternatives using weighted criteria agreed with the board: security of minting, reviewability, upgrade safety, operational simplicity and cost. Each criterion has a definition and a scoring guide from one to three. He scores both designs with a partner engineer, who scores independently first. Differences are discussed and reasons recorded. Weighted criteria make the comparison transparent, so that the board can see why a recommendation was made and challenge specific scores. The criteria and weights are agreed before any design is scored, so they cannot be tuned to favour one option.

### 26.2 Upgradeability options

Both designs must handle future changes. Options include deploying immutable contracts and migrating to new ones when needed, or using a proxy pattern where the code behind an address can be replaced. The EthTrust specification explains that proxies mean the system cannot be treated as immutable, and that each new implementation needs review. Jonas recommends a proxy only for the transfer contract, with upgrades requiring three of five keyholders and a 48-hour timelock, and an immutable minting contract that is simple enough to replace by migration.

### 26.3 Selection

The split design scores 2.6 against 2.2 for the single contract, mainly because the minimal minting contract is easier to review and does not need upgradeability. Jonas presents the result with its sensitivity: if operational simplicity were weighted twice as heavily, the single contract would win narrowly. The board selects the split design, accepting extra interface testing. Reporting sensitivity shows decision-makers how robust a recommendation is, rather than presenting a single number as certain. The decision record includes the scores, weights and sensitivity result.

### Worked example

The split design scores 2.6 against 2.2; sensitivity shows the result would reverse if simplicity were weighted double; the board selects the split design.

> **Synthetic case.** Scores and designs are synthetic; EEA EthTrust is a real source.

### Errors and limits

Presenting a weighted score without its sensitivity hides how fragile the choice may be.

### Exercises

- **EX076 — Independent scoring.** Why does the partner score independently first? *Rubric:* 3 = to expose differences in judgement;; 2 = independence;; 1 = speed;; 0 = none.
- **EX077 — Proxy use.** Where is a proxy used? *Rubric:* 3 = only for the transfer contract;; 2 = transfer;; 1 = everywhere;; 0 = none.
- **EX078 — Final scores.** What were the final scores? *Rubric:* 3 = split 2.6, single 2.2;; 2 = 2.6 vs 2.2;; 1 = equal;; 0 = none.

### Synthesis

Transparent criteria, careful upgrade choices and sensitivity analysis justify architecture selection.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Web3, blockchain and cryptoasset security: control design

### Learning outcomes

You will (1) design privileged-role controls; (2) check role configuration against policy; (3) close gaps before deployment.

### 27.1 Role policy

Jonas writes a role policy: any function that mints, upgrades, moves reserves or changes data sources or fees must require at least two signers and a timelock of at least 48 hours, except pause, which needs two signers but no timelock because its purpose is fast protection. The policy reflects EthTrust guidance on timelocks for sensitive operations and ConsenSys advice on restricting administrative power. Writing the policy as rules allows automatic checking of configurations against it. The board approves the policy as a formal document.

### 27.2 Checking configuration

Jonas writes a standard-library script that reads a synthetic inventory of privileged functions across four contracts, with controller type, signers required and timelock hours, and reports any function that breaks the policy. It only reads the inventory and prints findings for review. Configuration drift is common in practice: a function may be deployed with a temporary single key during testing and never moved to the multi-signature wallet. Jonas tests the script on a small inventory with known breaches first, then runs it against the full synthetic inventory and records the date of each run so later runs can show drift.

### Lab — Role policy check

```python
"""Privileged-role inventory check for synthetic contracts (read-only)."""
# contract, function, controller, signers needed, timelock hours
ROLES = [
    ("Credit", "mint", "multisig", 3, 48), ("Credit", "pause", "multisig", 2, 0),
    ("Credit", "upgrade", "multisig", 3, 48), ("Market", "setFee", "single", 1, 0),
    ("Market", "upgrade", "multisig", 3, 24), ("Oracle", "setSource", "single", 1, 0),
    ("Vault", "withdrawReserve", "multisig", 3, 72),
]
FUND_OR_CODE = {"mint", "upgrade", "withdrawReserve", "setSource", "setFee"}
MIN_TIMELOCK = 48

def main():
    for c, f, ctl, n, t in ROLES:
        notes = []
        if f in FUND_OR_CODE and n < 2:
            notes.append("single signer")
        if f in FUND_OR_CODE and t < MIN_TIMELOCK:
            notes.append(f"timelock {t}h < {MIN_TIMELOCK}h")
        if notes:
            print(f"{c}.{f}: {'; '.join(notes)}")
    print(f"privileged functions {len(ROLES)}; pause is exempt from timelock by design")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_roles.py`. Verified output:

```text
Market.setFee: single signer; timelock 0h < 48h
Market.upgrade: timelock 24h < 48h
Oracle.setSource: single signer; timelock 0h < 48h
privileged functions 7; pause is exempt from timelock by design
```

### 27.3 Closing gaps

The check reports three issues among seven privileged functions: Market.setFee has a single signer and no timelock; Market.upgrade has a 24-hour timelock, below the 48-hour policy; and Oracle.setSource has a single signer and no timelock. Pause is correctly exempt from the timelock. Jonas notes that setSource is the most serious because a changed data source could affect credit prices. The team moves both single-signer functions to the multi-signature wallet and sets timelocks to 48 hours before deployment, then reruns the check.

### Worked example

The check finds three policy breaches among seven privileged functions, including single-signer control of Oracle.setSource; all are fixed and rechecked.

> **Synthetic case.** Contracts and inventory are synthetic; EEA EthTrust and ConsenSys best practices are real sources.

### Errors and limits

Leaving test-time single-key control on production functions is a common, avoidable gap.

### Exercises

- **EX079 — Pause exemption.** Why is pause exempt from the timelock? *Rubric:* 3 = its purpose is fast protection;; 2 = speed;; 1 = oversight;; 0 = none.
- **EX080 — Breaches found.** How many breaches did the check report? *Rubric:* 3 = three of seven functions;; 2 = three;; 1 = vague;; 0 = none.
- **EX081 — Most serious.** Which finding is most serious? *Rubric:* 3 = Oracle.setSource single signer;; 2 = data source;; 1 = pause;; 0 = none.

### Synthesis

A written role policy checked automatically against configuration closes privileged-control gaps.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Web3, blockchain and cryptoasset security: implementation I

### Learning outcomes

You will (1) implement the minting contract defensively; (2) apply secure patterns; (3) document special code use.

### 28.1 Minimal contract

Jonas implements the minting contract in a test environment with only three functions: mint against a signed batch, read the hourly minted amount, and read configuration. It contains no upgrade mechanism, no external calls except to the credit token, and no low-level assembly. Keeping it minimal follows the design choice and makes review straightforward. Every line is justified in comments, and the contract is compiled with a pinned compiler version recorded in the build file. Jonas asks a classmate to read it for clarity before review.

### 28.2 Secure patterns

Where the contract calls the token to mint, Jonas applies the checks-effects-interactions pattern described in EthTrust and ConsenSys guidance: validate inputs, update the hourly counter, then make the external call. He checks the return value of every call. He avoids using the transaction originator for authorisation and uses the immediate caller instead, as EthTrust requires. Each pattern is linked to the weakness it prevents in the code comments, so reviewers can check that defences are present and understood. Tests confirm each pattern.

### 28.3 Documentation

EthTrust asks that special code use, such as external calls and use of block timestamps, be documented with how misuse is prevented. Jonas writes a short document listing each external call and timestamp use, its purpose and protections. The hourly cap uses block timestamps; he explains that small timestamp variations do not matter at hourly granularity. Documentation supports review and future maintenance, and forms part of the evidence for the verification laboratory. The document is stored with the code and versioned alongside it, so reviewers always see documentation matching the deployed version.

### Worked example

The minimal minting contract has three functions, applies checks-effects-interactions, checks call returns, avoids transaction-originator authorisation and documents timestamp use.

> **Synthetic case.** Code and documents are synthetic; EEA EthTrust and ConsenSys best practices are real sources.

### Errors and limits

Adding unnecessary features to a high-value contract enlarges what reviewers must verify.

### Exercises

- **EX082 — Excluded features.** Name one feature the minting contract omits. *Rubric:* 3 = upgrade mechanism;; 2 = assembly;; 1 = minting;; 0 = none.
- **EX083 — CEI order.** What is the checks-effects-interactions order? *Rubric:* 3 = validate, update state, then call externally;; 2 = CEI;; 1 = call first;; 0 = none.
- **EX084 — Authorisation source.** What is used for authorisation instead of the transaction originator? *Rubric:* 3 = the immediate caller;; 2 = msg.sender;; 1 = tx origin;; 0 = none.

### Synthesis

Minimal, pattern-based and documented implementations make high-value contracts reviewable.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Web3, blockchain and cryptoasset security: measurement

### Learning outcomes

You will (1) define security and operational metrics; (2) collect them reliably; (3) use them to judge controls.

### 29.1 Choosing metrics

Jonas defines metrics that show whether controls work: percentage of privileged functions meeting the role policy; invariant violations detected per month; time from a queued privileged action to monitor confirmation; minting events blocked by the cap; reconciliation mismatches between database and ledger; and validator availability. Each metric has a definition, data source, collection method and target. He avoids counting activity, such as the number of transactions, as a security metric. The board approves the list, and Jonas explains each metric in one plain sentence in the monthly report.

### 29.2 Collecting reliably

Metrics are collected by scripts from ledger events, monitoring logs and configuration exports, run on a schedule with results stored and versioned. Jonas tests each collection script on synthetic data with known answers before using it. He records any change to a metric's definition, because a changed definition can create an apparent trend that is not real. Reliable collection is what makes metrics trustworthy enough to drive decisions by the board. Each script's output includes the data source, run date and definition version, so any figure can be traced back to how it was produced.

### 29.3 Judging controls

After three months of test operation, metrics show 100 percent policy conformance, zero invariant violations, a median monitor confirmation of nine hours and three minting batches blocked by the cap due to a meter clock fault. Jonas uses the last to show the cap working as intended and to prompt a fix to meter clocks. Metrics are valuable when they lead to action; he adds a short action column to each monthly report. The board reviews the report monthly and decides on actions, which Jonas tracks to completion.

### Worked example

Six metrics are defined; three months of test operation show full policy conformance, no invariant violations and three cap blocks caused by a meter clock fault.

> **Synthetic case.** Metrics and results are synthetic.

### Errors and limits

Using transaction counts as a security metric says nothing about whether controls work.

### Exercises

- **EX085 — Metric example.** Name one defined metric. *Rubric:* 3 = policy conformance percentage;; 2 = invariant violations;; 1 = transactions;; 0 = none.
- **EX086 — Definition change.** Why record metric definition changes? *Rubric:* 3 = changes can create false trends;; 2 = false trends;; 1 = cost;; 0 = none.
- **EX087 — Cap blocks cause.** What caused the three cap blocks? *Rubric:* 3 = a meter clock fault;; 2 = clock;; 1 = attack;; 0 = none.

### Synthesis

Defined, reliably collected metrics show whether controls work and prompt improvements.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify system consistency through reconciliation; (2) investigate mismatches; (3) record verification evidence.

### 30.1 Why reconcile

The cooperative keeps member account records in its database and balances on the ledger. They should agree; if they do not, statements to members may be wrong. Reconciliation compares the two systematically. Jonas explains that reconciliation verifies the integration between systems, not the contract alone, and catches problems such as missed events, failed database writes or accounts created in one place but not the other. In financial systems, regular reconciliation is a basic control that auditors expect. Brightwater schedules reconciliation weekly.

### 30.2 The reconciliation script

Jonas writes a standard-library script that reads a synthetic database snapshot and a synthetic ledger snapshot, compares balances per account, and prints mismatches and totals. It reads only the two synthetic files and changes nothing. He tests it on a pair of identical snapshots, which must report zero mismatches, before using it on the verification lab data. He also tests it on a pair that differs in exactly one account, which must report exactly one mismatch. Both tests pass. The script prints mismatches sorted by account so the output can be compared between weeks, and it saves the results with the snapshot dates for the verification record.

### Lab — Database and ledger reconciliation

```python
"""Reconcile an off-chain account database with an on-chain balance snapshot (synthetic, read-only)."""
DB = {"h01": 150, "h02": 20, "h03": 0, "h04": 60, "h05": 100, "h06": 25}
CHAIN = {"h01": 150, "h02": 20, "h04": 60, "h05": 90, "h07": 10}

def main():
    keys = sorted(set(DB) | set(CHAIN))
    diffs = [(k, DB.get(k), CHAIN.get(k)) for k in keys if DB.get(k, 0) != CHAIN.get(k, 0)]
    print(f"accounts compared {len(keys)}, mismatches {len(diffs)}")
    for k, d, c in diffs:
        print(f"  {k}: db={d} chain={c}")
    print(f"totals db={sum(DB.values())} chain={sum(CHAIN.values())}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_reconcile.py`. Verified output:

```text
accounts compared 7, mismatches 3
  h05: db=100 chain=90
  h06: db=25 chain=None
  h07: db=None chain=10
totals db=355 chain=330
```

### 30.3 Investigating mismatches

The run compares seven accounts and finds three mismatches: h05 shows 100 in the database but 90 on the ledger; h06 exists only in the database with 25; and h07 exists only on the ledger with 10. Totals are 355 and 330. Jonas investigates each: h05's difference matches a transfer the database missed during a gateway restart; h06 is a new member whose wallet was not yet created; h07 is a test account left on the network. Each finding becomes a fix and a test.

### Worked example

Reconciliation of seven accounts finds three mismatches, traced to a missed event during a gateway restart, an unfinished onboarding and a leftover test account.

> **Synthetic case.** Snapshots and accounts are synthetic.

### Errors and limits

Assuming database and ledger always agree leaves member statements unchecked.

### Exercises

- **EX088 — Reconciliation purpose.** What does reconciliation verify? *Rubric:* 3 = integration between database and ledger;; 2 = consistency;; 1 = contract code;; 0 = none.
- **EX089 — Mismatch count.** How many mismatches were found? *Rubric:* 3 = three of seven accounts;; 2 = three;; 1 = vague;; 0 = none.
- **EX090 — h05 cause.** What caused h05's difference? *Rubric:* 3 = a transfer missed during gateway restart;; 2 = missed event;; 1 = theft;; 0 = none.

### Synthesis

Regular reconciliation verifies integration between systems and reveals hidden operational faults.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Web3, blockchain and cryptoasset security: implementation II

### Learning outcomes

You will (1) implement the transfer contract and proxy safely; (2) protect initialisation; (3) prepare for review.

### 31.1 Transfer contract

Jonas implements the transfer contract behind a proxy, as selected in the architecture. The contract supports transfer, burn for redemption and read functions, and enforces non-negative balances and positive amounts. He reuses a widely reviewed open-source token implementation at a pinned version rather than writing token logic from scratch, adding only the cooperative's specific rules. Reusing reviewed code reduces the amount of new code to verify, but he still reads the library's documentation and known issues before adopting it, recording the version and reasons in a decision record.

### 31.2 Initialisation and upgrades

Proxied contracts are configured by an initialiser function rather than a constructor. The EthTrust specification warns that many protocols have suffered because initialisers were left unprotected or not called in the same transaction as deployment. Jonas deploys and initialises in one transaction, sets roles to the board multi-signature during initialisation, and disables re-initialisation afterwards. The upgrade function is restricted to the governance role with a 48-hour timelock. He documents the deployment script so that the process can be repeated exactly on the test network and later in production.

### 31.3 Preparing for review

Before external review, Jonas prepares a review pack: the requirements, state and role models, architecture decision, source code at a tagged version, compiler settings, test results, invariant replays, documentation of special code use and known limitations. The EthTrust specification lists compiler options and metadata as part of a conformance claim, so he includes them. A complete pack lets reviewers spend time on finding problems rather than reconstructing context, which improves the value of limited review budgets. Reviewers confirm the pack was complete when they begin.

### Worked example

The transfer contract reuses a pinned, reviewed library; deployment and initialisation occur in one transaction with re-initialisation disabled; a full review pack is prepared.

> **Synthetic case.** Contracts, scripts and packs are synthetic; EEA EthTrust is a real source.

### Errors and limits

Leaving an initialiser callable after deployment can let someone else take control of a proxied contract.

### Exercises

- **EX091 — Library reuse.** Why reuse a reviewed token implementation? *Rubric:* 3 = less new code to verify;; 2 = reviewed;; 1 = cheaper only;; 0 = none.
- **EX092 — Initialiser protection.** How is the initialiser protected? *Rubric:* 3 = called in deployment transaction, then disabled;; 2 = same transaction;; 1 = left open;; 0 = none.
- **EX093 — Pack contents.** Name two items in the review pack. *Rubric:* 3 = models and compiler settings;; 2 = tests, docs;; 1 = nothing;; 0 = none.

### Synthesis

Reused reviewed code, protected initialisation and complete review packs make upgradeable contracts safer.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Web3, blockchain and cryptoasset security: reliability

### Learning outcomes

You will (1) reason about finality and confirmations; (2) plan for node and gateway failures; (3) set reliability targets.

### 32.1 Finality

On a proof-of-work chain, a transaction becomes harder to reverse as blocks are added after it. Nakamoto's paper, section 11, gives the probability that an attacker with a share q of computing power could catch up from z blocks behind. Jonas implements that formula in a standard-library script to understand how confirmations reduce risk. Brightwater's permissioned ledger reaches finality differently, once its validators agree, but the cooperative also accepts payments bridged from a public chain, so the confirmation question applies to those deposits.

### Lab — Confirmations from Nakamoto's formula

```python
"""Confirmations needed using the catch-up probability in Nakamoto (2008), section 11 (read-only)."""
import math

def attacker_success(q, z):
    p = 1 - q; lam = z * q / p; s = 1.0
    for k in range(z + 1):
        poisson = math.exp(-lam) * lam ** k / math.factorial(k)
        s -= poisson * (1 - (q / p) ** (z - k))
    return s

def main():
    for q in (0.1, 0.3):
        for z in (0, 2, 6):
            print(f"q={q} z={z} P={attacker_success(q, z):.7f}")
        z = 0
        while attacker_success(q, z) >= 0.001:
            z += 1
        print(f"q={q}: z for P<0.001 = {z}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_finality.py`. Verified output:

```text
q=0.1 z=0 P=1.0000000
q=0.1 z=2 P=0.0509779
q=0.1 z=6 P=0.0002428
q=0.1: z for P<0.001 = 5
q=0.3 z=0 P=1.0000000
q=0.3 z=2 P=0.4457171
q=0.3 z=6 P=0.1321112
q=0.3: z for P<0.001 = 24
```

### 32.2 Reading the results

The script reproduces the values in Nakamoto's paper: with q equal to 0.1, the probability is 0.0509779 at two confirmations and 0.0002428 at six; five confirmations bring it below 0.001. With q equal to 0.3, six confirmations still leave 0.1321112, and twenty-four are needed to go below 0.001. Jonas concludes that the number of confirmations must depend on assumptions about adversary strength and the value at stake, and recommends a documented waiting rule for bridged deposits based on deposit size.

With q equal to 0.1, for example, six confirmations put the risk near 0.0002, while larger deposits could justify a longer wait under a stronger adversary assumption.

### 32.3 Failure planning

Reliability also means surviving component failures. Jonas lists failures and planned responses: if one validator fails, the other two continue; if two fail, the ledger halts and members are informed while operators restore service; if the gateway fails, readings queue at meters for up to seven days; and if the member app fails, paper statements and phone support continue. He sets targets with the board: ledger availability of 99.5 percent monthly and recovery of the gateway within four hours. Targets make reliability measurable rather than hoped for.

### Worked example

The lab reproduces Nakamoto's values (q=0.1: z=5 for P<0.001; q=0.3: z=24); failure responses and targets of 99.5% availability and four-hour gateway recovery are set.

> **Synthetic case.** Targets and failure plans are synthetic; Nakamoto (2008) is a real source.

### Errors and limits

Using a fixed number of confirmations regardless of value and adversary assumptions misjudges risk.

### Exercises

- **EX094 — Paper values.** What probability does q=0.1 give at six confirmations? *Rubric:* 3 = 0.0002428;; 2 = about 0.0002;; 1 = 0.05;; 0 = none.
- **EX095 — Strong adversary.** How many confirmations for P<0.001 at q=0.3? *Rubric:* 3 = 24;; 2 = twenty-four;; 1 = 6;; 0 = none.
- **EX096 — Gateway queue.** How long can meters queue readings? *Rubric:* 3 = up to seven days;; 2 = seven days;; 1 = one hour;; 0 = none.

### Synthesis

Confirmation rules, planned failure responses and measurable targets make the platform reliable.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Web3, blockchain and cryptoasset security: safety and resilience

### Learning outcomes

You will (1) plan for emergencies; (2) design pause and recovery procedures; (3) rehearse incident response.

### 33.1 Emergency scenarios

Jonas describes emergency scenarios: a suspected flaw in the transfer contract, a compromised gateway key, a validator operator acting outside agreements, and a mass outage at the cooperative's site. For each he writes what members would experience, which controls limit harm and what decisions are needed. Thinking through scenarios before they happen allows calm, prepared responses. The EthTrust specification notes that organisational and off-chain security posture, including incident response procedures and emergency shutdown capabilities, matters as much as code. Each is reviewed by the board.

### 33.2 Pause and recovery

The pause procedure requires two of five board keyholders, an announcement to members within an hour, and continued redemption so members can still use credits for bills. Recovery after a contract flaw follows a documented path: investigate on a test copy, prepare and review a fix, queue the upgrade with the 48-hour timelock, inform members, and unpause after verification. For a compromised gateway key, the minting role is moved to a new multi-signature wallet through governance. Each path names who acts and what evidence is recorded.

### 33.3 Rehearsal

Jonas runs a tabletop exercise with the board, the developer and one partner operator, using the compromised gateway key scenario. The exercise reveals that only two keyholders know how to sign on the multi-signature wallet, so a timely pause could fail if either is away. The board arranges training for all five and a quarterly signing drill on the test network. Rehearsals reveal practical gaps that documents hide, and they build the confidence needed to act under pressure. The drill results are recorded.

### Worked example

Four emergency scenarios are documented; a tabletop exercise reveals only two keyholders can sign, leading to training and quarterly drills.

> **Synthetic case.** Scenarios, exercises and people are synthetic; EEA EthTrust is a real source.

### Errors and limits

Writing emergency procedures without rehearsing them leaves untested assumptions about who can act.

### Exercises

- **EX097 — Redemption during pause.** Why does redemption continue during a pause? *Rubric:* 3 = members can still use credits for bills;; 2 = bills;; 1 = vague;; 0 = none.
- **EX098 — Recovery step.** Name one step in contract-flaw recovery. *Rubric:* 3 = queue upgrade with 48-hour timelock;; 2 = review fix;; 1 = delete contract;; 0 = none.
- **EX099 — Rehearsal gap.** What gap did the tabletop reveal? *Rubric:* 3 = only two keyholders knew how to sign;; 2 = signing skills;; 1 = vague;; 0 = none.

### Synthesis

Prepared scenarios, clear pause and recovery paths, and rehearsals make the system resilient.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Web3, blockchain and cryptoasset security: integration

### Learning outcomes

You will (1) integrate contracts with gateway, app and utility; (2) test end to end; (3) manage integration risk.

### 34.1 Integration points

The contracts must work with the gateway that submits minting batches, the member app that shows balances and initiates transfers, the database that produces statements, and the utility's billing system that receives redemption reports. Jonas lists each integration point with its interface agreement and owner. Integration is where earlier assumptions meet reality: the utility's system, for example, expects redemption reports in a fixed file format at a fixed time each night, which the design had not specified precisely. Each owner confirms their entry.

### 34.2 End-to-end testing

Jonas builds an end-to-end test on the test network: simulated meters produce signed readings, the gateway batches them, the minting contract issues credits, members transfer and redeem through the app, the database updates statements and a redemption file is produced for the utility. Each step is checked against expected outcomes, including invariants and reconciliation. The first run fails because the app shows balances before transactions are final, confusing users; he changes it to show pending and confirmed amounts separately. The test is then rerun.

### 34.3 Managing integration risk

Integration changes can break things far from where they are made. Jonas introduces a rule that any change to an interface requires updating the agreement, running the end-to-end test and notifying the other owner. He also schedules integration tests nightly on the test network. When the utility changes its file format with a week's notice, the agreement process catches it and the change is made before the deadline. Integration risk is managed through communication as much as through code. Records are kept.

### Worked example

Five integration points are documented; the end-to-end test reveals a pending-balance display problem, and an interface change rule catches the utility's format change in time.

> **Synthetic case.** Systems, tests and changes are synthetic.

### Errors and limits

Testing contracts alone without end-to-end tests misses failures at integration points.

### Exercises

- **EX100 — Utility expectation.** What did the utility system expect? *Rubric:* 3 = fixed file format at a fixed nightly time;; 2 = file format;; 1 = API calls;; 0 = none.
- **EX101 — First failure.** What did the first end-to-end run reveal? *Rubric:* 3 = app showed balances before finality;; 2 = pending balances;; 1 = nothing;; 0 = none.
- **EX102 — Interface rule.** What does an interface change require? *Rubric:* 3 = update agreement, rerun end-to-end test, notify owner;; 2 = three steps;; 1 = nothing;; 0 = none.

### Synthesis

Documented integration points, end-to-end tests and interface change rules manage integration risk.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) review the integrated design with peers; (2) address open risks; (3) plan production readiness.

### 35.1 Studio review

In the second design studio, Jonas presents the integrated system: architecture, implemented contracts, integration, metrics and emergency procedures. Peers and a visiting practitioner from a fictional audit firm review it against the requirements and threat analysis. They ask how the design handles a member losing their own wallet key, a risk listed in the threat analysis but not fully addressed. Studio reviews bring fresh eyes to a design that its author has stared at for months. He records every question raised for follow-up.

### 35.2 Addressing open risks

For member key loss, the team designs two paths. Members using cooperative-managed custody recover through identity verification at the office. Members using their own wallets can register a recovery address in advance; if they lose their key, the board can, after a 14-day timelock and identity verification, move their credits to the recovery address. Jonas weighs this against the risk that the recovery power could be misused, and adds requirements that every recovery is announced and logged. The board approves both paths after discussion.

### 35.3 Production readiness

The studio produces a readiness checklist: external review completed and findings resolved; role policy conformance at 100 percent; invariant and reconciliation tests passing; monitoring and alerts live; emergency drills done with all keyholders; member communications prepared; and rollback plans documented. Each item has an owner and evidence. Jonas notes that readiness is a decision by the board based on evidence, not a date on a calendar, and that the checklist makes that decision transparent. Evidence for each item is stored in the readiness folder for the board.

### Worked example

Studio review identifies member key loss as unresolved; two recovery paths with a 14-day timelock are designed; a seven-item readiness checklist is agreed.

> **Synthetic case.** Designs, reviewers and checklists are synthetic.

### Errors and limits

Launching on a fixed date without evidence of readiness puts members' credits at risk.

### Exercises

- **EX103 — Unaddressed risk.** What risk did the studio find unaddressed? *Rubric:* 3 = member wallet key loss;; 2 = key loss;; 1 = vague;; 0 = none.
- **EX104 — Recovery timelock.** How long is the recovery timelock? *Rubric:* 3 = 14 days;; 2 = two weeks;; 1 = 48 hours;; 0 = none.
- **EX105 — Readiness nature.** What is readiness according to Jonas? *Rubric:* 3 = a board decision based on evidence;; 2 = evidence;; 1 = a date;; 0 = none.

### Synthesis

Peer review closes open risks, and an evidence-based checklist supports the production decision.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Web3, blockchain and cryptoasset security: performance and scale

### Learning outcomes

You will (1) estimate load and costs; (2) identify bottlenecks; (3) plan for growth without weakening security.

### 36.1 Estimating load

Jonas estimates load: 400 households produce hourly readings, giving about 9,600 readings per day, batched into 24 minting transactions. Transfers and redemptions add perhaps 300 transactions per day. The permissioned ledger handles this easily. He then models growth to 2,000 households if neighbouring villages join. Load is still modest, but database size and statement generation grow linearly. Estimating load with simple arithmetic prevents both over-engineering and surprises when growth arrives. He records the assumptions behind each estimate and plans to compare them with measured load each quarter, adjusting the model when real data differ.

### 36.2 Bottlenecks

The analysis identifies bottlenecks: statement generation takes 40 minutes nightly at current size and would take over three hours at 2,000 households; the reconciliation script reads entire snapshots; and the gateway processes batches sequentially. Jonas notes that none is a contract problem, but each affects reliability and the timeliness of security checks. Slow reconciliation, for example, means mismatches are found later. He proposes incremental reconciliation and parallel statement generation. He measures each bottleneck on the test network to confirm the estimates, and finds the statement estimate accurate within ten percent, which gives confidence in the growth plan.

### 36.3 Growth without weakening security

Jonas warns against scaling shortcuts that weaken controls, such as raising the minting cap without changing the capacity bound, or batching privileged actions to save effort. Growth plans must keep the same controls: new villages' meters must be signed and registered, new capacity must be reflected in configuration through governance with a timelock, and monitoring thresholds must be recalculated. He adds these to the growth plan so that performance changes are reviewed for security effects. The board approves the plan with these conditions.

### Worked example

Load of about 9,600 readings and 300 transactions per day is modest; statement generation would exceed three hours at 2,000 households, prompting incremental and parallel processing.

> **Synthetic case.** Loads, times and plans are synthetic.

### Errors and limits

Raising caps or bypassing reviews to cope with growth weakens the controls that protect members.

### Exercises

- **EX106 — Daily readings.** How many readings per day at 400 households? *Rubric:* 3 = about 9,600;; 2 = 9600;; 1 = 400;; 0 = none.
- **EX107 — Statement bottleneck.** How long would statements take at 2,000 households? *Rubric:* 3 = over three hours;; 2 = three hours;; 1 = 40 minutes;; 0 = none.
- **EX108 — Growth control.** How must new capacity be reflected? *Rubric:* 3 = in configuration through governance with a timelock;; 2 = governance;; 1 = directly;; 0 = none.

### Synthesis

Simple load estimates and security-aware growth plans let the platform scale safely.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Web3, blockchain and cryptoasset security: operations

### Learning outcomes

You will (1) monitor privileged actions against change records; (2) triage alerts; (3) run routine operational checks.

### 37.1 Watching privileged actions

In operation, the most important events to watch are queued privileged actions, because the timelock gives a window to stop or respond to unwanted changes. Jonas writes a standard-library script that compares queued actions with the approved change calendar and flags any that lack a matching approved change reference. It reads only synthetic queue and calendar data and prints alerts for staff, who then check with the board. Jonas tests the script on a small queue with known matches and mismatches first, and schedules it to run every hour so that the timelock window leaves plenty of time to react.

### Lab — Queued action monitor

```python
"""Flag queued privileged actions that are not on the approved change calendar (synthetic, read-only)."""
APPROVED = {("Credit", "upgrade", "CHG-31"), ("Vault", "withdrawReserve", "CHG-33")}
QUEUED = [("Credit", "upgrade", "CHG-31", 49), ("Market", "upgrade", None, 25),
          ("Vault", "withdrawReserve", "CHG-33", 72), ("Credit", "mint", "CHG-34", 48)]

def main():
    for c, f, chg, hours in QUEUED:
        ok = (c, f, chg) in APPROVED
        print(f"{c}.{f} ref={chg} eta={hours}h -> {'expected' if ok else 'ALERT'}")
    print(f"alerts {sum((c, f, g) not in APPROVED for c, f, g, _ in QUEUED)} of {len(QUEUED)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_monitor.py`. Verified output:

```text
Credit.upgrade ref=CHG-31 eta=49h -> expected
Market.upgrade ref=None eta=25h -> ALERT
Vault.withdrawReserve ref=CHG-33 eta=72h -> expected
Credit.mint ref=CHG-34 eta=48h -> ALERT
alerts 2 of 4
```

### 37.2 Triage

The run checks four queued actions and raises two alerts. Market.upgrade has no change reference at all, and Credit.mint carries CHG-34, which is not on the approved calendar. Jonas's triage procedure contacts the keyholders who approved each action. The Market upgrade turns out to be a test-network action mistakenly queued on production by a developer; it is cancelled within the timelock. CHG-34 was approved by the board the day before but not yet added to the calendar, which is then updated.

### 37.3 Routine checks

Jonas writes an operations runbook with daily, weekly and monthly checks: daily review of alerts and node health; weekly reconciliation and invariant replay; monthly role policy check, metrics report and key holder availability confirmation; and quarterly signing drills. Each check has an owner and records its result. Routine checks keep controls working between incidents, and the records provide evidence that the system is operated as designed. Jonas reviews the records each quarter with the board to confirm checks are happening, and adjusts the runbook when a check proves unhelpful or a new risk appears, recording each change.

### Worked example

The monitor flags two of four queued actions; one mistaken upgrade is cancelled within the timelock and one calendar gap is corrected.

> **Synthetic case.** Actions, calendar and runbooks are synthetic.

### Errors and limits

Ignoring queued privileged actions wastes the window a timelock provides.

### Exercises

- **EX109 — Alert count.** How many alerts did the monitor raise? *Rubric:* 3 = two of four;; 2 = two;; 1 = vague;; 0 = none.
- **EX110 — Market upgrade outcome.** What happened with the Market upgrade? *Rubric:* 3 = mistaken test action, cancelled within timelock;; 2 = cancelled;; 1 = executed;; 0 = none.
- **EX111 — Weekly checks.** What happens weekly? *Rubric:* 3 = reconciliation and invariant replay;; 2 = reconciliation;; 1 = drills;; 0 = none.

### Synthesis

Monitoring queued actions against approvals, careful triage and routine checks keep operations safe.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Web3, blockchain and cryptoasset security: validation

### Learning outcomes

You will (1) validate the system against stakeholder needs; (2) commission an external review; (3) respond to findings.

### 38.1 Verification versus validation

Verification asks whether the system was built right, according to specifications; validation asks whether the right system was built, meeting stakeholders' real needs. Jonas validates by observing members using the app, interviewing the board and checking with the utility that redemption reports work for billing. He finds members confused by pending balances despite the earlier fix, and that some elderly members prefer monthly paper statements. Validation finds needs that specifications missed. He records each validation finding with its source and agrees changes with the board, such as offering monthly paper statements.

### 38.2 External review

The cooperative commissions an external security review of the contracts against the EthTrust Security Levels at level M, using the review pack. Reviewers report no high-severity issues, two medium issues and four informational notes. One medium issue concerns a missing event when the minting cap is changed, which would make monitoring harder; the other concerns rounding in fee calculation that slightly favours the sender. Jonas records each finding with its requirement and planned fix. He also confirms which parts of the system were outside the review's scope.

### 38.3 Responding to findings

Both medium issues are fixed, retested and confirmed by the reviewers. The rounding fix follows EthTrust guidance that rounding must not create value for the initiator. Informational notes are either adopted or recorded with reasons for not adopting. Jonas publishes a summary of the review and responses to members in plain language. Responding transparently to review findings builds trust and demonstrates that the cooperative takes security seriously. Members are invited to ask questions at the next general meeting, and the summary is kept with the review report so future reviewers can see how earlier findings were handled.

### Worked example

Validation reveals confusion about pending balances and demand for paper statements; an EthTrust level M review finds two medium issues, both fixed and confirmed.

> **Synthetic case.** Reviews, findings and members are synthetic; EEA EthTrust is a real source.

### Errors and limits

Treating a passed external review as proof of security ignores its stated limits.

### Exercises

- **EX112 — Validation question.** What does validation ask? *Rubric:* 3 = whether the right system was built;; 2 = needs;; 1 = built right;; 0 = none.
- **EX113 — Review result.** What did the external review find? *Rubric:* 3 = no high, two medium, four informational;; 2 = two medium;; 1 = nothing;; 0 = none.
- **EX114 — Rounding fix basis.** What guidance did the rounding fix follow? *Rubric:* 3 = rounding must not create value for the initiator;; 2 = EthTrust rounding;; 1 = vague;; 0 = none.

### Synthesis

Validation with stakeholders and transparent response to external review confirm the system meets real needs.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Web3, blockchain and cryptoasset security: maintainability

### Learning outcomes

You will (1) plan long-term maintenance; (2) manage upgrades and dependency changes; (3) keep knowledge transferable.

### 39.1 Maintenance plan

Contracts may run for years, but everything around them changes: compilers, libraries, network software and people. Jonas writes a maintenance plan covering scheduled reviews of dependencies, monitoring of security advisories for the compiler and libraries, annual review of role assignments and keyholders, and a budget for re-review when upgrades are needed. The EthTrust specification notes that network upgrades can change how code behaves and that certifications apply only to specified virtual machine versions, so the plan includes checking each ledger software upgrade.

### 39.2 Managing upgrades

Each upgrade of the transfer contract follows a defined path: change request, design note, implementation on a branch, tests including invariants and end-to-end runs, review by a second engineer or external reviewer, queuing with the timelock, member notice and post-upgrade verification. Jonas tests the path once with a trivial change on the test network to find friction, such as unclear responsibility for member notices. A rehearsed upgrade path reduces the temptation to bypass controls when an urgent fix is needed.

### 39.3 Transferable knowledge

With one developer, knowledge loss is a major risk. Jonas ensures that runbooks, decision records, architecture documents and scripts are complete and stored in the repository, and that a second person from a partner organisation can deploy to the test network unaided. He records a short video walkthrough of the system for future staff. Maintainability is a security property: a system nobody understands will eventually be changed unsafely or left unpatched. The partner engineer's notes on unclear steps are used to improve the runbooks.

### Worked example

A maintenance plan covers dependencies, advisories, keyholders and network upgrades; a trial upgrade finds unclear notice responsibility; a partner engineer deploys to test unaided.

> **Synthetic case.** Plans and people are synthetic; EEA EthTrust is a real source.

### Errors and limits

Assuming deployed contracts need no maintenance ignores changing compilers, libraries and networks.

### Exercises

- **EX115 — Network upgrade issue.** Why check ledger software upgrades? *Rubric:* 3 = they can change code behaviour;; 2 = behaviour changes;; 1 = vague;; 0 = none.
- **EX116 — Trial friction.** What did the trial upgrade reveal? *Rubric:* 3 = unclear responsibility for member notices;; 2 = notices;; 1 = nothing;; 0 = none.
- **EX117 — Knowledge test.** How is knowledge transfer tested? *Rubric:* 3 = partner engineer deploys to test unaided;; 2 = second person;; 1 = quiz;; 0 = none.

### Synthesis

Planned maintenance, rehearsed upgrades and transferable knowledge keep the system secure over years.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify the whole system with combined methods; (2) compare evidence across methods; (3) produce a verification report.

### 40.1 Combined methods

In the second verification laboratory, Jonas brings together methods: unit and property tests, invariant replay of three months of test-network logs, role policy checks, reconciliation, end-to-end tests, the external review and monitoring records. The EthTrust specification notes that thorough evaluation uses multiple approaches, each finding different issues. Jonas maps each requirement to the methods that verified it, looking for requirements covered by only one method or none. He builds the mapping as a simple table in the repository, with each cell naming the evidence file, so assessors can follow any requirement to its proof.

### 40.2 Comparing evidence

The mapping shows that minting controls are verified by five methods, transfer correctness by four, and governance by three. Redemption reporting is verified only by end-to-end tests. Jonas adds a reconciliation of redemption reports against burn events, which immediately finds one day where a report was generated twice due to a scheduler retry. Comparing evidence across methods shows where verification is thin and exposes issues that a single method would miss. The duplicate is fixed and a test is added so the scheduler cannot generate a second report for the same day.

### 40.3 Verification report

Jonas writes a verification report: scope, methods, coverage by requirement, findings and their resolution, residual risks and limitations. He states that verification shows the system meets its requirements under tested conditions, not that it is free of defects, echoing the EthTrust statement that no review can guarantee security against all vulnerabilities. Dr Nwosu and the board accept the report as evidence for the production decision. The report lists each residual risk with its owner and planned treatment, and it is stored with the dossier so assessors and future reviewers can see what was and was not verified.

### Worked example

Coverage mapping shows redemption reporting verified by only one method; a new reconciliation finds a duplicated report; a verification report states residual risks.

> **Synthetic case.** Methods, findings and reports are synthetic; EEA EthTrust is a real source.

### Errors and limits

Relying on a single verification method leaves requirements weakly checked.

### Exercises

- **EX118 — Thin coverage.** Which requirement had only one method? *Rubric:* 3 = redemption reporting;; 2 = redemption;; 1 = minting;; 0 = none.
- **EX119 — New finding.** What did the new reconciliation find? *Rubric:* 3 = a report generated twice by a scheduler retry;; 2 = duplicate;; 1 = nothing;; 0 = none.
- **EX120 — Report claim.** What does the report claim? *Rubric:* 3 = requirements met under tested conditions, not defect-free;; 2 = bounded;; 1 = perfect;; 0 = none.

### Synthesis

Combining methods and mapping coverage gives honest, well-supported verification.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Web3, blockchain and cryptoasset security: system optimization

### Learning outcomes

You will (1) optimise cost and performance without weakening controls; (2) evaluate gas and storage choices; (3) measure the effect of changes.

### 41.1 What to optimise

After production readiness, Jonas looks for improvements. Candidates include reducing transaction costs on the ledger, shortening statement generation, and reducing the time from a queued privileged action to monitor confirmation. He ranks candidates by member benefit and risk of introducing defects. He sets a rule that no optimisation may remove or weaken a control listed in the architecture document, and that every optimisation must be measured before and after, so that improvements are real rather than assumed. The board agrees the rule and the ranking.

### 41.2 Gas and storage

Wood's yellow paper assigns gas costs to each operation, with storage writes among the most expensive. Jonas finds that the transfer contract writes a redundant timestamp for each transfer, used only by the app. Removing it saves gas but requires the app to read event logs instead. He evaluates the change with the full test suite and an external reviewer's quick check, because even small contract changes go through the upgrade path. The saving per transfer is modest, but over years it reduces member fees noticeably.

### 41.3 Measuring effects

Jonas measures each optimisation: gas per transfer falls by about eleven percent after removing the redundant write; incremental reconciliation cuts the weekly check from 25 minutes to four; and adding a second on-call contact reduces median monitor confirmation from nine hours to five. He records results in the metrics report. Measurement prevents optimisations being judged by how clever they feel, and shows the board which changes delivered value. Each result is compared with the previous three months to confirm that the improvement is stable rather than a one-off.

### Worked example

Removing a redundant storage write saves about 11% gas per transfer; incremental reconciliation cuts weekly checks from 25 to 4 minutes; median confirmation falls from 9 to 5 hours.

> **Synthetic case.** Measurements and changes are synthetic; Wood's yellow paper is a real source.

### Errors and limits

Optimising contract code by removing checks to save gas trades security for small savings.

### Exercises

- **EX121 — Optimisation rule.** What rule constrains optimisation? *Rubric:* 3 = no control may be removed or weakened;; 2 = keep controls;; 1 = vague;; 0 = none.
- **EX122 — Gas saving.** How much gas per transfer was saved? *Rubric:* 3 = about eleven percent;; 2 = 11%;; 1 = half;; 0 = none.
- **EX123 — Confirmation change.** How did median confirmation change? *Rubric:* 3 = nine hours to five;; 2 = faster;; 1 = slower;; 0 = none.

### Synthesis

Measured optimisations that preserve every control improve cost and responsiveness safely.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Web3, blockchain and cryptoasset security: applied research

### Learning outcomes

You will (1) frame an applied research question from operations; (2) design a small study; (3) report findings carefully.

### 42.1 Question from practice

Operations raise a question: do members who use their own wallets experience more support problems than members using cooperative custody? Jonas frames it as an applied research question with measurable outcomes: support tickets per member per quarter and time to resolve. He notes that members choosing their own wallets may differ in digital skills, a confounder he must consider. Applied research turns operational curiosity into evidence that can guide decisions. He discusses the question with support staff to make sure the outcomes reflect their real workload.

### 42.2 Study design

Jonas uses six months of synthetic support records for 400 members, comparing the two groups and stratifying by age band as a proxy for digital experience. He pre-states his analysis in a short plan approved by Dr Nwosu, and ensures support records are pseudonymised and handled under the cooperative's privacy policy. He also reads Perez and Livshits (2021) as an example of careful interpretation, noting that apparent risk does not always translate into actual harm. The plan is filed before any analysis.

### 42.3 Careful reporting

Self-custody members raised more tickets overall, but within age bands the difference was smaller and mostly concerned key backup. Jonas reports this with counts and intervals, recommends improved backup guidance, and avoids claiming that self-custody is unsafe. The board adopts the guidance and asks for a follow-up after a year. Careful reporting keeps research useful to decisions without overstating what the data show. He shares the report with support staff, who suggest a short printed backup guide, and the follow-up study is planned with the same measures so results can be compared directly.

### Worked example

Self-custody members raise more tickets, but stratifying by age band shrinks the difference, mostly to key backup issues; guidance is improved.

> **Synthetic case.** Members, tickets and results are synthetic; Perez and Livshits (2021) is a real source.

### Errors and limits

Comparing groups without considering who chooses each option can mislead decisions.

### Exercises

- **EX124 — Outcome measures.** What outcomes are measured? *Rubric:* 3 = tickets per member per quarter and resolution time;; 2 = tickets;; 1 = balances;; 0 = none.
- **EX125 — Confounder.** What confounder is considered? *Rubric:* 3 = digital skills, proxied by age band;; 2 = skills;; 1 = weather;; 0 = none.
- **EX126 — Main issue.** What did self-custody tickets mostly concern? *Rubric:* 3 = key backup;; 2 = backup;; 1 = fees;; 0 = none.

### Synthesis

Small, pre-planned applied studies with careful reporting improve operational decisions.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a professional organisation; (2) apply standards in practice; (3) reflect on professional conduct.

### 43.1 Placement

Jonas spends a term with the fictional audit firm Northgate Assurance, which reviews smart contracts for public-sector and cooperative clients. He joins reviews under supervision, using the EthTrust Security Levels and the SWC registry as structured references. He learns how a professional review is scoped, how findings are rated and written, and how client confidentiality is protected. Practice shows him that technical skill is only part of the job; clear communication and careful scoping matter just as much. He keeps a reflective log.

### 43.2 Standards in practice

At Northgate, reviewers record which EthTrust requirements were tested and the result for each, as the specification asks of conformance claims, and include the compiler options and metadata. Jonas notices that clients often misunderstand what a review guarantees, so reports include an explicit statement that certification does not guarantee freedom from all vulnerabilities. He helps write a plain-language summary template for non-technical clients, which the firm adopts. Clients receive both the technical report and the summary, and Jonas collects feedback showing that board members of client organisations found the summary easier to act on.

### 43.3 Professional conduct

Jonas reflects on conduct: never discussing a client's unfixed findings outside the engagement; refusing to rate a finding lower to please a client; and declining to review code where he has a conflict of interest, such as a classmate's project. When a client asks for a review to be completed faster by skipping tests, his supervisor explains how to negotiate scope honestly instead. These experiences give practical meaning to the ethics he studied in chapter ten. He records each lesson.

### Worked example

Jonas joins EthTrust-based reviews at Northgate Assurance, helps create a plain-language summary template, and observes how scope pressure is handled honestly.

> **Synthetic case.** Northgate Assurance, clients and events are synthetic; EEA EthTrust and the SWC registry are real sources.

### Errors and limits

Lowering a finding's rating to please a client undermines the purpose of review.

### Exercises

- **EX127 — Placement firm.** Where does Jonas do his placement? *Rubric:* 3 = Northgate Assurance, an audit firm;; 2 = audit firm;; 1 = bank;; 0 = none.
- **EX128 — Report statement.** What explicit statement do reports include? *Rubric:* 3 = certification does not guarantee freedom from all vulnerabilities;; 2 = limits;; 1 = guarantee;; 0 = none.
- **EX129 — Conflict example.** What conflict of interest is declined? *Rubric:* 3 = reviewing a classmate's project;; 2 = classmate;; 1 = vague;; 0 = none.

### Synthesis

Professional practice combines structured standards, clear communication and principled conduct.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define a capstone project; (2) plan scope and evaluation; (3) begin implementation.

### 44.1 Capstone choice

For his capstone, Jonas chooses to design and verify a community redemption feature: members can donate credits to a hardship fund that pays energy bills for households in difficulty, with the board approving payouts. The feature touches issuance, transfer, governance, privacy and member experience, which lets him demonstrate the whole engineering process. He writes a capstone brief with goals, stakeholders, constraints and success criteria, approved by Dr Nwosu and the board. He also lists the risks of the project and how he will manage them.

### 44.2 Scope and evaluation

The scope includes a fund contract, board approval through the existing multi-signature with a timelock, monthly public totals without naming recipients, and app changes. Evaluation criteria include requirements coverage, invariant tests, role policy conformance, a privacy review and a usability test with five members. Jonas excludes automatic payouts, which would require more complex rules, recording the reason. Clear scope and criteria make the capstone assessable and keep it achievable in the time available. Dr Nwosu confirms the criteria are measurable before work begins.

### 44.3 Beginning implementation

Jonas writes requirements and state models first, then a minimal fund contract on the test network. An early property test finds that donations could be made to the fund after it is paused, contrary to his model. He fixes the rule and adds the test permanently. He also drafts the privacy review, confirming that recipients are recorded only off-chain. Starting with models and tests continues the habits built over the degree and shows them working on a new problem. Progress is logged.

### Worked example

The capstone brief defines a hardship fund with board-approved payouts; an early property test finds donations accepted while paused, which is fixed.

> **Synthetic case.** The fund, members and tests are synthetic.

### Errors and limits

Expanding capstone scope to include complex automatic payouts risks an unfinished, unverified result.

### Exercises

- **EX130 — Capstone feature.** What feature does the capstone build? *Rubric:* 3 = a hardship fund from donated credits;; 2 = fund;; 1 = exchange;; 0 = none.
- **EX131 — Excluded scope.** What is excluded from scope? *Rubric:* 3 = automatic payouts;; 2 = automation;; 1 = donations;; 0 = none.
- **EX132 — Early defect.** What did the early property test find? *Rubric:* 3 = donations accepted while paused;; 2 = paused donations;; 1 = nothing;; 0 = none.

### Synthesis

A clearly scoped capstone with criteria and model-first implementation demonstrates the full engineering process.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) obtain independent review of the capstone design; (2) handle disagreement professionally; (3) record outcomes.

### 45.1 Arranging review

Jonas arranges an independent design review with an engineer from a partner organisation who has not seen the capstone. He sends the brief, requirements, models, threat analysis and code, and asks for a review against the EthTrust level M requirements and the cooperative's role policy. Independence matters because the author's familiarity hides assumptions. He schedules a meeting to discuss findings rather than receiving them only in writing. He also asks the reviewer to say what they found hardest to understand, since unclear parts often hide defects.

### 45.2 Findings and disagreement

The reviewer raises four findings. Jonas accepts three: a missing event for payout approval, an unclear error message and a test gap for maximum fund size. He disagrees with the fourth, a suggestion to allow any board member to approve small payouts alone, because the threat analysis ranked single-person approval as high risk. They discuss it with Dr Nwosu, who agrees with keeping multi-signature approval. Disagreement is handled by reasoning from requirements and evidence, not seniority. The discussion is recorded.

### 45.3 Recording outcomes

Jonas records each finding, his response, the decision and evidence in a review log. Accepted findings are fixed and retested; the rejected suggestion is recorded with its reasoning, so a future reviewer can see that it was considered. The reviewer confirms the fixes. A review log shows assessors that the design survived scrutiny and documents decisions for future maintainers who might otherwise repeat the debate. Jonas also writes a short reflection on what the review taught him about his own blind spots, noting that he had assumed events were obvious and therefore had not tested them, and plans to test events explicitly in future.

### Worked example

An independent reviewer raises four findings; three are accepted and fixed, and one is rejected with documented reasoning tied to the threat analysis.

> **Synthetic case.** Reviewers, findings and decisions are synthetic; EEA EthTrust is a real source.

### Errors and limits

Rejecting review findings without recorded reasoning leaves future maintainers unsure why.

### Exercises

- **EX133 — Review basis.** What does the reviewer review against? *Rubric:* 3 = EthTrust level M and role policy;; 2 = EthTrust;; 1 = taste;; 0 = none.
- **EX134 — Rejected suggestion.** Which suggestion was rejected? *Rubric:* 3 = single board member approving small payouts;; 2 = single approval;; 1 = events;; 0 = none.
- **EX135 — Rejection basis.** On what basis was it rejected? *Rubric:* 3 = threat analysis ranked single approval high risk;; 2 = threat analysis;; 1 = seniority;; 0 = none.

### Synthesis

Independent review, reasoned handling of disagreement and a review log strengthen a design.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) complete implementation and verification; (2) run a usability test; (3) prepare deployment.

### 46.1 Completing verification

Jonas completes the fund contract and app changes, then runs the full verification suite: unit and property tests, invariant replay including fund balances, role policy check, end-to-end tests and reconciliation of fund totals against the database. All pass after one fix to a reconciliation script that had not included the fund's address. He updates the traceability matrix so every capstone requirement links to at least two verification methods. The final run results, with dates and versions, are stored in the dossier, and Dr Nwosu samples two to confirm they match the recorded outputs.

### 46.2 Usability test

Five members, including two over seventy, try donating and checking fund totals using the app on the test network. Three find the donation confirmation unclear because it shows a transaction identifier rather than a plain message. Jonas changes the confirmation to say how many credits were donated and that the fund total will update within an hour. A second test with three members succeeds. Usability affects security too, because confused users make mistakes and lose trust. He records the findings.

### 46.3 Deployment preparation

Deployment follows the established path: board approval, deployment and initialisation in one transaction, role assignment to the multi-signature wallet, timelock configuration, monitoring rules for fund events, member announcement and post-deployment checks. Jonas runs the full path on the test network first. The board approves production deployment, scheduled for a weekday morning with all keyholders available. Preparation reduces the chance that deployment itself introduces errors. After deployment, Jonas runs the post-deployment checks, confirms roles and timelocks match the configuration record, verifies that monitoring sees fund events, and records the results for the board, which formally closes the deployment change.

### Worked example

Verification passes after a reconciliation fix; usability testing improves the donation confirmation; deployment is rehearsed and approved for a staffed weekday morning.

> **Synthetic case.** Members, tests and deployment are synthetic.

### Errors and limits

Deploying when keyholders are unavailable leaves no one able to respond if something goes wrong.

### Exercises

- **EX136 — Reconciliation fix.** What reconciliation fix was needed? *Rubric:* 3 = include the fund's address;; 2 = fund address;; 1 = vague;; 0 = none.
- **EX137 — Usability problem.** What confused test members? *Rubric:* 3 = confirmation showed a transaction identifier;; 2 = unclear confirmation;; 1 = colours;; 0 = none.
- **EX138 — Deployment timing.** When is deployment scheduled? *Rubric:* 3 = weekday morning with all keyholders available;; 2 = staffed weekday;; 1 = weekend night;; 0 = none.

### Synthesis

Complete verification, usability testing and rehearsed deployment finish the capstone safely.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) rehearse failure and recovery on the test network; (2) measure recovery; (3) improve procedures.

### 47.1 Trial design

Before relying on recovery procedures, Jonas runs a failure and recovery trial on a full copy of the system on the test network. Scenarios include the loss of two validators, a corrupted gateway database and a mistaken fund parameter change detected during its timelock. Each scenario has a start signal, expected actions, success criteria and a time target. Participants include the developer, two board keyholders and a partner operator. Trials expose gaps that tabletop exercises cannot. The scenarios are approved by the board.

### 47.2 Running the trial

Restoring two validators takes three hours, within the four-hour target, but reveals that one partner's restore guide is out of date. Restoring the gateway database from backup takes 50 minutes and a replay of queued readings succeeds. The mistaken fund parameter change is detected by the monitor within 40 minutes and cancelled within the timelock by the multi-signature wallet. Jonas records every action and time, and notes where people hesitated. He also notes that the trial took longer to start than planned because participants were not sure who should declare the scenario started.

### 47.3 Improving procedures

After the trial, the partner updates its restore guide, the gateway backup schedule is increased to every four hours, and the cancellation procedure gains a checklist because one keyholder was unsure which transaction to sign. Jonas reruns the cancellation scenario a week later and it completes in 15 minutes. Recording measured recovery times gives the board realistic expectations and evidence for regulators and members. He also adds a named trial lead role to future trials so that start and end are declared clearly, and schedules the next full trial for six months later.

### Worked example

The trial restores two validators in three hours, the gateway database in 50 minutes, and cancels a mistaken change within the timelock; three procedure improvements follow.

> **Synthetic case.** Scenarios, timings and participants are synthetic.

### Errors and limits

Assuming backups and procedures work without trial leaves recovery untested until a real emergency.

### Exercises

- **EX139 — Validator restore time.** How long did restoring two validators take? *Rubric:* 3 = three hours;; 2 = 3 h;; 1 = four days;; 0 = none.
- **EX140 — Detection time.** How quickly was the mistaken change detected? *Rubric:* 3 = within 40 minutes;; 2 = 40 minutes;; 1 = never;; 0 = none.
- **EX141 — Rerun result.** How long did the rerun cancellation take? *Rubric:* 3 = 15 minutes;; 2 = quarter hour;; 1 = hours;; 0 = none.

### Synthesis

Measured recovery trials turn procedures into proven capabilities and guide improvements.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble evidence of engineering work; (2) organise it for assessors; (3) protect sensitive content.

### 48.1 Dossier purpose

The evidence dossier shows assessors what Jonas did and how he knows it worked. It includes requirements, models, threat analysis, architecture decisions, code at tagged versions, test and verification reports, external and independent review logs, metrics, trial results and reflections. Each item is linked to the competence it demonstrates. A dossier differs from a diary: it is organised around claims and the evidence for each, so assessors can check them efficiently. Dr Nwosu reviews the structure early to confirm it matches assessment criteria.

### 48.2 Organising evidence

Jonas organises the dossier by the engineering lifecycle, with an index mapping each assessment criterion to evidence items. For example, the criterion on verification links to the two verification laboratory reports, the coverage matrix and the external review response. He includes short notes explaining context where an item could be misread. Dr Nwosu checks a sample of links and asks for one missing test log, which he adds. He also adds a one-page reading guide explaining how to navigate the dossier, which assessors later say saved them time.

### 48.3 Protecting sensitive content

Some evidence is sensitive: production configuration, keyholder names and the details of findings in deployed contracts. Jonas includes redacted versions and states where full versions are held under the cooperative's control. He confirms with the board that nothing in the dossier would help someone target the live system. Balancing assessability with security is itself evidence of professional judgement. He records which items were redacted and why in a short note, so assessors understand the gaps. The board's security lead reviews the redactions and confirms that the dossier can be shared with university assessors under the confidentiality terms agreed at the start of the project.

### Worked example

The dossier maps every criterion to evidence, a missing test log is added after sampling, and sensitive content is redacted with board approval.

> **Synthetic case.** Dossier contents are synthetic.

### Errors and limits

Including unredacted production configuration in an assessment dossier exposes the live system.

### Exercises

- **EX142 — Dossier organisation.** How is the dossier organised? *Rubric:* 3 = by lifecycle with a criteria index;; 2 = index;; 1 = by date;; 0 = none.
- **EX143 — Sampling result.** What did the supervisor's sampling find? *Rubric:* 3 = a missing test log;; 2 = missing log;; 1 = nothing;; 0 = none.
- **EX144 — Sensitive handling.** How is sensitive content handled? *Rubric:* 3 = redacted, full versions held by the cooperative;; 2 = redaction;; 1 = included;; 0 = none.

### Synthesis

An organised, claim-based and safely redacted dossier demonstrates engineering competence.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write the engineering thesis; (2) argue from evidence; (3) state limitations and future work.

### 49.1 Thesis structure

Jonas's thesis argues that a small community organisation can operate a secure token system if security is engineered across the whole lifecycle and its operations, not only in contract code. Chapters cover the problem, requirements, architecture, implementation, verification, operations and the capstone. Each chapter presents claims with evidence from the dossier. Dr Nwosu advises him to keep the argument visible in every chapter's introduction and conclusion. He drafts the introduction last, after the evidence chapters are complete, so it describes the argument as it actually developed. Dr Nwosu reads each draft chapter and marks claims that lack evidence.

### 49.2 Arguing from evidence

Jonas supports his argument with measured results: full role policy conformance, no invariant violations in production months, reconciliation mismatches traced and fixed, recovery times within targets, and external review findings resolved. He compares his approach with public guidance from EthTrust, ConsenSys and NIST IR 8202, showing where he followed and adapted it. He avoids claiming the system is secure in absolute terms, citing EthTrust's statement that no review guarantees security. Each comparison is tabulated, so readers can see which guidance items were adopted, adapted or not applicable.

### 49.3 Limitations and future work

Limitations include a permissioned ledger with only three validators, a small member base, synthetic test data and one external review. Future work includes extending to neighbouring villages with independent validator operators, formal verification of the minting contract, and a longer study of member custody choices. Stating limitations and future work honestly shows assessors that Jonas understands the boundaries of his results, which is part of engineering maturity. He also explains how each limitation might have affected his results and what evidence would be needed to address it.

### Worked example

The thesis argues lifecycle-wide security engineering, supported by measured results and comparison with public guidance, with four stated limitations and three future directions.

> **Synthetic case.** Results and the thesis are synthetic; EEA EthTrust, ConsenSys best practices and NIST IR 8202 are real sources.

### Errors and limits

Claiming absolute security for a system contradicts the limits stated by review standards.

### Exercises

- **EX145 — Thesis argument.** What does the thesis argue? *Rubric:* 3 = secure token systems need lifecycle-wide engineering;; 2 = lifecycle;; 1 = code alone;; 0 = none.
- **EX146 — Evidence example.** Name one measured result used. *Rubric:* 3 = full role policy conformance;; 2 = recovery within targets;; 1 = vague;; 0 = none.
- **EX147 — Future work.** Name one future direction. *Rubric:* 3 = formal verification of the minting contract;; 2 = independent validators;; 1 = vague;; 0 = none.

### Synthesis

An evidence-based argument with honest limits forms a strong engineering thesis.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend the thesis; (2) answer questions with evidence; (3) plan professional next steps.

### 50.1 Preparing

Jonas prepares a presentation that follows his argument and rehearses with classmates acting as assessors. He prepares answers to likely questions: why a permissioned ledger, how keys are protected, what happens if two keyholders leave, how privacy is preserved, and what the external review did not cover. Each answer cites dossier evidence. Preparation focuses on understanding his own evidence deeply, so that answers are accurate and calm. Dr Nwosu runs a final rehearsal with a colleague unfamiliar with the project, whose questions reveal two terms Jonas had not defined clearly.

### 50.2 The defense

Assessors question the timelock lengths, the decision to keep pause without a timelock, and the representativeness of synthetic test data. Jonas explains each with requirements and trial results, acknowledging that synthetic data cannot capture every real behaviour and describing how production monitoring compensates. One assessor asks what he would do differently; he answers that he would involve members in usability testing earlier. Assessors pass the thesis with commendation for its operational evidence. The assessors' written comments are filed with the thesis.

### 50.3 Next steps

Jonas joins the cooperative part-time as its security engineer while continuing at Northgate Assurance. He hands over the dossier, runbooks and maintenance plan to the board and partner engineers, and schedules the first annual review. Reflecting on five years, he notes that the most important lessons were not about clever code but about clear requirements, layered controls, honest measurement and people who know what to do. The degree ends where professional responsibility begins. Dr Nwosu notes in her final report that the handover was as thorough as the engineering.

### Worked example

Jonas defends timelock and pause decisions with trial evidence, passes with commendation, and hands over the system with an annual review scheduled.

> **Synthetic case.** The defense, assessors and next steps are synthetic.

### Errors and limits

Defending decisions by assertion rather than evidence weakens a thesis defense.

### Exercises

- **EX148 — Assessor question.** Name one assessor question. *Rubric:* 3 = timelock lengths;; 2 = synthetic data;; 1 = hobbies;; 0 = none.
- **EX149 — Different approach.** What would Jonas do differently? *Rubric:* 3 = involve members in usability testing earlier;; 2 = earlier members;; 1 = nothing;; 0 = none.
- **EX150 — Key lessons.** What did Jonas call the most important lessons? *Rubric:* 3 = requirements, layered controls, measurement and people;; 2 = process;; 1 = clever code;; 0 = none.

### Synthesis

Evidence-based defense and responsible handover complete an engineering degree in blockchain security.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Jonas Weber, Dr Amara Nwosu, Avalon Polytechnic University, Brightwater Community Energy Cooperative and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About 400 member households.

**EX002.** As the integral of issuance minus redemptions over time.

**EX003.** The cooperative's installed solar capacity of 1.2 megawatts.

**EX004.** The sender's balance must be at least a.

**EX005.** It reveals tampering to anyone who compares against a trusted head.

**EX006.** Index 2, the edited record.

**EX007.** A small set of known validator nodes on a permissioned ledger.

**EX008.** The integrity of what is recorded, not the truth of what was measured.

**EX009.** Confirmation of which device sent each reading.

**EX010.** What happens to zero-value transfers.

**EX011.** To avoid floating-point rounding errors that create or destroy value.

**EX012.** He forgot to deduct the fee from the sender.

**EX013.** Decision needed, options, trade-offs and recommendation in plain words.

**EX014.** A permissioned ledger with published governance rules.

**EX015.** It answered a new board member's question in two minutes.

**EX016.** As the integral of f times r(t) over time, minus withdrawals.

**EX017.** The number of transfers times one unit.

**EX018.** It must never favour the person initiating the transaction.

**EX019.** About twelve.

**EX020.** Because the pilot sample is small.

**EX021.** Each covers the other's weakness, with the capacity bound as a hard limit.

**EX022.** A stack-based virtual machine.

**EX023.** Storage writes.

**EX024.** By letting each member claim their own credits.

**EX025.** Into modules for ledger state, validation rules and reporting.

**EX026.** Unchecked return values from low-level calls.

**EX027.** A transfer to oneself doubled the balance.

**EX028.** The safety and welfare of the public.

**EX029.** Household readings are kept off the shared ledger.

**EX030.** Work only on test networks and synthetic data, never handle private keys, or disclose privately.

**EX031.** Three, one at the cooperative and two at partners.

**EX032.** A partner node exposed its administrative interface publicly.

**EX033.** So one outage does not halt the ledger.

**EX034.** As its own unprivileged user.

**EX035.** Block timestamps and logs depend on accurate time.

**EX036.** In a hardware security module or encrypted keystore readable only by the node user.

**EX037.** Credit balances and transfers.

**EX038.** By publishing a monthly hash commitment of all readings.

**EX039.** Hashes of small, guessable data could be reversed by trying all values.

**EX040.** Code is hard or impossible to change after deployment.

**EX041.** The exact compiler version and settings used.

**EX042.** Listed, pinned to exact versions, with provenance recorded.

**EX043.** Integrity.

**EX044.** Confidentiality, because shared data is visible to all nodes.

**EX045.** When an external call lets code be entered again before state is updated.

**EX046.** The gateway assumed UTC while meters reported local time.

**EX047.** Data format, units, timing, error handling and owner.

**EX048.** The gateway bound check, the contract's per-hour cap and a monitoring alert.

**EX049.** A feedback loop that measures, compares and responds.

**EX050.** The gateway stops submitting minting requests and alerts staff.

**EX051.** Two board members through a multi-signature decision.

**EX052.** Meters to gateway, internet to app, cooperative to partner validators, or administrators to contracts.

**EX053.** Five: gateway check, contract cap, multisig, timelock and monitoring.

**EX054.** How validator software upgrades are coordinated.

**EX055.** Access to the account is lost, with no password reset.

**EX056.** Three.

**EX057.** From the ledger, not from the party supplying the proof.

**EX058.** Spend them on energy bills or transfer them to neighbours.

**EX059.** The design must be simple enough to maintain.

**EX060.** Issuance, transfer, redemption, governance and privacy.

**EX061.** Only by the minting role, against signed meter batches, never above the hourly cap.

**EX062.** Approval by three of five board keyholders and a 48-hour timelock.

**EX063.** Minting controls and transfer correctness.

**EX064.** No, burning continues so members can still redeem.

**EX065.** The gateway's multi-signature wallet.

**EX066.** Governance could change the minting cap without limit.

**EX067.** The SWC registry and OWASP Smart Contract Top 10.

**EX068.** A compromised gateway key, negative balances, or loss of two board keys.

**EX069.** Five keyholders with a threshold of three and a replacement procedure.

**EX070.** Balances sum to supply, no balance is negative, and supply never exceeds the cap.

**EX071.** A transfer exceeding the balance, correctly rejected.

**EX072.** A mint raised supply to 1,470, above the 1,400 cap.

**EX073.** Assumptions, state and role models, and how it meets top requirements.

**EX074.** It concentrates all roles in one contract, making upgrades riskier.

**EX075.** Two.

**EX076.** So differences in judgement can be found and discussed.

**EX077.** Only for the transfer contract, with multisig and timelock.

**EX078.** The split design 2.6 and the single contract 2.2.

**EX079.** Because its purpose is fast protection.

**EX080.** Three among seven privileged functions.

**EX081.** Oracle.setSource, because a changed data source could affect prices.

**EX082.** An upgrade mechanism, low-level assembly, or unnecessary external calls.

**EX083.** Validate inputs, update state, then make external calls.

**EX084.** The immediate caller.

**EX085.** Policy conformance, invariant violations, confirmation time, cap blocks, reconciliation mismatches or availability.

**EX086.** A changed definition can create an apparent trend that is not real.

**EX087.** A meter clock fault.

**EX088.** The integration between the database and the ledger.

**EX089.** Three among seven accounts.

**EX090.** A transfer the database missed during a gateway restart.

**EX091.** It reduces the amount of new code to verify.

**EX092.** It is called in the same transaction as deployment and re-initialisation is disabled.

**EX093.** Requirements, models, tagged source, compiler settings, tests, invariant replays and documentation.

**EX094.** 0.0002428.

**EX095.** Twenty-four.

**EX096.** Up to seven days.

**EX097.** So members can still use credits to pay bills.

**EX098.** Investigate on a test copy, review a fix, queue it with the timelock, inform members, unpause.

**EX099.** Only two of five keyholders knew how to sign.

**EX100.** Redemption reports in a fixed file format at a fixed time each night.

**EX101.** The app showed balances before transactions were final.

**EX102.** Updating the agreement, running the end-to-end test and notifying the other owner.

**EX103.** A member losing their own wallet key.

**EX104.** Fourteen days.

**EX105.** A decision by the board based on evidence, not a calendar date.

**EX106.** About 9,600.

**EX107.** Over three hours.

**EX108.** In configuration through governance with a timelock.

**EX109.** Two of four queued actions.

**EX110.** It was a mistaken test action and was cancelled within the timelock.

**EX111.** Reconciliation and invariant replay.

**EX112.** Whether the right system was built, meeting stakeholders' needs.

**EX113.** No high-severity issues, two medium and four informational.

**EX114.** EthTrust guidance that rounding must not create value for the initiator.

**EX115.** Network upgrades can change how code behaves.

**EX116.** Unclear responsibility for member notices.

**EX117.** A partner engineer deploys to the test network unaided.

**EX118.** Redemption reporting.

**EX119.** One day's report generated twice due to a scheduler retry.

**EX120.** The system meets requirements under tested conditions, not that it is free of defects.

**EX121.** No optimisation may remove or weaken an architecture control.

**EX122.** About eleven percent.

**EX123.** From nine hours to five.

**EX124.** Support tickets per member per quarter and time to resolve.

**EX125.** Digital skills, using age band as a proxy.

**EX126.** Key backup.

**EX127.** At the fictional audit firm Northgate Assurance.

**EX128.** That certification does not guarantee freedom from all vulnerabilities.

**EX129.** Reviewing a classmate's project.

**EX130.** A community hardship fund from donated credits with board-approved payouts.

**EX131.** Automatic payouts.

**EX132.** Donations could be made while the fund was paused.

**EX133.** EthTrust level M requirements and the cooperative's role policy.

**EX134.** Allowing any single board member to approve small payouts.

**EX135.** The threat analysis ranked single-person approval as high risk.

**EX136.** Including the fund's address in the reconciliation script.

**EX137.** The confirmation showed a transaction identifier instead of a plain message.

**EX138.** A weekday morning with all keyholders available.

**EX139.** Three hours, within the four-hour target.

**EX140.** Within 40 minutes.

**EX141.** Fifteen minutes.

**EX142.** By the engineering lifecycle with an index mapping criteria to evidence.

**EX143.** One missing test log.

**EX144.** Redacted versions included, full versions held under the cooperative's control.

**EX145.** A small organisation can operate a secure token system if security is engineered across the lifecycle and operations.

**EX146.** Role policy conformance, no invariant violations, fixed mismatches, recovery times or resolved findings.

**EX147.** Formal verification, independent validator operators or a custody study.

**EX148.** Timelock lengths, pause without timelock, or representativeness of synthetic data.

**EX149.** Involve members in usability testing earlier.

**EX150.** Clear requirements, layered controls, honest measurement and prepared people.

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
