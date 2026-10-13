# Security Architecture and Engineering: Bachelor's Course

- Language: English (`en`); course 099, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; ten offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: undergraduate students learning to design, assess and operate security architecture for real organisations.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs evaluate logic, search attack paths, compute sample intervals, pseudonymise, measure coverage, count dependencies, check least privilege, tune a detection rule, estimate a difference-in-differences and weigh options, all on synthetic data; nothing touches a real system. Production designs use vetted products and standards; never roll your own cryptography. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one undergraduate on placement at a small retail co-operative: foundations in mathematics, computing, networks, data, probability and privacy; measurement, architecture and cryptography concepts; research methods; the core security architecture and engineering sequence with two laboratories; advanced and interdisciplinary cases; and the capstone, field practice, evidence review and thesis. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lucas Haddon** | Undergraduate student | Invented |
| **Dr Marco Bellini** | Tutor | Invented |
| **Hannah Osei** | IT security lead at the co-operative | Invented |
| **Ashgrove University** | Fictional university | Invented |
| **Fernway Outdoor Co-operative** | Fictional outdoor retailer | Invented |

### Core sources

Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939); Anderson, *Security Engineering* 3e (2020); Shostack, *Threat Modeling* (2014); Sherwood, Clark and Lynas, *Enterprise Security Architecture* (SABSA, 2005); NIST [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5) and [SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1); ISO/IEC 27001:2022 and 27002:2022. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) express security policies as logical statements; (2) test a policy with a truth table; (3) spot contradictions and gaps in written rules.

### 1.1 The case and logic

Lucas Haddon is a first-year student on a four-year bachelor's programme at the fictional Ashgrove University, tutored by Dr Marco Bellini. From the second year he also works part-time at the fictional Fernway Outdoor Co-operative, a member-owned retailer with an online shop, a warehouse and two stores, under its IT security lead Hannah Osei. Every person, organisation and figure here is synthetic. Dr Bellini starts with logic because security policies are logical statements. A rule such as staff may issue refunds if they are store managers or the amount is under twenty pounds and a receipt exists can be written with AND, OR and NOT, and then checked precisely.

### 1.2 Truth tables for policy

Lucas writes the refund rule as a formula with three conditions: M for manager, S for small amount and R for receipt. The English sentence is ambiguous: does the receipt requirement apply to managers too? He writes both readings, M OR (S AND R) and (M OR S) AND R, and builds a truth table for each. The lab below prints both tables and the rows where they disagree. Those rows are real cases, such as a manager refunding without a receipt, where staff following different readings would act differently. Logic exposes ambiguity before it becomes an argument at a till.

### Lab — Two readings of a refund rule

```python
# Truth tables for two readings of a refund policy (M manager, S small amount, R receipt).
from itertools import product
a = lambda M, S, R: M or (S and R)
b = lambda M, S, R: (M or S) and R
diff = 0
print(" M S R | A B")
for M, S, R in product([0, 1], repeat=3):
    x, y = int(a(M, S, R)), int(b(M, S, R)); diff += x != y
    print(f" {M} {S} {R} | {x} {y}{'  <- differ' if x != y else ''}")
print("rows that differ:", diff)
```

Run with `python3 lab_truth.py`. Verified output:

```text
 M S R | A B
 0 0 0 | 0 0
 0 0 1 | 0 0
 0 1 0 | 0 0
 0 1 1 | 1 1
 1 0 0 | 1 0  <- differ
 1 0 1 | 1 1
 1 1 0 | 1 0  <- differ
 1 1 1 | 1 1
rows that differ: 2
```

### 1.3 Gaps and contradictions

Policies also contain gaps, where no rule applies, and contradictions, where two rules give opposite answers. Fernway's draft remote-access policy says contractors must use the VPN and that warehouse scanners never use the VPN; it is silent about contractors maintaining scanners. Lucas lists the combinations systematically and finds that case. Systematic enumeration is a simple mathematical habit, but it catches the situations that informal reading misses. He recommends adding an explicit rule and a default: anything not explicitly permitted is denied, the fail-safe default of Saltzer and Schroeder (1975).

### Worked example

Lucas formalises a refund rule two ways, finds the rows where readings disagree and identifies an uncovered contractor-scanner case in a remote-access policy.

> **Synthetic case.** Ashgrove University, Fernway Outdoor Co-operative, Lucas, Hannah and Dr Bellini are invented; Saltzer and Schroeder (1975) is real.

### Errors and limits

Real policies include context that formulas omit, such as emergencies. Enumeration grows quickly with many conditions.

### Exercises

- **EX001 — Two readings.** Write the two readings of the refund rule in logic. *Rubric:* 3 = M OR (S AND R) and (M OR S) AND R;; 2 = one;; 1 = vague;; 0 = none.
- **EX002 — Disagreeing rows.** According to the lab, in how many rows do the readings disagree, and what do they share? *Rubric:* 3 = 2 rows, both a manager without a receipt;; 2 = count and pattern;; 1 = vague;; 0 = none.
- **EX003 — Policy gap.** What gap did Lucas find in the remote-access policy? *Rubric:* 3 = contractors maintaining warehouse scanners;; 2 = case;; 1 = vague;; 0 = none.

### Synthesis

Writing policies as logic reveals ambiguity, gaps and contradictions before they cause inconsistent decisions.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the hardware, software and service layers of a retail organisation; (2) identify where security responsibilities sit in each layer; (3) build a first asset inventory.

### 2.1 Layers at Fernway

Lucas visits Fernway with Dr Bellini's class. Hannah shows them the layers: hardware such as tills, warehouse scanners, laptops and a small server room; software such as the shop platform, the stock database and email; and services bought from outside, including card payments, cloud hosting and a delivery partner's tracking system. Each layer depends on the one below. A secure shop platform running on an unpatched server inherits the server's weaknesses. Lucas learns that architecture starts by seeing the whole stack, not only the part a project team happens to own.

### 2.2 Responsibility by layer

For bought services, responsibility is shared. The cloud host secures its data centres and hypervisors; Fernway secures its virtual machines, accounts and data. The card payment provider handles card numbers; Fernway must protect its integration keys and the checkout page. Lucas draws a responsibility table with three columns: Fernway, supplier and shared. He finds that nobody at Fernway was listed as responsible for reviewing the delivery partner's access to customer addresses, which had been granted years ago. Unowned responsibilities are among the most common architecture weaknesses in small organisations.

### 2.3 A first inventory

Hannah asks Lucas to start an asset inventory. Each row lists the asset, its owner, its location or provider, the data it holds and its criticality. He finds more than he expected: an old laptop used for label printing still had stored customer data, and a test copy of the shop database sat on a cloud storage bucket. Inventories are the foundation of architecture work, because nobody can protect what they do not know exists. He records the two surprises as findings for Hannah and notes that the inventory must be updated whenever systems change.

### Worked example

Lucas maps Fernway's hardware, software and service layers, draws a responsibility table finding an unowned delivery-partner access review, and starts an inventory that reveals two forgotten data copies.

> **Synthetic case.** Fernway's systems and findings are synthetic.

### Errors and limits

Inventories are never complete on the first pass. Shared-responsibility boundaries differ between providers and contracts.

### Exercises

- **EX004 — Inherited weakness.** Why can a secure shop platform still be vulnerable? *Rubric:* 3 = it inherits weaknesses of an unpatched server below it;; 2 = lower layer;; 1 = it cannot;; 0 = none.
- **EX005 — Unowned item.** Which responsibility had no owner at Fernway? *Rubric:* 3 = reviewing the delivery partner's access to customer addresses;; 2 = named;; 1 = vague;; 0 = none.
- **EX006 — Inventory surprises.** What two surprises did the inventory reveal? *Rubric:* 3 = old label-printing laptop with customer data; test database copy in cloud bucket;; 2 = both;; 1 = one;; 0 = none.

### Synthesis

Seeing all layers, assigning every responsibility and inventorying assets are the first steps of security architecture.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write simple Python programs that process records safely; (2) validate inputs with allow-lists; (3) avoid hard-coding secrets.

### 3.1 Processing records

Lucas's first programs read order records from synthetic CSV files and compute totals. Dr Bellini adds a security lens from the start: every input is untrusted until checked. Lucas writes functions that check each field: order identifiers must match a fixed pattern, quantities must be positive integers below a limit and postcodes must match an allowed format. Records that fail are set aside with a reason. Programming habits formed in the first year last, so the course treats validation as part of correct programming rather than an advanced security topic added later.

### 3.2 Allow-lists over block-lists

Lucas first tries to block dangerous characters in product names. Dr Bellini shows him that block-lists are always incomplete: there are many ways to encode dangerous input. An allow-list, describing what valid input looks like, is safer: product names may contain letters, digits, spaces and a few punctuation marks, up to sixty characters. Anything else is rejected. Lucas rewrites his checks this way and finds the code shorter and clearer. The principle applies at every scale, from a single field to firewall rules, where allowing known-good flows is safer than blocking known-bad ones.

### 3.3 Secrets out of code

Lucas's program needs to call a synthetic stock service with an API key. His first version writes the key in the source file. Dr Bellini explains that source code is copied, shared and often published by mistake, so keys in code leak. Lucas moves the key to an environment variable read at runtime and adds the configuration file to the ignore list of his version control system. He also learns that if a key is ever committed, removing it from the file is not enough; it must be revoked and replaced, because copies of the history may exist.

### Worked example

Lucas writes an order-record checker with allow-list validation and moves an API key from source code to an environment variable.

> **Synthetic case.** Records, services and keys are synthetic.

### Errors and limits

Allow-lists can reject valid unusual inputs, such as names with accents, unless designed carefully. Environment variables are not a full secrets-management solution.

### Exercises

- **EX007 — Block-list weakness.** Why are block-lists weaker than allow-lists? *Rubric:* 3 = dangerous input has many encodings, so block-lists are always incomplete;; 2 = incomplete;; 1 = stronger;; 0 = none.
- **EX008 — Product name rule.** Describe Lucas's allow-list for product names. *Rubric:* 3 = letters, digits, spaces and a few punctuation marks, up to sixty characters;; 2 = rule;; 1 = block-list;; 0 = none.
- **EX009 — Committed key.** What must happen if an API key is committed to version control? *Rubric:* 3 = revoke and replace it, not just delete it from the file;; 2 = revoke;; 1 = delete only;; 0 = none.

### Synthesis

Secure programming starts with validating every input against what is allowed and keeping secrets out of code.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) structure an argument in a security report; (2) cite sources accurately; (3) distinguish evidence from opinion in writing.

### 4.1 Structuring an argument

Dr Bellini asks Lucas to write a two-thousand-word essay on whether small retailers should adopt zero trust architecture. He first lists claims and their support, then orders them into an argument: what zero trust means according to NIST SP 800-207, what problems it addresses, what it costs a small organisation and what a proportionate adoption might look like. Each paragraph makes one point and links to the next. He learns that a clear argument structure matters more than vocabulary, because readers must follow reasoning to judge whether the conclusion is justified.

### 4.2 Citing accurately

Lucas initially cites a blog post summarising SP 800-207. Dr Bellini asks him to read the publication itself and cite it directly, because summaries often distort. He learns to quote sparingly and accurately, give the full reference with its identifier and avoid citing sources he has not read. He also learns to verify that a reference exists: a fabricated or mistyped identifier undermines the whole essay. In security writing, accurate citation is especially important because readers may make decisions affecting real systems on the basis of the claims.

### 4.3 Evidence versus opinion

Lucas's draft says that zero trust makes networks secure. Dr Bellini marks it as an opinion presented as fact. Lucas revises: SP 800-207 describes zero trust as a set of principles aimed at reducing implicit trust; whether adoption reduces incidents in small retailers is not established by the sources reviewed. He separates what sources state, what evidence shows and what he argues. This separation becomes a habit for the rest of the course and for professional reports, where mixing opinion with evidence can mislead decision makers.

### Worked example

Lucas structures an essay on zero trust for small retailers, replaces a blog citation with SP 800-207 itself and rewrites an overclaim as a sourced, qualified statement.

> **Synthetic case.** The essay and feedback are synthetic; SP 800-207 is real.

### Errors and limits

Primary sources can be long and technical; summaries help orientation but must not replace them. Careful qualification can be overdone until no claim remains.

### Exercises

- **EX010 — One point per paragraph.** What structure does Lucas use for paragraphs? *Rubric:* 3 = each makes one point and links to the next;; 2 = one point;; 1 = random;; 0 = none.
- **EX011 — Primary source.** Why must Lucas cite SP 800-207 directly rather than a blog? *Rubric:* 3 = summaries can distort; cite what you have read;; 2 = distortion;; 1 = blog fine;; 0 = none.
- **EX012 — Overclaim rewrite.** How did Lucas rewrite zero trust makes networks secure? *Rubric:* 3 = principles reducing implicit trust; effect on small retailers not established;; 2 = qualified;; 1 = unchanged;; 0 = none.

### Synthesis

Academic writing in security requires structured arguments, accurate primary citations and clear separation of evidence from opinion.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core security concepts in plain language; (2) recognise common attack patterns against retailers; (3) relate controls to the attacks they address.

### 5.1 Core concepts

Lucas learns the language of security: confidentiality, integrity and availability; assets, threats, vulnerabilities and risk; authentication and authorisation. He practises explaining each to a Fernway store manager without jargon. Confidentiality means only the right people see customer details; integrity means prices and orders cannot be changed without permission; availability means the shop stays open online. Being able to explain concepts plainly is part of security literacy, because architects must persuade non-specialists to fund and follow controls. If the manager cannot repeat the idea in her own words, the explanation has not yet worked.

### 5.2 Attacks on retailers

Hannah describes attacks Fernway faces. Phishing emails impersonating suppliers ask staff to change bank details. Credential stuffing uses passwords leaked from other sites to log in to member accounts. Skimming scripts injected into checkout pages steal card details as customers type. Gift-card fraud exploits weak checks on balance enquiries. Lucas notes that most do not break cryptography or exploit exotic flaws; they abuse ordinary processes and weak authentication. Architecture must therefore cover business processes and people, not only servers and networks.

### 5.3 Controls for attacks

Lucas matches controls to attacks. Supplier bank-detail changes require a phone call to a known number and two approvals. Credential stuffing is reduced by rate limiting, checking passwords against known breached lists and offering multi-factor authentication. Checkout skimming is reduced by limiting third-party scripts, using content security policy and monitoring page changes. Gift-card fraud is reduced by rate limits and requiring the card number plus a PIN. Each control addresses a specific attack path, and he can explain why it exists, which helps staff accept it.

### Worked example

Lucas explains five core concepts to a store manager, lists four retail attacks and matches each to controls.

> **Synthetic case.** Attacks and controls at Fernway are synthetic.

### Errors and limits

Attack patterns change; lists need regular updating. Controls can shift attacks elsewhere rather than stopping them.

### Exercises

- **EX013 — Integrity in retail.** Give a retail example of integrity. *Rubric:* 3 = prices and orders cannot be changed without permission;; 2 = example;; 1 = confidentiality;; 0 = none.
- **EX014 — Credential stuffing.** What is credential stuffing and one control against it? *Rubric:* 3 = logging in with passwords leaked elsewhere; rate limiting, breached-password checks or MFA;; 2 = both;; 1 = vague;; 0 = none.
- **EX015 — Bank-detail control.** How should supplier bank-detail changes be verified? *Rubric:* 3 = phone call to a known number plus two approvals;; 2 = both;; 1 = email reply;; 0 = none.

