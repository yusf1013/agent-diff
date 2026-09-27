# Role: author of a second matching record

You add one record to the seed data of a grounding test. A grounding test gives an AI assistant a request in plain
language against a work service (Box, Google Calendar, Linear or Slack). The request asks for one record, and exactly
one record in the seed (the target) fits it. The test you help build checks what the assistant does when **two**
records fit a request that asks for one.

**Your job:** describe a second record, a copy of the target, that also fits every condition of the request and
differs from the target only where the request does not care: its name or title, and the fields that must be
unique. The code copies the target, applies your changes, copies the rows that point at the target (for example its
comments or attendees) with every reference to the target moved to the copy, and checks that the request's conditions
select exactly the two records.

## Rules
1. **Every condition of the request must still hold for the copy.** You may change a field that a condition uses
   only if the new value still clearly meets that condition (for example, a new title that still contains the words
   the request uses).
2. **Give it a different, plausible name or title** of the same kind as the target's, for a record that could
   really sit next to the target in this workspace. It must not repeat the request's wording in a way that would make
   it look like the intended record, and it must not fail any condition. If the record has no name or title, or the
   request uses it, make the copy differ in another field that the request does not use (for example, the record it
   is attached to), keeping it plausible.
3. **Give every unique field a new value** in the record's own conventions: its id (the key), and identifiers,
   numbers, slugs, URLs, uids, etags, timestamps used as ids. Keep them consistent with each other (for example a
   Linear issue's identifier, number, branch name and URL; a Slack message's ts and its creation time).
4. **Say when it is not possible.** Sometimes the service does not allow two such records, because a value that the
   service keeps unique is itself one of the request's conditions. Then answer `possible: false` and explain. Judge
   only whether such a copy can exist and fit every condition: the wording of the request is checked separately.
5. Touch nothing else. Other records stay as they are.

## Input
- The request, the service, and the conditions as a tree.
- The target record, and a few other records of the same table (for their conventions).
- The rows that point at the target (the code copies them, giving each a new key).
- The replica notes for the domain.

## Output
- `possible`, and `reason` (one or two sentences).
- `new_key`: the copy's key value.
- `changes`: every field you change besides the key, as `field` and `value` (write the value as JSON: a string in
  quotes, a number, true or false).
- `skip_children`: tables whose rows pointing at the target should not be copied, if copying them would break
  something (for example, rows keyed by a timestamp that must stay unique). Usually empty.


---

Service: Slack.

Request:
> Invite to #incident-response whoever posted the message in #incidents about the deploy freeze that got 4 replies.

Conditions of the request:
Records of `users`, where:
  - at least one record of `messages` linked by `user_id` eq `messages.user_id`, where:
    - `channel_id` = "C_INC"
    - `message_text` contains_ci "deploy freeze"
    - a number = 4 of records of `messages` linked by `message_id` eq `messages.parent_id`

The target record (table `users`, key `user_id`):
{"user_id": "U_DIEGO", "username": "diego.alvarez", "email": "diego.alvarez@northwind.example", "real_name": "Diego Alvarez", "display_name": "Diego", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}

Other records of `users`, for their conventions:
{"user_id": "U01AGENBOT9", "username": "agentbot", "email": "agentbot@northwind.example", "real_name": "Agent Bot", "display_name": "AgentBot", "created_at": "2025-01-01T00:05:00Z", "is_bot": true, "is_active": true}
{"user_id": "U_PRIYA", "username": "priya.sharma", "email": "priya.sharma@northwind.example", "real_name": "Priya Sharma", "display_name": "Priya", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_LEO", "username": "leo.park", "email": "leo.park@northwind.example", "real_name": "Leo Park", "display_name": "Leo", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_OMAR", "username": "omar.haddad", "email": "omar.haddad@northwind.example", "real_name": "Omar Haddad", "display_name": "Omar", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}
{"user_id": "U_AISHA", "username": "aisha.khan", "email": "aisha.khan@northwind.example", "real_name": "Aisha Khan", "display_name": "Aisha", "created_at": "2025-01-01T00:05:00Z", "is_bot": false, "is_active": true}

Keys already used in `users` (the copy needs a new one): U01AGENBOT9, U_PRIYA, U_DIEGO, U_LEO, U_OMAR, U_AISHA, U_MAYA

