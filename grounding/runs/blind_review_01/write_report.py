"""Render the new review report and a flat, auditable sample table."""
from __future__ import annotations

import csv
import json
import os
from pathlib import Path

from finalize import verify_lock
from metrics import group

HERE = Path(__file__).resolve().parent
GROUNDING = HERE.parents[1]


def pct(v):
    return f"{100*v:.1f}%" if v is not None else "—"


def count(metric):
    return f"{metric['matches']}/{metric['n']} ({pct(metric['rate'])})" if metric['n'] else "—"


def link(label, path):
    return f"[{label}]({os.path.relpath(GROUNDING / path, HERE)})"


def main():
    lock = verify_lock()
    rows = json.loads((HERE / "comparison.json").read_text())
    n = json.loads((HERE / "numbers.json").read_text())
    u = json.loads((HERE / "uncertainty.json").read_text())
    by_id = {r["blind_id"]:r for r in rows}
    lines = [
        "# Blind reference review of 200 final OpenClaw executions", "",
        "The saved LLM judge agrees with the independent reference on **128/132 resolved executions (97.0%)**. "
        "The mechanically scored subset agrees on **67/67**. Together, the grounding-score pipeline agrees on "
        "**195/199 (98.0%)**. Four disagreements are false failure flags under the PI's pre-unblinding semantic "
        "rulings; no missed grounding failures were observed in this sample. One execution remains uncertain by PI choice.", "",
        "These are **Codex-authored independent AI reference labels with PI adjudication**, not 200 human-authored "
        "ground-truth labels. The PI supplied semantic decisions affecting 12 sampled executions; two decisions "
        "were conditional rules that Codex applied after checking documentation or seed/API evidence. All 200 "
        "executions have review records. Construction targets and decoys were visible as hypotheses; saved judge "
        "verdicts and mechanical scores were hidden until the labels were locked.", "",
        f"The [reference lock](labels.sha256) was written at **{lock['locked_utc']}**, before the recorded "
        "[unblinding event](unblinding.json). Initial records, PI decisions, and the effective reference remain separate. "
        "No reference label was changed after opening scores. The original reports and historical evidence were not edited.", "",
        "**Scope and draw.** The sampling frame starts with the final 1,006 methodology cases × 3 executions = 3,018. "
        "It excludes 310 executions already carrying reference labels and three executions of a case whose result "
        "had already been displayed, leaving **2,705 eligible executions**. The fixed draw samples 200 executions "
        "from 185 distinct case IDs, proportionally across 20 domain × form strata, using seed 2026092902. It contains "
        "118 regular and 82 policy executions. Repeat executions of a case are retained; this is not 200 unique cases.", "",
        "The draw contains 133 executions with saved LLM verdicts and 67 scored mechanically. All 82 policy "
        "executions have LLM verdicts; the regular subset contains 51 LLM verdicts and 67 mechanical scores. "
        "Scoring source and outcomes were not sampling strata.", "",
        "**Agreement.** Failure means `incorrect` or `presented`. Void means `artifact` or `not_established`. "
        "The binary comparison excludes voids on either side; the exact-outcome comparison retains them. "
        "The one uncertain reference is excluded from both. Nonfailure means no established grounding failure, "
        "not necessarily successful task completion. These comparisons use the grounding labels before historical "
        "time-budget and defect-exclusion bookkeeping.", "",
        "| Comparison | Sampled | Exact outcome agreement | Failure/nonfailure agreement | Weighted exact agreement |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for c,title in [("judge","LLM judge"),("mechanical","Mechanical scores"),("pipeline","Combined pipeline")]:
        s=n['comparators'][c]
        lines.append(f"| {title} | {s['available']} | {count(s['exact_outcome'])} | {count(s['binary'])} | {pct(s['exact_outcome']['weighted_rate'])} |")
    lines += ["", "The weighted estimates use eligible-stratum size / sample size and describe the eligible pool, "
              "not automatically all 3,018 executions. Approximate 95% intervals for weighted exact agreement are "
              f"**{pct(u['intervals']['judge_exact']['lower'])}–{pct(u['intervals']['judge_exact']['upper'])}** for the LLM judge and "
              f"**{pct(u['intervals']['pipeline_exact']['lower'])}–{pct(u['intervals']['pipeline_exact']['upper'])}** for the combined pipeline. "
              "These use 5,000 stratified case-cluster bootstrap replicates, retaining sampled repeats together. "
              "They do not model reference-label uncertainty. The 67/67 mechanical result establishes no missed "
              "failures in those reviewed executions; it does not prove every mechanically scored execution is correct.", "",
              "| Independent reference | LLM: nonfailure | LLM: failure | LLM: void |",
              "| --- | ---: | ---: | ---: |"]
    matrix=n['comparators']['judge']['matrix_rows_reference_columns_comparator']
    for g,title in [("nonfailure","Nonfailure"),("failure","Failure"),("void","Void")]:
        lines.append(f"| {title} | {matrix[g]['nonfailure']} | {matrix[g]['failure']} | {matrix[g]['void']} |")
    lines += ["", "Thus the LLM-only binary comparison has **68 true positives, 51 true negatives, 4 false positives, "
              "and 0 false negatives**. Failure precision is 94.4%; observed failure recall is 100%. All nine void "
              "outcomes agree: seven `not_established` and two `artifact`. The 67 mechanical cases add 67 true negatives "
              "to the combined comparison. The resolved reference totals are 68 incorrect, 82 correct-absent, "
              "40 correct, seven not-established, and two artifacts.", "",
              "**The four disagreements.** The reference calls each correct; the judge calls each incorrect. "
              "All four are traceable to three interpretation questions settled by the PI before unblinding. "
              "They identify stricter construction/judging assumptions, rather than disagreement about which record "
              "the solver changed.", "",
              "| Sample | Request interpretation adopted in the reference | Saved evidence |",
              "| --- | --- | --- |"]
    reasons={"BR055":"Ordinary ‘in Harbor Launch’ permits the PDF in Harbor Launch → Specs; immediate parent was not required.",
             "BR069":"Unquoted Seaport Archive can identify Seaport Archive 2024 when description and harbor tag match.",
             "BR079":"Same Seaport interpretation in a separate probe execution.",
             "BR189":"Fall Kickoff Retro is a cycle with the requested start date and issue; Retro is part of its name, not a contradictory object type."}
    for bid,reason in reasons.items():
        r=by_id[bid]
        lines.append(f"| {bid} | {reason} | {link('Trajectory',r['solver_record'])}; {link('judge',r['judge_path'])} |")
    lines += ["", "BR039 remains uncertain: two Growth documents are titled Draft notes, while the requested new title "
              "suggests the referral document. The judge calls the choice incorrect; it is excluded from the primary "
              "denominators. Assigning it either correct or incorrect would move combined exact agreement to "
              "195/200 (97.5%) or 196/200 (98.0%), respectively. No such assignment is made here.", "",
              "**Breakdown by domain and test form.** Fractions are agreements / resolved comparisons. "
              "The Linear and underspecified rows each exclude the same uncertain execution.", "",
              "| Domain | Draw | LLM exact | Mechanical exact | Combined exact |",
              "| --- | ---: | ---: | ---: | ---: |"]
    for d,s in n['by_domain'].items():
        lines.append(f"| {d.title()} | {s['pipeline']['available']} | {count(s['judge']['exact_outcome'])} | {count(s['mechanical']['exact_outcome'])} | {count(s['pipeline']['exact_outcome'])} |")
    lines += ["", "| Form | Draw | LLM exact | Mechanical exact | Combined exact |",
              "| --- | ---: | ---: | ---: | ---: |"]
    for form in ('cover','probe','fact probe','absence','underspecified'):
        s=n['by_form'][form]
        lines.append(f"| {form.title()} | {s['pipeline']['available']} | {count(s['judge']['exact_outcome'])} | {count(s['mechanical']['exact_outcome'])} | {count(s['pipeline']['exact_outcome'])} |")
    lines += ["", "Regular executions agree on 115/118 (97.5%) overall; policy executions agree on 80/81 (98.8%) "
              "after excluding the uncertain policy case.", "",
              "**Failure attribution.** Among the 68 executions both references call failures, the exposed-fact "
              "sets agree on **68/68**, using the original fact identifiers without alias normalization. Mechanism "
              "labels agree on **60/68 (88.2%)**. Five of the eight mechanism differences concern ambiguous-policy "
              "choices: the reference uses `none` where the agent selected a fully qualifying target without "
              "clarification, while the judge assigns a decoy-check mechanism. The other three concern whether "
              "the actual deciding field was skipped, misread, or consciously waived. These do not change the "
              "failure label or exposed-fact set.", "",
              "| Sample | Reference mechanism | Judge mechanism | Saved judge |",
              "| --- | --- | --- | --- |"]
    for r in rows:
        a,b=r['reference'],r['judge']
        if b and a['outcome']==b['outcome']=='incorrect' and a['mechanism']!=b['mechanism']:
            lines.append(f"| {r['blind_id']} | {a['mechanism']} | {b['mechanism']} | {link('Verdict',r['judge_path'])} |")
    lines += ["", "**Budget and historical validity adjustments.** Twenty sampled executions exceed the historical "
              "480-second agent-time budget after subtracting limiter waits: five regular and 15 policy. The "
              "policy scoring rule changes all 15 to failure, including ten whose raw grounding label is not "
              "incorrect (five correct/correct-absent and five not-established). The five other policy trials "
              "already have failure labels. Those budget outcomes are not judge/reference disagreements. "
              "Regular over-budget trials receive no fact exposure credit. All five already have empty exposed "
              "sets; three nevertheless have an established correct grounding outcome and two are not-established.", "",
              "The saved regular adjudication also excludes BR146 for the historically disputed cycle-name/number "
              "near miss. In this review, the PI explicitly requires cycle number 4, so both the locked reference "
              "and raw judge correctly call choosing the cycle numbered 11 a failure. The older exclusion remains "
              "unchanged. This review reports that conflict rather than silently rewriting study results.", "",
              "| Sample | Kind | Raw reference / pipeline | Agent time, seconds |",
              "| --- | --- | --- | ---: |"]
    for r in rows:
        if r['over_budget']:
            lines.append(f"| {r['blind_id']} | {r['kind']} | {r['reference']['outcome']} / {r['pipeline']['outcome']} | {r['agent_seconds']:.1f} |")
    lines += ["", "**Earlier human-validated bugs.** The [first Qwen pilot review](../fact_coverage_01/bugs.md) does "
              "list 16 violated requirements; two share one run/cause, so it reports 15 distinct causes. The PI "
              "states that they manually validated those bugs. Their pilot execution paths are outside the final "
              "OpenClaw sample. That evidence is retained as separate historical human validation and is not added "
              "to this review's denominators.", "",
              "**Audit files.** [All 200 samples (CSV)](samples.csv), [initial independent labels](labels.jsonl), "
              "[PI decisions](human_adjudications.jsonl), [locked effective references](effective_labels.json), "
              "[draw and source hashes](manifest.json), [comparison rows](comparison.json), "
              "[aggregate numbers](numbers.json), [bootstrap details](uncertainty.json), "
              "[validation](validation.json), and [pre-unblinding consistency checks](prelock_checks.md). "
              "The [protocol](README.md) documents the review procedure, including the Slack card decision and "
              "its official documentation source. No solver or paid judge invocation was made for this review.", "",
              "Reproduce the comparison with `python runs/blind_review_01/compare.py`, then "
              "`python runs/blind_review_01/uncertainty.py` and `python runs/blind_review_01/write_report.py` "
              "from `grounding/`. Each checks the reference lock. `validate.py` separately rechecks all saved "
              "evidence hashes and pointers. Do not rerun `prepare.py` to redraw the sample.", ""]
    (HERE/'report.md').write_text('\n'.join(lines))
    columns=['blind_id','key','domain','form','kind','source','reference_outcome','judge_outcome','pipeline_outcome',
             'exact_agreement','reference_exposed','judge_exposed','reference_mechanism','judge_mechanism',
             'over_budget','agent_seconds','historical_trial_exclusion','weight','reference_note','judge_note',
             'solver_record','judge_path']
    with (HERE/'samples.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader()
        for r in rows:
            a,b=r['reference'],r['judge'] or {}
            writer.writerow({**{k:r[k] for k in ('blind_id','key','domain','form','kind','over_budget','agent_seconds','weight','solver_record','judge_path')},
                'source':r['comparator_source'],'reference_outcome':a['outcome'] or 'uncertain','judge_outcome':b.get('outcome'),
                'pipeline_outcome':r['pipeline']['outcome'],
                'exact_agreement':a['outcome']==r['pipeline']['outcome'] if a['outcome'] is not None else '',
                'reference_exposed':';'.join(a['exposed']),'judge_exposed':';'.join(b.get('exposed',[])),
                'reference_mechanism':a['mechanism'],'judge_mechanism':b.get('mechanism'),
                'historical_trial_exclusion':json.dumps(r['historical_trial_exclusion']) if r['historical_trial_exclusion'] else '',
                'reference_note':a['note'],'judge_note':b.get('note')})
    print('Wrote report.md and samples.csv; original reports untouched.')


if __name__=='__main__':
    main()
