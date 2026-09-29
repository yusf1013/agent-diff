"""Resolve recorded adjudications and lock references before reading saved scores."""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from validate import main as validate_sources, read_lines

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_lock():
    lock = json.loads((HERE / "labels.sha256").read_text())
    for name, expected in lock["files"].items():
        assert sha(HERE / name) == expected, f"Locked reference changed: {name}"
    return lock


def main():
    if (HERE / "labels.sha256").exists():
        verify_lock()
        print("Existing reference lock verified; no files changed.")
        return
    pending = json.loads((HERE / "pending_adjudications.json").read_text())
    assert not pending["pending"], f"Unresolved PI questions: {pending['pending']}"
    validate_sources()
    labels = {r["blind_id"]: r for r in read_lines("labels.jsonl")}
    for r in labels.values():
        r["initial_outcome"] = r["outcome"]
        r["initial_note"] = r["note"]
        r["provenance"] = "Codex-authored independent AI reference label"
    # Optional pre-lock quality corrections are separate from the original records.
    for revision in read_lines("review_revisions.jsonl"):
        r = labels[revision["blind_id"]]
        r.update(revision["changes"])
        r.setdefault("prelock_revisions", []).append(revision)
    for a in read_lines("human_adjudications.jsonl"):
        r = labels[a["blind_id"]]
        r["outcome"] = a["final_outcome"]
        r["note"] = a["reason"]
        r["human_adjudication"] = a
        r["provenance"] = "Codex-authored independent AI reference with PI semantic adjudication"
        for key in ("acted_on", "exposed", "mechanism", "artifact_reason"):
            if key in a:
                r[key] = a[key]
        r["review_status"] = "uncertain_retained" if r["outcome"] is None else "adjudicated"
        if r["outcome"] is None:
            r["confidence"] = "uncertain"
            r["exposed"] = []
            r["mechanism"] = "none"
        else:
            r["confidence"] = a.get("confidence", "PI adjudication")
    assert len(labels) == 200
    for r in labels.values():
        assert r["review_status"] != "pending_user", r["blind_id"]
        assert r["confidence"] != "pending_user", r["blind_id"]
        if r["outcome"] not in {"incorrect", "presented"}:
            assert not r["exposed"], r["blind_id"]
            assert r["mechanism"] == "none", r["blind_id"]
        if r["outcome"] not in {"artifact", None}:
            assert not r["artifact_reason"], r["blind_id"]
    (HERE / "effective_labels.json").write_text(json.dumps(list(sorted(labels.values(), key=lambda r: r["blind_id"])), indent=2, ensure_ascii=False) + "\n")
    names = ["README.md", "prelock_checks.md", "manifest.json", "draw.sha256", "labels.jsonl", "human_adjudications.jsonl",
             "pending_adjudications.json", "effective_labels.json", "prepare.py", "view.py", "record.py",
             "validate.py", "finalize.py", "metrics.py"]
    if (HERE / "review_revisions.jsonl").exists():
        names.append("review_revisions.jsonl")
    lock = {"locked_utc": datetime.now(timezone.utc).isoformat(),
            "phase": "before unblinding any selected saved verdict or mechanical score",
            "labels": 200, "outcomes": dict(Counter(r["outcome"] or "uncertain" for r in labels.values())),
            "files": {name: sha(HERE / name) for name in names}}
    (HERE / "labels.sha256").write_text(json.dumps(lock, indent=2) + "\n")
    print(json.dumps({k:v for k,v in lock.items() if k != "files"}, indent=2))


if __name__ == "__main__":
    main()