Rows that point at the target (copied with the target):
`messages`:
{"message_id": "1789052400.000001", "channel_id": "C_INC", "user_id": "U_DIEGO", "message_text": "Are we still under the deploy freeze until Friday?", "type": "message", "ts": "1789052400.000001", "created_at": "2026-09-10T15:00:00Z"}
{"message_id": "1789052700.000002", "channel_id": "C_INC", "user_id": "U_DIEGO", "message_text": "Following up since I haven't heard back.", "type": "message", "ts": "1789052700.000002", "created_at": "2026-09-10T15:05:00Z", "parent_id": "1789052400.000001"}
{"message_id": "1789052820.000003", "channel_id": "C_INC", "user_id": "U_DIEGO", "message_text": "Bumping this again.", "type": "message", "ts": "1789052820.000003", "created_at": "2026-09-10T15:07:00Z", "parent_id": "1789052400.000001"}
{"message_id": "1789053000.000004", "channel_id": "C_INC", "user_id": "U_DIEGO", "message_text": "Never mind, found the announcement.", "type": "message", "ts": "1789053000.000004", "created_at": "2026-09-10T15:10:00Z", "parent_id": "1789052400.000001"}
{"message_id": "1789053120.000005", "channel_id": "C_INC", "user_id": "U_DIEGO", "message_text": "Confirmed with the release team, we're still frozen.", "type": "message", "ts": "1789053120.000005", "created_at": "2026-09-10T15:12:00Z", "parent_id": "1789052400.000001"}
`channel_members`:
{"channel_id": "C_INC", "user_id": "U_DIEGO", "joined_at": "2026-01-05T09:05:00Z"}
`user_teams`:
{"user_id": "U_DIEGO", "team_id": "T1", "role": "member"}

Replica notes:

# Slack replica: how it differs from real Slack, and its constraints

This replica is what the agent under test talks to. Where it differs from the real service, the replica decides.

## Reads
- **`conversations.history` returns every message of the channel, thread replies included.** Real Slack leaves
  replies out. `conversations.replies` returns a thread (its root first).
- **`conversations.list`** lists every channel the actor can see (with `is_private`, topic, purpose, created,
  `is_archived`). With few channels, the agent usually lists them all.
- **Messages** carry `user` (a user id), `text`, `ts`, `thread_ts` for replies, and their `reactions`. Names need
  `users.info` or `users.list` (username, real name, display name, email, title, timezone, is_bot, deleted).
- **`search.messages`** matches message text and supports `from:@user` and `in:#channel`.
- **`users.conversations`** lists a user's channels; `conversations.members` a channel's members.
- `reactions.get` returns one message's reactions.

## Values
- A message's id is its `ts` (epoch seconds with a sequence suffix). The agent sees `ts`, not a date; converting it
  to a local day is its job. Seeds give each message a `created_at` instant that matches its `ts`.

## Writes
- `reactions.add` accepts only these names: raised_hands, bow, thumbsup, thumbsdown, clap, tada, dart, joy, +1, -1,
  eyes, heart, fire, rocket, check, x, wave, pray, thinking, shrug, facepalm, grimacing, sweat_smile, zzz, coffee,
  pizza, finish_flag, blob_smiley, alert, mic-drop, cool-doge, thankyou, party_blob, partyparrot, this_is_fine,
  extreme-teamwork, done, loading, huh, dumpster-fire, blob-yes, blob-no, blob_help, chefs-kiss, troll, 1000,
  catjam, keanu-thanks, art, honey_pot, sunrise. Any other name (for example `white_check_mark`) is rejected.
- `chat.postMessage` (with `thread_ts` to reply), `chat.update`, `chat.delete`, `conversations.setTopic`,
  `conversations.invite`, `conversations.kick`, `conversations.archive`, `conversations.rename` work as in Slack.
- The actor is a bot user that is a member of every seeded channel.

## Seeds
- The actor is `U01AGENBOT9` (Agent Bot). People by default: Priya Sharma, Diego Alvarez, Leo Park, Omar Haddad,
  Aisha Khan, Maya Chen (ids `U_<FIRST NAME>`), usernames like `priya.sharma`.

## Gaps found by autogen_01 (added for autogen_02)
- **`users.conversations` ignores `types`.** Asking for a user's private channels returns their public channels too.
  The response still shows each channel's `is_private`. A near miss returned by such a query came from the ignored
  filter.
- **Group DMs are reported as private** (`is_private: true` for a group DM), as in Slack.


Describe the copy, following the rules.