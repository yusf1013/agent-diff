Write scenario `AP-BOX-02` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:File.created_at", "kind": "A", "subkind": "time", "entity": "File", "table": "box_files", "field": "created_at", "evidence": "file full/item", "mutation": "DROP", "designated_substitutes": ["File.modified_at"], "suggested_families": ["F7", "F6", "F1", "F0"]}
{"id": "A:Comment.created_at", "kind": "A", "subkind": "time", "entity": "Comment", "table": "box_comments", "field": "created_at", "evidence": "comment dict", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F6", "F1", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.