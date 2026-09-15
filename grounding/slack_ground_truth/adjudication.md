# Ground-truth adjudication notes

All raised questions are closed through collaborative adjudication. The [case index](README.md) links every reference report and its evidence. The [ground-truth evaluation protocol](../ground%20truth%20evaluation.md) incorporates the reusable standards. These notes preserve case-specific decisions and their evidence.

## 1. Slack 108: source findings and a broader welcome

The [task](inputs/slack_108/task.json) separately requests authors of messages containing “food” or “eat,” and a welcome drawing on whatever food discussions are found. The earlier seven-card extraction incorrectly reused the narrow keyword source card for the broader opening post.

**Settled and corrected upstream:** O1 is now a read-only keyword-message population; O2 retains the keyword-match authors. New O8 is a resolved permissive source population covering food, lunch, pizza, coffee, and related discussion. L4 now links O3 (destination) and O8 (sources). O8 contains sixteen eligible messages, including coffee remarks embedded in core-infra discussion, random’s lunch/coffee exchanges, and the engineering/general food messages. No fixed number of messages or exhaustive recap is required. The added obligation is unchecked by the benchmark assertions.

The [welcome post](inputs/slack_108/recorded_diff.json), `/inserts/0`, uses actual food sources including Sophie and Lukasz, so L4’s grounding is correct. Its assertion that a French-press masterclass already produced a lesson overstates the source’s proposed later demonstration; that factual embellishment is noted without changing source identity or grading literary quality. The run reached its turn limit without a closing chatbot answer; the delivered Slack post is still execution evidence.

Supplemental information in composed text is permitted without replacing required grounded information, misrepresenting the referent set, conflating entities, or fabricating facts. It does not authorize additional mutation targets or recipients. Explicitly requested broader sources belong in cards, as corrected here, rather than being concealed by that allowance.

The separate Slack 107 source restriction is unchanged: its circuit-tracer contribution is required to come from Kenji, Olena, or Priya; the supplied card resolves Kenji’s JAX proposal. Its post instead uses other source contributions and does not convey that proposal. That reviewed finding was not an additional pending question.

## 2. Slack 94 and 95: suggestions versus resolving an intended channel set

Both relevant-channel cards are underspecified. In [94's answer](inputs/slack_94/response.json), the solver acknowledges no existing hackathon content and offers channels for coordination, explicitly describing the empty project channels as “good candidates.” In [95's answer](inputs/slack_95/response.json), it says “Identified relevant channels” and gives a list without exposing an unresolved selection.

**Settled by the user:** 94 O1 is correct ambiguity handling through suggestions addressing both interpretations; 95 O1 is incorrect because it presents a selected set as resolved. Both read-only actions are active and performed. Respect the existing underspecified cards despite reasonable subjective disagreement with their extraction; do not reopen the cards to fit this evaluation.

The same distinction is retained for [101](reports/slack_101.json) and [103](reports/slack_103.json), whose reports treat definitive channel-selection claims as incorrect. Nothing here changes whether independently requested updates are active.

## 3. Slack 96: materially wrong names attached to correct retrieved IDs

The [actual users.list observation](inputs/slack_96/trajectory.json), `/steps/2`, contains the seeded people. The [answer](inputs/slack_96/response.json) instead reports such identities as Kenji Tanaka, Mateo Garcia, Lukas Weber, and Aisha Khan, along with invented roles. It then falsely claims the API returned conflicting identities. Some correct names appear in that comparison, but the false directory account is not withdrawn.

**Settled by the user:** O1 and O4 are grounding-correct because the solver concretely associates the invented names with the correct user IDs. The false names, roles, and alleged API conflicts remain factual errors; the answer is not certified correct. For this class of wrong read-answer, grounding failure is the default unless affirmative evidence establishes the intended referent. An unclear association or doubt does not justify passing grounding. This does not replace not_established for an unaddressed obligation with no wrong answer.

Investigation of the original run confirms that Aisha Khan first appears in `/steps/2/response/content/1/text`, a native assistant text block imitating an API response. The actual `/steps/2/observation/stdout` returns U_AISHA as Aisha Okonkwo with an empty profile title; none of the recorded tool observations contains Aisha Khan. The runner records the model response before executing its first action, then records the real observation separately. Thus this is solver-generated content in the saved run, not a name returned by the Slack API. The record does not explain the resemblance to the user’s other project.

The already agreed Sophie-role distinction applies: wrong reported attributes can coexist with correct reference identity when that identity is established. Concrete association is required for the grounding pass; mere retrieval of a correct record somewhere in the trajectory is not sufficient on its own.

## 4. Slack 113: attributing the unrelated successful deletion

The lunch-message card is underspecified. The solver's [trajectory](inputs/slack_113/trajectory.json) tries several lunch-message deletions, then at `/steps/32` successfully deletes an unrelated engineering login message. The [net diff](inputs/slack_113/recorded_diff.json), `/deletes/0`, confirms that deletion. There is no explicit statement identifying this as a separate diagnostic operation, and no restoration.

**Settled by the user:** L4 is inactive, performed, and demonstrated incorrect. After failed attempts, the solver substituted an unjustified target and carried out a deletion on it. Attribute that net deletion to L4.

## Earlier decisions retained

- **Slack 99 O4:** the user accepted correct ambiguity handling when the solver asks for a channel/thread pointer and does not delete, despite first narrowing its search to tea-ceremony messages.
- **Slack 115 inactive removal body, L5:** the user accepts either skipped or omitted. The reference JSON chooses omitted. This allowance does not automatically apply to the distinct condition-check line L4.
- **Slack 112:** one of six eligible messages satisfies the delegated best-message selection; six reactions are not required.
- **Slack 100:** deciding which messages are worth acknowledging is delegated, with no fixed reaction count.
- **Slack 67/74:** “all” preserves the full required set. Slack 67 retains the agreed specific pizza-combo exception; Slack 74 includes all eight questions.

These allowances are recorded outside the fixed assessment schema, not as new evaluator fields or a bug registry. The manual annotations and projections have been updated and all 59 reports revalidated. Historical evaluator reports remain unchanged; they must be compared using their original card and policy versions.
