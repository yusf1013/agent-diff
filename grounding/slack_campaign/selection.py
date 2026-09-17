"""Finite relational selectors for construction checks; no generated code execution.

These queries establish facts about a supplied seed. They do not establish that
the natural-language prompt expresses the query or that APIs reveal its inputs.
"""

from __future__ import annotations

import ast
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


SCHEMA_PATH = Path(__file__).resolve().parents[2] / "backend/src/services/slack/database/schema.py"
EXPOSED_TABLES = frozenset({"teams", "users", "channels", "messages", "user_teams", "channel_members", "message_reactions"})
OPS = frozenset({"eq", "ne", "in", "not_in", "contains_ci", "lt", "le", "gt", "ge"})
COUNT_OPS = frozenset({"eq", "ne", "lt", "le", "gt", "ge"})

SELECTOR_GUIDE = """The private.selector object has root_table, scope, focal, auxiliary.
scope is a conjunction of root-field filters; [] covers every root row. Never
restrict scope to the intended answers unless the request supplies that scope.
focal and each auxiliary are queries with path (table names), joins (one per
step), and filters (conjoined node-indexed real-field comparisons). A join is
the foreign-key name table.field, usable in either direction; it must connect
the adjacent tables. Each joined tuple preserves the identities along the path.
Operations: eq, ne, in, not_in, contains_ci, lt, le, gt, ge. Values use seed types;
in/not_in require a list. Filters have {node:0,field:'message_text',op:'contains_ci',value:'rollout'};
scope filters omit node. Every query starts at root_table. Without count it
requires at least one complete matching tuple. Optional count:{node:N,op:'eq',value:3}
counts DISTINCT row handles at N in complete matching tuples, not join rows.
Count comparisons also allow ne,lt,le,gt,ge; no tuples means zero. For a direct
member count use path ['channels','channel_members'], join
['channel_members.channel_id'], count node 1. No arbitrary Python, SQL, aliases,
or invented fields. Scalar-primary-key handles are their string IDs. Composite
handles are objects of exactly the actual PK fields, e.g.
{message_id:'1712345678.000001',user_id:'U1',reaction_type:'thumbsup'}. Lists contain distinct handles.
API compatibility: every new messages.message_id must be a timestamp-like numeric
string whose float conversion is finite (e.g. '1712345678.000001'); Slack history
parses message_id as a number. Cards, reactions, parents, and handles use that
actual ID.
Example:
{"root_table":"messages","scope":[],"focal":{
 "path":["messages","message_reactions","users","channel_members","channels"],
 "joins":["message_reactions.message_id","message_reactions.user_id","channel_members.user_id","channel_members.channel_id"],
 "filters":[{"node":4,"field":"channel_name","op":"eq","value":"security"}]},
 "auxiliary":[{"path":["messages"],"joins":[],"filters":[
 {"node":0,"field":"message_text","op":"contains_ci","value":"rollout"}]}]}
"""


class SelectorError(ValueError):
    pass


@dataclass(frozen=True)
class Column:
    kind: str
    nullable: bool
    primary_key: bool = False
    unique: bool = False
    maximum_length: int | None = None
    foreign_key: str | None = None
    enum_values: tuple[str, ...] = ()
    has_default: bool = False
    literal_default: Any = None
    dynamic_default: bool = False


@dataclass(frozen=True)
class Table:
    columns: dict[str, Column]
    unique_groups: tuple[tuple[str, ...], ...]

    @property
    def primary_key(self) -> tuple[str, ...]:
        return tuple(name for name, col in self.columns.items() if col.primary_key)


def _literal(node: ast.AST, default: Any = None) -> Any:
    try:
        return ast.literal_eval(node)
    except (ValueError, TypeError):
        return default


