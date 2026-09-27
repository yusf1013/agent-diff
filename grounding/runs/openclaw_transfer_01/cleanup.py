"""Remove AgentDiff environments and templates left by interrupted attempts of one run directory.

    python -m grounding.runs.openclaw_transfer_01.cleanup runs/<run> [--apply]

Only templates named in the run's own environment/preflight/prepared.json files are touched.
Evidence on disk is never modified.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--database-url", default="postgresql://postgres@127.0.0.1:15432/agentdiff_campaign")
    parser.add_argument("--base-url", default="http://127.0.0.1:18001")
    args = parser.parse_args()
    os.environ.setdefault("DATABASE_URL", args.database_url)
    from sqlalchemy import create_engine, text
    from agent_diff import AgentDiff
    from grounding.integrations.openclaw.runtime import cleanup_template
    prepared = {}
    for path in args.run.glob("*/attempt-*/environment/preflight/prepared.json"):
        spec = json.loads(path.read_text())
        case = json.loads((path.parents[2] / "case.json").read_text())
        prepared[spec["template_name"]] = (spec, case)
    engine = create_engine(args.database_url)
    with engine.connect() as conn:
        live = set(conn.execute(text("select name from public.environments")).scalars().all())
        stale = {name: v for name, v in prepared.items() if name in live}
        envs = {name: conn.execute(text(
            "select r.id from public.run_time_environments r join public.environments t on t.id = r.template_id "
            "where t.name = :n and r.status != 'deleted'"), {"n": name}).scalars().all() for name in stale}
    engine.dispose()
    print(f"templates recorded by this run: {len(prepared)}; still present: {len(stale)}; "
          f"active environments on them: {sum(len(v) for v in envs.values())}")
    if not args.apply:
        return
    client = AgentDiff(base_url=args.base_url)
    for name, (spec, case) in stale.items():
        for env_id in envs[name]:
            client.delete_env(envId=str(env_id))
        cleanup_template(case if "domain" in case else {**case, "domain": "slack"}, spec, args.database_url)
        print("removed", name)


if __name__ == "__main__":
    main()
