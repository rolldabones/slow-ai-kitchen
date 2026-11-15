"""Reanalyse published observations and test proposed accounting invariants.
No model calls, vendor prices, production data or invented human timings.
"""
from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
import csv, json, os, re, collections

ROOT = Path(__file__).resolve().parent.parent
# The captured corpus is not published here: it is the account's own 22 public
# repositories. To rerun, place each repository at the commit named in
# evidence/snapshot.json under one directory and name it in LEAN_AI_SOURCES.
SRC = Path(os.environ.get('LEAN_AI_SOURCES', ROOT / 'sources'))
OUT = ROOT / 'evidence'
checks=[]
def check(name, ok, evidence):
    checks.append({'test':name,'pass':bool(ok),'evidence':evidence})

def unit_cost(costs, accepted):
    if accepted < 0 or any(x is not None and D(str(x))<0 for x in costs): raise ValueError('negative')
    if accepted==0 or any(x is None for x in costs): return None
    return sum(D(str(x)) for x in costs)/D(accepted)

check('C01 all attempts retained',unit_cost([100,20,30],5)==D('30'),'150 total including failed-work cost / 5 accepted = 30')
check('C02 zero accepted is undefined',unit_cost([150],0) is None,'No successful denominator, never zero cost')
check('C03 missing cost blocks full result',unit_cost([100,None],5) is None,'Missing is not zero')
try: unit_cost([-1],1); negative=False
except ValueError: negative=True
check('C04 negative cost rejected',negative,'Input validation')
check('C05 one-time cost shown separately',unit_cost([100,40],10)==14 and unit_cost([100,40,300],10)==44,'Recurring 14; pilot including setup 44')
check('C06 human effort can reverse token savings',unit_cost([10,180],10)>unit_cost([20,100],10),'Illustrative 19 vs 12, not an observed enterprise result')
check('C07 price shock applies only to model component',unit_cost([20*3,100],10)==16,'Illustrative model 20 -> 60; human 100 unchanged')
def spend(unit, volume): return D(str(unit))*D(volume)
def recommend(mandatory_gates, new_unit_cost, old_unit_cost):
    """Mandatory gates are evaluated first; cost is compared only if all pass."""
    if not all(mandatory_gates): return False
    return new_unit_cost is not None and old_unit_cost is not None and new_unit_cost < old_unit_cost
def needs_revalidation(accepted_configuration, proposed_configuration):
    return accepted_configuration != proposed_configuration
check('C08 lower unit cost need not lower spend',spend(8,150)>spend(10,100) and unit_cost([spend(8,150)],150)<unit_cost([spend(10,100)],100),'Illustrative: unit cost 8 against 10, volume 150 against 100, spend 1200 against 1000')
check('C09 failed mandatory gate blocks recommendation',recommend([True,False,True],D(8),D(10)) is False and recommend([True,True,True],D(8),D(10)) is True and recommend([True,True,True],None,D(10)) is False,'Gate evaluated before savings; an undefined unit cost never recommends')
check('C10 safe refusal separate from accepted output',unit_cost([100],8)==D('12.5'),'10 attempted, 8 accepted, 2 refused; refusals not denominator')
check('C11 means are not summed ratios',unit_cost([60,40],2+8)==10,'Pooled cost 100 / 10, not mean(60/2,40/8)')
check('C12 changed configuration needs revalidation',needs_revalidation(('model-a','p1'),('model-b','p1')) and not needs_revalidation(('model-a','p1'),('model-a','p1')),'Configuration identity changes with the model even when the prompt does not')

# Existing F24 calculations, verified as arithmetic only. No claim the cells
# labelled Actual month 1 / 3 are observed production measurements.
f24=[]
for label,attempt,tries,mins,rate,printed in [('modeled','0.31','1.2','9','1.4','12.97'),('month1','0.44','1.9','16','1.4','23.24'),('month3','0.33','1.3','10','1.4','14.43')]:
    val=(D(attempt)*D(tries)+D(mins)*D(rate)).quantize(D('.01'),rounding=ROUND_HALF_UP)
    f24.append({'column':label,'computed':str(val),'printed':printed,'match':val==D(printed)})
check('C13 F24 displayed arithmetic',all(x['match'] for x in f24),f24)
check('C14 workbook fictional worked example',900-600==300 and 300/60-16==-11,'5 hours case saving - 16 setup = -11 before other costs; synthetic')

# The worked illustration in lean-ai.md section 4: invented figures, recomputed here.
model, human, recurring, setup, accepted, attempted = D('26.00'), D(300)*D('1.40'), D('120.00'), D('800.00'), 8, 10
case_cost = model+human
two = lambda x: x.quantize(D('.01'), rounding=ROUND_HALF_UP)
illustration = {'case_processing': str(case_cost), 'per_accepted': str(two(unit_cost([model,human],accepted))),
  'full_recurring_per_accepted': str(two(unit_cost([model,human,recurring],accepted))),
  'pilot_per_accepted': str(two(unit_cost([model,human,recurring,setup],accepted))),
  'per_attempted_wrong': str(two(case_cost/D(attempted))),
  'price_x2': str(two(unit_cost([model*2,human],accepted))), 'price_x5': str(two(unit_cost([model*5,human],accepted))),
  'x5_rise_pct': str((unit_cost([model*5,human],accepted)/unit_cost([model,human],accepted)*100-100).quantize(D('.1'), rounding=ROUND_HALF_UP)),
  'understatement_pct': str(((1-(case_cost/D(attempted))/unit_cost([model,human],accepted))*100).quantize(D('.1'), rounding=ROUND_HALF_UP))}
