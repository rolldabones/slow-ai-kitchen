# Lean Tiny Servants

**Slow AI Kitchen · [Lean AI](../../lean-ai.md) · sample workflows for the workplace · 2026-11-19 (KST) · WIP (work in progress): none specified yet**

**Tiny Servants** are narrow AI services with one purpose, clear boundaries and a named owner, which do one useful task well and then stop ([profile README](https://github.com/rolldabones/rolldabones#definitions)). A Lean Tiny Servant is a Tiny Servant published with its ledger: what one accepted outcome costs, what it asks of its owner and how it stops. A servant of this kind is a tool with a named owner. It is not a person and should not be taken for one.

This folder will hold the servants as they are built, one at a time, under the [plan](../PLAN.md). Each is a small workflow for a real kind of work, written so that a reader can read every instruction, run it and check the result. None exists yet.

*GRC Solutions Korea is not affiliated with Anthropic, and Anthropic has not reviewed or endorsed these samples. Claude is Anthropic's product name, used here to refer to the product.*

## The card

Every servant carries one card. Lines 1 to 10 are the ten-line Tiny Servant spec, unchanged, as [The AI Generalist](https://github.com/rolldabones/the-ai-generalist/blob/main/facilitator-guide.md) gives it in Module 3: purpose, inputs, outputs, boundaries, owner, exit, evidence, review, tier and done-when. Lines 11 to 15 are the ledger.

| Line | Field | Write |
|---|---|---|
| 11 | Unit | The accepted outcome; how refused, abandoned and unresolved cases are counted |
| 12 | Means | What ordinary software does, what a model does and the smallest configuration that clears the cases |
| 13 | Envelope | Maximum attempts, tool calls, time and spend; where each limit is enforced |
| 14 | Stop | The abnormalities it detects, what it does at each and the fallback |
| 15 | Ledger | Cost per accepted outcome and which cost view it is; for the owner, the items, the routine minutes per item, the share of items needing a person, the minutes each of those takes and the standing hours; time to exit |

The card is the specification, not the authorization. A servant that uses tools also carries the [service ticket](../../take-out-delivery-and-vending-machines.md#write-the-ticket), and a human who meets the five authorizer conditions of [Informed Intent](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#2-informed-intent) authorizes it before it runs.

## What makes one lean

The test is the author's: "AI should take busywork away from the Human, not manufacture more of it to check." Six things serve it.

- **By hand first.** A person does the task on the cases before any model does, so that done and its abnormalities can be defined.
- **Ordinary software where a rule can be stated.** A model is used only where the work needs judgment, and then in the smallest configuration that clears the cases.
- **The check comes before the person.** Each step carries its own test, so that the owner's minutes go to the cases that need a person.
- **It stops.** At an abnormality it stops and says why. A refusal is a stop and is not retried by another route.
- **Only what is needed.** When there is nothing to report, it reports nothing.
- **It can leave.** The instructions are plain text and the cases are kept outside any provider, so the servant can be run elsewhere or by hand.

## Two stages

1. **Specified.** The card; the definition of done as pass or fail cases with literal, synthetic inputs; a first pass by hand on those cases; the service ticket where tools are used. No instruction text ships at this stage, so nothing is yet an instrument.
2. **Run.** The instruction text and any script; a tests file with its critical cases named; one logged run, with the ledger filled from it; the status under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), stated here and in the account's instrument table.

A servant that fails its run ships as not accepted, with its failures disclosed, and the failed run stays in the record.

## The slate

The servants are drawn from the kinds of work that vendors now package for whole job functions. [*Claude's Plugin Families and The Slow AI Kitchen*](https://github.com/rolldabones/AI-Governance-Academy/blob/main/claude-plugin-families-and-the-slow-ai-kitchen.md) maps one such shelf. That map is a reading of published files, and its Section 12 says so: nothing was run. The servants are where one workflow of each kind is run, tested and costed.

| Order | Kind of work | Working name |
|---|---|---|
| 1 | Legal | Non-disclosure agreement (NDA) triage |
| 2 | Operations | Vendor review |
| 3 | Finance | Reconciliation check |
| 4 | Customer support | Ticket triage |
| 5 | Manufacturing | Production report |
| 6 | Productivity | Weekly status summary |

The order and the names are working ones. The first is a legal workflow because its author is qualified to accept or refuse its output: an hour of oversight counts only from someone who can judge the work.

## Rules

1. **Written from scratch.** No servant adapts a vendor's published instruction files. The kinds of work are common, and the text is the author's, under this repository's license.
2. **Plain text.** The instructions can be read by a person and by any assistant, and the checks are code that needs only a standard library. The first runs are made on Claude, and each run record names its configuration.
3. **Synthetic data only.** No Client data and no personal data is used in a case, a run or a record here.
4. **A case drawn from Client work appears only with the Client's written consent,** anonymized and as derived figures. No Client data is kept in this repository.
5. **Tested, and the record kept.** Each servant's cases, runs, results and failures stay with it, and the [book](../book/README.md) lists them as its appendices.
6. **No doctrine.** A servant applies the Kitchen's method and adds no step, gate, tier, role or rule.

## Index

None yet. The first servant is due at unit 3 of the [plan](../PLAN.md).

**Final Liability rests with the Human.**