### Synthesis

Security literacy means explaining concepts plainly and connecting real attacks to specific controls.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) model systems and access as graphs; (2) find attack paths with graph search; (3) use graph measures to prioritise controls.

### 6.1 Graphs of access

Dr Bellini shows how graphs model security. Nodes can be users, machines and data stores; edges can be logins, network connections or permissions. An attacker who controls one node can follow edges to others. Lucas builds a small synthetic graph of Fernway: a phished staff laptop, a shared file server, the warehouse management system, an admin workstation and the shop database. Edges represent permissions and network reachability. Drawing the graph makes paths visible that are hard to see in lists of rules spread across different systems and teams.

### 6.2 Shortest attack paths

Using breadth-first search, Lucas finds the shortest path from the phished laptop to the shop database. The lab below shows a three-hop path: laptop to file server, file server to admin workstation through a saved administrator credential, admin workstation to database. Shortest paths matter because attackers prefer easy routes. Removing the saved credential cuts this path; the search then finds a longer path through the warehouse system. Each change can be checked by rerunning the search, giving a precise way to evaluate whether a control actually blocks the route it targets.

### Lab — Attack paths by breadth-first search

```python
# BFS attack paths on a synthetic Fernway graph.
from collections import deque
def bfs(E, s, t):
    prev, q = {s: None}, deque([s])
    while q:
        u = q.popleft()
        if u == t:
            p = [];
            while u: p.append(u); u = prev[u]
            return p[::-1]
        for v in E.get(u, []):
            if v not in prev: prev[v] = u; q.append(v)
E = {"staff-laptop": ["file-server", "warehouse-wms"], "file-server": ["admin-ws"],
     "warehouse-wms": ["integration-svc"], "integration-svc": ["stock-api"], "stock-api": ["shop-db"], "admin-ws": ["shop-db"]}
p = bfs(E, "staff-laptop", "shop-db"); print(f"{len(p)-1} hops:", " -> ".join(p))
E["file-server"] = []          # saved admin credential removed
p = bfs(E, "staff-laptop", "shop-db"); print(f"{len(p)-1} hops:", " -> ".join(p))
```

Run with `python3 lab_paths.py`. Verified output:

```text
3 hops: staff-laptop -> file-server -> admin-ws -> shop-db
4 hops: staff-laptop -> warehouse-wms -> integration-svc -> stock-api -> shop-db
```

### 6.3 Prioritising with graphs

Some nodes appear on many paths; securing them gives more benefit. Lucas counts how many shortest paths from staff laptops to sensitive data pass through each node. The admin workstation and the file server stand out. He recommends hardening the admin workstation and removing stored credentials from the file server first. Graph reasoning gives an objective basis for priorities, but Lucas notes that the graph is only as good as its edges: unknown connections, such as forgotten remote-access tools, would change the answer, which is why inventories matter.

### Worked example

Lucas models Fernway as a graph, finds a three-hop path to the shop database, shows removal of a saved credential lengthens the path and prioritises two choke-point nodes.

> **Synthetic case.** The graph and credentials are synthetic.

### Errors and limits

Graphs omit edges nobody knows about. Path length is a rough proxy for attacker effort.

### Exercises

- **EX016 — Edge meaning.** What can edges represent in a security graph? *Rubric:* 3 = logins, network connections or permissions;; 2 = two;; 1 = vague;; 0 = none.
- **EX017 — Lab path change.** What happened to the shortest path after removing the saved credential? *Rubric:* 3 = grew from 3 hops to 4 hops via the warehouse system;; 2 = longer;; 1 = unchanged;; 0 = none.
- **EX018 — Choke points.** Which nodes did Lucas prioritise and why? *Rubric:* 3 = admin workstation and file server, which lie on many shortest paths;; 2 = both;; 1 = random;; 0 = none.

### Synthesis

Graph models turn scattered permissions into visible attack paths and objective priorities.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) describe how Fernway's shop, stores and warehouse connect; (2) explain DNS, HTTP and TLS roles in an online shop; (3) identify network design weaknesses in a small organisation.

### 7.1 How Fernway connects

Lucas maps Fernway's network. Customers reach the shop over the internet; the shop runs on a cloud host. Stores connect to head office through broadband links with a site-to-site VPN. The warehouse has its own wireless network for scanners. Staff use cloud email and a file service. He labels each connection with its protocol and encryption, and notes which traffic crosses the public internet. The map shows that the warehouse wireless network and the office network are bridged, so a scanner and a finance laptop sit on the same segment.

### 7.2 DNS, HTTP and TLS in a shop

When a customer visits the shop, DNS translates the name into an address, the browser opens a TLS connection specified in RFC 8446 and then sends HTTP requests. Lucas learns that compromise of Fernway's DNS account would let an attacker redirect customers to a fake shop, which could obtain its own certificate for a look-alike name but not for Fernway's name unless it also controlled the DNS used for certificate validation. He therefore recommends strong authentication on the domain registrar account, an asset often forgotten in architecture reviews because it sits outside the technical estate.

### 7.3 Small-organisation weaknesses

Lucas lists network weaknesses typical of small organisations, all present at Fernway: the bridged warehouse and office networks, a shared Wi-Fi password unchanged for years, remote desktop exposed to the internet for a supplier and no record of firewall rule owners. He proposes simple fixes: separate networks for scanners, guests and staff; replace exposed remote desktop with a managed remote-access service using multi-factor authentication; and annotate firewall rules with owners and review dates. Each fix is cheap compared with the impact of the weakness it removes.

### Worked example

Lucas maps Fernway's connections, recommends registrar account protection and proposes three network fixes including separating the bridged warehouse and office segments.

> **Synthetic case.** Fernway's network is synthetic; RFC 8446 is real.

### Errors and limits

Separating networks can break undocumented dependencies; test first. Cloud services may bypass the office network entirely.

### Exercises

- **EX019 — Bridged networks.** What risk does the bridged warehouse and office network create? *Rubric:* 3 = a compromised scanner can reach finance laptops directly;; 2 = reach;; 1 = vague;; 0 = none.
- **EX020 — Registrar account.** Why protect the domain registrar account strongly? *Rubric:* 3 = its compromise lets an attacker redirect customers and possibly obtain certificates;; 2 = redirect;; 1 = not important;; 0 = none.
- **EX021 — Remote desktop fix.** What should replace internet-exposed remote desktop for the supplier? *Rubric:* 3 = a managed remote-access service with multi-factor authentication;; 2 = managed MFA;; 1 = leave it;; 0 = none.

### Synthesis

Network architecture for a small organisation starts with an honest map and simple separations that remove large risks cheaply.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) build a small web service with authentication and authorisation; (2) write tests for access-control rules; (3) log security-relevant events usefully.

### 8.1 A small service

In Programming II Lucas builds a synthetic stock-query service for store staff using Python's standard library HTTP server for learning purposes. Staff log in, then query stock levels; managers can also adjust stock. He separates authentication, which establishes who the user is, from authorisation, which decides what that user may do. Each request checks both. He learns that mixing them causes bugs, such as checking only that a user is logged in and forgetting to check whether that user is a manager before allowing an adjustment.

### 8.2 Testing access rules

Lucas writes tests for every combination of role and action: staff can query, staff cannot adjust, managers can do both, anonymous users can do neither. He also tests edge cases, such as a manager from one store adjusting another store's stock, which the rules forbid. A test fails: the service checks the manager role but not the store. He fixes the check and the test passes. Testing access rules as a matrix makes missing checks visible, and these tests later protect the rule when someone modifies the code.

### 8.3 Logging usefully

The service logs logins, failed logins, stock adjustments and authorisation failures with user, time, action and outcome, but never passwords or session tokens. Lucas learns that logs serve investigations, so each entry must answer who did what, when and with what result. He also learns to avoid logging excessive personal data. Hannah reviews his log design and asks for a correlation identifier for each request, so that events across services can be linked during an incident. Useful logging is designed with its future readers in mind.

### Worked example

Lucas builds a stock service separating authentication from authorisation, finds a missing store check through a role-action test matrix and designs logs with correlation identifiers.

> **Synthetic case.** The service, roles and stores are synthetic.

### Errors and limits

Standard-library servers are for learning; production uses maintained frameworks. Test matrices grow quickly with roles and resources.

### Exercises

- **EX022 — AuthN versus AuthZ.** What is the difference between authentication and authorisation? *Rubric:* 3 = authentication establishes identity; authorisation decides permitted actions;; 2 = both;; 1 = same;; 0 = none.
- **EX023 — Failed test.** Which test failed and why? *Rubric:* 3 = manager adjusting another store's stock; store not checked;; 2 = named;; 1 = vague;; 0 = none.
- **EX024 — Never logged.** What must never appear in logs? *Rubric:* 3 = passwords or session tokens;; 2 = both;; 1 = usernames;; 0 = none.

### Synthesis

Secure services separate identity from permission, test every rule combination and log what investigators will need.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) design database access for least privilege; (2) prevent injection through parameterised queries; (3) protect backups and test copies.

### 9.1 Least-privilege database access

Fernway's shop database holds members, orders and stock. Lucas reviews how applications connect. The shop uses one database account with full rights to everything, including dropping tables. He proposes separate accounts: the shop can read products and write orders; reporting can read aggregated views; only an administrator account, used rarely and logged, can change the schema. Each account receives only the rights its function needs. If the shop is compromised, the attacker inherits only the shop's rights, not the power to delete or export every table.

### 9.2 Injection and parameters

Lucas reviews the shop's search code and finds a query built by joining strings with customer input. He demonstrates, on a synthetic database using Python's sqlite3, how a crafted search term returns every member record. The fix is to pass input as parameters, which the database treats strictly as data. He also checks other queries and finds two more built the same way. Parameterised queries are a simple, well-established control, yet injection remains common because developers under time pressure copy old patterns. Code review checklists should include it explicitly.

### 9.3 Backups and test copies

The inventory in chapter 2 found a test copy of the database in cloud storage. Lucas investigates: it contained real member data and was readable by anyone with the link. He recommends that test environments use synthetic or masked data, that backups be encrypted with keys held separately and that storage permissions be reviewed automatically. ISO/IEC 27002:2022 includes controls on test information and data masking. Copies of data multiply risk, and architecture must treat every copy with the same care as the original or avoid creating it.

### Worked example

Lucas splits one all-powerful database account into three least-privilege accounts, finds three injectable queries and recommends synthetic test data and encrypted backups.

> **Synthetic case.** Database contents and queries are synthetic; ISO/IEC 27002:2022 is real.

### Errors and limits

Splitting accounts needs application changes and testing. Masked data can still be re-identifiable if done poorly.

### Exercises

- **EX025 — Compromise impact.** How do separate database accounts limit a shop compromise? *Rubric:* 3 = attacker gains only the shop account's limited rights;; 2 = limited;; 1 = vague;; 0 = none.
- **EX026 — Injection count.** How many injectable queries did Lucas find in total? *Rubric:* 3 = three: the search query and two others built the same way;; 2 = three, without saying which;; 1 = one;; 0 = none.
- **EX027 — Test data rule.** What data should test environments use? *Rubric:* 3 = synthetic or masked data;; 2 = synthetic;; 1 = real;; 0 = none.

### Synthesis

Database architecture limits each account's power, keeps input as data and controls every copy of the data.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) explain why authorisation is required before security testing; (2) handle personal data encountered during work ethically; (3) apply professional codes to dilemmas.

### 10.1 Authorisation first

Lucas wants to test whether Fernway's member login is vulnerable to credential stuffing. Hannah explains that even with good intentions, testing without written authorisation could break laws on computer misuse and could disrupt customers. Authorisation states what may be tested, how, when and by whom, and names a contact for emergencies. It must come from someone with authority over the system. For the shop, that includes the cloud host's rules, which restrict certain tests. Lucas writes a test request, Hannah approves a limited version in a staging environment and the test proceeds safely.

### 10.2 Personal data in practice

While reviewing logs, Lucas sees member names, addresses and order histories. He learns to access only what the task requires, never to browse out of curiosity and never to copy personal data into personal notes or coursework. When he needs examples for his university assignment, he creates synthetic records instead. Privacy law in many countries requires such care, but the ethical point is simpler: members trusted Fernway with their data for shopping, not for a student's convenience. Respecting that trust is part of professional practice.

### 10.3 Dilemmas and codes

Lucas faces a dilemma: a friend at another retailer mentions that their checkout page loads scripts from an unknown domain. Should he investigate? Professional codes, such as those of computing societies, emphasise honesty, avoiding harm and respecting authorisation. He does not probe the other site. Instead, he suggests his friend report it internally to their security team. He discusses the case with Dr Bellini, who praises the restraint: helping is right, but acting on systems one is not authorised to test causes harm, even when motivated by concern.

### Worked example

Lucas obtains limited written authorisation for a staging test, uses synthetic data for coursework and declines to probe another retailer's site.

> **Synthetic case.** The test request, logs and friend's case are synthetic.

### Errors and limits

Laws differ by jurisdiction; seek advice when unsure. Staging environments may not reproduce production behaviour.

### Exercises

- **EX028 — Authorisation contents.** What should a test authorisation specify? *Rubric:* 3 = what, how, when, by whom and an emergency contact;; 2 = four;; 1 = vague;; 0 = none.
- **EX029 — Coursework data.** What does Lucas use for coursework examples? *Rubric:* 3 = synthetic records, not member data;; 2 = synthetic;; 1 = real;; 0 = none.
- **EX030 — Friend's report.** What did Lucas advise his friend to do about the suspicious script? *Rubric:* 3 = report it internally to their own security team;; 2 = report;; 1 = probe it;; 0 = none.

### Synthesis

Authorised practice and respect for personal data are prerequisites for any security work, however well meant.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) compare account and permission models on Windows and Linux; (2) harden laptops and servers with baselines; (3) manage updates in a small organisation.

### 11.1 Accounts and permissions

Lucas studies how Windows and Linux control access. Both have users and groups; both distinguish administrators from ordinary users. At Fernway, every store laptop user is a local administrator, a convenience that lets any malware run with full rights. Hannah agrees to remove local administrator rights and provide a request process for software installation. Lucas also reviews a Linux server where several staff share the root password. He recommends individual accounts with elevated rights through logged commands, so actions can be attributed to people.

### 11.2 Baselines

A baseline is a documented set of secure settings. For laptops, Lucas proposes full-disk encryption, automatic screen lock, a host firewall, removal of unused software and standard user accounts. For servers, he proposes disabling unused services, key-based administrator login with multi-factor authentication and centralised logging. He maps the baseline to SP 800-53 Rev. 5 control families such as configuration management and access control, so Fernway can show auditors what it does. Applying a baseline consistently removes many easy footholds attackers rely on.

### 11.3 Updates

Unpatched software is a frequent entry point. Fernway's laptops update automatically, but tills run an old operating system version that the vendor still supports only with paid updates, and the warehouse scanners have never been updated. Lucas proposes an update policy: automatic updates where possible, a monthly window for servers, vendor contracts covering tills and a replacement plan for scanners. Each exception is recorded with an owner and a review date. He notes that the hardest updates are those for devices nobody thinks of as computers.

### Worked example

Lucas removes local administrator rights, replaces a shared root password with individual accounts, proposes laptop and server baselines and writes an update policy with exceptions.

