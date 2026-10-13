# Cryptography and Trust Services: Engineering Course

- Language: English (`en`); course 123, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; eight offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students designing, building and operating cryptographic trust services for critical infrastructure.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: labs exist to understand and verify behaviour against standards and test vectors. Production systems use vetted libraries and hardware security modules; never roll your own cryptography. All people, organisations, keys and devices are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one engineering student over five years as she helps a water utility authenticate smart-meter readings and firmware: foundations in mathematics, physics and programming; systems, networks and security; then requirements, models, threats, methods, studios, implementation, verification, operations, post-quantum migration, a capstone revocation pipeline, a recovery trial, an evidence dossier, a thesis and a defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Aiyana Torres** | Engineering student | Invented |
| **Marcus Webb** | Utility engineer and mentor | Invented |
| **Halden Institute of Engineering** | Fictional institute | Invented |
| **Ridgeway Water Utility** | Fictional utility with 50,000 smart meters | Invented |

### Core sources

Katz and Lindell (3rd ed.); Boneh and Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); Menezes et al., [*Handbook of Applied Cryptography*](https://cacr.uwaterloo.ca/hac/); [FIPS 197](https://doi.org/10.6028/NIST.FIPS.197-upd1), [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4), [FIPS 186-5](https://doi.org/10.6028/NIST.FIPS.186-5), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204); [SP 800-57 Part 1](https://doi.org/10.6028/NIST.SP.800-57pt1r5); [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869), [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446). Full list in [References](#references).

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

You will (1) read growth rates as the language of cryptographic strength; (2) use logarithms to compare enormous quantities; (3) estimate exhaustive-search time for key lengths.

### 1.1 The case and why growth matters

Aiyana Torres is a first-year engineering student at the fictional Halden Institute of Engineering. Over five years she will help the fictional Ridgeway Water Utility design how its 50,000 smart water meters authenticate readings and accept firmware updates, mentored by utility engineer Marcus Webb. Every meter, key and figure in this book is synthetic. Calculus begins with rates of change, and cryptography depends on one rate above all: how fast the work to guess a key grows as the key gets longer. Linear growth adds a fixed amount per step; exponential growth multiplies. Key search is exponential, and that difference is why a few extra bits protect so much.

### 1.2 Logarithms tame huge numbers

A 128-bit key has 2^128 possible values, about 3.4 × 10^38, a number too large to picture. Logarithms turn multiplication into addition: log10(2^128) = 128 × log10(2), roughly 38.5. Aiyana learns to compare security levels by comparing exponents, not raw numbers. The derivative of 2^x is ln(2) × 2^x, so the growth rate is itself proportional to the current size, the signature of exponential behaviour. When engineers say a key length offers "128-bit security", they mean an attacker needs work on the order of 2^128 operations, and Katz and Lindell use the same convention when they define concrete security.

### Lab — Exhaustive-search time

```python
"""Exhaustive-search time for key lengths at a hypothetical 10^12 guesses per second (synthetic rate)."""
import math
RATE = 10**12
YEAR = 365.25 * 24 * 3600

def main():
    for bits in (40, 56, 80, 128):
        years = 2 ** (bits - 1) / RATE / YEAR  # expected half the space
        print(f"{bits:>3}-bit key: log10(years) = {math.log10(years):6.2f}")
    print(f"each extra bit multiplies work by {2 ** 1}; 10 extra bits by {2 ** 10}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_keyspace.py`. Verified output:

```text
 40-bit key: log10(years) =  -7.76
 56-bit key: log10(years) =  -2.94
 80-bit key: log10(years) =   4.28
128-bit key: log10(years) =  18.73
each extra bit multiplies work by 2; 10 extra bits by 1024
```

### 1.3 Reading the estimate

At a hypothetical trillion guesses per second, a 40-bit key falls in a fraction of a second (log10 of years about -7.8) and a 56-bit key, the length of the retired DES cipher, in about a day (log10 about -2.9). An 80-bit key needs around nineteen thousand years, and a 128-bit key about 10^18.7 years, far longer than the age of the universe. Each extra bit doubles the work and ten extra bits multiply it by 1,024. Aiyana notes that the rate is invented and that real attackers improve, which is why standards such as AES in FIPS 197 start at 128 bits rather than at the edge of feasibility.

### Worked example

Aiyana tabulates search times for 40, 56, 80 and 128 bits, compares them by their base-10 logarithms, and recommends that Ridgeway never accept meter keys below 128 bits.

> **Synthetic case.** Ridgeway, its meters and the guess rate are invented; FIPS 197 is the real AES standard.

### Errors and limits

Exhaustive search is only one attack; a long key does not help if it is stored badly or generated from a weak random source. Logarithmic estimates are orders of magnitude, not schedules.

### Exercises

- **EX001 — Exponential versus linear.** Why is key search described as exponential rather than linear in key length? *Rubric:* 3 = each extra bit doubles the number of keys, so work multiplies;; 2 = "grows fast";; 1 = linear answer;; 0 = none.
- **EX002 — Key-search logs.** Using the lab, give the base-10 log of expected years for 56-bit and 128-bit keys. *Rubric:* 3 = about -2.94 and 18.73;; 2 = one right;; 1 = wrong sign;; 0 = none.
- **EX003 — Why start at 128.** Why does Aiyana recommend at least 128-bit keys for meters? *Rubric:* 3 = 2^127 expected work is infeasible with margin; matches FIPS 197 minimum;; 2 = "safer";; 1 = 56 bits enough;; 0 = none.

### Synthesis

Calculus gives engineers the vocabulary of growth; exponential key spaces, compared through logarithms, explain why modern keys start at 128 bits.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) compute with modular arithmetic; (2) explain why modular inverses and Fermat's little theorem matter to public-key systems; (3) recognise why toy examples must never become real keys.

### 2.1 Clock arithmetic

Modular arithmetic works like a clock: numbers wrap around after reaching the modulus. Seventeen hours after 9 o'clock is 2 o'clock because 26 mod 24 equals 2. Public-key cryptography lives in this world. Aiyana practises addition, multiplication and exponentiation modulo n, and learns that Python's three-argument pow(b, e, n) computes b^e mod n efficiently by repeated squaring, without ever building the huge intermediate number. The Handbook of Applied Cryptography, chapter 2, collects these number-theoretic tools and is free online, which makes it her reference for definitions such as greatest common divisor and multiplicative inverse.

### 2.2 Inverses and Fermat

A number e has an inverse modulo m when gcd(e, m) = 1; the inverse d satisfies e × d mod m = 1, and the extended Euclidean algorithm finds it. Fermat's little theorem says that for a prime p and a not divisible by p, a^(p-1) mod p = 1. Together with Euler's generalisation, these facts explain why the textbook RSA construction can reverse an exponentiation with a second exponent. Aiyana treats this as understanding, not engineering: RFC 8017 shows that real RSA needs padding schemes such as OAEP and PSS, because the bare textbook operation leaks structure and is insecure.

### Lab — Toy modular arithmetic

```python
"""Modular arithmetic facts behind public-key cryptography, on toy numbers (never a real key)."""
from math import gcd
p, q = 61, 53            # textbook-sized primes, far too small for any real use
n, phi = p * q, (p - 1) * (q - 1)
e = 17

def main():
    d = pow(e, -1, phi)  # modular inverse (Python 3.8+)
    print(f"n={n} phi={phi} gcd(e,phi)={gcd(e, phi)} d={d} (e*d mod phi = {e * d % phi})")
    m = 65
    c = pow(m, e, n)
    print(f"toy m={m} -> c={c} -> back {pow(c, d, n)}")
    print(f"Fermat check: 7^(61-1) mod 61 = {pow(7, 60, 61)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_modular.py`. Verified output:

```text
n=3233 phi=3120 gcd(e,phi)=1 d=2753 (e*d mod phi = 1)
toy m=65 -> c=2790 -> back 65
Fermat check: 7^(61-1) mod 61 = 1
```

### 2.3 Reading the toy

With primes 61 and 53 the modulus is 3233 and phi is 3120. The exponent 17 shares no factor with 3120, so its inverse exists and equals 2753, and 17 × 2753 mod 3120 is 1. Raising 65 to the 17th power gives 2790, and raising 2790 to 2753 returns 65. Fermat's check prints 1 for 7^60 mod 61. Aiyana writes in red in her notes that these numbers can be factored instantly by hand, there is no padding and no randomness, and that Ridgeway will use vetted libraries implementing FIPS 186-5 or RFC 8032 signatures instead. Real RSA moduli today are at least 2048 bits, and key generation is left to audited libraries.

### Worked example

Aiyana computes the inverse of 17 modulo 3120, verifies Fermat's theorem for 7 and 61, and explains why the same arithmetic with real-sized numbers still needs standard padding.

> **Synthetic case.** The primes and message are textbook toys; RFC 8017 and FIPS 186-5 are the real standards.

### Errors and limits

Toy RSA is a teaching device. Copying it into software, even with large primes, produces an insecure system without padding, side-channel care and vetted key generation.

### Exercises

- **EX004 — Inverse condition.** When does an inverse of e modulo m exist? *Rubric:* 3 = when gcd(e, m) = 1;; 2 = coprime stated loosely;; 1 = always;; 0 = none.
- **EX005 — Toy values.** From the lab, give d and the ciphertext of 65. *Rubric:* 3 = d = 2753, c = 2790;; 2 = one;; 1 = other numbers;; 0 = none.
- **EX006 — Why padding.** Why is textbook RSA unsafe even with large primes? *Rubric:* 3 = no padding or randomness leaks structure; RFC 8017 requires OAEP/PSS;; 2 = "too simple";; 1 = it is safe;; 0 = none.

### Synthesis

Modular arithmetic, inverses and Fermat's theorem explain public-key mathematics, but real systems rely on standardised schemes and vetted libraries.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical signals to information leakage; (2) explain side channels such as timing and power; (3) connect physical randomness to key generation.

### 3.1 Computation is physical

Every computation draws current, takes time and emits heat and electromagnetic radiation. Aiyana's physics course connects this to security: a meter that processes a secret key may leak information through how long an operation takes or how much power it draws. These leaks are called side channels. They matter because Ridgeway's meters sit in basements and street pits where an attacker could attach probes. A mathematically strong algorithm can be broken in practice if its implementation leaks key bits through physics, which is why standards bodies and vendors test implementations, not just designs.

### 3.2 Timing and power

A timing side channel appears when execution time depends on secret data, for example a comparison that stops at the first wrong byte. Measuring many attempts can reveal how many leading bytes were correct. Power analysis records the current drawn during cryptographic operations; differences between processing a 0 bit and a 1 bit can, with statistics, reveal keys. Defences include constant-time code, masking and hardware designed to resist analysis. Aiyana learns that Python's hmac.compare_digest exists precisely so that comparing authentication tags takes the same time regardless of where they differ.

### 3.3 Physical randomness

Keys must be unpredictable, and unpredictability ultimately comes from physical noise such as thermal fluctuations or oscillator jitter. Hardware entropy sources feed deterministic random bit generators, specified in NIST SP 800-90A, which stretch a small, well-measured seed into many unpredictable bits. A meter that boots with the same state every time, without good entropy, may produce the same keys as thousands of other meters. Aiyana notes that operating systems expose vetted generators, and Python's secrets module uses them, so engineers should never invent their own random number routines for keys.

### Worked example

Aiyana lists three physical leaks for a street-pit meter (timing, power, electromagnetic emission) and maps each to a defence: constant-time comparison, masked hardware and shielding, plus vetted entropy for key generation.

> **Synthetic case.** The meter deployment is invented; SP 800-90A is the real NIST recommendation.

### Errors and limits

Side-channel resistance cannot be confirmed by reading code alone; it needs measurement on the real device. Physical entropy can fail silently, so generators must be health-tested.

### Exercises

- **EX007 — Side channel defined.** What is a side channel? *Rubric:* 3 = information leaked through physical effects like time or power rather than the algorithm's outputs;; 2 = "physical attack";; 1 = network attack;; 0 = none.
- **EX008 — Early-exit comparison.** Why does a byte-by-byte comparison that stops early leak secrets? *Rubric:* 3 = time reveals how many leading bytes matched;; 2 = slower;; 1 = no leak;; 0 = none.
- **EX009 — Role of SP 800-90A.** What does SP 800-90A specify and why does it matter to meters? *Rubric:* 3 = deterministic random bit generators seeded by entropy so meters do not produce identical keys;; 2 = randomness;; 1 = encryption;; 0 = none.

### Synthesis

Cryptography runs on physical devices; timing, power and entropy determine whether a sound algorithm stays secure in a basement meter.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) represent bytes, text and hexadecimal correctly; (2) use the standard library's hash functions; (3) avoid common encoding errors that break cryptographic checks.

### 4.1 Bytes are not text

Cryptographic functions operate on bytes, not characters. In Python, "litres" is text and b"litres" is bytes; converting between them requires an explicit encoding such as UTF-8. Aiyana's first bug comes from hashing a reading on one system with a different encoding from another, so equal readings produced different digests. She learns to fix one canonical encoding in the specification, to convert once at the boundary and to keep bytes everywhere inside. Hexadecimal is a display format for bytes: two hex characters represent one byte, which is why a 32-byte SHA-256 digest prints as 64 characters.

### 4.2 Using hashlib

The hashlib module provides SHA-256 and other functions from FIPS 180-4. A hash maps input of any length to a fixed-length digest; changing one bit changes about half the output bits. Aiyana writes small functions that hash a reading string and print the hexadecimal digest, then checks published test vectors from the standard to confirm she is calling the function correctly. She learns the difference between calling update repeatedly on a hash object, which hashes the concatenation, and hashing each piece separately, which gives different results that confused her first test.

### 4.3 Canonical formats

Two programs must agree byte for byte before hashes or signatures can match. Aiyana defines a canonical reading format for Ridgeway: fixed field order, semicolon separators, integer litres and timestamps in UTC with a trailing Z. She avoids floating-point litres because 18342.0 and 18342 would hash differently. She also avoids letting a dictionary's printing order define the bytes. This discipline anticipates later chapters, where readings are authenticated with HMAC and firmware with signatures; both fail, harmlessly but confusingly, if sender and receiver disagree about the exact bytes.

### Worked example

Aiyana fixes a failing test by encoding readings as UTF-8 once, using integer litres and UTC timestamps, then confirms her SHA-256 calls against a FIPS 180-4 test vector.

> **Synthetic case.** The reading format is invented for Ridgeway; FIPS 180-4 is real.

### Errors and limits

Hashing is not encryption: anyone can compute a digest. Mixing text and bytes silently changes results, so specify encodings explicitly.

### Exercises

- **EX010 — Hex length.** Why does a SHA-256 digest print as 64 hex characters? *Rubric:* 3 = 32 bytes, two hex characters per byte;; 2 = 64 bytes;; 1 = random;; 0 = none.
- **EX011 — Encoding bug.** What caused Aiyana's first mismatched digests? *Rubric:* 3 = different text encodings on two systems for equal readings;; 2 = encoding mentioned;; 1 = wrong algorithm;; 0 = none.
- **EX012 — Integer litres.** Why does the canonical format use integer litres? *Rubric:* 3 = 18342.0 and 18342 produce different bytes and digests;; 2 = floats imprecise;; 1 = style;; 0 = none.

### Synthesis

Correct cryptographic programming starts with bytes, explicit encodings, verified test vectors and a canonical format both sides agree on.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) explain cryptographic decisions to non-specialists; (2) write a decision record for a key-management choice; (3) avoid misleading security language.

### 5.1 Writing for the board

Ridgeway's board includes a farmer, a retired nurse and an accountant. Aiyana must explain why meters need authenticated readings. She starts with the decision needed, approve a budget for meter keys, then states the risk in plain words: without authentication, someone could alter readings and bills. She defines jargon once: a message authentication code is a short tag that proves a reading came from the meter and was not changed. Marcus Webb tells her the board does not need the mathematics, but it does need to know what could go wrong and what it costs to prevent.

### 5.2 Honest security language

Aiyana avoids words such as "unbreakable" or "military-grade", which promise more than any engineer can deliver. She writes instead that HMAC-SHA256, specified in RFC 2104 and FIPS 198-1, is widely reviewed and has no known practical attacks when keys are protected, and that the main risk is key handling rather than the algorithm. She lists what the control does not do: it does not hide readings from eavesdroppers, which would need encryption. Precise claims protect the utility when auditors or journalists later ask what was promised and why.

### 5.3 Decision records

Aiyana writes a decision record for the first major choice: one unique authentication key per meter, derived from a master key in the utility's key service, rather than one shared key for all meters. The record states context, options, decision, consequences, date and approver. Its key consequence is explicit: stealing one meter's key lets an attacker forge only that meter's readings, not the whole fleet's. Years later, when a contractor proposes a shared key to simplify provisioning, the record explains in two minutes why that was rejected.

### Worked example

Aiyana's one-page board note requests a key-service budget, explains forged readings in plain words, avoids "unbreakable", and links to a decision record choosing per-meter keys.

> **Synthetic case.** The board and decision are invented; RFC 2104 and FIPS 198-1 are real.

### Errors and limits

Oversimplifying can mislead: saying "encrypted" when data is only authenticated is a factual error. Records without the rejected options lose half their value.

### Exercises

- **EX013 — Board note opening.** How does Aiyana open her note to the board? *Rubric:* 3 = with the decision needed (budget for meter keys) then plain-language risk;; 2 = risk first;; 1 = jargon;; 0 = none.
- **EX014 — What HMAC does not do.** What does the note say HMAC does not provide? *Rubric:* 3 = confidentiality; readings are not hidden, encryption would be needed;; 2 = secrecy;; 1 = everything;; 0 = none.
- **EX015 — Per-meter keys.** What consequence of per-meter keys does the record highlight? *Rubric:* 3 = stealing one meter's key forges only that meter, not the fleet;; 2 = limits damage;; 1 = cheaper;; 0 = none.

### Synthesis

Clear, honest communication and decision records make cryptographic choices understandable to decision-makers and durable across staff changes.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) use series and limits to reason about cumulative risk; (2) model the probability of failure over many trials; (3) apply the approximation 1 - e^-x to security events.

### 6.1 Accumulating small risks

A single event with tiny probability becomes likely when repeated enough. If each of n independent trials fails with probability p, the chance that none fails is (1 - p)^n. Calculus II gives Aiyana the tool to simplify this: for small p, (1 - p)^n is close to e^(-np), a limit she derives from the series for the exponential function. This approximation appears constantly in cryptography, from nonce collisions to random key reuse, because engineers repeat operations billions of times. A risk of one in a billion per operation is not small for a fleet that performs ten billion operations.

### 6.2 Series and the exponential

The exponential function can be written as an infinite series, 1 + x + x²/2 + x³/6 and so on. For small x, the first two terms dominate, which is why 1 - e^(-x) is approximately x when x is tiny. Python's math.expm1 computes e^x - 1 accurately even for very small x, avoiding the rounding error of subtracting nearly equal numbers. Aiyana discovers this the hard way when her naive computation of 1 - exp(-1e-18) prints zero. She switches to -expm1(-x) and gets the correct tiny probability, a lesson in numerical care.

### 6.3 Applying it to Ridgeway

Suppose a faulty meter firmware chooses a 32-bit random identifier for each session, and the server confuses sessions if two identifiers match. With many sessions, the collision chance grows roughly as the square of the number of sessions divided by twice the space, the birthday effect developed further in Chapter 7. Aiyana uses the exponential approximation to show the board that a design acceptable for a pilot of a hundred meters fails for fifty thousand. The calculus tells her when "rare" stops being rare, which guides how many bits identifiers and nonces need.

### Worked example

Aiyana derives (1 - p)^n ≈ e^(-np), fixes a rounding bug with math.expm1, and shows that a per-session identifier safe for a pilot is unsafe at full scale.

> **Synthetic case.** The identifier design is invented; the mathematics is standard.

### Errors and limits

The approximation assumes independence and small p; correlated failures, such as a shared bad random seed, break it badly. Floating-point subtraction of nearly equal numbers loses precision.

### Exercises

