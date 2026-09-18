"""Pilot two-turn workflow: preserve turn-one history, then request the full report."""
import copy
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

REPO=Path('/home/yusf/PyProj/agent-diff')
sys.path.insert(0,str(REPO/'grounding/oracle_bedrock'))
from run import invoke_and_record, repair_saved_run, save

root=Path(__file__).parent
number=sys.argv[1]
first=root/f'two-turn-{number}-applicability'
final=root/f'two-turn-{number}'
cmd=[sys.executable,str(REPO/'grounding/oracle_bedrock/run.py'),
     '--inputs','/tmp/cc-oracle-v3-slack98-9nk6u16v',
     '--instructions',str(root/'two-turn-instructions.md'),
     '--schema',str(REPO/'docs/for eval/oracle-assessment.schema.json'),
     '--instruction-placement','after-evidence','--effort','medium',
     '--focus','applicability','--out',str(first)]
subprocess.run(cmd,check=False)
previous=json.loads((first/'summary.json').read_text())
if previous.get('status') != 'returned' or previous.get('stop_reason') != 'end_turn':
    raise SystemExit('First turn did not complete; no continuation sent')
body=json.loads((first/'request.json').read_text())
response=json.loads((first/'response.json').read_text())
schema=json.loads((first/'supplied_schema.json').read_text())
followup=('Now assess execution and grounding, account for the net changes and user-facing output, '
          'and return the complete full assessment. Use the applicability assessment from the preceding turn. '
          'The applicability-only output restriction applied to that turn only; for this turn use the original full-report instructions '
          'and the full schema below.\n\nOutput schema:\n'+json.dumps(schema,separators=(',',':')))
body['messages'].extend([{'role':'assistant','content':copy.deepcopy(response['content'])},
                         {'role':'user','content':[{'type':'text','text':followup}]}])
final.mkdir(exist_ok=False)
for name in ('packet.txt','instructions.md','supplied_schema.json','manifest.json'):
    shutil.copyfile(first/name,final/name)
shutil.copytree(first/'sources',final/'sources')
save(final/'schema.json',schema)
save(final/'request.json',body)
(final/'followup.txt').write_text(followup+'\n')
sources={p.stem:json.loads(p.read_text()) for p in (final/'sources').glob('*.json')}
manifest=json.loads((first/'manifest.json').read_text())
keys=('test_id','run_id','model','region','effort','max_tokens','native_schema','instruction_placement',
      'instructions_sha256','adapter_sha256','packet_characters','cost_usd','cost_note','runner_sha256','validator_sha256')
summary={k:previous[k] for k in keys}
summary.update(focus='full',workflow_variant='two-turn',workflow_turn=2,
               started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               output_directory=str(final),parent_output_directory=str(first),
               request_sha256=hashlib.sha256(json.dumps(body).encode()).hexdigest(),
               parent_response_sha256=hashlib.sha256((first/'response.json').read_bytes()).hexdigest(),
               workflow_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
code=invoke_and_record(body,final,summary,schema,sources,manifest)
result=json.loads((final/'summary.json').read_text())
if result['status']=='returned' and result.get('validation_errors'):
    code=repair_saved_run(final,final.with_name(final.name+'-repair-1'))
raise SystemExit(code)
