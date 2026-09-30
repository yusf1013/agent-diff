"""P1: the status quo's own tests, mutated mechanically into absence and underspecified variants (no LLM).

The rule, fixed before generation (README.md in this folder states it for readers):

- **Scope.** Agent-Diff's Slack, Box and Linear tests (59 + 48 + 57 = 164; Calendar has no obligation cards yet). One
  candidate per (obligation, mode) for every obligation the cards call resolved.
- **Absence.** Remove the obligation's referents from the service's shared seed, then every row that points at a
  removed row through a foreign key, until none do (the removal our own derivation uses,
  `autogen_01/kit/derive.py` `prune_orphans`; self-references included here). The prompt is unchanged.
- **Underspecified** (singular, state-changing obligations only). Add a copy of the referent: a new key, and new values
  for the fields the service keeps unique (the replica schema's unique constraints; the unique-identifier fields our
  clone check knows, `autogen_02/kit/variants2.py` `UNIQUE_FIELDS`, when the seed keeps them unique; and Box's rule
  that an item's name is unique within its folder). Then a copy of every row that points at a copied row, recursively:
  the record duplicated with everything under it. The prompt is unchanged.
- **Automatic exclusions**, recorded with the reason, never silent:
  - `deletes_actor`: the removal takes the acting user;
  - `confounded`: the removal also removes, or the copy also duplicates, a referent or candidate of another obligation
    of the same test (the variant would change more than the one obligation);
  - `not_derivable`: the copy had to change a field the obligation identifies its referent by, or the referent's
    table has a composite key;
  - `still_matched` (absence): another row keeps every identifying value of one of the obligation's identifying sets
    (flagged for the review, not excluded: the review decides whether the request still has a match).
- Everything not excluded goes to the manual review ([review.jsonl](review.jsonl)).

Run from the repository root with the backend's interpreter (for nothing but json here; schemas.json is a dump):
    python -m grounding.runs.related_work_01.p1.generate
Writes candidates.jsonl (one row per candidate, with its summary and flags) and patches.jsonl (the rows each variant
removes or adds), and prints the counts.
"""
from __future__ import annotations

import copy
import json
import re
import uuid
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
HERE = Path(__file__).parent
SEEDS = {"slack": "examples/slack/seeds/slack_bench_v2.json", "box": "examples/box/seeds/box_default.json",
         "linear": "examples/linear/seeds/linear_expanded.json"}
UNIQUE_FIELDS = re.compile(r"^(identifier|number|url|slugId|slug|ts|ical_uid|iCalUID|etag|branchName)$")
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)
COPY_CAP = 200


def load():
    schemas = json.loads((HERE / "schemas.json").read_text())
    tests = {}
    for line in (REPO / "datasets/agent-diff-bench/all_numbered.jsonl").read_text().splitlines():
        row = json.loads(line)
        tests[row["test_id"]] = row
    return schemas, tests


def pk_of(schema, table):
    return next(x["columns"] for x in schema[table]["unique"] if x["kind"] == "PrimaryKeyConstraint")


def fks_of(schema):
    return [(t, fk["column"], fk["ref_table"], fk["ref_column"]) for t, info in schema.items() for fk in info["fks"]]


def row_key(schema, table, row):
    return json.dumps([row.get(c) for c in pk_of(schema, table)])


def find_rows(schema, seed, table, ref):
    rows = seed.get(table, [])
    if isinstance(ref, dict):
        return [r for r in rows if all(str(r.get(k)) == str(v) for k, v in ref.items())]
    pk = pk_of(schema, table)
    return [r for r in rows if len(pk) == 1 and str(r.get(pk[0])) == str(ref)]


def referent_ids(card):
    """Every referent or candidate id an obligation names (candidate sets of underspecified cards included)."""
    refs = card["Referent set"]
    if isinstance(refs, dict):
        out = []
        for cand in refs.get("candidate_sets") or []:
            out += list(cand or [])
        return [_ident(x) for x in out]
    return [_ident(x) for x in refs or []]


def _ident(x):
    return json.dumps(x, sort_keys=True) if isinstance(x, dict) else str(x)


def identifying_columns(card, table):
    cols = set()
    for alt in card.get("Alternative sufficient identifying sets") or []:
        for item in alt or []:
            t, _, c = item.partition(".")
            if t == table:
                cols.add(c)
    return cols


def identifying_sets(card, table):
    out = []
    for alt in card.get("Alternative sufficient identifying sets") or []:
        cols = [item.partition(".")[2] for item in alt or [] if item.partition(".")[0] == table]
        if cols:
            out.append(cols)
    return out


