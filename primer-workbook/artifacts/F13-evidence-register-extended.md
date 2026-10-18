---
id: F13
title: "Evidence register, extended"
owner: "Each row has its own named owner. The governance, risk management and compliance function owns the register."
trigger: "At design, because generation triggers must be built rather than added."
signatory: "Governance, risk management and compliance owner; each row owner attests their own row at the review cadence."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F13. Evidence register, extended

**Purpose.** The primer's Practice Layer register lists what to demand of a design under review. This extension lists what the architecture must emit while it runs, with the trigger that produces it.
**Owner.** Each row has its own named owner. The governance, risk management and compliance function owns the register.
**Produced.** At design, because generation triggers must be built rather than added.
**Signed by.** Governance, risk management and compliance owner; each row owner attests their own row at the review cadence.

The base register is section 4.9 of the Primer; use it as the starting rows. The rows below are the operating-effectiveness additions beyond 4.9, each of which requires the build to emit something continuously.

| Control | Artifact emitted | Owner | Generation trigger | Retention | Assertion supported |
| --- | --- | --- | --- | --- | --- |
| Judge calibration | Human agreement per class with date | Quality owner | Quarterly and on judge model change | Rolling 24 months | Metrics produced by a model grader are trustworthy |
| Completeness | Independent event count from the gateway, identity provider or billing record, reconciled to the audit log | Platform owner | Daily | Per tier logging retention | The logged population is the whole population |

```
THE THREE CONCEPTS EVERY ASSURANCE CONVERSATION USES
 Population     the complete set of events subject to the
                control in the period. Asked for before any
                sample. This is why the audit log is complete
                and not sampled
 Completeness   demonstration that the population is whole,
                by reconciliation to an independent count.
                If the platform is the only source of its own
                event count, the assertion is circular
 Sampling       how operating effectiveness is tested once
                the population is established. One deviation
                in a small sample can invalidate the period

The gap that sinks first audits is completeness, not quality.
Design the independent counter on day one. It is small work
at design time and impossible retrospectively.
```

**Final Liability rests with the Human.**
