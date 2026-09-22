"""Render explicit manual audit annotations; never infer semantic approval."""
import json
from pathlib import Path


def render_audit(base):
    path = base / 'model_audit.json'
    if not path.exists():
        return []
    audit = json.loads(path.read_text())
    lines = ['', '## Completion audit: explicit evidence mappings', '',
             audit['status'], '',
             'This section supersedes the earlier broad audit summary. It records manual interpretation; inventories and checks establish accounting, not semantic correctness by themselves.', '',
             '### Shared API field mappings', '',
             '| ID | Source witness | Fields, disposition and model destination |', '|---|---|---|']
    for row in audit['api_groups']:
        lines.append(f"| {row['id']} | {row['source']} | {row['mapping']} |")
    lines += ['', '### Operation-to-field-group coverage', '',
              'Every registered operation is assigned below. Shared response mappings are recorded once above. Operations retain their exact dispatch/source references in the preceding inventory.', '',
              '| Operation | Applicable field mappings | Operation-specific qualification |', '|---|---|---|']
    for row in audit['operations']:
        lines.append(f"| `{row['operation']}` | {', '.join(row['groups'])} | {row['note']} |")
    lines += ['', '### Model-to-source checks', '',
              '| Model elements | Source and concrete check | Result / qualification |', '|---|---|---|']
    for row in audit['reverse_checks']:
        lines.append(f"| {row['elements']} | {row['check']} | {row['result']} |")
    field_path = base / 'api_field_accounting.json'
    if field_path.exists():
        accounting = json.loads(field_path.read_text())
        lines += ['', '### Declared GraphQL fields: exhaustive disposition index', '',
                  'The [field accounting file](api_field_accounting.json) assigns every field declared on an ORM-mapped type to its existing storage, relationship projection, explicit resolver, declaration-only omission, or Python-attribute collision. This supplements L-A1; it does not add model attributes or certify that a requested field executes successfully.', '',
                  '| Type | Stored fields | Explicit resolvers | Relationship projections | Declared-only or Python-collision fields |', '|---|---|---|---|---|']
        for owner in sorted({r['owner'] for r in accounting['fields']}):
            rows = [r for r in accounting['fields'] if r['owner'] == owner]
            def fields(dispositions):
                return ', '.join('`' + r['field'] + '`' for r in rows if r['disposition'] in dispositions) or '—'
            lines.append(f"| {owner} | {fields({'represented'})} | {fields({'derived_or_projected'})} | {fields({'represented_relationship_projection'})} | {fields({'omitted_from_implemented_inference', 'deferred_interface_collision'})} |")
    lines += ['', '### Findings and approval boundary', '']
    lines.extend('- ' + s for s in audit['findings'])
    return lines
