"""Card-free direct judge on the same prepared baseline evidence."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from .bedrock import Conversation, save
from .generate import ROOT, read, dump
from .workflow import PROMPTS

def validate(result,packet):
    errors=[]
    if result.get('test_id')!=packet['prompt']['test_id']:errors.append('test_id must match')
    if result.get('run_id')!=packet['prompt']['run_id']:errors.append('run_id must match')
    for field in ('violations','unresolved'):
        if not isinstance(result.get(field),list):errors.append(field+' must be an array')
    for i,v in enumerate(result.get('violations',[])):
        for e in v.get('evidence',[]):
            try:
                doc=packet[e['source']]
                for part in e['location'].split('/')[1:]:
                    key=part.replace('~1','/').replace('~0','~')
                    doc=doc[int(key)] if isinstance(doc,list) else doc[key]
            except (KeyError,ValueError,TypeError,IndexError):
                errors.append(f'violations[{i}] evidence locator does not resolve within source: {e}')
    return errors


def judge(inputs,out):
    cid=inputs.name
    if (out/cid/'result.json').exists():return cid,'existing'
    # Deliberately exclude cards, task_spec, provenance, native assertions/results.
    mapping={'prompt':'task.json','initial_state':'initial_state.json','diff':'recorded_diff.json',
             'response':'response.json','trajectory':'trajectory.json'}
    packet={name:read(inputs/file) for name,file in mapping.items()}
    if (inputs/'final_state.json').exists():packet['final_state']=read(inputs/'final_state.json')
    packet['api_docs']={p.name:read(p) for p in sorted((inputs/'api_docs').glob('*.json'))}
    agent=Conversation(out/cid/'direct_judge',(PROMPTS/'direct_judge.md').read_text(),max_tokens=16000)
    save(out/cid/'input.json',packet)
    try:
        result=agent.ask(dump(packet))
        errors=validate(result,packet)
        if errors:
            result=agent.ask('Thanks. Validation failed: '+dump(errors)+'. Make minimal required changes; return the complete JSON.')
        save(out/cid/'validation.json',{'errors':validate(result,packet)})
        save(out/cid/'result.json',result)
        return cid,'returned'
    except Exception as exc:
        save(out/cid/'error.json',{'error':str(exc)})
        return cid,'error'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--concurrency',type=int,default=9);a=p.parse_args()
    base=ROOT/'experiments/slack_campaign/campaign_02/baseline'
    with ThreadPoolExecutor(max_workers=a.concurrency) as pool:
        fs=[pool.submit(judge,x,base/'direct') for x in sorted((base/'inputs').iterdir()) if x.is_dir()]
        for f in as_completed(fs):print(f.result(),flush=True)
