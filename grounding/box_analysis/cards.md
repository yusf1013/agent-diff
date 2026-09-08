# Box obligation cards

Only agreed card fields appear inside each JSON block. Test/obligation headings are document navigation, not card fields. `Grounding obligations` is the total for the parent test, repeated on each of its cards; count cards once. See [tables and evidence](report.md).

<a id="box_116"></a>
## #60 — box_116

### Obligation 1

```json
{
  "Test ID": "box_116",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the current user profile",
  "Grounding obligation description": "Resolve the current user profile. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_users in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "27512847635"
  ],
  "Alternative sufficient identifying sets": [
    []
  ],
  "Change-computation attributes": [
    [
      "box_users.name"
    ]
  ],
  "Written attributes": [
    "box_folders.name"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_116",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

<a id="box_117"></a>
## #61 — box_117

### Obligation 1

```json
{
  "Test ID": "box_117",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve investments folder",
  "Grounding obligation description": "Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5610825569"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

<a id="box_118"></a>
## #62 — box_118

### Obligation 1

```json
{
  "Test ID": "box_118",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the FOMC document set",
  "Grounding obligation description": "Choose one of the four eligible FOMC files for the comment; do not require a particular retrieval order.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3379954793",
    "2667428831",
    "1246789615",
    "1439014490"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

<a id="box_119"></a>
## #63 — box_119

### Obligation 1

```json
{
  "Test ID": "box_119",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the Google earnings PDF",
  "Grounding obligation description": "Resolve the Google earnings PDF. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2748861636"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

<a id="box_120"></a>
## #64 — box_120

### Obligation 1

```json
{
  "Test ID": "box_120",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve macroeconomics folder",
  "Grounding obligation description": "Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1973339758"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.name"
  ]
}
```

<a id="box_121"></a>
## #65 — box_121

### Obligation 1

```json
{
  "Test ID": "box_121",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the April transport CSV",
  "Grounding obligation description": "Resolve the April transport CSV. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1421498350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_121",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve investments folder",
  "Grounding obligation description": "Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5610825569"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

<a id="box_122"></a>
## #66 — box_122

No grounding-obligation cards: see the test notes for new outputs and supplied context.

<a id="box_123"></a>
## #67 — box_123

### Obligation 1

```json
{
  "Test ID": "box_123",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve investments folder",
  "Grounding obligation description": "Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5610825569"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.tags"
  ]
}
```

<a id="box_124"></a>
## #68 — box_124

### Obligation 1

```json
{
  "Test ID": "box_124",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve investments folder",
  "Grounding obligation description": "Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5610825569"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.description"
  ]
}
```

<a id="box_125"></a>
## #69 — box_125

### Obligation 1

```json
{
  "Test ID": "box_125",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the history study notes about Argentina’s 2001 crisis",
  "Grounding obligation description": "Resolve the history study notes about Argentina’s 2001 crisis. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5696874158"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message",
    "box_tasks.item_id",
    "box_tasks.message"
  ]
}
```

<a id="box_126"></a>
## #70 — box_126

### Obligation 1

```json
{
  "Test ID": "box_126",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_126",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve interviewing tips FINAL.txt",
  "Grounding obligation description": "Resolve interviewing tips FINAL.txt. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1364279594"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

<a id="box_127"></a>
## #71 — box_127

### Obligation 1

```json
{
  "Test ID": "box_127",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve investments folder",
  "Grounding obligation description": "Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5610825569"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.description"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_127",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve files in the investments area for counting",
  "Grounding obligation description": "Resolve files in the investments area for counting. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1376125085",
    "2748861636",
    "2772059170",
    "7889164469",
    "1414825331",
    "1585447101",
    "1352749393",
    "2284320887",
    "3205344472",
    "3234744487",
    "2215195296",
    "2665143622",
    "1812751520",
    "1680035539",
    "1731377376",
    "2130264605",
    "1818721808",
    "2208613029",
    "3131211280",
    "3128241842",
    "1698478564",
    "2819267910",
    "1193919506",
    "2152227285",
    "3056642419",
    "2647359146",
    "5500857985",
    "1044921469",
    "2323418229",
    "3649010344",
    "1962119681",
    "1502930304",
    "1494147682",
    "1542940481",
    "2396992486",
    "1302660570",
    "2941895851",
    "1351294877",
    "2127882706",
    "9891894086",
    "8259080169",
    "1891960519",
    "1064362959",
    "4847599630",
    "1115105829",
    "1553809035",
    "1484641315",
    "3024573843",
    "7099094335",
    "1280559514",
    "2641266627",
    "6543141533",
    "2064689726",
    "2543780536",
    "8695847712",
    "1107398791",
    "3379954793",
    "2667428831",
    "1246789615",
    "1439014490",
    "1490177849",
    "1421498350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_folders.description"
  ]
}
```

<a id="box_128"></a>
## #72 — box_128

### Obligation 1

```json
{
  "Test ID": "box_128",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve accessible hubs for counting",
  "Grounding obligation description": "Resolve accessible hubs for counting. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_hubs in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "999999",
    "888888",
    "777777"
  ],
  "Alternative sufficient identifying sets": [
    []
  ],
  "Change-computation attributes": [
    [
      "box_hubs.id"
    ]
  ],
  "Written attributes": [
    "box_folders.name"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_128",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

<a id="box_129"></a>
## #73 — box_129

### Obligation 1

```json
{
  "Test ID": "box_129",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the FOMC document set",
  "Grounding obligation description": "Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3379954793",
    "2667428831",
    "1246789615",
    "1439014490"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_129",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

<a id="box_130"></a>
## #74 — box_130

### Obligation 1

```json
{
  "Test ID": "box_130",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve crisis text files containing 2001 outside history",
  "Grounding obligation description": "Resolve crisis text files containing 2001 outside history. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "9979104500"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.content",
      "box_files.parent_id",
      "box_folders.name",
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.parent_id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_130",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve history folder",
  "Grounding obligation description": "Resolve history folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1660804823"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

<a id="box_131"></a>
## #75 — box_131

### Obligation 1

```json
{
  "Test ID": "box_131",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve macroeconomics folder",
  "Grounding obligation description": "Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1973339758"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_hub_items.item_id"
  ]
}
```

<a id="box_132"></a>
## #76 — box_132

### Obligation 1

```json
{
  "Test ID": "box_132",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the misfiled root crisis copy",
  "Grounding obligation description": "Resolve the misfiled root crisis copy. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "9979104500"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.content",
      "box_files.parent_id"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.item_status"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_132",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the correctly filed history crisis notes",
  "Grounding obligation description": "Resolve the correctly filed history crisis notes. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5696874158"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content"
    ]
  ],
  "Written attributes": [
    "box_files.tags"
  ]
}
```

<a id="box_133"></a>
## #77 — box_133

### Obligation 1

```json
{
  "Test ID": "box_133",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve macroeconomics folder",
  "Grounding obligation description": "Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1973339758"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.name",
    "box_folders.description"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_133",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve December 2025 price-index CSV",
  "Grounding obligation description": "Resolve December 2025 price-index CSV. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1490177849"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content"
    ]
  ],
  "Written attributes": [
    "box_folders.name",
    "box_folders.description"
  ]
}
```

<a id="box_134"></a>
## #78 — box_134

### Obligation 1

```json
{
  "Test ID": "box_134",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve 2018-census-totals-by-topic-national-highlights-csv folder",
  "Grounding obligation description": "Resolve 2018-census-totals-by-topic-national-highlights-csv folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "9782984299"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.name"
  ]
}
```

<a id="box_135"></a>
## #79 — box_135

### Obligation 1

```json
{
  "Test ID": "box_135",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve macroeconomics folder",
  "Grounding obligation description": "Resolve macroeconomics folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1973339758"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_135",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve transport registrations source CSV",
  "Grounding obligation description": "Resolve transport registrations source CSV. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1421498350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content"
    ]
  ],
  "Written attributes": [
    "box_files.name",
    "box_files.content"
  ]
}
```

<a id="box_136"></a>
## #80 — box_136

### Obligation 1

```json
{
  "Test ID": "box_136",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve April 2025 transport CSV for line count",
  "Grounding obligation description": "Resolve April 2025 transport CSV for line count. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1421498350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content",
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

<a id="box_137"></a>
## #81 — box_137

### Obligation 1

```json
{
  "Test ID": "box_137",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the smallest investments file",
  "Grounding obligation description": "Resolve the smallest investments file. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1064362959"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.size",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.extension"
    ]
  ],
  "Written attributes": [
    "box_files.name"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_137",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the largest investments file",
  "Grounding obligation description": "Resolve the largest investments file. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1490177849"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.size",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.extension"
    ]
  ],
  "Written attributes": [
    "box_files.name"
  ]
}
```

<a id="box_138"></a>
## #82 — box_138

### Obligation 1

```json
{
  "Test ID": "box_138",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_138",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve investments folder",
  "Grounding obligation description": "Resolve investments folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5610825569"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

<a id="box_139"></a>
## #83 — box_139

### Obligation 1

```json
{
  "Test ID": "box_139",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve misspelled ethics and philosophy filenames",
  "Grounding obligation description": "Resolve misspelled ethics and philosophy filenames. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "6478815895",
    "2228856784",
    "1956298215",
    "8847291035",
    "9958302146"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.name"
    ]
  ],
  "Written attributes": [
    "box_files.name"
  ]
}
```

<a id="box_140"></a>
## #84 — box_140

### Obligation 1

```json
{
  "Test ID": "box_140",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the misfiled digital history reading",
  "Grounding obligation description": "Resolve the misfiled digital history reading. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2797160615"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_140",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve digital humanities folder",
  "Grounding obligation description": "Resolve digital humanities folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "7905906319"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

<a id="box_141"></a>
## #85 — box_141

### Obligation 1

```json
{
  "Test ID": "box_141",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve model-evaluation JSON files",
  "Grounding obligation description": "Resolve model-evaluation JSON files. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "8647156721",
    "2466872085",
    "2713928524",
    "4373646747",
    "3094163556",
    "2112512450",
    "1238342109",
    "2211626350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_hub_items.item_id"
  ]
}
```

<a id="box_142"></a>
## #86 — box_142

### Obligation 1

```json
{
  "Test ID": "box_142",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the misfiled cross-folder duplicate reading",
  "Grounding obligation description": "Resolve the misfiled cross-folder duplicate reading. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "8847291036"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.item_status"
  ]
}
```

<a id="box_143"></a>
## #87 — box_143

### Obligation 1

```json
{
  "Test ID": "box_143",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve readings folder",
  "Grounding obligation description": "Resolve readings folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2113564020"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_143",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve readings files for extension-based relocation",
  "Grounding obligation description": "Resolve readings files for extension-based relocation. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2204814480",
    "8930492081",
    "2503333498",
    "2460105954",
    "3266469077",
    "9979104400",
    "2228856784",
    "6478815895",
    "1956298215",
    "2576277563",
    "8847291035",
    "8847291036",
    "2219576536",
    "2488685816",
    "1723962562",
    "6322534720",
    "3166892170",
    "9086815882",
    "1822613980",
    "2358251230",
    "2408528068",
    "8268998082",
    "1898807902",
    "2107290365",
    "2350170522",
    "1678816614",
    "2166760427",
    "7827931276",
    "6154217723",
    "2322959540"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.extension"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_143",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve category folders empty after the requested moves",
  "Grounding obligation description": "Resolve category folders empty after the requested moves. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "7905906319"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.parent_id",
      "box_folders.id",
      "box_folders.name",
      "box_files.parent_id",
      "box_files.extension"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.item_status"
  ]
}
```

<a id="box_144"></a>
## #88 — box_144

### Obligation 1

```json
{
  "Test ID": "box_144",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the transport CSV for its size-conditioned rename",
  "Grounding obligation description": "Seed size 6063648 exceeds either common 1MB threshold, activating only the large_transport.csv branch.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1421498350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.size"
    ]
  ],
  "Written attributes": [
    "box_files.name"
  ]
}
```

<a id="box_145"></a>
## #89 — box_145

### Obligation 1

```json
{
  "Test ID": "box_145",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the misspelled computational Markdown reading",
  "Grounding obligation description": "Resolve the misspelled computational Markdown reading. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3266469077"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.name"
    ]
  ],
  "Written attributes": [
    "box_files.name"
  ]
}
```

<a id="box_146"></a>
## #90 — box_146

### Obligation 1

```json
{
  "Test ID": "box_146",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve history folder",
  "Grounding obligation description": "Resolve history folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1660804823"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

<a id="box_147"></a>
## #91 — box_147

### Obligation 1

```json
{
  "Test ID": "box_147",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

<a id="box_148"></a>
## #92 — box_148

### Obligation 1

```json
{
  "Test ID": "box_148",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve 2001 crisis notes for a new version",
  "Grounding obligation description": "Resolve the exact-named existing file. A1 fixes its identity and version change, but does not certify preservation of prior content or the appended line.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5696874158"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content"
    ]
  ],
  "Written attributes": [
    "box_files.content"
  ]
}
```

<a id="box_149"></a>
## #93 — box_149

### Obligation 1

```json
{
  "Test ID": "box_149",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the duplicate Dirty War Markdown notes",
  "Grounding obligation description": "Resolve the duplicate Dirty War Markdown notes. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3320893579"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.size",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.item_status"
  ]
}
```

<a id="box_150"></a>
## #94 — box_150

### Obligation 1

```json
{
  "Test ID": "box_150",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the FOMC document set",
  "Grounding obligation description": "Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3379954793",
    "2667428831",
    "1246789615",
    "1439014490"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_hub_items.item_id"
  ]
}
```

<a id="box_151"></a>
## #95 — box_151

### Obligation 1

```json
{
  "Test ID": "box_151",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve investments PDF files",
  "Grounding obligation description": "Resolve investments PDF files. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2748861636",
    "3379954793",
    "2667428831",
    "1246789615",
    "1439014490"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.tags"
  ]
}
```

<a id="box_152"></a>
## #96 — box_152

### Obligation 1

```json
{
  "Test ID": "box_152",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve the FOMC document set",
  "Grounding obligation description": "Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3379954793",
    "2667428831",
    "1246789615",
    "1439014490"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.name"
    ]
  ],
  "Written attributes": [
    "box_files.description"
  ]
}
```

<a id="box_153"></a>
## #97 — box_153

### Obligation 1

```json
{
  "Test ID": "box_153",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve comments on the Google 10-Q PDF",
  "Grounding obligation description": "Resolve comments on the Google 10-Q PDF. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_comments in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1640914640"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.id",
      "box_comments.item_id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_comments.id"
    ]
  ],
  "Written attributes": [
    "box_folders.name"
  ]
}
```

<a id="box_154"></a>
## #98 — box_154

### Obligation 1

```json
{
  "Test ID": "box_154",
  "Task type": "state-changing",
  "Grounding obligations": 1,
  "Grounding obligation name": "Resolve Argentina crisis notes as slogan source and comment target",
  "Grounding obligation description": "The seed text supplies Que se vayan todos and A1 fixes both file identity and that slogan fragment; this does not certify all surrounding prose.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "5696874158"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content",
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

<a id="box_155"></a>
## #99 — box_155

### Obligation 1

```json
{
  "Test ID": "box_155",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve macroeconomic time-series CSVs",
  "Grounding obligation description": "Resolve macroeconomic time-series CSVs. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1107398791",
    "1490177849",
    "1421498350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.extension",
      "box_files.content",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content",
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id",
    "box_files.tags",
    "box_folders.name",
    "box_files.content",
    "box_hub_items.item_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_155",
  "Task type": "state-changing",
  "Grounding obligations": 2,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

<a id="box_156"></a>
## #100 — box_156

### Obligation 1

```json
{
  "Test ID": "box_156",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve the cryptozoology sighting report",
  "Grounding obligation description": "The Pacific Northwest report is the asserted permissive sighting target. Its content includes photographic evidence and expedition Sasquatch Survey NW-7, activating verified tagging. Identity is checked; tag correctness and review text are not certified.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3302188295"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content",
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_files.tags",
    "box_files.parent_id",
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_156",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve the root destination",
  "Grounding obligation description": "Resolve the root destination. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "0"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_156",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve the obvious backup of the sighting report",
  "Grounding obligation description": "Resolve the obvious backup of the sighting report. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1891733744"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.item_status"
  ]
}
```

### Obligation 4

```json
{
  "Test ID": "box_156",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve cryptozoology_raw folder",
  "Grounding obligation description": "Resolve cryptozoology_raw folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "4313494130"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.name"
    ]
  ],
  "Written attributes": [
    "box_folders.name"
  ]
}
```

<a id="box_157"></a>
## #101 — box_157

### Obligation 1

```json
{
  "Test ID": "box_157",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve the existing seasonal tea-materials hub",
  "Grounding obligation description": "Resolve the existing seasonal tea-materials hub. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_hubs in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "888888"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_hubs.title"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_hubs.id"
    ]
  ],
  "Written attributes": [
    "box_hub_items.hub_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_157",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve the current winter preparation guide",
  "Grounding obligation description": "Resolve the current winter preparation guide. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3180616460"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_files.tags",
    "box_files.description",
    "box_comments.item_id",
    "box_comments.message",
    "box_hub_items.item_id"
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_157",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve the utensil inventory",
  "Grounding obligation description": "Resolve the utensil inventory. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3309661031"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

### Obligation 4

```json
{
  "Test ID": "box_157",
  "Task type": "state-changing",
  "Grounding obligations": 4,
  "Grounding obligation name": "Resolve the obsolete winter draft",
  "Grounding obligation description": "Resolve the obsolete winter draft. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1018029878"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.item_status"
  ]
}
```

<a id="box_158"></a>
## #102 — box_158

### Obligation 1

```json
{
  "Test ID": "box_158",
  "Task type": "read-only",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve Minimoog restoration documents for review",
  "Grounding obligation description": "Resolve Minimoog restoration documents for review. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1062973727",
    "3212140342",
    "2666248889"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Answer-computation attributes": [
    [
      "box_files.name",
      "box_files.content"
    ]
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_158",
  "Task type": "read-only",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve the Minimoog project folder",
  "Grounding obligation description": "Resolve the Minimoog project folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "9559162103"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Answer-computation attributes": [
    [
      "box_folders.name",
      "box_folders.description"
    ]
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_158",
  "Task type": "read-only",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve Favorites for the restoration-document check",
  "Grounding obligation description": "Resolve Favorites for the restoration-document check. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_collections in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "926489"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_collections.name"
    ]
  ],
  "Answer-computation attributes": [
    [
      "box_files.collections"
    ]
  ]
}
```

### Obligation 4

```json
{
  "Test ID": "box_158",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve the capacitor replacement log",
  "Grounding obligation description": "Resolve the capacitor replacement log. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1062973727"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

### Obligation 5

```json
{
  "Test ID": "box_158",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve the C31 verified comment",
  "Grounding obligation description": "Resolve the C31 verified comment. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_comments in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2656068403"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_comments.message",
      "box_comments.item_id",
      "box_files.name",
      "box_files.id"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_comments.message"
    ]
  ],
  "Written attributes": [
    "box_comments.message"
  ]
}
```

### Obligation 6

```json
{
  "Test ID": "box_158",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve the resonance calibration task",
  "Grounding obligation description": "Resolve the resonance calibration task. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_tasks in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1828124557"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_tasks.message",
      "box_tasks.item_id",
      "box_files.id",
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_tasks.is_completed"
  ]
}
```

### Obligation 7

```json
{
  "Test ID": "box_158",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve the cutoff tracking task",
  "Grounding obligation description": "Resolve the cutoff tracking task. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_tasks in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "8610023888"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_tasks.message",
      "box_tasks.item_id",
      "box_files.id",
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_tasks.message"
  ]
}
```

### Obligation 8

```json
{
  "Test ID": "box_158",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve oscillator schematic notes",
  "Grounding obligation description": "Resolve oscillator schematic notes. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2666248889"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.tags"
  ]
}
```

<a id="box_159"></a>
## #103 — box_159

### Obligation 1

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve current user for audit attribution",
  "Grounding obligation description": "Resolve current user for audit attribution. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_users in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "27512847635"
  ],
  "Alternative sufficient identifying sets": [
    []
  ],
  "Change-computation attributes": [
    [
      "box_users.login"
    ]
  ],
  "Written attributes": [
    "box_comments.message"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_159",
  "Task type": "read-only",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve the conservation folder for review",
  "Grounding obligation description": "Resolve the conservation folder for review. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3578701092"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Answer-computation attributes": [
    [
      "box_folders.name",
      "box_folders.description"
    ]
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve the Q3 2025 humidity log",
  "Grounding obligation description": "Resolve the Q3 2025 humidity log. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2679438618"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content"
    ]
  ],
  "Written attributes": [
    "box_comments.message",
    "box_files.content"
  ]
}
```

### Obligation 4

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve the Q4 2025 humidity log",
  "Grounding obligation description": "Resolve the Q4 2025 humidity log. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1747153578"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content"
    ]
  ],
  "Written attributes": [
    "box_comments.message",
    "box_files.content"
  ]
}
```

