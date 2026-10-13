# Cryptography and Trust Services: Bachelor's Course

- Language: English (`en`); course 100, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; six offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: bachelor's students learning cryptography from mathematical foundations to operating trust services in a real organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: labs illustrate concepts (XOR, classical ciphers, salted hashing, hash chains) on synthetic data; toy ciphers are shown only to explain why they fail. Production systems use vetted libraries; never roll your own cryptography. All people, organisations and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one student over four years as she helps a public library consortium protect patron data: mathematics, systems and programming foundations; security literacy, discrete structures, protocols, databases, ethics, privacy and evidence; then trust services in theory and practice, authenticated encryption, signatures, verification, failure analysis and operations; and finally research, a comparative project, a capstone certificate inventory, community workshops and a thesis. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Priya Raman** | Bachelor's student | Invented |
| **Dr. Tomás Echeverría** | Lecturer | Invented |
| **Grace Okafor** | Consortium IT lead | Invented |
| **Ashford University** | Fictional university | Invented |
| **Tidewell Public Library Consortium** | Fictional partner with twelve branches | Invented |

### Core sources

Katz and Lindell (3rd ed.); Menezes et al., [*Handbook of Applied Cryptography*](https://cacr.uwaterloo.ca/hac/); Boneh and Shoup, [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/); [FIPS 180-4](https://doi.org/10.6028/NIST.FIPS.180-4); [SP 800-38D](https://doi.org/10.6028/NIST.SP.800-38D); [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446); [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280); [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) reason precisely about definitions and claims in cryptography; (2) use the XOR operation and its algebraic properties; (3) prove why reusing a one-time pad key fails.

### 1.1 The case and precise claims

Priya Raman is a first-year bachelor's student at the fictional Ashford University. Over four years she will work with the fictional Tidewell Public Library Consortium, twelve branch libraries sharing a patron portal, an e-book service and staff systems, guided by lecturer Dr. Tomás Echeverría and the consortium's IT lead, Grace Okafor. Every patron, key and figure here is synthetic. Her first lesson is that cryptography is a mathematical discipline: a claim such as "this cipher is secure" means nothing until security is defined, the attacker is described and the claim is proved or reduced to a well-studied assumption, as Katz and Lindell insist.

### 1.2 XOR and its algebra

Exclusive or, written XOR, compares two bits and outputs 1 when they differ. It has properties Priya proves from its truth table: x XOR x = 0, x XOR 0 = x, and XOR is associative and commutative. These make XOR reversible: if c = p XOR k then c XOR k = p. The one-time pad encrypts by XORing a message with a truly random key of the same length used once, and Shannon proved it perfectly secret under those conditions. Proving small algebraic facts carefully is practice for reading the proofs in later courses.

### Lab — One-time pad reuse

```python
"""Why a one-time pad must never be reused: XOR of two ciphertexts cancels the key (toy data)."""
import secrets
def xor(a, b): return bytes(x ^ y for x, y in zip(a, b))

def main():
    p1, p2 = b"RENEW BOOK 0417", b"FINE PAID  0938"
    key = bytes.fromhex("8f1e2a77c03b5d9e4412ab6f0e7c31")  # fixed demo pad, used twice on purpose
    c1, c2 = xor(p1, key), xor(p2, key)
    print("c1 xor c2 == p1 xor p2:", xor(c1, c2) == xor(p1, p2))
    guess = xor(xor(c1, c2), b"RENEW BOOK 0417")
    print("knowing p1 reveals p2:", guess.decode())
    fresh = secrets.token_bytes(len(p1))
    print("fresh pad length matches message:", len(fresh) == len(p1))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_xor.py`. Verified output:

```text
c1 xor c2 == p1 xor p2: True
knowing p1 reveals p2: FINE PAID  0938
fresh pad length matches message: True
```

### 1.3 Why reuse fails

The lab encrypts two patron messages with the same pad on purpose. XORing the two ciphertexts cancels the key, since (p1 XOR k) XOR (p2 XOR k) = p1 XOR p2, which the lab confirms as True. If an attacker knows or guesses one message, such as a standard "RENEW BOOK" notice, the other appears in clear: FINE PAID 0938. The proof takes three lines, and the lesson lasts a career: a scheme that is perfect under its conditions can fail completely when a condition, here "use once", is violated. The fresh pad drawn from the secrets module shows how keys should be generated, though real systems use standard ciphers instead of pads.

### Worked example

Priya proves x XOR x = 0 from the truth table, derives c1 XOR c2 = p1 XOR p2, and uses the lab to recover a second message from a known first message when a pad is reused.

> **Synthetic case.** Tidewell, its patrons and messages are invented.

### Errors and limits

Perfect secrecy holds only for truly random, never-reused keys as long as the message; practical systems use AES-GCM or similar from vetted libraries, not pads. Toy demonstrations are not designs.

### Exercises

- **EX001 — Defining secure.** Why is "this cipher is secure" meaningless on its own? *Rubric:* 3 = security must be defined with an attacker model and proved or reduced to an assumption;; 2 = needs definition;; 1 = it is meaningful;; 0 = none.
- **EX002 — XOR identities.** State two XOR identities that make decryption work. *Rubric:* 3 = x XOR x = 0 and x XOR 0 = x (with associativity);; 2 = one;; 1 = wrong;; 0 = none.
- **EX003 — Pad reuse result.** What did the lab recover, and why? *Rubric:* 3 = FINE PAID 0938, because c1 XOR c2 = p1 XOR p2 and p1 was known;; 2 = message;; 1 = vague;; 0 = none.

### Synthesis

Cryptography begins with precise definitions and proofs; the one-time pad shows how a perfect scheme collapses when one condition is broken.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe where cryptography sits in a computing system; (2) explain data at rest, in transit and in use; (3) identify which component protects each.

### 2.1 Layers of a system

Priya maps Tidewell's systems in layers: hardware in branch servers and patron laptops, operating systems, applications such as the catalogue and patron portal, networks connecting branches, and cloud services hosting e-books. Cryptography appears at several layers: disk encryption in the operating system, TLS in network libraries, password hashing in the portal application and signatures on software updates. She learns that a protection at one layer does not cover the others; encrypting a disk does nothing for data travelling between branches, and TLS does nothing for a stolen laptop's disk.

### 2.2 Three states of data

Data exists in three states. At rest, it sits on disks and backups; full-disk encryption and database encryption protect it against theft of media. In transit, it moves across networks; TLS protects it against eavesdropping and tampering. In use, it is being processed in memory, where it is usually decrypted and protected mainly by access control and operating-system isolation. Priya classifies Tidewell's patron records in each state and notes that the consortium encrypts laptops and uses TLS for the portal, but backup tapes sent to an off-site store are not encrypted.

### 2.3 Matching protections

Priya builds a table matching each data flow to its protection and owner. Patron logins travel over TLS and are stored as salted password hashes; loan history sits in an encrypted database; backups travel by courier unencrypted. She recommends encrypting backups with keys held by the consortium, not by the courier company, and records that key loss would make backups unreadable, so the keys need their own protected backup. Grace Okafor accepts the recommendation and asks Priya to estimate the cost of the backup software change.

### Worked example

Priya's layer map and data-state table show unencrypted backup tapes as a gap, and she recommends consortium-held backup encryption with protected key backup.

> **Synthetic case.** Tidewell's systems are invented.

### Errors and limits

Encryption at rest does not protect data in use by a compromised application. Losing encryption keys destroys data as surely as losing the media.

### Exercises

- **EX004 — Layer limits.** Why does disk encryption not protect data moving between branches? *Rubric:* 3 = it protects data at rest only; transit needs TLS;; 2 = layers differ;; 1 = it does;; 0 = none.
- **EX005 — Data in use.** What mainly protects data in use? *Rubric:* 3 = access control and operating-system isolation, since data is decrypted in memory;; 2 = access control;; 1 = encryption;; 0 = none.
- **EX006 — Backup gap.** What gap did Priya find and what did she recommend? *Rubric:* 3 = unencrypted backup tapes; encrypt with consortium-held keys and back up keys;; 2 = gap;; 1 = vague;; 0 = none.

### Synthesis

Cryptography protects specific layers and data states; mapping them reveals gaps such as unencrypted backups.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) handle bytes, encodings and hexadecimal in Python; (2) compute SHA-256 digests with hashlib; (3) check results against published test vectors.

### 3.1 Bytes and encodings

Priya's first programs show that computers store text as bytes according to an encoding. The string "café" becomes five bytes in UTF-8 because é needs two. Cryptographic functions take bytes, so she always writes text.encode("utf-8") before hashing. Hexadecimal displays bytes readably, two characters per byte. She practises converting with bytes.hex() and bytes.fromhex(). Small mistakes here, such as hashing a string with a trailing newline read from a file, produce entirely different digests, which taught her to print lengths and hex forms when debugging.

### 3.2 Hashing with hashlib

Python's hashlib implements SHA-256 from FIPS 180-4. Priya computes the digest of the empty string and of "abc" and compares them with the examples published with the standard: the "abc" digest begins ba7816bf. Matching a published vector proves she is calling the function correctly. She observes the avalanche effect: changing "abc" to "abd" changes about half of the 256 output bits. She learns that hashes are public functions, so anyone can compute them; a hash proves integrity only when the expected digest comes from a trusted source.

### 3.3 A file-integrity tool

Priya writes a small program that computes the SHA-256 digest of every file in a folder and saves a list, then later recomputes and reports changes. She uses Tidewell's synthetic catalogue export files for testing. Large files are read in chunks and fed to the hash object's update method, so memory use stays small. She documents a limit: an attacker who can modify both files and the saved list can hide changes, so the list must be stored somewhere protected or signed. This anticipates digital signatures later in the course.

### Worked example

Priya confirms her SHA-256 calls against the FIPS 180-4 "abc" example, builds a chunked file-integrity checker, and records that the digest list itself needs protection.

> **Synthetic case.** The catalogue files are invented; FIPS 180-4 is real.

### Errors and limits

Hashes do not hide data and do not authenticate by themselves. Encoding mistakes are the most common cause of mismatched digests.

### Exercises

- **EX007 — UTF-8 length.** Why is "café" five bytes in UTF-8? *Rubric:* 3 = é takes two bytes;; 2 = encoding;; 1 = four;; 0 = none.
- **EX008 — Test vector check.** How did Priya confirm she used SHA-256 correctly? *Rubric:* 3 = matched the FIPS 180-4 "abc" example digest beginning ba7816bf;; 2 = matched vector;; 1 = guessed;; 0 = none.
- **EX009 — Integrity tool limit.** What limit does the integrity checker have? *Rubric:* 3 = attacker modifying files and the digest list hides changes; list must be protected or signed;; 2 = protect list;; 1 = vague;; 0 = none.

### Synthesis

Careful byte handling, verified hashing and awareness of what a digest proves are the programmer's first cryptographic skills.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write clear explanations of cryptographic ideas; (2) cite standards and textbooks correctly; (3) avoid overclaiming in security writing.

### 4.1 Explaining clearly

Priya's first essay explains to a general reader why passwords should not be stored in plain text. She uses a concrete example, a stolen database exposing every patron's password, then explains hashing with salts in plain words before introducing terms. Dr. Echeverría marks down a paragraph that used "hash", "salt" and "key derivation" without defining them. She learns to define each term once, use it consistently and prefer short sentences. Clear writing is not simplification; it is precision that readers can follow.

### 4.2 Citing correctly

For cryptographic claims Priya cites primary sources: FIPS 180-4 for SHA-256, RFC 9106 for Argon2, Katz and Lindell for definitions, and Menezes and colleagues' Handbook of Applied Cryptography for classical background. She cites the exact document and section where possible and checks that each link works. She avoids citing blog posts for facts that standards state, and never invents a reference or identifier. When a source is a draft, such as Boneh and Shoup's online textbook, she notes the version she read.

### 4.3 Avoiding overclaiming

Security writing often overclaims: "unbreakable", "completely secure" or "hackers cannot". Priya rewrites such phrases with precise claims: "Argon2id makes each password guess costly in time and memory, slowing offline guessing." She also states what the measure does not do: it does not protect weak passwords such as "library1" against determined guessing. Dr. Echeverría tells the class that careful limits make writing more persuasive to expert readers and protect authors when claims are tested. She keeps a list of banned phrases beside her desk as a reminder.

### Worked example

Priya's essay defines terms once, cites FIPS 180-4 and RFC 9106, and replaces "unbreakable" with a precise claim and stated limit.

> **Synthetic case.** The essay is invented; cited standards are real.

### Errors and limits

Citations to secondary sources can carry errors; check the primary document. Precise language still needs a correct technical basis.

### Exercises

- **EX010 — Defining terms.** What did Dr. Echeverría mark down, and why? *Rubric:* 3 = terms like hash and salt used without definition;; 2 = undefined jargon;; 1 = style;; 0 = none.
- **EX011 — Primary sources.** Which primary sources did Priya cite for SHA-256 and Argon2? *Rubric:* 3 = FIPS 180-4 and RFC 9106;; 2 = one;; 1 = blog;; 0 = none.
- **EX012 — Precise rewrite.** Rewrite "Argon2 makes passwords unbreakable" precisely. *Rubric:* 3 = Argon2id makes each guess costly in time and memory, slowing offline guessing; weak passwords remain at risk;; 2 = partial;; 1 = unchanged;; 0 = none.

### Synthesis

Good security writing defines terms, cites primary sources and states claims with their limits.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) recognise the goals cryptography serves; (2) distinguish encryption, hashing, MACs and signatures; (3) spot common misconceptions.

### 5.1 What cryptography is for

Priya lists the goals cryptography serves: confidentiality, keeping data secret; integrity, detecting changes; authentication, confirming who sent something; and non-repudiation, preventing a signer from denying a signature. She maps Tidewell examples: patron reading history needs confidentiality, catalogue exports need integrity, staff logins need authentication and signed contracts with e-book publishers benefit from non-repudiation. Each goal needs different tools, and confusing them is the root of many errors she will meet later. She pins the four goals above every later design discussion, so that each proposed tool must name the goal it serves.

### 5.2 Four tools

Encryption provides confidentiality with a key; AES in FIPS 197 is the standard symmetric cipher. Hash functions such as SHA-256 provide a fixed-size fingerprint without a key. Message authentication codes such as HMAC from RFC 2104 provide integrity and authentication between parties sharing a key. Digital signatures, such as ECDSA in FIPS 186-5 or Ed25519 in RFC 8032, provide integrity, authentication and non-repudiation using a private key to sign and a public key to verify. Priya draws a table of which tool meets which goal.

### 5.3 Common misconceptions

Priya collects misconceptions from staff interviews at Tidewell: "the website has a padlock, so our data is safe everywhere"; "we hash backups, so they are encrypted"; "a longer password is always a stronger password"; and "encryption means nobody can change the data". She corrects each: TLS protects only the connection; hashing is not encryption; length helps only if the password is not predictable; and unauthenticated encryption may allow undetected tampering, which is why authenticated encryption such as AES-GCM is preferred.

### Worked example

Priya maps four goals to Tidewell examples, builds a tool-goal table, and corrects four staff misconceptions.

> **Synthetic case.** The staff quotes are invented.

