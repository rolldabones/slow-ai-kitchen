# G14. The adoption funnel

*Enterprise AI Architecture Primer, Appendix G, entry G14. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart TD
    subgraph HDR [" "]
        direction LR
        H1["STAGE"] ~~~ H2["METRIC"] ~~~ H3["FAILURE AT THIS STAGE"]
    end
    subgraph R1 [" "]
        direction LR
        S1["AWARE"] ~~~ M1["%  of eligible who know<br/>it exists and what for"] ~~~ F1["communication gap"]
    end
    subgraph R2 [" "]
        direction LR
        S2["PROVISIONED"] ~~~ M2["%  with working access<br/>(login + entitlement)"] ~~~ F2["access friction,<br/>licensing, approval<br/>queue"]
    end
    subgraph R3 [" "]
        direction LR
        S3["ACTIVATED"] ~~~ M3["%  who completed one real<br/>task, not a demo"] ~~~ F3["no trigger in the<br/>workflow; first task<br/>chosen badly"]
    end
    subgraph R4 [" "]
        direction LR
        S4["HABITUAL"] ~~~ M4["%  active in 4 of the<br/>last 6 weeks on real<br/>work"] ~~~ F4["value not felt; review<br/>burden exceeds saving"]
    end
    subgraph R5 [" "]
        direction LR
        S5["DEPENDENT"] ~~~ M5["%  who would escalate if<br/>it were unavailable"] ~~~ F5["never reached: system<br/>is peripheral to the<br/>real work"]
    end
    subgraph R6 [" "]
        direction LR
        S6["ADVOCATE"] ~~~ M6["%  who onboarded another<br/>user or contributed a<br/>correction or template"] ~~~ F6["no social proof; the<br/>program relies on<br/>push forever"]
    end
    HDR ~~~ R1
    R1 --> R2
    R2 --> R3
    R3 --> R4
    R4 --> R5
    R5 --> R6
    N1["The RATIO between adjacent stages diagnoses.<br/>The absolute numbers do not.<br/>DEPENDENT is the only stage that predicts survival of a<br/>budget cycle."]
    R6 ~~~ N1
    class N1 note
    classDef note stroke-dasharray: 4 4
```

**What it shows.** Six stages, one metric each, one distinct failure each.

**Three things to point at.** The ratio rule: eighty percent provisioned against nine percent activated is a workflow-entry problem, and no amount of awareness work will move it. The dependent stage, which is the only honest predictor of survival. The advocate stage, whose absence means the program pushes forever.

**The failure it makes visible.** A healthy-looking usage number covering a system nobody would escalate about, which will be cut, and the cut will be justified using the same usage number.

<details><summary>ASCII original</summary>

```
  STAGE          METRIC                  FAILURE AT THIS STAGE
  -----          ------                  ---------------------
  AWARE       %  of eligible who know    communication gap
    |            it exists and what for
    v
  PROVISIONED %  with working access     access friction,
    |            (login + entitlement)   licensing, approval
    v                                    queue
  ACTIVATED   %  who completed one real  no trigger in the
    |            task, not a demo        workflow; first task
    v                                    chosen badly
  HABITUAL    %  active in 4 of the      value not felt; review
    |            last 6 weeks on real    burden exceeds saving
    v            work
  DEPENDENT   %  who would escalate if   never reached: system
    |            it were unavailable     is peripheral to the
    v                                    real work
  ADVOCATE    %  who onboarded another   no social proof; the
                 user or contributed a   program relies on
                 correction or template  push forever

  The RATIO between adjacent stages diagnoses.
  The absolute numbers do not.
  DEPENDENT is the only stage that predicts survival of a
  budget cycle.
```

</details>

**Final Liability rests with the Human.**