> **Synthetic case.** Devices, versions and policies are synthetic; SP 800-53 Rev. 5 is real.

### Errors and limits

Removing admin rights increases support requests at first. Some vendor devices cannot be updated without breaking warranties.

### Exercises

- **EX031 — Local admin risk.** Why is local administrator for every user risky? *Rubric:* 3 = malware runs with full rights;; 2 = full rights;; 1 = vague;; 0 = none.
- **EX032 — Shared root fix.** What replaces the shared root password? *Rubric:* 3 = individual accounts with logged elevation;; 2 = individual;; 1 = new shared password;; 0 = none.
- **EX033 — Hardest updates.** Which updates does Lucas call hardest? *Rubric:* 3 = those for devices nobody thinks of as computers, like scanners and tills;; 2 = devices;; 1 = laptops;; 0 = none.

### Synthesis

Operating-system security rests on individual accounts, consistent baselines and an update policy that includes forgotten devices.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) estimate a proportion from an audit sample; (2) compute and interpret a confidence interval; (3) avoid common statistical errors in security reports.

### 12.1 Sampling for audit

Fernway has about four thousand user and service accounts across systems. Hannah cannot review every account, so Lucas draws a random sample of two hundred and checks each for problems such as missing owners or stale access. He finds twenty-six with problems. The sample proportion is thirteen per cent. Random sampling matters: if he had checked only accounts he already suspected, the estimate would be biased upward. He records how the sample was drawn, with the random seed, so the audit can be repeated and checked by someone else.

### 12.2 Confidence intervals

A single proportion hides uncertainty. Lucas computes a ninety-five per cent confidence interval using the Wilson method, which behaves well for proportions. The lab below shows the estimate and interval, and the implied range of affected accounts across the population. He reports that between roughly nine and eighteen per cent of accounts likely have problems, about 360 to 740 accounts. That range is more honest and more useful than thirteen per cent alone, because it tells Hannah how much clean-up effort to plan for.

### Lab — Audit sample and confidence interval

```python
# Wilson 95% interval for an account-audit sample (synthetic).
import math
N, n, x, z = 4000, 200, 26, 1.96
p = x / n
den = 1 + z*z/n; centre = (p + z*z/(2*n)) / den
half = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den
lo, hi = centre - half, centre + half
print(f"sample {x}/{n} = {p:.1%}; Wilson 95% CI {lo:.1%} to {hi:.1%}")
print(f"implied affected accounts: {lo*N:.0f} to {hi*N:.0f} of {N}")
```

Run with `python3 lab_sample.py`. Verified output:

```text
sample 26/200 = 13.0%; Wilson 95% CI 9.0% to 18.4%
implied affected accounts: 361 to 735 of 4000
```

### 12.3 Common errors

Lucas lists errors he has seen in security reports: percentages without counts, comparisons of small numbers presented as dramatic changes, averages of skewed data and confusing correlation with cause. A report claiming phishing clicks fell by half after training, based on four clicks falling to two, says little. He resolves to always report counts with proportions, intervals where sampling is involved and the method used. Statistics do not make a report more scientific unless used carefully; misused, they lend false authority to weak claims.

### Worked example

Lucas samples 200 of 4,000 accounts, finds 26 with problems, computes a Wilson interval and reports a range of affected accounts.

> **Synthetic case.** Accounts and findings are synthetic.

### Errors and limits

Intervals assume random sampling; convenience samples invalidate them. Problems found depend on reviewer consistency.

### Exercises

- **EX034 — Why random.** Why must the audit sample be random? *Rubric:* 3 = targeted samples bias the estimate;; 2 = bias;; 1 = faster;; 0 = none.
- **EX035 — Lab interval.** What interval did the lab report? *Rubric:* 3 = about 9.0 to 18.4 per cent, roughly 361 to 735 accounts;; 2 = interval;; 1 = vague;; 0 = none.
- **EX036 — Four to two.** Why is phishing clicks fell by half, four to two, weak evidence? *Rubric:* 3 = tiny counts make the change meaningless by chance;; 2 = small numbers;; 1 = strong;; 0 = none.

### Synthesis

Sampling with stated methods and intervals turns partial audits into honest estimates.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) design identity life-cycle processes for joiners, movers and leavers; (2) apply role-based access with separation of duties; (3) strengthen authentication with phishing-resistant methods.

### 13.1 Joiners, movers, leavers

Most access problems found in chapter 12 came from the identity life cycle. New staff were given access by copying a colleague's account, moving staff kept old rights and leavers' accounts stayed active for weeks. Lucas designs processes: joiners receive access from role definitions approved by managers; movers lose old roles when gaining new ones; leavers are disabled on their last day, triggered by the HR system. Each step is logged. Life-cycle processes prevent access from growing silently, a pattern called privilege creep that undermines least privilege over time.

### 13.2 Roles and duties

Lucas defines roles for Fernway: store staff, store manager, warehouse operator, buyer, finance clerk and administrator. Each role has a documented set of permissions. He checks for toxic combinations: a buyer who can also approve supplier payments could create a fake supplier and pay it. He marks such pairs as conflicts that cannot be held together, implementing separation of duties. Roles simplify access reviews, because managers review role assignments rather than hundreds of individual permissions. But roles need maintenance, or exceptions accumulate until roles mean little.

### 13.3 Stronger authentication

Fernway staff use passwords plus text-message codes. Lucas explains that text codes can be phished through fake login pages that relay codes in real time. Phishing-resistant methods, such as passkeys or hardware security keys using public-key cryptography bound to the real website, prevent this because the credential will not work on a fake domain. He proposes passkeys for administrators and finance staff first, then others. He also recommends that the member shop offer passkeys as an option. Authentication strength should follow the value of what an account can do.

### Worked example

Lucas designs joiner-mover-leaver processes, defines six roles with one toxic combination blocked and proposes phishing-resistant authentication for privileged staff first.

> **Synthetic case.** Roles and processes are synthetic.

### Errors and limits

Role models drift without regular review. Passkey recovery processes can become a weak point.

### Exercises

- **EX037 — Privilege creep.** What is privilege creep and which process prevents it? *Rubric:* 3 = access accumulating over moves; mover process removes old roles;; 2 = both;; 1 = vague;; 0 = none.
- **EX038 — Toxic combination.** What toxic combination did Lucas block? *Rubric:* 3 = buyer who can also approve supplier payments;; 2 = named;; 1 = vague;; 0 = none.
- **EX039 — Text-code weakness.** Why are text-message codes weaker than passkeys? *Rubric:* 3 = they can be phished and relayed in real time; passkeys bind to the real site;; 2 = relay;; 1 = stronger;; 0 = none.

### Synthesis

Identity architecture controls the whole access life cycle, separates conflicting duties and matches authentication strength to account power.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) apply privacy principles to Fernway's member data; (2) design pseudonymisation for analytics; (3) handle data-subject requests through architecture.

### 14.1 Privacy principles

Lucas studies privacy principles common to data-protection laws: lawful purpose, data minimisation, accuracy, storage limitation, security and accountability. He applies them to Fernway's member programme. Members give their address for deliveries and purchase history for rewards. The marketing team wants to analyse purchases by area. Minimisation suggests they need postcode districts and product categories, not names and full addresses. Lucas learns that privacy shapes architecture: the analytics system should receive less data than the shop holds, by design rather than by policy alone.

### 14.2 Pseudonymisation

For analytics, Lucas designs pseudonymisation: member identifiers are replaced by keyed hashes computed with HMAC and a secret key held by the data team, not by analysts. The same member always maps to the same pseudonym, so purchases can be linked, but analysts cannot reverse it without the key. The lab below shows this on synthetic members and why an unkeyed hash is weaker: anyone can hash candidate member numbers and match them. Pseudonymised data is still personal data under many laws, so it still needs protection, but the risk is lower.

### Lab — Keyed versus unkeyed pseudonyms

```python
# Keyed (HMAC) vs unkeyed pseudonyms for synthetic member numbers. Teaching only.
import hmac, hashlib
KEY = b"synthetic-data-team-key"
members = ["M100231", "M100232", "M100233"]
keyed = {m: hmac.new(KEY, m.encode(), hashlib.sha256).hexdigest()[:12] for m in members}
plain = {m: hashlib.sha256(m.encode()).hexdigest()[:12] for m in members}
target_plain, target_keyed = plain["M100232"], keyed["M100232"]
guesses = [f"M1002{i:02d}" for i in range(100)]
hit_plain = [g for g in guesses if hashlib.sha256(g.encode()).hexdigest()[:12] == target_plain]
hit_keyed = [g for g in guesses if hashlib.sha256(g.encode()).hexdigest()[:12] == target_keyed]
print("stable keyed pseudonym:", keyed["M100232"] == hmac.new(KEY, b"M100232", hashlib.sha256).hexdigest()[:12])
print("guessing unkeyed pseudonym recovers:", hit_plain)
print("guessing keyed pseudonym (no key) recovers:", hit_keyed)
```

Run with `python3 lab_pseudo.py`. Verified output:

```text
stable keyed pseudonym: True
guessing unkeyed pseudonym recovers: ['M100232']
guessing keyed pseudonym (no key) recovers: []
```

### 14.3 Data-subject requests

Members may ask to see or delete their data. Lucas maps where member data lives: the shop database, email marketing, analytics, backups and the delivery partner. Without the map, Fernway could not answer requests completely. He proposes that each system expose a way to find and delete a member's records, and that backups expire on a schedule rather than being edited. Handling requests becomes a test of the architecture: if data is spread in unknown places, the organisation cannot keep its promises to members.

### Worked example

Lucas applies six privacy principles to the member programme, designs HMAC-based pseudonyms for analytics and maps five data locations for data-subject requests.

> **Synthetic case.** Members, systems and keys are synthetic.

### Errors and limits

Pseudonymised data can be re-identified by combining fields. Legal requirements differ by jurisdiction.

### Exercises

- **EX040 — Analytics minimisation.** What data does marketing actually need for area analysis? *Rubric:* 3 = postcode districts and product categories, not names or full addresses;; 2 = minimal;; 1 = everything;; 0 = none.
- **EX041 — Unkeyed weakness.** What did the lab show about unkeyed hashes? *Rubric:* 3 = anyone can hash candidate member numbers and match them; keyed hashes resist this;; 2 = match;; 1 = equal;; 0 = none.
- **EX042 — Backup deletion.** How does Lucas handle member deletion in backups? *Rubric:* 3 = backups expire on a schedule rather than being edited;; 2 = expiry;; 1 = edit backups;; 0 = none.

### Synthesis

Privacy architecture minimises data per purpose, pseudonymises analytics with keys and maps every copy to honour requests.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) choose measurements that show whether controls work; (2) compute coverage metrics from synthetic data; (3) present evidence with context.

### 15.1 What to measure

Hannah asks Lucas how Fernway can know whether its controls work. Counting controls says little. He proposes measuring outcomes and coverage: the share of staff accounts with phishing-resistant authentication, the share of laptops meeting the baseline, the time from leaving to account disablement and the number of exposed services found in monthly scans. Each measure links to a risk from earlier chapters. He writes definitions precisely, for example what counts as meeting the baseline, so the numbers mean the same thing each month and cannot be inflated by changing the rules.

### 15.2 Computing coverage

Lucas writes a script that reads synthetic exports from the identity system and device management tool and computes coverage for each measure, broken down by department. The lab below shows overall figures and the department with the weakest coverage: warehouse staff have the lowest share of phishing-resistant authentication because many share scanners and lack individual devices. A department breakdown turns a single average into an action: the warehouse needs a different authentication design, perhaps badge-based login on shared devices, rather than a general reminder to enrol.

### Lab — Control coverage by department

```python
# Coverage of phishing-resistant auth and laptop baseline by department (synthetic export).
staff = {"finance": (12, 11), "buying": (9, 7), "stores": (40, 22), "warehouse": (15, 2), "it": (5, 5)}
laptops = {"finance": (12, 12), "buying": (9, 8), "stores": (14, 11), "warehouse": (3, 2), "it": (6, 6)}
tot = sum(n for n, _ in staff.values()); ok = sum(k for _, k in staff.values())
print(f"phishing-resistant auth: {ok}/{tot} = {ok/tot:.0%}")
for d, (n, k) in sorted(staff.items(), key=lambda x: x[1][1] / x[1][0]): print(f"  {d:9} {k}/{n} = {k/n:.0%}")
tl = sum(n for n, _ in laptops.values()); bl = sum(k for _, k in laptops.values())
print(f"laptops meeting baseline: {bl}/{tl} = {bl/tl:.0%}")
```

Run with `python3 lab_coverage.py`. Verified output:

```text
phishing-resistant auth: 47/81 = 58%
  warehouse 2/15 = 13%
  stores    22/40 = 55%
  buying    7/9 = 78%
  finance   11/12 = 92%
  it        5/5 = 100%
laptops meeting baseline: 39/44 = 89%
```

### 15.3 Evidence in context

Lucas presents results to Fernway's management with counts, percentages and trends, and he explains what each figure does and does not show. High baseline coverage does not prove laptops are secure, only that they meet the baseline; the baseline may itself miss risks. Leaver disablement times show process performance, not whether former staff misused access. He also lists data quality issues, such as devices missing from the management tool. Measurement builds trust when its limits are stated alongside its results.

### Worked example

Lucas defines four coverage and timeliness measures, computes them by department and presents results with limits and data-quality notes.

> **Synthetic case.** Exports and figures are synthetic.

### Errors and limits

Coverage metrics measure presence of controls, not their effectiveness. Missing devices inflate apparent coverage.

### Exercises

- **EX043 — Precise definition.** Why define meeting the baseline precisely? *Rubric:* 3 = so numbers mean the same each month and cannot be inflated by redefinition;; 2 = consistency;; 1 = vague;; 0 = none.
- **EX044 — Weakest department.** Which department had the weakest phishing-resistant coverage in the lab, and why? *Rubric:* 3 = warehouse, 2 of 15, shared scanners without individual devices;; 2 = warehouse;; 1 = finance;; 0 = none.
- **EX045 — Coverage caution.** What does high baseline coverage not prove? *Rubric:* 3 = that laptops are secure; only that they meet the baseline;; 2 = limit;; 1 = proves security;; 0 = none.

### Synthesis

Measurement shows whether controls are in place and working when it is precise, broken down and presented with its limits.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) describe what a security architecture contains; (2) apply SABSA-style attribute thinking to Fernway; (3) produce an architecture overview for a small organisation.

### 16.1 What an architecture contains

Lucas learns that a security architecture is a structured description of how security is achieved across an organisation: principles, the business attributes security must support, the main components and services, how they connect and who owns them. It is not a product list. Dr Bellini introduces SABSA, described by Sherwood, Clark and Lynas (2005), which starts from business attributes, and the Open Group's guide on integrating risk and security into TOGAF. Both emphasise that architecture links what the business values to what is built and operated.

### 16.2 Attributes for Fernway

Lucas works with Hannah to define Fernway's key attributes: available, so the shop sells during peak seasons; trustworthy, so members trust Fernway with their data; accurate, so stock and prices are correct; and compliant, so card and privacy obligations are met. For each attribute he lists the services that support it. Availability depends on cloud hosting and incident response; trustworthiness depends on identity, privacy and checkout protection. When someone proposes cutting a service, the attribute map shows which business value would weaken, turning technical debates into business ones.

