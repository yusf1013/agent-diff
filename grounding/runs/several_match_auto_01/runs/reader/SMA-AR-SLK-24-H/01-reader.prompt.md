You check test cases for an AI assistant that acts in a workspace on a user's behalf. You read carefully
and literally, the way the user who wrote the request would mean it.

---

A user sent the assistant this request in their Slack workspace:

    "React with the eyes emoji on every message in #incidents about the payment gateway timeout that was posted by someone who's a member of #payments-oncall."

The user is Agent Bot. Below is every Slack message in the workspace, with what the assistant can see about it. Which of
them does the user's request ask the assistant to act on?

List the id of every record the request covers, and only those. Read each condition of the request as the user
would mean it. If you cannot tell whether the user means a record, list it under `unsure` with the reason (and do
not list it in `ids`). Answer with JSON: {"ids": [...], "unsure": [{"id", "why"}], "notes": "..."}.

Records:
[
 {
  "id": "1790258400.000001",
  "message_id": "1790258400.000001",
  "channel_id": "C_INC",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Seeing 504s tied to a payment gateway timeout on checkout after the last deploy.",
  "ts": "1790258400.000001",
  "created_at": "2026-09-24T14:00:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T14:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T07:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY",
      "channel_name": "payments-oncall",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790258700.000002",
  "message_id": "1790258700.000002",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Getting the same payment gateway timeout error on the mobile checkout flow.",
  "ts": "1790258700.000002",
  "created_at": "2026-09-24T14:05:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T14:05:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T07:05:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790259000.000003",
  "message_id": "1790259000.000003",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "We're also seeing payment gateway timeout spikes in the EU region.",
  "ts": "1790259000.000003",
  "created_at": "2026-09-24T14:10:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T14:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T07:10:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790259300.000004",
  "message_id": "1790259300.000004",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Another payment gateway timeout, this time hitting the refunds endpoint.",
  "ts": "1790259300.000004",
  "created_at": "2026-09-24T14:15:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T14:15:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T07:15:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790259600.000005",
  "message_id": "1790259600.000005",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "FYI, seeing intermittent payment gateway timeout warnings in staging.",
  "ts": "1790259600.000005",
  "created_at": "2026-09-24T14:20:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T14:20:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T07:20:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790240400.000006",
  "message_id": "1790240400.000006",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Standup notes: sprint review moved to Thursday.",
  "ts": "1790240400.000006",
  "created_at": "2026-09-24T09:00:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790240700.000007",
  "message_id": "1790240700.000007",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "On-call handoff notes are posted in the wiki.",
  "ts": "1790240700.000007",
  "created_at": "2026-09-24T09:05:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:05:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:05:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1789898400.000008",
  "message_id": "1789898400.000008",
  "channel_id": "C_PAY",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Handing off on-call to Aisha this week.",
  "ts": "1789898400.000008",
  "created_at": "2026-09-20T10:00:00Z",
  "channel": "payments-oncall",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-20T10:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-20T03:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_PAY",
    "channel_name": "payments-oncall",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790157600.000009",
  "message_id": "1790157600.000009",
  "channel_id": "C_PAY",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Bumping this - anyone around to check the alert queue?",
  "ts": "1790157600.000009",
  "created_at": "2026-09-23T10:00:00Z",
  "channel": "payments-oncall",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-23T10:00:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-23T03:00:00-07:00",
  "channels": [
   {
    "channel_id": "C_PAY",
    "channel_name": "payments-oncall",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY",
      "channel_name": "payments-oncall",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790258460.000701",
  "message_id": "1790258460.000701",
  "channel_id": "C_INC",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Seeing 500s tied to a payment gateway timeout on checkout after today's push.",
  "ts": "1790258460.000701",
  "created_at": "2026-09-24T14:01:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T14:01:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T07:01:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY",
      "channel_name": "payments-oncall",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790233800.000702",
  "message_id": "1790233800.000702",
  "channel_id": "C_INC",
  "user_id": "U_AISHA (Aisha Khan)",
  "message_text": "Seeing 500s tied to a payment gateway timeout on checkout after today's push.",
  "ts": "1790233800.000702",
  "created_at": "2026-09-24T07:10:00Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:10:00+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:10:00-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY",
    "user_id": "U_AISHA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY",
      "channel_name": "payments-oncall",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790234019.000703",
  "message_id": "1790234019.000703",
  "ts": "1790234019.000703",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 1 passed.",
  "created_at": "2026-09-24T07:13:39Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:13:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:13:39-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790234239.000704",
  "message_id": "1790234239.000704",
  "ts": "1790234239.000704",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 2 passed.",
  "created_at": "2026-09-24T07:17:19Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:17:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:17:19-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790234458.000705",
  "message_id": "1790234458.000705",
  "ts": "1790234458.000705",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 3 passed.",
  "created_at": "2026-09-24T07:20:58Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:20:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:20:58-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790234678.000706",
  "message_id": "1790234678.000706",
  "ts": "1790234678.000706",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 4 passed.",
  "created_at": "2026-09-24T07:24:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:24:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:24:38-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790234898.000707",
  "message_id": "1790234898.000707",
  "ts": "1790234898.000707",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 5 passed.",
  "created_at": "2026-09-24T07:28:18Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:28:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:28:18-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790235117.000708",
  "message_id": "1790235117.000708",
  "ts": "1790235117.000708",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 6 passed.",
  "created_at": "2026-09-24T07:31:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:31:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:31:57-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790235337.000709",
  "message_id": "1790235337.000709",
  "ts": "1790235337.000709",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 7 passed.",
  "created_at": "2026-09-24T07:35:37Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:35:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:35:37-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790235557.000710",
  "message_id": "1790235557.000710",
  "ts": "1790235557.000710",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 8 passed.",
  "created_at": "2026-09-24T07:39:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:39:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:39:17-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790235776.000711",
  "message_id": "1790235776.000711",
  "ts": "1790235776.000711",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 9 passed.",
  "created_at": "2026-09-24T07:42:56Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:42:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:42:56-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790235996.000712",
  "message_id": "1790235996.000712",
  "ts": "1790235996.000712",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 10 passed.",
  "created_at": "2026-09-24T07:46:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:46:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:46:36-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790236216.000713",
  "message_id": "1790236216.000713",
  "ts": "1790236216.000713",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 11 passed.",
  "created_at": "2026-09-24T07:50:16Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:50:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:50:16-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790236435.000714",
  "message_id": "1790236435.000714",
  "ts": "1790236435.000714",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 12 passed.",
  "created_at": "2026-09-24T07:53:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:53:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:53:55-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790236655.000715",
  "message_id": "1790236655.000715",
  "ts": "1790236655.000715",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 13 passed.",
  "created_at": "2026-09-24T07:57:35Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T07:57:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T00:57:35-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790236874.000716",
  "message_id": "1790236874.000716",
  "ts": "1790236874.000716",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 14 passed.",
  "created_at": "2026-09-24T08:01:14Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:01:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:01:14-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790237094.000717",
  "message_id": "1790237094.000717",
  "ts": "1790237094.000717",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 15 passed.",
  "created_at": "2026-09-24T08:04:54Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:04:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:04:54-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790237314.000718",
  "message_id": "1790237314.000718",
  "ts": "1790237314.000718",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 16 passed.",
  "created_at": "2026-09-24T08:08:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:08:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:08:34-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790237533.000719",
  "message_id": "1790237533.000719",
  "ts": "1790237533.000719",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 17 passed.",
  "created_at": "2026-09-24T08:12:13Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:12:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:12:13-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790237753.000720",
  "message_id": "1790237753.000720",
  "ts": "1790237753.000720",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 18 passed.",
  "created_at": "2026-09-24T08:15:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:15:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:15:53-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790237973.000721",
  "message_id": "1790237973.000721",
  "ts": "1790237973.000721",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 19 passed.",
  "created_at": "2026-09-24T08:19:33Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:19:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:19:33-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790238192.000722",
  "message_id": "1790238192.000722",
  "ts": "1790238192.000722",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 20 passed.",
  "created_at": "2026-09-24T08:23:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:23:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:23:12-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790238412.000723",
  "message_id": "1790238412.000723",
  "ts": "1790238412.000723",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 21 passed.",
  "created_at": "2026-09-24T08:26:52Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:26:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:26:52-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790238632.000724",
  "message_id": "1790238632.000724",
  "ts": "1790238632.000724",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 22 passed.",
  "created_at": "2026-09-24T08:30:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:30:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:30:32-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790238851.000725",
  "message_id": "1790238851.000725",
  "ts": "1790238851.000725",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 23 passed.",
  "created_at": "2026-09-24T08:34:11Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:34:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:34:11-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790239071.000726",
  "message_id": "1790239071.000726",
  "ts": "1790239071.000726",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 24 passed.",
  "created_at": "2026-09-24T08:37:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:37:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:37:51-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790239291.000727",
  "message_id": "1790239291.000727",
  "ts": "1790239291.000727",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 25 passed.",
  "created_at": "2026-09-24T08:41:31Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:41:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:41:31-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790239510.000728",
  "message_id": "1790239510.000728",
  "ts": "1790239510.000728",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 26 passed.",
  "created_at": "2026-09-24T08:45:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:45:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:45:10-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790239730.000729",
  "message_id": "1790239730.000729",
  "ts": "1790239730.000729",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 27 passed.",
  "created_at": "2026-09-24T08:48:50Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:48:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:48:50-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790239949.000730",
  "message_id": "1790239949.000730",
  "ts": "1790239949.000730",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 28 passed.",
  "created_at": "2026-09-24T08:52:29Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:52:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:52:29-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790240169.000731",
  "message_id": "1790240169.000731",
  "ts": "1790240169.000731",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 29 passed.",
  "created_at": "2026-09-24T08:56:09Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:56:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:56:09-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790240389.000732",
  "message_id": "1790240389.000732",
  "ts": "1790240389.000732",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 30 passed.",
  "created_at": "2026-09-24T08:59:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T08:59:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T01:59:49-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790240608.000733",
  "message_id": "1790240608.000733",
  "ts": "1790240608.000733",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 31 passed.",
  "created_at": "2026-09-24T09:03:28Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:03:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:03:28-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790240828.000734",
  "message_id": "1790240828.000734",
  "ts": "1790240828.000734",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 32 passed.",
  "created_at": "2026-09-24T09:07:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:07:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:07:08-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790241048.000735",
  "message_id": "1790241048.000735",
  "ts": "1790241048.000735",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 33 passed.",
  "created_at": "2026-09-24T09:10:48Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:10:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:10:48-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790241267.000736",
  "message_id": "1790241267.000736",
  "ts": "1790241267.000736",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 34 passed.",
  "created_at": "2026-09-24T09:14:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:14:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:14:27-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790241487.000737",
  "message_id": "1790241487.000737",
  "ts": "1790241487.000737",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 35 passed.",
  "created_at": "2026-09-24T09:18:07Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:18:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:18:07-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790241707.000738",
  "message_id": "1790241707.000738",
  "ts": "1790241707.000738",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 36 passed.",
  "created_at": "2026-09-24T09:21:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:21:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:21:47-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790241926.000739",
  "message_id": "1790241926.000739",
  "ts": "1790241926.000739",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 37 passed.",
  "created_at": "2026-09-24T09:25:26Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:25:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:25:26-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790242146.000740",
  "message_id": "1790242146.000740",
  "ts": "1790242146.000740",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 38 passed.",
  "created_at": "2026-09-24T09:29:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:29:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:29:06-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790242366.000741",
  "message_id": "1790242366.000741",
  "ts": "1790242366.000741",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 39 passed.",
  "created_at": "2026-09-24T09:32:46Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:32:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:32:46-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790242585.000742",
  "message_id": "1790242585.000742",
  "ts": "1790242585.000742",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 40 passed.",
  "created_at": "2026-09-24T09:36:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:36:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:36:25-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790242805.000743",
  "message_id": "1790242805.000743",
  "ts": "1790242805.000743",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 41 passed.",
  "created_at": "2026-09-24T09:40:05Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:40:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:40:05-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790243024.000744",
  "message_id": "1790243024.000744",
  "ts": "1790243024.000744",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 42 passed.",
  "created_at": "2026-09-24T09:43:44Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:43:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:43:44-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790243244.000745",
  "message_id": "1790243244.000745",
  "ts": "1790243244.000745",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 43 passed.",
  "created_at": "2026-09-24T09:47:24Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:47:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:47:24-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790243464.000746",
  "message_id": "1790243464.000746",
  "ts": "1790243464.000746",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 44 passed.",
  "created_at": "2026-09-24T09:51:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:51:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:51:04-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790243683.000747",
  "message_id": "1790243683.000747",
  "ts": "1790243683.000747",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 45 passed.",
  "created_at": "2026-09-24T09:54:43Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:54:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:54:43-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790243903.000748",
  "message_id": "1790243903.000748",
  "ts": "1790243903.000748",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 46 passed.",
  "created_at": "2026-09-24T09:58:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T09:58:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T02:58:23-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790244123.000749",
  "message_id": "1790244123.000749",
  "ts": "1790244123.000749",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 47 passed.",
  "created_at": "2026-09-24T10:02:03Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:02:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:02:03-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790244342.000750",
  "message_id": "1790244342.000750",
  "ts": "1790244342.000750",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 48 passed.",
  "created_at": "2026-09-24T10:05:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:05:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:05:42-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790244562.000751",
  "message_id": "1790244562.000751",
  "ts": "1790244562.000751",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 49 passed.",
  "created_at": "2026-09-24T10:09:22Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:09:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:09:22-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790244782.000752",
  "message_id": "1790244782.000752",
  "ts": "1790244782.000752",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 50 passed.",
  "created_at": "2026-09-24T10:13:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:13:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:13:02-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790245001.000753",
  "message_id": "1790245001.000753",
  "ts": "1790245001.000753",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 51 passed.",
  "created_at": "2026-09-24T10:16:41Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:16:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:16:41-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790245221.000754",
  "message_id": "1790245221.000754",
  "ts": "1790245221.000754",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 52 passed.",
  "created_at": "2026-09-24T10:20:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:20:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:20:21-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790245441.000755",
  "message_id": "1790245441.000755",
  "ts": "1790245441.000755",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 53 passed.",
  "created_at": "2026-09-24T10:24:01Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:24:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:24:01-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790245660.000756",
  "message_id": "1790245660.000756",
  "ts": "1790245660.000756",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 54 passed.",
  "created_at": "2026-09-24T10:27:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:27:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:27:40-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790245880.000757",
  "message_id": "1790245880.000757",
  "ts": "1790245880.000757",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 55 passed.",
  "created_at": "2026-09-24T10:31:20Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:31:20+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:31:20-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790246099.000758",
  "message_id": "1790246099.000758",
  "ts": "1790246099.000758",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 56 passed.",
  "created_at": "2026-09-24T10:34:59Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:34:59+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:34:59-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790246319.000759",
  "message_id": "1790246319.000759",
  "ts": "1790246319.000759",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 57 passed.",
  "created_at": "2026-09-24T10:38:39Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:38:39+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:38:39-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790246539.000760",
  "message_id": "1790246539.000760",
  "ts": "1790246539.000760",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 58 passed.",
  "created_at": "2026-09-24T10:42:19Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:42:19+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:42:19-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790246758.000761",
  "message_id": "1790246758.000761",
  "ts": "1790246758.000761",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 59 passed.",
  "created_at": "2026-09-24T10:45:58Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:45:58+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:45:58-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790246978.000762",
  "message_id": "1790246978.000762",
  "ts": "1790246978.000762",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 60 passed.",
  "created_at": "2026-09-24T10:49:38Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:49:38+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:49:38-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790247198.000763",
  "message_id": "1790247198.000763",
  "ts": "1790247198.000763",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 61 passed.",
  "created_at": "2026-09-24T10:53:18Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:53:18+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:53:18-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790247417.000764",
  "message_id": "1790247417.000764",
  "ts": "1790247417.000764",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 62 passed.",
  "created_at": "2026-09-24T10:56:57Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T10:56:57+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T03:56:57-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790247637.000765",
  "message_id": "1790247637.000765",
  "ts": "1790247637.000765",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 63 passed.",
  "created_at": "2026-09-24T11:00:37Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:00:37+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:00:37-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790247857.000766",
  "message_id": "1790247857.000766",
  "ts": "1790247857.000766",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 64 passed.",
  "created_at": "2026-09-24T11:04:17Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:04:17+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:04:17-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790248076.000767",
  "message_id": "1790248076.000767",
  "ts": "1790248076.000767",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 65 passed.",
  "created_at": "2026-09-24T11:07:56Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:07:56+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:07:56-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790248296.000768",
  "message_id": "1790248296.000768",
  "ts": "1790248296.000768",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 66 passed.",
  "created_at": "2026-09-24T11:11:36Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:11:36+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:11:36-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790248516.000769",
  "message_id": "1790248516.000769",
  "ts": "1790248516.000769",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 67 passed.",
  "created_at": "2026-09-24T11:15:16Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:15:16+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:15:16-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790248735.000770",
  "message_id": "1790248735.000770",
  "ts": "1790248735.000770",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 68 passed.",
  "created_at": "2026-09-24T11:18:55Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:18:55+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:18:55-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790248955.000771",
  "message_id": "1790248955.000771",
  "ts": "1790248955.000771",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 69 passed.",
  "created_at": "2026-09-24T11:22:35Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:22:35+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:22:35-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790249174.000772",
  "message_id": "1790249174.000772",
  "ts": "1790249174.000772",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 70 passed.",
  "created_at": "2026-09-24T11:26:14Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:26:14+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:26:14-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790249394.000773",
  "message_id": "1790249394.000773",
  "ts": "1790249394.000773",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 71 passed.",
  "created_at": "2026-09-24T11:29:54Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:29:54+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:29:54-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790249614.000774",
  "message_id": "1790249614.000774",
  "ts": "1790249614.000774",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 72 passed.",
  "created_at": "2026-09-24T11:33:34Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:33:34+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:33:34-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790249833.000775",
  "message_id": "1790249833.000775",
  "ts": "1790249833.000775",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 73 passed.",
  "created_at": "2026-09-24T11:37:13Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:37:13+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:37:13-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790250053.000776",
  "message_id": "1790250053.000776",
  "ts": "1790250053.000776",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 74 passed.",
  "created_at": "2026-09-24T11:40:53Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:40:53+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:40:53-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790250273.000777",
  "message_id": "1790250273.000777",
  "ts": "1790250273.000777",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 75 passed.",
  "created_at": "2026-09-24T11:44:33Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:44:33+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:44:33-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790250492.000778",
  "message_id": "1790250492.000778",
  "ts": "1790250492.000778",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 76 passed.",
  "created_at": "2026-09-24T11:48:12Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:48:12+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:48:12-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790250712.000779",
  "message_id": "1790250712.000779",
  "ts": "1790250712.000779",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 77 passed.",
  "created_at": "2026-09-24T11:51:52Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:51:52+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:51:52-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790250932.000780",
  "message_id": "1790250932.000780",
  "ts": "1790250932.000780",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 78 passed.",
  "created_at": "2026-09-24T11:55:32Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:55:32+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:55:32-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790251151.000781",
  "message_id": "1790251151.000781",
  "ts": "1790251151.000781",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 79 passed.",
  "created_at": "2026-09-24T11:59:11Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T11:59:11+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T04:59:11-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790251371.000782",
  "message_id": "1790251371.000782",
  "ts": "1790251371.000782",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 80 passed.",
  "created_at": "2026-09-24T12:02:51Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:02:51+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:02:51-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790251591.000783",
  "message_id": "1790251591.000783",
  "ts": "1790251591.000783",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 81 passed.",
  "created_at": "2026-09-24T12:06:31Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:06:31+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:06:31-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790251810.000784",
  "message_id": "1790251810.000784",
  "ts": "1790251810.000784",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 82 passed.",
  "created_at": "2026-09-24T12:10:10Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:10:10+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:10:10-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790252030.000785",
  "message_id": "1790252030.000785",
  "ts": "1790252030.000785",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 83 passed.",
  "created_at": "2026-09-24T12:13:50Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:13:50+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:13:50-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790252249.000786",
  "message_id": "1790252249.000786",
  "ts": "1790252249.000786",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 84 passed.",
  "created_at": "2026-09-24T12:17:29Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:17:29+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:17:29-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790252469.000787",
  "message_id": "1790252469.000787",
  "ts": "1790252469.000787",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 85 passed.",
  "created_at": "2026-09-24T12:21:09Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:21:09+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:21:09-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790252689.000788",
  "message_id": "1790252689.000788",
  "ts": "1790252689.000788",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 86 passed.",
  "created_at": "2026-09-24T12:24:49Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:24:49+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:24:49-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790252908.000789",
  "message_id": "1790252908.000789",
  "ts": "1790252908.000789",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 87 passed.",
  "created_at": "2026-09-24T12:28:28Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:28:28+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:28:28-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790253128.000790",
  "message_id": "1790253128.000790",
  "ts": "1790253128.000790",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 88 passed.",
  "created_at": "2026-09-24T12:32:08Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:32:08+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:32:08-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790253348.000791",
  "message_id": "1790253348.000791",
  "ts": "1790253348.000791",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 89 passed.",
  "created_at": "2026-09-24T12:35:48Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:35:48+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:35:48-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790253567.000792",
  "message_id": "1790253567.000792",
  "ts": "1790253567.000792",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 90 passed.",
  "created_at": "2026-09-24T12:39:27Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:39:27+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:39:27-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790253787.000793",
  "message_id": "1790253787.000793",
  "ts": "1790253787.000793",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 91 passed.",
  "created_at": "2026-09-24T12:43:07Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:43:07+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:43:07-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790254007.000794",
  "message_id": "1790254007.000794",
  "ts": "1790254007.000794",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 92 passed.",
  "created_at": "2026-09-24T12:46:47Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:46:47+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:46:47-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790254226.000795",
  "message_id": "1790254226.000795",
  "ts": "1790254226.000795",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 93 passed.",
  "created_at": "2026-09-24T12:50:26Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:50:26+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:50:26-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790254446.000796",
  "message_id": "1790254446.000796",
  "ts": "1790254446.000796",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 94 passed.",
  "created_at": "2026-09-24T12:54:06Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:54:06+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:54:06-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790254666.000797",
  "message_id": "1790254666.000797",
  "ts": "1790254666.000797",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 95 passed.",
  "created_at": "2026-09-24T12:57:46Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T12:57:46+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T05:57:46-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790254885.000798",
  "message_id": "1790254885.000798",
  "ts": "1790254885.000798",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 96 passed.",
  "created_at": "2026-09-24T13:01:25Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:01:25+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:01:25-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790255105.000799",
  "message_id": "1790255105.000799",
  "ts": "1790255105.000799",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 97 passed.",
  "created_at": "2026-09-24T13:05:05Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:05:05+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:05:05-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790255324.000800",
  "message_id": "1790255324.000800",
  "ts": "1790255324.000800",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 98 passed.",
  "created_at": "2026-09-24T13:08:44Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:08:44+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:08:44-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790255544.000801",
  "message_id": "1790255544.000801",
  "ts": "1790255544.000801",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 99 passed.",
  "created_at": "2026-09-24T13:12:24Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:12:24+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:12:24-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790255764.000802",
  "message_id": "1790255764.000802",
  "ts": "1790255764.000802",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 100 passed.",
  "created_at": "2026-09-24T13:16:04Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:16:04+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:16:04-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790255983.000803",
  "message_id": "1790255983.000803",
  "ts": "1790255983.000803",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 101 passed.",
  "created_at": "2026-09-24T13:19:43Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:19:43+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:19:43-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790256203.000804",
  "message_id": "1790256203.000804",
  "ts": "1790256203.000804",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 102 passed.",
  "created_at": "2026-09-24T13:23:23Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:23:23+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:23:23-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790256423.000805",
  "message_id": "1790256423.000805",
  "ts": "1790256423.000805",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 103 passed.",
  "created_at": "2026-09-24T13:27:03Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:27:03+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:27:03-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790256642.000806",
  "message_id": "1790256642.000806",
  "ts": "1790256642.000806",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 104 passed.",
  "created_at": "2026-09-24T13:30:42Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:30:42+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:30:42-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790256862.000807",
  "message_id": "1790256862.000807",
  "ts": "1790256862.000807",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 105 passed.",
  "created_at": "2026-09-24T13:34:22Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:34:22+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:34:22-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790257082.000808",
  "message_id": "1790257082.000808",
  "ts": "1790257082.000808",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 106 passed.",
  "created_at": "2026-09-24T13:38:02Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:38:02+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:38:02-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790257301.000809",
  "message_id": "1790257301.000809",
  "ts": "1790257301.000809",
  "channel_id": "C_INC",
  "user_id": "U_OMAR (Omar Haddad)",
  "message_text": "Payment gateway timeout check 107 passed.",
  "created_at": "2026-09-24T13:41:41Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:41:41+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:41:41-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   },
   {
    "channel_id": "C_PAY_EU",
    "user_id": "U_OMAR",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_PAY_EU",
      "channel_name": "payments-oncall-eu",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790257521.000810",
  "message_id": "1790257521.000810",
  "ts": "1790257521.000810",
  "channel_id": "C_INC",
  "user_id": "U_MAYA (Maya Chen)",
  "message_text": "Payment gateway timeout check 108 passed.",
  "created_at": "2026-09-24T13:45:21Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:45:21+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:45:21-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_MAYA",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790257741.000811",
  "message_id": "1790257741.000811",
  "ts": "1790257741.000811",
  "channel_id": "C_INC",
  "user_id": "U_DIEGO (Diego Alvarez)",
  "message_text": "Payment gateway timeout check 109 passed.",
  "created_at": "2026-09-24T13:49:01Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:49:01+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:49:01-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_DIEGO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 },
 {
  "id": "1790257960.000812",
  "message_id": "1790257960.000812",
  "ts": "1790257960.000812",
  "channel_id": "C_INC",
  "user_id": "U_LEO (Leo Park)",
  "message_text": "Payment gateway timeout check 110 passed.",
  "created_at": "2026-09-24T13:52:40Z",
  "channel": "incidents",
  "private": false,
  "archived": false,
  "direct message": false,
  "posted (UTC)": "2026-09-24T13:52:40+00:00",
  "posted (user's time zone, Los Angeles)": "2026-09-24T06:52:40-07:00",
  "channels": [
   {
    "channel_id": "C_INC",
    "channel_name": "incidents",
    "is_private": false,
    "is_dm": false,
    "is_gc": false,
    "created_at": "2026-01-05T09:00:00Z",
    "is_archived": false
   }
  ],
  "channel_members": [
   {
    "channel_id": "C_INC",
    "user_id": "U_LEO",
    "joined_at": "2026-01-05T09:05:00Z",
    "channels": [
     {
      "channel_id": "C_INC",
      "channel_name": "incidents",
      "is_private": false,
      "is_dm": false,
      "is_gc": false,
      "created_at": "2026-01-05T09:00:00Z",
      "is_archived": false
     }
    ]
   }
  ]
 }
]
