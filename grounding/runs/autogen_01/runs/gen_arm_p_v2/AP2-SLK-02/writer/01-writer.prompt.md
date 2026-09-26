Write scenario `AP2-SLK-02` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Conversation.channel_name", "kind": "A", "subkind": "identity", "entity": "Conversation", "table": "channels", "field": "channel_name", "evidence": "conversations.list/info `name`", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F8", "F1", "F0"]}
{"id": "A:Conversation.topic_text", "kind": "A", "subkind": "text", "entity": "Conversation", "table": "channels", "field": "topic_text", "evidence": "topic.value", "mutation": "DROP", "designated_substitutes": ["Conversation.purpose_text"], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:Conversation.is_archived", "kind": "A", "subkind": "state", "entity": "Conversation", "table": "channels", "field": "is_archived", "evidence": "`is_archived`", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.