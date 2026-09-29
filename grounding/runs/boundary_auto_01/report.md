# boundary_auto_01: automating the capability-boundary method (phases 2 and 3)

*2026-09-28/29, overnight. The method is [../boundary_02/method.md](../boundary_02/method.md) (version 1.2), made by
hand in the manual investigation. Here Muse (`muse-spark-1.3-contributor`) does the creative step (the request's
wording) and names what the request asks for; code builds the oracle's spec and the test; the self-hosted Qwen is the
instrument. Numbers from [summary.py](summary.py) → `summary.json`.*

## The numbers the PI asked for

[pending: filled when runs/p3b is graded]

## What is automated, and what is not yet

| Step | Phase 1 (manual) | Here |
|---|---|---|
| The space: derivation over the fact catalog, filters on the replica | [catalog.py](../boundary_02/catalog.py), [space.py](../boundary_02/space.py) (93 faithful of 152) | taken as input, not re-derived |
| The request | hand-worded ([tests.py](../boundary_02/tests.py)) | the Muse writer, one call per service, from the element's description and the seed ([writer.py](writer.py)) |
| What the request asks for | hand-written oracle spec per element ([oracle.py](../boundary_02/oracle.py), SPEC) | the writer's structured target; code turns it into the spec ([specs.py](specs.py)) |
| Request check | by eye | a cold Muse reader: the record it names, no hint of the limit, natural wording ([reader.py](reader.py)) |
| Seed | per service ([probe_elements.py](../boundary_02/probe_elements.py)) | the same |
| Oracle | the state first, then the answer; the PI's rulings | the same, with the generated spec ([grade.py](grade.py)) |
| The judge's review | every failure read by hand | a seeded quarter of the trials read by hand, drawn before the verdicts ([review.py](review.py)) |

The derivation stays manual in this study. It is mechanical once the fact catalog exists (one element per attribute
without a writing operation, one per precondition), but the filters need a probe per element on the replica, which
phase 1 made by hand.

## Phase 2: does the automation meet the manual standard?

**The oracle's spec.** Every graded phase-1 trial (275, cycles 2–6, void trials out) was judged again with the spec
generated from the writer's target. The generated spec agrees with the hand spec on **272 of 275** trials; 91 of 93
elements agree on every trial. The two that do not carry knowledge the target lacks:
- LIN-04 (a completion date): the hand spec counts the state change that sets it as a move toward the fact;
- LIN-19 (the Web team's In Review state): the hand spec names the state by description, so a re-creation that keeps
  everything can pass; the generated spec names it by id.

**The requests.** The cold reader (a fresh Muse session per request, no view of the limit or the element) agreed on
**89 of 93**: it named the record the element is about, found no hint of the limit, and judged the wording natural.
No request hinted at the limit. The four it refused are real writer errors, so the four tests are invalid:
- SLA-34: "Diego's message in #payments-ops": there is no such message in the seed;
- CAL-18: "the Budget review from Leo's on-call calendar": the event is on the actor's calendar;
- BOX-06: "Convert Budget 2026.docx to a PDF": read as creating a new file, not changing the named one;
- LIN-24: "Show Priya's comment as written on September 10": read as a display request, with nothing to change.

The first version of the reader also rejected requests that are impossible by design ("the request names a change
the service cannot make"). Its prompt now judges the wording only (the first verdicts are kept in `reader.v1.json`).

## Phase 3: the numbers

[pending]

## Files

- [writer.py](writer.py) → `writer.json`; [specs.py](specs.py) → `specs.json` (the phase-2 agreement);
  [reader.py](reader.py) → `reader.json`; [cases.py](cases.py) → `cases/`; [grade.py](grade.py) →
  `digest-<run>.json`, `grades-<run>.json`; [review.py](review.py) → `review.json`; [summary.py](summary.py) →
  `summary.json`.
- Muse calls: `runs/calls.jsonl`, `runs/writer/`, `runs/reader/` (prompts, transcripts, usage).
- Solver runs: `runs/p3a` (16 cases, beside the several-match batch at 3 in flight) and `runs/p3b` (77 cases at 9);
  the split is in `batches.json`.
