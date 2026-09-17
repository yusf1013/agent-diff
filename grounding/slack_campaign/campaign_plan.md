# Slack G1–G4 campaign, authorized 2026-09-17

The user authorized implementation and Git checkpoints after reviewing the five
sketches in design_review.md. That authorization supersedes that note's former
read-only status. The historical pilot is preserved in commit 1524d6d; it is not
the new generation workflow or a clean estimate of its yield.

## Frozen decisions

Use the 174 retained complete routes, separate identifying-attribute coverage,
28 entity/mode requirements, and representative capability limitations. Do not
multiply these dimensions. Keep 38 excluded routes and unavailable capabilities
visible in the catalog. Attempted/unrealized cases remain in denominators.

Reuse slack_bench_v2 for new cases. Prefer additions; allow explicit necessary
edits with reasons. Writer produces a short design; separate compiler binds it
to concrete records; reviewer checks ordinary-language validity, API access and
quality. Code assembles cards from design and bindings. Structured queries check
seed facts, not natural-language equivalence. Semantic review remains explicit.

Select conditions along the assigned path; negatives can violate different
conditions or bindings. No three-condition ceiling, no mandatory single focal
attribute, no generated easy controls. Preserve approved short prompts during
compilation. Open-ended discovery is preferred. If genuinely unavailable, record
any supplied candidate scope as an exception, preserving filterable results.

Native conversation continuation is mandatory for repairs. All attempts, usage,
provider thinking blocks when returned, prompts, outputs and failure reasons are
saved. Costs use recorded tokens and explicitly labeled historical price estimates.
Automated writer/compiler/reviewer/solver/evaluator calls use Bedrock Sonnet 5.
Codex design, debugging, manual audits and labels are manual work.

## Work sequence

1. Calibrate six fresh writer sketches across short/long paths and modes, inspect
   recurring defects, then compile/review/run them. Do not calibrate indefinitely.
2. Expand the fixed route inventory with balanced modes and supported attributes;
   review final cases and run eligible ones. Coverage credit follows validation,
   not assignments. Retain intermediate failures and review/repair costs.
3. Audit baseline cards/native assertion coverage (G1); evaluate original runs and
   manually confirm flagged native false passes (G2). Mutate suitable baseline
   requests under the same validity/quality standards, recording changed prompts
   separately from environment-only variants.
4. G4 alone uses existing ground-truth run labels. Compare current evaluator and
   direct judge on matched baseline evidence; report exact labels and detection
   precision/recall, uncertainty, exclusions and manual matching.
5. Report tables for all four goals, final validity and quality yields, scope
   exceptions, failures, coverage and costs. Keep development and measurement
   phases distinguishable. Poor or zero results are valid findings.

A route is not a prescribed tool-call path. Unsupported access is not absence.
Grounding failures are the primary bug signal; execution/applicability statuses
are descriptive and do not certify all downstream correctness.
