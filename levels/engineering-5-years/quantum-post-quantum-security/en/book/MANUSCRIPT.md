# Quantum and Post-Quantum Security: Engineering Quantum-Resistant Systems

- Language: English (`en`); engineering course, five years; approximately 4,000 hours of planned study.
- Editorial state: **draft**. Chapters 1–50 of 50 have authored teaching text; exercises EX001–EX100 (two per chapter) have matching worked results; offline labs use the Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: future security systems designers who will design, build and validate systems that remain secure when large quantum computers exist. Entry knowledge: calculus, computing, networks and systems engineering at school-leaving or first-year level.
- Relation to neighbouring books: the [master's](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) and [doctoral](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) books in this area study PQC deployment empirically. **This book is about engineering the migration**: the mathematics under lattice, hash and code-based schemes, inventory, requirements, hybrid PQ/T architecture, crypto-agility, implementation, verification, operations and a capstone.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited degree or licence. No authority to test real systems. All organizations, people and numbers in examples are **synthetic** unless a sentence cites a public source. Toy cryptography in the labs is deliberately insecure; production systems must use vetted implementations of [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) and [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208).

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Fifty chapters run in ten stages over five years: foundations (1–19), the PQC engineering core (20–42) and practice, capstone and defense (43–50). Each chapter has learning outcomes, teaching, a worked example, a practical activity, common errors, two exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs run offline with Python 3; the printed output is shown so you can check your run.

### The running case: Brightwater Port Authority

**Brightwater Port Authority (BPA)** is a synthetic container port. It runs a terminal operating system, a customs data exchange whose records must stay confidential for 25 years, site-to-site VPNs with shipping lines, an internal PKI that signs electronic bills of lading (which must remain verifiable for at least 12 years), signed firmware for gate scanners and cranes, and a public web portal. BPA's board has asked engineering to make the port's cryptography quantum-resistant without disrupting operations. Every number about BPA is invented.

### Source policy

Primary sources were checked on 12 October 2026: NIST FIPS 203/204/205 (August 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (initial public draft)](https://doi.org/10.6028/NIST.IR.8547.ipd), [NIST IR 8545](https://doi.org/10.6028/NIST.IR.8545), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) and [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). FN-DSA (FIPS 206) and the HQC standard were still in development. Re-verify status before relying on it.

## Contents

| Stage | Chapters |
|---|---|
| Foundations | [1 Calculus I](#ch-01) · [2 Discrete mathematics](#ch-02) · [3 Physics for computing](#ch-03) · [4 Programming I](#ch-04) · [5 Engineering communication](#ch-05) · [6 Calculus II](#ch-06) · [7 Probability and statistics](#ch-07) · [8 Computer architecture](#ch-08) · [9 Programming II](#ch-09) · [10 Engineering ethics and safety](#ch-10) · [11 Networks and protocols](#ch-11) · [12 Operating systems](#ch-12) · [13 Data systems](#ch-13) · [14 Software engineering](#ch-14) · [15 Security fundamentals](#ch-15) · [16 Systems engineering](#ch-16) · [17 Control and feedback basics](#ch-17) · [18 Security architecture](#ch-18) · [19 Identity and cryptography](#ch-19) |
| PQC core | [20 Engineering context](#ch-20) · [21 Requirements](#ch-21) · [22 System and data models](#ch-22) · [23 Threat and failure analysis](#ch-23) · [24 Methods I](#ch-24) · [25 Design studio I](#ch-25) · [26 Architecture alternatives](#ch-26) · [27 Control design](#ch-27) · [28 Implementation I](#ch-28) · [29 Measurement](#ch-29) · [30 Verification laboratory I](#ch-30) · [31 Implementation II](#ch-31) · [32 Reliability](#ch-32) · [33 Safety and resilience](#ch-33) · [34 Integration](#ch-34) · [35 Design studio II](#ch-35) · [36 Performance and scale](#ch-36) · [37 Operations](#ch-37) · [38 Validation](#ch-38) · [39 Maintainability](#ch-39) · [40 Verification laboratory II](#ch-40) · [41 System optimization](#ch-41) · [42 Applied research](#ch-42) |
| Practice and capstone | [43 Industry or public-service practice](#ch-43) · [44 Capstone I](#ch-44) · [45 Independent design review](#ch-45) · [46 Capstone II](#ch-46) · [47 Failure and recovery trial](#ch-47) · [48 Evidence dossier](#ch-48) · [49 Engineering thesis](#ch-49) · [50 Final defense](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) compare growth rates — polynomial, sub-exponential and exponential — and explain why they decide what a quantum computer threatens; (2) use logarithms to convert work factors into "bits of security"; and (3) read an asymptotic claim critically. This chapter starts the foundations stage and prepares the discrete mathematics of Chapter 2.

### 1.1 Why an engineer needs growth rates

Every security claim in this book is a claim about how fast some cost grows. Brute-forcing a *k*-bit key takes about 2^*k* trials: the cost doubles with each extra bit, which is **exponential** growth. The best classical factoring algorithm, the general number field sieve, runs in **sub-exponential** time, roughly exp(c·(ln N)^(1/3)·(ln ln N)^(2/3)) for a modulus *N*. Shor's algorithm factors in time **polynomial** in the number of bits — on the order of *n*³ elementary quantum gates for an *n*-bit modulus, ignoring error-correction overhead ([Shor 1997](https://doi.org/10.1137/S0097539795293172)). Grover's search finds a key among 2^*k* candidates in about 2^(*k*/2) sequential iterations ([Grover 1996](https://doi.org/10.1145/237814.237866)). The whole PQC story follows from these four functions: Shor turns a sub-exponential problem into a polynomial one, which is catastrophic for RSA and elliptic curves; Grover only halves the exponent, which is why AES-256 remains acceptable.

### 1.2 Logarithms and bits of security

Taking log₂ of a work factor gives "bits of security". A cost of 2^128 operations is "128-bit security". Logarithms turn products into sums, so doubling the work adds one bit, and multiplying it by a million (≈2^20) adds about twenty bits. This is why engineers say a 2^20 speed-up from better hardware "costs" twenty bits. The derivative helps intuition: the GNFS cost curve flattens in bits as keys grow, so each extra RSA bit buys less security than each extra AES bit — one reason RSA keys are thousands of bits long.

### 1.3 Limits and asymptotic notation

"Big-O" statements describe behaviour as input size tends to infinity and hide constants. Shor's *n*³ hides a large constant and, more importantly, the overhead of quantum error correction, which may multiply physical qubit counts by a thousand or more. Resource estimates such as [Gidney (2025)](https://arxiv.org/abs/2505.15917) — under one million noisy qubits for RSA-2048 under stated hardware assumptions — fill in those constants. An engineer must never read an asymptotic bound as a time.

Two algorithms with the same big-O can differ by factors that decide whether an attack takes an hour or a decade. The jump from twenty million noisy qubits to under a million came from better constants and codes, not from a change in Shor's n³. When a vendor quotes an asymptotic bound, the engineer asks for the hardware assumptions behind the constant.

### 1.4 Practical activity — Lab G

```python
# Lab G (ch 1): growth rates that decide what quantum computers threaten.
import math
print("Symmetric key search: classical 2^k trials vs Grover ~2^(k/2) sequential iterations")
for k in (128, 192, 256):
    print(f"  k={k}: classical 2^{k}, Grover ~2^{k//2}")
def gnfs_bits(n_bits):            # heuristic L_N[1/3, (64/9)^(1/3)] work, expressed in bits
    ln_n = n_bits * math.log(2)
    work = (64/9) ** (1/3) * ln_n ** (1/3) * math.log(ln_n) ** (2/3)
    return work / math.log(2)
print("Factoring an n-bit RSA modulus: classical GNFS (heuristic) vs Shor gate count ~n^3")
for n in (1024, 2048, 3072):
    print(f"  n={n}: GNFS ~2^{gnfs_bits(n):.0f} operations; Shor ~n^3 = 2^{math.log2(n**3):.0f} logical gates")
```

Expected output:

```text
Symmetric key search: classical 2^k trials vs Grover ~2^(k/2) sequential iterations
  k=128: classical 2^128, Grover ~2^64
  k=192: classical 2^192, Grover ~2^96
  k=256: classical 2^256, Grover ~2^128
Factoring an n-bit RSA modulus: classical GNFS (heuristic) vs Shor gate count ~n^3
  n=1024: GNFS ~2^87 operations; Shor ~n^3 = 2^30 logical gates
  n=2048: GNFS ~2^117 operations; Shor ~n^3 = 2^33 logical gates
  n=3072: GNFS ~2^139 operations; Shor ~n^3 = 2^35 logical gates
```

The GNFS formula is heuristic (its *o*(1) term is dropped), so the bit values approximate the commonly quoted 112-bit strength of RSA-2048 rather than match it. The Shor "gate counts" are logical gates before error correction.

The lab's comparison exists to make the shapes visible side by side: brute force doubles per bit, GNFS bends more slowly, and Shor's logical gate count grows only polynomially. Running it for 1024, 2048 and 3072-bit moduli shows why longer RSA keys buy little against a quantum adversary. Students should annotate their table with the warning that the Shor column omits error-correction overhead, so no row should be read as a time to break.

### 1.5 Worked example: BPA's first question

BPA's board asks whether to double AES key sizes "because of quantum". Using 1.1: AES-128 under Grover falls to roughly 2^64 sequential iterations in the idealized model, but Grover parallelizes poorly, so many guidance documents still accept AES-128; moving bulk encryption to AES-256 is cheap and removes the debate. The urgent item is not AES but every RSA and elliptic-curve key exchange, which Shor breaks outright.

The memo to BPA's board therefore separates two decisions. Symmetric keys move to AES-256 during normal refresh, at almost no cost. Key exchange and signatures need a planned migration to ML-KEM and ML-DSA, because no key length rescues RSA or elliptic curves from Shor. Mixing the two questions is how boards spend money on the cheap fix and delay the important one.

### 1.6 Common errors and limits

- Treating Grover as fatal to symmetric cryptography.
- Reading *O*(*n*³) as "fast" without error-correction overhead.
- Comparing bits across exponential and sub-exponential curves as if they grew alike.

Each error leads to a wrong decision. Treating Grover as fatal sends budget to symmetric upgrades that were already adequate. Reading n³ as fast ignores the physical qubits needed for each logical one. Comparing bit numbers across different growth curves makes RSA-3072 look stronger against quantum attack than it is. The models in this chapter compare options; they are not schedules.

### Exercises

- **EX001 — Bits from work.** Convert 10^30 and 2^100 × 10^6 operations into bits of security. Rubric: 3 = both correct with method.
- **EX002 — Explain the asymmetry.** In 150 words, explain to BPA's board why RSA must be replaced but AES-256 need not. Rubric: 3 = growth-rate argument correct and non-technical.

### Synthesis

Growth rates decide everything: Shor makes factoring and discrete logarithms polynomial; Grover merely square-roots search. Bits of security are logarithms of work, and asymptotic bounds need resource estimates before they mean time.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) compute in modular arithmetic and polynomial rings; (2) explain the ring Z_q[x]/(x^n+1) used by ML-KEM and ML-DSA; (3) state what a hash function's security properties are; and (4) connect group structure to why Shor's algorithm works. It builds on Chapter 1 and prepares probability (Chapter 7) and the lattice methods of Chapter 24.

### 2.1 Modular arithmetic

Arithmetic modulo *q* keeps numbers in {0, …, *q*−1}. RSA uses a composite modulus; elliptic-curve cryptography uses groups of points over a prime field. Both rely on the hardness of finding a hidden *period* — the order of an element, or a discrete logarithm. Shor's insight is that a quantum computer can find periods efficiently with the quantum Fourier transform; that is why every scheme whose security reduces to a hidden period in an abelian group falls together.

This shared weakness is why migration cannot be done one algorithm at a time by swapping RSA for elliptic curves: both fall to the same idea. Post-quantum schemes are chosen precisely because their hard problems, such as noisy linear equations or hash inversion, have no known hidden period for a quantum computer to find.

### 2.2 Polynomial rings

ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)) computes with polynomials of degree below 256 whose coefficients are integers modulo *q* = 3329, reduced modulo *x*^256 + 1. In this ring, multiplying by *x* shifts coefficients up one place, and the coefficient that falls off the top wraps to the bottom with its sign flipped, because *x*^*n* = −1. Vectors and matrices of such polynomials form a *module*, hence "module-lattice". The structure gives compact keys and fast multiplication (via the number-theoretic transform), while hardness comes from adding small noise — the subject of Chapter 24.

### 2.3 Practical activity — Lab R

```python
# Lab R (ch 2): multiplication in R_q = Z_q[x]/(x^n + 1), the ring behind ML-KEM (there n=256, q=3329).
q, n = 17, 4
def mul(a, b):
    c = [0] * n
    for i in range(n):
        for j in range(n):
            k = i + j
            if k < n:
                c[k] = (c[k] + a[i] * b[j]) % q
            else:                       # x^n = -1, so wrap around with a sign flip
                c[k - n] = (c[k - n] - a[i] * b[j]) % q
    return c
a = [1, 2, 0, 3]      # 1 + 2x + 3x^3
b = [0, 1, 0, 0]      # x
print("a*x  =", mul(a, b), " (coefficients shift; x^3 * x = x^4 = -1 -> 17-3 = 14)")
print("a*a  =", mul(a, a))
```

Expected output:

```text
a*x  = [14, 1, 2, 0]  (coefficients shift; x^3 * x = x^4 = -1 -> 17-3 = 14)
a*a  = [6, 4, 12, 6]
```

Check by hand: (1 + 2*x* + 3*x*³)·*x* = *x* + 2*x*² + 3*x*⁴ = *x* + 2*x*² − 3 ≡ 14 + *x* + 2*x*² (mod 17).

The hand check shows the wrap-around rule at work: the x⁴ term exceeds the degree limit for n equal to four, so it becomes minus three, and minus three modulo seventeen is fourteen. ML-KEM uses the same rule with n equal to 256 and q equal to 3329. Students who get the sign wrong will compute a different polynomial, and in a real implementation that mistake would break every decapsulation, which is why known-answer tests catch it at once.

### 2.4 Hash functions

A cryptographic hash maps any input to a fixed-length digest. Its required properties are *preimage resistance* (given a digest, find no input), *second-preimage resistance* and *collision resistance*. Hash-based signatures (SLH-DSA in [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205); LMS and XMSS in [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208)) need only these properties, which is why they are the most conservative post-quantum signatures: quantum computers are not known to do much better than Grover-style speed-ups against good hash functions.

Grover can search for preimages faster, roughly square-rooting the work, so a 256-bit hash still offers about 128 bits against preimage search. Collision search with quantum algorithms gains less in practice than the idealised bounds suggest. The trade-off for hash-based signatures is size and speed, not security assumptions.

### 2.5 Worked example

A BPA developer asks why the post-quantum library "multiplies polynomials" when RSA "just exponentiates". The answer: RSA's security lives in the multiplicative group modulo *N*, where Shor finds periods. ML-KEM's lives in noisy linear algebra over a polynomial ring, where no period-finding shortcut is known; the ring is for efficiency, the noise is for security.

The developer's follow-up is usually about cost: polynomial multiplication with the number-theoretic transform is fast, and ML-KEM key generation is often quicker than RSA key generation. What changes for the system is size: keys and ciphertexts are larger than elliptic-curve ones. That shifts the engineering problem from CPU time to bytes on the wire.

### 2.6 Common errors and limits

- Forgetting the sign flip when reducing by *x*^*n* + 1.
- Thinking ring structure alone provides security (without noise, the linear system is easy).
- Confusing collision resistance with preimage resistance.

A missed sign flip produces outputs that look plausible but fail interoperability tests against the standard. Assuming the ring alone gives security misses the role of noise: without small errors, Gaussian elimination recovers the secret. Mixing up collision and preimage resistance leads to wrong parameter claims, for example halving a hash length for a use that only needs preimage resistance.

### Exercises

- **EX003 — Ring multiplication.** Compute (2 + *x*)(3 + *x*³) in Z_17[*x*]/(*x*⁴ + 1) by hand and check with Lab R. Rubric: 3 = correct with reduction steps.
- **EX004 — Hash properties.** For each of SLH-DSA, a file-integrity manifest and password storage, state which hash property matters most. Rubric: 3 = correct and justified.

### Synthesis

Traditional public-key cryptography hides a period that Shor's algorithm finds; lattice schemes compute in a polynomial ring and hide secrets under noise; hash-based schemes rely only on hash properties.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) describe a qubit, superposition, measurement and entanglement in engineering terms; (2) explain decoherence and why error correction dominates the cost of a quantum computer; (3) distinguish physical from logical qubits; and (4) separate quantum computing from quantum key distribution. It builds on Chapters 1–2 and frames the threat used throughout the book.

### 3.1 Qubits and measurement

A classical bit is 0 or 1. A qubit's state is a combination α|0⟩ + β|1⟩ with complex amplitudes whose squared magnitudes sum to one; measurement returns 0 with probability |α|² and 1 with probability |β|², and destroys the superposition. *n* qubits are described by 2^*n* amplitudes, but measurement yields only *n* bits, so a quantum algorithm must arrange interference so that wrong answers cancel and right answers reinforce. Shor's algorithm does this for periods; for most problems no such arrangement is known, which is why quantum computers are not general accelerators.

### 3.2 Entanglement and gates

Entangled qubits have correlated measurement outcomes that cannot be explained by independent states. Gates — rotations of single qubits and controlled operations on pairs — build circuits. Algorithms are measured in logical gate counts and circuit *depth*, the number of sequential layers, which matters because errors accumulate with time.

Depth matters because qubits decohere while they wait: a circuit with many sequential layers must finish before errors overwhelm it, or error correction must keep up. That is why resource estimates report both logical qubits and a runtime figure. Entanglement is a resource algorithms use, not a speed-up on its own; most problems gain nothing from it.

### 3.3 Decoherence and error correction

Physical qubits lose their state through interaction with the environment (decoherence) and through imperfect gates. Quantum error correction encodes one *logical* qubit in many *physical* qubits — in surface-code designs, hundreds to thousands — and continuously measures syndromes to correct errors. This overhead is why estimates for breaking RSA-2048 moved from twenty million noisy qubits ([Gidney and Ekerå 2021](https://doi.org/10.22331/q-2021-04-15-433)) to under a million ([Gidney 2025](https://arxiv.org/abs/2505.15917)) as algorithms and codes improved — and why counts of physical qubits in press releases say little about cryptographic relevance without error rates.

### 3.4 Quantum key distribution is different

Quantum key distribution (QKD) uses quantum states of light to agree keys, with security grounded in physics, but it needs special hardware, point-to-point links and authenticated classical channels, and it does not provide signatures. Several agencies, including the [NSA](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/), recommend PQC rather than QKD for most uses. This book treats QKD as a niche technology and PQC as the migration path.

QKD also leaves authentication to classical cryptography, so a QKD link still needs signatures or pre-shared keys, which brings PQC back into the design. Its distance limits and trusted-node relays add physical security problems. For BPA's customs exchange over the public internet, QKD is not an option, while hybrid TLS with ML-KEM can be deployed on existing servers.

### 3.5 Worked example

A vendor tells BPA that "a 1,000-qubit machine was announced, so RSA is broken soon". The engineering response: ask for error rates, logical qubit counts and circuit depth; compare with published resource estimates; note that a thousand noisy physical qubits is orders of magnitude short of the estimates; and still migrate, because recorded traffic must stay secret for decades (Chapter 20).

The vendor's number answers none of the questions that matter for RSA-2048. Physical qubits must be turned into logical ones at a ratio of hundreds or thousands, and the circuit must run long enough without failure. Even so, the conclusion is to keep migrating: the case for action rests on how long customs data must stay secret, not on the date of the next announcement.

### 3.6 Common errors and limits

- Saying quantum computers "try all answers at once".
- Equating physical and logical qubits.
- Presenting QKD as a replacement for PQC.

Superposition does not let a quantum computer read out all answers; measurement returns one result, and only interference designed for a specific structure helps. Physical and logical qubits differ by error-correction overhead, so headlines about qubit counts say little about cryptographic risk. QKD needs dedicated links and leaves signatures unsolved, so it cannot replace PQC across ordinary networks such as the internet links BPA's partners use.

### Exercises

- **EX005 — Overhead arithmetic.** If a logical qubit needs 1,000 physical qubits and an algorithm needs 1,400 logical qubits plus 30% ancilla overhead, how many physical qubits are needed? Rubric: 3 = correct (1.82 million) and comment on assumptions.
- **EX006 — Vendor claim.** Write three questions that turn a qubit-count announcement into evidence. Rubric: 3 = error rate, logical count, depth/time.

### Synthesis

Quantum algorithms exploit interference for special problems; error correction makes useful machines enormous; announcements must be translated into logical resources; QKD is not the migration path.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write small, testable Python programs with the standard library; (2) handle bytes, encodings and integers correctly; (3) use `hashlib`, `hmac` and `secrets` safely; and (4) recognize why you must not implement production cryptography yourself. It prepares the labs used throughout the book.

### 4.1 Bytes, not strings

Cryptographic functions operate on bytes. Python's `str` is text; convert with an explicit encoding (`"text".encode("utf-8")`). Mixing them causes subtle bugs, such as hashing the string representation of a byte object (`"b'...'"`) instead of the bytes themselves. Integers convert with `int.from_bytes(b, "big")` and `n.to_bytes(length, "big")`; always state the byte order and length, because protocol specifications such as FIPS 203 define exact encodings.

A common symptom of mixing types is two systems computing different hashes for the same message because one encoded text as UTF-8 and the other as Latin-1. Fixing the encoding at the boundary, and passing bytes everywhere inside, removes that class of bug. Length and byte order matter too: FIPS 203 encodes coefficients in a precise bit layout, and a test against the standard's vectors is the only reliable check.

### 4.2 Randomness

Use `secrets.token_bytes()` for keys and nonces; never `random`, which is a predictable pseudo-random generator designed for simulations. The labs in this book use `random` only to generate synthetic data and toy parameters, and say so.

Python's `random` is seeded from a state that can be recovered after observing enough outputs, so any key it produces can be predicted. `secrets` draws from the operating system's cryptographic generator. Keeping the two visibly separate in code, for example by never importing `random` in production modules, makes reviews easier and stops toy code from slipping into real systems.

### 4.3 Hashes and MACs

`hashlib.sha256`, `hashlib.sha3_256` and `hashlib.shake_256` are available; SHA-3 and SHAKE are used inside ML-KEM and ML-DSA. `hmac.new(key, msg, hashlib.sha256)` computes a message authentication code, and `hmac.compare_digest` compares tags in constant time — a normal `==` can leak timing information about where two values first differ.

SHAKE is an extendable-output function: it can produce as many output bytes as needed, which ML-KEM uses to expand seeds into matrices. A MAC differs from a hash because it needs a secret key; without one, anyone can recompute a hash over a modified message. The constant-time comparison matters most when an attacker can submit many guesses and measure response times.

### 4.4 Testing

Every function gets a test with a known answer. For cryptography, *known-answer tests* (KATs) published with standards let you confirm that an implementation produces exactly the expected bytes. NIST's Cryptographic Algorithm Validation Program publishes test vectors for approved algorithms.

A KAT fixes the inputs, including what would normally be random, so the expected output is a single exact byte string. Passing KATs proves the implementation matches the standard on those inputs; it does not prove resistance to side channels or misuse. Engineers run KATs in continuous integration so that a library upgrade that changes outputs is caught before deployment.

### 4.5 Worked example: a hash-chain audit log

BPA wants tamper-evident logs. Each entry stores `h_i = SHA-256(h_{i-1} || entry_i)`. A short program computes the chain, and a test verifies that changing any entry changes every later hash. The program uses bytes throughout, fixed encodings and `compare_digest`. This is a sound use of standard primitives; designing a new signature scheme would not be.

The chain detects modification, deletion and reordering, because each change alters every later hash. It does not stop someone with write access from rebuilding the whole chain, so BPA publishes the latest hash daily to a separate system. The program is short enough to review completely, and every primitive it uses is already standardised.

### 4.6 Practical activity

Write the hash-chain function with a test, then add a deliberate bug (hashing `str(entry)` instead of `entry`) and see the test catch it.

The deliberate bug shows why tests must compare exact bytes: hashing `str(entry)` hashes the text "b'...'" with quotes and a prefix, so every later hash changes even though the log content looks identical. Write the failing test first, confirm it fails with the bug, then fix the code and confirm it passes. Keep the test in the suite so the mistake cannot return.

### 4.7 Common errors and limits

- Using `random` for keys.
- Comparing secrets with `==`.
- Implementing ML-KEM or ML-DSA yourself for production: implementation security (Chapter 31) is harder than correctness.

Each error has caused real failures. Predictable random numbers have exposed keys, plain comparisons have leaked authentication tags through timing, and home-made implementations of standard algorithms have passed correctness tests while leaking secrets through timing or power use. BPA uses vetted libraries for ML-KEM and ML-DSA and reserves its own code for the glue around them, which it tests with KATs.

### Exercises

- **EX007 — Encoding bug.** Explain why `hashlib.sha256(str(b"abc").encode())` differs from `hashlib.sha256(b"abc")` and what bug class it represents. Rubric: 3 = correct and generalized.
- **EX008 — Hash chain.** Write the hash-chain function and a test that detects tampering. Rubric: 3 = runs, tests pass, uses bytes and `compare_digest`.

### Synthesis

Cryptographic code is byte-exact, uses secure randomness, compares secrets in constant time, and is tested against known answers; engineers compose vetted primitives rather than inventing them.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write a decision memo that separates facts, assumptions and recommendations; (2) present uncertainty about quantum timelines honestly; (3) draw architecture diagrams with text alternatives; and (4) adapt a message for technical and executive audiences. It builds on Chapters 1–4 and is used in every design review later.

### 5.1 The decision memo

A memo opens with the decision requested, then gives context, options, recommendation, risks and what would change the recommendation. In PQC work, label four kinds of statement: **fact** ("FIPS 203 was published in August 2024"), **assumption** ("we plan as if a cryptographically relevant quantum computer could exist within 15 years"), **estimate** ("migration of the VPN will take nine months") and **recommendation**. Mixing them is how timelines become myths.

Labelling each statement lets readers challenge the right thing. A fact can be checked against its source; an assumption can be varied to see whether the recommendation still holds; an estimate can be compared with actual progress later. When a sentence mixes them, such as a migration date presented as certain, nobody can tell which part to question.

### 5.2 Communicating uncertainty

Never give a single "Q-Day". State a range of assumptions and show which decisions are robust across it. Mosca's inequality — if data lifetime plus migration time exceeds time-to-quantum, act now ([Mosca 2018](https://doi.org/10.1109/MSP.2018.3761723)) — is useful precisely because it can be evaluated across a range. A recommendation that holds for all plausible ranges is easy to defend.

In practice, the memo shows a small table: rows for assumed time-to-quantum, columns for data lifetime and migration time, and cells marking where action is needed. If every cell says act, the debate about the exact year becomes irrelevant. If the answer flips within the plausible range, the memo says so and explains what new evidence would settle it.

### 5.3 Diagrams

Architecture diagrams show components, trust boundaries and where each cryptographic function happens: key exchange, signature, data at rest. Every diagram needs a text alternative describing the same content for accessibility and for review; reviewers often find errors when forced to read the text version.

Marking where each cryptographic function happens shows the migration scope at a glance: every key exchange and signature arrow is a candidate for change, while symmetric encryption at rest may only need larger keys. The text version lists each arrow with its algorithm and owner. Reviewers reading that list often spot a hidden dependency, such as a signature used inside a firmware update path that the diagram drew as a single box.

### 5.4 Audiences

For engineers: algorithms, parameter sets, protocols, test evidence. For executives: risk, cost, schedule, what is protected and what is not. For auditors: requirement traceability and evidence. The same facts, differently ordered.

An engineer reading the executive version may think detail is missing, and an executive reading the engineering version may miss the decision. Writing separate versions from one source of facts keeps them consistent. Auditors need a third ordering: each requirement, the evidence that it is met, and where that evidence is stored. BPA keeps all three versions in one repository so a changed fact updates every audience together.

### 5.5 Worked example: BPA's one-page memo

Decision requested: fund a 12-month cryptographic inventory and a hybrid TLS pilot. Facts: standards exist; customs records must remain confidential for 25 years. Assumption: time-to-quantum swept from 10 to 30 years. Finding: for 25-year records, any time-to-quantum below about 26 years (25 years of confidentiality plus roughly 9 months of migration) means today's recorded traffic is at risk — so the decision is robust across the whole 10–30-year sweep except its optimistic tail, and the tail does not change the action. Not claimed: any date. Risks: middlebox incompatibility, vendor delay.

### 5.6 Common errors and limits

- Executive slides with a single date for quantum computers.
- Diagrams without text alternatives.
- Memos that bury the decision on page three.

A single date invites argument about the date instead of the decision, and it becomes wrong as soon as estimates move. A diagram without text excludes readers using screen readers and hides errors that writing would expose. A buried decision means executives leave the meeting without making it. Each of these is easy to fix before the memo is sent.

### Exercises

- **EX009 — Label statements.** Label ten sentences from a vendor brochure as fact, assumption, estimate or recommendation. Rubric: 3 = all correct with justification for borderline cases.
- **EX010 — Executive rewrite.** Rewrite a technical paragraph on ML-KEM parameter choice for BPA's board in 100 words. Rubric: 3 = accurate, no jargon, decision clear.

### Synthesis

Good engineering communication labels facts, assumptions, estimates and recommendations, expresses timelines as ranges, gives diagrams text alternatives and orders the same facts for each audience.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use exponential and logarithmic models for growth and decay; (2) compute sums and integrals that appear in cost and risk models; (3) apply optimization to choose parameters under constraints; and (4) model the "harvest-now, decrypt-later" exposure window. It builds on Chapter 1 and supports performance (Chapter 36) and optimization (Chapter 41).

### 6.1 Exponential models

Many quantities in this field are modelled exponentially: the volume of recorded traffic, the decline in cost per qubit, the decay of a certificate's usefulness. A model *f*(*t*) = *f*₀·*e*^(*rt*) has doubling time ln 2 / *r*. Engineers should treat such models as scenarios: an assumed doubling time of qubit quality is an assumption, not a law.

Doubling time is the most intuitive way to state an exponential model: if recorded traffic doubles every 3.8 years, a reader can picture the growth without logarithms. Showing results under a fast and a slow scenario keeps the model honest. If the recommendation changes between scenarios, the memo must say which assumption drives the change.

### 6.2 Sums and integrals for exposure

Suppose BPA records traffic at a rate *v*(*t*) GB per year, and any traffic recorded before migration date *T* is exposed if a CRQC appears at time *Z*. The exposed volume is the integral of *v* from 0 to *T*. If *v* grows exponentially, ∫₀^*T* *v*₀*e*^(*rt*) d*t* = (*v*₀/*r*)(*e*^(*rT*) − 1): delaying migration grows exposure faster than linearly. The engineering lesson is that a one-year delay late in the programme costs more exposure than a one-year delay early.

### 6.3 Optimization

Parameter choice is constrained optimization. Example: choose an ML-KEM parameter set to maximize security subject to a handshake byte budget. ML-KEM-512, -768 and -1024 offer NIST categories 1, 3 and 5 with encapsulation keys of 800, 1,184 and 1,568 bytes ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)). If the budget for the client key share is 1,300 bytes, ML-KEM-768 is the largest that fits. Lagrange multipliers formalize such trade-offs for continuous variables; in discrete parameter sets you simply enumerate.

The byte budget comes from real limits: some networks fragment or drop handshake messages above certain sizes, and middleboxes may reject unusual records. Choosing ML-KEM-768 within a 1,300-byte budget gives category 3 security with room left. If the budget were 1,000 bytes, only ML-KEM-512 would fit, and the memo would have to discuss whether category 1 is acceptable.

### 6.4 Worked example

BPA's customs exchange sends 2 TB/year today, growing 20% per year (*r* ≈ 0.182). Exposed volume if migration completes after 3 years: (2/0.182)(*e*^0.547 − 1) ≈ 8.0 TB; after 5 years: ≈ 16.3 TB. Two extra years roughly double the exposed archive.

With r equal to 0.182, the exponential terms are about 1.73 after three years and 2.49 after five. Multiplying the excess over one by about eleven, the factor two divided by r, gives the two figures. The doubling shows why the programme plan front-loads the customs exchange: it has the fastest-growing volume and the longest confidentiality requirement.

### 6.5 Practical activity

Compute the exposed volume for migration after 1–8 years and plot (or tabulate) it. Identify the year where exposure exceeds 10 TB.

Use the formula from the worked example rather than adding up yearly volumes: summing 2, 2.4, 2.88 and so on treats each year's traffic as arriving on the first day and gives slightly lower totals, about 7.3 TB after three years instead of 8.0. Both methods agree on which year first crosses 10 TB, but only the integral matches the figures in the worked example and in the exercise set. Tabulating each year shows the gaps between consecutive years growing, which is the non-linear effect that makes late delays expensive. Students should state their growth assumption beside the table and rerun it at 10% and 30%.

### 6.6 Common errors and limits

- Treating growth assumptions as forecasts.
- Linear thinking about delay under exponential growth.
- Ignoring that exposure also depends on how long data stays sensitive (Chapter 20).

Growth rates are assumptions; a 20% rate may fall if a service is retired or rise if new partners join. Linear thinking underestimates the cost of delay because each later year adds more volume than the one before. Exposure also depends on lifetime: traffic that loses value after a year matters less than customs records that must stay confidential for twenty-five years.

### Exercises

- **EX011 — Exposure integral.** Compute BPA's exposed volume for *T* = 4 years. Rubric: 3 = correct (≈ 11.8 TB) with working.
- **EX012 — Budgeted choice.** With a 900-byte client-share budget, which ML-KEM set fits, and what should the engineer do if category 3 is required? Rubric: 3 = ML-KEM-512 fits; proposes changing the budget or transport rather than downgrading silently.

### Synthesis

Calculus turns migration timing into exposure: under growth, delay costs more than linearly; parameter choice is constrained optimization over published parameter sets.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) reason about rare events such as decryption failures; (2) estimate rates with confidence intervals; (3) distinguish statistical from cryptographic security levels; and (4) design a measurement with enough samples. It builds on Chapters 1 and 6 and supports measurement (Chapter 29) and validation (Chapter 38).

### 7.1 Rare events

Lattice KEMs have a tiny probability that decapsulation produces the wrong key. FIPS 203's parameter sets keep it extremely small — around 2^-139 for ML-KEM-512 and smaller for the larger sets — far below any rate an engineer will observe. The expected number of failures in *N* operations is *N*·*p*. Lab P shows why a probability like 2^-20, fine for many engineering purposes, would be unacceptable for a KEM used billions of times, while 2^-139 is negligible at any scale.

The decision rule is simple: multiply by the largest number of operations the system will ever perform and check that the product stays far below one.

### 7.2 Practical activity — Lab P

```python
# Lab P (ch 7): how small must a failure probability be? Binomial reasoning for rare events.
import math
for p_exp in (-20, -40, -139):
    p = 10.0 ** (p_exp * math.log10(2))       # p = 2^p_exp
    for n_ops in (1e9, 1e15):
        exp_fail = n_ops * p
        print(f"p = 2^{p_exp:5d}, {n_ops:.0e} operations -> expected failures {exp_fail:.3e}")
```

Expected output:

```text
p = 2^  -20, 1e+09 operations -> expected failures 9.537e+02
p = 2^  -20, 1e+15 operations -> expected failures 9.537e+08
p = 2^  -40, 1e+09 operations -> expected failures 9.095e-04
p = 2^  -40, 1e+15 operations -> expected failures 9.095e+02
p = 2^ -139, 1e+09 operations -> expected failures 1.435e-33
p = 2^ -139, 1e+15 operations -> expected failures 1.435e-27
```

Read the six lines in pairs. At 2^-20, a billion operations already produce nearly a thousand expected failures, so such a scheme would fail visibly every day at BPA's scale. At 2^-40, a billion operations look safe, but a quadrillion, roughly the global volume of a widely deployed protocol over some years, gives about 900. At 2^-139 even the larger count leaves an expected 1.4 × 10^-27, which is why decryption failure is not a design concern for ML-KEM at all. Extend the loop with 1e18 operations and confirm the conclusion does not change.

### 7.3 Confidence intervals

When measuring handshake failure rates after enabling a hybrid group, report an interval, not just a point. For small proportions use the Wilson interval (Chapter 37's canary lab uses it). The *rule of three* gives a quick bound: if zero failures occur in *n* trials, the 95% upper bound on the rate is about 3/*n*.

The rule follows from requiring that zero failures in n trials has at most a 5% chance: (1 − p)^n = 0.05 gives p ≈ 3/n. It holds only when trials are independent; failures caused by one broken proxy cluster at one site, so a canary spread across several sites gives a more honest bound than the same count from one.

### 7.4 Statistical versus cryptographic security

A statistical test that finds no failures in a million runs says only that the rate is probably below 3 × 10^-6. Cryptographic security levels such as 2^-128 cannot be established by testing; they come from analysis. Engineers test to find bugs, not to prove security.

To show a rate below 2^-128 by testing, one would need around 10^39 trials, far beyond any computer. Tests are still worth running, because an implementation bug usually produces failures at a rate of one in a few hundred or thousand, which a modest test campaign catches quickly. A clean test run therefore rules out gross bugs while leaving the security claim to the published analysis.

### 7.5 Worked example

BPA's pilot sees 0 handshake failures in 12,000 hybrid connections at one site. The rule of three bounds the failure rate below 2.5 × 10^-4 (95%). Is that good enough to roll out to 2 million daily connections? At the bound, up to 500 failures per day could still occur — so the gate needs a larger canary before full rollout.

To bring the bound down to about one failure per day at 2 million connections, the rate must be shown below 5 × 10^-7, which by the rule of three needs about 6 million clean connections. BPA can reach that by widening the canary to several sites for a few days, which also tests different middleboxes.

### 7.6 Common errors and limits

- "No failures observed" interpreted as "rate is zero".
- Confusing a decryption-failure probability with a security level.
- Ignoring that operations multiply: rare per event is not rare per year.

The first error leads teams to declare success after a small pilot, as in the worked example where zero failures in 12,000 still allowed 500 a day. The second confuses two numbers: ML-KEM's 2^-139 failure probability is a reliability figure, while category 3 describes the work an attacker needs. The third is fixed by multiplying per-event rates by annual volume before judging them.

### Exercises

- **EX013 — Rule of three.** How many failure-free trials are needed to bound a rate below 10^-5? Rubric: 3 = 300,000 with reasoning.
- **EX014 — Scale.** If a component fails with probability 2^-30 per operation and BPA runs 10^10 operations a year, how many failures are expected? Rubric: 3 = ≈ 9.3 and interpretation.

### Synthesis

Rare events become common at scale; testing bounds rates but cannot establish cryptographic security; report intervals, and size samples to the decision being made.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) relate algorithm performance to processor features such as vector units and caches; (2) explain timing and power side channels; (3) assess memory and code size on constrained devices; and (4) understand hardware security modules (HSMs) and their migration constraints. It prepares implementation (Chapters 28 and 31) and performance (Chapter 36).

### 8.1 Performance features

Lattice schemes spend most of their time in polynomial multiplication via the number-theoretic transform and in hashing with SHAKE. Vector instructions (AVX2 on x86, NEON on ARM) parallelize coefficient operations, making ML-KEM very fast on servers. Constrained microcontrollers without vector units are slower but often still acceptable; memory, not speed, is usually the limit there.

For BPA this means the TLS servers will spend more time sending bytes than computing; benchmark results that show ML-KEM key generation faster than X25519 on a server do not carry over to a crane controller.

### 8.2 Side channels

Execution time, cache access patterns and power draw can reveal secrets if they depend on secret values. The "KyberSlash" findings showed that a division by a constant whose dividend depended on secret data leaked timing in several Kyber implementations ([Bernstein et al. 2024](https://eprint.iacr.org/2024/1049)). Constant-time coding — no secret-dependent branches, memory indices or variable-time instructions — is a requirement, not an optimization.

The fix in that case was to replace the division with a multiplication and shift that take the same time for every input. Reviews look for the same pattern elsewhere: any branch, table lookup or division whose input depends on a key or a decrypted value. Tools that run code with secret-marked inputs and flag such dependencies help, but they need to be run on the compiled binary, because compilers can reintroduce branches that the source did not have.

### 8.3 Memory and code size

ML-DSA signing needs several kilobytes of working memory; SLH-DSA signatures are large but keys are tiny; stateful hash-based schemes need non-volatile state that must never roll back. On a gate scanner with 64 KB of RAM, the choice of signature verification algorithm is an architecture decision.

An ML-DSA-44 verifier needs the 1,312-byte public key, the 2,420-byte signature and a working area for the matrix expansion, which some implementations keep small by generating rows on demand. A verifier that fits by recomputing data trades speed for memory, which a scanner verifying one update per month can easily afford. The architecture review records which trade-off was chosen and why.

### 8.4 HSMs and secure elements

Private keys at BPA's certificate authority live in an HSM. Migration needs HSM firmware that supports ML-DSA and possibly LMS/XMSS with state protection, validated under the relevant certification program. HSM upgrade cycles are often years long — a classic constraint on migration schedules.

BPA's plan therefore asks its HSM vendor three questions now: which post-quantum algorithms the current firmware supports, when certified firmware will be available, and whether existing hardware can be upgraded or must be replaced. The answers set the earliest date for issuing ML-DSA certificates, which in turn constrains every later migration step for authentication.

### 8.5 Worked example

BPA's crane controllers verify firmware signatures in a bootloader with 32 KB of flash available. ML-DSA-44 verification code and a 1,312-byte public key may fit; an LMS verifier is smaller and needs only hashing, and since only verification happens on the device, LMS's state problem stays at the signing server. The architecture review records both options and their memory budgets.

The decision also depends on how often firmware is signed. LMS keys can sign only a fixed number of messages, for example 2^10 or 2^15, and losing the signer's state can cause key reuse. With a few releases a year, a key with 2^15 signatures will last indefinitely, so the risk sits in the signing server's backup procedure, not in capacity.

### 8.6 Common errors and limits

- Benchmarking only on servers.
- Assuming a correct implementation is constant-time.
- Forgetting HSM procurement lead times.

Server benchmarks hide the memory limits that decide what fits on a gate scanner or crane controller, so each device class needs its own measurement. A correct implementation can still leak timing, as the KyberSlash case showed, which is why constant-time behaviour is tested separately from known answers. HSM upgrades can take years, so the request goes out before the software work starts, as BPA did with its certificate authority.

### Exercises

- **EX015 — Side-channel review.** Identify the timing risk in `if secret_coeff > q//2: x = slow_path()` and propose a fix. Rubric: 3 = identifies branch and gives branch-free alternative.
- **EX016 — Device fit.** Compare ML-DSA-44 and LMS verification for a 32 KB bootloader. Rubric: 3 = memory, state location and standards (FIPS 204, SP 800-208) considered.

### Synthesis

Architecture determines speed, memory fit and leakage: lattice schemes are fast with vector units, constant-time code is mandatory, constrained devices shape algorithm choice and HSM cycles shape schedules.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure code so that algorithms are replaceable; (2) parse and validate untrusted inputs such as certificates and key shares; (3) write property-based and known-answer tests; and (4) manage dependencies on cryptographic libraries. It builds on Chapter 4 and prepares agility (Chapter 39).

### 9.1 Interfaces over implementations

Write code against interfaces — `kem.encapsulate(public_key)`, `signer.sign(message)` — not against algorithm-specific functions. An algorithm identifier, chosen by policy, selects the implementation. This is the programming basis of crypto-agility ([CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1)): migration becomes a configuration change plus testing, not a rewrite.

The policy file names an algorithm per use, such as ML-DSA-65 for e-document signatures, and the code never mentions it. When BPA later moves from a hybrid to a pure post-quantum setting, the change is one line in policy plus the test run. Code review checks that no module bypasses the interface by importing an algorithm library directly.

### 9.2 Input validation

Post-quantum keys and ciphertexts have fixed lengths per parameter set. FIPS 203 requires checks on encapsulation keys (a modulus check that encoded coefficients are below *q*) and decapsulation keys before use. Code should reject wrong lengths before calling a library and never "pad" or "truncate" to make inputs fit.

An ML-KEM-768 encapsulation key must be exactly 1,184 bytes and a ciphertext exactly 1,088. Checking these lengths first gives a clear error message and avoids passing malformed data into code that might behave unpredictably. The modulus check catches keys whose coefficients were encoded with values of 3329 or higher, which a malicious peer might send to probe for implementation weaknesses.

### 9.3 Testing beyond examples

Known-answer tests confirm exact outputs. Property-based tests check invariants over many random inputs: decapsulate(encapsulate(pk)) yields the same key; a signature verifies for the signed message and fails for any one-bit change. Negative tests matter as much as positive ones.

A property test for BPA's signer runs a thousand random messages, signs each, verifies each, then flips one random bit in the message and in the signature and expects both checks to fail. A test that only checks successful verification would pass even if `verify` always returned true, which is precisely the bug negative tests exist to catch.

### 9.4 Dependencies

Pin versions of cryptographic libraries, track their advisories and record which algorithms and parameter sets each exposes. Draft-era names (e.g. "Kyber768") and final names (ML-KEM-768) are not interchangeable: the final standard changed details, so draft implementations do not interoperate with FIPS 203.

BPA's dependency file records the library name, the exact version, and the algorithms that version provides under final names. When a library release renames or removes a draft algorithm, the build fails at upgrade time rather than at a partner's handshake. Advisory tracking matters because post-quantum libraries are newer and have had more security fixes per year than mature RSA code.

### 9.5 Worked example

BPA's e-document service calls `rsa_sign()` in 41 places. Refactoring introduces `Signer` with implementations `RSA-PSS-3072` and `ML-DSA-65`, selected by a policy file. A test suite runs every call path with both. The diff is large once; the next migration will be small.

The 41 call sites are first found by searching for `rsa_sign`, then each is checked for assumptions such as a fixed 384-byte signature length in a database column. ML-DSA-65 signatures are 3,309 bytes, so the schema change is part of the same work item. The policy file starts with RSA-PSS-3072 so nothing changes for users until the switch.

### 9.6 Common errors and limits

- Hard-coding algorithm names and key lengths.
- Treating draft and final algorithm versions as the same.
- Testing only success paths.

Hard-coded names turn each future migration into a code change at every call site, which is exactly what the `Signer` refactoring removed. Draft and final versions differ in details, so a library still offering Kyber768 will not interoperate with ML-KEM-768. Testing only success paths leaves validation and error handling unchecked, and attackers target precisely those paths with malformed keys and ciphertexts.

### Engineering note

Interfaces also need versioned algorithm identifiers that travel with data. A signature stored today must carry an identifier naming its algorithm and parameter set, so that a verifier in ten years selects the right implementation and can refuse retired ones. Without identifiers, systems guess from lengths, which breaks as soon as two algorithms share a size. Treat the identifier as part of the signed or authenticated content wherever the format allows, so an attacker cannot relabel a weak signature as a strong one. This small design habit is what later makes policy-driven migration in Chapter 39 safe rather than merely convenient.

### Exercises

- **EX017 — Interface design.** Write a `KEM` interface (method names and types) suitable for ML-KEM and a future HQC. Rubric: 3 = no algorithm-specific assumptions such as sizes.
- **EX018 — Length checks.** Write a validator that rejects an ML-KEM-768 encapsulation key of the wrong length (correct: 1,184 bytes). Rubric: 3 = rejects, never pads.

### Synthesis

Replaceable algorithms start in code: interfaces, policy-chosen identifiers, strict validation, property and negative tests, and dependency tracking that knows draft from final.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply professional ethics to cryptographic migration decisions; (2) identify who bears the risk of "harvest-now, decrypt-later"; (3) handle vulnerability findings responsibly; and (4) avoid overstating quantum risk to sell products. It closes the first foundations block and informs every design decision later.

### 10.1 Duties

Engineering codes of ethics place public welfare first. In PQC work this means protecting people whose data will remain sensitive for decades — medical, legal, customs and personal records — even though harm, if it comes, comes years after the engineer's decision. It also means honesty: neither minimizing the risk ("quantum is science fiction") nor inflating it to sell ("RSA will be broken next year").

For a BPA engineer, honesty means stating the range of expert estimates and the 25-year record lifetime side by side, without picking the date that suits the budget.

### 10.2 Who bears the risk

Data subjects bear harvest-now-decrypt-later risk, but they rarely decide migration budgets. An ethical engineer makes this asymmetry visible in decision memos: "If we postpone, customs declarants' commercial data recorded from now until migration may become readable by a future adversary."

The memo then names who decides and who would be harmed, so the board sees that postponing transfers risk to people outside the room. Quantifying exposure, as in the 8.0 versus 16.3 TB comparison, makes the transfer concrete. It also gives declarants' representatives something to ask about when BPA reports on data protection.

### 10.3 Safety interactions

Cryptographic changes can break availability: an oversized handshake that a middlebox drops, a firmware signature that a bootloader cannot verify, a certificate that a medical device rejects. In safety-related systems — cranes, port traffic control — a failed update can stop operations or create hazards. Change management with rollback plans, testing in isolated environments and staged rollouts is an ethical duty, not bureaucracy.

In practice, BPA's crane firmware change is tested on a spare controller, rolled out to one crane, and held for a week before the rest.

### 10.4 Responsible disclosure and testing limits

If testing reveals a vulnerability in a product, report it to the vendor and give time to fix before publishing. Never test systems you are not authorized to test, and never run downgrade experiments on production traffic.

For BPA's teams, authorization means a written scope that names systems, dates and allowed techniques. A downgrade test that strips the hybrid group from a ClientHello belongs in a lab copy of the portal, not on the live service where it could break partners' sessions. Findings in vendor products go to the vendor first, with a disclosure date agreed in advance.

### 10.5 Worked example

A vendor offers BPA a "quantum-proof" appliance using an unpublished algorithm. Ethical evaluation: an unvetted algorithm offers no assurance (Rainbow and SIKE were broken despite years of public scrutiny — [Beullens 2022](https://eprint.iacr.org/2022/214), [Castryck and Decru 2022](https://eprint.iacr.org/2022/975)); the marketing overstates; the engineer's duty is to recommend standardized algorithms and to say why, even if the vendor is a friend of management.

The written evaluation goes to the board, not only to the vendor, so the reasons survive any later pressure to reverse it.

### 10.6 Common errors and limits

- Deferring migration because the harm is far away.
- Accepting marketing terms like "quantum-proof".
- Rolling out cryptographic changes to safety systems without rollback.

Deferral feels safe because nobody is harmed this year, but recorded customs traffic accumulates exposure every month the decision waits. "Quantum-proof" claims should prompt a request for the algorithm, its standard and its review history. Safety systems such as crane controllers need tested rollback before any firmware signature change, since a device that rejects its own update can halt operations.

### Exercises

- **EX019 — Risk bearers.** For BPA, list three groups who bear quantum risk and how each is represented in decisions. Rubric: 3 = groups distinct, representation gap identified.
- **EX020 — Vendor letter.** Write a polite letter declining an unvetted "quantum-proof" algorithm. Rubric: 3 = cites standards and the breaks, offers a path forward.

### Synthesis

Ethical PQC engineering protects long-lived data on behalf of people who cannot see the risk, communicates honestly, treats availability and safety as part of security and rejects unvetted cryptography.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) trace a TLS 1.3 handshake and identify where key exchange and authentication happen; (2) explain how packet size, MTU and fragmentation interact with larger post-quantum messages; (3) describe IKEv2, SSH and DNSSEC from a migration viewpoint; and (4) recognize middlebox ossification. It prepares integration (Chapter 34) and performance (Chapter 36).

### 11.1 TLS 1.3

In TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html)) the client sends a ClientHello with key shares for one or more groups; the server replies with its share, and both derive keys from the shared secret. The server then sends its certificate chain and a CertificateVerify signature, encrypted. Key exchange protects confidentiality against recording; certificates and signatures provide authentication at the time of connection. Hybrid groups such as X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) change only the key-share part: the client share grows from 32 to 1,216 bytes, the server's to 1,120 bytes.

### 11.2 Size and the network

An Ethernet path typically carries 1,500-byte IP packets, about 1,460 bytes of TCP payload. A ClientHello with a hybrid share often exceeds that and needs two TCP segments. TCP handles this transparently, but some middleboxes and servers inspect only the first packet. Google reported such incompatibilities when Chrome began offering hybrid Kyber ([Chromium Blog 2023](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)). Over UDP (QUIC, DTLS, IKEv2) larger messages raise fragmentation and amplification-limit issues that protocol designers handle explicitly.

Testing therefore covers the whole path, including proxies and load balancers.

### 11.3 Other protocols

IKEv2 VPNs add post-quantum key exchange through additional exchanges ([RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html) defines multiple key exchanges in IKEv2). SSH implementations have deployed hybrid key exchange methods combining a lattice KEM with X25519. DNSSEC is mostly a signature problem: post-quantum signatures are much larger than today's ECDSA signatures, which strains UDP responses.

Each protocol needs its own plan. BPA's site-to-site VPN can add an ML-KEM exchange through RFC 9370 once both gateways support it; SSH administration can switch to a hybrid method with a configuration change on servers and clients; DNSSEC must wait for standards that fit large signatures into DNS responses, so it stays in the inventory as a tracked dependency.

### 11.4 Ossification

When middleboxes assume protocol fields never change, new values break connections. TLS 1.3 introduced GREASE ([RFC 8701](https://www.rfc-editor.org/rfc/rfc8701.html)) — random reserved values — to keep implementations tolerant. Post-quantum migration is a test of ossification: the protocol allows it, but deployed equipment may not.

BPA's test plan sends hybrid ClientHellos through every inspection device on the path to partner portals before enabling them. A device that resets the connection is logged with its firmware version, and the vendor is asked for a fix. This turns ossification from a surprise outage into a list of known items with owners and dates.

### 11.5 Worked example

BPA's terminal staff report that the shipping-line portal fails through the old inspection proxy after enabling a hybrid group. Packet traces show the proxy resetting connections whose ClientHello spans two segments. Options: update proxy firmware, bypass inspection for that destination, or temporarily disable the hybrid group only on that path while the vendor fixes it — keeping it everywhere else.

The targeted exception is the right choice because the proxy fault affects only one path, while the harvest risk applies to all traffic. The exception is recorded with an expiry date and an owner, so it cannot become permanent. Once the vendor's firmware is installed, the test from the lab is rerun before the hybrid group is enabled again on that path.

### 11.6 Common errors and limits

- Assuming hybrid key exchange also migrates certificates.
- Forgetting UDP protocols' size limits.
- Rolling back PQC globally for a local middlebox fault.

Hybrid key exchange protects recorded traffic but leaves authentication on RSA or ECDSA certificates, which need their own migration. UDP protocols such as QUIC and IKEv2 must handle size explicitly because they lack TCP's segmentation. A global rollback for one proxy throws away protection for every other path, as the shipping-line portal case showed; a time-limited exception for that one path keeps everything else protected.

### Exercises

- **EX021 — Segment count.** A ClientHello is 540 bytes without key shares. How many 1,460-byte segments with an X25519-only share (32 B) and with X25519MLKEM768 (1,216 B), counting ~4 B overhead per share? Rubric: 3 = 1 and 2 segments with arithmetic.
- **EX022 — Protocol map.** For TLS, IKEv2, SSH and DNSSEC, state whether migration is mainly key exchange, signatures or both. Rubric: 3 = correct with one-line reasons.

### Synthesis

Hybrid key exchange changes message sizes, which networks and middleboxes may mishandle; each protocol has its own migration shape, and ossification, not cryptography, is often the obstacle.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) locate cryptographic libraries and configuration in an operating system; (2) explain system-wide crypto policies; (3) understand secure boot and update signing; and (4) manage entropy and key storage. It builds on Chapters 8–9 and prepares inventory (Chapter 22) and maintainability (Chapter 39).

### 12.1 Where cryptography lives

On a Linux server, TLS usually comes from a shared library (OpenSSL, GnuTLS, NSS, BoringSSL in some applications), SSH from OpenSSH, VPNs from kernel IPsec plus a user-space IKE daemon. Applications may also bundle their own libraries — Java, Go and Rust programs often do. An inventory that checks only the system library misses statically linked or bundled cryptography.

Finding bundled code requires checking binaries and application packages, not just the package manager. For a Go binary, the build information lists the cryptographic modules compiled in; for Java, the configured security providers show which library handles TLS. These checks belong in the inventory script so every host is assessed the same way.

### 12.2 System-wide policies

Some distributions provide system-wide cryptographic policies that set default algorithms for all libraries that honour them. Policies are a powerful agility lever: changing one profile can enable hybrid groups or disable weak algorithms across many services. Their limit is coverage — applications with bundled libraries ignore them.

BPA uses the policy to enable the hybrid group on all services that use the system library in a single change, then checks each service's handshake to confirm it took effect. Services that do not show the hybrid group after the change are exactly those with bundled libraries, so the policy rollout doubles as a test of inventory coverage.

### 12.3 Secure boot and updates

Firmware verifies the bootloader's signature, which verifies the kernel's, and so on. These signatures must remain verifiable for the device's lifetime, which may exceed a decade. That makes boot chains early candidates for hash-based signatures (LMS, XMSS per [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208)), which CNSA 2.0 also prioritizes for software and firmware signing.

A device shipped in 2026 with a fifteen-year life will still verify updates in 2041, so the boot key chosen now must remain secure for that whole period. Changing the root of trust later may need physical access or may be impossible, which is why boot chains get first priority rather than last.

### 12.4 Entropy and key storage

Keys need good randomness from the OS (`getrandom`), especially at early boot and in virtual machines. Private keys belong in protected storage — HSMs, TPMs or OS keystores — never in world-readable files.

Virtual machines cloned from one image can start with identical random state, so keys generated at first boot may repeat across hosts. Waiting for `getrandom` to report that the pool is ready, and generating keys after boot completes, avoids that. On BPA's terminal servers, TLS private keys are stored in the TPM-backed keystore and audited monthly for file-permission drift.

### 12.5 Worked example

BPA's inventory of a terminal server finds OpenSSL 3.x as the system library, a Java application with its own provider, a Go binary statically linked, and an IPsec daemon. Enabling hybrid TLS through the system policy affects only the first; the other two need application changes. The migration plan records one work item per cryptographic provider, not per server.

Counting by provider gives four work items for this server, with different owners: the platform team for OpenSSL and IPsec, the application team for Java, and the developers of the Go service, who must rebuild with a newer toolchain. A plan counted per server would have marked this host done after the policy change while two of its four providers were untouched.

### 12.6 Common errors and limits

- Assuming one policy change migrates the whole host.
- Ignoring boot-chain signatures because they are "not network".
- Storing keys in configuration directories.

The worked example showed a policy change reaching only one of four providers on a single host. Boot-chain signatures matter because they must stay valid for the device's life and are hard to replace, so they come first in signing migrations. Keys kept in configuration directories are copied into backups and images, where they may outlive the systems they were meant to protect.

### Exercises

- **EX023 — Provider inventory.** List four places cryptography may live on a server and how you would detect each. Rubric: 3 = includes bundled/static libraries.
- **EX024 — Boot chain.** Explain why firmware signing is an early PQC priority. Rubric: 3 = device lifetime and verification-only constraints.

### Synthesis

Cryptography lives in many providers on one host; system policies help but do not cover bundled code; long-lived boot chains need early migration; keys need protected storage and good entropy.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) classify data by confidentiality lifetime; (2) distinguish encryption at rest, in transit and in backups; (3) understand envelope encryption and key wrapping; and (4) identify where quantum-vulnerable algorithms protect stored data. It prepares system and data models (Chapter 22).

### 13.1 Confidentiality lifetime

The key input to quantum risk is how long data must stay secret. BPA's container manifests matter for weeks; customs declarations for 25 years; employee records for decades. Classify data by lifetime first; the migration order follows.

### 13.2 At rest, in transit, in backups

Bulk data at rest is usually encrypted with symmetric algorithms (AES-GCM), which are not seriously threatened by quantum computers at 256-bit keys. The danger is in **how symmetric keys are protected**: if a data key is wrapped with RSA or transmitted over an ECDH-protected channel that an adversary recorded, the data inherits that vulnerability. Backups and archives copied to third parties extend exposure.

### 13.3 Envelope encryption

Cloud key-management services encrypt data with a data key and wrap the data key with a master key. If the master key is symmetric and stays inside the service, quantum risk is low; if keys are exchanged between parties using RSA-OAEP or ECDH (as in many document-encryption formats), the wrap is the weak point. Post-quantum KEMs can replace those wraps — the CMS standard now has a [KEM-based mechanism](https://www.rfc-editor.org/rfc/rfc9629.html) (RFC 9629).

### 13.4 Database and replication links

Database replication across sites often runs over TLS. Recorded replication streams of a 25-year customs database are a prime harvest target, making replication links early hybrid-TLS candidates.

### 13.5 Worked example

BPA's customs archive: AES-256-GCM at rest (acceptable), data keys wrapped by an on-premises KMS with an AES master key (acceptable), nightly replication to a disaster-recovery site over TLS 1.2 with ECDHE (vulnerable to harvest), and exports to the national customs agency as RSA-encrypted files (vulnerable). Priorities: replication link and export format.

### 13.6 Common errors and limits

- Replacing AES "because quantum" while leaving RSA key wraps.
- Ignoring backup and export paths.
- Not classifying data lifetime before prioritizing.

### Exercises

- **EX025 — Classify.** Classify six BPA data sets by confidentiality lifetime and justify. Rubric: 3 = lifetimes plausible and linked to priority.
- **EX026 — Find the weak wrap.** For a document-encryption flow using AES-256 and RSA-OAEP, identify the quantum-vulnerable step and a standards-based replacement. Rubric: 3 = RSA wrap; KEM (e.g. ML-KEM via CMS KEMRecipientInfo).

### Synthesis

Quantum risk to stored data comes through key exchange and key wrapping, not AES; classify data by lifetime, then fix replication links, exports and wraps.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) manage requirements, design, implementation and testing in a migration project; (2) use version control and code review for cryptographic changes; (3) build a software bill of materials (SBOM) and a cryptographic bill of materials (CBOM); and (4) plan staged releases. It builds on Chapters 4 and 9 and prepares implementation (Chapter 28).

### 14.1 Lifecycle

A migration is a software project: requirements (which functions must become quantum-resistant, by when), design (hybrid or pure PQC, which libraries), implementation, testing, staged release and maintenance. Cryptographic changes are high-impact and low-visibility: if wrong, they fail silently or catastrophically.

### 14.2 Review

Every cryptographic change gets review by someone with cryptographic knowledge, plus tests for interoperability. Checklists ask: are algorithm identifiers from policy? Are lengths validated? Are comparisons constant-time? Is the library version pinned and supported?

### 14.3 SBOM and CBOM

An SBOM lists components and versions. A CBOM extends this to cryptographic assets: algorithms, parameter sets, key lengths, protocols, certificates and where keys live. Formats such as CycloneDX support CBOM fields. A CBOM is the basis for answering "where do we use RSA?" in minutes rather than months.

### 14.4 Staged releases

Use feature flags for algorithm choices, canary deployments with measured failure rates (Chapter 37) and rollback plans. Keep both old and new algorithms available during transition.

### 14.5 Worked example

BPA's portal team adds hybrid TLS behind a flag, runs interoperability tests against the top 50 partner clients, deploys to 1% of traffic, monitors failures and promotes in steps. The CBOM is updated automatically from build metadata so the inventory stays current.

### 14.6 Common errors and limits

- Cryptographic changes merged without specialist review.
- CBOMs built once by hand and never updated.
- Big-bang releases without flags.

### Engineering note

Treat the CBOM as a living artefact owned by a named team, generated from build pipelines, configuration management and telemetry rather than spreadsheets. Each release should diff its CBOM against the previous one: a new RSA dependency introduced by a library upgrade is a regression to catch in review, exactly like a failing test. Teams that wire this diff into continuous integration discover quantum-vulnerable additions within days instead of during the next annual audit, and they also gain an accurate list for vendor questionnaires and regulators.

### Exercises

- **EX027 — Review checklist.** Write a ten-item checklist for reviewing a PQC change. Rubric: 3 = covers identifiers, validation, constant time, versions, tests, rollback.
- **EX028 — CBOM fields.** List the minimum fields of a CBOM entry for a TLS endpoint. Rubric: 3 = algorithm, parameter set, protocol, key location, owner, certificate details.

### Synthesis

Treat migration as software engineering: reviewed changes, flags, canaries, rollback and an automatically maintained CBOM.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) apply confidentiality, integrity and availability to cryptographic migration; (2) explain security levels and NIST's five PQC categories; (3) distinguish attack models — passive recording, active man-in-the-middle and forgery; and (4) understand defence in depth. It prepares security architecture (Chapter 18).

### 15.1 CIA in migration

Confidentiality is threatened by recorded key exchanges; integrity and authenticity by future signature forgery on long-lived documents and firmware; availability by migration itself — oversized messages, incompatible clients, expired certificates. A plan that improves confidentiality but causes outages has failed on availability.

### 15.2 Security categories

NIST defined five post-quantum security categories by comparison with the cost of breaking symmetric primitives: category 1 is at least as hard as key search on AES-128, category 3 as AES-192, category 5 as AES-256; categories 2 and 4 compare with SHA-256 and SHA-384 collisions. ML-KEM-512/768/1024 target categories 1/3/5 ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)). CNSA 2.0 requires the category-5 sets (ML-KEM-1024, ML-DSA-87) for national-security systems.

### 15.3 Attack models

**Passive recording now, decryption later** threatens confidentiality of anything protected by vulnerable key exchange today. **Active attacks with a quantum computer** — impersonating a server by forging signatures — require the CRQC to exist at the time of attack, so signature migration is less urgent for short-lived authentication but urgent for long-lived roots of trust. **Forgery of archived signatures** threatens documents whose signatures must remain meaningful for years.

### 15.4 Defence in depth

Hybrid key exchange is defence in depth across assumptions: an attacker must break both the traditional and the post-quantum component ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)). Agility is defence in depth across time: if one algorithm weakens, replace it quickly.

### 15.5 Worked example

BPA's bills of lading are signed with ECDSA and must be verifiable for 12 years. A CRQC within 12 years would allow forging a bill dated in the past unless the document carries a post-quantum signature or a trusted timestamp chain that is itself migrated. Priority: high — integrity of legal documents over long periods.

### 15.6 Common errors and limits

- Treating PQC as confidentiality-only.
- Choosing category 5 everywhere without considering size and performance.
- Forgetting availability.

### Exercises

- **EX029 — Category choice.** Recommend a category for BPA's portal and for a national-security partner link; justify. Rubric: 3 = category 3 (or 1) for portal with reasoning; category 5 per CNSA 2.0 for the partner.
- **EX030 — Attack models.** For VPN traffic, firmware signatures and bills of lading, state which attack model dominates. Rubric: 3 = recording; forgery of long-lived roots; archived-signature forgery.

### Synthesis

Migration touches all of confidentiality, integrity and availability; categories tie PQC strength to symmetric benchmarks; urgency differs by attack model; hybrids and agility give depth.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) apply a systems lifecycle to a multi-year migration; (2) manage interfaces and dependencies across organizations; (3) use trade studies; and (4) plan verification and validation from the start. It builds on Chapter 14 and prepares requirements (Chapter 21).

### 16.1 Lifecycle view

A port-wide migration spans concept (why and what), requirements, architecture, implementation, integration, verification, validation, operation and retirement. Lifecycle standards such as ISO/IEC/IEEE 15288 describe these processes. Cryptographic migration differs from most system changes because it touches every interface at once and because partners outside the organization must change in step.

### 16.2 Interfaces and dependencies

BPA depends on shipping lines (VPN peers), the customs agency (export formats), vendors (appliances, HSMs, crane firmware) and browser makers (TLS clients). An interface control document lists, per interface, the current algorithms, the target, who must change and by when. Dependencies explain schedules better than effort estimates.

### 16.3 Trade studies

A trade study compares options against weighted criteria. For BPA's VPN: (a) hybrid IKEv2 with ML-KEM now, (b) wait for vendor native support, (c) add a pre-shared-key layer as an interim mitigation. Criteria: security gain, availability risk, cost, partner readiness, standards conformance. Weights come from requirements, not preference.

### 16.4 V&V planning

Verification asks "did we build it right?" (requirements met); validation asks "did we build the right thing?" (stakeholder needs met). Plan both before implementation: for example, verify that the VPN negotiates ML-KEM-768 or stronger in every tunnel, and validate that shipping-line operations continue without delay.

### 16.5 Worked example

The trade study scores option (a) highest on security and standards, (b) highest on availability, (c) as a cheap interim. Decision: (c) immediately for the two highest-value partners, (a) in a pilot with one partner, (b) for others when vendors deliver — documented with review dates.

### 16.6 Common errors and limits

- Planning migration as an internal project when partners must change too.
- Trade studies with weights chosen after scoring.
- V&V invented after deployment.

### Engineering note

Systems engineering also asks when to stop. A migration has an exit criterion per interface — for example, "classical-only negotiation below 0.5% of tunnels for 90 days and partner confirmation received" — after which the old path is removed rather than left as permanent fallback. Without exit criteria, transitional configurations become permanent, and the organization carries both the old risk and the new complexity. Record exit criteria in the interface control document so that progress reviews can close work packages objectively.

### Exercises

- **EX031 — Interface list.** Draft five rows of BPA's interface control document. Rubric: 3 = current, target, owner, date for each.
- **EX032 — Trade study.** Score the three VPN options with explicit weights. Rubric: 3 = weights justified before scoring; sensitivity noted.

### Synthesis

Migration is a systems problem dominated by interfaces and partners; trade studies with prior weights and early V&V planning keep decisions defensible.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) model a migration programme as a feedback loop; (2) choose leading and lagging indicators; (3) recognize instability from over-correction; and (4) apply control ideas to rollout gates. It prepares operations (Chapter 37) and optimization (Chapter 41).

### 17.1 Programmes as loops

A feedback loop measures output, compares it with a set point and adjusts input. In migration, the "output" is protected share of traffic and assets; the set point is the target trajectory; the input is engineering effort and rollout pace. Without measurement there is no control — only hope.

### 17.2 Indicators

**Lagging** indicators show results: percentage of key exchanges negotiated with hybrid groups, share of certificates with post-quantum signatures, unknown-asset share. **Leading** indicators predict results: vendors with committed PQC roadmaps, CBOM coverage, test-environment readiness. A dashboard needs both.

### 17.3 Stability

Over-correction causes oscillation: enabling hybrid groups everywhere after a good week, rolling back everywhere after a bad day. Control theory suggests damping — smaller steps, delays for measurement and hysteresis (different thresholds for promoting and rolling back).

### 17.4 Rollout gates as controllers

A canary gate is a simple controller: increase exposure when the failure rate's upper confidence bound is below budget, hold otherwise, roll back only when a higher threshold is crossed. Chapter 37 implements one.

### 17.5 Worked example

BPA's dashboard shows hybrid negotiation at 62% of portal traffic (lagging) and CBOM coverage at 71% of assets (leading). Unknown assets are 18%. The control action: raise inventory effort on unknown assets rather than push portal traffic higher, because the larger risk sits where nothing is measured.

### 17.6 Common errors and limits

- Dashboards with only lagging indicators.
- Rolling back globally for local faults (over-correction).
- Measuring configured rather than negotiated algorithms.

### Engineering note

Measurement delay matters in this loop. Passive telemetry may lag configuration changes by a day; partner-side changes may lag by weeks. A controller that reacts faster than its sensors oscillates, so the rollout cadence must be slower than the slowest relevant measurement. In practice BPA sets weekly promotion decisions for internal services and monthly reviews for partner interfaces, and it records the measurement lag next to each indicator so that no one mistakes yesterday's picture for today's state.

### Exercises

- **EX033 — Indicators.** Propose three leading and three lagging indicators for BPA. Rubric: 3 = measurable, owner named.
- **EX034 — Hysteresis.** Design promote/hold/rollback thresholds for a hybrid-group rollout. Rubric: 3 = distinct thresholds with rationale.

### Synthesis

A migration is a controlled process: measure negotiated outcomes, combine leading and lagging indicators, damp corrections and use gates with hysteresis.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) identify trust boundaries and where cryptography enforces them; (2) design a cryptographic architecture with zones and services; (3) place key management centrally; and (4) document crypto-agility as an architectural property. It builds on Chapters 15–17 and prepares the PQC core.

### 18.1 Trust boundaries

Draw every boundary where data crosses between trust domains: internet to portal, BPA to shipping line, terminal network to crane network, BPA to customs agency. At each boundary, list the cryptographic functions: key establishment, authentication, integrity, confidentiality at rest. That list is the architecture's skeleton.

### 18.2 Cryptographic services

Centralize where possible: a TLS termination layer, a PKI with an HSM-backed CA, a key-management service, a signing service for firmware and documents. Centralization turns migration of one service into migration for many consumers. Decentralized cryptography — each application with its own library and keys — multiplies the work.

### 18.3 Crypto-agility as architecture

NIST's crypto-agility white paper ([CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1)) describes agility as the capability to replace algorithms in protocols, applications, software, hardware and infrastructure while preserving security and operations. Architecturally this means: algorithm choices in policy, not code; protocols that negotiate algorithms securely; certificate and key lifecycles short enough to rotate; and inventory that shows where everything is.

### 18.4 Hybrid placement

Decide where hybrids apply: key exchange at every external TLS and VPN boundary first; signatures for long-lived roots and firmware next; internal service-to-service traffic by data lifetime. Record the decision and its review date.

### 18.5 Worked example

BPA's target architecture: hybrid TLS at the edge proxy and partner VPNs; a new PQC-capable HSM for the CA; LMS-signed crane firmware via a central signing service with state management; ML-DSA for bills of lading with timestamping; policy-driven algorithm selection in internal services.

### 18.6 Common errors and limits

- Architecture diagrams with no cryptographic functions marked.
- Each team choosing algorithms independently.
- Agility claimed but key lifetimes of 20 years.

### Engineering note

Trust boundaries also exist in time. A document signed today crosses a boundary into the future when a court or partner verifies it years later, so the architecture should show long-term validation services — timestamping, archive re-signing, evidence records — as components with their own cryptography to migrate. Drawing them explicitly prevents the common oversight in which every online path is migrated while archived evidence stays protected by algorithms that a future adversary could forge.

### Exercises

- **EX035 — Boundary table.** Create a boundary table for four BPA boundaries with functions and current algorithms. Rubric: 3 = complete and accurate.
- **EX036 — Centralize.** Argue for or against centralizing TLS termination for migration purposes. Rubric: 3 = agility benefit and single-point-of-failure risk both weighed.

### Synthesis

Architecture maps trust boundaries to cryptographic functions, centralizes services to make migration tractable and encodes agility in policy, protocols, lifecycles and inventory.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) explain digital signatures, certificates and PKI hierarchies; (2) understand one-time and many-time hash-based signatures; (3) compare ML-DSA, SLH-DSA, LMS/XMSS and the forthcoming FN-DSA; and (4) plan PKI migration including roots and long-lived signatures. It closes the foundations stage.

### 19.1 Signatures and PKI

A signature binds a message to a key; a certificate binds a key to an identity, signed by a certificate authority (CA); a chain leads to a root trusted by relying parties. Roots often live 20+ years, so a root key that a future CRQC could forge undermines every certificate beneath it.

### 19.2 Hash-based signatures from first principles

A Lamport one-time signature publishes hashes of two random secrets per message-digest bit and reveals one secret per bit when signing. Security needs only a one-way hash. Using a key twice reveals both secrets at many positions, enabling forgery. Merkle trees combine many one-time keys under one public key; LMS and XMSS ([RFC 8554](https://www.rfc-editor.org/rfc/rfc8554.html), [RFC 8391](https://www.rfc-editor.org/rfc/rfc8391.html), [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208)) do this statefully; SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) avoids state by using a hypertree with few-time signatures at the leaves, at the cost of larger signatures.

### 19.3 Practical activity — Lab L

```python
# Lab L (ch 19): Lamport one-time signatures from SHA-256 - the idea under SLH-DSA, LMS and XMSS.
import hashlib, secrets
H = lambda b: hashlib.sha256(b).digest()
def keygen(bits=256):
    sk = [(secrets.token_bytes(32), secrets.token_bytes(32)) for _ in range(bits)]
    pk = [(H(a), H(b)) for a, b in sk]
    return sk, pk
def bits_of(msg):
    d = int.from_bytes(H(msg), "big"); return [(d >> (255 - i)) & 1 for i in range(256)]
def sign(sk, msg): return [sk[i][b] for i, b in enumerate(bits_of(msg))]
def verify(pk, msg, sig): return all(H(s) == pk[i][b] for i, (s, b) in enumerate(zip(sig, bits_of(msg))))
sk, pk = keygen()
s1 = sign(sk, b"firmware v1.0")
print("valid signature verifies:", verify(pk, b"firmware v1.0", s1))
print("tampered message rejected:", not verify(pk, b"firmware v1.1", s1))
s2 = sign(sk, b"firmware v1.1")          # KEY REUSE: never do this
revealed = sum(1 for i in range(256) if bits_of(b"firmware v1.0")[i] != bits_of(b"firmware v1.1")[i])
print(f"after one reuse, both secrets revealed at {revealed}/256 positions -> forgeries become feasible")
print("signature size:", 256 * 32, "bytes; public key:", 2 * 256 * 32, "bytes")
```

Expected output:

```text
valid signature verifies: True
tampered message rejected: True
after one reuse, both secrets revealed at 118/256 positions -> forgeries become feasible
signature size: 8192 bytes; public key: 16384 bytes
```

### 19.4 The standardized options

| Scheme | Basis | Public key / signature (bytes) | Notes |
|---|---|---|---|
| ML-DSA-44/65/87 ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) | Module lattices | 1,312/2,420 · 1,952/3,309 · 2,592/4,627 | General purpose |
| SLH-DSA (FIPS 205) | Hashes, stateless | 32–64 / 7,856–49,856 | Conservative, large |
| LMS, XMSS (SP 800-208) | Hashes, stateful | Small / ~1–3 kB typical | State must never repeat; firmware |
| FN-DSA (Falcon) | NTRU lattices | ~900 / ~666 at level 1 | Standard (FIPS 206) in development |

### 19.5 Worked example

BPA's PKI plan: a new ML-DSA-87 root (or a composite traditional+PQC root, depending on relying-party support) created now and distributed; intermediates migrated over the next certificate cycle; LMS for firmware signing with HSM-protected state; SLH-DSA considered for a rarely used offline root because of its conservative assumption.

### 19.6 Common errors and limits

- Reusing one-time or stateful keys (state rollback after a backup restore is a classic failure).
- Migrating leaf certificates while leaving a vulnerable long-lived root.
- Quoting FN-DSA as a final standard.

### Exercises

- **EX037 — Lamport reuse.** Explain from Lab L why signing two messages with one key enables forgery. Rubric: 3 = revealed-secret argument correct.
- **EX038 — Scheme selection.** Choose a signature scheme for (a) TLS server certificates, (b) crane firmware, (c) an offline root used twice a year. Rubric: 3 = ML-DSA; LMS/XMSS or ML-DSA with reasons; SLH-DSA or ML-DSA with reasons.

### Synthesis

Signatures and PKI carry long-lived trust; hash-based schemes are conservative and either stateful or large; ML-DSA is the general-purpose choice; roots must migrate first.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Quantum and post-quantum security: engineering context

### Learning outcomes

You will (1) explain the quantum threat to deployed cryptography precisely; (2) apply Mosca's inequality to prioritize systems; (3) summarize the standards and policy landscape with status; and (4) frame BPA's migration as an engineering programme. This chapter opens the PQC core and builds on all foundations.

### 20.1 What breaks and what does not

Shor's algorithm breaks RSA, finite-field Diffie–Hellman, DSA, ECDSA, EdDSA, ECDH and X25519 — every widely deployed public-key algorithm. Grover's algorithm weakens symmetric ciphers and hashes only modestly; AES-256 and SHA-384/SHA-512 remain conservative choices. So migration is about *public-key* cryptography: key establishment and digital signatures.

### 20.2 Prioritizing with Mosca

For each system, estimate *x* (how long its data or signatures must remain secure), *y* (how long migration will take) and treat *z* (time until a CRQC) as a range. If *x* + *y* > *z* for plausible *z*, the system is already late ([Mosca 2018](https://doi.org/10.1109/MSP.2018.3761723)). BPA's customs data (*x* = 25) is late under any plausible range; the container-tracking feed (*x* ≈ 0.1) can follow the normal technology cycle.

### 20.3 Standards and policy, with status

NIST published ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)), ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) and SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) in August 2024; stateful hash-based signatures are in [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208); KEM usage guidance is [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) (September 2025). HQC was selected in March 2025 as a backup KEM ([IR 8545](https://doi.org/10.6028/NIST.IR.8545)); FN-DSA is being standardized. The draft [NIST IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) proposes deprecating 112-bit quantum-vulnerable algorithms after 2030 and disallowing them after 2035. The IETF has standardized hybrid TLS groups ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) and hybrid terminology ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)). Statuses change — re-verify.

### 20.4 Migration as a programme

The NCCoE's [Migration to Post-Quantum Cryptography project](https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms) runs two workstreams with industry collaborators — cryptographic discovery (inventory tools that support risk-based prioritization) and interoperability testing of the standardized algorithms in common protocols. Engineering work packages for BPA: inventory (CBOM), requirements, architecture, vendor engagement, pilots, rollout, verification and agility.

### 20.5 Worked example

BPA's initial priority list: (1) customs replication and exports — confidentiality, *x* = 25; (2) partner VPNs — recorded traffic includes commercial terms, *x* = 10; (3) PKI root and firmware signing — long-lived trust; (4) public portal — hybrid TLS available cheaply; (5) internal short-lived telemetry — later.

### 20.6 Common errors and limits

- Migrating symmetric cryptography first.
- Treating policy dates as quantum forecasts.
- Using vendor names ("Kyber") for final standards ("ML-KEM").

### Exercises

- **EX039 — Mosca table.** Build a Mosca table (*x*, *y*, verdict across *z* = 10–30) for five BPA systems. Rubric: 3 = values justified, verdicts consistent.
- **EX040 — Status brief.** Write a 150-word status brief of PQC standards with citations. Rubric: 3 = correct statuses and dates.

### Synthesis

Quantum computers threaten public-key cryptography; Mosca's inequality orders the work; standards exist for KEMs and signatures with more coming; migration is a multi-year programme.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Quantum and post-quantum security: requirements

### Learning outcomes

You will (1) write verifiable PQC requirements; (2) derive requirements from data lifetimes, policy and partner constraints; (3) include availability and agility requirements; and (4) trace requirements to verification methods. It builds on Chapter 20 and prepares models and threat analysis.

### 21.1 Good requirements

A requirement is necessary, unambiguous, verifiable and traceable. "The system shall be quantum-safe" fails all four. Better: "REQ-KE-01: All TLS connections at the external edge shall negotiate X25519MLKEM768 or a stronger PQ/T hybrid group when the client offers one. Verification: passive telemetry shows ≥ 99% of offering clients negotiate it."

### 21.2 Sources

Derive requirements from: data confidentiality lifetimes (Chapter 13), signature validity periods (bills of lading: 12 years), policy (NIST transition plans, sector regulators, CNSA 2.0 for national-security partners), partner capabilities and operational constraints (handshake size budgets, device memory).

### 21.3 Requirement categories

- **Key establishment**: which protocols use hybrid or PQC KEMs, which parameter sets.
- **Signatures**: which artefacts need post-quantum signatures, by when.
- **Agility**: "REQ-AG-02: Replacing the KEM algorithm in edge TLS shall require only a policy change and shall be completable within 30 days including testing."
- **Inventory**: "REQ-INV-01: The CBOM shall cover ≥ 95% of assets, with unknown share reported monthly."
- **Availability**: "REQ-AV-01: Enabling hybrid groups shall not raise handshake failures above baseline + 0.04 percentage points (95% upper bound)."

### 21.4 Traceability

Each requirement links to a source and to a verification method (test, analysis, inspection, demonstration). A traceability matrix shows coverage and helps reviewers find orphaned requirements.

### 21.5 Worked example

BPA's customs export requirement: "REQ-EXP-03: Files exported to the customs agency shall be encrypted to the agency's ML-KEM-1024 key using CMS KEMRecipientInfo ([RFC 9629](https://www.rfc-editor.org/rfc/rfc9629.html)), with an RSA-OAEP recipient retained in parallel until the agency confirms support (target date recorded). Verification: inspection of exported file structure; interoperability test with agency test system."

### 21.6 Common errors and limits

- Requirements that name products instead of properties.
- No availability or agility requirements.
- Requirements without verification methods.

### Exercises

- **EX041 — Rewrite.** Rewrite "Use PQC for VPN" as a verifiable requirement. Rubric: 3 = protocol, parameter, condition and verification stated.
- **EX042 — Trace.** Build a five-row traceability matrix for BPA. Rubric: 3 = sources and verification methods for each.

### Synthesis

PQC requirements are specific, verifiable and traced to data lifetimes, policy and constraints, and they include agility, inventory and availability, not only algorithms.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Quantum and post-quantum security: system and data models

### Learning outcomes

You will (1) model systems as assets, flows and cryptographic functions; (2) build a data model for a CBOM; (3) link data flows to confidentiality lifetimes; and (4) use models to compute exposure. It builds on Chapters 13, 14 and 21.

### 22.1 Asset and flow models

Model each asset (service, device, data store) and each flow between assets. Annotate flows with protocol, key-establishment algorithm, authentication algorithm and data classes carried. Annotate stores with encryption, key-wrapping method and retention. The model becomes the backbone of inventory, threat analysis and planning.

### 22.2 CBOM data model

A minimal CBOM entity set: *Asset* (id, owner, type, location); *CryptoUse* (asset, function: key-exchange/signature/encryption/hash, algorithm, parameter set, protocol, library, source of evidence, last observed); *Key/Certificate* (algorithm, size, issuer, expiry, storage); *DataClass* (lifetime). The *source of evidence* field — code, configuration, passive observation, vendor declaration — matters because sources differ in reliability.

### 22.3 Exposure computation

Exposure of a flow = (data lifetime > time until assumed CRQC) × (vulnerable key exchange) × (recordable by adversary). A query over the model lists exposed flows; joining with traffic volume ranks them. Uncertain fields are *unknown*, never assumed safe.

### 22.4 Worked example

BPA's model has 412 assets and 1,930 flows. Querying for flows carrying lifetime ≥ 10-year data over ECDHE-only key exchange returns 37 flows, 29 of which pass through four gateways — making the gateways the highest-leverage migration targets.

### 22.5 Practical activity

Sketch the CBOM entities in a table or as Python dataclasses, then populate ten records from the BPA description and write a query for exposed flows. Chapter 29's Lab I extends this.

### 22.6 Common errors and limits

- Models that record algorithms but not evidence source.
- Treating unknown as safe.
- Models built once and never updated.

### Engineering note

Models must also record time. A flow observed once eighteen months ago may no longer exist, and a library upgraded last week may have changed defaults. Store first-seen and last-seen timestamps with every observation and age out stale records into an "unverified" state rather than deleting them silently. This keeps the exposure query honest: it distinguishes flows known to be vulnerable now from flows that were vulnerable when last seen and need re-observation before anyone spends migration budget on them.

### Exercises

- **EX043 — Entity design.** Define the CryptoUse entity with field types and allowed values. Rubric: 3 = includes evidence source and last-observed timestamp.
- **EX044 — Exposure query.** Write pseudocode for the exposed-flows query. Rubric: 3 = handles unknown values explicitly.

### Synthesis

Asset-flow models annotated with cryptographic functions and data lifetimes turn migration questions into queries; the CBOM model must record evidence sources and unknowns.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Quantum and post-quantum security: threat and failure analysis

### Learning outcomes

You will (1) model quantum-era threats with STRIDE-style analysis; (2) analyse failure modes introduced by migration itself; (3) include downgrade and implementation attacks; and (4) prioritize with risk scoring. It builds on Chapters 15 and 22.

### 23.1 Quantum-era threats

- **Harvest-now, decrypt-later**: recording traffic protected by vulnerable key exchange.
- **Future forgery**: forging signatures on long-lived artefacts once a CRQC exists.
- **Downgrade**: an active attacker strips post-quantum options so peers fall back to classical-only exchange. TLS 1.3 protects the negotiation transcript, so downgrade requires breaking authentication — but misconfigured fallback logic in applications can reintroduce it.
- **Implementation attacks**: side channels and fault injection against new code (Chapter 31).
- **Cryptanalytic surprise**: a weakness found in a new scheme, as happened to Rainbow and SIKE ([Beullens 2022](https://eprint.iacr.org/2022/214); [Castryck and Decru 2022](https://eprint.iacr.org/2022/975)).

### 23.2 Migration failure modes

Failure-mode and effects analysis (FMEA) applies: oversized handshakes dropped by middleboxes; clients that cannot parse new certificates; HSMs that cannot hold new keys; stateful signature keys reused after backup restore; interoperability failures between draft and final implementations; expired transition certificates. Each has a cause, effect, detection method and mitigation.

### 23.3 Risk scoring

Score likelihood and impact; for harvest threats, impact scales with data lifetime and volume. Avoid false precision: three or five levels with clear definitions are enough.

### 23.4 Worked example

FMEA for BPA's crane firmware signing with LMS: failure "state counter reset after HSM restore" → effect "one-time key reuse enabling forgery" → detection "monotonic counter audit against log" → mitigation "HSM with state reservation, restore procedures that forbid rollback, separate key per signing site". Severity high, likelihood medium → priority action.

### 23.5 Common errors and limits

- Analysing only cryptanalytic threats, not migration failures.
- Assuming hybrids remove the need to analyse downgrade.
- Numeric risk scores presented as measurements.

### Engineering note

Finally, rank threats by when they can be realized. Harvest-now-decrypt-later is happening today for any recorded traffic, even though decryption needs a future machine; active forgery requires the machine to exist at attack time. This temporal split explains why the same organization can rationally migrate key exchange this year while scheduling signature migration for later, and it gives decision-makers a clear reason for the order of work rather than an undifferentiated list of quantum risks.

### Exercises

- **EX045 — Threat table.** Produce a threat table for BPA's partner VPN covering the five threat classes. Rubric: 3 = each with mitigation.
- **EX046 — FMEA row.** Write an FMEA row for "middlebox drops two-segment ClientHello". Rubric: 3 = cause, effect, detection, mitigation, priority.

### Synthesis

Threat analysis in the quantum era includes recording, future forgery, downgrade, implementation attacks and cryptanalytic surprise; migration itself has failure modes that FMEA makes visible.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Quantum and post-quantum security: methods I

### Learning outcomes

You will (1) explain learning with errors (LWE) and why noise makes linear algebra hard; (2) follow a toy LWE encryption; (3) relate it to ML-KEM's structure; and (4) understand the role of the Fujisaki–Okamoto transform. It builds on Chapter 2 and grounds design choices in Chapters 25–28.

### 24.1 Learning with errors

Given a random matrix *A* and *b* = *A*·*s* + *e* mod *q*, where *s* is secret and *e* is a vector of small random errors, find *s*. Without *e* this is Gaussian elimination. With *e*, no efficient classical or quantum algorithm is known for suitable parameters; [Regev (2009)](https://doi.org/10.1145/1568318.1568324) related LWE to worst-case lattice problems. Best attacks use lattice reduction, whose cost grows exponentially in dimension.

### 24.2 Encrypting one bit

To encrypt a bit, sum a random subset of rows of (*A*, *b*): *u* = Σ*r*ᵢ*A*ᵢ, *v* = Σ*r*ᵢ*b*ᵢ + bit·⌊*q*/2⌋. The key holder computes *v* − ⟨*u*, *s*⟩ = bit·⌊*q*/2⌋ + small noise and rounds. Decryption works while the accumulated noise stays below *q*/4.

### 24.3 Practical activity — Lab W (toy, insecure)

```python
# Lab W (ch 24): a TOY Regev-style LWE encryption of one bit. Deliberately insecure parameters.
import random
rng = random.Random(5)
n, q, m = 16, 3329, 64
def small(): return rng.choice([-2, -1, 0, 1, 2])
s = [rng.randrange(q) for _ in range(n)]
A = [[rng.randrange(q) for _ in range(n)] for _ in range(m)]
b = [(sum(A[i][j] * s[j] for j in range(n)) + small()) % q for i in range(m)]   # b = A s + e
def enc(bit):
    r = [rng.randrange(2) for _ in range(m)]                                        # random subset
    u = [sum(r[i] * A[i][j] for i in range(m)) % q for j in range(n)]
    v = (sum(r[i] * b[i] for i in range(m)) + bit * (q // 2)) % q
    return u, v
def dec(u, v):
    d = (v - sum(u[j] * s[j] for j in range(n))) % q                                 # = bit*q/2 + small noise
    return 1 if q // 4 < d < 3 * q // 4 else 0
ok = sum(dec(*enc(bit)) == bit for bit in [rng.randrange(2) for _ in range(2000)])
print(f"toy LWE: {ok}/2000 bits decrypted correctly (noise stays below q/4)")
```

Expected output:

```text
toy LWE: 2000/2000 bits decrypted correctly (noise stays below q/4)
```

These parameters are far too small for security and leak through many routes; the lab exists only to make the algebra concrete.

### 24.4 From toy to ML-KEM

ML-KEM replaces integers with polynomials in Z₃₃₂₉[*x*]/(*x*²⁵⁶+1) and uses module structure (*k* = 2, 3 or 4 polynomial vectors) for compact keys, compresses ciphertexts, samples noise from a centred binomial distribution and derives randomness with SHAKE. The underlying public-key encryption is only secure against passive attackers; ML-KEM applies a Fujisaki–Okamoto-style transform — re-encrypting during decapsulation and returning a pseudo-random "implicit rejection" key on mismatch — to resist chosen-ciphertext attacks ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)).

### 24.5 Worked example

A BPA engineer asks why ML-KEM decapsulation re-encrypts. Answer: to detect manipulated ciphertexts. Without that check, an attacker could submit crafted ciphertexts and learn about the secret key from whether decryption succeeds. Implementations must perform the comparison in constant time, or the timing of the check leaks the same information.

### 24.6 Common errors and limits

- Thinking LWE security comes from the matrix rather than the noise.
- Using the passive-secure encryption without the FO transform.
- Treating the toy as a usable scheme.

### Exercises

- **EX047 — Noise budget.** In Lab W, change the error choices to `rng.randint(-150, 150)` and then `rng.randint(-300, 300)` and observe decryption. Explain. Rubric: 3 = failures appear; explains accumulated noise vs *q*/4.
- **EX048 — FO purpose.** Explain implicit rejection to a developer in 120 words. Rubric: 3 = chosen-ciphertext reasoning and constant-time requirement.

### Synthesis

LWE hides secrets under noise; a toy shows decryption as rounding; ML-KEM adds ring/module structure, compression and the FO transform for chosen-ciphertext security.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) run a structured design studio on a real-shaped problem; (2) produce a design for hybrid key exchange at BPA's edge; (3) present and defend it with evidence; and (4) incorporate critique. It integrates Chapters 20–24.

### 25.1 Brief

Design quantum-resistant key establishment for BPA's public portal and partner API edge: 2 million connections per day, mixed client population (browsers, partner software, old handheld scanners), an inspection proxy on one path and a CDN in front of the portal. Constraints: no availability regression beyond the requirement in Chapter 21, budget for one appliance upgrade, six-month timeline.

### 25.2 Studio method

Teams produce: context diagram; requirements subset; two alternatives; trade study; chosen design with configuration sketch; test plan; risks. Each team presents for ten minutes and receives critique from a panel playing operations, security, partners and finance.

### 25.3 Reference solution outline

Terminate TLS at the CDN and edge proxy with X25519MLKEM768 offered first and X25519 as fallback for clients that do not support the hybrid group ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)); upgrade the inspection proxy firmware or bypass inspection for TLS 1.3 to partner APIs; leave handheld scanners on classical groups behind a short-term exception with a replacement date; measure negotiated groups via logs; staged rollout with canary gates. Note: hybrid key exchange protects against recording; certificates remain classical for now — documented as a known gap with a later work package.

### 25.4 Critique examples

Operations asks how fallback is monitored; security asks whether fallback could be forced (in TLS 1.3, only by breaking authentication or exploiting application-level retry logic, which must be checked); partners ask about their clients' library versions; finance asks about appliance costs. Good teams answer with evidence or add work items.

### 25.5 Common errors and limits

- Designs that ignore the old client population.
- No measurement plan for negotiated groups.
- Claiming the portal is "quantum-safe" while certificates are classical.

### Engineering note

Studios also train the habit of writing down what the design does not do. The reference solution protects recorded key exchanges but not authentication, does not cover handheld scanners until replacement, and relies on vendor firmware for the inspection proxy. Listing these explicitly in the design record turns them into tracked work packages with owners, instead of discoveries made by an auditor. A design that states its gaps is easier to approve than one that appears complete but is not.

### Exercises

- **EX049 — Studio deliverable.** Produce the context diagram (with text alternative) and the trade study for the brief. Rubric: 3 = two real alternatives, weights before scores.
- **EX050 — Critique response.** Answer the security panel's fallback question in 150 words. Rubric: 3 = TLS 1.3 transcript protection and application retry risk both addressed.

### Synthesis

A design studio turns standards into a configured, measured and staged design whose gaps are stated and whose critics have been answered.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Quantum and post-quantum security: architecture alternatives

### Learning outcomes

You will (1) compare pure PQC, PQ/T hybrid and interim mitigations; (2) evaluate composite versus parallel certificates; (3) consider symmetric-key alternatives such as pre-shared keys; and (4) choose architecture per context. It builds on Chapters 18 and 25.

### 26.1 Pure versus hybrid

**Pure PQC** uses only post-quantum algorithms: simpler, smaller than hybrid, but stakes everything on newer assumptions. **PQ/T hybrid** combines both ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)): secure if either holds, at extra cost in bytes and complexity. During transition, many protocols and guidance documents favour hybrids for key exchange; some government guidance, such as CNSA 2.0, accepts pure PQC with the category-5 parameter sets. The choice depends on the risk appetite for cryptanalytic surprise versus complexity.

