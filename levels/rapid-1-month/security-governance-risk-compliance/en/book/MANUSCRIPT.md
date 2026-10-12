# Security Governance, Risk and Compliance: A One-Month Practical Course

- Edition: working draft, 11 October 2026
- Language: English
- Course: rapid, one month
- Status: one of four subject-chapters drafted; five of fifty minimum exercises and their worked results drafted. The A4 page count has not been verified.
- Public-domain dedication for original text: [CC0 1.0](../../../../../LICENSE); [scope and exceptions](../../../../../RIGHTS.md)

## How to use this book

This course teaches a small security team to turn business priorities into a short, testable security strategy. Readers work with a fictional organization so that every exercise can be completed without access to a real company or its confidential records. The final product will be a one-page strategy, a prioritized action plan, and a compact measurement sheet. Readers may use the method for an actual organization only with permission to access its information.

This is the one principal English book for the rapid Security governance, risk and compliance course. It incorporates the earlier Security Strategy draft as its first chapter. Its [subject grade](../SUBJECTS.md) and [book plan](PLAN.md) define four chapters, one per subject. Each chapter will include its own examples and exercises; all worked results belong in the final appendix of this same book. This draft contains only the first chapter and five exercises. The chapter currently emphasizes strategy; governance, risk and compliance coverage still needs editorial expansion. The page target has not yet been validated.

<a id="ch-01"></a>

## Chapter 1 — Security governance, risk and compliance: foundations and decisions

### Learning outcomes

After this chapter, a reader should be able to distinguish a business objective from a security activity, explain how a risk scenario affects a service, identify who must own a decision, write a measurable security outcome, and test whether a proposed action belongs in a strategy.

### 1.1 The decision problem

A security strategy is a set of choices about what the organization will protect, why it matters, what level of disruption or loss it can tolerate, who can decide, and how progress will be checked. It has a time horizon and a resource limit. A list of controls, tools, or standards is useful evidence for a strategy, but the list alone does not explain which outcome matters first.

Consider two proposals: “Buy a new security platform” and “Restore the customer booking service within four hours after a destructive event.” The first is a possible activity. The second is a service outcome. The organization may eventually need a platform, backups, runbooks, training, or a different architecture to meet the outcome. The outcome provides a reason to compare those options. It also creates a test: a timed restoration exercise can show whether the promise is credible.

The [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) offers a useful language for this work. Its six functions are Govern, Identify, Protect, Detect, Respond, and Recover. A strategy uses all six, but Govern is where the organization sets expectations, responsibilities, and risk direction. NIST's [small-business quick-start resources](https://www.nist.gov/itl/smallbusinesscyber/nist-cybersecurity-framework-0) illustrate that a modest organization can begin with its own context and priorities rather than a large program copied from another company.

### 1.2 Start with a service, not a product

Security work has value because it protects a service, a duty, a person, or an asset that matters to the mission. Begin by naming the services in plain language. A payment processor may depend on card authorization, settlement, merchant access, and support. A clinic may depend on appointment booking, medical record access, and laboratory results. The same technology can support several services, and one service can cross multiple vendors and systems.

For each service, capture five facts: the owner, the people affected, the supporting systems and data, the maximum tolerable interruption, and the consequences of failure. The owner is the person accountable for choosing acceptable tradeoffs; the security team provides evidence and options. A credible owner can say whether a four-hour outage matters more than a delayed release, and can approve a recovery exercise that temporarily uses staff time.

Do not make the first inventory perfect. A first pass that names the most important services and unknown dependencies is more useful than a comprehensive spreadsheet whose entries have no owner. Record uncertainty as uncertainty. If the recovery time is guessed, label it as an assumption to validate with the service owner.

### 1.3 Translate a threat into a business scenario

“Ransomware” is a threat label. “The scheduling service is unavailable for two days because administrators cannot restore its database” is a risk scenario. The scenario can be tested against evidence: backup age, restoration time, separation of administrator accounts, and whether a manual scheduling process exists. It also has a business consequence: delayed service, staff overload, or contractual impact.

A compact scenario has four parts:

1. **Condition:** the event or weakness that could occur.
2. **Service:** the business process that would be affected.
3. **Consequence:** the kind of harm that would follow.
4. **Evidence gap:** what is not yet known well enough to decide.

