"""Manual review verdicts for P1's Linear candidates (related_work_01, 2026-09-30), by the session. Same questions and
defaults as review_slack.py, including the indistinguishable-duplicate rule for copies."""
from grounding.runs.related_work_01.p1.review_slack import indistinguishable

ABSENCE_EXCEPTIONS = {
    "P1-A-linear_35-O2": ("invalid", "relative description: removing the least-loaded members makes others the least loaded"),
    "P1-A-linear_55-O1": ("invalid", "a count ('Count how many comments contain this word'): zero is a legal answer"),
    "P1-A-linear_15-O1": ("invalid", "still matched by a natural reading: ENG-6 ('Add email sign-in and SSO support') is also a login issue John commented on"),
    "P1-A-linear_37-O1": ("valid_permitted", "permissive ('Find any Engineering tickets in In Progress …'): absence is permitted"),
}
PLURAL_ABSENCE = {"P1-A-linear_32-O1", "P1-A-linear_36-O2", "P1-A-linear_41-O1"}
UNDERSPECIFIED_EXCEPTIONS = {
    "P1-U-linear_29-O1": ("invalid", "contested: with three copies of the trace issue, marking every newer copy as a duplicate is a defensible reading"),
    "P1-U-linear_37-O1": ("invalid", "a plural request ('any Engineering tickets …'): the copy joins the set, it does not make the request ambiguous"),
    "P1-U-linear_41-O2": ("invalid", "a count feeding a rate: the copy changes the count, not which record is meant"),
    "P1-U-linear_30-O1": ("invalid", "the request gives Artem's id; the copy's new id disambiguates"),
}
TEAM_COPY = "valid_unverified"


def verdicts(candidates):
    out = []
    for c in candidates:
        if c["service"] != "linear" or c["status"] != "review":
            continue
        v = c["variant"]
        if c["mode"] == "absence":
            verdict, reason = ABSENCE_EXCEPTIONS.get(v, ("valid", None))
            if reason is None:
                kind = "plural (none of the set exists)" if v in PLURAL_ABSENCE else "named referent"
                reason = f"{kind}: the request presupposes it; nothing left matches; a report of absence is the correct response"
            question = "n/a (no intended match)"
        else:
            verdict, reason = UNDERSPECIFIED_EXCEPTIONS.get(v, ("valid", None))
            if v not in UNDERSPECIFIED_EXCEPTIONS and indistinguishable(c):
                verdict, reason = ("invalid", "contested: the copy differs from the target only in its key (a duplicate "
                                   "state, label, comment or relation); acting on either or both is a defensible reading")
            elif v not in UNDERSPECIFIED_EXCEPTIONS and c["referent_table"] == "teams":
                verdict, reason = (TEAM_COPY, "a second team with the same name and a new key; whether Linear allows two "
                                   "teams with one name is not documented (the replica allows it)")
            if reason is None:
                reason = ("the copy keeps every attribute the request identifies by (a namesake with a new email, or an "
                          "issue with a new identifier); two distinct full matches")
            question = "yes" if verdict in ("valid", TEAM_COPY) or "contested" in reason else "n/a"
        out.append({"variant": v, "verdict": verdict, "reason": reason, "action_on_each_match": question})
    return out
