# Replica issues found in autogen_01 and autogen_02

Every place where the AgentDiff replicas behave unlike the real service, as found in these two studies. Some are in
the replica notes that the writer and the judge read (`inputs/<domain>/replica.md`). The ones marked **new** are
not yet: adding them mid-study would change the judge's input between batches. They go into the notes when this
study's runs are judged. None is fixed in `backend/`.

| Service | Issue | Kind | Found | Effect on tests | Where recorded |
|---|---|---|---|---|---|
| Box | `search` ignores `content_types` | ignored filter | autogen_01 | a trial that trusts the filter acts on what it returns (judged `artifact`) | replica notes |
| Box | **`PUT /files/{id}` without `shared_link` in the body removes the file's shared link.** `api/routes.py` passes `body.get("shared_link")` (None), which `update_file` reads as "remove"; the folder handler uses an UNSET sentinel | bug | **new**: 06:13, a policy trial's state diff | tagging a shared file unshares it; changes no grounding outcome here, but breaks state assertions | report §9 |
| Calendar | `events.list` ignores `eventTypes` | ignored filter | autogen_01 | as above | replica notes |
| Calendar | a fixed clock (2018-06-17); relative days ("on Thursday") are anchored to the seed's week | property | autogen_02 | none; Qwen found the date | report §9 (dates) |
| Linear | `issues(filter: {parent})` and `subscribers` are ignored; `documents(filter: {project: {name}})` is ignored | ignored filter | autogen_01 | as above | replica notes |
| Linear | every `projects` query errors (`searchProjects` works) | gap | autogen_01 | long trials and timeouts: 5 of batch 1's, most of the policy run's 16 | replica notes; report §9 |
| Linear | nested connections fail: `issue { attachments }`, `team { cycles }`, `team { projects }`, `comment { children }` (the top-level queries work) | gap | autogen_01 | as above; a solver that stops at the error has not established anything | replica notes |
| Linear, Box, Slack | no fixed clock: "overdue" and other facts relative to today depend on the run date | property | **new**: 05:33 | G4-LIN-02 is valid only for runs from 09-23 to 09-30 | report §9; `eval/phase4_review.json` |
| Slack | `users.conversations` ignores `types` | ignored filter | autogen_01 | as above | replica notes |
| Slack | `search.messages` matches message text only, not card (`blocks`) text | fidelity question | **new** as an effect (the notes say "matches message text"): 05:45 | a search finds only plain-text near misses of a card condition (G4-SLK-04) | report §6.3 |
| Slack | **`conversations.history` returns thread replies** (with `thread_ts`); real Slack returns only top-level messages and broadcast replies | fidelity | **new**: 05:50, P-G4-SLK-03-I12 t2 | a scenario built on "history without replies" (G4-SLK-03's near miss) does not behave as its writer assumed | this file |

**Also from the runs, not replica issues:** Purdue's effective limit is about 20 requests a minute, signalled as HTTP
400 (memory note `purdue-genai-quirks`).
