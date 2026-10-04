"""The sample for the models-and-harnesses study: 30 tests per form, drawn without looking at any result.

    python3 grounding/runs/models_sample_01/kit/draw.py [--per-form 30] [--seed 20261004]

Forms (the PI, 2026-10-01): packed probes, single-decoy probes (the separate tests beside a packed probe), absence
tests, underspecified tests, boundary tests; covers skipped. The frame is the designated tests of the denominator
(`denominator_01/numbers/retained.json`, kinds "denominator: ...") and the 90 valid boundary tests, all of them in
their date templates (`dates_02/suite`), which the runners fill in for the run day.

Rules: services in proportion to the form's tests (largest remainder); at most one test per fact within a form; the
boundary tests spread over their limit classes in proportion within each service; a seeded shuffle decides
everything else. No outcome of any agent is read. Writes ../sample.json and prints the per-form, per-service counts.
"""
from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
RUNS = HERE.parent
SUITE = RUNS / "dates_02" / "suite"
SERVICES = ("box", "calendar", "linear", "slack")
FORMS = {   # form -> (retained.json kind, the key in retained.json, template folder)
    "packed probe": ("denominator: packed probe", "tests", "cases"),
    "single-decoy probe": ("denominator: single-decoy probe (counted)", "tests", "cases"),
    "absence": ("denominator: absence test", "units", "units"),
    "underspecified": ("denominator: underspecified test", "units", "units"),
}


def largest_remainder(sizes: dict[str, int], n: int) -> dict[str, int]:
    total = sum(sizes.values())
    quotas = {k: n * v / total for k, v in sizes.items()}
    alloc = {k: int(q) for k, q in quotas.items()}
    for k in sorted(quotas, key=lambda k: (quotas[k] - alloc[k], sizes[k]), reverse=True)[: n - sum(alloc.values())]:
        alloc[k] += 1
    return alloc


def pick(cands: list[dict], n: int, rng: random.Random) -> list[dict]:
    """n tests in a seeded order, skipping a test whose fact is already taken."""
    order = sorted(cands, key=lambda c: c["test"])
    rng.shuffle(order)
    out, taken = [], set()
    for c in order:
        if len(out) == n:
            break
        if taken & set(c["facts"]):
            continue
        out.append(c)
        taken |= set(c["facts"])
    if len(out) < n:
        raise SystemExit(f"only {len(out)} of {n} with distinct facts")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-form", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20261004)
    a = ap.parse_args()
    retained = json.loads((RUNS / "denominator_01/numbers/retained.json").read_text())["qwen"]
    sample, frames = [], {}
    for form, (kind, key, folder) in FORMS.items():
        cands = [{"test": t, "form": form, "domain": v["domain"], "facts": sorted(v["facts"]),
                  "template": str((SUITE / folder / v["domain"] / f"{t}.json").relative_to(RUNS.parents[1]))}
                 for t, v in retained[key].items() if v["kind"] == kind]
        assert all((RUNS.parents[1] / c["template"]).exists() for c in cands), form
        frames[form] = Counter(c["domain"] for c in cands)
        alloc = largest_remainder(frames[form], a.per_form)
        for d in SERVICES:
            rng = random.Random(f"{a.seed}:{form}:{d}")
            sample += pick([c for c in cands if c["domain"] == d], alloc[d], rng)
    bcands = []
    for f in sorted((SUITE / "boundary").glob("*/*.json")):
        t = json.loads(f.read_text())
        bcands.append({"test": t["case_id"], "form": "boundary", "domain": t["domain"],
                       "facts": [t["boundary"]["element"]], "class": t["boundary"]["class"],
                       "template": str(f.relative_to(RUNS.parents[1]))})
    frames["boundary"] = Counter(c["domain"] for c in bcands)
    alloc = largest_remainder(frames["boundary"], a.per_form)
    for d in SERVICES:
        mine = [c for c in bcands if c["domain"] == d]
        by_class = largest_remainder(Counter(c["class"] for c in mine), alloc[d])
        for cls, n in sorted(by_class.items()):
            sample += pick([c for c in mine if c["class"] == cls], n, random.Random(f"{a.seed}:boundary:{d}:{cls}"))
    doc = {"seed": a.seed, "per_form": a.per_form, "covers": "skipped (the PI, 2026-10-01)",
           "frame": {f: dict(c) for f, c in frames.items()}, "tests": sample}
    (HERE / "sample.json").write_text(json.dumps(doc, indent=1) + "\n")
    table = Counter((s["form"], s["domain"]) for s in sample)
    print(f"{'form':20s}" + "".join(f"{d:>10s}" for d in SERVICES) + f"{'all':>8s}")
    for form in list(FORMS) + ["boundary"]:
        print(f"{form:20s}" + "".join(f"{table[(form, d)]:>10d}" for d in SERVICES) + f"{sum(table[(form, d)] for d in SERVICES):>8d}")
    print(f"{'all':20s}" + "".join(f"{sum(table[(f, d)] for f in list(FORMS) + ['boundary']):>10d}" for d in SERVICES) + f"{len(sample):>8d}")
    print("boundary classes:", dict(Counter(s["class"] for s in sample if s["form"] == "boundary")))


if __name__ == "__main__":
    main()
