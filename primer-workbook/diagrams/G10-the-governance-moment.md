# G10. The governance moment

*Enterprise AI Architecture Primer, Appendix G, entry G10. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart TD
    subgraph TWIN ["EVERY ARCHITECTURAL DECISION HAS A TWIN"]
        direction LR
        subgraph TECH ["TECHNICAL DECISION"]
            direction TB
            TD1["which model, which version"]
            TD2["what the agent may call"]
            TD3["what is indexed"]
            TD4["where the human gate sits"]
            TD5["what is logged"]
            TD6["how it fails"]
        end
        subgraph GOVD ["GOVERNANCE DECISION"]
            direction TB
            GD1["who approves a change to it,<br/>and what evidence is produced"]
            GD2["who grants the scope, who<br/>recertifies it, on what cycle"]
            GD3["who may write to the corpus,<br/>whose entitlements filter it"]
            GD4["what an objection does, and<br/>who may overrule it"]
            GD5["who may read it, how long it<br/>is kept, and it is now<br/>regulated data"]
            GD6["who is told, on what clock,<br/>and who decides notification"]
        end
        TD1 --> GD1
        TD2 --> GD2
        TD3 --> GD3
        TD4 --> GD4
        TD5 --> GD5
        TD6 --> GD6
    end
    MS["MADE AT THE SAME MOMENT<br/>by the same person, in the same record"]
    TECH --> MS
    GOVD --> MS
    N1["Made later, the governance decision is made by whoever is<br/>present when the question arrives, which is usually the<br/>person with the least authority to answer it."]
    MS ~~~ N1
    class N1 note
    classDef note stroke-dasharray: 4 4
```

**What it shows.** Governance is not a review stage after design. Each technical decision carries a governance decision that is cheapest to make at the same moment.

**Three things to point at.** The pairing itself, which is the whole idea. The logging row, because every observability decision is simultaneously a compliance decision and creates regulated data. The bottom line, because deferred governance decisions are not deferred, they are delegated downward by accident.

**The failure it makes visible.** A design document with a separate governance annex, which is the physical form of a decision made twice by two people who never spoke.

<details><summary>ASCII original</summary>

```
  EVERY ARCHITECTURAL DECISION HAS A TWIN
  ---------------------------------------------------------
  TECHNICAL DECISION            GOVERNANCE DECISION
  ---------------------------------------------------------
  which model, which version -> who approves a change to it,
                                and what evidence is produced
  what the agent may call    -> who grants the scope, who
                                recertifies it, on what cycle
  what is indexed            -> who may write to the corpus,
                                whose entitlements filter it
  where the human gate sits  -> what an objection does, and
                                who may overrule it
  what is logged             -> who may read it, how long it
                                is kept, and it is now
                                regulated data
  how it fails               -> who is told, on what clock,
                                and who decides notification
  ---------------------------------------------------------
       |                                       |
       +------------------+--------------------+
                          v
             MADE AT THE SAME MOMENT
             by the same person, in the same record

  Made later, the governance decision is made by whoever is
  present when the question arrives, which is usually the
  person with the least authority to answer it.
```

</details>

**Final Liability rests with the Human.**
