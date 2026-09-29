I moved the "Review the contract" task to Budget 2026.docx by recreating it there (task id 78372673731, action=review, completion_rule=all_assignees, on file 7112). 

However, the move could not be fully completed due to API limitations in this environment:
- The original task (7120) on Budget 2026.pdf (7111) could not be deleted — DELETE /tasks/{id} returned a persistent 500 internal_error.
- The task could not be re-assigned to the original assignee Maya Chen (30000000002) — POST /task_assignments returned 404.

Neither of these endpoints is present in the provided API documentation (only POST /tasks and GET /files/{id}/tasks are documented), so the source task and its assignee transfer remain blocked. The task now exists on the docx, but it also still exists on the PDF and is currently unassigned.