### 16.3 An overview document

Lucas writes a ten-page architecture overview: principles such as deny by default and least privilege; attributes; a diagram of zones and services; key security services including identity, logging, backup and payment integration; owners; and known gaps with plans. He keeps it short so it is read. Hannah presents it to Fernway's board, who for the first time see security as a coherent design rather than a series of purchases. The overview becomes the reference for future project reviews. It is reviewed each spring.

### Worked example

Lucas defines four business attributes for Fernway, maps supporting services and writes a ten-page architecture overview presented to the board.

> **Synthetic case.** Attributes and overview are synthetic; SABSA and TOGAF G152 are real.

### Errors and limits

Overviews simplify; details live in supporting documents. Attributes need revisiting when the business changes.

### Exercises

- **EX046 — Not a product list.** Why is a security architecture not a product list? *Rubric:* 3 = it describes principles, attributes, services, connections and owners;; 2 = structure;; 1 = it is;; 0 = none.
- **EX047 — Attribute use.** How does the attribute map help when someone proposes cutting a service? *Rubric:* 3 = it shows which business value would weaken;; 2 = value;; 1 = vague;; 0 = none.
- **EX048 — Board effect.** What did the overview change for Fernway's board? *Rubric:* 3 = they saw security as a coherent design rather than purchases;; 2 = coherent;; 1 = vague;; 0 = none.

### Synthesis

A security architecture links business attributes to services and owners in a short document people actually use.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain the main cryptographic building blocks and their uses; (2) place cryptography in Fernway's architecture; (3) identify key management responsibilities.

### 17.1 Building blocks

Lucas studies symmetric encryption, hashing, message authentication codes, digital signatures and key exchange, using Katz and Lindell's textbook as background. He focuses on what each provides. Encryption gives confidentiality; authenticated encryption such as AES-GCM also gives integrity. Hashes give fingerprints; message authentication codes give integrity and authenticity between parties sharing a key; signatures let anyone verify origin with a public key. Key exchange lets two parties agree a key over an open network. Architects choose among these by need and never design new ones.

### 17.2 Cryptography at Fernway

Lucas maps where cryptography is used: TLS for the shop and email; the payment provider's tokenisation, so Fernway never stores card numbers; HMAC-signed webhooks from the delivery partner; disk encryption on laptops; encrypted backups; and the pseudonymisation from chapter 14. For each he notes the goal and the key holder. He finds that the delivery partner's webhook secret is the same in test and production, which means a leak from a test system would allow forged delivery updates in production. He recommends separate secrets per environment.

### 17.3 Key management responsibilities

Each use of cryptography creates key management duties: generation, secure storage, rotation, revocation and destruction, as NIST SP 800-57 Part 1 Rev. 5 describes. Lucas lists Fernway's keys and secrets with owners and rotation periods. Several had no owner or had never been rotated. He recommends a secrets manager for application secrets and a calendar for certificate renewals. He notes that most cryptographic failures in small organisations come from key handling, not from weak algorithms, so ownership and rotation deserve as much attention as algorithm choice.

### Worked example

Lucas summarises five building blocks, maps six uses at Fernway, finds a shared test and production webhook secret and builds a key inventory with owners.

> **Synthetic case.** Fernway's keys and secrets are synthetic; Katz and Lindell and SP 800-57 Part 1 Rev. 5 are real.

### Errors and limits

Provider-managed keys reduce burden but add dependency. Rotation can break integrations if not coordinated.

### Exercises

- **EX049 — Signature versus MAC.** What does a signature offer that a MAC does not? *Rubric:* 3 = public verification without the ability to sign;; 2 = public verification;; 1 = same;; 0 = none.
- **EX050 — Shared webhook secret.** Why is one webhook secret for test and production a problem? *Rubric:* 3 = a test leak would allow forged production updates;; 2 = forged;; 1 = vague;; 0 = none.
- **EX051 — Main failure source.** Where do most cryptographic failures in small organisations come from? *Rubric:* 3 = key handling rather than weak algorithms;; 2 = keys;; 1 = algorithms;; 0 = none.

### Synthesis

Cryptography in architecture means choosing standard building blocks by need and owning every key they create.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) frame a researchable question about Fernway's security; (2) choose between survey, case study and experiment; (3) plan ethical data collection.

### 18.1 Framing a question

Dr Bellini asks Lucas to turn his placement into a research project. Lucas starts with a vague interest in whether staff follow security policy and narrows it to a question he can answer: do Fernway store staff who received short in-store briefings report suspicious emails more often than staff who received only the online module? The question names a population, an intervention, a comparison and an outcome. It is answerable with data Fernway already collects through its report-phishing button, and it matters to Hannah because it informs how training budget is spent.

### 18.2 Choosing a method

Lucas considers three methods. A survey would ask staff what they do, but self-reports overstate good behaviour. A case study would describe one store in depth but would not support comparison. A quasi-experiment comparing stores that received briefings with similar stores that did not, using actual report rates, gives the strongest answer available. Wohlin and colleagues (2012) describe how to design such studies in software and systems settings, including threats to validity. Lucas chooses the quasi-experiment and notes that stores were not randomly assigned, which limits causal claims.

### 18.3 Ethics and data

Lucas applies to Ashgrove's ethics committee. He will use only aggregated report counts per store per month, with no individual names, and Fernway's management agrees in writing. Staff are told through a notice that store-level data is used for a student study. He stores data on university systems, deletes it after the project and will share only aggregate results. The committee approves with a condition that stores with fewer than five staff are merged so that no individual's behaviour can be inferred from a store figure.

### Worked example

Lucas narrows a vague interest to a comparative question, chooses a quasi-experiment over survey and case study, and obtains ethics approval with a small-cell merging condition.

> **Synthetic case.** The study and stores are synthetic; Wohlin et al. (2012) is real.

### Errors and limits

Non-random assignment limits causal claims. Report button use is only one indicator of vigilance.

### Exercises

- **EX052 — Question parts.** What four parts does Lucas's question name? *Rubric:* 3 = population, intervention, comparison and outcome;; 2 = three of four;; 1 = vague;; 0 = none.
- **EX053 — Why not a survey.** Why did Lucas reject a survey as the main method? *Rubric:* 3 = self-reports overstate good behaviour;; 2 = bias;; 1 = cost;; 0 = none.
- **EX054 — Small-cell condition.** Why did the committee require merging small stores? *Rubric:* 3 = so individual behaviour cannot be inferred from a store figure;; 2 = privacy;; 1 = vague;; 0 = none.

### Synthesis

Good student research starts with a precise question, the strongest feasible method and data collected ethically.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Security architecture and engineering: scope and theory

### Learning outcomes

You will (1) state what security architecture and engineering cover; (2) apply Saltzer and Schroeder's principles to Fernway; (3) relate theory to practical design reviews.

### 19.1 Scope

Lucas writes a short essay on the scope of the field. Security architecture describes how protection is arranged across an organisation; security engineering is the discipline of building systems that stay dependable under attack, as Anderson (2020) puts it. Both cover people, processes and technology, and both work across the life cycle from requirements to retirement. NIST SP 800-160 Vol. 1 Rev. 1 frames this as systems security engineering, integrated into normal engineering rather than added at the end. Lucas notes that at a co-operative of Fernway's size one person often does both.

### 19.2 Classic principles

Lucas applies Saltzer and Schroeder's (1975) design principles to Fernway. Economy of mechanism suggests one identity provider rather than separate logins per system. Fail-safe defaults mean new staff accounts start with no access. Complete mediation means every request to the stock system is checked, not just the first. Least privilege means warehouse accounts cannot change prices. Psychological acceptability means controls must fit busy store routines, or staff will bypass them. He finds that principles nearly fifty years old still explain most of Fernway's weaknesses.

### 19.3 Theory in reviews

Hannah asks how theory helps day to day. Lucas turns the principles into review questions for new projects: what is the default access, is every request checked, who has the least privilege needed, and will staff find the control acceptable. He uses them on a proposed staff rota app and finds that it would give every manager access to all stores' rotas, breaking least privilege. The vendor adds store-level scoping. Theory gives reviewers a shared vocabulary and a checklist grounded in decades of experience.

### Worked example

Lucas defines the field, applies five Saltzer and Schroeder principles to Fernway and uses them to fix a rota app's access scope.

> **Synthetic case.** Fernway and the rota app are synthetic; Anderson (2020), SP 800-160v1r1 and Saltzer and Schroeder (1975) are real.

### Errors and limits

Principles can conflict, such as least privilege versus acceptability. Judgement is still needed.

### Exercises

- **EX055 — Fail-safe default.** How does Fernway apply fail-safe defaults? *Rubric:* 3 = new staff accounts start with no access;; 2 = no access;; 1 = open access;; 0 = none.
- **EX056 — Acceptability.** Why does psychological acceptability matter in stores? *Rubric:* 3 = controls that do not fit routines are bypassed;; 2 = bypass;; 1 = vague;; 0 = none.
- **EX057 — Rota app finding.** What did the principles reveal about the rota app? *Rubric:* 3 = every manager could see all stores, breaking least privilege;; 2 = least privilege;; 1 = vague;; 0 = none.

### Synthesis

Classic principles remain practical review tools that link theory to everyday design decisions.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Security architecture and engineering: foundational cases

### Learning outcomes

You will (1) analyse published incidents for architectural lessons; (2) map lessons to Fernway; (3) write a short case analysis.

### 20.1 Learning from cases

Dr Bellini assigns three well-documented public incident patterns rather than specific company stories: compromise through a supplier with network access, theft of data from an exposed cloud storage bucket, and ransomware that spread because backups were reachable from the same network. Lucas analyses each for architectural causes rather than individual blame. The supplier case shows excessive trust; the storage case shows weak defaults and missing monitoring; the ransomware case shows a single failure domain. Each points to a design principle that could have limited damage.

### 20.2 Mapping to Fernway

Lucas checks Fernway against each pattern. The shopfitting contractor has a permanent VPN account with broad access, matching the supplier pattern; he recommends time-limited access approved per job. Fernway's product images sit in a cloud bucket, correctly public, but an export folder in the same bucket holds a stock file; he recommends a separate private bucket. Backups are already offline from chapter 11. The mapping turns abstract cases into three concrete actions, ranked by the size of the gap and the ease of fixing it.

### 20.3 Writing a case analysis

Lucas writes each analysis in a fixed structure: what happened, architectural causes, what would have limited impact, and relevance to Fernway. He keeps blame out and cites published guidance where it applies, such as SP 800-207 for limiting supplier trust. Each analysis is under a page. Hannah shares them with Fernway's managers, who find short structured cases more persuasive than general warnings. Lucas learns that the value of a case lies in the transferable design lesson, not in the drama of the incident.

### Worked example

Lucas analyses three incident patterns for architectural causes, maps them to Fernway and produces three ranked actions in one-page analyses.

> **Synthetic case.** The incident patterns are generic and synthetic; SP 800-207 is real.

### Errors and limits

Generic patterns may miss local detail. Case lessons need checking against current configurations.

### Exercises

- **EX058 — Supplier pattern.** Which Fernway arrangement matched the supplier pattern? *Rubric:* 3 = the shopfitter's permanent broad VPN account;; 2 = contractor;; 1 = vague;; 0 = none.
- **EX059 — Bucket fix.** What did Lucas recommend for the cloud bucket? *Rubric:* 3 = move the export folder to a separate private bucket;; 2 = separate;; 1 = delete images;; 0 = none.
- **EX060 — Value of a case.** Where does a case's value lie? *Rubric:* 3 = in the transferable design lesson;; 2 = lesson;; 1 = drama;; 0 = none.

### Synthesis

Analysing cases for architectural causes turns other organisations' incidents into specific local improvements.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Security architecture and engineering: system models

### Learning outcomes

You will (1) build a model of Fernway's order system; (2) identify trust boundaries and assets; (3) use the model in a STRIDE review.

### 21.1 Building the model

Lucas draws a data-flow diagram of Fernway's order system: the customer's browser, the web shop, the payment provider, the stock database, the warehouse picking app and the delivery partner. He marks processes, data stores, external entities and flows, and he labels what each flow carries. He validates the diagram with the developer and the warehouse manager, who correct two flows he had missed: a nightly price import from a supplier and a manual spreadsheet upload. Models are only useful if the people who run the system agree they are accurate.

### 21.2 Boundaries and assets

Lucas marks trust boundaries where data crosses between parties or privilege levels: between browser and shop, shop and payment provider, Fernway and the delivery partner, and between the office network and the cloud. He lists assets: customer details, order history, prices and stock levels. The manual spreadsheet upload crosses a boundary without any validation, which means a mistaken or malicious file could change prices across the shop. Marking boundaries makes such gaps visible because every crossing should have a defined check.

### 21.3 STRIDE review

Using Shostack's (2014) STRIDE categories, Lucas examines each element. Spoofing: the delivery partner's webhooks are signed. Tampering: the spreadsheet upload lacks validation. Repudiation: price changes are not logged with the user who made them. Information disclosure: order history is accessible to all staff accounts. Denial of service: the shop relies on one hosting region. Elevation of privilege: the picking app runs with database owner rights. He records seven threats with proposed mitigations and owners, and Fernway schedules the top three for the next quarter.

### Worked example

Lucas builds and validates a data-flow model, marks four trust boundaries and runs a STRIDE review producing seven threats with owners.

> **Synthetic case.** The order system is synthetic; Shostack (2014) is real.

### Errors and limits

Models age as systems change. STRIDE finds categories of threat, not every attack.

### Exercises

- **EX061 — Validating the model.** What did the developer and warehouse manager add? *Rubric:* 3 = a nightly supplier price import and a manual spreadsheet upload;; 2 = one flow;; 1 = vague;; 0 = none.
- **EX062 — Unvalidated crossing.** Why is the spreadsheet upload a concern? *Rubric:* 3 = it crosses a boundary unvalidated and could change prices;; 2 = validation;; 1 = vague;; 0 = none.
- **EX063 — Repudiation finding.** What repudiation gap did STRIDE find? *Rubric:* 3 = price changes are not logged with the user;; 2 = logging;; 1 = vague;; 0 = none.

### Synthesis

A validated model with marked boundaries turns STRIDE into a concrete, owned list of threats.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Security architecture and engineering: data and dependencies

### Learning outcomes

You will (1) classify Fernway's data; (2) map dependencies on suppliers and services; (3) identify single points of failure.

### 22.1 Classifying data

Lucas proposes three data classes for Fernway: public, such as product descriptions; internal, such as stock levels and rotas; and confidential, such as member details, staff records and supplier contracts. Each class has handling rules for storage, sharing and disposal. He keeps the scheme small because staff must apply it without training manuals. He labels the main data stores with their class and finds that a shared drive folder named "misc" holds confidential staff records alongside public marketing images, which means anyone with marketing access can read payroll data.

### 22.2 Mapping dependencies

Lucas lists every external service Fernway depends on: hosting, payment, email, delivery, identity, accounting and the supplier price feed. For each he records the data shared, the contract owner, whether the supplier has security commitments, and what happens if the service fails. The lab below models dependencies as a graph and counts how many business functions each service supports. Identity and hosting each support every online function, so their failure would stop almost everything at once, while the price feed affects only pricing updates.

### Lab — Counting functions affected by each dependency

