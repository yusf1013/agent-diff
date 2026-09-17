"""One exact-request retry when a native authoring call returned no response."""
import argparse,copy
from .generate import ROOT,read
from .bedrock import save,Conversation
from .salvage_recorded import salvage

BASE=ROOT/'experiments/slack_campaign/campaign_02/construction'
def retry(cid,stage):
    p=BASE/cid;folder=p/stage;marker=p/(stage+'-transport-retry.json')
    if marker.exists():return
    last=sorted(folder.glob('turn-*/request.json'))[-1].parent
    meta=read(last/'summary.json')
    if (last/'response.json').exists() or meta.get('status')!='error':raise ValueError('Only an unreturned failed request can be retried')
    body=read(last/'request.json');message=body['messages'][-1]
    if message['role']!='user' or len(message['content'])!=1 or message['content'][0]['type']!='text':raise ValueError('Unexpected message shape; do not reconstruct')
    obj=Conversation.__new__(Conversation);obj.folder=folder;obj.model=meta['model'];obj.region=meta['region'];obj.turn=int(last.name.split('-')[-1]);obj.body=copy.deepcopy(body);obj.body['messages'].pop()
    save(marker,{'status':'retrying','source_request':str(last/'request.json'),'policy':'Same native request, no response to fabricate, no semantic feedback.'})
    try:
        obj.ask(message['content'][0]['text'])
    except Exception as exc:
        save(marker,{'status':'retry_failed','source_request':str(last/'request.json'),'retried_request':str(folder/f'turn-{obj.turn:02d}'/'request.json'),'error':str(exc)})
        raise
    actual=read(folder/f'turn-{obj.turn:02d}'/'request.json')
    if actual!=body:raise AssertionError('Technical retry changed the request')
    save(marker,{'status':'returned','source_request':str(last/'request.json'),'retried_request':str(folder/f'turn-{obj.turn:02d}'/'request.json'),'identical_body':True})
    salvage(cid)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--id',required=True);p.add_argument('--stage',choices=['writer','compiler','reviewer'],required=True);a=p.parse_args();retry(a.id,a.stage)