### 26.2 Certificates

Options for post-quantum authentication: (a) **pure PQC certificates** (ML-DSA keys and signatures); (b) **composite certificates** in which one certificate carries a traditional and a post-quantum key and both signatures must verify; (c) **parallel chains** — two certificates, one per algorithm, with negotiation choosing; (d) **delayed migration** with short-lived classical certificates, acceptable where active quantum attacks are not yet feasible. Each trades compatibility, size and complexity.

### 26.3 Interim mitigations

Where PQC is not yet available — old VPN appliances, for example — mixing a pre-shared symmetric key into key derivation can protect recorded traffic, since PSKs are not vulnerable to Shor. [RFC 8784](https://www.rfc-editor.org/rfc/rfc8784.html) defines such a mechanism for IKEv2. PSKs bring key-distribution and rotation burdens, so they are a bridge, not a destination.

### 26.4 Decision table

| Context | Key exchange | Authentication |
|---|---|---|
| Public web portal | Hybrid X25519MLKEM768 | Classical now, ML-DSA when clients support it |
| Partner VPN, old appliance | IKEv2 + PSK mixing (interim) | Classical, short-lived |
| Partner VPN, modern | IKEv2 with ML-KEM additional exchange (RFC 9370) | Per partner capability |
| Crane firmware | — | LMS/XMSS or ML-DSA |
| National-security partner | ML-KEM-1024 per CNSA 2.0 | ML-DSA-87 |

### 26.5 Worked example

BPA debates composite certificates for its internal PKI. Pros: one chain, both algorithms verified. Cons: limited library support, larger certificates, complex policy. Decision: parallel chains internally where clients can be updated, delay public certificate migration until browser ecosystem support exists; review annually.

### 26.6 Common errors and limits

- One architecture for all contexts.
- PSKs without rotation plans.
- Assuming composite certificates are universally supported.

### Exercises

- **EX051 — Hybrid argument.** Argue for hybrid key exchange in BPA's portal in 150 words, citing the scheme breaks. Rubric: 3 = either-holds reasoning and cost acknowledged.
- **EX052 — PSK bridge.** Design an interim PSK approach for one old VPN, including rotation. Rubric: 3 = distribution, rotation, retirement date.

### Synthesis

Architecture alternatives differ by context: hybrids hedge surprise, pure PQC simplifies, PSKs bridge, and certificate strategies trade compatibility against assurance.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Quantum and post-quantum security: control design

### Learning outcomes

You will (1) design the controls that make hybrid key exchange secure — combiners, transcript binding and negotiation; (2) design key-management controls for new key types; (3) specify policy controls for allowed algorithms; and (4) test a combiner. It builds on Chapters 24–26.

### 27.1 Combiner controls

A hybrid key exchange must derive the session key from both shared secrets so that compromise of one does not reveal the key. In X25519MLKEM768 the secrets are concatenated (ML-KEM first) and fed into the TLS 1.3 key schedule, which binds them to the handshake transcript ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)). Custom combiners outside standard protocols should follow [SP 800-56C](https://doi.org/10.6028/NIST.SP.800-56Cr2) key-derivation methods, which FIPS 203 permits for ML-KEM shared secrets, and bind context (identities, ciphertexts, transcript).

### 27.2 Practical activity — Lab C

```python
# Lab C (ch 27): a hybrid key combiner. The session key depends on BOTH shared secrets.
import hashlib, hmac
def hkdf_extract(salt, ikm): return hmac.new(salt, ikm, hashlib.sha256).digest()
def combine(ss_pq, ss_trad, context):
    # Concatenate secrets (PQ first, as in X25519MLKEM768), bind the transcript/context, then extract.
    return hkdf_extract(b"\x00" * 32, ss_pq + ss_trad + context).hex()[:16]
pq, trad, ctx = b"P" * 32, b"T" * 32, b"handshake-transcript-hash"
print("baseline              ", combine(pq, trad, ctx))
print("PQ secret changed     ", combine(b"Q" * 32, trad, ctx))
print("traditional changed   ", combine(pq, b"U" * 32, ctx))
print("context changed       ", combine(pq, trad, b"other-transcript"))
```

Expected output:

```text
baseline               d48e982e8c06ca60
PQ secret changed      d4c36ea2d90b2e9c
traditional changed    8dcefa12ded3d99c
context changed        af06eca8abcd45a9
```

Changing either secret or the context changes the output: the derived key depends on both components and on what was negotiated.

### 27.3 Negotiation controls

Algorithm negotiation must be authenticated. TLS 1.3 signs the transcript, so an attacker who strips hybrid groups is detected unless they can forge the server's signature. Application logic that retries without hybrid groups after any failure re-opens downgrade; controls: log and alert on fallback, and disable fallback where all peers support hybrids.

### 27.4 Key-management controls

New key types need lifecycle controls: generation in approved modules, storage, rotation, backup and destruction. ML-KEM decapsulation keys can be stored as a 64-byte seed per FIPS 203; stateful hash-based signature keys require state protection against rollback; ML-DSA keys need HSM support.

### 27.5 Policy controls

An allow-list of algorithms and parameter sets per context — e.g. "edge TLS: X25519MLKEM768, SecP256r1MLKEM768; fallback X25519 until 2027-12-31" — implemented in configuration and verified by telemetry.

### 27.6 Worked example

A BPA team proposes XOR-ing the two shared secrets to save a KDF call. Review rejects it: XOR offers no context binding and is fragile in some security proofs; use the protocol's standard combiner or SP 800-56C derivation with both secrets and context.

### 27.7 Common errors and limits

- Ad-hoc combiners (XOR, truncation).
- Silent fallback without logging.
- Treating stateful keys like ordinary keys in backup.

### Exercises

- **EX053 — Combiner review.** Review a proposal that hashes only the PQC secret "because it is stronger". Rubric: 3 = explains loss of hedge and recommends standard combiner.
- **EX054 — Policy file.** Write a policy allow-list for BPA's edge and internal services with expiry dates for fallbacks. Rubric: 3 = parameter sets explicit, expiry dated.

### Synthesis

Hybrid security depends on controls: standard combiners with context binding, authenticated negotiation without silent fallback, lifecycle management for new key types and dated allow-lists.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Quantum and post-quantum security: implementation I

### Learning outcomes

You will (1) select vetted libraries and validated modules; (2) integrate ML-KEM and ML-DSA through provider interfaces; (3) handle encodings, identifiers and interoperability; and (4) implement stateful signature management safely. It builds on Chapters 9, 14 and 27.

### 28.1 Library selection

Use maintained, reviewed implementations with constant-time code, test vectors and, where required, validation under NIST's Cryptographic Module Validation Program (CMVP). Prefer libraries that implement the final FIPS versions, not draft Kyber/Dilithium. Record the library, version and algorithm identifiers in the CBOM.

### 28.2 Integration through providers

Most platforms expose cryptography through providers (OpenSSL providers, Java security providers, PKCS#11 for HSMs). Integrate PQC by adding or upgrading providers and configuring algorithm names through policy. Applications calling generic interfaces (Chapter 9) need no code changes; those calling algorithm-specific functions do.

### 28.3 Identifiers and encodings

Interoperability depends on exact identifiers: TLS codepoints (0x11EC for X25519MLKEM768 in the [IANA registry](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml)), X.509 object identifiers for ML-DSA and ML-KEM keys, and key encodings (seed versus expanded key). Mismatches cause failures that look like network faults.

### 28.4 Stateful signatures

LMS/XMSS signing must never reuse a one-time key index. Controls: perform signing in an HSM that enforces monotonic state; reserve index ranges per signer; forbid restoring state from backups; monitor remaining signature capacity ([SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) requires hardware-module key generation and signing for these schemes). If these controls are infeasible, prefer stateless SLH-DSA or ML-DSA.

### 28.5 Worked example

BPA integrates ML-DSA-65 for bills of lading. The signing service uses an HSM via PKCS#11; verifiers in partner systems use a different library. Interoperability testing reveals that one library expected an expanded private-key format — irrelevant to verifiers but blocking key import in a backup HSM. Resolution: standardize on seed-based key storage and test import/export in both HSMs before production.

### 28.6 Common errors and limits

- Mixing draft and final algorithm implementations.
- Software signing for stateful schemes.
- Assuming identifiers match across vendors.

### Engineering note

Plan key and certificate formats with migration in mind. Store ML-KEM and ML-DSA private keys as seeds where the standard and module allow it, because seeds are compact and expand deterministically, which simplifies backup and HSM migration. Record which encoding each system uses in the CBOM, test export and import between every pair of modules before production, and keep a written procedure for key ceremonies that names the parameter set, encoding, module firmware version and witnesses.

### Exercises

- **EX055 — Library checklist.** Write a selection checklist for a PQC library. Rubric: 3 = final FIPS versions, constant-time, KATs, maintenance, validation.
- **EX056 — State plan.** Design LMS state management for two signing sites. Rubric: 3 = index partitioning, no rollback, capacity monitoring.

### Synthesis

Implement PQC through vetted, validated providers, exact identifiers and encodings, and rigorous state management for stateful signatures.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Quantum and post-quantum security: measurement

### Learning outcomes

You will (1) build and query a CBOM; (2) measure negotiated versus configured algorithms; (3) report coverage and unknown share; and (4) design metrics resistant to gaming. It builds on Chapters 17 and 22.

### 29.1 Sources of evidence

Inventory evidence comes from code scanning, configuration analysis, passive network observation of handshakes, endpoint logs and vendor declarations. Each sees different things: code shows intent, configuration shows what is offered, passive observation shows what is negotiated, vendors declare what closed products do. Combine them and record the source per finding.

### 29.2 Practical activity — Lab I

```python
# Lab I (ch 29): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("gateway-1", "key-exchange", "X25519MLKEM768", "passive"), ("gateway-1", "signature", "RSA-2048", "config"),
    ("scada-hmi", "key-exchange", "ECDHE-P256", "passive"), ("scada-hmi", "signature", "ECDSA-P256", "code"),
    ("billing", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("crane-plc", "unknown", "unknown", "none"), ("vpn", "key-exchange", "ECDHE-P384", "config")]
VULN = {"RSA-2048", "ECDHE-P256", "ECDSA-P256", "RSA-kex", "ECDHE-P384"}
assets = {r[0] for r in records}
unknown = {r[0] for r in records if r[2] == "unknown"}
vuln = [r for r in records if r[2] in VULN]
print(f"assets {len(assets)}, unknown {len(unknown)} ({100*len(unknown)/len(assets):.0f}%)")
print(f"quantum-vulnerable uses {len(vuln)}:", ", ".join(f"{a}/{f}" for a, f, _, _ in vuln))
print("hybrid key exchange present on:", [r[0] for r in records if "MLKEM" in r[2]])
```

Expected output:

```text
assets 5, unknown 1 (20%)
quantum-vulnerable uses 5: gateway-1/signature, scada-hmi/key-exchange, scada-hmi/signature, billing/key-exchange, vpn/key-exchange
hybrid key exchange present on: ['gateway-1']
```

The crane PLC's unknown status is a finding, not a gap to hide: it is 20% of this tiny inventory and must be resolved by vendor declaration or testbed analysis.

### 29.3 Metrics

- **Coverage**: assets with at least one cryptographic determination ÷ all assets.
- **Unknown share**: reported separately.
- **Negotiated hybrid share**: connections negotiating PQ/T groups ÷ connections, weighted by data class.
- **Vulnerable-use count** by function and data lifetime.
- **Time-to-replace**: elapsed days from policy change to full negotiation of a new algorithm in a service (an agility metric).

### 29.4 Gaming

"Percentage migrated" can be inflated by redefining assets or counting configuration instead of negotiation. Use auditable denominators and publish definitions.

### 29.5 Worked example

BPA's first CBOM report: 412 assets, coverage 82%, unknown 18%, 311 vulnerable uses, hybrid negotiation 0% (before rollout). After six months: coverage 94%, unknown 6%, hybrid negotiation 64% of edge connections, vulnerable uses on long-lived data reduced from 37 flows to 12.

### 29.6 Common errors and limits

- Hiding unknowns.
- Counting configured algorithms as protection.
- One-source inventories.

### Engineering note

Present measurements with their blind spots. Passive sensors in TLS 1.3 see the negotiated key-exchange group in the ServerHello but not the certificate, which is encrypted; endpoint logs fill that gap but only where logging is enabled. A good dashboard therefore shows, next to every metric, which source produced it and what share of assets that source can observe. Decision-makers then understand why certificate-migration figures come from configuration evidence while key-exchange figures come from the wire.

### Exercises

- **EX057 — Extend Lab I.** Add a record for a VPN with "IKEv2 ML-KEM-768 + ECDH" and update the hybrid list logic. Rubric: 3 = code works, VPN recognized as hybrid.
- **EX058 — Metric definitions.** Write precise definitions for coverage and negotiated hybrid share. Rubric: 3 = numerator, denominator, time window, data source.

### Synthesis

Measurement means a multi-source CBOM, negotiated rather than configured metrics, explicit unknowns and definitions that resist gaming.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify implementations with known-answer tests; (2) write negative tests for malformed inputs; (3) test interoperability across libraries; and (4) record verification evidence. It builds on Chapters 9, 28 and 29.

### 30.1 Known-answer tests

Known-answer tests (KATs) feed fixed inputs and compare outputs with published values. Standards bodies and the NIST Cryptographic Algorithm Validation Program publish vectors; for ML-KEM, deterministic test modes allow fixed randomness so outputs can be compared byte for byte.

### 30.2 Practical activity — Lab V

```python
# Lab V (ch 30): known-answer and negative tests - the habit behind validating PQC libraries.
import hashlib
KATS = [  # (function, input, expected hex prefix) - published test values for SHA-3 / SHAKE on empty input
    ("sha3_256", b"", "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"),
    ("shake_128/32", b"", "7f9c2ba4e88f827d616045507605853ed73b8093f6efbc88eb1a6eacfa66ef26"),
]
def run(name, data):
    if name == "sha3_256": return hashlib.sha3_256(data).hexdigest()
    return hashlib.shake_128(data).hexdigest(32)
for name, data, want in KATS:
    print(f"KAT {name:13s}", "PASS" if run(name, data) == want else "FAIL")
SIZES = {"ML-KEM-512": 800, "ML-KEM-768": 1184, "ML-KEM-1024": 1568}   # encapsulation-key bytes, FIPS 203
def validate_ek(param, ek):
    if len(ek) != SIZES[param]: raise ValueError(f"{param}: expected {SIZES[param]} bytes, got {len(ek)}")
    return True
for param, n in [("ML-KEM-768", 1184), ("ML-KEM-768", 1183), ("ML-KEM-512", 1184)]:
    try: validate_ek(param, bytes(n)); print(f"negative/positive test {param} len {n}: accepted")
    except ValueError as e: print(f"negative/positive test {param} len {n}: rejected ({e})")
```

Expected output:

```text
KAT sha3_256      PASS
KAT shake_128/32  PASS
negative/positive test ML-KEM-768 len 1184: accepted
negative/positive test ML-KEM-768 len 1183: rejected (ML-KEM-768: expected 1184 bytes, got 1183)
negative/positive test ML-KEM-512 len 1184: rejected (ML-KEM-512: expected 800 bytes, got 1184)
```

The length validator is only the first check: FIPS 203 also requires checking that encoded coefficients of an encapsulation key are below *q* (the modulus check) and a hash check on decapsulation keys. Real libraries implement these; your tests should confirm they reject bad keys.

### 30.3 Interoperability

Run handshakes between every pair of client and server implementations in scope; encapsulate with one library and decapsulate with another; sign with the HSM and verify in partner software. Record the matrix. Interoperability failures early in the programme are cheap; in production they are outages.

### 30.4 Evidence

Each test run records: implementation and version, test vectors used, result, date, operator. Evidence feeds the verification column of the traceability matrix (Chapter 21).

### 30.5 Worked example

BPA's interoperability matrix for edge TLS: three server stacks × five client families. Two failures: an old partner library offered the obsolete pre-standard codepoint and could not complete hybrid handshakes; a load balancer stripped unknown groups. Both get work items; neither blocks rollout, because fallback to X25519 works and is logged.

### 30.6 Common errors and limits

- Only positive tests.
- Testing a library against itself.
- Unrecorded results.

### Engineering note

Verification evidence should be reproducible by someone else. Store the exact test vectors, tool versions and command lines alongside results, and rerun the suite automatically whenever a library, provider or HSM firmware changes. When a vendor publishes an advisory, the team can then answer within hours whether the affected version is deployed and whether its tests still pass, instead of reconstructing the original verification from memory and screenshots.

### Exercises

- **EX059 — Negative tests.** List five negative tests for an ML-KEM decapsulation function. Rubric: 3 = wrong length, modified ciphertext, wrong key, malformed key, repeated calls consistency.
- **EX060 — Interop matrix.** Design the interoperability matrix for BPA's bills-of-lading signatures. Rubric: 3 = signers, verifiers, formats, expected results.

### Synthesis

Verification combines known-answer tests, negative tests and cross-implementation interoperability, all recorded as evidence traced to requirements.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Quantum and post-quantum security: implementation II

### Learning outcomes

You will (1) apply constant-time techniques to lattice code; (2) understand fault attacks and countermeasures; (3) handle randomness and seeds safely; and (4) assess embedded implementations. It deepens Chapter 28 with implementation security.

### 31.1 Constant time

Lattice implementations must avoid secret-dependent branches, memory accesses and variable-time instructions. Division is a known trap: compilers and processors may implement division by a constant with variable timing, and KyberSlash showed real leaks from secret-dependent divisions ([Bernstein et al. 2024](https://eprint.iacr.org/2024/1049)). The fix is arithmetic that avoids division (multiplication by precomputed constants and shifts) and verification with timing-analysis tools.

### 31.2 Decapsulation comparison

ML-KEM's implicit rejection compares a re-encrypted ciphertext with the received one. The comparison and the selection between the real key and the rejection key must be constant-time; otherwise timing reveals whether a manipulated ciphertext decrypted "correctly", re-opening chosen-ciphertext attacks.

### 31.3 Fault attacks

Injecting faults (voltage glitches, clock glitches, lasers) can skip checks or corrupt computations. In signatures, a fault during ML-DSA signing can leak information about the secret key; in deterministic schemes, faults can be especially dangerous. Countermeasures include redundant computation, verifying a signature before releasing it and hardened hardware. These matter for devices an attacker can physically access — gate scanners, smart cards.

### 31.4 Randomness and seeds

ML-KEM key generation and encapsulation consume fresh randomness; ML-DSA offers a "hedged" mode mixing fresh randomness with deterministic derivation, which helps against fault and randomness failures ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)). Seeds that generate keys are as sensitive as the keys themselves.

### 31.5 Worked example

BPA's gate-scanner vendor provides an ML-DSA verifier for firmware. Since the device only verifies, secret-key leakage is not at stake on the device; the main risks are faults that skip the verification result. Countermeasure: verify twice with different code paths and check a hash of the image after boot.

### 31.6 Common errors and limits

- Assuming compilers preserve constant-time intent.
- Ignoring physical attacks for field devices.
- Treating seeds as non-sensitive.

### Exercises

- **EX061 — Division audit.** Explain why `coeff // 1665` on a secret value can leak and propose an alternative. Rubric: 3 = variable-time division risk and multiplication/shift alternative.
- **EX062 — Fault threat.** For a verify-only bootloader, identify the fault threat and two countermeasures. Rubric: 3 = skipped check; redundant verification and post-boot hash.

### Synthesis

Implementation security for PQC means constant-time arithmetic and comparisons, fault resistance where attackers have physical access, and careful randomness and seed handling.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Quantum and post-quantum security: reliability

### Learning outcomes

You will (1) identify reliability risks from larger messages and new code paths; (2) design fallback and retry behaviour that preserves security; (3) plan capacity for stateful signature schemes; and (4) monitor for silent failures. It builds on Chapters 23 and 30.

### 32.1 Reliability risks

New risks: fragmentation and middlebox drops; timeouts on slow constrained devices; certificate parsing failures; library bugs in new code; exhausted stateful signature keys; HSM performance limits. Each needs detection and response.

### 32.2 Secure fallback

Fallback can preserve availability but must not create silent downgrade. Design rules: fallback only to approved algorithms; log every fallback with reason; alert when fallback rates rise; set an expiry date on fallback permission; never fall back on authentication failures, only on demonstrable incompatibility.

### 32.3 Capacity of stateful schemes

An LMS key with tree height 20 supports about one million signatures; a height-10 tree about one thousand. Capacity must exceed expected signing volume over the key's life with margin; monitoring alerts at thresholds (e.g. 70% used) trigger planned rollover.

### 32.4 Silent failures

The worst reliability failure is security silently disabled: a configuration that falls back to classical-only everywhere because of a typo. Monitoring negotiated groups (Chapter 29) detects this.

### 32.5 Worked example

BPA signs about 2,000 firmware images a year across all device families. A height-15 LMS tree (32,768 signatures) per signing site lasts more than a decade at current volume; the team still sets alerts at 50% and 80% and documents rollover to a new key with distribution of its public key in advance.

### 32.6 Common errors and limits

- Fallback without logging or expiry.
- Under-sized stateful keys.
- Monitoring configuration instead of negotiation.

### Engineering note

Reliability reviews should also cover clocks and expiry. Transitional certificates, PSKs with rotation dates and fallback permissions all expire by design; if renewal automation fails, the result is an outage that looks like a cryptographic fault. Calendar the expiries in the monitoring system with alerts at 30, 14 and 3 days, and test renewal paths in the replica environment, because the first renewal of a new algorithm's certificate is a classic place for parsing or policy mismatches to appear.

### Exercises

- **EX063 — Fallback policy.** Write a fallback policy for edge TLS satisfying the rules in 32.2. Rubric: 3 = all five rules embodied.
- **EX064 — Capacity.** A site signs 15 documents per minute continuously with LMS. Is a height-20 tree enough for one year? Rubric: 3 = 7.9 million signatures/year > 1,048,576 — not enough; proposes HSS/multiple trees or ML-DSA.

### Synthesis

Reliability engineering for PQC anticipates size and code-path failures, designs logged, expiring, authentication-safe fallback, sizes stateful keys with margin and monitors negotiated outcomes.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Quantum and post-quantum security: safety and resilience

### Learning outcomes

You will (1) analyse how cryptographic migration interacts with safety-related operations; (2) design resilient rollouts for operational technology at the port; (3) plan cryptographic incident response, including algorithm compromise; and (4) prepare for a "crypto-break" scenario. It builds on Chapters 10, 23 and 32.

### 33.1 Safety interactions

At BPA, cranes, gate systems and vessel-traffic services must keep operating. A failed firmware signature verification can brick a crane controller; a certificate rejected by a gate scanner can stop trucks. Migration steps on such systems require testing on spare units, maintenance windows, verified rollback images and operator sign-off.

### 33.2 Resilient rollout

Use rings: lab → spare unit → one low-impact unit → one site → all. Each ring has a hold period and explicit success criteria. Keep the previous verification key trusted until the new chain is proven, so rollback remains possible.

### 33.3 Cryptographic incident response

Plan for: a vulnerability in a PQC library (patch and re-key), a key compromise (revoke and replace), a stateful key index reuse (treat as compromise), and a cryptanalytic break of an algorithm (switch to the alternative). Hybrids give time in the last case: if ML-KEM were weakened, X25519 still protects against classical attackers while agility replaces the post-quantum component — for example with HQC once standardized ([IR 8545](https://doi.org/10.6028/NIST.IR.8545)).

### 33.4 Tabletop: algorithm break

Scenario: a credible paper reports a practical attack on one post-quantum signature parameter set. Questions: where is it used (CBOM)? What depends on it (roots, firmware)? What is the alternative (SLH-DSA, a different ML-DSA level)? How long does replacement take (time-to-replace metric)? Who decides? The tabletop measures agility directly.

### 33.5 Worked example

BPA's tabletop finds that crane firmware trusts only one signature algorithm, with no provision for a second key in the bootloader. Action: the next bootloader release accepts two verification keys of different algorithms (e.g. LMS and ML-DSA), so a break of one does not strand devices.

### 33.6 Common errors and limits

- Rolling cryptographic changes to safety systems without spares and rollback.
- No plan for algorithm compromise.
- Single-algorithm trust anchors in long-lived devices.

### Exercises

- **EX065 — Rings.** Define rollout rings and criteria for crane firmware signed with a new algorithm. Rubric: 3 = spares, hold periods, rollback.
- **EX066 — Tabletop.** Run the algorithm-break tabletop for BPA's bills of lading and record actions. Rubric: 3 = uses CBOM, alternative scheme, time-to-replace.

### Synthesis

Safety and resilience demand ringed rollouts with rollback, incident plans that include algorithm breaks, and trust anchors that can accept more than one algorithm.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Quantum and post-quantum security: integration

### Learning outcomes

You will (1) integrate PQC across TLS, VPN, PKI, code signing and data formats; (2) manage partner and vendor integration; (3) sequence integration to manage dependencies; and (4) run integration tests end to end. It builds on Chapters 16, 28 and 30.

### 34.1 Integration map

| Domain | Integration point | Dependency |
|---|---|---|
| Web/TLS | CDN, edge proxy, internal load balancers | Client support, middleboxes |
| VPN | IKEv2 gateways | Peer vendors, RFC 9370 support |
| PKI | CA software, HSM, certificate profiles | Relying-party support |
| Code signing | Signing service, device bootloaders | Device firmware updates |
| Documents | Bill-of-lading signatures, CMS exports | Partner and customs software |

### 34.2 Partner integration

Partners move at their own pace. Publish a migration notice with timelines, supported algorithms and test endpoints; offer an interoperability test environment; keep classical paths available with dated sunset. The customs agency, for example, may accept ML-KEM-wrapped exports only after its own upgrade; parallel recipients in CMS (classical and PQC) bridge the gap.

### 34.3 Sequencing

Sequence by dependency and value: edge TLS first (independent, high value); PKI root and HSM next (long lead time, enabler for signatures); firmware signing as devices are refreshed; documents with partners; internal services by data lifetime.

### 34.4 End-to-end tests

Integration tests exercise whole flows: a partner client connecting through the edge to an API that signs a document with ML-DSA, stored and replicated over hybrid TLS, verified by a customs test system. Failures in such tests reveal interface mismatches no unit test finds.

### 34.5 Worked example

BPA's integration plan has 14 work packages. A dependency graph shows that the HSM upgrade gates five of them; procurement is therefore started in month one even though signatures are not urgent until month nine.

### 34.6 Common errors and limits

- Integrating domains in isolation.
- Forgetting partner sunset dates.
- No end-to-end tests.


### 34.7 Integration readiness checklist

Before BPA switches a partner link to hybrid key exchange, the integration owner confirms four items: the partner's stack advertises the same hybrid group, both sides log the negotiated group, a classical fallback is still allowed only where the agreed exception list permits it, and a joint test window is booked with a rollback contact on each side. A link that fails any item stays on its current configuration and is rescheduled rather than forced.

### Exercises

- **EX067 — Dependency graph.** Draw (or list) the dependency graph for BPA's 5 domains. Rubric: 3 = HSM and partner dependencies visible.
- **EX068 — Partner notice.** Write a migration notice for shipping-line partners. Rubric: 3 = algorithms, test endpoints, timeline, sunset, contact.

### Synthesis

Integration spans protocols, PKI, signing and documents; partners need notices and test environments; sequencing follows dependencies; end-to-end tests catch interface mismatches.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design post-quantum authentication for a document and firmware ecosystem; (2) choose among ML-DSA, SLH-DSA and stateful hash signatures; (3) design long-term validation with timestamps; and (4) defend the design to a panel. It integrates Chapters 26–34.

### 35.1 Brief

Design post-quantum signatures for BPA's (a) electronic bills of lading verifiable for 12 years by partners and courts, and (b) firmware for 3,000 field devices with 10–20 year lifetimes and constrained bootloaders. Constraints: partner verification software varies; some devices cannot be updated beyond one more bootloader version.

### 35.2 Reference solution outline

(a) Bills of lading: sign with ML-DSA-65 alongside the existing ECDSA signature during transition (dual signatures in the document format), add trusted timestamps, and plan re-timestamping (archive timestamp renewal) so that evidence remains valid if an algorithm weakens. (b) Firmware: final bootloader version accepts two verification keys — LMS (SP 800-208, verify-only on device, signing in HSM with state control) and ML-DSA-44 — so that compromise or breakage of one leaves the other; sign every image with both.

### 35.3 Panel critique

Legal asks whether dual signatures confuse courts — answer: document policy states either valid signature suffices during transition, both required after a date. Operations asks about signing throughput — LMS capacity sized per Chapter 32. Security asks why not SLH-DSA for firmware — its larger signatures (7.8 kB+ for the small variant) may exceed boot-time and storage budgets on the smallest devices, but it remains a candidate for others.

### 35.4 Common errors and limits

- Single-algorithm trust anchors for devices that cannot be updated again.
- Ignoring long-term validation and timestamp renewal.
- Choosing stateful signatures without state management capability.

### Engineering note

Long-term validation deserves its own test. Simulate verifying a bill of lading in a future year by setting the verifier's policy to reject ECDSA and accept only ML-DSA and renewed timestamps; documents signed early in the transition must still validate through their archive timestamp chain. Running this test now reveals whether the document format, timestamp authority and verifier software actually support the transition rules that the legal team approved on paper.

### Exercises

- **EX069 — Document design.** Specify the signature fields and validation policy for dual-signed bills of lading. Rubric: 3 = transition rules and timestamp renewal.
- **EX070 — Bootloader keys.** Justify the two-algorithm bootloader design and its cost. Rubric: 3 = diversity benefit vs code size and signing cost.

### Synthesis

Long-lived authentication needs algorithm diversity, timestamping with renewal and signature choices fitted to device constraints and state-management capability.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Quantum and post-quantum security: performance and scale

### Learning outcomes

You will (1) budget bytes and computation for post-quantum handshakes; (2) measure latency and throughput; (3) assess certificate-chain size effects; and (4) scale signing and verification services. It builds on Chapters 8, 11 and 29.

### 36.1 Byte budgets

ML-KEM adds about 2.3 kB to a hybrid TLS handshake (1,216-byte client share plus 1,120-byte server share). Post-quantum certificates add far more: each ML-DSA-44 certificate carries a 1,312-byte key and a 2,420-byte signature; a chain plus CertificateVerify and Certificate Transparency signatures can exceed 15 kB — beyond TCP's initial congestion window in many configurations, costing an extra round trip.

### 36.2 Practical activity — Lab B

```python
# Lab B (ch 36): bytes of authentication in a TLS handshake for different signature choices.
# Sizes in bytes: (public key, signature). ML-DSA from FIPS 204; SLH-DSA-128s from FIPS 205.
algs = {"ECDSA P-256": (65, 72), "RSA-2048": (270, 256), "ML-DSA-44": (1312, 2420),
        "ML-DSA-65": (1952, 3309), "SLH-DSA-SHA2-128s": (32, 7856)}
def chain_bytes(alg, depth=2, scts=2):
    pk, sig = algs[alg]
    certs = depth * (pk + sig + 400)          # leaf + intermediate: key + CA signature + ~400 B fields
    return certs + sig + scts * sig           # + CertificateVerify + embedded SCT signatures
for a in algs:
    print(f"{a:20s} ~{chain_bytes(a):6d} bytes of certificates and signatures")
```

Expected output:

```text
ECDSA P-256          ~  1290 bytes of certificates and signatures
RSA-2048             ~  2620 bytes of certificates and signatures
ML-DSA-44            ~ 15524 bytes of certificates and signatures
ML-DSA-65            ~ 21249 bytes of certificates and signatures
SLH-DSA-SHA2-128s    ~ 40144 bytes of certificates and signatures
```

The ~400-byte per-certificate overhead and the two embedded SCT signatures are simplifying assumptions; real sizes vary. The result explains why authentication migration on the public web is harder than key exchange and why proposals to reduce chain size (such as abridged or merkle-tree certificates) are active research topics.

### 36.3 Computation

ML-KEM operations are fast — often faster than X25519 on servers with vector instructions. ML-DSA signing and verification are fast; SLH-DSA signing is slow (milliseconds to seconds depending on variant). Server capacity planning therefore focuses on bandwidth and signing services rather than KEM CPU.

### 36.4 Measurement

Measure handshake latency percentiles (p50, p95, p99) by client type and network path before and after; throughput of signing services; HSM operations per second for new algorithms. Report distributions, not averages.

### 36.5 Worked example

BPA measures edge handshakes: p50 latency +0.4 ms, p99 +3 ms after enabling X25519MLKEM768 (synthetic); within budget. A test of an ML-DSA-65 chain on a satellite link to a vessel shows an extra round trip (+600 ms) — so vessel connections keep classical certificates longer and get session resumption tuned.

### 36.6 Common errors and limits

- Benchmarking only CPU.
- Averages instead of tail latency.
- Ignoring congestion-window effects of large chains.

### Engineering note

Capacity planning should include the people who will read the numbers. Express results as changes in user-visible latency at the 99th percentile per path and as bytes per connection for the network team, not only as operations per second. A two-millisecond median change is usually invisible, while a whole extra round trip on a high-latency vessel link is not; presenting both side by side lets stakeholders accept the cheap change and plan around the expensive one.

### Exercises

- **EX071 — Chain budget.** Using Lab B, find the depth-1 (leaf only) size for ML-DSA-44 with no SCTs. Rubric: 3 = correct value and method.
- **EX072 — Measurement plan.** Write a latency measurement plan for the vessel link. Rubric: 3 = percentiles, paths, before/after, sample size.

### Synthesis

PQC performance is mostly about bytes: key exchange adds kilobytes, certificates add many more; measure tails and paths, and plan signing capacity.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Quantum and post-quantum security: operations

### Learning outcomes

You will (1) operate staged rollouts with statistical gates; (2) monitor negotiated algorithms and fallback; (3) manage certificates and keys for new algorithms; and (4) run change and incident processes. It builds on Chapters 17, 32 and 36.

### 37.1 Canary gates

Promote a rollout stage only when the upper confidence bound of the failure rate is within the budget. Small canaries cannot demonstrate small effects — the bound is wide — so the gate holds until enough traffic has been observed.

### 37.2 Practical activity — Lab K

```python
# Lab K (ch 37): canary gate for enabling a hybrid group - promote only if failures stay within budget.
import math
def upper95(k, n):                      # Wilson upper bound
    z = 1.96; p = k / n; d = 1 + z*z/n
    return ((p + z*z/(2*n)) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
baseline, budget = 5e-4, 4e-4            # baseline failure rate, allowed increase
for stage, k, n in [("1% canary", 3, 5000), ("10% canary", 28, 50000), ("10% canary (proxy site)", 96, 50000)]:
    ub = upper95(k, n); ok = ub <= baseline + budget
    print(f"{stage:24s} {k}/{n}  upper95={ub:.5f}  {'PROMOTE' if ok else 'HOLD'}")
```

Expected output:

```text
1% canary                3/5000  upper95=0.00176  HOLD
10% canary               28/50000  upper95=0.00081  PROMOTE
10% canary (proxy site)  96/50000  upper95=0.00234  HOLD
```

The 1% canary holds not because failures are high but because 5,000 connections cannot bound the rate tightly. The proxy site holds because its rate is genuinely higher — a local problem to fix, not a reason to roll back globally.

### 37.3 Monitoring

Dashboards: negotiated groups by service, fallback rate and reasons, handshake failures by path, certificate algorithms in use, stateful key capacity, library versions. Alerts on fallback spikes and on any unexpected classical-only negotiation where hybrids are required.

### 37.4 Certificate and key operations

Certificate lifecycle automation (for example ACME, [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555.html)) makes algorithm changes routine: short-lived certificates can switch algorithms at renewal. Key ceremonies for new PQC roots are planned like any root ceremony, with witnesses and recorded procedures.

### 37.5 Worked example

BPA's operations runbook for hybrid TLS: daily dashboard review during rollout; promote via gates; on gate hold, investigate by path; on fallback spike, check recent changes; on proxy-site failures, apply path-specific exception with expiry and open vendor ticket.

### 37.6 Common errors and limits

- Promoting on point estimates from small canaries.
- Global rollback for local faults.
- Manual certificate processes that make algorithm change slow.

### Engineering note

Operations also own communication during rollout. Publish a short status note each promotion stage listing the stage, measured failure bound, known exceptions and next decision date, so that help-desk staff can recognize related tickets and partners can plan. A help desk that knows a hybrid rollout reached the hospital-wing proxy yesterday will route a cluster of connection complaints correctly in minutes instead of treating them as unrelated faults for days.

### Exercises

- **EX073 — Gate arithmetic.** With baseline 5e-4 and budget 4e-4, is 30 failures in 50,000 connections promotable? Use Lab K's function. Rubric: 3 = correct decision with upper bound shown.
- **EX074 — Runbook.** Write the runbook section for "fallback rate doubled overnight". Rubric: 3 = triage steps, owners, escalation.

### Synthesis

Operations turns rollout into controlled steps with statistical gates, monitoring of negotiated outcomes, automated certificate lifecycles and path-specific responses.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Quantum and post-quantum security: validation

### Learning outcomes

You will (1) validate that the migrated system meets stakeholder needs; (2) distinguish verification evidence from validation evidence; (3) run user-facing and partner acceptance tests; and (4) validate risk reduction claims carefully. It builds on Chapters 16, 30 and 37.

### 38.1 Verification versus validation

Verification shows requirements are met ("edge TLS negotiates X25519MLKEM768 with 99.2% of offering clients"). Validation shows the system serves its purpose ("shipping lines, customs and staff operate normally, and long-lived data flows are protected against recording"). Both are needed; one does not imply the other.

### 38.2 Acceptance tests

Partners run acceptance tests on their workflows; operations staff confirm no new incidents; legal confirms dual-signed documents are acceptable; device teams confirm firmware updates succeed across models. Record acceptance with dates and signatories.

### 38.3 Validating risk reduction

Claim carefully: "Recorded edge traffic negotiated with hybrid groups is protected against future quantum decryption if either X25519 or ML-KEM-768 remains secure" is defensible. "BPA is quantum-safe" is not — certificates, some VPNs, devices and unknown assets remain. Validation reports what is protected and what is not.

### 38.4 Independent validation

An independent team (internal audit or external assessor) samples flows, checks negotiated algorithms from their own vantage point and reviews the CBOM's unknowns. Independence catches optimistic self-assessment.

### 38.5 Worked example

BPA's validation report: 64% of edge connections hybrid (verification); partner acceptance complete for 11 of 14 lines (validation); customs exports dual-recipient (validation pending agency test); firmware dual-key bootloader on 40% of devices; unknown assets 6%. Statement of residual risk lists the remaining classical paths with dates.

### 38.6 Common errors and limits

- Treating verification metrics as validation.
- Overclaiming "quantum-safe".
- Self-validation only.

### Engineering note

Validation should revisit the original stakeholder needs from Chapter 21 one by one. For each, state whether it is met, partly met or not met, with evidence, and record any need that changed during the programme — for example, a partner whose data retention requirement grew from five to ten years after a contract renewal. Needs drift; validation that checks against the original list alone can declare success on a target that no longer reflects what stakeholders actually require.

### Exercises

- **EX075 — Residual risk.** Write the residual-risk statement for BPA after year one. Rubric: 3 = lists unprotected paths with dates and owners.
- **EX076 — Independence.** Design an independent validation sample for edge TLS. Rubric: 3 = vantage point, sample size, comparison with internal metrics.

### Synthesis

Validation confirms the migrated system serves its stakeholders and states residual risk honestly, ideally checked by an independent team.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Quantum and post-quantum security: maintainability

### Learning outcomes

You will (1) design for crypto-agility so future changes are cheap; (2) implement policy-driven algorithm selection; (3) manage algorithm retirement; and (4) keep inventory and documentation current. It builds on Chapters 9, 18 and 27.

### 39.1 Agility as maintainability

The post-quantum transition will not be the last: parameter sets may change, HQC and FN-DSA will arrive, and some algorithm may weaken. [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) describes agility across protocols, applications, hardware and infrastructure. Maintainable systems make algorithm change a routine operation measured in days.

### 39.2 Practical activity — Lab A

```python
# Lab A (ch 39): crypto-agility through a policy-driven registry instead of hard-coded algorithms.
import hashlib, hmac
REGISTRY = {"hmac-sha256": lambda k, m: hmac.new(k, m, hashlib.sha256).digest(),
            "hmac-sha3-256": lambda k, m: hmac.new(k, m, hashlib.sha3_256).digest()}
POLICY = {"tag-algorithm": "hmac-sha256", "accept": ["hmac-sha256", "hmac-sha3-256"]}
def protect(key, msg):
    alg = POLICY["tag-algorithm"]; return alg, REGISTRY[alg](key, msg)
def check(key, msg, alg, tag):
    if alg not in POLICY["accept"]: return False            # algorithm identifier is authenticated by policy
    return hmac.compare_digest(REGISTRY[alg](key, msg), tag)
k, m = b"k" * 32, b"meter reading 42"
a1, t1 = protect(k, m)
POLICY["tag-algorithm"] = "hmac-sha3-256"                   # migration = one policy change
a2, t2 = protect(k, m)
print("old tag still verifies during transition:", check(k, m, a1, t1))
print("new tag verifies:", check(k, m, a2, t2), "| algorithms:", a1, "->", a2)
POLICY["accept"] = ["hmac-sha3-256"]                        # retire the old algorithm
print("old tag after retirement:", check(k, m, a1, t1))
```

Expected output:

```text
old tag still verifies during transition: True
new tag verifies: True | algorithms: hmac-sha256 -> hmac-sha3-256
old tag after retirement: False
```

The lab uses symmetric MACs to keep the code short; the pattern — registry, policy, accept-list, retirement — is identical for KEMs and signatures.

### 39.3 Retirement

Retiring an algorithm has phases: stop generating new uses; accept old uses during a transition window; reject after a date; remove code. Each phase is a policy change plus monitoring of residual use.

### 39.4 Documentation and inventory

Keep the CBOM, interface control documents, policies and runbooks current through automation where possible (build-time CBOM generation, telemetry-fed dashboards). Stale documentation makes the next migration as hard as the first.

### 39.5 Worked example

BPA measures time-to-replace by switching the internal MAC algorithm on a test service through policy: 2 days including tests. The same exercise on a legacy service with hard-coded algorithms takes 6 weeks — a quantified case for refactoring.

### 39.6 Common errors and limits

- Treating PQC migration as a one-time project.
- Accepting algorithm identifiers from untrusted input without policy checks.
- Retiring algorithms without monitoring residual use.

### Engineering note

Agility is also contractual. Procurement language should require vendors to support algorithm replacement through configuration, publish cryptographic inventories for their products, provide security updates for new algorithms within stated periods and disclose the libraries they embed. BPA adds these clauses to every new contract for appliances and software; over a hardware refresh cycle, the share of assets that can change algorithms without replacement rises, and the next migration becomes cheaper by design.

### Exercises

- **EX077 — Extend Lab A.** Add a third algorithm and a retirement date check. Rubric: 3 = works and fails closed after the date.
- **EX078 — Time-to-replace.** Design a time-to-replace measurement for BPA's edge KEM. Rubric: 3 = start/end events and evidence defined.

### Synthesis

Maintainability means agility: policy-driven algorithms, phased retirement, current inventory and a measured time-to-replace.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify end-to-end protections from an attacker's vantage point in a lab; (2) test downgrade resistance; (3) verify stateful signature state handling; and (4) produce a verification report. It builds on Chapters 30–39.

### 40.1 Attacker's-vantage verification

In an isolated lab replicating BPA's edge, capture handshakes and confirm the negotiated group from the wire, not from server logs. Verify that recorded sessions with hybrid groups would require breaking both X25519 and ML-KEM — by checking that the session key derivation includes both shares (Lab C's principle).

### 40.2 Downgrade tests

A lab man-in-the-middle strips hybrid groups from ClientHello. Expected: TLS 1.3's transcript signature causes failure, or the client retries without hybrid only if application logic permits — which the test should catch and the policy should forbid where possible. Run only in the lab.

### 40.3 State-handling tests

For LMS/XMSS: simulate HSM restore from backup and confirm the HSM refuses to reuse indices; simulate concurrent signing requests and confirm no duplicate index; exhaust a small test tree and confirm signing stops cleanly.

### 40.4 Verification report

Report: scope, environment, tests, results, deviations, residual issues, evidence links. A good report lets a reviewer re-run tests.

### 40.5 Worked example

BPA's lab finds that one internal client library retries with classical-only groups after any handshake error, including those caused by an attacker. Fix: restrict retry to specific incompatibility errors, log retries and plan removal of fallback for that client by a set date.

### 40.6 Common errors and limits

- Verifying from server logs only.
- Downgrade testing on production.
- Not testing state restore for stateful signatures.

### Engineering note

Include negative controls in every lab run. Before testing downgrade resistance, confirm that the test harness can detect a successful downgrade by deliberately configuring a client that permits it; if the harness reports no downgrade even then, it is broken. Negative controls are cheap and prevent the most embarrassing verification failure — a green report produced by a test that could never have failed.

### Exercises

- **EX079 — Downgrade test plan.** Write the lab plan for the downgrade test. Rubric: 3 = isolation, expected results, pass/fail criteria.
- **EX080 — State test.** Write three state-handling test cases for an LMS HSM. Rubric: 3 = restore, concurrency, exhaustion.

### Synthesis

Second-stage verification checks protections from the attacker's vantage point, tests downgrade and state handling in isolation and produces re-runnable reports.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Quantum and post-quantum security: system optimization

### Learning outcomes

You will (1) optimize parameter and algorithm choices across a system; (2) reduce handshake overhead with resumption and caching; (3) balance security categories against cost; and (4) prioritize remaining migration work for maximum risk reduction. It builds on Chapters 6, 36 and 39.

### 41.1 Parameter choices

ML-KEM-768 (category 3) is the common default for hybrid TLS; ML-KEM-1024 where policy requires category 5 (CNSA 2.0). ML-DSA-44 versus -65 trades size against margin. Choose per context with documented rationale, not "maximum everywhere".

### 41.2 Overhead reduction

Session resumption avoids repeated full handshakes; connection reuse amortizes certificate cost; certificate compression ([RFC 8879](https://www.rfc-editor.org/rfc/rfc8879.html)) helps classical chains but compresses random-looking post-quantum keys and signatures poorly; trimming intermediate certificates where clients cache them reduces bytes.

### 41.3 Risk-reduction prioritization

With limited budget, rank remaining work by exposure reduced per unit effort: flows carrying long-lived data × volume ÷ effort. A greedy ordering is usually good enough and transparent.

### 41.4 Worked example

BPA's remaining items: vessel links (high latency cost of large chains; moderate data lifetime), legacy VPN (high lifetime, appliance replacement cost), internal telemetry (low lifetime). Optimization: vessel links get hybrid key exchange only (cheap) with classical certificates and tuned resumption; legacy VPN gets PSK mixing now and appliance replacement next budget cycle; telemetry waits.

### 41.5 Common errors and limits

- Category 5 everywhere without need.
- Expecting compression to shrink PQC signatures.
- Prioritizing by ease rather than exposure.

### Engineering note

Optimization decisions should be revisited when inputs change. A new browser release that supports post-quantum certificates, a firmware update that fixes a middlebox, or a revised policy date can reorder the remaining work. Keep the ranking as a small, version-controlled table with the assumptions written beside each score, and recompute it at every quarterly review rather than treating the first ranking as a permanent plan.


### 41.6 Optimisation that must not weaken security

Shrinking handshake size by dropping intermediate certificates or caching keys for longer can save milliseconds, but each such change is reviewed against BPA's confidentiality horizon. An optimisation that shortens latency but reintroduces a classical-only path for the 25-year customs data is rejected, however large the gain.

### Exercises

- **EX081 — Rank.** Rank five remaining BPA items by exposure ÷ effort with stated numbers. Rubric: 3 = method transparent and sensitivity noted.
- **EX082 — Resumption.** Explain how resumption changes the cost of large PQC chains for repeat clients. Rubric: 3 = correct with caveat about resumption and forward secrecy settings.

### Synthesis

System optimization chooses parameters per context, reduces repeated overhead and orders remaining work by exposure reduced per unit effort.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Quantum and post-quantum security: applied research

### Learning outcomes

You will (1) formulate an applied research question from engineering work; (2) design a small study with measurable outcomes; (3) read and assess PQC research critically; and (4) contribute findings back to the community responsibly. It builds on Chapters 29, 36 and 38.

### 42.1 Questions from practice

Engineering raises research-worthy questions: how often do middleboxes mishandle large ClientHellos in a given sector? What is the real time-to-replace for different architectures? How accurate are inventory tools against adjudicated ground truth? The [master's](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) and [doctoral](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) books in this area develop such studies in depth.

### 42.2 Small studies

Define question, population, measurements, comparison and analysis before collecting data; use synthetic or authorized data; report intervals and limits. An engineering thesis (Chapter 49) can include one such study.

### 42.3 Reading research

Check what a paper's numbers measure (configured or negotiated? lab or field?), whether baselines are fair, whether code and data are available, and how old the results are — the field moves quickly, and results about draft algorithms may not apply to final standards.

### 42.4 Contributing back

Report interoperability bugs to implementers, publish anonymized aggregate findings, contribute test vectors, and participate in standards discussions. Coordinate disclosure of vulnerabilities.

### 42.5 Worked example

BPA's engineers ask whether their passive telemetry under-counts hybrid negotiation because of TLS 1.3 encrypted extensions. A small study compares server-log and wire-capture determinations on 1,000 synthetic sessions in the lab and finds agreement on the key-exchange group (visible in clear in ServerHello) but not on certificate algorithms (encrypted) — an applied finding that changes the measurement design.

### 42.6 Common errors and limits

- Studies designed after data collection.
- Applying draft-algorithm results to final standards.
- Publishing identifiable organizational data.

### Engineering note

Applied studies must respect the same authorization and minimization rules as operations. Use synthetic data or data from systems you are authorized to study, minimize identifiers at collection, get approval from the data owner before publishing aggregates, and route any product weakness through coordinated disclosure. These constraints rarely weaken an engineering study; they usually sharpen its question to what the organization actually needs to know.

### Exercises

- **EX083 — Question.** Write an applied research question from your own engineering context with measurement plan. Rubric: 3 = measurable and bounded.
- **EX084 — Paper check.** Apply the 42.3 checklist to a PQC performance paper of your choice. Rubric: 3 = each check answered with evidence.

### Synthesis

Applied research grows from engineering questions, uses small pre-planned studies, reads literature critically and contributes back responsibly.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a real-shaped migration team under supervision; (2) apply professional practices — change control, documentation, stakeholder communication; (3) reflect on gaps between theory and practice; and (4) produce a placement report without disclosing confidential information. It begins the practice and capstone stage.

### 43.1 The placement

A placement in a security team, a vendor, a public agency or a standards organization exposes the realities of migration: procurement cycles, legacy systems, partner politics, change freezes. In this book the placement is simulated at BPA; in a real programme, the host's confidentiality rules apply.

### 43.2 Professional practice

Follow change control: every cryptographic change has a ticket, risk assessment, test evidence, approval and rollback plan. Document decisions with rationale. Communicate progress in the host's language — risk and service impact rather than algorithm names.

### 43.3 Theory versus practice

Common surprises: inventory is harder than algorithm selection; vendors' "PQC-ready" claims vary from roadmaps to shipping features; partners set the pace; the hardest problems are organizational. Record these as reflective notes.

### 43.4 Confidentiality

The placement report describes methods and lessons without identifying systems, vulnerabilities or partners. Use synthetic examples where needed and get host approval before submission.

### 43.5 Worked example

A placement student at BPA (synthetic) builds the passive-telemetry dashboard. Lessons recorded: one TLS library logged only the "first offered" group, not the negotiated one — the dashboard was wrong until fixed; vendor declarations for appliances took eight weeks to obtain; the change board required a rollback rehearsal before approving hybrid TLS on the partner API.

### 43.6 Common errors and limits

- Bypassing change control "because it's only configuration".
- Reports that disclose host vulnerabilities.
- Treating vendor roadmaps as shipped capability.

### Engineering note

Placements also teach how decisions are actually made. Observe who approves cryptographic changes, what evidence they ask for, which risks they accept and which they escalate. Record these observations without names. Students who understand the decision path write better designs in Capstone I, because they anticipate the questions of the change board, the procurement office and partner managers instead of discovering them at the end.

### Exercises

- **EX085 — Change ticket.** Write a change ticket for enabling hybrid TLS on one internal service. Rubric: 3 = risk, tests, approval, rollback.
- **EX086 — Reflection.** Write a 300-word reflection on one theory-practice gap. Rubric: 3 = specific, analytic, confidential.

### Synthesis

Practice teaches that migration is organizational as much as technical; change control, documentation and confidentiality are professional obligations.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) scope a capstone migration project; (2) produce requirements, architecture and plan; (3) build a first increment; and (4) present progress with evidence. It integrates Chapters 20–43.

### 44.1 Capstone brief

Migrate BPA's partner-facing ecosystem — edge TLS, partner VPNs, bills-of-lading signatures and customs exports — to quantum-resistant key establishment and a defined path for signatures, with crypto-agility and measurement, within an 18-month programme. Capstone I covers scoping through a first increment; Capstone II (Chapter 46) completes and validates.

### 44.2 Deliverables for Capstone I

1. Scope statement and stakeholder map.
2. Requirements with traceability (Chapter 21).
3. Asset-flow model and CBOM baseline (Chapters 22, 29).
4. Threat and FMEA analysis (Chapter 23).
5. Architecture with alternatives and decisions (Chapters 25–27).
6. First increment: hybrid TLS on the partner API in a test environment with measurement.
7. Plan for Capstone II with risks.

### 44.3 Assessment

Assessors look for traceability from requirements to design to tests, honest unknowns in the CBOM, a working increment with evidence, and a plan whose dependencies are visible.

### 44.4 Worked example

A model Capstone I submission identifies 37 exposed long-lived flows, chooses hybrid key exchange everywhere external, defers public certificate migration with rationale, demonstrates the partner-API increment with 0 failures in 20,000 lab connections (95% upper bound 1.5 × 10^-4) and lists HSM procurement as the critical path.

### 44.5 Common errors and limits

- Scope too broad to deliver an increment.
- No baseline measurement.
- Plans without dependencies.

### Engineering note

Keep a decision log from the first day of the capstone. Each entry records the date, decision, alternatives considered, evidence and who agreed. The log feeds the architecture chapter of the thesis, answers reviewers' "why" questions quickly and protects the team when a later discovery makes an earlier decision look wrong — it shows what was known at the time. Examiners consistently rate capstones with clear decision logs higher than those with polished but unexplained designs.


### 44.6 Agreeing the capstone baseline

Capstone I begins by recording BPA's starting state: which links use hybrid key exchange, which certificates chain to classical roots, and which inventory entries are still unverified. Progress in Capstone II is measured against this baseline, so later claims of improvement can be checked by the assessor.

### Exercises

- **EX087 — Scope.** Write the capstone scope statement with in/out of scope. Rubric: 3 = deliverable increment, explicit exclusions.
- **EX088 — Increment evidence.** Define the evidence package for the first increment. Rubric: 3 = configuration, tests, measurements, traceability.

### Synthesis

Capstone I proves that the student can scope, model, design and deliver a first measured increment of a real-shaped migration.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) conduct and receive an independent design review; (2) use a structured review checklist for PQC designs; (3) classify findings by severity; and (4) respond with changes or justified acceptance. It examines Capstone I before Capstone II.

### 45.1 Review method

Reviewers independent of the design team read the requirements, architecture, threat analysis and evidence, then interview the team. Findings are written, classified (critical, major, minor, observation) and answered.

### 45.2 PQC review checklist

- Are all public-key uses inventoried, with unknowns reported?
- Are algorithms and parameter sets from current standards (FIPS 203/204/205, SP 800-208) and are draft-era implementations excluded?
- Are hybrid combiners standard and context-bound?
- Is negotiation authenticated and fallback logged and dated?
- Are stateful signature keys protected against reuse?
- Are long-lived trust anchors algorithm-diverse?
- Is agility demonstrated (time-to-replace), not just claimed?
- Are availability risks (size, middleboxes, devices) tested?
- Are residual risks stated honestly?

### 45.3 Severity

Critical: a design flaw that defeats the security goal (e.g. XOR combiner without binding, stateful keys in software with backups). Major: significant gap (no fallback monitoring). Minor: documentation or clarity. Observations: suggestions.

### 45.4 Worked example

Review of the model Capstone I: one major finding — customs exports would use ML-KEM only, with no traditional component and no interoperability evidence from the agency; response: add parallel RSA-OAEP recipient during transition and schedule agency test. One minor — CBOM evidence source missing for 40 records; fixed.

### 45.5 Common errors and limits

- Reviews by the design team itself.
- Findings without severity or response.
- Defensive responses instead of changes or reasoned acceptance.

### Engineering note

Reviewers should also check what the design team measured against what it claimed. Sample three metrics from the team's dashboard and recompute them from raw evidence; disagreements reveal definition drift or pipeline bugs. A review that only reads documents can miss that the "negotiated" metric is in fact computed from offered groups — exactly the kind of error that makes a programme look further ahead than it is.

### Exercises

- **EX089 — Review.** Review a peer's (or the model) design with the checklist and write three findings with severity. Rubric: 3 = specific, actionable, correctly classified.
- **EX090 — Response.** Write a response to a major finding accepting risk with justification. Rubric: 3 = risk owner, rationale, review date.

### Synthesis

Independent review with a PQC-specific checklist and severity classification catches design flaws before they become deployments.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) complete the capstone implementation across domains; (2) execute verification and validation; (3) demonstrate agility; and (4) prepare evidence for the dossier. It follows the review of Chapter 45.

### 46.1 Scope of Capstone II

Complete hybrid key exchange on edge and partner VPNs (or interim PSK where appliances lack support), dual-signed bills of lading with timestamps, dual-recipient customs exports, CBOM coverage ≥ 95% with unknowns reported, and an agility demonstration.

### 46.2 Verification and validation

Run Verification Laboratories I and II test suites against the completed system; collect partner acceptance; produce the residual-risk statement. Address every review finding with evidence.

### 46.3 Agility demonstration

Demonstrate replacing one algorithm through policy within the target time — for example, switching the edge's preferred hybrid group from X25519MLKEM768 to SecP256r1MLKEM768 for a compliance scenario, then back, measuring time-to-replace and confirming telemetry follows.

### 46.4 Worked example

Model results: edge hybrid share 71%; VPNs — 9 of 14 partners with ML-KEM additional key exchange, 5 with PSK mixing; bills of lading dual-signed since month 14; exports dual-recipient, agency acceptance pending; CBOM coverage 96%, unknown 4%; agility demonstration: policy change to full negotiation in 3 days.

### 46.5 Common errors and limits

- Claiming completion with unresolved review findings.
- Agility demonstrated only on a test bench.
- Residual risk omitted.

### Engineering note

Capstone II is also the moment to rehearse handover. Write the operations runbook, the CBOM maintenance procedure and the agility procedure as if a different team will run the system tomorrow, then ask a peer who did not work on the project to perform one routine task — rotating a fallback expiry, adding a partner, changing the preferred group — using only the documents. Every question they ask marks a gap to close before the dossier is assembled.


### 46.6 Handing the capstone to operations

The Capstone II package goes to BPA's operations team with the configuration changes, the test evidence, the rollback steps and a list of what remains classical and why. An operations engineer replays the agility demonstration without the student present; only when that replay succeeds does the capstone count as transferable rather than a one-person result, and any step that needed the student's help is rewritten.

### Exercises

- **EX091 — Agility demo plan.** Write the agility demonstration plan with success criteria. Rubric: 3 = start/end events, telemetry evidence, rollback.
- **EX092 — Findings closure.** Produce a findings-closure table for Chapter 45's review. Rubric: 3 = each finding with evidence of closure or accepted risk.

### Synthesis

Capstone II completes the migration increment by increment, verifies and validates it, demonstrates agility and closes review findings with evidence.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) design and run a controlled failure trial; (2) recover from cryptographic failures within objectives; (3) measure recovery time; and (4) improve plans from results. It tests the resilience designed in Chapter 33.

### 47.1 Trial scenarios

In an isolated replica environment: (a) PQC library vulnerability requiring emergency patch and re-key; (b) LMS signing HSM restored from backup — confirm refusal to sign until state is reconciled; (c) simulated algorithm break: disable ML-DSA in policy and switch bills-of-lading signing to the alternative; (d) middlebox update that drops large ClientHellos at one site.

### 47.2 Objectives

Define recovery time objectives: e.g. patch and re-key edge within 72 hours; switch signature algorithm within 14 days; path-specific exception for middlebox within 2 hours. Measure actual times.

### 47.3 Running the trial

Brief participants; inject faults; observe without helping; record times, decisions and problems; stop if safety or production is at risk (it should not be — replica only).

### 47.4 Worked example

Model trial results: (a) 41 hours; (b) HSM refused, but the runbook lacked reconciliation steps — added; (c) 19 days, exceeding objective because partner verifiers needed updates — partner test endpoints added to the plan; (d) 35 minutes.

### 47.5 Common errors and limits

- Trials on production.
- Objectives set after the trial.
- No follow-up actions.

### Engineering note

Trials should vary who is on duty. A recovery that works only when the system's designer is present is not a recovery capability; run at least one scenario with the on-call team alone and the designers observing silently. Measure not only elapsed time but also decision quality: whether the team consulted the CBOM, followed the runbook and communicated with partners at the right moments. Those observations drive the most valuable improvements.


### 47.6 Following up the trial findings

Each gap found in the trial becomes a tracked action: the missing reconciliation steps in the runbook, the partner test endpoints and the slower-than-planned 19-day partner rollout. The trial is repeated for the scenarios that failed their objective, and the repeat results are added to the evidence dossier beside the originals, so readers can see both the failure and the correction.

### Exercises

- **EX093 — Scenario design.** Design scenario (c) in detail with injects and observers. Rubric: 3 = realistic, measurable, isolated.
- **EX094 — After-action.** Write the after-action report for scenario (c). Rubric: 3 = root cause, actions, owners, dates.

### Synthesis

Failure trials measure real recovery capability against objectives and turn surprises into plan improvements.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble an evidence dossier for the migrated system; (2) link evidence to requirements and claims; (3) protect sensitive evidence; and (4) make the dossier reviewable by auditors and successors. It prepares the thesis and defense.

### 48.1 Contents

Requirements and traceability matrix; architecture and decision records; CBOM snapshots with method; threat and FMEA analyses; test reports (KATs, interoperability, downgrade, state); measurement data (negotiated groups, failures, latency); validation and acceptance records; failure-trial reports; residual-risk statement; agility demonstration results.

### 48.2 Linking claims to evidence

Every claim in summaries has an evidence identifier. "Edge connections negotiating hybrid groups: 71% (EV-MEAS-14, 30-day window, passive telemetry)". Unlinked claims are removed.

### 48.3 Protecting evidence

Evidence can reveal weaknesses. Classify dossier parts; share sensitive parts (vulnerability details, network maps) only with authorized reviewers; publish only sanitized summaries.

### 48.4 Reviewability

Use a consistent structure, index and version control. A successor should find in minutes where ML-DSA keys live and how to replace them.

### 48.5 Worked example

BPA's dossier index lists 126 evidence items. An auditor samples ten claims and traces each to evidence in under an hour; one claim — "all firmware dual-signed" — is found to apply only to devices with the new bootloader; the claim is corrected to "all images dual-signed; 40% of devices verify both".

### 48.6 Common errors and limits

- Claims without evidence identifiers.
- Dossiers with sensitive details shared broadly.
- Evidence scattered across personal folders.

### Engineering note

Dossiers also need a maintenance owner. Evidence ages: measurements become stale, standards statuses change, partners upgrade. Assign an owner, a review frequency and an expiry date to each evidence item, so that the dossier remains a truthful description of the system rather than a snapshot of the week it was submitted. Auditors trust dossiers that show their own update history.


### 48.7 Keeping the dossier current

BPA's dossier is versioned: each update states what changed, why and who approved it. When a standard is revised or a vendor ships a new post-quantum option, the affected claims are re-checked and their evidence refreshed, and stale items are marked rather than silently removed.

### Exercises

- **EX095 — Index.** Draft the dossier index structure. Rubric: 3 = categories, identifiers, classification.
- **EX096 — Claim audit.** Audit five claims from Chapter 46's results against evidence needs. Rubric: 3 = each linked or corrected.

### Synthesis

An evidence dossier links every claim to protected, indexed evidence that auditors and successors can navigate.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis that documents the design, implementation and validation; (2) present results with uncertainty and limits; (3) generalize lessons responsibly; and (4) meet academic integrity standards. It synthesizes the capstone.

### 49.1 Structure

Introduction (problem, stakeholders, contribution); background (quantum threat, standards, hybrids, agility); requirements; design and alternatives; implementation; verification and validation; operations and failure trial; discussion (lessons, generalization, limits); conclusion and future work. Optionally include an applied study (Chapter 42).

### 49.2 Results and limits

Report measured results with windows and intervals; state residual risks; describe limits with direction (e.g. "passive telemetry cannot see certificate algorithms in TLS 1.3, so certificate migration status is from configuration only").

### 49.3 Generalization

Lessons that generalize: inventory first; hybrid key exchange early; authentication by trust-anchor lifetime; agility measured; partners set pace. Lessons that may not: specific failure rates, vendor behaviours, BPA's dependency structure.

### 49.4 Integrity

Cite standards and research accurately; distinguish your work from team work; label synthetic data; do not disclose host confidential information.

### 49.5 Worked example

A model thesis abstract: "This thesis designs and validates a quantum-resistant migration for a synthetic port authority's partner ecosystem. Hybrid X25519MLKEM768 key exchange reached 71% of edge connections without exceeding the failure budget; partner VPNs used ML-KEM additional exchanges or interim pre-shared-key mixing; bills of lading were dual-signed with ML-DSA-65 and ECDSA with timestamp renewal; a policy-driven design replaced a KEM in three days. Certificates on the public portal remain classical; residual risks and generalizable lessons are discussed."

### 49.6 Common errors and limits

- Overgeneralizing from one organization.
- Omitting residual risks.
- Unlabelled synthetic data.

### Engineering note

Write the thesis so that a practitioner at another organization can reuse it. Include the requirement templates, the CBOM schema, the policy allow-list format and the test plans as appendices, with synthetic examples. Reusable artefacts multiply the value of the work and are often what examiners and employers remember. Keep confidential details out, and label every number that comes from the synthetic BPA case.

### Exercises

- **EX097 — Abstract.** Write your thesis abstract (200 words). Rubric: 3 = problem, method, results with numbers, limits.
- **EX098 — Generalization table.** Separate ten lessons into "likely general" and "context-specific". Rubric: 3 = justified classification.

### Synthesis

The thesis records a validated design with honest results and limits and separates general lessons from local ones.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) present and defend the engineering thesis; (2) answer technical, ethical and management questions; (3) demonstrate the system or its evidence; and (4) set a forward plan for the system's next cryptographic change. It completes the course.

### 50.1 Presentation

Twenty minutes: problem and stakes; requirements; architecture and key decisions; results with evidence; failures and recovery; residual risk; what you would do differently. Use diagrams with text alternatives.

### 50.2 Likely questions

- Why hybrid rather than pure PQC? (Hedge against cryptanalytic surprise; cite Rainbow/SIKE; cost accepted.)
- Why are portal certificates still classical? (Active quantum attacks need a CRQC at connection time; ecosystem support and size; plan and trigger for change.)
- How do you know fallback is not a downgrade path? (Transcript authentication; logged, dated fallback; lab downgrade test.)
- What happens if ML-KEM is broken? (X25519 still protects against classical attackers; agility path to an alternative such as HQC once standardized; measured time-to-replace.)
- What would you do with twice the budget? (Prioritize by exposure ÷ effort.)

### 50.3 Demonstration

Show the dashboard, a policy-driven algorithm change in the replica environment and the dossier tracing for one claim.

### 50.4 Forward plan

Agility is the legacy: schedule re-verification of standards (FN-DSA, HQC, revised IR 8547), annual algorithm-break tabletops, CBOM refresh automation and partner reviews.

### 50.5 Common errors and limits

- Claiming the organization is "quantum-safe".
- No answer for algorithm compromise.
- Demonstrations that depend on production systems.

### Engineering note

After the defense, hand the system to its owners with a short letter that states what was achieved, what remains, the dates of upcoming expiries and reviews, and how to reach the people who know the design. Quantum readiness depends on continuity more than on any single engineer, so the final act of the course is to make sure the capability survives the end of the project and the next algorithm change finds a prepared team.

### Exercises

- **EX099 — Defense answers.** Write answers to the five questions in 50.2 for your own capstone. Rubric: 3 = evidence-based, bounded.
- **EX100 — Forward plan.** Write the two-year forward plan for BPA's cryptography after the capstone. Rubric: 3 = re-verification, tabletops, inventory, partner milestones.

### Synthesis

The defense shows a validated, measured and agile migration, answers hard questions with evidence and leaves a plan for the next change — because quantum readiness is a capability, not a finish line.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Numbers about BPA are synthetic.

**EX001.** log₂(10^30) = 30 × 3.32 ≈ 99.7 → about 100 bits. log₂(2^100 × 10^6) = 100 + 19.9 ≈ 120 bits.

**EX002.** Shor's algorithm would reduce breaking RSA from an infeasible sub-exponential effort to a polynomial one — a qualitative collapse — so RSA must be replaced. Grover only square-roots the search for an AES key: AES-256 would still need about 2^128 sequential steps, which remains far out of reach. Replace RSA and elliptic curves; keep AES-256.

**EX003.** (2 + *x*)(3 + *x*³) = 6 + 3*x* + 2*x*³ + *x*⁴ = 6 + 3*x* + 2*x*³ − 1 = 5 + 3*x* + 2*x*³ → [5, 3, 0, 2], matching Lab R's `mul`.

**EX004.** SLH-DSA: second-preimage/collision-type resistance of its internal hashes (the standard relies on specific tweakable-hash properties); file manifest: second-preimage resistance (an attacker substitutes a file); password storage: preimage resistance plus deliberate slowness (use a password-hashing function, not a bare hash).

**EX005.** 1,400 × 1.3 = 1,820 logical qubits × 1,000 = 1.82 million physical qubits — under assumed error rates and code distance; different assumptions change the overhead by large factors.

**EX006.** What are the two-qubit gate error rates? How many logical (error-corrected) qubits can run, and for how long? What circuit depth or runtime is achievable for a target algorithm?

**EX007.** `str(b"abc")` is the text "b'abc'", so its UTF-8 encoding is six bytes different from the three bytes `abc`; the bug class is type confusion between text and bytes, which silently produces wrong digests and interoperability failures.

**EX008.** A function iterating `h = sha256(h + entry).digest()` from a fixed 32-byte zero start; the test modifies one entry and asserts with `hmac.compare_digest` that the final hash differs.

**EX009.** "FIPS 203 was published in 2024" = fact; "quantum computers will break RSA by 2030" = assumption presented as fact; "our appliance migrates in a day" = estimate; "buy now" = recommendation. Borderline cases need source checks.

**EX010.** "We will use the middle-strength version of the new standard encryption method. It gives a strong safety margin for decades, keeps messages small enough for our network, and is what browsers already use. The strongest version is reserved for links where national-security rules require it."

**EX011.** (2/0.1823)(*e*^(0.1823×4) − 1) = 10.97 × (2.074 − 1) ≈ 11.8 TB.

**EX012.** ML-KEM-512 (800 B) fits 900 B; if category 3 is required, change the budget (e.g. accept two segments, adjust the transport) rather than silently downgrade to category 1.

**EX013.** 3/*n* ≤ 10^-5 → *n* ≥ 300,000 failure-free trials.

**EX014.** 10^10 × 2^-30 ≈ 9.3 expected failures per year — rare per operation, routine per year; design for detection and recovery.

**EX015.** The branch timing reveals whether the secret coefficient exceeds *q*/2; replace with a constant-time mask computation (e.g. compute a mask from the sign of `q//2 - x` via arithmetic shift and select with bitwise operations).

**EX016.** ML-DSA-44 verify: larger code, 1,312-byte key, no state; LMS verify: hash-only, very small code, small key; signing state stays at the signing HSM (SP 800-208). Both can fit; LMS is smaller, ML-DSA avoids state management at the signer.

**EX017.** `generate_keypair() -> (public, secret)`, `encapsulate(public) -> (ciphertext, shared_secret)`, `decapsulate(secret, ciphertext) -> shared_secret`, plus `algorithm_id` and `sizes()` queried from the implementation, never hard-coded by callers.

**EX018.** `if len(ek) != 1184: raise ValueError(...)`; never pad or truncate; then call the library, which also performs FIPS 203's modulus check.

**EX019.** Customs declarants (commercial secrets; represented indirectly by the customs agency), employees (HR data; represented by works council/HR), shipping partners (commercial terms; represented by contracts). Gap: data subjects are rarely in the room when budgets are set.

**EX020.** The letter thanks the vendor, explains that BPA uses only algorithms standardized after public review (FIPS 203/204/205, SP 800-208), cites the Rainbow and SIKE breaks as reasons unvetted designs cannot be accepted, and invites a quote for a standards-based product.

**EX021.** 540 + 32 + 4 = 576 B → one segment; 540 + 1,216 + 4 = 1,760 B → two segments.

**EX022.** TLS: both (key exchange first). IKEv2: mainly key exchange (authentication later). SSH: both (key exchange deployed first). DNSSEC: signatures.

**EX023.** System library (package queries), bundled/statically linked libraries (binary scanning), runtime provider configuration (config analysis), HSM/TPM-held keys (PKCS#11/device inventory).

**EX024.** Devices live 10–20 years and verify firmware offline; a signature scheme forgeable within the lifetime lets an attacker install malicious firmware; bootloaders are hard to update, so the trust anchor must be chosen early.

**EX025.** Container status feed (days), terminal operational logs (1 year), bills of lading (12 years integrity), customs declarations (25 years confidentiality), HR records (decades), security camera footage (weeks–months). Longer lifetimes first.

**EX026.** The RSA-OAEP key wrap; replace with a KEM recipient (ML-KEM via CMS KEMRecipientInfo, RFC 9629), optionally alongside RSA during transition.

**EX027.** Algorithm from policy; parameter set approved; lengths validated; constant-time comparisons; library pinned and final-standard; KATs pass; interoperability tests; fallback logged; rollback plan; CBOM updated.

**EX028.** Asset id, endpoint, protocol/version, key-exchange groups offered and negotiated, signature algorithm, certificate issuer/expiry/key algorithm, library and version, key storage location, owner, evidence source, last observed.

**EX029.** Portal: category 3 (ML-KEM-768 in X25519MLKEM768), balancing margin and size; national-security partner: category 5 (ML-KEM-1024, ML-DSA-87) as CNSA 2.0 requires.

**EX030.** VPN traffic: harvest-now-decrypt-later; firmware signatures: future forgery against long-lived roots; bills of lading: forgery of archived signatures.

**EX031.** E.g. "Shipping-line VPN — IKEv2 ECDH P-384 → IKEv2 + ML-KEM-768 (RFC 9370) — owner BPA network + partner — target Q3 next year"; similar rows for customs export, edge TLS, firmware signing, HSM.

**EX032.** Weights set first (security 0.35, availability 0.25, standards 0.15, partner readiness 0.15, cost 0.10); scores per option; sensitivity check shows whether the winner changes when availability weight rises.

**EX033.** Leading: CBOM coverage, vendor PQC commitments, test-environment readiness. Lagging: negotiated hybrid share, dual-signed document share, unknown-asset share trend. Each with an owner.

**EX034.** Promote when upper bound ≤ baseline + budget; hold when between budget and 2× budget; roll back the affected path only when the lower bound exceeds 2× budget — different thresholds prevent oscillation.

**EX035.** Internet→portal: TLS key exchange X25519, cert RSA; BPA→shipping line: IKEv2 ECDH, cert ECDSA; terminal→cranes: firmware RSA signatures; BPA→customs: RSA-OAEP file encryption.

**EX036.** For: one place to enable hybrids and monitor negotiation, fast agility. Against: single point of failure and concentration of keys; mitigate with redundancy and HSM-backed keys.

**EX037.** Each signature reveals one of two secrets per digest bit; two messages whose digests differ at position *i* reveal both secrets there; with both secrets known at many positions, an attacker can assemble signatures for other digests that use only revealed values.

**EX038.** (a) ML-DSA (general purpose, ecosystem support); (b) LMS/XMSS if the signing HSM manages state (small verifier) or ML-DSA otherwise; (c) SLH-DSA for maximum conservatism given low signing frequency, or ML-DSA-87 if size matters.

**EX039.** Customs (x=25, y=2 → late for all z ≤ 27); partner VPN (x=10, y=1.5 → late if z ≤ 11.5); firmware (x=15, y=3 → late if z ≤ 18); portal (x=1, y=0.5 → not late); telemetry (x≈0.1 → not late).

**EX040.** Must state FIPS 203/204/205 final (August 2024), SP 800-208, SP 800-227 final (September 2025), HQC selected (IR 8545, March 2025) with standard pending, FN-DSA pending, IR 8547 draft.

**EX041.** "REQ-VPN-01: All IKEv2 tunnels to partners shall perform an additional ML-KEM-768 (or stronger) key exchange per RFC 9370 when the peer supports it, otherwise PSK mixing per RFC 8784 until a dated sunset. Verification: gateway logs show negotiated exchanges for 100% of tunnels."

**EX042.** Five requirements each with source (data lifetime, policy, partner contract) and method (test, inspection, demonstration, analysis).

**EX043.** CryptoUse{asset_id: str, function: enum[key-exchange, signature, encryption, hash, unknown], algorithm: str, parameter_set: str|None, protocol: str|None, library: str|None, evidence_source: enum[code, config, passive, vendor, endpoint-log], last_observed: datetime}.

**EX044.** `for flow in flows: if flow.lifetime is None or flow.kex is None: report(flow, "unknown"); elif flow.lifetime >= T and flow.kex in VULNERABLE and flow.recordable: report(flow, "exposed")`.

**EX045.** Harvest (mitigate: PQ key exchange/PSK), future forgery (short-lived auth, migrate later), downgrade (authenticated negotiation, no silent fallback), implementation attacks (vetted constant-time libraries, patching), cryptanalytic surprise (hybrid, agility).

**EX046.** Cause: middlebox reads only the first segment; effect: connection resets, outages on one path; detection: path-level failure telemetry and packet traces; mitigation: firmware update, path exception with expiry; priority: high.

**EX047.** With ±150 about 1,880/2,000 bits decrypt correctly; with ±300 only about 1,272/2,000: the sum of ~32 errors grows with error size until it often exceeds *q*/4 ≈ 832, so rounding fails. Real schemes choose noise so the failure probability is negligible.

**EX048.** "When a ciphertext arrives, ML-KEM decrypts it, re-encrypts the result and compares. If they differ, it returns a pseudo-random key derived from a secret, rather than an error. An attacker sending crafted ciphertexts learns nothing from success or failure — provided the comparison and selection take the same time either way."

**EX049.** Diagram of clients, CDN, edge proxy, inspection proxy, APIs with text alternative; alternatives (hybrid now vs wait for native vendor support); weights fixed before scoring.

**EX050.** TLS 1.3 signs the handshake transcript, so stripping hybrid groups is detected unless authentication is broken; the residual risk is application-level retry logic that falls back after any error — logged, restricted to known incompatibility errors and dated for removal.

**EX051.** Hybrid requires breaking both X25519 and ML-KEM-768; Rainbow and SIKE show new schemes can fall unexpectedly; the cost is ~2.3 kB per handshake and some middlebox risk, acceptable for the portal.

**EX052.** Generate per-peer 256-bit PSKs, distribute out of band, mix via RFC 8784, rotate every 90 days with overlap, retire when the appliance is replaced (dated).

**EX053.** Hashing only the PQ secret discards the classical hedge: if ML-KEM were broken, the session would fall too. Use the standard concatenation combiner with transcript binding.

**EX054.** Edge: X25519MLKEM768, SecP256r1MLKEM768; fallback X25519 until a stated date. Internal: hybrid where libraries support it; classical allowed for telemetry until a stated date. National-security link: ML-KEM-1024 only.

**EX055.** Implements final FIPS 203/204/205 (not drafts); constant-time with evidence; passes KATs; active maintenance and advisories; CMVP validation where required; clear licence; interoperability record.

**EX056.** Separate LMS keys per site (or partitioned HSS subtrees), HSM-enforced monotonic counters, no state restore from backup, alerts at 50%/80%, documented rollover.

**EX057.** Add `("vpn-2", "key-exchange", "IKEv2 ML-KEM-768 + ECDH", "config")`; change the hybrid test to `"ML-KEM" in alg or "MLKEM" in alg`.

**EX058.** Coverage = assets with ≥ 1 determination ÷ assets in register, monthly, all sources. Negotiated hybrid share = connections negotiating PQ/T groups ÷ connections, 30-day window, passive telemetry, by service and data class.

**EX059.** Wrong-length ciphertext; ciphertext with one flipped bit (expect implicit-rejection key, no error leak); decapsulation key that fails hash check; encapsulation key failing modulus check; repeated decapsulation of the same input returns the same key.

**EX060.** Signers (HSM A, HSM B) × verifiers (BPA, three partner systems, customs) × formats (dual-signed document) with expected verify results including negative cases.

**EX061.** Division of a secret by a constant may compile to variable-time instructions on some platforms; use Barrett-style multiplication by a precomputed reciprocal and shifts.

**EX062.** A glitch that skips the verification check; countermeasures: verify twice via different code paths and check a hash of the loaded image after boot.

**EX063.** Fallback only to X25519; log reason; alert above threshold; permission expires on a date; never fall back on authentication failure.

**EX064.** 15 × 60 × 24 × 365 ≈ 7.9 million signatures per year > 1,048,576 — insufficient; use multi-level HSS with more capacity, several keys, or ML-DSA for this volume.

**EX065.** Lab → spare unit (2 weeks) → one low-impact crane (2 weeks) → one terminal → all; rollback image verified with the old key at each ring.

**EX066.** CBOM identifies ML-DSA-65 in bills of lading; alternative: ECDSA remains valid short-term plus switch to SLH-DSA or another ML-DSA level; timestamp renewal; target 14 days; partner verifier updates as dependency.

**EX067.** HSM → PKI → document signing and firmware signing; partner readiness → VPN and documents; customs readiness → exports; edge TLS largely independent.

**EX068.** Notice lists supported groups (X25519MLKEM768), test endpoint, timeline, sunset of classical-only VPN proposals, contact.

**EX069.** Two signature fields (ECDSA, ML-DSA-65), timestamp tokens, policy: either valid until a date, both required after; archive timestamp renewal schedule.

**EX070.** Diversity means compromise of one algorithm does not strand devices; costs: bootloader code size and dual signing per image.

**EX071.** 1 × (1,312 + 2,420 + 400) + 2,420 = 6,552 bytes.

**EX072.** Measure p50/p95/p99 handshake latency for classical vs hybrid vs PQ certificates over the satellite path, ≥ 1,000 handshakes per condition, same time windows.

**EX073.** Upper bound for 30/50,000 ≈ 0.00086 ≤ 0.0009 → PROMOTE (barely); a cautious team might extend observation.

**EX074.** Check recent changes, break down fallback by client and path, compare with vendor advisories, apply path exception if local, escalate to security if fallback has no incompatibility reason.

**EX075.** Lists classical certificates on portal (review annually), 5 PSK-mixed VPNs (replacement next budget), devices with single-key bootloaders (refresh dates), unknown assets 6% (owners named).

**EX076.** External vantage point capturing a random sample of 2,000 handshakes per week; compare negotiated share with internal telemetry; investigate differences > 2 points.

**EX077.** Add `"hmac-sha512"` to the registry and a `RETIRE = {"hmac-sha256": date(...)}` check in `check` that rejects after the date.

**EX078.** Start: policy change merged; end: ≥ 99% of offering clients negotiate the new group; evidence: telemetry time series and change ticket.

**EX079.** Isolated lab with MITM proxy; strip hybrid groups; expect handshake failure or logged, policy-permitted retry; fail if silent classical-only connection occurs where policy forbids.

**EX080.** Restore HSM backup → signing refused until reconciliation; 100 concurrent requests → all indices unique; exhaust test tree → clean refusal and alert.

**EX081.** E.g. legacy VPN (exposure 9, effort 3 → 3.0), customs exports (8, 2 → 4.0), vessel links (4, 2 → 2.0), internal DB replication (6, 1 → 6.0), telemetry (1, 1 → 1.0): order replication, exports, VPN, vessel, telemetry.

**EX082.** Resumption skips certificate transmission for repeat clients, removing most PQ chain bytes; keep resumption with (EC)DHE/hybrid key exchange to retain forward secrecy.

**EX083.** E.g. "In our 300 services, what share of hybrid-capable clients fall back to classical groups, and why?" with telemetry window and categories.

**EX084.** Answers each check: measured quantity, baseline, availability of code/data, date and algorithm versions.

**EX085.** Ticket: service, change (enable X25519MLKEM768), risk (middlebox), tests (interop matrix), approval, rollback (policy revert), monitoring.

**EX086.** A 300-word analytic reflection on, e.g., the gap between "PQC-ready" marketing and shipped features.

**EX087.** In scope: partner API hybrid TLS increment, CBOM baseline, requirements, architecture; out: public certificates, internal telemetry, device refresh.

**EX088.** Configuration files, interop results, 20,000-connection lab measurement with bound, traceability links, rollback test.

**EX089.** Findings such as "fallback not dated (major)", "CBOM evidence source missing (minor)", "single-key bootloader (critical for long-lived devices)".

**EX090.** Accept classical portal certificates: risk owner CISO, rationale (no active quantum attack possible today; ecosystem), review annually or on trigger.

**EX091.** Switch preferred group by policy, measure until 99% negotiation, confirm telemetry and rollback; success if within 7 days with no failure-budget breach.

**EX092.** Table of findings with closure evidence (exports dual-recipient, CBOM sources added) or accepted risks with owners.

**EX093.** Inject: "practical attack on ML-DSA-65 published"; observers time CBOM query, decision, policy change, partner notices; isolated replica only.

**EX094.** Root cause of 19-day switch: partner verifiers; actions: partner test endpoints, pre-agreed alternative algorithm, owners and dates.

**EX095.** Sections: requirements, design, inventory, tests, measurements, validation, trials, risk; IDs EV-REQ-nn etc.; classification per item.

**EX096.** "71% hybrid" → EV-MEAS; "9 of 14 partners" → EV-VAL; "3-day agility" → EV-AGIL; "all firmware dual-signed" → corrected to images vs devices; "CBOM 96%" → EV-INV.

**EX097.** A 200-word abstract with problem, method, numeric results and limits, e.g. as in 49.5.

**EX098.** General: inventory first, hybrids early, trust-anchor diversity, measured agility, partner pacing. Specific: failure rates, vendor timelines, BPA dependency graph, latency numbers, PSK choices.

**EX099.** Evidence-based answers to the 50.2 questions citing the dossier.

**EX100.** Year 1: re-verify FN-DSA/HQC/IR 8547 status, CBOM automation, tabletop; year 2: portal certificate decision, remaining VPN replacements, partner milestones, second tabletop.

<a id="references"></a>

## References

Links checked 12 October 2026; standards status changes, so re-verify.

- Beullens, W. (2022). Breaking Rainbow takes a weekend on a laptop. IACR ePrint 2022/214. <https://eprint.iacr.org/2022/214>
- Bernstein, D. J., et al. (2024). KyberSlash. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- Castryck, W., and Decru, T. (2022). An efficient key recovery attack on SIDH. IACR ePrint 2022/975. <https://eprint.iacr.org/2022/975>
- Chromium Blog (2023). Protecting Chrome Traffic with Hybrid Kyber KEM. <https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html>
- Gidney, C. (2025). How to factor 2048 bit RSA integers with less than a million noisy qubits. arXiv:2505.15917. <https://arxiv.org/abs/2505.15917>
- Gidney, C., and Ekerå, M. (2021). *Quantum* 5, 433. <https://doi.org/10.22331/q-2021-04-15-433>
- Grover, L. K. (1996). A fast quantum mechanical algorithm for database search. *STOC '96*. <https://doi.org/10.1145/237814.237866>
- IANA. TLS Supported Groups registry. <https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml>
- IETF RFCs: 8446 (TLS 1.3), 8554 (LMS), 8391 (XMSS), 8555 (ACME), 8701 (GREASE), 8784 (IKEv2 PSK mixing), 8879 (certificate compression), 9370 (multiple key exchanges in IKEv2), 9629 (KEMs in CMS), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NCCoE. Migration to Post-Quantum Cryptography project. <https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025); SP 800-56C Rev. 2. <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227> · <https://doi.org/10.6028/NIST.SP.800-56Cr2>
- NIST IR 8545 (2025); IR 8547 initial public draft (2024); CSWP 39 upd1 (2026). <https://doi.org/10.6028/NIST.IR.8545> · <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- NSA. Quantum Key Distribution (QKD) and Quantum Cryptography (QC). <https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/>
- Regev, O. (2009). *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
