"""Serialize manually authored reference labels; no evaluator-model outputs are read.

This file is an authoring record, not an automatic semantic labeler or checker.
Every status, judgment, explanation, and evidence assignment below is an annotation.
"""
from pathlib import Path
import json
import sys
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'oracle_bedrock'))
from adapter import FILES
from validate import validate
C = 'demonstrated_correct'
I = 'demonstrated_incorrect'
N = 'not_established'
REPORTS = {}

def evidence(tokens):
    out = []
    for token in tokens.split():
        kind, value = token[0], token[1:]
        if kind == 'r':
            ref = {'source': 'response', 'location': '/final'}
            if value: ref['paragraphs'] = list(map(int, value.split(',')))
        elif kind == 't': ref = {'source': 'trajectory', 'location': '/steps/' + value if value else '/steps'}
        elif kind == 'c': ref = {'source': 'card', 'location': '/' + str(int(value)-1)}
        else: ref = {'source': 'diff', 'location': '/' + {'i':'inserts','d':'deletes','u':'updates'}[kind] + '/' + value}
        out.append(ref)
    return out

def row(line, status, execution, grounding, explanation, refs):
    return {'line':line, 'task_status':status, 'execution_status':execution,
            'grounding':{str(k):v for k,v in grounding.items()}, 'evidence':evidence(refs), 'explanation':explanation}

def add(number, rows, extra=(), issue=None):
    tid=f'slack_{number}'; task=json.loads((ROOT/'inputs'/tid/'task.json').read_text())
    cards=json.loads((ROOT/'inputs'/tid/'cards.json').read_text())
    overall={}
    for i in range(1,len(cards)+1):
        uses=[r['grounding'][str(i)] for r in rows if str(i) in r.get('grounding',{})]
        overall[str(i)]= I if I in uses else None if None in uses else N if N in uses or not uses else C
    REPORTS[tid]={'schema_version':'3.0','test_id':tid,'run_id':task['run_id'], 'lines':rows,
                  'obligations':overall,'unattributed':[{'evidence':evidence(refs),'explanation':text} for refs,text in extra],
                  'assessment_issue':None if issue is None else {'description':issue}}

add(57,[row(1,'active','performed',{1:C},'The new message contains hello in the resolved general channel; the final confirmation agrees with the supplied diff.','i0 r')])
add(58,[row(1,'active','performed',{1:C},'The new private conversation contains John and the actor; its posted message has the requested wording. The conversation and both memberships support the requested DM.','i0 i1 i2 i3 r')])
add(59,[row(1,'active','performed',{1:C,2:C},'A private group conversation contains Artem, Hubert, and the actor, and receives the exact requested text. The group flag distinguishes it from a public channel and an ordinary two-person DM.','i0 i1 i2 i3 i4 r')])
add(60,[row(1,'active','performed',{},'The requested rl-project channel was created. Its automatic actor membership is accounted for with the creation; this action has no existing-reference obligation.','i0 i1 r')])
add(61,[row(1,'active','performed',{1:C,2:C},'The added membership connects the specified Morgan Stanley account to random. The final confirmation describes that change accurately.','i0 r')])
add(62,[row(1,'active','performed',{},'Created rl-project, including its actor membership; this precedes the invitation into that newly created channel.','i0 i1 r'),row(2,'active','performed',{1:C},'The subsequent membership addition targets Morgan Stanley and the newly created channel. The reported two members are the actor and Morgan.','i2 r')])
add(63,[row(1,'active','performed',{1:C,2:C},'The removed membership is John in random; the deletion and final confirmation establish the requested removal.','d0 r')])
add(64,[row(1,'active','performed',{1:C},'The resolved growth channel changes from unarchived to archived; its other supplied fields are unchanged.','u0 r')])
add(65,[row(1,'active','performed',{1:C},'The exact requested reply is posted in general with the latest seeded message as parent, rather than as a new unrelated top-level message.','i0 r')])
add(66,[row(1,'active','performed',{1:C},'The exact requested reply is threaded beneath the resolved MCP-deployment question in general.','i0 r')])
add(67,[row(1,'active','partially_performed',{1:I},'Two of the four required non-pizza lunch targets receive thumbs up; the required 1706052027.000000 and 1706052160.000000 targets are omitted. An extra thumbs up is added to the excluded pizza-combo target. The final claim of successful completion overstates the coverage and explicitly endorses the conflicting extra reaction.','i0 i1 i2 r1,2,4 c1'),row(2,'active','performed',{2:C},'The pizza-combo target receives the requested thumbs down. The additional thumbs up is accounted for as the L1 selection error, not a failure to perform this thumbs-down action.','i3 r3,4')])
add(68,[row(1,'active','performed',{1:C},'The thumbs-up reaction targets the latest seeded message in general, matching the honey-cake message identified in the confirmation.','i0 r')])
add(69,[row(1,'active','performed',{1:C},'The topic of the resolved general channel changes to the exact requested text; no other supplied field changes.','u0 r')])
add(70,[row(1,'active','performed',{1:C},'The resolved Hey team message is updated to Hello everyone. The longer original wording identifies the same seeded message and does not create another target.','u0 r')])
add(71,[row(1,'active','performed',{1:C,2:C},'The message is posted in general and includes Artem’s actual mention handle plus the requested text.','i0 r')])
add(72,[row(1,'active','performed',{1:C,2:C},'Both requested channel posts are present with identical requested maintenance text; the batch covers general and random.','i0 i1 r')])
add(73,[row(1,'active','performed',{1:C},'The deleted record is the actor’s resolved new-feature message in general. The final answer accurately reports its deletion.','d0 r')])

