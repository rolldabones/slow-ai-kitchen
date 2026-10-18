# G8. The human-in-the-loop placements

*Enterprise AI Architecture Primer, Appendix G, entry G8. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart LR
    MO["model output"]
    ACT["ACTION"]
    CON["consequence"]
    MO ~~~ ACT ~~~ CON
    subgraph R1 ["1 PRE-ACTION APPROVAL"]
        H1["[ human ]<br/>blocks"]
    end
    H1 --> ACT
    subgraph R2 ["2 POST-ACTION REVIEW"]
        H2["[ human ]<br/>reviews"]
    end
    ACT --> H2
    H2 -->|"undo window"| CON
    subgraph R3 ["3 SAMPLED AUDIT"]
        S3["[ n% ]"]
    end
    ACT -->|"detective only"| S3
    S3 --> CON
    subgraph R4 ["4 ESCALATION ON UNCERTAINTY"]
        SG4["[ signal? ]"]
        H4["[ human ]"]
        SG4 -->|"yes"| H4
    end
    SG4 -->|"no"| CON
    subgraph R5 ["5 EXCEPTION ONLY"]
        RF5["[ rule flags ]"]
        H5["[ human ]"]
        RF5 -->|"yes"| H5
    end
    RF5 -->|"no"| CON
    N1["1, 4 and 5 are PREVENTIVE.<br/>2 is CORRECTIVE and needs a real undo window.<br/>3 is DETECTIVE and is not a safety control.<br/><br/>Placement 4: route on STRUCTURAL signals (nothing above<br/>threshold, required field absent, value out of range,<br/>schema failure, two passes disagree, amount over limit).<br/>Never on the model's self-reported confidence."]
    CON ~~~ N1
    class N1 note
    classDef note stroke-dasharray: 4 4
```

**What it shows.** Five placements positioned against the action, with the control class of each.

**Three things to point at.** Where each sits relative to the action, because that is what determines whether it prevents anything. Row 3, which is a quality instrument and is routinely presented as a safety control. Row 4's signal list, because the wrong input there is the most common design error in the set.

**The failure it makes visible.** A sampled audit described as the control that makes an irreversible action safe, and post-action review applied to something that cannot actually be reversed, such as anything already sent to a client.

<details><summary>ASCII original</summary>

```
                 model output       ACTION       consequence
                       |              |              |
  1 PRE-ACTION   [ human ]----------->|              |
    APPROVAL      blocks              |              |
                                      |              |
  2 POST-ACTION                       |-->[ human ]->|  undo
    REVIEW                            |    reviews   |  window
                                      |              |
  3 SAMPLED                           |--------->[ n% ]---->
    AUDIT                             |      detective only
                                      |              |
  4 ESCALATION   [ signal? ]--yes-->[ human ]        |
    ON UNCERTAINTY   |--no--------------------------->
                                      |              |
  5 EXCEPTION    [ rule flags ]-yes->[ human ]       |
    ONLY             |--no--------------------------->

  1, 4 and 5 are PREVENTIVE.
  2 is CORRECTIVE and needs a real undo window.
  3 is DETECTIVE and is not a safety control.

  Placement 4: route on STRUCTURAL signals (nothing above
  threshold, required field absent, value out of range,
  schema failure, two passes disagree, amount over limit).
  Never on the model's self-reported confidence.
```

</details>

**Final Liability rests with the Human.**
