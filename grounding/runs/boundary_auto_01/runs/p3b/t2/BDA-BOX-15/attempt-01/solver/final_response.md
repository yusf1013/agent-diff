I was unable to move the Finance folder into its Q1 subfolder because this operation is logically invalid.

Details found:
- **Finance** folder: ID 7100 (in root "All Files")
- **Q1** subfolder: ID 7101, which is a child *of* Finance

When I attempted the move (`PUT /folders/7100` with `parent.id = 7101`), the API returned:
- **400 Bad Request** — "Cannot move folder into its own descendant"

A folder cannot be moved into one of its own descendants (Q1 → Finance → Q1 would be a cycle), so this move is impossible by design.

If you intended something different, let me know — for example:
- Move **Q1** up out of Finance,
- Move the **Finance** folder into some *other* folder, or
- Move files *into* the Q1 folder.

I can perform any of those alternatives if you confirm.
