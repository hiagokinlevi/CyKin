# Authorized Offensive Security and Red Team: An Engineering Degree Book

- Language: English (`en`); five years; approximately 4,000 hours of planned study.
- Editorial state: **draft**. Chapters 1–50 of 50 have authored teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; offline labs use the Python 3 standard library and their printed outputs were produced by real runs against synthetic data only. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: future security systems engineers who design authorized assessment tooling, measurement and reporting platforms.
- Relation to neighbouring books: the [bachelor's book](../../../../bachelors-4-years/offensive-security-red-team/en/book/MANUSCRIPT.md) is broader; the [technologist book](../../../../technologist-3-years/offensive-security-red-team/en/book/MANUSCRIPT.md) is more implementation-focused. **This book is design-heavy**: requirements, architecture, controls, verification and capstone evidence for authorized red-team platforms.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not a qualification and **no authority to test real systems**. All organizations, people, findings and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, measurement and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Each chapter has learning outcomes, teaching text, a worked example, errors and limits, exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs are deterministic, run offline with `python3 file.py` on synthetic data, and print the results shown under *Expected output*.

### The running example (synthetic): Riverstone Transit

> **Synthetic case — fiction.** **Riverstone Transit** is invented. It runs TrackScope (scope and ROE checker), FindingsDesk (ticket and severity tool), and PulseMap (ATT&CK coverage reporter). *Sam Ito*, engineering intern on the authorized assessment platform team, follows these systems through the course. Every number is invented; all testing happens on isolated copies with synthetic data and written authorization.

### Source policy

Sources were checked on 12 October 2026: [NIST SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); [MITRE ATT&CK](https://attack.mitre.org/); [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide) (2024 Implementation Guide). Albrecht and Jensen (arXiv:2010.06377) critique empty security scores. Legal content is orientation, not advice.

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) model a cumulative quantity in an assessment as an integral of a rate; (2) use a derivative to find when a rate peaks; (3) turn both into a rate limit Sam Ito can defend in the rules of engagement (ROE).

### 1.1 Rates and accumulations in an engagement

Every authorized test produces traffic, and the client cares about two things: how fast it arrives and how much accumulates. If an enumeration job sends requests at rate r(t) requests per second, the total sent between times a and b is the integral ∫ r(t) dt from a to b. A ROE that says "no more than 5 requests per second" limits r(t); one that says "no more than 20,000 requests per day against the ticketing API" limits the integral. They are different constraints and a schedule can satisfy one while breaking the other.

### 1.2 Finding the peak

Suppose TrackScope ramps a scan up and then down, with r(t) = 6t − t² requests per second for 0 ≤ t ≤ 6 minutes (t in minutes, synthetic). The derivative r′(t) = 6 − 2t is zero at t = 3, where r(3) = 9 requests per second. If the ROE ceiling is 5 per second, this schedule breaches it between the two roots of 6t − t² = 5, that is t = 1 and t = 5 minutes. Calculus tells you not just *whether* a plan breaks the limit but *for how long*, which is what the client's operations team asks first.

### 1.3 From total to schedule

The total for that ramp is ∫₀⁶ (6t − t²) dt = [3t² − t³/3]₀⁶ = 108 − 72 = 36 request-minutes per second, i.e. 36 × 60 = 2,160 requests. A flat schedule at 5 per second would need 2,160 / 5 = 432 seconds, 7.2 minutes, to send the same volume without any breach. Engineers prefer the flat schedule because its peak equals its average and is trivial to verify from logs.

> **Synthetic case — Riverstone Transit.** Sam's draft ramp for the fare-gateway test peaked at 9 req/s; the ROE allowed 5. Sam replaced it with a 5 req/s token bucket (see Chapter 36) and attached the integral calculation to the change request.

### 1.4 Errors and limits

Real traffic is bursty, not smooth; a continuous model gives an average-case picture, and the ROE limit must be enforced by a mechanism, not by the calculation. Units cause most mistakes: keep seconds and minutes separate.

Enforcement belongs in the scanner configuration and in a network rate limiter the client can see, so a mistake in the schedule cannot silently exceed the agreed limit. When converting between minutes and seconds, write the units next to every number and check the final figure against a rough estimate. Burstiness means a short spike can break a per-second limit even when the hourly average is fine, so Sam Ito sets both a short-window and a long-window ceiling in the ROE and tests them before the engagement starts.

### Exercises

- **EX001 — Breach window.** For r(t) = 8t − t² req/s (t in minutes, 0–8) and a ceiling of 7 req/s, find the peak and the interval during which the ceiling is breached. Rubric: 3 = peak 16 at t=4 and breach between t=1 and t=7 (6 minutes); 2 = one slip; 1 = peak only; 0 = none.
- **EX002 — Two kinds of limit.** Give one ROE clause that limits a rate and one that limits a total, for the same API, and say which one a log-based check verifies more easily. Rubric: 3 = both clauses with units and justified answer; 2 = clauses without justification; 1 = one clause; 0 = none.
- **EX003 — Flat equivalent.** How long does a flat 4 req/s schedule take to send the 2,160 requests of §1.3? Rubric: 3 = 540 s (9 minutes) with working; 2 = right number, no units; 1 = method only; 0 = none.

### Synthesis

A rate limit and a volume limit are a derivative and an integral of the same curve. Checking both turns a vague promise of "low impact" into numbers the client can audit.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) express scope as sets and predicates; (2) prove a simple property of a scope rule; (3) count the size of a scope so that coverage claims have a denominator.

### 2.1 Scope is a set

Written scope lists what may be tested: in-scope networks I, in-scope ports P and a deny-list D. The set of permitted targets is T = {(h, p) : h ∈ I, h ∉ D, p ∈ P}. Writing scope this way exposes ambiguities a prose ROE hides. "The 10.20.0.0/16 network except the gateway" is the set difference I \ D with D = {10.20.0.1}. "Web services" is not a set until someone lists the ports.

Once targets are pairs of host and port, every proposed action can be checked against the same predicate. Ambiguous phrases such as 'web services' disappear, because the set either contains a port or it does not. The deny-list sits inside the definition of T, so forgetting to apply it is a coding error rather than a judgement call during the test. Sam keeps the written ROE and the machine-readable set in the same change, so they cannot drift apart.

### 2.2 Predicates and proofs

TrackScope implements the predicate allowed(h, p) = inCIDR(h, I) ∧ ¬(h ∈ D) ∧ (p ∈ P). Because every clause is a conjunction, adding a host to D can only shrink T: if (h, p) ∈ T after the change then it was in T before. That monotonicity is worth proving and testing, because the opposite (a change that silently widens scope) is the incident engineers most want to prevent. A unit test checks the property on all pairs drawn from a small synthetic universe.

```python
"""Check proposed engagement targets against a written scope (synthetic)."""
SCOPE_CIDRS = [("10.20.0.0", 16), ("192.168.50.0", 24)]  # inclusive synthetic ranges
SCOPE_PORTS = {22, 80, 443, 8080}
DENY_HOSTS = {"10.20.0.1", "192.168.50.1"}  # out-of-scope infra

def ip_int(s):
    a,b,c,d = map(int, s.split("."))
    return (a<<24)|(b<<16)|(c<<8)|d

def in_cidr(ip, net, bits):
    mask = (0xFFFFFFFF << (32-bits)) & 0xFFFFFFFF
    return (ip_int(ip) & mask) == (ip_int(net) & mask)

def check(host, port):
    reasons = []
    if host in DENY_HOSTS:
        reasons.append("deny-list")
    if not any(in_cidr(host, n, b) for n,b in SCOPE_CIDRS):
        reasons.append("outside-cidr")
    if port not in SCOPE_PORTS:
        reasons.append("port-not-in-scope")
    return ("ALLOW" if not reasons else "DENY"), reasons

tests = [
    ("10.20.1.10", 443),
    ("10.20.0.1", 443),
    ("192.168.50.20", 22),
    ("192.168.50.20", 3389),
    ("8.8.8.8", 80),
    ("192.168.1.10", 80),
]
for h,p in tests:
    v, r = check(h,p)
    print(f"target={h}:{p} decision={v} reasons={','.join(r) or '-'}")
```

Expected output:

```text
target=10.20.1.10:443 decision=ALLOW reasons=-
target=10.20.0.1:443 decision=DENY reasons=deny-list
target=192.168.50.20:22 decision=ALLOW reasons=-
target=192.168.50.20:3389 decision=DENY reasons=port-not-in-scope
target=8.8.8.8:80 decision=DENY reasons=outside-cidr
target=192.168.1.10:80 decision=DENY reasons=outside-cidr
```

### 2.3 Counting the denominator

A /16 holds 2¹⁶ = 65,536 addresses; a /24 holds 256. With four permitted ports and one denied host, |T| = (65,536 − 1 + 256) × 4 = 263,164 host–port pairs. Nobody tests every pair, so coverage must be stated as "pairs examined / |T|" or as a sampled fraction, never as "the network was covered".

> **Synthetic case — Riverstone Transit.** The first ROE draft said "all depot systems". Sam rewrote it as two CIDRs, a port set and a one-host deny-list, and the client's network lead found that one depot CIDR also contained a supplier's kiosk, which was added to D before signing.

### 2.4 Errors and limits

Sets describe intent, not reality: DHCP can move a host into or out of a range during the test, so the predicate must be re-evaluated per action. Overlapping CIDRs double-count if you add sizes naively; use inclusion–exclusion.

Re-evaluating the predicate before each action costs little and catches a host that moved during the day. When two ranges overlap, adding their sizes twice is the common mistake; compute the union instead. A scope file that is correct at kickoff can be wrong by lunchtime if the client renumbers a subnet, which is why TrackScope logs the version of the scope file with every decision.

### Exercises

- **EX004 — Set notation.** Write the permitted-target set for networks 192.168.50.0/24, ports {22, 443} and deny-list {192.168.50.1, 192.168.50.254}. Rubric: 3 = correct set expression and |T| = 508; 2 = expression without count; 1 = partial; 0 = none.
- **EX005 — Monotonicity.** Prove that adding a port to P can only enlarge T, and state which review rule this implies. Rubric: 3 = proof plus "port additions need a second approver"; 2 = proof only; 1 = assertion; 0 = none.
- **EX006 — Lab reading.** In the lab output, why is 192.168.50.20:3389 denied while 192.168.50.20:22 is allowed? Rubric: 3 = port 3389 not in P, host in I and not in D; 2 = reason without the other clauses; 1 = vague; 0 = wrong.

### Synthesis

Treat scope as a predicate over a countable set. It can then be tested and counted, and a change to it can be shown not to widen it.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate signal propagation, bandwidth and latency to what a test can observe; (2) estimate the physical side effects of test traffic; (3) explain why radio and physical-access tests need separate authorization.

### 3.1 Latency has a floor

Signals in fibre travel at about two-thirds of the speed of light, roughly 200,000 km/s, so 1,000 km of fibre adds about 5 ms each way. When TrackScope reports a 40 ms round trip to a depot server 300 km away, about 3 ms is propagation and the rest is queuing, switching and processing. Engineers use this floor to sanity-check timing evidence: a round trip *below* the propagation floor means the measurement or the location assumption is wrong.

If a measured round trip is shorter than light could travel the claimed distance, either the server is closer than believed or the clock is wrong. Sam uses the floor as a check on evidence, not as a location finder: many paths take longer routes, so a high latency proves nothing about distance. For depot links over a few hundred kilometres, a few milliseconds of propagation is normal; tens of milliseconds of processing on a busy fare system is also normal and must not be read as proof of a distant host.

### 3.2 Bandwidth and serialisation

Serialisation time is size divided by link rate. A 1,500-byte frame on a 10 Mb/s depot uplink takes 1,500 × 8 / 10⁷ = 1.2 ms to put on the wire. If an authorized scan sends 2,000 small probes per second at 100 bytes each, it consumes 1.6 Mb/s, 16% of that uplink, which is why low-bandwidth OT and branch links get tighter ROE limits than data-centre networks.

Serialisation time adds to every packet before any processing delay. On a slow uplink, many small probes add up faster than engineers expect, because each probe still carries headers. Sixteen percent of a depot link is already enough to annoy operations and to trigger capacity alarms. Sam therefore sizes scans against the smallest link in scope, not against the data-centre core, and writes the assumed link rate into the ROE so the client can correct it.

### 3.3 Heat, power and physical media

Computation dissipates power as heat. A stress test that keeps an embedded fare validator's CPU at 100% may push it past its thermal envelope in a sealed kiosk; that is a safety issue, not a security finding. Radio is a physical medium shared with people who never signed the ROE: Wi-Fi and Bluetooth assessments transmit into public space and are regulated, so they need explicit written authorization naming frequencies, locations and times.

> **Synthetic case — Riverstone Transit.** A proposed throughput test on the depot uplink would have used 70% of a 10 Mb/s link during the morning dispatch window. Sam moved it to 02:00–04:00 and capped it at 1 Mb/s after computing the serialisation load.

### 3.4 Errors and limits

Back-of-envelope physics gives orders of magnitude; real links have overheads (headers, retransmissions) that add 5–20%. Do not infer geographic location from latency alone; routing paths are rarely straight lines.

Header and retransmission overhead means a calculation that ignores them underestimates load. Using latency to guess location fails when traffic is routed through a distant hub or a VPN. Sam states assumptions next to every estimate and treats a mismatch with measured values as a signal to revise the model, not as a finding about the target.

### Exercises

- **EX007 — Propagation floor.** A report claims a 2 ms round trip between sites 800 km apart over fibre. Is it plausible? Rubric: 3 = floor ≈ 8 ms round trip, so implausible, with a likely cause (cache, wrong site, local proxy); 2 = calculation only; 1 = guess; 0 = none.
- **EX008 — Link share.** What fraction of a 2 Mb/s link do 500 probes per second of 120 bytes use? Rubric: 3 = 0.48 Mb/s = 24%; 2 = one unit slip; 1 = method only; 0 = none.
- **EX009 — Radio authorization.** List four fields a written authorization for a Wi-Fi assessment must contain beyond a normal network ROE. Rubric: 3 = frequencies/bands, physical locations, times, and a rule for third-party devices/data; 2 = three; 1 = one or two; 0 = none.

### Synthesis

Physics sets floors and budgets. Using them catches impossible evidence and keeps test traffic within what fragile links and devices can take.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small, testable functions for assessment bookkeeping; (2) choose data structures that make wrong states hard to represent; (3) write a unit test before trusting a tool's output.

### 4.1 Functions that return decisions

Assessment tooling is mostly bookkeeping: is this target allowed, which finding is a duplicate, how old is this ticket. Each question should be a pure function with explicit inputs and a return value, such as `allowed(host, port, scope) -> (bool, reason)`. Returning the *reason* as well as the decision makes logs useful: "DENY outside-cidr" tells the reviewer which rule fired. Avoid global state; a function that reads a hidden global scope file cannot be tested against a synthetic scope.

A pure function can be called from a unit test with a fake scope and from the live tool with the real one, and both paths share the same logic. Returning a reason string turns every denial into an explanation the engagement log can store. Global state is the enemy of that pattern: if the scope is read from a file inside the function, a test cannot inject a synthetic scope without touching the filesystem. Sam keeps scope as an argument everywhere TrackScope decides allow or deny.

### 4.2 Data structures that resist errors

Store ports as a `set` of integers, not a comma-separated string: membership is exact and "443" cannot match "4430". Store CIDRs as parsed network objects (the standard `ipaddress` module) rather than strings, because string prefix matching thinks 10.2.0.5 is inside "10.20". Store findings as dictionaries with a fixed schema and validate required keys on creation.

Wrong types create silent bugs that look like scope mistakes. A string of ports invites a substring match; a set of integers does not. String prefix checks on addresses are a classic trap, which is why the standard library's network objects exist. Validating finding records on creation catches a missing ticket reference before the report is written, when fixing it still costs seconds rather than an awkward correction to the client.

### 4.3 Test first

Before using a scope checker on a client network, write five tests on synthetic data: one allow, one deny for each rule, and one boundary case (the first and last address in a range). The lab in Chapter 2 is exactly such a table of decisions; reproducing it in a unit test means a later refactor that breaks the deny-list is caught before it reaches a real engagement.

```python
import ipaddress
def in_scope(h, nets):
    a = ipaddress.ip_address(h)
    return any(a in ipaddress.ip_network(n) for n in nets)
assert in_scope("10.20.255.255", ["10.20.0.0/16"])
assert not in_scope("10.2.0.5", ["10.20.0.0/16"])
print("scope tests passed")
```

> **Synthetic case — Riverstone Transit.** An intern script matched scope with `host.startswith("10.2")`. Sam's boundary test showed it accepted 10.200.0.0/16, a partner network. The fix used `ipaddress` and the test now runs in CI.

### 4.4 Errors and limits

Tests prove behaviour on the cases you wrote, not on all inputs. Keep test data synthetic; never paste a client's real host list into a public repository.

A passing suite means the written cases behave; an untested boundary can still be wrong. Synthetic hosts keep client networks out of git history and out of student machines. When a new rule is added to the scope checker, Sam adds a test for it in the same change, so the suite and the rules stay aligned.

### Exercises

- **EX010 — Bug hunt.** Explain why `"443" in "8443,22"` is true in Python and how to fix the port check. Rubric: 3 = substring semantics explained and set-of-int fix; 2 = fix only; 1 = vague; 0 = none.
- **EX011 — Boundary tests.** Give the two boundary addresses to test for 192.168.50.0/24 and the expected result for 192.168.51.0. Rubric: 3 = .0 and .255 inside, 192.168.51.0 outside; 2 = one missing; 1 = partial; 0 = none.
- **EX012 — Reason codes.** Why should a scope function return a reason string and not only a boolean? Rubric: 3 = audit/log value and test precision with an example; 2 = one reason; 1 = vague; 0 = none.

### Synthesis

Small pure functions, exact data types and tests written on synthetic data are the cheapest scope-safety mechanism an engineer has.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write a finding that a non-specialist can act on without exploit detail; (2) structure a short engineering report; (3) state uncertainty plainly.

### 5.1 The reader decides

A red-team report is read by an engineer who must fix something and a manager who must fund it. Neither needs a recipe. A finding needs: a title stating the weakness and asset; the affected scope; the evidence (what was observed, with time and ticket reference); the impact in business terms; the recommended fix; and how the fix will be verified. NIST SP 800-115 treats reporting as part of the assessment, not an afterthought.

Putting the fix and its verification next to the evidence means the engineer who must act has everything on one page. Business impact answers the manager's funding question without technical jargon: delayed trains, exposed rider data or a ticket forgery risk each land differently. Leaving out a working recipe is not vagueness; it is a deliberate choice so the report can be forwarded inside the client without becoming a how-to. NIST SP 800-115's place for reporting reminds teams that an unreported finding helps nobody.

### 5.2 Write the claim at the right strength

"We compromised the domain" is a headline. "Within the authorized window, a service account in the lab directory had domain-administrator rights; we confirmed the group membership read-only and did not use it" is a finding. The second states what was done, what was not done and on which scope, and the reader can verify it.

The weaker, careful claim is stronger as engineering because another team can re-check it. Stating what was not done closes the gap where a reader invents a worse scenario than occurred. Naming the scope, such as the lab directory rather than production, stops a finding being applied to the wrong system. Sam reads each draft aloud and asks whether every noun points to something in the evidence store.

### 5.3 Report structure

A short engineering report has: an executive summary (three sentences: what was tested, the most important result, the one decision needed); scope and method with ROE version; findings ordered by priority; limitations (what was out of scope or not reached); and an appendix with evidence hashes. Use tables for findings, prose for reasoning.

```python
"""Score synthetic findings for report priority (no exploit details)."""
# impact 0-3, exploitability 0-3, exposure 0-3  -> priority
findings = [
    ("SYN-001", "default admin password on staging web UI", 3, 3, 2),
    ("SYN-002", "missing security headers on public site", 1, 1, 3),
    ("SYN-003", "outdated TLS on internal admin port", 2, 2, 1),
    ("SYN-004", "verbose error messages disclose paths", 1, 2, 2),
    ("SYN-005", "service account with domain admin in lab AD", 3, 2, 1),
]

def priority(impact, exploitability, exposure):
    score = impact*4 + exploitability*2 + exposure
    if score >= 16: return "critical", score
    if score >= 11: return "high", score
    if score >= 7: return "medium", score
    return "low", score

for fid, title, i, e, x in findings:
    p, s = priority(i, e, x)
    print(f"{fid} priority={p:8} score={s:2} impact={i} exploitability={e} exposure={x} :: {title}")
```

Expected output:

```text
SYN-001 priority=critical score=20 impact=3 exploitability=3 exposure=2 :: default admin password on staging web UI
SYN-002 priority=medium   score= 9 impact=1 exploitability=1 exposure=3 :: missing security headers on public site
SYN-003 priority=high     score=13 impact=2 exploitability=2 exposure=1 :: outdated TLS on internal admin port
SYN-004 priority=medium   score=10 impact=1 exploitability=2 exposure=2 :: verbose error messages disclose paths
SYN-005 priority=critical score=17 impact=3 exploitability=2 exposure=1 :: service account with domain admin in lab AD
```

> **Synthetic case — Riverstone Transit.** Sam's first draft of SYN-001 said "the staging UI is totally owned". The revised finding reads: "Staging admin UI (10.20.1.10:443) accepts the vendor default password; observed 10:45, ticket FD-118; an attacker on the corporate network could change fare tables in staging; fix: rotate and enforce unique credentials; verify by a re-test login failure."

### 5.4 Errors and limits

Avoid adjectives that cannot be checked ("trivial", "catastrophic"). Do not include working payloads, credentials or step-by-step instructions in reports; reference the evidence store instead.

Unchecked adjectives invite argument and hide the real evidence. Working payloads and credentials belong in a controlled store with access logs, not in a PDF that will be mailed around. When a reader needs more detail to verify a fix, Sam points them at the ticket and the evidence hash rather than pasting secrets into the report body.

### Exercises

- **EX013 — Rewrite.** Rewrite "The VPN is wide open lol" as a finding title and one-sentence evidence line. Rubric: 3 = asset, weakness, observation time/ref, no exploit detail; 2 = one element missing; 1 = still vague; 0 = unchanged.
- **EX014 — Executive summary.** Write a three-sentence summary for the five lab findings. Rubric: 3 = scope, the two critical items, one decision requested; 2 = missing decision; 1 = list only; 0 = none.
- **EX015 — Limitations.** Name two limitations a report on this engagement must state. Rubric: 3 = two specific limits (e.g. hosts not reached, time window, no social engineering) with effect on conclusions; 2 = two without effect; 1 = one; 0 = none.

### Synthesis

A good finding is specific, verifiable and safe to circulate. Writing it that way is part of the engineering, not decoration.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use series and accumulation to reason about repeated probes; (2) apply a simple differential model to a remediation backlog; (3) decide when a continuous model is good enough for a ROE debate.

### 6.1 Geometric series and retries

If each attempt to upload evidence succeeds with probability p = 0.8 independently, the chance of succeeding within k tries is 1 − (1 − p)^k. That is a finite geometric series. With k = 3, 1 − 0.2³ = 0.992. Retries raise the success rate, but they also multiply traffic: expected attempts until success is 1/p = 1.25, so a 1,000-upload batch expects 1,250 requests. The ROE must count the retries, not only the logical uploads.

```python
"""Reliability of a synthetic evidence-upload step with retries (deterministic)."""
import random
random.seed(7)
P_FAIL = 0.2
def upload_attempts(max_tries):
    for t in range(1, max_tries + 1):
        if random.random() > P_FAIL:
            return True, t
    return False, max_tries
for tries in (1, 2, 3, 5):
    random.seed(7)
    ok = sum(upload_attempts(tries)[0] for _ in range(1000))
    print(f"max_tries={tries} success={ok}/1000 theory={1-P_FAIL**tries:.4f}")
```

Expected output:

```text
max_tries=1 success=784/1000 theory=0.8000
max_tries=2 success=949/1000 theory=0.9600
max_tries=3 success=988/1000 theory=0.9920
max_tries=5 success=1000/1000 theory=0.9997
```

Counting only logical uploads understates load by the retry factor. With p equal to 0.8, every thousand logical uploads mean about twelve hundred and fifty attempts on average, which is what the client's rate limiter will see. The lab's seed keeps the demonstration stable across machines; production uses the same formula with measured failure rates. Sam writes the expected attempt count into the ROE volume budget before the engagement.

### 6.2 Differential model of a backlog

Let B(t) be open findings. Findings arrive at rate a and are closed at rate c when staffed. Then B′(t) ≈ a − c. If a = 4/day and c = 6/day, the backlog falls by about 2 per day; starting from 30, it reaches zero in 15 days. If arrivals jump to 8/day (a campaign week) while staffing stays at 6, the backlog grows. The model is crude — it ignores priority — but it makes the staffing decision quantitative.

The sign of a minus c tells the story at a glance: negative and the pile shrinks, positive and it grows. Priority still matters in real queues, so Sam uses the model to ask for staffing, not to promise a calendar date. When a campaign week doubles arrivals, the same model shows how many extra closers are needed to stay level. Plotting B(t) over a month makes the effect visible to managers who will not read the equation.

### 6.3 When continuous is enough

ROE debates often need an order of magnitude, not a closed form. "Will a 5 req/s scan for 30 minutes produce about 9,000 requests?" Yes: 5 × 1,800 = 9,000. Reserve exact calculus for schedules with peaks (§1) and for models the client will audit.

> **Synthetic case — Riverstone Transit.** FindingsDesk showed a backlog of 28 medium findings with two remediations per day. Sam's B′ model predicted 14 days to clear if no new arrivals; the manager funded a third engineer for that fortnight.

Order-of-magnitude arithmetic settles most ROE debates in minutes. Exact schedules with peaks need the fuller treatment from the first calculus chapter, and those are the ones Sam brings to a client who will audit the numbers. For a flat scan, multiplying rate by duration is enough, and writing the product next to the volume limit shows compliance at a glance. If the product sits near the limit, he switches to the exact schedule check rather than hoping bursts stay small.

### 6.4 Errors and limits

