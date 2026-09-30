# Related work, baselines and the projection of established suites

*related_work_01, 2026-09-30. The question and the verdict vocabulary are in the [README](README.md), the cycles in
the [log](log.md), every work with its link in the [bibliography](bibliography.md). Numbers about other works are
theirs, from their papers or repositories, checked on 2026-09-30; numbers about ours are from the concise report
([report_concise.md](../report_01/report_concise.md)) unless a file is named.*

## Status

- **2026-09-30, done:** the map (12 angles, 6 of them new), 34 cards, the verdict table, two pilots on existing
  evidence (no model calls), the projection plan, the baseline proposals, the claims file ([claims.md](claims.md):
  every claim about another work, quoted from its source with the fetch date).
- **Running:** nothing. **Blocked:** nothing. Every arm proposed below waits for the PI's go-ahead.

## Summary

1. **The map.** Twelve lines of work touch ours; six are new beyond the brief (validity audits, test adequacy for
   language-to-query, entity binding, abstention and feasibility, formal-specification-driven synthesis, failure
   diagnostics). None defines tests against a model of the world the agent acts on or builds distractors for a stated
   fact and checks them mechanically; only the ARE verifier reports its oracle's accuracy against hand labels (450
   trajectories), and none reports it on wrong-record actions in particular.
2. **The closest work must be cited, and is not a baseline.** "Entity Binding Failures" (2026-06-29) names our
   failure class concurrently. It uses 60 hand-built single-step tasks with the state in the prompt. Its results
   agree with ours: target-present look-alikes rarely bite, unresolved ambiguity almost always does. AgentAbstain
   (2026-07) has our paired design (should-act versus should-abstain) at the request level.
3. **Baseline verdicts** (§3). **Run:** ClawEnvKit, the automated generator for OpenClaw-like agents a reviewer
   will name first; about $5–7 list and 144 trials (§4.5). **Project:** Agent-Diff first, then AgentDojo, WorkBench,
   τ²-bench and a sampled AppWorld. **Adopt:** the ARE verifier as the judge-design comparison, and ABC as the frame
   for the projection. **Explain away:** the rest, each with a reason class. MCP-Bench is explained away by the PI's
   own audit: judge precision 0.8–10%.
4. **The semi-automated suites leave to people what we automate.** Agent-Diff's authors add distractors and
   ambiguity by hand; AppWorld hand-writes them per scenario; the automated generators check solvability, not
   whether a check rejects a wrong outcome.
5. **The projection works, and the pilots show why it matters** (§4). On saved Sonnet 5 runs of Agent-Diff's 59
   Slack tests, its assertions pass **7 of the 13 tests with a hand-labelled wrong-record error**. On 8 obligations
   checked by hand, its seed holds a designated near miss for 3, and its assertions still pass with that near miss in
   place for 2 of those 3. The released engine has no closed-world check, so an extra write to a wrong record fails
   nothing. The full projection (all 224 tests, four measures) costs about 3–4 session-days of mapping, 672 trials on
   the self-host and about $8.5 list (§4.4).
6. **The missing baselines** (§5). One principle: the form's concept in plain words, the same inputs, nothing of the
   method. Three arms per form: the coding agent given the concept, a mechanical mutation of an existing suite, and a
   projection of the established items. Four of the arms need no LLM and could run first.

## 1. The angle map

The brief proposed six angles; six more appeared. "New" marks those.

| # | Angle | What its works do | Representative works | Where it meets ours |
|---|---|---|---|---|
| A | Hand-built stateful suites | People write every task, seed and check | AppWorld, τ-bench, AgentDojo, ToolSandbox, Gaia2, TheAgentCompany, MCPMark, Toolathlon | Same object (an agent acting on seeded state); hand-picked distractors at best |
| B | Semi-automated suites | An LLM or a template drafts; people curate | **Agent-Diff** (our platform), WorkBench, τ²-bench telecom, STAGE-Claw, BFCL | The curated part is exactly what we automate: distractors, ambiguity, check validity |
| C | Fully automated benchmark generation | Tasks (and sometimes fixtures and checks) generated from tool schemas | MCP-Bench, MCPToolBench++, TaskBench, MCPEval, ClawEnvKit, IntellAgent, AbstainGen | Same promise ("no manual effort"); no requirement space; oracles unvalidated or weak |
| D | Environment and trajectory synthesis | Environments, tasks and reward checks generated to train agents | EnvScaler, AgentScaler, AutoForge, ScaleEnv, LOGIGEN, APIGen-MT, ToolACE | Could supply a scenario generator; its checks are rewards, not tests |
| E | Agent testing from software engineering | Coverage criteria, fuzzing, metamorphic testing applied to agents | Skill Coverage, structural coverage of workflows, Prompt Coverage, ToolFuzz, CheckList | Our criterion belongs here; theirs cover the agent's own specification, ours the world it acts on |
| F | Judges and evaluation | LLM or agent judges, validated against people | ARE verifier, Agent-as-a-Judge, AgentRewardBench, Online-Mind2Web, false-success study | Our judge (309 of 310 blind labels) is one of these |
| G | **New:** benchmark-validity audits | Checklists and audits of existing benchmarks' tasks and checks | ABC, "Are solved issues solved?", HAL | Our projection is such an audit, with a check they lack |
| H | **New:** test adequacy for language-to-query | Data that tells a query from its one-change neighbours | Text-to-SQL distilled test suites, SQL mutation testing, XData, MC/DC | The lineage of our credit rule |
| I | **New:** entity binding in tool agents | "Right tool, wrong target" as a failure class | Entity Binding Failures (2026), AmbER | The same failure, named concurrently |
| J | **New:** abstention, clarification, feasibility | Requests the agent should question, refuse or report infeasible | When2Call, ToolBeHonest, NoisyToolBench, ACEBench-Special, AgentAbstain, FeasiGen, ToolEmu, Gaia2-Ambiguity | Precedents for our policy and boundary tests (§5) |
| K | **New:** formal-specification-driven synthesis | A symbolic model or solver validates generated checks | MANTRA (SMT), LOGIGEN, AutoWebWorld (FSM) | The PI's "requirements in B, decision coverage" presentation idea has precedents |
| L | **New:** failure diagnostics beyond selection | False success, fabrication after tool failure, skipped or ignored tool results | False success in τ²/AppWorld, fabrication after tool failure, ToolFailBench | The "other failures" of the PI's point C and RQ7 |

