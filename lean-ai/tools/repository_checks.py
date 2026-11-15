"""Rerun selected inspected offline repository checks; no model calls."""
from pathlib import Path
import subprocess, sys, os, json
ROOT = Path(__file__).resolve().parent.parent
# The captured corpus is not published here: it is the account's own 22 public
# repositories. To rerun, place each repository at the commit named in
# evidence/snapshot.json under one directory and name it in LEAN_AI_SOURCES.
SRC = Path(os.environ.get('LEAN_AI_SOURCES', ROOT / 'sources'))
OUT = ROOT / 'evidence'
OUT.mkdir(parents=True, exist_ok=True)
k = SRC / 'slow-ai-kitchen'
commands = [
 ('grcnext-fixtures', [SRC/'GRCnext-Copilot/tools/check_fixtures.py']),
 ('definition-of-done-release', [SRC/'definition-of-done/tools/check_release.py']),
 ('origami-release', [SRC/'origami-method/tools/check_release.py']),
 ('kitchen-appendix-canonical', [k/'tools/build_appendix_i.py', '--check', k/'primer/figures.yaml', k/'enterprise-ai-architecture-primer.md']),
 ('kitchen-appendix-split', [k/'tools/build_appendix_i.py', '--check', k/'primer/figures.yaml', k/'primer/18-appendix-i-sources-and-current-figures.md'])
]
results = []
for name, args in commands:
    result = subprocess.run([sys.executable, *map(str,args)], capture_output=True, text=True, timeout=30, env={**os.environ, 'PYTHONDONTWRITEBYTECODE':'1'}, cwd=SRC)
    out, err = (v.replace(str(SRC)+os.sep, '') for v in (result.stdout, result.stderr))
    results.append(dict(check=name, exit_code=result.returncode, stdout=out, stderr=err))
    (OUT/(name+'.log')).write_text(out+err)
    print(name, result.returncode)
(OUT/'repository-checks.json').write_text(json.dumps(results,indent=2)+'\n')
raise SystemExit(any(x['exit_code'] for x in results))
