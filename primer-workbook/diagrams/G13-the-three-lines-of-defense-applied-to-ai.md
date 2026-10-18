# G13. The three lines of defense applied to AI

*Enterprise AI Architecture Primer, Appendix G, entry G13. Source of record for the text: this file; the ASCII original is preserved below.*

```mermaid
flowchart TD
    L1["FIRST LINE<br/>owns and<br/>runs the<br/>risk"]
    L2["SECOND LINE<br/>sets the<br/>standard and<br/>challenges"]
    L3["THIRD LINE<br/>independent<br/>assurance"]
    M1["business owner<br/>architect<br/>delivery team"]
    M2["risk, compliance,<br/>privacy, security<br/>governance committee"]
    M3["internal audit<br/>external assurance"]
    L1 ~~~ M1
    L2 ~~~ M2
    L3 ~~~ M3
    D1["tiers itself<br/>builds controls<br/>produces<br/>evidence"]
    D2["re-scores a sample<br/>sets the standard<br/>tests design<br/>effectiveness"]
    D3["tests the whole<br/>arrangement,<br/>including whether<br/>line 2 challenged"]
    M1 --- D1
    M2 --- D2
    M3 --- D3
    WB["WHERE IT BREAKS FOR ARTIFICIAL INTELLIGENCE<br/>1 the first line is the only line that understands the<br/>system, so challenge becomes theater<br/>2 the second line cannot test what it cannot read;<br/>evidence must be emitted, not assembled on request<br/>3 the third line arrives after the design is frozen and<br/>finds design defects it can only report"]
    D1 --> WB
    D2 --> WB
    D3 --> WB
    FIX["Fix: second-line calibration sampling, objective<br/>triggers that bypass scoring, and evidence generated<br/>by the system rather than by a person before an audit."]
    WB ~~~ FIX
    class FIX note
    classDef note stroke-dasharray: 4 4
```

**What it shows.** The conventional control model and the three specific places it fails when the first line holds all the expertise.

**Three things to point at.** The calibration-sampling arrow from line two, which is the cheapest working mitigation because it makes optimism visible rather than punishing it. The evidence arrow, which must originate in the running system. Line three's position, arriving late, which is the argument for pulling assurance into the design review at tier 3 and above.

**The failure it makes visible.** Effective challenge that cannot happen because only the builder understands the build. It shows up as a second line that signs everything and an audit finding written a year later about a decision nobody can now reverse.

<details><summary>ASCII original</summary>

```
 +------------+  +------------------+  +--------------------+
 | FIRST LINE |  | SECOND LINE      |  | THIRD LINE         |
 | owns and   |  | sets the         |  | independent        |
 | runs the   |  | standard and     |  | assurance          |
 | risk       |  | challenges       |  |                    |
 +------------+  +------------------+  +--------------------+
 business owner   risk, compliance,     internal audit
 architect        privacy, security     external assurance
 delivery team    governance committee
       |                  |                     |
   tiers itself      re-scores a sample     tests the whole
   builds controls   sets the standard      arrangement,
   produces          tests design           including whether
   evidence          effectiveness          line 2 challenged
       |                  |                     |
       +------------------+---------------------+
                          v
     WHERE IT BREAKS FOR ARTIFICIAL INTELLIGENCE
     1 the first line is the only line that understands the
       system, so challenge becomes theater
     2 the second line cannot test what it cannot read;
       evidence must be emitted, not assembled on request
     3 the third line arrives after the design is frozen and
       finds design defects it can only report

     Fix: second-line calibration sampling, objective
     triggers that bypass scoring, and evidence generated
     by the system rather than by a person before an audit.
```

</details>

**Final Liability rests with the Human.**
