---
id: F24
title: "Cost model and unit economics sheet"
owner: "Business owner, modeled with the architect."
trigger: "At the readiness gate under the commercial dimension; refreshed monthly against actuals."
signatory: "Business owner; finance where the figure enters a business case."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F24. Cost model and unit economics sheet

**Purpose.** Produce the one figure that belongs in a business case and the attribution that keeps it defensible.
**Owner.** Business owner, modeled with the architect.
**Produced.** At the readiness gate under the commercial dimension; refreshed monthly against actuals.
**Signed by.** Business owner; finance where the figure enters a business case.

| Line | Definition | Modeled | Actual month 1 | Actual month 3 | Note |
| --- | --- | --- | --- | --- | --- |
| Volume, expected | Completed tasks per month | 160 | 148 | 171 | |
| Volume, peak | Completed tasks in the peak week | 62 | 58 | 74 | March peak, against F1's 260 for the month and F23's throughput objective |
| Input tokens per attempt | Including retrieved context | 24,000 | 27,400 | 26,100 | Context grew after corpus extension |
| Output tokens per attempt | | 1,800 | 2,050 | 2,010 | |
| Cache hit ratio | Reads against reads plus writes | 0.85 | 0.71 | 0.88 | Month 1 dip was a changed prefix |
| Call multiplier | Model calls per attempt, including graders | 2.4 | 3.1 | 2.5 | Judge calls counted |
| Retrieval and tool cost per attempt | | 0.04 | 0.04 | 0.04 | |
| **Cost per attempt** | Model plus retrieval plus tools for one run | 0.31 | 0.44 | 0.33 | The engineering number |
| **Attempts per completed task** | Including retries and re-asks | 1.2 | 1.9 | 1.3 | The largest multiplier and a quality problem wearing a cost costume |
| **Human minutes per completed task** | Review, correction, escalation handling | 9 | 16 | 10 | Usually dominant and usually unmeasured |
| Loaded cost per human minute | Fully loaded | 1.40 | 1.40 | 1.40 | |
| **Fully loaded cost per completed task** | All three combined | 12.97 | 23.24 | 14.43 | The only figure for a business case |
| Baseline cost per completed task | The process before the system: 95 human minutes at the loaded rate, from F1's measured touch time | 133.00 | 133.00 | 133.00 | Held constant across the period; re-measure before the saving is claimed again |

```
SENSITIVITY, the three that move the answer and the one
that does not
 Attempts per completed task +0.5   -> +__ per task
 Human minutes +3                   -> +__ per task
 Cache hit ratio -0.2               -> +__ per task
 Model unit price +20%              -> +__ per task
 Note which is largest. It is almost never the last one

ATTRIBUTION, built on day one
 Every call carries a cost tag: tenant, business unit, use
 case, feature, task class
 Retrofitting attribution across a shared deployment is
 close to impossible, and unattributed cost becomes a
 central overhead line, which is cut centrally and equally,
 including across the use cases that pay for themselves

BUDGET GUARDRAILS, four, and the fourth is skipped
 Per-request bound   max tokens, max tool calls, max turns
                     -> terminate, log, degrade gracefully
 Per-user or tenant quota, rolling window
                     -> throttle with an explicit message
 Per-use-case budget alert on run rate
                     -> notify the owner, do not stop
 Hard stop, absolute ceiling per use case
                     -> stops the use case. Agreed before
                     launch with a named person who can lift
                     it. A ceiling nobody agreed to in
                     advance becomes an emergency
                     negotiation during an incident

OPERATING LEVERS WHEN AN ALARM FIRES
 Apply the levers in the order of section 8.10.
 Never change the model in response to a cost alarm before
 measuring attempts per completed task
```

**Final Liability rests with the Human.**
