"""Offline source/accounting and risky-representation checks; no DB or API calls."""
import importlib
import hashlib
import json
import warnings

from sqlalchemy.exc import SAWarning
from grounding.modeling.inventory import build
from grounding.paths import REPO_ROOT


def inventories_and_models():
    reports = {}
    for domain in ['box', 'calendar', 'linear']:
        base = REPO_ROOT / 'grounding/domains' / domain
        inv = json.loads((base / 'source_inventory.json').read_text())
        assert build(domain) == inv, f'{domain}: source inventory drift'
        graph = json.loads((base / 'model.json').read_text())
        schema = importlib.import_module(f'src.services.{domain}.database.schema')
        metadata = schema.Base.metadata
        assert set(metadata.tables) == {t['table'] for t in inv['tables']}
        dispositions = {d['table']: d for d in graph['table_dispositions']}
        assert set(dispositions) == set(metadata.tables)
        edge_ids = {e['id'] for e in graph['relationships']}
        assert len(edge_ids) == len(graph['relationships'])
        nodes = {e['name'] for e in graph['entities']}
        for edge in graph['relationships']:
            assert edge['source'] in nodes and edge['target'] in nodes
            assert (REPO_ROOT / edge['source_file']).exists()
            assert edge['source_line'] > 0
        for table in inv['tables']:
            actual = metadata.tables[table['table']]
            # An ORM attribute can map to a differently named SQL column (metadata_).
            cols = list(actual.columns)
            assert len(cols) == len(table['columns'])
            for stored, live in zip(table['columns'], cols):
                assert stored['nullable'] == live.nullable, (domain, table['class'], stored['name'], 'nullable')
                assert stored['primary_key'] == live.primary_key
                assert stored['unique'] == bool(live.unique)
                assert stored['foreign_keys'] == [fk.target_fullname for fk in live.foreign_keys]
                if stored['foreign_keys'] and dispositions[table['table']]['disposition'] == 'entity':
                    assert table['class'] + '.' + stored['name'] in edge_ids
            if table['association']:
                assert table['class'] in edge_ids
        reports[domain] = {'tables': len(inv['tables']), 'columns': sum(len(t['columns']) for t in inv['tables']),
                           'operation_bindings': len(inv['operations']), 'entities': len(nodes), 'relationships': len(edge_ids)}
    return reports


def representations():
    from ariadne import make_executable_schema
    from graphql import graphql_sync
    from src.services.linear.api.resolvers import bindables
    from src.services.linear.database.schema import Issue, Project, Team, User
    source = (REPO_ROOT / 'backend/src/services/linear/api/schema/Linear-API.graphql').read_text()
    schema = make_executable_schema(source, *bindables)
    project = Project(id='p', teams=[Team(id='t')])
    issue = Issue(id='i', project=project, assignee=User(id='u'))
    # Supply the root record without DB access. Nested resolvers/default behavior
    # are the actual mounted executable schema's behavior.
    schema.query_type.fields['issue'].resolve = lambda *args, **kwargs: issue
    good = graphql_sync(schema, '{ issue(id:"i") { id assignee { id } project { id } } }')
    assert not good.errors and good.data['issue']['assignee']['id'] == 'u'
    bad = graphql_sync(schema, '{ issue(id:"i") { project { teams { nodes { id } } } } }')
    assert bad.errors and any('TeamConnection.nodes' in str(e) for e in bad.errors)
    assert schema.query_type.fields['project'].resolve is None
    from src.services.box.database.schema import HubItem, FileVersion
    item = HubItem(id='entry', item_type='file', item_id='f', item_name='Report', added_by_id='actor')
    assert item.to_dict() == {'type': 'file', 'id': 'f', 'name': 'Report'}
    version = FileVersion(id='v', sha_1='digest', modified_by_id='u')
    assert set(version.to_mini_dict()) == {'type', 'id', 'sha1'}
    from src.services.calendar.database.schema import Event
    from src.services.calendar.core.serializers import serialize_event
    from datetime import datetime
    event = Event(id='e', calendar_id='c', etag='tag', created_at=datetime(2026, 1, 1), updated_at=datetime(2026, 1, 1),
                  start={'date': '2026-01-01'}, end={'date': '2026-01-02'}, creator_id='local-id',
                  organizer_id='other-local-id', creator_email='external@example.test',
                  organizer_email='organizer@example.test', reminders={'useDefault': False, 'overrides': []})
    output = serialize_event(event)
    assert output['creator']['email'] == 'external@example.test'
    assert output['organizer']['email'] == 'organizer@example.test'
    assert 'local-id' not in json.dumps(output)
    assert output['reminders'] == {'useDefault': False, 'overrides': []}
    return ['Linear singular default relationship works; list/Connection mismatch reproduced; project root unbound',
            'Box hub target projection hides entry identity/actor; version mini hides user roles',
            'Calendar person payload is separate from User FKs; reminder JSON is the response source']


