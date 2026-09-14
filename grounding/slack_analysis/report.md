# Slack grounding obligations

See [method and source policy](README.md). These are benchmark annotations, not measurements of agent behavior. Cards use the locked schema in [cards.md](cards.md).

59 tests; 197 task-expressed obligations: 168 resolved, 6 absent, 23 underspecified. Assertions fully cover 77, partially cover 34, and leave 86 unchecked.

Coverage concerns the grounded contribution in the final state or requested output; it never requires a trajectory or source provenance. Full coverage does not certify whole-task correctness. See [the focused coverage audit](coverage_audit.md). The denominator includes unresolved and absent obligations. Zero-obligation tasks have no coverage ratio.

| # | Test | Obligations | Resolved | Absent | Underspecified | Full | Partial | Unchecked |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | [slack_57](#slack_57) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 2 | [slack_58](#slack_58) | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 3 | [slack_59](#slack_59) | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 4 | [slack_60](#slack_60) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | [slack_61](#slack_61) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 6 | [slack_62](#slack_62) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 7 | [slack_63](#slack_63) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 8 | [slack_64](#slack_64) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 9 | [slack_65](#slack_65) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 10 | [slack_66](#slack_66) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 11 | [slack_67](#slack_67) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 12 | [slack_68](#slack_68) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 13 | [slack_69](#slack_69) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 14 | [slack_70](#slack_70) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 15 | [slack_71](#slack_71) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 16 | [slack_72](#slack_72) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 17 | [slack_73](#slack_73) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 18 | [slack_74](#slack_74) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 19 | [slack_75](#slack_75) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 20 | [slack_76](#slack_76) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 21 | [slack_77](#slack_77) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 22 | [slack_78](#slack_78) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 23 | [slack_79](#slack_79) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 24 | [slack_80](#slack_80) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 25 | [slack_81](#slack_81) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 26 | [slack_82](#slack_82) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 27 | [slack_83](#slack_83) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 28 | [slack_84](#slack_84) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 29 | [slack_85](#slack_85) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 30 | [slack_86](#slack_86) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 31 | [slack_87](#slack_87) | 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 32 | [slack_88](#slack_88) | 2 | 1 | 1 | 0 | 1 | 1 | 0 |
| 33 | [slack_89](#slack_89) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 34 | [slack_90](#slack_90) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 35 | [slack_91](#slack_91) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 36 | [slack_92](#slack_92) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 37 | [slack_93](#slack_93) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 38 | [slack_94](#slack_94) | 8 | 5 | 0 | 3 | 0 | 0 | 8 |
| 39 | [slack_95](#slack_95) | 10 | 6 | 1 | 3 | 0 | 0 | 10 |
| 40 | [slack_96](#slack_96) | 4 | 2 | 0 | 2 | 0 | 0 | 4 |
| 41 | [slack_97](#slack_97) | 11 | 9 | 0 | 2 | 0 | 0 | 11 |
| 42 | [slack_98](#slack_98) | 8 | 4 | 0 | 4 | 0 | 0 | 8 |
| 43 | [slack_99](#slack_99) | 5 | 2 | 0 | 3 | 0 | 0 | 5 |
| 44 | [slack_100](#slack_100) | 7 | 5 | 0 | 2 | 0 | 0 | 7 |
| 45 | [slack_101](#slack_101) | 8 | 6 | 0 | 2 | 0 | 0 | 8 |
| 46 | [slack_102](#slack_102) | 11 | 6 | 4 | 1 | 0 | 0 | 11 |
| 47 | [slack_103](#slack_103) | 5 | 4 | 0 | 1 | 2 | 0 | 3 |
| 48 | [slack_104](#slack_104) | 3 | 3 | 0 | 0 | 2 | 1 | 0 |
| 49 | [slack_105](#slack_105) | 3 | 3 | 0 | 0 | 2 | 1 | 0 |
| 50 | [slack_106](#slack_106) | 7 | 7 | 0 | 0 | 5 | 2 | 0 |
| 51 | [slack_107](#slack_107) | 6 | 6 | 0 | 0 | 4 | 2 | 0 |
| 52 | [slack_108](#slack_108) | 7 | 7 | 0 | 0 | 4 | 1 | 2 |
| 53 | [slack_109](#slack_109) | 10 | 10 | 0 | 0 | 3 | 5 | 2 |
| 54 | [slack_110](#slack_110) | 7 | 7 | 0 | 0 | 2 | 4 | 1 |
| 55 | [slack_111](#slack_111) | 8 | 8 | 0 | 0 | 2 | 5 | 1 |
| 56 | [slack_112](#slack_112) | 5 | 5 | 0 | 0 | 3 | 0 | 2 |
| 57 | [slack_113](#slack_113) | 6 | 6 | 0 | 0 | 3 | 3 | 0 |
| 58 | [slack_114](#slack_114) | 4 | 4 | 0 | 0 | 4 | 0 | 0 |
| 59 | [slack_115](#slack_115) | 2 | 2 | 0 | 0 | 0 | 2 | 0 |

<a id="slack_57"></a>
## #1 — slack_57

Send a 'hello' message to the general channel

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L1) · [Cards](cards.md#slack_57)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the general channel | resolved | `["C01ABCD1234"]` | yes | A1: Assertion 1 fixes the new message destination to C01ABCD1234. |

Boundary and selection notes:

- **1.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "hello"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_58"></a>
## #2 — slack_58

Send a DM to John saying 'Can we sync later?'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L2) · [Cards](cards.md#slack_58)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve John | resolved | `["U02JOHNDOE1"]` | no | A1, A2: The message author is the actor; neither assertion fixes the DM recipient to John. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to John Doe in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'John Doe'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "sync later"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_59"></a>
## #3 — slack_59

Send a DM (group conversation not channel) to Artem and Hubert saying 'Hey, I've took a look at the presentation and I have some questions. Can you help me?'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L3) · [Cards](cards.md#slack_59)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Artem | resolved | `["U02ARTEM23"]` | no | A1, A2: A group conversation and message are required, but no recipient identities are constrained. |
| 2. Resolve Hubert | resolved | `["U06HUBERT23"]` | no | A1, A2: A group conversation and message are required, but no recipient identities are constrained. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to Artem Bogdanov in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Artem Bogdanov'
- **2.** The prompt’s name resolves to Hubert Marek in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Hubert Marek'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "presentation and I have some questions"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_gc": {
        "eq": true
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_60"></a>
## #4 — slack_60

Create a new channel called 'rl-project'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L4) · [Cards](cards.md#slack_60)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| No existing-referent obligation | — | — | N/A | Creation of a new named entity only |

Boundary and selection notes:

- Zero grounding obligations: rl-project names a new channel, not an existing referent. Creation-name validation does not establish an existing-entity grounding obligation.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "channel_name": {
        "i_contains": "rl-project"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_61"></a>
## #5 — slack_61

Add Morgan Stanley to the 'random' channel

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L5) · [Cards](cards.md#slack_61)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Morgan Stanley | resolved | `["U05MORGAN23"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |
| 2. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to Morgan Stanley in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Morgan Stanley'
- **2.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U05MORGAN23"
      },
      "channel_id": {
        "eq": "C02EFGH5678"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_62"></a>
## #6 — slack_62

Create a new channel called 'rl-project' and add Morgan Stanley to it

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L6) · [Cards](cards.md#slack_62)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Morgan Stanley | resolved | `["U05MORGAN23"]` | yes | A2: Assertion 2 requires Morgan’s membership, but does not link it to the newly created channel. The user identity is covered; the new-channel relationship is outside existing-referent coverage. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to Morgan Stanley in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Morgan Stanley'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "channel_name": {
        "i_contains": "rl-project"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U05MORGAN23"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_63"></a>
## #7 — slack_63

Remove John from the #random channel

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L7) · [Cards](cards.md#slack_63)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve John | resolved | `["U02JOHNDOE1"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |
| 2. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to John Doe in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'John Doe'
- **2.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "user_id": {
        "eq": "U02JOHNDOE1"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_64"></a>
## #8 — slack_64

Archive the #growth channel

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L8) · [Cards](cards.md#slack_64)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #growth | resolved | `["C04MNOP3456"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #growth; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'growth'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": {
        "eq": "C04MNOP3456"
      }
    },
    "expected_changes": {
      "is_archived": {
        "to": true
      }
    }
  }
]
```

</details>

<a id="slack_65"></a>
## #9 — slack_65

Reply 'Next monday.' to the most recent message in #general

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L9) · [Cards](cards.md#slack_65)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the most recent message in #general | resolved | `["1706115500.000001"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve general by name; choose the maximum numeric message timestamp in its history.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "parent_id": {
        "eq": "1706115500.000001"
      },
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "Next monday"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_66"></a>
## #10 — slack_66

Reply 'Next monday.' to the to MCP deployment questions in #general

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L10) · [Cards](cards.md#slack_66)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the MCP deployment question in #general | resolved | `["1700173200.000456"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve general by name; select messages containing MCP and deployment.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "parent_id": {
        "eq": "1700173200.000456"
      },
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "Next monday"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_67"></a>
## #11 — slack_67

In #random, react with :thumbsup: to all messages that are questions about lunch, and react with :thumbsdown: to the message about piza combo

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L11) · [Cards](cards.md#slack_67)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve lunch-question messages in #random | resolved | `["1699572000.000789","1706052665.000000"]` | yes | A1, A2: Assertions 1, 2 constrain the resulting change to this seeded referent. |
| 2. Resolve the pizza-combo message in #random | resolved | `["1706051755.000000"]` | yes | A3: Assertions 3 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Permissive assertion-guided boundary: the two lunch-question targets are supported by their text. The separately described pizza-combo message is assigned to the other obligation; no exhaustive classification of all food questions is imposed. Selection: Within random, select a question about whether people want lunch or how shared lunch participation works.
- **2.** Within random, select content containing pizza combo.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1699572000.000789"
      },
      "reaction_type": {
        "eq": "thumbsup"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706052665.000000"
      },
      "reaction_type": {
        "eq": "thumbsup"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706051755.000000"
      },
      "reaction_type": {
        "eq": "thumbsdown"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_68"></a>
## #12 — slack_68

React with :thumbsup: to the most recent posted message in #general

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L12) · [Cards](cards.md#slack_68)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the most recent posted message in #general | resolved | `["1706115500.000001"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Within general, select the greatest numeric timestamp.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706115500.000001"
      },
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "reaction_type": {
        "eq": "thumbsup"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_69"></a>
## #13 — slack_69

Change the #general channel topic to 'Weekly standup discussions'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L13) · [Cards](cards.md#slack_69)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      }
    },
    "expected_changes": {
      "topic_text": {
        "to": {
          "contains": "Weekly standup"
        }
      }
    }
  }
]
```

</details>

<a id="slack_70"></a>
## #14 — slack_70

Find the message that says 'Hey team' and edit it to say 'Hello everyone'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L14) · [Cards](cards.md#slack_70)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the message saying Hey team | resolved | `["1699564800.000123"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Select content containing Hey team.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_id": {
        "eq": "1699564800.000123"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "Hello everyone"
        }
      }
    }
  }
]
```

</details>

<a id="slack_71"></a>
## #15 — slack_71

Post to #general mentioning Artem with text 'Please review the pull request'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L15) · [Cards](cards.md#slack_71)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |
| 2. Resolve Artem | resolved | `["U02ARTEM23"]` | yes | A1: Assertion 1 requires Artem’s encoded mention in the message text. |

Boundary and selection notes:

- **1.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'
- **2.** The prompt’s name resolves to Artem Bogdanov in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Artem Bogdanov'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "<@U02ARTEM23>"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_72"></a>
## #16 — slack_72

Send 'System maintenance tonight at 10pm' to both #general and #random

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L16) · [Cards](cards.md#slack_72)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |
| 2. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A2: Assertions 2 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'
- **2.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "message_text": {
        "contains": "maintenance"
      },
      "channel_id": {
        "eq": "C01ABCD1234"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "message_text": {
        "contains": "maintenance"
      },
      "channel_id": {
        "eq": "C02EFGH5678"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_73"></a>
## #17 — slack_73

Delete the message about new feature you posted in #general

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L17) · [Cards](cards.md#slack_73)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the actor’s new-feature message in #general | resolved | `["1699564800.000123"]` | yes | A1: The removal predicate’s channel and content identify the single seeded message; author is not explicitly checked but does not create another match in this seed. |

Boundary and selection notes:

- **1.** Within general, select the actor’s message about the new feature.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "removed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "new feature"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_74"></a>
## #18 — slack_74

Find all questions in #random and post each one to #general as separate messages.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L18) · [Cards](cards.md#slack_74)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve questions in #random for reposting | resolved | `["1700210000.000001","1700210180.000004","1706052160.000000","1706052665.000000"]` | partial | A1, A2, A3, A4: The four output keywords do not require the actual question contents: four keyword-only messages satisfy the text constraints without reposting the questions. Source IDs or retrieval evidence are unnecessary; missing source-derived question content is the outcome gap. |
| 2. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A1, A2, A3, A4: Assertions 1, 2, 3, 4 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The assertions select a permissive subset of question messages, as authorized for subjective mutation-source boundaries. Other lunch/pizza questions exist; this is an assertion-guided boundary, not a claim to include every question in the prompt’s broad wording. Selection: Within random, select question messages about Gemini, preview availability, garlic knots, or shared lunch.
- **2.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "Gemini"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "preview"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "garlic knots"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "shared lunch"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_75"></a>
## #19 — slack_75

Search for all messages (4 messages) in the #engineering channel related to login issues and combine them into a single new message as DM to Hubert. Do not change the meaning of the original messages just combine them.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L19) · [Cards](cards.md#slack_75)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the login-issue source messages | resolved | `["1699651200.000321","1699737600.000654","1699824000.000987","1699910400.000246"]` | partial | A4, A5, A6, A7: The output can contain the required issue fragments while omitting the reported symptoms, timings, and proposed improvements. That does not preserve the source messages’ meaning as requested. The defect is incomplete final content, not missing source IDs or evidence of reading the messages. |
| 2. Resolve Hubert | resolved | `["U06HUBERT23"]` | yes | A2: A membership addition for Hubert is required. Linking that membership to the message’s conversation is not enforced, but the described user identity is constrained. |

Boundary and selection notes:

- **1.** Prompt gives a concrete source count; the listed messages describe the requested login failures and improvements. Assertions corroborate their distinctive fragments. Selection: Select messages containing one of: 500 errors, invalid_grant, login rate limit, login endpoint, within engineering.
- **2.** The prompt’s name resolves to Hubert Marek in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Hubert Marek'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      },
      "channel_id": {
        "regex": "^D"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U06HUBERT23"
      },
      "channel_id": {
        "regex": "^D"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "channel_id": {
        "regex": "^D"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "channel_id": {
        "regex": "^D"
      },
      "message_text": {
        "contains": "500 errors"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "channel_id": {
        "regex": "^D"
      },
      "message_text": {
        "contains": "invalid_grant"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "channel_id": {
        "regex": "^D"
      },
      "message_text": {
        "contains": "login rate limit"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "channel_id": {
        "regex": "^D"
      },
      "message_text": {
        "contains": "login endpoint"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_76"></a>
## #20 — slack_76

Search for all messages (6 messages) related to login issues and auth improvments. Combine them into a single new message as DM to Hubert. Do not change the meaning of the original messages just combine them.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L20) · [Cards](cards.md#slack_76)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the login-issue and authentication-improvement source messages | resolved | `["1699651200.000321","1699737600.000654","1699824000.000987","1699910400.000246","1699996800.000777","1700083200.000888"]` | partial | A3, A4, A5, A6, A7, A8: The output can contain the required issue fragments while omitting the reported symptoms, timings, and proposed improvements. That does not preserve the source messages’ meaning as requested. The defect is incomplete final content, not missing source IDs or evidence of reading the messages. |
| 2. Resolve Hubert | resolved | `["U06HUBERT23"]` | yes | A2: A membership addition for Hubert is required. Linking that membership to the message’s conversation is not enforced, but the described user identity is constrained. |

Boundary and selection notes:

- **1.** Prompt gives a concrete source count; the listed messages describe the requested login failures and improvements. Assertions corroborate their distinctive fragments. Selection: Select messages containing one of: 500 errors, invalid_grant, login rate limit, login endpoint, empty password, captcha.
- **2.** The prompt’s name resolves to Hubert Marek in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Hubert Marek'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U06HUBERT23"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "500 errors"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "invalid_grant"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "login rate limit"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "login endpoint"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "captcha"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "empty password"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_77"></a>
## #21 — slack_77

Search for all messages (6 messages) related to login issues and auth improvments. Edit the message in the #engineering channel you sent before without details about issues and add the details about the issues and improvements. Do not change the meaning/ woring of the original messages just combine them.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L21) · [Cards](cards.md#slack_77)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the login-issue and authentication-improvement source messages | resolved | `["1699651200.000321","1699737600.000654","1699824000.000987","1699910400.000246","1699996800.000777","1700083200.000888"]` | partial | A1, A2, A3, A4, A5, A6: The output can contain the required issue fragments while omitting the reported symptoms, timings, and proposed improvements. That does not preserve the source messages’ meaning as requested. The defect is incomplete final content, not missing source IDs or evidence of reading the messages. |
| 2. Resolve the actor’s engineering placeholder about auth issues | resolved | `["1700143200.000999"]` | yes | A1, A2, A3, A4, A5, A6: Assertions 1, 2, 3, 4, 5, 6 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Prompt gives a concrete source count; the listed messages describe the requested login failures and improvements. Assertions corroborate their distinctive fragments. Selection: Select messages containing one of: 500 errors, invalid_grant, login rate limit, login endpoint, empty password, captcha.
- **2.** Select the actor’s engineering message whose text is I've noticed a few auth issues and potential improvements:.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_id": {
        "eq": "1700143200.000999"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "500 errors"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_id": {
        "eq": "1700143200.000999"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "invalid_grant"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_id": {
        "eq": "1700143200.000999"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "login rate limit"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_id": {
        "eq": "1700143200.000999"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "ogin endpoint"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_id": {
        "eq": "1700143200.000999"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "captcha"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_id": {
        "eq": "1700143200.000999"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "empty password"
        }
      }
    }
  }
]
```

</details>

<a id="slack_78"></a>
## #22 — slack_78

You've replied to one of the messages with a bad joke. Edit it, for 'I will make a proposal for auth improvements tommorow EOD'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L22) · [Cards](cards.md#slack_78)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the actor’s bad-joke reply | resolved | `["1700153200.000999"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Select the actor’s reply containing Joke: and AI enginner.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "parent_id": {
        "eq": "1700143200.000999"
      },
      "message_id": {
        "eq": "1700153200.000999"
      },
      "user_id": {
        "eq": "U01AGENBOT9"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "proposal for auth improvements tommorow EOD"
        }
      }
    }
  }
]
```

</details>

<a id="slack_79"></a>
## #23 — slack_79

Send a message to #general saying 'Attention' in bold and 'check logs' in italics. Use Slack Block Kit rich_text blocks with style attributes (bold:true, italic:true).

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L23) · [Cards](cards.md#slack_79)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "blocks": {
        "contains": "rich_text_section"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "blocks": {
        "contains": "\"bold\":true"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "blocks": {
        "contains": "\"italic\":true"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_80"></a>
## #24 — slack_80

Send a bulleted list to #random with three items: 'Bagels', 'Coffee', and 'Donuts'. Use Slack Block Kit rich_text blocks with rich_text_list (style:bullet).

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L24) · [Cards](cards.md#slack_80)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "blocks": {
        "contains": "rich_text_list"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "blocks": {
        "contains": "\"style\":\"bullet\""
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_81"></a>
## #25 — slack_81

Do two things using Slack Block Kit: 1) Send a code snippet to #engineering containing `{"status": 200}` using rich_text_preformatted element, and 2) Send a numbered list to #general with items 'Phase 1' and 'Phase 2' using rich_text_list with style:ordered.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L25) · [Cards](cards.md#slack_81)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #engineering | resolved | `["C03IJKL9012"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |
| 2. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A2: Assertions 2 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #engineering; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'engineering'
- **2.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "blocks": {
        "contains": "rich_text_preformatted"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "blocks": {
        "contains": "rich_text_list"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_82"></a>
## #26 — slack_82

Quote the text 'To be or not to be' in the #random channel. Use Slack Block Kit rich_text blocks with rich_text_quote element.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L26) · [Cards](cards.md#slack_82)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "blocks": {
        "contains": "rich_text_quote"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_83"></a>
## #27 — slack_83

Send a table to #growth with headers 'Metric' and 'Value', and one row of data: 'DAU', '1500'. Use Slack Block Kit with a table block type.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L27) · [Cards](cards.md#slack_83)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #growth | resolved | `["C04MNOP3456"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #growth; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'growth'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C04MNOP3456"
      },
      "blocks": {
        "contains": "\"type\":\"table\""
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C04MNOP3456"
      },
      "blocks": {
        "contains": "DAU"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_84"></a>
## #28 — slack_84

Send a markdown formatted message to #engineering with a header 'Daily Report' and a bold item '**All Systems Go**'. Use Slack Block Kit with a markdown block type.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L28) · [Cards](cards.md#slack_84)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #engineering | resolved | `["C03IJKL9012"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #engineering; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'engineering'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "blocks": {
        "contains": "\"type\":\"mrkdwn\""
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_85"></a>
## #29 — slack_85

Mention @Artem in #general using Slack Block Kit rich_text blocks with a user element type containing Artem's user ID.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L29) · [Cards](cards.md#slack_85)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A1, A2: Assertions 1, 2 constrain the resulting change to this seeded referent. |
| 2. Resolve Artem | resolved | `["U02ARTEM23"]` | yes | A2: Assertions 2 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'
- **2.** The prompt’s name resolves to Artem Bogdanov in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Artem Bogdanov'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "blocks": {
        "contains": "\"type\":\"user\""
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "blocks": {
        "contains": "U02ARTEM23"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_86"></a>
## #30 — slack_86

Find the user who complained about 'captcha' in #general and send them a DM saying 'I am looking into this.'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L30) · [Cards](cards.md#slack_86)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the author of the captcha complaint in #general | resolved | `["U06HUBERT23"]` | yes | A3: Assertion 3 requires Hubert’s user ID in a membership addition; the DM/message linkage is not checked. |

Boundary and selection notes:

- **1.** The requested subject is the author. The qualifying message is evidence used to identify that user, not a separately requested subject. Selection: Within general, find the message containing captcha and return its author.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "looking into this"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U06HUBERT23"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_87"></a>
## #31 — slack_87

Create a new channel called 'auth-force' and invite everyone who has posted about 'login' or 'password'.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L31) · [Cards](cards.md#slack_87)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve authors of login/password discussions | resolved | `["U01AGENBOT9","U02JOHNDOE1","U03ROBERT23","U05MORGAN23","U02ARTEM23","U06HUBERT23"]` | partial | A2: The final additions must include six membership rows whose users belong to the six-person set. They need not cover all six distinct people: the same person can occur in different channel memberships. Thus the required recipient set is not enforced by these predicates. |

Boundary and selection notes:

- **1.** Six distinct users authored messages containing login or password. Hubert’s captcha-improvement message explicitly mentions repeated login failures; no expansion beyond the requested terms is needed. Selection: Select distinct authors of messages containing the words login or password.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "channel_name": {
        "contains": "auth-force"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "in": [
          "U01AGENBOT9",
          "U02JOHNDOE1",
          "U03ROBERT23",
          "U05MORGAN23",
          "U02ARTEM23",
          "U06HUBERT23"
        ]
      }
    },
    "expected_count": 6
  }
]
```

</details>

<a id="slack_88"></a>
## #32 — slack_88

Try to invite the user 'ElonMusk' to #general. If you can't find him, inform me (Hubert) via Slack.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L32) · [Cards](cards.md#slack_88)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the user ElonMusk | absent | `[]` | partial | A1, A3: The outcome need not report the requested user’s absence: the text "ElonMusk was found." satisfies the found alternative in A3 while A1 permits no invitation. This checks neither the polarity nor the subject-specific truth of the failure report; no lookup trace is required. |
| 2. Resolve Hubert | resolved | `["U06HUBERT23"]` | yes | A4: Assertions 4 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- Card protocol: v1.0.1.
- **1.** No seeded user matches the explicit requested name; this is absent, not underspecified. The established absence determines the applicable notification branch and contributes to its message text; invitation membership fields belong to the inactive branch. Selection: Case-insensitive exact comparison of ElonMusk with username, display_name, and real_name.
- **2.** Resolve Hubert, the requested notification recipient when ElonMusk cannot be found, to the unique seeded Hubert Marek. ElonMusk’s established absence activates this branch; the general-channel invitation destination belongs only to the inactive branch. Selection: users.real_name == 'Hubert Marek'
- Count subjects needed to determine the condition and those required by the branch applicable to the supplied seed. ElonMusk is absent, so notifying Hubert is applicable; #general is used only by the inactive invitation branch and is excluded. General exists: exclusion is not an absent resolution. Assertion 1 forbids added memberships in general, but this constraint does not create a task grounding obligation or contribute a separate covered obligation.
- Protocol v1.0.1 review: the explicit name ElonMusk establishes an empty match, not competing identities. Keep the existing absent/resolved cards and two-obligation count; no underspecified-selection object is needed.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "regex": "find|found|unable|couldn't|could not|not exist"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U06HUBERT23"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_89"></a>
## #33 — slack_89

Who are the admins of the 'Test Workspace'? Reply with their names in #random.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L33) · [Cards](cards.md#slack_89)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the admins of Test Workspace | resolved | `["U03ROBERT23","U07MORGANFREE"]` | partial | A1, A2: The output "The admins are Robert Chen and Morgan Stanley." contains both required names but identifies the wrong seeded admins (Robert Walsh and Morgan Freeman). The missing constraint is correct reported names, not user IDs or a retrieval trace. |
| 2. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A1, A2: Assertions 1, 2 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The seed explicitly records workspace admin roles. Job titles are irrelevant to this obligation. Selection: Select workspace memberships whose role is admin; return the associated users.
- **2.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "message_text": {
        "contains": "Robert"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "message_text": {
        "contains": "Morgan"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_90"></a>
## #34 — slack_90

Invite the Morgan who is NOT an admin to #random.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L34) · [Cards](cards.md#slack_90)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the non-admin Morgan | resolved | `["U05MORGAN23"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |
| 2. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Select users whose real_name contains Morgan and whose workspace role is not admin.
- **2.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U05MORGAN23"
      },
      "channel_id": {
        "eq": "C02EFGH5678"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_91"></a>
## #35 — slack_91

Post 'Status update: Alpha is on track' to the alpha dev channel.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L35) · [Cards](cards.md#slack_91)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #project-alpha-dev | resolved | `["C06ALPHADEV"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The phrase alpha dev uniquely matches project-alpha-dev among the seed’s channel names. Selection: channels.channel_name == 'project-alpha-dev'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "message_text": {
        "contains": "Status update"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_92"></a>
## #36 — slack_92

Summarize the discussion about 'Gemini' in #random and post the summary to #engineering.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L36) · [Cards](cards.md#slack_92)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the Gemini discussion in #random | resolved | `["1699572000.000789","1700210000.000001","1700210060.000002","1700210120.000003","1700210180.000004","1700210240.000005","1706051580.000000","1706051755.000000","1706052027.000000","1706052160.000000","1706052433.000000","1706052665.000000","1706052779.000000","1706052950.000000","1706053102.000000","1706053181.000000"]` | partial | A1: An output such as "I will not summarize the Gemini discussion." meets the keyword condition but contains no faithful summary. The assertion does not check the requested source-dependent facts in the final summary. |
| 2. Resolve #engineering | resolved | `["C03IJKL9012"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Permissive discussion boundary: the containing history is sufficient evidence, without classifying every reply for topical relevance. The summary keyword does not identify individual source messages. Selection: Resolve random by name and retain its history as the broad discussion source.
- **2.** Resolve the named channel #engineering; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'engineering'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_text": {
        "contains": "Gemini"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_93"></a>
## #37 — slack_93

Check the discussion in #growth. If the team decided to double down on Reddit, react with :rocket: to the message proposing it.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L37) · [Cards](cards.md#slack_93)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the growth message proposing doubling down on Reddit | resolved | `["1700300240.000005"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The conditional outcome and proposed action refer to the same discussion subject; the seed contains an explicit proposal and decision. Selection: Within growth, select content containing double down on Reddit.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1700300240.000005"
      },
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "reaction_type": {
        "eq": "rocket"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_94"></a>
## #38 — slack_94

Hey, I need your help coordinating our 24-hour global hackathon across Lagos, Kyiv, Warsaw, and SF. First, can you find out which channels are relevant for this open source hackathon we're running? I want to make sure #core-infra has an updated topic that reflects we're in hackathon mode.

Also, I need to post an update to the infrastructure team about our coordination status. Before I loop in Łukasz Kowalski and Kenji Sato, can you pull up their profiles? I want to confirm Łukasz is still our performance lead and check Kenji's role on the APAC growth side.

I posted something outdated in one of the channels yesterday that needs to be removed - it had wrong timezone info. Can you also check what's been discussed recently in #project-alpha-dev so I'm caught up? And verify who's currently in #frontend - we might need to add some people.

Oh, and when you find any important messages about the hackathon prep, just give them a thumbs up so people know we've seen them.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L38) · [Cards](cards.md#slack_94)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve channels relevant to the global hackathon | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve #core-infra | resolved | `["C_INFRA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve Lukasz | resolved | `["U_LUKAS"]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve Kenji | resolved | `["U_KENJI"]` | no | None: No assertion constrains this described referent or its derived result. |
| 5. Resolve the actor’s outdated message with wrong timezone information | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 6. Resolve #project-alpha-dev | resolved | `["C06ALPHADEV"]` | no | None: No assertion constrains this described referent or its derived result. |
| 7. Resolve the current members of #frontend | resolved | `["U01AGENBOT9","U_PRIYA","U_LUKAS","U_SOPHIE","U_OLENA","U_MATEO","U_KENJI","U_ROBERT","U_AISHA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 8. Resolve important hackathon-preparation messages | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- **1.** The prompt gives no defensible boundary for relevance to this newly introduced event; the seed has no dedicated hackathon channel. As in slack_98, absence of the event name does not prove absence of potentially relevant channels.
- **2.** The named infrastructure channel is also the infrastructure-team announcement destination; repeated use is one obligation. Selection: channels.channel_name == 'core-infra'
- **3.** The prompt’s name resolves to Łukasz Kowalski in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Łukasz Kowalski'
- **4.** The prompt’s name resolves to 佐藤健二 (Kenji Sato) in the seed. This is one described person even when used repeatedly. Selection: users.real_name == '佐藤健二 (Kenji Sato)'
- **5.** Yesterday and wrong timezone information do not identify a message without a supplied reference date or the incorrect text.
- **6.** Resolve the named channel #project-alpha-dev; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha-dev'
- **7.** Resolve channel_name == 'frontend', join channel_members on channel_id, return member user_ids.
- **8.** Important is subjective and no concrete preparation-message description or constraining assertion is supplied.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {},
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_95"></a>
## #39 — slack_95

I need some help organizing our Diwali x Thanksgiving potluck celebration! We're doing a combined Indian and American traditions thing and I want to make sure we coordinate this properly across the team.

First, can you check what channels we have that might be relevant for this event and see what's been discussed recently in #core-infra? I want to make sure I'm not stepping on any ongoing conversations. Also, I need to know who's on our team so I can figure out who to involve based on their backgrounds and expertise.

Once you've got that context, please update the topics for #core-infra, #project-alpha, and #growth to reflect that we're planning this potluck celebration. Then post an announcement in #project-alpha about the event.

I also need you to check who's currently in #growth to make sure the right people are included, and open a direct message with Kenji Sato since I need to coordinate with him separately about timing given APAC schedules.

Oh, and there's an old message I posted earlier about the event that has wrong details - can you update it with the correct information? There's also an outdated announcement from last week that's no longer relevant, so please delete that. Finally, just react to Priya's message about bringing samosas to show I've seen it!

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L39) · [Cards](cards.md#slack_95)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve channels relevant to the Diwali–Thanksgiving potluck | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve #core-infra | resolved | `["C_INFRA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve the workspace user roster | resolved | `["U01AGENBOT9","U02JOHNDOE1","U02ARTEM23","U03ROBERT23","U04OMER23","U05MORGAN23","U06HUBERT23","U07MORGANFREE","U08NICK23","U09GABRIEL","U_PRIYA","U_LUKAS","U_SOPHIE","U_OLENA","U_MATEO","U_KENJI","U_ROBERT","U_AISHA","U_INCOGNITO"]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve #project-alpha | resolved | `["C05ALPHA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 5. Resolve #growth | resolved | `["C04MNOP3456"]` | no | None: No assertion constrains this described referent or its derived result. |
| 6. Resolve the current members of #growth | resolved | `["U08NICK23","U09GABRIEL","U06HUBERT23","U01AGENBOT9"]` | no | None: No assertion constrains this described referent or its derived result. |
| 7. Resolve Kenji | resolved | `["U_KENJI"]` | no | A1: A DM must be created, but its participant is unconstrained. |
| 8. Resolve the actor’s earlier potluck message with wrong details | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 9. Resolve the outdated announcement from last week | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 10. Resolve Priya’s message about bringing samosas | absent | `[]` | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- **1.** The description does not justify a particular entity or entity set in the allowed evidence.
- **2.** Resolve core-infra for reviewing its history and changing its topic; no subjective message-level boundary is needed. Selection: channels.channel_name == 'core-infra'
- **3.** Select all users in the seeded workspace.
- **4.** Resolve project-alpha for the topic update and announcement; these repeated uses share one obligation. Selection: channels.channel_name == 'project-alpha'
- **5.** Resolve the named channel #growth; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'growth'
- **6.** Resolve channel_name == 'growth', join channel_members on channel_id, return member user_ids.
- **7.** The prompt’s name resolves to 佐藤健二 (Kenji Sato) in the seed. This is one described person even when used repeatedly. Selection: users.real_name == '佐藤健二 (Kenji Sato)'
- **8.** The description does not justify a particular entity or entity set in the allowed evidence.
- **9.** The description does not justify a particular entity or entity set in the allowed evidence.
- **10.** The description names a concrete subject (samosa); the seed contains no matching message. Absence is relative to the supplied seed, not a running service. Selection: Case-insensitive content match for 'samosa', authored by Priya.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {},
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_96"></a>
## #40 — slack_96

I need some help getting our Lunar New Year product launch coordination sorted out. We're targeting APAC markets and I want to make sure we're being culturally sensitive with our timing and messaging.

First, can you help me figure out who on our team has the right expertise for this? I need to reach out directly to our frontend person about some UI elements that need to be adapted, and also connect with our engineering lead separately about the technical rollout schedule.

Also, I noticed the #project-alpha-dev channel might have some people who aren't really needed for this particular launch, and I want to keep discussions focused. Can you check who's currently in that channel? We may need to streamline the membership a bit - I think there are a couple of folks who were added for previous projects but don't need to be looped in on the APAC launch details.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L40) · [Cards](cards.md#slack_96)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the team roster as evidence of launch expertise | resolved | `["U01AGENBOT9","U02JOHNDOE1","U02ARTEM23","U03ROBERT23","U04OMER23","U05MORGAN23","U06HUBERT23","U07MORGANFREE","U08NICK23","U09GABRIEL","U_PRIYA","U_LUKAS","U_SOPHIE","U_OLENA","U_MATEO","U_KENJI","U_ROBERT","U_AISHA","U_INCOGNITO"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve the frontend person for direct coordination | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve the engineering lead for direct coordination | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve the current members of #project-alpha-dev | resolved | `["U01AGENBOT9","U_PRIYA","U_LUKAS","U_MATEO","U_KENJI","U_ROBERT","U_AISHA"]` | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- **1.** Select all users in the seeded workspace.
- **2.** The seed has several frontend participants but no explicit job-title field establishing one designated frontend person. Do not promote a plausible contributor into a justified unique referent.
- **3.** Participation, an admin flag, and apparent leadership in discussion do not uniquely establish the requested job role.
- **4.** Resolve channel_name == 'project-alpha-dev', join channel_members on channel_id, return member user_ids.
- May need to streamline membership is tentative context, not a definite instruction to remove a particular person/set; no removal obligation is invented.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_97"></a>
## #41 — slack_97

I need some help cleaning up our Afrobeats festival streaming project workspace. We've had some organizational issues lately. First, can you find out who's currently hanging out in #random and also get me a list of everyone on the team? I need to verify Robert Chen's role since he's supposed to be leading the engineering side of things.

I also need you to dig through our CDN-related conversations - we had some important discussions about our content delivery setup that I need to reference. Check what's been happening recently in #project-alpha too.

Once you've got the lay of the land, please remove Artem Bogdanov from #project-alpha-dev and also kick Hubert Marek from #core-infra - they've moved to different workstreams. Post an update to #core-infra about our streaming infrastructure progress, and update the topic there to reflect our virtual festival focus.

There's also an outdated message I posted earlier that needs deleting, and I need to correct some information in a previous update I sent. Can you help me sort all this out?

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L41) · [Cards](cards.md#slack_97)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the current members of #random | resolved | `["U01AGENBOT9","U02JOHNDOE1","U03ROBERT23","U06HUBERT23"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve the workspace user roster | resolved | `["U01AGENBOT9","U02JOHNDOE1","U02ARTEM23","U03ROBERT23","U04OMER23","U05MORGAN23","U06HUBERT23","U07MORGANFREE","U08NICK23","U09GABRIEL","U_PRIYA","U_LUKAS","U_SOPHIE","U_OLENA","U_MATEO","U_KENJI","U_ROBERT","U_AISHA","U_INCOGNITO"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve Robert Chen | resolved | `["U_ROBERT"]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve the CDN-related discussion source | resolved | `["C_GROWTH"]` | no | None: No assertion constrains this described referent or its derived result. |
| 5. Resolve #project-alpha | resolved | `["C05ALPHA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 6. Resolve Artem | resolved | `["U02ARTEM23"]` | no | None: No assertion constrains this described referent or its derived result. |
| 7. Resolve #project-alpha-dev | resolved | `["C06ALPHADEV"]` | no | None: No assertion constrains this described referent or its derived result. |
| 8. Resolve Hubert | resolved | `["U06HUBERT23"]` | no | None: No assertion constrains this described referent or its derived result. |
| 9. Resolve #core-infra | resolved | `["C_INFRA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 10. Resolve the actor’s outdated message to delete | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 11. Resolve the actor’s previous update to correct | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- **1.** Resolve channel_name == 'random', join channel_members on channel_id, return member user_ids.
- **2.** Select all users in the seeded workspace.
- **3.** The prompt’s name resolves to Robert Chen in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Robert Chen'
- **4.** The product-growth history contains the CDN/CloudFront discussion. Reporting-only relevance is resolved at its containing channel, not a subjective exact message set. Selection: Select channels containing CDN/CloudFront routing discussion; retain the containing conversation as the permissive evidence boundary.
- **5.** Resolve the named channel #project-alpha; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha'
- **6.** The prompt’s name resolves to Artem Bogdanov in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Artem Bogdanov'
- **7.** Resolve the named channel #project-alpha-dev; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha-dev'
- **8.** The prompt’s name resolves to Hubert Marek in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Hubert Marek'
- **9.** Resolve the named channel #core-infra; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'core-infra'
- **10.** The description does not justify a particular entity or entity set in the allowed evidence.
- **11.** The description does not justify a particular entity or entity set in the allowed evidence.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {},
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_98"></a>
## #42 — slack_98

I need your help coordinating something for our Polish-Ukrainian debugging session today. We're calling it the "Pierogi vs Varenyky Debug Session" because Olena and Sophie are bringing food during our break!

First, can you check on Sophie Dubois and Olena Petrenko's profiles? I want to make sure I have their roles right when I introduce them to the rest of the team. Also, I need to catch up on what's been happening in the engineering channel - there were some login issues discussed that might be relevant.

Could you find any channels that might already be discussing this topic, and if there isn't a dedicated space yet, please create a new channel for our pierogi-vs-varenyky session? We should also post a heads-up in core-infra about our debugging plans.

Oh, and Aisha left a great message earlier that I want to react to with a thumbs up. Also, I need to remove someone from one of our project channels who's no longer on the team. Thanks!

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L42) · [Cards](cards.md#slack_98)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Sophie Dubois’s profile | resolved | `["U_SOPHIE"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve Olena Petrenko’s profile | resolved | `["U_OLENA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve engineering as the source of discussion to review | resolved | `["C03IJKL9012"]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve channels already discussing the session’s topic | underspecified | `{"selection":"set(channels)","partial_constraints":["channels.channel_id in {\"C01ABCD1234\", \"C03IJKL9012\"}"],"candidate_sets":[[],["C01ABCD1234","C03IJKL9012"]]}` | no | None: No assertion constrains this described referent or its derived result. |
| 5. Resolve core-infra as the announcement destination | resolved | `["C_INFRA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 6. Resolve Aisha’s earlier great message | underspecified | `{"selection":"one(messages)","partial_constraints":["messages.user_id == \"U_AISHA\""],"candidate_sets":[["1706043661.000000"],["1706044159.000000"],["1706044630.000000"],["1706045415.000000"],["1706052665.000000"],["1706052950.000000"]]}` | no | None: No assertion constrains this described referent or its derived result. |
| 7. Resolve the person who is no longer on the team | underspecified | `{"selection":"one(users)","partial_constraints":[],"candidate_sets":null}` | no | None: No assertion constrains this described referent or its derived result. |
| 8. Resolve the project channel for the removal | underspecified | `{"selection":"one(channels)","partial_constraints":[],"candidate_sets":null}` | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- Card protocol: v1.0.1.
- **1.** The prompt’s name resolves to Sophie Dubois in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Sophie Dubois'
- **2.** The prompt’s name resolves to Olena Petrenko in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Olena Petrenko'
- **3.** User-approved permissive boundary: identify the engineering channel and do not impose an exact subset of its login-related messages. Selection: channels.channel_name == 'engineering'
- **4.** The prompt first names a Polish-Ukrainian debugging session, then mentions login issues before asking for channels discussing “this topic.” If this means the named session, no seeded channel discussion matches (the empty candidate set). If it means the login issues, general and engineering match (C01ABCD1234 and C03IJKL9012). These readings give different sets, and the prompt does not distinguish the intended reading. The competing sets do not authorize choosing a reading arbitrarily.
- **5.** Resolve the named channel #core-infra; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'core-infra'
- **6.** The request says “Aisha left a great message earlier that I want to react to.” Six seeded messages are authored by Aisha, but the user’s intended message is not distinguished. “Great” describes that remembered message rather than delegating a choice to the agent. Each candidate set contains one possible reaction target; it is not permission to choose any of them.
- **7.** No person is named, and departure status is not recorded in the seed. This is unknown identity, not a demonstrated empty set.
- **8.** Several project channels exist; one of our project channels does not distinguish the intended one.
- Protocol v1.0.1: O4 retains competing topic interpretations; O6 retains Aisha’s authorship without resolving the user’s intended message. The login reading is supported by four engineering messages and two general messages about login failures/improvements. The food mention in general does not discuss the named session. O7’s departure fact and O8’s intended project channel are not distinguished by the supplied evidence; no departure or project-channel flag is invented.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_private": {
        "eq": false
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {},
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_99"></a>
## #43 — slack_99

I need some help organizing our cross-cultural tea ceremony exchange between the Tokyo and Paris offices. Can you set up a dedicated channel for this traditional tea ceremony planning initiative and make sure the channel topic clearly explains what it's about?

Before we get started, I want to check what's been happening in #random lately - there was some casual conversation about lunch plans and something about Gemini that might be relevant to who's interested. Also, take a look at #growth because I remember seeing some Reddit strategy discussion that could tie into how we promote this cultural exchange.

I posted a few messages earlier about the event that need updating with corrected information - the dates and details have changed. There's also one outdated message I sent that's no longer relevant and should just be removed entirely to avoid confusion.

Oh, and if you see the message where Priya or Mateo showed interest in participating, can you add a reaction to acknowledge it? I don't want to clutter the thread with another reply.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L43) · [Cards](cards.md#slack_99)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #random | resolved | `["C02EFGH5678"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve #growth | resolved | `["C04MNOP3456"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve the actor’s event messages needing corrected dates and details | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve the actor’s outdated message to remove | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 5. Resolve the message where Priya or Mateo expressed participation interest | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- **1.** Lunch and Gemini are contextual examples in a request to catch up on random; retain the named channel as one broad discussion source. Selection: channels.channel_name == 'random'
- **2.** Resolve the named channel #growth; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'growth'
- **3.** The description does not justify a particular entity or entity set in the allowed evidence.
- **4.** The description does not justify a particular entity or entity set in the allowed evidence.
- **5.** The event-specific interest is not pinned to a concrete statement; the disjunction of authors does not establish a message.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_private": {
        "eq": false
      }
    },
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_100"></a>
## #44 — slack_100

I need your help coordinating our Lunar New Year product launch for the APAC market. Can you first catch me up on what's been happening in #model-research and #core-infra? I want to make sure we're not planning a launch during any technical instability.

Also, I need to verify that Kenji Sato and Robert Chen are the right people to loop in on this - can you confirm their roles for me? Kenji should be handling APAC growth and Robert should be our engineering lead.

Once you've gathered that context, please set up a dedicated channel for this initiative and make sure the topic clearly reflects what we're working on. Then post a summary of what you found to #project-alpha-dev so the team is aligned.

Oh, and I think I sent a message earlier about the timeline that needs updating with the correct dates - can you fix that? And if there's anything important in those channel histories worth acknowledging, give it a thumbs up so people know we've seen it.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L44) · [Cards](cards.md#slack_100)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #model-research | resolved | `["C_MODEL"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve #core-infra | resolved | `["C_INFRA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve Kenji | resolved | `["U_KENJI"]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve Robert Chen | resolved | `["U_ROBERT"]` | no | None: No assertion constrains this described referent or its derived result. |
| 5. Resolve #project-alpha-dev | resolved | `["C06ALPHADEV"]` | no | None: No assertion constrains this described referent or its derived result. |
| 6. Resolve the actor’s earlier timeline message to correct | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 7. Resolve important messages in the reviewed histories | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- **1.** Resolve the named channel #model-research; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'model-research'
- **2.** Resolve the named channel #core-infra; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'core-infra'
- **3.** The prompt’s name resolves to 佐藤健二 (Kenji Sato) in the seed. This is one described person even when used repeatedly. Selection: users.real_name == '佐藤健二 (Kenji Sato)'
- **4.** The prompt’s name resolves to Robert Chen in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Robert Chen'
- **5.** Resolve the named channel #project-alpha-dev; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha-dev'
- **6.** The description does not justify a particular entity or entity set in the allowed evidence.
- **7.** Important supplies no justified reaction target, and no assertion supplies a permissive candidate boundary.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_private": {
        "eq": false
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {},
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_101"></a>
## #45 — slack_101

I need some help coordinating our virtual Afrobeats festival streaming infrastructure project. Can you help me get things organized across our Slack workspace?

First, I want to make sure the #engineering channel clearly reflects that we're focused on the Music Festival Tech Stack right now - the topic should be updated so everyone knows what we're working on.

I remember there were some discussions about CDN solutions a while back that would be really relevant to our streaming needs - can you dig those up for me?

I also need to figure out who on our team should be involved. I know Robert Chen is supposed to be leading the engineering side, but can you confirm his role? And I think Łukasz Kowalski has some great performance optimization experience - make sure he's part of the conversation in our main coordination channel.

Once you've gathered all this info, I need updates posted to #engineering, #frontend, and #general to get everyone aligned on our festival streaming infrastructure plans. Also, check what channels we have available that might be relevant to this project.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L45) · [Cards](cards.md#slack_101)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #engineering | resolved | `["C03IJKL9012"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve the CDN-discussion source | resolved | `["C_GROWTH"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve Robert Chen | resolved | `["U_ROBERT"]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve Lukasz | resolved | `["U_LUKAS"]` | no | A2: The membership-addition assertion contains no user predicate. |
| 5. Resolve the main coordination channel | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 6. Resolve #frontend | resolved | `["C_FRONTEND"]` | no | None: No assertion constrains this described referent or its derived result. |
| 7. Resolve #general | resolved | `["C01ABCD1234"]` | no | None: No assertion constrains this described referent or its derived result. |
| 8. Resolve channels relevant to festival streaming coordination | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- **1.** Resolve the named channel #engineering; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'engineering'
- **2.** Retain the containing conversation as the permissive reporting source. Selection: Select channels containing CDN/CloudFront routing discussion.
- **3.** The prompt’s name resolves to Robert Chen in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Robert Chen'
- **4.** The prompt’s name resolves to Łukasz Kowalski in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Łukasz Kowalski'
- **5.** The main coordination channel is not named. Engineering is plausible but not established as the invitation destination.
- **6.** Resolve the named channel #frontend; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'frontend'
- **7.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'
- **8.** The description does not justify a particular entity or entity set in the allowed evidence.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {},
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {},
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_102"></a>
## #46 — slack_102

I need help getting our anime convention booth coordination sorted out. Can you check what's been happening in #product-growth and #random lately? I want to make sure I'm caught up on any relevant discussions before we dive into planning.

Also, I remember there were some conversations about badges somewhere - can you find those for me? We had some outdated messages about our old booth location that need to be removed since we got reassigned to a different hall.

I need to loop in Olena Petrenko on this since her perspective would be really helpful for the setup logistics. And I should probably reach out directly to John Doe and Priya Sharma separately - John for general coordination and Priya about the infrastructure stuff like power and internet at the booth.

Oh, and let's update the channel topics for #product-growth and #project-alpha-dev to reflect that we're focusing on the anime expo booth setup now. There were a couple of my earlier messages that need corrections too - I posted the wrong setup times initially. Once you find the key planning message, just give it a thumbs up so everyone knows we're aligned.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L46) · [Cards](cards.md#slack_102)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #product-growth | resolved | `["C_GROWTH"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve #random | resolved | `["C02EFGH5678"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve the discussions about badges | absent | `[]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve outdated messages about the old booth location | absent | `[]` | no | None: No assertion constrains this described referent or its derived result. |
| 5. Resolve Olena | resolved | `["U_OLENA"]` | no | A2: A membership addition is required but neither participant nor destination is specified. |
| 6. Resolve the conversation in which to involve Olena | underspecified | `{"selection":"one(channels)","partial_constraints":[],"candidate_sets":null}` | no | None: No assertion constrains this described referent or its derived result. |
| 7. Resolve John | resolved | `["U02JOHNDOE1"]` | no | A1: At least one DM is required; neither recipient is constrained. |
| 8. Resolve Priya | resolved | `["U_PRIYA"]` | no | A1: At least one DM is required; neither recipient is constrained. |
| 9. Resolve #project-alpha-dev | resolved | `["C06ALPHADEV"]` | no | None: No assertion constrains this described referent or its derived result. |
| 10. Resolve the actor’s messages with incorrect setup times | absent | `[]` | no | None: No assertion constrains this described referent or its derived result. |
| 11. Resolve the key planning message | absent | `[]` | no | None: No assertion constrains this described referent or its derived result. |

Boundary and selection notes:

- Card protocol: v1.0.1.
- **1.** Resolve the named channel #product-growth; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'product-growth'
- **2.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'
- **3.** The description names a concrete subject (badge); the seed contains no matching message. Absence is relative to the supplied seed, not a running service. Selection: Case-insensitive content match for 'badge'.
- **4.** The request asks to remove outdated messages about the anime convention’s old booth location. No seeded message discusses that booth location, so the necessary candidate population is empty. The unnamed old hall does not turn this established absence into an unresolved selection. Selection: Select messages whose content concerns the anime convention booth location, then the described old-location messages. The necessary booth-location population is empty in this seed; no old-hall predicate is needed to establish the empty result.
- **5.** The prompt’s name resolves to Olena Petrenko in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Olena Petrenko'
- **6.** The request says “loop in Olena Petrenko” for booth coordination but does not identify the destination conversation. Several conversations exist; the intended one is not distinguished. Olena’s identity is a separate resolved obligation, and no destination constraint can be encoded from her name alone.
- **7.** The prompt’s name resolves to John Doe in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'John Doe'
- **8.** The prompt’s name resolves to Priya Sharma in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Priya Sharma'
- **9.** Resolve the named channel #project-alpha-dev; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha-dev'
- **10.** The request asks to correct the actor’s earlier messages with wrong anime convention setup times. No seeded messages discuss setup times for that convention, including those authored by the actor. The necessary candidate population is empty despite the unspecified wrong and replacement times. Selection: Select messages authored by U01AGENBOT9 whose content concerns setup times for the anime convention, then the described incorrect-time messages. The necessary convention setup-time population is empty.
- **11.** The request asks for a thumbs-up reaction on the key planning message for the anime convention booth. No seeded message concerns that convention’s planning, so there is no matching message. The adjective “key” does not create an unresolved choice within an empty candidate population. Selection: Select messages whose content concerns planning the anime convention booth. This necessary population is empty, so there is no key planning message.
- Protocol v1.0.1: O4, O10, and O11 change from underspecified to absent because their necessary convention-related message populations are empty; O6 remains underspecified. These content judgments concern the described event, not generic planning, timing, or location language elsewhere in the seed. Empty computation inputs on these absent targets do not supply missing replacement times or certify an executable state change. Obligation counts and assertion coverage are unchanged.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {},
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_103"></a>
## #47 — slack_103

Hey, I need your help organizing a Cricket World Cup watch party for our office! We've got team members spread across India, UK, and Australia timezones, so this needs some coordination.

First, can you check what channels we already have that might be relevant to this kind of event? I want to make sure we're not duplicating efforts.

I think we should create a dedicated channel for the watch party coordination. Once that's set up, update the topic so people know what it's for. I also need to reach out to Priya Sharma directly since she handles infrastructure and we'll need her help with the streaming setup across offices.

Can you pull up our team roster so I can see who else might want to be involved? Oh, and I posted a message in #general about the watch party time being 3pm PST - that's wrong, it should be 3pm IST since we're primarily coordinating with the India office. Please fix that. There's also an old message I sent about booking a downtown venue that's no longer happening - just delete that one entirely.

Thanks!

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L47) · [Cards](cards.md#slack_103)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve existing channels relevant to the watch party | underspecified | Undetermined | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve Priya | resolved | `["U_PRIYA"]` | no | A2: A DM is required with no recipient constraint. |
| 3. Resolve the workspace user roster | resolved | `["U01AGENBOT9","U02JOHNDOE1","U02ARTEM23","U03ROBERT23","U04OMER23","U05MORGAN23","U06HUBERT23","U07MORGANFREE","U08NICK23","U09GABRIEL","U_PRIYA","U_LUKAS","U_SOPHIE","U_OLENA","U_MATEO","U_KENJI","U_ROBERT","U_AISHA","U_INCOGNITO"]` | no | None: No assertion constrains this described referent or its derived result. |
| 4. Resolve the actor’s incorrect 3pm PST watch-party message | resolved | `["1699564900.000124"]` | yes | A3: Assertions 3 constrain the resulting change to this seeded referent. |
| 5. Resolve the actor’s downtown-venue booking message | resolved | `["1699564950.000125"]` | yes | A4: Assertions 4 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** General contains watch-party messages, but might be relevant does not establish which existing channels qualify. Retain the agreed underspecification convention for event-channel discovery.
- **2.** The prompt’s name resolves to Priya Sharma in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Priya Sharma'
- **3.** Select all users in the seeded workspace.
- **4.** Within general, select the actor’s watch-party message containing 3pm PST.
- **5.** Select the actor’s message containing booking the downtown venue.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_private": {
        "eq": false
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "message_id": {
        "eq": "1699564900.000124"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "contains": "IST"
        }
      }
    }
  },
  {
    "diff_type": "removed",
    "entity": "messages",
    "where": {
      "message_id": {
        "eq": "1699564950.000125"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_104"></a>
## #48 — slack_104

I need to do a quick audit of our #engineering channel. Can you get me the full details about the channel and check who's currently in it?

Post the audit results to #general - I want a message showing the exact member count (as a number) and a list of the current members by name.

After that, rename #engineering to "engineering-backend" since that's what the team mainly works on. Then post a follow-up message in #general confirming the rename was successful with the new channel name.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L48) · [Cards](cards.md#slack_104)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve #engineering | resolved | `["C03IJKL9012"]` | yes | A3: Assertions 3 constrain the resulting change to this seeded referent. |
| 2. Resolve the current members of #engineering | resolved | `["U01AGENBOT9","U02JOHNDOE1","U03ROBERT23","U05MORGAN23","U06HUBERT23"]` | partial | A1, A2: A1 accepts "Member count: 15" because it contains 5, and A2 only requires a member word. The correct count of five and the requested member-name list are not reliably checked in the output. |
| 3. Resolve #general | resolved | `["C01ABCD1234"]` | yes | A1, A2, A4: Assertions 1, 2, 4 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The channel is independently requested for details and rename. Both uses refer to the same seeded entity. Selection: channels.channel_name == 'engineering'
- **2.** Resolve channel_name == 'engineering', join channel_members on channel_id, return member user_ids.
- **3.** Resolve the named channel #general; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'general'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "5"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "regex": "[Mm]ember"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      }
    },
    "expected_changes": {
      "channel_name": {
        "to": {
          "contains": "engineering-backend"
        }
      }
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "contains": "engineering-backend"
      }
    },
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_105"></a>
## #49 — slack_105

There's a thread in #engineering where Robert asked about the circuit tracer library rewrite timeline. We've been having issues with the layer-by-layer loading and need to rewrite it in PyTorch from scratch to handle multi-GPU distribution properly.

Sophie sent me a DM with her implementation plan and timeline since she's leading the PyTorch migration. Check my DM with Sophie to find her estimated completion date, then reply to Robert's question in the thread with that information.

After replying, add a checkmark reaction to the original thread message to mark it as addressed.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L49) · [Cards](cards.md#slack_105)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Robert’s circuit-tracer question and its thread | resolved | `["1706110000.000200"]` | yes | A1: A1 fixes the final reply’s channel to engineering and its parent to the circuit-tracer root, which is the documented destination for replying to Robert’s question in that thread. Recording Robert’s reply ID or proving that his question was read is unnecessary. Timeline-answer fidelity is assessed separately under obligation 2. |
| 2. Resolve Sophie’s DM containing her implementation plan and timeline | resolved | `["1706100000.000001"]` | partial | A1: Sophie’s seeded estimate is Wednesday next week, but "Completion is Friday next week; Wednesday is only a review meeting." satisfies A1. The output need not state the correct completion estimate. This remains partial for answer fidelity, not because the DM or its ID must be exposed. |
| 3. Resolve the original circuit-tracer thread message | resolved | `["1706110000.000100"]` | yes | A2: Assertions 2 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The question is independently described as the reply target. Its parent relationship provides the thread-root handle needed to reply. Selection: Within engineering, select the reply asking when the PyTorch rewrite will be ready.
- **2.** Resolve Sophie by real_name, find the actor–Sophie DM by membership, and select her PyTorch-plan message.
- **3.** Within engineering, select the circuit-tracer root about layer-by-layer loading and a PyTorch rewrite.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "parent_id": {
        "eq": "1706110000.000100"
      },
      "message_text": {
        "contains": "Wednesday"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706110000.000100"
      },
      "user_id": {
        "eq": "U01AGENBOT9"
      }
    },
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_106"></a>
## #50 — slack_106

It's end of Q4 and I need to reorganize our Slack workspace. Help me with the following:

1. First, list all the channels I'm currently a member of. Format it as a numbered list showing: channel name, member count. Send that list to me as a DM to myself.

2. The "old-project-q3" channel was archived but we're reviving it for Q1 planning. Unarchive it and rename it to "q1-planning-2026". Update the topic to "Q1 2026 Planning - Americas Team".

3. In #project-alpha-dev, we want to focus on the Americas timezone team only. Check each member's timezone using their profile info, then remove anyone who is NOT in an Americas timezone (timezone should start with "America/").

4. I left an 👀 reaction on the circuit-tracer thread in #engineering a while back - please remove that since we've addressed the issue.

5. Join the #product-growth channel since I'm not in it yet.

6. Finally, post a Q1 kickoff message in the newly renamed channel. In the message, list which team members from #project-alpha-dev are in Americas timezones (the ones who remain after cleanup) - include their names and timezones.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L50) · [Cards](cards.md#slack_106)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve conversations the acting user currently belongs to | resolved | `["C01ABCD1234","C02EFGH5678","C03IJKL9012","C04MNOP3456","C06ALPHADEV","C05ALPHA","C_INFRA","C_MODEL","C_FRONTEND"]` | partial | A1: An output containing only general meets A1 while omitting the other current channels and their member counts. The missing check concerns the completeness of the requested final list, not how the memberships were retrieved. |
| 2. Resolve #old-project-q3 | resolved | `["C_OLD_PROJECT"]` | yes | A2, A3, A16, A17: Assertions 2, 3, 16, 17 constrain the resulting change to this seeded referent. |
| 3. Resolve #project-alpha-dev | resolved | `["C06ALPHADEV"]` | yes | A4, A5, A6, A7, A8, A9, A10, A11, A12, A13: Assertions 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 constrain the resulting change to this seeded referent. |
| 4. Resolve non-Americas members of #project-alpha-dev | resolved | `["U_PRIYA","U_LUKAS","U_KENJI","U_AISHA"]` | yes | A4, A5, A6, A7: Each of the four explicit non-Americas users is individually required to be removed from the correct channel. |
| 5. Resolve the actor’s eyes reaction on the engineering circuit-tracer root | resolved | `[{"message_id":"1706110000.000100","user_id":"U01AGENBOT9","reaction_type":"eyes"}]` | yes | A14: The removal predicate identifies the existing reaction by message and emoji and acting user. |
| 6. Resolve #product-growth | resolved | `["C_GROWTH"]` | yes | A15: Assertions 15 constrain the resulting change to this seeded referent. |
| 7. Resolve the Americas members remaining in #project-alpha-dev | resolved | `["U_MATEO","U_ROBERT"]` | partial | A8, A9, A10, A11, A12, A13, A16, A17: A8–A13 preserve the two relevant memberships, but A16–A17 accept "Mateo and Robert remain" without either requested timezone. Preservation constrains the underlying state; the source-dependent report remains incomplete. No source IDs are required in the report. |

Boundary and selection notes:

- **1.** Select memberships of the acting user and return the associated non-DM channels.
- **2.** Resolve the named channel #old-project-q3; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'old-project-q3'
- **3.** Resolve the named channel #project-alpha-dev; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha-dev'
- **4.** The four non-Americas profile timezones are explicit. The actor has no seeded timezone; do not infer a missing timezone or remove the acting account. Selection: Resolve project-alpha-dev, join its members to users, select explicit timezones not starting America/.
- **5.** The message and its author/channel are qualifiers of this one described existing reaction; no additional optional lookup obligations are counted. Selection: Resolve the circuit-tracer root in engineering, then its eyes reaction by the acting user.
- **6.** Resolve the named channel #product-growth; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'product-growth'
- **7.** Mateo and Robert Chen are the two members with explicit America/ timezones. The requested remaining-member report is a separately described subject from the removal set. Selection: Resolve project-alpha-dev, join its members to users, select explicit timezones starting America/.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "message_text": {
        "contains": "general"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": {
        "eq": "C_OLD_PROJECT"
      }
    },
    "expected_changes": {
      "is_archived": {
        "to": {
          "eq": false
        }
      },
      "channel_name": {
        "to": {
          "contains": "q1-planning"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": {
        "eq": "C_OLD_PROJECT"
      }
    },
    "expected_changes": {
      "topic_text": {
        "to": {
          "contains": "Americas"
        }
      }
    }
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_PRIYA"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_LUKAS"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_KENJI"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_AISHA"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_MATEO"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_MATEO"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "changed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_MATEO"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_ROBERT"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_ROBERT"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "changed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_ROBERT"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "removed",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706110000.000100"
      },
      "user_id": {
        "eq": "U01AGENBOT9"
      },
      "reaction_type": {
        "eq": "eyes"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C_GROWTH"
      },
      "user_id": {
        "eq": "U01AGENBOT9"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C_OLD_PROJECT"
      },
      "message_text": {
        "contains": "Mateo"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C_OLD_PROJECT"
      },
      "message_text": {
        "contains": "Robert"
      }
    },
    "expected_count": {
      "min": 1
    }
  }
]
```

</details>

<a id="slack_107"></a>
## #51 — slack_107

Kenji, Olena, and Priya want to spin up a generative art project using the team's GPU infrastructure. They drew inspiration from the compute discussions and that circuit-tracer visualization work happening somewhere in the workspace. Can you get them organized? They need a channel — call it #fractal-forge — with a topic that contains "GPU-meets-art". Invite all three, and post an inaugural message that references whatever you can dig up about the GPU work and the circuit-tracer thread that got them excited -- those are going to be messeges on the topic, written by either three. Kenji also wants an :art: reaction on whichever message in #engineering first mentioned the circuit-tracer. Set up a group DM with just Kenji and Olena so they can sort out GPU scheduling privately. And actually, rename the channel to #silicon-dreams — everyone agreed it sounds better.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L51) · [Cards](cards.md#slack_107)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Kenji | resolved | `["U_KENJI"]` | yes | A4: A membership count is fixed for this individual user. The new-channel/group-DM allocation is not fully tied together. |
| 2. Resolve Olena | resolved | `["U_OLENA"]` | yes | A5: A membership count is fixed for this individual user. The new-channel/group-DM allocation is not fully tied together. |
| 3. Resolve Priya | resolved | `["U_PRIYA"]` | yes | A3: A membership count is fixed for this individual user. The new-channel/group-DM allocation is not fully tied together. |
| 4. Resolve the three participants’ GPU-work discussion | resolved | `["1706000496.000000","1706000791.000000","1706001104.000000","1706001136.000000","1706001628.000000","1706001817.000000","1706001931.000000","1706002397.000000","1706012958.000000","1706013249.000000","1706013725.000000","1706014443.000000","1706067650.000000","1706068303.000000"]` | partial | A8: The opening text can merely mention GPU without conveying any of the participants’ GPU-work discussion. A8 checks a topic word, not the requested source-dependent contribution to the final opening post. |
| 5. Resolve the three participants’ circuit-tracer discussion | resolved | `["1706110000.000300"]` | partial | A7, A12, A13, A14: A7 and the destination exclusions permit a circuit keyword in an allowed destination without any information from the participants’ circuit-tracer discussion. Final content fidelity is unchecked; citation of source records is not required. |
| 6. Resolve the first engineering message mentioning circuit-tracer | resolved | `["1706110000.000100"]` | yes | A6: Assertions 6 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to 佐藤健二 (Kenji Sato) in the seed. This is one described person even when used repeatedly. Selection: users.real_name == '佐藤健二 (Kenji Sato)'
- **2.** The prompt’s name resolves to Olena Petrenko in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Olena Petrenko'
- **3.** The prompt’s name resolves to Priya Sharma in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Priya Sharma'
- **4.** Use a broad compute-discussion boundary rather than requiring an exact summary selection; author restrictions remain explicit. Selection: Select messages by the three named participants about GPU/CUDA/tensor/VRAM/batch-size/quantization work.
- **5.** Kenji’s JAX reply is in the described circuit-tracer thread. The participant restriction is retained even though the root was authored by Lukasz. Selection: Select messages by the three named participants explicitly mentioning circuit-tracer or replying under its identified engineering root.
- **6.** Within engineering, filter circuit-tracer content and choose the earliest numeric timestamp.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "channel_name": {
        "eq": "silicon-dreams"
      },
      "topic_text": {
        "i_contains": "GPU-meets-art"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_gc": {
        "eq": true
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_PRIYA"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_KENJI"
      }
    },
    "expected_count": 2
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_OLENA"
      }
    },
    "expected_count": 2
  },
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706110000.000100"
      },
      "reaction_type": {
        "eq": "art"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "message_text": {
        "i_contains": "circuit"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "message_text": {
        "i_contains": "GPU"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706110000.000100"
      },
      "reaction_type": {
        "eq": "eyes"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "removed",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706110000.000100"
      },
      "reaction_type": {
        "eq": "eyes"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "changed",
    "entity": "message_reactions",
    "where": {
      "message_id": {
        "eq": "1706110000.000100"
      },
      "reaction_type": {
        "eq": "eyes"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C01ABCD1234"
      },
      "message_text": {
        "i_contains": "circuit"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "message_text": {
        "i_contains": "circuit"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C03IJKL9012"
      },
      "message_text": {
        "i_contains": "circuit"
      }
    },
    "expected_count": 0
  }
]
```

</details>

<a id="slack_108"></a>
## #52 — slack_108

Sophie and Mateo want to bring the workspace's food culture together under one roof — a "Midnight Bazaar" inspired by all those coffee and pizza conversations scattered around the channels. Dig through the workspace to find what food chatter has been going on and who's been part of it - specifically, search for the authors of the messages that contain the words "food" or "eat". That old archived channel nobody uses anymore — revive it and repurpose it as bazaar headquarters. Set a topic that captures the night-market vibe (needs to include the words "street food"), and write an opening post that weaves in whatever food discussions you find. While you're at it, some housekeeping: Mateo says he's drowning in #project-alpha-dev notifications and wants out — remove him. Also, that message about the espresso machine in #random? Edit it to plug the bazaar. And delete that stale message in #random asking about ordering "large pies" — the bazaar makes casual lunch plans obsolete.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L52) · [Cards](cards.md#slack_108)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the workspace’s food/eat discussion | resolved | `["1706052779.000000","1706115000.000001","1706115500.000001"]` | no | A3: The opening post’s destination is checked, but nothing in its content must reflect the food discussion. |
| 2. Resolve authors of food/eat messages | resolved | `["U_MATEO","U_KENJI","U_OLENA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve the old archived channel to revive | resolved | `["C_OLD_PROJECT"]` | yes | A1, A2, A3: Assertions 1, 2, 3 constrain the resulting change to this seeded referent. |
| 4. Resolve Mateo | resolved | `["U_MATEO"]` | yes | A4: Assertions 4 constrain the resulting change to this seeded referent. |
| 5. Resolve #project-alpha-dev | resolved | `["C06ALPHADEV"]` | yes | A4: Assertions 4 constrain the resulting change to this seeded referent. |
| 6. Resolve an espresso-machine message in #random | resolved | `["1706051580.000000","1706052433.000000"]` | partial | A5: A5 permits an edit to any message in random, including a non-espresso message. The resulting edited record need not belong to the card’s eligible espresso-message set. |
| 7. Resolve the large-pies lunch-planning message in #random | resolved | `["1706051755.000000"]` | yes | A6: Assertions 6 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The prompt explicitly supplies food and eat as words; whole-word matching avoids accidental matches in feature or great. Selection: Case-insensitive whole-word match for food or eat in message content.
- **2.** What food chatter and who participated are separately requested subjects; the same source messages support both. Selection: Select distinct authors of messages with whole-word food or eat.
- **3.** The seed has exactly one channel explicitly marked archived. Missing archive flags on other channels are not treated as independently observed runtime values. Selection: Select the explicitly archived channel in the seed.
- **4.** The prompt’s name resolves to Mateo Rivera in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Mateo Rivera'
- **5.** Resolve the named channel #project-alpha-dev; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha-dev'
- **6.** Permissive choose-one boundary: either of the two explicit espresso-machine messages is an eligible target; the task edits one, not both. Selection: Within random, select messages explicitly mentioning espresso.
- **7.** Within random, select content containing large pies.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": {
        "eq": "C_OLD_PROJECT"
      }
    },
    "expected_changes": {
      "is_archived": {
        "from": true,
        "to": false
      },
      "topic_text": {
        "to": {
          "i_contains": "street food"
        }
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C_OLD_PROJECT"
      },
      "user_id": {
        "eq": "U01AGENBOT9"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C_OLD_PROJECT"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": {
        "eq": "C06ALPHADEV"
      },
      "user_id": {
        "eq": "U_MATEO"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      }
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "i_contains": "bazaar"
        }
      }
    },
    "ignore": [
      "blocks"
    ],
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "removed",
    "entity": "messages",
    "where": {
      "channel_id": {
        "eq": "C02EFGH5678"
      },
      "message_text": {
        "i_contains": "large pies"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="slack_109"></a>
## #53 — slack_109

Aisha, Lukasz, Gabriel, Nick, and Priya want to launch a collaborative radio drama called "Phantom Frequencies" — a serialized fiction project where each person broadcasts a story from their timezone. They got the idea from all the talk about signal latency, CDN routing, and transmission in the workspace. Set them up with a channel called #phantom-frequencies, give it a topic that fits the concept (need to mention "Phantom Frequencies"), and get everyone in. Check Aisha's profile to confirm her timezone for the broadcast schedule, and DM her separately to ask about her episode's Lagos-blackout storyline. Write a first post in the channel that draws on whatever transmission and signal discussions you can find in the workspace. Also, that :eyes: reaction you left on the circuit-tracer message in #engineering — remove it, it's stale. There's a channel called #product-growth you're not in — pop in and check if there's anything about the APAC launch that could feed into the drama's world-building, then leave once you've got what you need. If you find in this chat a user with any user with a name that contains "incognito" ping them to change the nickname to "anything" - we need to maintain a trustful atmosphere here. And that #project-alpha channel that's basically just you — archive it, nobody's using it.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L53) · [Cards](cards.md#slack_109)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Aisha | resolved | `["U_AISHA"]` | partial | A2, A4: A2 requires five membership rows drawn from the five-person ID list, not one for each named person. A final membership set can omit this individual and use another listed person in multiple channels. The Lagos keyword also does not fix the private-message recipient or check a timezone assertion about Aisha. |
| 2. Resolve Lukasz | resolved | `["U_LUKAS"]` | partial | A2: A2 requires five membership rows drawn from the five-person ID list, not one for each named person. A final membership set can omit this individual and use another listed person in multiple channels. |
| 3. Resolve Gabriel | resolved | `["U09GABRIEL"]` | partial | A2: A2 requires five membership rows drawn from the five-person ID list, not one for each named person. A final membership set can omit this individual and use another listed person in multiple channels. |
| 4. Resolve Nick | resolved | `["U08NICK23"]` | partial | A2: A2 requires five membership rows drawn from the five-person ID list, not one for each named person. A final membership set can omit this individual and use another listed person in multiple channels. |
| 5. Resolve Priya | resolved | `["U_PRIYA"]` | partial | A2: A2 requires five membership rows drawn from the five-person ID list, not one for each named person. A final membership set can omit this individual and use another listed person in multiple channels. |
| 6. Resolve transmission and signal discussion sources | resolved | `["C02EFGH5678","C_INFRA","C_MODEL","C_GROWTH","C_FRONTEND"]` | no | A8: A generic actor-message count does not check the inspiration source. |
| 7. Resolve the actor’s eyes reaction on the engineering circuit-tracer root | resolved | `[{"message_id":"1706110000.000100","user_id":"U01AGENBOT9","reaction_type":"eyes"}]` | yes | A5: The removal predicate identifies the existing reaction by message and emoji; the seed contains just this reaction. |
| 8. Resolve #product-growth | resolved | `["C_GROWTH"]` | no | None: No assertion constrains this described referent or its derived result. |
| 9. Resolve the product-growth participant whose name contains incognito | resolved | `["U_INCOGNITO"]` | yes | A7: Assertion 7 fixes the user to U_INCOGNITO, although it checks a membership addition rather than the requested ping. |
| 10. Resolve #project-alpha | resolved | `["C05ALPHA"]` | yes | A6: Assertions 6 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to Aisha Okonkwo in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Aisha Okonkwo'
- **2.** The prompt’s name resolves to Łukasz Kowalski in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Łukasz Kowalski'
- **3.** The prompt’s name resolves to Gabriel Horn in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Gabriel Horn'
- **4.** The prompt’s name resolves to Nick Fury in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Nick Fury'
- **5.** The prompt’s name resolves to Priya Sharma in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Priya Sharma'
- **6.** Permissive thematic boundary: five histories contain latency, CDN, CloudFront, routing, network, or transmission discussion. This includes infrastructure and model-performance latency as well as network delivery. No individual-message relevance ranking is imposed. Selection: Select channels containing latency, CDN, CloudFront, routing, network, or transmission in message content; retain those conversations as broad inspiration sources.
- **7.** The message and its author/channel are qualifiers of this one described existing reaction; no additional optional lookup obligations are counted. Selection: Resolve the circuit-tracer root in engineering, then its eyes reaction by the acting user.
- **8.** The same named channel is used for joining, inspecting APAC discussion, and leaving; count it once. Selection: channels.channel_name == 'product-growth'
- **9.** The seed contains one matching participant, El Incognito. Coverage records the identity constraint; the mismatch in requested versus asserted operation is separately noted. Selection: Within product-growth members, select a display name containing incognito case-insensitively.
- **10.** Resolve the named channel #project-alpha; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha'
- Assertion 7 asks for a membership addition for Incognito although the prompt asks for a ping. Under the agreed assumption, count the identity constraint without treating it as proof of the requested operation. This is a visible source tension, not a new grounding obligation.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "channel_name": "phantom-frequencies",
      "topic_text": {
        "i_contains": "Phantom Frequencies"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "in": [
          "U_AISHA",
          "U_LUKAS",
          "U09GABRIEL",
          "U08NICK23",
          "U_PRIYA"
        ]
      }
    },
    "expected_count": {
      "min": 5
    }
  },
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": true
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "message_text": {
        "i_contains": "Lagos"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "removed",
    "entity": "message_reactions",
    "where": {
      "message_id": "1706110000.000100",
      "reaction_type": "eyes"
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": "C05ALPHA"
    },
    "expected_changes": {
      "is_archived": {
        "to": true
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": "U_INCOGNITO"
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": "U01AGENBOT9"
    },
    "expected_count": {
      "min": 3
    }
  }
]
```

</details>

<a id="slack_110"></a>
## #54 — slack_110

Hubert, John, Morgan, and Omer want to start a mapping project for forgotten underground rivers — they're calling it "Cartography of Lost Rivers". Pull up some details about #core-infra to see if that community would be a good match for cross-pollination. Now, "Morgan" — I mean the one who's been in the engineering discussions, not the other one. Also, that Morgan asked me to count all of the messages across all of the chats that mention the word "supercomputer." Do this please. Then create #lost-rivers-cartography, set a topic about mapping forgotten urban waterways, invite all four, and write a project manifesto as the opening post that will say: '"supercomputer" mentioned <your_count> number of times across all of the chats'. DM Morgan privately to ask whether they'd rather lead the cartography side or the field exploration. Lastly, find a message about infrastructure in #engineering and edit it to include a mention of the new project.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L54) · [Cards](cards.md#slack_110)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Hubert | resolved | `["U06HUBERT23"]` | partial | A2: A2 counts four membership rows with users drawn from four IDs; it does not require this particular person to appear. Repeated appearances of other permitted people in different channels can meet the aggregate condition. |
| 2. Resolve John | resolved | `["U02JOHNDOE1"]` | partial | A2: A2 counts four membership rows with users drawn from four IDs; it does not require this particular person to appear. Repeated appearances of other permitted people in different channels can meet the aggregate condition. |
| 3. Resolve Omer | resolved | `["U04OMER23"]` | partial | A2: A2 counts four membership rows with users drawn from four IDs; it does not require this particular person to appear. Repeated appearances of other permitted people in different channels can meet the aggregate condition. |
| 4. Resolve the Morgan participating in engineering discussions | resolved | `["U05MORGAN23"]` | yes | A2, A6: Assertion 6 independently requires two membership additions for U05MORGAN23. |
| 5. Resolve #core-infra | resolved | `["C_INFRA"]` | no | None: No assertion constrains this described referent or its derived result. |
| 6. Resolve all messages mentioning supercomputer | resolved | `["1706069700.000001","1706112500.000001"]` | partial | A3: A3 accepts "supercomputer mentioned 99 times; 2 reviewers checked this." The regex requires a later standalone 2 but does not bind it to the reported occurrence count. Checking the correct count would suffice without source message IDs; this predicate leaves the numeric claim unconstrained. |
| 7. Resolve an engineering message as the infrastructure-edit target | resolved | `["1699651200.000321","1699737600.000654","1699824000.000987","1699910400.000246","1700143200.000999","1700153200.000999","1706110000.000100","1706110000.000200","1706110000.000300","1706112500.000001","1706115000.000001"]` | yes | A7: The assertion fixes the edit to engineering, matching this explicitly broadened candidate boundary. |

Boundary and selection notes:

- **1.** The prompt’s name resolves to Hubert Marek in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Hubert Marek'
- **2.** The prompt’s name resolves to John Doe in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'John Doe'
- **3.** The prompt’s name resolves to Omer Narwhal in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Omer Narwhal'
- **4.** Morgan Stanley authored an engineering login message; Morgan Freeman did not. This is one person used for both invitation and a DM. Selection: Select users named Morgan who authored messages in engineering.
- **5.** Resolve the named channel #core-infra; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'core-infra'
- **6.** Case-insensitive whole-word supercomputer match across seeded accessible histories.
- **7.** Assertion-guided permissive boundary for the thematic phrase about infrastructure: select an eligible message from engineering, without claiming a unique subject-specific message. Exactly one is to be edited. Selection: Resolve engineering by name; retain its history as the permissive choose-one edit population.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "channel_name": "lost-rivers-cartography",
      "topic_text": {
        "i_contains": "waterway"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "in": [
          "U06HUBERT23",
          "U02JOHNDOE1",
          "U05MORGAN23",
          "U04OMER23"
        ]
      }
    },
    "expected_count": {
      "min": 4
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": "U01AGENBOT9",
      "message_text": {
        "regex": "(?i)supercomputer.*\\b2\\b"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": true
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": "U01AGENBOT9",
      "message_text": {
        "regex": "(?i)exploration"
      }
    },
    "expected_count": {
      "min": 1
    }
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": "U05MORGAN23"
    },
    "expected_count": {
      "min": 2
    }
  },
  {
    "diff_type": "changed",
    "entity": "messages",
    "where": {
      "channel_id": "C03IJKL9012"
    },
    "expected_changes": {
      "message_text": {
        "to": {
          "regex": "(?i)lost.rivers"
        }
      }
    },
    "ignore": [
      "blocks"
    ],
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": "U01AGENBOT9"
    },
    "expected_count": {
      "min": 2
    }
  }
]
```

</details>

<a id="slack_111"></a>
## #55 — slack_111

Kenji, Priya, Aisha, Sophie, Lukasz, and Mateo want to do a "Sunrise Relay" — a collaborative poetry chain where each person writes a verse when dawn breaks in their timezone, passing the baton westward as the sun moves around the earth. Pull up everyone's locale and timezone info so you can figure out the correct relay order from earliest sunrise to latest. Check what's been going on in #frontend for some creative inspiration to seed the poem's theme. Create a channel called #sunrise-relay, set the topic to the relay schedule showing each person and their timezone in sunrise order in exactly this format: "<username>: <timezone>\n" , invite all six, and post the full relay plan as the opening message. Drop a :sunrise: reaction on that schedule post. While you're looking at timezones, Mateo mentioned he can't keep up with #model-research because all the discussions happen during European hours and he's on Pacific time — pull him out of that channel. Oh, and rename #sunrise-relay to #dawn-chorus — the group decided the poem should be about birdsong at first light.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L55) · [Cards](cards.md#slack_111)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Kenji | resolved | `["U_KENJI"]` | partial | A1, A2, A3: A2’s aggregate invitation count does not force this individual’s inclusion. A1/A3 also allow timezone fragments without associating each person with the correct timezone in the schedule. Both gaps concern the resulting memberships or report, not profile-lookup activity. |
| 2. Resolve Priya | resolved | `["U_PRIYA"]` | partial | A1, A2, A3: A2’s aggregate invitation count does not force this individual’s inclusion. A1/A3 also allow timezone fragments without associating each person with the correct timezone in the schedule. Both gaps concern the resulting memberships or report, not profile-lookup activity. |
| 3. Resolve Aisha | resolved | `["U_AISHA"]` | partial | A1, A2, A3: A2’s aggregate invitation count does not force this individual’s inclusion. A1/A3 also allow timezone fragments without associating each person with the correct timezone in the schedule. Both gaps concern the resulting memberships or report, not profile-lookup activity. |
| 4. Resolve Sophie | resolved | `["U_SOPHIE"]` | partial | A1, A2, A3: A2’s aggregate invitation count does not force this individual’s inclusion. A1/A3 also allow timezone fragments without associating each person with the correct timezone in the schedule. Both gaps concern the resulting memberships or report, not profile-lookup activity. |
| 5. Resolve Lukasz | resolved | `["U_LUKAS"]` | partial | A1, A2, A3: A2’s aggregate invitation count does not force this individual’s inclusion. A1/A3 also allow timezone fragments without associating each person with the correct timezone in the schedule. Both gaps concern the resulting memberships or report, not profile-lookup activity. |
| 6. Resolve Mateo | resolved | `["U_MATEO"]` | yes | A2, A5: The removal assertion fixes Mateo’s identity. |
| 7. Resolve #frontend | resolved | `["C_FRONTEND"]` | no | None: No assertion constrains this described referent or its derived result. |
| 8. Resolve #model-research | resolved | `["C_MODEL"]` | yes | A5: Assertions 5 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- Card protocol: v1.0.1.
- **1.** The prompt’s name resolves to 佐藤健二 (Kenji Sato) in the seed. This is one described person even when used repeatedly. Selection: users.real_name == '佐藤健二 (Kenji Sato)'
- **2.** The prompt’s name resolves to Priya Sharma in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Priya Sharma'
- **3.** The prompt’s name resolves to Aisha Okonkwo in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Aisha Okonkwo'
- **4.** The prompt’s name resolves to Sophie Dubois in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Sophie Dubois'
- **5.** The prompt’s name resolves to Łukasz Kowalski in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Łukasz Kowalski'
- **6.** The prompt’s name resolves to Mateo Rivera in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Mateo Rivera'
- **7.** Resolve the named channel #frontend; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'frontend'
- **8.** Resolve the named channel #model-research; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'model-research'
- The schedule post and newly created/renamed channel are generated during this task and introduce no existing-referent obligations. Reusing named participants for timezone lookup, invitations, and removal does not multiply their obligations.
- Protocol v1.0.1 review: all six named participants and the two named existing channels have determined referents. Requests to inspect timezones, invite the same people, and remove Mateo reuse those identities. The schedule post and renamed channel arise during the task, so uncertainty about downstream scheduling does not create an underspecified initial referent. All eight cards remain resolved, with unchanged coverage.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "channel_name": "dawn-chorus",
      "topic_text": {
        "regex": "(?s)(?=.*Lagos)(?=.*Warsaw)(?=.*Paris)Tokyo.*Kolkata.*Los_Angeles"
      }
    },
    "expected_count": 1,
    "description": "Channel created as #sunrise-relay and renamed to #dawn-chorus, topic has relay schedule with all 6 timezones in correct east-to-west sunrise order"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "in": [
          "U_KENJI",
          "U_PRIYA",
          "U_AISHA",
          "U_LUKAS",
          "U_SOPHIE",
          "U_MATEO"
        ]
      }
    },
    "expected_count": {
      "min": 6
    },
    "description": "All 6 relay participants invited to the new channel"
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": "U01AGENBOT9",
      "message_text": {
        "regex": "(?s)(?=.*Tokyo)(?=.*Los_Angeles)"
      }
    },
    "expected_count": {
      "min": 1
    },
    "description": "Agent posted the full relay plan as opening message with timezone references"
  },
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "reaction_type": "sunrise"
    },
    "expected_count": 1,
    "description": ":sunrise: reaction dropped on the schedule post"
  },
  {
    "diff_type": "removed",
    "entity": "channel_members",
    "where": {
      "channel_id": "C_MODEL",
      "user_id": "U_MATEO"
    },
    "expected_count": 1,
    "description": "Mateo removed from #model-research due to Pacific timezone mismatch with European discussion hours"
  }
]
```

