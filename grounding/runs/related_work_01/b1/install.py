"""B1, step 3: put an item's mask into an OpenClaw state directory (the skill documentation and the curl on PATH).

Used by run.py after the runtime builds a trial's state directory (the judge layout: a neutral agent, the curl shim
at state/bin/curl). Two changes, nothing else:
- **the documentation:** each masked operation's section is removed from the agent's skill (for Google Calendar,
  from its references/ file and from the endpoint index in SKILL.md). Operations the skill never documented (several
  Linear mutations, Box's task update) have nothing to remove; the agent knows them from elsewhere.
- **the curl:** the shim moves to state/lib/curl, and state/bin/curl becomes mask_curl.py with the item's rules. A
  masked call gets the answer a service gives for an operation it does not have (Slack unknown_method, Box 405,
  Google 404, a GraphQL validation error) and never reaches the backend; any other call goes to the shim unchanged.
  Linear introspection answers leave out the masked mutations.

The installed wrapper names only operations: no benchmark, study or mask names (the runtime's leak check).
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

HERE = Path(__file__).parent


def remove_section(text: str, heading: str) -> tuple[str, int]:
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.S | re.M)
    new, n = pattern.subn("", text)
    return new, n


def mask_skills(skills: Path, docs: list[list[str]]) -> list[dict]:
    """Remove each (skill, heading) section; returns what was removed, and fails if a documented one is not found."""
    removed = []
    for skill, heading in docs:
        base = skills / skill
        hits = 0
        for path in sorted(base.rglob("*.md")):
            text = path.read_text()
            new, n = remove_section(text, heading)
            if skill == "google-calendar" and path.name == "SKILL.md":  # the endpoint index lists it too
                new = re.sub(rf"(?<=: |; ){re.escape(heading)}(; )?", "", new).replace("; \n", "\n")
            if new != text:
                path.write_text(new)
                removed.append({"file": str(path.relative_to(skills)), "heading": heading,
                                "chars": len(text) - len(new)})
                hits += n
        if not hits:
            raise ValueError(f"{skill}: no section '## {heading}' to remove")
        leftover = [str(p) for p in base.rglob("*.md") if heading in p.read_text()]
        if leftover:
            raise ValueError(f"{skill}: '{heading}' still appears in {leftover}")
    return removed


def wrapper_source(rules: list, base: Path) -> str:
    src = (HERE / "mask_curl.py").read_text()
    return src.replace("__RULES__", json.dumps(rules)).replace("__BASE__", json.dumps(str(base)))


def apply_mask(state: Path, config: dict, item: dict) -> dict:
    agent_id = config["agents"]["list"][0]["id"]
    workspace = state / f"workspace-{agent_id}"
    removed = mask_skills(workspace / "skills", item["docs"])
    shim, lib = state / "bin" / "curl", state / "lib" / "curl"
    if not shim.exists():
        raise ValueError("no curl shim in the state directory: B1 runs need the judge layout (neutral)")
    lib.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(shim), str(lib))
    shim.write_text(wrapper_source(item["refuse"], lib))
    shim.chmod(0o755)
    return {"docs_removed": removed, "refused": item["refuse"]}
