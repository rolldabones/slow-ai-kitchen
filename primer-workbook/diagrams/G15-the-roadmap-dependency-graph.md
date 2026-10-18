# G15. The roadmap dependency graph

*Enterprise AI Architecture Primer, Appendix G, entry G15. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart TD
    GMA["[ Governed model access + contracted terms ]"]
    IE["[ Identity #amp; entitlement ]"]
    EH["[ Evaluation<br/>harness ]"]
    OB["[ Observability<br/>#amp; evidence ]"]
    GMA --> IE
    GMA --> EH
    GMA --> OB
    KL["[ Knowledge layer:<br/>ingest, freshness,<br/>deletion ]"]
    IE --> KL
    CTL["[ Control layer with<br/>failure behavior ]"]
    OPM["[ Operating model:<br/>owners, support ]"]
    KL & EH & OB --> CTL & OPM
    U1["[ UC1: internal<br/>assistant ]<br/>needs 1,2,3"]
    U2["[ UC2: regulated<br/>decision ]<br/>needs ALL"]
    U3["[ UC3: client<br/>facing ]<br/>needs ALL<br/>+ exit plan"]
    CTL & OPM --> U1 & U2 & U3
    N1["Read from the BOTTOM. A use case cannot be scheduled<br/>before every box above it is complete.<br/>Order by dependency and by the political capital each<br/>item generates or consumes. Where those conflict,<br/>dependency wins."]
    U2 ~~~ N1
    class N1 note
    classDef note stroke-dasharray: 4 4
```

**What it shows.** Capability sequence rather than a list of use cases, with each use case's prerequisites visible.

**Three things to point at.** The entitlement layer, which no single use case pays for and without which four are impossible. The regulated use case sitting last, because sequencing it early means either shipping without controls or a public failure on the most-watched item. The exit plan attached to the client-facing case rather than treated as an end-of-life activity.

**The failure it makes visible.** Which budget cut costs a quarter and which cut costs the program. A roadmap that shows only use cases cannot answer that question, so the committee cuts by cost and removes a foundation.

<details><summary>ASCII original</summary>

```
   [ Governed model access + contracted terms ]
              |
              +--------------------+-------------------+
              v                    v                   v
   [ Identity & entitlement ]  [ Evaluation ]   [ Observability
              |                  harness ]        & evidence ]
              v                    |                   |
   [ Knowledge layer:              |                   |
     ingest, freshness,            |                   |
     deletion ]                    |                   |
              |                    |                   |
              +--------+-----------+---------+---------+
                       v                     v
              [ Control layer with    [ Operating model:
                failure behavior ]      owners, support ]
                       |                     |
          +------------+------+--------------+
          v                   v              v
   [ UC1: internal      [ UC2: regulated  [ UC3: client
     assistant ]          decision ]        facing ]
     needs 1,2,3          needs ALL         needs ALL
                                            + exit plan

   Read from the BOTTOM. A use case cannot be scheduled
   before every box above it is complete.
   Order by dependency and by the political capital each
   item generates or consumes. Where those conflict,
   dependency wins.
```

</details>

**Final Liability rests with the Human.**
