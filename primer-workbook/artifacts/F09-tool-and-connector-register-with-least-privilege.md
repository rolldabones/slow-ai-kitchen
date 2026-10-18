---
id: F9
title: "Tool and connector register with least-privilege review"
owner: "Security owner, maintained with the architect."
trigger: "At design, on every tool addition or scope widening and at scheduled recertification."
signatory: "Security owner; the business owner countersigns any state-changing tool."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F9. Tool and connector register with least-privilege review

**Purpose.** Enumerate every capability the system can exercise, the scope it holds and the justification, so that excess privilege can be removed rather than logged.
**Owner.** Security owner, maintained with the architect.
**Produced.** At design, on every tool addition or scope widening and at scheduled recertification.
**Signed by.** Security owner; the business owner countersigns any state-changing tool.

| Tool ID | What it does | State-changing | Scope granted | Scope actually used (90 days) | Identity used | Justification | Gate | Recertified | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TL-01 | Read contract by ID | No | Read, own tenant | Read, own tenant | End-user delegated | Core function | None | 2026-03-01 | Keep |
| TL-02 | Search supplier master | No | Read all suppliers | Read, 4 fields of 31 | End-user delegated | Counterparty resolution | None | 2026-03-01 | Narrow to 4 fields |
| TL-03 | Create purchase order | Yes | Create, no ceiling | Created 0 in 90 days | Service account | Requested in original design | None | 2026-03-01 | **Remove.** Unused and unbounded |
| TL-04 | Send email to counterparty | Yes | Send as function mailbox | 212 sends | Service account | Acknowledgement only | Pre-action approval | 2026-03-01 | Keep, gate confirmed |

```
REVIEW QUESTIONS, per row
 1 Would a competent engineer be able to say definitively when
   this tool should be used? If not, the model cannot either
 2 Is the granted scope wider than the used scope? Narrow it
 3 Does the tool act as the user or as a shared service
   account? A shared privileged account removes attribution
 4 Is authorization decided outside the model, before the
   action executes?
 5 If this is excess privilege, the answer is removal.
   Logging it, confirming it or gating it does not close the
   exposure
 6 If the catalog is large but each tool is legitimate, this
   is a scale problem and the answer is progressive
   disclosure, not removal. The two problems have different
   answers
```

**Final Liability rests with the Human.**
