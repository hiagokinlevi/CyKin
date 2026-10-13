# Quantum and Post-Quantum Security: Foundations for Defensible Decisions

- Language: English (`en`); bachelor's course, four years; approximately 3,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–40 of 40 have authored teaching text; exercises EX001–EX080 (two per chapter) have matching worked results; offline labs use the Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: broad security and computing students who need durable foundations — mathematics, systems, networks, cryptographic concepts, evidence and ethics — and then a careful first study of the quantum threat and post-quantum cryptography (PQC). Entry knowledge: school-leaving mathematics, basic computing and written communication.
- Relation to neighbouring books: the [engineering book](../../../../engineering-5-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) designs and builds migrations; the [master's](../../../../masters-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) and [doctoral](../../../../doctorate-2-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) books study them empirically. **This book builds the foundations and the habit of comparing alternatives with explicit assumptions and evidence.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited degree. No authority to test real systems. All organizations, people and numbers in examples are **synthetic** unless a sentence cites a public source. Toy cryptography in the labs is deliberately insecure; real systems must use vetted implementations of [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204), [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) and [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208).

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Forty chapters run over four years: general foundations (1–18), the quantum and post-quantum core (19–32) and research, project and capstone work (33–40). Each chapter has learning outcomes, teaching, a worked example, a practical activity, common errors, two exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs run offline with Python 3; the printed output is shown so you can check your run.

### The running case: Harbourline Credit Union

**Harbourline Credit Union (HCU)** is a synthetic member-owned financial cooperative with 40 branches. It runs a core banking system, a mobile app, card terminals and ATMs, branch-to-data-centre VPNs, an internal certificate authority, and an archive of mortgage documents that must remain confidential and verifiable for 30 years. Its board asks a simple question — "what does quantum computing mean for us?" — and the book answers it step by step. Every number about HCU is invented.

### Source policy

Primary sources were checked on 12 October 2026: NIST FIPS 203/204/205 (August 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (initial public draft)](https://doi.org/10.6028/NIST.IR.8547.ipd), [CSWP 39 upd1](https://doi.org/10.6028/NIST.CSWP.39-upd1), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) and [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). FN-DSA (FIPS 206) and the HQC standard were still in development. Re-verify status before relying on it.

## Contents

| Stage | Chapters |
|---|---|
| Foundations | [1 Mathematical reasoning](#ch-01) · [2 Computing systems](#ch-02) · [3 Programming I](#ch-03) · [4 Academic writing](#ch-04) · [5 Security literacy](#ch-05) · [6 Discrete structures](#ch-06) · [7 Networks and protocols](#ch-07) · [8 Programming II](#ch-08) · [9 Data and databases](#ch-09) · [10 Ethics and authorized practice](#ch-10) · [11 Operating systems](#ch-11) · [12 Probability and statistics](#ch-12) · [13 Identity and access](#ch-13) · [14 Privacy foundations](#ch-14) · [15 Evidence and measurement](#ch-15) · [16 Security architecture](#ch-16) · [17 Cryptography concepts](#ch-17) · [18 Research methods I](#ch-18) |
| Quantum and PQC core | [19 Scope and theory](#ch-19) · [20 Foundational cases](#ch-20) · [21 System models](#ch-21) · [22 Data and dependencies](#ch-22) · [23 Methods I](#ch-23) · [24 Controls](#ch-24) · [25 Laboratory I](#ch-25) · [26 Methods II](#ch-26) · [27 Verification](#ch-27) · [28 Failure analysis](#ch-28) · [29 Operations](#ch-29) · [30 Laboratory II](#ch-30) · [31 Advanced cases](#ch-31) · [32 Interdisciplinary interfaces](#ch-32) |
| Research and capstone | [33 Research methods II](#ch-33) · [34 Comparative project](#ch-34) · [35 Capstone proposal](#ch-35) · [36 Field or community practice](#ch-36) · [37 Evidence review seminar](#ch-37) · [38 Capstone implementation](#ch-38) · [39 Capstone evaluation](#ch-39) · [40 Thesis and presentation](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) read and write a short proof by direct argument, contradiction and induction; (2) compare growth rates using logarithms and big-O notation; (3) explain why "how fast does the attack cost grow?" is the central question in cryptography; and (4) distinguish a mathematical claim from an empirical estimate. The chapter prepares discrete structures (Chapter 6) and probability (Chapter 12).

### 1.1 Why security students need proofs

A security claim is a statement about *every* attacker within a model, not about the attackers we happened to test. Testing a lock with ten picks shows it resisted ten picks; it does not show it resists the eleventh. Mathematics is the only tool that lets us make "for all" statements, and it does so by stating assumptions precisely. When a standard says a scheme is secure "if the Module-LWE problem is hard", that sentence is a conditional theorem: the conclusion is only as strong as the assumption, and the assumption is supported by decades of failed attacks rather than by proof. Learning to separate the proved part from the assumed part is the most useful mathematical habit in this book.

Three proof shapes recur. A *direct proof* chains true statements to the conclusion. A *proof by contradiction* assumes the opposite and derives something impossible; Euclid's proof that there are infinitely many primes is the classic example and underpins why RSA moduli can be chosen freely. *Induction* proves a base case and a step from *n* to *n*+1; it is how we reason about loops, hash chains and the counters inside stateful signatures.

### 1.2 Growth rates

Cryptographers measure security in bits: a "128-bit" problem needs about 2^128 basic operations. Logarithms convert between scales: log₂(10^30) ≈ 100, so 10^30 operations is about 2^100. Big-O notation keeps only the dominant term: an algorithm doing 3*n*³ + 50*n* steps is O(*n*³). The quantum threat is, at heart, a change in growth rate. Classically, the best known factoring algorithm grows *sub-exponentially* in the bit length of the number; Shor's algorithm (Shor, 1997) grows *polynomially*, roughly like *n*³ logical operations. For brute-force key search, Grover's algorithm (Grover, 1996) only reduces 2^*k* trials to about 2^(*k*/2) sequential iterations. One change is a collapse; the other is a square root that longer keys absorb.

### 1.3 Worked example

HCU's IT manager reads a headline saying quantum computers will "break all encryption". Using growth rates, we sort HCU's cryptography. RSA-2048 and elliptic-curve keys protect logins and VPN key exchange: a polynomial-time attack exists on a large fault-tolerant quantum computer, so these must be replaced. AES-256 encrypts the database: Grover leaves roughly 2^128 sequential work, still far beyond reach, so it stays. The headline is wrong in its scope, and the correction comes from a comparison of growth, not from an opinion.

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

Read the output as a table of growth rates, not as predicted run times: the numbers ignore constants, error correction and hardware speed, which Chapter 19 treats as explicit assumptions.

Two contrasts stand out. For symmetric keys, Grover's search halves the exponent, so a 256-bit key still leaves a very large problem. For RSA, the gap is far wider: the classical cost grows faster than any polynomial in the key size, while Shor's cost grows only as the cube of it. Doubling the key from 1024 to 2048 bits adds a lot of classical work but only a few bits of quantum work. That difference is why RSA must be replaced rather than lengthened.

### 1.5 Common errors and limits

- Treating "secure if problem X is hard" as an unconditional proof.
- Comparing operation counts across machines as if a quantum gate and a classical instruction cost the same.
- Reading the heuristic factoring estimates as exact; they are order-of-magnitude guides.

Each error comes from forgetting what the calculation leaves out. Security proofs are conditional, so the condition must be stated beside the result. Operation counts compare growth, not wall-clock time, since a single error-corrected quantum operation may take far longer than a classical one. Heuristic estimates are useful for deciding which algorithms are in danger, not for predicting a date. A careful student writes the assumption next to every number.

### Exercises

- **EX001 — Bits of work.** Express 10^24 operations and 10^24 × 2^20 operations in bits of work. Rubric: 3 = both correct with the logarithm shown.
- **EX002 — Proof shape.** Prove by induction that a hash chain of length *n* built as h₁ = H(s), h_{k+1} = H(h_k) requires exactly *n* hash evaluations. Rubric: 3 = base case, step and conclusion stated.

### Synthesis

Security arguments combine proved implications with assumed hard problems. The quantum threat is a change in growth rate: polynomial-time Shor collapses factoring and discrete logarithms, while Grover only halves the exponent of key search.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the layers of a computing system from hardware to application; (2) explain where cryptographic code and keys live in each layer; (3) contrast classical bits with qubits at a conceptual level; and (4) map one HCU service onto these layers.

### 2.1 Layers and where cryptography sits

A modern service is a stack. At the bottom are processors, memory, storage and network interfaces; above them firmware boots the machine, an operating system manages resources, libraries provide shared functions, and applications deliver features. Cryptography appears in almost every layer. Firmware verifies signatures on the next boot stage. The operating system stores keys and offers a cryptographic provider. Libraries such as TLS stacks negotiate algorithms with remote peers. Applications sign documents or encrypt fields. Hardware security modules (HSMs) and smart cards are small computers whose whole purpose is to keep keys inside a boundary.

This layering matters for migration. Replacing an algorithm in an application is a software release; replacing it in a card terminal's boot ROM may require replacing the device. Students who can locate each cryptographic use in the stack can estimate how hard it will be to change, and that estimate drives every later plan in this book.

### 2.2 Bits, qubits and what quantum computers are

A classical bit is 0 or 1. A qubit's state is described by two complex amplitudes; measuring it yields 0 or 1 with probabilities given by those amplitudes. Several qubits can be *entangled*, so their joint state is not a list of independent bits. Quantum algorithms arrange interference so that wrong answers cancel and right answers reinforce. That is a narrow capability: quantum computers are not faster general-purpose machines, and for most workloads — databases, web servers, spreadsheets — they offer nothing. Their security relevance comes from a few algorithms, above all Shor's period finding.

Today's devices are noisy. Running Shor against RSA-2048 needs *error-corrected logical qubits*, each built from many physical qubits. Public estimates have fallen over time — Gidney (2025) estimated under a million noisy qubits running for less than a week under stated hardware assumptions — but no such machine exists, and its arrival date is uncertain.

### 2.3 Worked example

Map HCU's mobile banking login. The phone's secure enclave holds a device key (hardware); the phone OS provides a keystore (operating system); the app's TLS library negotiates key exchange with the server (library); the server's load balancer terminates TLS using a certificate from HCU's CA (infrastructure); the core banking application checks a signed session token (application). Five layers, at least four quantum-relevant algorithms, three different owners.

Five layers each hold a key or a check, and each could need a different change in a migration. The device key and the TLS key exchange are both quantum-vulnerable if they use elliptic curves. The session token's signature may be checked only on the server, which is easier to change. Mapping the login this way shows the HCU team that the app is not one cryptographic decision but several, owned by different people.

### 2.4 Practical activity

Choose a device you own. List its layers and, for each, one cryptographic function you believe it performs. Mark each belief as *observed* (you saw configuration or documentation) or *assumed*. Keep the list; Chapter 22 turns such lists into an inventory.

Most students find more assumed entries than observed ones, especially in firmware and hardware. That gap is the point of the exercise: an organisation's knowledge of its own cryptography is usually incomplete, and the first job of a migration is to find out what is really there. Note where you would look to confirm each assumption, such as a settings screen or a vendor's documentation.

### 2.5 Common errors and limits

- Assuming "quantum computer" means a faster laptop.
- Forgetting firmware and hardware when listing cryptography.
- Quoting a qubit count without the error rate and run time it assumes.

A quantum computer is a different kind of machine that is faster only for certain problems; for most tasks it offers no advantage. Firmware and hardware are often missed because nobody configures them day to day, yet they verify signatures and hold keys. A qubit count alone says little, since useful algorithms need error-corrected qubits and long run times, and published estimates make those assumptions explicit.

### Exercises

- **EX003 — Layer map.** Map HCU's ATM withdrawal across at least four layers and name one cryptographic function in each. Rubric: 3 = four correct layers with plausible functions and owners.
- **EX004 — Myth check.** Explain in three sentences why a quantum computer would not speed up HCU's monthly statement batch job. Rubric: 3 = refers to narrow algorithmic advantage and to the workload type.

### Synthesis

Cryptography is spread across every layer of a system, and the layer determines how hard it is to change. Quantum computers are specialised machines whose security impact comes from a few algorithms, and their arrival depends on error correction at scale.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write small Python programs with functions, loops and conditionals; (2) handle text and bytes correctly; (3) use the standard library's `hashlib` and `secrets` modules; and (4) test a function with assertions.

### 3.1 Programs as precise statements

A program is an argument a machine can check by running it. Security work uses programs to reproduce claims: if a report says "this configuration offers only classical key exchange", a short script that parses the configuration and prints the groups makes the claim repeatable. Throughout this book labs are short Python programs using only the standard library, so that every reader can run them offline and compare output.

Start with the core constructs: variables hold values; functions name a reusable computation; `for` loops repeat; `if` statements choose. Readable programs use descriptive names, small functions and comments that explain *why*, not *what*.

### 3.2 Text versus bytes

Cryptographic functions operate on bytes, not text. In Python, `"abc"` is text (a sequence of Unicode characters) and `b"abc"` is bytes. Converting text to bytes requires an encoding, normally UTF-8: `"abc".encode("utf-8")`. A classic bug is hashing `str(b"abc")`, which is the six-character text `b'abc'`, not the three bytes. The digest is silently wrong, and two systems that disagree on encoding will fail to verify each other's signatures. Interoperability problems in post-quantum deployments are often of this kind: wrong byte order, wrong encoding, wrong length.

### 3.3 Randomness and hashing in the standard library

`secrets.token_bytes(32)` returns 32 bytes from the operating system's cryptographically secure generator; the `random` module is *not* suitable for keys because its output is predictable from its seed. `hashlib.sha256(data).hexdigest()` computes a SHA-256 digest; `hashlib.sha3_256` and `hashlib.shake_128` compute members of the SHA-3 family used inside ML-KEM and ML-DSA. To compare secret values use `hmac.compare_digest`, which takes time independent of where the inputs differ.

Known-answer tests use published inputs and outputs, so a wrong implementation fails at once. The SHA-3 family is useful in this book because ML-KEM and ML-DSA use it internally. Never print secret bytes while debugging; print their length or a digest instead.

### 3.4 Worked example

An HCU intern writes a function to fingerprint certificates:

```python
import hashlib
def fingerprint(der: bytes) -> str:
    return hashlib.sha256(der).hexdigest()
assert fingerprint(b"") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
print("fingerprint test passed")
```

The assertion uses the published digest of the empty string as a known answer. If someone later changes the function to hash text, the test fails immediately.

The test checks the function against an outside fact, not against its own output, which is what makes it able to fail. A second test with a real certificate's bytes and its published fingerprint would catch a different mistake, such as hashing a text encoding of the certificate instead of its raw bytes. The intern adds both tests to HCU's repository so that every later change is checked automatically.

### 3.5 Practical activity

Write `is_valid_length(alg, data)` that returns `True` only if `data` has the length expected for that algorithm, using a dictionary such as `{"ML-KEM-768-ek": 1184}` (the encapsulation-key size in FIPS 203). Test one correct and two incorrect inputs.

A length check is not a security check; it only catches gross errors such as truncated or concatenated values. It is still worth having, because many integration bugs in post-quantum migrations come from buffers sized for classical keys. Take the expected sizes from the standard itself rather than from a blog post, and note the document and table you used, so a reviewer can verify each number.

### 3.6 Common errors and limits

- Using `random` for keys or nonces.
- Mixing text and bytes, or printing secrets in logs while debugging.
- Writing tests that cannot fail (asserting a value against itself).

Each mistake produces code that seems to work. A key from the random module looks random but can be predicted by anyone who learns the seed. A digest of the wrong bytes looks like a digest and fails only when compared with another system. A test that compares a value with itself always passes, so it gives false confidence. Logging secrets leaves them in files that more people can read than the program itself.

### Exercises

- **EX005 — Encoding bug.** Explain why `hashlib.sha256(str(b"abc").encode())` differs from `hashlib.sha256(b"abc")`, and name the class of bug. Rubric: 3 = correct explanation and bug class.
- **EX006 — Known-answer test.** Write a function that returns the SHA3-256 hex digest of its input and a test using the empty-string digest `a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a`. Rubric: 3 = runs, test can fail if the function is wrong.

### Synthesis

Small, tested programs make security claims reproducible. Bytes, encodings and secure randomness are where beginners' cryptographic code most often goes wrong.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) structure an argument as claim, evidence and reasoning; (2) cite primary sources accurately, including their status; (3) write about uncertainty without overstating or hiding it; and (4) adapt one finding for a technical and a non-technical reader.

### 4.1 Claim, evidence, reasoning

Every paragraph in a security report should let the reader find three things: what you claim, what evidence supports it and why the evidence supports the claim. "HCU's VPN is quantum-vulnerable" is a claim. "The VPN configuration exported on 3 March negotiates only ECDH group 19" is evidence. "ECDH is broken by Shor's algorithm on a cryptographically relevant quantum computer, so recorded VPN traffic could be decrypted later" is reasoning. When one of the three is missing, readers either distrust a correct finding or accept an unsupported one.

### 4.2 Citing standards and their status

Cryptographic writing depends on standards whose status changes. Cite the document precisely — "NIST FIPS 203, *Module-Lattice-Based Key-Encapsulation Mechanism Standard*, August 2024" — with a persistent link such as its DOI. State the status when it matters: FIPS 203, 204 and 205 are final standards; [NIST IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) was an initial public draft on 12 October 2026, so its proposed transition dates are proposals, not rules; FN-DSA was still in development. Prefer primary sources over news articles, and check that the source actually says what you attribute to it. Many errors in migration reports come from quoting a secondary summary of a draft as if it were a final requirement.

### 4.3 Writing about uncertainty

Nobody knows when a cryptographically relevant quantum computer will exist. Good writing turns that uncertainty into explicit assumptions: "If such a machine exists within 15 years, records with a 30-year confidentiality requirement are already exposed to harvest-now-decrypt-later collection." Avoid both false precision ("in 2031") and dismissal ("decades away, ignore it"). Use ranges, state who made an estimate and when, and show how your recommendation changes across the range.

Two-part statements of this kind let the reader replace your assumption with their own and still use your reasoning. Say who made each estimate you cite and when.

### 4.4 Worked example

A draft sentence reads: "Quantum computers will break our encryption by 2030, so NIST requires us to switch to Kyber immediately." Rewritten: "Public estimates of when a quantum computer could break RSA-2048 vary widely and none is authoritative. NIST published ML-KEM, derived from CRYSTALS-Kyber, as FIPS 203 in 2024, and its draft IR 8547 proposes deprecating quantum-vulnerable algorithms after 2030 and disallowing them after 2035. Because our mortgage archive must stay confidential for 30 years, we recommend starting key-exchange migration for archive transfers this year." Each claim is now sourced, dated and qualified.

### 4.5 Practical activity

Take a one-page news article about quantum computing. Mark every factual claim, find its primary source if one exists, and rewrite the article's main conclusion in three sentences that respect the evidence.

Most news articles mix accurate facts with claims that have no source or that overstate one. Writing your three sentences forces you to decide what the evidence actually supports. Compare your version with a classmate's: if they differ, check whether one of you relied on a claim the other could not source. Keep the primary sources you found, as you will reuse them in later chapters.

### 4.6 Common errors and limits

- Citing a vendor blog for a standard's content.
- Presenting a draft's proposed dates as mandatory.
- Writing "quantum-proof" or "unbreakable"; prefer "designed to resist known quantum attacks".

A vendor blog may describe a standard accurately, but it may also mix in product claims or an earlier draft. Cite the standard itself. Draft documents propose dates for comment; they are not requirements until published in final form. Absolute words such as unbreakable promise more than any cryptographer can deliver, and readers who later learn of an attack will distrust everything else in the report.

### Exercises

- **EX007 — Claim, evidence, reasoning.** Write a three-sentence finding that HCU's internal CA uses RSA-2048 and why that matters. Label each sentence C, E or R. Rubric: 3 = all three present and accurate.
- **EX008 — Status discipline.** Correct this sentence: "FIPS 206 requires Falcon for all signatures from 2025." Rubric: 3 = notes FIPS 206 was in development, names FN-DSA, removes the false requirement.

### Synthesis

Clear security writing separates claim, evidence and reasoning, cites primary sources with their status and turns uncertainty into stated assumptions.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) define confidentiality, integrity, availability and authenticity; (2) relate assets, threats, vulnerabilities and controls; (3) explain "harvest now, decrypt later" and "forge later" as threat patterns; and (4) read a simple risk statement critically.

### 5.1 Core properties

*Confidentiality* means only authorized parties can read information; *integrity* means unauthorized changes are detected or prevented; *availability* means authorized users can use the service when needed; *authenticity* means we can tell who produced a message. Cryptography mainly serves confidentiality (encryption, key exchange), integrity and authenticity (message authentication codes and signatures). Availability is easy to forget in cryptographic changes: a migration that makes handshakes fail is an availability incident even if it improves confidentiality.

In HCU's case, a gateway that rejects members' older phones after a change of algorithm would be a security failure even if no data leaked.

### 5.2 Assets, threats, vulnerabilities, controls

An *asset* is something of value — member data, the ability to approve payments. A *threat* is a potential cause of harm, usually an actor with a capability and motive. A *vulnerability* is a weakness the threat can exploit. A *control* reduces likelihood or impact. Risk is the combination of likelihood and impact for a scenario linking these elements. In quantum security the vulnerability is often not a bug but a mathematical property of an algorithm that becomes exploitable once a new capability exists.

### 5.3 Two quantum threat patterns

*Harvest now, decrypt later* (HNDL): an adversary records encrypted traffic today and stores it until a quantum computer can recover the key exchange. The harm happens in the future, but the collection — and therefore the need to act — is now, for any data whose confidentiality must outlast the arrival of such a machine. *Forge later*: once a quantum computer exists, an adversary can derive private signing keys from public keys and forge signatures, firmware updates or certificates. Unlike HNDL, forgery needs the machine at the time of attack, so signature migration can follow a different timetable — except where signatures must remain trustworthy for many years, such as mortgage documents or devices that cannot be updated.

### 5.4 Worked example

HCU risk statement, draft: "Risk of quantum attack: high." Improved: "Asset: mortgage archive transfers between branches and the data centre (confidentiality required 30 years). Threat: a well-resourced adversary recording WAN traffic. Vulnerability: VPN key exchange uses ECDH only. Impact if realized: disclosure of member financial histories. Likelihood: collection plausible now; decryption depends on an uncertain future capability. Control options: hybrid post-quantum key exchange, reduced data in transit." The improved statement supports a decision; the draft does not.

The improved version names each element of the risk separately, so readers can disagree with one part without rejecting the whole. It also shows why the risk is urgent despite the uncertain date: collection can happen today. A reviewer can check each part against evidence, such as the VPN configuration or the archive's retention policy.

### 5.5 Practical activity

Write risk statements in the improved format for two HCU assets: card authorization messages and the mobile app's code-signing key. Note how their time horizons differ.

Card authorization messages need confidentiality only for a short time, so harvest now, decrypt later matters little there; the concern is authentication. The code-signing key matters for as long as old app versions are trusted, which makes forge-later the main concern. Writing both statements in the same format makes these differences visible, and the comparison helps decide which asset to migrate first.

### 5.6 Common errors and limits

- Treating every cryptographic use as equally urgent.
- Ignoring availability when changing algorithms.
- Confusing a threat (actor) with a vulnerability (weakness).

Urgency depends on how long data must stay confidential and how long signatures must be trusted. Treating every use as equally urgent spreads effort thinly and delays the cases that matter most. Ignoring availability can turn a security improvement into an outage that members notice. Confusing threats with vulnerabilities leads to controls aimed at the wrong thing, such as trying to stop an adversary rather than removing the weakness they would exploit.

### Exercises

- **EX009 — Pattern sorting.** Classify each as HNDL, forge-later or neither: archived VPN traffic, firmware signing for ATMs, AES-256 database encryption, TLS session to the mobile app. Rubric: 3 = all four correct with one-line reasons.
- **EX010 — Risk statement.** Rewrite "PKI is at quantum risk" as a full risk statement for HCU's internal CA. Rubric: 3 = asset, threat, vulnerability, impact, likelihood and controls present.

### Synthesis

Security properties, risk elements and two time-shaped threat patterns — harvest-now-decrypt-later and forge-later — give a vocabulary precise enough to rank quantum risks.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) compute with modular arithmetic; (2) explain groups and why hidden periods matter; (3) multiply polynomials in the ring Z_q[x]/(x^n+1); and (4) connect these structures to RSA, elliptic curves and ML-KEM.

### 6.1 Modular arithmetic and groups

Working modulo *q* keeps numbers in {0, …, *q*−1}: 15 mod 7 = 1. A *group* is a set with an operation that is associative, has an identity and inverses. The non-zero numbers modulo a prime *p* form a group under multiplication; the points of an elliptic curve form a group under point addition. Repeating the operation from a starting element *g* eventually cycles: *g*, *g*², *g*³, … returns to 1 after *r* steps, where *r* is the *order* of *g*. Finding *r* — a hidden period — is hard classically for large groups, and RSA, Diffie–Hellman and elliptic-curve cryptography all rest on problems equivalent to or reducible to finding such periods or discrete logarithms. Shor's algorithm finds periods efficiently on a quantum computer, which is why all of these fall together.

### 6.2 Polynomial rings

A polynomial ring Z_q[*x*]/(*x*^*n*+1) contains polynomials of degree below *n* with coefficients modulo *q*. To multiply, multiply normally, then replace *x*^*n* by −1. ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)) uses *n* = 256 and *q* = 3329; ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) uses *n* = 256 and *q* = 8380417. Vectors of these polynomials form *modules*, hence "module lattice". The ring is chosen for compactness and fast multiplication; security comes from adding small random noise, a topic of Chapter 23. No efficient quantum period-finding attack is known against these noisy problems.

