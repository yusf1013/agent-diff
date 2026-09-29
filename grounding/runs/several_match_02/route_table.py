"""The route table (method.md, input 3), the shortcuts generated from it, and a comparison with the hand-coded ones.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.several_match_02.route_table

ROUTES records, per service, the operations that list or search the records a plural request is about, read from
the replica code: the container listing (with its visibility default and the flags that narrow it), the record
listing (per container or per workspace, with its default and largest page), the hierarchy between containers,
and the search (its page, and what it can express).

`generate` applies each behaviour's rule to those entries, with nothing specific to a service:
- scope: read one container only (the named, default or guessed one), at each page size, or every page of it;
- pages: walk every container, but read one page of each; or take a workspace listing's first page;
- visibility: list the containers with the default visibility, or a narrowing flag, then read each;
- filter: search with words that do not express the condition, at each page size; or search on another expressible
  field under the scope;
- selection: fetch every record, then keep only the named container.
ALIAS maps each hand-coded shortcut (strategies.py) to the generated one it is. The report lists the hand-coded
shortcuts no rule generates (a gap in the rules) and the generated ones never hand-coded (shortcuts the
investigation did not try).
"""
from __future__ import annotations

import json
from pathlib import Path

from grounding.runs.several_match_02 import strategies

HERE = Path(__file__).resolve().parent

ROUTES = {
    "box": {
        "record_list": {"call": "folder items", "per": "container", "page": (100, 1000)},
        "hierarchy": "subfolders",
        "search": {"call": "search", "page": (30, 200), "expresses": ["words", "extension", "a person's name"],
                   "scoped_by": "ancestor folder"},
    },
    "calendar": {
        "container_list": {"call": "calendar list", "visibility_flag": "showHidden", "narrowing": ["owner only"]},
        "record_list": {"call": "events", "per": "container", "page": (250, 2500), "default_container": "primary"},
        "search": {"call": "events q", "page": (250, 2500), "expresses": ["words"], "scoped_by": "one calendar"},
    },
    "linear": {
        "record_list": {"call": "issues", "per": "workspace", "page": (50, None), "container_attr": "team",
                        "filters": ["team", "assignee", "state", "labels", "creator", "title"]},
        "hierarchy": "sub-teams",
    },
    "slack": {
        "container_list": {"call": "conversation list", "visibility_flag": "types", "narrowing": ["exclude archived"]},
        "record_list": {"call": "history", "per": "container", "page": (100, 999)},
        "search": {"call": "message search", "page": (20, 100), "expresses": ["words", "from:", "in:"],
                   "scoped_by": "in:"},
    },
}


def generate(service: str) -> list[tuple[str, str]]:
    r, out = ROUTES[service], []
    rl, cl, s, h = r["record_list"], r.get("container_list"), r.get("search"), r.get("hierarchy")
    small, large = rl["page"]
    if rl["per"] == "container":
        out += [("scope", f"one container's {rl['call']}, first page ({small})"),
                ("scope", f"one container's {rl['call']}, first page ({large})"),
                ("scope", f"one container's {rl['call']}, every page")]
        if h:
            out.append(("pages", f"every container through {h}, one page ({large}) of each"))
        if cl:
            out += [("visibility", f"{cl['call']} (default visibility) -> {rl['call']} of each")]
            out += [("visibility", f"{cl['call']} ({n}) -> {rl['call']} of each") for n in cl["narrowing"]]
            out.append(("pages", f"{cl['call']} (every visibility) -> one page ({large}) of {rl['call']} of each"))
    else:  # a workspace listing with a container attribute
        out += [("pages", f"every {rl['call']}, first page ({small})"),
                ("pages", f"every {rl['call']}, first page (250)"),
                ("pages", f"every {rl['call']}, first page (1000)"),
                ("scope", f"{rl['call']} filtered on the named {rl['container_attr']}, first page (250)"),
                ("scope", f"{rl['call']} filtered on every condition, first page (250)"),
                ("selection", f"every {rl['call']} (1000) -> keep the named {rl['container_attr']}")]
    if s:
        out += [("filter", f"{s['call']} with the request's words, first page ({small_or(s)})"),
                ("filter", f"{s['call']} with the request's words, first page ({s['page'][1]})")]
        out += [("filter", f"{s['call']} on {what}, under the {s['scoped_by']}, first page ({s['page'][1]})")
                for what in s["expresses"]]
    return out