### Errors and limits

Simplified tables omit nuances such as authenticated encryption combining goals. Non-repudiation also depends on key protection and legal context.

### Exercises

- **EX013 — Goal mapping.** Which goal do signed publisher contracts serve? *Rubric:* 3 = non-repudiation (plus integrity and authentication);; 2 = integrity;; 1 = confidentiality;; 0 = none.
- **EX014 — MAC versus signature.** How does a MAC differ from a signature? *Rubric:* 3 = MAC uses a shared key, no non-repudiation; signature uses private/public keys and supports non-repudiation;; 2 = partial;; 1 = same;; 0 = none.
- **EX015 — Padlock misconception.** Correct "the padlock means our data is safe everywhere". *Rubric:* 3 = TLS protects only the connection, not data stored on servers;; 2 = partial;; 1 = agree;; 0 = none.

### Synthesis

Knowing what each cryptographic tool achieves, and what it does not, is the foundation of security literacy.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) use modular arithmetic and groups; (2) explain the discrete logarithm problem; (3) relate it to Diffie-Hellman key agreement.

### 6.1 Modular arithmetic and groups

Priya studies integers modulo a prime p. Multiplication modulo p, excluding zero, forms a group: it is closed, associative, has an identity and every element has an inverse. Some elements, called generators, produce every non-zero element when raised to successive powers. For p = 23 and generator 5, the powers of 5 modulo 23 cycle through all 22 non-zero values. These structures, covered in chapter 2 of the Handbook of Applied Cryptography, underlie many public-key systems and give precise meaning to operations that otherwise look like arbitrary arithmetic.

### 6.2 The discrete logarithm

Computing 5^x mod 23 is easy for any x, using fast exponentiation. Going backwards, finding x from the result, is the discrete logarithm problem. For tiny primes Priya can search all values, but for primes of thousands of bits no efficient classical algorithm is known. This asymmetry, easy forward and hard backward, is what public-key cryptography needs. Priya notes the word "known": security rests on the belief that the problem is hard, and Shor's algorithm would solve it on a large quantum computer, which motivates post-quantum standards such as FIPS 203.

### 6.3 Diffie-Hellman by hand

Priya works a toy Diffie-Hellman exchange: Alice picks secret a = 6 and sends 5^6 mod 23 = 8; Bob picks b = 15 and sends 5^15 mod 23 = 19. Alice computes 19^6 mod 23 = 2 and Bob computes 8^15 mod 23 = 2, a shared secret neither sent. An eavesdropper sees 8 and 19 but must solve a discrete logarithm. She emphasises that real systems use large groups or elliptic curves such as X25519 from RFC 7748, authenticate the exchange to stop active attackers, and run inside TLS 1.3 rather than as hand-written code. Priya repeats the calculation with a classmate to confirm both sides really reach the same value.

### Worked example

Priya verifies that 5 generates the group modulo 23, computes a toy Diffie-Hellman shared secret of 2, and explains why real exchanges use X25519 inside TLS with authentication.

> **Synthetic case.** Toy numbers only; RFC 7748 and FIPS 203 are real.

### Errors and limits

Unauthenticated Diffie-Hellman is open to man-in-the-middle attacks. Toy groups are trivially breakable.

### Exercises

- **EX016 — Group properties.** List the four group properties. *Rubric:* 3 = closure, associativity, identity, inverses;; 2 = three;; 1 = one;; 0 = none.
- **EX017 — Toy shared secret.** What shared secret did the toy exchange produce, and from which public values? *Rubric:* 3 = 2, from public values 8 and 19;; 2 = secret only;; 1 = wrong;; 0 = none.
- **EX018 — Quantum threat.** Why does Shor's algorithm matter here? *Rubric:* 3 = it would solve discrete logarithms on a large quantum computer, motivating FIPS 203;; 2 = quantum;; 1 = vague;; 0 = none.

### Synthesis

Groups and the discrete logarithm problem explain key agreement; real systems use standard curves inside authenticated protocols.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain the TLS 1.3 handshake at a high level; (2) describe certificate validation by browsers; (3) identify protocol-level risks such as downgrade and misconfiguration.

### 7.1 The TLS 1.3 handshake

When a patron opens Tidewell's portal, the browser and server run a TLS 1.3 handshake from RFC 8446. The client sends supported algorithms and a key share; the server replies with its key share, and both derive keys using HKDF from RFC 5869. The server sends its certificate and signs the handshake transcript to prove it holds the private key, then both confirm the handshake with message authentication codes. All later data is encrypted with an authenticated cipher such as AES-GCM. Priya captures the handshake in a lab using a test server and identifies each message.

### 7.2 Certificate validation

The browser checks that the server's certificate chains to a root it trusts, that the name matches portal.tidewell.example, that it is within its validity dates and that it has not been revoked. RFC 5280 defines the certificate fields and path validation. If any check fails, the browser shows a warning. Priya explains to library staff why clicking through such warnings is dangerous: the warning may be the only sign that someone on the café Wi-Fi is intercepting the connection with a forged certificate.

### 7.3 Protocol risks

Older TLS versions allowed attackers to push connections down to weaker algorithms. TLS 1.3 removes legacy options and protects against downgrade by signing the whole handshake. Most practical problems now come from configuration: servers still offering TLS 1.0, expired certificates or applications that disable verification. Priya scans Tidewell's public services with permission and finds the staff wiki still accepts TLS 1.0. She reports it to Grace, who schedules a configuration change, and she records the scan's scope and authorisation in her notes. She retests after the change.

### Worked example

Priya identifies each TLS 1.3 handshake message, explains certificate checks to staff, and reports a TLS 1.0 setting found in an authorised scan.

> **Synthetic case.** Tidewell's hosts are invented; RFC 8446, RFC 5869 and RFC 5280 are real.

### Errors and limits

Scanning systems without permission is unethical and may be illegal. A valid certificate shows who runs a server, not that the server is safe.

### Exercises

- **EX019 — Transcript signature.** Why does the server sign the handshake transcript? *Rubric:* 3 = to prove it holds the certificate's private key and protect against tampering/downgrade;; 2 = prove key;; 1 = encrypt;; 0 = none.
- **EX020 — Browser checks.** List three checks the browser makes on a certificate. *Rubric:* 3 = three of chain to trusted root, name match, validity dates, revocation;; 2 = two;; 1 = one;; 0 = none.
- **EX021 — Scan finding.** What did Priya's authorised scan find? *Rubric:* 3 = staff wiki accepting TLS 1.0;; 2 = old TLS;; 1 = vague;; 0 = none.

### Synthesis

TLS 1.3 secures connections when certificates validate and configurations stay current; most failures are now operational.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) use high-level cryptographic APIs safely; (2) structure code to avoid misuse; (3) write negative tests.

### 8.1 High-level APIs

Priya learns that cryptographic libraries offer low-level primitives and high-level recipes. Low-level APIs require choosing modes, nonces and padding, where mistakes are easy. High-level APIs, such as an authenticated-encryption function that generates nonces and returns a single token, make safe use the default. For Tidewell's export tool, she uses a maintained library's authenticated-encryption recipe rather than assembling AES and a mode herself. The course rule is explicit: students learn how primitives work, but production code uses vetted high-level APIs. Teammates agree to follow it.

### 8.2 Structuring for safety

Priya isolates cryptography in one module with a small interface: protect(data) and unprotect(token). Keys are loaded from the consortium's secret store, never from source code. Errors in unprotect raise a single generic exception, so callers cannot learn why a token failed. She writes type hints marking secret values and avoids logging them. Code review focuses on this module, which is small enough to read carefully. The structure means future changes of algorithm affect one file rather than the whole application.

### 8.3 Negative tests

Priya writes tests that should fail: tampered tokens, truncated tokens, tokens protected with a different key and empty input. Each must be rejected. She also tests that two protections of the same data produce different tokens, confirming that nonces are fresh. A teammate's earlier version passed all positive tests while returning data even for tampered tokens, because it skipped tag verification. Negative tests caught it. She adds them to continuous integration so they run on every change. Each test has a one-line comment explaining its purpose.

### Worked example

Priya uses a high-level authenticated-encryption recipe in a small protect/unprotect module, loads keys from a secret store and catches a skipped tag check with negative tests.

> **Synthetic case.** The export tool is invented.

### Errors and limits

High-level APIs still need correct key management. Tests prove only what they check.

### Exercises

- **EX022 — High-level advantage.** Why prefer high-level cryptographic APIs? *Rubric:* 3 = safe defaults handle nonces, modes and padding, reducing misuse;; 2 = safer;; 1 = faster;; 0 = none.
- **EX023 — Generic exception.** Why does unprotect raise one generic exception? *Rubric:* 3 = so callers or attackers cannot learn why a token failed;; 2 = hide reason;; 1 = simpler;; 0 = none.
- **EX024 — Fresh-nonce test.** What does protecting the same data twice test? *Rubric:* 3 = tokens differ, confirming fresh nonces;; 2 = nonces;; 1 = vague;; 0 = none.

### Synthesis

Safe cryptographic code relies on high-level APIs, a small isolated module and negative tests that prove rejection.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) store passwords with salted, slow hashing; (2) explain why salts and work factors matter; (3) choose field-level protections in a database.

### 9.1 Password storage

Tidewell's old portal stored passwords with plain SHA-256, which Priya explains is unsafe: SHA-256 is fast, so an attacker with a stolen table can test billions of guesses per second, and identical passwords produce identical hashes. A proper scheme adds a unique random salt per user and uses a deliberately slow function. RFC 9106 specifies Argon2id, the preferred choice; PBKDF2, available in Python's hashlib, is an older fallback that needs a high iteration count. The lab demonstrates salting with PBKDF2 because it is in the standard library.

### Lab — Salted password hashing

```python
"""Salted password hashing with hashlib.pbkdf2_hmac on synthetic passwords (prefer Argon2id, RFC 9106)."""
import hashlib, hmac
def h(pw, salt, n=600_000):
    return hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, n).hex()

def main():
    s1, s2 = bytes.fromhex("a1" * 16), bytes.fromhex("b2" * 16)  # fixed demo salts for reproducible output
    a, b = h("correct horse 42", s1), h("correct horse 42", s2)
    print("same password, different salts differ:", a != b)
    print("stored:", a[:24], "...")
    print("login with right password:", hmac.compare_digest(a, h("correct horse 42", s1)))
    print("login with wrong password:", hmac.compare_digest(a, h("correct horse 43", s1)))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_pbkdf2.py`. Verified output:

```text
same password, different salts differ: True
stored: c96866459ba12d6a7bc6285d ...
login with right password: True
login with wrong password: False
```

### 9.2 Reading the run

The same password with two different salts produces different stored values, so an attacker cannot see which patrons share a password or use precomputed tables. Logging in with the right password recomputes the same value and compare_digest returns True; a one-character change returns False. The fixed demonstration salts exist only to make the output repeatable; real salts come from secrets.token_bytes. The 600,000 iterations slow each guess. Priya recommends migrating to Argon2id, rehashing each password at the patron's next successful login.

### 9.3 Field-level choices

Beyond passwords, Priya classifies database fields: names and addresses are encrypted at the field level with keys from the consortium's key service; loan history older than ninety days is deleted, following the privacy principle of keeping only what is needed; and patron card numbers are tokenised for reporting systems. She records that deleting old data is often the strongest protection, since data that does not exist cannot leak. Grace agrees and schedules the retention change after board approval. The policy is published for patrons.

### Worked example

Priya replaces plain SHA-256 with salted slow hashing, plans migration to Argon2id at next login, encrypts personal fields and deletes loan history after ninety days.

> **Synthetic case.** Tidewell's database is invented; RFC 9106 is real.

### Errors and limits

Slow hashing does not save very weak passwords. Encryption keys stored beside the database offer little protection.

### Exercises

- **EX025 — Why SHA-256 fails.** Why is plain SHA-256 unsafe for passwords? *Rubric:* 3 = fast, enabling billions of guesses, and identical passwords give identical hashes;; 2 = fast;; 1 = it is fine;; 0 = none.
- **EX026 — Salt effect.** What did the lab show about salts? *Rubric:* 3 = same password with different salts gives different stored values;; 2 = differ;; 1 = same;; 0 = none.
- **EX027 — Strongest protection.** What does Priya call often the strongest protection? *Rubric:* 3 = deleting data that is not needed;; 2 = deletion;; 1 = encryption;; 0 = none.

### Synthesis

Salted, slow password hashing, field encryption and data minimisation protect patron data in databases.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) apply ethical rules to cryptographic testing; (2) obtain and document authorisation; (3) handle discovered weaknesses responsibly.

### 10.1 Authorisation first

Priya learns that testing a system's cryptography, for example scanning TLS settings or attempting to crack password hashes, requires written authorisation from its owner. Before her Chapter 7 scan, Grace signed a scope listing hosts, dates and allowed tools. Testing outside scope, even with good intentions, can break laws and trust. Dr. Echeverría tells the class that the same technical act can be legitimate research or a crime depending on authorisation, which is why professionals document it every time. Priya keeps a copy with her notes.

### 10.2 Handling sensitive material

During a class exercise on password strength, Priya's group receives a synthetic password-hash file created by the lecturer. They are reminded never to use real leaked password databases, which contain real people's secrets even if publicly available. Results are discussed only in aggregate. Priya learns to treat keys, hashes and personal data as hazardous materials: minimise copies, store them encrypted, delete them when done and record who had access. Group members sign a short handling agreement at the start of the exercise, and the lecturer deletes the file at the end of term.

### 10.3 Responsible disclosure

Later, while using a public e-book app outside her coursework, Priya notices that it sends login details over plain HTTP. She does not test further. She reports it to the vendor's security contact with a short description and a ninety-day disclosure window, following the coordinated disclosure practice her course teaches, and informs Dr. Echeverría. The vendor fixes it within a month and thanks her. She notes that exploiting the flaw to "prove" it would have been unethical and unnecessary.

### Worked example

Priya documents a signed scan scope, uses only synthetic hash files, and reports an HTTP login flaw through coordinated disclosure without further testing.

> **Synthetic case.** The vendor and events are invented.

### Errors and limits

Public availability of leaked data does not make its use ethical. Disclosure without giving the vendor time can harm users.

### Exercises

- **EX028 — Authorisation content.** What did Grace's signed scope list? *Rubric:* 3 = hosts, dates and allowed tools;; 2 = two;; 1 = vague;; 0 = none.
- **EX029 — Leaked databases.** Why must students not use real leaked password databases? *Rubric:* 3 = they contain real people's secrets even if public;; 2 = privacy;; 1 = allowed;; 0 = none.
- **EX030 — Disclosure steps.** How did Priya handle the HTTP login flaw? *Rubric:* 3 = stopped testing, reported to vendor security contact with ninety-day window, informed lecturer;; 2 = reported;; 1 = exploited;; 0 = none.

### Synthesis

Authorised scope, careful handling of secrets and coordinated disclosure make cryptographic testing ethical.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain how operating systems store and protect keys; (2) use the system's secure random generator; (3) configure full-disk encryption sensibly.

### 11.1 Keys in the operating system

