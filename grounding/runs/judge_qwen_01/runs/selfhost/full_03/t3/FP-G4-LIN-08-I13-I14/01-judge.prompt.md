# Trial of test `FP-G4-LIN-08-I13-I14` (linear)

Test form: fact probe. Target present: no.

## Request given to the solver
Set the priority of the 3-point sub-issue of MOB-42 due on October 15 to High. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- No target: no record meets this reference.
- DECOY `e4fea75a-58e3-44a0-abe8-de6f29e4a6ea` (fact `A:Issue.dueDate`, family F7): Same parent and same estimate, but it is due on October 16, the day after.
  record: {"id": "e4fea75a-58e3-44a0-abe8-de6f29e4a6ea", "identifier": "MOB-53", "title": "Fix Apple Pay sheet dark mode", "teamId": "0576069f-f49a-4be2-80ab-fad2bfc741eb", "stateId": "4a9cf737-a0f4-4fee-acb6-27d126f3a5b4", "creatorId": "u-actor", "priority": 4.0, "priorityLabel": "Low", "number": 53.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 3, "dueDate": "2026-10-16", "parentId": "7228f1ff-c1e3-40b3-b6d3-25911ebdb320"}
- DECOY `53e1707d-41ff-4f91-b514-e8582f862a11` (fact `A:Issue.dueDate`, family F1): Same parent and same estimate, and it was created on October 15, but it is due on October 22.
  record: {"id": "53e1707d-41ff-4f91-b514-e8582f862a11", "identifier": "MOB-54", "title": "Fix Apple Pay sheet voiceover", "teamId": "0576069f-f49a-4be2-80ab-fad2bfc741eb", "stateId": "4a9cf737-a0f4-4fee-acb6-27d126f3a5b4", "creatorId": "u-actor", "priority": 4.0, "priorityLabel": "Low", "number": 54.0, "customerTicketCount": 0, "createdAt": "2026-10-15T09:00:00", "updatedAt": "2026-10-15T09:00:00", "estimate": 3, "dueDate": "2026-10-22", "parentId": "7228f1ff-c1e3-40b3-b6d3-25911ebdb320"}

## Solver steps
Run status: completed; termination: done; steps: 7.

#### Step 1
Reasoning: The user is asking me to do the following in Linear:
1. Find MOB-42
2. Find its sub-issues (child issues)
3. Identify the one with story points of 3, with a due date of October 15 (presumably 2026, but I need to check the year — the current date is 2026-10-16, so "October 15" probably means 2026-10-15)
4. Set its priority to High (priority 3 in Linear)
5. If no such sub-issue exists, tell the user so.

First, let me read Linear's SKILL.md.
Command: read {"path": "~/.openclaw-state/ca516805454c4b9a/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: SKILL.md is somewhat sparse. The base URL is https://api.linear.app/graphql. I need to look up the sub-issues of MOB-42, find the one with storyPoints 3 and dueOn 2025-10-15... wait, the current date is 2026-10-16. Hmm, due date is October 15 — probably 2026-10-15 (yesterday) or 2025. The user says "due date is October 15" — the current date is Friday 2026-10-16, so October 15 is probably 2026-10-15.

Let me try querying the Linear API via curl. Authentication is handled automatically via a proxy using a placeholder token `<TOKEN>`.

Let's run the GraphQL query. First, fetch the sub-issues of MOB-42:

```graphql
query {
  issue(id: "MOB-42") {
    id
    identifier
    title
    subIssues {
      nodes {
        id
        identifier
        title
        priority
        storyPoints
        dueOn
      }
    }
  }
}
```

Then update the matching one with issueUpdate(id, priority: 2) — Linear's priority: 0=none, 1=low, 2=medium, 3=high, 4=urgent. High = 3.

Let me run the query.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issue(id: \"MOB-42\") { id identifier title subIssues(first: 100) { nodes { id identifier title priority storyPoints dueOn } } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'subIssues' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":51}]}]}"}

