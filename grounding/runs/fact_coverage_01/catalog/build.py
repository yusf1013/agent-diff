"""Build fact-discrimination coverage (FDC) catalogs from the curated inventories.

Checks complete accounting against the adopted models (every stored column of an
included entity and every model relationship has a disposition), then writes
<domain>.json catalogs and counts.md. No model or service calls.

    python -m grounding.runs.fact_coverage_01.catalog.build          # write
    python -m grounding.runs.fact_coverage_01.catalog.build --check  # verify only
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path

from grounding.paths import REPO_ROOT
from grounding.runs.fact_coverage_01.catalog import facts

HERE = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slack_inventory():
    """Slack columns come from the implemented schema; relationships from its FKs."""
    from grounding.generation.selection import SCHEMA
    tables = {name: [{"name": c, "fk": bool(t.columns[c].foreign_key)} for c in t.columns]
              for name, t in SCHEMA.items()}
    rels = [{"id": f"{name}.{c}", "source_table": name, "observable": None}
            for name, t in SCHEMA.items() for c in t.columns if t.columns[c].foreign_key]
    return tables, rels, [REPO_ROOT / "backend/src/services/slack/database/schema.py"]


def model_inventory(domain):
    model_path = REPO_ROOT / domain["model"]
    inv_path = REPO_ROOT / domain["inventory"]
    model = json.loads(model_path.read_text())
    inv = json.loads(inv_path.read_text())
    tables = {t["table"]: [{"name": c["name"], "fk": bool(c["foreign_keys"])} for c in t["columns"]]
              for t in inv["tables"]}
    rels = [{"id": r["id"], "source": r["source"], "target": r["target"],
             "observable": bool(r.get("read_witnesses"))} for r in model["relationships"]]
    entities = {e["name"]: e["source_table"] for e in model["entities"]}
    return tables, rels, [model_path, inv_path], entities


def disposition(domain, entity, column, is_fk, errors):
    """Return (category, note) for a column not included as an attribute."""
    explicit = domain.get("excluded_columns", {})
    for scope in (entity, "*"):
        entry = explicit.get(scope, {})
        if column in entry:
            value = entry[column]
            return value if isinstance(value, tuple) else (value, "")
    if is_fk:
        return ("fk", "")
    for pattern, category, note in domain.get("column_patterns", []):
        if re.search(pattern, column):
            return (category, note)
    for scope in (entity, "*"):
        entry = explicit.get(scope, {})
        if "*" in entry:
            value = entry["*"]
            return value if isinstance(value, tuple) else (value, "catch-all")
    errors.append(f"{domain['name']}: unaccounted column {entity}.{column}")
    return ("UNACCOUNTED", "")


def build_domain(domain):
    errors: list[str] = []
    if domain["name"] == "slack":
        tables, rels, sources = slack_inventory()
        entity_rows = {name: row for name, row in domain["entities"].items()}
        entity_table = {name: row[0] for name, row in entity_rows.items()}
        included = [n for n, row in entity_rows.items() if row[1] == "included"]
        excluded = {n: row[2] for n, row in entity_rows.items() if row[1] == "excluded"}
        for r in rels:  # observable per model section 3: unexposed tables have no dispatched access
            table = r["source_table"]
            owner = next(n for n, t in entity_table.items() if t == table)
            r["observable"] = owner in included and r["id"] != "team_settings.default_channel_id"
    else:
        tables, rels, sources, model_entities = model_inventory(domain)
        if "entities" in domain:
            entity_table = {n: row[0] for n, row in domain["entities"].items()}
            included = [n for n, row in domain["entities"].items() if row[1] == "included"]
            excluded = {n: row[2] for n, row in domain["entities"].items() if row[1] == "excluded"}
        else:
            entity_table = dict(model_entities)
            included = list(domain["entities_included"])
            excluded = dict(domain["entities_excluded"])
        missing = set(model_entities) - set(included) - set(excluded)
        extra = (set(included) | set(excluded)) - set(model_entities)
        if missing or extra:
            errors.append(f"{domain['name']}: entity accounting mismatch missing={sorted(missing)} extra={sorted(extra)}")
    covered_tables = {entity_table[n] for n in entity_table} | set(domain.get("folded_tables", {}))
    for table in tables:
        if table not in covered_tables and not any(r["id"].startswith(table) for r in rels):
            errors.append(f"{domain['name']}: table {table} has no entity/fold/association disposition")

    requirements = []
    column_accounting = []
    for entity in included:
        table = entity_table[entity]
        cols = tables[table]
        attrs = domain["attributes"].get(entity, {})
        names = {c["name"] for c in cols}
        for field in attrs:
            if field not in names:
                errors.append(f"{domain['name']}: attribute {entity}.{field} not in {table}")
        for c in cols:
            if c["name"] in attrs:
                kind, evidence = attrs[c["name"]]
                if kind not in facts.KINDS:
                    errors.append(f"bad kind {kind}")
                key = f"{entity}.{c['name']}"
                requirements.append({"id": f"A:{key}", "kind": "A", "subkind": kind, "entity": entity,
                                     "table": table, "field": c["name"], "evidence": evidence,
                                     "alternatives": domain.get("attribute_alternatives", {}).get(key, []),
                                     "mutation": "DROP"})
                column_accounting.append({"column": f"{table}.{c['name']}", "disposition": "A"})
            else:
                category, note = disposition(domain, entity, c["name"], c["fk"], errors)
                if category not in facts.CATEGORIES and category != "UNACCOUNTED":
                    errors.append(f"bad category {category} for {entity}.{c['name']}")
                column_accounting.append({"column": f"{table}.{c['name']}", "disposition": category, "note": note})

    rel_ids = {r["id"]: r for r in rels}
    used_roles = {}
    for group, kind, mutation in (("relationships", "R", "SUB_OR_DROP"), ("hierarchy", "H", "LEVEL")):
        for item in domain.get(group, []):
            for role in item["roles"]:
                if role not in rel_ids:
                    errors.append(f"{domain['name']}: {item['id']} names unknown relationship {role}")
                    continue
                if not rel_ids[role]["observable"]:
                    errors.append(f"{domain['name']}: {item['id']} uses unobservable relationship {role}")
                used_roles[role] = item["id"]
            requirements.append({"id": item["id"], "kind": kind, "roles": item["roles"],
                                 "meaning": item["meaning"],
                                 "alternatives": item.get("alternatives", [item.get("confusion", "")]),
                                 "mutation": mutation})
    rel_accounting = []
    explicit = domain.get("excluded_relationships", {})
    for r in rels:
        rid = r["id"]
        if rid in used_roles:
            rel_accounting.append({"relationship": rid, "disposition": used_roles[rid]})
        elif rid in explicit:
            category, note = explicit[rid]
            rel_accounting.append({"relationship": rid, "disposition": category, "note": note})
        elif r.get("source") in excluded or r.get("target") in excluded:
            rel_accounting.append({"relationship": rid, "disposition": "entity_excluded", "note": ""})
        elif not r["observable"]:
            rel_accounting.append({"relationship": rid, "disposition": "unexposed", "note": "no read witness in the model"})
        else:
            errors.append(f"{domain['name']}: unaccounted observable relationship {rid}")
    for rid in explicit:
        if rid not in rel_ids:
            errors.append(f"{domain['name']}: excluded relationship {rid} not in model")

    for item in domain.get("bindings", []):
        requirements.append({"id": item["id"], "kind": "B", "parent": item["parent"], "child": item["child"],
                             "meaning": item["meaning"], "mutation": "SPLIT"})
    for item in domain.get("derived", []):
        requirements.append({"id": item["id"], "kind": "D", "meaning": item["meaning"],
                             "alternatives": [item["confusion"]], "mutation": "VIEW"})
    # Sibling attributes: same entity and kind (identity, text, time, quantity) are designated alternatives for
    # each other; states are enumerations whose alternative is another value, not another attribute.
    attrs = [r for r in requirements if r["kind"] == "A"]
    for r in attrs:
        if r["subkind"] == "state":
            continue
        sib = [f"{x['entity']}.{x['field']}" for x in attrs
               if x is not r and x["entity"] == r["entity"] and x["subkind"] == r["subkind"]]
        r["sibling_alternatives"] = sib
    ids = [r["id"] for r in requirements]
    if len(ids) != len(set(ids)):
        errors.append(f"{domain['name']}: duplicate requirement ids")
    catalog = {
        "domain": domain["name"],
        "criterion": "fact-discrimination coverage; see ../criterion.md",
        "sources": {str(p.relative_to(REPO_ROOT)): sha(p) for p in sources},
        "curation": {"path": "grounding/runs/fact_coverage_01/catalog/facts.py",
                     "sha256": sha(HERE / "facts.py")},
        "entities": {"included": included, "excluded": excluded},
        "requirements": requirements,
        "column_accounting": column_accounting,
        "relationship_accounting": rel_accounting,
    }
    return catalog, errors


def route_sizes(name):
    """Alternative-criterion sizes from the adopted exact route counts."""
    if name == "slack":
        probe = json.loads((REPO_ROOT / "grounding/domains/slack/coverage/route_probe.json").read_text())
        return {"structural": 2870, "read_screened": 212, "ordinary_reviewed": 174, "probe_keys": sorted(probe)[:3]}
    counts = json.loads((REPO_ROOT / f"grounding/domains/{name}/route_counts.json").read_text())
    screened = counts["direct_read_and_tag_consistent"]
    by = screened["by_relationship_edges"]
    return {"structural": counts["structural"]["routes"], "read_screened": screened["routes"],
            "read_screened_len_le_2": sum(v for k, v in by.items() if int(k) <= 2),
            "read_screened_len_le_3": sum(v for k, v in by.items() if int(k) <= 3)}


def counts_table(catalogs):
    lines = ["# Requirement counts", "",
             "Generated by `build.py` from the curated inventories in `facts.py`. FDC counts are requirements, "
             "not tests. Route counts are the adopted exact counts in `grounding/domains/*/route_counts.json` "
             "(Slack: `coverage/route_probe.json` and the 174-route review).", "",
             "## Fact-discrimination requirements", "",
             "| Domain | A attributes | R relationships | H hierarchy | B bindings | D derived | **Total** |",
             "|---|---:|---:|---:|---:|---:|---:|"]
    totals = [0] * 6
    for c in catalogs:
        k = [sum(r["kind"] == x for r in c["requirements"]) for x in "ARHBD"]
        k.append(sum(k))
        totals = [a + b for a, b in zip(totals, k)]
        lines.append(f"| {c['domain']} | " + " | ".join(str(x) for x in k[:-1]) + f" | **{k[-1]}** |")
    lines.append("| all | " + " | ".join(str(x) for x in totals[:-1]) + f" | **{totals[-1]}** |")
    lines += ["", "Attribute subkinds:", "", "| Domain | identity | text | time | quantity | state |", "|---|---:|---:|---:|---:|---:|"]
    for c in catalogs:
        a = [r for r in c["requirements"] if r["kind"] == "A"]
        lines.append(f"| {c['domain']} | " + " | ".join(str(sum(r['subkind'] == s for r in a))
                                                   for s in ("identity", "text", "time", "quantity", "state")) + " |")
    lines += ["", "Facts with at least one designated alternative (explicit, sibling role/attribute, or kind-level "
              "confusion for H/B/D):", "", "| Domain | With alternative | Without | Share |", "|---|---:|---:|---:|"]
    for c in catalogs:
        reqs = c["requirements"]
        has = [r for r in reqs if r["kind"] in "HBD" or r.get("alternatives") or r.get("sibling_alternatives")]
        lines.append(f"| {c['domain']} | {len(has)} | {len(reqs) - len(has)} | {len(has) / len(reqs):.0%} |")
    lines += ["", "## Comparison with route-based criteria", "",
              "| Domain | FDC requirements | Structural routes | Read-screened routes | Read-screened, ≤2 edges | Read-screened, ≤3 edges | Entity×route×mode (read-screened ×4) |",
              "|---|---:|---:|---:|---:|---:|---:|"]
    for c in catalogs:
        s = route_sizes(c["domain"])
        n = len(c["requirements"])
        le2 = s.get("read_screened_len_le_2", "—")
        le3 = s.get("read_screened_len_le_3", "—")
        rs = s["read_screened"] if c["domain"] != "slack" else s["ordinary_reviewed"]
        lines.append(f"| {c['domain']} | {n} | {s['structural']:,} | {s['read_screened']:,}"
                     + (f" (174 after ordinary review)" if c["domain"] == "slack" else "")
                     + f" | {le2 if isinstance(le2, str) else f'{le2:,}'} | {le3 if isinstance(le3, str) else f'{le3:,}'} | {4 * rs:,} |")
    lines += ["", "Pairwise fact interactions (all unordered pairs of FDC facts, an upper bound for "
              "interaction coverage) would give: " + ", ".join(
                  f"{c['domain']} {math.comb(len(c['requirements']), 2):,}" for c in catalogs) + ".",
              "", "## Accounting", "", "| Domain | Included entities | Excluded entities | Columns accounted | Relationships accounted |",
              "|---|---:|---:|---:|---:|"]
    for c in catalogs:
        lines.append(f"| {c['domain']} | {len(c['entities']['included'])} | {len(c['entities']['excluded'])} | "
                     f"{len(c['column_accounting'])} | {len(c['relationship_accounting'])} |")
    lines += ["", "Column dispositions by category:", ""]
    for c in catalogs:
        cats = {}
        for row in c["column_accounting"]:
            cats[row["disposition"]] = cats.get(row["disposition"], 0) + 1
        lines.append(f"- **{c['domain']}**: " + ", ".join(f"{k} {v}" for k, v in sorted(cats.items(), key=lambda x: -x[1])))
    lines += ["", "Relationship dispositions:", ""]
    for c in catalogs:
        cats = {}
        for row in c["relationship_accounting"]:
            d = row["disposition"]
            d = "included (R/H)" if d.startswith(("R:", "H:")) else d
            cats[d] = cats.get(d, 0) + 1
        lines.append(f"- **{c['domain']}**: " + ", ".join(f"{k} {v}" for k, v in sorted(cats.items(), key=lambda x: -x[1])))
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalogs, errors = [], []
    for domain in facts.DOMAINS:
        catalog, errs = build_domain(domain)
        catalogs.append(catalog)
        errors += errs
    if errors:
        raise SystemExit("\n".join(errors))
    outputs = {HERE / f"{c['domain']}.json": json.dumps(c, indent=1, ensure_ascii=False) + "\n" for c in catalogs}
    outputs[HERE / "counts.md"] = counts_table(catalogs)
    if args.check:
        stale = [p.name for p, text in outputs.items() if not p.exists() or p.read_text() != text]
        if stale:
            raise SystemExit("Stale outputs: " + ", ".join(stale))
        print("catalogs current")
        return
    for path, text in outputs.items():
        path.write_text(text)
    print(json.dumps({c["domain"]: len(c["requirements"]) for c in catalogs}))


if __name__ == "__main__":
    main()
