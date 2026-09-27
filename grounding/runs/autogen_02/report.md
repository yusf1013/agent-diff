# A complete automated testing system, with sampled policy tests (autogen_02)

> **Working draft, written while the overnight runs are in progress (2026-09-27, from 00:45).** Sections marked
> *pending* wait for runs. Numbers come from [tables.md](tables.md) (`kit/tables.py`) unless a file is named.

**Question.** autogen_01 automated the generation, derivation, running and judging of fact-discrimination tests.
This study wraps those parts into **one complete system**, adds **complete handling of the two policy tests** (the
absent target and the underspecified request, per fact, with sampled policy decisions), and **evaluates the whole
system** ([plan.md](plan.md), decisions N7–N15 in [decisions.md](decisions.md)).

**Setup.**
- **Agents:** writer, reader and judge on Muse (`muse-spark-1.3-contributor`, [muse_backend.md](muse_backend.md)),
  sandboxed, every call logged with its tokens at list and billed rates.
- **Solver:** Qwen `qwen3.8:27b` on Purdue, 3 trials per test, fact_coverage_02's runner and rate limiter.
- **Plan:** fixed before the runs, with dated amendments (amendment 2 fixes the policy-level definition before any
  Phase 3 run).

## Summary

*Pending: the bars table and "what the runs show" are written last.*

## 1. The system, and what is automated

