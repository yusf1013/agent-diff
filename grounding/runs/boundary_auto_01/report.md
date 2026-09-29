# boundary_auto_01: automating the capability-boundary method (phases 2 and 3)

*2026-09-28, overnight. The method is [../boundary_02/method.md](../boundary_02/method.md) (version 1.2), made by
hand in the manual investigation. Here Muse (`muse-spark-1.3-contributor`) does the creative step (the request's
wording) and names what the request asks for; code builds the oracle's spec and the test; the self-hosted Qwen is the
instrument. Numbers marked [pending] are filled as the runs finish.*

## What is automated, and what is not yet

| Step | Phase 1 (manual) | Here |
|---|---|---|
| The space: derivation over the fact catalog, filters on the replica | [catalog.py](../boundary_02/catalog.py), [space.py](../boundary_02/space.py) (93 faithful of 152) | taken as input, not re-derived |
| The request | hand-worded ([tests.py](../boundary_02/tests.py)) | the Muse writer, one call per service, from the element's description and the seed ([writer.py](writer.py)) |
| What the request asks for | hand-written oracle spec per element ([oracle.py](../boundary_02/oracle.py), SPEC) | the writer's structured target; code turns it into the spec ([specs.py](specs.py)) |
| Request check | by eye | a cold Muse reader: the record it names, no hint of the limit, natural wording ([reader.py](reader.py)) |
| Seed | per service ([probe_elements.py](../boundary_02/probe_elements.py)) | the same |
| Oracle | the state first, then the answer; the PI's rulings | the same, with the generated spec ([grade.py](grade.py)) |

## Phase 2: does the automation meet the manual standard?

**The oracle's spec.** Every graded phase-1 trial (275, cycles 2–6, void trials out) was judged again with the spec
generated from the writer's target. The generated spec agrees with the hand spec on **272 of 275** trials; 91 of 93
elements agree on every trial. The two that do not carry knowledge the target lacks:
- LIN-04 (a completion date): the hand spec counts the state change that sets it as a move toward the fact;
- LIN-19 (the Web team's In Review state): the hand spec names the state by description, so a re-creation that keeps
  everything can pass; the generated spec names it by id.

**The requests.** The cold reader's verdicts: [pending].

## Phase 3: the numbers

[pending: coverage space; tests generated; valid; failures exposed by kind of alternative; judge true and false
positives; tokens and costs]
