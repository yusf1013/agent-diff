# Brief: related work and the baseline question (session "related")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/related_work_01/`. No model runs
are needed; this is reading, searching and analysis. Web search and fetch are yours to use.

## The questions

1. What are the lines of work around testing and benchmarking tool-using agents, and how does each stack up
   against ours: where do we overlap, what do we do that they cannot, and can it serve as a baseline? If it can,
   how; if it cannot, why not. The PI's rule: anything a reviewer might take for a baseline at first glance must
   either be run as a baseline or be explained away, explicitly.
2. Which established test suites should we project onto our coverage space, and how? The model is our AgentDiff
   analysis: nearly all of its hand-written tests need at least one fact discrimination, and its assertions never
   check it. For a suite we adopt: how much of our space its tests cover; of the part they do not cover, how many
   failures our tests expose; of the part they do cover, how many failures their own assertions miss when the
   solver runs their tests; and whether our generation exposes more in the same space.
3. Where are the gaps in our own baselines: policy tests, several-match tests and capability boundaries have none.
   What would a fair baseline for each look like?

## Materials, in this order

- The PI's own account of the earlier baseline work, in the notes file's Appendix D (the MCP-Bench experience:
  contrived tasks on public data, an over-flagging judge, false positives such as New York versus Indianapolis time;
  the augmentation attempt with LLM-generated environment data) and section D.
- `~/PyProj/baseline_study/`: earlier coding-agent analyses of candidate baselines, mostly rejected for not being
  fully automated. Read the `.md` files first. Treat their claims as leads to verify, not facts.
- arXiv 2606.12191: a recent survey with a large literature study. Read the sections that map the field; use its
  bibliography.
- EnvScaler (github.com/RUC-NLPIR/EnvScaler): the environment-generation line (environments and trajectories for
  training or evaluation). The PI looked at one such work and found its checks thin.
- Our side: `grounding/runs/fact_coverage_01/criterion.md` (the coverage criterion), the concise report
  (`grounding/runs/report_01/report_concise.md`), the AgentDiff analysis (`grounding/campaigns/coverage_codex_01/`
  and `grounding/runs/fact_coverage_01/`), and `grounding/runs/baselines_01/report.md` (our current baselines and
  what they showed).

## Steps

1. Build the map: the angles (for a start: fully automated benchmark generation; semi-automated with manual parts;
   fully manual suites such as AppWorld; environment and trajectory generation; agent testing from software
   engineering, such as metamorphic or property-based testing of agents; judge and evaluation work). Expect other
   angles to appear; say which are new.
2. For each work that matters, a card: what it tests; domains and data; what is automated and what is manual; its
   oracle and how it was validated; its evidence; overlap with ours; verdict on baseline use with the reason.
3. Pick three to five established suites for the projection and check feasibility for each: are the tests and
   assertions public; do they touch our services or domains, or can our catalog be built for theirs; what the work
   would cost. Write the projection plan for the best candidate in enough detail that a session could run it.
4. Answer question 3 with concrete proposals.

## Deliverable

`grounding/runs/related_work_01/report.md`: status; the angle map; the cards; the baseline verdicts in one table;
the projection plan; the proposals for the missing baselines; a bibliography with links. Message the lead when the
map and cards exist, and at the end.