Independence of retries fails when the failure is systematic (a broken endpoint). Backlog models ignore priority and SLA; use them as a conversation starter, not as a forecast the board will quote.

A broken endpoint fails every try, so multiplying attempts does not raise the success rate and only adds load. Staffing models that ignore severity will clear easy tickets while critical ones age. Sam labels every model with its assumptions and refuses to let a backlog chart be quoted as a delivery date.

### 6.3b Choosing a retry cap from the series

The geometric series gives the chance that every attempt fails as p to the power n. Sam uses it backwards: TrackScope's evidence upload must succeed 99% of the time, and synthetic runs show a 20% failure rate per attempt, so three attempts (0.8%) meet the goal while two (4%) do not. He writes the derivation into the design note so a reviewer can check the cap without rerunning experiments.

Working backwards from a reliability goal turns a taste decision into a short derivation. Three attempts leave under one percent failure when each try fails one time in five, which matches the lab. Putting the derivation in the design note means a later engineer can change the failure rate and recompute the cap without guessing why three was chosen. Sam re-runs the synthetic check whenever the upload path changes.

### Exercises

- **EX016 — Retry traffic.** With p = 0.7 and a batch of 500 uploads, expected attempts until each succeeds once? Rubric: 3 = 500/0.7 ≈ 714 with working; 2 = one slip; 1 = formula only; 0 = none.
- **EX017 — Backlog.** B(0) = 40, a = 3/day, c = 5/day. When does B reach 0? Rubric: 3 = 20 days; 2 = method, wrong arithmetic; 1 = qualitative; 0 = none.
- **EX018 — Lab reading.** From the lab, by how many percentage points does k = 3 improve on k = 1 at p = 0.8? Rubric: 3 = 98.8 − 80.0 ≈ 18.8 points (theory) or the empirical gap; 2 = one number; 1 = vague; 0 = wrong.

### Synthesis

Series and rates turn "try again" and "hire someone" into numbers that fit in a ROE or a staffing request.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) report a rate with an interval, not a bare percentage; (2) apply Bayes' rule to alarm precision; (3) refuse a ranking that the sample cannot support.

### 7.1 Rates and Wilson intervals

Three successes in twenty trials is 15%. A Wilson 95% interval for that is about 5%–36%. You can say the rate is probably not zero and probably below 40%; you cannot say it is better than a defence that scored 20/100 (20%). Larger n shrinks the interval: 300/2,000 is still 15% but about 13.5%–16.6%. Albrecht and Jensen warn against empty single scores; an interval is the cheapest honesty.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Expected output:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

The same fifteen percent means very different things at n equals twenty and at n equals two thousand. An interval makes that visible without a statistics lecture. Sam reports the interval next to every attack-success rate so a defence is not crowned on a tiny sample. The lab's seed variation and paired bootstrap give two further checks: stability across seeds and a difference that may include zero.

### 7.2 Base rates and precision

A detector with 95% true-positive rate and 5% false-positive rate looks excellent until the base rate of the bad class is 0.1%. Then almost every alert is a false positive (precision ≈ 1.9%). Bayes' rule: precision = TPR·π / (TPR·π + FPR·(1−π)). PulseMap must show precision at the client's base rate, not only TPR.

```python
"""Lab B: base rates and alarm precision (Bayes' rule).
A detector for malicious prompts with given true- and false-positive rates
is applied to traffic with different shares of malicious prompts."""
for tpr, fpr in ((0.95, 0.05), (0.95, 0.01), (0.80, 0.001)):
    for prev in (0.10, 0.01, 0.001):
        tp = tpr * prev; fp = fpr * (1 - prev)
        prec = tp / (tp + fp)
        per_10k = round(10000 * (tp + fp))
        print(f"tpr={tpr:.2f} fpr={fpr:.3f} prevalence={prev:.3f} precision={prec:.3f} alerts_per_10k={per_10k}")
```

Expected output:

```text
tpr=0.95 fpr=0.050 prevalence=0.100 precision=0.679 alerts_per_10k=1400
tpr=0.95 fpr=0.050 prevalence=0.010 precision=0.161 alerts_per_10k=590
tpr=0.95 fpr=0.050 prevalence=0.001 precision=0.019 alerts_per_10k=509
tpr=0.95 fpr=0.010 prevalence=0.100 precision=0.913 alerts_per_10k=1040
tpr=0.95 fpr=0.010 prevalence=0.010 precision=0.490 alerts_per_10k=194
tpr=0.95 fpr=0.010 prevalence=0.001 precision=0.087 alerts_per_10k=109
tpr=0.80 fpr=0.001 prevalence=0.100 precision=0.989 alerts_per_10k=809
tpr=0.80 fpr=0.001 prevalence=0.010 precision=0.890 alerts_per_10k=90
tpr=0.80 fpr=0.001 prevalence=0.001 precision=0.445 alerts_per_10k=18
```

Precision collapses when the bad class is rare, which is exactly PulseMap's setting. A dashboard that shows only true-positive rate will look excellent while flooding analysts with false alarms. Computing precision at the client's measured prevalence, as the lab table does, is what Sam puts in the report. If prevalence is unknown, he shows a small table across a range rather than picking a flattering number.

### 7.3 Ranking defences

Two defences with overlapping intervals are not ranked. Prefer a paired design on the same prompts and a bootstrap of the difference, as the lab shows. If the interval for the difference includes zero, report "no significant difference in this sample", not a winner.

> **Synthetic case — Riverstone Transit.** A vendor claimed "our filter is 99% effective". Sam asked for the base rate and sample size; neither was in the brochure. The pilot used 200 synthetic prompts at a 1% attack share and measured precision ≈ 16%.

### 7.4 Errors and limits

Independence of trials fails when prompts share a template. Intervals assume a fixed process; changing the model mid-test voids them. Never invent a p-value for a table you did not test.

Shared templates make trials dependent, so intervals that assume independence are too narrow. Changing the model mid-test mixes two processes and voids the sample. Sam never attaches a significance claim to a table that was not tested for one, and he restarts the sample when the defence under test changes.

### 7.3b Reporting uncertainty to non-statisticians

A detection rate of 7 out of 10 and a rate of 700 out of 1,000 print the same percentage but deserve very different confidence. When Sam reports PulseMap coverage to the Riverstone Transit security manager, he gives the count, the interval and one plain sentence: "we saw seven of ten test events; the true rate could plausibly be anywhere from about 40% to 90%." Managers then ask for more trials instead of treating a small sample as a fact, and the ranking of defences waits until intervals stop overlapping.

### Exercises

- **EX019 — Interval.** State what you can claim from 8/40 successes at 95%. Rubric: 3 = Wilson ≈ 10.5%–34.5% (or Clopper–Pearson), cannot rank vs 25%; 2 = interval only; 1 = point estimate; 0 = wrong.
- **EX020 — Precision.** Detector TPR 0.9, FPR 0.02, π = 0.005. Precision? Rubric: 3 ≈ 0.184 with working; 2 = one slip; 1 = formula; 0 = none.
- **EX021 — Ranking refusal.** Two filters score 12/100 and 18/100. Write the sentence that refuses a ranking. Rubric: 3 = cites overlapping uncertainty / need for paired design; 2 = vague caution; 1 = picks a winner; 0 = none.

### Synthesis

Statistics is the language for not overclaiming. Rates with intervals and precision at the real base rate keep PulseMap honest.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) map privilege levels to what an authorized test may observe; (2) explain why timing and cache side channels need special ROE clauses; (3) design an evidence path that does not require kernel privileges.

### 8.1 Privilege and observability

User mode sees process memory and system calls it is allowed; kernel mode sees devices and page tables; a hypervisor sees guests. An authorized engagement that stays in user mode cannot claim "we ruled out a kernel rootkit". State the privilege level of each observation in the evidence package. TrackScope should record the account and role used for every action.

A finding is only as strong as the vantage point that produced it. User-mode evidence cannot rule out threats that live below it, and claiming otherwise oversells the engagement. Recording the account and role next to each action lets a reviewer see whether a later claim matches the access used. TrackScope refuses to store an observation without that field.

### 8.2 Side channels are physical

Cache and timing side channels measure microarchitectural state. They are research techniques, noisy, and often out of scope for commercial assessments. If they are in scope, the ROE must name the platforms, forbid production traffic, and require a stop condition if latency to users rises. Do not treat a student lab on a laptop as evidence about a server.

These techniques measure shared hardware state and can disturb production latency, which is why they need their own ROE clauses. A laptop lab says nothing about a server's cache behaviour under load. When side channels are out of scope, Sam states that limit in the report so readers do not assume they were tried. Stop conditions protect users who never agreed to be part of the experiment.

### 8.3 Evidence without root

Most durable evidence for an authorized assessment is logs, configuration reads and application responses — all available to a suitably authorized user account. Prefer that path: it is safer, easier to revoke after the engagement, and sufficient for findings about authentication, authorization and exposure.

> **Synthetic case — Riverstone Transit.** A proposed "full disk image" of a fare validator needed root and would take the device offline. Sam replaced it with a configuration export and an application-level read of the account list, both authorized under the existing ROE.

### 8.4 Errors and limits

Architecture diagrams in marketing decks omit shared caches and management planes. Verify the actual platform before promising a privilege level in the ROE.

Marketing diagrams often hide management interfaces and shared hardware. Sam confirms the real platform with the client before the ROE promises a privilege level. If the platform cannot be confirmed, the engagement stays at the least privilege that is known to exist, and the report states that limit so readers do not invent a stronger vantage point.

### 8.3b Privilege in tickets

FindingsDesk should store `privilege_used` as an enum (user, admin-local, admin-domain, hypervisor, out-of-band). Sorting and SLA logic can then treat hypervisor findings differently from user-mode config reads. Without the field, two findings that look similar in title may have been obtained under radically different authorization, and the re-test plan will be wrong.

An enum stops free-text drift such as 'admin' meaning local on one ticket and domain on another. SLA clocks can then give hypervisor findings a different path, because verifying them needs different access and different stop conditions. Re-test plans read the field so the re-tester brings the right authorization. FindingsDesk rejects a ticket that omits it.

### Exercises

- **EX022 — Privilege map.** List three observations possible as a standard user and three that need elevated privileges. Rubric: 3 = six concrete items mapped correctly; 2 = four; 1 = vague; 0 = none.
- **EX023 — Side-channel ROE.** Write two ROE clauses for an authorized cache-timing study on a spare lab host. Rubric: 3 = platform named, production excluded, stop condition; 2 = two of three; 1 = one; 0 = none.
- **EX024 — Evidence path.** Propose an evidence path for "default admin password on staging UI" that does not need root. Rubric: 3 = login attempt under ROE, screenshot/log, ticket, no credential left behind; 2 = missing one; 1 = vague; 0 = root required.

### Synthesis

Say what privilege you used. Prefer user-level evidence. Treat side channels as special, not as a default tool.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) design a finding schema that forbids exploit recipes; (2) implement idempotent updates; (3) use property tests for scope rules.

### 9.1 Schemas without payloads

FindingsDesk stores title, asset, weakness class, evidence reference, impact, status and timestamps. It must not store a working exploit, a live credential or a step-by-step attack. Schema validation rejects fields named `payload`, `password` or `shell`. Evidence lives in a sealed store referenced by hash (Chapter 48).

Rejecting those field names at the door stops a well-meaning engineer pasting a password into a ticket during a busy close-out. Evidence by hash means the ticket stays shareable while the sealed store stays locked. Sam reviews every new column proposal against the same rule: if it could hold a recipe or a secret, it does not belong in FindingsDesk.

### 9.2 Idempotent updates

Closing a finding twice must leave it closed; attaching the same evidence hash twice must leave one attachment. Idempotency lets retries (Chapter 6) be safe. Use a stable finding id and treat create-or-update as a single operation keyed by that id.

```python
"""Deduplicate synthetic findings by a stable fingerprint (asset, weakness class, location)."""
import hashlib
raw = [
    ("web-01", "missing-header", "/login"),
    ("web-01", "missing-header", "/login"),
    ("web-01", "missing-header", "/account"),
    ("web-02", "default-credential", "admin-ui"),
    ("web-02", "default-credential", "admin-ui"),
    ("db-01", "weak-tls", "5432"),
]
seen = {}
for asset, cls, loc in raw:
    fp = hashlib.sha256(f"{asset}|{cls}|{loc}".encode()).hexdigest()[:10]
    seen.setdefault(fp, [asset, cls, loc, 0])[3] += 1
print(f"raw={len(raw)} unique={len(seen)}")
for fp, (a, c, l, n) in sorted(seen.items(), key=lambda x: x[1]):
    print(f"{fp} {a:7} {c:19} {l:9} occurrences={n}")
```

Expected output:

```text
raw=6 unique=4
f9bb6de442 db-01   weak-tls            5432      occurrences=1
66fb6f1d56 web-01  missing-header      /account  occurrences=1
c4bfba3b72 web-01  missing-header      /login    occurrences=2
296a3331f0 web-02  default-credential  admin-ui  occurrences=2
```

Retries are normal when uploads fail, and without idempotency each retry would reopen work or create duplicate tickets. A stable id turns create and update into the same path, so the second call finds the existing row. The lab's fingerprint collapses six raw rows to four unique findings, which is what remediation owners want to see.

### 9.3 Property tests

Beyond example tests, state a property: "for every host in the deny-list and every port, allowed is False". Generate dozens of synthetic hosts and assert the property. Property tests catch the bug where a deny-list entry is ignored for ports not in a hard-coded list.

> **Synthetic case — Riverstone Transit.** Deduplicating six raw rows left four unique findings; the two duplicates were the same missing header on /login reported by two scanners. Sam made the fingerprint (asset, weakness, location) the idempotency key.

### 9.4 Errors and limits

Schemas drift; version them. Property tests are only as good as the generator; include known edge cases by hand.

A schema without a version field forces clients to guess which fields exist. Generators that never emit the last address in a range will never catch a bug there. Sam keeps a small hand-written table of nasty cases next to the property suite and runs both on every change. A generator bug is treated like a product bug: fix it before the next engagement.

### 9.2b Migration without downtime

When the finding schema gains a required field, deploy a two-phase change: first accept and persist the field as optional while backfilling; then flip the validator to required. Engagements mid-window must not break because a mobile client is one version behind. Publish the schema version in API responses so clients can refuse to write when incompatible.

Two-phase changes keep mid-engagement clients writing safely. Backfill fills old rows before the field becomes required, so validators do not reject historical tickets. Publishing the schema version lets a mobile client refuse an incompatible write instead of corrupting a finding. Sam rehearses the flip on a staging copy with a live engagement fixture before touching production.

### 9.1b Idempotency keys from fingerprints

When two scanners report the same weakness, compute the fingerprint first and use it to mint or look up the finding id before insert. Humans still confirm merges when fingerprints collide across different root causes (same header missing on two unrelated apps). Log the scanner ids as evidence references, not as separate findings, so remediation tracks one ticket.

Scanners disagree on wording but often agree on asset, class and location, which is enough for a fingerprint. Collisions across unrelated apps are rare and need a human merge, which is cheaper than dozens of duplicate tickets. Storing scanner ids as evidence keeps provenance without multiplying the backlog. Sam shows the fingerprint in the ticket so owners can see why two alerts became one.

### Exercises

- **EX025 — Schema reject.** Write a validation rule that rejects a finding containing a field whose name matches `(?i)payload|password|passwd|shell`. Rubric: 3 = rule plus a failing example; 2 = rule only; 1 = idea; 0 = none.
- **EX026 — Fingerprint.** From the lab, why do two /login rows collapse and two /account rows not? Rubric: 3 = same fingerprint vs different location; 2 = "same finding"; 1 = vague; 0 = wrong.
- **EX027 — Property.** State one property of `allowed` that must hold after any deny-list addition. Rubric: 3 = monotonic shrink / every deny host always denied; 2 = informal; 1 = wrong property; 0 = none.

### Synthesis

Schemas, idempotency and properties make assessment software boring in the good sense: predictable under retry and review.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) refuse dual-use and out-of-scope requests; (2) apply stop conditions without waiting for a meeting; (3) document consent and authorization so a review can reconstruct them.

### 10.1 Authorization is not enthusiasm

A manager saying "go ahead" in chat is not written authorization. NIST SP 800-115 and PTES expect a signed scope, methods, dates, limits, contacts and stop conditions. Without that document, the engineer stops. Enthusiasm from a single stakeholder who does not own the asset is a common path to unauthorized testing.

Chat messages vanish, lack scope detail and rarely name stop conditions. A signed document can be shown months later when someone asks why a host was touched. Stopping without that document is not stubbornness; it is the only move that keeps the engineer and the client inside the law. Sam keeps the signed ROE hash in TrackScope next to every run.

### 10.2 Dual use and teaching

This book teaches scoping, measurement and reporting. It does not teach exploit development, weaponised payloads or bypass recipes. When a peer asks for "just the PoC", the answer is the finding description and the evidence reference, not a working attack. Publishing student work that contains live techniques against real products is a disclosure decision with vendors and law, not a homework upload.

The refusal protects classmates, future employers and vendors who never agreed to be homework targets. A finding description plus an evidence reference lets a peer learn what was wrong without receiving a ready-made attack. When coursework might touch a real product, Sam routes it through the same disclosure path a professional engagement would use. Course labs stay on synthetic systems for that reason.

### 10.3 Stop conditions

Stop conditions are pre-agreed triggers: probing a deny-listed host, latency above a threshold, a safety alarm, or a request from the client contact. When a trigger fires, stop first, then notify. TrackScope should enforce hard denies in software so "I forgot" is not a failure mode.

```python
"""Evaluate proposed actions against synthetic rules of engagement."""
ROE = {
    "hours": ("09:00", "17:00"),
    "deny_actions": {"denial-of-service", "phishing-staff", "exfiltrate-real-data"},
    "require_approval": {"password-spray-lab", "privilege-escalation-lab"},
    "max_concurrency": 5,
}
proposals = [
    ("service-enum", "10:30", 3, False),
    ("denial-of-service", "10:30", 1, False),
    ("password-spray-lab", "10:30", 2, False),
    ("password-spray-lab", "10:30", 2, True),
    ("service-enum", "18:00", 2, False),
    ("service-enum", "11:00", 20, False),
]

def ok_time(t):
    return ROE["hours"][0] <= t <= ROE["hours"][1]

for action, when, conc, approved in proposals:
    reasons=[]
    if action in ROE["deny_actions"]: reasons.append("deny-action")
    if action in ROE["require_approval"] and not approved: reasons.append("needs-approval")
    if not ok_time(when): reasons.append("outside-hours")
    if conc > ROE["max_concurrency"]: reasons.append("concurrency")
    print(f"action={action:20} when={when} conc={conc:2} approved={approved} -> {'ALLOW' if not reasons else 'DENY'} {','.join(reasons) or '-'}")
```

Expected output:

```text
action=service-enum         when=10:30 conc= 3 approved=False -> ALLOW -
action=denial-of-service    when=10:30 conc= 1 approved=False -> DENY deny-action
action=password-spray-lab   when=10:30 conc= 2 approved=False -> DENY needs-approval
action=password-spray-lab   when=10:30 conc= 2 approved=True -> ALLOW -
action=service-enum         when=18:00 conc= 2 approved=False -> DENY outside-hours
action=service-enum         when=11:00 conc=20 approved=False -> DENY concurrency
```

> **Synthetic case — Riverstone Transit.** At 11:10 the scan touched 10.20.0.1 (deny-listed). TrackScope denied further actions; Sam escalated; the client confirmed. Resume required an updated ROE line, not a verbal "it's fine".

The lab shows denies for banned actions, missing approval, wrong hours and excess concurrency. Software enforcement means the stop happens even if the human is tired or distracted. Notify after stop, not before, so the harmful action does not continue while someone looks for a meeting slot. Sam tests the deny path in staging with a deliberate banned action before each engagement.

### 10.4 Errors and limits

Ethics is not a chapter you finish; it is a constraint on every later chapter. Legal text here is orientation, not advice — consult counsel for real engagements.

Later chapters on tools and methods inherit these limits; none of them override a missing ROE. Orientation text cannot replace counsel when a real contract is on the table. Sam escalates legal questions instead of inventing answers from a textbook paragraph, and he revisits consent when scope changes mid-engagement, before any new action runs.

### 10.3b Dual control for dangerous verbs

Actions that change authorization — publishing a new ScopeVersion, disabling a stop condition, exporting a sealed dossier — require two authenticated people or a time-delayed single control with a cancel window. Engineering convenience is not an argument against dual control when the blast radius is the client's estate.

One tired engineer should not be able to widen scope for an entire estate. A second person, or a delay that allows cancel, turns a mistake into a recoverable event. Publishing a new ScopeVersion and exporting a sealed dossier both change who can see what, which is why they sit on the dual-control list. Sam logs both approvers on every such action.

### Exercises

- **EX028 — Refuse.** Write a two-sentence refusal to a request for a working exploit against a vendor product for a graded assignment. Rubric: 3 = refuses, offers allowed alternative (finding text / synthetic lab), cites safety; 2 = refuses without alternative; 1 = vague; 0 = provides exploit.
- **EX029 — Stop.** From the lab, which actions are denied and why? Rubric: 3 = DoS always; password-spray without approval; outside hours; concurrency; 2 = three; 1 = one; 0 = wrong.
- **EX030 — Authorization fields.** List six fields a signed ROE must contain. Rubric: 3 = systems, methods, dates, rate/data limits, contacts, stop conditions (or equivalent six); 2 = four; 1 = two; 0 = none.

### Synthesis

Written permission, stop conditions and a refusal habit are safety engineering, not bureaucracy.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) describe what an authorized observer can learn from each OSI layer without attacking it; (2) define port and protocol scope precisely; (3) interpret a deny as a successful control, not a failed test.

### 11.1 Layers as observation points

Link-layer captures need access to a segment; network-layer routing data need a vantage; application-layer evidence often needs credentials. An assessment that only has application credentials should not claim link-layer visibility. State the vantage in the method section.

Credentials for an app say nothing about frames on the wire. Claiming a broader vantage than you held invents coverage. Naming the layer in the method write-up lets a reviewer match each finding to what could actually be seen. Sam refuses to file link-layer claims when the engagement only held an application account.

### 11.2 Ports are not services

Port 443 often means TLS and HTTPS, but it can carry other protocols. Scope that says "web ports" must list numbers and, if needed, expected application protocols. A finding that "HTTPS was open" is incomplete without the certificate subject, auth method and whether the service was the expected one.

Listing port numbers removes the fuzzy phrase 'web ports' from the ROE. Confirming the certificate subject and auth method stops a finding that mistakes a different service on 443 for the expected portal. Sam's notes always include what protocol was observed, not only that the port answered.

### 11.3 Denies are data

A closed port, a refused TCP handshake or a WAF block is evidence that a control worked for that probe. Report it as coverage of a planned check, not as a failure to "get in". PulseMap's covered/planned-not-seen distinction (Chapter 29) depends on this.

```python
"""Rank synthetic assets for authorized engagement scoping."""
assets = [
    ("public-web-portal", 3, 3, 3),      # exposure, data_sensitivity, blast_radius 1-3
    ("staging-admin-ui", 2, 3, 2),
    ("corp-vpn-edge", 3, 2, 3),
    ("internal-wiki", 1, 2, 1),
    ("printer-fleet", 2, 1, 1),
    ("lab-jump-host", 1, 1, 2),
]
print(f"{'asset':20} score exposure data blast")
for name, e, d, b in sorted(assets, key=lambda x: -(x[1]+x[2]+x[3])):
    print(f"{name:20} {e+d+b:5} {e:8} {d:4} {b:5}")
```

Expected output:

```text
asset                score exposure data blast
public-web-portal        9        3    3     3
corp-vpn-edge            8        3    2     3
staging-admin-ui         7        2    3     2
internal-wiki            4        1    2     1
printer-fleet            4        2    1     1
lab-jump-host            4        1    1     2
```

> **Synthetic case — Riverstone Transit.** The inventory ranked public-web-portal highest (score 9). Sam scheduled it first under the ROE and deferred printer-fleet, which scored 4 and was out of the week's window.

Coverage metrics become honest when a block counts as a completed check. Chasing only open paths biases the report toward failure and hides controls that worked. PulseMap's planned-not-seen bucket exists so a quiet deny is still recorded. Sam lists blocked probes next to successful ones in the daily digest.

### 11.4 Errors and limits

Scanners fingerprint banners; banners lie. Confirm with an application-level check before writing a finding. Do not scan the public Internet from the course environment.

A banner that claims a product version can be copied from a template or left stale after an upgrade. An application-level check, such as reading a health page under authorization, confirms what is really there. Course environments stay off the public Internet so students never become an unwelcome scanner on someone else's network. Sam's lab machines have no route there.

### 11.3b Protocol families in scope

Scope documents should name protocol families explicitly: "TCP 443 with HTTPS application data" is clearer than "443". If TLS interception is forbidden, say so. If only TLS 1.2+ is eligible for testing, say so. Ambiguity here becomes an argument during the engagement when someone wants to try a legacy cleartext port "just to see".

Naming HTTPS on TCP 443 leaves no room for a cleartext experiment on the same number. Forbidding TLS interception up front avoids a mid-test argument with privacy and legal teams. Legacy cleartext ports stay closed unless the ROE lists them. Sam reads the protocol paragraph aloud with the client contact before kickoff.

### 11.4b Capturing only what the ROE allows

Packet captures taken during an authorized test often contain data outside the engagement's purpose, such as staff credentials or passenger records in Riverstone Transit's case. Sam's capture plan names the interfaces, a filter limited to in-scope hosts, a retention period and who may open the files, and the capture is deleted on schedule.

Filters and short retention shrink how much staff or passenger data can linger after the test. Naming who may open the files stops casual browsing of a capture that happened to include a login. Deletion on schedule is checked, not assumed. Sam's close-out includes a ticket showing the capture was wiped.

### Exercises

