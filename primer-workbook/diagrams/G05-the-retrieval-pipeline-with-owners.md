# G5. The retrieval pipeline with owners

*Enterprise AI Architecture Primer, Appendix G, entry G5. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart TD
    subgraph PIPE [" "]
        direction LR
        SRC["SOURCE<br/>(biz)"] --> ING["INGEST<br/>(data)"] --> PAR["PARSE<br/>(data)"] --> ENR["ENRICH<br/>(data)"] --> CHU["CHUNK<br/>(arch)"] --> EMB["EMBED<br/>(arch)"]
        EMB --> IDX["INDEX<br/>(platform)"]
        IDX --> RET["RETRIEVE<br/>(arch)"]
        RET --> RR["RERANK<br/>(arch)"]
        RR --> ASM["ASSEMBLE<br/>(arch)"] --> GEN["GENERATE<br/>(arch)"] --> CIT["CITE<br/>(arch)"] --> EVA["EVALUATE<br/>(quality)"]
        SRC --- EVA
        RET -->|"query log"| EVA
    end
    subgraph TBL ["STAGE / WHAT BREAKS / INSTRUMENT THAT SEES IT"]
        direction TB
        T1["source #124; wrong authority, stale #124; estate inventory"]
        T2["ingest #124; silently not collected #124; document count reconcile"]
        T3["parse #124; tables flattened #124; parse fidelity sampling"]
        T4["enrich #124; metadata absent #124; metadata completeness"]
        T5["chunk #124; mid-idea cuts #124; chunk inspection"]
        T6["embed #124; version changed silently #124; embedding version log"]
        T7["index #124; stale, partial rebuild #124; freshness monitor"]
        T8["retrieve #124; filters after ranking #124; recall at k, labeled set"]
        T9["rerank #124; right chunk cut #124; recall before/after"]
        T10["assemble #124; truncation drops answer #124; assembled-context capture"]
        T11["generate #124; correct context, wrong reading  #lt;- the ONLY genuine model failure #124; faithfulness grading"]
        T12["cite #124; citation does not support #124; citation accuracy"]
        T13["evaluate #124; nothing measured, so nothing above is visible #124; instrument the eval suite itself"]
        T1 ~~~ T2 ~~~ T3 ~~~ T4 ~~~ T5 ~~~ T6 ~~~ T7 ~~~ T8 ~~~ T9 ~~~ T10 ~~~ T11 ~~~ T12 ~~~ T13
    end
    PIPE ~~~ TBL
```

**What it shows.** Retrieval is thirteen stages with distinct owners, distinct failures and distinct instruments, not a technique.

**Three things to point at.** The owner row, where the first four stages belong to the business and to data engineering rather than to architecture. The single stage that is a model failure. The query log feeding back into evaluation, which is the loop most implementations never close.

**The failure it makes visible.** Failure attribution. "The answer was wrong" is reported as a model defect nearly always and is one nearly never. Teams upgrade models against a corpus problem, see no improvement and conclude the technology is immature.

<details><summary>ASCII original</summary>

```
 SOURCE -> INGEST -> PARSE -> ENRICH -> CHUNK -> EMBED
 (biz)     (data)    (data)   (data)   (arch)  (arch)
   |                                              |
   |                                              v
 EVALUATE <- CITE <- GENERATE <- ASSEMBLE <- RERANK <- INDEX
 (quality)  (arch)   (arch)      (arch)     (arch)  (platform)
   ^                                              |
   |                RETRIEVE (arch) <-------------+
   +------------------ query log -----------------+

 STAGE          WHAT BREAKS          INSTRUMENT THAT SEES IT
 source     wrong authority, stale   estate inventory
 ingest     silently not collected   document count reconcile
 parse      tables flattened         parse fidelity sampling
 enrich     metadata absent          metadata completeness
 chunk      mid-idea cuts            chunk inspection
 embed      version changed silently embedding version log
 index      stale, partial rebuild   freshness monitor
 retrieve   filters after ranking    recall at k, labeled set
 rerank     right chunk cut          recall before/after
 assemble   truncation drops answer  assembled-context capture
 generate   correct context, wrong   faithfulness grading
            reading  <- the ONLY genuine model failure
 cite       citation does not support citation accuracy
 evaluate   nothing measured, so     instrument the eval
            nothing above is visible suite itself
```

</details>

**Final Liability rests with the Human.**
