# Chapter 04 expansion component — Preservation with provenance and explicit limitations

> **Editorial state:** Public integration draft for professional Chapter 04. This transient component is intended for the [single English manuscript](../MANUSCRIPT.md#ch-04), not a separate published book. EX016–EX020 and their identifiers are preserved; no independent review or A4 completion is claimed.
>
> **Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original exercises are subject to [CyberABC rights](../../../../../../RIGHTS.md); external publications retain their rights.

## Additional learning objectives

The learner can prepare a collection request that limits personal-data exposure, write a source-specific receipt rather than a reconstructed story, separate source integrity from analytic interpretation, reproduce a local SHA-256 check, and recognize why a timestamped screenshot is not an authoritative application record. The end product is a two-artifact evidence package for the synthetic Cedar Training Network (CTN) case.

## 1. Preservation begins with an answerable question

At the close of Chapter 03, the case has C08's statement that detailed IdP events for the relevant interval expire at 10:00 UTC. The analyst wants to know whether the summary for svc-enroll and session s-77 can be expanded into a scoped, reviewable source record. That question leads to a **bounded request**, not to a tenant-wide export. A useful request includes the event producer, precise interval, selectors, required fields, decision use, custodian, authorizing rule, storage destination, retention rationale and requested metadata receipt.

For CTN, a reasonable proposed selection is **svc-enroll, 08:50–09:05 UTC**. Expected fields include original event identifier, source timestamp and zone, account, session, client and authentication outcome, plus export or source-object identifiers where available. This proposal does not guarantee that all these fields exist or that the current analyst may see them. The identity custodian must decide whether policy permits the requested retrieval and which minimum subset answers the case question. If records have additional identity attributes, apply the local access, redaction and audit policy rather than opening them unnecessarily.

Think about two costs at once: the **cost of delay** before a stated expiry and the **cost of excessive collection**. A narrow source might disappear; a broad export can unnecessarily expose learner data, burden the reviewer, obscure what changed between copies and enlarge access risk. The correct response is not a universal "collect everything." The responder should be able to explain how the proposed source will discriminate between plausible explanations and how the selection can be independently inspected.

[NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) describes forensic collection, examination, analysis and reporting from an IT perspective. It expressly is not complete legal advice or a universal forensic procedure. [NIST SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) discusses log-management processes but predates modern cloud provider interfaces. Neither grants access to CTN or supplies missing collection metadata. A live process must follow management-approved policy and appropriate legal guidance.

## 2. Different states belong to different records

In the main fictional case, C08 was released at 09:14. At **09:16**, C09 now records an approval for the bounded identity request. At **09:18**, the case receives an IdP CSV described as covering 08:50–09:05. That chronological progression matters. A 09:14 request cannot be called "approved" because a later card will approve it; record the request and then append the approval as its own event. An approval does not mean the entire expected export metadata arrived.

C09 contains two visible rows: the first reports a successful 08:58 sign-in for svc-enroll, session s-77, client runner-03; the second reports a denied 08:59 event for svc-enroll, session s-78, client unknown. The case **does not supply** the original object identifier, exact export command, source-object digest or original byte count. It reports that a copy was received at 09:18; it does not demonstrate full source completeness. These omissions must stay visible.

At **09:22**, C10 enters the case as a support screenshot. Its display reads **11:21 UTC+02:00**, which conditionally translates to **09:21 UTC**. The case records receipt at 09:22. The capture device, local time proof, URL, login context and cache behavior remain unknown. The screenshot reports a displayed "unavailable" state, not a verified database row, not the time S42 changed, and not how many users were affected.

These are **separate evidence objects**. Do not write one combined receipt claiming that the screenshot validates the IdP export. They have different producers, acquisition paths, time semantics and decision uses. Their interpretations may later appear together in a timeline, but those interpretations are derived records with their own references.

## 3. Use a provenance model that can survive handoff

For each received object, track five layers:

1. **Source identity:** generating system, dataset, partition or source event ID where provided, plus stated event interval. An object named "export.csv" is not a globally unique source identity.
2. **Acquisition authorization:** approving role, policy or case reference, allowed scope and time. This is not the same as the copy's contents.
3. **Acquisition operation:** who performed it, selection query, tool/method, source version, export location and completion time. If unprovided, explicitly mark "not supplied."
4. **Received bytes:** received object reference, byte count and cryptographic digest **only if the actual bytes are available and measured**; handling/access records; and a preserved original separate from derivatives.
5. **Interpretive claim:** what the object supports, what it does not support, and what other source is needed to test a hypothesis.

At C09, layers one and two are partially described; the case does not give a complete layer three or four. A reviewer can say "the case received a CSV copy with these two readable rows," not "the complete IdP source was forensically preserved." That narrower sentence is both accurate and actionable: a custodian can be asked for a richer acquisition receipt or a fresh, authorized bounded copy before the stated expiry.

An **access history** is not an automatic proof of a lawful chain of custody. Recording who viewed an artifact and when improves reproducibility, but legal admissibility and retention obligations depend on jurisdiction and organizational requirements. This teaching exercise does not certify legal handling. Likewise, a SHA-256 digest identifies bytes under a computation; it does not authenticate the producer unless a trustworthy baseline and collection process link those bytes to the stated source.

Consider a sample manifest entry for C09:

| Field | Correct entry at 09:18 |
|---|---|
| Evidence reference | CTN-IR-014 / C09 copy |
| Described source | IdP detailed export, svc-enroll, 08:50–09:05 |
| Case approval | Recorded in C09 at 09:16 |
| Case copy receipt | 09:18 UTC |
| Visible contents | Two reported rows, sessions s-77 and s-78 |
| Original object/version | **Not supplied** |
| Original byte count and digest | **Not supplied** |
| Source query/method | **Not supplied** |
| Claim supported | Within supplied rows, s-77 is associated with client runner-03 |
| Claim not supported | Complete IdP history or a direct s-77 → q-144 link |

C10 requires a separate line: screenshot display time 11:21 +02:00, conditional 09:21 UTC; receipt 09:22; file identity and cache context unverified; supported claim restricted to the depicted UI. An analyst may propose obtaining the original image and support ticket metadata but may not silently record those as present.

## 4. Distinguish integrity, authenticity, completeness and relevance

These four qualities answer different questions.

**Byte integrity:** "Does this local byte sequence still match the reference digest?" A measured digest can answer this relative to the stated reference. It cannot answer whether the data were valid when produced.

**Source authenticity:** "Can we substantiate which producer emitted this event and the path through which this copy arrived?" This depends on collection records, producer validation, access control and sometimes signed outputs; a bare digest is insufficient.

**Completeness:** "Does the selected set cover the specified event interval and field scope?" Completeness may require producer counts, query semantics, paging checks, source-object versions or known-good control events. Two visible rows do not prove there were only two matching source events.

**Decision relevance:** "Will the record change a response decision?" A perfect byte copy of an irrelevant file may offer little value. C09 is relevant to the session/client question but still does not link s-77 to API request q-144. C10 is relevant to a reported user-facing symptom but does not establish authoritative slot state.

A defensible practitioner notes all four separately. Poor language collapses them: "Hash matched, therefore data genuine and case proven." Better language is "This payload's bytes match the published fixture digest; source provenance, full export scope and causal claims require other tests." When the baseline digest is missing, write "not tested," not "failed" and not "passed."

## 5. Offline byte-integrity exercise with executed output

The following local Python 3 fixture is **V4, not C09**. It uses exactly the classroom payload in the canonical manuscript and changes one ASCII byte in a working copy. No file, network, identity account or production log is touched.

~~~python
import hashlib

original = b"case=CTN-IR-014\nsource=idp-export\n"
modified = original.replace(b"idp-export", b"idp-Export")

print("C4|length", len(original), "SHA256", hashlib.sha256(original).hexdigest())
print("C4|mutated_length", len(modified), "SHA256", hashlib.sha256(modified).hexdigest())
print("C4|equal_digests", hashlib.sha256(original).digest() == hashlib.sha256(modified).digest())
~~~

**Output executed for this exact fixture:**

~~~text
C4|length 34 SHA256 1407e98f466990ff5aa4eee42cd30291826490e2c910ee57887824e6946136cc
C4|mutated_length 34 SHA256 c4ad3cfb2707356a80767e6555ce8c7ff92f7ef549d8f128468de23a1ce13e61
C4|equal_digests False
~~~

The change is lowercase "e" to uppercase "E" inside the source label: the byte count remains 34, yet the digest changes. This demonstrates why the number of bytes alone cannot detect alteration and why a digest comparison is specific to **exact bytes**. It does **not** prove that SHA-256 gives a truthful source provenance guarantee; cryptographic integrity and source authenticity remain separate properties.

A reproducing student should explicitly label: **input** is the 34-byte synthetic payload; **method** is SHA-256 over byte strings; **observed output** is the two digests and False comparison; **inference** is that these two byte strings differ; **non-inference** is that any CTN IdP source was verified. If a student writes the V4 digest into C09's missing object-digest field, the evidence record becomes false. This is a critical grading error despite the correct hash arithmetic.

For an additional negative control, compute the original digest twice without mutation: the values should match. Keep original and modified bytes separate, never "fix" an original artifact in place. If source bytes later become available, the correct workflow is to take an authorized read-only copy and record the actual digest and source identifiers of **that object**, not substitute the fixture.

## 6. Preserve image context and time semantics

A screenshot can corroborate what a user or tester saw on a display. It generally cannot prove which backend version produced the display unless the system also supplies validated request, response, cache and data records. A screenshot may show cached HTML, a delayed client state, a localization offset or a UI error without demonstrating a database mutation. These alternatives are **hypotheses**, not counterproof of the reported symptom.

For C10, calculate 11:21 − 02:00 = **09:21 UTC**, but retain the condition that the displayed offset is correct. The capture timestamp is not independently established. The 09:22 support receipt is a separate fact about the case workflow. Ask support to preserve the original image bytes rather than a cropped or re-encoded derivative, to retain the ticket text, and—if permitted—to document the device time settings and URL context. Do not request screenshots of real learner records for this classroom exercise.

A peer reviewer should be able to challenge a caption. "Screenshot proves S42 inaccessible at 09:21 UTC" overclaims both time and authoritative state. "Support provided a screenshot at 09:22 that displays S42 as unavailable, with clock reading 11:21 UTC+02:00 (conditional conversion 09:21 UTC), while cache and capture clock remain unverified" is traceable and honest.

## 7. Make a preservation queue based on reversible loss and decision value

At 09:22, **C08's stated 10:00 expiry** is the concrete time-sensitive issue. A high-value first follow-up is to have the already authorized identity custodian clarify C09's collection source, query/method, object version, byte count and digest if available, and preserve a documented narrow copy before the source window is lost. This addresses whether the detailed IdP data can support subsequent analysis. It does not prove that a complete copy exists now.

A second high-value request is an owner-approved **read-only authoritative S42 state and last-change check**, minimized to slot status, version/request ID and necessary timestamps. This can discriminate whether the reported display matches current backend state. An application or service custodian should select the safe permitted method; students should not query production directly. The two requests can proceed in parallel when separate custodians are available, but each needs its own approval and receipt.

Preservation priority should not be confused with action severity. Data may expire while the probability of a malicious actor remains low. Nor does an impending deadline authorize sharing protected raw records with any available analyst. The escalation may instead be "request supervisor and data-owner decision now; method unavailable until proper approval," which accurately documents a governance gap.

## 8. EX016–EX020: deeper practice and worked-answer supplements

**EX016 — Bounded collection request.** Objective: obtain decision-relevant session detail without unnecessary exposure. Input: C08's expiry statement plus C03/C05 identifiers. Deliver a request specifying svc-enroll, 08:50–09:05 UTC, source identity, relevant fields, identity custodian, approval gate, method/metadata request, deadline, minimum storage and use restriction. Model: record request at 09:14, with approval and completion **not yet present at that checkpoint**. Two points require explicit missing state and bounded selectors, not a full-tenant dump.

**EX017 — Two receipts.** Objective: document distinct evidence objects truthfully. Input: C09/C10. Create two manifest rows: C09 received 09:18 after 09:16 case approval, detailed source/bytes/digest incomplete; C10 received 09:22 with displayed conditional 09:21 UTC and unknown capture clock. Each must have a limitation and follow-up. The correct answer never assigns the V4 digest to C09. Two points require keeping source event, receipt and interpretation in separate fields.

**EX018 — Hash verification.** Objective: run and explain an exact integrity computation. Input: V4 original bytes and published SHA-256. Recompute 34 bytes and 1407e98f466990ff5aa4eee42cd30291826490e2c910ee57887824e6946136cc, then compare one-byte mutation as shown. Explain that equal original digests test local byte consistency, not the producer, completeness or C09 authenticity. A two-point answer includes the exact digest and two meaningful limits.

**EX019 — Timezone annotation.** Objective: distinguish display time from source receipt. Input: C10 "11:21 UTC+02:00", support receipt 09:22 UTC. Model output: conditional 09:21 UTC display, 09:22 separate receipt, no confirmed capture clock or authoritative state. Two points require explicit subtraction and a cache/context caveat. "Slot changed at 09:21" is unsupported.

**EX020 — Preservation queue.** Objective: prioritize by expected evidence loss and decision impact. Input: C08–C10. Model priority one: custodian-approved C09 metadata and complete bounded IdP preservation before 10:00, with object/version/digest/query receipt. Priority two: owner-approved minimal authoritative S42 state comparison to test C10's relevance. Either can be requested but neither is an already received result. The assessor looks for owner, scope, purpose, expected discriminator and remaining unknowns.

### Common mistakes and limits

- Replacing missing C09 acquisition fields with plausible defaults rather than labeling them unknown.
- Copying the local V4 digest into another object's manifest.
- Confusing a screenshot's display clock with the source event time.
- Presenting an analyst-created spreadsheet as an unchanged original.
- Claiming "complete" because a source yielded rows without checking paging, filters and query semantics.
- Ignoring privacy and source-expiry trade-offs when asking for broader access.
- Treating an evidence-handling worksheet as legal chain-of-custody certification.

### Sources and case provenance

- [NIST SP 800-86 (final 2006)](https://csrc.nist.gov/pubs/sp/800/86/final) provides historical IT-forensic principles and explicitly limits its legal role.
- [NIST SP 800-92 (final 2006)](https://csrc.nist.gov/pubs/sp/800/92/final) informs logging-process vocabulary; platform-specific collection details are **not** inferred from that guide.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) places collection decisions within risk-governed response. All C09/C10 fields and V4 bytes are fictional teaching artifacts, not provider records.

### Synthesis

Preservation is a contract among scope, authorization, method, received object and honest limitations. C09 provides valuable details but incomplete acquisition provenance; C10 provides an image of a symptom, not the authoritative S42 state. Chapter 05 may reason from these bounded observations only while preserving the gaps and the original time bases.

### Continue studying — Chapter 04 of 12 (integration draft)

[← Chapter 03](../MANUSCRIPT.md#ch-03) · [Chapter index](../../SUBJECTS.md) · [Canonical Chapter 04](../MANUSCRIPT.md#ch-04) · [Chapter 05 →](../MANUSCRIPT.md#ch-05)