#### Step 3
Reasoning: The `subIssues` field does not exist directly on the Issue type. In the Linear API, you query sub-issues by using the `relatedIssues` field, or by querying issues with `relatedTo`... Actually, in the Linear API, the `Issue` type has a `subIssues` connection... let me check. In Linear's GraphQL API, does `Issue` have `subIssues: IssueConnection!`? Hmm, apparently that's not the case in this schema. Instead, let's query for issues whose parentId matches the ID of MOB-42.

First, I need to get the ID of MOB-42, and then query for issues whose parentId matches it.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issue(id: \"MOB-42\") { id identifier title } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"7228f1ff-c1e3-40b3-b6d3-25911ebdb320\",\"identifier\":\"MOB-42\",\"title\":\"Checkout crash on launch\"}}}"}

#### Step 4
Reasoning: I need to find sub-issues. In Linear's GraphQL API, sub-issues are queried with `issues(filter: { parentId: { eq: "..." } })`. Let me try that.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issues(filter: { parentId: { eq: \"7228f1ff-c1e3-40b3-b6d3-25911ebdb320\" } }, first: 100) { nodes { id identifier title priority storyPoints dueOn } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Field 'parentId' is not defined by type 'IssueFilter'. Did you mean 'parent'?\",\"locations\":[{\"line\":1,\"column\":26}]},{\"message\":\"Cannot query field 'storyPoints' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":137}]},{\"message\":\"Cannot query field 'dueOn' on type 'Issue'.\",\"locations\":[{\"line\":1,\"column\":149}]}]}"}

#### Step 5
Reasoning: The fields might be different. Let's investigate the schema. There's `parent` in the filter. The field names for priority, story points, and due date might be different. Let's use Introspection.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { __type(name: \"Issue\") { fields { name type { name kind ofType { name } } } } }"}' | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['__type']['fields']:
    t=f['type']
    tn=t['name'] or (t.get('ofType') or {}).get('name') or t['kind']
    print(f['name'], ':', tn)
"
Response: {"status": "success", "stdout": "activitySummary : JSONObject\naddedToCycleAt : DateTime\naddedToProjectAt : DateTime\naddedToTeamAt : DateTime\narchivedAt : DateTime\nasksExternalUserRequester : ExternalUser\nasksRequester : User\nassignee : User\nattachments : AttachmentConnection\nautoArchivedAt : DateTime\nautoClosedAt : DateTime\nbotActor : ActorBot\nbranchName : String\ncanceledAt : DateTime\nchildren : IssueConnection\ncomments : CommentConnection\ndocuments : DocumentConnection\ncompletedAt : DateTime\ncreatedAt : DateTime\ncreator : User\ncustomerTicketCount : Int\ncycle : Cycle\ndelegate : User\ndescription : String\ndescriptionState : String\ndocumentContent : DocumentContent\ndueDate : TimelessDate\nestimate : Float\nexternalUserCreator : ExternalUser\nfavorite : Favorite\nformerAttachments : AttachmentConnection\nformerNeeds : CustomerNeedConnection\nhistory : IssueHistoryConnection\nid : ID\nidentifier : String\nincomingSuggestions : IssueSuggestionConnection\nintegrationSourceType : IntegrationService\ninverseRelations : IssueRelationConnection\nlabelIds : NON_NULL\nlabels : IssueLabelConnection\nlastAppliedTemplate : Template\nneeds : CustomerNeedConnection\nnumber : Float\nparent : Issue\npreviousIdentifiers : NON_NULL\npriority : Float\npriorityLabel : String\nprioritySortOrder : Float\nproject : Project\nprojectMilestone : ProjectMilestone\nreactionData : JSONObject\nreactions : NON_NULL\nrecurringIssueTemplate : Template\nrelations : IssueRelationConnection\nslaBreachesAt : DateTime\nslaHighRiskAt : DateTime\nslaMediumRiskAt : DateTime\nslaStartedAt : DateTime\nslaType : String\nsnoozedBy : User\nsnoozedUntilAt : DateTime\nsortOrder : Float\nsourceComment : Comment\nstartedAt : DateTime\nstartedTriageAt : DateTime\nstate : WorkflowState\nsubIssueSortOrder : Float\nsubscribers : UserConnection\nsuggestions : IssueSuggestionConnection\nsuggestionsGeneratedAt : DateTime\nsyncedWith : LIST\nteam : Team\ntitle : String\ntrashed : Boolean\ntriagedAt : DateTime\nupdatedAt : DateTime\nurl : String"}

