# Lean AI: File Audit and Validation Report

**Slow AI Kitchen · evidence for [Lean AI](../lean-ai.md) v0.1.0 · captured and rerun 15 November 2026 (KST) · a dated record: it is not re-dated when the account changes**

## Conclusion

The Lean AI module is built as an integration of existing Kitchen instruments with explicit constrained-supply scenarios. The public corpus supports the method's foundations. It does not establish that the proposed module produces enterprise savings.

Completed: an exhaustive current-file inventory and defined structural scan across all 22 public repositories; targeted substantive review of the material governing the module; retrospective cross-checking of 136 recorded model outputs; 20 arithmetic and historical-consistency checks; and five existing repository checks executed offline.

Not completed: a line-by-line semantic, legal or security audit of every sentence and program; live execution of every existing test suite; a new model comparison; a prospective Client workflow pilot; or human acceptance of the new module. “Exhaustive” applies to coverage of the enumerated files by the disclosed structural checks, not to those unperformed tasks. The broader objective, empirical validation of the module, therefore remains open.

## 1. Scope and reproducibility

The public repository listing contained 22 repositories. Recursive inventories reported no truncation. All 1,658 listed blobs were downloaded, totaling 27,017,305 bytes. Each file's computed Git blob SHA-1 matched the inventory entry. All files decoded as UTF-8.

The captured inventory is [evidence/snapshot.json](evidence/snapshot.json): for each repository, the identifier the API returned for `main` and the blob identifier of every file. On 15 November 2026 (KST) those identifiers were compared with the working clones: 21 of 22 equal the clone's HEAD commit, each equal to its `origin/main` as last fetched. The exception is `the-ai-generalist`, captured at `7485f55` and released at v2.1.0 (`1f94223`) later the same day; this report describes it at the earlier commit. This is a snapshot, not a claim that live branches remain unchanged.

The downloaded bytes are not republished here, because they are the account's own repositories. To rerun, place each repository at its captured commit under one directory, name that directory in `LEAN_AI_SOURCES` and run the scripts in [tools/](tools/). [README.md](README.md) gives the commands. The rerun of 15 November 2026 reproduced every derived file under `evidence/`.

Scope excludes private repositories, other branches, commit history, issue threads, external linked documents and deployed web applications. The contents of published historical transcripts and fixtures were scanned, but their claims were not promoted into present authority.

| Repository | Files |
|---|---:|
| AI-Governance-Academy | 681 |
| GRCnext-Copilot | 242 |
| slow-ai-kitchen | 141 |
| RedCap-00 | 93 |
| master-prompt-for-in-house-legal-and-compliance | 69 |
| final-liability-rests-with-the-human-book-wip | 50 |
| final-liability-rests-with-the-human-ko-wip | 48 |
| grc | 48 |
| AI-GRC-Copilot | 35 |
| AI-Impact-Assessment-Tool | 35 |
| definition-of-done | 35 |
| origami-method | 31 |
| RedCap-01 | 27 |
| Contract-Mechanism-Review-Assistant | 26 |
| ai-governance-for-boards | 19 |
| the-ungoverned-channel | 19 |
| risk-informed-decision-making-prompt | 18 |
| computational-drafting | 16 |
| rolldabones | 9 |
| the-ai-generalist | 8 |
| AI-GRC-Master-List-of-Questions | 4 |
| grc-workbook | 4 |
| **Total** | **1,658** |

## 2. Checks performed on every applicable file

| Check | Result | Limitation |
|---|---|---|
| Inventory coverage and Git blob hashes | 1,658 of 1,658 match | Integrity, not substantive correctness |
| UTF-8 decoding | 1,658 pass | Does not assess translation quality |
| JSON syntax | 300 parse | Does not validate every schema or domain rule |
| Python syntax | 26 parse | Syntax coverage only; selected offline checks below; no security certification |
| Explicit inline Markdown file links | 5,092 occurrences checked; 82 missing-target candidates | No fragment-anchor, reference-style, redirect or external-site validation |
| Missing-target triage | 4 current-reference occurrences; 5 history; 73 historical evidence | Historical links are not automatically current defects. Repository names in GitHub addresses are matched without regard to case, as GitHub matches them; a case-sensitive match reports a fifth, false, candidate |
| Exact whole-file duplication | One 19-byte duplicated .gitignore | Does not measure conceptual or generated-content duplication |
| Topical scan | Every file scanned for economics, measurement, eligibility, portability and acceptance | Discovery aids, not semantic judgments |
| JSON token records discovered | 329 | Record count is not an independent trial count |

The file-level CSV records coverage and the topic-match counts. Link findings include source path, target, category and existence result. No repository code was executed merely because it appeared in the downloaded corpus.

## 3. Substantive findings affecting Lean AI

### A01. Measurement instruments already exist

