# Slack downstream task specifications

Pre-execution rewrites of all 59 Slack prompts, guided by their existing obligation cards. Editable source: [analysis.json](analysis.json). See [rewriting and linking rules](README.md#downstream-task-specifications).

Line numbers identify specification lines, including conditions; they are not action counts. Indentation, conditions, and explicit sequencing words express workflow. Other line order does not impose execution order. Links describe each line's direct use of existing obligations, including source-dependent content; they do not inherit enclosing conditions or other workflow dependencies. Empty links do not mean an action is optional or already complete.

Both conditional branches remain in the specification. Cards and links retain the seed-specific obligation inventory. Underspecified and absent references remain as requested; no arbitrary target or recovery behavior is supplied.

<a id="slack_57"></a>
## #1 — slack_57

[Original prompt and evidence](report.md#slack_57) · [Obligation cards](cards.md#slack_57)

```text
 1: Send a 'hello' message to #general.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_57-o1) |

<a id="slack_58"></a>
## #2 — slack_58

[Original prompt and evidence](report.md#slack_58) · [Obligation cards](cards.md#slack_58)

```text
 1: Send John a DM saying 'Can we sync later?'
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_58-o1) |

<a id="slack_59"></a>
## #3 — slack_59

[Original prompt and evidence](report.md#slack_59) · [Obligation cards](cards.md#slack_59)

```text
 1: Send Artem and Hubert a group DM (a group conversation, not a channel) saying 'Hey, I've took a look at the presentation and I have some questions. Can you help me?'
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_59-o1), [O2](cards.md#slack_59-o2) |

<a id="slack_60"></a>
## #4 — slack_60

[Original prompt and evidence](report.md#slack_60) · [Obligation cards](cards.md#slack_60)

```text
 1: Create a new channel called 'rl-project'.
```

| Line | Direct obligation links |
|---|---|
| L1 | — |

<a id="slack_61"></a>
## #5 — slack_61

[Original prompt and evidence](report.md#slack_61) · [Obligation cards](cards.md#slack_61)

```text
 1: Add Morgan Stanley to #random.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_61-o1), [O2](cards.md#slack_61-o2) |

<a id="slack_62"></a>
## #6 — slack_62

[Original prompt and evidence](report.md#slack_62) · [Obligation cards](cards.md#slack_62)

```text
 1: Create a new channel called 'rl-project'.
 2: Then add Morgan Stanley to that new channel.
```

| Line | Direct obligation links |
|---|---|
| L1 | — |
| L2 | [O1](cards.md#slack_62-o1) |

<a id="slack_63"></a>
## #7 — slack_63

[Original prompt and evidence](report.md#slack_63) · [Obligation cards](cards.md#slack_63)

```text
 1: Remove John from #random.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_63-o1), [O2](cards.md#slack_63-o2) |

<a id="slack_64"></a>
## #8 — slack_64

[Original prompt and evidence](report.md#slack_64) · [Obligation cards](cards.md#slack_64)

```text
 1: Archive #growth.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_64-o1) |

<a id="slack_65"></a>
## #9 — slack_65

[Original prompt and evidence](report.md#slack_65) · [Obligation cards](cards.md#slack_65)

```text
 1: Reply 'Next monday.' to the most recent message in #general.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_65-o1) |

<a id="slack_66"></a>
## #10 — slack_66

[Original prompt and evidence](report.md#slack_66) · [Obligation cards](cards.md#slack_66)

```text
 1: Reply 'Next monday.' to the MCP deployment questions in #general.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_66-o1) |

<a id="slack_67"></a>
## #11 — slack_67

[Original prompt and evidence](report.md#slack_67) · [Obligation cards](cards.md#slack_67)

```text
 1: React with :thumbsup: to all lunch-question messages in #random, except the separately specified pizza-combo message.
 2: React with :thumbsdown: to the pizza-combo message in #random.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_67-o1) |
| L2 | [O2](cards.md#slack_67-o2) |

<a id="slack_68"></a>
## #12 — slack_68

[Original prompt and evidence](report.md#slack_68) · [Obligation cards](cards.md#slack_68)

```text
 1: React with :thumbsup: to the most recent posted message in #general.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_68-o1) |

<a id="slack_69"></a>
## #13 — slack_69

[Original prompt and evidence](report.md#slack_69) · [Obligation cards](cards.md#slack_69)

```text
 1: Change #general's topic to 'Weekly standup discussions'.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_69-o1) |

<a id="slack_70"></a>
## #14 — slack_70

[Original prompt and evidence](report.md#slack_70) · [Obligation cards](cards.md#slack_70)

```text
 1: Edit the message that says 'Hey team' to say 'Hello everyone'.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_70-o1) |

<a id="slack_71"></a>
## #15 — slack_71

[Original prompt and evidence](report.md#slack_71) · [Obligation cards](cards.md#slack_71)

```text
 1: Post to #general mentioning Artem with the text 'Please review the pull request'.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_71-o1), [O2](cards.md#slack_71-o2) |

<a id="slack_72"></a>
## #16 — slack_72

[Original prompt and evidence](report.md#slack_72) · [Obligation cards](cards.md#slack_72)

```text
 1: Send 'System maintenance tonight at 10pm' to both #general and #random.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_72-o1), [O2](cards.md#slack_72-o2) |

<a id="slack_73"></a>
## #17 — slack_73

[Original prompt and evidence](report.md#slack_73) · [Obligation cards](cards.md#slack_73)

```text
 1: Delete the message about the new feature that you posted in #general.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_73-o1) |

<a id="slack_74"></a>
## #18 — slack_74

[Original prompt and evidence](report.md#slack_74) · [Obligation cards](cards.md#slack_74)

```text
 1: Post every question from #random to #general, each as a separate message.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_74-o1), [O2](cards.md#slack_74-o2) |

<a id="slack_75"></a>
## #19 — slack_75

[Original prompt and evidence](report.md#slack_75) · [Obligation cards](cards.md#slack_75)

```text
 1: Combine all four messages in #engineering related to login issues into a single new DM to Hubert; preserve the original messages' meaning.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_75-o1), [O2](cards.md#slack_75-o2) |

<a id="slack_76"></a>
## #20 — slack_76

[Original prompt and evidence](report.md#slack_76) · [Obligation cards](cards.md#slack_76)

```text
 1: Combine all six messages related to login issues and auth improvements into a single new DM to Hubert; preserve the original messages' meaning.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_76-o1), [O2](cards.md#slack_76-o2) |

<a id="slack_77"></a>
## #21 — slack_77

[Original prompt and evidence](report.md#slack_77) · [Obligation cards](cards.md#slack_77)

```text
 1: Edit your earlier #engineering message about auth issues that lacked details, adding the combined details from all six messages about login issues and auth improvements; preserve their original meaning and wording.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_77-o1), [O2](cards.md#slack_77-o2) |

<a id="slack_78"></a>
## #22 — slack_78

[Original prompt and evidence](report.md#slack_78) · [Obligation cards](cards.md#slack_78)

```text
 1: Edit your bad-joke reply to say 'I will make a proposal for auth improvements tommorow EOD'.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_78-o1) |

<a id="slack_79"></a>
## #23 — slack_79

[Original prompt and evidence](report.md#slack_79) · [Obligation cards](cards.md#slack_79)

```text
 1: Send a message to #general saying 'Attention' in bold and 'check logs' in italics, using Slack Block Kit rich_text blocks with style attributes bold:true and italic:true.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_79-o1) |

<a id="slack_80"></a>
## #24 — slack_80

[Original prompt and evidence](report.md#slack_80) · [Obligation cards](cards.md#slack_80)

```text
 1: Send a bulleted list to #random with the three items 'Bagels', 'Coffee', and 'Donuts', using Slack Block Kit rich_text blocks with rich_text_list (style:bullet).
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_80-o1) |

<a id="slack_81"></a>
## #25 — slack_81

[Original prompt and evidence](report.md#slack_81) · [Obligation cards](cards.md#slack_81)

```text
 1: Send a code snippet to #engineering containing `{"status": 200}`, using Slack Block Kit with a rich_text_preformatted element.
 2: Send a numbered list to #general with 'Phase 1' and 'Phase 2', using Slack Block Kit with rich_text_list (style:ordered).
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_81-o1) |
| L2 | [O2](cards.md#slack_81-o2) |

<a id="slack_82"></a>
## #26 — slack_82

[Original prompt and evidence](report.md#slack_82) · [Obligation cards](cards.md#slack_82)

```text
 1: Quote 'To be or not to be' in #random, using Slack Block Kit rich_text blocks with a rich_text_quote element.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_82-o1) |

<a id="slack_83"></a>
## #27 — slack_83

[Original prompt and evidence](report.md#slack_83) · [Obligation cards](cards.md#slack_83)

```text
 1: Send a table to #growth with headers 'Metric' and 'Value' and one data row 'DAU', '1500', using Slack Block Kit with a table block type.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_83-o1) |

<a id="slack_84"></a>
## #28 — slack_84

[Original prompt and evidence](report.md#slack_84) · [Obligation cards](cards.md#slack_84)

```text
 1: Send a markdown-formatted message to #engineering with the header 'Daily Report' and bold item '**All Systems Go**', using Slack Block Kit with a markdown block type.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_84-o1) |

<a id="slack_85"></a>
## #29 — slack_85

[Original prompt and evidence](report.md#slack_85) · [Obligation cards](cards.md#slack_85)

```text
 1: Mention Artem in #general, using Slack Block Kit rich_text blocks with a user element containing Artem's user ID.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_85-o1), [O2](cards.md#slack_85-o2) |

<a id="slack_86"></a>
## #30 — slack_86

[Original prompt and evidence](report.md#slack_86) · [Obligation cards](cards.md#slack_86)

```text
 1: Send the user who complained about 'captcha' in #general a DM saying 'I am looking into this.'
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_86-o1) |

<a id="slack_87"></a>
## #31 — slack_87

[Original prompt and evidence](report.md#slack_87) · [Obligation cards](cards.md#slack_87)

```text
 1: Create a new channel called 'auth-force'.
 2: Then invite everyone who has posted about 'login' or 'password' to that new channel.
```

| Line | Direct obligation links |
|---|---|
| L1 | — |
| L2 | [O1](cards.md#slack_87-o1) |

<a id="slack_88"></a>
## #32 — slack_88

[Original prompt and evidence](report.md#slack_88) · [Obligation cards](cards.md#slack_88)

```text
 1: If you find the user 'ElonMusk':
 2:     Invite him to #general.
 3: Else:
 4:     Inform me (Hubert) via Slack.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_88-o1) |
| L2 | [O1](cards.md#slack_88-o1) |
| L3 | — |
| L4 | [O2](cards.md#slack_88-o2) |

<a id="slack_89"></a>
## #33 — slack_89

[Original prompt and evidence](report.md#slack_89) · [Obligation cards](cards.md#slack_89)

```text
 1: Post the names of the admins of 'Test Workspace' in #random.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_89-o1), [O2](cards.md#slack_89-o2) |

<a id="slack_90"></a>
## #34 — slack_90

[Original prompt and evidence](report.md#slack_90) · [Obligation cards](cards.md#slack_90)

```text
 1: Invite the Morgan who is NOT an admin to #random.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_90-o1), [O2](cards.md#slack_90-o2) |

<a id="slack_91"></a>
## #35 — slack_91

[Original prompt and evidence](report.md#slack_91) · [Obligation cards](cards.md#slack_91)

```text
 1: Post 'Status update: Alpha is on track' to the alpha dev channel.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_91-o1) |

<a id="slack_92"></a>
## #36 — slack_92

[Original prompt and evidence](report.md#slack_92) · [Obligation cards](cards.md#slack_92)

```text
 1: Post a summary of the 'Gemini' discussion in #random to #engineering.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_92-o1), [O2](cards.md#slack_92-o2) |

<a id="slack_93"></a>
## #37 — slack_93

[Original prompt and evidence](report.md#slack_93) · [Obligation cards](cards.md#slack_93)

```text
 1: If the discussion in #growth establishes that the team decided to double down on Reddit:
 2:     React with :rocket: to the message proposing it.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_93-o1) |
| L2 | [O1](cards.md#slack_93-o1) |

<a id="slack_94"></a>
## #38 — slack_94

[Original prompt and evidence](report.md#slack_94) · [Obligation cards](cards.md#slack_94)

```text
 1: First, identify channels relevant to our 24-hour global open-source hackathon across Lagos, Kyiv, Warsaw, and SF.
 2: Update #core-infra's topic to reflect that we're in hackathon mode.
 3: Post an update to the infrastructure team in #core-infra about our hackathon coordination status.
 4: Pull up Łukasz Kowalski's and Kenji Sato's profiles before I loop them in: confirm whether Łukasz is still our performance lead and check Kenji's role on the APAC growth side.
 5: Remove the outdated message I posted yesterday in one of the channels that had wrong timezone information.
 6: Catch me up on recent discussions in #project-alpha-dev.
 7: Verify who's currently in #frontend; we might need to add people later.
 8: When you find important messages about the hackathon prep:
 9:     Give those messages a thumbs up to show we've seen them.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_94-o1) |
| L2 | [O2](cards.md#slack_94-o2) |
| L3 | [O2](cards.md#slack_94-o2) |
| L4 | [O3](cards.md#slack_94-o3), [O4](cards.md#slack_94-o4) |
| L5 | [O5](cards.md#slack_94-o5) |
| L6 | [O6](cards.md#slack_94-o6) |
| L7 | [O7](cards.md#slack_94-o7) |
| L8 | [O8](cards.md#slack_94-o8) |
| L9 | [O8](cards.md#slack_94-o8) |

<a id="slack_95"></a>
## #39 — slack_95

[Original prompt and evidence](report.md#slack_95) · [Obligation cards](cards.md#slack_95)

```text
 1: First, identify channels that might be relevant to our combined Diwali–Thanksgiving potluck celebration.
 2: Catch me up on recent discussions in #core-infra so we don't step on ongoing conversations.
 3: Tell me who's on our team so I can decide whom to involve based on their backgrounds and expertise.
 4: Once you have that context, update the topics of #core-infra, #project-alpha, and #growth to reflect planning the potluck celebration.
 5: Then post an announcement in #project-alpha about the event.
 6: Check who's currently in #growth so I can verify that the right people are included.
 7: Open a DM with Kenji Sato so I can coordinate timing separately with him given APAC schedules.
 8: Update my old message about the event that has wrong details with the correct information.
 9: Delete the outdated announcement from last week that's no longer relevant.
10: Finally, react to Priya's message about bringing samosas to show I've seen it.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_95-o1) |
| L2 | [O2](cards.md#slack_95-o2) |
| L3 | [O3](cards.md#slack_95-o3) |
| L4 | [O2](cards.md#slack_95-o2), [O4](cards.md#slack_95-o4), [O5](cards.md#slack_95-o5) |
| L5 | [O4](cards.md#slack_95-o4) |
| L6 | [O6](cards.md#slack_95-o6) |
| L7 | [O7](cards.md#slack_95-o7) |
| L8 | [O8](cards.md#slack_95-o8) |
| L9 | [O9](cards.md#slack_95-o9) |
| L10 | [O10](cards.md#slack_95-o10) |

<a id="slack_96"></a>
## #40 — slack_96

[Original prompt and evidence](report.md#slack_96) · [Obligation cards](cards.md#slack_96)

```text
 1: First, identify who on our team has the expertise for the Lunar New Year product launch targeting APAC markets, with culturally sensitive timing and messaging.
 2: Reach out directly to our frontend person about UI elements that need adapting for the launch.
 3: Connect separately with our engineering lead about the technical rollout schedule.
 4: Check who's currently in #project-alpha-dev to keep launch discussions focused; we may need to streamline membership.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_96-o1) |
| L2 | [O2](cards.md#slack_96-o2) |
| L3 | [O3](cards.md#slack_96-o3) |
| L4 | [O4](cards.md#slack_96-o4) |

<a id="slack_97"></a>
## #41 — slack_97

[Original prompt and evidence](report.md#slack_97) · [Obligation cards](cards.md#slack_97)

```text
 1: First, tell me who's currently in #random and list everyone on the team for our Afrobeats festival streaming workspace cleanup.
 2: Verify Robert Chen's role, since he's supposed to be leading engineering.
 3: Find our CDN-related conversations about the content delivery setup for me to reference.
 4: Catch me up on recent discussions in #project-alpha.
 5: Once you have that context, remove Artem Bogdanov from #project-alpha-dev.
 6: Also, after gathering that context, remove Hubert Marek from #core-infra; he and Artem have moved to different workstreams.
 7: Post an update to #core-infra about our streaming infrastructure progress.
 8: Update #core-infra's topic to reflect our virtual festival focus.
 9: Delete the outdated message I posted earlier.
10: Correct the information in my previous update that needs fixing.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_97-o1), [O2](cards.md#slack_97-o2) |
| L2 | [O3](cards.md#slack_97-o3) |
| L3 | [O4](cards.md#slack_97-o4) |
| L4 | [O5](cards.md#slack_97-o5) |
| L5 | [O6](cards.md#slack_97-o6), [O7](cards.md#slack_97-o7) |
| L6 | [O8](cards.md#slack_97-o8), [O9](cards.md#slack_97-o9) |
| L7 | [O9](cards.md#slack_97-o9) |
| L8 | [O9](cards.md#slack_97-o9) |
| L9 | [O10](cards.md#slack_97-o10) |
| L10 | [O11](cards.md#slack_97-o11) |

<a id="slack_98"></a>
## #42 — slack_98

[Original prompt and evidence](report.md#slack_98) · [Obligation cards](cards.md#slack_98)

```text
 1: First, check Sophie Dubois's and Olena Petrenko's profiles so I have their roles right when introducing them at today's Polish-Ukrainian 'Pierogi vs Varenyky Debug Session'; they're bringing food for the break.
 2: Catch me up on what's been happening in #engineering, including the potentially relevant login issues discussed there.
 3: Find channels that might already be discussing 'this topic'.
 4: If there isn't a dedicated space yet:
 5:     Create a new channel for our pierogi-vs-varenyky session.
 6: Post a heads-up in #core-infra about our debugging plans.
 7: React with a thumbs up to the great message Aisha left earlier that I have in mind.
 8: Remove the person who's no longer on the team from the project channel I mean.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_98-o1), [O2](cards.md#slack_98-o2) |
| L2 | [O3](cards.md#slack_98-o3) |
| L3 | [O4](cards.md#slack_98-o4) |
| L4 | [O4](cards.md#slack_98-o4) |
| L5 | — |
| L6 | [O5](cards.md#slack_98-o5) |
| L7 | [O6](cards.md#slack_98-o6) |
| L8 | [O7](cards.md#slack_98-o7), [O8](cards.md#slack_98-o8) |

<a id="slack_99"></a>
## #43 — slack_99

[Original prompt and evidence](report.md#slack_99) · [Obligation cards](cards.md#slack_99)

```text
 1: Before getting started on our traditional tea ceremony exchange between the Tokyo and Paris offices, check recent discussions in #random, including lunch plans and Gemini as possible context for participation.
 2: Also, before getting started, review #growth's Reddit strategy discussion for possible promotion of the cultural exchange.
 3: Then create a dedicated channel for the traditional tea ceremony planning initiative.
 4: Then set that channel's topic to clearly explain the initiative.
 5: Update the messages I posted earlier about the event with the corrected dates and details.
 6: Remove the one outdated message I sent that's no longer relevant.
 7: If you see the message where Priya or Mateo showed interest in participating:
 8:     Acknowledge that message with a reaction; do not add another reply to the thread.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_99-o1) |
| L2 | [O2](cards.md#slack_99-o2) |
| L3 | — |
| L4 | — |
| L5 | [O3](cards.md#slack_99-o3) |
| L6 | [O4](cards.md#slack_99-o4) |
| L7 | [O5](cards.md#slack_99-o5) |
| L8 | [O5](cards.md#slack_99-o5) |

<a id="slack_100"></a>
## #44 — slack_100

[Original prompt and evidence](report.md#slack_100) · [Obligation cards](cards.md#slack_100)

```text
 1: First, catch me up on #model-research and #core-infra so we can avoid planning our Lunar New Year product launch for APAC during technical instability.
 2: Confirm Kenji Sato's and Robert Chen's roles so I can verify that they're the right people to involve: Kenji should handle APAC growth and Robert should be our engineering lead.
 3: Once you have that context, create a dedicated channel for the Lunar New Year APAC product launch.
 4: Then set the new channel's topic to clearly reflect the initiative.
 5: Then post a summary of what you found in #model-research and #core-infra and about Kenji's and Robert's roles to #project-alpha-dev so the team is aligned.
 6: Update my earlier message about the launch timeline with the correct dates.
 7: If you judge anything in those two channel histories important and worth acknowledging:
 8:     Give whichever messages you judge worth acknowledging a thumbs up; no fixed number of reactions is required.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_100-o1), [O2](cards.md#slack_100-o2) |
| L2 | [O3](cards.md#slack_100-o3), [O4](cards.md#slack_100-o4) |
| L3 | — |
| L4 | — |
| L5 | [O1](cards.md#slack_100-o1), [O2](cards.md#slack_100-o2), [O3](cards.md#slack_100-o3), [O4](cards.md#slack_100-o4), [O5](cards.md#slack_100-o5) |
| L6 | [O6](cards.md#slack_100-o6) |
| L7 | [O7](cards.md#slack_100-o7) |
| L8 | [O7](cards.md#slack_100-o7) |

<a id="slack_101"></a>
## #45 — slack_101

[Original prompt and evidence](report.md#slack_101) · [Obligation cards](cards.md#slack_101)

```text
 1: First, update #engineering's topic to reflect our current focus on the Music Festival Tech Stack for the virtual Afrobeats festival streaming project.
 2: Find the earlier discussions about CDN solutions for me to reference for our streaming needs.
 3: Confirm Robert Chen's role, since he's supposed to lead engineering.
 4: Make sure Łukasz Kowalski is part of the conversation in our main coordination channel for the festival streaming project.
 5: Once you have gathered this information, post updates to #engineering, #frontend, and #general to align everyone on our festival streaming infrastructure plans.
 6: Check which available channels might be relevant to this project.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_101-o1) |
| L2 | [O2](cards.md#slack_101-o2) |
| L3 | [O3](cards.md#slack_101-o3) |
| L4 | [O4](cards.md#slack_101-o4), [O5](cards.md#slack_101-o5) |
| L5 | [O1](cards.md#slack_101-o1), [O6](cards.md#slack_101-o6), [O7](cards.md#slack_101-o7) |
| L6 | [O8](cards.md#slack_101-o8) |

<a id="slack_102"></a>
## #46 — slack_102

[Original prompt and evidence](report.md#slack_102) · [Obligation cards](cards.md#slack_102)

```text
 1: Before diving into planning our anime convention booth, catch me up on relevant recent discussions in #product-growth and #random.
 2: Find the conversations about badges for me.
 3: Remove the outdated messages about our old booth location because we've been reassigned to a different hall.
 4: Loop Olena Petrenko into the conversation for booth setup logistics.
 5: Reach out directly to John Doe about general booth coordination.
 6: Reach out separately to Priya Sharma about booth infrastructure, such as power and internet.
 7: Update the topics of #product-growth and #project-alpha-dev to reflect our focus on anime expo booth setup.
 8: Correct my earlier messages in which I posted the wrong setup times.
 9: Once you find the key planning message:
10:     Give that message a thumbs up to show we're aligned.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_102-o1), [O2](cards.md#slack_102-o2) |
| L2 | [O3](cards.md#slack_102-o3) |
| L3 | [O4](cards.md#slack_102-o4) |
| L4 | [O5](cards.md#slack_102-o5), [O6](cards.md#slack_102-o6) |
| L5 | [O7](cards.md#slack_102-o7) |
| L6 | [O8](cards.md#slack_102-o8) |
| L7 | [O1](cards.md#slack_102-o1), [O9](cards.md#slack_102-o9) |
| L8 | [O10](cards.md#slack_102-o10) |
| L9 | [O11](cards.md#slack_102-o11) |
| L10 | [O11](cards.md#slack_102-o11) |

<a id="slack_103"></a>
## #47 — slack_103

[Original prompt and evidence](report.md#slack_103) · [Obligation cards](cards.md#slack_103)

```text
 1: First, check existing channels relevant to our Cricket World Cup watch party across the India, UK, and Australia offices so we don't duplicate efforts.
 2: Create a dedicated channel for watch party coordination.
 3: Once it's set up, update the new channel's topic to explain what it's for.
 4: Reach out directly to Priya Sharma for help with the streaming infrastructure across offices.
 5: Show me the team roster so I can see who else might want to be involved.
 6: Correct my #general watch party message from 3pm PST to 3pm IST, since we're primarily coordinating with the India office.
 7: Delete my old message about booking a downtown venue, since that is no longer happening.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_103-o1) |
| L2 | — |
| L3 | — |
| L4 | [O2](cards.md#slack_103-o2) |
| L5 | [O3](cards.md#slack_103-o3) |
| L6 | [O4](cards.md#slack_103-o4) |
| L7 | [O5](cards.md#slack_103-o5) |

<a id="slack_104"></a>
## #48 — slack_104

[Original prompt and evidence](report.md#slack_104) · [Obligation cards](cards.md#slack_104)

```text
 1: Get me the full details of #engineering and check its current membership for a channel audit.
 2: Post the audit results to #general, showing #engineering's exact current member count as a number and the current members' names.
 3: After posting the audit, rename #engineering to 'engineering-backend'.
 4: Then post a follow-up in #general confirming the successful rename to 'engineering-backend'.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_104-o1), [O2](cards.md#slack_104-o2) |
| L2 | [O1](cards.md#slack_104-o1), [O2](cards.md#slack_104-o2), [O3](cards.md#slack_104-o3) |
| L3 | [O1](cards.md#slack_104-o1) |
| L4 | [O1](cards.md#slack_104-o1), [O3](cards.md#slack_104-o3) |

<a id="slack_105"></a>
## #49 — slack_105

[Original prompt and evidence](report.md#slack_105) · [Obligation cards](cards.md#slack_105)

```text
 1: Using Sophie's DM containing her implementation plan and timeline for the circuit-tracer rewrite in PyTorch for multi-GPU distribution, reply to Robert's question in the #engineering thread with her estimated completion date.
 2: After replying, add a checkmark reaction to the original thread message to mark it as addressed.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_105-o1), [O2](cards.md#slack_105-o2) |
| L2 | [O3](cards.md#slack_105-o3) |

<a id="slack_106"></a>
## #50 — slack_106

[Original prompt and evidence](report.md#slack_106) · [Obligation cards](cards.md#slack_106)

```text
 1: First, send me a DM to myself listing all channels I'm currently a member of as a numbered list with each channel's name and member count, for the end-of-Q4 workspace reorganization.
 2: Unarchive #old-project-q3 for Q1 planning.
 3: Then rename that channel to 'q1-planning-2026'.
 4: Set that revived channel's topic to 'Q1 2026 Planning - Americas Team'.
 5: Remove every member of #project-alpha-dev whose profile timezone does NOT start with 'America/'.
 6: Remove my existing 👀 reaction on the circuit-tracer thread in #engineering.
 7: Join #product-growth.
 8: Finally, after the membership cleanup and channel rename, post a Q1 kickoff message in the newly renamed channel listing the names and timezones of the Americas members who remain in #project-alpha-dev.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_106-o1) |
| L2 | [O2](cards.md#slack_106-o2) |
| L3 | [O2](cards.md#slack_106-o2) |
| L4 | [O2](cards.md#slack_106-o2) |
| L5 | [O3](cards.md#slack_106-o3), [O4](cards.md#slack_106-o4) |
| L6 | [O5](cards.md#slack_106-o5) |
| L7 | [O6](cards.md#slack_106-o6) |
| L8 | [O2](cards.md#slack_106-o2), [O3](cards.md#slack_106-o3), [O7](cards.md#slack_106-o7) |

<a id="slack_107"></a>
## #51 — slack_107

[Original prompt and evidence](report.md#slack_107) · [Obligation cards](cards.md#slack_107)

```text
 1: Create #fractal-forge for Kenji, Olena, and Priya's generative art project using the team's GPU infrastructure.
 2: Then set the new channel's topic to include 'GPU-meets-art'.
 3: Invite Kenji, Olena, and Priya to the new channel.
 4: Post an inaugural message in the new channel referencing the GPU-work discussions and circuit-tracer thread, using relevant messages written by Kenji, Olena, or Priya.
 5: React with :art: to the first message in #engineering that mentioned circuit-tracer.
 6: Set up a group DM with just Kenji and Olena so they can coordinate GPU scheduling privately.
 7: Rename the created channel from #fractal-forge to #silicon-dreams.
```

| Line | Direct obligation links |
|---|---|
| L1 | — |
| L2 | — |
| L3 | [O1](cards.md#slack_107-o1), [O2](cards.md#slack_107-o2), [O3](cards.md#slack_107-o3) |
| L4 | [O4](cards.md#slack_107-o4), [O5](cards.md#slack_107-o5) |
| L5 | [O6](cards.md#slack_107-o6) |
| L6 | [O1](cards.md#slack_107-o1), [O2](cards.md#slack_107-o2) |
| L7 | — |

<a id="slack_108"></a>
## #52 — slack_108

[Original prompt and evidence](report.md#slack_108) · [Obligation cards](cards.md#slack_108)

```text
 1: For Sophie and Mateo's 'Midnight Bazaar', find the workspace's food chatter and its participants, specifically the authors of messages containing the words 'food' or 'eat'.
 2: Revive the old archived channel nobody uses anymore and repurpose it as bazaar headquarters.
 3: Then set that channel's topic to capture the night-market vibe and include 'street food'.
 4: Write an opening post in that revived channel weaving in the food discussions you found.
 5: Remove Mateo from #project-alpha-dev because he wants out of its notifications.
 6: Edit that message about the espresso machine in #random to promote the bazaar.
 7: Delete the stale message in #random asking about ordering 'large pies'.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_108-o1), [O2](cards.md#slack_108-o2) |
| L2 | [O3](cards.md#slack_108-o3) |
| L3 | [O3](cards.md#slack_108-o3) |
| L4 | [O3](cards.md#slack_108-o3), [O8](cards.md#slack_108-o8) |
| L5 | [O4](cards.md#slack_108-o4), [O5](cards.md#slack_108-o5) |
| L6 | [O6](cards.md#slack_108-o6) |
| L7 | [O7](cards.md#slack_108-o7) |

<a id="slack_109"></a>
## #53 — slack_109

[Original prompt and evidence](report.md#slack_109) · [Obligation cards](cards.md#slack_109)

```text
 1: Create #phantom-frequencies for the collaborative radio drama 'Phantom Frequencies', where Aisha, Lukasz, Gabriel, Nick, and Priya each broadcast a story from their timezone.
 2: Then set the new channel's topic to fit the concept and include 'Phantom Frequencies'.
 3: Invite Aisha, Lukasz, Gabriel, Nick, and Priya to that new channel.
 4: Check Aisha's profile to confirm her timezone for the broadcast schedule.
 5: DM Aisha separately to ask about her episode's Lagos-blackout storyline.
 6: Write a first post in the new channel drawing on the workspace's transmission and signal discussions, including signal latency and CDN routing.
 7: Remove my existing :eyes: reaction on the circuit-tracer message in #engineering.
 8: Join #product-growth.
 9: Then check that channel for APAC launch discussion that could inform the drama's world-building.
10: Then leave #product-growth once you have what you need.
11: If you find a user in that chat whose name contains 'incognito':
12:     Ping that user to change their nickname to 'anything'.
13: Archive #project-alpha, which is basically just me and isn't being used.
```

| Line | Direct obligation links |
|---|---|
| L1 | — |
| L2 | — |
| L3 | [O1](cards.md#slack_109-o1), [O2](cards.md#slack_109-o2), [O3](cards.md#slack_109-o3), [O4](cards.md#slack_109-o4), [O5](cards.md#slack_109-o5) |
| L4 | [O1](cards.md#slack_109-o1) |
| L5 | [O1](cards.md#slack_109-o1) |
| L6 | [O6](cards.md#slack_109-o6) |
| L7 | [O7](cards.md#slack_109-o7) |
| L8 | [O8](cards.md#slack_109-o8) |
| L9 | [O8](cards.md#slack_109-o8) |
| L10 | [O8](cards.md#slack_109-o8) |
| L11 | [O9](cards.md#slack_109-o9) |
| L12 | [O9](cards.md#slack_109-o9) |
| L13 | [O10](cards.md#slack_109-o10) |

<a id="slack_110"></a>
## #54 — slack_110

[Original prompt and evidence](report.md#slack_110) · [Obligation cards](cards.md#slack_110)

```text
 1: Pull up details about #core-infra to assess whether its community would be a good match for cross-pollination with 'Cartography of Lost Rivers', our project mapping forgotten underground rivers.
 2: Count all messages across all chats mentioning the word 'supercomputer'.
 3: Then create #lost-rivers-cartography.
 4: Set the new channel's topic to describe mapping forgotten urban waterways.
 5: Invite Hubert, John, Omer, and Morgan (the one who participated in engineering discussions, not the other Morgan) to that channel.
 6: Write a project manifesto as the opening post in that channel, saying: '"supercomputer" mentioned <your_count> number of times across all of the chats', using the count of messages mentioning "supercomputer".
 7: DM that Morgan privately to ask whether they'd rather lead cartography or field exploration.
 8: Lastly, edit the intended message about infrastructure in #engineering to include a mention of the new project.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O5](cards.md#slack_110-o5) |
| L2 | [O6](cards.md#slack_110-o6) |
| L3 | — |
| L4 | — |
| L5 | [O1](cards.md#slack_110-o1), [O2](cards.md#slack_110-o2), [O3](cards.md#slack_110-o3), [O4](cards.md#slack_110-o4) |
| L6 | [O6](cards.md#slack_110-o6) |
| L7 | [O4](cards.md#slack_110-o4) |
| L8 | [O7](cards.md#slack_110-o7) |

<a id="slack_111"></a>
## #55 — slack_111

[Original prompt and evidence](report.md#slack_111) · [Obligation cards](cards.md#slack_111)

```text
 1: Pull up Kenji's, Priya's, Aisha's, Sophie's, Lukasz's, and Mateo's locale and timezone information for the 'Sunrise Relay' poetry chain, ordered from earliest sunrise to latest as each writes at dawn and passes the poem westward.
 2: Check recent discussions in #frontend for creative inspiration for the poem's theme.
 3: Create #sunrise-relay.
 4: Then set the new channel's topic to the relay schedule, showing each of those six people and their timezone in sunrise order, exactly as "<username>: <timezone>\n" for each person.
 5: Invite Kenji, Priya, Aisha, Sophie, Lukasz, and Mateo to the new channel.
 6: Post the full relay plan for those six participants as the opening message in the new channel.
 7: Then add a :sunrise: reaction to that schedule post.
 8: Remove Mateo from #model-research because its European-hours discussions don't suit his Pacific time.
 9: Rename the created channel from #sunrise-relay to #dawn-chorus, reflecting the group's choice of birdsong at first light as the poem's theme.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_111-o1), [O2](cards.md#slack_111-o2), [O3](cards.md#slack_111-o3), [O4](cards.md#slack_111-o4), [O5](cards.md#slack_111-o5), [O6](cards.md#slack_111-o6) |
| L2 | [O7](cards.md#slack_111-o7) |
| L3 | — |
| L4 | [O1](cards.md#slack_111-o1), [O2](cards.md#slack_111-o2), [O3](cards.md#slack_111-o3), [O4](cards.md#slack_111-o4), [O5](cards.md#slack_111-o5), [O6](cards.md#slack_111-o6) |
| L5 | [O1](cards.md#slack_111-o1), [O2](cards.md#slack_111-o2), [O3](cards.md#slack_111-o3), [O4](cards.md#slack_111-o4), [O5](cards.md#slack_111-o5), [O6](cards.md#slack_111-o6) |
| L6 | [O1](cards.md#slack_111-o1), [O2](cards.md#slack_111-o2), [O3](cards.md#slack_111-o3), [O4](cards.md#slack_111-o4), [O5](cards.md#slack_111-o5), [O6](cards.md#slack_111-o6) |
| L7 | — |
| L8 | [O6](cards.md#slack_111-o6), [O8](cards.md#slack_111-o8) |
| L9 | — |

<a id="slack_112"></a>
## #56 — slack_112

[Original prompt and evidence](report.md#slack_112) · [Obligation cards](cards.md#slack_112)

```text
 1: First, give Hubert's quarterly 'Apiary Report' survey: how many channels the workspace has and which ones are active.
 2: Then read through what's been happening in #growth.
 3: Choose the single best message in #growth and react with :honey_pot:.
 4: Once you've reviewed #growth, post a Forager's Report in #random summarizing noteworthy conversation from #growth and containing the words 'FORAGERS REPORT'.
 5: Last, archive #project-alpha, described as empty and inactive.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_112-o1) |
| L2 | [O2](cards.md#slack_112-o2) |
| L3 | [O3](cards.md#slack_112-o3) |
| L4 | [O2](cards.md#slack_112-o2), [O4](cards.md#slack_112-o4) |
| L5 | [O5](cards.md#slack_112-o5) |

<a id="slack_113"></a>
## #57 — slack_113

[Original prompt and evidence](report.md#slack_113) · [Obligation cards](cards.md#slack_113)

```text
 1: Start by listing the workspace's users, classifying them as 'admin' or 'member', and counting how many of each there are for the coastal field survey.
 2: Send Omer the channel survey in alphabetic channel-name order, reporting the admin and member counts for each channel exactly as "Field Repoert 1: <channel_name>: [<admins_count>, <members_count>]".
 3: Then inspect the circuit-tracer thread in #engineering: count its replies exactly and note who left them.
 4: Remove that message about coordinating lunch plans in #random.
 5: Open a private conversation with whoever originally posted the circuit-tracer message in #engineering.
 6: Then send that author a field report in the private conversation, using the circuit-tracer reply count and repliers' names, exactly as "Field Report 2: [N] replies found under circuit-tracer in #engineering — organisms: [comma-separated names of repliers]".
```

| Line | Direct obligation links |
|---|---|
| L1 | [O2](cards.md#slack_113-o2) |
| L2 | [O1](cards.md#slack_113-o1), [O2](cards.md#slack_113-o2), [O3](cards.md#slack_113-o3) |
| L3 | [O4](cards.md#slack_113-o4) |
| L4 | [O5](cards.md#slack_113-o5) |
| L5 | [O6](cards.md#slack_113-o6) |
| L6 | [O4](cards.md#slack_113-o4), [O6](cards.md#slack_113-o6) |

<a id="slack_114"></a>
## #58 — slack_114

[Original prompt and evidence](report.md#slack_114) · [Obligation cards](cards.md#slack_114)

```text
 1: First, check which channels Nick belongs to and count them for the 'Palimpsest' workspace project.
 2: Then remove my existing :eyes: reaction on the circuit-tracer message in #engineering.
 3: Rename #project-alpha to #palimpsest-archive.
 4: Finally, post to #random exactly "PALIMPSEST COMPLETE: [N] channels found for Nick", replacing [N] with the number of channels Nick belongs to.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_114-o1) |
| L2 | [O2](cards.md#slack_114-o2) |
| L3 | [O3](cards.md#slack_114-o3) |
| L4 | [O1](cards.md#slack_114-o1), [O4](cards.md#slack_114-o4) |

<a id="slack_115"></a>
## #59 — slack_115

[Original prompt and evidence](report.md#slack_115) · [Obligation cards](cards.md#slack_115)

```text
 1: Tell me how many active private conversations I have.
 2: If I have fewer than seven active private conversations:
 3:     Create new conversations with eligible users one by one in alphabetic order, skipping users with whom I already have conversations, until I have seven.
 4: If I have more than seven active private conversations:
 5:     Remove conversations in alphabetic order of the users until I have exactly seven active private conversations.
```

| Line | Direct obligation links |
|---|---|
| L1 | [O1](cards.md#slack_115-o1) |
| L2 | [O1](cards.md#slack_115-o1) |
| L3 | [O1](cards.md#slack_115-o1), [O2](cards.md#slack_115-o2) |
| L4 | [O1](cards.md#slack_115-o1) |
| L5 | [O1](cards.md#slack_115-o1) |