- **EX016 — Limit approximation.** What approximation does Aiyana use for (1 - p)^n when p is small? *Rubric:* 3 = e^(-np);; 2 = exponential;; 1 = np exactly;; 0 = none.
- **EX017 — expm1 fix.** Why did 1 - exp(-1e-18) print zero, and what fixed it? *Rubric:* 3 = rounding when subtracting nearly equal numbers; use -math.expm1(-x);; 2 = rounding;; 1 = wrong formula;; 0 = none.
- **EX018 — Correlated failure.** When does the independence assumption fail badly? *Rubric:* 3 = correlated failures such as a shared bad random seed across meters;; 2 = correlation;; 1 = never;; 0 = none.

### Synthesis

Series and limits explain how tiny per-operation risks accumulate at scale, and careful numerics keep those estimates honest.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) apply the birthday bound to collisions; (2) choose tag and identifier lengths from collision targets; (3) interpret probability claims in standards.

### 7.1 The birthday problem

In a room of 23 people, the chance that two share a birthday exceeds one half, though there are 365 days. The reason is that the number of pairs grows with the square of the number of people. For random values from a space of size N, collisions become likely after about the square root of N draws. For an n-bit value, that is about 2^(n/2). Katz and Lindell use this bound to explain why a hash function with n-bit output offers only about n/2 bits of collision resistance, which is why SHA-256 is described as giving 128-bit collision security.

### Lab — Collision probability

```python
"""Birthday bound: chance two of k random n-bit tags collide (approximation)."""
import math

def p(k, bits):
    return -math.expm1(-k * (k - 1) / 2 ** (bits + 1))

def main():
    for bits in (32, 64, 128):
        k = 2 ** (bits // 2)
        print(f"{bits:>3}-bit tags, k=2^{bits // 2}: P(collision) = {p(k, bits):.3f}")
    print(f"meters 50,000 with 32-bit ids: P = {p(50_000, 32):.3f}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_birthday.py`. Verified output:

```text
 32-bit tags, k=2^16: P(collision) = 0.393
 64-bit tags, k=2^32: P(collision) = 0.393
128-bit tags, k=2^64: P(collision) = 0.393
meters 50,000 with 32-bit ids: P = 0.253
```

### 7.2 Reading the results

For each tag length, drawing 2^(n/2) random values gives a collision probability of about 0.393, the same for 32, 64 and 128 bits. That constant shows the square-root rule exactly. More practically, giving 50,000 meters random 32-bit identifiers produces about a 25 percent chance that two share an identifier. Aiyana recommends that Ridgeway assign identifiers sequentially from a registry instead of randomly, and that any random value whose uniqueness matters, such as a nonce, use at least 96 bits as GCM does, with counting and rotation as SP 800-38D requires.

### 7.3 Interpreting probability claims

Standards often state security as a probability bound for an attacker making a certain number of queries. Aiyana learns to ask three questions of any such claim: what the attacker is allowed to do, how many operations are counted, and what event counts as failure. A claim of 2^-32 failure after 2^32 messages is very different from 2^-32 per message. She also learns that statistics of real systems rarely match ideal randomness, so engineers measure, for instance by checking production logs for duplicate nonces, rather than relying on the theoretical bound alone.

### Worked example

Aiyana computes a 25 percent collision chance for 50,000 random 32-bit meter identifiers and recommends registry-assigned identifiers and 96-bit counted nonces.

> **Synthetic case.** The fleet size is invented; SP 800-38D is real.

### Errors and limits

The birthday bound assumes uniform randomness; biased generators collide sooner. Probability bounds depend on the counted unit, so read them carefully.

### Exercises

- **EX019 — Square-root rule.** After roughly how many draws do n-bit random values start colliding? *Rubric:* 3 = about 2^(n/2);; 2 = square root stated;; 1 = 2^n;; 0 = none.
- **EX020 — Meter identifiers.** What collision chance did the lab give for 50,000 meters with 32-bit identifiers, and what fix followed? *Rubric:* 3 = about 0.253; registry-assigned identifiers;; 2 = number only;; 1 = fix only;; 0 = none.
- **EX021 — Reading a bound.** Name the three questions Aiyana asks of a probability claim. *Rubric:* 3 = attacker capabilities, operations counted, failure event;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

The birthday bound turns collision risk into bit-length requirements, and careful reading of probability claims prevents false comfort.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) describe how processors accelerate cryptography; (2) explain caches as a source of leakage; (3) evaluate secure elements for storing meter keys.

### 8.1 Hardware support for cryptography

Modern processors include instructions that accelerate AES and SHA-2 directly in hardware, which makes encryption fast and also helps resist timing leaks, because the hardware executes in constant time regardless of key values. Aiyana compares the server processors at Ridgeway, which have such instructions, with the small microcontrollers in meters, which may not. On a microcontroller, software AES must be written carefully to avoid table lookups that depend on secret data. This architectural detail affects which algorithms Ridgeway selects for meters and why it prefers vendors whose libraries document constant-time behaviour.

### 8.2 Caches and leakage

Caches make memory access faster by keeping recently used data close to the processor. Because access time depends on whether data is cached, a program whose memory accesses depend on secrets can leak those secrets to another program sharing the cache. Classic table-based AES implementations had this weakness. Aiyana learns that this is why cloud servers isolate sensitive workloads and why hardware instructions replaced lookup tables. For Ridgeway's servers, she recommends running the key service on dedicated hosts rather than shared virtual machines, a cost judged worthwhile for the most sensitive keys.

### 8.3 Secure elements

A secure element is a small tamper-resistant chip that stores keys and performs cryptographic operations internally, so the key never appears in the meter's main memory. It resists probing and side-channel attacks better than a general microcontroller. Aiyana compares three meter designs: key in flash memory, key in a protected region of the microcontroller, and key inside a secure element. The secure element costs more per meter but means that opening one meter and dumping its memory does not reveal its key. She records the trade-off and the residual risk that remains even with tamper resistance.

### Worked example

Aiyana recommends secure elements for meter keys, hardware AES on servers, and dedicated hosts for the key service, with costs and residual risks recorded.

> **Synthetic case.** Meter designs and costs are invented.

### Errors and limits

Tamper resistance raises attacker cost but is not absolute. Hardware acceleration does not fix misuse such as nonce reuse.

### Exercises

- **EX022 — Hardware AES benefit.** Name two benefits of hardware AES instructions. *Rubric:* 3 = speed and constant-time execution resisting timing leaks;; 2 = one;; 1 = none;; 0 = none.
- **EX023 — Cache leak.** How can a cache leak secrets? *Rubric:* 3 = access time depends on cached data; secret-dependent accesses reveal keys to a co-resident program;; 2 = timing mentioned;; 1 = no leak;; 0 = none.
- **EX024 — Secure element value.** What does a secure element prevent compared with keys in flash? *Rubric:* 3 = dumping memory from one opened meter does not reveal its key;; 2 = protects key;; 1 = encrypts data;; 0 = none.

### Synthesis

Architecture shapes cryptographic security: hardware instructions, cache behaviour and secure elements decide how well keys survive in real devices.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure code that calls cryptographic libraries safely; (2) handle errors without leaking information; (3) test cryptographic code with known-answer and negative tests.

### 9.1 Wrapping libraries safely

Aiyana writes a small module that the meter-reading service will call for authentication. It exposes two functions, tag a reading and verify a reading, and hides all key handling and algorithm choices inside. Callers cannot choose algorithms or pass raw keys. This wrapper pattern reduces misuse: developers cannot accidentally use a weak hash or compare tags with ordinary equality. Marcus reminds her that the wrapper delegates to the standard library's hmac and hashlib, which implement RFC 2104 and FIPS 180-4, rather than reimplementing any primitive.

### 9.2 Errors that do not leak

When verification fails, the service must not tell the caller why, for example whether the meter identifier was unknown or the tag was wrong, because detailed errors help attackers probe the system. Aiyana's verify function returns only true or false to the caller and writes the detailed reason to a protected log. She also ensures exceptions never include key material or full readings in their messages. These rules reflect a broader principle: in security code, convenience for debugging must not become information for attackers.

### 9.3 Testing cryptographic code

Aiyana writes three kinds of tests. Known-answer tests check her wrapper against published vectors, such as RFC 4231 values for HMAC-SHA256, confirming correct use. Negative tests check that an altered reading, a wrong key or a truncated tag all fail. Property tests generate many random readings and confirm that tag-then-verify always succeeds. She learns that negative tests are often missing in practice, so a verification function that always returns true could pass every positive test. Her test suite runs on every change in continuous integration.

### Worked example

Aiyana's wrapper exposes only tag and verify, returns bare true or false, logs details privately, and passes known-answer, negative and property tests.

> **Synthetic case.** The service and wrapper are invented; RFC 2104 and FIPS 180-4 are real.

### Errors and limits

Wrappers can hide bugs as well as complexity; they must be reviewed and tested. A test suite without negative cases cannot catch a verifier that accepts everything.

### Exercises

- **EX025 — Wrapper benefit.** How does the wrapper reduce misuse? *Rubric:* 3 = callers cannot choose algorithms, pass raw keys, or compare tags unsafely;; 2 = hides details;; 1 = faster;; 0 = none.
- **EX026 — Silent failure.** Why does verify return only true or false to callers? *Rubric:* 3 = detailed reasons help attackers probe; details go to protected logs;; 2 = security;; 1 = simpler;; 0 = none.
- **EX027 — Missing negative tests.** What danger do negative tests guard against? *Rubric:* 3 = a verifier that always returns true passing all positive tests;; 2 = bugs;; 1 = none;; 0 = none.

### Synthesis

Safe cryptographic programming wraps vetted libraries, reveals little on failure and proves behaviour with positive and negative tests.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to cryptographic systems in critical infrastructure; (2) handle discovered weaknesses responsibly; (3) weigh safety against security.

### 10.1 Duty to the public

Engineering codes of ethics put public safety first. For a water utility, safety includes reliable water and accurate bills, and also not cutting off supply because a security control fails. Aiyana considers a design where meters refuse to report if their firmware signature cannot be verified. That protects against tampering but could leave the utility blind to leaks if a certificate expires. She learns that engineers must think through failure modes of security controls themselves, because a control that fails dangerously can harm the public it was meant to protect.

### 10.2 Responsible disclosure

During testing on a lab bench, Aiyana notices that a vendor's meter accepts firmware without checking the signature when its battery is low. She reports it to Marcus, who reports it to the vendor under Ridgeway's coordinated disclosure process, giving the vendor time to fix it before details are shared. She does not post about it or test it on deployed meters. Ethical practice means reporting weaknesses to those who can fix them, keeping details confidential until fixed and never exploiting them, even to prove a point.

### 10.3 Safety versus security trade-offs

Aiyana writes a short analysis of the low-battery case and of the expiry case. For each, she lists what happens if the control fails open, accepting anything, and if it fails closed, refusing everything. For firmware updates, failing closed is right: a meter should keep its current firmware rather than install unverified code. For reporting readings, failing closed would harm customers, so meters keep reporting while raising an alert. Writing these choices down lets the utility's safety and security teams agree in advance rather than argue during an incident.

### Worked example

Aiyana reports a low-battery signature bypass through coordinated disclosure and writes a fail-open versus fail-closed table for firmware updates and readings.

> **Synthetic case.** The vendor flaw is invented for teaching.

### Errors and limits

Treating every security control as fail-closed can create safety hazards; treating every one as fail-open invites attack. Disclosure without coordination can harm users.

### Exercises

- **EX028 — Expiry hazard.** What safety risk did Aiyana see in refusing to report on signature failure? *Rubric:* 3 = utility blind to leaks if a certificate expires;; 2 = outage;; 1 = none;; 0 = none.
- **EX029 — Disclosure path.** How was the low-battery flaw handled? *Rubric:* 3 = reported to Marcus and vendor via coordinated disclosure, kept confidential, not tested on live meters;; 2 = reported;; 1 = posted publicly;; 0 = none.
- **EX030 — Firmware fail mode.** Should firmware verification fail open or closed, and why? *Rubric:* 3 = closed: keep current firmware rather than install unverified code;; 2 = closed;; 1 = open;; 0 = none.

### Synthesis

Ethical cryptographic engineering protects the public by planning how controls fail and by disclosing weaknesses responsibly.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) trace how meter data crosses networks; (2) explain what TLS 1.3 protects and what it does not; (3) choose where to authenticate and encrypt.

### 11.1 The path of a reading

A reading leaves a meter over a low-power radio link to a neighbourhood collector, travels over a cellular network to Ridgeway's gateway, then crosses the utility's internal network to the billing database. Aiyana draws each hop and asks who could read or modify data there: a nearby radio listener, the cellular carrier, an insider on the internal network. Each hop has different attackers. Drawing the path first prevents a common error, protecting one link strongly while leaving another open, and it shows where end-to-end protection from meter to database would remove dependence on intermediate hops.

### 11.2 What TLS 1.3 provides

Between collector and gateway, Ridgeway uses TLS 1.3, specified in RFC 8446. TLS provides confidentiality, integrity and server authentication for the connection, using an ephemeral key exchange such as X25519 from RFC 7748 so that recorded traffic cannot be decrypted later even if long-term keys leak, a property called forward secrecy. Aiyana notes what TLS does not do: it protects data only while in transit on that connection. Once the gateway decrypts it, readings are plaintext inside the utility, and TLS says nothing about whether the meter itself was honest.

### 11.3 End-to-end authentication

Because TLS ends at the gateway, Aiyana proposes that each meter also attach an HMAC tag to every reading, using its per-meter key from Chapter 5. The billing database verifies the tag directly, so a compromised gateway or collector cannot alter readings undetected. This layering, transport security plus message authentication, is common in critical infrastructure. She documents which layer defends against which attacker: TLS against carriers and eavesdroppers on that link, HMAC against any intermediate system modifying readings. Overlap is deliberate, so one failure does not remove all protection.

### Worked example

Aiyana's diagram shows four hops; TLS 1.3 protects collector to gateway, and per-meter HMAC tags protect readings from meter to database.

> **Synthetic case.** Ridgeway's network is invented; RFC 8446 and RFC 7748 are real.

### Errors and limits

TLS does not authenticate data origin beyond the endpoint; message-level controls are needed when intermediaries are untrusted. Radio links to meters may need separate protection.

### Exercises

- **EX031 — Hop attackers.** Name the attacker Aiyana associates with the cellular hop. *Rubric:* 3 = the cellular carrier or anyone on its network;; 2 = network;; 1 = none;; 0 = none.
- **EX032 — Forward secrecy.** What does forward secrecy mean in TLS 1.3? *Rubric:* 3 = recorded traffic cannot be decrypted later even if long-term keys leak, due to ephemeral key exchange;; 2 = ephemeral keys;; 1 = encryption;; 0 = none.
- **EX033 — Why HMAC too.** Why add HMAC tags when TLS is already used? *Rubric:* 3 = TLS ends at the gateway; HMAC lets the database detect altered readings from compromised intermediaries;; 2 = layering;; 1 = redundant;; 0 = none.

### Synthesis

Network security means mapping each hop's attackers and layering transport and message protections so no single endpoint is trusted blindly.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain how operating systems protect keys in memory and on disk; (2) use the OS random generator correctly; (3) apply least privilege to cryptographic services.

### 12.1 Processes and memory

An operating system separates processes so that one cannot read another's memory. Ridgeway's key service runs as its own process under a dedicated account; the billing application asks it to compute tags rather than holding keys itself. Aiyana learns that a key in a process's memory may also end up in swap files or crash dumps, so the service disables core dumps and locks key pages in memory where the platform allows. These operating-system details matter as much as the algorithm, because most real key thefts read keys from memory or disk, not by breaking cryptography.

### 12.2 The OS random generator

The operating system gathers entropy from hardware events and exposes a cryptographically secure generator to programs, on Linux through the getrandom system call. Python's secrets module uses it. Aiyana compares secrets.token_bytes with the random module, which is a fast, predictable generator meant for simulations; its outputs can be reconstructed after observing enough values. She rewrites a teammate's key-generation script that used random.getrandbits. The rule she adopts is simple: anything secret, including keys, nonces and tokens, comes from secrets or a vetted library, never from random.

### 12.3 Least privilege

Aiyana configures the key service to run with the minimum rights it needs: read access to its own encrypted key file, a single listening socket, and no shell. File permissions restrict the key file to the service account. Administrators access the service through an audited interface rather than logging into the host. SP 800-57 Part 1 stresses protecting keys throughout their lifecycle, and least privilege at the operating-system level is a large part of that protection. If the billing application is compromised, the attacker still cannot read raw keys.

### Worked example

Aiyana moves keys into a dedicated service process with locked memory, no core dumps, minimal file permissions, and secrets-based generation.

> **Synthetic case.** The key service is invented; SP 800-57 Part 1 is real.

### Errors and limits

Memory locking and dump suppression are platform-dependent and imperfect. A privileged attacker on the host can still read memory, so isolation reduces rather than removes risk.

### Exercises

- **EX034 — Swap and dumps.** Why disable core dumps for the key service? *Rubric:* 3 = keys in memory could be written to dumps or swap and stolen from disk;; 2 = disk leak;; 1 = performance;; 0 = none.
- **EX035 — random versus secrets.** Why must keys never come from Python's random module? *Rubric:* 3 = it is predictable and reconstructible; secrets uses the OS CSPRNG;; 2 = predictable;; 1 = slower;; 0 = none.
- **EX036 — Compromised billing app.** What can an attacker who compromises the billing application not do? *Rubric:* 3 = read raw keys, since the separate key service holds them under least privilege;; 2 = limited;; 1 = everything;; 0 = none.

### Synthesis

Operating-system isolation, secure randomness and least privilege protect keys where most real thefts happen: in memory and on disk.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) choose between hashing, encrypting and tokenising stored data; (2) store passwords with memory-hard functions; (3) plan encryption at rest with separate keys.

### 13.1 Three tools for stored data

Ridgeway's database holds customer names, addresses, bank details and meter readings. Aiyana learns to choose the right tool for each field. Encryption hides data that must later be read, such as bank details for direct debit. Tokenisation replaces data with a meaningless reference stored elsewhere, useful when most systems need only a placeholder. Hashing, which is one-way, suits values that need only to be checked, never recovered. Picking the wrong tool, such as hashing bank details that must be used, or encrypting passwords that never need decrypting, creates either broken systems or unnecessary risk.

### 13.2 Storing passwords

Customer portal passwords must never be stored in plain text or with a fast hash such as SHA-256 alone, because attackers who steal the table can test billions of guesses per second. Aiyana recommends a memory-hard password hashing function, Argon2id from RFC 9106, which forces each guess to use significant memory and time, with a unique random salt per user. If Argon2 is unavailable, scrypt from RFC 7914 or PBKDF2 with a high iteration count are fallbacks. Python's hashlib offers scrypt and pbkdf2_hmac; production code still uses a vetted password-hashing library with sensible defaults.

### 13.3 Encryption at rest

For bank details, Ridgeway uses database encryption with a data-encryption key, itself encrypted by a key-encryption key held in the key service, a pattern called envelope encryption. Aiyana explains its benefit: rotating the key-encryption key requires re-encrypting only small data keys, not the whole database. She also notes a limit: encryption at rest protects against stolen disks and backups, but not against an attacker who queries the running application, which decrypts data for legitimate users. Access control and monitoring remain essential alongside encryption.

### Worked example

Aiyana assigns encryption to bank details, tokens to reporting systems, and Argon2id with per-user salts to portal passwords, and designs envelope encryption with keys in the key service.

> **Synthetic case.** The database is invented; RFC 9106 and RFC 7914 are real.

### Errors and limits

Encryption at rest does not stop application-level theft. A slow password hash still fails if users choose very common passwords, so rate limiting and breach checks help.

### Exercises

- **EX037 — Choosing a tool.** Which tool suits portal passwords and why? *Rubric:* 3 = hashing with a memory-hard function, since they need checking not recovery;; 2 = hashing;; 1 = encryption;; 0 = none.
- **EX038 — Argon2 choice.** What does Aiyana recommend for passwords and which RFC defines it? *Rubric:* 3 = Argon2id with per-user salts, RFC 9106;; 2 = Argon2;; 1 = SHA-256;; 0 = none.
- **EX039 — Envelope benefit.** What benefit does envelope encryption give? *Rubric:* 3 = rotating the key-encryption key re-encrypts only small data keys;; 2 = rotation easier;; 1 = faster queries;; 0 = none.

