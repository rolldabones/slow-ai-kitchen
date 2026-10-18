---
id: F17
title: "Incident record and post-incident review for an AI system"
owner: "Incident commander, pre-named per tier."
trigger: "At declaration; the review within a fixed period of closure."
signatory: "Incident commander; business owner for the harm assessment; governance, risk management and compliance owner for the notification decision record."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F17. Incident record and post-incident review for an AI system

**Purpose.** Record an incident whose signature may be a fluent correct-looking output rather than an error, and produce learning that compounds.
**Owner.** Incident commander, pre-named per tier.
**Produced.** At declaration; the review within a fixed period of closure.
**Signed by.** Incident commander; business owner for the harm assessment; governance, risk management and compliance owner for the notification decision record.

```
INCIDENT RECORD
 ID / system / tier / declared by / declared at
 Awareness timestamp   [when the organization first knew.
                        Recorded separately from declaration
                        because clocks frequently start here]
 Severity  1 harm occurred or is occurring
           2 systematic wrong output in a consequential
             process, no confirmed harm yet
           3 degraded quality or availability, contained
           4 isolated defect, no pattern
 Harm type  financial | legal | discriminatory | confidentiality
            | safety | regulatory obligation missed | none yet
            [severity 1 includes harms with no technical
             signature and every dashboard green]

 DETECTION
 Detected by   sampling | user complaint | outcome tracing |
               alert | third party
 Detection latency   first bad output to detection: __
 What would have detected it sooner: __________

 BLAST RADIUS
 Defined by time window, not by system, because a prompt or
 model change affects every subsequent interaction
 Window: from ______ to ______
 Outputs in window: ____  Acted upon: ____  Enumerable: Y/N
 Affected individuals or tenants: ____

 CONTAINMENT, narrowest option that contains the harm
 [ ] disable one tool          [ ] roll back the prompt
 [ ] tighten a guardrail       [ ] roll back model or version
 [ ] route affected traffic to a human
 [ ] kill switch
 Chosen: ______  Executed at: ______  Required a deploy: Y/N

 PRESERVATION
 Logs, retrieved sets, prompt versions, model identifier and
 reviewer records preserved before any cleanup. The instinct
 to disable and tidy destroys the only evidence of what
 happened

 COMMUNICATION, three audiences on three clocks
 Affected users: what to distrust and what to do instead,
   issued at ______, before cause was known
 Business owner: exposure and expected restoration, ______
 Governance, risk management and compliance: facts as facts,
   no speculation about cause, ______

 NOTIFICATION DECISION
 Escalated to legal and the governance, risk management and
 compliance function at ______
 Whether an incident is notifiable, to whom and within what
 period is a determination for counsel. It is not made in
 the incident channel. Record the referral, the decision and
 who made it

POST-INCIDENT REVIEW, blameless and timeboxed
 Four artifacts and no others
 1 Timeline, with the awareness timestamp on it
 2 Root cause reaching past the proximate trigger
 3 Actions with named owners and dates
 4 At least one new evaluation case, added permanently
 Two questions that are usually missing
   How long was this running before anyone noticed
   What would have detected it sooner
 Detection latency predicts the severity of the next one
```

**Final Liability rests with the Human.**
