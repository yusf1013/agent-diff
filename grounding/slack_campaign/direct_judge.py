"""Card-free direct judge on the same prepared baseline evidence."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from .bedrock import Conversation, save
from .generate import ROOT, read, dump
from .workflow import PROMPTS

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
        errors=[]
        if result.get('test_id')!=cid:errors.append('test_id must match')
        if result.get('run_id')!=packet['prompt']['run_id']:errors.append('run_id must match')
        if not isinstance(result.get('violations'),list):errors.append('violations must be array')
        if not isinstance(result.get('unresolved'),list):errors.append('unresolved must be array')
        if errors:
            result=agent.ask('Thanks. Validation failed: '+dump(errors)+'. Make minimal required changes; return the complete JSON.')
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
