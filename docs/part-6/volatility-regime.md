---
title: "Volatility Regime"
---

Volatility regime refers to the **general level and behavior of volatility in the market environment**. Markets cycle between low-volatility and high-volatility environments.

**Volatility level and skew typically interact**. When volatility rises sharply during crises, downside skew often steepens simultaneously as demand for crash protection increases.

#### Algebraic Framing of Vol Regime

Often measured using:

$\sigma_t$

realized or implied volatility.

Regime detection may use:

```text
moving averages
GARCH models
volatility percentiles
```

Example rule:

```text
Low vol regime: VIX < 15
Normal regime: VIX 15 to 25
High vol regime: VIX 25 to 40
Crisis vol regime: VIX > 40
```

*Example:*

| Period     | Regime    | VIX |
| ---------- | --------- | --- |
| 2017       | ultra low | 10  |
| 2020 crash | extreme   | 80  |
| 2022       | elevated  | 30  |

#### Portfolio Interpretation of Vol Regime

Volatility regimes influence:

```text
option prices
skew
carry cost
hedging effectiveness
```

In low-vol regimes:

```text
options cheap
good time to buy hedges
```

In high-vol regimes:

```text
options expensive
carry high
```

