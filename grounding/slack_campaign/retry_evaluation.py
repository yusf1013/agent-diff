"""One transport-only retry of the identical oracle request; no semantic selection."""
import argparse,datetime,importlib.util,shutil,sys
from .generate import ROOT,read
from .bedrock import save

def retry(cid):
    out=ROOT/'experiments/slack_campaign/campaign_02/execution'/cid
    status=read(out/'summary.json')
    if status['status']!='evaluation_unresolved':return
    parent=__import__('pathlib').Path(status['evaluator_output']);old=read(parent/'summary.json')
    if old.get('status')!='error' or (parent/'response.json').exists():return
    target=out/'assessment-technical-retry-1'
    if target.exists():return
    target.mkdir()
    for name in ['packet.txt','instructions.md','schema.json','supplied_schema.json','manifest.json','request.json']:
        shutil.copyfile(parent/name,target/name)
    shutil.copytree(parent/'sources',target/'sources')
    sys.path.insert(0,str(ROOT/'grounding/oracle_bedrock'))
    spec=importlib.util.spec_from_file_location('recorded_oracle_runner',ROOT/'grounding/oracle_bedrock/run.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
    summary={k:v for k,v in old.items() if k not in ['status','error','elapsed_seconds','usage','validation_errors','stop_reason']}
    summary.update(started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),output_directory=str(target),technical_retry_of=str(parent),usage=None)
    sources={p.stem:read(p) for p in (target/'sources').glob('*.json')}
    code=runner.invoke_and_record(read(target/'request.json'),target,summary,read(target/'schema.json'),sources,read(target/'manifest.json'),300)
    result=read(target/'summary.json');chosen=target
    if result['status']=='returned' and result.get('validation_errors'):
        chosen=target.with_name(target.name+'-repair-1');code=runner.repair_saved_run(target,chosen)
        result=read(chosen/'summary.json')
    status.update(status='completed' if code==0 else 'evaluation_unresolved',evaluator_output=str(chosen),validation_errors=result.get('validation_errors',[]))
    if (chosen/'assessment.json').exists():
        report=read(chosen/'assessment.json');status['obligations']=report['obligations']
        status['automated_flags']=[k for k,v in report['obligations'].items() if v=='demonstrated_incorrect']
    save(out/'summary.json',status)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);a=p.parse_args()
    for cid in a.ids:retry(cid)
