---
title: "Structure 2 — Put Spread Tail Hedge"
---

Structure

```text
buy deep OTM put
sell further OTM put
```

Example:

```text
buy 3500 put
sell 2500 put
```

## Purpose

Reduce cost relative to an outright long put at the same strike, by selling a
further OTM put against it. How much the spread reduces carry depends on how
close the sold strike sits to the long strike — see
[Annual Premium Budget Bands](../part-7/typical-hedge-program-targets.md#annual-premium-budget-bands)
for the ranges programs budget to, and
[Convexity Budget and Premium Budget](../part-7/convexity-budget-and-premium-budget.md)
for how strike distance drives that figure.

Trade-off:

```text
cap extreme crash payoff
```

The capped payoff is the visible trade-off. The sold leg also consumes
collateral for as long as the position is open, must be bought back to monetise
the structure, and gives back part of the crash repricing that the long leg
earns. See [Running Structures with Sold Legs](running-structures-with-sold-legs.md).
