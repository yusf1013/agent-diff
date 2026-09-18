# Box grounding obligations

See [method and source policy](README.md). These are benchmark annotations, not measurements of agent behavior. Cards use the locked schema in [cards.md](cards.md).

48 tests; 99 task-expressed obligations: 97 resolved, 2 absent, 0 underspecified. Assertions fully cover 54, partially cover 8, and leave 37 unchecked.

Coverage concerns the grounded contribution in the final state or requested output; it never requires a trajectory or source provenance. Full coverage does not certify whole-task correctness. See [the focused coverage audit](coverage_audit.md). The denominator includes unresolved and absent obligations. Zero-obligation tasks have no coverage ratio.

| # | Test | Obligations | Resolved | Absent | Underspecified | Full | Partial | Unchecked |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 60 | [box_116](#box_116) | 2 | 2 | 0 | 0 | 1 | 0 | 1 |
| 61 | [box_117](#box_117) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 62 | [box_118](#box_118) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 63 | [box_119](#box_119) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 64 | [box_120](#box_120) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 65 | [box_121](#box_121) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 66 | [box_122](#box_122) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 67 | [box_123](#box_123) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 68 | [box_124](#box_124) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 69 | [box_125](#box_125) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 70 | [box_126](#box_126) | 2 | 2 | 0 | 0 | 1 | 0 | 1 |
| 71 | [box_127](#box_127) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 72 | [box_128](#box_128) | 2 | 2 | 0 | 0 | 0 | 1 | 1 |
| 73 | [box_129](#box_129) | 2 | 2 | 0 | 0 | 0 | 1 | 1 |
| 74 | [box_130](#box_130) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 75 | [box_131](#box_131) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 76 | [box_132](#box_132) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 77 | [box_133](#box_133) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 78 | [box_134](#box_134) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 79 | [box_135](#box_135) | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 80 | [box_136](#box_136) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 81 | [box_137](#box_137) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 82 | [box_138](#box_138) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 83 | [box_139](#box_139) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 84 | [box_140](#box_140) | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 85 | [box_141](#box_141) | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 86 | [box_142](#box_142) | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 87 | [box_143](#box_143) | 3 | 3 | 0 | 0 | 2 | 0 | 1 |
| 88 | [box_144](#box_144) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 89 | [box_145](#box_145) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 90 | [box_146](#box_146) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 91 | [box_147](#box_147) | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 92 | [box_148](#box_148) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 93 | [box_149](#box_149) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 94 | [box_150](#box_150) | 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 95 | [box_151](#box_151) | 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 96 | [box_152](#box_152) | 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 97 | [box_153](#box_153) | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| 98 | [box_154](#box_154) | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 99 | [box_155](#box_155) | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 100 | [box_156](#box_156) | 4 | 4 | 0 | 0 | 3 | 0 | 1 |
| 101 | [box_157](#box_157) | 4 | 4 | 0 | 0 | 3 | 0 | 1 |
| 102 | [box_158](#box_158) | 8 | 8 | 0 | 0 | 2 | 0 | 6 |
| 103 | [box_159](#box_159) | 11 | 11 | 0 | 0 | 4 | 0 | 7 |
| 104 | [box_160](#box_160) | 8 | 8 | 0 | 0 | 2 | 0 | 6 |
| 105 | [box_161](#box_161) | 3 | 3 | 0 | 0 | 1 | 0 | 2 |
| 106 | [box_162](#box_162) | 3 | 2 | 1 | 0 | 2 | 0 | 1 |
| 107 | [box_163](#box_163) | 3 | 2 | 1 | 0 | 1 | 0 | 2 |

<a id="box_116"></a>
## #60 — box_116

Find out who I am logged in as, and create a folder named exactly equal to my display name in the root directory.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L60) · [Cards](cards.md#box_116)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the current user profile | resolved | `["27512847635"]` | yes | A1: A1 fixes the folder name to Admin User, the requested current-profile display name; no retrieval trace is needed. |
| 2. Resolve the root destination | resolved | `["0"]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve the current user profile. The selected reference is supported by the supplied seed and the stated selection rule. Select the current authenticated profile using the supplied actor context. Selection: Select the current authenticated profile using the supplied actor context.
- **2.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Admin User"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_117"></a>
## #61 — box_117

Create a new folder named 'Analysis_2026' inside the 'investments' folder.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L61) · [Cards](cards.md#box_117)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve investments folder | resolved | `["5610825569"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["investments"]. Selection: Select the described box_folders using box_folders.name: ["investments"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Analysis_2026"
      },
      "parent_id": {
        "eq": "5610825569"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_118"></a>
## #62 — box_118

Search for files with 'fomc' in the name. Add a comment 'Relevant' to the first file found.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L62) · [Cards](cards.md#box_118)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the FOMC document set | resolved | `["3379954793","2667428831","1246789615","1439014490"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Choose one of the four eligible FOMC files for the comment; do not require a particular retrieval order. Select PDF files whose names contain fomc under the investments/macroeconomics tree. Selection: Select PDF files whose names contain fomc under the investments/macroeconomics tree.
- Permissive choose-one boundary: no fixed search ordering is supplied; A1 accepts any of the four FOMC candidates.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "message": {
        "eq": "Relevant"
      },
      "item_id": {
        "in": [
          "3379954793",
          "2667428831",
          "1246789615",
          "1439014490"
        ]
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_119"></a>
## #63 — box_119

Add a comment 'Needs review' to the Google earnings report PDF in the investments folder.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L63) · [Cards](cards.md#box_119)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the Google earnings PDF | resolved | `["2748861636"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the Google earnings PDF. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["goog-10-q-q2-2025.pdf"]. Selection: Select the described box_files using box_files.name: ["goog-10-q-q2-2025.pdf"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "message": {
        "contains": "Needs review"
      },
      "item_id": {
        "eq": "2748861636"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_120"></a>
## #64 — box_120

Rename the 'macroeconomics' folder to 'Global Economics'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L64) · [Cards](cards.md#box_120)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve macroeconomics folder | resolved | `["1973339758"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["macroeconomics"]. Selection: Select the described box_folders using box_folders.name: ["macroeconomics"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "1973339758"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "Global Economics"
        }
      }
    }
  }
]
```

</details>

<a id="box_121"></a>
## #65 — box_121

Move the file 'transport-april-2025-csv.csv' into the 'investments' folder.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L65) · [Cards](cards.md#box_121)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the April transport CSV | resolved | `["1421498350"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve investments folder | resolved | `["5610825569"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the April transport CSV. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"]. Selection: Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"].
- **2.** Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["investments"]. Selection: Select the described box_folders using box_folders.name: ["investments"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1421498350"
      }
    },
    "expected_changes": {
      "parent_id": {
        "to": {
          "eq": "5610825569"
        }
      }
    }
  }
]
```

</details>

<a id="box_122"></a>
## #66 — box_122

Create a new Box Hub titled 'Research Center'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L66) · [Cards](cards.md#box_122)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| No existing-referent obligation | — | — | N/A | Only new outputs or supplied context; see notes |

Boundary and selection notes:

- Only a new hub is requested; no initial referent.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "eq": "Research Center"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_123"></a>
## #67 — box_123

Add the tags 'finance', 'investments', and 'quarterly' to the investments folder.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L67) · [Cards](cards.md#box_123)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve investments folder | resolved | `["5610825569"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["investments"]. Selection: Select the described box_folders using box_folders.name: ["investments"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "5610825569"
      }
    },
    "expected_changes": {
      "tags": {
        "to": {
          "contains": "finance"
        }
      }
    }
  }
]
```

</details>

<a id="box_124"></a>
## #68 — box_124

Get details for the 'investments' folder and change its description to 'Audit Complete'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L68) · [Cards](cards.md#box_124)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve investments folder | resolved | `["5610825569"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["investments"]. Selection: Select the described box_folders using box_folders.name: ["investments"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "5610825569"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "eq": "Audit Complete"
        }
      }
    }
  }
]
```

</details>

<a id="box_125"></a>
## #69 — box_125

In the history area, find the plain-text study notes about Argentina's 2001 economic crisis. Add a comment 'Please review this note' to that file and then create a task 'Review content' for the same file.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L69) · [Cards](cards.md#box_125)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the history study notes about Argentina’s 2001 crisis | resolved | `["5696874158"]` | yes | A1, A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the history study notes about Argentina’s 2001 crisis. The selected reference is supported by the supplied seed and the stated selection rule. Select the plain-text 2001 crisis notes directly under history; the matching root copy is excluded by location. Selection: Select the plain-text 2001 crisis notes directly under history; the matching root copy is excluded by location.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "5696874158"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_tasks",
    "where": {
      "item_id": {
        "eq": "5696874158"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_126"></a>
## #70 — box_126

Create a folder 'Project_Beta' in root, then create a subfolder 'Docs' inside it, and move 'interviewing tips FINAL.txt' into 'Docs'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L70) · [Cards](cards.md#box_126)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the root destination | resolved | `["0"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 2. Resolve interviewing tips FINAL.txt | resolved | `["1364279594"]` | yes | A3: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.
- **2.** Resolve interviewing tips FINAL.txt. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["interviewing tips FINAL.txt"]. Selection: Select the described box_files using box_files.name: ["interviewing tips FINAL.txt"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Project_Beta"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Docs"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1364279594"
      }
    },
    "expected_changes": {
      "parent_id": {
        "to": {
          "ne": "1088403890"
        }
      }
    }
  }
]
```

</details>

<a id="box_127"></a>
## #71 — box_127

Count how many files are in the 'investments' folder and set the folder's description to the count.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L71) · [Cards](cards.md#box_127)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve investments folder | resolved | `["5610825569"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve files in the investments area for counting | resolved | `["1376125085","2748861636","2772059170","7889164469","1414825331","1585447101","1352749393","2284320887","3205344472","3234744487","2215195296","2665143622","1812751520","1680035539","1731377376","2130264605","1818721808","2208613029","3131211280","3128241842","1698478564","2819267910","1193919506","2152227285","3056642419","2647359146","5500857985","1044921469","2323418229","3649010344","1962119681","1502930304","1494147682","1542940481","2396992486","1302660570","2941895851","1351294877","2127882706","9891894086","8259080169","1891960519","1064362959","4847599630","1115105829","1553809035","1484641315","3024573843","7099094335","1280559514","2641266627","6543141533","2064689726","2543780536","8695847712","1107398791","3379954793","2667428831","1246789615","1439014490","1490177849","1421498350"]` | partial | A1: A1 only requires a nonempty description on investments. A wrong nonempty count such as 999 meets the checked value condition. |

Boundary and selection notes:

- **1.** Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["investments"]. Selection: Select the described box_folders using box_folders.name: ["investments"].
- **2.** Resolve files in the investments area for counting. The selected reference is supported by the supplied seed and the stated selection rule. Select files under investments recursively through parent relationships. Selection: Select files under investments recursively through parent relationships.
- Use the investments subtree as the permissive file population, consistent with the explicit subtree extrema in box_137. A direct-children interpretation would contain no files; the coverage conclusion remains partial for the file-count source.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "5610825569"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "ne": ""
        }
      }
    }
  }
]
```

</details>

<a id="box_128"></a>
## #72 — box_128

List all accessible hubs and create a folder named 'Hubs_Found_<count>' in the root, where <count> is the number of hubs found.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L72) · [Cards](cards.md#box_128)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve accessible hubs for counting | resolved | `["999999","888888","777777"]` | partial | A1: Hubs_Found_999 meets the prefix predicate; the required seeded count 3 is not constrained. |
| 2. Resolve the root destination | resolved | `["0"]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve accessible hubs for counting. The selected reference is supported by the supplied seed and the stated selection rule. Select the whole supplied accessible hub population (three hubs). Selection: Select the whole supplied accessible hub population (three hubs).
- **2.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "contains": "Hubs_Found_"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_129"></a>
## #73 — box_129

