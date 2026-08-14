---
title: "Delta-Based Strike Selection"
---

Delta-based strikes adapt better to changing vol regimes than fixed moneyness alone. This is how many professional options desks actually think about and quote strike selection.

Common rule:

```text
choose strikes by delta rather than price distance
```

Example:

| Delta          | Approx Strike |
| -------------- | ------------- |
| 25$\Delta$ put | ~10% OTM      |
| 10$\Delta$ put | ~20% OTM      |
| 5$\Delta$ put  | ~30% OTM      |

Deep OTM puts provide **maximum skew beta**.

Note that this delta-to-moneyness mapping table is highly regime-dependent. At VIX = 12, a 25-delta put on a 1-year horizon is roughly 7 to 9% OTM. At VIX = 25, the same delta corresponds to 14 to 18% OTM. The table approximations assume a specific IV regime.

#### Delta Sweet Spot: Balancing Cost and Coverage

For a single protective put, a delta of approximately 0.30 often represents a practical balance between coverage and cost — particularly for shorter-dated hedges (3 to 12 months) or investors new to protective puts.

| Delta range | Characteristic                    | Trade-off                                                                        |
| ----------- | --------------------------------- | -------------------------------------------------------------------------------- |
| > 0.40      | High coverage, immediate response | Expensive; option behaves increasingly like a stock replacement                  |
| ~0.30       | Balanced cost and protection      | Good gamma exposure; activates meaningfully in moderate corrections              |
| 0.10–0.15   | Deep OTM, high skew beta          | Lower carry; only activates in larger moves — appropriate for pure tail programs |
| < 0.10      | Very deep OTM                     | Minimal protection in moderate drawdowns; optimized for catastrophic scenarios   |

For **systematic long-dated tail programs**, the typical emphasis is on the 0.05 to 0.15 delta range — lower delta, lower carry, maximum crash convexity. The 0.30 delta level is more appropriate for tactical near-term hedges where coverage of moderate corrections is a priority.

Note that delta changes continuously as price moves (this is gamma). A put bought at 0.30 delta will drift toward zero delta as the market rallies, which is part of why the strike drift trigger and rolling rules are essential for maintaining meaningful protection over time.

