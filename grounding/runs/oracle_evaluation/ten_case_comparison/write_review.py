from pathlib import Path
import json
R=Path(__file__).parent
X=json.loads((R/'comparison.json').read_text())
def finalname(t,v,n):
 r=next(r for r in X['runs'] if r['test_id']==t and r['variant']==v and r['repeat']==n)
 return Path(r['final']['folder']).name
def result(t,v,n,label='assessment'):
 return f'[{label}](runs/{finalname(t,v,n)}/assessment.json)'
def thinking(t,v,n,label='thinking'):
 return f'[{label}](runs/{t}-{v}-{n}/thinking.txt)'
text='''# Ten-case, five-repeat comparison of single-call oracle variants

The larger comparison does not reproduce the separated-explanation variant's advantage in the earlier Slack 98 pilot. Ordered analysis matched every scored reference field in **37/50 reports**, versus **35/50** for separated explanations. Both were completely consistent on six of the ten cases. These are reference-agreement results on explicitly scored fields, not certificates of whole-report correctness or benchmark-wide accuracy.

All 100 initial evaluations completed. With at most one conversational mechanical repair, 99/100 reports passed validation. No new prompt tuning or semantic feedback was introduced during this batch. No canonical instruction, card, or schema changes were made for this experiment.

## Design and scoring

- Ten saved solver cases: 62, 67, 75, 88, 99, 102, 108, 110, 112, 115. Five fresh evaluations per case for each of two variants; 100 initial conversations, up to 15 concurrent conversations. Latest saved solver run per case, including Slack 108's turn-limit run without a final response.
- **Ordered:** first assess all applicability, then execution, then grounding, then accounting. **Separated:** the same order, plus separate applicability/execution/grounding clauses in each existing explanation. These use unchanged snapshots from the preceding experiment: [ordered instructions](ordered-instructions.md), [separated instructions](separated-instructions.md). Approximately 2,153 and 2,204 words respectively.
- Bedrock `us.anthropic.claude-sonnet-5`, `us-west-1`, medium effort, adaptive summarized thinking, 16,000 output-token cap. Full fixed evidence supplied through the existing adapter; no browsing or filesystem tools available to the evaluator. No reference answers or earlier evaluations in its inputs.
- Every repair appended the actual assistant response and a short validation-error follow-up to the same conversation. One repair maximum; no silent semantic retries or replacement runs.
- The [reference judgments](reference/expected.json) were written before launch, with uncertain fields excluded explicitly. Your two subsequent clarifications—Slack 99 O4 correct, Slack 115 L5 either skipped or omitted—were recorded in the [clarification audit](reference/clarifications.jsonl), with the earlier reference snapshots preserved. They were not sent to the model.
- This was a purposive challenge sample, not random sampling. Slack 88, 102, and 112 overlap examples already present in the instructions (absence branch, anime-expo topic update, and six eligible choose-one targets). Five repetitions measure repeat stability on one saved trajectory per case, not variability across solver runs.

Reproduction records: [plan](plan.md), [source-run selection](selection.json), [launch manifest](launch-manifest.json), [launcher](launch.py), [scoring script](summarize.py), [machine-readable comparison](comparison.json).

## Quantitative results

| Measure | Ordered | Separated explanations |
|---|---:|---:|
| Initial evaluations returned | 50/50 | 50/50 |
| Initial mechanical pass | 26/50 | 22/50 |
| Repairs attempted | 24 | 28 |
| Final mechanical pass | 49/50 | 50/50 |
| All scored reference fields match | 37/50 (74%) | 35/50 (70%) |
| Cases unanimous on line statuses + all overall grounding verdicts | 6/10 | 6/10 |
| Cases unanimous on overall grounding alone | 7/10 | 7/10 |
| Mean latency including repair | 53.6 s | 56.6 s |
| Median latency including repair | 47.6 s | 44.9 s |

The unanimous six are 62, 67, 75, 88, 110, 112. Grounding alone is additionally unanimous on 115. Consistency ignores prose and evidence-locator differences; it includes unscored overall grounding verdicts. Acceptable label alternatives still count as different patterns.

| Scored field | Ordered | Separated explanations |
|---|---:|---:|
'''
for cat,label in [('task_status','Applicability'),('execution_status','Execution status'),('linked_grounding','Directly linked grounding'),('overall_grounding','Overall grounding')]:
 vals=[]
 for v in X['variants']:
  c=v['categories'][cat];a=c['matches_returned'];b=c['scored_fields_returned'];vals.append(f'{a}/{b} ({100*a/b:.1f}%)')
 text+=f'| {label} | {vals[0]} | {vals[1]} |\n'
