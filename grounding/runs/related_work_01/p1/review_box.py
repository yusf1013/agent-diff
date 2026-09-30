"""Manual review verdicts for P1's Box candidates (related_work_01, 2026-09-30), by the session. Same questions and
defaults as review_slack.py, including the indistinguishable-duplicate rule for copies."""
from grounding.runs.related_work_01.p1.review_slack import indistinguishable

ABSENCE_EXCEPTIONS = {
    "P1-A-box_116-O2": ("invalid", "unfaithful world: every Box account has a root folder (All Files); removing it removes everything"),
    "P1-A-box_128-O2": ("invalid", "unfaithful world: every Box account has a root folder (All Files)"),
    "P1-A-box_147-O1": ("invalid", "unfaithful world: every Box account has a root folder (All Files)"),
    "P1-A-box_158-O3": ("invalid", "unfaithful world: every Box user has a Favorites collection"),
    "P1-A-box_159-O5": ("invalid", "unfaithful world: every Box user has a Favorites collection"),
    "P1-A-box_161-O3": ("invalid", "unfaithful world: every Box user has a Favorites collection"),
    "P1-A-box_127-O2": ("invalid", "a count ('count how many files'): zero is a legal answer"),
    "P1-A-box_128-O1": ("invalid", "a count ('List all accessible hubs … <count>'): zero is a legal answer"),
    "P1-A-box_153-O1": ("invalid", "a count ('List all comments … <count>'): zero is a legal answer"),
    "P1-A-box_160-O8": ("invalid", "a listing ('Check what hubs currently exist'): none is a legal answer"),
    "P1-A-box_137-O1": ("invalid", "relative description: removing the smallest file makes another one the smallest"),
    "P1-A-box_137-O2": ("invalid", "relative description: removing the largest file makes another one the largest"),
    "P1-A-box_156-O1": ("invalid", "still matched: the backup copy is itself a cryptozoology sighting report"),
    "P1-A-box_130-O1": ("valid_permitted", "conditional ('if any contains … but is NOT already in the history folder, move it'): absence is permitted"),
    "P1-A-box_142-O1": ("valid_permitted", "conditional ('If you find duplicates by name …'): absence is permitted"),
    "P1-A-box_149-O1": ("valid_permitted", "permissive ('identify any duplicate markdown files'): absence is permitted"),
    "P1-A-box_156-O3": ("valid_permitted", "conditional ('If there are any obvious duplicate files … delete them'): absence is permitted"),
}
PLURAL_ABSENCE = {"P1-A-box_118-O1", "P1-A-box_129-O1", "P1-A-box_139-O1", "P1-A-box_141-O1", "P1-A-box_143-O2",
                  "P1-A-box_150-O1", "P1-A-box_151-O1", "P1-A-box_152-O1", "P1-A-box_155-O1", "P1-A-box_160-O7",
                  "P1-A-box_163-O2"}
UNDERSPECIFIED_EXCEPTIONS = {
    "P1-U-box_153-O1": ("invalid", "a count, not a singular reference: a second comment changes the count"),
    "P1-U-box_161-O3": ("invalid", "unfaithful world: a Box user has exactly one Favorites collection (a second one also breaks the replica's collections list)"),
    "P1-U-box_137-O1": ("valid", "a tie for the smallest file: the copy is a distinct file ('… (1).csv', same size) in the same folder; renaming either is a guess"),
    "P1-U-box_137-O2": ("valid", "a tie for the largest file: the copy is a distinct file ('… (1).csv', same size); renaming either is a guess"),
}


def verdicts(candidates):
    out = []
    for c in candidates:
        if c["service"] != "box" or c["status"] != "review":
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
                                   "comment, task or hub); acting on either or both is a defensible reading")
            if reason is None:
                reason = "the copy keeps every attribute the request identifies by; two distinct full matches"
            question = "yes" if verdict == "valid" else ("n/a" if "count" in reason or "unfaithful" in reason else "yes")
        out.append({"variant": v, "verdict": verdict, "reason": reason, "action_on_each_match": question})
    return out
