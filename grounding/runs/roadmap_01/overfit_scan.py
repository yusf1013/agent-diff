"""The mechanical half of the overfit audit: which names, phrases and identifiers of the prompts the automated system
sends also appear in the tests (requests and seeds) and in the hand labels. Reads files only.

    python grounding/runs/fact_coverage_02/launch.py grounding.runs.roadmap_01.overfit_scan

Tokens taken from each prompt source: capitalized name phrases, quoted phrases, identifier-like words (pat.kim,
q3-close, ENG-42), and every 5-word phrase. The seed builders' default people (seed_ops.md) are reported apart: a
test that uses them follows the seed conventions, it does not copy a prompt. Writes overfit_scan.json.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent
G = RUNS.parent
A1, A2 = RUNS / "autogen_01", RUNS / "autogen_02"
DOMAINS = ("box", "calendar", "linear", "slack")

PROMPTS = {  # source -> (who receives it, path)
    "writer.md": ("scenario writer", A1 / "kit/prompts/writer.md"),
    "reader.md": ("cold reader (scenarios, drop-F expected-set mode, clones)", A1 / "kit/prompts/reader.md"),
    "method.md": ("scenario writer", A1 / "kit/docs/method.md"),
    "format.md": ("scenario writer", A1 / "kit/docs/format.md"),
    "box-example.json": ("scenario writer", A1 / "kit/examples/box-example.json"),
    "calendar-example.json": ("scenario writer", A1 / "kit/examples/calendar-example.json"),
    "judge.md (v1)": ("judge v1", A1 / "kit/prompts/judge.md"),
    "judge_v2.md": ("judge v2", A2 / "kit/prompts/judge_v2.md"),
    "dropf_writer.md": ("drop-F request editor", A2 / "kit/prompts/dropf_writer.md"),
    "clone_writer.md": ("clone author", A2 / "kit/prompts/clone_writer.md"),
}
for d in DOMAINS:
    PROMPTS[f"{d}/replica.md (autogen_02)"] = ("writer, clone author, judge", A2 / "inputs" / d / "replica.md")
    PROMPTS[f"{d}/seed_ops.md"] = ("scenario writer", A1 / "inputs" / d / "seed_ops.md")
    PROMPTS[f"{d}/model.md"] = ("scenario writer", G / "domains" / d / "model.md")

NAME = re.compile(r"\b([A-Z][a-z0-9]+(?:[ '][A-Z0-9][A-Za-z0-9]+){1,3})\b")
QUOTED = re.compile(r"[\"“']([^\"“”'\n]{4,60})[\"”']")
IDENT = re.compile(r"\b([a-z]+(?:[._-][a-z0-9]+)+|[A-Z]{2,5}-\d+|q\d-[a-z]+)\b")
WORD = re.compile(r"[a-z0-9']+")
GENERIC = {"Google Calendar", "Box", "Slack", "Linear", "The", "A", "An", "Room", "API", "JSON", "UTC", "ISO",
           "All Files", "Northwind", "Agent Bot", "New York", "Los Angeles", "northwind.example", "The API",
           "The File", "If there isn", "there isn", "sub-issue", "top-level", "one-to-one"}
ESCAPE = ("there isn't one", "just tell me", "there aren't any", "isn t one", "just tell")


def strings_in(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from strings_in(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings_in(v)
    elif isinstance(obj, str):
        yield obj


def text_of(path: Path) -> str:
    raw = path.read_text()
    return "\n".join(strings_in(json.loads(raw))) if path.suffix == ".json" else raw


def distinctive(t: str) -> bool:
    """A token worth matching: a phrase of two or more words, or one with a digit, dot, hyphen or underscore."""
    return len(t) >= 4 and (" " in t.strip() or re.search(r"[\d._-]", t) is not None)


def tokens(text: str) -> set[str]:
    out = {m.group(1) for m in NAME.finditer(text)} | {m.group(1).strip() for m in QUOTED.finditer(text)} | \
          {m.group(1) for m in IDENT.finditer(text)}
    return {t for t in out if t not in GENERIC and distinctive(t) and not any(e in t.lower() for e in ESCAPE)}


def shingles(text: str, n: int = 5) -> set[str]:
    words = WORD.findall(text.lower().replace("’", "'"))
    sh = {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}
    return {s for s in sh if not any(e in s for e in ESCAPE)}


def default_people() -> set[str]:
    """The seed builders' default people, with their logins (first.last) and first names."""
    people = set()
    for d in DOMAINS:
        text = (A1 / "inputs" / d / "seed_ops.md").read_text()
        block = text[text.find("**People**"):text.find("\n- **", text.find("**People**") + 5)]
        names = {m.group(1) for m in re.finditer(r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b", block)}
        people |= names | {n.lower().replace(" ", ".") for n in names}
    return people


def tests():
    """Every test case the suites and policy runs used: id -> (request, seed text)."""
    out = {}
    folders = [A1 / "runs" / f"gen_arm_{a}" / "cases" for a in ("r", "p", "p_v2")] + \
              [A2 / "runs/phase4/batch1_cases", A2 / "runs/phase4/batch2_cases", A2 / "runs/phase4/batch1_policy_cases",
               A2 / "runs/phase3/units", RUNS / "fact_coverage_02" / "cases"]
    for folder in folders:
        for p in folder.rglob("*.json"):
            try:
                case = json.loads(p.read_text())
            except ValueError:
                continue
            if not isinstance(case, dict) or "prompt" not in case:
                continue
            out[case.get("case_id") or p.stem] = (case["prompt"], json.dumps(case.get("seed", ""), ensure_ascii=False))
    return out


def label_texts():
    out = {}
    for p in list((A2 / "eval").rglob("*.json")) + list((A1 / "eval").rglob("*.json")):
        try:
            out[str(p.relative_to(RUNS))] = p.read_text()
        except OSError:
            pass
    return out


def main():
    cases = tests()
    people = default_people()
    labels = label_texts()
    report = {"tests_scanned": len(cases), "default_people": sorted(people), "sources": {}}
    request_shingles = {cid: shingles(req) for cid, (req, _) in cases.items()}
    for name, (who, path) in PROMPTS.items():
        if not path.exists():
            report["sources"][name] = {"missing": str(path)}
            continue
        text = text_of(path)
        in_requests, in_seeds, in_labels = defaultdict(list), defaultdict(list), defaultdict(list)
        for tok in sorted(tokens(text)):
            low = tok.lower()
            for cid, (req, seed) in cases.items():
                if low in req.lower():
                    in_requests[tok].append(cid)
                elif low in seed.lower():
                    in_seeds[tok].append(cid)
            if not tok in people:
                for lf, lt in labels.items():
                    if low in lt.lower():
                        in_labels[tok].append(lf)
        src_sh = shingles(text)
        shared = {cid: sorted(src_sh & sh) for cid, sh in request_shingles.items() if src_sh & sh}
        split = lambda d: ({t: v for t, v in d.items() if t in people}, {t: v for t, v in d.items() if t not in people})
        rp, rn = split(in_requests)
        sp, sn = split(in_seeds)
        report["sources"][name] = {
            "received_by": who, "path": str(path.relative_to(G.parent)),
            "tokens_in_requests": {t: sorted(v) for t, v in sorted(rn.items(), key=lambda x: -len(x[1]))},
            "tokens_in_seeds_only": {t: len(v) for t, v in sorted(sn.items(), key=lambda x: -len(x[1]))},
            "default_people_in_requests": {t: len(v) for t, v in rp.items()},
            "tokens_in_labels": {t: sorted(set(v)) for t, v in in_labels.items()},
            "requests_sharing_5_word_phrases": shared}
    (HERE / "overfit_scan.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print("tests scanned:", len(cases))
    for name, r in report["sources"].items():
        if "missing" in r:
            print(f"{name}: MISSING {r['missing']}")
            continue
        top = list(r["tokens_in_requests"].items())[:6]
        print(f"{name}: {len(r['tokens_in_requests'])} tokens in requests "
              f"({', '.join(f'{t!r}:{len(v)}' for t, v in top)}); {len(r['tokens_in_seeds_only'])} in seeds only; "
              f"{len(r['requests_sharing_5_word_phrases'])} requests share 5-word phrases; "
              f"{len(r['tokens_in_labels'])} tokens in label files")


if __name__ == "__main__":
    main()
