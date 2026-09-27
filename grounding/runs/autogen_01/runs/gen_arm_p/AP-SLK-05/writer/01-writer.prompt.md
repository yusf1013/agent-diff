Write scenario `AP-SLK-05` for the slack domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Conversation.created_at", "kind": "A", "subkind": "time", "entity": "Conversation", "table": "channels", "field": "created_at", "evidence": "`created`", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "A:WorkspaceMembership.role", "kind": "A", "subkind": "state", "entity": "WorkspaceMembership", "table": "user_teams", "field": "role", "evidence": "profile is_admin/is_owner flags", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "D:member_count", "kind": "D", "meaning": "conversation member count", "mutation": "VIEW", "designated_substitutes": ["members vs posters; off-by-boundary"], "suggested_families": ["F6", "F7", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.