### Synthesis

Matching hashing, encryption and tokenisation to each field, with memory-hard password hashing and envelope encryption, protects stored data proportionately.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) integrate cryptographic requirements into the development lifecycle; (2) manage dependencies on cryptographic libraries; (3) review code for common misuse.

### 14.1 Requirements in the lifecycle

Aiyana joins Ridgeway's software team and finds that cryptography was added late to previous projects, causing rework. She proposes that security requirements, such as "every reading is authenticated with a per-meter key" and "firmware is accepted only with a valid signature", appear in the backlog from the start, each with an acceptance test. Treating cryptographic properties as testable requirements rather than as a final review makes them visible in planning and estimates, and makes it clear which team owns each property.

### 14.2 Managing dependencies

Ridgeway depends on a few cryptographic libraries. Aiyana records each library's version, its source and its maintainers, and subscribes to its security advisories. She pins versions so builds are reproducible but schedules regular updates, because cryptographic libraries fix vulnerabilities regularly. She also checks that downloaded packages match published hashes or signatures, to avoid tampered dependencies. The team agrees never to copy cryptographic code from forums into the codebase; if a function is missing, they find a maintained library or raise it in design review.

### 14.3 Reviewing for misuse

Aiyana writes a short review checklist: no hard-coded keys; secrets from the secrets module; no ECB mode or unauthenticated encryption; nonces never reused under a key; tags compared with hmac.compare_digest; passwords hashed with Argon2id; TLS verification never disabled. Reviewers tick each item for changes touching cryptography. In the first month the checklist catches a test helper that disabled certificate verification and was about to be reused in production code. Checklists do not replace expertise but catch common mistakes reliably.

### Worked example

Aiyana adds testable crypto requirements to the backlog, pins and monitors libraries, and introduces a seven-item review checklist that catches disabled TLS verification.

> **Synthetic case.** The team and incident are invented.

### Errors and limits

Checklists can become box-ticking; reviewers must understand each item. Pinning without updating leaves known vulnerabilities in place.

### Exercises

- **EX040 — Testable requirement.** Give an example of a cryptographic requirement written as a backlog item. *Rubric:* 3 = every reading authenticated with a per-meter key (or firmware accepted only with valid signature), with acceptance test;; 2 = example without test;; 1 = vague;; 0 = none.
- **EX041 — Dependency rule.** What did the team agree about forum code? *Rubric:* 3 = never copy cryptographic code from forums; use a maintained library or raise in design review;; 2 = avoid;; 1 = allowed;; 0 = none.
- **EX042 — Checklist catch.** What did the checklist catch in its first month? *Rubric:* 3 = a test helper disabling certificate verification about to enter production;; 2 = TLS issue;; 1 = nothing;; 0 = none.

### Synthesis

Cryptography becomes reliable when it is a tested requirement, its libraries are managed actively and reviews check for known misuse.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) map confidentiality, integrity and availability to cryptographic controls; (2) define threat models; (3) distinguish authentication from authorisation.

### 15.1 The three properties

Security is often described through confidentiality, integrity and availability. Aiyana maps each to Ridgeway's meters. Confidentiality of readings matters because consumption patterns reveal when homes are empty. Integrity matters because altered readings change bills. Availability matters because the utility needs readings to detect leaks. Cryptography mainly serves confidentiality and integrity: encryption for the first, authentication codes and signatures for the second. It can harm availability if keys are lost or certificates expire, which is why key management and operations are as important as algorithms.

### 15.2 Threat models

A threat model states who the attackers are, what they want, what they can do and what is out of scope. Aiyana writes one for meters: a curious neighbour with a radio receiver, a customer trying to lower a bill, a criminal group seeking to disrupt supply and a malicious insider. She sets nation-state hardware attacks out of scope for the pilot, stating that explicitly. Katz and Lindell insist that every security definition depends on an explicit attacker model; without one, claims such as "secure" have no meaning.

### 15.3 Authentication and authorisation

Authentication establishes who or what is communicating; authorisation decides what that party may do. A meter authenticates with its per-meter key, but it is authorised only to submit its own readings, not those of other meters or configuration changes. Aiyana finds a design draft where any authenticated meter could submit readings for any identifier, a classic confusion of the two. She adds a check binding each key to one meter identifier. Cryptography provides authentication; authorisation is a policy decision implemented in application logic.

### Worked example

Aiyana maps CIA properties to meter controls, writes a four-attacker threat model with an explicit exclusion, and fixes a design where authentication did not imply correct authorisation.

> **Synthetic case.** The threat model is invented.

### Errors and limits

Threat models age; revisit them when systems change. Strong authentication with weak authorisation still allows abuse.

### Exercises

- **EX043 — Why confidentiality.** Why does meter reading confidentiality matter? *Rubric:* 3 = consumption patterns reveal when homes are empty;; 2 = privacy;; 1 = no reason;; 0 = none.
- **EX044 — Out of scope.** What did Aiyana place out of scope and why state it? *Rubric:* 3 = nation-state hardware attacks; explicit scope makes claims meaningful;; 2 = scope stated;; 1 = nothing;; 0 = none.
- **EX045 — Authorisation fix.** What check fixed the authorisation flaw? *Rubric:* 3 = binding each key to one meter identifier so meters submit only their own readings;; 2 = binding;; 1 = encryption;; 0 = none.

### Synthesis

Security fundamentals frame cryptography: map it to explicit properties and attacker models, and keep authentication separate from authorisation.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) treat key management as a system with lifecycle stages; (2) define interfaces and responsibilities; (3) trace requirements through components.

### 16.1 Keys as a system

Aiyana learns from SP 800-57 Part 1 that keys have lifecycles: generation, distribution, use, storage, rotation, revocation and destruction. Each stage involves people, processes and technology. She draws Ridgeway's key system: a key service generating meter keys, a factory process loading them into secure elements, collectors forwarding readings, and a billing system verifying tags. Systems engineering helps her see that a weakness anywhere, such as keys emailed to the factory, undermines strong algorithms everywhere else. Her diagram also shows the people involved, because a careless procedure breaks a system as surely as a weak algorithm.

### 16.2 Interfaces and responsibilities

For each interface Aiyana defines what is exchanged, how it is protected and who owns it. The factory receives meter keys encrypted under a transport key, not in clear; the key service owns generation; operations owns rotation; security owns revocation decisions. She uses a responsibility table so that no lifecycle step is unowned. In past projects, revocation fell between teams and compromised keys stayed active for months. Clear ownership is a security control in its own right. The table is reviewed every quarter so that reorganisations never leave a stage without an owner.

### 16.3 Requirements traceability

Aiyana traces each top-level requirement, such as "a stolen meter key affects only that meter", down to component requirements: per-meter derivation in the key service, binding of keys to identifiers in billing, revocation lists in collectors. Each component requirement has a verification method, test, inspection or analysis. When a vendor proposes a change to the factory process, the trace shows which requirements it touches and which tests must be rerun. Traceability turns a security goal into checkable engineering work. Traceability also helps auditors, who can follow any requirement to its evidence.

### Worked example

Aiyana's key-system diagram, responsibility table and traceability matrix show every lifecycle stage owned and every security requirement linked to a test.

> **Synthetic case.** Ridgeway's processes are invented; SP 800-57 Part 1 is real.

### Errors and limits

Diagrams drift from reality; review them against deployments. Traceability helps only if tests actually run.

### Exercises

- **EX046 — Lifecycle stages.** List four key lifecycle stages from SP 800-57. *Rubric:* 3 = four of generation, distribution, use, storage, rotation, revocation, destruction;; 2 = three;; 1 = one;; 0 = none.
- **EX047 — Factory interface.** How are keys protected on the way to the factory? *Rubric:* 3 = encrypted under a transport key, never in clear;; 2 = encrypted;; 1 = emailed;; 0 = none.
- **EX048 — Ownership lesson.** What past failure motivated the responsibility table? *Rubric:* 3 = revocation fell between teams and compromised keys stayed active for months;; 2 = unowned step;; 1 = none;; 0 = none.

### Synthesis

Treating key management as a system with owned interfaces and traced requirements prevents strong algorithms from being undermined by weak processes.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) apply feedback loops to security operations; (2) design alerts on cryptographic health signals; (3) avoid oscillation and alert fatigue.

### 17.1 Feedback in operations

Control engineering studies systems that measure output and adjust input. Aiyana applies the idea to cryptographic operations: measure signals such as tag verification failures, certificate days to expiry and key ages, compare them with targets, and act. Without feedback, problems are noticed only when customers complain. A feedback loop for Ridgeway might measure the hourly rate of verification failures per collector and alert if it rises sharply, which could indicate a faulty meter batch or an attempted forgery. Aiyana treats each signal as a sensor and each runbook as the controller that closes the loop.

### 17.2 Designing alerts

Aiyana chooses thresholds from baseline data. Normal verification failures, from radio noise and clock drift, run at about 0.1 percent; she alerts above 1 percent sustained for fifteen minutes. Certificates alert at thirty days before expiry and escalate at seven. Key ages alert at the end of their cryptoperiod. Each alert has an owner and a runbook stating the first checks. She also adds alerts for the absence of expected signals, such as no renewal attempt in the past week, because silent failures cause many outages.

### 17.3 Avoiding fatigue and oscillation

Too many alerts train people to ignore them, and automated reactions that are too aggressive can oscillate, for instance repeatedly revoking and re-provisioning keys for a meter with a flaky radio. Aiyana adds hysteresis: an alert clears only when the rate falls well below the trigger. Automated actions are limited to safe steps, such as flagging a meter for inspection, while revocation requires a human decision. She reviews alert volumes monthly and removes alerts that never led to action, keeping the signal meaningful.

### Worked example

Aiyana designs alerts on verification-failure rates, certificate expiry and key age, with baselines, hysteresis and human approval for revocation.

> **Synthetic case.** The baselines are invented.

### Errors and limits

Thresholds set without baselines create noise. Automated revocation without hysteresis can disrupt service.

### Exercises

- **EX049 — Health signals.** Name three cryptographic health signals Aiyana measures. *Rubric:* 3 = verification failures, certificate days to expiry, key ages;; 2 = two;; 1 = one;; 0 = none.
- **EX050 — Missing signal alert.** Why alert on the absence of renewal attempts? *Rubric:* 3 = silent failures such as broken renewal clients cause outages;; 2 = silence;; 1 = not needed;; 0 = none.
- **EX051 — Hysteresis use.** What does hysteresis prevent here? *Rubric:* 3 = oscillating alerts or repeated revoke/re-provision for flaky meters;; 2 = flapping;; 1 = nothing;; 0 = none.

### Synthesis

Feedback loops with baselined thresholds, hysteresis and human gates keep cryptographic systems healthy without drowning operators in noise.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) place cryptographic trust anchors in an architecture; (2) design defence in depth for keys; (3) compare centralised and distributed key services.

### 18.1 Trust anchors

Every cryptographic architecture rests on trust anchors, keys whose authenticity is assumed rather than proven, such as a root certificate or a firmware-signing public key embedded in meters. Aiyana identifies Ridgeway's anchors: the firmware root key, the TLS root for collectors and the master key in the key service. Compromise of an anchor is catastrophic, so anchors are few, kept offline where possible, and protected by multi-person procedures. Her architecture diagram marks anchors in red, so reviewers immediately see where the highest protection is needed.

### 18.2 Defence in depth for keys

Aiyana layers protection: the firmware root key lives in an offline hardware security module used only in signing ceremonies; intermediate signing keys sign day-to-day releases and can be revoked; meters accept firmware only when the chain verifies and the version number increases, preventing rollback to old vulnerable versions. Each layer limits the damage from the failure of another. If an intermediate key leaks, the root can revoke it; if a signed old version is replayed, the version check rejects it.

### 18.3 Centralised or distributed

A single central key service simplifies audit and rotation but becomes a high-value target and a single point of failure. Distributing keys among regional services improves availability but multiplies places to secure. Aiyana proposes a central service with a hot standby in a second data centre and regional caches holding only derived, short-lived keys. She evaluates the design against the threat model from Chapter 15, recording that an insider at a regional site can affect only that region's short-lived keys. She notes that the standby site doubles the physical controls to audit.

### Worked example

Aiyana's architecture marks three trust anchors, places the firmware root offline with intermediates for releases and rollback protection, and chooses a central key service with standby and regional short-lived caches.

> **Synthetic case.** The architecture is invented.

### Errors and limits

Offline roots are only as safe as ceremony procedures. Rollback protection fails if version counters can be reset.

### Exercises

- **EX052 — Trust anchor defined.** What is a trust anchor? *Rubric:* 3 = a key whose authenticity is assumed, like a root certificate or embedded firmware-signing key;; 2 = root key;; 1 = any key;; 0 = none.
- **EX053 — Rollback protection.** How does the design prevent firmware rollback? *Rubric:* 3 = meters require version number to increase in addition to valid chain;; 2 = version check;; 1 = signature only;; 0 = none.
- **EX054 — Regional insider.** What can an insider at a regional site affect in the chosen design? *Rubric:* 3 = only that region's short-lived derived keys;; 2 = limited;; 1 = everything;; 0 = none.

### Synthesis

Architectures should name their trust anchors, layer key protection and balance central control against availability with limited regional exposure.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) authenticate devices and people with keys and certificates; (2) use HMAC for message authentication; (3) relate identities to certificates and revocation.

### 19.1 Device identity

Each Ridgeway meter needs an identity that others can verify. Aiyana compares two approaches. Symmetric identity uses a per-meter secret key shared with the key service; it is cheap but the service must protect every key. Asymmetric identity gives each meter a key pair and a certificate signed by Ridgeway's device authority, following the X.509 profile in RFC 5280; verifiers need only public keys. She recommends symmetric HMAC keys for readings, where volume is high, and certificates for collectors, which authenticate to the gateway over TLS.

### Lab — Message authentication

```python
"""Authenticate synthetic meter readings with HMAC-SHA256 (RFC 2104) and constant-time compare."""
import hmac, hashlib
KEY = bytes(range(32))   # demo key; real keys come from the utility's key service
def tag(msg): return hmac.new(KEY, msg, hashlib.sha256).hexdigest()

def main():
    msg = b"meter=M-0417;litres=18342;ts=2026-04-01T06:00Z"
    t = tag(msg)
    print("tag", t[:24], "...")
    print("genuine verifies:", hmac.compare_digest(t, tag(msg)))
    forged = msg.replace(b"18342", b"08342")
    print("edited reading verifies:", hmac.compare_digest(t, tag(forged)))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_hmac.py`. Verified output:

```text
tag bc7de0101afc1c79bfc23747 ...
genuine verifies: True
edited reading verifies: False
```

### 19.2 Reading the HMAC run

The lab tags a canonical reading with HMAC-SHA256 and verifies it. The genuine reading verifies and the edited reading, with one digit changed, fails, because without the key nobody can compute a valid tag for a modified message. Verification uses hmac.compare_digest to avoid timing leaks. The demonstration key is a fixed byte sequence only so the output is reproducible; real keys come from the key service. Aiyana stresses that HMAC gives integrity and origin authentication between parties sharing the key, but not non-repudiation, because either party could have produced the tag.

### 19.3 People and revocation

People at Ridgeway authenticate with hardware security keys and short-lived certificates for administrative access. When someone leaves, their access must end quickly. Aiyana documents revocation for each identity type: meter keys are disabled in the key service; collector certificates are added to a revocation list or simply allowed to expire, since they are short-lived; staff certificates are revoked and their tokens disabled. She notes that short lifetimes reduce dependence on revocation checking, which clients perform unevenly. Revocation steps are rehearsed twice a year so that staff know them under pressure.

### Worked example

Aiyana chooses HMAC per-meter keys for readings and certificates for collectors and staff, demonstrates tag verification, and documents revocation per identity type.

> **Synthetic case.** Identities and the demo key are invented; RFC 5280 and RFC 2104 are real.

### Errors and limits

HMAC cannot prove to a third party which side created a message. Long-lived certificates make revocation essential and hard.

### Exercises

- **EX055 — Symmetric or asymmetric.** Why use HMAC keys for readings but certificates for collectors? *Rubric:* 3 = high-volume readings suit cheap symmetric tags; collectors use TLS with public verification;; 2 = reasons partial;; 1 = random;; 0 = none.
- **EX056 — Edited reading.** What did the lab print for the edited reading, and why? *Rubric:* 3 = False, since a valid tag cannot be computed without the key;; 2 = False;; 1 = True;; 0 = none.
- **EX057 — Non-repudiation.** Why does HMAC not give non-repudiation? *Rubric:* 3 = both parties share the key, so either could have made the tag;; 2 = shared key;; 1 = it does;; 0 = none.

### Synthesis

Identity combines keys, certificates and revocation; HMAC authenticates high-volume messages between key holders, while certificates scale verification.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Cryptography and trust services: engineering context

### Learning outcomes

You will (1) frame Ridgeway's cryptographic needs as an engineering problem; (2) list stakeholders and constraints; (3) define success measures for the trust service.

### 20.1 The engineering problem

Entering the specialisation years, Aiyana writes a problem statement: Ridgeway needs a trust service that issues and manages keys and certificates for 50,000 meters, 400 collectors and 120 staff, authenticates every reading end to end, signs firmware with rollback protection, and remains available during outages. Constraints include meter battery life, radio bandwidth and a fixed budget. Framing the problem this way moves the discussion from which algorithm is strongest to which system meets security, cost and reliability needs together. She keeps the statement to one page so every stakeholder can read and challenge it.

### 20.2 Stakeholders

Aiyana lists stakeholders and what they need: customers need accurate bills and privacy; field technicians need to replace meters without complex steps; operations needs alerts it can act on; the regulator needs evidence of controls; vendors need clear interfaces. She interviews each group. Technicians reveal that meters are sometimes swapped between addresses during repairs, which affects how keys are bound to identities. Such operational facts, invisible in a security textbook, shape the design as much as standards do. Aiyana records each interview in a short note so later design choices can cite real needs.

### 20.3 Success measures

Aiyana defines measurable goals: zero accepted forged readings in independent testing; certificate expiry incidents fewer than one per year; firmware updates reaching 99 percent of meters within thirty days; key rotation completed on schedule for every key class; and provisioning a replacement meter in under ten minutes. Each measure has a data source and an owner. Measures keep the project honest, prevent gold-plating and give the regulator evidence beyond assurances. She also plans to review the measures yearly, since a target set in the pilot may be too loose or too strict at full scale.

### Worked example

Aiyana's problem statement names scale, constraints, stakeholders and five success measures, including the technician's ten-minute provisioning target.

> **Synthetic case.** Ridgeway's figures are invented.

### Errors and limits

Success measures can be gamed if they ignore quality; pair each with a review. Stakeholder interviews may miss silent groups such as customers with accessibility needs.

### Exercises

- **EX058 — Problem constraints.** Name three constraints in the problem statement. *Rubric:* 3 = three of battery life, radio bandwidth, budget, availability during outages;; 2 = two;; 1 = one;; 0 = none.
- **EX059 — Technician insight.** What did technicians reveal and why does it matter? *Rubric:* 3 = meters swapped between addresses during repairs, affecting key-identity binding;; 2 = swapping;; 1 = nothing;; 0 = none.
- **EX060 — Firmware measure.** State the firmware success measure. *Rubric:* 3 = 99 percent of meters updated within thirty days;; 2 = 99 percent;; 1 = always;; 0 = none.

### Synthesis

Cryptographic engineering starts by framing scale, constraints, stakeholders and measurable goals for the whole trust service.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Cryptography and trust services: requirements

### Learning outcomes

You will (1) write verifiable cryptographic requirements; (2) derive algorithm and key-length requirements from standards; (3) separate functional from assurance requirements.

### 21.1 Verifiable statements