### Obligation 5

```json
{
  "Test ID": "box_159",
  "Task type": "read-only",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve Favorites for conservation-document review",
  "Grounding obligation description": "Resolve Favorites for conservation-document review. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_collections in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "926489"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_collections.name"
    ]
  ],
  "Answer-computation attributes": [
    [
      "box_files.collections"
    ]
  ]
}
```

### Obligation 6

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve the incunabula condition report",
  "Grounding obligation description": "Resolve the incunabula condition report. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1701916585"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

### Obligation 7

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve the Budget review pending comment",
  "Grounding obligation description": "Resolve the Budget review pending comment. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_comments in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "7404947855"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_comments.message"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_comments.message"
  ]
}
```

### Obligation 8

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve the outdated condition-report comment",
  "Grounding obligation description": "Resolve the outdated condition-report comment. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_comments in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2912801714"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_comments.message",
      "box_comments.item_id",
      "box_files.id",
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": []
}
```

### Obligation 9

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve annual summary for updating treatment totals",
  "Grounding obligation description": "Resolve annual summary for updating treatment totals. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1172138282"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content"
    ]
  ],
  "Written attributes": [
    "box_files.content"
  ]
}
```

### Obligation 10

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve Conservation Lab Archive",
  "Grounding obligation description": "Resolve Conservation Lab Archive. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_hubs in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "777777"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_hubs.title"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_hubs.description"
  ]
}
```

