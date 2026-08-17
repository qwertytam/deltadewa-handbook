---
title: "Net Delta"
---

Delta represents the first derivative of option value with respect to the underlying price [[Wikipedia: Greeks]](../footnotes/index.md#wiki-greeks).

$\Delta = \frac{\partial V}{\partial S}$

**Net Delta** measures directional exposure of the entire portfolio to the underlying.

## Portfolio Metric

Net delta is measured first in dollars of underlying exposure:

$\text{Net Delta}_\$ = \sum_i \Delta_i \times N_i \times m$

Where:

- $\Delta_i$ = delta of position $i$
- $N_i$ = number of contracts in position $i$
- $m$ = contract multiplier, typically 100

Expressed as a fraction of portfolio value, this gives the blended portfolio delta used in the interpretation table below:

$\text{Net Delta} = \frac{\text{Net Delta}_\$}{\text{Portfolio Value}}$

*Example:*

A \$10M equity portfolio hedged with 20 SPX puts at a delta of −0.20, with SPX at 5,000:

```text
Equity dollar delta:     $10M × 1.0                  = +$10.0M
Put hedge dollar delta:  -0.20 × 20 × 100 × 5,000    = -$2.0M
```

Net delta in dollars:

```text
$10.0M - $2.0M = $8.0M
```

As a fraction of portfolio value:

```text
$8M / $10M = 0.80
```

The 20-contract hedge is the same position sized in [Beta-Adjusted Hedge Sizing](../part-7/beta-adjusted-hedge-sizing.md), where each SPX contract covers \$500,000 of notional at SPX 5,000.

## Interpretation of Net Delta

| Value | Meaning        |
| ----- | -------------- |
| 1.0   | fully exposed  |
| 0.8   | 20% hedge      |
| 0.0   | market neutral |
