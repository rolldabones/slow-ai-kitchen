# G17. The environment and promotion pipeline

*Enterprise AI Architecture Primer, Appendix G, entry G17. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart TD
    subgraph ENV [" "]
        direction LR
        DEV["DEV<br/>real subset<br/>of data<br/>(or the prompt<br/>is tuned<br/>against fiction)"]
        INT["INTEGRATION<br/>real tool<br/>endpoints in<br/>sandbox mode<br/>(mocked tools<br/>hide error<br/>handling and<br/>retries)"]
        EVL["EVALUATION<br/>FROZEN corpus<br/>and index, so<br/>scores compare<br/>across runs"]
        STG["STAGING<br/>LIVE corpus<br/>and index,<br/>shadow and<br/>canary, no<br/>user-visible<br/>output on<br/>the shadow<br/>path"]
        PRD["PRODUCTION<br/>per-request<br/>identity,<br/>trace ids and<br/>model id<br/>captured on<br/>every request"]
        DEV --> INT --> EVL --> STG --> PRD
    end
    PG1["[ PG1 EVAL ]<br/>per-segment thresholds vs frozen sets<br/>plus a self-disagreement baseline"]
    PG2["[ PG2 COST ]<br/>cost per completed outcome at 1x and 3x<br/>volume, cache hit ratio verified"]
    PG3["[ PG3 SAFETY ]<br/>harmful-output rate AND false-refusal<br/>rate, injection resistance, permission<br/>assertions"]
    PG4["[ PG4 OPERABILITY ]<br/>runbook current, owner named and<br/>agreed, rollback rehearsed, alerts wired"]
    ENV --> PG1
    PG1 --> PG2
    PG2 --> PG3
    PG3 --> PG4
    SHD["SHADOW (no user output)"]
    CAN["CANARY (slice)"]
    FUL["FULL"]
    PG4 --> SHD
    SHD --> CAN
    CAN --> FUL
    N1["Every gate is PER SEGMENT. An aggregate pass hides a<br/>segment-level regression, which is how quality leaves<br/>quietly."]
    FUL ~~~ N1
    class N1 note
    classDef note stroke-dasharray: 4 4
```

*Relabel: the promotion gates read "G1 EVAL" to "G4 OPERABILITY" in the ASCII original; they are relabeled PG1 to PG4 (promotion gate) here and in the prose so they do not collide with diagram IDs G1 to G4.*

**What it shows.** Five environments with the artificial-intelligence-specific requirement of each, and four gates that promote a candidate release tuple rather than a code build.

**Three things to point at.** The evaluation environment, which most organizations lack and which is routinely collapsed into staging. The contradiction that forces the separation: eval needs a frozen corpus for comparability, staging needs a live one for realism, and one environment cannot hold both. PG3's paired metrics, because measuring harmful output without measuring false refusal optimizes toward a system that refuses everything.

**The failure it makes visible.** An aggregate pass concealing a segment regression, and a promotion decision made on a corpus that does not resemble production, which makes every retrieval number meaningless.

<details><summary>ASCII original</summary>

```
 DEV ---> INTEGRATION ---> EVALUATION ---> STAGING ---> PRODUCTION
 real     real tool        FROZEN corpus   LIVE corpus  per-request
 subset   endpoints in     and index, so   and index,   identity,
 of data  sandbox mode     scores compare  shadow and   trace ids and
 (or the  (mocked tools    across runs     canary, no   model id
 prompt   hide error                       user-visible captured on
 is tuned handling and                     output on    every request
 against  retries)                         the shadow
 fiction)                                  path
                                                    |
                                                    v
   [ G1 EVAL ]      per-segment thresholds vs frozen sets
        |           plus a self-disagreement baseline
        v
   [ G2 COST ]      cost per completed outcome at 1x and 3x
        |           volume, cache hit ratio verified
        v
   [ G3 SAFETY ]    harmful-output rate AND false-refusal
        |           rate, injection resistance, permission
        v           assertions
   [ G4 OPERABILITY ] runbook current, owner named and
        |             agreed, rollback rehearsed, alerts wired
        v
   SHADOW (no user output) --> CANARY (slice) --> FULL

  Every gate is PER SEGMENT. An aggregate pass hides a
  segment-level regression, which is how quality leaves
  quietly.
```

</details>

**Final Liability rests with the Human.**
