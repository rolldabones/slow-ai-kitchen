# LEAN AI

### Governing the Cost of Useful Intelligence

*Waste less. Keep what makes the work worth relying on.*

*An operating module of Slow AI Kitchen, for the business owner, the architect and the finance reviewer who must show what one accepted outcome costs, what that cost depends on and whether the service survives a narrower or dearer choice of models. It connects the measurement instruments the Kitchen already has. It replaces none of them.*

**Son-U Michael Paik**
CEO, GRC Solutions Korea
[www.grcskorea.com](http://www.grcskorea.com)

| Version | Date | Status | License |
|---|---|---|---|
| v0.2.0 | 2026-11-25 (KST) | WIP (work in progress): documentary and retrospective checks only, no enterprise pilot run | CC BY-NC-SA 4.0 |

**Final Liability rests with the Human.**

> **Status: WIP.** This module is a work in progress, first issued at v0.1.0 and open to revision. The documentary and retrospective checks described in [What the present evidence establishes](#9-what-the-present-evidence-establishes) were completed and rerun on 15 November 2026 (KST). No enterprise pilot has been run, and no saving is established. A savings claim needs a pilot run under [lean-ai/pilot-protocol.md](./lean-ai/pilot-protocol.md) and reported whatever its result. At v0.1.1, 17 November 2026 (KST), and at v0.2.0, 25 November 2026 (KST), this status is unchanged.

> **Scope note.** This module adds an economic operating practice to the Kitchen. It adds no doctrine, step, gate, tier, role or rule. The [doctrine canon](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) governs, and where a formulation below and DOCTRINE.md differ, DOCTRINE.md controls. No claim of novelty or of exclusive ownership of the term "Lean AI" is made.

> **Link currency.** The three policy sources under [Sources](#sources-and-integration-references) were read on 15 November 2026 (KST), and the help article [V1] on 25 November 2026 (KST). All other links are internal to the account.

**Amendment, 17 November 2026 (KST), v0.1.1.** Sources and integration references gains one line, a pointer to the working paper *The Boundary and the Limit* in AI-Governance-Academy, which sets out the theory behind this module. No section, measure, record or status changes.

**Amendment, 25 November 2026 (KST), v0.2.0.** Purpose and boundary gains the order of the two pillars. Section 4 gains two subsections: The owner's hours, the oversight load per owner and the governed share, with an invented illustration that `lean-ai/tools/oversight.py` recomputes; and Reading a vendor's usage analytics. Section 9 names the new script and Sources gains [V1]. The [pilot protocol](./lean-ai/pilot-protocol.md), at v0.2.0, gains the record of an owner's hours. No doctrine, step, gate, tier, role or rule is added, and no saving is established.

---

## Purpose and boundary

Lean AI is the disciplined removal of avoidable work, inference and dependency from AI-enabled workflows, while preserving defined outcomes, required controls and human accountability.

Its unit is one accepted business outcome. Its question is: what is the least costly, sufficiently capable and governable way to produce that outcome using the options actually available to us?

The answer may be a stronger model, a smaller model, ordinary software, a reusable template, a human decision or discontinuing work whose recipient cannot explain its value. Lower model expenditure is one possible result. It is not the acceptance criterion.

Lean AI must remain within the purpose, authority, boundaries and exit already authorized for the workflow. No financial advantage overrides an applicable mandatory constraint.

**The power to stop comes first.** Toyota's account of its production system rests on two pillars and lists *jidoka*, stopping at an abnormality, before just-in-time, the economy of making only what is needed. Lean AI keeps that order ([*The Boundary and the Limit*](https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-boundary-and-the-limit.md), Section 9.3). The doctrine canon says of Slow AI: "It is a precondition" ([DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#1-slow-ai)). Economy without the power to stop makes agents cheaper and nothing else. In this module the resource envelope of section 6 and the exit of section 7 come before any saving sought under section 8. This orders the module's existing sections. It adds no step or gate.

**Who uses it.** The business owner owns value and the decision to fund the service. The architect and operational owner measure and change the system. Finance reviews cost allocation and claims of cash savings. The designated reviewer and approver retain the Kitchen's tier-specific responsibilities. One person may hold several roles where the existing governance permits it; the roles and decisions still remain distinct.

**What goes in and what comes out.** In: the task brief and the definition of done (W03, W08), the measurement protocol (W15), the case observations (W16) and the billing or contract rates for the same cases. Out: the eligibility fields of section 2, the result set of section 4, the resource envelope of section 6 in the authorization (W10), the exit rehearsal record of section 7 and a decision under section 8 recorded in W17. A reader with one workflow and its W16 records can start at section 4.

**Where it comes from.** Tiny Servants are narrow AI services with one purpose, clear boundaries and a named owner, which do one useful task well and then stop ([profile README](https://github.com/rolldabones/rolldabones#definitions)). A service specified that narrowly seldom needs the largest model for every task, and what it costs can be counted. Lean AI is the accounting for that claim, not a second argument for it. [*The Artificial Familiar*](https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-artificial-familiar.md) carries the vocabulary.

**When to use it.** At workflow selection, before the commercial readiness decision, after a material cost or eligibility change and at the existing operational review. Use the module proportionately. A personal task may need a short comparison; a consequential enterprise service needs recorded inputs, reproducible calculations and a tested continuity route.

## 1. Start from the instruments already in the Kitchen

Use existing records rather than creating a parallel paperwork system.

| Work to perform | Existing record | Lean AI addition |
|---|---|---|
| State the useful outcome and baseline | Kitchen Steps 1 to 4; W03 and W08 | Name the recipient, demand and non-AI alternative |
| Authorize use and resource limits | W10; Take-Out service ticket | Add the spending envelope and eligibility conditions to the existing boundaries |
| Specify architecture and cost | Primer section 8.10; F24 | Separate case-processing, full recurring and transition economics |
| Set the comparison before running it | W15 Measurement protocol | Pre-register the intervention, cost boundary and minimum worthwhile improvement |
| Capture observations | W16 Case observation record | Link per-attempt usage and billing to the same case ID |
| Interpret results | W17 Results and business value | Report cost per accepted outcome with acceptance rates and total expenditure |
| Change and release | W20; Kitchen Gates 6 and 7 | Re-evaluate every materially changed configuration |
| Preserve continuity | F22; W21; RedCap-00 provider exit drill | Rehearse loss of eligibility and an economic exit |
| Learn from operation | Service Record; W18 and W24a | Record where apparent savings moved work or risk to someone else |

The [Consultant Workbook](https://github.com/rolldabones/slow-ai-kitchen/blob/main/consultant-workbook.md) is the source of record for W15 to W17 and their measurement rules. The [Enterprise AI Architecture Primer](https://github.com/rolldabones/slow-ai-kitchen/blob/main/enterprise-ai-architecture-primer.md) is the source of record for the architecture and cost guidance. Split files are reading aids, not independent authorities to ingest and count again.

## 2. Treat constrained model choice as a scenario

An enterprise's usable model set can narrow because of law, procurement rules, customer terms, internal policy, data restrictions, withdrawn products or commercial conditions. Record the actual constraint and its scope. Do not turn a scenario into a statement of law.

The policy hypothesis motivating this module is that restrictions on some suppliers or deployments could concentrate enterprise demand among eligible providers and raise effective costs. It is not a prediction that all open models will be discouraged or that all private enterprises must buy from a government-approved list.

For context, the July 2025 US AI Action Plan expressly supports open-source and open-weight AI. The 2 June 2026 executive order on advanced AI expressly disclaims creation of mandatory model licensing or preclearance under its section 3. The Department of Homeland Security's notice of 20 October 2026 imposes specific DeepSeek procurement and removal restrictions in federal civilian systems. These are different kinds of policy action. The cited instruments do not establish a universal approved-provider obligation for private enterprises. [P1 to P3]

Use three scenarios, without assigning unsupported probabilities:

| Scenario | Question to test | Trigger to monitor |
|---|---|---|
| Broad choice | Does the workflow pay for itself while eligible options remain available? | Actual cost, quality and utilization |
| Selective restriction | Can the service continue if one supplier, model lineage or deployment becomes ineligible? | Applicable rule, contract or policy change with scope and effective date |
| Constrained supply | Can the service operate if the eligible set narrows and prices or minimum commitments rise? | Price notice, withdrawal, capacity restriction or approval loss |

For price sensitivity, use explicit stress assumptions, for example unchanged price, twice the model price and five times the model price. These are test inputs, not forecasts. Reprice the affected component, not the entire workflow. Test falling prices as contrary evidence too.

Open-source and open-weight are not interchangeable license classifications. Model origin, distribution license, deployment location and operating provider are separate facts. Self-hosting is neither automatically cheap nor automatically eligible. An American hosting provider does not by itself resolve a restriction on the underlying model.

**Eligibility fields to add to the existing tool record:** model and version; developer and relevant lineage; license; hosting and region; data class; authorized use; approving authority; source and effective date of the constraint; evidence; review date; fallback. Unknown eligibility blocks the affected deployment decision until resolved by the appropriate authority. It is not permission to experiment with restricted data.

## 3. Define value and remove unnecessary work

Before optimizing the model, ask the recipient what decision, action or service the output supports. Record the answer in the task brief. An output that is generated but neither used nor required is a candidate for removal.

Map the whole workflow, including preparation, waiting, model interaction, verification, correction, release and downstream handling. Mark each activity as necessary for the outcome, necessary for a constraint or a candidate for removal. The owner of the relevant obligation decides whether an activity is genuinely unnecessary.

Common candidates include duplicate status reports, repeated collection of known facts, repeatedly drafting approved standard language, regenerating an entire document to change one field and asking a model to perform calculations already defined in code. Review the evidence before removing any of them.

Preserve exploratory work where exploration is the authorized purpose. Its definition of done may be a tested hypothesis, a decision to stop or a bounded set of alternatives. Do not impose a production throughput metric on discovery and then declare discovery wasteful.

**Record:** the activity removed, its former purpose, the evidence that removal is permissible, its owner and the observed effect. “The AI can do it cheaply” is not evidence that it should be done.

## 4. Count the whole cost, once

Set the unit, population, period, currency and cost boundary in W15 before collecting results. One case may contain several attempts and several model or tool calls. A failed attempt consumes resources even when a later attempt succeeds.

Keep three economic views:

1. **Case-processing cost:** model and tool charges, attributable compute and the human effort required to process all cases, including unsuccessful cases and fallback.
2. **Full recurring cost:** case-processing cost plus incremental monitoring, support, maintenance, recurring evaluation and allocated shared operating costs for the period.
3. **Pilot or transition cost:** recurring cost for the pilot period plus setup, training, initial evaluation, migration and change costs. If costs are amortized in a longer business case, disclose the horizon and allocation method and also show the cash requirement.

For a defined cohort:

**Cost per accepted outcome = total attributable cost for all cases and attempts in the cohort / number of outcomes accepted under the pre-agreed definition of done.**

Show which of the three cost views supplies the numerator. If a required cost is missing, label the result partial. If no outcomes are accepted, the ratio is undefined and the cost incurred remains visible. Never convert either condition to zero.

Use W16's five mutually exclusive human-effort categories. Sum effort across everyone involved, including reviewers and downstream correction. Count a minute once. Do not add review cost again if it already appears in the case total. Separate elapsed turnaround from active effort. Waiting may matter economically, but its valuation must be stated separately rather than silently added to labor cost.

Report accepted, refused, abandoned and unresolved cases against all attempted cases. A safe refusal can be a successful control outcome without being an accepted business output. If the service itself is a triage or refusal service, define that outcome in advance and report each disposition separately. Do not inflate the denominator after seeing the results.

**A worked illustration, with invented figures.** Ten cases are attempted in a month. Eight are accepted, one is refused and one is abandoned, across thirteen attempts.

| Line | Amount | Running total | Per accepted outcome (8) |
|---|---:|---:|---:|
| Model and tool charges, all thirteen attempts | 26.00 | | |
| Human effort, all ten cases: 300 minutes at 1.40 | 420.00 | | |
| **Case-processing cost** | | 446.00 | 55.75 |
| Monitoring, support and recurring evaluation allocated to the month | 120.00 | | |
| **Full recurring cost** | | 566.00 | 70.75 |
| Setup, training and initial evaluation | 800.00 | | |
| **Pilot cost, as a cash requirement** | | 1,366.00 | 170.75 |

Three things the illustration shows. Dividing the case-processing cost by the ten cases attempted gives 44.60, a fifth below the true 55.75, because two cases cost money and produced nothing accepted. Doubling the model price moves the case-processing figure from 55.75 to 59.00, and a fivefold price moves it to 68.75, a rise of 23.3%, because the reviewer's minutes carry the cost and the model does not. And the same month reports 55.75, 70.75 or 170.75 depending on the view, which is why the view is named beside every figure. The figures are invented to show the arithmetic; `lean-ai/tools/validate.py` recomputes them as check C15.

F24's arithmetic combines attempt cost, attempts per completed task and reviewer minutes. Its displayed totals reconcile. For this module, treat that calculation as case-processing cost unless the other recurring costs are demonstrably included; from slow-ai-kitchen v3.5.0, F24 says so itself. W15 and W17 already require the wider cost boundary. The word “fully” must be supported by an allocation record.

F24 counts completed tasks and this module counts accepted outcomes. The two agree only where completion means acceptance under the definition of done. State which is meant before the figures are compared.

**Minimum result set:** total cost; cost per accepted outcome; attempted and accepted counts; first-pass acceptance; final acceptance; material defects; mandatory control failures; active human effort; elapsed turnaround; difficult-case performance; missing data; continuing dependency and exit cost. Averages alone are insufficient.

Capacity released is not automatically cash saved. Identify the actual expense avoided, capacity redeployed or service improvement realized. Keep uncertain incident losses and disruption exposures in separate scenario analysis rather than burying speculative precision in the unit cost.

### The owner's hours

The cost per accepted outcome prices the minutes people spend overseeing the work. Those minutes have a second limit, which no price shows: the hours of the named owner who answers for the workflow. [*The Boundary and the Limit*](https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-boundary-and-the-limit.md) sets out the arithmetic in its Section 8, and on the theory the paper governs. This module carries it as the second of three measures, between cost per accepted outcome and time to exit (the paper's Section 9.4).

For each named owner, over a week or a month and in the busiest period, compare the hours of oversight the owner's workflows demand, D, with the qualified hours the owner, or people the owner has authorized, can give, O. For each workflow, D counts the items N, the routine minutes per item a, the share of items that need a person e, the minutes to resolve each such item t and the standing hours s:

**D = the sum, over the owner's workflows, of N × (a + e × t) / 60 + s**

The **oversight load** is D / O. The **governed share** is O / D, capped at one: the largest part of the designed oversight that the owner can in fact perform. Unlike a ratio of activity, the share has a ceiling.

The terms come from records the Kitchen already keeps. W16's three oversight categories (initial review; correction and re-review including fallback; final approval) and its first-pass result give a, e and t. The standing hours are in W18, W20 and W24A, and W22 settles whose hours count toward O. The pilot protocol's [record of an owner's hours](./lean-ai/pilot-protocol.md#3a-owners-hours) takes them down. A minute counted here is the same minute already in the case total, read against a second limit and not priced again.

**The illustration again, with invented figures.** Split the 300 minutes of the month above into W16's five categories: preparation and first-pass work 40, production or AI interaction 80, initial review 100, correction and re-review 50, final approval 30. Oversight is the last three, 180 minutes. The month's owner has a standing hour of review and 3.5 qualified hours to give.

| Line | Figure |
|---|---:|
| Oversight effort, 180 minutes at 1.40 | 252.00 |
| Share of the case-processing cost of 446.00 that was oversight | 56.5% |
| Oversight in the 55.75 per accepted outcome | 31.50 |
| D: 180 minutes, plus the standing hour | 4.0 hours |
| O: the owner's qualified hours | 3.5 hours |
| Oversight load, D / O | 1.14 |
| Governed share, O / D | 87.5% |

Two things the illustration shows. More than half of what an accepted outcome costs here is oversight, and a model that cost nothing would still leave 52.50 of the 55.75. And the owner is asked for half an hour more than the owner has, so 12.5% of the designed oversight cannot be performed as designed, whatever the unit cost says. The figures are invented to show the arithmetic; `lean-ai/tools/oversight.py` recomputes them and checks each one against this page.

When the load passes one, the choice is the owner's or the management body's: fewer items, a better specification, more qualified hours or an accepted risk, with the name of the person who accepted it (the paper's Appendix C). Read the arithmetic with the paper's own limits (its Section 8.5). It has no term for errors that pass unseen, so it is read beside the material defects of the minimum result set. It counts hours and not competence. It is read at the peak, because work arrives in bursts. It cannot see one person who both operates and oversees a workflow. And it does not set the threshold. In the paper's words, "It has no equilibrium and it proves nothing."

### Reading a vendor's usage analytics

Vendors now offer reports built from a workforce's AI sessions. Claude Enterprise's smart reports are the example here, as Anthropic's help article described them when read in full on 25 November 2026 (KST) [V1]: available on Enterprise plans and off by default, built by Claude reading a sample of the sessions in scope and pricing spend at list price. Check the current article before relying on any detail. Such a report can feed this module. It cannot replace it.

| What the report gives | Where it goes in this module | What it does not give |
|---|---|---|
| Spend by workstream and type of output, at list price | Model and tool charges, one line of case-processing cost | Billed cost, human effort, recurring and transition cost; label any figure built from it partial |
| Deliverables produced and task outcomes, from a sample of sessions as Claude reads them | Attempted and completed counts, once sessions are mapped to cases | A full count, because the report reads a sample; acceptance under the owner's definition of done, because completion is not acceptance (section 4) |
| Pain points: a connector not set up, output that did not match the ask, approval or sign-in gating, tool failures, rework loops | Candidate bottlenecks for section 5 | Proof of the bottleneck; observe it before optimizing against it |
| Recurring workflows worth turning into shared skills | Candidates for removal or standardization in section 3 | The record section 3 requires: owner, former purpose, evidence that the change is permissible |
| Inefficiencies: sessions that produced nothing usable, with their cost | Unsuccessful attempts, which section 4 already counts in the numerator | A judgment that the work was waste; exploratory work is preserved where exploration is authorized (section 3) |

Before the report is used here, the people whose sessions are read are told, and consulted where the law of their workplace requires it, before the feature is turned on. Attribution to individuals stays off, because this module counts the cost of outcomes, not the performance of people. The article itself says the reports should not be used to evaluate individual performance or to make employment decisions, and it describes attribution as off by default, with each reveal of names logged. Each team sees its own report first and names the fixes. Acceptance comes from the owner, not from a classifier reading transcripts after the fact.

## 5. Optimize against an observed bottleneck

Primer section 8.10 remains the operational reference. The following sequence adds an upstream question about unnecessary work and a downstream requirement to validate the result; it does not replace the Primer's detailed playbook.

| Intervention | Evidence to seek | Failure to test |
|---|---|---|
| Remove unnecessary activity | Recipient confirms no required value or obligation is lost | Hidden downstream use disappears |
| Improve facts and specifications | Fewer correction cycles at unchanged acceptance criteria | Missing facts are silently assumed |
| Reuse approved material | Provenance, applicability and review date remain valid | Stale, unauthorized or cross-Client reuse |
| Use deterministic processing | Rule can be stated and tested without interpretive judgment | Code makes a precise version of the wrong rule |
| Repair retries and tool chains | Fewer calls per accepted outcome | Failed or uncertain actions are repeated |
| Reduce unused context and output | Required evidence and instructions remain available | Material exception or provenance is omitted |
| Cache or defer suitable work | Actual traffic, freshness, permission and timing permit it | Stale response, confidentiality leak or missed deadline |
| Change effort, routing or model | Evaluated configuration clears the same requirements | Hard cases are misrouted or quality cost exceeds the saving |
| Change architecture | Whole-service benefit exceeds build and operating cost | Added orchestration costs more than it saves |

Measure one material intervention at a time where practical. Where changes must be bundled, say so and do not assign the result to one component. Treat provider-specific prices, caching rules, batch eligibility and feature support as dated implementation facts to verify for the actual contract and deployment.

A routing policy is itself part of the evaluated configuration. Test the selection decision, the downstream result and the escalation route. Do not deploy a router merely because each model performed well when humans selected its tasks.

## 6. Put the resource envelope in the authorization

Use W10 and the Take-Out service ticket to record maximum attempts, tool calls, wall time, concurrent work and expenditure. Separate an alert from an enforceable limit. Name the person authorized to change the envelope and the conditions for doing so.

Enforce material limits in the host, gateway or equivalent control layer. A prompt promising not to overspend is not an expenditure control. Where calls run concurrently, reserve capacity or funds for in-flight work before authorizing more. Reconcile actual charges and uncertain outcomes afterwards. Test the enforcement mechanism in its deployment; this module contains no production gateway implementation.

State what happens when a limit is reached: stop the AI activity, preserve its record and enter the authorized fallback. Do not remove the reviewer to make the budget fit. Do not route around a denied permission. A timeout leaves an action's outcome uncertain until reconciled, not automatically failed and safe to repeat.

For a critical service, stopping an AI run does not terminate the organization's service obligation. Fund and staff the fallback before relying on the limit. An uneconomic task may be deferred or retired only by the person who has authority over that service and its obligations.

## 7. Test the exit that the economics assumes

Use F22 and the [Provider Exit Drill](https://github.com/rolldabones/RedCap-00/blob/main/provider-exit-drill.md). Keep authoritative specifications, source material, evaluation cases and decision records in appropriate custody outside the incumbent provider.

Rehearse loss of access, loss of eligibility and a price change that exceeds tolerance. Record time to restore an accepted service, the people required, migration and revalidation costs, data custody gaps and residual defects. A successful export is not a successful service restoration.

Check dependency independence. Two applications that call the same underlying model or share the same restricted dependency may fail together. A provider abstraction layer improves some switching mechanics but does not establish equivalent behavior, lawful processing or contractual rights.

The rehearsal must use an eligible destination and authorized data. If none is available, test the manual or conventional-software fallback. Do not name an untested alternative as an executable exit.

## 8. Validate before claiming a saving

Use W15 for a prospective comparison, W16 for observations and W17 for conclusions. [lean-ai/pilot-protocol.md](./lean-ai/pilot-protocol.md) supplies a ready-to-complete plan and data fields.

The baseline is the actual incumbent process or a measured non-AI alternative. The intervention is the proposed Lean change. Compare both at the same mandatory requirements, outcome definition and representative case mix. Predefine an acceptable quality margin for non-critical measures, a minimum worthwhile economic improvement and the treatment of refusals, missing data and outliers. Mandatory controls cannot be exchanged for cost reductions.

Where feasible, use paired cases with separate operators or balanced assignment to limit learning effects. Blind reviewers to the method where feasible. Separate development examples from held-out evaluation cases and from adversarial stress cases. Repeat stochastic runs. The pilot's sample size must be justified against the required precision and failure consequences; a convenient small sample does not demonstrate rare-event safety.

Report uncertainty for paired cost and quality differences, including segment results. Use resampling or another justified statistical method appropriate to the unit of independence. Three repeated outputs from one case are not three independent business cases. No observed critical failure is necessary for this release decision but does not establish that the true critical failure rate is zero.

**Decision rule:** adopt the change only when applicable mandatory requirements are met, the owner accepts the measured quality and operational limits, the economics meet the pre-agreed threshold and the continuity route is adequate. An inconclusive trial remains inconclusive. Preserve a rollback route and monitor actuals after adoption.

The account's [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md) continues to govern prompt-instrument acceptance. Passing a workflow pilot does not silently grant acceptance to a new prompt configuration. Conversely, a previously accepted prompt does not establish the economics of an enterprise workflow. If this module is later converted into a system prompt, that new instrument needs its own cases and logged acceptance run.

## 9. What the present evidence establishes

The evidence is in [lean-ai/](./lean-ai/README.md): the [audit and validation report](./lean-ai/audit-and-validation-report.md), the derived records under `lean-ai/evidence/` and the three scripts that produce them. It is a record of the account as captured on 15 November 2026 (KST), not a standing claim about later versions.

**Structural scan.** Every file in the captured public inventory was scanned: 1,658 files in 22 repositories, each verified against its Git blob hash. The scan covered file integrity, UTF-8 decoding, JSON and Python syntax where applicable, explicit inline Markdown file links and topical evidence discovery. The captured commit of 21 repositories matched the working clone on the same day; `the-ai-generalist` was released at v2.1.0 after the capture and is scanned at the commit before it. Substantive review went to the sources that govern this module. It was not a legal or semantic audit of every sentence.

**Retrospective analysis.** Token counts in 136 published transcript records were checked against six run manifests. All 136 matched. In the GRCnext R2 record, both configurations received the same recorded input-token total, 242,629 across 26 cases. Recorded output totals were 110,892 for `claude-opus-5-5` and 127,107 for `claude-sonnet-5-5`, 14.622% more for the latter. Those strings are the identifiers in the historical records, not recommendations about current products.

The published reviewed result accepts the former configuration with a residual and rejects the latter. Recalculation reproduces the recorded gate arithmetic. It does not independently regrade the outputs. The record also documents a judgment-call qualification on A6; that qualification stays attached to the finding. [E1]

This supports a narrow conclusion: output consumption and acceptance can differ across configurations even on the same case set. It does not establish a price advantage, a model ranking or a Lean AI savings effect. Billing, reviewer time, an intervention comparison and production case mix are absent from this comparison.

**Published examples.** The workbook's 900-minute against 600-minute worked example is explicitly fictional. F24's Modeled and Actual columns are the artifact set's worked figures and are labeled as such from slow-ai-kitchen v3.5.0. Neither is empirical evidence of savings.

**Checks.** Twenty checks pass: fifteen worked examples of the accounting and decision rules in section 4 and section 8, the illustration in section 4 among them, and five consistency checks on the historical records. They are arithmetic and logic. They are not behavioral acceptance tests of any deployed system and they confer no acceptance on this module. Five existing repository checks (GRCnext fixtures, the Definition of Done and Origami release checks and the two Appendix I figure checks) also pass, on the captured files and again in the working clones with their Git history.

**From v0.2.0.** `lean-ai/tools/oversight.py` recomputes the invented figures of [The owner's hours](#the-owners-hours), checks each against this page and writes `lean-ai/evidence/oversight-illustration.json`, dated 25 November 2026 (KST). It needs no captured sources and changes neither the twenty checks nor the record of 15 November 2026.

**Empirical enterprise validation: pending.** No new model benchmark and no enterprise pilot was run for this issue.

## 10. Operate and learn

At the existing review cadence, compare forecast with actual cost and acceptance, investigate the expensive tail and check whether demand increased after the workflow became easier to use. Lower unit cost can coexist with higher total expenditure.

Use the Service Record to identify who gained time and who inherited more work. Record substantive review, maintenance and escalation effort even when it lands in another cost center. Retire controls only through the existing authority and change process, with evidence that their objective remains met or is no longer required.

**Bias check.** The preferred story is that simplification saves money. The strongest contrary result is a simpler or cheaper model configuration that creates enough review, error or continuity burden to cost more. Design the pilot so it can find that result and publish it if it does.

**The release question:** has the enterprise removed avoidable work while keeping the outcome worth relying on, or merely moved the cost to someone less visible?

## Sources and integration references

- [P1] White House, [America's AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf), July 2025, “Encourage Open-Source and Open-Weight AI”, printed pages 4 to 5. Read 15 November 2026.
- [P2] White House, [Promoting Advanced Artificial Intelligence Innovation and Security](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/), 2 June 2026, section 3(c). Read 15 November 2026.
- [P3] Department of Homeland Security, [notice concerning DeepSeek exclusion and removal](https://www.govinfo.gov/content/pkg/FR-2026-10-20/html/2026-21447.htm), 91 FR 66346, 20 October 2026, summary and supplementary information. Read 15 November 2026. This module does not interpret the full signed order or its application to a particular contractor.
- [V1] Anthropic, [Get started with smart reports](https://support.claude.com/en/articles/16893491-get-started-with-smart-reports), Claude Help Center, read in full on 25 November 2026 (KST); the page gives no publication date. A dated description of a vendor feature, cited as an example, not as a recommendation.
- [E1] [GRCnext prompt evaluation cases](https://github.com/rolldabones/GRCnext-Copilot/blob/main/tests/prompt-evaluation-cases.md), R2 of 27 October 2026, and associated run manifests and transcripts. The captured inventory and the calculations are under [lean-ai/evidence/](./lean-ai/README.md).
- [Kitchen method](https://github.com/rolldabones/slow-ai-kitchen/blob/main/README.md); [F24](https://github.com/rolldabones/slow-ai-kitchen/blob/main/primer-workbook/artifacts/F24-cost-model-and-unit-economics-sheet.md); [W15](https://github.com/rolldabones/slow-ai-kitchen/blob/main/workbook/30-w15-measurement-protocol.md); [W16](https://github.com/rolldabones/slow-ai-kitchen/blob/main/workbook/31-w16-case-observation-record.md); [W17](https://github.com/rolldabones/slow-ai-kitchen/blob/main/workbook/32-w17-results-and-business-value.md); [Service Record](https://github.com/rolldabones/slow-ai-kitchen/blob/main/service-record.md); [Take-Out](https://github.com/rolldabones/slow-ai-kitchen/blob/main/take-out-delivery-and-vending-machines.md).
- [Computational Drafting](https://github.com/rolldabones/computational-drafting); [Definition of Done: Trade-Offs](https://github.com/rolldabones/definition-of-done/blob/main/05-trade-offs.md); [GRCnext methodology](https://github.com/rolldabones/GRCnext-Copilot/blob/main/methodology/method-and-logic.md).
- [*The Boundary and the Limit: Effectiveness, Lean AI and the Theory of the Governed Firm*](https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-boundary-and-the-limit.md), working paper, version 1.4, 17 November 2026: the theory behind this module, why its unit is the accepted outcome (its Section 4), the arithmetic of the owner's hours (its Section 8) and why the power to stop comes before economy (its Section 9). On the theory, the paper governs.

**Final Liability rests with the Human.**
