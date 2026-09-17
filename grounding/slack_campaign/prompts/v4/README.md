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
