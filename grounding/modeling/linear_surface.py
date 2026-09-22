"""Inspect actual ORM/GraphQL field shapes without a database or service calls.

Run: PYTHONPATH=backend backend/.venv/bin/python -m grounding.modeling.linear_surface
This is evidence for the manual capability screen, not automatic ER extraction.
"""
import json
import warnings
from pathlib import Path

from graphql import build_schema, get_named_type
from sqlalchemy import inspect
from sqlalchemy.exc import SAWarning

from grounding.paths import REPO_ROOT


def build():
    from src.services.linear.database import schema as models
    warnings.filterwarnings('ignore', category=SAWarning)
    base = REPO_ROOT / 'grounding/domains/linear'
    inv = json.loads((base / 'source_inventory.json').read_text())
    schema = build_schema((REPO_ROOT / 'backend/src/services/linear/api/schema/Linear-API.graphql').read_text())
    tables = {t['class']: t for t in inv['tables'] if not t['association']}
    bindings = {'query': 'Query', 'mutation': 'Mutation', 'issue_type': 'Issue', 'team_type': 'Team', 'user_type': 'User'}
    custom = {(bindings[o['binding']], o['field']): o for o in inv['operations']}
    rows = []
    for name in tables:
        typ = schema.type_map.get(name)
        if not typ:
            continue
        for rel in inspect(getattr(models, name)).relationships:
            field = typ.fields.get(rel.key)
            if field is None:
                status = 'not_declared'
            elif (name, rel.key) in custom:
                status = 'explicit_resolver'
            elif rel.uselist and get_named_type(field.type).name.endswith('Connection'):
                status = 'list_connection_mismatch'
            else:
                status = 'default_attribute'
            if name == 'Issue' and rel.key == 'history':
                status = 'resolver_references_missing_columns'
            rows.append(dict(owner=name, field=rel.key, target=rel.mapper.class_.__name__,
                             status=status, sdl_type=str(field.type) if field else None,
                             fks=sorted(str(c) for c in rel._calculated_foreign_keys)))
    roots = set()
    for op in inv['operations']:
        if op['binding'] != 'query':
            continue
        name = get_named_type(schema.query_type.fields[op['field']].type).name
        for suffix in ['Connection', 'SearchPayload']:
            if name.endswith(suffix):
                name = name[:-len(suffix)]
        if name in tables:
            roots.add(name)
    # Verified wrappers: searchProjects/searchIssues/searchDocuments. Project
    # search dictionaries expose scalars; Project ORM fields are also reachable
    # through Issue.project and milestone/relation roots.
    roots |= {'Project', 'Issue', 'Document'}
    reachable = set(roots)
    while True:
        new = reachable | {r['target'] for r in rows if r['owner'] in reachable and r['status'] in ['default_attribute', 'explicit_resolver']}
        if new == reachable:
            break
        reachable = new
    for row in rows:
        row['owner_read_reachable'] = row['owner'] in reachable
    return dict(
        roots=sorted(roots), reachable=sorted(reachable), relationships=rows,
        unbound_roots={typ: sorted(set(schema.type_map[typ].fields) - {o['field'] for o in inv['operations'] if o['binding'] == binding})
                       for typ, binding in [('Query', 'query'), ('Mutation', 'mutation')]},
        mapped_type_fields={name: {k: str(v.type) for k, v in schema.type_map[name].fields.items()} for name in tables if name in schema.type_map},
        root_fields={typ: {k: {'returns': str(v.type), 'arguments': {a: str(b.type) for a, b in v.args.items()}, 'bound': (typ, k) in custom}
                          for k, v in schema.type_map[typ].fields.items()} for typ in ['Query', 'Mutation']},
    )


if __name__ == '__main__':
    out = REPO_ROOT / 'grounding/domains/linear/api_surface.json'
    out.write_text(json.dumps(build(), indent=2) + '\n')
    print(out.relative_to(REPO_ROOT))