Operating systems provide key stores: protected areas where applications keep private keys and certificates, often backed by hardware such as a trusted platform module. Priya examines how Tidewell's staff laptops store the certificates used to connect to the staff wiki. The private key is marked non-exportable, so applications can use it to sign but cannot copy it out. She learns that this design limits damage from malware: an attacker may misuse the key while on the machine but cannot take it elsewhere, and removing the malware ends the misuse.

### 11.2 Secure randomness

The operating system collects unpredictable events and offers a cryptographically secure random generator. Python's secrets module uses it, while the random module does not and must never be used for keys, tokens or salts. Priya reviews a library volunteer's script that generated temporary portal passwords with random.choice and replaces it with secrets.choice. She explains that random's outputs can be predicted after observing enough of them, which would let someone guess other patrons' temporary passwords. NIST SP 800-90A describes the generator designs operating systems build on.

### 11.3 Full-disk encryption

Tidewell's laptops use full-disk encryption, which protects data if a laptop is lost while powered off. Priya checks the configuration: recovery keys are stored in the consortium's management system, not on sticky notes; laptops require a PIN at start-up in addition to the hardware module; and sleep mode is replaced by hibernation, since memory contents, including disk keys, persist during sleep. She documents that full-disk encryption does not protect a laptop that is stolen while unlocked, so screen locks remain essential.

### Worked example

Priya confirms non-exportable laptop keys, replaces random.choice with secrets.choice for temporary passwords, and tightens full-disk encryption with central recovery keys and start-up PINs.

> **Synthetic case.** Tidewell's laptops are invented; SP 800-90A is real.

### Errors and limits

Non-exportable keys can still be misused while malware runs. Full-disk encryption offers nothing once the system is unlocked.

### Exercises

- **EX031 — Non-exportable benefit.** What does a non-exportable key prevent? *Rubric:* 3 = copying the key off the machine, limiting malware damage to local misuse;; 2 = copying;; 1 = all misuse;; 0 = none.
- **EX032 — Temporary passwords.** Why replace random.choice with secrets.choice? *Rubric:* 3 = random is predictable; secrets uses the OS secure generator;; 2 = predictable;; 1 = speed;; 0 = none.
- **EX033 — Sleep versus hibernate.** Why prefer hibernation to sleep on encrypted laptops? *Rubric:* 3 = memory, including disk keys, stays powered during sleep;; 2 = memory keys;; 1 = battery;; 0 = none.

### Synthesis

Operating systems protect keys with non-exportable stores, secure randomness and full-disk encryption when configured carefully.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) measure password strength in bits; (2) compare policies by guessing space; (3) recognise why human choices reduce real strength.

### 12.1 Guessing space in bits

Strength against guessing is measured by the number of equally likely possibilities, expressed in bits as the base-2 logarithm. A secret chosen uniformly from N possibilities has log2(N) bits. Each extra bit doubles the attacker's work. Priya computes this for password policies Tidewell is considering. The calculation assumes that every possibility is equally likely, which holds for machine-generated secrets but rarely for human choices. She keeps that assumption visible in every table she produces. She also explains bits to staff using coin tosses.

### Lab — Password policy bits

```python
"""Guessing space for password policies, in bits (synthetic policies, uniform choice assumed)."""
import math
POLICIES = [("8 lowercase letters", 26, 8), ("8 mixed + digits", 62, 8),
            ("4 words from 7776-word list", 7776, 4), ("6 words from 7776-word list", 7776, 6)]

def main():
    for name, alpha, n in POLICIES:
        print(f"{name:<30} {n * math.log2(alpha):5.1f} bits")
    print("human-chosen passwords fall far below these uniform figures")

if __name__ == "__main__":
    main()
```

Run with `python3 lab_entropy.py`. Verified output:

```text
8 lowercase letters             37.6 bits
8 mixed + digits                47.6 bits
4 words from 7776-word list     51.7 bits
6 words from 7776-word list     77.5 bits
human-chosen passwords fall far below these uniform figures
```

### 12.2 Reading the table

Eight random lowercase letters give 37.6 bits; eight random characters from letters and digits give 47.6. Four words chosen randomly from a 7,776-word list give 51.7 bits, and six words give 77.5. A randomly generated passphrase therefore beats a complex-looking eight-character password and is easier to remember. Priya stresses the word "randomly": a phrase chosen by a person, such as a favourite book title, has far fewer effective bits because attackers try common phrases first. The lab's last line states this limit. Grace asks for the table in the staff newsletter.

### 12.3 Human choices and policy

Real password studies show that people choose predictable patterns: capitalised first letters, years and exclamation marks. Composition rules often make passwords harder to remember without making them much harder to guess. Priya recommends that Tidewell allow long passphrases, check new passwords against lists of commonly used and breached passwords, rate-limit login attempts and offer a passphrase generator. She frames the recommendation as reducing guessability rather than satisfying rules, and notes that slow password hashing from Chapter 9 adds further protection. Grace takes the plan to the board.

### Worked example

Priya shows that six random words give 77.5 bits against 47.6 for eight mixed characters, and recommends long passphrases, breached-password checks and rate limiting.

> **Synthetic case.** The policies are invented; the calculations are standard.

### Errors and limits

Bit calculations apply only to uniformly random choices. Rate limiting protects online guessing, not offline attacks on stolen hashes.

### Exercises

- **EX034 — Bits formula.** How many bits does a uniformly chosen secret from N possibilities have? *Rubric:* 3 = log2(N);; 2 = logarithm;; 1 = N;; 0 = none.
- **EX035 — Passphrase result.** Compare four random words and eight mixed characters from the lab. *Rubric:* 3 = 51.7 bits versus 47.6 bits;; 2 = numbers;; 1 = reversed;; 0 = none.
- **EX036 — Human phrases.** Why does a person's chosen phrase have fewer effective bits? *Rubric:* 3 = attackers try common phrases first; choices are not uniform;; 2 = predictable;; 1 = same;; 0 = none.

### Synthesis

Measuring guessing space in bits shows why random passphrases outperform complex short passwords, provided choices are truly random.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) explain how cryptography supports authentication; (2) compare passwords, one-time codes and security keys; (3) design access for staff and patrons.

### 13.1 Authentication factors

Authentication proves identity using something you know, have or are. Passwords are knowledge; phones generating one-time codes and hardware security keys are possession. Priya studies how one-time codes work: the phone and server share a secret and compute short codes from it and the current time using HMAC, so a stolen password alone is not enough. Hardware security keys go further, using public-key signatures bound to the website's name, which stops phishing sites from replaying responses. Priya demonstrates both factors in a staff workshop.

### 13.2 Comparing methods

Priya compares methods for Tidewell staff. Passwords alone are vulnerable to phishing and reuse. Time-based codes stop many attacks but can be phished in real time by a fake site that relays codes. Security keys resist phishing because the key signs a challenge that includes the real site's origin, and a fake site's origin produces a useless signature. She recommends security keys for administrators and staff with access to patron data, and one-time codes as a fallback, noting costs and the need for spare keys.

### 13.3 Access design

For patrons, Priya recommends passwords or passphrases with optional one-time codes, since requiring hardware keys would exclude many users. For staff she designs role-based access: branch staff see their branch's patrons; administrators use separate accounts with security keys; and service accounts use certificates rather than shared passwords. She documents that authentication proves who someone is but authorisation decides what they may do, and that both must be reviewed when staff change roles or leave. Access reviews are scheduled every six months with branch managers.

### Worked example

Priya recommends security keys for administrators and data-handling staff, optional one-time codes for patrons, and role-based access with certificate-based service accounts.

> **Synthetic case.** Tidewell's roles are invented.

### Errors and limits

Strong authentication cannot fix excessive permissions. Recovery processes are often the weakest link.

### Exercises

- **EX037 — One-time codes.** How are time-based one-time codes computed? *Rubric:* 3 = HMAC over a shared secret and the current time;; 2 = HMAC;; 1 = random;; 0 = none.
- **EX038 — Phishing resistance.** Why do security keys resist phishing? *Rubric:* 3 = they sign a challenge bound to the real site's origin, useless for fake sites;; 2 = origin binding;; 1 = they don't;; 0 = none.
- **EX039 — Patron accessibility.** Why not require hardware keys for patrons? *Rubric:* 3 = it would exclude many users;; 2 = exclusion;; 1 = cost only;; 0 = none.

### Synthesis

Cryptography strengthens authentication, from HMAC-based codes to origin-bound security keys, but access design must balance security and inclusion.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) apply privacy principles to library data; (2) use pseudonymisation and its limits; (3) decide when encryption supports privacy.

### 14.1 Library privacy

Libraries have a long tradition of protecting what patrons read. Priya studies Tidewell's privacy policy and applicable data-protection law, identifying principles: collect only needed data, use it only for stated purposes, keep it no longer than necessary and protect it appropriately. Reading history is especially sensitive because it can reveal health, religion or politics. Cryptography supports these principles but cannot replace them; encrypting data that should not have been collected still leaves a risk. She lists which principles each Tidewell system currently meets or misses.

### 14.2 Pseudonymisation

For a study of branch usage, Grace asks for loan data without identities. Priya replaces card numbers with keyed pseudonyms computed with HMAC, using a key held by the consortium. Unkeyed hashing would fail, because card numbers follow a known format and could be hashed exhaustively. She notes that pseudonymised data is still personal data under many laws, because the key holder can re-identify it, and that rare combinations, such as one patron borrowing unusual books at a small branch, can identify people even without card numbers.

### 14.3 When encryption helps

Priya maps where encryption supports privacy: TLS keeps reading choices private on the network, database encryption protects against stolen backups, and end-to-end encryption would protect messages between patrons and librarians. Encryption does not help when the consortium itself misuses data or keeps it too long, which is why retention limits and access logs matter. She recommends deleting loan histories after return unless patrons opt in to keep them, which removes risk more effectively than any cipher. Grace takes the deletion proposal to the board for approval.

### Worked example

Priya pseudonymises loan data with HMAC under a consortium key, flags re-identification risks, and recommends deleting histories after return by default.

> **Synthetic case.** Tidewell's data and study are invented.

### Errors and limits

Pseudonymised data can often be re-identified. Encryption does not prevent misuse by authorised holders.

### Exercises

- **EX040 — Sensitive reading.** Why is reading history especially sensitive? *Rubric:* 3 = it can reveal health, religion or politics;; 2 = personal;; 1 = not sensitive;; 0 = none.
- **EX041 — Unkeyed hashing.** Why does unkeyed hashing of card numbers fail? *Rubric:* 3 = known format allows exhaustive hashing and matching;; 2 = guessable;; 1 = it works;; 0 = none.
- **EX042 — Default deletion.** What default does Priya recommend for loan histories? *Rubric:* 3 = delete after return unless patrons opt in;; 2 = delete;; 1 = keep;; 0 = none.

### Synthesis

Privacy depends on minimisation and purpose limits; cryptography such as keyed pseudonyms and encryption supports, but cannot replace, those principles.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) make logs tamper-evident with hash chains; (2) measure security controls with clear definitions; (3) interpret evidence honestly.

### 15.1 Why logs need protection

When a patron complains that someone accessed their record, Tidewell checks the access log. But an insider who misused data could also edit the log. Priya learns that evidence must be tamper-evident: changes must be detectable. A hash chain does this by including each entry's hash in the next, so editing any entry changes every later hash. Publishing or separately storing the latest hash, called the head, lets an auditor detect edits. Certificate Transparency logs, defined in RFC 6962, use a related structure, a Merkle tree, at internet scale.

### Lab — Hash-chained audit log

```python
"""Tamper-evident audit log: each entry's hash includes the previous hash (SHA-256)."""
import hashlib
def chain(entries):
    prev, out = "0" * 64, []
    for e in entries:
        prev = hashlib.sha256((prev + e).encode()).hexdigest(); out.append(prev)
    return out

def main():
    log = ["2026-05-01 admin login", "2026-05-01 patron export", "2026-05-02 key rotated"]
    good = chain(log)
    print("head:", good[-1][:16])
    log[1] = "2026-05-01 report viewed"
    bad = chain(log)
    print("head after editing entry 2:", bad[-1][:16])
    print("first differing entry:", next(i + 1 for i, (x, y) in enumerate(zip(good, bad)) if x != y))

if __name__ == "__main__":
    main()
```

Run with `python3 lab_chain.py`. Verified output:

```text
head: 4492b592d8b729f0
head after editing entry 2: c36641715cd10666
first differing entry: 2
```

### 15.2 Reading the chain

The three-entry log has a head beginning 4492b592. When the second entry is edited from "patron export" to "report viewed", the head becomes c3664171 and the first differing hash is at entry 2, showing exactly where tampering began. Priya notes the limit: if an insider can rewrite the whole chain and the stored head, nothing is detected. The head must therefore be stored where the insider cannot change it, for instance sent daily to a separate auditor's system or signed by a different team.

### 15.3 Measuring controls

Priya defines measures for Tidewell's controls: percentage of staff accounts using security keys, number of days certificates are renewed before expiry, and share of access-log entries reviewed. Each measure has a precise definition and data source. She reports baselines honestly: only 40 percent of staff use security keys so far, and log reviews happen monthly rather than weekly. She resists presenting only favourable numbers, because management decisions depend on an accurate picture. She shows each measure as a trend over months, so management can see whether controls are improving or slipping.

### Worked example

Priya builds a hash-chained log, shows an edit changes the head from 4492b592 to c3664171 and locates it at entry 2, and reports control baselines including the 40 percent security-key adoption.

> **Synthetic case.** Log entries and baselines are invented; RFC 6962 is real.

### Errors and limits

Hash chains detect tampering only if the head is protected separately. Measures without definitions produce inconsistent numbers.

### Exercises

- **EX043 — Chain property.** Why does editing one entry change every later hash? *Rubric:* 3 = each entry's hash includes the previous hash;; 2 = chaining;; 1 = it doesn't;; 0 = none.
- **EX044 — Lab heads.** Report the head before and after the edit and where the difference starts. *Rubric:* 3 = 4492b592 then c3664171, differing from entry 2;; 2 = heads;; 1 = wrong;; 0 = none.
- **EX045 — Protecting the head.** Where must the head be stored and why? *Rubric:* 3 = somewhere the insider cannot change, e.g. a separate auditor's system or signed by another team;; 2 = separate;; 1 = same server;; 0 = none.

### Synthesis

Tamper-evident logs and honestly reported measures turn security claims into evidence others can check.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) place cryptographic controls in an overall architecture; (2) identify trust boundaries; (3) apply defence in depth to library systems.

### 16.1 Trust boundaries

Priya draws Tidewell's architecture with trust boundaries: lines where data passes between areas with different levels of trust, such as the internet and the portal, the portal and the patron database, and the consortium and the e-book provider. Cryptographic controls cluster at boundaries: TLS where the internet meets the portal, mutual authentication where the portal calls the database, and signed messages where the consortium exchanges loan data with the provider. Drawing boundaries first shows where cryptography is needed and where it would only add complexity.

### 16.2 Defence in depth

Priya layers controls so one failure does not expose patrons. The portal uses TLS and security headers; the application authenticates users and checks permissions; the database encrypts sensitive fields and accepts connections only from the portal with certificates; backups are encrypted; and logs are hash-chained. If an attacker exploited a bug in the portal, they would still face database permissions and field encryption. She documents which threats each layer addresses and avoids layers that duplicate each other without adding protection.

