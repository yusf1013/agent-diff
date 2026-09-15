"""Build the review index and provenance inventory; never assign semantic labels."""
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = read(ROOT / 'manifest.json')
    review = read(ROOT / 'review_status.json')
    pending = set()
    for item in review['pending']:
        pending.update(item.get('cases', [item.get('case')]))
    checks = read(ROOT / 'validation.json')
    totals = Counter()
    inventory = {}
    rows = []
    for case in manifest['cases']:
        tid = case['test_id']
        report = read(ROOT / 'reports' / f'{tid}.json')
        assert sha(REPO / case['source_run']) == case['source_sha256'], tid
        assert report['run_id'] == case['run_id'], tid
        assert not checks[tid]['errors'], tid
        case['status'] = 'draft_pending_adjudication' if tid in pending else 'manually_reviewed_draft'
        case['report'] = f'reports/{tid}.json'
        counts = Counter(report['obligations'].values())
        totals.update(counts)
        inputs = ROOT / 'inputs' / tid
        for path in sorted(inputs.rglob('*')):
            if path.is_file():
                inventory[str(path.relative_to(ROOT))] = sha(path)
        path = ROOT / case['report']
        inventory[case['report']] = sha(path)
        changes = read(inputs / 'recorded_diff.json')
        count_diff = sum(len(changes.get(kind, [])) for kind in ('inserts', 'updates', 'deletes'))
        n_actions = sum('task_status' in row for row in report['lines'])
        verdicts = '/'.join(str(counts[k]) for k in ('demonstrated_correct', 'demonstrated_incorrect', 'not_established'))
        links = ' · '.join(f'[{label}](inputs/{tid}/{name}.json)' for label, name in (
            ('task', 'task'), ('spec', 'task_spec'), ('cards', 'cards'),
            ('diff', 'recorded_diff'), ('answer', 'response'), ('trajectory', 'trajectory')))
        status = 'Pending clarification' if tid in pending else 'Reviewed draft'
        rows.append(f'| [{tid}](reports/{tid}.json) | {status} | {n_actions} | {verdicts} | {count_diff} | {links} |')
    manifest['status'] = review['status']
    manifest['label_authoring'] = 'Personally authored annotations serialized by author_labels.py; no evaluator-model calls or model-report ingestion.'
    (ROOT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    policy = [
        'grounding/card extraction.md',
        'grounding/oracle_bedrock/prompts/lean.md',
        'docs/for eval/oracle-assessment.schema.json',
        'grounding/oracle_bedrock/prepare.py',
        'grounding/oracle_bedrock/validate.py',
    ]
    provenance = {'algorithm': 'sha256', 'repo_sources': {p: sha(REPO / p) for p in policy}, 'bundle_files': inventory}
    (ROOT / 'content_hashes.json').write_text(json.dumps(provenance, indent=2) + '\n')
    intro = f'''# Slack ground-truth review

**Draft: collaborative adjudication is still open.** These are personally authored assessments of all 59 saved Slack runs (`slack_57`–`slack_115`), not an evaluator-model consensus. Use the per-case JSONs to review the proposed reference answers; do not yet treat the collection as a frozen ground-truth release.

The [manifest](manifest.json) binds each assessment to its saved run and SHA256. [Content hashes](content_hashes.json) bind the prepared inputs, reports, policy, and checker. All 59 reports pass the unchanged [mechanical validator](validation.json); that checks structure, references, and accounting, not semantic correctness.

The drafts contain {sum(totals.values())} overall obligation judgments: {totals['demonstrated_correct']} demonstrated correct, {totals['demonstrated_incorrect']} demonstrated incorrect, and {totals['not_established']} not established. These are judgments of the saved runs, **not** the benchmark's assertion-coverage metrics or a count of all task failures. A correct grounding judgment can coexist with false content, a wrong uncarded destination, or an omitted deliverable; read the associated explanation.

## Review the unresolved judgments first

See [the four clarification topics](adjudication.md). A pending clarification may affect related cases, even where their table row currently says reviewed draft. No onboarding protocol or final accuracy score is issued until those decisions are settled.

## Case index

Click a case for its evaluation JSON. The remaining links open its exact inputs. Evidence `location` values are JSON Pointers within those inputs; response paragraph numbers use the protocol's blank-line split. Paths are relative file links without editor-specific line suffixes.

The C/I/N column counts overall obligation judgments. “Actions” excludes bare markers but includes requested condition checks. “Diff rows” counts supplied insert/update/delete entries, not requested actions or bugs.

| Assessment | Review state | Actions | C/I/N | Diff rows | Evidence |
| --- | --- | ---: | --- | ---: | --- |
'''
    ending = '''
## Authoring and reproducibility

[author_labels.py](author_labels.py) is the manual annotation record. It serializes the authored line judgments and aggregates overall grounding according to the existing policy; it does not infer statuses from solver behavior or read model-generated assessments. [build_review.py](build_review.py) only updates this index and file inventories.

From the repository root:

```bash
python grounding/slack_ground_truth/author_labels.py
python grounding/slack_ground_truth/build_review.py
```

The prepared input bundles are separate from reports. Future evaluator calls should receive only the selected input bundle and approved policy/schema, never this folder wholesale, these labels, adjudication notes, or historical evaluator answers. No new API invocations were made to author these labels.

Inputs retain the supplied seed, API documentation, recorded net diff, trajectory, and designated final response. They do not reconstruct a final database snapshot, rerun recorded commands, or treat solver-authored descriptions of API results as actual tool observations. Runs 108 and 113 ended at the turn limit without a designated final response; that is preserved in their task metadata and response inventories.
'''
    (ROOT / 'README.md').write_text(intro + '\n'.join(rows) + '\n' + ending)
    print(f'Indexed {len(rows)} reports; {len(pending)} cases directly awaiting adjudication.')


if __name__ == '__main__':
    main()
