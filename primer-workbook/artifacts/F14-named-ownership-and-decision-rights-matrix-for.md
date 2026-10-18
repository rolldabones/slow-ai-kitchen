---
id: F14
title: "Named ownership and decision rights matrix for the AI lifecycle"
owner: "Governance, risk management and compliance function."
trigger: "At program establishment; owner attestation at the review cadence."
signatory: "The accountable executive for the program."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F14. Named ownership and decision rights matrix for the AI lifecycle

**Purpose.** Put a person, not a team, against every asset and every decision, so that questions have an addressee and commitments survive reorganization.
**Owner.** Governance, risk management and compliance function.
**Produced.** At program establishment; owner attestation at the review cadence.
**Signed by.** The accountable executive for the program.

**Part one, the asset register.** Seven fields and no more. Everything else belongs in the artifact.

| Asset ID | Asset | Accountable person | Deputy | Tier of the system it serves | Last attestation | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| PRM-014 | Contract review system prompt | A. Okafor | R. Lindqvist | T3 | 2026-03-01 | 2026-06-01 (illustrative) |
| RET-002 | Policy corpus and filters | D. Marsh | S. Iyer | T3 | 2026-03-01 | 2026-06-01 (illustrative) |
| CTL-007 | Pre-action approval gate | J. Ferreira | M. Adeyemi | T3 | 2026-03-01 | 2026-06-01 (illustrative) |

**Part two, decision rights.** Exactly one Accountable per row. Fill with role titles the organization actually has.

| Lifecycle stage | Accountable | Responsible | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Intake and tiering | Business system owner | Architect | Second-line risk, privacy, security | Governance committee |
| Design approval | Architect | Delivery team | Second-line risk, security, privacy, legal at T3 and above | System owner |
| Data approval | Data owner for the source system | Delivery team | Privacy, legal, records management | Architect, system owner |
| Evaluation sign-off | Quality owner | Delivery team | Second-line risk, affected business function | Governance committee |
| Go-live | Business system owner at T1, function head at T2, governance committee at T3, executive or board at T4 | Delivery lead | Security, operations, second line | All parties |
| Change | Asset owner for the asset changed | Delivery team | Second line where the change crosses a re-tier trigger | System owner |
| Incident | Incident commander, pre-named per tier | Response team | Legal, privacy, communications, second line | Executive, per severity |
| Retirement | Business system owner | Delivery team | Records management, legal for holds, privacy for erasure | Governance committee |

```
NON-DELEGABLE DECISIONS, listed explicitly in the charter
 Tier assignment at T4
 Acceptance of residual risk above the stated appetite
 Approval to deploy without a required control
 Any decision binding the organization's position on
 privilege or on regulatory classification

DELEGATION RULES
 To a named individual only, never a team, vendor or committee
 The delegate holds the authority and the budget to discharge
 it. Delegation without resource is abandonment with paperwork
 Recorded, dated and time-bounded. Permanent delegation is a
 role change and is processed as one

SUCCESSION
 Every deputy has performed the role at least once
 Vacancy has a maximum duration by tier, after which the asset
 is suspended rather than left unowned
 Owner departure is a re-tier trigger at T3 and above
```

**Final Liability rests with the Human.**
