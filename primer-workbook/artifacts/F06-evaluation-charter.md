---
id: F6
title: "Evaluation charter"
owner: "Quality or evaluation owner."
trigger: "Before build, updated at every material change."
signatory: "Quality owner as author, business owner as the party accepting the thresholds and the residual error rate."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F6. Evaluation charter

**Purpose.** Define what good means before anything is built, so that "better" is a number rather than an impression.
**Owner.** Quality or evaluation owner.
**Produced.** Before build, updated at every material change.
**Signed by.** Quality owner as author, business owner as the party accepting the thresholds and the residual error rate.

```
SYSTEM / tier / charter version / date

1 WHAT GOOD MEANS
  Task the system performs, in the business owner's words
  Success criterion, stated as an observable outcome
  Named populations and segments that must be reported
  separately: [payer, service line, jurisdiction, language,
  document type, affected group]
  Explicitly out of scope: __________
  Behavior required on out-of-scope input: [refuse and route]
```

**2. The sets.**

| Set | Size | Source | Frozen | Refresh rule |
| --- | --- | --- | --- | --- |
| Golden set | 400 | Human-labeled real cases | Yes | Add only, never edit |
| Regression suite | 180 | Every fixed production failure | Yes | Add on every fix |
| Labeled retrieval set | 250 | Query to correct chunk | Yes | Add on every gap found |
| Adversarial set | 90 | Red team plus injection cases | Yes | Add on every finding |
| Online sample | Continuous | Stratified live traffic | No | Not applicable |

**3. Graders.** A metric produced by a model grader is reported with the date of its last human calibration attached. An uncalibrated judge score is not admissible evidence for a change.

| Measure | Grader | Rubric | Calibration |
| --- | --- | --- | --- |
| Citation validity | Deterministic check | Offset and span match | Not applicable |
| Criterion coverage | Model judge | Four point, reasons stated first | Human agreement per class, quarterly |
| Faithfulness | Model judge | Binary plus the unsupported span | Human agreement per class, quarterly |
| Overall acceptability | Human, sampled | Written rubric | Inter-rater agreement |

**4. Thresholds.**

| Measure | Threshold | Per segment | Blocks what |
| --- | --- | --- | --- |
| Citation validity | 95% | Yes | Promotion |
| Criterion coverage | 90% | Yes | Promotion |
| False refusal rate | 3% or below | No | Promotion |
| Recall at 8 | 0.92 | Yes | Promotion |

```
5 CADENCE AND SIGN-OFF
  Blocking at change: regression suite, golden set
  Scheduled: labeled retrieval set daily, online sample
  continuous, human review sample weekly
  Shadow evaluation before any model or version change
  Segment representation: no segment below __ cases
  Baseline of the simpler alternative, dated: __________
  Self-disagreement baseline (same input, n runs): __
  Judge model and version: __________ pinned: yes
  Last human calibration: __________ agreement per class: __
  Sign-off on results: quality owner
  Acceptance of the residual error rate: business owner
```

**The business owner is not signing that the system is accurate.** They are signing that they accept a known error rate on a named population with a defined routing rule for the remainder.

**Final Liability rests with the Human.**