def small_or(s):
    return s["page"][0]


ALIAS = {  # hand-coded shortcut (strategies.py) -> the generated shortcut it is
    ("box", "list named (default page)"): "one container's folder items, first page (100)",
    ("box", "list named (limit 1000)"): "one container's folder items, first page (1000)",
    ("box", "list named, every page (limit 1000)"): "one container's folder items, every page",
    ("box", "list tree, one page per folder (limit 1000)"): "every container through subfolders, one page (1000) of each",
    ("box", "search words (default limit)"): "search with the request's words, first page (30)",
    ("box", "search words under folder (limit 200)"): "search on words, under the ancestor folder, first page (200)",
    ("box", "search extension under folder (limit 200)"):
        "search on extension, under the ancestor folder, first page (200)",
    ("box", "search person's name under folder (limit 200)"):
        "search on a person's name, under the ancestor folder, first page (200)",
    ("calendar", "primary only"): "one container's events, first page (250)",
    ("calendar", "primary, text search"): "events q with the request's words, first page (250)",
    ("calendar", "calendar list (default) -> each"): "calendar list (default visibility) -> events of each",
    ("calendar", "calendar list (owner only) -> each"): "calendar list (owner only) -> events of each",
    ("linear", "all issues (default page)"): "every issues, first page (50)",
    ("linear", "all issues (first 250)"): "every issues, first page (250)",
    ("linear", "all issues (first 1000)"): "every issues, first page (1000)",
    ("linear", "named team's issues (first 250)"): "issues filtered on the named team, first page (250)",
    ("linear", "server filter, all conditions (first 250)"): "issues filtered on every condition, first page (250)",
    ("linear", "all issues (first 1000) -> keep the named team"): "every issues (1000) -> keep the named team",
    ("slack", "named channel history (default)"): "one container's history, first page (100)",
    ("slack", "named channel history (limit 999)"): "one container's history, first page (999)",
    ("slack", "named channel history, every page (limit 999)"): "one container's history, every page",
    ("slack", "channel list (default types) -> history"): "conversation list (default visibility) -> history of each",
    ("slack", "channel list (exclude archived) -> history"): "conversation list (exclude archived) -> history of each",
    ("slack", "channel list (public+private) -> one page of history"):
        "conversation list (every visibility) -> one page (999) of history of each",
    ("slack", "search words (default count)"): "message search with the request's words, first page (20)",
    ("slack", "search words (count 100)"): "message search with the request's words, first page (100)",
    # the other two kinds of Slack request, over the same routes
    ("slack", "conversations (default types) -> history"): "conversation list (default visibility) -> history of each",
    ("slack", "conversations (public+private) -> history"):
        "conversation list (every visibility) -> one page (999) of history of each",
    ("slack", "search words -> channels of the hits"): "message search with the request's words, first page (100)",
    ("slack", "channel list (default types) -> topics"): "conversation list (default visibility) -> history of each",
}


def main():
    tables = {"box": ["box"], "calendar": ["calendar"], "linear": ["linear"],
              "slack": ["slack", "slack-channels", "slack-messages"]}
    report = {}
    for service, names in tables.items():
        hand = sorted({n for t in names for n, (thorough, _f) in strategies.STRATEGIES[t].items() if not thorough})
        gen = {name for _b, name in generate(service)}
        unmatched = [n for n in hand if ALIAS.get((service, n)) not in gen]
        used = {ALIAS[(service, n)] for n in hand if (service, n) in ALIAS}
        report[service] = {"hand-coded": len(hand), "generated": len(gen),
                           "hand-coded with no generated match": unmatched,
                           "generated, never hand-coded": sorted(gen - used)}
        print(f"== {service}: hand-coded {len(hand)}, generated {len(gen)}, hand-coded unmatched {len(unmatched)}")
        for n in unmatched:
            print(f"   unmatched: {n}")
        for g in sorted(gen - used):
            print(f"   generated, never hand-coded: {g}")
    (HERE / "route_table.json").write_text(json.dumps({"routes": ROUTES, "comparison": report}, indent=1) + "\n")


if __name__ == "__main__":
    main()
