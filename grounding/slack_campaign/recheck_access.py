"""Recheck saved observations after a harness correction, without model calls.

Only a newly established mechanical proof permits resuming execution. Earlier
failed artifacts and costs are preserved. Cases rejected by manual route review
are not resumed.
"""
import argparse,asyncio
from .generate import ROOT,read
from .bedrock import save
from .runtime import certify_visibility
from .execute import one

async def run(concurrency):
    b=ROOT/'experiments/slack_campaign/campaign_02';manual=read(b/'manual_review.json')['cases'];todo=[]
    for p in sorted((b/'execution').glob('*/summary.json')):
        if read(p)['status']!='access_unresolved':continue
        cid=p.parent.name
        if manual.get(cid,{}).get('assigned_route_realized') is False:continue
        q=p.parent/'preflight'
        result=certify_visibility(read(q/'case.json'),read(q/'initial_state.json'),read(q/'visibility.json'))
        save(p.parent/'mechanical-access-recheck.json',result)
        if result['certified']:
            archive=b/'execution_attempts'/(cid+'-before-mechanical-recheck')
            if archive.exists():continue
            p.parent.rename(archive);todo.append(cid)
    semaphore=asyncio.Semaphore(concurrency)
    async def execute(cid):
        async with semaphore:await one(b,cid,'postgresql://postgres@127.0.0.1:15432/agentdiff_campaign')
    await asyncio.gather(*(execute(cid) for cid in todo))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--concurrency',type=int,default=1);a=p.parse_args();asyncio.run(run(a.concurrency))
