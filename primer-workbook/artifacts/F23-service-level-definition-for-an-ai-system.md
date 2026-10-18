---
id: F23
title: "Service level definition for an AI system"
owner: "Operational owner, agreed with the business owner."
trigger: "At the readiness gate, before launch."
signatory: "Operational owner and business owner. Not negotiated during an incident."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F23. Service level definition for an AI system

**Purpose.** Commit to what can be committed to, and state plainly the one thing that cannot.
**Owner.** Operational owner, agreed with the business owner.
**Produced.** At the readiness gate, before launch.
**Signed by.** Operational owner and business owner. Not negotiated during an incident.

| Indicator | Objective | Measured how | Measurement lag | Consequence of breach |
| --- | --- | --- | --- | --- |
| Availability | 99.5% monthly, pass-through of the provider minus our own | Gateway success rate | Seconds | Incident, and the disclosure that this is pass-through |
| Latency, time to first token | p95 under 2.5 seconds where a human is waiting | Per request at the gateway | Seconds | Investigate. Report p50, p90, p95, p99 separately, never a mean |
| Latency, end to end | p95 under 40 seconds, segmented by task class and turn count | Per run | Seconds | A p99 that doubles with a flat p50 is a retry loop or a non-converging agent |
| Throughput | 260 cases in the peak month, about 13 per working day, with rate-limit headroom of 40% | Gateway | Seconds | Capacity review |
| Task completion rate | 92% of runs reach a usable output without escalation | Run outcome field | Minutes | Leading quality indicator, investigate |
| Escalation and override rate | Between 8% and 20% | Review event records | Minutes to hours | Outside the band in either direction triggers investigation of the control, not the population |
| Quality | Criterion coverage 90% per segment on the golden set, 88% on the online stratified sample | Graded sample | Hours to days | Error budget consumption |
| Reviewer capacity | 40 reviews per reviewer per day, one reviewer rostered with a named deputy | Roster and queue depth | Days | 40 a day against 13 at peak, which is the three-times-peak headroom the gate requires. Throughput is capped by this and it is a hard constraint |
| Detection latency | Under 24 hours for a systematic quality regression | Time from first bad output to detection | Days | The number that converts an abstract quality argument into a quantity of harm |
| Recovery time objective | 4 hours | Exercise | n/a | Resilience review |
| Recovery point objective | 15 minutes | Exercise | n/a | Resilience review |
| Recovery quality objective | Not below 80% criterion coverage during degraded operation | Eval suite against the degraded path | Hours | A system technically available while producing materially worse output is not recovered |

```
ERROR BUDGET
 Quality objective 90% on the named population. Budget is
 the gap to 100% over the period.
 While intact: ship changes.
 When exhausted: only changes that restore quality.
 Agreed before launch, not negotiated during an incident.

THE HONEST STATEMENT, in the agreement itself
 We commit to availability, to latency percentiles, to a
 measured quality level on a named population with a
 defined routing rule for the remainder, and to a response
 procedure when quality misses.
 We do not commit to correctness on any individual case.
 Saying this at signature is the difference between a
 defensible agreement and an argument in month four.

DEGRADED MODES, in descending capability
 Full service | Reduced capability (smaller model, narrower
 tools, higher human review rate, defined trigger) |
 Human-only (requires the manual path to exist and be
 staffed) | Suspended (with a defined communication and a
 named authority to declare it)
```

**Final Liability rests with the Human.**
