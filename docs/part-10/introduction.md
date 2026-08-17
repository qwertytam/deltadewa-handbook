---
title: "Introduction"
---

These are the kinds of metrics volatility funds and institutional portfolio hedgers monitor daily. They combine the Greeks with **portfolio-level normalization**.

These metrics help investors maintain **constant protection while controlling cost**, since tail-risk hedging aims to cushion severe drawdowns while preserving long-term portfolio growth [[Resonanz Capital]](../footnotes/index.md#resonanzcapital).

## Metric Prioritization

There are many possible metrics to include. The full list below is prioritized by *Tier*.

An alternative take is this list of six:

1. Carry vs Convexity
2. Crash Scenario Table
3. Vega Sufficiency
4. Skew Exposure
5. Volatility Regime
6. Hedge Efficiency

## Example of a Full Dashboard

```text
TAIL HEDGE DASHBOARD

Portfolio value: $10M

Carry cost:             2.1% / year
Crash convexity:        28% @ -25% SPX
Hedge efficiency ratio: 13.3
Vega exposure:          $18k / vol point
Skew exposure:          High
Skew percentile:        22%  (cheap)
Vol regime:             Low (VIX 14)
Forward variance:       cheap
Dealer gamma:           negative
```

The efficiency ratio is the two lines above it divided out — 28% of crash
convexity against 2.1% of annual carry. It is one line item, not two: see
[Ratio Disambiguation](../part-6/ratio-disambiguation.md) for why
"convexity/carry ratio" and "hedge efficiency" name the same quantity.

Conclusion:

```text
increase hedge allocation
```

## Key Driver of the Dashboard

The **best opportunities to buy crash protection** typically occur when:

```text
market calm
volatility low
skew moderate
```

Investor's instinct is to hedge **after markets fall**, but that is when hedges are **most expensive**.
