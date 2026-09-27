---
name: linear
description: "Linear project management and issue tracking API. Use it for anything in the user's Linear account."
metadata: {"openclaw": {"requires": {"bins": ["curl"]}}}
---

# Linear

## Current Session
- **Service**: Linear
- **Base URL**: https://api.linear.app/graphql
- **Description**: Linear project management and issue tracking API

## Environment
- You are authenticated as a user in the Linear workspace/account.
- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.
- You execute bash commands (primarily curl) to interact with the Linear API.

## API Documentation
## teams
All teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.

## issues
All issues.

## issue
Get a single issue by ID.

## workflowStates
All issue workflow states.

## users
All users for the organization.

## issueCreate
Creates a new issue.

## issueUpdate
Updates an issue.

## commentCreate
Creates a new comment.

## teamCreate
Creates a new team. The user who creates the team will automatically be added as a member to the newly created team.

## issueLabelCreate
Creates a new label.

## issueLabels
All issue labels.

## comments
All comments.

## commentUpdate
Updates a comment.

## commentDelete
Deletes a comment.

## issueLabelUpdate
Updates a label.

## workflowStateCreate
Creates a new state, adding it to the workflow of a team.

## workflowStateArchive
Archives a state. Only states with issues that have all been archived can be archived.

## teamMembershipCreate
Creates a new team membership.

## issueRelationCreate
Creates a new issue relation.
