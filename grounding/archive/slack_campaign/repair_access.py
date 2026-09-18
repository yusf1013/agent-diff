"""Bounded compiler continuation after a live access failure; preserve every attempt."""
import argparse
import asyncio
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from grounding.common.bedrock import Conversation,save
from grounding.archive.slack_campaign.generate import ROOT,read,dump
from grounding.archive.slack_campaign.workflow import assemble,check,PROMPTS,source_context
from grounding.archive.slack_campaign.execute import one

def repair(cid):
    base=ROOT/'grounding/runs/slack_campaign/campaign_02';source=base/'construction'/cid;execution=base/'execution'/cid
    if not (execution/'summary.json').exists():return
    prior=read(execution/'summary.json')
    if prior['status']!='access_unresolved' or (source/'access-repair-summary.json').exists():return
    design=read(source/'design.json');assignment=read(source/'assignment.json')
    save(source/'case-before-access-repair.json',read(source/'case.json'))
    compiler=Conversation.resume(source/'compiler');reviewer=Conversation.resume(source/'reviewer')
    feedback={'status':prior['status'],'findings':prior.get('access',{}).get('findings'),
              'errors':prior.get('access',{}).get('errors')}
    compiled=compiler.ask('Live API preflight could not establish the selection from accessible evidence. Repair the environment while keeping the prompt, intended design, route and resolution mode fixed. Actor channel memberships can be added when needed for complete relevant histories. An inaccessible background record must not be claimed as a solver-visible negative; either expose it legitimately or remove it from negative_referents while retaining at least one useful accessible negative and preserving the full seed. Do not assume users.list team_id switches workspaces; it is ignored in this replica. Do not invent capabilities or supply hidden answers in user text. Return complete compilation JSON including seed_edits, bindings, selectors, negative_referents, notes.\n'+dump(feedback))
    for n in range(1,3):
        save(source/f'access-repair-compiled-{n}.json',compiled)
        try:case=assemble(assignment,design,compiled);checked=check(case,assignment,design,compiled)
        except Exception as exc:checked={'errors':[str(exc)]};case=None
        save(source/f'access-repair-checks-{n}.json',checked)
        if checked['errors']:
            if n==1:
                compiled=compiler.ask('Thanks. Validation failed: '+dump(checked)+'. Make minimal required fixes; return complete compilation JSON.');continue
            save(source/'access-repair-summary.json',{'status':'unrealized','errors':checked['errors']});return
        review=reviewer.ask(dump({'stage':'compiled repair after actual live API access failure','instructions':(PROMPTS/'reviewer.md').read_text(),
            'assignment':assignment,'design':design,'compiled':compiled,'case':case,'mechanical_checks':checked,
            'prior_access_failure':feedback,'actual_api_qualifications':source_context()['runtime_qualifications']}))
        save(source/f'access-repair-review-{n}.json',review)
        if review['validity']=='pass' and not any(i['kind'] in ('validity','annotation','access') for i in review['issues']):
            save(source/'case.json',case);save(source/'access-repair-summary.json',{'status':'review_pass','quality':review['quality']})
            archive=base/'execution_attempts'/(cid+'-before-access-repair');archive.parent.mkdir(exist_ok=True)
            execution.rename(archive)
            asyncio.run(one(base,cid,'postgresql://postgres@127.0.0.1:15432/agentdiff_campaign'))
            return
        if n==1:
            compiled=compiler.ask('Review found: '+dump(review)+'. Repair concrete compilation defects without changing the design. Return complete compilation JSON.')
    save(source/'access-repair-summary.json',{'status':'unrealized','review':review})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);p.add_argument('--concurrency',type=int,default=2);a=p.parse_args()
    with ThreadPoolExecutor(max_workers=a.concurrency) as pool:list(pool.map(repair,a.ids))