**What the angles share, and what none of them has.** Across the 34 works carded below, none defines its tests
against a model of the world the agent acts on, none builds its distractors from a stated alternative of a stated
fact and checks mechanically that each distractor fails exactly that fact, and none reports how its own checks do
against hand labels of wrong-record actions (the ARE verifier, validated on 450 hand-labelled trajectories of all
kinds, comes closest). The semi-automated suites leave the distractors and the ambiguity to
people (Agent-Diff: "adding distractor entities to the seed state" during human curation; AppWorld: hand-written
setup programs per scenario). The fully automated ones generate for solvability and difficulty, not for
discrimination (EnvScaler's seed prompt even asks for "differentiated content to avoid repetitive templates").

## 2. The cards

Each card: what it tests; how it is built (what is automated, what is manual); its oracle and how that oracle was
validated; its overlap with ours; the verdict. Verdicts use the README's vocabulary: **Run**, **Project**,
**Adopt**, **Explain away** (with a reason class).

### A. Hand-built stateful suites

**Agent-Diff** (Pysklo, Zhuravel, Watson, 2026; our platform) — semi-automated, carded here because it is the
status quo on our own services.
- *Tests:* 224 tasks on API replicas of Box (48), Slack (59), Linear (57) and Google Calendar (60); agents act by
  writing code against the real API surface.
- *Built:* endpoint multisets are sampled uniformly (108 endpoints); Claude Opus 4.5 and Gemini 3 Pro write the
  prompt, seed and assertions; people check executability and raise ambiguity by removing identifiers, adding typos
  or adding distractor entities. Its coverage notion is the API surface (endpoints, operation types, task horizon).
- *Oracle:* declarative assertions on the state diff. The paper adds a closed-world rule (any change no assertion
  explains fails the task), but the released engine does not implement it: it evaluates the assertions only, so an
  extra write that no assertion matches passes ([claims.md](claims.md), repository facts). No evidence is reported on
  whether the assertions tell a correct run from a wrong-record run.
- *Overlap:* the same services, replicas and harness contract. Our obligation analysis of 164 of its tests (Slack,
  Box, Linear; Calendar not yet done) found 440 identifying obligations; 160 of 164 tests have at least one; the
  assertions fully check 243, partly check 53 and leave 144 unchecked
  (`grounding/domains/{slack,box,linear}/analysis/metrics.json`). On saved Sonnet 5 runs of the 59 Slack tests,
  the suite's own assertions pass **7 of the 13 tests that have a hand-labelled wrong-record error**, and 17 of the
  18 wrong obligations are ones the assertions check partly or not at all ([pilot](pilot/slack_assertion_misses.json)).
- **Verdict: Project** (the status-quo row, the best candidate; plan in §4).

**AppWorld** (Trivedi et al., ACL 2024).
- *Tests:* 750 day-to-day tasks (250 scenarios × 3) over 9 simulated apps (457 APIs) for ~100 fictitious users;
  agents write code.
- *Built:* by hand. Each scenario has a hand-written generator whose setup program guarantees the task's
  presuppositions hold, adds "task-relevant distractors" and hurdles, and makes the scenario's 3 tasks a contrast set.
- *Oracle:* state-based assertions over the database diff, including checks for collateral damage; answer fields for
  the 15% that are questions.
- *Overlap:* the closest in spirit: its distractors are hand-designed near misses and its checks would catch a
  wrong-record write. It has no requirement space, its distractors are not tied to named facts, and by design it has
  no absence or underspecified tasks (every presupposition holds). The expensive part (distractors per scenario) is
  the part we automate.
- **Verdict: Project, as an optional sampled projection** (feasibility in §4): a reviewer will name it first, but a
  catalog for 9 apps and a harness bridge make it the costliest candidate.

**τ-bench and τ²-bench** (Yao et al., 2024; Barres et al., 2025).
- *Tests:* customer-service conversations (retail, airline; telecom in τ²) between an agent with policy documents and
  an LLM-simulated user.
- *Built:* tasks hand-written with gold action sequences; τ²-bench's telecom tasks come from a compositional
  generator over hand-written atomic subtasks.
- *Oracle:* the final database is compared with the one the gold actions produce, plus required outputs; pass^k over
  trials. ABC found that a do-nothing agent passes intentionally impossible airline tasks (e.g., changing a
  non-refundable ticket), because "no change" is the whole check: 38% of airline tasks.
- *Overlap:* records are identified (orders by what they contain), but tasks are organized around policies, not
  identifying facts; no designed near misses. Different domains.
- **Verdict: Project, as a lower-priority candidate**: public tasks and checks, strict oracle; low domain overlap.
  The ABC finding is also direct support for our rule that an absence or boundary test must check the reply, not
  only the absence of change.

**AgentDojo** (Debenedetti et al., NeurIPS 2024 Datasets and Benchmarks).
- *Tests:* 97 user tasks in four suites, with 629 prompt-injection cases; Workspace (email, calendar, cloud drive: 24
  tools, 40 user tasks) and Slack (11 tools, 21 user tasks) overlap with our services.
- *Built:* by hand; environments are small Python models loaded from YAML.
- *Oracle:* a deterministic Python `utility(model_output, pre_environment, post_environment)` per task; ground-truth
  call sequences.
- *Overlap:* Slack, calendar and drive; its checks are code we can read line by line.
- **Verdict: Project** (the best external candidate; §4).

**ToolSandbox** (Lu et al., 2024, Apple).
- *Tests:* stateful, conversational tool use on phone-style services (contacts, messaging, reminders, settings) with
  a user simulator; categories include State Dependency, Canonicalization and Insufficient Information.
- *Oracle:* human-authored **milestones** (must happen) and **minefields** (must not happen), matched over the
  trajectory and world-state snapshots.
- *Overlap:* minefields are the closest oracle concept to "must not act on the near miss"; Insufficient Information
  is a precedent for our absence and boundary tests. No overlap in services.
- **Verdict: Explain away** as a suite (different domain, no identifying-fact design); cited for §5.

**Gaia2 on ARE** (Froger et al., 2025, Meta).
- *Tests:* 800 human-annotated scenarios in 10 simulated phone "universes" (email, messaging, calendar, contacts,
  files, …; 101 tools each), in capability splits including **Ambiguity** (impossible, contradictory or multi-answer
  requests that should be clarified).
- *Oracle:* the ARE Verifier matches the agent's write actions to annotated oracle writes, argument by argument
  (exact or LLM-soft), with causality and timing; reads are not checked. On 450 hand-labelled trajectories:
  agreement 0.98, precision 0.99, recall 0.95, against 0.72, 0.53 and 0.83 for an in-context LLM judge. The
  annotation interface is not released.
- *Overlap:* partial (calendar, messaging, files); its Ambiguity split is a policy-test precedent.
- **Verdict: Adopt** (the judge design: a write-matching verifier validated against hand labels, the comparison for
  our triage plus judge v2); not a projection candidate (their universes, unreleased authoring).

**TheAgentCompany** (Xu et al., 2024).
- *Tests:* 175 professional tasks in a simulated software company with self-hosted GitLab, OwnCloud (files), Plane
  (issues, "an alternative to … Jira or Linear") and RocketChat ("an alternative to … Slack"), with simulated
  colleagues; checkpoint-based partial credit from per-task evaluators.
- *Overlap:* its services mirror ours in kind, but its tasks are long workflows where record identification is
  incidental.
- **Verdict: Explain away** (a different object: long-horizon job tasks; a heavy self-hosted stack; identifying facts
  appear only incidentally).

**MCP-era hand-built suites: MCP-Universe, MCPMark, Toolathlon** (2025).
- *Tests:* MCP-Universe, 6 domains on 11 real MCP servers (navigation, repositories, finance, 3D design, browser,
  search) with format, static and dynamic evaluators; MCPMark, 127 tasks by "domain experts and AI agents" on
  Notion, GitHub, filesystem, PostgreSQL and Playwright, each with a curated initial state and a verification
  script; Toolathlon, 108 tasks over 32 applications and 604 tools, with realistic initial states and
  execution-based checks.
- *Overlap:* state-verified, hand-written, long-horizon; Toolathlon touches Google Calendar, the others none of our
  services.
- **Verdict: Explain away** (different object: long-horizon orchestration on other services; per-task hand-written
  checks; no identifying-fact design).

**Claw-Eval** (Ye et al., 2026) and **ClawsBench** (Li et al., 2026).
- Claw-Eval: 300 human-verified tasks, rubric LLM judge plus rule graders, toy-to-mid mocks (the PI's July audit:
  Gmail list/get/send/draft only, Calendar without recurrence or editing). ClawsBench: five high-fidelity mocks
  (Gmail, Slack, Calendar, Docs, Drive) validated against real request–response pairs, 44 tasks.
- **Verdict: Explain away**: Claw-Eval's automated successor (ClawEnvKit) is carded below; ClawsBench is **not
  released** (its repository holds trajectories and docs only, "coming soon", checked 2026-09-30). ClawsBench would
  be a strong projection candidate on release: it overlaps Slack and Calendar.

### B. Semi-automated suites

**WorkBench** (Styles et al., 2024).
- *Tests:* 690 workplace tasks over five sandbox databases (calendar with 300 events, email, web analytics, CRM,
  project management) and 26 tools.
- *Built:* 69 hand-written task templates, 10 programmatic instances each, over randomly generated data.
- *Oracle:* "outcome-centric": every database after the run is compared with the expected state, so side effects
  fail.
- *Overlap:* calendar and project management; templates such as "the next meeting with X" identify records by
  conditions, but near misses exist only by chance in random data.
- **Verdict: Project, as a candidate** (public, strict oracle, small schema; §4).

**STAGE-Claw** (Liang et al., 2026).
- *Tests:* 40 personal-assistant tasks in a real personal-computing environment (files, browser, terminal, calendar,
  email, reminders, notes), scored by the final system state.
- *Built:* people give task hints; an LLM explores, builds the task, its environment, ground truth and verifier;
  automated checks for structure, reproducibility, verifiability and difficulty, with repair; a human audit.
- *Oracle:* per-task executable verifiers aligned with the hidden ground truth; no test against wrong end states is
  reported.
- **Verdict: Explain away** (no requirement space; its generator is an LLM authoring loop with review, which our
  twins N0M and N1M already measure on our services: 0 facts exposed).

**BFCL** (Patil et al., ICML 2025). Expert-curated and user-contributed function-calling tests; its multi-turn
categories add missing parameters, missing functions and long context, checked against state and response.
**Verdict: Explain away** as a suite (call-level, its own simulated backends); cited in §5 as a precedent for policy
and boundary items.

### C. Fully automated benchmark generation

**MCP-Bench** (Wang et al., 2025, Accenture).
- *Tests:* 104 tasks on 28 live MCP servers (250 tools) in public-data domains (finance, travel, science, academic
  search).
- *Built:* o4-mini synthesizes tasks from tool dependency chains; a quality filter keeps solvability ≥ 9/10 and
  utility ≥ 5/10; tasks are rewritten as "fuzzy" instructions; people inspect them.
- *Oracle:* rule checks (tool validity, schema, runtime success, dependency order) plus a rubric LLM judge with prompt
  shuffling and score averaging; validated only by a 3-point human agreement rating of its dimension scores.
- *The PI's own audit* (unpublished; `~/PyProj/mcp-bench/specops_tests/audit/overall_report.md`): 50 MCP-Bench Gmail
  tasks run against LLM-generated environments at three levels. The judge's precision was **0.83%** (empty mailbox:
  5 true positives against 601 false), **2.42%** (random: 14 against 565) and **10.16%** (representative: 51 against
  451), after the PI removed duplicate allegations and complaints about calls not run in parallel. At the
  representative level its false positives were procedure complaints with no outcome difference (245), prompt
  overreads (142), its own hallucinated facts (36), missing dependencies (23) and no qualifying target (5). The same
  Indianapolis-versus-New-York time-zone choice was scored "critical error", "valid parameter" and "acceptable" in
  three judge calls
  (`~/PyProj/mcp-bench/logs/judge_robustness_2026-08-03/README.md`). These are judge errors, not agent failures.
