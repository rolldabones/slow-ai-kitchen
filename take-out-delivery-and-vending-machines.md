# TAKE-OUT, DELIVERY & VENDING MACHINES

### Governed Delegation for AI Agents

*Who may use the service, what may it do and who owns the result?*

| Version | Date | Status | License |
|---|---|---|---|
| v1.0.0 | 2026-09-07 (KST) | Final manuscript | CC BY-NC-SA 4.0 |

## Contents

- [The order travels](#the-order-travels)
- [Decide what is being delegated](#decide-what-is-being-delegated)
- [Specify the delivery](#specify-the-delivery)
- [Keep the vending machine fit for use](#keep-the-vending-machine-fit-for-use)
- [Write the ticket](#write-the-ticket)
- [Test what travels](#test-what-travels)
- [Stop, reconcile and hand back](#stop-reconcile-and-hand-back)
- [A worked order: investigate stalled onboarding](#a-worked-order-investigate-stalled-onboarding)
- [Before another order](#before-another-order)

## The order travels

The kitchen's work can leave the counter in several ways. With take-out, someone collects the order and carries it onward. With delivery, the kitchen arranges its journey to a destination. A food vending machine offers pickup at another location, often with no kitchen staff nearby. The menu remains available after the people who prepared or stocked it have left.

AI agents create similar distances from direct supervision. Given an objective, an agent may choose intermediate steps, use tools and act on what it finds. A deployed service may do this repeatedly for users far from the team that built it. Its value depends on carrying useful work forward while keeping authority within the limits humans set.

The analogy describes three service patterns:

- **Take-out:** the agent prepares work for a human to collect, review and carry into use: an analysis, draft or proposed change set.
- **Delivery:** the agent is also authorized to carry released work to a specified destination and perform specified actions there: send the approved message, apply the approved change or hand work to an authorized receiving workflow.
- **Vending machines:** a bounded service is available for repeated use at distributed points of access. Users select from an approved menu and collect the result, through a branch portal, shared application or other authorized interface.

The patterns can combine. A distributed service may return work for human collection or initiate authorized delivery. They introduce no new risk tiers and confer no additional authority. Each remains subject to preparation, verification, human release and ownership through reliance. The practical question is **what may happen between human checkpoints?**

Use this companion to write a **service ticket**, test its controls and reconcile a **service receipt**. The [worked example](#a-worked-order-investigate-stalled-onboarding) follows an investigation into delivery, then considers making that service available at several branches.

**Scope.** This module adds operating instruments. It changes no step, gate, tier, role or principle. The [README](./README.md) controls on method and [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) on doctrine. [Newton's Kitchen](./newtons-kitchen.md) supplies the conceptual foundation and defines agents broadly, including systems whose advice people act on. This companion concentrates on agents that use tools across multiple steps.

---

## Decide what is being delegated

Use an agent when the next useful step depends on what the previous step reveals: following a source reference, investigating a discrepancy or deciding which permitted evidence to inspect next. A fixed sequence may be better served by an ordinary workflow. A single task can contain both: adaptive investigation followed by tightly specified execution.

Write the boundary as actions on particular resources. “Help with customer onboarding” is too broad to govern. “Read these case files and receipt logs; investigate missing-document discrepancies; prepare sourced follow-ups; hold all sending for release” gives the team something to authorize and test.

| The agent | The execution system | The human |
|---|---|---|
| Selects intermediate steps, uses permitted tools, prepares outputs and requests authorized actions. | Enforces access to tools, records and destinations; applicable approval; time, cost and action limits. | Sets purpose, acceptance criteria and authority; decides consequential release and confirms material outcomes. |

A tool's presence does not authorize every use of it. Keep the existing decisions distinct:

- **Step 10, Gate 8:** authorize the system for specified organizational uses.
- **Step 5, Gate 4:** use AI within the authorized purpose, authority, boundaries and exit.
- **Steps 8–9, Gates 6–7:** verify the deliverable and make the human release decision before consequential reliance or execution.

Steps 1–4 still precede AI: frame the task, set the Definition of Done (DoD), perform the human manual first pass and examine the context. Name the Owner in the initial specification; Step 6 confirms that ownership, as the [Consultant Workbook](./consultant-workbook.md#the-task-method-and-its-evidence) explains.

**Approval can cover a verified batch.** Identify its exact targets, content, permitted effects and validity conditions. Routine execution within that approval need not return for a decision at every tool call. New proposals must fit the approved scope. Material changes to content, recipients or relevant source conditions return for review.

Newton's Kitchen requires human confirmation of material outcomes against criteria set in advance. A completion summary cannot supply missing prior authority.

**Apply the README's tiers.** Automation tied to action is Tier 3: full method, distinct human Reviewer, Approver and Owner, second review, sign-off, escalation and a remediation or rollback plan. Drafting-only work follows its actual stakes. Count consequences across related agents and runs; splitting work does not lower its aggregate impact.

---

## Specify the delivery

Authorize the destination together with what arrival may cause. An address may identify a person, account, application record or receiving workflow. Placing a file in a watched folder can start another process. The ticket must cover that effect as well as the write.

Delivery may begin on an approved schedule or event while authorization remains valid. Define the trigger, permitted frequency, limits and expiry. A useful discovery does not authorize another recipient or a larger mission.

Define the required evidence of completion before dispatch:

| Evidence | What it establishes |
|---|---|
| The service accepted the request. | Dispatch was accepted. Arrival or successful execution still needs evidence. |
| The specified destination received the approved item, or the approved change is visible there. | Receipt or the specified effect is verified to the extent supported by the record. |
| The recipient acknowledged it, or a required downstream result was verified. | The additional outcome is evidenced, where the DoD requires it. |

Choose the evidence appropriate to the task. Human confirmation of material outcomes remains the Owner's recorded judgment against the DoD. Receipt, acknowledgment and confirmation are distinct; none grants authority for further action.

---

## Keep the vending machine fit for use

Vending adds continuing availability at a distance. Its governance must remain effective across locations, users and time. The point of access may be a physical kiosk, a branch application or a shared interface; remoteness is also distance from the people who designed and authorized the service.

The analogy has a limit. Many food vending machines dispense a finished product. An AI service may generate a new result for every request. **Approval of the service and its menu does not verify each generated result.**

Apply the existing Feast and [Your Restaurant](./README.md#addendum-your-restaurant) controls to the service:

| What must be maintained | What the operating record establishes |
|---|---|
| **Menu and access** | Permitted tasks, intended users, task tiers and prohibited uses. Each request is checked against the caller's current access and the specific records it needs. A visible menu is not permission to use every item. |
| **Sources and versions** | Approved source, model, instruction and tool versions; freshness requirements; review dates; changes requiring revalidation. Stale or unverified items are held or withdrawn. |
| **Ownership and coverage** | The organizational AI Owner is accountable for the service. Each task has a named human Owner with decision rights, oversight and intervention power. Reviewers, operators and escalation coverage are available when required. |
| **All active locations** | An inventory of interfaces and running instances, their configurations and permissions, and limits on total workload, spending and reach. Opening another instance does not reset shared limits. |
| **Intervention and withdrawal** | Tested suspension across affected locations, queues and delegated work, with a manual fallback and a record of operations already in flight. Previously released outputs remain traceable for correction and follow-up. |

A standing authorization can cover repeated, specified operations while its conditions remain valid. Each run references that authorization and records the requester, task scope, applicable versions and Owner. A menu selection starts work only within those bounds.

The task gates still apply. Each new task needs its human-defined criteria, relevant context check and human first pass at the required tier. Reusable preparation may support a task when checked for applicability; a pilot's sample cases cannot supply human judgment on unknown future cases. A specifically prepared batch is different from an open-ended stream of requests.

Newly generated work still passes the required verification and human release before reliance. Repeated collection of an unchanged, previously released item is governed by its approved audience, purpose and validity conditions. A change in use or evidence can require renewed review. The service should make these conditions visible where users collect the result.

---

## Write the ticket

Keep one authoritative task record. Link existing briefs, evidence and workbook sheets instead of copying them. For a reusable service, reference the current registry and service authorization, then record the details of this run. The four headings below are the four elements of Informed Intent. Complete preparation authorization before starting; attach the release record before enabling the actions it covers.

```markdown
# Service ticket
ID / version / task tier:
Requester / service and instance IDs, if applicable:
Task brief, DoD, human first pass and context-map references:
Tool-registry entry / system and configuration version:

## Purpose
Objective, intended use and observable completion criteria:
Delivery outcome and required evidence of receipt or effect, if applicable:
Material outcomes, threshold and basis; human who authorized that threshold:

## Authority
Authorizer / institutional authority / date:
Owner / decision rights / oversight / intervention power:
Builder or AI Operator / Reviewer / Approver / escalation contact:
Evidence of the authorizer's five Informed Intent conditions:

## Boundaries
Permitted actions, sources, accounts, targets and data uses:
Approved menu item / requester access / source currency requirements:
Delivery recipient/system, channel, approved item/version and effects on arrival:
Prohibited actions and destinations:
Human release checkpoints / evidence / approved action-set version:
Conditions invalidating approval:
Total time, cost, actions, retries and concurrency limits:
Scheduled/event triggers, frequency and shared limits, if applicable:
Subagents and memory: permitted scope, retention and shared limits:
Enforcing controls and test-evidence references:

## Exit
Expiry / stop or hold triggers / what work must stop:
Responder, response time and tested intervention path:
Queued and in-flight work / uncertain outcomes / recovery plan:
Failed, refused, late or misdirected delivery: authorized response and human responsible:
Who may resume, under what conditions:
Evidence location, access, retention and Service Record deadline:
```

Under [Informed Intent](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#2-informed-intent), the authorizer must have **Knowledge, Evidence, Authority, Time and Permission**: understanding of the specific action; evidence of tests, residual risk, dissent and alternatives; current institutional authority; time to consider; and freedom to decline without retaliation. A filled form does not establish those conditions by itself.

Set materiality in advance with regard to affected people and cumulative consequences. Record unresolved limits as unresolved. They grant no additional permission.

---

## Test what travels

Apply Newton's four properties to the actual system.

| Property | Evidence required before live execution |
|---|---|
| **Bounded** | An out-of-scope target or action is denied by access controls; expired or invalidated approval cannot be used; limits cover the whole run. |
| **Observable** | A run ID joins the ticket, source versions, human decisions and tool events, including blocked actions and partial failures. |
| **Interruptible** | A trial demonstrates stopping new dispatch and delegated work, identifies operations already in flight and measures intervention time. |
| **Attributable** | The named Owner has decision rights, access to the record and practical power to intervene. |

The Owner must also be able to explain a material outcome in terms an affected person can use. Logs support that account; they do not supply judgment for it.

**Put restrictions where actions occur.** Prompts instruct the agent. Access controls and the receiving system enforce permissions. At execution, check that the requested action matches its release record and that relevant preconditions still hold. If a material change could occur between checking and acting, use a conditional operation that rejects changed state, or hold for a controlled human procedure. Merely telling an agent to recheck is insufficient evidence of enforcement.

**Keep encountered content separate from authority.** Documents, emails, tool results and other agents' messages cannot grant new permissions. Test an input that asks the agent to send records to an unauthorized address. The destination should remain inaccessible. Read access also needs boundaries: information can be disclosed through model inputs, exports, logs or memory without changing its source record. Retain only needed evidence, with protected source references where appropriate.

**Keep delegation within the ticket.** Subagents receive the parent run ID, a narrower assignment, necessary source references, permissions, remaining limits and exit conditions. Budget, concurrency and action limits include every child. Expiry and stopping propagate to child work. Agent criticism may inform review; it cannot occupy the method's human Reviewer role.

For delivery to another system or agent, carry the output version, intended use and provenance; link the receiving workflow's authorization and evidence of receipt. Identify who can intervene after the handoff. The payload cannot grant the receiver permissions, and handing it over does not end the sending Owner's accountability for the originating outcome through reliance.

Preserve source evidence, agent inferences and human judgments as distinguishable records. This applies [Return to Source and Cognitive Provenance](./coetzees-kitchen.md) to handoffs. Memory retained from a prior session is context to check, not continuing authority. Validate the current ticket and permissions on resumption.

Implementation detail is already available in the Primer's [access controls](./primer/05-part-4-governance-by-design.md#least-privilege-for-agents) and [agent traces](./primer/04-part-3-integration-engineering.md#what-a-trace-of-an-agent-run-must-contain).

---

## Stop, reconcile and hand back

Specify whether an exception blocks one case or the entire run. A conflicting source may hold one independent case; loss of required logging may stop every action. Continuing unaffected work is permissible only where the ticket allows it and the dependency is understood.

When a stop is triggered:

1. **Contain.** Halt affected dispatch, queued operations and child work. Identify requests already accepted by another system; stopping the agent may not cancel them.
2. **Preserve and alert.** Retain the authorization, approvals, events and last known state. Notify the named responder through the tested path.
3. **Reconcile.** Inspect the affected system. Separate confirmed success, confirmed failure, unknown outcome and work not attempted. A timeout does not prove failure.
4. **Recover.** Apply the authorized fallback or remediation. Before retrying an uncertain action, establish whether its effect occurred. Where supported, reuse the same idempotency key so the receiving system recognizes retries of that action; follow its rules for key scope and expiry. A failed or refused delivery does not authorize an alternate recipient or channel. Use only an approved fallback; otherwise hold and escalate. Sending or disclosure may require remediation because they cannot be undone.
5. **Hand back.** The designated human records whether work may resume. Changed scope or expired authority requires reauthorization; changed material content or preconditions requires renewed verification and release.

Test the sequence using the workbook's [stop and fallback exercise](./consultant-workbook.md#w21-stop-and-fallback-exercise). The Primer explains [why an uncertain action must not be blindly retried](./primer/04-part-3-integration-engineering.md#never-retry-a-non-idempotent-action-blindly).

The **service receipt** is the run record below. “Evidence” means records from the source or affected system, checked independently of the agent's completion claim. Record downstream work already triggered; stopping the sender may not stop the receiver.

```markdown
# Service receipt
Run / requester / service and instance / ticket version / release record / system version:
Start, stop and completion times / actual spend and limits used:

| Action ID | Target and approved version | Attempts | Observed state | Evidence | Follow-up |
|---|---|---|---|---|---|

Approved actions: successful + failed + unknown + not attempted = total.
Record every attempt, retry and blocked request separately.
Sources checked / exceptions / unresolved uncertainty:
Required delivery outcome / actual receipt, acknowledgment or downstream effects:
Owner decision: confirm / refuse / amend and confirm; criteria and evidence:
Remediation owner / due date / Service Record / ownership through reliance:
```

Count success against the required outcome, using the delivery evidence specified in the ticket. Preserve unknown states until resolved; they are not an additional human confirmation outcome or permission to rely.

The receipt feeds the existing [Service Record](./service-record.md), required for Tier 3 and written by the Owner within one day of release. It records judgment and learning, including open remediation. Ownership continues through reliance.

---

## A worked order: investigate stalled onboarding

*Fictional teaching case, 7 September 2026 (KST). All people, identifiers, addresses, evidence records and test results below are illustrative.*

**The Dish.** Investigate four stalled cases and prepare justified missing-document follow-ups. The next lookup depends on discrepancies between the case file, upload log and approved policy. The investigation pack is the take-out deliverable; the authorized sending is delivery. The agent investigates and prepares proposals; a restricted sending service executes the released messages. Its value is assessed against the existing workflow's quality and total effort.

**Done Means.** D1 sets six checks:

- Every finding traces to current evidence.
- Each recipient and missing-document request is verified; contradictory cases are held.
- Only released messages are sent while their approval conditions hold.
- Delivery success requires evidence of arrival at the specified recipient mailbox.
- Every attempted action has a reconciled state; unknown outcomes block confirmation of completion.
- The Owner records the material-outcome decision and any required follow-up.

The fictional service is assumed to provide mailbox-arrival evidence; acceptance of a dispatch request is insufficient. Reading or replying is outside this run's completion criteria.

**Prep by Hand.** Jo, the Preparer and AI Operator, reads Missing Documents Policy v4, examines two representative cases and draws the source-checking sequence and exception rules. The team retains that work as H1 and records the DoD and affected-customer risks in D1. Organizational authorization and trained operators are in place under Steps 10–11.

**The completed ticket.**

| Field | Ticket T1, version 1 — Kitchen Tier 3 |
|---|---|
| Purpose | Investigate C17–C20 against D1; prepare follow-ups. Each proposed customer communication is material. Elena Park records that threshold and its basis in D1. |
| Authority | Arun Patel, operations director, authorizes the run at 13:35. AUTH1 records current authority and all five Informed Intent conditions. Elena Park is Owner, with oversight and stop power; Jo Kim is AI Operator; Mira Cho is Reviewer; Arun performs second review and is Approver. |
| Sources and tools | Registered configuration R1: read C17–C20, their upload-log entries and Policy v4; write to the restricted draft area. No other customer records, external search or account-status changes. |
| Release | Sending is disabled during preparation. S1 identifies exact messages, recipients, the registered customer-service sender and expected source versions. After S1 is released, R1 enforces source-condition validation and commits dispatch as one conditional operation: a mismatch commits no send. |
| Delivery | Email only to the recipients in S1. Record service evidence of arrival at each specified mailbox. No alternate address, second channel, response-chasing or downstream account action is authorized. |
| Limits | Twenty minutes of investigation; at most 20 source lookups and USD 3 total; at most three sends, one in flight at a time; no automatic retries, subagents or persistent memory. |
| Exit | Release expires at 14:30 KST on 7 September 2026. A source conflict holds its case. An unknown send or lost logging stops all dispatch. Jo receives the alert and responds within five minutes; Elena is the fallback. Elena authorizes resumption after reconciliation, with renewed review when approval conditions change. |
| Control evidence | TEST1 records denial of an unauthorized destination and a concurrent source update at the conditional-dispatch boundary; TEST2 records a stop within two seconds and identification of work in flight. R1 blocks dispatch when logging fails. |
| Records | Restricted case evidence folder E1, retained under the organization's applicable schedule; Owner completes the Service Record within one day of release. |

**Bring in AI.** C17's case file says Form A is missing. The agent follows the discrepancy to the permitted upload log, finds a later receipt and checks its link to C17. It proposes no reminder and cites both records. That branch was selected from the evidence; the human verifies the finding. C18–C20 produce supported missing-document proposals. The agent cannot change eligibility or account status.

With take-out alone, the team would collect and verify that pack, then carry any released communications into use itself. This ticket also requests delivery, so sending requires the release below.

**Plate and Taste.** Mira verifies the four findings and source versions. Arun completes second review and releases the following three messages as S1 at 14:00 KST. Elena confirms the prepared output against D1's preparation criteria; delivery completion remains unconfirmed. The addresses below are deliberately non-deliverable examples.

| Action | Recipient | Exact approved message | Required source state |
|---|---|---|---|
| A1 | c18@example.invalid | Please upload your signed Form A through the customer portal. | C18 v7: Form A missing; current contact permitted. |
| A2 | c19@example.invalid | Please upload your signed Form B through the customer portal. | C19 v3: Form B missing; current contact permitted. |
| A3 | c20@example.invalid | Please upload your signed Form C through the customer portal. | C20 v5: Form C missing; current contact permitted. |

R1 permits only these recipient-and-message pairs under S1. A changed source version is rejected for human review; the agent cannot edit the batch to make it pass.

**Deliver and verify.** In the simulated run, the service reports A1's arrival at the specified mailbox. A2 times out. Dispatch stops before A3. The initial receipt is:

**Receipt RC1:** run RUN1; ticket T1 v1; configuration R1; release S1; evidence folder E1. Investigation ran 13:40–13:53 KST; dispatch stopped at 14:02. Actual use: nine source lookups, two send attempts, USD 0.38 total. No retries or delegated work.

| Action | Attempts | Observed state | Evidence | Follow-up |
|---|---|---|---|---|
| A1 | 1 | Mailbox arrival confirmed | Messaging-service event M1, matched to S1's recipient and message | D1 delivery criterion met; reading or reply unverified and not required. |
| A2 | 1 | Unknown | Request M2; timeout; no delivery determination | Jo checks M2 in the messaging service before any retry. |
| A3 | 0 | Not attempted | Queue Q1 stopped | Recheck S1 and current source conditions before resumption. |

**Three approved = one successful + zero confirmed failed + one unknown + one not attempted.**

While Jo investigates M2, C20 uploads Form C and its record becomes v6. S1 no longer permits A3. Its receipt state becomes **not attempted — withdrawn after source change**. The original three approved actions stay in the record; the agent cannot use the old approval. A2 remains held until its state is established. Updates preserve the initial stop record.

At 14:07 Elena **refuses confirmation of the batch as complete** against D1, records A1's verified result and assigns Jo the unresolved A2 investigation, due for escalation by 14:20. Jo may investigate M2; switching to a personal address or another channel requires new authority. RC1 retains the decision and the open follow-up. The Service Record captures the effective stop and the incomplete delivery result separately. A successful intervention does not make an unfinished task complete.

---

## Before another order

### The same service at three branches

After a separate organizational deployment decision, the investigation capability becomes a menu item at three branch portals. This is the vending-machine pattern: staff collect assistance where they work, away from the team maintaining the service. Sending retains its human release checkpoint.

The service checks each requester and restricts retrieval to that person's authorized cases. Each run links its own task preparation, current service authorization and named Owner. A request for another branch's records is denied. Merely seeing the menu does not make those records accessible.

Policy v5 later takes effect and invalidates the v4 procedure. The AI Owner suspends the affected menu item at all three branches, including instances still using cached v4 instructions. New requests wait for the revised procedure to be tested and authorized. Previously dispatched messages and already released analyses remain in the evidence record; their task Owners assess whether correction or follow-up is needed. Taking the service out of use does not erase earlier reliance.

### Keep the service in review

Organizational deployment invokes Steps 10–12 at every task tier. Register the service, staff its operation and maintain the review cycle. Continuing availability connects this companion to the Restaurant's five pillars: governance, risk management, regulatory compliance, lifecycle management and continuous improvement.

Size concurrent work to the team's capacity to inspect exceptions and intervene. Measure usable results together with preparation, review, rework and recovery effort, following the [Consultant Workbook](./consultant-workbook.md). Ten Service Records trigger the existing method review.

Take-out governs what a human collects. Delivery governs what the system carries onward. Vending machines extend that discipline to repeated use at a distance. In every case, the service must remain bounded, the result must be checked and a named human must own its consequences.

**Final Liability rests with the Human.**

---

## Source basis and attribution

Prepared against README v2.8.0 at repository commit [`7869f35`](https://github.com/rolldabones/slow-ai-kitchen/tree/7869f35f283f32c4ace2fd6c5e5780e8a4736319) and DOCTRINE.md v1.1.1, reviewed on 7 September 2026 (KST).

This companion adapts Slow AI Kitchen by Son-U Michael Paik, GRC Solutions Korea. It adds the three service patterns, ticket, receipt and fictional teaching examples. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/); see [LICENSE](./LICENSE). Accountability language follows the repository's governance doctrine; this module does not allocate legal liability in any jurisdiction.
