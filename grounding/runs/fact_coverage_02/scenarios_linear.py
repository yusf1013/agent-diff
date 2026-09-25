"""New Linear scenarios for facts the pilot never tested (manual design). Each has its target; probes are derived.

Every claim carries its substitute family (method.md). Seeds reuse the pilot's Linear Seed and people.
"""
from __future__ import annotations

from grounding.runs.fact_coverage_01.pilot.cases_linear import ACTOR, Seed, gql, user_named
from grounding.runs.fact_coverage_01.pilot.common import DROP, REPLACE, SUB, claim, e, f, n, q, ref
from grounding.runs.fact_coverage_02.scenarios_box import fam


def case(cid, s, prompt, refs, probes, mode="single"):
    return {"case_id": cid, "domain": "linear", "form": "present", "mode": mode, "acting_user_id": ACTOR,
            "seed": s.seed(), "prompt": prompt, "references": refs, "probes": probes}


# ---------------------------------------------------------------------------
def lin_21():
    """Issue creator, creation day and team (a similarly named team is the team's substitute)."""
    s = Seed()
    s.team("t-web", "Web", "WEB")
    s.team("t-webp", "Web Platform", "WBP")
    s.team("t-mob", "Mobile", "MOB")
    day = "2026-09-{}T12:00:00"  # the same calendar day from UTC-11 to UTC+11
    s.issue("i-21", "t-web", "Login redirect loops after SSO", creator="omar", created=day.format(10))       # target
    s.issue("i-22", "t-web", "Login redirect drops the return URL", creator="dana", assignee="omar",
            created=day.format(10))                                                                          # assigned
    s.issue("i-23", "t-web", "Login redirect ignores locale", creator="omar", created=day.format(11))        # next day
    s.issue("i-24", "t-webp", "Login redirect fails behind the proxy", creator="omar", created=day.format(10))  # Web Platform
    s.issue("i-25", "t-mob", "Login redirect opens the browser", creator="omar", created=day.format(10))    # Mobile
    query = q("issues", [f("f_title", "title", "contains_ci", "login redirect", "A:Issue.title"),
                         f("f_created", "createdAt", "contains_ci", "2026-09-10", "A:Issue.createdAt")], [
        e("e_creator", "creatorId", "id", user_named("f_creator", "Omar Haddad"), "R:Issue.creatorId"),
        e("e_team", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Web", "A:Team.name")]), "R:Issue.teamId")])
    near_team = e("e_team", "teamId", "id", n("teams", [f("x", "name", "contains_ci", "web")]))
    claims = [
        fam(claim("R:Issue.creatorId", "i-22", SUB("e_creator", e("e_creator", "assigneeId", "id", user_named("x", "Omar Haddad"))),
                  "Omar is the assignee; Dana created it.", alternative="Issue.assigneeId"), "F1"),
        fam(claim("A:Issue.createdAt", "i-23", DROP("f_created"), "Created on September 11, the next day.",
                  alternative="adjacent day"), "F7"),
        fam(claim("R:Issue.teamId", "i-24", SUB("e_team", near_team), "In the Web Platform team, not Web.",
                  alternative="similarly named team"), "F8"),
        fam(claim("R:Issue.teamId", "i-25", DROP("e_team"), "In the Mobile team."), "F0"),
    ]
    return case("LIN-21", s, "Assign to Priya Nair the Web team issue about the login redirect that Omar Haddad created "
                             "on September 10.",
                [ref("LIN-21.r1", "Resolve the issue", "The Web team's login-redirect issue created by Omar Haddad on "
                     "2026-09-10; only i-21.", "target", query, ["i-21"], claims,
                     paths=[{"entities": ["issues", "users"], "relationships": ["issues.creatorId"]},
                            {"entities": ["issues", "teams"], "relationships": ["issues.teamId"]}],
                     identifying=["issues.title", "issues.createdAt", "issues.creatorId", "teams.name"],
                     written=["issues.assigneeId"], effect={"table": "issues", "changes": ["update"], "columns": ["assigneeId"]})],
                [gql("{ issues { nodes { identifier title createdAt creator { name } assignee { name } team { name parent { name } } } } }")])


# ---------------------------------------------------------------------------
def lin_22():
    """Document last editor and document project."""
    s = Seed()
    s.team("t-web", "Web", "WEB")
    s.project("p-co", "Checkout Redesign", lead="maya")
    s.project("p-co2", "Checkout Redesign v2", lead="maya")
    s.project("p-pay", "Payments Revamp", lead="sam")
    s.initiative("in-com", "Commerce", owner="maya")
    s.t["initiative_to_projects"].append({"id": "itp-1", "initiativeId": "in-com", "projectId": "p-co",
                                          "sortOrder": 0.0, "createdAt": "2026-06-01T09:00:00", "updatedAt": "2026-06-01T09:00:00"})
    s.document("d-21", "Checkout test notes", "maya", "leo", project="p-co", content="Cases for the new flow.")   # target
    s.document("d-22", "Checkout rollout", "leo", "sam", project="p-co", content="Rollout steps.")              # Leo created it
    s.document("d-23", "Commerce QA overview", "maya", "leo", initiative="in-com", content="QA across commerce.")  # initiative
    s.document("d-24", "Checkout v2 test notes", "maya", "leo", project="p-co2", content="Cases for v2.")        # v2 project
    s.document("d-25", "Payments test notes", "maya", "leo", project="p-pay", content="Cases for payments.")     # other project
    query = q("documents", [], [
        e("e_upd", "updatedById", "id", user_named("f_upd", "Leo Park"), "R:Document.updatedById"),
        e("e_proj", "projectId", "id", n("projects", [f("f_proj", "name", "eq", "Checkout Redesign", "A:Project.name")]),
          "R:Document.projectId")])
    near_project = e("e_proj", "projectId", "id", n("projects", [f("x", "name", "contains_ci", "checkout redesign")]))
    via_initiative = e("e_proj", "initiativeId", "id", n("initiatives", [], [
        e("e_ip", "id", "initiativeId", n("initiative_to_projects", [], [
            e("e_pp", "projectId", "id", n("projects", [f("x", "name", "eq", "Checkout Redesign")]))]))]))
    claims = [
        fam(claim("R:Document.updatedById", "d-22", SUB("e_upd", e("e_upd", "creatorId", "id", user_named("x", "Leo Park"))),
                  "Leo created Checkout rollout; Sam edited it last.", alternative="Document.creatorId"), "F1"),
        fam(claim("R:Document.projectId", "d-23", SUB("e_proj", via_initiative),
                  "Attached to the Commerce initiative, which contains the project; not to the project.",
                  alternative="document of the initiative containing the project"), "F2"),
        fam(claim("R:Document.projectId", "d-24", SUB("e_proj", near_project), "In Checkout Redesign v2.",
                  alternative="similarly named project"), "F8"),
        fam(claim("R:Document.projectId", "d-25", DROP("f_proj"), "In Payments Revamp."), "F0"),
    ]
    return case("LIN-22", s, "Rename the doc Leo Park last edited in the Checkout Redesign project to \"Checkout QA plan\".",
                [ref("LIN-22.r1", "Resolve the document", "The document of the Checkout Redesign project last edited by "
                     "Leo Park; only d-21.", "target", query, ["d-21"], claims,
                     paths=[{"entities": ["documents", "users"], "relationships": ["documents.updatedById"]},
                            {"entities": ["documents", "projects"], "relationships": ["documents.projectId"]}],
                     identifying=["documents.updatedById", "users.name", "documents.projectId", "projects.name"],
                     written=["documents.title"], effect={"table": "documents", "changes": ["update"]})],
                [gql("{ documents { nodes { id title creator { name } updatedBy { name } project { name } initiative { name } } } }")])


# ---------------------------------------------------------------------------
def lin_23():
    """Who resolved a comment thread."""
    s = Seed()
    s.team("t-web", "Web", "WEB")
    s.issue(("i-w5", 5), "t-web", "Flaky checkout test")
    s.comment("c-21", "i-w5", "sam", "The retry wrapper hides the real failure.", resolver="maya")      # target
    s.comment("c-22", "i-w5", "maya", "Can we pin the browser version?", resolver="dana")             # Maya wrote it
    s.comment("c-25", "i-w5", "sam", "Timeouts are too short on CI.", resolver="dana")                 # Dana resolved it
    query = q("comments", [f("f_root", "parentId", "is_null")], [
        e("e_issue", "issueId", "id", n("issues", [f("f_iss", "identifier", "eq", "WEB-5", "A:Issue.identifier")]),
          "R:Comment.issueId"),
        e("e_res", "resolvingUserId", "id", user_named("f_res", "Maya Chen"), "R:Comment.resolvingUserId")])
    claims = [
        fam(claim("R:Comment.resolvingUserId", "c-22", SUB("e_res", e("e_res", "userId", "id", user_named("x", "Maya Chen"))),
                  "Maya started this thread; Dana resolved it.", alternative="Comment.userId"), "F1"),
        fam(claim("R:Comment.resolvingUserId", "c-25", DROP("e_res"), "Resolved by Dana."), "F0"),
    ]
    return case("LIN-23", s, "Reopen the comment thread on WEB-5 that Maya Chen resolved.",
                [ref("LIN-23.r1", "Resolve the thread", "The WEB-5 thread whose resolver is Maya Chen; only c-21.",
                     "target", query, ["c-21"], claims,
                     paths=[{"entities": ["comments", "users"], "relationships": ["comments.resolvingUserId"]}],
                     identifying=["comments.issueId", "comments.resolvingUserId", "users.name"],
                     written=["comments.resolvedAt"], effect={"table": "comments", "changes": ["update"]})],
                [gql('{ issue(id: "i-w5") { comments { nodes { id body user { name } resolvingUser { name } resolvedAt } } } }')])


# ---------------------------------------------------------------------------
def lin_24():
    """A cycle's number (the adjacent number is the substitute)."""
    s = Seed()
    s.team("t-eng", "Engineering", "ENG")
    s.cycle("cy-15", "t-eng", 15, "2026-09-21T00:00:00", "2026-10-05T00:00:00", active=True)       # target
    s.cycle("cy-16", "t-eng", 16, "2026-10-05T00:00:00", "2026-10-19T00:00:00", nxt=True)
    s.issue(("i-e9", 9), "t-eng", "Rotate the signing keys")
    query = q("cycles", [f("f_num", "number", "eq", 15.0, "A:Cycle.number")], [
        e("e_team", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Engineering")]), "R:Cycle.teamId")])
    claims = [
        fam(claim("A:Cycle.number", "cy-16", DROP("f_num"), "Cycle 16, the next one.", alternative="adjacent number"), "F7"),
    ]
    issue_query = q("issues", [f("f_i", "identifier", "eq", "ENG-9")])
    return case("LIN-24", s, "Move ENG-9 into cycle 15 of the Engineering team.",
                [ref("LIN-24.r1", "Resolve the cycle", "The Engineering cycle numbered 15; only cy-15.", "target", query,
                     ["cy-15"], claims, paths=[{"entities": ["cycles", "teams"], "relationships": ["cycles.teamId"]}],
                     identifying=["cycles.number", "cycles.teamId"], written=["issues.cycleId"],
                     effect={"table": "issues", "changes": ["update"], "field": "cycleId"}),
                 ref("LIN-24.r2", "Resolve the issue", "ENG-9; only i-e9.", "input", issue_query, ["i-e9"], [],
                     paths=[{"entities": ["issues"], "relationships": []}], identifying=["issues.identifier"])],
                [gql("{ cycles { nodes { id number name startsAt endsAt team { name } } } }")])


# ---------------------------------------------------------------------------
def lin_25():
    """A label's group (a top-level label and a similarly named group are the substitutes)."""
    s = Seed()
    s.team("t-mob", "Mobile", "MOB")
    bug = s.label("lab-bug", "Bug", group=True)
    triage = s.label("lab-bt", "Bug triage", group=True)
    s.label("lab-reg", "Regression", parent=bug)                 # target
    s.label("lab-reg-top", "Regression")                          # top-level
    s.label("lab-reg-bt", "Regression", parent=triage)            # in Bug triage
    s.issue(("i-m3", 3), "t-mob", "Crash on resume from background")
    query = q("issue_labels", [f("f_name", "name", "eq", "Regression", "A:IssueLabel.name")], [
        e("e_parent", "parentId", "id", n("issue_labels", [f("f_group", "name", "eq", "Bug")]), "H:IssueLabel.parentId")])
    near_group = q("issue_labels", [f("f_name", "name", "eq", "Regression")], [
        e("e_parent", "parentId", "id", n("issue_labels", [f("f_group", "name", "contains_ci", "bug")]))])
    claims = [
        fam(claim("H:IssueLabel.parentId", "lab-reg-top", DROP("e_parent"), "A top-level Regression label, in no group.",
                  alternative="label outside the group"), "F4"),
        fam(claim("H:IssueLabel.parentId", "lab-reg-bt", REPLACE(near_group, "group name loosened"),
                  "The Regression label in the Bug triage group.", alternative="similarly named group"), "F8"),
    ]
    issue_query = q("issues", [f("f_i", "identifier", "eq", "MOB-3")])
    return case("LIN-25", s, "Add the Regression label from the Bug group to MOB-3.",
                [ref("LIN-25.r1", "Resolve the label", "The Regression label inside the Bug group; only lab-reg.", "target",
                     query, ["lab-reg"], claims,
                     paths=[{"entities": ["issue_labels"], "relationships": ["issue_labels.parentId"]}],
                     identifying=["issue_labels.name", "issue_labels.parentId"],
                     written=["issue_label_issue_association"],
                     effect={"table": "issue_label_issue_association", "changes": ["insert"],
                             "key": ["issue_id", "issue_label_id"], "field": "issue_label_id"}),
                 ref("LIN-25.r2", "Resolve the issue", "MOB-3; only i-m3.", "input", issue_query, ["i-m3"], [],
                     paths=[{"entities": ["issues"], "relationships": []}], identifying=["issues.identifier"])],
                [gql("{ issueLabels { nodes { id name isGroup parent { name } } } }")])


# ---------------------------------------------------------------------------
def lin_26():
    """Issue subscribers (assignee and creator are the substitutes)."""
    s = Seed()
    s.team("t-web", "Web", "WEB")
    s.issue("i-61", "t-web", "Search results jump on scroll", creator="sam", subscribers=["dana"])          # target
    s.issue("i-62", "t-web", "Pagination skips a page", creator="sam", assignee="dana", subscribers=["leo"])  # assigned
    s.issue("i-63", "t-web", "Filters reset on back", creator="dana", subscribers=["leo"])                   # created
    s.issue("i-64", "t-web", "Sort order ignored", creator="sam", subscribers=["sam"])                       # other person
    query = q("issues", [], [
        e("e_team", "teamId", "id", n("teams", [f("f_team", "name", "eq", "Web")])),
        e("e_sub", "id", "issue_id", n("issue_subscriber_user_association", [], [
            e("e_su", "user_id", "id", user_named("f_sub", "Dana Whitfield"))]), "R:issue_subscriber_user_association")])
    claims = [
        fam(claim("R:issue_subscriber_user_association", "i-62",
                  SUB("e_sub", e("e_sub", "assigneeId", "id", user_named("x", "Dana Whitfield"))),
                  "Dana is the assignee, not a subscriber.", alternative="Issue.assigneeId"), "F1"),
        fam(claim("R:issue_subscriber_user_association", "i-63",
                  SUB("e_sub", e("e_sub", "creatorId", "id", user_named("x", "Dana Whitfield"))),
                  "Dana created it; she is not subscribed.", alternative="Issue.creatorId"), "F1"),
        fam(claim("R:issue_subscriber_user_association", "i-64", DROP("f_sub"), "Only Sam is subscribed."), "F0"),
    ]
    return case("LIN-26", s, "Set the priority to Low on the Web team issue that Dana Whitfield is subscribed to.",
                [ref("LIN-26.r1", "Resolve the issue", "The Web issue with Dana Whitfield among its subscribers; only i-61.",
                     "target", query, ["i-61"], claims,
                     paths=[{"entities": ["issues", "users"], "relationships": ["issue_subscriber_user_association"]}],
                     identifying=["issue_subscriber_user_association.user_id", "users.name"],
                     written=["issues.priority"], effect={"table": "issues", "changes": ["update"], "columns": ["priority"]})],
                [gql("{ issues { nodes { identifier title assignee { name } creator { name } subscribers { nodes { name } } } } }")])


SCENARIOS = [lin_21, lin_22, lin_23, lin_24, lin_25, lin_26]