### 6.3 Practical activity — Lab R

```python
# Lab R (ch 6): multiplication in R_q = Z_q[x]/(x^n + 1), the ring behind ML-KEM (there n=256, q=3329).
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

Check by hand: (1 + 2*x* + 3*x*³)·*x* = *x* + 2*x*² + 3*x*⁴ = −3 + *x* + 2*x*² ≡ 14 + *x* + 2*x*² (mod 17).

The lab multiplies two small polynomials in a ring with toy parameters and prints the result. Doing one product by hand, as shown, is the best way to see where the sign flip happens. Real parameters are far larger, but the rule is the same, and the libraries you will use apply it with much faster algorithms. The toy ring is not secure; it exists only to make the arithmetic visible.

### 6.4 Worked example

An HCU developer asks why their post-quantum library "multiplies polynomials" when RSA "exponentiates numbers". RSA works in the multiplicative group modulo *N*, where a hidden period exists and Shor can find it. ML-KEM works with noisy linear algebra over polynomial rings, where no such period structure is known to help. The arithmetic looks different because the hard problem is different.

The developer's question is a good one to answer before any migration work, because it explains why the new algorithms need new review skills. Code that handles polynomials and noise has different failure modes from code that handles large integers, such as mistakes in reduction or in sampling the noise.

### 6.5 Common errors and limits

- Forgetting the sign flip when reducing *x*^*n* to −1.
- Believing the ring structure alone provides security; without noise the equations are easy to solve.
- Assuming "no known attack" means "proved secure".

The sign flip is the most common hand-calculation mistake, and tests with known answers catch it. The second error matters more: the ring makes the arithmetic convenient, but the security comes from the added noise. Without it, the equations are ordinary linear algebra and easy to solve. No known attack is a statement about current knowledge, so standards include security margins and are reviewed as research continues.

### Exercises

- **EX011 — Order of an element.** Find the order of 3 modulo 7 by listing powers. Rubric: 3 = correct order with the list.
- **EX012 — Ring product.** Compute (2 + *x*)(3 + *x*³) in Z_17[*x*]/(*x*⁴+1) and check with Lab R. Rubric: 3 = correct coefficients with the reduction shown.

### Synthesis

Classical public-key cryptography hides periods in groups, which Shor's algorithm finds. Lattice-based PQC computes in polynomial rings and hides secrets under noise, a structure with no known quantum shortcut.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) describe the TCP/IP layers and where TLS, IPsec and SSH operate; (2) trace a TLS 1.3 handshake and identify key exchange and authentication; (3) explain why post-quantum keys and signatures stress message sizes; and (4) name the IETF documents that define hybrid key exchange.

### 7.1 Layers and secure channels

Data crosses networks in layers: link, internet (IP), transport (TCP, UDP, QUIC) and application. Secure channels insert cryptography at different points. TLS protects application streams such as HTTPS; IPsec with IKEv2 protects IP packets between sites, as in HCU's branch VPNs; SSH protects administrator sessions. Each has two cryptographic jobs: *key establishment*, which agrees a fresh session secret, and *authentication*, which proves who the peer is, usually with certificates and signatures.

The two jobs face different quantum threats. Key establishment matters for harvest now, decrypt later, because recorded traffic can be opened once the session secret is recovered. Authentication matters only at the moment of connection, since a forged signature later cannot change a past handshake.

### 7.2 The TLS 1.3 handshake

In TLS 1.3 ([RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html)) the client sends a ClientHello listing supported groups and a key share; the server answers with a ServerHello holding its key share, then encrypted messages carrying its certificate chain and a CertificateVerify signature. Key establishment and authentication are separate: a hybrid group such as X25519MLKEM768, specified for TLS in [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html), replaces only the key-exchange part. Its client key share is 1,216 bytes and its server share 1,120 bytes, against 32 bytes for X25519 alone. The certificate chain is unchanged until post-quantum certificates are deployed.

### 7.3 Size and middleboxes

Bigger messages matter. A ClientHello above about 1,500 bytes may span two TCP segments; some old firewalls and inspection devices mishandle such messages or unknown group identifiers. Post-quantum signatures are larger still: an ML-DSA-44 signature is 2,420 bytes ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)), versus about 72 for ECDSA P-256. Chapter 30 measures what this does to certificate chains.

Before blaming the new algorithm for a failure, check where the bytes went. A packet capture in a lab shows whether a message was split, dropped or rejected, and by which device.

### 7.4 Worked example

HCU's network team sees a rise in failed connections after enabling a hybrid group on a test web gateway. A packet capture in the lab shows the ClientHello now spans two segments, and a legacy inspection proxy at one branch drops the connection. The fix is not to disable post-quantum key exchange everywhere but to update or bypass that proxy, while recording the issue in the migration log. The diagnosis needed knowledge of both layers: the size came from cryptography, the failure from transport handling.

### 7.5 Practical activity

Using a lab browser and your own test server, or published handshake traces, identify the supported-groups list in a ClientHello and the selected group in the ServerHello. Record which messages are encrypted in TLS 1.3. Do not capture other people's traffic.

Most of the handshake after the ServerHello is encrypted in TLS 1.3, including the certificate, so a passive observer sees less than in older versions. Compare a connection that offers a hybrid group with one that offers only classical groups, and note the difference in ClientHello size. Published traces are a safe alternative if you have no test server of your own. Write down which tool you used and its version, so another student can repeat the observation.

### 7.6 Common errors and limits

- Believing hybrid key exchange also makes authentication post-quantum.
- Blaming the algorithm for failures caused by middleboxes.
- Capturing traffic on networks you are not authorized to monitor.

Hybrid key exchange protects session secrets against later decryption, but the certificate and its signature remain classical until certificates change, which is a separate and slower migration. Middlebox failures are common in early deployments, and diagnosing them needs evidence from the network, not assumptions about the algorithm. Capturing traffic without authority is unlawful in many places and breaks the trust that security work depends on, however good the intention.

### Exercises

- **EX013 — Split the jobs.** For TLS 1.3, IKEv2 and SSH, name the key-establishment and the authentication mechanism in a typical classical deployment. Rubric: 3 = six correct entries.
- **EX014 — Size budget.** How many more bytes does a client send in its key share with X25519MLKEM768 than with X25519 alone? Rubric: 3 = 1,184 bytes with sizes cited.

### Synthesis

Secure protocols separate key establishment from authentication. Hybrid post-quantum key exchange changes the first, enlarges handshakes and can expose old middleboxes; authentication changes later with post-quantum certificates.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) structure larger programs with modules, data classes and error handling; (2) parse structured inputs such as CSV and JSON; (3) write tests for both valid and invalid inputs; and (4) avoid common security mistakes in code that handles keys.

### 8.1 Structure and data

As programs grow, structure keeps them correct. Group related functions in modules, represent records with `dataclasses` so fields are named, and raise exceptions for invalid states instead of returning silently wrong values. The standard library's `csv` and `json` modules parse common formats; validating every field as you read it — type, range, allowed values — stops bad data from propagating. In migration work, inventories arrive as CSV exports from scanners and configuration databases, and most analysis errors begin with an unvalidated column.

### 8.2 Negative testing

A positive test checks that valid input works; a *negative test* checks that invalid input is rejected. Cryptographic code needs both. A decoder for ML-KEM encapsulation keys must accept exactly 800, 1,184 or 1,568 bytes for the three parameter sets in FIPS 203 and reject anything else, and FIPS 203 also specifies input checks on the key's coefficients. Libraries that skipped such checks have historically accepted malformed inputs that leaked information or crashed services. Write the negative tests before you write the decoder.

HCU's tests include keys one byte too short and one byte too long.

### 8.3 Handling secrets in code

Keep secrets out of logs, exception messages and version control. Prefer passing key *handles* (references held by an HSM or OS keystore) instead of raw key bytes. Compare secrets with constant-time functions. Never write your own production implementation of a post-quantum algorithm; use a vetted library, and treat even small wrapper code with suspicion, because side channels and parsing bugs live in the glue as often as in the core.

For HCU, this means calling the approved library through a small interface and reviewing that interface as carefully as anything else.

### 8.4 Worked example

An HCU analyst receives `inventory.csv` with columns `host, protocol, group`. A careless script counts rows where `group == "x25519"` and reports "most hosts classical". A careful version normalises case, rejects rows with empty groups as *unknown* rather than *classical*, and prints three numbers: classical, hybrid and unknown. The careful script reveals that 18 % of synthetic rows are unknown — a fact the first script hid.

Treating unknown as classical would have made the inventory look more complete and more uniformly classical than it was, hiding the hosts whose cryptography nobody knew. Unknowns become a work list of their own: someone must check those hosts directly before the inventory can be trusted. The careful script also records the input file's date, so later readers know how fresh the counts are.

### 8.5 Practical activity

Write a function that reads lines `host,group`, validates that `group` belongs to an allowed set, and returns counts of hybrid, classical and unknown. Include one negative test with an unknown group string.

Normalise case and spaces before comparing, and decide in advance what counts as hybrid. A group name you have never seen should fall into unknown, never into classical by default. Your negative test should show that a misspelt or invented group name is counted as unknown and that the function does not crash on an empty line. Print the three counts in a fixed order so outputs from different runs can be compared.

### 8.6 Common errors and limits

- Treating missing data as a negative finding.
- Catching all exceptions and continuing silently.
- Writing custom cryptography instead of calling a vetted implementation.

Missing data is a finding about the inventory, not about the systems. Swallowing exceptions hides the rows that failed, so the totals look complete when they are not; log each failure with its line number instead. Custom cryptography fails in ways that tests rarely catch, such as timing differences, and vetted libraries have had years of review that a new implementation cannot match.

### Exercises

- **EX015 — Negative tests.** List four negative tests for a function that loads an ML-DSA-65 public key (1,952 bytes in FIPS 204). Rubric: 3 = four distinct, meaningful failure cases.
- **EX016 — Unknown is not no.** Explain in two sentences why counting empty fields as "classical" biases an inventory. Rubric: 3 = identifies bias direction and decision consequence.

### Synthesis

Structured code, validated inputs and negative tests make analysis trustworthy; in cryptographic code, rejecting bad input is as important as handling good input.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) model data with entities, attributes and relationships; (2) write simple SQL queries; (3) attach retention and confidentiality lifetimes to data; and (4) explain how data lifetime drives quantum urgency.

### 9.1 Modelling data

A relational database stores tables of rows. An *entity* (member, account, document) becomes a table; *attributes* become columns; *relationships* become keys linking tables. SQL queries select, filter and join: `SELECT host FROM services WHERE kex_group = 'ECDHE-P256'` returns hosts using a particular group. Sound models make analysis possible: if a migration team stores each cryptographic observation with its source and date, it can later ask which observations are stale.

HCU's inventory table records host, protocol, group, source and observation date for each row. The source column distinguishes a configuration export from a passive capture, which have different reliability.

### 9.2 Data lifetimes

Every data class has a *retention period* (how long it is kept) and a *confidentiality lifetime* (how long disclosure would cause harm). These differ: card authorisation messages are kept seven years for disputes but are mostly harmless after the card expires; mortgage documents are kept and remain sensitive for 30 years. Michele Mosca (2018) framed the quantum consequence: if *x* is the time data must stay secure, *y* the time to migrate and *z* the time until a capable quantum computer, then *x* + *y* > *z* means data is already at risk. Databases are where *x* is recorded, so a data model with lifetime attributes is the first quantitative tool of migration planning.

### 9.3 Encryption at rest

Databases encrypt data at rest with symmetric algorithms such as AES-256, whose keys are wrapped by key-encryption keys. The symmetric layer is not the quantum problem. The problem is how keys travel: if database keys are backed up to another site over a channel using RSA key transport or ECDH, recorded backups may expose them later. Inventory therefore follows keys, not just data.

HCU's backup jobs, for example, copy wrapped keys between data centres over the same VPN that carries the mortgage archive.

### 9.4 Worked example

HCU models `data_class(name, retention_years, confidentiality_years, transfer_channel)`. A query finds classes with `confidentiality_years >= 15 AND transfer_channel = 'vpn-ecdh'`: mortgage documents and member identity records. Those two classes become the first candidates for hybrid key exchange, before the high-volume but short-lived card traffic.

Card traffic is high in volume but loses its value within days, so harvest now, decrypt later matters little for it. Mortgage and identity records keep their value for decades. Ordering migration by confidentiality lifetime, rather than by traffic volume or ease, puts effort where future exposure is greatest. The query result is a starting list for discussion with data owners, who may know of other long-lived classes the table does not yet hold.

### 9.5 Practical activity

Create a five-row table of synthetic HCU data classes with retention, confidentiality lifetime and channel. Write the query above and justify the order of migration it suggests.

Include at least one class whose retention is long but whose confidentiality lifetime is short, such as published annual reports, so the difference is visible. Your justification should explain why each class falls where it does and which assumption would change its place. Compare your ordering with a classmate's and note any class you placed differently, with the reason. Keep the table; later chapters extend it.

### 9.6 Common errors and limits

- Confusing retention with confidentiality lifetime.
- Assuming encryption at rest solves in-transit exposure.
- Recording lifetimes once and never revisiting them after contract or law changes.

Retention is how long a record is kept; confidentiality lifetime is how long its disclosure would cause harm. They often differ. Encryption at rest protects stored copies but says nothing about copies sent over a network. Lifetimes change when laws, contracts or business practices change, so each one needs an owner and a review date, otherwise migration priorities slowly drift away from reality.

### Exercises

- **EX017 — SQL.** Write a query returning data classes whose confidentiality lifetime exceeds 10 years and whose channel uses a quantum-vulnerable key exchange. Rubric: 3 = correct syntax and conditions.
- **EX018 — Lifetimes.** Give plausible retention and confidentiality lifetimes for card authorisations and mortgage files, and explain the difference. Rubric: 3 = reasonable values and justified difference.

### Synthesis

Data models with lifetime attributes turn the quantum question into a query. Keys, not only data, must be followed to find exposure.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) explain why authorization defines legitimate security work; (2) write a scope statement for a cryptographic assessment; (3) handle dual-use knowledge responsibly; and (4) route discovered weaknesses through coordinated disclosure.

### 10.1 Authorization is the boundary

The same action — scanning a server for its supported TLS groups, capturing a handshake, testing whether a device accepts a downgraded algorithm — is professional work when the system owner authorizes it in writing and an offence or a breach of trust when they do not. Authorization must name the systems, the time window, the permitted techniques, the data you may collect and the person to contact if something breaks. Verbal approval from a friendly engineer is not authorization; neither is the fact that a service is reachable from the internet.

### 10.2 Scope for cryptographic work

Cryptographic assessments can look harmless, but they touch sensitive things: certificates reveal internal hostnames, handshake captures may contain metadata, and downgrade tests can break production sessions. A good scope says, for example: "Passive observation of TLS handshakes on the HCU test gateway mirror port, 1–14 May; no payload retention; no active downgrade testing outside the isolated lab; results shared with the HCU security office only." Active experiments that modify negotiation or inject faults belong in isolated testbeds.

A written scope also protects the student: if something breaks, the record shows what was permitted.

### 10.3 Dual use and disclosure

Knowing how to find quantum-vulnerable systems also tells an adversary where to look. Publish aggregate findings rather than lists of named vulnerable hosts. If you find a weakness in a vendor product — for example, a library that accepts malformed ML-KEM keys — report it privately to the vendor, agree a timeline, and publish only after a fix or the agreed deadline. Label all synthetic data clearly so that teaching examples are never mistaken for real findings about real organizations.

HCU's reports on its own migration follow the same rule and describe progress as counts.

### 10.4 Worked example

An HCU student intern notices that a partner bank's public website still offers only classical key exchange and proposes to "scan all partner banks" for a class project. The ethical response: the observation of one public handshake made by a normal browser visit is ordinary, but systematic scanning of partners is outside HCU's authority. The intern instead studies published aggregate measurements and asks HCU's vendor-management team to include post-quantum readiness questions in partner questionnaires.

The response keeps the useful goal, learning how ready partners are, while moving it into a channel where HCU has standing to ask.

### 10.5 Practical activity

Draft a one-page authorization request for a passive TLS inventory of a synthetic HCU test network. Include systems, dates, techniques, data handling, stop conditions and contacts.

Stop conditions say when to halt: for example, if the test network shows unexpected production traffic or a service degrades. Contacts should include someone who can authorise a stop at any hour. Data handling states what is captured, where it is stored and when it is deleted. Ask a classmate to read your request as if they were the system owner and list anything they would refuse to sign.

### 10.6 Common errors and limits

- Treating internet reachability as permission.
- Retaining packet payloads "just in case".
- Publishing named lists of vulnerable systems.

Being able to reach a system is not the same as being allowed to test it; permission comes from its owner in writing. Payloads may contain personal data that the assessment never needed, and keeping them creates risk for no benefit. Named lists help attackers choose targets, so share them only with the people who will fix the systems. Each mistake damages the trust that lets security teams do their work.

### Exercises

- **EX019 — Scope gaps.** Identify three missing elements in: "You may test our crypto next week." Rubric: 3 = three of systems, techniques, data handling, window, contacts, stop conditions.
- **EX020 — Disclosure.** Outline the steps after finding that a vendor's VPN appliance silently falls back to classical key exchange when hybrid is configured. Rubric: 3 = private report, evidence, timeline, coordinated publication.

### Synthesis

Authorization, scoped data handling and coordinated disclosure are what make cryptographic assessment professional. Active downgrade or fault experiments belong only in isolated, authorized testbeds.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) describe processes, memory isolation, file permissions and system services; (2) explain how operating systems provide cryptographic services and key storage; (3) identify OS-level dependencies that control a migration; and (4) reason about update channels and their signatures.

### 11.1 Isolation and privilege

An operating system isolates processes in separate address spaces, enforces file permissions and grants privileges to users and services. Keys stored in a world-readable file defeat all of this; keys held by a privileged service, or by hardware such as a TPM, are reachable only through defined interfaces. Least privilege — giving each component only the access it needs — applies to cryptographic material as much as to files.

HCU's inventory therefore records where each key lives as well as which algorithm it uses.

### 11.2 Cryptographic providers

Applications rarely implement cryptography themselves. They call a *provider*: OpenSSL providers on Linux, the CNG framework on Windows, platform keystores on mobile systems. The provider and its version decide which algorithms an application can use, so a post-quantum migration often begins as an OS or library upgrade. System-wide crypto policies on some Linux distributions set allowed algorithms in one place; this is valuable for agility, because one policy change can enable a hybrid group across many services, and dangerous if changed without testing.

### 11.3 Updates and boot

Operating systems trust signed updates and, through secure boot, signed boot components. These signatures typically use RSA or ECDSA today. Because forge-later attacks target long-lived trust anchors, vendors are planning post-quantum or hash-based signatures for firmware and boot chains; [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) approves the stateful hash-based schemes LMS and XMSS, which suit firmware signing where the signer can manage state carefully. Devices whose boot ROM can verify only RSA cannot be upgraded by software alone.

Such devices need a replacement plan.

### 11.4 Worked example

HCU's branch servers run a Linux distribution whose current OpenSSL version supports the hybrid X25519MLKEM768 group in TLS. The team discovers that the core banking middleware ships its own older, statically linked TLS library and ignores the OS provider. Upgrading the OS changes nothing for that middleware; the vendor must ship a new build. The OS-level view revealed a hidden dependency that a server-by-server checklist would have missed.

The team adds a column to its inventory recording whether each application uses the system library or its own, and asks every vendor for a roadmap.

### 11.5 Practical activity

On a lab virtual machine you control, list the installed cryptographic libraries and their versions, and find where the system crypto policy (if any) is configured. Record which applications link their own copies.

Look for applications that bundle their own TLS library, such as some databases, language runtimes and vendor agents. Their versions may lag the system library by years. Do this only on a machine you control, and do not change the crypto policy during the exercise. Your record becomes a small version of the dependency inventory that HCU builds for its servers, and the same questions apply at scale.

### 11.6 Common errors and limits

- Assuming an OS upgrade migrates every application.
- Editing a system-wide crypto policy directly on production.
- Overlooking boot-chain and update signatures.

Applications that bundle their own libraries do not change when the operating system does. System-wide policy changes can break services in ways that are hard to trace, so test them in a lab and roll them out gradually. Boot and update signatures are easy to overlook because they work silently, yet they protect the most trusted code on the machine and often have the longest migration lead times.

### Exercises

- **EX021 — Provider dependency.** Explain why an application that statically links its TLS library is a separate migration item. Rubric: 3 = dependency, ownership and testing consequences.
- **EX022 — Boot chain.** Why are stateful hash-based signatures suited to firmware signing but risky for a web server? Rubric: 3 = mentions state management, signing volume and recovery.

### Synthesis

Operating systems supply the cryptographic providers, key storage and signed update chains that applications depend on. Migration therefore runs through OS and library layers — and through every component that bypasses them.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) compute probabilities of independent events and expected counts; (2) reason about very small failure probabilities; (3) use confidence intervals for measured rates; and (4) interpret decryption-failure figures in post-quantum schemes.

### 12.1 Rare events at scale

If an event has probability *p* per trial and there are *N* independent trials, the expected number of occurrences is *Np*, and the probability of at least one is 1 − (1 − *p*)^*N* ≈ *Np* when *Np* is small. This simple formula explains why cryptographers demand astronomically small failure probabilities. A 2^−20 failure rate sounds tiny, yet across 10^9 handshakes it predicts about 950 failures. ML-KEM is designed so that honest decapsulation fails with probability below about 2^−138 for ML-KEM-768 per FIPS 203's analysis, so failures are negligible at any realistic scale.

### 12.2 Practical activity — Lab P

```python
# Lab P (ch 12): how small must a failure probability be? Binomial reasoning for rare events.
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

