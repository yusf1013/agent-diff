I could not change the creation date, because it is not modifiable.

Details:
- The review task on "Budget 2026.pdf" is task ID 7120 (action: "review") on file ID 7111 (in the Finance folder), currently assigned to Maya Chen.
- Its current creation date is 2026-06-01T09:00:00.
- I attempted `PUT /tasks/7120` with `created_at` set to 2026-09-01. The API returned HTTP 200, but the returned object still showed `created_at: 2026-06-01T09:00:00` — the value was ignored.
- In Box, a task's `created_at` is a system-generated, immutable field. The only updatable task properties are `action`, `message`, `due_at`, `completion_rule`, and `is_completed`.

Therefore the creation date cannot be set to September 1, 2026. If you actually meant the task's *due date* (`due_at`, currently null), that field is updatable — let me know and I'll set it to 2026-09-01.
