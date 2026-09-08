# Box grounding-obligation measurements

This analysis covers all 48 Box entries (`box_116`–`box_163`, numbered 60–107) under [protocol v1](../GROUNDING_OBLIGATIONS_ONBOARDING.md). It measures benchmark requirements and assertion coverage, not agent behavior. Start with [the tables](report.md), then [cards](cards.md), [metrics](metrics.json), and the [partial-coverage review](coverage_audit.md).

## Evidence and conventions

The full test entries, referenced `box_default` seed and its file contents, local API extract, and listed official API documentation are the only evidence. [sources.json](sources.json) hashes all 131 referenced file contents as well as the entry, seed, and API extract. [source_map.md](source_map.md) documents accessible projections. Excluded: service/evaluator implementation, ORM/seeder defaults, live databases, solving-agent outputs as performance evidence, and the separate ER models.

The user explicitly confirmed that a requested root directory is a destination obligation. Its documented ID 0 makes the identifying rule trivial; it does not eliminate the subject. Root is counted only when requested, not added to every creation. A new hub/folder/file and reuse of its generated handle add no initial-state obligation.

Repeated uses of a file count once. A separately requested source collection or source file can coexist with an output-target obligation. Identity constrained on an existing file can count fully even when content preservation or other operation details are unchecked; this is not whole-task correctness. A source used only to derive another record's content requires coverage of that requested contribution, so partial source checks remain partial. Counts use the locked schema and all resolution states in the denominator; no additional fields were added to cards.

For `box_118`, the four eligible FOMC files form a choose-one population, consistent with Slack's permissive subjective-target rule. For `box_127`, investments descendants form a permissive file-count boundary, consistent with the asserted extrema in `box_137`; the direct-child interpretation is also noted. For `box_142`, the identical methodology reading in ethics supplies a defensible cross-folder duplicate target; the generic deletion assertion covers none of its identity.

## Source tensions and conditional cases

- `box_143`: only digital humanities becomes empty after moving the requested extensions. Five other category folders retain text files. The assertion requires all six folder removals. Its target constraint includes the intended folder, but its extra demanded removals are a task discrepancy; the card does not broaden the intended set to match them.
- `box_162`: no census filename contains population. Keep an absent choose-one subject rather than fabricating a match.
- `box_163`: Analysis_2026 is absent. The existence check is an obligation; the subsequently created folder is a new output. The Google PDF is 676600 seeded bytes, so standard_audit is the active branch.
- `box_155`: the economic CSV domain codes are BDCQ, CPIM, TPTA, one file each. No domain qualifies for the two-or-more-file hub-addition branch.
- Favorites membership is omitted from the seed. The named collection itself is resolved, but a runtime-empty membership default is not assumed. This limits establishing the conditional addition in `box_161`; it does not create an unknown assertion-coverage label.
- Two spelling-correction files have seed size/hash metadata inconsistent with their actual content. Selection in `box_139` uses names, not repaired metadata. See the [preflight](../REMAINING_DOMAINS_PREFLIGHT.md).

There are no pending assertion-specification questions for this pass. Missing expected-count fields are not treated as an explicit requirement to change every matching seeded record. Partial explanations identify the absent set/completeness constraint without asserting implementation behavior.

## Validation and maintenance

`analysis.json` is the maintained annotation source. The tables and cards carry the same per-obligation association and supporting fields as Slack. `config.json` supplies domain-specific sources, documented extra attributes, and API links; `build.py` uses the shared structural renderer in `../_analysis_support.py`.

```bash
python grounding/box_analysis/build.py
python grounding/box_analysis/build.py --check
```

Checks cover all 48 entries, locked keys, seed referent existence, declared attribute vocabulary, assertion indices, counts, and generated-file consistency. They are not semantic proofs or an independently protected checker. Separate seed inspection verified the 44761 transport lines, CPI/transport first rows, file-size extrema, remaining category-folder contents, obsolete task links, and quarterly treatment counts (23 + 17; annual total 80). The outcome review checks partial explanations against final content/state, never retrieval trajectories.
