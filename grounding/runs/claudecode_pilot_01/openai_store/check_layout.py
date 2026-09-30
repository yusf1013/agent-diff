"""Check the AGENTDIFF_OPENAI_STORE change to grounding/integrations/openclaw/runtime.py without running OpenClaw:

1. With the variable unset, the new runtime.py builds exactly what the committed one (BASE, a git revision) builds:
   the same files with the same bytes (the copied login store compared by its SQL dump, since two backups of one
   database may differ in header bytes) and the same openclaw.json.
2. With AGENTDIFF_OPENAI_STORE=main, the layout: the login store in agents/main/agent (owned by agent "main"), no
   store in the attempt agent's directory, the model catalog in both.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.claudecode_pilot_01.openai_store.check_layout [BASE]

Writes layout_check.json next to this file. No model call; the login store is read the way a run reads it.
"""
import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import types
from pathlib import Path

from grounding.paths import REPO_ROOT

HERE = Path(__file__).resolve().parent
RUNTIME = "grounding/integrations/openclaw/runtime.py"


def load(source: str, name: str):
    """A module from source text whose __file__ is the real runtime.py, so its paths (skills, shim, clock) resolve."""
    module = types.ModuleType(f"grounding.integrations.openclaw.{name}")
    module.__file__ = str(REPO_ROOT / RUNTIME)
    exec(compile(source, module.__file__, "exec"), module.__dict__)
    return module


def sql_owner(db: Path) -> dict:
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        row = con.execute("SELECT role, agent_id FROM schema_meta WHERE meta_key = 'primary'").fetchone()
        dump = "\n".join(con.iterdump())
    finally:
        con.close()
    return {"owner": {"role": row[0], "agent_id": row[1]} if row else None,
            "dump_sha256": hashlib.sha256(dump.encode()).hexdigest()}


def tree(state: Path) -> dict:
    out = {}
    for path in sorted(p for p in state.rglob("*") if p.is_file()):
        rel = str(path.relative_to(state))
        if path.suffix == ".sqlite":
            out[rel] = {"sqlite": sql_owner(path)}
        else:
            out[rel] = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    return out


def build(module, state: Path) -> dict:
    if state.exists():
        shutil.rmtree(state)
    state.mkdir(parents=True)
    config = module.build_state_dir(state, "route0", "slack", backend="openai", neutral=True)
    return {"tree": tree(state), "config": config}


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    old_src = subprocess.run(["git", "show", f"{base}:{RUNTIME}"], capture_output=True, text=True, cwd=REPO_ROOT,
                             check=True).stdout
    new_src = (REPO_ROOT / RUNTIME).read_text()
    old, new = load(old_src, "runtime_base"), load(new_src, "runtime_new")
    state = Path.home() / ".openclaw-state" / "layout-check"  # the same path for every build, so paths match
    os.environ.pop("AGENTDIFF_OPENAI_STORE", None)
    try:
        base_build = build(old, state)
        new_default = build(new, state)
        os.environ["AGENTDIFF_OPENAI_STORE"] = "main"
        new_main = build(new, state)
    finally:
        os.environ.pop("AGENTDIFF_OPENAI_STORE", None)
        shutil.rmtree(state, ignore_errors=True)
    same = base_build == new_default
    agent = "assistant"
    result = {
        "base": base, "runtime_sha256": {"base": hashlib.sha256(old_src.encode()).hexdigest(),
                                         "new": hashlib.sha256(new_src.encode()).hexdigest()},
        "default_path_identical": same,
        "default_differences": [] if same else sorted(set(base_build["tree"]) ^ set(new_default["tree"])) or
        [k for k in base_build["tree"] if base_build["tree"][k] != new_default["tree"].get(k)] or ["config"],
        "default_tree": new_default["tree"],
        "main_layout_tree": new_main["tree"],
        "main_layout_checks": {
            "main_store_owner": new_main["tree"].get("agents/main/agent/openclaw-agent.sqlite", {}).get("sqlite", {}).get("owner"),
            "attempt_agent_has_no_store": f"agents/{agent}/agent/openclaw-agent.sqlite" not in new_main["tree"],
            "catalog_in_main": "agents/main/agent/plugins/openai/catalog.json" in new_main["tree"],
            "catalog_in_attempt_agent": f"agents/{agent}/agent/plugins/openai/catalog.json" in new_main["tree"],
            "config_same_as_default": new_main["config"] == new_default["config"]}}
    (HERE / "layout_check.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("default_tree", "main_layout_tree")}, indent=1))


if __name__ == "__main__":
    main()
