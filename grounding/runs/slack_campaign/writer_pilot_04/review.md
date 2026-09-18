# Revised writer and self-reflection: ten fresh assignments

The revised pipeline produces **6/10 conceptually ready sketches**, compared with
**5/10** in the previous pipeline. First-pass readiness improves from **3/10 to
5/10**. All ten reflections return a final sketch; the previous run had one
output-budget failure. This is a modest improvement, with four unresolved cases.

“Ready” means no material conceptual construction defect under our agreed writer
standard, including the required negatives. It does not mean a validated runnable
test. A coherent task can still fail this stricter construction standard: W02 and
W07 lack required negatives. W04 and W05 have risks to the intended selection itself.

Read [all first outputs](outputs.md), [all reflected outputs](reflection/outputs.md),
[per-case manual labels](comparison.json), and the [previous review](../writer_pilot_03/reflection/review.md).

## What changed and what was held fixed

The [v4 prompt notes](../../../prompts/GENERATION_HISTORY.md) document
the run6 lessons retained: explicit conditions, distinct roots in one shared
environment, preserved witness bindings, reverse reading of the request, visible
evidence, consequential alternatives, and credible near misses. We retain our
path-derived negatives rather than run6's single focal decoy and condition cap.

The [writer instructions](../../../prompts/writer/writer.md)
now choose an operation first, translate the complete route, plan independent
negatives before fixing the story, and recompute selection across the entire table.
Each assignment receives only its referent's operation menu and its mode fragment.
One longer-route example demonstrates shared messages and distinct user roots.
The [reflection](reflection/followup.md) requests actual roots, a condition-to-row
mapping, a specific capability check, and concrete repairs.

Main writer instructions shrink from 702 to 628 words, and reflection from 338 to
299. These counts exclude the model, capability brief, menus and examples. The
[recorded system](system.md) and each assignment contain the actual full inputs;
this is not a claim that the entire request is 628 words.

The [experiment plan](plan.md) uses the same ten route/mode/count assignments as
v3, but fresh conversations and stories. Same Sonnet 5, medium effort, 6,000 output
tokens per call. Ten initial calls and exactly one native continuation each; no
case-specific manual feedback, semantic retries, compiler or solver calls. Two
substantive calls check caching before each phase's remaining eight run in parallel.
The [initial manual assessments](initial_assessment.json) were saved before reflection.

This is development-set iteration, not held-out validation. The prompts changed
together, and each assignment has one sample; individual changes cannot be credited
causally, nor do these counts establish repeatability.

## Results

| Measure | Previous v3 | Revised v4 |
|---|---:|---:|
| First-pass ready | 3/10 | 5/10 |
| Ready after reflection | 5/10 | 6/10 |
| Complete reflection outputs | 9/10 | 10/10 |
| Newly ready through reflection | 2 | 1 |
| Initially ready sketches preserved | 3/3 | 5/5 |
| Combined estimated cost | $0.8707 | $0.8981 |

| Case | V4 first pass | V4 reflection | Main assessment |
|---|---|---|---|
| [W01](W01/writer/turn-02/output.md) | Ready | Ready | Two matches and emoji/person/missing-edge/split-binding negatives preserved. |
| [W02](W02/writer/turn-02/output.md) | Needs revision | Needs revision | Wrong-message negative changes both topic and channel; no channel-only negative. |
| [W03](W03/writer/turn-02/output.md) | Needs revision | Ready | Adds the missing non-Alex reactor negative. Two competing destinations remain consequential. |
| [W04](W04/writer/turn-02/output.md) | Needs revision | Needs revision | Marketing launch checklist can reasonably be a rollout checklist; reflection accepts the questionable distinction. |
| [W05](W05/writer/turn-02/output.md) | Needs revision | Partly repaired | Repairs a malformed membership-count row, but continues treating a private qualifying channel as a nonmatch. |
| [W06](W06/writer/turn-02/output.md) | Ready | Ready | Keeps author membership distinct from message location. |
| [W07](W07/writer/turn-02/output.md) | Needs revision | Minor cleanup only | Coherent ambiguity and supported write, but still missing a non-Jordan name-only negative. |
| [W08](W08/writer/turn-02/output.md) | Ready | Ready | Own-reaction removal; varying authors avoids inconsistent facts about one fixed person. |
| [W09](W09/writer/turn-02/output.md) | Ready | Ready, compiler qualification | Complementary bot/channel/workspace-association near misses; null associations and access still need validation. |
| [W10](W10/writer/turn-02/output.md) | Ready | Ready | Answers exposed admin/owner flags; a false answer does not exclude a selected user. |

Within v4 reflection, no ready sketch becomes defective. Relative to the **previous
pipeline's final outputs**, W08 and W10 become ready, while W05 loses readiness;
the other cases retain their category. Those are different generated stories on
the same assignments, not edits to the old outputs. W03 also starts weaker than its
old counterpart but reflection repairs it.

