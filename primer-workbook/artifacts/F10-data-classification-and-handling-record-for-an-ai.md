---
id: F10
title: "Data classification and handling record for an AI system"
owner: "Data owner for each source, consolidated by the architect."
trigger: "At design, on any new data source and on any change to the output's purpose."
signatory: "Data owner per source; privacy owner for the record as a whole."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F10. Data classification and handling record for an AI system

**Purpose.** Fix the deployment route, the logging depth and the caching rules before cost or latency is considered.
**Owner.** Data owner for each source, consolidated by the architect.
**Produced.** At design, on any new data source and on any change to the output's purpose.
**Signed by.** Data owner per source; privacy owner for the record as a whole.

| Data element or source | Tier | Enters as | Leaves boundary to | Agreement permitting it | Route permitted | Content logging | Cache scope | Retention | Deletion path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Executed contract text | Confidential | Retrieved chunk | Gateway to managed model route | Enterprise agreement, no training use | Managed private route | Metadata only, content to segregated store | Per tenant and per classification | 30 days audit sink | Source delete propagates to chunks, embeddings, index, cache, assembled-context log, eval sets |
| Supplier bank details | Restricted | Not ingested | Does not leave | n/a | **Does not go to a model** | n/a | n/a | System of record | n/a |
| Reviewer decision record | Confidential | Written by the system | Stays inside | n/a | Internal | Full | Not cached | Per legal retention | Legal hold aware |
| The generated recommendation | Confidential by purpose | Output | Contract system | Internal | Internal | Full | Not cached | Record retention | Business record, not deletable on request |

```
OUTPUT CLASSIFICATION
 Rule: an output's classification is the higher of its
 inputs' classifications and the classification its purpose
 implies. Purpose usually wins.
 Purpose floor for this system: Confidential
 Aggregation check: does combining these sources create
 something more sensitive than any input? [state the answer]

DERIVED ARTIFACT MAP, required before the first erasure
 request arrives, not after
 source record -> chunks -> embeddings -> index entries ->
 response cache -> assembled-context logs -> evaluation sets
 -> memory stores -> analytics extracts
 Named owner able to execute a delete across all nine: ______
```

**Final Liability rests with the Human.**
