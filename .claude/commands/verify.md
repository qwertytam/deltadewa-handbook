---
description: Run the two CI gates (pinned markdownlint + strict MkDocs build) and report only failures
argument-hint: "[optional: path to focus the report on]"
disable-model-invocation: false
---

Delegate to the `build-verifier` sub-agent. Ask it to run, in order:

```bash
npx --yes markdownlint-cli2@0.23.2
poetry run mkdocs build --strict
```

and return only failures in its table format, plus a PASS line if both are
clean. Do not run the commands in this context — the point is to keep the
build log out of the main thread.

$ARGUMENTS

If arguments were given, ask the agent to sort its table so failures under that
path come first, but still report everything — a link this branch broke may
surface in a file it never touched.

When the report comes back, fix the failures here in the main thread, then
re-run this command. Do not open a PR while either gate is red.
