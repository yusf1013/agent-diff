"""The S1 probes: Agent-Diff's plural obligations that require every match, their kind of request and parameters.

The first run (commit 2b4f3306a2) chose these before any run, from each request's wording. The review after it made
the changes listed in CHANGED_AFTER_FIRST_RUN; every one follows a rule stated here, not a result.

Rules:
- A probe is an obligation the cards resolve to a set of targets that the request needs *every one* of. Pick-one
  requests and permissive source sets ("whatever you can dig up") are not probes: missing some is not a failure.
- Search words are the request's own words for the targets. Punctuation is not a word (real Slack search drops it).
  When the request names alternatives ("food" or "eat"; .pdf, .docx and .md), each is searched and the hits combined.
- Linear's "server filter, all conditions" carries every condition the request states. When the request names no
  team, the team routes use the first target's team (a guess, as the Box "anywhere" routes guess the first target's
  folder), and the complete route is the workspace listing (the seed has 44 issues, under one page of 1000).
"""

# (test, obligation, kind, parameters). `None` means the request gives no such parameter (the route is then marked
# not applicable). A list means alternatives, each run and combined.
PROBES = [
    ("slack_67", 1, "slack", {"channel": "random", "search": "lunch"}),
    ("slack_74", 1, "slack", {"channel": "random", "search": None}),  # "questions": no searchable word
    ("slack_75", 1, "slack", {"channel": "engineering", "search": "login"}),
    ("slack_76", 1, "slack-messages", {"search": "login"}),  # slack_77 O1 has the same targets and wording
    ("slack_106", 1, "slack-channels-any", {"search": None}),
    ("slack_108", 1, "slack-messages", {"search": ["food", "eat"]}),
    ("slack_110", 6, "slack-messages", {"search": "supercomputer"}),
    ("slack_112", 1, "slack-channels-any", {"search": None}),  # slack_113 O1 has the same targets
    ("box_127", 2, "box", {"folder": "investments", "words": None, "ext": None}),
    ("box_129", 1, "box-anywhere", {"words": "fomc", "ext": "pdf"}),
    ("box_139", 1, "box", {"folder": "readings", "words": "ethics", "ext": None}),
    ("box_141", 1, "box", {"folder": "agent-diff-research", "words": "results", "ext": "json"}),
    ("box_143", 2, "box", {"folder": "readings", "words": None, "ext": ["pdf", "docx", "md"]}),
    ("box_150", 1, "box", {"folder": "investments", "words": "fomc", "ext": "pdf"}),
    ("box_151", 1, "box", {"folder": "investments", "words": "pdf", "ext": "pdf"}),
    ("box_152", 1, "box", {"folder": "macroeconomics", "words": "fomc", "ext": "pdf"}),
    ("box_155", 1, "box", {"folder": "macroeconomics", "words": "csv", "ext": "csv"}),
    ("box_158", 1, "box-anywhere", {"words": "Moog", "ext": "txt"}),
    ("linear_32", 1, "linear", {"team": "Engineering", "team_named": False,
                                "filter": 'assignee: {name: {eq: "John Doe"}}, priority: {eq: 1}'}),
    ("linear_41", 1, "linear", {"team": "Seed Library",
                                "filter": 'team: {name: {eq: "Seed Library"}}, title: {contains: "Yuto"}'}),
    ("linear_41", 3, "linear", {"team": "Seed Library",
                                "filter": 'team: {name: {eq: "Seed Library"}}, title: {contains: "Szymon"}'}),
    ("linear_41", 5, "linear", {"team": "Seed Library",
                                "filter": 'team: {name: {eq: "Seed Library"}}, title: {contains: "Szymon"}, '
                                          'state: {name: {neq: "Sprouted"}}'}),
    ("linear_56", 2, "linear", {"team": "Racing Operations",
                                "filter": 'team: {name: {eq: "Racing Operations"}}, state: {name: {eq: "In Flight"}}'}),
]
# (test, obligation) -> the probe with the same targets, words and kind of request
SAME_AS = {("slack_77", 1): ("slack_76", 1), ("slack_113", 1): ("slack_112", 1), ("box_163", 2): ("box_129", 1)}

