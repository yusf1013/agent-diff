"""Mechanical campaign checks. Passing is not semantic or API-access certification."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any

from .selection import (
    SCHEMA, SelectorError, canonical_handle, evaluate_selector, handle_key,
    validate_seed,
)


COMMON_CARD_FIELDS = {
    "Test ID", "Task type", "Grounding obligations", "Grounding obligation name",
    "Grounding obligation description", "Resolution", "Shared scope", "Referent set",
    "Alternative sufficient identifying sets",
}
READ_FIELDS = {"Answer-computation attributes"}
WRITE_FIELDS = {"Change-computation attributes", "Written attributes"}


def _handle_set(table: str, values: Any, label: str, errors: list[str]) -> set[str] | None:
    if not isinstance(values, list):
        errors.append(f"{label} must be an array of row handles")
        return None
    keys = set()
    for value in values:
        try:
            key = handle_key(table, value)
        except SelectorError as exc:
            errors.append(f"{label}: {exc}")
            continue
        if key in keys:
            errors.append(f"{label} repeats handle {value!r}")
        keys.add(key)
    return keys


def _candidate_sets(table: str, values: Any, label: str, errors: list[str]) -> list[set[str]] | None:
    if not isinstance(values, list) or len(values) < 2:
        errors.append(f"{label} must give at least two distinct candidate sets")
        return None
    sets = [_handle_set(table, value, f"{label}[{i}]", errors) for i, value in enumerate(values)]
    if any(value is None for value in sets):
        return None
    if len({frozenset(s) for s in sets}) != len(sets):
        errors.append(f"{label} repeats an alternative candidate set")
    return sets


def _validate_inventory(case: dict, errors: list[str]) -> None:
    cards = case.get("cards")
    if not isinstance(cards, list):
        errors.append("cards must be an array of raw fixed-schema cards")
        return
    known_handles = set()
    for table, rows in case.get("seed", {}).items():
        if table in SCHEMA and isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict):
                    try:
                        known_handles.add(handle_key(table, canonical_handle(table, row)))
                    except SelectorError:
                        pass  # Already reported by seed checks.
    for i, card in enumerate(cards, 1):
        label = f"cards[{i - 1}] (O{i})"
        if not isinstance(card, dict):
            errors.append(f"{label} must be an object")
            continue
        task_type = card.get("Task type")
        if task_type not in {"read-only", "state-changing"}:
            errors.append(f"{label}: invalid Task type")
        expected_fields = COMMON_CARD_FIELDS | (READ_FIELDS if task_type == "read-only" else WRITE_FIELDS)
        if "Identifying paths" in card:
            expected_fields = expected_fields | {"Identifying paths"}
            paths = card["Identifying paths"]
            if not isinstance(paths, list) or not paths:
                errors.append(f"{label}: Identifying paths must be a nonempty array")
            else:
                for path in paths:
                    if not isinstance(path, dict) or set(path) != {"entities", "relationships"}:
                        errors.append(f"{label}: path requires entities and relationships")
                    elif not path["entities"] or len(path["relationships"]) != len(path["entities"])-1:
                        errors.append(f"{label}: path must have one relationship per adjacent entity pair")
        if set(card) != expected_fields:
            errors.append(f"{label}: fixed card fields differ; missing={sorted(expected_fields - set(card))}, extra={sorted(set(card) - expected_fields)}")
        if card.get("Test ID") != case.get("case_id"):
            errors.append(f"{label}: Test ID must equal case_id")
        if type(card.get("Grounding obligations")) is not int or card.get("Grounding obligations") != len(cards):
            errors.append(f"{label}: Grounding obligations must equal card count")
        for field in ("Grounding obligation name", "Grounding obligation description", "Shared scope"):
            if not isinstance(card.get(field), str) or not card[field].strip():
                errors.append(f"{label}: {field} must be nonempty text")
        resolution = card.get("Resolution")
        referents = card.get("Referent set")
        if resolution in {"resolved", "absent"}:
            if not isinstance(referents, list):
                errors.append(f"{label}: resolved/absent Referent set must be an array")
            elif resolution == "absent" and referents:
                errors.append(f"{label}: absent Referent set must be empty")
            elif resolution == "resolved" and not referents:
                errors.append(f"{label}: resolved Referent set must not be empty")
            elif resolution == "resolved":
                for handle in referents:
                    key = json.dumps(handle, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
                    if key not in known_handles:
                        errors.append(f"{label}: referent handle {handle!r} is absent from the seed")
        elif resolution == "underspecified":
            if not isinstance(referents, dict) or set(referents) != {"selection", "partial_constraints", "candidate_sets"}:
                errors.append(f"{label}: underspecified Referent set requires selection, partial_constraints, candidate_sets")
            else:
                if not isinstance(referents["selection"], str) or not referents["selection"].startswith(("one(", "set(")) or not referents["selection"].endswith(")"):
                    errors.append(f"{label}: selection must be one(entity) or set(entity)")
                if not isinstance(referents["partial_constraints"], list):
                    errors.append(f"{label}: partial_constraints must be an array")
                if referents["candidate_sets"] is not None and not isinstance(referents["candidate_sets"], list):
                    errors.append(f"{label}: candidate_sets must be an array or null")
        else:
            errors.append(f"{label}: Resolution must be resolved, absent, or underspecified")
        for field in ("Alternative sufficient identifying sets", "Answer-computation attributes", "Change-computation attributes"):
            if field in card and card[field] is not None and (not isinstance(card[field], list) or not all(isinstance(group, list) and all(isinstance(item, str) for item in group) for group in card[field])):
                errors.append(f"{label}: {field} must be nested string arrays or null")
            elif isinstance(card.get(field), list):
                for group in card[field]:
                    for attribute in group:
                        if re.fullmatch(r"[A-Za-z_]\w*\.[A-Za-z_]\w*", attribute):
                            table, column = attribute.split(".")
                            if table not in SCHEMA or column not in SCHEMA[table].columns:
                                errors.append(f"{label}: {field} names unknown real field {attribute!r}")
        if "Written attributes" in card and (not isinstance(card["Written attributes"], list) or not all(isinstance(field, str) for field in card["Written attributes"])):
            errors.append(f"{label}: Written attributes must be a string array")
        elif isinstance(card.get("Written attributes"), list):
            for attribute in card["Written attributes"]:
                if re.fullmatch(r"[A-Za-z_]\w*\.[A-Za-z_]\w*", attribute):
                    table, column = attribute.split(".")
                    if table not in SCHEMA or column not in SCHEMA[table].columns:
                        errors.append(f"{label}: Written attributes names unknown real field {attribute!r}")
    spec = case.get("task_spec")
    if not isinstance(spec, list) or not spec:
        errors.append("task_spec must be a nonempty array")
        return
    linked = set()
    for index, line in enumerate(spec, 1):
        label = f"task_spec[{index - 1}]"
        if not isinstance(line, dict) or set(line) != {"line", "text", "obligations"}:
            errors.append(f"{label} requires exactly line, text, obligations")
            continue
        if type(line["line"]) is not int or line["line"] != index:
            errors.append(f"{label}: line numbers must be contiguous, starting at 1")
        if not isinstance(line["text"], str) or not line["text"].strip():
            errors.append(f"{label}: text must be nonempty")
        links = line["obligations"]
        if not isinstance(links, list) or any(type(x) is not int or not 1 <= x <= len(cards) for x in links):
            errors.append(f"{label}: obligations must be valid 1-based card indices")
        else:
            if len(set(links)) != len(links):
                errors.append(f"{label}: repeated obligation link")
            linked.update(links)
    missing = set(range(1, len(cards) + 1)) - linked
    if missing:
        errors.append(f"cards have no task-spec links: {sorted(missing)}")


def validate_case(case: Any) -> dict[str, Any]:
    """Recompute focal referents/negatives and inventory constraints.

    NLP fidelity, authority to select, API visibility, ordinary realism, and
    nonfocal card semantics require independent review. They are not inferred
    from the author's labels or this function's absence of errors.
    """
    errors: list[str] = []
    result: dict[str, Any] = {"errors": errors, "computed_matches": [], "computed_focal_negatives": [], "candidate_population": []}
    if not isinstance(case, dict):
        errors.append("case must be an object")
        return result
    for field in ("case_id", "prompt", "acting_user_id"):
        if not isinstance(case.get(field), str) or not case[field].strip():
            errors.append(f"{field} must be nonempty text")
    seed = case.get("seed")
    seed_errors = validate_seed(seed)
    errors.extend(seed_errors)
    if not isinstance(seed, dict):
        return result
    # API compatibility, deliberately separate from ORM/schema validity:
    # operations.list_channel_history orders actual IDs with cast(message_id, Float).
    messages = seed.get("messages", [])
    if isinstance(messages, list):
        for index, message in enumerate(messages):
            if not isinstance(message, dict):
                continue
            message_id = message.get("message_id")
            try:
                compatible = isinstance(message_id, str) and math.isfinite(float(message_id))
            except (ValueError, TypeError, OverflowError):
                compatible = False
            if not compatible:
                errors.append(f"API compatibility: seed.messages[{index}].message_id={message_id!r} must be a timestamp-like numeric string with finite float conversion; Slack history parses the actual message_id, not the separate ts field")
    users = seed.get("users", [])
    if not isinstance(users, list) or not any(isinstance(u, dict) and u.get("user_id") == case.get("acting_user_id") for u in users):
        errors.append("acting_user_id does not identify a seeded user")
    _validate_inventory(case, errors)
    private = case.get("private")
    if not isinstance(private, dict):
        errors.append("private must be an object")
        return result
    mode = private.get("mode")
    if mode not in {"single", "multiple", "absent", "underspecified"}:
        errors.append("private.mode must be single, multiple, absent, or underspecified")
    focal_id = private.get("focal_obligation")
    cards = case.get("cards", [])
    focal_card = None
    if type(focal_id) is not int or not isinstance(cards, list) or not 1 <= focal_id <= len(cards) or not isinstance(cards[focal_id - 1], dict):
        errors.append("private.focal_obligation must name a 1-based card index")
    else:
        focal_card = cards[focal_id - 1]
        expected_resolution = "resolved" if mode in {"single", "multiple"} else mode
        if focal_card.get("Resolution") != expected_resolution:
            errors.append("focal card Resolution disagrees with private.mode")
    if seed_errors:
        return result  # Invalid relation populations cannot establish selector results.
    try:
        computed = evaluate_selector(seed, private.get("selector"))
    except (SelectorError, KeyError, TypeError, ValueError) as exc:
        errors.append(f"private.selector: {exc}")
        return result
    table = private["selector"]["root_table"]
    result.update(computed_matches=computed["matches"], computed_focal_negatives=computed["focal_negatives"], candidate_population=computed["population"])
    match_keys = {handle_key(table, value) for value in computed["matches"]}
    population_keys = {handle_key(table, value) for value in computed["population"]}
    negative_keys = {handle_key(table, value) for value in computed["focal_negatives"]}
    expected = _handle_set(table, private.get("expected_matches"), "private.expected_matches", errors)
    if expected is not None and expected != match_keys:
        errors.append(f"private.expected_matches differs from recomputed matches: {computed['matches']!r}")
    near_misses = _handle_set(table, private.get("near_misses", []), "private.near_misses", errors)
    if private.get("workflow_version") == 2:
        # Path-derived negatives may challenge any requested condition, including
        # a scope or independent condition. Keep legacy focal-only checks intact.
        all_root_keys = {handle_key(table, canonical_handle(table, row)) for row in seed[table]}
        if near_misses is not None and (not near_misses <= all_root_keys or near_misses & match_keys):
            errors.append("private.near_misses must be existing root records outside the complete matching set")
    elif near_misses is not None and not near_misses <= negative_keys:
        errors.append("private.near_misses includes a handle outside scoped focal negatives (must fail focal and pass every auxiliary)")
    require_near_miss = private.get("require_near_miss", True)
    if type(require_near_miss) is not bool:
        errors.append("private.require_near_miss must be a boolean")
    if require_near_miss and not near_misses:
        errors.append("this construction requires at least one explicitly identified, recomputed focal negative")
    if mode == "single":
        if private.get("selection", "one") not in {"one", "choose_one"}:
            errors.append("single private.selection must be one or choose_one")
        if not match_keys or (private.get("selection", "one") == "one" and len(match_keys) != 1):
            errors.append("single mode requires exactly one match unless private.selection is choose_one; choose_one requires at least one eligible match")
    elif mode == "multiple" and not match_keys:
        errors.append("multiple mode requires a nonempty determined collection; collection intent does not require two seed matches")
    elif mode == "absent" and match_keys:
        errors.append("absent mode requires zero recomputed matches")
    if focal_card and mode in {"single", "multiple", "absent"}:
        card_keys = _handle_set(table, focal_card.get("Referent set"), "focal card Referent set", errors)
        if card_keys is not None and card_keys != match_keys:
            errors.append("focal card Referent set differs from recomputed matches")
    if mode == "underspecified":
        sets = _candidate_sets(table, private.get("candidate_sets"), "private.candidate_sets", errors)
        if sets is not None:
            union = set().union(*sets)
            if union != match_keys:
                errors.append("candidate_sets union differs from the recomputed eligible unresolved population")
            if not union <= population_keys:
                errors.append("candidate_sets contains out-of-scope handles")
            if focal_card and isinstance(focal_card.get("Referent set"), dict):
                card_sets = _candidate_sets(table, focal_card["Referent set"].get("candidate_sets"), "focal card candidate_sets", errors)
                if card_sets is not None and {frozenset(s) for s in card_sets} != {frozenset(s) for s in sets}:
                    errors.append("focal card candidate_sets differs from private.candidate_sets")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", type=Path)
    args = parser.parse_args()
    result = validate_case(json.loads(args.case.read_text()))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(bool(result["errors"]))


if __name__ == "__main__":
    main()
