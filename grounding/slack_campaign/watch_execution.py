"""Bounded execution queue for completed construction, with restartable artifacts."""
import argparse
import asyncio
from .generate import ROOT,read
from .execute import one

async def watch(concurrency):
    folder=ROOT/'experiments/slack_campaign/campaign_02'
    active={};seen=set();database='postgresql://postgres@127.0.0.1:15432/agentdiff_campaign'
    while True:
        for cid,task in list(active.items()):
            if task.done():
                try:task.result()
                except Exception as exc:print(cid,'worker_error',str(exc),flush=True)
                del active[cid]
        planned=read(folder/'assignments.json')
        if (folder/'mutation_assignments.json').exists():planned+=read(folder/'mutation_assignments.json')
        finished=0
        for a in planned:
            cid=a['case_id'];source=folder/'construction'/cid
            if not (source/'summary.json').exists():continue
            status=read(source/'summary.json')['status']
            if status not in ('design_written','running'):finished+=1
            if status!='review_pass' or cid in active or cid in seen:continue
            manual=read(folder/'manual_review.json').get('cases',{}) if (folder/'manual_review.json').exists() else {}
            if manual.get(cid,{}).get('assigned_route_realized') is False:
                seen.add(cid);continue
            if (folder/'execution'/cid/'summary.json').exists():seen.add(cid);continue
            if len(active)>=concurrency:continue
            active[cid]=asyncio.create_task(one(folder,cid,database));seen.add(cid)
        if finished==len(planned) and not active:
            print('Execution queue drained; construction attempts:',finished,flush=True);return
        await asyncio.sleep(3)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--concurrency',type=int,default=2);a=p.parse_args()
    asyncio.run(watch(a.concurrency))
