# Lean AI: Plan, Book, Tiny Servants and Evidence

**Slow AI Kitchen · the working folder of [Lean AI](../lean-ai.md) · v0.2.0 · 2026-11-25 (KST) · WIP (work in progress)**

The module is [../lean-ai.md](../lean-ai.md). This folder holds what stands behind it and what is being built from it: the plan, a book in progress, sample workflows called Lean Tiny Servants, the plan for the pilot that has not been run and the record of the checks that have. All of it is a work in progress. The report, its evidence and its three tools were issued with the module's v0.1.0 on 15 November 2026 (KST) and are unchanged; the report keeps v0.1.0 as the dated record of that day. At v0.2.0, 25 November 2026 (KST), the module and the pilot protocol gain the owner's hours, and `tools/oversight.py` recomputes the module's invented figures for them.

| File | What it holds | Read it when |
|---|---|---|
| [PLAN.md](PLAN.md) | What is being built, in what order and under what rules, with the log of what has shipped | You want to know where the work stands and what comes next |
| [book/](book/README.md) | *Slow AI, Lean AI: The Owner's Acceptance and the Power to Stop*, a book in progress: its thesis, its contents and, as they are written, its chapters | You want the argument at length |
| [tiny-servants/](tiny-servants/README.md) | The Lean Tiny Servants: what one is, the card each carries, the two stages each passes and, as they are built, the servants and their test records | You want a small workflow that you can read, run and check |
| [pilot-protocol.md](pilot-protocol.md) | A ready-to-complete extension of W15 to W17: charter, three candidate workflow families, data model, the record of an owner's hours, execution steps and eleven adversarial cases | You have one authorized workflow and want to test whether a Lean change saves anything |
| [audit-and-validation-report.md](audit-and-validation-report.md) | What was checked on 15 November 2026 (KST), what was found and what was not done | You want to know what the module's evidence does and does not establish |
| [evidence/](evidence/) | The derived records: the captured inventory of 1,658 files in 22 repositories, the per-file and per-link results, the token records of six published runs and the results of the twenty checks; from v0.2.0 also the invented figures of the module's owner's hours | You want to check a figure in the module or the report |
| [tools/](tools/) | `audit.py`, `validate.py` and `repository_checks.py`; from v0.2.0, `oversight.py` | You want to rerun the checks |

The theory behind the module is in the working paper [*The Boundary and the Limit: Effectiveness, Lean AI and the Theory of the Governed Firm*](https://github.com/rolldabones/AI-Governance-Academy/blob/main/the-boundary-and-the-limit.md), which stays in AI-Governance-Academy. On the theory, the paper governs.

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

Each script rewrites its derived files under `evidence/`. `oversight.py` needs no captured sources: `python3 lean-ai/tools/oversight.py` recomputes the invented figures of the module's owner's hours, checks each against the module and rewrites `evidence/oversight-illustration.json`. Against the captured commits the files come back byte for byte, except that `repository-checks.json` and the five logs carry the release-check output of the day. Against later commits the hash and link results differ, which is the scan reporting the change.

## Limits

The structural scan covers every captured file for the checks it names: integrity, decoding, JSON and Python syntax and explicit inline Markdown links. It does not check fragment anchors, reference-style links or external sites, and it is not a review of substance. The account's own guards and its weekly sweep remain the maintenance controls; this scan does not replace them.

Model identifiers in the historical records name what those runs used. They say nothing about what is available or what it costs today.

**Final Liability rests with the Human.**
