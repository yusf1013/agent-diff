Successfully changed the Web team's "In Review" workflow state from a "started" state to a "completed" state. Since the API's `workflowStateUpdate` mutation does not support changing the state type, I:
1. Verified there were no issues in the old "In Review" state (t-web-st-3, type: started)
2. Archived the old "In Review" state
3. Created a new "In Review" state (id: 6b4efe66-67ca-4467-b967-0569661f10c5) with type "completed", preserving the original name, color (#95a2b3), and position (3.0)

Verified that the Web team now has an active "In Review" state of type "completed".
