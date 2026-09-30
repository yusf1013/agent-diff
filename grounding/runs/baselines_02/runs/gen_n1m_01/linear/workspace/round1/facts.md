# Facts to test

Together, your tests must check the assistant on each fact below: for every fact, at least one test in which that
fact decides which record is the right one.

The kinds of fact:
- **attribute:** an identifying attribute of a record (identity, text, time, quantity, state);
- **relationship:** a record's related person or record in a given role (a foreign-key role, an association);
- **hierarchy:** a level of a hierarchy or a self-relationship (a parent, a reply's parent);
- **binding:** several conditions that must hold on the same related record, across a to-many relationship;
- **derived value:** a value computed from records (a count, the latest one, a local date, the primary calendar).

| Fact | Kind | Rests on |
|---|---|---|
| `A:Attachment.sourceType` | attribute | `attachments.sourceType` |
| `A:Cycle.endsAt` | attribute | `cycles.endsAt` |
| `A:Issue.dueDate` | attribute | `issues.dueDate` |
| `A:Issue.estimate` | attribute | `issues.estimate` |
| `A:Issue.identifier` | attribute | `issues.identifier` |
| `A:ProjectMilestone.name` | attribute | `project_milestones.name` |
| `B:Attachment.issueId` | binding | `Attachment.issueId` |
| `B:ProjectMilestone.projectId` | binding | `ProjectMilestone.projectId` |
| `B:issue_label_issue_association` | binding | `issue_label_issue_association` |
| `D:overdue` | derived value | `overdue` |
| `R:Attachment.creatorId` | relationship | `Attachment.creatorId` |
| `R:Cycle.teamId` | relationship | `Cycle.teamId` |
| `R:Issue.assigneeId` | relationship | `Issue.assigneeId` |
| `R:Issue.cycleId` | relationship | `Issue.cycleId` |
| `R:Issue.projectId` | relationship | `Issue.projectId` |
| `R:ProjectMilestone.projectId` | relationship | `ProjectMilestone.projectId` |
| `R:issue_label_issue_association` | relationship | `issue_label_issue_association` |