#### Step 6
Reasoning: The Issue type has a `children` field, `estimate` (Float, story points), `dueDate` (TimelessDate), and `priority` (Float). Let's query the children of MOB-42.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"query":"query { issue(id: \"MOB-42\") { id children(first: 100) { nodes { id identifier title priority priorityLabel estimate dueDate state { name } } } } }"}'
Response: {"status": "success", "stdout": "{\"data\":{\"issue\":{\"id\":\"7228f1ff-c1e3-40b3-b6d3-25911ebdb320\",\"children\":{\"nodes\":[{\"id\":\"e4fea75a-58e3-44a0-abe8-de6f29e4a6ea\",\"identifier\":\"MOB-53\",\"title\":\"Fix Apple Pay sheet dark mode\",\"priority\":4.0,\"priorityLabel\":\"Low\",\"estimate\":3.0,\"dueDate\":\"2026-10-16\",\"state\":{\"name\":\"Todo\"}},{\"id\":\"383c10b8-c8ec-4487-8b2f-cabdf03772cd\",\"identifier\":\"MOB-57\",\"title\":\"Polish saved-card search\",\"priority\":4.0,\"priorityLabel\":\"Low\",\"estimate\":5.0,\"dueDate\":\"2026-10-22\",\"state\":{\"name\":\"Todo\"}},{\"id\":\"53e1707d-41ff-4f91-b514-e8582f862a11\",\"identifier\":\"MOB-54\",\"title\":\"Fix Apple Pay sheet voiceover\",\"priority\":4.0,\"priorityLabel\":\"Low\",\"estimate\":3.0,\"dueDate\":\"2026-10-22\",\"state\":{\"name\":\"Todo\"}}]}}}}"}

#### Step 7
Reasoning: Sub-issues of MOB-42:
- MOB-53: 3 points, due date 2026-10-16 (not 10-15)
- MOB-57: 5 points, due date 2026-10-22
- MOB-54: 3 points, due date 2026-10-22

User's question: the 3-point sub-issue whose due date is October 15. None have a due date of October 15. MOB-53 is 3 points but due on October 16 (tomorrow… no wait, according to the message the current date is 2026-10-16). MOB-54 is 3 points but due on October 22.

Hmm, "due on October 15"—today is October 16. The user might be misremembering, but the instructions are clear: set the priority of the 3-point sub-issue whose due date is October 15 to High. If none exists, just report that. There is no sub-issue with a due date of 10-15. Two sub-issues have 3 points, but their due dates are different.

Should I just report without making any changes? The instruction is: "If none exists, just report." None matches (3 points + due date October 15). So I should just report, and not change anything. To be safe, I shouldn't guess and modify MOB-53 (due 10-16, possibly "last night" from their perspective… but that would be 10-16, not 10-15).

I'll report: no 3-point sub-issue with a due date of October 15 exists. I'll list what does exist. I won't make any changes.

I checked MOB-42 ("Checkout crash on launch") and none of its sub-issues match that description — so I didn't change anything.

What it has:
- **MOB-53** – Fix Apple Pay sheet dark mode — 3 pts, due **Oct 16** (tomorrow… today, actually), Low
- **MOB-54** – Fix Apple Pay
Command: 
Response: null

## Final answer
I checked MOB-42 ("Checkout crash on launch") and none of its sub-issues match that description — so I didn't change anything.

What it has:
- **MOB-53** – Fix Apple Pay sheet dark mode — 3 pts, due **Oct 16** (tomorrow… today, actually), Low
- **MOB-54** – Fix Apple Pay sheet voiceover — 3 pts, due **Oct 22**, Low
- **MOB-57** – Polish saved-card search — 5 pts, due **Oct 22**, Low

There are two 3-point sub-issues, but neither is due October 15. If you meant MOB-53 (due tomorrow) or MOB-54, tell me which and I'll bump it to High.

## State diff
(no changes)

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": []}. Provisional outcome: correct_absent. Provisional exposed facts: [].

Give your verdict for this trial.