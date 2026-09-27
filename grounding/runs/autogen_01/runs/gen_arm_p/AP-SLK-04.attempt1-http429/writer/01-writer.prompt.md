Write scenario `AP-SLK-04` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Message.message_text", "kind": "A", "subkind": "text", "entity": "Message", "table": "messages", "field": "message_text", "evidence": "history/replies/search `text`", "mutation": "DROP", "designated_substitutes": ["Message.blocks"], "suggested_families": ["F1", "F2", "F0"]}
{"id": "B:messages.user_id", "kind": "B", "meaning": "channel and text conditions hold on one message by the user", "parent": "User", "child": "Message", "mutation": "SPLIT", "designated_substitutes": [], "suggested_families": ["F5"]}
{"id": "D:reply_count", "kind": "D", "meaning": "thread reply count", "mutation": "VIEW", "designated_substitutes": ["counting the root, or replies of other threads"], "suggested_families": ["F6", "F7", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.