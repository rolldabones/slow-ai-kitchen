---
id: F4
title: "Delegation map"
owner: "Architect."
trigger: "Before pattern selection, and re-issued whenever a step moves owner."
signatory: "Architect and business process owner."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F4. Delegation map

**Purpose.** Assign every step of the work to Claude, to an existing system or to a human, with the reasoning stated.
**Owner.** Architect.
**Produced.** Before pattern selection, and re-issued whenever a step moves owner.
**Signed by.** Architect and business process owner.

| Step | Owner | Reversibility | Stakes | Accountability | Verified by | Outcome class / routing |
| --- | --- | --- | --- | --- | --- | --- |
| Extract clause set from the contract | Claude | Reversible, draft only | Low | Architect | Schema validation plus citation check | AI-appropriate |
| Resolve counterparty to the supplier master | Existing system | Reversible | Medium | Data owner | Deterministic match, ask on multiple hits | Routed: exact match the supplier master already does reliably |
| Apply the approval threshold | Existing system | Reversible | High | Policy owner | Policy engine test suite | Routed: deterministic rule, never a prompt |
| Compare each clause to the standard playbook | Claude | Reversible | Medium | Architect | Labeled comparison set, quarterly | Collaborative |
| Decide whether a deviation is acceptable | Human | Irreversible once signed | High | Contract counsel | Named reviewer, recorded decision | Human-retained |
| File the executed contract | Existing system | Reversible | Low | Records manager | Records schedule | Routed: records system of record, on its own schedule |

**The three outcome classes describe what Claude does**, and there are exactly three: AI-appropriate, human-retained and collaborative. A step owned by an existing system is recorded here as routed, with the reason, because the three classes describe delegation to the model and say nothing about what the estate already does reliably.

```
COMPLETENESS CHECKS, all four must pass
 [ ] Every step has exactly one owner
 [ ] Every step assigned to Claude names the thing that
     verifies it. If nothing verifies it, add verification
     or move the step
 [ ] No deterministic business rule sits in a prompt
 [ ] Every irreversible or high-stakes step has a human
     owner or a preventive gate, and the ungated remainder
     has a stated sampling rate
```

**Absence of this artifact is the single best predictor of over-assignment to the model.** It is the first thing to ask for in a review and the fastest to read.

**Final Liability rests with the Human.**
