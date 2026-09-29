"""Seed operations for the automation, generic over the four services' tables.

- `pk(domain, table)`: a table's primary-key columns, from the replica's schema (autogen_01's derive).
- `find_row(case, table, key)`: a record by its key.
- `clone(seed, domain, table, key, overrides)`: a copy of a record under a new key, with copies of every row that
  references it by that key (attendees, comments, reactions, versions…), so a condition that looks at related rows
  still holds for the copy. Overrides set the copy's own fields (a new text, a new container, a new time).
The reference query decides afterwards whether a copy matches (fdc.check_reference).
"""
from __future__ import annotations

import copy
from functools import lru_cache

from grounding.runs.autogen_01.kit import derive


@lru_cache(maxsize=None)
def pk(domain: str, table: str) -> tuple:
    try:
        return tuple(derive.effect_key(domain, table))
    except Exception:  # a table the schema does not know: fall back to the usual names
        return ("id",)


def key_of(domain, table, row):
    cols = pk(domain, table)
    return str(row.get(cols[0])) if cols and cols[0] in row else str(row.get("id"))


def find_row(case, table, key):
    for row in case["seed"].get(table) or []:
        if key_of(case["domain"], table, row) == str(key):
            return row
    return None


def _new_key(domain, table, rows, old, n):
    """A fresh key for a copy: the next number for numeric keys, a suffix otherwise."""
    col = pk(domain, table)[0]
    values = [r.get(col) for r in rows]
    if isinstance(old, int):
        return max(v for v in values if isinstance(v, int)) + 1
    if isinstance(old, str) and old.isdigit():
        return str(max(int(v) for v in values if isinstance(v, str) and v.isdigit()) + 1)
    if table == "messages" and isinstance(old, str) and "." in old:  # Slack ts: seconds.sequence
        return old  # the caller sets the ts (it is also the message's time)
    return f"{old}-sm{n}"


def dependents(seed, domain, table, key):
    """Rows of other tables (and same-table rows other than the record) that hold the record's key in a column."""
    out = []
    for t, rows in seed.items():
        if not isinstance(rows, list):
            continue
        own = pk(domain, t)[0] if t == table else None
        for r in rows:
            if t == table and key_of(domain, t, r) == str(key):
                continue
            cols = [c for c, v in r.items() if c != own and not c.startswith("__") and v is not None
                    and not isinstance(v, (list, dict)) and str(v) == str(key)]
            if cols:
                out.append((t, r, cols))
    return out


_counter = {"n": 0}


def _copy_dependents(seed, domain, table, key, nk, depth, root):
    """Copy the rows that reference `key`, pointing them at `nk`; follow one more level for rows that got a new key
    (a task's assignments). Association rows keep their composite key, with the reference swapped."""
    for t, r, cols in dependents(seed, domain, table, key):
        if t in (table, root):  # replies and other same-table references stay with the original
            continue
        dep = copy.deepcopy(r)
        pkc = pk(domain, t)
        new_dep_key = None
        if len(pkc) == 1 and pkc[0] in r and pkc[0] not in cols:
            new_dep_key = _new_key(domain, t, seed[t], r.get(pkc[0]), _counter["n"])
            dep[pkc[0]] = new_dep_key
        for c in cols:
            dep[c] = nk
        seed[t].append(dep)
        if depth > 1 and new_dep_key is not None:
            _copy_dependents(seed, domain, t, str(r.get(pkc[0])), new_dep_key, depth - 1, root)


def clone(seed, domain, table, key, overrides=None, new_key=None, follow=True):
    """Copy a record (and the rows that reference it) under a new key; returns the new key."""
    rows = seed[table]
    src = next(r for r in rows if key_of(domain, table, r) == str(key))
    _counter["n"] += 1
    col = pk(domain, table)[0]
    nk = new_key if new_key is not None else _new_key(domain, table, rows, src.get(col), _counter["n"])
    new = copy.deepcopy(src)
    new[col] = nk
    new.update(overrides or {})
    rows.append(new)
    if follow:
        _copy_dependents(seed, domain, table, key, nk, 2, table)
    return nk
