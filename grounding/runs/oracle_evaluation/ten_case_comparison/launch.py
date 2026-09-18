import concurrent.futures
import hashlib
import json
from pathlib import Path
import random
import subprocess
import time

ROOT=Path(__file__).parent
REPO=Path('/home/yusf/PyProj/agent-diff')
tests=[x['test_id'] for x in json.loads((ROOT/'selection.json').read_text())]
jobs=[(tid,v,n) for tid in tests for v in ('ordered','separated') for n in range(1,6)]
random.Random(20260915).shuffle(jobs)
(ROOT/'launch-manifest.json').write_text(json.dumps({'concurrency':15,'shuffle_seed':20260915,'jobs':jobs,'reference_sha256':hashlib.sha256((ROOT/'reference/expected.json').read_bytes()).hexdigest()},indent=2)+'\n')
def run(job):
 tid,v,n=job;name=f'{tid}-{v}-{n}';start=time.monotonic()
 cmd=['python',str(REPO/'grounding/oracle_bedrock/run.py'),'--inputs',str(ROOT/'inputs'/tid),'--instructions',str(ROOT/f'{v}-instructions.md'),'--schema',str(REPO/'docs/for eval/oracle-assessment.schema.json'),'--instruction-placement','after-evidence','--effort','medium','--repair-on-validation-failure','--out',str(ROOT/'runs'/name)]
 with (ROOT/'runs'/f'{name}.log').open('w') as log:
  code=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,cwd=REPO).returncode
 return {'name':name,'exit_code':code,'wall_seconds':round(time.monotonic()-start,3)}
with concurrent.futures.ThreadPoolExecutor(max_workers=15) as pool:
 futures=[pool.submit(run,j) for j in jobs]
 for i,f in enumerate(concurrent.futures.as_completed(futures),1):
  r=f.result()
  with (ROOT/'completion.jsonl').open('a') as out:out.write(json.dumps(r)+'\n')
  print(f'{i}/100 '+json.dumps(r),flush=True)
