---
id: F16
title: "Data protection impact assessment structure, as an architecture artifact"
owner: "Privacy owner, drafted with the architect."
trigger: "Before processing begins, and on material change."
signatory: "Privacy owner; the named person accepting residual risk; legal where the assessment reaches a determination."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F16. Data protection impact assessment structure, as an architecture artifact

**Purpose.** Assess privacy risk in a form an architect can act on, producing design changes rather than a narrative.
**Owner.** Privacy owner, drafted with the architect.
**Produced.** Before processing begins, and on material change.
**Signed by.** Privacy owner; the named person accepting residual risk; legal where the assessment reaches a determination.

```
SYSTEM / tier / assessment version / date

1 DESCRIPTION OF THE PROCESSING
  What the system does, in plain language
  Categories of individuals affected and approximate numbers
  Categories of data, per source, with classification (F10)
  Whether any category is special or otherwise heightened
  Recipients, including the model provider and subprocessors
  Retention per artifact, including derived artifacts
  Cross-border movement, with the destination named

2 NECESSITY AND PROPORTIONALITY
  Purpose stated specifically enough to constrain reuse
  Why the same outcome cannot be achieved with less data
  Data minimized how, against the pull of the context window
  Lawful basis, as determined by the privacy function
  Whether this is a new purpose for data collected earlier
  Information provided to individuals, and where

3 RISKS TO INDIVIDUALS  [tabulated below]

4 ARCHITECTURAL CONSEQUENCES, the section that makes this an
  architecture artifact rather than a form
  Each control above maps to a design element with an owner
  and a test. List the design changes this assessment forced:
    - identity-based pre-filtering replaced service-account
      retrieval
    - content logging moved to a segregated store at
      Confidential and above
    - erasure rehearsal added to the readiness gate

5 DATA SUBJECT RIGHTS AS ENGINEERING REQUIREMENTS
  Access        can we produce everything held about a person,
                including chunks, logs and eval set entries
  Rectification can a correction propagate to derived stores
  Erasure       tested end to end, evidenced, within __ days
  Objection     can processing be stopped for one individual
  Explanation   can we reconstruct why the system said what it
                said, from lineage (F12, F13 and the lineage
                chain in G12)

6 RESIDUAL RISK AND SIGN-OFF
  Residual risk statement, in one paragraph
  Accepted by (named person): __________  date: ______
  Review trigger: any re-tier trigger, or __________
```

**Section 3, risks to individuals.** Likelihood and severity are graded low, medium or high.

| Risk to the individual | Cause in this design | Likelihood | Severity | Control | Residual |
| --- | --- | --- | --- | --- | --- |
| A wrong output is relied on | Model error uncaught | M | H | Pre-action human approval, F5 | L |
| Disclosure across users | Entitlement filter applied after ranking | L | H | Pre-filter by end-user identity, F12 | L |
| Excess retention | Logs contain inputs and outputs and are therefore regulated data | H | M | Tiered logging, segregated content store, F10 | L |
| Erasure not effective | Derived artifacts missed | H | H | Derived-artifact map plus a tested delete, F10 | M |
| Inference beyond the stated purpose | Aggregation across sources | M | M | Purpose floor classification, F10 | M |
| Unfair outcome by group | Corpus skew inherited by every answer | M | H | Segmented evaluation, F6 | M |

**The legal determinations in sections 2 and 5, including lawful basis, whether an assessment is required and what rights attach, belong to the privacy function and counsel.** The architect owns sections 3, 4 and the testability of section 5.

**Final Liability rests with the Human.**