# ------------------------------------------------------------------ absence

def remove(schema, seed, table, targets):
    """Remove the target rows and, repeatedly, every row whose foreign key points at a removed row."""
    seed = copy.deepcopy(seed)
    removed = defaultdict(list)
    target_keys = {row_key(schema, table, r) for r in targets}
    keep = []
    for r in seed[table]:
        (removed[table].append(r) if row_key(schema, table, r) in target_keys else keep.append(r))
    seed[table] = keep
    fks = [fk for fk in fks_of(schema) if fk[0] in seed and fk[2] in seed]
    while True:
        n = 0
        for child, col, parent, pcol in fks:
            present = {r.get(pcol) for r in seed[parent]}
            kept = []
            for r in seed[child]:
                if r.get(col) is not None and r.get(col) not in present:
                    removed[child].append(r)
                    n += 1
                else:
                    kept.append(r)
            seed[child] = kept
        if not n:
            return seed, removed


# ------------------------------------------------------------------ underspecified

def fresh_value(value, taken, table, col):
    """A value in the style of `value`, unused in `taken` (the style our fresh_id keeps: next number, new UUID)."""
    taken = {str(x) for x in taken}
    if isinstance(value, int):
        n = max([int(x) for x in taken if x.lstrip("-").isdigit()] + [value]) + 1
        return n
    text = str(value)
    if UUID.match(text):
        return str(uuid.uuid5(uuid.NAMESPACE_URL, f"related_work_01 P1 copy of {table}.{col}={text}"))
    if col == "email" and "@" in text:
        local, _, domain = text.partition("@")
        n = 2
        while f"{local}{n}@{domain}" in taken:
            n += 1
        return f"{local}{n}@{domain}"
    if col == "name" and table in ("box_files", "box_folders"):
        stem, dot, ext = text.rpartition(".") if "." in text else (text, "", "")
        n = 1
        while True:
            cand = f"{stem} ({n}){dot}{ext}" if dot else f"{text} ({n})"
            if cand not in taken:
                return cand
            n += 1
    m = re.match(r"^(.*?)(\d+)$", text)
    if m:
        prefix, digits = m.groups()
        n = int(digits) + 1
        while f"{prefix}{str(n).zfill(len(digits))}" in taken:
            n += 1
        return f"{prefix}{str(n).zfill(len(digits))}"
    key_like = col.endswith("id") or col.endswith("Id") or col.endswith("_ID")
    sep = "" if key_like else "-" if (col in ("channel_name", "username", "key") or " " not in text) else " "
    n = 2
    while f"{text}{sep}{n}" in taken:
        n += 1
    return f"{text}{sep}{n}"


def unique_fields(schema, seed, table, row):
    """Fields a copy of `row` must change: the key, schema-unique columns, known unique identifiers the seed keeps
    unique, and Box's name-in-folder rule."""
    pk = pk_of(schema, table)
    fks = {fk["column"] for fk in schema[table]["fks"]}
    out = set(pk)
    for u in schema[table]["unique"]:
        if u["kind"] == "PrimaryKeyConstraint":
            continue
        free = [c for c in u["columns"] if c not in fks]
        out |= set(free or u["columns"])
    rows = seed.get(table, [])
    for col, value in row.items():
        if UNIQUE_FIELDS.match(col) and value not in (None, "", [], {}):
            values = [r.get(col) for r in rows if r.get(col) not in (None, "")]
            if len(values) == len(set(map(str, values))):
                out.add(col)
    if table in ("box_files", "box_folders"):
        out.add("name")
    return out


