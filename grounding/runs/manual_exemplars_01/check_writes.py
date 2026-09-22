"""Exercise manually specified writes in isolated native fixtures, without a solver.

This checks that a known target/operation can execute and that its complete net
diff is the intended one. It does not measure agent grounding or discovery.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from grounding.integrations.agentdiff import runtime


def row_key(row, keys):
    return tuple(row[k] for k in keys)


def difference(before, after, metadata):
    changes = {}
    for name, table in metadata.tables.items():
        keys = [c.name for c in table.primary_key.columns]
        old = {row_key(r, keys): r for r in before[name]}
        new = {row_key(r, keys): r for r in after[name]}
        added = [new[k] for k in new.keys() - old.keys()]
        removed = [old[k] for k in old.keys() - new.keys()]
        updated = [{'before': old[k], 'after': new[k]} for k in old.keys() & new.keys() if old[k] != new[k]]
        if added or removed or updated:
            changes[name] = {'added': added, 'removed': removed, 'updated': updated}
    return changes


def verify_changes(case, before, after, changes, dm_channels):
    reference = case['private']['reference_outcome']
    op, targets, actor = reference['operation'], reference['targets'], case['acting_user_id']
    kind = op['kind']
    errors = []
    expected_tables = {
        'react': {'message_reactions'}, 'remove_reaction': {'message_reactions'},
        'remove_member': {'channel_members'}, 'post': {'messages'},
        'reply': {'messages'}, 'dm': {'messages', 'channels', 'channel_members'},
    }[kind]
    if set(changes) != expected_tables:
        errors.append(f'Changed tables {sorted(changes)} differ from expected {sorted(expected_tables)}')
    if any(change['updated'] for change in changes.values()):
        errors.append('Existing rows were modified')
    added = {t: c['added'] for t, c in changes.items()}
    removed = {t: c['removed'] for t, c in changes.items()}
    if kind in ('remove_member', 'remove_reaction'):
        if any(added.values()):
            errors.append('A removal inserted records')
        table = 'channel_members' if kind == 'remove_member' else 'message_reactions'
        keys = ('channel_id', 'user_id') if kind == 'remove_member' else ('message_id', 'user_id', 'reaction_type')
        observed = {row_key(r, keys) for r in removed.get(table, [])}
        expected = {row_key(r, keys) for r in targets}
        if observed != expected:
            errors.append(f'Deleted targets differ: expected {sorted(expected)!r}, observed {sorted(observed)!r}')
    else:
        if any(removed.values()):
            errors.append('An additive operation deleted records')
        if kind == 'react':
            keys = ('message_id', 'user_id', 'reaction_type')
            expected = {(mid, actor, op['emoji']) for mid in targets}
            observed = {row_key(r, keys) for r in added.get('message_reactions', [])}
            if observed != expected:
                errors.append(f'Added reactions differ: expected {sorted(expected)!r}, observed {sorted(observed)!r}')
        else:
            messages = added.get('messages', [])
            if len(messages) != len(targets):
                errors.append(f'Expected {len(targets)} new messages, observed {len(messages)}')
            if any(m['user_id'] != actor or m['message_text'] != op['text'] for m in messages):
                errors.append('New message author or exact text differs')
            if kind == 'reply':
                old_messages = {m['message_id']: m for m in before['messages']}
                expected = {(old_messages[mid]['channel_id'], mid) for mid in targets}
            elif kind == 'dm':
                expected = {(dm_channels[uid], None) for uid in targets}
            else:
                expected = {(cid, None) for cid in targets}
            observed = {(m['channel_id'], m.get('parent_id')) for m in messages}
            if observed != expected:
                errors.append(f'Message destinations/parent IDs differ: expected {sorted(expected)!r}, observed {sorted(observed)!r}')
            if kind == 'dm':
                new_channels = added.get('channels', [])
                created_ids = {ch['channel_id'] for ch in new_channels}
                if created_ids != set(dm_channels.values()) or len(new_channels) != len(targets):
                    errors.append('Created DM channels do not correspond one-to-one with intended recipients')
                actor_team = next(r['team_id'] for r in before['user_teams'] if r['user_id'] == actor)
                if any(ch.get('is_dm') is not True or ch.get('is_gc') is True or ch['team_id'] != actor_team for ch in new_channels):
                    errors.append('Created channel is not a direct conversation in the actor workspace')
                expected_members = {(cid, uid) for uid, cid in dm_channels.items()} | {(cid, actor) for cid in dm_channels.values()}
                observed_members = {(r['channel_id'], r['user_id']) for r in added.get('channel_members', [])}
                if observed_members != expected_members:
                    errors.append('DM membership changes do not exactly contain actor plus intended recipient')
    return errors


async def exercise(case, database_url):
    import httpx
    from sqlalchemy.orm import Session
    from starlette.applications import Starlette
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.routing import Mount, Router

    _, metadata, _ = runtime.dependencies()
    from src.services.slack.api.methods import routes
    engine = runtime.engine_for(database_url)
    template = None
    before = None
    result = {'case_id': case['case_id'], 'status': 'running', 'calls': [], 'errors': []}
    try:
        template = runtime.install_template(case, engine)
        before = runtime.export_state(engine, template['template_name'])
        scoped = engine.execution_options(schema_translate_map={None: template['template_name']})
        app = Starlette(routes=[Mount('/api/env/manual_write/services/slack', app=Router(routes=routes))])

        async def supply_session(request, call_next):
            with Session(scoped) as session:
                request.state.db_session = session
                request.state.environment_id = 'manual_write'
                request.state.impersonate_user_id = case['acting_user_id']
                request.state.impersonate_email = None
                response = await call_next(request)
                # Match SessionManager.with_session_for_environment's transaction
                # boundary. The existing read-only preflight has no writes to commit.
                session.commit()
                return response

        app.add_middleware(BaseHTTPMiddleware, dispatch=supply_session)
        dm_channels = {}
        reference = case['private']['reference_outcome']
        op, targets = reference['operation'], reference['targets']
        result.update({'operation': op, 'targets': targets})
        messages = {m['message_id']: m for m in before['messages']}
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url='http://native') as client:
            async def call(method, payload):
                response = await client.post('/api/env/manual_write/services/slack/' + method, json=payload)
                body = response.json()
                result['calls'].append({'method': method, 'request': payload, 'http_status': response.status_code, 'response': body})
                if not response.is_success or body.get('ok') is not True:
                    raise ValueError(f'{method} failed: {body}')
                return body

            for target in targets:
                if op['kind'] == 'react':
                    await call('reactions.add', {'channel': messages[target]['channel_id'], 'timestamp': target, 'name': op['emoji']})
                elif op['kind'] == 'reply':
                    await call('chat.postMessage', {'channel': messages[target]['channel_id'], 'thread_ts': target, 'text': op['text']})
                elif op['kind'] == 'post':
                    await call('chat.postMessage', {'channel': target, 'text': op['text']})
                elif op['kind'] == 'dm':
                    response = await call('conversations.open', {'users': target})
                    cid = response['channel']['id']
                    dm_channels[target] = cid
                    await call('chat.postMessage', {'channel': cid, 'text': op['text']})
                elif op['kind'] == 'remove_member':
                    await call('conversations.kick', {'channel': target['channel_id'], 'user': target['user_id']})
                elif op['kind'] == 'remove_reaction':
                    await call('reactions.remove', {'channel': messages[target['message_id']]['channel_id'],
                               'timestamp': target['message_id'], 'name': target['reaction_type']})
                else:
                    raise ValueError(f'Unknown manual operation {op["kind"]!r}')
        after = runtime.export_state(engine, template['template_name'])
        changes = difference(before, after, metadata)
        result['net_changes'] = changes
        result['errors'] = verify_changes(case, before, after, changes, dm_channels)
        result['status'] = 'passed' if not result['errors'] else 'failed'
    except Exception as exc:
        result['errors'].append(f'{type(exc).__name__}: {exc}')
        result['status'] = 'error'
        if template and before is not None:
            try:
                after = runtime.export_state(engine, template['template_name'])
                result['net_changes'] = difference(before, after, metadata)
                result['state_unchanged_after_rejection'] = before == after
            except Exception as export_exc:
                result['errors'].append(f'Final export {type(export_exc).__name__}: {export_exc}')
    finally:
        try:
            if template:
                runtime.cleanup(template, database_url)
            result['isolated_schema_cleaned'] = True
        except Exception as exc:
            result['errors'].append(f'Cleanup {type(exc).__name__}: {exc}')
            result['status'] = 'error'
            result['isolated_schema_cleaned'] = False
        engine.dispose()
    return result


async def run(folder, database_url, case_ids=None):
    selected = []
    for path in sorted((folder / 'cases').glob('*.json')):
        case = json.loads(path.read_text())
        if case['private']['reference_outcome']['state_changes_permitted'] and (not case_ids or case['case_id'] in case_ids):
            assert case['private']['mode'] in ('single', 'multiple')
            selected.append((path, case))
    if case_ids and set(case_ids) != {case['case_id'] for _, case in selected}:
        raise ValueError('Requested cases must exist and permit resolved state-changing operations')
    output = folder / 'write_checks.json'
    results = []
    if case_ids and output.exists():
        # A focused rerun replaces only those fixtures, preserving other evidence.
        results = [r for r in json.loads(output.read_text())['cases'] if r['case_id'] not in case_ids]
    summary = {'scope': 'Known-correct manual fixture operations through native Slack API handlers; not solver performance or discovery.',
               'transport': 'In-process ASGI with isolated PostgreSQL schemas and scoped actor sessions.',
               'model_calls': 0, 'solver_runs': 0, 'cases': results}
    for path, case in selected:
        result = await exercise(case, database_url)
        result['source_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        results.append(result)
        print(case['case_id'], result['status'], result['errors'], flush=True)
        runtime.write(folder / 'write_checks.json', summary)
    summary['case_count'] = len(results)
    results.sort(key=lambda result: result['case_id'])
    summary['passed'] = sum(r['status'] == 'passed' for r in results)
    summary['failed'] = len(results) - summary['passed']
    runtime.write(folder / 'write_checks.json', summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--folder', type=Path, default=Path(__file__).parent)
    parser.add_argument('--database-url', required=True)
    parser.add_argument('--cases', nargs='+', help='Rerun these fixtures only, retaining other saved results.')
    args = parser.parse_args()
    result = asyncio.run(run(args.folder, args.database_url, args.cases))
    raise SystemExit(result['failed'] != 0)


if __name__ == '__main__':
    main()
