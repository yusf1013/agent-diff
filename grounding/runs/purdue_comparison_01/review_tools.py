"""Read saved evidence for manual review. No verdict generation or model calls."""
from pathlib import Path
import argparse
import json

HERE = Path(__file__).resolve().parent


def packet(model, cid):
    case = json.loads((HERE/'dataset/cases'/(cid+'.json')).read_text())
    attempts = sorted((HERE/'runs'/model/cid).glob('attempt-*/execution_summary.json'))
    if not attempts:
        raise ValueError('Not started: '+model+'/'+cid)
    p=attempts[-1].parent
    summary=json.loads(attempts[-1].read_text())
    if summary['status'] != 'completed':
        raise ValueError('Not completed: '+model+'/'+cid+' '+summary['status'])
    record=json.loads((p/'solver'/(cid+'.json')).read_text())
    print('\nCASE',model,cid,'mode='+case['private']['mode'])
    print('PROMPT',case['prompt'])
    print('GROUNDING',json.dumps(case['cards'],ensure_ascii=False))
    print('INITIAL SEED',json.dumps(case['seed'],ensure_ascii=False))
    print('ROW BINDINGS',json.dumps(case['private']['row_bindings'],ensure_ascii=False))
    print('EXPECTED',json.dumps(case['private']['reference_outcome'],ensure_ascii=False))
    for step in record['steps']:
        print('\nTURN',step['turn'])
        for block in step['response']['content']:
            if block['type']=='text':
                print('ASSISTANT',block['text'])
        if 'action' in step:
            print('ACTUAL COMMAND',step['action'])
        if 'observation' in step:
            print('ACTUAL OBSERVATION',json.dumps(step['observation'],ensure_ascii=False))
    print('\nFINAL',record.get('final','<NO RECORDED FINAL>'))
    print('TERMINATION',record.get('termination'),record.get('error'))
    print('NET DIFF',json.dumps(record.get('evaluation',{}).get('diff'),ensure_ascii=False))
    print('EVIDENCE DIRECTORY',p)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model',choices=['qwen36','sonnet5','haiku45'])
    parser.add_argument('cases',nargs='+')
    args=parser.parse_args()
    for cid in args.cases:
        packet(args.model,cid)