Find all files with 'fomc' in their name. Create a new folder named 'FOMC_Reports' in the root directory, and move all found files into it.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L73) · [Cards](cards.md#box_129)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the FOMC document set | resolved | `["3379954793","2667428831","1246789615","1439014490"]` | partial | A2: A2 locates changed FOMC files but gives no explicit four-file requirement or linkage to the newly created FOMC_Reports folder. A proper subset is not ruled out by the stated predicates. |
| 2. Resolve the root destination | resolved | `["0"]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule. Select PDF files whose names contain fomc under the investments/macroeconomics tree. Selection: Select PDF files whose names contain fomc under the investments/macroeconomics tree.
- **2.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "FOMC_Reports"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "name": {
        "contains": "fomc"
      }
    },
    "expected_changes": {
      "parent_id": {
        "to": {
          "ne": "0"
        }
      }
    }
  }
]
```

</details>

<a id="box_130"></a>
## #74 — box_130

Search for 'crisis' in my Box, read the text files found, and if any contains the year '2001' but is NOT already in the history folder, move it there.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L74) · [Cards](cards.md#box_130)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve crisis text files containing 2001 outside history | resolved | `["9979104500"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve history folder | resolved | `["1660804823"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve crisis text files containing 2001 outside history. The selected reference is supported by the supplied seed and the stated selection rule. Select crisis-named plain-text files whose contents include 2001 and whose parent is not history; the root misfiled copy is the sole match. Selection: Select crisis-named plain-text files whose contents include 2001 and whose parent is not history; the root misfiled copy is the sole match.
- **2.** Resolve history folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["history"]. Selection: Select the described box_folders using box_folders.name: ["history"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "9979104500"
      }
    },
    "expected_changes": {
      "parent_id": {
        "to": {
          "eq": "1660804823"
        }
      }
    }
  }
]
```

</details>

<a id="box_131"></a>
## #75 — box_131

Create a Hub named 'Economic Data' and add the 'macroeconomics' folder to it.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L75) · [Cards](cards.md#box_131)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve macroeconomics folder | resolved | `["1973339758"]` | yes | A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["macroeconomics"]. Selection: Select the described box_folders using box_folders.name: ["macroeconomics"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "eq": "Economic Data"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_hub_items",
    "where": {
      "item_id": {
        "eq": "1973339758"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_132"></a>
## #76 — box_132

Search for all plain-text files about Argentina's 2001 economic crisis. You should find two copies - one properly filed in the history folder and one misfiled in the root. Delete the misfiled copy, then read the correctly filed one. If it mentions 'Argentina', add the tag 'Latin_America' to it.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L76) · [Cards](cards.md#box_132)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the misfiled root crisis copy | resolved | `["9979104500"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve the correctly filed history crisis notes | resolved | `["5696874158"]` | yes | A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the misfiled root crisis copy. The selected reference is supported by the supplied seed and the stated selection rule. Select the root crisis text copy; contents describe Argentina 2001 and its root parent distinguishes it. Selection: Select the root crisis text copy; contents describe Argentina 2001 and its root parent distinguishes it.
- **2.** Resolve the correctly filed history crisis notes. The selected reference is supported by the supplied seed and the stated selection rule. Select 2001 crisis notes in history. Its text contains Argentina, activating the tag branch. Selection: Select 2001 crisis notes in history. Its text contains Argentina, activating the tag branch.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "9979104500"
      }
    },
    "expected_changes": {
      "item_status": {
        "to": {
          "eq": "trashed"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "5696874158"
      }
    },
    "expected_changes": {
      "tags": {
        "to": {
          "contains": "Latin_America"
        }
      }
    }
  }
]
```

</details>

<a id="box_133"></a>
## #77 — box_133

In the investments area, locate the folder that contains macroeconomic CSV datasets. Find the CPI/price indexes CSV for December 2025, download/read it, and extract the first data row values for Series_reference and Series_title_1. Rename the macro-data folder to `macro_<Series_reference>` + `_` + `<Series_title_1>`, but replace '.' with '_' in the Series_reference. Then set the folder's description to: `series=<Series_reference>; title=<Series_title_1>`.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L77) · [Cards](cards.md#box_133)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve macroeconomics folder | resolved | `["1973339758"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve December 2025 price-index CSV | resolved | `["1490177849"]` | partial | A1: The renamed folder correctly checks both first-row values, but the requested description can omit title=Food while containing CPIM.SE901. This is missing final content, not missing source IDs. |

Boundary and selection notes:

- **1.** Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["macroeconomics"]. Selection: Select the described box_folders using box_folders.name: ["macroeconomics"].
- **2.** Resolve December 2025 price-index CSV. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["selected-price-indexes-december-2025.csv"]. Selection: Select the described box_files using box_files.name: ["selected-price-indexes-december-2025.csv"].
- The first CPI row is Series_reference=CPIM.SE901, Series_title_1=Food. A1 fully binds both in the new folder name but only checks the reference fragment in the separate description.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "1973339758"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "macro_CPIM_SE901_Food"
        }
      },
      "description": {
        "to": {
          "contains": "CPIM.SE901"
        }
      }
    }
  }
]
```

</details>

<a id="box_134"></a>
## #78 — box_134

In the macroeconomics area, there is a dataset folder that contains dozens of 2018 Census CSV files (national highlights / totals by topic). Find that dataset folder and rename it to 'Census_2018_Data'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L78) · [Cards](cards.md#box_134)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve 2018-census-totals-by-topic-national-highlights-csv folder | resolved | `["9782984299"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve 2018-census-totals-by-topic-national-highlights-csv folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["2018-census-totals-by-topic-national-highlights-csv"]. Selection: Select the described box_folders using box_folders.name: ["2018-census-totals-by-topic-national-highlights-csv"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "9782984299"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "Census_2018_Data"
        }
      }
    }
  }
]
```

</details>

<a id="box_135"></a>
## #79 — box_135

In the same macro-data folder, find the transport registrations CSV (it has columns like Series_reference, Period, Data_value). Download/read it and take the first data row values for Series_reference and Period. Upload a new small TXT file into the macro-data folder named `transport_<Series_reference>_<Period>.txt`, but replace '.' with '_' in both fields. The file content should include the extracted Series_reference, Period, and Data_value from that first row.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L79) · [Cards](cards.md#box_135)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve macroeconomics folder | resolved | `["1973339758"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve transport registrations source CSV | resolved | `["1421498350"]` | partial | A1: The output filename binds reference and period, but the uploaded content and Data_value=2771 are not checked. |

Boundary and selection notes:

- **1.** Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["macroeconomics"]. Selection: Select the described box_folders using box_folders.name: ["macroeconomics"].
- **2.** Resolve transport registrations source CSV. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"]. Selection: Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"].
- First transport row: Series_reference=TPTA.S22IA, Period=1970.12, Data_value=2771.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_files",
    "where": {
      "name": {
        "eq": "transport_TPTA_S22IA_1970_12.txt"
      },
      "parent_id": {
        "eq": "1973339758"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_136"></a>
## #80 — box_136

Find the transport dataset CSV from April 2025 (in the investments/macroeconomics area). Download/read it, count the total number of lines (INCLUDING the header), and add a comment to the file exactly in the format: `Line count: 44761`.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L80) · [Cards](cards.md#box_136)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve April 2025 transport CSV for line count | resolved | `["1421498350"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve April 2025 transport CSV for line count. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"]. Selection: Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "1421498350"
      },
      "message": {
        "eq": "Line count: 44761"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_137"></a>
## #81 — box_137

Look at the files in the 'investments' folder. Rename the smallest file to 'smallest_file' (keep extension) and the largest file to 'largest_file' (keep extension).

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L81) · [Cards](cards.md#box_137)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the smallest investments file | resolved | `["1064362959"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve the largest investments file | resolved | `["1490177849"]` | yes | A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the smallest investments file. The selected reference is supported by the supplied seed and the stated selection rule. Select the smallest file by seeded size over investments descendants; use the declared metadata, not local filesystem size. Selection: Select the smallest file by seeded size over investments descendants; use the declared metadata, not local filesystem size.
- **2.** Resolve the largest investments file. The selected reference is supported by the supplied seed and the stated selection rule. Select the largest file by seeded size over investments descendants; use the declared metadata, not local filesystem size. Selection: Select the largest file by seeded size over investments descendants; use the declared metadata, not local filesystem size.
- The adopted investments population includes descendants, corroborated by both asserted extrema.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1064362959"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "smallest_file.csv"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1490177849"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "largest_file.csv"
        }
      }
    }
  }
]
```

</details>

<a id="box_138"></a>
## #82 — box_138

Create a folder named 'Backup' in the root directory, and another folder named 'Backup' inside the 'investments' folder. Then, rename the 'Backup' folder that is inside 'investments' to 'Backup_in_investments'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L82) · [Cards](cards.md#box_138)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the root destination | resolved | `["0"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve investments folder | resolved | `["5610825569"]` | yes | A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.
- **2.** Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["investments"]. Selection: Select the described box_folders using box_folders.name: ["investments"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Backup"
      },
      "parent_id": {
        "eq": "0"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Backup_in_investments"
      },
      "parent_id": {
        "eq": "5610825569"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_139"></a>
## #83 — box_139

Hey, I uploaded some ethics and philosophy notes to history readings recently. I'm dyslexic so I probably made spelling mistakes in the filenames - could you find them and fix any typos? I think there were a few files about moral philosophy, judgment, research ethics, that kind of stuff.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L83) · [Cards](cards.md#box_139)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve misspelled ethics and philosophy filenames | resolved | `["6478815895","2228856784","1956298215","8847291035","9958302146"]` | yes | A1, A2, A3, A4, A5: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve misspelled ethics and philosophy filenames. The selected reference is supported by the supplied seed and the stated selection rule. Within the ethics folder, select moral judgement in histroy variants, phylosophy of sciance.md, and reserch ethics guidlines.txt. Other relevant names need no specified correction. Selection: Within the ethics folder, select moral judgement in histroy variants, phylosophy of sciance.md, and reserch ethics guidlines.txt. Other relevant names need no specified correction.
- Use the five asserted spelling corrections as a permissive mutation boundary; the seed supports the misspellings. Two seed size/hash discrepancies do not affect filename selection.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "6478815895"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "regex": "moral judge?ment in history\\.md"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "2228856784"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "regex": "moral judge?ment in history\\.docx"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1956298215"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "regex": "moral judge?ment in history\\.pdf"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "8847291035"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "philosophy of science.md"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "9958302146"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "research ethics guidelines.txt"
        }
      }
    }
  }
]
```

</details>

<a id="box_140"></a>
## #84 — box_140

In the personal_final history area, there is a digital humanities reading that was stored directly under the main 'history' folder instead of under 'readings/digital humanities'. Find the misfiled text reading about digital history methods and move it into the 'digital humanities' folder under 'readings'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L84) · [Cards](cards.md#box_140)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the misfiled digital history reading | resolved | `["2797160615"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve digital humanities folder | resolved | `["7905906319"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the misfiled digital history reading. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["digital history methods - week 3 reading.txt"]. Selection: Select the described box_files using box_files.name: ["digital history methods - week 3 reading.txt"].
- **2.** Resolve digital humanities folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["digital humanities"]. Selection: Select the described box_folders using box_folders.name: ["digital humanities"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "2797160615"
      }
    },
    "expected_changes": {
      "parent_id": {
        "to": {
          "eq": "7905906319"
        }
      }
    }
  }
]
```

</details>

<a id="box_141"></a>
## #85 — box_141

Create a new hub called 'Model Evaluations'. Find all the JSON files in the agent-diff-research folder that contain model evaluation results and add them to this new hub.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L85) · [Cards](cards.md#box_141)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve model-evaluation JSON files | resolved | `["8647156721","2466872085","2713928524","4373646747","3094163556","2112512450","1238342109","2211626350"]` | no | A2: A2 permits any eight file hub-item additions; it fixes neither these files nor their source folder. A generic file count is not source-derived result coverage. |

Boundary and selection notes:

- **1.** Resolve model-evaluation JSON files. The selected reference is supported by the supplied seed and the stated selection rule. Select the eight full_results JSON files in agent-diff-research; their role is seeded task documents. Selection: Select the eight full_results JSON files in agent-diff-research; their role is seeded task documents.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "contains": "Model Evaluations"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_hub_items",
    "where": {
      "item_type": {
        "eq": "file"
      }
    },
    "expected_count": {
      "min": 8
    }
  }
]
```

</details>

<a id="box_142"></a>
## #86 — box_142

In the readings folder under history, search for files with similar names across different subfolders (e.g., same base name in different topic folders). If you find duplicates by name, keep the one in the most appropriate topic folder and trash the others.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L86) · [Cards](cards.md#box_142)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the misfiled cross-folder duplicate reading | resolved | `["8847291036"]` | no | A1: A1 requires a trashed file without constraining name, source folder, or duplicate identity. |

Boundary and selection notes:

- **1.** Resolve the misfiled cross-folder duplicate reading. The selected reference is supported by the supplied seed and the stated selection rule. Match identical intro to hist methods.md names across ethics and methodology; keep the methodology copy and select the ethics copy for removal. Selection: Match identical intro to hist methods.md names across ethics and methodology; keep the methodology copy and select the ethics copy for removal.
- The assertion only requires a trashed file; it supplies no semantic duplicate boundary. The exact cross-folder duplicate intro to hist methods.md in ethics versus methodology supports a conservative target. Similar backup names within one folder are not cross-folder duplicates.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "item_status": {
        "eq": "trashed"
      }
    },
    "expected_changes": {
      "item_status": {
        "to": {
          "eq": "trashed"
        }
      }
    }
  }
]
```