Aiyana rewrites vague goals as verifiable requirements. "Readings must be secure" becomes "Every reading carries an HMAC-SHA256 tag computed with a 256-bit per-meter key; the billing service rejects any reading whose tag fails verification." Each requirement names the property, mechanism, parameter and observable behaviour. A tester can check it without guessing what "secure" meant. She avoids requirements that dictate implementation details unnecessarily, so vendors can meet them in different ways, but she is precise where precision prevents misuse, such as key length and verification behaviour.

### 21.2 Grounding in standards

For algorithm choices Aiyana cites standards rather than preference: AES-256-GCM per FIPS 197 and SP 800-38D for encrypting configuration data; SHA-256 per FIPS 180-4; ECDSA P-256 per FIPS 186-5 or Ed25519 per RFC 8032 for firmware signatures; TLS 1.3 per RFC 8446 for collectors. Key lengths and cryptoperiods follow SP 800-57 Part 1. She adds a forward-looking requirement that firmware-signing design must allow migration to post-quantum signatures, such as ML-DSA from FIPS 204, without replacing meters. Citing standards also lets auditors check choices against public criteria rather than against the team's preferences, and it simplifies future review when guidance changes.

### 21.3 Assurance requirements

Functional requirements say what the system does; assurance requirements say how Ridgeway will know it is done correctly. Aiyana adds assurance items: libraries must come from maintained projects with security advisories; hardware security modules must hold a recognised validation certificate; independent testers must attempt reading forgery before go-live; key ceremonies must have two witnesses and recorded minutes. These requirements cost money and time, so she ranks them by risk and records which are mandatory for the pilot and which for full rollout.

### Worked example

Aiyana's requirement set specifies HMAC-SHA256 with 256-bit keys, standard-backed algorithms, a post-quantum migration path and ranked assurance items.

> **Synthetic case.** Ridgeway's requirement set is invented; the cited standards are real.

### Errors and limits

Over-specifying implementation can block better designs; under-specifying parameters invites weak choices. Requirements need periodic review as standards change.

### Exercises

- **EX061 — Rewriting a goal.** Rewrite "readings must be secure" as a verifiable requirement. *Rubric:* 3 = names HMAC-SHA256, 256-bit per-meter key, rejection on failed verification;; 2 = partial mechanism;; 1 = vague;; 0 = none.
- **EX062 — Signature standards.** Which standards back the firmware signature options? *Rubric:* 3 = FIPS 186-5 (ECDSA P-256) or RFC 8032 (Ed25519);; 2 = one;; 1 = none;; 0 = none.
- **EX063 — Assurance example.** Give two assurance requirements. *Rubric:* 3 = two of maintained libraries, validated HSMs, independent forgery testing, witnessed ceremonies;; 2 = one;; 1 = functional item;; 0 = none.

### Synthesis

Good cryptographic requirements are verifiable, grounded in standards, ready for migration and paired with assurance evidence.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Cryptography and trust services: system and data models

### Learning outcomes

You will (1) model keys, certificates and identities as data; (2) design a key inventory schema; (3) model states and transitions of keys.

### 22.1 Modelling key objects

Aiyana models the trust service's data. A key record has an identifier, purpose, algorithm, length, owner, creation date, activation date, expiry or cryptoperiod end, state and storage location; it never contains key material itself. A certificate record links a subject identity, public key fingerprint, issuer, serial number and validity dates. Meter records link a physical meter, its current key identifier and its installation address. Separating identity from key allows meters to be re-keyed or moved between addresses without losing history.

### 22.2 The key inventory

Using the model, Aiyana designs a key inventory, the single place listing every key Ridgeway owns. SP 800-57 Part 1 stresses that organisations must know what keys they have and where they are used. The inventory answers operational questions: which keys expire this month, which systems use the firmware intermediate key, which keys still use an algorithm scheduled for retirement. She finds three keys in old scripts that nobody had recorded, demonstrating why the inventory matters before any cryptographic change can be planned safely.

### 22.3 Key states

Aiyana models a key's states: pre-activation, active, suspended, deactivated, compromised and destroyed, following the lifecycle described in SP 800-57 Part 1. Each transition has a trigger and an authorised actor: activation after provisioning, deactivation at cryptoperiod end, compromised on evidence of exposure. Deactivated keys may still verify old data but not create new tags or signatures. The state model prevents mistakes such as signing new firmware with a key already marked for retirement, because the service checks state before every operation. State changes are logged with actor and reason for audit.

### Worked example

Aiyana's data model separates meters, identities and keys; the inventory finds three unrecorded keys; and a six-state lifecycle blocks signing with retired keys.

> **Synthetic case.** The schema and findings are invented; SP 800-57 Part 1 is real.

### Errors and limits

Inventories decay without automated discovery. A state model is only enforced if every operation checks it.

### Exercises

- **EX064 — No key material.** What must a key record never contain? *Rubric:* 3 = the key material itself;; 2 = secrets;; 1 = metadata;; 0 = none.
- **EX065 — Inventory finding.** What did building the inventory reveal? *Rubric:* 3 = three keys in old scripts that nobody had recorded;; 2 = unrecorded keys;; 1 = nothing;; 0 = none.
- **EX066 — Deactivated key.** What may a deactivated key still do and not do? *Rubric:* 3 = verify old data but not create new tags or signatures;; 2 = verify only;; 1 = everything;; 0 = none.

### Synthesis

Clear data models, a complete inventory and an enforced key state machine make keys manageable rather than hidden liabilities.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Cryptography and trust services: threat and failure analysis

### Learning outcomes

You will (1) analyse threats to the trust service systematically; (2) analyse non-malicious failure modes; (3) rank risks for treatment.

### 23.1 Systematic threats

Aiyana uses a structured method, walking each component and data flow and asking how an attacker could spoof identity, tamper with data, deny actions, disclose information, deny service or gain privilege. For the firmware path she finds that an attacker who compromised the build server could get malicious code signed legitimately. For readings, a stolen meter key allows forging that meter's readings. For the key service, an insider could export keys. Each threat is written with its preconditions, so the team can judge likelihood rather than react to the most dramatic story.

### 23.2 Failure modes

Not all problems are attacks. Aiyana adds failure analysis: an expired collector certificate stops readings from a district; clock drift in meters causes timestamp checks to reject valid readings; loss of the hardware security module without backup makes firmware signing impossible; a faulty random number generator after a firmware update produces repeated nonces. For each she records detection and effect. Several failures have consequences as severe as attacks, and some are more likely, which reshapes priorities. Recording detection methods also shows which failures would currently go unnoticed.

### 23.3 Ranking and treatment

Aiyana scores each threat and failure by likelihood and impact on a simple scale, and chooses a treatment: mitigate, transfer, accept or avoid. Build-server compromise gets mitigated with reproducible builds and two-person signing approval. HSM loss gets mitigated with an encrypted backup under split custody. Meter clock drift gets mitigated with a tolerance window. A residual risk, physical tampering with individual meters, is accepted with monitoring because per-meter keys limit its impact. Decisions and owners are recorded. The register is revisited after every incident or major change.

### Worked example

Aiyana's analysis lists build-server compromise, stolen meter keys, insider export, certificate expiry, clock drift and HSM loss, ranks them and assigns treatments with owners.

> **Synthetic case.** The threats and scores are invented.

### Errors and limits

Scores are judgements, not measurements; record reasoning. Ignoring non-malicious failures misses many real outages.

### Exercises

- **EX067 — Build-server threat.** Why is build-server compromise serious for firmware? *Rubric:* 3 = malicious code could be signed legitimately and accepted by meters;; 2 = signing abuse;; 1 = minor;; 0 = none.
- **EX068 — Failure example.** Give two non-malicious failure modes. *Rubric:* 3 = two of certificate expiry, clock drift, HSM loss, faulty RNG;; 2 = one;; 1 = an attack;; 0 = none.
- **EX069 — HSM loss treatment.** How is HSM loss treated? *Rubric:* 3 = encrypted backup under split custody;; 2 = backup;; 1 = accept;; 0 = none.

### Synthesis

Pairing threat analysis with failure analysis and explicit treatments gives a balanced, owned risk picture for the trust service.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Cryptography and trust services: methods I

### Learning outcomes

You will (1) derive many keys from one master key with HKDF; (2) verify an implementation against published test vectors; (3) separate keys by purpose with context information.

### 24.1 Why derive keys

Ridgeway needs separate keys for each meter and each purpose. Storing 50,000 random keys is possible, but deriving them from a master key in the key service simplifies backup and provisioning. HKDF, specified in RFC 5869, does this in two steps: extract concentrates the entropy of input keying material into a pseudorandom key using HMAC with a salt, and expand produces as many output bytes as needed, bound to an info string describing the purpose. Different info strings yield independent keys, so a telemetry key cannot be confused with a firmware key.

### Lab — HKDF against RFC 5869

```python
"""Check HKDF-SHA256 against RFC 5869 test case 1 (teaching only: use a vetted library in production)."""
import hmac, hashlib

def hkdf(ikm, salt, info, length):
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()          # extract
    okm, t, i = b"", b"", 1
    while len(okm) < length:                                     # expand
        t = hmac.new(prk, t + info + bytes([i]), hashlib.sha256).digest(); okm += t; i += 1
    return prk, okm[:length]

def main():
    prk, okm = hkdf(bytes([0x0b]) * 22, bytes(range(13)), bytes(range(0xf0, 0xfa)), 42)
    want = "3cb25f25faacd57a90434f64d0362f2a2d2d0a90cf1a5a4c5db02d56ecc4c5bf34007208d5b887185865"
    print("PRK", prk.hex()[:32], "...")
    print("OKM matches RFC 5869 A.1:", okm.hex() == want)
    a = hkdf(b"utility-master-demo", b"salt", b"telemetry-tls", 16)[1].hex()
    b = hkdf(b"utility-master-demo", b"salt", b"firmware-sign", 16)[1].hex()
    print("different info, different keys:", a != b)

if __name__ == "__main__":
    main()
```

Run with `python3 lab_hkdf.py`. Verified output:

```text
PRK 077709362c2e32df0ddc3f0dc47bba63 ...
OKM matches RFC 5869 A.1: True
different info, different keys: True
```

### 24.2 Reading the HKDF run

The lab implements HKDF with hmac solely to make the two steps visible, and checks it against RFC 5869 test case A.1: the 42-byte output matches exactly. It then derives two keys from the same demonstration master with different info strings, telemetry-tls and firmware-sign, and confirms they differ. Aiyana writes beside the code that Ridgeway's production key service uses a vetted library's HKDF; the purpose of the exercise is to understand and verify behaviour, not to deploy a hand-written version. A matching test vector proves correct use, not side-channel safety.

### 24.3 Context and separation

Aiyana designs info strings carefully: they include purpose, meter identifier and key version, such as "ridgeway/reading-hmac/M-0417/v3". Including the version allows rotation by deriving a new key without changing the master. Including the meter identifier makes each meter's key unique. She warns against reusing one derived key for two purposes, such as tagging readings and encrypting configuration, because a weakness or misuse in one use could compromise the other. Key separation is a cheap, powerful design habit. She documents the label format so all teams derive keys identically.

### Worked example

Aiyana verifies HKDF behaviour against RFC 5869 A.1, then specifies info strings that encode purpose, meter identifier and version for per-meter, rotatable keys.

> **Synthetic case.** The master key and labels are invented; RFC 5869 and its test vector are real.

### Errors and limits

HKDF does not add entropy; a weak master key yields weak derived keys. Hand-written versions are for learning only.

### Exercises

- **EX070 — Extract and expand.** What do HKDF's two steps do? *Rubric:* 3 = extract makes a pseudorandom key from input material with a salt; expand outputs bytes bound to info;; 2 = one step;; 1 = encryption;; 0 = none.
- **EX071 — Test vector result.** What did the lab print for the RFC 5869 check? *Rubric:* 3 = OKM matches RFC 5869 A.1: True;; 2 = True;; 1 = False;; 0 = none.
- **EX072 — Info string design.** What does Aiyana put in info strings and why include the version? *Rubric:* 3 = purpose, meter identifier, version; version enables rotation without changing master;; 2 = partial;; 1 = random;; 0 = none.

### Synthesis

HKDF derives many separated, rotatable keys from one well-protected master, and test vectors confirm correct use.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) produce a first integrated design for meter reading authentication; (2) present it for critique; (3) revise it based on feedback.

### 25.1 The studio brief

In the first design studio, Aiyana's team must design end-to-end authentication of readings from meter to billing, using what earlier chapters taught: per-meter keys derived with HKDF, canonical reading formats, HMAC tags, TLS between collectors and gateway, and key state checks. The brief includes constraints: each reading message may add at most 32 bytes, meters wake for two seconds per hour, and the system must tolerate collectors being offline for a day. The team works on whiteboards before writing any document.

### 25.2 The first design

The team's design truncates HMAC tags to 16 bytes to fit the size limit, includes a monotonically increasing counter in each reading to prevent replay, and has collectors buffer readings during outages. Billing verifies the tag, checks the counter is higher than the last accepted one, and checks the key's state. Aiyana justifies 16-byte tags: forging requires guessing 128 bits, far beyond feasible, and RFC 2104 allows truncation with care. She documents each design decision and the requirement it meets. The counter also lets billing spot gaps that hint at lost readings.

### 25.3 Critique and revision

Reviewers raise three issues. First, if a meter is replaced, the new meter's counter restarts, so billing would reject its readings; the team adds a key version to the message so counters reset with new keys. Second, buffered readings arrive out of order after outages; billing now accepts counters within a window and tracks gaps. Third, nothing records failed verifications; the team adds logging and the alert from Chapter 17. Aiyana learns that critique finds operational problems that design documents rarely reveal.

### Worked example

The team's design uses 16-byte truncated HMAC tags with counters, then revises for meter replacement, out-of-order buffered readings and missing failure logs.

> **Synthetic case.** The studio and reviewers are invented.

### Errors and limits

Truncation reduces forgery resistance; never truncate below what the threat model allows. Replay counters need careful handling of resets.

### Exercises

- **EX073 — Tag truncation.** Why is a 16-byte truncated tag acceptable here? *Rubric:* 3 = forgery requires guessing 128 bits; RFC 2104 allows careful truncation;; 2 = 128 bits;; 1 = unsafe;; 0 = none.
- **EX074 — Replay defence.** How does the design stop replayed readings? *Rubric:* 3 = monotonically increasing counter checked by billing;; 2 = counter;; 1 = timestamps only;; 0 = none.
- **EX075 — Replacement fix.** How did the team fix counter resets on replacement meters? *Rubric:* 3 = added key version so counters reset with new keys;; 2 = version;; 1 = ignore;; 0 = none.

### Synthesis

Studio critique turns a correct-looking design into an operable one by exposing replacement, ordering and monitoring gaps.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Cryptography and trust services: architecture alternatives

### Learning outcomes

You will (1) compare symmetric and public-key architectures for meters; (2) evaluate a managed cloud key service against on-premises HSMs; (3) document trade-offs.

### 26.1 Symmetric versus public key

Aiyana compares two architectures for reading authentication. The symmetric design uses HMAC with keys derived in the key service: small tags, low meter energy, but the service holds every key. The public-key design gives each meter a signing key pair with Ed25519 from RFC 8032: billing verifies with public keys and the central service holds no secrets, but signatures are 64 bytes and signing costs more energy. She measures both against constraints and threat model, and finds the symmetric design fits the 32-byte limit while the public-key design reduces central risk.

### 26.2 Managed or on-premises

For the key service itself, Aiyana compares a managed cloud key service with on-premises hardware security modules. The cloud option offers high availability and less maintenance, but places key custody with a provider and depends on network connectivity. On-premises HSMs keep custody in house but require skilled staff, ceremonies and replacement cycles. She lists regulatory constraints: the regulator requires that keys for billing remain under the utility's control. Both options can satisfy this with the right contracts and key-wrapping designs, so cost and staffing decide.

### 26.3 Documenting trade-offs

Aiyana writes an alternatives analysis with a table of criteria: security, energy, message size, availability, cost, staff skills and migration path. She scores each option and explains the scores in prose. The recommendation is symmetric HMAC for readings, Ed25519 or ECDSA for firmware, and on-premises HSMs for the firmware root with a managed service for derived reading keys. She records which future change would reverse each decision, for example larger radio frames making signatures feasible for readings. Reviewers can then challenge a score without rejecting the whole analysis.

### Worked example

Aiyana's alternatives table recommends HMAC for readings, signatures for firmware, an on-premises HSM for the firmware root and a managed service for derived keys, with reversal conditions.

> **Synthetic case.** The options and scores are invented; RFC 8032 is real.

### Errors and limits

Scores hide assumptions; explain them. Cloud custody needs contractual and technical controls, not trust alone.

### Exercises

- **EX076 — Signature size.** Why did the public-key design not fit readings? *Rubric:* 3 = Ed25519 signatures are 64 bytes, exceeding the 32-byte limit;; 2 = size;; 1 = speed;; 0 = none.
- **EX077 — Regulatory constraint.** What regulatory constraint affects the key service choice? *Rubric:* 3 = billing keys must remain under the utility's control;; 2 = custody;; 1 = none;; 0 = none.
- **EX078 — Reversal condition.** Give a condition that would reverse the readings decision. *Rubric:* 3 = larger radio frames making signatures feasible;; 2 = frames bigger;; 1 = none;; 0 = none.

### Synthesis

Comparing architectures openly, with criteria, scores and reversal conditions, leads to a defensible mix of symmetric and public-key designs.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Cryptography and trust services: control design

### Learning outcomes

You will (1) design preventive, detective and corrective controls for keys; (2) specify a key ceremony; (3) map controls to risks.

### 27.1 Three types of control

Aiyana designs controls in three types. Preventive controls stop problems: HSMs prevent key export, state checks prevent use of retired keys, and code review prevents hard-coded secrets. Detective controls notice problems: verification-failure alerts, inventory scans for unknown keys and Certificate Transparency monitoring under RFC 6962. Corrective controls recover: revocation, re-keying procedures and restoring from encrypted backups. A balanced set matters because preventive controls eventually fail and detection without correction only documents harm. She checks that every high risk has at least one control of each type, and flags any risk that relies on prevention alone.

### 27.2 The key ceremony

For generating the firmware root key, Aiyana specifies a ceremony: an offline HSM in a secured room, three custodians each holding a smart card, a witness from audit, a written script, video recording of the room but not of screens showing secrets, and signed minutes. The key is generated inside the HSM and backed up in encrypted form split among custodians, so that two of three are needed for recovery. The ceremony's purpose is to produce evidence, to regulators and future engineers, that no single person ever had the root key.

### 27.3 Mapping controls to risks

Aiyana maps each risk from Chapter 23 to its controls. Build-server compromise maps to reproducible builds, two-person release approval and signature logging. Stolen meter keys map to per-meter derivation, verification alerts and revocation. Insider export maps to HSM non-exportability, dual control and audit logs. The map reveals one risk, meter clock drift, with only a corrective control; she adds a detective control that tracks timestamp skew. Gaps found on paper are cheaper to fix than gaps found in incidents. The map is kept beside the risk register and updated together with it.

### Worked example

Aiyana lists preventive, detective and corrective controls, specifies a three-custodian root key ceremony, and maps controls to risks, closing a clock-drift detection gap.

> **Synthetic case.** The ceremony details are invented; RFC 6962 is real.

### Errors and limits

Ceremonies fail if scripts are ignored under time pressure. Controls mapped on paper still need testing.

### Exercises

- **EX079 — Control types.** Give one preventive, one detective and one corrective control. *Rubric:* 3 = e.g. HSM non-export, verification alerts, revocation;; 2 = two;; 1 = one;; 0 = none.
- **EX080 — Ceremony purpose.** What is the purpose of the key ceremony? *Rubric:* 3 = produce evidence that no single person ever had the root key;; 2 = evidence;; 1 = speed;; 0 = none.
- **EX081 — Gap found.** Which gap did the risk map reveal and how was it closed? *Rubric:* 3 = clock drift had only corrective control; added skew-tracking detective control;; 2 = gap named;; 1 = none;; 0 = none.

### Synthesis

Balanced preventive, detective and corrective controls, evidenced by ceremonies and mapped to risks, keep the trust service resilient.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Cryptography and trust services: implementation I

### Learning outcomes

