"""Linear pilot cases (manual design). Rows clone required fields from the benchmark seed."""
from __future__ import annotations

import copy
import json

from functools import partial

from grounding.paths import REPO_ROOT
from grounding.runs.fact_coverage_01.pilot.common import (DROP, REPLACE, SPLIT, SUB, claim, e, f, n, q, ref)

TEMPLATE = json.loads((REPO_ROOT / "backend/seeds/linear/linear_expanded.json").read_text())
ORG = "org-northwind"
ACTOR = "u-actor"
T0 = "2026-06-01T09:00:00"
PEOPLE = {"actor": "Jordan Lee", "maya": "Maya Chen", "priya": "Priya Nair", "leo": "Leo Park", "sam": "Sam Rivera",
          "dana": "Dana Whitfield", "omar": "Omar Haddad"}
PRIORITY = {0: "No priority", 1: "Urgent", 2: "High", 3: "Medium", 4: "Low"}
STATES = [("Backlog", "backlog"), ("Todo", "unstarted"), ("In Progress", "started"), ("In Review", "started"),
          ("Done", "completed"), ("Canceled", "canceled")]


class Seed:
    def __init__(self, people=None):
        self.t = {k: [] for k in ["organizations", "users", "teams", "workflow_states", "team_memberships", "projects",
                                  "project_milestones", "project_statuses", "cycles", "issue_labels", "issues",
                                  "issue_label_issue_association", "comments", "attachments", "issue_relations",
                                  "documents", "initiatives", "initiative_to_projects", "issue_subscriber_user_association"]}
        org = copy.deepcopy(TEMPLATE["organizations"][0])
        org.update(id=ORG, name="Northwind", urlKey="northwind")
        self.t["organizations"].append(org)
        self.issue_numbers = {}
        for key, name in (people or PEOPLE).items():
            self.user(key, name)

    def uid(self, key):
        return ACTOR if key == "actor" else "u-" + key

    def user(self, key, name, **kw):
        row = copy.deepcopy(TEMPLATE["users"][0])
        handle = name.lower().replace(" ", ".")
        row.update(id=self.uid(key), name=name, displayName=name.split()[0].lower(), email=f"{handle}@northwind.example",
                   organizationId=ORG, inviteHash=f"inv-{key}", url=f"https://linear.app/northwind/profiles/{key}",
                   initials="".join(p[0] for p in name.split()), isMe=False, active=True, admin=False, guest=False,
                   app=False)
        row.update(kw)
        self.t["users"].append(row)
        return row["id"]

    def team(self, tid, name, key, parent=None):
        row = copy.deepcopy(TEMPLATE["teams"][0])
        row.update(id=tid, name=name, key=key, displayName=name, organizationId=ORG, inviteHash=f"team-{tid}",
                   description=f"{name} team", issueCount=0, parentId=parent)
        self.t["teams"].append(row)
        for i, (sname, stype) in enumerate(STATES):
            self.t["workflow_states"].append({"id": f"{tid}-st-{i}", "teamId": tid, "name": sname, "type": stype,
                                              "color": "#95a2b3", "position": float(i), "createdAt": T0, "updatedAt": T0})
        return tid

    def state(self, team, name):
        return next(s["id"] for s in self.t["workflow_states"] if s["teamId"] == team and s["name"] == name)

    def member(self, team, user, owner=False):
        self.t["team_memberships"].append({"id": f"tm-{team}-{user}", "userId": self.uid(user), "teamId": team,
                                           "owner": owner, "sortOrder": 0.0, "createdAt": T0, "updatedAt": T0})

    def label(self, lid, name, team=None, parent=None, group=False):
        self.t["issue_labels"].append({"id": lid, "name": name, "teamId": team, "organizationId": ORG, "parentId": parent,
                                       "isGroup": group, "color": "#EB5757", "createdAt": T0, "updatedAt": T0})
        return lid

    def issue(self, iid, team, title, *, state="Todo", assignee=None, creator="actor", priority=0, estimate=None,
              due=None, project=None, milestone=None, cycle=None, parent=None, labels=(), description="",
              created=T0, subscribers=()):
        key = next(t["key"] for t in self.t["teams"] if t["id"] == team)
        number = self.issue_numbers.get(iid) or (sum(1 for i in self.t["issues"] if i["teamId"] == team) + 1)
        if isinstance(iid, tuple):
            iid, number = iid
        row = copy.deepcopy(TEMPLATE["issues"][0])
        row.update(id=iid, identifier=f"{key}-{number}", number=float(number), title=title, description=description,
                   teamId=team, stateId=self.state(team, state), assigneeId=self.uid(assignee) if assignee else None,
                   creatorId=self.uid(creator), priority=float(priority), priorityLabel=PRIORITY[priority],
                   estimate=estimate, dueDate=due, projectId=project, projectMilestoneId=milestone, cycleId=cycle,
                   parentId=parent, labelIds=list(labels), branchName=f"{key.lower()}-{number}",
                   url=f"https://linear.app/northwind/issue/{key}-{number}", createdAt=created, updatedAt=created)
        self.t["issues"].append(row)
        for lab in labels:
            self.t["issue_label_issue_association"].append({"issue_id": iid, "issue_label_id": lab})
        for sub in subscribers:
            self.t["issue_subscriber_user_association"].append({"issue_id": iid, "user_id": self.uid(sub)})
        return iid

    def status(self, sid, name, stype, position):
        self.t["project_statuses"].append({"id": sid, "organizationId": ORG, "name": name, "type": stype,
                                           "color": "#5e6ad2", "position": float(position), "indefinite": False,
                                           "createdAt": T0, "updatedAt": T0})
        return sid

    def project(self, pid, name, *, lead=None, creator="actor", status=None, state="started", start=None, target=None,
                priority=0, description=""):
        self.t["projects"].append({
            "id": pid, "name": name, "description": description, "leadId": self.uid(lead) if lead else None,
            "creatorId": self.uid(creator), "statusId": status, "state": state, "startDate": start, "targetDate": target,
            "priority": float(priority), "priorityLabel": PRIORITY[priority], "prioritySortOrder": 0.0,
            "color": "#5e6ad2", "slugId": pid, "url": f"https://linear.app/northwind/project/{pid}", "sortOrder": 0.0,
            "labelIds": [], "progress": 0.0, "scope": 0.0, "currentProgress": {}, "progressHistory": {},
            "completedIssueCountHistory": [], "completedScopeHistory": [], "inProgressScopeHistory": [],
            "issueCountHistory": [], "scopeHistory": [], "frequencyResolution": "weekly",
            "slackIssueComments": False, "slackIssueStatuses": False, "slackNewIssue": False,
            "createdAt": T0, "updatedAt": T0})
        return pid

    def milestone(self, mid, project, name, target=None, status="unstarted"):
        self.t["project_milestones"].append({"id": mid, "projectId": project, "name": name, "targetDate": target,
                                             "status": status, "progress": 0.0, "currentProgress": {},
                                             "progressHistory": {}, "sortOrder": 0.0, "createdAt": T0, "updatedAt": T0})
        return mid

    def cycle(self, cid, team, number, starts, ends, *, active=False, nxt=False, past=False, future=False, prev=False):
        self.t["cycles"].append({"id": cid, "teamId": team, "number": float(number), "name": f"Cycle {number}",
                                 "startsAt": starts, "endsAt": ends, "isActive": active, "isNext": nxt, "isPast": past,
                                 "isFuture": future, "isPrevious": prev, "progress": 0.0, "currentProgress": {},
                                 "progressHistory": {}, "completedIssueCountHistory": [], "completedScopeHistory": [],
                                 "inProgressScopeHistory": [], "issueCountHistory": [], "scopeHistory": [],
                                 "createdAt": T0, "updatedAt": T0})
        return cid

    def comment(self, cid, issue, author, body, parent=None, resolver=None):
        self.t["comments"].append({"id": cid, "issueId": issue, "userId": self.uid(author), "body": body,
                                   "bodyData": json.dumps({"type": "doc", "content": [{"type": "paragraph", "content": [
                                       {"type": "text", "text": body}]}]}),
                                   "parentId": parent, "resolvingUserId": self.uid(resolver) if resolver else None,
                                   "resolvedAt": T0 if resolver else None, "reactionData": {},
                                   "url": f"https://linear.app/northwind/comment/{cid}", "createdAt": T0, "updatedAt": T0})

    def relation(self, rid, issue, related, rtype="blocks"):
        title = {i["id"]: i["title"] for i in self.t["issues"]}
        self.t["issue_relations"].append({"id": rid, "issueId": issue, "relatedIssueId": related, "type": rtype,
                                          "issueTitle": title[issue], "relatedIssueTitle": title[related],
                                          "createdAt": T0, "updatedAt": T0})

    def attachment(self, aid, issue, title, source, creator, url):
        self.t["attachments"].append({"id": aid, "issueId": issue, "title": title, "subtitle": None, "url": url,
                                      "source": {"type": source}, "sourceType": source, "creatorId": self.uid(creator),
                                      "groupBySource": True, "metadata": {}, "createdAt": T0, "updatedAt": T0})

    def initiative(self, iid, name, owner=None, creator="actor", status="Active"):
        self.t["initiatives"].append({"id": iid, "name": name, "description": f"{name} initiative", "ownerId":
                                      self.uid(owner) if owner else None, "creatorId": self.uid(creator),
                                      "organizationId": ORG, "status": status, "slugId": iid, "sortOrder": 0.0,
                                      "frequencyResolution": "weekly", "url": f"https://linear.app/northwind/initiative/{iid}",
                                      "createdAt": T0, "updatedAt": T0})

    def document(self, did, title, creator, updater=None, project=None, initiative=None, team=None, content=""):
        self.t["documents"].append({"id": did, "title": title, "content": content, "creatorId": self.uid(creator),
                                    "updatedById": self.uid(updater or creator), "projectId": project,
                                    "initiativeId": initiative, "teamId": team, "slugId": did, "sortOrder": 0.0,
                                    "url": f"https://linear.app/northwind/document/{did}", "createdAt": T0, "updatedAt": T0})

    def seed(self):
        return {k: v for k, v in self.t.items() if v}


