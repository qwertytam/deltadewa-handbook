# Prompt playbook — resolving deltadewa-handbook issues #16–#27

Companion to the `.claude/` bundle. Five batches, in dependency order, each one
branch and one PR. Prompts are written to be pasted verbatim into Claude Code
in VS Code.

## Setup, once

1. Copy `CLAUDE.md` to the repo root and the `.claude/` directory alongside it.
   Commit them on their own branch — tooling config landing in the same PR as
   content changes makes both harder to review.
2. Confirm the toolchain: `poetry install --only dev`, then `/verify`. It
   should report PASS against a clean `main`. If it does not, fix that before
   touching any issue — you cannot tell your breakage from pre-existing
   breakage otherwise.
3. `gh` is installed and authenticated — confirmed. The `/issue` command reads
   issues and opens PRs through it.

## Batch order and why

| PR | Branch | Issues | Depends on |
| --- | --- | --- | --- |
| 1 | `docs/roll-timing-canon` | #27 (P1) | — |
| 2 | `docs/consistency-sweep` | #21, #22, #23, #24 | PR1 — both edit the targets page |
| 3 | `docs/mechanics-gaps` | #16, #17, #19, #25(c)(d) | PR2 — #19's table is where #25(c) lands |
| 4 | *(no branch)* | #18 | — runs any time; produces a private doc, not a commit |
| 5 | `docs/cross-repo-seams` + a deltadewa PR | #20, #26, #25(a)(b) | PR3 — both touch Appendix A4 |

Three ordering traps. #27 and #23 both rewrite
`docs/part-7/typical-hedge-program-targets.md`. #17 and #26 both edit
`docs/appendices/a4-crash-repricing-methodology.md`. And PR2 moves the
"Mathematical Definition of the Ratio" heading out of
`docs/part-10/tier-1-core-hedge-metrics.md` — which is one of the nine anchors
that #20 is repointing deltadewa's coverage doc at, so PR5 must resolve those
links against the *final* headings, not today's. Sequencing avoids all three;
running batches in parallel invites them.

## A conflict to resolve before PR3 and PR5

Three acceptance criteria ask the handbook to describe **the deltadewa
application specifically**:

- #25(a) — "state what deltadewa actually implements (the SKEW index
  percentile)"
- #25(b) — realized-carry methodology, framed as feeding a deltadewa issue and
  the digest
- #19 — a table column for "which deltadewa surface shows it"

Under the general-reference rule these are carve-outs, not content. The
handbook can define the *measure* (25Δ risk reversal, SKEW index percentile,
and how they differ) without ever saying which one a particular application
reads. Recommended resolution: write the general half in the handbook, move
the application half to a deltadewa-side issue, and note the split when closing
each issue. Confirm before PR3 starts.

---

## PR1 — Roll timing (#27, the only P1)

**Decided:** remaining-maturity framing is canonical — "roll when 9–12 months
remain". `rolling-rules.md` Rule 1 is the outlier and gets rewritten.

```text
/issue 27

Standing decision, already made: remaining-maturity framing is canonical.
The handbook says "roll when 9–12 months remain" everywhere. Rule 1 in
docs/part-7/rolling-rules.md currently says "roll after 9 to 12 months" —
that is the defect, not the standard.

Before editing, run /audit-claim "9–12 months roll timing" so we have every
location, including paraphrases that carry the timing without the numbers
(anything about theta acceleration, the danger zone, or when to act).

Then propose, and stop:
  - the exact replacement wording for Rule 1
  - which page owns roll timing (I expect
    docs/part-7/typical-hedge-program-targets.md) and what it should say
  - which of the other locations should stop restating the numbers and link
    to the owner instead
  - any location where the prose logic assumes elapsed time and needs more
    than a numbers swap
  - anything about the *live* book or the dashboard's roll trigger that this
    surfaces — carve that out, do not write it into docs/

The issue's fourth acceptance box is "audit downstream tools against the
final interpretation". That is a deltadewa-side check, not a handbook edit —
report what needs checking there rather than editing that repo.
```

