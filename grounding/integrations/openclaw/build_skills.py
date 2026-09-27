"""Build the OpenClaw skills that give the agent the toy harness's API documentation.

    python3 -m grounding.integrations.openclaw.build_skills [--install WORKSPACE]

Each SKILL.md carries, verbatim, the parts of the toy harness's system prompt that
describe the service (REACT_SYSTEM_PROMPT_WITH_API_DOCS as assembled by
smoke_runtime.official_prompt): the Current Session block (service, base URL,
description), the environment lines that still hold in OpenClaw, and the full
API documentation. Left out: the XML response protocol and loop rules (OpenClaw
has native tool calls), the "stateless between commands" line (untrue in
OpenClaw), and Calendar's current-date line (the harness clock provides the date).

The agent calls the real API base URLs with a placeholder token, as in the toy
harness; bin/curl rewrites them to the run's AgentDiff environment.

OpenClaw's read tool returns at most ~15,900 characters per call. A skill whose
single file would exceed SPLIT_AT (only Google Calendar, 38,923 characters) keeps
the header and an endpoint index in SKILL.md and moves the verbatim endpoint
documentation into references/<resource>.md files, each within one read (the
usual layout for large skills). The documentation text is unchanged.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from grounding.integrations.agentdiff import smoke_runtime as smoke

HERE = Path(__file__).resolve().parent
SKILLS = HERE / "skills"
# OpenClaw skill name -> toy harness service key
SERVICES = {"slack": "slack", "box": "box", "google-calendar": "calendar", "linear": "linear"}


def section(prompt: str, title: str) -> str:
    match = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", prompt, re.S | re.M)
    if not match:
        raise ValueError(f"toy prompt has no '## {title}' section")
    return match.group(1)


SPLIT_AT = 15000   # characters; OpenClaw's read tool truncates at ~15,900
REFERENCE_MAX = 12000


def resource(endpoint: str) -> str:
    """Reference file for a REST endpoint heading such as 'GET /calendars/{calendarId}/events'."""
    path = endpoint.split(" ", 1)[1]
    for prefix, name in (("/calendars/{calendarId}/events", "events"), ("/calendars/{calendarId}/acl", "acl"),
                         ("/users/me/calendarList", "calendar-list"), ("/calendars", "calendars")):
        if path.startswith(prefix):
            return name
    return "other"


def split_docs(docs: str) -> dict[str, list[tuple[str, str]]]:
    """Group verbatim endpoint sections by resource, splitting a group that would exceed one read."""
    sections = re.split(r"(?m)^(?=## )", docs)
    groups: dict[str, list[tuple[str, str]]] = {}
    for sec in sections:
        if not sec.strip():
            continue
        heading = sec.splitlines()[0][3:].strip()
        groups.setdefault(resource(heading), []).append((heading, sec.rstrip() + "\n"))
    files: dict[str, list[tuple[str, str]]] = {}
    for name, items in groups.items():
        part, size, parts = [], 0, []
        for heading, text in items:
            if part and size + len(text) > REFERENCE_MAX:
                parts.append(part)
                part, size = [], 0
            part.append((heading, text))
            size += len(text) + 1
        parts.append(part)
        for i, p in enumerate(parts, 1):
            files[name if len(parts) == 1 else f"{name}-{i}"] = p
    return files


def build(skill: str, service: str) -> dict[str, str]:
    """Return {relative path: content} for the skill directory."""
    prompt = smoke.official_prompt(service)
    session = [line for line in section(prompt, "Current Session").splitlines()
               if line.startswith(("- **Service**", "- **Base URL**", "- **Description**"))]
    environment = [line for line in section(prompt, "Environment").splitlines()
                   if line.startswith("- ") and "stateless" not in line]
    docs = prompt.split("## API Documentation\n", 1)[1].rstrip() + "\n"
    name = session[0].split(":", 1)[1].strip()
    description = session[2].split(":", 1)[1].strip()
    front = (f"---\nname: {skill}\n"
             f'description: "{description}. Use it for anything in the user\'s {name} account."\n'
             'metadata: {"openclaw": {"requires": {"bins": ["curl"]}}}\n---\n')
    head = (f"# {name}\n\n## Current Session\n" + "\n".join(session) + "\n\n## Environment\n"
            + "\n".join(environment) + "\n\n## API Documentation\n")
    single = front + "\n" + head + docs
    if len(single) <= SPLIT_AT:
        return {"SKILL.md": single}
    files = split_docs(docs)
    index = ["The endpoint documentation is split by resource into the files below (in this skill's "
             "`references/` folder). Read the file for the resource you need.", ""]
    out = {}
    for file, items in files.items():
        index.append(f"- `references/{file}.md`: " + "; ".join(h for h, _ in items))
        out[f"references/{file}.md"] = f"# {name} API: {file}\n\n" + "\n".join(t for _, t in items)
    out["SKILL.md"] = front + "\n" + head + "\n".join(index) + "\n"
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", type=Path, help="copy the built skills into WORKSPACE/skills")
    args = parser.parse_args()
    for skill, service in SERVICES.items():
        if (SKILLS / skill).exists():
            shutil.rmtree(SKILLS / skill)
        for rel, content in build(skill, service).items():
            path = SKILLS / skill / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(f"{path.relative_to(HERE)}: {len(content)} chars")
    if args.install:
        target = args.install / "skills"
        for skill in SERVICES:
            if (target / skill).exists():
                shutil.rmtree(target / skill)
            shutil.copytree(SKILLS / skill, target / skill)
        print(f"installed into {target}")


if __name__ == "__main__":
    main()
