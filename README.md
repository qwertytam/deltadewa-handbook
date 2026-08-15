# Hedging Handbook

A practical reference for the design, implementation, and ongoing management of
a systematic downside hedging program for a long-only equity portfolio.

**📖 Read it here: <https://qwertytam.github.io/deltadewa-handbook/>**

> **Educational and operational reference only — not investment advice.**
> Nothing here should be implemented without independent analysis, legal review
> of the investment mandate, and consultation with qualified derivatives
> professionals. Tax content is for general orientation and is not tax advice.

## Contents

The handbook is written to be read sequentially on a first pass and used as a
reference thereafter.

| Part | Topic |
| ---- | ----- |
| Preface | Philosophy, scope, limitations |
| Quick Start | Five key decisions to orient quickly |
| I–II | Options fundamentals and the Greeks |
| III–IV | Volatility, the vol surface, trading terminology |
| V–VI | Tail-hedging structures and metrics |
| VII–VIII | Program design, monetization and re-risk rules |
| IX–XI | Common mistakes, dashboards, further reading |
| Appendices | Terminology, formulas, tax, crash repricing methodology |

## Local development

Requires Python 3.14+ and [Poetry](https://python-poetry.org/).

```bash
poetry install --only dev     # install mkdocs-material and tooling
poetry run mkdocs serve       # live-reload preview at http://127.0.0.1:8000
poetry run mkdocs build --strict   # the exact build CI runs
npx markdownlint-cli2         # the exact Markdown lint CI runs
```

`--strict` promotes MkDocs warnings to errors. Broken internal links, missing
heading anchors, and pages absent from the nav all fail the build, so run it
before opening a pull request. `mkdocs serve` deliberately leaves these as
warnings so that drafting is not blocked.

## Repository layout

```text
docs/                 # all handbook content, one directory per part
  index.md            # site landing page (reached via the header title)
  <part-n>/index.md   # part overview, shown as the section landing page
  footnotes/index.md  # central References page; cited via #anchor links
  javascripts/        # MathJax configuration for pymdownx.arithmatex
mkdocs.yml            # site config, nav, and validation rules
.markdownlint-cli2.jsonc  # Markdown lint rules, shared by CI and VS Code
.github/workflows/    # ci.yml (lint + build check), deploy.yml (Pages deploy)
```

### Heading levels

Page bodies start at `##`. The `#` comes from the `title:` front matter, which
Material renders as the page heading — so a page that opens with `##` produces
a correct `h1 → h2 → h3` outline. Do not add an `#` heading to a page body.

## Authoring conventions

- **Front matter.** Every page sets a `title:`, which is what the nav shows.
- **Cross-references.** Link to other pages by relative *source* path, e.g.
  `[Crash Convexity](../part-6/crash-convexity.md)`. MkDocs rewrites these to
  the correct URL and validates them under `--strict`. Do not hand-write
  built URLs.
- **Citations.** Add the source to `docs/footnotes/index.md` with an explicit
  `{ #slug }` anchor, then cite it inline as
  `[[Short Label]](../footnotes/index.md#slug)`.
- **Maths.** Inline maths is `$...$` with no space inside the delimiters
  (`$S$`, not `$ S $`); display maths is `$$...$$`. A literal dollar sign in
  prose is escaped as `\$`, including inside a maths expression
  (`$\text{Cost} = \$225k$`).
- **Callouts.** Use admonitions rather than a bare `Note:` paragraph. Content
  must be indented four spaces:

  ```markdown
  !!! note

      Body text here.

  !!! warning "Custom title"

      Used for anything with legal or tax consequence.
  ```

## Deployment

Every push to `main` builds the site and publishes it to GitHub Pages via
OIDC (`actions/deploy-pages`). The workflow holds `contents: read` only — it
has no write access to the repository.

## Licence

Code and configuration are MIT licensed — see [LICENSE](LICENSE).
