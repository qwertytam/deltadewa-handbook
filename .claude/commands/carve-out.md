---
description: Collect and report everything that would pull the handbook toward one specific program, for the maintainer's private document
argument-hint: "[issue numbers in this batch]"
disable-model-invocation: false
---

Produce the carve-out register for: $ARGUMENTS

The handbook is a **general reference**. Program-specific material is carved
out, never written in and never paraphrased into a generic-sounding sentence.
See the scope-boundary section of `CLAUDE.md` for what counts.

## What to sweep

Go back over everything the batch surfaced — issue bodies, sub-agent findings,
draft prose, and anything you decided not to write — and pull out every item
that is true of one book rather than of hedging programs generally: live book
composition, broker or account or margin regime, named people and contacts,
one investor's chosen band presented as the number, and anything true only
because of how the deltadewa application is built.

Include items you already excluded silently. The register is the maintainer's
record, not a list of your mistakes — an item you correctly kept out of `docs/`
still belongs here so they can capture it privately.

## Output

```markdown
## Carve-out register — batch <name>, issues #<n>, #<n>

### <short title>
- **Surfaced by:** #<issue>, <where — issue body / A4 / source-verifier finding>
- **The specific fact:** <what it actually is>
- **Why it is carved out:** <which scope-boundary category>
- **What the handbook says instead:** <the general version written, or "nothing">
- **Where the maintainer will need it:** <private continuity doc / IPS / deltadewa config / broker file>
```

End with a one-line count and this sentence: *"No issue in this batch closes
until this register is acknowledged."*

## Rules

- Never write the register into `docs/`, and never commit it to this repo.
- Reproduce the specific fact accurately in the register — it exists so the
  maintainer can record it privately, so a vague entry is useless.
- Do not include credentials, account numbers or passwords even here. Refer to
  them ("the broker login lives in X") rather than reproducing them.
- If the batch produced nothing program-specific, say exactly that.
