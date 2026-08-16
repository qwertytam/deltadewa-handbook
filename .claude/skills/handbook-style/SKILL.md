---
name: handbook-style
description: House style for writing or editing pages in the Hedging Handbook — voice, page shape, tables, worked examples, admonitions, maths, citations and nav wiring. Use whenever drafting a new page or section, rewriting prose, or reconciling a number across pages.
---

# Handbook house style

## Voice

The reader is a competent investor running, or about to run, a real hedging
program with real money — not a student and not a quant. Write the way the
existing pages do:

- Declarative and unhedged about mechanics; explicitly hedged about outcomes.
  "SPX options are European and cash-settled" is a fact. "This typically
  reduces drawdown by..." needs its conditions stated.
- Short paragraphs. One idea each. No throat-clearing openers — the first
  sentence of a page states what the page is for.
- Second person for instructions to the operator; no "we".
- No marketing register, no "powerful", "robust", "seamless".
- Every number carries its basis: percent *of what*, over *what horizon*,
  measured *how*. Most defects in this handbook are a missing basis, not a
  wrong number.
- British/US spelling follows whatever the surrounding page already uses;
  do not restyle a page you are only patching.

## Scope

General reference, not one investor's manual. Write the mechanism, the
trade-off, and the questions an operator must answer — never the answer one
particular program chose. "Short SPX puts consume buying power under Reg-T and
portfolio margin differently; confirm which regime the account is under before
sizing" is in scope. "The program runs put spreads under portfolio margin at
<broker>" is not — carve it out (see `CLAUDE.md`), do not paraphrase it.

Where a value genuinely differs by investor type, present the range and what
distinguishes the cases, and let the reader locate themselves in it.

## Page shape

```markdown
---
title: "Sentence Case Title"
---

One or two sentences: what this page is and when the reader needs it.

## First Section

Body.

### Subsection

Body.
```

Body starts at `##` — the `h1` comes from `title:`. A metric page conventionally
runs: definition → formula → worked example → interpretation → target band →
failure modes.

## Mechanics

- **Maths.** `$\Delta$` inline, no spaces inside the delimiters. Display maths
  in `$$...$$`. Literal dollars escape as `\$`, including inside maths:
  `$\text{Cost} = \$225k$`.
- **Worked examples.** Inputs in a fenced ` ```text ` block, then the result in
  a second ` ```text ` block, matching the existing metric pages. Give an
  explicit anchor before a reusable example so other pages can link to it:
  `<a id="hedge-efficiency-dollar-worked-example"></a>`.
- **Tables.** Header row, then a separator row; keep columns narrow enough to
  read on a phone. A comparison table needs a units row or a units suffix in
  every cell — a bare number in a table is where basis gets lost.
- **Admonitions.** Four-space-indented body. `!!! note` for asides,
  `!!! warning` for anything with legal, tax or capital consequence,
  `!!! tip` for operator shortcuts. Collapsible variants use `???`.
- **Cross-references.** Relative source paths only:
  `[Rolling Rules](../part-7/rolling-rules.md)`. Add `#anchor` only if the
  target heading actually exists.
- **Inline HTML.** Only `<a>`, `<br>`, `<sup>`, `<sub>`.
- **Never** leave `TODO`, `TBD`, `FIXME` or an editorial note in `docs/` —
  it publishes on merge.

## Citations

External facts need a source. Add the entry to `docs/footnotes/index.md` under
the right group, with an explicit anchor on its heading:

```markdown
### Cboe (2026) — SPX Options Specifications { #cboe-spx-specs }

Cboe Global Markets, *S&P 500 Index Options Product Specifications*,
retrieved 2026-08-16.

Establishes the AM/PM settlement split between standard monthly SPX series and
SPXW weeklies, and the SET calculation.
```

Then cite inline: `[[Cboe SPX Specs]](../footnotes/index.md#cboe-spx-specs)`.

Reuse an existing anchor rather than adding a second entry for the same source.

## Numbers and canon

One page owns each number (see the canonical-sources table in `CLAUDE.md`).
When you need a value on a non-canonical page:

- prefer naming the concept and linking: "within the annual carry budget
  ([targets](../part-7/typical-hedge-program-targets.md))";
- if the number must appear, state its basis and say it is the canonical
  figure's application to this case, so a future reader can tell a restatement
  from a contradiction.

Never introduce a fourth phrasing of a range that already has three.

## Wiring a new page

1. Create `docs/part-N/slug.md` with front matter.
2. Add it to `nav:` in `mkdocs.yml`, inside the right Part, with a nav title.
3. Link it from the Part's `index.md` if that index lists its pages.
4. Run the build gates — an orphaned page fails `--strict`.
