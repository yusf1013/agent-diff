"""Linear controls: target-removed/added flips and isolated one-near-miss variants."""
from __future__ import annotations

import copy
import json
from functools import partial

from grounding.runs.fact_coverage_01.pilot import cases_linear as L
from grounding.runs.fact_coverage_01.pilot.variants import absent_of, isolate, present_of


def lin_02_p():
    base = L.lin_02()
    row = {"id": "c-5", "issueId": "i-eng-42", "userId": "u-leo", "body": "Can we postpone the release until the migration lands?",
           "bodyData": json.dumps({"type": "doc", "content": []}), "parentId": None, "resolvingUserId": None,
           "resolvedAt": None, "reactionData": {}, "url": "https://linear.app/northwind/comment/c-5",
           "createdAt": L.T0, "updatedAt": L.T0}
    return present_of(base, "comments", [("comments", row)], ["c-5"])


def lin_04_p():
    base = L.lin_04()
    row = {"id": "r-5", "issueId": "i-eng-9", "relatedIssueId": "i-eng-7", "type": "blocks",
           "issueTitle": "Run database migration for the v2 schema", "relatedIssueTitle": "Upgrade auth library",
           "createdAt": L.T0, "updatedAt": L.T0}
    return present_of(base, "issue_relations", [("issue_relations", row)], ["r-5"])


PRESENT_BASE = [L.lin_01, L.lin_03, L.lin_05, L.lin_06, L.lin_07, L.lin_09]
FLIPS = [partial(lambda b: absent_of(b()), b) for b in PRESENT_BASE] + [lin_02_p, lin_04_p]
ABSENT = [(L.lin_02, 4), (L.lin_04, 4)] + [(partial(lambda b: absent_of(b()), b), None) for b in PRESENT_BASE]


def _iso(builder, k):
    return isolate(builder(), 0, k)


ISOLATED = []
for builder, _ in ABSENT:
    n_claims = len(builder()["references"][0]["claims"])
    ISOLATED += [partial(_iso, builder, k) for k in range(n_claims)]

CASES = FLIPS + ISOLATED