- **EX031 — Vantage.** Match three evidence types to the minimum vantage needed. Rubric: 3 = correct mapping (e.g. ARP table → link access; TLS cert → TCP to port; API field → authenticated session); 2 = two; 1 = one; 0 = none.
- **EX032 — Scope ports.** Rewrite "all web stuff" as a port set and an application note for Riverstone. Rubric: 3 = {80,443,8080} plus "only HTTP(S) to fare and staff apps"; 2 = ports only; 1 = vague; 0 = none.
- **EX033 — Inventory.** Which two assets would you schedule first from the lab and why? Rubric: 3 = public-web-portal and corp-vpn-edge with score/exposure reasons; 2 = correct without reasons; 1 = one; 0 = wrong.

### Synthesis

Networks give you a vantage and a port set. Scope them; treat blocks as results.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) separate configuration review from runtime abuse; (2) collect OS evidence under least privilege; (3) record account use so revocation is possible.

### 12.1 Configuration is usually enough

Password policy, patch level, listening services and local admin group membership answer most OS questions in an authorized assessment. Reading those under an admin account granted for the engagement is different from exploiting a service to obtain that account. Prefer the former; PTES-style discovery stays inside the agreed methods.

Admin-granted reads answer patch level and local group membership without turning the engagement into a hunt for a foothold. That distinction matters for ethics and for clarity of remediation: a finding from a granted account is about exposure and policy, not about a break-in path. Sam records that the account was issued for the test so readers do not infer stealth access.

### 12.2 Least privilege for the tester

Issue a named assessment account with a time-boxed role. Log every elevation. At the end of the engagement, disable the account and rotate any shared secrets it touched. FindingsDesk should store the account id used for each finding so revocation can be checked.

A named, time-boxed account can be disabled without hunting shared passwords. Logging elevation makes unusual rights visible during the engagement, not only afterwards. Storing the account id on each finding makes the revocation checklist mechanical. Sam's close-out fails if any finding still points at an enabled test account.

### 12.3 Local vs domain

A local administrator on one host is not domain administrator. Findings must name the identity store (local SAM, LDAP, cloud IdP). Conflating them inflates severity and misdirects remediation.

> **Synthetic case — Riverstone Transit.** SYN-005 was a lab service account with domain-admin rights — a directory finding, not a "Windows is broken" finding. Remediating meant removing the group membership and rotating the password, then verifying with a read of the group.

Remediation for a local admin is host hardening; remediation for domain admin is identity-store work. Mixing the labels sends the wrong team and the wrong urgency. Cloud identity providers add a third store that must be named explicitly. Sam's finding template requires the identity-store field before a ticket can leave draft.

### 12.4 Errors and limits

OS vendors change defaults; cite the version you observed. Do not disable security tools to "make the test work"; if a tool blocks you, that is a result under the ROE.

Defaults from last year's hardening guide may not match the build you saw. Citing the observed version keeps the finding checkable. A security tool that blocks a probe has done its job under the ROE; turning it off would invent a different system than the client runs. Sam reports the block and moves on to the next planned check.

### 12.3b Image and offline analysis

Full-disk images are high impact: they take systems offline, contain personal data, and tempt out-of-scope browsing. Prefer live, least-privilege reads. If an image is truly required, the ROE must name chain-of-custody, encryption at rest, who may mount it, and a destroy-by date — and the course labs still do not practice imaging real hosts.

Images are a last resort because of downtime and privacy. Live reads under least privilege answer most questions without copying whole disks. When an image is unavoidable, chain-of-custody and a destroy-by date are ROE requirements, not niceties. Course labs never image real hosts, so students practice the decision to avoid imaging rather than the imaging itself.

### 12.4b Recording host changes

Any setting a tester changes on a host, even a temporary log level, is written to the engagement log with time, reason and the command used to revert it. At close-out Sam walks that list with the system owner, so no Riverstone Transit host is left in a state nobody remembers creating.

Temporary log-level changes are still changes. A revert command written at the time survives staff turnover and weekend shifts. Walking the list with the owner turns close-out into a shared checklist rather than a memory test. Sam refuses to mark an engagement complete while any unreverted change remains on the list.

### Exercises

- **EX034 — Account design.** Specify a least-privilege assessment account for reading local admin group membership on three Windows hosts. Rubric: 3 = named account, group/role, time box, logging, revocation; 2 = three of five; 1 = "admin"; 0 = none.
- **EX035 — Severity wording.** Rewrite "we got SYSTEM everywhere" as a scoped finding sentence. Rubric: 3 = identity, hosts, method (config/authz), no exploit; 2 = missing scope; 1 = still vague; 0 = exploit language.
- **EX036 — Revocation check.** List three post-engagement checks that the assessment account is gone. Rubric: 3 = directory disabled, local leftover, ticket/log review; 2 = two; 1 = one; 0 = none.

### Synthesis

Read configuration with a temporary account; name the identity store; revoke when done.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) scope database assessment without extracting personal data; (2) test authorization at the query layer; (3) design synthetic datasets for labs.

### 13.1 Data minimization

Authorized database work uses synthetic rows or masked copies. Exporting production personal data into a student laptop is a privacy incident, not a finding. The ROE must state: no SELECT of columns tagged personal, no full-table dumps, row limits and a destroy-by date for any temporary extract.

Row limits and destroy-by dates turn temporary extracts into controlled objects rather than souvenirs. Tagging personal columns gives the query tool something to refuse automatically. A student laptop with a production dump is a breach waiting for a lost bag. Sam's ROE checklist fails the kickoff if any of those clauses is missing.

### 13.2 Authorization, not injection recipes

The engineering question is usually "can role R read table T?" Test that with the granted role. Teaching SQL injection payloads is out of this book's safety boundary; if injection is in scope for a professional engagement, it is under a separate method line and disclosure plan, not a homework exercise.

Role tests answer the client's real question: who among their staff can see which tables. Payloads belong outside this course because they teach harm without teaching the engineering of access control. When a professional ROE includes injection, it is a named method with its own disclosure path, never a lab exercise. Sam files authorization gaps as findings about roles and grants.

### 13.3 Synthetic data

Generate deterministic synthetic customers with faker-like rules or fixed seeds so labs reproduce. Never copy a production backup into the course repository.

> **Synthetic case — Riverstone Transit.** Sam needed fare-product rows for a report test. Ops provided a synthetic snapshot with product ids and prices only — no passenger names — and a 48-hour destroy tag.

Fixed seeds mean two students and a CI job see the same customers and the same failing checks. Production backups bring privacy duty and irreversible exposure if the repo leaks. Sam generates data in the lab setup script and commits only the generator, never a dump.

### 13.4 Errors and limits

Masking that leaves unique rare values can still identify people. Prefer synthetic generation over imperfect masking when teaching.

A rare disease code or an unusual job title can re-identify someone even after names are stripped. Synthetic rows avoid that argument entirely for teaching. When a client still demands masked extracts, Sam waits for privacy sign-off and keeps the files on client-controlled hosts and records the destroy-by date in the engagement log. Teaching labs never receive even masked production rows from any client.

### 13.3b Row-level and column-level controls

Modern warehouses offer row and column policies. Assessment questions become: does role R see column C? Does row filter F apply? Test with the role itself. Document the policy engine version; "we ran SELECT *" against an admin role proves little about analyst exposure.

Admin SELECT * shows what an admin sees, which is the wrong question for analyst exposure. Running as role R with the policy engine's version recorded makes the result match production behaviour. Column denies and row filters fail differently, so both need their own checks. Sam stores the role name on every such finding.

### 13.1b Masking pitfalls

Replacing names with initials or shuffling rare zip codes still leaves quasi-identifiers. For teaching and most assessments, synthetic generation with a fixed seed is simpler and safer than arguing about imperfect masks. If the host insists on masked production extracts, require a privacy review and keep the extract off student laptops.

Quasi-identifiers combine: a birth year, a depot and a rare job title can point to one staff member. Fixed-seed synthesis sidesteps the debate and still stresses authorization logic. Masked extracts that must be used stay off personal devices and under the privacy review's retention rules. Sam prefers to demonstrate the same finding on synthetic rows whenever the client allows it.

### Exercises

- **EX037 — ROE data clause.** Write a data-handling clause for a Postgres assessment. Rubric: 3 = no PII columns, row limit, no dumps, destroy-by, synthetic preferred; 2 = three; 1 = one; 0 = none.
- **EX038 — Authz test.** How do you test whether role `analyst` can read `passengers` without using an injection technique? Rubric: 3 = connect as analyst, attempt SELECT, record grant/deny; 2 = idea without role; 1 = vague; 0 = injection.
- **EX039 — Synthetic.** Give three fields safe for a synthetic fare table and two that must never appear in the course dataset. Rubric: 3 = e.g. product_id, price, zone vs name, card_number; 2 = partial; 1 = weak; 0 = none.

### Synthesis

Minimize data, test roles, synthesize for teaching. The database is not a trophy store.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) put assessment tools under version control with review; (2) gate scope-widening changes; (3) keep CI on synthetic fixtures only.

### 14.1 Tools are products

TrackScope and FindingsDesk are software. They need repositories, code review, tagged releases and changelogs. A ROE that cites "TrackScope" without a version is incomplete; cite `TrackScope v0.9.2` or the git SHA used.

Without a version, two engineers can run different builds and disagree about what the tool denied. Tags and changelogs make that disagreement checkable. Code review catches a scope check that fails open before it reaches an engagement. Sam pastes the SHA into the kickoff notes and refuses to start if the running binary differs.

### 14.2 Gate widening

Merges that add a CIDR, open a port or remove a deny-list entry require a second reviewer and a linked authorization ticket. Merges that only tighten scope can be lighter. Encode this in CODEOWNERS or a required check that diffs the scope files.

Widening scope is an authorization event, so it needs the same dual attention as a ROE change. Tightening can move faster because it cannot create new targets. A required check on scope diffs stops a quiet CIDR addition in a large pull request. Sam links every widening merge to the client's written approval ticket.

### 14.3 CI fixtures

Continuous integration runs the labs and unit tests on synthetic data. Never point CI at a client network. Seed data lives in the repo; secrets for real engagements live in a vault and never in CI logs.

> **Synthetic case — Riverstone Transit.** A PR added 10.30.0.0/16 to scope "for next month". CI's scope-diff check blocked merge until ticket AUTH-442 was linked and a second owner approved.

CI that can reach a client network would turn every broken test into a possible probe. Synthetic fixtures keep failures local and repeatable. Secrets in logs become incidents; vaults keep them out of build output. Sam's pipelines have no routes to engagement networks and fail if someone adds one.

### 14.4 Errors and limits

Version tags can drift from what operators actually run; record the running version in the engagement log at start.

Operators install hotfixes by hand and forget to update the tag on the checklist. Logging the running version at start makes the mismatch visible before traffic flows. Sam compares that log line to the ROE pin and stops the window on disagreement until operators install the pinned build or the ROE is revised. A sticky note on a laptop is not a version pin.

### 14.3b Release trains vs hotfixes

Normal improvements ride a release train with Lab I/II. Safety hotfixes may skip features but not verification: a minimal fail-closed regression pack is mandatory. Tag hotfixes clearly so an engagement can pin either the train build or the hotfix SHA with eyes open.

Safety fixes must still prove fail-closed behaviour, even when features wait. Clear tags stop an engagement from silently mixing a train build with a laptop hotfix. Pinning with eyes open means the client knows which binary produced the evidence. Sam keeps the regression pack small so hotfixes stay fast without skipping it.

### 14.1b Branching model

Use short-lived branches with mandatory CI on synthetic fixtures. Long-lived feature branches diverge from safety fixes on main and recreate fail-open merges. Protect main with required reviewers and status checks named after Lab I safety rows.

Short branches pick up safety fixes from main instead of reinventing them weeks later. Long-lived branches are how fail-open merges return after they were fixed. Required checks named after Lab I rows make the safety suite impossible to skip with a casual approve. Sam deletes stale branches weekly so divergence cannot hide.

### Practice note

Version pins appear in the engagement kickoff checklist beside the ROE hash. Operators read the pin aloud before the window opens so nobody silently runs a laptop build. If the pin and the running binary disagree, the window does not start until someone files an AUTH note or rolls back. That ritual has prevented more incidents than any banner in the UI, because it forces a human to look at the SHA while the client is still on the call.

### Exercises

- **EX040 — Version line.** Write the method sentence that pins TrackScope for an engagement. Rubric: 3 = name, version/SHA, date loaded; 2 = name+version; 1 = name only; 0 = none.
- **EX041 — Gate rule.** Write a one-sentence merge policy for scope files. Rubric: 3 = second reviewer + auth ticket for widen; 2 = reviewer only; 1 = vague; 0 = none.
- **EX042 — CI boundary.** Why must CI never use client VPN credentials? Rubric: 3 = unauthorized automation risk, secret leakage in logs, non-determinism; 2 = one solid reason; 1 = vague; 0 = wrong.

### Synthesis

Treat assessment software like production software: versions, review gates and synthetic CI.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) map CIA and authentication/authorization to assessment questions; (2) distinguish vulnerability, exposure and risk; (3) refuse risk scores without a model.

### 15.1 CIA as questions

Confidentiality: who can read this? Integrity: who can change this? Availability: what stops this working? Each finding should say which property is affected and for which asset. "Security issue" without that map is not actionable.

Mapping each finding to confidentiality, integrity or availability tells the fixer what kind of harm to prevent. An asset without a property leaves the client guessing whether to encrypt, validate or add capacity. Sam rejects draft tickets that still say only 'security issue' and sends them back with the three questions listed.

### 15.2 Vulnerability, exposure, risk

A default password is a vulnerability. On a staging host reachable from the corporate network it is an exposure. Risk adds likelihood and impact for the organization — which needs their context, not a universal CVSS-only story. FindingsDesk stores impact and exposure fields separately; risk acceptance stays with the client.

Separating the three stops a default password on an isolated lab host being scored like one on the public portal. Exposure fields capture reachability; impact fields capture harm; acceptance of residual risk stays a client decision. CVSS alone cannot know Riverstone Transit's ridership or depot layout. Sam fills exposure and impact and leaves the acceptance box for the client owner.

### 15.3 Empty scores

Albrecht and Jensen (arXiv:2010.06377) criticize methodology scores that do not predict outcomes. Prefer concrete measures: out-of-scope probe count, time-to-fix, precision at the client's base rate. If you show a score, show the model and the inputs.

> **Synthetic case — Riverstone Transit.** Sam stopped putting a single "risk = 42" on slides. The deck now shows two critical findings, three SLA breaches and 71% technique coverage of the planned set.

A methodology score that does not predict outcomes flatters the assessor and misleads the buyer. Counts of out-of-scope probes and time-to-stop are ugly and useful. When a score must appear, the model and inputs sit beside it so another engineer can recompute. Sam's dashboards lead with those concrete measures.

### 15.4 Errors and limits

Fundamentals are shared vocabulary; they are not a complete threat model. Continue into Chapter 23 for structured failure analysis.

Shared vocabulary gets teams talking; it does not list every failure mode. Structured analysis later in the course builds on these terms rather than replacing them. Sam treats a CIA label as the start of a finding, not the end of the threat model. He expects the structured analysis chapters to add failure modes these terms alone cannot name. Until then, the vocabulary still prevents vague tickets.

### 15.3b Mapping to tickets

Every finding should cite which property (C, I, or A) is primarily affected and whether the issue is vulnerability, exposure, or a risk judgment left to the client. FindingsDesk can require the fields so reports stay consistent across authors and semesters.

Required fields stop authors inventing private shorthand for the same ideas. Consistency across semesters means a re-test engineer can read last year's ticket without a translation guide. Clients comparing two firms see the same shape of claim. Sam's template blocks submit until property and issue-kind are set.

### 15.1b From property to test

If a finding claims confidentiality impact, the validation plan must include a confidentiality check (who can still read). If it claims availability impact, validation includes a canary or synthetic probe — not a new attack. Align property, finding and re-test method in one paragraph of the ticket.

A confidentiality claim without a who-can-read check cannot be closed honestly. Availability claims need a gentle canary, not a fresh flood. One paragraph that ties property, finding and re-test keeps the ticket coherent after handoff. Sam pastes that paragraph into the validation plan field before the finding leaves draft.

### Exercises

- **EX043 — CIA map.** Map SYN-001 (default admin on staging) to C/I/A with one sentence each. Rubric: 3 = all three scoped; 2 = two; 1 = one; 0 = none.
- **EX044 — Terms.** In one sentence each, distinguish vulnerability, exposure and risk for SYN-005. Rubric: 3 = clear split; 2 = two clear; 1 = muddled; 0 = none.
- **EX045 — Score refusal.** A stakeholder wants a single 0–100 "hackability" score. Write a refusal with an alternative. Rubric: 3 = refuses empty score, offers concrete measures; 2 = refuses only; 1 = vague; 0 = invents score.

### Synthesis

Name the property, separate exposure from risk, and prefer measures you can recompute.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) write requirements that are testable; (2) trace a requirement to an artefact; (3) manage interfaces between TrackScope, FindingsDesk and PulseMap.

### 16.1 Testable requirements

"The system should be secure" is not a requirement. "TrackScope rejects any target outside the signed CIDR/port set and records the reason code" is. Each requirement needs an id, a shall-statement, a verification method (test, inspection, analysis) and an owner.

Shall-statements with ids turn arguments into checks. Verification method and owner stop requirements that nobody can prove and nobody maintains. Sam writes the reject-and-record behaviour of TrackScope as requirement TS-SCOPE-1 with a unit test as its method. Anything weaker is rewritten before design starts.

### 16.2 Traceability

A simple matrix: requirement → design element → test case → engagement evidence. When a finding shows a scope bypass, you know which requirement and test failed. Without the matrix, post-mortems become blame.

When a scope bypass appears, the matrix names the broken test and the requirement it was meant to enforce. Blame cultures grow in the gap where that link is missing. Sam updates the matrix in the same change as the code so the link cannot rot for a week. Post-mortems open on that row first.

### 16.3 Interfaces

TrackScope emits allow/deny events; FindingsDesk consumes finding drafts; PulseMap consumes technique tags. Agree JSON schemas and version them. An interface change is a release, not a silent edit.

> **Synthetic case — Riverstone Transit.** Requirement R-17 "deny reasons are immutable after insert" traced to the FindingsDesk append-only event table and test T-17 that tries an UPDATE and expects failure.

Silent schema edits break stop-condition pages at the worst moment. Versioned JSON contracts make breakage a deliberate release with a migration note. Each consumer declares the versions it accepts. Sam's integration tests publish a sample event at each supported version.

### 16.4 Errors and limits

Traceability matrices rot if not updated in the same PR as the code. Keep them next to the code.

A matrix in a slide deck dies first. Keeping it beside the code means the same review that merges a feature sees the traceability update. Sam fails CI if a new requirement id lacks a test row. Slide-only matrices are rejected in review. Owners get a weekly mail if their rows lag the merged code, and the engagement cannot cite a requirement that has no current test.

### 16.3b Interface SLAs

Internal SLAs between services matter: TrackScope may need FindingsDesk to accept an event within N seconds during a stop condition. Write that as a requirement with a synthetic load test. Without it, stop-condition pages arrive after the human already called the client.

A stop-condition event that arrives late is an event that failed its purpose. Synthetic load tests prove FindingsDesk can accept bursts when TrackScope denies many targets at once. Writing the latency budget as a requirement makes it visible in planning, not only in an outage. Sam pages on SLA breaches during exercises so the path is rehearsed.

### 16.1b Glossary for stakeholders

Maintain a one-page glossary: ROE, ScopeVersion, deny-list, planned technique, sealed evidence. Stakeholders misuse "coverage" and "risk" constantly; the glossary is a requirements artefact, not decoration, and appears in the engagement kickoff deck.

Coverage and risk are everyday words with special meanings here, and misuse drives bad decisions. A one-page glossary in the kickoff deck gives everyone the same definitions before the window opens. ROE, ScopeVersion and sealed evidence each get one plain sentence. Sam reads the three most-abused terms aloud at kickoff and leaves the page in the shared folder.

### Practice note

Traceability also covers retirement: when a requirement is withdrawn, mark it superseded with a pointer to the replacement rather than deleting the row. Historical findings still cite old ids. A living matrix that forgets history makes last year's dossier unverifiable and trains engineers to treat requirements as disposable slides instead of engineering artefacts that outlive a single release train.

### Exercises

- **EX046 — Shall.** Rewrite "make scanning safe" as two shall-requirements. Rubric: 3 = two testable shalls with verify method; 2 = one good; 1 = still vague; 0 = none.
- **EX047 — Trace.** For R-17 above, name the artefact and the failing test signal. Rubric: 3 = event table + UPDATE fails; 2 = one; 1 = vague; 0 = none.
- **EX048 — Interface.** List three fields in a TrackScope deny event. Rubric: 3 = timestamp, target, reason (or equiv.); 2 = two; 1 = one; 0 = none.

### Synthesis

Requirements you can test, links you can follow, schemas you version.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) model a control loop around assessment tooling; (2) choose sensors and actuators; (3) avoid unstable feedback (alert storms).

### 17.1 Loop

Sensor: out-of-scope probe count per hour. Controller: compare to threshold 0. Actuator: TrackScope hard-deny and page the lead. Plant: the engagement. Without the sensor, you only discover scope breaks in the final report.

The zero threshold means any out-of-scope probe is already a breach of the promise, not a soft warning. Paging the lead closes the loop while the window is still open, when stop and notify still help. Without an hourly count, the final report becomes the first sensor, which is too late for the client. Sam graphs the count live next to the deny log so a spike is obvious.

### 17.2 Stability

If every medium finding pages the whole company, people silence the pager (alert fatigue). Severity-based routing and rate limits on notifications are the damping. The baserate lab (Chapter 7) is the same idea for detectors.

Damping keeps the signal useful. Medium findings go to the owning team queue; only stop conditions and critical safety events page everyone. Rate limits stop a flapping sensor from waking the company every minute. The same lesson as the base-rate work applies: a detector that cries often is turned off.

### 17.3 Manual vs automatic

Hard denies of deny-listed hosts can be automatic. Changing the ROE mid-engagement must stay manual and signed. Put automation on the inner loop; keep humans on the outer loop.

> **Synthetic case — Riverstone Transit.** After the 11:10 deny-list touch, Sam added a sensor: any deny-list hit pages the lead within one minute. False pages in a week: zero.

Automatic deny is fast enough to stop a bad probe in the same second. A mid-window ROE change alters what is legal, so it needs a signature and two people. Drawing that line in the design review prevents arguments during the engagement. Sam's runbook says which class of change is which.

### 17.4 Errors and limits

Feedback assumes the sensor is honest. A broken logger looks like a quiet system. Heartbeat the sensors.

A silent logger can hide a flood of denies or pretend none occurred. Heartbeats prove the sensor still reports, even when the count stays at zero. Sam pages on missing heartbeats with the same urgency as a real spike, because both mean the loop is blind. He checks the heartbeat path in staging before each engagement window opens and keeps a screenshot of the green check in the dossier.

### 17.2b Choosing the sampling interval

A sensor that samples once an hour can miss a five-minute out-of-scope burst. Sample at least twice as often as the shortest stop-condition window you promised the client. If the kill-switch must act in 30 seconds, poll every 10–15 seconds. The cost is cheap compared with explaining a missed stop in the report.

Nyquist-style thinking applies: sample faster than the event you must catch. A thirty-second kill-switch with hourly polls is theatre. Ten to fifteen seconds leaves margin for slow disks and busy leaders. Sam records the chosen interval next to the stop-condition text so auditors see they match.

### 17.3b Human-in-the-loop placement

Put humans where judgment about authorization is required; put automation where delay is dangerous. Approving a scope widen is human. Denying a deny-listed host is automation. Mixing them — waiting for a human to approve a deny — recreates the incident the control was meant to stop.

Judgment about permission cannot be rushed into a script; delay on a deny can. Waiting for a human to approve a deny-list hit is how out-of-scope traffic continues. Sam's design review checklist asks of every control whether delay helps or hurts, and places the human only where it helps.

### 17.1b Set-points and drift

Write the set-point next to the sensor ("out-of-scope probes per hour = 0"). Review set-points when the client changes windows or when false pages exceed an agreed rate. Unreviewed set-points drift into ignored alarms.

A set-point nobody revisits becomes folklore. Client window changes and false-page budgets both force a fresh look. Writing the number beside the sensor keeps operators from inventing a private threshold. Sam reviews set-points at kickoff and after any week that exceeded the false-page budget, and he writes the new number into the sensor config in the same change.

### Exercises

- **EX049 — Loop design.** Name sensor, threshold, actuator for SLA breaches. Rubric: 3 = all three coherent; 2 = two; 1 = one; 0 = none.
- **EX050 — Fatigue.** Give one damping rule for finding notifications. Rubric: 3 = specific rule (batch, severity, rate); 2 = vague "don't spam"; 1 = none useful; 0 = none.
- **EX051 — Manual boundary.** Which change must not be automated mid-engagement? Rubric: 3 = ROE/scope widening with reason; 2 = partial; 1 = wrong; 0 = none.

### Synthesis

Sense, compare, act — with humans on authorization and machines on enforcement.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) place assessment tools in a zone model; (2) define trust boundaries for evidence; (3) choose when to isolate a test range.

### 18.1 Zones

Assessment laptops, TrackScope, FindingsDesk and the client's assets sit in different trust zones. Traffic from the assessment zone to client assets is only what the ROE allows; traffic back carries evidence into a store the client can audit. Do not put the evidence store on the same VLAN as the targets "for convenience".

Separating the evidence store from targets means a compromised test host cannot quietly rewrite history. ROE-shaped traffic is the only path toward client assets; everything else is dropped and logged. Convenience VLANs are how evidence and targets share fate. Sam's kickoff includes a traceroute from TrackScope to the store and to a sample target to prove the zones.

### 18.2 Trust boundaries

Crossing a boundary needs authentication, authorization and logging. A student exporting findings to a personal drive crosses a boundary without a control — forbid it in the ROE and in tool policy.

Personal drives sit outside every client control. Tool policy that blocks export is stronger than a paragraph nobody reads under deadline. Authentication, authorization and logging are the minimum trio at each crossing. Sam treats a blocked export as a successful control, not as friction to remove. He demos the block during kickoff so nobody asks for a bypass later.

### 18.3 Isolated ranges

When methods are noisy or the client is fragile, use a synthetic range that mirrors configuration. Results then support claims about the mirrored config, not about production runtime. Say so in the report.