expected = {'case_processing':'446.00','per_accepted':'55.75','full_recurring_per_accepted':'70.75','pilot_per_accepted':'170.75',
  'per_attempted_wrong':'44.60','price_x2':'59.00','price_x5':'68.75','x5_rise_pct':'23.3','understatement_pct':'20.0'}
check('C15 module section 4 illustration reproduces',illustration==expected,illustration)

# Aggregate only manifests with generator telemetry, not arbitrary JSON numbers.
runs=[]; paired=[]; header_fail=[]
for p in sorted(SRC.rglob('*_run.json')):
    data=json.loads(p.read_text())
    if 'transcripts' not in data: continue
    ts=data['transcripts']; verified=0
    for t in ts:
        file=p.parent/t['file']
        txt=file.read_text() if file.exists() else ''
        # Case-sensitive published metadata label variants supported explicitly.
        inp=re.search(r'\*\*Input tokens:\*\*\s*(\d+)',txt)
        out=re.search(r'\*\*Output tokens:\*\*\s*(\d+)',txt)
        ok=bool(inp and out and int(inp[1])==t['input_tokens'] and int(out[1])==t['output_tokens'])
        if ok: verified+=1
        else: header_fail.append(str(file.relative_to(SRC)))
    runs.append({'source':str(p.relative_to(SRC)),'run':data['stamp'],'model':data['model_requested'],
      'cases':len(ts),'input_tokens':sum(t['input_tokens'] for t in ts),
      'output_tokens':sum(t['output_tokens'] for t in ts),'truncated':sum(t.get('truncated',False) for t in ts),
      'headers_verified':verified,'prompt_sha256':data['prompt_proper_sha256']})
    if data['stamp']=='20261027-R2':
        for t in ts: paired.append({'model':data['model_requested'],'case':t.get('case',t.get('test_id')),'input_tokens':t['input_tokens'],'output_tokens':t['output_tokens']})
check('E01 manifest tokens agree with transcript headers',not header_fail,{'records':sum(x['cases'] for x in runs),'unmatched':header_fail})
pairmodels=collections.defaultdict(dict)
for x in paired: pairmodels[x['model']][x['case']]=x
aa=pairmodels['claude-opus-5-5'];bb=pairmodels['claude-sonnet-5-5']
check('E02 R2 paired case sets match',aa.keys()==bb.keys(),{'cases':len(aa)})
check('E03 R2 input tokens match per case',all(aa[k]['input_tokens']==bb[k]['input_tokens'] for k in aa),{'cases':len(aa)})
check('E04 R2 prompt hashes match',len({r['prompt_sha256'] for r in runs if r['run']=='20261027-R2'})==1,'Same recorded prompt hash')
op=sum(x['output_tokens'] for x in aa.values());so=sum(x['output_tokens'] for x in bb.values())
comparison={'opus_output_tokens':op,'sonnet_output_tokens':so,'sonnet_vs_opus_output_pct':round((so/op-1)*100,3),
 'interpretation':'Recorded output-token counts only; not price, cost, latency, human effort or a causal savings estimate.'}

# Recompute latest GRC recorded acceptance arithmetic from the published per-case
# reviewed table. This reproduces the record; it does not independently regrade prose.
casefile=SRC/'GRCnext-Copilot/tests/prompt-evaluation-cases.md'
section=casefile.read_text().split('### Run 20261027-R2')[1].split('### Run 20261027-R1')[0]
case_rows=re.findall(r'^\| (B\d+|A\d+|SC\d+) \| (yes|no) \| (PASS|FAIL) \| (PASS|FAIL) \|',section,re.M)
acceptance={}
for idx,name in [(2,'claude-opus-5-5'),(3,'claude-sonnet-5-5')]:
    crit=[r for r in case_rows if r[1]=='yes']; other=[r for r in case_rows if r[1]=='no']
    cp=sum(r[idx]=='PASS' for r in crit);np=sum(r[idx]=='PASS' for r in other)
    acceptance[name]={'critical_pass':cp,'critical_total':len(crit),'other_pass':np,'other_total':len(other),
      'arithmetic_gate_pass':len(case_rows)==26 and cp==len(crit) and np/len(other)>=.8,
      'failed_cases':[r[0] for r in case_rows if r[idx]=='FAIL']}
check('E05 acceptance arithmetic reproduces recorded contrast',acceptance['claude-opus-5-5']['arithmetic_gate_pass'] and not acceptance['claude-sonnet-5-5']['arithmetic_gate_pass'],acceptance)

with (OUT/'historical-run-summary.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(runs[0]));w.writeheader();w.writerows(runs)
with (OUT/'paired-r2-tokens.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(paired[0]));w.writeheader();w.writerows(paired)
result={'checks':checks,'passed':sum(x['pass'] for x in checks),'total':len(checks),
 'runs':runs,'r2_comparison':comparison,'recorded_acceptance':acceptance,
 'fresh_model_calls':0,'enterprise_savings_validation':'NOT ESTABLISHED',
 'missing':['paired baseline and intervention workflow observations','measured human effort','invoice or attributable billing','pre-agreed enterprise thresholds','independent human acceptance of new module']}
(OUT/'validation-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
