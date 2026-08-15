---
title: "Tier 2 — Market Environment Metrics"
---

These determine when hedges are cheap or expensive. Useful, but not core.

#### 6. Volatility Regime Indicator

See [Volatility Regime](../part-6/volatility-regime.md) for definition details.

##### Dashboard Logic

Common indicators:

```text
VIX level
realized volatility
volatility percentile
```

```text
Volatility Regime: LOW
Recommendation: accumulate hedges
```

Low-volatility environments are often the best time to buy protection.

###### VIX Level

Most common regime indicator.

Example ranges:

| VIX      | Regime   |
| -------- | -------- |
| < 15     | low vol  |
| 15 to 25 | normal   |
| 25 to 40 | stressed |
| > 40     | crisis   |

###### Realized versus Implied Volatility

See [Volatility Risk Premium](../part-4/volatility-risk-premium.md)

##### Hedge Decision Rule for Vix

Volatility funds prefer to **buy protection when volatility is cheap**.

Typical rule:

| VIX      | Hedge action                 |
| -------- | ---------------------------- |
| < 15     | accumulate                   |
| 15 to 25 | maintain                     |
| 25 to 40 | partial reduction            |
| > 40     | more aggressive monetization |

#### 7. Skew Percentile Gauge

See [Skew Percentile](../part-3/volatility-skew.md#skew-percentile) for details.

##### Skew Percentile Dashboard Display

```text
LOW <----|-----[x]---------|------> HIGH
15%          Current                  85%
               40%
```

##### Hedge Decision Rule for Skew Percentile

Typical logic:

| Skew Percentile | Action                                          |
| --------------- | ----------------------------------------------- |
| < 30%           | add tail hedges in "*normal*" market conditions |
| 30 to 70%       | neutral                                         |
| > 70%           | avoid buying                                    |

When skew is high, **deep OTM puts become extremely expensive**.

#### 8. Forward Variance Level

See [Forward Variance Level](../part-6/forward-variance-level.md) for details.