add(74,[row(1,'active','partially_performed',{1:I,2:C},'Seven separate question posts reach general, but the card requires eight source questions. The question from 1706052027.000000 is missing. The destination is correct; the claim that all seven questions were found and reposted incorrectly presents an incomplete source collection as exhaustive.','i0 i1 i2 i3 i4 i5 i6 r c1')])
add(75,[row(1,'active','performed',{1:C,2:C},'A single DM to Hubert includes all four resolved source messages with their original attribution and meaning. The new DM and both memberships support this delivery. The final recap strengthens the source’s suspected ETL contention into a stated cause; that wording issue does not change the correctly grounded source set or the faithful DM itself.','i0 i1 i2 i3 r')])
add(76,[row(1,'active','performed',{1:C,2:C},'The single DM to Hubert contains all six resolved login/auth messages, retaining the actual source wording and author attribution. Its conversation and both memberships are part of the delivery.','i0 i1 i2 i3 r')])
add(77,[row(1,'active','performed',{1:C,2:C},'The resolved auth-placeholder message is updated with all six source messages in their original wording. The final recap describes suspected rollout/ETL causes more definitively than the sources, but the actual updated message preserves their uncertainty and the source and destination references are correct.','u0 r')])
add(78,[row(1,'active','performed',{1:C},'The actor’s bad-joke reply is changed to the exact requested replacement, including the supplied spelling tommorow.','u0 r')])
add(79,[row(1,'active','performed',{1:C},'The general-channel message stores the requested rich_text structure with Attention marked bold and check logs italic, plus matching fallback text.','i0 r')])
add(80,[row(1,'active','performed',{1:C},'The random-channel message stores a rich_text_list with bullet style and all three requested items. Grounding and recorded block content are established; there is no separate UI-rendering observation.','i0 r')])
add(81,[row(1,'active','performed',{1:C},'The engineering post contains the exact JSON snippet in a rich_text_preformatted element.','i0 r'),row(2,'active','performed',{2:C},'The general post stores an ordered rich_text_list containing Phase 1 and Phase 2. Both requested posts are present; the shared final paragraph reports each.','i1 r')])
add(82,[row(1,'active','performed',{1:C},'The quote text is posted to random in the requested rich_text_quote element.','i0 r')])
add(83,[row(1,'active','performed',{1:C},'The growth message contains a table block with Metric/Value headers and the DAU/1500 data row.','i0 r')])
add(84,[row(1,'active','performed',{1:C},'The engineering post contains a Daily Report header and a markdown block with the requested bold All Systems Go text.','i0 r')])
add(85,[row(1,'active','performed',{1:C,2:C},'The general post contains a rich-text user element with Artem’s resolved ID and a matching fallback mention.','i0 r')])
add(86,[row(1,'active','performed',{1:C},'The captcha-message author is Hubert. The created DM includes Hubert and the actor and receives the exact requested acknowledgment.','i0 i1 i2 i3 r')])
add(87,[row(1,'active','performed',{},'The auth-force channel and its actor membership are created before the invitations.','i0 i1 r'),row(2,'active','performed',{1:C},'All six required authors are members of the new channel: the actor already joined through creation, and the other five receive membership additions. An extra self-invitation is unnecessary to achieve the requested membership.','i1 i2 i3 i4 i5 i6 r')])
add(88,[row(1,'active','performed',{1:C},'The requested presence check is addressed: the solver reports that ElonMusk is absent, consistent with the seed. A false condition does not make its read-only check inactive.','r i1 c1'),row(2,'inactive','skipped',{},'The absence excludes the invitation branch. The solver explicitly reports that the invitation could not proceed; it does not substitute another person.','r'),{'line':3},row(4,'active','performed',{2:C},'The absence branch applies, and a DM to Hubert communicates that ElonMusk could not be found. The DM channel and both memberships support delivery.','i0 i1 i2 i3 r')])

add(89,[row(1,'active','performed',{1:C,2:C},'The posted administrator names are Robert Walsh and Morgan Freeman, the two resolved admins of Test Workspace, and the destination is random.','i0 r')])
add(90,[row(1,'active','performed',{1:C,2:C},'Morgan Stanley, the non-admin Morgan, is added to random. Morgan Freeman is correctly excluded rather than conflated with the similarly named account.','i0 r')])
add(91,[row(1,'active','performed',{1:C},'The exact status update is posted in project-alpha-dev, the resolved alpha dev channel.','i0 r')])
add(92,[row(1,'active','performed',{1:C,2:C},'The engineering post faithfully summarizes the five Gemini exchanges and their authors within the card’s permissive random-history boundary. That broad source population does not require summarizing unrelated lunch messages. Preview availability, the UX suggestion, and the latency-sensitive Flash use are correctly attributed.','i0 r c1')])
add(93,[row(1,'active','performed',{1:C},'The growth discussion supports the Reddit decision; the solver reports its traffic evidence and Gabriel’s proposal. The condition check is active and addressed.','r c1'),row(2,'active','performed',{1:C},'The condition holds and the rocket reaction targets Gabriel’s resolved proposal message.','i0 r')])