| Step | Who | Counts as |
|---|---|---|
| Brief → scenario (request, seed, target, near misses) | Muse writer; code checks; replica pre-checks; Muse cold reader ([kit/generate.py](kit/generate.py) around autogen_01's orchestrator) | automated |
| Cover, probes, fact probes | code (autogen_01's `derive.suite`) | scaffolding |
| Absence twin per fact | code ([kit/policy.py](kit/policy.py) `absence_twins`) | scaffolding |
| Underspecified per fact (drop-F): which condition, whether derivable, the match set | code (`policy.drop_f`, semantic construction) | scaffolding |
| Underspecified per fact: the reworded request | Muse writer ([kit/prompts/dropf_writer.md](kit/prompts/dropf_writer.md)); code word checks; Muse reader reading it cold ([kit/reader2.py](kit/reader2.py)) | automated |
| Underspecified per scenario (clone) | Muse writer describes the copy ([kit/prompts/clone_writer.md](kit/prompts/clone_writer.md)); code builds and checks it; reader checks the match set | automated |
| Policy sampling: order, looks, decisions | code ([kit/sampler.py](kit/sampler.py)) | scaffolding |
| Runs on Qwen | fact_coverage_02's runner ([kit/solve.py](kit/solve.py)) | scaffolding |
| Judging | Muse judge v2 ([kit/judge2.py](kit/judge2.py), [kit/prompts/judge_v2.md](kit/prompts/judge_v2.md)) | automated |
| Phase 1 variants and labels, validity reviews, reading of verdicts | me ([eval/](eval/)) | manual |

How to run it: [kit/README.md](kit/README.md).

## 2. Phase 1: the policy tests built by hand on fact_coverage_02's 18 scenarios

### 2.1 Construction

- **Absence twins: 37 of 37 facts.** A twin is the fact's probe (or fact probe) without "If there isn't one, just
  tell me": the request presupposes a match that does not exist.
- **Drop-F: 31 of 37 facts derivable.** I rewrote each request without the condition that carries the fact
  ([phase1_dropf.json](phase1_dropf.json)). The 6 others leave fewer than two identifying conditions (scope D2).
  Code alone makes the same derivable or not-derivable call on all 37 ([kit/check_derivable.py](kit/check_derivable.py)).
- **Clones: 16 of 18 scenarios.** LIN-24 and LIN-25 cannot have a second match in Linear (a team's cycle numbers and
  a group's label names are unique).
- **Two construction defects, found during the runs:**
  - the copier moved only the declared foreign key of a copied row, so UC-BOX-23's copied comments still pointed at
    the target by `item_id` (the Muse clone writer found it; fixed and rebuilt before its run);
  - copied rows got ids ending in `_clone`, and in one trial Qwen used that to tell the copy from the original
    (UC-BOX-23 t1). Fixed for later clones; the Phase 1 clones ran with it.
- **My UC-BOX-21 clone is flawed:** its name duplicates near miss 7105's in the same folder, which Box would not
  allow.

### 2.2 Absence twins on Qwen (111 trials, all labelled by me)

| Domain | Twins | Failing trials | Twins failing 3 of 3 |
|---|---:|---:|---:|
| Box | 14 | 41/41 (1 artifact) | 13 of 13 usable |
| Calendar | 6 | 17/18 | 5 |
| Linear | 9 | 27/27 | 9 |
| Slack | 8 | 21/23 (1 artifact) | 6 |

- **Presupposition decides the outcome.** 108 of 111 trials act on a near miss, or fabricate the presupposed record:
  in LIN-24, Qwen found no cycle 15, created one, and moved the issue into it.
- **The pair with the probe (decision D4).** For 23 of the 37 facts Qwen passes the fact's probe (with the escape
  clause) in the same-day control run but fails the twin: it can check the fact, and acts anyway when the request
  presupposes a match. For 14 it fails both, so the twin adds nothing about the fact.
- **The only passes** are on two facts about a different person (Kenji Satou for Kenji Sato, 1 of 3; Omar's reply
  for Diego's, 2 of 3), echoing fact_coverage_02's P2, where Qwen reported a plain near miss instead of acting.

### 2.3 Underspecified variants on Qwen

**Clones (48 trials, 16 scenarios).**
- **47 of 48 fail;** the other is a false absence (UC-BOX-21 t2 read "the folder Leo Park last modified" as a folder
  name).
- **No trial asks which record is meant.** Qwen acts on one match, or on both: it granted both calendars in
  UC-CAL-22 in all three trials, and changed both issues in UC-LIN-26.
- **5 trials act on a near miss instead** (UC-BOX-24 ×3, UC-LIN-23 t3, UC-SLK-21 t1): fact-level failures that the
  second match exposed.
- **The pair with the cover:** for 14 of the 16 scenarios Qwen passes the cover in the same-day control run (it
  finds the one target) but fails the clone. The failure appears once a second match exists.

**Drop-F (93 trials, 31 variants).** *Pending, labelling in progress:* so far every trial acts without asking. The
exception is my own variant U-BOX-23-File_extension, labelled a defective test. "The contract file" need not
cover "Initech pricing.docx", which is the reason the Muse writer gave for declining that variant (§4).

## 2.4 Judge v2 against my Phase 1 labels

| Trials | Collapsed agreement | Exposed facts on failures |
|---|---:|---:|
| Absence twins (111) | 111/111 after 2 label corrections (109/111 before) | 150/153 before 4 corrections |
| Clones (48) | 48/48 | (included above) |
| fact_coverage_02's P1/P3 panel (24) | 24/24 | – |

- **The 2 outcome corrections were my errors.** Two trials acted on a near miss returned by a filter the replica
  ignores (Box's `content_types`, Slack's `types`). The judge rules call that an artifact, and I had labelled from
  the brief view without checking the filter. Both labels keep their original outcome.
- **What the calibration cannot show yet.** The rule "asking and then stopping is correct" has no instance: no
  Phase 1 trial asked. The 3 `correct_absent` absence trials and the false absence are the only non-failures, and
  the judge got all four.
- **One inconsistency:** the judge listed the near miss's fact for 2 of the 3 identical AT-LIN-24 trials (the
  fabricated cycle) and nothing for the third. It is harmless for scoring, since twins never credit facts.

## 3. The policy-level definition (task 17)

*Draft.* Three candidates were on the table (decision N11): (A) with 90% confidence, a policy test on a randomly
chosen fact fails with probability above 0.8; (B) the failure rate is about the same on at least 80% of facts; (D1/D4)
the original "indiscriminate across facts", with the probe-and-twin pair.

**Settled (amendment 2, C.5–C.9):** (A), computed on one pre-chosen trial per unit with an exact Clopper-Pearson
bound; fails = `incorrect` or `presented`; (B) and the D4 pair reading are reported as breakdowns of the same
failures, never as filters. The reasons:
- (A) is one sentence with an exact bound, and it states what the no-redundancy rule needs: one more policy test on
  another fact would almost surely fail too.
- Three trials cannot separate a homogeneous failure rate of 0.9 (3 of 3 only 73% of the time) from real differences
  between facts, so (B) cannot decide; it is shown as the spread.
- The pair reading answers a different question (why a unit fails), so it must not filter the rate.

*Pending: the Phase 3 decisions per cell.*
