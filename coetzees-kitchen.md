# COETZEE'S KITCHEN

### His Man and His Machine: On AI, Representation and the Strange Question of Who Is Writing Whom

*A standalone add-on module to Slow AI Kitchen, for readers who want the epistemics of the working session rather than only the mechanics of deployment. Karpathy's Kitchen derives the method from what the technology is. Newton's Kitchen derives it from what the technology is permitted to do. This module derives it from what working with the technology does to the person doing the work.*

**Son-U Michael Paik**
CEO, GRC Solutions Korea | former General Counsel, BABL AI
[www.grcskorea.com](http://www.grcskorea.com)

| Version | Date | Status | License |
|---|---|---|---|
| v1.0.0 | 2026-08-30 (KST) | Final | CC BY-NC-SA 4.0 (see the license convention below) |

**Final Liability rests with the Human.**

> **Doctrine.** The three doctrines engaged here, Slow AI, Informed Intent and Final Liability, are stated normatively once, in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md) in the profile repository. This module restates them at the altitude of the working session. It does not vary them. Where a formulation below and DOCTRINE.md differ, DOCTRINE.md controls. **Return to Source** and **Cognitive Provenance**, introduced below, are disciplines of this module, not doctrine: they operationalize the doctrines inside the human-AI loop and state no rule of their own.

> **License.** The text of this module is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Suggested attribution: "Coetzee's Kitchen by Son-U Michael Paik, GRC Solutions Korea, licensed under CC BY-NC-SA 4.0."

