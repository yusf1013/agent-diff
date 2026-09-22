"""Verify audit provenance and replay saved native assertions, without API calls.

This checks accounting and evidence locations, not the manual semantic judgments.
Run with the configured project Python environment (requires jsonschema).
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from src.platform.evaluationEngine.assertion import AssertionEngine
from src.platform.evaluationEngine.compiler import DSLCompiler


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pointer(document, location):
    for part in location.split("/")[1:]:
        key = part.replace("~1", "/").replace("~0", "~")
        document = document[int(key)] if isinstance(document, list) else document[key]
    return document


def verify():
    audit = read(HERE / "audit.json")
    manual = read(HERE / "manual_review.json")
    for path, expected in audit["source_sha256"].items():
        assert digest(ROOT / path) == expected, f"Source changed: {path}"
    manifest = read(ROOT / "experiments/slack_campaign/campaign_02/baseline/manifest.json")
    failed = {x["test_id"] for x in manifest if x["native_result"]["passed"] is False}
    cases = audit["cases"]
    assert len(cases) == len(failed) and {c["test_id"] for c in cases} == failed
    decisions = {c["test_id"]: c for c in manual["cases"]}
    counts = Counter()
    evidence_count = 0
    for case in cases:
        original = decisions[case["test_id"]]
        assert case["other_findings"] == original["other_findings"]
        assert len(case["assertions"]) == len(original["assertions"])
        for row, authored in zip(case["assertions"], original["assertions"]):
            assert all(row[k] == v for k, v in authored.items())
        sources = {name: read(ROOT / path) for name, path in case["sources"].items()}
        assert case["run_id"] == sources["run"]["run_id"] == sources["ground_truth"]["run_id"]
        assert case["prompt"] == sources["task"]["prompt"] == sources["run"]["question"]
        assert sources["diff"] == sources["run"]["evaluation"]["diff"]
        spec = DSLCompiler().compile(case["expected_output"])
        replay = AssertionEngine(spec).evaluate(sources["diff"])
        assert replay["score"] == case["native_score"]
        recorded = [f for a in case["assertions"] for f in a["recorded_failures"]]
        assert replay["failures"] == recorded == sources["run"]["evaluation"]["failures"]
        numbers = sorted({int(re.match(r"assertion#(\d+)", f)[1]) for f in recorded})
        assert numbers == [a["number"] for a in case["assertions"]]
        for row in case["assertions"]:
            assert row["native_assertion"] == case["expected_output"]["assertions"][row["number"] - 1]
            counts[row["classification"]] += 1
            for evidence in row["evidence"]:
                pointer(sources[evidence["source"]], evidence["location"])
                evidence_count += 1
    assert dict(counts) == audit["summary"]["assertion_classifications"]
    assert sum(counts.values()) == audit["summary"]["failed_assertions"]
    assert len(cases) == audit["summary"]["runs"]
    provenance = read(HERE / "g4_prompt_provenance.json")
    prompt_path = HERE / "g4_direct_judge_prompt.md"
    assert digest(prompt_path) == provenance["prompt_sha256"]
    for entry in provenance["saved_requests"]:
        path = ROOT / entry["path"]
        assert digest(path) == entry["sha256"], f"Judge request changed: {path}"
        assert read(path)["system"] == prompt_path.read_text()
    packet = read(ROOT / provenance["example_user_packet"])
    request = read(ROOT / provenance["example_request"])
    assert json.loads(request["messages"][0]["content"][0]["text"]) == packet
    print(json.dumps({"status": "verified", "runs": len(cases),
                      "failed_assertions": sum(counts.values()),
                      "evidence_pointers": evidence_count,
                      "source_hashes": len(audit["source_sha256"]),
                      "saved_judge_requests": len(provenance["saved_requests"]),
                      "limitation": "Mechanical verification does not approve semantic judgments."}, indent=2))


if __name__ == "__main__":
    verify()
