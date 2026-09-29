"""Validate blind reference records and their source evidence without reading scores."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GROUNDING = HERE.parents[1]
OUTCOMES = {"correct", "correct_absent", "incorrect", "presented", "false_absence",
            "incomplete", "artifact", "not_established"}


def read_lines(name):
    path = HERE / name
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []


def main():
    manifest = json.loads((HERE / "manifest.json").read_text())
    sample = {r["blind_id"]: r for r in manifest["sample"]}
    labels = read_lines("labels.jsonl")
    assert len(labels) == len(sample) == 200
    assert len({r["blind_id"] for r in labels}) == 200
    assert {r["blind_id"] for r in labels} == set(sample)
    checked, pointers, errors = set(), 0, []
    for row in labels:
        bid = row["blind_id"]
        source = sample[bid]
        assert row["outcome"] in OUTCOMES, bid
        assert row["mechanism"] in {"none", "skipped-check", "saw-mismatch-accepted", "misread"}, bid
        assert all(isinstance(row[k], list) for k in ("acted_on", "exposed", "evidence")), bid
        assert row["note"] and row["confidence"] and row["evidence"], bid
        if row["outcome"] not in {"incorrect", "presented"}:
            assert not row["exposed"], bid
        for name, expected in source["source_hashes"].items():
            if expected and name not in checked:
                actual = hashlib.sha256((GROUNDING / name).read_bytes()).hexdigest()
                assert actual == expected, (bid, name, "source changed")
                checked.add(name)
        for reference in row["evidence"]:
            name, _, pointer = reference.partition("#")
            path = GROUNDING / source["solver_record"] if name == "solver_record" else GROUNDING / source["attempt"] / name
            try:
                assert path.is_file(), f"missing {path}"
                if pointer:
                    data = json.loads(path.read_text())
                    for part in pointer.removeprefix("/").split("/"):
                        part = part.replace("~1", "/").replace("~0", "~")
                        data = data[int(part)] if isinstance(data, list) else data[part]
                pointers += 1
            except (AssertionError, KeyError, IndexError, ValueError) as exc:
                errors.append({"blind_id": bid, "evidence": reference, "error": str(exc)})
    result = {"labels": len(labels), "unique_cases": len({r["key"].split("/", 2)[-1] for r in sample.values()}),
              "source_files_verified": len(checked), "evidence_references_verified": pointers, "errors": errors,
              "scores_read": False}
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
