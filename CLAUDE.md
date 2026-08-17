# CLAUDE.md — deltadewa-handbook

Project memory for Claude Code. Facts and hard rules only; procedures live in
`.claude/skills/` and `.claude/commands/`.

## What this repository is

A Material for MkDocs site — the *Hedging Handbook*, a reference for running a
systematic downside-hedging program for a long-only equity portfolio. It is
content, not software: `pyproject.toml` sets `package-mode = false` and there
are no Python sources to import or test. Roughly 110 pages under `docs/`,
~28k words, one directory per Part.

Published at <https://qwertytam.github.io/deltadewa-handbook/>.

The companion **application** repo is `qwertytam/deltadewa` (Python options
hedging dashboard). It is a *separate* repo with its own PRs. Some issues here
have a deltadewa-side half — never edit that repo from a handbook branch.

## Commands

```bash
poetry install --only dev            # toolchain (mkdocs-material etc.)
poetry run mkdocs serve              # live preview, warnings stay warnings
poetry run mkdocs build --strict     # the exact gate CI runs — must pass
npx --yes markdownlint-cli2@0.23.2   # the exact lint CI runs (version pinned)
```

Run **both** the strict build and the pinned markdownlint before opening a PR.
`--strict` promotes MkDocs warnings to errors: a broken relative link, a
missing heading anchor, or a page absent from `nav` fails the build.

Note the markdownlint version pin. CI runs `markdownlint-cli2@0.23.2`; a bare
`npx markdownlint-cli2` may resolve to a newer release with different rules and
disagree with CI in either direction.

## Hard authoring rules

These are enforced by CI or by convention; breaking them breaks the build or
the published page.

1. **Front matter.** Every page starts with `---` / `title: "..."` / `---`.
   The `title` is what the nav shows and what Material renders as the `h1`.
2. **Heading levels.** Page bodies start at `##`. Never put an `#` heading in
   a page body — the `h1` comes from `title:`.
3. **Nav.** Every new page must be added to the `nav:` list in `mkdocs.yml`,
   in the right Part, or the strict build fails as an orphaned file.
   `docs/index.md` is the one deliberate exception (`not_in_nav`).
4. **Cross-references.** Link by relative *source* path:
   `[Crash Convexity](../part-6/crash-convexity.md)`. Never hand-write a
   built URL, and never use a root-absolute path.
5. **Citations.** Add the source to `docs/footnotes/index.md` under the right
   group with an explicit `{ #slug }` anchor on its heading, then cite inline
   as `[[Short Label]](../footnotes/index.md#slug)`.
6. **Maths.** Inline `$S$` with no space inside the delimiters; display
   `$$...$$`. Escape a literal dollar as `\$`, including inside maths
   (`$\text{Cost} = \$225k$`).
7. **Callouts.** Use admonitions (`!!! note`, `!!! warning "Custom title"`)
   with the body indented four spaces. Anything with legal or tax consequence
   uses `!!! warning`. Never a bare `Note:` paragraph.
8. **Inline HTML.** Only `<a>`, `<br>`, `<sup>`, `<sub>` (MD033 allowlist).
   Explicit anchors are written as `<a id="slug"></a>`.
9. **No editorial notes in `docs/`.** No `TODO`, `TBD`, `FIXME`, or "Editing
   note:" — `docs/` is published on every push to `main`.
10. **Licence.** Content under `docs/` is CC BY-ND 4.0. Never remove or soften
    the disclaimers on `docs/preface/important-limitations.md`, and never
    delete the "not investment advice" framing from a page.

## Scope boundary — general reference only

**Standing instruction from the maintainer.** The handbook is a *general
reference*. It is not the maintainer's operating manual. Anything that starts
pulling it toward one specific program must be **carved out**, not written in.

Program-specific means anything true of one book rather than of hedging
programs generally:

- the composition of a live book (that it is put spreads, its strikes,
  notional, or counterparties);
- a specific broker, account type, margin regime, custodian or platform;
- named people, contacts, credentials, or succession arrangements;
- one investor's chosen budget, band or threshold presented as *the* number;
- anything only true because of how the deltadewa application happens to be
  built.

When a task turns up program-specific material:

1. Do **not** write it into `docs/`. Do not write a generic-sounding paraphrase
   of it either — that is the same defect with the identifying detail filed off.
2. Write the general version if one exists — the mechanism, the trade-off, the
   questions an operator should ask — with no assumed answer.
3. Record the carved-out item in the batch's **carve-out register** (see
   `/carve-out`): what it was, which issue surfaced it, and where the
   maintainer will need it.
4. **Report the register to the maintainer before any issue is closed**, so it
   can be recorded in their private document. An issue is not done while its
   carve-outs are unreported.

This applies to every issue, current and future.

