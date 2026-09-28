"""Opaque ids for a test: every made-up id gets a random-looking id in its service's own format, the same way
throughout the test. Decided on 2026-09-28 (grounding/protocols/roadmap.md, the discussion after 6a): ids that name
a record's role or the difference under test ("ev_target", "ev_budget_free") hand the answer to the agent, which
reads them through the API, and a writer should not have to think about ids.

What changes:
- **Made-up ids:** the value of every single-column primary key in the seed, unless it is a number (Box ids, Slack
  message timestamps), the acting user's id, or a person's email (a primary calendar's id).
- **Everywhere they occur:** as a whole string anywhere in the test (a foreign key, an expected id, a witness, a
  query filter's value, a dict key), and as a whole token inside text (a URL's last segment, a claim's explanation,
  a Slack mention). The request is never changed: `obfuscate` raises if a made-up id occurs in it.
- **Fields that copy an id** get a value in the service's form: Calendar's `etag` and `ical_uid`, and Linear's
  `inviteHash`. (Linear's `slugId` and `url` carry the id whole or as a URL segment, and follow it.)
- **Formats:** Slack keeps a valid first letter (C, G, D for conversations; U, W, B for users; T for workspaces)
  and adds 10 upper-case letters and digits. Linear ids are UUIDs. Google Calendar event ids are 26 base32hex
  characters, secondary calendars `c_<26 hex>@group.calendar.google.com`, other Calendar rows 24 hex characters. A
  made-up Box id becomes a 12-digit number. All fit the replica's columns.
- **Deterministic** in (scenario, old id): every test of a scenario, and every run of this function, agrees. The
  mapping is returned, so rulings and verdicts that name old ids can be translated.

`check(original, opaque, mapping)` verifies one test: the request is unchanged; every other difference is a
replaced id, a rewritten copy field or the digest; no made-up id is left anywhere; and the reference check
(`fdc.check_reference`) selects and credits the same records, under their new ids.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
import uuid

SALT = "opaque-ids-v1"
NUMBER = re.compile(r"[\d.]+")
SLACK_PREFIXES = {"channels": "CGD", "users": "UWB", "teams": "T"}
ALNUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
B32HEX = "0123456789abcdefghijklmnopqrstuv"
COPY_FIELDS = {"calendar": ("etag", "ical_uid"), "linear": ("inviteHash",)}
TEXT_KEYS = ("prompt",)  # never changed


def _hash(scenario: str, text: str) -> bytes:
    return hashlib.sha256(f"{SALT}:{scenario}:{text}".encode()).digest()


def _encode(h: bytes, alphabet: str, n: int) -> str:
    number, out = int.from_bytes(h, "big"), []
    for _ in range(n):
        number, r = divmod(number, len(alphabet))
        out.append(alphabet[r])
    return "".join(out)


def new_id(domain: str, table: str, scenario: str, old: str) -> str:
    h = _hash(scenario, old)
    if domain == "slack":
        allowed = SLACK_PREFIXES.get(table, "")
        prefix = old[0] if old[:1] and old[0] in allowed else (allowed[:1] or "X")
        return prefix + _encode(h, ALNUM, 10)
    if domain == "linear":
        return str(uuid.UUID(bytes=h[:16], version=4))
    if domain == "calendar":
        if table == "calendars":
            return f"c_{h.hex()[:26]}@group.calendar.google.com"
        if table == "calendar_events":
            return _encode(h, B32HEX, 26)
        return h.hex()[:24]
    if domain == "box":
        return str(int.from_bytes(h[:8], "big") % 10 ** 12).zfill(12)
    raise ValueError(f"no id format for {domain}")


def _primary_keys(domain: str) -> dict[str, list[str]]:
    from grounding.runs.autogen_01.kit.seedops import _metadata
    return {name: [c.name for c in t.primary_key.columns] for name, t in _metadata(domain).tables.items()}


def made_up_ids(case: dict) -> dict[str, str]:
    """old id -> its table, for the made-up ids of one test's seed."""
    domain, seed = case["domain"], case["seed"]
    keys = _primary_keys(domain)
    people = {str(r["email"]) for t in ("calendar_users", "users", "box_users") for r in seed.get(t, [])
              if isinstance(r, dict) and r.get("email")}
    out = {}
    for table, rows in seed.items():
        key = keys.get(table)
        if not isinstance(rows, list) or not key or len(key) != 1:
            continue
        for row in rows:
            value = row.get(key[0]) if isinstance(row, dict) else None
            if (isinstance(value, str) and value and not NUMBER.fullmatch(value)
                    and value != case.get("acting_user_id") and value not in people):
                out.setdefault(value, table)
    return out


def mapping_for(scenario: str, cases: list[dict]) -> dict[str, str]:
    """old -> new for every made-up id in any of a scenario's tests (they share one mapping)."""
    tables: dict[str, str] = {}
    domain = cases[0]["domain"]
    for case in cases:
        for old, table in made_up_ids(case).items():
            if tables.setdefault(old, table) != table:
                raise ValueError(f"{scenario}: id {old!r} is a key of both {tables[old]} and {table}")
    mapping = {old: new_id(domain, table, scenario, old) for old, table in sorted(tables.items())}
    if len(set(mapping.values())) != len(mapping):
        raise ValueError(f"{scenario}: two ids map to the same new id")
    return mapping


