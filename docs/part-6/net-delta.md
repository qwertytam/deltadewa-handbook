---
title: "Net Delta"
---

Delta represents the first derivative of option value with respect to the underlying price [[Wikipedia: Greeks]](../footnotes/index.md#wiki-greeks).

$\Delta = \frac{\partial V}{\partial S}$

**Net Delta** measures directional exposure of the entire portfolio to the underlying.

## Portfolio Metric

$\text{Net Delta} = \sum_i \Delta_i \times N_i$

Where:

- $N_i$ = number of contracts

*Example:*

```text
Equities: $10M
Equity delta: +1.0
Put hedge delta: -0.20
```

Net delta:

```text
1.0 - 0.20 = 0.80
```

Dollar effective exposure:

```text
$10M × 0.80 = $8M
```

## Interpretation of Net Delta

| Value | Meaning        |
| ----- | -------------- |
| 1.0   | fully exposed  |
| 0.8   | 20% hedge      |
| 0.0   | market neutral |
