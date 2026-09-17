"""One explicit writer revision after manual route audit; no solver feedback.

Earlier cases, executions, labels and costs remain independently inspectable.
The writer receives only construction findings, never run outcomes or flags.
"""
import argparse,asyncio,hashlib
from concurrent.futures import ThreadPoolExecutor
from .generate import ROOT,read
from .bedrock import save
from .recover_construction import recover
from .execute import one

def revise(cid):
    base=ROOT/'experiments/slack_campaign/campaign_02';p=base/'construction'/cid
    if (p/'route-revision-summary.json').exists():return
    audit=read(base/'manual_review.json')['cases'][cid]
    # Only the construction reason is passed; solver judgments stay outside.
    reason=audit['reason'].split(' Independently of the unsupported tenure field')[0]
    old=read(p/'summary.json');save(p/'summary-before-route-revision.json',old)
    save(p/'case-before-route-revision.json',read(p/'case.json'))
    save(base/'manual_review_history'/f'{cid}-before-route-revision.json',audit)
    save(p/'summary.json',{'status':'manual_revision_required','construction_finding':reason,
         'instruction':'Return the defect to the writer. Revise the prompt only as necessary to realize the assigned relationships and supported deliverable; preserve route/mode. Do not retain unrelated old identifying clauses merely to reuse seed text.'})
    recover(cid)
    final=read(p/'summary.json')
    save(p/'route-revision-summary.json',{'construction_status':final['status'],'manual_development_revision':True})
    if final['status']=='review_pass':
        execution=base/'execution'/cid
        if execution.exists():execution.rename(base/'execution_attempts'/(cid+'-before-route-revision'))
        # The original queue may already have visited this ID; resume explicitly.
        asyncio.run(one(base,cid,'postgresql://postgres@127.0.0.1:15432/agentdiff_campaign'))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);p.add_argument('--concurrency',type=int,default=2);a=p.parse_args()
    def safe(cid):
        try:revise(cid);print(cid,'revision_finished',flush=True)
        except Exception as exc:print(cid,type(exc).__name__,str(exc),flush=True)
    with ThreadPoolExecutor(max_workers=a.concurrency) as pool:list(pool.map(safe,a.ids))
