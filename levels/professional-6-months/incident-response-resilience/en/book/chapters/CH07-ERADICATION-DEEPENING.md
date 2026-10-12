# Chapter 07 supplementary teaching component — Causal linkage, persistence paths, and verification contracts

> **Editorial status: PUBLIC DRAFT — TRANSITORY COMPONENT, NOT AN ADDITIONAL CHAPTER.** Intended for integration into [Chapter 7 of the single English professional manuscript](../MANUSCRIPT.md#ch-07). It adds original instruction and supplements the existing EX031–EX035 and their worked answers without changing identifiers. All Cedar Training Network (CTN) cards and V-series branches are synthetic, not real-world findings.

**Author and editorial responsibility:** [hiagokinlevi](https://github.com/hiagokinlevi). Original text is covered only to the extent described in [RIGHTS.md](../../../../../../RIGHTS.md); referenced third-party works retain their own rights.

## Learning outcomes and chronological entry

The learner should (1) justify a mechanism claim by testing a chain of independently documented joins; (2) identify why a proven mechanism does not identify an actor; (3) decompose eradication into task, identity and service-dependency tracks; (4) create a verification contract with positive, negative and recurrence checks; (5) distinguish a short observation from a demonstrated durable result; and (6) defend EX031–EX035 using recorded approvals instead of assumed permissions.

**Initial decision time: 09:54 UTC.** The 09:46 C20 scheduler record has now been released. It names an unapproved task, sync-override, registered at 08:47 and run at 09:00, and records request q-144 against S42. A custodian verified the request-ID namespace linking C20, C05 and C13. At 09:46:30 C21 records *new* authority to extend the S42 hold until 10:07; the operator reports that extension at 09:46:45. C22 is a **separate retained configuration-audit record** released at 09:50: it reports an 08:52 recovery-method addition with a blank actor field. It is not a late acquisition of the expiring detailed sign-in record discussed earlier. C23's 09:54 inventory comparison says neither change is approved. At this initial checkpoint C24's later action and C25's identity remediation are unavailable.

### 7.A Proof of a mechanism requires a chain, not a matching word

A response analyst should separate three levels of explanation. **Correlation** says two events occupy similar time or share a label. **Operational mechanism** says a demonstrated component or workflow produced an identified outcome. **Human attribution** says a particular principal intentionally or accidentally caused that mechanism. These claims demand different evidence. The first may follow from time overlap; the second generally needs validated identifier semantics and producer records; the third may need additional identity, access, operator and authorization material.

For CTN, C12's self-reported batch-17 tag initially appeared to explain q-144. It was a field supplied by one event producer, not verified execution provenance. C14 later provided a custodian-confirmed complete manifest for **that approved run** containing q-140 and q-141 but not q-144. C20 provides the stronger causal link: its preserved task-run record identifies q-144, and a custodian verifies it is in the same request namespace as the application evidence. Therefore “sync-override issued the observed S42 edit” is supported more tightly than “batch-17 issued that edit.”

An analyst should still explicitly consider collision, transformation and time semantics. A request label is useful only after checking which subsystem generated it, its uniqueness domain, how it is propagated, whether transformations or retries reuse it, and whether the relevant records cover the same transaction. A label copied into a free-text field is not equivalent to a trusted transaction identifier. CTN's narrative supplies the custodian's namespace validation, but does **not** provide enough material to conclude that the task's registrant was a particular person or that the 08:52 recovery-method addition was made by the same actor. Those would be new hypotheses, not consequences of the join.

The course uses a **claim–source–scope–discriminator** record:
- **Claim:** sync-override's observed run generated the q-144 edit.
- **Source:** C20 scheduler run, C05 application request, C13 owner-approved state, and custodian's explicit ID-semantics check.
- **Scope:** this request and these observed records; not every runner or possible copy.
- **Discriminator:** a trusted contradictory namespace mapping, a mismatched application transaction, or an alternative producer record would force revision.

When a claim becomes better supported, **version it**; do not replace the earlier uncertainty with invented foreknowledge. The investigative record at 09:26 could not have cited C20. This discipline is consistent with the evidence-process orientation described by [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final). That 2006 guide supplies general forensic context, not an up-to-date vendor procedure or a legal conclusion.

### 7.B Inventory deviation, operational failure and malicious intent are different classifications

An **approved inventory** is a versioned statement about expected configuration. An **observed inventory** is what a particular source returned under a particular query at a particular time. Their difference can identify unapproved or unexpected objects; it cannot by itself classify motive. An inventory may be stale, exclude contractors or emergency work, cover only one environment, or fail to include dynamically generated tasks. Conversely, an observed list may be incomplete because the responder queried only runner-03. Treat a match as evidence within its declared scope and a mismatch as a question requiring owner review.

C23 records that the owners compared sync-override and the recovery-method change against their authoritative approval sources through 09:54. That supports the case's **unapproved change** designation. It does not imply a named intruder, privileged insider, intentional sabotage or a single campaign. The registration at 08:47 and method addition at 08:52 make a related sequence plausible, but adjacency alone cannot link their initiators. A person could have made both, two different people could have made them, or an automation or mistaken procedure could have introduced either. The supplied cards do not discriminate those alternatives.

Use a two-track matrix before discussing eradication:

| Track | Evidence-backed concern | Proposal that needs approval | Verification question | Residual gap |
|---|---|---|---|---|
| Scheduler task | C20 links a nonbaseline sync-override run to q-144; C23 finds no approval. | Preserve task configuration and run record; disable **this task**, not the runner fleet. | Is task disabled, has the next expected run been missed, and does batch-17 still work? | Re-registration, copied task, unknown author. |
| Identity recovery method | C22 reports an 08:52 addition; C23 has no approved change. | Identity owner assesses active state and authorizes scoped removal and associated credential/session handling. | Is the specific method gone, and do approved integrations still authenticate? | Blank actor, other methods, sessions and unobserved paths. |
| S42 temporary guard | C21 authorized an extension until 10:07; C19 had only one-route observation. | Continue only within that bounded authorization; re-evaluate cost before expiry. | Are unexpected writes observed and is legitimate service impact tolerable? | Alternate route coverage and post-expiry exposure. |

This approach avoids an attractive but unsafe shortcut: “disable svc-enroll so nothing can run.” Such an action might interrupt the approved batch-17 path, erase discrimination between suspect and healthy workflows, and exceed the specific authority supplied. Broader intervention may be appropriate with new evidence and explicit owner approval, but it cannot be smuggled into the narrower task decision.

### 7.C Preservation before modification, without creating a second evidence incident

There is a practical tension: the system may continue harmful actions while the team spends time preserving proof. Solve it with a **bounded preservation plan** that names essential sources, protected metadata, access approvals, collection time and stop conditions. The task definition, schedule, owner metadata, run record, request-ID mapping and current inventory version each answer a different question. Preserve sufficient material to assess the unexpected task later; do not request unrelated credential secrets merely to make the package appear comprehensive.

A change receipt and a collection receipt are also different. A collection receipt records **what was acquired**, from which custodian/source, under what authorization, when, in what form, and how its integrity or provenance was checked. A change receipt records **what was altered**, target identifier, configuration revision, operator, permission and observed result. If the team writes one sentence “evidence saved and task removed,” the reviewer cannot determine whether the preservation happened before modification or whether the content matches the prior state.

A cryptographic digest can detect unintended byte differences in a preserved artifact. It cannot guarantee that the source was complete, honestly produced or semantically correct. Similarly, recording “task disabled” as a state at 10:03 is not proof that a schedule will never execute anywhere again. An adequate observation design must include the expected next trigger interval, other schedulers in scope and a method to detect re-creation. CTN only supplies a short window through 10:07; those additional checks remain future work.

Eradication has an asymmetry: **confirming activity** may require one trustworthy positive event, while **asserting durable absence** requires a defined observation window and credible coverage of the relevant sources. A four-minute non-occurrence can be entirely expected if a job runs hourly. Do not calculate “success” by dividing zero observed executions by an unspecified exposure period.

### 7.D Verification contracts that can fail visibly

For each authorized change, state a falsifiable verification contract. A concise contract includes: starting hypothesis; preserved baseline; approval owner and exact target; operator and rollback; immediate positive condition; negative control proving legitimate behavior remains; observation period; independent source; and a **reopen trigger**. If the contract cannot be tested, revise the action plan instead of declaring success by inspection of a configuration flag.

At the **09:54 planning checkpoint**, the scheduler contract remains *proposed*: verify that sync-override is absent from active schedules after its approved disablement; check for no expected invocation in the relevant later window; confirm the approved batch-17 S40/S41 job retains its intended function; alert on task re-creation or renewed S42 requests; and preserve the pre-change task copy. A recovery-method contract remains a separate proposed identity-owner action. Positive method removal and negative integration testing must both succeed before an identity track can be described as addressed. Because the method may affect authentication dependencies, the identity owner also must coordinate with the service owner.

At 09:59, **C24 later supplies** authorization to disable sync-override only. At 10:03 the application operator reports that task disabled, a read-only status agrees, and no later run is observed **through 10:07**. This fills some previously pending contract fields. It does not fill the recurrence check or resolve C22. The approved account remains enabled, and the book does not present a real-system disablement command. In a professional case record, the remaining fields must retain the state *pending* rather than being colored successful merely because the immediate status looks correct.

At 10:06 the service owner weighs the remaining legitimate S42 cost and chooses not to extend the hold beyond C21's approved **10:07** expiry. Read-only S42 monitoring and escalation on a new unexpected edit replace the temporary guard. This is an explicitly documented risk choice. It is neither a hidden extension nor a claim that task recurrence and identity access are impossible.

### 7.E Correct and incorrect handoff decisions

**Correct 10:07 handoff:** “The preserved C20 run record and verified request semantics join sync-override to q-144. The owners classify the task and the distinct C22 recovery-method addition as unapproved changes; no supplied record identifies their author. C21 authorized the S42-only hold through 10:07. Under C24 the owners approved task-only disablement at 09:59, an operator reported it disabled at 10:03, and a status query plus short observation period supported that result. The hold was not extended after the 10:06 impact review. The identity-owner work and a complete recurrence/route assessment remain pending. Reopen/escalate immediately on an unexpected S42 write or task reappearance.” The handoff does not need an emotional label like “attacker neutralized”; it needs precise remaining work.

**Incorrect 10:07 handoff:** “We found the attacker at 08:47, removed persistence, revoked all access and verified the incident eradicated.” The available evidence never linked a human to registration; the recovery method remains unresolved; the narrow task disablement does not revoke the shared account; C19 covered only one route; and the observation window is too short for durable absence. A second error would be to say “we must keep the hold active indefinitely because the job was suspicious,” ignoring C21's deadline and the service owner's actual 10:06 decision.

In review, ask the author to replace each unbounded adjective—**all**, **fully**, **cleared**, **permanent**—with the source, exact scope, timestamp and check that would justify it. If those sources do not exist, record the qualified narrower claim. This is an exercise in measurable operational language, not in euphemism.

### 7.F Offline laboratory: identify inventory deltas without identifying people

**Objective:** reproduce a scoped approval-versus-observation comparison and state two limits. **Inputs:** two in-memory mappings of invented job-to-request associations. **Authorization and safety:** disconnected Python 3; no imported logs, no production tasks and no tenant changes. **Method:** calculate set differences; keep the declared source coverage and task identity separate from the verdict.

~~~python
approved = {"batch-17": {"q-140", "q-141"}}
observed = {
    "batch-17": {"q-140", "q-141"},
    "sync-override": {"q-144"},
}
print("C7 unexpected tasks:", sorted(set(observed) - set(approved)))
outside = set().union(*observed.values()) - set().union(*approved.values())
print("C7 outside approved:", sorted(outside))
~~~

**Executed output** (standard Python 3):

~~~text
C7 unexpected tasks: ['sync-override']
C7 outside approved: ['q-144']
~~~

The words **unexpected** and **outside approved** are labels relative to this fixture's baseline only. The program has no human-actor fields and therefore cannot infer registration intent, credential theft or a shared actor with C22. It also cannot determine whether the task exists on a runner not represented in the input. A safe extension is to add a fictional second approved run with a source/version annotation, rerun the comparison and explain how the classification changes without rewriting the preserved original input. Changing an approved baseline after seeing a suspicious row, with no record of who approved that change, would defeat the audit purpose.

**Failure injection:** remove the batch-17 entry from the observed mapping. The difference then indicates a missing approved task as well as the unexpected sync-override key, but it does not tell you whether the job actually vanished or the inventory collection was incomplete. The reviewer must request coverage metadata rather than launching a corrective disablement based on the set difference. The laboratory tests reasoning over finite sets; it is not an endpoint detection rule.

### 7.G Extensions to EX031–EX035 and worked-answer rationale

These supplements correspond exactly to the pre-existing IDs. No new IDs, assignments or renumbering are introduced.

**EX031 — claim-chain extension.** Require the learner to write a separate **identifier-validity test** and **actor-attribution test**. Model reasoning: C20 plus verified q-144 namespace strengthens the task-to-edit mechanism; C14 rules out q-144 as part of the particular approved batch-17 manifest; C12's self-described tag is therefore weak. Neither C20 nor the blank-actor C22 log identifies who registered the task or changed the recovery method, and s-77 is not directly joined to the task registration. Award full credit only when “known mechanism” and “unknown actor” coexist explicitly.

**EX032 — dual-contract extension.** Add a line identifying the *source that could show recurrence*. Scheduler: preserved C20 baseline, approved task-only change needed, positive status disabled, negative batch-17 functioning, future registration/run monitor; all execution fields blank at 09:54. Identity: C22 configuration-audit baseline, identity-owner approval required, positive method-state check, negative approved integration functioning, follow-up on method re-addition or unexplained sessions. A completed answer separates the method's observation from proof of active exploitability and avoids assuming one operator for both changes.

**EX033 — hold chronology extension.** The learner should distinguish **authorization expiry** from **process risk**. C17 approves until 09:47; C21 separately authorizes an extension at 09:46:30 through 10:07 and the operator reports its configuration at 09:46:45. C24 later gives task-only approval at 09:59, execution at 10:03, 10:06 cost review and expiry at 10:07. After the hold ends, monitoring and escalation operate under a new risk choice, not under a silently extended hold. Mark down any answer that assigns C21's authorization to C16 or describes indefinite coverage.

**EX034 — manifest extension.** The executed fixture above yields precisely one unexpected task, sync-override, and one out-of-baseline request, q-144. To earn the full result, explain **two different uncertainties**: inventory coverage may omit other runners, and baseline comparison cannot infer human intent even if coverage is complete. A deeper review should ask whether both maps describe the same time span and identifier namespace. The string output is not independently sourced CTN evidence; C20/C14 provide the fictional scenario's relevant provenance.

**EX035 — handoff extension.** Preserve the C20 task and run record, C22 configuration audit, C23 inventory versions, C21 authorization and C24 action/status evidence. State “task disabled at 10:03 and no further run observed through 10:07” rather than “persistence removed”; explicitly assign the recovery-method work to the identity owner, describe the S42 monitoring trigger and avoid naming an attacker. The outcome rubric should assess whether another responder can distinguish **approved**, **performed**, **observed** and **still required** without outside conversation.

### Operational limits, references, and synthesis

A local inventory comparison cannot establish the completeness of records, the origins of a task, or the identity of a human. Short monitoring does not prove permanent absence. The organization must choose evidence handling, retention and authorized change rules in its own context. [NIST SP 800-61 Revision 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) offers an organizational risk-management context for coordinated response. [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) discusses forensic process and expressly is not legal advice. [CISA's federal response playbook publication](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/2fc7609) is an example of documented response workflow, not a requirement to use the fictional CTN procedure.

**Synthesis:** the q-144 mechanism can be well supported while actor attribution and persistence removal remain open. Eradication is not a noun that an analyst can award after one configuration change. It is a versioned set of approvals, specific actions, independent observations, negative controls and assigned recurrence checks, linked to the handoff needed for Chapter 8's data and service recovery.

### Continue studying — supplementary component for chapter 07 of 12

[← Chapter 06 (authored draft)](../MANUSCRIPT.md#ch-06) · [Course chapter index](../../SUBJECTS.md) · [Chapter 08 (authored draft) →](../MANUSCRIPT.md#ch-08)

Return to the [principal Chapter 07](../MANUSCRIPT.md#ch-07) for the existing EX031–EX035 prompts and to the [single worked-answer appendix](../MANUSCRIPT.md#worked-answers) for the current canonical answer order.
