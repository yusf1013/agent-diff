Write scenario `AR-BOX-22` for the box domain (see brief.json).

Facts your scenario must test (each needs at least one decoy):
{"id": "A:File.name", "kind": "A", "subkind": "identity", "entity": "File", "table": "box_files", "field": "name", "evidence": "file full/mini/item; search", "mutation": "DROP", "designated_substitutes": ["File.uploader_display_name"], "suggested_families": ["F8", "F1", "F0"]}
{"id": "R:Hub.updated_by_id", "kind": "R", "roles": ["Hub.updated_by_id"], "meaning": "hub last updater", "mutation": "SUB_OR_DROP", "designated_substitutes": ["Hub.created_by_id"], "suggested_families": ["F1", "F2", "F8", "F0"]}
{"id": "R:HubItem.file", "kind": "R", "roles": ["HubItem.hub_id", "HubItem.item_id:file"], "meaning": "file included in hub", "mutation": "SUB_OR_DROP", "designated_substitutes": ["File.parent_id (file in a folder of the same name)", "File.collections"], "suggested_families": ["F1", "F2", "F8", "F0"]}

Start by reading docs/method.md, docs/format.md and the two examples, then the domain files. Save the scenario as scenario.json in your working directory.