Notice how each 20-bit change in the exponent shifts the expected count by a factor of about a million.

The middle rows show why failure probabilities in standards are so small. A rate that looks negligible for a billion operations may produce hundreds of failures at a million billion, which large services reach over their lifetime. The last rows show a probability so small that failures are not expected at any realistic scale. When a design quotes a failure rate, multiply it by the number of operations you expect before deciding whether it matters.

### 12.3 Measured rates and intervals

Operational data gives counts, not probabilities. If 3 of 5,000 test connections fail, the point estimate is 0.06 %, but the true rate could be higher. A 95 % confidence interval — for example the Wilson interval used in Chapter 29 — expresses that uncertainty. With small samples, the upper bound is what matters for a go/no-go decision: "we are fairly confident the failure rate is below *u*" is the defensible statement.

Report the interval with the count and the sample size, so the reader can judge it.

### 12.4 Base rates

Probability also protects against misleading alarms. If a detector flags handshakes that "look like downgrade attempts" with 99 % sensitivity and 1 % false positives, but real downgrade attempts occur in one handshake per million, then almost every alert is false. Always ask for the base rate before interpreting an alert count.

In this example, a million handshakes would give about ten thousand false alerts and roughly one true one. A team receiving that stream would learn to ignore the alert, which defeats its purpose. Better detectors, or applying the rule only where downgrades are more likely, raise the share of true alerts. HCU asks for these figures before adopting any new detection rule.

### 12.5 Worked example

HCU's mobile app performs 2 × 10^8 key establishments per year. If a hypothetical scheme failed with probability 2^−40, expected failures would be 2 × 10^8 × 9.1 × 10^−13 ≈ 1.8 × 10^−4 per year — negligible. If an implementation bug raised the rate to 1 in 10^5, the expected count would be 2,000 per year, visible in support tickets. Measured failure rates therefore test the implementation, not the mathematics.

HCU's support team was asked to watch for this pattern during the hybrid pilot. A sudden rise in connection errors after a library update would point to the code, since the scheme's own failure rate cannot produce such numbers.

### 12.6 Common errors and limits

- Reading a point estimate from a small sample as the true rate.
- Ignoring base rates when interpreting alerts.
- Assuming independence where failures are correlated (one bad middlebox affects every connection through it).

Small samples can produce a point estimate far from the true rate, especially for rare events; report the interval. Base rates decide whether an alert is likely to be real. Correlated failures, such as many connections passing through one faulty device, break the independence that simple models assume, so failures cluster and averages mislead. Check where failures occur before treating them as independent.

### Exercises

- **EX023 — Expected failures.** With *p* = 2^−30 and 10^12 operations, compute the expected number of failures. Rubric: 3 = ≈ 931 with method shown.
- **EX024 — Base rate.** For the downgrade detector in 12.4, estimate the fraction of alerts that are true among 10^8 handshakes. Rubric: 3 = about 100 true of about 10^6 alerts (≈ 0.01 %), method shown.

### Synthesis

Expected counts, confidence bounds and base rates turn tiny probabilities and noisy operational data into defensible decisions.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) distinguish identification, authentication and authorization; (2) explain how certificates and public-key infrastructure (PKI) bind identities to keys; (3) identify quantum-vulnerable elements in common authentication flows; and (4) plan where post-quantum signatures will be needed first.

### 13.1 Three steps

*Identification* claims an identity; *authentication* proves it; *authorization* decides what the authenticated party may do. Passwords, one-time codes and passkeys authenticate users; certificates and signatures authenticate machines and software. Authorization is usually symmetric bookkeeping — access-control lists and roles — and is not directly threatened by quantum computers. Authentication based on public-key signatures is.

Keeping the three steps apart helps a migration team focus. HCU's role tables and access lists need no change for quantum reasons. Every place where a signature or a public-key login proves identity does, and those places are spread across phones, servers, the certificate authority and software releases. Listing them by step makes the scope of the work clearer.

### 13.2 PKI in brief

A certificate is a signed statement by a certificate authority (CA): "this public key belongs to this name, valid until this date". Verifiers trust a small set of root CAs and follow chains to them. If an adversary can compute a CA's private key from its public key — as Shor's algorithm would allow for RSA and ECDSA — they can issue certificates for any name. Because root keys are long-lived and widely embedded, PKI is the archetypal forge-later target. Post-quantum signature standards provide replacements: ML-DSA in [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) for general use and SLH-DSA in [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) as a conservative hash-based option.

### 13.3 Authentication flows

Passkeys and FIDO authenticators use public-key signatures (often ECDSA) inside a secure element. Single sign-on tokens are signed with RSA or ECDSA. Code-signing certificates protect software updates. Each flow has a different migration path: tokens with short lifetimes can switch quickly once libraries support ML-DSA; hardware authenticators need new devices; root CAs need long planning because relying parties must first trust the new roots.

HCU groups its flows by which of these paths they need. Short-lived tokens come first, the CA last.

### 13.4 Worked example

HCU lists authentication uses: member passkeys (ECDSA in phone hardware), staff SSO tokens (RSA-2048, 10-minute lifetime), internal CA (RSA-4096 root, 20-year validity), mobile app code signing (ECDSA, platform-controlled). The forge-later risk is greatest for the long-lived root and for code signing, where a forged signature would let an adversary distribute malicious software. Short-lived SSO tokens are lower priority: forging one requires a quantum computer at the moment of attack, and the key can rotate quickly once one exists.

The list also shows who controls each change. HCU can change its own tokens and CA; it depends on phone makers and app platforms for passkeys and code signing.

### 13.5 Practical activity

Draw HCU's certificate hierarchy: root, two intermediates, server and client leaves. Annotate each with algorithm, validity and who must trust it. Mark which changes require relying parties to update trust stores.

Relying parties include member phones, branch servers, ATMs and partner banks, each with a different way of updating trust. Some can take a new root in a routine update; others, such as ATMs, may need a vendor visit. Mark those carefully, because they set the pace of the whole certificate migration. Compare your diagram with a classmate's and check that both of you placed the same validity periods on the same certificates.

### 13.6 Common errors and limits

- Treating authorization lists as quantum-vulnerable.
- Planning to migrate leaf certificates before relying parties trust a post-quantum root.
- Forgetting hardware authenticators that cannot be updated.

Access lists and role tables use no public-key mathematics, so quantum computers do not threaten them. Issuing post-quantum leaf certificates before relying parties trust a matching root causes connections to fail. Hardware authenticators with fixed algorithms can only be replaced, which takes budget and years. A plan that ignores them will look complete on paper and stall in practice, when the devices turn out to be in members' pockets.

### Exercises

- **EX025 — Classify.** For passwords, passkeys, SSO tokens and an internal root CA, state whether a quantum computer threatens the mechanism and why. Rubric: 3 = four correct, reasoned entries.
- **EX026 — Order of work.** Explain why a post-quantum root must be distributed to relying parties before post-quantum leaf certificates are useful. Rubric: 3 = chain validation logic stated.

### Synthesis

Quantum computers threaten public-key authentication, not authorization logic. PKI roots and code signing are the long-lived targets; short-lived tokens can follow later.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) state core privacy principles such as purpose limitation and minimization; (2) relate privacy harm to confidentiality lifetime; (3) explain why harvest-now-decrypt-later is a privacy problem; and (4) design data-minimizing measurement for migration work.

### 14.1 Principles

Privacy law and practice share common principles: collect personal data for a stated purpose, collect no more than needed (*minimization*), keep it no longer than needed (*storage limitation*), protect it appropriately, and be transparent. These principles are about people, not systems; a privacy harm is a harm to a member whose data is exposed, even if the organization suffers no loss.

For a quantum migration these principles shape two things: which data most needs protection, and how the migration work itself handles personal information found along the way.

### 14.2 Lifetime of harm

Some personal data stops mattering quickly; other data stays sensitive for a lifetime — health conditions, financial distress, identity documents. Harvest-now-decrypt-later turns long-lived sensitivity into present risk: traffic recorded today can reveal tomorrow what a member disclosed in confidence decades earlier. For privacy, the relevant *x* in Mosca's inequality is the lifetime of the harm to the person, which can exceed the organization's retention period. Deleting a record from HCU's database does not delete a copy an adversary recorded in transit.

### 14.3 Minimization as a quantum control

The cheapest protection for data is not to send it. Reducing what crosses networks — tokenising account numbers, keeping sensitive fields at the data centre and sending only derived results — lowers HNDL exposure regardless of algorithm. Minimization also applies to migration measurement itself: an inventory needs algorithm names and host identifiers, not message contents.

HCU's first review of branch traffic found member names travelling with transactions that needed only an account token. Replacing the names with tokens reduced the exposure at once, before any algorithm changed.

### 14.4 Worked example

HCU's loan application flow sends full applicant profiles from branches to head office, including medical notes for hardship cases. A privacy review finds that underwriters at head office need only a hardship flag and an amount. Changing the form so that medical notes stay in the branch case file reduces both the privacy footprint and the data exposed to future decryption, before any post-quantum algorithm is deployed. Hybrid key exchange on the branch VPN is then scheduled for the remaining flows.

### 14.5 Practical activity

For three synthetic HCU data flows, list the personal data fields, the purpose, and which fields could be removed, tokenised or aggregated before transmission.

Typical candidates are full names sent where an identifier would do, dates of birth sent for checks that only need an age band, and account numbers sent where a token works. For each field you remove, say who would notice and whether any process breaks. Then estimate how much the change reduces the long-lived data crossing the network, which is the exposure harvest now, decrypt later depends on.

### 14.6 Common errors and limits

- Equating retention period with lifetime of harm.
- Collecting full packet captures for an inventory.
- Treating PQC as a substitute for minimization rather than a complement.

The harm from disclosure can last far longer than the record is kept: a deleted mortgage file that was recorded in transit can still be decrypted later. Full captures collect personal data the inventory never needed and create a new store to protect. Post-quantum algorithms protect what is sent; minimization reduces what is sent at all. The two work together, and neither replaces the other.

### Exercises

- **EX027 — Lifetime of harm.** Give two data types whose privacy harm outlasts HCU's retention period and explain the consequence for HNDL. Rubric: 3 = two examples, reasoning linked to recorded traffic.
- **EX028 — Minimize the inventory.** Specify the minimum fields a passive TLS inventory needs and two fields it should not collect. Rubric: 3 = justified lists.

### Synthesis

Privacy harm can last longer than any retention schedule, which makes harvest-now-decrypt-later a privacy issue. Minimization reduces exposure under every algorithm and should precede and accompany PQC.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) define validity, reliability and coverage for security measurements; (2) choose indicators for cryptographic readiness; (3) record provenance for every observation; and (4) present measurements with their blind spots.

### 15.1 What makes a measurement useful

A measurement is *valid* if it measures what it claims, *reliable* if it gives the same result when repeated, and has known *coverage* if we know what share of the population it observes. "Percentage of TLS connections using hybrid key exchange" is valid if counted from ServerHello messages, reliable if the sensor is stable, and its coverage is the share of traffic passing the sensor. Without coverage, a 90 % figure may describe only the easy tenth of the estate.

Coverage is the property most often missing from security dashboards.

### 15.2 Readiness indicators

Useful indicators for a quantum migration include: share of assets with a known cryptographic inventory; share of long-lived data flows protected by hybrid key exchange; share of certificates issued by CAs that can issue post-quantum certificates; number of vendors with a published PQC roadmap; and mean time to change an algorithm by configuration. Each indicator should have an owner, a source and a refresh frequency.

HCU began with three of these and added the others once owners were agreed. Each has a source.

### 15.3 Provenance

Record for every observation: what was observed, by which method (passive network, configuration, code scan, vendor statement), when, and by whom. Methods differ in confidence: an observed handshake is stronger evidence than a vendor's datasheet. In TLS 1.3 a passive sensor sees the selected group but not the server certificate, which is encrypted, so certificate algorithms must come from endpoint or configuration evidence. Mixing methods without labels makes dashboards look more certain than they are.

HCU's inventory has a column for method and one for date, and dashboards show both.

### 15.4 Worked example

HCU's first dashboard reports "92 % of connections hybrid". On inspection, the only sensor sits in front of the new web gateway, which already uses X25519MLKEM768; branch VPNs and the ATM network are invisible to it. The corrected dashboard shows "web traffic: 92 % hybrid (sensor coverage 100 % of web gateway); VPN: 0 % (configuration evidence, 40/40 branches); ATM: unknown (no sensor)". The headline number fell, and the decision quality rose.

The correction did not change any system, only what the dashboard claimed. Managers could now see where work remained and where the team simply lacked sight. The ATM row led to a request to the ATM vendor for configuration evidence, since adding a network sensor there was not possible.

### 15.5 Practical activity

Design three readiness indicators for HCU. For each, give definition, source, coverage, owner and refresh rate, and name one way it could mislead.

A good definition says exactly what is counted and what is not. Coverage should state which part of the estate the source can see. An owner is a person or role who will notice when the figure looks wrong. The way an indicator could mislead is often its most useful line: for example, a count of vendors with roadmaps says nothing about whether the roadmaps are realistic or have dates.

### 15.6 Common errors and limits

- Reporting a percentage without its denominator and coverage.
- Treating vendor claims as observations.
- Counting connections when the decision concerns assets or data classes.

A percentage without its base can hide a tiny sample or a biased one. Vendor statements are useful but untested; label them as claims until someone observes the behaviour. Counting connections favours busy systems, while migration decisions usually concern which assets or data classes are protected. A single busy web service can make the figure look good while a quiet but sensitive archive link stays classical. Choose the unit that matches the decision.

### Exercises

- **EX029 — Coverage.** Rewrite "95 % of our certificates are ready for PQC" so that it states method, coverage and denominator. Rubric: 3 = all three present and plausible.
- **EX030 — Indicator design.** Propose an indicator for "ability to change algorithms quickly" and explain how to measure it. Rubric: 3 = definition, measurement method, limitation.

### Synthesis

Valid, reliable measurements with stated coverage and provenance let decision-makers see both progress and blind spots.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) describe trust boundaries, zones and defence in depth; (2) draw a data-flow diagram showing cryptographic protections; (3) explain crypto-agility as an architectural property; and (4) identify long-lived trust boundaries that cross time.

### 16.1 Boundaries and zones

A *trust boundary* separates components with different levels of trust — the internet and HCU's web tier, the web tier and the core banking zone, a branch and the data centre. Data crossing a boundary needs protection appropriate to its sensitivity: encryption, authentication, validation. *Defence in depth* layers independent controls so that one failure does not expose everything.

For quantum migration, the boundaries that matter most are those where long-lived data leaves a protected zone over a network someone else could record.

### 16.2 Data-flow diagrams

A data-flow diagram shows external entities, processes, data stores and the flows between them, with trust boundaries drawn as dashed lines. Annotating each flow with protocol, key-exchange algorithm, authentication algorithm and data lifetime turns the diagram into a quantum-exposure map: any flow crossing an untrusted boundary with long-lived data and classical key exchange is a harvest-now-decrypt-later candidate.

HCU's first diagram took a week to annotate, mostly because nobody knew which algorithm several flows used. Those gaps were as useful as the answers: each became a question for an owner or vendor. Drawing the diagram before choosing any new algorithm meant the plan started from what the systems actually do.

### 16.3 Crypto-agility

*Crypto-agility* is the ability to change cryptographic algorithms with bounded effort and risk. Architecturally it means centralised policy, algorithm identifiers that travel with data, libraries that support multiple algorithms, and interfaces that tolerate larger keys and signatures. NIST's [CSWP 39](https://doi.org/10.6028/NIST.CSWP.39-upd1) discusses crypto-agility considerations. An architecture without agility treats the PQC migration as a one-off rebuild; an agile one treats it as the first of several planned changes.

For HCU, agility is tested by asking how long it would take to switch an algorithm on the branch VPN.

### 16.4 Boundaries in time

Some boundaries are crossed not in space but in time. A mortgage signed today will be verified by a court or buyer years later; an archive encrypted today will be decrypted during a future audit. Architecture should show long-term services — timestamping, archive re-encryption, evidence renewal — as components whose own cryptography must be migrated.

HCU's mortgage archive is the clearest case: its encryption and its signatures must still work, and stay secure, decades after the documents were created. Each needs an owner.

### 16.5 Worked example

HCU's diagram shows the mobile app → web gateway (internet boundary, TLS hybrid), web gateway → core banking (internal, TLS classical), core banking → archive (internal, AES-256 at rest, keys wrapped with RSA-OAEP), branch → data centre (WAN boundary, IPsec ECDH). Annotation reveals two priorities: the branch WAN for HNDL and the RSA-wrapped archive keys, which are exposed if the wrapped keys are ever copied off-site.

The internal TLS link between the gateway and core banking is classical but lies within the data centre, which lowers its priority. The diagram made these trade-offs visible in one page, and the HCU security office used it to agree the first year's migration plan.

### 16.6 Common errors and limits

- Drawing diagrams without algorithms and lifetimes.
- Considering only network boundaries, not time boundaries.
- Hard-coding algorithm choices in application code.

A diagram without algorithms and lifetimes cannot show quantum exposure, however neat it looks. Time boundaries are easy to miss because they do not appear on network maps; archives, timestamps and signed records cross them silently. Algorithm choices hard-coded in application code turn every future change into a software project, which is the opposite of crypto-agility. Record each choice in configuration or policy instead, so that it can be found and changed later.

### Exercises

- **EX031 — Exposure map.** For the HCU diagram in 16.5, rank the four flows by HNDL priority and justify the ranking. Rubric: 3 = ranking consistent with boundary, lifetime and algorithm.
- **EX032 — Agility features.** List three architectural features that would let HCU switch from ML-KEM-768 to another KEM if needed. Rubric: 3 = three concrete, distinct features.

### Synthesis

Trust boundaries, annotated data flows and crypto-agility let architects locate quantum exposure and design for repeated algorithm change, including boundaries crossed in time.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) distinguish symmetric encryption, hash functions, MACs, key exchange, KEMs and signatures; (2) explain security levels and NIST's post-quantum categories; (3) build and break a Lamport one-time signature; and (4) name the three final NIST post-quantum standards.

### 17.1 The toolbox

*Symmetric encryption* (AES) uses one shared key; *hash functions* (SHA-2, SHA-3) compress data to a fingerprint; *MACs* (HMAC) prove integrity with a shared key; *key exchange* (Diffie–Hellman) lets two parties derive a shared secret over a public channel; a *key-encapsulation mechanism* (KEM) lets one party encapsulate a fresh secret to another's public key; *signatures* let anyone verify that the holder of a private key approved a message. Quantum computers threaten key exchange, public-key encryption and signatures based on factoring and discrete logarithms; symmetric primitives and hashes need at most larger parameters.

### 17.2 The NIST standards

