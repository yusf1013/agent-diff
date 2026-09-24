"""Reference queries, fact mutations and credit checks for FDC cases.

A reference query is a join tree rooted at the referent table. Every filter and
edge carries a `key` (unique in the query) and optionally the requirement `fact`
it realizes. Semantics are existential: a root row matches when some assignment
of related rows satisfies every filter and edge; filters on one node bind to the
same row. Edge options:

  join     {"parent": col, "child": col, "op": "eq"|"json_contains"|"json_in"}
           json_contains: the parent's JSON list contains the child's value;
           json_in: the child's JSON list contains the parent's value.
  closure  true: follow the join transitively through the same table (1+ steps).
  count    {"op": "ge", "value": 2}: count distinct matching child rows instead
           of requiring existence (count "eq" 0 expresses "has none").

A credit claim names a requirement, a near-miss witness (root handle) and a
mutation of the query: DROP (remove a filter, or the join condition of an edge),
SUB (replace an edge with an alternative edge), SPLIT (split an edge's node
filters across two independent copies), LEVEL (toggle closure) or REPLACE
(explicit alternative query, for derived views). The claim holds when the witness
is selected by the mutant but not by the original query. Witnesses must be
distinct across claims of a reference. No model or service calls.
"""
from __future__ import annotations

import copy
import json
from datetime import datetime, date


def _as_time(value):
    if isinstance(value, (datetime, date)):
        return value if isinstance(value, datetime) else datetime(value.year, value.month, value.day)
    if isinstance(value, str) and len(value) >= 10 and value[4] == "-" and value[7] == "-":
        text = value.replace("Z", "+00:00")
        try:
            parsed = datetime.fromisoformat(text)
        except ValueError:
            return None
        if parsed.tzinfo is None:
            from datetime import timezone
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed
    return None


def compare(left, op, right):
    if op == "is_null":
        return left is None
    if op == "not_null":
        return left is not None
    if op == "eq":
        return left == right
    if op == "ne":
        return left != right
    if op == "in":
        return left in right
    if op == "not_in":
        return left not in right
    if op == "contains_ci":
        return isinstance(left, str) and right.casefold() in left.casefold()
    if op == "not_contains_ci":
        return not (isinstance(left, str) and right.casefold() in left.casefold())
    if op == "json_has":
        items = left if isinstance(left, list) else (json.loads(left) if isinstance(left, str) and left.startswith("[") else [])
        return any((isinstance(i, str) and isinstance(right, str) and i.casefold() == right.casefold()) or i == right for i in items)
    if op in {"lt", "le", "gt", "ge"}:
        if left is None:
            return False
        lt, rt = _as_time(left), _as_time(right)
        if lt is not None and rt is not None:
            left, right = lt, rt
        return {"lt": left < right, "le": left <= right, "gt": left > right, "ge": left >= right}[op]
    raise ValueError(f"unknown op {op}")


def _json_list(value):
    if isinstance(value, list):
        return value
    if isinstance(value, str) and value.startswith("["):
        return json.loads(value)
    return []


def _joined(seed, table, row, edge):
    """Child rows reachable from `row` through the edge's join (with optional closure)."""
    join = edge.get("join")
    child_table = edge["node"]["table"]
    rows = seed.get(child_table, [])
    if join is None:  # DROP of the relationship: any row of the child table
        return list(rows)

    def step(parent_row):
        op = join.get("op", "eq")
        pv = parent_row.get(join["parent"])
        out = []
        for c in rows:
            cv = c.get(join["child"])
            if op == "eq" and pv is not None and pv == cv:
                out.append(c)
            elif op == "json_contains" and cv is not None and cv in _json_list(pv):
                out.append(c)
            elif op == "json_in" and pv is not None and pv in _json_list(cv):
                out.append(c)
        return out

    first = step(row)
    if not edge.get("closure"):
        return first
    if child_table != table:
        raise ValueError("closure requires a self join")
    seen, frontier, result = set(), first, []
    if edge["closure"] == "star":  # zero or more steps: include the row itself
        frontier = [row] + first
    while frontier:
        nxt = []
        for c in frontier:
            ident = json.dumps(c, sort_keys=True, default=str)
            if ident in seen:
                continue
            seen.add(ident)
            result.append(c)
            nxt.extend(step(c))
        frontier = nxt
    return result


def get_field(row, field):
    """Column value; a dotted path reads into JSON objects (e.g. start.dateTime)."""
    head, _, rest = field.partition(".")
    value = row.get(head)
    while rest:
        if isinstance(value, str) and value.startswith("{"):
            value = json.loads(value)
        if not isinstance(value, dict):
            return None
        head, _, rest = rest.partition(".")
        value = value.get(head)
    return value


def node_matches(seed, node, row):
    for f in node.get("filters", []):
        if not compare(get_field(row, f["field"]), f["op"], f.get("value")):
            return False
    for edge in node.get("edges", []):
        children = _joined(seed, node["table"], row, edge)
        matching = [c for c in children if node_matches(seed, edge["node"], c)]
        if "count" in edge:
            distinct = {json.dumps(c, sort_keys=True, default=str) for c in matching}
            if not compare(len(distinct), edge["count"]["op"], edge["count"]["value"]):
                return False
        elif edge.get("negate"):
            if matching:
                return False
        elif not matching:
            return False
    return True