> **Synthetic case — Riverstone Transit.** PulseMap and FindingsDesk run in the security-tools VPC; scanners egress through a controlled proxy that enforces the CIDR allow-list.

Mirrors prove configuration claims when production is too fragile for noise. They do not prove runtime behaviour under live load, and the report must not pretend otherwise. Sam labels every finding from a mirror with the range id and the config revision used.

### 18.4 Errors and limits

Diagrams age. Re-validate zones at engagement start.

A diagram from last quarter may show a VLAN that no longer exists. Re-validation is a checklist item at engagement start, with a dated screenshot or export in the dossier. If the live path disagrees with the diagram, Sam stops until architecture and ROE are updated together, so the team does not test against a map of a different network. The dated export is hashed like any other evidence file and linked from the kickoff checklist.

### 18.3b Egress control

Assessment zones need egress allow-lists: only the client's in-scope CIDRs and the evidence store. Open egress turns a compromised laptop into a pivot that the ROE never authorized. Enforce egress in the same policy pipeline as target allow/deny when possible.

Allow-lists for egress shrink the blast of a stolen laptop to what the engagement already permitted. Open DNS and web egress are enough for many silent exfiltration paths. Putting egress in the same pipeline as target checks means one policy language and one audit log. Sam tests a denied egress destination on day one and keeps the log line.

### 18.1b Jump hosts

Assessment jump hosts are high-value: harden them, log session start/stop, forbid personal file sync agents, and rebuild from golden images between engagements when feasible. A messy jump host undermines every careful zone diagram.

Golden-image rebuilds wipe leftover tools, sync agents and stale credentials between clients. Session logs answer who was on the host when a change occurred. Personal sync agents are forbidden because they copy evidence to unmanaged clouds. Sam's pre-flight fails if a sync agent package is present.

### Practice note

Network diagrams for the assessment zone go into the dossier with the same hash discipline as evidence files. When an auditor asks how traffic reached staging, you show the diagram version that was live, not a newer cleaned-up sketch. Treating diagrams as versioned artefacts closes a common gap between architecture intent and what actually ran during the window.

### Exercises

- **EX052 — Zone sketch.** Place laptop, TrackScope, evidence store, staging UI in zones and name two controls on the arrows. Rubric: 3 = clear zones + two controls; 2 = zones only; 1 = muddle; 0 = none.
- **EX053 — Boundary.** Why is "email the finding to my Gmail" a boundary violation? Rubric: 3 = data leaves controlled store/authz; 2 = privacy handwave; 1 = vague; 0 = okays it.
- **EX054 — Mirror claim.** Write the limitation sentence for a synthetic-range-only test. Rubric: 3 = claims config not prod runtime; 2 = vague limit; 1 = overclaim; 0 = none.

### Synthesis

Zones, boundaries and honest limits on what a range can prove.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) assess auth configuration without attacking crypto; (2) use hashing for evidence integrity; (3) handle secrets safely in tooling.

### 19.1 Auth configuration

Ask: which IdP, which factors, which roles, which token lifetimes? Read configuration and logs under authorization. Breaking TLS or cracking password hashes is outside this book's labs and usually outside student scope.

Configuration and logs under a granted role answer lifetime, factors and role maps without turning the lab into crypto breaking. Token lifetime findings are operational and fixable. Sam records the IdP product and version beside each auth finding so remediation aims at the right console. Password-hash cracking requests are refused with a pointer to this boundary.

### 19.2 Evidence hashing

Hash evidence files (SHA-256) and store the digests in the ticket. Re-hash later to detect tampering. The lab shows a mismatch when a file changed.

```python
"""Verify integrity of a synthetic evidence package."""
import hashlib, json
files = {
    "roe.pdf": b"SYNTHETIC-ROE-v1",
    "scope.csv": b"host,port\n10.20.1.10,443\n",
    "findings.json": b'[{"id":"SYN-001"}]',
}
expected = {n: hashlib.sha256(b).hexdigest()[:16] for n,b in files.items()}
# Simulate tampering of findings.json
current = dict(expected)
current["findings.json"] = hashlib.sha256(b'[{"id":"SYN-001"},{"id":"TAMPERED"}]').hexdigest()[:16]
print(json.dumps(expected, indent=1))
for n in sorted(expected):
    status = "OK" if expected[n] == current[n] else "MISMATCH"
    print(f"{n:16} {status}")
```

Expected output:

```text
{
 "roe.pdf": "18d74983d403e7db",
 "scope.csv": "01cc4815eddf3de6",
 "findings.json": "7f5f178ab43ef00f"
}
findings.json    MISMATCH
roe.pdf          OK
scope.csv        OK
```

Digests in the ticket make later tampering visible even if the file store is altered. Re-hashing at review time is a one-line check. The lab's mismatch case trains the reflex to dig when hashes disagree. Sam refuses to close a finding whose current digest differs from the ticket without an AUTH note explaining the change.

### 19.3 Secrets in tools

Assessment credentials live in a vault; tools fetch short-lived tokens. No secrets in git, screenshots or chat. Rotate at engagement end.

> **Synthetic case — Riverstone Transit.** The hash lab showed findings.json mismatched — someone had edited a severity field after sealing. Sam restored from the sealed store and opened a process finding about uncontrolled edits.

Short-lived tokens limit how long a leaked string works. Git and chat are permanent enough to treat any secret pasted there as burned. Rotation at close-out is on the same checklist as account disable. Sam's CI greps for token-shaped strings and fails the build when they appear.

### 19.4 Errors and limits

Hashes detect change, not malice versus accident. Pair them with access logs.

A changed file might be an edited screenshot or a malicious swap; the hash alone cannot say which. Access logs show who touched the object and when. Sam always files hash and log reference together before calling evidence sealed, and he treats a missing log as an incomplete seal even when the digest still matches. Accident versus malice is then a question for the access log and the people who hold it.

### 19.2b What a hash does not prove

A matching digest says the bytes are the same as when sealed; it does not say the bytes were obtained lawfully, that the account was authorized, or that the interpretation in the finding text is correct. Pair hashes with the ROE version, actor id and a short method note so a reviewer can reconstruct the claim, not only the file.

Reviewers who stop at a green checkmark miss unlawful collection and wrong interpretation. ROE version and actor id tie the bytes to permission and person. A short method note explains what the file is supposed to show. Sam's seal checklist has four boxes: digest, ROE, actor, method.

### 19.3b Algorithm choices

Prefer SHA-256 or stronger for evidence manifests; avoid MD5/SHA-1 for new work. Document the algorithm in the manifest so a future reader does not guess. Cryptographic agility here is a version field, not a silent swap mid-engagement.

MD5 and SHA-1 collisions are teaching history, not a base for new manifests. Naming the algorithm in the manifest stops a future reader from assuming MD5 because a legacy tool printed it. Silent swaps mid-engagement split the evidence set into incompatible digests. Sam pins the algorithm in TrackScope config and rejects uploads that omit it.

### 19.1b Certificate inventory

For TLS-facing assets, record presented certificates (subject, issuer, notAfter) under authorization. Expired or mismatched certs are findings about operations integrity; do not turn the exercise into a research-grade TLS attack.

Subject, issuer and notAfter under authorization are enough to flag expiry and name mismatch. Those are integrity and operations findings, not an invitation to research-grade protocol attacks. Sam stores the PEM fingerprint in the ticket so a re-test can see whether the cert changed. Inventory runs are scheduled, not improvised during a noisy scan.

### Exercises

- **EX055 — Auth questions.** List five configuration questions for Riverstone's staff SSO. Rubric: 3 = five concrete (IdP, MFA, roles, lifetime, admin path); 2 = three; 1 = one; 0 = none.
- **EX056 — Hash lab.** Which file mismatched and what do you do? Rubric: 3 = findings.json; restore/re-seal; investigate who wrote; 2 = file only; 1 = vague; 0 = wrong.
- **EX057 — Secret rule.** Write a one-line policy for assessment passwords in tickets. Rubric: 3 = never in ticket body; reference vault id; 2 = "don't share"; 1 = weak; 0 = allows paste.

### Synthesis

Read identity config; hash evidence; keep secrets in a vault.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Authorized offensive security and red team: engineering context

### Learning outcomes

You will (1) place red-team engineering among PTES, NIST SP 800-115 and ATT&CK; (2) define what this degree programme builds; (3) state the safety boundary for all later chapters.

### 20.1 Discipline map

NIST SP 800-115 frames testing and assessment. PTES sequences pre-engagement through reporting. ATT&CK names techniques for planning and coverage — not as a score of residual risk. TIBER-EU and CBEST add threat-led oversight for certain financial contexts. Engineers build the platforms that make those frameworks operable: scope checkers, finding systems, coverage reporters, evidence stores.

Frameworks describe the engagement lifecycle; ATT&CK labels techniques for planning. None of them is a residual-risk score on its own. The engineering job is making scope checks, findings and coverage reports real systems operators can run. Sam cites the framework version in each ADR that implements a control they require.

### 20.2 What we build

Riverstone's TrackScope, FindingsDesk and PulseMap are the running example of that platform layer. Graduates should leave able to design, verify and operate such systems under authorization — not to invent exploits.

Design, verification and operation under authorization is the graduate outcome. Exploit invention is out of scope for the degree and for Riverstone's platform team. TrackScope, FindingsDesk and PulseMap show how far that platform layer reaches into daily work. Sam's studio briefs always ask which platform artefact the student will leave behind.

### 20.3 Safety boundary

No exploit payloads, no unauthorized targets, no live personal data, labs on synthetic local data only. Dual-use requests are refused (Chapter 10). This boundary is a requirement on every design review in Chapters 21–50.

> **Synthetic case — Riverstone Transit.** Leadership asked for "a red team that hacks everything". Sam reframed the charter: "an authorized assessment platform that enforces ROE and measures remediation."

The boundary is enforced in design review, not only in a preface. Dual-use refusals from the ethics chapter apply to every later feature request. Synthetic local labs keep coursework off real networks and real people. Sam rejects studio proposals that need live personal data or unauthorized targets, even as demonstrations.

### 20.4 Errors and limits

Frameworks evolve; re-check URLs and versions before citing in a thesis. This chapter orients; it does not replace reading the primary sources.

Primary sources move; a thesis that cites a dead URL fails a basic check. This chapter points; it does not summarise every clause of PTES or NIST SP 800-115. Sam bookmarks the versions he used and re-opens them before submission week, and he quotes clause ids rather than paraphrases when a requirement hangs on the text. Paraphrase alone has caused more than one failed viva.

### 20.3b Neighbouring courses

This engineering book assumes comfort with calculus, probability and software engineering from earlier chapters. The bachelor's RED book is broader and less design-heavy; the technologist book emphasizes implementation drills. Pick artefacts that match the level — a thesis-sized empty score is still empty.

Choosing artefacts that match the level avoids empty thesis scores in a book that demands design evidence. Implementation drills belong in the technologist path; this book wants schemas, tests and ADRs. Sam steers students who arrive from the bachelor's path toward deeper verification of the same tools.

### 20.1b Engineering deliverables vs operator deliverables

Operators need runbooks and tickets; engineers need schemas, tests and ADRs. Capstone grading looks for both. A beautiful tool without a runbook fails operations; a runbook without fail-closed tests fails engineering.

Graders look for both because either gap fails in the field. Fail-closed tests without a runbook leave night staff guessing; runbooks without tests leave fail-open paths latent. Sam's capstone rubric scores the pair together on each feature. Students who ship only one of the two revise before the defense.

### 20.4b Who the engineering team serves

The platform team's users are testers and engagement leads; its stakeholders also include the client's system owners, who never see the code but carry the risk if TrackScope fails open. Sam's requirement notes list both groups, so a feature that helps testers move faster but weakens a client safeguard is visible as a trade-off before it is built.

### Exercises

- **EX058 — Framework fit.** Pair each need with PTES / SP 800-115 / ATT&CK / TIBER-EU. Rubric: 3 = four sensible pairs; 2 = three; 1 = two; 0 = none.
- **EX059 — Charter rewrite.** Rewrite "hack everything" as an engineering charter sentence. Rubric: 3 = authorization + platform + measurement; 2 = partial; 1 = still attack-centric; 0 = none.
- **EX060 — Boundary.** Give three concrete "out of scope for this programme" items. Rubric: 3 = three clear (payloads, real targets, PII dumps…); 2 = two; 1 = one; 0 = none.

### Synthesis

Engineers enable authorized assessment; they do not replace authorization with cleverness.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Authorized offensive security and red team: requirements

### Learning outcomes

You will (1) elicit requirements from ROE and operators; (2) separate functional, safety and measurement requirements; (3) write acceptance criteria a tester can run.

### 21.1 Sources of requirements

Operators want fewer false blocks; counsel wants an audit trail; the client wants clear findings. Elicitation interviews produce shall-statements tagged by source. Conflicts (speed vs approval gates) are recorded, not papered over.

Tagged sources make conflicts discussable: speed versus gates is a recorded trade-off with an owner. Papering over it produces a tool nobody trusts. Interviews end in shall-statements, not vibes. Sam keeps the conflict log next to the requirements file so a new lead can see old arguments without replaying them.

### 21.2 Three families

Functional: "TrackScope evaluates allowed(host,port) before every action." Safety: "TrackScope fails closed if the policy file does not load." Measurement: "PulseMap reports planned-vs-observed technique counts with denominators." Safety requirements win ties.

Safety winning ties means a fast path that skips policy load is rejected even if testers cheer. Measurement requirements force denominators so coverage cannot be a bare count. Functional requirements name the moment of check, such as before every action. Sam colours safety rows in reviews so they cannot be bargained down quietly.

### 21.3 Acceptance criteria

Each requirement has a Given/When/Then on synthetic data. Example: Given deny-list {10.20.0.1}, When probe 10.20.0.1:443, Then DENY deny-list and an event is stored. Criteria that need a real client network are rejected at review.

> **Synthetic case — Riverstone Transit.** Safety requirement S-3 "fail closed on missing policy" failed its acceptance test when a typo path returned ALLOW. The fix shipped before any engagement use.

Synthetic Given/When/Then keeps CI honest and keeps client networks out of the test bed. Criteria that need production are redesigns, not stretch goals. The deny-list example is copied into TrackScope's suite as a named test. Sam fails review when a Must requirement lacks such a criterion.

### 21.4 Errors and limits

Stakeholders invent requirements mid-engagement; park them in a backlog with an authorization ticket, do not hot-patch production TrackScope during a live test window.

Hot-patching TrackScope mid-window risks a fail-open mistake while traffic is flowing. Backlog plus authorization ticket is the only path for new ideas during a test. Sam's on-call script says no production config changes except stop and revoke. Feature ideas raised in the war room go to the ticket queue the same hour, still untouched in production until a signed change lands after the window.

### 21.3b Requirement ids in code

Put requirement ids in test names and in log fields (`req=S-3`). When an incident happens, searchability beats a slide that once mapped requirements to modules. Dead requirements without tests should fail CI.

Searchable ids turn an incident channel into an index. Tests named for dead requirements fail CI until someone deletes or replaces them. Log fields carry the same ids so a deny event points at S-3 without a slide deck. Sam greps for req= in incident reviews before assigning blame.

### 21.1b MoSCoW under safety

Must/Should/Could prioritization still places all safety requirements in Must. A Could that weakens Must (optional deny-list) is reclassified or rejected. Product managers do not outvote fail-closed.

Optional deny-lists are not Could items; they break Must. Product managers who want a demo mode that loads without policy get a recorded refusal. Sam's prioritization board has a hard swimlane for safety Musts that cannot be dragged to Should. Demo modes that skip policy load are closed as wontfix with a link to this rule.

### Practice note

Acceptance tests are named after requirement ids and fail CI when skipped. A dashboard of requirements without tests is reviewed weekly in studio. Orphan Must requirements are either tested or formally deferred with an executive owner — silence is not deferral. This habit is what turns a requirements spreadsheet into something that still matters on the Friday before an engagement.

### Exercises

- **EX061 — Elicit.** Write one functional and one safety shall from "we must never hit the gateway." Rubric: 3 = both testable; 2 = one; 1 = vague; 0 = none.
- **EX062 — Acceptance.** Give Given/When/Then for fail-closed on missing policy. Rubric: 3 = complete with expected DENY/error; 2 = partial; 1 = idea; 0 = none.
- **EX063 — Conflict.** Speed vs dual approval for scope widening — record the conflict and the chosen rule. Rubric: 3 = conflict named + safety-first rule; 2 = rule only; 1 = picks speed; 0 = none.

### Synthesis

Requirements come from people, split into families, and ship with acceptance tests on synthetic fixtures.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Authorized offensive security and red team: system and data models

### Learning outcomes

You will (1) draw an entity model for engagements, scopes and findings; (2) choose keys and cardinality; (3) keep exploit content out of the model.

### 22.1 Entities

Engagement 1—* ScopeVersion; Engagement 1—* Finding; Finding *—* EvidenceObject (by hash); TechniqueTag *—* Finding. Cardinality mistakes (many scopes active without a version pointer) cause auditors to ask "which ROE was live?"

### 22.2 Keys

Finding ids are ULID/UUID. Evidence is content-addressed by SHA-256. ScopeVersion has (engagement_id, version_int). Never key findings by title — titles change.

### 22.3 Forbidden attributes

No attribute for payload, password or shell command. EvidenceObject stores bytes in a sealed bucket; the model stores only hash, media type and retention class.

> **Synthetic case — Riverstone Transit.** An early schema had `notes` as free text; people pasted passwords. Sam replaced it with structured fields plus an evidence hash, and a linter rejects password-like strings in titles.

### 22.4 Errors and limits

Models that try to encode all of ATT&CK as mandatory fields force junk tags. Keep technique tags optional and reviewed.

### 22.2b Time and actors

Every mutable entity needs `created_at`, `created_by`, and for state changes `updated_at`/`updated_by` or an append-only event. Wall-clock alone is not an audit trail. Prefer UTC with an explicit offset in exports so shift handovers across time zones do not reorder history.

### 22.3b Soft delete vs purge

Findings are rarely hard-deleted during retention; they soft-delete with an actor and reason. Purge jobs honour retention class and emit an audit event. A silent DELETE FROM findings is a repudiation gift to anyone challenging the dossier later.

### 22.1b Attachment size limits

Evidence objects need size caps and media-type allow-lists. Unbounded uploads become availability attacks on the store and tempt dumping of bulk personal data. Large artefacts stay in the sealed bucket with streaming hash computation.

### Exercises

- **EX064 — Cardinality.** Why is ScopeVersion required instead of editing Scope in place? Rubric: 3 = audit/history of what was authorized when; 2 = vague versioning; 1 = "best practice"; 0 = none.
- **EX065 — Key choice.** Why content-address evidence? Rubric: 3 = integrity + dedup + tamper evidence; 2 = one reason; 1 = vague; 0 = none.
- **EX066 — Forbidden.** Propose a validation that stops passwords in `title`. Rubric: 3 = heuristic/linter + process; 2 = one; 1 = vague; 0 = none.

### Synthesis

Model engagements, versions, findings and hashes — not attacks.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Authorized offensive security and red team: threat and failure analysis

### Learning outcomes

You will (1) enumerate failures of the assessment platform itself; (2) use a lightweight STRIDE-on-tools pass; (3) feed results into requirements.

### 23.1 The tool can fail dangerously

TrackScope failing open, FindingsDesk losing deny events, PulseMap counting coverage without a denominator — these are threats to *safety and honesty*, not only to confidentiality of the tool.

### 23.2 STRIDE on the platform

Spoofing: fake assessment account. Tampering: edit finding severity after seal. Repudiation: no actor on deny events. Information disclosure: evidence bucket world-readable. Denial of service: scanner floods client. Elevation: operator role can widen scope alone. Each row gets a mitigation requirement.

### 23.3 Engagement threats stay in scope docs

Threats *to the client* belong in the engagement's threat-led scenario (if any), not as features of TrackScope. Do not build "automated exploitation" to satisfy a STRIDE row.

> **Synthetic case — Riverstone Transit.** STRIDE row "fail open" became safety requirement S-3 (Chapter 21). Row "solo scope widen" became the dual-approval gate (Chapter 14).

### 23.4 Errors and limits

STRIDE is a prompt, not a proof. Revisit after architecture changes.

### 23.2b Abuse cases vs misuse cases

Abuse cases are intentional adversary actions against the platform (forge a policy signature). Misuse cases are honest operators making dangerous mistakes (paste a CIDR that includes a partner). Design controls for both; training alone does not stop misuse when the UI makes widen-scope a single click.

### 23.3b Feeding backlog

STRIDE rows become issues with links to requirements. Unowned rows are theatre. Review the threat list when adding a new trust boundary (for example, a new SaaS adapter) — not only at programme start.

### 23.1b Assuming breach of the jumphost

Include "jumphost compromised" in the platform threat model: short-lived credentials, egress allow-lists, and rapid revocation. If your response is only "trust the jumphost", the analysis is incomplete.


### 23.4b Ranking platform threats

Sam ranks the STRIDE findings by consequence to the client: a tampered scope file that lets testing reach an excluded rail signalling host is first; a spoofed dashboard login that leaks coverage charts is lower. The ranking decides which mitigations land before the next engagement.

### Exercises

- **EX067 — Fail open.** Describe one test that proves fail-closed. Rubric: 3 = remove policy, expect deny+alert; 2 = idea; 1 = vague; 0 = none.
- **EX068 — STRIDE row.** Write mitigation for repudiation on deny events. Rubric: 3 = authenticated actor + immutable log; 2 = logging only; 1 = vague; 0 = none.
- **EX069 — Boundary.** Why doesn't platform STRIDE justify an exploit module? Rubric: 3 = different goal/safety boundary; 2 = partial; 1 = justifies it; 0 = none.

### Synthesis

Analyse how your platform can hurt the client or lie; mitigate those first.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Authorized offensive security and red team: methods I

### Learning outcomes

You will (1) sequence pre-engagement → discovery → validation → reporting per PTES/SP 800-115; (2) pick methods that match authorization; (3) define "done" for a method without a shell.

### 24.1 Sequence

Pre-engagement produces the signed ROE. Discovery enumerates in-scope assets by agreed methods. Validation confirms configuration issues with least privilege. Reporting delivers findings and evidence hashes. Skipping pre-engagement is how unauthorized testing happens.

### 24.2 Method cards

Each method card: name, purpose, required privilege, noisy?, stop conditions, expected artefacts. "Authenticated configuration review" is a card; "weaponised exploit" is not in this programme's deck.

### 24.3 Done means artefacts

A method is done when its artefacts exist: inventory CSV, config excerpts, finding drafts, coverage update — not when someone "feels finished".

```python
"""Rebuild a synthetic engagement timeline from event records."""
events = [
    ("09:00", "ROE brief signed", "auth"),
    ("09:15", "scoped host inventory loaded (12 hosts)", "prep"),
    ("10:02", "service enumeration on 10.20.1.0/28", "enum"),
    ("10:45", "finding SYN-001 noted on staging UI", "find"),
    ("11:10", "stop: host 10.20.0.1 probed — out of scope", "stop"),
    ("11:12", "escalated to client contact; confirmed deny-list", "comm"),
    ("13:00", "resume on in-scope hosts only", "auth"),
    ("15:30", "debrief draft shared with client", "report"),
]
# print chronological with phase tags; compute stop latency
print("phase timeline:")
for t, msg, phase in events:
    print(f"  {t} [{phase:6}] {msg}")
t0 = 10*60+45; t1 = 11*60+10
print(f"minutes from SYN-001 note to stop: {t1-t0}")
print(f"stop reason present: yes")
print(f"events={len(events)} phases={len(set(p for _,_,p in events))}")
```

Expected output:

```text
phase timeline:
  09:00 [auth  ] ROE brief signed
  09:15 [prep  ] scoped host inventory loaded (12 hosts)
  10:02 [enum  ] service enumeration on 10.20.1.0/28
  10:45 [find  ] finding SYN-001 noted on staging UI
  11:10 [stop  ] stop: host 10.20.0.1 probed — out of scope
  11:12 [comm  ] escalated to client contact; confirmed deny-list
  13:00 [auth  ] resume on in-scope hosts only
  15:30 [report] debrief draft shared with client
minutes from SYN-001 note to stop: 25
stop reason present: yes
events=8 phases=7
```

> **Synthetic case — Riverstone Transit.** The timeline lab shows a stop at 11:10 and resume after confirmation — the method card required that path.

### 24.4 Errors and limits

Copying someone else's method list without matching authorization is cargo-cult PTES.

### 24.2b Quiet vs noisy methods

Quiet methods (authenticated reads, config export) fit daytime windows on shared systems. Noisy methods (broad service enumeration) need tighter rate limits and often off-peak hours. The method card's "noisy?" field drives the schedule; leaving it blank is how morning dispatch windows get congested.

### 24.3b Method freeze

During an engagement window, adding a new method mid-flight needs the same authorization path as a scope widen. "While we were here we also tried…" is how ROE drift happens. Park ideas in the next engagement's planning backlog.

### 24.1b Method dependencies

Some methods require outputs of others (inventory before authenticated review). Encode dependencies in the plan so the timeline does not schedule the review on day one against an empty asset list. PulseMap can show blocked-by links for planned techniques.


### 24.4b Reviewing a method card

Before a method card enters the catalogue, a second engineer reads it as if they had never seen the method: is the purpose clear, are stop conditions observable, does it name the evidence it produces? Sam's first card for passive service inventory came back with one change: the stop condition "if the network seems slow" became "if the client's monitoring reports latency above the agreed threshold."

### Exercises

- **EX070 — Card.** Write a method card for authenticated web config review. Rubric: 3 = all fields filled safely; 2 = missing one; 1 = includes exploit; 0 = none.
- **EX071 — Sequence error.** What is wrong with discovery before signed ROE? Rubric: 3 = unauthorized testing; 2 = process vague; 1 = "bad order"; 0 = none.
- **EX072 — Timeline.** From the lab, what should appear in the report about 11:10–11:12? Rubric: 3 = out-of-scope probe, stop, escalate, confirm; 2 = stop only; 1 = omit; 0 = wrong.

### Synthesis

