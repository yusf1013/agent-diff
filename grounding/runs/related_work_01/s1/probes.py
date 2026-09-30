"""The S1 probes: Agent-Diff plural obligations, their kind of request and parameters (chosen before any run)."""

# (test, obligation, kind, parameters). Parameters name the request's own container, words and extension; `None`
# words mean the request gives no search words. Chosen before any run, from the request's wording.
PROBES = [
    ("slack_67", 1, "slack", {"channel": "random", "search": "lunch"}),
    ("slack_74", 1, "slack", {"channel": "random", "search": "?"}),
    ("slack_75", 1, "slack", {"channel": "engineering", "search": "login"}),
    ("slack_76", 1, "slack-messages", {"search": "login"}),  # slack_77 O1 has the same targets and wording
    ("slack_106", 1, "slack-channels-any", {"search": None}),
    ("slack_107", 4, "slack-messages", {"search": "GPU"}),
    ("slack_108", 1, "slack-messages", {"search": "food"}),
    ("slack_109", 6, "slack-channels-any", {"search": "latency"}),
    ("slack_110", 6, "slack-messages", {"search": "supercomputer"}),
    ("slack_112", 1, "slack-channels-any", {"search": None}),  # slack_113 O1 has the same targets
    ("box_118", 1, "box-anywhere", {"words": "fomc", "ext": "pdf"}),  # box_129 O1: same targets and words
    ("box_127", 2, "box", {"folder": "investments", "words": None, "ext": None}),
    ("box_139", 1, "box", {"folder": "readings", "words": "ethics", "ext": None}),
    ("box_141", 1, "box", {"folder": "agent-diff-research", "words": "results", "ext": "json"}),
    ("box_143", 2, "box", {"folder": "readings", "words": None, "ext": "pdf"}),
    ("box_150", 1, "box", {"folder": "investments", "words": "fomc", "ext": "pdf"}),
    ("box_151", 1, "box", {"folder": "investments", "words": "pdf", "ext": "pdf"}),
    ("box_152", 1, "box", {"folder": "macroeconomics", "words": "fomc", "ext": "pdf"}),
    ("box_155", 1, "box", {"folder": "macroeconomics", "words": "csv", "ext": "csv"}),
    ("box_158", 1, "box-anywhere", {"words": "Moog", "ext": "txt"}),
    ("linear_32", 1, "linear", {"team": "Engineering"}),  # the request names no team; the team route is a scope guess
    ("linear_41", 1, "linear", {"team": "Seed Library"}),
    ("linear_56", 2, "linear", {"team": "Racing Operations"}),
]
SAME_AS = {"slack_77": "slack_76", "slack_113": "slack_112", "box_129": "box_118"}
LEFT_OUT = {
    "slack_92": "the card counts the whole #random history as 'the Gemini discussion', so a search that finds the "
                "Gemini messages would count as missing the rest",
    "slack_100": "a delegated judgment ('if you judge anything important'): missing some is not a failure",
    "slack_108 O8": "a permissive source set for an opening post",
    "slack_112 O3": "choose one eligible message",
    "slack_113 O4": "a thread's replies: no route table",
    "linear_48": "issues blocked by one issue: a relation, not a listing (no route table)",
    "linear_55": "issues found through their comments (no route table)",
    "linear_54": "choose any eligible issue",
    "calendar": "no obligation cards yet (step 1 of the projection plan)",
}
