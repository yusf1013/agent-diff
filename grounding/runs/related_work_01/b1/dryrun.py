"""B1's check without a model: a real state directory with an item's mask, and its curl, against a live environment.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.b1.dryrun

For one item per service (and Linear's upserting attachmentCreate), exactly as run.py would set a trial up:
build the neutral state directory (runtime.build_state_dir; no model is called), install the mask (install.py), install
the item's seed and open an environment (runtime.prepare), then call the installed curl the way an agent would:
- the masked operation, in several spellings (-X / --request / -XPATCH, -d @file, --json, -sS, -f, -w, -i): each must get
  the service's "no such operation" answer and never reach the backend;
- a read of the target afterwards: it must be unchanged;
- an open operation: it must pass through the shim to the environment;
- for Linear, introspection: the masked mutations must be gone, the others there.
The documentation check: the masked sections are gone from the workspace's skill. Writes dryrun.json.
"""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path

from grounding.integrations.agentdiff.runtime import ddl_lock
from grounding.integrations.openclaw import runtime as oc
from grounding.runs.related_work_01.b1.install import apply_mask
from grounding.runs.related_work_01.b1.masks import attempt as source_attempt

HERE = Path(__file__).parent
DB = os.environ.get("DATABASE_URL", "postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
BASE = "http://127.0.0.1:18001"
B = "https://api.box.com/2.0"
C = "https://www.googleapis.com/calendar/v3"
L = "https://api.linear.app/graphql"
S = "https://slack.com/api"
AUTH = ["-H", "Authorization: Bearer <TOKEN>"]
JSON = ["-H", "Content-Type: application/json"]


def gql(q):
    return json.dumps({"query": q})


# item -> list of (label, curl args, expectation). Expectations: refused (the service's answer), passes (the backend
# answered), unchanged (the read shows the original value), absent/present (introspection).
PLAN = {
    "AP-BOX-02": [
        ("masked: PUT, -X", ["-s", "-X", "PUT", f"{B}/files/8201", *AUTH, *JSON, "-d", '{"tags":["needs-legal-review"]}'], "refused 405"),
        ("masked: PUT, --request=, -w", ["-sS", "--request=PUT", f"{B}/files/8201", *AUTH, "--json",
                                         '{"tags":["x"]}', "-w", "\\n%{http_code}"], "refused 405"),
        ("masked: PUT, -f", ["-sf", "-XPUT", f"{B}/files/8201", *AUTH, "-d", "{}"], "exit 22"),
        ("read the target", ["-s", f"{B}/files/8201", *AUTH], "unchanged tags"),
        ("open: list the root", ["-s", f"{B}/folders/0/items", *AUTH], "passes"),
    ],
    "AR-CAL-21": [
        ("masked: PATCH", ["-s", "-X", "PATCH", f"{C}/calendars/primary/events/jbdvmavve54iqhlkogbod4v41v", *AUTH,
                           *JSON, "-d", '{"location":"Room 4C"}'], "refused 404"),
        ("masked: PUT (the same change)", ["-s", "-XPUT", f"{C}/calendars/primary/events/jbdvmavve54iqhlkogbod4v41v",
                                           *AUTH, *JSON, "-d", '{"location":"Room 4C"}', "-i"], "refused 404"),
        ("read the target", ["-s", f"{C}/calendars/primary/events/jbdvmavve54iqhlkogbod4v41v", *AUTH],
         "unchanged location"),
        ("open: calendar list", ["-s", f"{C}/users/me/calendarList", *AUTH], "passes"),
    ],
    "AP2-LIN-01": [
        ("masked: issueUpdate, -d @file", ["-s", L, *AUTH, *JSON, "-d", "@{tmp}/q.json"], "refused 400"),
        ("masked: issueBatchUpdate", ["-s", L, *AUTH, *JSON, "-d", gql(
            'mutation { issueBatchUpdate(ids: ["35a6986c-7034-4f07-b91a-a0b08601d74e"], input: {priority: 1}) '
            '{ success } }')], "refused 400"),
        ("read the target", ["-s", L, *AUTH, *JSON, "-d", gql(
            '{ issue(id: "35a6986c-7034-4f07-b91a-a0b08601d74e") { priority } }')], "unchanged priority"),
        ("open: teams", ["-s", L, *AUTH, *JSON, "-d", gql("{ teams { nodes { id name } } }")], "passes"),
        ("introspection", ["-s", L, *AUTH, *JSON, "-d", gql('{ __type(name: "Mutation") { fields { name } } }')],
         "absent issueUpdate issueBatchUpdate; present issueCreate commentCreate"),
    ],
    "AP-LIN-06": [
        ("masked: attachmentCreate (it updates by URL)", ["-s", L, *AUTH, *JSON, "--data-raw", gql(
            'mutation { attachmentCreate(input: {issueId: "WEB-14", url: "https://runbooks.northwind.example/'
            'deploy-staging", title: "Deploy runbook (v2)"}) { success } }')], "refused 400"),
        ("masked: attachmentUpdate, stdin", ["-s", L, *AUTH, *JSON, "-d", "@-"], "refused 400"),
    ],
    "AP-SLK-01": [
        ("masked: reactions.add", ["-s", "-X", "POST", f"{S}/reactions.add", *AUTH, "-d",
                                   "channel=C0&name=tada&timestamp=1772377200.000001"], "refused 200"),
        ("masked: reactions.add, GET", ["-s", f"{S}/reactions.add?name=tada&timestamp=1772377200.000001", *AUTH],
         "refused 200"),
        ("open: auth.test", ["-s", "-X", "POST", f"{S}/auth.test", *AUTH], "passes"),
    ],
}
STDIN = {("AP-LIN-06", "masked: attachmentUpdate, stdin"): gql(
    'mutation { attachmentUpdate(id: "58dd7492-0dde-49bb-b4db-f9b063082ab9", input: {title: "x"}) { success } }')}
FILES = {"AP2-LIN-01": {"q.json": gql('mutation { issueUpdate(id: "35a6986c-7034-4f07-b91a-a0b08601d74e", '
                                      'input: {priority: 1}) { success } }')}}


def check(expect: str, out: str, code: int, before: dict) -> tuple[bool, str]:
    if expect.startswith("refused"):
        status = expect.split()[1]
        if status == "200":
            return '"unknown_method"' in out, "Slack unknown_method"
        if status == "400":
            return "Cannot query field" in out, "GraphQL validation error"
        return (('"status": 405' in out) if status == "405" else ('"code": 404' in out)) and code == 0, f"HTTP {status}"
    if expect == "exit 22":
        return code == 22 and not out, "curl --fail exit 22"
    if expect == "passes":
        try:
            body = json.loads(out)
        except ValueError:
            return False, "not JSON"
        return not ("error" in body and body.get("ok") is not True and "errors" not in body and "data" not in body) \
            and '"unknown_method"' not in out and "Cannot query field" not in out, "answered by the backend"
    if expect.startswith("unchanged"):
        col = expect.split()[1]
        return before.get(col) is not None and before[col] in out, f"{col} still {before.get(col)!r}"
    if expect.startswith("absent"):
        absent, present = expect[len("absent "):].split("; present ")
        names = {f["name"] for f in json.loads(out)["data"]["__type"]["fields"]}
        return (not (set(absent.split()) & names) and set(present.split()) <= names), \
            f"{len(names)} mutations listed"
    raise ValueError(expect)


def main():
    from agent_diff import AgentDiff
    from grounding.runs.related_work_01.b1.masks import CAPABILITIES  # noqa: F401
    items = {i["case_id"]: i for i in json.loads((HERE / "items.json").read_text()) if i["verdict"] == "valid"}
    client, results = AgentDiff(base_url=BASE), {}
    root = Path(tempfile.mkdtemp(prefix="b1-dryrun-", dir=os.environ.get("TMPDIR")))
    for cid, calls in PLAN.items():
        item = items[cid]
        case = json.loads((source_attempt(item["run"], "t1", cid) / "case.json").read_text())
        state = root / cid
        state.mkdir(parents=True)
        config = oc.build_state_dir(state, "dryrun", case["domain"], None, "selfhost", neutral=True)
        mask = apply_mask(state, config, item)
        workspace = state / f"workspace-{config['agents']['list'][0]['id']}"
        docs_gone = all(h not in p.read_text() for _s, h in item["docs"] for p in (workspace / "skills").rglob("*.md"))
        prepared = oc.prepare(case, root / f"{cid}-prep", DB, BASE)
        with ddl_lock():
            env = client.init_env(templateService=case["domain"], templateName=prepared["template_name"],
                                  impersonateUserId=case["acting_user_id"])
        try:
            tmp = root / f"{cid}-files"
            tmp.mkdir()
            for name, text in FILES.get(cid, {}).items():
                (tmp / name).write_text(text)
            envv = {"PATH": f"{state / 'bin'}:/usr/bin:/bin", "HOME": str(Path.home()), "SVC_BASE_URL": BASE,
                    "SVC_ENV_ID": env.environmentId}
            before = {}
            if item["F"]["kind"] == "field":
                initial = json.loads(Path(prepared["initial_state_path"]).read_text())
                kc = {"channels": "channel_id", "messages": "message_id"}.get(item["F"]["table"], "id")
                row = next(r for r in initial[item["F"]["table"]] if str(r.get(kc)) == item["F"]["key"])
                before = {k: (json.dumps(v)[1:-1] if isinstance(v, str) else json.dumps(v)) for k, v in row.items()}
            rows = []
            for label, args, expect in calls:
                args = [a.replace("{tmp}", str(tmp)) for a in args]
                done = subprocess.run([str(state / "bin" / "curl"), *args], env=envv, capture_output=True, text=True,
                                      input=STDIN.get((cid, label), ""), timeout=120)
                ok, what = check(expect, done.stdout, done.returncode, before)
                rows.append({"call": label, "expect": expect, "ok": ok, "what": what, "exit": done.returncode,
                             "stdout": done.stdout[:300]})
                print(f"{cid:<11} {'OK ' if ok else 'BAD'} {label:<44} {what}")
            results[cid] = {"capability": item["capability"], "docs_removed": mask["docs_removed"],
                            "docs_gone": docs_gone, "calls": rows}
        finally:
            with ddl_lock():
                client.delete_env(envId=env.environmentId)
            oc.cleanup_template(case, prepared, DB)
    (HERE / "dryrun.json").write_text(json.dumps(results, indent=1) + "\n")
    bad = [(c, r["call"]) for c, v in results.items() for r in v["calls"] if not r["ok"]]
    print(f"{sum(len(v['calls']) for v in results.values())} calls, {len(bad)} not as expected; docs removed in all: "
          f"{all(v['docs_gone'] for v in results.values())}")


if __name__ == "__main__":
    main()
