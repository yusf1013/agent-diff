"""Find attempts whose model stream was cut by the provider (HTTP 200, no finish reason, no terminator), and
attempts whose model hit the output limit (finish reason "length", e.g. reasoning that never ends).

    python3 -m grounding.runs.openclaw_transfer_01.streams runs/t1 [runs/t2 ...] [--json cut.json]

A cut stream in the *last* request of a turn leaves OpenClaw with a truncated or empty reply ("Agent couldn't
generate a response"); such turns are infrastructure failures, not agent behaviour. Earlier cut requests were
retried by OpenClaw itself and are only counted.
"""
from __future__ import annotations

import argparse
import json
import tarfile
from pathlib import Path

from grounding.runs.openclaw_transfer_01.analyze import latest_attempts


def cut_requests(attempt: Path) -> tuple[list[str], int, list[str]]:
    bundle = attempt / "solver" / "requests.tar.xz"
    if not bundle.exists():
        return [], 0, []
    metas = {}
    with tarfile.open(bundle) as tar:
        for member in tar.getmembers():
            if member.name.endswith(".meta.json"):
                metas[Path(member.name).name.split(".")[0]] = json.load(tar.extractfile(member))
    cut = [n for n, m in sorted(metas.items())
           if m.get("path", "").endswith("/chat/completions") and not m.get("done_seen") and not m.get("finish_reason")]
    length = [n for n, m in sorted(metas.items()) if m.get("finish_reason") == "length"]
    return cut, len(metas), length


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    found, length_stops = {}, {}
    for run in args.runs:
        for attempt in latest_attempts(run):
            cut, total, length = cut_requests(attempt)
            if length:
                length_stops[f"{run.name}/{attempt.parent.name}"] = length
            if cut:
                last = cut[-1] == f"{total:04d}"
                found[f"{run.name}/{attempt.parent.name}"] = {"attempt": str(attempt), "cut": cut, "requests": total,
                                                              "last_request_cut": last}
    for key, info in found.items():
        print(f"{key}: cut {info['cut']} of {info['requests']} requests; last request cut: {info['last_request_cut']}")
    print(f"{sum(1 for i in found.values() if i['last_request_cut'])} attempts end on a cut stream; "
          f"{len(found)} attempts have any cut stream")
    for key, requests in length_stops.items():
        print(f"{key}: output limit reached in request(s) {requests}")
    print(f"{len(length_stops)} attempts hit the output limit")
    if args.json:
        args.json.write_text(json.dumps(found, indent=1))


if __name__ == "__main__":
    main()
