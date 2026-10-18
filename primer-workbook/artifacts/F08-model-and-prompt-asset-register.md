---
id: F8
title: "Model and prompt asset register"
owner: "Model configuration owner."
trigger: "At first deployment, updated on every change, reconciled to production monthly."
signatory: "Model configuration owner attests quarterly that the register matches production."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F8. Model and prompt asset register

**Purpose.** Know which model version and which prompt text is running where, so that a deprecation notice or a quality change has an answerable blast radius.
**Owner.** Model configuration owner.
**Produced.** At first deployment, updated on every change, reconciled to production monthly.
**Signed by.** Model configuration owner attests quarterly that the register matches production.

| Asset ID | Type | Version | Pinned | Systems using it | Owner | Deputy | Eval set bound to it | Last change | Deprecation horizon | Migration owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRM-014 | System prompt | v7 | n/a | Contract review assistant | A. Okafor | R. Lindqvist | GS-CR-400 | 2026-02-18 | n/a | n/a |
| MDL-002 | Model | sonnet-class, exact identifier recorded | Yes | Contract review, intake triage | A. Okafor | R. Lindqvist | GS-CR-400, GS-IT-120 | 2026-01-06 | Assumed 12 months from pin | Platform lead |
| EMB-001 | Embedding model | v2 | Yes | Policy corpus index | D. Marsh | S. Iyer | RET-250 | 2025-11-02 | Assumed 18 months | Data platform lead |
| TPL-009 | Output template | v3 | n/a | Contract review assistant | A. Okafor | R. Lindqvist | Structural check | 2026-03-01 | n/a | n/a |

```
REGISTER RULES
 The embedding model is a second, separately versioned model
 dependency. Registering the generation model only is the
 common omission and it hides the dependency that forces a
 full reindex when it changes.
 Prompt assets are versioned artifacts, not text in a file
 someone edits. A tool definition change invalidates the
 prompt cache entirely, so tool definitions are registered
 here too and treated as stable.
 Reconciliation: the register is compared to the model
 identifier captured on live requests, monthly. A register
 that has never disagreed with production has never been
 reconciled.
```

**Final Liability rests with the Human.**