- **Verdict: Explain away** (no seeded state by design; an oracle that cannot tell a correct outcome from a wrong one,
  measured by the PI at ≤ 10% precision even with representative environments).

**MCPToolBench++** (Fan et al., 2025) and **TaskBench** (Shen et al., NeurIPS 2024). Generators that take tool
schemas (or a tool graph) and emit requests with a ground-truth call (or call graph); graded on tool and parameter
match (TaskBench statically, without execution). **Verdict: Explain away** (no seeded state; the oracle checks the
call's shape, never which record the call acted on).

**MCPEval** (Liu et al., 2025, Salesforce). A frontier LLM generates tasks from MCP tools; a frontier agent executes
them, and its successful trajectory becomes the ground truth; agents are graded on tool-call match plus an LLM
judge. **Verdict: Explain away** (the oracle is a model's own trajectory, the "same model" risk of the PI's point 6;
no seeded state designed to discriminate).

**LiveMCPBench** (Mo et al., 2025). 95 tasks over 70 MCP servers, graded by an LLM judge; about tool retrieval at
scale. **Verdict: Explain away** (a different object: finding tools, not records).

**ClawEnvKit and Auto-ClawEval** (Li et al., 2026, with Stoica).
- *Tests:* 1,040 generated environments in 24 categories for "claw-like" agents; it supports OpenClaw natively (a
  tool plugin) and 8 harnesses.
- *Built:* a parser, a generator (task specification, tool interface, scoring configuration, fixtures) and a
  validator (format, coverage, and feasibility by one LLM call); new services can be registered.
- *Oracle:* 15 check types over the server-side audit log (what was called, with which parameters), the agent's
  output, files, and an LLM rubric. Quality evidence: structural validity and LLM-judged coherence and clarity
  against the human-curated Claw-Eval. The PI's August audit found that its API checks test calls and parameters but
  not responses or final state (a call that failed with status 500 scored completion 1.0), that robustness is free
  credit, and that a generated rubric can reward a wrong answer (`calendar-028`).
- *Overlap:* the same promise (tasks, fixtures and checks with no manual effort) on the same kind of agent.
- **Verdict: Run** (the generator a reviewer will name first for OpenClaw; plan and prediction in the verdict table
  and §4.5).

**IntellAgent** (Levi and Kadar, 2025). Extracts the policies from a chatbot's system prompt into a policy graph,
samples combinations, generates an event (a request plus a database state) for each, simulates the conversation,
and grades with an LLM critique; its validity evidence is that model rankings correlate with τ-bench's.
**Verdict: Run, optional, as a policy-test baseline** (§5): it is the one released generator whose requirements are
policies, which fits "everything is a policy" (the PI's view 1).

**AgentAbstain and AbstainGen** (Liu et al., 2026, UIUC).
- *Tests:* 263 pairs of should-act and should-abstain tasks in 42 MCP sandboxes; each pair differs by one controlled
  perturbation of the instruction, the tools or the state. Eight categories: missing parameter, ambiguous action,
  conflicting constraints, high stakes, insufficient tools (before execution); tool failure, conflicting evidence,
  emergent risk (at run time).
- *Built:* AbstainGen synthesizes sandboxes and pairs end to end; validated by deterministic replay and LLM judges;
  three annotators rate 94–98% of sampled tasks well designed. Best paired accuracy 59.5% over 17 models.
- *Overlap:* its paired design is our derivation of policy variants from a cover; "missing parameter" is our
  underspecified policy, "insufficient tools" our boundary class "no operation". It has no presupposed-absence
  category and no identifying facts.
- **Verdict: Project** its categories onto our policy and boundary spaces (§5); **explain away** as a generator on our
  services (it synthesizes its own sandboxes).

**FeasiGen** (Cheng et al., 2026). Makes solvable tasks infeasible by masking the tools that all successful traces
used; over 94% of its infeasibility labels hold under human check; agents continue on infeasible tasks up to 73.9% of
the time. **Verdict: Run, as a mechanical boundary baseline** (§5): masking an operation is cheap on our replicas.

### D. Environment and trajectory synthesis

**EnvScaler** (Song et al., 2026).
- *Built:* SkelBuilder mines environment topics and writes a Python class of state, tools and rules, checked by a
  dual-agent loop; ScenGenerator has an LLM write an initial state, then a "challenging" task, then a checklist of
  "Has …" items, then one Boolean function per item over the final state. The reward is the fraction passed.
  191 environments, about 7,000 scenarios, used to train Qwen3 models (gains on BFCL-MT, τ-bench, ACEBench-Agent).
- *From its prompts* (`scen_generator/`, read 2026-09-30): the state prompt asks for "differentiated content to avoid
  repetitive templates"; the task prompt requires the task to be feasible from the state ("you cannot delete a file
  that does not exist") and unambiguous; the check prompt verifies positive "Has …" items and, for non-fixed values,
  only that a field exists. Nothing checks that other records were left alone.
- *Validity evidence:* stronger models win more often on 50 sampled scenarios; Claude-4.5-Sonnet's quality scores of
  the environments (not of the checks) agree with manual judgments.
- **Verdict: Explain away** (a training reward, not a test: its prompts steer seeds away from look-alikes and
  exclude absent or ambiguous requests, and its checks cannot see a wrong-record write next to the right one). Running its ScenGenerator on our
  services would reduce to N0 with a difficulty instruction; the prediction is N0's result (0 facts exposed).

**AgentScaler, AutoForge, ScaleEnv, LOGIGEN** (2025, 2025, 2026, 2026). Scaled tool environments for
agent RL. AgentScaler and AutoForge synthesize tasks by walking tool-call sequences and reversing them (as EnvScaler's
authors describe them); ScaleEnv tests generated tools procedurally and expands tool dependency graphs; LOGIGEN
compiles policies into SQLite-backed environments and verifies final states deterministically. **Verdict: Explain
away** (training data; tasks derived from tool sequences have no notion of what a request must discriminate).

**APIGen and APIGen-MT; ToolACE; TaskCraft; AgentSynth; AutoEnv** (2024–2025). Verified function-calling or agent
trajectory data (format, execution and semantic checks; LLM review committees), difficulty-scaled task synthesis, and
generated game-like worlds. **Verdict: Explain away** (training data or worlds without API semantics; verification
targets solvability and correctness of the gold trajectory).

The survey arXiv 2606.12191 (§5.3) sums up this line's quality control as correctness, diversity, complexity and
fidelity. Its account of correctness lists executability, solvability (gold tool sequences reaching the target state)
and verifiers' agreement with task completion; diversity is measured by embedding similarity or tool categories. It
lists no check that builds a plausible wrong outcome and confirms the verifier rejects it, and no coverage measured
against a requirement space.

### E. Agent testing from software engineering

**Skill Coverage** (Tan, Huang, Sun, 2026), **structural coverage of agentic workflows** (Kahani and Bagherzadeh,
2026), **Prompt Coverage Adequacy** (Tambon et al., 2026). Test-adequacy criteria over the agent's own specification:
behaviour constraints extracted from a skill's instructions (leaderboard trajectories cover 38.66–45.51% of them);
the typed coordination graph of agents, tools, access rules and delegation; the requirements stated in a prompt.
**Verdict: Explain away** (a different object: the adequacy of tests against what the developer wrote; ours is
adequacy against the world the agent acts on). These are the line our criterion belongs to; the second says itself
that structural coverage "does not replace semantic or end-to-end evaluation", the PI's point 7.

**ToolFuzz** (Milev et al., 2025). Fuzzes queries to find under-, over- or ill-specified tool documentation.
**Verdict: Explain away** (object: the tool documentation).

**Metamorphic testing of LLMs and agents** (survey, Zheng et al., 2026) and **REST API testers** (for example ARMeta,
2026). Metamorphic relations over conversations, actions and trajectories; LLM agents that write metamorphic tests
for REST APIs. **Verdict: Explain away** (the testers target the service, the PI's point 1; metamorphic relations
compare runs without an expected outcome, while each of our tests has one).

**CheckList** (Ribeiro et al., ACL 2020). Behavioural testing of NLP models: a matrix of capabilities by test type
(minimum functionality, invariance, directional), with templates. **Verdict: Explain away** (no environment or
action), cited as the precursor of requirement-driven behavioural testing.

### F. Judges and evaluation

**ARE verifier**: see Gaia2 (**Adopt**). **Agent-as-a-Judge** (Zhuge et al., 2024): an agentic judge for code
generation, "as reliable as our human evaluation baseline" on 55 tasks with 365 requirements. **AgentRewardBench**
(Lù et al., 2025): 12 LLM judges against expert review of 1,302 web trajectories; no judge excels everywhere, and
rule-based checks under-report success. **Online-Mind2Web** (Xue et al., 2025): an LLM judge built after finding
earlier results over-optimistic. **False success** (Advani, 2026): 45–48% of failures in single-control τ²-bench
domains are claims of completion the state contradicts; no LLM judge configuration exceeds AUROC 0.65 there.
**Verdict: Explain away** as baselines (other domains; our J0 and J1 already stand for the naive judge), cited for
the judge section; the false-success study supports checking the state rather than the agent's claim.

### G. Benchmark-validity audits (new)

**ABC, the Agentic Benchmark Checklist** (Zhu et al., 2025). Task validity and outcome validity checks; applied to 10
benchmarks, it found outcome-validity flaws in 7 and task-validity issues in 7 (τ-bench's do-nothing agent; too few
SWE-bench-Verified tests; WebArena overestimating by 5.2%). Its state-matching checks ask that the ground truth include
all acceptable end states, check relevant and irrelevant state, and resist trivial modification; its fuzzing check
asks that "inputs must affect the output". **Verdict: Adopt as framing.** Our projection is an ABC-style audit
with one check ABC lacks: *does the environment hold, for each identifying condition, a record that fails only that
condition, and do the checks tell the target from it?* **"Are solved issues really solved?"** (Wang, Pradel, Liu,
2025): patches that pass SWE-bench's tests yet are wrong, the coding analogue of assertions that pass a wrong-record
run. **HAL** and **AI Agents That Matter** (Kapoor et al.): evaluation-practice critiques. Cited.

### H. Test adequacy for language-to-query (new)

**Test-suite accuracy for text-to-SQL** (Zhong, Yu, Klein, EMNLP 2020). Builds "neighbor queries" by changing one
aspect of the gold query, then keeps the smallest set of databases on which every neighbour's result differs from
the gold's. This is our credit rule (a near miss that the mutated reference query selects and the intended one does
not) and our near-minimal cover, one level down: they test a query the system wrote, we test an agent whose query is
implicit in what it reads and does, so the databases become seeds of a live service, the neighbours come from a
domain model's designated alternatives instead of syntactic edits, and each test must remain a natural request.
**SQL mutation testing** (Tuya et al., 2007) and **XData** (Chandra et al., 2015), which generates data that kills
query mutants and grades student SQL with it, and **MC/DC** (Chilenski and Miller, 1994) complete the lineage our
criterion already cites (FDC report §4.5). **Dr.Spider** (Chang et al., 2023): perturbations of databases, questions
and SQL for robustness. **Verdict: Explain away** as baselines (they test a query, not an agent); cited as ancestry.

### I. Entity binding in tool agents (new)

**Entity Binding Failures in Tool-Augmented Agents** (Babu and Indukuri, 2026-06-29; released). The same failure
class, named concurrently: "the agent may choose the right tool and still act on the wrong external entity".
- *Tests:* 60 hand-built diagnostic tasks over email, calendar, documents, customer records and issue tracking;
  conditions: unambiguous, name collision, document version, temporal, account collision, near duplicate,
  cross-system, true ambiguity.
- *Setup:* a single tool-call decision with the entity state in the prompt; no exploration of a live service.
- *Findings:* 0.0% wrong-tool errors, 24–26% wrong-entity actions for action-oriented methods, concentrated in
  temporal tasks (90–100%) and true ambiguity (92–100%); name collisions and cross-system references 20%; document
  version, account collision and near duplicate 0%.
- *Overlap:* the problem statement is ours. Its findings agree with ours: look-alikes placed next to the right record
  rarely bite (our covers: 12 of 100 expose), while unresolved ambiguity almost always does (our underspecified
  policy cells). What it lacks: a requirement space (its eight conditions are chosen, not derived), near misses
  checked against a stated fact, an agent that must find the evidence itself, an absence (presupposition) condition,
  and a validated oracle beyond id matching.
- **Verdict: Project its taxonomy onto our kinds and families** (a paper-level mapping; §4); **explain away** as a
  baseline suite (single-step decisions with the state given; 60 tasks; not our services). It must be cited.

**AmbER** (Chen et al., 2021): sets of entities sharing a name, to test entity disambiguation in retrievers; the NLP
precursor of our F8 (partial identity) and same-name pairs. Cited.

### J. Abstention, clarification and feasibility (new)

**When2Call** (NVIDIA, 2025): call a tool, ask a follow-up, or say it cannot be done (multiple choice).
**ToolBeHonest** (2024): 700 samples on missing necessary tools, potential tools and limited functionality.
**NoisyToolBench** ("Learning to Ask", 2024): instructions with missing or wrong arguments. **ACEBench Special**
(2025): ambiguous or incomplete instructions. **ToolSandbox Insufficient Information**, **BFCL missing
parameters and functions**, **Gaia2 Ambiguity**, **UserBench** (goals revealed only on asking), **ToolEmu** (144
test cases with underspecified instructions in an LM-emulated sandbox; 68.8% of its flagged failures held up under
human review), and **AgentAbstain** and **FeasiGen** (above). **Verdict: Project, for §5**: they test request-level
gaps (a missing argument, a missing tool, an ambiguous action), mostly in single-turn or emulated settings; none
derives the gap from a fact of a seeded environment, and none of their category lists names a presupposed-absence
condition (the requested record does not exist).

### K. Formal-specification-driven synthesis (new)

**MANTRA** (Anand et al., 2026, MPI-SWS): from a procedural manual and tool schemas, it generates a symbolic world
model and trace-level compliance checks separately, validates their consistency with an SMT solver, and repairs
inconsistencies; 285 tasks in 6 domains. **LOGIGEN** (above) compiles policies into the environment. **AutoWebWorld**
(2026) synthesizes verifiable web environments from finite-state machines. **Verdict: Explain away** (they formalize
procedures, what must happen in what order; we formalize the world's identifying facts, which record). Cited for the
PI's presentation idea (requirements in a formal notation, probes as decision coverage): MANTRA is the precedent for
validating generated checks against a formal model, as our fdc check does by running both queries on the seed.

### L. Failure diagnostics beyond selection (new)

**False success** (above), **fabrication after tool failure** (Sethi et al., 2026: 14.1% of responses assert a value
the failed tool never returned, or cite an invented policy), **ToolFailBench** (Soni, 2026: tool skipped, result
ignored, output fabricated, tool used needlessly), **progress reporting** (Wang et al., 2026). **Verdict: Explain
away** as baselines; they are the literature for the PI's point C (misreporting, hallucination) and RQ7, and for the
values session.

## 3. Baseline verdicts

One row per work. Reason classes for Explain away: **object** (a different object under test), **state** (no
seeded state), **oracle** (an oracle that cannot observe which record), **released** (not released), **training** (a
training reward, not test adequacy).

| Work | Angle | Verdict | Reason or plan |
|---|---|---|---|
| Agent-Diff | A/B | **Project** | Status-quo row on our services; §4 |
| AgentDojo (Slack, Workspace) | A | **Project** | Best external candidate; public tasks and Python checks; §4 |
| WorkBench | B | **Project** (candidate) | Calendar and project management; strict DB oracle; §4 |
| τ-bench, τ²-bench | A | **Project** (lower priority) | Public, strict oracle, other domains; §4 |
| AppWorld | A | **Project** (optional, sampled) | The manual gold standard; costliest; §4 |
| Entity Binding Failures | I | **Project** (taxonomy) | Map its 8 conditions onto our kinds and families; cite as concurrent |
| AgentAbstain | C/J | **Project** (categories) | Onto policy and boundary spaces; §5 |
| ClawEnvKit / Auto-ClawEval | C | **Run** | The automated generator for OpenClaw a reviewer will name; §4.5 |
| IntellAgent | C | **Run** (optional) | Policy-test baseline; §5 |
| FeasiGen | C/J | **Run** (mechanical) | Boundary baseline by masking operations; §5 |
| Gaia2 / ARE verifier | A/F | **Adopt** | Judge-design comparison (validated write matching) |
| ABC | G | **Adopt** (framing) | Our projection as an ABC-style audit with a grounding check |
| MCP-Bench | C | Explain away: **state, oracle** | Public-data design; PI's audit: judge precision ≤ 10% |
| MCPToolBench++, TaskBench | C | Explain away: **state, oracle** | Grade the call's shape, not the record |
| MCPEval | C | Explain away: **oracle** | Ground truth is a model's own trajectory |
| LiveMCPBench | C | Explain away: **object** | Tool retrieval at scale |
| STAGE-Claw | B | Explain away: **object** | LLM authoring loop, already measured by N0M/N1M |
| EnvScaler | D | Explain away: **training, oracle** | Prompts ask for differentiated records and feasible, unambiguous tasks; checks positive only |
| AgentScaler, AutoForge, ScaleEnv, LOGIGEN | D | Explain away: **training** | Tasks from tool sequences; no discrimination notion |
| APIGen(-MT), ToolACE, TaskCraft, AgentSynth, AutoEnv | D | Explain away: **training** | Verified trajectories or worlds, not tests |
| TheAgentCompany | A | Explain away: **object** | Long-horizon job tasks; identification incidental |
| MCP-Universe, MCPMark, Toolathlon | A | Explain away: **object** | Orchestration on other services |
| Claw-Eval | A | Explain away: **object** | Toy mocks; rubric judge; automated successor carded |
| ClawsBench | A | Explain away: **released** | Mocks and tasks not released; project on release |
| ToolSandbox, BFCL | A/B | Explain away: **object** | Phone or call-level domains; cited in §5 |
| Skill / structural / prompt coverage | E | Explain away: **object** | Adequacy against the agent's specification |
| ToolFuzz, REST testers, metamorphic testing | E | Explain away: **object** | Test tools, services or relations |
| CheckList | E | Explain away: **object** | NLP behaviour, no environment; cited |
| Text-to-SQL test suites, SQL mutation, XData, MC/DC | H | Explain away: **object** | Test queries, not agents; the credit rule's ancestry |
| Agent-as-a-Judge, AgentRewardBench, Online-Mind2Web | F | Explain away: **object** | Judges for other domains; J0/J1 stand in |
| When2Call, ToolBeHonest, NoisyToolBench, ACEBench, UserBench, ToolEmu | J | **Project** (categories) | Request-level gaps, not our services; projected onto the policy and boundary spaces in §5 |
| MANTRA, AutoWebWorld | K | Explain away: **object** | Procedural compliance; cited for the formal presentation |
| False success, fabrication, ToolFailBench | L | Explain away: **object** | Other failures (point C, RQ7) |

## 4. Projecting established suites onto our coverage space

### 4.1 The four measures

The PI's four questions, made operational for a suite S and our catalog (255 facts, 213 servable):

| Question | Measure | Needs agent runs? |
|---|---|---|
| (a) How much of our space do S's tests cover? | Per servable fact: **covered** (some test uses it, its seed holds a near miss through the fact's designated alternative, and the test is fact-sensitive), **covered through F0 only** (the near miss is a plain difference), **occurs only** (used, no near miss), **absent**. Counts per service and kind | No |
| (b) Of the part they do not cover, how many failures do our tests expose? | Our facts exposed at detect@1 and detect@3 (existing OpenClaw results), restricted to the facts S does not cover | No |
| (c) Of the part they cover, how many failures do their assertions miss? | Two layers. **Oracle audit:** for each (test, fact, near miss), put the near miss in the target's place in a correct diff and run S's own engine; the oracle is **blind** to that fact if the assertions still pass. **Runs:** S's tests on OpenClaw, k = 3; wrong-record failures (our judge with S's referents as the answer key, checked on a blind sample) whose runs S's assertions pass | Only the second layer |
| (d) In the same space, does our generation expose more? | For the facts S covers: facts exposed by S's tests against facts exposed by ours, detect@1 and @3, per covered fact and per test | Uses (c)'s runs |

