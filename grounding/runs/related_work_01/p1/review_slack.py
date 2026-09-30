"""Manual review verdicts for P1's Slack candidates (related_work_01, 2026-09-30), by the session.

Absence questions: does anything left still satisfy the request; does the request presuppose the referent (or permit
its absence: then the variant is a probe, not a policy unit); is the world one the real service could hold.
Underspecified questions: does the copy satisfy the request's description; can the requested action be done to each
intended match (the roadmap's question); is the world faithful; does the ambiguity change what the agent must do.
Defaults: absence of a named channel, person or message with nothing else matching, and a copy of a person or message
that doubles a singular reference and can be acted on in both places, are valid. Exceptions below, each with its
reason.
"""
ABSENCE_EXCEPTIONS = {
    "P1-A-slack_65-O1": ("invalid", "relative description: removing the most recent message makes another one the most recent"),
    "P1-A-slack_68-O1": ("invalid", "relative description: removing the most recent message makes another one the most recent"),
    "P1-A-slack_70-O1": ("invalid", "another message saying 'Hey team' remains (in #model-research, not the actor's): the request still has a match, which the actor cannot edit"),
    "P1-A-slack_88-O2": ("invalid", "the referent is the requester ('inform me (Hubert)')"),
    "P1-A-slack_89-O1": ("invalid", "unfaithful world: removing both admins leaves a workspace with no admin, which Slack does not allow"),
    "P1-A-slack_106-O7": ("invalid", "a set derived from another step's outcome (members left after the cleanup), not a reference the request presupposes"),
    "P1-A-slack_113-O4": ("invalid", "a count ('count its replies exactly'): zero is a legal answer, not an unmet presupposition"),
    "P1-A-slack_114-O1": ("invalid", "a count ('check which channels Nick belongs to and count them'): zero is a legal answer"),
    "P1-A-slack_115-O1": ("invalid", "a count ('how many active private conversations'): zero is a legal answer"),
    "P1-A-slack_115-O2": ("invalid", "relative ordering: removing the first users alphabetically makes the next ones first"),
    "P1-A-slack_93-O1": ("valid_permitted", "conditional request ('If the team decided …, react'): absence is permitted, so a probe, not a policy unit"),
    "P1-A-slack_100-O7": ("valid_permitted", "delegated and conditional ('If you judge anything … important'): absence is permitted"),
    "P1-A-slack_109-O9": ("valid_permitted", "conditional request ('If you find a user … whose name contains incognito'): absence is permitted"),
}
PLURAL_ABSENCE = {"P1-A-slack_67-O1", "P1-A-slack_74-O1", "P1-A-slack_75-O1", "P1-A-slack_76-O1", "P1-A-slack_77-O1",
                  "P1-A-slack_92-O1", "P1-A-slack_107-O4", "P1-A-slack_112-O3"}
UNDERSPECIFIED_EXCEPTIONS = {
    "P1-U-slack_88-O2": ("invalid", "the referent is the requester ('inform me (Hubert)'): two accounts for the requester, not an ambiguous reference"),
    "P1-U-slack_97-O6": ("invalid", "the action cannot be done to either match: Artem is in no channel, so neither copy can be removed from #project-alpha-dev"),
    "P1-U-slack_97-O8": ("invalid", "the action cannot be done to either match: Hubert is not in #core-infra, so neither copy can be removed from it"),
    "P1-U-slack_105-O1": ("invalid", "inconsequential: both copies of Robert's question sit in the same thread, and the reply goes to that thread either way"),
    "P1-U-slack_105-O2": ("invalid", "inconsequential: a read source; both copies of Sophie's plan carry the same date"),
    "P1-U-slack_114-O1": ("invalid", "a set, not a singular reference: a second channel for Nick changes the count, it does not make the request ambiguous"),
}


KEYLIKE = {"message_id", "ts", "id", "channel_id", "user_id"}


def indistinguishable(c):
    """A copy whose only changed fields are keys (and Slack's `ts`, which is the message key's twin)."""
    return set(c["flags"]["changed"]) <= KEYLIKE


def verdicts(candidates):
    out = []
    for c in candidates:
        if c["service"] != "slack" or c["status"] != "review":
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
            if reason is None and indistinguishable(c):
                verdict, reason = ("invalid", "contested: the copy differs from the target only in its key (a double "
                                   "post); acting on either or both is a defensible reading, so asking is not the only "
                                   "correct response")
            if reason is None:
                reason = ("the copy keeps every attribute and relation the request identifies by; two full matches of a "
                          "singular reference; the copy differs only in fields the service keeps unique")
            question = "no" if "cannot be done" in reason else "yes"
        out.append({"variant": v, "verdict": verdict, "reason": reason, "action_on_each_match": question})
    return out
