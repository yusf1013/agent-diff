"""Which real-service limits does the replica enforce the same way? (boundary_01 plan, "Candidates")

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_01.probe_replica

For each candidate limit: install a tiny seed, open an environment as the actor, make the call the real service
refuses (or ignores), and record the replica's status, body and state change. No model calls; the local replica only.
Writes probes.json.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from grounding.integrations.agentdiff import custom_runtime, runtime
from grounding.integrations.agentdiff import smoke_runtime as smoke
from grounding.integrations.agentdiff.runtime import ddl_lock, engine_for, environment_schema
from grounding.runs.autogen_01.kit import seedops
from grounding.runs.autogen_01.kit.preflight import perform_write

HERE = Path(__file__).resolve().parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = os.environ.get("AGENTDIFF_BASE_URL", "http://127.0.0.1:18001")
A = "jordan.lee@northwind.example"

SEEDS = {
    "slack": [["channel", {"id": "C_LIVE", "name": "payments-old", "members": ["priya", "diego"]}],
              ["channel", {"id": "C_ARCH", "name": "payments-legacy", "members": ["priya"],
                           "set": {"is_archived": True}}],
              ["message", {"channel": "C_LIVE", "author": "priya", "text": "Standup moved to 10.",
                           "at": "2026-09-21T12:00:00Z", "ref": "m_priya"}]],
    "calendar": [["calendar", {"id": "maya-team@northwind.example", "summary": "Maya's team", "owner": "maya",
                               "access": "writer"}],
                 ["calendar", {"id": "leo-oncall@northwind.example", "summary": "Leo on-call", "owner": "leo",
                               "access": "reader"}],
                 ["acl", {"id": "acl1", "calendar": "maya-team@northwind.example", "role": "writer",
                          "scope_type": "user", "scope_value": A}],
                 ["event", {"id": "ev_leo", "calendar": "leo-oncall@northwind.example", "summary": "On-call handoff",
                            "start": "2018-06-19T09:00:00", "end": "2018-06-19T09:30:00", "organizer": "leo"}],
                 ["event", {"id": "ev_maya", "calendar": "primary", "summary": "Design sync",
                            "start": "2018-06-19T11:00:00", "end": "2018-06-19T11:30:00", "organizer": "maya",
                            "attendees": [["maya", "accepted"], ["kenji", "accepted"]]}]],
    "linear": [["team", {"id": "t-web", "name": "Web", "key": "WEB"}],
               ["issue", {"id": "i-web-1", "team": "t-web", "title": "Checkout button broken", "state": "Todo"}]],
    "box": [["folder", {"id": "6100", "name": "Drafts"}],
            ["file", {"id": "6101", "name": "Plan.docx", "parent": "6100"}],
            ["file", {"id": "6102", "name": "Budget.xlsx", "parent": "6100", "owner": "MC"}]],
}
CALLS = {  # domain -> [(class, what, call)]
    "slack": [
        ("state precondition", "unarchive a channel that is not archived",
         {"slack": "conversations.unarchive", "params": {"channel": "C_LIVE"}}),
        ("state precondition", "post to an archived channel",
         {"slack": "chat.postMessage", "params": {"channel": "C_ARCH", "text": "hello"}}),
        ("state precondition", "invite someone to an archived channel",
         {"slack": "conversations.invite", "params": {"channel": "C_ARCH", "users": "U_LEO"}}),
        ("missing permission", "edit another user's message",
         {"slack": "chat.update", "params": {"channel": "C_LIVE", "ts": "@m_priya", "text": "Standup moved to 11."}}),
        ("missing permission", "delete another user's message",
         {"slack": "chat.delete", "params": {"channel": "C_LIVE", "ts": "@m_priya"}}),
        ("limit", "rename a channel to a name with spaces and capitals",
         {"slack": "conversations.rename", "params": {"channel": "C_LIVE", "name": "Payments Old"}}),
    ],
    "calendar": [
        ("missing permission", "rename a calendar the actor can only write to",
         {"method": "PATCH", "path": "/calendars/maya-team@northwind.example", "body": {"summary": "Design team"}}),
        ("missing permission", "read a calendar's sharing rules as a writer",
         {"method": "GET", "path": "/calendars/maya-team@northwind.example/acl"}),
        ("missing permission", "change an event on a read-only calendar",
         {"method": "PATCH", "path": "/calendars/leo-oncall@northwind.example/events/ev_leo",
          "body": {"summary": "On-call handoff (moved)"}}),
        ("read-only field", "change an event's organizer by patching it",
         {"method": "PATCH", "path": f"/calendars/{A}/events/ev_maya",
          "body": {"organizer": {"email": A}}}),
    ],
    "linear": [
        ("read-only field", "change an issue's identifier",
         {"graphql": "mutation { issueUpdate(id: \"i-web-1\", input: {identifier: \"WEB-100\"}) { success } }"}),
        ("state precondition", "archive a workflow state that still has issues",
         {"graphql": "mutation { workflowStateArchive(id: \"t-web-st-1\") { success } }"}),
        ("limit", "set a priority outside 0-4",
         {"graphql": "mutation { issueUpdate(id: \"i-web-1\", input: {priority: 7}) { issue { id priority } } }"}),
    ],
    "box": [
        ("state precondition", "delete a folder that is not empty, without recursive",
         {"method": "DELETE", "path": "/folders/6100"}),
        ("read-only field", "change a file's modified time",
         {"method": "PUT", "path": "/files/6101", "body": {"modified_at": "2026-01-01T00:00:00Z"}}),
        ("read-only field", "change a file's owner by updating it",
         {"method": "PUT", "path": "/files/6102", "body": {"owned_by": {"id": "30000000001"}}}),
    ],
}


def changed(before: dict, after: dict) -> dict:
    out = {}
    for table in set(before) | set(after):
        b, a = before.get(table) or [], after.get(table) or []
        if json.dumps(b, sort_keys=True, default=str) != json.dumps(a, sort_keys=True, default=str):
            out[table] = {"before_rows": len(b), "after_rows": len(a)}
    return out


def main():
    from agent_diff import AgentDiff
    client, engine, results = AgentDiff(base_url=BASE), engine_for(DB), []
    for domain, calls in CALLS.items():
        seed, refs, actor = seedops.expand(domain, SEEDS[domain])
        case = {"case_id": f"BND-PROBE-{domain}", "domain": domain, "seed": seed, "acting_user_id": actor,
                "references": [], "prompt": "probe"}
        if domain == "slack":
            template = runtime.install_template(case, engine)
        else:
            metadata = smoke.load_seed_module(domain).Base.metadata
            template = custom_runtime.install_custom_template(domain, seed, engine, case["case_id"])
        try:
            for cls, what, call in calls:
                call = seedops.resolve(call, refs)
                with ddl_lock():
                    env = client.init_env(templateService=domain, templateName=template["template_name"],
                                          impersonateUserId=actor)
                schema = environment_schema(engine, env.environmentId, template["template_id"])
                export = (lambda: runtime.export_state(engine, schema)) if domain == "slack" else \
                    (lambda: smoke.export_state(engine, schema, metadata))
                before = export()
                status, body = perform_write(client, env.environmentId, domain, call)
                after = export()
                results.append({"domain": domain, "class": cls, "what": what, "call": call, "status": status,
                                "body": json.dumps(body, default=str)[:700], "state_changed": changed(before, after)})
                print(f"{domain:8} {cls:20} {what:55} -> {status} {json.dumps(body, default=str)[:140]} "
                      f"changed={list(changed(before, after))}")
                with ddl_lock():
                    client.delete_env(envId=env.environmentId)
        finally:
            if domain == "slack":
                runtime.cleanup(template, DB)
            else:
                smoke.cleanup_isolated_template({**template, "service": domain}, DB)
    (HERE / "probes.json").write_text(json.dumps(results, indent=1) + "\n")
    engine.dispose()


if __name__ == "__main__":
    main()
