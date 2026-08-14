---
title: "Theta Carry / Insurance Cost"
---

Theta carry measures how much money the hedge costs to hold over time due to time decay. It is essentially the insurance premium paid to maintain protection.

#### Algebraic Framing of Theta Carry

Theta:

$\Theta = -\frac{\partial V}{\partial t}$

Theta carry is usually expressed relative to portfolio size:

$\text{Theta Carry} = \frac{-\Theta \times 252}{\text{Portfolio Value}}$

*Example:*

Portfolio:

```text
$10M
```

Hedge theta:

```text
-$2,500 per day
```

Annualized cost:

```text
-$2,500 × 252 ≈ -$630k → 6.3% of portfolio
```

Note: See See Theta Day Convention

#### Portfolio Interpretation

Good hedges try to balance:

```text
maximize crash convexity
minimize theta carry
```

See See Typical institutional targets.