def handle(query, row):
    key = query.get("key", ["id"])
    return row[key[0]] if len(key) == 1 else {k: row[k] for k in key}


def evaluate(seed, query):
    rows = [r for r in seed.get(query["table"], []) if node_matches(seed, query, r)]
    for mode in ("argmax", "argmin"):
        if query.get(mode) and rows:
            values = [(_as_time(get_field(r, query[mode])) or get_field(r, query[mode])) for r in rows]
            best = max(values) if mode == "argmax" else min(values)
            rows = [r for r, v in zip(rows, values) if v == best]
    return [handle(query, r) for r in rows]


def _find(node, key, parent=None, container=None):
    for i, f in enumerate(node.get("filters", [])):
        if f.get("key") == key:
            return ("filter", node, i)
    for i, e in enumerate(node.get("edges", [])):
        if e.get("key") == key:
            return ("edge", node, i)
        found = _find(e["node"], key)
        if found:
            return found
    return None


def keys(node):
    out = [f.get("key") for f in node.get("filters", [])]
    for e in node.get("edges", []):
        out.append(e.get("key"))
        out += keys(e["node"])
    return [k for k in out if k]


def mutate(query, mutation):
    kind = mutation["type"]
    if kind == "REPLACE":
        return copy.deepcopy(mutation["query"])
    mutant = copy.deepcopy(query)
    found = _find(mutant, mutation["target"])
    if not found:
        raise ValueError(f"mutation target {mutation['target']} not found")
    what, node, index = found
    if kind == "DROP":
        if what == "filter":
            del node["filters"][index]
        else:
            node["edges"][index]["join"] = None
            node["edges"][index].pop("closure", None)
    elif kind == "SUB":
        if what != "edge":
            raise ValueError("SUB targets an edge")
        node["edges"][index] = copy.deepcopy(mutation["replacement"])
    elif kind == "LEVEL":
        if what != "edge":
            raise ValueError("LEVEL targets an edge")
        node["edges"][index]["closure"] = bool(mutation.get("closure", True))
    elif kind == "SPLIT":
        if what != "edge":
            raise ValueError("SPLIT targets an edge")
        edge = node["edges"][index]
        groups = mutation["groups"]
        copies = []
        for g, members in enumerate(groups):
            twin = copy.deepcopy(edge)
            twin["key"] = f"{edge.get('key')}__split{g}"
            twin["node"]["filters"] = [f for f in edge["node"].get("filters", []) if f.get("key") in members]
            twin["node"]["edges"] = [e for e in edge["node"].get("edges", []) if e.get("key") in members]
            copies.append(twin)
        node["edges"][index:index + 1] = copies
    else:
        raise ValueError(f"unknown mutation {kind}")
    return mutant


def _same(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def check_reference(seed, reference):
    """Recompute the referent set and every claimed credit for one reference."""
    query = reference["query"]
    errors, results = [], []
    selected = evaluate(seed, query)
    expected = reference.get("expected", [])
    if sorted(json.dumps(x, sort_keys=True) for x in selected) != sorted(json.dumps(x, sort_keys=True) for x in expected):
        errors.append(f"{reference['id']}: expected {expected} but query selects {selected}")
    ks = keys(query)
    if len(ks) != len(set(ks)):
        errors.append(f"{reference['id']}: duplicate keys in query")
    witnesses = []
    for claim in reference.get("claims", []):
        mutant = mutate(query, claim["mutation"])
        mutant_selected = evaluate(seed, mutant)
        w = claim["witness"]
        in_original = any(_same(w, s) for s in selected)
        in_mutant = any(_same(w, s) for s in mutant_selected)
        ok = in_mutant and not in_original
        if any(_same(w, x) for x in witnesses):
            ok = False
            errors.append(f"{reference['id']}: witness {w} reused for {claim['requirement']}")
        witnesses.append(w)
        if not ok:
            errors.append(f"{reference['id']}: claim {claim['requirement']} not killed by witness {w} "
                          f"(original={in_original}, mutant={in_mutant})")
        results.append({"requirement": claim["requirement"], "witness": w, "mutation": claim["mutation"]["type"],
                        "strength": "alternative" if claim.get("alternative") else "drop",
                        "alternative": claim.get("alternative"), "credited": ok,
                        "mutant_selects": mutant_selected})
    return {"reference": reference["id"], "selected": selected, "claims": results}, errors


def facts_used(query):
    """Requirement ids realized by filters/edges of the query (occurrence credit)."""
    out = []

    def walk(node):
        for f in node.get("filters", []):
            if f.get("fact"):
                out.append(f["fact"])
        for e in node.get("edges", []):
            if e.get("fact"):
                out.append(e["fact"])
            walk(e["node"])
    walk(query)
    return out
