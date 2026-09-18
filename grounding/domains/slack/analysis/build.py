"""Validate annotation structure and render reports; this is not a proof checker.

Only the allowlisted benchmark entry, seed, API definitions, and curated annotation
are read. No service/evaluator implementation, database, or agent run is inspected.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
from grounding.paths import REPO_ROOT as ROOT
ENTRY = ROOT / "datasets/agent-diff-bench/all_numbered.jsonl"
SEED = ROOT / "examples/slack/seeds/slack_bench_v2.json"
API = ROOT / "examples/slack/testsuites/slack_docs/slack_api_full_docs.json"
COMMON = {
    "Test ID", "Task type", "Grounding obligations", "Grounding obligation name",
    "Grounding obligation description", "Resolution", "Shared scope",
    "Referent set", "Alternative sufficient identifying sets",
    "Identifying paths",
}
EXTRA = {
    "read-only": {"Answer-computation attributes"},
    "state-changing": {"Change-computation attributes", "Written attributes"},
}
COVERAGE = ("yes", "partial", "no")
RESOLUTIONS = ("resolved", "absent", "underspecified")
KEYS = {"channels": "channel_id", "users": "user_id", "messages": "message_id"}
PATH_RELATIONSHIPS = {
    "channels.team_id": {"channels", "teams"},
    "user_teams.user_id": {"user_teams", "users"},
    "user_teams.team_id": {"user_teams", "teams"},
    "channel_members.channel_id": {"channel_members", "channels"},
    "channel_members.user_id": {"channel_members", "users"},
    "messages.channel_id": {"messages", "channels"},
    "messages.user_id": {"messages", "users"},
    "messages.parent_id": {"messages"},
    "message_reactions.message_id": {"message_reactions", "messages"},
    "message_reactions.user_id": {"message_reactions", "users"},
}


def validate(analysis, entries, seed):
    """Structural/evidence-reference checks, never semantic certification."""
    assert len(analysis) == len(entries) == 59
    assert [t["test_id"] for t in analysis] == list(entries)
    seed_ids = {entity: {r[key] for r in seed[entity]} for entity, key in KEYS.items()}
    seed_fields = {f"{entity}.{key}" for entity, rows in seed.items() for row in rows for key in row}
    # blocks is documented in the API definition and named in the test assertions,
    # even though no initial seeded message contains it.
    fields = seed_fields | {"messages.blocks"}
    count = 0
    for item in analysis:
        entry = entries[item["test_id"]]
        assertions = json.loads(entry["answer"])["assertions"]
        assert item["number"] == entry["#"]
        spec = item["task_spec"]
        assert isinstance(spec, list) and spec, item["test_id"]
        linked = set()
        for number, line in enumerate(spec, 1):
            assert set(line) == {"line", "text", "obligations"}, item["test_id"]
            assert type(line["line"]) is int and line["line"] == number
            assert isinstance(line["text"], str) and line["text"].strip()
            assert not any(c in line["text"] for c in "\n\r\t"), item["test_id"]
            links = line["obligations"]
            assert isinstance(links, list)
            assert all(type(i) is int and 1 <= i <= len(item["obligations"]) for i in links), item["test_id"]
            assert links == sorted(set(links)), item["test_id"]
            linked.update(links)
        assert linked == set(range(1, len(item["obligations"]) + 1)), (item["test_id"], "Unlinked obligation")
        names = set()
        for row in item["obligations"]:
            count += 1
            card = row["card"]
            assert card["Task type"] in EXTRA
            assert set(card) == COMMON | EXTRA[card["Task type"]], (entry["test_id"], set(card))
            assert card["Test ID"] == entry["test_id"]
            assert card["Grounding obligations"] == len(item["obligations"])
            assert card["Grounding obligation name"] not in names
            names.add(card["Grounding obligation name"])
            assert card["Resolution"] in RESOLUTIONS
            paths = card["Identifying paths"]
            assert isinstance(paths, list) and paths, entry["test_id"]
            assert len({json.dumps(p, sort_keys=True) for p in paths}) == len(paths)
            for path in paths:
                assert set(path) == {"entities", "relationships"}
                entities, relationships = path["entities"], path["relationships"]
                assert isinstance(entities, list) and entities
                assert entities[0] == row["referent_entity"]
                assert set(entities) <= set(seed)
                assert isinstance(relationships, list) and len(relationships) == len(entities) - 1
                for left, right, relationship in zip(entities, entities[1:], relationships):
                    assert relationship in fields
                    assert PATH_RELATIONSHIPS.get(relationship) == {left, right}, (entry["test_id"], path)
            assert row["assertion_coverage"] in COVERAGE
            assert row["coverage_explanation"] and row["semantic_justification"]
            assert all(1 <= i <= len(assertions) for i in row["assertion_indices"])
            if row["assertion_coverage"] != "no":
                assert row["assertion_indices"], entry["test_id"]
            refs = card["Referent set"]
            resolution = card["Resolution"]
            protocol_version = row.get("protocol_version", item.get("protocol_version", "v1"))
            assert protocol_version in {"v1", "v1.0.1"}
            if resolution == "underspecified":
                assert card["Alternative sufficient identifying sets"] is None
                if protocol_version == "v1":
                    # Cases outside the explicitly migrated scope retain v1.
                    assert refs is None
                else:
                    assert isinstance(refs, dict)
                    assert set(refs) == {"selection", "partial_constraints", "candidate_sets"}
                    entity = row["referent_entity"]
                    assert refs["selection"] in {f"one({entity})", f"set({entity})"}
                    assert isinstance(refs["partial_constraints"], list)
                    for condition in refs["partial_constraints"]:
                        assert isinstance(condition, str) and condition.strip()
                        attributes = set(re.findall(r"\b[a-z_]+\.[a-z_]+\b", condition))
                        assert attributes <= fields, (entry["test_id"], attributes - fields)
                    candidates = refs["candidate_sets"]
                    if candidates is not None:
                        assert isinstance(candidates, list) and len(candidates) >= 2
                        canonical = []
                        for candidate in candidates:
                            assert isinstance(candidate, list)
                            assert len(set(candidate)) == len(candidate)
                            assert set(candidate) <= seed_ids[entity]
                            if refs["selection"].startswith("one("):
                                assert len(candidate) <= 1
                            canonical.append(tuple(sorted(candidate)))
                        assert len(set(canonical)) == len(canonical)
            else:
                assert isinstance(refs, list)
                assert (len(refs) > 0) == (resolution == "resolved")
                assert len({json.dumps(r, sort_keys=True) for r in refs}) == len(refs)
                if row["referent_entity"] in KEYS:
                    assert set(refs) <= seed_ids[row["referent_entity"]], (entry["test_id"], refs)
                else:
                    assert row["referent_entity"] == "message_reactions"
                    assert all(r in seed["message_reactions"] for r in refs)
            for name in ["Alternative sufficient identifying sets", "Change-computation attributes", "Answer-computation attributes"]:
                if name not in card or card[name] is None:
                    continue
                assert isinstance(card[name], list) and card[name]
                for alternative in card[name]:
                    assert isinstance(alternative, list)
                    assert len(alternative) == len(set(alternative))
                    assert set(alternative) <= fields, (entry["test_id"], name, set(alternative) - fields)
            assert set(card.get("Written attributes", [])) <= fields
    by_id = {t["test_id"]: t for t in analysis}
    assert len(by_id["slack_57"]["obligations"]) == 1
    assert by_id["slack_57"]["obligations"][0]["card"]["Referent set"] == ["C01ABCD1234"]
    assert not by_id["slack_60"]["obligations"]
    agreed = by_id["slack_98"]["obligations"]
    assert len(agreed) == 8
    assert Counter(r["card"]["Resolution"] for r in agreed) == {"resolved": 4, "underspecified": 4}
    assert all(r["assertion_coverage"] == "no" for r in agreed)
    return count


def test_metrics(item):
    rows = item["obligations"]
    resolution = Counter(r["card"]["Resolution"] for r in rows)
    coverage = Counter(r["assertion_coverage"] for r in rows)
    total = len(rows)
    return {
        "number": item["number"], "test_id": item["test_id"],
        "obligations": total, **{k: resolution[k] for k in RESOLUTIONS},
        "fully_covered": coverage["yes"], "partially_covered": coverage["partial"],
        "unchecked": coverage["no"],
        "not_fully_covered": coverage["partial"] + coverage["no"],
        "full_coverage_fraction": coverage["yes"] / total if total else None,
    }


def safe(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def refs_text(refs):
    if refs is None:
        return "Undetermined"
    return "`" + safe(json.dumps(refs, ensure_ascii=False, separators=(",", ":"))) + "`"


def make_outputs(analysis, entries, seed):
    per_test = [test_metrics(t) for t in analysis]
    sum_keys = ["obligations", *RESOLUTIONS, "fully_covered", "partially_covered", "unchecked", "not_fully_covered"]
    aggregate = {k: sum(t[k] for t in per_test) for k in sum_keys}
    aggregate.update(tests=len(per_test), tests_with_zero_obligations=sum(t["obligations"] == 0 for t in per_test))
    aggregate["full_coverage_fraction"] = aggregate["fully_covered"] / aggregate["obligations"]
    aggregate["tests_with_obligations_but_no_coverage"] = sum(t["obligations"] > 0 and t["fully_covered"] + t["partially_covered"] == 0 for t in per_test)
    cross = {r: {c: sum(o["card"]["Resolution"] == r and o["assertion_coverage"] == c for t in analysis for o in t["obligations"]) for c in COVERAGE} for r in RESOLUTIONS}
    metric_data = {"aggregate": aggregate, "resolution_by_coverage": cross, "tests": per_test}
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=list(per_test[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(per_test)
    cards = [o["card"] for t in analysis for o in t["obligations"]]
    outputs = {
        "metrics.json": json.dumps(metric_data, indent=2) + "\n",
        "metrics.csv": stream.getvalue(),
        "cards.jsonl": "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cards),
    }
    report = ["# Slack grounding obligations", "", "See [method and source policy](README.md). These are benchmark annotations, not measurements of agent behavior. Cards use the locked schema in [cards.md](cards.md).", "",
        f"{aggregate['tests']} tests; {aggregate['obligations']} task-expressed obligations: {aggregate['resolved']} resolved, {aggregate['absent']} absent, {aggregate['underspecified']} underspecified. Assertions fully cover {aggregate['fully_covered']}, partially cover {aggregate['partially_covered']}, and leave {aggregate['unchecked']} unchecked.", "",
        "Coverage concerns the grounded contribution in the final state or requested output; it never requires a trajectory or source provenance. Full coverage does not certify whole-task correctness. See [the focused coverage audit](coverage_audit.md). The denominator includes unresolved and absent obligations. Zero-obligation tasks have no coverage ratio.", "",
        "| # | Test | Obligations | Resolved | Absent | Underspecified | Full | Partial | Unchecked |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for m in per_test:
        report.append(f"| {m['number']} | [{m['test_id']}](#{m['test_id']}) | " + " | ".join(str(m[k]) for k in ["obligations", "resolved", "absent", "underspecified", "fully_covered", "partially_covered", "unchecked"]) + " |")
    card_md = ["# Slack obligation cards", "", "Only agreed card fields appear inside each JSON block. Test/obligation headings are document navigation, not card fields. `Grounding obligations` is the total for the parent test, repeated on each of its cards; count cards once. See [tables and evidence](report.md) and [task specifications and action links](task_specs.md).", ""]
    task_md = ["# Slack downstream task specifications", "",
        "Pre-execution rewrites of all 59 Slack prompts, guided by their existing obligation cards. Editable source: [analysis.json](analysis.json). See [rewriting and linking rules](README.md#downstream-task-specifications).", "",
        "Line numbers identify specification lines, including conditions; they are not action counts. Indentation, conditions, and explicit sequencing words express workflow. Other line order does not impose execution order. Links describe each line's direct use of existing obligations, including source-dependent content; they do not inherit enclosing conditions or other workflow dependencies. Empty links do not mean an action is optional or already complete.", "",
        "Both conditional branches remain in the specification. Cards and links retain the seed-specific obligation inventory. Underspecified and absent references remain as requested; no arbitrary target or recovery behavior is supplied.", ""]
    for item in analysis:
        tid = item["test_id"]
        entry = entries[tid]
        report += ["", f'<a id="{tid}"></a>', f"## #{item['number']} — {tid}", "", entry["question"], "",
            f"[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L{item['number']}) · [Cards](cards.md#{tid}) · [Task specification](task_specs.md#{tid})", "",
            "| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |",
            "|---|---|---|---|---|"]
        card_md += [f'<a id="{tid}"></a>', f"## #{item['number']} — {tid}", "", f"[Task specification and links](task_specs.md#{tid})", ""]
        task_md += [f'<a id="{tid}"></a>', f"## #{item['number']} — {tid}", "",
            f"[Original prompt and evidence](report.md#{tid}) · [Obligation cards](cards.md#{tid})", "", "```text"]
        task_md += [f"{line['line']:>2}: {line['text']}" for line in item["task_spec"]]
        task_md += ["```", "", "| Line | Direct obligation links |", "|---|---|"]
        for line in item["task_spec"]:
            links = ", ".join(f"[O{i}](cards.md#{tid}-o{i})" for i in line["obligations"]) or "—"
            task_md.append(f"| L{line['line']} | {links} |")
        task_md.append("")
        if "protocol_version" in item:
            card_md += [f"Card protocol: {item['protocol_version']}.", ""]
        if not item["obligations"]:
            report.append("| No existing-referent obligation | — | — | N/A | Creation of a new named entity only |")
            card_md += ["No grounding-obligation cards: this task creates a new channel without describing an existing referent.", ""]
        for i, row in enumerate(item["obligations"], 1):
            card = row["card"]
            indices = ", ".join(f"A{a}" for a in row["assertion_indices"]) or "None"
            report.append(f"| {i}. {safe(card['Grounding obligation name'])} | {card['Resolution']} | {refs_text(card['Referent set'])} | {row['assertion_coverage']} | {indices}: {safe(row['coverage_explanation'])} |")
            card_md += [f'<a id="{tid}-o{i}"></a>', f"### Obligation {i}", ""]
            if "protocol_version" in row:
                card_md += [f"Card protocol: {row['protocol_version']} (focused obligation review).", ""]
            card_md += ["```json", json.dumps(card, indent=2, ensure_ascii=False), "```", ""]
        report += ["", "Boundary and selection notes:", ""]
        if "protocol_version" in item:
            report.append(f"- Card protocol: {item['protocol_version']}.")
        for i, row in enumerate(item["obligations"], 1):
            report.append(f"- **{i}.** {row['semantic_justification']}" + (f" Selection: {row['selection_rule']}" if row['selection_rule'] and row['selection_rule'] != row['semantic_justification'] else ""))
        for note in item["notes"]:
            report.append(f"- {note}")
        report += ["", "<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>", "", "```json",
            json.dumps(json.loads(entry["answer"])["assertions"], ensure_ascii=False, indent=2), "```", "", "</details>"]
    outputs["report.md"] = "\n".join(report) + "\n"
    outputs["cards.md"] = "\n".join(card_md) + "\n"
    outputs["task_specs.md"] = "\n".join(task_md) + "\n"
    sources = {}
    for path in [ENTRY, SEED, API]:
        sources[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    outputs["sources.json"] = json.dumps({"local_source_sha256": sources,
        "api_documentation": [
            "https://docs.slack.dev/reference/methods/conversations.list/",
            "https://docs.slack.dev/reference/objects/user-object/",
            "https://docs.slack.dev/reference/methods/conversations.replies/",
            "https://docs.slack.dev/reference/methods/search.messages/",
            "https://docs.slack.dev/reference/methods/conversations.members/",
            "https://docs.slack.dev/reference/methods/reactions.get/",
            "https://docs.slack.dev/reference/methods/conversations.history/",
            "https://docs.slack.dev/reference/methods/chat.postMessage/",
        ], "documentation_consulted_on": "2026-09-08",
        "excluded": ["service implementation", "evaluator implementation", "live database", "agent runs/audits", "external conceptual ER model"]}, indent=2) + "\n"
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check structure and generated-file freshness without writing")
    args = parser.parse_args()
    entries = {r["test_id"]: r for r in map(json.loads, ENTRY.read_text().splitlines()) if r["service"] == "slack"}
    analysis = json.loads((HERE / "analysis.json").read_text())
    seed = json.loads(SEED.read_text())
    count = validate(analysis, entries, seed)
    for name, text in make_outputs(analysis, entries, seed).items():
        path = HERE / name
        if args.check:
            assert path.exists() and path.read_text() == text, f"Stale generated file: {name}"
        else:
            path.write_text(text)
    print(f"Checked {len(analysis)} tests and {count} cards: locked fields, referent existence, assertion indices, counts, task-spec line structure and obligation links, and generated artifacts. No semantic/procedure proof is claimed.")


if __name__ == "__main__":
    main()