</details>

<a id="box_143"></a>
## #87 — box_143

In the history/readings folder, reorganize all files by extension: create three folders 'PDFs', 'Word_Docs', and 'Markdown' directly in history/readings. Move ALL .pdf, .docx, and .md files from all subfolders into these new folders, flattening the structure. After moving the files, delete all the now-empty category subfolders.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L87) · [Cards](cards.md#box_143)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve readings folder | resolved | `["2113564020"]` | yes | A1, A2, A3: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve readings files for extension-based relocation | resolved | `["2204814480","8930492081","2503333498","2460105954","3266469077","9979104400","2228856784","6478815895","1956298215","2576277563","8847291035","8847291036","2219576536","2488685816","1723962562","6322534720","3166892170","9086815882","1822613980","2358251230","2408528068","8268998082","1898807902","2107290365","2350170522","1678816614","2166760427","7827931276","6154217723","2322959540"]` | no | A1: No assertion constrains this subject or its source-dependent result. |
| 3. Resolve category folders empty after the requested moves | resolved | `["7905906319"]` | yes | A4: A4 requires changed rows for all six unique category-folder IDs, necessarily including the sole intended empty folder; it also demands five extra removals, a whole-task discrepancy. |

Boundary and selection notes:

- **1.** Resolve readings folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["readings"]. Selection: Select the described box_folders using box_folders.name: ["readings"].
- **2.** Resolve readings files for extension-based relocation. The selected reference is supported by the supplied seed and the stated selection rule. Select all PDF, DOCX, and Markdown files in readings descendants. Selection: Select all PDF, DOCX, and Markdown files in readings descendants.
- **3.** Resolve category folders empty after the requested moves. The selected reference is supported by the supplied seed and the stated selection rule. Select readings category folders with no remaining children after removing the requested extensions. Only digital humanities qualifies. Selection: Select readings category folders with no remaining children after removing the requested extensions. Only digital humanities qualifies.
- After moving .pdf/.docx/.md files, only digital humanities becomes empty. The other five category folders retain .txt files. A4 demands all six removals, which exceeds the prompt’s now-empty condition; keep this discrepancy visible instead of expanding the intended target set.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "PDFs"
      },
      "parent_id": {
        "eq": "2113564020"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Word_Docs"
      },
      "parent_id": {
        "eq": "2113564020"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Markdown"
      },
      "parent_id": {
        "eq": "2113564020"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "in": [
          "7905906319",
          "3298967046",
          "1031140335",
          "2396378676",
          "1088403890",
          "7891120016"
        ]
      }
    },
    "expected_changes": {
      "item_status": {
        "to": {
          "eq": "trashed"
        }
      }
    },
    "expected_count": 6
  }
]
```

</details>

<a id="box_144"></a>
## #88 — box_144

Check the size of the file named 'transport-april-2025-csv.csv' inside 'investments'. If it's larger than 1MB, rename it to 'large_transport.csv', otherwise rename it to 'small_transport.csv'.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L88) · [Cards](cards.md#box_144)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the transport CSV for its size-conditioned rename | resolved | `["1421498350"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Seed size 6063648 exceeds either common 1MB threshold, activating only the large_transport.csv branch. Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"]. Selection: Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1421498350"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "large_transport.csv"
        }
      }
    }
  }
]
```

</details>

<a id="box_145"></a>
## #89 — box_145

In the history readings under digital humanities, there is a markdown file whose filename misspells the word 'computational' (letters swapped). Find it (try a couple search queries) and fix the typo in the filename without changing the content.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L89) · [Cards](cards.md#box_145)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the misspelled computational Markdown reading | resolved | `["3266469077"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the misspelled computational Markdown reading. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["computaional approaches to hist research.md"]. Selection: Select the described box_files using box_files.name: ["computaional approaches to hist research.md"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "3266469077"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "computational approaches to hist research.md"
        }
      }
    }
  }
]
```

</details>

<a id="box_146"></a>
## #90 — box_146

Upload a txt note saying 'Hi, I am working on history project' inside the history folder.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L90) · [Cards](cards.md#box_146)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve history folder | resolved | `["1660804823"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve history folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["history"]. Selection: Select the described box_folders using box_folders.name: ["history"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_files",
    "where": {
      "parent_id": {
        "eq": "1660804823"
      },
      "extension": {
        "eq": "txt"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_147"></a>
## #91 — box_147

Upload a small text file named 'tmp_delete_me.txt' to the root folder with content 'delete-me'. Then delete the file.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L91) · [Cards](cards.md#box_147)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the root destination | resolved | `["0"]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.
- The temporary file is newly created, then trashed; it is not an initial-state referent.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_files",
    "where": {
      "name": {
        "eq": "tmp_delete_me.txt"
      },
      "item_status": {
        "eq": "trashed"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_148"></a>
## #92 — box_148

Download the '2001 crisis notes.txt' file, append the line 'UPDATED: Version 2' to its content, and upload it as a new version of the same file.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L92) · [Cards](cards.md#box_148)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve 2001 crisis notes for a new version | resolved | `["5696874158"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the exact-named existing file. A1 fixes its identity and version change, but does not certify preservation of prior content or the appended line. Select the described box_files using box_files.name: ["2001 crisis notes.txt"]. Selection: Select the described box_files using box_files.name: ["2001 crisis notes.txt"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "5696874158"
      }
    },
    "expected_changes": {
      "version_number": {
        "to": {
          "ne": "1"
        }
      }
    },
    "ignore": [
      "sha_1",
      "size",
      "file_version_id"
    ]
  }
]
```

</details>

<a id="box_149"></a>
## #93 — box_149

In the history area, open the 'Buenos Aires' folder and identify any duplicate markdown files that appear to be copies of the same Dirty War class notes. Use clues like near-identical filenames and identical file size to decide which one is the duplicate copy. Keep the canonical original and delete/trash only the duplicate.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L93) · [Cards](cards.md#box_149)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the duplicate Dirty War Markdown notes | resolved | `["3320893579"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the duplicate Dirty War Markdown notes. The selected reference is supported by the supplied seed and the stated selection rule. Within Buenos Aires, compare the matching Dirty War Markdown names and equal seeded sizes (3163); select the (1) copy and keep the unsuffixed original. Selection: Within Buenos Aires, compare the matching Dirty War Markdown names and equal seeded sizes (3163); select the (1) copy and keep the unsuffixed original.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "3320893579"
      }
    },
    "expected_changes": {
      "item_status": {
        "to": {
          "eq": "trashed"
        }
      }
    }
  }
]
```

</details>

<a id="box_150"></a>
## #94 — box_150

Search for all FOMC minutes PDFs in the investments area. Create a hub called 'Fed Minutes Archive' and add all the FOMC documents to it.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L94) · [Cards](cards.md#box_150)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the FOMC document set | resolved | `["3379954793","2667428831","1246789615","1439014490"]` | partial | A2: A2 constrains item_name containing fomc and at least four hub-item rows, but does not require the four distinct seeded file IDs or a common destination hub. Repeated associations across hubs are not ruled out by the predicates. |

Boundary and selection notes:

- **1.** Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule. Select PDF files whose names contain fomc under the investments/macroeconomics tree. Selection: Select PDF files whose names contain fomc under the investments/macroeconomics tree.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "contains": "Fed Minutes"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_hub_items",
    "where": {
      "item_name": {
        "contains": "fomc"
      }
    },
    "expected_count": {
      "min": 4
    }
  }
]
```

