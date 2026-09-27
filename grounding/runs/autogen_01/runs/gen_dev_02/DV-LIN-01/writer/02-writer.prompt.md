A cold reader, who saw only the request and then the records, reports:
- The reader says the decoy `i-decoy-rel` (for R:Issue.projectMilestoneId, conditions ['c2']) fails ['c2', 'c3', 'c4']: it fails more than its own fact (No milestone at all.).
- The reader finds the phrase "hasn't started yet" genuinely ambiguous, in a way that changes which records match: Milestone-status reading gives a unique match (i-target); issue-status reading also matches i-decoy-status, breaking uniqueness.
- (Not blocking) The reader thinks a careful colleague could argue that decoy `i-decoy-status` meets the request: Milestone status is next, not unstarted; issue state is Todo though.

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.