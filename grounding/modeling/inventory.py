"""Inventory source declarations without treating them as a conceptual model.

Run with backend/.venv/bin/python (some replica source requires Python 3.14).
This does not import service handlers, access a database, or invoke models.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

from grounding.paths import REPO_ROOT


def calls(node, name):
    return [x for x in ast.walk(node) if isinstance(x, ast.Call) and ast.unparse(x.func) == name]


def declaration(node, name, annotation=None):
    kws = {k.arg: ast.unparse(k.value) for k in node.keywords}
    refs = [ast.literal_eval(x.args[0]) for x in calls(node, "ForeignKey")]
    nullable = kws.get("nullable")
    if nullable is None and annotation is not None:
        nullable = "Optional[" in annotation or "None" in annotation
    else:
        nullable = nullable == "True"
    return {"name": name, "line": node.lineno, "annotation": annotation,
            "definition": ast.unparse(node), "foreign_keys": refs,
            "nullable": nullable, "primary_key": kws.get("primary_key") == "True",
            "unique": kws.get("unique") == "True"}


def schema_inventory(path):
    tree = ast.parse(path.read_text())
    tables, enums = [], []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            table = next((ast.literal_eval(n.value) for n in node.body
                          if isinstance(n, ast.Assign) and any(ast.unparse(t) == "__tablename__" for t in n.targets)), None)
            if table is None:
                if any(ast.unparse(b) in ("Enum", "PyEnum") for b in node.bases):
                    enums.append({"name": node.name, "line": node.lineno,
                                  "values": {ast.unparse(n.targets[0]): ast.literal_eval(n.value) for n in node.body if isinstance(n, ast.Assign)}})
                continue
            cols, relationships = [], []
            for n in node.body:
                if isinstance(n, ast.AnnAssign) and isinstance(n.value, ast.Call):
                    if ast.unparse(n.value.func) == "mapped_column":
                        cols.append(declaration(n.value, ast.unparse(n.target), ast.unparse(n.annotation)))
                    elif ast.unparse(n.value.func) == "relationship":
                        relationships.append({"name": ast.unparse(n.target), "line": n.lineno, "definition": ast.unparse(n.value)})
            constraints = [ast.unparse(n.value) for n in node.body if isinstance(n, ast.Assign) and any(ast.unparse(t) == "__table_args__" for t in n.targets)]
            tables.append({"class": node.name, "table": table, "line": node.lineno,
                           "columns": cols, "relationships": relationships, "constraints": constraints, "association": False})
        elif isinstance(node, ast.Assign) and isinstance(node.value, ast.Call) and ast.unparse(node.value.func) == "Table":
            cols = [declaration(c, ast.literal_eval(c.args[0])) for c in node.value.args if isinstance(c, ast.Call) and ast.unparse(c.func) == "Column"]
            tables.append({"class": ast.unparse(node.targets[0]), "table": ast.literal_eval(node.value.args[0]),
                           "line": node.lineno, "columns": cols, "relationships": [], "constraints": [], "association": True})
    return {"tables": tables, "enums": enums}


def function_inventory(path):
    tree = ast.parse(path.read_text())
    result = []
    for n in ast.walk(tree):
        if not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        keys = set()
        for x in ast.walk(n):
            if isinstance(x, ast.Subscript) and isinstance(x.slice, ast.Constant) and isinstance(x.slice.value, str):
                keys.add(x.slice.value)
            if isinstance(x, ast.Call) and isinstance(x.func, ast.Attribute) and x.func.attr == "get" and x.args and isinstance(x.args[0], ast.Constant) and isinstance(x.args[0].value, str):
                keys.add(x.args[0].value)
        result.append({"name": n.name, "line": n.lineno, "end_line": n.end_lineno,
                       "decorators": [ast.unparse(d) for d in n.decorator_list],
                       "literal_input_keys": sorted(keys),
                       "literal_object_keys": sorted({k.value for x in ast.walk(n) if isinstance(x, ast.Dict) for k in x.keys if isinstance(k, ast.Constant) and isinstance(k.value, str)}),
                       "keyword_arguments": sorted({k.arg for x in ast.walk(n) if isinstance(x, ast.Call) for k in x.keywords if k.arg}),
                       "calls": sorted({ast.unparse(x.func) for x in ast.walk(n) if isinstance(x, ast.Call)}),
                       "attributes": sorted({ast.unparse(x) for x in ast.walk(n) if isinstance(x, ast.Attribute)})})
    return result


def build(domain):
    base = REPO_ROOT / "backend/src/services" / domain
    schema = schema_inventory(base / "database/schema.py")
    if domain == "box":
        schema["enums"] = schema_inventory(base / "utils/enums.py")["enums"]
    source_files = sorted(base.rglob("*.py"))
    functions = {str(p.relative_to(REPO_ROOT)): function_inventory(p) for p in source_files}
    operations = []
    if domain == "linear":
        for f in functions[str((base / "api/resolvers.py").relative_to(REPO_ROOT))]:
            for d in f["decorators"]:
                call = ast.parse(d, mode="eval").body
                if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute) and call.func.attr == "field":
                    operations.append({"binding": ast.unparse(call.func.value), "field": ast.literal_eval(call.args[0]), "handler": f["name"], "line": f["line"]})
    else:
        for fname in (["routes.py"] if domain == "box" else ["methods.py", "batch.py"]):
            path = base / "api" / fname
            tree = ast.parse(path.read_text())
            funcs = {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
            for call in calls(tree, "Route"):
                route = ast.literal_eval(call.args[0]); handler = ast.unparse(call.args[1])
                methods = next(ast.literal_eval(k.value) for k in call.keywords if k.arg == "methods")
                for method in methods:
                    selected = handler
                    if handler.endswith("_handler") and handler != "batch_handler":
                        for branch in ast.walk(funcs[handler]):
                            if isinstance(branch, ast.If) and isinstance(branch.test, ast.Compare) and any(isinstance(v, ast.Constant) and v.value == method for v in branch.test.comparators):
                                targets = [x.value.value.func for x in branch.body if isinstance(x, ast.Return) and isinstance(x.value, ast.Await) and isinstance(x.value.value, ast.Call)]
                                if targets: selected = ast.unparse(targets[0])
                    operations.append({"method": method, "path": route, "handler": selected, "dispatcher": handler,
                                       "source": str(path.relative_to(REPO_ROOT)), "line": funcs[selected].lineno if selected in funcs else call.lineno})
    documentation = REPO_ROOT / f"examples/{domain}/testsuites/{domain}_docs/{domain}_api_full_docs.json"
    other_sources = [documentation]
    if domain == "linear": other_sources.append(base / "api/schema/Linear-API.graphql")
    other_sources.extend([REPO_ROOT / f"backend/utils/seed_{domain}_template.py", REPO_ROOT / "backend/src/platform/api/main.py"])
    return {"domain": domain, "interpretation": "Mechanical declaration inventory; semantic dispositions and reverse audit belong in model_source_ledger.md.",
            **schema, "operations": operations, "functions": functions,
            "source_sha256": {str(p.relative_to(REPO_ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files + other_sources}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", choices=["box", "calendar", "linear"])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    data = build(args.domain)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"tables": len(data["tables"]), "columns": sum(len(t["columns"]) for t in data["tables"]), "operation_bindings": len(data["operations"])}))


if __name__ == "__main__":
    main()