### Obligation 11

```json
{
  "Test ID": "box_159",
  "Task type": "state-changing",
  "Grounding obligations": 11,
  "Grounding obligation name": "Resolve deprecated_2024 folder",
  "Grounding obligation description": "Resolve deprecated_2024 folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "7983826892"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.item_status"
  ]
}
```

<a id="box_160"></a>
## #104 — box_160

### Obligation 1

```json
{
  "Test ID": "box_160",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve BA folder",
  "Grounding obligation description": "Resolve BA folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2228309175"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_folders.parent_id",
    "box_folders.name"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_160",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve Buenos Aires folder",
  "Grounding obligation description": "Resolve Buenos Aires folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1206853609"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_160",
  "Task type": "read-only",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve readings as the review source",
  "Grounding obligation description": "Resolve readings as the review source. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2113564020"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Answer-computation attributes": [
    [
      "box_folders.id",
      "box_files.name",
      "box_files.parent_id"
    ]
  ]
}
```

### Obligation 4

```json
{
  "Test ID": "box_160",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve the misfiled digital history methods reading",
  "Grounding obligation description": "Resolve the misfiled digital history methods reading. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2797160615"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 5

```json
{
  "Test ID": "box_160",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve digital humanities folder",
  "Grounding obligation description": "Resolve digital humanities folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "7905906319"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

### Obligation 6

```json
{
  "Test ID": "box_160",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve history folder",
  "Grounding obligation description": "Resolve history folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1660804823"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.parent_id"
  ]
}
```

### Obligation 7

```json
{
  "Test ID": "box_160",
  "Task type": "state-changing",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve obsolete tasks attached to duplicate-marked files",
  "Grounding obligation description": "Resolve obsolete tasks attached to duplicate-marked files. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_tasks in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3292462467",
    "1751119378",
    "1884936347",
    "1177785842"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_tasks.message",
      "box_tasks.item_id",
      "box_files.id",
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": []
}
```

### Obligation 8

```json
{
  "Test ID": "box_160",
  "Task type": "read-only",
  "Grounding obligations": 8,
  "Grounding obligation name": "Resolve existing hubs for review",
  "Grounding obligation description": "Resolve existing hubs for review. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_hubs in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "999999",
    "888888",
    "777777"
  ],
  "Alternative sufficient identifying sets": [
    []
  ],
  "Answer-computation attributes": [
    [
      "box_hubs.title",
      "box_hubs.description"
    ]
  ]
}
```

<a id="box_161"></a>
## #105 — box_161

### Obligation 1

```json
{
  "Test ID": "box_161",
  "Task type": "read-only",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve current user details",
  "Grounding obligation description": "Resolve current user details. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_users in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "27512847635"
  ],
  "Alternative sufficient identifying sets": [
    []
  ],
  "Answer-computation attributes": [
    [
      "box_users.name",
      "box_users.login"
    ]
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_161",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve Annual Summary 2025",
  "Grounding obligation description": "Resolve Annual Summary 2025. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1172138282"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.shared_link",
    "box_files.collections"
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_161",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve Favorites for the membership check and conditional addition",
  "Grounding obligation description": "Resolve Favorites for the membership check and conditional addition. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_collections in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "926489"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_collections.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_collections.id",
      "box_files.collections"
    ]
  ],
  "Written attributes": [
    "box_files.collections"
  ]
}
```

<a id="box_162"></a>
## #106 — box_162

### Obligation 1

```json
{
  "Test ID": "box_162",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve 2018-census-totals-by-topic-national-highlights-csv folder",
  "Grounding obligation description": "Resolve 2018-census-totals-by-topic-national-highlights-csv folder. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "9782984299"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_folders.name",
    "box_folders.parent_id",
    "box_files.parent_id"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_162",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve transport CSV for relocation and series comment",
  "Grounding obligation description": "A4 fixes the source/target file identity but the Transport series marker does not check its first-row reference. Full identity coverage does not certify that computation.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "1421498350"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.content",
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id",
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_162",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve an eligible population-named census file",
  "Grounding obligation description": "Choose one eligible population-named file if present. The concrete filename condition has no match in the census folder, so this is absent, not underspecified.",
  "Resolution": "absent",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    []
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

<a id="box_163"></a>
## #107 — box_163

### Obligation 1

```json
{
  "Test ID": "box_163",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve Google earnings PDF for size-based audit",
  "Grounding obligation description": "A1 and A4 fix the file identity. They do not check the correct size-derived tag, size text, or manifest content.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "2748861636"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.size",
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_files.tags",
    "box_files.content",
    "box_comments.item_id",
    "box_comments.message"
  ]
}
```

### Obligation 2

```json
{
  "Test ID": "box_163",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve the FOMC document set",
  "Grounding obligation description": "Resolve the FOMC document set. The selected reference is supported by the supplied seed and the stated selection rule.",
  "Resolution": "resolved",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_files in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [
    "3379954793",
    "2667428831",
    "1246789615",
    "1439014490"
  ],
  "Alternative sufficient identifying sets": [
    [
      "box_files.name",
      "box_files.extension",
      "box_files.parent_id",
      "box_folders.id",
      "box_folders.parent_id",
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_files.id"
    ]
  ],
  "Written attributes": [
    "box_hub_items.item_id"
  ]
}
```

### Obligation 3

```json
{
  "Test ID": "box_163",
  "Task type": "state-changing",
  "Grounding obligations": 3,
  "Grounding obligation name": "Resolve Analysis_2026 folder",
  "Grounding obligation description": "Resolve Analysis_2026 folder. The described subject has no seeded match.",
  "Resolution": "absent",
  "Shared scope": "The supplied Box account of acting user 27512847635; box_folders in box_default. Named subfolders are selection criteria, not hidden scope.",
  "Referent set": [],
  "Alternative sufficient identifying sets": [
    [
      "box_folders.name"
    ]
  ],
  "Change-computation attributes": [
    [
      "box_folders.id"
    ]
  ],
  "Written attributes": [
    "box_files.parent_id"
  ]
}
```

