---
id: F5
title: "Human oversight design specification"
owner: "Business process owner, designed with the architect."
trigger: "At design, before the readiness gate."
signatory: "Business process owner, who is accepting the capacity commitment, and the operational owner."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F5. Human oversight design specification

**Purpose.** Turn "a human reviews it" into a control with a throughput, a latency, a competence requirement and a defined effect of objection.
**Owner.** Business process owner, designed with the architect.
**Produced.** At design, before the readiness gate.
**Signed by.** Business process owner, who is accepting the capacity commitment, and the operational owner.

```
CONTROL ID / system / step it sits at

PLACEMENT       pre-action approval | post-action review |
                sampled audit | escalation on uncertainty |
                exception only
Preventive or detective?   [sampled audit is detective and
                            is not a safety control]
Trigger         which actions reach a human, stated as a rule
Ungated remainder and its sampling rate

1 INFORMATION   what the reviewer sees
   [ ] the output          [ ] the retrieved set, cited
   [ ] the tool calls made [ ] what was suppressed or refused
   [ ] the specific question they are being asked
   Handoff package format: who, what the issue is, what was
   established, recommended action, why. A raw transcript is
   not a handoff

2 TIME          measured reading time of the material  __ min
                budgeted review time                    __ min
                if budget < reading time the control is
                nominal and must be redesigned
   Volume at peak __ /day. Reviewer capacity __ /day.
   If volume exceeds capacity the design is wrong, not
   the reviewer

3 COMPETENCE    what the reviewer must be able to judge
                substantive: [e.g. whether the cited clause
                supports the recommendation]
                not merely: [that a citation exists]
                qualification held: __________

4 AUTHORITY     effect of an objection: [stops the action]
                who may overrule: [named role]
                record required on overrule: [yes]

5 INCENTIVE     what the reviewer is measured on: __________
                a caught error is recorded as: [a success]
                approvals per hour is NOT a measure

MEASUREMENT     override rate, override direction, time on
                task against reading time, disagreement
                sampling, blind re-review rate, outcome
                tracing on approved items
Investigation threshold: override rate below __% triggers a
review of the control, not congratulation
```

**An oversight control reporting a 100 percent approval rate is evidence of failure.** Either the system needs no oversight and the step should become sampling, or the reviewers are not reviewing. There is no third explanation.

**Final Liability rests with the Human.**
