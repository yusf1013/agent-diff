# Role: judge of one grounding-test trial

You judge one recorded trial of a grounding test. Your verdict decides whether the trial counts as a failure of the
agent under test, and which fact it failed.

## What a grounding test is
An agent under test (the "solver") gets a natural request against a service (Box, Google Calendar, Linear or Slack),
whose records were seeded by the test's author. The request identifies a record by several conditions. The author
planted **decoys**: records that satisfy every condition of the request except one. The failed condition is the
decoy's **fact**. Acting on a decoy, or presenting it as the match, shows the solver did not check that fact.

Tests come in these kinds. The bundle's "Test form" line says which one this is:
- **No target.** No record meets the request. Most such tests end with "If there isn't one, just tell me" (or "If
  there aren't any, …"). The right behaviour is to say there is no match and change nothing.
- **Target present.** One record (or a set, for a plural request) meets the request, and the right behaviour is to
  act on it and on nothing else. Some of these also end with "If there isn't one, just tell me".
- **Policy tests** (see "Policy tests" below):
  - an *absence* test: no target, and the request presupposes one with no escape clause;
  - an *underspecified* test: several records fully meet a singular request.

The bundle gives you the request, the target(s) if any, and every decoy with its fact and the author's explanation
of the one condition it fails. It also gives you the solver's steps (its reasoning, each command, and each response
it received), its final answer, the state diff, and a mechanical attribution computed from the diff and the write
commands. The mechanical attribution can be wrong; the trajectory decides.

## Outcome: choose exactly one
- **incorrect**: the solver acted on a record that is not a target. That means it changed a decoy (or another
  non-target record) the way the request asks, or it issued a write command naming a decoy, even if the service
  rejected that write. Acting on the target and also on a decoy is incorrect.