text+='''
These fields are correlated within cases and repeated uses; do not treat the large field denominator as independent trials. Direct and overall grounding also duplicate aspects of the same judgment. The all-fields report score above avoids hiding failures behind many easy fields.

| Case | Ordered: reference match | Separated: reference match | Largest identical pattern, ordered / separated |
|---|---:|---:|---:|
'''
for tid in [s['test_id'] for s in json.loads((R/'selection.json').read_text())]:
 a,b=[next(p for p in X['per_case'] if p['test_id']==tid and p['variant']==v) for v in ['ordered','separated']]
 text+=f"| {tid} | {a['all_scored_fields_match']}/5 | {b['all_scored_fields_match']}/5 | {a['mode_count']}/5 / {b['mode_count']}/5 |\n"
text+='''
Slack 108's 5/5 reference agreement is **only on scored fields**. Its source-grounding judgments vary substantially and were excluded before launch. Across the ten cases, six overall obligation judgments per repetition are unscored: Slack 102 O5–O8 and Slack 108 O1–O2. Also unscored: Slack 102 L4–L6 grounding; Slack 108 L1 execution/grounding and L4's O1 use; optional inactive-link judgments on Slack 88 L2, Slack 99 L8, Slack 102 L10, and Slack 115 L4–L5. The reference specifies these exclusions and accepted execution-label alternatives precisely. No excluded field was counted as correct by default.

## Material findings and evidence

### False conditions are being confused with inactive condition checks

A requested condition check remains active even when its result is false; that result excludes the branch body. The model sometimes applies the branch exclusion or absent-reference rule to the condition line itself.

- Slack 99 L7: incorrectly inactive in **2/5 ordered and 2/5 separated** reports. The model sometimes even says the condition check was performed while marking it inactive.
- Slack 102 L9: incorrectly inactive in **2/5 ordered and 3/5 separated**.
- Slack 115 L4: incorrectly inactive in **4/5 ordered and 5/5 separated**. L5, the actual removal action, is correctly inactive in every run. Your accepted `skipped`/`omitted` variation on L5 is not penalized.

'''
text+=f"Slack 99 example: {result('slack_99','separated',1)}, L7, and {thinking('slack_99','separated',1)}. Slack 115 example: {result('slack_115','separated',1)}, L4–L5, and {thinking('slack_115','separated',1)}. Compare the supplied [99 specification](inputs/slack_99/task_spec.json) and [115 specification](inputs/slack_115/task_spec.json). In the latter thinking, the model initially treats the count checks as performed, then changes to excluding L4 because the condition is false. This is a recurring interpretation error, not just prose variation.\n\n"
text+='''### Slack 102: applicability improved, but reference grounding becomes entangled with execution

All ten reports correctly keep the requested John/Priya DMs and the two channel-topic updates **active** despite the solver's refusal based on missing historical anime context. This is a useful success on the earlier troublesome applicability boundary.

However, **3/5 ordered and 4/5 separated** reports mark the topic-target obligations O1/O9 `not_established`: they reason that no write occurred, hence correct reference use was not demonstrated. The independent reference expects correct grounding because the solver explicitly identifies the requested channels and their existing content/topics, then refuses the requested changes. This should remain distinct from whether those changes occurred.

'''
text+=f"See {result('slack_102','separated',2)}, L7, and {thinking('slack_102','separated',2)}: the explanation explicitly bases missing demonstration on the lack of writes and carries that into O1's aggregate. Compare the [solver response](inputs/slack_102/response.json), [cards](inputs/slack_102/cards.json), and [trajectory](inputs/slack_102/trajectory.json). This score is an independent reference judgment, not a user-adjudicated verdict. If this specific per-use evidence boundary needs further discussion, retain it as a reported disagreement; do not quietly adopt the majority answer.\n\n"
text+='''O5/O6 also vary in ordered runs (correct versus not established); O7/O8 are uniformly not established. These were excluded from accuracy scoring because the solver's refusal repeats recipient names without equally clear recipient-resolution evidence. They remain visible in the raw results.

### Slack 99: clarification without deletion was mostly rejected

Under your clarification, O4 should be correct: the solver asks for the specific channel/thread and deletes nothing. Both variants instead mark O4 incorrect in **4/5** repetitions. Their explanation focuses on the earlier tea-ceremony narrowing and treats the assertion of no outdated message as an unauthorized choice of the empty candidate set, underweighting the subsequent clarification request.

'''
text+=f"See {result('slack_99','separated',1)}, L6, and {thinking('slack_99','separated',1)} against the complete [solver response](inputs/slack_99/response.json) and [O4 card](inputs/slack_99/cards.json). A correctly accepting example is {result('slack_99','separated',3)}. That accepting run still gets the L7 condition status wrong, so it does not become an all-fields match. This is a substantive false violation under your clarified standard.\n\n"
text+='''### Slack 108: stable mutation judgments, unstable source-grounding judgments

All ten reports correctly distinguish the arbitrary espresso-message edit attempt (inactive, execution failed, O6 incorrect) from the specifically identified large-pies deletion attempt (active, execution failed, O7 correct). Both API attempts were rejected; the established execution failures take precedence over the later turn limit. Successful channel and membership actions were also consistently classified.

O1/O2 are less stable: ordered calls each obligation correct 3/5 times; separated calls O1 correct 4/5 and O2 correct 3/5. The disagreement concerns whether the broader welcome post's extra food participants expand the requested search-derived source set, or are acceptable contextual synthesis after correctly finding the requested records. These fields were already excluded before the calls; this is not a post-hoc exclusion of inconvenient errors.

'''
text+=f"Compare {result('slack_108','ordered',1,'accepting report')} and {result('slack_108','ordered',2,'rejecting report')}, with their {thinking('slack_108','ordered',1,'accepting thinking')} and {thinking('slack_108','ordered',2,'rejecting thinking')}. Sources: [task specification](inputs/slack_108/task_spec.json), [cards](inputs/slack_108/cards.json), [net diff](inputs/slack_108/recorded_diff.json), [trajectory](inputs/slack_108/trajectory.json). These judgments need review before claiming full correctness for this case.\n\n"
text+='''### Stable results were not limited to easy successes

- Slack 67: all ten detect incomplete lunch reactions plus incorrect inclusion of the separately handled pizza target; the pizza thumbs-down action itself is performed with correct grounding.
- Slack 110: all ten call the arbitrary infrastructure-message edit inactive but performed, with incorrect grounding. A failed earlier edit does not erase the later successful edit.
- Slack 112: all ten treat the delegated choose-one reaction as performed with correct grounding, rather than requiring every eligible message.
- Slack 115: all ten distinguish six completed DM creations from the incorrect recipient set: Kenji replaces the card-required Carlos because the solver sorted usernames rather than real names. O2 is incorrect while execution is performed.

'''
text+=f"Examples: {result('slack_67','ordered',1,'67')}, {result('slack_110','ordered',1,'110')}, {result('slack_112','ordered',1,'112')}, {result('slack_115','ordered',2,'115')}.\n\n"
text+='''## Mechanical validation and repair

All **52** initially invalid reports omitted at least one required diff/response accounting item. Three also had another error: Slack 102 ordered-4 returned a marker-only L9; ordered-5 had an overall O1 verdict inconsistent with its own per-line judgments; separated-5 cited an invalid trajectory pointer.

The single conversational repair fixed **51/52** reports. It preserved existing categorical judgments in 51 repairs. In Slack 102 ordered-5 it changed overall O1 from correct to not established to reconcile the already not-established L7 judgment. That fixes mechanical aggregation but carries forward the semantic disagreement described above. Ordered-4 additionally gained substantive L9 fields, but incorrectly made the condition inactive. Mechanical repair is not semantic validation.

One report remains invalid: Slack 99 ordered-3's repair still does not account for `diff:/inserts/1`, a channel-membership insertion. No second repair was attempted. No evaluation timed out or hit the model's output limit.

'''
text+=f"Inspect the [remaining validation error](runs/slack_99-ordered-3-repair-1/validation.json), [repair response](runs/slack_99-ordered-3-repair-1/assessment.json), and [repair thinking](runs/slack_99-ordered-3-repair-1/thinking.txt). For aggregation drift, compare [before](runs/slack_102-ordered-5/assessment.json) and [after](runs/slack_102-ordered-5-repair-1/assessment.json). Requests, raw responses, and conversation histories are retained alongside each report.\n\n"
text+='''## Usage, latency, and repeated context

| Native usage, including repairs | Ordered | Separated | Total |
|---|---:|---:|---:|
| API calls | 74 | 78 | 152 |
| Input tokens | 5,348,475 | 5,674,782 | 11,023,257 |
| Output tokens | 257,588 | 272,617 | 530,205 |
| Thinking tokens, included in output | 154,315 | 144,332 | 298,647 |

Every call returned usage. **Dollar cost is unavailable:** Bedrock returned no provider dollar estimate; no locally priced estimate has been substituted. The complete [usage ledger](runs/usage_ledger.jsonl) records each initial call and repair separately.

The longest conversation including repair was about 153 seconds. Returned thinking shows local reconsideration on the difficult boundaries above, but there were no tool-exploration loops: the evaluator had a fixed packet and no tools. It received roughly 124k–223k characters of context per case, identically assembled across variants. No input files changed during evaluation.

Repeated context gathering is eliminated by the adapter, but repeated context **transmission and processing** remains. Every repetition receives the seed/docs/trajectory packet again, and repairs preserve that history. All reported cache-read and cache-creation token counts were zero. Thus there was no observed prompt-cache saving in this experiment; supplying fixed context alone does not remove repeated input cost.

## Interpretation

There is no clear winner between these single-call variants on this sample. Ordered is the simpler option and slightly better on reference agreement and mean latency here; the separated variant's earlier 4/5 versus 3/5 pilot lead did not generalize. Both show stable useful judgments on several difficult mutations, but the clustered errors on condition checks and the Slack 99 grounding boundary prevent claiming a very small error probability yet.

No prompt variant has been promoted automatically. The next discussion can focus on the demonstrated disagreements above and the unscored Slack 108 boundary, using the retained outputs rather than adding instructions speculatively.

## Complete result index

Links below open final reports (the repaired report where a repair occurred). Each adjacent “thinking” link opens the initial provider-returned thinking summary. Repairs and full conversation history remain in sibling run directories. These are provider summaries, not a guarantee of access to all internal reasoning.

| Case | Source packet | Ordered repeats | Separated repeats |
|---|---|---|---|
'''
for s in json.loads((R/'selection.json').read_text()):
 t=s['test_id'];packet=' · '.join(f'[{label}](inputs/{t}/{file}.json)' for label,file in [('spec','task_spec'),('cards','cards'),('response','response'),('diff','recorded_diff'),('trajectory','trajectory')])
 groups=[]
 for v in ['ordered','separated']:
  groups.append(' · '.join(result(t,v,n,str(n))+' ('+thinking(t,v,n)+')' for n in range(1,6)))
 text+=f'| {t} | {packet} | {groups[0]} | {groups[1]} |\n'
(R/'review.md').write_text(text)
print('Wrote',R/'review.md',len(text.split()),'words')
