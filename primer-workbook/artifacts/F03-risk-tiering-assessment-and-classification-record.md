---
id: F3
title: "Risk tiering assessment and classification record"
owner: "Business system owner, scored with the architect."
trigger: "At intake, and on any of the nine re-tier triggers."
signatory: "Business system owner; second-line risk owner countersigns at tier 3 and above."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F3. Risk tiering assessment and classification record

**Purpose.** Assign the tier that determines how much of the control set applies, and record the reasoning so the assignment can be challenged.
**Owner.** Business system owner, scored with the architect.
**Produced.** At intake, and on any of the nine re-tier triggers.
**Signed by.** Business system owner; second-line risk owner countersigns at tier 3 and above.

| Dimension | Score 0 to 4 | Evidence for the score |
| --- | --- | --- |
| Autonomy | 1 | Draft only, no state change, no outbound message |
| Reversibility | 1 | A bad draft is discarded at no cost |
| Stakes | 3 | A missed indemnity in a live negotiation is material |
| Affected population | 1 | Internal professionals who chose the tool |
| Data sensitivity | 4 | Privileged and commercially confidential material |
| External exposure | 1 | Internal corpus, no untrusted ingestion |
| Regulatory character | 1 | No specific regime identified for this use |
| Novelty | 2 | Second deployment of an established pattern |
| **Raw total** | **14** | Band T2 before overrides |

```
OVERRIDES APPLIED
 [x] 1  any single dimension at 4 floors the tier at T3
 [ ] 2  output affects legal rights, entitlements, employment,
        credit, health or liberty: floor T3 plus human decision
        authority
 [ ] 3  autonomy >= 3 AND reversibility <= 1: floor T4
 [ ] 4  novelty = 4: one tier above computed for the first
        operating period, then re-score

FINAL TIER              T3
Rationale               Data sensitivity carries the entire
                        risk. Low autonomy misleads here
Control consequences    Data protection impact assessment,
   forced by the tier   third-party assessment, privilege
                        segregation, retrieval filtering,
                        quarterly review, staged rollout
Dissent recorded        None / [who disagreed and on what point]
Re-tier triggers armed  All nine: new tool on the allowlist;
                        corpus class change; new user population
                        or jurisdiction; model or version change;
                        any incident; regulatory character
                        change; review cadence lapse; departure
                        of the named owner at T3 and above;
                        change in the recorded purpose of the
                        system or of its corpus
Next scheduled review   2026-09-30 (illustrative)
Regulatory band field   [separate field, left blank unless a
                        determination has been made by counsel]
```

**Never merge the internal tier field with the regulatory classification field.** They classify by different inputs, internal tiering by what the system can do and regulatory schemes typically by what it is for, and a tier quietly relabeled as a legal classification is a misrepresentation waiting to be found.

**Final Liability rests with the Human.**