```python
# Count business functions depending on each service (synthetic map).
deps = {"online sales": ["hosting", "identity", "payment", "email"],
        "click-and-collect": ["hosting", "identity", "email"],
        "delivery tracking": ["hosting", "identity", "delivery"],
        "member accounts": ["hosting", "identity", "email"],
        "pricing updates": ["hosting", "identity", "price feed"],
        "month-end accounts": ["accounting"]}
count = {}
for f, svcs in deps.items():
    for s in svcs: count[s] = count.get(s, 0) + 1
for s, n in sorted(count.items(), key=lambda x: (-x[1], x[0])): print(f"{s:11} supports {n} function(s)")
```

Run with `python3 lab_deps.py`. Verified output:

```text
hosting     supports 5 function(s)
identity    supports 5 function(s)
email       supports 3 function(s)
accounting  supports 1 function(s)
delivery    supports 1 function(s)
payment     supports 1 function(s)
price feed  supports 1 function(s)
```

### 22.3 Single points of failure

The dependency count shows where resilience matters most. Lucas recommends a documented manual fallback for identity, such as a sealed break-glass account, and confirmation that the hosting provider's plan includes recovery in a second region. For the payment provider he notes a contractual commitment instead of technical redundancy, since a second payment provider would cost more than the risk justifies. He explains that not every single point of failure must be removed; some are accepted knowingly with a recovery plan and an owner who monitors the supplier.

### Worked example

Lucas defines three data classes, finds confidential records in a mixed folder, maps seven dependencies and ranks them by functions affected.

> **Synthetic case.** Data, services and counts are synthetic.

### Errors and limits

Dependency maps miss fourth parties, the suppliers of suppliers. Classifications drift without periodic review.

### Exercises

- **EX064 — Mixed folder.** What was wrong with the misc folder? *Rubric:* 3 = confidential staff records next to public images, readable by marketing;; 2 = mixed classes;; 1 = vague;; 0 = none.
- **EX065 — Widest dependency.** Which services supported the most functions in the lab? *Rubric:* 3 = identity and hosting, 5 functions each;; 2 = identity;; 1 = price feed;; 0 = none.
- **EX066 — Accepting a dependency.** Why keep a single payment provider? *Rubric:* 3 = a second would cost more than the risk; covered by contract and a plan;; 2 = cost;; 1 = must remove;; 0 = none.

### Synthesis

Classifying data and counting dependencies show where protection and resilience effort should go.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Security architecture and engineering: methods I

### Learning outcomes

You will (1) apply a risk assessment method to a Fernway project; (2) estimate likelihood and impact consistently; (3) document decisions for review.

### 23.1 A risk assessment method

Fernway plans a click-and-collect service. Lucas runs a risk assessment using the structure in NIST SP 800-30 Rev. 1: identify threat sources and events, vulnerabilities, likelihood, impact and resulting risk. He scales it down for a co-operative, using a one-page template per risk. Threat events include someone collecting another customer's order and staff misusing customer phone numbers. He involves a store manager, because people who run the process know where it can go wrong in ways a diagram never shows. The template fits on a single page so that it gets used.

### 23.2 Consistent estimates

Lucas defines likelihood and impact scales with examples so different people rate consistently: high likelihood means expected several times a year at Fernway; high impact means loss above a set amount or harm to many members. He asks Hannah and the store manager to rate the same five risks independently, then compares ratings. They differ on two, and discussion reveals the store manager knows of past collection mistakes Hannah had not heard about. Consistent scales help, but discussion of differences is where most information emerges.

### 23.3 Documenting decisions

For each risk Lucas records the rating, the proposed treatment and the decision maker. Wrong-person collection is treated with a collection code sent by text and checked at the counter. Phone number misuse is treated by masking numbers in the store app after collection. One low risk, a delayed notification email, is accepted. Each decision has a review date. The record allows auditors and future staff to see why choices were made, which matters when people leave and the reasoning would otherwise be lost.

### Worked example

Lucas applies an SP 800-30-style assessment to click-and-collect with defined scales, compares independent ratings and records treatment decisions.

> **Synthetic case.** The project and ratings are synthetic; SP 800-30 Rev. 1 is real.

### Errors and limits

Qualitative scales hide uncertainty. Small teams may share blind spots despite independent rating.

### Exercises

- **EX067 — Why a store manager.** Why did Lucas involve a store manager? *Rubric:* 3 = people who run the process know where it fails;; 2 = local knowledge;; 1 = vague;; 0 = none.
- **EX068 — Rating differences.** What did comparing independent ratings reveal? *Rubric:* 3 = past collection mistakes known only to the store manager;; 2 = new information;; 1 = vague;; 0 = none.
- **EX069 — Wrong-person treatment.** How was wrong-person collection treated? *Rubric:* 3 = a text collection code checked at the counter;; 2 = code;; 1 = vague;; 0 = none.

### Synthesis

A scaled-down, documented risk method with clear scales turns a new project's risks into owned decisions.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Security architecture and engineering: controls

### Learning outcomes

You will (1) select controls from a catalogue for Fernway; (2) tailor controls to a small organisation; (3) link controls to risks and owners.

### 24.1 Using a catalogue

Lucas uses NIST SP 800-53 Rev. 5 and ISO/IEC 27002:2022 as catalogues rather than checklists. He searches for controls that address the risks already recorded: access control, audit logging, configuration management, supplier relationships and incident response. Catalogues help him avoid forgetting whole areas, such as media disposal, which Fernway had never considered for old till hard drives. He keeps a short list of about thirty controls that matter for Fernway, instead of trying to implement hundreds written for much larger organisations. The short list is reviewed every year.

### 24.2 Tailoring

Each selected control is tailored to Fernway's size. The SP 800-53 audit review control becomes a monthly thirty-minute review of identity alerts by Hannah, not a security operations centre. Configuration management becomes a single baseline for laptops managed by the device tool. Supplier controls become a one-page questionnaire and a contract clause. Lucas records the tailoring reasons so that an auditor can see the control was considered and adapted deliberately. Tailoring is how frameworks become usable for organisations without large security teams.

### 24.3 Linking controls to risks

Lucas builds a table linking each control to the risks it reduces, its owner and its evidence, such as a review log or a configuration report. Controls with no linked risk are questioned; two turn out to be leftovers from a former insurer's requirements and are retired. Risks with no linked control are flagged as gaps. The table becomes Fernway's statement of how security is achieved and gives the board a way to follow progress without reading technical detail. It also makes later audits quicker.

### Worked example

Lucas selects about thirty controls from SP 800-53 and ISO/IEC 27002, tailors them to Fernway's size and links each to risks, owners and evidence.

> **Synthetic case.** Fernway's control list is synthetic; SP 800-53 Rev. 5 and ISO/IEC 27002:2022 are real.

### Errors and limits

Tailoring can slide into weakening controls. Evidence must be real, not a promise.

### Exercises

- **EX070 — Forgotten area.** Which area had Fernway never considered? *Rubric:* 3 = media disposal for old till hard drives;; 2 = disposal;; 1 = vague;; 0 = none.
- **EX071 — Tailored audit review.** How was audit review tailored? *Rubric:* 3 = a monthly thirty-minute review of identity alerts;; 2 = monthly review;; 1 = a security operations centre;; 0 = none.
- **EX072 — Unlinked controls.** What happened to controls with no linked risk? *Rubric:* 3 = questioned; two leftovers were retired;; 2 = retired;; 1 = kept;; 0 = none.

### Synthesis

Catalogues prevent omissions; tailoring and risk links make controls fit a small organisation.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) build a small access-control checker; (2) test least privilege on synthetic role data; (3) report results with limitations.

### 25.1 The task

Dr Bellini sets a laboratory exercise: write a Python program that reads Fernway's synthetic role definitions and user assignments and finds users whose permissions exceed their job's needs. Lucas defines what each job should need, such as till staff needing sales but not price changes, and compares this with what each user actually has. The program runs offline on synthetic data, so it can be shared with classmates without exposing real accounts. The aim is to practise turning a principle, least privilege, into a repeatable check.

### Lab — Finding permissions beyond job needs

```python
# Find permissions beyond job needs (synthetic roles and users).
need = {"till": {"sales"}, "store-manager": {"sales", "rota", "refunds"},
        "warehouse": {"picking", "stock-read"}, "buyer": {"stock-read", "price-change"}}
users = {"u01": ("till", {"sales"}), "u02": ("till", {"sales", "price-change"}),
         "u03": ("till", {"sales", "price-change"}), "u04": ("store-manager", {"sales", "rota", "refunds"}),
         "u05": ("warehouse", {"picking", "stock-read", "db-owner"}), "u06": ("buyer", {"stock-read", "price-change"}),
         "u07": ("warehouse", {"picking", "stock-read"})}
found = 0
for u, (job, has) in sorted(users.items()):
    extra = has - need[job]
    if extra: found += 1; print(f"{u} ({job}) excess: {', '.join(sorted(extra))}")
print(f"{found} of {len(users)} users exceed job needs")
```

Run with `python3 lab_excess.py`. Verified output:

```text
u02 (till) excess: price-change
u03 (till) excess: price-change
u05 (warehouse) excess: db-owner
3 of 7 users exceed job needs
```

### 25.2 Results

The lab finds three users with excess permissions. Two store staff hold price-change rights left over from a temporary promotion project, and one warehouse user holds database owner rights granted during an urgent fix. Lucas checks with Hannah that the job definitions are right before calling these findings, because an incorrect definition would produce false alarms. Hannah removes the promotion rights the same week and opens a change ticket to replace the database owner right with a narrower role after the developer confirms what the warehouse task needs.

### 25.3 Limitations

Lucas lists the limits of his checker. It only knows permissions recorded in the export, not those inside applications with their own user lists. Job definitions are simplified and may miss legitimate exceptions. It finds excess, not misuse. He suggests running it monthly and adding a field for approved exceptions with expiry dates, so temporary rights are visible rather than forgotten. Dr Bellini praises the honest limitations section, noting that reviewers trust tools more when their authors say plainly what they cannot do.

### Worked example

Lucas writes an offline least-privilege checker, finds three excess permissions, confirms definitions with Hannah and lists the checker's limits.

> **Synthetic case.** Roles and users are synthetic.

### Errors and limits

Application-internal permissions are invisible to the checker. Exceptions need expiry to stay honest.

### Exercises

- **EX073 — Excess found.** How many users had excess permissions and why? *Rubric:* 3 = three: two promotion leftovers and one urgent-fix database owner right;; 2 = three;; 1 = vague;; 0 = none.
- **EX074 — Checking definitions.** Why confirm job definitions before reporting? *Rubric:* 3 = wrong definitions cause false alarms;; 2 = accuracy;; 1 = vague;; 0 = none.
- **EX075 — Exception field.** What improvement did Lucas suggest for exceptions? *Rubric:* 3 = an approved-exception field with expiry dates;; 2 = expiry;; 1 = vague;; 0 = none.

### Synthesis

A simple checker turns least privilege into a repeatable monthly test, if its limits are stated.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Security architecture and engineering: methods II

### Learning outcomes

You will (1) use attack trees to analyse a goal; (2) compare designs by attacker cost; (3) combine methods for a design decision.

### 26.1 Attack trees

Lucas analyses the goal "obtain a member's order history" with an attack tree, a method Shostack (2014) describes alongside STRIDE. The root is the goal; branches are ways to reach it: guess or steal the member's password, abuse a staff account, exploit the order page, or obtain a stale export. Each branch splits into steps. Writing the tree forces him to think like an attacker about paths rather than listing controls. He finds the stale export branch, an old spreadsheet emailed to a marketing agency, needs no technical skill at all.

### 26.2 Comparing designs

Lucas assigns rough effort levels to leaf steps and compares two designs for member accounts: passwords with email reset, and passkeys with email fallback. For each design, the cheapest path to the goal shows the attacker's likely route. With passwords, credential stuffing is cheapest. With passkeys, the email fallback becomes cheapest, so the design's strength depends on protecting the email reset. The comparison shows that adding a strong method does not help much if a weak fallback remains, a lesson that applies far beyond Fernway.

### 26.3 Combining methods

Lucas combines his STRIDE results, the attack tree and the risk ratings into one recommendation: adopt passkeys, require a second factor for email fallback, and recall the stale export from the agency with a data-sharing agreement for the future. Each method contributed something different: STRIDE gave breadth, the tree gave attacker paths and the risk ratings gave priority. Dr Bellini notes that experienced architects routinely combine methods because each has blind spots that the others partly cover. Lucas records which method found each issue.

### Worked example

Lucas builds an attack tree for order-history theft, compares password and passkey designs by cheapest path and combines methods into a recommendation.

> **Synthetic case.** The tree and designs are synthetic; Shostack (2014) is real.

### Errors and limits

Effort estimates are rough judgements. Trees can miss branches no one imagined.

### Exercises

- **EX076 — Low-skill branch.** Which branch needed no technical skill? *Rubric:* 3 = the stale export emailed to a marketing agency;; 2 = stale export;; 1 = password;; 0 = none.
- **EX077 — Passkey weak point.** What became the cheapest path with passkeys? *Rubric:* 3 = the email fallback;; 2 = fallback;; 1 = passkeys;; 0 = none.
- **EX078 — Method contributions.** What did STRIDE, the tree and ratings each contribute? *Rubric:* 3 = breadth, attacker paths and priority;; 2 = two of three;; 1 = vague;; 0 = none.

### Synthesis

Attack trees expose the cheapest attacker path, and combining methods covers each one's blind spots.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Security architecture and engineering: verification

### Learning outcomes

You will (1) plan verification of security requirements; (2) use tests, reviews and scans appropriately; (3) record verification evidence.

### 27.1 Planning verification

For the click-and-collect service, Lucas writes security requirements as testable statements: a collection code must be required to release an order; codes must expire after fourteen days; staff app screens must mask phone numbers after collection; and the service must log every release with the staff member's identity. For each requirement he names a verification method and who performs it. Requirements written as vague goals, such as "the service must be secure", cannot be verified and give false comfort to everyone who reads them.

### 27.2 Choosing methods

Lucas matches methods to requirements. Code expiry is checked by an automated test with a clock set forward. Masking is checked by a reviewer using the staff app on a test account. Logging is checked by performing a release and reading the log. A dependency scan checks for known vulnerable libraries, as SP 800-218 recommends. He notes that scans find known issues but not logic flaws such as releasing an order without a code, which only a designed test can catch. Each method covers what it can.

### 27.3 Recording evidence

Every verification produces a record: date, method, result and who performed it. One test fails: codes do not expire because the expiry job was not scheduled in production. The developer fixes it and Lucas reruns the test. The record shows both the failure and the fix, which is more convincing to an auditor than a clean sheet. Lucas adds the tests to the release checklist so that future changes are verified again rather than assumed to have preserved the behaviour.

### Worked example

Lucas writes four testable requirements, matches each to a verification method, finds an unscheduled expiry job and records the failure and fix.

> **Synthetic case.** The service and results are synthetic; SP 800-218 is real.

### Errors and limits

Tests verify only what they were designed to check. Evidence ages with each change.

### Exercises

- **EX079 — Untestable requirement.** Why is "the service must be secure" a poor requirement? *Rubric:* 3 = it cannot be verified;; 2 = untestable;; 1 = fine;; 0 = none.
- **EX080 — Scan limit.** What can a dependency scan not find? *Rubric:* 3 = logic flaws such as release without a code;; 2 = logic flaws;; 1 = everything;; 0 = none.
- **EX081 — Failed test.** Which test failed and why? *Rubric:* 3 = code expiry; the job was not scheduled in production;; 2 = expiry;; 1 = masking;; 0 = none.

