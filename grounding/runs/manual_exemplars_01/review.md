# Manual suite review

The reviewed result is **32 new variants plus 10 originals: 42 full tests**. Every case has a concrete seed, prompt, grounding card, task specification, independent expected targets, and reference outcome. These are manually authored tests, not automated campaign results.

| Resolution mode | Originals | New variants | Total |
|---|---:|---:|---:|
| Single | 2 | 8 | 10 |
| Multiple | 4 | 6 | 10 |
| Absent | 2 | 9 | 11 |
| Underspecified | 2 | 9 | 11 |
| **Total** | **10** | **32** | **42** |

W01 has two absence mechanisms. W02 has two ambiguity mechanisms. Each other family adds its three missing modes. W01/W05/W06/W10 single variants intentionally retain plural wording when the fixture contains exactly one qualifying target, following the agreed W01 convention. This is an instance-cardinality distinction; no coverage-catalog policy is changed here.

## Executable test index

`base` denotes the corresponding original story. Links open complete JSON tests.

| Family | Single | Multiple | Absent | Underspecified |
|---|---|---|---|---|
| W01 | [single](cases/W01-single.json) | [base](cases/W01-base.json) | [absent-authorship](cases/W01-absent-authorship.json) / [absent-text-emoji](cases/W01-absent-text-emoji.json) | [underspecified](cases/W01-underspecified.json) |
| W02 | [base](cases/W02-base.json) | [multiple](cases/W02-multiple.json) | [absent](cases/W02-absent.json) | [underspecified-reactor](cases/W02-underspecified-reactor.json) / [underspecified-announcement](cases/W02-underspecified-announcement.json) |
| W03 | [single](cases/W03-single.json) | [multiple](cases/W03-multiple.json) | [absent](cases/W03-absent.json) | [base](cases/W03-base.json) |
| W04 | [single](cases/W04-single.json) | [multiple](cases/W04-multiple.json) | [base](cases/W04-base.json) | [underspecified](cases/W04-underspecified.json) |
| W05 | [single](cases/W05-single.json) | [base](cases/W05-base.json) | [absent](cases/W05-absent.json) | [underspecified](cases/W05-underspecified.json) |
| W06 | [single](cases/W06-single.json) | [base](cases/W06-base.json) | [absent](cases/W06-absent.json) | [underspecified](cases/W06-underspecified.json) |
| W07 | [single](cases/W07-single.json) | [multiple](cases/W07-multiple.json) | [absent](cases/W07-absent.json) | [base](cases/W07-base.json) |
| W08 | [base](cases/W08-base.json) | [multiple](cases/W08-multiple.json) | [absent](cases/W08-absent.json) | [underspecified](cases/W08-underspecified.json) |
| W09 | [single](cases/W09-single.json) | [multiple](cases/W09-multiple.json) | [base](cases/W09-base.json) | [underspecified](cases/W09-underspecified.json) |
| W10 | [single](cases/W10-single.json) | [base](cases/W10-base.json) | [absent](cases/W10-absent.json) | [underspecified](cases/W10-underspecified.json) |

## Review against the agreed standards

The review used [the original manual designs and feedback](../../archive/slack_campaign/design_review.md), [the writer-pilot review](../slack_campaign/writer_pilot_04/review.md), and [the later compiler reviews](../slack_campaign/compiler_pilot_02/manual_reviews/). Earlier seed-reuse notes are superseded by the agreed fresh-environment policy. The current cases use fresh environments.

