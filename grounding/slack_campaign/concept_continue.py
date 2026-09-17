"""Recorded development continuation after a diagnosed checker/instruction defect.

Recheck a saved compilation without regenerating it, or continue the original
compiler conversation with supplied feedback. Original outcomes remain intact.
"""
import argparse
import asyncio
import hashlib
from pathlib import Path

from .bedrock import Conversation, save
from .concept_batch import execute
from .concept_compile import check_compilation, selector_is_valid, system_prompt
from .generate import ROOT, read, dump


def continue_compilation(source, out, feedback, candidate=None):
    out.mkdir(parents=True, exist_ok=False)
    packet = read(source/'input.json')
    if hashlib.sha256((ROOT/packet['source']).read_bytes()).hexdigest() != packet['source_sha256']:
        raise ValueError('Writer source changed')
    (out/'feedback.txt').write_text(feedback+'\n')
    save(out/'provenance.json', {'original': str(source), 'candidate': candidate,
        'development_intervention': True, 'writer_changed': False,
        'reason': feedback, 'original_outcome': read(source/'summary.json')})
    compiler = Conversation.resume(source/'compiler')
    lock = read(source/'locked_selector.json') if (source/'locked_selector.json').exists() else None
    message = feedback
    result = {'status': 'running'}
    try:
        while candidate is not None or compiler.turn < 3:
            if candidate is not None:
                compiled = read(source/f'compiled-{candidate}.json')
                candidate = None
            else:
                compiled = compiler.ask(message)
            label = compiler.turn
            save(out/f'compiled-{label}.json', compiled)
            if lock is None and isinstance(compiled,dict) and selector_is_valid(compiled.get('selector'),compiled.get('seed')):
                lock=compiled['selector']; save(out/'locked_selector.json',lock)
            case, checks = check_compilation(packet, compiled, lock)
            save(out/f'checks-{label}.json',checks)
            if checks['errors']:
                result={'status':'design_conflict' if checks.get('design_defect') else 'mechanical_failure','errors':checks['errors']}
                if checks.get('design_defect'): return result
                message='Thanks. Validation failed: '+dump(checks['errors'])+'. Correct only compilation defects. Keep the sketch and locked selector unchanged. Return complete JSON.'
                continue
            reviewer=Conversation(out/f'review-{label}'/'reviewer',system_prompt(True),cache_system=True,max_tokens=5000)
            review=reviewer.ask(dump({'source':packet,'compilation':compiled,'case':case,'mechanical_checks':checks}))
            save(out/f'review-{label}.json',review)
            issues=review.get('issues')
            if not isinstance(issues,list) or any(not isinstance(i,dict) or i.get('kind') not in ('validity','quality') or i.get('origin') not in ('design','compilation','selector') for i in issues):
                result={'status':'review_unresolved','review':review}; return result
            failures=[i for i in issues if i['kind']=='validity']
            if review.get('validity')=='pass' and not failures:
                save(out/'case.json',case)
                result={'status':'review_pass','quality':review.get('quality'),'development_intervention':True,
                        'computed_matches':checks['computed_matches']}; return result
            result={'status':'review_unresolved','review':review}
            if not failures or any(i['origin']!='compilation' for i in failures): return result
            message='Thanks. Review found these compilation defects: '+dump(failures)+'. Make minimal repairs; preserve the story and locked selector. Return complete JSON.'
        return result
    except Exception as exc:
        result={'status':'error','error':f'{type(exc).__name__}: {exc}'}
        raise
    finally:
        save(out/'summary.json',result)


async def main(args):
    source=args.folder/'construction'/args.case
    out=source/'continuation-01'
    result=await asyncio.to_thread(continue_compilation,source,out,args.feedback.read_text(),args.candidate)
    result.update(case_id=args.case,continuation=str(out))
    def update(value):
        save(args.folder/'continuation_statuses'/f'{args.case}.json',value)
        print(dump(value),flush=True)
    update(result)
    if result['status']=='review_pass':
        result=await execute(out/'case.json',args.folder/'execution'/args.case,
            'postgresql://postgres@127.0.0.1:15432/agentdiff_campaign','http://127.0.0.1:18000',update)
        update(result)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--folder',type=Path,required=True);p.add_argument('--case',required=True)
    p.add_argument('--feedback',type=Path,required=True);p.add_argument('--candidate',type=int)
    args=p.parse_args();args.folder=args.folder.resolve()
    asyncio.run(main(args))
