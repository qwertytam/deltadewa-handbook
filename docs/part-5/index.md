---
title: "Tail-Hedging Concepts and Structures"
---

The goal of tail hedging is **not to eliminate volatility or offset small drawdowns**. The goal is to create **liquidity during crises**. This liquidity allows the investor to rebalance by buying heavily sold equities and avoid forced selling.

During a crash, the hedge produces cash (liquidity) that can be used by investors to:

```text
rebalance
buy equities cheaply
avoid forced selling
```

This is why many institutional investors treat tail hedges as a **strategic portfolio allocation**, not a tactical trade.

For a hedged equity portfolio, key metrics to track are:

| Metric                                       | What it answers                        |
| -------------------------------------------- | -------------------------------------- |
| See [Crash Convexity](../part-6/crash-convexity.md)          | How much protection in a crash         |
| See [Vega Sufficiency](../part-6/vega-sufficiency.md)        | If the hedge benefits from vol spikes  |
| See [Theta Carry](../part-6/theta-carry-insurance-cost.md)  | Cost of holding hedge                  |
| See [Skew Exposure / Beta](../part-6/skew-exposure-beta.md) | Sensitivity to downside skew           |
| See [Volatility Regime](../part-6/volatility-regime.md)      | Whether options are expensive or cheap |

Professional hedge design is essentially optimizing:

```text
maximize crash convexity
maximize vega sufficiency
maximize skew beta
minimize theta carry
```

given the current volatility regime.

