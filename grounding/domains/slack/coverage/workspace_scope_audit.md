# Slack multi-workspace scope: source investigation

Read-only repository investigation, 2026-09-16. No live environment or API execution. Repository root: `/home/yusf/PyProj/agent-diff`.

## Conclusion

Multiple workspaces are allowed by the Slack data model and seed/template mechanism. A benchmark environment is an isolated database schema, not intrinsically one Slack workspace. The shipped Slack seeds each contain one workspace, but that is seed content, not a model/platform invariant.

The solver-facing API does not provide a coherent general workspace-selection mechanism. Actor-wide listing, search, and creation use one actor membership selected without ordering; documented `team_id` arguments are ignored. Some channel-ID- or user-ID-addressed operations can nonetheless access other workspaces. Thus neither “all workspace routes are redundant” nor “other workspaces are entirely inaccessible” follows.

## Evidence

- `backend/src/services/slack/database/schema.py:64`: Team is a normal keyed table, with unique names, no singleton constraint.
- `backend/src/services/slack/database/schema.py:75`: channels have nullable workspace FK and uniqueness of `(team_id, channel_name)`, explicitly permitting the same channel name in different workspaces.
- `backend/src/services/slack/database/schema.py:230`: UserTeam has composite `(user_id, team_id)` identity, permitting a user to belong to several workspaces.
- `backend/utils/seed_slack_template.py:50`: insertion iterates all records in each seed table, including `teams` and `user_teams`; no single-workspace restriction.
- `backend/src/platform/isolationEngine/environment.py:304`: cloning copies whole template-table contents via `INSERT ... SELECT *`; no team filter.
- `backend/src/platform/api/models.py:131`: initEnv selects template and impersonated user/email, with no selected Slack workspace field.
- `backend/src/platform/api/middleware.py:143`: requests receive impersonated identity and environment-scoped DB session, not a separate current-workspace setting.
- Both `examples/slack/seeds/slack_bench_default.json` and `slack_default.json` presently contain one Team (`T01WORKSPACE`). This is an observed baseline instance, not a restriction on generated seeds.

## Documentation versus behavior

The primary local API documentation advertises `team_id` on `conversations.create` (line186), `conversations.list` (377), `search.all` (707), `search.messages` (760), `users.conversations` (793), and `users.list` (859), described as workspace selection for org tokens. The implementation reads none of these parameters. The adopted ledger already records this discrepancy under its documentation audit.

`backend/src/services/slack/api/methods.py:767`, `_get_env_team_id`:

- With a channel ID, derives workspace from that actual channel.
- Without a channel ID, selects the first UserTeam row for the given user using `.first()` and **no `ORDER BY`**.
- Therefore multi-membership defaults are not a caller-controlled or documented stable selection. Do not claim the first inserted workspace is guaranteed.

The actor comes from environment impersonation (`methods.py:116`). A different request token does not select a different Slack user/workspace. The dispatched handler set (`methods.py:3170`) contains no workspace list/info/switch operation.

| Operation | Actual workspace behavior | Source |
|---|---|---|
| auth.test | Actor's first membership; synthetic `Workspace {team_id}` name, not Team.team_name | methods.py:2269 |
| conversations.list | Actor's first membership; channels filtered to that workspace; public channels listed regardless of channel membership, other types require membership | methods.py:1036; operations.py:536,582 |
| users.list | Actor's first membership; UserTeam join filters to that workspace | methods.py:2319; operations.py:394 |
| search.messages/search.all | Actor's first membership; only channels returned by list_user_channels in that workspace enter search scope | methods.py:2871,2924,2961,3135 |
| conversations.create | Actor's first membership; supplied team_id ignored | methods.py:981 |
| users.info | Looks up target user by ID globally in the environment, then uses **target user's** first workspace membership; not actor's workspace filter | methods.py:2297 |
| users.conversations | Optional target user; enumerates that user's memberships in **that user's** first workspace | methods.py:2442 |
| conversations.info | Resolves channel globally by ID/name; takes workspace from channel; reports membership but no actor workspace membership check | methods.py:1727 |
| conversations.history | Resolves channel, requires actor channel membership, derives channel workspace, then operations require actor workspace membership; no requirement that workspace equal actor's default | methods.py:1144; operations.py:682 |
| chat.postMessage | Resolves specific channel and checks actor membership in that channel; no actor-default-workspace filter | methods.py:786,817; operations.py:226 |

These are source-derived execution paths, not live-tested claims. In a coherent generated two-workspace seed with the actor a workspace/channel member in both, a known channel ID in the second workspace can support history reading and posting despite global list/search defaulting to only one workspace.

The global name resolver (`methods.py:173`) uses `channel_name == name` with `.scalar_one_or_none()` and no workspace filter. Legal duplicate names across workspaces can consequently cause lookup ambiguity/errors; callers should use IDs returned through a legitimate discovery path rather than relying on names to select workspace.

Workspace names are particularly limited: auth output manufactures its label from workspace ID, and no team.info/list handler exposes actual Team.team_name. Channel responses expose context team IDs; observing IDs is different from being able to enumerate/search arbitrary workspace names or all their records.

## Coverage implications

1. A generated multi-workspace environment is structurally supported; choosing to restrict this campaign to one workspace would be an explicit experimental scope decision, not something forced by the ER model or initEnv.
2. Scope-factorization claims must state the candidate scope: a workspace-dependent suffix can be constant across candidate messages in one fixed workspace, but discriminating across messages from different workspaces.
3. Do not remove workspace paths globally because the historical seed has one team or because default list/search sees one team.
4. Multi-workspace grounding tests need explicit checks that the relevant workspace identity/evidence is discoverable. Known IDs plus memberships can make some cross-workspace tasks feasible; generic enumeration/name-based selection may be a capability-limitation case.
5. Lack of complete workspace enumeration supports an accurate inability response, not a conclusion that other workspaces do not exist.
6. For ordinary-request generation, distinguish workspace identification, within-workspace reference selection, and cross-workspace selection. Do not count a fixed-scope condition repeatedly as different discrimination merely because many roots inherit it; equally, do not collapse it when workspace is allowed to vary.
