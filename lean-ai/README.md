# Lean AI: Protocol and Evidence

**Slow AI Kitchen · companion folder to [Lean AI](../lean-ai.md) v0.1.0 · 2026-11-15 (KST) · WIP (work in progress)**

The module is [../lean-ai.md](../lean-ai.md). This folder holds what stands behind it: the plan for the pilot that has not been run and the record of the checks that have.

| File | What it holds | Read it when |
|---|---|---|
| [pilot-protocol.md](pilot-protocol.md) | A ready-to-complete extension of W15 to W17: charter, three candidate workflow families, data model, execution steps and ten adversarial cases | You have one authorized workflow and want to test whether a Lean change saves anything |
| [audit-and-validation-report.md](audit-and-validation-report.md) | What was checked on 15 November 2026 (KST), what was found and what was not done | You want to know what the module's evidence does and does not establish |
| [evidence/](evidence/) | The derived records: the captured inventory of 1,658 files in 22 repositories, the per-file and per-link results, the token records of six published runs and the results of the twenty checks | You want to check a figure in the module or the report |
| [tools/](tools/) | `audit.py`, `validate.py` and `repository_checks.py` | You want to rerun the checks |

## What the evidence is

A dated record. It describes the account's public repositories as captured on 15 November 2026 (KST), each at the commit named in [evidence/snapshot.json](evidence/snapshot.json). It is not regenerated when a repository changes, and the module's section 9 cites it as of that date.

It establishes that the Kitchen's measurement instruments exist and reconcile, that the published run records are internally consistent and that the worked examples compute. It does not establish that Lean AI saves an enterprise anything. That needs the pilot.

## Rerunning the checks

The scripts need Python 3 and its standard library. They make no network request and no model call. `repository_checks.py` also needs the `jsonschema` package, for the GRCnext fixture check.

The captured files are not republished here, because they are the account's own repositories. Place each of the 22 repositories at the commit named in `evidence/snapshot.json` under one directory, each in a folder of its own name, and run:

```
LEAN_AI_SOURCES=/path/to/that/directory python3 lean-ai/tools/audit.py
LEAN_AI_SOURCES=/path/to/that/directory python3 lean-ai/tools/validate.py
LEAN_AI_SOURCES=/path/to/that/directory python3 lean-ai/tools/repository_checks.py
```

Each script rewrites its derived files under `evidence/`. Against the captured commits the files come back byte for byte, except that `repository-checks.json` and the five logs carry the release-check output of the day. Against later commits the hash and link results differ, which is the scan reporting the change.

## Limits

The structural scan covers every captured file for the checks it names: integrity, decoding, JSON and Python syntax and explicit inline Markdown links. It does not check fragment anchors, reference-style links or external sites, and it is not a review of substance. The account's own guards and its weekly sweep remain the maintenance controls; this scan does not replace them.

Model identifiers in the historical records name what those runs used. They say nothing about what is available or what it costs today.

**Final Liability rests with the Human.**