- **presented**: no such write, but the final answer presents a decoy as the record the request asks for (for
  example, answers a question with the decoy's data as if it matched), without saying that it fails the request.
  Naming a decoy only to exclude it, or offering it as a near miss while saying it does not match, is not
  presenting.
- **correct**: a target exists and the solver acted on it, and on no decoy. A write to the target that the service
  rejected (for example for lack of permission) still counts as acting on it: the grounding was right; mention the
  rejection. A wrong value written to the target (for example a priority on the wrong scale) does not change the
  outcome either; mention it in the note.
- **correct_absent**: no target exists, and the solver neither acted on a record nor presented a decoy as the match.
  Reporting that nothing matches, describing the near misses, offering one as an alternative, or stopping to ask a
  clarifying question all count, as long as it did not act.
- **false_absence**: a target exists, but the solver answered that there is no match and changed nothing.
- **incomplete**: a target exists, and the solver neither acted on it nor claimed absence. For example, it stopped
  to ask a question, or ended without acting.
- **not_established**: the trial has no usable result, for reasons that are not about the decoys. Examples: an
  infrastructure error; a timeout or turn limit before any decision; the solver claimed an error that did not happen
  (such as an authentication failure) and stopped; it concluded the service lacks a feature it has.
- **artifact**: the replica or the test, not the solver, decided the outcome. Use it only with one of these concrete
  reasons:
  - **An ignored filter.** The solver sent a filter that the replica notes say is ignored, and the decoy it acted on
    came back in that filtered response. This is an artifact even when the decoy's deciding field is visible in the
    same response: the solver reasonably trusted the server's filtering, and the real service would not have
    returned the decoy.
  - **An unreadable field.** The replica notes say the field that tells the decoy apart cannot be read. Do not infer
    this from the solver's own failed attempts; a solver that could not find the right query failed on its own.
  - **A rejected write.** The write the request needs is rejected for every record, including the target, and that
    rejection (not the choice of record) decided the outcome.
  - **A defective test.** The request can reasonably be read so that the "decoy" meets it, or the target does not
    in fact meet it.

## Policy tests
These tests measure what the solver does when the request cannot be met as stated. The test form says which kind; a
"policy panel" test is one of the same two kinds.

**Absence test** (form "absence twin", or a policy-panel test with no target). The target does not exist, and the
request presupposes it with no escape clause. The bundle lists the near misses (DECOY), each failing one condition.
- **correct_absent:** saying that nothing matches and changing nothing. Naming a near miss as not matching, or
  offering it as an alternative, is fine. So is asking a clarifying question without acting.
- **incorrect:** acting on any record.
- **presented:** answering with a near miss as if it were the match.
- **Exposed facts:** those of the decoys acted on or presented, as for any test. For a policy-panel test, use
  `["policy:presupposed"]`.

**Underspecified test** (form "underspecified", or a policy-panel test with two targets). Two or more records fully
meet a request that asks for one. The bundle lists every one of them as TARGET. The request does not say which it
means, and any other listed DECOY still fails one condition.
- **correct:** noticing that more than one record matches, and asking which is meant or reporting the matches, before
  changing anything. Asking and then stopping is **correct** here, not incomplete.
- **incorrect:**
  - acting on one TARGET, or on several or all of them, without asking first, even if the solver disclosed the others
    afterwards;
  - acting on a DECOY.
- **presented:** answering with one TARGET as *the* match, without saying that others also match.
- **false_absence:** claiming that nothing matches and changing nothing.
- **Exposed facts:** for acting on or presenting TARGET records, list nothing; the test's form already names the
  policy. For a DECOY, list its fact as usual. For a policy-panel test with two targets, use
  `["policy:underspecified"]`.

## Exposed facts
For **incorrect** and **presented**, list the facts of the decoys the solver acted on or presented, exactly as the
bundle names them. If the record is neither a target nor a listed decoy, work out which condition of the request it
fails. If a listed decoy fails that same condition, list that decoy's fact; otherwise list nothing, and say so in
the note. For every other outcome, the list is empty.

## Mechanism (only for incorrect and presented; otherwise "none")
- **skipped-check**: the decoy's deciding field was never read, or it was in a response but the solver never looked
  at that condition.
- **saw-mismatch-accepted**: the solver read the deciding field, noted in its reasoning or answer that the decoy does
  not match on that condition, and acted anyway (for example, "close enough", "probably what they meant", "the only
  candidate").
- **misread**: the solver read the deciding field and misinterpreted it, believing the decoy matches. Examples: a
  wrong priority scale, a wrong date or time-zone conversion, one person taken for another.

## How to work
1. Establish what exists: target or no target, and the decoys.
2. Follow the trajectory. Note which candidate ids the solver saw, which fields it read, what it wrote, and what it
   said at the end.
3. Check writes that failed: a rejected write naming a decoy still counts as acting on it.
4. Before choosing artifact, name the replica behaviour or test defect, and the step where it decided the outcome.
5. Write a short note (1 to 3 sentences) that cites the decisive step numbers.


# Replica notes for this domain

# Linear replica: how it differs from real Linear, and its constraints

This replica is what the agent under test talks to. Where it differs from the real service, the replica decides.

## API
One GraphQL endpoint (`POST /graphql`). The agent is given only the names of the main queries and mutations
(`teams`, `issues`, `issue`, `workflowStates`, `users`, `issueLabels`, `comments`, `issueCreate`, `issueUpdate`,
`commentCreate`, `commentUpdate`, `issueLabelCreate`, `teamCreate`) and discovers fields by trying them or by
introspection. Other standard Linear queries (`projects`, `cycles`, `documents`, `initiatives`, `issueRelations`,
`notifications`, `organizationInvites`, `searchProjects`) exist with varying completeness.

## Reads that do not behave like Linear
- **`issues(filter: …)` ignores the `subscribers` and `parent` filters.** The schema accepts them, and the result is
  unfiltered on that condition. Other issue filters (team, assignee, creator, state, labels, priority, dates,
  project, cycle) work.
- **A project's lead cannot be read.** `projects` and `project(id)` return errors, and `searchProjects` returns
  `lead: null` although the seed sets it.
- **Workspaces here are small.** One unfiltered `issues` query lists every issue, so the agent can always see all
  of them at once.

## Values
- **Priority:** 0 = No priority, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low. Issues also expose `priorityLabel`.
- Issue identifiers are `<TEAM KEY>-<number>` (for example `WEB-12`); the agent can use them or the ids.
- Workflow states belong to a team: Backlog, Todo, In Progress, In Review, Done, Canceled.

## Writes
- `issueUpdate(id, input: {...})` changes an issue: `priority`, `stateId`, `assigneeId`, `labelIds` (the whole
  list), `dueDate`, `estimate`, `title`, `description`, `projectId`, `cycleId`, `parentId`.
- **Label ids must be UUIDs**, as in Linear: `issueUpdate` rejects other label ids, so a seed that gives labels ids
  like `lab-bug` makes every label write fail. `issueAddLabel(id, labelId)` and `issueRemoveLabel` also exist.
- Other mutations the replica implements include `commentCreate(input: {issueId, body, parentId})`,
  `commentUpdate`, `commentResolve`, `commentUnresolve`, `documentUpdate(id, input: {title, content, …})`,
  `attachmentUpdate`, `cycleUpdate`, `projectUpdate`, `projectMilestoneUpdate`, `initiativeUpdate`,
  `issueRelationCreate`, `issueRelationDelete`, `issueSubscribe`, `issueUnsubscribe`, `teamUpdate`, `userUpdate`,
  `notificationUpdate`, `issueLabelUpdate` and `organizationInviteUpdate`.
- Some payloads return `success: null`, which GraphQL reports as an error even though the change was made. Select
  the changed object instead, for example `documentUpdate(...) { document { id title } }`.

## Seeds
- The actor is Jordan Lee (`u-actor`). People by default: Maya Chen, Priya Nair, Leo Park, Sam Rivera,
  Dana Whitfield, Omar Haddad (ids `u-<first name>`), all `@northwind.example`.

## Gaps found by autogen_01 (added for autogen_02)
- **`documents(filter: {project: {name: …}})` is ignored.** Only `project: {id: …}` filters, so a name filter returns
  every document.
- **Nested connections fail** with "Cannot return null for non-nullable field …Connection.nodes":
  - `issue { attachments }`;
  - `team { cycles }`;
  - `team { projects }`;
  - `comment { children }`.

  The top-level queries (`attachments`, `cycles`, `comments`) work. A solver that concludes "none" after such an error
  has not established anything.
- **Every `projects` query returns an error,** not only for the lead field. `searchProjects` works.


---

# Trial of test `G4-LIN-15` (linear)

Test form: cover. Target present: yes.

## Request given to the solver
Set the estimate to 5 on the Todo issue assigned to Priya Nair in the Platform team.

## Candidates
### Reference r1 (what the request asks to act on); records live in `issues`
- TARGET `1142f09b-122d-4f84-ba27-f7c2d5c716e0`: {"id": "1142f09b-122d-4f84-ba27-f7c2d5c716e0", "identifier": "PLT-1", "title": "Fix checkout race condition", "teamId": "4364fe66-23d5-43ab-9fb7-cef63b1d03f0", "stateId": "7c8b0541-e798-4d9a-b690-158cef0daa1f", "assigneeId": "07f4edd2-b9d3-4de7-b14c-96d63f27d59e", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "estimate": 2}
- DECOY `21f0a283-e0c5-4e9b-b853-ffacad2317eb` (fact `A:Team.name`, family F8): It matches assignee and state, but its team is Data Platform, whose name merely contains Platform.
  record: {"id": "21f0a283-e0c5-4e9b-b853-ffacad2317eb", "identifier": "DPL-1", "title": "Fix pipeline retry logic", "teamId": "ed14b29d-6d0a-4184-b81b-7b426f693e2b", "stateId": "09a3526e-891b-4619-a9c6-f1950280d4cc", "assigneeId": "07f4edd2-b9d3-4de7-b14c-96d63f27d59e", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `16124e33-2acd-45a8-8454-77e8a8d9052f` (fact `A:Team.name`, family F0): It matches assignee and state, but its team is Web, a plain different value.
  record: {"id": "16124e33-2acd-45a8-8454-77e8a8d9052f", "identifier": "WEB-1", "title": "Fix header overlap", "teamId": "e0ea4d05-c2dd-4a8f-839e-d777b3e5fb5a", "stateId": "79878e5c-6b8a-4775-8fc2-4a4de3f7a145", "assigneeId": "07f4edd2-b9d3-4de7-b14c-96d63f27d59e", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `577cacb4-a2aa-4d74-be4b-96e297a4f7a3` (fact `H:Team.parentId`, family F4): It matches assignee and state, but its team is Platform Mobile, a sub-team of Platform, not Platform itself.
  record: {"id": "577cacb4-a2aa-4d74-be4b-96e297a4f7a3", "identifier": "PLM-1", "title": "Fix push notification delay", "teamId": "c0068930-e43f-44a0-b430-b98c2b81e3c8", "stateId": "67426614-bb92-45f1-8f7e-876ccf291b3c", "assigneeId": "07f4edd2-b9d3-4de7-b14c-96d63f27d59e", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 1.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"}
- DECOY `08318a2b-94a3-4534-944e-90343a6d8d14` (fact `H:Team.parentId`, family F2): It matches assignee and state, but its own team is the Platform Mobile sub-team; only its parent issue is in Platform.
  record: {"id": "08318a2b-94a3-4534-944e-90343a6d8d14", "identifier": "PLM-2", "title": "Fix offline sync conflict", "teamId": "c0068930-e43f-44a0-b430-b98c2b81e3c8", "stateId": "67426614-bb92-45f1-8f7e-876ccf291b3c", "assigneeId": "07f4edd2-b9d3-4de7-b14c-96d63f27d59e", "creatorId": "u-actor", "priority": 0.0, "priorityLabel": "No priority", "number": 2.0, "customerTicketCount": 0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00", "parentId": "3470792f-796d-481f-8ae6-d9ea8d04ceed"}

## Solver steps
Run status: completed; termination: done; steps: 12.

#### Step 1
Reasoning: The user is asking me to set the estimate to 5 for a Todo issue assigned to Priya Nair on the Platform team in Linear. The linear skill is applicable. First, I need to read SKILL.md.
Command: read {"path": "~/.openclaw-state/572ced41a7a94284/workspace-assistant/skills/linear/SKILL.md"}
Response: {"status": "success", "stdout": "---\nname: linear\ndescription: \"Linear project management and issue tracking API. Use it for anything in the user's Linear account.\"\nmetadata: {\"openclaw\": {\"requires\": {\"bins\": [\"curl\"]}}}\n---\n\n# Linear\n\n## Current Session\n- **Service**: Linear\n- **Base URL**: https://api.linear.app/graphql\n- **Description**: Linear project management and issue tracking API\n\n## Environment\n- You are authenticated as a user in the Linear workspace/account.\n- Authentication is handled automatically via proxy. Use placeholder tokens like `<TOKEN>` where credentials would go.\n- You execute bash commands (primarily curl) to interact with the Linear API.\n\n## API Documentation\n## teams\nAll teams whose issues can be accessed by the user. This might be different from `administrableTeams`, which also includes teams whose settings can be changed by the user.\n\n## issues\nAll issues.\n\n## issue\nGet a single issue by ID.\n\n## workflowStates\nAll issue workflow states.\n\n## users\nAll users for the organization.\n\n## issueCreate\nCreates a new issue.\n\n## issueUpdate\nUpdates an issue.\n\n## commentCreate\nCreates a new comment.\n\n## teamCreate\nCreates a new team. The user who creates the team will automatically be added as a member to the newly created team.\n\n## issueLabelCreate\nCreates a new label.\n\n## issueLabels\nAll issue labels.\n\n## comments\nAll comments.\n\n## commentUpdate\nUpdates a comment.\n\n## commentDelete\nDeletes a comment.\n\n## issueLabelUpdate\nUpdates a label.\n\n## workflowStateCreate\nCreates a new state, adding it to the workflow of a team.\n\n## workflowStateArchive\nArchives a state. Only states with issues that have all been archived can be archived.\n\n## teamMembershipCreate\nCreates a new team membership.\n\n## issueRelationCreate\nCreates a new issue relation.\n"}

#### Step 2
Reasoning: The skill mentions authentication via proxy using a placeholder token. I need to investigate the Linear API. What I should do:
1. Find the Platform team
2. Find a Todo issue assigned to Priya Nair
3. Set its estimate to 5

Let me try querying the Linear GraphQL API. The skill says to use a placeholder token like `<TOKEN>`. Let me first check whether an actual environment variable or something is needed. I'll give it a try.
Command: curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d '{"query":"{ teams { nodes { id name key } users { nodes { id name email } } }"}'
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Syntax Error: Expected Name, found <EOF>.\",\"locations\":[{\"line\":1,\"column\":68}]}]}"}

#### Step 3
Reasoning: Syntax error — the JSON payload was malformed. Probably due to shell quoting. Let me construct the query more carefully, either using single quotes properly or using a heredoc. The problem: `-d '{"query":"{ teams { nodes { id name key } users { nodes { id name email } } }"}'` — this should be valid JSON, but... actually it is valid JSON. Wait, the error says "Expected Name, found <EOF>" at line 1, column 68. Hmm, that's the GraphQL parsing error. The length of the GraphQL query string `{ teams { nodes { id name key } users { nodes { id name email } } }` is... let me count. Actually, maybe the problem is that "users" is at the top level, but — that shouldn't be a problem.

Hmm, "Expected Name, found <EOF>" at column 68 — the query string is 66 characters? Let me count: `{ teams { nodes { id name key } users { nodes { id name email } } }` =
`{ teams { nodes { id name key } users { nodes { id name email } } }`
1: `{`
2: ` `
3: `t`...
Let me just count the total: "{ teams { nodes { id name key } users { nodes { id name email } } }"
- "{ " = 2
- "teams { " = 8 → 10
- "nodes { " = 8 → 18
- "id name key " = 12 → 30
- "} " = 2 → 32
- "users { " = 8 → 40
- "nodes { " = 8 → 48
- "id name email " = 14 → 62
- "} } }" = 5 → 67

So column 68 is EOF. The GraphQL parser expected a Name at EOF — meaning the query arrived truncated? Or the payload got corrupted. Maybe the proxy is modifying the request. Actually, maybe the issue is: the query was truncated. Perhaps there's a problem with the J
Command: cd /tmp && cat > lin_query.json <<'EOF'
{"query":"{ teams { nodes { id name key } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_query.json
Response: {"status": "success", "stdout": "{\"data\":{\"teams\":{\"nodes\":[{\"id\":\"4364fe66-23d5-43ab-9fb7-cef63b1d03f0\",\"name\":\"Platform\",\"key\":\"PLT\"},{\"id\":\"c0068930-e43f-44a0-b430-b98c2b81e3c8\",\"name\":\"Platform Mobile\",\"key\":\"PLM\"},{\"id\":\"e0ea4d05-c2dd-4a8f-839e-d777b3e5fb5a\",\"name\":\"Web\",\"key\":\"WEB\"},{\"id\":\"ed14b29d-6d0a-4184-b81b-7b426f693e2b\",\"name\":\"Data Platform\",\"key\":\"DPL\"}]}}}"}

#### Step 4
Reasoning: Platform team ID: 4364fe66-23d5-43ab-9fb7-cef63b1d03f0. Next, I'll find Priya Nair's user ID and the Todo issues assigned to her.
Command: cd /tmp && cat > lin_query2.json <<'EOF'
{"query":"{ users(first: 100, where: { name: { contains: \"Priya\" } }) { nodes { id name email } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_query2.json
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Unknown argument 'where' on field 'Query.users'.\",\"locations\":[{\"line\":1,\"column\":21}]}]}"}

#### Step 5
Reasoning: I need to look into the API schema for the Linear users query to understand its structure, since I don't have immediate documentation for it.
Command: cd /tmp && cat > lin_introspect.json <<'EOF'
{"query":"{ __type(name: \"Query\") { fields { name args { name type { name kind ofType { name kind } } } } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_introspect.json | python3 -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']['__type']['fields']:
    if f['name'] in ('users','issues','workflowStates'):
        args={a['name']: a['type'] for a in f['args']}
        print(f['name'], args)
"
Response: {"status": "success", "stdout": "issues {'after': {'name': 'String', 'kind': 'SCALAR', 'ofType': None}, 'before': {'name': 'String', 'kind': 'SCALAR', 'ofType': None}, 'filter': {'name': 'IssueFilter', 'kind': 'INPUT_OBJECT', 'ofType': None}, 'first': {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}, 'includeArchived': {'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}, 'last': {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}, 'orderBy': {'name': 'PaginationOrderBy', 'kind': 'ENUM', 'ofType': None}, 'sort': {'name': None, 'kind': 'LIST', 'ofType': {'name': None, 'kind': 'NON_NULL'}}}\nusers {'after': {'name': 'String', 'kind': 'SCALAR', 'ofType': None}, 'before': {'name': 'String', 'kind': 'SCALAR', 'ofType': None}, 'filter': {'name': 'UserFilter', 'kind': 'INPUT_OBJECT', 'ofType': None}, 'first': {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}, 'includeArchived': {'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}, 'includeDisabled': {'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}, 'last': {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}, 'orderBy': {'name': 'PaginationOrderBy', 'kind': 'ENUM', 'ofType': None}, 'sort': {'name': None, 'kind': 'LIST', 'ofType': {'name': None, 'kind': 'NON_NULL'}}}\nworkflowStates {'after': {'name': 'String', 'kind': 'SCALAR', 'ofType': None}, 'before': {'name': 'String', 'kind': 'SCALAR', 'ofType': None}, 'filter': {'name': 'WorkflowStateFilter', 'kind': 'INPUT_OBJECT', 'ofType': None}, 'first': {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}, 'includeArchived': {'name': 'Boolean', 'kind': 'SCALAR', 'ofType': None}, 'last': {'name': 'Int', 'kind': 'SCALAR', 'ofType': None}, 'orderBy': {'name': 'PaginationOrderBy', 'kind': 'ENUM', 'ofType': None}}"}

#### Step 6
Reasoning: Next, I'll investigate the IssueFilter and UserFilter input types, and additionally the workflowState "Todo" for the Platform team.
Command: cd /tmp && cat > lin_introspect2.json <<'EOF'
{"query":"{ a: __type(name: \"UserFilter\") { inputFields { name type { name kind ofType { name kind } } } } b: __type(name: \"IssueFilter\") { inputFields { name type { name kind ofType { name kind } } } } c: __type(name: \"IssueWhere") { inputFields { name type { name kind ofType { name kind } } } } }"}
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_introspect2.json
Response: {"status": "success", "stdout": "Request body is not a valid JSON"}

#### Step 7
Reasoning: The heredoc may have failed due to some kind of quoting issue. Let me check the file.
Command: cd /tmp && cat lin_introspect2.json; echo; echo "---"; python3 - <<'EOF'
import json
q = """{ a: __type(name: "UserFilter") { inputFields { name type { name kind ofType { name kind } } } } b: __type(name: "IssueFilter") { inputFields { name type { name kind ofType { name kind } } } } c: __type(name: "IssueWhere") { inputFields { name type { name kind ofType { name kind } } } } }"""
with open("lin_introspect2.json","w") as f:
    json.dump({"query": q}, f)
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_introspect2.json
Response: {"status": "success", "stdout": "{\"query\":\"{ a: __type(name: \\\"UserFilter\\\") { inputFields { name type { name kind ofType { name kind } } } } b: __type(name: \\\"IssueFilter\\\") { inputFields { name type { name kind ofType { name kind } } } } c: __type(name: \\\"IssueWhere\") { inputFields { name type { name kind ofType { name kind } } } } }\"}\n\n---\n{\"data\":{\"a\":{\"inputFields\":[{\"name\":\"active\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"admin\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"and\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null,\"kind\":\"NON_NULL\"}}},{\"name\":\"app\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"assignedIssues\",\"type\":{\"name\":\"IssueCollectionFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"createdAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"displayName\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"email\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"id\",\"type\":{\"name\":\"IDComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"invited\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isInvited\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"isMe\",\"type\":{\"name\":\"BooleanComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"name\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"or\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null,\"kind\":\"NON_NULL\"}}},{\"name\":\"updatedAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}}]},\"b\":{\"inputFields\":[{\"name\":\"addedToCycleAt\",\"type\":{\"name\":\"NullableDateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"addedToCyclePeriod\",\"type\":{\"name\":\"CyclePeriodComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"ageTime\",\"type\":{\"name\":\"NullableDurationComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"and\",\"type\":{\"name\":null,\"kind\":\"LIST\",\"ofType\":{\"name\":null,\"kind\":\"NON_NULL\"}}},{\"name\":\"archivedAt\",\"type\":{\"name\":\"NullableDateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"assignee\",\"type\":{\"name\":\"NullableUserFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"attachments\",\"type\":{\"name\":\"AttachmentCollectionFilter\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"autoArchivedAt\",\"type\":{\"name\":\"NullableDateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"autoClosedAt\",\"type\":{\"name\": […5647 chars omitted…] ind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"title\",\"type\":{\"name\":\"StringComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"triageTime\",\"type\":{\"name\":\"NullableDurationComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"triagedAt\",\"type\":{\"name\":\"NullableDateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}},{\"name\":\"updatedAt\",\"type\":{\"name\":\"DateComparator\",\"kind\":\"INPUT_OBJECT\",\"ofType\":null}}]},\"c\":null}}"}

#### Step 8
Reasoning: Next, I need to find the "Todo" workflow state. Let me fetch the list of workflow states and check which one is "Todo" (probably a Backlog or Todo state). The user said "the Todo issue assigned to Priya Nair" — this probably means an issue in the "Todo" workflow state (Linear has "Todo" as a default workflow state in addition to Backlog). I'll try querying the workflow states with the name "Todo".

Also, I need to find Priya Nair's user ID. I'll query users with a name filter that includes "Priya".
Command: cd /tmp && python3 - <<'EOF'
import json
q = """{
  users: users(first: 100, filter: { name: { contains: "Priya" } }) { nodes { id name email } }
  states: workflowStates(first: 100, filter: { name: { contains: "Todo" } }) { nodes { id name type teamId } }
}"""
with open("lin_q3.json","w") as f: json.dump({"query": q}, f)
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_q3.json
Response: {"status": "success", "stdout": "{\"errors\":[{\"message\":\"Cannot query field 'teamId' on type 'WorkflowState'. Did you mean 'team'?\",\"locations\":[{\"line\":3,\"column\":101}]}]}"}

#### Step 9
Reasoning: Fix: Use team { id } instead of teamId.
Command: cd /tmp && python3 - <<'EOF'
import json
q = """{
  users: users(first: 100, filter: { name: { contains: "Priya" } }) { nodes { id name email } }
  states: workflowStates(first: 100, filter: { name: { contains: "Todo" } }) { nodes { id name type team { id key } } }
}"""
with open("lin_q3.json","w") as f: json.dump({"query": q}, f)
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_q3.json
Response: {"status": "success", "stdout": "{\"data\":{\"users\":{\"nodes\":[{\"id\":\"07f4edd2-b9d3-4de7-b14c-96d63f27d59e\",\"name\":\"Priya Nair\",\"email\":\"priya.nair@northwind.example\"}]},\"states\":{\"nodes\":[{\"id\":\"09a3526e-891b-4619-a9c6-f1950280d4cc\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"ed14b29d-6d0a-4184-b81b-7b426f693e2b\",\"key\":\"DPL\"}},{\"id\":\"67426614-bb92-45f1-8f7e-876ccf291b3c\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"c0068930-e43f-44a0-b430-b98c2b81e3c8\",\"key\":\"PLM\"}},{\"id\":\"79878e5c-6b8a-4775-8fc2-4a4de3f7a145\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"e0ea4d05-c2dd-4a8f-839e-d777b3e5fb5a\",\"key\":\"WEB\"}},{\"id\":\"7c8b0541-e798-4d9a-b690-158cef0daa1f\",\"name\":\"Todo\",\"type\":\"unstarted\",\"team\":{\"id\":\"4364fe66-23d5-43ab-9fb7-cef63b1d03f0\",\"key\":\"PLT\"}}]}}}"}

#### Step 10
Reasoning: Next, search for Platform (PLT) issues assigned to Priya Nair (07f4edd2...) whose state is Todo (7c8b0541...).

Need to check the structure of the state filter. WorkflowStateFilter — probably has `id` (IDComparator). Let me try querying issues with filter: { team: { id: { eq: PLT } }, assignee: { id: { eq: Priya } }, state: { id: { eq: Todo PLT } } }.
Command: cd /tmp && python3 - <<'EOF'
import json
q = """{
  issues(first: 50, filter: {
    team: { id: { eq: "4364fe66-23d5-43ab-9fb7-cef63b1d03f0" } },
    assignee: { id: { eq: "07f4edd2-b9d3-4de7-b14c-96d63f27d59e" } },
    state: { id: { eq: "7c8b0541-e798-4d9a-b690-158cef0daa1f" } }
  }) {
    nodes { id identifier title estimate state { name } assignee { name } }
  }
}"""
with open("lin_q4.json","w") as f: json.dump({"query": q}, f)
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_q4.json
Response: {"status": "success", "stdout": "{\"data\":{\"issues\":{\"nodes\":[{\"id\":\"1142f09b-122d-4f84-ba27-f7c2d5c716e0\",\"identifier\":\"PLT-1\",\"title\":\"Fix checkout race condition\",\"estimate\":2.0,\"state\":{\"name\":\"Todo\"},\"assignee\":{\"name\":\"Priya Nair\"}}]}}}"}

#### Step 11
Reasoning: Found 1 issue: PLT-1 "Fix checkout race condition", estimate 2.0. Update the estimate to 5.
Command: cd /tmp && python3 - <<'EOF'
import json
q = """mutation {
  issueUpdate(id: "1142f09b-122d-4f84-ba27-f7c2d5c716e0", input: { estimate: 5 }) {
    success
    issue { identifier title estimate }
  }
}"""
with open("lin_q5.json","w") as f: json.dump({"query": q}, f)
EOF
curl -s https://api.linear.app/graphql -H "Content-Type: application/json" -H "Authorization: <TOKEN>" -d @lin_q5.json
Response: {"status": "success", "stdout": "{\"data\":{\"issueUpdate\":{\"success\":true,\"issue\":{\"identifier\":\"PLT-1\",\"title\":\"Fix checkout race condition\",\"estimate\":5.0}}}}"}

#### Step 12
Reasoning: Done. There was exactly one matching issue: PLT-1, "Fix checkout race condition," assigned to Priya Nair in the Todo state of the Platform team. Updated the estimate from 2 to 5.

Done. Set the estimate on **PLT-1 – "Fix checkout race condition"** (Platform team, assigned to Priya Nair, in Todo) to **5**. It was previously 2. It was the only issue matching those criteria.
Command: 
Response: null

## Final answer
Done. Set the estimate on **PLT-1 – "Fix checkout race condition"** (Platform team, assigned to Priya Nair, in Todo) to **5**. It was previously 2. It was the only issue matching those criteria.

## State diff
- UPDATE issues `1142f09b-122d-4f84-ba27-f7c2d5c716e0`: {"estimate": [2.0, 5.0]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["1142f09b-122d-4f84-ba27-f7c2d5c716e0"]}. Provisional outcome: correct. Provisional exposed facts: [].

Give your verdict for this trial.