W15 establishes pre-agreed thresholds, comparable cases, all-person effort, elapsed time and separate implementation and recurring costs. W16 records the raw case observations. W17 interprets net value and distinguishes released capacity from cash savings. The module uses these records rather than replacing them.

Sources: `slow-ai-kitchen/workbook/30-w15-measurement-protocol.md`, `31-w16-case-observation-record.md`, `32-w17-results-and-business-value.md`, with `consultant-workbook.md` as source of record.

### A02. F24 arithmetic passes, but provenance is insufficient for an empirical claim

The three displayed totals reconcile to 12.97, 23.24 and 14.43 using attempt cost multiplied by attempts, plus human minutes multiplied by loaded rate. However, the “Actual month 1” and “Actual month 3” labels do not carry a case-level observation source or a provenance label in F24. Those numbers cannot be used here as independently verified operational observations.

**Disposition, slow-ai-kitchen v3.5.0.** The artifact set's own index says that a worked example row is supplied where an artifact is tabular, and F24's peak-volume row continues F1's worked scenario. F24 now carries a note saying that its Modeled and Actual columns are those worked figures, not observations from a deployment.

### A03. “Fully loaded” needs a boundary

F24's displayed formula covers model/tool attempt costs and human minutes. It has no separate line for support, recurring evaluation, maintenance or allocated implementation cost. Such amounts may be included in a rate, but the file does not demonstrate that allocation. W15 and W17 already provide the broader accounting discipline.

The module separates case-processing, full recurring and pilot/transition costs and requires an allocation record. It preserves F24's correct arithmetic while limiting the claim attached to it.

**Disposition, slow-ai-kitchen v3.5.0.** The same F24 note states the arithmetic, names the boundary as case processing and says what must be shown before the word "fully" is relied on in a business case. F24's table and figures are unchanged.

### A04. Four current links need path repair

Three occurrences are in `AI-Governance-Academy/slow-ai-for-the-chief-legal-officer.md`. One is in `AI-Governance-Academy/the-compression-and-the-harness.md`. They point to superseded split-file names.

| Superseded filename | Current filename |
|---|---|
| `02-part-2-solution-architecture-to-2-8-entry-points-and.md` | `02-part-2-solution-architecture-to-output-contract.md` |
| `03-2-9-the-ai-architecture-decision-record-to-solution.md` | `03-2-8-entry-points-and-delivery-routes-to-solution.md` |

The three target headings, “The eval gate on a model swap,” “Model deprecation as a standing architectural risk” and “Rollback when the artifact is a prompt and a model version,” exist in the current files. The other 78 candidates are retained for historical-context triage rather than bulk replacement.

**Disposition, AI-Governance-Academy v1.21.1.** The four paths are repaired. The slow-ai-kitchen v3.3.8 changelog entry, which renamed the two part files, said that no other repository linked to the old names; these four links did.

### A05. Generated reading views are not separate evidence

The Kitchen has 22 Markdown files with generated navigation in `primer/` and 49 in `workbook/`, totaling 1,656,086 bytes including navigation and indexes. Their canonical source files also exist. These views are useful to readers and are not exact whole-file duplicates, but naive ingestion can count the same underlying content more than once.

The module directs implementers to select the canonical source or the reading view for a given section and preserve source identity. This is a potential retrieval-design improvement, not a measured token saving.

### A06. Historical acceptance is configuration-specific

The account acceptance rule attaches to the instrument text and model configuration. The GRCnext R2 record accepts one configuration with a residual and rejects the other. A provider switch or cheaper route does not inherit acceptance. The proposed module preserves separate instrument acceptance and business-workflow release decisions.

### A07. Published examples are not field validation

The workbook's 20-case worked example explicitly calls its measurements fictional. Its 900 versus 600 minutes and 16 hours of setup reproduce a five-hour case saving and an eleven-hour initial deficit before unmeasured oversight and fees. The arithmetic is useful; treating it as observed savings would be false.

### A08. No general open-model prohibition is established

The policy sources cited in the module distinguish explicit support for open models from specific supplier restrictions. The module is robust to its motivating forecast being wrong. Eligibility and price scenarios are kept separate. No current provider price or universal private-enterprise approval obligation is asserted.

## 4. Retrospective empirical work

Six run manifests from the GRCnext and in-house legal repositories contain 136 generator records. All recorded input/output token values match the corresponding published transcript headers. Two records in the earlier GRCnext Sonnet R1 run are flagged truncated; they remain in the evidence. No truncation appears in the R2 pair.

