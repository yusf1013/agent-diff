# Testing our assistant

We are building an AI assistant that carries out requests for our team in Slack through its API: it works with
channels, messages, people and reactions. Before we deploy it, we want to test one thing: **does it act on exactly the record the user means?** A
request describes what the user has in mind. The assistant should act on exactly that, and when nothing in the
workspace fits the request, it should say so instead of acting.

Please write **12 test cases** for this, and save them as `tests.json` in this folder, in the format of `format.md`.

Make sure each test checks a different property. Make the tests challenging: a careless assistant should fail them,
but a perfect assistant must be able to pass them. Use neutral ids that do not reveal which record is the right one.

Each test runs on its own:
1. The records in the test's `seed` are created in an empty Slack workspace (`seed_ops.md`).
2. The assistant receives the test's `request` from Agent Bot, the bot account the assistant uses, the user it acts as.
3. It works through the Slack API. `api.md` is the documentation it gets.
4. Afterwards, the test's `assertions` are checked against how the workspace changed, and a reviewer reads the
   assistant's final reply against the test's `expected`.

Scope: only whether the assistant finds and acts on the right record or records. Security, prompt injection, speed
and writing style are out of scope.

Work on your own: make every decision yourself and do not ask questions. When `tests.json` is saved, reply with a
one-line summary of each test.
