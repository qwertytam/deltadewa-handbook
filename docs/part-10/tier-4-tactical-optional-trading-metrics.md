---
title: "Tier 4 — Tactical / Optional Trading Metrics"
---

These are not really tail-hedging metrics. For example, dealer gamma is short-term flow information, not structural hedge design. Most institutional tail programs do not include it on core dashboards.

## 12. Liquidity Risk

See [Liquidity Risk / Spread](../part-4/liquidity-risk-spread.md) for definition details.

### Liquidity Risk Metrics

Common liquidity indicators:

#### Bid-ask spread

```text
Spread % = (Ask − Bid) / Mid
```

```text
Bid = 2.40
Ask = 2.60
```

Spread:

```text
0.20
```

#### Market depth

Contracts available near the mid price.

#### Open interest

```text
OI per strike
```

#### Trading volume

```text
Average daily volume
```

### Liquidity Risk Interpretation

Warning signs:

```text
wide bid-ask spreads
low open interest
thin order books
```

Liquidity risk matters most when:

```text
monetizing hedges during crashes
rolling positions
scaling hedge size
```

## 13. Delta Drift { #13-delta-drift }

### Delta Drift Definition

Delta drift measures how quickly the hedge’s delta becomes more negative as markets fall. This captures early-stage protection before a full crash occurs.

It answers:
> How quickly does the hedge begin offsetting losses?

### Delta Drift Metric { #delta-drift-metric }

Compute the change in hedge delta across small price moves.

Let:

```text
Δ0 = hedge delta today
Δ5 = hedge delta if market falls 5%
```

Define:

```text
Delta Drift = Δ5 − Δ0
```

Example:

```text
Current hedge delta = −0.08
Delta if SPX −5% = −0.18
Delta Drift = −0.10
```

### Delta Drift Interpretation

| Drift magnitude | Meaning                                |
| --------------- | -------------------------------------- |
| small           | hedge only activates in deep crashes   |
| moderate        | hedge begins protecting in corrections |
| large           | hedge responds early                   |

Tail-risk strategies often accept slower delta drift in exchange for cheaper carry.

## 14. Vega Term Exposure

### Vega Term Exposure Definition

Vega term exposure measures how hedge sensitivity to volatility is distributed across maturities. Volatility spikes often affect multiple parts of the term structure, so hedge exposure across maturities matters.

It answers:
> Which part of the volatility curve does the hedge benefit from?

### Vega Term Exposure Metric

Aggregate vega by maturity bucket:

Example:

```text
1-year vega = $8k / vol point
2-year vega = $14k / vol point
3-year vega = $6k / vol point
```

The same buckets can be normalised by portfolio value, which is the metric
defined as [Vega Sufficiency](../part-6/vega-sufficiency.md) in PART VI. What
this panel adds is the distribution across maturities, not a second definition.

### Vega Term Exposure Interpretation

Different structures produce different exposures:

| Hedge structure     | Vega exposure                    |
| ------------------- | -------------------------------- |
| short-dated options | concentrated near front of curve |
| LEAPS               | long-dated vega                  |
| mixed ladder        | balanced exposure                |

Institutional tail hedges typically prefer:

```text
long-dated vega exposure
```

This is because crisis volatility often lifts long-dated implied volatility as well.

## 15. Hedge Efficiency Ratio

See [Hedge Efficiency Ratio](../part-6/hedge-efficiency-ratio.md) for details.
