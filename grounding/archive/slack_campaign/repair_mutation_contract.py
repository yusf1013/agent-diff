"""Bounded correction: environment-only mutation reuses its existing source cards.

Author/compile history remains intact. No solver or ground-truth feedback is
supplied. Fixes redundant reference extraction, not the user's source semantics.
"""
import argparse,copy
from concurrent.futures import ThreadPoolExecutor
from grounding.common.bedrock import save
from grounding.archive.slack_campaign.generate import ROOT,read,dump
from grounding.archive.slack_campaign.recover_construction import resume_recorded
from grounding.archive.slack_campaign.workflow import assemble,check,PROMPTS

def repair(cid):
    p=ROOT/'grounding/runs/slack_campaign/campaign_02/construction'/cid
    if (p/'source-contract-summary.json').exists():return
    a=read(p/'assignment.json');a['preserve_source_cards']=True
    save(p/'assignment-before-source-contract.json',read(p/'assignment.json'));save(p/'assignment.json',a)
    old=read(p/'design.json');save(p/'design-before-source-contract.json',old)
    design=copy.deepcopy(old);design['obligations']=design['obligations'][:1]
    design['task_spec']=a['source_context']['task_spec']
    save(p/'design.json',design)
    compiler=resume_recorded(p/'compiler');reviewer=resume_recorded(p/'reviewer')
    prior=sorted(p.glob('recovery-compiled-*.json'))[-1]
    compiled=read(prior)
    if compiled.get('selectors'):compiled['selectors']=compiled['selectors'][:1]
    save(p/'source-contract-provenance.json',{'reason':'Environment-only mutation should preserve the supplied source cards/spec; re-extracting them invented extra references and unnecessary bindings. Code copies them. Only the primary selector/bindings need compilation.','source_compilation':str(prior),'feedback_excludes':['solver outcomes','ground-truth labels']})
    for n in range(1,4):
        save(p/f'source-contract-compiled-{n}.json',compiled)
        try:case=assemble(a,design,compiled);checks=check(case,a,design,compiled)
        except Exception as exc:case=None;checks={'errors':[str(exc)]}
        save(p/f'source-contract-checks-{n}.json',checks)
        review=None
        if not checks['errors']:
            review=reviewer.ask(dump({'stage':'Final environment-only mutation review after mechanical source-card preservation. Do not re-extract extra references or require selectors for unchanged additional source cards. Check new rows do not alter ANY original intended reference. The same original prompt and cards define the request.', 'instructions':(PROMPTS/'reviewer.md').read_text(),'assignment':a,'design':design,'compiled':compiled,'case':case,'checks':checks}))
            save(p/f'source-contract-review-{n}.json',review)
            if review['validity']=='pass' and not any(i['kind'] in ('validity','annotation','access') for i in review['issues']):
                save(p/'case.json',case);status={'status':'review_pass','quality':review['quality'],'source_cards_preserved':True}
                save(p/'summary.json',status);save(p/'source-contract-summary.json',status);return
        if n<3:
            compiled=compiler.ask(dump({'feedback':'Thanks. Correct the compilation below. This environment-only mutation mechanically retains ALL original source cards and task lines. Return exactly ONE selector for the main obligation, with its original positive referents. Do not invent extra cards or DM membership references. Keep source prompt and all original intended selections unchanged. Full seed_edits, bindings, selectors, negative_referents and notes JSON required.','design':design,'source_cards':a['source_context']['cards'],'errors':checks['errors'],'review':review}))
    save(p/'source-contract-summary.json',{'status':'unrealized','errors':checks['errors'],'review':review})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);p.add_argument('--concurrency',type=int,default=1);a=p.parse_args()
    def safe(cid):
        try:repair(cid);print(cid,'source_contract_finished',flush=True)
        except Exception as exc:print(cid,type(exc).__name__,str(exc),flush=True)
    with ThreadPoolExecutor(max_workers=a.concurrency) as pool:list(pool.map(safe,a.ids))
