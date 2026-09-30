# related_work_01: cycle log

## 2026-09-30, cycle 0: orientation

**Read:** the brief and the shared rules; the PI's notes of 2026-09-29; the roadmap; the concise report; the
criterion (`fact_coverage_01/criterion.md`) and the FDC report's §§1–5, 8.3, 9; the AgentDiff obligation analysis
(`grounding/domains/{slack,box,linear}/analysis/`: 59 + 48 + 57 tests, 198 + 99 + 143 obligations) and the manual
57-case analysis (`campaigns/coverage_codex_01/manual_findings.md`); `baselines_01/report.md`; the headlines of
`several_match_auto_01` and `boundary_auto_01`; `~/PyProj/baseline_study/*.md` (July–August audits of 61 benchmarks
as generators for the PI's own MCP servers); the survey arXiv 2606.12191 (§4.5 tools, §5 environment synthesis, §5.3
quality control); the EnvScaler paper and README.

**Learned:**
- **The brief's pointer to the MCP-Bench account is wrong.** The notes file's Appendix C is the PI's second
  follow-up; it does not describe MCP-Bench. The substance is in the PI's own project, outside this repository:
  `~/PyProj/mcp-bench/specops_tests/audit/overall_report.md` (50 Gmail tasks at three environment levels; judge
  precision 0.83%, 2.42% and 10.16%; 18, 32 and 34 of 172 reference cells covered) and
  `~/PyProj/mcp-bench/logs/judge_robustness_2026-08-03/README.md` (the same Indianapolis time-zone error scored
  "critical error", "valid parameter" and "acceptable for fuzzy task" by three judge calls). Unpublished.
- **The July audit answered a different question.** Its legend (GENERATOR-SHIPPED, NO-GENERATOR, ...) asks whether a
  repository ships a runnable generator for the PI's own MCP servers. Our question is whether a work can be a
  baseline for fact-discrimination tests: a manual suite can be one (a status-quo row), and a shipped generator can
  be irrelevant (it tests tool selection, not which record). Its claims are leads; repositories have moved since.
- **The survey maps environments, not testing.** It has no line on software-engineering testing of agents
  (metamorphic, mutation, property-based, coverage criteria). Its quality dimensions for synthesized environments are
  correctness, diversity, complexity and fidelity; diversity is measured by embedding similarity or tool categories,
  never against a requirement space.
- **EnvScaler's checks** are LLM-written Boolean functions over the final state, one per checklist item that an LLM
  derived from an LLM-written "challenging task"; the reward is the fraction passed. Their validity evidence is that
  stronger models win more often on 50 sampled scenarios, and that Claude-4.5-Sonnet's quality scores of the
  environments (not of the checks) agree with manual judgments.

## 2026-09-30, cycle 1: what already exists for the AgentDiff projection

**Checked:** whether the repository already holds runs of an established suite with hand labels, before planning
any new run. It does, for Slack: `grounding/reference_labels/slack/` holds finalized hand labels (198 obligation
judgments) of the latest saved run of each of the 59 AgentDiff Slack tests (slack_57–115). The runs
(`grounding/runs/slack_baseline/`) are Claude Sonnet 5 via Bedrock, one trial per test, and keep AgentDiff's own
evaluation. [pilot/slack_assertion_misses.py](pilot/slack_assertion_misses.py) crosses the two with the obligation
analysis's assertion-coverage labels ([pilot/slack_assertion_misses.json](pilot/slack_assertion_misses.json)).

**Learned:**
- **13 of 59 tests have a demonstrated grounding error; the suite's own assertions pass 7 of those 13.** 9 of the
  18 incorrect obligations sit in runs the assertions passed.
- **The misses sit where the annotation said the assertions do not look:** of the 18 incorrect obligations, 10 are
  on obligations the assertions leave unchecked, 7 on partially checked ones, 1 on a fully checked one (slack_105
  O3, whose run the assertions failed). The annotation-level coverage labels predict the behavioural misses.
- **11 of the 18 are on obligations the annotation calls underspecified**, 7 on resolved ones. The established
  suite's failures come mostly from its own natural ambiguity, which our design puts in the policy tests.
- 6 tests fail their assertions with no grounding error; they are failures of another kind or false failures (not
  read yet).
- Denominators: one solver (Sonnet 5), one trial, grounding judgments only (not all task failures), Slack only.
  Box and Linear have obligation analyses but no labelled runs.

## 2026-09-30, cycle 2: the search, the map and the cards

**Searched:** the survey's bibliography (§4.5 tools, §5 synthesis); the PI's July audits as leads; arXiv and the web for
2026 work on wrong-entity actions, coverage criteria for agents, metamorphic and property-based testing of agents,
false-premise and infeasible requests, and automated state-based benchmark generation. Every cited arXiv entry was
checked through the arXiv API; the works that got Run, Project or Adopt were read in their papers (and EnvScaler in its
prompts, AgentDojo and ClawsBench in their repositories).

