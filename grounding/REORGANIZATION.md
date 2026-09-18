# Reorganization verification — 2026-09-18

Parent revision: `2725afdd049dbbd7c69465ca049232262b62c859`. This is a location/import/layout change, not a new generation or evaluation experiment.

- Moved 37,093 tracked files into the component directories listed in [README.md](README.md). AgentDiff's backend, SDK, examples, dataset and operations directories are unchanged.
- Compared every moved file with its pre-move SHA256: no missing files; no changes to raw run records or reference-label JSON. Human documentation links and Python source paths/imports were updated. Historical internal run layouts are retained.
- Preserved all 2,187 reference JSON files byte-for-byte; all 59 reference assessments pass the existing mechanical validator, and their bound original solver-run hashes still match using the [path mapping](relocation.json).
- Verified all assembled current writer assignments, compiler/reviewer systems and mode instructions, and reflection text against pre-move assembly. The only instruction-context text differences are three relocated Markdown link targets in the adopted domain model.
- Ran 85 offline tests: 83 passed; two opt-in full runtime tests skipped because the HTTP backend was not running. Tests cover new/legacy artifact lookup, compilation stage directories, execution output routing, accounting, validators, and exact repair-history preservation.
- Native W01 load/read check passed against the local PostgreSQL service: two intended matches, 19 API probes, no probe errors, certified selector visibility and unchanged state. This used in-process Slack handlers, no HTTP backend, sandbox, solver, or model. It does not test requested writes.
- All active command entry points passed `--help` with their stage dependencies. W01 compiler and evaluator requests were prepared without API calls. Annotation projection checks passed for Slack (59 tests, 198 cards), Box (48 tests, 99 cards), and Linear (57 tests, 143 cards). The shared renderer now computes links relative to its output directory, preserving the old location used by untracked Calendar work.
- Preserved the Git LFS treatment of all 10 moved files larger than 1 MiB. Also relocated 188 ignored local run logs, without adding them to Git.

No paid model calls were made. Solver/evaluator verdicts, acceptance gates, retry policy and token limits were not changed. The writer default now explicitly selects the already-used current prompt version instead of the stale v3 default. Legacy v3 prompts remain in the archive.

Pre-existing untracked work (other-domain drafts, the native failure audit, the v3 exemplar draft and behavioral model) was left untouched. The user's existing deletion of `GROUNDING_OBLIGATIONS_ONBOARDING.md` was not staged; maintained documentation now points to the current card-extraction protocol.

Some historical review links already referenced files absent from the checkout: the ten-case `runs/usage_ledger.jsonl`, one workflow-variant answer text, and three `assessment-change.diff` files. This move does not invent or regenerate that missing evidence. Recorded original paths can be looked up with `python -m grounding.paths OLD_PATH`.

New experiments should use the [current generation commands](generation/README.md) and [stage-separated artifact layout](runs/README.md). Historical source scripts and prompt versions are in [archive](archive/README.md); they retain earlier workflow assumptions and are not the default launch path.