In August 2024 NIST published three post-quantum standards: [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203) ML-KEM, a lattice-based KEM with parameter sets ML-KEM-512, -768 and -1024; [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) ML-DSA, a lattice-based signature; and [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205) SLH-DSA, a stateless hash-based signature. Earlier, [SP 800-208](https://doi.org/10.6028/NIST.SP.800-208) approved the stateful hash-based signatures LMS and XMSS. NIST defines security *categories* 1–5 by comparison with breaking AES-128, SHA-256, AES-192, SHA-384 and AES-256; ML-KEM-768 targets category 3.

For HCU, category three parameter sets are the common starting point, since they offer a comfortable margin at moderate size.

### 17.3 Practical activity — Lab L

The Lamport scheme signs one message by revealing, for each bit of its hash, one of two secret values whose hashes form the public key.

```python
# Lab L (ch 17): Lamport one-time signatures from SHA-256 - the idea under SLH-DSA, LMS and XMSS.
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
print(f"after one reuse, both secrets revealed at {revealed}/256 positions -> forging needs ~2^{256 - revealed} hashes, not 2^256")
print("signature size:", 256 * 32, "bytes; public key:", 2 * 256 * 32, "bytes")
```

Expected output:

```text
valid signature verifies: True
tampered message rejected: True
after one reuse, both secrets revealed at 118/256 positions -> forging needs ~2^138 hashes, not 2^256
signature size: 8192 bytes; public key: 16384 bytes
```

Security rests only on the hash function, which is why hash-based signatures are considered conservative. Reuse is fatal: two signatures reveal both secrets at many positions. SLH-DSA builds trees of one-time and few-time signatures so that a single key can sign many messages without state; LMS and XMSS do so with state that the signer must never repeat.

### 17.4 Worked example

HCU's architect asks which primitive fits each need: archive encryption (AES-256, keep), key transport to the archive (KEM: ML-KEM-768 in a hybrid), statement signing (ML-DSA-65 once supported, or hybrid with ECDSA during transition), firmware signing for ATMs (LMS via SP 800-208 or SLH-DSA, because signing volume is low and conservatism is valued).

Each choice follows from the need rather than from the newest algorithm. Symmetric encryption stays because Grover's search leaves AES-256 strong. Key transport needs a KEM. Signatures need to be verifiable for as long as the signed statement matters. Firmware signing favours hash-based schemes because their security rests on hash functions alone, and the low signing volume makes managing state practical.

### 17.5 Common errors and limits

- Calling ML-KEM "encryption"; it is a KEM producing a shared secret.
- Reusing one-time or stateful signature keys.
- Treating the toy Lamport lab as usable code.

A KEM gives both sides a shared secret; the data itself is then encrypted with a symmetric algorithm. Stateful signature keys must never sign twice with the same one-time key, which means the signer must track state reliably, including across backups and failures. The lab's Lamport scheme exists to show the idea of hash-based signatures; it is insecure in practice and must never be used outside the classroom.

### Exercises

- **EX033 — Pick the primitive.** For password storage, message integrity between two HCU servers, session key agreement and document approval, name the primitive and a standard algorithm. Rubric: 3 = four correct choices.
- **EX034 — Reuse.** Using Lab L's output, explain why the second Lamport signature enables forgery. Rubric: 3 = both secrets at many positions, mixing to sign new messages.

### Synthesis

Quantum computers break public-key key exchange and signatures based on factoring and discrete logarithms. NIST's FIPS 203, 204 and 205 and SP 800-208 supply replacements; symmetric and hash primitives remain, with adequate sizes.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) formulate a researchable question; (2) choose between literature review, measurement, experiment and case study; (3) design a simple measurement study with a stated population and sample; and (4) identify threats to validity.

### 18.1 Questions

A good research question is specific, answerable with available evidence and relevant to a decision. "Is PQC good?" is not researchable. "What share of HCU's branch-to-data-centre flows carry data with a confidentiality lifetime above 15 years?" is. Questions in this field often take the forms *how much* (measurement), *what happens if* (experiment), *how did it go* (case study) or *what is known* (literature review).

HCU's security office asks the student team for questions of the second kind, because each answer changes a migration priority or a budget line.

### 18.2 Methods

A *literature review* summarises primary sources systematically, recording search terms and inclusion rules. A *measurement study* counts properties of a population, such as TLS groups offered by a set of servers. An *experiment* changes one factor and observes the effect, such as handshake latency with and without a hybrid group in a lab. A *case study* examines one migration in depth. Each method answers different questions; combining them strengthens conclusions.

HCU's own studies combine a measurement of its estate with lab experiments on the slowest branch links.

### 18.3 Populations, samples and validity

State the population (all HCU web services), the sampling frame (services in the asset register) and the sample (those reachable from the test network). *Internal validity* asks whether the observed effect is caused by the factor studied; *external validity* asks whether results generalise. A latency experiment on a fast lab network may not predict results on rural branch links; that is an external-validity limit, not a failure, as long as it is stated.

HCU's asset register itself may be incomplete, which is a frame problem to state.

### 18.4 Worked example

Question: "Does enabling X25519MLKEM768 on HCU's test gateway increase median handshake time for branch clients?" Method: lab experiment with emulated branch latency of 40 ms and 1 % loss; 1,000 handshakes per condition, alternating order to control drift. Result (synthetic): median increases by 0.9 ms; the 99th percentile increases by 3 ms because some ClientHellos need a second segment. Validity note: emulated loss does not reproduce the behaviour of the branch's real inspection proxy.

The report states both the median and the tail, and the limit of the emulation. HCU's network team then tested at one branch with the real proxy before wider rollout, which is where the external-validity gap would show.

### 18.5 Practical activity

Write a one-page study protocol for measuring how many HCU internal services support TLS 1.3, including population, frame, sample, method, data handling and validity threats.

A protocol written before collecting data stops later choices from being shaped by the results. Say how you will count a service that does not respond, how you will treat services outside the register and how long the data will be kept. Validity threats might include services only reachable from some networks or a test network that differs from production. Have a classmate read the protocol and try to find a choice you left unstated.

### 18.6 Common errors and limits

- Questions too broad to answer.
- Unstated sampling frames that hide selection bias.
- Generalising lab latency to production networks.

A broad question produces vague answers that no one can act on. An unstated frame hides which systems were never in the sample, and the missing ones are often the oldest and most fragile. Lab networks are cleaner than production, so latency and failure results should be presented as lower bounds until confirmed in the field. Write each limit next to the result it affects, not in a separate place readers may skip.

### Exercises

- **EX035 — Sharpen the question.** Turn "Are our vendors ready for quantum?" into a researchable question with a method. Rubric: 3 = specific, measurable, decision-relevant.
- **EX036 — Validity.** Name one internal and one external validity threat in the experiment of 18.4. Rubric: 3 = both correct and explained.

### Synthesis

Researchable questions, explicit populations and stated validity limits turn opinions about quantum readiness into evidence.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Quantum and post-quantum security: scope and theory

### Learning outcomes

You will (1) define the scope of quantum and post-quantum security; (2) state Mosca's inequality and apply it with swept assumptions; (3) distinguish post-quantum cryptography from quantum key distribution; and (4) summarise the status of NIST standards and transition guidance.

### 19.1 Scope

The field covers four questions. What can quantum computers do to cryptography? (Shor breaks RSA, Diffie–Hellman and elliptic curves; Grover weakens symmetric search quadratically.) What replaces vulnerable algorithms? (Post-quantum cryptography: classical algorithms believed to resist quantum attack.) How do organizations migrate? (Inventory, prioritisation, hybrid deployment, agility.) And what role, if any, for quantum communication technologies such as quantum key distribution (QKD)? This book concentrates on the first three, because PQC runs on today's computers and networks.

QKD is discussed briefly below.

### 19.2 PQC versus QKD

PQC algorithms such as ML-KEM are software and hardware implementations of mathematical schemes; they work over any network. QKD uses quantum states of light to establish keys and needs dedicated links and trusted nodes, and it still needs classical authentication. The [NSA](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/) has stated that it does not support QKD for national security systems and recommends quantum-resistant algorithms instead. For an organization like HCU, PQC is the practical path.

HCU's links run over leased lines and the internet, where QKD would need new infrastructure.

### 19.3 Mosca's inequality

Mosca (2018) gave the field its planning rule. Let *x* be how long data must stay secure, *y* how long migration takes and *z* how long until a cryptographically relevant quantum computer (CRQC) exists. If *x* + *y* > *z*, you are already late for that data. Because *z* is unknown, sweep it: decisions that are correct across a plausible range of *z* are robust.

For HCU, the archive's thirty years make the left side large whatever value of the migration time is chosen. Even if a CRQC were forty years away, a migration taking more than ten years would leave some archive data exposed. The inequality turns an unanswerable question, when will the machine arrive, into a usable one: for which data does the answer not matter?

### 19.4 Practical activity — Lab M

```python
# Lab M (ch 19): Mosca's inequality x + y > z for synthetic Harbourline Credit Union data, sweeping z.
assets = [  # (name, shelf-life x in years, migration time y in years) - synthetic
    ("mortgage archive", 30, 4), ("member records", 10, 3), ("card authorisation", 0.01, 5), ("branch VPN traffic", 7, 2)]
for z in (10, 15, 20):  # years until a cryptographically relevant quantum computer: an assumption, not a forecast
    late = [n for n, x, y in assets if x + y > z]
    print(f"z={z:>2}: at risk now -> {', '.join(late) if late else 'none'}")
```

Expected output:

```text
z=10: at risk now -> mortgage archive, member records
z=15: at risk now -> mortgage archive
z=20: at risk now -> mortgage archive
```

Card authorisation messages are short-lived, so they drop out; the mortgage archive is at risk under every assumption in the sweep. That is the robust conclusion.

The lab sweeps the unknown arrival time across three values and, for each, prints the HCU data classes whose confidentiality lifetime plus migration time exceeds it. Member records appear only under the shortest assumption, so their status depends on the uncertain date; the mortgage archive appears under all three. Classes that change status within the sweep are where the date really matters, and those need closer judgment and regular review as estimates change. Classes that never appear, such as card messages, can wait for routine upgrades.

### 19.5 Standards and transition status

FIPS 203, 204 and 205 are final (August 2024). [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) gives recommendations for using KEMs. NIST's draft [IR 8547](https://doi.org/10.6028/NIST.IR.8547.ipd) proposes deprecating 112-bit-security quantum-vulnerable algorithms after 2030 and disallowing quantum-vulnerable public-key algorithms after 2035; as a draft, it signals direction rather than binding dates. FN-DSA (FIPS 206) and a standard based on HQC were in development on 12 October 2026. [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) defines terminology for post-quantum/traditional (PQ/T) hybrid schemes.

HCU tracks these documents with their status and the date checked.

### 19.6 Worked example

HCU's board asks for a one-slide answer. "Quantum computers capable of breaking our public-key cryptography do not exist today and their date is uncertain. Our mortgage archive must stay confidential for 30 years, so recorded transfers are at risk under any plausible timeline; we will protect those flows first with hybrid post-quantum key exchange, following NIST's 2024 standards. Signatures and devices follow a planned schedule aligned with NIST's draft transition guidance."

The slide avoids a predicted date, states the requirement that drives urgency and names the first action. Board members can challenge any part, and each part points to evidence in the plan. A follow-up slide lists what the board will hear about each quarter.

### 19.7 Common errors and limits

- Quoting a single CRQC date as fact.
- Presenting QKD as a drop-in replacement for PQC.
- Treating IR 8547's draft dates as final.

Published estimates of when a CRQC might exist vary widely and change as research advances, so a single date gives false confidence. QKD needs special hardware and dedicated links, solves only key distribution and still needs classical authentication. Draft guidance invites comment and may change before publication. Each mistake makes a plan look firmer than the evidence allows, and the plan breaks when the assumption does.

### Exercises

- **EX037 — Mosca.** For member records with *x* = 10 and *y* = 3, for what values of *z* is HCU already late? Rubric: 3 = *z* < 13 with reasoning.
- **EX038 — PQC or QKD.** Give two reasons why HCU should prioritise PQC over QKD for branch links. Rubric: 3 = infrastructure and authentication/guidance reasons.

### Synthesis

Quantum and post-quantum security asks what quantum computers break, what replaces it and how to migrate. Mosca's inequality, swept over uncertain timelines, ranks data; FIPS 203/204/205 provide the replacements.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Quantum and post-quantum security: foundational cases

### Learning outcomes

You will (1) summarise public cases that shaped post-quantum practice; (2) explain what each case teaches about evidence and assumptions; (3) relate the cases to hybrid deployment; and (4) apply their lessons to HCU decisions.

### 20.1 Shor and resource estimates

Shor's 1994 algorithm (journal version 1997) showed that factoring and discrete logarithms are efficiently solvable on a quantum computer. For decades, the question was resources. Gidney and Ekerå (2021) estimated 20 million noisy qubits running for eight hours to factor RSA-2048; Gidney (2025) lowered this to under a million noisy qubits in under a week, under stated assumptions about error rates and connectivity. The lesson: resource estimates fall as algorithms and error correction improve, so plans must not depend on today's estimate staying fixed.

HCU's plan therefore uses a range of arrival dates rather than one figure.

### 20.2 Broken candidates

The NIST process eliminated candidates publicly. Rainbow, a multivariate signature, was broken by Beullens (2022) with a key-recovery attack running "over a weekend on a laptop". SIKE, an isogeny-based KEM, was broken by Castryck and Decru (2022) with a classical attack. Both had survived years of analysis. The lesson: new schemes carry the risk of classical breaks, which is a main argument for hybrid deployment — combining a post-quantum and a traditional algorithm so that an attacker must break both.

Neither break needed a quantum computer.

### 20.3 Implementation flaws

KyberSlash (Bernstein et al., 2024) showed that several implementations of Kyber leaked secret information through timing of division operations, even though the mathematics was sound. The lesson: a correct standard is not a correct implementation; use vetted libraries and keep them updated.

For HCU the lesson became a procurement question: which library and version does each appliance use, and how quickly does the vendor ship fixes? A vendor that cannot answer is a risk regardless of which algorithm it claims to support.

### 20.4 Early deployment

Google's Chrome team announced hybrid post-quantum key exchange in 2023 ([Chromium Blog](https://blog.chromium.org/2023/08/protecting-chrome-traffic-with-hybrid.html)), and some servers and middleboxes failed on the larger ClientHello. The lesson: deployment exposes ecosystem bugs that no specification review finds; staged rollout and monitoring are essential.

Most failures came from software that had assumed handshake messages would stay small. Browsers rolled out gradually, measured failures and worked with server operators to fix them. HCU follows the same pattern on a smaller scale with its pilot branches.

### 20.5 Worked example

HCU's vendor proposes enabling pure ML-KEM on branch VPNs immediately. Applying the cases: SIKE shows that a new scheme can fail suddenly, so a hybrid with ECDH is the prudent transition design; KyberSlash shows that the vendor's implementation version matters, so HCU asks which library and version the appliance uses; the Chrome experience shows that one branch with a legacy device might break, so HCU starts with three pilot branches.

Each pilot branch is monitored for fallback and handshake failures before any wider rollout is approved.

### 20.6 Practical activity

Write a half-page lesson card for one of the four cases: what happened, primary source, what it changed in practice, and one question it raises for HCU.

A good card is short enough to read in a minute and links to the primary source, not a summary of it. The practical change should be specific, such as the move to hybrid designs or stricter timing tests. Your question for HCU should be one the team could actually answer, for example which of its vendors' products still use a vulnerable library version.

### 20.7 Common errors and limits

- Concluding from SIKE that all PQC is fragile; ML-KEM rests on a different, well-studied problem family.
- Treating resource estimates as predictions of dates.
- Assuming a final standard implies safe implementations.

SIKE and Rainbow were broken through their own structures; ML-KEM's lattice problems have a long research history and have resisted analysis. That is evidence, not proof, which is why hybrids are used during transition. Resource estimates show what an algorithm would need, not when someone will build it. Implementations need separate review and testing, as KyberSlash showed for a sound design.

### Exercises

- **EX039 — Case to control.** Map each of the four cases to one control HCU should adopt. Rubric: 3 = four plausible, distinct mappings.
- **EX040 — Estimate trend.** Explain why falling resource estimates should change the *y* (migration time) planning in Mosca's inequality, not just *z*. Rubric: 3 = argues for starting earlier and building agility.

### Synthesis

Falling resource estimates, broken candidates, implementation flaws and deployment bugs each teach a control: plan for uncertainty, deploy hybrids, use vetted libraries and roll out in stages.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Quantum and post-quantum security: system models

### Learning outcomes

You will (1) build a system model listing components, interfaces and cryptographic functions; (2) classify each function by quantum exposure; (3) record ownership and change mechanisms; and (4) use the model to compare migration alternatives.

### 21.1 What the model contains

A system model for quantum security lists, for each component, its cryptographic functions (key establishment, authentication, data protection, code integrity), the algorithms used, the parameters, the library or hardware implementing them, the owner and the *change mechanism* — configuration, software update, vendor release or hardware replacement. The model extends the data-flow diagram of Chapter 16 with the facts needed to estimate effort.

The change mechanism is often the deciding fact, since it sets how long a change takes. HCU fills it in owner by owner.

### 21.2 Exposure classes

Classify each function: *HNDL-exposed* (classical key establishment protecting data whose confidentiality outlasts plausible *z*); *forge-later-exposed* (classical signatures whose trust must last beyond *z*, or that cannot be quickly replaced); *Grover-adequate* (symmetric and hash functions with sufficient sizes); and *unknown*. The unknown class is not a rounding error; it often contains the hardest items, such as embedded devices.

HCU records the reason for each classification so it can be reviewed. A function moves out of unknown only when evidence arrives, such as a configuration export or a tested vendor statement.

### 21.3 Comparing alternatives

With the model, alternatives become comparable. For HCU's branch VPN: (a) upgrade appliance firmware to support hybrid IKEv2 key exchange per [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html); (b) add a pre-shared key mixed into IKEv2 per [RFC 8784](https://www.rfc-editor.org/rfc/rfc8784.html) as an interim post-quantum layer; (c) replace appliances. The model records for each the change mechanism, the protection gained, operational cost and residual risk. Option (b) protects against HNDL quickly if keys are managed well; (a) is the target; (c) is needed only where firmware support never arrives.

### 21.4 Worked example

HCU models its card terminal estate: 3,000 terminals, ECDH key exchange to the payment switch, RSA-signed firmware, vendor-controlled updates, hardware boot ROM verifying RSA only. Exposure: key exchange is HNDL-exposed only for the short-lived card data (low priority); firmware signing is forge-later-exposed and the boot ROM cannot change, so the realistic path is replacement at end of life with a procurement requirement for post-quantum firmware signing.

The model turns a hard technical problem into a planning decision with a known date: replacement cycles are already in HCU's budget, so adding a requirement to the next purchase costs little now and avoids an unplanned replacement later.

### 21.5 Practical activity

Model three HCU components (web gateway, internal CA, ATM) in a table with function, algorithm, implementation, owner, change mechanism and exposure class.

For each component, the change mechanism should name who acts: HCU staff changing configuration, a vendor shipping an update or a hardware replacement. Mark the exposure class with a short reason. If you cannot determine an entry, write unknown rather than guessing, and note what evidence would settle it. Compare your table with a classmate's; disagreements usually reveal an assumption one of you made silently.

### 21.6 Common errors and limits

- Omitting change mechanisms, which hides the true effort.
- Treating unknown items as low risk.
- Modelling only servers and forgetting devices and partners.

The change mechanism sets the effort: a configuration change might take a day, while a hardware replacement takes years. Unknown items are often unknown because they are old or closed, which makes them more likely to be hard, not less. Devices and partners carry much of the risk in a financial estate, from card terminals to partner bank links, and leaving them out makes the model look simpler than reality.

### Exercises

- **EX041 — Exposure class.** Classify: TLS to the mobile app (session data kept 7 years), AES-256 archive encryption, RSA code signing for internal tools, unknown cryptography in ATM cash dispensers. Rubric: 3 = four correct classes with reasons.
- **EX042 — Alternatives.** Compare options (a) and (b) in 21.3 on protection, effort and residual risk. Rubric: 3 = three dimensions for each.

### Synthesis

A system model records cryptographic functions, implementations, owners and change mechanisms, classifies exposure and makes alternatives comparable on explicit criteria.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Quantum and post-quantum security: data and dependencies

### Learning outcomes

You will (1) explain what a cryptographic bill of materials (CBOM) is; (2) combine evidence sources into an inventory; (3) compute coverage and unknown shares; and (4) trace dependencies through libraries, vendors and partners.

### 22.1 Inventory sources

No single method finds all cryptography. *Passive network observation* sees negotiated algorithms on the wire; *configuration review* reads what services are set to offer; *code and binary scanning* finds library calls and embedded constants; *vendor statements* describe closed products; *certificate stores* reveal signature algorithms and validity. A CBOM records, for each asset and function, the algorithm, parameters, implementation and evidence source, analogous to a software bill of materials for components.

Each method has blind spots, so HCU combines them and records the source for every entry.

### 22.2 Practical activity — Lab I

```python
# Lab I (ch 22): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("web-gateway", "key-exchange", "X25519MLKEM768", "passive"), ("web-gateway", "signature", "RSA-2048", "config"),
    ("atm-controller", "key-exchange", "ECDHE-P256", "passive"), ("atm-controller", "signature", "ECDSA-P256", "code"),
    ("core-banking", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("card-terminal", "unknown", "unknown", "none"), ("branch-vpn", "key-exchange", "ECDHE-P384", "config")]
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
assets 6, unknown 1 (17%)
quantum-vulnerable uses 5: web-gateway/signature, atm-controller/key-exchange, atm-controller/signature, core-banking/key-exchange, branch-vpn/key-exchange
hybrid key exchange present on: ['web-gateway']
```

Six synthetic assets yield five quantum-vulnerable uses and one asset (17 %) whose cryptography is unknown. The unknown card terminal needs a vendor inquiry before it can be planned.

The lab combines evidence from more than one source for each asset and prints a summary with the share of unknowns. Each row keeps its source, so a reader can see which findings rest on observation and which on vendor statements. Running the same script on next quarter's data will show whether the unknown share is falling, which is itself a useful progress indicator for the migration.

### 22.3 Dependencies

Cryptography is inherited. An application uses a framework that uses a TLS library that uses the OS provider; a SaaS vendor terminates TLS on a CDN that HCU does not control; a partner's API dictates which algorithms HCU's client must support. Draw dependency chains for high-priority flows and identify the *controlling party* for each link — the one that must act for the algorithm to change. A migration is complete for a flow only when every link has moved.

Links HCU does not control need roadmaps from their owners.

### 22.4 Worked example

HCU's mobile banking flow depends on: the phone OS TLS stack (platform vendor), the app's networking library (HCU developers), a CDN terminating TLS (CDN provider), the web gateway (HCU network team) and the core banking API (core vendor). Hybrid key exchange from phone to CDN depends on platform and CDN support; from CDN to gateway on CDN and HCU; from gateway to core on HCU and the core vendor. Three controlling parties, three different timelines.

The flow is recorded as migrated only when all three have moved, and HCU follows up each party separately.

### 22.5 Common errors and limits

- Relying on one evidence source.
- Recording algorithms without evidence source and date.
- Declaring a flow migrated when only HCU's segment has changed.

Each source misses something: network sensors miss certificates in TLS 1.3, configuration may differ from behaviour, vendor statements may be out of date. Combining them, with each row labelled, gives a fuller and more honest picture. A flow is migrated only when every party in its chain has changed, so record the state of each link separately rather than marking the flow complete when HCU's part is done.

### Exercises

- **EX043 — Coverage arithmetic.** If two more assets in Lab I become unknown, what is the unknown share? Rubric: 3 = 3/8 ≈ 38 % with method (eight assets, three unknown).
- **EX044 — Controlling parties.** For the mobile flow in 22.4, which segments can HCU migrate unilaterally? Rubric: 3 = gateway configuration and app library, with reasoning about others.

### Synthesis

A CBOM fuses multiple evidence sources with provenance; coverage and unknown shares show what the inventory cannot yet see, and dependency chains reveal who must act.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Quantum and post-quantum security: methods I

### Learning outcomes

You will (1) state the Learning With Errors (LWE) problem; (2) run a toy LWE encryption and explain why decryption works; (3) describe how ML-KEM turns this idea into a KEM; and (4) explain parameter sets and security categories.

### 23.1 Learning With Errors

Given a random matrix *A* modulo *q* and a vector *b* = *As* + *e*, where *s* is secret and *e* is a vector of small random errors, recover *s*. Without *e*, Gaussian elimination solves the system quickly. With *e*, the best known classical and quantum algorithms take time exponential in the dimension, because the problem becomes one of finding short vectors in high-dimensional lattices. Regev (2009) introduced LWE and showed its hardness relates to worst-case lattice problems. ML-KEM uses a structured variant, Module-LWE, over the polynomial rings of Chapter 6.

### 23.2 Practical activity — Lab W

```python
# Lab W (ch 23): a TOY Regev-style LWE encryption of one bit. Deliberately insecure parameters.
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

To encrypt a bit, add a random subset of the rows; the accumulated noise stays small, while the bit is placed at *q*/2. The decryptor removes the *s*-dependent part and checks whether the remainder is nearer 0 or *q*/2. The parameters here are toys — a 16-dimensional secret is easy to recover — and serve only to show the mechanism.

Running the lab several times with different random choices shows that decryption still succeeds, because the noise stays below the threshold.

### 23.3 From LWE to ML-KEM

ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)) uses Module-LWE with 256-coefficient polynomials, compresses ciphertexts, and wraps the encryption in a transform (a variant of Fujisaki–Okamoto) so that decapsulation re-encrypts and checks the ciphertext, which protects against chosen-ciphertext attacks. The interface is a KEM: KeyGen produces an encapsulation key and decapsulation key; Encaps produces a ciphertext and a 32-byte shared secret; Decaps recovers the secret. Parameter sets ML-KEM-512, -768 and -1024 target NIST categories 1, 3 and 5. Encapsulation keys are 800, 1,184 and 1,568 bytes; ciphertexts 768, 1,088 and 1,568 bytes.

### 23.4 Worked example

HCU chooses ML-KEM-768 for hybrid key exchange because category 3 offers a margin above AES-128-equivalent security, it is the parameter set used by the widely deployed X25519MLKEM768 TLS group, and its 1,184-byte key fits typical handshakes. ML-KEM-1024 is reserved for any partner whose rules demand category 5.

The choice is recorded with its reasons so it can be revisited if guidance changes. Larger keys and ciphertexts were measured in the lab before the choice was confirmed, and the branch links handled them without changes to the network.

### 23.5 Common errors and limits

- Thinking the toy lab's parameters are secure.
- Forgetting that ML-KEM is a KEM, not a general encryption function.
- Choosing parameters by size alone without considering policy requirements.

The toy parameters are chosen so that a reader can follow the arithmetic, which means an attacker could too. A KEM produces a shared secret that a symmetric cipher then uses; it does not encrypt arbitrary messages directly. Parameter choice depends on security category, policy and protocol support, as well as size. A smaller set may suit most uses, but a partner's rules can require a larger one regardless of performance.

### Exercises

- **EX045 — Why noise matters.** Explain in three sentences why LWE without error is easy and with error is believed hard. Rubric: 3 = linear algebra versus lattice short-vector argument.
- **EX046 — Parameter choice.** HCU's partner requires category 5 for key establishment. Which ML-KEM set, and how many bytes are the encapsulation key and ciphertext? Rubric: 3 = ML-KEM-1024, 1,568 and 1,568 bytes.

### Synthesis

LWE hides a secret under small noise; ML-KEM builds an efficient, chosen-ciphertext-secure KEM on its module variant, with three parameter sets mapped to NIST categories.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Quantum and post-quantum security: controls

### Learning outcomes

You will (1) list the main control families for quantum risk; (2) explain hybrid PQ/T key establishment and its terminology; (3) choose controls for HNDL and forge-later exposures; and (4) document residual risk after controls.

### 24.1 Control families

Controls for quantum risk fall into five families. *Algorithm controls* deploy post-quantum or hybrid algorithms. *Data controls* minimise, shorten or re-encrypt data so that less is exposed. *Key-management controls* add symmetric pre-shared keys or shorten key lifetimes. *Architecture controls* centralise cryptographic policy for agility. *Governance controls* include inventory ownership, procurement clauses and transition timelines.

Most HCU exposures need controls from more than one family. Governance controls are the slowest to show effect but keep the other families moving over the years a migration takes.

### 24.2 Hybrid key establishment

A PQ/T hybrid scheme, in the terminology of [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html), combines a post-quantum and a traditional component so that the result is secure if either component is. In TLS, X25519MLKEM768 ([RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html)) concatenates an ML-KEM-768 shared secret with an X25519 shared secret and feeds both into the key schedule. Hybrids hedge two risks at once: a future quantum computer (breaking X25519) and an unexpected classical break or implementation flaw in the new scheme. [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227) discusses combining KEMs and approved key-combination methods.

### 24.3 Matching controls to exposure

For HNDL exposure, deploy hybrid key establishment on flows carrying long-lived data and minimise what those flows carry. For forge-later exposure, plan post-quantum signatures, starting with long-lived trust anchors and code signing, and procure devices that support them; where signatures must remain verifiable for decades, also plan archive timestamp renewal. For unknown items, the control is investigation: a vendor inquiry or lab test.

HCU's plan lists each exposure with the control chosen and the evidence that will show it worked.

### 24.4 Residual risk

No control removes all risk. After hybrid key exchange on the branch VPN, residual risks include classical authentication (forge-later, lower urgency), unknown devices behind branches and the chance that a configuration silently falls back to classical-only. State residual risk explicitly with an owner and review date; a migration report that claims "quantum-safe" without residual risk is not credible.

HCU monitors handshakes to detect silent fallback to classical-only groups. Each fallback is logged and reviewed by the network team within a week.

### 24.5 Worked example

HCU's control plan for the mortgage archive: (1) hybrid IKEv2 for branch transfers; (2) stop sending scanned documents nightly, sending them once on completion; (3) re-wrap archive keys with ML-KEM-based key transport inside the HSM when the HSM supports it; (4) residual risk: RSA-signed archive timestamps, owner Records Management, review annually.

Item two is a data control that reduces exposure immediately and costs almost nothing. Item three depends on a vendor and is therefore dated by the HSM roadmap rather than by HCU. Item four names an owner for a risk that cannot yet be closed. Together they show that a credible plan mixes control families and admits what remains.

### 24.6 Practical activity

Produce a control table for three HCU exposures with control family, specific control, expected effect, owner and residual risk.

Choose exposures of different kinds, such as one HNDL-exposed flow, one forge-later trust anchor and one unknown device. Expected effect should be measurable, for example the share of a flow's traffic using hybrid key exchange. Name a real role as owner, not a team. Residual risk should state what stays exposed after the control and when it will be reviewed, so the table records what remains open as well as what was done.

### 24.7 Common errors and limits

- Claiming hybrid key exchange makes authentication post-quantum.
- Ignoring data controls, which are often the cheapest.
- Omitting residual risk.

Hybrid key exchange protects session secrets; signatures and certificates remain classical until changed separately. Data controls such as sending less, sending it less often or deleting it sooner often cut exposure faster and more cheaply than any algorithm change. Omitting residual risk makes a plan look finished when it is not, and readers who notice the gap stop trusting the rest of the report.

### Exercises

- **EX047 — Hybrid rationale.** Give two distinct risks that a PQ/T hybrid hedges. Rubric: 3 = quantum break of traditional and classical/implementation break of PQ.
- **EX048 — Control table row.** Write a complete control row for HCU's internal root CA. Rubric: 3 = family, control, effect, owner, residual risk.

### Synthesis

Algorithm, data, key-management, architecture and governance controls together reduce quantum risk; hybrids hedge both quantum and classical surprises, and residual risk must be stated.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) run known-answer tests (KATs) and negative tests; (2) explain why validation programs test implementations; (3) build a reproducible lab record; and (4) interpret pass and fail results correctly.

### 25.1 Why test implementations

Standards define algorithms; implementations can still be wrong. Known-answer tests run an implementation on fixed inputs and compare with published outputs; negative tests feed malformed inputs and expect rejection. NIST's Cryptographic Algorithm Validation Program applies such tests to implementations of FIPS 203, 204 and 205. Students cannot validate a production library, but they can learn the habit with primitives from the standard library.

The point of the exercise is to separate two claims that are easy to blur: that an algorithm is sound, and that a given piece of code computes it correctly. HCU's developers rely on the first from the standards process and must establish the second themselves for every library they deploy.

### 25.2 Practical activity — Lab V

```python
# Lab V (ch 25): known-answer and negative tests - the habit behind validating PQC libraries.
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

The hash KATs pass because Python's SHA-3 matches published values; the length checks show one acceptance and two rejections. A real ML-KEM decoder also checks coefficient ranges as FIPS 203 requires.

Both kinds of test are needed. The KATs confirm that correct inputs give the published outputs; the negative tests confirm that inputs of the wrong size are refused rather than processed. Note the third case: a key of the right length for ML-KEM-768 is still rejected when the caller claims ML-KEM-512, because the parameter set must match. Many real interoperability bugs come from exactly this kind of mismatch between a label and the bytes that accompany it.

### 25.3 Lab records

A lab record states the question, environment (OS, Python and library versions), inputs, exact commands, outputs and interpretation. Store it with the code so that anyone can rerun it. If a library update changes a result, the record shows what changed.

Good records also note what was not tested, so that a later reader does not assume coverage that never existed. For HCU, the lab record for each cryptographic library sits beside its configuration in version control, and the change ticket for any library upgrade links to the rerun record. An auditor can then trace a production version back to the evidence that it passed.

### 25.4 Interpreting results

A passing KAT shows that the implementation matches the reference on those inputs; it does not show constant-time behaviour, correct key handling or safe integration. A failing test may reveal a bug in the implementation, the test vector or the harness. Include a *negative control* — a deliberately wrong implementation that the test must catch — to confirm the harness can fail.

In Lab V the rejected key lengths act as a simple version of that control. If the control passes, the harness itself is broken and every earlier result is in doubt.

### 25.5 Worked example

An HCU developer integrates a new PQC library. Their lab record: library version, test vectors from the vendor's published KAT files, a harness that compares outputs, and a negative control that flips one byte of an expected output to check the harness reports failure. All KATs pass; the negative control fails as expected. The record notes that side-channel behaviour was not tested and is covered by the library's own evaluation.

The developer also records where the vectors came from and when they were downloaded, so that a later update to the vendor files can be checked against the version used.

### 25.6 Common errors and limits

- Treating KAT success as proof of security.
- Harnesses that cannot fail.
- Unrecorded versions, making results irreproducible.

- Running only positive tests, so that malformed inputs are never exercised. - Downloading test vectors from an unofficial mirror without checking their origin. - Rerunning nothing after a library upgrade because the earlier run passed. - Testing a library in isolation and assuming the integration behaves the same, when the calling code may pass the wrong parameter set or mishandle errors. Each of these leaves a gap that the lab record should make visible rather than hide.

### Exercises

- **EX049 — Negative control.** Describe a negative control for Lab V's SHA3-256 KAT. Rubric: 3 = deliberately wrong input or expected value that must produce FAIL.
- **EX050 — Limits.** List three properties a passing KAT does not establish. Rubric: 3 = side channels, key management, integration/protocol use (or equivalents).

### Synthesis

Known-answer and negative tests, recorded reproducibly and checked with negative controls, are the basic evidence that an implementation matches its standard — and nothing more.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Quantum and post-quantum security: methods II

### Learning outcomes

You will (1) explain how hybrid secrets are combined with a key-derivation function; (2) run a toy combiner and interpret its outputs; (3) describe ML-DSA and SLH-DSA at a conceptual level; and (4) compare signature options by size, speed and assumptions.

### 26.1 Combining secrets

A hybrid KEM produces two shared secrets. A *combiner* feeds both, plus context such as the handshake transcript, into a key-derivation function (KDF) so that the output is unpredictable if either secret is. Concatenation followed by HKDF-Extract, as in the TLS hybrid design, is one standard approach; [SP 800-56C Rev. 2](https://doi.org/10.6028/NIST.SP.800-56Cr2) and SP 800-227 describe approved key-derivation and combination methods.

The combiner is small, but it is where the security of the hybrid is actually decided.

### 26.2 Practical activity — Lab C

```python
# Lab C (ch 26): a hybrid key combiner. The session key depends on BOTH shared secrets.
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

Changing either secret, or the context, changes the derived key completely. Binding the context prevents an attacker from reusing secrets across different handshakes.

The four keys share no visible pattern, which is the property a KDF should give. The order of inputs matters too: the lab puts the post-quantum secret first, matching X25519MLKEM768, and both ends must use the same order or they derive different keys. In a real protocol the context is the handshake transcript hash, and the output is expanded into separate keys for each direction rather than truncated as here for display.

### 26.3 Post-quantum signatures

ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) is a lattice-based signature using the "Fiat–Shamir with aborts" technique: the signer repeatedly samples until the candidate signature reveals nothing about the key. Parameter sets ML-DSA-44, -65 and -87 have signatures of 2,420, 3,309 and 4,627 bytes. SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) relies only on hash functions; it has tiny public keys (32–64 bytes) but large signatures (7,856 to 49,856 bytes) and slower signing. LMS and XMSS are smaller and faster but stateful. FN-DSA, based on Falcon, promised compact signatures and was still in development.

### 26.4 Comparing options

Compare signatures on: assumption (lattice versus hash), sizes, signing and verification speed, statefulness, and ecosystem support. For TLS certificates, ML-DSA's speed and moderate size fit best. For firmware signed rarely and verified on boot, SLH-DSA's conservatism or LMS's small signatures may be preferred. For documents needing decades of trust, conservatism weighs heavily.

HCU's own choices follow this pattern: ML-DSA for its gateway certificates, with firmware signing for card terminals still under review. Each choice is written down with the reason, so it can be revisited when ecosystem support or cryptanalysis changes.

### 26.5 Worked example

HCU compares options for signing member statements, produced 500,000 times per month: ML-DSA-65 (3,309-byte signatures, fast signing) versus SLH-DSA-SHA2-128s (7,856-byte signatures, slow signing). The volume and PDF size favour ML-DSA-65; HCU records the residual assumption risk and plans to keep algorithm identifiers in each document so that a future change is possible.

The comparison is recorded in the decision log together with the measured signing rate on HCU's statement servers, so it can be revisited if volumes change. Signing time on the existing servers was also measured, and SLH-DSA would have needed extra hardware to keep up.

### 26.6 Common errors and limits

- Combining secrets by XOR without context binding.
- Choosing SLH-DSA for high-volume TLS without measuring cost.
- Using stateful signatures where state cannot be protected.

- Truncating the combined output below the strength needed for the session key. - Comparing signature schemes on signature size alone, ignoring the public key carried in each certificate. - Leaving the algorithm identifier out of signed documents, which makes a later migration hard. - Assuming a hybrid design is secure because each component is, without checking that the combiner binds both secrets and the context.

### Exercises

- **EX051 — Combiner property.** Using Lab C, explain why the session key stays unpredictable if X25519 is broken but ML-KEM is not. Rubric: 3 = attacker lacks one KDF input.
- **EX052 — Signature choice.** Choose a signature for ATM firmware signed four times a year and justify it. Rubric: 3 = LMS/XMSS or SLH-DSA with reasoning about volume, state and conservatism.

### Synthesis

Hybrid secrets are combined through a KDF bound to context. ML-DSA suits high-volume signing; SLH-DSA and stateful hash-based signatures trade size or state for conservative assumptions.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Quantum and post-quantum security: verification

### Learning outcomes

You will (1) define verification objectives for a migration; (2) test that hybrid key exchange is actually negotiated; (3) detect downgrade and fallback in a lab; and (4) collect verification evidence that others can reproduce.

### 27.1 Verification objectives

Verification asks whether the system does what the design says. For a migration, objectives include: the hybrid group is offered and selected for in-scope clients; classical fallback occurs only where permitted; certificates validate in all supported clients; performance stays within budget; and logs record the negotiated algorithms.

Each objective needs a method and an expected result written down before testing starts, so that results cannot be reinterpreted afterwards. For HCU, the objectives are applied separately to the web gateway and the branch VPN, because they use different products and fail in different ways.

### 27.2 Checking negotiation

Configuration says what a server *offers*; the handshake shows what is *selected*. Verify selection from the client side (test client output showing the group) and the server side (logs of negotiated groups). In TLS 1.3, the selected group appears in the cleartext ServerHello, so an authorized passive sensor can confirm it. For IKEv2, appliance logs or lab captures show the key-exchange methods negotiated under RFC 9370.

Both views should agree. If the client reports the hybrid group but server logs disagree, suspect a middlebox or a log that records offers rather than selections. HCU checks both views for each site.

### 27.3 Downgrade and fallback

TLS 1.3 protects negotiation integrity through the transcript-bound handshake, so an active attacker cannot simply strip the hybrid group without detection. But fallback can still happen legitimately: a client that does not support the group, or a server configured with classical groups preferred. Lab tests should include clients with and without hybrid support and confirm that each gets the expected outcome. Active downgrade experiments belong only in an isolated testbed.

Each expected outcome should be written beside the client version in the test plan.

### 27.4 Evidence

Record test cases, client versions, server configuration hashes, outputs and dates. A verification report lists each objective with pass, fail or not tested, plus the evidence location.

Untested objectives are listed as openly as failures, because a report that omits them overstates coverage. HCU keeps the configuration hash with each result so that a later reviewer can tell whether a pass still applies after the gateway configuration changes. A report older than the current configuration is treated as stale until the tests are rerun against it.

### 27.5 Worked example

HCU's lab verifies the pilot web gateway: a hybrid-capable client selects X25519MLKEM768 (pass); a legacy client selects X25519 (expected fallback, pass); the gateway's preference order was accidentally set with X25519 first, so even hybrid-capable clients chose X25519 on one test build (fail, fixed by reordering). Without the client-side check, the configuration would have looked correct.

The fix was verified by rerunning both clients after the change. The lesson for HCU was to make the client-side check a standing part of every gateway change, not only of the pilot, so that a reordered preference list is caught before it reaches members.

### 27.6 Practical activity

Write a verification checklist of six objectives for a hybrid-enabled HCU gateway, with method and expected evidence for each.

Include at least one objective on fallback for legacy clients and one on logging of negotiated groups. For each objective, name the client or tool used, the expected result, and where the evidence will be stored. Then mark which objectives could be checked in the lab and which need production logs, since the second kind can only be confirmed after the pilot starts.

### 27.7 Common errors and limits

- Verifying configuration instead of negotiation.
- Testing only modern clients.
- Running downgrade tests on production.

- Treating a single passing handshake as proof for every site and client type. - Forgetting to recheck after a configuration change, so earlier evidence no longer matches what runs. - Reading the server's offer list as if it were the selected group. - Leaving untested objectives out of the report instead of marking them as not tested. Each of these makes a report look more complete than the evidence behind it.

### Exercises

- **EX053 — Offer versus select.** Explain how a server can offer a hybrid group yet never select it. Rubric: 3 = preference order or client support explained.
- **EX054 — Evidence record.** List five fields every verification record should contain. Rubric: 3 = five relevant fields.

### Synthesis

Verification checks negotiated behaviour, fallback paths and evidence, not just configuration; reproducible records turn tests into assurance.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Quantum and post-quantum security: failure analysis

### Learning outcomes

You will (1) apply failure-mode and effects analysis (FMEA) to a migration; (2) plan for an algorithm break; (3) use a policy-driven registry for agility; and (4) define recovery procedures and exit criteria.

### 28.1 FMEA for cryptographic change

FMEA lists, for each component, ways it can fail, the effect, the cause, how it would be detected and a risk priority. Migration failure modes include: handshake failure due to message size; silent fallback to classical; certificate validation failure in old clients; performance degradation on constrained devices; key-management mismatch between HSMs; and an algorithm becoming untrusted after cryptanalysis.

Scoring each failure mode on severity, likelihood and detectability makes the ranking explicit and open to challenge. Silent failures deserve special attention because nothing alerts on them by default.

### 28.2 Algorithm-break response

Rainbow and SIKE show that a scheme can fall suddenly. A response plan says who decides, how quickly configuration can remove the algorithm, which systems need a release and which need hardware, and what fallback is acceptable. Hybrids make this survivable: if ML-KEM were unexpectedly weakened, hybrid flows would still rest on X25519 while a replacement is deployed.

The plan should be rehearsed in the lab before it is needed. Without a plan, HCU would be deciding under pressure which branches and terminals to change first, and the answer would depend on who happened to be on call.

### 28.3 Practical activity — Lab A

```python
# Lab A (ch 28): crypto-agility through a policy-driven registry instead of hard-coded algorithms.
import hashlib, hmac
REGISTRY = {"hmac-sha256": lambda k, m: hmac.new(k, m, hashlib.sha256).digest(),
            "hmac-sha3-256": lambda k, m: hmac.new(k, m, hashlib.sha3_256).digest()}
POLICY = {"tag-algorithm": "hmac-sha256", "accept": ["hmac-sha256", "hmac-sha3-256"]}
def protect(key, msg):
    alg = POLICY["tag-algorithm"]; return alg, REGISTRY[alg](key, msg)
def check(key, msg, alg, tag):
    if alg not in POLICY["accept"]: return False            # algorithm identifier is authenticated by policy
    return hmac.compare_digest(REGISTRY[alg](key, msg), tag)
k, m = b"k" * 32, b"member statement 42"
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

Migration is a policy change, not a code change. The algorithm identifier travels with the data; during transition both algorithms are accepted, and after retirement the old one is refused. Using a MAC here keeps the lab simple; the same pattern applies to signatures and KEMs.

In a real system the registry would hold KEM and signature identifiers, and the policy would be loaded from configuration rather than set in code. The lab also shows why retirement is a separate step: tags created under the old algorithm stop verifying, so data that must stay valid needs re-protecting first.

### 28.4 Recovery and exit criteria

Each stage needs a rollback procedure and an exit criterion. Rollback restores the previous configuration quickly if failures exceed budget. Exit criteria say when a transitional state ends, such as "classical-only negotiation below 0.5 % for 90 days", so that fallback does not become permanent.

Both should be agreed before the stage begins, not after a problem appears. HCU writes the rollback steps into the change ticket and tests them in the lab, because a rollback that has never been run tends to fail at the moment it is needed. The exit criterion is reviewed at each stage decision, and any extension is recorded with a reason and a new date.

### 28.5 Worked example

HCU's FMEA ranks "silent fallback to classical on branch VPN" highest: severe for HNDL, likely due to misconfiguration, hard to detect without monitoring. Control: alert when any branch negotiates without the post-quantum method, weekly report of fallback share. "Large ClientHello dropped by legacy proxy" ranks second: visible quickly, so the control is staged rollout and a rollback runbook.

The FMEA is reviewed after each rollout stage, since measured results may change the rankings. Both controls are tested in the lab before the pilot begins.

### 28.6 Common errors and limits

- Considering only availability failures, not silent security failures.
- No plan for an algorithm break.
- Transitional fallbacks with no exit criteria.

- Scoring detectability too generously for failures that produce no error. - Writing rollback procedures that have never been rehearsed. - Ranking failure modes once and never revisiting them after the rollout produces real data. - Leaving key-management mismatches out of scope because they sit with a different team. Each one leaves a risk on the table that the analysis was supposed to expose.

### Exercises

- **EX055 — FMEA row.** Write one FMEA row for "certificate validation failure in legacy clients after post-quantum certificates". Rubric: 3 = mode, effect, cause, detection, priority.
- **EX056 — Break response.** Outline five steps HCU takes if a serious weakness is announced in a deployed PQ algorithm. Rubric: 3 = decision owner, assessment, configuration change, releases/hardware, communication.

### Synthesis

FMEA exposes both noisy and silent failures; agility, hybrids, rollback runbooks and exit criteria make algorithm change and algorithm breaks survivable.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Quantum and post-quantum security: operations

### Learning outcomes

You will (1) plan a staged rollout with canaries; (2) use confidence bounds for promotion decisions; (3) monitor negotiated algorithms in production; and (4) coordinate change with help desk and partners.

### 29.1 Staged rollout

Operations introduce change gradually: enable a hybrid group for 1 % of traffic, then 10 %, then everyone, checking at each stage that failure rates stay within an agreed budget. Each stage has a duration long enough to see weekly patterns and a named decision-maker.

The budget and the stage durations are agreed before the first stage starts, so that pressure to finish does not change them midway. HCU sets its budget against the baseline failure rate measured on the gateway before any change, and it treats a site with unusual equipment as its own stage rather than averaging it into the rest.

### 29.2 Practical activity — Lab K

```python
# Lab K (ch 29): canary gate for enabling a hybrid group - promote only if failures stay within budget.
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

The decision uses the upper confidence bound, not the point estimate. The first canary's point estimate is low but the sample is small; the bound exceeds the budget, so the team waits for more data. The proxy-site canary shows a real problem.

The second canary has a larger sample, so its bound is tight enough to promote. The third has the same sample size but more failures, and its bound is well above the budget, so the team holds and investigates the site instead of waiting for more data.

### 29.3 Monitoring

Production monitoring should report negotiated key-exchange groups by service and site, fallback shares, handshake failures by error type, and certificate validation errors. Alerts fire when fallback exceeds thresholds. Measurement lag matters: if partner data arrives monthly, promotion decisions for partner flows cannot be weekly.

Dashboards should separate sites, so that one problem location does not disappear in an average. HCU's monitoring reports fallback share for each branch, which is how the proxy problem in its rollout was found quickly. Fallback that grows slowly is a warning sign too.

### 29.4 Communication

Publish a short note at each stage: what changed, measured failure bound, known exceptions and next decision date. Help-desk staff who know that a hybrid rollout reached a site will route related tickets quickly.

Notes are short and go to the same list each time, so that staff know where to look. HCU sends them to branch managers and the help desk, and keeps them with the rollout record as part of the evidence of what changed and when. When a stage is held, the note says so plainly and gives the reason, so nobody assumes the rollout has quietly moved on.

### 29.5 Worked example

HCU rolls out hybrid key exchange on its web gateway. Stage 1 (1 %, one week) holds because the confidence bound is wide; stage 1 extended to two weeks promotes. Stage 2 at 10 % reveals elevated failures from one branch with a legacy inspection proxy; that branch is excluded, the proxy vendor is engaged and the rest proceeds. Monitoring shows 0.3 % fallback after full rollout, all from old clients.

The excluded branch has its own exit date, after which it is reviewed again. The note for each stage went to the help desk the same day.

### 29.6 Common errors and limits

- Promoting on point estimates from small samples.
- Monitoring only failures, not fallback.
- Changing configuration without help-desk awareness.

- Averaging all sites together, so one failing location is hidden. - Holding a stage without recording a reason or a new decision date. - Leaving an excluded site without an owner or a deadline, so it never rejoins the rollout. - Setting the failure budget after seeing the data rather than before. Each of these turns a measured, staged change into a rollout that nobody can fully explain later.

### 29.7 Rollback in practice

Every stage needs a rehearsed rollback: the exact configuration to restore, who may trigger it, and how long it takes. Rehearse it in the lab before the first canary. A rollback that has never been tested is a hope, not a control. After a rollback, record what was observed, keep the evidence, and decide whether the cause was the algorithm, the implementation or the environment before trying again; most first-attempt rollbacks in hybrid deployments trace to environment issues such as old proxies.

### Exercises

- **EX057 — Promotion rule.** Explain why Lab K's first canary is held even though 3/5,000 = 0.06 % is below the 0.09 % threshold. Rubric: 3 = upper bound exceeds budget due to small sample.
- **EX058 — Monitoring set.** List four metrics for monitoring a hybrid rollout and the alert condition for one. Rubric: 3 = four relevant metrics, one sensible alert.

### Synthesis

Staged rollouts with confidence-bound gates, monitoring of negotiated algorithms and clear communication turn a risky change into a controlled one.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) estimate handshake bytes for post-quantum certificate chains; (2) compare signature options quantitatively; (3) relate byte counts to network behaviour; and (4) report results with assumptions.

### 30.1 Why bytes matter for authentication

Hybrid key exchange adds about 2.3 kB per TLS handshake. Post-quantum authentication adds more: each certificate contains a public key and a signature, and the handshake includes a CertificateVerify signature and often signed certificate timestamps (SCTs). With ML-DSA every one of these grows.

Because a chain carries several of these elements, the growth multiplies rather than adds. A server might send two certificates, each with an ML-DSA key and signature, plus the CertificateVerify and two SCT signatures, so the authentication bytes can exceed the key-exchange bytes several times over. That is why HCU treats certificates as a separate migration decision from key exchange.

### 30.2 Practical activity — Lab B

```python
# Lab B (ch 30): bytes of authentication in a TLS handshake for different signature choices.
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

The model assumes a two-certificate chain, ~400 bytes of other fields per certificate and two SCTs; real chains vary. ML-DSA-44 raises authentication bytes roughly twelve-fold over ECDSA; SLH-DSA-128s more than thirty-fold.

The counting is deliberately simple: each certificate carries its own public key and a signature from the issuer, and the handshake adds one CertificateVerify signature plus one signature per SCT. SLH-DSA has a tiny public key but very large signatures, so it is hit hardest by the number of signatures in the chain. Changing the depth or SCT count in the lab shows which lever matters most for each scheme.

### 30.3 Network effects

TCP's initial congestion window commonly allows about ten segments (~14 kB) before waiting for acknowledgement. A server flight exceeding it costs an extra round trip — small on a data-centre link, noticeable on a 150-ms mobile or satellite path. Certificate compression ([RFC 8879](https://www.rfc-editor.org/rfc/rfc8879.html)) helps little with high-entropy keys and signatures. Engineering responses include shorter chains, fewer SCTs and careful choice of parameter sets.

For HCU's mobile users, that extra round trip on cellular links is the main concern.

### 30.4 Reporting

Report results with assumptions: chain depth, field sizes, number of SCTs, initial window. State that the model estimates bytes, not latency, and that latency needs measurement.

Comparisons are valid only when every scheme is run with the same assumptions. HCU attaches the Lab B parameters to its report on certificate options, so a reviewer can change one assumption, such as the number of SCTs, and see the effect. Measured latency from the emulated links is reported separately from the byte estimate.

### 30.5 Worked example

HCU's mobile app talks to the gateway over cellular links with 80-ms round trips. Lab B suggests ~15.5 kB of authentication with ML-DSA-44, slightly above a typical initial window. HCU's plan: keep ECDSA certificates while monitoring ecosystem support, test ML-DSA-44 chains in the lab with one SCT, and measure latency on emulated cellular links before any change.

The decision is to be revisited when browsers and client libraries support ML-DSA certificates widely. Members on slow links would notice the delay first, so the emulated tests use the worst branch and mobile conditions HCU has recorded rather than the average.

### 30.6 Common errors and limits

- Equating bytes with latency.
- Ignoring SCTs and intermediate certificates.
- Comparing signature schemes only by signature size, not public key plus signature.

- Assuming certificate compression will make up the difference. - Testing only on fast lab networks, where an extra round trip is invisible. - Choosing a larger parameter set than policy needs, adding bytes with no benefit. - Reporting a single byte figure without the chain depth and SCT count behind it. Each makes the cost of post-quantum authentication look different from what users actually experience.

### 30.7 Trimming the chain

When bytes matter, engineers have several levers before choosing a different algorithm: remove unnecessary intermediates, reduce the number of embedded SCTs where policy permits, avoid sending a root certificate the client already trusts, and prefer ML-DSA-44 over larger parameter sets where category 2 meets policy. Each lever has a cost in policy or compatibility, so record which were used and why. Re-run Lab B with the trimmed configuration and keep both results in the lab record.

Note any client that fails with the trimmed chain.

### Exercises

- **EX059 — Recompute.** Using Lab B's formula, compute ML-DSA-65 bytes with one SCT instead of two. Rubric: 3 = 21,249 − 3,309 = 17,940 bytes.
- **EX060 — Assumption list.** List four assumptions behind Lab B and how each could change the result. Rubric: 3 = four assumptions with direction of effect.

### Synthesis

Post-quantum authentication multiplies handshake bytes; simple models with stated assumptions guide where to measure latency and how to trim chains.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Quantum and post-quantum security: advanced cases

### Learning outcomes

You will (1) analyse migrations with constrained devices, long-term signatures and partners; (2) apply stateful signature management; (3) plan long-term archive protection; and (4) reason about third-party dependencies.

### 31.1 Constrained devices

Card terminals, ATMs and building controllers have limited memory, slow processors and long lifetimes. ML-KEM is fast enough for most, but key and signature sizes may exceed buffers, and boot ROMs that verify only RSA cannot change. The realistic plan combines firmware upgrades where possible, gateways that terminate post-quantum protocols in front of devices that cannot, and procurement requirements so that replacements are ready.

For HCU, the 3,000 card terminals are the clearest case. Each model needs a record of what its firmware can verify and how much memory it has, so that the plan can say which terminals will be upgraded and which will sit behind a gateway until they are replaced.

### 31.2 Stateful signatures in practice

LMS and XMSS ([SP 800-208](https://doi.org/10.6028/NIST.SP.800-208)) require that each one-time key is used once. State must survive crashes, backups and HSM failover without rollback. SP 800-208 requires these schemes to be generated and used within hardware cryptographic modules and forbids exporting private keys, which reflects the danger of state duplication. Organisations using them plan the total number of signatures in advance and monitor remaining capacity.

Running out of one-time keys stops signing completely, so capacity planning is part of the design.

### 31.3 Long-term signatures and archives

A mortgage signed with ECDSA today must still be verifiable in 30 years. If a quantum computer can later forge ECDSA, a forger could backdate documents. Archive systems address this with timestamps and evidence records renewed with stronger algorithms before the old ones weaken; the renewal proves the document existed while its original signature was still trustworthy. Encrypted archives need similar care: re-encrypting with new keys does not help if old ciphertexts or wrapped keys were already copied.

For HCU this means the archive plan covers signatures, timestamps and keys together.

### 31.4 Partners and suppliers

Payment networks, shared service providers and regulators set requirements HCU cannot change alone. Migration plans list partner dependencies, ask for roadmaps, and include contract clauses for algorithm support and inventory disclosure.

Where a partner cannot yet say when it will support post-quantum algorithms, the plan records that as an open dependency with an owner and a date to ask again, rather than assuming the partner will be ready in time. HCU tracks its payment network and core banking provider this way, since both control flows it cannot change on its own.

### 31.5 Worked example

HCU's ATM vendor offers a firmware update supporting ML-KEM for the ATM-to-switch link but not post-quantum firmware signing, because the boot ROM verifies only RSA. Decision: deploy the key-exchange update to protect PIN-related traffic (short-lived but sensitive), accept forge-later residual risk for firmware until replacement in five years, and require LMS or ML-DSA boot verification in the replacement tender.

The residual risk is written into the risk register with an owner, so that it is reviewed each year rather than forgotten until the replacement arrives.

### 31.6 Practical activity

Write a one-page plan for HCU's 30-year mortgage archive covering signatures, timestamps, encryption and key wrapping.

Say which documents need protection for the full period, when evidence records will be renewed, how the renewal is triggered, and who owns it. Explain how the plan deals with ciphertexts and wrapped keys that may already have been copied, since re-encryption alone cannot help them. Finish with the first three actions HCU should take this year and the evidence each will produce. Keep it to one page.

### 31.7 Common errors and limits

- Using stateful signatures in software without protected state.
- Assuming re-encryption fixes past exposure.
- Leaving partner dependencies out of the plan.

- Treating a gateway in front of old devices as permanent rather than as a bridge to replacement. - Renewing archive timestamps only after the old algorithm is already doubted, when the renewal can no longer prove anything. - Planning the total number of stateful signatures without allowing for test, backup and failover use. - Buying replacement devices without post-quantum boot verification in the tender.

### Exercises

- **EX061 — State rollback.** Describe what happens if an LMS signer is restored from yesterday's backup and signs again. Rubric: 3 = one-time key reuse, forgery risk, prevention.
- **EX062 — Archive renewal.** Explain why timestamp renewal must happen before the original algorithm is weakened. Rubric: 3 = proof of existence while trust held.

### Synthesis

Constrained devices, stateful signatures, long-term archives and partner dependencies demand plans that combine upgrades, gateways, procurement, renewal and contracts.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Quantum and post-quantum security: interdisciplinary interfaces

### Learning outcomes

You will (1) connect PQC migration to law, finance, procurement and communications; (2) translate technical risk for board decisions; (3) estimate migration cost drivers; and (4) design stakeholder engagement.

### 32.1 Law and regulation

Regulators increasingly expect financial institutions to manage cryptographic risk. Contracts define confidentiality periods that become *x* in Mosca's inequality. Evidence rules for signed documents shape archive design. A lawyer and a cryptographer looking at the same mortgage archive see two sides of one requirement.

Getting both views into the same room early prevents a design that is technically sound but cannot be relied on in a dispute. For HCU, the legal team supplies the confidentiality periods for each data class, and those periods become the inputs to the prioritisation model rather than estimates made by the technical team alone.

### 32.2 Finance and procurement

Migration cost drivers include inventory effort, software upgrades, hardware replacement, testing, staff training and partner coordination. Aligning hardware replacement with natural refresh cycles lowers cost; procurement clauses requiring algorithm agility, post-quantum support and cryptographic inventories reduce future cost. Finance teams need ranges and assumptions, not single figures.

A range that shows the effect of a delayed vendor or an early replacement is more useful than a precise number that turns out wrong. HCU's estimate separates costs it controls, such as testing and training, from costs set by partners and vendors.

### 32.3 Communication and governance

Boards need one-page decisions: exposure, options, recommendation, cost range, residual risk. Staff need to know what changes for them. Members need reassurance without alarm. Avoid fear-based messaging; describe what is being protected and why the timing is prudent.

The same facts can serve each audience if the level of detail changes. HCU's board paper on the migration fits on one page, with the technical evidence attached for those who want it. The member notice, if one is ever needed, says what is protected and that nothing is required of members.

### 32.4 Worked example

HCU's security lead presents to the board: "Our 30-year mortgage archive is exposed to recorded-traffic risk under any plausible quantum timeline. Option A: hybrid key exchange on branch VPNs within 12 months, cost CU 180–260k (synthetic currency units). Option B: wait for full appliance replacement in four years, cost included in refresh budget, but four more years of exposure. Recommendation: A, plus post-quantum requirements in the refresh tender. Residual risk: classical signatures on archive timestamps, addressed in the archive plan." The board approves A with a quarterly report.

### 32.5 Practical activity

Prepare a stakeholder map for HCU's migration: legal, finance, procurement, IT operations, vendors, partners, members and regulators, with what each needs and provides.

Mark which groups must approve decisions, which must be consulted, and which only need to be informed. Note any group whose cooperation is on the critical path, such as the payment network, and say how and when it will be contacted. Then compare your map with a classmate's and discuss any group one of you missed. Keep the map current as the plan changes.

### 32.6 Common errors and limits

- Presenting technical detail without a decision.
- Single-figure cost estimates.
- Ignoring procurement as a control.

- Leaving legal and procurement out until the technical design is finished. - Treating member communication as an afterthought. - Writing board papers that list risks but do not ask for a decision. - Assuming regulators want the same detail as engineers. - Forgetting that partners' timelines may set the pace. Each makes a sound technical plan harder to fund, approve or carry out. Involving these groups early costs little and avoids rework.

### 32.7 Regulators and auditors

Auditors will ask for evidence, not intentions: the inventory with its coverage, the prioritisation method, the approved plan and progress against it. Organizing the migration programme so that these artefacts exist as by-products of normal work — the CBOM regenerated each quarter, decision records for each choice — makes audits cheaper and more honest than preparing special documents before each review.

An honest progress report includes the items that are late and why. HCU's internal audit team reviews the CBOM and decision records once a year and reports any gaps to the risk committee.

### Exercises

- **EX063 — Board slide.** Write a five-line board decision for HCU's internal CA migration. Rubric: 3 = exposure, options, recommendation, cost range, residual risk.
- **EX064 — Procurement clause.** Draft two contract clauses supporting crypto-agility. Rubric: 3 = enforceable, specific clauses.

### Synthesis

PQC migration is interdisciplinary: law sets lifetimes, finance and procurement shape cost, and governance turns analysis into decisions.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) design comparative studies with controlled variables; (2) handle measurement uncertainty and replication; (3) analyse qualitative data from interviews; and (4) write a methods section others could repeat.

### 33.1 Comparative design

Comparative questions — "which of two hybrid configurations performs better on branch links?" — need controlled variables: same hardware, same network emulation, same client versions, randomised order. Record everything that could differ. Prefer paired designs, where each condition runs on the same set of clients, so that client variation cancels out.

In a lab, small differences such as a background update on one virtual machine can be larger than the effect being measured. Run a short pilot first to check that the measurement itself is stable before collecting the main data.

### 33.2 Uncertainty and replication

Report medians and high percentiles with confidence intervals; repeat runs on different days; publish scripts and configurations. A result that disappears on replication was noise. For rare events such as handshake failures, plan sample sizes in advance so that confidence bounds are narrow enough to support the decision.

State the intervals in the write-up, not only in an appendix, so readers see how certain each result is. A difference smaller than the run-to-run variation should be reported as no detectable difference, which is itself a useful finding for a migration decision.

### 33.3 Qualitative evidence

Many migration questions are organisational: why did a team delay? what do vendors say about roadmaps? Semi-structured interviews, coded for recurring themes, answer such questions. Protect interviewees with consent, anonymisation and secure storage. Combine qualitative findings with measurements: interviews may explain why fallback persists at certain branches.

Interview notes are analysed with the same care as measurements: the coding scheme is written down, and a second person codes a sample to check agreement. Quotes are reported without names or details that would identify a branch or a person.

### 33.4 Methods sections

A methods section states question, design, setting, participants or systems, procedure, measures, analysis and limitations. The test is replication: could another student rerun your study from the text and obtain comparable results?

Write it as the study is done, not afterwards. Include the exact versions of software, the configuration of any network emulation, and how many runs were made. Limitations belong here too: for HCU studies, the most common is that the lab does not reproduce every device found in the branches.

### 33.5 Worked example

An HCU study compares ML-KEM-768 hybrid against classical X25519 handshakes on emulated branch links (40 ms RTT, 1 % loss). Paired design: 20 client VMs, each runs 500 handshakes per condition in random order, repeated on three days. Result (synthetic): median +0.8 ms (95 % CI 0.6–1.0), p99 +3.1 ms (CI 2.2–4.3). Interviews with five branch IT staff explain that two branches route through an old proxy, which the emulation did not include — a stated limitation and next study.

The proxy finding links to the rollout in Chapter 29. The study's scripts are kept so it can be rerun.

### 33.6 Practical activity

Write a methods section for a study of certificate-chain size effects on HCU's mobile app, including sample size reasoning.

Explain how many handshakes you need to detect a difference you care about, which client devices and network conditions you will emulate, and how you will separate the effect of chain size from other changes. State what result would lead HCU to keep ECDSA and what would support a move to ML-DSA. List the limitations you expect before collecting any data.

### 33.7 Common errors and limits

- Unpaired comparisons with uncontrolled clients.
- Reporting only means for skewed latency.
- Interviews without consent or anonymisation.

- Changing two variables at once, so that the effect cannot be attributed. - Running all of one condition before the other, letting time-of-day effects creep in. - Reporting one day's results as if they were general. - Drawing conclusions from interviews with only the most enthusiastic staff. Each weakens the evidence a migration decision depends on. The fix in each case is planning before data collection. Write the plan down first.

### Exercises

- **EX065 — Paired design.** Explain why the paired design in 33.5 is stronger than running each condition on different clients. Rubric: 3 = variance reduction and confounding.
- **EX066 — Methods checklist.** List the eight elements of a methods section and give one HCU-specific example for two of them. Rubric: 3 = complete list with examples.

### Synthesis

Controlled comparisons, replicated measurements with uncertainty, ethical qualitative inquiry and replicable methods sections make research on migration trustworthy.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two or more migration approaches on explicit criteria; (2) weight criteria transparently; (3) test the sensitivity of the conclusion to weights and assumptions; and (4) present a defensible recommendation.

### 34.1 Criteria and weights

Comparisons need criteria agreed in advance: protection against HNDL, protection against forge-later, operational risk, cost, time to deploy, agility for future change and dependency on third parties. Weights express priorities; publish them so readers can disagree with the weights rather than with hidden judgments.

A criterion that cannot be scored with evidence should be reworded or dropped. For HCU, the weights were set by the risk owner after discussion with operations and finance, and each criterion has a short definition so that two scorers would read it the same way. HNDL protection carries the largest weight because of the mortgage archive.

### 34.2 Scoring and sensitivity

Score each alternative per criterion on a simple scale with evidence. Multiply by weights and sum. Then vary weights and key assumptions (CRQC timeline, vendor delivery dates) to see whether the ranking changes. A recommendation that holds across reasonable weightings is robust; one that flips with small changes should be presented as a close call.

Record each score with its source. A score with no evidence behind it is a guess and should be marked as one. Sensitivity runs are chosen where reviewers disagree most, not at random, so that the analysis answers the questions people are actually asking.

### 34.3 The project

Students compare, for HCU's branch WAN, three options: (A) hybrid IKEv2 via appliance firmware, (B) RFC 8784 post-quantum pre-shared keys as an interim layer, and (C) a new SD-WAN product with native hybrid support. Evidence comes from the system model (Chapter 21), lab measurements (Chapters 25 and 30) and vendor statements labelled as such.

Each option is described in enough detail that a reader can see what would actually change at a branch. The comparison covers all 40 branches, noting where a branch's appliance or link differs from the rest, because one exception can change which option is practical there.

### 34.4 Worked example

Synthetic scores (1–5) with weights HNDL 0.35, operational risk 0.2, cost 0.15, time 0.15, agility 0.15: A = 4,4,4,3,4 → 3.85; B = 3,3,5,5,2 → 3.45; C = 5,2,1,2,5 → 3.35. Sensitivity: if time weight rises to 0.3 (taking 0.15 from HNDL), B narrowly overtakes A (A 3.70 vs B 3.75). The recommendation becomes "A as target; B as interim at branches where firmware is delayed".

The weights were agreed with HCU's risk owner before scoring began, and the sensitivity run was chosen because delivery time was the factor most disputed in review. Branches waiting on firmware are named in the plan.

### 34.5 Practical activity

Complete the comparison with your own scores and evidence; run at least two sensitivity variations; write a one-page recommendation.

Where a score depends on a vendor statement, label it and say how you would check it. In the recommendation, state the option, the main reason, the sensitivity result that could change it, and the first action HCU should take. Keep the page readable by someone who will not open the scoring table. Then ask a classmate to change one weight and see whether your recommendation still holds.

### 34.6 Common errors and limits

- Choosing criteria after scoring.
- Treating vendor claims as measured evidence.
- Presenting a single ranking without sensitivity.

- Using too many criteria, so each carries little weight and the scoring becomes noise. - Double-counting one concern under two names, such as cost and time when both measure the same vendor delay. - Scores without recorded evidence. - Omitting the option of doing nothing yet, which is a real choice with its own risks. Review the criteria list with someone outside the project before scoring. Keep notes of that review.

### 34.7 Presenting the comparison

Show the scoring table, the weights and the sensitivity results on one page, followed by the evidence behind each score. Readers should be able to change one weight in their head and see whether the conclusion survives. Where a score rests on a vendor statement rather than measurement, mark it, because those scores are the first to revisit when the vendor delivers or slips.

Keep the version history of the table. When a vendor delivers late or early, update the affected score, rerun the sensitivity checks and note the date, so readers can see how and why the recommendation evolved.

### Exercises

- **EX067 — Recompute.** Verify the weighted totals in 34.4 for A and B under the changed weights. Rubric: 3 = correct arithmetic shown.
- **EX068 — Criterion.** Propose an additional criterion relevant to HCU and explain how you would score it with evidence. Rubric: 3 = relevant, measurable criterion.

### Synthesis

Transparent criteria, weights and sensitivity analysis turn a comparison of migration options into a recommendation that others can check and challenge.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) choose a capstone problem in quantum and post-quantum security; (2) write aims, scope, methods and deliverables; (3) plan authorization, ethics and data handling; and (4) define success criteria and risks.

### 35.1 Choosing a problem

A good capstone addresses a real decision, can be completed in one academic year, and uses evidence the student can lawfully obtain. Suitable topics: an inventory and prioritisation method for a synthetic organization; a lab comparison of hybrid configurations; an archive-protection design; a crypto-agility refactoring of a small open-source tool; or a study of vendor PQC roadmaps from public documents.

The best topics come with a named person who would use the result. A study that answers a question nobody is asking is harder to motivate and to evaluate, however good its method.

### 35.2 Proposal structure

State the problem and why it matters; the aims and research questions; scope (in and out); method; data and authorization; deliverables (report, code, lab records); timeline with milestones; risks and mitigations; and success criteria. Success criteria should be observable, for example "a reproducible lab showing negotiated groups for five client types".

A proposal of three or four pages is enough. The most important part is often the part on risks: what happens if a library, dataset or interview access does not arrive in time, and what the fallback plan will be. Reviewers look for criteria that can clearly be met or missed.

### 35.3 Authorization and ethics

Any work on real systems needs written authorization from the owner. Prefer synthetic or lab environments. Plan data minimisation and retention. If interviews are included, plan consent and anonymisation. If you might find vulnerabilities in products, plan coordinated disclosure.

Write these plans down before starting, and have them checked by the supervisor and, where interviews are involved, by the ethics process of your institution. Record any data you will not collect and why. For projects based on HCU, all data is synthetic, which removes most risks but not the need to describe how the model was built.

### 35.4 Worked example

Proposal (synthetic): "Prioritising HCU's quantum migration with a lifetime-weighted CBOM." Aims: build a CBOM for a synthetic 60-asset HCU model; rank flows using Mosca's inequality swept over *z*; validate ranking with three practitioner interviews. Scope: key establishment and signatures; excludes QKD. Data: synthetic model, public standards, consented interviews. Deliverables: Python tool, report, lab record. Success: ranking stable across *z* from 10 to 25 years for the top five flows, or a documented explanation where it is not.

The interview plan was reviewed for consent before approval.

### 35.5 Practical activity

Draft your proposal using the structure above, then exchange with a peer for review against the success-criteria test.

The reviewer should check whether each success criterion could clearly be judged met or not met at the end of the year, and whether the scope fits the time available. Revise the proposal using their comments, and keep both versions so that the changes are visible to your supervisor. If the reviewer could not judge a criterion, rewrite it until they can.

### 35.6 Common errors and limits

- Scope too large for one year.
- Unobservable success criteria.
- Assuming access to real systems without authorization.

- Choosing a method before the question is clear. - Leaving the timeline without milestones, so delays are noticed too late. - Planning interviews without allowing time for ethics approval. - Writing aims that describe activity, such as studying a topic, rather than an answer that can be judged. Each makes the final evaluation harder to do fairly. A peer review of the proposal usually catches them early.

### 35.7 Supervisor agreement

Before starting, agree the proposal with your supervisor in writing, including what counts as success and what happens if a key dependency fails — for example, if a library needed for the lab is not released. A one-paragraph fallback plan prevents a late scramble and makes it clear that a well-documented negative result is an acceptable outcome.

The agreement is revisited if the scope changes. Note any change in a dated addendum signed by both of you, so that the final evaluation is measured against the agreed version rather than the first draft.

### Exercises

- **EX069 — Success criteria.** Rewrite "the tool should work well" as two observable success criteria. Rubric: 3 = measurable, relevant criteria.
- **EX070 — Risk table.** List three project risks for the worked proposal with mitigations. Rubric: 3 = plausible risks and mitigations.

### Synthesis

A capstone proposal states a decision-relevant problem, bounded scope, lawful evidence, observable success criteria and managed risks.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) apply course skills in a supervised placement or community project; (2) work within an organisation's authorization and change processes; (3) communicate with non-specialists; and (4) reflect on practice using evidence.

### 36.1 Forms of practice

Placements might involve supporting an organisation's cryptographic inventory, writing internal guidance on PQC, testing a library upgrade in a lab, or helping a community organisation (a library, charity or small business) understand which of its services rely on vendors that must migrate. The learning comes from doing real work under real constraints.

Whatever the setting, agree at the start what you will produce and who will use it. A short inventory or a page of guidance that a team actually adopts teaches more than a large report nobody reads, and it gives you concrete evidence for your practice log.

### 36.2 Working within processes

Organisations have change control, security policies and supervisors. Follow them. Obtain written scope from your supervisor. Never run tools on production systems without approval; never take data home. If you notice something serious — for example, an exposed private key — report it through the organisation's process immediately.

Ask early how changes are approved, because a lab test that seemed simple may need a ticket and a review. Keep copies of approvals with your log. Working inside these processes is part of the learning: a migration in a real organisation moves at the speed of its change control.

### 36.3 Communication

Non-specialists need plain language. Instead of "migrate KEX to ML-KEM-768 hybrid", say "update how our systems agree secret keys so that recorded traffic stays protected even if powerful quantum computers are built". Check understanding by asking what the listener will do next.

A short written summary after a meeting helps too. It records what was agreed in words both sides understand, and it lets the listener correct a misunderstanding before it turns into wrong action. Keep technical detail in an appendix for those who want it.

### 36.4 Reflection

Keep a practice log: what you did, what evidence you produced, what surprised you, what you would do differently. Link entries to course concepts. Reflection turns experience into transferable skill.

Write entries soon after the work, while details are fresh, and keep them brief. Include mistakes and what you learned from them, since these are often the most useful entries. Over a placement, the log shows how your judgment developed, which is exactly what assessors look for. Note any evidence you can share and anything you must keep confidential.

### 36.5 Worked example

A student volunteers with a small (synthetic) community credit cooperative that uses a hosted banking platform. With the manager's written approval, the student reviews the vendor's public security documents and contract, finds no PQC roadmap, and drafts three questions for the next vendor meeting: which algorithms protect data in transit, when hybrid key exchange will be supported, and whether the vendor maintains a cryptographic inventory. The student also writes a one-page plain-language explainer for the board.

The questions were agreed with the manager first.

### 36.6 Practical activity

Write a scope agreement and the first three entries of a practice log for your placement or a simulated one.

The scope agreement should name your supervisor, the systems or documents you may access, what you will produce, and what you must not do. Each log entry should record the task, the evidence produced and one reflection. If you are simulating a placement, base it on the HCU case and state which parts are invented. Ask your supervisor to sign the agreement.

### 36.7 Common errors and limits

- Acting outside agreed scope to be helpful.
- Using jargon with non-specialists.
- Logs that list tasks without evidence or reflection.

- Keeping notes only in your head, so that nothing can be shown later. - Promising results the organisation did not ask for. - Taking copies of documents outside the agreed scope. - Assuming silence means approval. - Forgetting to close the placement with a handover of what you produced. Each makes it harder for the organisation to trust the work or use it. A weekly check against the scope helps.

### Exercises

- **EX071 — Plain language.** Explain "signature migration" to a non-technical board member in three sentences. Rubric: 3 = accurate, jargon-free, actionable.
- **EX072 — Escalation.** You find a private key in a shared folder during a placement. List your next four actions. Rubric: 3 = stop, report via process, do not copy/use, document.

### Synthesis

Supervised practice applies course skills within authorization and change processes, with plain communication and evidence-based reflection.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critically appraise sources on quantum computing and PQC; (2) distinguish peer-reviewed results, standards, preprints, vendor material and journalism; (3) assess claims about timelines and performance; and (4) give and receive structured peer critique.

### 37.1 Source types

*Standards* (FIPS, SP, RFC) are authoritative for what algorithms are and how to use them, with status noted. *Peer-reviewed papers* carry expert scrutiny but can still be wrong. *Preprints* such as arXiv or IACR ePrint papers are early and unreviewed, though many are later published; Gidney (2025) was a preprint when cited here. *Vendor material* has commercial interests. *Journalism* simplifies and often misreports. Weight evidence accordingly and say which type you rely on.

A claim supported by two independent sources of different types is stronger than one repeated by many sources that copy each other.

### 37.2 Appraising timeline claims

Ask: who made the estimate, on what assumptions (error rates, qubit counts, algorithms), when, and what range they give? Distinguish resource estimates ("how many qubits would it take") from forecasts ("when will they exist"). Expert surveys provide distributions, not dates.

Check whether a newer estimate has replaced the one you are reading, since resource estimates have fallen sharply over time. When a news story gives a single year, trace it back to the original source and see what range and assumptions it actually stated. For HCU, timeline claims feed into Mosca's inequality, so a careless date can change which flows look urgent.

### 37.3 Appraising performance claims

Ask: what hardware, which implementation, which parameter set, what was measured (operations per second, handshake latency, bytes), and with what variability? Benchmarks of optimised assembly do not predict constrained-device behaviour.

Ask also whether the result has been reproduced by someone other than the authors. A performance figure measured on a server tells you little about a card terminal. For HCU, the useful benchmarks are those run on the same appliances and links used in the branches, so lab measurements often matter more than published tables.

### 37.4 Structured critique

Critique follows a structure: summarise the claim fairly; assess evidence; identify assumptions; note what would change the conclusion; suggest improvements. Critique the work, not the person.

A fair summary is the hardest step and the most important: if the author would not recognise your summary, the rest of the critique will miss. End with what the source does establish, not only its weaknesses. A critique that finds nothing useful in a source should say why it was considered at all.

### 37.5 Worked example

A vendor whitepaper states "our QKD system makes your network quantum-proof". Appraisal: vendor source; "quantum-proof" is not a defined property; QKD still needs authentication, which the paper does not address; NSA guidance does not support QKD for national security systems; the claim lacks scope. Conclusion: not adequate evidence for HCU's decision.

The appraisal still notes what the paper does show: the vendor has working hardware, which may matter for niche links. It simply does not answer HCU's question. A request for an independent evaluation would be the next step.

### 37.6 Practical activity

In groups, appraise one preprint, one standard and one news article on PQC using the frameworks above; present a two-minute critique each.

Use the same structure for each source: a fair summary, the evidence offered, the assumptions, and what would change the conclusion. Note the source type and how much weight it deserves. Then compare the three critiques as a group: did the standard, the preprint and the news article agree, and if not, which should a decision-maker trust and why?

### 37.7 Common errors and limits

- Treating preprints as settled.
- Rejecting vendor material outright rather than weighting it.
- Critiquing tone instead of evidence.

- Quoting a single year for quantum arrival without the range behind it. - Citing a secondary summary when the original is available. - Ignoring the date of a source in a field where estimates change quickly. - Accepting a benchmark without asking what hardware it ran on. Each lets weak evidence shape a decision it cannot support. Keep a short appraisal note for each source you rely on.

### Exercises

- **EX073 — Source weighting.** Rank by authority for "ML-KEM-768 ciphertext size": a news article, FIPS 203, a vendor blog, a peer-reviewed benchmark. Rubric: 3 = FIPS 203 first, reasons for others.
- **EX074 — Timeline claim.** Appraise: "Experts agree RSA will be broken in 2029." Rubric: 3 = identifies false consensus, missing assumptions, forecast vs estimate.

### Synthesis

Evidence review weighs sources by type and interest, interrogates assumptions behind timeline and performance claims, and critiques work constructively.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) execute your capstone plan with milestones; (2) maintain reproducible code and lab records; (3) manage scope changes; and (4) document decisions as you go.

