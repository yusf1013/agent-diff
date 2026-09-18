"""Finish recorded model outputs after local file-handling failures, without resampling."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from grounding.common.bedrock import Conversation,save
from grounding.archive.slack_campaign.generate import ROOT,read,dump
from grounding.archive.slack_campaign.recover_construction import resume_recorded,finish
from grounding.archive.slack_campaign.workflow import assemble,check,check_design,PROMPTS,source_context
from grounding.generation.selection import SELECTOR_GUIDE

def salvage(cid):
    p=ROOT/'grounding/runs/slack_campaign/campaign_02/construction'/cid
    if (p/'salvage-summary.json').exists():return
    a=read(p/'assignment.json');design=read(sorted((p/'writer').glob('turn-*/output.json'))[-1]);save(p/'design.json',design)
    errors=check_design(design,a)
    if errors:finish(p,{'status':'unrealized','errors':errors});return
    outputs=sorted((p/'compiler').glob('turn-*/output.json'))
    if outputs:
        compiled=read(outputs[-1]);compiler=resume_recorded(p/'compiler')
    else:
        cf=p/'compiler'
        if cf.exists():cf.rename(p/'compiler-before-salvage')
        compiler=Conversation(cf,(PROMPTS/'compiler.md').read_text(),max_tokens=24000)
        compiled=compiler.ask(dump({'assignment':a,'design':design,'base_seed':read(ROOT/'examples/slack/seeds/slack_bench_v2.json'),'domain':source_context(),'selector_syntax':SELECTOR_GUIDE}))
    rf=p/'reviewer'
    if list(rf.glob('turn-*/request.json')):reviewer=resume_recorded(rf)
    else:
        if rf.exists():rf.rename(p/'reviewer-before-salvage')
        reviewer=Conversation(rf,(PROMPTS/'reviewer.md').read_text(),max_tokens=24000)
    try:case=assemble(a,design,compiled);checks=check(case,a,design,compiled)
    except Exception as exc:case=None;checks={'errors':[str(exc)]}
    save(p/'salvage-compiled.json',compiled);save(p/'salvage-checks.json',checks)
    status={'status':'unrealized','errors':checks['errors'],'local_harness_recovery':True}
    if not checks['errors']:
        review=reviewer.ask(dump({'assignment':a,'design':design,'case':case,'compiled':compiled,'checks':checks}));save(p/'salvage-review.json',review)
        if review['validity']=='pass' and not any(i['kind'] in ('validity','annotation','access') for i in review['issues']):
            save(p/'case.json',case);status={'status':'review_pass','quality':review['quality'],'local_harness_recovery':True}
        else:status['review']=review
    save(p/'salvage-summary.json',status);finish(p,status)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);a=p.parse_args()
    def safe(cid):
        try:salvage(cid);print(cid,'salvage_finished',flush=True)
        except Exception as exc:
            status={'status':'error','local_harness_recovery':True,'error':f'{type(exc).__name__}: {exc}'}
            folder=ROOT/'grounding/runs/slack_campaign/campaign_02/construction'/cid
            save(folder/'salvage-summary.json',status);finish(folder,status);print(cid,status,flush=True)
    with ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(safe,a.ids))