</details>

<a id="box_151"></a>
## #95 — box_151

Find all PDF files in the investments folder and its subfolders. Add the tag 'pdf-document' to each of them.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L95) · [Cards](cards.md#box_151)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve investments PDF files | resolved | `["2748861636","3379954793","2667428831","1246789615","1439014490"]` | partial | A1: A1 constrains PDF extension and tag but neither the investments scope nor all five intended records; a different PDF or subset is not excluded. |

Boundary and selection notes:

- **1.** Resolve investments PDF files. The selected reference is supported by the supplied seed and the stated selection rule. Select all five PDFs under investments and descendants. Selection: Select all five PDFs under investments and descendants.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "extension": {
        "eq": "pdf"
      },
      "tags": {
        "contains": "pdf-document"
      }
    },
    "expected_changes": {
      "tags": {
        "to": {
          "contains": "pdf-document"
        }
      }
    }
  }
]
```

</details>

<a id="box_152"></a>
## #96 — box_152

For all FOMC minutes PDFs in macroeconomics, set their description to include the date from their filename (e.g., 'FOMC minutes from January 2025').

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L96) · [Cards](cards.md#box_152)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the FOMC document set | resolved | `["3379954793","2667428831","1246789615","1439014490"]` | partial | A1: A1 identifies changed fomc-named files but lacks an explicit four-file requirement and only checks FOMC in the description, not the requested filename-derived dates. |

Boundary and selection notes:

- **1.** Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule. Select PDF files whose names contain fomc under the investments/macroeconomics tree. Selection: Select PDF files whose names contain fomc under the investments/macroeconomics tree.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "name": {
        "contains": "fomc"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "contains": "FOMC"
        }
      }
    }
  }
]
```

