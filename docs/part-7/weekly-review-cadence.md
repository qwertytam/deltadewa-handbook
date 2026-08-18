---
title: "Weekly Review Cadence"
---

A tail-hedge program is designed once and then operated for years. This page
covers the operating rhythm: a short, fixed, scheduled review, what it looks at,
and — the part that makes it work — what it is not allowed to decide.

The program's governing document sets the review frequency that carries
authority, which is
[quarterly](program-constraints-and-governance.md#investment-policy-statement-ips-integration),
with an annual review of the parameters themselves. The weekly check described
here sits underneath both. It is not a governance review, it changes nothing,
and it exists so that the quarterly review is never the first time anyone
notices something.

## Why a Fixed Short Review Beats Continuous Attention

Continuous attention feels like diligence and behaves like a trading desk. A
hedge that is watched all day is a hedge that gets adjusted in response to
things that were never part of its design — a bad week, a headline, a number
that looked wrong out of context. The program's edge comes from being
systematic, and continuous attention erodes exactly that.

The opposite failure is worse and more common. A program nobody looks at drifts:
the portfolio it was sized against changes, expiries approach unnoticed, and
carry accumulates without anyone comparing it to what was budgeted. Then a
quarterly review turns up three months of drift at once, which is when programs
get abandoned rather than corrected. See
[Behavioral Risks — Abandoning the Program](../part-9/behavioral-risks-abandoning-the-program.md).

A scheduled review produces neither. It is frequent enough that nothing
accumulates for long, and bounded enough that it does not become a place to
take positions. Fixing the time matters as much as fixing the content: a review
that happens when you feel like checking is a review that happens most often
when you are anxious, which is the worst possible sampling.

Keep it short. The right length is one that survives a busy quarter — long
enough to look at four things and note what changed, short enough that it never
competes with anything. Ten minutes is the right order of magnitude. A review
that grows to an hour is a review that gets skipped in the year it matters, and
one that has quietly turned into something other than a review.

## The Four Categories

Look at four things. These are categories, not thresholds — the numbers that
define "too far" belong to your program's own documented parameters, and the
ranges those are drawn from live in
[Typical Hedge Program Targets](typical-hedge-program-targets.md).

**Time to the nearest expiry.** The one item that changes predictably and never
in your favour. You are checking whether the nearest position has entered the
window where the roll rules apply, and whether its last trading day is where you
assumed — for standard monthly index series, that is not the same date as
settlement. See
[Rolling Rules](rolling-rules.md) and
[AM and PM Settled Series](../part-1/exercise-settlement.md#am-and-pm-settled-series).

**Whether the hedge is still sized to the portfolio it protects.** Hedge
notional is fixed at the trade; the portfolio it was sized against is not. A
long rally leaves a program under-hedged in percentage terms without any
position changing, which is the drift that goes unnoticed longest because
everything looks fine. See
[Portfolio Hedge Sizing Framework](portfolio-hedge-sizing-framework.md).

**Whether carry is tracking budget.** Compare accrued cost against what was
budgeted for the period, and note the direction of the gap rather than the
value. A program running over budget is a decision waiting for the next
governance review; a program running well under it may be carrying less
protection than intended. See
[Realized Carry Methodology](realized-carry-methodology.md).

**Whether any pre-defined trigger has fired.** The monetization and re-risk
triggers in your governing document are conditions, not judgements. The weekly
check is where you find out one has been met — the trigger's own rules then say
what happens, and that is not a weekly-review decision. See
[Typical Monetization Triggers](../part-8/typical-monetization-triggers.md) and
[Re-Risking Rules](../part-8/re-risking-rules.md).

## Notice, Do Not Decide

This is the discipline that makes the whole thing work, and it is a single rule:

!!! note

    **A weekly review is for noticing. It is not for deciding.**

The review's output is an observation — a roll window is open, sizing has
drifted, a trigger has fired. What happens next is determined by rules written
in advance: the
[Rolling Rules](rolling-rules.md) for when and how positions are replaced, and
the [Monetization Triggers](../part-8/typical-monetization-triggers.md) and
[Re-Risking Rules](../part-8/re-risking-rules.md) for taking and rebuilding
protection. The weekly review invokes those rules; it does not compete with
them and it does not improvise around them.

Collapse the two and the routine stops being a control. A recurring appointment
to look at option positions with authority to act is a discretionary trading
session that happens to run weekly, and it will drift toward whatever the market
did that week. Separating them is what keeps a check on the program from
becoming a source of the very behaviour it exists to prevent.

The practical form of the separation: write down what you noticed, name the rule
it invokes, and act only if that rule says to. If you find yourself reasoning
about whether to act, you have found a gap in the rules — which is a finding for
the quarterly review, not something to resolve at the keyboard.

## Acting Between Reviews

A weekly cadence needs a closed list of things that justify acting sooner.
Without one, "something happened" becomes a standing invitation and the schedule
means nothing.

| Justifies acting between reviews | Does not |
| -------------------------------- | -------- |
| A margin call or a collateral shortfall | A large single-day market move |
| A documented monetization or re-risk trigger being met | Volatility rising or falling sharply |
| Nearest expiry inside its last trading week | A forecast, a headline, or a research note |
| A material change to the portfolio being hedged | The hedge showing a large gain or loss |
| A broker or account event preventing normal access | A roll window opening for the first time |

The right-hand column is the one to read carefully. Each entry is a real event
and each is a legitimate thing to *notice*; none of them is a reason to act
outside the schedule, because each is already handled by a rule with its own
timing. A large move that matters will have fired a trigger, and one that has
not fired a trigger is a move the program was designed to sit through.

If an item recurs in the right-hand column and keeps feeling urgent, that is
evidence about the rules rather than about the market. Raise it at the
quarterly review, where the parameters can be changed deliberately and on the
record.
