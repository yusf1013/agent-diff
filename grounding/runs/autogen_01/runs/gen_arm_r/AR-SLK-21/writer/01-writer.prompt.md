Write scenario `AR-SLK-21` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Message.created_at", "kind": "A", "subkind": "time", "entity": "Message", "table": "messages", "field": "created_at", "evidence": "`ts` encodes post time; history oldest/latest filters", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "R:messages.user_id", "kind": "R", "roles": ["messages.user_id"], "meaning": "message author", "mutation": "SUB_OR_DROP", "designated_substitutes": ["reactor of the message (message_reactions)", "member of the message's channel"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "R:messages.channel_id", "kind": "R", "roles": ["messages.channel_id"], "meaning": "message location", "mutation": "SUB_OR_DROP", "designated_substitutes": ["channel the author belongs to", "channel a reactor belongs to"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.