def read_schema(path: Path = SCHEMA_PATH) -> dict[str, Table]:
    """Read real ORM declarations with AST; no SQLAlchemy/import side effects."""
    tree = ast.parse(path.read_text())
    enums = {}
    for cls in (n for n in tree.body if isinstance(n, ast.ClassDef)):
        if any(isinstance(base, ast.Name) and base.id == "PyEnum" for base in cls.bases):
            enums[cls.name] = tuple(_literal(n.value) for n in cls.body if isinstance(n, ast.Assign))
    tables = {}
    for cls in (n for n in tree.body if isinstance(n, ast.ClassDef)):
        table_name = next((_literal(n.value) for n in cls.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "__tablename__" for t in n.targets)), None)
        if table_name is None:
            continue
        columns, unique_groups = {}, []
        for node in cls.body:
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "__table_args__" for t in node.targets):
                for call in ast.walk(node.value):
                    if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id == "UniqueConstraint":
                        unique_groups.append(tuple(_literal(x) for x in call.args))
            if not isinstance(node, ast.AnnAssign) or not isinstance(node.target, ast.Name):
                continue
            call = node.value
            if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name) or call.func.id != "mapped_column":
                continue
            opts = {x.arg: x.value for x in call.keywords}
            annotation = ast.unparse(node.annotation)
            kind = "datetime" if "datetime" in annotation else "bool" if "bool" in annotation else "int" if "int" in annotation else "json" if "list" in annotation else "str"
            fk, maximum_length, enum_values = None, None, ()
            for arg in call.args:
                if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name):
                    if arg.func.id == "ForeignKey":
                        fk = _literal(arg.args[0])
                    elif arg.func.id == "String":
                        maximum_length = _literal(arg.args[0])
                    elif arg.func.id == "Enum":
                        enum_values = enums[ast.unparse(arg.args[0])]
            pk = bool(_literal(opts.get("primary_key")))
            nullable = bool(_literal(opts["nullable"])) if "nullable" in opts else "None" in annotation and not pk
            default_node = opts.get("default", opts.get("server_default"))
            has_default = default_node is not None
            literal_default = _literal(default_node)
            dynamic_default = has_default and not isinstance(default_node, (ast.Constant, ast.List, ast.Dict, ast.Tuple))
            if kind == "bool" and isinstance(literal_default, str):
                literal_default = {"true": True, "false": False}.get(literal_default.lower(), literal_default)
            columns[node.target.id] = Column(kind, nullable, pk, bool(_literal(opts.get("unique"))), maximum_length, fk, enum_values, has_default, literal_default, dynamic_default)
        tables[table_name] = Table(columns, tuple(unique_groups))
    return tables


SCHEMA = read_schema()


def canonical_handle(table: str, row: dict[str, Any]) -> str | dict[str, str]:
    """Return a stable external handle using only actual primary-key fields."""
    if table not in SCHEMA:
        raise SelectorError(f"unknown table {table!r}")
    fields = SCHEMA[table].primary_key
    if not all(field in row and isinstance(row[field], str) and row[field] for field in fields):
        raise SelectorError(f"{table}: missing/non-string primary key in {row!r}")
    return row[fields[0]] if len(fields) == 1 else {field: row[field] for field in fields}