You will (1) implement firmware verification with a hash manifest and signature; (2) explain why the manifest must be signed; (3) integrate verification into the update process.

### 28.1 The firmware update path

Aiyana implements the first part of the firmware update path. The build system produces an image and a manifest containing the version and the image's SHA-256 digest. The manifest is signed with the intermediate signing key. Meters download both, verify the manifest signature against the embedded root and intermediate chain, check the version is newer, then hash the image and compare it with the manifest digest. Only if every check passes does the meter write the image to its inactive slot and reboot into it.

### Lab — Manifest check

```python
"""Verify a synthetic firmware image against a SHA-256 manifest before install (FIPS 180-4)."""
import hashlib
IMAGE = b"RIDGEWAY-METER-FW v3.2.1\n" + bytes(range(256)) * 4
MANIFEST = {"version": "3.2.1", "sha256": hashlib.sha256(IMAGE).hexdigest()}

def check(img):
    return hashlib.sha256(img).hexdigest() == MANIFEST["sha256"]

def main():
    print("manifest digest", MANIFEST["sha256"][:20], "...")
    print("intact image accepted:", check(IMAGE))
    bad = bytearray(IMAGE); bad[100] ^= 1
    print("one flipped bit accepted:", check(bytes(bad)))
    print("note: the manifest itself must be signed, or an attacker swaps both")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_manifest.py`. Verified output:

```text
manifest digest 29de505e903e58072161 ...
intact image accepted: True
one flipped bit accepted: False
note: the manifest itself must be signed, or an attacker swaps both
```

### 28.2 Reading the manifest check

The lab computes the SHA-256 digest of a synthetic image and stores it in a manifest. The intact image is accepted; flipping a single bit makes the check fail, illustrating the avalanche property of FIPS 180-4 hashes. The lab's last line states the key lesson: a hash alone proves only that the image matches the manifest. An attacker who can replace both the image and an unsigned manifest wins easily. The signature over the manifest, made with ECDSA or Ed25519 in a vetted library, is what ties the digest to Ridgeway.

### 28.3 Integration details

Aiyana handles practical details. Meters keep two firmware slots so a failed update can roll back to the previous version without bricking. Verification happens before writing and again at boot. Large images are hashed in chunks to fit meter memory, using hashlib's incremental update method. Meters report the installed version and verification outcome, feeding the firmware success measure from Chapter 20. She documents that signature verification uses the vendor's certified library on the meter, not her own code. Reports of failed verifications go to the alerting system described earlier.

### Worked example

Aiyana implements manifest-based verification with signature, version check, dual slots and boot-time recheck, and shows that one flipped bit fails the hash.

> **Synthetic case.** The image and manifest are invented; FIPS 180-4 is real.

### Errors and limits

A hash without a signature authenticates nothing against an active attacker. Dual slots need rollback protection so attackers cannot force old versions.

### Exercises

- **EX082 — Verification order.** List the checks a meter performs before installing firmware. *Rubric:* 3 = manifest signature chain, newer version, image hash matches manifest;; 2 = two;; 1 = one;; 0 = none.
- **EX083 — Flipped bit.** What happened when one bit was flipped? *Rubric:* 3 = the image was rejected (accepted: False);; 2 = rejected;; 1 = accepted;; 0 = none.
- **EX084 — Unsigned manifest.** Why must the manifest be signed? *Rubric:* 3 = otherwise an attacker swaps both image and manifest;; 2 = swap;; 1 = no need;; 0 = none.

### Synthesis

Firmware verification links a hash of the image to a signed manifest, checked before install and at boot, with safe rollback slots.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Cryptography and trust services: measurement

### Learning outcomes

You will (1) measure key-management health with inventory data; (2) report overdue keys against cryptoperiods; (3) build a measurement dashboard that drives action.

### 29.1 What to measure

Aiyana designs metrics for the trust service: share of keys within their cryptoperiod, days to expiry for certificates, verification failure rates, firmware version spread across meters, and time to revoke a compromised key in exercises. SP 800-57 Part 1 recommends cryptoperiods for key types; measuring adherence turns that guidance into management information. Each metric has a definition, data source and target, so two analysts produce the same number from the same data. She keeps the list short, because a dashboard with fifty metrics hides the few that matter, and agrees each definition with the team that owns the data.

### Lab — Cryptoperiod audit

```python
"""Key inventory ages against a 365-day cryptoperiod (synthetic utility keys, fixed audit date)."""
from datetime import date
AUDIT = date(2026, 6, 30); PERIOD = 365
KEYS = [("telemetry-tls", date(2026, 1, 10)), ("fw-signing", date(2024, 2, 1)),
        ("db-at-rest", date(2025, 9, 1)), ("webhook-hmac", date(2025, 5, 20)), ("backup-wrap", date(2023, 11, 5))]

def main():
    over = 0
    for name, made in KEYS:
        age = (AUDIT - made).days; late = age > PERIOD; over += late
        print(f"{name:<14} age {age:>4} d {'OVERDUE' if late else ''}")
    print(f"overdue {over}/{len(KEYS)}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_rotation.py`. Verified output:

```text
telemetry-tls  age  171 d 
fw-signing     age  880 d OVERDUE
db-at-rest     age  302 d 
webhook-hmac   age  406 d OVERDUE
backup-wrap    age  968 d OVERDUE
overdue 3/5
```

### 29.2 Reading the audit

On the synthetic audit date of 30 June 2026, three of five sampled keys exceed a 365-day cryptoperiod: the firmware signing intermediate at 880 days, the webhook HMAC key at 406 and the backup wrapping key at 968. Only the telemetry TLS key and the database key are within period. Aiyana does not panic: an overdue key is not necessarily compromised, but the longer a key is used, the more data it protects and the greater the impact of undiscovered exposure. She schedules rotations by risk, starting with the firmware intermediate.

### 29.3 Dashboards that drive action

Aiyana's dashboard shows each metric with its target, trend and owner. Overdue keys appear as a list with owners and planned rotation dates, not just a percentage. Monthly reviews ask why metrics moved. She avoids vanity metrics, such as counting keys generated, which say nothing about safety. When the firmware intermediate is rotated, the dashboard records the change, and the overdue share drops from three of five to two of five, giving the team visible progress. Owners must explain any red item at the next review.

### Worked example

Aiyana's audit finds three of five keys overdue, schedules rotation starting with the firmware intermediate, and builds a dashboard of owned metrics with targets.

> **Synthetic case.** The keys and dates are invented; SP 800-57 Part 1 is real.

### Errors and limits

Metrics can encourage gaming, such as renaming keys to reset ages. Cryptoperiods are guidance to be adapted to risk, not universal constants.

### Exercises

- **EX085 — Overdue keys.** Which sampled keys were overdue and by age? *Rubric:* 3 = fw-signing 880, webhook-hmac 406, backup-wrap 968 days;; 2 = names;; 1 = count only;; 0 = none.
- **EX086 — Overdue meaning.** Does overdue mean compromised? Explain. *Rubric:* 3 = no; longer use increases data protected and impact of undetected exposure;; 2 = no;; 1 = yes;; 0 = none.
- **EX087 — Vanity metric.** Give an example of a vanity metric Aiyana avoids. *Rubric:* 3 = counting keys generated;; 2 = similar;; 1 = real metric;; 0 = none.

### Synthesis

Measuring adherence to cryptoperiods and other key-health metrics, with owners and targets, turns standards into action.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) plan verification of cryptographic controls; (2) run negative tests against reading authentication; (3) record evidence for assurance.

### 30.1 Planning verification

In the first verification laboratory, Aiyana's team tests the reading authentication design on a bench with ten test meters, a collector and a copy of the billing verifier. The test plan lists each requirement, the test, expected result and evidence to keep. Tests run in an isolated network with synthetic keys, never production keys. The plan also states what is out of scope, such as physical tampering, which a later laboratory covers, so that results are not over-interpreted. Each test is reviewed by a second engineer before it runs.

### 30.2 Negative testing

The team runs negative tests: altered readings, replayed readings with old counters, readings tagged with a revoked key, readings with truncated tags and readings from a meter identifier bound to a different key. Each must be rejected and logged. One test fails: readings tagged with a revoked key are accepted for up to an hour because the verifier caches key states. The team reduces the cache time to one minute and adds an explicit revocation push. Finding this on a bench costs far less than finding it in production.

### 30.3 Recording evidence

For each test the team records inputs, outputs, logs, software versions and the tester's name, and stores them in a tamper-evident archive with SHA-256 digests. Aiyana writes a summary: twenty-four tests, twenty-three passed initially, one failed and was fixed and retested. Evidence supports the regulator's review and future regression testing. She stresses that passing tests shows the absence of known defects under tested conditions, not the absence of all defects. The archive is read-only for testers, so results cannot be quietly edited after the fact, and every retest is added as a new entry.

### Worked example

The laboratory runs twenty-four tests; a cached revocation flaw is found and fixed by shortening the cache and pushing revocations, and evidence is archived with digests.

> **Synthetic case.** The laboratory and results are invented.

### Errors and limits

Bench tests use idealised conditions; field behaviour may differ. Tests with production keys risk real exposure.

### Exercises

- **EX088 — Isolation rule.** What keys and network does the laboratory use? *Rubric:* 3 = synthetic keys in an isolated network, never production keys;; 2 = synthetic;; 1 = production;; 0 = none.
- **EX089 — Revocation flaw.** What failed and how was it fixed? *Rubric:* 3 = revoked-key readings accepted for an hour due to cache; cache cut to one minute plus revocation push;; 2 = failure only;; 1 = fix only;; 0 = none.
- **EX090 — Limits of passing.** What does passing all tests show? *Rubric:* 3 = absence of known defects under tested conditions, not all defects;; 2 = limited;; 1 = proves security;; 0 = none.

### Synthesis

Planned negative testing with archived evidence finds real flaws early and supports honest assurance claims.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Cryptography and trust services: implementation II

### Learning outcomes

You will (1) deploy TLS 1.3 for collectors with mutual authentication; (2) automate certificate issuance and renewal; (3) avoid common TLS configuration errors.

### 31.1 Mutual TLS for collectors

Collectors connect to Ridgeway's gateway using TLS 1.3 from RFC 8446 with mutual authentication: the gateway presents its certificate and each collector presents a client certificate issued by Ridgeway's device authority. The gateway checks that the certificate chains to the device authority, has not expired and is not revoked, and maps its subject to a collector record. Aiyana configures the gateway to accept only TLS 1.3, removing older versions and their legacy cipher suites, which simplifies configuration and eliminates whole classes of downgrade problems.

### 31.2 Automating certificates

Collector certificates last ninety days and renew automatically through an internal ACME service, using the protocol from RFC 8555. Each collector generates its key pair locally, so the private key never leaves the device, and requests a certificate by proving control of its identity. Renewal starts when a third of the lifetime remains. Failed renewals raise alerts, following the lesson that automation can fail silently. Aiyana tests renewal by advancing a test collector's clock and confirming that it renews and that the gateway accepts the new certificate.

### 31.3 Configuration pitfalls

Aiyana lists TLS mistakes she checks for: disabling certificate verification in clients to get past an error; trusting the operating system's public roots for device certificates instead of only Ridgeway's authority; skipping hostname or identity checks; and using one certificate key across many collectors. She writes automated configuration tests that connect with an expired certificate, a certificate from another authority and a revoked certificate, and confirms each is rejected. These tests run whenever gateway configuration changes. A failing test blocks deployment until someone fixes the cause.

### Worked example

Aiyana deploys TLS 1.3-only mutual authentication with ninety-day ACME certificates generated on device, and adds configuration tests for expired, foreign and revoked certificates.

> **Synthetic case.** The device authority is invented; RFC 8446 and RFC 8555 are real.

### Errors and limits

Mutual TLS adds certificate management burden; automation must be monitored. Trusting public roots for private device identity lets outsiders authenticate.

### Exercises

- **EX091 — Mutual authentication.** What does mutual TLS add for collectors? *Rubric:* 3 = collectors present client certificates from Ridgeway's device authority, checked by the gateway;; 2 = client cert;; 1 = encryption;; 0 = none.
- **EX092 — Key generation location.** Where are collector private keys generated and why? *Rubric:* 3 = on the collector, so keys never leave the device;; 2 = locally;; 1 = central;; 0 = none.
- **EX093 — Root pitfall.** Why not trust public roots for device certificates? *Rubric:* 3 = anyone with a public certificate could authenticate as a device; trust only Ridgeway's authority;; 2 = outsiders;; 1 = fine;; 0 = none.

### Synthesis

Mutual TLS with automated, device-generated certificates and tested configurations secures collector links without manual toil.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Cryptography and trust services: reliability

### Learning outcomes

You will (1) model the availability of key custodians and services; (2) choose quorum sizes for recovery; (3) design redundancy without weakening security.

### 32.1 Reliability of people and services

A key that cannot be used when needed is a reliability failure. Aiyana models the firmware root recovery process, which requires custodians with smart cards. If only one custodian holds the root backup, the root is unavailable whenever that person is ill or travelling, and lost if they leave. If all five must be present, availability falls sharply. Quorum schemes, where any m of n custodians suffice, balance the two. She uses probability to choose m and n, given each custodian's availability.

### Lab — Custodian quorum

```python
"""Probability that at least m of n key custodians are reachable (each independently with prob a)."""
from math import comb

def at_least(m, n, a):
    return sum(comb(n, k) * a ** k * (1 - a) ** (n - k) for k in range(m, n + 1))

def main():
    for m, n in [(1, 1), (2, 3), (3, 5), (5, 5)]:
        print(f"{m}-of-{n}, each 0.90 reachable: P = {at_least(m, n, 0.90):.4f}")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_quorum.py`. Verified output:

```text
1-of-1, each 0.90 reachable: P = 0.9000
2-of-3, each 0.90 reachable: P = 0.9720
3-of-5, each 0.90 reachable: P = 0.9914
5-of-5, each 0.90 reachable: P = 0.5905
```

### 32.2 Reading the quorum results

With each custodian reachable 90 percent of the time, a single custodian gives 0.90 availability, two of three gives 0.972, three of five gives 0.9914, and requiring all five gives only 0.5905. Requiring everyone is worse than a single person. Aiyana recommends three of five for the root: high availability, and no two custodians can collude to recover the key alone. The HSM vendor's key-splitting feature implements the split; she does not implement secret sharing herself, consistent with the rule against home-made cryptography. Her choice is recorded in the key-management policy.

### 32.3 Redundancy for services

For the online key service, Aiyana designs active-standby replicas in two data centres with keys replicated in encrypted form between HSMs of the same model. Replication uses the vendor's secure key-transfer mechanism, so keys never appear in plain text. Failover is tested quarterly. She records a trade-off: more replicas mean more places to secure and audit. She limits replicas to two sites and requires the same physical controls at both. Reliability and security reinforce each other only when redundancy is designed with the same rigour as the primary.

### Worked example

Aiyana chooses a three-of-five custodian quorum (0.9914 availability) implemented by the HSM vendor, and active-standby key service replicas in two sites with quarterly failover tests.

> **Synthetic case.** Availability figures are invented assumptions.

### Errors and limits

Independence assumptions fail if custodians travel together or share a building. More replicas increase attack surface.

### Exercises

- **EX094 — All-five quorum.** What availability does requiring all five custodians give, and why is it bad? *Rubric:* 3 = 0.5905, worse than a single custodian;; 2 = number;; 1 = good;; 0 = none.
- **EX095 — Recommended quorum.** What quorum does Aiyana recommend and why? *Rubric:* 3 = three of five: 0.9914 availability and no two can collude;; 2 = 3-of-5;; 1 = 1-of-1;; 0 = none.
- **EX096 — Splitting implementation.** Who implements the key split and why? *Rubric:* 3 = the HSM vendor's feature, avoiding home-made cryptography;; 2 = vendor;; 1 = Aiyana;; 0 = none.

### Synthesis

Quorum and redundancy designs keep keys available without concentrating power, provided they are built on vetted mechanisms and tested.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Cryptography and trust services: safety and resilience

### Learning outcomes

You will (1) design safe behaviour when cryptographic checks fail; (2) plan for compromise of signing keys; (3) build resilience into meters and services.

### 33.1 Failing safely

Building on Chapter 10, Aiyana specifies behaviour for every cryptographic failure. If a reading's tag fails, billing stores it in quarantine and alerts, rather than discarding it, so evidence remains. If a firmware signature fails, the meter keeps its current firmware and reports. If a collector certificate expires, the collector buffers readings for up to seven days while alerting operations, so readings are delayed but not lost. Each behaviour is tested. The goal is that cryptographic failures cause visible, recoverable delays rather than silent data loss or unsafe states.

### 33.2 Signing key compromise

Aiyana plans for the worst case: the firmware intermediate signing key leaks. The response runbook revokes the intermediate by publishing a signed revocation from the offline root, issues a new intermediate in a ceremony, re-signs current firmware and pushes an update that installs the new intermediate's trust. Because meters check the chain against the root, the revoked intermediate becomes useless. She estimates the time to complete the response and practises it in a tabletop exercise, identifying slow steps such as convening custodians at short notice.

### 33.3 Resilience features

Aiyana adds features that help the system survive surprises: meters hold two trust anchors, the current root and a pre-provisioned backup root stored offline in a separate ceremony, so loss of the primary root is survivable; firmware supports algorithm agility, allowing a future post-quantum signature scheme from FIPS 204 or FIPS 205; and collectors can fall back to a second gateway. Resilience costs money and complexity, so each feature is linked to a specific risk from the analysis. Each feature is reviewed yearly to confirm its risk still exists.

### Worked example

Aiyana specifies quarantine for failed readings, keep-current behaviour for failed firmware, seven-day buffering for expired collector certificates, and a rehearsed intermediate-key compromise runbook with a backup root.

> **Synthetic case.** The runbook and features are invented; FIPS 204 and FIPS 205 are real.

### Errors and limits

Backup roots must be protected as carefully as primaries. Untested runbooks fail under pressure.

### Exercises

- **EX097 — Failed tag behaviour.** What happens to a reading whose tag fails? *Rubric:* 3 = quarantined with alert, not discarded, preserving evidence;; 2 = quarantine;; 1 = discarded;; 0 = none.
- **EX098 — Intermediate compromise.** Summarise the response to a leaked firmware intermediate key. *Rubric:* 3 = root-signed revocation, new intermediate in ceremony, re-sign firmware, push new trust;; 2 = partial;; 1 = ignore;; 0 = none.
- **EX099 — Backup root.** Why do meters hold a backup root? *Rubric:* 3 = loss or compromise of the primary root remains survivable;; 2 = resilience;; 1 = none;; 0 = none.

### Synthesis

Safe failure behaviour, rehearsed compromise response and planned resilience let cryptographic systems degrade gracefully.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Cryptography and trust services: integration

### Learning outcomes

You will (1) integrate the trust service with billing, field operations and monitoring; (2) define interface contracts; (3) test end-to-end flows.

### 34.1 Integration points

The trust service touches many systems: billing verifies readings, field operations provisions replacement meters, monitoring receives alerts, the build system requests firmware signatures and identity management controls staff access. Aiyana lists each integration with its data, protocol and authentication. She finds that field operations' handheld tool needs to request a new meter key during replacement, which had not been designed. Integration analysis surfaces such missing flows before rollout, when changing interfaces is still cheap. She records each flow in a shared table that the owning teams review together.

### 34.2 Interface contracts

For each integration Aiyana writes a contract: request and response formats, error codes, rate limits, authentication method and what happens on timeout. The signing contract states that the build system submits a manifest digest, not the whole image, and receives a signature only if two approvers have authorised the release. The key-provisioning contract states that handheld tools never receive meter keys; they receive an encrypted blob that only the target meter's secure element can unwrap. Contracts let teams work independently while preserving security properties.

### 34.3 End-to-end tests

Aiyana runs end-to-end tests that cross every integration: provision a replacement meter, take a reading, verify it in billing, push a firmware update, revoke the old meter and confirm its readings are rejected. Tests run in a staging environment with synthetic keys. One test reveals that billing still accepts the old meter's readings because the revocation event goes to monitoring but not to billing. The fix routes revocations through a message queue that all verifiers subscribe to. Such tests run before every release of any connected system.