</details>

<a id="box_153"></a>
## #97 — box_153

List all comments on the Google 10-Q PDF in investments. Create a folder named 'File_Has_<count>_Comments' where <count> is the number of comments found.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L97) · [Cards](cards.md#box_153)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve comments on the Google 10-Q PDF | resolved | `["1640914640"]` | no | A1: The literal Comments marker carries no count or referent information. File_Has_999_Comments meets it; even the File_Has prefix is not required. |

Boundary and selection notes:

- **1.** Resolve comments on the Google 10-Q PDF. The selected reference is supported by the supplied seed and the stated selection rule. Resolve goog-10-q-q2-2025.pdf, then select its comments by item_id; one is seeded. Selection: Resolve goog-10-q-q2-2025.pdf, then select its comments by item_id; one is seeded.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "contains": "Comments"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_154"></a>
## #98 — box_154

Find the plain-text study notes about Argentina's 2001 economic crisis (in the history area). Download/read the file and identify the protest slogan used during the December uprising. Post a comment on that file with the exact slogan text.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L98) · [Cards](cards.md#box_154)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Argentina crisis notes as slogan source and comment target | resolved | `["5696874158"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** The seed text supplies Que se vayan todos and A1 fixes both file identity and that slogan fragment; this does not certify all surrounding prose. Select the described box_files using box_files.name: ["2001 crisis notes.txt"]. Selection: Select the described box_files using box_files.name: ["2001 crisis notes.txt"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "5696874158"
      },
      "message": {
        "contains": "Que se vayan todos"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_155"></a>
## #99 — box_155

In the investments/macroeconomics area, locate all CSV files containing economic time-series data (files with columns 'Series_reference', 'Period', 'Data_value'). For each CSV file, download it and extract the domain code from the first data row's Series_reference value (the domain is everything before the first dot, e.g., 'CPIM' from 'CPIM.SE9A', or 'TTRC' from 'TTRC.S1A1A'). Create a new folder called 'Economic_Domains' in the root directory. Inside it, create one subfolder for each unique domain you discover, named exactly Domain_<CODE> (e.g., 'Domain_CPIM'). Move each CSV file into its corresponding domain subfolder, and add the tag domain:<CODE> to each file (e.g., tag domain:CPIM for files in the CPIM domain). After organising all files, create a Hub named 'Economic Data Index' and add only the domain subfolders that contain 2 or more files to this hub. Finally, upload a new text file named 'domain_manifest.txt' into the 'Economic_Domains' folder. This manifest should list each domain alphabetically, one per line, in the format: <DOMAIN>: <count> file(s) | Hub: <YES/NO>.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L99) · [Cards](cards.md#box_155)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve macroeconomic time-series CSVs | resolved | `["1107398791","1490177849","1421498350"]` | no | A1, A2, A3, A4: Only output names and generic domain-folder counts are checked. No source files, actual domain codes, routing, tags, or manifest content are constrained. |
| 2. Resolve the root destination | resolved | `["0"]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve macroeconomic time-series CSVs. The selected reference is supported by the supplied seed and the stated selection rule. Select macroeconomics CSVs with Series_reference, Period, Data_value columns; first rows give BDCQ, CPIM, TPTA, one file each. Selection: Select macroeconomics CSVs with Series_reference, Period, Data_value columns; first rows give BDCQ, CPIM, TPTA, one file each.
- **2.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.
- Every actual domain has one file, so no domain folder qualifies for the conditional hub-addition branch.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Economic_Domains"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "contains": "Domain_"
      }
    },
    "expected_count": {
      "min": 2
    }
  },
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "contains": "Economic Data Index"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_files",
    "where": {
      "name": {
        "eq": "domain_manifest.txt"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_156"></a>
## #100 — box_156

Your research institute's Box storage is disorganized. Somewhere in the archive, there are field research documents from cryptozoology expeditions — specifically sighting reports that may contain photographic evidence of unidentified creatures. Your task: Find a cryptozoology sighting report (search for relevant terms). Download and read its content. If the document mentions "photographic evidence" anywhere in the text, it should be tagged as verified; otherwise tag it unverified. Create a proper organizational structure: a main folder "Expeditions_2025" in the root, with a subfolder "Cryptid_Sightings" inside it. Move the sighting report into this subfolder with the appropriate tag. Add a comment to the file documenting your review: include today's date and the expedition name (which you'll find mentioned in the document's content). After moving the file, check its original location. If there are any obvious duplicate files (backup copies with similar names), delete them to clean up. Then rename the original source folder by appending "_archived" to its name. Finally, create a Hub called "2025 Field Research Index" and add the "Expeditions_2025" folder to it for easy access.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L100) · [Cards](cards.md#box_156)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the cryptozoology sighting report | resolved | `["3302188295"]` | yes | A3, A4: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve the root destination | resolved | `["0"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 3. Resolve the obvious backup of the sighting report | resolved | `["1891733744"]` | yes | A5: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 4. Resolve cryptozoology_raw folder | resolved | `["4313494130"]` | yes | A6: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** The Pacific Northwest report is the asserted permissive sighting target. Its content includes photographic evidence and expedition Sasquatch Survey NW-7, activating verified tagging. Identity is checked; tag correctness and review text are not certified. Select the described box_files using box_files.name: ["pacific_northwest_sighting_march2025.txt"]. Selection: Select the described box_files using box_files.name: ["pacific_northwest_sighting_march2025.txt"].
- **2.** Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule. Use the documented root-folder handle 0 explicitly requested by the prompt. Selection: Use the documented root-folder handle 0 explicitly requested by the prompt.
- **3.** Resolve the obvious backup of the sighting report. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["pacific_northwest_sighting_march2025_backup.txt"]. Selection: Select the described box_files using box_files.name: ["pacific_northwest_sighting_march2025_backup.txt"].
- **4.** Resolve cryptozoology_raw folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["cryptozoology_raw"]. Selection: Select the described box_folders using box_folders.name: ["cryptozoology_raw"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Expeditions_2025"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Cryptid_Sightings"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "3302188295"
      }
    },
    "expected_changes": {
      "tags": {
        "to": {
          "ne": null
        }
      }
    },
    "ignore": [
      "parent_id"
    ]
  },
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "3302188295"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1891733744"
      }
    },
    "expected_changes": {
      "item_status": {
        "to": {
          "eq": "trashed"
        }
      }
    }
  },
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "4313494130"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "contains": "archived"
        }
      }
    }
  },
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "contains": "2025 Field Research Index"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_157"></a>
## #101 — box_157

