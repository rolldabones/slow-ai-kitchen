"""Read-only structural scan of every file in the captured public trees.
Does not establish substantive correctness, current law or instrument acceptance.
Reads evidence/snapshot.json (the captured inventory) and the corpus directory
named in LEAN_AI_SOURCES. Standard library only; no network, no model calls.
"""
from pathlib import Path
import ast, csv, hashlib, json, os, re, collections, urllib.parse

ROOT = Path(__file__).resolve().parent.parent
# The captured corpus is not published here: it is the account's own 22 public
# repositories. To rerun, place each repository at the commit named in
# evidence/snapshot.json under one directory and name it in LEAN_AI_SOURCES.
SRC = Path(os.environ.get('LEAN_AI_SOURCES', ROOT / 'sources'))
OUT = ROOT / 'evidence'
inventory = json.loads((OUT/'snapshot.json').read_text())
manifest = [{'repo':r['name'],'path':t['path'],'sha':t['sha']} for r in inventory for t in r['tree'] if t['type']=='blob']
# GitHub resolves owner and repository names without regard to case; so does this scan.
REPOS = {r['name'].lower(): r['name'] for r in inventory}
rows, links, issues, telemetry = [], [], [], []
duplicates = collections.defaultdict(list)
topics = {
    'economics': r'cost per|unit economics|fully loaded|net benefit|budget',
    'measurement': r'first.pass|human effort|review.*minutes|measurement protocol|sample size',
    'eligibility': r'approved provider|open.weight|open.source|supplier|provenance',
    'portability': r'provider.exit|custody|substitut|lock.in|fallback',
    'acceptance': r'critical case|not accepted|accepted with residuals|mandatory gate',
}
texts = {}
def classify(p):
    if re.search(r'(^|/)(evidence|transcripts[^/]*|runs|scores)(/|$)',p): return 'historical_evidence'
    if re.search(r'CHANGELOG|HISTORY|RETIREMENT',p): return 'history'
    if re.search(r'(^|/)(tests?|fixtures)(/|$)',p): return 'test_asset'
    if re.search(r'(^|/)(primer|workbook)/',p): return 'split_or_workbook'
    return 'current_reference_or_tool'

for m in sorted(manifest, key=lambda x:(x['repo'],x['path'])):
    rel=m['repo']+'/'+m['path']; p=SRC/rel; b=p.read_bytes()
    sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    try: text=b.decode('utf-8'); utf=True
    except UnicodeDecodeError: text=b.decode('utf-8',errors='replace'); utf=False
    texts[rel]=text
    duplicates[hashlib.sha256(b).hexdigest()].append(rel)
    row={'repository':m['repo'],'path':m['path'],'category':classify(m['path']),
         'bytes':len(b),'git_blob_sha1':sha,'hash_verified':sha==m['sha'],
         'utf8':utf,'lines':len(text.splitlines()),'json_parse':'not_applicable','python_parse':'not_applicable'}
    for k,pattern in topics.items(): row[k]=len(re.findall(pattern,text,re.I))
    if p.suffix=='.json':
        try:
            data=json.loads(text); row['json_parse']='pass'
            def walk(obj, pointer=''):
                if isinstance(obj,dict):
                    if 'input_tokens' in obj and 'output_tokens' in obj:
                        telemetry.append({'source':rel,'pointer':pointer,**{k:obj.get(k) for k in ['test_id','model_returned','input_tokens','output_tokens','stop_reason','truncated']}})
                    for k,v in obj.items(): walk(v,pointer+'/'+str(k))
                elif isinstance(obj,list):
                    for i,v in enumerate(obj): walk(v,pointer+'/'+str(i))
            walk(data)
        except Exception as e: row['json_parse']='fail'; issues.append({'kind':'json_parse','source':rel,'detail':str(e)})
    if p.suffix=='.py':
        try: ast.parse(text); row['python_parse']='pass'
        except Exception as e: row['python_parse']='fail'; issues.append({'kind':'python_parse','source':rel,'detail':str(e)})
    rows.append(row)
    if p.suffix!='.md': continue
    # Explicit inline Markdown links only, after fenced code removal. Fragments,
    # reference-style links and external websites are not validated by this check.
    scrub=re.sub(r'```.*?```','',text,flags=re.S)
    for match in re.finditer(r'\[[^\]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)',scrub):
        target=match.group(1).strip('<>'); parsed=urllib.parse.urlsplit(target)
        if not target or target.startswith('#') or parsed.scheme in ('mailto','tel'): continue
        local=None; scope='relative'
        if parsed.scheme or target.startswith('//'):
            if parsed.netloc=='github.com':
                bits=parsed.path.strip('/').split('/')
                if len(bits)>=2 and bits[0]=='rolldabones':
                    bits[1]=REPOS.get(bits[1].lower(),bits[1])
                    if len(bits)==2: local=SRC/bits[1]
                    elif len(bits)>=5 and bits[2] in ('blob','tree') and bits[3]=='main': local=SRC/bits[1]/urllib.parse.unquote('/'.join(bits[4:]))
                    scope='github_current_tree'
            if local is None: continue
        else:
            local=(SRC/m['repo']/urllib.parse.unquote(parsed.path.lstrip('/'))) if target.startswith('/') else p.parent/urllib.parse.unquote(parsed.path)
        exists=local.exists()
        links.append({'source':rel,'category':row['category'],'target':target,'scope':scope,'exists':exists})

def write_csv(name, data):
    if not data: return
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
write_csv('file-audit.csv',rows)
write_csv('link-audit.csv',links)
write_csv('token-telemetry.csv',telemetry)
dup=[{'sha256':k,'paths':v,'bytes_each':(SRC/v[0]).stat().st_size} for k,v in duplicates.items() if len(v)>1]
(OUT/'duplicate-groups.json').write_text(json.dumps(dup,indent=2))
(OUT/'parse-findings.json').write_text(json.dumps(issues,indent=2))
summary={'files':len(rows),'repositories':len(set(r['repository'] for r in rows)),
 'bytes':sum(r['bytes'] for r in rows),'hash_failures':sum(not r['hash_verified'] for r in rows),
 'utf8_failures':sum(not r['utf8'] for r in rows),'json_files':sum(r['json_parse']!='not_applicable' for r in rows),
 'python_files':sum(r['python_parse']!='not_applicable' for r in rows),'parse_failures':len(issues),
 'links_checked':len(links),'missing_link_candidates':sum(not l['exists'] for l in links),
 'missing_by_category':dict(collections.Counter(l['category'] for l in links if not l['exists'])),
 'duplicate_groups':len(dup),'duplicate_bytes_beyond_one_copy':sum(d['bytes_each']*(len(d['paths'])-1) for d in dup),
 'json_token_records':len(telemetry),'by_repository':dict(collections.Counter(r['repository'] for r in rows))}
(OUT/'audit-summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
print('Missing current-reference candidates:')
for l in links:
    if not l['exists'] and l['category']=='current_reference_or_tool': print(json.dumps(l))