### Worked example

Aiyana maps five integrations, writes contracts for signing and provisioning, and finds through end-to-end testing that revocation events never reached billing.

> **Synthetic case.** The systems are invented.

### Errors and limits

Contracts drift unless tested automatically. End-to-end tests are slow, so keep them focused on security-critical flows.

### Exercises

- **EX100 — Missing flow.** Which flow was missing before integration analysis? *Rubric:* 3 = handheld tool requesting a new meter key during replacement;; 2 = provisioning;; 1 = none;; 0 = none.
- **EX101 — Handheld blob.** Why do handheld tools receive an encrypted blob instead of a key? *Rubric:* 3 = only the meter's secure element can unwrap it, so handhelds never hold keys;; 2 = protect key;; 1 = speed;; 0 = none.
- **EX102 — Revocation routing.** What did end-to-end testing reveal about revocation, and what fixed it? *Rubric:* 3 = revocations reached monitoring but not billing; route through queue all verifiers subscribe to;; 2 = finding only;; 1 = fix only;; 0 = none.

### Synthesis

Integration with explicit contracts and end-to-end tests makes the trust service work across systems without leaking keys or missing events.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) redesign the system for a new requirement; (2) evaluate post-quantum readiness; (3) present a migration plan for critique.

### 35.1 The new requirement

In the second design studio, the regulator announces that utilities must plan migration of long-lived signatures to post-quantum algorithms. Meters last fifteen years, so firmware signed today must remain verifiable and secure until about 2041. Aiyana's team must redesign firmware signing so meters can accept post-quantum signatures without hardware replacement. They read FIPS 204 for ML-DSA and FIPS 205 for SLH-DSA, noting that both produce much larger signatures and keys than Ed25519 or ECDSA. The team also reads NIST's transition guidance so its plan matches expected timelines, and records which meter generations can be updated in the field.

### 35.2 Evaluating options

The team compares options. ML-DSA offers moderate signature sizes of a few kilobytes and fast verification; SLH-DSA relies only on hash functions, offering conservative security assumptions, with larger signatures. A hybrid scheme requires both a classical and a post-quantum signature to verify, protecting against failure of either. For firmware, size matters less than for readings because updates are infrequent. The team proposes hybrid ECDSA plus ML-DSA signatures on manifests, with meters accepting firmware only when both verify, and a later phase dropping the classical signature.

### 35.3 Critique and plan

Reviewers question whether meters have enough memory and flash to verify post-quantum signatures. The team measures with the vendor's library on a test meter and finds verification fits but needs a firmware update to the bootloader, which itself must be signed classically. They write a migration plan: update bootloaders with classical signatures now, introduce hybrid manifests next, and retire classical-only verification after confidence grows. Each step has a rollback. Reviewers accept the plan with a request to track NIST guidance on transition timelines.

### Worked example

The team proposes hybrid ECDSA plus ML-DSA manifest signatures, verifies feasibility on a test meter, and stages migration through a classically signed bootloader update.

> **Synthetic case.** The regulator's rule and measurements are invented; FIPS 204 and FIPS 205 are real.

### Errors and limits

Hybrid schemes add complexity and size; they must be designed by experts and implemented with vetted libraries. Timelines change, so plans need review.

### Exercises

- **EX103 — Why plan now.** Why must Ridgeway plan post-quantum firmware signing now? *Rubric:* 3 = meters last fifteen years, so signatures must stay secure until about 2041;; 2 = long life;; 1 = no need;; 0 = none.
- **EX104 — Hybrid rule.** How does the proposed hybrid scheme accept firmware? *Rubric:* 3 = only when both ECDSA and ML-DSA signatures verify;; 2 = both;; 1 = either;; 0 = none.
- **EX105 — Bootloader step.** Why does the plan begin with a bootloader update? *Rubric:* 3 = verification of PQ signatures needs updated bootloader, itself signed classically;; 2 = bootloader;; 1 = skip;; 0 = none.

### Synthesis

Post-quantum readiness for long-lived devices needs early, staged, hybrid migration grounded in measurement and standards.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Cryptography and trust services: performance and scale

### Learning outcomes

You will (1) estimate cryptographic workload at fleet scale; (2) tune password hashing and verification costs; (3) plan capacity for peaks.

### 36.1 Fleet workload

Aiyana estimates load: 50,000 meters reporting hourly produce about 1.2 million readings per day, each needing an HMAC verification. HMAC-SHA256 on short messages takes microseconds on modern servers, so verification is cheap; the bottleneck is database writes and key lookups. She designs a cache of derived keys in the verifier's protected memory, refreshed when keys rotate. Estimating first prevents wasted optimisation of the cryptography when the real cost lies elsewhere. She confirms the estimate with a load test in staging, which shows HMAC using under one percent of processor time while the database queue grows during bursts.

### 36.2 Password hashing costs

The customer portal uses Argon2id from RFC 9106, which is deliberately slow. Aiyana tunes parameters so each login takes about half a second on the server and uses enough memory to slow attackers with specialised hardware. At peak, when bills are issued, thousands of customers log in within an hour. She calculates required server capacity and adds rate limiting per account and per network address, so attackers cannot use logins to exhaust resources. Tuning balances user experience, capacity and resistance to offline guessing.

### 36.3 Planning for peaks

Firmware rollouts create peaks: if all 50,000 meters downloaded and verified at once, collectors would saturate. Aiyana staggers updates in waves of five percent, monitors verification outcomes, and pauses automatically if failures exceed a threshold. Certificate renewals are also spread by adding random jitter to renewal times, avoiding the situation where all collectors renew within the same minute. Capacity planning for cryptography is often about scheduling, not raw speed. She also rehearses a rollout pause so that operators know how to stop a wave quickly if verification failures rise during an update.

### Worked example

Aiyana estimates 1.2 million daily verifications, caches derived keys, tunes Argon2id to about half a second with rate limits, and staggers firmware and renewals.

> **Synthetic case.** Workload figures are invented; RFC 9106 is real.

### Errors and limits

Lowering password-hash cost to save capacity weakens protection. Caches of keys must be protected like the key service.

### Exercises

- **EX106 — Daily readings.** How many readings per day does the fleet produce? *Rubric:* 3 = about 1.2 million;; 2 = order right;; 1 = wrong;; 0 = none.
- **EX107 — Real bottleneck.** Where is the bottleneck for reading verification? *Rubric:* 3 = database writes and key lookups, not HMAC;; 2 = database;; 1 = HMAC;; 0 = none.
- **EX108 — Renewal jitter.** Why add jitter to certificate renewals? *Rubric:* 3 = to avoid all collectors renewing simultaneously and overloading services;; 2 = spread load;; 1 = security;; 0 = none.

### Synthesis

At scale, cryptographic performance depends on estimating load, tuning deliberate costs and scheduling peaks rather than on raw algorithm speed.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Cryptography and trust services: operations

### Learning outcomes

You will (1) write operational runbooks for routine key tasks; (2) run key rotation without downtime; (3) handle incidents involving keys.

### 37.1 Routine runbooks

Aiyana writes runbooks for routine tasks: rotating reading keys, renewing gateway certificates, adding a custodian, replacing an HSM and responding to verification-failure alerts. Each runbook lists preconditions, steps, checks and rollback. She tests each with an operator who did not write it, revising unclear steps. Runbooks turn expert knowledge into repeatable operations and reduce errors at 3 a.m., when incidents seem to happen. They also give auditors evidence that procedures exist and are followed. Each runbook names its owner and the date it was last exercised.

### 37.2 Rotation without downtime

Rotating reading keys for 50,000 meters cannot happen at once. Aiyana designs overlapping validity: the key service derives version 4 keys and pushes them to meters in waves; billing accepts tags from both version 3 and 4 during the transition; after all meters confirm, version 3 is deactivated and only used to verify historical readings. The key version in each message, added during Design studio I, makes this possible. Monitoring tracks the share of readings on the new version, giving operators a clear picture of progress.

### 37.3 Key incidents

When a technician reports a lost handheld tool, Aiyana's team follows the key incident runbook: confirm what the handheld could access, which is only encrypted blobs per Chapter 34; revoke the handheld's own credentials; review logs for misuse; and record the incident. Because handhelds never hold meter keys, no meter rotation is needed. She contrasts this with a hypothetical incident in which a key service administrator's credentials leak, requiring broader rotation. Designs that limit what each component holds make incidents small.

### Worked example

Aiyana's runbooks are tested by other operators, version 4 reading keys roll out with overlapping acceptance, and a lost handheld is contained without meter rotation.

> **Synthetic case.** Incidents and versions are invented.

### Errors and limits

Overlap periods that never end leave old keys active. Runbooks need updating after each use.

### Exercises

- **EX109 — Runbook testing.** How did Aiyana test runbooks? *Rubric:* 3 = an operator who did not write them followed them and unclear steps were revised;; 2 = tested;; 1 = not tested;; 0 = none.
- **EX110 — Overlapping validity.** How do reading keys rotate without downtime? *Rubric:* 3 = push v4 in waves, billing accepts v3 and v4, deactivate v3 after all confirm;; 2 = overlap;; 1 = all at once;; 0 = none.
- **EX111 — Lost handheld.** Why did the lost handheld require no meter rotation? *Rubric:* 3 = handhelds hold only encrypted blobs, never meter keys;; 2 = no keys;; 1 = luck;; 0 = none.

### Synthesis

Tested runbooks, overlapping rotation and designs that limit what components hold make cryptographic operations calm and incidents small.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Cryptography and trust services: validation

### Learning outcomes

You will (1) validate that the trust service meets stakeholder needs; (2) commission independent testing; (3) interpret validation results honestly.

### 38.1 Verification versus validation

Verification asks whether the system was built as specified; validation asks whether it meets the real needs. Aiyana's laboratories verified requirements. Validation asks stakeholders: Do technicians provision meters in under ten minutes? Do operators understand alerts? Does the regulator accept the evidence? She runs a field pilot with 500 meters in one district for three months, collecting data on each success measure from Chapter 20. Several requirements were met in the lab but not in the field, such as provisioning time when mobile signal is weak.

### 38.2 Independent testing

Ridgeway commissions an independent security firm to attempt to forge readings, install unsigned firmware and extract keys from a sample of meters, under a written authorisation and in a test district. The firm finds no way to forge readings or install unsigned firmware, but extracts a meter key from a prototype meter without a secure element, confirming the earlier decision to require secure elements. Independent testing brings attacker creativity the design team lacks and provides credible evidence to the regulator.

### 38.3 Honest interpretation

Aiyana writes the validation report. Provisioning met the ten-minute target in 91 percent of cases; failures came from weak signal, addressed by allowing offline provisioning with later synchronisation. Zero forged readings were accepted in testing, but she notes the test covered three months and one district. Firmware updates reached 97 percent of pilot meters within thirty days, below the 99 percent target, because some meters were unreachable in flooded pits. She reports misses as clearly as successes, with corrective actions. Corrective actions get owners and dates for the next review.

### Worked example

The 500-meter pilot and independent test show no forgery or unsigned firmware, confirm the secure-element decision, and report misses on provisioning and firmware reach with fixes.

> **Synthetic case.** The pilot, firm and figures are invented.

### Errors and limits

Validation in one district may not represent the whole service area. Independent tests are bounded by scope and time.

### Exercises

- **EX112 — Validation question.** How does validation differ from verification? *Rubric:* 3 = validation checks real stakeholder needs; verification checks build against specification;; 2 = difference partial;; 1 = same;; 0 = none.
- **EX113 — Key extraction.** What did the independent test extract and what did it confirm? *Rubric:* 3 = a key from a prototype without secure element, confirming the secure-element requirement;; 2 = finding;; 1 = none;; 0 = none.
- **EX114 — Firmware miss.** What firmware result missed its target and why? *Rubric:* 3 = 97 percent within thirty days versus 99, due to unreachable meters in flooded pits;; 2 = number;; 1 = reason;; 0 = none.

### Synthesis

Validation in the field, independent testing and honest reporting of misses show whether the trust service truly serves its stakeholders.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Cryptography and trust services: maintainability

### Learning outcomes

You will (1) design for cryptographic agility; (2) manage algorithm deprecation over time; (3) keep documentation and knowledge current.

### 39.1 Cryptographic agility

Algorithms age. SHA-1 moved from recommended to deprecated during the working lives of systems still in use. Aiyana designs Ridgeway's trust service for agility: messages and manifests carry algorithm identifiers; verifiers accept a configured set of algorithms; and keys are tagged with their algorithm in the inventory. Changing algorithms then becomes a configuration and rollout task rather than a redesign. She cautions that agility must not let attackers choose weak options, so verifiers refuse algorithms removed from the allowed list.

### 39.2 Managing deprecation

Aiyana sets up a deprecation process. Each year the security team reviews NIST guidance, such as SP 800-131A on transitioning algorithms and key lengths, and updates an approved-algorithms list with planned retirement dates. The inventory reports how many keys use each algorithm, so retirement can be planned. When an algorithm is scheduled for removal, the team first stops creating new keys with it, then migrates existing uses, then removes verification support after a grace period. Deprecation becomes routine rather than an emergency.

### 39.3 Documentation and knowledge

Maintainability also means people. Aiyana keeps architecture documents, decision records, runbooks and the inventory in one repository with change history. Each document has an owner and a review date. New engineers follow an onboarding path that includes a supervised key rotation in staging. She notes that many cryptographic incidents in older systems began when nobody remembered why a design was chosen, so knowledge management is a security control as real as an HSM. Review dates appear on the dashboard, so stale documents become visible.

### Worked example

Aiyana adds algorithm identifiers and allowed lists, an annual deprecation review based on SP 800-131A, and owned documentation with onboarding through a supervised rotation.

> **Synthetic case.** Ridgeway's process is invented; SP 800-131A is a real NIST publication.

### Errors and limits

Agility can introduce downgrade attacks if weak options remain accepted. Documentation without owners decays.

### Exercises

- **EX115 — Agility mechanism.** Name two mechanisms that give agility. *Rubric:* 3 = algorithm identifiers in messages, configured allowed lists, algorithm tags in inventory;; 2 = one;; 1 = none;; 0 = none.
- **EX116 — Deprecation steps.** What are the three steps of retiring an algorithm? *Rubric:* 3 = stop new keys, migrate existing uses, remove verification after grace period;; 2 = two;; 1 = one;; 0 = none.
- **EX117 — Knowledge risk.** Why is knowledge management a security control? *Rubric:* 3 = incidents start when nobody remembers why designs were chosen;; 2 = memory;; 1 = not;; 0 = none.

### Synthesis

Agility, routine deprecation and maintained knowledge keep a trust service secure through decades of algorithm and staff change.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) test physical and side-channel resistance of meters; (2) run a failure-injection test of the trust service; (3) document residual risk.

### 40.1 Physical testing

The second laboratory tests meters physically, with authorisation and on lab samples only. The team checks that secure elements resist simple probing and that debug ports are disabled in production builds. A specialised partner laboratory performs side-channel measurements on the HMAC operation in the secure element, confirming no measurable correlation with key bits within the test budget. Aiyana records that results apply to the tested hardware revision and that a new revision requires retesting. The team logs each sample's serial number so results can be tied to an exact revision.

### 40.2 Failure injection

The team injects failures into the staging trust service: the primary HSM is powered off, a collector's clock jumps a week ahead, the revocation queue is delayed and a corrupted firmware image is offered. Each injection checks that the designed safe behaviour from Chapter 33 occurs. The standby HSM takes over in forty seconds. The clock jump causes the collector to present a certificate as not yet valid, which the gateway rejects correctly, but the collector's alert message is unclear; the team rewrites it.

### 40.3 Residual risk

Aiyana writes a residual-risk statement: risks remaining after controls, why they are accepted and who accepted them. Examples include a determined, well-funded attacker extracting keys from a single meter with advanced equipment, accepted because per-meter keys limit impact; and a simultaneous loss of both data centres, accepted with an offline recovery plan of several days. Management signs the statement. Making residual risk explicit prevents the false impression that testing made the system perfectly secure. The statement is reviewed whenever the threat model changes, and at least once a year.

### Worked example

The laboratory confirms secure-element and debug-port protections, passes failure injections with a forty-second HSM failover, clarifies a clock-jump alert, and records signed residual risks.

> **Synthetic case.** Results are invented.

### Errors and limits

Side-channel tests are bounded by budget and technique. Residual risk statements must be revisited when threats change.

### Exercises

- **EX118 — Hardware scope.** What limit applies to the physical test results? *Rubric:* 3 = they apply to the tested hardware revision; new revisions need retesting;; 2 = revision;; 1 = universal;; 0 = none.
- **EX119 — Clock jump.** What did the clock-jump injection reveal? *Rubric:* 3 = certificate rejected as not yet valid correctly, but alert message unclear and rewritten;; 2 = alert;; 1 = failure;; 0 = none.
- **EX120 — Residual example.** Give one accepted residual risk and its rationale. *Rubric:* 3 = single-meter key extraction by advanced attacker, limited by per-meter keys (or both data centres lost, offline recovery);; 2 = example;; 1 = none;; 0 = none.

### Synthesis

Physical tests, failure injection and signed residual-risk statements complete verification with an honest account of what remains.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Cryptography and trust services: system optimization

### Learning outcomes

You will (1) optimise the trust service for cost and energy without weakening security; (2) reduce operational toil through automation; (3) evaluate optimisations against requirements.

### 41.1 Energy on meters

Meter batteries must last fifteen years. Aiyana measures energy per reading: radio transmission dominates, and the HMAC computation in the secure element costs a small fraction. She optimises by batching four hourly readings into one transmission with one tag covering the batch, reducing radio wake-ups. The batch tag covers every reading and its counter, so no reading can be removed or reordered undetected. She checks that batching does not violate the requirement that billing receives readings within six hours, and documents the trade-off in latency.

### 41.2 Reducing toil

Operations staff spend hours each month on manual certificate requests for internal web services outside the ACME system. Aiyana extends automated issuance to those services and adds a weekly report of certificates discovered by scanning that are not in the inventory. Manual steps fall by about two-thirds. She treats automation itself as a system to secure: the ACME service's own credentials are stored in the key service, and its issuance logs feed monitoring, so automation does not become an unmonitored path to certificates.

### 41.3 Evaluating optimisations

Each optimisation is evaluated against requirements before adoption. A proposal to shorten reading tags to 8 bytes for further energy savings is rejected: 64-bit forgery resistance is below the threat model's target, and savings are marginal since radio cost is driven by headers. A proposal to lower Argon2 parameters to cut server costs is also rejected. Aiyana records rejected optimisations with reasons, preventing the same ideas from returning without new evidence. Each rejected idea is stored with the data that disproved it, so a future proposer can see exactly what new evidence would be needed to reopen it.

### Worked example

Aiyana batches four readings under one tag to save energy, automates internal certificates to cut toil by two-thirds, and rejects 8-byte tags and weaker Argon2 parameters with recorded reasons.

> **Synthetic case.** Measurements are invented.

### Errors and limits

Optimisations that reduce security margins often look attractive in isolation. Batching changes latency and replay semantics, which must be retested.

### Exercises

- **EX121 — Batch tag coverage.** What must the batch tag cover and why? *Rubric:* 3 = every reading and its counter, so none can be removed or reordered undetected;; 2 = readings;; 1 = header only;; 0 = none.
- **EX122 — Automation security.** How is the automation itself secured? *Rubric:* 3 = ACME service credentials in the key service and issuance logs monitored;; 2 = logs;; 1 = not needed;; 0 = none.
- **EX123 — Rejected tag cut.** Why was shortening tags to 8 bytes rejected? *Rubric:* 3 = 64-bit forgery resistance below threat model target and savings marginal;; 2 = security;; 1 = cost;; 0 = none.

### Synthesis

Optimisation must save energy, money or toil while staying within security requirements, and rejected ideas deserve records too.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Cryptography and trust services: applied research

### Learning outcomes

You will (1) frame an applied research question from operational data; (2) design a small study with synthetic or authorised data; (3) report findings with limits.

### 42.1 A question from operations