</details>

<a id="slack_112"></a>
## #56 — slack_112

Hubert does this thing he calls the "Apiary Report" — he sees the workspace as a beehive, and he wants a quarterly survey. First he needs the full picture: how many honeycomb cells does this hive have, and which ones are alive? Then go taste the honey in #growth — read through whatever's been happening there. Find the sweetest drop — the single best message — and mark it with a :honey_pot:. That's Hubert's forager tradition. Once you've done your tasting, write up a Forager's Report and post it in #random for the rest of the colony, summarizing whatever noteworthy conversation you found in #growth. Note, that the report must contain the words "FORAGERS REPORT". Last thing: #project-alpha is an empty cell. Nobody's in it, nothing's happening. Seal it off.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L56) · [Cards](cards.md#slack_112)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the workspace’s channels for the hive survey | resolved | `["C01ABCD1234","C02EFGH5678","C03IJKL9012","C04MNOP3456","C05ALPHA","C06ALPHADEV","C_INFRA","C_MODEL","C_GROWTH","C_FRONTEND","C_OLD_PROJECT"]` | no | None: No assertion constrains this described referent or its derived result. |
| 2. Resolve #growth | resolved | `["C04MNOP3456"]` | no | None: No assertion constrains this described referent or its derived result. |
| 3. Resolve an eligible growth message for the honey-pot reaction | resolved | `["1700300000.000001","1700300060.000002","1700300120.000003","1700300180.000004","1700300240.000005","1700300300.000006"]` | yes | A1: The reaction must target one of the six seeded growth messages, exactly the permissive eligible set. |
| 4. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A2: Assertions 2 constrain the resulting change to this seeded referent. |
| 5. Resolve #project-alpha | resolved | `["C05ALPHA"]` | yes | A3: Assertions 3 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- Card protocol: v1.0.1.
- **1.** Honeycomb cells are explicitly metaphorical channels; the whole channel population is one set obligation. Selection: Select public non-DM channels; retain archived channels for the active-versus-inactive survey.
- **2.** Resolve growth as the broad source for the Forager’s Report. The assertion only requires the report label, not its source-derived content. Selection: channels.channel_name == 'growth'
- **3.** The prompt asks to “find the sweetest drop — the single best message” in growth, explicitly delegating the choice to the agent. Choose one of the six eligible growth messages for the honey-pot reaction. The assertion supports this permissive eligible population; it does not supply the delegation. Six eligible referents mean one requested reaction, not six. Selection: Resolve growth by name; retain all six messages as eligible targets; choose one for the reaction.
- **4.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'
- **5.** Resolve the named channel #project-alpha; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha'
- Protocol v1.0.1 review: the best-message request delegates a choice, unlike Slack 98’s reference to Aisha’s remembered great message. The eligible set remains resolved and fully covered; no ranking or canonical best message is invented.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "message_reactions",
    "where": {
      "reaction_type": "honey_pot",
      "user_id": "U01AGENBOT9",
      "message_id": {
        "in": [
          "1700300000.000001",
          "1700300060.000002",
          "1700300120.000003",
          "1700300180.000004",
          "1700300240.000005",
          "1700300300.000006"
        ]
      }
    },
    "expected_count": 1,
    "description": ":honey_pot: reaction added to a message in #growth channel"
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": "C02EFGH5678",
      "user_id": "U01AGENBOT9",
      "message_text": {
        "contains": "FORAGERS REPORT"
      }
    },
    "expected_count": 1,
    "description": "Forager's Report posted to #random with required phrase"
  },
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": "C05ALPHA"
    },
    "expected_count": 1,
    "expected_changes": {
      "is_archived": {
        "from": false,
        "to": true
      }
    },
    "description": "#project-alpha archived (empty cell sealed)"
  }
]
```

</details>

<a id="slack_113"></a>
## #57 — slack_113

Think of the workspace as a coastline full of tide pools — each channel is its own micro-ecosystem, and you're the naturalist on a field survey. Start by pulling a roster of every organism on this coast and classify them into two species: "admin" and "member." How many of each do you count? You need to sort the channel names in alphabetic order and send a message to Omer, in exactly this format: "Field Repoert 1: <channel_name>: [<admins_count>, <members_count>]". Then inspect #engineering. Probe under the circuit-tracer rock in that channel — there's a thread with replies most people never noticed. Count exactly how many replies are down there and note who left them. Over in #random, that message about coordinating lunch plans is an invasive species — remove it. And whoever originally posted that circuit-tracer message in #engineering — open a private channel with them and send them a field report formatted exactly like this: "Field Report 2: [N] replies found under circuit-tracer in #engineering — organisms: [comma-separated names of repliers]".

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L57) · [Cards](cards.md#slack_113)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the workspace channel population for the alphabetical survey | resolved | `["C01ABCD1234","C02EFGH5678","C03IJKL9012","C04MNOP3456","C05ALPHA","C06ALPHADEV","C_INFRA","C_MODEL","C_GROWTH","C_FRONTEND","C_OLD_PROJECT"]` | partial | A2: A2 permits a report containing only nine channel names, with product-growth and the archived channel omitted from the card’s adopted eleven-channel population. The final survey can therefore be incomplete. |
| 2. Resolve the workspace user roster for admin/member classification | resolved | `["U01AGENBOT9","U02JOHNDOE1","U02ARTEM23","U03ROBERT23","U04OMER23","U05MORGAN23","U06HUBERT23","U07MORGANFREE","U08NICK23","U09GABRIEL","U_PRIYA","U_LUKAS","U_SOPHIE","U_OLENA","U_MATEO","U_KENJI","U_ROBERT","U_AISHA","U_INCOGNITO"]` | partial | A2: The requested roster-derived result is the per-channel admin/member survey. A2 constrains counts for nine channels but omits two channels in the adopted population; their counts and members’ contribution can be omitted. Individual user IDs or a displayed full roster are not independently required for checking this aggregate result. |
| 3. Resolve Omer | resolved | `["U04OMER23"]` | yes | A1: Assertions 1 constrain the resulting change to this seeded referent. |
| 4. Resolve replies under the engineering circuit-tracer root | resolved | `["1706110000.000200","1706110000.000300"]` | partial | A5: A5 checks two replies and later Robert/Kenji substrings, but accepts "Field Report 2: 2 replies found under circuit-tracer in #engineering — organisms: Robert, Aisha. Report prepared by Kenji." It need not report the correct pair of authors. Reply IDs and retrieval provenance are unnecessary; the author attribution in the final report is the gap. |
| 5. Resolve a lunch-coordination message in #random | resolved | `["1699572000.000789","1706051755.000000","1706052665.000000","1706053102.000000"]` | yes | A3: The removal assertion selects exactly this permissive channel-and-content candidate population. |
| 6. Resolve the author of the original engineering circuit-tracer message | resolved | `["U_LUKAS"]` | yes | A4: A membership addition for U_LUKAS is explicitly required. The report’s delivery to that same conversation is not enforced. |

Boundary and selection notes:

- **1.** Channels across the coastline are a separately described set needed to organize the per-channel report. Retain the broad seeded public-channel population; do not silently delete omitted channels to fit the answer. Selection: Select public non-DM channels.
- **2.** Select all seeded workspace users.
- **3.** The prompt’s name resolves to Omer Narwhal in the seed. This is one described person even when used repeatedly. Selection: users.real_name == 'Omer Narwhal'
- **4.** The count and author list are computations over one described reply set. No separate optional user-lookup obligations are added. Selection: Resolve the engineering circuit-tracer root, then select messages whose parent_id is that root.
- **5.** Assertion-guided choose-one boundary. The prompt’s singular lunch-coordination description is not forced into an arbitrary unique message. Selection: Within random, select messages containing lunch; choose one for deletion.
- **6.** Within engineering, identify the circuit-tracer root about layer-by-layer loading and return its author.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": "U04OMER23"
    },
    "expected_count": 1,
    "description": "DM channel opened with Omer to deliver the channel survey (Field Report 1)"
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": "U01AGENBOT9",
      "message_text": {
        "regex": "(?s)Field Repoert 1.*core-infra[^\\n]*\\[0,\\s*9\\].*engineering[^\\n]*\\[1,\\s*4\\].*frontend[^\\n]*\\[0,\\s*9\\].*general[^\\n]*\\[1,\\s*2\\].*growth[^\\n]*\\[0,\\s*4\\].*model-research[^\\n]*\\[0,\\s*9\\].*project-alpha[^\\n]*\\[0,\\s*1\\].*project-alpha-dev[^\\n]*\\[0,\\s*7\\].*random[^\\n]*\\[1,\\s*3\\]"
      }
    },
    "expected_count": 1,
    "description": "Field Report 1 sent to Omer listing all channels alphabetically with correct per-channel admin/member counts (engineering [1,4], general [1,2], random [1,3], project-alpha-dev [0,7], etc.)"
  },
  {
    "diff_type": "removed",
    "entity": "messages",
    "where": {
      "channel_id": "C02EFGH5678",
      "message_text": {
        "i_contains": "lunch"
      }
    },
    "expected_count": 1,
    "description": "Lunch coordination message removed from #random — invasive species eliminated"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": "U_LUKAS"
    },
    "expected_count": 1,
    "description": "DM opened with Lukasz (U_LUKAS) — the original poster of the circuit-tracer message in #engineering"
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "user_id": "U01AGENBOT9",
      "message_text": {
        "regex": "(?si)Field Report 2:\\s*\\[?2\\]?\\s+repl.*circuit-tracer.*robert.*kenji"
      }
    },
    "expected_count": 1,
    "description": "Field Report 2 sent to circuit-tracer poster reporting exactly 2 replies by Robert and Kenji under the circuit-tracer thread"
  }
]
```