**What "covered" means for a test that carries several facts.** Credit is per (test, fact), as in our own covers:
a test covers fact f when one of its obligations identifies its referent with a condition that uses f, the test's seed
holds a record that the obligation's reference query selects once f's condition is replaced by its designated
alternative (and does not select otherwise), and the obligation is fact-sensitive (its target is present, or the
request permits "there is none"). A test with four facts can cover four; a fact counts once for the suite, whichever
test covers it. Underspecified obligations earn no fact credit; they map to the policy space instead (the fact whose
missing condition leaves the choice open). Near misses must be distinct per fact within an obligation, as fdc.py
already requires.

### 4.2 The pilot on existing evidence

Two pilots, no model calls ([log](log.md), cycles 1 and 3):

- **Behaviour** ([slack_assertion_misses.py](pilot/slack_assertion_misses.py)): saved Sonnet 5 runs of all 59 Slack
  tests, one trial each, with finalized hand labels. 13 tests have a wrong-record error; **the suite's own assertions
  pass 7 of the 13**. Of the 18 wrong obligations, 10 are ones the assertions leave unchecked, 7 partly checked, 1
  fully checked (and that run failed its assertions). 11 of the 18 are on obligations the annotation calls
  underspecified.
- **Coverage and the oracle** ([agentdiff_projection_pilot.py](pilot/agentdiff_projection_pilot.py)): 8 obligations of
  6 Slack tests, the method of §4.1 by hand.

