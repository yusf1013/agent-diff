# Muse's verify-reminder off for judge and reader: the check

**The change** (`grounding/runs/autogen_01/kit/agent.py`, `_muse_settings`). Judge and reader sessions run with an
empty reminder roster. A `settings.json` in the session's home holds it:

```json
{"schema_version": 1, "run": {"reminder_roster": {"agents": []}}}
```

- **Why:** in autogen_02, all 4,883 of the judge and reader calls' reminder decisions were "no reminder", and no judge
  or reader session took a second step. The reminders still cost $1.98 of the study's $9.45 billed.
- **The writer keeps Muse's default,** since its reminder fired 9 times.
- **To restore the default** for every role, set `AUTOGEN_MUSE_NO_REMINDER_ROLES=""`.

**Finding the syntax, offline.** [scripts/muse_echo_probe.py](scripts/muse_echo_probe.py) runs `muse exec
--provider echo` in a bubblewrap sandbox with no network and no key. The default session links both reminders
(`skill-reminder`, `verify-reminder`). With the file above, the roster's source is `settings`, it has no agents, and
no reminder starts. The file needs `schema_version`; without it, Muse refuses to start.

**The check (approved by the PI; 2026-09-27, 15:52–15:58).** Judge v2 re-judged batch 1's 30 blind-labelled trials
([trials.json](trials.json)) with reminders off, into [judged/](judged/).
- **The passes:** the first pass ran with a Python that lacked `psycopg2`, so 12 Calendar and Linear bundles failed
  before any Muse call. The second pass used the bedrock-llm virtualenv and still lacked `starlette` for 4 Calendar
  bundles. The third used the backend's virtualenv, the environment of the earlier runs. Cached verdicts were kept,
  so each trial was judged exactly once ([run.log](run.log), [run_pass2.log](run_pass2.log),
  [run_pass3.log](run_pass3.log)).
- **Results** ([judged/comparison_with_reminders_on.json](judged/comparison_with_reminders_on.json),
  [judged/comparison_batch1_blind_reminders_off.json](judged/comparison_batch1_blind_reminders_off.json)):

| | Reminders on (autogen_02) | Reminders off |
|---|---:|---:|
| Agreement with my blind labels | 30/30 | 30/30 |
| Same verdict as before: outcome, exposed facts, records acted on, mechanism | – | 30/30 on each |
| Input tokens (cached) | 985,511 (244,677) | 760,223 (37,346) |
| Output tokens | 76,119 | 31,996 |
| Cost, list / billed | $1.29 / $0.090 | $1.05 / $0.079 |
| Median seconds per call | 40 | 12 |

- **Reading the cost line:** input fell by 23% and output by 58%. The billed saving here (12%) is smaller than the 21%
  estimated from the whole study, because this run happened to get fewer cache hits (5% of input against 25%).
  Whether a fresh session finds Muse's fixed prefix in the cache is a coin flip (see the Muse cache analysis of
  2026-09-27).
