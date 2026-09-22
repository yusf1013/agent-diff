"""Account for every declared field on mapped Linear types, without adding concepts.

Mechanical field shape/source evidence supplements the manual L-A1 disposition.
It does not certify successful execution or turn public declarations into state.
"""
import json
import warnings

from graphql import build_schema, get_named_type, GraphQLEnumType
from sqlalchemy import inspect
from sqlalchemy.exc import SAWarning

from grounding.paths import REPO_ROOT


def build():
    from src.services.linear.database import schema as models
    warnings.filterwarnings('ignore', category=SAWarning)
    base = REPO_ROOT / 'grounding/domains/linear'
    inv = json.loads((base / 'source_inventory.json').read_text())
    surface = json.loads((base / 'api_surface.json').read_text())
    schema = build_schema((REPO_ROOT / 'backend/src/services/linear/api/schema/Linear-API.graphql').read_text())
    tables = {t['class']: t for t in inv['tables'] if not t['association']}
    rels = {(r['owner'], r['field']): r for r in surface['relationships']}
    bindings = {'query': 'Query', 'mutation': 'Mutation', 'issue_type': 'Issue', 'team_type': 'Team', 'user_type': 'User'}
    custom = {(bindings[o['binding']], o['field']): o for o in inv['operations']}
    rows = []
    for owner, fields in surface['mapped_type_fields'].items():
        cls = getattr(models, owner)
        columns = {c['name']: c for c in tables[owner]['columns']}
        for field, type_ in fields.items():
            row = dict(owner=owner, field=field, graphql_type=type_)
            if (owner, field) in custom:
                op = custom[owner, field]
                row.update(disposition='derived_or_projected', witness=f"api/resolvers.py:{op['line']} {op['handler']}",
                           interpretation='Explicit resolver; use operation-specific L-A mappings, not a new stored field.')
            elif field in columns:
                col = columns[field]
                row.update(disposition='represented', witness=f"database/schema.py:{col['line']} {owner}.{field}",
                           interpretation='Existing mapped column; default field lookup. GraphQL coercion and object reachability are separate qualifications.')
            elif (owner, field) in rels:
                r = rels[owner, field]
                row.update(disposition='represented_relationship_projection', witness=f'{owner}.{field}: {r["fks"]}',
                           interpretation=r['status'])
            elif hasattr(cls, field):
                row.update(disposition='deferred_interface_collision', witness=f'Unmapped Python attribute {owner}.{field}',
                           interpretation='Default lookup finds a Python attribute, not a mapped domain value. In particular metadata is SQLAlchemy MetaData, not metadata_.')
            else:
                row.update(disposition='omitted_from_implemented_inference', witness='No mapped column/property or registered field resolver',
                           interpretation='Declared-only field on this implementation type; do not invent a domain attribute or relationship.')
            named = get_named_type(schema.type_map[owner].fields[field].type)
            if isinstance(named, GraphQLEnumType):
                row['graphql_enum_values'] = list(named.values)
            rows.append(row)
    return dict(scope='Fields declared on ORM-mapped GraphQL types; root contracts remain in api_surface.json.',
                meaning='Accounting and source witnesses, not runtime certification or automatic conceptual extraction.', fields=rows)


if __name__ == '__main__':
    path = REPO_ROOT / 'grounding/domains/linear/api_field_accounting.json'
    path.write_text(json.dumps(build(), indent=2) + '\n')
    print(path.relative_to(REPO_ROOT))
