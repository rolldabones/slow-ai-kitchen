---
id: F7
title: "Production readiness gate checklist with signatories"
owner: "Governance, risk management and compliance function operates the gate; the delivery lead presents."
trigger: "Before first production traffic, and again on any change that crosses a re-tier trigger."
signatory: "Eight dimensions, five signatories, each signing only the dimensions they can actually judge. No single approver."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F7. Production readiness gate checklist with signatories

**Purpose.** Stop systems that are not ready, and produce a record of who accepted what when one ships anyway.
**Owner.** Governance, risk management and compliance function operates the gate; the delivery lead presents.
**Produced.** Before first production traffic, and again on any change that crosses a re-tier trigger.
**Signed by.** Eight dimensions, five signatories, each signing only the dimensions they can actually judge. No single approver.

| Dimension | Binary condition | Evidence | Pass | Signatory |
| --- | --- | --- | --- | --- |
| Functional | Scope stated with explicit exclusions; behavior on out-of-scope input defined; output contract enforced outside the model | Scope statement, contract schema, refusal test | Y/N | Business owner |
| Evaluation | Eval suite exists; baseline recorded; performance known by segment; retrieval measured separately; thresholds agreed | Eval report with segment breakdown | Y/N | Business owner |
| Resilience | Behavior defined for transient, validation, business-rule and permission failures; timeouts and retries set; degraded mode defined; load tested at peak and three times peak | Failure matrix, load test results | Y/N | Operational owner |
| Security | Tool capability reviewed against role need; authorization enforced outside the model; injection tested against retrieved and tool content; secrets and egress reviewed | Threat review, test note | Y/N | Security owner |
| Governance | Data path documented; retention and deletion designed including derived artifacts; approvals recorded; risk assessment complete; disclosure agreed | Data flow, records schedule, approval log | Y/N | Governance, risk management and compliance owner |
| Operational | Named operational owner who is not the architect; runbook; on-call route; observability answers "what happened on request X" without redeploying; rollback without a deployment | Runbook, ownership record, trace demonstration | Y/N | Operational owner |
| Commercial | Cost per completed outcome known at expected and three times expected volume; budget approved; hard stop ceiling and lifting authority agreed | Sizing model, budget approval | Y/N | Business owner |
| Change | Prompt, model, tool, corpus and guardrail changes all trigger an eval run; versioning in place; no path to production bypasses the gate | Change policy, pipeline configuration | Y/N | Engineering owner |

```
OUTCOME, exactly three are available
 [ ] Pass. Proceed to shadow, then canary, then full
 [ ] Ship with a time-bounded accepted risk
       condition failed: __________  expires: __________
       accepted by (named person, not a role): __________
       remediation owner and date: __________
 [ ] Do not ship

There is no fourth outcome. The absence of a fourth outcome
is what gives the gate teeth.
```

**Diagnostic on the gate itself.** If no condition could plausibly have blocked any system shipped in the last twelve months, the gate is decorative.

**Final Liability rests with the Human.**