def handle_key(table: str, handle: Any) -> str:
    fields = SCHEMA[table].primary_key
    if len(fields) == 1:
        if not isinstance(handle, str) or not handle:
            raise SelectorError(f"{table} handle must be a nonempty string ID")
    else:
        if not isinstance(handle, dict) or set(handle) != set(fields) or not all(isinstance(handle[x], str) and handle[x] for x in fields):
            raise SelectorError(f"{table} handle must contain exactly {list(fields)} with string values")
    return json.dumps(handle, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _typed(value: Any, column: Column) -> bool:
    if value is None:
        return column.nullable
    if column.enum_values:
        return value in column.enum_values
    if column.kind == "str":
        return isinstance(value, str) and (column.maximum_length is None or len(value) <= column.maximum_length)
    if column.kind == "bool":
        return type(value) is bool
    if column.kind == "int":
        return type(value) is int
    if column.kind == "datetime":
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
            return isinstance(value, str)
        except (TypeError, ValueError, AttributeError):
            return False
    if column.kind == "json":
        return isinstance(value, list)
    return False


def validate_seed(seed: Any) -> list[str]:
    """Check every supplied table, real field, PK/unique constraint and FK."""
    errors = []
    if not isinstance(seed, dict):
        return ["seed must be an object mapping real table names to row arrays"]
    for table in seed:
        if table not in SCHEMA:
            errors.append(f"seed: unknown table {table!r}")
    for table, metadata in SCHEMA.items():
        rows = seed.get(table, [])
        if not isinstance(rows, list):
            errors.append(f"seed.{table} must be an array")
            continue
        constraints = [metadata.primary_key, *metadata.unique_groups, *((name,) for name, col in metadata.columns.items() if col.unique)]
        seen = {fields: set() for fields in constraints}
        for i, row in enumerate(rows):
            where = f"seed.{table}[{i}]"
            if not isinstance(row, dict):
                errors.append(f"{where} must be an object")
                continue
            for field in row.keys() - metadata.columns.keys():
                errors.append(f"{where}: unknown field {field!r}")
            for field, column in metadata.columns.items():
                if field not in row:
                    if not column.nullable and not column.has_default:
                        errors.append(f"{where}: required field {field!r} missing")
                    continue
                value = row[field]
                if not _typed(value, column):
                    errors.append(f"{where}.{field}: invalid {column.kind} value {value!r}")
                if column.foreign_key and value is not None:
                    target, target_field = column.foreign_key.split(".")
                    target_rows = seed.get(target, [])
                    if not isinstance(target_rows, list) or not any(isinstance(r, dict) and r.get(target_field) == value for r in target_rows):
                        errors.append(f"{where}.{field}: {value!r} does not reference {column.foreign_key}")
            for fields in constraints:
                values = tuple(row.get(field) for field in fields)
                if any(value is None for value in values):
                    continue  # PostgreSQL UNIQUE permits NULLs; required checks above handle PKs.
                key = json.dumps(values, sort_keys=True)
                if key in seen[fields]:
                    errors.append(f"{where}: duplicate unique key {fields}={values!r}")
                seen[fields].add(key)
    return errors


def _field_value(table: str, row: dict, field: str) -> Any:
    column = SCHEMA[table].columns[field]
    if field in row:
        return row[field]
    if column.dynamic_default:
        raise SelectorError(f"{table}.{field}: dynamic database default must be supplied explicitly when used by a selector")
    if column.has_default:
        return column.literal_default
    return None


def _compare(left: Any, op: str, right: Any) -> bool:
    if op == "eq":
        return type(left) is type(right) and left == right
    if op == "ne":
        return not _compare(left, "eq", right)
    if op in {"in", "not_in"}:
        answer = any(_compare(left, "eq", value) for value in right)
        return answer if op == "in" else not answer
    if op == "contains_ci":
        return isinstance(left, str) and right.casefold() in left.casefold()
    if left is None or right is None:
        return False
    try:
        return {"lt": lambda: left < right, "le": lambda: left <= right, "gt": lambda: left > right, "ge": lambda: left >= right}[op]()
    except TypeError as exc:
        raise SelectorError(f"incomparable values {left!r} {op} {right!r}") from exc


def _check_filter(f: Any, path: list[str], *, scope: bool = False) -> None:
    allowed = {"field", "op", "value"} if scope else {"node", "field", "op", "value"}
    if not isinstance(f, dict) or set(f) != allowed:
        raise SelectorError(f"filter must contain exactly {sorted(allowed)}")
    node = 0 if scope else f["node"]
    if type(node) is not int or not 0 <= node < len(path):
        raise SelectorError(f"filter node index {node!r} outside path")
    table = path[node]
    if f["field"] not in SCHEMA[table].columns:
        raise SelectorError(f"filter uses unknown real field {table}.{f['field']}")
    if f["op"] not in OPS:
        raise SelectorError(f"unsupported filter op {f['op']!r}")
    value, column = f["value"], SCHEMA[table].columns[f["field"]]
    if f["op"] in {"in", "not_in"}:
        if not isinstance(value, list) or not all(_typed(v, column) for v in value):
            raise SelectorError(f"{table}.{f['field']} {f['op']} requires a list of correctly typed values")
    elif not _typed(value, column):
        raise SelectorError(f"filter value has wrong type for {table}.{f['field']}")
    if f["op"] == "contains_ci" and (column.kind != "str" or not isinstance(value, str)):
        raise SelectorError("contains_ci requires a string field and value")
    if column.kind == "json" and f["op"] not in {"eq", "ne", "in", "not_in"}:
        raise SelectorError("structured JSON only supports equality/membership filters")


def _join_fields(left: str, right: str, join: str) -> tuple[str, str]:
    if not isinstance(join, str) or join.count(".") != 1:
        raise SelectorError(f"join must be a real foreign-key name, got {join!r}")
    owner, field = join.split(".")
    column = SCHEMA.get(owner, Table({}, ())).columns.get(field)
    if column is None or not column.foreign_key:
        raise SelectorError(f"{join!r} is not a foreign key")
    target, target_field = column.foreign_key.split(".")
    if left == owner and right == target:
        return field, target_field
    if left == target and right == owner:
        return target_field, field
    raise SelectorError(f"{join!r} does not connect {left!r} and {right!r}")


def validate_query(query: Any, root_table: str) -> None:
    if not isinstance(query, dict) or not {"path", "joins", "filters"} <= set(query) or set(query) - {"path", "joins", "filters", "count"}:
        raise SelectorError("query requires path, joins, filters, and optional count only")
    path = query["path"]
    if not isinstance(path, list) or not path or path[0] != root_table or any(t not in EXPOSED_TABLES for t in path):
        raise SelectorError("query path must start at root_table and use exposed real tables")
    if len(path) > 8:
        raise SelectorError("query path is longer than this finite selector contract supports")
    joins = query["joins"]
    if not isinstance(joins, list) or len(joins) != len(path) - 1:
        raise SelectorError("query joins must have exactly len(path)-1 entries")
    for i, join in enumerate(joins):
        _join_fields(path[i], path[i + 1], join)
    if not isinstance(query["filters"], list):
        raise SelectorError("query filters must be an array")
    for f in query["filters"]:
        _check_filter(f, path)
    if "count" in query:
        count = query["count"]
        if not isinstance(count, dict) or set(count) != {"node", "op", "value"}:
            raise SelectorError("count requires node, op, value")
        if type(count["node"]) is not int or not 0 <= count["node"] < len(path) or count["op"] not in COUNT_OPS or type(count["value"]) is not int or count["value"] < 0:
            raise SelectorError("invalid count node, operator or nonnegative integer value")


def query_matches(seed: dict, root: dict, query: dict) -> bool:
    """Existential/path-count query, evaluated with bound row identities."""
    path = query["path"]
    filters = [[] for _ in path]
    for f in query["filters"]:
        filters[f["node"]].append(f)

    def accepts(node: int, row: dict) -> bool:
        for f in filters[node]:
            value = _field_value(path[node], row, f["field"])
            comparison = f["value"]
            if SCHEMA[path[node]].columns[f["field"]].kind == "datetime" and f["op"] in {"lt", "le", "gt", "ge"} and value is not None:
                value = datetime.fromisoformat(value.replace("Z", "+00:00"))
                comparison = datetime.fromisoformat(comparison.replace("Z", "+00:00"))
            if not _compare(value, f["op"], comparison):
                return False
        return True

    def walk(bound: list[dict]):
        node = len(bound) - 1
        if not accepts(node, bound[-1]):
            return
        if node == len(path) - 1:
            yield bound
            return
        left, right = _join_fields(path[node], path[node + 1], query["joins"][node])
        value = _field_value(path[node], bound[-1], left)
        if value is None:
            return
        for row in seed.get(path[node + 1], []):
            if _field_value(path[node + 1], row, right) == value:
                yield from walk([*bound, row])

    tuples = walk([root])
    if "count" not in query:
        return next(tuples, None) is not None
    count = query["count"]
    node = count["node"]
    keys = {handle_key(path[node], canonical_handle(path[node], bound[node])) for bound in tuples}
    return _compare(len(keys), count["op"], count["value"])


def evaluate_selector(seed: dict, selector: Any) -> dict[str, list[Any]]:
    if not isinstance(selector, dict) or set(selector) != {"root_table", "scope", "focal", "auxiliary"}:
        raise SelectorError("selector requires exactly root_table, scope, focal, auxiliary")
    table = selector["root_table"]
    if table not in EXPOSED_TABLES:
        raise SelectorError(f"unsupported root table {table!r}")
    if not isinstance(selector["scope"], list) or not isinstance(selector["auxiliary"], list):
        raise SelectorError("scope and auxiliary must be arrays")
    for f in selector["scope"]:
        _check_filter(f, [table], scope=True)
    validate_query(selector["focal"], table)
    for query in selector["auxiliary"]:
        validate_query(query, table)
    scoped, matches, negatives, focal_matches = [], [], [], []
    for row in seed.get(table, []):
        if not all(_compare(_field_value(table, row, f["field"]), f["op"], f["value"]) for f in selector["scope"]):
            continue
        handle = canonical_handle(table, row)
        scoped.append(handle)
        focal = query_matches(seed, row, selector["focal"])
        auxiliary = all(query_matches(seed, row, q) for q in selector["auxiliary"])
        if focal:
            focal_matches.append(handle)
        if auxiliary:
            (matches if focal else negatives).append(handle)
    return {"population": scoped, "matches": matches, "focal_matches": focal_matches, "focal_negatives": negatives}