def deep_copy(schema, seed, table, target):
    """A copy of `target` with its unique fields changed, and one copy of every row that points at a copied row.

    Two passes: first the closure of rows under the target (rows whose foreign key points at a row of the closure,
    repeatedly, read from the original seed); then one copy of each, with a fresh key, and every foreign key that
    points inside the closure moved to the copy."""
    fks = [fk for fk in fks_of(schema) if fk[0] in seed]
    closure = {(table, row_key(schema, table, target)): (table, target)}
    frontier = [(table, target)]
    capped = False
    while frontier and not capped:
        nxt = []
        for ptable, prow in frontier:
            for child, col, parent, pcol in fks:
                if parent != ptable or prow.get(pcol) is None:
                    continue
                for r in seed[child]:
                    if r.get(col) == prow.get(pcol):
                        k = (child, row_key(schema, child, r))
                        if k not in closure:
                            closure[k] = (child, r)
                            nxt.append((child, r))
                            if len(closure) > COPY_CAP:
                                capped = True
        frontier = nxt
    seed = copy.deepcopy(seed)
    # fresh keys and unique fields, table by table
    remap = defaultdict(dict)  # (table, column) -> {old value: new value}
    copies = []
    changed = {}
    for (t, _k), (_t, row) in closure.items():
        new = copy.deepcopy(row)
        pk = pk_of(schema, t)
        fk_cols = {fk["column"] for fk in schema[t]["fks"]}
        fields = unique_fields(schema, seed, t, row) if t == table else (
            set(pk) if len(pk) == 1 and pk[0] not in fk_cols else set())
        if t != table:
            fields |= {c for c in unique_fields(schema, seed, t, row) if c not in fk_cols and c not in pk}
            if t in ("box_files", "box_folders"):
                fields.discard("name")  # rows under a copied folder keep their names: they sit in the copied folder
        for col in sorted(fields):
            if row.get(col) is None:
                continue
            taken = [r.get(col) for r in seed[t]] + [c.get(col) for _, c in copies if _ == t]
            new[col] = fresh_value(row[col], taken, t, col)
            remap[(t, col)][row[col]] = new[col]
            if t == table:
                changed[col] = new[col]
        copies.append((t, new))
    for t, new in copies:
        for fk in schema[t]["fks"]:
            m = remap.get((fk["ref_table"], fk["ref_column"]))
            if m and new.get(fk["column"]) in m:
                new[fk["column"]] = m[new[fk["column"]]]
        seed[t].append(new)
    added = defaultdict(list)
    for t, new in copies:
        added[t].append(new)
    sources = defaultdict(list)
    for (t, _k), (_t, row) in closure.items():
        sources[t].append(row)
    return seed, added, sources, changed, capped


# ------------------------------------------------------------------ summaries for the review

def describe(service, table, row, seed):
    g = lambda t, k, v: next((r for r in seed.get(t, []) if r.get(k) == v), {})
    if service == "slack":
        if table == "channels":
            return f"#{row['channel_name']}" + (" (private)" if row.get("is_private") else "")
        if table == "users":
            return f"{row.get('real_name')} (@{row.get('username')}, display {row.get('display_name')!r})"
        if table == "messages":
            ch = g("channels", "channel_id", row.get("channel_id")).get("channel_name")
            au = g("users", "user_id", row.get("user_id")).get("real_name")
            reply = " (reply)" if row.get("parent_id") else ""
            return f"#{ch} {au}{reply}: {row.get('message_text', '')[:90]!r}"
        if table == "message_reactions":
            return f":{row.get('reaction_type')}: by {row.get('user_id')} on {row.get('message_id')}"
    if service == "box":
        if table in ("box_files", "box_folders"):
            parent = g("box_folders", "id", row.get("parent_id")).get("name", row.get("parent_id"))
            return f"{row.get('name')!r} in {parent!r}"
        return f"{table} {row.get('name') or row.get('title') or row.get('message') or row.get('id')!r}"[:120]
    if service == "linear":
        if table == "issues":
            team = g("teams", "id", row.get("teamId")).get("key")
            state = g("workflow_states", "id", row.get("stateId")).get("name")
            return f"{row.get('identifier')} {row.get('title')!r} (team {team}, {state})"
        if table == "teams":
            return f"team {row.get('name')!r} ({row.get('key')})"
        if table == "users":
            return f"{row.get('name')} ({row.get('displayName')}, {row.get('email')})"
        if table == "workflow_states":
            team = g("teams", "id", row.get("teamId")).get("key")
            return f"state {row.get('name')!r} of {team}"
        if table == "issue_labels":
            return f"label {row.get('name')!r}"
        if table == "comments":
            return f"comment {str(row.get('body'))[:80]!r}"
    return f"{table} {json.dumps(row)[:100]}"


# ------------------------------------------------------------------ main

