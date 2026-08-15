---
title: "Historical Crash Analysis"
---

Understanding past market crashes helps calibrate hedge programs.

Below are several major historical events.

## 1987 Crash

```text
SPX peak-to-trough decline ≈ −34%
single day collapse  ≈ −20%
volatility explosion
```

Deep OTM puts produced extremely large payoffs.

## 2008 Global Financial Crisis

```text
SPX decline ≈ −57%
volatility (VIX) > 80
extended drawdown
```

Long-dated put hedges performed strongly.

## 2020 COVID Crash

```text
SPX decline ≈ −34%
fastest bear market in history
VIX ≈ 85
```

Short-dated options increased in value dramatically.

## 2022 Bear Market

```text
SPX decline ≈ −25%
volatility moderately elevated
slower decline
```

This type of environment, (e.g., slow bear markets), can be challenging for hedges due to **volatility decay**. Slow bear markets with declining volatility are particularly challenging for long-dated put hedges.

The mechanism is counterintuitive: in a slow-grinding −25% decline, the put gains value from delta as the market falls but simultaneously loses value from two sources — ongoing theta decay as time passes, and vega compression as volatility fails to spike. If the decline takes 12 months rather than 12 days, the cumulative theta absorbed by the position can exceed the delta gains. The net result can be a hedge that is worth less at −25% in a slow decline than at −20% in a fast crash, because the fast crash delivers the vega spike that the slow decline does not. This is why the 2022 experience disappointed many hedgers despite a significant market decline: the absence of a volatility event was itself a source of hedge underperformance.
