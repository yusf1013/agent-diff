"""Qualify the already-written access repair before asking the reviewer to approve it."""
import argparse,asyncio
from grounding.common.bedrock import save
from grounding.archive.slack_campaign.generate import ROOT,read,dump
from grounding.archive.slack_campaign.recover_construction import resume_recorded
from grounding.archive.slack_campaign.workflow import assemble,check
from grounding.integrations.agentdiff import runtime
from grounding.archive.slack_campaign.verify_access import verify_access
from grounding.archive.slack_campaign.execute import one

BASE=ROOT/'grounding/runs/slack_campaign/campaign_02';DB='postgresql://postgres@127.0.0.1:15432/agentdiff_campaign'
def finish(cid):
    p=BASE/'construction'/cid
    if (p/'live-access-repair-summary.json').exists():return
    compiled=read(sorted(p.glob('access-repair-compiled-*.json'))[-1]);a=read(p/'assignment.json');design=read(p/'design.json')
    case=assemble(a,design,compiled);checks=check(case,a,design,compiled)
    if checks['errors']:raise ValueError(str(checks['errors']))
    folder=p/'live-access-repair';prepared=runtime.prepare(case,folder,DB)
    try:
        state=read(prepared['initial_state_path']);visibility=read(prepared['visibility_certification_path'])
        if not visibility['certified']:
            visibility=verify_access(case,state,read(prepared['visibility_path']),visibility,folder/'access_review')
        save(folder/'accepted_or_rejected_access.json',visibility)
    finally:runtime.cleanup(prepared,DB)
    if not visibility['certified']:
        save(p/'live-access-repair-summary.json',{'status':'access_unresolved','access':visibility});return
    reviewer=resume_recorded(p/'reviewer')
    result=reviewer.ask(dump({'feedback':'Thanks. The previous access findings described the OLD environment. The harness has now installed the compiler’s repaired seed and gathered fresh API evidence below. Judge the same repaired case against this evidence. Compiler notes are non-authoritative construction commentary; any statement claiming an earlier reviewer verdict is not evidence and is excluded from the case/solver packet. No further authoring change is being requested.', 'case':case,'checks':checks,'fresh_access':visibility,'fresh_probes':read(prepared['visibility_path'])}))
    save(folder/'review.json',result)
    status={'status':'unrealized','review':result,'local_harness_recovery':True}
    if result['validity']=='pass' and not any(i['kind'] in ('validity','annotation','access') for i in result['issues']):
        save(p/'case-before-live-access-repair.json',read(p/'case.json'));save(p/'case.json',case)
        status={'status':'review_pass','quality':result['quality'],'local_harness_recovery':True};save(p/'summary.json',status)
        e=BASE/'execution'/cid;e.rename(BASE/'execution_attempts'/(cid+'-before-live-access-repair'))
        asyncio.run(one(BASE,cid,DB))
    save(p/'live-access-repair-summary.json',status)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);a=p.parse_args()
    for cid in a.ids:
        try:finish(cid);print(cid,'live_access_repair_finished',flush=True)
        except Exception as exc:
            save(BASE/'construction'/cid/'live-access-repair-summary.json',{'status':'error','error':str(exc)})
            print(cid,type(exc).__name__,str(exc),flush=True)
