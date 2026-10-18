---
id: F15
title: "Third-party and model provider assessment"
owner: "Vendor relationship owner, with security, privacy and the architect."
trigger: "Before contracting; refreshed annually and on any contract or subprocessor change."
signatory: "Vendor relationship owner, security owner, privacy owner and, for a critical third party, the accountable executive."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F15. Third-party and model provider assessment

**Purpose.** Assess the provider as a critical third party rather than as a software vendor, and record the substitution position before it is needed in anger.
**Owner.** Vendor relationship owner, with security, privacy and the architect.
**Produced.** Before contracting; refreshed annually and on any contract or subprocessor change.
**Signed by.** Vendor relationship owner, security owner, privacy owner and, for a critical third party, the accountable executive.

| Assessment area | Question | Finding | Evidence held | Residual risk | Owner |
| --- | --- | --- | --- | --- | --- |
| Criticality | Would failure of this supplier prevent delivery of an important business service | Yes. Critical third party | Dependency map | Accepted with exit plan | Resilience owner |
| Data handling | What is retained, for how long, where and by whom | Zero retention on the contracted configuration | Contract clause reference, configuration attestation | Configuration drift | Vendor relationship owner |
| Training use | Is customer content used to train | Contractually excluded | Contract clause reference | None | Privacy owner |
| Subprocessors | Who else touches the data, notice of change | Named list, 30 day notice | Subprocessor schedule | Change may arrive without action | Privacy owner |
| Residency | Where is processing performed and where is data at rest | Named region, pinned | Deployment configuration | Failover may cross the boundary | Architect |
| Security posture | Independent assurance held, scope and period | Report held, scope reviewed | Report on file | Scope excludes the service we use | Security owner |
| Availability and support | Committed levels, remedies, support hours, escalation route | Documented | Contract | Pass-through availability only | Operational owner |
| Model lifecycle | Deprecation notice period, version pinning available, change notification | Pinning available, notice stated | Contract and documentation | Provider may change the model behind a stable identifier | Model configuration owner |
| Viability | Funding, customer concentration, category maturity | Assessed | Public filings, references | Category immature | Vendor relationship owner |
| Exit | Data return format, deletion certification, transition assistance | Defined | Contract exit clause | Untested | Resilience owner |

```
SUBSTITUTABILITY POSITION, set by tier and not by preference
 L0 Locked        provider-specific features load-bearing,
                  prompts and evals tuned to one model  -> rebuild
 L1 Portable with rework   abstraction exists, prompts and
                  evals model-specific                  -> months
 L2 Substitutable abstraction plus a maintained evaluation
                  suite that runs against any candidate  -> weeks
 L3 Dual-run      second provider configured and exercised
                  with live traffic                      -> days

 Current level: __   Target for this tier: __   Gap plan: ______
 The evaluation suite is the thing that makes substitution
 possible. Exit planning that does not fund evaluation is a
 document rather than a capability.

CONFIGURATION CONFORMANCE, the assertion nobody owns
 Contracted term      Production setting     Verified   Date
 zero retention       retention = 0          [ ]        ____
 no training use      flag = off             [ ]        ____
 region pinned        region = ____          [ ]        ____
 Named owner of this verification: __________
```

**Legal determinations about which regime applies, which clauses are required and whether a given arrangement is permitted belong to counsel.** This artifact records what was agreed and whether the running configuration matches it.

**Final Liability rests with the Human.**