The tea ceremony school is transitioning to Ro season (炉, the winter hearth period). You need to help organize the digital materials for this important seasonal change. First, find which hub already exists for tea ceremony seasonal materials — you'll need to add updated content there later. Locate the winter preparation guide in the chado folder. Verify it's the current document (not a draft), then update it with the tag winter_season and set its description to "Ro season preparation - 炉 (November-April)". Add a comment to the winter preparation guide noting: "Ready for Ro season (炉) - charcoal placement verified." Next, find the utensil inventory file. Add a comment reminding the team: "Utensils require cleaning before Hatsugama ceremony." There's an old draft file in the same folder that has been superseded — it's clearly marked as obsolete. Delete it to clean up the archive. Finally, add the winter preparation guide to the seasonal materials hub so it's easily accessible to all practitioners.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L101) · [Cards](cards.md#box_157)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve the existing seasonal tea-materials hub | resolved | `["888888"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 2. Resolve the current winter preparation guide | resolved | `["3180616460"]` | yes | A1, A2, A5: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 3. Resolve the utensil inventory | resolved | `["3309661031"]` | yes | A3: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 4. Resolve the obsolete winter draft | resolved | `["1018029878"]` | yes | A4: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve the existing seasonal tea-materials hub. The selected reference is supported by the supplied seed and the stated selection rule. Match Chado Seasonal Materials title and its tea ceremony seasonal description. Selection: Match Chado Seasonal Materials title and its tea ceremony seasonal description.
- **2.** Resolve the current winter preparation guide. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["winter_preparation_guide.txt"]. Selection: Select the described box_files using box_files.name: ["winter_preparation_guide.txt"].
- **3.** Resolve the utensil inventory. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["utensil_inventory_2025.txt"]. Selection: Select the described box_files using box_files.name: ["utensil_inventory_2025.txt"].
- **4.** Resolve the obsolete winter draft. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["winter_prep_DRAFT_old.txt"]. Selection: Select the described box_files using box_files.name: ["winter_prep_DRAFT_old.txt"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "3180616460"
      }
    },
    "expected_changes": {
      "tags": {
        "to": {
          "contains": "winter_season"
        }
      },
      "description": {
        "to": {
          "contains": "Ro season"
        }
      }
    },
    "ignore": [
      "parent_id",
      "shared_link"
    ]
  },
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "3180616460"
      },
      "message": {
        "contains": "charcoal"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "3309661031"
      },
      "message": {
        "contains": "Hatsugama"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1018029878"
      }
    },
    "expected_changes": {
      "item_status": {
        "to": {
          "eq": "trashed"
        }
      }
    }
  },
  {
    "diff_type": "added",
    "entity": "box_hub_items",
    "where": {
      "item_id": {
        "eq": "3180616460"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_158"></a>
## #102 — box_158

You're helping manage the documentation for a Moog Minimoog restoration project. The synth is from 1974 (serial 10847) and the team has been tracking repairs and calibrations in Box. First, search for files related to the Minimoog or Moog restoration. Get the details of the project folder to understand what's there. Check if any synth restoration documents are in your favorites collection. On the capacitor replacement log, add a new comment documenting: "C47 replaced with Nichicon 47µF/25V - oscillator section complete." Then find the existing comment about "C31 verified" and update it to add: "- measurement confirmed at 0.98x nominal." For the filter calibration procedure file, there are two pending tasks. Find the task about "resonance calibration" and mark it as complete. Find the task about "cutoff tracking" and update its message to: "Cutoff tracking verified ±3 cents across 5 octaves - exceeds spec." Add the tag restoration-complete to the oscillator schematic notes file since that section is now finished. Finally, create a new hub called "Synth Restoration Archive" to centralize all vintage instrument documentation going forward.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L102) · [Cards](cards.md#box_158)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Minimoog restoration documents for review | resolved | `["1062973727","3212140342","2666248889"]` | no | A1: No assertion constrains this subject or its source-dependent result. |
| 2. Resolve the Minimoog project folder | resolved | `["9559162103"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 3. Resolve Favorites for the restoration-document check | resolved | `["926489"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 4. Resolve the capacitor replacement log | resolved | `["1062973727"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 5. Resolve the C31 verified comment | resolved | `["2656068403"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 6. Resolve the resonance calibration task | resolved | `["1828124557"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 7. Resolve the cutoff tracking task | resolved | `["8610023888"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 8. Resolve oscillator schematic notes | resolved | `["2666248889"]` | yes | A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve Minimoog restoration documents for review. The selected reference is supported by the supplied seed and the stated selection rule. Select the three files in moog_minimoog_1974 as the explicitly requested search population. Selection: Select the three files in moog_minimoog_1974 as the explicitly requested search population.
- **2.** Resolve the Minimoog project folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["moog_minimoog_1974"]. Selection: Select the described box_folders using box_folders.name: ["moog_minimoog_1974"].
- **3.** Resolve Favorites for the restoration-document check. The selected reference is supported by the supplied seed and the stated selection rule. Select the collection named Favorites; related membership requires the documented collections projection. Selection: Select the collection named Favorites; related membership requires the documented collections projection.
- **4.** Resolve the capacitor replacement log. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["capacitor_replacement_log.txt"]. Selection: Select the described box_files using box_files.name: ["capacitor_replacement_log.txt"].
- **5.** Resolve the C31 verified comment. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_comments using box_comments.message, box_comments.item_id, box_files.name, box_files.id: ["C31 verified - within spec"]. Selection: Select the described box_comments using box_comments.message, box_comments.item_id, box_files.name, box_files.id: ["C31 verified - within spec"].
- **6.** Resolve the resonance calibration task. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_tasks using box_tasks.message, box_tasks.item_id, box_files.id, box_files.name: ["Complete resonance calibration sign-off"]. Selection: Select the described box_tasks using box_tasks.message, box_tasks.item_id, box_files.id, box_files.name: ["Complete resonance calibration sign-off"].
- **7.** Resolve the cutoff tracking task. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_tasks using box_tasks.message, box_tasks.item_id, box_files.id, box_files.name: ["Verify cutoff tracking across octaves"]. Selection: Select the described box_tasks using box_tasks.message, box_tasks.item_id, box_files.id, box_files.name: ["Verify cutoff tracking across octaves"].
- **8.** Resolve oscillator schematic notes. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["oscillator_schematic_notes.txt"]. Selection: Select the described box_files using box_files.name: ["oscillator_schematic_notes.txt"].

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "1062973727"
      },
      "message": {
        "contains": "C47"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "2666248889"
      }
    },
    "expected_changes": {
      "tags": {
        "to": {
          "contains": "restoration-complete"
        }
      }
    }
  },
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "contains": "Synth Restoration Archive"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_159"></a>
## #103 — box_159

The rare book conservation lab is running its year-end audit. You need to aggregate treatment data and update the annual summary. First, confirm your identity — who are you logged in as? You'll need this for audit attribution. Locate the conservation lab folder and check its contents. Get the details of both quarterly humidity logs (Q3 and Q4 2025) — each contains a "BOOKS TREATED THIS QUARTER" count that you'll need. Check if any conservation documents are currently in your favorites collection. On the incunabula condition report, add a comment: "Audit initiated by [your username] on [today's date]." Also find the existing comment about "Budget review pending" and update it to: "Budget approved - Q3+Q4 aggregated total: [X] books" where X is the sum of books treated in Q3 and Q4. There's an outdated comment on the condition report marked "[OUTDATED]" with incorrect information — delete it. Download the annual summary file, update it with the correct Q3 and Q4 treatment counts (extracted from the humidity logs), and upload it as a new version. The total YTD should now reflect all four quarters. Find the "Conservation Lab Archive" hub and update its description to: "Rare book conservation documentation - Last audit: Q4 2025." Finally, there's a deprecated folder from 2024 that's scheduled for deletion — remove it.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L103) · [Cards](cards.md#box_159)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve current user for audit attribution | resolved | `["27512847635"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 2. Resolve the conservation folder for review | resolved | `["3578701092"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 3. Resolve the Q3 2025 humidity log | resolved | `["2679438618"]` | no | A1: No assertion constrains this subject or its source-dependent result. |
| 4. Resolve the Q4 2025 humidity log | resolved | `["1747153578"]` | no | A1: No assertion constrains this subject or its source-dependent result. |
| 5. Resolve Favorites for conservation-document review | resolved | `["926489"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 6. Resolve the incunabula condition report | resolved | `["1701916585"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 7. Resolve the Budget review pending comment | resolved | `["7404947855"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 8. Resolve the outdated condition-report comment | resolved | `["2912801714"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 9. Resolve annual summary for updating treatment totals | resolved | `["1172138282"]` | yes | A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 10. Resolve Conservation Lab Archive | resolved | `["777777"]` | yes | A3: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 11. Resolve deprecated_2024 folder | resolved | `["7983826892"]` | yes | A4: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |

Boundary and selection notes:

- **1.** Resolve current user for audit attribution. The selected reference is supported by the supplied seed and the stated selection rule. Select the supplied authenticated user profile. Selection: Select the supplied authenticated user profile.
- **2.** Resolve the conservation folder for review. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["rare_books_conservation"]. Selection: Select the described box_folders using box_folders.name: ["rare_books_conservation"].
- **3.** Resolve the Q3 2025 humidity log. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["humidity_log_q3_2025.txt"]. Selection: Select the described box_files using box_files.name: ["humidity_log_q3_2025.txt"].
- **4.** Resolve the Q4 2025 humidity log. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["humidity_log_q4_2025.txt"]. Selection: Select the described box_files using box_files.name: ["humidity_log_q4_2025.txt"].
- **5.** Resolve Favorites for conservation-document review. The selected reference is supported by the supplied seed and the stated selection rule. Select the collection named Favorites and use documented file collections membership. Selection: Select the collection named Favorites and use documented file collections membership.
- **6.** Resolve the incunabula condition report. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["condition_report_incunabula.txt"]. Selection: Select the described box_files using box_files.name: ["condition_report_incunabula.txt"].
- **7.** Resolve the Budget review pending comment. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_comments using box_comments.message: ["Budget review pending - awaiting Q3/Q4 data"]. Selection: Select the described box_comments using box_comments.message: ["Budget review pending - awaiting Q3/Q4 data"].
- **8.** Resolve the outdated condition-report comment. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_comments using box_comments.message, box_comments.item_id, box_files.id, box_files.name: ["[OUTDATED] Previous assessment showed 5 priority items - this was incorrect"]. Selection: Select the described box_comments using box_comments.message, box_comments.item_id, box_files.id, box_files.name: ["[OUTDATED] Previous assessment showed 5 priority items - this was incorrect"].
- **9.** Resolve annual summary for updating treatment totals. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["annual_summary_2025.txt"]. Selection: Select the described box_files using box_files.name: ["annual_summary_2025.txt"].
- **10.** Resolve Conservation Lab Archive. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_hubs using box_hubs.title: ["Conservation Lab Archive"]. Selection: Select the described box_hubs using box_hubs.title: ["Conservation Lab Archive"].
- **11.** Resolve deprecated_2024 folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["deprecated_2024"]. Selection: Select the described box_folders using box_folders.name: ["deprecated_2024"].
- Seeded Q3=23, Q4=17, Q3+Q4=40; annual summary Q1=19 and Q2=21, yielding YTD=80. Favorites membership is not explicitly populated in the seed; do not infer runtime defaults.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "1701916585"
      },
      "message": {
        "contains": "Audit initiated"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1172138282"
      }
    },
    "expected_changes": {
      "version_number": {
        "to": {
          "ne": "1"
        }
      }
    },
    "ignore": [
      "sha_1",
      "size",
      "file_version_id"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "box_hubs",
    "where": {
      "id": {
        "eq": "777777"
      }
    },
    "expected_changes": {
      "description": {
        "to": {
          "contains": "Q4 2025"
        }
      }
    },
    "ignore": [
      "updated_at"
    ]
  },
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "7983826892"
      }
    },
    "expected_changes": {
      "item_status": {
        "to": {
          "eq": "trashed"
        }
      }
    }
  }
]
```

</details>

<a id="box_160"></a>
## #104 — box_160

Your history research archive in Box is disorganized and needs cleanup. You have redundant folders, misfiled documents, and obsolete tasks cluttering the system. In the history area, there are two folders that seem to contain overlapping Buenos Aires research: one called "BA" and one called "Buenos Aires". Consolidate them by moving the entire "BA" folder into "Buenos Aires" as a subfolder, then rename the "BA" folder to "Legacy_Materials" to indicate it contains older content. In the readings area, list the contents and look for organizational issues. The file "digital history methods - week 3 reading.txt" is sitting at the top level of the history folder but belongs in the "digital humanities" subfolder under readings. Move this file to its correct location. Create a new folder called "Archive_Cleanup_2026" in the root of the history folder to track this reorganization effort. Inside it, create a subfolder called "Duplicates_Review" where duplicate files can be moved for review. Look through the seed for files marked as duplicates (files with "(1)" in the name or "backup"/"copy" in the name). These files have obsolete tasks attached. Find and delete the tasks marked "[OBSOLETE]" or "[OUTDATED]" since the reorganization will handle these files differently. Check what hubs currently exist — you may want to add reorganized materials to an appropriate hub later.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L104) · [Cards](cards.md#box_160)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve BA folder | resolved | `["2228309175"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve Buenos Aires folder | resolved | `["1206853609"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 3. Resolve readings as the review source | resolved | `["2113564020"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 4. Resolve the misfiled digital history methods reading | resolved | `["2797160615"]` | no | A1: No assertion constrains this subject or its source-dependent result. |
| 5. Resolve digital humanities folder | resolved | `["7905906319"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 6. Resolve history folder | resolved | `["1660804823"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 7. Resolve obsolete tasks attached to duplicate-marked files | resolved | `["3292462467","1751119378","1884936347","1177785842"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 8. Resolve existing hubs for review | resolved | `["999999","888888","777777"]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve BA folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["BA"]. Selection: Select the described box_folders using box_folders.name: ["BA"].
- **2.** Resolve Buenos Aires folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["Buenos Aires"]. Selection: Select the described box_folders using box_folders.name: ["Buenos Aires"].
- **3.** Resolve readings as the review source. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["readings"]. Selection: Select the described box_folders using box_folders.name: ["readings"].
- **4.** Resolve the misfiled digital history methods reading. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["digital history methods - week 3 reading.txt"]. Selection: Select the described box_files using box_files.name: ["digital history methods - week 3 reading.txt"].
- **5.** Resolve digital humanities folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["digital humanities"]. Selection: Select the described box_folders using box_folders.name: ["digital humanities"].
- **6.** Resolve history folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["history"]. Selection: Select the described box_folders using box_folders.name: ["history"].
- **7.** Resolve obsolete tasks attached to duplicate-marked files. The selected reference is supported by the supplied seed and the stated selection rule. Select tasks containing [OBSOLETE] or [OUTDATED] attached to files whose names contain (1), backup, or copy. Selection: Select tasks containing [OBSOLETE] or [OUTDATED] attached to files whose names contain (1), backup, or copy.
- **8.** Resolve existing hubs for review. The selected reference is supported by the supplied seed and the stated selection rule. Select all three supplied accessible hubs; later additions are only tentative. Selection: Select all three supplied accessible hubs; later additions are only tentative.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "2228309175"
      }
    },
    "expected_changes": {
      "parent_id": {
        "to": {
          "eq": "1206853609"
        }
      },
      "name": {
        "to": {
          "eq": "Legacy_Materials"
        }
      }
    }
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Archive_Cleanup_2026"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "Duplicates_Review"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_161"></a>
## #105 — box_161

You are preparing the final conservation audit for external review. First, confirm your identity — get your current user details. Locate the "Annual Summary 2025" file in the rare books folder. Create a shared link for this file with access set to "open" so external auditors can view it. Then, check your "Favorites" collection. If the Annual Summary is not already in your favorites, add it to the collection for quick access. Finally, verify the file's details to confirm the shared link is active and the file is listed in the collection.

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L105) · [Cards](cards.md#box_161)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve current user details | resolved | `["27512847635"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 2. Resolve Annual Summary 2025 | resolved | `["1172138282"]` | yes | A1: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 3. Resolve Favorites for the membership check and conditional addition | resolved | `["926489"]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve current user details. The selected reference is supported by the supplied seed and the stated selection rule. Select the authenticated user profile. Selection: Select the authenticated user profile.
- **2.** Resolve Annual Summary 2025. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_files using box_files.name: ["annual_summary_2025.txt"]. Selection: Select the described box_files using box_files.name: ["annual_summary_2025.txt"].
- **3.** Resolve Favorites for the membership check and conditional addition. The selected reference is supported by the supplied seed and the stated selection rule. Select the named Favorites collection. Membership is a documented file projection, not inferred from omitted seed values. Selection: Select the named Favorites collection. Membership is a documented file projection, not inferred from omitted seed values.
- Favorites membership is not explicitly represented in the supplied seed, so the conditional addition cannot be established from a runtime default. Retain the collection obligation while recording the unsettled condition.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "1172138282"
      }
    },
    "expected_changes": {
      "shared_link": {
        "from": {
          "exists": false
        },
        "to": {
          "exists": true
        }
      }
    },
    "ignore": [
      "collections"
    ]
  }
]
```

</details>

<a id="box_162"></a>
## #106 — box_162

You are reorganizing the institute's demographic data assets. The goal is to consolidate disparate 2018 Census files and April 2025 transport data into a unified structure. First, create a new Hub called "Demographics 2025". This will be the central access point. In the macroeconomics area, there is a folder containing 2018 Census CSV files (look for a folder with many CSVs). Rename this folder to "Census_2018_Master". Inside "Census_2018_Master", create a subfolder called "National_Highlights". Now, search for and identify the "transport-april-2025-csv.csv" file. Download/read it to extract the first row's Series_reference. Task 1 (Left Branch): Move the transport file into "Census_2018_Master". Add a comment to it: "Transport series [Series_reference] included for cross-reference." Task 2 (Right Branch): Find any file in the census folder that contains "population" in its name. Move it into the "National_Highlights" subfolder you created. Finally, create a new text file named "hub_manifest.txt" inside "Census_2018_Master" with the content: "Consolidated: Census 2018 + Transport 2025." Update the "Demographics 2025" hub description to: "Unified demographic and transport datasets." 

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L106) · [Cards](cards.md#box_162)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve 2018-census-totals-by-topic-national-highlights-csv folder | resolved | `["9782984299"]` | yes | A2: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve transport CSV for relocation and series comment | resolved | `["1421498350"]` | yes | A4: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 3. Resolve an eligible population-named census file | absent | `[]` | no | A1: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** Resolve 2018-census-totals-by-topic-national-highlights-csv folder. The selected reference is supported by the supplied seed and the stated selection rule. Select the described box_folders using box_folders.name: ["2018-census-totals-by-topic-national-highlights-csv"]. Selection: Select the described box_folders using box_folders.name: ["2018-census-totals-by-topic-national-highlights-csv"].
- **2.** A4 fixes the source/target file identity but the Transport series marker does not check its first-row reference. Full identity coverage does not certify that computation. Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"]. Selection: Select the described box_files using box_files.name: ["transport-april-2025-csv.csv"].
- **3.** Choose one eligible population-named file if present. The concrete filename condition has no match in the census folder, so this is absent, not underspecified. Within the census folder, select filenames containing population; none of the 54 supplied census filenames matches. Selection: Within the census folder, select filenames containing population; none of the 54 supplied census filenames matches.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "contains": "Demographics 2025"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "changed",
    "entity": "box_folders",
    "where": {
      "id": {
        "eq": "9782984299"
      }
    },
    "expected_changes": {
      "name": {
        "to": {
          "eq": "Census_2018_Master"
        }
      }
    }
  },
  {
    "diff_type": "added",
    "entity": "box_folders",
    "where": {
      "name": {
        "eq": "National_Highlights"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "1421498350"
      },
      "message": {
        "contains": "Transport series"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_files",
    "where": {
      "name": {
        "eq": "hub_manifest.txt"
      }
    },
    "expected_count": 1
  }
]
```

