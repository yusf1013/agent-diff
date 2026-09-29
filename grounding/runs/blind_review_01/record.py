"""Append explicitly authored blind labels; never infer labels from evidence or scores."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE / 'labels.jsonl'
assert not (HERE / 'labels.sha256').exists(), 'Labels already frozen'
existing = [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []
known = {r['blind_id'] for r in json.loads((HERE / 'manifest.json').read_text())['sample']}
seen = {r['blind_id'] for r in existing}
rows = json.load(sys.stdin)
for row in rows:
    bid = row['blind_id']
    assert bid in known and bid not in seen, bid
    seen.add(bid)
    assert row['outcome'] in {'correct','correct_absent','incorrect','presented','false_absence','incomplete','artifact','not_established'}
    assert row.get('note') and row.get('evidence') and row.get('confidence')
    row.setdefault('acted_on', [])
    row.setdefault('exposed', [])
    row.setdefault('mechanism', 'none')
    row.setdefault('artifact_reason', '')
    row.setdefault('review_status', 'labelled')
    row['reviewer'] = 'Codex independent AI reference review, blind to saved scores'
with path.open('a') as f:
    for row in rows:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
print(f'{len(rows)} authored labels appended; {len(seen)}/200 recorded')