Acceptance: all six locations agree on the remaining-maturity referent; the
targets page owns the numbers; both CI gates clean; the deltadewa-side audit is
written up for a separate issue there.

---

## PR2 — Consistency and accuracy sweep (#21, #22, #23, #24)

Four small issues, one branch, one commit each.

```text
/issue 21 22 23 24

Work these as one batch, one commit per issue. Notes per issue:

#23 carry budget — the targets page is the canonical home. It should present
all the bands that legitimately exist (institutional 1–3%, family office
0.5–1.5%, the ~4% richer-program case) and say what distinguishes them,
rather than picking one. The Quick Start, the IPS example in
program-constraints, and convexity-budget should link to it instead of
restating their own numbers. The "family office survey data" claim is
unsourced: try source-verifier for a real survey; if there is no primary
source, soften the wording so it no longer implies a citation, and list that
in the PR body. Already checked (2026-08-16): the UBS Global Family Office
Report — the largest such survey — quantifies allocation and derivative usage
but gives no hedging premium budget as a percentage of AUM. Treat "family
office survey data" as unsourceable unless you find something better.

#24 — (a) pick one basis for the β=0.85 example and state it explicitly at
both the 15% and 18% mentions; (b) align net-delta's formula and worked
example on the contract multiplier; (c) the "10% spread premium" on XSP gets
sourced or softened, same rule as above; (d) VIX 2020 — say explicitly which
of intraday 85 / closing 82.69 is meant, and prefer naming both.

On (c), already checked (2026-08-16): Cboe's own Mini-SPX publication gives
an absolute figure — a 3-cent ATM spread on roughly $31,000 of notional — but
no comparison against SPX or SPY, so nothing supports "10%". Preferred fix is
not just softening but stating the actual mechanism: a comparable quoted tick
is a larger fraction of premium on a contract one-tenth the notional, so
execution cost per unit of exposure is what to compare, not the tick. That is
general, true, and needs no number.

#22 — my preference is to scope the Greeks table to "long options, typical"
rather than widen every range, unless you think the table is used as a
general reference in a way that makes scoping misleading. Say which and why
before editing.

#21 — the split is decided: dashboard-related material stays in
docs/part-10/tier-1-core-hedge-metrics.md; definitions of terms stay in
docs/part-5/convexity.md and Part VI. Apply it:

  - convexity.md:29–34 keeps its qualitative payoff-shape table — it
    illustrates the definition. Delete the editing note at line 36.
  - tier-1's dollar crash-scenario table (lines 19–26) and both ASCII
    dashboard blocks stay where they are.
  - tier-1 §5 currently holds a *definition*: the Carry-Convexity Ratio
    formula (line 72), the worked example (74–80), the interpretation bands
    (84–88) and the typical-values table (94–97). Under the rule that earlier
    chapters own the material, all four move to Part VI, and tier-1 keeps the
    dashboard visualisation plus a link.
  - preserve the <a id="convexity-carry-worked-example"></a> anchor when the
    worked example moves, and tell me every heading anchor the move changes —
    deltadewa's coverage doc links to #mathematical-definition-of-the-ratio,
    so #20 depends on where this lands.
  - tier-1 line 96 states carry as "1 to 3% per year". That is a fifth
    carry-budget location which #23 does not list — fold it into #23's fix.
  - the typical crash-convexity band at tier-1 line 97 is 15–40%, but
    evaluating-and-testing-tail-hedge-strategies.md:166 gives a target of
    15–25%. Ask me which is the general band before publishing either.
  - propose the CI guard the issue asks for: a grep step in
    .github/workflows/ci.yml that fails if TODO, TBD, FIXME or "Editing note"
    appears under docs/. Its own step, not a markdownlint rule.

Start with /audit-claim on the carry-budget ranges and on the β=0.85
overhedge figures before touching anything.
```

