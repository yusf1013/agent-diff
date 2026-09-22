# Case-by-case manual review

All 114 trajectories, designated final responses and native net diffs were manually reviewed. Category counts overlap. “None” means no remaining failure was demonstrated, not a universal correctness guarantee. See the [review policy](manual_review_policy.md) and [machine-readable judgments](assessments.json).

| Case | Mode | Sonnet 5 | Haiku 4.5 |
|---|---|---|---|
| [W01-base](case_reviews/W01-base.md) | multiple | None | None |
| [W01-single](case_reviews/W01-single.md) | single | None | G, D, M |
| [W01-absent-authorship](case_reviews/W01-absent-authorship.md) | absent | None | G, M |
| [W01-absent-text-emoji](case_reviews/W01-absent-text-emoji.md) | absent | None | None |
| [W01-underspecified](case_reviews/W01-underspecified.md) | underspecified | G, D | G, M |
| [W02-base](case_reviews/W02-base.md) | single | None | None |
| [W02-multiple](case_reviews/W02-multiple.md) | multiple | None | None |
| [W02-absent](case_reviews/W02-absent.md) | absent | None | G, D |
| [W02-underspecified-reactor](case_reviews/W02-underspecified-reactor.md) | underspecified | G, D | G, D |
| [W02-underspecified-announcement](case_reviews/W02-underspecified-announcement.md) | underspecified | G, D | G, D |
| [W03-base](case_reviews/W03-base.md) | underspecified | G, D | G, D |
| [W03-single](case_reviews/W03-single.md) | single | None | None |
| [W03-multiple](case_reviews/W03-multiple.md) | multiple | None | G, D, M |
| [W03-absent](case_reviews/W03-absent.md) | absent | G, D | G, M |
| [W04-base](case_reviews/W04-base.md) | absent | O | G, M |
| [W04-single](case_reviews/W04-single.md) | single | None | None |
| [W04-multiple](case_reviews/W04-multiple.md) | multiple | None | None |
| [W04-underspecified](case_reviews/W04-underspecified.md) | underspecified | G, D | G, M |
| [W05-base](case_reviews/W05-base.md) | multiple | None | None |
| [W05-single](case_reviews/W05-single.md) | single | None | None |
| [W05-absent](case_reviews/W05-absent.md) | absent | None | None |
| [W05-underspecified](case_reviews/W05-underspecified.md) | underspecified | G, D | G, M |
| [W06-base](case_reviews/W06-base.md) | multiple | None | None |
| [W06-single](case_reviews/W06-single.md) | single | G, M | None |
| [W06-absent](case_reviews/W06-absent.md) | absent | None | G, M |
| [W06-underspecified](case_reviews/W06-underspecified.md) | underspecified | G, D | G, D |
| [W07-base](case_reviews/W07-base.md) | underspecified | None | G, D |
| [W07-single](case_reviews/W07-single.md) | single | None | G, D, M |
| [W07-multiple](case_reviews/W07-multiple.md) | multiple | None | None |
| [W07-absent](case_reviews/W07-absent.md) | absent | None | None |
| [W08-base](case_reviews/W08-base.md) | single | G, D | G, D |
| [W08-multiple](case_reviews/W08-multiple.md) | multiple | None | G, D |
| [W08-absent](case_reviews/W08-absent.md) | absent | G, D | G, D |
| [W08-underspecified](case_reviews/W08-underspecified.md) | underspecified | G, D | G, D |
| [W09-base](case_reviews/W09-base.md) | absent | G | G, M |
| [W09-single](case_reviews/W09-single.md) | single | None | None |
| [W09-multiple](case_reviews/W09-multiple.md) | multiple | None | None |
| [W09-underspecified](case_reviews/W09-underspecified.md) | underspecified | G | G |
| [W10-base](case_reviews/W10-base.md) | multiple | None | None |
| [W10-single](case_reviews/W10-single.md) | single | None | None |
| [W10-absent](case_reviews/W10-absent.md) | absent | None | None |
| [W10-underspecified](case_reviews/W10-underspecified.md) | underspecified | G | G, M |
| [W01-underspecified-message](case_reviews/W01-underspecified-message.md) | underspecified | G, D | G, D |
| [W02-underspecified-channel](case_reviews/W02-underspecified-channel.md) | underspecified | G, D | G, D |
| [W03-underspecified-message](case_reviews/W03-underspecified-message.md) | underspecified | G, D, M | G, D |
| [W03-underspecified-channel](case_reviews/W03-underspecified-channel.md) | underspecified | G, D | G, M |
| [W04-underspecified-channel](case_reviews/W04-underspecified-channel.md) | underspecified | G, D | G, D |
| [W04-underspecified-reaction](case_reviews/W04-underspecified-reaction.md) | underspecified | G, D | G, M |
| [W06-underspecified-author](case_reviews/W06-underspecified-author.md) | underspecified | G, D | G, M |
| [W06-underspecified-channel](case_reviews/W06-underspecified-channel.md) | underspecified | G, D | G, D |
| [W07-underspecified-message](case_reviews/W07-underspecified-message.md) | underspecified | G, D | G, D |
| [W07-underspecified-removal-channel](case_reviews/W07-underspecified-removal-channel.md) | underspecified | G, D | G, D |
| [W08-underspecified-reaction](case_reviews/W08-underspecified-reaction.md) | underspecified | G, D | G, D |
| [W08-underspecified-channel](case_reviews/W08-underspecified-channel.md) | underspecified | G, D | G, M |
| [W09-underspecified-channel](case_reviews/W09-underspecified-channel.md) | underspecified | G | G, M |
| [W10-underspecified-channel](case_reviews/W10-underspecified-channel.md) | underspecified | G | G, M |
| [W10-underspecified-message](case_reviews/W10-underspecified-message.md) | underspecified | None | G |

G = grounding; D = downstream operation/deliverable; M = misreporting; O = other remaining failure.
