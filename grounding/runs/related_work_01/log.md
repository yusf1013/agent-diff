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
