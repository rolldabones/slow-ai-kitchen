---
id: F22
title: "Exit and decommissioning plan"
owner: "Business system owner, with records management and the resilience owner."
trigger: "At design, as a funded deliverable. Refreshed annually."
signatory: "Business system owner; records management; legal for preservation obligations; privacy for erasure."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F22. Exit and decommissioning plan

**Purpose.** Design the end at the same moment as the entry, because every obligation the system creates outlives it.
**Owner.** Business system owner, with records management and the resilience owner.
**Produced.** At design, as a funded deliverable. Refreshed annually.
**Signed by.** Business system owner; records management; legal for preservation obligations; privacy for erasure.

```
SYSTEM / tier / plan version / date

1 EVIDENCE PRESERVATION
 Artifacts that must outlive the system: logs, evaluation
 results, decision records, model identifiers, prompt
 versions, human review records, lineage
 Retention period: set by the limitation period, the
 regulatory retention obligation and the client contract.
 This is counsel's determination, not an engineering default
 Extraction format readable without the system: __________
 Rehearsed: date ______

2 RECORD CONTINUITY
 Outputs that entered a business record: __________
 The context preserved alongside each at creation: prompt
 version, corpus version, model identifier, retrieved set
 An output whose meaning depended on artifacts that no
 longer exist is a record nobody can explain, and
 reconstruction at the end is generally impossible

3 MANUAL CAPABILITY RESTORATION
 Does the manual path still exist:  Y / N
 Last exercised with real volume:  ______
 Staff trained on it today:  ____ of ____
 Time and cost to restore:  ______
 This is the workstream discovered late and it can add two
 quarters

4 DATA DISPOSITION
 Per artifact: corpora, indexes, embeddings, caches,
 evaluation sets, logs, adapted artifacts, memory stores,
 analytics extracts
 | Artifact | Retention basis | Destruction method | Owner | Evidence |
 The derived-artifact map that erasure needed is the map
 decommissioning needs

5 DEPENDENCY UNWINDING
 Downstream processes, reports, controls and systems that
 consume this system's output, including undocumented ones
 Discovered by instrumenting consumption before announcing
 the end date, not by asking

6 KNOWLEDGE CAPTURE
 Why it was built, what it learned, why it is ending

7 IF THIS IS A MIGRATION RATHER THAN A SHUTDOWN
 Behavioral difference by segment, both systems against the
 same labeled set. The new system will be worse on some
 segment. Find it before cutover
 Users' working methods invalidated: treat as an adoption
 event with its own enablement
 Evidence continuity across the boundary: identifiers and
 format that permit a question spanning the cutover date
 Parallel running: cost ______ end date ______, both stated
 at the decision. Parallel running with no end date becomes
 permanent and is worse than either alternative

8 SUBSTITUTABILITY, carried from F15
 Current level L__  Target L__  Cost and duration of exit __
```

**Final Liability rests with the Human.**
