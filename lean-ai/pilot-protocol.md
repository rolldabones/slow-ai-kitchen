# Lean AI: Prospective Pilot Protocol

**Slow AI Kitchen · companion to [Lean AI](../lean-ai.md) · v0.1.0 · 2026-11-15 (KST) · WIP, not yet run**

This is a ready-to-complete extension of Kitchen W15 to W17, not a record of a pilot already run. No Client facts, thresholds, observations or approval have been filled in by inference. A field marked Unknown is a field the Client's named owner must complete.

## 1. Charter before data collection

| Field | Entry required |
|---|---|
| Service, business outcome and recipient | Unknown |
| Business owner, reviewer and approver | Unknown |
| Risk tier, jurisdictions and applicable obligations | Unknown |
| Definition of done and version | Unknown |
| Mandatory quality and control requirements | Unknown |
| Non-critical quality margin and minimum worthwhile cost improvement | Unknown |
| Baseline process, case mix and cost boundary | Unknown |
| Proposed intervention and reason it should help | Unknown |
| Eligible configurations, data authorization and budget | Unknown |
| Held-out cases and development cases | Unknown |
| Sample-size justification and uncertainty method | Unknown |
| Operator assignment, order balancing and reviewer blinding | Unknown |
| Stop, fallback, rollback and incident routes | Unknown |
| Review date and authorized decision-maker | Unknown |

Unknown mandatory fields prevent a release recommendation. Public or synthetic material can be used for a feasibility exercise, labeled as such, but does not establish Client savings.

## 2. Three proposed workflow families

| Family | Baseline | Candidate Lean intervention | Required evaluation |
|---|---|---|---|
| Document extraction | Current extraction and manual verification | Deterministic field validation and bounded extraction | Exact fields, missing-value handling, unsupported values, exceptions and reviewer effort |
| Evidence-backed drafting | Current professional drafting process | Reusable approved structure and narrower evidence pack | Claim support, omissions, factual invention, source fidelity, reviewer effort and release decision |
| Bounded tool workflow | Current authorized action sequence | Fewer tool calls with explicit state and retry controls | Permission, amount, recipient and state boundaries; duplicate action, uncertain outcome, stop and recovery |

Select one first. A portfolio-wide rollout is not needed to learn whether the method works. These are proposed trials, not three completed demonstrations.

## 3. Data model

Use one case record, one or more attempt records and separately allocated overhead. Do not copy case cost into every attempt row.

### Case fields

`case_id`, `pair_id`, `workflow_id`, `method`, `difficulty_stratum`, `operator`, `reviewer`, `input_hash`, `configuration_id`, `dod_version`, `start_timestamp`, `release_timestamp`, `preparation_minutes`, `production_minutes`, `review_minutes`, `correction_and_fallback_minutes`, `approval_minutes`, `first_pass_accepted`, `final_disposition`, `defect_severity`, `mandatory_gate_pass`, `release_evidence`, `measurement_status`.

Allowed final dispositions: accepted, refused, abandoned, unresolved. A control test may pass because a request was refused; record that in the control-test result, not as a fictional completed service outcome. The comparison specification defines whether a particular triage disposition is the service's intended accepted outcome before the run.

### Attempt fields

`attempt_id`, `case_id`, `parent_attempt_id`, `configuration_id`, `model_returned`, `prompt_hash`, `corpus_version`, `tool_versions`, `input_tokens`, `cache_write_tokens`, `cache_read_tokens`, `output_tokens`, `billable_other_units`, `model_charge`, `tool_charge`, `compute_charge`, `currency`, `billing_evidence`, `stop_reason`, `attempt_disposition`, `error_or_retry_reason`.

Token categories must match the provider's actual billing definitions. Do not assume reported input tokens include or exclude caching in the same way across providers. Retain both raw usage and the invoiced or contract-priced amount. Use null for missing data, not zero.

### Period costs and configuration fields

Record allocated support, monitoring, recurring evaluation and maintenance, with allocation basis and evidence. Record setup, training, initial evaluation and migration separately. A configuration includes model/version, prompt, tools, corpus, routing and relevant host controls. Preserve the actual run parameters, not merely a marketing model name.

## 4. Execution and comparison

1. Approve the charter and freeze the baseline and intervention definitions.
2. Check eligibility and data authorization. Establish the metering and limits before running.
3. Run development cases to establish feasibility. Exclude them from the held-out comparison and state the exclusion in advance.
4. Run comparable baseline and intervention cases with balanced assignment. Record every attempt and failed or abandoned case. Keep tool errors and refunds visible.
5. Score outputs against the same criteria. Record human concurrence and disputed judgments. Do not substitute a model's self-report for acceptance.
6. Reconcile usage with billing and case IDs. Investigate unmatched or missing records.
7. Calculate pooled cost per accepted outcome and paired differences with uncertainty. Preserve difficult-case and refusal results separately. Report total expenditure as well as unit cost.
8. Conduct the authorized stop and fallback exercise. For an external action, reconcile its actual state before any retry.
9. Decide retain, revise, defer or retire. A candidate failing a mandatory requirement cannot win on its cost result.
10. Recheck actuals at the existing operational review and record drift, volume growth and reviewer workload.

## 5. Adversarial cases to include

| Case | Expected behavior | Evidence |
|---|---|---|
| Missing reviewer time | Full cost remains incomplete | Calculation record names missing input |
| No accepted outcomes | Undefined unit cost; cost incurred disclosed | Denominator and disposition counts |
| Cheap configuration fails a mandatory case | Candidate rejected for release | Failure retained alongside cost |
| Price rises while volume changes | Separate price, volume, mix and quality effects | Repriced component ledger |
| Cache contains stale or unauthorized content | No silent reuse | Freshness and permission control result |
| Router sends difficult case to weak path | Detection and authorized escalation | Route, outcome and reviewer record |
| Concurrent calls approach limit | Enforcement accounts for in-flight work | Host test and charge reconciliation |
| Tool times out after action | Outcome treated as uncertain until checked | State check and idempotency record |
| Provider eligibility is withdrawn | Authorized eligible fallback or safe pause | Actual recovery exercise |
| Context is shortened | Material facts and constraints still retained | Held-out omission and provenance tests |

These are prospective behavioral tests. The module's local arithmetic checks do not establish that any deployed system passes them.

## 6. Evidence required to close the present gap

One authorized workflow, its baseline and representative cases; access to the chosen execution environment; a bounded test budget; attributable billing or contract rates; measured human effort; pre-agreed acceptance and economic thresholds; and a named reviewer able to concur. Client information should be de-identified where appropriate and processed only in its authorized environment.

None of these was available when this protocol was drafted: no Client observation set, no human timing record and no billing evidence. That prevents a prospective enterprise validation claim. It did not prevent drafting, the public-file audit or the retrospective reanalysis recorded in the [audit and validation report](audit-and-validation-report.md).

**Final Liability rests with the Human.**
