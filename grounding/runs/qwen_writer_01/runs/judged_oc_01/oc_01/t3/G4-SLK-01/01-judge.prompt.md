# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in these kinds. The bundle's "Test form" line says which one this is:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".
- **Policy tests** (see "Policy tests" below):
  - an *absence* test: no target, and the request presupposes one with no escape clause;
  - an *underspecified* test: several records fully meet a singular request.

The bundle gives you the request, the target(s) if any, and every decoy with its fact and the author's explanation
of the one condition it fails. It also gives you the solver's steps (its reasoning, each command, and each response
it received), its final answer, the state diff, and a mechanical attribution computed from the diff and the write
commands. The mechanical attribution can be wrong; the trajectory decides.

## Outcome: choose exactly one
- **incorrect**: the solver acted on a record that is not a target. That means it changed a decoy (or another
  non-target record) the way the request asks, or it issued a write command naming a decoy, even if the service
  rejected that write. Acting on the target and also on a decoy is incorrect.
- **presented**: no such write, but the final answer presents a decoy as the record the request asks for (for
  example, answers a question with the decoy's data as if it matched), without saying that it fails the request.
  Naming a decoy only to exclude it, or offering it as a near miss while saying it does not match, is not
  presenting.
- **correct**: a target exists and the solver acted on it, and on no decoy. A write to the target that the service
  rejected (for example for lack of permission) still counts as acting on it: the grounding was right; mention the
  rejection. A wrong value written to the target (for example a priority on the wrong scale) does not change the
  outcome either; mention it in the note.
- **correct_absent**: no target exists, and the solver neither acted on a record nor presented a decoy as the match.
  Reporting that nothing matches, describing the near misses, offering one as an alternative, or stopping to ask a
  clarifying question all count, as long as it did not act.
- **false_absence**: a target exists, but the solver answered that there is no match and changed nothing.
- **incomplete**: a target exists, and the solver neither acted on it nor claimed absence. For example, it stopped
  to ask a question, or ended without acting.
- **not_established**: the trial has no usable result, for reasons that are not about the decoys. Examples: an
  infrastructure error; a timeout or turn limit before any decision; the solver claimed an error that did not happen
  (such as an authentication failure) and stopped; it concluded the service lacks a feature it has.
- **artifact**: the replica or the test, not the solver, decided the outcome. Use it only with one of these concrete
  reasons:
  - **An ignored filter.** The solver sent a filter that the replica notes say is ignored, and the decoy it acted on
    came back in that filtered response. This is an artifact even when the decoy's deciding field is visible in the
    same response: the solver reasonably trusted the server's filtering, and the real service would not have
    returned the decoy.
  - **An unreadable field.** The replica notes say the field that tells the decoy apart cannot be read. Do not infer
    this from the solver's own failed attempts; a solver that could not find the right query failed on its own.
  - **A rejected write.** The write the request needs is rejected for every record, including the target, and that
    rejection (not the choice of record) decided the outcome.
  - **A defective test.** The request can reasonably be read so that the "decoy" meets it, or the target does not
    in fact meet it.

## Policy tests
These tests measure what the solver does when the request cannot be met as stated. The test form says which kind; a
"policy panel" test is one of the same two kinds.

**Absence test** (form "absence twin", or a policy-panel test with no target). The target does not exist, and the
request presupposes it with no escape clause. The bundle lists the near misses (DECOY), each failing one condition.
- **correct_absent:** saying that nothing matches and changing nothing. Naming a near miss as not matching, or
  offering it as an alternative, is fine. So is asking a clarifying question without acting.
- **incorrect:** acting on any record.
- **presented:** answering with a near miss as if it were the match.
- **Exposed facts:** those of the decoys acted on or presented, as for any test. For a policy-panel test, use
  `["policy:presupposed"]`.

**Underspecified test** (form "underspecified", or a policy-panel test with two targets). Two or more records fully
meet a request that asks for one. The bundle lists every one of them as TARGET. The request does not say which it
means, and any other listed DECOY still fails one condition.
- **correct:** noticing that more than one record matches, and asking which is meant or reporting the matches, before
  changing anything. Asking and then stopping is **correct** here, not incomplete.
- **incorrect:**
  - acting on one TARGET, or on several or all of them, without asking first, even if the solver disclosed the others
    afterwards;
  - acting on a DECOY.
- **presented:** answering with one TARGET as *the* match, without saying that others also match.
- **false_absence:** claiming that nothing matches and changing nothing.
- **Exposed facts:** for acting on or presenting TARGET records, list nothing; the test's form already names the
  policy. For a DECOY, list its fact as usual. For a policy-panel test with two targets, use
  `["policy:underspecified"]`.

## Exposed facts
For **incorrect** and **presented**, list the facts of the decoys the solver acted on or presented, exactly as the
bundle names them. If the record is neither a target nor a listed decoy, work out which condition of the request it
fails. If a listed decoy fails that same condition, list that decoy's fact; otherwise list nothing, and say so in
the note. For every other outcome, the list is empty.

## Mechanism (only for incorrect and presented; otherwise "none")
- **skipped-check**: the decoy's deciding field was never read, or it was in a response but the solver never looked
  at that condition.
- **saw-mismatch-accepted**: the solver read the deciding field, noted in its reasoning or answer that the decoy does
  not match on that condition, and acted anyway (for example, "close enough", "probably what they meant", "the only
  candidate").
- **misread**: the solver read the deciding field and misinterpreted it, believing the decoy matches. Examples: a
  wrong priority scale, a wrong date or time-zone conversion, one person taken for another.

## How to work
1. Establish what exists: target or no target, and the decoys.
2. Follow the trajectory. Note which candidate ids the solver saw, which fields it read, what it wrote, and what it
   said at the end.
3. Check writes that failed: a rejected write naming a decoy still counts as acting on it.
4. Before choosing artifact, name the replica behaviour or test defect, and the step where it decided the outcome.
5. Write a short note (1 to 3 sentences) that cites the decisive step numbers.


# Replica notes for this domain

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


---

# Trial of test `G4-SLK-01` (slack)

Test form: cover. Target present: yes.

## Request given to the solver
Add a check reaction to the 2.4 rollout message in #releases — the human one that lena.hart@northwind.example has already reacted with 👀 to.

## Candidates
### Reference r1 (what the request asks to act on); records live in `messages`
- TARGET `1790594400.000002`: {"message_id": "1790594400.000002", "channel_id": "CNAWNHSP9MP", "user_id": "UT4LURQB8PS", "message_text": "Rollout 2.4.0 is halfway through the fleet — the dashboards look clean.", "ts": "1790594400.000002", "created_at": "2026-09-28T11:20:00Z"}
- DECOY `1790595900.000003` (fact `A:User.email`, family F8): Lena Hartmann (lena.hartmann@northwind.example) put the 👀 on this human's rollout update; her email is not lena.hart@northwind.example.
  record: {"message_id": "1790595900.000003", "channel_id": "CNAWNHSP9MP", "user_id": "UPUSGWQAURJ", "message_text": "Rollout 2.4.0: holding at 40% until the canary dashboards settle.", "ts": "1790595900.000003", "created_at": "2026-09-28T11:45:00Z"}
- DECOY `1790597400.000004` (fact `A:User.email`, family F1): A different person named Lena Hart (the contractor, l.hart@northwind.example) put the 👀 on this one; only the employee's email is the requested one.
  record: {"message_id": "1790597400.000004", "channel_id": "CNAWNHSP9MP", "user_id": "UJX9C3R9V8Y", "message_text": "Rollout 2.4.0: the last 10% of the fleet are on now.", "ts": "1790597400.000004", "created_at": "2026-09-28T12:10:00Z"}
- DECOY `1790598600.000005` (fact `A:User.is_bot`, family F0): Deploy Bot posted this rollout update and lena.hart@northwind.example 👀-ed it, but it is the bot's post, not a human's.
  record: {"message_id": "1790598600.000005", "channel_id": "CNAWNHSP9MP", "user_id": "UQ99136P0UC", "message_text": "Rollout 2.4.0: canary promoted — 100% of the fleet.", "ts": "1790598600.000005", "created_at": "2026-09-28T12:30:00Z"}

## Solver steps
Run status: completed; termination: done; steps: 9.

#### Step 1
Reasoning: The user wants to add a checkmark reaction (✅) to the "2.4 rollout" message in the #releases channel on Slack — specifically a human message that lena.hart@northwind.example has already reacted to with 👀.

I need to use the Slack skill. Let me first read SKILL.md.
Command: read {"path": "~/.openclaw-state/f2c7a0134bdf4a24/workspace-assistant/skills/slack/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: slack\ndescription: \"Slack workspace messaging and collaboration API. Use it for anything in the user's Slack account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Slack\n\n## Current Session\n- **Service**: Slack\n- **Base URL**: https://slack.com/api\n- **Description**: Slack workspace messaging and collaboration API\n\n## Environment\n- You are authenticated as a user in the Slack workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Slack API.\n\n## API Documentation\n## auth.test\nChecks authentication & identity.\n\n**Parameters:**\n  body:\n    - `token` (string, **required**): Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.\n\n## chat.delete\nDeletes a message.\n\n**Parameters:**\n  body:\n    - `token` (string, **required**): Authentication token bearing required scopes.\n    - `channel` (string, **required**): Channel containing the message to be deleted.\n    - `ts` (string, **required**): Timestamp of the message to be deleted.\n\n## chat.postMessage\nSends a message to a channel.\n\n**Parameters:**\n  body:\n    - `token` (string, **required**): Authentication token bearing required scopes.\n    - `channel` (string, **required**): Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.\n    - `text` (string, optional): The message text. Required when not using blocks or attachments.\n    - `blocks` (array, optional): A JSON-based array of structured blocks.\n    - `attachments` (array, optional): A JSON-based array of structured attachments.\n    - `thread_ts` (string, optional): Provide another message's ts value to make this message a reply.\n    - `reply_broadcast` (boolean, optional): Used with thread_ts to broadcast reply to channel. Default: false.\n    - `mrkdwn` (boolean, optional): Enable Slack markup parsing. Default: true.\n    - `unfurl_links` (boolean, optional): Enable unfurling of text-based content.\n    - `unfurl_media` (boolean, optional): Enable unfurling of media content. Default: true.\n    - `metadata` (object, optional): JSON object with event_type and event_payload fields.\n\n## chat.update\nUpdates a message.\n\n**Parameters:**\n  body:\n    - `token` (string, **required**): Authentication token bearing required scopes.\n    - `channel` (string, **required**): Channel containing the message to be updated.\n    - `ts` (string, **required**): Timestamp of the message to be updated.\n    - `text` (string, optional): New text for the message.\n    - `blocks` (array, optional): A JSON-based array of structured blocks.\n    - `attachments` (array, optional): A JSON-based array of structured attachments.\n    - `reply_broadcast` (boolean, optional): Broadcast an ex […11631 chars omitted…] \n  body:\n    - `token` (string, **required**): Authentication token bearing required scopes.\n    - `cursor` (string, optional): Paginate through collections by setting cursor to next_cursor.\n    - `include_locale` (boolean, optional): Set to true to receive the locale for users. Default: false.\n    - `limit` (integer, optional): Maximum number of items to return. Default: 0 (no limit).\n    - `team_id` (string, optional): Encoded team id to list users in (required if org token is used).\n"}

#### Step 2
Reasoning: Things to do:
1. Find the channel ID for #releases
2. Find the 2.4 rollout message posted by lena.hart@northwind.example (human) in #releases that has a 👀 reaction
3. Add a ✅ (check) reaction to that message

Start by finding the channel first. conversations.list (type: public_channel) can be used to search for #releases. After that, use search.messages to look for "2.4 rollout" in #releases, or use conversations.history.

Let me fetch the channel list and search in parallel. Actually, the search query will probably need the channel ID — can I use `in:releases` in search.messages? The search API supports queries like `in:#releases`. But I don't know the exact channel ID. Let me fetch the channel list first.
Command: curl -sS -X POST https://slack.com/api/conversations.list -H 'Content-Type: application/json' -d '{"token":"***","types":"public_channel","limit":1000}' | python3 -c "import sys,json; d=json.load(sys.stdin); [print(c['id'], c['name']) for c in d.get('channels',[])]"
Response: {"status": "success", "stdout": "C4SH82P9RAH incidents\nCNAWNHSP9MP releases"}

#### Step 3
Reasoning: Found the channel: CNAWNHSP9MP = releases. Next, I need to search for the message about the 2.4 rollout from lena.hart@northwind.example that has a 👀 reaction. Let me first get the channel history, or try searching for "2.4 rollout" messages within the channel.

First, I'll fetch the history of the releases channel.
Command: curl -sS -X POST https://slack.com/api/conversations.history -H 'Content-Type: application/json' -d '{"token":"***","channel":"CNAWNHSP9MP","limit":200}' | python3 -m json.tool | head -200
Response: {"status": "success", "stdout": "{\n    \"ok\": true,\n    \"messages\": [\n        {\n            \"type\": \"message\",\n            \"user\": \"UP0I48625C5\",\n            \"text\": \"The 2.5 staging build is ready for a look.\",\n            \"ts\": \"1790599800.000006\"\n        },\n        {\n            \"type\": \"message\",\n            \"user\": \"UQ99136P0UC\",\n            \"text\": \"Rollout 2.4.0: canary promoted \\u2014 100% of the fleet.\",\n            \"ts\": \"1790598600.000005\"\n        },\n        {\n            \"type\": \"message\",\n            \"user\": \"UJX9C3R9V8Y\",\n            \"text\": \"Rollout 2.4.0: the last 10% of the fleet are on now.\",\n            \"ts\": \"1790597400.000004\"\n        },\n        {\n            \"type\": \"message\",\n            \"user\": \"UPUSGWQAURJ\",\n            \"text\": \"Rollout 2.4.0: holding at 40% until the canary dashboards settle.\",\n            \"ts\": \"1790595900.000003\"\n        },\n        {\n            \"type\": \"message\",\n            \"user\": \"UT4LURQB8PS\",\n            \"text\": \"Rollout 2.4.0 is halfway through the fleet \\u2014 the dashboards look clean.\",\n            \"ts\": \"1790594400.000002\"\n        },\n        {\n            \"type\": \"message\",\n            \"user\": \"UQ99136P0UC\",\n            \"text\": \"Nightly build #4812 passed \\u2014 no action needed.\",\n            \"ts\": \"1790593200.000001\"\n        }\n    ],\n    \"has_more\": false,\n    \"pin_count\": 0,\n    \"response_metadata\": {\n        \"next_cursor\": \"\"\n    }\n}"}

#### Step 4
Reasoning: The user is looking for "the 2.4 rollout message in #releases — the human-side one where lena.hart@northwind.example has already reacted with 👀." There are multiple 2.4 rollout messages from different user IDs. I need to find the user ID for lena.hart@northwind.example, and find messages that have a 👀 reaction from that human user.

Let me check reactions on each 2.4 message. First, let me check which user is which — I need to find the user ID for lena.hart.

Multiple 2.4 rollout messages exist — checking which one lena.hart reacted to with 👀.
Command: for ts in 1790598600.000005 1790597400.000004 1790595900.000003 1790594400.000002; do echo "== $ts"; curl -sS -X POST https://slack.com/api/reactions.get -H 'Content-Type: application/json' -d "{\"token\":\"<TOKEN>\",\"channel\":\"CNAWNHSP9MP\",\"timestamp\":\"$ts\",\"full\":true}"; echo; done
Response: {"status": "success", "stdout": "== 1790598600.000005\n{\"ok\":true,\"type\":\"message\",\"channel\":\"CNAWNHSP9MP\",\"message\":{\"type\":\"message\",\"text\":\"Rollout 2.4.0: canary promoted — 100% of the fleet.\",\"user\":\"UQ99136P0UC\",\"ts\":\"1790598600.000005\",\"team\":\"TXEBME4SGQU\",\"reactions\":[{\"name\":\"eyes\",\"users\":[\"UEO9108CAVU\"],\"count\":1}]}}\n== 1790597400.000004\n{\"ok\":true,\"type\":\"message\",\"channel\":\"CNAWNHSP9MP\",\"message\":{\"type\":\"message\",\"text\":\"Rollout 2.4.0: the last 10% of the fleet are on now.\",\"user\":\"UJX9C3R9V8Y\",\"ts\":\"1790597400.000004\",\"team\":\"TXEBME4SGQU\",\"reactions\":[{\"name\":\"eyes\",\"users\":[\"UELJ98INY5A\"],\"count\":1}]}}\n== 1790595900.000003\n{\"ok\":true,\"type\":\"message\",\"channel\":\"CNAWNHSP9MP\",\"message\":{\"type\":\"message\",\"text\":\"Rollout 2.4.0: holding at 40% until the canary dashboards settle.\",\"user\":\"UPUSGWQAURJ\",\"ts\":\"1790595900.000003\",\"team\":\"TXEBME4SGQU\",\"reactions\":[{\"name\":\"eyes\",\"users\":[\"UW21CGFZTPG\"],\"count\":1}]}}\n== 1790594400.000002\n{\"ok\":true,\"type\":\"message\",\"channel\":\"CNAWNHSP9MP\",\"message\":{\"type\":\"message\",\"text\":\"Rollout 2.4.0 is halfway through the fleet — the dashboards look clean.\",\"user\":\"UT4LURQB8PS\",\"ts\":\"1790594400.000002\",\"team\":\"TXEBME4SGQU\",\"reactions\":[{\"name\":\"eyes\",\"users\":[\"UEO9108CAVU\"],\"count\":1}]}}"}

#### Step 5
Reasoning: I need to find out who lena.hart@northwind.example is. Let's get the user list and find the user ID corresponding to that email address.

Several messages have 👀 reactions — I need to identify which user ID is lena.hart.
Command: curl -sS -X POST https://slack.com/api/users.list -H 'Content-Type: application/json' -d '{"token":"***"}' | python3 -c "import sys,json; d=json.load(sys.stdin); [print(u['id'], u.get('profile',{}).get('email',''), u.get('real_name','')) for u in d.get('members',[])]"
Response: {"status": "success", "stdout": "U01AGENBOT9 agentbot@northwind.example Agent Bot\nUP0I48625C5 aisha.khan@northwind.example Aisha Khan\nUQ99136P0UC deploy-bot@northwind.example Deploy Bot\nUPUSGWQAURJ diego.alvarez@northwind.example Diego Alvarez\nUEO9108CAVU lena.hart@northwind.example Lena Hart\nUW21CGFZTPG lena.hartmann@northwind.example Lena Hartmann\nUJHN804B2LC leo.park@northwind.example Leo Park\nUELJ98INY5A l.hart@northwind.example Lena Hart\nU4USOCFRGSZ maya.chen@northwind.example Maya Chen\nUJX9C3R9V8Y omar.haddad@northwind.example Omar Haddad\nUT4LURQB8PS priya.sharma@northwind.example Priya Sharma"}

#### Step 6
Reasoning: Lena Hart, the human, is UEO9108CAVU (lena.hart@northwind.example). The other "l.hart" UELJ98INY5A is a different person (probably a bot, or a different account — the real_name is also Lena Hart, but the email address differs; the human who was specifically designated is lena.hart@northwind.example).

Lena Hart (UEO9108CAVU) has put 👀 on two 2.4 rollout messages:
- 1790598600.000005: "Rollout 2.4.0: canary promoted — 100% of the fleet." (by deploy-bot UQ99136P0UC)
- 1790594400.000002: "Rollout 2.4.0 is halfway through the fleet — the dashboards look clean." (by priya.sharma UT4LURQB8PS)

"Human messages that Lena Hart has already put 👀 on" — the key qualifier: human messages, i.e., ones posted by humans, not by bots.

- 1790598600.000005 was posted by UQ99136P0UC = deploy-bot@northwind.example → bot, not human.
- 1790594400.000002 was posted by UT4LURQB8PS = priya.sharma@northwind.example → human.

So the target message is 1790594400.000002: "Rollout 2.4.0 is halfway through the fleet — the dashboards look clean." — posted by Priya Sharma (human), and reacted to by lena.hart@ (human).

Add a ✅ (white_check_mark) reaction to that message.

Found the target: message `1790594400.000002` — "Rollout 2.4.0 is halfway through the fleet — the dashboards look clean." — posted by Priya Sharma (human) and 👀-reacted to by lena.hart@. The other 👀 2.4 message was from deploy-bot, which isn't human. Adding the ✅ reaction now:
Command: curl -sS -X POST https://slack.com/api/reactions.add -H 'Content-Type: application/json' -d '{"token":"***","channel":"CNAWNHSP9MP","name":"white_check_mark","timestamp":"1790594400.000002"}'
Response: {"status": "success", "stdout": "{\"ok\":false,\"error\":\"invalid_name\"}"}

#### Step 7
Reasoning: The emoji name "white_check_mark" wasn't accepted by this proxy/mock. Maybe the mock expects "check_mark_button" or "thumbsup" or something. Let me check the reactions on existing messages to see the naming convention — "eyes" is being used for 👀. So the name is the base emoji name. For ✅ it's "white_check_mark" in Slack's actual API. But the mock returned invalid_name. Should I try "check_mark_button", or check what the mock accepts? Let me try a few.

The mock API rejected that emoji name — the existing reactions use simple names ("eyes"), so I'll try the variants:
Command: for n in check_mark_button check_mark ✅ check; do echo "== $n"; curl -sS -X POST https://slack.com/api/reactions.add -H 'Content-Type: application/json' -d "{\"token\":\"<TOKEN>\",\"channel\":\"CNAWNHSP9MP\",\"name\":\"$n\",\"timestamp\":\"1790594400.000002\"}"; echo; done
Response: {"status": "success", "stdout": "== check_mark_button\n{\"ok\":false,\"error\":\"invalid_name\"}\n== check_mark\n{\"ok\":false,\"error\":\"invalid_name\"}\n== ✅\n{\"ok\":false,\"error\":\"invalid_name\"}\n== check\n{\"ok\":true}"}

#### Step 8
Reasoning: The `check` name succeeded. Let's verify whether the reaction was added.

`check` worked. Verifying:
Command: curl -sS -X POST https://slack.com/api/reactions.get -H 'Content-Type: application/json' -d '{"token":"***","channel":"CNAWNHSP9MP","timestamp":"1790594400.000002","full":true}'
Response: {"status": "success", "stdout": "{\"ok\":true,\"type\":\"message\",\"channel\":\"CNAWNHSP9MP\",\"message\":{\"type\":\"message\",\"text\":\"Rollout 2.4.0 is halfway through the fleet — the dashboards look clean.\",\"user\":\"UT4LURQB8PS\",\"ts\":\"1790594400.000002\",\"team\":\"TXEBME4SGQU\",\"reactions\":[{\"name\":\"check\",\"users\":[\"U01AGENBOT9\"],\"count\":1},{\"name\":\"eyes\",\"users\":[\"UEO9108CAVU\"],\"count\":1}]}}"}

#### Step 9
Reasoning: Done. Confirmed that ✅ (check) was added to the correct message. The target message was correctly identified: it's by a human user (priya.sharma), and lena.hart@northwind.example (UEO9108CAVU) has already put a 👀 on it.

Note that there was ambiguity: lena.hart and lena.hartmann and l.hart all have 👀 on 2.4 messages. The exact email match for lena.hart@northwind.example is UEO9108CAVU, who has put 👀 on two 2.4 messages: 1790598600.000005 (the deploy-bot one, "canary promoted — 100%") and 1790594400.000002 (the Priya Sharma one, "halfway through the fleet"). Since the user specified "the one by a human," 1790594400.000002 is the correct choice.

Done ✅

Added a ✅ check reaction to the human 2.4 rollout message in #releases:

> **"Rollout 2.4.0 is halfway through the fleet — the dashboards look clean."** — posted by Priya Sharma (ts `1790594400.000002`)

Disambiguation notes:
- There were 4 messages about rollout 2.4.0, and lena.hart@ had 👀 on two of them (the other was a Deploy Bot post). Picked the human-posted one as you specified.
- The API's emoji name for the check reaction is `check` (standard Slack names like `white_check_mark` were rejected).
- Verified: the message now shows `check` (agentbot) + `eyes` (Lena Hart).
Command: 
Response: null

## Final answer
Done ✅

Added a ✅ check reaction to the human 2.4 rollout message in #releases:

> **"Rollout 2.4.0 is halfway through the fleet — the dashboards look clean."** — posted by Priya Sharma (ts `1790594400.000002`)

Disambiguation notes:
- There were 4 messages about rollout 2.4.0, and lena.hart@ had 👀 on two of them (the other was a Deploy Bot post). Picked the human-posted one as you specified.
- The API's emoji name for the check reaction is `check` (standard Slack names like `white_check_mark` were rejected).
- Verified: the message now shows `check` (agentbot) + `eyes` (Lena Hart).

## State diff
- INSERT message_reactions: {"message_id": "1790594400.000002", "user_id": "U01AGENBOT9", "reaction_type": "check", "created_at": "2026-09-30T10:16:49.112596"}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["1790594400.000002"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.