---
title: "Forward Variance Level"
---

Forward variance measures **expected volatility in the future**. This is crucial for long-dated hedges.

## Concept of Forward Variance

Variance is volatility squared:

$Variance = \sigma^2$

Forward variance is implied volatility for a **future time window**.

| Option  | IV  |
| ------- | --- |
| 6-month | 22% |
| 2-year  | 19% |

This implies **lower expected volatility long term**.

## Approximation

The forward variance can be estimated between maturities.

Example:

$\sigma_{fwd}^2 = \frac{T_2\sigma_2^2 - T_1\sigma_1^2}{T_2 - T_1}$

## Interpretation of Forward Variance Level

Forward variance estimates the market's expectation of volatility
during a future time window rather than over the entire option maturity.

If long-dated volatility is unusually cheap:

```text
forward variance low
```

Long-dated puts become attractive.

## Hedge Decision Rule for Forward Variance Level

Tail funds often prefer buying:

```text
cheap long-dated vol
```

Because crashes inflate short-dated volatility sharply and usually pull long-dated volatility higher as well, although the magnitude of the repricing is typically smaller.
