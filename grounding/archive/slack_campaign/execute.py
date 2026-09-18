"""Execute reviewed workflow-v2 cases using the unchanged baseline solver."""
import argparse
import asyncio
import sys
from pathlib import Path
from grounding.integrations.agentdiff import runtime
from grounding.common.bedrock import save
from grounding.archive.slack_campaign.generate import ROOT,read
from grounding.generation.validate import validate_case
from grounding.archive.slack_campaign.verify_access import verify_access

async def one(folder,cid,database_url):
    source=folder/'construction'/cid;out=folder/'execution'/cid
    if (out/'summary.json').exists():return read(out/'summary.json')
    if not (source/'summary.json').exists() or read(source/'summary.json')['status']!='review_pass':
        return {'case_id':cid,'status':'not_reviewed'}
    out.mkdir(parents=True)
    status={'case_id':cid,'status':'preflight'};save(out/'summary.json',status)
    prepared=None
    try:
        case=read(source/'case.json')
        check=validate_case(case);save(out/'source_validation.json',check)
        if check['errors']:raise ValueError(str(check['errors']))
        prepared=await asyncio.to_thread(runtime.prepare,case,out/'preflight',database_url)
        state=read(prepared['initial_state_path'])
        check=validate_case({**case,'seed':state});save(out/'installed_validation.json',check)
        if check['errors']:raise ValueError(str(check['errors']))
        visibility=read(prepared['visibility_certification_path'])
        if not visibility['certified']:
            visibility=await asyncio.to_thread(verify_access,case,state,read(prepared['visibility_path']),visibility,out/'access_review')
            save(out/'visibility_review.json',visibility)
            if visibility['certified']:
                prepared['visibility_certification_path']=str(out/'visibility_review.json')
        if not visibility['certified']:
            status.update(status='access_unresolved',access=visibility)
            return status
        save(out/'accepted_access.json',visibility)
        status['status']='solver_running';save(out/'summary.json',status)
        def installed(original,actual):
            result=validate_case({**original,'seed':actual})
            if result['errors']:raise ValueError(str(result['errors']))
        record=await runtime.run_prepared(case,prepared,out/'solver',database_url,validate_installed=installed)
        prepared=None
        status.update(solver_termination=record.get('termination'),solver_error=record.get('error'))
        if 'evaluation' not in record:raise ValueError('No solver diff recorded')
        status['status']='evaluator_running';save(out/'summary.json',status)
        assessment=out/'assessment'
        cmd=[sys.executable,str(ROOT/'grounding/evaluation/run.py'),'--inputs',str(out/'solver/oracle_input'),
             '--instructions',str(ROOT/'grounding/prompts/evaluator/ordered.md'),
             '--schema',str(ROOT/'grounding/evaluation/oracle-assessment.schema.json'),'--instruction-placement','after-evidence',
             '--repair-on-validation-failure','--out',str(assessment)]
        with (out/'evaluator.log').open('w') as log:
            process=await asyncio.create_subprocess_exec(*cmd,stdout=log,stderr=asyncio.subprocess.STDOUT)
            code=await process.wait()
        repair=out/'assessment-repair-1'
        chosen=repair if (repair/'summary.json').exists() else assessment
        summary=read(chosen/'summary.json')
        status.update(status='completed' if code==0 else 'evaluation_unresolved',evaluator_output=str(chosen),
                      validation_errors=summary.get('validation_errors',[]))
        if (chosen/'assessment.json').exists():
            result=read(chosen/'assessment.json');status['obligations']=result['obligations']
            status['automated_flags']=[k for k,v in result['obligations'].items() if v=='demonstrated_incorrect']
    except Exception as exc:status.update(status='error',error=f'{type(exc).__name__}: {exc}')
    finally:
        if prepared:await asyncio.to_thread(runtime.cleanup,prepared,database_url)
        save(out/'summary.json',status)
        print(cid,status['status'],status.get('error',''),status.get('automated_flags',[]),flush=True)
    return status

async def run(args):
    folder=ROOT/'grounding/runs/slack_campaign/campaign_02'
    semaphore=asyncio.Semaphore(args.concurrency)
    async def wrapped(cid):
        async with semaphore:return await one(folder,cid,args.database_url)
    await asyncio.gather(*(wrapped(cid) for cid in args.ids))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--ids',nargs='+',required=True);p.add_argument('--concurrency',type=int,default=2)
    p.add_argument('--database-url',default='postgresql://postgres@127.0.0.1:15432/agentdiff_campaign')
    asyncio.run(run(p.parse_args()))
