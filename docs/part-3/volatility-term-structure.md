---
title: "Volatility Term Structure"
---

Implied volatility varies across maturities:

$\sigma = \sigma(T)$

*Example:* “Near-term vol elevated vs LEAPS.”

```text
1-month vol = 15%
6-month vol = 18%
2-year vol = 20%
```

This is typically **upward sloping** in normal markets.

During crises the volatility term structure often inverts,
with short-dated volatility trading far above long-dated volatility.

Example (March 2020)

```text
1-month IV: 80%
1-year IV: 40%
```

This inversion dramatically increases the value of near-dated options and affects roll decisions. See [Volatility Roll Yield](../part-7/volatility-roll-yield.md) for how term structure shape determines the cost or benefit of rolling long-dated positions.
