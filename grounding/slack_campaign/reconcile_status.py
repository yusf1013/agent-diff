"""Reconcile terminal development markers after all relevant workers have stopped."""
import argparse,re
from .generate import ROOT,read
from .bedrock import save
BASE=ROOT/'experiments/slack_campaign/campaign_02'
def run():
    changed=[]
    for folder in sorted((BASE/'construction').iterdir()):
        if not (folder/'summary.json').exists():continue
        old=read(folder/'summary.json')
        if old['status'] not in ('manual_revision_required','error'):continue
        # Never finalize a live model request.
        if any(read(p).get('status')=='running' for p in folder.glob('*/turn-*/summary.json')):continue
        marker=folder/'recovery-summary.json'
        if marker.exists() and read(marker).get('status') in ('unrealized','error'):
            new=read(marker)
        elif old['status']=='manual_revision_required':
            turns=sorted(folder.glob('*/turn-*/summary.json'),key=lambda p:p.stat().st_mtime)
            last=read(turns[-1]) if turns else {}
            if last.get('status') not in ('incomplete','error'):continue
            new={'status':'error','bounded_revision_exhausted':True,'error':last.get('error',last.get('parse_error','Incomplete authoring response')),'terminal_evidence':str(turns[-1].relative_to(BASE))}
        else:continue
        if new==old:continue
        save(folder/'summary-before-terminal-reconciliation.json',old)
        save(folder/'summary.json',new);changed.append(folder.name)
    save(BASE/'terminal_reconciliation.json',{'cases':changed,'note':'Only completed failure markers/local incomplete calls reconciled; no model output or case content changed.'});print(changed)
if __name__=='__main__':run()
