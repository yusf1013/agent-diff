"""Explicit development feedback through the existing native conversations."""
from concurrent.futures import ThreadPoolExecutor
from grounding.common.bedrock import Conversation, save
from grounding.archive.slack_campaign.generate import ROOT, read, dump
from grounding.archive.slack_campaign.workflow import PROMPTS, source_context, assemble, check, check_design
from grounding.generation.selection import SELECTOR_GUIDE

FEEDBACK={
 'G-R001':'The assigned route is Conversation→Workspace. The present request identifies a channel by topic inside one already fixed workspace, so the workspace is incidental shared context. Revise the design so the workspace relationship genuinely distinguishes candidate channels. Prefer open-ended discovery; if this truly cannot be done through supported discovery, explicitly declare the minimal supplied-scope exception and reason. Preserve short natural wording and a consequential action or meaningful question. The caller needs to identify via workspace, not simply within a fixed workspace.',
 'G-R073':'The prompt gives the full unique name Robert Walsh, with admin status as an asserted background fact. It does not need the membership role to distinguish the intended author. Make the role an actual identifying condition, e.g. a partially shared name distinguished by the admin condition, rather than telling the solver the resolved person. Use ordinary wording; the specific example is not mandatory.',
 'G-R146':'Mechanical formatting feedback is authoritative here. written_attributes is ONLY bare real source fields, for example ["messages.message_text", "messages.channel_id"]. It must not contain assignments, descriptions, literal values, or the authentication-supplied actor field. Earlier reviewer suggestions demanding assignments/literals were erroneous. Keep the prompt and semantic design unchanged; fix only this metadata.'}

def run(cid):
    folder=ROOT/'grounding/runs/slack_campaign/campaign_02/construction'/cid
    assignment=read(folder/'assignment.json');design=read(folder/'design.json')
    save(folder/'development-before.json',{'design':design,'summary':read(folder/'summary.json')})
    if cid in FEEDBACK:
        save(folder/'development-feedback.json',{'provenance':'manual Codex calibration, not automatic production review','feedback':FEEDBACK[cid]})
        writer=Conversation.resume(folder/'writer')
        design=writer.ask('Development review: '+FEEDBACK[cid]+' Return the complete revised design JSON.')
        save(folder/'design.json',design)
    errors=check_design(design,assignment)
    if errors:
        save(folder/'development-summary.json',{'status':'unrealized','errors':errors});return
    compiler_folder=folder/'compiler'
    compiler=Conversation.resume(compiler_folder) if compiler_folder.exists() else Conversation(compiler_folder,(PROMPTS/'compiler.md').read_text(),max_tokens=20000)
    compiled=compiler.ask(dump({'instruction':(PROMPTS/'compiler.md').read_text(),
          'note':'Continuation after development fixes. Compiler now supplies negative_referents as root handles. Negatives can violate any requested condition, including scope. Return complete compilation JSON.',
          'assignment':assignment,'design':design,'base_seed':read(ROOT/'examples/slack/seeds/slack_bench_v2.json'),
          'domain':source_context(),'selector_syntax':SELECTOR_GUIDE}))
    reviewer=Conversation.resume(folder/'reviewer')
    for attempt in range(1,3):
        save(folder/f'development-compiled-{attempt}.json',compiled)
        try:
            case=assemble(assignment,design,compiled);checks=check(case,assignment,design,compiled)
        except Exception as exc:
            checks={'errors':[str(exc)]};case=None
        save(folder/f'development-checks-{attempt}.json',checks)
        if checks['errors']:
            if attempt==1:
                compiled=compiler.ask('Thanks. Validation failed: '+dump(checks)+'. Please make minimal required changes and return complete compilation JSON.');continue
            save(folder/'development-summary.json',{'status':'unrealized','checks':checks});return
        review=reviewer.ask(dump({'instruction':(PROMPTS/'reviewer.md').read_text(),'note':'Field names, not assignment expressions, belong in written_attributes. Earlier contrary suggestions are withdrawn. Check semantic validity and actual full-route selection, not mere occurrence of entity names.',
                                  'assignment':assignment,'design':design,'case':case,'compiled':compiled,'checks':checks}))
        save(folder/f'development-review-{attempt}.json',review)
        if review['validity']=='pass' and not any(x['kind'] in ('validity','annotation','access') for x in review['issues']):
            save(folder/'case.json',case)
            result={'status':'review_pass','quality':review['quality'],'manual_development_feedback':cid in FEEDBACK}
            save(folder/'summary.json',result);save(folder/'development-summary.json',result);return
        if attempt==1:
            compiled=compiler.ask('Review found: '+dump(review)+'. Repair concrete compilation issues only, preserving the design. Return complete compilation JSON.');continue
        save(folder/'development-summary.json',{'status':'unrealized','review':review})

if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:
        list(pool.map(run,['G-R001','G-R073','G-R146','G-R089','G-R024']))