</details>

<a id="slack_114"></a>
## #58 — slack_114

Robert and Nick want to do a "Palimpsest" — scraping off old marks in the workspace and writing over them with new ones. First, check what channels Nick is actually in — Robert suspects he's barely present anywhere. Count them. Then scrape off that :eyes: reaction you left on the circuit-tracer message in #engineering — it's old ink that needs to go. That lonely #project-alpha channel? Overwrite its name — rename it to #palimpsest-archive, it's being repurposed as a record of overwritten things. Finally, write the new text: post a message in #random that says exactly "PALIMPSEST COMPLETE: [N] channels found for Nick" where [N] is however many channels Nick turned out to be in.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L58) · [Cards](cards.md#slack_114)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve conversations Nick belongs to | resolved | `["C04MNOP3456"]` | yes | A3: A3 binds the count 1 to the requested "PALIMPSEST COMPLETE ... channels found for Nick" statement in random. One is the seed-derived answer. The underlying channel need not be named, and there is no requirement to expose source IDs or retrieval activity. |
| 2. Resolve the actor’s eyes reaction on the engineering circuit-tracer root | resolved | `[{"message_id":"1706110000.000100","user_id":"U01AGENBOT9","reaction_type":"eyes"}]` | yes | A1: The removal predicate identifies the existing reaction by message and emoji and acting user. |
| 3. Resolve #project-alpha | resolved | `["C05ALPHA"]` | yes | A2: Assertions 2 constrain the resulting change to this seeded referent. |
| 4. Resolve #random | resolved | `["C02EFGH5678"]` | yes | A3: Assertions 3 constrain the resulting change to this seeded referent. |