| Standard | Review result |
|---|---|
| Natural request, supported operation | Requests remain short, without candidate menus, search instructions, emphasized ALL, or explanations of the trap. W01–W08 use writes; W09/W10 ask substantive open-ended questions. W07 required the approved channel revision below. |
| Preserve the intended route | Each selector follows the required relationships. Additional name/channel lookups are explicit identifying paths, not substitute answer IDs or new coverage-route claims. |
| Preserve modes and alternatives | Resolved collections are jointly intended. Singular descriptions with competing matches have explicit alternatives and no delegated choice. W01 alternatives identify different Priyas' message sets; W10 preserves `{Alice, Ben}` versus `{Elena}`, not three independent choices or one combined answer. |
| Derive negatives from conditions | Wrong emoji/person/topic/channel, missing relationships, wrong relationship roles and split bindings are retained. Legitimate alternatives are not negatives. New variants remove or change the specific positive witnesses needed to change mode. |
| Same-record binding | Emoji, reactor, message, and membership conditions must occur along one connected path. Independent occurrence of those facts elsewhere never creates a match. |
| Clean semantic boundaries | Office relocation messages contain rooms/moving dates, with no budget approval, rollout checklist, or security audit. Cancellation/negation is not used as a shortcut for topic exclusion. Explicit `#channel` names distinguish near names. |
| No giveaways | Seed text does not say decoy, ignore this, no action needed, or disclose row roles. M1–M9 are private labels, not text shown to the solver. The requested reaction is not suggested by the subject matter. |
| Preserve negative mechanisms during instantiation | W06 Lucia truly has zero channel memberships; Theo's historical message does not imply current membership. W08 Elena remains outside the relevant channel. W05 private-channel membership and exact counts are preserved. W10 negative memberships remain real records. |
| Avoid answer shortcuts | W10 uses the same text and author in the qualifying and wrong-channel checklist messages. Admin/owner flags are answer content, not identifying filters. W08 message subjects do not reveal the author's channel memberships. |
| API-supported answer fields | W09 reports the workspace ID actually exposed on a profile; explanatory workspace names are not assumed exposed. W10 derives flags from `user_teams.role`; an owner is also an admin. |
| Minimal cards and task specifications | One consolidated route-based obligation and one requested action per case. Cards use the locked fields plus the authorized identifying-path extension. Pure removal has `Written attributes: []`. Known count restrictions remain in underspecified partial constraints. |
| Source independence | Manually specified expected sets are compared with selectors and with independently written relationship traversals. Neither check is a general semantic-language validator; concrete message meanings were manually reviewed. |

No remaining semantic validity defect was identified in this review. These are controlled small environments with meaningful relational negatives. Their empirical difficulty and failure-exposure rate are **unmeasured**. W09 is the lightest family, with only two or three explanatory workspace rows; validity does not make it a strong stress test. A whole row-count or shortcut-resistance score is not inferred from passing validation.

## Native verification and corrections

- **42/42** pass seed/schema/foreign-key, selector, card, task-link and independent expected-set checks: [checks.json](checks.json), [independent audit](audit_suite.py).
- **42/42** load into isolated PostgreSQL schemas and pass native Slack read/visibility checks: [read_checks.json](read_checks.json). Reads leave state unchanged. Required W09/W10 probes additionally verify the workspace and role answer fields.
- **16/16** resolved state-changing cases successfully execute the requested native operations and produce exactly the intended net changes: [write_checks.json](write_checks.json). Checks cover all changed tables, exact targets/text/thread parents, recipient-specific DMs, and absence of unrelated changes. These are reference-operation smoke tests with known targets, not solver runs.
- Absent and underspecified mutations are not executed by the reference checks. Their expected behavior is acknowledgment/clarification without making an unsupported selection. Read-only cases remain read-only. Assessing a solver's actual response still requires the existing evaluator and recorded execution.

The write test discovered `cant_kick_from_general` for W07. The user explicitly approved replacing **#general with #team-hub** throughout that family's original story, variants and tests. All people, reactions, alternatives and negative patterns remain unchanged. The corrected single and multiple cases now pass. The earlier rejection is preserved in [write_checks_before_channel_fix.json](write_checks_before_channel_fix.json); it is not an outcome on the final fixtures.

Two verification-harness issues were corrected without weakening a case: profile-probe paths must be arrays rather than dotted strings; and write-check middleware must commit the scoped transaction, matching the real runtime boundary. The initial uncommitted-session diagnostic is retained in [write_checks_initial_uncommitted_sessions.json](write_checks_initial_uncommitted_sessions.json). Final checks refer to the final case hashes in [manifest.json](manifest.json).

All temporary native schemas were cleaned up. **No solver/evaluator experiments or paid model calls were made. No commits were made.** Platform HTTP authentication and the solver sandbox were not exercised by these in-process checks.
