"""Account every recorded invocation once, including failed/repair calls."""
from collections import defaultdict
import json
from pathlib import Path
from grounding.common.io import ROOT, read
from grounding.common.bedrock import save
RATES={'input_tokens':3.0,'output_tokens':15.0,'cache_creation_input_tokens':3.75,'cache_read_input_tokens':0.30}

def report(folder):
    calls=[]
    for path in sorted(folder.rglob('summary.json')):
        obj=read(path)
        if 'usage' not in obj and not ('model' in obj and (path.parent/'request.json').exists()):continue
        rel=str(path.relative_to(folder))
        parts=path.parts
        stage=next((s for s in ('writer','compiler','reviewer','direct_judge','access_review') if s in parts),'evaluator')
        calls.append({'source':rel,'stage':stage,'status':obj.get('status'),'usage':obj.get('usage'),
                      'native_cost_usd':obj.get('cost_usd'),'elapsed_seconds':obj.get('elapsed_seconds')})
    for path in sorted(folder.glob('**/solver/*.json')):
        obj=read(path)
        if not isinstance(obj,dict) or 'steps' not in obj or 'test_id' not in obj:continue
        for step in obj['steps']:
            calls.append({'source':str(path.relative_to(folder)),'stage':'solver',
                          'turn':step['turn'],'usage':step.get('usage'),'status':'returned'})
    totals=defaultdict(int);buckets={};unknown=[]
    for row in calls:
        usage=row.get('usage')
        if usage is None:unknown.append(row['source']);continue
        bucket=buckets.setdefault(row['stage'],{k:0 for k in RATES})
        for key in RATES:
            n=usage.get(key,0) or 0
            totals[key]+=n;bucket[key]+=n
    output={'invocations':len(calls),'usage_unavailable':unknown,'tokens':dict(totals),'by_stage':buckets,
            'estimated_cost_usd':sum(totals[k]*r/1e6 for k,r in RATES.items()),
            'historical_rates_usd_per_million':RATES,
            'cost_note':'Own historical-rate estimate from native usage, not a Bedrock billed dollar amount. Unknown and still-running usage is not treated as free.'}
    save(folder/'usage_ledger.json',calls);save(folder/'usage_summary.json',output)
    print(json.dumps(output,indent=2))
    return output
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path, help='Run folder whose invocation records should be counted')
    report(parser.parse_args().folder)
