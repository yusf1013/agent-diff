"""Project manually authored Qwen judgments into tables and evidence pages; no grading.

Mirrors manual_comparison_01/build_report.py for the single Purdue model.
Scored trial per case is the latest completed attempt (attempt-02 normally,
attempt-03 for the W04-underspecified-channel server-error retry). Usage and
costs cover scored trials only; failed infrastructure attempts are retained
separately and disclosed in the report.
"""
from pathlib import Path
from collections import Counter
import json
import os

HERE = Path(__file__).resolve().parent
CATEGORIES = ['grounding_failures', 'downstream_failures', 'misreporting', 'other_failures']
MODEL_NAMES = {'qwen36': 'Qwen 3.6 27B'}
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

def read(path): return json.loads(Path(path).read_text())
def write(path, value): path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
def link(label, path, source):
 return f'[{label}]({Path(os.path.relpath(path, source.parent)).as_posix()})'
def tally(rows):
 return {'cases': len(rows), 'grounding': dict(Counter(r['grounding'] for r in rows)),
         **{k: sum(bool(r[k]) for r in rows) for k in CATEGORIES},
         'any_failure': sum(any(r[k] for k in CATEGORIES) for r in rows)}

def scored_attempt(cid):
    cands = sorted((HERE/'runs'/'qwen36'/cid).glob('attempt-*/execution_summary.json'))
    done = [p for p in cands if read(p).get('status') == 'completed']
    assert done, f'No completed attempt for {cid}'
    return done[-1].parent

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
  assert r['uncertainty'] is None, f"Unsettled judgment: {r['model']}/{r['case_id']}"
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
 # Scored-trial usage from solver records (excludes failed infrastructure attempts).
 tokens = {'input_tokens':0,'output_tokens':0,'cache_creation_input_tokens':0,'cache_read_input_tokens':0}
 turns = 0; terms = Counter(); reqs = 0; retries = 0
 for cid in cases:
  raw = scored_attempt(cid)
  rec = read(raw/'solver'/(cid+'.json'))
  u = rec.get('usage',{})
  for k in tokens: tokens[k]+=u.get(k,0)
  turns += len(rec.get('steps',[]))
  terms[rec.get('termination')]+=1
  reqs += u.get('successful_requests',0)
  retries += u.get('retry_attempts',0)
 costs={'qwen36':{'attempts':57,'completed':57,'tokens':tokens,
   'thinking_tokens':None,
   'thinking_tokens_note':'unavailable: provider does not report thinking-token counts; historical costs.json records 0, see LIMITATIONS.md',
   'estimated_cost_usd':0.0,
   'cost_source':'Purdue GenAI Studio has no per-token charge to this account; tokens are provider-reported, cost is recorded as 0 (not an invoice)',
   'total_prompt_tokens':tokens['input_tokens'],'cache_read_fraction':0.0,
   'same_tokens_without_cache_usd':0.0,'estimated_savings_usd':0.0,'estimated_savings_fraction':0.0,
   'successful_requests':reqs,'failed_requests':0,'retry_attempts':retries,
   'terminations':dict(terms),'total_turns':turns,
   'scored_attempts_note':'attempt-02 except W01-base/W01-single (attempt-01) and W04-underspecified-channel (attempt-03)'}}
 write(HERE/'costs.json',costs)
 pages=HERE/'case_reviews';pages.mkdir(exist_ok=True)
 index=['# Case-by-case manual review','', 'All 57 trajectories, designated final responses and native net diffs were manually reviewed. Category counts overlap. “None” means no remaining failure was demonstrated, not a universal correctness guarantee. See the [review policy](manual_review_policy.md) and [machine-readable judgments](assessments.json).','', '| Case | Mode | Qwen 3.6 27B |','|---|---|---|']
 for cid in cases:
  c=cases[cid];page=pages/(cid+'.md');group=[r for r in rows if r['case_id']==cid]
  lines=[f'# {cid}', '',c['prompt'],'',f"Resolution mode: **{c['private']['mode']}**. "+link('Fixed seed, card and specification',HERE/'dataset/cases'/(cid+'.json'),page)+'.','']
  if cid in LOCI:
   e,p,d=LOCI[cid];lines += [f'Ambiguity: **{e} — {d}** ({p.replace("_"," ")}).','']
  for m in MODEL_NAMES:
   r=next(r for r in group if r['model']==m);raw=scored_attempt(cid);flags=[k.replace('_',' ') for k in CATEGORIES if r[k]]
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
  index.append(f'| {link(cid,page,HERE/"case_reviews.md")} | {c["private"]["mode"]} | {cells[0]} |')
 index += ['', 'G = grounding; D = downstream operation/deliverable; M = misreporting; O = other remaining failure.','']
 (HERE/'case_reviews.md').write_text('\n'.join(index))
 ambiguity=['# Ambiguity-location results','','All entries use the pre-execution cards. Position is relative to the target-rooted chain. Outcomes are grounding judgments; follow the case link for action/reporting findings and raw evidence.','','| Case | Ambiguous entity and role | Position | Qwen 3.6 27B |','|---|---|---|---|']
 for cid in sorted(LOCI):
  a=next(r for r in rows if r['case_id']==cid and r['model']=='qwen36')
  locus=a['ambiguity_locus']
  ambiguity.append(f"| [{cid}](case_reviews/{cid}.md) | {locus['entity']}: {locus['description']} | {locus['position'].replace('_',' ')} | {a['grounding']} |")
 (HERE/'ambiguity_reviews.md').write_text('\n'.join(ambiguity)+'\n')
 print(json.dumps({'overall':{m:v['overall'] for m,v in summary.items()},'tokens':tokens,'requests':reqs,'retries':retries,'terminations':dict(terms)},indent=2))

if __name__=='__main__': main()
