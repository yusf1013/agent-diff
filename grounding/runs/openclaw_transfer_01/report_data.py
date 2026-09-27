"""Every number cited in report.md, computed from the run records and the manual labels (no model or service calls).

    python3 -m grounding.runs.openclaw_transfer_01.report_data [--variant runs/verify1]
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from grounding.runs.openclaw_transfer_01.analyze import (OK, collect, primary, strict_facts, toy_rows)
from grounding.runs.openclaw_transfer_01.behaviors import scan
from grounding.runs.openclaw_transfer_01.disclosure import toy_texts

HERE = Path(__file__).resolve().parent
RUNS = [HERE / "runs" / r for r in ("t1", "t1r", "t2")]
SENSITIVE = ("present", "told-packed", "contrast-alt", "alt-sweep", "wording")
PRESUPPOSING = ("presupposing-packed", "presupposing-isolated", "presupposing-plain")
ABSENCE = ("told-packed", "contrast-alt", "contrast-plain", "alt-sweep")
ONLY = re.compile(r"\bthe only\b|\bonly one\b|\bonly match\b", re.I)


def clear(r: dict, harness: str) -> bool:
    return r.get("outcome") == "incorrect" or r.get("outcome") in OK or (harness == "oc" and r.get("oc_outcome") == "asked")


def frac(rows: list[dict], harness: str) -> str:
    c = [r for r in rows if clear(r, harness)]
    wrong = sum(r.get("outcome") == "incorrect" for r in c)
    return f"{wrong}/{len(c)} ({100 * wrong / len(c):.0f}%)" if c else "–"


def failing(rows: list[dict]) -> Counter:
    return Counter(x for r in rows if r.get("condition") in SENSITIVE and r.get("outcome") in ("incorrect", "recovered")
                   for x in r.get("exposed", []))


def oc_text(r: dict) -> str:
    record = json.loads((Path(r["attempt"]) / "solver" / f"{r['case_id']}.json").read_text())
    return " ".join((s.get("thinking") or "") + " " + (s.get("text") or "") for s in record.get("steps", [])) + " " + \
        (Path(r["attempt"]) / "solver" / "final_response.md").read_text()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", type=Path)
    args = parser.parse_args()
    all_rows = collect(RUNS)
    oc = primary([r for r in all_rows if r.get("status") == "completed"])
    toy = primary(toy_rows())

    print("## Presupposing and absence-permitted totals")
    for label, conds in (("presupposing", PRESUPPOSING), ("absence permitted", ABSENCE), ("present", ("present",))):
        print(f"- {label}: toy {frac([r for r in toy if r['condition'] in conds], 'toy')}, "
              f"OpenClaw {frac([r for r in oc if r.get('condition') in conds], 'oc')}")
        for h, rows in (("toy", toy), ("oc", oc)):
            by = defaultdict(list)
            for r in rows:
                if r.get("condition") in conds:
                    by[r["domain"]].append(r)
            print(f"    {h}: " + ", ".join(f"{d} {frac(v, h)}" for d, v in sorted(by.items())))
    pre = [r for r in oc if r.get("condition") in PRESUPPOSING]
    print(f"- OpenClaw presupposing outcomes: {dict(Counter(r['oc_outcome'] for r in pre))}")

    print("\n## Distinct failing requirements (fact-sensitive forms)")
    t, o = failing(toy), failing(oc)
    print(f"- toy {len(t)}, OpenClaw pooled {len(o)}, shared {len(set(t) & set(o))}")
    for trial in ("t1", "t2"):
        print(f"- OpenClaw {trial}: {len(failing([r for r in oc if r['run'].rstrip('r') == trial]))}")
    print(f"- OpenClaw only: {sorted(set(o) - set(t))}")
    print(f"- toy only: {sorted(set(t) - set(o))}")
    for name, rows in (("toy", toy), ("OpenClaw", oc)):
        for engaged in (False, True):
            s = strict_facts(rows, engaged)
            failed = sum(1 for v in s.values() if v[1])
            print(f"- facts {name} {'engaged' if engaged else 'strict'}: tested {len(s)}, failed {failed}, held {len(s) - failed}")
    s = strict_facts(oc, True)
    print("- OpenClaw engaged failed/tested: " + ", ".join(f"{k[1]} {v[1]}/{v[0]}" for k, v in sorted(s.items()) if v[1]))

    print("\n## Disclosure of wrong actions in fact-sensitive forms (incl. contrast-plain)")
    disc = json.loads((HERE / "disclosure_labels.json").read_text())
    sens = SENSITIVE + ("contrast-plain",)
    for name, rows, key in (("toy", toy, "toy"), ("OpenClaw", oc, "openclaw")):
        wrong = [r for r in rows if r.get("condition") in sens and r.get("outcome") == "incorrect"]
        labels = [disc[key].get(f"{r['run']}/{r['case_id']}") for r in wrong]
        missing = [f"{r['run']}/{r['case_id']}" for r, l in zip(wrong, labels) if not l]
        got = [l for l in labels if l]
        line = f"- {name}: {len(wrong)} wrong; {dict(Counter(l['reply'] for l in got))}"
        if key == "openclaw":
            line += (f"; noticed {sum(bool(l.get('noticed')) for l in got)}, noticed but not flagged "
                     f"{sum(1 for l in got if l.get('noticed') and l['reply'] != 'flagged')}")
        print(line + (f"; UNLABELED {missing}" if missing else ""))

    print("\n## 'the only' in reasoning or reply of wrong actions (all non-Slack conditions)")
    ocw = [r for r in oc if r.get("outcome") == "incorrect" and r.get("condition") != "slack"]
    tw = [r for r in toy if r.get("outcome") == "incorrect"]
    print(f"- OpenClaw {sum(bool(ONLY.search(oc_text(r))) for r in ocw)}/{len(ocw)}, "
          f"toy {sum(bool(ONLY.search(' '.join(toy_texts(r)))) for r in tw)}/{len(tw)}")

    print("\n## Offers and follow-ups")
    offers = [r for r in oc if r.get("oc_outcome") in ("absent_offered", "asked")]
    sent = [r for r in offers if json.loads((Path(r["attempt"]) / "execution_summary.json").read_text())
            .get("followup", {}).get("sent")]
    print(f"- offers or questions: {len(offers)}; follow-up sent: {len(sent)}; "
          f"outcomes: {dict(Counter(r.get('followup_outcome') or 'slack (manual)' for r in sent))}")
    print(f"- offers without follow-up: {[f'{r['run']}/{r['case_id']}' for r in offers if r not in sent]}")

    print("\n## Consistency across trials (same verdict on every trial)")
    for name, rows, h in (("toy", toy, "toy"), ("OpenClaw", oc, "oc")):
        by = defaultdict(list)
        for r in rows:
            if r.get("condition") not in ("env-limited", "slack") and clear(r, h):
                by[r["case_id"]].append(r.get("outcome") == "incorrect")
        multi = [v for v in by.values() if len(v) >= 2]
        print(f"- {name}: {sum(len(set(v)) == 1 for v in multi)}/{len(multi)}")

    print("\n## Harness behaviour and health (latest completed attempt per case)")
    done = {r["attempt"]: r for r in all_rows if r.get("status") == "completed"}
    kinds, usage = Counter(), Counter()
    for attempt, r in done.items():
        for kind in scan(Path(attempt), r["case_id"]):
            kinds[kind] += 1
        for k, v in (r.get("usage") or {}).items():
            if isinstance(v, (int, float)):
                usage[k] += v
    print(f"- attempts: {len(done)}; behaviours (attempts): {dict(kinds)}")
    print(f"- usage: {dict(usage)}; extra upstream attempts: "
          f"{(usage['attempts'] - usage['requests']) / usage['requests']:.1%}")
    revised = [p for run in RUNS for p in run.glob("*/attempt-*/execution_summary.json")
               if json.loads(p.read_text()).get("status_revised")]
    print(f"- infrastructure reruns: {len(revised)}: " + ", ".join(
        f"{p.parts[-4]}/{p.parts[-3]} {json.loads(p.read_text())['status_revised'].get('rule', 'R1 provider hang')}" for p in revised))
    labels = json.loads((HERE / "manual_labels.json").read_text())
    print(f"- probe writes: {[k for k, v in labels.items() if isinstance(v, dict) and v.get('probe_write')]}")
    print(f"- recovered: {[k for k, v in labels.items() if isinstance(v, dict) and v.get('outcome') == 'recovered']}")

    if args.variant:
        var = primary([r for r in collect([args.variant.resolve()]) if r.get("status") == "completed"])
        cases = {r["case_id"] for r in var}
        print(f"\n## Variant {args.variant.name} ({len(var)} runs) vs default trials on the same cases")
        for label, conds in (("presupposing", PRESUPPOSING), ("absence permitted", ABSENCE), ("present", ("present",)),
                             ("slack", ("slack",))):
            base = [r for r in oc if r.get("condition") in conds and r["case_id"] in cases]
            print(f"- {label}: default {frac(base, 'oc')}, variant {frac([r for r in var if r.get('condition') in conds], 'oc')}")
        print(f"- variant outcomes: {dict(Counter(r['oc_outcome'] for r in var))}")


if __name__ == "__main__":
    main()
