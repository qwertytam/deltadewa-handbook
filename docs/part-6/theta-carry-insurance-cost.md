---
title: "Theta Carry / Insurance Cost"
---

Theta carry measures how much money the hedge costs to hold over time due to time decay. It is essentially the insurance premium paid to maintain protection.

See [Ratio Disambiguation](ratio-disambiguation.md) for how it differs from the
annual carry budget used in backtesting and from realized carry. Theta carry is
a forward-looking accrual off the current book; what a program actually spent
over a past period is measured instead by
[Realized Carry Methodology](../part-7/realized-carry-methodology.md), and the
two will not agree.

## Algebraic Framing of Theta Carry

Theta:

$\Theta = -\frac{\partial V}{\partial t}$

Theta carry is usually expressed relative to portfolio size:

$\text{Theta Carry} = \frac{-\Theta \times 365}{\text{Portfolio Value}}$

*Example:*

Portfolio:

```text
$10M
```

Hedge theta:

```text
-$550 per day
```

Annualized cost:

```text
-$550 × 365 ≈ -$201k → 2.0% of portfolio
```

The 365 multiplier is the calendar-day convention this handbook uses
throughout; see [Theta Day Convention](../part-2/theta.md#theta-day-convention)
for why, and check the basis of any theta you take off a platform before
annualizing it here.

At 2.0% of portfolio value this example sits inside the institutional carry
band; the bands themselves are owned by
[Annual Premium Budget Bands](../part-7/typical-hedge-program-targets.md#annual-premium-budget-bands).

## Portfolio Interpretation

Good hedges try to balance:

```text
maximize crash convexity
minimize theta carry
```

See [Typical institutional targets](../part-7/typical-hedge-program-targets.md#typical-institutional-targets).