Operational data shows that verification failures cluster on certain collectors at dawn. Aiyana frames an applied research question: are dawn failures caused by meter clock drift exceeding the timestamp tolerance after cold nights, rather than by attacks or radio noise? This question matters because widening tolerance weakens replay protection, while tightening it causes false rejections. Applied research in engineering answers questions that improve a specific system, using rigorous methods at a modest scale. Answering it could avoid both needless alerts and weaker protection.

### 42.2 Designing the study

Aiyana designs a study using authorised pilot data: for each failure she records collector, time, temperature from a public weather feed and the meter's reported clock offset. She defines in advance that the drift explanation is supported if failures correlate with low temperatures and large offsets, and that the attack explanation would show tags failing rather than timestamps. She uses only pseudonymised meter identifiers. The study plan is short but written before analysis, a habit from research methods that prevents fitting stories to data.

### 42.3 Findings and limits

The data show that most dawn failures have valid tags but timestamps outside tolerance, and occur after nights below freezing, with offsets growing in older meters. The drift explanation is supported. Aiyana recommends periodic time synchronisation from collectors, authenticated with the meter's key, instead of widening tolerance. She reports limits: one district, one winter, and correlation rather than controlled experiment. She shares the method with other utilities through the regulator's working group, without any meter identifiers. She plans a controlled follow-up with deliberately cooled test meters.

### Worked example

Aiyana's study links dawn failures to cold-induced clock drift with valid tags and recommends authenticated time synchronisation rather than wider tolerance.

> **Synthetic case.** The data and findings are invented.

### Errors and limits

Correlation does not prove cause; a controlled test would strengthen it. Sharing methods must not reveal infrastructure details.

### Exercises

- **EX124 — Research question.** State Aiyana's applied research question. *Rubric:* 3 = whether dawn failures come from cold-induced clock drift beyond tolerance rather than attacks or noise;; 2 = partial;; 1 = vague;; 0 = none.
- **EX125 — Distinguishing attack.** What evidence would indicate attack rather than drift? *Rubric:* 3 = tags failing rather than timestamps;; 2 = tag failures;; 1 = temperature;; 0 = none.
- **EX126 — Recommendation.** What did she recommend instead of widening tolerance? *Rubric:* 3 = periodic authenticated time synchronisation from collectors;; 2 = sync;; 1 = widen;; 0 = none.

### Synthesis

Applied research turns operational puzzles into small, pre-planned studies whose findings improve the system without weakening controls.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) apply course knowledge during a placement at a utility; (2) work within governance and change control; (3) reflect on professional practice.

### 43.1 The placement

Aiyana spends a term on placement in Ridgeway's security operations team, now as a supervised junior engineer. Her tasks include triaging verification alerts, assisting with a quarterly key rotation and updating runbooks. Marcus Webb supervises and signs off her work. She learns that most days are routine and that the value of good design shows in uneventful operations. She also learns how much context engineers need before acting on an alert, such as recent changes and known faulty meters. She keeps a log of each task and what she learned from it.

### 43.2 Change control

Every production change at Ridgeway goes through change control: a written request, risk assessment, approval and a rollback plan. Aiyana submits her first change, adjusting an alert threshold, and is asked to show evidence from the baseline data. She initially sees the process as slow, then sees its value when another team's unreviewed change to the gateway configuration briefly disables client certificate checks in staging, caught before reaching production. Cryptographic configurations are especially sensitive to small changes, so disciplined change control protects them.

### 43.3 Professional reflection

At the end of the placement Aiyana writes a reflection. She notes that her academic designs underestimated the time needed for coordination with vendors and field teams, that clear runbooks reduced stress during a minor incident, and that she was tempted once to bypass a slow approval to fix an alert, but didn't. She identifies skills to develop: negotiating with vendors about security requirements and explaining risk to managers. Reflection turns experience into deliberate learning. She shares the reflection with Marcus and agrees two goals for her first year.

### Worked example

Aiyana triages alerts, assists a rotation and updates runbooks under supervision, follows change control, and writes a reflection identifying vendor negotiation as a skill gap.

> **Synthetic case.** The placement and events are invented.

### Errors and limits

Placements can become passive observation; set concrete tasks and reviews. Change control can become bureaucratic if it ignores risk levels.

### Exercises

- **EX127 — Placement tasks.** Name two tasks Aiyana performed on placement. *Rubric:* 3 = two of alert triage, assisting rotation, updating runbooks;; 2 = one;; 1 = none;; 0 = none.
- **EX128 — Change-control lesson.** What event showed the value of change control? *Rubric:* 3 = an unreviewed gateway change disabled client certificate checks in staging, caught before production;; 2 = event;; 1 = none;; 0 = none.
- **EX129 — Skill gap.** Which skills did she identify to develop? *Rubric:* 3 = negotiating security requirements with vendors and explaining risk to managers;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Practice shows that disciplined change control, clear runbooks and reflection matter as much as design knowledge.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) scope a capstone project on the trust service; (2) plan milestones and evidence; (3) identify risks to the project itself.

### 44.1 Choosing the capstone

For her capstone Aiyana chooses to design and prototype the automated revocation pipeline: when a meter is reported stolen or a key is suspected exposed, revocation must reach every verifier within one minute and be auditable. The project combines earlier topics: key states, message queues, monitoring and runbooks. She writes a scope statement that includes design, a prototype in staging, tests and an operations handover, and excludes changes to meter firmware, which would need vendor involvement beyond the capstone's time.

### 44.2 Milestones and evidence

Aiyana plans milestones: requirements and threat model by week three, design review by week six, prototype by week ten, verification tests by week twelve and handover by week fifteen. For each milestone she defines evidence: documents, review minutes, test results and a demonstration recording. Her supervisor and Marcus agree the evidence will be assessed against the engineering programme's criteria. Defining evidence early prevents the common capstone failure of a working prototype with no documented reasoning. Missing evidence at a milestone counts as a missed milestone.

### 44.3 Project risks

Aiyana lists risks to the project: staging environment availability, dependency on the operations team's time, and the possibility that her design conflicts with a planned key service upgrade. Mitigations include booking staging slots early, agreeing a weekly hour with operations, and meeting the key service team in week two. She keeps a risk log updated weekly. Treating the capstone as an engineering project, with its own risks and controls, practises the habits she will need professionally. Risks that grow are escalated to her supervisor the same week.

### Worked example

Aiyana scopes a one-minute auditable revocation pipeline capstone, sets five evidence-backed milestones, and logs three project risks with mitigations.

> **Synthetic case.** The capstone plan is invented.

### Errors and limits

Capstones often over-scope; firm exclusions protect delivery. Evidence planned late is usually incomplete.

### Exercises

- **EX130 — Capstone goal.** What must the revocation pipeline achieve? *Rubric:* 3 = revocation reaches every verifier within one minute and is auditable;; 2 = one minute;; 1 = vague;; 0 = none.
- **EX131 — Exclusion.** What did Aiyana exclude from scope and why? *Rubric:* 3 = meter firmware changes, needing vendor involvement beyond the time available;; 2 = firmware;; 1 = nothing;; 0 = none.
- **EX132 — Project risk.** Name one project risk and its mitigation. *Rubric:* 3 = e.g. key service upgrade conflict mitigated by early meeting;; 2 = risk only;; 1 = none;; 0 = none.

### Synthesis

A well-scoped capstone with evidence-backed milestones and its own risk log practises professional engineering on a real security need.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to review findings; (3) distinguish blocking from advisory findings.

### 45.1 Preparing for review

Aiyana's revocation design goes to an independent review panel: a cryptographer from another utility, a reliability engineer and an auditor. She sends a package a week ahead with the requirements, threat model, architecture, interface contracts, test plan and open questions. She lists assumptions explicitly, such as that the message queue preserves order per meter. A good package lets reviewers spend their time on judgement rather than on reconstructing the design from scattered notes. She also includes a list of known weaknesses so reviewers start from honest ground.

### 45.2 Review findings

The panel raises five findings. Two are blocking: revocation messages are not authenticated, so an attacker on the internal network could forge revocations and cause denial of service, and there is no defined behaviour if a verifier misses messages while offline. Three are advisory: naming, dashboard layout and a suggestion to reuse an existing audit store. Aiyana appreciates the first finding particularly: she had protected readings carefully but treated internal control messages as trusted. Each finding is logged with its severity and the reviewer who raised it.

### 45.3 Responding

For the blocking findings, Aiyana signs revocation messages with a dedicated key held in the key service and verified by every subscriber, and adds a reconciliation step where verifiers fetch the full revocation list on reconnect and compare a hash of it with the published value. For advisory findings she accepts two and declines one with a reason. She re-presents the changed design to the panel, which closes the blocking findings. Independent review caught a flaw that would have been costly in production.

### Worked example

The panel finds unauthenticated revocation messages and missing offline behaviour; Aiyana adds signed revocations and reconnect reconciliation and closes both blocking findings.

> **Synthetic case.** The panel and findings are invented.

### Errors and limits

Review packages that hide assumptions get shallow reviews. Treating internal messages as trusted is a common design flaw.

### Exercises

- **EX133 — Review package.** List four items in Aiyana's review package. *Rubric:* 3 = four of requirements, threat model, architecture, contracts, test plan, open questions, assumptions;; 2 = three;; 1 = one;; 0 = none.
- **EX134 — Forged revocation.** Why were unauthenticated revocation messages a blocking finding? *Rubric:* 3 = attackers on internal network could forge revocations causing denial of service;; 2 = forgery;; 1 = minor;; 0 = none.
- **EX135 — Offline fix.** How does the revised design handle verifiers that were offline? *Rubric:* 3 = fetch full revocation list on reconnect and compare its hash with the published value;; 2 = fetch;; 1 = ignore;; 0 = none.

### Synthesis

Independent review with a complete package catches flaws designers miss, especially trust placed in internal messages.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) build and test the capstone prototype; (2) measure it against requirements; (3) hand it over to operations.

### 46.1 Building the prototype

Aiyana builds the revocation pipeline in staging. A revocation request from an authorised operator creates a signed message with the key identifier, reason, time and sequence number. The message queue delivers it to billing, collectors' configuration service and monitoring. Each subscriber verifies the signature with the vetted library, checks the sequence number, updates its key state cache and acknowledges. Unacknowledged deliveries trigger alerts. The prototype uses only existing, approved components, so it can move to production without new security approvals for unfamiliar technology.

### 46.2 Measuring results

Aiyana runs 1,000 test revocations. The median time to reach all verifiers is four seconds and the slowest is thirty-eight seconds, within the one-minute requirement. Forged revocations signed with a wrong key are rejected by all subscribers. A verifier taken offline for an hour reconciles correctly on reconnect. She also measures operator effort: issuing a revocation takes under a minute through the approved interface. She reports one gap: monitoring dashboards show revocations but not acknowledgements per subscriber, which she adds. All runs are scripted so others can repeat them.

### 46.3 Handover

Handover includes the design, decision records, runbooks for issuing and auditing revocations, test results and a training session for operators. Operations runs a revocation exercise themselves before accepting the system. Aiyana stays available for two weeks of support. She records known limitations, such as dependence on the message queue's availability, with a fallback runbook for manual revocation distribution. A capstone that ends with a working handover, not just a demonstration, shows professional completeness. Operations signs an acceptance note listing any open issues and their owners.

### Worked example

The prototype meets the one-minute target with a median of four seconds and maximum thirty-eight, rejects forgeries, reconciles offline verifiers and is handed over after an operations-run exercise.

> **Synthetic case.** Measurements are invented.

### Errors and limits

Staging performance may differ from production. Handover without operator practice leaves knowledge with the builder.

### Exercises

- **EX136 — Revocation message.** What fields does a revocation message contain? *Rubric:* 3 = key identifier, reason, time, sequence number, signed;; 2 = three;; 1 = one;; 0 = none.
- **EX137 — Timing results.** Report median and maximum revocation times. *Rubric:* 3 = four seconds median, thirty-eight seconds maximum;; 2 = one;; 1 = wrong;; 0 = none.
- **EX138 — Handover condition.** What did operations do before accepting the system? *Rubric:* 3 = ran a revocation exercise themselves;; 2 = exercise;; 1 = nothing;; 0 = none.

### Synthesis

A capstone proves itself through measured performance against requirements and a handover that leaves operations able to run it.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) plan a large-scale recovery exercise; (2) recover the firmware root from custodian shares; (3) learn from exercise findings.

### 47.1 Planning the trial

Ridgeway holds an annual failure and recovery trial, and Aiyana helps plan this year's scenario: the primary signing HSM is destroyed in a simulated fire, and a security patch must be signed and released within forty-eight hours. The trial uses the real backup procedures but a test root and test meters, so no production key is exposed. Objectives, success criteria, observers and a stop rule are agreed in advance. Planning ensures the exercise tests procedures rather than improvisation. A safety officer may halt the trial at any time if a step risks real systems.

### 47.2 Running the recovery

Three of five custodians are called; one is abroad and one is unreachable, but the three-of-five quorum from Chapter 32 allows recovery. They meet in the backup site, restore the test root into a spare HSM from encrypted shares, issue a new intermediate in a ceremony and sign the patch. Test meters accept it. Total time is thirty-one hours. Observers record each step. One delay arises because the spare HSM's firmware was older than required, needing an update during the trial.

### 47.3 Learning from the trial

The post-trial review lists findings without blame: the spare HSM was not kept on the same firmware as production; the custodian contact list had an outdated phone number; and the ceremony script lacked a step for recording the new intermediate in the inventory. Each finding gets an owner and deadline. Aiyana updates the ceremony script and adds spare HSM firmware checks to the monthly operations checklist. The trial's value lies in these findings, discovered in practice rather than during a real emergency.

### Worked example

The trial recovers a test root from three custodian shares, signs a patch in thirty-one hours, and yields three blameless findings with owners.

> **Synthetic case.** The scenario and timings are invented.

### Errors and limits

Exercises with unrealistic conditions give false confidence. Using production keys in trials risks real exposure.

### Exercises

- **EX139 — Test root.** Why does the trial use a test root and test meters? *Rubric:* 3 = to exercise real procedures without exposing production keys;; 2 = safety;; 1 = realism;; 0 = none.
- **EX140 — Quorum in practice.** How did the quorum design help during the trial? *Rubric:* 3 = only three of five custodians were available, enough for recovery;; 2 = quorum;; 1 = not;; 0 = none.
- **EX141 — Trial findings.** Name two findings from the post-trial review. *Rubric:* 3 = two of outdated spare HSM firmware, wrong phone number, missing inventory step;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

Realistic recovery trials with blameless review reveal the small operational gaps that would cripple a real emergency.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble an evidence dossier for regulators and assessors; (2) link evidence to requirements and risks; (3) protect sensitive evidence.

### 48.1 Purpose of the dossier

The regulator requires Ridgeway to demonstrate that its metering trust service is adequately secured. Aiyana assembles an evidence dossier: requirements, architecture, risk register, control map, test reports, independent testing summary, ceremony minutes, trial findings and residual-risk statements. The dossier is organised by requirement, so an assessor can follow any requirement to its design, tests and operational evidence. A dossier turns years of work into an auditable argument rather than a pile of documents. It also gives future engineers a single map of why the system looks the way it does.

### 48.2 Linking evidence

For each requirement the dossier includes a short claim, the evidence supporting it and any limitations. For example, the claim that readings cannot be forged without a meter key links to the HMAC design, laboratory negative tests, the independent test finding no forgery and monitoring data showing verification failures investigated. Where evidence is weaker, such as side-channel resistance tested on one hardware revision, the dossier says so. Aiyana uses SHA-256 digests to identify each evidence file, so assessors can confirm they examined the exact versions referenced.

### 48.3 Protecting sensitive evidence

Some evidence would help attackers, such as detailed penetration test reports or HSM configuration. Aiyana classifies each item: public summaries, regulator-only material and internal-only material available for on-site inspection. Key material never appears in any dossier. Ceremony minutes include key identifiers and fingerprints but not keys. She agrees handling rules with the regulator. Evidence that protects the public must not itself become a risk to the public. Access to regulator-only and internal material is logged, and copies are numbered so that any leak could be traced back to a specific recipient.

### Worked example

Aiyana's dossier organises evidence by requirement, links claims to tests and operations with digests, and classifies sensitive items with agreed handling.

> **Synthetic case.** The dossier is invented.

### Errors and limits

Dossiers that hide weak evidence lose credibility when assessors find gaps. Over-sharing detailed test reports increases risk.

### Exercises

- **EX142 — Dossier organisation.** How is the dossier organised and why? *Rubric:* 3 = by requirement, so assessors can trace each to design, tests and operations;; 2 = requirement;; 1 = date;; 0 = none.
- **EX143 — Weak evidence.** How does the dossier treat weaker evidence? *Rubric:* 3 = states its limits openly, e.g. side-channel tests on one revision;; 2 = honest;; 1 = hides;; 0 = none.
- **EX144 — Ceremony minutes.** What do ceremony minutes include and exclude? *Rubric:* 3 = key identifiers and fingerprints, never key material;; 2 = fingerprints;; 1 = keys;; 0 = none.

### Synthesis

An evidence dossier organised by requirement, honest about limits and careful with sensitive material makes security claims auditable.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis on the trust service; (2) present design reasoning and evidence; (3) state contributions and limitations.

### 49.1 Thesis structure

Aiyana's thesis presents the design and evaluation of the Ridgeway metering trust service, focusing on her revocation pipeline and the post-quantum migration plan. Chapters cover the problem and requirements, related standards, architecture and alternatives, implementation, verification and validation, operations, and conclusions. Each design decision cites its requirement and evidence. The thesis is not a diary of the project; it is an argument that the design meets its requirements under stated assumptions. She uses the evidence dossier as the backbone, so every claim in the thesis points to an existing artefact.

### 49.2 Evidence and reasoning

The thesis reports measured results: revocation reaching all verifiers in a median of four seconds; independent testing with no forged readings; firmware reach of 97 percent in the pilot; and recovery in thirty-one hours in the trial. It explains why alternatives were rejected, such as public-key readings exceeding the message budget. Aiyana includes the laboratory programs as appendices, all using only the standard library on synthetic data, and states clearly that production systems use vetted cryptographic libraries and HSMs. Every number cites the test or log that produced it.

### 49.3 Contributions and limits

She states contributions: a revocation pipeline design with authenticated messages and reconciliation, a measured approach to post-quantum migration for long-lived meters, and an operational metrics set tied to SP 800-57 lifecycle stages. Limits include a single utility, a pilot rather than full deployment and dependence on vendor implementations she could not inspect. She suggests future work on hybrid signature performance across meter generations. Clear limits make contributions more credible. Her supervisor reads the limits section first, as examiners often do, and asks her to make each limit specific about who might see different results.

### Worked example

Aiyana's thesis argues the trust service meets its requirements, reports measured results, explains rejected alternatives and states three contributions with limits.

> **Synthetic case.** Results are invented; SP 800-57 is real.

### Errors and limits

Theses that list activities instead of arguing claims are weak. Claiming more than the evidence supports invites rejection.

### Exercises

- **EX145 — Thesis nature.** What is the thesis, according to the chapter? *Rubric:* 3 = an argument that the design meets requirements under stated assumptions, not a diary;; 2 = argument;; 1 = diary;; 0 = none.
- **EX146 — Lab appendix statement.** What does the thesis say about the laboratory programs? *Rubric:* 3 = stdlib only on synthetic data; production uses vetted libraries and HSMs;; 2 = stdlib;; 1 = production code;; 0 = none.
- **EX147 — Thesis limits.** Name two limits Aiyana states. *Rubric:* 3 = two of single utility, pilot not full deployment, uninspected vendor implementations;; 2 = one;; 1 = none;; 0 = none.

### Synthesis

An engineering thesis is a reasoned, evidenced argument with clear contributions and honest limits.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend design decisions before an examining panel; (2) answer questions about security trade-offs; (3) reflect on the engineer's ongoing responsibility.

### 50.1 Preparing the defense

Aiyana prepares a twenty-minute presentation: the problem, key design choices, evidence and limits. She anticipates questions: why symmetric keys for readings, why three of five custodians, why hybrid post-quantum signatures, and what happens if the key service is compromised. For each she prepares a concise answer pointing to evidence in the thesis or dossier. Marcus and her supervisor run a mock defense, pressing her on cost assumptions she had not fully justified, which she strengthens. She rehearses answers aloud until each fits in under two minutes.