> **Link currency.** This module cites the third-party sources listed under [Sources](#sources). External links were checked on 29 August 2026 (KST). All other links are internal to the account.

**Scope note.** This module does not alter any step, gate, role or principle of the core method. It supplies the epistemic warrant for three of the method's standing gates, verification, context and intent, by naming the problems they answer: the report is not the world, the report lands in a system and the report changes its reader. It borrows two things from Coetzee's lecture: its unresolved question of who is writing whom, and its opening emblem, the decoy ducks of the Lincolnshire fens. It makes no claim to settle the lecture's meaning, and no reading offered here should be attributed to its author. It takes no position on the philosophical status of AI systems; it governs the practical consequences of working with them. It works at the altitude of the single deployment, the pond rather than the fens; the technology's societal scale enters only where it reaches into the session. It assumes no other module and requires none.

---

## Contents

- [Preface: Coetzee's Inversion](#preface-coetzees-inversion)
- [I. The Report Is Not the World](#i-the-report-is-not-the-world)
- [II. The Decoy Pond](#ii-the-decoy-pond)
- [III. Return to Source](#iii-return-to-source)
- [IV. The Stranger Problem](#iv-the-stranger-problem)
- [V. The Machine Begins to Write the Human](#v-the-machine-begins-to-write-the-human)
- [VI. Cognitive Provenance](#vi-cognitive-provenance)
- [VII. Informed Intent](#vii-informed-intent)
- [VIII. Slow AI](#viii-slow-ai)
- [IX. Final Liability](#ix-final-liability)
- [X. Governing the Loop](#x-governing-the-loop)
- [XI. His Man and His Machine](#xi-his-man-and-his-machine)
- [XII. One More Turn of the Screw](#xii-one-more-turn-of-the-screw)
- [Where the Disciplines Land in the Method](#where-the-disciplines-land-in-the-method)
- [Sources](#sources)
- [Part of the Ecosystem](#part-of-the-ecosystem)

---

## Preface: Coetzee's Inversion

> *But to return to my new companion. I was greatly delighted with him, and made it my business to teach him everything that was proper to make him useful, handy, and helpful; but especially to make him speak, and understand me when I spoke; and he was the aptest scholar there ever was.*
>
> Daniel Defoe, *Robinson Crusoe*. The epigraph Coetzee set at the head of the lecture.

I came to this question by way of an excellent Pursuit of Wonder video:

Pursuit of Wonder, ["This Nobel Prize Winner Has a Really Strange Theory About the Mind"](https://youtu.be/BrxheXPuCJ4)

The video takes up a Nobel lecture unlike any other. In Stockholm in December 2003, where laureates customarily reflect on a life in literature, J. M. Coetzee instead read a story, *He and His Man*, and the video reads that story as a parable about the self, language and reality: about the distance between the one who lives and the one who narrates, and about language as a decoy that can lead its hearers where they did not choose to go.

I say I came to this question by way of the video, but let me be more precise. I did not find the video; the video found me. A recommendation algorithm, having watched what I watch, decided I should see it, and the video has been retitled at least once since then, so even the door I came through has not held still. The first machine in this essay's lineage appears, in other words, before its first thought. The video sent me back to Coetzee, and then, perhaps inevitably these days, it sent me to AI.

There is something wonderfully unsettling in *He and His Man*. Coetzee returns to Robinson Crusoe, but not quite to Daniel Defoe's Robinson Crusoe; the relationship between character and author has somehow been turned around. Crusoe is old now, done with the sea, keeping a room above the Bristol waterfront, and "his man" travels the kingdom sending him reports of what he sees: the decoy ducks of the Lincolnshire fens, an engine of execution in Halifax, London in the year of the plague. People and places and stories.

Or so it appears. Because Coetzee also shows us Crusoe at his desk in the evenings, sharpening his quills, writing a page or two of his man. The reports arrive, and Crusoe writes them, and the lecture declines to settle which.

Except, of course, we know something Crusoe apparently does not. Coetzee never names the man; he gives him a quick step, a mole on the chin, a tradesman's history and an able pen. His man resembles Daniel Defoe. Defoe created Crusoe. Yet Coetzee has somehow placed the creation in a position from which he contemplates the creator, and the creation writes better: Crusoe marvels that this man of his, "a kind of parrot" he never taught, turns phrases his own pen could not reach, and admits that the words come only when he gives himself over to his man.

Who, then, is the author and who is the character? Who is master and who is servant? Who is observing the world, and who is constructing the story through which the other understands it?

Coetzee refuses to make the relationship comfortable. Toward the end he has Crusoe wonder what the two of them actually are to one another, master and slave, brothers, comrades or enemies, and he offers no answer. The lecture closes with the two of them as deckhands on ships passing close in rough weather, one bound west, the other east, near enough to hail, each too taken up with the rigging to raise a hand.

They never meet.

And Coetzee set Defoe's own words at the head of it all: Crusoe teaching his new companion to speak, and to understand when spoken to, the aptest scholar there ever was. We have lately made a companion of our own and taught it, above all, to speak.

That unsettled question is the one we need now, for thinking about our relationship with Artificial Intelligence (AI). Because when we work seriously with AI, something similarly peculiar begins to happen.

At first the relationship looks simple.

**Human → AI → Output**

I have an idea; I instruct the machine; the machine produces something; I evaluate it. I am the principal and AI is the agent. I am Crusoe, and AI is His Man. There is considerable truth in that description, and I think we should preserve it, particularly when allocating responsibility. But it is not the whole story. There are at least two complications. The first is that His Man never actually brings us the world; he brings us a report about the world. The second is stranger: after listening to His Man for long enough, Crusoe himself begins to change.

## I. The Report Is Not the World

Suppose I ask an AI system to analyze a contract.

There is, somewhere underneath the exercise, an actual commercial relationship. There are parties, people, histories. There are negotiations, incentives and bargaining power; emails, telephone calls and drafts; things remembered, things forgotten and things deliberately left unsaid. There are applicable laws and institutional practices, personalities and money, deadlines and consequences. There is, in other words, a messy reality, and the contract is already a representation of some portion of it.

Then I select the contract and perhaps other documents and give them to an AI system. I add a prompt describing what I believe matters, I formulate questions and I provide some facts while omitting others, consciously or unconsciously. The model receives that representation and produces another, and I read the output and construct my own understanding from it.

So what looked like

**Human → AI → Output**

is actually closer to

**Reality → Human Perception → Language → Context → AI Interpretation → AI Output → Human Interpretation**

Every arrow matters, and every arrow can lose something.

That loss need not involve a hallucination, and this may be one of the more important mistakes we make when thinking about AI reliability: we tend to focus on whether the model has said something false. But imagine that every statement in the AI's answer is true. The answer may nevertheless be misleading. Perhaps I omitted a document, or a critical conversation was never written down, or the legal authorities I supplied were incomplete. Perhaps my initial framing caused the model to treat as a problem of contract interpretation what was really a problem of commercial leverage. Perhaps the available data captured what could easily be measured while leaving out what actually mattered. Perhaps I simply asked the wrong question.

The model can reason beautifully from the world it has been given while that world remains importantly different from the world in which the decision must be made. That is not necessarily model failure. It may be representation failure.

And AI makes representation failure unusually dangerous because AI is so good at producing coherence. A beautifully structured answer feels complete. Specificity feels like knowledge, a table feels like coverage, a citation feels like proof and a confident synthesis feels like understanding. The representation becomes increasingly pleasant to inhabit, and eventually, if we are not careful, we stop noticing that it is a representation.

Coetzee's lecture opens on an emblem of exactly this. The first report concerns the decoy ducks, the duckoys, of the Lincolnshire fens: tame ducks sent abroad each season to tell the ducks of Holland and Germany, in their own tongue, of an England with open water, quiet ponds, corn the gleaners left behind and hardly any frost. Representation is the lecture's own word for what the duckoys offer. The foreign ducks follow the picture home, led up waterways that narrow by the day, reassured at every turn of how well they will live, until the net closes over the water.

The particulars were true. England has such shores, such ponds, such corn.

What the report left out was the net.

So the first principle I take from all of this is quite simple: never confuse the report with the world.

## II. The Decoy Pond

Stay in the fens a moment longer, because the duckoys' story, by itself, kills nothing. A tale of English abundance, told in duck language on a frozen Dutch river, is only a tale. What kills is the assembly around it: decoys bred in the ponds and fed by hand; the season chosen for the crossing; the fen-men waiting hidden in the reeds; corn scattered on the water at the right moment; waterways that narrow by design; the arched nets; the trained dog, sent in at the end; and beyond the pond, a market that buys fowl in the hundreds and the thousands, which is why the whole apparatus exists. Remove any piece and the representation is just a story. Together they are a system.

And the system is the trap.

There is a name for this kind of arrangement: a socio-technical system. Technique and technology embedded in people, practices, incentives and institutions, such that the behavior of the whole emerges from their interaction, and neither the tools nor the humans explain the outcome alone. The name comes out of the English coal mines just after the Second World War, where researchers from the Tavistock Institute, one of whom had been a miner himself, studied pits in which new machinery kept underperforming and found that the machines had broken up the small self-regulating work groups the coal was actually won by. Productivity did not live in the equipment, and it did not live in the men. It lived in the joint system. Seventy-five years later the finding transfers intact.

Every AI deployment is a decoy pond in this one respect. A model considered alone can only talk. It becomes consequential when it is deployed: connected to data, given instructions, granted tools and permissions, wired into workflows and placed among people who will act on what it says. And those people bring the rest of the system with them. Their training or the lack of it. Their incentives and their deadlines. Their fatigue at four in the afternoon. Their standing in the organization and their fear for it. The customs of the institution around them: what gets questioned here, what gets waved through, who is allowed to say stop.

The same model is therefore safe in one deployment and dangerous in another. A drafting assistant whose output crosses a careful reviewer's desk is one system; the same assistant wired to send is a different system with the same model inside it. A screening model treated as one input by a trained officer with time is one system; the same model treated as the decision by an exhausted officer at the end of a quota is another. Automation bias, the human habit of deferring to the confident machine, is not a property of the model at all. It is a property of the deployment, of training, workload, incentive and culture.

It lives in the kitchen, not in the knife.

This is why evaluating the model alone is never enough. To audit only the model is to audit the duckoys' story and ignore the men in the reeds. Section I said that the representation supplied to the machine comes from a socio-technical world, with its omissions and its leverage and its things left unsaid; this section says that the output returns into one. The report must answer not only to the world it describes but to the system it lands in.

The ducks did not die of a false sentence. They died of an unmapped system.

A note on the word, because the auditor and the scholar share it at different altitudes. In AI assurance, socio-technical is the working term for exactly this inspection: NIST's AI Risk Management Framework describes AI systems as "inherently socio-technical in nature," influenced by societal dynamics and human behavior, and an audit worth the name examines the workflows, the training, the incentives and the human-in-the-loop structure around the model, not the code alone. The scholarly literature uses the same word one level up, for whole societies of ponds: socio-technical systems, regimes and transitions, the study of how a technology and a society remake each other. A variant, socio-technological, sometimes appears in the societal register, but I can find no settled division of labor between the suffixes, and minting one would be a small decoy of its own. His man notes in passing that fen is an English word and stays home, although wetlands are everywhere. The distinction that matters is not in the suffix. It is in the unit of analysis.

One pond is a deployment. It has an owner, a specification, gates and records that can be audited, and everything in this module and in the method it serves applies there. The fen country is the technology at large: thousands of ponds, the market that makes them worth digging, the practice spreading from county to county, and no single owner anywhere. At that scale governance stops being a specification and becomes law, standards, professional norms and, not least, the private discipline of attention each of us brings to our own feeds. This module works at the scale of the pond. But the fens keep reaching into it: the recommendation engine that chooses what a professional reads before the session opens, the ambient assistants of Section IV, the customs one industry imports from another. The disciplines below are built to notice fen-scale forces when they arrive at pond scale, which, as Section XII will confess, is exactly how this essay began.

So for consequential AI the question is never only what the model said. It is also what the system around it will do with the saying.

## III. Return to Source

Both questions suggest a practical discipline. Call it **Return to Source**.

For consequential decisions, we should retain the ability to move backward through the chain:

**Conclusion → Evidence → Source → Observable Reality**

And observable reality, at the end of that chain, is not a database. It is the fens: the deployment, the people, the incentives, the place where the decision must live.

The greater the consequence, the stronger the obligation to make that journey. This does not mean verifying every sentence an AI system produces; if that were necessary, much of the utility of AI would disappear. It means making verification proportional to consequence. If I ask AI to improve the wording of an inconsequential email, the threshold can be low. If I ask it whether a particular clause creates a US$100 million exposure, the threshold should be rather higher. And if an AI system is involved in deciding whether someone receives a loan, loses a job, undergoes a medical procedure, is investigated for misconduct or is denied some important opportunity, we should expect stronger evidence and stronger pathways back to reality still.

This is where AI governance can become overly preoccupied with the model. The model is only one part of the epistemic chain, and a perfectly functioning model operating on a defective representation can produce a perfectly reasoned answer to the wrong world. The control objective therefore cannot simply be whether the AI is accurate. It must also be whether the representation supplied to the AI corresponds sufficiently to the reality in which the decision will have consequences.

That is a harder question. But it is the more important one.

## IV. The Stranger Problem

If that were the whole lesson, this would largely be an essay about checking, about representations and the systems they land in. But Coetzee's puzzle points somewhere more interesting.

The simple model of AI collaboration assumes that the human remains essentially unchanged while the machine performs work on the human's behalf. That is not my experience of working seriously with these systems. I begin with an idea and ask AI to examine it. The model develops the idea, perhaps drawing a distinction I had not considered. I read the distinction, and now I understand my original idea differently, so I formulate another question. But the person asking that second question is not quite the person who asked the first. The AI responds again, and that response changes my understanding again. And so the real interaction looks something like this:

**Human → AI → Human′ → AI′ → Human″ → AI″ → …**

The primes matter. The human coming out of each interaction is not quite the human who went into it.

This is not a defect; it is much of the reason to use AI. We have always sought out things that change our thinking. We read books, we hire teachers, we consult experts and we argue with colleagues. We send drafts to people whose judgment we respect precisely because we hope the draft that comes back will alter the draft in our heads. Civilization itself depends on people placing thoughts into one another's minds, and AI belongs somewhere in that tradition.

But it introduces something new in degree, and perhaps eventually in kind. It operates at extraordinary speed and it is indefinitely patient. It can participate at the moment a thought is being formed. It can propose ten alternatives before I have fully formulated one and summarize a thousand pages before I have read twenty. It can reorganize my notes, challenge my assumptions, invent taxonomies, supply analogies, identify counterarguments and convert a vague intuition into a beautifully articulated proposition.

And it is ceasing to be an occasion. The loop used to be a session: you sat down to it, and it ended. Increasingly the machine is ambient, in the feed that decides what we see, in the document as we type, in the meeting as we speak, in the agents left running overnight and, with memory, carrying yesterday's interaction into today's. The loop is becoming an environment. Which is why we need to understand what the loop does to us, most of all, now.

And then something interesting happens.

I start using the proposition.

## V. The Machine Begins to Write the Human

AI does not merely give us answers. It gives us categories. It tells us which similarities deserve attention and suggests what should be compared. It identifies what appears salient, compresses complexity into labels and gives names to things we had sensed but had not articulated. Those names then become available to us. We use them in the next prompt, and the next memorandum, and the next meeting, and eventually they may become part of how we understand the problem.

Our creation has begun participating in our creation.

Again, this is not necessarily bad; a good concept should change the person who encounters it. But there is a governance issue here that is subtler than hallucination. The machine does not have to persuade us of something false. It can influence the frame within which we decide what is worth asking whether it is true.

That is considerably more powerful. An incorrect factual assertion can be checked. A framing assumption may never present itself as an assertion at all; it simply determines what enters the analysis. What is important and what is irrelevant. What counts as risk and what counts as success. Which stakeholder matters, which time horizon, which alternative, which evidence, which question.

If AI increasingly participates in constructing those categories, then governing AI output alone is insufficient. We also need to pay attention to what happens to the human during the interaction.

## VI. Cognitive Provenance

We already understand the importance of provenance in information systems. Where did this data come from, who collected it, has it been altered, what is the authoritative source, and can we trace the conclusion back to evidence? AI adds another provenance problem. Not merely the provenance of information.

The provenance of thought.

Call it **Cognitive Provenance**.

Where did this framing come from?

Who introduced this assumption?

What placed the question in my path at all?

Was this distinction mine or the model's?

Did the model identify this risk or did I?

What did the model cause me to notice, and what did its summary cause me not to notice?

Did I define the objective before beginning the interaction, or did the objective gradually emerge from the interaction itself?

Would I have reached this conclusion without the model? Would another model have led me toward a different one? Would another human?

These questions should not become rituals, and they should not become a strange attempt to protect human thought from contamination by machines. Human thought has never been pure in that sense. My ideas contain traces of teachers, books, colleagues, clients, mistakes, arguments, cultures and experiences accumulated over decades, and often I could not possibly identify where a particular idea originated. The objective is not purity. It is visibility where visibility matters.

For consequential decisions, we should be able to understand not only the evidentiary lineage of the answer but, to an appropriate degree, the intellectual lineage of the decision. That becomes particularly important when AI has participated materially in defining the problem rather than merely answering it.

## VII. Informed Intent

This brings me back to something I have been calling **Informed Intent**. Before beginning consequential AI-assisted work, we should articulate what we are trying to do.

What is the objective?

What are the constraints, and what assumptions are we making?

What evidence matters, and what is outside scope?

What would count as success, and what would cause us to stop?

What requires escalation, and what must remain a human decision?

This is not merely good prompting. It is a governance control. If we do not know our intent before entering the recursive human-AI loop, something else can happen: the system we asked to help us achieve an objective can gradually help us determine what the objective was. That is not necessarily improper, since discovery is often the point of intellectual work. But there is a material difference between deliberately revising an objective because new information warrants it and simply drifting into a new objective because the interaction carried us there.

The former is learning. The latter may be loss of control.

Informed Intent therefore establishes the human starting point. Not an immutable starting point, but a visible one. If the destination changes, we should be able to notice that it changed.

## VIII. Slow AI

This also gives me a different way of understanding **Slow AI**.

Slow AI is not about making AI slow. That would be futile. AI systems will become faster, agents will perform more steps, context windows will expand and models will consume more information and produce more analysis in less time. The machine is unlikely to be the bottleneck.

We are.

Human attention is finite. Context is finite, our ability to switch between problems is finite and our capacity to interrogate ten simultaneously operating agents is finite. Our ability to notice when an assumption has quietly shifted is very finite indeed.

Slow AI therefore means something different. It means creating enough structure around fast machines for humans to retain meaningful judgment. It means governing the loop. Ask, look and listen. Challenge and compare. Return to source, and notice when the question changes. Preserve provenance when consequence warrants it, insert friction where friction creates judgment and create gates where the next step is difficult to reverse.

Slow AI is therefore less a speed limit than an architecture of attention. The machine may operate in milliseconds.

The decision does not have to.

## IX. Final Liability

Eventually, however, the recursive loop must end. Something must happen in the world. A contract is signed and money moves. A person is hired, a transaction closes, a product launches, a system is deployed. A claim is made; someone is denied something; someone is given something. A decision becomes consequential.

At that point, someone must be able to step outside the human-machine loop and say: this is the decision, these are the reasons, and I own it.

That is **Final Liability**.

**Final Liability rests with the Human.**

Not because humans are always wiser than machines; plainly, we are not. Not because human reasoning is unbiased; it is not. Not because human judgment is somehow pristine; history rather decisively disposes of that proposition. Final Liability rests with the Human because governance ultimately requires a principal who has authority, responsibility and the capacity to intervene in the world where the consequences occur.

The human cannot discharge that responsibility by pointing backward into the recursive loop and saying that the AI recommended it. That is not accountability. It is an attribution of causation masquerading as one.

## X. Governing the Loop

Put together, the architecture begins to look quite simple:

**Informed Intent → Slow AI → Final Liability**

Informed Intent governs entry, Slow AI governs the interaction and Final Liability governs exit. And two complementary disciplines run through the whole process. Return to Source protects the connection between representation and reality; Cognitive Provenance protects visibility into how the human-machine interaction shaped the reasoning itself. One looks outward and asks whether this account is sufficiently connected to the world. The other looks inward and asks what this interaction has done to the person making the decision.

And all of it runs somewhere. Intent is declared, the loop turns and liability is owned inside a socio-technical system, among incentives, workloads and customs the specification never fully captures. The architecture is only as strong as the deployment that carries it, which is why mapping the system is not a preliminary. It is part of the governance.

Together, the disciplines address the two problems with His Man. His reports may not be the world.

And his reports may change his master.

## XI. His Man and His Machine

Which brings us back to Coetzee. The interesting question is not simply whether Crusoe can trust the reports arriving from His Man. It is who His Man is becoming to Crusoe. Servant, agent, author, collaborator or adversary? Or a source through which Crusoe increasingly encounters a world he does not directly see?

Calling AI "just a tool" does not quite capture this. A hammer does not ordinarily suggest that the carpenter reconsider the architecture of the house. A calculator does not normally propose a different objective for the calculation. A word processor does not usually tell the writer that the essay would be more interesting if it were about something else.

AI can.

Yet the opposite mistake would be equally serious. We need not anthropomorphize AI into another human mind in order to recognize that the relationship is unusual, and we do not have to settle the philosophical status of the machine before we can govern the practical consequences of working with it. We can govern the verb, the boundary and the consequence. We can preserve the distinction between representation and reality, maintain pathways back to source and preserve, where it matters, the provenance not merely of evidence but of thought. And we can insist that somewhere at the end of the chain stands a human being capable of saying: I have considered this; I understand sufficiently where it came from; I have returned to the world where necessary; and I am prepared to act on it.

## XII. One More Turn of the Screw

There is, of course, one final complication. This essay is itself an example of the thing it describes.

A recommendation algorithm, trained on my viewing, placed a Pursuit of Wonder video in front of me, and I watched it. The video caused me to encounter Coetzee's *He and His Man* differently, and Coetzee changed the question I was asking. I brought that question into a conversation with an AI. The AI proposed connections; I accepted some, rejected others and reframed several. The interaction changed my understanding of the original video, which changed the essay. And now the essay may change the next thing I ask the machine.

The provenance therefore looks something like:

**Defoe → Crusoe → Coetzee → Pursuit of Wonder → Recommendation Algorithm → Human → AI → Human′ → Essay**

And even that is a simplification, which is precisely the point.

Notice, too, where the chain now starts moving on its own. Before I had a question, a machine had already chosen what I would notice. Cognitive Provenance, it turns out, begins earlier than the first prompt: the question of who introduced this frame now includes the recommendation engine that placed the frame in my path before I had formed any intent at all. Which is one more reason to declare the starting point when consequential work begins. Not because we control the road that brought us there.

Because we do not.

Perhaps we are entering an era in which authorship becomes increasingly recursive. The important question may therefore not be the one we have spent so much time asking, whether machines can think like us. The more immediate question may be what happens to us when we think with machines. Coetzee's strange inversion gives us an excellent question with which to approach that future:

Who is writing whom?

Slow AI does not pretend to supply a final philosophical answer. It supplies something more practical: a discipline for living with the question.

Never confuse the report with the world.

Never forget the system the report lands in.

And do not merely govern what the AI produces. Govern what happens to the human while producing it.

---

## Where the Disciplines Land in the Method

The module adds two named disciplines and no new gates. They land inside the method as it stands.

**Return to Source** is the discipline of Gate 2 and Gate 6. Step 3 (Knife Work) establishes direct contact with the source material before the machine touches it, which is what makes the journey backward possible later. Step 8 (Taste Before Service) is where the journey is made, and the risk tiers already say how far to travel: verification proportional to consequence is the tier logic stated as an epistemic rule.

**Cognitive Provenance** is the discipline of Gate 1 and Gate 7. Steps 1 and 2 (Define the Dish, Mise en Place) record the human starting point, which is Informed Intent doing its work: the objective is visible before the loop begins. Step 9 (Open the Pass) then asks the provenance question in its operational form: is the objective this output serves the objective the session opened with, and if it moved, did it move deliberately, on the record, or did the interaction carry it there.

The socio-technical section is not a third discipline. It is Gate 3 stated as an argument: Step 4 (Read the Kitchen) already requires the system around the machine to be mapped, the people, incentives, workflows and customs the output will land among, before the machine is put to work at Step 5. The Decoy Pond supplies the reason that gate exists.

It changes no step, gate, role or principle.

---

## Sources

- Pursuit of Wonder, "This Nobel Prize Winner Has a Really Strange Theory About the Mind," YouTube: https://youtu.be/BrxheXPuCJ4
- J. M. Coetzee, "He and His Man," Nobel Lecture in Literature, delivered at the Swedish Academy, Stockholm, 7 December 2003: https://www.nobelprize.org/prizes/literature/2003/coetzee/lecture/
- Daniel Defoe, *Robinson Crusoe* (1719). The epigraph above is Defoe's text as Coetzee set it at the head of the lecture.
- E. L. Trist and K. W. Bamforth, "Some Social and Psychological Consequences of the Longwall Method of Coal-Getting," *Human Relations* 4(1), 3-38 (1951), the study that founded the socio-technical systems field: https://journals.sagepub.com/doi/10.1177/001872675100400101
- National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023, which characterizes AI systems as inherently socio-technical in nature: https://doi.org/10.6028/NIST.AI.100-1

---

## Part of the Ecosystem

This module is part of the rolldabones ecosystem, mapped in [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md). Nearest neighbors:

- [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md): the single normative statement of the three doctrines this module works with. Where a formulation here and DOCTRINE.md differ, DOCTRINE.md controls.
- [newtons-kitchen.md](./newtons-kitchen.md): the mechanics: the same three doctrines derived as three laws of consequential motion. Newton's Kitchen governs the agent's motion through the world; this module governs the loop between the agent and the person directing it.
- [karpathys-kitchen.md](./karpathys-kitchen.md): the technical warrant: the method derived from the mechanisms of the technology rather than asserted.
- [computational-drafting](https://github.com/rolldabones/computational-drafting): Return to Source, operationalized: the proof-carrying analysis record and the claim-evidence matrix are instruments for the journey from conclusion back to evidence and source, and the specification is Informed Intent in written form.
- [README.md](./README.md): the canonical method this module serves. Every other file defers to it.

---

**Final Liability rests with the Human.**