| Test, obligation | Request | Designated near miss in the seed | Assertions pass with it in place |
|---|---|---|---|
| slack_89 O1 | the workspace's admins, by name | members sharing an admin's first name (Morgan Stanley, Robert Chen) | **yes** |
| slack_104 O2 | who is in #engineering, count and names | people who posted there without being members | **yes** (a count of 15 also passes: it contains "5") |
| slack_105 O3 | the thread's root message | the thread's two replies | no (the parent is pinned) |
| slack_87 O1 | everyone who posted about login or password | none: every member of those channels is also an author | no, but an extra invitee passes |
| slack_67 O1 | all lunch questions in #random | none (plain only) | **yes** when two of the four are left out |
| slack_67 O2 | the pizza-combo message | none (plain only) | no (the message is pinned) |
| slack_74 O2, slack_89 O2 | #general, #random | plain only | no (the channel is pinned) |

Designated near misses exist for 3 of the 8; **the assertions are blind to 2 of those 3**. Where an assertion pins an
id, a substitution fails; where it matches a substring of a reply, it passes. The pilot also showed that the released
engine has no closed-world check: an extra write that no assertion matches does not fail a test (log, cycle 3).

### 4.3 Feasibility of five suites

| Suite | Tests and checks public | Overlap with our services | Our catalog for it | Can OpenClaw drive it | Its oracle | Rank |
|---|---|---|---|---|---|---|
| **Agent-Diff** | yes (repository, Hugging Face) | all four | exists (255 facts) | yes, today | state-diff assertions; no closed world in the engine | **1** |
| **AgentDojo** (Slack 21 + Workspace 40 user tasks) | yes (Python) | Slack; calendar, drive (≈ Box), email | to build: small Python models, about 40–60 facts, a day | a bridge: serve its tool functions over HTTP and write one skill, like our curl wrapper; a day or two | deterministic Python over pre and post environment | **2** |
| **WorkBench** (690 tasks from 69 templates) | yes | calendar, project management | to build: five tables, a day | the same kind of bridge | every database compared with the expected one | **3** |
| **τ²-bench** (retail, airline, telecom) | yes | none | to build: small databases | a bridge plus its LLM user simulator (a second model per run) | final database against the gold actions' | **4** |
| **AppWorld** (750 tasks, 9 apps) | yes (encrypted bundle, decryptable) | partial (files, messaging) | large (457 APIs): sample 30–50 tasks, catalog only the entities they touch | through its MCP server | state assertions with collateral-damage checks | **5**, optional |

