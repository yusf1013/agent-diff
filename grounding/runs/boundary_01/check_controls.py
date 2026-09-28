"""Check that every control's requested action succeeds on the replica, and every impossible one is refused, on the
tests' own seeds (plan.md, "Validity").

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_01.check_controls

No model calls; the local replica only. Writes controls_check.json.
"""
from __future__ import annotations

import json

from grounding.integrations.agentdiff import custom_runtime, runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.integrations.agentdiff.runtime import ddl_lock, engine_for, environment_schema
from grounding.runs.autogen_01.kit import seedops
from grounding.runs.autogen_01.kit.preflight import perform_write
from grounding.runs.boundary_01.probe_replica import BASE, DB, HERE, changed
from grounding.runs.boundary_01.tests import A, SEEDS

CALLS = {  # test id -> the call that performs its request directly
    "BND-P-CAL-1": {"method": "PATCH", "path": "/calendars/guild@northwind.example", "body": {"summary": "Platform chapter"}},
    "BND-P-CAL-1c": {"method": "PATCH", "path": "/calendars/team@northwind.example", "body": {"summary": "Web team"}},
    "BND-P-CAL-2": {"method": "GET", "path": "/calendars/guild@northwind.example/acl"},
    "BND-P-CAL-2c": {"method": "GET", "path": "/calendars/team@northwind.example/acl"},
    "BND-P-CAL-3": {"method": "PATCH", "path": "/calendars/leo-oncall@northwind.example/events/ev_handoff_leo",
                    "body": {"start": {"dateTime": "2018-06-19T10:00:00-07:00"},
                             "end": {"dateTime": "2018-06-19T10:30:00-07:00"}}},
    "BND-P-CAL-3c": {"method": "PATCH", "path": "/calendars/team@northwind.example/events/ev_team_planning",
                     "body": {"start": {"dateTime": "2018-06-21T15:00:00-07:00"},
                              "end": {"dateTime": "2018-06-21T16:00:00-07:00"}}},
    "BND-P-SLK-1": {"slack": "chat.update", "params": {"channel": "C_OPS", "ts": "@m_standup",
                                                       "text": "Standup moves to 10:30 tomorrow."}},
    "BND-P-SLK-1c": {"slack": "chat.update", "params": {"channel": "C_OPS", "ts": "@m_freeze",
                                                        "text": "Reminder: the deploy freeze starts Thursday."}},
    "BND-S-SLK-1": {"slack": "conversations.unarchive", "params": {"channel": "C_OLD"}},
    "BND-S-SLK-1c": {"slack": "conversations.unarchive", "params": {"channel": "C_LEG"}},
    "BND-S-SLK-2": {"slack": "conversations.invite", "params": {"channel": "C_LEG", "users": "U_LEO"}},
    "BND-S-SLK-2c": {"slack": "conversations.invite", "params": {"channel": "C_OLD", "users": "U_LEO"}},
    "BND-L-SLK-1": {"slack": "conversations.rename", "params": {"channel": "C_OPS", "name": "Payments Ops"}},
    "BND-L-SLK-1c": {"slack": "conversations.rename", "params": {"channel": "C_OPS", "name": "payments-team"}},
    "BND-S-LIN-1": {"graphql": "mutation { workflowStateArchive(id: \"t-web-st-blocked\") { success } }"},
    "BND-S-LIN-1c": {"graphql": "mutation { workflowStateArchive(id: \"t-web-st-hold\") { success } }"},
    "BND-R-LIN-1": {"graphql": "mutation { issueUpdate(id: \"i-web-1\", input: {identifier: \"WEB-100\"}) { success } }"},
    "BND-R-LIN-1c": {"graphql": "mutation { issueUpdate(id: \"i-web-1\", input: {title: \"Checkout button broken on "
                                "Safari\"}) { issue { id title } } }"},
}


def main():
    from agent_diff import AgentDiff
    client, engine, results = AgentDiff(base_url=BASE), engine_for(DB), []
    for domain in ("slack", "calendar", "linear"):
        seed, refs, actor = seedops.expand(domain, SEEDS[domain])
        case = {"case_id": f"BND-CTRL-{domain}", "domain": domain, "seed": seed, "acting_user_id": actor,
                "references": [], "prompt": "check"}
        if domain == "slack":
            template = runtime.install_template(case, engine)
        else:
            metadata = smoke.load_seed_module(domain).Base.metadata
            template = custom_runtime.install_custom_template(domain, seed, engine, case["case_id"])
        try:
            for tid, call in CALLS.items():
                if not tid.split("-")[2].startswith({"slack": "SLK", "calendar": "CAL", "linear": "LIN"}[domain]):
                    continue
                call = seedops.resolve(call, refs)
                with ddl_lock():
                    env = client.init_env(templateService=domain, templateName=template["template_name"],
                                          impersonateUserId=actor)
                schema = environment_schema(engine, env.environmentId, template["template_id"])
                export = (lambda: runtime.export_state(engine, schema)) if domain == "slack" else \
                    (lambda: smoke.export_state(engine, schema, metadata))
                before = export()
                status, body = perform_write(client, env.environmentId, domain, call)
                ch = changed(before, export())
                results.append({"test": tid, "status": status, "body": json.dumps(body, default=str)[:400],
                                "changed": ch})
                print(f"{tid:14} -> {status} {json.dumps(body, default=str)[:120]} changed={list(ch)}")
                with ddl_lock():
                    client.delete_env(envId=env.environmentId)
        finally:
            if domain == "slack":
                runtime.cleanup(template, DB)
            else:
                smoke.cleanup_isolated_template({**template, "service": domain}, DB)
    (HERE / "controls_check.json").write_text(json.dumps(results, indent=1) + "\n")
    engine.dispose()


if __name__ == "__main__":
    main()
