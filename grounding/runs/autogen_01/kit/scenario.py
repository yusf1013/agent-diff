"""A writer's scenario.json: format checks, seed expansion, and conversion to the case format the runs use.

    case, problems = build(scenario, brief)

`problems` lists everything the writer must fix, each as one plain sentence. The checks are mechanical:
- format;
- the seed expands and every `@ref` resolves;
- `fdc.check_reference`: the reference selects exactly the target, and every claim is killed by its witness;
- every primary fact of the brief has a decoy;
- every decoy's fact is named by one of the request's conditions;
- anchors survive in every derived no-target test;
- replica rules;
- request lint.

They verify executable properties only. Whether the request means what the query says is the reader's job.
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

from grounding.runs.autogen_01.kit import derive, seedops
from grounding.runs.fact_coverage_01 import fdc
from grounding.runs.fact_coverage_01.pilot.common import finish
from grounding.runs.fact_coverage_02.anchors import missing_anchors

STUDY = Path(__file__).resolve().parents[1]
CATALOG = STUDY.parent / "fact_coverage_01" / "catalog"
FAMILIES = {f"F{i}" for i in range(9)}
MUTATIONS = {"DROP", "SUB", "REPLACE", "SPLIT", "LEVEL"}
SLACK_REACTIONS = {
    "raised_hands", "bow", "thumbsup", "thumbsdown", "clap", "tada", "dart", "joy", "+1", "-1", "eyes", "heart",
    "fire", "rocket", "check", "x", "wave", "pray", "thinking", "shrug", "facepalm", "grimacing", "sweat_smile", "zzz",
    "coffee", "pizza", "finish_flag", "blob_smiley", "alert", "mic-drop", "cool-doge", "thankyou", "party_blob",
    "partyparrot", "this_is_fine", "extreme-teamwork", "done", "loading", "huh", "dumpster-fire", "blob-yes",
    "blob-no", "blob_help", "chefs-kiss", "troll", "1000", "catjam", "keanu-thanks", "art", "honey_pot", "sunrise"}
ESCAPE = re.compile(r"just tell me|if there (isn't|is not|aren't|are not) (one|any)", re.I)


def catalog(domain):
    data = json.loads((CATALOG / f"{domain}.json").read_text())
    return {r["id"]: r for r in data["requirements"]}


def _walk(node, fn, path=()):
    fn(node, path)
    for e in node.get("edges", []):
        _walk(e["node"], fn, path + (e.get("key"),))


def _derived_paths(query):
    tables, rels, ident = [], [], []

    def visit(node, path):
        tables.append(node["table"])
        for f in node.get("filters", []):
            ident.append(f"{node['table']}.{f['field']}")
        for e in node.get("edges", []):
            join = e.get("join") or {}
            rels.append(f"{node['table']}.{join.get('parent')}")
    _walk(query, visit)
    return ([{"entities": sorted(set(tables)), "relationships": sorted(set(rels))}],
            sorted(set(ident + rels)))


def _format(s, brief) -> list[str]:
    p = []
    for key, kind in (("scenario_id", str), ("domain", str), ("request", str), ("answer", str), ("seed", list),
                      ("conditions", list), ("reference", dict), ("write", dict)):
        if not isinstance(s.get(key), kind):
            p.append(f"`{key}` is missing or not a {kind.__name__}.")
    if p:
        return p
    if s["scenario_id"] != brief["scenario_id"] or s["domain"] != brief["domain"]:
        p.append(f"`scenario_id`/`domain` must be {brief['scenario_id']}/{brief['domain']}.")
    if s["answer"] not in ("one", "all"):
        p.append("`answer` must be \"one\" (a single record) or \"all\" (every record that matches).")
    ref = s["reference"]
    for key, kind in (("name", str), ("target", list), ("query", dict), ("decoys", list), ("effect", dict)):
        if not isinstance(ref.get(key), kind):
            p.append(f"`reference.{key}` is missing or not a {kind.__name__}.")
    if p:
        return p
    if not ref["target"]:
        p.append("`reference.target` is empty: the scenario must contain its target.")
    facts = catalog(s["domain"])
    cond_facts = {}
    for i, c in enumerate(s["conditions"]):
        if not (isinstance(c, dict) and isinstance(c.get("id"), str) and isinstance(c.get("text"), str)
                and isinstance(c.get("facts"), list)):
            p.append(f"conditions[{i}] needs `id`, `text` and `facts` (a list).")
            continue
        for fact in c["facts"]:
            if fact not in facts:
                p.append(f"conditions[{i}] names `{fact}`, which is not a fact of the {s['domain']} catalog.")
            cond_facts.setdefault(fact, []).append(c["id"])
    witnesses = []
    for i, d in enumerate(ref["decoys"]):
        where = f"reference.decoys[{i}]"
        if not isinstance(d, dict):
            p.append(f"{where} is not an object.")
            continue
        for key in ("witness", "fact", "family", "mutation", "explanation"):
            if key not in d:
                p.append(f"{where} lacks `{key}`.")
        if d.get("fact") and d["fact"] not in facts:
            p.append(f"{where}: `{d['fact']}` is not a fact of the {s['domain']} catalog.")
        elif d.get("fact") and d["fact"] not in cond_facts:
            p.append(f"{where}: its fact `{d['fact']}` is not listed in any condition's `facts`.")
        if d.get("family") not in FAMILIES:
            p.append(f"{where}: `family` must be one of F0..F8.")
        if not isinstance(d.get("mutation"), dict) or d["mutation"].get("type") not in MUTATIONS:
            p.append(f"{where}: `mutation.type` must be one of {sorted(MUTATIONS)}.")
        witnesses.append(json.dumps(d.get("witness")))
    if len(witnesses) != len(set(witnesses)):
        p.append("Two decoys share a witness; every decoy is a different record.")
    decoy_facts = {d.get("fact") for d in ref["decoys"] if isinstance(d, dict)}
    for fact in brief.get("facts", []):
        if fact not in decoy_facts:
            p.append(f"The brief's fact `{fact}` has no decoy.")
    return p


def _lint(s) -> list[str]:
    p = []
    text = s["request"]
    if ESCAPE.search(text):
        p.append("The request must not contain an escape clause (\"If there isn't one, just tell me\"); the suite "
                 "adds it where needed.")
    if re.search(r"\b[ARHBD]:[A-Za-z_]+\.", text):
        p.append("The request names a catalog fact id; write it as a user would.")
    if len(text) > 420:
        p.append(f"The request is {len(text)} characters; keep it under 420, as a user would write it.")
    return p


def _ids_in_request(case) -> list[str]:
    """Seed ids that appear verbatim in the request (a user would not know internal ids)."""
    words = set(re.findall(r"[A-Za-z0-9_.@:-]+", case["prompt"]))
    found = []
    for rows in case["seed"].values():
        for row in rows:
            for key in ("id", "message_id", "channel_id", "user_id"):
                v = row.get(key)
                if isinstance(v, str) and len(v) >= 3 and v in words and not re.fullmatch(r"[A-Za-z]+", v) \
                        and "@" not in v:
                    found.append(v)
    return sorted(set(found))


def _replica_rules(s, case) -> list[str]:
    p = []
    if s["domain"] == "slack":
        text = json.dumps(s.get("write", {})) + " " + s["request"]
        for name in re.findall(r":([a-z0-9_+\-]+):", s["request"]):
            if name not in SLACK_REACTIONS:
                p.append(f"The Slack replica rejects the reaction `{name}`; use one it accepts (see replica.md).")
        params = (s.get("write") or {}).get("params") or {}
        if (s.get("write") or {}).get("slack") == "reactions.add" and params.get("name") not in SLACK_REACTIONS:
            p.append(f"The write adds reaction `{params.get('name')}`, which the Slack replica rejects.")
    return p


def build(s: dict, brief: dict):
    """(case or None, problems). The case is the scenario as written: target and all decoys present."""
    problems = _format(s, brief)
    if problems:
        return None, problems
    try:
        seed, refs, actor = seedops.expand(s["domain"], s["seed"])
    except seedops.SeedError as exc:
        return None, [f"Seed: {exc}"]
    except Exception as exc:  # a malformed argument the builder did not anticipate
        return None, [f"Seed: {type(exc).__name__}: {exc}"]
    try:
        rest = seedops.resolve({k: v for k, v in s.items() if k != "seed"}, refs)
    except seedops.SeedError as exc:
        return None, [f"Reference outside the seed: {exc}"]
    ref = rest["reference"]
    sid = s["scenario_id"]
    claims = []
    for d in ref["decoys"]:
        c = {"requirement": d["fact"], "witness": d["witness"], "mutation": d["mutation"],
             "explanation": d["explanation"], "family": d["family"]}
        if d.get("substitute"):
            c["alternative"] = d["substitute"]
        claims.append(c)
    paths, identifying = _derived_paths(ref["query"])
    query = copy.deepcopy(ref["query"])
    query.setdefault("key", ["message_id"] if query.get("table") == "messages" and s["domain"] == "slack" else ["id"])
    references = [{
        "id": f"{sid}.r1", "name": ref["name"], "description": ref.get("description") or ref["name"], "use": "target",
        "query": query, "expected": ref["target"], "claims": claims, "resolution": "resolved",
        "scope": "All records in the supplied environment visible to the actor.", "paths": paths,
        "identifying": identifying, "written": ref.get("written", []), "answer": [], "effect": ref["effect"]}]
    for i, other in enumerate(rest.get("other_references", []) or [], start=2):
        oq = copy.deepcopy(other.get("query", {}))
        oq.setdefault("key", ["id"])
        opaths, oident = _derived_paths(oq) if oq.get("table") else ([], [])
        references.append({"id": f"{sid}.r{i}", "name": other.get("name", f"input {i}"),
                           "description": other.get("name", ""), "use": "input", "query": oq,
                           "expected": other.get("target", []), "claims": [], "resolution": "resolved",
                           "scope": "All records in the supplied environment visible to the actor.", "paths": opaths,
                           "identifying": oident, "written": [], "answer": []})
    case = {"case_id": sid, "domain": s["domain"], "form": "present",
            "mode": "multiple" if s["answer"] == "all" else "single", "plural": s["answer"] == "all",
            "acting_user_id": actor, "seed": seed, "prompt": s["request"].strip(), "references": references,
            "probes": [list(p) for p in rest.get("probes", []) or []], "write_check": rest["write"],
            "conditions": rest["conditions"]}
    try:
        case, _results, errors = finish(case)
    except Exception as exc:
        return None, [f"Reference query or mutation cannot be evaluated: {type(exc).__name__}: {exc}"]
    problems += [f"Claim check: {e}" for e in errors]
    problems += _lint(s)
    ids = _ids_in_request(case)
    if ids:
        problems.append(f"The request contains internal ids {ids}; name records as a user would.")
    problems += _replica_rules(s, case)
    if not errors:
        for test, meta in derive.suite(case):
            if meta["form"] in ("probe", "fact probe"):
                problems += [f"{test['case_id']}: {m} (an entity the request names must still exist when the "
                             "target is removed)" for m in missing_anchors(test)]
    return case, problems
