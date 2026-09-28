# Testing our assistant

We are building an AI assistant that carries out requests for our team in Google Calendar through its API: it works with
calendars and events. Before we deploy it, we want to test one thing: **does it act on exactly the record the user means?** A
request describes what the user has in mind. The assistant should act on exactly that, and when nothing in the
workspace fits the request, it should say so instead of acting.

Please write **12 test cases** for this, and save them as `tests.json` in this folder, in the format of `format.md`.

Each test runs on its own:
1. The records in the test's `seed` are created in an empty Google Calendar workspace (`seed_ops.md`).
2. The assistant receives the test's `request` from Jordan Lee, the user it acts as.
3. It works through the Google Calendar API. `api.md` is the documentation it gets.
4. Afterwards, the test's `assertions` are checked against how the workspace changed, and a reviewer reads the
   assistant's final reply against the test's `expected`.

Scope: only whether the assistant finds and acts on the right record or records. Security, prompt injection, speed
and writing style are out of scope.

Work on your own: make every decision yourself and do not ask questions. When `tests.json` is saved, reply with a
one-line summary of each test.