### Synthesis

Verification needs testable requirements, matched methods and recorded evidence, including failures.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Security architecture and engineering: failure analysis

### Learning outcomes

You will (1) run a blameless review of a Fernway incident; (2) separate causes into design, process and human factors; (3) produce improvements that last.

### 28.1 The incident

During a weekend sale, Fernway's shop showed some items at a price of zero for forty minutes, and twenty-three orders were placed. Hannah asks Lucas to help run a blameless review. They build a timeline from logs and interviews: a buyer uploaded a price spreadsheet with a blank column, the import treated blanks as zero, and no alert fired because the monitoring watched availability, not prices. Building the timeline before discussing causes keeps the review grounded in what actually happened rather than early assumptions.

### 28.2 Layers of cause

Lucas sorts contributing causes into layers. Design: the import accepted blanks as zero and the spreadsheet upload crossed a trust boundary without validation, as noted in chapter 21. Process: no second person checked large price changes before weekend sales. Human: the buyer was rushing to meet a deadline set by marketing. He avoids naming the buyer as the cause, since anyone under the same pressure with the same tools could have made the error. Blameless framing encourages people to report problems early.

### 28.3 Lasting improvements

The review produces four improvements: the import rejects blanks and any price change over fifty percent without approval; a dashboard alert fires when many prices change at once; a second-person check is added for sale preparation; and deadlines for sale pricing move one day earlier. Each has an owner and a date. Fernway honours the orders as goodwill. Three months later, Lucas checks the improvements are in place and finds the alert has already caught a mistaken currency conversion before customers saw it.

### Worked example

Lucas helps run a blameless review of a zero-price incident, separates design, process and human causes and verifies four improvements later.

> **Synthetic case.** The incident and figures are synthetic.

### Errors and limits

Blameless does not mean accountless; owners are still named for fixes. Timelines from memory need log confirmation.

### Exercises

- **EX082 — Why no alert.** Why did no alert fire? *Rubric:* 3 = monitoring watched availability, not prices;; 2 = monitoring gap;; 1 = vague;; 0 = none.
- **EX083 — Not blaming the buyer.** Why avoid naming the buyer as the cause? *Rubric:* 3 = anyone under the same pressure and tools could err;; 2 = system;; 1 = blame;; 0 = none.
- **EX084 — Later proof.** What showed the improvements worked? *Rubric:* 3 = the alert caught a currency conversion mistake;; 2 = alert;; 1 = vague;; 0 = none.

### Synthesis

Blameless failure analysis finds design and process causes and produces improvements that can be checked later.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Security architecture and engineering: operations

### Learning outcomes

You will (1) describe the operational activities that keep an architecture effective; (2) design a light operating rhythm for Fernway; (3) handle change without losing security.

### 29.1 Architecture in operation

Lucas learns that an architecture decays without operation. Accounts accumulate rights, certificates expire, suppliers change and new tools appear. NIST SP 800-37 Rev. 2 calls the ongoing part continuous monitoring: checking that controls still work and that risk stays acceptable. For Fernway this cannot mean a large team. Lucas lists the activities that matter most: access reviews, patching, backup tests, log review, supplier checks and incident drills. Each has a frequency and an owner, and each produces a small piece of evidence.

### 29.2 An operating rhythm

Lucas designs a calendar. Weekly: Hannah checks identity alerts and patch status. Monthly: the least-privilege checker from chapter 25 runs and results are reviewed; a backup restore is tested. Quarterly: supplier list review, tabletop exercise and a report to the board with the metrics from chapter 15. Annually: architecture overview refresh and risk review. He estimates the total at about four hours a week. Writing the rhythm down means tasks survive holidays and staff changes, because the calendar rather than memory carries them.

### 29.3 Changing safely

Fernway changes often: new stores, seasonal staff and new suppliers. Lucas adds security questions to the existing change form: does this change add a supplier, new data, a new boundary crossing or new privileged access? A yes triggers a short review with Hannah. Most changes answer no and pass quickly. During his placement, the questions catch a new loyalty app that would have received the full member list. The integration is redesigned to send only member numbers and points balances, which is all the app needs.

### Worked example

Lucas lists operational activities, designs a four-hour-a-week rhythm and adds four security questions to the change form, catching an oversharing loyalty app.

> **Synthetic case.** Rhythm and app are synthetic; SP 800-37 Rev. 2 is real.

### Errors and limits

Rhythms slip under workload pressure. Change questions depend on honest answers.

### Exercises

- **EX085 — Why a calendar.** Why write the operating rhythm down? *Rubric:* 3 = tasks survive holidays and staff changes;; 2 = continuity;; 1 = vague;; 0 = none.
- **EX086 — Change trigger.** What triggers a security review of a change? *Rubric:* 3 = adding a supplier, new data, a boundary crossing or privileged access;; 2 = trigger;; 1 = all changes;; 0 = none.
- **EX087 — Loyalty app fix.** How was the loyalty app redesigned? *Rubric:* 3 = to receive only member numbers and points balances;; 2 = minimise;; 1 = vague;; 0 = none.

### Synthesis

An architecture stays effective through a written operating rhythm and light security questions in change management.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) simulate log review for suspicious sign-ins; (2) tune a simple detection rule; (3) measure false positives and misses on synthetic data.

### 30.1 The task

The second laboratory asks Lucas to write a detection rule for suspicious sign-ins using synthetic logs from Fernway's identity system. Each record has a user, a time, a country and a result. He starts with a rule that flags sign-ins from a country other than the user's usual one. The synthetic data includes labelled events, some of them genuine attacks planted by Dr Bellini, so Lucas can measure how well his rule works. All data is generated, so no real staff activity is examined.

### Lab — Tuning an impossible-travel rule

```python
# Tune a sign-in rule on labelled synthetic logs: (user, hour, country, attack?)
logs = [("ana", 9, "UK", 0), ("ana", 10.5, "BR", 1), ("ben", 8, "UK", 0), ("ben", 20, "FR", 0),
        ("cai", 7, "UK", 0), ("cai", 8.5, "RU", 1), ("dee", 9, "UK", 0), ("dee", 15, "ES", 0),
        ("eli", 12, "UK", 0), ("eli", 13.5, "CN", 1), ("fay", 9, "DE", 0), ("fay", 18, "DE", 0),
        ("gus", 9, "UK", 0), ("gus", 30, "IT", 0), ("hal", 9, "UK", 0), ("hal", 9.8, "US", 1)]
home = "UK"
def evaluate(name, flags):
    tp = sum(1 for i in flags if logs[i][3]); fp = len(flags) - tp
    miss = sum(r[3] for r in logs) - tp
    print(f"{name}: flagged {len(flags)}, attacks caught {tp}, false positives {fp}, missed {miss}")
evaluate("any foreign", [i for i, r in enumerate(logs) if r[2] != home])
def travel(window):
    out = []
    for i, r in enumerate(logs):
        for j, p in enumerate(logs[:i]):
            if p[0] == r[0] and p[2] != r[2] and r[1] - p[1] <= window: out.append(i)
    return out
evaluate("2-hour travel", travel(2)); evaluate("1-hour travel", travel(1))
```

Run with `python3 lab_detect.py`. Verified output:

```text
any foreign: flagged 9, attacks caught 4, false positives 5, missed 0
2-hour travel: flagged 4, attacks caught 4, false positives 0, missed 0
1-hour travel: flagged 1, attacks caught 1, false positives 0, missed 3
```

### 30.2 Tuning

The first rule flags every foreign sign-in, including buyers on supplier trips, producing many false alarms. Lucas adds a condition: flag only when two successful sign-ins for the same user come from different countries within two hours, which is too fast to travel. The lab shows the change: false positives fall sharply while the planted attacks are still caught. He also tests a tighter one-hour window and finds it misses three of the four attacks, so he keeps two hours. Tuning is a trade between noise and misses, measured on labelled data.

### 30.3 Reporting

Lucas reports the rule's performance on synthetic data and warns that real data will differ. He recommends a two-week trial in Fernway's identity tool in alert-only mode, with Hannah recording which alerts were real. He notes that the rule misses attackers who sign in from the same country as the user, so it complements rather than replaces phishing-resistant authentication. Dr Bellini notes that stating what a rule cannot detect is as important as its detection rate, because defenders otherwise trust it too much.

### Worked example

Lucas writes and tunes an impossible-travel rule on labelled synthetic logs, compares windows by false positives and misses and plans a trial.

> **Synthetic case.** Logs and attacks are synthetic.

### Errors and limits

Synthetic data rarely matches real noise. VPNs and travel apps can confuse location rules.

### Exercises

- **EX088 — First rule problem.** What was wrong with flagging all foreign sign-ins? *Rubric:* 3 = buyers on trips caused many false alarms;; 2 = false positives;; 1 = vague;; 0 = none.
- **EX089 — Window choice.** Why keep two hours rather than one? *Rubric:* 3 = one hour missed three of four attacks;; 2 = miss;; 1 = faster;; 0 = none.
- **EX090 — Rule blind spot.** What does the rule miss? *Rubric:* 3 = attackers signing in from the user's own country;; 2 = same country;; 1 = vague;; 0 = none.

### Synthesis

Detection rules are tuned on labelled data by trading false alarms against misses, and their blind spots must be stated.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Security architecture and engineering: advanced cases

### Learning outcomes

You will (1) analyse a zero trust migration for Fernway; (2) weigh resilience design for peak seasons; (3) evaluate trade-offs in advanced designs.

### 31.1 Zero trust for a co-operative

Hannah wonders whether zero trust applies to Fernway. Lucas reads NIST SP 800-207 and explains its core idea: no implicit trust based on network location; every access request is evaluated using identity, device state and context. For Fernway this means retiring the office VPN for most uses and putting the stock system and staff apps behind an identity-aware access proxy. He plans a phased move starting with the finance app, which has few users and high value, so lessons are learned before the busy stores are included.

### 31.2 Resilience for peak season

Fernway earns a third of its online revenue in six weeks before winter. Lucas uses ideas from NIST SP 800-160 Vol. 2 Rev. 1 on cyber resilience: anticipate, withstand, recover and adapt. He proposes a pre-season freeze on non-essential changes, a tested failover for the shop to a second hosting region, a rehearsed manual order process if payment fails, and extra monitoring during peak. Each measure is sized to the risk: the failover costs money all year, so he checks it against the revenue lost in a peak-day outage before recommending it.

### 31.3 Weighing trade-offs

Advanced designs bring costs. The access proxy adds a dependency on the identity provider, already a single point of failure from chapter 22. The change freeze delays features marketing wants. Lucas presents each trade-off openly: what is gained, what is lost and who carries the cost. The board approves the proxy for finance and the freeze, but defers the second hosting region until next year's budget, accepting the risk for one season with the manual order process as a fallback. Lucas records the decision and its review date.

### Worked example

Lucas plans a phased zero trust move starting with finance, applies resilience goals to peak season and presents trade-offs leading to a recorded board decision.

> **Synthetic case.** Plans and costs are synthetic; SP 800-207 and SP 800-160 Vol. 2 Rev. 1 are real.

### Errors and limits

Zero trust is a direction, not a product. Deferred resilience leaves the season exposed.

### Exercises

- **EX091 — Why finance first.** Why start zero trust with the finance app? *Rubric:* 3 = few users and high value, so lessons are learned safely;; 2 = pilot;; 1 = stores first;; 0 = none.
- **EX092 — Four resilience goals.** What four resilience goals did Lucas use? *Rubric:* 3 = anticipate, withstand, recover and adapt;; 2 = three;; 1 = vague;; 0 = none.
- **EX093 — Deferred item.** What did the board defer and with what fallback? *Rubric:* 3 = the second hosting region; manual order process;; 2 = deferred;; 1 = vague;; 0 = none.

### Synthesis

Advanced designs such as zero trust and resilience planning are phased and justified by explicit trade-offs.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Security architecture and engineering: interdisciplinary interfaces

### Learning outcomes

You will (1) work with legal, finance and operations colleagues on security decisions; (2) translate security into each discipline's language; (3) resolve conflicting priorities.

### 32.1 Different languages

Lucas finds that each Fernway department hears security differently. The finance manager thinks in costs and losses; the operations manager thinks in throughput and staff time; the co-operative's legal adviser thinks in obligations and liability. When Lucas presented the access proxy in technical terms, nobody engaged. When he described it to finance as reducing the chance of payment fraud, to operations as removing the VPN step that slows store staff, and to legal as supporting data protection duties, each person saw a reason to support it.

### 32.2 Working with legal and privacy

The legal adviser asks whether the sign-in detection rule from chapter 30 is lawful under data protection rules, since it processes staff location data. Lucas and the adviser document the purpose, the data minimised to country level, the retention period and the staff notice, and they record a legitimate-interest assessment. ISO/IEC 27001:2022 expects such obligations to be identified and met. The work slows the trial by two weeks but makes it defensible. Lucas learns that early legal involvement is cheaper than redesign after an objection.

### 32.3 Resolving conflicts

Operations wants seasonal staff to start work within an hour of arrival; security wants accounts approved and trained first. Lucas brokers a compromise: seasonal accounts are pre-created with limited till rights, activated on arrival by a store manager, and expire at season end. Training is a five-minute video on the till. Both sides get most of what they need. He records the compromise as a design decision so that it is not reopened every season. Interdisciplinary work is mostly finding designs that serve several goals at once.

### Worked example

Lucas translates the access proxy into finance, operations and legal terms, documents a lawful basis for detection and brokers a seasonal account compromise.

> **Synthetic case.** Departments and decisions are synthetic; ISO/IEC 27001:2022 is real.

### Errors and limits

Translation can oversell benefits. Compromises need review if conditions change.

### Exercises

- **EX094 — Finance framing.** How did Lucas frame the proxy for finance? *Rubric:* 3 = reducing the chance of payment fraud;; 2 = fraud;; 1 = technical terms;; 0 = none.
- **EX095 — Detection and law.** What did Lucas and the adviser document for the detection rule? *Rubric:* 3 = purpose, country-level minimisation, retention, notice and a legitimate-interest assessment;; 2 = three items;; 1 = vague;; 0 = none.
- **EX096 — Seasonal compromise.** What was the seasonal account compromise? *Rubric:* 3 = pre-created limited accounts activated on arrival, expiring at season end;; 2 = limited;; 1 = vague;; 0 = none.

### Synthesis

Security decisions succeed when translated into each discipline's language and designed to serve several goals at once.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse the quasi-experiment data from chapter 18; (2) address threats to validity; (3) report findings with appropriate caution.

### 33.1 Analysing the data

Lucas collects six months of aggregated report-button counts. Briefed stores show a monthly report rate per staff member before and after the briefings; comparison stores show the same over the same months. He computes the change in each group and the difference between those changes, a simple difference-in-differences. The lab below runs the calculation on the synthetic counts. Briefed stores rose more than comparison stores, suggesting the briefings helped, though the estimate rests on the assumption that both groups would otherwise have followed similar trends.

### Lab — Difference-in-differences on report rates

