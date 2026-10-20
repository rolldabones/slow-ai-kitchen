# WISZOWATY'S KITCHEN

### The Architect's Practical Reference, and the Page It Does Not Have

*A standalone add-on module to Slow AI Kitchen, for readers who build, or who are learning to. Karpathy's Kitchen derives the method from what the technology is. Newton's Kitchen derives it from what the technology is permitted to do. Coetzee's Kitchen derives it from what working with the technology does to the person doing the work. Mondrian's Kitchen derives it from what the governed whole must look like. This module derives it from what the craft of building already asks of the builder, and names the one thing the builder's own reference leaves out.*

**Son-U Michael Paik**
CEO, GRC Solutions Korea
[www.grcskorea.com](http://www.grcskorea.com)

| Version | Date | Status | License |
|---|---|---|---|
| v1.0.0 | 2026-10-21 (KST) | Final | CC BY-NC-SA 4.0 (see the license convention below) |

**Final Liability rests with the Human.**

> **Doctrine.** The three doctrines engaged here, Slow AI, Informed Intent and Final Liability, are stated normatively once, in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) in the profile repository. This module sets them against the practice of software architecture. It does not vary them. Where a formulation below and DOCTRINE.md differ, DOCTRINE.md controls. Where this module compresses a doctrine, it copies the short forms of [DOCTRINE.md section 8](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#8-short-forms). GRCnext™, named in Sections III and VI, is a framework of this account, stated in the [grc](https://github.com/rolldabones/grc) repository; it is not doctrine, and this module adds nothing to it.

> **License.** The text of this module is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Suggested attribution: "Wiszowaty's Kitchen by Son-U Michael Paik, GRC Solutions Korea, licensed under CC BY-NC-SA 4.0." The book read here is the work of its author and publisher and is excluded from this grant. It is summarized, not reproduced; no passage of it is quoted.

> **Link currency.** This module cites the third-party sources listed under [Sources](#sources). The book's site, the publisher's site, Nygard's post, the Developer to Architect resources page, Conway's paper and the Team Topologies site were read on 21 October 2026 (KST). *Building Evolutionary Architectures* is cited from the book itself; the publisher's page did not load on that date. All other links are internal to the account.

**Scope note.** This module does not alter any step, gate, role or principle of the core method. It introduces no new discipline and no new gate. It reads the six-part Practical Reference that closes one short book on software architecture and sets each part against the step or gate of the method that already does the same work in a different vocabulary. Where the reference and the method agree, the agreement is evidence that the method is not governance imposed on building from outside, but a restatement of what careful builders already do. Where the reference is silent, the silence is the point of the module. The reading of the book is the author's. The book's author offered no theory of AI governance, and nothing below should be read as a claim about what he meant.

---

## Contents

- [Preface: Met Where I Am](#preface-met-where-i-am)
- [I. Purpose Before Design](#i-purpose-before-design)
- [II. The Room and the Wall](#ii-the-room-and-the-wall)
- [III. Constraints Close Options](#iii-constraints-close-options)
- [IV. Style and Debt](#iv-style-and-debt)
- [V. Four Drawings and a Sequence](#v-four-drawings-and-a-sequence)
- [VI. Tests, Then People](#vi-tests-then-people)
- [VII. The Missing Page](#vii-the-missing-page)
- [Where the Reference Lands in the Method](#where-the-reference-lands-in-the-method)
- [A Note on Provenance](#a-note-on-provenance)
- [Sources](#sources)
- [Part of the Ecosystem](#part-of-the-ecosystem)

---

## Preface: Met Where I Am

Karol Wiszowaty's *The One Minute Architect* is a short book about a job its subtitle calls the most invisible in software. It follows Joe from his first day as an architect through the questions nobody trained him for. Then, having told the story, it stops telling stories and ends in a six-part Practical Reference: the worksheets, records, diagrams and organizational patterns a working architect reaches for once the system has to be built.

The book met me where I am today: a lawyer learning to build. That is a precise claim, not a modest one. A lawyer who has spent twenty-five years in governance, risk management and compliance reads a software architect's reference and finds, part after part, instruments he already uses under other names. The Purpose Statement is a recital. The Architecture Decision Record is a board minute. Constraints versus preferences is the difference between a covenant and a wish list. A fitness function is a compliance test with the human removed from the one step where the human was never adding anything. Conway's Law is why committee charters matter.

The method this repository carries was written from the governance side of that line, under the doctrine of **Slow AI**. The reference was written from the building side. This module walks the six parts in order and shows that they arrive at the same gates. Then it turns to what the reference does not contain: a page naming the Human who answers for the system. That page is mine, and the method is where I keep it.

---

## I. Purpose Before Design

Part One of the reference begins before architecture does. It begins with Five Whys, the Toyota practice of asking why until the stated problem gives way to the real one. An architect who accepts the first statement of a problem builds a correct solution to the wrong thing. So does a lawyer who drafts to the first statement of a Client's wish.

From the real problem comes the Purpose Statement, and the reference is strict about what it may contain: why the system exists and for whom, with the measure by which success will be known. It may not contain what the system does or how. I called this **Informed Intent** by another name when I first read it, and that is a quarter right. The doctrine's instrument has four elements: purpose, authority, boundaries, exit. The Purpose Statement is the first of the four, stated the way the doctrine wants it, in terms that do not presuppose the solution and with a measure a later reviewer can apply. The method's Step 1, Define the Dish, asks the same question in the kitchen's vocabulary, and Gate 1, the Definition of Done at Step 2, is where the measure of success is written down before anything is produced. The other three elements will come up as the reference proceeds. One of them never does.

Part One then splits requirements. Functional requirements are what the system must do. They are buildable, testable and confirmable. Non-functional requirements are what the system must be, and here the reference makes an observation that belongs in every governance program: a non-functional requirement is present in every decision or absent everywhere. It is never ticked off. Security, auditability and explainability are not features that ship in a release. They are properties that either pervade the design or do not exist. A compliance checklist that treats them as items to be completed has misunderstood what kind of thing they are.

The reference asks the architect to name the tensions between requirements rather than pretend they resolve. Each function is then tested against the purpose, and what survives is the Brief: wishes out, needs in, quality first. The reference does not claim the Brief is perfect or complete. It claims the Brief is structured and honest. That is also the standard the method sets for the Definition of Done. Gate 1 does not ask for omniscience. It asks for a written statement of what done means that a reviewer can hold the output against.

Part One closes with the Architecture Decision Record. The record, in the form Michael Nygard proposed in 2011, keeps the context, the options considered, the consequences, the reasoning and the decision, with a status that moves from proposed to accepted and may later be marked superseded. The reference states its purpose plainly, and it is the auditor's purpose: so that someone who was not in the room knows why. A decision's history is part of its meaning. A decision whose history has been lost is no longer the same decision, because it can no longer be reviewed, defended or reversed on its own terms.

The method's Service Record is the kitchen's Architecture Decision Record, written by the named owner within a day of release; ten of them trigger a method review at Step 12. The architect's record and the owner's record serve the same reader, who arrives later and needs to know why.

---

## II. The Room and the Wall

Part Two moves from purpose to the domain, and it does so with people in a room. Event Storming, in Alberto Brandolini's practice, needs a wall, a supply of sticky notes, one past-tense event per note and the right people present. Events are placed in time, sorted, argued over and sorted again until the gaps appear, the actors emerge and the systems that must exist to carry the events surface on their own. The reference is clear about the output. It is not the diagram on the wall. It is the shared understanding of the people who built it. The diagram is a residue of that understanding and will be wrong within a month. The understanding is what the team carries into design.

That is Step 4 of the method, Read the Kitchen, and its gate, the socio-technical context at Gate 3. Before heat is applied, the method requires the team to know who is in the kitchen, what they already do, where the work actually flows and where it does not. The method states the gate in prose. The reference supplies a way to run it in an afternoon.

Part Two then introduces Bounded Contexts, from Eric Evans's Domain-Driven Design, and the reference's account of how they are found is the part a lawyer recognizes first. Bounded Contexts surface as vocabulary collisions. The same word means different things to two teams, and each team is correct within its own model. The reference's remedies are ownership, translation and Anticorruption Layers: decide who owns each meaning, translate explicitly at the border and build a layer that keeps one model's assumptions from leaking into the other.

Contract drafters do this with a definitions section and a precedence clause. Regulators do it with scope articles. An enterprise deploying AI across functions does it, or fails to, whenever "customer", "risk" or "approval" means one thing in the model's training data and another in the department that relies on its output. The method's Gate 3 is where those collisions are supposed to be found. The reference gives the finding a name and a cure.

---

## III. Constraints Close Options

Part Three turns to the qualities that drive design. The Architecture Characteristics Worksheet asks the architect to choose, from the long list of qualities a system might have, the few this system must have, because a system that optimizes for everything optimizes for nothing. The method makes the same demand at the Definition of Done: name the qualities the output must have, and name the ones you are prepared to trade.

The reference then draws the distinction this module turns on: Constraints versus Preferences. Law, regulation, contracts, platform, infrastructure and safety are constraints. They close options before design begins. They shape the trade-off; they do not enter it. A preference is something the architect weighs. A constraint is something the architect receives, already decided, from outside the design. The reference's instruction is that the two be separated at the start, so that no one spends a design review weighing a legal obligation against a performance target as though the two were commensurable.

In my experience it does not always go that way. Constraints are routinely demoted to preferences in practice, not by decision but by drift. A regulatory requirement is placed on the worksheet beside latency and cost, assigned a weight and traded away by a team that would never have agreed to trade it had the question been put plainly. The reference's discipline is the cure. The method's version of the same cure is the order of the steps. Steps 1 through 4 are completed before Step 5, Apply Heat, is permitted. The constraints are known before the tool is engaged, which is the only moment at which they can still close options rather than be weighed against them.

Constraints are also where the reference supplies the third element of Informed Intent's instrument, boundaries, without using the word. In GRCnext™ terms, a constraint received from outside the design is a Tolerance set by someone other than the builder. The framework is read here, not varied.

---

## IV. Style and Debt

Part Four is the architect's own ground: the choice of architectural style. The Architecture Styles Worksheet, which Mark Richards and Neal Ford built for *Fundamentals of Software Architecture*, rates candidate styles against the characteristics chosen in Part Three, and the result feeds the Architecture Decision Record. The style is a decision with a context, options and consequences, and it is recorded as one. The method has no view on architectural style. It has a view on recording the decision, and the reference takes the same view.

Part Four then takes up technical debt, and the reference's treatment is one a finance committee would recognize: debt carried deliberately. Borrow now, pay later, and know that you have borrowed. The vice is not the debt. The vice is debt that no one recorded, that accrues interest no one tracks and that comes due in a release no one planned.

The method's Step 5, Apply Heat, is bounded AI use, and the boundary is a form of debt discipline. Every output the AI produces that the Human has not yet verified is borrowed confidence. Step 8, Taste Before Service, is where the loan is repaid, in verification against something outside the model. An organization that applies heat and skips the tasting is carrying technical debt in the reference's exact sense, and is usually carrying it without a record.

---

## V. Four Drawings and a Sequence

Part Five is about drawings. Simon Brown's C4 Model gives four: Context, Container, Component and Code. Each is a level of zoom, and the reference's rule for choosing the level is the auditor's rule for choosing the level of detail in a report. The reader is shown what the reader needs to know, and need to know is for clarity, not secrecy. The Code level, the reference notes, is almost never hand-drawn. It is generated from the thing itself, because a hand drawing of code is out of date before the pen lifts.

Sequence Diagrams add behavior to structure: the participants, the messages between them, the activations and, critically, both the happy path and the hard paths. A sequence diagram that shows only the happy path is a sales document.

This is how I review contracts. The good, the bad and the ugly: what the parties intend to happen, what happens when one of them does not perform and what happens when the thing nobody planned for arrives. A contract that describes only the first is not a contract. It is a hope with signatures. The method's Step 7, Build the Plate, and Step 8, Taste Before Service, are the kitchen's happy path and hard paths. The plate is built to the Definition of Done. The tasting is where the reviewer asks what happens when the output is wrong, and whether anyone would know.

---

## VI. Tests, Then People

Part Six begins with Fitness Functions, from *Building Evolutionary Architectures* by Neal Ford, Rebecca Parsons and Patrick Kua. A fitness function is an automated check of an architectural property rather than a code property. It may be structural, behavioral or compliance-oriented. The reference's recipe for writing one is four questions. State the constraint. Ask how you would know it had been violated. Ask what would differ in the system if it had. Ask how to test for that difference automatically. Then fail the build when the test fails.

That is a legal obligation rewritten as a test, and it is the most useful page in the reference for anyone who works in governance, risk management and compliance. Most compliance controls are reviewed by a human reading a document after the fact. A fitness function reviews the system itself, continuously, and refuses to let a violating version ship. It is the practical follow-up to a pre-mortem: the pre-mortem imagines the failure, and the fitness function makes the imagined failure impossible to deploy unnoticed. In the method this is Gate 6, verification and validation, carried from Step 8 into Step 12, the operational audit and review cycle, where review stops being an event and becomes a property of the build. In GRCnext™ terms a fitness function is a Switch: a condition that stops the pipe. The framework is read here, not varied.

Then the reference turns to people, and it does so with three works that governance practitioners should know as well as architects do.

Conway's Law, from Melvin Conway's 1968 paper, holds that organizations are constrained to produce designs that are copies of their own communication structures. A system mirrors the structure of the people who built it. In AI governance, risk management and compliance the consequence is direct: an oversight committee whose members share one background will produce oversight with that background's blind spots built in. Diversity of lived experience on an oversight body is not a courtesy. It is an architectural property of the oversight, and Conway's Law says it will show up in the system whether or not anyone intended it.

Team Topologies, from Matthew Skelton and Manuel Pais, gives the organizational vocabulary the reference adopts: stream-aligned, platform, enabling and complicated-subsystem teams; collaboration, X-as-a-Service and facilitating as the modes in which they interact; and the Inverse Conway Maneuver, which is the deliberate shaping of the organization so that the system it produces has the structure you want. Step 11 of the method, Staff the Brigade, is an Inverse Conway Maneuver for the governed deployment of AI. The brigade is staffed so that the output has the properties the Feast requires.

Cognitive Load closes the reference. John Sweller's three forms, intrinsic, extraneous and germane, are the reason platform teams exist. Intrinsic load belongs to the problem and cannot be removed. Extraneous load is imposed by the environment and can be. Germane load is the effort of actually learning and deciding. Cut the extraneous so that the team can carry more of the germane. Platform teams absorb extraneous load so that stream-aligned teams can spend their attention on the domain.

This is a structural fix, and it applies to agentic workers as it applies to human ones. An agent given a bounded service, a clear ticket and a receipt to return, which is what the method's agent companion specifies, is an agent whose extraneous load has been cut by design. The failure modes the method guards against at Step 5 are, in Sweller's terms, extraneous load that has been allowed to crowd out the germane.

---

## VII. The Missing Page

Six parts. Purpose, domain, qualities and constraints, style and debt, drawings, tests and people. The reference is good, and its agreement with the method is close enough that a reader could conclude the method is redundant for anyone who owns the reference.

It is not, and the reason is one page the reference does not have.

Nothing in the six parts names the Human who answers for the system. The Purpose Statement names the people the system is for. The Architecture Decision Record preserves the decision and its reasoning. Event Storming puts the right people in the room. Team Topologies organizes the people who build and run the system, and Conway's Law explains why their arrangement matters. Not one of these instruments records who had the authority to release the system, who is accountable when it causes harm and who holds that accountability through the period of reliance. The reference describes, with care, how good decisions are made and recorded. It does not say who answers for them.

In the vocabulary of Section I, the reference supplies purpose and boundaries and never arrives at authority. That is not a defect in the book. It is a boundary of the craft the book describes. Software architecture is a discipline of structure, and accountability is not a structure. It is a relationship between a system and a person, and establishing that relationship is what the method exists to do. The doctrine states it in one sentence: Final Liability rests with the Human: every material outcome attaches to a named human owner with decision rights, oversight and the power to intervene. The owner is named at specification, attaches at confirmation, holds through reliance. Step 6 of the method, Name the Chef de Partie, is Gate 5, the point at which that Human is named before the output moves. Step 9, Open the Pass, is Gate 7, the point at which that Human releases it, with no model in the room.

The reference ends with cognitive load. The method begins where the reference ends, with the one load that cannot be delegated to a platform team or cut by design: answering for the system. That page is mine. The method is where I keep it.

---

## Where the Reference Lands in the Method

The module adds no discipline and no gate. It supplies a correspondence, and the correspondence maps onto the method as it stands.

**Part One, Purpose,** is Step 1 (Define the Dish) and Gate 1 (Definition of Done, at Step 2). The Purpose Statement is the purpose element of Informed Intent; the Brief is the Definition of Done; the Architecture Decision Record is the Service Record's ancestor.

**Part Two, Domain,** is Step 4 (Read the Kitchen) and Gate 3 (Socio-Technical Context). Event Storming is a way to run the gate. Bounded Contexts name what the gate is looking for.

**Part Three, Qualities and Constraints,** is Gate 1 and the order of Steps 1 through 4 before Step 5. Constraints close options before the tool is engaged, which is the only moment at which they can.

**Part Four, Style and Debt,** is Step 5 (Apply Heat, Gate 4, Bounded AI Use) read as debt discipline, with Step 8 (Taste Before Service, Gate 6) as repayment.

**Part Five, Drawings,** is Step 7 (Build the Plate) and Step 8 (Taste Before Service): the happy path built to the Definition of Done, the hard paths exercised in verification.

**Part Six, Tests and People,** is Gate 6 (Verification and Validation) carried into Step 12 (Run the Event, Gate 10, Operational Audit and Review Cycle) for fitness functions, and Step 11 (Staff the Brigade, Gate 9) for Conway's Law, Team Topologies and cognitive load.

**The missing page** is Step 6 (Name the Chef de Partie, Gate 5, Final Liability) and Step 9 (Open the Pass, Gate 7, Human Release Decision). The reference has no instrument at either gate. The method has nothing else at either gate.

---

## A Note on Provenance

In the spirit of Coetzee's Kitchen, the lineage of this module is stated.

I read the book in October 2026, as a lawyer learning to build, and found it excellent. I have not built a system of the scale the book's architect builds. I have designed six AI governance, risk management and compliance management systems from scratch and audited others, and the correspondences in Sections I to VI are the ones that presented themselves from that side of the line. A working architect may find others, or find mine forced in places. The mapping onto the steps and gates is mine. The book makes no reference to this method, and its author has no connection to it.

The module began as a LinkedIn post. It was expanded in conversation with an AI system against the repository's existing derivation modules, and the external sources were checked on the date stated in the link-currency note. The AI system did not read the book. The book's contents as summarized here rest on my reading, and I reviewed the expansion against the book before release; where the summary is wrong, the error is mine. The published sources for each practice are cited so that a reader can test the practices against their originals rather than against the book or against me.

Cognitive Provenance asks which conclusions are the Human's and which arrived from the machine. The six correspondences and the missing page were in the post before any machine was engaged. The prose that carries them was drafted with one and reviewed by me. The sentence the module turns on, that nothing in the reference names the Human who answers for the system, was the reason the post was written. One thing changed in the expansion: the machine pointed out that the Purpose Statement answers to one of Informed Intent's four elements, not to the doctrine entire, and Section I now says so. That correction is the machine's, and it made the missing page easier to name.

---

## Sources

- Karol Wiszowaty, *The One Minute Architect: The Story of the Most Invisible Job in Software* (Arpeggia, 234 pp., ISBN 978-83-982636-0-3). Book site: https://theoneminutearchitect.com/ ; publisher: https://arpeggia.studio/ . The six-part Practical Reference and its contents are summarized from the author's reading; no passage is quoted.
- Five Whys: attributed to Sakichi Toyoda; popularized by Taiichi Ohno, *Toyota Production System: Beyond Large-Scale Production* (Diamond, 1978; English edition, Productivity Press, 1988).
- Architecture Decision Records: Michael Nygard, "Documenting Architecture Decisions," 15 November 2011: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions . Nygard's statuses are proposed, accepted, deprecated and superseded.
- Event Storming: Alberto Brandolini, *Introducing EventStorming: An Act of Deliberate Collective Learning* (Leanpub): https://leanpub.com/introducing_eventstorming
- Bounded Context, Anticorruption Layer, Shared Kernel, Open Host Service: Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Addison-Wesley, 2003).
- Architecture Characteristics Worksheet and Architecture Styles Worksheet (the latter by Mark Richards and Neal Ford, for *Fundamentals of Software Architecture*, O'Reilly, 2020): https://developertoarchitect.com/resources.html
- C4 Model: Simon Brown: https://c4model.com
- Fitness Functions: Neal Ford, Rebecca Parsons and Patrick Kua, *Building Evolutionary Architectures: Support Constant Change* (O'Reilly, 2017); second edition, with Pramod Sadalage, *Building Evolutionary Architectures: Automated Software Governance* (O'Reilly, 2022).
- Conway's Law: Melvin E. Conway, "How Do Committees Invent?" *Datamation*, April 1968: https://www.melconway.com/Home/Committees_Paper.html
- Team Topologies, Inverse Conway Maneuver and cognitive load as applied to teams: Matthew Skelton and Manuel Pais, *Team Topologies: Organizing Business and Technology Teams for Fast Flow* (IT Revolution, 2019; a second edition is announced on the authors' site): https://teamtopologies.com/
- The three forms of cognitive load: John Sweller, "Cognitive Load During Problem Solving: Effects on Learning," *Cognitive Science* 12(2), 1988, pp. 257–285.
- Informed Intent and Final Liability, with Slow AI: [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), and this repository.

---

## Part of the Ecosystem

This module is part of the rolldabones ecosystem, mapped in [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md). Nearest neighbors:

- [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md): the single normative statement of the three doctrines this module sets against the architect's reference. Where a formulation here and DOCTRINE.md differ, DOCTRINE.md controls.
- [grc](https://github.com/rolldabones/grc): GRCnext™ and its five primitives, two of which, Tolerances and Switches, are read in Sections III and VI; this module adds nothing to that framework.
- [enterprise-ai-architecture-primer.md](./enterprise-ai-architecture-primer.md): the repository's own architecture reference, with the artifact templates this module's correspondences would be filled into.
- [karpathys-kitchen.md](./karpathys-kitchen.md): the technical warrant: the method derived from the mechanisms of the technology.
- [newtons-kitchen.md](./newtons-kitchen.md): the conceptual warrant: the three doctrines as three laws of consequential motion.
- [coetzees-kitchen.md](./coetzees-kitchen.md): the epistemic warrant, and the source of the two disciplines, Return to Source and Cognitive Provenance, that the provenance note above applies to this module itself.
- [mondrians-kitchen.md](./mondrians-kitchen.md): the compositional warrant: the governed whole seen before it is built one gate at a time. Mondrian's Kitchen shows the picture; this module shows the builder's instruments that produce it, and the one the builder does not have.
- [take-out-delivery-and-vending-machines.md](./take-out-delivery-and-vending-machines.md): the agent companion, whose service ticket and receipt are the cut in extraneous load that Section VI describes.
- [service-record.md](./service-record.md): the kitchen's Architecture Decision Record, written by the named owner.
- [README.md](./README.md): the canonical method this module serves. Every other file defers to it.

---

**Final Liability rests with the Human.**
