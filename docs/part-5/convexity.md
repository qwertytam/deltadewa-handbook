---
title: "Convexity"
---

#### Convexity Definition

Convexity describes **non-linear payoff behavior** where gains accelerate as the underlying moves further.

In linear instruments such as equities or futures:

```text
P&L moves proportionally with price.
```

In options portfolios:

```text
P&L can accelerate as the underlying moves further.
```

This non-linear payoff structure is called convexity.

Convexity in tail hedging is primarily a portfolio-level concept rather than a local option Greek. It reflects the combined impact of gamma, vega expansion, and skew repricing during large market moves.

Convex strategies benefit from extreme moves in the benchmark index [[Informa Connect]](../footnotes/index.md#informaconnect).

##### Example Tail Hedge Payoff Structure

| Market move | Hedge P&L     |
| ----------- | ------------- |
| −5%         | small gain    |
| −15%        | moderate gain |
| −30%        | large gain    |
| -40%        | very large    |

#### Convexity in Tail-Hedging

Convexity can be defined in two different ways:

1. Mathematical convexity (gamma)
   > The second derivative of option value with respect to price.

2. Crash convexity (portfolio concept)
   > The scenario payoff acceleration during large market declines.

In tail-hedging practice, convexity usually refers to the second concept
because investors care about crisis payoff rather than instantaneous gamma.

#### Sources of Convexity

In options portfolios, convexity arises primarily from **gamma**, which causes delta exposure to increase as the underlying moves.

However, during market crises additional effects amplify the payoff of tail hedges:

```text
delta acceleration (gamma)
+ volatility expansion (vega)
+ skew steepening
```

Because of these interacting effects, the performance of crash hedges is not determined by gamma alone.

Skew contributes to convexity, but convexity is **not the same thing as skew**.

#### Convexity versus Skew

| Concept   | Meaning                                   |
| --------- | ----------------------------------------- |
| Convexity | accelerating hedge payoff as market falls |
| Skew      | relative price of downside options        |
| Skew beta | hedge sensitivity to skew changes         |

#### Convexity Budget

Many institutional tail-hedge programs manage hedges using a
convexity budget rather than a fixed notional allocation.

The convexity budget specifies the expected hedge payoff
under defined crash scenarios (for example a −20% equity shock).

This approach ensures the hedge program is calibrated
to the portfolio’s true downside risk rather than
arbitrary premium spending.

For how convexity targets are used to size hedge programs, see See [Convexity Budget and Premium Budget](../part-7/convexity-budget-and-premium-budget.md) in PART VII.

#### Practical Value of Convexity

For a tail-hedge program, convexity is what allows the hedge to:

```text
produce modest gains in moderate selloffs
but very large gains in severe crashes
```

This property makes convex hedges valuable because they can:

```text
offset deep portfolio drawdowns
provide liquidity during crises
fund rebalancing into cheap assets
```

In practice, convexity is not measured using instantaneous gamma.
Instead, hedge programs evaluate **crash convexity** using scenario analysis, which estimates hedge performance under large market declines.

