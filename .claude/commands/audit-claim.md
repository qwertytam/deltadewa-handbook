---
description: Find every place in the handbook that states, restates or contradicts a given number, range, term or claim
argument-hint: "\"1–3% carry budget\" | \"9–12 months\" | \"crash payoff ratio\""
disable-model-invocation: false
---

Dispatch the `docs-auditor` sub-agent to sweep `docs/` for:

$ARGUMENTS

Tell it to cover en-dash and hyphen forms, the spelled-out "to" form, the bare
numbers without units, symbol and spelled-out Greek letters, and to sweep for
paraphrases that carry the claim without its numbers.

Require its standard output: one table of `file:line | class | quote` plus a
one-paragraph verdict naming the canonical location, the contradictions, and
any place where changing the value means rewriting prose rather than swapping
a figure.

When it reports back, do not start editing. First state:

1. which page owns this value per the canonical-sources table in `CLAUDE.md`;
2. whether the owner currently states it correctly;
3. the list of restatements to replace with links, and the list of genuine
   contradictions to resolve;
4. any judgement call that needs the maintainer, phrased as a question with
   the options and your recommendation.

Then wait.
