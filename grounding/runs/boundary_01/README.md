# boundary_01

*A pilot, superseded by [../boundary_02](../boundary_02) (2026-09-28). It is a sample from a coverage space that was
never defined.*

Roadmap step 5, third investigation: when a request asks for something the service does not allow, does the agent
say so? The alternatives are acting on a nearby record, making changes nobody asked for, or claiming a success that
did not happen. The pilot has 10 cells (limit class × service), each with an impossible request and a near
control. It ran on the self-hosted Qwen, at 3 trials per test.

- **Start with:** [report.md](report.md), then [plan.md](plan.md).
- **Result:**
  - Qwen reports a limit when nothing gets around it.
  - It takes a workaround with a side effect, every time and disclosed, when one exists: a personal calendar name,
    unarchiving a channel, moving a state's issues.
  - It never touched a decoy and never claimed a false success. The controls all succeed.
- **Of the 42 facts the replicas cannot serve,** only the 4 Calendar sharing-rule facts are a real limit.

Reproduce, from the repository root:

```bash
python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_01.probe_replica    # probes.json (local replica)
python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_01.tests            # cases/
python grounding/runs/fact_coverage_02/launch.py grounding.runs.boundary_01.check_controls   # controls_check.json
SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_02.kit.solve \
    --cases-dir grounding/runs/boundary_01/cases --out grounding/runs/boundary_01/runs/NEW --trials 3 --concurrency 10
python grounding/runs/boundary_01/digest.py grounding/runs/boundary_01/runs/NEW                # digest.json
python grounding/runs/boundary_01/grades.py                                                   # grades.json (hand grades)
```
