Changed the Web team's "In Review" state to a completed state. Since the Linear API doesn't allow directly updating a workflow state's type, I:
1. Created a new "In Review" state with type "completed" (ID: 01c1cabf-a435-45ea-80eb-d1b443e3c1be)
2. Archived the old "In Review" state (t-web-st-3, type "started")

The Web team now has "In Review" as a completed state in its workflow.
