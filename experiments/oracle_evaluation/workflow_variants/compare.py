from pathlib import Path
import json,statistics
root=Path(__file__).parent
expected_ground={str(i):'demonstrated_correct' if i in (1,2,3,5) else 'demonstrated_incorrect' for i in range(1,9)}
links={1:['1','2'],2:['3'],3:['4'],4:['4'],5:[],6:['5'],7:['6'],8:['7','8']}
def read_stage(p,phase=False):
 if not (p/'summary.json').exists(): return None
 summary=json.loads((p/'summary.json').read_text())
 result={k:summary.get(k) for k in ['status','stop_reason','elapsed_seconds','usage','validation_errors','error']}
 result['directory']=str(p)
 report=p/('applicability.json' if phase else 'assessment.json')
 if report.exists():
  a=json.loads(report.read_text());result['lines']=[{k:r[k] for k in ('line','task_status','execution_status','grounding') if k in r} for r in a['lines']]
  result['assessment_issue']=a.get('assessment_issue')
  result['applicability_errors']=[];result['execution_errors']=[];result['grounding_errors']=[]
  rows={r['line']:r for r in a['lines']}
  if [r['line'] for r in a['lines']]!=list(range(1,9)):result['applicability_errors'].append('inventory')
  for i in range(1,9):
   r=rows.get(i,{})
   if r.get('task_status')!=('active' if i<7 else 'inactive'):result['applicability_errors'].append(i)
   if not phase:
    if r.get('execution_status')!='performed':result['execution_errors'].append(i)
    if r.get('grounding')!={k:expected_ground[k] for k in links[i]}:result['grounding_errors'].append(i)
  if not phase:
   result['overall_grounding']=a['obligations'];result['overall_grounding_correct']=a['obligations']==expected_ground
   result['categorical_match']=not any(result[k] for k in ['applicability_errors','execution_errors','grounding_errors']) and result['overall_grounding_correct']
  result['output_characters']=len(report.read_text())
  result['explanation_characters']=sum(len(r.get('explanation','')) for r in a['lines'])
 return result
runs=[]
for v in ('ordered','separated','two-turn'):
 for i in range(1,6):
  p=root/f'{v}-{i}';r={'variant':v,'repeat':i,'initial':read_stage(p),'repair':read_stage(p.with_name(p.name+'-repair-1'))}
  if v=='two-turn':r['applicability_stage']=read_stage(p.with_name(p.name+'-applicability'),True)
  r['final']=r['repair'] if r['repair'] and r['repair'].get('lines') else r['initial']
  if r['initial'] and r['repair'] and r['initial'].get('lines') and r['repair'].get('lines'):
   byline={x['line']:x for x in r['repair']['lines']};changes=[]
   for row in r['initial']['lines']:
    for k in ('task_status','execution_status','grounding'):
     if k in row and row[k]!=byline.get(row['line'],{}).get(k):changes.append({'line':row['line'],'field':k,'before':row[k],'after':byline.get(row['line'],{}).get(k)})
   r['repair_judgment_changes']=changes
  runs.append(r)
ledger=[json.loads(line) for line in (root/'usage_ledger.jsonl').read_text().splitlines()] if (root/'usage_ledger.jsonl').exists() else []
summaries=[]
for v in ('ordered','separated','two-turn'):
 selected=[r for r in runs if r['variant']==v]
 calls=[c for c in ledger if Path(c['output_directory']).name.startswith(v+'-')]
 out={'variant':v,'complete_initial_reports':sum(bool(r['initial'] and r['initial'].get('lines')) for r in selected),'initial_categorical_matches':sum(bool(r['initial'] and r['initial'].get('categorical_match')) for r in selected),'final_categorical_matches':sum(bool(r['final'] and r['final'].get('categorical_match')) for r in selected),'final_mechanical_passes':sum(bool(r['final'] and r['final']['status']=='returned' and r['final'].get('validation_errors')==[]) for r in selected),'api_calls_recorded':len(calls),'input_tokens':sum(c.get('usage',{}).get('input_tokens',0) for c in calls),'output_tokens':sum(c.get('usage',{}).get('output_tokens',0) for c in calls),'thinking_tokens':sum(c.get('usage',{}).get('output_tokens_details',{}).get('thinking_tokens',0) for c in calls),'calls_without_usage':sum(c.get('usage') is None for c in calls),'cost_usd':None}
 elapsed=[]
 for r in selected:
  stages=[r.get('applicability_stage'),r['initial'],r['repair']]
  present=[s for s in stages if s]
  if r['final'] and r['final']['status']!='running' and all(s.get('elapsed_seconds') is not None for s in present): elapsed.append(sum(s['elapsed_seconds'] for s in present))
 out['mean_total_seconds']=statistics.mean(elapsed) if elapsed else None
 summaries.append(out)
(root/'comparison.json').write_text(json.dumps({'runs':runs,'summary':summaries},indent=2)+'\n')
for s in summaries:print(json.dumps(s))
for r in runs:
 final=r['final'];state='not ready' if not final else final['status']
 print(r['variant'],r['repeat'],state,'app',final.get('applicability_errors') if final else None,'ground',final.get('overall_grounding_correct') if final else None,'validation',final.get('validation_errors') if final else None)
