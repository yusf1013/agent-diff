The Box API doesn't support tags on folders — `PUT`/`PATCH` on a folder returns 405, and per the API reference the `tags` parameter only exists on `PUT /files/{file_id}` (file updates). I verified the target folder is the right one (Summer Launch, id 8110: directly under Marketing, owned by Dana Whitfield, created by Leo Park), but the tag itself can't be applied.

Options:
- If you meant to tag a **file** inside Summer Launch (e.g., a launch doc), tell me which and I'll tag it.
- Alternatively I can add "launch-ready" to the folder's **description** as a workaround — just say the word.