### 16.3 Keys in the architecture

Priya adds key management to the diagram, which earlier drafts left out. A managed key service holds database and backup keys; the portal's TLS private key lives on the web servers with restricted permissions; and staff security keys hold their own private keys. She marks the key service as a high-value component requiring separate administration and monitoring. Grace notes that previous architecture documents never showed keys, which made it impossible to plan rotation or assess who could decrypt what. The revised diagram is versioned.

### Worked example

Priya's diagram marks three trust boundaries, five layers of defence and the location of every key, highlighting the key service as a high-value component.

> **Synthetic case.** The architecture is invented.

### Errors and limits

Layers that share a weakness, such as one admin account controlling all, do not add depth. Diagrams must be updated as systems change.

### Exercises

- **EX046 — Trust boundary.** Name two trust boundaries in Tidewell's architecture. *Rubric:* 3 = two of internet-portal, portal-database, consortium-provider;; 2 = one;; 1 = vague;; 0 = none.
- **EX047 — Portal bug.** What would an attacker still face after exploiting a portal bug? *Rubric:* 3 = database permissions and field encryption;; 2 = one layer;; 1 = vague;; 0 = none.
- **EX048 — Missing keys.** What did earlier architecture documents omit and why did it matter? *Rubric:* 3 = key locations; rotation and access to decryption could not be assessed;; 2 = keys;; 1 = vague;; 0 = none.

### Synthesis

Architectures should show trust boundaries, layered controls and every key, so cryptography is placed where it protects most.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain Kerckhoffs's principle; (2) show why classical ciphers fail; (3) define modern security goals such as indistinguishability.

### 17.1 Kerckhoffs's principle

A cipher should remain secure even if everything about it except the key is public. This principle, stated by Auguste Kerckhoffs in the nineteenth century, guides modern cryptography: AES is fully published in FIPS 197, and its security rests on the secrecy of keys. Priya learns why secret algorithms are a poor bet: they get reverse-engineered, they receive little public scrutiny and changing them is expensive. Public, well-analysed standards concentrate expert attention where weaknesses can be found and fixed early. Tidewell's suppliers are asked to confirm they use published algorithms.

### Lab — Breaking a Caesar cipher

```python
"""Break a toy Caesar cipher by frequency analysis to show why classical ciphers fail."""
from collections import Counter
TEXT = "THE LIBRARY OPENS AT NINE AND THE READING ROOM CLOSES AT EIGHT EVERY EVENING"

def shift(s, k):
    return "".join(chr((ord(c) - 65 + k) % 26 + 65) if c.isalpha() else c for c in s)

def main():
    ct = shift(TEXT, 11)
    top = Counter(c for c in ct if c.isalpha()).most_common(1)[0][0]
    k = (ord(top) - ord("E")) % 26
    print("ciphertext:", ct[:30], "...")
    print("most common letter:", top, "-> guessed shift", k)
    print("recovered:", shift(ct, -k)[:30], "...")
    print("keys to try by brute force:", 25)

if __name__ == "__main__":
    main()
```

Run with `python3 lab_caesar.py`. Verified output:

```text
ciphertext: ESP WTMCLCJ ZAPYD LE YTYP LYO  ...
most common letter: P -> guessed shift 11
recovered: THE LIBRARY OPENS AT NINE AND  ...
keys to try by brute force: 25
```

### 17.2 Why classical ciphers fail

The lab encrypts a sentence about library hours with a Caesar shift of 11. The most common ciphertext letter is P, and assuming it stands for E, the most common English letter, gives the shift 11 and recovers the text. Even without frequency analysis, only 25 shifts exist, so brute force is instant. Priya extends the lesson: substitution ciphers preserve letter patterns, and any cipher that leaks structure about the plaintext can be attacked statistically. The Handbook of Applied Cryptography, chapter 7, surveys such classical systems and why they were abandoned.

### 17.3 Modern goals

Modern cryptography defines security precisely. Katz and Lindell describe indistinguishability: an attacker who chooses two messages and sees the encryption of one should not be able to tell which, with probability meaningfully better than a coin toss. This rules out leaking patterns, lengths aside. A deterministic scheme, where the same message always encrypts the same way, fails this definition because repeated messages are visible. That is why modern encryption uses random or unique nonces and why authenticated encryption also guarantees integrity.

### Worked example

Priya breaks a shift-11 Caesar cipher by frequency analysis, explains Kerckhoffs's principle using FIPS 197, and shows why deterministic encryption fails indistinguishability.

> **Synthetic case.** The message is invented; FIPS 197 and the Handbook are real.

### Errors and limits

Indistinguishability does not hide message length. Classical ciphers are for history and teaching, never protection.

### Exercises

- **EX049 — Kerckhoffs.** State Kerckhoffs's principle. *Rubric:* 3 = a cipher should be secure even if everything except the key is public;; 2 = key secrecy;; 1 = secret algorithm;; 0 = none.
- **EX050 — Caesar break.** How did the lab find the shift? *Rubric:* 3 = most common letter P assumed to be E, giving shift 11;; 2 = frequency;; 1 = brute force only;; 0 = none.
- **EX051 — Deterministic failure.** Why does deterministic encryption fail indistinguishability? *Rubric:* 3 = repeated messages encrypt identically, revealing repetition;; 2 = patterns;; 1 = it passes;; 0 = none.

### Synthesis

Public algorithms, precise definitions and randomised encryption replaced classical ciphers whose patterns gave them away.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) formulate a researchable question about cryptographic practice; (2) search literature and standards systematically; (3) plan a small study ethically.

### 18.1 A researchable question

Priya wants to study how library staff respond to TLS certificate warnings. She refines a vague interest into a researchable question: "When shown a simulated certificate warning on a staff training site, what share of Tidewell staff proceed, and does a one-page explanation reduce that share?" The question names a population, a measurable behaviour and an intervention. Dr. Echeverría points out that a simulation must be clearly separate from real systems, so staff are never put at risk. She refines the wording twice.

### 18.2 Searching sources

Priya searches academic databases for studies of security warnings, records search terms and dates, and reads RFC 8446 and RFC 5280 to describe what warnings indicate technically. She keeps a table of sources with each study's population, method and findings, noting which used laboratory participants and which observed real browsing. She distinguishes peer-reviewed studies from vendor reports and records every source's full citation, verifying links before adding them to her bibliography. She also asks the university librarian to check her search strategy, which leads her to two relevant studies she had missed.

### 18.3 Ethical planning

The study involves people, so Priya applies to the university's ethics committee. Her plan explains that participation is voluntary, responses are anonymous, the warning appears only on a training site with no real data, and participants are debriefed afterwards with the explanation of why warnings matter. Grace confirms the consortium's support in writing. The committee asks her to ensure managers never see individual results, which she adds. Ethical review shapes design, not just paperwork. She also prepares a plain-language information sheet for participants.

### Worked example

Priya writes a specific question about certificate warnings, keeps a sourced literature table, and obtains ethics approval for an anonymous training-site simulation with debriefing.

> **Synthetic case.** The study is invented; RFC 8446 and RFC 5280 are real.

### Errors and limits

Simulations may not reflect real behaviour under pressure. Studies with staff must protect them from employment consequences.

### Exercises

- **EX052 — Question parts.** What three elements make the question researchable? *Rubric:* 3 = population, measurable behaviour, intervention;; 2 = two;; 1 = one;; 0 = none.
- **EX053 — Source table.** What does Priya record for each study? *Rubric:* 3 = population, method, findings (and lab versus real browsing);; 2 = two;; 1 = citation only;; 0 = none.
- **EX054 — Committee request.** What did the ethics committee ask Priya to add? *Rubric:* 3 = ensure managers never see individual results;; 2 = anonymity;; 1 = vague;; 0 = none.

### Synthesis

Researchable questions, systematic sources and ethical design turn curiosity about cryptographic practice into a credible study.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Cryptography and trust services: scope and theory

### Learning outcomes

You will (1) define the scope of trust services; (2) explain public-key infrastructure as a theory of delegated trust; (3) describe what certificates and timestamps assert.

### 19.1 What trust services are

Trust services help people and systems rely on electronic information: certificate authorities issue certificates; timestamping services prove when data existed; signature services help create and validate digital signatures; and key management services protect keys. Priya maps which Tidewell uses: a public authority for its websites, an internal authority for staff devices, and a signing service for contracts with publishers. Each service makes an assertion others rely on, so its own security and procedures become part of everyone's security. Priya records each assertion in a table.

### 19.2 Delegated trust

Public-key infrastructure delegates trust. A browser cannot know every website's key, so it trusts a small set of root authorities, which vouch for intermediates, which vouch for websites. RFC 5280 defines how certificates chain and how clients validate them. Priya explains the theory's weak point: any trusted root can issue a certificate for any name, so one compromised or careless authority can undermine everyone. Certificate Transparency, specified in RFC 6962, responds by making issuance public so misissued certificates can be detected. She shows staff how to view CT entries.

### 19.3 What assertions mean

A certificate asserts that a public key belongs to a name for a period; it does not assert that the named party is honest. A timestamp asserts that data existed at a time, not that the data is true. A signature asserts that the holder of a private key approved specific bytes, not that the holder understood them. Priya writes these distinctions for Tidewell's contract process, where staff sometimes assumed a signed PDF meant the publisher had agreed to terms that were actually in an unsigned attachment.

### Worked example

Priya maps Tidewell's trust services, explains delegated trust and Certificate Transparency, and clarifies that a signature covers only the signed bytes in a contract case.

> **Synthetic case.** Tidewell's services and contract are invented; RFC 5280 and RFC 6962 are real.

### Errors and limits

Trusting many roots widens risk. Signatures prove approval of bytes, not intent or understanding.

### Exercises

- **EX055 — Four services.** Name four kinds of trust service. *Rubric:* 3 = certificate authorities, timestamping, signature services, key management;; 2 = three;; 1 = one;; 0 = none.
- **EX056 — Root weakness.** What is the main weakness of delegated trust? *Rubric:* 3 = any trusted root can issue for any name, so one bad authority undermines all;; 2 = any root;; 1 = vague;; 0 = none.
- **EX057 — Contract misunderstanding.** What did staff misunderstand about the signed PDF? *Rubric:* 3 = assumed signature covered terms in an unsigned attachment;; 2 = coverage;; 1 = vague;; 0 = none.

### Synthesis

Trust services make specific assertions; understanding exactly what each asserts prevents misplaced reliance.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Cryptography and trust services: foundational cases

### Learning outcomes

You will (1) analyse documented classes of trust failure; (2) extract lessons for an organisation like Tidewell; (3) separate cryptographic from procedural causes.

### 20.1 Classes of failure

Priya studies classes of failure documented in public sources and textbooks. Certificate authorities have issued certificates to the wrong parties because of weak validation; organisations have suffered outages when certificates expired; software has accepted certificates without checking names; and private keys have leaked through misconfigured servers. She classifies causes as cryptographic, such as weak algorithms, or procedural, such as poor validation or monitoring. Most cases she reads are procedural; the mathematics held while people and processes failed. She keeps a summary table of cases and causes.

### 20.2 Lessons for Tidewell

For each class Priya writes a lesson: monitor Certificate Transparency logs for certificates issued for Tidewell names, which would reveal misissuance; automate renewals and alert before expiry; test applications against certificates with wrong names; and keep private keys on servers with restricted access and inventory them. Grace adopts the expiry and monitoring lessons immediately, since an expired certificate took the catalogue offline for half a day the previous year. Priya also adds a quarterly check that scans for certificates with wrong names, using only the consortium's own authorised hosts.

### 20.3 Separating causes

Priya practises separating causes using Tidewell's catalogue outage. The certificate expired because renewal was manual and the person responsible had left; no alert existed; and the replacement took hours because nobody knew which server held the key. None of these causes involved cryptographic weakness. She writes a short analysis with timeline, causes and actions: automated renewal, an owner for each certificate and an inventory of key locations. This becomes the template for later failure analyses. The template is stored in the shared drive.

### Worked example

Priya classifies trust failures as mostly procedural and analyses Tidewell's catalogue outage into three non-cryptographic causes with matching actions.

> **Synthetic case.** The outage is invented; failure classes are drawn from public literature.

### Errors and limits

Blaming individuals hides process causes. Rare cryptographic failures still occur, so algorithm choices matter too.

### Exercises

- **EX058 — Dominant cause.** What kind of cause dominated the cases Priya read? *Rubric:* 3 = procedural, not cryptographic;; 2 = procedural;; 1 = cryptographic;; 0 = none.
- **EX059 — CT monitoring lesson.** What does monitoring Certificate Transparency logs reveal? *Rubric:* 3 = certificates issued for Tidewell names, exposing misissuance;; 2 = misissuance;; 1 = expiry;; 0 = none.
- **EX060 — Outage causes.** Name the three causes of the catalogue outage. *Rubric:* 3 = manual renewal by departed person, no alert, unknown key location;; 2 = two;; 1 = one;; 0 = none.

### Synthesis

Most trust failures are procedural; analysing them without blame yields practical lessons for any organisation.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Cryptography and trust services: system models

### Learning outcomes

You will (1) model Tidewell's trust services as components and flows; (2) identify which component asserts what; (3) find single points of trust.

### 21.1 Components and flows

Priya models the consortium's trust services as a system. Components include the public certificate authority used for websites, the internal authority for staff devices, the key service, the contract-signing service and the e-book provider's licence server, which checks signed loan tokens. Flows connect them: certificate requests, signed tokens, encrypted backups and revocation information. She draws the model with arrows labelled by what each flow carries and how it is protected, building on the architecture from Chapter 16. Grace reviews the diagram with her team for accuracy.

### 21.2 Who asserts what

For each component Priya records its assertion and who relies on it. The public authority asserts that Tidewell controls its domain names, relied on by patrons' browsers. The internal authority asserts that a device belongs to staff, relied on by the wiki. The licence server relies on Tidewell's signed loan tokens asserting that a patron may borrow a title for fourteen days. Writing assertions explicitly shows which failures would mislead whom, and therefore which components need the strongest controls. She shares the table with Grace.

### 21.3 Single points of trust

The model reveals single points of trust: the internal authority's signing key, if stolen, would let an attacker create staff device certificates; and one administrator account controls both the key service and its audit logs. Priya recommends moving the internal authority's root offline with a separate issuing key, and separating key-service administration from log administration. Each recommendation reduces the damage one compromise can cause. Grace adds both to the next year's plan with estimated costs. Both items gain owners and target dates.

### Worked example

Priya's system model labels each flow, lists each component's assertion and finds two single points of trust with recommendations.

> **Synthetic case.** The model is invented.

### Errors and limits

Models simplify; verify them against real configurations. Single points of trust may hide in people as well as systems.

### Exercises

- **EX061 — Licence assertion.** What do Tidewell's signed loan tokens assert to the licence server? *Rubric:* 3 = a patron may borrow a title for fourteen days;; 2 = loan permission;; 1 = identity;; 0 = none.
- **EX062 — Internal authority risk.** What could an attacker do with the internal authority's signing key? *Rubric:* 3 = create staff device certificates;; 2 = impersonate devices;; 1 = vague;; 0 = none.
- **EX063 — Admin separation.** Which separation did Priya recommend for administration? *Rubric:* 3 = separate key-service administration from audit-log administration;; 2 = separation;; 1 = merge;; 0 = none.

