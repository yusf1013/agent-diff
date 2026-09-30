# The openai backend's login store: AGENTDIFF_OPENAI_STORE=main

A development task from the lead (2026-09-30), for OpenClaw's openai backend
(`grounding/integrations/openclaw/runtime.py`).

## The problem

The backend copied `~/.openclaw`'s main agent store (`openclaw-agent.sqlite`, which holds the OpenAI login) into the
attempt agent's own directory. That database records its owner (`schema_meta.agent_id = "main"`), and OpenClaw
refuses to open it as another agent. So every `memory_search` failed ("OpenClaw agent database …/agents/assistant/
agent/openclaw-agent.sqlite belongs to agent main; requested agent assistant", in 3 of the Sol pilot's 32 runs),
and the auth failover after a stall failed the same way.

## The change

Off by default. With `AGENTDIFF_OPENAI_STORE=main` in the runner's environment:
- the login store (and the model catalog) is copied to the attempt state's own main agent,
  `<state>/agents/main/agent/`;
- the attempt agent's directory gets no store; OpenClaw creates one owned by the attempt agent;
- OpenClaw finds the login read-through: a secondary agent without a profile reads the main store, which is always
  `agents/main/agent` under `OPENCLAW_STATE_DIR` (`docs/auth-credential-semantics.md`; in the code,
  `loadAuthProfileStoreForRuntime` merges `resolveAuthStorePath()`, which resolves the default agent of an empty
  configuration, `main`);
- the catalog is also copied into the attempt agent's `plugins/openai/`, because model catalogs are read from each
  agent's own directory (`models-config` reads `plugins/<id>/catalog.json` under the agent's directory);
- each attempt's `solver/config.json` records `"openai_store": "main"`.

Without the variable nothing changes: `copy_auth_store(agent_dir)` runs as before and `config.json` has no new key.

## Evidence

- **The default path is byte-for-byte unchanged** ([check_layout.py](check_layout.py) →
  [layout_check.json](layout_check.json), no model call): the committed `runtime.py` and the new one, with the
  variable unset, build the same state directory for the openai backend (every file's bytes; the store compared by
  owner and SQL dump) and the same `openclaw.json`. With the variable set: the main store is owned by `main`, the
  attempt agent has no store, the catalog is in both, the configuration is unchanged.
- **Three runs** (`runs/openai_store_01`, the openai backend, `gpt-6.1-sol`, one trial each, on the three pilot
  tests where Sol called `memory_search` in the Sol pilot: P-G4-CAL-01-I13, P-G4-CAL-07-I13, P-G4-SLK-07-I11):
  - all three completed on `openai/gpt-6.1-sol`: the login was found through the main store;
  - `memory_search` was called in two runs and succeeded in both (`"results": []`, OpenAI embeddings
    `text-embedding-3-small`, no owner error);
  - the kept states ([state_inspection.json](state_inspection.json), counts only, then deleted since they held a
    copy of the login): the main store owned by `main` with 1 profile; the attempt agent's store created by OpenClaw,
    owned by `assistant`, with 0 profiles; the catalog in both.
- **Not exercised:** the auth failover after a stall (no stall happened). It opens the same database, now the
  attempt agent's own.
- **Tests:** `grounding/tests/test_openclaw_eval.py`: 8 pass. The 2 that fail predate this change and do not touch
  the store: `test_selection_applies_the_known_defects` builds a case without `references`, which the rulings now
  read; `test_known_defects_have_a_frozen_suite_action` expects G4-LIN-02's old "keep until 2026-09-30", which the
  test-clock decision of 2026-09-28 replaced with "keep".

## Unchanged risk, checked

As before, a token refresh inside an attempt would write to the attempt's copy, not to `~/.openclaw`. The login
lasts until 2026-10-10 and nothing in a run refreshes it. Checked after the three runs (01:59-02:02 EDT): the real
store `~/.openclaw/agents/main/agent/openclaw-agent.sqlite` was last written 2026-09-29 20:40 and its WAL 22:59;
only the `-shm` index moved (02:06), which every read of the database touches.

## For whoever switches it on

- **Treatment:** with the layout on, `memory_search` returns results instead of an error, and each call makes an
  embeddings request (`text-embedding-3-small`) on the plan. Switch it on at the start of a round, not between the
  trials of one.
- **Records:** a run folder created after this change records a new `runtime.py` hash in its `plan.json`
  (`code_sha256`); existing folders keep theirs, since `write_plan` does not rewrite a plan.
