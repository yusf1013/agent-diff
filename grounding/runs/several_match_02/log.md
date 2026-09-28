# several_match_02 log

One entry per cycle: what changed, what ran, what was learned.

## Cycle 0: the pilot's routes (2026-09-28, no runs)

**What ran:** [routes.py](routes.py) over several_match_01's 24 plural trials (the self-hosted Qwen).

**What was learned:**
- **Generous quantities almost always.** The agent asked for `limit=1000`, `limit=999`, `limit=200`,
  `maxResults=250` or `count=100` in nearly every listing or search. The one pagination miss was an unfiltered
  GraphQL `issues` query at Linear's default of 50 (SM-LIN-01 t1).
- **Recursion when the request states the scope:**
  - "including the ones in its subfolders": 3/3 listed every subfolder;
  - "on the calendars I own": 6/6 listed the owned calendars (`minAccessRole=owner`) and queried each;
  - "and its sub-teams": the agent read the team tree and filtered on all three team ids, or listed every issue.
- **Server-side filters whenever they work** (Linear: team, assignee, state, labels).
- **"Stops after the first batch": 1 of 24** (SM-LIN-01 t1, the unfiltered page). In SM-BOX-01 (2 matches in the
  named folder, then 2 in subfolders) the agent went on into the subfolders 3/3. In SM-LIN-01 t3 it widened a narrow
  filter after finding 2.
- **The placements were all explicit.** Every hidden place was named by the request's wording (subfolders, owned
  calendars, sub-teams) or fell to a larger page. So the pilot tested whether the agent follows a stated scope, and
  it does.

**The replica's defaults that hide records** (checked in the code; they are faithful):
- Calendar `calendarList` leaves out hidden calendars unless `showHidden=true`;
- Slack `conversations.list` lists only public channels unless `types` includes `private_channel`;
- Linear `issues` leaves out archived issues unless `includeArchived: true`;
- Box `search` requires a query term (as real Box does).

These, and scopes that span containers, are the candidate hiding places for cycle 1.

**Measurement note:** routes.py matched records by name as well as by id. Calendar events that share a title were
therefore counted together. From cycle 1 it matches by id only.

## Cycle 1: the first strategy matrix (2026-09-28, mechanical, no agent runs)

**What was built:**
- [strategies.py](strategies.py) runs each strategy as real API calls against the replica.
- [probes.py](probes.py) has 9 probe seeds, each isolating one candidate hiding place.
- Results are in `matrix.json`.

**What ran:** every strategy of each service on every probe (5–6 strategies per service, one environment per probe).

| Probe (place) | Strategies that miss a match | Strategies that find all |
|---|---|---|
| BX-TREE (subfolders, 1–2 levels) | list named folder (default and limit 1000); search by the folder's name | search `pdf` below the folder (limit 200); list the tree |
| BX-PAGE (150-item folder) | list named folder (default page); search by the folder's name | list named (limit 1000); search `pdf` below the folder |
| CL-OWNED (owned secondary calendars) | primary only (with or without text search) | calendar list → each calendar (any variant) |
| **CL-HIDDEN (an owned calendar hidden in the list)** | primary only; calendar list (default); calendar list (owner only) | calendar list with `showHidden=true` → each |
| LN-PAGE (70 issues) | all issues (default page of 50) | all issues (first 250); named team; server filter |
| LN-SUBTEAM (2 sub-teams) | named team's issues; server filter on the named team | all issues (the workspace is small); team tree |
| SK-PRIVATE (a private channel in a name-prefix scope) | named channel's history; channel list (default types) | search (text); channel list with private types |
| SK-HISTORY (140 messages) | named channel history (default 100) | history (limit 999); search |
| SK-SEARCH (34 other messages match the words) | search (default count 20); history (default) | search (count 100); history (limit 999) |

**What was learned:**
- **Quantity placements never hide from the generous variant.** Beyond-the-first-page fails in all four services,
  as the pilot's routes predicted. Page size is not a hiding place for an agent that asks for big pages.
- **One placement defeats every shortcut tried: a hidden calendar the actor owns.** Only `showHidden=true` finds
  it. Hiding here comes from a visibility default, not from quantity or structure.
- **A container scope hides a match only when no single query spans the containers:**
  - a Box tree falls to one search below the folder whenever the condition is searchable (here the `pdf`
    extension);
  - Linear sub-teams fall to "list every issue" in a small workspace;
  - a private Slack channel falls to search, because search spans private channels and the condition is text.
- **The next hypothesis:** a hiding place works when a structural scope (a tree, a team hierarchy, channel
  privacy) combines with a condition that no search or filter can express. That combination forces enumeration of
  the containers.

**Next (cycle 2, mechanical):**
- a Box tree with a condition search cannot express (the last modifier, which listings show);
- Linear sub-teams in a workspace too large to list at once (over 250 issues; also check whether the replica caps
  `first`);
- a Slack request about channels (search does not search topics), with private channels in scope;
- Slack archived channels, to see what search and `exclude_archived` do.

## Cycle 2: conditions no search can express, and selection (2026-09-28, mechanical)

**What changed:**
- Box: a person-name search strategy.
- Linear:
  - `first: 1000`;
  - strategies that model selection as well as retrieval ("retrieve every issue, then keep the named team" against
    "…keep the team tree");
- Slack:
  - channel-level strategies (a request about channels, where search does not help);
  - `exclude_archived`.
- New probes: BX-TREE-MOD, LN-SUBTEAM-BIG, SK-CHANNELS, SK-ARCHIVED.

| Probe (place) | Lazy strategies that miss | Strategies that find all |
|---|---|---|
| **BX-TREE-MOD** (tree; condition: the last modifier; mixed file types) | list named (both); search by the folder's name, the extension, the person's name | list the tree only |
| LN-SUBTEAM(-BIG) (sub-teams; 5 or 285 issues) | named team's issues; server filter on the named team; all issues → keep the named team | all issues → keep the team tree; the team tree's issues |
| **SK-CHANNELS** (a request about channels; 2 of the 4 are private) | search (it does not cover topics); channel list (default types) | channel list with private types only |
| SK-ARCHIVED (an archived channel in the scope) | named channel history; channel list with `exclude_archived` | search (it covers archived channels); channel list (default) |

**What was learned:**
- **The hypothesis holds on these probes.** A structural scope hides a match when the condition cannot be put into a
  search or a filter:
  - the last modifier in Box (real Box search has no modifier filter, and search needs a query term);
  - channel topics in Slack (search covers messages, not topics).
- **Laziness can be in the selection, not the retrieval.** In Linear an agent can fetch every issue and still drop
  the sub-teams' issues by keeping only the named team. The strategies must model both steps. With selection
  modeled, sub-teams hide in a small workspace too.
- **Workspace size does not help in the replica.** The replica does not cap `first` (1000 works; real Linear's
  documented maximum is 250), so "list everything" always fits in one page here.
- **Archived channels are a weak hiding place.** Only an agent that passes `exclude_archived=true` misses them;
  search and the default listing include them.
- **For Slack message requests, no hiding place survives search** in these probes. Search spans every channel the
  bot is in (private and archived included) and matches the text.

**The candidate lazy-proof placements, one per service, for agent tests (cycle 3):**
- **Box:** a folder tree (depth 1 and 2), with a condition listings show but search cannot express (the last
  modifier).
- **Calendar:** an owned calendar that is hidden in the calendar list.
- **Linear:** sub-teams (depth 1 and 2), with the scope stated. The stated scope hands the hiding place to the
  agent, which is recorded.
- **Slack:** a request about channels, with private channels in scope.
