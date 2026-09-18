from pathlib import Path
from collections import Counter,defaultdict
import itertools,json,statistics
ROOT=Path(__file__).parent
references={r['test_id']:r for r in json.loads((ROOT/'reference/expected.json').read_text())}
selection=json.loads((ROOT/'selection.json').read_text())

def load(p):return json.loads(p.read_text())
def stage(folder):
 if not (folder/'summary.json').exists():return None
 summary=load(folder/'summary.json')
 report=load(folder/'assessment.json') if (folder/'assessment.json').exists() else None
 if not isinstance(report,dict) or not isinstance(report.get('lines'),list):report=None
 return {'folder':str(folder),'summary':summary,'report':report}
def score(ref,report):
 actual={x.get('line'):x for x in report.get('lines',[]) if isinstance(x,dict)} if report else {}
 checks=[]
 def check(category,key,value,allowed):checks.append({'category':category,'key':key,'observed':value,'allowed':allowed,'match':value in allowed})
 for expected in ref['lines']:
  n=expected['line'];got=actual.get(n,{})
  if expected.get('marker'):
   check('structure',f'L{n}.marker',got=={'line':n},[True]);continue
  for category in ('task_status','execution_status'):
   if category not in expected.get('unscored_fields',[]):check(category,f'L{n}.{category}',got.get(category,'MISSING'),expected[category])
  for key,allowed in expected.get('grounding',{}).items():
   check('linked_grounding',f'L{n}.O{key}',got.get('grounding',{}).get(key,'MISSING'),allowed)
 for key,allowed in ref['obligations'].items():
  check('overall_grounding',f'O{key}',(report or {}).get('obligations',{}).get(key,'MISSING'),allowed)
 return {'checks':checks,'matches':sum(c['match'] for c in checks),'total':len(checks),'all_match':all(c['match'] for c in checks),'mismatches':[c for c in checks if not c['match']]}
def fingerprint(report):
 if not report:return None
 value={'lines':[{k:r[k] for k in ('line','task_status','execution_status') if k in r} for r in report['lines']], 'obligations':report.get('obligations')}
 return json.dumps(value,sort_keys=True)

runs=[]
for sel in selection:
 tid=sel['test_id'];ref=references[tid]
 for variant in ('ordered','separated'):
  for n in range(1,6):
   name=f'{tid}-{variant}-{n}';first=stage(ROOT/'runs'/name);repair=stage(ROOT/'runs'/(name+'-repair-1'))
   final=repair if repair else first
   obj={'test_id':tid,'variant':variant,'repeat':n,'initial':first,'repair':repair,'final':final}
   obj['complete']=bool(final and final['summary'].get('status')=='returned' and final['summary'].get('stop_reason')=='end_turn' and final['report'])
   obj['pending']=not final or final['summary'].get('status')=='running'
   obj['mechanical_pass']=bool(obj['complete'] and final['summary'].get('validation_errors')==[])
   obj['score']=score(ref,final['report'] if obj['complete'] else None)
   obj['initial_score']=score(ref,first['report'] if first and first['summary'].get('stop_reason')=='end_turn' else None)
   obj['fingerprint']=fingerprint(final['report']) if obj['complete'] else None
   obj['latency']=sum(s['summary'].get('elapsed_seconds',0) for s in (first,repair) if s) if not obj['pending'] else None
   if first and repair and first['report'] and repair['report']:
    before={r['line']:r for r in first['report']['lines']};after={r['line']:r for r in repair['report']['lines']}
    obj['repair_judgment_changes']=[{'line':n,'field':k,'before':r[k],'after':after.get(n,{}).get(k,'MISSING')} for n,r in before.items() for k in ('task_status','execution_status','grounding') if k in r and r[k]!=after.get(n,{}).get(k,'MISSING')]
    if first['report'].get('obligations')!=repair['report'].get('obligations'):obj['repair_judgment_changes'].append({'field':'obligations','before':first['report'].get('obligations'),'after':repair['report'].get('obligations')})
   runs.append(obj)
