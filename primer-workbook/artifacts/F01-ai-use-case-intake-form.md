---
id: F1
title: "AI use case intake form"
owner: "Requesting business function, completed with the architect."
trigger: "Before any design work, at first request."
signatory: "Requesting function head, and the architect who accepts it into the pipeline."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F1. AI use case intake form

**Purpose.** Capture enough about a proposed use case to tier it, route it and refuse it without a design phase.
**Owner.** Requesting business function, completed with the architect.
**Produced.** Before any design work, at first request.
**Signed by.** Requesting function head, and the architect who accepts it into the pipeline.

```
INTAKE ID              AI-2026-0147
Requesting function    Procurement
Named business owner   [person, not team]
Deputy                 [person]
Date received          2026-03-04

THE WORK
Problem in one sentence  Contract review before signature is a
                         12 day queue and the queue is the risk
Unit of work (case)      One inbound supplier contract, receipt
                         to signature recommendation
Current volume           1,900 per year, peak 260 in March
Current touch time       95 minutes per case, 3 roles
Current failure rate     Escapes to signature with a
                         non-standard indemnity: 4%
Do-nothing consequence   Queue grows 18% on forecast volume
Existing manual path     Yes, fully staffed today

THE PROPOSAL
What Claude would do     Draft clause comparison against the
                         standard playbook, with citations
What stays with systems  Threshold application, workflow state,
                         signature routing
What stays with humans   Every deviation decision
Entry point sought       Internal web application via gateway
Deadline and why         None stated. Confirmed not artificial

INPUTS
Data classes             Confidential. Counterparty commercial
                         terms. No special category identified
Systems of record        Contract lifecycle system, supplier
                         master
Affected population      Internal only at this stage
External exposure        None. No third-party content ingested

BENEFIT
Metric that will move    Days from receipt to recommendation
Baseline value           12.1 days, measured Jan to Feb 2026
Target and by when       6 days by Q4, agreed by the owner
Who claims the benefit   Procurement director, in their own
                         quarterly review

PRELIMINARY POSITION
Estimated tier           T2 pending assessment
Known blockers           None
Routing decision         Accept to design / Return for
                         rework / Refuse, with reason
```

**The two fields that do the work** are the do-nothing consequence and who claims the benefit. A use case with no do-nothing consequence is an enthusiasm. A benefit nobody outside the technology function will claim in their own review will not survive a budget cycle.

**A note on the worked figures, because 9.1 carries a similar one and they are not the same scenario.** This is a procurement function reviewing inbound supplier contracts at 1,900 a year with a 95-minute touch time across three roles. 9.1's briefing is an in-house legal function reviewing commercial contracts, and its 1,900 is the pilot volume over ten weeks at a different touch time and a different failure rate. The coincidence of the number across two contract-review examples is accidental. **Do not reconcile the two or carry a figure from one into the other.**

**Final Liability rests with the Human.**
