# SLOW AI KITCHEN

### Karpathy's Kitchen

*A Technical Reading and Viewing Guide for Governance, Risk, Audit and Accountability*

**A standalone add-on module for readers who want Slow AI derived from the technology's actual mechanisms rather than asserted as policy.**

**Son-U Michael Paik**
CEO, GRC Solutions Korea
Former General Counsel, BABL AI
[www.grcskorea.com](http://www.grcskorea.com)

August 24, 2026 (KST)

**Final Liability rests with the Human.**

> **Attribution and independence.** This module is an independent reading of Andrej Karpathy's published work. He has no involvement in it, has not reviewed it and does not endorse it. His works are cited and linked to their primary sources and are quoted only in short passages under fair use. The governance conclusions drawn from them are the author's own and should not be attributed to him. The title is descriptive of the subject and signals no association.

> **Link currency.** Every external link in this module was checked on 24 August 2026 (KST). The status of each is recorded in the [Link Register](#link-register) at the end. Third-party material moves, and a link that resolved on that date may not resolve later. Check the register before relying on any citation.

**Scope note.** This module does not alter any step, gate, role or principle of the core method. It supplies the derivation beneath the method's controls: what fact about the technology forces each gate to exist. It assumes no other module and requires none.

---

## Contents

- [Why Karpathy, and Where Slow AI Came From](#why-karpathy-and-where-slow-ai-came-from)
  - [The instructor](#the-instructor)
  - [What I actually took from it](#what-i-actually-took-from-it)
  - [Knowledge, and the nerve to use it](#knowledge-and-the-nerve-to-use-it)
  - [Where I part company](#where-i-part-company)
- [What This Module Adds to the Method](#what-this-module-adds-to-the-method)
  - [How the twelve sections build](#how-the-twelve-sections-build)
- [1. Intro to Large Language Models](#1-intro-to-large-language-models)
- [2. Deep Dive into LLMs like ChatGPT](#2-deep-dive-into-llms-like-chatgpt)
- [3. State of GPT](#3-state-of-gpt)
- [4. How I Use LLMs](#4-how-i-use-llms)
- [5. Software 2.0](#5-software-20)
- [6. A Recipe for Training Neural Networks](#6-a-recipe-for-training-neural-networks)
- [7. Neural Networks: Zero to Hero](#7-neural-networks-zero-to-hero)
- [8. microgpt](#8-microgpt)
- [9. Software Is Changing (Again)](#9-software-is-changing-again)
- [10. Tesla, and the Distance Between a Demo and a Product](#10-tesla-and-the-distance-between-a-demo-and-a-product)
- [11. Verifiability](#11-verifiability)
- [12. Animals vs Ghosts](#12-animals-vs-ghosts)
- [The Karpathy Governance Synthesis](#the-karpathy-governance-synthesis)
- [A Governance Architecture Derived from Karpathy](#a-governance-architecture-derived-from-karpathy)
- [The Technical Derivation of Slow AI](#the-technical-derivation-of-slow-ai)
- [Recommended Study Sequence](#recommended-study-sequence)
  - [The short pass](#the-short-pass)
- [Master Resources](#master-resources)
- [Link Register](#link-register)
- [The Larger Lesson](#the-larger-lesson)

---

Andrej Karpathy is not primarily an AI governance scholar. That is precisely why his work is useful to one.

Governance frameworks frequently begin with principles, risks, controls and obligations, then work backward toward the technology being governed. Karpathy approaches the problem from the opposite direction. He strips artificial intelligence down to its mechanisms, shows what those mechanisms can and cannot do, then builds upward toward increasingly capable systems.

For AI governance, that sequence matters.

Before deciding how an AI system should be governed, we should understand what kind of thing it is.

The following curriculum is designed around that proposition.

---

## Why Karpathy, and Where Slow AI Came From

Most readers know Andrej Karpathy for two things.

He was a founding member of OpenAI and then Director of AI at Tesla from 2017 to 2022, where he led the computer vision team behind Autopilot. And in February 2025 he coined the phrase vibe coding, for a way of working he later described, in the interview cited in section 12, as "Hi, please implement this or that, enter, and then let the model do it." The phrase escaped the industry inside a year and was reported as Collins Dictionary's word of the year for 2025.

Both facts point a reader toward the same expectation: that this is a body of work about how far the technology can be pushed.

That expectation is useful here precisely because it is incomplete.

### The instructor

Karpathy is a teacher before he is anything else in this curriculum. He designed and was the primary instructor for CS231n at Stanford, the university's first deep learning course, which grew from 150 students in 2015 to 750 in 2017. He published Neural Networks: Zero to Hero as a free course that builds a language model upward from backpropagation in code the reader runs themselves. In 2024 he founded Eureka Labs to work on AI-native education full time. His own site sorts his lectures into a technical track and a general audience track, which is a teacher's distinction rather than a researcher's.

What makes him effective is not enthusiasm. It is that he refuses to leave an abstraction closed. He builds the thing from nothing, in front of you, until the mechanism is visible. His page for microgpt states the discipline in one line: "This file is the complete algorithm. Everything else is just efficiency."

A mechanism you can see is a mechanism whose limits you can also see. That is the part I took away.

### What I actually took from it

I did not come to these works looking for governance material. I came to them to understand what I was being asked to audit, certify and advise on. What I found was an engineer being unusually candid about where the technology does not hold.

Neural network training is a leaky abstraction. Networks fail silently, and a misconfigured one "will throw exceptions only if you're lucky." Capability is jagged, so a model that is excellent at one task can be unreliable at a task that looks almost identical. The Software 2.0 stack can adopt the biases in its training data silently. None of this appears as a warning issued to the public. It appears as practical advice to engineers who have to make the thing work, which is exactly why it carries weight.

Slow AI came out of reading the limitations rather than the potential.

If the machine fails without crashing, the absence of an error is not evidence of correctness, and verification has to sit inside the workflow rather than after it. If capability is jagged, testing the model tells you very little and you have to test the use. If the weights cannot explain themselves, explainability has to be assembled from the record around them: what went in, what was used, what came out, who checked it and who decided. Each gate in the method answers a specific technical fact rather than a general preference for caution.

He documents these limits going up, in order to build well. The method applies them coming down, in order to deploy safely. That is the whole of the relationship, and it is why the doctrine is derived rather than declared.

### Knowledge, and the nerve to use it

There is a second thing these lectures gave me and it is harder to write down than the first.

I am a lawyer. I did not train as an engineer and I am not going to become one. For a long time that felt like a permanent disqualification from holding an informed view of the systems I was being asked to advise on, and the natural response to that feeling is deference: accept the vendor's account of what the system does, treat the model as a black box because someone said it was one, and write governance language that floats above the technology without ever touching it. A great deal of published AI governance reads exactly like that, and the reason is not laziness. It is nerve.

Karpathy's lectures made the deference unnecessary. Not because they turned me into an engineer. Because they demonstrate that the mechanism is comprehensible to anyone willing to sit with it, and that the people who understand it best are the ones most willing to say plainly where it fails.

So I studied on my own, in the evenings, at my own pace, using AI to learn AI: asking models to explain their own mechanisms, then checking those explanations against the primary sources, and building an account I could defend rather than one I had been handed. The method was itself an instance of the doctrine. Bounded use, verification against something the tool could not fabricate, judgment retained.

Karpathy describes the same trap from the teacher's side, and names why the checking matters:

*"There's the high-level surface knowledge, but when you build something from scratch, you're forced to come to terms with what you don't understand and you don't know that you don't understand it."*

He follows it with a line he attributes to Feynman: "If I can't build it, I don't understand it." A governance professional is not going to build a language model. But the principle transfers exactly, and the method already has a step for it. Step 3, Knife Work, exists because a person who has not done the irreversible preparation cannot evaluate what comes back. What Karpathy is describing to engineers is Gate 2, stated in a different room.

What I gained was knowledge. What I also gained, and needed more, was the courage to proceed. The courage to sit in a room with engineers and ask the question that actually matters. The courage to write a requirement knowing why it has to say what it says, and to hold it when someone pushes back.

That is part of why this module belongs in a repository about method rather than in a reading list. A practitioner who understands the mechanism does not need anyone's permission to govern it.

### Where I part company

Not with the work. With a popular reading of it.

In April 2025 Karpathy vibe coded a real application, MenuGen, and wrote up what happened. For anyone being told that AI has retired the need for engineering discipline, it is the most useful document in this curriculum.

**Read:** https://karpathy.bearblog.dev/vibe-coding-menugen/

The local prototype came together almost instantly. "I felt like I was 80% done but (foreshadowing...) it was a bit closer to 20%." Then came deployment. The model hallucinated deprecated interfaces. It produced roughly a thousand lines against an authentication API that no longer existed. And at one point it wired the payment flow to match customers by email address, which would have silently failed to credit anyone whose checkout email differed from their sign-in email. He caught it because he knew what to look for. Nothing in the system would have raised an error. His summary of the pattern: the models "make subtle but critical design mistakes when you watch them closely, and sometimes they hallucinate or gaslight you about solutions."

His own conclusion: "Ultimately, vibe coding full web apps today is kind of messy and not a good idea for anything of actual importance."

So the disagreement is not with him. He wrote the sentence himself, in the same post where he celebrates what the technique makes possible. The disagreement is with the reading that keeps the celebration and drops the sentence.

Anyone who has followed the argument about silent failure cannot carry vibe coding into a regulated production system and call the result governed. The freedom and the discipline come from the same source: knowing what the machine is doing, and knowing where it stops being trustworthy.

That is the reading this module sets out to make explicit.

A word on the title. The borrowing runs in one direction only. The Kitchen is the method, and it is mine. Karpathy's Kitchen is the reading of his published work that sits underneath it, assembled by a reader who was never his student in any formal sense and has never met him.

---

## What This Module Adds to the Method

Slow AI Kitchen states five core principles and calls them operating constraints. It then explains why they work by describing what happens to a team that prompts before it has thought. That explanation is behavioral. It is correct, and it is not sufficient for a reader who wants to know why the constraints take the shape they do rather than some other shape.

This module supplies the layer beneath. It reads twelve works by an engineer rather than a governance author and shows that each of the method's controls is forced by a property of the technology itself. Verify before reliance is not caution. It is the only available response to a class of system that fails without crashing. Keep responsibility human is not sentiment. It is the consequence of a system that accrues agency without accruing responsibility.

The seven-point synthesis below is not a restatement of the five core principles. Two of its points, design for silent failure and preserve the human principal, are those principles derived. The rest extend past the task register into system and program scale, where the method already operates through the Feast and the Your Restaurant addendum. Nothing in the synthesis contradicts a principle and nothing replaces one.

Nothing here is new doctrine. The twelve steps, the ten gates, the three tiers and the two role sets are unchanged, and this module defers to them throughout. Where it names an accountable human it names one of the method's canonical roles. Where it names a control it points at the gate that already carries it. The contribution is the derivation, not the architecture.

### How the twelve sections build

The sections are a sequence, not a list. Each one adds a distinct move, and the later ones do not work without the earlier ones.

| Sections | What they establish | What it forces |
|---|---|---|
| 1 to 3 | What the thing is: output is generated rather than retrieved, capability is uneven, and the deployed object is a stack rather than a model | You cannot govern the model. You have to govern the system and the use |
| 4 and 9 | What it is allowed to do: capability follows permissions, and execution authority is delegable by degree | Govern verbs, and set autonomy per verb on evidence |
| 5 to 8 | Why it cannot simply be inspected: behavior is learned rather than specified, failure is silent, and the mechanism is small enough to see plainly | Verification has to sit inside the workflow, and explanation has to be assembled around the model rather than extracted from it |
| 10 and 11 | Where it will and will not work: the demo-to-product gap, and verifiability as the predictor of reliability | Triage the use-case inventory, and never authorize on a demonstration |
| 12 | What it is not: not an animal, not a mind, not a bearer of responsibility | The principal stays human, and the language in governance artifacts has to say so |

Read that way, the seven-point synthesis that follows is not a set of opinions. It is what is left after the twelve sections have removed the alternatives.

---

## 1. Intro to Large Language Models

**Purpose:** Establish the basic mental model.

Karpathy's 2023 lecture is the best entry point. It explains how Large Language Models are trained, how they generate text, why capabilities emerge and why apparently intelligent behavior should not be confused with conventional deterministic computation.

**Watch:** https://www.youtube.com/watch?v=zjkBMFhNj_g

**Governance lesson:** The output of an LLM is generated, not retrieved from an authoritative store of truth. Reliability therefore cannot simply be assumed from fluency.

Karpathy puts the mechanism plainly elsewhere, and it is worth carrying into this section: what the model holds from training is "a hazy recollection" of the documents it saw, because trillions of tokens have been compressed into a few billion parameters. Nothing in the system marks which parts of the recollection are sound. That is why a model will answer a question about a document with something roughly right, and why giving it the document instead produces a different quality of answer. Compression is the mechanism, and it does not announce its own edges.

This immediately changes the governance question.

The relevant question is not:

*Is the AI accurate?*

It is:

*Accurate enough for what purpose, under what conditions and with what consequence if it is wrong?*

That is the beginning of risk classification.

**Framework connection:** **Informed Intent**. Before deploying the model, define the objective, permitted use, constraints and acceptance criteria.

**Control implication:** Risk-tier the use, not merely the model.

---

## 2. Deep Dive into LLMs like ChatGPT

**Purpose:** Understand the modern LLM stack.

This is Karpathy's more comprehensive treatment. He moves from pretraining data and tokenization through inference, post-training, hallucination, tool use, reinforcement learning and what he calls the model's "jagged intelligence."

**Watch:** https://www.youtube.com/watch?v=7xTGNNLPyMI

The phrase jagged intelligence may be especially important for governance.

A model can perform a task requiring remarkable abstraction, then fail at something apparently elementary.

Capability therefore does not rise uniformly.

**Governance lesson:** Benchmark performance is not equivalent to operational reliability.

A model that is excellent at Task A may be unreliable at superficially similar Task B. Governance based only on model-level capability scores will therefore miss important risk.

**Framework connection:** **Slow AI**. Evaluation must occur in the actual workflow, with the actual inputs, tools, constraints and consequences.

**Control implication:** Test systems and use cases, not merely foundation models.

---

## 3. State of GPT

**Purpose:** Understand the training pipeline.

Karpathy's State of GPT, delivered at Microsoft Build in 2023, explains the sequence through which a base model becomes an assistant.

That distinction is important because there is no single thing called "the model." A deployed AI system reflects pretraining, post-training, prompting, context, retrieval, tools, system instructions and runtime environment.

**Watch:** https://www.youtube.com/watch?v=bZQun8Y4L2A

The slide deck his site links beside this talk did not resolve when this module was checked. See the [Link Register](#link-register).

**Governance lesson:** The behavior being governed arises from a stack, not a single artifact.

That means model governance alone is insufficient.

**Control implication:** Maintain provenance across:

base model → model version → system prompt → retrieval sources → tools → permissions → user inputs → output → human action

This is effectively an AI chain of custody.

**Framework connection:** Slow AI. Make the relevant system visible and auditable.

---

## 4. How I Use LLMs

**Purpose:** Move from models to workflows.

Karpathy's practical lecture covers ordinary LLM interaction, reasoning models, web search, deep research, document context, Python tools, coding, multimodal systems, memory and custom assistants.

**Watch:** https://www.youtube.com/watch?v=EWvNQjAaOHw

This is where the governance problem changes significantly.

An LLM that merely produces text has one risk profile.

An LLM that can:

- search,
- read files,
- execute code,
- remember information,
- call tools or
- change external systems

has another.

**Governance lesson:** Capability follows permissions.

The model's intelligence matters, but the tools available to it may matter more.

**Framework connection:** Govern the verb, the boundary and the consequence.

"Summarize this contract" is different from:

"Amend the contract."

"Review these transactions" is different from:

"Block the transaction."

"Recommend payment" is different from:

"Send payment."

**Control implication:** Classify AI systems partly by the verbs they are authorized to execute.

---

## 5. Software 2.0

**Purpose:** Understand why AI governance cannot simply copy traditional software governance.

Karpathy introduced the idea of Software 2.0 in November 2017.

**Read:** https://karpathy.medium.com/software-2-0-a64152b37c35

Traditional software largely consists of instructions explicitly written by programmers.

Machine-learning systems instead learn important parts of their behavior from data through optimization.

This has enormous governance consequences.

**Governance lesson:** Some system behavior is no longer directly specified by human-readable rules.

Therefore:

documentation cannot be identical to explanation.

Knowing the architecture, training process and intended function does not mean we can completely explain every individual model output.

Karpathy makes this point against his own thesis. The essay carries a section headed The limitations of Software 2.0, which records that these systems "can 'silently fail', e.g., by silently adopting biases in their training data," and that across many application areas "we'll be left with a choice of using a 90% accurate model we understand, or 99% accurate model we don't." An author who publishes the failure modes of his own proposal is a more reliable source than one who does not.

**Framework connection:** Slow AI. Explainability should therefore be understood pragmatically.

We may not always be able to explain every internal computation, but we can make the decision system explainable:

- what went in,
- what model was used,
- what tools were available,
- what came out,
- what evidence supported it,
- who reviewed it and
- who decided.

That is governable even when the neural network itself remains partially opaque.

---

## 6. A Recipe for Training Neural Networks

**Purpose:** Understand invisible failure.

For governance professionals, this may be Karpathy's most underrated essay.

He describes neural-network training as a "leaky abstraction" and, even more importantly, observes that neural networks can fail silently. His recommended response is disciplined incremental development: start simple, understand the data, introduce complexity gradually, formulate expectations and test them.

**Read:** https://karpathy.github.io/2019/04/25/recipe/

This translates almost directly into assurance.

**Governance lesson:** The absence of an error message is not evidence that the system is working correctly.

This is one of the central problems of AI assurance.

A system can:

- run,
- produce plausible output,
- pass superficial inspection and
- still be materially wrong.

**Framework connection:** Slow AI. This is the technical argument for the sequence the method already runs, rather than deploy first and govern afterward. Read against the twelve steps:

FRAME (Steps 1 through 4) → DRAFT (Steps 5 and 7) → TEST and VERIFY (Step 8, the two halves of Gate 6) → LOCK (Step 9, Gate 7)

The five-word form is a mnemonic. The steps and the gates are the method.

**Control implication:** Build verification into the workflow rather than treating review as a final administrative step. This is Gate 6 stated as a technical necessity rather than a procedural preference.

---

## 7. Neural Networks: Zero to Hero

**Purpose:** Learn enough mechanics to avoid governance by metaphor.

Karpathy's course builds neural networks from first principles, progressing from backpropagation to language models and eventually GPT.

**Course:** https://karpathy.ai/zero-to-hero.html

**YouTube playlist:** https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ

**GitHub repository:** https://github.com/karpathy/nn-zero-to-hero

You do not need to complete the entire programming course.

For governance purposes I would prioritize:

- **micrograd**: Understand how neural networks learn.
- **makemore**: Understand probabilistic language generation.
- **tokenization**: Understand why what humans see as words and what models process as tokens are not the same thing.
- **Let's build GPT**: Understand attention and the basic Transformer architecture.

**Governance lesson:** Enough technical literacy prevents us from governing imaginary systems.

Many governance errors begin with anthropomorphic descriptions such as:

"the AI knows,"

"the AI understands,"

"the AI decided."

Technical understanding replaces those statements with more precise claims.

Precision improves governance.

---

## 8. microgpt

**Purpose:** Strip the technology down to its essence.

On February 12, 2026 Karpathy published microgpt, a single file of 200 lines of pure Python with no dependencies that trains and runs a GPT. In his own description it contains "the full algorithmic content of what is needed: dataset of documents, tokenizer, autograd engine, a GPT-2-like neural network architecture, the Adam optimizer, training loop, and inference loop. Everything else is just efficiency." He calls it the culmination of a decade-long effort to reduce language models to their essentials.

**Read:** https://karpathy.github.io/2026/02/12/microgpt/

**Code and interactive version:** https://karpathy.ai/microgpt.html

The trained model in that file has 4,192 parameters. GPT-4 class models have hundreds of billions. The algorithm is the same one.

Two answers in the post's own FAQ are worth more to a governance reader than most of the compliance literature on the same subjects.

On understanding: "mechanically: no magic is happening. The model is a big math function that maps input tokens to a probability distribution over the next token."

On hallucination: "It has no concept of truth, it only knows what sequences are statistically plausible given the training data. microgpt 'hallucinating' a name like 'karia' is the same phenomenon as ChatGPT confidently stating a false fact."

Read that second answer twice. Hallucination is not the mechanism failing. It is the mechanism working. The model that produces a correct citation and the model that invents one are running the identical operation, and nothing inside the system distinguishes the two cases. Any control that treats hallucination as a defect to be patched is aimed at the wrong thing. The only place the distinction can be made is outside the model, by something that checks.

This is conceptually important.

Industrial AI systems are extraordinarily complicated.

The fundamental mechanism is not.

**Governance lesson:** Distinguish essential model behavior from the infrastructure wrapped around it.

Much operational risk is introduced not by the Transformer itself but by:

- data,
- retrieval,
- memory,
- tools,
- agents,
- application programming interfaces,
- permissions,
- interfaces,
- automation and
- organizational processes.

**Framework connection:** Slow AI. Govern the entire sociotechnical system.

---

## 9. Software Is Changing (Again)

**Purpose:** Understand the transition from models to agents.

Karpathy's 2025 presentation at Y Combinator's AI Startup School may be the most directly relevant work in this curriculum.

**Watch:** https://www.youtube.com/watch?v=LCEmiRjPEtQ

He describes a progression:

- Software 1.0: humans write code.
- Software 2.0: neural networks learn behavior.
- Software 3.0: humans increasingly program computers through natural language.

He also characterizes LLMs as a new kind of computing platform and discusses partially autonomous applications, human-AI collaboration and lessons from autonomous driving.

Most importantly for governance, Karpathy argues for partial autonomy rather than indiscriminate automation.

**Governance lesson:** Autonomy should be a variable, not a binary condition.

The important question is not:

*Human or AI?*

It is:

*How much authority should this system receive for this particular action?*

The image is his own. He calls it an "autonomy slider," and describes the trend as one in which "more and more stuff is automated, of the stuff that can be automated at any point in time, and we're doing a bit less and less and raising ourselves in the layer of abstraction over the automation."

Read that carefully, because it contains a governance obligation that is easy to miss. Raising yourself in the layer of abstraction over the automation is how the human stops being able to check the work. It is the right move for productivity and the dangerous one for accountability, and the two happen at the same time whether or not anyone decides they should.

Stated as a ladder:

Suggest → Draft → Recommend → Execute with approval → Execute with supervision → Execute autonomously

Different verbs can occupy different levels. The slider is set per verb, deliberately, on evidence, and it is set by a named person rather than allowed to drift upward through convenience.

**Framework connection:** **Final Liability**. The further execution authority moves toward the machine, the more explicitly the human principal must be identified.

---

## 10. Tesla, and the Distance Between a Demo and a Product

**Purpose:** Learn to price the gap between what you were shown and what you would be running.

Karpathy led the Tesla Autopilot vision team from 2017 to 2022. The talks from that period are worth studying because driving exposes what conversational AI lets us ignore: the system operates in the world, the failures are irreversible, and nobody grades the work.

His archive collects them. Four repay a governance reader's time, in this order:

- **Tesla Autonomy Day, 2019:** https://www.youtube.com/watch?v=Ucp0TTmvqOE
- **PyTorch at Tesla, PyTorch DevCon 2019:** https://www.youtube.com/watch?v=oBklltKXtDE
- **AI for Full Self-Driving, the CVPR 2021 Workshop on Autonomous Driving keynote:** https://www.youtube.com/watch?v=g6bOwQdCJrc
- **Tesla AI Day 2021:** https://www.youtube.com/watch?v=j0z4FweCy4M

**Karpathy archive:** https://karpathy.ai/

The AI Day link is the full livestream. Karpathy's own site points readers into it at roughly the forty-eighth minute, where his segment begins.

But the most useful thing he has said about that period was said afterwards, looking back on it, in the October 2025 conversation cited in section 12. It is the single most transferable idea in this guide and it takes three sentences.

**Read the transcript, section titled Why self driving took so long:** https://www.dwarkesh.com/p/andrej-karpathy

He describes riding in a Waymo in 2014 that gave him a flawless drive around Palo Alto, and thinking the problem was nearly solved. It was not. He then spent five years working on it and it still is not.

His explanation:

*"For some kinds of tasks and jobs and so on, there's a very large demo-to-product gap where the demo is very easy, but the product is very hard. It's especially the case in cases like self-driving where the cost of failure is too high."*

And the shape of that gap:

*"it's a march of nines. Every single nine is a constant amount of work. Every single nine is the same amount of work. When you get a demo and something works 90% of the time, that's just the first nine. Then you need the second nine, a third nine, a fourth nine, a fifth nine."*

By his own account Tesla covered perhaps two or three nines in five years, and more remain. Which produces the sentence a governance function should have framed on the wall:

*"I'm very unimpressed by demos."*

He then generalizes off the road and into ordinary software, unprompted:

*"in software, people should be careful, kind of like in self-driving. In self-driving, if things go wrong, you might get injured. There are worse outcomes. But in software, it's almost unbounded how terrible something could be."*

**Governance lesson:** A demonstration carries almost no information about production reliability, and the remaining distance is not a matter of polish. It is a fixed, repeated cost per nine.

This is the answer to the most common failure of AI procurement. A vendor demonstrates a system that works, the room is impressed, and the impression is converted into an authorization. Nothing in the demonstration establishes the ninth-tenth-hundredth case, and the party that will carry the consequence of those cases is not the party doing the demonstrating.

Note also what he says about which work has this property. Vibe coding does not. Production code does, because a single mistake becomes a security vulnerability or a mass disclosure of personal data. Regulated work sits on the same side of that line as self-driving, not the same side as the weekend project.

**Framework connection:** **GRCnext™**. The relevant capability is not prediction. It is the ability to respond when prediction fails:

detect → decide → intervene → recover

within an operationally meaningful period. Each nine is bought with exactly that loop, run over and over against the cases reality supplies and the demonstration did not.

**Control implication:** Never authorize on the strength of a demonstration. Require evidence of the nines: what failure rate, measured on what population, over what period, with what intervention record. Where that evidence does not exist, the tool registry entry says so, and the autonomy level stays where the evidence puts it rather than where the demonstration suggested.

---

## 11. Verifiability

**Purpose:** Learn to predict where the system will be reliable before deploying it there.

This is a short post from November 2025 and it may be the most immediately usable thing in the curriculum.

**Read:** https://karpathy.bearblog.dev/verifiability/

Karpathy's argument is that each programming paradigm has a feature that predicts which work it will absorb. For hand-written software, which he calls Software 1.0, the predictive feature was specifiability: could the task be written down as a rote procedure. For Software 2.0, the predictive feature is verifiability: can the system practice the task. He gives three conditions for a task to be verifiable. The environment has to be resettable, so a new attempt can be started; efficient, so many attempts can be made; and rewardable, so an automated process can score any given attempt.

He closes with the formulation:

*Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.*

**Governance lesson:** The jagged frontier is not random. It has a shape and the shape can be predicted.

This is the answer to a question section 2 raises but cannot resolve. Capability is jagged, so test the use case rather than the model. But an organization with hundreds of candidate use cases cannot test everything at equal depth, and needs to know where to look first. Verifiability supplies that. Tasks that are resettable, cheap to attempt and automatically scorable have been optimized hard and tend to be strong. Tasks that combine real-world knowledge, state, context and judgment have not, and lag by comparison. Legal, compliance and risk work sits almost entirely in the second category.

That produces an uncomfortable and useful conclusion. The tasks a governance function most wants to automate are, as a class, the tasks this paradigm is worst at, because there is no cheap automated way to score whether the answer was right. Where the score does not exist, a human has to be it.

**Framework connection:** **Informed Intent** and **Slow AI**. Verifiability belongs in the tool registry beside the risk tier. It is the question that decides how much evidence a use case needs before it may run.

**Control implication:** Triage the use-case inventory by verifiability. Unverifiable tasks do not become prohibited; they become the ones where human review is load-bearing rather than ceremonial, and where the evidence requirement rises rather than falls.

---

## 12. Animals vs Ghosts

**Purpose:** Stop reasoning about these systems by analogy to minds.

**Read:** https://karpathy.bearblog.dev/animals-vs-ghosts/

**Watch the companion conversation:** https://www.youtube.com/watch?v=lXUZvyajciY

**Or read its transcript, which is easier to quote from:** https://www.dwarkesh.com/p/andrej-karpathy

In October 2025 Karpathy wrote a response to a conversation between Dwarkesh Patel and Richard Sutton about whether large language models learn the way animals do. His conclusion is stated flatly:

"Stated plainly, today's frontier LLM research is not about building animals. It is about summoning ghosts."

Animals arrive with an enormous inheritance. A newborn zebra runs within the hour because evolution has already written most of the answer into its DNA. Language models have no such inheritance. What they have instead is the text. In his phrase, "pretraining is our crappy evolution," and what comes out the other side is an imperfect replica, "a kind of statistical distillation of humanity's documents."

**Governance lesson:** These systems are a different kind of thing, and the analogies we reach for are the wrong ones.

Section 7 of this guide warns against the anthropomorphic register: the AI knows, the AI understands, the AI decided. Here is the technical reason that register misleads. A ghost is not a mind with gaps. It is a statistical reconstruction of what people have written, which will therefore be fluent about anything well documented and unreliable about anything that was not, in a pattern that has nothing to do with how difficult a human would find the task.

There is a second, quieter mechanism in the same interview that matters more to an auditor than the metaphor does. Karpathy distinguishes what the model holds in its weights from what it holds in its context window:

*"anything that happens during the training of the neural network, the knowledge is only a hazy recollection of what happened in training time... Whereas anything that happens in the context window of the neural network... is very directly accessible to the neural net."*

Weights are a hazy recollection. Context is working memory. That single distinction explains why a model asked about a document from memory will produce something roughly right and confidently wrong at the edges, and why the same model given the document performs far better. It is the technical case for retrieval, for supplying source material rather than relying on recall, and for treating any unsourced factual assertion from a model as an artifact of compression rather than a citation.

The same conversation is also where Karpathy broke publicly with the industry's timeline. He argued for "the decade of agents" rather than the year of agents, explaining it as "a reaction to a pre-existing quote... I was triggered by that because there's some over-prediction going on in the industry." He described current models as carrying "cognitive deficits." On the code produced by frontier models when he was building his own repository, he was blunter:

*"I feel like the industry is making too big of a jump and is trying to pretend like this is amazing, and it's not. It's slop."*

That is the person who coined vibe coding, in 2025, about the state of the art. Anyone quoting him in support of accelerated deployment should read the same interview.

**Framework connection:** **Final Liability**. An entity that is not an animal, not a person and not a legal subject cannot hold responsibility, however capable it becomes.

**Control implication:** Ban the anthropomorphic register from governance artifacts. Risk registers, incident reports and board papers should record what the system produced and who relied on it, never what it knew, understood or decided. And treat any factual claim a model makes from memory alone as unsourced until it is checked, because on the author's own account that is precisely what it is.

---

## The Karpathy Governance Synthesis

Taken together, these works suggest a different architecture for AI governance.

### 1. Govern systems, not models

The model is one component.

The governed object is:

Model + Context + Data + Tools + Permissions + Workflow + Humans + Consequences

### 2. Govern verbs

Risk follows what the system can do.

An AI allowed to describe something presents a different risk from one allowed to approve, reject, transfer, publish, diagnose, terminate, trade or pay.

The verb is therefore an unusually efficient unit of governance.

### 3. Treat autonomy as a dial

AI governance should not divide systems merely into "human-controlled" and "autonomous."

Instead ask how far authority has been delegated.

The autonomy level should rise only when evidence supports it, and a demonstration is not that evidence. The evidence is a measured failure rate on a real population, which is bought one nine at a time.

### 4. Assume capability is jagged

Do not infer reliability in one task from brilliance in another.

Test the actual use case, and use verifiability to decide how deep the test has to go. Where a task is resettable, cheap to attempt and automatically scorable, the technology has been optimized against it hard. Where it is not, expect the lag, and put the human there.

### 5. Design for silent failure

AI systems frequently fail without crashing.

Therefore controls must detect plausible wrongness, not simply technical malfunction.

Two illustrations from this curriculum, both from Karpathy's own hand. A payment flow that matched customers by the wrong field and would have quietly failed to credit them, caught by a human who knew what to look for and by nothing else in the system. And a model inventing a name that never existed, which the post shows is the identical operation to the model producing a correct one. Neither event raises an error. Both are what the machine does when it is working.

### 6. Put determinism around probability

The neural network may remain stochastic.

The surrounding governance need not be.

We can make deterministic:

- permissions,
- approval thresholds,
- logging,
- escalation,
- data access,
- tool access,
- human review,
- deployment gates and
- shutdown authority.

This produces a useful Slow AI principle:

*Do not demand determinism from the probabilistic core. Demand governability from the system around it.*

### 7. Preserve the human principal

An AI system can acquire increasing agency without acquiring legal, moral or organizational responsibility.

That asymmetry matters.

As delegated capability increases, accountability should become more explicit, not less.

Hence:

*Keep AI as the agent. Name the right human principal.*

And ultimately:

**Final Liability rests with the Human.**

---

## A Governance Architecture Derived from Karpathy

Karpathy's technical worldview can therefore be translated into five governance layers:

1. **Intent.** What is the system supposed to accomplish?
2. **Boundary.** What information, tools and environments may it access?
3. **Authority.** What verbs may it perform and at what level of autonomy?
4. **Evidence.** How do we know whether it performs adequately under the relevant conditions?
5. **Liability.** Which human owns the resulting decision and has authority to intervene?

These correspond closely to:

Informed Intent → Slow AI → Govern the Verb → Evidence → Final Liability

The sequence is important.

Governance begins before the prompt and ends after the output.

These five layers are not a second structure standing beside the method. They are the method read at a different altitude. Intent is Step 1 and Step 2 (Gate 1). Boundary is Step 4 (Gate 3) and Step 5 (Gate 4). Authority is Step 6 (Gate 5) at task level and Steps 10 and 11 (Gates 8 and 9) at organizational level. Evidence is Step 8 (Gate 6). Liability is Step 9 (Gate 7) and Step 12 (Gate 10). Steps 3 and 7 do not appear here because they are production work rather than governance layers, which is why the method marks them as the two steps without a gate.

---

## The Technical Derivation of Slow AI

Slow AI is usually stated as a doctrine: governed, explainable, auditable AI.

A doctrine stated can be dismissed as preference.

A doctrine derived cannot.

Each principle in the synthesis above is forced by a technical fact established in this curriculum. The discipline is a chain:

Technical fact → Failure mode → Governance principle → Control → Evidence → Human owner

Applied to the seven principles:

| Technical fact | Failure mode | Governance principle | Control | Evidence | Human owner |
|---|---|---|---|---|---|
| A deployed system is a stack: model, context, data, tools, permissions, workflow, humans (3, 8) | The model is governed while the system drifts | Govern systems, not models | System inventory with explicit boundaries, carried in the authorized tool registry (Step 10, Gate 8) | The inventory and boundary records | AI Owner |
| Capability follows permissions; tools determine reach (4) | Verbs escalate without authorization | Govern verbs | Verb-level authorization in the tool registry and the competency and authorization record (Steps 10 and 11, Gates 8 and 9) | Permission grants and approval records | AI Owner, with the Executive Sponsor where the grant crosses functions |
| Execution authority is delegable by degree, and the distance from demo to production is a fixed cost per nine (9, 10) | Binary automation; authority outruns evidence; a demonstration is read as proof | Treat autonomy as a dial | Autonomy level set per verb and raised only on evidence, in the registry at deployment and at the release decision at task level (Step 10, Gate 8; Step 9, Gate 7) | Delegation and escalation records | AI Owner at deployment level, Approver at task level |
| Capability is jagged across tasks, and the jaggedness tracks verifiability (2, 11) | Reliability inferred from adjacent brilliance | Assume capability is jagged | Use-case testing in the actual workflow, triaged by whether the task is resettable, cheap to attempt and automatically scorable (Step 4, Gate 3; Step 8, Gate 6) | Per-use-case evaluation results and the verifiability assessment behind the test depth | Reviewer, with the AI Owner for use cases carried in the registry |
| Output is generated, not retrieved, and networks fail silently (1, 6) | Plausible wrongness passes inspection | Design for silent failure | Verification inside the workflow rather than after it (Step 8, Gate 6) | Gate results and sign-offs | Reviewer |
| Learned behavior is not rule-specified; the core is stochastic (5) | Explanations are demanded that the weights cannot give | Put determinism around probability | Deterministic permissions, thresholds, logging, review and shutdown authority (Steps 10 and 12, Gates 8 and 10) | Decision records: inputs, model, tools, output, review, decision | Approver |
| Agency accrues without responsibility, the system is not a mind, and consequences bind in the environment (9, 10, 12) | A capable system with no accountable principal | Preserve the human principal | Named ownership with authority to detect, decide, intervene and recover (Step 6, Gate 5; Step 12, Gate 10) | Ownership register and intervention logs | Owner, with the Executive Sponsor at program scale |

Numbers in the first column refer to the sections of this guide. Step and gate references are to the twelve-step method.

The last column names the method's own roles and introduces none. Preparer, Builder, Reviewer, Approver and Owner are the task roles that govern Steps 1 through 9. AI Owner, AI Operator and Executive Sponsor are the organizational roles that govern Steps 10 through 12. Where a row lands differently at task and organizational scale, both are named, because the same technical fact produces an obligation in each register.

Read the columns, not only the rows.

The control column is what governed means in practice. The evidence column is what auditable means in practice. The decision records in the sixth row are what explainable means when the weights cannot explain themselves.

Governed, explainable, auditable.

That is Slow AI, derived rather than declared.

That is the bridge from Karpathy's engineering to a defensible technical foundation for Slow AI.

---

## Recommended Study Sequence

I would approach the curriculum in three passes.

### Pass I: Understand

1. Intro to Large Language Models: https://www.youtube.com/watch?v=zjkBMFhNj_g
2. Deep Dive into LLMs like ChatGPT: https://www.youtube.com/watch?v=7xTGNNLPyMI
3. State of GPT: https://www.youtube.com/watch?v=bZQun8Y4L2A

*Question: What exactly are we governing?*

### Pass II: Operate

4. How I Use LLMs: https://www.youtube.com/watch?v=EWvNQjAaOHw
5. Software 2.0: https://karpathy.medium.com/software-2-0-a64152b37c35
6. A Recipe for Training Neural Networks: https://karpathy.github.io/2019/04/25/recipe/

*Question: How does this technology fail when people actually use it?*

### Pass III: Govern

7. Selected Zero to Hero lectures: https://karpathy.ai/zero-to-hero.html
8. microgpt: https://karpathy.github.io/2026/02/12/microgpt/
9. Software Is Changing (Again): https://www.youtube.com/watch?v=LCEmiRjPEtQ
10. Tesla autonomy presentations: https://karpathy.ai/

*Question: How much authority should we delegate and what must surround that delegation?*

### The short pass

If you have one hour rather than thirty, read these three in this order. They are short, they are recent, and between them they carry most of what a governance reader needs.

1. Verifiability: https://karpathy.bearblog.dev/verifiability/
2. Vibe coding MenuGen: https://karpathy.bearblog.dev/vibe-coding-menugen/
3. A Recipe for Training Neural Networks, sections 1 and 2 only: https://karpathy.github.io/2019/04/25/recipe/

*Question: where will this technology be reliable, where will it fail quietly, and how would I know the difference?*

This is the pass to give an executive, a board member or a new team member. It is also the one to run before a vendor meeting, with one addition: read the march of nines passage in section 10 of this guide on the way into the room.

---

## Master Resources

- Andrej Karpathy home page and archive: https://karpathy.ai/
- Current blog, where sections 11 and 12 come from: https://karpathy.bearblog.dev/blog/
- Original blog and essays, including the training recipe and microgpt: https://karpathy.github.io/
- Karpathy YouTube channel: https://www.youtube.com/@AndrejKarpathy
- Karpathy GitHub: https://github.com/karpathy
- Neural Networks: Zero to Hero: https://karpathy.ai/zero-to-hero.html
- Zero to Hero GitHub repository: https://github.com/karpathy/nn-zero-to-hero
- nanochat, the full ChatGPT-style pipeline in roughly eight thousand lines: https://github.com/karpathy/nanochat

A note on the blogs, because it costs an hour to discover the hard way. Karpathy has written on three platforms and the material is not consolidated. The original blog at karpathy.github.io carries the training recipe and microgpt. Software 2.0 sits alone on Medium. Everything since 2024, including the two shortest and most governance-relevant posts in this guide, is on the Bear blog. A reader who stops at the first blog will conclude he has written almost nothing since 2022, which is wrong by a wide margin.

---

## Link Register

Every external link in this module was opened in a browser on 24 August 2026 (KST) and the destination checked against the citation. All of them resolve, with one exception recorded below.

| Link | Cited at | Destination as loaded |
|---|---|---|
| karpathy.ai/ | 10, Master Resources | Andrej Karpathy home page and archive |
| karpathy.bearblog.dev/blog/ | Master Resources | Current blog index |
| karpathy.bearblog.dev/verifiability/ | 11 | Verifiability, 18 Nov 2025 |
| karpathy.bearblog.dev/animals-vs-ghosts/ | 12 | Animals vs Ghosts, 2 Oct 2025 |
| karpathy.bearblog.dev/vibe-coding-menugen/ | Origin section | Vibe coding MenuGen, 27 Apr 2025 |
| dwarkesh.com/p/andrej-karpathy | 10, 12, origin section | Full transcript, published 18 Oct 2025 |
| karpathy.github.io/ | Master Resources | Andrej Karpathy blog index |
| karpathy.github.io/2019/04/25/recipe/ | 6, Pass II | A Recipe for Training Neural Networks, 25 Apr 2019 |
| karpathy.medium.com/software-2-0-a64152b37c35 | 5, Pass II | Software 2.0, 11 Nov 2017 |
| karpathy.ai/zero-to-hero.html | 7, Pass III, Master Resources | Neural Networks: Zero to Hero syllabus |
| karpathy.github.io/2026/02/12/microgpt/ | 8, Pass III | microgpt, 12 Feb 2026 |
| karpathy.ai/microgpt.html | 8 | microgpt source page |
| github.com/karpathy | Master Resources | Andrej Karpathy GitHub profile |
| github.com/karpathy/nn-zero-to-hero | 7, Master Resources | nn-zero-to-hero repository |
| github.com/karpathy/nanochat | Master Resources | nanochat repository |
| youtube.com/watch?v=zjkBMFhNj_g | 1, Pass I | [1hr Talk] Intro to Large Language Models |
| youtube.com/watch?v=7xTGNNLPyMI | 2, Pass I | Deep Dive into LLMs like ChatGPT |
| youtube.com/watch?v=bZQun8Y4L2A | 3, Pass I | State of GPT, session BRK216HFS |
| youtube.com/watch?v=EWvNQjAaOHw | 4, Pass II | How I use LLMs |
| youtube.com/watch?v=LCEmiRjPEtQ | 9, Pass III | Andrej Karpathy: Software Is Changing (Again) |
| youtube.com/watch?v=lXUZvyajciY | 10, 12 | Andrej Karpathy: We're summoning ghosts, not building animals |
| youtube.com/watch?v=Ucp0TTmvqOE | 10 | Tesla Autonomy Day |
| youtube.com/watch?v=oBklltKXtDE | 10 | PyTorch at Tesla, Andrej Karpathy, Tesla |
| youtube.com/watch?v=g6bOwQdCJrc | 10 | [CVPR'21 WAD] Keynote, Andrej Karpathy, Tesla |
| youtube.com/watch?v=j0z4FweCy4M | 10 | Tesla AI Day 2021 |
| youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ | 7, Master Resources | Neural Networks: Zero to Hero playlist |
| youtube.com/@AndrejKarpathy | Master Resources | Andrej Karpathy channel |
| grcskorea.com | Masthead | GRC Solutions Korea |
| github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md | Closing | The ecosystem map, v1.7.7 |
| karpathy.ai/stateofgpt.pdf | 3 | **Does not resolve** |

**The one failure.** Karpathy's own site links a slide deck at `karpathy.ai/stateofgpt.pdf` beside the State of GPT talk. Requesting that address returns the karpathy.ai home page as HTML rather than a PDF, which is what a static site does when it serves its index in place of a missing file. This was confirmed in a browser, not inferred from a failed fetch. The talk is unaffected and the deck is not cited in this module. If you find a working copy, the citation can be restored.

Two titles are worth noting because they differ from how the works are commonly named. The CVPR 2021 talk is published as a workshop keynote rather than under the title AI for Full Self-Driving that the archive gives it. The Dwarkesh conversation carries the ghosts title on YouTube and the AGI timeline title on the transcript page; they are the same conversation, published 18 October 2025.

Every quotation in this module was taken from the source named beside it and checked against that source on the date above. Where a phrase is attributed to Karpathy without quotation marks it is a paraphrase, and the source is linked in the same section so the reader can test the paraphrase against the original.

Three biographical statements do not come from the sources above and are marked here rather than left implicit. That he founded Eureka Labs in 2024, that he coined vibe coding in February 2025, and that the phrase was named Collins Dictionary's word of the year for 2025 are taken from press reporting, consistent across independent outlets, and are not load-bearing for any argument in this module. The Collins page was not reachable on the day of the check because the site was running a bot verification screen.

---

## The Larger Lesson

Karpathy's work suggests that the central governance challenge of AI is not that machines suddenly became deterministic decision-makers capable of replacing human judgment.

It is almost the opposite.

We have created extraordinarily capable probabilistic machinery and begun connecting it to increasingly consequential systems.

That creates a temptation to solve uncertainty by demanding certainty from the model.

We should resist it.

The better response is architectural.

Allow probabilistic systems to generate, infer and propose.

Make their boundaries explicit.

Control what they can see.

Control what they can do.

Measure how they behave.

Preserve evidence.

Escalate uncertainty.

Retain intervention.

And attach consequential decisions to an identifiable human principal.

That is where Karpathy's engineering and AI governance meet.

The model may remain probabilistic. Governance cannot afford to be.

The method this module derives is the twelve-step Slow AI Kitchen, published in the [repository README](./README.md). The doctrines referenced throughout, Slow AI, Informed Intent, Final Liability and GRCnext™, are maintained and mapped in [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md).

---

*AI is a tool in the kitchen, not the chef.*

**Final Liability rests with the Human.**

---

*This document is provided for general informational purposes regarding the technical foundations of AI governance. It does not constitute legal advice with respect to any specific matter, jurisdiction or engagement.*