Boundary and selection notes:

- **1.** Nick qualifies the requested channel set; a separate Nick lookup is not another independently requested subject. Selection: Resolve Nick Fury by real_name; select his memberships and return their channel IDs.
- **2.** The message and its author/channel are qualifiers of this one described existing reaction; no additional optional lookup obligations are counted. Selection: Resolve the circuit-tracer root in engineering, then its eyes reaction by the acting user.
- **3.** Resolve the named channel #project-alpha; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'project-alpha'
- **4.** Resolve the named channel #random; its name selects one seeded conversation. Repeated uses in the task share this obligation. Selection: channels.channel_name == 'random'

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "removed",
    "entity": "message_reactions",
    "where": {
      "message_id": "1706110000.000100",
      "user_id": "U01AGENBOT9",
      "reaction_type": "eyes"
    },
    "expected_count": 1,
    "description": "Agent's :eyes: reaction removed from circuit-tracer message in #engineering — old ink scraped off"
  },
  {
    "diff_type": "changed",
    "entity": "channels",
    "where": {
      "channel_id": "C05ALPHA"
    },
    "expected_count": 1,
    "expected_changes": {
      "channel_name": {
        "from": "project-alpha",
        "to": "palimpsest-archive"
      }
    },
    "description": "#project-alpha renamed to #palimpsest-archive — overwritten with new purpose"
  },
  {
    "diff_type": "added",
    "entity": "messages",
    "where": {
      "channel_id": "C02EFGH5678",
      "user_id": "U01AGENBOT9",
      "message_text": {
        "regex": "PALIMPSEST COMPLETE:\\s*1\\s+channels?\\s+found\\s+for\\s+Nick"
      }
    },
    "expected_count": 1,
    "description": "Palimpsest record posted in #random: 'PALIMPSEST COMPLETE: 1 channel(s) found for Nick' — Nick is only in #growth"
  }
]
```

</details>

<a id="slack_115"></a>
## #59 — slack_115

How many active private conversations do I have? If I have less than seven conversations, please create new conversations with the users one by one in alphabetic order, skipping those with whom I already have conversations. If I have more than seven conversations, start removing conversations with those in alphabetic order until I have exactly seven conversations.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L59) · [Cards](cards.md#slack_115)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the actor’s existing active private conversations | resolved | `["D01AGENTSOPHIE"]` | partial | A1: A1 constrains six DM additions, but the listed predicates do not ensure that the resulting state contains exactly seven active private conversations for the actor. Preservation/activity/membership of the final conversation population is not checked. Naming the initial Sophie DM or proving it was counted is unnecessary. |
| 2. Resolve the alphabetically first eligible users for new conversations | resolved | `["U_AISHA","U02ARTEM23","U_INCOGNITO","U09GABRIEL","U06HUBERT23","U02JOHNDOE1"]` | partial | A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12: The output-state predicates forbid eleven user IDs and count six DM additions, but do not ensure the final six new conversations are with the intended six distinct eligible counterparts, skipping existing conversations. The missing constraint is the final recipient/conversation relationship, not the order of API calls or a sorting trace. |

Boundary and selection notes:

- **1.** The seed’s only private conversation is the actor–Sophie DM. Treat it as the existing conversation for this seed-level analysis; no implementation defaults are inspected. Selection: Select seeded DMs with an acting-user membership. The seed has one DM and no explicit closed-DM state.
- **2.** The first six sorted real names are Aisha, Artem, Carlos, Gabriel, Hubert, John; the assertion description corroborates these identities. The removal branch is inactive in this seed and adds no instance-specific target set. Selection: Sort users by real_name case-insensitively, excluding the actor and existing DM counterpart Sophie, and select the first 7 minus current-DM-count users.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "channels",
    "where": {
      "is_dm": {
        "eq": true
      }
    },
    "expected_count": 6,
    "description": "6 new DM channels created to reach target of 7 private conversations (Agent started with 1 DM with Sophie, needs DMs with: Aisha, Artem, Carlos, Gabriel, Hubert, John — first 6 alphabetically excluding Sophie)"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_LUKAS"
      }
    },
    "expected_count": 0,
    "description": "Łukasz (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_MATEO"
      }
    },
    "expected_count": 0,
    "description": "Mateo (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U07MORGANFREE"
      }
    },
    "expected_count": 0,
    "description": "Morgan Freeman (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U05MORGAN23"
      }
    },
    "expected_count": 0,
    "description": "Morgan Stanley (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U08NICK23"
      }
    },
    "expected_count": 0,
    "description": "Nick (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_OLENA"
      }
    },
    "expected_count": 0,
    "description": "Olena (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U04OMER23"
      }
    },
    "expected_count": 0,
    "description": "Omer (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_PRIYA"
      }
    },
    "expected_count": 0,
    "description": "Priya (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_ROBERT"
      }
    },
    "expected_count": 0,
    "description": "Robert Chen (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U03ROBERT23"
      }
    },
    "expected_count": 0,
    "description": "Robert Walsh (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  },
  {
    "diff_type": "added",
    "entity": "channel_members",
    "where": {
      "user_id": {
        "eq": "U_KENJI"
      }
    },
    "expected_count": 0,
    "description": "Kenji (alphabetically after John) should NOT be added — agent stops at 7 conversations"
  }
]
```

</details>