</details>

<a id="box_163"></a>
## #107 — box_163

You are auditing the "investments" folder for the upcoming financial review. Locate the Google earnings report PDF (goog-10-q-q2-2025.pdf). Get its file details to check its size. Condition 1: If the file size is greater than 1MB (1,048,576 bytes), add the tag large_audit. Condition 2: If the file size is less than or equal to 1MB, add the tag standard_audit. Next, create a new Hub called "Q2 Financial Review". Search for all files with "fomc" in their name. For each file found, add it to the "Q2 Financial Review" hub. Find the "Analysis_2026" folder (if it exists, otherwise create it). Inside, upload a new text file named audit_summary.txt. The content should be: "Audit complete. Google report size: [SIZE_IN_BYTES] bytes." Finally, add a comment to the Google earnings report: "Audit status: Tagged based on size ([SIZE_IN_BYTES]b)." 

[Test entry](../../../../datasets/agent-diff-bench/all_numbered.jsonl#L107) · [Cards](cards.md#box_163)

| Obligation | Resolution | Referent set | Assertion coverage | Assertion evidence |
|---|---|---|---|---|
| 1. Resolve Google earnings PDF for size-based audit | resolved | `["2748861636"]` | yes | A1, A4: The predicate fixes the resulting record or destination to the intended seeded referent. This covers identity, not every requested field or operation linkage. |
| 2. Resolve the FOMC document set | resolved | `["3379954793","2667428831","1246789615","1439014490"]` | no | None: No assertion constrains this subject or its source-dependent result. |
| 3. Resolve Analysis_2026 folder | absent | `[]` | no | None: No assertion constrains this subject or its source-dependent result. |

Boundary and selection notes:

- **1.** A1 and A4 fix the file identity. They do not check the correct size-derived tag, size text, or manifest content. Select the described box_files using box_files.name: ["goog-10-q-q2-2025.pdf"]. Selection: Select the described box_files using box_files.name: ["goog-10-q-q2-2025.pdf"].
- **2.** Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule. Select PDF files whose names contain fomc under the investments/macroeconomics tree. Selection: Select PDF files whose names contain fomc under the investments/macroeconomics tree.
- **3.** Resolve Analysis_2026 folder. The described subject has no seeded match. Select the described box_folders using box_folders.name: []. Selection: Select the described box_folders using box_folders.name: [].
- Google PDF seeded size is 676600 bytes, activating standard_audit. Analysis_2026 is absent in this seed; creation supplies its later handle.

<details><summary>Assertion predicates from the test entry (A1, A2, …)</summary>

```json
[
  {
    "diff_type": "changed",
    "entity": "box_files",
    "where": {
      "id": {
        "eq": "2748861636"
      }
    },
    "expected_changes": {
      "tags": {
        "to": {
          "ne": null
        }
      }
    }
  },
  {
    "diff_type": "added",
    "entity": "box_hubs",
    "where": {
      "title": {
        "contains": "Q2 Financial Review"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_files",
    "where": {
      "name": {
        "eq": "audit_summary.txt"
      }
    },
    "expected_count": 1
  },
  {
    "diff_type": "added",
    "entity": "box_comments",
    "where": {
      "item_id": {
        "eq": "2748861636"
      },
      "message": {
        "contains": "Audit status"
      }
    },
    "expected_count": 1
  }
]
```

</details>