### 38.1 Executing the plan

Work in milestones: environment ready; first data or model; first analysis; full analysis; draft report. At each milestone, compare progress with the plan and record deviations. Small, frequent progress beats large late pushes.

Plan a buffer before the draft report milestone, since analysis almost always takes longer than expected. If a milestone slips, say so early and adjust what follows, rather than compressing the writing into the final weeks. A short note at each milestone, saying what was done and what is next, makes later reporting much easier.

### 38.2 Reproducibility

Use version control for code, configuration and text. Record environment versions. Write scripts that regenerate every figure and table from raw inputs. Keep synthetic data generators with fixed seeds so results can be reproduced exactly, as the labs in this book do.

Test reproducibility yourself before submission by cloning the repository into a clean environment and running everything from scratch. Anything that fails there would fail for an examiner too. Record the date and result of that check in your lab record, so you can show it was done.

### 38.3 Scope changes

Discoveries change plans. If a vendor's documentation shows that a planned lab is impossible, record the change, its reason and its effect on aims, and agree it with your supervisor. Silent scope changes make evaluation unfair and conclusions unclear.

Keep scope changes in the same place as decision records, so that the final report can list them together. A change that narrows the work is acceptable if it is explained; a change hidden in the results is not. Your evaluation will be judged against the agreed scope, so make sure it is current.

