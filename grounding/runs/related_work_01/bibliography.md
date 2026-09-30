# Bibliography

*Every work cited in [report.md](report.md), grouped by the angle of the map. arXiv entries give the first
version's date; titles, authors and dates were fetched from the arXiv API on 2026-09-30.*

**Unpublished, the PI's own:** the MCP-Bench audit on Gmail (`~/PyProj/mcp-bench/specops_tests/audit/overall_report.md`),
the judge-robustness note (`~/PyProj/mcp-bench/logs/judge_robustness_2026-08-03/README.md`), and the July–August
baseline audits (`~/PyProj/baseline_study/baseline_audit_results.md`, `baseline_audit_2.md`, `practical_plan.md`).

## A. Hand-built stateful suites

- **Agent-Diff.** Hubert M. Pysklo, Artem Zhuravel, Patrick D. Watson. *Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation.* arXiv:2602.11224 (2026-02-11). [abs](https://arxiv.org/abs/2602.11224), [code](https://github.com/agent-diff-bench/agent-diff)
- **AppWorld.** Harsh Trivedi, Tushar Khot, Mareike Hartmann, et al. *AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents.* arXiv:2407.18901 (2024-07-26). [abs](https://arxiv.org/abs/2407.18901), [code](https://github.com/stonybrooknlp/appworld)
- **τ-bench.** Shunyu Yao, Noah Shinn, Pedram Razavi, et al. *$τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains.* arXiv:2406.12045 (2024-06-17). [abs](https://arxiv.org/abs/2406.12045), [code](https://github.com/sierra-research/tau-bench)
- **τ²-bench.** Victor Barres, Honghua Dong, Soham Ray, et al. *$τ^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment.* arXiv:2506.07982 (2025-06-09). [abs](https://arxiv.org/abs/2506.07982), [code](https://github.com/sierra-research/tau2-bench)
- **AgentDojo.** Edoardo Debenedetti, Jie Zhang, Mislav Balunović, et al. *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents.* arXiv:2406.13352 (2024-06-19). [abs](https://arxiv.org/abs/2406.13352), [code](https://github.com/ethz-spylab/agentdojo)
- **ToolSandbox.** Jiarui Lu, Thomas Holleis, Yizhe Zhang, et al. *ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities.* arXiv:2408.04682 (2024-08-08). [abs](https://arxiv.org/abs/2408.04682), [code](https://github.com/apple/ToolSandbox)
- **Gaia2 / ARE.** Romain Froger, Pierre Andrews, Matteo Bettini, et al. *ARE: Scaling Up Agent Environments and Evaluations.* arXiv:2509.17158 (2025-09-21). [abs](https://arxiv.org/abs/2509.17158), [code](https://github.com/facebookresearch/meta-agents-research-environments)
- **TheAgentCompany.** Frank F. Xu, Yufan Song, Boxuan Li, et al. *TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks.* arXiv:2412.14161 (2024-12-18). [abs](https://arxiv.org/abs/2412.14161)
- **MCP-Universe.** Ziyang Luo, Zhiqi Shen, Wenzhuo Yang, et al. *MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers.* arXiv:2508.14704 (2025-08-20). [abs](https://arxiv.org/abs/2508.14704)
- **MCPMark.** Zijian Wu, Xiangyan Liu, Xinyuan Zhang, et al. *MCPMark: A Benchmark for Stress-Testing Realistic and Comprehensive MCP Use.* arXiv:2509.24002 (2025-09-28). [abs](https://arxiv.org/abs/2509.24002), [code](https://github.com/eval-sys/mcpmark)
- **Toolathlon.** Junlong Li, Wenshuo Zhao, Jian Zhao, et al. *The Tool Decathlon: Benchmarking Language Agents for Diverse, Realistic, and Long-Horizon Task Execution.* arXiv:2510.25726 (2025-10-29). [abs](https://arxiv.org/abs/2510.25726)
- **Claw-Eval.** Bowen Ye, Rang Li, Qibin Yang, et al. *Claw-Eval: Towards Trustworthy Evaluation of Autonomous Agents.* arXiv:2604.06132 (2026-04-07). [abs](https://arxiv.org/abs/2604.06132)
- **ClawsBench.** Xiangyi Li, Kyoung Whan Choe, Yimin Liu, et al. *ClawsBench: Evaluating Capability and Safety of LLM Productivity Agents in Simulated Workspaces.* arXiv:2604.05172 (2026-04-06). [abs](https://arxiv.org/abs/2604.05172), [code](https://github.com/benchflow-ai/ClawsBench)
- **WebArena.** Shuyan Zhou, Frank F. Xu, Hao Zhu, et al. *WebArena: A Realistic Web Environment for Building Autonomous Agents.* arXiv:2307.13854 (2023-07-25). [abs](https://arxiv.org/abs/2307.13854)

## B. Semi-automated suites

- **WorkBench.** Olly Styles, Sam Miller, Patricio Cerda-Mardini, et al. *WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting.* arXiv:2405.00823 (2024-05-01). [abs](https://arxiv.org/abs/2405.00823)
- **STAGE-Claw.** Sirui Liang, Bohan Yu, Peiyu Wang, et al. *STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios.* arXiv:2606.10394 (2026-06-09). [abs](https://arxiv.org/abs/2606.10394)
- **BFCL.** S. G. Patil, H. Mao, F. Yan, C. C.-J. Ji, V. Suresh, I. Stoica, J. E. Gonzalez. *The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models.* ICML 2025, PMLR 267. [proceedings](https://proceedings.mlr.press/v267/patil25a.html), [leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)

## C. Fully automated benchmark generation

- **MCP-Bench.** Zhenting Wang, Qi Chang, Hemani Patel, et al. *MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers.* arXiv:2508.20453 (2025-08-28). [abs](https://arxiv.org/abs/2508.20453), [code](https://github.com/Accenture/mcp-bench)
- **MCPToolBench++.** Shiqing Fan, Xichen Ding, Liang Zhang, et al. *MCPToolBench++: A Large Scale AI Agent Model Context Protocol MCP Tool Use Benchmark.* arXiv:2508.07575 (2025-08-11). [abs](https://arxiv.org/abs/2508.07575), [code](https://github.com/mcp-tool-bench/MCPToolBenchPP)
- **TaskBench.** Yongliang Shen, Kaitao Song, Xu Tan, et al. *TaskBench: Benchmarking Large Language Models for Task Automation.* arXiv:2311.18760 (2023-11-30). [abs](https://arxiv.org/abs/2311.18760), [code](https://github.com/microsoft/JARVIS/tree/main/taskbench)
- **MCPEval.** Zhiwei Liu, Jielin Qiu, Shiyu Wang, et al. *MCPEval: Automatic MCP-based Deep Evaluation for AI Agent Models.* arXiv:2507.12806 (2025-07-17). [abs](https://arxiv.org/abs/2507.12806)
- **LiveMCPBench.** Guozhao Mo, Wenliang Zhong, Jiawei Chen, et al. *LiveMCPBench: Can Agents Navigate an Ocean of MCP Tools?* arXiv:2508.01780 (2025-08-03). [abs](https://arxiv.org/abs/2508.01780)
- **ClawEnvKit / Auto-ClawEval.** Xirui Li, Ming Li, Ion Stoica, et al. *ClawEnvKit: Automatic Environment Generation for Claw-Like Agents.* arXiv:2604.18543 (2026-04-20). [abs](https://arxiv.org/abs/2604.18543), [code](https://github.com/xirui-li/ClawEnvKit)
- **IntellAgent.** Elad Levi, Ilan Kadar. *IntellAgent: A Multi-Agent Framework for Evaluating Conversational AI Systems.* arXiv:2501.11067 (2025-01-19). [abs](https://arxiv.org/abs/2501.11067), [code](https://github.com/plurai-ai/intellagent)
- **AgentAbstain / AbstainGen.** Xun Liu, Yi Evie Zhang, Vira Kasprova, et al. *AgentAbstain: Do LLM Agents Know When Not to Act?* arXiv:2607.10059 (2026-07-11). [abs](https://arxiv.org/abs/2607.10059)
- **FeasiGen.** Liang Cheng, Mingsheng Cai, Jiuming Jiang, et al. *Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents.* arXiv:2605.28532 (2026-05-27). [abs](https://arxiv.org/abs/2605.28532), [code](https://github.com/LeonChengg/FeasiGen)

## D. Environment and trajectory synthesis

- **Survey: agentic environment engineering.** Jiachun Li, Zhuoran Jin, Tianyi Men, et al. *Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application.* arXiv:2606.12191 (2026-06-10). [abs](https://arxiv.org/abs/2606.12191)
- **EnvScaler.** Xiaoshuai Song, Haofei Chang, Guanting Dong, et al. *EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis.* arXiv:2601.05808 (2026-01-09). [abs](https://arxiv.org/abs/2601.05808), [code](https://github.com/RUC-NLPIR/EnvScaler)
- **AgentScaler.** Runnan Fang, Shihao Cai, Baixuan Li, et al. *Towards General Agentic Intelligence via Environment Scaling.* arXiv:2509.13311 (2025-09-16). [abs](https://arxiv.org/abs/2509.13311)
- **AutoForge.** Shihao Cai, Runnan Fang, Jialong Wu, et al. *AutoForge: Automated Environment Synthesis for Agentic Reinforcement Learning.* arXiv:2512.22857 (2025-12-28). [abs](https://arxiv.org/abs/2512.22857)
- **ScaleEnv.** Dunwei Tu, Hongyan Hao, Hansi Yang, et al. *ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training.* arXiv:2602.06820 (2026-02-06). [abs](https://arxiv.org/abs/2602.06820)
- **LOGIGEN.** Yucheng Zeng, Weipeng Lu, Linyun Liu, et al. *LOGIGEN: Logic-Driven Generation of Verifiable Agentic Tasks.* arXiv:2603.00540 (2026-02-28). [abs](https://arxiv.org/abs/2603.00540)
- **APIGen.** Zuxin Liu, Thai Hoang, Jianguo Zhang, et al. *APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets.* arXiv:2406.18518 (2024-06-26). [abs](https://arxiv.org/abs/2406.18518)
- **APIGen-MT.** Akshara Prabhakar, Zuxin Liu, Ming Zhu, et al. *APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay.* arXiv:2504.03601 (2025-04-04). [abs](https://arxiv.org/abs/2504.03601)
- **ToolACE.** Weiwen Liu, Xu Huang, Xingshan Zeng, et al. *ToolACE: Winning the Points of LLM Function Calling.* arXiv:2409.00920 (2024-09-02). [abs](https://arxiv.org/abs/2409.00920)
- **TaskCraft.** Dingfeng Shi, Jingyi Cao, Qianben Chen, et al. *TaskCraft: Automated Generation of Agentic Tasks.* arXiv:2506.10055 (2025-06-11). [abs](https://arxiv.org/abs/2506.10055)
- **AgentSynth.** Jingxu Xie, Dylan Xu, Xuandong Zhao, et al. *AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents.* arXiv:2506.14205 (2025-06-17). [abs](https://arxiv.org/abs/2506.14205)
- **AutoEnv.** Jiayi Zhang, Yiran Peng, Fanqi Kong, et al. *AutoEnv: Automated Environments for Measuring Cross-Environment Agent Learning.* arXiv:2511.19304 (2025-11-24). [abs](https://arxiv.org/abs/2511.19304)

## E. Agent testing from software engineering

- **Skill Coverage.** Boyin Tan, Xiaowei Huang, Youcheng Sun. *Skill Coverage: A Test Adequacy Metric for Agent Skills.* arXiv:2606.20659 (2026-06-09). [abs](https://arxiv.org/abs/2606.20659)
- **Structural coverage of agentic workflows.** Nafiseh Kahani, Mojtaba Bagherzadeh. *Testing Agentic Workflows with Structural Coverage Criteria.* arXiv:2605.26521 (2026-05-26). [abs](https://arxiv.org/abs/2605.26521)
- **Prompt Coverage Adequacy.** Florian Tambon, Michael Konstantinou, Cedric Richter, et al. *Prompt Coverage Adequacy.* arXiv:2607.02057 (2026-07-02). [abs](https://arxiv.org/abs/2607.02057)
- **ToolFuzz.** Ivan Milev, Mislav Balunović, Maximilian Baader, et al. *ToolFuzz -- Automated Agent Tool Testing.* arXiv:2503.04479 (2025-03-06). [abs](https://arxiv.org/abs/2503.04479)
- **Metamorphic testing and LLMs (survey).** Zheng Zheng, Zenghui Zhou, Yinwang Xu, et al. *Bidirectional Empowerment of Metamorphic Testing and Large Language Models: A Systematic Survey.* arXiv:2605.13898 (2026-05-12). [abs](https://arxiv.org/abs/2605.13898)
- **ARMeta.** Shehroz Khan, Abdullah Mughees, Gaadha Sudheerbabu, et al. *Multi-Agent LLM-based Metamorphic Testing for REST APIs.* arXiv:2605.28321 (2026-05-27). [abs](https://arxiv.org/abs/2605.28321)
- **CheckList.** Marco Tulio Ribeiro, Tongshuang Wu, Carlos Guestrin, et al. *Beyond Accuracy: Behavioral Testing of NLP models with CheckList.* arXiv:2005.04118 (2020-05-08). [abs](https://arxiv.org/abs/2005.04118)

## F. Judges and evaluation

- **Agent-as-a-Judge.** Mingchen Zhuge, Changsheng Zhao, Dylan Ashley, et al. *Agent-as-a-Judge: Evaluate Agents with Agents.* arXiv:2410.10934 (2024-10-14). [abs](https://arxiv.org/abs/2410.10934)
- **AgentRewardBench.** Xing Han Lù, Amirhossein Kazemnejad, Nicholas Meade, et al. *AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories.* arXiv:2504.08942 (2025-04-11). [abs](https://arxiv.org/abs/2504.08942)
- **Online-Mind2Web.** Tianci Xue, Weijian Qi, Tianneng Shi, et al. *An Illusion of Progress? Assessing the Current State of Web Agents.* arXiv:2504.01382 (2025-04-02). [abs](https://arxiv.org/abs/2504.01382)
- **False success.** Laksh Advani. *From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents.* arXiv:2606.09863 (2026-06-01). [abs](https://arxiv.org/abs/2606.09863)

## G. Benchmark-validity audits

- **ABC.** Yuxuan Zhu, Tengjun Jin, Yada Pruksachatkun, et al. *Establishing Best Practices for Building Rigorous Agentic Benchmarks.* arXiv:2507.02825 (2025-07-03). [abs](https://arxiv.org/abs/2507.02825)
- **Are solved issues solved?** You Wang, Michael Pradel, Zhongxin Liu. *Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical Study.* arXiv:2503.15223 (2025-03-19). [abs](https://arxiv.org/abs/2503.15223)
- **HAL.** Sayash Kapoor, Benedikt Stroebl, Peter Kirgis, et al. *Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation.* arXiv:2510.11977 (2025-10-13). [abs](https://arxiv.org/abs/2510.11977)
- **AI Agents That Matter.** Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, et al. *AI Agents That Matter.* arXiv:2407.01502 (2024-07-01). [abs](https://arxiv.org/abs/2407.01502)

## H. Test adequacy for language-to-query

- **Test-suite accuracy for text-to-SQL.** Ruiqi Zhong, Tao Yu, Dan Klein. *Semantic Evaluation for Text-to-SQL with Distilled Test Suites.* arXiv:2010.02840 (2020-10-06). [abs](https://arxiv.org/abs/2010.02840)
- **XData.** Bikash Chandra, Bhupesh Chawda, Biplab Kar, et al. *Data Generation for Testing and Grading SQL Queries.* arXiv:1411.6704 (2014-11-25). [abs](https://arxiv.org/abs/1411.6704)
- **Dr.Spider.** Shuaichen Chang, Jun Wang, Mingwen Dong, et al. *Dr.Spider: A Diagnostic Evaluation Benchmark towards Text-to-SQL Robustness.* arXiv:2301.08881 (2023-01-21). [abs](https://arxiv.org/abs/2301.08881)
- **SQL mutation testing.** J. Tuya, M. J. Suárez-Cabal, C. de la Riva. *Mutating database queries.* Information and Software Technology 49(4):398–417, 2007. [record](https://digibuo.uniovi.es/dspace/handle/10651/29255)
- **XData (journal).** B. Chandra, B. Chawda, B. Kar, K. V. M. Reddy, S. Shah, S. Sudarshan. *Data generation for testing and grading SQL queries.* The VLDB Journal 24:731–755, 2015. [doi](https://doi.org/10.1007/s00778-015-0395-0)
- **MC/DC.** J. J. Chilenski, S. P. Miller. *Applicability of modified condition/decision coverage to software testing.* Software Engineering Journal 9(5):193–200, 1994.

## I. Entity binding in tool agents

- **Entity Binding Failures.** Rahul Suresh Babu, Shashank Indukuri. *Entity Binding Failures in Tool-Augmented Agents.* arXiv:2606.30531 (2026-06-29). [abs](https://arxiv.org/abs/2606.30531), [code](https://github.com/R-Suresh/EntityBindingFailures)
- **AmbER.** Anthony Chen, Pallavi Gudipati, Shayne Longpre, et al. *Evaluating Entity Disambiguation and the Role of Popularity in Retrieval-Based NLP.* arXiv:2106.06830 (2021-06-12). [abs](https://arxiv.org/abs/2106.06830)

## J. Abstention, clarification and feasibility

- **When2Call.** Hayley Ross, Ameya Sunil Mahabaleshwarkar, Yoshi Suhara. *When2Call: When (not) to Call Tools.* arXiv:2504.18851 (2025-04-26). [abs](https://arxiv.org/abs/2504.18851), [code](https://github.com/NVIDIA/When2Call)
- **ToolBeHonest.** Yuxiang Zhang, Jing Chen, Junjie Wang, et al. *ToolBeHonest: A Multi-level Hallucination Diagnostic Benchmark for Tool-Augmented Large Language Models.* arXiv:2406.20015 (2024-06-28). [abs](https://arxiv.org/abs/2406.20015)
- **NoisyToolBench (Learning to Ask).** Wenxuan Wang, Juluan Shi, Zixuan Ling, et al. *Learning to Ask: When LLM Agents Meet Unclear Instruction.* arXiv:2409.00557 (2024-08-31). [abs](https://arxiv.org/abs/2409.00557)
- **ACEBench.** Chen Chen, Xinlong Hao, Weiwen Liu, et al. *ACEBench: Who Wins the Match Point in Tool Usage?* arXiv:2501.12851 (2025-01-22). [abs](https://arxiv.org/abs/2501.12851)
- **UserBench.** Cheng Qian, Zuxin Liu, Akshara Prabhakar, et al. *UserBench: An Interactive Gym Environment for User-Centric Agents.* arXiv:2507.22034 (2025-07-29). [abs](https://arxiv.org/abs/2507.22034)
- **ToolEmu.** Yangjun Ruan, Honghua Dong, Andrew Wang, et al. *Identifying the Risks of LM Agents with an LM-Emulated Sandbox.* arXiv:2309.15817 (2023-09-25). [abs](https://arxiv.org/abs/2309.15817)

## K. Formal-specification-driven synthesis

- **MANTRA.** Ashwani Anand, Ivi Chatzi, Ritam Raha, et al. *MANTRA: Synthesizing SMT-Validated Compliance Benchmarks for Tool-Using LLM Agents.* arXiv:2605.06334 (2026-05-07). [abs](https://arxiv.org/abs/2605.06334)
- **AutoWebWorld.** Yifan Wu, Yiran Peng, Yiyu Chen, et al. *AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines.* arXiv:2602.14296 (2026-02-15). [abs](https://arxiv.org/abs/2602.14296)

## L. Failure diagnostics beyond selection

- **Fabrication after tool failure.** Arham Sethi, Arsen Kenzhebayev, Saanvi Paturi, et al. *Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return.* arXiv:2609.14758 (2026-09-13). [abs](https://arxiv.org/abs/2609.14758)
- **ToolFailBench.** Harsh Soni. *ToolFailBench: Diagnosing Tool-Use Failures in LLM Agents.* arXiv:2607.04686 (2026-07-06). [abs](https://arxiv.org/abs/2607.04686)
- **Progress reporting.** Boyang Wang, Yunhan Wang, Yalun Wu. *The Unreliable Progress Bar: Can LLM Agents Reliably Report Task Progress Throughout Execution?* arXiv:2609.08589 (2026-09-08). [abs](https://arxiv.org/abs/2609.08589)
