Write scenario `AP-SLK-03` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Reaction.reaction_type", "kind": "A", "subkind": "state", "entity": "Reaction", "table": "message_reactions", "field": "reaction_type", "evidence": "reactions.get name", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "R:message_reactions", "kind": "R", "roles": ["message_reactions.message_id", "message_reactions.user_id"], "meaning": "user reacted to message", "mutation": "SUB_OR_DROP", "designated_substitutes": ["authored the message", "reacted to another message in the same channel"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "B:message_reactions.user", "kind": "B", "meaning": "message and emoji conditions hold on one reaction by the user", "parent": "User", "child": "Reaction", "mutation": "SPLIT", "designated_substitutes": [], "suggested_families": ["F5"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.