def main():
    schemas, tests = load()
    candidates, patches = [], []
    for service in ("slack", "box", "linear"):
        schema = schemas[service]
        seed = json.loads((REPO / SEEDS[service]).read_text())
        analysis = json.loads((REPO / f"grounding/domains/{service}/analysis/analysis.json").read_text())
        for test in analysis:
            tid = test["test_id"]
            info = json.loads(tests[tid]["info"])
            actor = info["impersonate_user_id"]
            actor_table = {"slack": "users", "box": "box_users", "linear": "users"}[service]
            obligations = test["obligations"]
            for oi, ob in enumerate(obligations, 1):
                card = ob["card"]
                if card["Resolution"] != "resolved":
                    continue
                table = ob["referent_entity"]
                refs = card["Referent set"]
                rows = [r for ref in refs for r in find_rows(schema, seed, table, ref)]
                others = {x for j, o2 in enumerate(obligations, 1) if j != oi for x in referent_ids(o2["card"])}
                other_tables = {o2["referent_entity"] for j, o2 in enumerate(obligations, 1) if j != oi}
                base = {"service": service, "test_id": tid, "obligation": oi, "name": card["Grounding obligation name"],
                        "description": card["Grounding obligation description"], "task_type": card["Task type"],
                        "referent_table": table, "referents": refs, "prompt": tests[tid]["question"][:240],
                        "referent_summary": [describe(service, table, r, seed) for r in rows],
                        "identifying_sets": card.get("Alternative sufficient identifying sets")}
                pk = pk_of(schema, table)

                # absence
                new_seed, removed = remove(schema, seed, table, rows)
                removed_ids = {str(r.get(c)) for t, rs in removed.items() for r in rs for c in pk_of(schema, t)
                               if len(pk_of(schema, t)) == 1}
                removed_ids |= {json.dumps({k: r.get(k) for k in pk_of(schema, t)}, sort_keys=True)
                                for t, rs in removed.items() for r in rs}
                confounded = sorted(x for x in others if x in removed_ids)
                deletes_actor = any(str(r.get(pk_of(schema, actor_table)[0])) == str(actor)
                                    for r in removed.get(actor_table, []))
                still = []
                for cols in identifying_sets(card, table):
                    for r in rows:
                        vals = {c: r.get(c) for c in cols}
                        if any(v is None for v in vals.values()):
                            continue
                        hits = [x for x in new_seed[table] if all(x.get(c) == v for c, v in vals.items())]
                        still += [describe(service, table, h, new_seed) for h in hits]
                flags = {"deletes_actor": deletes_actor, "confounded": confounded, "still_matched": sorted(set(still))}
                status = ("excluded:deletes_actor" if deletes_actor else
                          "excluded:confounded" if confounded else "review")
                vid = f"P1-A-{tid}-O{oi}"
                candidates.append({**base, "variant": vid, "mode": "absence", "status": status, "flags": flags,
                                   "removed": {t: len(rs) for t, rs in removed.items()},
                                   "removed_summary": [describe(service, t, r, seed) for t, rs in removed.items()
                                                       for r in rs][:6]})
                patches.append({"variant": vid, "service": service, "remove": {
                    t: [{c: r.get(c) for c in pk_of(schema, t)} for r in rs] for t, rs in removed.items()}})

                # underspecified
                if card["Task type"] != "state-changing" or len(rows) != 1:
                    continue
                vid = f"P1-U-{tid}-O{oi}"
                target = rows[0]
                if len(pk) != 1:
                    candidates.append({**base, "variant": vid, "mode": "underspecified",
                                       "status": "excluded:not_derivable",
                                       "flags": {"not_derivable": f"{table} has a composite key {pk}"}})
                    continue
                new_seed, added, sources, changed, capped = deep_copy(schema, seed, table, target)
                ident = identifying_columns(card, table)
                clash = sorted(set(changed) & ident)
                source_ids = {str(r.get(c)) for t, rs in sources.items() for r in rs for c in pk_of(schema, t)
                              if len(pk_of(schema, t)) == 1 and not (t == table and r == target)}
                dup = sorted(x for x in others if x in source_ids)
                flags = {"not_derivable": (f"the copy must change {clash}, which the obligation identifies by"
                                           if clash else None),
                         "confounded": dup, "copy_capped": capped, "changed": changed,
                         "copied": {t: len(rs) for t, rs in added.items()}}
                status = ("excluded:not_derivable" if clash else "excluded:confounded" if dup else
                          "excluded:copy_capped" if capped else "review")
                candidates.append({**base, "variant": vid, "mode": "underspecified", "status": status, "flags": flags,
                                   "clone_summary": describe(service, table, added[table][0], new_seed)})
                patches.append({"variant": vid, "service": service, "add": {t: rs for t, rs in added.items()}})

    (HERE / "candidates.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in candidates))
    (HERE / "patches.jsonl").write_text("".join(json.dumps(p, ensure_ascii=False, default=str) + "\n" for p in patches))
    counts = Counter((c["service"], c["mode"], c["status"]) for c in candidates)
    for k in sorted(counts):
        print(k, counts[k])
    print("total", len(candidates), "review", sum(c["status"] == "review" for c in candidates))


if __name__ == "__main__":
    main()