Methods are authorized, carded and done when artefacts exist.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) sketch TrackScope's allow/deny pipeline; (2) justify trade-offs in a short design review; (3) produce a one-page decision record.

### 25.1 Studio problem

Design the pipeline: input action → load ScopeVersion → evaluate predicate → emit event → return decision. Competitors: embed policy in code vs data file; sync vs async events.

### 25.2 Trade-offs

Policy-as-data lets ROE updates ship without redeploying binaries but needs signature verification. Async events scale but can reorder; for deny-list hits, prefer sync alert.

### 25.3 Decision record

One page: context, options, decision, consequences, date, owners. Store next to the code.

> **Synthetic case — Riverstone Transit.** Studio chose policy-as-signed-JSON, sync path for denies, async bulk for allows. ADR-004 captures it.

### 25.4 Errors and limits

Studios that skip safety requirements produce pretty diagrams that fail open.

### 25.2b Sketch quality bar

A studio sketch must name trust boundaries, data stores, and the fail-closed path in writing — not only boxes and arrows. If a reviewer cannot point to where DENY happens when policy is missing, the sketch is incomplete. Ten minutes of labelling beats an hour of aesthetic layout.

### 25.3b Facilitator role

Studios need a facilitator who watches for safety omissions and empty scores while teams debate latency. The facilitator can pause the room with a single question: "Where do we DENY if policy is missing?" If nobody can answer, architecture is not ready.

### 25.1b Constraint cards

Hand each studio team physical or digital constraint cards: residency, two-engineer ops, fail-closed, no empty scores. Designs that violate a card are rejected before aesthetic debate starts. Cards rotate across studios so teams practice different constraints.

### Practice note

Each studio ends with a gallery: teams post ADR drafts and other teams try to find a fail-open path in five minutes. Finding one is success for the reviewers, not failure for the authors — provided the path is fixed before the next milestone. The competitive energy goes into safety hunting rather than slide polish, which is the point of Design Studio I and II in this programme.

### Exercises

- **EX073 — Options.** Name two options for policy delivery and one risk each. Rubric: 3 = two options + risks; 2 = options only; 1 = one; 0 = none.
- **EX074 — ADR.** Write the Decision line for sync deny alerts. Rubric: 3 = clear decision + why; 2 = decision only; 1 = vague; 0 = none.
- **EX075 — Review ask.** List three questions a reviewer must ask. Rubric: 3 = fail-closed, authn of policy, performance under flood; 2 = two; 1 = one; 0 = none.

### Synthesis

Studio work ends in a recorded decision, not a vibe.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Authorized offensive security and red team: architecture alternatives

### Learning outcomes

You will (1) compare monolith vs service split for assessment tools; (2) evaluate a "scanner in the cloud" option against data-residency rules; (3) pick an alternative with an explicit rejection of the others.

### 26.1 Alternatives

A: monolith on a hardened jump host. B: TrackScope / FindingsDesk / PulseMap as separate services. C: SaaS scanner with client data leaving the premises. Each serves different constraints.

### 26.2 Criteria

Authorization clarity, data residency, fail-closed behaviour, operability by two engineers, cost. Weight safety and residency above novelty.

### 26.3 Decision

Riverstone rejected C because fare and staff identity logs must not leave the region. Chose B for independent scaling of reporting, with A as the disaster-fallback (export policy files and run local).

> **Synthetic case — Riverstone Transit.** A vendor demo of C looked slick; counsel blocked it on residency. ADR-011 records the rejection so the question is not reopened monthly.

### 26.4 Errors and limits

Alternatives analysis that ignores the ROE's data clauses is theatre.

### 26.2b Switching costs

Architecture alternatives include the cost of changing your mind later. A monolith that already exports signed policy files can grow into services; a SaaS contract with residency exceptions is harder to unwind mid-incident. Prefer options that keep an offline escape hatch for deny/allow.

### 26.3b Exit criteria for alternatives

An alternatives analysis ends with a decision, rejected options with reasons, and a revisit trigger ("reopen if residency law changes"). Without a revisit trigger, people re-argue C every sprint.

### 26.1b Cost models

Include rough annual cost (compute, seats, staff time for dual approval). An alternative that needs six FTEs to operate fail-closed is not free because the license was cheap. Cost belongs in the decision record beside safety.

### Practice note

Document the skills your chosen alternative demands. Option B's service split needs on-call engineers who understand event ordering; if the squad lacks that skill, budget training or prefer a simpler option until hiring catches up. Architecture that assumes unavailable skills fails closed in theory and fails open in practice when nobody can operate the deny path under stress.

### Exercises

- **EX076 — Criterion.** Add one criterion for radio assessments and score A/B/C. Rubric: 3 = sensible criterion + scores; 2 = criterion only; 1 = vague; 0 = none.
- **EX077 — Reject C.** Write the rejection sentence with the residency reason. Rubric: 3 = clear; 2 = partial; 1 = cost only; 0 = accepts C.
- **EX078 — Fallback.** When is monolith A the right runtime? Rubric: 3 = outage/isolation drill with exported policy; 2 = vague; 1 = always; 0 = never.

### Synthesis

Choose architecture against weighted constraints; record rejected options.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Authorized offensive security and red team: control design

### Learning outcomes

You will (1) design preventive, detective and corrective controls for the platform; (2) bind controls to requirements; (3) avoid controls that require exploit skills to operate.

### 27.1 Three kinds

Preventive: scope predicate before action. Detective: alert on deny-list hit. Corrective: auto-disable assessment account at window end. Each maps to a requirement id.

### 27.2 Operator skill

Controls must be operable by engineers who follow runbooks — not only by exploit specialists. A control that needs a custom shellcode to verify is the wrong control for this programme.

### 27.3 Compensation

If preventive control is weak (legacy system cannot enforce port scope), add detective monitoring and a tighter human approval. Document the compensation in the ROE.

```python
"""Evaluate proposed actions against synthetic rules of engagement."""
ROE = {
    "hours": ("09:00", "17:00"),
    "deny_actions": {"denial-of-service", "phishing-staff", "exfiltrate-real-data"},
    "require_approval": {"password-spray-lab", "privilege-escalation-lab"},
    "max_concurrency": 5,
}
proposals = [
    ("service-enum", "10:30", 3, False),
    ("denial-of-service", "10:30", 1, False),
    ("password-spray-lab", "10:30", 2, False),
    ("password-spray-lab", "10:30", 2, True),
    ("service-enum", "18:00", 2, False),
    ("service-enum", "11:00", 20, False),
]

def ok_time(t):
    return ROE["hours"][0] <= t <= ROE["hours"][1]

for action, when, conc, approved in proposals:
    reasons=[]
    if action in ROE["deny_actions"]: reasons.append("deny-action")
    if action in ROE["require_approval"] and not approved: reasons.append("needs-approval")
    if not ok_time(when): reasons.append("outside-hours")
    if conc > ROE["max_concurrency"]: reasons.append("concurrency")
    print(f"action={action:20} when={when} conc={conc:2} approved={approved} -> {'ALLOW' if not reasons else 'DENY'} {','.join(reasons) or '-'}")
```

Expected output:

```text
action=service-enum         when=10:30 conc= 3 approved=False -> ALLOW -
action=denial-of-service    when=10:30 conc= 1 approved=False -> DENY deny-action
action=password-spray-lab   when=10:30 conc= 2 approved=False -> DENY needs-approval
action=password-spray-lab   when=10:30 conc= 2 approved=True -> ALLOW -
action=service-enum         when=18:00 conc= 2 approved=False -> DENY outside-hours
action=service-enum         when=11:00 conc=20 approved=False -> DENY concurrency
```

> **Synthetic case — Riverstone Transit.** Password-spray-lab is denied unless approved — preventive gate with a detective event when someone tries without approval.

### 27.4 Errors and limits

Stacks of compensating controls without an owner become ignored alerts.

### 27.2b Control ownership

Every control has an owner who receives its alerts and a review date. Orphan detective controls become noise; orphan preventive controls become folklore nobody dares to change. Put owner and review date in the same repo as the control code.

### 27.3b Testing controls

Each control needs a negative test: remove it or break it in a lab and show the bad outcome is caught by a higher control or by fail-closed defaults. Untested controls are wishes.

### 27.1b Detecting control bypass

Log when an operator uses break-glass to skip dual approval. Break-glass without detection is just a hidden single control. Weekly review of break-glass events is part of the control design.

### Practice note

Controls degrade. Schedule a quarterly control-health day: break each preventive control in a synthetic lab and confirm detective controls fire. Record the date next to the control owner. A control that has never been broken on purpose is a control you are only hoping works, and hope is not an engineering control in an authorized assessment platform.

### Exercises

- **EX079 — Map.** Give one preventive and one detective control for evidence tampering. Rubric: 3 = both (e.g. sealed store + hash mismatch alert); 2 = one; 1 = vague; 0 = none.
- **EX080 — Operable.** Why is "verify by exploiting again" a bad control? Rubric: 3 = dual-use + unstable + wrong skill; 2 = one reason; 1 = vague; 0 = defends it.
- **EX081 — Lab.** Which ROE rule blocks concurrency 20? Rubric: 3 = concurrency limit; 2 = vague deny; 1 = wrong; 0 = none.

### Synthesis

Controls are preventive/detective/corrective, owned, and operable without exploits.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Authorized offensive security and red team: implementation I

### Learning outcomes

You will (1) implement allowed() with explicit reason codes; (2) add tests for each clause; (3) log without storing secrets.

### 28.1 Implementation shape

Pure function: inputs host, port, ScopeVersion → (allow: bool, reason: str). No network I/O inside the predicate; I/O belongs to the caller. That keeps tests fast and free of client contact.

### 28.2 Clause tests

One test file per clause: cidr, deny-list, port, hours, concurrency, approval flag. Synthetic fixtures only. Mutation: break a clause and watch the test fail.

```python
"""Check proposed engagement targets against a written scope (synthetic)."""
SCOPE_CIDRS = [("10.20.0.0", 16), ("192.168.50.0", 24)]  # inclusive synthetic ranges
SCOPE_PORTS = {22, 80, 443, 8080}
DENY_HOSTS = {"10.20.0.1", "192.168.50.1"}  # out-of-scope infra

def ip_int(s):
    a,b,c,d = map(int, s.split("."))
    return (a<<24)|(b<<16)|(c<<8)|d

def in_cidr(ip, net, bits):
    mask = (0xFFFFFFFF << (32-bits)) & 0xFFFFFFFF
    return (ip_int(ip) & mask) == (ip_int(net) & mask)

def check(host, port):
    reasons = []
    if host in DENY_HOSTS:
        reasons.append("deny-list")
    if not any(in_cidr(host, n, b) for n,b in SCOPE_CIDRS):
        reasons.append("outside-cidr")
    if port not in SCOPE_PORTS:
        reasons.append("port-not-in-scope")
    return ("ALLOW" if not reasons else "DENY"), reasons

tests = [
    ("10.20.1.10", 443),
    ("10.20.0.1", 443),
    ("192.168.50.20", 22),
    ("192.168.50.20", 3389),
    ("8.8.8.8", 80),
    ("192.168.1.10", 80),
]
for h,p in tests:
    v, r = check(h,p)
    print(f"target={h}:{p} decision={v} reasons={','.join(r) or '-'}")
```

Expected output:

```text
target=10.20.1.10:443 decision=ALLOW reasons=-
target=10.20.0.1:443 decision=DENY reasons=deny-list
target=192.168.50.20:22 decision=ALLOW reasons=-
target=192.168.50.20:3389 decision=DENY reasons=port-not-in-scope
target=8.8.8.8:80 decision=DENY reasons=outside-cidr
target=192.168.1.10:80 decision=DENY reasons=outside-cidr
```

### 28.3 Logging

Log decision, reason, policy version, actor. Do not log tokens or passwords. Redact query parameters that might contain secrets.

> **Synthetic case — Riverstone Transit.** Implementation I shipped reason codes that the timeline UI shows — operators finally saw *why* a probe stopped.

### 28.4 Errors and limits

Stringly-typed reasons drift; use an enum shared with PulseMap.

### 28.2b Reason-code catalogue

Publish the enum of reason codes as a versioned document PulseMap and operators share: `outside-cidr`, `deny-list`, `port-not-in-scope`, `outside-hours`, `concurrency`, `needs-approval`, `policy-unavailable`. Unknown codes must fail closed in consumers, not display as "OK".

### 28.3b Fuzzing inputs

Feed the predicate random hosts, ports and broken UTF-8. It must DENY or error closed, never throw uncaught and never ALLOW on parse failure. A five-minute fuzz harness in CI catches embarrassing crashes before an engagement does.

### 28.1b Property-based hours

For the hours gate, generate random timestamps across a week and assert DENY outside the ROE window and ALLOW inside (with other clauses satisfied). Example tests miss timezone edges that property tests catch.

### Practice note

Code review checklists for predicate changes include: new clause? new tests? reason-code docs? fuzz case? fail-closed on parse error? Reviewers who skip the list are doing social review, not safety review. TrackScope's deny path is the wrong place for informal LGTM culture; the checklist is short on purpose so it actually gets used under time pressure.

### Exercises

- **EX082 — Signature.** Write the type signature of allowed and explain why ScopeVersion is an argument. Rubric: 3 = signature + version pin reason; 2 = signature; 1 = vague; 0 = none.
- **EX083 — Mutation.** Which test fails if deny-list membership is ignored? Rubric: 3 = deny-list fixture expects DENY; 2 = vague; 1 = wrong; 0 = none.
- **EX084 — Redact.** Give two log fields to redact. Rubric: 3 = e.g. Authorization header, password query param; 2 = one; 1 = vague; 0 = none.

### Synthesis

Pure predicate, clause tests, safe logs.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Authorized offensive security and red team: measurement

### Learning outcomes

You will (1) define coverage with a denominator; (2) separate activity metrics from outcome metrics; (3) publish a measurement that can be wrong in only one direction.

### 29.1 Coverage needs a plan

ATT&CK coverage is observed ∩ planned / |planned|, not observed / |all ATT&CK|. Without a plan, "coverage" is vanity. PulseMap requires a planned set per engagement.

```python
"""ATT&CK-style coverage matrix over synthetic authorized techniques (names only)."""
# Synthetic engagement log: technique_id -> observed (True/False)
PLAN = ["T1046", "T1595", "T1082", "T1083", "T1059", "T1078", "T1021"]
OBSERVED = {"T1046", "T1595", "T1082", "T1083", "T1078"}
LABELS = {
    "T1046": "Network Service Discovery",
    "T1595": "Active Scanning",
    "T1082": "System Information Discovery",
    "T1083": "File and Directory Discovery",
    "T1059": "Command and Scripting Interpreter",
    "T1078": "Valid Accounts",
    "T1021": "Remote Services",
}
covered = 0
for tid in PLAN:
    hit = tid in OBSERVED
    covered += hit
    print(f"{tid} {LABELS[tid]:34} {'COVERED' if hit else 'PLANNED-NOT-SEEN'}")
print(f"coverage={covered}/{len(PLAN)} ({100*covered/len(PLAN):.0f}%)")
```

Expected output:

```text
T1046 Network Service Discovery          COVERED
T1595 Active Scanning                    COVERED
T1082 System Information Discovery       COVERED
T1083 File and Directory Discovery       COVERED
T1059 Command and Scripting Interpreter  PLANNED-NOT-SEEN
T1078 Valid Accounts                     COVERED
T1021 Remote Services                    PLANNED-NOT-SEEN
coverage=5/7 (71%)
```

### 29.2 Activity vs outcome

Activity: tools launched, packets sent. Outcome: verified remediations, SLA breaches closed, out-of-scope probes. Steer on outcomes; use activity only for capacity planning.

### 29.3 One-sided error

Prefer metrics that, if wrong, under-claim success (e.g. count a fix only after re-test). Over-claiming security is the failure mode Albrecht and Jensen attack.

> **Synthetic case — Riverstone Transit.** Coverage 5/7 (71%) with two planned-not-seen — the report said "incomplete planned coverage", not "71% safe".

### 29.4 Errors and limits

Denominators stolen from another engagement invalidate the metric.

### 29.2b Sampling without lying

If you sample 50 of 500 hosts, say so and do not scale the finding count as if you visited all 500. Stratify by exposure when possible (Chapter 11 inventory). A honest sample with a confidence note beats a fake census.

### 29.3b Dashboards as arguments

Every dashboard widget is a claim. Caption widgets with the formula and the engagement id. A widget without a formula is decoration and should be removed in review.

### 29.1b Cohort comparisons

Comparing coverage across engagements requires the same planning rules. Publish the planning guide beside PulseMap so "71%" in March means the same kind of denominator as "71%" in September.

### Practice note

When leadership asks for a trend line, give them the same formula across engagements and mark methodology changes with vertical lines on the chart. A smooth upward coverage curve that hides a denominator change is a reporting failure. PulseMap exports include a methodology_id field so dishonest joins across incompatible plans are harder to automate.

### Exercises

- **EX085 — Formula.** Write PulseMap's coverage formula and plug in the lab numbers. Rubric: 3 = 5/7; 2 = formula only; 1 = 5/all ATT&CK; 0 = none.
- **EX086 — Metric pick.** Choose outcome metric for remediation quality. Rubric: 3 = e.g. % critical fixed within SLA with re-test; 2 = activity metric; 1 = vague; 0 = none.
- **EX087 — Under-claim.** Give one design that under-claims success. Rubric: 3 = require re-test before closed; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Plan the denominator; measure outcomes; prefer under-claim.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) run a verification plan against TrackScope; (2) record pass/fail with evidence hashes; (3) stop the lab if a safety test fails.

### 30.1 Plan

Tests: allow in-scope; deny deny-list; deny bad port; fail-closed missing policy; hours gate; concurrency gate. Each row: id, setup, action, expected, evidence path.

### 30.2 Execution

Use synthetic hosts only. Capture stdout and config hashes. Any safety failure (fail-open) stops the lab and opens a blocker ticket — no "continue to gather data".

```python
"""Evaluate proposed actions against synthetic rules of engagement."""
ROE = {
    "hours": ("09:00", "17:00"),
    "deny_actions": {"denial-of-service", "phishing-staff", "exfiltrate-real-data"},
    "require_approval": {"password-spray-lab", "privilege-escalation-lab"},
    "max_concurrency": 5,
}
proposals = [
    ("service-enum", "10:30", 3, False),
    ("denial-of-service", "10:30", 1, False),
    ("password-spray-lab", "10:30", 2, False),
    ("password-spray-lab", "10:30", 2, True),
    ("service-enum", "18:00", 2, False),
    ("service-enum", "11:00", 20, False),
]

def ok_time(t):
    return ROE["hours"][0] <= t <= ROE["hours"][1]

for action, when, conc, approved in proposals:
    reasons=[]
    if action in ROE["deny_actions"]: reasons.append("deny-action")
    if action in ROE["require_approval"] and not approved: reasons.append("needs-approval")
    if not ok_time(when): reasons.append("outside-hours")
    if conc > ROE["max_concurrency"]: reasons.append("concurrency")
    print(f"action={action:20} when={when} conc={conc:2} approved={approved} -> {'ALLOW' if not reasons else 'DENY'} {','.join(reasons) or '-'}")
```

Expected output:

```text
action=service-enum         when=10:30 conc= 3 approved=False -> ALLOW -
action=denial-of-service    when=10:30 conc= 1 approved=False -> DENY deny-action
action=password-spray-lab   when=10:30 conc= 2 approved=False -> DENY needs-approval
action=password-spray-lab   when=10:30 conc= 2 approved=True -> ALLOW -
action=service-enum         when=18:00 conc= 2 approved=False -> DENY outside-hours
action=service-enum         when=11:00 conc=20 approved=False -> DENY concurrency
```

### 30.3 Report

A one-page lab report: environment version, table of results, open blockers, sign-off. Attach hashes.

> **Synthetic case — Riverstone Transit.** Lab I failed the missing-policy row once; release halted until S-3 was fixed (Chapter 21).

### 30.4 Errors and limits

Labs on shared clients collide; book the synthetic range.

### 30.2b Golden fixtures

Keep a sealed directory of synthetic fixtures with known expected decisions. Lab runs must hash-match the fixture set before they count as release evidence. Fixtures drift when someone "fixes" them to match a buggy build — protect them with CODEOWNERS.

### 30.3b Independent runner

Lab I is run by someone who did not implement the change under test. Pairing is fine for debugging afterward; the recorded pass needs an independent green checklist.

### 30.1b Lab data retention

Lab result logs are evidence; retain them with the release tag. Deleting green lab logs to save space destroys the ability to investigate a later regression.

### Practice note

Photograph or export the lab environment inventory (package versions, kernel, policy key ids) into the lab report. It passed on my machine without inventory is not transferable evidence. Lab I exists to create transferable confidence for people who were not in the room, including your future self during an incident review six months later.


### 30.4b What the first lab run proved

The first verification run proved that TrackScope denies every out-of-scope address in the golden fixture set and logs each denial with the rule that fired. It did not prove behaviour under concurrent requests or with malformed scope files; Sam lists those as open items for Laboratory II.

### Exercises

- **EX088 — Row.** Write the fail-closed lab row. Rubric: 3 = complete row; 2 = partial; 1 = vague; 0 = none.
- **EX089 — Stop rule.** What happens on fail-open? Rubric: 3 = stop, blocker, no engagement use; 2 = note only; 1 = continue; 0 = none.
- **EX090 — Evidence.** Name three hashes to attach. Rubric: 3 = policy, binary/version, result log; 2 = two; 1 = one; 0 = none.

### Synthesis

Verify safety first; stop on fail-open; hash everything.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Authorized offensive security and red team: implementation II

### Learning outcomes

You will (1) add idempotent finding upserts; (2) enforce schema validation on write; (3) version API responses.

### 31.1 Upsert

PUT /findings/{id} with full body; same id twice yields one row. Dedup fingerprints (Chapter 9) propose ids, humans confirm.

```python
"""Deduplicate synthetic findings by a stable fingerprint (asset, weakness class, location)."""
import hashlib
raw = [
    ("web-01", "missing-header", "/login"),
    ("web-01", "missing-header", "/login"),
    ("web-01", "missing-header", "/account"),
    ("web-02", "default-credential", "admin-ui"),
    ("web-02", "default-credential", "admin-ui"),
    ("db-01", "weak-tls", "5432"),
]
seen = {}
for asset, cls, loc in raw:
    fp = hashlib.sha256(f"{asset}|{cls}|{loc}".encode()).hexdigest()[:10]
    seen.setdefault(fp, [asset, cls, loc, 0])[3] += 1
print(f"raw={len(raw)} unique={len(seen)}")
for fp, (a, c, l, n) in sorted(seen.items(), key=lambda x: x[1]):
    print(f"{fp} {a:7} {c:19} {l:9} occurrences={n}")
```

Expected output:

```text
raw=6 unique=4
f9bb6de442 db-01   weak-tls            5432      occurrences=1
66fb6f1d56 web-01  missing-header      /account  occurrences=1
c4bfba3b72 web-01  missing-header      /login    occurrences=2
296a3331f0 web-02  default-credential  admin-ui  occurrences=2
```

### 31.2 Validate on write

Reject unknown fields and forbidden names; coerce severity through an enum. Validation errors return machine-readable codes for the UI.

### 31.3 API versioning

Prefix /v1/; additive changes only within v1. Breaking changes require /v2/ and a migration note for PulseMap.

> **Synthetic case — Riverstone Transit.** A mobile client sent `risk_score`; validator rejected it — empty scores stay out (Chapter 15).

### 31.4 Errors and limits

Idempotency keys must not be derived from wall-clock alone.

### 31.2b Partial updates

PATCH that allows severity changes without evidence references invites silent downgrades. Prefer full PUT of the validated body, or a restricted PATCH that cannot clear evidence hashes or change status to closed without a re-test pointer.

### 31.3b Bulk import

Bulk finding import from scanners must pass the same schema validation as interactive create, including forbidden-field checks and fingerprint idempotency. A separate "trusted import" path is how payloads sneak into the store.

### 31.1b Optimistic concurrency

Use ETags or version numbers on findings so two remediators do not clobber each other. A lost update that clears a re-test pointer looks like a mysterious reopen later.

### Practice note

Bulk deletes are forbidden without dual control. Soft-delete with reason is the default path; hard purge follows retention only. API clients that issue DELETE in a loop during a buggy retry get their credentials revoked automatically after a threshold — another place where reliability and safety meet.



Document the upsert semantics in the OpenAPI description so mobile clients do not invent their own retry ids.


### 31.4b Migration of stored findings

When the findings schema gains a field, existing FindingsDesk records need a default or a backfill. Sam writes the migration to run on a copy first, compares record counts and checksums before and after, and keeps the old schema readable for one release.

### Exercises

- **EX091 — Upsert.** Why is POST-without-id risky for retries? Rubric: 3 = duplicates on retry; 2 = vague; 1 = wrong; 0 = none.
- **EX092 — Reject.** Give a JSON body that must 400. Rubric: 3 = contains payload/password/risk_score etc.; 2 = weak; 1 = valid body; 0 = none.
- **EX093 — Version.** Is renaming reason_code → reason a v1-safe change? Rubric: 3 = no, breaking → v2; 2 = hesitant; 1 = yes; 0 = none.

### Synthesis

Idempotent writes, strict schema, explicit versions.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Authorized offensive security and red team: reliability

### Learning outcomes

You will (1) set availability targets for assessment tools; (2) use retries with budgets; (3) degrade safely when a dependency fails.

### 32.1 Targets

TrackScope deny path: high availability during engagement windows. PulseMap dashboards: best-effort. State the target; do not imply five-nines without a budget.

### 32.2 Retries

Retries help flaky uploads (Chapter 6) but need a deadline and jitter. Cap total attempts so the ROE rate limit still holds.

```python
"""Reliability of a synthetic evidence-upload step with retries (deterministic)."""
import random
random.seed(7)
P_FAIL = 0.2
def upload_attempts(max_tries):
    for t in range(1, max_tries + 1):
        if random.random() > P_FAIL:
            return True, t
    return False, max_tries
for tries in (1, 2, 3, 5):
    random.seed(7)
    ok = sum(upload_attempts(tries)[0] for _ in range(1000))
    print(f"max_tries={tries} success={ok}/1000 theory={1-P_FAIL**tries:.4f}")
```

