Write scenario `AR-BOX-23` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:File.description", "kind": "A", "subkind": "text", "entity": "File", "table": "box_files", "field": "description", "evidence": "file full; search", "mutation": "DROP", "designated_substitutes": ["File.tags"], "suggested_families": ["F1", "F2", "F0"]}
{"id": "A:File.size", "kind": "A", "subkind": "quantity", "entity": "File", "table": "box_files", "field": "size", "evidence": "file full/item", "mutation": "DROP", "designated_substitutes": ["File.version_number"], "suggested_families": ["F7", "F0"]}
{"id": "A:File.extension", "kind": "A", "subkind": "state", "entity": "File", "table": "box_files", "field": "extension", "evidence": "file full; search file_extensions", "mutation": "DROP", "designated_substitutes": [], "suggested_families": ["F7", "F1", "F0"]}
{"id": "D:File.comment_count", "kind": "D", "meaning": "comment count (stored cache vs listed comments)", "mutation": "VIEW", "designated_substitutes": ["count of replies vs top-level; cache vs listing"], "suggested_families": ["F6", "F7", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.