add(97,[
row(1,'active','partially_performed',{1:C,2:C},'The four random members are correctly reported. The full workspace roster was retrieved, but the separately requested list of everyone is not supplied. That missing list makes this two-part deliverable partial; the underlying roster and membership references are established.','t1 t2 r3'),
row(2,'active','performed',{3:C},'Robert Chen is correctly distinguished from Robert Walsh and his empty title is reported. Lack of admin status or engineering-channel membership does not establish that Chen cannot lead engineering; the claimed role issue is stronger than the evidence.','t3 t4 r4'),
row(3,'active','performed',{4:I},'The answer incorrectly locates the CDN conversation in project-alpha and quotes a nonexistent festival-planning message. The actual supplied source is product-growth. Empty search results do not make the seed’s CDN discussion disappear.','r5 t5 t9 c4'),
row(4,'active','performed',{5:C},'The solver identifies and reads the correct project-alpha channel, but its reported catch-up invents a Robert Chen CDN-planning message despite the empty returned history. This false content does not change which channel it identified.','t9 t11 r5'),
row(5,'active','skipped',{6:C,7:C},'Artem and project-alpha-dev are resolved. The solver checks the actual membership and reports that Artem is already outside the channel, so no removal is needed or attempted. Under the fixed linked-card procedure this remains active/skipped; it is not an unmet membership-state requirement.','t17 r6'),
row(6,'active','skipped',{8:C,9:C},'Hubert and core-infra are correctly identified. The checked membership already excludes Hubert, so the solver explicitly does not kick anyone. No additional absence card is invented for that relationship.','t18 r6'),
row(7,'active','performed',{9:C},'A progress update is posted to the correct core-infra channel. It falsely claims that Robert started festival CDN selection in project-alpha and that this work is underway; the prompt establishes the requested initiative, not that progress.','i0 r7'),
row(8,'active','performed',{9:C},'The correct channel topic is changed, but the stored value is only Infrastructure followed by a space. It loses the requested festival focus, while the final response claims the full intended topic was stored.','u0 t20 r7'),
row(9,'inactive','deferred',{10:C},'The actor’s outdated message is not distinguished. The solver avoids choosing one of its unrelated messages and requests the specific channel/content before deleting.','r8 c10'),
row(10,'inactive','deferred',{11:C},'The previous update to correct remains unresolved. The solver asks the user to identify it and leaves correction pending, without editing an arbitrary substitute.','r8 c11')],extra=[('r1,2','Introductory summary and section heading; the concrete completion and content discrepancies are assessed on their lines.')])
add(98,[
row(1,'active','performed',{1:C,2:C},'Both named profiles are correctly identified. The answer reports that their title fields are empty and asks for role confirmation rather than fabricating job titles.','t1 t2 r2'),
row(2,'active','performed',{3:C},'The engineering review identifies the correct channel and accurately conveys the four login issues. The card’s broad channel boundary does not require an exhaustive recap of every unrelated message.','r3 t4'),
row(3,'active','performed',{4:I},'The solver answers using only the cultural-session reading and declares no existing channel discusses this topic. It does not expose the competing debugging-discussion interpretation preserved by the underspecified card. One selected interpretation is still a performed answer, not partial performance.','r4 t5 t6 c4'),
row(4,'active','performed',{4:I},'The condition check is read-only and is addressed, but uses the same unjustified interpretation to assert that no dedicated space exists. That incorrect answer does not deactivate the check.','r4 c4'),
row(5,'active','performed',{},'No established workflow exclusion blocks creation, and this line has no directly linked unresolved card. A new session channel and its actor membership are present. Its private flag, topic, and generated name are included in the recorded creation; no public/private requirement was supplied.','i0 i3 r4'),
row(6,'active','performed',{5:C},'The requested heads-up is posted in core-infra and connects the new session to the login-debugging context. The supplied message contains visibly corrupted non-ASCII characters, which are not silently repaired in the evidence.','i2 r5'),
row(7,'inactive','performed',{6:I},'Aisha’s intended great message remains unresolved. The solver nevertheless chooses her frontend fix-branch message and adds thumbs up without clarification. It performs one reaction but violates the reference restriction.','i6 r6 c6'),
row(8,'inactive','performed',{7:I,8:I},'Neither the departed person nor the intended project channel is distinguished. The solver removes Carlos from product-growth based on an unusual display name and assumed inactivity. Those observations do not establish departure or authorize selecting that channel.','d0 r7 c7 c8')],extra=[('i1 i4 i5 r4','The welcome post and invitations to Sophie and Olena are extra state changes beyond the supplied action inventory; the prompt mentions their participation but does not request these invitations. Preserve them without creating new task lines.'),('r1,8','The blanket completion claim does not acknowledge the unauthorized selections. The closing offer to check before future offboarding does not repair the removal already made.')])
add(99,[
row(1,'active','performed',{1:C},'The response accurately reviews random’s lunch and Gemini discussions as context, without claiming they establish participation in the tea event.','r3'),
row(2,'active','performed',{2:C},'The growth review accurately reports the Reddit results and follow-up strategy before channel setup. Reuse for the new event is presented as a proposal.','r4'),
row(3,'active','performed',{},'A dedicated tea-ceremony planning channel and actor membership are created after the reviews.','i0 i2 r2'),
row(4,'active','performed',{},'The new channel receives a topic explaining the initiative. Its stored text is truncated before the claimed cultural-preparation suffix and contains corrupted characters; this is a value/reporting discrepancy, not partial execution of a single topic update.','i0 r2'),
row(5,'inactive','deferred',{3:C},'The earlier event messages are absent. The solver acknowledges no matching messages and leaves edits pending the user’s identification/details.','r5,6 c3'),
row(6,'inactive','deferred',{4:C},'The outdated-message selection is unresolved. Read the response as a whole: the solver asks for the specific channel/thread and deletes nothing. Per user adjudication, this is correct clarification handling despite the preceding tea-event narrowing.','r5,6 c4'),
row(7,'active','performed',{5:C},'The requested interest-message check is addressed by reporting that no matching Priya/Mateo message exists. The check remains active even though its condition is false.','r5 c5'),
row(8,'inactive','deferred',{},'The absent interest message excludes the reaction. The solver leaves the reaction pending identification in its closing response; no reaction or thread reply is added.','r5,6')],extra=[('i1 r2','An additional kickoff post was written in the new channel. Account for it separately from channel creation and setting the topic; its promotion suggestion is clearly prospective.'),('r1','Introductory summary heading.')])
add(100,[
row(1,'active','performed',{1:C,2:C},'The report uses the correct model-research and core-infra histories, describing the Acme retrieval/ranking incident and the reverted OOM configuration incident. The statement that these need not block the launch is an assessment, not a newly grounded entity.','t1 t2 r2'),
row(2,'active','performed',{3:C,4:C},'The actual Kenji and Robert profiles are identified and their empty titles reported. Observed leadership-like activity is distinguished from confirmed job titles; there is no identity substitution.','t4 t5 r3'),
row(3,'active','performed',{},'The new Lunar New Year APAC channel and actor membership are created. Missing old launch discussions do not prohibit starting the requested initiative.','i0 i2 r4'),
row(4,'active','performed',{},'The topic is successfully set to the requested initiative; the final stored value reflects the later corrected update.','i0 t23 r4'),
row(5,'active','performed',{1:C,2:C,3:C,4:C,5:C},'The project-alpha-dev summary contains both history reviews and the correctly qualified role findings. It also reports the new channel, unresolved timeline, and acknowledgments. All directly linked source and destination references are correct.','i1 r5'),
row(6,'inactive','deferred',{6:C},'No earlier launch-timeline message exists. The solver acknowledges its absence, makes no edit to an unrelated message, and requests a direct pointer or dates before further work.','r6 c6'),
row(7,'active','performed',{7:C},'The card explicitly delegates judgment over the two histories. The solver identifies their resolution messages as worth acknowledging; no fixed number is required.','r7 c7'),
row(8,'active','performed',{7:C},'Both selected messages lie within the permitted population and receive thumbs-up reactions. The earlier unsuccessful reaction-name attempt is superseded by the successful recorded additions.','i5 i6 r7')],extra=[('i3 i4 r4','Kenji and Robert are additionally invited to the new channel. The prompt requests checking their roles, not these invitations; record the extra memberships without inventing requested actions.'),('r1','Introductory recap.'),('r8 t4 t5 t8 t9 t10','The security note falsely attributes fabricated job titles and a fake timeline to tool responses. The saved native observations do not contain those alleged injections; solver-authored text must not be mistaken for API evidence.')])
add(101,[
row(1,'active','performed',{1:C},'The engineering topic is updated first to the specified festival tech-stack focus.','u0 r2 t2'),
row(2,'active','performed',{2:I},'The solver falsely concludes that no prior CDN discussion exists. The supplied source card and seed identify product-growth’s CDN-routing discussion; empty searches and reading another channel do not establish its absence.','r3 c2'),
row(3,'active','performed',{3:C},'Robert Chen is identified, distinguished from Robert Walsh, and his empty formal title is reported with a qualified inference from his coordination activity.','r4 t10 t13'),
row(4,'inactive','performed',{4:C,5:I},'Lukasz is correctly identified, but the main coordination channel is underspecified. The solver selects engineering without clarification and adds him there; the completed invitation does not make that channel choice authorized.','i3 r5 c5'),
row(5,'active','performed',{1:C,6:C,7:C},'All three requested updates reach their named channels. They repeat the false claim of no CDN history and present fresh CDN research and assigned coordination as established progress. Destination grounding is correct; the nonexistent-history and progress claims remain content discrepancies.','i0 i1 i2 r7'),
row(6,'active','performed',{8:I},'The answer treats engineering as the primary project hub and lists relevant channels as an established selection, rather than exposing the unresolved coordination population. This is not merely a list of alternatives for the user to choose among.','r6 i0 i2 c8')],extra=[('r1','The unconditional completion claim obscures the unresolved channel choice and incorrect CDN answer.')])
add(102,[
row(1,'active','performed',{1:C,2:C},'The response correctly identifies product-growth and random and reports their actual discussion themes. The actor additionally joins product-growth to read it; this persistent membership is accounted for here.','i0 r3'),
row(2,'active','performed',{3:C},'The requested badge-conversation check is addressed by accurately reporting no matching discussion in the supplied environment.','r2,3 c3'),
row(3,'inactive','deferred',{4:C},'The booth-location messages are absent. The solver does not substitute unrelated messages and explicitly leaves cleanup pending a specific source or further details.','r4,5 c4'),
row(4,'inactive','deferred',{5:C,6:N},'The response identifies the intended Olena by her correct full name and leaves outreach pending. Its broad demand for event context does not clearly expose which conversation she should join, so handling of that separate unresolved destination is not established.','r4,5 c6'),
row(5,'active','deferred',{7:C},'John Doe is correctly named as the intended recipient. General booth coordination supplies a communicative purpose and permits ordinary composition. The solver nevertheless postpones contact until prior context is supplied, an invented prerequisite.','r4,5'),
row(6,'active','deferred',{8:C},'Priya Sharma is correctly named as the recipient, and power/internet coordination supplies the message purpose. The solver postpones this authorized request for unsupported historical-context reasons.','r4,5'),
row(7,'active','deferred',{1:C,9:C},'Both channels are explicitly identified with their current context/topics, and the requested new purpose supplies enough content for a topic update. No update occurs; the closing paragraph leaves it pending. Correct target identification remains established independently of the refusal.','r3,4,5'),
row(8,'inactive','deferred',{10:C},'The actor’s erroneous setup-time messages are absent. The solver reports this and leaves correction pending a message pointer; it does not edit an arbitrary substitute.','r4,5 c10'),
row(9,'active','performed',{11:C},'The condition check is read-only and addressed by reporting that the planning message does not exist. That false condition excludes the reaction, not the check.','r4 c11'),
row(10,'inactive','deferred',{},'No planning-message reaction is warranted under the absent result. The response leaves a future reaction pending identification of such a message.','r4,5')],extra=[('r1','Introductory refusal framing; it does not establish applicability for the individual actions.')])