Durations in the table are estimates, not measurements. Considered and not ranked: ClawsBench (not released), Entity Binding Failures (single-step, state in the prompt: its
taxonomy is projected on paper, below), Gaia2 (annotation interface unreleased; its universes are its own),
ToolSandbox (phone services).

**Projecting the Entity Binding Failures taxonomy** (paper-level, no runs): its conditions map onto our families as
name collision → F8 (partial identity); document version and temporal → F7 (neighbouring value) or D (derived: "the
latest"); account collision and near duplicate → F8 or F0; cross-system → R (a relationship across services, outside
our single-service catalog); true ambiguity → our underspecified policy. It has nothing for F1 (sibling field or
role), F2 (indirection), F3 (direction), F4 (hierarchy), F5 (split binding) or F6 (representation), and no absence
condition. Its strongest failures (temporal, true ambiguity) are the ones our policy tests and F7 already target.

### 4.4 The plan for Agent-Diff (runnable by a session)

**What exists:** obligation cards for 164 of the 224 tests (Slack 59, Box 48, Linear 57: 440 obligations,
`grounding/domains/<service>/analysis/`), with each card's referent set and the columns and relationships it
identifies by; hand-labelled Sonnet 5 runs for Slack; the catalog; fdc.py; the backend's assertion engine; OpenClaw
on the self-host.

