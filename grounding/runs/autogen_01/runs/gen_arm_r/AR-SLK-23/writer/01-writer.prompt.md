Write scenario `AR-SLK-23` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Conversation.purpose_text", "kind": "A", "subkind": "text", "entity": "Conversation", "table": "channels", "field": "purpose_text", "evidence": "purpose.value", "mutation": "DROP", "designated_substitutes": ["Conversation.topic_text"], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:Conversation.is_private", "kind": "A", "subkind": "state", "entity": "Conversation", "table": "channels", "field": "is_private", "evidence": "is_private/is_group", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.