### Synthesis

Modelling who asserts what, and who relies on it, exposes single points of trust before attackers find them.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Cryptography and trust services: data and dependencies

### Learning outcomes

You will (1) inventory cryptographic assets and dependencies; (2) track libraries and algorithms in use; (3) plan for supplier changes.

### 22.1 Cryptographic inventory

Priya builds an inventory of Tidewell's cryptographic assets: certificates with expiry dates and owners; keys with purposes, algorithms and locations; and protocols in use on each service. SP 800-57 Part 1 stresses knowing what keys an organisation has. She discovers two forgotten certificates on old servers and a backup key stored in a shared folder. The inventory turns invisible risks into a list with owners and becomes the basis for every later change, including algorithm migration. The inventory is reviewed monthly by Grace's team for accuracy.

### 22.2 Library and algorithm dependencies

Tidewell's systems depend on cryptographic libraries in operating systems, web servers and applications. Priya lists each library and version and records which algorithms each system uses. She finds that the contract-signing service uses RSA with 2048-bit keys and SHA-256, acceptable today, and that an old reporting tool uses SHA-1 for file checks. She notes NIST's guidance in SP 800-131A on transitioning away from SHA-1 and schedules the reporting tool's replacement. She stores the dependency list in the shared repository so that any team can see which systems a library update would affect.

### 22.3 Supplier changes

Several services come from suppliers, including the e-book provider and the portal host. Priya asks each for its cryptographic practices: TLS versions, key storage and plans for post-quantum migration. One supplier cannot answer about post-quantum plans; she records this as a risk rather than a failure, since migration is still at an early stage. She recommends adding cryptographic requirements to future contracts, such as supporting current TLS versions and notifying Tidewell of key compromises. Grace includes the requirement template in the next tender.

### Worked example

Priya's inventory finds two forgotten certificates and a backup key in a shared folder, flags an SHA-1 tool for replacement, and adds cryptographic requirements to supplier contracts.

> **Synthetic case.** Inventory findings are invented; SP 800-57 and SP 800-131A are real.

### Errors and limits

Inventories decay without regular discovery scans. Supplier answers need evidence, not only assurances.

### Exercises

- **EX064 — Inventory findings.** What did the inventory uncover? *Rubric:* 3 = two forgotten certificates and a backup key in a shared folder;; 2 = one;; 1 = vague;; 0 = none.
- **EX065 — SHA-1 tool.** What did Priya decide about the SHA-1 reporting tool and which guidance supports it? *Rubric:* 3 = schedule replacement; SP 800-131A transition guidance;; 2 = replace;; 1 = keep;; 0 = none.
- **EX066 — Supplier risk.** How did she treat a supplier unable to answer about post-quantum plans? *Rubric:* 3 = recorded as a risk, not a failure, given early migration stage;; 2 = risk;; 1 = dropped supplier;; 0 = none.

### Synthesis

A cryptographic inventory of keys, certificates, libraries and suppliers is the foundation for every safe change.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Cryptography and trust services: methods I

### Learning outcomes

You will (1) apply authenticated encryption correctly; (2) understand nonces and their rules; (3) choose AES-GCM parameters from standards.

### 23.1 Authenticated encryption

Authenticated encryption combines confidentiality and integrity: decryption fails if the ciphertext was changed. AES-GCM, specified in SP 800-38D using AES from FIPS 197, is the most widely used scheme. Priya learns its interface: a key, a unique nonce, the plaintext and optional associated data, which is authenticated but not encrypted, such as a record identifier. Including the identifier as associated data prevents an attacker from swapping encrypted records between patrons without detection. Priya demonstrates on synthetic records that changing the identifier makes decryption fail, which convinces sceptical colleagues.

### 23.2 Nonce rules

GCM requires that a nonce never repeat under the same key. A repeat lets an attacker learn the XOR of two plaintexts, as with the reused pad in Chapter 1, and forge messages. SP 800-38D allows either counters, which must never reset, or random 96-bit nonces, limited to about 2^32 encryptions per key. Priya recommends random nonces generated by the library together with key rotation well before that limit. She checks that Tidewell's export tool never constructs nonces itself. She documents the rule in the code review checklist.

### 23.3 Choosing parameters

Priya writes a parameter note for Tidewell: AES-256-GCM, 96-bit nonces generated by the library, 128-bit authentication tags, associated data containing the record type and identifier, and keys rotated yearly or after a set number of encryptions. Each choice cites SP 800-38D or SP 800-57. She notes that the library's high-level recipe already chooses most of these, which is the point: engineers should verify parameters, not invent them. Grace files the note with the system documentation, and Priya schedules a yearly review to confirm that the parameters still match current guidance.

### Worked example

Priya specifies AES-256-GCM with library-generated 96-bit nonces, full tags and associated data binding records to patrons, citing SP 800-38D.

> **Synthetic case.** The parameter note is invented; SP 800-38D and FIPS 197 are real.

### Errors and limits

Nonce reuse breaks GCM badly. Associated data must be identical at encryption and decryption.

### Exercises

- **EX067 — Associated data.** Why include the record identifier as associated data? *Rubric:* 3 = to stop encrypted records being swapped between patrons undetected;; 2 = binding;; 1 = encrypts it;; 0 = none.
- **EX068 — Random nonce limit.** What limit applies to random 96-bit GCM nonces? *Rubric:* 3 = about 2^32 encryptions per key;; 2 = limit;; 1 = vague;; 0 = none.
- **EX069 — Parameter source.** Why does Priya call verifying parameters the point? *Rubric:* 3 = engineers should verify, not invent, parameters; recipes choose most;; 2 = verify;; 1 = invent;; 0 = none.

### Synthesis

Authenticated encryption with unique nonces and bound associated data protects records when parameters follow standards.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Cryptography and trust services: controls

### Learning outcomes

You will (1) select controls for key management; (2) apply separation of duties and dual control; (3) document controls for audit.

### 24.1 Selecting controls

Priya selects key-management controls for Tidewell based on SP 800-57: keys generated in the key service, never by individuals; access to keys limited by role; rotation on schedule; revocation procedures; and secure destruction when keys retire. For each control she lists its purpose, owner and evidence, such as logs or tickets. She prioritises controls for the highest-value keys, the internal authority and backup keys, rather than applying every control everywhere. She explains that spreading effort evenly would leave the most valuable keys no better protected than trivial ones.

### 24.2 Separation and dual control

Separation of duties means no single person can complete a sensitive action alone; dual control means two people must act together. Priya applies both: restoring backup keys requires two administrators; the person who approves certificate requests cannot also issue them; and audit logs are reviewed by someone outside the IT team. These controls protect against both mistakes and insiders, and they protect honest staff by making it clear they could not have acted alone. She documents each control in the access policy.

### 24.3 Documenting for audit

Priya writes a control register: control, risk addressed, owner, frequency and evidence location. When the consortium's auditors visit, they sample the register: they ask for evidence of last quarter's backup-key test and the approval records for three certificates. Two items are missing because evidence was kept in personal email. Priya moves evidence storage to a shared, access-controlled location. Documentation is what lets an organisation prove its controls operate, not just claim them. Grace adds a reminder to the quarterly checklist to confirm that evidence is stored correctly.

### Worked example

Priya builds a control register with dual control for backup keys and separation for certificate approval, and fixes evidence kept in personal email after an audit sample.

> **Synthetic case.** The controls and audit are invented; SP 800-57 is real.

### Errors and limits

Controls without evidence fail audits. Dual control erodes if staff share credentials to save time.

### Exercises

- **EX070 — Priority keys.** Which keys did Priya prioritise for controls? *Rubric:* 3 = the internal authority and backup keys;; 2 = one;; 1 = all equally;; 0 = none.
- **EX071 — Dual control example.** Give one dual control Priya applied. *Rubric:* 3 = restoring backup keys requires two administrators;; 2 = example;; 1 = vague;; 0 = none.
- **EX072 — Audit gap.** What audit gap was found and how was it fixed? *Rubric:* 3 = evidence in personal email; moved to shared access-controlled storage;; 2 = gap;; 1 = vague;; 0 = none.

### Synthesis

Prioritised key-management controls with separation, dual control and documented evidence make trust services auditable.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) build a small protected-export tool in a lab; (2) test it with positive and negative cases; (3) write a lab report.

### 25.1 The lab task

In Laboratory I, Priya's team builds a tool that exports synthetic patron records for a partner library, protected with authenticated encryption from a vetted library, using the parameters from Chapter 23. The tool loads a key from a test secret store, encrypts each record with associated data, and writes a file the partner can decrypt with the shared key. The lab uses only synthetic records; no real patron data enters the lab environment. Each team member reviews another member's code before tests run, so mistakes are caught early.

### 25.2 Testing

The team writes tests: decryption returns the original records; a tampered byte causes failure; swapping two records' associated data causes failure; a wrong key causes failure; and encrypting the same record twice produces different outputs. One test fails initially because the team accidentally reused a fixed nonce from an example snippet, so repeated encryptions matched. They remove the fixed nonce and let the library generate it. The failing test prevented a dangerous mistake from reaching production. They also add a regression test for the nonce bug.

### 25.3 The lab report

Priya writes the report: aim, design, parameters with citations, tests and results, the nonce bug and its fix, and limitations. Limitations include key sharing by manual transfer, which a later lab will replace, and lack of side-channel review. She includes the test output and states plainly that the tool relies on the library's cryptography and that the team implemented no primitives. Dr. Echeverría grades the report for clarity and honesty as well as correctness. She also attaches the test logs as an appendix.

### Worked example

The team's export tool passes five tests after a fixed-nonce bug from an example snippet is caught and removed, and Priya's report states limitations.

> **Synthetic case.** The lab and records are invented.

### Errors and limits

Example code often contains fixed keys or nonces for demonstration; never copy them. Manual key transfer is a weak point.

### Exercises

- **EX073 — Five tests.** List three of the five tests. *Rubric:* 3 = three of correct decryption, tamper fails, swapped AD fails, wrong key fails, different outputs;; 2 = two;; 1 = one;; 0 = none.
- **EX074 — Nonce bug.** What bug did testing reveal? *Rubric:* 3 = a fixed nonce copied from an example snippet, making repeated encryptions identical;; 2 = fixed nonce;; 1 = vague;; 0 = none.
- **EX075 — Report limitations.** Name one limitation in the report. *Rubric:* 3 = manual key transfer or no side-channel review;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Laboratory work proves design choices with tests, and honest reports record both bugs and limits.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Cryptography and trust services: methods II

### Learning outcomes

You will (1) explain digital signatures and verification; (2) apply signatures to documents and software; (3) choose between ECDSA and Ed25519.

### 26.1 How signatures work

A digital signature scheme has three operations: key generation, signing with a private key and verifying with the matching public key. FIPS 186-5 specifies ECDSA and EdDSA, and RFC 8032 specifies Ed25519. Anyone with the public key can verify that the signature matches the exact bytes signed, but only the private-key holder could create it. Priya contrasts this with HMAC, where verifiers share the secret and could create tags themselves. She demonstrates with a library that changing one byte of a signed file makes verification fail, while the original verifies.

### 26.2 Applying signatures

Tidewell signs two kinds of things. Contracts with publishers are signed as PDF documents with certificates, so either party can verify them years later. Software scripts deployed to branch servers are signed by the IT team, and servers refuse unsigned scripts. Priya explains that signatures prove origin and integrity but rely on protecting private keys and distributing trusted public keys. She recommends keeping the script-signing key in the key service, where signing requires an approved request. Grace approves the change for the next quarter.

### 26.3 ECDSA or Ed25519

Priya compares the two. ECDSA with P-256 is widely supported and allowed by FIPS 186-5, but requires a fresh secret value per signature, and implementations that reused or leaked it have exposed private keys. Ed25519 derives that value deterministically from the key and message, removing that failure mode, and is fast. Both are in FIPS 186-5. She recommends Ed25519 where supported and ECDSA through vetted libraries where compatibility requires, and notes that post-quantum signatures from FIPS 204 will be needed later. Grace adopts the recommendation.

### Worked example

Priya explains signing and verification, applies signatures to contracts and scripts with a key-service signing key, and recommends Ed25519 where supported.

> **Synthetic case.** Tidewell's signing uses are invented; FIPS 186-5, RFC 8032 and FIPS 204 are real.

### Errors and limits

Signatures are useless if private keys leak or public keys are not authenticated. Per-signature randomness failures in ECDSA have exposed keys.

### Exercises

- **EX076 — Three operations.** Name the three operations of a signature scheme. *Rubric:* 3 = key generation, signing, verification;; 2 = two;; 1 = one;; 0 = none.
- **EX077 — Script signing.** What do branch servers do with scripts, and where is the signing key kept? *Rubric:* 3 = refuse unsigned scripts; key in key service with approved requests;; 2 = both;; 1 = one;; 0 = none.
- **EX078 — Ed25519 advantage.** What failure mode does Ed25519 avoid? *Rubric:* 3 = per-signature secret derived deterministically, avoiding reused/leaked nonces exposing keys;; 2 = nonce;; 1 = vague;; 0 = none.

### Synthesis

Digital signatures prove origin and integrity publicly; Ed25519's deterministic design avoids a classic ECDSA failure.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Cryptography and trust services: verification

### Learning outcomes

You will (1) verify cryptographic configurations against requirements; (2) test certificate validation in applications; (3) report findings with evidence.

### 27.1 Configuration verification

Priya verifies Tidewell's services against its cryptographic requirements: TLS 1.2 minimum with TLS 1.3 preferred, certificates from approved authorities, no SHA-1 signatures and HSTS on public sites. With authorisation she runs configuration scanners and records results. The patron portal passes; the staff wiki, already flagged in Chapter 7, now supports TLS 1.3 but still accepts TLS 1.0, so the earlier change was incomplete. Verification after changes catches partial fixes. Priya reopens the original ticket and attaches the scan output, so the team can see exactly which protocol versions remain enabled and why the change was incomplete.

### 27.2 Testing validation

Applications must reject bad certificates. In a test environment Priya presents a reporting application with an expired certificate, a certificate for the wrong name and a self-signed certificate. The application rejects the first two but accepts the self-signed one, because a developer had added it to a trust list during testing and never removed it. She reports the issue and suggests that test trust settings live only in test configuration files that cannot ship to production. The developer removes the entry the same day.

### 27.3 Reporting findings

Priya's report lists each finding with severity, evidence, affected system and recommended fix, and separates confirmed findings from observations. She avoids sensational language and includes what passed, so readers see the overall state. Grace uses the report to schedule fixes, and Priya retests after each fix, recording dates. The report becomes evidence for the consortium's annual security review. Grace presents the summary to the consortium board, which approves budget for the remaining fixes. Priya keeps the raw scan outputs and test logs in the evidence store, linked from the report, so later reviewers can check every statement she made.

### Worked example

Priya verifies TLS settings, finds the staff wiki still accepting TLS 1.0 and a reporting app trusting a leftover self-signed certificate, and reports with evidence and retests.