## Remaining defects and what the recorded reasoning shows

**W02: the condition inventory can conceal a conjunction.** The request names a
budget-freeze announcement in #finance. Nora reacts to an office-relocation
announcement in #general, changing both topic and location. The audit packages
“budget-freeze announcement in #finance” into one message condition, calls Nora a
single-failure negative and stops. Its [recorded reasoning](W02/writer/turn-02/thinking.txt)
checks unique selection but does not separately check these two conditions.
The task's core unique answer is coherent; the decoy construction is weaker than
required. A condition-to-row mapping helps only when the conditions are decomposed
at the right level.

**W04: a semantic judgment remains unsupported.** “Launch checklist for marketing
site copy” can be a rollout checklist. Nothing in the request limits rollout to
engineering or a particular channel. Both the [audit](W04/writer/turn-02/output.md)
and [recorded reasoning](W04/writer/turn-02/thinking.txt) simply accept the narrower
interpretation. That makes the claimed absence unsafe. The first two rows also
repeat the same message description without clear distinct-root labels. This is
not evidence of a reasoning loop; it is a confident semantic miss.

**W05: access is substituted for selection.** A private onboarding channel with
six members still satisfies the written request. The author adds “public” to its
own condition line and then excludes that channel as undiscoverable. The capability
brief says public channels can be discovered and access can be arranged; it does
not make private matches cease to exist. Reflection fixes the malformed count row
but replaces it with an inaccessible other-workspace row. That replacement removes
one inconsistency while adding complexity that does not challenge the stated
onboarding/count criteria. See [output](W05/writer/turn-02/output.md) and
[recorded reasoning](W05/writer/turn-02/thinking.txt). Capability guidance can be
misread as a selection boundary; this case exposes that risk.

**W07: ambiguity does not remove the specified first-name condition.** The two
Jordan alternatives are coherent and produce different removals. A non-Jordan
person satisfying the other criteria would still be a useful required negative.
The [recorded reasoning](W07/writer/turn-02/thinking.txt) instead treats preserving
the first name across every negative as protecting the ambiguity. The missing
information is the surname; the supplied first name remains a condition. W03 fixes
the analogous omission, so the procedure is understood inconsistently.

These diagnoses use the reasoning summaries actually exposed by Bedrock, not an
assumption of complete access to internal computation. All twenty calls ended
normally. The repeated final defects are verification misses, not output exhaustion.

## Quality and challenge potential

Eight requests now ask for writes (W01–W08); the two workspace-root cases use read
fallbacks. Most are short and consequential. W01's `raised_hands` wording is less
natural than an emoji or ordinary phrase, but is not a selection defect.

W01 and W08 contain strong competing emoji/reactor/binding evidence. W06 forces
the distinction between authors' memberships and messages' locations. W03 gives
two equally supported destinations and independent negatives. W10 gives different
observable answers for its selected users. These are useful challenge mechanisms,
not demonstrated solver failures.

W09's absence is more substantial than an empty relevant population: bots and
channel members exist, but the whole chain does not. Its final quality still depends
on exposing the required profile associations and making the missing association
realizable. The compiler must also check the full seed for extra matches in every
case. No sketch is being passed off as a validated environment.

The revision helps most with capabilities, shared-record consistency and choosing
consequential operations. It does not make self-reflection a dependable acceptance
gate. The next focused issue is concrete condition decomposition and checking each
negative against those conditions, including partial-name conditions in ambiguous
cases. Semantic boundary review remains necessary. This batch alone does not
justify restarting broad generation.

## Cost and verification

| Usage | First pass | Reflection | Combined |
|---|---:|---:|---:|
| Calls | 10 | 10 | 20 |
| Uncached input tokens | 9,267 | 38,947 | 48,214 |
| Output tokens, including thinking | 22,977 | 23,081 | 46,058 |
| Cache creation tokens | 6,624 | 0 | 6,624 |
| Cache read tokens | 59,616 | 66,240 | 125,856 |
| Estimated dollars | $0.4151808 | $0.4829280 | $0.8981088 |

These are our historical-rate estimates from native token counts, **not Bedrock
billed dollars**. All usage is present. Nineteen of twenty calls hit the shared
system cache; the first created it. First-pass output is longer than before, while
reflection output is shorter; combined estimated cost rises about 3.1%.

See [first-pass usage](reflection/initial_usage_summary.json),
[reflection usage](reflection/usage.json), [combined usage](usage_summary.json),
[native continuation manifest](reflection/manifest.json), and [verification](verification.json).
All ten histories preserve the exact original native assistant blocks and request
settings; original artifact hashes match. Twelve targeted unit tests pass. No
historical pilot artifacts were overwritten, and no incomplete attempt was replaced.
