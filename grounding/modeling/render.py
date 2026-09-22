"""Project reviewed model.json and source inventories to human-readable ledgers."""
import argparse
import json
from pathlib import Path

from grounding.paths import REPO_ROOT
from grounding.modeling.audit_ledger import render_audit


def code(items):
    return ', '.join('`' + x + '`' for x in items) or '—'


def source(path, line=None):
    return f'[{Path(path).name}' + (f':{line}' if line else '') + f'](../../../{path})'


def render(domain):
    base = REPO_ROOT / 'grounding/domains' / domain
    g = json.loads((base / 'model.json').read_text())
    inv = json.loads((base / 'source_inventory.json').read_text())
    tables = {t['class']: t for t in inv['tables']}
    schema_path = f'backend/src/services/{domain}/database/schema.py'
    model = [f'# {domain.title()} conceptual model', '',
        '## Scope', '',
        f"Implemented AgentDiff replica at `{g['revision']}`. Extracted manually under the [adopted protocol](../../protocols/conceptual_meta_model.md) and [contextualization](contextualization.md). The implementation is authoritative; local API documentation supports terminology. This is not a model of the entire public service.", '',
        'Full field declarations, constraints, source hashes and dispatched operations are retained in [source_inventory.json](source_inventory.json). [model.json](model.json) records the reviewed entity/relationship decisions; [the ledger](model_source_ledger.md) records dispositions and the reverse audit. API exposure is a separate qualification: an unexposed domain concept remains in the structural model.', '',
        '## Vocabulary and entities', '', '| Entity | Meaning | Source |', '|---|---|---|']
    for entity in g['entities']:
        table = tables[entity['name']]
        model.append(f"| {entity['name']} | {entity['meaning']} | {source(schema_path, table['line'])} |")
    model += ['', '## Entity–relationship model', '',
        'The attributes below retain real implementation names. Reference columns are represented by named relationships in the following table; they are not additional scalar concepts. Structured JSON values remain structured attributes unless the implementation gives them relationship meaning. Stored snapshots/caches are retained even when API writers usually synchronize them.', '',
        '| Entity | Identity and extra uniqueness | Stored values outside declared FKs |', '|---|---|---|']
    for entity in g['entities']:
        table = tables[entity['name']]
        keys = [c['name'] for c in table['columns'] if c['primary_key']]
        unique = [c['name'] for c in table['columns'] if c['unique'] and not c['primary_key']]
        attrs = [c['name'] for c in table['columns'] if not c['primary_key'] and not c['foreign_keys']]
        identity = 'PK ' + code(keys) + ('; unique ' + code(unique) if unique else '')
        if table['constraints']:
            identity += '; see exact composite constraints/indexes in inventory'
        model.append(f"| {entity['name']} | {identity} | {code(attrs)} |")
    model += ['', 'Folded values preserve their storage identity and existence:', '']
    for disposition in g['table_dispositions']:
        if disposition['disposition'] == 'folded_value':
            table = tables[disposition['implementation_class']]
            model.append(f"- **{table['class']} → {disposition['destination']}**: {disposition['reason']} Fields: {code([c['name'] for c in table['columns']])}.")
    model += ['', '### Relationships', '',
        '`Targets/source` means the number of target records for one source record; `sources/target` is the inverse. These are storage-supported cardinalities, not stronger implications of ORM presentation or public API documentation. FK roles are named by their actual source columns. Interpreted references have their subtype/integrity qualifications below.', '',
        '| Relationship / role | Source → target | Targets/source | Sources/target | Evidence |', '|---|---|---|---|---|']
    for e in g['relationships']:
        model.append(f"| `{e['id']}` | {e['source']} → {e['target']} | {e['target_cardinality']} | {e['source_cardinality']} | {source(e['source_file'], e['source_line'])} |")
    model += ['', '<details>', '<summary>ER diagram (all relationship roles)</summary>', '', '```mermaid', 'erDiagram']
    left = {'1': '||', '0..1': '|o', '0..*': '}o'}
    right = {'1': '||', '0..1': 'o|', '0..*': 'o{'}
    for e in g['relationships']:
        # Match Slack's notation: solid only when the referenced identity
        # contributes to the child's key. Contracted associations have no child
        # entity in this diagram; their original pair keys stay in the inventory.
        identifying = e['kind'] == 'foreign_key' and any(
            c['name'] == e['role'] and c['primary_key']
            for c in tables[e['source']]['columns']
        )
        line = '--' if identifying else '..'
        model.append(f"    {e['source']} {left[e['source_cardinality']]}{line}{right[e['target_cardinality']]} {e['target']} : \"{e['role']}\"")
    model += ['```', '', '</details>', '',
        'Solid lines mean the referenced identity contributes to the child entity’s key; dashed lines mean it does not. Contracted pair associations are shown as many-to-many links, with their pair keys preserved in the source inventory. This matches Slack’s identifying/non-identifying notation and does not change graph connectivity.', '',
        '### Representations and qualifications', '']
    for key, title, body, *paths in g['qualifications']:
        model.append(f"- **{key}: {title}.** {body} Sources: " + ', '.join(source(f'backend/src/services/{domain}/{p}') for p in paths) + '.')
    model += ['', 'Derived representations do not add independent base-graph entities or duplicate edges:', '']
    model += ['- ' + text for text in g['derived']]
    model += ['', '## States and classifications', '',
        'Boolean flags, status/type strings, archive/deletion timestamps and structured policy values are attributes of their owning entity. A stored value does not prove a transition, permission check or background service is implemented. The explicit enum declarations are:', '',
        '| Declaration | Values | Interpretation |', '|---|---|---|']
    for enum in inv['enums']:
        model.append(f"| {enum['name']} | {code(list(enum['values'].values()))} | " + ('Interface vocabulary; deferred from domain graph' if enum['name'] in {'BoxErrorCode', 'BoxSortDirection'} else 'Stored/API vocabulary; use only on the fields whose implementation uses it') + ' |')
    if domain == 'linear':
        model += ['', 'Additional resolver vocabulary: priority `0..4` maps to No priority/Urgent/High/Medium/Low; default issue-state types are triage/backlog/unstarted/started/completed/canceled. Initiative/project state and health, notification category, import service/status and policy classifications remain source strings. GraphQL enum types describe accepted/serialized values, not guaranteed database constraints; mapped field types are in [api_surface.json](api_surface.json).']
    (base / 'model.md').write_text('\n'.join(model) + '\n')
    ledger = [f'# {domain.title()} model source ledger', '',
        f"Revision: `{g['revision']}`. Scope and mapping discipline: [contextualization](contextualization.md). The full declaration/field index is [source_inventory.json](source_inventory.json), and reviewed decisions are [model.json](model.json).", '',
        '## Persistence: forward coverage', '',
        '| Source table | Disposition / destination | Field treatment and reason |', '|---|---|---|']
    for d in g['table_dispositions']:
        t = tables[d['implementation_class']]
        if d['disposition'] == 'entity':
            treatment = 'Identity: ' + code([c['name'] for c in t['columns'] if c['primary_key']])
            treatment += '; FK roles: ' + code([c['name'] for c in t['columns'] if c['foreign_keys']])
            treatment += '; stored values (including separately interpreted references): ' + code([c['name'] for c in t['columns'] if not c['primary_key'] and not c['foreign_keys']])
        elif d['disposition'] == 'relationship':
            treatment = 'Pair identity/endpoints: ' + code([c['name'] for c in t['columns']])
        else:
            treatment = 'All fields follow this disposition: ' + code([c['name'] for c in t['columns']])
        ledger.append(f"| `{d['table']}` ({source(schema_path, t['line'])}) | {d['disposition']} → {d['destination']} | {d['reason']} {treatment}. Exact declarations and constraints are in the inventory. |")
    ledger += ['', 'ORM reverse relationships are projections of these roles, not extra edges. The full relationship declarations remain in the inventory. Composite pair associations are contracted once; owner-value folds remove only the storage split, preserving all values. No table is silently omitted.', '',
        '## API: forward coverage', '',
        'The operation inventory expands HTTP dispatchers by verb or records each actual GraphQL binding. Each operation maps to the families below. Within each handler the inventory retains accessed input keys, constructed object keys, keyword arguments, attribute expressions and helper calls; follow these to the corresponding entity fields/representations. Transport arguments (pagination, cursors, formatting, field selection), error/success envelopes and execution preconditions/effects are deferred to interface/behavior analysis. None establishes another domain entity.', '',
        '| Family | Domain-bearing inputs/outputs and treatment |', '|---|---|']
    for name, prefixes, text in g['operation_groups']:
        ledger.append(f'| {name} | {text} |')
    ledger += ['', '| Registered operation/binding | Handler evidence |', '|---|---|']
    for o in inv['operations']:
        name = f"{o['binding']}.{o['field']}" if domain == 'linear' else f"{o['method']} {o['path']}"
        path = o.get('source', f'backend/src/services/{domain}/api/resolvers.py')
        ledger.append(f"| `{name}` | `{o['handler']}` — {source(path, o['line'])} |")
    if domain == 'linear':
        ledger += ['', 'The SDL also declares 77 unbound Query fields and 173 unbound Mutation fields. They are explicitly inventoried in [api_surface.json](api_surface.json): declared-only domain concepts are not claimed implemented. All mapped ORM relationship fields are recorded there, including missing SDL fields, broken list/connection shapes and explicit/default resolver witnesses. Derived Team.members/User.teams and Issue.documents do not duplicate base relations. Public type fields without storage or a resolver remain unsupported declarations, not invented entity attributes.']
    if domain == 'calendar':
        ledger += ['', 'The 37 batch aliases reuse the direct handlers; the additional registered batch operation is transport. Channel/SyncToken fields, channel response objects and nextSyncToken/watch metadata are deferred interface state. Defaults and virtual instances are derived values, with evidence in operations/serializers/utils.']
    ledger += ['', '## Validation scope', '',
        'The completion audit below records both directions of review, corrections and remaining qualifications. Its manual source decisions are stored in model_audit.json; the earlier broad summary in model.json is not used as a substitute for those checks.', '',
        'The modeling tools compare inventory with live ORM metadata, check all retained FK targets/cardinalities and operation mappings, and exercise risky serializer/GraphQL shapes offline. Mechanical accounting supplements the manual interpretation; it does not prove runtime correctness.', '',
        'Route counting excludes repeated entity types, attributes, resolution modes and derived shortcuts. The read screen does not certify whole-route discovery, every attribute, permissions or ordinary-use meaningfulness. No ordinary-request inclusion review is claimed.']
    ledger += render_audit(base)
    (base / 'model_source_ledger.md').write_text('\n'.join(ledger) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', choices=['box', 'calendar', 'linear'])
    render(parser.parse_args().domain)