For example: “If a compromised administrator account can delete both the live scheduling database and its backups, booking may stop beyond the four-hour target; the team has not run a full restore test this quarter.” The statement does not assert that compromise has happened. It links a plausible condition to a measurable service outcome and a testable gap.

Real incidents show why these distinctions matter. In its public reporting on the 2021 Colonial Pipeline ransomware event, the [U.S. Government Accountability Office](https://www.gao.gov/products/gao-21-105263) states that ransomware was deployed against the operator's business systems and discusses the subsequent pipeline security response. The strategic lesson here is an **inference**: business-system dependencies can affect operational decisions, so service mapping and continuity planning should not stop at the most visible technical system. This book does not infer the incident's detailed root cause from that source.

### 1.4 Choose outcomes that can be checked

A security outcome describes a state the organization wants to reach. It should have an owner, a date, a boundary, and evidence. “Improve monitoring” has no boundary or success test. “By the end of the quarter, every production identity provider and externally exposed application sends security events to the monitored log store, and a weekly coverage report identifies missing sources” can be checked.

An outcome need not guarantee that no incident will occur. Security teams cannot promise zero attacks or zero loss. They can set clear expectations about capability: detect a class of event within a defined time, restore a service within a tested window, review privileged access on a defined cadence, or resolve critical exposures according to an agreed risk rule. The measurement should use evidence collected during ordinary work rather than numbers invented for a presentation.

Useful measures combine **coverage**, **quality**, and **effect**. Coverage asks whether the target population is included. Quality asks whether a control works under a test. Effect asks whether the service outcome improved. For backups, these might be: percentage of critical services with protected copies; percentage of sampled restores that succeed; and measured time to restore a service. A high backup coverage number cannot substitute for a restore test.

### 1.5 Set priorities under a real limit

Most teams cannot do everything at once. A strategy therefore needs an explicit prioritization rule. Start with service criticality and exposure, then consider the evidence supporting the scenario, the time required to reduce risk, dependencies, and cost. Use consistent labels such as “act this month,” “plan this quarter,” and “accept for now with an owner and review date.” Avoid false precision: a score of 8.7 is not useful if nobody can explain how it was calculated or what decision changes at 8.7.

An action can be valuable even when it is small. Testing whether backups can be restored may cost less than buying a new tool and reveal the most consequential gap. Conversely, a visible security dashboard may be a poor early investment if no one owns the underlying alerts. Prioritization is a decision about **expected reduction of meaningful harm**, not a contest to deploy the most controls.

The strategy should name what is deferred and why. An approved deferral is not evidence that the risk disappeared. It records the tradeoff, the owner, the compensating measures, and the date on which the decision will be revisited. The separate [NIST Privacy Framework](https://www.nist.gov/privacy-framework) can help when the scenario concerns harms from processing personal data; privacy risk is broader than breach prevention.

### 1.6 A short working example

The fictional **Northstar Community Services** runs a public appointment portal, an internal case-management service, and a volunteer roster. Its executive team has one security engineer and limited budget for the next three months. The organization has no confirmed inventory of third-party integrations. Its most important service outcome is that appointments can continue during a system outage, even if the portal is temporarily unavailable.

A first strategy conversation might produce the following record:

| Decision item | First draft | Evidence to request |
|---|---|---|
| Priority service | Appointment scheduling | Service owner confirmation and dependency map |
| Tolerable interruption | Four hours | Front-desk staffing and manual process test |
| Leading scenario | Portal or database unavailable after account compromise | Identity access review and restore test |
| First outcome | Run one timed end-to-end restore and document the result within 30 days | Exercise log, timestamps, service-owner sign-off |
| Interim measure | Daily review of backup failures and privileged changes | Review log and alert routing |
| Decision owner | Operations director | Written acceptance of service target and resource use |

This is deliberately incomplete. The four-hour target is a working assumption until the operations director validates it. The dependency map may change the priority. The exercise may reveal that the manual process is more important than the technical restore. A strategy is allowed to change when evidence improves; the change should be recorded so that people understand why the decision moved.

### 1.7 The one-page strategy test

Before buying or building anything, try to write six sentences:

1. We must keep **this service** available or recoverable for **these people**.
2. The service owner accepts **this impact limit**.
3. Our leading evidence-backed scenarios are **these**.
4. This quarter we will deliver **these measurable outcomes**.
5. **These owners** will make the tradeoff decisions and perform the work.
6. We will review **these signals** on **this cadence** and revise the plan when evidence changes.

If any sentence is impossible to complete, the missing fact is the next research task. The purpose of the one-page test is not to hide complexity. It forces the team to show the relationship between mission, risk, action, and evidence before it expands into a long plan.

### Chapter 1 exercises

These five exercises are the first of the required minimum of fifty. Their worked results appear at the end of this draft. Use only the fictional Northstar Community Services case above.

### EX001 — Activity or outcome

Classify each statement as an activity or a measurable service outcome, then rewrite one activity as an outcome: (a) buy an endpoint security tool; (b) restore appointment scheduling from backup within four hours in a timed exercise; (c) write a phishing policy; (d) send an alert to an assigned reviewer within fifteen minutes of a privileged account change.

### EX002 — Scenario construction

Write a four-part risk scenario for the volunteer roster using condition, service, consequence, and evidence gap. State one assumption that needs confirmation. Do not claim that any breach has occurred.

### EX003 — Evidence selection

Northstar reports that “all critical services have backups.” Name three pieces of evidence that would test whether this supports its appointment continuity goal. Explain why a configuration screenshot alone is insufficient.

### EX004 — Priority decision

The team has one week. It can either (a) purchase a dashboard with no assigned alert owner or (b) run a timed restoration exercise with the operations director. Choose the first action and give two reasons. State one condition under which the other action might become appropriate later.

### EX005 — One-page strategy

Complete the six-sentence strategy test for Northstar. Mark at least two statements as assumptions or pending owner approval. Include one outcome with an owner, date, and evidence.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 plan →](PLAN.md#ch-02)

The next chapter is an outline, not yet an authored lesson.
<!-- cyberabc:chapter-navigation:end -->

## Sources for this chapter

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — framework functions and risk-management purpose.
- [NIST CSF 2.0 Small Business Quick Start](https://www.nist.gov/itl/smallbusinesscyber/nist-cybersecurity-framework-0) — starting a modest program in organizational context.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — privacy risk beyond security events.
- [U.S. GAO, Critical Infrastructure Protection: TSA Is Taking Steps to Address Some Pipeline Security Program Weaknesses](https://www.gao.gov/products/gao-21-105263) — public facts about the 2021 Colonial Pipeline incident.

All case details for Northstar Community Services are fictional. The strategic lesson drawn from the GAO report is explicitly identified as an inference.

## Final appendix — worked results and assessment notes

The completed book will gather the worked results for every chapter here. This draft contains the results for the first five exercises only.

### EX001 — Worked result

(a) and (c) are activities. (b) and (d) are measurable outcomes or operational targets, provided their scope and owners are defined. A stronger rewrite of (a) is: “By the end of month one, all managed staff laptops produce endpoint health and threat events visible to the assigned responder, and a sample alert reaches that responder within fifteen minutes.” This version states a population, time, evidence, and reviewer. A specific tool may be chosen later.

### EX002 — Worked result

“If an outdated volunteer account can access the roster after the volunteer leaves, personal contact details may be exposed, and Northstar has not completed an access review this quarter.” The condition is lingering access; the service is the volunteer roster; the consequence is exposure of contact data; the evidence gap is the missing review. The assumption is that departed volunteers currently retain access, which must be tested rather than stated as fact.

### EX003 — Worked result

Request a recent backup inventory for the appointment database, a restore-test log with timestamps and success criteria, and a dependency map showing whether identity, network, and application configuration can also be restored. A screenshot can show that a backup job is configured. It cannot show that a usable copy exists, that all dependencies are included, or that the service returns within four hours.

### EX004 — Worked result

Run the timed restoration exercise first. It directly tests the priority service outcome and produces evidence of the largest unknown. It also identifies dependencies that may guide later spending. A dashboard becomes appropriate when monitoring sources, alert definitions, review ownership, and action paths are defined; then the purchase can support a measurable detection target.

### EX005 — Worked result

One acceptable draft is: “We must keep appointment scheduling recoverable for clients and front-desk staff. The operations director is asked to confirm a four-hour interruption limit; it is currently an assumption. Our leading scenario is loss of the portal and database after an account compromise, pending access and dependency review. Within thirty days, the security engineer and operations director will run one end-to-end restore test and retain timestamps and a signed result. The operations director owns the service tradeoff, while the engineer owns the exercise. They will review backup failures daily and the strategy monthly, updating it after the restore test.” The answer earns credit for explicit owner approval, measurable evidence, and honest uncertainty rather than for using these exact words.
