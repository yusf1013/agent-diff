# Linear grounding obligations

See [method and source policy](README.md). These are benchmark annotations, not measurements of agent behavior. Cards use the locked schema in [cards.md](cards.md).

57 tests; 143 task-expressed obligations: 139 resolved, 4 absent, 0 underspecified. Assertions fully cover 115, partially cover 8, and leave 20 unchecked.

Coverage concerns the grounded contribution in the final state or requested output; it never requires a trajectory or source provenance. Full coverage does not certify whole-task correctness. See [the focused coverage audit](coverage_audit.md). The denominator includes unresolved and absent obligations. Zero-obligation tasks have no coverage ratio.

| # | Test | Obligations | Resolved | Absent | Underspecified | Full | Partial | Unchecked |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 108 | [linear_0](#linear_0) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 109 | [linear_1](#linear_1) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 110 | [linear_2](#linear_2) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 111 | [linear_3](#linear_3) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 112 | [linear_4](#linear_4) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 113 | [linear_5](#linear_5) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 114 | [linear_6](#linear_6) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 115 | [linear_7](#linear_7) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 116 | [linear_8](#linear_8) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 117 | [linear_9](#linear_9) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 118 | [linear_10](#linear_10) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 119 | [linear_11](#linear_11) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 120 | [linear_12](#linear_12) | 2 | 1 | 1 | 0 | 1 | 0 | 1 |
| 121 | [linear_13](#linear_13) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 122 | [linear_14](#linear_14) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 123 | [linear_15](#linear_15) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 124 | [linear_16](#linear_16) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 125 | [linear_17](#linear_17) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 126 | [linear_18](#linear_18) | 3 | 3 | 0 | 0 | 1 | 0 | 2 |
| 127 | [linear_19](#linear_19) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 128 | [linear_20](#linear_20) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 129 | [linear_21](#linear_21) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 130 | [linear_22](#linear_22) | 3 | 3 | 0 | 0 | 1 | 0 | 2 |
| 131 | [linear_23](#linear_23) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 132 | [linear_24](#linear_24) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 133 | [linear_25](#linear_25) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 134 | [linear_26](#linear_26) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 135 | [linear_27](#linear_27) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 136 | [linear_28](#linear_28) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 137 | [linear_29](#linear_29) | 2 | 1 | 1 | 0 | 1 | 0 | 1 |
| 138 | [linear_30](#linear_30) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 139 | [linear_31](#linear_31) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 140 | [linear_32](#linear_32) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 141 | [linear_33](#linear_33) | 3 | 2 | 1 | 0 | 2 | 0 | 1 |
| 142 | [linear_34](#linear_34) | 3 | 3 | 0 | 0 | 0 | 1 | 2 |
| 143 | [linear_35](#linear_35) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 144 | [linear_36](#linear_36) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 145 | [linear_37](#linear_37) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 146 | [linear_38](#linear_38) | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 147 | [linear_39](#linear_39) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 148 | [linear_40](#linear_40) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 149 | [linear_41](#linear_41) | 6 | 6 | 0 | 0 | 4 | 2 | 0 |
| 150 | [linear_42](#linear_42) | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 151 | [linear_43](#linear_43) | 4 | 4 | 0 | 0 | 4 | 0 | 0 |
| 152 | [linear_44](#linear_44) | 5 | 4 | 1 | 0 | 2 | 0 | 3 |
| 153 | [linear_45](#linear_45) | 4 | 4 | 0 | 0 | 4 | 0 | 0 |
| 154 | [linear_46](#linear_46) | 4 | 4 | 0 | 0 | 4 | 0 | 0 |
| 155 | [linear_47](#linear_47) | 5 | 5 | 0 | 0 | 4 | 0 | 1 |
| 156 | [linear_48](#linear_48) | 7 | 7 | 0 | 0 | 3 | 1 | 3 |
| 157 | [linear_49](#linear_49) | 8 | 8 | 0 | 0 | 8 | 0 | 0 |
| 158 | [linear_50](#linear_50) | 3 | 3 | 0 | 0 | 2 | 0 | 1 |
| 159 | [linear_51](#linear_51) | 4 | 4 | 0 | 0 | 4 | 0 | 0 |
| 160 | [linear_52](#linear_52) | 8 | 8 | 0 | 0 | 8 | 0 | 0 |
| 161 | [linear_53](#linear_53) | 5 | 5 | 0 | 0 | 4 | 0 | 1 |
| 162 | [linear_54](#linear_54) | 5 | 5 | 0 | 0 | 2 | 2 | 1 |
| 163 | [linear_55](#linear_55) | 4 | 4 | 0 | 0 | 3 | 1 | 0 |
| 164 | [linear_56](#linear_56) | 3 | 3 | 0 | 0 | 2 | 0 | 1 |

<a id="linear_0"></a>
## #108 — linear_0

Create a new issue in the Engineering team titled 'Fix login bug' 

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L108) · [Cards](cards.md#linear_0)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      },
      "title": {
        "contains": "login bug"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_1"></a>
## #109 — linear_1

Create a new issue in the Engineering team titled 'Fix login bug' with high priority

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L109) · [Cards](cards.md#linear_1)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      },
      "title": {
        "contains": "login bug"
      },
      "priority": {
        "eq": 2.0
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_2"></a>
## #110 — linear_2

Move issue ENG-1 to 'In Progress' status

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L110) · [Cards](cards.md#linear_2)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-1 | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Engineering In Progress workflow state | resolved | `["6963a682-5967-477a-9afc-0b8a5b70b070"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-1. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-1"]. Selection: Select issues by issues.identifier matching ["ENG-1"].
- **2.** Resolve Engineering In Progress workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'In Progress' in Engineering; the target issue/team establishes this team context. Selection: Select workflow state 'In Progress' in Engineering; the target issue/team establishes this team context.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "6963a682-5967-477a-9afc-0b8a5b70b070"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_3"></a>
## #111 — linear_3

Assign issue ENG-2 to John Doe

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L111) · [Cards](cards.md#linear_3)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-2 | resolved | `["5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve John Doe | resolved | `["2dcc8dc2-ca19-475d-9882-3ba5e911e7ec"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-2. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-2"]. Selection: Select issues by issues.identifier matching ["ENG-2"].
- **2.** Resolve John Doe. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["John Doe"]. Selection: Select users by users.name, users.displayName matching ["John Doe"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-2"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "from": {
          "eq": "03b0809e-713e-44ee-95de-b7a198b135ac"
        },
        "to": {
          "eq": "2dcc8dc2-ca19-475d-9882-3ba5e911e7ec"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_4"></a>
## #112 — linear_4

Add a comment to issue ENG-1 saying 'I am working on this now'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L112) · [Cards](cards.md#linear_4)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-1 | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-1. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-1"]. Selection: Select issues by issues.identifier matching ["ENG-1"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "issueId": {
        "eq": "c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"
      },
      "body": {
        "contains": "working on this"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_5"></a>
## #113 — linear_5

Create a new team called 'Design'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L113) · [Cards](cards.md#linear_5)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| No existing-referent obligation | — | — | N/A | Only new outputs or supplied context; see notes |

Boundary and selection notes:

- Design already exists in this expanded seed, but the prompt explicitly requests creation of a new team. No existing Design lookup or automatic Backlog state is a requested initial-state subject.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "teams",
    "where": {
      "name": {
        "eq": "Design"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "workflow_states",
    "where": {
      "name": {
        "eq": "Backlog"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_6"></a>
## #114 — linear_6

Change the priority of issue ENG-1 to Urgent

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L114) · [Cards](cards.md#linear_6)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-1 | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-1. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-1"]. Selection: Select issues by issues.identifier matching ["ENG-1"].
- Urgent is the documented priority enum, not the separately named Urgent issue-label entity.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_changes": {
      "priority": {
        "to": {
          "eq": 1.0
        }
      },
      "priorityLabel": {
        "to": {
          "eq": "Urgent"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_7"></a>
## #115 — linear_7

Create a new issue 'Improve performance' in Engineering team, assign to John, with description 'Optimize database queries'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L115) · [Cards](cards.md#linear_7)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve John | resolved | `["2dcc8dc2-ca19-475d-9882-3ba5e911e7ec"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].
- **2.** Resolve John. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["John Doe"]. Selection: Select users by users.name, users.displayName matching ["John Doe"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      },
      "title": {
        "contains": "performance"
      },
      "assigneeId": {
        "eq": "2dcc8dc2-ca19-475d-9882-3ba5e911e7ec"
      },
      "description": {
        "contains": "database queries"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_8"></a>
## #116 — linear_8

Update the description of issue ENG-1 to include 'Root cause: session timeout issue'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L116) · [Cards](cards.md#linear_8)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-1 | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-1. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-1"]. Selection: Select issues by issues.identifier matching ["ENG-1"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "contains": "session timeout"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_9"></a>
## #117 — linear_9

Create three new issues in the Engineering team: 'Update documentation', 'Refactor API endpoints', and 'Add unit tests'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L117) · [Cards](cards.md#linear_9)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      }
    },
    "expected_count": 3
  }
]
```

</details>

<a id="linear_10"></a>
## #118 — linear_10

Mark issue ENG-1 as completed

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L118) · [Cards](cards.md#linear_10)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-1 | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Engineering Done workflow state | resolved | `["4334c4ee-405c-4d2c-bf25-4dcb7a8c0512"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-1. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-1"]. Selection: Select issues by issues.identifier matching ["ENG-1"].
- **2.** Resolve Engineering Done workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Done' in Engineering; the target issue/team establishes this team context. Selection: Select workflow state 'Done' in Engineering; the target issue/team establishes this team context.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "4334c4ee-405c-4d2c-bf25-4dcb7a8c0512"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_11"></a>
## #119 — linear_11

Create a new label called 'Bugs' 

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L119) · [Cards](cards.md#linear_11)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| No existing-referent obligation | — | — | N/A | Only new outputs or supplied context; see notes |

Boundary and selection notes:

- The prompt creates a new label; no existing referent is requested.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "Bugs"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_12"></a>
## #120 — linear_12

Add the newly created 'Bugs' label to the Engineering login issue currently assigned to John Doe.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L120) · [Cards](cards.md#linear_12)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the Engineering login issue assigned to John | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Bugs label | absent | `[]` | no | None: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve the Engineering login issue assigned to John. Use the described subject and the supported seed-level selector. Select the Engineering login issue assigned to John Doe; ENG-1 matches. Selection: Select the Engineering login issue assigned to John Doe; ENG-1 matches.
- **2.** Resolve Bugs label. The explicit description has no matching seeded referent. Select issue_labels by issue_labels.name matching []. Selection: Select issue_labels by issue_labels.name matching [].
- Every entry initializes from linear_expanded. The label created in linear_11 is not carried forward; no Bugs label exists here. The issue is selected by its login topic, Engineering team, and John Doe assignee; John is a qualifier.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {
      "issue_id": {
        "eq": "c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_13"></a>
## #121 — linear_13

Add the 'UX' label to the onboarding dashboard issue that Sarah Smith owns.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L121) · [Cards](cards.md#linear_13)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Sarah’s onboarding dashboard issue | resolved | `["5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve UX label | resolved | `["f9c5b7c8-3909-4f8b-bc25-73e1b56a9c0c"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Sarah’s onboarding dashboard issue. Use the described subject and the supported seed-level selector. Select the onboarding dashboard issue assigned to Sarah Smith. Selection: Select the onboarding dashboard issue assigned to Sarah Smith.
- **2.** Resolve UX label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["UX"]. Selection: Select issue_labels by issue_labels.name matching ["UX"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {
      "issue_id": {
        "eq": "5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f"
      },
      "issue_label_id": {
        "eq": "f9c5b7c8-3909-4f8b-bc25-73e1b56a9c0c"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_14"></a>
## #122 — linear_14

Rename the Engineering issue describing intermittent login failures to 'Fix login bug - follow up'.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L122) · [Cards](cards.md#linear_14)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the Engineering intermittent-login issue | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve the Engineering intermittent-login issue. Use the described subject and the supported seed-level selector. Select the Engineering issue describing intermittent login failures. Selection: Select the Engineering issue describing intermittent login failures.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_changes": {
      "title": {
        "to": {
          "contains": "follow up"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_15"></a>
## #123 — linear_15

Add the 'RL' label to the login issue that John Doe recently commented on.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L123) · [Cards](cards.md#linear_15)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the login issue John commented on | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve RL label | resolved | `["8f01ce9d-1433-4c4c-969d-21ca3bf2718f"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve the login issue John commented on. Use the described subject and the supported seed-level selector. Join John Doe’s comment to its login issue; no reference date is required to distinguish the unique matching commented login issue. Selection: Join John Doe’s comment to its login issue; no reference date is required to distinguish the unique matching commented login issue.
- **2.** Resolve RL label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["RL"]. Selection: Select issue_labels by issue_labels.name matching ["RL"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {
      "issue_id": {
        "eq": "c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"
      },
      "issue_label_id": {
        "eq": "8f01ce9d-1433-4c4c-969d-21ca3bf2718f"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_16"></a>
## #124 — linear_16

Move issue ENG-2 to 'In Review'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L124) · [Cards](cards.md#linear_16)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-2 | resolved | `["5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Engineering In Review workflow state | resolved | `["4379b3d7-1143-4aa4-a3a6-da0c436e73b6"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-2. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-2"]. Selection: Select issues by issues.identifier matching ["ENG-2"].
- **2.** Resolve Engineering In Review workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'In Review' in Engineering; the target issue/team establishes this team context. Selection: Select workflow state 'In Review' in Engineering; the target issue/team establishes this team context.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-2"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "4379b3d7-1143-4aa4-a3a6-da0c436e73b6"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_17"></a>
## #125 — linear_17

Assign ENG-3 to Sarah Smith

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L125) · [Cards](cards.md#linear_17)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-3 | resolved | `["87c1d2f3-66c4-4dd0-bc93-1b99d04dc374"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Sarah Smith | resolved | `["03b0809e-713e-44ee-95de-b7a198b135ac"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-3. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-3"]. Selection: Select issues by issues.identifier matching ["ENG-3"].
- **2.** Resolve Sarah Smith. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Sarah Smith"]. Selection: Select users by users.name, users.displayName matching ["Sarah Smith"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-3"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "to": {
          "eq": "03b0809e-713e-44ee-95de-b7a198b135ac"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_18"></a>
## #126 — linear_18

Create a new Engineering issue 'Polish navigation' with labels 'UX' and 'Urgent'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L126) · [Cards](cards.md#linear_18)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve UX label | resolved | `["f9c5b7c8-3909-4f8b-bc25-73e1b56a9c0c"]` | no | A2: No assertion constrains this subject or its requested source-derived result. |
| 3. Resolve Urgent label | resolved | `["6c2b0d3c-3d6d-4d91-9a77-b93b59b8d5a0"]` | no | A2: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].
- **2.** Resolve UX label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["UX"]. Selection: Select issue_labels by issue_labels.name matching ["UX"].
- **3.** Resolve Urgent label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["Urgent"]. Selection: Select issue_labels by issue_labels.name matching ["Urgent"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      },
      "title": {
        "contains": "Polish navigation"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {},
    "expected_count": {
      "min": 2
    }
  }
]
```

</details>

<a id="linear_19"></a>
## #127 — linear_19

Add a comment to ENG-3: 'Please add logs for the error path'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L127) · [Cards](cards.md#linear_19)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-3 | resolved | `["87c1d2f3-66c4-4dd0-bc93-1b99d04dc374"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-3. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-3"]. Selection: Select issues by issues.identifier matching ["ENG-3"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "issueId": {
        "eq": "87c1d2f3-66c4-4dd0-bc93-1b99d04dc374"
      },
      "body": {
        "contains": "error path"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_20"></a>
## #128 — linear_20

Update the seeded comment on ENG-1 to: 'Updated: working on a fix and adding tests'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L128) · [Cards](cards.md#linear_20)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the described existing comment | resolved | `["e10f59c3-7a49-4d52-8dba-8c8602f8c807"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve the described existing comment. Use the described subject and the supported seed-level selector. Select the specified seeded comment by its body and qualifying issue, or the explicit prompt ID where supplied. Selection: Select the specified seeded comment by its body and qualifying issue, or the explicit prompt ID where supplied.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "comments",
    "where": {
      "id": {
        "eq": "e10f59c3-7a49-4d52-8dba-8c8602f8c807"
      }
    },
    "expected_changes": {
      "body": {
        "to": {
          "contains": "Updated: working on a fix"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_21"></a>
## #129 — linear_21

Delete the seeded comment on ENG-1

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L129) · [Cards](cards.md#linear_21)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the described existing comment | resolved | `["e10f59c3-7a49-4d52-8dba-8c8602f8c807"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve the described existing comment. Use the described subject and the supported seed-level selector. Select the specified seeded comment by its body and qualifying issue, or the explicit prompt ID where supplied. Selection: Select the specified seeded comment by its body and qualifying issue, or the explicit prompt ID where supplied.
- The assertion represents deletion by archiving the existing comment. No replacement field value is computed; the generated archive timestamp is omitted from written attributes.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "comments",
    "where": {
      "id": {
        "eq": "e10f59c3-7a49-4d52-8dba-8c8602f8c807"
      }
    },
    "expected_changes": {
      "archivedAt": {
        "from": {
          "exists": false
        },
        "to": {
          "exists": true
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_22"></a>
## #130 — linear_22

Create two Engineering issues: 'Update onboarding docs' (label UX) and 'Add circuit breaker' (label Urgent)

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L130) · [Cards](cards.md#linear_22)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1, A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve UX label | resolved | `["f9c5b7c8-3909-4f8b-bc25-73e1b56a9c0c"]` | no | A3: No assertion constrains this subject or its requested source-derived result. |
| 3. Resolve Urgent label | resolved | `["6c2b0d3c-3d6d-4d91-9a77-b93b59b8d5a0"]` | no | A3: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].
- **2.** Resolve UX label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["UX"]. Selection: Select issue_labels by issue_labels.name matching ["UX"].
- **3.** Resolve Urgent label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["Urgent"]. Selection: Select issue_labels by issue_labels.name matching ["Urgent"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      },
      "title": {
        "contains": "onboarding docs"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      },
      "title": {
        "contains": "circuit breaker"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {},
    "expected_count": {
      "min": 2
    }
  }
]
```

</details>

<a id="linear_23"></a>
## #131 — linear_23

Cancel issue ENG-1 (set its status to Canceled)

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L131) · [Cards](cards.md#linear_23)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-1 | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Engineering Canceled workflow state | resolved | `["d4f59a6d-33cb-45d1-8f4e-3e57536f912d"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-1. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-1"]. Selection: Select issues by issues.identifier matching ["ENG-1"].
- **2.** Resolve Engineering Canceled workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Canceled' in Engineering; the target issue/team establishes this team context. Selection: Select workflow state 'Canceled' in Engineering; the target issue/team establishes this team context.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "d4f59a6d-33cb-45d1-8f4e-3e57536f912d"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_24"></a>
## #132 — linear_24

Create a new label 'Backend' and add it to ENG-2

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L132) · [Cards](cards.md#linear_24)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-2 | resolved | `["5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-2. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-2"]. Selection: Select issues by issues.identifier matching ["ENG-2"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "Backend"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {
      "issue_id": {
        "eq": "5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_25"></a>
## #133 — linear_25

Rename the label 'UX' to 'User Experience'

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L133) · [Cards](cards.md#linear_25)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve UX label | resolved | `["f9c5b7c8-3909-4f8b-bc25-73e1b56a9c0c"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve UX label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["UX"]. Selection: Select issue_labels by issue_labels.name matching ["UX"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issue_labels",
    "where": {
      "id": {
        "eq": "f9c5b7c8-3909-4f8b-bc25-73e1b56a9c0c"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "User Experience"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_26"></a>
## #134 — linear_26

Unassign ENG-1 so it has no assignee

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L134) · [Cards](cards.md#linear_26)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve issue ENG-1 | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve issue ENG-1. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-1"]. Selection: Select issues by issues.identifier matching ["ENG-1"].
- Removing the assignee does not describe a separate person to resolve; the issue is the target.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "to": {
          "exists": false
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_27"></a>
## #135 — linear_27

Add a new workflow state for the product team called 'Done'. Then, create a new issue in this team called 'Mini-demo', mark it as done, and add a comment to it saying 'Marking it as done because Hubert already prepped the demo but forgot to create an issue'.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L135) · [Cards](cards.md#linear_27)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Product team | resolved | `["cdb85540-5065-4346-8aef-ae2b72d6e940"]` | yes | A1, A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Product team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Product"]. Selection: Select teams by teams.name matching ["Product"].
- Done is explicitly created in this task; Hubert occurs only in literal comment text.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "workflow_states",
    "where": {
      "name": {
        "eq": "Done"
      },
      "teamId": {
        "eq": "cdb85540-5065-4346-8aef-ae2b72d6e940"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "eq": "Mini-demo"
      },
      "teamId": {
        "eq": "cdb85540-5065-4346-8aef-ae2b72d6e940"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Hubert already prepped"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_28"></a>
## #136 — linear_28

Remove the 'Duplicate' workflow state from the Engineering team.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L136) · [Cards](cards.md#linear_28)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering Duplicate state | resolved | `["ab04ec5f-1292-48b0-9426-50d354957357"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Engineering Duplicate state. Use the described subject and the supported seed-level selector. Select the Duplicate state belonging to Engineering; deletion is represented by archive evidence. Selection: Select the Duplicate state belonging to Engineering; deletion is represented by archive evidence.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "workflow_states",
    "where": {
      "id": {
        "eq": "ab04ec5f-1292-48b0-9426-50d354957357"
      }
    },
    "expected_changes": {
      "archivedAt": {
        "from": {
          "exists": false
        },
        "to": {
          "exists": true
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_29"></a>
## #137 — linear_29

Find duplicated issues regarding 'trace analysis' in the Product team and mark the 2nd one (the newer one) as a duplicate.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L137) · [Cards](cards.md#linear_29)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the newer Product trace duplicate | resolved | `["33a21e17-7c49-4b93-a45d-28f58960a109"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Product Duplicate workflow state | absent | `[]` | no | None: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve the newer Product trace duplicate. Use the described subject and the supported seed-level selector. Within Product trace-related issues, select the later-created duplicate PROD-2 (2025-01-15 versus 2025-01-01), corroborated by A2. Selection: Within Product trace-related issues, select the later-created duplicate PROD-2 (2025-01-15 versus 2025-01-01), corroborated by A2.
- **2.** Resolve Product Duplicate workflow state. The explicit description has no matching seeded referent. Select workflow state 'Duplicate' in Product; the target issue/team establishes this team context. Selection: Select workflow state 'Duplicate' in Product; the target issue/team establishes this team context.
- The asserted permissive target is PROD-2. PROD-2 was created January 15, later than PROD-1 on January 1; both descriptions concern the same trace-analysis work. Product has no seeded Duplicate state, so its requested status is absent; creating a new state is the expected response, not a carried-over initial record.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "workflow_states",
    "where": {
      "name": {
        "eq": "Duplicate"
      },
      "teamId": {
        "eq": "cdb85540-5065-4346-8aef-ae2b72d6e940"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "PROD-2"
      }
    },
    "expected_changes": {
      "stateId": {
        "from": {
          "eq": "0fde0f94-ee5f-4a37-ad23-a3acd0080c57"
        },
        "to": {
          "exists": true
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_30"></a>
## #138 — linear_30

Add Artem (b55072d7-ccaa-43cd-8ab7-3dca324e3294) to the Product team.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L138) · [Cards](cards.md#linear_30)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Artem | resolved | `["b55072d7-ccaa-43cd-8ab7-3dca324e3294"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Product team | resolved | `["cdb85540-5065-4346-8aef-ae2b72d6e940"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Artem. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Artem Bogdanov"]. Selection: Select users by users.name, users.displayName matching ["Artem Bogdanov"].
- **2.** Resolve Product team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Product"]. Selection: Select teams by teams.name matching ["Product"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "team_memberships",
    "where": {
      "userId": {
        "eq": "b55072d7-ccaa-43cd-8ab7-3dca324e3294"
      },
      "teamId": {
        "eq": "cdb85540-5065-4346-8aef-ae2b72d6e940"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_31"></a>
## #139 — linear_31

Please edit the comment (id: e6a0f6c4-4d0e-4f4c-9a54-444444444444) about open telemetry and include the link 'https://smith.langchain.com/' as an example.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L139) · [Cards](cards.md#linear_31)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the explicitly identified OpenTelemetry comment | resolved | `["e6a0f6c4-4d0e-4f4c-9a54-444444444444"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve the explicitly identified OpenTelemetry comment. Use the described subject and the supported seed-level selector. Match the literal comment ID supplied by the prompt; append the requested example link. Selection: Match the literal comment ID supplied by the prompt; append the requested example link.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "comments",
    "where": {
      "id": {
        "eq": "e6a0f6c4-4d0e-4f4c-9a54-444444444444"
      }
    },
    "expected_changes": {
      "body": {
        "to": {
          "contains": "smith.langchain.com"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_32"></a>
## #140 — linear_32

John Doe is going on vacation. Reassign all of his 'Urgent' issues to Sarah Smith, but leave his non-urgent work as is.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L140) · [Cards](cards.md#linear_32)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve John’s urgent issues | resolved | `["87c1d2f3-66c4-4dd0-bc93-1b99d04dc374","33a21e17-7c49-4b93-a45d-28f58960a109"]` | partial | A1, A2: A1 requires ENG-3 reassignment, but also-urgent PROD-2 is unchecked. A2 protects ENG-1, not the completeness of urgent reassignment. |
| 2. Resolve Sarah Smith | resolved | `["03b0809e-713e-44ee-95de-b7a198b135ac"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve John’s urgent issues. Use the described subject and the supported seed-level selector. Select John Doe’s issues with priority=1 (Urgent); ENG-3 and PROD-2 match. John qualifies the issue set, not a separate requested user subject. Selection: Select John Doe’s issues with priority=1 (Urgent); ENG-3 and PROD-2 match. John qualifies the issue set, not a separate requested user subject.
- **2.** Resolve Sarah Smith. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Sarah Smith"]. Selection: Select users by users.name, users.displayName matching ["Sarah Smith"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-3"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "from": {
          "eq": "2dcc8dc2-ca19-475d-9882-3ba5e911e7ec"
        },
        "to": {
          "eq": "03b0809e-713e-44ee-95de-b7a198b135ac"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-1"
      }
    },
    "expected_count": 0,
    "expected_changes": {
      "assigneeId": {
        "to": {
          "exists": true
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_33"></a>
## #141 — linear_33

The 'Polish onboarding dashboard UX' issue was filed in Engineering by mistake. Move it to the Product team and reset its status to 'In Review'.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L141) · [Cards](cards.md#linear_33)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Polish onboarding dashboard UX issue | resolved | `["5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Product team | resolved | `["cdb85540-5065-4346-8aef-ae2b72d6e940"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Product In Review workflow state | absent | `[]` | no | None: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve Polish onboarding dashboard UX issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Polish onboarding dashboard UX'. Selection: Select the seeded issue whose title contains 'Polish onboarding dashboard UX'.
- **2.** Resolve Product team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Product"]. Selection: Select teams by teams.name matching ["Product"].
- **3.** Resolve Product In Review workflow state. The explicit description has no matching seeded referent. Select workflow state 'In Review' in Product; the target issue/team establishes this team context. Selection: Select workflow state 'In Review' in Product; the target issue/team establishes this team context.
- A1 names a destination state ID absent from the seed. Product has only Todo, so its requested In Review state is absent; the unchecked identity cannot be inferred from the answer-only ID.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-2"
      }
    },
    "expected_changes": {
      "teamId": {
        "from": {
          "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
        },
        "to": {
          "eq": "cdb85540-5065-4346-8aef-ae2b72d6e940"
        }
      },
      "stateId": {
        "to": {
          "eq": "31d46818-d16d-4279-90e6-a7bab45561c0"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_34"></a>
## #142 — linear_34

Read the comments on the 'production incident' ticket. Create a new Engineering ticket titled 'Fix 500 errors in eval runner' with a description based on the analysis in the comments. Mark this new ticket as being blocked by ENG-3.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L142) · [Cards](cards.md#linear_34)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve production-incident comments as analysis evidence | resolved | `["b3f7c3f2-1a7b-4d8e-9f21-111111111111"]` | partial | A1: The description need only contain agent. It can omit the 500-error spike, timing, and analysis reported by the source comments. |
| 2. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | no | None: No assertion constrains this subject or its requested source-derived result. |
| 3. Resolve issue ENG-3 | resolved | `["87c1d2f3-66c4-4dd0-bc93-1b99d04dc374"]` | no | A2: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve production-incident comments as analysis evidence. Use the described subject and the supported seed-level selector. Select comments attached to the production incident issue. Selection: Select comments attached to the production incident issue.
- **2.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].
- **3.** Resolve issue ENG-3. Use the described subject and the supported seed-level selector. Select issues by issues.identifier matching ["ENG-3"]. Selection: Select issues by issues.identifier matching ["ENG-3"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Fix 500 errors"
      },
      "description": {
        "contains": "agent"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_35"></a>
## #143 — linear_35

Assign the 'email sign-in' ticket to the Engineering team member who currently has the fewest assigned issues. If there is a tie, pick anyone with the lowest count.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L143) · [Cards](cards.md#linear_35)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the email sign-in issue | resolved | `["7d3f21ac-89c1-4f3b-9c2e-4fe3a1b71002"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve eligible least-loaded Engineering members | resolved | `["b55072d7-ccaa-43cd-8ab7-3dca324e3294","res-user-eng-5-001","mod-user-derek-001","mod-user-mila-001"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve the email sign-in issue. Use the described subject and the supported seed-level selector. Select the issue whose title describes email sign-in. Selection: Select the issue whose title describes email sign-in.
- **2.** Choose one eligible least-loaded member; the four-member set is a candidate population, not four assignments. Count assigned seeded issues for each Engineering member and select all tied minima (zero). Selection: Count assigned seeded issues for each Engineering member and select all tied minima (zero).
- Four Engineering members have zero assigned issues: Artem, Engineer Five, Derek, and Mila. The prompt explicitly permits ties. A1 selects Artem, an eligible choice, so that destination is fully covered; it is not required to accept every valid choice.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-6"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "to": {
          "eq": "b55072d7-ccaa-43cd-8ab7-3dca324e3294"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_36"></a>
## #144 — linear_36

We are replacing the 'RL' label with a new 'AI' label. Create a new label named 'AI'. Find all tickets with the 'RL' label, tag them with 'AI', and remove the 'RL' label.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L144) · [Cards](cards.md#linear_36)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve RL label | resolved | `["8f01ce9d-1433-4c4c-969d-21ca3bf2718f"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve issues bearing RL | resolved | `["b4f5130f-5c1b-4bc0-a8f6-60a22b0adf5e"]` | yes | A2, A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve RL label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["RL"]. Selection: Select issue_labels by issue_labels.name matching ["RL"].
- **2.** Resolve issues bearing RL. Use the described subject and the supported seed-level selector. Select issues linked to the RL label; only ENG-4 is linked. AI is newly created and adds no initial obligation. Selection: Select issues linked to the RL label; only ENG-4 is linked. AI is newly created and adds no initial obligation.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "AI"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "removed",
    "entity": "issue_label_issue_association",
    "where": {
      "issue_id": {
        "eq": "b4f5130f-5c1b-4bc0-a8f6-60a22b0adf5e"
      },
      "issue_label_id": {
        "eq": "8f01ce9d-1433-4c4c-969d-21ca3bf2718f"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {
      "issue_id": {
        "eq": "b4f5130f-5c1b-4bc0-a8f6-60a22b0adf5e"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_37"></a>
## #145 — linear_37

Find any Engineering tickets in 'In Progress' that were created before Jan 2nd, 2025. Move them back to 'Todo' and add a comment: 'Demoted due to lack of progress'.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L145) · [Cards](cards.md#linear_37)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve old In Progress Engineering issues | resolved | `["87c1d2f3-66c4-4dd0-bc93-1b99d04dc374"]` | yes | A1, A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Engineering Todo workflow state | resolved | `["741f29ae-cfb3-4b8a-a1f8-c5161c842366"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve old In Progress Engineering issues. Use the described subject and the supported seed-level selector. Select Engineering issues created before 2025-01-02 whose state is In Progress; only ENG-3 qualifies. Selection: Select Engineering issues created before 2025-01-02 whose state is In Progress; only ENG-3 qualifies.
- **2.** Resolve Engineering Todo workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Todo' in Engineering; the target issue/team establishes this team context. Selection: Select workflow state 'Todo' in Engineering; the target issue/team establishes this team context.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "ENG-3"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "741f29ae-cfb3-4b8a-a1f8-c5161c842366"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "issueId": {
        "eq": "87c1d2f3-66c4-4dd0-bc93-1b99d04dc374"
      },
      "body": {
        "contains": "Demoted"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_38"></a>
## #146 — linear_38

Break down the 'SSO' ticket into two sub-issues: 'Frontend Implementation' (assigned to Sarah) and 'Backend API' (assigned to John). Ensure the previous ticket is set as the parent for both.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L146) · [Cards](cards.md#linear_38)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the SSO parent issue | resolved | `["7d3f21ac-89c1-4f3b-9c2e-4fe3a1b71002"]` | yes | A1, A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Sarah | resolved | `["03b0809e-713e-44ee-95de-b7a198b135ac"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve John | resolved | `["2dcc8dc2-ca19-475d-9882-3ba5e911e7ec"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve the SSO parent issue. Use the described subject and the supported seed-level selector. Select the SSO issue by its title. Selection: Select the SSO issue by its title.
- **2.** Resolve Sarah. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Sarah Smith"]. Selection: Select users by users.name, users.displayName matching ["Sarah Smith"].
- **3.** Resolve John. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["John Doe"]. Selection: Select users by users.name, users.displayName matching ["John Doe"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "parentId": {
        "eq": "7d3f21ac-89c1-4f3b-9c2e-4fe3a1b71002"
      },
      "assigneeId": {
        "eq": "03b0809e-713e-44ee-95de-b7a198b135ac"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "parentId": {
        "eq": "7d3f21ac-89c1-4f3b-9c2e-4fe3a1b71002"
      },
      "assigneeId": {
        "eq": "2dcc8dc2-ca19-475d-9882-3ba5e911e7ec"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_39"></a>
## #147 — linear_39

Create three new issues in Engineering: 'Alpha', 'Beta', and 'Gamma'. Configure them as a dependency chain where Alpha blocks Beta, and Beta blocks Gamma.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L147) · [Cards](cards.md#linear_39)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Engineering team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Engineering team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Engineering"]. Selection: Select teams by teams.name matching ["Engineering"].
- All dependency endpoints are new issues; no extra initial-state relation obligations.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
      }
    },
    "expected_count": 3
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      }
    },
    "expected_count": 2
  }
]
```

</details>

<a id="linear_40"></a>
## #148 — linear_40

The community center is hosting the "Living Cultures Festival" from Feb 15-19. Create a new team called "Fermentation Guild" to coordinate this event. We need to track fermentation timelines carefully.

First, add a new workflow state called "Fermenting" (color: #8B4513, type: started) to the new team - this will help us track items that are actively culturing.

Create a label called "time-critical" for tasks with strict biological deadlines.

Now for the tricky scheduling: Kenji needs to start his 3-week miso base by January 25th at the latest for it to be ready for the festival tasting on Feb 18th. Create an issue titled "Prepare Kenji miso base for Feb 18 tasting" and assign it to Kenji with the time-critical label.

However, Fatima needs access to the koji room first to inoculate spores for her amazake demonstration. Create another issue "Inoculate koji spores for amazake - Fatima" and set it up so that it blocks Kenji's miso preparation (they share the temperature-controlled koji room and can't run both processes simultaneously).

Finally, add a comment to the miso task that says: "CULTURE_READY_CHECK: Verify koji colonization complete before rice inoculation. Target temp 86F for 48hrs."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L148) · [Cards](cards.md#linear_40)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Kenji | resolved | `["a1b2c3d4-e5f6-7890-abcd-ef1234567890"]` | yes | A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Kenji. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Kenji Tanaka"]. Selection: Select users by users.name, users.displayName matching ["Kenji Tanaka"].
- Fatima occurs in the new issue’s supplied title and motivation; no separate lookup or assignment to Fatima is requested.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "teams",
    "where": {
      "name": {
        "eq": "Fermentation Guild"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "workflow_states",
    "where": {
      "name": {
        "eq": "Fermenting"
      },
      "color": {
        "eq": "#8B4513"
      },
      "type": {
        "eq": "started"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "time-critical"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "miso base"
      },
      "assigneeId": {
        "eq": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "koji spores"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {},
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      },
      "issueTitle": {
        "contains": "koji spores"
      },
      "relatedIssueTitle": {
        "contains": "miso"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "CULTURE_READY_CHECK"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_41"></a>
## #149 — linear_41

The Seed Library team is conducting its quarterly germination audit. We need to evaluate each donor's success rate and take appropriate action.

First, calculate Yuto's germination rate: count how many of his seed packets are in "Sprouted" status versus "Failed" status, then compute (sprouted / total) × 100. If his rate is 75% or higher AND he has at least 2 different varieties that sprouted, create a new label called "Seed Guardian" and apply it to all of his packets as recognition.

Next, handle Nneka's special case: she donated exactly one packet and it's marked as priority 1 (rare heirloom). Regardless of whether it sprouted or failed, move this packet to "Preserved Collection" status—the library will attempt tissue culture propagation on rare genetics.

Finally, evaluate Szymon's packets the same way. If his germination rate is below 60%, move all his non-sprouted packets to "Needs Donor Review" status and add a comment to each one that reads: "GERMINATION_AUDIT: X sprouted / Y total = Z% - below 60% threshold" where X, Y, Z are the actual calculated values.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L149) · [Cards](cards.md#linear_41)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Yuto’s seed packet evidence | resolved | `["56789012-def0-1234-5678-9abcdef01234","67890123-ef01-2345-6789-abcdef012345","78901234-f012-3456-789a-bcdef0123456","89012345-0123-4567-89ab-cdef01234567"]` | partial | A1, A2: The label name reflects the positive branch, but four generic label associations do not require the four Yuto packets. |
| 2. Resolve Nneka’s seed packet evidence | resolved | `["9a012345-1234-5678-9abc-def012345678"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Szymon’s seed packet evidence | resolved | `["ab123456-2345-6789-abcd-ef0123456789","bc234567-3456-789a-bcde-f01234567890","cd345678-4567-89ab-cdef-012345678901"]` | partial | A4, A5, A6: The two failed-packet changes constrain the action subset, but GERMINATION_AUDIT: alone does not check the requested 1/3 rate and counts. |
| 4. Resolve Seed Library Preserved Collection workflow state | resolved | `["34567890-bcde-f012-3456-789abcdef012"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 5. Resolve Szymon’s non-sprouted action targets | resolved | `["bc234567-3456-789a-bcde-f01234567890","cd345678-4567-89ab-cdef-012345678901"]` | yes | A4, A5: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 6. Resolve Seed Library Needs Donor Review workflow state | resolved | `["45678901-cdef-0123-4567-89abcdef0123"]` | yes | A4, A5: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Yuto’s seed packet evidence. Use the described subject and the supported seed-level selector. Select the Seed Library packet titles naming Yuto. Selection: Select the Seed Library packet titles naming Yuto.
- **2.** Resolve Nneka’s seed packet evidence. Use the described subject and the supported seed-level selector. Select the Seed Library packet titles naming Nneka. Selection: Select the Seed Library packet titles naming Nneka.
- **3.** Resolve Szymon’s seed packet evidence. Use the described subject and the supported seed-level selector. Select the Seed Library packet titles naming Szymon. Selection: Select the Seed Library packet titles naming Szymon.
- **4.** Resolve Seed Library Preserved Collection workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Preserved Collection' in Seed Library; the target issue/team establishes this team context. Selection: Select workflow state 'Preserved Collection' in Seed Library; the target issue/team establishes this team context.
- **5.** Resolve Szymon’s non-sprouted action targets. Use the described subject and the supported seed-level selector. Select Szymon’s Seed Library packets not in Sprouted state; the two Failed packets qualify. Selection: Select Szymon’s Seed Library packets not in Sprouted state; the two Failed packets qualify.
- **6.** Resolve Seed Library Needs Donor Review workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Needs Donor Review' in Seed Library; the target issue/team establishes this team context. Selection: Select workflow state 'Needs Donor Review' in Seed Library; the target issue/team establishes this team context.
- Seed-derived rates: Yuto 3/4=75% with three sprouted varieties; Szymon 1/3=33.333…%. Both conditional action branches apply. Donor names qualify packet sets, not separately requested profiles.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "Seed Guardian"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {},
    "expected_count": 4
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "SEED-5"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "34567890-bcde-f012-3456-789abcdef012"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "SEED-7"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "45678901-cdef-0123-4567-89abcdef0123"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "identifier": {
        "eq": "SEED-8"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "45678901-cdef-0123-4567-89abcdef0123"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "GERMINATION_AUDIT:"
      }
    },
    "expected_count": 2
  }
]
```

</details>

<a id="linear_42"></a>
## #150 — linear_42

The Forest Mycology Collective is organizing their autumn foraging expedition. First, create a new team called "Forest Mycology Collective" to track all club activities.

Create a label called "awaiting-spore-print" for specimens that need laboratory analysis before identification can be confirmed.

Now set up the expedition: create an issue titled "Coastal Redwood Reserve Autumn Foray" and assign it to Haruki as the expedition leader.

During the planning phase, we're pre-logging anticipated specimen finds based on last year's survey. Create a specimen issue titled "Specimen #1: Cantharellus formosus cluster - Sector 7" and assign it to Priya for documentation. Create another specimen issue "Specimen #2: Unknown Amanita - requires cross-reference" and assign it to Dmitri, applying the "awaiting-spore-print" label.

The Amanita identification depends on comparing its spore print against the Cantharellus specimen first (they were found in the same microhabitat and we need to rule out look-alikes). Set up the Amanita issue as blocked by the Cantharellus issue.

Finally, add a field note comment to the Cantharellus specimen that reads: "FIELD_NOTE_REF: GPS coordinates 41.2132°N, found near fallen Douglas fir. Fruiting body golden-yellow, false gills present, apricot aroma confirmed."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L150) · [Cards](cards.md#linear_42)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Haruki | resolved | `["f6a7b8c9-d0e1-2345-0123-789012345678"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Priya | resolved | `["b8c9d0e1-f2a3-4567-2345-901234567890"]` | yes | A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Dmitri | resolved | `["a7b8c9d0-e1f2-3456-1234-890123456789"]` | yes | A5: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Haruki. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Haruki Tanaka"]. Selection: Select users by users.name, users.displayName matching ["Haruki Tanaka"].
- **2.** Resolve Priya. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Priya Sharma"]. Selection: Select users by users.name, users.displayName matching ["Priya Sharma"].
- **3.** Resolve Dmitri. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Dmitri Volkov"]. Selection: Select users by users.name, users.displayName matching ["Dmitri Volkov"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "teams",
    "where": {
      "name": {
        "eq": "Forest Mycology Collective"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "awaiting-spore-print"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Coastal Redwood Reserve"
      },
      "assigneeId": {
        "eq": "f6a7b8c9-d0e1-2345-0123-789012345678"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Cantharellus formosus"
      },
      "assigneeId": {
        "eq": "b8c9d0e1-f2a3-4567-2345-901234567890"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Amanita"
      },
      "assigneeId": {
        "eq": "a7b8c9d0-e1f2-3456-1234-890123456789"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {},
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      },
      "issueTitle": {
        "contains": "Cantharellus"
      },
      "relatedIssueTitle": {
        "contains": "Amanita"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "FIELD_NOTE_REF:"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_43"></a>
## #151 — linear_43

The Mobile team is preparing for the v2.5 release and QA has reported some critical bugs that need to be tracked.

First, create a new issue titled "App crashes on login with special characters" in the Mobile team. This is a high priority bug. Assign it to Marcus.

Create another issue titled "Push notifications not working on Android 14" in the same team and assign it to Aisha.

Move both issues to "In Progress" status since the developers are starting work on them immediately.

Finally, add a comment to the login crash issue with the following reproduction steps: "REPRO_STEPS: 1. Open app 2. Enter username with & or % character 3. Tap login button 4. App crashes to home screen. Tested on iOS 17.2 and Android 14."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L151) · [Cards](cards.md#linear_43)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Mobile team | resolved | `["a0b1c2d3-e4f5-6789-0123-456789abcdef"]` | yes | A1, A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Marcus Aurelius | resolved | `["c9d0e1f2-a3b4-5678-3456-012345678901"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Aisha | resolved | `["d0e1f2a3-b4c5-6789-4567-123456789012"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve Mobile In Progress workflow state | resolved | `["mob-state-inprogress-567890abcdef"]` | yes | A1, A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Mobile team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Mobile"]. Selection: Select teams by teams.name matching ["Mobile"].
- **2.** Resolve the Marcus selected by the task’s Mobile context and assertion: Marcus Aurelius, not Marcus Johnson. The first name alone is ambiguous. Select users by users.name, users.displayName matching ["Marcus Aurelius"]. Selection: Select users by users.name, users.displayName matching ["Marcus Aurelius"].
- **3.** Resolve Aisha. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Aisha Mohammed"]. Selection: Select users by users.name, users.displayName matching ["Aisha Mohammed"].
- **4.** Resolve Mobile In Progress workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'In Progress' in Mobile; the target issue/team establishes this team context. Selection: Select workflow state 'In Progress' in Mobile; the target issue/team establishes this team context.
- Two seeded users are named Marcus. The asserted mutation target Marcus Aurelius supplies the adopted permissive name boundary. Mobile is also constrained through the team-specific In Progress state handle; this covers the derived team reference without requiring a redundant teamId predicate.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "crashes on login"
      },
      "assigneeId": {
        "eq": "c9d0e1f2-a3b4-5678-3456-012345678901"
      },
      "stateId": {
        "eq": "mob-state-inprogress-567890abcdef"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Push notifications"
      },
      "assigneeId": {
        "eq": "d0e1f2a3-b4c5-6789-4567-123456789012"
      },
      "stateId": {
        "eq": "mob-state-inprogress-567890abcdef"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "REPRO_STEPS:"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_44"></a>
## #152 — linear_44

The IT Support team received a critical server outage report. Here's the workflow to execute:

First, check if a label called "hardware-failure" exists. If it doesn't, create it.

Create a new issue titled "Server rack B7 unresponsive - power supply failure" in the IT Support team.

Apply the "hardware-failure" label to this ticket and assign it to Kofi for initial triage.

Add a comment to the ticket with this diagnostic entry: "DIAG_LOG_001: Initial ping test failed. Checked physical connections. PSU indicator light is off. Replacement unit requested from inventory."

Now update that same comment to append the following resolution note at the end: " || UPDATE: PSU replaced at 14:32. Server responding. Monitoring for 24hrs."

Finally, update the ticket to change the assignee from Kofi to Elena for post-incident verification, and move the ticket to "In Review" status.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L152) · [Cards](cards.md#linear_44)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve IT Support team | resolved | `["b1c2d3e4-f5a6-7890-1234-567890abcdef"]` | no | None: No assertion constrains this subject or its requested source-derived result. |
| 2. Resolve hardware-failure label | absent | `[]` | yes | A1: A1 checks the appropriate named creation for this absent-label branch. It does not prove a lookup occurred or that the new label was attached correctly. |
| 3. Resolve Kofi | resolved | `["f2a3b4c5-d6e7-8901-6789-345678901234"]` | no | None: No assertion constrains this subject or its requested source-derived result. |
| 4. Resolve Elena | resolved | `["a3b4c5d6-e7f8-9012-7890-456789012345"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 5. Resolve IT Support In Review workflow state | resolved | `["its-state-inreview-4567-def0123456"]` | no | None: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve IT Support team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["IT Support"]. Selection: Select teams by teams.name matching ["IT Support"].
- **2.** Resolve hardware-failure label. The explicit description has no matching seeded referent. Select issue_labels by issue_labels.name matching []. Selection: Select issue_labels by issue_labels.name matching [].
- **3.** Resolve Kofi. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Kofi Mensah"]. Selection: Select users by users.name, users.displayName matching ["Kofi Mensah"].
- **4.** Resolve Elena. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Elena Papadopoulos"]. Selection: Select users by users.name, users.displayName matching ["Elena Papadopoulos"].
- **5.** Resolve IT Support In Review workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'In Review' in IT Support; the target issue/team establishes this team context. Selection: Select workflow state 'In Review' in IT Support; the target issue/team establishes this team context.
- hardware-failure is absent; the prompt explicitly requires checking before creation. Kofi is a definite initial assignee, not an inactive conditional branch. The assertions’ added/changed treatment of newly created objects is recorded as written, without inspecting evaluator behavior.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "hardware-failure"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Server rack B7"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Server rack B7"
      }
    },
    "expected_count": 1,
    "expected_changes": {
      "assigneeId": {
        "to": {
          "eq": "a3b4c5d6-e7f8-9012-7890-456789012345"
        }
      }
    },
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {},
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "DIAG_LOG_001:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "|| UPDATE:"
      }
    },
    "expected_count": 1,
    "expected_changes": {
      "body": {
        "to": {
          "contains": "|| UPDATE:"
        }
      }
    }
  }
]
```

</details>

<a id="linear_45"></a>
## #153 — linear_45

The Backend team is doing sprint cleanup. Here's what needs to happen:

First, find the existing issue about "database migration" - we'll need its ID for a dependency.

Create a new parent issue titled "Q1 Infrastructure Overhaul" in the Backend team. This will be our tracking epic.

Create a sub-issue under that epic titled "Upgrade Redis cluster to v7" - make sure to set the parent relationship to the epic you just created.

The Redis upgrade cannot start until the database migration is complete. Set up the Redis issue as blocked by the database migration issue.

Now, add a standup note comment to the Redis issue that says: "STANDUP_NOTE: Jamal will start this after migration completes. ETA next Tuesday."

Wait - that comment was supposed to go on the migration ticket, not the Redis ticket. Delete that comment.

Finally, assign the Redis sub-task to Jamal, and assign the parent epic "Q1 Infrastructure Overhaul" to Olga with High priority.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L153) · [Cards](cards.md#linear_45)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Backend team | resolved | `["c2d3e4f5-a6b7-8901-2345-6789abcdef01"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve database migration issue | resolved | `["de456789-5678-9abc-def0-123456789012"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Jamal | resolved | `["e7f8a9b0-c1d2-3456-1234-890123456789"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve Olga | resolved | `["d6e7f8a9-b0c1-2345-0123-789012345678"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Backend team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Backend"]. Selection: Select teams by teams.name matching ["Backend"].
- **2.** Resolve database migration issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'database migration'. Selection: Select the seeded issue whose title contains 'database migration'.
- **3.** Resolve Jamal. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Jamal Abdullah"]. Selection: Select users by users.name, users.displayName matching ["Jamal Abdullah"].
- **4.** Resolve Olga. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Olga Petrova"]. Selection: Select users by users.name, users.displayName matching ["Olga Petrova"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Q1 Infrastructure Overhaul"
      },
      "teamId": {
        "eq": "c2d3e4f5-a6b7-8901-2345-6789abcdef01"
      },
      "assigneeId": {
        "eq": "d6e7f8a9-b0c1-2345-0123-789012345678"
      },
      "priority": {
        "eq": 2.0
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Redis cluster"
      },
      "assigneeId": {
        "eq": "e7f8a9b0-c1d2-3456-1234-890123456789"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      },
      "issueTitle": {
        "contains": "database migration"
      },
      "relatedIssueTitle": {
        "contains": "Redis"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_46"></a>
## #154 — linear_46

The Launch Coordination team is preparing for the April 1st product release. We need to set up the critical path with proper dependencies and timing.

First, create a new workflow state called "Awaiting Dependency" (color: #FFA500, type: started) - we'll use this for tasks that are time-blocked by predecessors.

Create three issues in the Launch Coordination team:

1. "Complete product documentation for v3.0 launch" - This is the first domino. Yuki owns this. Due date must be March 22nd because legal needs 5 business days after this completes.

2. "Legal review of launch materials" - Svetlana from Legal owns this. Due date is March 29th. This CANNOT start until documentation is complete - set up the blocking relationship.

3. "Publish marketing campaign assets" - Kwame owns this. Due date is March 31st (press embargo lifts at 9am that day). This is blocked by legal review completion.

Set up the dependency chain: Documentation blocks Legal Review, and Legal Review blocks Marketing.

Finally, add a comment to the documentation issue that explains the timeline pressure: "CRITICAL_PATH_NOTE: This task has ZERO slack. If documentation slips past March 22nd, legal review (5 business days) won't complete by March 29th, which blocks marketing from the March 31st embargo lift. Launch date is immovable."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L154) · [Cards](cards.md#linear_46)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Launch Coordination team | resolved | `["d3e4f5a6-b7c8-9012-3456-789abcdef012"]` | yes | A2, A3, A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Yuki | resolved | `["f8a9b0c1-d2e3-4567-2345-901234567890"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Svetlana | resolved | `["b0c1d2e3-f4a5-6789-4567-123456789012"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve Kwame | resolved | `["a9b0c1d2-e3f4-5678-3456-012345678901"]` | yes | A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Launch Coordination team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Launch Coordination"]. Selection: Select teams by teams.name matching ["Launch Coordination"].
- **2.** Resolve Yuki. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Yuki Tanaka"]. Selection: Select users by users.name, users.displayName matching ["Yuki Tanaka"].
- **3.** Resolve Svetlana. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Svetlana Ivanova"]. Selection: Select users by users.name, users.displayName matching ["Svetlana Ivanova"].
- **4.** Resolve Kwame. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Kwame Asante"]. Selection: Select users by users.name, users.displayName matching ["Kwame Asante"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "workflow_states",
    "where": {
      "name": {
        "eq": "Awaiting Dependency"
      },
      "color": {
        "eq": "#FFA500"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "product documentation"
      },
      "teamId": {
        "eq": "d3e4f5a6-b7c8-9012-3456-789abcdef012"
      },
      "assigneeId": {
        "eq": "f8a9b0c1-d2e3-4567-2345-901234567890"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Legal review"
      },
      "teamId": {
        "eq": "d3e4f5a6-b7c8-9012-3456-789abcdef012"
      },
      "assigneeId": {
        "eq": "b0c1d2e3-f4a5-6789-4567-123456789012"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "marketing campaign"
      },
      "teamId": {
        "eq": "d3e4f5a6-b7c8-9012-3456-789abcdef012"
      },
      "assigneeId": {
        "eq": "a9b0c1d2-e3f4-5678-3456-012345678901"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      }
    },
    "expected_count": 2
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "CRITICAL_PATH_NOTE:"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_47"></a>
## #155 — linear_47

The Research team needs to set up the grant application pipeline for the upcoming NIH submission deadline (June 15th).

First, find the existing "IRB Ethics Approval" issue - this is our starting point and is already in progress.

Create three new issues in the Research team to complete the pipeline:

1. "Data Collection Protocol v2" - Nadia will own this. It cannot begin until ethics approval is complete.

2. "Pilot Study Design - 50 participant cohort" - Tomás will lead this. It depends on having the data collection protocol finalized.

3. "Grant Submission Draft - R01 mechanism" - Chioma will compile the final submission. This is the last step and depends on pilot study results.

Set up the blocking relationships to enforce the sequential workflow:
- IRB Ethics Approval blocks Data Collection Protocol
- Data Collection Protocol blocks Pilot Study Design
- Pilot Study Design blocks Grant Submission Draft

After setting up the dependencies, add a comment to the Grant Submission issue summarizing the critical path: "PIPELINE_STATUS: This submission depends on completion chain: Ethics (in progress) → Data Protocol (Nadia) → Pilot Study (Tomás) → This draft. Target: June 15th deadline."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L155) · [Cards](cards.md#linear_47)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Research team | resolved | `["e4f5a6b7-c8d9-0123-4567-89abcdef0123"]` | yes | A1, A2, A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve IRB Ethics Approval issue | resolved | `["ef567890-6789-abcd-ef01-234567890123"]` | no | A4: No assertion constrains this subject or its requested source-derived result. |
| 3. Resolve Nadia | resolved | `["c1d2e3f4-a5b6-7890-5678-234567890123"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve Tomás | resolved | `["d2e3f4a5-b6c7-8901-6789-345678901234"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 5. Resolve Chioma | resolved | `["e3f4a5b6-c7d8-9012-7890-456789012345"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Research team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Research"]. Selection: Select teams by teams.name matching ["Research"].
- **2.** Resolve IRB Ethics Approval issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'IRB Ethics Approval'. Selection: Select the seeded issue whose title contains 'IRB Ethics Approval'.
- **3.** Resolve Nadia. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Nadia Kowalczyk"]. Selection: Select users by users.name, users.displayName matching ["Nadia Kowalczyk"].
- **4.** Resolve Tomás. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Tomás Silva"]. Selection: Select users by users.name, users.displayName matching ["Tomás Silva"].
- **5.** Resolve Chioma. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Chioma Okafor"]. Selection: Select users by users.name, users.displayName matching ["Chioma Okafor"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Data Collection Protocol"
      },
      "teamId": {
        "eq": "e4f5a6b7-c8d9-0123-4567-89abcdef0123"
      },
      "assigneeId": {
        "eq": "c1d2e3f4-a5b6-7890-5678-234567890123"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Pilot Study"
      },
      "teamId": {
        "eq": "e4f5a6b7-c8d9-0123-4567-89abcdef0123"
      },
      "assigneeId": {
        "eq": "d2e3f4a5-b6c7-8901-6789-345678901234"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Grant Submission"
      },
      "teamId": {
        "eq": "e4f5a6b7-c8d9-0123-4567-89abcdef0123"
      },
      "assigneeId": {
        "eq": "e3f4a5b6-c7d8-9012-7890-456789012345"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      }
    },
    "expected_count": 3
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "PIPELINE_STATUS:"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_48"></a>
## #156 — linear_48

The Post-Production team is managing the editing pipeline for "Project Aurora". Here's what needs to happen:

First, find the "Master Edit Lock" issue - this is the critical gate that must complete before downstream work can proceed.

Count how many issues are directly blocked by "Master Edit Lock". You'll need this exact number for your report.

Create two new issues in the Post-Production team:
1. "Final Color Grade - DCI-P3 Mastering" - Kenji will handle this. It cannot start until "Color Grading Phase 1" is complete.
2. "Audio Mix Master - Dolby Atmos" - Amara will handle this. It depends on "Sound Design Draft" being finished.

Additionally, the colorist needs to lock the final look before audio can be mixed to picture. Set up "Final Color Grade" accordingly.

After setting up all the new dependencies, add a comment to the "Master Edit Lock" issue with a dependency audit in this exact format:

"DEPENDENCY_AUDIT: Master Edit Lock directly blocks [X] downstream issues. New dependencies added: Final Color Grade (Kenji), Audio Mix Master (Amara). Cross-stream link established between color and audio pipelines."

Replace [X] with the actual count of issues directly blocked by Master Edit Lock.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L156) · [Cards](cards.md#linear_48)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Post-Production team | resolved | `["f5a6b7c8-d9e0-1234-5678-9abcdef01234"]` | yes | A1, A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Master Edit Lock issue | resolved | `["post-issue-master-edit-lock-001"]` | no | A4: No assertion constrains this subject or its requested source-derived result. |
| 3. Resolve issues directly blocked by Master Edit Lock | resolved | `["post-issue-color-grading-phase1-002","post-issue-sound-design-draft-003","post-issue-vfx-compositing-004","post-issue-subtitle-localization-005"]` | partial | A5: The number 4 is bound to directly blocks, but its subject need not be Master Edit Lock. A statement that an unrelated issue directly blocks 4 meets A5; A4 adds only an audit marker. |
| 4. Resolve Color Grading Phase 1 issue | resolved | `["post-issue-color-grading-phase1-002"]` | no | A3: No assertion constrains this subject or its requested source-derived result. |
| 5. Resolve Sound Design Draft issue | resolved | `["post-issue-sound-design-draft-003"]` | no | A3: No assertion constrains this subject or its requested source-derived result. |
| 6. Resolve Kenji | resolved | `["a1b2c3d4-e5f6-7890-abcd-ef1234567890"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 7. Resolve Amara | resolved | `["f4a5b6c7-d8e9-0123-8901-567890123456"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Post-Production team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Post-Production"]. Selection: Select teams by teams.name matching ["Post-Production"].
- **2.** Resolve Master Edit Lock issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Master Edit Lock'. Selection: Select the seeded issue whose title contains 'Master Edit Lock'.
- **3.** Resolve issues directly blocked by Master Edit Lock. Use the described subject and the supported seed-level selector. Follow outgoing blocks relations from Master Edit Lock exactly one hop. Selection: Follow outgoing blocks relations from Master Edit Lock exactly one hop.
- **4.** Resolve Color Grading Phase 1 issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Color Grading Phase 1'. Selection: Select the seeded issue whose title contains 'Color Grading Phase 1'.
- **5.** Resolve Sound Design Draft issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Sound Design Draft'. Selection: Select the seeded issue whose title contains 'Sound Design Draft'.
- **6.** Resolve Kenji. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Kenji Tanaka"]. Selection: Select users by users.name, users.displayName matching ["Kenji Tanaka"].
- **7.** Resolve Amara. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Amara Tesfaye"]. Selection: Select users by users.name, users.displayName matching ["Amara Tesfaye"].
- Four issues are directly blocked by Master Edit Lock; Color Grading Phase 2 is only indirectly blocked and excluded from the count.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Final Color Grade"
      },
      "teamId": {
        "eq": "f5a6b7c8-d9e0-1234-5678-9abcdef01234"
      },
      "assigneeId": {
        "eq": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Audio Mix Master"
      },
      "teamId": {
        "eq": "f5a6b7c8-d9e0-1234-5678-9abcdef01234"
      },
      "assigneeId": {
        "eq": "f4a5b6c7-d8e9-0123-8901-567890123456"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      }
    },
    "expected_count": 3
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "DEPENDENCY_AUDIT:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "directly blocks 4"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_49"></a>
## #157 — linear_49

The Archaeology team is managing the Season 3 excavation at Site Karnak-West. There's a workflow problem blocking progress.

Examine the issues "Artifact Photography Documentation" and "Lab Sample Analysis". These two issues are in a dependency deadlock - each one is marked as blocking the other, which means neither can proceed.

Determine which blocking relationship is incorrect. The correct archaeological workflow is: Photography must complete BEFORE samples can go to the lab (you need photos of artifacts in situ before extraction for the record). The reverse relationship (lab blocking photography) was added by mistake and makes no sense.

Delete the incorrect blocking relationship to resolve the deadlock.

Now extend the workflow. Create a new issue called "Final Site Report Compilation - Season 3" in the Archaeology team. This report cannot be written until BOTH the photography documentation AND the lab analysis are complete. Set up both as blockers for the report.

Assign the work: Ximena handles photography, Okonkwo handles lab analysis, and Søren compiles the final report.

Move the photography issue to "In Progress" now that it's unblocked.

After fixing everything, add a comment to the "Lab Sample Analysis" issue documenting the fix: "WORKFLOW_FIX: Removed erroneous blocking relation where Lab was blocking Photography. Correct flow is Photography → Lab (need in-situ photos before extraction). Deadlock resolved. Current chain: Photography → Lab Analysis → Final Report."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L157) · [Cards](cards.md#linear_49)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Archaeology team | resolved | `["a6b7c8d9-e0f1-2345-6789-0abcdef12345"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Artifact Photography Documentation issue | resolved | `["arch-issue-photography-001"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Lab Sample Analysis issue | resolved | `["arch-issue-lab-analysis-002"]` | yes | A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve the erroneous Lab-blocks-Photography relation | resolved | `["rel-lab-blocks-photo-002"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 5. Resolve Ximena | resolved | `["b6c7d8e9-f0a1-2345-0123-789012345678"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 6. Resolve Nneka Okonkwo | resolved | `["d4e5f6a7-b8c9-0123-def0-456789012345"]` | yes | A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 7. Resolve Søren | resolved | `["c7d8e9f0-a1b2-3456-1234-890123456789"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 8. Resolve Archaeology In Progress workflow state | resolved | `["arch-state-inprogress-2345-cdef01"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Archaeology team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Archaeology"]. Selection: Select teams by teams.name matching ["Archaeology"].
- **2.** Resolve Artifact Photography Documentation issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Artifact Photography Documentation'. Selection: Select the seeded issue whose title contains 'Artifact Photography Documentation'.
- **3.** Resolve Lab Sample Analysis issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Lab Sample Analysis'. Selection: Select the seeded issue whose title contains 'Lab Sample Analysis'.
- **4.** Resolve the erroneous Lab-blocks-Photography relation. Use the described subject and the supported seed-level selector. Select the blocks edge from Lab Sample Analysis to Artifact Photography Documentation; the prompt explicitly specifies the reverse dependency is wrong. Selection: Select the blocks edge from Lab Sample Analysis to Artifact Photography Documentation; the prompt explicitly specifies the reverse dependency is wrong.
- **5.** Resolve Ximena. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Ximena Rodríguez"]. Selection: Select users by users.name, users.displayName matching ["Ximena Rodríguez"].
- **6.** Resolve Nneka Okonkwo. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Nneka Okonkwo"]. Selection: Select users by users.name, users.displayName matching ["Nneka Okonkwo"].
- **7.** Resolve Søren. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Søren Andersen"]. Selection: Select users by users.name, users.displayName matching ["Søren Andersen"].
- **8.** Resolve Archaeology In Progress workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'In Progress' in Archaeology; the target issue/team establishes this team context. Selection: Select workflow state 'In Progress' in Archaeology; the target issue/team establishes this team context.
- Okonkwo matches the seeded user Nneka Okonkwo by surname. The request has no competing seeded user with that surname.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issue_relations",
    "where": {
      "id": {
        "eq": "rel-lab-blocks-photo-002"
      }
    },
    "expected_changes": {
      "archivedAt": {
        "from": {
          "exists": false
        },
        "to": {
          "exists": true
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Final Site Report"
      },
      "teamId": {
        "eq": "a6b7c8d9-e0f1-2345-6789-0abcdef12345"
      },
      "assigneeId": {
        "eq": "c7d8e9f0-a1b2-3456-1234-890123456789"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "arch-issue-photography-001"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "arch-state-inprogress-2345-cdef01"
        }
      },
      "assigneeId": {
        "to": {
          "eq": "b6c7d8e9-f0a1-2345-0123-789012345678"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "arch-issue-lab-analysis-002"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "to": {
          "eq": "d4e5f6a7-b8c9-0123-def0-456789012345"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "issue_relations",
    "where": {
      "type": {
        "eq": "blocks"
      }
    },
    "expected_count": 2
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "WORKFLOW_FIX:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Deadlock resolved"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_50"></a>
## #158 — linear_50

The Stargazers astronomy club needs to set up their spring celestial events schedule.

Create a new issue in the Stargazers team titled "Lyrid Meteor Shower Viewing Party - Peak Night April 22nd" with description "Annual club gathering at Dark Sky Preserve. Expected rate: 18 meteors/hour. Radiant rises after midnight in Perseus."

Assign this event to Priya as the event coordinator.

Apply the "public-event" label to this issue since non-members are welcome to attend.

Add a comment with the viewing logistics: "OBSERVATION_DETAILS: Meet at Ridgeline Observatory parking lot at 10pm. Bring red flashlights only - no white light. Bogdan will set up the 12-inch Dobsonian for Saturn viewing while we wait for the radiant to rise. Best meteor photography settings: ISO 3200, f/2.8, 20-second exposures pointed northeast."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L158) · [Cards](cards.md#linear_50)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Stargazers team | resolved | `["b7c8d9e0-f1a2-3456-7890-abcdef123456"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Priya | resolved | `["b8c9d0e1-f2a3-4567-2345-901234567890"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve public-event label | resolved | `["star-label-public-event-001"]` | no | A4: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve Stargazers team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Stargazers"]. Selection: Select teams by teams.name matching ["Stargazers"].
- **2.** Resolve Priya. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Priya Sharma"]. Selection: Select users by users.name, users.displayName matching ["Priya Sharma"].
- **3.** Resolve public-event label. Use the described subject and the supported seed-level selector. Select issue_labels by issue_labels.name matching ["public-event"]. Selection: Select issue_labels by issue_labels.name matching ["public-event"].
- Bogdan occurs only in the literal logistics comment; no separate person-resolution request.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Lyrid Meteor Shower"
      },
      "teamId": {
        "eq": "b7c8d9e0-f1a2-3456-7890-abcdef123456"
      },
      "assigneeId": {
        "eq": "b8c9d0e1-f2a3-4567-2345-901234567890"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "April 22"
      },
      "description": {
        "contains": "Dark Sky Preserve"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "description": {
        "contains": "18 meteors/hour"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issue_label_issue_association",
    "where": {},
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "OBSERVATION_DETAILS:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Ridgeline Observatory"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "12-inch Dobsonian"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_51"></a>
## #159 — linear_51

The Clay & Fire pottery studio tracks their kiln schedule. Help update the firing queue.

First, find the existing issues "Fatou's Celadon Vase" and "Stoneware Bowl Set" in the Ceramics team.

The celadon vase is ready to go in the kiln - move it to "Firing" status.

The stoneware bowls have finished their cone 10 firing and need to cool down - move them to "Cooling" status.

Create a new label called "raku-firing" for pieces that will use the rapid-cooling technique (we'll apply it to future items).

Finally, add a kiln log comment to the celadon vase issue: "KILN_LOG: Loaded into kiln #2 at 9:15am. Target: Cone 9 oxidation (~2300°F). Fatou requested slow cooling for crystal development. Do not open kiln door until temp drops below 400°F."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L159) · [Cards](cards.md#linear_51)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Celadon Vase issue | resolved | `["cer-issue-vase-001"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Stoneware Bowl Set issue | resolved | `["cer-issue-bowls-002"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Ceramics Firing workflow state | resolved | `["cer-state-firing-1234-bcdef012"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve Ceramics Cooling workflow state | resolved | `["cer-state-cooling-2345-cdef0123"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Celadon Vase issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Celadon Vase'. Selection: Select the seeded issue whose title contains 'Celadon Vase'.
- **2.** Resolve Stoneware Bowl Set issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Stoneware Bowl Set'. Selection: Select the seeded issue whose title contains 'Stoneware Bowl Set'.
- **3.** Resolve Ceramics Firing workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Firing' in Ceramics; the target issue/team establishes this team context. Selection: Select workflow state 'Firing' in Ceramics; the target issue/team establishes this team context.
- **4.** Resolve Ceramics Cooling workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Cooling' in Ceramics; the target issue/team establishes this team context. Selection: Select workflow state 'Cooling' in Ceramics; the target issue/team establishes this team context.
- Ceramics scopes the two described issues/statuses; no separate team mutation or report is requested. Fatou qualifies the named vase issue.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "cer-issue-vase-001"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "cer-state-firing-1234-bcdef012"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "cer-issue-bowls-002"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "cer-state-cooling-2345-cdef0123"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "issue_labels",
    "where": {
      "name": {
        "eq": "raku-firing"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "KILN_LOG:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Cone 9"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "2300"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "crystal development"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_52"></a>
## #160 — linear_52

The Garden Plots team manages our community garden cooperative. It's spring reassignment season and we need to shuffle some plots around.

First, find the existing plot issues: "Plot A7 - Tomatoes", "Plot B3 - Herbs", and "Plot C1 - Squash".

Look up gardeners Ines and Rashida - they're involved in this season's reassignments.

Create a new tracking issue titled "Spring 2025 Plot Reassignment Tracker" in the Garden Plots team with description "Documenting all plot changes for the growing season. Reassignments finalized at March board meeting."

Now process the reassignments:

1. Plot A7 (tomatoes) was abandoned when Marcus moved away. Reassign it to Ines and change its status to "Active" since she's starting immediately.

2. Ines and Rashida agreed to swap their herb plots. Reassign "Plot B3 - Herbs" from Ines to Rashida. Keep the current status unchanged.

3. The squash plot (C1) owner has left the cooperative entirely. Move it to "Dormant" status but don't assign anyone yet - we'll offer it at the next meeting.

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L160) · [Cards](cards.md#linear_52)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Garden Plots team | resolved | `["d9e0f1a2-b3c4-5678-9012-cdef01234567"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Plot A7 issue | resolved | `["gp-issue-a7-tomatoes-001"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Plot B3 issue | resolved | `["gp-issue-b3-herbs-002"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve Plot C1 issue | resolved | `["gp-issue-c1-squash-003"]` | yes | A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 5. Resolve Ines | resolved | `["f0a1b2c3-d4e5-6789-4567-123456789012"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 6. Resolve Rashida | resolved | `["a1b2c3d4-e5f6-7890-5678-234567890123"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 7. Resolve Garden Plots Active workflow state | resolved | `["gp-state-active-0003-cdef0123"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 8. Resolve Garden Plots Dormant workflow state | resolved | `["gp-state-dormant-0001-abcdef01"]` | yes | A4: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Garden Plots team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Garden Plots"]. Selection: Select teams by teams.name matching ["Garden Plots"].
- **2.** Resolve Plot A7 issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Plot A7'. Selection: Select the seeded issue whose title contains 'Plot A7'.
- **3.** Resolve Plot B3 issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Plot B3'. Selection: Select the seeded issue whose title contains 'Plot B3'.
- **4.** Resolve Plot C1 issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Plot C1'. Selection: Select the seeded issue whose title contains 'Plot C1'.
- **5.** Resolve Ines. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Ines Ferreira"]. Selection: Select users by users.name, users.displayName matching ["Ines Ferreira"].
- **6.** Resolve Rashida. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Rashida Hassan"]. Selection: Select users by users.name, users.displayName matching ["Rashida Hassan"].
- **7.** Resolve Garden Plots Active workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Active' in Garden Plots; the target issue/team establishes this team context. Selection: Select workflow state 'Active' in Garden Plots; the target issue/team establishes this team context.
- **8.** Resolve Garden Plots Dormant workflow state. Use the described subject and the supported seed-level selector. Select workflow state 'Dormant' in Garden Plots; the target issue/team establishes this team context. Selection: Select workflow state 'Dormant' in Garden Plots; the target issue/team establishes this team context.
- Marcus is contextual former ownership, not a requested lookup. The unchanged current status on Plot B3 is a preservation constraint, not an independently described state to resolve.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "Spring 2025"
      },
      "teamId": {
        "eq": "d9e0f1a2-b3c4-5678-9012-cdef01234567"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "gp-issue-a7-tomatoes-001"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "to": {
          "eq": "f0a1b2c3-d4e5-6789-4567-123456789012"
        }
      },
      "stateId": {
        "to": {
          "eq": "gp-state-active-0003-cdef0123"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "gp-issue-b3-herbs-002"
      }
    },
    "expected_changes": {
      "assigneeId": {
        "to": {
          "eq": "a1b2c3d4-e5f6-7890-5678-234567890123"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "gp-issue-c1-squash-003"
      }
    },
    "expected_changes": {
      "stateId": {
        "to": {
          "eq": "gp-state-dormant-0001-abcdef01"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>

<a id="linear_53"></a>
## #161 — linear_53

The Meeple & Brew board game café has a scheduling emergency. The venue for our Catan Regional Championship double-booked us, so we need to reschedule the entire tournament pipeline.

Find the three tournament issues: "Catan Regional Championship - Spring 2025", "Qualifying Round - Top 16 Bracket", and "Tournament Registration Deadline".

The championship was originally March 15th but must move to March 23rd (8-day delay).

Here's the critical part - the dates are interdependent:
- The Qualifying Round must happen exactly 7 days before the Championship
- The Registration Deadline must close exactly 5 days before the Qualifying Round

Calculate and update all three due dates accordingly.

Also, Yuto was organizing the championship but has a work trip conflict on the new date. Reassign the championship to Adaeze. Keep Henrik on the qualifying round.

After updating all dates, add a comment to the championship issue documenting the changes:

"RESCHEDULE_AUDIT: Venue conflict forced 8-day delay. New timeline calculated:
- Registration closes: March 11th (was March 3rd)
- Qualifiers: March 16th (was March 8th)
- Championship: March 23rd (was March 15th)
Organizer handoff: Yuto → Adaeze due to travel conflict."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L161) · [Cards](cards.md#linear_53)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Catan Regional Championship issue | resolved | `["mb-issue-championship-001"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve Qualifying Round issue | resolved | `["mb-issue-qualifying-002"]` | yes | A2: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Tournament Registration Deadline issue | resolved | `["mb-issue-registration-003"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve Adaeze | resolved | `["d4e5f6a7-b8c9-0123-8901-567890123456"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 5. Resolve Henrik as the retained qualifying-round assignee | resolved | `["e5f6a7b8-c9d0-1234-9012-678901234567"]` | no | None: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve Catan Regional Championship issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Catan Regional Championship'. Selection: Select the seeded issue whose title contains 'Catan Regional Championship'.
- **2.** Resolve Qualifying Round issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Qualifying Round'. Selection: Select the seeded issue whose title contains 'Qualifying Round'.
- **3.** Resolve Tournament Registration Deadline issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Tournament Registration Deadline'. Selection: Select the seeded issue whose title contains 'Tournament Registration Deadline'.
- **4.** Resolve Adaeze. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Adaeze Obi"]. Selection: Select users by users.name, users.displayName matching ["Adaeze Obi"].
- **5.** Resolve Henrik as the retained qualifying-round assignee. Use the described subject and the supported seed-level selector. Select the explicitly named retained assignee Henrik; no assertion constrains preservation of his assignment. Selection: Select the explicitly named retained assignee Henrik; no assertion constrains preservation of his assignment.
- Yuto is the former owner and occurs in supplied audit text, not a separate requested target. The prompt’s explicit arithmetic and example both give March 11, 16, 23, 2025.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "mb-issue-championship-001"
      }
    },
    "expected_changes": {
      "dueDate": {
        "to": {
          "eq": "2025-03-23"
        }
      },
      "assigneeId": {
        "to": {
          "eq": "d4e5f6a7-b8c9-0123-8901-567890123456"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "mb-issue-qualifying-002"
      }
    },
    "expected_changes": {
      "dueDate": {
        "to": {
          "eq": "2025-03-16"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "mb-issue-registration-003"
      }
    },
    "expected_changes": {
      "dueDate": {
        "to": {
          "eq": "2025-03-11"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "RESCHEDULE_AUDIT:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Yuto"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Adaeze"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_54"></a>
## #162 — linear_54

The PMO is conducting a Q1 resource allocation review. Here's what needs to happen:

First, look at all teams and count how many members each team has.

Find the team with the most members - this is our "fully staffed" benchmark.

For every team that has FEWER members than the benchmark team, create a new issue in that team titled "Q1 Staffing Request - Need [X] additional team members" where [X] is the exact difference between that team's member count and the benchmark team's count. Set priority to High for these issues.

Also, there's a misrouted issue: "API Documentation Update" was accidentally created in the Design team but belongs in Engineering. Move it to the Engineering team.

Finally, add a comment to any issue in the Engineering team summarizing the analysis:

"RESOURCE_AUDIT: Q1 staffing review complete. Engineering has [MAX] members (benchmark). Staffing gaps identified: Product needs [A], Design needs [B], QA needs [C]. Total headcount gap across org: [TOTAL]. Staffing request issues created in all understaffed teams."

Replace the bracketed values with the actual numbers from your analysis. Note: [TOTAL] should be the sum of headcount gaps from ALL understaffed teams (not just Product, Design, and QA).

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L162) · [Cards](cards.md#linear_54)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve all teams for membership comparison | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8","cdb85540-5065-4346-8aef-ae2b72d6e940","58c03c85-7b0c-466d-9a4c-120209fccb56","a0b1c2d3-e4f5-6789-0123-456789abcdef","b1c2d3e4-f5a6-7890-1234-567890abcdef","f6a7b8c9-d0e1-2345-f012-678901234567","c2d3e4f5-a6b7-8901-2345-6789abcdef01","d3e4f5a6-b7c8-9012-3456-789abcdef012","e4f5a6b7-c8d9-0123-4567-89abcdef0123","f5a6b7c8-d9e0-1234-5678-9abcdef01234","a6b7c8d9-e0f1-2345-6789-0abcdef12345","b7c8d9e0-f1a2-3456-7890-abcdef123456","c8d9e0f1-a2b3-4567-8901-bcdef1234567","d9e0f1a2-b3c4-5678-9012-cdef01234567","e0f1a2b3-c4d5-6789-0123-def012345678","f1a2b3c4-d5e6-7890-1234-567890abcdef","a1b2c3d4-e5f6-7890-1234-567890abcdef","mod-team-001","race-team-001"]` | partial | A6, A7, A8, A9, A10: Some named counts are correct, but the all-team report is incomplete and A10 demands total 28 while the supplied seed yields 112. Separate comments can carry the fragments; no complete correct population report is enforced. |
| 2. Resolve the most-populated benchmark team | resolved | `["ad608998-915c-4bad-bcd9-85ebfccccee8"]` | yes | A1, A6: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve all understaffed destination teams | resolved | `["cdb85540-5065-4346-8aef-ae2b72d6e940","58c03c85-7b0c-466d-9a4c-120209fccb56","a0b1c2d3-e4f5-6789-0123-456789abcdef","b1c2d3e4-f5a6-7890-1234-567890abcdef","f6a7b8c9-d0e1-2345-f012-678901234567","c2d3e4f5-a6b7-8901-2345-6789abcdef01","d3e4f5a6-b7c8-9012-3456-789abcdef012","e4f5a6b7-c8d9-0123-4567-89abcdef0123","f5a6b7c8-d9e0-1234-5678-9abcdef01234","a6b7c8d9-e0f1-2345-6789-0abcdef12345","b7c8d9e0-f1a2-3456-7890-abcdef123456","c8d9e0f1-a2b3-4567-8901-bcdef1234567","d9e0f1a2-b3c4-5678-9012-cdef01234567","e0f1a2b3-c4d5-6789-0123-def012345678","f1a2b3c4-d5e6-7890-1234-567890abcdef","a1b2c3d4-e5f6-7890-1234-567890abcdef","mod-team-001","race-team-001"]` | partial | A2, A3, A4: Only Product, Design, and QA staffing issues are required; fifteen other understaffed teams are omitted, and no per-issue numeric gap is checked. |
| 4. Resolve API Documentation Update issue | resolved | `["res-issue-api-docs-001"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 5. Resolve an eligible Engineering issue for the resource audit | resolved | `["c6e168e3-fed4-45d0-b03f-a1c1f89ee7ab","5c62f29d-0f6a-4c4d-9d25-52293e2a8d4f","87c1d2f3-66c4-4dd0-bc93-1b99d04dc374","b4f5130f-5c1b-4bc0-a8f6-60a22b0adf5e","6fc548fb-49f1-48f7-b00f-0fe3b272ab0b","7d3f21ac-89c1-4f3b-9c2e-4fe3a1b71002","res-issue-api-docs-001","mod-issue-darkmode-001","mod-issue-checkout-001"]` | no | A5, A6, A7, A8, A9, A10: No assertion constrains this subject or its requested source-derived result. |

Boundary and selection notes:

- **1.** Resolve all teams for membership comparison. Use the described subject and the supported seed-level selector. Select all 19 supplied teams, including teams with zero membership rows. Selection: Select all 19 supplied teams, including teams with zero membership rows.
- **2.** Resolve the most-populated benchmark team. Use the described subject and the supported seed-level selector. Count memberships for each team and select the unique maximum, Engineering (7). The same team is the explicit move destination and is counted once. Selection: Count memberships for each team and select the unique maximum, Engineering (7). The same team is the explicit move destination and is counted once.
- **3.** Resolve all understaffed destination teams. Use the described subject and the supported seed-level selector. Select every team with membership count below Engineering’s 7; 18 teams qualify. Selection: Select every team with membership count below Engineering’s 7; 18 teams qualify.
- **4.** Resolve API Documentation Update issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'API Documentation Update'. Selection: Select the seeded issue whose title contains 'API Documentation Update'.
- **5.** Choose one Engineering issue; the candidate set includes the separately grounded API Documentation Update after its requested move into Engineering. Choose one existing Engineering issue as a permissible audit destination. The explicitly moved API Documentation Update is also eligible after the move; that subject is already grounded separately. Selection: Choose one existing Engineering issue as a permissible audit destination. The explicitly moved API Documentation Update is also eligible after the move; that subject is already grounded separately.
- Seed membership counts across all 19 teams give Engineering=7, Product=3, Design=2, QA=4, Growth=1, Moderation=1, Racing Operations=3 and twelve zero-member teams. Total staffing gap is 112, whereas A10 demands 28. Preserve this factual conflict; do not restrict the prompt’s explicit ALL-teams population to make 28 fit.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "res-issue-api-docs-001"
      }
    },
    "expected_changes": {
      "teamId": {
        "to": {
          "eq": "ad608998-915c-4bad-bcd9-85ebfccccee8"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "cdb85540-5065-4346-8aef-ae2b72d6e940"
      },
      "title": {
        "contains": "Staffing Request"
      },
      "priority": {
        "eq": 2
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "f1a2b3c4-d5e6-7890-1234-567890abcdef"
      },
      "title": {
        "contains": "Staffing Request"
      },
      "priority": {
        "eq": 2
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
      },
      "title": {
        "contains": "Staffing Request"
      },
      "priority": {
        "eq": 2
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "RESOURCE_AUDIT:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "7 members"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Product needs 4"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Design needs 5"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "QA needs 3"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Total headcount gap across org: 28"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_55"></a>
## #163 — linear_55

The moderation team has flagged the word "YOLO_BAD" as inappropriate for our workspace. We need to audit and address any comments containing this term.

First, search through all comments to find any that contain "YOLO_BAD". Count how many comments contain this word and note their IDs.

Create a new issue in the Moderation team titled "Content Cleanup Required - YOLO_BAD audit" assigned to Saoirse. In the description, include:
- The exact count of comments found containing "YOLO_BAD"
- A list of the comment IDs that need to be reviewed
- Use this format: "AUDIT_RESULT: Found [X] comments containing flagged content. Comment IDs: [id1, id2, ...]"

For each issue that has a comment containing "YOLO_BAD", add a warning comment: "MODERATION_NOTICE: A comment on this issue contains content that violates community guidelines. Please review and edit your comment to remove inappropriate language. Ref: YOLO_BAD audit."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L163) · [Cards](cards.md#linear_55)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve flagged comments for the count-and-ID report | resolved | `["mod-comment-bad-001","mod-comment-bad-002","mod-comment-bad-003"]` | partial | A4, A5: Found 3 comments checks the count fragment, but the requested three comment IDs are completely unchecked. |
| 2. Resolve Moderation team | resolved | `["mod-team-001"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 3. Resolve Saoirse | resolved | `["mod-user-saoirse-001"]` | yes | A3: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 4. Resolve issues with flagged comments for warnings | resolved | `["mod-issue-darkmode-001","mod-issue-checkout-001"]` | yes | A7, A8: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve flagged comments for the count-and-ID report. Use the described subject and the supported seed-level selector. Select all seeded comments containing YOLO_BAD; three comments match. Selection: Select all seeded comments containing YOLO_BAD; three comments match.
- **2.** Resolve Moderation team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Moderation"]. Selection: Select teams by teams.name matching ["Moderation"].
- **3.** Resolve Saoirse. Use the described subject and the supported seed-level selector. Select users by users.name, users.displayName matching ["Saoirse"]. Selection: Select users by users.name, users.displayName matching ["Saoirse"].
- **4.** Resolve issues with flagged comments for warnings. Use the described subject and the supported seed-level selector. Project the distinct issue IDs of YOLO_BAD comments; darkmode and checkout are the two targets. Selection: Project the distinct issue IDs of YOLO_BAD comments; darkmode and checkout are the two targets.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "mod-team-001"
      },
      "title": {
        "contains": "Content Cleanup"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "YOLO_BAD"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "assigneeId": {
        "eq": "mod-user-saoirse-001"
      },
      "title": {
        "contains": "Content Cleanup"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "description": {
        "contains": "AUDIT_RESULT:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "description": {
        "contains": "Found 3 comments"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "MODERATION_NOTICE:"
      }
    },
    "expected_count": 2
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "issueId": {
        "eq": "mod-issue-darkmode-001"
      },
      "body": {
        "contains": "MODERATION_NOTICE:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "issueId": {
        "eq": "mod-issue-checkout-001"
      },
      "body": {
        "contains": "MODERATION_NOTICE:"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="linear_56"></a>
## #164 — linear_56

The Wing & Wind pigeon racing club has an emergency. A fast-moving storm system is approaching the race corridor and we need to execute safety protocols.

First, find all birds currently marked as "In Flight" in the Racing Operations team - these are the ones at risk.

Create an emergency coordination issue in the Racing Operations team titled "WEATHER ALERT: Storm cell approaching sector 7 - All birds at risk" with description "NWS severe thunderstorm warning issued 14:32 UTC. Wind gusts to 60mph expected. Initiating emergency diversion protocol."

Find the bird tracking issue for "Stormchaser" (Liora's champion racer, band #2847). Update it to add this to the description: "DIVERSION ACTIVE: Rerouted to backup loft at coordinates 41.8781° N, 87.6298° W. Amadi's loft confirmed ready to receive."

Finally, add a weather advisory comment to the emergency coordination issue:
"WEATHER_LOG: Storm tracking update at 14:45 UTC. Cell moving NNE at 35mph. ETA to race corridor: 47 minutes. All handlers notified via SMS. GPS tracking shows 3 birds diverted successfully. Amadi confirming visual on Stormchaser approaching backup loft."

[Test entry](../../datasets/agent-diff-bench/all_numbered.jsonl#L164) · [Cards](cards.md#linear_56)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Racing Operations team | resolved | `["race-team-001"]` | yes | A1: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |
| 2. Resolve in-flight birds for review | resolved | `["race-issue-stormchaser-001","race-issue-quicksilver-001","race-issue-nightwing-001"]` | no | None: No assertion constrains this subject or its requested source-derived result. |
| 3. Resolve Stormchaser issue | resolved | `["race-issue-stormchaser-001"]` | yes | A5, A6, A10, A11: The resulting target or reference is explicitly constrained to the intended seeded subject. This does not certify every operation or output field. |

Boundary and selection notes:

- **1.** Resolve Racing Operations team. Use the described subject and the supported seed-level selector. Select teams by teams.name matching ["Racing Operations"]. Selection: Select teams by teams.name matching ["Racing Operations"].
- **2.** Resolve in-flight birds for review. Use the described subject and the supported seed-level selector. Select Racing Operations issues whose state is In Flight: Stormchaser, Quicksilver, Nightwing. Selection: Select Racing Operations issues whose state is In Flight: Stormchaser, Quicksilver, Nightwing.
- **3.** Resolve Stormchaser issue. Use the described subject and the supported seed-level selector. Select the seeded issue whose title contains 'Stormchaser'. Selection: Select the seeded issue whose title contains 'Stormchaser'.
- The weather figures, Amadi, and Liora appear as supplied text or issue qualifiers. They do not add independent person lookups.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "teamId": {
        "eq": "race-team-001"
      },
      "title": {
        "contains": "WEATHER ALERT"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "title": {
        "contains": "sector 7"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "description": {
        "contains": "NWS"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "issues",
    "where": {
      "description": {
        "contains": "60mph"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "race-issue-stormchaser-001"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "contains": "DIVERSION ACTIVE"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "race-issue-stormchaser-001"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "contains": "41.8781"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "WEATHER_LOG:"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "14:45 UTC"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "Amadi confirming"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "comments",
    "where": {
      "body": {
        "contains": "WEATHER_LOG:"
      },
      "issueId": {
        "eq": "race-issue-stormchaser-001"
      }
    },
    "expected_count": 0
  },
  {
    "diff_type": "changed",
    "entity": "issues",
    "where": {
      "id": {
        "eq": "race-issue-stormchaser-001"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "contains": "87.6298"
        }
      }
    },
    "expected_count": 1,
    "ignore": [
      "updatedAt"
    ]
  }
]
```

</details>
