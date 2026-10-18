---
id: F25
title: "Developer tooling and team configuration standard"
owner: "Engineering lead, with security for the managed policy rows and identity management for entitlement."
trigger: "Before the second team onboards, not before the first."
signatory: "Engineering lead; head of application security; identity owner for the entitlement section."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F25. Developer tooling and team configuration standard

**Purpose.** Fix what the engineering organization runs, where each setting lives, who may change it and what evidence exists that the standard is the thing actually deployed. Without it, agentic development tooling spreads as personal configuration and the organization cannot answer what its engineers are permitted to do.
**Owner.** Engineering lead, with security for the managed policy rows and identity management for entitlement.
**Produced.** Before the second team onboards, not before the first.
**Signed by.** Engineering lead; head of application security; identity owner for the entitlement section.

| Setting | Scope it lives in | Value | Changeable by | Why it is at this scope |
| --- | --- | --- | --- | --- |
| Denied command list | Managed policy | `curl` to non-allowlisted hosts, direct production database clients, credential printers | Security only, through device management | An engineer must not be able to lift it in the branch they are working in |
| Permitted model set | Managed policy | Named models only; no third-party endpoints | Security | Route and residency commitment (2.8, 6.8) |
| Mandatory pre-tool hook | Managed policy | Secret-scan and denied-path check, blocking | Security | A mandatory step on an observe-only event is not mandatory |
| Telemetry destination | Managed policy | Central log sink with the correlation identifier | Platform engineering | Diagnosis and audit both depend on it |
| Project conventions file | Project settings, shared | Repo layout, coding standards, test command, review expectations | Engineering team, through code review | Should apply to everyone who clones the repository |
| Project MCP servers | Project settings, shared | Named servers, credentials by reference only | Engineering team, with security approval per server | Credentials in a committed file are an incident |
| Permission mode, interactive | Project settings, shared | Plan mode default on this repository | Engineering team | |
| Permission mode, pipeline | Command line, in the pipeline definition | Auto-deny, allow rules only | Pipeline author, reviewed as code | Run-specific, and must not inherit a developer's settings |
| Personal deviations | Project settings, local (ignored) or user settings | Editor preferences, personal commands | The individual | Never lands in another engineer's session |

```
DISTRIBUTION
 Standard distributed as ................. plugin / marketplace / manual
 Marketplace owner .......................
 Version in force ........................  Superseded version ........
 Withdrawal path tested on ...............  (a component you cannot
                                             withdraw is a component you
                                             cannot correct)

ENTITLEMENT
 Provisioned through .....................  group, from the corporate
                                             directory
 Joiner / mover / leaver handled by ......
 Seats issued ............  Seats active in last 30 days ............
 Cost center receiving the invoice .......

INTEGRATION POINTS IN THE PIPELINE, and the measure for each
 Change review ........ on / off   Finding acceptance rate ..........
 Test generation ...... on / off   Seeded-defect catch rate .........
 Pipeline gating ...... on / off   Flip rate on unchanged input .....
 Docs generation ...... on / off   Task completion without author ...

DELIVERY BASELINE, taken before rollout
                              Baseline      Target      Current
 Lead time for change ......  ........      ......      .......
 Deployment frequency ......  ........      ......      .......
 Change failure rate .......  ........      ......      .......
 Time to restore service ...  ........      ......      .......
 A rise in deployment frequency with a rise in change failure
 rate is work moved downstream, not productivity

GENERATED CODE CONTROLS, all four or the section is incomplete
 Static analysis ............  Dependency scanning ..........
 Secret scanning ............  License provenance ...........

DRIFT CHECK, quarterly
 Sample N engineer machines and compare deployed configuration
 against the standard. Record deviations and whether each was
 an exception, an error or an undocumented improvement worth
 adopting. A standard never checked against reality is a
 document, not a control
```

**Final Liability rests with the Human.**