### 38.4 Decision records

Keep short decision records: context, options, decision, consequences. "We chose ML-KEM-768 rather than -1024 for the lab because the synthetic HCU policy requires category 3 and the TLS group uses -768." Decision records make the final report easier to write and defend.

Write each record at the time of the decision. A record written months later tends to justify the outcome rather than explain the reasoning, and reviewers can usually tell the difference. For the capstone, a folder of dated one-page records is enough.

### 38.5 Worked example

The capstone from Chapter 35 builds a 60-asset synthetic HCU CBOM generator with a fixed seed, a ranking script sweeping *z* from 10 to 25 years and a report generator. At milestone 3 the student finds that the top-five ranking changes at *z* = 12 because member records enter. Decision record: report the change as a finding and add a sensitivity figure rather than adjusting assumptions to make the ranking stable.

The sensitivity figure later became one of the main results of the capstone. It was kept in the final report.

### 38.6 Practical activity

Set up your repository with code, data generator, lab record template and decision-record folder; complete your first milestone review.

The milestone review should compare what you planned with what you have done and record any changes. Check that a fresh clone of the repository can run the data generator and reproduce the first results. If it cannot, fix that before going further, because the problem only grows as more code and data are added. Then plan the second milestone with dates.

### 38.7 Common errors and limits