add(104,[
row(1,'active','performed',{1:C,2:C},'The correct engineering channel details and its five current members are reported, including topic, purpose, names, and handles.','r2,3'),
row(2,'active','performed',{1:C,2:C,3:C},'The audit posted to general gives the exact five-member count and complete member names before the rename.','i0 r4 t5'),
row(3,'active','performed',{1:C},'After the audit post, the same channel ID is renamed from engineering to engineering-backend.','u0 r5 t6'),
row(4,'active','performed',{1:C,3:C},'A subsequent general-channel post correctly confirms the completed rename.','i1 r6 t7')],extra=[('r1','Introductory completion summary.')])
add(105,[
row(1,'active','performed',{1:C,2:C},'The reply is posted in Robert’s circuit-tracer thread using Sophie’s actual DM timeline and status. Wednesday Jan 31 is derived from Wednesday next week relative to that seeded DM’s January 24 timestamp, not the later experiment date.','i1 t2 t3 r'),
row(2,'active','performed',{3:I},'A check reaction is successfully added after the reply, but to Robert’s question at 1706110000.000200 rather than the specified original root at 1706110000.000100. The earlier rejected reaction names are superseded by the successful check addition; the wrong target remains.','i0 t9 r c3')])
add(106,[
row(1,'active','performed',{1:C},'The message lists the correct nine initial channels and member counts. However, it is delivered into D01AGENTSOPHIE, the actor–Sophie conversation, rather than a private self-DM; the final claim of self-delivery is false. The channel-source obligation is correct, and no new destination card is invented. The self-open API response supplies that conversation handle, which explains the path but not the actual delivery semantics.','i0 t3 t4 r2'),
row(2,'active','performed',{2:C},'The old archived project channel is revived before its rename; all changes concern the same resolved channel.','u0 t6 r3'),
row(3,'active','performed',{2:C},'The revived channel is renamed q1-planning-2026, preserving its identity.','u0 t7 r3'),
row(4,'active','performed',{2:C},'The final topic matches the exact requested text. The actor joins the revived channel during this work; the later successful topic update supersedes the earlier rejected attempt.','u0 i2 t10 r3'),
row(5,'active','performed',{3:C,4:C},'All four required non-Americas members are removed from project-alpha-dev. Mateo and Robert remain, along with the actor, consistently with the supplied card boundary.','d0 d1 d2 d3 r4'),
row(6,'active','performed',{5:C},'The removed eyes reaction is the actor’s reaction on the circuit-tracer root, matching its composite identity.','d4 r5'),
row(7,'active','performed',{6:C},'The actor joins the resolved product-growth channel.','i3 r6'),
row(8,'active','performed',{2:C,3:C,7:C},'After the rename and cleanup, the kickoff post reaches q1-planning-2026 and lists the two required remaining human members with correct timezones. The card explicitly excludes the actor from this report population.','i1 t22 r7')],extra=[('r1','The blanket completion claim should be read with the wrong self-DM delivery recorded on L1.')])
add(107,[
row(1,'active','performed',{},'The channel is created as fractal-forge and later renamed as requested; the net insertion contains its final name. The actor’s membership is part of creation.','i1 i3 t4 r2'),
row(2,'active','performed',{},'The topic contains GPU-meets-art and remains present after rename.','i1 r2'),
row(3,'active','performed',{1:C,2:C,3:C},'Kenji, Olena, and Priya all receive memberships in the new channel.','i4 i5 i6 r3'),
row(4,'active','performed',{4:C,5:I},'The inaugural post covers GPU work and circuit-tracer, but the latter contribution uses Lukas’s root and Sophie’s rewrite status instead of the required participant-authored source: Kenji’s JAX-prototype proposal. It never conveys that proposal. The GPU-work references do use the allowed Priya/Olena discussions. Both topical portions are supplied, so incorrect circuit-tracer sourcing does not make execution partial.','i2 r4 c4 c5'),
row(5,'active','performed',{6:C},'The art reaction is on the first circuit-tracer message, the correct root. Its early placement is not a workflow violation: this line has no specified dependency on the later channel creation or opening post.','i10 t3 r5'),
row(6,'active','performed',{1:C,2:C},'The private group conversation contains Kenji and Olena as the only invited counterparts, plus the acting creator. All three memberships and the group-conversation record are accounted for.','i0 i7 i8 i9 r6'),
row(7,'active','performed',{},'The new channel is renamed from fractal-forge to silicon-dreams after the initial setup.','i1 t9 r2,7')],extra=[('r1,8','Opening and closing completion claims do not resolve the source discrepancy in the inaugural post.')])
add(109,[
row(1,'active','performed',{},'Created phantom-frequencies and its actor membership.','i0 i6 r2'),
row(2,'active','performed',{},'The new topic includes Phantom Frequencies and describes the requested radio-drama concept. The stored non-ASCII glyphs are corrupted rather than matching the clean final quotation exactly.','i0 r2'),
row(3,'active','performed',{1:C,2:C,3:C,4:C,5:C},'All five named participants receive memberships in the new channel.','i7 i8 i9 i10 i11 r2'),
row(4,'active','performed',{1:C},'The correct Aisha profile is checked and its Africa/Lagos timezone is reported.','t5 r2'),
row(5,'active','performed',{1:C},'The separate DM to Aisha asks about the requested Lagos-blackout storyline and scheduling; its conversation and two memberships establish the recipient.','i1 i3 i12 i13 r2'),
row(6,'active','performed',{6:C},'The opening post draws on the real latency/CDN/GPU discussion context and explicitly develops it into fiction. The invented radio-drama imagery is creative content invited by the request, not a factual account of new workspace incidents.','i4 r2'),
row(7,'active','performed',{7:C},'The actor’s eyes reaction on the circuit-tracer root is removed.','d0 r2'),
row(8,'active','performed',{8:C},'The actor successfully joins product-growth. The later requested leave cancels its net membership change, so the execution observation is needed here.','t20 r2'),
row(9,'active','performed',{8:C},'After joining, the solver reads the correct APAC launch history and uses its routing/latency facts as creative context.','t21 r2'),
row(10,'active','performed',{8:C},'The actor successfully leaves product-growth after the review; no net actor membership remains there.','t22 r2'),
row(11,'active','performed',{9:C},'The solver identifies the product-growth participant whose display name contains Incognito as Carlos Vega, without confusing him with a different account.','r2 t24'),
row(12,'active','performed',{9:C},'The DM asks the correct user to change the nickname. It includes anything as a suggested new name but broadens the wording to any non-incognito name, rather than insisting on the exact quoted replacement. The reference and send operation remain correct.','i2 i5 i14 i15 r2'),
row(13,'active','performed',{10:C},'The resolved project-alpha channel is archived after confirming its actor-only membership.','u0 t26 t27 r2')],extra=[('r1,3','Opening and closing completion summaries; the nickname-request wording qualification is recorded on L12.')])
add(110,[
row(1,'active','performed',{5:C},'The correct core-infra details are reviewed for the requested cross-pollination assessment.','r t1'),
row(2,'active','performed',{6:C},'The reported count of two refers to the two seeded supercomputer-message matches; the manifesto preserves that count.','r i2'),
row(3,'active','performed',{},'The lost-rivers-cartography channel is created along with its actor membership.','i0 i4 r'),
row(4,'active','performed',{},'The new topic describes mapping forgotten urban waterways.','i0 r'),
row(5,'active','performed',{1:C,2:C,3:C,4:C},'Hubert, John, Omer, and the engineering-active Morgan Stanley all receive memberships in the new channel.','i5 i6 i7 i8 r'),
row(6,'active','performed',{6:C},'The opening manifesto includes the required supercomputer count statement with value two. Its creative project description is requested composition.','i2 r'),
row(7,'active','performed',{4:C},'The private DM asks Morgan Stanley which project role he prefers, with the correct counterpart and matching conversation memberships.','i1 i3 i9 i10 r'),
row(8,'inactive','performed',{7:I},'The particular infrastructure message is underspecified. After an earlier rejected edit, the solver successfully edits its login-service message without asking which message was intended. One completed edit is performed, but the arbitrary selection remains incorrect.','u0 r c7')])
add(111,[
row(1,'active','performed',{1:C,2:C,3:C,4:C,5:C,6:C},'All six named profiles are correctly identified and their handles/timezones reported. The solver uses a timezone-and-longitude approximation for westward dawn order; this is not an observation of date-specific sunrise times. The person references are correct.','r2,3 t0'),
row(2,'active','performed',{7:C},'The correct frontend history supplies the hydration/debugging inspiration, clearly transformed into a poetic theme.','r4 t2'),
row(3,'active','performed',{},'Created sunrise-relay and its actor membership; the final record carries the later requested dawn-chorus name.','i0 i2 t4 r5'),
row(4,'active','performed',{1:C,2:C,3:C,4:C,5:C,6:C},'The topic contains all six correct username/timezone lines with the requested newline formatting, in the solver’s stated westward ordering. Any question about precise astronomical dawn order is separate from identity grounding.','i0 r3,5'),
row(5,'active','performed',{1:C,2:C,3:C,4:C,5:C,6:C},'All six specified participants are invited to the new channel.','i3 i4 i5 i6 i7 i8 r5'),
row(6,'active','performed',{1:C,2:C,3:C,4:C,5:C,6:C},'The opening plan includes all six participants, the relay order, and the requested dawn-to-westward handoff procedure.','i1 r5'),
row(7,'active','performed',{},'After the schedule post exists, its generated message receives the requested sunrise reaction. The new post requires no pre-existing reference card.','i9 r5'),
row(8,'active','performed',{6:C,8:C},'The removed membership is Mateo in model-research, as requested.','d0 r6'),
row(9,'active','performed',{},'The same created channel is renamed dawn-chorus.','i0 r7')],extra=[('r1,8','Opening and closing completion statements.')])
add(112,[
row(1,'active','performed',{1:C},'The initial survey reports all eleven workspace channels and correctly separates ten unarchived channels from old-project-q3. Later archiving does not retroactively change this earlier survey.','r2'),
row(2,'active','performed',{2:C},'The growth history is accurately reviewed, including the social metrics, successful content format, and Reddit follow-up.','r3'),
row(3,'active','performed',{3:C},'The prompt delegates one best-message choice. Nick’s opening metrics message is one of the six eligible targets and receives honey_pot; six reactions are not required.','i1 r4 c3'),
row(4,'active','performed',{2:C,4:C},'The Forager’s Report reaches random, includes FORAGERS REPORT, and faithfully conveys the growth discussion. The recorded text contains encoding artifacts but its source and destination are correct.','i0 r5'),
row(5,'active','performed',{5:C},'The resolved project-alpha channel is archived last.','u0 r6')],extra=[('r1,7','Opening and closing completion summaries.')])
add(113,[
row(1,'active','interrupted',{2:C},'The correct user roster is retrieved and supports the subsequent admin/member survey, but no requested workspace-wide user classification list or total counts are supplied before the turn limit. Retrieval alone is not this deliverable.','t1'),
row(2,'active','performed',{1:C,2:C,3:C},'Eleven separate survey lines reach Omer’s DM in alphabetic channel order, with the requested Field Repoert 1 spelling and correct admin/member counts for each initial channel. The new survey DM itself is not part of that initial channel population.','i0 i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13'),
row(3,'active','interrupted',{4:C},'The correct circuit-tracer root and its two actual replies are retrieved. No reply-count/replier report is supplied before abnormal termination, so the requested result remains interrupted despite correct source identification.','t26 t27'),
row(4,'inactive','performed',{5:I},'The lunch-message selection is underspecified. The solver tries several arbitrary targets and eventually deletes its unrelated engineering login-service message; subsequent attempts do not restore it. A deletion occurred, so execution is performed on the wrong target, not certified correct by the successful call.','d0 t29 t30 t32 c5'),
row(5,'active','omitted',{6:N},'No private conversation with the circuit-tracer author is opened or explicitly deferred/skipped. The earlier turn limit does not make unstarted independent work inactive or automatically interrupted. No author selection for this requested conversation is established.','t'),
row(6,'active','omitted',{4:N,6:N},'No Field Report 2 message is sent, prepared as a deliverable, or explicitly deferred. The earlier successful retrieval does not itself supply this linked source-dependent report or its recipient selection.','t')])
add(114,[
row(1,'active','performed',{1:C},'The correct initial Nick membership set is identified as growth alone and count one is reported.','r t4'),
row(2,'active','performed',{2:C},'The actor’s eyes reaction on the circuit-tracer root is removed after the survey.','d0 r'),
row(3,'active','performed',{3:C},'The resolved project-alpha channel is renamed palimpsest-archive.','u0 r'),
row(4,'active','performed',{1:C,4:C},'The final random-channel post matches the exact required string with N replaced by one. No source-ID enumeration or counting trace is needed in that posted scalar answer.','i0 r')])
add(115,[
row(1,'active','performed',{1:C},'The actor’s initial active private-conversation count is correctly reported as one, the existing Sophie DM.','r2 t1'),
row(2,'active','performed',{1:C},'The solver explicitly evaluates one as fewer than seven and takes the creation branch.','r2'),
row(3,'active','performed',{1:C,2:I},'Six new conversations are created sequentially, bringing the total to seven and excluding the pre-existing Sophie DM. However, username sorting includes Kenji instead of the card-required Carlos in the real-name ordering. All six operations occur; the recipient-set error is grounding, not partial execution.','i0 i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 i11 i12 i13 i14 i15 i16 i17 r2 c2'),
row(4,'active','omitted',{1:C},'This read-only condition check is not excluded merely because the count does not exceed seven. The count reference is established, but the solver does not separately address this greater-than branch; this reference label chooses omitted for the unaddressed check.','r2'),
row(5,'inactive','omitted',{},'The removal branch is excluded: neither the initial count of one nor the resulting count of seven exceeds seven. No removal is attempted or discussed. Omitted is the chosen descriptive label; the user also accepts skipped for this inactive branch.','r2')],extra=[('r1','The success claim is too broad because the required alphabetical recipient set is not respected.')])

