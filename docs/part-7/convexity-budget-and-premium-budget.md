---
title: "Convexity Budget and Premium Budget"
---

Institutional tail hedge programs typically operate under two constraints:

1. Premium Budget
2. Convexity Target

## Premium Budget

The premium budget defines the acceptable annual cost of maintaining the hedge program.

The band a program should budget to depends on investor type and on how close to spot the ladder sits. See [Annual Premium Budget Bands](typical-hedge-program-targets.md#annual-premium-budget-bands) for the bands and what distinguishes them.

Note on cash management: premium is typically paid in advance when options are purchased. The portion of the annual hedge budget not yet deployed — for example, budget reserved for future quarterly rolls — should be held in short-duration, high-quality instruments (money market funds or short-term Treasuries) rather than left idle. At prevailing yields, a hedge budget held in short-term Treasuries for several months before deployment generates income that partially offsets the net theta cost of the program. This is a small but real benefit that improves the program's effective economics.

## Convexity Target

The convexity target defines the expected hedge payoff under a defined crash scenario.

A convexity target is a schedule of required payoffs across several crash
depths, which is what a program sizes against. That is not the same object as
the crash-convexity band in
[Typical Hedge Program Targets](typical-hedge-program-targets.md#typical-institutional-targets),
which is a single figure at a single depth — 10 to 20% at −25% SPX. The two are
the same metric, [Crash Convexity](../part-6/crash-convexity.md), read at
different scenarios, so a schedule cannot be checked against the band row by
row. Only its −25% row is comparable, and none of the illustrative rows below
is quoted there:

- +3% portfolio return during a −15% equity drawdown
- +5% portfolio return during a −20% equity drawdown
- +10% portfolio return during a −30% equity drawdown

These are floors rather than expected payoffs, and they are deliberately modest.
Because hedge payoff is convex in the size of the move, the gap between a floor
and what a book actually returns widens with depth: the
[convexity profile](../part-6/crash-convexity.md#convexity-profile) illustrates
one book delivering 5.0% at −20% and 21.0% at −30%. Set the schedule against
your own repriced book at each depth, not against a band quoted at another one.

## Implementation

Hedges are sized so that:

```text
Scenario Payoff ≥ Convexity Target
Expected Cost ≤ Premium Budget
```

This dual-constraint approach prevents two common problems:

- Overspending on hedges that rarely pay off
- Holding hedges that are too small to matter in a crash