Acceptance: no number restated on a non-canonical page without a link; nothing
softened without being listed in the PR body; the editorial note gone and the
CI guard passing on a deliberately seeded `TODO` before you remove it.

---

## PR3 — Mechanics gaps (#16, #17, #19, #25 c and d)

This is the batch with real writing in it. Resolve the general-vs-application
conflict above first.

```text
/issue 16 17 19

Plus #25 items (c) and (d) only — (a) and (b) are cross-repo and belong in a
later batch.

#16 settlement — dispatch source-verifier against Cboe's own SPX/SPXW product
specifications for: AM settlement of standard monthlies against the opening
print, SET, PM settlement of SPXW weeklies and EOM, and the exercise-notice
mechanics. Every fact gets a citation in docs/footnotes/index.md. Add the
settlement-mechanics subsection to docs/part-1/exercise-settlement.md and the
settlement-timing row to the instrument-choice table. The guidance about not
holding through AM settlement should be written as a general operator
principle with its reasoning, not as an instruction to one program.

#17 margin and short legs — general treatment only: how short legs consume
buying power, how Reg-T and portfolio margin differ in principle, leg-by-leg
versus spread-order execution when markets are moving, and how a capped upper
wing interacts with skew steepening in the A4 repricing methodology. No
broker, no account type, no live-book composition — carve those out. A4 gets
a note on capped wings, not a rewrite.

#19 ratio table — decided: it goes at the front of Part VI, as a new page
listed early in that Part's nav, because definitions belong in the earliest
Part that owns them and later Parts refer back. Drop the "which deltadewa
surface shows it" column — that is application detail. Columns: primary name,
synonyms in use, formula with numerator and denominator written out,
interpretation band.

Six rows, with where each currently lives:

  1. Crash convexity — docs/part-6/crash-convexity.md:33 (and a second form
     at :129); restated at docs/appendices/a4-crash-repricing-methodology.md:5
  2. Crash payoff / offset ratio — docs/part-6/crash-payoff-ratio-tail-hedge-
     effectiveness.md:22, bands at :45. "Offset ratio" as a synonym at
     part-7/typical-hedge-program-targets.md:11, part-7/evaluating-and-
     testing-tail-hedge-strategies.md:331 and :348, footnotes/index.md:45
  3. Payoff-vs-premium multiple — defined nowhere; zero hits in docs/
  4. Convexity/carry ratio (hedge efficiency) — four names across four pages,
     and two different numerators:
       part-6/hedge-efficiency-ratio.md:14  "Hedge Efficiency = crash payoff / annual carry"
       part-10/tier-1-core-hedge-metrics.md:72  "Carry-Convexity Ratio = Convexity / Carry"  (name inverted against its own formula)
       part-7/evaluating-and-testing-tail-hedge-strategies.md:25  "Carry-to-Convexity = Crash Payoff Ratio(25%) / Annual Carry Budget"  (different numerator)
       part-10/introduction.md:31  "Convexity/carry ratio: 7.5"  (and tier-1's worked example gives 7.3)
  5. Theta carry — docs/part-6/theta-carry-insurance-cost.md:15
  6. Vega sufficiency — docs/part-6/vega-sufficiency.md:26, alternatives
     at :32, further metrics at :39

Row 4 is the real work: pick one primary name, one numerator, and say plainly
in the synonyms column that the other three names exist and which of them
computes something different. Row 3 is net-new (#25c). Every metric page then
links to its row instead of restating the definition.

#25(c) payoff-vs-premium multiple gets defined in that table. #25(d) — move
the terms currently defined only inline into
docs/appendices/a1-additional-terminology.md, including SET from #16.

Plan first, including which target bands you propose to publish and where
each comes from. A band that exists only because one program chose it is a
carve-out, not a table cell.
```

Acceptance: every new external fact cited; the ratio table is the single
definition site and metric pages link to it; A1 gains the inline-only terms;
strict build clean (new pages wired into `nav`); carve-out register reported.

---

