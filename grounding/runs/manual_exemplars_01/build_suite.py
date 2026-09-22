"""Build the manual suite. Offline and deterministic; no API/model calls.

Run from the repository root: python grounding/runs/manual_exemplars_01/build_suite.py
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2]))

from grounding.generation.validate import validate_case
from suite_support import story_section
from suite_w01_w02 import build_entries as first
from suite_w03_w06 import build_entries as middle
from suite_w07_w10 import build_entries as last
from suite_locations_w01_w04 import build_entries as locations_first
from suite_locations_w06_w07 import build_entries as locations_middle
from suite_locations_w08_w10 import build_entries as locations_last
from story_locations import render as render_locations


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def build():
    entries = first() + middle() + last()
    additions = locations_first() + locations_middle() + locations_last()
    assert len(entries) == 42 and len(additions) == 15
    entries += additions
    additional_ids = {e['case']['case_id'] for e in additions}
    total = len(entries)
    assert len({e['case']['case_id'] for e in entries}) == total
    originals = (HERE / 'story.md').read_text()
    original_sections = {m.group(1): m.group(2) for m in re.finditer(r'^## (W\d+)\n(.*?)(?=^## W\d+\n|\Z)', originals, re.M | re.S)}
    checks, manifest = [], []
    variants = []
    (HERE / 'cases').mkdir(exist_ok=True)
    from audit_suite import audit
    for entry in entries:
        case = entry['case']
        cid, base = case['case_id'], entry['base_id']
        section = original_sections[base]
        entry['route'] = re.search(r'\*\*Route:\*\* (.+)', section).group(1)
        original_prompt = re.search(r'\*\*Request:\*\* (.+)', section).group(1)
        if cid.endswith('-base'):
            assert case['prompt'] == original_prompt, (cid, case['prompt'], original_prompt)
        # Validate computation inputs through actual profile responses in the native check.
        if base in ('W09', 'W10'):
            probes = []
            for membership in case['seed']['user_teams']:
                uid, tid, role = (membership[k] for k in ('user_id', 'team_id', 'role'))
                fields = [{'path': ['user', 'team_id'], 'equals': tid}]
                if base == 'W10':
                    fields += [{'path': ['user', 'is_admin'], 'equals': role in ('admin', 'owner')},
                               {'path': ['user', 'is_owner'], 'equals': role == 'owner'}]
                probes.append({'method': 'users.info', 'params': {'user': uid}, 'required': True, 'checks': fields})
            case['visibility_probes'] = probes
        check = validate_case(case)
        independent_errors = audit(case)
        checks.append({'case_id': cid, 'mechanical': check, 'independent_errors': independent_errors})
        if check['errors'] or independent_errors:
            raise ValueError(f'{cid}: {check["errors"] + independent_errors}')
        path = HERE / 'cases' / (cid + '.json')
        write_json(path, case)
        manifest.append({'case_id': cid, 'base': base, 'original': cid.endswith('-base'),
                         'mode': case['private']['mode'], 'path': f'cases/{cid}.json',
                         'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                         'expected_match_or_candidate_union_count': len(case['private']['expected_matches']),
                         'candidate_sets': case['private']['candidate_sets'],
                         'source': 'story3.md' if cid in additional_ids else 'story.md' if cid.endswith('-base') else 'story2.md',
                         'change': entry['change'],
                         **({'ambiguity': entry['ambiguity']} if cid in additional_ids else {})})
        if not cid.endswith('-base') and cid not in additional_ids:
            variants.append(story_section(entry))
    intro = '''# Manual Slack exemplars — resolution variants

These 32 manually authored variants supplement the 10 originals in [story.md](story.md).
Every entry is a separate environment. The original story's conventions apply:
labels such as M1 are private table labels; repeated names identify the same records
unless distinct people are explicitly named; the actor can read every scenario channel.
Tables describe current facts, including exact membership counts. Neither the table
nor its interpretations are given to the solver.

Requests retain their short wording. Singular/plural changes distinguish one unresolved
target from a jointly intended collection where necessary. As explicitly agreed for
W01 (and applied to W05/W06/W10), a single variant can retain a plural request when the
supplied environment has exactly one match. This is an instance cardinality variant.
Underspecified candidate sets are alternatives, not permission to choose or combine them.

Full executable cases, including the originals, are indexed in [manifest.json](manifest.json).
The review and verification limits are documented in [review.md](review.md).

'''
    (HERE / 'story2.md').write_text(intro + '\n'.join(variants))
    (HERE / 'story3.md').write_text(render_locations(additions))
    modes = dict(sorted(Counter(e['case']['private']['mode'] for e in entries).items()))
    write_json(HERE / 'manifest.json', {'provenance': 'Manual test design and labels; deterministic serialization.',
        'originals': 10, 'new_variants': total - 10, 'resolution_variants': 32,
        'ambiguity_location_additions': len(additions), 'total': total, 'modes': modes,
        'solver_runs': 0, 'paid_model_calls': 0, 'cases': manifest})
    write_json(HERE / 'checks.json', {'total': total, 'passed': len(checks), 'checks': checks})
    print(json.dumps({'total': total, 'new_variants': total - 10, 'modes': modes, 'checks_passed': len(checks)}))


if __name__ == '__main__':
    build()
