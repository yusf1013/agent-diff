"""Prepare baseline evidence without consulting ground-truth run labels."""
from pathlib import Path
import json
import sys
from grounding.archive.slack_campaign.generate import ROOT, read
from grounding.common.bedrock import save

def prepare_all(out):
    sys.path.insert(0,str(ROOT/'grounding/evaluation'))
    from prepare import prepare
    summary=read(ROOT/'grounding/runs/slack_baseline/full_slack/summary.json')
    rows=summary['results']
    manifest=[]
    for row in rows:
        run_path=Path(row['artifact'])
        if not run_path.exists():
            run_path=ROOT/str(run_path).split('/agent-diff/')[-1]
        run=read(run_path)
        cid=run['test_id']
        target=out/'inputs'/cid
        if not target.exists():
            prepare(run_path,ROOT/'grounding/domains/slack/analysis/analysis.json',
                    ROOT/'datasets/agent-diff-bench/all_numbered.jsonl',
                    ROOT/'examples/slack/seeds/slack_bench_v2.json',
                    ROOT/'examples/slack/testsuites/slack_docs/slack_api_full_docs.json',target)
        manifest.append({'test_id':cid,'run':str(run_path.relative_to(ROOT)),
                         'native_result':run.get('evaluation',{}).get('result',run.get('evaluation',{}))})
    save(out/'manifest.json',manifest)
    return manifest

if __name__=='__main__':
    prepare_all(ROOT/'grounding/runs/slack_campaign/campaign_02/baseline')