per_case=[]
for tid in references:
 for v in ('ordered','separated'):
  rr=[r for r in runs if r['test_id']==tid and r['variant']==v]
  fingerprints=[r['fingerprint'] for r in rr if r['fingerprint']]
  tally=Counter(fingerprints);pairs=list(itertools.combinations(fingerprints,2))
  byfield=defaultdict(Counter)
  for r in rr:
   if r['complete']:
    for c in r['score']['checks']:byfield[c['key']][json.dumps(c['observed'])]+=1
  per_case.append({'test_id':tid,'variant':v,'complete':sum(r['complete'] for r in rr),'pending':sum(r['pending'] for r in rr),'mechanical_pass':sum(r['mechanical_pass'] for r in rr),'all_scored_fields_match':sum(r['complete'] and r['score']['all_match'] for r in rr),'initial_all_scored_fields_match':sum(bool(r['initial'] and r['initial']['report'] and r['initial_score']['all_match']) for r in rr),'mode_count':max(tally.values(),default=0),'distinct_category_patterns':len(tally),'pairwise_agreement':sum(a==b for a,b in pairs)/len(pairs) if pairs else None,'scored_field_outcomes':dict(byfield)})
ledger=[json.loads(l) for l in (ROOT/'runs/usage_ledger.jsonl').read_text().splitlines()] if (ROOT/'runs/usage_ledger.jsonl').exists() else []
variants=[]
for v in ('ordered','separated'):
 rr=[r for r in runs if r['variant']==v];counts={}
 for category in ('task_status','execution_status','linked_grounding','overall_grounding','structure'):
  cc=[c for r in rr for c in r['score']['checks'] if c['category']==category]
  returned=[c for r in rr if r['complete'] for c in r['score']['checks'] if c['category']==category]
  counts[category]={'matches_all_attempts':sum(c['match'] for c in cc),'scored_fields_all_attempts':len(cc),'matches_returned':sum(c['match'] for c in returned),'scored_fields_returned':len(returned)}
 calls=[c for c in ledger if f'-{v}-' in Path(c['output_directory']).name]
 variants.append({'variant':v,'attempted_conversations':50,'pending':sum(r['pending'] for r in rr),'complete':sum(r['complete'] for r in rr),'mechanical_pass':sum(r['mechanical_pass'] for r in rr),'initial_mechanical_pass':sum(bool(r['initial'] and r['initial']['report'] and r['initial']['summary'].get('status')=='returned' and r['initial']['summary'].get('validation_errors')==[]) for r in rr),'repairs':sum(bool(r['repair']) for r in rr),'all_scored_fields_match':sum(r['complete'] and r['score']['all_match'] for r in rr),'initial_all_scored_fields_match':sum(bool(r['initial'] and r['initial']['report'] and r['initial_score']['all_match']) for r in rr),'categories':counts,'cases_unanimous':sum(p['complete']==5 and p['mode_count']==5 for p in per_case if p['variant']==v),'api_calls':len(calls),'input_tokens':sum((s.get('usage') or {}).get('input_tokens',0) for s in calls),'output_tokens':sum((s.get('usage') or {}).get('output_tokens',0) for s in calls),'thinking_tokens':sum((s.get('usage') or {}).get('output_tokens_details',{}).get('thinking_tokens',0) for s in calls),'calls_without_usage':sum(not s.get('usage') for s in calls),'cost_usd':None,'mean_total_latency':statistics.mean(r['latency'] for r in rr if r['latency'] is not None) if any(r['latency'] is not None for r in rr) else None})
# Reports and raw histories remain in per-call directories; avoid duplicating payloads here.
serial_runs=[]
for r in runs:
 rr=dict(r)
 for name in ('initial','repair','final'):
  if rr[name]:rr[name]={k:v for k,v in rr[name].items() if k!='report'}
 serial_runs.append(rr)
(ROOT/'comparison.json').write_text(json.dumps({'variants':variants,'per_case':per_case,'runs':serial_runs},indent=2)+'\n')
for v in variants:print(json.dumps({k:val for k,val in v.items() if k!='categories'}))
for p in per_case:
 if p['complete'] or p['pending']<5:print(p['test_id'],p['variant'],'complete',p['complete'],'reference match',p['all_scored_fields_match'],'mode',p['mode_count'],'pending',p['pending'])
