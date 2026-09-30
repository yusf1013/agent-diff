# Claims and their sources

*Every claim about another work that report.md relies on, with the exact words it rests on. All sources were fetched
on 2026-09-30 (arXiv PDFs and abstracts through arxiv.org and its API; repositories through GitHub). Quotes are
verbatim after collapsing whitespace; line-break artifacts of the PDF text are kept. Built by [pilot/build_claims.py](pilot/build_claims.py)
from the fetched texts, which are not committed (size and licences); the quotes are the record.*

## Agent-Diff (arXiv 2602.11224)

Source: <https://arxiv.org/abs/2602.11224>, fetched 2026-09-30.

- **224 tasks over four services** (paper text): “The resulting benchmark comprises 224 tasks across four enterprise services: Box (file management), Linear (project management), Slack (messaging), and Google Calendar (scheduling). Table 3 summarizes the distribution across taxonomy d…”
- **endpoints sampled uniformly; 108 endpoints** (paper text): “Uniform sampling encourages coverage across the API surface. The benchmark spans 108 unique endpoints (Box: 27, Slack: 25, Linear: 19, Calendar: 37). Task generation pipeline. For each sampled endpoint multiset, we use a mix of LLMs (Claude Opus 4.5 and Gemini…”
- **LLMs write prompt, seed and assertions** (paper text): “we use a mix of LLMs (Claude Opus 4.5 and Gemini 3 Pro) to generate: (1) a natural-language user prompt whose completion induces state changes consistent with (𝜀 1, . . . , 𝜀𝑛 ), (2) a deterministic seed template defining the i…”
- **people add ambiguity and distractors** (paper text): “Reviewers then control the ambiguity dimension (𝑑 amb ) by selectively degrading prompts – removing explicit identifiers, introducing typographical variations, or adding distractor entities to the seed stat…”
- **closed-world invariant (paper)** (paper text): “Any other insertion, deletion, or mutation is treated as a side effect and causes the task to fail. Scoring and uncertainty. Let sat(𝑎, Δ𝑆) ∈ {0, 1} indicate whether assertion 𝑎 holds on the state diff. We report two task-level metrics: Agent-Diff: Benchmark…”

## AppWorld (arXiv 2407.18901)

Source: <https://arxiv.org/abs/2407.18901>, fetched 2026-09-30.

- **9 apps, 457 APIs, ~100 users** (abstract): “a high-quality execution environment (60K lines of code) of 9 day-to-day apps operable via 457 APIs and populated with realistic digital activities simulating the lives of ~100 fictitious users. We then created $\textbf{AppWorld Benchmark}$ (40K lines of code…”
- **presuppositions hold; distractors added** (paper text): “Pre-suppositions implied by the task are satisfied in the task DB state. E.g., in Fig. 3 task, the supervisor has placed past T-shirt orders, and the latest one is availabl…”
- **distractors** (paper text): “Has Distractors: Many task-relevant distractors are added to ensure that skipping intended interaction or not reasoning carefully will often lead the agent astray. E.g., Supervisor has multiple past orders for T-shirt…”
- **state-based evaluation, collateral damage** (paper text): “an agent solving the task can cause collateral damage in vastly many ways (e.g., deleting a wish list or initiating a return not asked for). To account for this, we propose a state-based programmatic evaluation approach, in contrast…”
- **250 scenarios x 3 tasks** (paper text): “Our benchmark has 250 task scenarios with 3 tasks each, totaling 750 tasks, split into Train (105), Dev (60), Test-N (168), and Test-C (417) splits. TestC (“challenge” set) consists of all tasks that need Di∆…”

## τ-bench (arXiv 2406.12045)

Source: <https://arxiv.org/abs/2406.12045>, fetched 2026-09-30.

- **database-state oracle; pass^k** (abstract): “compares the database state at the end of a conversation with the annotated goal state. We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials. Our experiments show that even state-of-the-art func…”

## τ²-bench (arXiv 2506.07982)

Source: <https://arxiv.org/abs/2506.07982>, fetched 2026-09-30.

- **compositional task generator** (abstract): “A compositional task generator that programmatically creates diverse, verifiable tasks from atomic components, ensuring domain coverage and controlled complexity, 3) A reliable user simulator tightly coupled with…”

## ABC, Agentic Benchmark Checklist (arXiv 2507.02825)

Source: <https://arxiv.org/abs/2507.02825>, fetched 2026-09-30.

- **τ-bench trivial agent passes impossible tasks** (paper text): “a trivial agent that returns empty responses is considered successful on intentionally impossible tasks (e.g., changing a non-refundable ticket). This trivial agent achieves a 38% success rate and outperforms a GPT-4o-based agent…”
- **38% of tasks** (paper text): “allows a trivial agent to pass 38% of tasks without knowledge of airline-ticketing rules. Following prior work on analyzing AI and code benchmarks [10, 65], we formulate our insights into an Agentic Benc…”
- **38% of the airline subset is intentionally unsolvable** (paper text): “First, τ -bench contains intentionally unsolvable tasks—38% of the airline subset and 6% of the retail subset. Because success is defined as leaving the environment unchanged,…”
- **7 and 7 of 10 benchmarks** (paper text): “resulting in seven benchmarks with flaws in outcome validity, seven with issues in task validity, and all with limitations in the result reporting. In addition to the issues found in τ -bench-Airline, some other example…”
- **WebArena overestimates by 5.2%** (paper text): “overestimates performance of agents by 5.2% due to various issues in its string matching. To demonstrate ABC’s practical value, we applied it to improve CVE-Bench, a complex, representative cybersecurity…”
- **state-matching checks** (paper text): “O.g.1. Ground truth includes all states achievable after success. O.g.2. Checks relevant and irrelevant states for the challenge. O.g.3. Ground truth is complex to prevent trivial state modifications. Answer matching: O.h.1.…”
- **inputs must affect the output** (paper text): “Moreover, the inputs must affect the output (O.e.3)—e.g., random negatives reveal nothing about relu(x) [35]. 3. End-to-end (E2E) Testing simulates complete user workflows, providing comprehensive testin…”

## AgentDojo (arXiv 2406.13352)

Source: <https://arxiv.org/abs/2406.13352>, fetched 2026-09-30.

- **97 tasks, 629 security cases** (abstract): “We populate the environment with 97 realistic tasks (e.g., managing an email client, navigating an e-banking website, or making travel bookings), 629 security test cases, and various attack and defense paradigms…”
- **suites and sizes (Table 1)** (paper text): “Workspace 24 40 6 “How many appointments do I have today?” “Send the Facebook security code to [attacker email]” Slack 11 21 5 “Invite Dora to Slack. You can find her e-mail on…”
- **Slack suite size** (paper text): “Slack 11 21 5 “Invite Dora to Slack. You can find her e-mail on her website: www.dora.com” “Send the link [phishing link] to Alice” Travel 28 20 7 “Make a reservation for th…”
- **utility function** (paper text): “The utility function is implemented as a deterministic binary function which, given outputs of the model together with the state of the environment before and after execution, determines whether the goal of the task has been accom…”
- **tasks designed manually** (paper text): “We first manually design user tasks that cover a diverse set of scenarios possible in the environment, including tasks requiring search capabilities over medium to long context windows (with up t…”

## ToolSandbox (arXiv 2408.04682)

Source: <https://arxiv.org/abs/2408.04682>, fetched 2026-09-30.

- **milestones and minefields** (paper text): “milestone / minefield based system for intermediate and final execution evaluation. A comparison between T OOL S ANDBOX and other benchmarks can be found in Table 1. 2 Stateful To construct challenging reasoning scenarios, T OOL S ANDBOX incl…”
- **Insufficient Information category** (abstract): “complex tasks like State Dependency, Canonicalization and Insufficient Information defined in ToolSandbox are challenging even the most capable SOTA LLMs, providing brand-new insights into tool-use LLM capabilities. ToolSandbox evaluation fra…”

## Gaia2 / ARE (arXiv 2509.17158)

Source: <https://arxiv.org/abs/2509.17158>, fetched 2026-09-30.

- **800 scenarios, 10 universes, 101 tools** (paper text): “Gaia2 consists of 800 unique verifiable scenarios, carefully annotated by humans across 10 distinct universes in the Mobile environment, with 101 tools each. The scenarios are organized into splits, each targeting one agent capability defined in Section 3.2. To support…”
- **verifier compares write actions** (paper text): “comparing agent write actions only to annotated oracle write actions, and for each write action, evaluating arguments, that can be seen as rubrics, via a soft (LLM judge) or hard (exact-match) comparison depending on the argumen…”
- **validation on 450 trajectories (Table 1)** (paper text): “In-context Verifier (LLM judge only) ARE Verifier Agreement Precision Recall 0.72 0.98 0.53 0.99 0.83 0.95 Table 1 ARE Verifier and In-context Verifier results on 450 trajectories annotated with human labels. We then evaluate the ARE Verifier powered with different…”
- **annotation interface not released** (paper text): “through an annotation interface (not released) described in Section A.5.4. The novelty of Mobile scenario creation is that it focuses on collecting the DAG of write events as ground truth, including user, o…”
- **Ambiguity split** (paper text): “Ambiguity scenarios reflect user tasks that are impossible, contradictory, or have multiple valid answers, with negative consequences arising during interaction if agents make mistakes. These scenarios test agents’ ability to recognize these issues and seek appropr…”

## TheAgentCompany (arXiv 2412.14161)

Source: <https://arxiv.org/abs/2412.14161>, fetched 2026-09-30.

- **175 tasks** (paper text): “a set of 175 diverse, realistic and professional tasks in a software engineering company setting. do not generalize well to novel tasks (Chollet et al., 2024), and may only have an impact on a small minority of the…”
- **Plane** (paper text): “Plane,6 an open-source alternative to task management software such as Jira or Linear. This is used to track issues, run sprints cycles, and manage product roadmaps. 4. RocketChat,7 an open-source alternative to communication software such as Sl…”
- **RocketChat** (paper text): “RocketChat,7 an open-source alternative to communication software such as Slack. This is a company-internal real-time messaging tool that facilitates collaboration between employees. All the websites hosted are reproducible and reset-able…”

## MCP-Universe (arXiv 2508.14704)

Source: <https://arxiv.org/abs/2508.14704>, fetched 2026-09-30.

- **6 domains, 11 servers, evaluators** (abstract): “Our benchmark encompasses 6 core domains spanning 11 different MCP servers: Location Navigation, Repository Management, Financial Analysis, 3D Design, Browser Automation, and Web Searching. To ensure rigorous evaluation, we implement…”

## MCPMark (arXiv 2509.24002)

Source: <https://arxiv.org/abs/2509.24002>, fetched 2026-09-30.

- **127 tasks, experts and AI agents, verification scripts** (abstract): “It consists of $127$ high-quality tasks collaboratively created by domain experts and AI agents. Each task begins with a curated initial state and includes a programmatic script for automatic verification. These tasks demand richer and more diverse intera…”

## Toolathlon (arXiv 2510.25726)

Source: <https://arxiv.org/abs/2510.25726>, fetched 2026-09-30.

- **32 apps, 604 tools** (abstract): “Toolathlon spans 32 software applications and 604 tools, ranging from everyday platforms such as Google Calendar and Notion to professional ones like WooCommerce, Kubernetes, and BigQuery. Most of the tools are base…”
- **108 tasks** (abstract): “This benchmark includes 108 manually sourced or crafted tasks in total, requiring interacting with multiple Apps over around 20 turns on average to complete. Each task is strictly verifiable through dedicated evaluation s…”

## Claw-Eval (arXiv 2604.06132)

Source: <https://arxiv.org/abs/2604.06132>, fetched 2026-09-30.

- **300 human-verified tasks** (abstract): “with 300 human-verified tasks spanning 9 categories across three groups: general service orchestration, multimodal perception and interaction, and multi-turn professional dialogue. To enable trajectory-aware gra…”

## ClawsBench (arXiv 2604.05172; github.com/benchflow-ai/ClawsBench)

Source: <https://arxiv.org/abs/2604.05172>, fetched 2026-09-30.

- **five mocks, 44 tasks** (abstract): “It includes five high-fidelity mock services (Gmail, Slack, Google Calendar, Google Docs, Google Drive) with full state management and deterministic snapshot/restore, along with 44 structured tasks coveri…”

## WorkBench (arXiv 2405.00823)

Source: <https://arxiv.org/abs/2405.00823>, fetched 2026-09-30.

- **5 databases, 26 tools, 690 tasks** (abstract): “WorkBench contains a sandbox environment with five databases, 26 tools, and 690 tasks. These tasks represent common business activities, such as sending emails and scheduling meetings. The tasks in WorkBench are challenging as they require plann…”
- **templates** (paper text): “we create 10 unique tasks for each template, yielding 690 tasks in total. Table 3 shows the number of templates for each domain in WorkBench. Our templates contain added linguistic variation, so that eac…”
- **outcome-centric evaluation** (abstract): “We call this key contribution outcome-centric evaluation. We evaluate five existing ReAct agents on WorkBench, finding they successfully complete as few as 3% of tasks (Llama2-70B), and just 43% for the best-performi…”

## STAGE-Claw (arXiv 2606.10394)

Source: <https://arxiv.org/abs/2606.10394>, fetched 2026-09-30.

- **automated creation from a task hint** (abstract): “Given a task hint, STAGE-Claw automatically creates and validates a realistic benchmark task with its environment, task prompts, ground truth, and related verification programs. Agents are then evaluated in realistic operating environments, where perfo…”
- **40 tasks** (abstract): “this paper creates a benchmark with 40 challenging real scenario agent tasks, evaluates 11 frontier models, and analyzes their task scores, costs, tool-call reliability, and common failure patterns. Overall, STAGE-Claw offers a scalable…”
- **human audit** (paper text): “human annotators check each accepted task for scenario realism, task completeness, instruction clarity, ground-truth correctness, and evaluator-rubric alignment. The annotation…”

## MCP-Bench (arXiv 2508.20453)

Source: <https://arxiv.org/abs/2508.20453>, fetched 2026-09-30.

- **o4-mini synthesis** (paper text): “We use o4-mini (OpenAI, 2025c) as the task synthesis LLM. All prompts used can be found in Section A.3. In total, we synthesized 56 tasks with a single server, 30 with 2 servers, and 18 with 3 servers. The single-ser…”
- **quality thresholds** (paper text): “Tasks failing the quality threshold (solvability: 9.0/10, utility: 5.0/10) are disgarded (see details in Section A.3). This ensures only high-quality tasks that meet our standards enter the final benchmark, maintaining benchmark integrity at the co…”
- **fuzzy rewriting** (paper text): “each task is rewritten into a fuzzy and instruction-minimal variant that retains the core objective but omits explicit tool references and execution steps. The example of the tasks in M C P- Be nc h can be found in Table 2 and…”
- **human inspection** (paper text): “the tasks in M C P- Be nc h also undergo human inspection to ensure their realism, executability, and the reasonability of the dependency chain analysis. We use o4-mini (OpenAI, 2025c) as the task synthesis LLM. All p…”
- **judge design** (paper text): “rubric-driven LLM-as-a-Judge scoring of task completion, tool usage, and planning effectiveness. To ensure stability, prompt shuffling and score averaging are applied. Our contributions can be summarized as follows: ① A realistic tool-using benchmark that…”
- **judge validation by agreement rating** (paper text): “rated their agreement on a 3-point scale: 0 for disagreement, 1 for partial agreement, and 2 for full agreement. The final human agreement score is the average across all annotators and tasks. As show…”

## MCPEval (arXiv 2507.12806)

Source: <https://arxiv.org/abs/2507.12806>, fetched 2026-09-30.

- **ground truth from a frontier agent** (paper text): “Successful execution trajectory leads directly to verified tasks and corresponding ground truth. In cases of task execution failure, the agent initiates a task updating request, prompting the generation of refined task descriptions. This iterative verific…”

## LiveMCPBench (arXiv 2508.01780)

Source: <https://arxiv.org/abs/2508.01780>, fetched 2026-09-30.

- **95 tasks, 70 servers** (abstract): “which evaluates 95 real-world daily tasks explicitly constructed to stress diverse tools and scaled multi-server routing. The benchmark includes a ready-to-deploy tool suite of 70 servers with 527 tool…”

## ClawEnvKit (arXiv 2604.18543; github.com/xirui-li/ClawEnvKit)

Source: <https://arxiv.org/abs/2604.18543>, fetched 2026-09-30.

- **pipeline** (abstract): “The pipeline comprises three modules: (1) a parser that extracts structured generation parameters from natural language input; (2) a generator that produces the task specification, tool interface,…”
- **1,040 environments, 13,800x** (paper text): “Auto-ClawEval matches or exceeds human-curated environments on coherence and clarity at 13,800× lower cost. Evaluated across 4 model families and 8 agent harness frameworks, we find that harness engineering boosts performance by up to 15.7 percentage points over a b…”
- **15 check types over audit log, output, files** (paper text): “15 check types drawn from three sources: audit-log checks (what the agent did), output checks (what the 6 agent said), and filesystem checks (what the agent created). The llm_judge (Zheng et al., 202…”
- **feasibility by one LLM call** (paper text): “A single LLM call checks for counterfactual tasks, for example, a prompt asking the agent to get tomorrow’s emails, or scoring criteria that reference information the agent cannot acce…”
- **OpenClaw via native plugin** (paper text): “native tool plugin (OpenClaw (Steinberger, 2025)), MCP server (Claude Code (Anthropic, 2025b), Codex (OpenAI, 2025b), Cursor (Anysphere, 2024), NanoClaw (qwibitai, 2026), IronCla…”

## IntellAgent (arXiv 2501.11067)

Source: <https://arxiv.org/abs/2501.11067>, fetched 2026-09-30.

- **policy graph and events** (paper text): “constructing a policy graph to represent the relationships, complexity, and likelihood of various policies, generating events by sampling combinations of policies from the graph that align with real-world tasks and dat…”
- **validity by correlation with τ-bench** (paper text): “strong correlation between model performance on the IntellAgent benchmark and the τ -bench [33], despite IntellAgent relying entirely on synthetic data. This validates IntellAgent as a robust alternative for ev…”

## AgentAbstain (arXiv 2607.10059)

Source: <https://arxiv.org/abs/2607.10059>, fetched 2026-09-30.

- **263 pairs, 42 environments** (abstract): “It contains 263 paired tasks across 42 executable sandbox environments, where each pair consists of a should-act task and a should-abstain variant produced through a controlled perturbation to the instruction, tool, or environment…”
- **one controlled perturbation** (abstract): “produced through a controlled perturbation to the instruction, tool, or environment state. To scale this paired design and resist data contamination, we propose AbstainGen, a fully automated pipeline that synthesizes sandbox environments and generat…”
- **categories** (paper text): “S1 Missing Parameter, S2 Ambiguous Action, S3 Conflicting Constraints, S4 High Stakes, S5 Insufficient Tools. Runtime categories (trigger discovered during execution): S6 Tool Failure, S7 Conflicting Evidence, S8 Emergent Risk. Avg. is the macro-average across all eig…”
- **annotators 94-98%** (abstract): “three independent annotators rate 94-98% of sampled tasks as well-designed. Across 17 frontier LLMs in 4 agent harnesses, the best agent (Gemini 3.1 Pro) achieves only 59.5% paired accuracy (correct on both the act and abstain sides o…”
- **best 59.5%** (abstract): “achieves only 59.5% paired accuracy (correct on both the act and abstain sides of each paired task). More importantly, abstention capability is largely independent of general task-solving capabil…”

## FeasiGen (arXiv 2605.28532)

Source: <https://arxiv.org/abs/2605.28532>, fetched 2026-09-30.

- **masking critical tools** (abstract): “masks these tools to automatically transform solvable tasks into infeasible ones. Human verification confirms that the infeasibility annotations for our constructed tasks achieve over 94% accuracy. We further introduce feasibility-aware eva…”
- **94% and 73.9%** (abstract): “over 94% accuracy. We further introduce feasibility-aware evaluation metrics for measuring whether agents can recognize infeasible tasks and stop execution appropriately. Extens…”
- **false continue** (abstract): “false continue rate reaching up to 73.9%. We further observe that multi-agent architectures significantly reduce erroneous execution under infeasible conditions.…”

## EnvScaler (arXiv 2601.05808; github.com/RUC-NLPIR/EnvScaler)

Source: <https://arxiv.org/abs/2601.05808>, fetched 2026-09-30.

- **191 environments, ~7K scenarios** (paper text): “we construct around 7K task scenarios for 191 environments and randomly sample 50 scenarios for a pilot study. As shown in Table 3, Qwen3-8B (Thinking) scores 57.78, while Qwen3-4B (Non-Think) scores only 37.53. Beside…”
- **check functions and reward** (paper text): “the proportion of passed functions is used as the trajectory’s reward score. Formally, we have: check {ck }K k=1 = M (Plist ||task), check fck = M (Pfunc ||ck ), K (10) 1 X reward = 1 [fck (Sfinal ) = True] . K k=1 Compared with a sing…”
- **validity via win rates** (paper text): “confirming the validity of the state-check functions in distinguishing and quantifying model performance. 5 Experiments 5.1 Experiment Setup Training. We conduct SFT and RL on Qwen3 series models (Thinking Mode) (Yang et al., 2025). A total of 140 environments are…”
- **environment quality scored by Claude** (paper text): “Claude-4.5-Sonnet’s scores align highly with manual judgments: (1) Tool-Program Alignment: it evaluates whether the semantic definition of the tool is consistent with its program implementation. (2) Functional Correctness…”
- **reverse synthesis (AgentScaler, AutoForge)** (paper text): “is to walk through tool invocation sequences and infer the corresponding task by reversing the sequence. However, this often yields low-quality tasks, and the existence of multiple valid task solution paths also make the sequence unsuitable as a unique “ground-tr…”
- **state prompt (scen_generator/step1_gen_env_config.py)** (repository file step1_gen_env_config.py): “with differentiated content to avoid repetitive templates. - Cover the different states and value ranges supported by the class wherever possible. - Dates should be distributed over a reasonable time span to provide d…”
- **task prompt: feasible (step2_gen_scenario_task.py)** (repository file step2_gen_scenario_task.py): “For example, you cannot delete a file that does not exist. ii. The task should be achievable through a combination of multiple operational interfaces supported by the environment. On one hand, the task description mus…”
- **task prompt: unambiguous** (repository file step2_gen_scenario_task.py): “The description must be easy to understand and unambiguous. Since the ultimate goal is to modify the state, query tools are only part of the task-solving process and serve to provide information to the Agent; therefore…”
- **checklist prompt (task_check_util/gen_checklist.py)** (repository file gen_checklist.py): “Every checklist item must start with the **exact phrase**: **"Has …"** followed by a clear description of the action or field to verify. 3. Use precise fields and exact values; **avoid vague wording**. 4. If the task requires chec…”
- **check prompt: existence only for non-fixed values (gen_check_func.py)** (repository file gen_check_func.py): “only verify that the field exists and meets basic conditions (e.g., non-empty string, correct data type). 4. If the check item specifies an explicit target value, you must strictly match it (`==`). 5. Use `initial_state`…”

## Survey: agentic environment engineering (arXiv 2606.12191)

Source: <https://arxiv.org/abs/2606.12191>, fetched 2026-09-30.

- **quality dimensions** (paper text): “We summarize existing evaluation practices along four complementary dimensions: correctness, diversity, complexity, and fidelity. We next discuss how prior work assesses environment quality from these perspectives. 5.3.1 Correctness Correctness is the most fundamental requirement for syn…”
- **diversity via embeddings** (paper text): “EnvScaler [161] uses embedding similarity and t-SNE visualization to analyze topic dispersion, and V-GameGym [344] applies clustering to select diverse game seeds from large code repositories. Other methods expa…”

## Skill Coverage (arXiv 2606.20659)

Source: <https://arxiv.org/abs/2606.20659>, fetched 2026-09-30.

- **38.66–45.51%** (paper text): “38.66–45.51% of the extracted skill behavior constraints on average. We then use Fail verdicts to strengthen the corresponding skill content only by emphasizing the…”

## Structural coverage of agentic workflows (arXiv 2605.26521)

Source: <https://arxiv.org/abs/2605.26521>, fetched 2026-09-30.

- **does not replace semantic evaluation** (paper text): “it does not replace semantic or end-to-end evaluation, but reveals whether declared agents, tool-access rules, restrictions, and delegation paths have been exercised. Index Terms—agent testing, coverage, mutation…”

## Prompt Coverage Adequacy (arXiv 2607.02057)

Source: <https://arxiv.org/abs/2607.02057>, fetched 2026-09-30.

- **criterion at the level of prompts** (abstract): “we propose Prompt Coverage Adequacy, a novel coverage criterion designed to support the testing of code generated from task descriptions. Prompt Coverage Adequacy serves as an analog to traditional code coverage, but operat…”

## ToolFuzz (arXiv 2503.04479)

Source: <https://arxiv.org/abs/2503.04479>, fetched 2026-09-30.

- **tests tool documentation** (abstract): “there currently exists no automated method to test the tool documentation for agents. To address this issue, we present ToolFuzz, the first method for automated testing of tool documentations. ToolFuzz is designed to discover two types of error…”

## Agent-as-a-Judge (arXiv 2410.10934)

Source: <https://arxiv.org/abs/2410.10934>, fetched 2026-09-30.

- **55 tasks, 365 requirements; reliability** (abstract): “is as reliable as our human evaluation baseline. Altogether, we believe that Agent-as-a-Judge marks a concrete step forward for modern agentic systems -- by providing rich and reliable reward signals necessa…”

## AgentRewardBench (arXiv 2504.08942)

Source: <https://arxiv.org/abs/2504.08942>, fetched 2026-09-30.

- **1,302 trajectories, 12 judges** (abstract): “AgentRewardBench contains 1302 trajectories across 5 benchmarks and 4 LLMs. Each trajectory in AgentRewardBench is reviewed by an expert, who answers questions pertaining to the success, side effects, an…”
- **rule-based checks under-report** (abstract): “tends to underreport the success rate of web agents, highlighting a key weakness of rule-based evaluation and the need to develop more flexible automatic evaluations. We release the benchmark at: https://agent-r…”

## False success (arXiv 2606.09863)

Source: <https://arxiv.org/abs/2606.09863>, fetched 2026-09-30.

- **45–48% and AUROC 0.65** (abstract): “45--48% of failures in single-control tau2-bench domains, 3% in dual-control telecom, and 75.8% among AppWorld self-assessing coding-agent trajectories with explicit status claims. LLM judges fail reliably: no config…”
- **judges** (abstract): “exceeds AUROC 0.65 on tau2-bench, and the same judges reach only 0.54 AUROC on AppWorld API-call traces. Judges rely on surface completion proxies -- confident closing language in tau2-bench a…”

## Are "solved issues" solved? (arXiv 2503.15223)

Source: <https://arxiv.org/abs/2503.15223>, fetched 2026-09-30.

- **plausible but incorrect patches** (abstract): “a patch may pass the tests but nevertheless fail to match the developers' expectations. Unfortunately, it is currently unclear to what extent evaluations performed with SWE-bench suffer from such plausible but incorrect patches. Thi…”

## Test-suite accuracy for text-to-SQL (arXiv 2010.02840)

Source: <https://arxiv.org/abs/2010.02840>, fetched 2026-09-30.

- **neighbor queries** (paper text): “which are generated by modifying one aspect of the gold query. For example, prediction 1 in Figure 1 is a neighbor query of the gold, since they differ only by a “WHERE” clause. These neighbor queries are usually semantic…”
- **distinguish neighbours** (paper text): “if a test suite can distinguish them from the gold, it is likely to distinguish other wrong queries as well. The latter holds because distinguishing all neighbors from the gold requires executions on these databases to exercise every modified part of the gold query,…”

## XData (arXiv 1411.6704; VLDB Journal 2015)

Source: <https://arxiv.org/abs/1411.6704>, fetched 2026-09-30.

- **kill query mutants; grading** (abstract): “mutations of the correct query. A mutation Q' of a query Q is killed by a dataset D if Q(D) $\neq$ Q'(D). Earlier work on the XData system showed how to generate datase…”

## Entity Binding Failures (arXiv 2606.30531; github.com/R-Suresh/EntityBindingFailures)

Source: <https://arxiv.org/abs/2606.30531>, fetched 2026-09-30.

- **the failure class** (paper text): “an agent may choose the right tool and still act on the wrong external entity. For example, a request to “email Alex about the launch” may lead the agent to contact the wrong Alex, attach the wrong launch document, reply in the wrong thr…”
- **60 tasks, 24–26%** (paper text): “all methods achieved 0.0% wrong-tool error, yet action-oriented baselines still produced wrong-entity actions in 24.0–26.0% of runs. Entity-aware methods eliminated wrong-entity actions and risk-weighted wrong-entity exposure in this setting, but reduced direct task completion by deferring…”
- **single-step decisions** (paper text): “The experiments focus on single-step tool execution decisions. This is appropriate for measuring whether an agent binds a requested action to the correct entity before execution. However, many deployed agents perform mult…”
- **state given to the agent** (paper text): “the agent receives the user instruction, environment state, and available tools, then directly produces a tool call. • Semantic filter: tools are filtered by semantic relevance to the user instruction before the agent acts. • CMTF only: tools are filtered using causal or sta…”
- **per-condition results (Table III)** (paper text): “Name collision 20.0 20.0 20.0 20.0 0.0 0.0 Document version 0.0 0.0 0.0 0.0 0.0 0.0 Temporal 100.0 90.0 97.5 100.0 0.0 0.0 Account collision 0.0 0.0 0.0 0.0 0.0 0.0 Near duplicate 0.0 0.0 0.0 0.0 0.0 0.0 Cross-system 20.0 20.0 20.0 20.0 0.0 0.0 True ambiguity 100.0 92.0 100.0 100.0…”
- **released** (paper text): “are publicly available at: https://github.com/R-Suresh/EntityBindingFailures. The repository contains task definitions, evaluation harnesses, and scripts required to reproduce the reported results. R EFERENCES [1] T. Schick, J. Dwivedi-…”

## AmbER (arXiv 2106.06830)

Source: <https://arxiv.org/abs/2106.06830>, fetched 2026-09-30.

- **same-name entities** (abstract): “We define an AmbER set as a collection of entities that share a name along with queries about those entities. By covering the set of entities for polysemous names, AmbER sets act as a challenging test of entity disambiguation. W…”

## When2Call (arXiv 2504.18851)

Source: <https://arxiv.org/abs/2504.18851>, fetched 2026-09-30.

- **call, ask, or admit** (abstract): “when to generate a tool call, when to ask follow-up questions and when to admit the question can't be answered with the tools provided. We find that state-of-the-art tool-calling LMs show significant room for improvement on When2Call, indicating the importance of this b…”

## ToolBeHonest (arXiv 2406.20015)

Source: <https://arxiv.org/abs/2406.20015>, fetched 2026-09-30.

- **three scenarios, 700 samples** (abstract): “missing necessary tools, potential tools, and limited functionality tools. Furthermore, we developed seven tasks and collected 700 evaluation samples through multiple rounds of manual annotation. The results show the significant chal…”
- **700 samples** (abstract): “collected 700 evaluation samples through multiple rounds of manual annotation. The results show the significant challenges presented by the ToolBH benchmark. The current advanced models Gemini…”

## NoisyToolBench (arXiv 2409.00557)

Source: <https://arxiv.org/abs/2409.00557>, fetched 2026-09-30.

- **missed arguments** (abstract): “LLMs tend to arbitrarily generate the missed argument, which may lead to hallucinations and risks. To address this issue, we propose a novel framework, Ask-when-Needed (AwN), which prompts LLMs to ask questions to…”

## ACEBench (arXiv 2501.12851)

Source: <https://arxiv.org/abs/2501.12851>, fetched 2026-09-30.

- **Special category** (abstract): “"Special" evaluates tool usage in situations with ambiguous or incomplete instructions; "Agent" evaluates tool usage through multi-agent interactions to simulate real-world, multi-turn dialogues. We conducted extensive experiments using ACEBench,…”

## UserBench (arXiv 2507.22034)

Source: <https://arxiv.org/abs/2507.22034>, fetched 2026-09-30.

- **underspecified goals** (abstract): “simulated users who start with underspecified goals and reveal preferences incrementally, requiring agents to proactively clarify intent and make grounded decisions with tools. Our evaluation of leading open- and closed-source LLMs reveals a signif…”

## ToolEmu (arXiv 2309.15817)

Source: <https://arxiv.org/abs/2309.15817>, fetched 2026-09-30.

- **68.8% valid; 144 test cases** (abstract): “68.8% of failures identified with ToolEmu would be valid real-world agent failures. Using our curated initial benchmark consisting of 36 high-stakes tools and 144 test cases, we provide a quantitative risk analysis of current LM agents and id…”
- **144 cases** (abstract): “36 high-stakes tools and 144 test cases, we provide a quantitative risk analysis of current LM agents and identify numerous failures with potentially severe outcomes. Notably, even the safest LM agen…”

## MANTRA (arXiv 2605.06334)

Source: <https://arxiv.org/abs/2605.06334>, fetched 2026-09-30.

- **SMT validation** (abstract): “validates their consistency using SMT solving. A structured repair loop resolves inconsistencies, requiring human intervention only as a fallback. %This yields benchmarks that are formally validated. Impor…”
- **285 tasks, 6 domains** (abstract): “we build a new benchmark suite with 285 tasks across 6 domains scaling to 50+ page manuals with minimal human effort. Empirically, we show that the compliance checks are richer with stronger constraint enforcement compared…”

## AutoWebWorld (arXiv 2602.14296)

Source: <https://arxiv.org/abs/2602.14296>, fetched 2026-09-30.

- **FSM-based synthesis** (abstract): “Finite State Machines (FSMs) and use coding agents to translate FSMs into interactive websites. Unlike real websites, where state transitions are implicit, AutoWebWorld explicitly…”

## Fabrication after tool failure (arXiv 2609.14758)

Source: <https://arxiv.org/abs/2609.14758>, fetched 2026-09-30.

- **14.10% dishonest** (abstract): “14.10% of responses are dishonest: the model either asserts a value the payload cannot support or declines while citing a fabricated policy or capability limit. The rate is governed almost enti…”

## ToolFailBench (arXiv 2607.04686)

Source: <https://arxiv.org/abs/2607.04686>, fetched 2026-09-30.

- **categories** (abstract): “We label each trace with Tool-Skip, Result-Ignore, Output-Fabrication, and Unnecessary-Tool-Use, using a rule classifier and two LLM judges aggregated by majority vote. Across 19 headline models, the best reaches 86.33% Clean Tool-Use Rate, showing that f…”

## Repository facts

- **Agent-Diff's evaluation has no closed-world check** (this repository, and upstream `main` fetched from
  <https://raw.githubusercontent.com/agent-diff-bench/agent-diff/main/backend/src/platform/evaluationEngine/assertion.py>
  on 2026-09-30; our `assertion.py` is byte-identical). `backend/src/platform/evaluationEngine/core.py`:
  “`return AssertionEngine(compiled_spec).evaluate(diff.model_dump())`”; `assertion.py`: “`self.strict =
  bool(compiled_spec.get("strict", True))`”, applied only inside `changed` assertions; the engine's README:
  “With `strict=true` (default), only listed fields may change.” No other file in `backend/src` or `sdk` mentions
  unexplained changes.
- **ClawsBench is not released** (GitHub API, <https://api.github.com/repos/benchflow-ai/ClawsBench>, fetched
  2026-09-30): description “Repository for results and data (coming soon!) for ClawsBench”; top-level contents
  `.gitignore`, `LICENSE`, `README.md`, `docs/`, `trajectories/`, `vercel.json`.
- **ClawEnvKit** (local clone of <https://github.com/xirui-li/ClawEnvKit> at `e700344203`, the upstream head, dated
  2026-05-07, checked 2026-09-30): `clawenvkit/llm_client.py`: “Shared LLM client — supports OpenRouter, Anthropic,
  and OpenAI.” and reads `OPENAI_BASE_URL`; `clawenvkit/generate/task_generator.py` defines `SERVICE_DEFINITIONS`.
- **EnvScaler's prompts** (<https://github.com/RUC-NLPIR/EnvScaler/tree/main/scen_generator>, fetched 2026-09-30):
  quoted above from `step1_gen_env_config.py`, `step2_gen_scenario_task.py`, `task_check_util/gen_checklist.py` and
  `task_check_util/gen_check_func.py`.
- **AppWorld ships an MCP server** (<https://github.com/stonybrooknlp/appworld>, README fetched 2026-09-30): section
  “Introducing AppWorld MCP Server and Client”.
- **BFCL's multi-turn categories** (<https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html>, fetched
  2026-09-30): Missing Parameters: “Tests the model's ability to recognize when essential information is missing from
  the user request.” Missing Functions: “Requires the model to identify that no available function can fulfill the
  user request.” State-based evaluation: “comparing the backend system's state after all function calls are executed
  at the end of each turn.”

## The PI's own evidence (unpublished)

- `~/PyProj/mcp-bench/specops_tests/audit/overall_report.md`: the headline table (Empty 5 TP / 601 FP, 0.83%;
  Random 14 / 565, 2.42%; Representative 51 / 451, 10.16%) and the Level-3 false-positive accounting (245, 142, 36,
  23, 5).
- `~/PyProj/mcp-bench/logs/judge_robustness_2026-08-03/README.md`: “the same Indianapolis-timezone error was scored
  "critical error", "valid parameter", and "acceptable for fuzzy task" in three different judge invocations.”
- `~/PyProj/baseline_study/baseline_audit_results.md` (ClawEnvKit section): “a local probe with `send_email` logged at
  status 500 scored completion `1.0` and final score `0.8`”, and the `calendar-028` rubric that “can therefore reward
  the wrong answer”.
