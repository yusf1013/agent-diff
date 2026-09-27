Write scenario `AP-LIN-07` for the linear domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:Document.content", "kind": "A", "subkind": "text", "entity": "Document", "table": "documents", "field": "content", "evidence": "Document.content", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:Document.title", "kind": "A", "subkind": "identity", "entity": "Document", "table": "documents", "field": "title", "evidence": "Document.title", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F8", "F1", "F0"]}
{"id": "R:Document.teamId", "kind": "R", "roles": ["Document.teamId"], "meaning": "document's team", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Document.projectId"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.