> **Synthetic case.** Findings are invented.

### Errors and limits

Scanners miss application-level validation flaws; test them directly. Reports that omit passes distort the picture.

### Exercises

- **EX079 — Partial fix.** What did verification reveal about the staff wiki? *Rubric:* 3 = supports TLS 1.3 but still accepts TLS 1.0, so earlier fix incomplete;; 2 = partial;; 1 = fixed;; 0 = none.
- **EX080 — Self-signed acceptance.** Why did the reporting app accept a self-signed certificate? *Rubric:* 3 = a developer added it to the trust list during testing and never removed it;; 2 = test leftover;; 1 = bug in TLS;; 0 = none.
- **EX081 — Report contents.** What does each finding in the report include? *Rubric:* 3 = severity, evidence, affected system, recommended fix;; 2 = three;; 1 = one;; 0 = none.

### Synthesis

Verification after changes, direct validation tests and evidence-based reports keep cryptographic configurations honest.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Cryptography and trust services: failure analysis

### Learning outcomes

You will (1) analyse a key compromise scenario; (2) build a timeline and causal chain; (3) define corrective and preventive actions.

### 28.1 The scenario

In a tabletop exercise, Tidewell simulates a compromise: the portal's TLS private key was found in a public code repository, committed by a contractor months earlier. Priya leads the analysis. Immediate questions are what the key allows an attacker to do, impersonate the portal to patrons if they can intercept traffic, and what must happen now: revoke the certificate, issue a new key and certificate, deploy them and check for misuse. The exercise uses no real key. Facilitators play the roles of attacker and contractor.

### 28.2 Timeline and causes

Priya builds a timeline from the simulated evidence: the contractor copied server configuration into a repository for convenience, the repository was public, no secret scanning was in place and the key was never rotated. She draws a causal chain and identifies contributing factors: unclear contractor rules, no inventory alert for keys outside approved locations and long certificate lifetimes. She avoids blaming the contractor alone, since the process made the mistake easy. She presents the timeline on a single page so participants can see how small decisions accumulated into a serious exposure.

### 28.3 Actions

Corrective actions: revoke and replace the certificate, rotate related credentials, and search Certificate Transparency logs and access logs for misuse. Preventive actions: secret scanning in repositories, contractor guidance, shorter certificate lifetimes with automated renewal, and keys generated on servers so they never pass through people's hands. Priya assigns owners and dates and schedules a follow-up exercise to check the actions work. Grace assigns the secret-scanning action to the development lead and the contractor guidance to procurement. Priya notes that generating keys on servers also simplifies future rotation, because nobody needs to move keys between machines.

### Worked example

Priya analyses a simulated leaked TLS key, builds a timeline with process causes, and defines corrective and preventive actions with owners.

> **Synthetic case.** The scenario is invented and uses no real key.

### Errors and limits

Revocation checking is uneven in clients, so short lifetimes matter. Blame-focused analysis misses systemic causes.

### Exercises

- **EX082 — Attacker capability.** What could an attacker do with the leaked portal key? *Rubric:* 3 = impersonate the portal to patrons whose traffic they intercept;; 2 = impersonate;; 1 = read database;; 0 = none.
- **EX083 — Contributing factors.** Name two contributing factors. *Rubric:* 3 = two of unclear contractor rules, no inventory alert, long lifetimes, no secret scanning;; 2 = one;; 1 = blame contractor;; 0 = none.
- **EX084 — Preventive action.** Give two preventive actions. *Rubric:* 3 = two of secret scanning, contractor guidance, short lifetimes with automation, server-generated keys;; 2 = one;; 1 = revoke;; 0 = none.

### Synthesis

Failure analysis of key compromise focuses on process causes and pairs corrective with preventive actions.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Cryptography and trust services: operations

### Learning outcomes

You will (1) operate certificate renewal and monitoring; (2) read certificate lifetimes and renewal windows; (3) run routine key rotation.

### 29.1 Certificate operations

Following the lessons of Chapter 20, Tidewell automates certificate renewal for its public sites with ACME, the protocol in RFC 8555, and monitors expiry dates centrally. Industry practice is moving toward shorter certificate lifetimes, which limit the damage from leaked keys but require reliable automation. Priya reviews the consortium's certificates as of a synthetic date to check renewal windows and spot certificates still renewed by hand. She uses the review to decide which remaining certificates should move to automation first. Priority goes to services that patrons use directly, since their outages are most visible and most damaging to trust.

### Lab — Certificate windows

```python
"""Certificate validity windows for a synthetic consortium, with the shorter lifetimes trend."""
from datetime import date, timedelta
TODAY = date(2026, 9, 1)
SITES = [("catalog", date(2026, 7, 10), 90), ("patron-portal", date(2026, 6, 20), 90),
         ("ebooks", date(2025, 10, 1), 397), ("staff-wiki", date(2026, 8, 15), 47)]

def main():
    for name, issued, life in SITES:
        exp = issued + timedelta(days=life); left = (exp - TODAY).days
        print(f"{name:<14} life {life:>3} d expires {exp} left {left:>4} d")
    print("renew soon (<21 d):", [n for n, i, l in SITES if (i + timedelta(days=l) - TODAY).days < 21])

if __name__ == "__main__":
    main()
```

Run with `python3 lab_certdays.py`. Verified output:

```text
catalog        life  90 d expires 2026-10-08 left   37 d
patron-portal  life  90 d expires 2026-09-18 left   17 d
ebooks         life 397 d expires 2026-11-02 left   62 d
staff-wiki     life  47 d expires 2026-10-01 left   30 d
renew soon (<21 d): ['patron-portal']
```

### 29.2 Reading the windows

On 1 September 2026 the patron portal certificate has seventeen days left and is flagged for renewal within the three-week window; the catalogue has thirty-seven days, the staff wiki thirty and the e-book site sixty-two. The e-book site's 397-day lifetime marks it as manually managed, an outlier now that the others use ninety days or less. Priya checks why the portal's automated renewal has not yet run and finds that its ACME client starts at a third of lifetime remaining, about thirty days, but failed silently after a firewall change. She fixes the rule and adds an alert on renewal failures.

### 29.3 Routine rotation

Beyond certificates, Priya schedules routine rotation of backup and database keys yearly using envelope encryption, so only data keys are re-wrapped. Each rotation follows a runbook with checks and rollback, and is recorded in the inventory. She also tests restoring a backup encrypted under the previous key, because a rotation that makes old backups unreadable would be a disaster. Operations succeed when they are routine, documented and tested. She records each rotation in the inventory with its date, so future auditors can confirm that keys were changed on schedule and old backups remained readable.

### Worked example

Priya finds the portal certificate flagged with seventeen days left because ACME renewal failed silently after a firewall change, fixes it with an alert, and schedules tested key rotation.

> **Synthetic case.** Dates and certificates are invented; RFC 8555 is real.

### Errors and limits

Automation fails silently without alerts. Rotation must keep old backups readable.

### Exercises

- **EX085 — Flagged certificate.** Which certificate was flagged and with how many days left? *Rubric:* 3 = patron-portal, 17 days;; 2 = name;; 1 = wrong;; 0 = none.
- **EX086 — Outlier lifetime.** Why is the e-book site an outlier? *Rubric:* 3 = 397-day lifetime indicates manual management versus 90 days or less elsewhere;; 2 = long;; 1 = short;; 0 = none.
- **EX087 — Rotation test.** Why test restoring an old backup after rotation? *Rubric:* 3 = rotation must not make old backups unreadable;; 2 = readability;; 1 = not needed;; 0 = none.

### Synthesis

Automated renewal with alerts and tested rotation make cryptographic operations routine rather than emergencies.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) replace manual key sharing with a public-key exchange in a lab; (2) sign and verify exported files; (3) evaluate the improved design.

### 30.1 Improving the export tool

Laboratory II returns to the export tool from Laboratory I, whose weak point was manual key sharing. Priya's team redesigns it with hybrid public-key encryption: the partner library publishes a public key, and the tool encrypts each export with a fresh symmetric key wrapped for that public key, following the hybrid public key encryption pattern in RFC 9180, using a vetted library. The team also signs each export with Tidewell's Ed25519 key so the partner can verify its origin. Each export carries its signature beside it.

### 30.2 Testing the new design

Tests check that the partner can decrypt and verify; that a file signed with the wrong key fails verification; that a file encrypted for another partner cannot be decrypted; and that tampering is detected. A test reveals that the tool signed the plaintext but the partner verified after decryption with a different associated data value, causing false failures. The team aligns the signed content definition in both tools, learning that sender and receiver must agree exactly on what is signed.

### 30.3 Evaluating the design

Priya evaluates improvements: no shared secret moves by email; each export has its own key; origin is verifiable. Remaining issues include distributing and trusting the partner's public key, which the team handles by exchanging key fingerprints in a meeting, and key rotation for both parties. She records that the team used library functions throughout and implemented no cryptographic primitives. The evaluation compares the designs in a table with security, usability and operational effort. Grace agrees to adopt the design for real partner exports.

### Worked example

The team replaces manual key sharing with library-based hybrid public-key encryption and Ed25519 signatures, fixes a mismatch in signed content and evaluates the design.

> **Synthetic case.** The lab is invented; RFC 9180 and RFC 8032 are real.

### Errors and limits

Public keys must be authenticated, for example by fingerprint comparison. Mismatched definitions of signed content cause false failures or gaps.

### Exercises

- **EX088 — Hybrid pattern.** How does the new tool encrypt exports? *Rubric:* 3 = fresh symmetric key per export wrapped for partner's public key (RFC 9180 pattern);; 2 = wrapped;; 1 = shared password;; 0 = none.
- **EX089 — Signature mismatch.** What caused false verification failures? *Rubric:* 3 = sender and receiver disagreed on signed content definition;; 2 = mismatch;; 1 = wrong key;; 0 = none.
- **EX090 — Fingerprint exchange.** How did the team trust the partner's public key? *Rubric:* 3 = exchanged key fingerprints in a meeting;; 2 = fingerprints;; 1 = trusted email;; 0 = none.

### Synthesis

Public-key encryption and signatures remove shared-secret transfer, provided keys are authenticated and both sides agree on what is signed.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Cryptography and trust services: advanced cases

### Learning outcomes

You will (1) analyse post-quantum migration for a small organisation; (2) evaluate end-to-end encrypted messaging for patron services; (3) weigh advanced options against capacity.

### 31.1 Post-quantum migration

Priya studies NIST's post-quantum standards: ML-KEM in FIPS 203 for key establishment, and ML-DSA in FIPS 204 and SLH-DSA in FIPS 205 for signatures. The main near-term risk is "harvest now, decrypt later": recorded traffic could be decrypted once large quantum computers exist. For Tidewell, the most sensitive long-lived data is patron reading history. Priya recommends relying on suppliers and libraries that adopt hybrid key exchange in TLS, keeping inventories ready for migration, and not attempting any custom implementation. She records the recommendation in the inventory plan.

### 31.2 End-to-end messaging

Tidewell considers letting patrons message librarians about sensitive topics, such as health information requests. Priya evaluates end-to-end encrypted messaging, where only the patron and librarian devices hold keys, so even the consortium's servers cannot read messages. Benefits include strong privacy; costs include losing messages if a device is lost, difficulty with shared librarian inboxes and inability to scan for abuse. She recommends a reputable existing service with published security design rather than building one. Grace takes the recommendation to the outreach team.

### 31.3 Capacity and priorities

Priya weighs these advanced options against Tidewell's capacity: a small IT team, limited budget and many basic gaps still open. She recommends finishing basic controls first, such as inventory, automated renewal and backup encryption, then adopting post-quantum protections through supplier updates as they arrive. Advanced cryptography adds value only when foundations are in place, and complexity beyond the team's ability to operate it becomes a risk itself. Grace agrees and adds the advanced options to a three-year roadmap, to be revisited once the basic controls are complete and measured.

### Worked example

Priya recommends post-quantum readiness through suppliers and inventories, an existing end-to-end messaging service for sensitive patron requests, and finishing basic controls first.

> **Synthetic case.** Tidewell's options are invented; FIPS 203, 204 and 205 are real.

### Errors and limits

Post-quantum migration timelines are uncertain; avoid panic and complacency. End-to-end encryption shifts risk to device and key loss.

### Exercises

- **EX091 — Harvest now.** What does "harvest now, decrypt later" mean? *Rubric:* 3 = recorded traffic decrypted later when large quantum computers exist;; 2 = future decryption;; 1 = vague;; 0 = none.
- **EX092 — E2E cost.** Name two costs of end-to-end encrypted patron messaging. *Rubric:* 3 = two of message loss with devices, shared inbox difficulty, no abuse scanning;; 2 = one;; 1 = vague;; 0 = none.
- **EX093 — Priority advice.** What did Priya advise before adopting advanced options? *Rubric:* 3 = finish basic controls first (inventory, renewal, backup encryption);; 2 = basics;; 1 = rush;; 0 = none.

### Synthesis

Advanced cryptography should follow solid foundations and arrive through vetted suppliers matched to the organisation's capacity.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Cryptography and trust services: interdisciplinary interfaces

### Learning outcomes

You will (1) connect cryptographic decisions to law, policy and user experience; (2) explain electronic signatures in legal contexts; (3) design understandable security interactions.

### 32.1 Law and policy

Cryptographic decisions touch law. Data-protection law may require appropriate security for personal data, and encryption can reduce breach notification duties in some jurisdictions when keys remain safe. Electronic signature laws recognise different levels of signatures, and some contexts require qualified trust service providers. Priya studies Tidewell's obligations with the consortium's legal adviser and learns to phrase technical facts precisely so lawyers can map them to legal terms without misunderstanding. Priya keeps a short glossary for the adviser, defining terms such as key, certificate and signature in plain language.

### 32.2 Electronic signatures

Priya explains to the legal adviser that a digital signature is a cryptographic mechanism, while an electronic signature is a legal concept that may include typed names or scanned images. Publisher contracts use certificate-based digital signatures, which give stronger evidence of integrity and origin. She documents how long signed contracts must remain verifiable and recommends adding timestamps from a trusted timestamping service, so signatures can be validated even after the signing certificate expires. The adviser adds the timestamp requirement to the contract template.

### 32.3 User experience

Security interactions must be understandable. Priya redesigns the portal's login and recovery screens with a designer: clear wording on passphrases, an explanation of why one-time codes help and a recovery process that does not rely on easily guessed questions. She tests with ten volunteers, including older patrons, and revises unclear wording. She learns that confusing security leads users to unsafe workarounds, so usability is part of security, not its opponent. Two volunteers mention that the new wording finally explains why one-time codes are worth the extra step.

### Worked example

Priya clarifies digital versus electronic signatures for the legal adviser, recommends trusted timestamps for long-term contract validation, and user-tests clearer login and recovery screens.

> **Synthetic case.** Tidewell's legal context is invented; specific laws vary by jurisdiction.

### Errors and limits

Legal requirements differ by jurisdiction; consult qualified advisers. Usability tests with few users find major issues but not all.

### Exercises