Expected output:

```text
max_tries=1 success=784/1000 theory=0.8000
max_tries=2 success=949/1000 theory=0.9600
max_tries=3 success=988/1000 theory=0.9920
max_tries=5 success=1000/1000 theory=0.9997
```

### 32.3 Safe degradation

If FindingsDesk is down, continue deny/allow locally and queue finding drafts on disk — never fail open on scope checks.

> **Synthetic case — Riverstone Transit.** During a FindingsDesk outage, Sam's laptop queue held 14 drafts; TrackScope keeps denying out-of-scope.

### 32.4 Errors and limits

Retries against a rate-limited API can look like abuse; coordinate budgets with the ROE.

### 32.2b Back-pressure

When the draft queue grows past a threshold, stop starting new discovery methods and page the lead. Continuing to scan while findings cannot be recorded creates untracked risk. Back-pressure is a safety feature, not only a performance feature.

### 32.3b Chaos in synthetic only

Reliability experiments (kill pods, partition networks) run in the synthetic range. Never chaos-test during a client's signed window. Record experiment ids separately from engagement ids so metrics do not mix.

### 32.1b Dependency health checks

TrackScope should health-check policy storage and event sink at start of window. Starting an engagement blind and discovering a broken sink mid-scan is an operations failure the reliability chapter is meant to prevent.

### Practice note

Define error budgets for the deny path separately from best-effort UI budgets. Burning the UI budget on a fancy dashboard is acceptable; burning the deny budget on the same work is not. Publish both budgets so product pressure has a number to argue with instead of a vague plea for more reliability.


### 32.4b Measuring whether targets were met

An availability target is only meaningful if it is measured. TrackScope records every deny or allow decision with a timestamp, so the team can compute the share of engagement-window minutes in which the service answered within its latency budget. Last month's synthetic report showed 99.6% against a 99.5% target.

### Exercises

- **EX094 — Target.** Write an availability sentence for TrackScope deny path. Rubric: 3 = windowed target + measure; 2 = vague high; 1 = five-nines joke; 0 = none.
- **EX095 — Budget.** With p=0.8 and max 3 tries, expected attempts? Rubric: 3 ≈ 1.248 with working; 2 = 1/p; 1 = 3; 0 = none.
- **EX096 — Degrade.** What must never degrade to ALLOW? Rubric: 3 = scope/policy decisions; 2 = partial; 1 = findings UI; 0 = wrong.

### Synthesis

Reliable denies, budgeted retries, degrade closed.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Authorized offensive security and red team: safety and resilience

### Learning outcomes

You will (1) write stop conditions as executable checks; (2) plan rollback of tool changes mid-engagement; (3) run a tabletop on a deny-list miss.

### 33.1 Executable stops

Stop conditions are code: deny-list, latency canary, client kill-switch file. Humans also call stop; software must not disagree with a human stop.

### 33.2 Rollback

Pin releases; keep previous TrackScope binary signed. If a new build mis-evaluates scope, roll back within minutes, not "after the sprint".

### 33.3 Tabletop

Walk the 11:10 timeline: who is called, what is said, what is logged, when resume is allowed. Update the runbook where the tabletop stuck.

> **Synthetic case — Riverstone Transit.** Tabletop found the kill-switch file path undocumented; runbook v1.4 fixed it before the next window.

### 33.4 Errors and limits

Resilience theatre is a binder nobody opens. Drill once per term.

### 33.2b Communication templates

Pre-write the SMS/email for stop, for resume, and for rollback. Under stress people improvise and omit the ROE version or the next checkpoint time. Templates live in the runbook and are tested in the tabletop.

### 33.3b Resume authority

Who may resume after a stop? Name the role in the ROE. TrackScope should require a resume token tied to that role and ScopeVersion, not a Boolean flip anyone on the jumphost can toggle.

### 33.1b Secondary contacts

Stop conditions that page only one person fail when that person is offline. Maintain primary and secondary contacts with acknowledged handoff, tested in the tabletop.

### Practice note

After every real stop, run a five-minute hotwash: what fired, what lagged, what confused the client. File at least one runbook edit when possible. Stops that produce no documentation updates will recur with the same confusion, and the timeline will look identical to the chapter's 11:10 example for the wrong reasons.


### 33.4b Proving the stop button works

Before each engagement, the lead presses the stop control in the synthetic range and checks that every running method halts within the time written in the ROE. The result, with the measured time, is attached to the engagement record; an untested stop is treated as no stop.

### Exercises

- **EX097 — Kill switch.** Design a human kill switch TrackScope honors in ≤30s. Rubric: 3 = mechanism + check interval + fail closed; 2 = idea; 1 = vague; 0 = none.
- **EX098 — Rollback.** List three preconditions to roll back mid-engagement. Rubric: 3 = prior binary, policy pin, notify client; 2 = two; 1 = one; 0 = none.
- **EX099 — Tabletop ask.** Write one inject for the tabletop. Rubric: 3 = specific inject; 2 = vague; 1 = none; 0 = unsafe inject.

### Synthesis

Stops you can run, rollbacks you can do, tabletops that update runbooks.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Authorized offensive security and red team: integration

### Learning outcomes

You will (1) integrate TrackScope events into FindingsDesk; (2) define idempotent consumers; (3) test contracts with fixtures.

### 34.1 Event contract

Deny/allow events: schema version, ids, timestamps (UTC), targets, reasons. Consumers ignore unknown fields; producers stay additive.

### 34.2 Idempotent consumers

FindingsDesk keys processed events by event_id. Replaying the log must not create duplicate findings.

### 34.3 Contract tests

Fixture JSON for each reason code; consumer tests assert resulting ticket fields. Run in CI on synthetic fixtures.

> **Synthetic case — Riverstone Transit.** A replay storm duplicated three tickets until event_id idempotency landed.

### 34.4 Errors and limits

Clock skew between hosts muddies timelines; prefer event time + receive time.

### 34.2b Poison events

Consumers must validate schema and reject events with future timestamps, unknown policy versions, or targets that fail format checks. A poisoned event stream should quarantine, not create findings against random hosts.

### 34.3b Schema evolution drill

Practice adding an optional field end-to-end in a dry run: producer, consumer, fixture, docs. Teams that only evolve schemas in emergencies invent incompatible shortcuts.

### 34.1b Dead-letter queues

Events that fail validation go to a dead-letter queue with an alert — not to `/dev/null` and not into findings. Operators replay after fixing the producer. Invisible drops recreate repudiation.

### Practice note

Contract tests run on a schedule against staging fixtures even when no PR is open, catching silent producer drift. A green CI on Monday and a broken consumer on Thursday usually means someone edited a fixture by hand in an environment CI does not see. Scheduled contract tests close that gap.



Include a consumer canary that fails the deploy if poison events are not quarantined within one minute in staging.



Dead-letter age is an SLO chart beside deny-path latency.


### 34.4b Ownership of the event contract

Each event type on the bus has one owning team that approves changes. PulseMap consumes FindingsDesk events but cannot alter their schema; it files a request instead, which keeps the contract stable for every other consumer.

### Exercises

- **EX100 — Field.** Why include policy_version on every event? Rubric: 3 = audit which ROE applied; 2 = vague; 1 = wrong; 0 = none.
- **EX101 — Replay.** How does event_id prevent duplicate findings? Rubric: 3 = upsert/ignore duplicates; 2 = vague; 1 = wrong; 0 = none.
- **EX102 — Fixture.** Name two fixtures required before integrating a new reason code. Rubric: 3 = producer example + consumer expected ticket; 2 = one; 1 = vague; 0 = none.

### Synthesis

Contracts, idempotent consumers, fixture tests.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) redesign PulseMap's coverage UI against under-claim principles; (2) defend the design in a review; (3) produce UI copy that refuses empty scores.

### 35.1 Problem

Stakeholders want a big green percentage. Design a UI that shows planned/observed/not-seen and refuses a single "security score".

### 35.2 Copy

"71% of planned techniques observed — not a residual-risk score." Link to Albrecht & Jensen in the help text. Button: export denominator.

### 35.3 Review

Reviewers try to force a red/yellow/green risk badge; studio must hold the line with measurement chapter rules.

> **Synthetic case — Riverstone Transit.** Studio II killed the badge; the dashboard now lists the two planned-not-seen techniques by id.

### 35.4 Errors and limits

Dark patterns ("just for executives") reintroduce empty scores — reject in CODEOWNERS for UI.

### 35.2b Accessibility of honesty

Under-claiming metrics must still be readable: large type for the fraction, plain language for the caveat, keyboard access to the denominator export. Hiding the caveat in a tooltip reintroduces the empty-score problem for anyone who does not hover.

### 35.3b Export as the source of truth

If the UI and the CSV export disagree, the export wins for the report. Build exports first; treat UI as a view. That removes arguments about what "71%" meant in a screenshot.

### 35.1b Narrative exports

Alongside CSV, export a short Markdown narrative generated from the same query as the UI ("planned 7, observed 5, not seen: T1059, T1021"). Narratives paste into reports without screenshot ambiguity.

### Practice note

User research for PulseMap includes one task: explain this number to a CFO without saying we are safe. If users cannot, the UI copy has failed regardless of visual design. Record those sessions (with consent) as qualitative evidence next to the quantitative coverage formula.


### 35.4b Testing copy with real readers

Sam asks two Riverstone Transit system owners who were not involved in the design to read the report summary aloud and explain what it means. Where they hesitate or misread a severity, the wording changes; reading tests catch ambiguity that reviewers who wrote the text cannot see.

### Exercises

- **EX103 — Copy.** Write the subtitle under the coverage number. Rubric: 3 = denies residual-risk reading; 2 = weak caveat; 1 = none; 0 = implies safety.
- **EX104 — Badge refusal.** One sentence refusing a RAG badge. Rubric: 3 = clear + alternative; 2 = refuse only; 1 = accepts; 0 = none.
- **EX105 — Export.** What columns does denominator export include? Rubric: 3 = technique id, planned, observed, notes; 2 = partial; 1 = just %; 0 = none.

### Synthesis

UI that teaches the metric, not a traffic light of vibes.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Authorized offensive security and red team: performance and scale

### Learning outcomes

You will (1) size scanners under ROE rate limits; (2) apply token buckets; (3) measure client impact with a canary.

### 36.1 Rate limits are first-class

Throughput goals that ignore the ROE are bugs. Size worker pools so the token bucket is the bottleneck, not a surprise 429 storm.

```python
"""Lab R: token-bucket limits against unbounded consumption (synthetic).
Simulates 60 seconds of requests from a normal client and a flooding client
against a model endpoint with a per-client token bucket."""
import random
rng = random.Random(4)
def simulate(rate_per_s, burst, reqs):
    tokens, last, ok = burst, 0.0, 0
    for t in reqs:
        tokens = min(burst, tokens + (t - last) * rate_per_s); last = t
        if tokens >= 1: tokens -= 1; ok += 1
    return ok
normal = sorted(rng.uniform(0, 60) for _ in range(90))
flood = sorted(rng.uniform(0, 60) for _ in range(3000))
for rate, burst in ((5, 20), (2, 10), (1, 5)):
    print(f"limit={rate}/s burst={burst:2d} normal_served={simulate(rate, burst, normal):3d}/90 "
          f"flood_served={simulate(rate, burst, flood):4d}/3000")
```

Expected output:

```text
limit=5/s burst=20 normal_served= 90/90 flood_served= 319/3000
limit=2/s burst=10 normal_served= 90/90 flood_served= 129/3000
limit=1/s burst= 5 normal_served= 62/90 flood_served=  64/3000
```

### 36.2 Token buckets

Capacity = burst; refill = sustained rate. Lab shows flood clients get clipped while normal clients proceed.

### 36.3 Canaries

A synthetic canary request every minute tracks latency/error rate; stop conditions fire on threshold (Chapter 33).

> **Synthetic case — Riverstone Transit.** Bucket 5/s burst 20 kept the fare API under 5% of capacity during the window.

### 36.4 Errors and limits

Distributed scanners need a coordinated global bucket or they N× the limit.

### 36.2b Fairness among methods

When several methods share one bucket, a noisy enumerator can starve a quiet config review. Weight or separate buckets by method class so authorized quiet work still completes inside the window.

### 36.3b Latency budgets

Allocate milliseconds across DNS, TCP, TLS, predicate, event write. When the budget is exceeded, shed work; do not skip the predicate. Publish the budget in the runbook so optimizations have a yardstick.

### 36.1b Warm-up and cool-down

Ramp traffic at window start and drain before hard stop. Instant full-rate starts look like floods to defenders and trip unrelated alerts. Encode ramp in the scheduler, not as tribal knowledge.

### Practice note

Publish a rate-limit economics note: cost of waiting versus cost of a client outage. Most arguments for raising ROE limits dissolve when the outage cost is written down. Keep the note next to the token-bucket config so the next optimization debate starts from numbers.



Separate buckets for quiet versus noisy methods so a hungry enumerator cannot starve config review work.


### 36.4b Load tests that respect the client

Performance tests of TrackScope and the method runners use synthetic targets only. Rates measured there become the ceiling allowed in engagements, always below the client's agreed limit, so speed improvements never translate into more traffic on client systems than was signed for.

### Exercises

- **EX106 — Size.** ROE 2 req/s; each worker does 1 req/s. Max workers? Rubric: 3 = 2 (+ coordinator note); 2 = 2; 1 = many; 0 = none.
- **EX107 — Lab.** At 1/s burst 5, how many flood requests of 3000 were served? Rubric: 3 = 64 from lab; 2 = approx; 1 = all; 0 = none.
- **EX108 — Global.** Why do three uncoordinated scanners break a 5/s ROE? Rubric: 3 = 3× rate; 2 = vague; 1 = deny; 0 = none.

### Synthesis

Bucket first, scale second, canary always.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Authorized offensive security and red team: operations

### Learning outcomes

You will (1) write an engagement runbook; (2) hand over between shifts; (3) manage secrets rotation at close.

### 37.1 Runbook contents

Contacts, ROE pointer, tool versions, stop conditions, escalation tree, evidence paths. Keep it short enough to use under stress.

### 37.2 Handover

Shift log: open findings, last event ids, pending approvals, kill-switch state. Verbal handover plus the log.

### 37.3 Close-out

Disable accounts, rotate secrets, seal evidence, export metrics, schedule retrospective. A checklist beats memory.

```python
"""Age synthetic findings against remediation SLAs by priority."""
SLA = {"critical": 7, "high": 30, "medium": 90, "low": 180}
findings = [
    ("SYN-001", "critical", 3, False),
    ("SYN-005", "critical", 12, False),
    ("SYN-003", "high", 25, False),
    ("SYN-004", "medium", 95, False),
    ("SYN-002", "medium", 40, True),
    ("SYN-006", "low", 200, False),
]
breaches = 0
for fid, pr, age, closed in findings:
    status = "closed" if closed else ("BREACH" if age > SLA[pr] else "open")
    breaches += status == "BREACH"
    print(f"{fid} priority={pr:8} age_days={age:3} sla={SLA[pr]:3} status={status}")
open_n = sum(1 for f in findings if not f[3])
print(f"open={open_n} sla_breaches={breaches}")
```

Expected output:

```text
SYN-001 priority=critical age_days=  3 sla=  7 status=open
SYN-005 priority=critical age_days= 12 sla=  7 status=BREACH
SYN-003 priority=high     age_days= 25 sla= 30 status=open
SYN-004 priority=medium   age_days= 95 sla= 90 status=BREACH
SYN-002 priority=medium   age_days= 40 sla= 90 status=closed
SYN-006 priority=low      age_days=200 sla=180 status=BREACH
open=5 sla_breaches=3
```

> **Synthetic case — Riverstone Transit.** Close-out caught SYN-005 still BREACH past SLA — escalated before the retro.

### 37.4 Errors and limits

Runbooks in wikis nobody can access from the jump host fail; keep an offline copy.

### 37.2b On-call hygiene

On-call for assessment tools is not a license to widen scope. Pages are about tool safety and ROE enforcement; client asset incidents route to the client's IR path. Keep the escalations separate in the runbook so tired engineers do not merge them.

### 37.3b Calendar integration

Engagement windows belong on a shared calendar with ROE version in the description. Accidental overlap of two noisy methods on the same CIDR is an operations failure, not a clever parallelization.

### 37.1b Spare consumables

Ops kits include spare jump-host images, printed contact cards, and offline ROE copies. When SSO is down, the engagement still needs a documented stop path.

### Practice note

Operations metrics include pages per window, mean time to acknowledge stops, and close-out checklist completion. Vanity metrics like hosts touched stay off the ops dashboard. What you measure weekly is what tired engineers will optimize when the client is watching.



Store the close-out checklist result hash in FindingsDesk so incomplete close-outs cannot be marked done quietly.



Handover includes reading the last ten TrackScope denies aloud to the incoming lead.


### 37.4b Measuring the runbook

After each engagement the lead notes which runbook steps were skipped, unclear or out of date. Sam tallies these over a quarter; steps skipped most often are rewritten or removed, and the runbook's revision history shows each change with its reason.

### Exercises

- **EX109 — Checklist.** List six close-out steps. Rubric: 3 = six sensible; 2 = four; 1 = two; 0 = none.
- **EX110 — Handover.** What three fields must the shift log include? Rubric: 3 = findings/events/approvals (or equiv.); 2 = two; 1 = one; 0 = none.
- **EX111 — SLA lab.** How many SLA breaches in the lab? Rubric: 3 = 3; 2 = list without count; 1 = wrong; 0 = none.

### Synthesis

Operate with runbooks, handovers and ruthless close-out.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Authorized offensive security and red team: validation

### Learning outcomes

You will (1) validate fixes with re-tests; (2) avoid validation that reintroduces risk; (3) record negative results.

### 38.1 Re-test design

Same vantage, least privilege, same evidence standard. For default password: confirm login fails; do not spray variants.

### 38.2 Negative results

"Still open" is a valid validation outcome. PulseMap and FindingsDesk must accept it without forcing close.

### 38.3 No new methods

Validation uses the method that found the issue, or a weaker read-only check — not a chance to try new attacks.

> **Synthetic case — Riverstone Transit.** Re-test of SYN-001: default login returned 401; ticket closed with evidence hash. SYN-005 still had group membership — left open.

### 38.4 Errors and limits

Different environment (staging vs prod) means you validated staging.

### 38.2b Sampling re-tests

When many similar findings share a root cause (fleet-wide header missing), re-test a sample plus the originally reported hosts, and say so. Claiming "all 200 closed" after checking five is a measurement lie.

### 38.3b Automating re-test safely

Automated re-tests are allow-listed checks (HTTP status, group membership read) with hard timeouts. They never include credential stuffing or exploit retries. If automation cannot validate safely, schedule a human read-only check.

### 38.1b Evidence of validation

Validation tickets link to the original finding, the method used, the timestamp, and the hash of the new evidence. "Looks good to me" without those fields does not close a critical.

### Practice note

Disputes over validation escalate to a named adjudicator role with access to both evidence hashes. The adjudicator does not re-attack; they compare evidence to the acceptance note. Document the decision in the ticket so the argument does not restart at every status meeting.



Require the re-test method id on every transition to closed for critical and high severities.


### 38.4b Communicating a failed re-test

When a re-test shows a fix did not work, the report says so plainly, includes the evidence and the date, and avoids suggesting blame. The Riverstone Transit owner receives it privately first, so the team can plan a new fix before the result reaches wider governance meetings.

### Exercises

- **EX112 — Re-test.** Steps to validate default-password fix safely. Rubric: 3 = single attempt, expect fail, evidence, no spray; 2 = partial; 1 = spray; 0 = exploit.
- **EX113 — Negative.** Why must "still open" be storable? Rubric: 3 = honesty/SLA; 2 = vague; 1 = always close; 0 = none.
- **EX114 — Env.** One sentence limitation when re-test was staging-only. Rubric: 3 = clear; 2 = vague; 1 = claims prod; 0 = none.

### Synthesis

Validate narrowly; keep negatives; don't widen methods.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Authorized offensive security and red team: maintainability

### Learning outcomes

You will (1) budget for policy and dependency updates; (2) keep adapters thin; (3) document ownership.

### 39.1 Churn

ATT&CK techniques, IdP APIs and ROE templates change. Budget calendar time for updates; pin versions and watch advisories.

### 39.2 Thin adapters

Isolate third-party SDKs behind interfaces so upgrades do not rewrite FindingsDesk core.

### 39.3 Ownership

Every service has a named owning squad and a backup. CODEOWNERS enforces review.

> **Synthetic case — Riverstone Transit.** PulseMap's ATT&CK mapper is an adapter; upgrading the technique list is a data PR, not a rewrite.

### 39.4 Errors and limits

Orphan tools rot into fail-open museums.

### 39.2b Dependency risk

Track libraries that parse CIDRs, YAML policy, or crypto. An RCE in a policy parser is a fail-open incident waiting to happen — pin, monitor CVEs, and prefer small parsers under your tests.

### 39.3b Deletion plan

Maintainability includes knowing how to retire a tool: export dossiers, revoke credentials, archive code, mark PulseMap sources deprecated. Orphan services attract unowned risk.

### 39.1b API deprecation windows

Announce deprecations with dates; keep dual-run periods for PulseMap consumers. Sudden removals of reason codes break timelines mid-engagement.

### Practice note

Write a bus-factor note for each service: who can release, who understands the predicate, who can restore the sealed store. If the answer is one person, schedule cross-training before the next engagement season. Maintainability is mostly about people who are allowed to be on holiday.



Calendar a dependency upgrade month each year so CVE pins do not wait for an emergency.



Ownership pages list vacation coverage by name, not by squad alias.



Treat missing vacation coverage as a release blocker equal to a failing test.



Cross-training sessions use the same synthetic fixtures as Lab I so teaching time also refreshes verification muscle.


### 39.4b Documentation as maintenance

Every module in the platform has a short README stating its purpose, owner, inputs, outputs and the tests that guard it. Sam updates these in the same pull request as code changes; reviewers reject changes that leave the README describing behaviour that no longer exists.

### Exercises

- **EX115 — Pin.** How do you pin TrackScope for an engagement and still allow security patches? Rubric: 3 = version range/policy + re-verify; 2 = partial; 1 = latest always; 0 = none.
- **EX116 — Adapter.** Give one method on a StoragePort interface. Rubric: 3 = e.g. put_evidence(hash,bytes); 2 = vague; 1 = concrete SDK call; 0 = none.
- **EX117 — Owner.** Write the ownership line for FindingsDesk. Rubric: 3 = squad + backup + contact; 2 = squad; 1 = "team"; 0 = none.

### Synthesis

Pins, adapters and named owners keep tools alive safely.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify end-to-end flow from action to ticket to coverage; (2) inject faults; (3) sign a release candidate.

### 40.1 End-to-end

Synthetic action → TrackScope decision → event → FindingsDesk ticket → PulseMap coverage update. Record hashes at each hop.

### 40.2 Faults

Kill FindingsDesk mid-flow; confirm TrackScope still denies and drafts queue. Corrupt an evidence file; confirm hash mismatch alert.

```python
"""Verify integrity of a synthetic evidence package."""
import hashlib, json
files = {
    "roe.pdf": b"SYNTHETIC-ROE-v1",
    "scope.csv": b"host,port\n10.20.1.10,443\n",
    "findings.json": b'[{"id":"SYN-001"}]',
}
expected = {n: hashlib.sha256(b).hexdigest()[:16] for n,b in files.items()}
# Simulate tampering of findings.json
current = dict(expected)
current["findings.json"] = hashlib.sha256(b'[{"id":"SYN-001"},{"id":"TAMPERED"}]').hexdigest()[:16]
print(json.dumps(expected, indent=1))
for n in sorted(expected):
    status = "OK" if expected[n] == current[n] else "MISMATCH"
    print(f"{n:16} {status}")
```

Expected output:

```text
{
 "roe.pdf": "18d74983d403e7db",
 "scope.csv": "01cc4815eddf3de6",
 "findings.json": "7f5f178ab43ef00f"
}
findings.json    MISMATCH
roe.pdf          OK
scope.csv        OK
```

### 40.3 Sign-off

Release candidate checklist signed by implementer and reviewer; safety rows must be green.

> **Synthetic case — Riverstone Transit.** Lab II found coverage updated before ticket create on retry — fixed ordering with outbox.

### 40.4 Errors and limits

E2E without fault injection only proves the happy path.

### 40.2b Observability in the lab

Lab II enables debug logs temporarily but seals a redacted copy. Leaving debug on in engagement builds can leak tokens into log aggregates. Toggle is part of the sign-off checklist.

### 40.3b Flaky tests

A flaky Lab II is a blocker, not a retry-until-green ritual. Quarantine the test, fix the race (clocks, ordering), then re-run. Shipping with "sometimes fail-closed" is shipping fail-open.

### 40.1b Environment parity

Lab II environment mirrors production tool versions and policy signing keys (test keys). Parity gaps explain "green in lab, red in engagement" surprises.

### Practice note

Lab II includes a malicious fixture pack: wrong hashes, reordered events, future timestamps. Passing only happy fixtures is an incomplete laboratory. The malicious pack is versioned beside the golden fixtures and covered by CODEOWNERS so it cannot be weakened quietly to make a release green.



Seal Lab II logs with the same manifest tool the dossier uses so students practise one hashing workflow.



Fault-injection scripts are checked into the lab folder and pinned by SHA in the report.



Happy-path green with malicious-pack red still fails Lab II sign-off.


### 40.4b Sign-off evidence

The Laboratory II sign-off pack holds the test plan, the run logs, the list of injected faults with observed behaviour, and the open issues with owners. An independent engineer signs only after reproducing two randomly chosen results from the pack.

### Exercises

- **EX118 — Ordering.** Why create ticket before coverage count increases? Rubric: 3 = coverage must reflect recorded findings; 2 = vague; 1 = either order; 0 = none.
- **EX119 — Fault.** Expected TrackScope behaviour when desk is down. Rubric: 3 = still evaluate/deny; queue drafts; 2 = partial; 1 = fail open; 0 = none.
- **EX120 — Sign-off.** Two signatures required — who? Rubric: 3 = implementer + independent reviewer; 2 = one; 1 = manager only; 0 = none.