def user_named(key, name, fact=None):
    return n("users", [f(key, "name", "eq", name, fact)])


def gql(query):
    return ("POST", "/graphql", {"query": query})


ISSUE_FIELDS = "identifier title priority estimate dueDate assignee { name } creator { name } team { name } " \
               "state { name type } labels { nodes { name } } parent { identifier } cycle { number } project { name }"


# ---------------------------------------------------------------------------
def lin_01():
    s = Seed()
    s.team("t-mob", "Mobile", "MOB")
    s.team("t-web", "Web", "WEB")
    bug = s.label("lab-bug", "Bug")
    feat = s.label("lab-feat", "Feature")
    s.issue("i-mob-12", "t-mob", "Crash when rotating on the login screen", assignee="priya", creator="dana", priority=2, labels=[bug])
    s.issue("i-mob-13", "t-mob", "Push notifications arrive twice", assignee="leo", creator="priya", priority=2, labels=[bug])
    s.issue("i-mob-14", "t-mob", "Settings toggle misaligned on tablets", assignee="priya", creator="dana", priority=4, labels=[bug])
    s.issue("i-mob-15", "t-mob", "Offline mode epic", assignee="leo", creator="dana", priority=4, labels=[bug])
    s.issue("i-mob-16", "t-mob", "Cache images for offline mode", assignee="priya", creator="dana", priority=2, parent="i-mob-15")
    s.issue("i-mob-17", "t-mob", "Add biometric login", assignee="priya", creator="dana", priority=2, labels=[feat])
    s.issue("i-web-21", "t-web", "Checkout button unresponsive on Safari", assignee="priya", creator="dana", priority=2, labels=[bug])
    labels = e("e_label", "id", "issue_id", n("issue_label_issue_association", [], [
        e("e_ln", "issue_label_id", "id", n("issue_labels", [f("f_lname", "name", "eq", "Bug", "A:IssueLabel.name")]))]),
        "R:issue_label_issue_association")
    query = q("issues", [f("f_prio", "priority", "eq", 2.0, "A:Issue.priority")], [
        e("e_team", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Mobile", "A:Team.name")]), "R:Issue.teamId"),
        e("e_asg", "assigneeId", "id", user_named("f_asg", "Priya Nair"), "R:Issue.assigneeId"),
        labels])
    parent_label = e("e_label", "parentId", "id", n("issues", [], [
        e("e_pl", "id", "issue_id", n("issue_label_issue_association", [], [
            e("e_pln", "issue_label_id", "id", n("issue_labels", [f("x", "name", "eq", "Bug")]))]))]))
    claims = [
        claim("R:Issue.assigneeId", "i-mob-13", SUB("e_asg", e("e_asg", "creatorId", "id", user_named("x", "Priya Nair"))),
              "Priya created MOB-13; Leo is assigned.", alternative="Issue.creatorId"),
        claim("A:Issue.priority", "i-mob-14", DROP("f_prio"), "Low priority."),
        claim("R:issue_label_issue_association", "i-mob-16", SUB("e_label", parent_label),
              "Only the parent epic carries the Bug label.", alternative="label on the parent issue"),
        claim("A:IssueLabel.name", "i-mob-17", DROP("f_lname"), "Labeled Feature."),
        claim("A:Team.name", "i-web-21", DROP("f_team"), "Web team."),
    ]
    dest = q("workflow_states", [f("f_sname", "name", "eq", "In Review", "A:WorkflowState.name")], [
        e("e_steam", "teamId", "id", n("teams", [f("f_steam", "name", "eq", "Mobile")]), "R:WorkflowState.teamId")])
    dest_claims = [
        claim("R:WorkflowState.teamId", "t-web-st-3", DROP("e_steam"), "The Web team's In Review state.",
              alternative="same-named state of another team"),
        claim("A:WorkflowState.name", "t-mob-st-2", DROP("f_sname"), "Mobile's In Progress state."),
    ]
    return {
        "case_id": "LIN-01", "domain": "linear", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Move the Mobile team's high-priority bug that's assigned to Priya Nair to In Review.",
        "references": [
            ref("LIN-01.r1", "Resolve the issue", "The Mobile issue with High priority, the Bug label and assignee Priya "
                "Nair; only MOB-1 (i-mob-12).", "target", query, ["i-mob-12"], claims,
                paths=[{"entities": ["issues", "users"], "relationships": ["issues.assigneeId"]},
                       {"entities": ["issues", "teams"], "relationships": ["issues.teamId"]},
                       {"entities": ["issues", "issue_labels"], "relationships": ["issue_label_issue_association"]}],
                identifying=["issues.priority", "issues.teamId", "teams.name", "issues.assigneeId", "users.name",
                             "issue_label_issue_association", "issue_labels.name"], written=["issues.stateId"],
                effect={"table": "issues", "changes": ["update"]}),
            ref("LIN-01.r2", "Resolve the destination state", "Mobile's In Review workflow state.", "target", dest,
                ["t-mob-st-3"], dest_claims,
                paths=[{"entities": ["workflow_states", "teams"], "relationships": ["workflow_states.teamId"]}],
                identifying=["workflow_states.name", "workflow_states.teamId", "teams.name"], written=["issues.stateId"],
                effect={"table": "issues", "changes": ["update"], "field": "stateId", "all": True}),
        ],
        "probes": [gql("{ issues(first: 50) { nodes { " + ISSUE_FIELDS + " } } }")],
    }


# ---------------------------------------------------------------------------
def lin_02():
    s = Seed()
    s.team("t-eng", "Engineering", "ENG")
    s.team("t-mob", "Mobile", "MOB")
    for i in range(1, 42):
        s.issue(f"i-eng-f{i}", "t-eng", f"Engineering chore {i}", state="Done")
    s.issue("i-eng-42", "t-eng", "Release 2.3 checklist", assignee="leo", creator="dana")
    s.issue("i-eng-43", "t-eng", "Release 2.3 QA sign-off", assignee="sam", creator="dana", parent="i-eng-42")
    for i in range(1, 42):
        s.issue(f"i-mob-f{i}", "t-mob", f"Mobile chore {i}", state="Done")
    s.issue("i-mob-42", "t-mob", "Release 4.1 checklist", assignee="leo", creator="dana")
    s.comment("c-1", "i-eng-42", "leo", "Please update the release notes before Friday.")
    s.comment("c-2", "i-eng-42", "sam", "Can we postpone the release to next week?")
    s.comment("c-3", "i-eng-43", "leo", "We should postpone the release until QA signs off.")
    s.comment("c-4", "i-mob-42", "leo", "Let's postpone the release by a week.")
    query = q("comments", [f("f_body", "body", "contains_ci", "postpone", "A:Comment.body")], [
        e("e_author", "userId", "id", user_named("f_author", "Leo Park"), "R:Comment.userId"),
        e("e_issue", "issueId", "id", n("issues", [f("f_ident", "identifier", "eq", "ENG-42", "A:Issue.identifier")]),
          "R:Comment.issueId")])
    by_assignee = e("e_author", "issueId", "id", n("issues", [], [e("e_ia", "assigneeId", "id", user_named("x", "Leo Park"))]))
    on_child = e("e_issue", "issueId", "id", n("issues", [], [
        e("e_par", "parentId", "id", n("issues", [f("x", "identifier", "eq", "ENG-42")]))]))
    claims = [
        claim("A:Comment.body", "c-1", DROP("f_body"), "Leo's comment on ENG-42 is about release notes."),
        claim("R:Comment.userId", "c-2", SUB("e_author", by_assignee),
              "Sam asked to postpone on ENG-42, which is assigned to Leo.", alternative="Issue.assigneeId"),
        claim("R:Comment.issueId", "c-3", SUB("e_issue", on_child),
              "Leo asked to postpone on ENG-43, a sub-issue of ENG-42.", alternative="comment on a sub-issue"),
        claim("A:Issue.identifier", "c-4", DROP("f_ident"), "Leo asked to postpone on MOB-42."),
    ]
    return {
        "case_id": "LIN-02", "domain": "linear", "form": "absent", "mode": "absent", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Delete the comment Leo Park left on ENG-42 asking to postpone the release.",
        "references": [ref("LIN-02.r1", "Resolve the comment", "A comment by Leo Park on ENG-42 asking to postpone the "
                           "release. None: Leo's ENG-42 comment concerns release notes; the postpone requests are "
                           "Sam's on ENG-42, Leo's on sub-issue ENG-43 and Leo's on MOB-42.", "target", query, [], claims,
                           paths=[{"entities": ["comments", "users"], "relationships": ["comments.userId"]},
                                  {"entities": ["comments", "issues"], "relationships": ["comments.issueId"]}],
                           identifying=["comments.body", "comments.userId", "users.name", "comments.issueId",
                                        "issues.identifier"],
                           effect={"table": "comments", "changes": ["delete", "update"]})],
        "probes": [gql('{ issue(id: "i-eng-42") { identifier comments { nodes { body user { name } } } children { nodes { identifier } } } }')],
    }


# ---------------------------------------------------------------------------
def lin_03():
    s = Seed()
    s.team("t-web", "Web", "WEB")
    s.project("p-1", "Checkout Redesign", lead="maya", creator="dana")
    s.project("p-2", "Checkout Redesign", lead="sam", creator="maya")
    s.project("p-3", "Payments Revamp", lead="maya", creator="maya")
    s.project("p-4", "Growth Experiments", lead="sam", creator="sam")
    s.milestone("m-1", "p-1", "Beta", target="2026-10-15")
    s.milestone("m-2", "p-1", "GA", target="2026-11-15")
    s.milestone("m-3", "p-2", "Beta", target="2026-10-10")
    s.milestone("m-4", "p-3", "Beta", target="2026-10-12")
    s.milestone("m-5", "p-4", "Beta", target="2026-10-20")
    query = q("project_milestones", [f("f_mname", "name", "eq", "Beta", "A:ProjectMilestone.name")], [
        e("e_proj", "projectId", "id", n("projects", [f("f_pname", "name", "eq", "Checkout Redesign", "A:Project.name")], [
            e("e_lead", "leadId", "id", user_named("f_lead", "Maya Chen"), "R:Project.leadId")]),
          "R:ProjectMilestone.projectId")])
    creator_alt = e("e_lead", "creatorId", "id", user_named("x", "Maya Chen"))
    claims = [
        claim("A:ProjectMilestone.name", "m-2", DROP("f_mname"), "The GA milestone of the right project."),
        claim("R:Project.leadId", "m-3", SUB("e_lead", creator_alt),
              "The other Checkout Redesign project was created by Maya but is led by Sam.", alternative="Project.creatorId"),
        claim("A:Project.name", "m-4", DROP("f_pname"), "Beta of Payments Revamp, also led by Maya."),
        claim("R:ProjectMilestone.projectId", "m-5", DROP("e_proj"), "Beta of a project Sam leads."),
    ]
    return {
        "case_id": "LIN-03", "domain": "linear", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Set the target date of the Beta milestone in the Checkout Redesign project that Maya Chen leads to "
                  "October 30, 2026.",
        "references": [ref("LIN-03.r1", "Resolve the milestone", "Beta milestone of the Checkout Redesign project led by "
                           "Maya Chen; only m-1.", "target", query, ["m-1"], claims,
                           paths=[{"entities": ["project_milestones", "projects", "users"],
                                   "relationships": ["project_milestones.projectId", "projects.leadId"]}],
                           identifying=["project_milestones.name", "project_milestones.projectId", "projects.name",
                                        "projects.leadId", "users.name"], written=["project_milestones.targetDate"],
                           effect={"table": "project_milestones", "changes": ["update"]})],
        "probes": [gql("{ projectMilestones { nodes { id name targetDate project { name lead { name } creator { name } } } } }")],
    }


# ---------------------------------------------------------------------------
def lin_04():
    s = Seed()
    s.team("t-eng", "Engineering", "ENG")
    for i in range(1, 7):
        s.issue(f"i-eng-f{i}", "t-eng", f"Engineering chore {i}", state="Done")
    s.issue("i-eng-7", "t-eng", "Upgrade auth library", assignee="leo")
    s.issue("i-eng-8", "t-eng", "Refactor session store", assignee="sam")
    s.issue("i-eng-9", "t-eng", "Run database migration for the v2 schema", assignee="priya")
    s.issue("i-eng-10", "t-eng", "Automate database backups", assignee="omar")
    s.relation("r-1", "i-eng-7", "i-eng-9", "blocks")     # ENG-7 blocks the migration (reverse)
    s.relation("r-2", "i-eng-9", "i-eng-7", "related")    # related, not blocking
    s.relation("r-3", "i-eng-10", "i-eng-7", "blocks")    # a backup issue blocks ENG-7
    s.relation("r-4", "i-eng-9", "i-eng-8", "blocks")     # the migration blocks ENG-8
    query = q("issue_relations", [f("f_type", "type", "eq", "blocks", "A:IssueRelation.type")], [
        e("e_src", "issueId", "id", n("issues", [f("f_title", "title", "contains_ci", "migration", "A:Issue.title")]),
          "R:IssueRelation.issueId"),
        e("e_dst", "relatedIssueId", "id", n("issues", [f("f_dst", "identifier", "eq", "ENG-7")]),
          "R:IssueRelation.relatedIssueId")])
    reversed_q = q("issue_relations", [f("f_type", "type", "eq", "blocks")], [
        e("e_src", "relatedIssueId", "id", n("issues", [f("f_title", "title", "contains_ci", "migration")])),
        e("e_dst", "issueId", "id", n("issues", [f("f_dst", "identifier", "eq", "ENG-7")]))])
    claims = [
        claim("R:IssueRelation.issueId", "r-1", REPLACE(reversed_q, "relation direction reversed"),
              "ENG-7 blocks the migration issue, not the other way round.", alternative="IssueRelation.relatedIssueId"),
        claim("A:IssueRelation.type", "r-2", DROP("f_type"), "The migration issue is only related to ENG-7."),
        claim("A:Issue.title", "r-3", DROP("f_title"), "A database-backup issue blocks ENG-7."),
        claim("R:IssueRelation.relatedIssueId", "r-4", DROP("e_dst"), "The migration issue blocks ENG-8."),
    ]
    return {
        "case_id": "LIN-04", "domain": "linear", "form": "absent", "mode": "absent", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "ENG-7 is blocked by the database migration issue. Remove that blocking relation.",
        "references": [ref("LIN-04.r1", "Resolve the blocking relation", "A blocks relation from the database migration "
                           "issue to ENG-7. None: ENG-7 blocks the migration; the migration is only related to ENG-7; "
                           "a backup issue blocks ENG-7.", "target", query, [], claims,
                           paths=[{"entities": ["issue_relations", "issues"], "relationships": ["issue_relations.issueId"]},
                                  {"entities": ["issue_relations", "issues"], "relationships": ["issue_relations.relatedIssueId"]}],
                           identifying=["issue_relations.type", "issue_relations.issueId", "issue_relations.relatedIssueId",
                                        "issues.title", "issues.identifier"],
                           effect={"table": "issue_relations", "changes": ["delete", "update"]})],
        "probes": [gql('{ issue(id: "i-eng-7") { identifier relations { nodes { type relatedIssue { identifier } } } '
                       'inverseRelations { nodes { type issue { identifier title } } } } }')],
    }


# ---------------------------------------------------------------------------
def lin_05():
    s = Seed()
    s.team("t-plt", "Platform", "PLT")
    s.team("t-web", "Web", "WEB")
    s.cycle("cy-p13", "t-plt", 13, "2026-08-31T00:00:00", "2026-09-13T23:59:59", past=True, prev=True)
    s.cycle("cy-p14", "t-plt", 14, "2026-09-14T00:00:00", "2026-09-27T23:59:59", active=True)
    s.cycle("cy-p15", "t-plt", 15, "2026-09-28T00:00:00", "2026-10-11T23:59:59", nxt=True, future=True)
    s.cycle("cy-w14", "t-web", 14, "2026-09-14T00:00:00", "2026-09-27T23:59:59", active=True)
    s.issue("i-plt-1", "t-plt", "Rotate service credentials", estimate=5.0, due="2026-09-15", cycle="cy-p14", assignee="leo")
    s.issue("i-plt-2", "t-plt", "Split the billing worker", state="In Progress", estimate=8.0, due="2026-09-20", cycle="cy-p14", assignee="sam")
    s.issue("i-plt-3", "t-plt", "Migrate cron jobs", estimate=8.0, due="2026-09-10", cycle="cy-p15", assignee="leo")
    s.issue("i-web-4", "t-web", "Upgrade the CDN config", estimate=5.0, due="2026-09-12", cycle="cy-w14", assignee="omar")
    s.issue("i-plt-5", "t-plt", "Tune database pool sizes", estimate=3.0, due="2026-09-15", cycle="cy-p14", assignee="sam")
    s.issue("i-plt-6", "t-plt", "Remove legacy queue", state="Done", estimate=5.0, due="2026-09-10", cycle="cy-p14", assignee="leo")
    s.issue("i-plt-7", "t-plt", "Add request tracing", estimate=5.0, due="2026-09-30", cycle="cy-p14", assignee="sam")
    s.issue("i-plt-8", "t-plt", "Harden the deploy script", estimate=8.0, due="2026-09-01", assignee="leo")
    cyc = n("cycles", [f("f_active", "isActive", "eq", True)], [
        e("e_cteam", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Platform")]), "R:Cycle.teamId")])
    open_state = e("e_open", "stateId", "id", n("workflow_states", [f("f_stype", "type", "not_in", ["completed", "canceled"])]))
    query = q("issues", [f("f_est", "estimate", "ge", 5.0, "A:Issue.estimate"),
                         f("f_due", "dueDate", "lt", "2026-09-23", "A:Issue.dueDate")],
              [e("e_cycle", "cycleId", "id", cyc, "R:Issue.cycleId"), open_state])

    def variant(active_field="isActive", with_open=True):
        c = n("cycles", [f("f_active", active_field, "eq", True)], [
            e("e_cteam", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Platform")]))])
        return q("issues", [f("f_est", "estimate", "ge", 5.0), f("f_due", "dueDate", "lt", "2026-09-23")],
                 [e("e_cycle", "cycleId", "id", c)] + ([open_state] if with_open else []))
    claims = [
        claim("D:current_cycle", "i-plt-3", REPLACE(variant("isNext"), "current cycle replaced by next cycle"),
              "In Platform's next cycle.", alternative="next cycle"),
        claim("R:Cycle.teamId", "i-web-4", DROP("e_cteam"), "In the Web team's active cycle 14.",
              alternative="another team's active cycle"),
        claim("A:Issue.estimate", "i-plt-5", DROP("f_est"), "Estimated at 3."),
        claim("D:overdue", "i-plt-6", REPLACE(variant(with_open=False), "open-state condition dropped"),
              "Past due but already Done."),
        claim("A:Issue.dueDate", "i-plt-7", DROP("f_due"), "Due September 30."),
        claim("R:Issue.cycleId", "i-plt-8", DROP("e_cycle"), "Overdue and large, but not in any cycle."),
    ]
    return {
        "case_id": "LIN-05", "domain": "linear", "form": "present", "mode": "multiple", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Today is September 23, 2026. Move every open issue in the Platform team's current cycle that's "
                  "estimated at 5 points or more and is past its due date into the team's next cycle.",
        "references": [ref("LIN-05.r1", "Resolve the overdue large issues", "Open Platform issues in the active Platform "
                           "cycle with estimate >= 5 and due before 2026-09-23: PLT-1 and PLT-2.", "target", query,
                           ["i-plt-1", "i-plt-2"], claims,
                           paths=[{"entities": ["issues", "cycles", "teams"], "relationships": ["issues.cycleId", "cycles.teamId"]},
                                  {"entities": ["issues", "workflow_states"], "relationships": ["issues.stateId"]}],
                           identifying=["issues.estimate", "issues.dueDate", "issues.cycleId", "cycles.isActive",
                                        "cycles.teamId", "teams.name", "workflow_states.type"], written=["issues.cycleId"],
                           effect={"table": "issues", "changes": ["update"]})],
        "probes": [gql("{ cycles { nodes { id number isActive isNext team { name } } } }"),
                   gql("{ issues(first: 50) { nodes { " + ISSUE_FIELDS + " } } }")],
    }


# ---------------------------------------------------------------------------
def lin_06():
    people = dict(PEOPLE, ava="Ava Brooks", noah="Noah Kim", liam="Liam Ortiz", emma="Emma Stone", mia="Mia Wong",
                  ethan="Ethan Cole", zoe="Zoe Park")
    s = Seed(people)
    for key in ("ava", "noah", "liam", "mia", "ethan", "zoe"):
        next(u for u in s.t["users"] if u["id"] == s.uid(key))["admin"] = True
    next(u for u in s.t["users"] if u["id"] == s.uid("liam"))["active"] = False
    s.team("t-des", "Design", "DES")
    s.team("t-dsy", "Design Systems", "DSY", parent="t-des")
    s.team("t-web", "Web", "WEB")
    s.member("t-des", "ava", owner=True)
    s.member("t-des", "noah", owner=True)
    s.member("t-des", "liam", owner=True)
    s.member("t-des", "emma", owner=True)
    s.member("t-des", "mia")
    s.member("t-des", "ethan")
    s.member("t-web", "ethan", owner=True)
    s.member("t-dsy", "zoe", owner=True)
    members = n("team_memberships", [f("f_owner", "owner", "eq", True, "A:TeamMembership.owner")], [
        e("e_mteam", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Design")]))])
    query = q("users", [f("f_active", "active", "eq", True, "A:User.active"), f("f_admin", "admin", "eq", True, "A:User.admin")],
              [e("e_mem", "id", "userId", members, "B:TeamMembership")])
    sub_team = e("e_mem", "id", "userId", n("team_memberships", [f("f_owner", "owner", "eq", True)], [
        e("e_mteam", "teamId", "id", n("teams", [], [
            e("e_up", "parentId", "id", n("teams", [f("f_team", "name", "eq", "Design")]), closure="star")]))]))
    claims = [
        claim("A:User.active", "u-liam", DROP("f_active"), "Liam owns Design but is deactivated."),
        claim("A:User.admin", "u-emma", DROP("f_admin"), "Emma owns Design but is not an admin."),
        claim("A:TeamMembership.owner", "u-mia", DROP("f_owner"), "Mia is a Design member, not an owner."),
        claim("B:TeamMembership", "u-ethan", SPLIT("e_mem", ["f_owner"], ["e_mteam"]),
              "Ethan owns Web and is a plain member of Design."),
        claim("H:Team.parentId", "u-zoe", SUB("e_mem", sub_team), "Zoe owns the Design Systems sub-team.",
              alternative="owner of a sub-team"),
    ]
    labels = {s.uid(k): v for k, v in people.items() if k in ("ava", "noah", "liam", "emma", "mia", "ethan", "zoe")}
    return {
        "case_id": "LIN-06", "domain": "linear", "form": "present", "mode": "multiple", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Which active admins are owners of the Design team itself (not its sub-teams)? Just list their names.",
        "references": [ref("LIN-06.r1", "Resolve the owners to report", "Active admin users with an owner membership in "
                           "the Design team: Ava Brooks and Noah Kim.", "evidence", query, ["u-ava", "u-noah"], claims,
                           paths=[{"entities": ["users", "team_memberships", "teams"],
                                   "relationships": ["team_memberships.userId", "team_memberships.teamId"]}],
                           identifying=["users.active", "users.admin", "team_memberships.owner", "team_memberships.teamId",
                                        "teams.name"], answer=["users.name"], labels=labels)],
        "probes": [gql("{ teamMemberships { nodes { owner user { name admin active } team { name parent { name } } } } }")],
    }


# ---------------------------------------------------------------------------
def lin_07():
    s = Seed()
    s.team("t-grw", "Growth", "GRW")
    s.initiative("in-grw", "Growth", owner="sam")
    s.initiative("in-ret", "Retention", owner="dana")
    s.project("p-ref", "Referral program", lead="maya")
    s.t["initiative_to_projects"].append({"id": "itp-1", "initiativeId": "in-grw", "projectId": "p-ref", "sortOrder": 0.0,
                                          "createdAt": T0, "updatedAt": T0})
    s.document("d-1", "Q4 planning draft", "maya", "sam", initiative="in-grw", content="Pricing and channel bets for Q4.")
    s.document("d-2", "Growth metrics", "sam", "maya", initiative="in-grw", content="Weekly activation metrics.")
    s.document("d-3", "Referral launch plan", "maya", project="p-ref", content="Launch steps for referrals.")
    s.document("d-4", "Retention ideas", "maya", initiative="in-ret", content="Win-back campaign ideas.")
    query = q("documents", [], [
        e("e_dcreator", "creatorId", "id", user_named("f_dc", "Maya Chen"), "R:Document.creatorId"),
        e("e_init", "initiativeId", "id", n("initiatives", [f("f_iname", "name", "eq", "Growth", "A:Initiative.name")]),
          "R:Document.initiativeId")])
    via_project = e("e_init", "projectId", "id", n("projects", [], [
        e("e_ip", "id", "projectId", n("initiative_to_projects", [], [
            e("e_ii", "initiativeId", "id", n("initiatives", [f("x", "name", "eq", "Growth")]))]))]))
    claims = [
        claim("R:Document.creatorId", "d-2", SUB("e_dcreator", e("e_dcreator", "updatedById", "id", user_named("x", "Maya Chen"))),
              "Maya last edited Growth metrics; Sam created it.", alternative="Document.updatedById"),
        claim("R:Document.initiativeId", "d-3", SUB("e_init", via_project),
              "Maya's doc belongs to Referral program, a project inside the Growth initiative.",
              alternative="document of a project in the initiative"),
        claim("A:Initiative.name", "d-4", DROP("f_iname"), "Maya's doc for the Retention initiative."),
    ]
    return {
        "case_id": "LIN-07", "domain": "linear", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Rename the doc Maya Chen created for the Growth initiative to \"Growth Q4 plan\".",
        "references": [ref("LIN-07.r1", "Resolve the document", "The document attached to the Growth initiative whose "
                           "creator is Maya Chen; only d-1.", "target", query, ["d-1"], claims,
                           paths=[{"entities": ["documents", "users"], "relationships": ["documents.creatorId"]},
                                  {"entities": ["documents", "initiatives"], "relationships": ["documents.initiativeId"]}],
                           identifying=["documents.creatorId", "users.name", "documents.initiativeId", "initiatives.name"],
                           written=["documents.title"], effect={"table": "documents", "changes": ["update"]})],
        "probes": [gql("{ documents { nodes { id title creator { name } updatedBy { name } initiative { name } project { name } } } }")],
    }


# ---------------------------------------------------------------------------
def lin_08():
    s = Seed()
    s.team("t-plt", "Platform", "PLT")
    planned = s.status("ps-planned", "Planned", "planned", 1)
    inprog = s.status("ps-started", "In Progress", "started", 2)
    paused = s.status("ps-paused", "Paused", "paused", 3)
    s.status("ps-done", "Completed", "completed", 4)
    s.project("p-1", "Search revamp", lead="priya", status=planned, state="started", target="2026-10-15", priority=3)
    s.project("p-2", "Billing cleanup", lead="priya", status=paused, state="paused", target="2026-10-20", priority=3)
    s.project("p-3", "Observability", lead="priya", status=inprog, state="started", start="2026-10-15",
              target="2026-12-01", priority=3)
    s.project("p-4", "Data retention", lead="sam", creator="priya", status=inprog, state="started", target="2026-10-20",
              priority=3)
    query = q("projects", [f("f_target", "targetDate", "lt", "2026-11-01", "A:Project.targetDate")], [
        e("e_status", "statusId", "id", n("project_statuses", [f("f_sname", "name", "eq", "In Progress", "A:ProjectStatus.name")]),
          "R:Project.statusId"),
        e("e_lead", "leadId", "id", user_named("f_lead", "Priya Nair"), "R:Project.leadId")])
    legacy = q("projects", [f("f_target", "targetDate", "lt", "2026-11-01"), f("f_state", "state", "eq", "started")],
               [e("e_lead", "leadId", "id", user_named("f_lead", "Priya Nair"))])
    by_start = q("projects", [f("f_start", "startDate", "lt", "2026-11-01")], [
        e("e_status", "statusId", "id", n("project_statuses", [f("f_sname", "name", "eq", "In Progress")])),
        e("e_lead", "leadId", "id", user_named("f_lead", "Priya Nair"))])
    claims = [
        claim("R:Project.statusId", "p-1", REPLACE(legacy, "status relation replaced by the legacy state string"),
              "Legacy state says started, but its status is Planned.", alternative="legacy Project.state"),
        claim("A:ProjectStatus.name", "p-2", DROP("f_sname"), "Paused."),
        claim("A:Project.targetDate", "p-3", REPLACE(by_start, "target date replaced by start date"),
              "Starts October 15 but targets December 1.", alternative="Project.startDate"),
        claim("R:Project.leadId", "p-4", SUB("e_lead", e("e_lead", "creatorId", "id", user_named("x", "Priya Nair"))),
              "Priya created Data retention; Sam leads it.", alternative="Project.creatorId"),
    ]
    return {
        "case_id": "LIN-08", "domain": "linear", "form": "absent", "mode": "absent", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Set the priority to Urgent on the in-progress project that Priya Nair leads and that's due before "
                  "November 1, 2026.",
        "references": [ref("LIN-08.r1", "Resolve the project", "An In Progress project led by Priya Nair with target "
                           "date before 2026-11-01. None.", "target", query, [], claims,
                           paths=[{"entities": ["projects", "project_statuses"], "relationships": ["projects.statusId"]},
                                  {"entities": ["projects", "users"], "relationships": ["projects.leadId"]}],
                           identifying=["projects.targetDate", "projects.statusId", "project_statuses.name",
                                        "projects.leadId", "users.name"], written=["projects.priority"],
                           effect={"table": "projects", "changes": ["update"]})],
        "probes": [gql('{ searchProjects(term: "a") { nodes { id name state startDate targetDate priority status { name } lead { name } creator { name } } } }')],
    }


# ---------------------------------------------------------------------------
def lin_09():
    s = Seed()
    s.team("t-web", "Web", "WEB")
    s.project("p-co", "Checkout", lead="dana")
    s.issue("i-1", "t-web", "Apple Pay button misplaced", project="p-co", creator="dana", assignee="sam")
    s.attachment("a-1", "i-1", "PR #481: Fix Apple Pay button", "github", "leo", "https://github.com/northwind/web/pull/481")
    s.issue("i-2", "t-web", "Tax total rounding error", project="p-co", creator="dana", assignee="sam")
    s.attachment("a-2", "i-2", "PR #482: Round tax totals", "github", "sam", "https://github.com/northwind/web/pull/482")
    s.attachment("a-3", "i-2", "Thread: rounding complaints", "slack", "leo", "https://northwind.slack.com/archives/C1/p1")
    s.issue("i-3", "t-web", "Coupon field redesign", project="p-co", creator="dana", assignee="sam")
    s.attachment("a-4", "i-3", "Coupon field mockups", "figma", "leo", "https://figma.com/file/coupon")
    s.issue("i-4", "t-web", "Saved cards not loading", project="p-co", creator="leo", assignee="sam")
    s.attachment("a-5", "i-4", "PR #483: Retry saved cards", "github", "sam", "https://github.com/northwind/web/pull/483")
    s.issue("i-6", "t-web", "Checkout performance epic", project="p-co", creator="dana", assignee="dana")
    s.issue("i-5", "t-web", "Lazy-load payment icons", parent="i-6", creator="dana", assignee="sam")
    s.attachment("a-6", "i-5", "PR #484: Lazy-load icons", "github", "leo", "https://github.com/northwind/web/pull/484")
    att = n("attachments", [f("f_src", "sourceType", "eq", "github", "A:Attachment.sourceType")], [
        e("e_acreator", "creatorId", "id", user_named("f_ac", "Leo Park"), "R:Attachment.creatorId")])
    query = q("issues", [], [
        e("e_proj", "projectId", "id", n("projects", [f("f_pname", "name", "eq", "Checkout")]), "R:Issue.projectId"),
        e("e_att", "id", "issueId", att, "B:Attachment.issueId")])
    by_issue_creator = q("issues", [], [
        e("e_proj", "projectId", "id", n("projects", [f("f_pname", "name", "eq", "Checkout")])),
        e("e_ic", "creatorId", "id", user_named("x", "Leo Park")),
        e("e_att", "id", "issueId", n("attachments", [f("f_src", "sourceType", "eq", "github")]))])
    parent_project = e("e_proj", "parentId", "id", n("issues", [], [
        e("e_pp", "projectId", "id", n("projects", [f("x", "name", "eq", "Checkout")]))]))
    claims = [
        claim("B:Attachment.issueId", "i-2", SPLIT("e_att", ["f_src"], ["e_acreator"]),
              "Its GitHub PR is Sam's; Leo attached a Slack thread."),
        claim("A:Attachment.sourceType", "i-3", DROP("f_src"), "Leo attached Figma mockups."),
        claim("R:Attachment.creatorId", "i-4", REPLACE(by_issue_creator, "attachment creator replaced by issue creator"),
              "Leo created the issue; Sam attached its PR.", alternative="Issue.creatorId"),
        claim("R:Issue.projectId", "i-5", SUB("e_proj", parent_project),
              "Only its parent epic is in the Checkout project.", alternative="project of the parent issue"),
    ]
    return {
        "case_id": "LIN-09", "domain": "linear", "form": "present", "mode": "single", "acting_user_id": ACTOR,
        "seed": s.seed(),
        "prompt": "Assign to Leo Park the Checkout project issue that has a GitHub pull request Leo attached.",
        "references": [ref("LIN-09.r1", "Resolve the issue", "The Checkout-project issue with a GitHub attachment "
                           "created by Leo Park; only i-1.", "target", query, ["i-1"], claims,
                           paths=[{"entities": ["issues", "projects"], "relationships": ["issues.projectId"]},
                                  {"entities": ["issues", "attachments", "users"],
                                   "relationships": ["attachments.issueId", "attachments.creatorId"]}],
                           identifying=["issues.projectId", "projects.name", "attachments.issueId",
                                        "attachments.sourceType", "attachments.creatorId", "users.name"],
                           written=["issues.assigneeId"], effect={"table": "issues", "changes": ["update"]})],
        "probes": [gql("{ attachments { nodes { title sourceType creator { name } issue { identifier creator { name } project { name } parent { identifier } } } } }")],
    }


# lin_08 dropped from runs: the mock returns null for project status (searchProjects/projects), so R:Project.statusId
# cannot be observed; kept here for the record.
CASES = [lin_01, lin_02, lin_03, lin_04, lin_05, lin_06, lin_07, lin_08, lin_09]


# ---------------------------------------------------------------------------
# Round 3: hierarchy and handle facts, each with a target-present and a no-target form.
def _form(case, form, present_expected):
    if form == "absent":
        case["variant_of"] = case["case_id"]
        case["case_id"] += "-A"
        case["form"], case["mode"] = "absent", "absent"
        for r in case["references"]:
            r["id"] = case["case_id"] + r["id"][r["id"].index("."):]
        case["references"][0]["expected"], case["references"][0]["resolution"] = [], "absent"
    else:
        case["references"][0]["expected"] = present_expected
    return case


def lin_10(form="present"):
    s = Seed()
    s.team("t-web", "Web", "WEB")
    s.issue(("i-epic", 1), "t-web", "Checkout revamp", assignee="sam", creator="dana")
    s.issue(("i-2", 2), "t-web", "Tax rules engine", assignee="leo", creator="dana", parent="i-epic")
    s.issue(("i-3", 3), "t-web", "Payment form", assignee="leo", creator="dana", parent="i-epic")
    s.issue(("i-4", 4), "t-web", "Card number validation", assignee="sam", creator="dana", parent="i-3")
    s.issue(("i-5", 5), "t-web", "Checkout analytics", assignee="dana", creator="dana")
    s.issue(("i-6", 6), "t-web", "Funnel dashboard", assignee="sam", creator="dana", parent="i-5")
    s.issue(("i-8", 8), "t-web", "Address autocomplete", assignee="leo", creator="sam", parent="i-epic")
    if form != "absent":
        s.issue(("i-9", 9), "t-web", "Saved payment methods", assignee="sam", creator="dana", parent="i-epic")
    query = q("issues", [], [
        e("e_par", "parentId", "id", n("issues", [f("f_ptitle", "title", "eq", "Checkout revamp", "A:Issue.title")]),
          "H:Issue.parentId"),
        e("e_asg", "assigneeId", "id", user_named("f_asg", "Sam Rivera"), "R:Issue.assigneeId")])
    nested = q("issues", [], [
        e("e_par", "parentId", "id", n("issues", [f("f_ptitle", "title", "eq", "Checkout revamp")]), closure=True),
        e("e_asg", "assigneeId", "id", user_named("f_asg", "Sam Rivera"))])
    claims = [
        claim("H:Issue.parentId", "i-4", REPLACE(nested, "direct parent replaced by any ancestor"),
              "Card number validation is a sub-issue of Payment form, i.e. a grandchild of the epic.",
              alternative="grandchild"),
        claim("R:Issue.assigneeId", "i-8", SUB("e_asg", e("e_asg", "creatorId", "id", user_named("x", "Sam Rivera"))),
              "Sam created this sub-issue; Leo is assigned.", alternative="Issue.creatorId"),
        claim("A:Issue.title", "i-6", DROP("f_ptitle"), "Sam's sub-issue of Checkout analytics."),
    ]
    case = {"case_id": "LIN-10", "domain": "linear", "form": form, "mode": "single", "acting_user_id": ACTOR,
            "seed": s.seed(),
            "prompt": "Mark the sub-issue of \"Checkout revamp\" that's assigned to Sam Rivera as Done.",
            "references": [ref("LIN-10.r1", "Resolve the sub-issue", "A direct sub-issue of Checkout revamp assigned "
                               "to Sam Rivera.", "target", query, [], claims,
                               paths=[{"entities": ["issues", "issues"], "relationships": ["issues.parentId"]},
                                      {"entities": ["issues", "users"], "relationships": ["issues.assigneeId"]}],
                               identifying=["issues.parentId", "issues.title", "issues.assigneeId", "users.name"],
                               written=["issues.stateId"], effect={"table": "issues", "changes": ["update"]})],
            "probes": [gql("{ issues(first: 50) { nodes { " + ISSUE_FIELDS + " } } }")],
            "notes": "The epic itself is assigned to Sam (unclaimed trap: the parent instead of a sub-issue)."}
    return _form(case, form, ["i-9"])


def lin_11(form="present"):
    people = dict(PEOPLE, mayal="Maya Lopez", mayank="Mayank Rao")
    s = Seed(people)
    handles = {"maya": "maya" if form != "absent" else "mchen", "mayal": "mlopez", "mayank": "mayank"}
    for key, handle in handles.items():
        next(u for u in s.t["users"] if u["id"] == s.uid(key))["displayName"] = handle
    s.team("t-eng", "Engineering", "ENG")
    for i in range(1, 5):
        s.issue(f"i-f{i}", "t-eng", f"Engineering chore {i}", state="Done")
    s.issue("i-5", "t-eng", "Document the rate limiter", creator="dana")
    query = q("users", [f("f_handle", "displayName", "eq", "maya", "A:User.displayName")])
    by_name = q("users", [f("f_name", "name", "contains_ci", "maya")])
    claims = [
        claim("A:User.displayName", "u-mayal", REPLACE(by_name, "handle replaced by a name match"),
              "Maya Lopez's handle is mlopez.", alternative="User.name"),
    ]  # u-mayank (handle "mayank") is an unclaimed prefix trap
    case = {"case_id": "LIN-11", "domain": "linear", "form": form, "mode": "single", "acting_user_id": ACTOR,
            "seed": s.seed(), "prompt": "Assign ENG-5 to @maya.",
            "references": [ref("LIN-11.r1", "Resolve the assignee", "The user whose handle (displayName) is maya.",
                               "target", query, [], claims,
                               paths=[{"entities": ["users"], "relationships": []}],
                               identifying=["users.displayName"], written=["issues.assigneeId"],
                               effect={"table": "issues", "changes": ["update"], "field": "assigneeId", "all": True})],
            "probes": [gql("{ users { nodes { id name displayName email } } }")]}
    return _form(case, form, ["u-maya"])


def lin_12(form="present"):
    s = Seed()
    s.team("t-web", "Web", "WEB")
    for i in range(1, 12):
        s.issue(f"i-f{i}", "t-web", f"Web chore {i}", state="Done")
    s.issue("i-12", "t-web", "Stabilize the CI pipeline", assignee="leo", creator="dana")
    s.issue("i-13", "t-web", "Speed up integration tests", assignee="leo", creator="dana")
    s.comment("c-1", "i-12", "omar", "Tests are flaky on CI again - three reruns today.")
    s.comment("c-2", "i-12", "priya", "Agreed, the flaky tests are blocking merges.", parent="c-1")
    s.comment("c-3", "i-12", "priya", "Can we add the deploy checklist to the runbook?")
    s.comment("c-4", "i-13", "priya", "The flaky tests are mostly in the payments suite.")
    if form != "absent":
        s.comment("c-5", "i-12", "priya", "Flaky tests: I quarantined the worst offenders.")
    query = q("comments", [f("f_body", "body", "contains_ci", "flaky", "A:Comment.body"),
                           f("f_root", "parentId", "is_null", None, "H:Comment.parentId")], [
        e("e_author", "userId", "id", user_named("f_author", "Priya Nair"), "R:Comment.userId"),
        e("e_issue", "issueId", "id", n("issues", [f("f_ident", "identifier", "eq", "WEB-12")]), "R:Comment.issueId")])
    claims = [
        claim("H:Comment.parentId", "c-2", DROP("f_root"), "Priya replied in Omar's flaky-test thread; she did not start it.",
              alternative="reply in the thread"),
        claim("A:Comment.body", "c-3", DROP("f_body"), "Priya's WEB-12 thread is about the deploy checklist."),
        claim("R:Comment.issueId", "c-4", DROP("e_issue"), "Priya's flaky-test thread is on WEB-13."),
    ]
    case = {"case_id": "LIN-12", "domain": "linear", "form": form, "mode": "single", "acting_user_id": ACTOR,
            "seed": s.seed(),
            "prompt": "Resolve the comment thread Priya Nair started on WEB-12 about the flaky tests.",
            "references": [ref("LIN-12.r1", "Resolve the thread", "A top-level comment by Priya Nair on WEB-12 about "
                               "flaky tests.", "target", query, [], claims,
                               paths=[{"entities": ["comments", "users"], "relationships": ["comments.userId"]},
                                      {"entities": ["comments", "comments"], "relationships": ["comments.parentId"]}],
                               identifying=["comments.body", "comments.parentId", "comments.userId", "comments.issueId"],
                               written=["comments.resolvedAt"], effect={"table": "comments", "changes": ["update", "delete"]})],
            "probes": [gql("{ comments { nodes { id body user { name } parent { id } issue { identifier } } } }")]}
    return _form(case, form, ["c-5"])


def lin_14(form="present"):
    s = Seed()
    s.team("t-plt", "Platform", "PLT")
    s.team("t-inf", "Infra", "INF", parent="t-plt")
    s.team("t-web", "Web", "WEB")
    s.issue("i-p1", "t-plt", "Certificate expiry alerts for the edge proxy", assignee="leo", creator="dana")
    s.issue("i-w1", "t-web", "Certificate expiry banner for customers", assignee="omar", creator="dana")
    s.issue("i-i1", "t-inf", "Rotate the database credentials", assignee="sam", creator="dana")
    if form != "absent":
        s.issue("i-i2", "t-inf", "Certificate expiry check for internal services", assignee="sam", creator="dana")
    query = q("issues", [f("f_title", "title", "contains_ci", "certificate expiry")], [
        e("e_team", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Infra")]), "R:Issue.teamId")])
    parent_team = q("issues", [f("f_title", "title", "contains_ci", "certificate expiry")], [
        e("e_team", "teamId", "id", n("teams", [], [
            e("e_sub", "id", "parentId", n("teams", [f("f_team", "name", "eq", "Infra")]))]))])
    claims = [
        claim("H:Team.parentId", "i-p1", REPLACE(parent_team, "team replaced by its parent team"),
              "The certificate issue belongs to Platform, Infra's parent team.", alternative="parent team"),
        claim("A:Team.name", "i-w1", DROP("f_team"), "The Web team's certificate issue."),
    ]
    case = {"case_id": "LIN-14", "domain": "linear", "form": form, "mode": "single", "acting_user_id": ACTOR,
            "seed": s.seed(),
            "prompt": "Set the priority to Urgent on the Infra team's issue about certificate expiry.",
            "references": [ref("LIN-14.r1", "Resolve the issue", "The Infra team's issue about certificate expiry.",
                               "target", query, [], claims,
                               paths=[{"entities": ["issues", "teams"], "relationships": ["issues.teamId"]}],
                               identifying=["issues.title", "issues.teamId", "teams.name"], written=["issues.priority"],
                               effect={"table": "issues", "changes": ["update"]})],
            "probes": [gql("{ teams { nodes { name key parent { name } } } }")]}
    return _form(case, form, ["i-i2"])


ROUND3 = [lin_10, partial(lin_10, form="absent"), lin_11, partial(lin_11, form="absent"),
          lin_12, partial(lin_12, form="absent"), lin_14, partial(lin_14, form="absent")]
CASES = CASES + ROUND3


def lin_15(form="present"):
    s = Seed(dict(PEOPLE, mia="Mia Wong", zoe="Zoe Park"))
    s.team("t-des", "Design", "DES")
    s.team("t-dsy", "Design Systems", "DSY", parent="t-des")
    s.team("t-web", "Web", "WEB")
    s.member("t-des", "mia")
    s.member("t-des", "maya")
    s.member("t-dsy", "zoe")
    s.member("t-web", "leo")
    s.member("t-web", "sam")
    if form != "absent":
        s.issue("i-w1", "t-web", "Update the pricing page illustrations", assignee="mia", creator="sam")   # target
    s.issue("i-d1", "t-des", "Refresh the icon set", assignee="leo", creator="maya")          # in Design, non-member
    s.issue("i-w2", "t-web", "Fix the navigation spacing", assignee="zoe", creator="sam")     # sub-team member
    s.issue("i-w3", "t-web", "Clean up the footer links", assignee="sam", creator="maya")     # created by a member
    s.issue("i-w4", "t-web", "Archive old landing pages", state="Done", assignee="maya", creator="sam")  # done
    members = n("team_memberships", [], [e("e_mt", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Design")]))])
    open_state = e("e_open", "stateId", "id", n("workflow_states", [f("f_open", "type", "not_in", ["completed", "canceled"])]))
    query = q("issues", [], [
        e("e_asg", "assigneeId", "id", n("users", [], [e("e_mem", "id", "userId", members, "R:TeamMembership")]),
          "R:Issue.assigneeId"), open_state])
    in_team = q("issues", [], [e("e_team", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Design")])), open_state])
    sub_members = q("issues", [], [
        e("e_asg", "assigneeId", "id", n("users", [], [e("e_mem", "id", "userId", n("team_memberships", [], [
            e("e_mt", "teamId", "id", n("teams", [], [
                e("e_up", "parentId", "id", n("teams", [f("f_team", "name", "eq", "Design")]), closure="star")]))]))])),
        open_state])
    claims = [
        claim("R:TeamMembership", "i-d1", REPLACE(in_team, "assignee's team membership replaced by the issue's team"),
              "Refresh the icon set is a Design-team issue, but Leo is not a Design member.", alternative="Issue.teamId"),
        claim("H:Team.parentId", "i-w2", REPLACE(sub_members, "member of Design replaced by member of a Design sub-team"),
              "Zoe belongs to Design Systems, not Design.", alternative="sub-team member"),
        claim("R:Issue.assigneeId", "i-w3", SUB("e_asg", e("e_asg", "creatorId", "id", n("users", [], [
            e("e_mem", "id", "userId", members)]))), "Maya (a Design member) created it; Sam is assigned.",
              alternative="Issue.creatorId"),
        claim("A:WorkflowState.type", "i-w4", DROP("e_open"), "Assigned to Maya but already Done."),
    ]
    case = {"case_id": "LIN-15", "domain": "linear", "form": form, "mode": "single", "acting_user_id": ACTOR,
            "seed": s.seed(),
            "prompt": "Set the priority to High on the open issue that's assigned to a member of the Design team.",
            "references": [ref("LIN-15.r1", "Resolve the issue", "The open issue whose assignee is a member of the "
                               "Design team; only i-w1.", "target", query, [], claims,
                               paths=[{"entities": ["issues", "users", "team_memberships", "teams"],
                                       "relationships": ["issues.assigneeId", "team_memberships.userId", "team_memberships.teamId"]}],
                               identifying=["issues.assigneeId", "team_memberships.userId", "team_memberships.teamId",
                                            "teams.name", "workflow_states.type"], written=["issues.priority"],
                               effect={"table": "issues", "changes": ["update"]})],
            "probes": [gql("{ teamMemberships { nodes { user { name } team { name } } } }")]}
    return _form(case, form, ["i-w1"])


CASES += [lin_15, partial(lin_15, form="absent")]


def lin_16(form="present"):
    """W08 pattern: Maya appears directly on the near-miss (assignee); the request's Maya is the project lead."""
    s = Seed()
    s.team("t-web", "Web", "WEB")
    bug = s.label("lab-bug", "Bug")
    s.project("p-mc", "Checkout Redesign", lead="maya", creator="dana")
    s.project("p-sr", "Search Revamp", lead="sam", creator="maya")
    if form != "absent":
        s.issue("i-1", "t-web", "Coupon code rejected at checkout", assignee="leo", project="p-mc", labels=[bug])   # target
    s.issue("i-2", "t-web", "Search results flicker on scroll", assignee="maya", project="p-sr", labels=[bug])     # Maya assignee
    s.issue("i-3", "t-web", "Autocomplete misses recent queries", assignee="leo", project="p-sr", labels=[bug])    # Maya created project
    s.issue("i-4", "t-web", "Checkout button copy update", assignee="leo", project="p-mc")                        # no Bug label
    query = q("issues", [], [
        e("e_proj", "projectId", "id", n("projects", [], [
            e("e_lead", "leadId", "id", user_named("f_lead", "Maya Chen"), "R:Project.leadId")]), "R:Issue.projectId"),
        e("e_label", "id", "issue_id", n("issue_label_issue_association", [], [
            e("e_ln", "issue_label_id", "id", n("issue_labels", [f("f_lname", "name", "eq", "Bug")]))]),
          "R:issue_label_issue_association")])
    as_assignee = q("issues", [], [e("e_proj", "assigneeId", "id", user_named("x", "Maya Chen")),
                                   e("e_label", "id", "issue_id", n("issue_label_issue_association", [], [
                                       e("e_ln", "issue_label_id", "id", n("issue_labels", [f("f_lname", "name", "eq", "Bug")]))]))])
    creator_alt = e("e_lead", "creatorId", "id", user_named("x", "Maya Chen"))
    claims = [
        claim("R:Issue.projectId", "i-2", REPLACE(as_assignee, "project lead Maya replaced by assignee Maya"),
              "Maya is the assignee; the project is Sam's.", alternative="Issue.assigneeId"),
        claim("R:Project.leadId", "i-3", SUB("e_lead", creator_alt), "Maya created Search Revamp; Sam leads it.",
              alternative="Project.creatorId"),
        claim("R:issue_label_issue_association", "i-4", DROP("e_label"), "In Maya's project, but not a bug."),
    ]
    case = {"case_id": "LIN-16", "domain": "linear", "form": form, "variant_of": "arrangement:W08",  "mode": "single", "acting_user_id": ACTOR,
            "seed": s.seed(),
            "prompt": "Set the priority to Urgent on the bug in the project Maya Chen leads.",
            "references": [ref("LIN-16.r1", "Resolve the bug", "The Bug-labelled issue in a project whose lead is Maya "
                               "Chen; only i-1.", "target", query, [], claims,
                               paths=[{"entities": ["issues", "projects", "users"], "relationships": ["issues.projectId", "projects.leadId"]}],
                               identifying=["issues.projectId", "projects.leadId", "users.name", "issue_labels.name"],
                               written=["issues.priority"], effect={"table": "issues", "changes": ["update"]})],
            "probes": [gql("{ issues(first: 50) { nodes { " + ISSUE_FIELDS + " } } }")]}
    return _form(case, form, ["i-1"])


CASES += [lin_16]


def lin_17(form="present"):
    """Hierarchy direction: 'the parent of WEB-12' vs its sub-issue."""
    s = Seed()
    s.team("t-web", "Web", "WEB")
    for i in range(1, 10):
        s.issue(f"i-f{i}", "t-web", f"Web chore {i}", state="Done")
    if form != "absent":
        s.issue(("i-10", 10), "t-web", "Payments reliability", assignee="dana")                       # target: parent
    s.issue(("i-11", 11), "t-web", "Retry failed card charges", assignee="leo")
    s.issue(("i-12", 12), "t-web", "Idempotent payment requests", assignee="sam",
            parent="i-10" if form != "absent" else None)
    s.issue(("i-13", 13), "t-web", "Idempotency keys for refunds", assignee="leo", parent="i-12")      # child of WEB-12
    if form != "absent":
        next(i for i in s.t["issues"] if i["id"] == "i-11")["parentId"] = "i-10"
    query = q("issues", [], [e("e_child", "id", "parentId", n("issues", [f("f_ident", "identifier", "eq", "WEB-12")]),
                               "H:Issue.parentId")])
    reversed_q = q("issues", [], [e("e_child", "parentId", "id", n("issues", [f("f_ident", "identifier", "eq", "WEB-12")]))])
    claims = [claim("H:Issue.parentId", "i-13", REPLACE(reversed_q, "parent replaced by child"),
                    "WEB-13 is WEB-12's sub-issue, not its parent.", alternative="sub-issue (reversed direction)")]
    case = {"case_id": "LIN-17", "domain": "linear", "form": form, "mode": "single", "acting_user_id": ACTOR,
            "variant_of": "arrangement:direction", "seed": s.seed(),
            "prompt": "Mark the parent issue of WEB-12 as Done.",
            "references": [ref("LIN-17.r1", "Resolve the parent issue", "The issue that WEB-12 is a sub-issue of.",
                               "target", query, [], claims,
                               paths=[{"entities": ["issues", "issues"], "relationships": ["issues.parentId"]}],
                               identifying=["issues.parentId", "issues.identifier"], written=["issues.stateId"],
                               effect={"table": "issues", "changes": ["update"]})],
            "probes": [gql('{ issue(id: "i-12") { identifier parent { identifier } children { nodes { identifier } } } }')]}
    return _form(case, form, ["i-10"])


CASES += [lin_17, partial(lin_17, form="absent")]