- **EX094 — Digital versus electronic.** Distinguish a digital signature from an electronic signature. *Rubric:* 3 = digital is cryptographic mechanism; electronic is legal concept that can include typed names;; 2 = partial;; 1 = same;; 0 = none.
- **EX095 — Timestamp purpose.** Why add trusted timestamps to signed contracts? *Rubric:* 3 = so signatures can be validated after the signing certificate expires;; 2 = long-term;; 1 = vague;; 0 = none.
- **EX096 — Usability link.** Why is usability part of security? *Rubric:* 3 = confusing security drives unsafe workarounds;; 2 = workarounds;; 1 = unrelated;; 0 = none.

### Synthesis

Cryptography meets law, policy and people; precise language and usable designs make it effective across disciplines.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) analyse data from a small security study; (2) report results with uncertainty; (3) discuss validity threats.

### 33.1 Running the study

Priya runs the certificate-warning study planned in Chapter 18. Sixty staff are randomly assigned to two groups; one reads a one-page explanation of certificate warnings first. All later see a simulated warning on the training site. In the control group, 18 of 30 proceed past the warning; in the explanation group, 9 of 30 proceed. Data are anonymous and stored according to the ethics approval. Everyone is debriefed afterwards. Priya checks that group sizes and baseline roles are similar across the two groups before comparing results, and records any imbalance she finds.

### 33.2 Reporting with uncertainty

The proportions are 60 percent and 30 percent. Priya computes the difference, 30 percentage points, and uses a permutation test, shuffling group labels many times, to estimate how often a difference this large would appear by chance; it is rare, under five percent of shuffles. She reports the difference with its uncertainty, noting the small sample. She avoids saying the explanation "works", writing instead that it was associated with fewer staff proceeding in this simulation. She shares the permutation script with the class so others can rerun it.

### 33.3 Validity threats

Priya discusses threats. Staff in the explanation group might have guessed the study's purpose and behaved differently. A training site differs from real work pressure. Thirty people per group cannot reveal small effects or effects in subgroups. Results come from one consortium. She recommends repeating the study elsewhere and measuring behaviour weeks later to test whether the effect lasts. Honest discussion of threats is part of the result, not an apology for it. Dr. Echeverría asks her to include the threats in the abstract.

### Worked example

Priya reports 60 versus 30 percent proceeding past a simulated warning, a permutation result under five percent, and four validity threats.

> **Synthetic case.** The study data are invented.

### Errors and limits

Small samples give unstable estimates. Simulated settings may not reflect real behaviour.

### Exercises

- **EX097 — Study results.** Report the share proceeding in each group. *Rubric:* 3 = 60 percent control (18/30) and 30 percent explanation (9/30);; 2 = one;; 1 = wrong;; 0 = none.
- **EX098 — Careful wording.** How does Priya describe the effect? *Rubric:* 3 = associated with fewer staff proceeding in this simulation, not "works";; 2 = careful;; 1 = "works";; 0 = none.
- **EX099 — Validity threat.** Name two validity threats. *Rubric:* 3 = two of guessing purpose, simulation vs real pressure, small sample, single consortium;; 2 = one;; 1 = vague;; 0 = none.

### Synthesis

Small studies can inform practice when results come with uncertainty and openly discussed threats.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two approaches to a trust problem; (2) define fair criteria; (3) recommend with justification.

### 34.1 The comparison

Priya's comparative project asks how Tidewell should give branch staff access to the staff wiki: passwords with one-time codes, or device certificates issued by the internal authority plus security keys for administrators. She defines the problem, the users and the threats, and states that both approaches must work for part-time volunteers who use shared branch computers. Comparisons are fair only when both options are tested against the same requirements. She also sets a time budget so the comparison can finish within the term, and agrees it with Grace and Dr. Echeverría.

### 34.2 Criteria and evidence

Priya defines criteria: resistance to phishing, effort for staff, administrative effort, cost, behaviour on shared computers and recovery when credentials are lost. She gathers evidence from a two-week trial in two branches, logs support requests and interviews staff. Device certificates remove passwords but fail on shared computers used by several people; one-time codes work anywhere but remain phishable. Security keys resist phishing but cost money and get lost. She tabulates support requests by type, finding that lost one-time code devices cause the most calls during the trial.

### 34.3 Recommendation

Priya recommends a mixed approach: device certificates to identify branch computers, combined with individual sign-in using passphrases and one-time codes for volunteers, and security keys for staff with access to patron data and for administrators. She justifies each choice by criteria and evidence and states what would change her view, such as lower security-key prices. The comparative method makes her recommendation traceable rather than a matter of preference. Grace accepts the recommendation and asks for a rollout plan covering the twelve branches over two terms.

### Worked example

Priya compares access approaches against six criteria in a two-branch trial and recommends device certificates plus individual sign-in, with security keys for privileged staff.

> **Synthetic case.** The trial is invented.

### Errors and limits

Short trials miss long-term problems. Mixed approaches add complexity that must be documented.

### Exercises

- **EX100 — Shared computers.** Why do device certificates alone fail for branch volunteers? *Rubric:* 3 = shared computers are used by several people, so devices do not identify individuals;; 2 = shared;; 1 = they work;; 0 = none.
- **EX101 — Criteria.** List four of Priya's criteria. *Rubric:* 3 = four of phishing resistance, staff effort, admin effort, cost, shared computers, recovery;; 2 = three;; 1 = one;; 0 = none.
- **EX102 — Changing view.** What would change Priya's recommendation? *Rubric:* 3 = lower security-key prices (or similar evidence change);; 2 = condition;; 1 = vague;; 0 = none.

### Synthesis

Comparing options against shared criteria with trial evidence yields traceable recommendations.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) propose a capstone that improves a trust service; (2) define scope, deliverables and evaluation; (3) obtain partner agreement.

### 35.1 Choosing the capstone

Priya proposes a capstone: a certificate and key inventory with automated discovery, expiry monitoring and owner alerts for Tidewell, building on lessons from the catalogue outage and the leaked-key exercise. The problem is clear, the partner needs it and the scope fits one academic year. She states the aim: every certificate and key in scope is listed with an owner, and no certificate expires without at least two alerts thirty and seven days before. She checks with Grace that the aim matches the consortium's priorities.

### 35.2 Scope and deliverables

In scope are public and internal TLS certificates and keys in the key service; out of scope are staff security keys and supplier-held keys. Deliverables are a discovery script that scans authorised hosts for certificates, an inventory database, an alerting service, documentation and a handover to Grace's team. The tools use the standard library and existing scanners; no cryptographic primitives are implemented. She lists risks, such as access to internal networks, with mitigations. She also writes a short data-handling plan for the scan results.

### 35.3 Evaluation and agreement

Priya defines evaluation: discovery finds all certificates in a test environment seeded with known certificates; alerts fire correctly for synthetic expiry dates; and staff can use the inventory without help after a short training. Grace signs the proposal, including authorisation to scan listed hosts. Dr. Echeverría approves it with one change: add a measure of false alerts, since noisy alerts would undermine adoption. Priya adds the false-alert target to the evaluation plan, aiming for fewer than one false alert per month, and agrees with Grace how alerts will be reviewed.

### Worked example

Priya proposes a certificate and key inventory with discovery and alerts, scopes it, defines evaluation and obtains signed partner authorisation, adding a false-alert measure.

> **Synthetic case.** The capstone is invented.

### Errors and limits

Scanning beyond authorised hosts is not allowed even for good purposes. Overly broad scope threatens delivery.

### Exercises

- **EX103 — Capstone aim.** State the capstone's aim. *Rubric:* 3 = every in-scope certificate and key listed with owner; no expiry without alerts at 30 and 7 days;; 2 = aim;; 1 = vague;; 0 = none.
- **EX104 — Out of scope.** What is out of scope? *Rubric:* 3 = staff security keys and supplier-held keys;; 2 = one;; 1 = vague;; 0 = none.
- **EX105 — Added measure.** What change did Dr. Echeverría require? *Rubric:* 3 = add a measure of false alerts;; 2 = false alerts;; 1 = vague;; 0 = none.

### Synthesis

A capstone proposal with clear aim, scope, deliverables, evaluation and authorisation sets up a useful and feasible project.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) apply cryptographic knowledge in community service; (2) teach security basics to non-specialists; (3) respect boundaries of advice.

### 36.1 Community workshops

As part of field practice, Priya runs workshops at Tidewell branches on digital safety for patrons. Topics include recognising browser certificate warnings, using passphrases and password managers, turning on two-step sign-in and understanding what encrypted messaging protects. She adapts language for each audience: teenagers, job seekers and older adults. She brings printed handouts and avoids collecting any personal information from participants. Each workshop lasts an hour and ends with a short practical exercise, such as turning on two-step sign-in for a demonstration account the library provides.

### 36.2 Teaching effectively

Priya uses concrete demonstrations: comparing a padlock warning on a deliberately misconfigured test site with a normal site, and generating a random passphrase with dice to show why random choices matter. She checks understanding with short questions rather than lecturing. Feedback shows participants valued learning how to use a password manager most. She revises the workshop to spend more time on that, learning that teaching should follow learners' needs, not the teacher's interests. She also keeps a log of which demonstrations work best.

### 36.3 Boundaries of advice

Some participants ask Priya to fix their personal devices or recover hacked accounts. She explains the limits of her role, points them to official recovery pages and the library's referral list, and never asks for passwords or accesses their accounts. She records anonymous topics of questions to improve future workshops. Dr. Echeverría praises her for maintaining boundaries, which protects both participants and the student. She shares the anonymous question log with the outreach team, who use it to plan future sessions and to update the library's printed guides on online safety.

### Worked example

Priya runs patron workshops with demonstrations, adapts content after feedback toward password managers, and keeps clear boundaries on personal device help.

> **Synthetic case.** The workshops are invented.

### Errors and limits

Well-meant personal help can expose participants' data. Demonstrations must never use real accounts.

### Exercises

- **EX106 — Dice demonstration.** Why use dice to generate a passphrase in workshops? *Rubric:* 3 = shows that random choices are stronger than chosen ones;; 2 = randomness;; 1 = fun;; 0 = none.
- **EX107 — Workshop revision.** How did Priya revise the workshop? *Rubric:* 3 = more time on password managers based on feedback;; 2 = feedback;; 1 = vague;; 0 = none.
- **EX108 — Boundary.** How did she respond to requests to fix personal accounts? *Rubric:* 3 = explained limits, pointed to official recovery and referrals, never asked for passwords;; 2 = boundary;; 1 = fixed them;; 0 = none.

### Synthesis

Community practice turns cryptographic knowledge into practical safety for the public, within clear boundaries.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critically review evidence about cryptographic practice; (2) assess sources' quality; (3) present a balanced synthesis.

### 37.1 The seminar task

In the evidence review seminar, each student reviews evidence on a question. Priya's is: "Does automated certificate management reduce expiry outages?" She gathers sources: the ACME specification, RFC 8555, which describes the protocol but not outcomes; peer-reviewed measurement studies of certificate ecosystems; operator reports; and her own Tidewell data. She classifies each by type and strength, noting that a specification explains how something works but not whether it improves results. She records each source in a table with its type, date and author, so peers can follow her reasoning.

### 37.2 Assessing quality

Priya assesses each source: who produced it, the method, sample, possible conflicts of interest and whether results can be checked. Vendor reports claim large reductions but give no method. Measurement studies offer large samples but measure certificate lifetimes, not outages. Her Tidewell data are accurate but tiny. She learns to weigh evidence by quality rather than by how often a claim is repeated, and to say when evidence is indirect. She asks a classmate to rate the sources independently and compares their ratings.

### 37.3 Balanced synthesis

Priya's synthesis says that evidence consistently suggests automation shortens certificate lifetimes and reduces manual work, that direct evidence on outage reduction is limited and mostly from operator reports, and that automation introduces silent failure modes requiring monitoring, as Tidewell's own portal case showed. She presents the synthesis with a table of sources and strengths. Peers question her treatment of vendor reports, and she adds a note explaining why she gave them low weight. The seminar leader commends the synthesis as a model.

### Worked example

Priya reviews sources on automated certificate management, weighs vendor, measurement and local data by quality, and presents a balanced synthesis noting silent-failure risks.

> **Synthetic case.** Her local data are invented; RFC 8555 is real.

### Errors and limits

Evidence that is repeated widely is not necessarily strong. Local data rarely generalise.

### Exercises

- **EX109 — Specification limit.** What can RFC 8555 tell Priya, and what not? *Rubric:* 3 = how ACME works, not whether it reduces outages;; 2 = partial;; 1 = outcomes;; 0 = none.
- **EX110 — Vendor weight.** Why did vendor reports receive low weight? *Rubric:* 3 = they give no method and may have conflicts of interest;; 2 = no method;; 1 = high weight;; 0 = none.
- **EX111 — Synthesis caveat.** What caveat does the synthesis include about automation? *Rubric:* 3 = automation introduces silent failure modes requiring monitoring;; 2 = silent failures;; 1 = vague;; 0 = none.

### Synthesis

Critical review weighs evidence by quality and directness, producing balanced conclusions with stated caveats.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) implement the capstone inventory and alerting; (2) test against a seeded environment; (3) manage changes during implementation.

### 38.1 Building the inventory

Priya implements the capstone. A discovery script connects to authorised hosts, retrieves certificates using the standard library's ssl module and records subject names, issuers, validity dates and fingerprints. Keys are listed from the key service's metadata interface, never by reading key material. Each record links to an owner from the staff directory. An alerting service checks daily for certificates within thirty and seven days of expiry and sends messages to owners and a shared mailbox. The code is reviewed by a classmate before deployment.

### 38.2 Testing in a seeded environment

Priya seeds a test environment with fifteen certificates: some valid, some expiring soon, some expired and two hidden on unusual ports. Discovery finds thirteen at first, missing the two on unusual ports. She adds those ports to the scan profile after confirming they are within authorisation, and discovery finds all fifteen. Alerts fire correctly for synthetic dates, with one false alert caused by a time-zone error, which she fixes by storing all dates in UTC. She keeps the seeded environment for regression testing.

### 38.3 Managing changes

Midway, Grace asks whether the tool can also track code-signing keys. Priya assesses the request against the proposal: it would add scope and risk to the timeline. She records it as a future enhancement, agrees with Grace and Dr. Echeverría to keep the original scope, and designs the inventory so the addition is easy later. Managing scope protects delivery and keeps the evaluation meaningful. She also writes a short design note describing how code-signing keys could be added later, so the next maintainer has a clear starting point and estimated effort.

### Worked example

Priya's discovery finds all fifteen seeded certificates after adding authorised ports, fixes a time-zone false alert with UTC, and defers code-signing keys as a planned enhancement.

> **Synthetic case.** The environment is invented.

### Errors and limits

Time handling causes subtle errors; store UTC. Scans must stay within authorisation even when expanding coverage.

### Exercises

- **EX112 — Discovery gap.** What did discovery miss at first and how was it fixed? *Rubric:* 3 = two certificates on unusual ports; added authorised ports to scan profile;; 2 = missed;; 1 = vague;; 0 = none.
- **EX113 — False alert cause.** What caused the false alert? *Rubric:* 3 = a time-zone error, fixed by storing dates in UTC;; 2 = time zone;; 1 = bug;; 0 = none.
- **EX114 — Scope request.** How did Priya handle the code-signing request? *Rubric:* 3 = recorded as future enhancement, kept scope, designed for easy addition;; 2 = deferred;; 1 = added;; 0 = none.