## PR4 — Continuity (#18) — no repo changes

**Decided:** the continuity annex stays entirely out of the repo. The handbook
closes #18 with a pointer; the substance lives in a private document.

Run this in a session you are happy to keep off the record — it will discuss
succession specifics.

```text
Do not create or edit any file in this repo for this task.

Draft a private continuity document, as a standalone file outside the
repository, covering what a partner needs if I am unable to run the program:

  - the maintain-versus-wind-down decision, framed so a non-specialist can
    make it, with what each choice commits them to
  - concrete steps to close SPX positions, in order, including what "do
    nothing yet" looks like and how long it is safe
  - which decisions are time-sensitive versus deferrable, with the actual
    deadlines that drive them (expiry, settlement, margin)
  - what to hand to whom, described by role rather than name
  - the questions a partner should ask a broker or adviser, with the answers
    that should worry them

Leave every place I must supply a specific — names, brokers, account
locations, contacts — as a clearly marked blank. Never invent one and never
put credentials in the file.

Then, separately: #18 also asks for a weekly 10-minute review checklist. Tell
me which items of that are general enough to publish as a handbook page (a
review cadence and what to look at) and which are specific to my setup (the
digest, the dashboard, my thresholds). If the general half is worth a page,
propose it as a follow-up issue rather than adding it here.
```

Acceptance: private document delivered outside the repo; #18 closed in GitHub
with a comment recording that continuity is deliberately private; a follow-up
issue opened if the general review-checklist page is worth writing.

---

## PR5 — Cross-repo seams (#20, #26, #25 a and b)

Two PRs: one here, one in `qwertytam/deltadewa`.

```text
/issue 20 26

Plus #25 items (a) and (b).

Start with cross-repo-scout. Clone deltadewa read-only outside this working
tree. I need from it:
  - all nine HANDBOOK.md#anchor links in deltadewa/docs/part-x-coverage.md,
    each resolved to the correct published URL under
    https://qwertytam.github.io/deltadewa-handbook/ — verify each anchor
    against the actual handbook page, do not guess slugs. Resolve them against
    main *after* PR2 and PR3 have merged: #mathematical-definition-of-the-ratio
    moves out of tier-1 in PR2, and the ratio table added in PR3 is probably
    the correct destination for several of the nine.
  - whether the repricing worked-example figures ($5,226,004, +24.6%, 17.5×)
    still agree across both repos
  - what the app actually computes for skew percentile and for realized carry,
    with file references

Then split the work explicitly into two lists:

This repo: the A4 spec version/date stamp (#26); the note in README or
HANDBOOK.md that anchors follow MkDocs Material's heading-slug convention
(#20); the general definitions for #25(a) — one stated lookback window, and
the distinction between a 25Δ-based skew measure and the SKEW index
percentile as measures, written without reference to what any application
reads — and #25(b), the realized-carry methodology as a method.

deltadewa repo: repoint the nine coverage-doc links; delete the
hedging-handbook.md stub; add the pointer comment from the repricing test
back to Appendix A4; add the link-check CI step for github.io URLs; and take
on anything from #25(a)/(b) that describes what the application implements.

Open the handbook PR first. For deltadewa, prepare the branch and PR body but
show me before pushing — that repo has its own review standards and I have
not reviewed its state in this session.
```

Acceptance: no dead cross-repo links; A4 carries a version stamp; the
duplicated repricing figures either agree or a divergence is filed; the
deltadewa-side changes are in their own PR in their own repo.

---

## Standing habits for every batch

- `/audit-claim` before changing any number. The handbook restates figures in
  places that grep for the number will not find.
- `/verify` before every commit, not just before the PR. The strict build
  catches broken anchors immediately after the edit that broke them, when the
  fix is obvious.
- `/carve-out` before closing anything.
- One commit per issue, so a single issue can be reverted after review.
- If a batch runs long, the sub-agents are the lever: sweeps, source
  verification, build logs and the second repo all belong outside the main
  context.
