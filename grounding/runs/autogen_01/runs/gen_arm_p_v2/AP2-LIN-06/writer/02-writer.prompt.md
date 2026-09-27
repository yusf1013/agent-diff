The replica pre-checks found these problems:
- Write feasibility: the write call failed on the replica (HTTP 400): {"errors": [{"message": "Field 'AttachmentUpdateInput.title' of required type 'String!' was not provided.", "locations": [{"line": 1, "column": 54}]}, {"message": "Field 'url' is not defined by type 'AttachmentUpdateInput'.", "locations": [{"line": 1, "column": 55}]}]}

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.