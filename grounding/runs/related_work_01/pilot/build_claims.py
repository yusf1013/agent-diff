import json, re, sys
from pathlib import Path
meta = {k.split('v')[0]: v for k, v in json.load(open('meta.json')).items()}
def norm(t): return re.sub(r'\s+', ' ', t)
texts = {}
def text(src):
    if src not in texts:
        if src.startswith('abs:'):
            texts[src] = norm(meta[src[4:]]['abstract'])
        else:
            texts[src] = norm(Path(src).read_text(errors='ignore'))
    return texts[src]
def quote(src, phrase, before=0, after=0):
    t = text(src)
    i = t.find(phrase)
    if i < 0:
        # tolerate hyphenation/line-break artifacts
        p2 = re.escape(phrase).replace('\\ ', r'\s*-?\s*')
        m = re.search(p2, t)
        if not m: return None
        i, j = m.start(), m.end()
    else:
        j = i + len(phrase)
    return t[max(0, i - before):j + after].strip()

A = 'https://arxiv.org/abs/'
C = []  # (heading, url, [(claim, src, phrase)])
def add(h, url, items): C.append((h, url, items))

add('Agent-Diff (arXiv 2602.11224)', A+'2602.11224', [
 ('224 tasks over four services', '2602.11224.txt', 'The resulting benchmark comprises 224 tasks across four enterprise services'),
 ('endpoints sampled uniformly; 108 endpoints', '2602.11224.txt', 'Uniform sampling encourages coverage across the API surface. The benchmark spans 108 unique endpoints'),
 ('LLMs write prompt, seed and assertions', '2602.11224.txt', 'we use a mix of LLMs (Claude Opus 4.5 and Gemini 3 Pro) to generate'),
 ('people add ambiguity and distractors', '2602.11224.txt', 'Reviewers then control the ambiguity dimension'),
 ('closed-world invariant (paper)', '2602.11224.txt', 'Any other insertion, deletion, or mutation is treated as a side effect and causes the task to fail'),
])
add('AppWorld (arXiv 2407.18901)', A+'2407.18901', [
 ('9 apps, 457 APIs, ~100 users', 'abs:2407.18901', 'a high-quality execution environment (60K lines of code) of 9 day-to-day apps operable via 457 APIs'),
 ('presuppositions hold; distractors added', '2407.18901.txt', 'Pre-supposit'),
 ('distractors', '2407.18901.txt', 'Has Distractors: Many task-relevant distractors are added'),
 ('state-based evaluation, collateral damage', '2407.18901.txt', 'an agent solving the task can cause collateral damage in vastly many ways'),
 ('250 scenarios x 3 tasks', '2407.18901.txt', 'Our benchmark has 250 task scenarios with 3 tasks'),
])
add('τ-bench (arXiv 2406.12045)', A+'2406.12045', [
 ('database-state oracle; pass^k', 'abs:2406.12045', 'compares the database state at the end of a conversation with the annotated goal state'),
])
add('τ²-bench (arXiv 2506.07982)', A+'2506.07982', [
 ('compositional task generator', 'abs:2506.07982', 'A compositional task generator that programmatically'),
])
add('ABC, Agentic Benchmark Checklist (arXiv 2507.02825)', A+'2507.02825', [
 ('τ-bench trivial agent passes impossible tasks', '2507.02825.txt', 'a trivial agent that returns empty responses is considered successful'),
 ('38% of tasks', '2507.02825.txt', 'allows a trivial agent to pass 38% of tasks'),
 ('7 and 7 of 10 benchmarks', '2507.02825.txt', 'resulting in seven benchmarks with flaws in outcome validity'),
 ('WebArena overestimates by 5.2%', '2507.02825.txt', 'overestimates performance of agents by 5.2%'),
 ('state-matching checks', '2507.02825.txt', 'O.g.1. Ground truth includes all states achievable after success'),
 ('inputs must affect the output', '2507.02825.txt', 'Moreover, the inputs must affect the output'),
])
add('AgentDojo (arXiv 2406.13352)', A+'2406.13352', [
 ('97 tasks, 629 security cases', 'abs:2406.13352', 'We populate the environment with 97 realistic tasks'),
 ('suites and sizes (Table 1)', '2406.13352.txt', 'Workspace 24 40 6'),
 ('Slack suite size', '2406.13352.txt', 'Slack 11 21 5'),
 ('utility function', '2406.13352.txt', 'The utility function is implemented as a deterministic binary function'),
 ('tasks designed manually', '2406.13352.txt', 'We first manually design user tasks'),
])
add('ToolSandbox (arXiv 2408.04682)', A+'2408.04682', [
 ('milestones and minefields', '2408.04682.txt', 'milestone / minefield based system for intermediate and final execution evaluation'),
 ('Insufficient Information category', 'abs:2408.04682', 'complex tasks like State Dependency, Canonicalization and Insufficient Information'),
])
add('Gaia2 / ARE (arXiv 2509.17158)', A+'2509.17158', [
 ('800 scenarios, 10 universes, 101 tools', '2509.17158.txt', 'Gaia2 consists of 800 unique verifiable scenarios, carefully annotated by humans across 10 distinct universes'),
 ('verifier compares write actions', '2509.17158.txt', 'comparing agent write actions only to annotated oracle write actions'),
 ('validation on 450 trajectories (Table 1)', '2509.17158.txt', 'In-context Verifier (LLM judge only) ARE Verifier Agreement Precision Recall 0.72 0.98 0.53 0.99 0.83 0.95'),
 ('annotation interface not released', '2509.17158.txt', 'through an annotation interface (not released)'),
 ('Ambiguity split', '2509.17158.txt', 'Ambiguity scenarios reflect user tasks that are impossible, contradictory, or have multiple valid answers'),
])
add('TheAgentCompany (arXiv 2412.14161)', A+'2412.14161', [
 ('175 tasks', '2412.14161.txt', 'a set of 175 diverse, realistic and professional tasks'),
 ('Plane', '2412.14161.txt', 'Plane,6 an open-source alternative to task management software such as Jira or Linear'),
 ('RocketChat', '2412.14161.txt', 'RocketChat,7 an open-source alternative to communication software such as Slack'),
])
add('MCP-Universe (arXiv 2508.14704)', A+'2508.14704', [
 ('6 domains, 11 servers, evaluators', 'abs:2508.14704', 'Our benchmark encompasses 6 core domains spanning 11 different MCP servers'),
])
add('MCPMark (arXiv 2509.24002)', A+'2509.24002', [
 ('127 tasks, experts and AI agents, verification scripts', 'abs:2509.24002', 'It consists of $127$ high-quality tasks collaboratively created by domain experts and AI agents'),
])
add('Toolathlon (arXiv 2510.25726)', A+'2510.25726', [
 ('32 apps, 604 tools', 'abs:2510.25726', 'Toolathlon spans 32 software applications and 604 tools'),
 ('108 tasks', 'abs:2510.25726', 'This benchmark includes 108 manually sourced or crafted tasks'),
])
add('Claw-Eval (arXiv 2604.06132)', A+'2604.06132', [
 ('300 human-verified tasks', 'abs:2604.06132', 'with 300 human-verified tasks spanning 9 categories'),
])
add('ClawsBench (arXiv 2604.05172; github.com/benchflow-ai/ClawsBench)', A+'2604.05172', [
 ('five mocks, 44 tasks', 'abs:2604.05172', 'It includes five high-fidelity mock services'),
])
add('WorkBench (arXiv 2405.00823)', A+'2405.00823', [
 ('5 databases, 26 tools, 690 tasks', 'abs:2405.00823', 'WorkBench contains a sandbox environment with five databases, 26 tools, and 690 tasks'),
 ('templates', '2405.00823.txt', 'we create 10 unique tasks for each template'),
 ('outcome-centric evaluation', 'abs:2405.00823', 'We call this key contribution outcome-centric evaluation'),
])
add('STAGE-Claw (arXiv 2606.10394)', A+'2606.10394', [
 ('automated creation from a task hint', 'abs:2606.10394', 'Given a task hint, STAGE-Claw automatically creates and validates a realistic benchmark task'),
 ('40 tasks', 'abs:2606.10394', 'this paper creates a benchmark with 40 challenging real scenario agent tasks'),
 ('human audit', '2606.10394.txt', 'human annotators'),
])
add('MCP-Bench (arXiv 2508.20453)', A+'2508.20453', [
 ('o4-mini synthesis', '2508.20453.txt', 'We use o4-mini (OpenAI, 2025c) as the task synthesis LLM'),
 ('quality thresholds', '2508.20453.txt', 'Tasks failing the quality threshold (solvability: 9.0/10, utility: 5.0/10) are disgarded'),
 ('fuzzy rewriting', '2508.20453.txt', 'each task is rewritten into a fuzzy and instruction-minimal variant'),
 ('human inspection', '2508.20453.txt', 'the tasks in M C P- Be nc h also undergo human inspection'),
 ('judge design', '2508.20453.txt', 'rubric-driven LLM-as-a-Judge scoring of task completion, tool usage, and planning effectiveness'),
 ('judge validation by agreement rating', '2508.20453.txt', 'rated their agreement on a 3-point scale'),
])
add('MCPEval (arXiv 2507.12806)', A+'2507.12806', [
 ('ground truth from a frontier agent', '2507.12806.txt', 'Successful execution trajectory leads directly to verified tasks and corresponding ground truth'),
])
add('LiveMCPBench (arXiv 2508.01780)', A+'2508.01780', [
 ('95 tasks, 70 servers', 'abs:2508.01780', 'which evaluates 95 real-world daily tasks'),
])
add('ClawEnvKit (arXiv 2604.18543; github.com/xirui-li/ClawEnvKit)', A+'2604.18543', [
 ('pipeline', 'abs:2604.18543', 'The pipeline comprises three modules'),
 ('1,040 environments, 13,800x', '2604.18543.txt', 'Auto-ClawEval matches or exceeds human-curated environments on coherence and clarity at 13,800× lower cost'),
 ('15 check types over audit log, output, files', '2604.18543.txt', '15 check types drawn from three sources'),
 ('feasibility by one LLM call', '2604.18543.txt', 'A single LLM call checks'),
 ('OpenClaw via native plugin', '2604.18543.txt', 'native tool plugin'),
])
add('IntellAgent (arXiv 2501.11067)', A+'2501.11067', [
 ('policy graph and events', '2501.11067.txt', 'constructing a policy graph to represent the relationships'),
 ('validity by correlation with τ-bench', '2501.11067.txt', 'strong correlation between model performance on th'),
])
add('AgentAbstain (arXiv 2607.10059)', A+'2607.10059', [
 ('263 pairs, 42 environments', 'abs:2607.10059', 'It contains 263 paired tasks across 42 executable sandbox environments'),
 ('one controlled perturbation', 'abs:2607.10059', 'produced through a controlled perturbation to the instruction, tool, or environment state'),
 ('categories', '2607.10059.txt', 'S1 Missing Parameter, S2 Ambiguous Action, S3 Conflicting Constraints, S4 High Stakes, S5 Insufficient Tools'),
 ('annotators 94-98%', 'abs:2607.10059', 'three independent annotators rate 94-98% of sampled tasks as well-designed'),
 ('best 59.5%', 'abs:2607.10059', 'achieves only 59.5% paired accuracy'),
])
add('FeasiGen (arXiv 2605.28532)', A+'2605.28532', [
 ('masking critical tools', 'abs:2605.28532', 'masks these tools to automatically transform solvable tasks into infeasible ones'),
 ('94% and 73.9%', 'abs:2605.28532', 'over 94% accuracy'),
 ('false continue', 'abs:2605.28532', 'false continue rate reaching up to 73.9%'),
])
add('EnvScaler (arXiv 2601.05808; github.com/RUC-NLPIR/EnvScaler)', A+'2601.05808', [
 ('191 environments, ~7K scenarios', 'envscaler.txt', 'we construct around 7K task scenarios for 191 environments'),
 ('check functions and reward', 'envscaler.txt', 'the proportion of passed functions is used as the trajectory’s reward score'),
 ('validity via win rates', 'envscaler.txt', 'confirming the validity of the state-check functions in distinguishing and quantifying model performance'),
 ('environment quality scored by Claude', 'envscaler.txt', "Claude-4.5-Sonnet’s scores align highly with manual judgments"),
 ('reverse synthesis (AgentScaler, AutoForge)', 'envscaler.txt', 'is to walk through tool invocation sequences and infer the corresponding task by reversing the sequence'),
 ('state prompt (scen_generator/step1_gen_env_config.py)', 'envscaler/step1_gen_env_config.py', 'with differentiated content to avoid repetitive templates'),
 ('task prompt: feasible (step2_gen_scenario_task.py)', 'envscaler/step2_gen_scenario_task.py', 'For example, you cannot delete a file that does not exist'),
 ('task prompt: unambiguous', 'envscaler/step2_gen_scenario_task.py', 'The description must be easy to understand and unambiguous'),
 ('checklist prompt (task_check_util/gen_checklist.py)', 'envscaler/gen_checklist.py', 'Every checklist item must start with the **exact phrase**: **"Has …"**'),
 ('check prompt: existence only for non-fixed values (gen_check_func.py)', 'envscaler/gen_check_func.py', 'only verify that the field exists and meets basic conditions'),
])
add('Survey: agentic environment engineering (arXiv 2606.12191)', A+'2606.12191', [
 ('quality dimensions', 'survey_plain.txt', 'We summarize existing evaluation practices along four complementary dimensions: correctness, diversity, complexity, and fidelity'),
 ('diversity via embeddings', 'survey_plain.txt', 'EnvScaler [161] uses embedding similarity and t-SNE'),
])
add('Skill Coverage (arXiv 2606.20659)', A+'2606.20659', [
 ('38.66–45.51%', '2606.20659.txt', '38.66'),
])
add('Structural coverage of agentic workflows (arXiv 2605.26521)', A+'2605.26521', [
 ('does not replace semantic evaluation', '2605.26521.txt', 'it does not replace semantic or end-to-end evaluation'),
])
add('Prompt Coverage Adequacy (arXiv 2607.02057)', A+'2607.02057', [
 ('criterion at the level of prompts', 'abs:2607.02057', 'we propose Prompt Coverage Adequacy, a novel coverage criterion'),
])
add('ToolFuzz (arXiv 2503.04479)', A+'2503.04479', [
 ('tests tool documentation', 'abs:2503.04479', 'there currently exists no automated method to test the tool documentation for agents'),
])
add('Agent-as-a-Judge (arXiv 2410.10934)', A+'2410.10934', [
 ('55 tasks, 365 requirements; reliability', 'abs:2410.10934', 'is as reliable as our human evaluation baseline'),
])
add('AgentRewardBench (arXiv 2504.08942)', A+'2504.08942', [
 ('1,302 trajectories, 12 judges', 'abs:2504.08942', 'AgentRewardBench contains 1302 trajectories'),
 ('rule-based checks under-report', 'abs:2504.08942', 'tends to underreport the success rate of web agents'),
])
add('False success (arXiv 2606.09863)', A+'2606.09863', [
 ('45–48% and AUROC 0.65', 'abs:2606.09863', '45--48% of failures in single-control tau2-bench domains'),
 ('judges', 'abs:2606.09863', 'exceeds AUROC 0.65 on tau2-bench'),
])
add('Are "solved issues" solved? (arXiv 2503.15223)', A+'2503.15223', [
 ('plausible but incorrect patches', 'abs:2503.15223', 'a patch may pass the tests but nevertheless fail to match the developers'),
])
add('Test-suite accuracy for text-to-SQL (arXiv 2010.02840)', A+'2010.02840', [
 ('neighbor queries', '2010.02840.txt', 'which are generated by modifying one aspect of the gold query'),
 ('distinguish neighbours', '2010.02840.txt', 'if a test suite can distinguish them from the gold, it is likely to distinguish other wrong queries as well'),
])
add('XData (arXiv 1411.6704; VLDB Journal 2015)', A+'1411.6704', [
 ('kill query mutants; grading', 'abs:1411.6704', 'mutation'),
])
add('Entity Binding Failures (arXiv 2606.30531; github.com/R-Suresh/EntityBindingFailures)', A+'2606.30531', [
 ('the failure class', '2606.30531.txt', 'an agent may choose the right tool and still act on the wrong external entity'),
 ('60 tasks, 24–26%', '2606.30531.txt', 'all methods achieved 0.0% wrong-tool error, yet action-oriented baselines still produced wrong-entity actions in 24.0–26.0% of runs'),
 ('single-step decisions', '2606.30531.txt', 'The experiments focus on single-step tool execution decisions'),
 ('state given to the agent', '2606.30531.txt', 'the agent receives the user instruction, environment state, and available tools, then directly produces a tool call'),
 ('per-condition results (Table III)', '2606.30531.txt', 'Name collision 20.0 20.0 20.0 20.0 0.0 0.0 Document version 0.0 0.0 0.0 0.0 0.0 0.0 Temporal 100.0 90.0 97.5 100.0 0.0 0.0'),
 ('released', '2606.30531.txt', 'are publicly available at: https://github.com/R-Suresh/EntityBindingFailures'),
])
add('AmbER (arXiv 2106.06830)', A+'2106.06830', [
 ('same-name entities', 'abs:2106.06830', 'We define an AmbER set as a collection of entities that share a name'),
])
add('When2Call (arXiv 2504.18851)', A+'2504.18851', [
 ('call, ask, or admit', 'abs:2504.18851', 'when to generate a tool call, when to ask follow-up questions and when to admit the question can\'t be answered'),
])
add('ToolBeHonest (arXiv 2406.20015)', A+'2406.20015', [
 ('three scenarios, 700 samples', 'abs:2406.20015', 'missing necessary tools, potential tools, and limited functionality tools'),
 ('700 samples', 'abs:2406.20015', 'collected 700 evaluation samples'),
])
add('NoisyToolBench (arXiv 2409.00557)', A+'2409.00557', [
 ('missed arguments', 'abs:2409.00557', 'LLMs tend to arbitrarily generate the missed argument'),
])
add('ACEBench (arXiv 2501.12851)', A+'2501.12851', [
 ('Special category', 'abs:2501.12851', '"Special" evaluates tool usage in situations with ambiguous or incomplete instructions'),
])
add('UserBench (arXiv 2507.22034)', A+'2507.22034', [
 ('underspecified goals', 'abs:2507.22034', 'simulated users who start with underspecified goals and reveal preferences incrementally'),
])
add('ToolEmu (arXiv 2309.15817)', A+'2309.15817', [
 ('68.8% valid; 144 test cases', 'abs:2309.15817', '68.8% of failures identified with ToolEmu would be valid real-world agent failures'),
 ('144 cases', 'abs:2309.15817', '36 high-stakes tools and 144 test cases'),
])
add('MANTRA (arXiv 2605.06334)', A+'2605.06334', [
 ('SMT validation', 'abs:2605.06334', 'validates their consistency using SMT solving'),
 ('285 tasks, 6 domains', 'abs:2605.06334', 'we build a new benchmark suite with 285 tasks across 6 domains'),
])
add('AutoWebWorld (arXiv 2602.14296)', A+'2602.14296', [
 ('FSM-based synthesis', 'abs:2602.14296', 'Finite State Machine'),
])
add('Fabrication after tool failure (arXiv 2609.14758)', A+'2609.14758', [
 ('14.10% dishonest', 'abs:2609.14758', '14.10% of responses are dishonest'),
])
add('ToolFailBench (arXiv 2607.04686)', A+'2607.04686', [
 ('categories', 'abs:2607.04686', 'We label each trace with Tool-Skip, Result-Ignore, Output-Fabrication, and Unnecessary-Tool-Use'),
])

out = ["# Claims and their sources", "",
       "*Every claim about another work that report.md relies on, with the exact words it rests on. All sources were fetched",
       "on 2026-09-30 (arXiv PDFs and abstracts through arxiv.org and its API; repositories through GitHub). Quotes are",
       "verbatim after collapsing whitespace; line-break artifacts of the PDF text are kept. Built by `build_claims.py`",
       "(kept in the session scratchpad; the quotes are the record).*", ""]
missing = 0
for h, url, items in C:
    out.append(f"## {h}")
    out.append("")
    out.append(f"Source: <{url}>, fetched 2026-09-30.")
    out.append("")
    for claim, src, phrase in items:
        q = quote(src, phrase, before=0, after=160)
        if q is None:
            missing += 1
            out.append(f"- **{claim}:** MISSING QUOTE ({phrase!r} in {src})")
        else:
            where = 'abstract' if src.startswith('abs:') else ('repository file ' + src.split('/')[-1] if src.startswith('envscaler/') else 'paper text')
            out.append(f"- **{claim}** ({where}): “{q[:420]}…”")
    out.append("")
Path(sys.argv[1]).write_text("\n".join(out) + "\n")
print("missing", missing)
