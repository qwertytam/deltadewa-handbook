---
description: Work a handbook issue end to end — read it, audit the evidence, plan, edit, verify, PR
argument-hint: "[issue number] [more issue numbers for the same batch]"
disable-model-invocation: true
---

Work these issues as one themed batch: $ARGUMENTS

Follow this loop. Do not skip the plan-and-stop step.

## 1. Read

`gh issue view <n>` for each number given. Extract each issue's acceptance
criteria verbatim into a checklist. Note its label set — `accuracy`,
`internal-consistency`, `gap` and `repo-migration` imply different work:

- **accuracy** — a fact is wrong or imprecise; needs `source-verifier`.
- **internal-consistency** — the handbook disagrees with itself; needs
  `docs-auditor` and a canonical decision.
- **gap** — content that does not exist yet; needs drafting to house style.
- **repo-migration** — has a deltadewa-side half; needs `cross-repo-scout`,
  and its changes go in a separate PR in that repo.

## 2. Gather

Dispatch the sub-agents the labels imply, in parallel where independent.
Do not read whole Parts yourself to answer a narrow question.

## 3. Plan and stop

Present, in under 30 lines:

- the file-by-file change list;
- every judgement call, each as a question with options and a recommendation
  (which number is canonical, which framing wins, what to soften vs source);
- **what you propose to carve out** — anything program-specific that the issue
  seems to ask for but the handbook must not contain (see the scope boundary
  in `CLAUDE.md`), with the general version you would write instead.

Then **stop and wait for answers**. Editing before this is answered is the
main way this workflow wastes a session.

## 4. Edit

Branch first: `git checkout -b docs/<short-theme>`. Apply the changes,
following `.claude/skills/handbook-style/SKILL.md`. Keep each issue's changes
in its own commit so a single issue can be reverted.

Respect canon: a number changed on a non-canonical page is either removed in
favour of a link to its owner, or the owner changes too.

## 5. Verify

Run `/verify`. Both gates must be clean. Then re-read the acceptance criteria
and tick each box explicitly, quoting the change that satisfies it.

Then run `/carve-out $ARGUMENTS` and present the register. No issue in the
batch is closed until the maintainer has acknowledged it.

## 6. PR

`gh pr create` with a body that:

- lists `Closes #<n>` for every issue fully resolved (and `Refs #<n>` for any
  only partly addressed, saying what is left);
- has one section per issue, mapping acceptance criteria to changes;
- names every judgement call made and who approved it;
- flags any deltadewa-side follow-up as a separate task, not a TODO in this
  repo.

Do not merge. Report the PR URL and stop.