def _pattern(mapping: dict[str, str]) -> re.Pattern | None:
    """Whole-token occurrences of the distinctive ids (3+ characters with a separator or a digit) inside text."""
    ids = sorted((i for i in mapping if len(i) >= 3 and re.search(r"[-_@.:\d]", i)), key=len, reverse=True)
    if not ids:
        return None
    return re.compile(rf"(?<![A-Za-z0-9_.-])(?:{'|'.join(map(re.escape, ids))})(?![A-Za-z0-9_@-]|\.[A-Za-z0-9])")


def occurrences(text: str, mapping: dict[str, str]) -> list[str]:
    """The made-up ids that occur in text, whole or inside other characters (3+ characters long). New ids are
    removed first: a short old id ("c-1") can occur inside a random new one by chance."""
    for new in mapping.values():
        text = text.replace(new, " ")
    return sorted(i for i in mapping if len(i) >= 3 and i in text)


def _replace(value, mapping, pattern):
    if isinstance(value, dict):
        return {(mapping.get(k, k) if isinstance(k, str) else k): _replace(v, mapping, pattern) for k, v in value.items()}
    if isinstance(value, list):
        return [_replace(v, mapping, pattern) for v in value]
    if isinstance(value, str):
        if value in mapping:
            return mapping[value]
        if pattern is not None:
            return pattern.sub(lambda m: mapping[m.group(0)], value)
    return value


def obfuscate(case: dict, scenario: str, mapping: dict[str, str]) -> dict:
    """The test with opaque ids (a new dict; `case` is unchanged), its digest recomputed."""
    from grounding.runs.autogen_01.kit.derive import digest
    found = occurrences(case["prompt"], mapping)
    if found:
        raise ValueError(f"{case['case_id']}: the request names made-up ids {found}; they cannot change")
    pattern = _pattern(mapping)
    out = {}
    for k, v in case.items():
        if k in TEXT_KEYS or k == "case_sha256":
            out[k] = copy.deepcopy(v)
        elif k == "task_spec":  # its lines are the request's text
            out[k] = [{**line, **{kk: _replace(vv, mapping, pattern) for kk, vv in line.items() if kk != "text"}}
                      for line in v]
        else:
            out[k] = _replace(v, mapping, pattern)
    for table, rows in out["seed"].items():
        original = case["seed"].get(table)
        for i, row in enumerate(rows if isinstance(rows, list) else []):
            for field in COPY_FIELDS.get(case["domain"], ()):
                before = original[i].get(field) if isinstance(original, list) and isinstance(original[i], dict) else None
                if not isinstance(before, str) or not occurrences(before, mapping):
                    continue
                if field == "ical_uid":
                    row[field] = f"{row['id']}@google.com"
                elif field == "etag":
                    row[field] = f'"{_hash(scenario, "etag:" + before).hex()[:16]}"'
                else:
                    row[field] = _hash(scenario, f"{field}:{before}").hex()[:16]
    if "case_sha256" in case:
        out["case_sha256"] = digest({k: v for k, v in out.items() if k != "case_sha256"})
    return out


def _leaves(value, path=""):
    if isinstance(value, dict):
        for k, v in value.items():
            yield from _leaves(v, f"{path}.{k}")
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from _leaves(v, f"{path}[{i}]")
    else:
        yield path, value


def _results(case: dict) -> list:
    from grounding.runs.fact_coverage_01 import fdc
    seed = copy.deepcopy(case["seed"])
    for table, rows in case.get("derived_rows", {}).items():
        seed[table] = rows
    return [fdc.check_reference(seed, r) for r in case["references"]]


def check(original: dict, opaque: dict, mapping: dict[str, str]) -> list[str]:
    """Problems with one obfuscated test (empty when it is faithful)."""
    from grounding.runs.autogen_01.kit.derive import digest
    problems = []
    if opaque["prompt"] != original["prompt"]:
        problems.append("the request changed")
    renamed = _replace(copy.deepcopy(original), {k: mapping[k] for k in mapping}, None)  # dict keys renamed
    left, right = dict(_leaves(renamed)), dict(_leaves(opaque))
    if set(left) != set(right):
        problems.append(f"structure differs: {sorted(set(left) ^ set(right))[:5]}")
    copy_fields = COPY_FIELDS.get(original["domain"], ())
    old_leaves = dict(_leaves(original))
    for path, value in right.items():
        before = left.get(path)
        if before == value or path == ".case_sha256":
            continue
        field = path.rsplit(".", 1)[-1]
        source = old_leaves.get(path, before)
        if field in copy_fields or (isinstance(source, str) and occurrences(source, mapping)):
            continue
        problems.append(f"{path}: {source!r} -> {value!r} is not an id change")
    for path, value in right.items():
        if isinstance(value, str) and not path.startswith((".prompt", ".task_spec")):
            left_over = occurrences(value, mapping)
            if left_over:
                problems.append(f"{path}: still names {left_over}")
    if opaque.get("case_sha256") and opaque["case_sha256"] != digest({k: v for k, v in opaque.items()
                                                                      if k != "case_sha256"}):
        problems.append("stale case_sha256")
    pattern = _pattern(mapping)
    expected = _replace(json.loads(json.dumps(_results(original))), mapping, pattern)  # the checker returns tuples
    got = json.loads(json.dumps(_results(opaque)))
    if expected != got:
        problems.append("the reference check differs under the new ids")
    kept = set(made_up_ids(opaque)) & set(mapping)
    if kept:
        problems.append(f"old ids still keys of the seed: {sorted(kept)[:5]}")
    return problems