| Published run | Configuration identifier | Cases | Input tokens | Output tokens | Truncated |
|---|---|---:|---:|---:|---:|
| GRCnext R1, 27 October 2026 | claude-opus-5-5 | 26 | 238,107 | 105,268 | 0 |
| GRCnext R1, 27 October 2026 | claude-sonnet-5-5 | 26 | 238,107 | 110,127 | 2 |
| GRCnext R2, 27 October 2026 | claude-opus-5-5 | 26 | 242,629 | 110,892 | 0 |
| GRCnext R2, 27 October 2026 | claude-sonnet-5-5 | 26 | 242,629 | 127,107 | 0 |
| Legal T5, 18 October 2026 | claude-opus-5-5 | 16 | 119,247 | 48,175 | 0 |
| Legal T5, 18 October 2026 | claude-sonnet-5-5 | 16 | 119,247 | 41,286 | 0 |

R2 uses the same recorded prompt hash and case IDs, with equal input tokens per paired case. Sonnet's recorded output-token total is 14.622% higher than Opus's in that run. This is not a dollar-cost comparison: unit prices, cache billing, scorer charges and human effort are not included. The opposite output-token direction in the legal pair further cautions against a general model ranking.

Recalculation of the reviewed R2 case table gives:

| Configuration | Critical cases | Other cases | Recorded acceptance |
|---|---:|---:|---|
| Opus | 12/12 | 13/14 | Accepted with residual SC2 |
| Sonnet | 11/12 | 11/14 | Not accepted |

This reproduces the published result, not an independent assessment of every output. The source records a later A6 judgment-call review and Michael's decision to retain the Opus PASS with a qualification. The module preserves that limitation. No new human concurrence is inferred from it.

The remaining 193 discovered JSON token records are Academy generation logs embedded with scores, including superseded attempts and repeated samples. They are retained in the discovery CSV but not pooled with the 136 records as independent evidence of an economic effect. Different prompts, cases and scoring histories would confound that interpretation.

**Empirical conclusion:** recorded resource consumption and acceptance differ by configuration. Enterprise savings caused by Lean AI are **not established**. No fresh model calls were made. This analysis cannot establish present model availability or present pricing from historical identifiers.

## 5. Local validation and its limits

Twenty reproducible checks pass: fifteen worked examples of the accounting and decision rules and five historical-consistency checks. The fifteenth recomputes the illustration in section 4 of the module. Each of the fifteen runs a small function (unit cost, spend, the release recommendation or the configuration comparison) on stated inputs; none is a constant expression. The examples cover failed-work cost, zero acceptance, missing inputs, setup versus recurring cost, reviewer burden, component-only repricing, volume rebound, mandatory-gate priority and published arithmetic. The empirical checks reconcile headers, paired cases, input tokens, prompt identity and recorded acceptance arithmetic.

These checks are deliberately narrow. Some are mathematical invariants, not tests of a deployed system. They do not demonstrate model behavior, host budget enforcement, cache isolation, routing quality or real provider substitution. The prospective protocol names those unperformed behavioral tests explicitly.

### Existing repository checks

Five additional offline checks exited successfully. The preserved logs and `repository-checks.json` record their output.

| Check | Observed result | Limit |
|---|---|---|
| GRCnext fixtures | 41 checked, zero mismatches or missing fixtures | Schema/fixture validation, not model behavior |
| Definition of Done release | Available checks passed, including 165 internal links | Changed-since-release check not performed without Git history |
| Origami release | Available checks passed, including 92 internal links and three worked-example packets | Historical substance comparison not performed without Git history |
| Kitchen canonical figure appendix | Up to date, 256 figures | Agreement with captured figure registry, not independent verification of each figure |
| Kitchen split figure appendix | Up to date, 256 figures | Same registry limitation |

`tools/repository_checks.py` reruns these selected checks against the captured files without model calls. The fixture check requires the `jsonschema` Python package. Successful process exit does not turn a reported “NOT CHECKED” into a pass.

The same five checks were run on 15 November 2026 (KST) in the working clones, where the Git history is present. All five passed, and the Definition of Done and Origami checks then made the comparison with the last release that they report as NOT CHECKED on the captured files: no companion changed. These checks add structural evidence; they do not close the prospective validation gap.

## 6. What is here and what remains

- [../lean-ai.md](../lean-ai.md): the module, with direct source links and evidence limits.
- [pilot-protocol.md](pilot-protocol.md): an executable plan once an owner, a workflow, data and execution access are supplied.
- `evidence/`: the per-file audit, link results, the captured inventory, token records and validation results.
- `tools/`: `audit.py`, `validate.py` and `repository_checks.py`, the offline rerun scripts.

The module is a work in progress, not an accepted prompt instrument. The next substantive decision is the selection of one authorized workflow and its pilot thresholds. A fresh empirical savings claim requires representative cases, measured baseline and intervention effort, billing evidence, a bounded execution budget and human review.

**Definition of done for this record:** module issued as a work in progress; every captured public file covered by the disclosed structural checks; retrospective consistency work completed and rerun; the four link repairs and the two F24 dispositions made. A substantive audit of every file and prospective empirical validation remain open.

**Final Liability rests with the Human.**
