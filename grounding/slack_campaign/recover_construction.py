"""One bounded recovery after diagnosed construction/transport defects.

Preserves all native assistant responses and every earlier artifact. This is a
second development pass, not a fresh best-of-N authoring sample.
"""
import copy
from concurrent.futures import ThreadPoolExecutor
import argparse
from .bedrock import Conversation,save
from .generate import ROOT,read,dump
from .workflow import PROMPTS,source_context,assemble,check,check_design
from .selection import SELECTOR_GUIDE
from .route_contract import build as build_route_contract

def resume_recorded(folder):
    """Recover the actual native history even after an unanswered transport call."""
    requests=sorted(folder.glob('turn-*/request.json'))
    latest=requests[-1].parent;meta=read(latest/'summary.json')
    obj=Conversation.__new__(Conversation);obj.folder=folder
    obj.body=read(latest/'request.json');obj.model=meta['model'];obj.region=meta['region']
    obj.turn=max(int(p.parent.name.split('-')[-1]) for p in requests)
    response=latest/'response.json'
    if response.exists():
        raw=read(response)
        # Preserve provider-returned blocks including native refusal text; no
        # artificial assistant answer is supplied. A new user clarification follows.
        obj.body['messages'].append({'role':'assistant','content':copy.deepcopy(raw.get('content',[]))})
    obj.body['max_tokens'] = max(obj.body.get('max_tokens', 0), 24000)
    return obj


def finish(folder, result):
    save(folder/'recovery-summary.json',result)
    save(folder/'summary.json',result)


def recover(cid):
    folder=ROOT/'experiments/slack_campaign/campaign_02/construction'/cid
    if (folder/'recovery-summary.json').exists():return
    old=read(folder/'summary.json')
    if old['status']=='review_pass':return
    save(folder/'summary-before-recovery.json',old)
    a=read(folder/'assignment.json')
    writer=resume_recorded(folder/'writer')
    feedback='Continue this same design. The attached current instructions clarify serialization and the task; earlier outputs remain recorded. Use native table names consistently; absence still has the assigned referent table and an empty target set. For a collection request with one seeded match use multiple, not single, and do not manufacture an extra positive in an environment-only mutation. Include all computation/written metadata required by task_type. A mutation uses exactly the same sketch JSON contract: describe the existing positives and proposed negative additions; the compiler, not you, writes the actual seed patch. The source prompt and intended referents remain fixed. Do not change the assignment to fit a draft. Return the complete corrected design JSON, or a concrete unrealized_reason if necessary.'
    save(folder/'recovery-feedback.json',{'provenance':'General development corrections, no solver output or ground-truth labels','feedback':feedback})
    design=writer.ask(dump({'feedback':feedback,'current_writer_instructions':(PROMPTS/'writer.md').read_text(),
                            'assignment':a,'route_contract':build_route_contract(a['route_nodes']),'prior_construction_failure':old}))
    if (folder/'design.json').exists():save(folder/'design-before-recovery.json',read(folder/'design.json'))
    save(folder/'design.json',design)
    if design.get('unrealized_reason'):
        finish(folder,{'status':'unrealized','reason':design['unrealized_reason']});return
    errors=check_design(design,a)
    if errors:
        design=writer.ask('Thanks. Mechanical validation failed: '+dump(errors)+'. Fix only required fields; keep selection semantics and assignment fixed. Return complete design JSON.')
        save(folder/'design.json',design);errors=check_design(design,a)
    if errors:
        finish(folder,{'status':'unrealized','errors':errors});return
    cf=folder/'compiler'
    compiler=resume_recorded(cf) if cf.exists() and list(cf.glob('turn-*/request.json')) else Conversation(cf,(PROMPTS/'compiler.md').read_text(),max_tokens=20000)
    compiled=compiler.ask(dump({'stage':'Explicit writer revision: the supplied current design supersedes earlier defective designs. Lock this current prompt during compilation.','instruction':(PROMPTS/'compiler.md').read_text(),'assignment':a,'design':design,
        'base_seed':read(ROOT/'examples/slack/seeds/slack_bench_v2.json'),'domain':source_context(),'selector_syntax':SELECTOR_GUIDE}))
    rf=folder/'reviewer'
    if rf.exists() and not list(rf.glob('turn-*/request.json')):
        rf.rename(folder/'reviewer-before-initial-recovery')
    reviewer=resume_recorded(rf) if rf.exists() and list(rf.glob('turn-*/request.json')) else Conversation(rf,(PROMPTS/'reviewer.md').read_text(),max_tokens=10000)
    for n in range(1,3):
        save(folder/f'recovery-compiled-{n}.json',compiled)
        try:case=assemble(a,design,compiled);checked=check(case,a,design,compiled)
        except Exception as exc:case=None;checked={'errors':[str(exc)]}
        save(folder/f'recovery-checks-{n}.json',checked)
        if checked['errors']:
            if n==1:
                compiled=compiler.ask('Thanks. Validation failed: '+dump(checked)+'. Make minimal compilation fixes without changing the design. Return full compilation JSON.');continue
            finish(folder,{'status':'unrealized','errors':checked['errors']});return
        review=reviewer.ask(dump({'current_review_instructions':(PROMPTS/'reviewer.md').read_text(),'assignment':a,'design':design,'case':case,'compiled':compiled,'checks':checked}))
        save(folder/f'recovery-review-{n}.json',review)
        if review['validity']=='pass' and not any(x['kind'] in ('validity','access','annotation') for x in review['issues']):
            save(folder/'case.json',case)
            status={'status':'review_pass','quality':review['quality'],'development_recovery':True}
            save(folder/'summary.json',status);save(folder/'recovery-summary.json',status);return
        if n==1:compiled=compiler.ask('Independent review found: '+dump(review)+'. Repair concrete compilation defects, keeping the design fixed. Return complete compilation JSON.')
    finish(folder,{'status':'unrealized','review':review})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);p.add_argument('--concurrency',type=int,default=1);args=p.parse_args()
    def safe(cid):
        try:recover(cid);print(cid,'recovery_finished',flush=True)
        except Exception as exc:
            finish(ROOT/'experiments/slack_campaign/campaign_02/construction'/cid, {'status':'error','bounded_recovery_exhausted':True,'error':f'{type(exc).__name__}: {exc}'})
            print(cid,type(exc).__name__,str(exc),flush=True)
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:list(pool.map(safe,args.ids))