def audit_accounting():
    baseline = json.loads((REPO_ROOT / 'grounding/modeling/audit_baseline.json').read_text())
    report = {}
    for domain, frozen in baseline.items():
        base = REPO_ROOT / 'grounding/domains' / domain
        for filename, key in [('model.json', 'model_sha256'), ('route_counts.json', 'route_counts_sha256')]:
            assert hashlib.sha256((base / filename).read_bytes()).hexdigest() == frozen[key], (domain, filename, 'approval boundary')
        graph = json.loads((base / 'model.json').read_text())
        inv = json.loads((base / 'source_inventory.json').read_text())
        audit = json.loads((base / 'model_audit.json').read_text())
        tables = {t['class']: t for t in inv['tables']}
        classes = {t['table']: t['class'] for t in inv['tables']}
        groups = {g['id'] for g in audit['api_groups']}
        expected = {o['binding'] + '.' + o['field'] if 'binding' in o else o['method'] + ' ' + o['path'] for o in inv['operations']}
        assert len(audit['operations']) == len(expected)
        assert {r['operation'] for r in audit['operations']} == expected
        assert all(set(r['groups']) <= groups for r in audit['operations'])
        for edge in graph['relationships']:
            if edge['kind'] == 'foreign_key':
                col = next(c for c in tables[edge['source']]['columns'] if c['name'] == edge['role'])
                assert edge['source_line'] == col['line'], edge['id']
                assert edge['target'] == classes[col['foreign_keys'][0].split('.')[0]], edge['id']
                assert edge['target_cardinality'] == ('0..1' if col['nullable'] else '1'), edge['id']
                unique = col['unique'] or (col['primary_key'] and sum(c['primary_key'] for c in tables[edge['source']]['columns']) == 1)
                assert edge['source_cardinality'] == ('0..1' if unique else '0..*'), edge['id']
            elif edge['kind'] == 'association':
                table = tables[edge['id']]
                assert len(table['columns']) == 2 and all(c['primary_key'] and c['foreign_keys'] for c in table['columns'])
                endpoints = {classes[c['foreign_keys'][0].split('.')[0]] for c in table['columns']}
                assert endpoints == {edge['source'], edge['target']}
                assert edge['source_cardinality'] == edge['target_cardinality'] == '0..*'
        for path, sha in audit.get('source_addenda_sha256', {}).items():
            assert hashlib.sha256((REPO_ROOT / path).read_bytes()).hexdigest() == sha
        report[domain] = {'frozen_graph_and_counts': True, 'all_operations_mapped': len(expected),
                          'all_fk_targets_and_cardinalities_checked': True}
    return report


def audit_examples():
    from datetime import datetime
    from src.services.calendar.database.schema import Calendar, CalendarListEntry, EventAttendee, Setting
    from src.services.calendar.core.serializers import serialize_attendee, serialize_calendar_list_entry, serialize_setting
    attendee = EventAttendee(id='storage-attendee', email='a@example.test', profile_id='external-profile', response_status='accepted')
    assert serialize_attendee(attendee)['id'] == 'external-profile'
    entry = CalendarListEntry(id='storage-entry', calendar_id='calendar-id', access_role='reader', calendar=Calendar(id='calendar-id', summary='Schedule'))
    assert serialize_calendar_list_entry(entry)['id'] == 'calendar-id'
    setting = Setting(id='storage-setting', setting_id='locale', value='en', etag='tag')
    assert serialize_setting(setting)['id'] == 'locale'
    from src.services.box.database.schema import File, FileVersion, Folder
    file = File(id='f', name='report.txt', file_version_id='cached-v', versions=[FileVersion(id='selected-v', sha_1='digest')])
    assert file._get_file_version_dict()['id'] == 'selected-v'
    folder = Folder(id='folder', collections=['c'])
    assert folder._get_collections_dict()[0]['name'] == 'Favorites'
    from ariadne import make_executable_schema
    from graphql import graphql_sync
    from src.services.linear.api.resolvers import bindables
    from src.services.linear.database.schema import Attachment, Issue
    schema = make_executable_schema((REPO_ROOT / 'backend/src/services/linear/api/schema/Linear-API.graphql').read_text(), *bindables)
    # A raw ORM object is not the payload wrapper required by the SDL.
    schema.mutation_type.fields['issueSubscribe'].resolve = lambda *args, **kwargs: Issue(id='i')
    result = graphql_sync(schema, 'mutation { issueSubscribe(id:"i", userId:"u") { success issue { id } } }')
    assert result.errors and any('IssuePayload.success' in str(e) for e in result.errors), result
    schema.query_type.fields['attachment'].resolve = lambda *args, **kwargs: Attachment(id='a', metadata_={'stored': 'value'})
    result = graphql_sync(schema, '{ attachment(id:"a") { id metadata } }')
    assert not result.errors
    assert type(result.data['attachment']['metadata']).__name__ == 'MetaData'
    try:
        json.dumps(result.data)
    except TypeError:
        pass
    else:
        raise AssertionError('Expected unaliased SQLAlchemy metadata to fail JSON serialization')
    return ['Calendar three API identity aliases checked against real serializers',
            'Box selected version and fixed collection name are not the stored cache/lookup',
            'Linear raw Issue does not satisfy IssuePayload.success under mounted schema',
            'Linear Attachment.metadata selects SQLAlchemy MetaData, not metadata_, and cannot serialize to JSON']


if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=SAWarning)
    print(json.dumps({'inventory_and_graph_checks': inventories_and_models(), 'representation_checks': representations(),
                      'audit_accounting': audit_accounting(), 'audit_examples': audit_examples()}, indent=2))
