# Conceptual writer revision 4

This revision keeps the conceptual Markdown interface and four resolution-mode
fragments from v3. No seed, native schema, historical generated answer or manual
case diagnosis is supplied. `root_operations.json` injects only the current
referent's operation choices into its assignment; the shared capability brief
continues to qualify the conceptual model.

The procedural changes are:

1. Choose a supported downstream operation and answer before settling the story.
2. Express the route as a request and a short selection-conditions line.
3. Plan independently discriminating negatives before freezing free story choices.
4. Build distinct roots in a single shared environment; preserve shared facts.
5. Map each challenged condition to a negative, then recompute complete selection.
6. During reflection, report actual roots/alternatives, negative mapping and the
   specific capability used; change an unsuitable free story instead of preserving
   contradictory versions of the same record.

The multiple-mode fragment adds one longer-route worked example (User → Reaction
→ Message → Conversation). The other mode examples remain available only with
their respective mode. Underspecified alternatives should have distinguishable
consequences; a property requested as an answer must not become an eligibility test.

The main instructions shrink from 702 to 628 whitespace-separated words, and the
reflection instructions from 338 to 299. These counts exclude the capability brief,
mode fragments/examples, operation menu and conceptual model, all of which remain
part of the actual recorded requests.

## Run 6 lessons retained

The older `specops_envgen` writer was checked against commit `d650efd` ("run6 done").
Its writer prompt and absence/ambiguity fragments matched the inspected current
copies. Its saved run6 inputs prescribed conditions and decoy match/fail patterns;
authoring logs show the `--review-checks` workflow. In contrast, the new writer
chooses conditions along its assigned route and then builds their negatives.

We retain its distinct-referent/shared-witness discipline, concrete condition
realization, reverse reading of natural requests, agent-visible grounding,
consequential alternatives and credible near misses. We do not copy its fixed
three-condition limit, single focal decoy, YAML output, oracle-writing task or
assumption that a selected operation is necessarily supported by the current API.

This is a combined prompt intervention, not an ablation isolating one sentence.
All source prompts are development work; Sonnet writes the measured sketches.

## Fresh-world compiler

[compiler.md](compiler.md) consumes the final reflected Markdown sketch, its fixed
route/mode assignment, the [native contract](compiler_domain.md), schema, selector
syntax and documented APIs. The writer still receives no seed or physical schema.
The compiler builds a fresh environment with ordinary filler; it does not inherit
the benchmark seed or rewrite the request. The card and task specification are
assembled by code from fixed source labels, computed native bindings and minimal
compiler annotations. Computation/write annotations require semantic review.

Python checks keys, fields, row bindings, exact referent sets, intended counts and
all declared negatives against the entire seed. It freezes the first structurally
valid selector: later seed repairs cannot silently change it to pass. A structurally
valid selector can still misinterpret the source; the
[independent reviewer](compiler_review.md) checks that distinction. Only concrete
compilation defects receive bounded repairs (at most three compiler turns), each
as a continuation preserving the previous native responses. A source/selector
conflict is reported for separate review. Quality issues remain visible separately.

The current interface handles one focal obligation and one action per sketch;
underspecified rows represent singleton alternatives. It does not claim arbitrary
workflow or multi-obligation compilation. API access is a supplied domain contract,
not an extra model task. Optional native load/read checks exercise that contract
with Python and the real handlers, without a solver or LLM fallback.

From the repository root, using a fresh output directory for each command:

```sh
# Prepare inputs without any model calls.
python -m grounding.slack_campaign.concept_compile --case W01 --out /tmp/w01-input
# Compile, check, review and record all calls/costs.
python -m grounding.slack_campaign.concept_compile --case W01 --out /tmp/w01-run --run
# Separate native load/read check; requires the backend dependencies and local DB.
python -m grounding.slack_campaign.native_compile_check /tmp/w01-run/case.json \
  --out /tmp/w01-native --database-url postgresql://postgres@127.0.0.1:15432/agentdiff_campaign
```

Static compiler/reviewer context uses explicit prompt caching. The first W01
compiler prefix was 12,723 tokens: unlike the writer, compilation currently gets
all documented Slack signatures. This is a measured pilot, not a minimal-context
claim. Requests, responses, thinking summaries, repairs and native usage are saved.
The [pilot report](../../../../experiments/slack_campaign/compiler_pilot_01/review.md)
records the manual correction and does not count it as autonomous success.
