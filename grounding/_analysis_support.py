"""Shared structural checks and rendering for curated grounding annotations.

This is not a proof checker or a semantic annotation algorithm.
"""
import argparse
import csv
import hashlib
import io
import json
import os
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
COMMON = {"Test ID", "Task type", "Grounding obligations", "Grounding obligation name", "Grounding obligation description", "Resolution", "Shared scope", "Referent set", "Alternative sufficient identifying sets"}
EXTRA = {"read-only": {"Answer-computation attributes"}, "state-changing": {"Change-computation attributes", "Written attributes"}}
RESOLUTIONS = ("resolved", "absent", "underspecified")
COVERAGE = ("yes", "partial", "no")

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


def make_outputs(analysis, entries, seed, config, here=None):
    entry_link = os.path.relpath(ROOT / config["entry"], here) if here else "../../datasets/agent-diff-bench/all_numbered.jsonl"
    per_test = [test_metrics(t) for t in analysis]
    sum_keys = ["obligations", *RESOLUTIONS, "fully_covered", "partially_covered", "unchecked", "not_fully_covered"]
    aggregate = {k: sum(t[k] for t in per_test) for k in sum_keys}
    aggregate.update(tests=len(per_test), tests_with_zero_obligations=sum(t["obligations"] == 0 for t in per_test))
    aggregate["full_coverage_fraction"] = aggregate["fully_covered"] / aggregate["obligations"] if aggregate["obligations"] else None
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
    report = [f"# {config['title']} grounding obligations", "", "See [method and source policy](README.md). These are benchmark annotations, not measurements of agent behavior. Cards use the locked schema in [cards.md](cards.md).", "",
        f"{aggregate['tests']} tests; {aggregate['obligations']} task-expressed obligations: {aggregate['resolved']} resolved, {aggregate['absent']} absent, {aggregate['underspecified']} underspecified. Assertions fully cover {aggregate['fully_covered']}, partially cover {aggregate['partially_covered']}, and leave {aggregate['unchecked']} unchecked.", "",
        "Coverage concerns the grounded contribution in the final state or requested output; it never requires a trajectory or source provenance. Full coverage does not certify whole-task correctness. See [the focused coverage audit](coverage_audit.md). The denominator includes unresolved and absent obligations. Zero-obligation tasks have no coverage ratio.", "",
        "| # | Test | Obligations | Resolved | Absent | Underspecified | Full | Partial | Unchecked |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for m in per_test:
        report.append(f"| {m['number']} | [{m['test_id']}](#{m['test_id']}) | " + " | ".join(str(m[k]) for k in ["obligations", "resolved", "absent", "underspecified", "fully_covered", "partially_covered", "unchecked"]) + " |")
    card_md = [f"# {config['title']} obligation cards", "", "Only agreed card fields appear inside each JSON block. Test/obligation headings are document navigation, not card fields. `Grounding obligations` is the total for the parent test, repeated on each of its cards; count cards once. See [tables and evidence](report.md).", ""]
    for item in analysis:
        tid = item["test_id"]
        entry = entries[tid]
        report += ["", f'<a id="{tid}"></a>', f"## #{item['number']} — {tid}", "", entry["question"], "",
            f"[Test entry]({entry_link}#L{item['number']}) · [Cards](cards.md#{tid})", "",
            "| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |",
            "|---|---|---|---|---|"]
        card_md += [f'<a id="{tid}"></a>', f"## #{item['number']} — {tid}", ""]
        if not item["obligations"]:
            report.append("| No existing-referent obligation | — | — | N/A | Only new outputs or supplied context; see notes |")
            card_md += ["No grounding-obligation cards: see the test notes for new outputs and supplied context.", ""]
        for i, row in enumerate(item["obligations"], 1):
            card = row["card"]
            indices = ", ".join(f"A{a}" for a in row["assertion_indices"]) or "None"
            report.append(f"| {i}. {safe(card['Grounding obligation name'])} | {card['Resolution']} | {refs_text(card['Referent set'])} | {row['assertion_coverage']} | {indices}: {safe(row['coverage_explanation'])} |")
            card_md += [f"### Obligation {i}", "", "```json", json.dumps(card, indent=2, ensure_ascii=False), "```", ""]
        report += ["", "Boundary and selection notes:", ""]
        for i, row in enumerate(item["obligations"], 1):
            report.append(f"- **{i}.** {row['semantic_justification']}" + (f" Selection: {row['selection_rule']}" if row['selection_rule'] and row['selection_rule'] != row['semantic_justification'] else ""))
        for note in item["notes"]:
            report.append(f"- {note}")
        report += ["", "<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>", "", "```json",
            json.dumps(json.loads(entry["answer"])["assertions"], ensure_ascii=False, indent=2), "```", "", "</details>"]
    outputs["report.md"] = "\n".join(report) + "\n"
    outputs["cards.md"] = "\n".join(card_md) + "\n"
    sources = {}
    for path in [ROOT / p for p in config["local_sources"]]:
        sources[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    outputs["sources.json"] = json.dumps({"local_source_sha256": sources,
        "protocol_version": "v1", "api_documentation": config["api_documentation"],
        "documentation_consulted_on": "2026-09-08",
        "excluded": ["service implementation", "evaluator implementation", "live database", "agent runs/audits", "external conceptual ER model"]}, indent=2) + "\n"
    return outputs


def run(here):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    config = json.loads((here / "config.json").read_text())
    entries = {t["test_id"]: t for t in map(json.loads, (ROOT / config["entry"]).read_text().splitlines()) if t["service"] == config["service"]}
    seed = json.loads((ROOT / config["seed"]).read_text())
    analysis = json.loads((here / "analysis.json").read_text())
    assert [t["test_id"] for t in analysis] == list(entries), "Incomplete/out-of-order annotation"
    fields = {f"{entity}.{key}" for entity, rows in seed.items() for r in rows for key in r} | set(config["additional_attributes"])
    for t in analysis:
        assert t["number"] == entries[t["test_id"]]["#"]
        names = set()
        for o in t["obligations"]:
            c = o["card"]
            assert set(c) == COMMON | EXTRA[c["Task type"]]
            assert c["Test ID"] == t["test_id"]
            assert c["Grounding obligations"] == len(t["obligations"])
            assert c["Grounding obligation name"] not in names
            names.add(c["Grounding obligation name"])
            assert c["Resolution"] in RESOLUTIONS and o["assertion_coverage"] in COVERAGE
            assert o["semantic_justification"] and o["coverage_explanation"]
            assertions = json.loads(entries[t["test_id"]]["answer"])["assertions"]
            assert all(1 <= i <= len(assertions) for i in o["assertion_indices"])
            assert o["assertion_coverage"] == "no" or o["assertion_indices"]
            refs = c["Referent set"]
            if c["Resolution"] == "underspecified":
                assert refs is None and c["Alternative sufficient identifying sets"] is None
            else:
                assert isinstance(refs, list)
                assert bool(refs) == (c["Resolution"] == "resolved")
                assert len({json.dumps(r, sort_keys=True) for r in refs}) == len(refs)
                entity = o["referent_entity"]
                population = seed.get(entity, config.get("documented_populations", {}).get(entity))
                assert population is not None, entity
                for ref in refs:
                    if isinstance(ref, dict):
                        assert any(all(r.get(k) == v for k,v in ref.items()) for r in population), (t["test_id"], ref)
                    else:
                        assert any(r.get("id") == ref for r in population), (t["test_id"], ref)
            for key in ["Alternative sufficient identifying sets", "Answer-computation attributes", "Change-computation attributes"]:
                if key in c and c[key] is not None:
                    assert isinstance(c[key], list) and c[key]
                    for alt in c[key]:
                        assert isinstance(alt, list) and len(alt) == len(set(alt))
                        assert set(alt) <= fields, (t["test_id"], set(alt) - fields)
            assert set(c.get("Written attributes", [])) <= fields, t["test_id"]
    outputs = make_outputs(analysis, entries, seed, config, here)
    audit = [f"# {config['title']} outcome-coverage review", "", "All coverage annotations are judged against final state/output, not retrieval traces. This table collects every partial label and its concrete missing constraint. Predicate examples are not full benchmark executions. See report.md for all assertions and semantic notes.", "", "| Test / obligation | Partial-coverage reason |", "|---|---|"]
    for t in analysis:
        for i,o in enumerate(t["obligations"],1):
            if o["assertion_coverage"] == "partial":
                audit.append(f"| [{t['test_id']} / {i}](report.md#{t['test_id']}) | {safe(o['coverage_explanation'])} |")
    outputs["coverage_audit.md"] = "\n".join(audit) + "\n"
    for name, content in outputs.items():
        p = here / name
        if args.check:
            assert p.exists() and p.read_text() == content, f"Stale output: {p}"
        else:
            p.write_text(content)
    print(f"Checked {len(analysis)} {config['service']} tests, {sum(len(t['obligations']) for t in analysis)} cards; structural consistency only.")