### 50.2 Answering trade-off questions

During the defense an examiner asks why Ridgeway did not use public-key signatures for readings to remove central key risk. Aiyana explains the 32-byte message budget and energy constraints, the mitigations for central risk (HSMs, per-meter derivation, monitoring and dual control) and the condition under which she would reverse the decision. Another examiner asks whether her lab code could be used in production; she answers firmly that it could not, because it exists to verify understanding against test vectors, while production relies on vetted libraries.

### 50.3 Ongoing responsibility

In closing, Aiyana reflects that the trust service will outlive her involvement. Algorithms will be deprecated, quantum computing may mature, staff will change and threats will evolve. Her responsibility as an engineer is to leave a system that others can understand, operate, test and change safely, with documentation, runbooks, metrics and an evidence trail. The panel passes her thesis, noting the clarity of its limits. She begins work at Ridgeway as a security engineer the following month. She schedules her own first review of the system for one year later.

### Worked example

Aiyana defends the symmetric reading design, the custodian quorum and hybrid migration, refuses to call lab code production-ready, and frames her responsibility as leaving a maintainable system.

> **Synthetic case.** The defense and outcome are invented.

### Errors and limits

Defending every decision as perfect undermines credibility; acknowledge trade-offs. Engineering responsibility continues after handover.

### Exercises

- **EX148 — Mock defense lesson.** What weakness did the mock defense expose? *Rubric:* 3 = cost assumptions not fully justified;; 2 = costs;; 1 = none;; 0 = none.
- **EX149 — Central risk mitigations.** Which mitigations did she cite for central key risk? *Rubric:* 3 = HSMs, per-meter derivation, monitoring, dual control;; 2 = three;; 1 = one;; 0 = none.
- **EX150 — Engineer's responsibility.** How does Aiyana describe her ongoing responsibility? *Rubric:* 3 = leave a system others can understand, operate, test and change safely with documentation and evidence;; 2 = partial;; 1 = none;; 0 = none.

### Synthesis

A defense shows mastery by explaining trade-offs honestly, and engineering responsibility continues through the system's whole life.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Aiyana Torres, Marcus Webb, Halden Institute of Engineering, Ridgeway Water Utility and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Each added bit doubles the key space, so the work multiplies rather than increases by a fixed step.

**EX002.** Roughly -2.94 for 56 bits (about a day) and 18.73 for 128 bits.

**EX003.** Expected 2^127 guesses is far beyond any foreseeable attacker, leaving margin for improvement, and AES in FIPS 197 starts at 128 bits.

**EX004.** Exactly when e and m share no common factor, that is gcd(e, m) = 1.

**EX005.** The inverse is 2753 and 65 encrypts to 2790, which decrypts back to 65.

**EX006.** Without the randomised padding required by RFC 8017 (OAEP or PSS), deterministic textbook RSA leaks structure and enables attacks.

**EX007.** Leakage of secret information through physical behaviour, such as timing, power or emissions, rather than through the intended outputs.

**EX008.** Its running time reveals how many leading bytes were correct, letting an attacker guess tags byte by byte.

**EX009.** Deterministic random bit generators that expand well-seeded entropy, preventing meters from booting into identical predictable keys.

**EX010.** The digest is 32 bytes and each byte is written as two hexadecimal characters.

**EX011.** The two systems encoded the same reading text with different encodings, so the hashed bytes differed.

**EX012.** Floating representations such as 18342.0 and 18342 are different byte strings and would never hash or verify identically.

**EX013.** With the decision she needs, approving a key budget, followed by the risk of altered readings in plain words.

**EX014.** It does not hide readings from eavesdroppers; confidentiality would need encryption.

**EX015.** A stolen key allows forging only that one meter's readings instead of every meter's.

**EX016.** (1 - p)^n is approximately e^(-np) for small p.

**EX017.** Subtracting two nearly equal floating numbers lost all precision; -math.expm1(-x) computes the tiny result accurately.

**EX018.** When failures are correlated, for example if many meters share the same weak random seed.

**EX019.** Around 2^(n/2) draws, the square root of the space.

**EX020.** About 25.3 percent; Aiyana recommends assigning identifiers sequentially from a registry.

**EX021.** What the attacker may do, how many operations are counted, and what event is defined as failure.

**EX022.** They make AES fast and execute in constant time, which avoids secret-dependent timing.

**EX023.** When memory access patterns depend on secrets, another program sharing the cache can measure timing differences and infer them.

**EX024.** The key never leaves the chip, so opening a meter and dumping its memory does not expose the key.

**EX025.** Callers cannot choose algorithms, handle keys or compare tags themselves, removing common mistakes.

**EX026.** Specific error reasons would help attackers probe the system, so details go only to a protected log.

**EX027.** Without negative tests, a verifier that accepts everything would still pass the test suite.

**EX028.** If a certificate expired, meters would stop reporting and the utility could miss leaks.

**EX029.** It went to Marcus and then the vendor through coordinated disclosure, stayed confidential until fixed and was never tried on deployed meters.

**EX030.** Closed, because keeping known firmware is safer than running unverified code.

**EX031.** The cellular carrier, or anyone with access to that network.

**EX032.** Ephemeral key exchange means stolen long-term keys cannot decrypt past recorded sessions.

**EX033.** TLS stops at the gateway, so end-to-end HMAC lets the database detect alterations by any intermediate system.

**EX034.** Crash dumps could write in-memory keys to disk where others could read them.

**EX035.** random is a predictable simulation generator whose state can be recovered; secrets draws from the OS cryptographic generator.

**EX036.** They cannot read raw keys, because only the isolated key service account can access them.

**EX037.** A one-way memory-hard hash, because passwords only need verifying, never decrypting.

**EX038.** Argon2id with a unique random salt per user, as defined in RFC 9106.

**EX039.** Rotating the master key only requires re-wrapping small data keys rather than re-encrypting the database.

**EX040.** "Every reading is authenticated with a per-meter key", with an acceptance test that rejects altered readings.

**EX041.** Never paste cryptographic code from forums; use a maintained library or take the gap to design review.

**EX042.** A test helper that turned off TLS certificate verification and was about to be reused in production.

**EX043.** Usage patterns show when occupants are away, which could help burglars.

**EX044.** Nation-state hardware attacks on the pilot; stating it explicitly keeps claims honest.

**EX045.** Each key is bound to a single meter identifier, so an authenticated meter can submit only its own readings.

**EX046.** For example generation, distribution, rotation and destruction.

**EX047.** They are sent encrypted under a transport key, never in plain form.

**EX048.** Revocation belonged to nobody, so compromised keys remained active for months.

**EX049.** Tag verification failure rate, days until certificate expiry and key ages.

**EX050.** Because renewal tooling can fail silently, and noticing no attempt prevents a later expiry.

**EX051.** Rapid flapping of alerts and repeated automated revocation for meters with intermittent faults.

**EX052.** A key trusted by assumption rather than proof, such as a root certificate or embedded firmware public key.

**EX053.** Meters accept only firmware with a valid chain and a higher version number than installed.

**EX054.** Only the short-lived derived keys cached for that region.

**EX055.** Readings are numerous and cheap symmetric tags suit them, while collectors authenticate over TLS where certificates let verifiers use public keys.

**EX056.** False, because changing the reading changes the required tag, which cannot be produced without the key.

**EX057.** Both the meter and the key service hold the key, so a tag cannot prove which of them created it.

**EX058.** Meter battery life, limited radio bandwidth and a fixed budget.

**EX059.** Meters get moved between addresses during repairs, so key bindings to identities must handle swaps.

**EX060.** Firmware updates should reach 99 percent of meters within thirty days of release.

**EX061.** Every reading carries an HMAC-SHA256 tag with a 256-bit per-meter key, and billing rejects readings whose tag fails.

**EX062.** ECDSA P-256 under FIPS 186-5, or Ed25519 under RFC 8032.

**EX063.** Independent forgery testing before go-live and witnessed key ceremonies with minutes.

**EX064.** The actual key bytes; only metadata about the key.

**EX065.** Three keys hidden in old scripts that were missing from any record.

**EX066.** It can still verify previously produced data but cannot create new tags or signatures.

**EX067.** Attackers could have malicious firmware signed with the genuine key, so meters would accept it.

**EX068.** An expired collector certificate and meter clock drift rejecting valid readings.

**EX069.** With an encrypted backup of the signing key held under split custody.

**EX070.** Extract condenses input keying material into a pseudorandom key using a salt; expand stretches it into output keys tied to an info string.

**EX071.** It printed that the output matched RFC 5869 test case A.1: True.

**EX072.** Purpose, meter identifier and key version; the version lets new keys be derived for rotation without a new master.

**EX073.** Forging a reading would require guessing a 128-bit value, and RFC 2104 permits truncation within such limits.

**EX074.** Each reading carries an increasing counter, and billing rejects counters not higher than the last accepted.

**EX075.** They added a key version to messages so a new meter's counter starts fresh with its new key.

**EX076.** Ed25519 signatures take 64 bytes, too large for the 32-byte per-message budget.

**EX077.** The regulator requires billing keys to stay under Ridgeway's control.

**EX078.** If radio frames grew enough to carry signatures, public-key readings would become feasible.

**EX079.** HSM non-exportability (preventive), verification-failure alerts (detective) and revocation (corrective).

**EX080.** To prove that the root key was generated and backed up without any single person controlling it.

**EX081.** Meter clock drift lacked detection, so a timestamp-skew monitor was added.

**EX082.** It verifies the manifest's signature chain, confirms the version is newer and checks the image digest against the manifest.

**EX083.** The check failed and the image was rejected.

**EX084.** Without a signature, an attacker could replace the image and the manifest together and pass the hash check.

**EX085.** The firmware signing key (880 days), webhook HMAC key (406) and backup wrapping key (968).

**EX086.** No, but longer use raises the amount of protected data and the harm if exposure has gone unnoticed.

**EX087.** The number of keys generated, which says nothing about safety.

**EX088.** Synthetic keys on an isolated network, never production keys.

**EX089.** Readings with a revoked key were accepted for up to an hour; the cache was cut to one minute and revocations are pushed.

**EX090.** Only that known defects are absent under the tested conditions, not that the system is free of defects.

**EX091.** Each collector proves its identity with a client certificate issued by Ridgeway's device authority.

**EX092.** On the collector itself, so the private key never has to be transmitted.

**EX093.** Any party holding a publicly issued certificate could then authenticate, so only Ridgeway's device authority should be trusted.

**EX094.** About 0.59, lower even than relying on one custodian.

**EX095.** Three of five, which gives about 0.99 availability while preventing any two people from recovering the key.

**EX096.** The HSM vendor's built-in key-splitting, because implementing secret sharing herself would be home-made cryptography.

**EX097.** It is quarantined and an alert is raised, keeping the evidence.

**EX098.** Revoke it with a root-signed statement, create a new intermediate in a ceremony, re-sign firmware and distribute the new trust.

**EX099.** So that losing or compromising the primary root does not strand the fleet.

**EX100.** The field handheld's request for a new meter key when replacing a meter.

**EX101.** So that only the target meter's secure element can unwrap it and the handheld never sees the key.

**EX102.** Billing never received revocation events; a shared message queue now delivers them to every verifier.

**EX103.** Meters remain in service around fifteen years, so firmware signed now must stay trustworthy until about 2041.

**EX104.** Only if both the classical ECDSA and the ML-DSA signatures verify.

**EX105.** Post-quantum verification requires a new bootloader, which must first be deployed using classical signatures.

**EX106.** About 1.2 million readings per day.

**EX107.** In database writes and key lookups; HMAC itself is cheap.

**EX108.** So collectors do not all renew at the same moment and overload the issuing service.

**EX109.** An operator unfamiliar with them carried them out, and confusing steps were rewritten.

**EX110.** New version keys are rolled out in waves while billing accepts both versions, and the old version is deactivated when every meter has moved.

**EX111.** It only ever held blobs encrypted for meters' secure elements, never meter keys themselves.

**EX112.** Verification confirms the system matches its specification; validation confirms it meets stakeholders' real needs.

**EX113.** A key from a prototype meter lacking a secure element, confirming the requirement for secure elements.

**EX114.** Only 97 percent updated within thirty days, short of 99 percent, because some meters in flooded pits were unreachable.

**EX115.** Algorithm identifiers in messages and manifests, and a configured list of accepted algorithms.

**EX116.** Stop issuing new keys with it, migrate existing uses, then drop verification support after a grace period.

**EX117.** Because many incidents start when engineers no longer know why a design was chosen and change it unsafely.

**EX118.** They hold only for the hardware revision tested, so new revisions must be retested.

**EX119.** The gateway correctly rejected the not-yet-valid certificate, but the collector's alert was unclear and was rewritten.

**EX120.** Extraction of one meter's key by a well-funded attacker, accepted because per-meter keys confine the damage to that meter.

**EX121.** All four readings and their counters, so deletion or reordering would be detected.

**EX122.** Its credentials sit in the key service and its issuance logs go to monitoring.

**EX123.** Sixty-four-bit forgery resistance falls below the threat model's target and radio headers dominate energy anyway.

**EX124.** Are dawn verification failures caused by meter clocks drifting past the timestamp tolerance after cold nights, not by attacks or radio noise?

**EX125.** Failures in the tag check itself rather than timestamps outside tolerance.

**EX126.** Regular time synchronisation from collectors, authenticated with each meter's key.

**EX127.** Triaging verification alerts and helping with a quarterly key rotation.

**EX128.** Another team's unreviewed change switched off client certificate checks in staging and was caught before production.

**EX129.** Negotiating security requirements with vendors and communicating risk to managers.

**EX130.** Revocations must reach all verifiers within one minute, with an audit trail.

**EX131.** Changes to meter firmware, which would require vendor work beyond the capstone schedule.

**EX132.** A conflict with the planned key service upgrade, mitigated by meeting that team in week two.

**EX133.** Requirements, threat model, architecture and test plan (plus contracts and open questions).

**EX134.** An internal attacker could forge revocations and knock legitimate meters offline.

**EX135.** On reconnecting, verifiers download the full revocation list and check its hash against the published value.

**EX136.** The key identifier, reason, timestamp and sequence number, all signed.

**EX137.** A median of four seconds and a maximum of thirty-eight seconds.

**EX138.** They performed their own revocation exercise.

**EX139.** So that real procedures are practised without risking production keys.

**EX140.** Two custodians were unavailable, but three of five were enough to recover.

**EX141.** The spare HSM's firmware was out of date and a custodian's phone number was wrong.

**EX142.** By requirement, letting an assessor trace each one through design, testing and operations.

**EX143.** It states the limitation openly, such as side-channel testing on only one hardware revision.

**EX144.** They include key identifiers and fingerprints but never key material.

**EX145.** An argument that the design satisfies its requirements under stated assumptions, not a project log.

**EX146.** They use only the standard library on synthetic data, while production relies on vetted libraries and HSMs.

**EX147.** One utility only and a pilot rather than full deployment.

**EX148.** Her cost assumptions had not been adequately justified.

**EX149.** Hardware security modules, per-meter key derivation, monitoring and dual control.

**EX150.** To leave a system that others can understand, run, test and change safely, supported by documentation, runbooks, metrics and evidence.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, keys and data in this book are synthetic unless a sentence cites a public source.

- Barker, E. (2020). *Recommendation for key management: Part 1 — General* (NIST SP 800-57 Part 1 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-57pt1r5>
- Barker, E., & Kelsey, J. (2015). *Recommendation for random number generation using deterministic random bit generators* (NIST SP 800-90A Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-90Ar1>
- Barker, E., & Roginsky, A. (2019). *Transitioning the use of cryptographic algorithms and key lengths* (NIST SP 800-131A Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-131Ar2>
- Barnes, R., Bhargavan, K., Lipp, B., & Wood, C. (2022). *Hybrid public key encryption* (RFC 9180). IETF. <https://www.rfc-editor.org/rfc/rfc9180>
- Barnes, R., Hoffman-Andrews, J., McCarney, D., & Kasten, J. (2019). *Automatic certificate management environment (ACME)* (RFC 8555). IETF. <https://www.rfc-editor.org/rfc/rfc8555>
- Biryukov, A., Dinu, D., Khovratovich, D., & Josefsson, S. (2021). *Argon2 memory-hard function for password hashing and proof-of-work applications* (RFC 9106). IETF. <https://www.rfc-editor.org/rfc/rfc9106>
- Boneh, D., & Shoup, V. (2023). *A graduate course in applied cryptography* (version 0.6, draft). <https://toc.cryptobook.us/>
- Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 public key infrastructure certificate and CRL profile* (RFC 5280). IETF. <https://www.rfc-editor.org/rfc/rfc5280>
- Dworkin, M. (2007). *Recommendation for block cipher modes of operation: Galois/Counter Mode (GCM) and GMAC* (NIST SP 800-38D). NIST. <https://doi.org/10.6028/NIST.SP.800-38D>
- Josefsson, S., & Liusvaara, I. (2017). *Edwards-curve digital signature algorithm (EdDSA)* (RFC 8032). IETF. <https://www.rfc-editor.org/rfc/rfc8032>
- Katz, J., & Lindell, Y. (2020). *Introduction to modern cryptography* (3rd ed.). CRC Press.
- Krawczyk, H., & Eronen, P. (2010). *HMAC-based extract-and-expand key derivation function (HKDF)* (RFC 5869). IETF. <https://www.rfc-editor.org/rfc/rfc5869>
- Krawczyk, H., Bellare, M., & Canetti, R. (1997). *HMAC: Keyed-hashing for message authentication* (RFC 2104). IETF. <https://www.rfc-editor.org/rfc/rfc2104>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Langley, A., Hamburg, M., & Turner, S. (2016). *Elliptic curves for security* (RFC 7748). IETF. <https://www.rfc-editor.org/rfc/rfc7748>
- Laurie, B., Langley, A., & Kasper, E. (2013). *Certificate transparency* (RFC 6962). IETF. <https://www.rfc-editor.org/rfc/rfc6962>
- Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). *Handbook of applied cryptography*. CRC Press. Chapters free online: <https://cacr.uwaterloo.ca/hac/>
- Moriarty, K., Kaliski, B., Jonsson, J., & Rusch, A. (2016). *PKCS #1: RSA cryptography specifications version 2.2* (RFC 8017). IETF. <https://www.rfc-editor.org/rfc/rfc8017>
- National Institute of Standards and Technology. (2001, updated 2023). *Advanced Encryption Standard (AES)* (FIPS 197). <https://doi.org/10.6028/NIST.FIPS.197-upd1>
- National Institute of Standards and Technology. (2008). *The keyed-hash message authentication code (HMAC)* (FIPS 198-1). <https://doi.org/10.6028/NIST.FIPS.198-1>
- National Institute of Standards and Technology. (2015). *Secure hash standard (SHS)* (FIPS 180-4). <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Institute of Standards and Technology. (2023). *Digital signature standard (DSS)* (FIPS 186-5). <https://doi.org/10.6028/NIST.FIPS.186-5>
- National Institute of Standards and Technology. (2024). *Module-lattice-based digital signature standard* (FIPS 204). <https://doi.org/10.6028/NIST.FIPS.204>
- National Institute of Standards and Technology. (2024). *Module-lattice-based key-encapsulation mechanism standard* (FIPS 203). <https://doi.org/10.6028/NIST.FIPS.203>
- National Institute of Standards and Technology. (2024). *Stateless hash-based digital signature standard* (FIPS 205). <https://doi.org/10.6028/NIST.FIPS.205>
- Nystrom, M. (2005). *Identifiers and test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512* (RFC 4231). IETF. <https://www.rfc-editor.org/rfc/rfc4231>
- Percival, C., & Josefsson, S. (2016). *The scrypt password-based key derivation function* (RFC 7914). IETF. <https://www.rfc-editor.org/rfc/rfc7914>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Shoup, V. (2004). *Sequences of games: A tool for taming complexity in security proofs* (Cryptology ePrint Archive, Paper 2004/332). <https://eprint.iacr.org/2004/332>
