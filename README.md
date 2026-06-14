[README.md](https://github.com/user-attachments/files/28936696/README.md)
# Slow AI Kitchen

### Method and Workshop Guide

*AI is a tool in the kitchen, not the chef.*

**Son-U Michael Paik**
CEO, GRC Solutions Korea | General Counsel, BABL AI
[www.grcskorea.com](http://www.grcskorea.com)

| Version | Date | Status | License |
|---|---|---|---|
| v2.0 | 2026-06-11 (KST) | Final | CC BY-NC-SA 4.0 (see [License](#license)) |

A 12-step governed AI methodology for professional work, from individual task discipline through organizational deployment and institutional program governance. It includes risk tiers, role architecture, a workshop guide and an addendum on sustained AI governance, risk management and compliance. It is built on one principle.

**Final Liability rests with the Human.**

---

## Contents

- [How to Use This Repository](#how-to-use-this-repository)
- [Repository Contents](#repository-contents)
- [What Slow AI Kitchen Is](#what-slow-ai-kitchen-is)
- [Core Principles](#core-principles)
- [Why This Works](#why-this-works)
- [The Method at a Glance](#the-method-at-a-glance)
- [Risk Tiers](#risk-tiers)
- [Roles](#roles)
- [The Twelve-Step Method](#the-twelve-step-method)
  - [Step 1: Define the Dish](#step-1-define-the-dish)
  - [Step 2: Mise en Place (Gate 1: Definition of Done)](#step-2-mise-en-place-gate-1-definition-of-done)
  - [Step 3: Knife Work (Gate 2: Manual First Pass)](#step-3-knife-work-gate-2-manual-first-pass)
  - [Step 4: Read the Kitchen (Gate 3: Socio-Technical Context)](#step-4-read-the-kitchen-gate-3-socio-technical-context)
  - [Step 5: Apply Heat (Gate 4: Bounded AI Use)](#step-5-apply-heat-gate-4-bounded-ai-use)
  - [Step 6: Name the Chef de Partie (Gate 5: Final Liability)](#step-6-name-the-chef-de-partie-gate-5-final-liability)
  - [Step 7: Build the Plate](#step-7-build-the-plate)
  - [Step 8: Taste Before Service (Gate 6: Verification and Validation)](#step-8-taste-before-service-gate-6-verification-and-validation)
  - [Step 9: Open the Pass (Gate 7: Human Release Decision)](#step-9-open-the-pass-gate-7-human-release-decision)
- [The Feast](#the-feast)
  - [Step 10: Plan the Menu (Gate 8: Authorized Tool Registry)](#step-10-plan-the-menu-gate-8-authorized-tool-registry)
  - [Step 11: Staff the Brigade (Gate 9: Competency and Authorization Record)](#step-11-staff-the-brigade-gate-9-competency-and-authorization-record)
  - [Step 12: Run the Event (Gate 10: Operational Audit and Review Cycle)](#step-12-run-the-event-gate-10-operational-audit-and-review-cycle)
- [Definition of Done for the Method Itself](#definition-of-done-for-the-method-itself)
- [The Workshop](#the-workshop)
- [Addendum: Your Restaurant](#addendum-your-restaurant)
- [Related Work](#related-work)
- [How to Cite](#how-to-cite)
- [License](#license)
- [Changelog](#changelog)
- [About the Author](#about-the-author)

---

## How to Use This Repository

**One professional, one task.** Read [Core Principles](#core-principles) and Steps 1 through 9, then cook from the [Slow AI Cookbook](./slow-ai-cookbook.md). The Cookbook stays in Tier 1 and Tier 2 and needs no org chart.

**A team lead or trainer.** Run [The Workshop](#the-workshop). Load one of the sample kitchen prompts as the operating prompt for the exercise.

**A function or program owner.** Read [The Feast](#the-feast) and [Your Restaurant](#addendum-your-restaurant), then start the tool registry at Step 10. The [restaurant resources](./restaurant-resources.md) file collects the referenced standards. The [federal workforce literacy bridge](./federal-workforce-literacy-bridge.md) aligns the method with U.S. federal workforce AI literacy standards.

## Repository Contents

| File | What it is | Use it when |
|---|---|---|
| [README.md](./README.md) | The canonical method: principles, tiers, roles, twelve steps, workshop guide and the Your Restaurant addendum | Always; every other file defers to this one |
| [slow-ai-cookbook.md](./slow-ai-cookbook.md) | Starter Edition recipes. Each recipe is one pass through Steps 1 through 9 in eight fields, scoped to Tier 1 and Tier 2 work | You want to run the Kitchen on a real task today |
| [sample-kitchen-prompts-compressed-builder-version.md](./sample-kitchen-prompts-compressed-builder-version.md) | Single-layer operating prompt implementing Steps 1 through 9 for GRC work (March 2026) | You want the discipline enforced inside the AI session itself |
| [sample-kitchen-prompts-two-layer-version.md](./sample-kitchen-prompts-two-layer-version.md) | Two-layer operating prompt: Steps 1 through 9 plus abbreviated Feast controls (March 2026) | You want session-level discipline with light deployment controls |
| [restaurant-resources.md](./restaurant-resources.md) | Reference standards for the Restaurant addendum, including ISO/IEC 42001 and NIST resources, with a note on certification versus substance | You are building the program governance layer |
| [federal-workforce-literacy-bridge.md](./federal-workforce-literacy-bridge.md) | Standalone add-on module integrating the U.S. Department of Labor AI Literacy Framework (TEN 07-25) with the method | You are aligning training to federal workforce literacy standards |

Both sample prompts carry scope notes identifying where they deviate from the canonical method. The scope note governs. Where a prompt and this README conflict, this README controls.

---

## What Slow AI Kitchen Is

Most organizations do not fail because they lack AI access. They fail because they use AI too early, too vaguely, too fast and without enough human control. Slow AI Kitchen corrects that by imposing sequence, standards and accountability.

The method is a disciplined operating framework for using artificial intelligence in professional work without outsourcing judgment. It is designed for knowledge work, operational work and team-based decision support. It works for one professional working alone, a cross-functional team producing a shared deliverable or a corporate workshop teaching proper AI use.

It is called a kitchen because a kitchen is not a theory space. It is a production space. Ingredients must be prepared. Order matters. Heat must be controlled. Hygiene matters. Standards matter. The thing that leaves the counter must be fit to serve. And in any real kitchen, the chef (the human) is responsible for what goes out the pass. When the kitchen scales to feed an organization, the kitchen becomes a feast: planned, staffed and governed as an event, not improvised as a series of individual meals.

**Final Liability rests with the Human.**

---

## Core Principles

Five principles govern the method. They are not aspirational. They are operating constraints.

**1. Think before prompting.** AI should extend thought, not replace the initial act of thinking.

**2. Define success before producing output.** The team must know what "done" means before it starts.

**3. Use AI inside a bounded frame.** AI is introduced only after the task, constraints and context are clear.

**4. Verify before reliance.** Plausible output is not trustworthy output.

**5. Keep responsibility human.** AI can assist, draft, simulate and challenge. It does not own the decision.

---

## Why This Works

The problem with most organizational AI use is not that the tools are bad. It is that premature prompting disconnects output generation from the cognitive work that would otherwise catch its errors. When a team prompts before it has thought, the AI fills the gap, and the team inherits whatever the AI invented without having the intellectual scaffolding to evaluate it.

Slow AI Kitchen corrects this by inserting irreversible human-first steps before AI is available. By the time AI is used, the team has already formed a judgment. The AI extends that judgment rather than substituting for it.

The method does not slow AI down arbitrarily. It slows it down to the speed of human verification, which is the only speed at which AI output can be responsibly relied upon. At organizational scale, the same logic applies: the Feast steps prevent institutions from deploying tools before they have defined what governed use looks like, staffed the people who will be accountable for it and built the operational layer to detect when it fails.

---

## The Method at a Glance

The method is both a sequence and a control architecture. It operates in two registers. Steps 1 through 9 (the Kitchen) govern the production of individual and team work product. Steps 10 through 12 (the Feast) govern the organizational deployment of multiple AI tools across multiple users and functions.

Ten of the twelve steps function as gates: checkpoints that output or deployment decisions must pass before advancing. Steps 1 and 7 are pure production steps with no gate function. A gate that is skipped does not disappear; it becomes a liability.

| Step | Register | Name | Gate | Gate Function | Primary Role | Output |
|---|---|---|---|---|---|---|
| 1 | Kitchen | Define the Dish | — | Production step | Preparer | Task brief |
| 2 | Kitchen | Mise en Place | Gate 1 | Definition of Done | Preparer | DoD checklist |
| 3 | Kitchen | Knife Work | Gate 2 | Manual First Pass | Preparer | Annotated sources, first-pass draft |
| 4 | Kitchen | Read the Kitchen | Gate 3 | Socio-Technical Context | Preparer | Context and risk map |
| 5 | Kitchen | Apply Heat | Gate 4 | Bounded AI Use | Builder | AI-assisted working draft |
| 6 | Kitchen | Name the Chef de Partie | Gate 5 | Final Liability | Owner (named here) | Accountability record |
| 7 | Kitchen | Build the Plate | — | Production step | Builder | Versioned deliverable |
| 8 | Kitchen | Taste Before Service | Gate 6 | Verification and Validation | Reviewer | Evidence and validation log |
| 9 | Kitchen | Open the Pass | Gate 7 | Human Release Decision | Approver, Owner | Decision record, post-action review |
| 10 | Feast | Plan the Menu | Gate 8 | Authorized Tool Registry | Executive Sponsor, AI Owner | Tool registry, deployment policy |
| 11 | Feast | Staff the Brigade | Gate 9 | Competency and Authorization Record | AI Owner | Role matrix, training log, escalation chain |
| 12 | Feast | Run the Event | Gate 10 | Operational Audit and Review Cycle | AI Owner, Executive Sponsor | Audit log, incident record, revised registry |

**Steps 1–9 are the kitchen. Steps 10–12 are the feast.**

---

## Risk Tiers

Not every task needs the same depth of control. A three-tier model makes the method usable in real organizations without treating a formatting task as a high-stakes audit. The tiers apply to task-level work governed by Steps 1 through 9. Steps 10 through 12 are not a tier; they are a separate organizational governance layer that applies whenever an organization deploys AI tools at any scale, regardless of which task tier dominates their work.

**Tier 1: Low-Stakes Work**
Examples: rough brainstorming, non-public internal drafts, formatting, idea generation.
Controls: abbreviated DoD; basic human review; no external deployment without verification.

**Tier 2: Moderate-Stakes Work**
Examples: internal analyses, training materials, client-facing drafts under review, process documentation.
Controls: full DoD; socio-technical context check; named reviewer; evidence log.

**Tier 3: High-Stakes Work**
Examples: decisions affecting customers, employees or regulated operations; legal, compliance or risk determinations; external representations; automation tied to action.
Controls: full Steps 1–9 method; explicit escalation path; second review; sign-off record; remediation or rollback plan.

### Tier Application Map

Tiering adjusts the depth of each gate. It never deletes a gate. These are defaults; a function may set stricter requirements through its tool registry under Step 10, never looser ones for Tier 3 work.

| Gate | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Gate 1: Definition of Done | Abbreviated: 1–3 pass/fail tests | Full: 3–7 tests | Full: 3–7 tests |
| Gate 2: Manual First Pass | At least one light form (sketch or outline) | At least one full form | Full first pass, retained as evidence |
| Gate 3: Socio-Technical Context | Rapid scan: who is affected if this is wrong | Documented context check | Documented context and risk map with escalation triggers |
| Gate 4: Bounded AI Use | Required | Required | Required; tools and uses logged |
| Gate 5: Final Liability | Individual is Owner by default | Named reviewer and Owner | Distinct Reviewer, Approver and Owner; escalation path named |
| Gate 6: Verification and Validation | Basic human review | Review against DoD with evidence log | Second review with evidence log |
| Gate 7: Human Release Decision | No external deployment without verification | Reviewer sign-off before release | Sign-off record; remediation or rollback plan on file |

---

## Roles

The method uses two distinct role sets at two different levels. Task roles govern Steps 1 through 9 and apply to individual and team work. Organizational roles govern Steps 10 through 12 and apply to the deployment and oversight of AI tools across functions.

### Task Roles (Steps 1–9)

| Role | Responsibility |
|---|---|
| Preparer | Frames the task, gathers sources, performs first-pass work |
| Builder | Uses AI within the approved frame to produce the artifact |
| Reviewer | Checks substance, logic, completeness and fit |
| Approver | Signs off on consequential use or deployment |
| Owner | Bears final responsibility for the outcome |

### Organizational Roles (Steps 10–12)

| Role | Responsibility | Task-Level Analogue |
|---|---|---|
| AI Owner | Accountable for AI-assisted outcomes within a specific function; carries organizational rather than task-specific accountability | Approver and Owner |
| AI Operator | Trained and authorized to use specific tools at specific risk tiers within their function | Builder |
| Executive Sponsor | The named executive at the top of the escalation chain; bears organizational liability for the deployment program | None; this role exists only at scale |

In a small team, one person may hold multiple task roles. In a larger team, they should be distinct. In every context, the Owner cannot be the AI.

---

## The Twelve-Step Method

### Step 1: Define the Dish

State the task clearly before work begins. Identify the objective, audience, business use, deadline, constraints and decision to be supported. This prevents the most common failure mode: using AI to compensate for a poorly formed task. This step has no gate function; it is the act of picking up the recipe. The gate that follows it ensures the dish is worth making.

*Output: Task brief.*

---

### Step 2: Mise en Place *(Gate 1: Definition of Done)*

Translate the task into 3 to 7 observable pass/fail tests. These are the acceptance criteria for the work. They should cover substance, usability, constraints and sign-off. Setting these before AI is used ensures the finish line is human-defined, not machine-generated.

Typical checks: accurate enough for intended use; tailored to the intended audience; within scope; supported by evidence or logic; includes owner and review path; fit for release or action.

*Output: DoD checklist.*

---

### Step 3: Knife Work *(Gate 2: Manual First Pass)*

Before AI is introduced, the human team must do the irreversible preparation. This is the knife work: reading, reasoning, calculating and sketching that cannot be delegated without losing cognitive grip on the task. A team that has not done this work cannot evaluate AI output on the same task.

Acceptable forms: annotated source materials, a hand-written outline or issue tree, a working thesis or hypothesis list, manual estimates with stated assumptions, a sketch of the structure or decision tree. Not every task requires all forms. Every task requires at least one.

*Output: Annotated source set and first-pass draft or sketch.*

---

### Step 4: Read the Kitchen *(Gate 3: Socio-Technical Context)*

Map the real-world setting in which the output will operate. Identify affected stakeholders, dependencies, weak inputs, edge cases, escalation triggers and foreseeable harms. This is where the team stops thinking about the document and starts thinking about the system.

Key questions: What is the real-world environment? What inputs are being relied on? What decision is being informed? What action will follow? Who could be affected if the output is wrong?

*Output: Context and risk map.*

---

### Step 5: Apply Heat *(Gate 4: Bounded AI Use)*

Now, and only now, use AI. Use it as an amplifier, critic, simulator, organizer or drafting assistant inside the defined frame. The controlling rule: use AI at the speed of human verification, not at the speed of machine generation.

Appropriate uses: challenge testing, alternative framing, red-teaming, outline expansion, structured drafting, summarization after human review, scenario generation.

Inappropriate uses: replacing the first pass, substituting for expert review, making unverified factual claims, making consequential decisions without human judgment.

*Output: AI-assisted working draft or analysis.*

---

### Step 6: Name the Chef de Partie *(Gate 5: Final Liability)*

Before relying on any consequential AI-assisted output, identify the accountable human. The chef de partie is the station chef who owns a specific section of the kitchen and is answerable for everything that leaves it. Name the equivalent here: the decision owner, reviewer, approver and escalation path for this output. If no one owns the outcome, the process stops.

This step prevents the standard institutional dodge: "the system said so."

*Output: Accountability record.*

---

### Step 7: Build the Plate

Convert the work into the actual deliverable: memo, checklist, workflow, briefing, presentation, policy, training asset or analysis pack. Build against the DoD, not against vague preference. Use version control where practical.

*Output: Versioned deliverable.*

---

### Step 8: Taste Before Service *(Gate 6: Verification and Validation)*

Test the deliverable against the DoD, evidence, logic, arithmetic, audience fit and operational context. Note what was checked, what failed, what changed and what remains uncertain.

This is the difference between "looks good" and "fit for use."

*Output: Evidence and validation log.*

---

### Step 9: Open the Pass *(Gate 7: Human Release Decision)*

Make the human decision. The pass is the final counter between the kitchen and the dining room. The chef stands there, reviews every plate and approves it before service. Nothing leaves without passing the pass. Here, the human reviews the verified deliverable and makes the release decision. Release or act only within defined scope.

Then review the result: did it achieve the objective, did AI help, where did risk surface and what control should change next time? This post-action review is not a formality. It is the prep list for the next service, and for any organization deploying AI at scale, it is the direct input into Steps 10 through 12.

This step turns the method into a learning system rather than a one-time ritual.

*Output: Decision record, deployment note and post-action review.*

---

## The Feast

*Organizational Deployment of Multiple Tools for Multiple Users*

A single dish, well executed, is a kitchen success. Feeding an organization is a different challenge entirely. A feast requires a menu, a brigade and a plan for running the event. Steps 10 through 12 address what happens when Slow AI Kitchen scales from one team producing one deliverable to an organization deploying multiple AI tools across multiple functions, roles and risk tiers.

The governance principles do not change. The scope does. At this scale, the failure mode is no longer one person prompting too early. It is an organization deploying tools without a menu, running an event without a brigade and blaming the kitchen when the service fails.

---

### Step 10: Plan the Menu *(Gate 8: Authorized Tool Registry)*

Before deploying multiple tools across multiple users, the organization must define which tools are authorized, for which workflows, at which risk tier and by whom. A feast is not one dish repeated. It is a coordinated set of courses, each designed for its audience, its sequence and its constraints. The organizational equivalent is a tool registry: authorized AI systems, permitted use cases, risk tier assignments and prohibited uses for each function.

Key decisions: Which tools are approved for production use? Which workflows may use AI without second review? What is the maximum risk tier any function may operate at without escalation? What tools are prohibited entirely? Who maintains the registry and on what review cycle?

This step prevents the most common organizational failure: individual teams deploying whatever tool is convenient, at whatever tier they choose, without any coordinated governance layer above them.

*Output: AI tool registry and deployment policy.*

---

### Step 11: Staff the Brigade *(Gate 9: Competency and Authorization Record)*

A large event cannot run on one chef. It requires a brigade de cuisine (the structured hierarchy of kitchen roles, from executive chef down to each station) with each position staffed, scoped and accountable upward. Deploying AI across an organization requires the same architecture. Individual competence does not aggregate into organizational reliability without explicit structure.

The brigade model applied to AI deployment: each function has a designated AI Owner (accountable for outcomes in that function), AI Operators (trained and authorized to use specific tools at specific tiers) and an escalation chain that reaches a named executive. No one operates above their authorized tier. No tool is deployed without a trained operator. No operator is authorized without verified training.

Key requirements: role assignment matrix mapping functions to authorized tools and risk tiers; training completion records for each authorized operator; documented escalation chain from operator to executive; periodic reauthorization cycle as tools and risks evolve.

*Output: Role assignment matrix, training completion log and escalation chain.*

---

### Step 12: Run the Event *(Gate 10: Operational Audit and Review Cycle)*

A feast that has been planned and staffed still has to be executed. Running the event means coordinating the brigade in real time, managing exceptions as they arise, logging what went wrong and why and conducting a full debrief afterward. Organizational AI governance requires exactly this: not a policy document that lives in a folder, but an active operational layer that monitors, responds, records and revises.

Operational requirements: audit logging for consequential AI-assisted decisions (what tool, what input, what output, what human reviewed it); incident response procedure for AI failures, errors or misuse; periodic review of the tool registry against regulatory developments, new risk disclosures and operational experience; updated training standards as tools change; executive reporting on AI use, incidents and governance health.

The event does not end when the last plate goes out. It ends when the debrief is complete, the waste log is filed and the prep list for next service is written. An organization that skips the debrief repeats the same failures under a different tool name.

*Output: Operational audit log, incident record, revised tool registry and updated training standards.*

---

## Definition of Done for the Method Itself

If you want to know whether Slow AI Kitchen was properly applied, use this test:

- [ ] the task was clearly framed
- [ ] "done" was defined in advance
- [ ] a real manual first pass occurred
- [ ] context and downstream consequences were considered
- [ ] AI was used in a bounded way
- [ ] a human owner was identified
- [ ] the deliverable was tested before reliance
- [ ] the outcome was reviewed after use

For organizational deployment, add:

- [ ] a tool registry authorizes the AI system in use
- [ ] operators are trained and assigned to their tier
- [ ] an audit and review cycle is active and maintained

If those are not true, the method was not followed, even if AI was used productively.

---

## The Workshop

### Purpose

The workshop teaches teams how to use AI properly in the normal course of work. It is not a prompt trick session. It is not a tour of features. It is a discipline workshop. Participants leave with a completed artifact, not a slide deck.

### Learning Objectives

By the end of the workshop, participants will be able to:

- frame a task clearly before prompting
- define measurable completion standards
- perform a meaningful manual first pass
- assess the socio-technical context of AI-assisted work
- use AI in a bounded and purposeful way
- verify output before relying on it
- identify the accountable human
- decide whether a deliverable is fit to deploy
- build and maintain an authorized tool registry for their function
- assign brigade roles and training requirements at organizational scale
- design an operational audit and review cycle for deployed AI tools

### Module Structure

**Module 1: Foundations (Steps 1–3)**
Focus: task clarity, Definition of Done, manual cognition and first-pass reasoning.
Message: human thinking is not optional overhead. It is the control surface.

**Module 2: Governance (Steps 4–6)**
Focus: socio-technical context, pacing and bounded AI use, accountability.
Message: AI output lives inside systems. Systems create risk. Risk requires named ownership.

**Module 3: Execution (Steps 7–9)**
Focus: building, validation, decision and deployment, review and improvement.
Message: real work is not finished when text appears. It is finished when a human can defend using it.

**Module 4: Organizational Deployment (Steps 10–12)**
Focus: tool authorization and registry, brigade structure and training at scale, operational governance and audit.
Message: individual discipline does not aggregate into organizational reliability without deliberate structure. A feast without a menu, a brigade and a debrief is just a lot of cooking happening at the same time.

### Workshop Agendas

#### Full-Day Format (8 hours including breaks)

| Time | Session |
|---|---|
| 09:00 – 09:20 | Opening: What Slow AI Kitchen is and why discipline, not access, is the problem |
| 09:20 – 10:15 | Module 1 instruction: Foundations (Steps 1–3) |
| 10:15 – 11:00 | Exercise 1: Define the task, set the DoD, complete the manual first pass |
| 11:00 – 11:15 | Break |
| 11:15 – 12:00 | Module 2 instruction: Governance (Steps 4–6) |
| 12:00 – 13:00 | Lunch |
| 13:00 – 13:45 | Exercise 2: Map socio-technical context, apply AI in bounded form, assign ownership |
| 13:45 – 14:15 | Module 3 instruction: Execution (Steps 7–9) |
| 14:15 – 15:00 | Exercise 3: Build the artifact, verify and validate, open the pass |
| 15:00 – 15:15 | Break |
| 15:15 – 16:00 | Module 4 instruction: Organizational Deployment via The Feast (Steps 10–12) |
| 16:00 – 16:40 | Exercise 4: Draft a tool registry entry, assign brigade roles, design an audit cycle |
| 16:40 – 17:00 | Closing: teams present deployment decision; common failure modes; next steps |

#### Half-Day Format (3.5 hours)

| Time | Session |
|---|---|
| 09:00 – 09:15 | Opening and framing: the kitchen and the feast |
| 09:15 – 10:00 | Condensed instruction: all twelve steps, gates and roles |
| 10:00 – 10:15 | Break |
| 10:15 – 11:30 | Integrated exercise: full sequence on one real problem through Step 9 |
| 11:30 – 12:00 | Module 4 debrief: draft tool registry entry and brigade assignment for the exercise tool |
| 12:00 – 12:30 | Debrief: failure modes surfaced, accountability assigned, deployment and registry decisions |

### Workshop Exercise

Use one real business problem relevant to the participants. The exercise must produce a genuine artifact, not a simulated one. Suitable examples:

- draft a client advisory
- prepare a policy summary
- build a workflow for customer intake
- create a management briefing
- structure a risk analysis
- develop a training note

Teams work the full sequence through Step 9: define the task, set the DoD, complete the manual first pass, map the socio-technical context, use AI in bounded form, assign ownership, build the deliverable, verify it and open the pass. In Module 4, they then treat the tool used in the exercise as the subject of an organizational deployment question: would you authorize it in a tool registry, who is the AI Owner, what training would operators require and what audit event would trigger a review?

This creates behavior change, not mere agreement.

### Workshop Outputs

A properly run workshop ends with eleven tangible artifacts:

- [ ] completed task brief
- [ ] DoD checklist
- [ ] first-pass notes
- [ ] context and risk map
- [ ] AI-assisted draft
- [ ] accountability record
- [ ] validated final artifact
- [ ] short post-action review
- [ ] draft AI tool registry entry
- [ ] brigade role assignment matrix
- [ ] audit and review cycle design

Teams leave with evidence of a process, not just slides.

### Facilitator Principles

Do not reward speed alone. Reward clear framing, good constraints, quality of review, the ability to spot weak outputs and the willingness to reject plausible but unfit AI output.

The core teaching move: show that the most dangerous AI outputs are often the most fluent ones, not the most useful. Polished language is not correct analysis.

### Common Failure Modes

Surface these explicitly in every session. They are not edge cases; they are the default behavior the method is designed to replace.

- prompting before the task is clear
- treating the DoD as a formality
- skipping the manual pass
- using AI without understanding context
- failing to name an owner
- confusing polished language with correct analysis
- deploying without evidence
- omitting post-action review
- deploying tools without an authorized registry
- assuming individual training scales without brigade structure
- treating the first deployment as the governance model and never revising it

---

## Addendum: Your Restaurant

*Sustained Institutional Deployment of AI*

Slow AI Kitchen is a method for producing governed AI-assisted work. The Feast extends it to organizational deployment. But both are episodic: a task, a project, an event. They are not a permanent institution.

Running your restaurant is different. A restaurant has a fixed address. It opens every day. Its Clients return and remember. Its staff turn over. Its menu must evolve. Regulators inspect it on a schedule it does not control. Its reputation compounds (in both directions). A single bad service does not close a well-run restaurant. A pattern of bad services does.

The difference between running a feast well and running a restaurant well is the difference between project governance and program governance. The twelve-step method and its feast extension will not, by themselves, sustain an AI program at institutional scale. That requires a permanent governance, risk management and compliance architecture built on five pillars.

### 1. Governance Structure

A restaurant needs an owner, a head chef, a floor manager and clear lines of authority. An institutional AI program needs the same: a named executive accountable for the AI program, a governance body with authority to approve and revoke tool authorizations, defined escalation paths that function in practice and board or senior leadership oversight where the risk profile warrants it. Governance is not a policy document. It is a set of humans with authority, accountability and the information they need to exercise both.

### 2. Risk Management Framework

A restaurant assesses risk continuously: ingredient quality, allergen exposure, equipment failure, staff error, supply chain disruption. An institutional AI program requires the same ongoing discipline. Risk assessments must be conducted before new tools are deployed, updated when tools or use cases change and reviewed on a defined cycle. The tool registry from Step 10 is a starting point, not a substitute. A risk management framework identifies what could go wrong across the entire program, prioritizes it and assigns remediation owners. The NIST AI Risk Management Framework provides a structured, jurisdiction-neutral approach to this work: its Govern, Map, Measure and Manage functions map directly onto the program governance obligations described here. Risk that is not actively managed defaults to the person holding liability when something fails.

### 3. Regulatory Compliance

A restaurant operates under health codes, labor law and food safety regulation. It does not choose which inspections to prepare for. An institutional AI program operates under an expanding and jurisdiction-specific body of AI regulation: the EU AI Act, data protection frameworks and sector-specific obligations in financial services, healthcare and employment. Compliance is not a one-time assessment. It is an ongoing obligation that must be mapped to the program, owned by a named function and updated as the regulatory landscape shifts. Regulatory change is not a surprise event. It is a scheduled cost of operating at institutional scale.

### 4. AI Lifecycle Management

A restaurant does not serve the same menu indefinitely. Ingredients change. Suppliers fail. Dishes are retired. The menu is revised. An institutional AI program must manage the full lifecycle of each deployed system: initial authorization, version tracking as models and tools are updated by vendors, performance monitoring for drift or degradation, incident response when outputs fail and formal decommissioning when a tool is retired or replaced. ISO/IEC 42001, the international standard for AI management systems, provides a lifecycle framework purpose-built for this work, covering design, development, deployment, monitoring and continual improvement of AI systems within a governed institutional structure. A tool that was fit for deployment in year one may not be fit in year two. Lifecycle management is the discipline that catches the difference before a Client does.

### 5. Continuous Improvement

A well-run restaurant debriefs every service, adjusts its prep, retrains its staff and revises its standards. The post-action review in Step 9 and the operational debrief in Step 12 are the correct instincts at task and event scale. At program scale, those instincts must be institutionalized: a regular review cycle for the governance framework itself, a mechanism for surfacing and acting on lessons from incidents and near-misses, updated training standards as tools and risks evolve and a clear process for incorporating regulatory and technological change into program design. Continuous improvement is not a quality aspiration. It is the mechanism that keeps the program calibrated to reality rather than to the assumptions made at launch.

---

These five pillars are not a checklist. They are a description of what a permanent institution requires to operate AI responsibly over time. The twelve-step method teaches the discipline of the kitchen. The feast teaches how to scale it to an event. Your restaurant is what you build when the events become a way of life. The [restaurant resources](./restaurant-resources.md) file in this repository collects the referenced standards and explains which are load-bearing and which are signals.

No method, framework or audit standard removes the obligation to govern. It can only make governance easier to see, easier to assign and harder to avoid. The pillar that holds up every other pillar is the one the twelve-step method places at the center of every step: a named human who owns the outcome and can be held to account for it.

*The kitchen teaches discipline. The feast teaches scale. The restaurant teaches permanence.*

---

## Related Work

- **Final Liability Rests with the Human** (book, free release) and companion appendices, including the AI GRC Master Reference and the AI Audit Due Diligence Checklist: [github.com/rolldabones](https://github.com/rolldabones)
- **GRC Workbook**: [github.com/rolldabones/grc-workbook](https://github.com/rolldabones/grc-workbook)

---

## How to Cite

> Paik, Son-U Michael. *Slow AI Kitchen: Method and Workshop Guide*, v2.0. GRC Solutions Korea, 2026. https://github.com/rolldabones/slow-ai-kitchen

---

## License

This repository, including the method and all companion files, is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0). You may share and adapt this material for non-commercial purposes provided you give appropriate credit, indicate if changes were made and distribute your contributions under the same license. Commercial use requires the author's prior written permission.

Suggested attribution: "Slow AI Kitchen by Son-U Michael Paik, GRC Solutions Korea, licensed under CC BY-NC-SA 4.0."

Full license text: https://creativecommons.org/licenses/by-nc-sa/4.0/

---

## Changelog

- **v2.0 (2026-06-11):** Added linked table of contents, repository contents index, gate map, Tier Application Map, role tables, checkbox Definition of Done, Related Work, citation, license and changelog sections. Licensed the repository under CC BY-NC-SA 4.0 and added a LICENSE file. Renamed the companion files to kebab-case with .md extensions and updated the internal cross-reference in federal-workforce-literacy-bridge.md accordingly. Corrected the standard designation to ISO/IEC 42001. Consolidated to a single title block. No change to the twelve steps, the ten gates, the three tiers, the workshop design or the Your Restaurant addendum.
- **v1.0 (2026):** Initial publication: method, risk tiers, roles, workshop guide, the Feast and the Your Restaurant addendum.

---

## About the Author

Son-U Michael Paik is an attorney, AI auditor and governance architect with more than 25 years of experience designing risk and compliance systems for cross-border institutions in regulated, high-stakes sectors across Asia, Europe and the United States. He is General Counsel at BABL.ai, a global AI audit provider, and Founder and Chief Executive Officer of GRC Solutions Korea, where he advises finance, industrial and public-sector Clients on AI governance, audit readiness and regulatory compliance.

Before founding GRC Solutions Korea, Paik served as General Counsel, Chief Legal Officer and senior executive for three listed groups in Korea, including Hankook Tire, SeAH Holdings and STX Group, with responsibility for legal, compliance and trade operations across multinational businesses. Earlier in his career he practiced at Wilson Sonsini Goodrich & Rosati and Cahill Gordon & Reindel in the United States, advising on mergers and acquisitions, venture capital and cross-border regulatory matters.

He holds a Juris Doctor from Columbia Law School, a Master of Business Administration from the Yale School of Management and a Bachelor of Arts in Economics from Syracuse University. He is admitted to the New York Bar and holds AI audit certifications from BABL.ai and ForHumanity, including certifications under the EU AI Act, GDPR and the Digital Services Act, as well as senior risk management credentials under ISO 31000. He has held faculty appointments at Seoul National University, Yonsei University and Ewha Womans University, and serves in board, fiduciary and advisory roles for listed and venture-backed organizations in Korea and internationally.

Slow AI Kitchen is an expression of his central conviction: that AI governance is not a compliance exercise. It is a professional discipline. And like any discipline, it must be taught, practiced and enforced by humans who own the outcome.

**GRC Solutions Korea:** [www.grcskorea.com](http://www.grcskorea.com)
**LinkedIn:** [linkedin.com/in/sonupaik](https://linkedin.com/in/sonupaik)

---

*AI is a tool in the kitchen, not the chef.*

**Final Liability rests with the Human.**