### Synthesis

E2E with faults; green safety; two signatures.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Authorized offensive security and red team: system optimization

### Learning outcomes

You will (1) profile assessment pipelines ethically; (2) optimize under ROE constraints; (3) reject optimizations that weaken safety.

### 41.1 Profile first

Measure where time goes: DNS, TLS handshake, predicate eval, ticket write. Optimize the dominant term. Synthetic load only.

### 41.2 Constraint-preserving

Caching ScopeVersion is fine if invalidation on publish is correct. Caching allow decisions across hosts is not — hosts differ.

### 41.3 Safety veto

Any optimization that skips deny-list checks, shortens audit fields or fails open is rejected regardless of speedup.

```python
"""Rank synthetic assets for authorized engagement scoping."""
assets = [
    ("public-web-portal", 3, 3, 3),      # exposure, data_sensitivity, blast_radius 1-3
    ("staging-admin-ui", 2, 3, 2),
    ("corp-vpn-edge", 3, 2, 3),
    ("internal-wiki", 1, 2, 1),
    ("printer-fleet", 2, 1, 1),
    ("lab-jump-host", 1, 1, 2),
]
print(f"{'asset':20} score exposure data blast")
for name, e, d, b in sorted(assets, key=lambda x: -(x[1]+x[2]+x[3])):
    print(f"{name:20} {e+d+b:5} {e:8} {d:4} {b:5}")
```

Expected output:

```text
asset                score exposure data blast
public-web-portal        9        3    3     3
corp-vpn-edge            8        3    2     3
staging-admin-ui         7        2    3     2
internal-wiki            4        1    2     1
printer-fleet            4        2    1     1
lab-jump-host            4        1    1     2
```

> **Synthetic case — Riverstone Transit.** Caching signed policy in memory cut latency 40%; invalidation on publish kept safety. A proposal to skip deny-list for "known good" hosts was vetoed.

### 41.4 Errors and limits

Benchmarks on laptops do not predict depot links (Chapter 3).

### 41.2b Load shedding

Under overload, shed discovery work before shedding deny evaluation. Users can wait for a scan; they cannot wait for a deny that never comes. Implement priority queues accordingly.

### 41.3b Capacity headroom

Keep headroom under the ROE limit so a retry storm (Chapter 32) does not breach it. If the ROE allows 5 req/s, engineer for 3–4 sustained. Document the headroom assumption.

### 41.1b N+1 queries

Chatty ticket updates during bulk import crush FindingsDesk. Batch writes and measure. Performance work often starts as an integration bug, not as a need for exotic caches.

### Practice note

Optimization proposals require a safety paragraph: which checks still run, which are skipped, how fail-closed is preserved. Proposals without that paragraph are returned unread. Speed reviews that ignore safety paragraphs have caused more ROE breaches than slow scanners ever did.



Reject optimization PRs that remove reason codes from logs even if latency improves.



Benchmarks cite the ROE limit next to the achieved rate so unconstrained benches are obvious.


### 41.4b Recording optimisation decisions

Each optimisation is recorded with the profile that justified it, the measured gain and any safety check it touched. When a later change slows a path, the record shows whether the earlier speed-up depended on an assumption that no longer holds.

### Exercises

- **EX121 — Veto.** Give an optimization that must be rejected. Rubric: 3 = safety-weakening example; 2 = vague; 1 = okays it; 0 = none.
- **EX122 — Cache.** When is decision caching safe? Rubric: 3 = same ScopeVersion+target+context, short TTL, invalidate on publish; 2 = partial; 1 = always; 0 = none.
- **EX123 — Inventory.** Why optimize scheduling with scores? Rubric: 3 = limited window → highest exposure first; 2 = vague; 1 = random; 0 = none.

### Synthesis

Speed under constraints; safety has veto power.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Authorized offensive security and red team: applied research

### Learning outcomes

You will (1) frame a research question about assessment platforms; (2) choose measures and baselines; (3) keep dual-use out of student research.

### 42.1 Questions that fit

"Does dual-approval reduce scope-widen incidents?" "Does showing denominators change stakeholder interpretation of coverage?" Not "new bypass against product X".

### 42.2 Design

Pre-register measures; use synthetic or consented operational data; report intervals. Replication beats novelty theatre.

### 42.3 Disclosure

If research accidentally finds a live issue, follow responsible disclosure — not a class blog.

> **Synthetic case — Riverstone Transit.** Sam's applied study compared ticket reopen rates before/after requiring re-test evidence; pre-registered, synthetic+anonymized.

### 42.4 Errors and limits

Course projects are not IRB-proofed human-subjects work; avoid collecting personal data.

### 42.2b Pre-registration

Write the hypothesis, primary measure and exclusion rules before looking at outcome data. File them in the repo. Changing the measure after seeing results is how empty scores return through the research door.

### 42.3b Negative results publishability

Publishable applied research includes negative results ("dual approval did not change reopen rates in this sample"). Hiding negatives biases the next cohort's designs toward empty confidence.

### 42.1b Data sharing agreements

Even synthetic-plus-anonymized operational metrics need a written agreement with the host for student theses. "My mentor said it was fine" is not a sharing agreement.

### Practice note

Preregistered analysis code lives in the repo with a freeze commit before data collection. Amending the analyzer after peeking at outcomes requires a logged amendment with reason. This is lightweight compared with clinical trials and still blocks the most common form of accidental p-hacking in undergraduate studies.



State the dual-use boundary in the thesis ethics section with a concrete refusal example.



Negative results get the same figure quality as positive ones in the thesis template.


### 42.4b Ethics review for platform research

A study comparing detection coverage across engagements uses client data, even if summarised. Sam's proposal goes through the organisation's ethics and legal review, uses only aggregated, anonymised counts, and has each client's written consent before any result is shared outside the team.

### Exercises

- **EX124 — Question.** Write one acceptable research question. Rubric: 3 = platform/process focused; 2 = borderline; 1 = exploit focused; 0 = none.
- **EX125 — Measure.** Name primary measure for dual-approval study. Rubric: 3 = e.g. unauthorized widen attempts/month; 2 = vague; 1 = "security"; 0 = none.
- **EX126 — Dual-use.** Refuse a project that asks for a new exploit. Rubric: 3 = refusal + allowed alternative; 2 = refusal; 1 = accepts; 0 = none.

### Synthesis

Research the platform and process; leave weaponization alone.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) adapt platform engineering to a host organization's constraints; (2) write a practice report without client confidential detail; (3) translate between counsel, ops and engineering.

### 43.1 Placement

In industry or public service, ROE templates, residency and procurement differ. Your job is still fail-closed tooling and honest measurement — not clever unauthorized tests.

### 43.2 Sanitized reporting

Course deliverables use synthetic names and aggregates. Real client identifiers stay inside the host's systems.

### 43.3 Translation

Counsel hears authorization and retention; ops hears change windows and canaries; engineering hears schemas and tests. Same facts, three dialects.

> **Synthetic case — Riverstone Transit.** Sam's placement memo used only Riverstone synthetic figures; real partner names were omitted.

### 43.4 Errors and limits

"I can't tell you what I did" is not a practice report — use synthetic reconstruction agreed with the host.

### 43.2b Procurement friction

Public-service hosts may take months to approve a new SaaS. Design the capstone to run on infrastructure the host already authorizes. A perfect architecture that cannot be purchased fails the practice course.

### 43.3b Conflict of interest

If your placement host sells scanners, your practice report must disclose that and still refuse empty scores. Marketing decks are not measurement.

### 43.1b Clearance and need-to-know

Public-service placements may involve clearances. Course artefacts stay at the lowest sensitivity: synthetic reconstructions. Never paste classified or restricted text into GitHub.

### Practice note

Practice reports include a constraints appendix: residency, procurement, clearance, change boards. Graders mark the appendix as heavily as the technical work because the course outcome is judgment under constraint, not unconstrained elegance on a personal laptop.



Agree the sanitized reconstruction with the host mentor in writing before writing the practice report.



If the host forbids even sanitized metrics, the practice report uses a fully synthetic twin scenario labelled as such.


### 43.4b Learning from the placement

Sam keeps a weekly placement journal: one thing learned about how a public transit operator actually runs security, one assumption from the course that did not hold, and one question for his supervisor. The journal becomes the reflective section of his placement report.

### Exercises

- **EX127 — Dialect.** Translate "fail closed on missing policy" for counsel. Rubric: 3 = legal/risk wording; 2 = partial; 1 = jargon dump; 0 = none.
- **EX128 — Sanitize.** Rewrite a sentence that leaks a real hostname. Rubric: 3 = synthetic substitute; 2 = partial redaction; 1 = still leaks; 0 = none.
- **EX129 — Constraint.** Name two public-service constraints that change architecture. Rubric: 3 = e.g. residency, procurement, FOIA logs; 2 = one; 1 = vague; 0 = none.

### Synthesis

Practice is real constraints plus sanitized learning artefacts.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) propose a capstone that ships a measurable platform improvement; (2) define scope and non-goals; (3) set a verification plan.

### 44.1 Proposal

Problem, users, requirements (safety first), architecture sketch, milestones, verification lab plan, ethics paragraph. Capstones that need exploit work are rejected.

### 44.2 Non-goals

Explicitly list what you will not build (exploit modules, live client scanning, ML risk oracles).

### 44.3 Milestone 1

Something demoable on synthetic data in week 3: e.g. kill-switch honored in ≤30s with a test.

> **Synthetic case — Riverstone Transit.** Capstone I proposals that mentioned "auto-pwn" were returned; "signed policy distribution with fail-closed" advanced.

### 44.4 Errors and limits

Capstone scope creep is the main killer — freeze non-goals.

### 44.2b Risk register for the capstone

List project risks: scope creep, dependency delay, reviewer unavailability, ethics boundary confusion. Each risk has an early warning and a mitigation. Review the register weekly in studio.

### 44.3b Advisor checkpoints

Capstone I has mandatory checkpoints: proposal accepted, milestone 1 demo, mid ethics check. Missing a checkpoint freezes coding until recovered — silent drift produces unreviewable piles.

### 44.1b Success metrics for the capstone

Define two metrics you will show at defense (e.g. deny-all time, percent of merges with AUTH tickets). If you cannot name them in Capstone I, the proposal is not ready.

### Practice note

Capstone I proposals that cannot name a verification lab row for each Must requirement return to draft. Mapping requirements to lab rows early prevents beautiful designs that cannot be shown to fail closed under Lab I.



Attach the ethics paragraph to the proposal so advisors can reject dual-use scope before coding starts.



Milestone demos that skip fail-closed are graded zero for that checkpoint regardless of UI polish.



Proposals without lab-row mapping are returned before studio time is booked.


### 44.4b Scoping the capstone honestly

The capstone proposal states what will be built in the time available — a scope-diff tool for TrackScope with tests and a short evaluation — and what will not, such as integration with every client's ticket system. Advisors judge the project against the stated scope, not against an imagined larger one.

### Exercises

- **EX130 — Non-goal.** Write three non-goals for a PulseMap capstone. Rubric: 3 = three clear; 2 = two; 1 = one; 0 = none.
- **EX131 — Milestone.** One week-3 milestone with acceptance test. Rubric: 3 = demo + test; 2 = demo only; 1 = vague; 0 = none.
- **EX132 — Ethics.** Four-sentence ethics paragraph. Rubric: 3 = auth, synthetic, dual-use, disclosure; 2 = partial; 1 = weak; 0 = none.

### Synthesis

Ship safety-relevant platform value; freeze non-goals early.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) run a review that can reject; (2) use a checklist tied to safety requirements; (3) record dissenting opinions.

### 45.1 Review rights

Reviewers may block merge for fail-open paths, missing tests, or empty scores in UI. "LGTM" without running the checklist is invalid.

### 45.2 Checklist

Fail-closed; policy authn; schema forbids payloads; coverage has denominator; secrets redaction; rollback path documented.

### 45.3 Dissent

If one reviewer disagrees, record the dissent in the ADR even if overruled — future incidents need that trail.

> **Synthetic case — Riverstone Transit.** A coverage badge PR was blocked twice under this checklist; the third revision shipped the honest UI (Chapter 35).

### 45.4 Errors and limits

Reviews after merge are archaeology, not control.

### 45.2b Reviewer preparation

Reviewers run the critical tests locally on synthetic fixtures before the meeting — not only read the diff. A review that never executed fail-closed is incomplete regardless of comment volume.

### 45.3b Review SLOs

Reviews complete within an agreed number of business days or the change auto-expires from the merge queue (not auto-merges). Pressure to rubber-stamp is a safety smell.

### 45.1b External reviewers

Once per term, invite an engineer from outside the squad to review a safety-critical PR. Fresh eyes catch normalized deviance ("we always skip that test").

### Practice note

Review culture forbids merging on Friday evenings before engagement weekends unless the change is a safety hotfix with Lab I evidence attached. The calendar is part of the control design; heroic late merges are a smell, not a badge.



Rotate checklist owners each month so review quality does not depend on one conscientious engineer.



Blocking comments must cite a requirement id or checklist item number.



Checklist item numbers appear in the PR template as a required fill-in list.



Repeated checklist skips by the same reviewer trigger a coaching conversation, not a silent reassignment forever.


### 45.4b Closing review comments

Every review comment ends in one of three states: fixed, with a link to the change; declined, with a reason the reviewer accepts; or carried as a known risk with an owner. Sam's design is approved only when no comment remains open without one of these states.

### Exercises

- **EX133 — Block.** Write a blocking comment for a fail-open retry. Rubric: 3 = cites safety req + fix ask; 2 = vague block; 1 = nit; 0 = approve.
- **EX134 — Checklist.** Add one item for radio engagements. Rubric: 3 = specific; 2 = vague; 1 = none; 0 = none.
- **EX135 — Dissent.** One sentence of recorded dissent. Rubric: 3 = clear; 2 = hedged; 1 = none; 0 = none.

### Synthesis

Reviews that can say no, with a checklist and a memory.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) finish implementation against the frozen proposal; (2) run Verification Lab II; (3) deliver operator docs.

### 46.1 Freeze

Feature freeze date is real: after it, only safety fixes. New ideas go to a sequel proposal.

### 46.2 Verify

Capstone must pass Lab II (Chapter 40) on synthetic fixtures with signed checklist.

### 46.3 Docs

Runbook section, ADR, operator tutorial with screenshots of synthetic UI — no client data.

```python
"""Rebuild a synthetic engagement timeline from event records."""
events = [
    ("09:00", "ROE brief signed", "auth"),
    ("09:15", "scoped host inventory loaded (12 hosts)", "prep"),
    ("10:02", "service enumeration on 10.20.1.0/28", "enum"),
    ("10:45", "finding SYN-001 noted on staging UI", "find"),
    ("11:10", "stop: host 10.20.0.1 probed — out of scope", "stop"),
    ("11:12", "escalated to client contact; confirmed deny-list", "comm"),
    ("13:00", "resume on in-scope hosts only", "auth"),
    ("15:30", "debrief draft shared with client", "report"),
]
# print chronological with phase tags; compute stop latency
print("phase timeline:")
for t, msg, phase in events:
    print(f"  {t} [{phase:6}] {msg}")
t0 = 10*60+45; t1 = 11*60+10
print(f"minutes from SYN-001 note to stop: {t1-t0}")
print(f"stop reason present: yes")
print(f"events={len(events)} phases={len(set(p for _,_,p in events))}")
```

Expected output:

```text
phase timeline:
  09:00 [auth  ] ROE brief signed
  09:15 [prep  ] scoped host inventory loaded (12 hosts)
  10:02 [enum  ] service enumeration on 10.20.1.0/28
  10:45 [find  ] finding SYN-001 noted on staging UI
  11:10 [stop  ] stop: host 10.20.0.1 probed — out of scope
  11:12 [comm  ] escalated to client contact; confirmed deny-list
  13:00 [auth  ] resume on in-scope hosts only
  15:30 [report] debrief draft shared with client
minutes from SYN-001 note to stop: 25
stop reason present: yes
events=8 phases=7
```

> **Synthetic case — Riverstone Transit.** Capstone II delivered signed policy distribution; Lab II green; runbook updated the same day.

### 46.4 Errors and limits

Demo magic on a laptop with hand-waved fail-closed does not pass.

### 46.2b Operator shadowing

Before claiming done, a second engineer follows the runbook cold on synthetic data while the author is silent. Places they stall become doc fixes. Capstone II is not done until the silent run succeeds.

### 46.3b Demo script

Capstone II demo follows a script on synthetic data: show fail-closed, show coverage denominator, show a stopped action. Improvised demos skip safety. Record the script next to the lab report.

### 46.1b Handover to ops

Capstone code without an ops owner at merge is unfinished. Name the owning squad in the README and CODEOWNERS before Lab II sign-off.

### Practice note

The silent runbook test is recorded on video for the advisor (synthetic data only). Watching a peer struggle is uncomfortable and uniquely effective at surfacing missing prerequisites — for example, never documenting that the test policy key is required.



Link the silent-run video hash in the Lab II report for advisor audit.



Ops acceptance is a required signature beside Lab II on the release checklist.



Without ops signature the release tag is not cut, even if Lab II is green.



Advisor review watches the silent-run recording at 1.5x and files doc issues before sign-off.


### 46.4b Final acceptance test

Before the capstone is handed over, an operator who did not build it runs the acceptance script alone, using only the documentation. Two steps failed in Sam's first attempt because the documentation assumed knowledge he had; both were rewritten and the operator's second run passed.

### Exercises

- **EX136 — Freeze.** What is allowed after feature freeze? Rubric: 3 = safety fixes only; 2 = "bugs"; 1 = features; 0 = none.
- **EX137 — Artefacts.** List five delivery artefacts. Rubric: 3 = five (code, tests, lab report, ADR, runbook…); 2 = three; 1 = code only; 0 = none.
- **EX138 — Timeline.** Where does capstone verification sit relative to engagement use? Rubric: 3 = before any client window; 2 = vague; 1 = during; 0 = none.

### Synthesis

Freeze, verify, document — then and only then operate.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a scripted failure trial; (2) measure recovery time; (3) file corrective actions.

### 47.1 Script

Inject: policy file deleted; FindingsDesk killed; clock skew; duplicate event replay. Observe denies, queues, alerts.

### 47.2 Measures

Time to deny-all after policy loss; time to alert; time to restore; findings lost (should be 0 with queue).

### 47.3 Corrective actions

Each miss becomes a ticket with owner and due date — not only a lesson-learned slide.

```python
"""Verify integrity of a synthetic evidence package."""
import hashlib, json
files = {
    "roe.pdf": b"SYNTHETIC-ROE-v1",
    "scope.csv": b"host,port\n10.20.1.10,443\n",
    "findings.json": b'[{"id":"SYN-001"}]',
}
expected = {n: hashlib.sha256(b).hexdigest()[:16] for n,b in files.items()}
# Simulate tampering of findings.json
current = dict(expected)
current["findings.json"] = hashlib.sha256(b'[{"id":"SYN-001"},{"id":"TAMPERED"}]').hexdigest()[:16]
print(json.dumps(expected, indent=1))
for n in sorted(expected):
    status = "OK" if expected[n] == current[n] else "MISMATCH"
    print(f"{n:16} {status}")
```

Expected output:

```text
{
 "roe.pdf": "18d74983d403e7db",
 "scope.csv": "01cc4815eddf3de6",
 "findings.json": "7f5f178ab43ef00f"
}
findings.json    MISMATCH
roe.pdf          OK
scope.csv        OK
```

> **Synthetic case — Riverstone Transit.** Trial showed 45s to deny-all; target 30s — poll interval tightened.

### 47.4 Errors and limits

Trials on production engagements are forbidden; use synthetic ranges.

### 47.2b Blameless correction

Failure trials exist to find system gaps. Write corrective tickets against components and runbooks, not against individuals who followed a bad procedure. Blame-seeking stops people from reporting the next miss.

### 47.3b Recurrence tests

After a corrective fix, re-run the inject that found the gap. Close the ticket only when the measure meets the SLO twice. Otherwise the same failure returns next term.

### 47.1b Observer roles

Failure trials include an observer who only notes timings and deviations — not a participant who fixes things live. Fixes come after through tickets.

### Practice note

Failure trials publish a short scoreboard: inject, expected, observed, delta, ticket. Celebrate tickets filed — they are the output. A trial with zero tickets usually skipped hard injects or ignored misses.



Schedule the next trial date before leaving the room so recurrence tests actually happen.



Observers rotate so nobody becomes permanently exempt from being the person under trial.



Scoreboard photos go into the dossier under the failure-trial evidence class.



If an inject cannot be run safely even on synthetic ranges, rewrite it — do not skip and mark green.


### 47.4b Choosing the failure to rehearse

The trial rehearses the failure with the worst consequence for clients, not the easiest to stage: TrackScope losing its scope file mid-engagement. The script checks that methods stop, the lead is paged and testing resumes only after the file is restored and verified.

### Exercises

- **EX139 — Inject.** Write one inject and expected safe behaviour. Rubric: 3 = both; 2 = inject only; 1 = vague; 0 = unsafe.
- **EX140 — Measure.** Primary measure for policy-loss inject. Rubric: 3 = time to deny-all; 2 = vague uptime; 1 = none; 0 = none.
- **EX141 — Action.** Turn a 45s result into a corrective ticket title. Rubric: 3 = specific; 2 = vague; 1 = none; 0 = none.

### Synthesis

Break it on purpose; measure; ticket the gaps.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble a dossier a third party can re-hash; (2) structure retention classes; (3) exclude dual-use material.

### 48.1 Contents

ROE PDF, ScopeVersion JSON, finding exports, evidence objects, hash manifest, tool versions, lab reports. Reader can verify without trusting your laptop.

```python
"""Verify integrity of a synthetic evidence package."""
import hashlib, json
files = {
    "roe.pdf": b"SYNTHETIC-ROE-v1",
    "scope.csv": b"host,port\n10.20.1.10,443\n",
    "findings.json": b'[{"id":"SYN-001"}]',
}
expected = {n: hashlib.sha256(b).hexdigest()[:16] for n,b in files.items()}
# Simulate tampering of findings.json
current = dict(expected)
current["findings.json"] = hashlib.sha256(b'[{"id":"SYN-001"},{"id":"TAMPERED"}]').hexdigest()[:16]
print(json.dumps(expected, indent=1))
for n in sorted(expected):
    status = "OK" if expected[n] == current[n] else "MISMATCH"
    print(f"{n:16} {status}")
```

Expected output:

```text
{
 "roe.pdf": "18d74983d403e7db",
 "scope.csv": "01cc4815eddf3de6",
 "findings.json": "7f5f178ab43ef00f"
}
findings.json    MISMATCH
roe.pdf          OK
scope.csv        OK
```

### 48.2 Retention

Classes: engagement working (90 days), sealed evidence (agreed years), aggregate metrics (longer). Deletion jobs are tested.

### 48.3 Exclusions

No payloads, no live credentials, no personal data. If it cannot be shared with counsel safely, it does not belong.

> **Synthetic case — Riverstone Transit.** Dossier v3 re-hashed clean after the findings.json incident; process note included.

### 48.4 Errors and limits

Dossiers in personal cloud accounts fail residency and retention.

### 48.2b Third-party readability

Hand the dossier to someone outside the project for a re-hash drill. If they cannot find the manifest or the ROE version, the dossier fails regardless of how neat it looks to its authors.

### 48.3b Redaction log

When redacting, keep a redaction log (what, why, actor) inside the sealed store. Future readers need to know that a blank was intentional, not truncated evidence.

### 48.1b Reader checklist

Include a one-page "how to verify this dossier" at the top: install tool versions, run `sha256sum -c manifest`, open ROE, spot-check one finding. If readers need a tour guide, the dossier is incomplete.

### Practice note

Dossier builds are automated from tags: a make target produces the zip and manifest. Manual dragging of files into folders is how findings.json gets edited after seal. Automation makes the happy path the safe path.



Test restore from dossier on a clean machine once per term as a graded exercise.



Manifest generation fails the build if any path matches a forbidden-name regex.



Forbidden-name failures print the offending path so authors can fix quickly.


### 48.4b Integrity of the dossier

Each file in the evidence dossier is listed with its SHA-256 hash in a manifest, and the manifest itself is signed by the lead. A reader can confirm that nothing was added or changed after sign-off without trusting the storage location.

### Exercises

- **EX142 — Manifest.** Sketch a hash manifest format (3 rows). Rubric: 3 = path+algo+digest; 2 = digests only; 1 = vague; 0 = none.
- **EX143 — Class.** Assign retention class to ROE PDF vs scratch notes. Rubric: 3 = sealed vs working/delete; 2 = partial; 1 = same forever; 0 = none.
- **EX144 — Exclude.** What do you do if a student pastes a password into a finding? Rubric: 3 = scrub, rotate, process finding; 2 = scrub only; 1 = ignore; 0 = publish.

### Synthesis

Dossiers are verifiable, classified and boringly safe.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) structure a thesis around a platform claim; (2) defend measures and limits; (3) cite primary frameworks correctly.

### 49.1 Claim

One sentence: what you built/measured and for whom. Example: "Signed policy distribution with fail-closed semantics reduces unauthorized allows in synthetic trials."

### 49.2 Body

Related work (SP 800-115, PTES, ATT&CK, Albrecht & Jensen), design, verification, results with intervals, limitations, ethics.

### 49.3 Citations

Use the verified URLs/DOIs from the source policy; do not invent papers. Frameworks change — note access dates.

> **Synthetic case — Riverstone Transit.** Thesis draft used only synthetic trial data and cited CBEST 2024 Implementation Guide correctly.

### 49.4 Errors and limits

A thesis that evaluates exploitation skill is out of programme scope.

### 49.2b Threats to validity

Discuss construct validity (does coverage measure what you claim?), internal validity (confounds in the trial), external validity (other orgs). A thesis that skips this section overclaims by omission.

### 49.3b Reproducibility appendix

Ship enough to replay synthetic trials: fixture hashes, tool SHAs, scripts. "Available on request" is not a reproducibility appendix for an engineering thesis in this programme.

