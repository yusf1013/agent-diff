# attribution_01: who owns a failure? (roadmap step 5, first investigation)

*Pre-registered 2026-09-27 22:40 EDT, before any scoring. Changes after this point are dated amendments below.*

## The question

When a trial looks like a failure, which component does it belong to: the agent, the test, the mock, the harness or
the judge? The PI's definition is about attribution, not about why the agent failed; the mechanisms stay a matter
for manual analysis. Bad tests cannot be prevented completely, so the aim is to detect them with a valid reason.
Whether that belongs in the judge or in a separate step is an open question, and this study should answer it.

The judge cannot settle it alone. It takes the test as given, and a flawed test and a failing agent can leave the same
trajectory. So the study scores evidence that comes from outside the one trajectory's reading, against ground truth that
already exists.

## Owners

Each hand-labelled trial gets exactly one owner:

| Owner | Meaning | Typical evidence in the labels |
|---|---|---|
| `agent` | The agent's own failure: it acted on a non-target, presented one, reported a false absence, or stopped short. Misreading a natural but ambiguous request is included, as the PI ruled (2026-09-27). | outcomes `incorrect`, `presented`, `false_absence`, `incomplete` |
| `test-wording` | The request can reasonably be read so that the "decoy" meets it, or the target does not; this includes a verb that implies the dropped condition | `artifact` notes: "defective test", "contestable", "reasonable reading" |
| `test-construction` | The test's construction broke it: a probe that lost its trap, a seed value the mock rejects, a seed field that contradicts the request, a fact that depends on the run date | `artifact` notes: "seed artifact", "scenario artifact"; known defects found by the witness check |
| `mock` | The replica behaves unlike the service, and that decided the outcome: an ignored filter, a failing query, an unreadable field | `artifact` notes: "replica artifact", "ignores the … filter" |
| `harness` | Infrastructure decided the outcome: a timeout, a crashed sandbox, an error | `not_established` notes about timeouts or errors |
| `none` | Not a failure | outcomes `correct`, `correct_absent` |

A judge error is not an owner of the trial. It is scored separately, as the judge's disagreement with the owner above.

**Rulings that override an original label:**
- AT-AP-SLK-05-I13-I14 is `agent` (the PI's ruling: the bot counts as a member).
- G4-BOX-05 is a valid test (the PI: natural ambiguity).

## The development set

- **Sources:** every hand label in autogen_02 (Phases 1, 3 and 4) and fact_coverage_02's manual labels. OpenClaw's labels
  are reported apart, since they come from a different harness.
- **Owners:** assigned by rule from each label's outcome, and by reading each `artifact` or `not_established` note.
  The assignment is written to `devset.json` and committed before any evidence source is scored. Doubtful
  assignments are marked, so that the scores can be reported with and without them.

## The evidence, scored in this order (cheapest first)

1. **The judge's own `artifact` calls** (judge v2, where it ran). This is the baseline: how well the judge already
   separates "not the agent" from "the agent".
2. **The mechanical checks that already exist:**
   - the witness check on each test (does every near miss still fail exactly its fact on this test's seed?);
   - where feasible, the replica pre-checks of write feasibility and observability.
3. **A scan of the mock's traces:** the calls in the trajectory that hit a gap the replica notes list (ignored filters,
   failing queries, nested reads).
4. **The agent's stated objection,** read by an LLM (Muse), only if sources 1–3 leave a class uncovered.

**For each source and owner class,** the study reports:
- the recall of a "not the agent" flag;
- its false alarms on `agent`-owned failures;
- whether the reason it gives names the right component.

## What would change the conclusion

- **If the judge's `artifact` calls already reach high recall with few false alarms,** attribution belongs in the
  judge, with the other sources as checks.
- **If the judge's calls fail on test-wording or test-construction defects** while the mechanical and trace sources
  catch them, attribution belongs in a separate step after the judge that combines the evidence.
- **If no source catches the test-wording class,** that class stays a job for human review, and the report says so.

## Cost

- Sources 1–3 need no model calls.
- Source 4, if it runs, uses a few Muse calls (under $5 at list).
- No agent runs.

## Amendments

**2026-09-27 22:41 EDT, before any scoring (the development set as built):**
- **Two levels of ground truth.** Besides the trial's owner, each row carries its test's flaw, judged on the test
  and not on any outcome (the PI's rule "flawed is flawed"). A test is flawed if roadmap_01's `known_defects.json`
  advises leaving it out or fixing its seed, or if a label blames the test. G4-BOX-05 is valid by the PI's ruling.
  G4-LIN-02 was valid when it ran. Test-level sources such as the witness check are scored against this level.
- **`also` and `doubtful`.**
  - `also` names a second component that the note blames. A source that names it is credited with the right
    component.
  - `doubtful` marks five trials whose owner a reasonable reader could assign differently:
    - two timeouts under the old clock, which counted time spent waiting for Purdue;
    - a 40-turn limit, assigned to the agent;
    - two trials on G4-CAL-06, whose seed has a known confound.
- **Denominators are small outside `agent`** (distinct tests): test-wording 7, test-construction 10 (2 scenarios),
  mock 8 (5 mechanisms), harness 2. The report gives counts by distinct test as well as by trial, since one
  scenario (SLK-21) supplies 21 of the 30 test-construction trials.

**2026-09-27 22:59 EDT, after sources 1–3 were scored (owners unchanged):**
- **Verdict pairing.** Two Phase 3 labels describe a first attempt that the runner's retry later superseded
  (`autogen_02/eval/labels_phase3/attempts.json`). The development set now pairs them with v2's verdicts on that
  attempt (`judge2_phase3_attempt01`), and the trace scan reads that attempt. Before, both were paired with v2's
  verdicts on the retry (`incorrect`); now they are `not_established` and `correct_absent`. A field-by-field
  comparison against commit ca8ae46c6 confirms that no owner changed.
- **Source 3 is in-sample.** The gap list and the naive rule come from the replica notes alone. The counterfactual
  rule was refined by inspecting development-set failures:
  - the real-service check per gap;
  - own ids for changed rows (a parent folder id in the diff caused false flags);
  - items the final answer names, when nothing changed;
  - the first-appearance condition;
  - a failing query counts only when the test has a target and the agent concluded none;
  - a turn limit is the agent's own budget;
  - the singular `eventType` parameter.

  Its scores are therefore development-set scores, not a test.
- **Contested cases.** Evidence contests the owners of 10 trials. `contested.json` lists them with both readings,
  for the PI to rule on:
  - the ignored-filter cases, C1 and C2;
  - three "Linear has no documents" trials, C3.

  C3 was found by checking an override's facts: its reason said that the solver's prompt names no endpoints.
  The prompt in fact lists 19 Linear operations and none for documents or projects. The reason text is corrected;
  the committed owner stays for the primary scores.