```python
# Difference-in-differences on report rates (reports per staff per month), synthetic.
briefed = {"before": [0.20, 0.25, 0.22], "after": [0.55, 0.58, 0.51]}
compare = {"before": [0.21, 0.19, 0.24], "after": [0.27, 0.25, 0.22]}
m = lambda xs: sum(xs) / len(xs)
db = m(briefed["after"]) - m(briefed["before"]); dc = m(compare["after"]) - m(compare["before"])
print(f"briefed change {db:+.2f}, comparison change {dc:+.2f}, difference-in-differences {db - dc:+.2f}")
```

Run with `python3 lab_did.py`. Verified output:

```text
briefed change +0.32, comparison change +0.03, difference-in-differences +0.29
```

### 33.2 Threats to validity

Lucas uses the categories in Wohlin and colleagues (2012). Internal validity: briefed stores were chosen by regional managers, perhaps because they were already engaged. Construct validity: report-button use measures willingness to report, not ability to detect. External validity: Fernway's stores may differ from other retailers. Conclusion validity: with few stores, the result could arise by chance. He addresses some threats by checking that pre-briefing trends were similar, and he states the rest openly rather than hiding them in an appendix. Each threat is listed with its likely direction of bias.

### 33.3 Reporting with caution

Lucas writes that briefed stores showed a larger rise in reporting than comparison stores, consistent with a benefit from briefings, but that the design cannot rule out other explanations. He recommends a randomised rollout for the next round, where stores are assigned by lot, which Fernway agrees to try. Hannah uses the cautious result to keep briefings while the stronger study runs. Dr Bellini marks the report highly for matching the strength of its claims to the strength of its evidence.

### Worked example

Lucas runs a difference-in-differences on synthetic report rates, lists four validity threats and reports a cautious finding with a randomised follow-up.

> **Synthetic case.** Counts are synthetic; Wohlin et al. (2012) is real.

### Errors and limits

Few units make estimates unstable. Parallel trends cannot be proven, only checked.

### Exercises

- **EX097 — DiD result.** What was the difference-in-differences in the lab? *Rubric:* 3 = 0.29 reports per staff per month;; 2 = positive;; 1 = vague;; 0 = none.
- **EX098 — Construct threat.** What construct validity threat did Lucas name? *Rubric:* 3 = report-button use measures willingness, not detection ability;; 2 = construct;; 1 = vague;; 0 = none.
- **EX099 — Stronger design.** What did Lucas recommend next? *Rubric:* 3 = randomised rollout by lot;; 2 = randomise;; 1 = vague;; 0 = none.

### Synthesis

Analysis should match claim strength to design strength and name validity threats openly.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two architectural options for Fernway's staff access; (2) use weighted criteria; (3) test sensitivity of the choice.

### 34.1 The options

Fernway must choose how store staff sign in to the stock app on shared tablets. Option A is individual passwords with a short session timeout. Option B is badge tap plus a short PIN, with badges linked to the identity provider. Lucas compares them as his comparative project. He defines criteria with Hannah and store managers: security against shared-credential misuse, speed at the till, cost, ease of leaver removal and accessibility for staff with disabilities. Defining criteria before scoring prevents the favoured option from shaping the criteria.

### Lab — Weighted comparison with sensitivity check

```python
# Weighted comparison of two sign-in options with a sensitivity check (synthetic).
crit = ["security", "speed", "cost", "leavers", "access"]
w = {"security": 0.30, "speed": 0.25, "cost": 0.15, "leavers": 0.15, "access": 0.15}
score = {"A": {"security": 3, "speed": 2, "cost": 5, "leavers": 3, "access": 3},
         "B": {"security": 4, "speed": 5, "cost": 2, "leavers": 5, "access": 4}}
def totals(wt):
    s = sum(wt.values()); return {o: sum(wt[c] * score[o][c] for c in crit) / s for o in score}
print("base:", {o: f"{v:.2f}" for o, v in totals(w).items()})
w2 = dict(w, cost=0.30); print("cost weight doubled:", {o: f"{v:.2f}" for o, v in totals(w2).items()})
```

Run with `python3 lab_weighted.py`. Verified output:

```text
base: {'A': '3.05', 'B': '4.10'}
cost weight doubled: {'A': '3.30', 'B': '3.83'}
```

### 34.2 Weighted scoring

Each criterion receives a weight agreed by the group, and each option is scored from one to five on each criterion. The lab computes weighted totals: Option B scores higher, mainly on speed and leaver removal, while Option A is cheaper. Lucas records who scored what and why, so the scores can be challenged. He notes that scoring hides uncertainty, so a narrow gap would not justify a strong recommendation without further evidence, such as a pilot in one store.

### 34.3 Sensitivity

Lucas checks whether the choice changes if weights shift. The lab doubles the cost weight and finds Option B still wins, though by less. Only if cost is weighted more heavily than security and speed together does Option A win. Because no one at Fernway believes cost matters that much here, the recommendation is robust. He presents the result with the sensitivity check, which persuades the finance manager more than the totals alone. A pilot in one store confirms that badge sign-in takes about four seconds.

### Worked example

Lucas compares two shared-tablet sign-in options with five weighted criteria, checks sensitivity to the cost weight and confirms with a pilot.

> **Synthetic case.** Options, weights and scores are synthetic.

### Errors and limits

Weights reflect opinions. Scores from a small group may share bias.

### Exercises

- **EX100 — Criteria first.** Why define criteria before scoring? *Rubric:* 3 = so the favoured option cannot shape them;; 2 = bias;; 1 = vague;; 0 = none.
- **EX101 — Totals.** What were the weighted totals in the lab? *Rubric:* 3 = A 3.05, B 4.10;; 2 = B higher;; 1 = A higher;; 0 = none.
- **EX102 — Sensitivity result.** What happened when the cost weight doubled? *Rubric:* 3 = B still won, 3.83 to 3.30;; 2 = B wins;; 1 = A wins;; 0 = none.

### Synthesis

Weighted comparison with a sensitivity check gives a robust, challengeable recommendation.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) write a capstone proposal for a security architecture project; (2) define scope, deliverables and evaluation; (3) obtain agreement from sponsors.

### 35.1 Choosing the capstone

Lucas proposes his capstone: a security architecture for Fernway's planned second warehouse, which will use automated picking robots and a new warehouse management system. The project is real enough to matter to Fernway, bounded enough for one student over two terms, and rich in architecture questions: new suppliers, operational technology on the network, new staff roles and integration with the existing stock system. Dr Bellini approves the topic on condition that the scope excludes the robots' internal safety systems, which need specialist engineers.

### 35.2 Scope and deliverables

The proposal defines deliverables: an architecture overview for the warehouse, a data-flow model with trust boundaries, a STRIDE and attack-tree analysis, a control set linked to risks, verification tests for five key requirements, and an evaluation. It lists what is out of scope, including robot safety and the supplier's internal development practices. It sets milestones each month. Writing exclusions down protects the student from scope creep and tells the sponsor clearly what will not be delivered, so expectations stay realistic.

### 35.3 Evaluation and agreement

Lucas defines how the capstone will be judged: whether Fernway adopts the design, whether verification tests pass, and whether an independent reviewer, a security architect from a partner co-operative, finds major gaps. He writes these criteria in the proposal so success is not defined after the fact. Hannah signs as sponsor, Dr Bellini as supervisor, and the warehouse project manager agrees to share documents. The proposal takes four pages and becomes the contract for the next two terms. Copies are kept by all three signatories.

### Worked example

Lucas proposes a warehouse security architecture capstone, defines deliverables and exclusions, sets evaluation criteria in advance and obtains three signatures.

> **Synthetic case.** The warehouse and people are synthetic.

### Errors and limits

Real projects slip, affecting student timelines. Sponsors may change priorities.

### Exercises

- **EX103 — Excluded area.** What did Dr Bellini require to be excluded? *Rubric:* 3 = the robots' internal safety systems;; 2 = robot safety;; 1 = vague;; 0 = none.
- **EX104 — Why list exclusions.** Why write exclusions into the proposal? *Rubric:* 3 = to prevent scope creep and set sponsor expectations;; 2 = scope;; 1 = vague;; 0 = none.
- **EX105 — Advance criteria.** Why define evaluation criteria in the proposal? *Rubric:* 3 = so success is not defined after the fact;; 2 = advance;; 1 = vague;; 0 = none.

### Synthesis

A capstone proposal fixes scope, deliverables, exclusions and evaluation before work begins.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) apply security architecture skills in a community setting; (2) adapt advice for organisations without IT staff; (3) reflect on what transfers.

### 36.1 A community placement

As part of field practice, Lucas volunteers for four weeks with a local food bank that uses donated laptops, a free email service and a spreadsheet of client households. There is no IT staff, and volunteers change weekly. He applies the same thinking as at Fernway, but the constraints are harsher: no budget, little time and users with mixed digital confidence. He starts by listening to how volunteers work, since any advice that adds steps to a busy distribution shift will be ignored.

### 36.2 Adapting the advice

Lucas identifies three priorities: the client spreadsheet is shared by link with anyone, the shared volunteer account has no second factor, and laptops are not encrypted. He fixes sharing to named accounts, turns on the email provider's free second factor for the coordinator and moves volunteers to individual free accounts, and enables built-in disk encryption. He writes a one-page guide with pictures. He drops a planned password manager rollout because volunteers would not sustain it. Advice for small community groups must be minimal, free and easy to keep doing.

### 36.3 Reflection

In his reflective log, Lucas notes what transferred from Fernway: data classification, least privilege and asking who would notice a problem. What did not transfer: change forms, metrics dashboards and supplier questionnaires, which assume staff time. He realises that architecture is about fitting protection to the organisation, and that a simple design that volunteers follow beats a complete design they abandon. The food bank coordinator later reports that the guide is pinned by the distribution desk and new volunteers read it on their first day.

### Worked example

Lucas adapts architecture advice for a food bank, fixes three priorities with free tools and reflects on what transfers from a retailer.

> **Synthetic case.** The food bank is synthetic.

### Errors and limits

Volunteer turnover erodes changes. Free services can change terms.

### Exercises

- **EX106 — First step.** Why did Lucas start by listening to volunteers? *Rubric:* 3 = advice that adds steps to busy shifts is ignored;; 2 = fit;; 1 = vague;; 0 = none.
- **EX107 — Dropped plan.** What did Lucas drop and why? *Rubric:* 3 = a password manager rollout volunteers would not sustain;; 2 = sustain;; 1 = cost;; 0 = none.
- **EX108 — What transferred.** Name two things that transferred from Fernway. *Rubric:* 3 = classification, least privilege, asking who would notice;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Security architecture in community settings means minimal, free measures that volunteers will actually keep doing.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) appraise published sources critically; (2) distinguish standards, research and opinion; (3) present a fair evidence summary to peers.

### 37.1 Appraising sources

In the seminar, each student reviews evidence on a question. Lucas takes the question: does network segmentation reduce the spread of ransomware in small organisations? He collects standards, vendor reports, academic papers and blog posts. For each he asks who wrote it, what method was used, what data supports it and what interests the author has. Herley and van Oorschot (2017) warn that much security knowledge rests on assertion rather than tested claims, so Lucas looks for evidence that would survive scrutiny.

### 37.2 Types of source

Lucas sorts his sources. Standards such as SP 800-53 Rev. 5 and ISO/IEC 27002:2022 record expert consensus about good practice but do not measure outcomes. Vendor reports offer large data sets but have commercial interests and unclear methods. Academic studies have clearer methods but often study simulated networks. Blog posts give vivid examples but cannot be generalised. He weighs each type for what it can show. The result is a picture in which segmentation is widely recommended and plausible, but outcome evidence for small organisations is thin.

### 37.3 Presenting fairly

Lucas presents his summary to the seminar with a table showing each source, its type, its finding and its limits. He states his conclusion carefully: segmentation is reasonable practice supported by expert consensus and simulation studies, but real-world measurements for small organisations are scarce. A classmate challenges him with a vendor statistic; he explains why its method is unclear. Dr Bellini praises the fairness, noting that an honest summary of weak evidence is more useful to practitioners than a confident one built on marketing.

### Worked example

Lucas appraises sources on segmentation and ransomware, classifies them by type and presents a fair summary noting thin outcome evidence.

> **Synthetic case.** The source collection is synthetic in detail; Herley and van Oorschot (2017), SP 800-53 Rev. 5 and ISO/IEC 27002:2022 are real.

### Errors and limits

Absence of evidence is not evidence of absence. Reviewers can carry their own bias.

### Exercises

- **EX109 — Four questions.** What four questions did Lucas ask of each source? *Rubric:* 3 = author, method, data and interests;; 2 = three;; 1 = vague;; 0 = none.
- **EX110 — Standards limit.** What do standards not do? *Rubric:* 3 = measure outcomes;; 2 = outcomes;; 1 = everything;; 0 = none.
- **EX111 — Conclusion.** What was Lucas's conclusion on segmentation? *Rubric:* 3 = reasonable practice backed by consensus and simulations, but thin real-world evidence for small organisations;; 2 = balanced;; 1 = proven;; 0 = none.

### Synthesis

Fair evidence review weighs each source type for what it can show and states weak evidence honestly.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) carry out the capstone architecture work; (2) manage changes in a live project; (3) keep traceability from risks to controls.

### 38.1 Doing the work

Lucas works through the capstone deliverables for the new warehouse. He models the warehouse management system, the robot controllers, the stock system integration and the supplier's remote support link. He marks a boundary between the robot network and the office network, with only the warehouse management system allowed to talk to both. He runs STRIDE and an attack tree for the goal "stop picking during peak season", which reveals that the supplier's remote support link is the easiest path because it uses a shared password.

### 38.2 Managing change

Midway, Fernway switches warehouse management vendors after a pricing dispute. Lucas's models are partly obsolete. He reviews which deliverables are affected, informs Hannah and Dr Bellini, and agrees a revised milestone. The new vendor's system uses a cloud service rather than an on-site server, so the boundary moves. He reuses his method and most of his risk list, updating only what changed. The experience teaches him that architecture documents must be designed to change, with clear assumptions so readers know what to revisit.

### 38.3 Traceability

Lucas keeps a table from each risk to its controls, requirements and verification tests, as in chapter 24. When the vendor changes, the table shows which controls depend on the old system and need replacing. The supplier remote support link becomes a requirement for named accounts with multi-factor authentication and session recording, verified by a test login. By the end, every high risk traces to at least one verified control. Traceability makes the capstone auditable and lets Fernway maintain the design after Lucas leaves.

### Worked example

Lucas models the warehouse, finds a shared-password support link, adapts to a vendor switch and maintains risk-to-test traceability.

> **Synthetic case.** The warehouse and vendors are synthetic.

### Errors and limits

Vendor changes can invalidate earlier tests. Traceability tables need ownership to stay current.

### Exercises

- **EX112 — Easiest path.** What was the easiest path to stopping picking? *Rubric:* 3 = the supplier's remote support link with a shared password;; 2 = support link;; 1 = vague;; 0 = none.
- **EX113 — Vendor switch.** How did Lucas handle the vendor switch? *Rubric:* 3 = reviewed affected deliverables, agreed new milestones, reused method and updated what changed;; 2 = adapted;; 1 = restarted;; 0 = none.
- **EX114 — Support link control.** What requirement replaced the shared support password? *Rubric:* 3 = named accounts with multi-factor authentication and session recording;; 2 = named;; 1 = vague;; 0 = none.

### Synthesis

