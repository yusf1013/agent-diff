"""One bounded patch-only continuation after redundant card extraction was removed."""
import argparse,asyncio,copy
from grounding.common.bedrock import save
from grounding.archive.slack_campaign.generate import ROOT,read,dump
from grounding.archive.slack_campaign.recover_construction import resume_recorded
from grounding.archive.slack_campaign.workflow import assemble,check,PROMPTS
from grounding.archive.slack_campaign.execute import one

BASE=ROOT/'grounding/runs/slack_campaign/campaign_02'
def repair(cid):
    p=BASE/'construction'/cid
    if (p/'patch-repair-summary.json').exists():return
    save(p/'summary-before-patch-repair.json',read(p/'summary.json'))
    a=read(p/'assignment.json');a['preserve_source_cards']=True;save(p/'assignment.json',a)
    design=copy.deepcopy(read(p/'design.json'));design['obligations']=design['obligations'][:1]
    design['task_spec']=a['source_context']['task_spec']
    compiler=resume_recorded(p/'compiler');reviewer=resume_recorded(p/'reviewer')
    compiled=compiler.ask(dump({'feedback':'The prior environment-only mutation did not produce a usable seed patch. One final compilation attempt: implement the existing writer design by adding at least one realistic, API-visible near-miss record. An unchanged seed is invalid. Preserve the source prompt and every original intended referent. All source cards and task specifications are now copied mechanically: do not extract or bind additional obligations. Exactly one focal selector and negative_referents are needed; bindings may be empty because positive identities come from the source card. Return the ordinary compilation JSON with seed_edits. Do not use owners as negative examples for an ordinary admins request, or use ambiguous semantic exclusions. No solver outcomes are supplied.', 'design':design,'original_cards':a['source_context']['cards']}))
    save(p/'patch-repair-compiled.json',compiled)
    try:case=assemble(a,design,compiled);checks=check(case,a,design,compiled)
    except Exception as exc:case=None;checks={'errors':[str(exc)]}
    save(p/'patch-repair-checks.json',checks)
    status={'status':'unrealized','bounded_patch_repair':True,'errors':checks['errors']}
    if not checks['errors']:
        review=reviewer.ask(dump({'stage':'Final patch-only mutation review. Existing source cards/task lines are preserved mechanically. Check the newly added near-miss changes do not change ANY intended reference and are meaningful, ordinary and accessible. No fresh obligation extraction is requested.', 'instructions':(PROMPTS/'reviewer.md').read_text(),'assignment':a,'design':design,'case':case,'compiled':compiled,'checks':checks}))
        save(p/'patch-repair-review.json',review);status['review']=review
        if review['validity']=='pass' and not any(i['kind'] in ('validity','annotation','access') for i in review['issues']):
            save(p/'case-before-patch-repair.json',read(p/'case.json')) if (p/'case.json').exists() else None
            save(p/'case.json',case);save(p/'design.json',design)
            status={'status':'review_pass','quality':review['quality'],'bounded_patch_repair':True,'source_cards_preserved':True}
    save(p/'summary.json',status);save(p/'patch-repair-summary.json',status)
    if status['status']=='review_pass':
        e=BASE/'execution'/cid
        if e.exists():e.rename(BASE/'execution_attempts'/(cid+'-before-patch-repair'))
        asyncio.run(one(BASE,cid,'postgresql://postgres@127.0.0.1:15432/agentdiff_campaign'))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);a=p.parse_args()
    for cid in a.ids:
        try:repair(cid);print(cid,'patch_repair_finished',flush=True)
        except Exception as exc:
            status={'status':'error','bounded_patch_repair':True,'error':f'{type(exc).__name__}: {exc}'}
            save(BASE/'construction'/cid/'patch-repair-summary.json',status)
            save(BASE/'construction'/cid/'summary.json',status)
            print(cid,status,flush=True)
