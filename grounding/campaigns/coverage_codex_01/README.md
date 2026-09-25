# Coverage investigation — independent restart

> **Import note (2026-09-24).** This folder was copied unchanged from the `exp/coverage-codex` worktree; only this note
> was added. The investigation was not continued. [manual_findings.md](manual_findings.md) is cited by the
> [fact-coverage report](../../runs/fact_coverage_01/report.md). The status, worktree and to-do lines below describe
> the original worktree at the time.

Status: investigation in progress. No coverage recommendation is validated yet.

First result: [analysis of the accepted three-model manual run](manual_findings.md), with a [linked case matrix](manual_matrix.md) and [reproduction script](analyze_manual.py). This is prior-evidence analysis, not fresh validation.

The [minimal-cover probe](manual_cover_probe.json) finds exact seven-case covers of 26 simple occurrence requirements expressed by this candidate pool. Equally small complete covers range from 3 to 18 observed grounding-error episodes across the three models. This is a retrospective diagnostic of the criterion, not a recommended final suite. Reproduce with `python grounding/campaigns/coverage_codex_01/analyze_manual.py` followed by `python grounding/campaigns/coverage_codex_01/probe_manual_cover.py` from the worktree root.

The user asked for a defensible coverage definition and a way to construct compact, useful suites across Slack, Box, Calendar and Linear. A simple linear definition is acceptable. The intended practical scale is high tens to a few hundred executed cases per domain; a larger requirement inventory is acceptable if a compact suite covers it. Failure discoveries should connect to specific domain-model facts, not come primarily from repeating underspecified requests.

Worktree: `/home/yusf/PyProj/agent-diff-coverage-codex`, branch `exp/coverage-codex`, based on `de7b1212`. Main and other worktrees are not research output locations. No subagents. No commits without another user request.

## Sources and boundaries

- Adopted domain models, contextualizations, field accounting, and API qualifications under `grounding/domains/`. Do not change the models to make a coverage proposal work.
- The accepted manual 57-case Slack suite and its earlier Sonnet/Haiku/Qwen evidence are prior observations, not new validation.
- Exclude the Muse coverage campaign's proposals, cases, labels, findings and conclusions from this investigation. Reuse the already-integrated Qwen/runtime infrastructure as code, with checks.
- Keep the agreed grounding policy: unresolved selection without delegated choice is underspecified; a resolvable conjunction is resolved. An unfinished search does not by itself demonstrate incorrect grounding. No mandatory lookup trajectory.
- Researcher-authored cases and labels are manual. No automated test-generation claim is made.

## First candidates to compare

1. Linear occurrence coverage: a model fact appears in a selection condition.
2. Linear discrimination coverage: the fact is used and a concrete alternative witnesses the consequence of dropping/confusing it. Credits may accumulate within one natural request.
3. Add only specific interaction requirements justified by a counterexample to (2), if such counterexamples exist. Do not assume every path, role pair or resolution cross-product is required.

A model fact may be an identifying attribute, named relationship, state/classification, identity/scope distinction, or explicitly modeled derived representation. Storage aliases do not manufacture extra facts. Unavailable capabilities need separate, proportionate treatment. Resolution-mode checks are supplementary and do not multiply every structural requirement.

## Work to do

1. Define credit rules precisely and derive reproducible candidate counts from all four unchanged models. Account for exclusions and unresolved availability rather than declaring every stored field observable.
2. Map prior manual examples to candidate requirements, including correct runs. Identify which apparent redundancy is merely the same coarse verdict.
3. Construct an explicit case-to-requirement matrix and compare single-requirement tests with multi-credit tests. Distinguish an exact minimum within a fixed candidate pool from a global minimum over all possible natural requests.
4. Freeze small diagnostic experiments before execution. Check prompts, actual installed names/relationships, expected referents, decoy witnesses and API visibility. Use Qwen with the established settings and shared limiter; preserve all attempts.
5. Judge trajectory, response and final diff. Separate invalid cases, infrastructure failures, unestablished grounding, and demonstrated errors. Compare matched or meaningfully controlled alternatives; do not promote association to causal proof.
6. Challenge the candidate with new cases across the four domains. Report what the final coverage definition does and does not guarantee, achieved coverage, candidate-pool compactness, failure diversity, costs, and unresolved limitations.

Stop when the deliverables are concrete and supported, not when a desired failure percentage appears. If evidence is insufficient, say what is missing and keep working where progress remains possible.