- Unversioned work.
- Figures made by hand that cannot be regenerated.
- Adjusting assumptions to obtain a preferred result.

- Leaving decision records until the end, when reasons are forgotten. - Changing scope without recording it. - Keeping raw data only on one laptop. - Skipping milestone reviews when work is going well, which is when small problems are easiest to fix. Each makes the final report harder to write and harder to defend. Most can be avoided with a fixed weekly routine of commits, notes and a brief check against the plan.

### 38.8 Working with supervisors

Share milestone reviews with your supervisor briefly and regularly: what was done, what was learned, what is blocked and what decision you need. Supervisors can only help with problems they know about, and a short written update creates a record that later shows how the work evolved.

Keep the updates in the repository. A good update fits in a few lines and ends with a clear question when you need a decision. Record the answer in your decision records, so that agreed changes to method or scope are visible later and are not reopened at the evaluation stage.

### Exercises

- **EX075 — Decision record.** Write a decision record for choosing a synthetic dataset over real data. Rubric: 3 = context, options, decision, consequences.
- **EX076 — Reproducibility audit.** List five checks a peer should run to confirm your capstone is reproducible. Rubric: 3 = five concrete checks.

### Synthesis

Milestones, version control, reproducible scripts, recorded scope changes and decision records turn a capstone plan into credible work.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate your capstone against its success criteria; (2) analyse limitations and threats to validity; (3) seek and respond to independent review; and (4) state what remains uncertain.

### 39.1 Against the criteria

Return to the success criteria in your proposal and assess each: met, partly met or not met, with evidence. If criteria changed, explain why. Evaluation is honest when it reports partial success clearly.

For each criterion, point to the evidence: a test run, a figure or a reviewer's comment. A criterion that cannot be assessed should be listed as such with the reason. Examiners respect a clear account of what was and was not achieved more than an evaluation that claims everything worked.

### 39.2 Limitations

Name limitations by type: data (synthetic, small sample), method (emulated networks), scope (only key exchange), and time (standards status as of a date). For each, state the likely effect on conclusions. Limitations are not apologies; they are the boundary of what your evidence supports.

Be specific about the direction of each effect where you can: for example, emulated networks may understate latency on the worst branch links. Where you cannot say which way a limitation pushes the result, say that too.

### 39.3 Independent review

Ask a peer or supervisor to rerun part of your work and challenge your conclusions. Record their comments and your responses. Reviewers often find unstated assumptions — for example, that all branches use the same appliance.

Give the reviewer a clear task, such as rerunning one figure from the repository and checking one conclusion. Their result is evidence about reproducibility; their challenge is evidence about the strength of your argument. Report disagreements you could not resolve rather than leaving them out.

### 39.4 Residual uncertainty

Close with what remains uncertain: quantum timelines, future standards (FN-DSA, HQC), vendor delivery. Explain how a reader should update your conclusions if these change.

For each uncertainty, say which conclusion it affects and in which direction. For example, an earlier quantum timeline would make more flows urgent but would not change which lead the ranking. This lets readers apply your work after the assumptions have moved, instead of discarding it. Date the statement, because what counts as uncertain in standards and products changes from year to year.

### 39.5 Worked example

Evaluation of the CBOM capstone: criterion 1 (reproducible tool) met — a peer reran it and obtained identical output; criterion 2 (stable ranking for *z* 10–25) partly met — stable for *z* ≥ 13, changes below; interviews (3) support relevance but are too few to generalise. Limitation: synthetic data may understate unknown assets, which in real inventories are often 20–40 % (an assumption to verify). Reviewer comment: the model ignores partner-controlled segments; response: added as future work with a sketch.

The evaluation reports each finding against the criteria agreed in the proposal.

### 39.6 Practical activity

Write your evaluation section and ask a peer to rerun one result.

Assess each success criterion with evidence, name the limitations by type and their likely effect, and record what remains uncertain. Give your peer clear instructions and a time limit, record whether they reproduced the result exactly, and note any step that confused them. Fix the instructions where needed, then add their comments and your responses to the evaluation. Keep the evaluation within two pages and put the detailed evidence in an appendix where readers can find it.

### 39.7 Common errors and limits

- Declaring success without evidence per criterion.
- Hiding limitations.
- Ignoring reviewer findings.

- Reporting only the results that support the conclusion. - Treating a limitation as a reason to dismiss the work rather than to bound it. - Calling a criterion met when the evidence is partial. - Asking reviewers who are unlikely to challenge you. - Leaving uncertainties undated. Each makes the evaluation less useful to the reader who needs to act on it. An independent reviewer helps to catch most of these. Ask for one early.

### 39.8 Learning from the evaluation

End the evaluation with lessons for the next project: which method choices worked, which assumptions were weakest, and what you would measure first if you started again. These lessons are useful to the organization and to future students, and they show examiners that you understand the work's place in a continuing programme rather than treating it as finished.

