---
title: "Typical Hedge Program Targets"
---

Typical institutional allocations range between 1 to 3% annual carry. Very large macro funds may allocate 3 to 5%.

#### Typical Institutional Targets

Carry budget:        1 to 3% per year
Crash convexity:     10 to 25% @ -25% SPX
Offset ratio:        20 to 35%
Vega exposure:       \$1k to \$3k per \$1M portfolio
Skew exposure:       positive
Roll interval:       9 to 12 months

#### Typical Tail Hedge Structure

Strike ladder:

```text
35% allocation → 20% OTM strike puts
40% allocation → 30% OTM strike puts
25% allocation → 40% OTM strike puts
```

Tenor ladder:

```text
1/3 position opened every quarter
maintain 12 to 24 month maturity
```

#### Industry Context and Family Office Benchmarks

While the parameters above represent institutional tail fund practice, family office survey data suggests that in practice many family offices hedge at lower premium budgets.

| Program Type                             | Typical Annual Premium |
| ---------------------------------------- | ---------------------- |
| Family office (cost-sensitive)           | 0.5–1.5% of AUM        |
| Institutional tail program (deep OTM)    | 1.5–2.5%               |
| Institutional (richer / closer-to-money) | 3–5%+                  |

Many family offices consider 1% per year a practical ceiling given performance sensitivity to carry. The 1–3% range in this handbook represents a defensible institutional target, but programs should be calibrated to what the investor and their stakeholders will sustain across a multi-year bull market without abandoning the program.

#### Dynamic Calibration to the Volatility Regime

Strike selection and hedge sizing do not need to be static. A regime-sensitive approach:

| Vol Regime | Skew Percentile | Recommended Adjustment                                         |
| ---------- | --------------- | -------------------------------------------------------------- |
| VIX < 15   | < 30%           | Increase allocation; consider slightly closer-to-money strikes |
| VIX < 15   | > 50%           | Buy standard deep OTM; avoid chasing expensive skew            |
| VIX 15–25  | < 40%           | Maintain program as designed                                   |
| VIX > 25   | > 70%           | Reduce new purchases; wait for vol to normalize                |

This is consistent with the See [Tail Hedge Decision Matrix](../part-10/tail-hedge-decision-matrix.md) in PART X.

