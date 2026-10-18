---
id: F2
title: "AI architecture decision record"
owner: "Architect."
trigger: "At design approval, and again on any material change to model, tools, corpus or oversight placement."
signatory: "Architect as author, business system owner as accepting party and for tier 3 and above the governance committee."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F2. AI architecture decision record

**Purpose.** Record the decision, the alternatives and the seven properties an artificial intelligence system has that a deterministic service does not.
**Owner.** Architect.
**Produced.** At design approval, and again on any material change to model, tools, corpus or oversight placement.
**Signed by.** Architect as author, business system owner as accepting party and for tier 3 and above the governance committee.

```
ADR ID / version / date / supersedes
Status        proposed | accepted | superseded | reversed
Context       the situation forcing the decision, 5 lines max
Decision      what will be built, in one sentence
Alternatives  each with the reason it was not chosen

CONVENTIONAL CLAUSES
Criterion     the measure the decision was made against
Consequences  what is now harder, what is now foreclosed

THE SEVEN AI CLAUSES
1 Model dependency and deprecation horizon
    identifier, pinned yes/no, assumed support end,
    migration owner, runway required
2 Non-determinism tolerance
    what may vary between runs, what must not,
    what downstream consumers assume about stability
3 Eval gate
    which set, which threshold, segmented how,
    run by whom, what it blocks
4 Human oversight point
    which of the five placements, at which step,
    handoff package, reviewer capacity assumption
5 Data egress boundary
    what data crosses which line, to whom, under
    which agreement, retained where, for how long
6 Failure mode and blast radius
    what a wrong output does, to how many cases,
    over what period, before detection
7 Reversal path and switching condition
    how to undo, whether undo needs a deployment,
    time to restore, how it was rehearsed, and the
    observable condition that would reopen the decision
```

**Test question per clause, asked out loud before signing.** Who moves this when the model is retired. If we run it twice what may differ. What number on what set blocks production. Which specific action pauses and who is on the other side. Draw the line the data crosses and name the agreement. How many wrong outputs are acted on before anyone notices. Restore the previous behavior, how long, does it need a deploy.

**Final Liability rests with the Human.**