**Steps:**

1. **Calendar cards** (manual; a coding-agent session following `protocols/card_extraction.md`): the 60 Calendar
   tests, the same schema and coverage labels as the other three. About a day (an estimate).
2. **Translation table** (manual, once per service, an hour each): card vocabulary to catalog fact ids, e.g.
   `channels.channel_name` → `A:Conversation.channel_name`, the `messages.user_id` path → `R:messages.user_id`, two
   conditions on one related record → the matching B fact. This gives occurrence (a) for every obligation mechanically.
3. **Reference queries** (manual, the only creative step): one fdc.py query per resolved or absent obligation, written
   from the card. **The check that keeps it honest is mechanical:** fdc's `check_reference` must reproduce the card's
   referent set on the test's seed, or the query is rejected. Conditions that are topical judgments ("questions about
   lunch") become an `in` filter over the card's referents plus the channel or author conditions that are executable;
   the text fact then earns F0 at most. About 3 minutes an obligation (the pilot's rate, with the witness search and
   substitution automated): 30–35 hours for 600–700 obligations, so split by service across sessions.
4. **Near-miss search** (code): for each (obligation, fact), run the fact's designated mutation from the catalog (SUB,
   SPLIT, LEVEL, or another state value) and DROP; the witnesses are what the mutant selects and the original does
   not. The form check (target present, or absence permitted) comes from the card's resolution and the prompt.
   Output: measure (a).
5. **Oracle audit** (code): for each witness, the correct diff with the witness in the target's place, run through
   the suite's own compiler and engine, as the pilot did. A correct diff comes from a passing labelled run where one
   exists, or is built from the assertions. Output: the model-free half of (c).
6. **Runs:** all 224 tests on OpenClaw with the self-hosted Qwen, k = 3 (672 trials), unchanged prompts and seeds,
   with the suite's assertions recorded on every trial.
7. **Grading:** our triage plus judge v2 with the cards' referent sets as the answer key (as baselines_01 graded the
   baselines), which never goes to the suite's own oracle; a blind sample of 60 trials labelled by hand before any
   verdict. Output: the behavioural half of (c), and (d).
8. **Tables:** (a) to (d) per service and kind, with denominators; the flawed-test count (a test is flawed if its
   request cannot be satisfied on its seed, as for our own).

**Which tests first (a calibration step before the rest):** the 6 pilot tests; the 10 other Slack tests with a
labelled Sonnet failure (slack_95, 97, 98, 101, 103, 107, 108, 110, 113, 115; see
[slack_assertion_misses.json](pilot/slack_assertion_misses.json)); and 5 tests each of Box, Linear and Calendar drawn
with a fixed seed (42), stratified by the suite's own `prompt_ambiguity` label: 31 tests. Two mappers (the session
and a second agent, independently) write the reference queries for these; agreement on the facts credited is
reported before the rest is mapped.

**Cost:** mapping, about 3 to 4 session-days for about 600–700 obligations (manual work by the PI's definition); runs,
672 trials on the self-host (no charge; about 2 to 3 hours at 12 in flight, scaled from baselines_01's estimate of
1,700 trials in 5 to 7 hours); judge v2 on about 45% of trials at $0.028 list each, about **$8.5 list (about $0.6
billed)**; 60 blind labels, a few hours.

**Decision rules fixed before the runs** (so the numbers cannot be steered): a fact is covered only through a witness
fdc confirms on the seed; the oracle is blind to a fact if any of its witnesses passes; a trial's failure counts for a
fact only if the agent acted on (or reported) that fact's witness, as in our regular suite.

### 4.5 The ClawEnvKit arm (the Run verdict), sized

**Why it is needed:** it is the released, automated generator of tasks, fixtures and checks for OpenClaw-like
agents; a reviewer will ask why it is not the baseline. N0 and N1 answer "a coding agent asked plainly"; ClawEnvKit
answers "an established automated generator".

**Plan:**
1. Register Box, Calendar, Linear and Slack in its `SERVICE_DEFINITIONS` (description, actions, fixture shape) from
   the same API documentation N0 received; no change to its prompts or generation code. Half a day.
2. Generate **48 tasks, 12 per service** (the baselines' size) with **Muse** as its model (its client accepts any
   OpenAI-compatible base URL), keeping the roadmap's rule that baselines run on Muse.
3. Convert each task's fixtures into an Agent-Diff seed (a converter from its fixture JSON to seed tables; a day) and
   run the tasks on OpenClaw with the self-hosted Qwen, k = 3: **144 trials**.
4. Grade three ways: its own GradingEngine (over an audit log rebuilt from each trial's API calls; half a day for the
   adapter), our structural review of §1 of baselines_01 (facts exercised properly, flawed tests), and our judge with
   the review's intended targets as the answer key; 30 blind labels.

**Cost at list prices** (estimated from baselines_01's measured per-test costs: N0 $0.011 and N0M $0.025 per test;
ClawEnvKit makes about 2 to 3 calls a task, a long generation call and a short feasibility judge): generation
**$1.5–3**; its LLM rubric grader, about **$1–2**; our judge, about **$2**; in all **about $5–7 list (under $0.5
billed)**; 144 trials on the self-host; about 2 days of adapter work.

**Prediction, written before any run:** its tasks leave the target present with plain look-alikes at most (its
fixtures are generated to make the task feasible), so, like N0M, it exposes **0 or 1** facts; its own grader reports
failures that are not wrong-record failures (calls and parameters, not state), so its precision on wrong-record
failures is below N0's assertions (0.54).

## 5. Baselines for the policy, several-match and boundary tests

### 5.1 The principle

A fair baseline for a test form gets what the roadmap's concept row gives G0 for regular tests, and nothing of the
method:

| Given to the baseline | Absence | Underspecified | Several-match | Boundary |
|---|:-:|:-:|:-:|:-:|
| The form's concept in plain words, and what passing means | ✓ | ✓ | ✓ | ✓ |
| The service's API docs, how to seed records, the test format, the scope (identifying records only) | ✓ | ✓ | ✓ | ✓ |
| The twins' reviewer lines (different properties; challenging but passable; neutral ids) | ✓ | ✓ | ✓ | ✓ |
| Our catalog, the substitute menus, the route tables, the boundary derivation, the method | – | – | – | – |

The concept lines, one per form: *absence*: "the request names a record that does not exist; the agent should say so
and change nothing"; *underspecified*: "more than one record fits; the agent should ask which one before changing
anything"; *several-match*: "the request asks for every record that fits; the agent passes if it acts on all of them
and nothing else"; *boundary*: "the request asks for a change this user cannot make here; the agent should say so and
change nothing it was not asked to change".

Everything else is shared with our arm: the same solver, k = 3, the same judge with the baseline's own intended
outcome as the answer key (never shown to the baseline's own oracle), a blind sample labelled before any verdict,
flawed tests counted as flawed, and each form's own unit of requirement. Three kinds of arm per form: the coding
agent given the concept (the analogue of N0M), a mechanical mutation of an existing suite (what a software-engineering
reviewer would try first), and a projection of the established items that exist (§2, angle J).

### 5.2 Policy tests: absence and underspecified

Our space: two requirements per covered fact, 408 fact–mode requirements; our 441 valid cases reach 370 of them.

| Arm | What it is | Measure | Cost |
|---|---|---|---|
| **P0**, the coding agent with the policy concepts | N0M's inputs plus the absence and underspecified lines; 48 tests (6 per service and mode) | Fact–mode requirements exercised properly (the absent request's near misses each fail one fact; the underspecified request leaves one condition open or has a second full match), and failed @1 and @3 | Generation about $1.2 list (N0M's); 144 trials; judging about $2 |
| **P1**, mutation of the status quo | From Agent-Diff's own tests, mechanically: delete the target from the seed (absence), or clone the target under a new id (underspecified); nothing else changes. No LLM | The same, over the same budget of variants per service | Code only; 144 trials |
| **P2**, projection of established items | Agent-Diff's own underspecified obligations (20 in Slack; 11 of Sonnet's 18 wrong obligations), AgentAbstain's missing-parameter and ambiguous-action pairs, ToolEmu's underspecified cases, BFCL's missing parameters, Gaia2's Ambiguity split | Which fact–mode requirement each item exercises, if any | Reading only |
| P3, optional | IntellAgent with our two policies as its "system prompt" and our schemas; events converted to seeds | As P0 | As the ClawEnvKit arm |

**What each isolates.** P0: our derivation against an LLM told the concept. P1: our derivation against the generic
mutation. Ours differs from P1 in exactly one designed way: our absence variant removes the target but keeps
designated near misses that each fail one fact, and our underspecified variant opens one condition at a time, so a
failure names a fact. **Prediction:** P0 and P1 expose many absence failures (the agent acts anyway, as N0's
presupposing tests showed: all its failing trials were there), attributed to few distinct facts; the established
items (P2) sit at the request level (a missing argument or tool), not on a fact.

### 5.3 Several-match

Our space: 6 kinds of request with a route table, 33 shortcuts, 19 of them lazy and practical to defeat; our
automation defeats all 19.

| Arm | What it is | Measure | Cost |
|---|---|---|---|
| **S0**, the coding agent with the several-match concept | N0M's inputs plus the several-match line; 48 tests | Shortcuts defeated on the baseline's seeds, by the same shortcut check the automation runs ([several_match_auto_01/checks.py](../several_match_auto_01/checks.py)); a test outside the six kinds earns no shortcut; misses and near misses acted on @1 and @3 | About $1.2 list; 144 trials |
| **S1**, projection of the status quo | Agent-Diff's multi-entity tests (20 Box, 49 Calendar, 24 Linear, 26 Slack; the suite's own label, a proxy for plural requests): the shortcut check on their seeds, and their assertions' view of an omitted target (the pilot: slack_67 passes with two of four targets left out) | Shortcuts defeated; oracle blind to omissions | Code only |
| Ablation, not a baseline | Our easy tier alone against easy plus hard | Already in several_match_auto_01's data | None |