### Synthesis

Implementation tested against seeded data and disciplined scope management delivers a reliable capstone.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against its criteria; (2) measure adoption and false alerts; (3) recommend next steps.

### 39.1 Evaluation results

Priya evaluates the capstone against the proposal. In the seeded test environment, discovery finds fifteen of fifteen certificates. In production, it finds forty-two certificates, including three that nobody had recorded. Over two months, alerts fire for six real expiries, all renewed in time, with one false alert in total. Staff complete common inventory tasks after a twenty-minute training. The aim is met for the scoped systems. She presents these results in a table that compares each measured value with the target set in the proposal, showing exactly where the aim was met.

### 39.2 Adoption and limits

Adoption is uneven: two branch IT volunteers ignore alert messages sent to personal addresses, so Priya routes alerts to the shared mailbox monitored by Grace's team. She lists limits: the inventory covers only scanned hosts, cannot see certificates on devices outside the network and depends on the staff directory being current. She reports that one alert was acted on only after the seven-day reminder, showing the second alert's value. She adds a monthly check that the staff directory matches current owners.

### 39.3 Next steps

Priya recommends next steps: add code-signing keys, as Grace requested; integrate with ACME renewal logs to spot failed renewals sooner; and review owners quarterly. She also recommends that the consortium keep the tool simple and maintained rather than adding features that would require skills the team lacks. Her evaluation report includes data tables, screenshots and a short guide for maintainers. Grace agrees to assign one team member as the tool's maintainer, with time set aside each month. Priya offers to help during the first maintenance cycle so that knowledge transfers smoothly.

### Worked example

Priya's evaluation finds forty-two production certificates including three unrecorded, six expiries handled with one false alert, and recommends routing alerts to a shared mailbox and modest next steps.

> **Synthetic case.** Results are invented.

### Errors and limits

Two months is short for evaluating reliability. Tools without maintainers decay.

### Exercises

- **EX115 — Production findings.** How many certificates were found in production, and how many were unrecorded? *Rubric:* 3 = 42, including 3 unrecorded;; 2 = one number;; 1 = wrong;; 0 = none.
- **EX116 — Alert routing.** Why were alerts moved to a shared mailbox? *Rubric:* 3 = volunteers ignored alerts sent to personal addresses;; 2 = ignored;; 1 = preference;; 0 = none.
- **EX117 — Second alert value.** What showed the value of the seven-day reminder? *Rubric:* 3 = one alert was acted on only after the seven-day reminder;; 2 = reminder;; 1 = vague;; 0 = none.

### Synthesis

Honest evaluation measures results, adoption and limits, and leads to modest, sustainable next steps.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write a bachelor's thesis on the capstone; (2) present findings to academic and partner audiences; (3) reflect on learning.

### 40.1 Writing the thesis

Priya's thesis presents the problem of unmanaged certificates and keys at Tidewell, related standards and evidence, the design and implementation of the inventory, the evaluation and conclusions. Each claim cites evidence: the catalogue outage, the leaked-key exercise, the seeded tests and the production results. She describes the tool's reliance on standard library functions and existing scanners, and states that no cryptographic primitives were implemented. Dr. Echeverría reminds her to keep the thesis focused on what she can show. She revises two chapters accordingly.

### 40.2 Presenting

Priya gives two presentations. For the academic panel she emphasises method, evaluation and limits; for Tidewell's board she emphasises outcomes in plain words: no certificate expiry since the tool went live, three forgotten certificates found and a clear owner for every key. She prepares for questions about cost, maintenance and privacy, and answers a board member's question about whether the tool reads patron data: it does not, as it handles only certificates and key metadata. The board asks to receive quarterly inventory reports.

### 40.3 Reflection

In her reflection Priya looks back over four years: from proving XOR identities to running an operational tool. She notes that the hardest problems were rarely mathematical; they were inventories, ownership, communication and silent failures. She also notes the value of foundations: understanding why nonces must be unique or why salts matter let her judge tools and suppliers. She plans to continue in a postgraduate course and to keep volunteering at Tidewell's workshops. Dr. Echeverría encourages her to submit the evaluation as a short practitioner article.

### Worked example

Priya's thesis argues from evidence, her board presentation reports no expiries since go-live, and her reflection identifies operational problems as harder than mathematical ones.

> **Synthetic case.** Outcomes are invented.

### Errors and limits

Theses that drift beyond the evidence lose credibility. Presentations must match the audience without changing the facts.

### Exercises

- **EX118 — Board emphasis.** What did Priya emphasise for the board? *Rubric:* 3 = outcomes in plain words: no expiries, three forgotten certificates found, owner for every key;; 2 = outcomes;; 1 = method;; 0 = none.
- **EX119 — Patron data question.** How did she answer whether the tool reads patron data? *Rubric:* 3 = it does not; it handles only certificates and key metadata;; 2 = no;; 1 = yes;; 0 = none.
- **EX120 — Hardest problems.** What did Priya find hardest over four years? *Rubric:* 3 = inventories, ownership, communication and silent failures rather than mathematics;; 2 = operational;; 1 = maths;; 0 = none.

### Synthesis

A bachelor's thesis grounded in evidence, presented to each audience honestly, closes four years of learning with practical impact.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Priya Raman, Dr. Tomás Echeverría, Grace Okafor, Ashford University, Tidewell Public Library Consortium and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Without a precise definition of security and of the attacker, the claim cannot be proved or tested.

**EX002.** x XOR x equals 0 and x XOR 0 equals x, so XORing the key again restores the message.

**EX003.** It recovered "FINE PAID 0938", since XORing the ciphertexts cancels the key and the first message was known.

**EX004.** Disk encryption covers stored data, whereas data in transit needs network protection such as TLS.

**EX005.** Mostly access control and operating-system isolation, because data must be decrypted to be processed.

**EX006.** Off-site backup tapes were unencrypted; she proposed encrypting them with keys the consortium controls, with a safe key backup.

**EX007.** Because é is encoded with two bytes in UTF-8, plus one byte for each other letter.

**EX008.** By comparing her digest of "abc" with the published FIPS 180-4 example, which begins ba7816bf.

**EX009.** If an attacker can change both the files and the stored list, changes go unnoticed, so the list needs protection or a signature.

**EX010.** A paragraph that used hash, salt and key derivation without defining them for a general reader.

**EX011.** FIPS 180-4 for SHA-256 and RFC 9106 for Argon2.

**EX012.** Argon2id makes every guess expensive in time and memory, slowing offline attacks, though weak passwords can still be guessed.

**EX013.** Non-repudiation, along with integrity and authentication.

**EX014.** A MAC uses one shared secret key and cannot prove which holder made it; a signature uses a private key and public verification, supporting non-repudiation.

**EX015.** The padlock shows TLS protects the connection in transit, not data stored on servers or devices.

**EX016.** Closure, associativity, an identity element and an inverse for every element.

**EX017.** Both parties computed 2, after exchanging the public values 8 and 19.

**EX018.** A large quantum computer running it would solve discrete logarithms efficiently, which is why post-quantum standards such as FIPS 203 exist.

**EX019.** To prove possession of the certificate's private key and to protect the handshake from tampering.

**EX020.** It checks the chain to a trusted root, that the name matches and that the date is within validity.

**EX021.** The staff wiki still accepted the outdated TLS 1.0 protocol.

**EX022.** They make secure choices about nonces, modes and padding by default, so fewer mistakes are possible.

**EX023.** So that neither callers nor attackers learn which check failed.

**EX024.** That the tokens differ, which shows a fresh nonce is used each time.

**EX025.** It is so fast that stolen hashes can be guessed at enormous rates, and equal passwords produce equal hashes.

**EX026.** The same password stored with two salts produced two different values.

**EX027.** Deleting data that is no longer needed, since absent data cannot leak.

**EX028.** The hosts in scope, the testing dates and the tools allowed.

**EX029.** Because they hold real people's passwords and personal data, whatever their public availability.

**EX030.** She stopped testing, reported it to the vendor's security contact with a ninety-day window and told her lecturer.

**EX031.** It stops the key from being copied elsewhere, so malware can misuse it only while present on that machine.

**EX032.** Because random's output can be predicted, while secrets draws on the operating system's secure generator.

**EX033.** During sleep the memory, including disk encryption keys, stays powered and could be read.

**EX034.** The base-2 logarithm of N.

**EX035.** Four random words give 51.7 bits, more than the 47.6 bits of eight random mixed characters.

**EX036.** People pick predictable phrases that attackers try early, so choices are far from uniform.

**EX037.** Both sides compute HMAC over their shared secret and the current time window.

**EX038.** The signature includes the real site's origin, so a fake site receives a response it cannot reuse.

**EX039.** Requiring them would shut out many patrons who lack or cannot use such devices.

**EX040.** Because it can reveal health conditions, religious beliefs or political views.

**EX041.** Card numbers follow a known format, so an attacker can hash every possible number and match.

**EX042.** Delete each loan record after return unless the patron chooses to keep a history.

**EX043.** Each hash covers the previous hash, so a change propagates through the rest of the chain.

**EX044.** The head changed from 4492b592 to c3664171, with the first difference at entry 2.

**EX045.** Outside the insider's control, such as a separate auditor's system, otherwise the whole chain can be rewritten.

**EX046.** Between the internet and the portal, and between the portal and the patron database.

**EX047.** Database permissions and field-level encryption.

**EX048.** They left out where keys lived, so nobody could plan rotation or judge who could decrypt data.

**EX049.** A system should stay secure when everything about it except the key is publicly known.

**EX050.** It took the most frequent ciphertext letter, P, as E, which gave a shift of 11.

**EX051.** Identical messages produce identical ciphertexts, so an attacker can tell when messages repeat.

**EX052.** A defined population, a measurable behaviour and an intervention to compare.

**EX053.** Each study's population, method and findings, noting whether it observed laboratory or real behaviour.

**EX054.** That managers would never see any individual's results.

**EX055.** Certificate authorities, timestamping services, signature creation and validation services, and key management services.

**EX056.** Every trusted root can certify any name, so a single compromised authority can undermine everyone.

**EX057.** They thought the signature covered terms in an attachment that was not part of the signed bytes.

**EX058.** Procedural causes such as poor validation or monitoring, rather than broken mathematics.

**EX059.** Any certificate issued for Tidewell's names, so misissued ones can be spotted.

**EX060.** Manual renewal owned by someone who had left, no expiry alert, and no record of which server held the key.

**EX061.** That a given patron is entitled to borrow a particular title for fourteen days.

**EX062.** Issue certificates that make their own devices look like staff devices.

**EX063.** That the people administering the key service should not also control its audit logs.

**EX064.** Two forgotten certificates on old servers and a backup key sitting in a shared folder.

**EX065.** She scheduled its replacement, following the transition guidance in SP 800-131A.

**EX066.** She logged it as a risk rather than a failure, since migration is still early.

**EX067.** So that moving an encrypted record to another patron's identifier makes decryption fail.

**EX068.** Roughly 2^32 encryptions under one key.

**EX069.** Because engineers should check that the library's choices meet the standard rather than design their own.

**EX070.** The internal certificate authority key and the backup keys.

**EX071.** Restoring backup keys needs two administrators acting together.

**EX072.** Evidence was in personal email, so storage moved to a shared, access-controlled location.

**EX073.** Correct decryption, failure on a tampered byte and failure with a wrong key.

**EX074.** A fixed nonce taken from example code, so repeated encryptions were identical.

**EX075.** Keys were shared by manual transfer.

**EX076.** Generating keys, signing with the private key and verifying with the public key.

**EX077.** They reject unsigned scripts, and the signing key stays in the key service, used only on approved requests.

**EX078.** It derives the per-signature secret deterministically, avoiding the reused or leaked random values that exposed ECDSA keys.

**EX079.** It now offered TLS 1.3 but still accepted TLS 1.0, so the earlier change had been incomplete.

**EX080.** A developer had trusted it during testing and forgot to remove it.

**EX081.** Severity, evidence, the affected system and a recommended fix.

**EX082.** Pose as the portal to any patron whose connection they can intercept.

**EX083.** Unclear rules for contractors and the absence of secret scanning.

**EX084.** Secret scanning in repositories and generating keys on servers so people never handle them.

**EX085.** The patron portal certificate, with seventeen days remaining.

**EX086.** Its 397-day lifetime shows manual handling while the others use ninety days or less.

**EX087.** To make sure rotation has not left earlier backups impossible to decrypt.

**EX088.** It encrypts each export with a new symmetric key that is wrapped for the partner's public key, following RFC 9180.

**EX089.** The two tools defined the signed content differently.

**EX090.** By comparing key fingerprints in a face-to-face meeting.

**EX091.** Adversaries record encrypted traffic today hoping to decrypt it once large quantum computers exist.

**EX092.** Messages are lost if devices are lost, and shared librarian inboxes become difficult.

**EX093.** Complete basic controls such as inventory, automated renewal and backup encryption first.

**EX094.** A digital signature is a cryptographic mechanism; an electronic signature is a legal notion that can include simple marks such as typed names.

**EX095.** So the signature can still be validated after the signer's certificate has expired.

**EX096.** Because confusing controls push users toward unsafe workarounds.

**EX097.** Eighteen of thirty (60 percent) in the control group and nine of thirty (30 percent) with the explanation.

**EX098.** As an association with fewer staff proceeding in this simulation, rather than claiming it works.

**EX099.** Participants guessing the purpose, and the difference between a training site and real work pressure.

**EX100.** Several people use the same branch computer, so a device certificate cannot tell individuals apart.

**EX101.** Phishing resistance, staff effort, cost and recovery after loss.

**EX102.** A fall in security-key prices would make wider use of keys worthwhile.

**EX103.** Every certificate and key in scope has an owner in the inventory, and none expires without alerts thirty and seven days before.

**EX104.** Staff security keys and keys held by suppliers.

**EX105.** Adding a measure of false alerts.

**EX106.** To show that truly random word choices are stronger than phrases people pick.

**EX107.** She spent more time on password managers because participants valued it most.

**EX108.** She explained her role's limits, referred them to official recovery resources and never asked for their passwords.

**EX109.** It explains how the protocol works but provides no evidence about outage reduction.

**EX110.** They report results without methods and may have conflicts of interest.

**EX111.** That automation brings silent failure modes that need monitoring.

**EX112.** Two certificates on unusual ports were missed until those authorised ports were added.

**EX113.** A time-zone mistake, corrected by keeping all dates in UTC.

**EX114.** She logged it as a future enhancement, kept the agreed scope and made the design easy to extend.

**EX115.** Forty-two certificates, three of them previously unrecorded.

**EX116.** Because volunteers ignored alerts sent to their personal addresses.

**EX117.** One expiry was handled only after the seven-day reminder.

**EX118.** Plain-language outcomes: no certificate expiries since launch, three forgotten certificates discovered and an owner for every key.

**EX119.** It does not; it deals only with certificates and key metadata.

**EX120.** Operational issues such as inventories, ownership, communication and silent failures, more than mathematics.

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