### 49.1b Related work honesty

Cite frameworks you actually used. Padding related work with unread papers is discovered quickly in defense questions. Thin and accurate beats thick and fake.

### Practice note

Examiners receive a one-page threats-to-validity summary. If you cannot fit honesty on one page, the thesis overclaims elsewhere. Length is not rigor; structured limits are.



Put the claim sentence in bold on page one so examiners and you share the same target.



Related-work claims require a one-line how-used note, not only a citation.



How-used notes stop citation padding cold in advisor review.



The threats-to-validity page is graded; leaving it blank fails the thesis gate regardless of implementation quality.



Examiners read that page first.


### 49.4b Structure of the argument

Sam's thesis states its claim in the first paragraph, presents evidence in the order a sceptical reader would demand it, and ends each chapter by stating what that chapter established and what remains uncertain. His advisor's test is whether the abstract alone tells a reader exactly what was shown.

### Exercises

- **EX145 — Claim.** Write a one-sentence thesis claim for dual-approval. Rubric: 3 = measurable+scoped; 2 = vague; 1 = exploit claim; 0 = none.
- **EX146 — Limit.** One limitation paragraph (3 sentences). Rubric: 3 = external validity clear; 2 = partial; 1 = none; 0 = overclaim.
- **EX147 — Cite.** Give the DOI for NIST SP 800-115. Rubric: 3 = 10.6028/NIST.SP.800-115; 2 = title only; 1 = wrong; 0 = none.

### Synthesis

One claim, honest limits, real citations.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) present the claim and evidence in 20 minutes; (2) answer safety and measurement questions; (3) state what you would not do again.

### 50.1 Talk structure

Claim; demo on synthetic data; verification results; one failure trial lesson; limits; questions. No live hacking demo.

### 50.2 Likely questions

Fail-closed proof? Denominator choice? Dual-use boundary? What broken in Lab II? Practice answering with pointers to artefacts.

### 50.3 Reflection

End with one design mistake and the fix — examiners trust engineers who saw their own failures.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Expected output:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

> **Synthetic case — Riverstone Transit.** Sam's defense led with the fail-closed lab, not a slide of logos. When asked for a risk score, Sam refused and showed SLA and coverage denominators.

### 50.4 Errors and limits

Defense is not a sales pitch for a scanner vendor.

### 50.2b After the defense

Archive the talk deck next to the dossier with matching hashes. Note examiner requests as issues. The defense is a gate, not the end of maintenance — ownership continues (Chapter 39).

### 50.3b Examiner packet

Provide examiners the claim sentence, Lab II summary, failure-trial measure, and ethics paragraph one day ahead. Surprise decks waste defense time that should test your judgment.

### 50.1b Time discipline

Twenty minutes means rehearsal with a timer. Cutting the limits slide to save time is the wrong cut — examiners need your honesty more than a fourth demo click.

### Practice note

After defense, schedule a maintenance review in ninety days: is the owning squad still correct, are pins current, did any corrective tickets reopen? The final chapter of the degree is the first chapter of stewardship.



Thank operators who ran synthetic trials; defense without their logs is storytelling.



Keep a parking lot for examiner ideas and process it within a week while context is fresh.


### 50.4b Rehearsing the defense

Two weeks before the defense, Sam gives the talk to peers who play examiners and ask the hardest questions on the likely-questions list. He times each section, cuts slides that run over, and writes short answers for the three questions he struggled with.

### Exercises

- **EX148 — Outline.** Six-bullet talk outline. Rubric: 3 = claim→demo→verify→failure→limits→Q; 2 = partial; 1 = vendor pitch; 0 = none.
- **EX149 — Answer.** 3–4 sentences answering "what's your risk score?" Rubric: 3 = refuse empty score + alternatives; 2 = partial; 1 = invents score; 0 = none.
- **EX150 — Mistake.** One real (synthetic-story) mistake and fix. Rubric: 3 = specific; 2 = vague; 1 = "none"; 0 = none.

### Synthesis

Defend the engineering, the measures and the refusals.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)


<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Riverstone Transit, Sam Ito and all numbers are synthetic. Any answer meeting the rubric scores equally.

**EX001.** r′(t) = 8 − 2t = 0 at t = 4, so the peak is r(4) = 32 − 16 = 16 req/s. Solving 8t − t² = 7 gives t² − 8t + 7 = 0, t = 1 or t = 7. The ceiling is breached from minute 1 to minute 7, six minutes. Score 3 needs both the peak and the window.

**EX002.** Rate: "No more than 5 requests per second to /api/tickets from the assessment source address." Total: "No more than 20,000 requests per calendar day to /api/tickets." The total is easier to verify from logs (a single count per day); the rate needs per-second bucketing and a tolerance for clock skew.

**EX003.** 2,160 / 4 = 540 seconds = 9 minutes. The flat schedule is longer than the 6-minute ramp but never exceeds the ceiling.

**EX004.** T = {(h, p) : h ∈ 192.168.50.0/24, h ∉ {192.168.50.1, 192.168.50.254}, p ∈ {22, 443}}. |T| = (256 − 2) × 2 = 508. (Counting usable hosts only, 254 − 2 = 252 hosts and 504 pairs, is also accepted if stated.)

**EX005.** Let P′ = P ∪ {q}. Any (h, p) ∈ T has p ∈ P ⊆ P′, and the other clauses are unchanged, so (h, p) ∈ T′. Hence T ⊆ T′. Because port additions can only widen scope, they need written client approval and a second reviewer, unlike deny-list additions.

**EX006.** Both use host 192.168.50.20, which is in the 192.168.50.0/24 range and not on the deny-list. Port 22 is in P = {22, 80, 443, 8080}; port 3389 is not, so that clause fails and the decision is DENY with reason port-not-in-scope.

**EX007.** 800 km each way at ~200,000 km/s is ~4 ms, so ~8 ms round trip is the floor. 2 ms is not plausible; likely the response came from a local cache, proxy or a different site than assumed. Ask for the measurement method and path.

**EX008.** 500 × 120 × 8 = 480,000 b/s = 0.48 Mb/s, which is 24% of 2 Mb/s. Add header overhead for a realistic figure.

**EX009.** Bands and channels permitted; exact physical locations (buildings/floors); dates and hours; transmit-power or active-test limits; and a rule that third-party devices and their traffic are out of scope, not recorded, or discarded immediately. Any four, with a named authorizing signatory.

**EX010.** `in` on strings tests for a substring, and "8443,22" contains "443". Parse the field into a set of integers, `ports = {int(x) for x in s.split(",")}`, and test `443 in ports`, which is False here.

**EX011.** Test 192.168.50.0 and 192.168.50.255 (both inside the /24 network object) and 192.168.51.0, which must be outside. A string-prefix implementation often fails the last case.

**EX012.** The reason identifies which rule fired, so logs show why an action was blocked ("deny-list" vs "outside-cidr") and reviewers can check the right rule. Tests can then assert the specific reason, catching a case where the right answer is reached for the wrong reason.

**EX013.** Title: "Corporate VPN edge permits legacy protocol version without multi-factor authentication." Evidence: "On 14 March 10:20 (synthetic), the authorized configuration review of corp-vpn-edge showed the legacy profile enabled with password-only login; ref FD-131." No commands, no credentials.

**EX014.** "Between 09:00 and 17:00 on the authorized day we assessed 12 in-scope Riverstone hosts under ROE v1.3. Two findings are critical: a default admin password on the staging web UI and a lab service account with domain-administrator rights. We ask the platform owner to approve credential rotation within the 7-day critical SLA."

**EX015.** For example: (1) the deny-listed gateway and two hosts that were offline were not assessed, so their state is unknown; (2) social engineering and physical access were out of scope, so the report says nothing about phishing resilience. Each limit narrows what the conclusions cover.

**EX016.** Expected attempts per upload = 1/0.7 ≈ 1.429; for 500 uploads, about 714 attempts. The ROE and rate limit must cover 714, not 500.

**EX017.** B′ = 3 − 5 = −2/day, so B(t) = 40 − 2t = 0 at t = 20 days, assuming constant rates and no priority.

**EX018.** Theory: 1 − 0.2³ = 0.992 versus 0.8, a gain of 0.192 (19.2 points). The lab's empirical 988/1000 vs 784/1000 is about 20.4 points; either figure with the comparison is a 3.

**EX019.** Point estimate 20%. A Wilson 95% interval is roughly 10.5%–34.5%. You may say the rate is likely in the teens to low thirties; you may not claim superiority over another method at 25% without a larger or paired sample.

**EX020.** Precision = (0.9·0.005) / (0.9·0.005 + 0.02·0.995) = 0.0045 / (0.0045 + 0.0199) ≈ 0.184 (18.4%).

**EX021.** "With 12/100 and 18/100 the intervals overlap substantially; this sample does not justify ranking the filters. We need a larger n or a paired test on the same prompts before choosing one."

**EX022.** User: HTTP responses, authenticated API reads, own process list, application logs the account can see, TLS certificate presented. Elevated: raw disk, other users' memory, kernel modules, firewall tables, hypervisor console. Any correct six with the split clear.

**EX023.** "Only host lab-cache-01 (no production traffic routed to it)." "Stop and notify the contact if median latency of the canary request exceeds 50 ms for five minutes." Plus "no results published with production keys or customer data."

**EX024.** Under ROE, attempt a login with the vendor default against the staging URL; capture the HTTP status and a redacted screenshot; open FindingsDesk ticket with time and URL; log out; do not store the password in the ticket body (reference the sealed evidence store). No OS access required.

**EX025.** On ingest, if any key matches the regex, reject with 400 and reason "forbidden field". Example failing body: `{"title":"x","payload":"..."}`. Tests assert rejection.

**EX026.** Fingerprint is (asset, weakness, location). Both /login rows share (web-01, missing-header, /login); /account is a different location, so a different fingerprint and a separate finding.

**EX027.** After adding host h to the deny-list, for every port p, allowed(h, p) is False. Equivalently, the permitted set after the change is a subset of the set before.

**EX028.** "I can't provide a working exploit or PoC for a real product — that is dual-use and outside this course's safety rules. I can help you write a finding description from synthetic evidence or point you at the vendor's public advisory process."

**EX029.** denial-of-service → deny-action; password-spray-lab without approval → needs-approval; service-enum at 18:00 → outside-hours; service-enum with concurrency 20 → concurrency. Approved password-spray and in-hours enum with concurrency 3 are ALLOW.

**EX030.** In-scope systems and endpoints; permitted methods; dates and times; rate, data and privacy limits; named contacts and escalation; stop conditions and resume rules. Signed by someone with authority over the assets.

**EX031.** Example: MAC/ARP observation needs link-segment access; presented TLS certificate needs a TCP connection to the port; a private API field needs an authenticated session. Exact triples may vary if justified.

**EX032.** P = {80, 443, 8080}; note: "HTTP and HTTPS only to the fare portal and staff apps listed in Appendix A; no TLS MITM, no other protocols on those ports."

**EX033.** public-web-portal (9) and corp-vpn-edge (8): highest exposure and blast radius, both Internet-facing. Staging-admin-ui (7) is next if time remains.

**EX034.** Account `svc-assess-sam` in a custom "Local group readers" role on the three hosts (or a gMSA with that right); valid 09:00–17:00 on the ROE dates; all logons audited; disabled automatically at end of day plus a manual check.

**EX035.** "On lab hosts HV-01 and HV-02, the assessment account was granted local Administrators membership via GPO Lab-Admins; confirmed by group read on 14 March; no exploit used; remove the GPO link and re-verify."

**EX036.** (1) IdP/directory shows the account disabled or deleted; (2) no local leftover admins with that name on sampled hosts; (3) last logon and ticket trail reviewed with no activity after the end timestamp.

**EX037.** "Use the synthetic replica only. No SELECT on columns tagged personal/PII. LIMIT 100 per query. No pg_dump or full-table export. Temporary files destroyed within 24 hours and confirmed in the ticket."

**EX038.** Obtain the `analyst` credentials issued for the test; connect with that role; run `SELECT 1 FROM passengers LIMIT 1` (or equivalent); record success or permission-denied. No crafted payloads.

**EX039.** Safe: product_id, price_cents, zone_code. Forbidden in the course set: passenger_name, payment_card_number (and similar identifiers).

**EX040.** "Discovery and scope checks used TrackScope v0.9.2 (git SHA a1b2c3d), loaded 14 March 09:00 from the internal release bucket."

**EX041.** "Any PR that widens scope (added CIDR/port or removed deny) requires a linked authorization ticket and approval from a second code owner; tightening changes need one owner."

**EX042.** CI with client VPN credentials would test systems without a human-authorized window, could leak secrets into logs/artifacts, and would make builds depend on external networks. Synthetic fixtures keep CI safe and repeatable.

**EX043.** Confidentiality: an unauthorized party who knows the default can read staging fare tables. Integrity: they can change those tables. Availability: they could lock out admins or break staging deploys. All limited to the staging UI asset.

**EX044.** Vulnerability: service account eligible for domain admin. Exposure: the account exists in the lab directory reachable by the assessment role. Risk: Riverstone's judgment of likelihood and impact if that membership were abused — accepted or remediated by them.

**EX045.** "We don't publish a single hackability score — it isn't reproducible and hides trade-offs (Albrecht & Jensen). Here are out-of-scope probes (1), critical opens (2) and planned-technique coverage (71%); we can track those over time."

**EX046.** "TrackScope shall deny targets outside the signed scope and persist reason codes." Verify: unit tests on synthetic scope. "FindingsDesk shall reject finding bodies containing forbidden field names." Verify: schema tests.

**EX047.** Artefact: append-only deny/allow event store. Signal: test T-17 attempts UPDATE on a deny reason and expects rejection/error.

**EX048.** event_id/timestamp, target (host:port), reason_code, policy_version, actor_account — any three of these with clear meaning.

**EX049.** Sensor: count of open findings past SLA by priority. Threshold: critical > 0 or any BREACH. Actuator: ticket escalate + daily digest to owner.

**EX050.** "Page immediately for critical; batch medium/low into a daily digest; suppress duplicates of the same fingerprint for 24 h."

**EX051.** Widening scope or relaxing a stop condition — requires a signed ROE update, not an automatic config push.

**EX052.** Laptop+TrackScope in assess zone; evidence store in tools zone; staging UI in client staging. Controls: allow-list proxy, mTLS to store (or VPN+SSO). Any coherent sketch.

**EX053.** Finding text and evidence references leave the authorized store into an uncleared personal account, breaking confidentiality and retention controls.

**EX054.** "Testing used a synthetic range mirroring staging configuration; results support claims about that configuration under the ROE, not about production runtime behaviour or data."

**EX055.** Which IdP? MFA required for admins? Which groups map to fare-admin? Access token lifetime? Break-glass admin path and its logging?

**EX056.** findings.json MISMATCH. Restore the sealed copy, re-verify hashes, check audit logs for writes after the seal time, and treat uncontrolled edits as a process finding.

**EX057.** "Assessment secrets are never pasted into tickets, chat or git; tickets store only a vault reference id and a last-rotated timestamp."

**EX058.** Example: engagement sequencing → PTES; technical testing guidance → SP 800-115; technique vocabulary/coverage → ATT&CK; regulator-led threat intel scenario → TIBER-EU/CBEST.

**EX059.** "Design and operate an authorized assessment platform that enforces written ROE, records evidence, and measures remediation — never testing outside signed scope."

**EX060.** Working exploit code; scanning systems without written ROE; exporting production personal data into labs; radio tests without spectrum authorization.

**EX061.** Functional: "TrackScope shall deny any target equal to the configured gateway address." Safety: "If the deny-list file is absent or unreadable, TrackScope shall deny all actions and alert."

**EX062.** Given policy path configured but file missing; When any allowed() call; Then result is DENY with reason policy-unavailable and no action proceeds; alert fired.

**EX063.** Conflict: operators want same-day CIDR adds; safety wants dual approval. Chosen rule: widening always needs dual approval and AUTH ticket; emergency adds use a break-glass role that still logs and expires in 4 hours.

**EX064.** In-place edits erase what was authorized at time t; ScopeVersion lets a finding point at the ROE that was live when the action ran.

**EX065.** Re-hash detects change; identical files collapse; tickets reference immutable bytes.

**EX066.** Reject titles matching password-assignment patterns or entropy heuristics; reviewers still check; vault references only in evidence metadata.

**EX067.** Deploy with policy path pointing at an empty mount; call allowed(); expect DENY policy-unavailable and an alert page; no packet leaves.

**EX068.** Every deny event stores authenticated actor id and policy version; storage is append-only; deletes require break-glass dual control.

**EX069.** Platform STRIDE protects assessment integrity and client safety; exploit modules increase dual-use harm and violate the programme boundary — they are not mitigations.

**EX070.** Name: Auth web config review. Purpose: read security-relevant settings. Privilege: app role `assess-read`. Noisy: low. Stop: any write attempt or deny-list host. Artefacts: settings export hash, finding drafts.

**EX071.** Actions without signed ROE are unauthorized; legal/ethical failure regardless of intent.

**EX072.** Report: host 10.20.0.1 probed (deny-list), actions stopped, client contact confirmed, resume only on in-scope hosts — with timestamps.

**EX073.** Signed JSON file: risk = operators forget to sign. Hard-coded policy: risk = redeploys for every ROE change, drift across nodes.

**EX074.** "Deny decisions alert synchronously before returning to the caller so stop conditions meet the one-minute sensor goal; allows may queue asynchronously."

**EX075.** Does it fail closed? Who can publish policy? What happens at 10× action rate?

**EX076.** Criterion: "keeps RF captures inside authorized premises." A high, B high if collectors local, C low if uploads to foreign SaaS.

**EX077.** "Option C rejected: assessment logs and evidence would leave the residency region required by Riverstone policy and the ROE data clause."

**EX078.** When services are down or network to them is out of ROE — run signed policy locally on the jump host for deny/allow only, with manual finding entry.

**EX079.** Preventive: append-only sealed bucket with write-once IAM. Detective: scheduled re-hash job alerts on mismatch.

**EX080.** It demands dual-use skill, is non-deterministic, and can harm the asset; prefer config re-read or authz test.

**EX081.** The concurrency clause — service-enum with conc=20 is DENY concurrency.

**EX082.** `allowed(host: str, port: int, scope: ScopeVersion, ctx: ActionContext) -> tuple[bool, Reason]`. ScopeVersion pins which ROE was evaluated for audit.

**EX083.** The test that asserts DENY deny-list for 10.20.0.1:443 (or equivalent fixture).

**EX084.** Authorization/cookie headers; password, token, or secret query parameters; raw evidence bytes.

**EX085.** coverage = |observed ∩ planned| / |planned| = 5/7 ≈ 71%; list the two planned-not-seen.

**EX086.** Fraction of critical findings closed within SLA with a recorded re-test — not "tickets closed".

**EX087.** Status stays open until a re-test ticket passes; auto-close on vendor promise is forbidden.

**EX088.** ID V-04; setup: empty policy mount; action: allowed(any); expected: DENY policy-unavailable + alert; evidence: log hash.

**EX089.** Halt lab, open blocker, revoke engagement approval until fix and re-lab pass.

**EX090.** Scope/policy file hash, TrackScope build/version hash, lab result log hash.

**EX091.** Network retry can create two findings with different server ids; clients should PUT known ids.

**EX092.** `{"title":"x","payload":"..."}` or `{"password":"..."}` or `{"risk_score":42}` — any forbidden/unknown per policy.

**EX093.** No — renaming breaks clients; keep reason_code in v1 or ship /v2/.

**EX094.** "During signed engagement hours, deny-path success ≥ 99.5% measured by synthetic probes every minute; outages page the lead."

**EX095.** Expected attempts = 1 + (1-p) + (1-p)^2 = 1 + 0.2 + 0.04 = 1.24 (geometric truncated); ≈1.248 with continuous form discussion also ok.

**EX096.** Scope and policy evaluation — must fail closed, never ALLOW when uncertain.

**EX097.** Drop file `/var/lib/trackscope/STOP` via SSH/SSO; TrackScope polls every 10s; if present or unreadable, deny all and alert.

**EX098.** Previous signed binary available; ScopeVersion unchanged or re-verified; client contact notified of the rollback.

**EX099.** "At 11:10 monitoring shows a probe to deny-listed 10.20.0.1; lead is in a tunnel with spotty signal."

**EX100.** So reviewers know which ScopeVersion authorized the decision when the event fired.

**EX101.** Consumer stores processed event_ids; duplicates are ignored or upserted without new tickets.

**EX102.** A sample event JSON for the new reason, and the expected FindingsDesk ticket fields after consume.

**EX103.** "Share of *planned* techniques observed in this engagement — not a residual risk or compliance score."

**EX104.** "We don't ship red/amber/green risk badges; use the finding list and SLA breach count instead."

**EX105.** technique_id, name, planned (Y/N), observed (Y/N), first_seen_utc, notes.

**EX106.** Two workers if each saturates 1/s; better one worker behind a 2/s bucket. Note coordination if distributed.

**EX107.** flood_served=64/3000 at limit=1/s burst=5.

**EX108.** Each may send 5/s → ~15/s aggregate, triple the ROE — need a shared limiter.

**EX109.** Disable assess accounts; rotate vault secrets; seal evidence hashes; export coverage/SLA metrics; confirm kill-switch clear; book retro; notify client of end timestamp.

**EX110.** Open finding ids + status; last processed event_id; pending approval requests; kill-switch state — any three+.

**EX111.** Three breaches (SYN-005, SYN-004, SYN-006); open=5.

**EX112.** Authorized single login attempt with the old default; expect failure; capture status; store hash; stop; no password list.

**EX113.** Otherwise metrics lie and SLAs look green while risk remains.

**EX114.** "Re-test confirmed staging only; production was out of scope for validation."

**EX115.** Pin exact version for the window; emergency patches need a mini verification lab (Chapter 30) before swap.

**EX116.** `put_evidence(key: Hash, body: bytes) -> None` / `get_evidence(key) -> bytes`.

**EX117.** "Owner: Platform Assessment squad (primary Sam Ito); backup: On-call security eng; contact: #findingsdesk."

**EX118.** Otherwise PulseMap claims observed techniques without a durable finding record — metric lies under partial failure.

**EX119.** Continues allow/deny from local policy; queues drafts; alerts on queue growth; never ALLOW on policy errors.

**EX120.** Implementer of the change and a second engineer who did not write the code (reviewer).

**EX121.** Skipping deny-list for previously allowed hosts, or failing open when the policy service is slow.

**EX122.** Cache key includes policy version, host, port, and context flags; short TTL; hard invalidate on policy publish.

**EX123.** Engagement hours are scarce; schedule high exposure×blast assets first (lab ranking).

**EX124.** "Does requiring a denominator in coverage reports reduce executive over-claims of 'percent secure' in post-engagement surveys?"

**EX125.** Count of scope-widening merges without AUTH ticket per quarter (or blocked attempts).

**EX126.** "That project crosses the course dual-use line; consider studying fail-closed rates or re-test policies instead."

**EX127.** "If the authorization rules file cannot be loaded, the system refuses all test actions and alerts staff — it does not continue under uncertainty."

**EX128.** "Host depot-sql-prod-03" → "synthetic host db-01 in the Riverstone lab range".

**EX129.** Data residency; procurement bans on foreign SaaS; retention/FOIA logging requirements; change advisory boards — any two concrete.

**EX130.** No residual-risk badge; no live ATT&CK auto-discovery on client nets; no storage of payloads.

**EX131.** "Kill-switch file stops all allows within 30s — acceptance: unit+lab V-KS green on synthetic."

**EX132.** Work uses synthetic data under course ROE. No unauthorized targets. No exploit development. Accidental live issues go to responsible disclosure, not the report appendix.

**EX133.** "Blocking: on policy-service timeout this retries then ALLOW — violates S-3 fail-closed. Change to DENY+alert before merge."

**EX134.** "Radio: confirms authorization lists bands/locations and that captures stay on-prem."

**EX135.** "Dissent: I still prefer sync alerts for allows during the first week of a new policy; overruled in ADR-019."

**EX136.** Safety/blocker fixes and doc corrections; no feature work.

**EX137.** Code+tests, Lab II report with hashes, ADR, runbook update, operator tutorial, ethics statement — any five.

**EX138.** After Lab II sign-off and before any authorized engagement uses the build.

**EX139.** Inject: delete policy file. Expect: DENY all within 30s, alert, no ALLOW.

**EX140.** Seconds from inject to first deny-all decision (and alert fired).

**EX141.** "Tighten TrackScope policy poll from 15s to 5s — trial deny-all was 45s > 30s SLO".

**EX142.** `roe.pdf sha256 18d7…`; `scope.json sha256 01cc…`; `findings.json sha256 7f5f…`.

**EX143.** ROE PDF → sealed evidence; scratch notes → working, delete at 90 days or sooner.

**EX144.** Remove from store, rotate the exposed secret, open a process finding, re-seal manifest, notify owner.

**EX145.** "Requiring dual approval and an AUTH ticket for scope-widening merges reduced unapproved widen attempts to zero in 12 weeks of Riverstone synthetic CI data."

**EX146.** "Trials used synthetic fixtures, not live client traffic. Results may not transfer to organizations without CODEOWNERS. We did not measure reviewer fatigue."

**EX147.** https://doi.org/10.6028/NIST.SP.800-115

**EX148.** Claim; synthetic demo; Lab II results; failure-trial lesson; limits/ethics; questions.

**EX149.** "I don't produce a single residual-risk score — it isn't reproducible (Albrecht & Jensen). Here are critical opens, SLA breaches and planned-technique coverage with denominators; those are what we track."

**EX150.** Example: "We cached allow decisions without policy version in the key; a publish left stale ALLOWs. Fix: include ScopeVersion in the cache key and hard-invalidate on publish."

<a id="references"></a>

## References

Links checked 12 October 2026; frameworks change, so re-verify. arXiv identifiers were opened and titles checked.

- Albrecht, M. R., Jensen, R. B. (2020). The Vacuity of the Open Source Security Testing Methodology Manual. arXiv:2010.06377.
- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide (2024 update). <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- MITRE ATT&CK. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
