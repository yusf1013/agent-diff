"""Load a compiled fresh seed and exercise native Slack reads without an LLM/server.

Uses the real PostgreSQL schema and Slack route handlers in an in-process ASGI app.
Middleware supplies the same scoped session/actor contract as the platform. This
does not exercise platform HTTP authentication, the solver sandbox, or writes.
"""
from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
from types import SimpleNamespace

from grounding.integrations.agentdiff import runtime
from grounding.common.bedrock import save
from grounding.common.io import TABLES, read
from grounding.generation.validate import validate_case


def check(case, out, database_url):
    import httpx
    from sqlalchemy.orm import Session
    from starlette.applications import Starlette
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.routing import Mount, Router
    runtime.dependencies()
    from src.services.slack.api.methods import routes

    out=Path(out); out.mkdir(parents=True,exist_ok=False)
    before=validate_case(case); save(out/'source_checks.json',before)
    if before['errors']: raise ValueError('Invalid input case: '+str(before['errors']))
    engine=runtime.engine_for(database_url); template=None; client=None
    loop=asyncio.new_event_loop()
    result={'status':'running'}
    try:
        template=runtime.install_template(case,engine)
        initial=runtime.export_state(engine,template['template_name'])
        save(out/'installed_state.json',initial)
        checks=validate_case({**case,'seed':{t:initial[t] for t in TABLES}})
        save(out/'installed_checks.json',checks)
        if checks['errors']: raise ValueError('Installed state failed checks: '+str(checks['errors']))
        app=Starlette(routes=[Mount('/api/env/compile/services/slack',app=Router(routes=routes))])
        scoped=engine.execution_options(schema_translate_map={None:template['template_name']})
        async def supply_session(request, call_next):
            with Session(scoped) as session:
                request.state.db_session=session
                request.state.environment_id='compile'
                request.state.impersonate_user_id=case['acting_user_id']
                request.state.impersonate_email=None
                return await call_next(request)
        app.add_middleware(BaseHTTPMiddleware, dispatch=supply_session)
        client=httpx.AsyncClient(transport=httpx.ASGITransport(app=app),base_url='http://native')
        def get(url, **kwargs):
            response=loop.run_until_complete(client.get(url,**kwargs))
            # Existing collector uses requests.Response's .ok attribute.
            response.ok=response.is_success
            return response
        adapter=SimpleNamespace(base_url='http://native',_headers=lambda:{})
        probes=runtime.probe_environment(adapter,'compile',case,initial,get=get)
        save(out/'visibility.json',probes)
        visibility=runtime.certify_visibility(case,initial,probes)
        save(out/'visibility_check.json',visibility)
        unchanged=runtime.digest(initial)==runtime.digest(runtime.export_state(engine,template['template_name']))
        result={'status':'passed' if not probes['required_errors'] and unchanged else 'failed',
                'loaded':True,'installed_matches':checks['computed_matches'],
                'probe_count':len(probes['probes']),
                'probe_errors':[e for p in probes['probes'] for e in p['errors']],
                'required_errors':probes['required_errors'],'state_unchanged':unchanged,
                'mechanical_visibility_established':visibility['certified'],
                'model_calls':0,'writes_exercised':False,
                'transport':'Native Slack handlers, in-process ASGI; scoped PostgreSQL session and actor middleware.',
                'scope':'Load and read checks; no platform-auth, sandbox or requested-write certification.'}
        return result
    except Exception as exc:
        result={'status':'error','error':f'{type(exc).__name__}: {exc}'}
        raise
    finally:
        try:
            if client: loop.run_until_complete(client.aclose())
            if template: runtime.cleanup(template,database_url)
        finally:
            engine.dispose(); loop.close()
            save(out/'summary.json',result)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('case',type=Path);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--database-url',required=True)
    args=p.parse_args(); result=check(read(args.case),args.out,args.database_url)
    print(result)
    raise SystemExit(result['status']!='passed')


if __name__=='__main__':main()
