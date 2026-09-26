Write scenario `AR-SLK-22` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "R:messages.user_id", "kind": "R", "roles": ["messages.user_id"], "meaning": "message author", "mutation": "SUB_OR_DROP", "designated_substitutes": ["reactor of the message (message_reactions)", "member of the message's channel"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "H:messages.parent_id", "kind": "H", "roles": ["messages.parent_id"], "meaning": "thread: root message vs direct replies", "mutation": "LEVEL", "designated_substitutes": ["reply taken for the root (or root for a reply); replies of another thread"], "suggested_families": ["F4", "F2"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.