**Learned:**
- **Concurrent work names our failure class.** "Entity Binding Failures in Tool-Augmented Agents" (arXiv 2606.30531,
  2026-06-29, released): 60 hand-built single-step tasks with the state in the prompt; 24–26% wrong-entity actions at
  0% wrong-tool errors. Its per-condition results agree with ours: target-present look-alikes rarely bite (name
  collision 20%, near duplicate and document version 0%), true ambiguity almost always does (92–100%).
- **The paired should-act / should-abstain design exists** (AgentAbstain, 2607.10059, released): 263 pairs, one
  controlled perturbation each, 8 categories. Missing parameter ≈ our underspecified policy, insufficient tools ≈
  our "no operation" boundary. No presupposed-absence category, no identifying facts.
- **The semi-automated suites leave to people exactly what we automate.** Agent-Diff's own paper: LLMs write prompt,
  seed and assertions from uniformly sampled endpoints; people add ambiguity and distractor entities. AppWorld: hand-
  written setup programs add distractors per scenario.
- **The automated generators do not validate that a check rejects a wrong outcome.** ClawEnvKit (OpenClaw-native,
  so the generator a reviewer will name) grades calls and parameters from an audit log; MCP-Bench's judge is
  validated by a 3-point agreement rating (the PI measured ≤ 10% precision); EnvScaler's prompts ask for
  differentiated seeds, feasible and unambiguous tasks, and positive "Has …" checks only.
- **The credit rule has a direct ancestor:** Zhong, Yu and Klein's test-suite accuracy for text-to-SQL (EMNLP 2020)
  keeps the smallest set of databases that tells the gold query from every one-change neighbour.
- **Six new angles:** validity audits (ABC), language-to-query test adequacy, entity binding, abstention and
  feasibility, formal-specification-driven synthesis (MANTRA with SMT), failure diagnostics beyond selection.
- **ClawsBench is not released** (repository: trajectories and docs, "coming soon"); it would be a projection
  candidate (Slack, Calendar) on release.

## 2026-09-30, cycle 3: a pilot of the Agent-Diff projection, and the engine's closed world

**Checked:** whether Agent-Diff's released evaluation enforces the paper's closed-world invariant ("any other insertion,
deletion, or mutation is treated as a side effect and causes the task to fail"). It does not: `core.py`'s `evaluate`
returns `AssertionEngine(compiled_spec).evaluate(diff)`, and the engine's `strict` flag only limits which fields may
change on rows an assertion already matched. This repository's `assertion.py` is byte-identical to upstream `main`
(fetched 2026-09-30); nothing in `backend/src` or `sdk` checks unexplained changes. Consistent with the saved Sonnet 5
run of slack_67, which added a thumbs-up to the excluded pizza-combo message and passed 3 of 3 assertions.

**Ran:** [pilot/agentdiff_projection_pilot.py](pilot/agentdiff_projection_pilot.py) on 8 obligations of 6 Slack tests
(slack_67, 74, 87, 89, 104, 105), no model calls. Per obligation: the catalog facts its conditions use; the near
misses the shared seed holds for each fact (designated alternative, or plain), computed from the seed; and whether
the test's own assertions, compiled and run by the backend's engine, still pass when a near miss replaces the target
in a correct diff ([pilot/agentdiff_projection_pilot.json](pilot/agentdiff_projection_pilot.json)).

**Learned:**
- **All 8 correct diffs pass** (the harness is sound).
- **The seed holds a designated near miss for 3 of 8:** members who share an admin's first name (Morgan Stanley,
  Robert Chen; slack_89 O1), people who posted in #engineering without being members (slack_104 O2), and the thread's
  replies for its root (slack_105 O3). slack_87 uses the author role, but every member of the channels with a login
  or password post is also an author, so "posted" is never told from "is in the channel".
- **The assertions still pass with the near miss in 3 of 8:** naming the two same-first-name members (slack_89 O1),
  listing a non-member poster (slack_104 O2; "Member Count: 15" also passes, it contains "5"), and leaving out two of
  the four lunch questions (slack_67 O1, a several-match miss). slack_87's count catches a swapped invitee but not an
  extra one.
- **Two of the three designated near misses sit where the assertions are blind.** Where an assertion pins an id
  (slack_105's parent, slack_67's pizza message, the destination channels), a substitution fails.
- **Cost:** about 5 minutes an obligation by hand, with the obligation cards already written. Most of it is
  mechanical: the cards already name the columns and relationships an obligation identifies by.
