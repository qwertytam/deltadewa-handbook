---
description: Cut a handbook version — check the release bar, tag it, and update the published set
argument-hint: "<major.minor.patch>, e.g. 0.2.0"
disable-model-invocation: false
---

Cut version `$ARGUMENTS`.

Stop and ask if no version was given, or if it is not `major.minor.patch`. Do
not invent the next number — which bump this is, is the maintainer's call, and
the rule for it is in the "Version numbers" section of `README.md`.

## 1. Confirm it is the right bump

Compare `main` against the previous tag and say which the changes are, before
touching anything:

```bash
git diff --stat <previous-tag>..main -- docs/ mkdocs.yml .github/cross-repo-anchors.txt
```

A **minor** is owed if a canonical number or band moved, a page was added,
moved or renamed, the `nav` restructured, or a line in
`.github/cross-repo-anchors.txt` changed. Otherwise it is a **patch**.

If the argument disagrees with what the diff shows, say so and stop. Tagging a
band change as a patch is how "cite `0.2` and it stays true" quietly stops
being true.

## 2. Check the release bar

All four must hold **on the commit being tagged**, not on the pull request
before it:

```bash
gh issue list --state open --label "priority: P1"
gh issue list --state open --label "internal-consistency"
gh run list --branch main --workflow=ci.yml --limit 1 \
  --json headSha,conclusion,jobs
```

The first two must be empty. The run must be a `success` **whose `headSha` is
the commit you are about to tag** — a green run on an earlier commit says
nothing about this one. Within it, confirm both `Lint Markdown` and `Build docs
(strict)` passed, and that the `Assert cross-repo anchors` step inside the
latter passed rather than being skipped.

Report which conditions hold and which do not. If any fails, stop — meeting the
bar is what the version is *for*.

## 3. Tag

An annotated tag, on `main`, recording the bar it met:

```bash
git checkout main && git pull
git tag -a <version> -F <message-file> <sha>
git push origin <version>
```

Never tag a commit that is not on `main`, and never move an existing tag: a
version someone has cited must keep meaning what it meant.

## 4. Update the published set

Branch, then edit `.github/versions.txt`:

- **Minor** — add a line `<major.minor>  <tag>  recency`. If that leaves more
  than five `recency` lines, remove the oldest. Never remove a `cited` line to
  make room; the published set is the union of both rules.
- **Patch** — update the `tag` field on the existing `major.minor` line. The
  directory republishes in place; no new directory appears.

Before retiring any line, check whether it is `cited`. Removing one means a
downstream repository loses a URL it links to — that citation comes out over
there **first**, in its own PR in that repo, exactly as the anchor contract
requires.

`ci.yml` validates the file on the pull request: format, that each tag exists,
that the tag matches its version, and that no two lines claim the same
directory.

## 5. Open the PR and stop

Body says which version, which bump and why, the bar conditions with the run
that proved them, and what was retired from the published set. Then report the
tag and the PR URL.

Do not merge it. The deploy runs on merge, and it is the first thing that
exercises the new version end to end.
