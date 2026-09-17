"""Redistribute not-yet-started members of the existing bounded recovery pass.

The original serial worker sees the atomic marker and skips claimed cases.
This does not create another authoring attempt or select by solver outcome.
"""
import argparse,json
from concurrent.futures import ThreadPoolExecutor
from .generate import ROOT,read
from .recover_construction import recover,finish

BASE=ROOT/'experiments/slack_campaign/campaign_02/construction'
def claim(cid):
    folder=BASE/cid
    # Never claim a case whose authoring call is already in flight.
    if any(read(p).get('status')=='running' for p in folder.glob('*/turn-*/summary.json')):
        return False
    try:
        with (folder/'recovery-summary.json').open('x') as f:
            json.dump({'status':'recovery_claimed','reason':'Same previously queued recovery, transferred to parallel worker.'},f)
        return True
    except FileExistsError:return False

def run(cid):
    try:recover(cid,claimed=True);print(cid,'recovery_finished',flush=True)
    except Exception as exc:
        finish(BASE/cid,{'status':'error','bounded_recovery_exhausted':True,'error':f'{type(exc).__name__}: {exc}'})
        print(cid,type(exc).__name__,str(exc),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);p.add_argument('--concurrency',type=int,default=8);a=p.parse_args()
    ids=[cid for cid in a.ids if claim(cid)]
    print('Transferred queued cases:',ids,flush=True)
    with ThreadPoolExecutor(max_workers=a.concurrency) as pool:list(pool.map(run,ids))
