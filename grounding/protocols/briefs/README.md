# Session briefs

One file per Claude Code session that the lead session ("RoadMap specialist") starts. Each brief states the
session's question, materials, steps and deliverable. The rules below apply to every session.

## Before you start

1. Read [grounding/AGENTS.md](../../AGENTS.md), then [the PI's notes of 2026-09-29](../brain_dump_2026-09-29.md)
   (the research goal and what the PI decided that day), then the [roadmap](../roadmap.md). Skim the concise report,
   [report_concise.md](../../runs/report_01/report_concise.md), for the numbers.
2. Read the study READMEs your brief names. Do not read every study.
3. State your investigation question in your README before running anything. Ask "how can we", not "can we".

## How to work

- **Iterate.** Learning comes from build, run, analyze, repeat. Keep a log of every cycle: what changed, what ran,
  what was learned. Stop when the question is answered with evidence, not when a report exists.
- **Manual means you.** Reviews, labels and adjudications done by you count as manual work. Label blind samples
  before reading any verdict, and keep the labels apart from anything an agent reads.
- **Keep apart:** test validity, test difficulty, solver failures and judge errors. Report denominators.
- **The PI's standing rules:**
  - flawed is flawed: a flawed test is left out of results and counted as flawed, whenever it was found;
  - natural ambiguity is part of a test: misreading a natural request is the agent's failure;
  - a solver that runs out its time budget has failed (10 minutes on OpenClaw; 480 s in the toy harness); never
    re-run it; re-run only infrastructure errors;
  - replica defects are reported, never fixed; void what they break and move on;
  - our notes never go into what agents are instructed;
  - existing prompts and pipeline code are not changed without discussing it with the lead first; small fixes of
    known defects are fine.
- **No blanket rules for verdicts.** When a case is unusual, look at the case: what was asked, what was done, whether
  it was authorized, what it left behind. Record the reasoning.

## Resources and limits

- **Python:** run pipeline kits with the backend venv through the launcher:
  `python grounding/runs/fact_coverage_02/launch.py <module> ...` (other Pythons lack psycopg2 and starlette).
- **Muse (writer, reader, judge):** through the existing pipeline code only. Spend cap per session: **$5 billed**
  unless your brief says otherwise. Record every call (requests, responses, usage), as the pipeline does.
- **The self-hosted Qwen:** only through `SOLVER_BACKEND=selfhost` and the launcher, and only after the lead says it
  is up. **Never run `qwen up` or `qwen down`.** Concurrency at most **24** per session; the shared limiter stays on.
- **Purdue's Qwen (20 requests a minute):** reserved for the judge session.
- **The OpenAI subscription:** reserved for the lead's solver runs. A harness smoke test may use at most 10 requests.
- **The Claude subscription** runs you. Sonnet smoke tests through Claude Code are fine.
- **Muse judge verdicts** of the final runs already exist; reuse them, don't re-judge.

## Repository conventions

- Work in your own worktree and branch (the launcher created them). Commit your own study folder only:
  `grounding/runs/<your_study>/`. Do not edit the roadmap, the notes file, report_01, other studies, the replicas or
  the frozen pipeline.
- Keep raw run evidence, but add a `.ignore` file in your study folder that hides run folders from ripgrep, as the
  other studies do. Don't commit anything over 1 MB without checking `.gitattributes`.
- Write a fresh commit message every time. Stage large result folders path by path if `git add` hits an index lock.
- Your README opens with a **Status** section (date, what is done, what is running, what is blocked) that you keep
  current. The lead reads it.

## Talking to the lead and the PI

- The lead session is named **"RoadMap specialist"**. `ListAgents` shows it; use `SendMessage` at milestones, when
  blocked, and when done. Say what you found, not that you are working.
- The PI may join your tmux session and talk to you directly. Their word overrides this brief; note what they said in
  your log.
- When your task is done, report and wait: the lead assigns the next one.