# Run in the first run, kept for the record, not counted: their cards call the set a permissive source.
PERMISSIVE = [
    ("slack_107", 4, "slack-messages", {"search": "GPU"}),
    ("slack_109", 6, "slack-channels-any", {"search": "latency"}),
]

# Plural obligations that are not a probe, because missing some targets is not a failure (or the card is wrong).
LEFT_OUT = {
    "box_118 O1": "pick one: a comment on 'the first file found' (its targets and words are box_129's, which is probed)",
    "slack_112 O3": "pick one: 'the single best message'",
    "linear_54 O5": "pick one: a comment on 'any issue in the Engineering team'",
    "slack_100 O7": "a delegated judgment ('if you judge anything important'): missing some is not a failure",
    "slack_108 O8": "a permissive source set for an opening post",
    "slack_92 O1": "the card counts the whole #random history as 'the Gemini discussion', so a search that finds the "
                   "Gemini messages would count as missing the rest",
}
OUT_OF_SCOPE = {"calendar": "no obligation cards yet (step 1 of the projection plan)"}

# The other plural obligations the cards resolve (60 in Slack, Box and Linear have two or more targets): kinds of
# request with no route table, so no shortcut to check.
NO_ROUTE_TABLE = {
    "a set of people (authors, members, admins, all users)": [
        "slack_87 O1", "slack_89 O1", "slack_94 O7", "slack_95 O3", "slack_95 O6", "slack_96 O1", "slack_96 O4",
        "slack_97 O1", "slack_97 O2", "slack_103 O3", "slack_104 O2", "slack_106 O4", "slack_106 O7", "slack_108 O2",
        "slack_113 O2", "slack_115 O2", "linear_35 O2"],
    "a set of teams (all teams; those below a member count)": ["linear_54 O1", "linear_54 O3"],
    "all hubs": ["box_128 O1", "box_160 O8"],
    "tasks on files": ["box_160 O7"],
    "a thread's replies": ["slack_113 O4"],
    "comments, and issues found through their comments": ["linear_55 O1", "linear_55 O4"],
    "issues reached through a relation (blocked by one issue)": ["linear_48 O3"],
}

# Rows the replica cannot decide: its Box search matches names and descriptions only, while Box's search also reads
# file content (the gap is recorded in grounding/domains/box/model_source_ledger.md, B-A10: "search does not inspect
# file bytes"). A search row is void when the words are in targets' content but not in their names.
VOID_SEARCH = {
    "box_139": "the replica finds 1 of 5 (by name); 'ethics' is also in phylosophy of sciance.md's content, which "
               "Box reads, and the other three say 'ethical', which Box may match or not (its stemming is not "
               "documented)",
    "box_158": "'Moog' is in all three targets' content and in none of their names (capacitor_replacement_log.txt, "
               "filter_calibration_procedure.txt, oscillator_schematic_notes.txt)",
}

CHANGED_AFTER_FIRST_RUN = [
    "box_118 -> box_129: box_118 asks for one file ('the first file found'); box_129 asks for all, same targets",
    "slack_107 O4, slack_109 O6: moved to PERMISSIVE (run, not counted), the criterion already used for slack_100",
    "slack_74: search '?' -> none; punctuation is not a searchable word",
    "slack_108: search 'food' -> 'food' and 'eat' combined, as the request names both",
    "box_143: extension 'pdf' -> pdf, docx and md combined, as the request names all three; and the extension "
    "route is no longer marked not applicable when the request gives no words (an ordering fault in the check)",
    "linear_32, linear_41, linear_56: 'server filter, all conditions' now carries the request's conditions "
    "(it carried the team only); linear_32 names no team, so its team routes are marked as a guess",
    "added three plural obligations the first selection missed: box_163 O2 (the FOMC files, as box_129) and "
    "linear_41 O3 and O5 (Szymon's packets, and those not sprouted)",
]
