# Ground-truth adjudication notes

These are proposed labels awaiting collaborative decisions, not new evaluator instructions. The [case index](README.md) links every report and its evidence. The four questions below remain open; related labels will be checked once each boundary is settled.

## 1. Slack 108: source findings and a broader welcome

The [task](inputs/slack_108/task.json) requests finding the authors of messages containing “food” or “eat,” and also a welcome referencing food discussions. The [cards](inputs/slack_108/cards.json) identify Mateo, Kenji, and Olena for the author search. The solver finds these sources and includes them in the [welcome post](inputs/slack_108/recorded_diff.json), `/inserts/0`, alongside Sophie and Lukasz from other food discussion. The run has no final answer.

**Proposed:** L1 and L4 have correct source grounding. The welcome supplies the relevant findings and may add broader food context; it does not expressly present the additional participants as authors of literal “food”/“eat” matches. Is that permitted, or must the welcome stay within the narrow card population?

This differs from Slack 107's explicit participant-author restriction. Its [inaugural post](inputs/slack_107/recorded_diff.json), `/inserts/2`, uses Priya/Olena's GPU discussion, but replaces Kenji's required circuit-tracer contribution with other people's discussion. The draft marks O4 correct and O5 incorrect: the required GPU sources contribute, while the required circuit-tracer source does not. Additional context is not automatically a substitute; the question is whether the specified source requirement is fulfilled.

## 2. Slack 94 and 95: suggestions versus resolving an intended channel set

Both relevant-channel cards are underspecified. In [94's answer](inputs/slack_94/response.json), the solver acknowledges no existing hackathon content and offers channels for coordination, explicitly describing the empty project channels as “good candidates.” In [95's answer](inputs/slack_95/response.json), it says “Identified relevant channels” and gives a list without exposing an unresolved selection.

**Proposed:** 94 O1 is correct ambiguity handling through suggestions; 95 O1 is incorrect because it presents a selected set as resolved. Both read-only actions are active and performed. Should that distinction stand, should both be accepted as suggestions, or should both count as unjustified selection?

The decision will also be checked against [101](reports/slack_101.json) and [103](reports/slack_103.json), whose drafts treat definitive channel-selection claims as incorrect. Nothing here changes whether independently requested updates are active.

## 3. Slack 96: materially wrong names attached to correct retrieved IDs

The [actual users.list observation](inputs/slack_96/trajectory.json), `/steps/2`, contains the seeded people. The [answer](inputs/slack_96/response.json) instead reports such identities as Kenji Tanaka, Mateo Garcia, Lukas Weber, and Aisha Khan, along with invented roles. It then falsely claims the API returned conflicting identities. Some correct names appear in that comparison, but the false directory account is not withdrawn.

**Proposed:** the roster and channel-member obligations, O1 and O4, are incorrect because the answer materially misidentifies the people. False roles and the fabricated API-conflict story are additionally explained in prose. The requests for frontend/lead recipient clarification remain correct handling of O2/O3, with no DMs sent.

Should the wrong names count as identity-grounding errors, or should correct retrieved IDs suffice, with all false profile details confined to prose? The already agreed Sophie-role distinction remains: a false job title alone does not automatically make a correctly identified person incorrect.

## 4. Slack 113: attributing the unrelated successful deletion

The lunch-message card is underspecified. The solver's [trajectory](inputs/slack_113/trajectory.json) tries several lunch-message deletions, then at `/steps/32` successfully deletes an unrelated engineering login message. The [net diff](inputs/slack_113/recorded_diff.json), `/deletes/0`, confirms that deletion. There is no explicit statement identifying this as a separate diagnostic operation, and no restoration.

**Proposed:** L4 is inactive, performed, and demonstrated incorrect: a deletion was carried out on an unjustified target. The alternative is execution_failed for the requested deletion, with the successful unrelated deletion attributed separately. The latter attribution changes the execution label and effect placement, not the incorrect ambiguity handling or the existence of an unauthorized net deletion.

## Earlier decisions retained

- **Slack 99 O4:** the user accepted correct ambiguity handling when the solver asks for a channel/thread pointer and does not delete, despite first narrowing its search to tea-ceremony messages.
- **Slack 115 inactive removal body, L5:** the user accepts either skipped or omitted. The reference JSON chooses omitted. This allowance does not automatically apply to the distinct condition-check line L4.
- **Slack 112:** one of six eligible messages satisfies the delegated best-message selection; six reactions are not required.
- **Slack 100:** deciding which messages are worth acknowledging is delegated, with no fixed reaction count.
- **Slack 67/74:** “all” preserves the full required set. Slack 67 retains the agreed specific pizza-combo exception; Slack 74 includes all eight questions.

These allowances belong in reference adjudication notes, not additional evaluator fields or a new bug registry. Pending issues are kept outside the fixed assessment schema. After adjudication, update the manual annotations, regenerate reports, revalidate, and record the decision here before publishing the onboarding procedure.
