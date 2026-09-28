"""The Linear seed conventions the generator builds on: the organization, default people, workflow states and
row templates from the benchmark's own seed.

Copied verbatim from grounding/runs/fact_coverage_01/pilot/cases_linear.py (lines 12-161) on 2026-09-27, so that
the kit no longer imports a study's hand-made cases (roadmap step 3). Behaviour is unchanged; the pilot keeps its
own copy.
"""
from __future__ import annotations

import copy
import json

from grounding.paths import REPO_ROOT

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