Capstone implementation succeeds through solid models, adaptation to change and traceability from risk to verified control.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against agreed criteria; (2) use an independent reviewer; (3) separate achievement from remaining gaps.

### 39.1 Against the criteria

Lucas returns to the criteria from his proposal. Adoption: Fernway adopted the architecture overview and controls for the new warehouse. Verification: four of five key tests passed; the fifth, robot network isolation, could not be run because the robots had not arrived. Independent review: a security architect from a partner co-operative reviewed the design. He reports each criterion with evidence and does not stretch the incomplete test into a pass. Pre-agreed criteria make evaluation straightforward and honest. The incomplete test is marked as pending, not passed.

### 39.2 Independent review

The reviewer finds no major gaps but two moderate ones: no plan for patching robot controllers, which often cannot be updated during operation, and no process for revoking the vendor's access if the contract ends. Lucas accepts both, adds a maintenance-window plan agreed with the vendor and a contract exit checklist. He notes that the reviewer saw gaps he had missed because she had worked with operational technology before. Independent review is valuable precisely because the reviewer brings different experience.

### 39.3 Achievement and gaps

Lucas's evaluation lists achievements, the two fixed review findings and remaining gaps: the isolation test awaits the robots, and the identity provider remains a single point of failure across both warehouses. He gives each remaining gap an owner at Fernway. Dr Bellini notes that a good evaluation leaves the sponsor knowing exactly what is done and what is not. Hannah schedules the isolation test for the robots' installation week and adds the identity resilience question to next year's budget. The handover note lists every open item with a date.

### Worked example

Lucas evaluates his capstone against three pre-agreed criteria, incorporates two reviewer findings and hands remaining gaps to named owners.

> **Synthetic case.** The evaluation and people are synthetic.

### Errors and limits

Reviewer availability limits depth. Tests deferred to installation may be forgotten without owners.

### Exercises

- **EX115 — Unrun test.** Which test could not be run and why? *Rubric:* 3 = robot network isolation; robots had not arrived;; 2 = isolation;; 1 = vague;; 0 = none.
- **EX116 — Reviewer findings.** What two gaps did the reviewer find? *Rubric:* 3 = no robot controller patching plan and no vendor access revocation process;; 2 = one;; 1 = vague;; 0 = none.
- **EX117 — Remaining gap owners.** What happened to remaining gaps? *Rubric:* 3 = each received an owner at Fernway;; 2 = owners;; 1 = ignored;; 0 = none.

### Synthesis

Honest evaluation against pre-agreed criteria, plus independent review, shows what is done and what remains.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) structure a bachelor's thesis in security architecture; (2) present findings to academic and practitioner audiences; (3) plan next steps in study or work.

### 40.1 Structuring the thesis

Lucas writes his thesis in the standard structure: introduction with the problem and questions, background on principles and standards, method, the Fernway architecture and capstone, results including verification and review, discussion of limits, and conclusion. He cites only sources he read, including Saltzer and Schroeder (1975), Shostack (2014), SP 800-207 and Anderson (2020). He keeps synthetic labels on every data set and case detail. The thesis runs to forty pages, with models and test records in appendices. Each chapter opens with a short summary, and a glossary explains terms such as trust boundary for non-specialist readers.

### 40.2 Two audiences

Lucas presents twice. To the examiners he explains methods, validity and how his work relates to published guidance. To Fernway's board he explains what changed, what it cost, what risks remain and what decisions they must make next. He uses the same evidence but different emphasis and language, as practised in chapter 32. The board asks about the identity provider risk, and the examiners ask about the quasi-experiment's validity. He answers both directly, admitting uncertainty where it exists. Each presentation lasts twenty minutes plus questions.

### 40.3 Next steps

Lucas reflects on his course. He has learned to model systems, assess risks, choose and verify controls, measure outcomes, review evidence and work across disciplines. Fernway offers him a junior security role, and Dr Bellini suggests a postgraduate certificate in security architecture later. He chooses the job, with plans to study part time. His final advice to future students is to treat every design as a hypothesis to test, and to write down what is not known as carefully as what is.

### Worked example

Lucas structures a forty-page thesis, presents to examiners and the board with different emphasis and plans to join Fernway while studying part time.

> **Synthetic case.** Thesis details and people are synthetic; cited works are real.

### Errors and limits

Presentations simplify; written work holds the detail. Career plans change.

### Exercises

- **EX118 — Thesis sources.** What rule did Lucas follow for citations? *Rubric:* 3 = cite only sources he actually read;; 2 = read;; 1 = any;; 0 = none.
- **EX119 — Board questions.** What did the board ask about? *Rubric:* 3 = the identity provider risk;; 2 = identity;; 1 = validity;; 0 = none.
- **EX120 — Final advice.** What was Lucas's advice to future students? *Rubric:* 3 = treat every design as a hypothesis and record unknowns carefully;; 2 = hypothesis;; 1 = vague;; 0 = none.

### Synthesis

A thesis and two tailored presentations complete the course, turning project work into shared knowledge and next steps.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Lucas Haddon, Dr Marco Bellini, Hannah Osei, Ashgrove University, Fernway Outdoor Co-operative and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** M OR (S AND R), and (M OR S) AND R.

**EX002.** In 2 of 8 rows, both where a manager issues a refund without a receipt.

**EX003.** The case of contractors maintaining warehouse scanners, which neither rule covered.

**EX004.** Because it runs on lower layers, such as an unpatched server, whose weaknesses it inherits.

**EX005.** Reviewing the delivery partner's long-standing access to customer addresses.

**EX006.** An old label-printing laptop holding customer data and a test copy of the shop database in cloud storage.

**EX007.** Because there are endless ways to encode harmful input, so a list of bad patterns is never complete.

**EX008.** Letters, digits, spaces and a small set of punctuation, with a maximum length of sixty characters.

**EX009.** It must be revoked and replaced, because copies of the history may already exist.

**EX010.** Each paragraph makes one point and leads logically to the next.

**EX011.** Because secondary summaries may distort the original, and he should cite only what he has read.

**EX012.** That SP 800-207 describes principles to reduce implicit trust, and that effects on small retailers' incidents are not established by the sources.

**EX013.** Prices and orders cannot be altered by anyone without authorisation.

**EX014.** Using passwords leaked from other sites to log in; rate limiting and multi-factor authentication help.

**EX015.** By calling the supplier on a known number and requiring two approvals.

**EX016.** Logins, network connections or permissions between nodes.

**EX017.** It grew from 3 to 4 hops, now passing through the warehouse management system.

**EX018.** The admin workstation and file server, because many shortest paths to sensitive data pass through them.

**EX019.** A compromised scanner sits on the same segment as finance laptops and can reach them directly.

**EX020.** Because an attacker controlling it can redirect customers and may pass certificate validation for Fernway's name.

**EX021.** A managed remote-access service requiring multi-factor authentication.

**EX022.** Authentication establishes who the user is; authorisation decides what that user may do.

**EX023.** A manager could adjust another store's stock because only the role, not the store, was checked.

**EX024.** Passwords and session tokens.

**EX025.** The attacker inherits only the shop's read and order-writing rights, not schema or export powers.

**EX026.** Three: the search query and two others built the same way.

**EX027.** Synthetic or properly masked data, never raw member records.

**EX028.** What may be tested, how, when, by whom, and an emergency contact.

**EX029.** Synthetic records he creates, never real member data.

**EX030.** Report it to their own organisation's security team rather than having Lucas investigate.

**EX031.** Because any malware a user runs gets full control of the laptop.

**EX032.** Individual accounts that elevate privileges through logged commands.

**EX033.** Updates for devices such as tills and scanners that people don't think of as computers.

**EX034.** Because checking only suspected accounts would bias the estimate upward.

**EX035.** About 9.0% to 18.4%, implying roughly 361 to 735 affected accounts.

**EX036.** Because with such small counts the change could easily be chance.

**EX037.** Access that accumulates as people change jobs; the mover process removes old roles when new ones are granted.

**EX038.** A buyer who could also approve supplier payments, enabling a fake supplier fraud.

**EX039.** Because fake pages can capture and relay text codes, while passkeys only work on the genuine website.

**EX040.** Postcode districts and product categories, without names or full addresses.

**EX041.** That an attacker who hashes guessed member numbers can match unkeyed pseudonyms, but not keyed ones without the key.

**EX042.** Backups expire on a set schedule instead of being edited record by record.

**EX043.** So results are comparable over time and cannot be improved simply by changing what counts.

**EX044.** The warehouse, at 2 of 15 staff, because staff share scanners and lack individual devices.

**EX045.** It does not prove the laptops are secure, only that they comply with a baseline that may itself have gaps.

**EX046.** Because it explains how security is achieved through principles, services, connections and owners, not what was bought.

**EX047.** It shows which business attribute, such as trustworthiness, would be weakened.

**EX048.** For the first time they saw security as a coherent design rather than a set of purchases.

**EX049.** Anyone with the public key can verify, without being able to create signatures.

**EX050.** Because a leak from the less protected test environment would let attackers forge production delivery updates.

**EX051.** From key handling, such as missing owners and rotation, rather than weak algorithms.

**EX052.** Store staff, in-store briefings, the online-only comparison and report rates.

**EX053.** Because staff tend to overstate their good behaviour when asked.

**EX054.** So no individual's behaviour could be inferred from a figure for a very small store.

**EX055.** New accounts start with no access until a role is granted.

**EX056.** Because staff under time pressure bypass controls that do not fit their routines.

**EX057.** It gave every manager access to every store's rota, so the vendor added store-level scoping.

**EX058.** The shopfitting contractor's permanent VPN account with broad access.

**EX059.** Move the stock export to a separate private bucket, leaving product images public.

**EX060.** In the transferable design lesson rather than the details of the incident.

**EX061.** A nightly price import from a supplier and a manual spreadsheet upload.

**EX062.** Because it crosses a trust boundary without validation, so a bad file could change prices across the shop.

**EX063.** Price changes are not logged with the identity of the user who made them.

**EX064.** It held confidential staff records alongside public images, so marketing users could read payroll data.

**EX065.** Identity and hosting, each supporting all 5 online functions.

**EX066.** Because redundancy would cost more than the risk justifies, so it is accepted with a contract, a plan and an owner.

**EX067.** Because people running the process know failure modes that diagrams do not show.

**EX068.** That the store manager knew of past collection mistakes Hannah had not heard about.

**EX069.** With a collection code sent by text and checked at the counter.

**EX070.** Media disposal, specifically old till hard drives.

**EX071.** As a monthly thirty-minute review of identity alerts by Hannah.

**EX072.** They were questioned, and two leftovers from an old insurer requirement were retired.

**EX073.** Three: two store staff with leftover promotion rights and one warehouse user with database owner rights from an urgent fix.

**EX074.** Because incorrect definitions would make the checker report false alarms.

**EX075.** Add approved exceptions with expiry dates so temporary rights stay visible.

**EX076.** The stale spreadsheet export held by a marketing agency.

**EX077.** The email fallback, so it needed a second factor.

**EX078.** STRIDE gave breadth, the attack tree gave attacker paths and the risk ratings gave priority.

**EX079.** Because it cannot be verified, so it gives false comfort.

**EX080.** Logic flaws, such as releasing an order without a code.

**EX081.** Code expiry failed because the expiry job was not scheduled in production.

**EX082.** Because monitoring watched shop availability, not price changes.

**EX083.** Because anyone with the same pressure and tools could have made the same mistake.

**EX084.** The new alert caught a mistaken currency conversion before customers saw it.

**EX085.** So tasks are carried by the calendar and survive holidays and staff changes.

**EX086.** A yes to any question about new suppliers, data, boundary crossings or privileged access.

**EX087.** To receive only member numbers and points balances instead of the full member list.

**EX088.** Buyers travelling for suppliers caused many false alarms.

**EX089.** Because the one-hour window missed three of the four planted attacks.

**EX090.** Attackers who sign in from the same country as the user.

**EX091.** Because it has few users and high value, giving lessons before busy stores move.

**EX092.** Anticipate, withstand, recover and adapt.

**EX093.** The second hosting region, with the rehearsed manual order process as the fallback for one season.

**EX094.** As reducing the chance of payment fraud.

**EX095.** The purpose, country-level data, retention, staff notice and a legitimate-interest assessment.

**EX096.** Pre-created limited till accounts activated by a manager on arrival and expiring at season end.

**EX097.** Briefed stores rose by 0.29 more reports per staff member per month than comparison stores.

**EX098.** That report-button use measures willingness to report rather than ability to detect.

**EX099.** A randomised rollout where stores are assigned by lot.

**EX100.** So the preferred option does not influence what is measured.

**EX101.** Option A scored 3.05 and Option B 4.10.

**EX102.** Option B still won, 3.83 to 3.30.

**EX103.** The robots' internal safety systems, which need specialist engineers.

**EX104.** To protect against scope creep and make clear what will not be delivered.

**EX105.** So success is judged by criteria agreed in advance rather than after the results.

**EX106.** Because advice that slows a busy distribution shift will be ignored.

**EX107.** The password manager rollout, because volunteers would not keep using it.

**EX108.** Data classification and least privilege, along with asking who would notice a problem.

**EX109.** Who wrote it, what method, what data and what interests the author has.

**EX110.** They record consensus about good practice but do not measure outcomes.

**EX111.** It is reasonable practice supported by consensus and simulation, with little real-world outcome evidence for small organisations.

**EX112.** The supplier's remote support link, because it used a shared password.

**EX113.** He identified affected deliverables, agreed revised milestones and updated only what changed.

**EX114.** Named accounts with multi-factor authentication and recorded sessions, verified by a test login.

**EX115.** The robot network isolation test, because the robots had not arrived.

**EX116.** No patching plan for robot controllers and no process to revoke vendor access at contract end.

**EX117.** Each was assigned an owner at Fernway with a scheduled action.

**EX118.** He cited only sources he had read.

**EX119.** The identity provider single point of failure.

**EX120.** Treat designs as hypotheses to test and record what is unknown as carefully as what is known.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems and data in this book are synthetic unless a sentence cites a public source.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. Author's page: <https://www.cl.cam.ac.uk/archive/rja14/book.html>
- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Herley, C., & van Oorschot, P. C. (2017). SoK: Science, security and the elusive goal of security as a scientific pursuit. *2017 IEEE Symposium on Security and Privacy*, 99–120. <https://doi.org/10.1109/SP.2017.38>
- International Organization for Standardization. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*. <https://www.iso.org/standard/27001>
- International Organization for Standardization. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-30r1>
- Joint Task Force. (2018). *Risk management framework for information systems and organizations* (NIST SP 800-37 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-37r2>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Ross, R., Pillitteri, V., Graubart, R., Bodeau, D., & McQuaid, R. (2021). *Developing cyber-resilient systems: A systems security engineering approach* (NIST SP 800-160 Vol. 2 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v2r1>
- Ross, R., Winstead, M., & McEvilley, M. (2022). *Engineering trustworthy secure systems* (NIST SP 800-160 Vol. 1 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-160v1r1>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Sherwood, J., Clark, A., & Lynas, D. (2005). *Enterprise security architecture: A business-driven approach* (SABSA). CMP Books.
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- The Open Group. (2016, revised 2022). *Integrating risk and security within a TOGAF enterprise architecture* (TOGAF Series Guide G152). The Open Group.
- Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in software engineering*. Springer. <https://doi.org/10.1007/978-3-642-29044-2>