Keep the lessons brief and specific. In the CBOM capstone, for example, the weakest assumption was the share of unknown assets, so the first lesson was to measure it early in any real inventory before trusting the ranking.

### Exercises

- **EX077 — Partial success.** Write an evaluation sentence for a criterion that was partly met. Rubric: 3 = status, evidence, reason.
- **EX078 — Limitation effect.** For "emulated network instead of real branches", state the likely direction of bias on latency results. Rubric: 3 = underestimates tail latency/middlebox effects, explained.

### Synthesis

Evaluation compares results honestly with criteria, names limitations and their effects, incorporates independent review and states residual uncertainty.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) structure a bachelor's thesis; (2) present findings to technical and non-technical audiences; (3) defend choices under questioning; and (4) hand over work so others can continue it.

### 40.1 Thesis structure

A thesis contains: abstract; introduction with problem and questions; background with sourced concepts and standards status; method; results; discussion including limitations; conclusion; references; appendices with code and lab records. Each chapter should be traceable to evidence. Label all synthetic data clearly in text and captions.

Keep the background short and focused on what the reader needs for your question; a full history of quantum computing is rarely necessary. Make the discussion answer the research questions directly, in the same order they were asked.

### 40.2 Presentation

Prepare two versions: a technical talk with method and results, and a short decision-oriented summary for non-specialists. Open with the question and the answer; then show evidence; end with what the audience should do. Use one idea per slide and readable figures.

Rehearse both versions with someone outside the field and note where they get lost. A figure that needs a minute of explanation is usually too complex for a slide. Keep backup slides with the detailed evidence for questions, and end on the decision you want the audience to take rather than on a summary of methods.

### 40.3 Defence

Expect questions on assumptions ("why *z* from 10 to 25?"), method ("why paired design?"), standards ("is IR 8547 final?") and ethics ("how did you obtain data?"). Answer directly, admit uncertainty, and point to evidence. If you do not know, say so and explain how you would find out.

Prepare by listing the questions you would ask if you were the examiner, especially about your weakest assumptions. Bring the lab records and decision records, so that you can show evidence rather than recall it. A calm, honest answer to a hard question counts for more than a polished answer to an easy one.

### 40.4 Handover

Leave a README explaining how to run the code, regenerate results and extend the work, plus a list of open questions. Quantum readiness depends on continuity; your work is most valuable when someone else can build on it.

Test the README by asking someone who has not seen the project to follow it. Include the versions of every tool used and the date of the standards status you relied on. For HCU, the handover would go to the team running the migration, so the open questions should be written as decisions they will face.

### 40.5 Worked example

The CBOM capstone presentation opens: "Which of HCU's cryptographic flows should migrate first? Under every quantum timeline from 13 to 25 years, the same five flows lead, headed by mortgage archive transfers." The non-specialist version ends: "Protect the branch connections carrying mortgage files within a year; plan certificate changes next." In the defence, an examiner asks why category 3 was assumed; the student cites the synthetic policy and FIPS 203's category mapping, and explains the effect of choosing category 5.

Both versions used the same figures.

### 40.6 Practical activity

Deliver a ten-minute presentation and a two-minute summary; answer three prepared questions from a peer acting as examiner.

Time both versions and cut anything that runs over. The peer should ask at least one question about assumptions and one about method, and should note any answer that was unclear. Afterwards, revise the slide or explanation that caused the most difficulty and record the change in your practice log, together with what you would do differently next time. Keep the peer's notes with your log.

### 40.7 Common errors and limits

- Results without the question.
- Defensiveness under questioning.
- No handover materials.

- Overloading slides with tables that cannot be read from the back of the room. - Claiming more certainty than the evidence supports when under pressure. - Answering a different question from the one asked. - Leaving code and data without instructions, so the work ends with the student. Each reduces the value of a capstone that may otherwise be strong. A practice run with a peer exposes most of them in time. Schedule it a week ahead.

### Exercises

- **EX079 — Abstract.** Write a 120-word abstract for the CBOM capstone. Rubric: 3 = problem, method, result, limitation, implication.
- **EX080 — Defence answer.** Answer: "Isn't this pointless if quantum computers never arrive?" Rubric: 3 = HNDL uncertainty argument, agility benefits, cost proportionality.

### Synthesis

A thesis traces every claim to evidence; good presentations lead with question and answer; good defences admit uncertainty; good handovers let others continue.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Numbers about HCU are synthetic.

**EX001.** log₂(10^24) = 24 × 3.32 ≈ 79.7 → about 80 bits; adding 2^20 gives about 100 bits.

**EX002.** Base: *n* = 1 needs one evaluation, h₁ = H(s). Step: if h_k needs *k* evaluations, h_{k+1} = H(h_k) needs exactly one more, *k* + 1. Conclusion: by induction h_n needs *n* evaluations for all *n* ≥ 1.

**EX003.** Hardware: the card chip and ATM encrypting PIN pad hold keys (vendor/card issuer). Firmware: signed ATM software verified at boot (ATM vendor). OS/library: TLS or IPsec from ATM to the switch (HCU network team/vendor). Application: authorization message MAC and host response verification (payment switch operator).

**EX004.** Quantum advantage exists only for specific structured problems such as period finding and unstructured search. A statement batch job is ordinary data processing — reading, formatting and writing records — dominated by I/O and simple arithmetic. No known quantum algorithm offers a meaningful speed-up, and today's quantum hardware would be far slower.

**EX005.** `str(b"abc")` produces the six-character text `b'abc'`, whose UTF-8 bytes differ from the three bytes `abc`, so the digests differ. Bug class: text/bytes type confusion (encoding error), which silently breaks interoperability.

**EX006.** `def h(b): return hashlib.sha3_256(b).hexdigest()` with `assert h(b"") == "a7ffc6f8…8434a"`. The test fails if the function hashes text, uses SHA-256 instead or truncates.

**EX007.** C: "HCU's internal certificate authority is exposed to future signature forgery." E: "Its root certificate, exported on (date), uses RSA-2048 with a validity to 2044." R: "A cryptographically relevant quantum computer could derive the RSA private key with Shor's algorithm and issue trusted certificates, and the root's validity extends beyond plausible arrival dates, so migration planning should start now."

**EX008.** "FIPS 206, which will specify FN-DSA (derived from Falcon), was still in development on 12 October 2026; it imposes no requirements yet. Final NIST signature standards are FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA)."

**EX009.** Archived VPN traffic: HNDL (recorded now, decrypted later). ATM firmware signing: forge-later (forged updates need a CRQC at attack time, but devices are long-lived). AES-256 database encryption: neither (Grover-adequate). TLS session to the mobile app: HNDL if session data stays sensitive beyond *z*; also forge-later for its certificate.

**EX010.** Asset: HCU internal CA root and issued certificates. Threat: future adversary with a CRQC. Vulnerability: RSA-2048 root key. Impact: forged certificates for internal services and VPNs, enabling impersonation. Likelihood: low today, rising with quantum progress; root validity to 2044 overlaps plausible arrival. Controls: plan post-quantum root (ML-DSA), shorten validity, distribute new root to relying parties early, inventory dependants.

**EX011.** 3¹ = 3, 3² = 2, 3³ = 6, 3⁴ = 4, 3⁵ = 5, 3⁶ = 1 (mod 7): order 6.

**EX012.** (2 + *x*)(3 + *x*³) = 6 + 3*x* + 2*x*³ + *x*⁴ = 6 + 3*x* + 2*x*³ − 1 = 5 + 3*x* + 2*x*³ → [5, 3, 0, 2].

**EX013.** TLS 1.3: (EC)DHE key exchange; certificate signatures (RSA/ECDSA) with CertificateVerify. IKEv2: Diffie–Hellman (often ECP groups); certificates or pre-shared keys with signatures/MACs. SSH: ECDH/curve25519 key exchange; host key signatures (Ed25519, ECDSA, RSA) and user keys.

**EX014.** 1,216 − 32 = 1,184 bytes more (the ML-KEM-768 encapsulation key, FIPS 203; share sizes from RFC 10024).

**EX015.** Reject: 1,951 bytes (short); 1,953 bytes (long); an ML-DSA-44 key (1,312 bytes) presented as ML-DSA-65; a key with wrong algorithm identifier/encoding wrapper; empty input. Any four distinct cases.

**EX016.** Counting empty fields as classical makes the inventory look more complete and more uniformly classical than it is, hiding assets whose cryptography nobody knows. Decision-makers then under-fund investigation of the unknown items, which often include the hardest devices.

**EX017.** `SELECT name FROM data_class WHERE confidentiality_years > 10 AND transfer_channel IN ('vpn-ecdh', 'tls-ecdhe', 'rsa-kex');`

**EX018.** Card authorisations: retention ~7 years (disputes), confidentiality ~2–3 years (until card expiry). Mortgage files: retention ~30 years, confidentiality ~30 years or more (personal financial data). The difference is because harm from disclosure ends when credentials expire for cards, but not for life-history data.

**EX019.** Missing: which systems; which techniques (passive/active); time window; data handling; contacts and stop conditions. Any three.

**EX020.** Reproduce in an isolated lab; record versions and evidence; report privately to the vendor's security contact; agree a disclosure timeline (e.g. 90 days); inform HCU's security office and apply mitigations (monitoring for fallback); publish an advisory jointly after a fix or the deadline.

**EX021.** It ignores the OS provider, so OS upgrades and system crypto policies do not change it; its vendor or developer owns the change; it must be tested and released separately, and its version must appear in the inventory.

**EX022.** Firmware is signed rarely by a controlled signer that can keep state in an HSM, and verification only needs small code. A web server signs constantly, may run on many replicas and restore from backups, so state reuse — fatal for LMS/XMSS — becomes likely.

**EX023.** 2^−30 ≈ 9.31 × 10^−10; × 10^12 ≈ 931 failures.

**EX024.** True attempts: 10^8/10^6 = 100, detected ≈ 99. False alerts: 1 % of ~10^8 ≈ 10^6. Fraction true ≈ 99/1,000,099 ≈ 0.01 %.

**EX025.** Passwords: not directly (symmetric/hash storage; Grover-adequate). Passkeys: yes, ECDSA signatures (forge-later). SSO tokens: yes, RSA/ECDSA signatures but short-lived, lower priority. Internal root CA: yes, long-lived signature key, high priority.

**EX026.** Verifiers build chains to a trusted root. A post-quantum leaf signed by a post-quantum intermediate chains to a post-quantum root; if relying parties do not trust that root, validation fails, so the root must be distributed to trust stores first.

**EX027.** Health information in hardship cases and identity documents; both remain harmful for a lifetime. Recorded traffic carrying them can be decrypted after HCU deletes its copy, so HNDL exposure is governed by harm lifetime, not retention.

**EX028.** Needed: host/service identifier, protocol, offered and selected groups, signature algorithm, certificate validity, observation date, method. Not collected: payloads; client IP addresses of members (or only truncated); session identifiers.

**EX029.** "Configuration review of HCU's certificate inventory (1,240 certificates from the CA database, 15 March) shows 95 % issued by CAs whose software supports ML-DSA issuance; certificates from external CAs (not in the database) are excluded."

**EX030.** Indicator: median time from approved algorithm change to production for a service class. Measure from change tickets (approval to deployment timestamps) for test changes such as enabling a new group. Limitation: test changes may be easier than real ones; small samples.

**EX031.** 1) Branch → data centre (WAN, untrusted boundary, 30-year data, ECDH). 2) Core banking → archive key wrapping (RSA-OAEP, long-lived keys; exposed if copied). 3) Gateway → core (internal, classical; lower interception likelihood). 4) Mobile → gateway (already hybrid; authentication remains classical).

**EX032.** Central crypto policy configuration; algorithm identifiers stored with ciphertexts/keys; libraries/providers supporting several KEMs behind one interface; message formats with length fields tolerating larger keys; tests runnable for any configured algorithm.

**EX033.** Password storage: password-hashing function (e.g. PBKDF2 or a memory-hard function). Server integrity: HMAC-SHA-256. Session key agreement: hybrid X25519MLKEM768 (FIPS 203 + RFC 10024). Document approval: ML-DSA-65 (FIPS 204) or hybrid with ECDSA during transition.

**EX034.** Each signature reveals one secret per bit position. Two different message hashes differ at ~half the positions, revealing both secrets there (118/256 in Lab L). An attacker can sign any new message whose hash bits at the remaining 138 positions match what was revealed, which takes about 2^138 hash attempts; each further reuse roughly halves the unmatched positions, so after a few reuses forgeries become easy.

**EX035.** "What share of HCU's 25 critical vendors have published a PQC roadmap with dates for hybrid key exchange, measured by review of their public documents and questionnaire responses by 30 June?"

**EX036.** Internal: drift in lab conditions over time (mitigated by alternating order), or caching effects. External: emulated loss and latency do not reproduce real branch proxies and radio conditions.

**EX037.** Late when *x* + *y* > *z*: 13 > *z*, so for *z* < 13 years.

**EX038.** PQC runs on existing networks and devices, while QKD needs dedicated optical links and trusted nodes across 40 branches; QKD still requires classical authentication and is not supported by NSA guidance for national security systems, while PQC is standardised in FIPS 203/204/205.

**EX039.** Falling estimates → plan with swept timelines and start early. Rainbow/SIKE → hybrid deployment. KyberSlash → vetted, updated libraries and version tracking. Chrome rollout → staged rollout with monitoring.

**EX040.** If *z* may be shorter than expected, the only variable HCU controls is *y*. Starting earlier and building agility reduces *y* for this and future migrations, keeping *x* + *y* below a wider range of *z*.

**EX041.** Mobile TLS: HNDL-exposed (7-year data plausibly beyond lower *z*), plus forge-later for authentication. AES-256: Grover-adequate. RSA code signing for internal tools: forge-later-exposed (moderate). Cash-dispenser cryptography: unknown — investigate.

**EX042.** (a) Protection: full hybrid PQ/T key exchange; effort: firmware upgrade and testing on 40 appliances; residual: authentication classical. (b) Protection: PQ-resistant if PSKs are strong and secret; effort: key distribution and rotation; residual: key-management risk, scaling and rotation burden.

**EX043.** Eight assets, three unknown: 3/8 = 37.5 % ≈ 38 %.

**EX044.** HCU controls the gateway configuration and its app networking library choices; phone OS support, CDN support and core vendor support depend on others, so the phone→CDN and gateway→core segments need partner action.

**EX045.** Without error, *b* = *As* is a linear system solvable by Gaussian elimination. With small error, elimination amplifies the noise and fails; recovering *s* becomes finding a close lattice point in high dimension, for which the best known classical and quantum algorithms take exponential time.

**EX046.** ML-KEM-1024: encapsulation key 1,568 bytes; ciphertext 1,568 bytes (FIPS 203).

**EX047.** A future quantum computer breaking the traditional component (X25519); an unexpected classical cryptanalytic or implementation break of the new PQ component.

**EX048.** Family: algorithm + governance. Control: create an ML-DSA root, distribute to relying parties, issue PQ intermediates, shorten classical root validity. Effect: removes forge-later exposure once dependants migrate. Owner: PKI team. Residual: legacy clients unable to verify ML-DSA; review annually.

**EX049.** Run the harness against a wrong implementation (e.g. SHA-256 instead of SHA3-256) or alter one hex digit of the expected value; the harness must print FAIL.

**EX050.** Constant-time behaviour and side-channel resistance; correct key generation and storage; correct integration in protocols (negotiation, error handling); randomness quality.

**EX051.** The KDF input concatenates both secrets; an attacker who breaks X25519 learns one secret but not the ML-KEM secret, so the KDF output remains unpredictable to them.

**EX052.** LMS (SP 800-208) in an HSM: few signatures, state easily controlled, small signatures and fast verification on the ATM; alternatively SLH-DSA for statelessness at the cost of larger signatures. Either is conservative (hash-based).

**EX053.** Server preference order places a classical group first and the server honours its own preference, or clients do not support the hybrid group; the configuration shows it "offered" while negotiations select classical.

**EX054.** Test case/objective; client and server versions; configuration hash; observed output (selected group); date, tester and evidence location.

**EX055.** Mode: PQ-signed chain rejected. Effect: service outage for legacy clients. Cause: client libraries lacking ML-DSA. Detection: validation errors in client telemetry and help-desk tickets. Priority: high severity, medium likelihood, good detection → high; control via dual certificates or staged issuance.

**EX056.** Security lead convenes the crypto decision group; assess the weakness against deployed parameter sets and hybrids; change policy to remove or deprioritise the algorithm where configuration allows; schedule releases and hardware work; communicate with staff, vendors, partners and regulators, and record the decision.

**EX057.** The Wilson upper bound for 3/5,000 is about 0.18 %, above the 0.09 % threshold (baseline 0.05 % + 0.04 %); the sample is too small to show the rate is within budget.

**EX058.** Negotiated groups per service/site; fallback share; handshake failure rate by error type; certificate validation errors. Alert: fallback share at any branch above 1 % for 24 hours.

**EX059.** Remove one ML-DSA-65 signature: 21,249 − 3,309 = 17,940 bytes.

**EX060.** Chain depth 2 (deeper chains increase bytes); ~400 bytes of other fields (more extensions increase); two SCTs (fewer reduce); no compression (compression barely reduces PQ keys). Also excludes key exchange bytes.

**EX061.** The restored signer reuses one-time keys already used yesterday; two signatures with the same one-time key reveal secrets and enable forgeries. Prevention: HSM-held state that cannot roll back, reserved index ranges, no backup restore of state without advancing.

**EX062.** Renewal adds a new timestamp proving the document and its original signature existed at that time; this proof is only trustworthy if the original algorithm was still unbroken then. After a break, forgeries could be timestamped too.

**EX063.** Exposure: RSA root valid to 2044 underpins all internal TLS and VPNs (forge-later). Options: PQ root now with staged issuance; wait for vendor CA upgrade. Recommendation: build ML-DSA root in 2027, distribute to trust stores, migrate intermediates by 2029. Cost: CU 90–150k. Residual risk: legacy devices that cannot verify ML-DSA.

**EX064.** "The supplier shall support configuration-based replacement of cryptographic algorithms, including NIST FIPS 203 and FIPS 204 algorithms, within 12 months of request." "The supplier shall provide and keep current a cryptographic inventory of the delivered product, listing algorithms, parameters and libraries."

**EX065.** Each client runs both conditions, so differences between clients (hardware, OS, network position) cancel in the comparison; this reduces variance and removes confounding between client and condition.

**EX066.** Question; design; setting; systems/participants; procedure; measures; analysis; limitations. Examples: setting — emulated branch WAN 40 ms/1 % loss; measures — handshake latency median and p99.

**EX067.** A: 4×0.2 + 4×0.2 + 4×0.15 + 3×0.3 + 4×0.15 = 3.70. B: 3×0.2 + 3×0.2 + 5×0.15 + 5×0.3 + 2×0.15 = 3.75.

**EX068.** "Partner compatibility": share of partner connections that would still work after the change, scored from partner questionnaires and lab interoperability tests.

**EX069.** "The tool reproduces the full report from raw inputs with one command in under five minutes." "On the synthetic model, the tool classifies 100 % of assets into an exposure class, with unknowns listed."

**EX070.** Interviews not available → use public case studies. Synthetic model unrealistic → calibrate with published inventory statistics. Scope creep → fixed milestone review with supervisor.

**EX071.** "Our systems prove who they are using digital signatures. Future quantum computers could forge today's signatures, so we will gradually switch to new signature methods that NIST standardised in 2024, starting with the systems that are trusted longest. This needs planning because many devices and partners must accept the new signatures."

**EX072.** Stop and do not copy, use or move the key; report immediately to the supervisor/security contact through the organization's process; document what you saw and when; follow instructions (e.g. revocation and rotation by owners).

**EX073.** FIPS 203 (primary standard) first; peer-reviewed benchmark second (verifiable, may report sizes); vendor blog third (interested, secondary); news article last.

**EX074.** No such consensus exists; surveys show wide disagreement. The claim gives no source, assumptions or range and confuses a forecast with a resource estimate. Rewrite as a sourced range.

**EX075.** Context: capstone needs inventory data; real HCU-like data is confidential. Options: real data under NDA; anonymised data; synthetic generator. Decision: synthetic with fixed seed. Consequences: reproducible and shareable; realism must be argued and limitations stated.

**EX076.** Fresh clone runs; versions pinned; one command regenerates all figures; fixed seeds give identical outputs; lab records match outputs.

**EX077.** "Criterion 2 was partly met: the top-five ranking was stable for *z* from 13 to 25 years but changed below 13 because member records (x + y = 13) entered; see Figure 4."

**EX078.** Emulation omits middleboxes and real radio/WAN variability, so it likely underestimates tail latency and failure rates.

**EX079.** (Example) "Organizations must decide which cryptography to migrate first as quantum computing advances. We built a lifetime-weighted cryptographic bill of materials for a synthetic 60-asset credit union and ranked flows with Mosca's inequality, sweeping the quantum timeline from 10 to 25 years. The top five flows, led by mortgage-archive transfers, were stable for timelines of 13 years or more; below that, member records joined. Three practitioner interviews supported the method's usefulness. Results depend on synthetic data and stated lifetimes. Organizations can adopt the method to prioritise hybrid key exchange on long-lived data flows before addressing signatures."

**EX080.** "Harvest-now-decrypt-later means recorded data is exposed if a capable machine ever arrives within its lifetime; we cannot know that it won't. The work also builds crypto-agility and inventory that pay off for any future algorithm change, and the first steps — hybrid key exchange on a few long-lived flows — are cheap relative to the potential harm."

## Forty-subject teaching route

This is the **bachelor's** course. It builds foundations (1–18) and then applies them to the synthetic **Harbourline Credit Union (HCU)**: scope and cases, system models, inventory, lattice methods, controls, labs, verification, failure analysis, operations, advanced cases, and research and capstone work (19–40).

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
- IETF RFCs: 8446 (TLS 1.3), 8784 (IKEv2 PSK mixing), 8879 (certificate compression), 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025); SP 800-56C Rev. 2. <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227> · <https://doi.org/10.6028/NIST.SP.800-56Cr2>
- NIST IR 8547 initial public draft (2024); CSWP 39 upd1. <https://doi.org/10.6028/NIST.IR.8547.ipd> · <https://doi.org/10.6028/NIST.CSWP.39-upd1>
- NSA. Quantum Key Distribution (QKD) and Quantum Cryptography (QC). <https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/>
- Regev, O. (2009). On lattices, learning with errors, random linear codes, and cryptography. *J. ACM* 56(6). <https://doi.org/10.1145/1568318.1568324>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
