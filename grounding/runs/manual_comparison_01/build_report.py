"""Project manually authored judgments into tables and evidence pages; no grading."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import os

HERE = Path(__file__).resolve().parent
CATEGORIES = ['grounding_failures', 'downstream_failures', 'misreporting', 'other_failures']
MODEL_NAMES = {'sonnet5': 'Sonnet 5', 'haiku45': 'Haiku 4.5'}
# Manual mapping from the fixed story3 ambiguity index. Position is relative to
# the target-rooted reference chain; W07's removal channel is a side branch.
LOCI = {
 'W01-underspecified': ('User', 'terminal', 'reacting Priya'),
 'W01-underspecified-message': ('Message', 'target', 'message'),
 'W02-underspecified-reactor': ('User', 'target', 'reactor'),
 'W02-underspecified-announcement': ('Message', 'intermediate', 'budget-freeze announcement'),
 'W02-underspecified-channel': ('Channel', 'terminal', 'announcement channel'),
 'W03-base': ('User', 'terminal', 'reacting Alex'),
 'W03-underspecified-message': ('Message', 'intermediate', 'budget-freeze announcement'),
 'W03-underspecified-channel': ('Channel', 'target', 'posting channel'),
 'W04-underspecified': ('Message', 'target', 'rollout checklist'),
 'W04-underspecified-reaction': ('Reaction', 'intermediate', 'emoji from source announcement'),
 'W04-underspecified-channel': ('Channel', 'terminal', 'reactor membership channel'),
 'W05-underspecified': ('Channel', 'target', 'onboarding channel'),
 'W06-underspecified': ('Message', 'target', 'kickoff message'),
 'W06-underspecified-author': ('User', 'intermediate', 'author Dana'),
 'W06-underspecified-channel': ('Channel', 'terminal', 'author membership channel'),
 'W07-base': ('User', 'target', 'Jordan'),
 'W07-underspecified-message': ('Message', 'intermediate', 'security-audit announcement'),
 'W07-underspecified-removal-channel': ('Channel', 'side_branch', 'removal channel'),
 'W08-underspecified-reaction': ('Reaction', 'target', 'reaction to remove'),
 'W08-underspecified': ('Message', 'intermediate', 'source message'),
 'W08-underspecified-channel': ('Channel', 'terminal', 'author membership channel'),
 'W09-underspecified': ('User', 'intermediate', 'bot'),
 'W09-underspecified-channel': ('Channel', 'terminal', 'bot membership channel'),
 'W10-underspecified': ('User', 'terminal', 'channel member Priya'),
 'W10-underspecified-channel': ('Channel', 'intermediate', 'checklist channel'),
 'W10-underspecified-message': ('Message', 'intermediate', 'checklist'),
}

def read(path): return json.loads(path.read_text())
def write(path, value): path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
def link(label, path, source):
 return f'[{label}]({Path(os.path.relpath(path, source.parent)).as_posix()})'
def tally(rows):
 return {'cases': len(rows), 'grounding': dict(Counter(r['grounding'] for r in rows)),
         **{k: sum(bool(r[k]) for r in rows) for k in CATEGORIES},
         'any_failure': sum(any(r[k] for k in CATEGORIES) for r in rows)}

def main():
 manifest = read(HERE/'dataset/manifest.json')
 cases = {v['case_id']:read(HERE/'dataset'/v['path']) for v in manifest['cases']}
 assert {k for k,c in cases.items() if c['private']['mode']=='underspecified'} == set(LOCI)
 rows = [r for f in sorted((HERE/'manual_review').glob('w*.json')) for r in read(f)]
 keys = [(r['model'],r['case_id']) for r in rows]
 expected = {(m,c) for m in MODEL_NAMES for c in cases}
 assert len(keys)==len(set(keys)), 'Duplicate judgments'
 assert set(keys)==expected, f'Missing/extra judgments: {expected.symmetric_difference(keys)}'
 for r in rows:
  assert r['uncertainty'] is None, f'Unsettled judgment: {r["model"]}/{r["case_id"]}'
  assert (r['grounding']=='incorrect') == bool(r['grounding_failures'])
  for e in r['evidence']:
   data=read(HERE/e['file'])
   for key in e['pointer'].strip('/').split('/'):
    if key: data=data[int(key)] if isinstance(data,list) else data[key.replace('~1','/').replace('~0','~')]
  c=cases[r['case_id']]
  r['mode']=c['private']['mode']
  r['family']=c['private']['base_story']
  r['task_type']=c['cards'][0]['Task type']
  r['ambiguity_locus']=dict(zip(['entity','position','description'],LOCI[r['case_id']])) if r['case_id'] in LOCI else None
 rows.sort(key=lambda r:(r['case_id'],r['model']))
 write(HERE/'assessments.json',rows)
 summary={}
 for m in MODEL_NAMES:
  rr=[r for r in rows if r['model']==m]
  summary[m]={'overall':tally(rr)}
  for field in ['mode','family','task_type']:
   summary[m]['by_'+field]={v:tally([r for r in rr if r[field]==v]) for v in sorted({r[field] for r in rr})}
  for field in ['entity','position']:
   summary[m]['ambiguity_by_'+field]={v:tally([r for r in rr if r['ambiguity_locus'] and r['ambiguity_locus'][field]==v]) for v in sorted({r['ambiguity_locus'][field] for r in rr if r['ambiguity_locus']})}
 write(HERE/'metrics.json',summary)
 usage=read(HERE/'usage_summary.json');plan=read(HERE/'plan.json');costs={}
 for m,u in usage['models'].items():
  t=u['tokens'];rates=plan['models'][m]['rates']; prompt=sum(t[k] for k in t if k!='output_tokens')
  cached=sum(t[k]*rates[k]/1e6 for k in t)
  no_cache=(prompt*rates['input_tokens']+t['output_tokens']*rates['output_tokens'])/1e6
  attempts=[a for a in usage['attempts'] if a['model_alias']==m]
  costs[m]={**u, 'total_prompt_tokens':prompt, 'cache_read_fraction':t['cache_read_input_tokens']/prompt,
            'same_tokens_without_cache_usd':no_cache,'estimated_savings_usd':no_cache-cached,
            'estimated_savings_fraction':(no_cache-cached)/no_cache,
            'successful_requests':sum(a['usage']['successful_requests'] for a in attempts),
            'failed_requests':sum(a['usage']['failed_requests'] for a in attempts),
            'retry_attempts':sum(a['usage']['retry_attempts'] for a in attempts),
            'terminations':dict(Counter(a['termination'] for a in attempts)),
            'total_turns':sum(a['turns'] for a in attempts)}
 write(HERE/'costs.json',costs)
 pages=HERE/'case_reviews';pages.mkdir(exist_ok=True)
 index=['# Case-by-case manual review','', 'All 114 trajectories, designated final responses and native net diffs were manually reviewed. Category counts overlap. “None” means no remaining failure was demonstrated, not a universal correctness guarantee. See the [review policy](manual_review_policy.md) and [machine-readable judgments](assessments.json).','', '| Case | Mode | Sonnet 5 | Haiku 4.5 |','|---|---|---|---|']
 for cid in cases:
  c=cases[cid];page=pages/(cid+'.md');group=[r for r in rows if r['case_id']==cid]
  lines=[f'# {cid}', '',c['prompt'],'',f"Resolution mode: **{c['private']['mode']}**. "+link('Fixed seed, card and specification',HERE/'dataset/cases'/(cid+'.json'),page)+'.','']
  if cid in LOCI:
   e,p,d=LOCI[cid];lines += [f'Ambiguity: **{e} — {d}** ({p.replace("_"," ")}).','']
  for m in MODEL_NAMES:
   r=next(r for r in group if r['model']==m);raw=HERE/'runs'/m/cid/'attempt-01';flags=[k.replace('_',' ') for k in CATEGORIES if r[k]]
   lines += [f'## {MODEL_NAMES[m]}','',f"Grounding: **{r['grounding']}**. Remaining failures: **{', '.join(flags) if flags else 'none demonstrated'}**.",'',r['trajectory_summary'],'', '**Response:** '+r['response_assessment'],'','**Net diff:** '+r['diff_assessment'],'']
   for k in CATEGORIES:
    if r[k]: lines += ['**'+k.replace('_',' ').capitalize()+':**','']+['- '+s for s in r[k]]+['']
   if r['recovered_notes']: lines += ['**Recovery notes:**','']+['- '+s for s in r['recovered_notes']]+['']
   answer = link('final answer',raw/'solver/final_response.md',page) if (raw/'solver/final_response.md').exists() else 'no designated final answer'
   lines += ['Sources: '+', '.join([link('full trajectory',raw/'solver'/(cid+'.json'),page),answer,link('native diff',raw/'environment/diff_run.json',page),link('initial state',raw/'environment/initial_state.json',page),link('final state',raw/'environment/final_state.json',page)])+'.','']
  page.write_text('\n'.join(lines))
  cells=[]
  for m in MODEL_NAMES:
   r=next(r for r in group if r['model']==m)
   short=[abbr for k,abbr in zip(CATEGORIES,['G','D','M','O']) if r[k]]
   cells.append(', '.join(short) or ('Not established' if r['grounding']=='not_established' else 'None'))
  index.append(f'| {link(cid,page,HERE/"case_reviews.md")} | {c["private"]["mode"]} | {cells[0]} | {cells[1]} |')
 index += ['', 'G = grounding; D = downstream operation/deliverable; M = misreporting; O = other remaining failure.','']
 (HERE/'case_reviews.md').write_text('\n'.join(index))
 ambiguity=['# Ambiguity-location results','','All entries use the pre-execution cards. Position is relative to the target-rooted chain. Outcomes are grounding judgments; follow the case link for action/reporting findings and raw evidence.','','| Case | Ambiguous entity and role | Position | Sonnet 5 | Haiku 4.5 |','|---|---|---|---|---|']
 for cid in sorted(LOCI):
  a=next(r for r in rows if r['case_id']==cid and r['model']=='sonnet5')
  b=next(r for r in rows if r['case_id']==cid and r['model']=='haiku45')
  locus=a['ambiguity_locus']
  ambiguity.append(f"| [{cid}](case_reviews/{cid}.md) | {locus['entity']}: {locus['description']} | {locus['position'].replace('_',' ')} | {a['grounding']} | {b['grounding']} |")
 (HERE/'ambiguity_reviews.md').write_text('\n'.join(ambiguity)+'\n')
 print(json.dumps({'overall':{m:v['overall'] for m,v in summary.items()},'costs':{m:c['estimated_cost_usd'] for m,c in costs.items()}},indent=2))

if __name__=='__main__': main()