## Standing decisions

Do not re-litigate these; change only on explicit instruction.

- **Roll timing** is expressed as **remaining** maturity: "roll when 9–12
  months remain". Never "roll after 9–12 months" — that reads as elapsed time
  and puts an 18-month put into the 6–9 month theta-acceleration zone the
  handbook warns against.
- **Where material lives.** Define once, in the earliest Part where the
  material belongs; later Parts refer back rather than restating. Definitions,
  formulas, interpretation bands and typical values live in Parts I–VII. Part
  X describes what a dashboard *displays* and links to the definition — a
  formula or a band appearing for the first time in Part X is a defect.
- **Unsourced numbers.** Try to source from a primary authority first
  (`source-verifier`). If no primary source exists, replace the figure with
  qualitative wording that drops the implied citation — "a materially wider
  spread", not "a 10% spread premium" — and list every softening in the PR
  body. Never keep a specific figure that implies a citation you cannot give.
- **Judgement calls.** Complete everything unambiguous first, then present all
  open calls at once, as one numbered list with options and a recommendation,
  and stop. One interruption per batch, not one per question.
- **Cross-repo.** Two specs are duplicated in `deltadewa` and must move
  together. Changing a figure in either half requires the matching change in
  the other, in a separate PR in that repo.
    1. The crash-repricing spec in
       `docs/appendices/a4-crash-repricing-methodology.md` and
       `deltadewa/docs/repricing-methodology.md` share worked-example figures.
    2. The hedge-efficiency ratio in `docs/part-6/hedge-efficiency-ratio.md`
       is pinned in deltadewa code: `ips_config.py` hardcodes the
       interpretation band (`3.0` / `6.0`) against that page's table, and
       `tests/test_analysis/test_hedge_efficiency.py` asserts the page's
       worked example (`22 / 3 = 7.3333`). Changing the band or the worked
       example breaks that test.

## Canonical sources

Numbers, ranges and metric names have **one owning page**. Other pages link to
the owner instead of restating the value. Before changing or introducing any
number, check the owner first; if a page disagrees with its owner, the owner
wins and the other page gets a link.

| Subject | Canonical page |
| --- | --- |
| Roll timing, maturity and roll-interval targets | `docs/part-7/typical-hedge-program-targets.md` |
| Annual carry / premium budget ranges | `docs/part-7/typical-hedge-program-targets.md` (family-office paragraph) |
| IPS-style hard constraints | `docs/part-7/program-constraints-and-governance.md` |
| Ratio names, formulas, interpretation bands | `docs/part-6/ratio-disambiguation.md` |
| Crash-repricing spec and worked example | `docs/appendices/a4-crash-repricing-methodology.md` |
| Greeks definitions and formulas | `docs/appendices/a2-mathematical-formula.md` |
| Term definitions | `docs/appendices/a1-additional-terminology.md` |
| Every external source | `docs/footnotes/index.md` |

A range that legitimately differs by investor type (institutional vs family
office) is still owned by one page: the owner states every band and what
distinguishes them, and other pages link rather than picking a favourite.

## Git and PR workflow

`main` is protected: force-push and deletion blocked, a PR is required, and
both `Lint Markdown` and `Build docs (strict)` must pass. Admins can bypass —
do not.

- Branch from `main`, one branch per themed batch of issues.
- Commit message and PR body reference the issues (`Closes #23, #24`).
- Never commit to `main` directly, never force-push, never merge your own PR
  without being asked.
- `site/` is a build artifact — never commit it.

## Definition of done for an issue

1. The carve-out register for the batch has been reported to the maintainer
   and acknowledged. Nothing closes before this.
2. Every box in the issue's acceptance criteria is satisfied, or explicitly
   flagged as deferred with a reason.
3. `poetry run mkdocs build --strict` and `npx --yes markdownlint-cli2@0.23.2`
   both clean.
4. Any number changed on a non-canonical page is either removed in favour of a
   link to its owner, or the owner was updated too.
5. Any new external fact carries a citation in `docs/footnotes/index.md`.
6. New pages appear in `mkdocs.yml` `nav`.
7. The PR body lists what changed per issue, names any judgement call made,
   and lists what was carved out rather than written.

## Token discipline

The corpus is large and mostly prose; reading whole Parts to answer a narrow
question is the main way a session burns context here.

- Use the `docs-auditor` sub-agent for "where does the handbook say X"
  sweeps — it returns `file:line` plus a one-line quote, not page bodies.
- Use `build-verifier` for lint and strict builds — it returns failures only,
  not the build log.
- Use `source-verifier` for anything needing the open web.
- Use `cross-repo-scout` for anything in `../deltadewa`.
- Drafting and editing stay in the main thread, where the maintainer reviews
  them. Sub-agents gather; the main thread writes.
