---
id: F18
title: "Change record for a prompt, model, tool, corpus or guardrail change"
owner: "The asset owner for the asset being changed."
trigger: "Per change, before it reaches production."
signatory: "The approver named per change type."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F18. Change record for a prompt, model, tool, corpus or guardrail change

**Purpose.** Apply one gate to all five change surfaces, because the fourth is ungoverned nearly everywhere.
**Owner.** The asset owner for the asset being changed.
**Produced.** Per change, before it reaches production.
**Signed by.** The approver named per change type.

| Field | Entry |
| --- | --- |
| Change ID and date | CHG-2026-0412, 2026-04-12 |
| Change type | Corpus publication |
| Asset changed | RET-002 policy corpus, 41 documents superseded |
| Requested by | Contract counsel |
| Description | Playbook v4 replaces v3 across all jurisdictions |
| Crosses a re-tier trigger | Yes, corpus class unchanged but scope extended to a second jurisdiction |
| Eval run required | Labeled retrieval set plus golden set |
| Eval result | Recall at 8: 0.93 (was 0.92). Criterion coverage 91% overall, 84% in the new jurisdiction segment |
| Segment regression | Yes, new jurisdiction below threshold |
| Decision | Hold. Extend the labeled set for the new jurisdiction before publication |
| Rollback method | Republish v3, no deployment, under 10 minutes |
| Rollback rehearsed | Yes, 2026-03-20 |
| Approver | Knowledge owner |
| Second-line consulted | Yes, re-tier trigger crossed |

```
MINIMUM GATE BY CHANGE TYPE
 Prompt            regression suite plus golden set, offline
                   before online                 -> quality owner
 Model or version  shadow evaluation, then canary with
                   guardrail metrics   -> quality and business owner
 Tool added or scope widened   security review plus regression
                   suite                        -> security owner
 Corpus publication  validation gate plus labeled retrieval
                   set                         -> knowledge owner
 Guardrail or threshold  regression suite plus false-refusal
                   measurement                  -> quality owner

Corpus changes are made by content owners who are not
engineers, through publication workflows that never touch the
deployment pipeline, and they change behavior as thoroughly
as a prompt edit does. A change policy that governs code and
leaves the corpus ungoverned has left the largest surface
uncontrolled.

A cost reduction is a change. It goes through the same eval
gate or it does not ship.
```

**Final Liability rests with the Human.**