**Prediction:** S0's targets sit in plain view (the easy tier), so it defeats "stopping early" and little else;
pages, hidden visibility and other scopes need a trap no one writes unprompted.

### 5.4 Capability boundaries

Our space: 152 elements derived from the catalog, 93 faithful to the replica, in five classes: permission, read-only
field, state precondition, value limit, no operation. Our tests are valid for 90 of 93; 49 of 89 fail at least once.

| Arm | What it is | Measure | Cost |
|---|---|---|---|
| **B0**, the coding agent with the boundary concept | N0M's inputs plus the boundary line; 48 tests | Faithful boundary elements with a valid test (checked on the replica, as our filter does) and failed @1 and @3, by class; failure kinds (substitute, re-creation, side change, false claim) | About $1.2 list; 144 trials |
| **B1**, mechanical infeasibility (FeasiGen's idea) | Take tests the agent solves (our covers, or Agent-Diff's) and remove the needed operation: drop it from the skill's documentation and refuse it in the curl wrapper | The same; all land in "no operation" | Code only; 144 trials |
| **B2**, projection of established items | AgentAbstain's insufficient-tools pairs, ToolBeHonest's three scenarios, BFCL's missing functions, When2Call's "cannot answer" | Which of the five classes each item exercises | Reading only |

**Prediction:** B0 writes mostly "no operation" and permission requests, several of them not boundaries on this
replica (the twins already wrote a bot deleting others' messages and an actor deleting a calendar it does not own,
by accident); B1 and B2 cover "no operation" only. Read-only fields, state preconditions and value limits stay
ours.

### 5.5 What stays the PI's choice

- **Budget:** 48 tests per arm (as now) or matched by tokens (the PI's idea in section G of the notes). Every arm above
  is cheap enough to run at either.
- **Stronger baseline agents:** Muse only (the roadmap's rule) or also Sonnet 5 and GPT-6.1 Sol through Codex.
- **The unit:** fact–mode requirements (ours) or request-level categories (the established suites'); I recommend
  reporting both, since the gap between them is the finding.
- **Order:** P1, S1, B1 and B2 need no LLM and no decision; they could run first.

## 6. What we do that they cannot

| Capability | Ours | Closest prior work |
|---|---|---|
| A requirement space from a model of the world the agent acts on | 255 facts, 213 servable, each with a designated alternative where one exists | API-surface coverage (Agent-Diff: 108 endpoints); coverage of the agent's own specification (Skill Coverage, workflow structure) |
| Near misses built for a stated fact and checked mechanically | Every decoy fails exactly its fact on the seed (fdc) | Hand-written distractors (AppWorld, Agent-Diff curation, EBF's conditions); neighbour queries for SQL (Zhong et al.), not agents |
| The forms that make a fact bite | Probes with absence permitted; policy variants derived per fact | Paired should-act/should-abstain tasks (AgentAbstain), one perturbation per pair, not per fact |
| An oracle validated on wrong-record actions | Triage plus judge v2: 309 of 310 blind labels | ARE verifier (0.99/0.95 on 450 labels, write matching); most others unvalidated or validated by agreement ratings |
| Flawed tests found and counted | Checks, cold reader, rulings; 565 of 582 derived candidates valid | ClawEnvKit's structural validator; ABC's audits after the fact |

## 7. Limits of this study

- **Coverage of the literature:** the search ran on one day (2026-09-30) through the survey's bibliography, arXiv and
  web search; the angles are a map, not a systematic review. Works after July 2026 are thinly covered.
- **Claims about other works** rest on their papers and repositories as fetched on 2026-09-30 ([claims.md](claims.md)
  quotes each). Their numbers are theirs; the PI's MCP-Bench audit is unpublished.
- **The pilots are small:** 59 Slack tests with one Sonnet 5 trial each; 8 obligations for the projection method.
  They show the method works and what it costs, not the suite-wide numbers.
- **No new model runs:** every arm in §4 and §5 is a proposal with a cost and a prediction, none run.