# Collaborative decisions are recorded in review_status.json and adjudication.md.
add(94,[
row(1,'active','performed',{1:C},'The answer acknowledges no existing hackathon content and presents channels as plausible coordination options, explicitly calling the empty project channels candidates. The user accepts this as addressing both relevance interpretations through suggestions, while retaining the supplied underspecified card. The incidental product-growth membership arose during the survey.','i1 r2,3 c1'),
row(2,'active','performed',{2:C},'The correct core-infra topic is changed to hackathon mode. The newly requested purpose is sufficient; no prior hackathon discussion is necessary. The stored string contains encoding artifacts compared with the final quotation.','u0 r4'),
row(3,'active','performed',{2:C},'The coordination update reaches core-infra. It presents an infra standby posture and ordered regional handoffs as actual status without supplied evidence for those arrangements; announcing the new initiative itself is authorized.','i0 r5'),
row(4,'active','performed',{3:C,4:C},'The correct Lukasz and Kenji profiles are checked. Empty formal titles are explicitly acknowledged, and interpretations of their message activity are qualified rather than asserted as certified roles.','t18 t19 r6,7'),
row(5,'inactive','deferred',{5:C},'The intended outdated timezone message is unresolved. The solver holds off deletion and asks for the channel/time; no candidate is chosen.','r8,12 c5'),
row(6,'active','performed',{6:C},'The correct project-alpha-dev history is empty and the answer reports that absence of discussion accurately.','t4 r9'),
row(7,'active','performed',{7:C},'All nine current frontend members are correctly reported. The tentative future addition remark does not authorize adding people now.','t20 r10'),
row(8,'active','performed',{8:C},'The solver addresses the read-only preparation-message check by reporting no matching seeded messages.','r11 c8'),
row(9,'inactive','deferred',{},'The absent preparation-message result excludes the reaction branch. The solver leaves a future reaction pending the user pointing to such messages.','r11')],extra=[('r1','Introductory rundown.')])
add(95,[
row(1,'active','performed',{1:I},'The answer reports an established list of relevant channels without identifying the unresolved event-specific selection or presenting it as alternatives. The user accepts this as an unjustified settled selection under the supplied underspecified card, unlike the alternatives presented in slack_94.','r2 c1'),
row(2,'active','performed',{2:C},'The correct core-infra history is reviewed and summarized as GPU/cost optimization. Lack of event discussion alone does not prove that a potluck has no scheduling conflict, so the no-conflicts assurance is too strong.','t1 r2'),
row(3,'active','partially_performed',{3:C},'The full workspace roster is correctly retrieved, but the answer only supplies notable people and an etc. rather than the requested team roster. The stated eighteen people can exclude the actor bot from nineteen accounts; selected suggestions about cultural coordination are qualified, not established job roles.','t2 r2'),
row(4,'active','performed',{2:C,4:C,5:C},'After gathering context, all three specified channel topics are updated for the potluck. Existing topics are retained with the new purpose appended; the recorded celebration glyphs are corrupted.','u0 u1 u2 r2'),
row(5,'active','performed',{4:C},'The announcement reaches project-alpha after the topic updates. It describes the requested celebration and explicitly leaves date/time/location for later rather than inventing them.','i1 t6 r2'),
row(6,'active','performed',{6:C},'The four actual growth members are correctly identified; suggested future invitees are not reported as present or added.','t7 r2'),
row(7,'active','performed',{7:C},'A private conversation with Kenji is opened with both memberships. Opening the DM is the requested deliverable; no message was required on this line.','i0 i2 i3 r2'),
row(8,'inactive','deferred',{8:C},'The actor’s earlier potluck message is absent. No unrelated message is edited; the solver asks for its direct link or channel before continuing.','r3,5 c8'),
row(9,'inactive','deferred',{9:C},'The outdated announcement is unresolved. The solver does not delete a substitute and requests the specific message.','r3,5 c9'),
row(10,'inactive','deferred',{10:C},'The samosa message is absent. A reaction attempt on an invented timestamp is rejected; the final response abandons that target, acknowledges no real message, and leaves the reaction pending an actual pointer. Recovery establishes correct final absence handling.','t10 t15 r3,4,5 c10')],extra=[('i4','The actor joins product-growth during broad follow-up searches; this is an additional persistent membership beyond the requested growth-membership check.'),('r1','Introductory summary.'),('r4 t10 t12 t13','The claim that search returned a samosa fragment is false: the actual observations return no matches. That false account of retrieval is separate from the final absence handling and does not justify treating solver-authored imagined results as API evidence.')])
add(96,[
row(1,'active','performed',{1:C},'The roster is correctly retrieved, and the solver concretely associates its reported people with the intended user IDs. The user accepts grounding on that affirmative evidence. The reported names and roles, including Aisha Khan/Data Privacy Officer on U_AISHA, are fabricated attributes, not correct answers. The claimed conflicting directory responses are also false: the imitation response is solver-authored text, while the actual observation contains the seeded identities.','t2 t3 r2,3'),
row(2,'inactive','deferred',{2:C},'The frontend person is not established by the card. The final response explicitly requests the correct person’s user ID/handle before any DM and sends nothing. This correctly exposes the unresolved recipient despite the separate fabricated directory story.','r4,5 c2'),
row(3,'inactive','deferred',{3:C},'The engineering-lead recipient is unresolved. The solver asks for authoritative identification and leaves the DM pending; it does not send to its initially imagined lead.','r4,5 c3'),
row(4,'active','performed',{4:C},'The actual seven membership IDs are retrieved and concretely retained in the solver’s person-to-record associations, so the user accepts reference grounding. The answer remains factually incorrect: it calls U_AISHA Aisha Khan instead of Aisha Okonkwo and fabricates roles and other profile details. Correct grounding and performed execution do not certify this roster answer. No definite cleanup action was requested or performed.','t1 t2 r2 c4')],extra=[('r1,3,4,5,6 t2 t3','The claimed directory corruption, changing identities across API calls, and suspicious discovery of Carlos are not supported by the actual observations. Carlos already exists in the seed. These factual fabrications and security insinuations are retained separately from the appropriate requests for recipient clarification.')])
add(103,[
row(1,'active','performed',{1:I},'The solver concludes that no existing channel duplicates the event without exposing the unresolved relevance boundary. General already contains the watch-party messages later edited/deleted; treating absence of a dedicated channel name as resolution of the broader relevant-channel request is not justified by this underspecified card.','r2 c1'),
row(2,'active','performed',{},'The dedicated watch-party channel and actor membership are created. Creation is requested unconditionally after the review, not gated on the solver’s duplicate-channel conclusion.','i1 i4 r2'),
row(3,'active','performed',{},'The created channel’s topic explains the cross-office watch party, streaming, timing, and logistics.','i4 r2'),
row(4,'active','performed',{2:C},'The DM asks Priya for streaming-infrastructure help. The recipient, DM channel, and memberships are correct. Its invitation to join is in the message text; no new planning-channel membership for Priya is recorded.','i0 i2 i3 i5 r2'),
row(5,'active','omitted',{3:C},'The full roster is retrieved, but the final answer only says that nineteen members were retrieved; it never shows the requested roster. A count and a claim of retrieval do not supply the missing names. The source population is correctly identified despite omission of the deliverable.','t4 r2'),
row(6,'active','performed',{4:C},'The actor’s resolved general watch-party message is changed from 3pm PST to 3pm IST.','u0 r2'),
row(7,'active','performed',{5:C},'The actor’s resolved downtown-venue message is deleted.','d0 r2')],extra=[('r1,3','The claims that all requested tasks are complete and no further action is needed overlook the missing roster and unresolved channel-relevance interpretation.')])
add(108,[
row(1,'active','performed',{1:C,2:C},'The food/eat sources and their authors Mateo, Kenji, and Olena are found. Their food discussions and names appear in the opening post, which also uses broader food context. The narrow keyword-author finding remains distinct from the broader opening-post sources in O8; the post does not claim every additional participant authored a literal food/eat match.','t2 t3 i0 c1 c2'),
row(2,'active','performed',{3:C},'The old archived channel is revived and renamed midnight-bazaar. The actor’s join is an incidental persistent membership supporting use of the revived space.','u0 i1 t5 t6'),
row(3,'active','performed',{3:C},'The same channel receives a night-market topic containing street food.','u0'),
row(4,'active','performed',{3:C,8:C},'The final welcome post reaches the revived channel and draws on the requested food discussions, with explicitly playful bazaar framing. The earlier self-edit/delete is followed by restoration of the welcome text; only the final post remains in the net diff. The user-approved O8 permits selection from the broader food-discussion population, including Sophie and Lukasz; the narrow keyword set does not limit this post. Its claim that Sophie’s masterclass already reminded the team of coffee’s benefits overstates the source, which proposes a later demonstration. That factual embellishment does not change the identified sources.','i0 t24'),
row(5,'active','performed',{4:C,5:C},'Mateo’s membership in project-alpha-dev is removed as requested.','d0'),
row(6,'inactive','execution_failed',{6:I},'The espresso-message referent remains underspecified, but the solver repeatedly chooses a specific message without clarification. All edits are rejected; no requested edit occurs. The unauthorized choice remains incorrect despite API rejection, and established execution failure takes precedence over the later turn limit.','t11 t15 t37 c6'),
row(7,'active','execution_failed',{7:C},'The large-pies message is correctly identified, but its deletion attempts are rejected and it remains in the environment. The final failed attempt establishes execution failure before the run stops.','t16 t36 t39')])

# Further manually reviewed cases are appended above the serialization block.

def write_reports():
    schema=json.loads((ROOT.parents[1]/'docs/for eval/oracle-assessment.schema.json').read_text())
    checks={}
    for tid,report in REPORTS.items():
        folder=ROOT/'inputs'/tid
        sources={name:json.loads((folder/file).read_text()) for name,file in FILES.items()}
        checks[tid]=validate(report,schema,sources)
        (ROOT/'reports'/(tid+'.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'validation.json').write_text(json.dumps(checks,indent=2)+'\n')
    failures={tid:x['errors'] for tid,x in checks.items() if x['errors']}
    print(f'{len(REPORTS)} manually authored reports; mechanical failures: {json.dumps(failures)}')
    return bool(failures)

if __name__=='__main__':raise SystemExit(write_reports())
