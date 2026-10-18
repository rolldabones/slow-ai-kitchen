# G2. The delegation map

*Enterprise AI Architecture Primer, Appendix G, entry G2. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart LR
    subgraph WORK ["THE WORK, step by step"]
        subgraph STEPS ["step"]
            direction TB
            S1["extract"]
            S2["resolve ID"]
            S3["apply rule"]
            S4["compare"]
            S5["decide"]
            S6["file"]
            S1 ~~~ S2 ~~~ S3 ~~~ S4 ~~~ S5 ~~~ S6
        end
        CL["CLAUDE"]
        ES["EXISTING SYSTEM"]
        HU["HUMAN"]
        S1 -->|"[X]"| CL
        S2 -->|"[X]"| ES
        S3 -->|"[X] #lt;- never a prompt"| ES
        S4 -->|"[X]"| CL
        S5 -->|"[X]"| HU
        S6 -->|"[X]"| ES
    end
    AX["For each assignment, three independent axes:<br/>REVERSIBILITY   can it be undone, by whom, at what cost<br/>STAKES          magnitude of one bad outcome<br/>ACCOUNTABILITY  who answers for it"]
    subgraph VER ["For every step assigned to Claude:"]
        direction LR
        VS["step"] --> VQ["[ what verifies it? ]"] --> VB["if blank,<br/>add verification<br/>or move the step"]
    end
    OC["Three outcome classes<br/>AI-appropriate #124; human-retained #124; collaborative<br/>(Claude drafts, a person decides)"]
    WORK ~~~ AX
    AX ~~~ VER
    VER ~~~ OC
    class AX,OC note
    classDef note stroke-dasharray: 4 4
```

**What it shows.** Ownership of each step was decided rather than defaulted, and the second owner is existing systems, meaning what the organization already paid to make reliable.

**Three things to point at.** The middle column, which is the one teams forget. The verification arrow, which is empty on at least one row in most real designs. The deterministic rule sitting in the existing-system column, because that is the row that migrates into a prompt when nobody is watching.

**The failure it makes visible.** Over-assignment to the model. Absence of this map is the best single predictor of it, and the map takes ten minutes to draw and an hour to argue about, which is the hour worth having.

<details><summary>ASCII original</summary>

```
  THE WORK, step by step
  ---------------------------------------------------------
  step        CLAUDE      EXISTING SYSTEM     HUMAN
  ---------------------------------------------------------
  extract       [X]
  resolve ID                   [X]
  apply rule                   [X]   <- never a prompt
  compare       [X]
  decide                                       [X]
  file                         [X]
  ---------------------------------------------------------
  For each assignment, three independent axes:
     REVERSIBILITY   can it be undone, by whom, at what cost
     STAKES          magnitude of one bad outcome
     ACCOUNTABILITY  who answers for it

  For every step assigned to Claude:
        step ---> [ what verifies it? ] ---> if blank,
                                             add verification
                                             or move the step

  Three outcome classes
     AI-appropriate | human-retained | collaborative
     (Claude drafts, a person decides)
```

</details>

**Final Liability rests with the Human.**
