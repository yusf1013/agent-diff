# Slack source map

This is a vocabulary mapping from allowed evidence, not an external ER model and not a description of implementation internals. Local paths and hashes, plus the documentation allowlist, are in [sources.json](sources.json).

| Card/seed vocabulary | API definition or documented projection | Use |
|---|---|---|
| `channels.channel_id`, `channels.channel_name` | `conversations.list` response `id`, `name` | Resolve a named conversation and retain its handle. |
| `channels.is_private`, `channels.is_dm`, `channels.is_archived` | Conversation flags `is_private`, `is_im`, `is_archived`; list `types` filter | Describe populations and channel lifecycle. |
| `channels.topic_text` | Conversation `topic.value`; `conversations.setTopic` input `topic` | Read or set a channel topic. |
| `users.user_id`, `users.real_name`, `users.display_name`, `users.username` | User `id`, `real_name`, `profile.display_name`, `name` | Resolve named people. |
| `users.timezone` | User `tz` | Select timezone-defined participant sets or compute a timezone report. |
| `user_teams.role`, `user_teams.user_id` | Workspace user's `is_admin`/`is_owner` flags and `id` | Map the seed's explicit workspace roles to documented role flags. |
| `channel_members.channel_id`, `channel_members.user_id` | `conversations.members(channel)` returns user IDs; `users.conversations(user)` returns conversations | Resolve member sets or a user's conversation set. |
| `messages.message_id`, `messages.message_text`, `messages.user_id` | History/search message `ts`, `text`, `user` | Identify messages by content, timestamp, or author. |
| `messages.channel_id` | History request channel, or search-result conversation identity | Keep messages associated with their conversation. |
| `messages.parent_id` | Message `thread_ts`; replies endpoint rooted by channel and timestamp | Resolve a root/reply relationship. |
| `messages.blocks` | `chat.postMessage` / `chat.update` input `blocks` | Task-directed structured message content; initial seed records need not contain it. |
| `message_reactions.message_id`, `.reaction_type`, `.user_id` | `reactions.get` message timestamp and `reactions[].name`, `reactions[].users[]` | Identify the actor's existing reaction or construct a new one. |

Channel field mappings are supported by [conversations.list](https://docs.slack.dev/reference/methods/conversations.list/). User identity, profile, timezone and role projections are documented in the [user object](https://docs.slack.dev/reference/objects/user-object/). The latter mapping is between seed vocabulary and the documented meaning of workspace roles; it is not a verified implementation mapping.

Membership projections are documented in [conversations.members](https://docs.slack.dev/reference/methods/conversations.members/). Message relationships and content are supported by [conversations.history](https://docs.slack.dev/reference/methods/conversations.history/), [conversations.replies](https://docs.slack.dev/reference/methods/conversations.replies/), and [search.messages](https://docs.slack.dev/reference/methods/search.messages/). Existing reaction fields are documented in [reactions.get](https://docs.slack.dev/reference/methods/reactions.get/); that documentation specifically includes the authenticated user in the reaction-user projection, which is sufficient for the actor's eyes-reaction obligations here.

The repository's [API definitions](../../examples/slack/testsuites/slack_docs/slack_api_full_docs.json) specify the operations used in the cards: listing/searching/history, user/member retrieval, opening DMs, channel creation/rename/topic/archive/unarchive, membership invitation/removal/join/leave, message posting/editing/deletion, and reaction addition/removal. Generated channel/message handles are outputs of those documented operations; they are not pre-existing referents supplied by an answer key.

Full workspace/current-user scopes come from the test's `info` plus the seed. Identifying alternatives list any additional joined attributes used to select a subject. IDs used solely to report/compare a referent set do not become hidden selection predicates. Pagination is a documented retrieval concern rather than an additional obligation. Permissions, missing runtime defaults, API parity, and operation success are not independently verified by this source-bounded study.
