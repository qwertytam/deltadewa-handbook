---
title: "Delta (Δ)"
---

Delta is the sensitivity of the option price to changes in the underlying price.

*Example:* “A 0.30 delta call moves ~\$0.30 per \$1 move in underlying.”

If the stock rises **\$1**, the option price increases **\$0.30**.

If the stock falls **\$1**, the option price decreases **\$0.30**.

| Underlying | Option price |
| ---------- | ------------ |
| \$100      | \$5.00       |
| \$101      | \$5.30       |

## Algebraic Definition

$\Delta = \frac{\partial V}{\partial S}$

## Meaning

> The partial derivative of the option price with respect to the underlying price.

## Black-Scholes expressions

Call option:  $\Delta_{call} = e^{-qT} N(d_1)$

Put option: $\Delta_{put} = -e^{-qT} N(-d_1)$

Where $N(\cdot)$ is the standard normal cumulative distribution function.

## Practical Interpretation

- Delta is sometimes interpreted as the risk-neutral probability of finishing ITM, but this approximation is most accurate for short-dated ATM options
- Properly, Delta corresponds to $N(d_1)$ while the true risk-neutral probability is $N(d_2)$ for calls and $N(-d_2)$ for puts
- Effective exposure to the underlying

Portfolio:

```text
100 calls
delta = 0.40
```

Total delta exposure: $100 \times 0.40 = 40$

Equivalent to owning 40 shares of the underlying.
